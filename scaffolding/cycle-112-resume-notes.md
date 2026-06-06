# Cycle-112 resume notes (post-batch-35 meta-phase)

**SESSION RESTART REQUIRED before cycle-112.** The batch-35 meta-phase edited `.claude/agents/*` role-specs; the parent must restart the Claude Code session so the new agent definitions load before the next cycle's dispatch.

## Agent-defs that changed (why a restart is needed)

- **`.claude/agents/harvester.md`** — §"L4 / L3 strawman + pseudo-language conventions" gained a **named-shape-groups** bullet: NEW signatures must use `Tensor[(S: ...)]` (rank-agnostic congruence, NO colon before `[`) / `Tensor[S]` re-uses — NOT bare `Tensor[N]` (which is rank-1 and silently pins shape-generic ops to one dimension); `LinOp[(R: ...), (D: ...)]` for domain≠range operators; reserve `Tensor[N]` for genuinely-flat L1/L0 dof-vectors + genuine rank-1 lists (`Tensor[K]`/`Tensor[m]`); complex renderings convert the shape to `(S: ...)` and preserve the `complex` annotation. Authoritative def: `book/src/design/l4_calculus.md` §1.2.1–§1.2.2; memory `project_named_shape_groups_notation`.
- **`.claude/agents/layer-intro-author.md`** — §"L4 / L3 strawman + pseudo-language conventions" gained the matching named-shape-groups bullet, scoped to dep-map signature cells + calculus-touching concept pages (keep a dep-map cell consistent with its owning chapter's signature).

## Why the restart (not a `/compact`)

Per CLAUDE.md §Methodology invariants, the post-meta session restart IS the primary-context reset mechanism (the retired `/compact` step is subsumed). Do NOT emit a `/compact` reminder — the restart resets context.

## State entering cycle-112 (batch-36 opener)

- **Plan:** `scaffolding/priorities.md` — the CYCLE-112 / batch-36 active head. LEAD = `graded-stack-lazy-tail-typing` (the `L3/orthogonalize`/`L3/nrm2` mid-node from-scratch `edges:` typing is the cheap opener; the lazy-untyped tail `untyped: 60` continues lazily).
- **Linter baseline (live tree, confirmed this meta-phase):** `reachable=122`, `rank_violations=0`, `untyped=60`, `unresolved_depends_on_targets=0`, `STRONGER GARBAGE SIGNAL=26`, `detritus=137`, `promotion_frontier=8`. Firm histogram 201.
- **Reachability baseline-exception set (Axis-2) RATIFIED** — `scaffolding/graded-stack-baseline-exceptions.md` Axis-2 section, RE1–RE5 (chebyshev/jacobi preconditioner leg; L3-orthogonalize sub-chain; `L2/gram` deflate-gated; `incremental-least-squares` absorbed; normalize/reciprocal internal-utility chain). These are the dominant ratified subset of the `STRONGER GARBAGE SIGNAL` — TRACKED, not detritus; do NOT force unfaithful edges to flip them. Each has a non-fix-forward promotion condition.
- **STOP-PROPOSING** in force: the `promotion_frontier: 8` members are all obstruction-/demand-gated; the redirect forbids forcing a rectangular pull-up.
- No carried meta-phase findings — the plan enters batch-36 clean.
