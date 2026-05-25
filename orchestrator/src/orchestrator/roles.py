"""Per-role API call functions. One module entry per agent role.

Each function:
- Loads its system prompt from `prompts/<role>.md`.
- Builds a user message from cycle-specific state.
- Calls the Anthropic API with the role's configured model (with prompt
  caching on the static system prompt).
- For Explorer: runs a tool-use loop, dispatching MCP tool calls to the
  codemap server.
- Parses the response (JSON for typed roles; single-line for Planner).
- Validates against the schema (for Explorer/Synthesizer/Critic/Meta-Critic).
- Returns the parsed result.

The `dry_run` flag short-circuits the API call and returns a canned
response that validates against the schema. Used to exercise the loop
plumbing without spending tokens.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from anthropic import Anthropic

from .config import Config
from .mcp_client import CodemapClient
from .schemas import SchemaSet, validate
from .state import State


@dataclass
class TokenUsage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_input_tokens: int = 0
    cache_creation_input_tokens: int = 0

    def add(self, usage: Any) -> None:
        self.input_tokens += getattr(usage, "input_tokens", 0) or 0
        self.output_tokens += getattr(usage, "output_tokens", 0) or 0
        self.cache_read_input_tokens += getattr(usage, "cache_read_input_tokens", 0) or 0
        self.cache_creation_input_tokens += getattr(usage, "cache_creation_input_tokens", 0) or 0


def _load_prompt(repo_root: Path, role: str) -> str:
    return (repo_root / "prompts" / f"{role}.md").read_text()


def _system_block(text: str) -> list[dict]:
    """One system content block with prompt caching enabled."""
    return [{"type": "text", "text": text, "cache_control": {"type": "ephemeral"}}]


# ───────────────────────────── Planner ─────────────────────────────


_PUSH_LINE_RE = re.compile(
    r"^push:\s*(forward|back|sideways|escalate)\b(.*)$",
    re.MULTILINE,
)


def parse_push_line(line: str) -> dict:
    """Parse a single `push: ...` line into a structured dict."""
    m = _PUSH_LINE_RE.search(line)
    if not m:
        raise ValueError(f"Planner output did not contain a parseable `push:` line: {line!r}")
    kind = m.group(1)
    rest = m.group(2).strip()
    fields: dict[str, str] = {}
    for token in re.findall(r"(\w+)=(\S+)", rest):
        k, v = token
        fields[k] = v
    reason_match = re.search(r"reason=(.+)$", rest)
    if reason_match:
        fields["reason"] = reason_match.group(1).strip()
    # For SIDEWAYS pushes, the `slices=a,b` field carries multiple slice names.
    # Expose them as `comparison_slices` (list) and synthesize a `slice` of the
    # form "a,b" for log/commit message use. (Added meta-review #8 after cycle
    # 22 dispatched SIDEWAYS with slice='unknown' because the parser ignored
    # the `slices=` field entirely.)
    if kind == "sideways" and "slices" in fields:
        comparison_slices = [s.strip() for s in fields["slices"].split(",") if s.strip()]
        fields["comparison_slices"] = comparison_slices
        if "slice" not in fields:
            fields["slice"] = ",".join(comparison_slices)
    return {"kind": kind, **fields}


def call_planner(
    *,
    state: State,
    cfg: Config,
    client: Anthropic | None,
    dry_run: bool = False,
) -> dict:
    if dry_run:
        return {
            "kind": "forward",
            "slice": "main_dispatch",
            "from": "L0",
            "to": "L1",
            "reason": "[dry-run] seed Q-shared-1",
            "scope_question": (
                "Q-shared-1. What is the top-level entry point in Palace, and how does "
                "it dispatch between solvers? Read palace/main.cpp."
            ),
        }

    assert client is not None
    system_prompt = _load_prompt(state.repo_root, "planner")
    questions = state.read_questions()
    lessons = state.read_lessons()
    spec_index = state.read_spec_index()
    recent_episodic = state.read_episodic_window(5)

    user_message = (
        "Current spec slice index:\n```\n" + spec_index + "\n```\n\n"
        "Current questions ledger:\n```\n" + questions + "\n```\n\n"
        "Current lessons:\n```\n" + lessons + "\n```\n\n"
        "Recent episodic entries (last 5):\n```json\n" +
        "\n".join(json.dumps(e, separators=(",", ":")) for e in recent_episodic) +
        "\n```\n\n"
        "OUTPUT FORMAT — produce ONLY these one or two lines, NO analysis, NO "
        "preamble, NO markdown headers, NO reasoning prose. Just the directive:\n\n"
        "  push: forward slice=<name> from=L0 to=L1 reason=<short>\n"
        "  scope_question: <full question text>\n"
        "\n"
        "(Or one of the other push kinds: `push: back ...`, `push: sideways ...`, "
        "`push: escalate ...`. The `scope_question:` line is only required when "
        "the push is a FORWARD-to-L1 cycle on a seed question.)\n"
    )

    response = client.messages.create(
        model=cfg.models["planner"],
        max_tokens=2048,
        system=_system_block(system_prompt),
        messages=[{"role": "user", "content": user_message}],
    )
    text = "".join(b.text for b in response.content if getattr(b, "type", "") == "text").strip()
    push = parse_push_line(text)

    # Optional scope_question follow-up line
    scope_match = re.search(r"^scope_question:\s*(.+)$", text, re.MULTILINE)
    if scope_match:
        push["scope_question"] = scope_match.group(1).strip()
    return push


def call_planner_with_addendum(
    *,
    state: State,
    cfg: Config,
    client: Anthropic | None,
    addendum: str,
    dry_run: bool = False,
) -> dict | None:
    """Re-invoke the Planner with an explicit text addendum (e.g., the
    retroactive-budget hard-gate recovery message from meta-19 item 1).
    The addendum is appended to the user-message after the standard
    spec_index/questions/lessons/episodic context. The Planner emits a
    fresh dispatch.

    Returns the parsed push dict, or None on failure (the caller
    should fall back to escalate in that case). Same dry-run contract
    as call_planner.
    """
    if dry_run:
        # In dry-run, just return None — the caller will fall back to
        # escalate, which is the correct behavior for a non-real run.
        return None

    assert client is not None
    system_prompt = _load_prompt(state.repo_root, "planner")
    questions = state.read_questions()
    lessons = state.read_lessons()
    spec_index = state.read_spec_index()
    recent_episodic = state.read_episodic_window(5)

    user_message = (
        "Current spec slice index:\n```\n" + spec_index + "\n```\n\n"
        "Current questions ledger:\n```\n" + questions + "\n```\n\n"
        "Current lessons:\n```\n" + lessons + "\n```\n\n"
        "Recent episodic entries (last 5):\n```json\n" +
        "\n".join(json.dumps(e, separators=(",", ":")) for e in recent_episodic) +
        "\n```\n\n"
        + addendum +
        "\n\nOUTPUT FORMAT — produce ONLY these one or two lines, NO analysis, NO "
        "preamble, NO markdown headers, NO reasoning prose. Just the directive:\n\n"
        "  push: forward slice=<name> from=L0 to=L1 reason=<short>\n"
        "  scope_question: <full question text>\n"
        "\n"
        "(Or one of the other push kinds: `push: back ...`, `push: sideways ...`, "
        "`push: escalate ...`.)\n"
    )

    try:
        response = client.messages.create(
            model=cfg.models["planner"],
            max_tokens=2048,
            system=_system_block(system_prompt),
            messages=[{"role": "user", "content": user_message}],
        )
        text = "".join(b.text for b in response.content if getattr(b, "type", "") == "text").strip()
        push = parse_push_line(text)
        scope_match = re.search(r"^scope_question:\s*(.+)$", text, re.MULTILINE)
        if scope_match:
            push["scope_question"] = scope_match.group(1).strip()
        return push
    except Exception:
        return None


# ───────────────────────────── Explorer ─────────────────────────────


async def call_explorer(
    *,
    state: State,
    cfg: Config,
    client: Anthropic | None,
    mcp_client: CodemapClient | None,
    schemas: SchemaSet,
    slice_name: str,
    scope_question: str,
    dry_run: bool = False,
) -> tuple[dict, TokenUsage]:
    """Returns (ExplorationFinding dict, TokenUsage). MCP tool use is async
    because the codemap session is async."""

    usage = TokenUsage()

    if dry_run:
        finding = {
            "slice": slice_name,
            "scope_question": scope_question,
            "citations": [
                {"file": "palace/main.cpp", "start_line": 1, "end_line": 50, "kind": "definition"}
            ],
            "l1_claims": [
                {
                    "statement": "[dry-run canned] main() dispatches to one of five solver drivers based on config",
                    "inputs": ["argv", "config_file"],
                    "outputs": ["exit_code"],
                    "mutation_pattern": "pure",
                    "citation_indices": [0],
                }
            ],
            "confidence": "low",
        }
        errors = validate(schemas, "exploration_finding", finding)
        assert not errors, f"dry-run canned finding fails schema: {errors}"
        return finding, usage

    assert client is not None and mcp_client is not None
    system_prompt = _load_prompt(state.repo_root, "explorer")
    lessons = state.read_lessons()
    current_l1 = state.read_slice(slice_name)
    schema_text = json.dumps(
        schemas.validators["exploration_finding"].schema, indent=2,
    )

    user_message = (
        f"Scope: {scope_question}\n\n"
        f"Slice: {slice_name}\n\n"
        f"Current L1 content (empty if this is the first cycle on this slice):\n"
        f"```\n{current_l1 or '(empty)'}\n```\n\n"
        f"Lessons:\n```\n{lessons}\n```\n\n"
        f"Produce the ExplorationFinding JSON validating against the schema "
        f"(repeated below for convenience). Output JSON ONLY — no prose, no markdown fence.\n\n"
        f"```json\n{schema_text}\n```\n"
    )

    tools = await mcp_client.list_tools()

    messages: list[dict] = [{"role": "user", "content": user_message}]
    final_text: str | None = None
    for _ in range(40):  # bound the tool-use loop
        response = client.messages.create(
            model=cfg.models["explorer"],
            max_tokens=8192,
            system=_system_block(system_prompt),
            messages=messages,
            tools=tools,
        )
        usage.add(response.usage)

        if response.stop_reason == "end_turn":
            final_text = "".join(
                b.text for b in response.content if getattr(b, "type", "") == "text"
            ).strip()
            break

        if response.stop_reason == "tool_use":
            # Append assistant turn (must include the tool_use blocks)
            messages.append({
                "role": "assistant",
                "content": [b.model_dump() for b in response.content],
            })
            tool_results: list[dict] = []
            for block in response.content:
                if getattr(block, "type", "") != "tool_use":
                    continue
                try:
                    result = await mcp_client.call_tool(block.name, block.input or {})
                    content = json.dumps(result) if not isinstance(result, str) else result
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": content,
                    })
                except Exception as e:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": f"ERROR: {e}",
                        "is_error": True,
                    })
            messages.append({"role": "user", "content": tool_results})
            continue

        raise RuntimeError(f"Explorer: unexpected stop_reason {response.stop_reason}")

    if final_text is None:
        raise RuntimeError("Explorer: tool-use loop exceeded budget without final text")

    finding = _parse_json_response(final_text)
    errors = validate(schemas, "exploration_finding", finding)
    if errors:
        raise ValueError(f"Explorer output failed schema: {errors}\nRaw: {final_text}")
    return finding, usage


# ───────────────────────────── Synthesizer ─────────────────────────────


def call_synthesizer(
    *,
    state: State,
    cfg: Config,
    client: Anthropic | None,
    schemas: SchemaSet,
    finding: dict | None,
    edge: str,
    slice_name: str,
    dry_run: bool = False,
) -> tuple[dict, TokenUsage]:
    """Returns (integration_plan_dict, TokenUsage).

    The integration_plan validates against schemas/integration_plan.json
    and structures all the cycle's writes (slice_writes, concept_writes,
    dependency_map_edges, lessons, log_synthesis, rotation_claims).
    The orchestrator's integrator (in loop.py) applies the plan.

    Refactored 2026-05-23 from the prior (diff, claims, file_creates,
    usage) shape per `scaffolding/decisions/integration-plan-architecture.md`.
    Cuts over cleanly — no backward compatibility with the legacy shape.
    """
    usage = TokenUsage()

    if dry_run:
        canned_claim = {
            "slice": slice_name,
            "edge": edge,
            "from_form": "[dry-run] L1: main() dispatches",
            "to_form": "[dry-run] L2: dispatch as a pure case-analysis function",
            "justification_kind": "structural",
            "justification": "[dry-run canned] no real synthesis happened",
        }
        plan = {
            "slice_writes": [],
            "concept_writes": [],
            "dependency_map_edges": [],
            "lessons": [],
            "log_synthesis": "[dry-run canned] no real synthesis",
            "rotation_claims": [canned_claim],
        }
        errors = validate(schemas, "integration_plan", plan)
        assert not errors, f"dry-run canned plan fails schema: {errors}"
        return plan, usage

    assert client is not None
    system_prompt = _load_prompt(state.repo_root, "synthesizer")
    current_slice = state.read_slice(slice_name)
    plan_schema_text = json.dumps(
        schemas.validators["integration_plan"].schema, indent=2,
    )
    claim_schema_text = json.dumps(
        schemas.validators["rotation_claim"].schema, indent=2,
    )

    user_message = (
        f"Slice: {slice_name}\nEdge: {edge}\n\n"
        f"Current slice content:\n```markdown\n{current_slice or '(empty — first push on this slice)'}\n```\n\n"
        + (
            f"Explorer's ExplorationFinding:\n```json\n{json.dumps(finding, indent=2)}\n```\n\n"
            if finding else ""
        )
        + f"Produce the {edge} rotation as an INTEGRATION PLAN — a single JSON object validating "
        f"against the schema below. Per `prompts/synthesizer.md` *Integration-plan output*, the "
        f"plan structures all the cycle's writes (slice_writes, concept_writes, "
        f"dependency_map_edges, lessons, log_synthesis, rotation_claims). The orchestrator's "
        f"integrator applies them with semantic-merge discipline.\n\n"
        f"integration_plan schema:\n```json\n{plan_schema_text}\n```\n\n"
        f"rotation_claim schema (referenced by `rotation_claims`):\n```json\n{claim_schema_text}\n```\n\n"
        f"OUTPUT FORMAT: the FIRST character of your response must be `{{` and the LAST must be "
        f"`}}`. No prose preamble, no markdown fence, no trailing commentary. ANY content outside "
        f"the single top-level JSON object will be parsed as the JSON output and fail. Use the "
        f"`slice_writes[i].content` and `concept_writes[i].content` fields for ALL slice/concept "
        f"prose, math, and commentary."
    )

    # max_tokens history: 8192 (init) → 16384 (cycle 20 truncated)
    #                   → 24576 (cycle 63 truncated on SIDEWAYS cg+gmres).
    # The Anthropic SDK forces streaming at max_tokens above ~18k because
    # the predicted wall-clock would exceed its 10-minute non-streaming
    # limit. Use the streaming API to collect the response — same result,
    # avoids the SDK's preemptive ValueError.
    with client.messages.stream(
        model=cfg.models["synthesizer"],
        max_tokens=24576,
        system=_system_block(system_prompt),
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        for _ in stream.text_stream:
            pass  # drain stream; we want the final message, not incremental
        response = stream.get_final_message()
    usage.add(response.usage)
    if response.stop_reason == "max_tokens":
        raise ValueError(
            "Synthesizer response was truncated by max_tokens. The plan JSON is incomplete and "
            "cannot be parsed. Either increase max_tokens or split the slice across multiple "
            "cycles (smaller scope per cycle). Truncated response head: "
            + "".join(b.text for b in response.content if getattr(b, "type", "") == "text")[:400]
        )
    final_text = "".join(
        b.text for b in response.content if getattr(b, "type", "") == "text"
    ).strip()
    plan = _parse_json_response(final_text)

    # Validate the plan envelope.
    errors = validate(schemas, "integration_plan", plan)
    if errors:
        raise ValueError(f"Synthesizer plan failed schema: {errors}\nPlan keys: {list(plan.keys())}")

    # Validate each rotation_claim individually (the plan schema accepts
    # any object in rotation_claims; per-claim validation is here).
    for i, claim in enumerate(plan.get("rotation_claims") or []):
        errors = validate(schemas, "rotation_claim", claim)
        if errors:
            raise ValueError(f"Synthesizer plan rotation_claims[{i}] failed schema: {errors}\nClaim: {claim}")

    return plan, usage


# ───────────────────────────── Critic ─────────────────────────────


def call_critic(
    *,
    state: State,
    cfg: Config,
    client: Anthropic | None,
    schemas: SchemaSet,
    claims: list[dict],
    cited_source: dict[str, str],
    diff: str,
    dry_run: bool = False,
) -> tuple[dict, TokenUsage]:
    """`cited_source` is a {file:line-range -> text} prefetch of all
    citations the Synthesizer referenced. The Critic must NOT see the
    Synthesizer's chain-of-thought — we only pass the claims and the source."""
    usage = TokenUsage()

    if dry_run:
        verdict = {"verdict": "pass", "issues": []}
        errors = validate(schemas, "critic_verdict", verdict)
        assert not errors, f"dry-run canned verdict fails schema: {errors}"
        return verdict, usage

    assert client is not None
    system_prompt = _load_prompt(state.repo_root, "critic")
    schema_text = json.dumps(
        schemas.validators["critic_verdict"].schema, indent=2,
    )

    source_block = "\n".join(
        f"=== {k} ===\n{v}\n" for k, v in cited_source.items()
    ) if cited_source else "(no source pre-fetched; consult MCP tools if needed but the schema only accepts text input here)"

    user_message = (
        f"Rotation claims to verify:\n```json\n{json.dumps(claims, indent=2)}\n```\n\n"
        f"Proposed diff (the Synthesizer's spec edit):\n```diff\n{diff or '(empty diff)'}\n```\n\n"
        f"Cited source ranges (pre-fetched):\n```\n{source_block}\n```\n\n"
        f"Produce a critic_verdict JSON validating against the schema. Output JSON ONLY.\n\n"
        f"```json\n{schema_text}\n```\n"
    )

    response = client.messages.create(
        model=cfg.models["critic"],
        max_tokens=4096,
        system=_system_block(system_prompt),
        messages=[{"role": "user", "content": user_message}],
    )
    usage.add(response.usage)
    final_text = "".join(
        b.text for b in response.content if getattr(b, "type", "") == "text"
    ).strip()
    verdict = _parse_json_response(final_text)
    errors = validate(schemas, "critic_verdict", verdict)
    if errors:
        raise ValueError(f"Critic output failed schema: {errors}\nRaw: {final_text}")
    return verdict, usage


