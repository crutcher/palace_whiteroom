"""Main cycle loop and meta-review handshake."""

from __future__ import annotations

import asyncio
import json
import subprocess
import sys
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


_SAFE_CREATE_PREFIXES = (
    "book/src/",
    "scaffolding/",
    "problems/",
)


def _is_safe_create_path(rel: str) -> bool:
    """True iff `rel` is a path the agent loop is allowed to create directly.

    Safe prefixes: book/src/, scaffolding/, problems/. The cycle commits
    apply only to CYCLE_OWNED_PATHS (per state.py); creating outside those
    paths would be staged-but-not-committed, OR worse, written into
    infrastructure code the loop must not modify.

    Also rejects path traversal (`..`), absolute paths, and empty paths.
    """
    if not rel or rel.startswith("/") or ".." in rel.split("/"):
        return False
    return any(rel.startswith(p) for p in _SAFE_CREATE_PREFIXES)


def _summarize_plan_for_critic(plan: dict) -> str:
    """Build a text rendering of the plan's writes for the Critic to verify.
    The Critic doesn't see the structured plan; it sees a readable summary
    of what the plan will do (concept-writes, slice-writes paths and modes,
    plus the diff strings if any). This preserves the Critic's existing
    `diff` input contract while the underlying plan is structured."""
    chunks: list[str] = []
    for sw in plan.get("slice_writes", []) or []:
        path = sw.get("path", "?")
        mode = sw.get("mode", "create")
        if mode == "create":
            content = sw.get("content", "")
            chunks.append(f"=== slice create: book/src/spec/slices/{path} ({len(content)} bytes) ===\n{content}")
        elif mode == "diff":
            chunks.append(f"=== slice diff: {path} ===\n{sw.get('diff', '')}")
    for cw in plan.get("concept_writes", []) or []:
        name = cw.get("name", "?")
        mode = cw.get("mode", "create")
        content = cw.get("content", "")
        chunks.append(f"=== concept {mode}: book/src/concepts/{name}.md ({len(content)} bytes) ===\n{content}")
    if plan.get("dependency_map_edges"):
        edges = plan["dependency_map_edges"]
        chunks.append(
            "=== dependency_map_edges ===\n"
            + "\n".join(f"{e.get('layer','?')}: {e.get('from','?')} -> {e.get('to', [])}" for e in edges)
        )
    if plan.get("lessons"):
        chunks.append(
            "=== lessons (append-dedupe) ===\n"
            + "\n".join(f"- {l}" for l in plan["lessons"])
        )
    if plan.get("log_synthesis"):
        chunks.append(f"=== log_synthesis ===\n{plan['log_synthesis']}")
    return "\n\n".join(chunks)


def _summarize_plan_dry_run(plan: dict) -> None:
    sw_count = len(plan.get("slice_writes") or [])
    cw_count = len(plan.get("concept_writes") or [])
    de_count = len(plan.get("dependency_map_edges") or [])
    le_count = len(plan.get("lessons") or [])
    print(
        f"[dry-run] would apply integration plan: "
        f"{sw_count} slice_writes, {cw_count} concept_writes, "
        f"{de_count} dependency_map_edges, {le_count} lessons"
    )


# Bookkeeping paths: the index/TOC files whose failure should NOT downgrade
# a content-pass verdict (per meta-review #9 item 2). When ALL failed writes
# target these paths AND at least one substantive write succeeded, the
# orchestrator records `bookkeeping_incomplete` and leaves the verdict alone;
# the next cycle on the same slice should re-attempt the bookkeeping write.
_BOOKKEEPING_PATHS = (
    "book/src/spec/index.md",
    "book/src/meta-reviews/index.md",
    "book/src/SUMMARY.md",
)


def _is_bookkeeping_path(rel: str) -> bool:
    """True if the given repo-relative path is a bookkeeping (index/TOC)
    file rather than substantive content. See meta-review #9 item 2."""
    return any(rel == p or rel.startswith(p + "#") for p in _BOOKKEEPING_PATHS)


