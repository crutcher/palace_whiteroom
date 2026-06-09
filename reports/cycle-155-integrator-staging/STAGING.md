# Cycle-155 integrator staging log

Per-report integration rows, newest LAST (append-only). Row ORDER is the authoritative
apply-order record (NOT `applied_at` timestamps). integrator-finalize reconciles from this log.

---

## 2026-06-09T052929Z-general-purpose-c155-lint-untyped-carveout-convergence
applied_at: 2026-06-09T053500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- tools/graded-stack-lint/graded_stack_lint.py (modify — extended OUTSIDE_DAG_PREFIXES += L0/, meta-reviews/; added OUTSIDE_DAG_EXACT = {SUMMARY, introduction, semantics/index}; split untyped count to exclude outside-DAG-by-design, reported separately as untyped_outside_dag_by_design)
- book/src/methodology/graded-stack-scheme.md (modify — added `### The outside-DAG-by-design carve-out` note in §5: L0-as-ground-truth-leaf + outside-DAG rationale + exactness invariant)

Note: edits were ALREADY APPLIED on disk + critic-verified before this dispatch. Staged + gate-checked only; did NOT re-apply.

Gate hits:
- (none) — no concept_writes / forward-edge / edge-label / H1-reuse / append-on-missing-slug / variant-axis / index-placeholder / implied-stub / deleted-slug-edge / KaTeX-$-sigil-fence / retroactive-budget gate triggered. Tooling change + an additive prose subsection to an existing registered chapter.
- SUMMARY registration: not needed — methodology/graded-stack-scheme.md already exists and is SUMMARY-registered; the change is an additive `###` subsection, no new file.
- citecheck bounds + path-hygiene lint: N/A — report carries no `file:start-end` Palace source citations (a lint-tooling refactor + a methodology scheme note); nothing to range-resolve.

Per-report gate result (graded-stack-lint --book-src book/src --json):
NEW POST-CONVERGENCE BASELINE confirmed exactly —
- untyped: 0  (CONVERGENCE — genuine edge-typing debt eliminated; NOT a regression)
- untyped_outside_dag_by_design: 61  (new key; == the old 61-untyped set)
- expected_unreachable_outside_dag: 54 → 106  (+52 carved-out L0/meta-reviews/nav nodes on the reachability axis; 0 genuine-DAG nodes added)
HARD INVARIANTS + key totals HELD (all unchanged):
- rank_violations: 0, unresolved_depends_on_targets: 0
- typed: 331, files: 392, roots: 45, promotion_frontier: 11
- detritus: 123, true_detritus: 51
Lint exit code: 0.

Open questions promoted:
- (none — report opens no new OQs)

Build-relevant: yes

Notes:
- DELIBERATE, ACCOUNTED baseline MOVE (the convergence), NOT a hold. `untyped: 0` is the intended new state; do NOT treat as a regression.
- This report DISCHARGES the `p1-edge-typing-true-detritus-sweep` backlog item (convergence: genuine untyped → 0). FINALIZE: remove it from priorities.md + record the new tripwire baseline `untyped 0` (the steady-state tripwire now trips on untyped > 0, since 0 is the converged floor).
- Tools/ change (`graded_stack_lint.py`) is part of this report's footprint — FINALIZE must commit it alongside the book change.
- deferred integrated_at to finalize per role-spec (also integration_commit).
- Only per-report integrator of cycle-155; created this STAGING.md.

---
