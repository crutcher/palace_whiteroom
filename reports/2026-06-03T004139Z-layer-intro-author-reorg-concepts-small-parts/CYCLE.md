---
agent: layer-intro-author
invoked_at: 2026-06-03T004139Z
scope: cycle-071 D6 — directive-3 mdBook reorg of Concepts + Meta-Reviews + Methodology + Feature + Design Parts
status: integrated
integrated_at: 2026-06-03T021500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-071 D6 (LAST per-report integration), applied clean by integrator-per-report (STAGING row 6), finalized
  by integrator-finalize. PURE STRUCTURAL directive-3 reorg — exactly ONE of the 5 owned Parts changed:
  # Concepts flat alpha re-sort (44 content slugs C-locale by file slug; 2 nav rows Index/Dependency-map kept
  at top; NO nesting — flat shared-library reference list). set(old)==set(new) — 44<->44 content slugs preserved,
  empty symmetric difference. CRITICAL GUARD HONORED: # Feature surfaces left UNTOUCHED (within-column high->low
  ordering electrostatic.L4->.L1->.L0 intact, standing batch-22-meta OQ); Meta-Reviews chronological, Methodology,
  Design all left as-is. NO count changes, NO status flips, NO dropped chapters. 1 OQ promoted:
  concepts-index-table-vs-summary-membership-drift-two-missing-rows (pre-existing concepts/index.md table missing
  2 rows that exist in SUMMARY + on disk — NOT a dropped concept, the table is the lagging derived surface; routed
  to batch-22 meta / cycle-072 hygiene). citecheck 0 citations (clean). cargo make book exit 0, linkcheck2 clean.
---

# CYCLE: directive-3 reorg — Concepts + small Parts (D6)

## Summary

Directive-3 one-time structural-reorg wave, the reference + small-Parts bundle. Of the 5 owned `SUMMARY.md` Parts, exactly **ONE** requires a change:

- **`# Concepts` (shared library)** — the 44 content concept entries (plus 2 navigation rows `Index`/`Dependency map`, 46 rows total) were in chronological-by-extraction order. **Alpha-sorted (flat, by file slug, C-locale)** to match the already-sorted `concepts/index.md` API table. `Index` + `Dependency map` kept as the navigation header rows (landing + dep-map view, not concepts). **No by-kind nesting** — a flat shared-library reference list is the natural shape (per scope directive: default flat-alpha, no obvious natural kind-split that improves navigation over the flat alpha list; the `Kind` column already lives in the `concepts/index.md` table for readers who want the by-kind cut).
- **`# Meta-Reviews` (23 dated records)** — **KEPT chronological** (cycles 1–3 → 116–127, verified monotonic by cycle range, no mis-sorted row). Chronological-by-cycle-id is the natural order for dated historical records; alpha would destroy it. No change.
- **`# Methodology` (2)** — small-Part guard: **no nesting**. Order `Overview` → `Goal & Flow` follows the universal landing-chapter-first convention (every Part in the book leads with its `Overview`/`Index`). Not a sort violation; no change.
- **`# Feature surfaces — entry points` (4)** — **LEFT AS-IS.** The within-column level ordering `electrostatic.L4` → `electrostatic.L1` → `electrostatic.L0` is the deliberate high→low level sequence (standing OQ `feature-surface-part-path-layout-and-within-column-level-ordering-ratification`); NOT alphabetized. Only one feature column exists, so there is no cross-column alpha sort to do. Small-Part guard: no nesting. No change.
- **`# Design Artifacts` (2)** — small-Part guard: **no nesting**. Order `Index` → `L4 calculus strawman` follows the landing-chapter-first convention. No change.

`concepts/index.md` API table: inspected — **already alpha-sorted** by Concept name (42 rows, C-locale-verified), consistent with the new SUMMARY ordering. No change needed.

No chapter dropped or renamed; the Concepts edit is a pure reordering of the same 44 content links (+ 2 navigation rows).

## Proposed changes

