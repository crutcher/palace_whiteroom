# Decision: P1 edge-home = per-chapter `edges:` frontmatter, incremental rollout

**Date:** 2026-06-04 (post-cycle-094 finalize; before cycle-095/P1)
**Decider:** user (resolving the flagged decision-fork)
**Resolves OQ:** `graded-stack-edge-home-fork-p1-cost` (formal closure deferred to the batch-30 meta-phase, which owns OQ-ledger unify; this record is the authoritative resolution the c095 planner + dispatches act on in the interim).
**Context:** The GRADED-STACK campaign's P1 (artifact-wide edge-typing audit) needs a single machine-readable home for typed dependency edges. Today ~250 leaf nodes carry edges only in unparseable prose `## Dependencies` sections; only 10 files have ad-hoc `depends_on:` frontmatter. D1 (`reports/2026-06-04T195500Z-layer-intro-author-cycle-094-graded-stack-scheme/`) enumerated the fork: (a) per-chapter `edges:` frontmatter everywhere; (b) parse the index dep-map tables; (c) hybrid.

## The decision

**Option (a)-incremental** (D1's recommendation). Edges live in a **single per-chapter `edges:` frontmatter block** (superseding the ad-hoc `depends_on:`), because the prose `## Dependencies` sections and index dep-map tables are not machine-parseable and table-parse (option b) misses lowering themes + concept pages that appear in no table.

**Rollout is incremental, NOT one whole-artifact pass:**
- Type **feature-root closure + the high-fan-out frontier FIRST** (the nodes the rank linter + reachability GC most need to produce a meaningful audit).
- The **long tail is lazy** — typed as cycles touch those nodes / as the frontier advances.
- The **linters warn-not-fail on untyped nodes** (already implemented in `tools/graded-stack-lint/`, D2) so the artifact stays buildable throughout the rollout.
- Adopt the rank invariant as a **HARD gate for NEW work immediately** (per `METHODOLOGY-GRADED-STACK.md` §5 audit-first / hard-gate-new); existing violations go to a **tracked baseline-exception set** with promotion conditions (the `partly-constructive` pattern), NOT open-ended fix-forward.

## Why (over the alternatives)

- **vs full-(a) all-at-once:** one whole-artifact pass of ~250 hand-classified nodes risks sprawling past a clean cycle; the incremental rollout bounds per-cycle cost while reaching the same clean end state. (`METHODOLOGY-GRADED-STACK.md` §104 says edge-typing + audit are one *campaign* — incremental keeps it one campaign across cycles, not one cycle.)
- **vs (b) table-parse:** lightest but incomplete — themes/concepts invisible to the graph; the GC/rank checks would have blind spots.
- **vs (c) hybrid:** full coverage but the linters must reconcile two edge sources (more parser complexity) for no end-state benefit over (a).

## Consequences for c095+ (P1)

- The `edges:` frontmatter grammar is the one D1 specified in `book/src/methodology/graded-stack-scheme.md` (bare-string = `depends-on` default; `{target:, rel: reference}` / `{target:, kind:}` mapping form; edge-to-a-root = `reference`).
- c095 P1 starts with the **feature-root closure + high-fan-out frontier** typing, runs both linters as the audit over the typed subset, and opens the baseline-exception set for the 22 pre-existing rank violations (the `bilinear-form` cascade — priorities item-1 discharges ~half).
- Priorities item-1 (`bilinear-form-firm-flip-and-cascade-wave`) is the campaign's first live rank-linter validation and composes naturally with the frontier-first typing.
