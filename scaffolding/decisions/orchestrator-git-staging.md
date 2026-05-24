# Decision: orchestrator commits stage specific paths, not `git add -A`

**Decided:** 2026-05-23 (during Phase 5's first real end-to-end cycle).

**Context.** The first real cycle (commit `8e5a480`, "cycle: forward cg_solver_integration [L0→L1] → revise") swept in unrelated working-tree changes alongside the cycle's own writes. The original `state.commit()` ran `git add -A`, which captured: `.env.example` dev edits, Phase 1 fixes (mcp/codemap/src/main.rs + types.rs), orchestrator robustness fixes (cli.py, roles.py) — *plus* the cycle's actual writes (LOG.md, episodic.jsonl, lessons.md).

**Result of `-A`.** A commit message claiming "cycle: forward cg_solver_integration [L0→L1] → revise" whose actual contents are a mix of (mostly) unrelated dev work and a small cycle output. Future readers parsing the git log to understand which commit is which cycle would be misled.

**Fix.** `state.commit()` now stages only paths from `CYCLE_OWNED_PATHS`:

- `episodic.jsonl`
- `LOG.md`
- `lessons.md`
- `questions.md`
- `book/` (spec, concepts, design, meta-reviews)
- `scaffolding/` (cross-cutting agent notes)
- `problems/` (agent-filed concerns)

Anything else in working tree stays unstaged. Developer edits don't contaminate cycle commits; renames or stray files don't contaminate either.

## What this does NOT cover

- **The orchestrator itself** (`orchestrator/`, `mcp/`, `prompts/`, `schemas/`, `skills/`) is **not** in the cycle-owned set — by design. The agent loop should not modify its own infrastructure mid-cycle. If a cycle did somehow rewrite `prompts/explorer.md`, that change would remain unstaged, would not commit, and would be visible to the developer for review. Defensive.
- **The Meta-Critic's enactment** of approved plan items still mutates files outside `CYCLE_OWNED_PATHS` (e.g., updating `prompts/` per a refinement plan). That happens out-of-band of `state.commit()`, in the human-approved enactment phase; the commit there should also stage paths explicitly, not use `-A`. Worth re-checking once we have a real meta-review cycle to drive the question.
- **A developer running the orchestrator while their own dev changes are uncommitted** will still see those changes in working tree after the cycle runs. That's the correct behavior — the cycle should be inert with respect to unrelated edits.

## Promotion candidates

If this convention proves out across many cycles, it could promote into:

- `book/src/methodology/` as part of the operational protocol.
- A `concepts/cycle-commit-discipline.md` entry once the spec calls for one.

For now it lives here as a decision artifact.

## Related friction

Search-text friction surfaced during the same cycle (`commit 8e5a480` lessons.md entry): the Critic flagged a slice that mixed three distinct concerns at L1, suggesting the Explorer's slice scoping needs tighter discipline. That's a different friction signal — about slice boundaries, not git staging — and belongs in a future scaffolding entry once it recurs.