```edit:book/src/SUMMARY.md
[old]:
# Concepts (shared library)
- [Index](./concepts/index.md)
  - [Dependency map](./concepts/dependency-map.md)
  - [rotation — methodology concept](./concepts/rotation.md)
  - [variant absorption — methodology concept](./concepts/variant-absorption.md)
  - [constructed operators — methodology concept](./concepts/constructed-operators.md)
  - [apply_linop](./concepts/apply_linop.md)
  - [axpy](./concepts/axpy.md)
  - [black-box vs accelerated kernels — methodology concept](./concepts/black-box-vs-accelerated-kernels.md)
  - [dot](./concepts/dot.md)
  - [nrm2](./concepts/nrm2.md)
  - [scal](./concepts/scal.md)
  - [givens](./concepts/givens.md)
  - [trsv](./concepts/trsv.md)
  - [gemv_basis](./concepts/gemv_basis.md)
  - [orthogonalization](./concepts/orthogonalization.md)
  - [incremental-least-squares](./concepts/incremental-least-squares.md)
  - [gmres](./concepts/gmres.md)
  - [set_subvector_zero](./concepts/set_subvector_zero.md)
  - [ksp_solve](./concepts/ksp_solve.md)
  - [tensor-field-lift](./concepts/tensor-field-lift.md)
  - [sequential-obstruction](./concepts/sequential-obstruction.md)
  - [state-stratification](./concepts/state-stratification.md)
  - [solve-monad](./concepts/solve-monad.md)
  - [convergence-test](./concepts/convergence-test.md)
  - [chebyshev-iteration](./concepts/chebyshev-iteration.md)
  - [elementwise-product](./concepts/elementwise-product.md)
  - [derived-view-hoisting](./concepts/derived-view-hoisting.md)
  - [solver-as-operator](./concepts/solver-as-operator.md)
  - [two_operator_split](./concepts/two_operator_split.md)
  - [complex-from-real-lift](./concepts/complex-from-real-lift.md)
  - [negative-result-slice](./concepts/negative-result-slice.md)
  - [constructed-operator-factory](./concepts/constructed-operator-factory.md)
  - [finest-level-unwrap](./concepts/finest-level-unwrap.md)
  - [counter-update](./concepts/counter-update.md)
  - [build-time-vs-run-time-stratification](./concepts/build-time-vs-run-time-stratification.md)
  - [first-iteration-unrolling](./concepts/first-iteration-unrolling.md)
  - [givens_generate](./concepts/givens_generate.md)
  - [givens_apply](./concepts/givens_apply.md)
  - [plane-rotation-stream](./concepts/plane-rotation-stream.md)
  - [apply_BA](./concepts/apply_BA.md)
  - [capability-typing](./concepts/capability-typing.md)
  - [scope-out-obstruction](./concepts/scope-out-obstruction.md)
  - [scalar-promotion](./concepts/scalar-promotion.md)
  - [nested-constructed-operator-gate](./concepts/nested-constructed-operator-gate.md)
  - [eigsolve](./concepts/eigsolve.md)
  - [erasure-scope](./concepts/erasure-scope.md)
[new]:
# Concepts (shared library)
- [Index](./concepts/index.md)
  - [Dependency map](./concepts/dependency-map.md)
  - [apply_BA](./concepts/apply_BA.md)
  - [apply_linop](./concepts/apply_linop.md)
  - [axpy](./concepts/axpy.md)
  - [black-box vs accelerated kernels — methodology concept](./concepts/black-box-vs-accelerated-kernels.md)
  - [build-time-vs-run-time-stratification](./concepts/build-time-vs-run-time-stratification.md)
  - [capability-typing](./concepts/capability-typing.md)
  - [chebyshev-iteration](./concepts/chebyshev-iteration.md)
  - [complex-from-real-lift](./concepts/complex-from-real-lift.md)
  - [constructed-operator-factory](./concepts/constructed-operator-factory.md)
  - [constructed operators — methodology concept](./concepts/constructed-operators.md)
  - [convergence-test](./concepts/convergence-test.md)
  - [counter-update](./concepts/counter-update.md)
  - [derived-view-hoisting](./concepts/derived-view-hoisting.md)
  - [dot](./concepts/dot.md)
  - [eigsolve](./concepts/eigsolve.md)
  - [elementwise-product](./concepts/elementwise-product.md)
  - [erasure-scope](./concepts/erasure-scope.md)
  - [finest-level-unwrap](./concepts/finest-level-unwrap.md)
  - [first-iteration-unrolling](./concepts/first-iteration-unrolling.md)
  - [gemv_basis](./concepts/gemv_basis.md)
  - [givens](./concepts/givens.md)
  - [givens_apply](./concepts/givens_apply.md)
  - [givens_generate](./concepts/givens_generate.md)
  - [gmres](./concepts/gmres.md)
  - [incremental-least-squares](./concepts/incremental-least-squares.md)
  - [ksp_solve](./concepts/ksp_solve.md)
  - [negative-result-slice](./concepts/negative-result-slice.md)
  - [nested-constructed-operator-gate](./concepts/nested-constructed-operator-gate.md)
  - [nrm2](./concepts/nrm2.md)
  - [orthogonalization](./concepts/orthogonalization.md)
  - [plane-rotation-stream](./concepts/plane-rotation-stream.md)
  - [rotation — methodology concept](./concepts/rotation.md)
  - [scal](./concepts/scal.md)
  - [scalar-promotion](./concepts/scalar-promotion.md)
  - [scope-out-obstruction](./concepts/scope-out-obstruction.md)
  - [sequential-obstruction](./concepts/sequential-obstruction.md)
  - [set_subvector_zero](./concepts/set_subvector_zero.md)
  - [solve-monad](./concepts/solve-monad.md)
  - [solver-as-operator](./concepts/solver-as-operator.md)
  - [state-stratification](./concepts/state-stratification.md)
  - [tensor-field-lift](./concepts/tensor-field-lift.md)
  - [trsv](./concepts/trsv.md)
  - [two_operator_split](./concepts/two_operator_split.md)
  - [variant absorption — methodology concept](./concepts/variant-absorption.md)
```