# ───────────────────────────── Meta-Critic ─────────────────────────────


def call_meta_critic(
    *,
    state: State,
    cfg: Config,
    client: Anthropic | None,
    schemas: SchemaSet,
    cycles_covered: list[int],
    dry_run: bool = False,
) -> tuple[dict, TokenUsage]:
    usage = TokenUsage()
    from datetime import date

    if dry_run:
        plan = {
            "meta_review_date": date.today().isoformat(),
            "cycles_covered": cycles_covered,
            "categorized_issues": {"low": [], "medium": [], "high": []},
            "direct_actions": [],
            "plan_items": [],
            "escalations": [],
        }
        errors = validate(schemas, "refinement_plan", plan)
        assert not errors, f"dry-run canned plan fails schema: {errors}"
        return plan, usage

    assert client is not None
    system_prompt = _load_prompt(state.repo_root, "meta_critic")
    schema_text = json.dumps(
        schemas.validators["refinement_plan"].schema, indent=2,
    )
    lessons = state.read_lessons()
    problems = state.open_problems()
    recent_episodic = state.read_episodic_window(50)
    prior_meta_dir = state.repo_root / "book/src/meta-reviews"
    prior_records = "\n\n".join(
        f"=== {p.name} ===\n{p.read_text()}"
        for p in sorted(prior_meta_dir.glob("*.md"))
        if p.name != "index.md"
    ) or "(no prior meta-review records yet)"

    user_message = (
        f"Cycles covered in this meta-review window: {cycles_covered}\n\n"
        f"Recent episodic entries (last 50):\n```json\n" +
        "\n".join(json.dumps(e, separators=(",", ":")) for e in recent_episodic) +
        "\n```\n\n"
        f"Lessons:\n```\n{lessons}\n```\n\n"
        f"Open problems:\n```\n" +
        ("\n---\n".join(p["content"] for p in problems) if problems else "(none)") +
        "\n```\n\n"
        f"Prior meta-review records:\n```\n{prior_records}\n```\n\n"
        f"Produce a refinement_plan JSON validating against the schema. Output JSON ONLY.\n\n"
        f"```json\n{schema_text}\n```\n"
    )

    response = client.messages.create(
        model=cfg.models["meta_critic"],
        max_tokens=8192,
        system=_system_block(system_prompt),
        messages=[{"role": "user", "content": user_message}],
    )
    usage.add(response.usage)
    final_text = "".join(
        b.text for b in response.content if getattr(b, "type", "") == "text"
    ).strip()
    plan = _parse_json_response(final_text)
    errors = validate(schemas, "refinement_plan", plan)
    if errors:
        raise ValueError(f"Meta-Critic output failed schema: {errors}\nRaw: {final_text}")
    return plan, usage


