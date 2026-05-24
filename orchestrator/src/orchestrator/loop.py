"""Main cycle loop and meta-review handshake."""

from __future__ import annotations

import asyncio
import json
import time
from dataclasses import asdict, is_dataclass
from datetime import date, datetime, timezone
from pathlib import Path

from anthropic import Anthropic

from .config import Config
from .log_entry import format_cycle_entry, format_meta_review_entry, prepend_log_entry
from .mcp_client import CodemapClient
from .roles import (
    TokenUsage,
    call_critic,
    call_explorer,
    call_meta_critic,
    call_planner,
    call_synthesizer,
)
from .schemas import SchemaSet, load_schemas
from .state import State


def _next_cycle_id(state: State) -> int:
    entries = state.read_episodic_window(10_000)
    if not entries:
        return 1
    max_id = 0
    for e in entries:
        if isinstance(e.get("cycle_id"), int):
            max_id = max(max_id, e["cycle_id"])
    return max_id + 1


def _prefetch_citations_from_claims(
    state: State,
    claims: list[dict],
) -> dict[str, str]:
    """For each citation referenced by a rotation claim, fetch the source
    text via direct file read (the Critic shouldn't need to call MCP)."""
    out: dict[str, str] = {}
    # rotation_claims don't directly carry citations — they're string from_form
    # / to_form. The Critic will work from the diff + claim text. The "cited
    # source" prefetch matters more in v2 when claims carry explicit
    # citation_indices. For now we return empty; the Critic message includes
    # the diff itself which references file paths.
    return out


async def run_normal_cycle(
    *,
    cfg: Config,
    state: State,
    schemas: SchemaSet,
    client: Anthropic | None,
    mcp_client: CodemapClient | None,
    dry_run: bool = False,
) -> bool:
    """Run one normal cycle: Planner → Explorer/Synthesizer → Critic →
    writes → commit. Returns True if the cycle completed; False on escalate.
    """
    state.cycle_id = _next_cycle_id(state)
    start = time.monotonic()
    total_usage = TokenUsage()

    push = call_planner(state=state, cfg=cfg, client=client, dry_run=dry_run)
    print(f"[cycle {state.cycle_id}] planner: {push}")

    if push["kind"] == "escalate":
        entry = format_cycle_entry(
            cycle_id=state.cycle_id,
            push_kind="escalate",
            slice_name="-",
            edge=None,
            verdict="escalate",
            synthesis=push.get("reason", "no productive next push"),
            friction="Planner could not find a productive push",
            structural_change=None,
        )
        commit_msg = f"cycle: escalate → {push.get('reason', 'no productive push')}"
        if dry_run:
            print(f"[dry-run] would record escalate: {commit_msg}")
        else:
            state.append_episodic({
                "cycle_id": state.cycle_id,
                "push_kind": "escalate",
                "verdict": "escalate",
                "reason": push.get("reason", ""),
                "friction_observed": "Planner emitted escalate; no productive next push found.",
                "structural_change": "",
                "push_back_signals": [],
                "concepts_touched": [],
                "tokens_in": total_usage.input_tokens,
                "tokens_out": total_usage.output_tokens,
                "wallclock_ms": int((time.monotonic() - start) * 1000),
            })
            prepend_log_entry(state.repo_root, entry)
            state.commit(commit_msg)
        return False

    slice_name = push.get("slice", "unknown")
    edge = None
    finding: dict | None = None

    # ─────── role calls ───────
    if push["kind"] == "forward":
        from_layer = push.get("from", "L0")
        to_layer = push.get("to", "L1")
        edge = f"{from_layer}→{to_layer}"
        if to_layer == "L1":
            scope_q = push.get("scope_question", "(no scope provided)")
            finding, ex_usage = await call_explorer(
                state=state,
                cfg=cfg,
                client=client,
                mcp_client=mcp_client,
                schemas=schemas,
                slice_name=slice_name,
                scope_question=scope_q,
                dry_run=dry_run,
            )
            total_usage.input_tokens += ex_usage.input_tokens
            total_usage.output_tokens += ex_usage.output_tokens

    diff, claims, syn_usage = call_synthesizer(
        state=state,
        cfg=cfg,
        client=client,
        schemas=schemas,
        finding=finding,
        edge=edge or "L0→L1",
        slice_name=slice_name,
        dry_run=dry_run,
    )
    total_usage.input_tokens += syn_usage.input_tokens
    total_usage.output_tokens += syn_usage.output_tokens

    cited_source = _prefetch_citations_from_claims(state, claims)
    verdict, cr_usage = call_critic(
        state=state,
        cfg=cfg,
        client=client,
        schemas=schemas,
        claims=claims,
        cited_source=cited_source,
        diff=diff,
        dry_run=dry_run,
    )
    total_usage.input_tokens += cr_usage.input_tokens
    total_usage.output_tokens += cr_usage.output_tokens
    print(f"[cycle {state.cycle_id}] critic verdict: {verdict['verdict']}")

    # ─────── writes ───────
    # In dry-run mode: log what WOULD happen but skip all persistent state
    # mutation (no diff apply, no episodic append, no LOG prepend, no commit).
    push_back_signals: list[str] = []
    if verdict["verdict"] == "pass":
        if diff.strip():
            if dry_run:
                print(f"[dry-run] would apply diff ({diff.count(chr(10))} lines)")
            else:
                try:
                    state.apply_unified_diff(diff)
                except RuntimeError as e:
                    push_back_signals.append(f"diff-apply failed: {e}")
    else:
        for issue in verdict.get("issues", []):
            if issue.get("kind") == "labored_rotation_push_back_candidate":
                push_back_signals.append(issue.get("description", ""))

    if verdict.get("lesson"):
        if dry_run:
            print(f"[dry-run] would append lesson: {verdict['lesson']!r}")
        else:
            state.append_lessons(verdict["lesson"])

    friction_summary = ""
    if push_back_signals:
        friction_summary = "; ".join(push_back_signals)
    elif verdict["verdict"] != "pass":
        friction_summary = f"verdict={verdict['verdict']}, {len(verdict.get('issues', []))} issue(s)"

    structural_change = ""
    if verdict["verdict"] == "pass" and diff.strip():
        structural_change = f"applied diff ({diff.count(chr(10))} lines); {len(claims)} rotation_claim(s)"

    episodic_entry = {
        "cycle_id": state.cycle_id,
        "push_kind": push["kind"],
        "slice": slice_name,
        "edge": edge,
        "verdict": verdict["verdict"],
        "friction_observed": friction_summary,
        "structural_change": structural_change,
        "push_back_signals": push_back_signals,
        "concepts_touched": [],  # v2 — extract from diff
        "tokens_in": total_usage.input_tokens,
        "tokens_out": total_usage.output_tokens,
        "wallclock_ms": int((time.monotonic() - start) * 1000),
    }
    log_entry = format_cycle_entry(
        cycle_id=state.cycle_id,
        push_kind=push["kind"],
        slice_name=slice_name,
        edge=edge,
        verdict=verdict["verdict"],
        synthesis=(
            f"{len(claims)} rotation_claim(s); "
            f"{'diff applied' if (verdict['verdict']=='pass' and diff.strip()) else 'no diff applied'}"
        ),
        friction=friction_summary or None,
        structural_change=structural_change or None,
    )
    commit_msg = (
        f"cycle: {push['kind']} {slice_name}{f' [{edge}]' if edge else ''} → {verdict['verdict']}"
    )

    if dry_run:
        print(f"[dry-run] would append episodic: cycle_id={state.cycle_id}, verdict={verdict['verdict']}")
        print(f"[dry-run] would prepend LOG.md: {log_entry.splitlines()[0]}")
        print(f"[dry-run] would commit: {commit_msg}")
    else:
        state.append_episodic(episodic_entry)
        prepend_log_entry(state.repo_root, log_entry)
        state.commit(commit_msg)
    return True