def _apply_integration_plan(state: State, plan: dict, push_back_signals: list[str]) -> dict:
    """Apply an integration plan to the project surface. Mutates state via
    State's helpers. Appends any errors to push_back_signals.

    Returns a result dict with keys:
      - apply_failed: True iff any write failed.
      - substantive_landed: count of non-bookkeeping writes that succeeded
        (slice creates, concept creates, section_appends to non-index files,
        non-index file_edits, dep-map edges, lessons).
      - failed_paths: list of {kind, path} for each failed write (used by the
        caller to classify bookkeeping vs content failures).
      - bookkeeping_only_failure: True iff at least one substantive write
        succeeded AND all failed writes targeted bookkeeping paths. Caller
        uses this to skip the verdict downgrade per meta-review #9 item 2.
    """
    apply_failed = False
    substantive_landed = 0
    failed_paths: list[dict] = []

    def _record_fail(kind: str, path: str) -> None:
        nonlocal apply_failed
        apply_failed = True
        failed_paths.append({"kind": kind, "path": path})

    def _record_success(path: str) -> None:
        nonlocal substantive_landed
        if not _is_bookkeeping_path(path):
            substantive_landed += 1

    # 1. slice_writes
    for sw in plan.get("slice_writes") or []:
        rel = sw.get("path", "")
        if not rel:
            push_back_signals.append("slice_write rejected: missing path")
            _record_fail("slice_write", "<missing>")
            continue
        full_rel = f"book/src/spec/slices/{rel.lstrip('/')}"
        if not _is_safe_create_path(full_rel):
            push_back_signals.append(f"slice_write rejected (unsafe path): {full_rel!r}")
            _record_fail("slice_write", full_rel)
            continue
        mode = sw.get("mode", "create")
        full_path = state.repo_root / full_rel
        if mode == "create":
            if full_path.exists():
                push_back_signals.append(
                    f"slice_write rejected (path exists; use mode=diff): {full_rel}"
                )
                _record_fail("slice_write", full_rel)
                continue
            try:
                content = sw.get("content", "")
                full_path.parent.mkdir(parents=True, exist_ok=True)
                if not content.endswith("\n"):
                    content += "\n"
                full_path.write_text(content)
                _record_success(full_rel)
                title = sw.get("title") or rel.removesuffix(".md").replace("_", " ")
                try:
                    state.register_in_summary(
                        category="slice",
                        link_title=title,
                        rel_path=f"./spec/slices/{rel.lstrip('/')}",
                    )
                except Exception as e_reg:
                    push_back_signals.append(f"slice auto-register failed for {full_rel}: {e_reg}")
            except Exception as e:
                push_back_signals.append(f"slice_write create failed for {full_rel}: {e}")
                _record_fail("slice_write", full_rel)
        elif mode == "diff":
            try:
                state.apply_unified_diff(sw.get("diff", ""))
                _record_success(full_rel)
            except RuntimeError as e:
                push_back_signals.append(f"slice_write diff failed for {full_rel}: {e}")
                _record_fail("slice_write", full_rel)
        else:
            push_back_signals.append(f"slice_write unknown mode {mode!r}")
            _record_fail("slice_write", full_rel)

    # 2. concept_writes
    for cw in plan.get("concept_writes") or []:
        name = cw.get("name", "")
        mode = cw.get("mode", "")
        content = cw.get("content", "")
        concept_rel = f"book/src/concepts/{name}.md"
        if not name or "/" in name or name.startswith("."):
            push_back_signals.append(f"concept_write rejected (bad name): {name!r}")
            _record_fail("concept_write", concept_rel)
            continue
        try:
            if mode == "create":
                created = state.create_concept_file(name, content)
                if not created:
                    push_back_signals.append(
                        f"concept_write create skipped (already exists; use append-section): {name}"
                    )
                else:
                    _record_success(concept_rel)
                    try:
                        state.register_in_summary(
                            category="concept",
                            link_title=name,
                            rel_path=f"./concepts/{name}.md",
                        )
                    except Exception as e_reg:
                        push_back_signals.append(
                            f"concept auto-register failed for {name}: {e_reg}"
                        )
            elif mode == "append-section":
                state.append_concept_section(name, content)
                _record_success(concept_rel)
            else:
                push_back_signals.append(f"concept_write unknown mode {mode!r}")
                _record_fail("concept_write", concept_rel)
        except FileNotFoundError as e:
            push_back_signals.append(f"concept_write append-section failed: {e}")
            _record_fail("concept_write", concept_rel)
        except Exception as e:
            push_back_signals.append(f"concept_write failed for {name}: {e}")
            _record_fail("concept_write", concept_rel)

    # 3a-pre. section_appends
    for sa in plan.get("section_appends") or []:
        rel = sa.get("path", "") if isinstance(sa, dict) else ""
        heading = sa.get("heading", "") if isinstance(sa, dict) else ""
        content = sa.get("content", "") if isinstance(sa, dict) else ""
        if not rel or not heading:
            push_back_signals.append("section_append rejected: missing path or heading")
            _record_fail("section_append", rel or "<missing>")
            continue
        if not _is_safe_create_path(rel):
            push_back_signals.append(f"section_append rejected (unsafe path): {rel!r}")
            _record_fail("section_append", rel)
            continue
        try:
            state.append_section(rel, heading, content)
            _record_success(rel)
        except FileNotFoundError:
            push_back_signals.append(
                f"section_append rejected (path doesn't exist; use slice_writes mode=create): {rel}"
            )
            _record_fail("section_append", rel)
        except ValueError as e:
            push_back_signals.append(f"section_append rejected for {rel}: {e}")
            _record_fail("section_append", rel)
        except Exception as e:
            push_back_signals.append(f"section_append failed for {rel}: {e}")
            _record_fail("section_append", rel)

    # 3a. file_edits
    for fe in plan.get("file_edits") or []:
        rel = fe.get("path", "") if isinstance(fe, dict) else ""
        old_string = fe.get("old_string", "") if isinstance(fe, dict) else ""
        new_string = fe.get("new_string", "") if isinstance(fe, dict) else ""
        replace_all = bool(fe.get("replace_all", False)) if isinstance(fe, dict) else False
        if not rel:
            push_back_signals.append("file_edit rejected: missing path")
            _record_fail("file_edit", "<missing>")
            continue
        if not _is_safe_create_path(rel):
            push_back_signals.append(f"file_edit rejected (unsafe path): {rel!r}")
            _record_fail("file_edit", rel)
            continue
        full_path = state.repo_root / rel
        if not full_path.exists():
            push_back_signals.append(
                f"file_edit rejected (path doesn't exist; use file_creates / slice_writes mode=create): {rel}"
            )
            _record_fail("file_edit", rel)
            continue
        try:
            text = full_path.read_text()
            occurrences = text.count(old_string) if old_string else 0
            if occurrences == 0:
                push_back_signals.append(
                    f"file_edit rejected (old_string not found in {rel}): {old_string[:80]!r}"
                )
                _record_fail("file_edit", rel)
                continue
            if occurrences > 1 and not replace_all:
                push_back_signals.append(
                    f"file_edit rejected (old_string ambiguous in {rel}: {occurrences} matches; "
                    f"either anchor more uniquely or set replace_all=true)"
                )
                _record_fail("file_edit", rel)
                continue
            new_text = text.replace(old_string, new_string) if replace_all else \
                       text.replace(old_string, new_string, 1)
            full_path.write_text(new_text)
            _record_success(rel)
        except Exception as e:
            push_back_signals.append(f"file_edit failed for {rel}: {e}")
            _record_fail("file_edit", rel)

    # 3b. dependency_map_edges (idempotent; substantive — relational content)
    for edge in plan.get("dependency_map_edges") or []:
        edge_path = "book/src/concepts/dependency-map.md"
        try:
            state.add_dependency_map_edge(
                layer=edge.get("layer", ""),
                from_=edge.get("from", ""),
                to_list=edge.get("to", []),
            )
            _record_success(edge_path)
        except Exception as e:
            push_back_signals.append(
                f"dependency_map_edge failed for {edge.get('from','?')}: {e}"
            )
            _record_fail("dependency_map_edge", edge_path)

    # 3c. slice_index_updates (mechanical row-rewrite; meta-10 item 1
    #     after recurrence #2 of file_edits anchor mismatch on spec/index.md).
    #     Tracked as bookkeeping — successful updates don't count toward
    #     substantive_landed; failed updates still trigger
    #     bookkeeping_only_failure when they're the only failure.
    index_md_path = "book/src/spec/index.md"
    for siu in plan.get("slice_index_updates") or []:
        slice_name = siu.get("slice", "") if isinstance(siu, dict) else ""
        layer = siu.get("layer", "") if isinstance(siu, dict) else ""
        date = (siu.get("date") if isinstance(siu, dict) else "") or \
               __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%d")
        summary = siu.get("summary", "") if isinstance(siu, dict) else ""
        link_title = siu.get("link_title") if isinstance(siu, dict) else None
        if not slice_name or not layer:
            push_back_signals.append(
                f"slice_index_update rejected: missing slice or layer "
                f"(slice={slice_name!r}, layer={layer!r})"
            )
            _record_fail("slice_index_update", index_md_path)
            continue
        try:
            state.update_slice_index_row(
                slice=slice_name,
                layer=layer,
                date=date,
                summary=summary,
                link_title=link_title,
            )
            # Track but classify as bookkeeping (path is index.md).
            # _record_success uses _is_bookkeeping_path so this stays correct.
        except FileNotFoundError as e:
            push_back_signals.append(
                f"slice_index_update: {e}. Add a row via file_edits/section_appends first, "
                "or the integrator can be extended with an append-by-slug fallback."
            )
            _record_fail("slice_index_update", index_md_path)
        except Exception as e:
            push_back_signals.append(f"slice_index_update failed: {e}")
            _record_fail("slice_index_update", index_md_path)

    # 4. lessons (dedupe-on-append)
    for lesson in plan.get("lessons") or []:
        if not isinstance(lesson, str) or not lesson.strip():
            continue
        try:
            state.append_lesson_unique(lesson)
            _record_success("lessons.md")
        except Exception as e:
            push_back_signals.append(f"lesson append failed: {e}")
            _record_fail("lesson", "lessons.md")

    bookkeeping_only_failure = (
        apply_failed
        and substantive_landed > 0
        and all(_is_bookkeeping_path(fp["path"]) for fp in failed_paths)
    )
    return {
        "apply_failed": apply_failed,
        "substantive_landed": substantive_landed,
        "failed_paths": failed_paths,
        "bookkeeping_only_failure": bookkeeping_only_failure,
    }


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

    # Precondition: a SIDEWAYS push must name ≥2 concrete slices that exist
    # on disk. Cycle 22 fired SIDEWAYS with slice='unknown' because the
    # Planner output's `slices=a,b` field was ignored by the parser; the
    # parser now populates `comparison_slices`, and here we validate.
    # Added meta-review #8.
    if push["kind"] == "sideways":
        cs = push.get("comparison_slices") or []
        if len(cs) < 2:
            print(
                f"[cycle {state.cycle_id}] SIDEWAYS precondition failed: "
                f"comparison_slices={cs!r} (need ≥2). Rejecting and recording as escalate."
            )
            # Convert to an escalate so the cycle records but doesn't run a
            # degenerate Synthesizer call.
            push = {
                "kind": "escalate",
                "reason": (
                    f"SIDEWAYS dispatched without ≥2 named slices "
                    f"(got comparison_slices={cs!r}). Planner-prompt defect."
                ),
            }
        else:
            # Sanity-check each slice exists on disk.
            missing = [
                s for s in cs
                if not (state.repo_root / "book/src/spec/slices" / f"{s}.md").exists()
                and not (state.repo_root / "book/src/spec/slices" / s / "index.md").exists()
            ]
            if missing:
                print(
                    f"[cycle {state.cycle_id}] SIDEWAYS precondition failed: "
                    f"slices {missing!r} not on disk. Rejecting."
                )
                push = {
                    "kind": "escalate",
                    "reason": (
                        f"SIDEWAYS dispatched with non-existent slices: "
                        f"{missing!r}. Planner-prompt defect."
                    ),
                }

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

    plan, syn_usage = call_synthesizer(
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

    # Extract structured fields from the integration plan for downstream use.
    claims = plan.get("rotation_claims") or []
    diff_for_critic = _summarize_plan_for_critic(plan)

    cited_source = _prefetch_citations_from_claims(state, claims)
    verdict, cr_usage = call_critic(
        state=state,
        cfg=cfg,
        client=client,
        schemas=schemas,
        claims=claims,
        cited_source=cited_source,
        diff=diff_for_critic,
        dry_run=dry_run,
    )
    total_usage.input_tokens += cr_usage.input_tokens
    total_usage.output_tokens += cr_usage.output_tokens
    print(f"[cycle {state.cycle_id}] critic verdict: {verdict['verdict']}")

    # ─────── integrator: apply the integration plan ───────
    # The integrator processes each plan section with semantic-merge
    # discipline:
    # - slice_writes: file_creates (path-safe) and diffs (git apply)
    # - concept_writes: create-or-append-section to concepts/ files
    # - dependency_map_edges: idempotent edge addition to mermaid graphs
    # - lessons: dedupe-on-append
    # - log_synthesis: passed to the LOG.md entry builder below
    # See `scaffolding/decisions/integration-plan-architecture.md` for design
    # rationale. In serial cycles (current state), the integrator is single-
    # threaded; Phase 8 parallelizes by queuing plans for serial application.
    push_back_signals: list[str] = []
    apply_failed = False
    bookkeeping_only_failure = False
    substantive_landed = 0
    if verdict["verdict"] in ("pass", "revise"):
        if dry_run:
            _summarize_plan_dry_run(plan)
        else:
            result = _apply_integration_plan(state, plan, push_back_signals)
            apply_failed = result["apply_failed"]
            bookkeeping_only_failure = result["bookkeeping_only_failure"]
            substantive_landed = result["substantive_landed"]

    # Verdict-downgrade rule (meta-5 + refined meta-9 item 2):
    # - pass + apply_failed + bookkeeping-only failure → hold pass, set
    #   bookkeeping_incomplete flag (content landed; the index/TOC write
    #   failed but is recoverable next cycle).
    # - pass + apply_failed + ANY substantive failure → downgrade to revise
    #   (the cycle's substantive content did not fully land).
    # Capture original verdict either way so audit can distinguish content
    # judgment from orchestrator action (meta-6 item 2).
    verdict["verdict_original"] = verdict.get("verdict")
    verdict["downgrade_applied"] = False
    verdict["bookkeeping_incomplete"] = False
    if verdict["verdict"] == "pass" and apply_failed:
        if bookkeeping_only_failure:
            verdict["bookkeeping_incomplete"] = True
            push_back_signals.append(
                f"bookkeeping_incomplete: {substantive_landed} substantive writes landed; "
                "only bookkeeping (index/TOC) write(s) failed. Verdict held pass per meta-9 "
                "item 2; next cycle on this slice should re-attempt the bookkeeping update."
            )
            print(
                f"[cycle {state.cycle_id}] verdict held pass (bookkeeping_incomplete; "
                f"{substantive_landed} substantive writes landed)"
            )
        else:
            verdict["verdict"] = "revise"
            verdict["downgrade_applied"] = True
            push_back_signals.append(
                "verdict auto-downgraded pass→revise: substantive write(s) did not land "
                f"(original Critic verdict was 'pass'; see verdict_original in episodic)"
            )
            print(f"[cycle {state.cycle_id}] verdict auto-downgraded pass→revise (apply failure)")

    # For revise (and reject), also collect labored-rotation issues as push-back
    # signals so the next cycle's Planner can see them.
    if verdict["verdict"] != "pass":
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

    # Structural-change summary built from the plan's contents and the apply result.
    structural_change = ""
    if verdict["verdict"] in ("pass", "revise") and not apply_failed:
        parts: list[str] = []
        sw = len(plan.get("slice_writes") or [])
        cw = len(plan.get("concept_writes") or [])
        de = len(plan.get("dependency_map_edges") or [])
        le = len(plan.get("lessons") or [])
        if sw: parts.append(f"{sw} slice_write(s)")
        if cw: parts.append(f"{cw} concept_write(s)")
        if de: parts.append(f"{de} dep-map edge(s)")
        if le: parts.append(f"{le} lesson(s)")
        if parts:
            structural_change = (
                f"applied: {', '.join(parts)}; {len(claims)} rotation_claim(s)"
            )

    concepts_touched = [
        cw.get("name", "") for cw in (plan.get("concept_writes") or [])
        if isinstance(cw, dict) and cw.get("name")
    ]

    episodic_entry = {
        "cycle_id": state.cycle_id,
        "push_kind": push["kind"],
        "slice": slice_name,
        "edge": edge,
        "verdict": verdict["verdict"],
        "verdict_original": verdict.get("verdict_original", verdict["verdict"]),
        "downgrade_applied": verdict.get("downgrade_applied", False),
        "bookkeeping_incomplete": verdict.get("bookkeeping_incomplete", False),
        "substantive_landed": substantive_landed,
        "plan_kind": (plan or {}).get("plan_kind", "new_content") if isinstance(plan, dict) else "new_content",
        "friction_observed": friction_summary,
        "structural_change": structural_change,
        "push_back_signals": push_back_signals,
        "concepts_touched": concepts_touched,
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
            plan.get("log_synthesis")
            or f"{len(claims)} rotation_claim(s); {structural_change or 'no writes applied'}"
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
    if dry_run:
        # No filesystem mutation in dry-run; print the rendered plan to stdout
        # so the operator can see what *would* be written.
        print("[dry-run] would write meta-review-pending.md with the following content:")
        print("─" * 60)
        print(plan_md)
        print("─" * 60)
    else:
        pending_path = state.write_meta_review_pending(plan_md)
        print(f"[meta-review] plan written to {pending_path.relative_to(state.repo_root)}; "
              f"awaiting APPROVAL marker.")
    return False


def _rebuild_book(repo_root: Path, *, dry_run: bool) -> None:
    """Rebuild the mdBook so the rendered HTML is fresh when the human
    sits down to review the meta-review pending plan. Runs `cargo make
    book` from repo_root. Failures are logged but non-fatal — the human
    can still inspect book/src/ markdown directly.

    Called immediately before every meta-review invocation.
    """
    if dry_run:
        print("[dry-run] would rebuild book (cargo make book)", file=sys.stderr)
        return
    print("[meta-review] rebuilding book before pause for human review...", file=sys.stderr)
    result = subprocess.run(
        ["cargo", "make", "book"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        # Don't crash the meta-review on book-build failure — surface clearly
        # and proceed.
        print(
            f"[meta-review] book rebuild FAILED (exit {result.returncode}); "
            f"plan will still be written and the markdown source is current. "
            f"stderr tail:\n{result.stderr[-1000:]}",
            file=sys.stderr,
        )
    else:
        print("[meta-review] book rebuild OK", file=sys.stderr)


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
        _rebuild_book(state.repo_root, dry_run=dry_run)
        await with_mcp(lambda _: run_meta_review(
            cfg=cfg, state=state, schemas=schemas, client=client, dry_run=dry_run,
        ))
        return

    # Run one or more normal cycles, firing meta-review at the configured cadence.
    while True:
        # Check pending meta-review handshake first
        if state.read_meta_review_pending() is not None:
            _rebuild_book(state.repo_root, dry_run=dry_run)
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
            _rebuild_book(state.repo_root, dry_run=dry_run)
            done = await run_meta_review(
                cfg=cfg, state=state, schemas=schemas, client=client, dry_run=dry_run,
            )
            if not done:
                return  # waiting on human

        if one_cycle:
            return


def main_loop(**kwargs) -> None:
    asyncio.run(main_loop_async(**kwargs))