# ───────────────────────────── helpers ─────────────────────────────


def _parse_json_response(text: str) -> dict:
    """Parse a JSON object out of an agent's response.

    Tolerant of:
    - leading/trailing whitespace
    - fenced code blocks (```json ... ``` or just ``` ... ```)
    - leading / trailing / interspersed prose around the JSON object.

    Strategy:
    1. Strip surrounding fence if present, try parsing the whole text.
    2. Otherwise: scan ALL top-level balanced `{...}` substrings and try
       parsing each, longest first. The Synthesizer sometimes writes
       prose containing math notation like `{r_0, Ar_0, ...}` BEFORE the
       real JSON; the longest balanced substring is almost always the
       real output, since JSON payloads are much longer than incidental
       brace pairs in prose.
    3. If none parse, raise with a snippet of the raw text.
    """
    raw = text
    text = text.strip()

    if not text:
        raise ValueError("agent response is empty (no text content at all)")

    # Strip a single surrounding code fence if present.
    if text.startswith("```"):
        lines = text.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()

    # Try the whole text first — happens when the agent followed instructions.
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Collect ALL top-level balanced `{...}` substrings via single scan.
    # "Top-level" = depth went from 0 → 1 at the opening `{` and back to 0
    # at the closing `}`. Nested braces inside one candidate are handled.
    candidates: list[str] = []
    depth = 0
    start = -1
    in_string = False
    escape = False
    for i, ch in enumerate(text):
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            if depth > 0:
                depth -= 1
                if depth == 0 and start >= 0:
                    candidates.append(text[start : i + 1])
                    start = -1

    if not candidates:
        snippet = raw if len(raw) < 400 else raw[:400] + "...[truncated]"
        raise ValueError(
            f"no balanced '{{...}}' found in agent response; raw text (head): {snippet!r}"
        )

    # Longest candidate first — JSON payloads dwarf incidental brace pairs.
    last_err = None
    for cand in sorted(candidates, key=len, reverse=True):
        try:
            return json.loads(cand)
        except json.JSONDecodeError as e:
            last_err = e
            continue

    snippet_text = raw if len(raw) < 400 else raw[:400] + "...[truncated]"
    candidate_snippets = "; ".join(
        f"{c[:80]!r}..." if len(c) > 80 else repr(c) for c in candidates[:5]
    )
    raise ValueError(
        f"found {len(candidates)} balanced '{{...}}' candidate(s); none parsed as JSON. "
        f"Last error: {last_err}. Candidate heads: {candidate_snippets}. "
        f"Raw text (head): {snippet_text!r}"
    )