def _render_plan_md(plan: dict) -> str:
    return (
        f"# Meta-review pending — {plan['meta_review_date']}\n\n"
        f"**Cycles covered:** {plan['cycles_covered']}\n\n"
        f"## Categorized issues\n\n"
        f"- **LOW** ({len(plan['categorized_issues'].get('low', []))}): "
        + "; ".join(plan["categorized_issues"].get("low", [])) + "\n"
        f"- **MEDIUM** ({len(plan['categorized_issues'].get('medium', []))}): "
        + "; ".join(plan["categorized_issues"].get("medium", [])) + "\n"
        f"- **HIGH** ({len(plan['categorized_issues'].get('high', []))}): "
        + "; ".join(plan["categorized_issues"].get("high", [])) + "\n\n"
        f"## Direct actions (LOW) — would be applied on approval\n\n"
        + "\n".join(
            f"- `{a['file']}`: {a['change_summary']} ({a['issue']})"
            for a in plan.get("direct_actions", [])
        )
        + "\n\n"
        f"## Plan items (MEDIUM) — require approval\n\n"
        + "\n".join(
            f"- **{p['issue']}**\n  - file: `{p['proposed_change'].get('file', '?')}`\n"
            f"  - edit: {p['proposed_change'].get('edit_description', '?')}\n"
            f"  - cascade trace: " + "; ".join(p.get('cascade_trace', [])) + "\n"
            f"  - risk: {p.get('risk_notes', '')}"
            for p in plan.get("plan_items", [])
        )
        + "\n\n"
        f"## Escalations (HIGH) — surfaced; not proposed\n\n"
        + "\n".join(
            f"- **{e['issue']}** — {e['why_high']}"
            for e in plan.get("escalations", [])
        )
        + "\n\n"
        f"## Full plan JSON\n\n```json\n{json.dumps(plan, indent=2)}\n```\n\n"
        f"---\n\n"
        f"APPROVAL: pending\n\n"
        f"<!-- To approve and enact the LOW+MEDIUM items, change the line above to `APPROVAL: APPROVED`. -->\n"
        f"<!-- To reject and discard the plan, change to `APPROVAL: REJECTED`. -->\n"
        f"<!-- Then re-invoke the orchestrator. -->\n"
    )