## Supporting evidence

- **Concepts block**: 44 content concept entries (lines 232–275 of `book/src/SUMMARY.md`) + `Index` (230) + `Dependency map` (231) = 46 rows. All 44 content entries preserved in the new block; verified by slug-set equality against the old block (no add, no drop). Sort key: file slug, C-locale lexicographic — chosen to match the **already-sorted** `concepts/index.md` API table (verified: table 42 rows, `sort -c` clean; `givens` < `givens_apply` < `givens_generate`, `scal` < `scalar-promotion` collation matches).
  - Note (pre-existing membership drift; corrected per critique): the SUMMARY Concepts block (44 content entries) is a strict **superset** of the `concepts/index.md` table (42 rows). Exactly **two** slugs are present in SUMMARY (and on disk) but **absent from the index table**: `nested-constructed-operator-gate` and `black-box-vs-accelerated-kernels`. (`eigsolve` and `erasure-scope` ARE in the index table — they are not part of the drift.) The reorder only touches SUMMARY ordering; it does not add/remove any link. See Open questions for the routed reconciliation.
- **Meta-Reviews chronological verification**: cycle-range starts extracted from the 23 rows are monotonic non-decreasing (1, 4, 7, 10, 13, 16, 19, 22, 25, 31, 37, 44, 50, 56, 62, 68, 74, 80, 86, 92, 104, 116). No mis-sorted row → kept as-is.
- **Landing-chapter convention**: every Part in the book leads with `Overview` or `Index` as its first chapter (verified across all 14 Parts). Methodology (`Overview`→`Goal & Flow`) and Design (`Index`→`strawman`) conform; their non-alpha first row is the landing convention, not a violation.
- **Feature within-column ordering left AS-IS**: `electrostatic.L4` → `.L1` → `.L0` is the deliberate high→low level sequence; confirmed untouched.

## Open questions / caveats

- **`concepts/index.md` table vs SUMMARY membership drift (pre-existing; out of D6 scope to fix):** The SUMMARY Concepts block carries **44** content concept entries; the `concepts/index.md` API table carries **42** rows. They are NOT a perfect set match — the SUMMARY (44) is a strict **superset** of the table (42). Exactly **two** slugs are present in SUMMARY (and exist on disk as `book/src/concepts/{nested-constructed-operator-gate,black-box-vs-accelerated-kernels}.md`) but are **absent from the index table**: `nested-constructed-operator-gate` AND `black-box-vs-accelerated-kernels`. (`eigsolve`/`erasure-scope` ARE in the table and are not part of the drift.) This is a hand-maintained-derived-surface drift (the same class as the index-table-status-cell drift in the role-spec), pre-existing before this reorg — the reorg is set-preserving (`set(old)==set(new)`), so it neither created nor widened it. D6 deliberately did NOT reconcile membership (scope is reorder-only, no add/drop). **Routed follow-up — batch-22 meta-phase OR a cycle-072 hygiene dispatch:** a `concepts/index.md` table is missing **2** rows that exist in SUMMARY + on disk; re-derive the table rows from the on-disk `concepts/*.md` file set + SUMMARY links, add **both** missing rows (`nested-constructed-operator-gate`, `black-box-vs-accelerated-kernels`), and confirm 1:1 (44 ⟷ 44).
- **No by-kind nesting applied to Concepts:** I left the Concepts Part flat-alpha per the scope directive's default. If the meta-phase later decides the shared-library reference list should be nested by the `Kind` taxonomy (`methodology`/`algorithm`/`primitive`/`layer-pattern`/`auxiliary`) that already exists in the `concepts/index.md` table, that is a deliberate future structural choice, not an omission here — the flat-alpha list is the lower-friction default for a 41-entry reference index.
