# Concept: erasure-scope

The **erasure scope** of a substantive L3>L2 lowering is *how much* of an operator's iteration view the L3>L2 hop erases. It is the classifying axis of the **substantive / non-identity** L3>L2 themes — the themes where the rotation carries real content because the L3 form names a first-class [`sequential-obstruction`](sequential-obstruction.md) (and, where Palace authors the loop, renders an explicit `iterate_while`-family tail recursion), and the L3>L2 hop **erases the iteration view** so the obstruction survives only as L2-vocabulary non-laws.

This axis cuts across the substantive L3>L2 cohort and the [`tensor-field-lift`](tensor-field-lift.md) / [`sequential-obstruction`](sequential-obstruction.md) concepts. It does NOT apply to the thin `-body-identity` themes (the BLAS-1 leaves, the fork-independent standalone floors, the fused composites, the constructed-operator gates): those carry **no** substantive erasure — the operator is L3-native by signature shape (no element loop, no obstruction), the body IS the identity, and there is nothing to erase. Erasure scope is only meaningful where there is an iteration view to erase.

The canonical write-up of the taxonomy lives in `book/src/L3-L2/index.md` §Erasure-scope-taxonomy (lines 67–71; the four roots at 68–71) and §Vocabulary-cohort (lines 56–61). This page is the cross-cutting home; it forwards the per-theme detail to the four substantive L3>L2 theme files.

## The four roots

The four substantive L3>L2 themes populate the four corners of the axis. Each erases a different *scope* of iteration view; each forwards its algebraic detail (the explicit L3 form, the L2 shadow non-laws, the citations) to its theme file.

1. **unconditional-single-loop** — the whole Palace-authored operator *is* the loop; the erasure holds for **every** parameter value.
   - Theme: [`ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md). Operator: `ksp_solve` ([`L3/ksp_solve`](../L3/ksp_solve.md) → [`L2/ksp_solve`](../L2/ksp_solve.md)).
   - The L3 explicit `iterate_while_L3` tail recursion (carrying the outer-loop obstruction) lowers to the L2 outer-driver-by-role composition; the obstruction shadows to the L2 fold non-mergeability / no-fold-lift non-laws. Cycle-021.

2. **variant-conditional-single-loop** — the substantive erasure is confined to **one variant branch**; the other branches lift cleanly on both sides of the hop.
   - Theme: [`orthogonalize-variant-split`](../L3-L2/orthogonalize-variant-split.md). Operator: `orthogonalize` ([`L3/orthogonalize`](../L3/orthogonalize.md) → [`L2/orthogonalize`](../L2/orthogonalize.md)).
   - The MGS `j`-loop is the obstruction (numerical-stability-rooted); CGS/CGS2 are batched global statements that lift. The MGS obstruction shadows to the column-order-non-commutativity non-law + the collective-shape residual axis. The per-step body is identity-in-form across all arms. The **first** substantive theme for a `partial-obstruction` operator. Cycle-044.

3. **unconditional-nested-double-loop** — a **nested double loop** (inner recurrence + outer sweep, both sequential); the erasure holds for every parameter value, but over a nested structure neither single-loop sibling exhibits.
   - Theme: [`chebyshev-nested-recurrence`](../L3-L2/chebyshev-nested-recurrence.md). Operator: `chebyshev` ([`L3/chebyshev`](../L3/chebyshev.md) → [`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md)).
   - The inner degree-`order` `k`-recurrence and the outer `pc_it` Richardson sweep are both explicit `iterate_while_pure_L3` tail recursions carrying first-class obstructions; they lower to the L2 `sweep`-iterated-by-role composition. The two obstructions shadow to the step-reordering / `pc_it`-commutativity / polynomial-expansion non-laws. The inner obstruction shares `orthogonalize`'s numerical-stability root. The per-inner-step body is identity-in-form. Cycle-045.

4. **opaque-library** — the loop lives **entirely outside Palace**; Palace authors no recurrence, so L3 cannot render the loop at all and can only attach an obstruction **marker** at the library boundary, which L2 then erases.
   - Theme: [`eigsolve-opaque-eigen-iteration`](../L3-L2/eigsolve-opaque-eigen-iteration.md). Operator: `eigsolve` ([`L3/eigsolve`](../L3/eigsolve.md) → [`L2/eigsolve`](../L2/eigsolve.md)).
   - The eigen-iteration loop (Krylov-Schur restart, Arnoldi/Lanczos basis extension, Rayleigh-Ritz extraction, convergence test) is inside SLEPc `EPSSolve` / ARPACK `naupd` RCI. The L3 `eigsolve` per-step body `apply_shift_invert = apply_linop ▷ ksp_solve [▷ scale_untransform ▷ project]` lifts cleanly; the loop is named `eigen_iterate` by role with an obstruction marker; L2 references the library fold by role only, erasing the marker (it shadows to the "Opening of the eigen-iteration fold at L2" + fold-merge / restart-associativity non-laws). Obstruction sub-kind `opaque-library-ownership` (per CLAUDE.md) — never re-promotable. Cycle-045.

## Renderable vs. marker — the root-4 distinction

The four roots divide into two structural shapes by **whether L3 can render the loop**:

- **Roots 1–3 (renderable-then-erased).** Palace authors the recurrence, so the L3 form *renders* it — an explicit `iterate_while`-family tail recursion (one loop, one variant branch's loop, or two nested loops) carrying a first-class [`sequential-obstruction`](sequential-obstruction.md) over a Palace-visible loop-carried dependency. The L3>L2 hop **erases the rendered iteration view**; the obstruction survives only as L2-vocabulary non-laws. The recurrence is real, Palace-visible, and the erasure is a deliberate layer-surface choice.

- **Root 4 (marker-only, opaque-library).** Palace authors **no** recurrence — the loop is owned by a third-party library reached through a thin wrapper (SLEPc / ARPACK). The L3 form cannot render the loop as a tail recursion; the `sequential-obstruction` is present only as a **marker** at the library boundary. The L2 hop **erases the marker**. The distinguishing structural fact: a substantive iteration-rotation erasure can arise from a loop Palace never wrote.

This is the `concepts-sequential-obstruction-opaque-library-marker-distinction`: a `sequential-obstruction` rooted in opaque-library-ownership (a marker, root 4) is distinct from a Palace-authored renderable-then-erased recurrence (roots 1–3). The distinction matters for promotion routing — a renderable obstruction (roots 1–3) records the Palace recurrence that L3 chose to surface; an opaque-library marker (root 4) records a boundary that Palace never sees inside and that is `never re-promotable`. See [`sequential-obstruction`](sequential-obstruction.md) §"Sub-kind: out-of-scope-obstruction" for the L0→L1 analogue of the same opaque-library boundary at a different layer edge.

## See also

- [concept: sequential-obstruction](sequential-obstruction.md) — the first-class L3 result that the substantive themes name; the marker-vs-rendering distinction above is rooted here.
- [concept: tensor-field-lift](tensor-field-lift.md) — the transparent L2→L3 lift the substantive themes are the *non-transparent* complement of; where the lift succeeds there is no erasure scope.
- `book/src/L3-L2/index.md` §Erasure-scope-taxonomy (lines 67–71; the four roots at 68–71) + §Vocabulary-cohort (lines 56–61) — the canonical taxonomy write-up this page is the cross-cutting home for.