def _approval_status(pending_text: str) -> str:
    """Returns 'pending' | 'APPROVED' | 'REJECTED' based on the marker line."""
    for line in pending_text.splitlines():
        if line.startswith("APPROVAL:"):
            return line.split(":", 1)[1].strip()
    return "pending"


async def run_meta_review(
    *,
    cfg: Config,
    state: State,
    schemas: SchemaSet,
    client: Anthropic | None,
    dry_run: bool = False,
) -> bool:
    """Pause-the-world meta-review. Returns True if completed (approved or
    rejected), False if waiting on human approval (handshake pending)."""

    pending = state.read_meta_review_pending()
    if pending is not None:
        status = _approval_status(pending)
        if status == "pending":
            print("[meta-review] handshake pending — see meta-review-pending.md")
            return False
        if status == "REJECTED":
            print("[meta-review] rejected by human; clearing handshake")
            state.clear_meta_review_pending()
            # Log the rejection
            entry = format_meta_review_entry(
                review_date=date.today().isoformat(),
                cycle_range=(0, state.cycle_id),
                status="rejected",
                push_breakdown="(see episodic.jsonl)",
                cascade_breakdown="0 LOW applied; 0 MEDIUM (rejected); 0 HIGH",
                plan_items_summary="rejected by human",
                recurring_patterns=None,
                record_path="(no record written — plan rejected)",
            )
            prepend_log_entry(state.repo_root, entry)
            state.append_episodic({
                "cycle_id": state.cycle_id,
                "push_kind": "meta",
                "verdict": "rejected",
                "friction_observed": "meta-review plan rejected by human",
                "structural_change": "",
                "push_back_signals": [],
                "tokens_in": 0,
                "tokens_out": 0,
            })
            state.commit("meta-review: plan rejected")
            return True
        if status == "APPROVED":
            print("[meta-review] approved by human; enactment is manual in v1 — "
                  "apply LOW/MEDIUM items by hand, then clear meta-review-pending.md")
            # v1: enactment is human-driven. The orchestrator records the
            # approval and the human applies edits manually (then commits and
            # clears the pending file). This is the conservative path —
            # automated enactment is a Phase 9+ concern.
            return False

    # No pending file → produce a fresh plan
    cycle_count = state.count_cycles_since_meta()
    cycles_covered = list(range(state.cycle_id - cycle_count + 1, state.cycle_id + 1))
    plan, usage = call_meta_critic(
        state=state,
        cfg=cfg,
        client=client,
        schemas=schemas,
        cycles_covered=cycles_covered,
        dry_run=dry_run,
    )

    plan_md = _render_plan_md(plan)
    pending_path = state.write_meta_review_pending(plan_md)
    print(f"[meta-review] plan written to {pending_path.relative_to(state.repo_root)}; "
          f"awaiting APPROVAL marker.")
    return False


async def main_loop_async(
    *,
    cfg: Config,
    state: State,
    schemas: SchemaSet,
    client: Anthropic | None,
    mcp_binary: Path | None,
    config_path: Path,
    one_cycle: bool,
    meta_only: bool,
    dry_run: bool,
) -> None:
    """Top-level entry. Holds the MCP client open for the duration."""

    if mcp_binary is None or dry_run:
        mcp_ctx = None
    else:
        mcp_ctx = CodemapClient(mcp_binary, config_path)

    async def with_mcp(coro):
        if mcp_ctx is None:
            return await coro(None)
        async with mcp_ctx as cmc:
            return await coro(cmc)

    if meta_only:
        await with_mcp(lambda _: run_meta_review(
            cfg=cfg, state=state, schemas=schemas, client=client, dry_run=dry_run,
        ))
        return

    # Run one or more normal cycles, firing meta-review at the configured cadence.
    while True:
        # Check pending meta-review handshake first
        if state.read_meta_review_pending() is not None:
            done = await run_meta_review(
                cfg=cfg, state=state, schemas=schemas, client=client, dry_run=dry_run,
            )
            if not done:
                return  # waiting on human

        await with_mcp(lambda cmc: run_normal_cycle(
            cfg=cfg, state=state, schemas=schemas,
            client=client, mcp_client=cmc, dry_run=dry_run,
        ))

        # Check meta-review trigger
        if state.count_cycles_since_meta() >= cfg.meta_review_every_n_cycles:
            done = await run_meta_review(
                cfg=cfg, state=state, schemas=schemas, client=client, dry_run=dry_run,
            )
            if not done:
                return  # waiting on human

        if one_cycle:
            return


def main_loop(**kwargs) -> None:
    asyncio.run(main_loop_async(**kwargs))
