---
agent: layer-intro-author
invoked_at: 2026-06-04T232852Z
scope: cycle-097 D5 (Wave 2) — shared-index row removal for the 4 deleted slices (SUMMARY.md + spec/index.md + concepts/dependency-map.md mermaid GC)
status: integrated
integrated_at: 2026-06-04T232852Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean by integrator-per-report (D5, the cycle's final dispatch); repairer fired pre-integration (softened green-build claim to cycle-scope + corrected 44->61 mermaid-edge tally). Removed the 4 deleted-slice rows from SUMMARY.md + spec/index.md + the snake_case mermaid edges from concepts/dependency-map.md (Edit x10) -> the 4 deleted slices FULLY unreachable. 5 survivor rows left intact for c098/c099. Batch finalize cycle-097: cargo make book EXIT 0 (the co-landing constraint held), step-5b rank_violations=0 (GATE PASS), no newly-orphaned node. OQ dependency-map-cg-precond-stale-mermaid-edges (D1-opened) resolved this cycle by this report; closeable at the batch-31 meta unify."
---

# CYCLE: shared-index removal for the 4 c097 slice deletions

## Summary

Cycle-097 (batch-31, graded-stack P2 slice-deletion campaign, first tranche) deletes 4 Phase-1 slice files in Wave 1 (D1–D4):

- `book/src/spec/slices/cg_preconditioning_framework.md` (D1)
- `book/src/spec/slices/divfree.md` (D2)
- `book/src/spec/slices/sparse_triangular_solve.md` (D3)
- `book/src/spec/slices/plane_rotation_stream.md` (D4)

As the **single owner of the shared index files** this cycle, this report (D5, Wave 2) proposes the matching removals in the three shared surfaces — the SUMMARY rows, the spec/index status-table rows, and the stale mermaid edges. Scope note (load-bearing): D5 makes the corpus's **index/SUMMARY/mermaid** references to the 4 deleted slices consistent; the remaining **18 inbound markdown links** to those slices that live in OTHER files (14 `concepts/*.md` pages + `L1/ksp_solve.md:131` + `L1-L0/triangular-solve-obstruction.md:277`) are NOT in D5's three-file scope — they are repointed by sibling dispatches **D1–D4 this same cycle** (D1 the 7 `cg_preconditioning_framework` concept links; D2 `L1/ksp_solve.md` + `L1/divfree-projector.md`; D3 the `triangular-solve-obstruction.md:277` self-link + 3 sparse-trisolve concept anchors; D4 the 5 `plane_rotation_stream` concept links). Because the integrator applies ALL per-report proposed-changes before the single finalize `cargo make book`, the D5 removals co-land with the D1–D4 repointings, so the finalize rebuild stays green at the **cycle** level. (D5 alone does not make the whole corpus consistent — the co-landing of D1–D4 is what closes the remaining inbound links.) The three D5 removals are:

1. `book/src/SUMMARY.md` — remove the 4 slice-row entries (linkcheck2 would hard-error on a SUMMARY entry pointing at a deleted file; these MUST land in the same commit as the D1–D4 deletions — satisfied because the integrator applies all per-report proposed-changes before the single finalize `cargo make book`).
2. `book/src/spec/index.md` — remove the 4 status-table rows and update the slice-count prose (9→5).
3. `book/src/concepts/dependency-map.md` — reachability-GC removal of the stale mermaid edges that reference the 3 deleted snake_case slice node-ids (`divfree`, `cg_preconditioning_framework`, `plane_rotation_stream`). `sparse_triangular_solve` has **zero** mermaid edges (it is the L0-obstruction slice with no rotation chain), so nothing to remove for it.

The 5 surviving slices (`arnoldi_step`, `cg`, `gmres`, `orthog`, `polynomial_recurrence_step`), deferred to c098/c099, are left fully intact — their SUMMARY rows, status-table rows, and mermaid edges are untouched.

**Disambiguation note (load-bearing):** the deleted-slice node-ids are the **snake_case** slugs `divfree` / `cg_preconditioning_framework` / `plane_rotation_stream`. The dependency-map ALSO contains a **hyphenated** `plane-rotation-stream` node (the `:::planned` roadmap marker at `:74-75`/`:92-103` and the L1 `givens_generate`/`givens_apply`/`trsv` stream at `:186-193`) and a hyphenated `sparse-triangular-solve:::planned` node (`:81`/`:99-101`). Those hyphenated nodes are NOT the deleted slices — they are planned/forward-projection roadmap markers and a distinct L1 stream — and are LEFT INTACT. Only the snake_case edges are removed.

## Proposed changes

### 1. `book/src/SUMMARY.md` — remove 4 slice rows

Verified present at `:294`, `:295`, `:298`, `:300` (Read of `book/src/SUMMARY.md:290-300`). The 5 surviving rows at `:292` (Arnoldi step), `:293` (CG), `:296` (GMRES), `:297` (Orthogonalisation), `:299` (Polynomial recurrence step) are preserved by the targeted removals below.

```edit:book/src/SUMMARY.md
[old]:   - [CG — Preconditioned Conjugate Gradient](./spec/slices/cg.md)
  - [CG Preconditioning Framework](./spec/slices/cg_preconditioning_framework.md)
  - [Divergence-free projection](./spec/slices/divfree.md)
  - [GMRES](./spec/slices/gmres.md)
[new]:   - [CG — Preconditioned Conjugate Gradient](./spec/slices/cg.md)
  - [GMRES](./spec/slices/gmres.md)
```

```edit:book/src/SUMMARY.md
[old]:   - [Orthogonalisation (MGS / CGS / CGS2)](./spec/slices/orthog.md)
  - [Plane rotation stream](./spec/slices/plane_rotation_stream.md)
  - [Polynomial recurrence step](./spec/slices/polynomial_recurrence_step.md)
  - [Sparse triangular solve (negative result)](./spec/slices/sparse_triangular_solve.md)
# Concepts (shared library)
[new]:   - [Orthogonalisation (MGS / CGS / CGS2)](./spec/slices/orthog.md)
  - [Polynomial recurrence step](./spec/slices/polynomial_recurrence_step.md)
# Concepts (shared library)
```

### 2. `book/src/spec/index.md` — remove 4 status-table rows

Verified present at `:18` (divfree), `:19` (plane rotation stream), `:21` (sparse triangular solve), `:22` (cg_preconditioning_framework) (Read of full file). The 5 surviving rows at `:15` (CG), `:16` (GMRES), `:17` (Orthogonalization), `:20` (arnoldi step), `:23` (polynomial recurrence step) are preserved.

Note the 4 deleted rows are NOT contiguous (rows `:20` arnoldi step and `:21`/`:22` interleave; `:23` polynomial recurrence step follows `:22`). I therefore split into two edit blocks to keep the surviving `arnoldi step` row in place:

```edit:book/src/spec/index.md
[old]:| [Orthogonalization (plane-rotation stream)](./slices/orthog.md) | L4 (Gram-Schmidt) + L1 (plane-rotation) | 2026-05-26 | Gram-Schmidt stream at L4 (state-stratified, Solve-monadic, sequential-obstruction at L4). Plane-rotation stream lifted to L1 in same slice; uses `givens` and `trsv` primitives. Open question: split into orthog/gram_schmidt and orthog/plane_rotation once both reach L4. |
| [divfree](./slices/divfree.md) | L4 | 2026-05-26 | L4 calculus form: stratified state (DivFreeParams internal-params vs SimState sim-state vs ephemeral intermediates), SolveM-monadic construction and apply, polymorphic complex specialization, composition into eigensolver driver. L4→L4 tightening (cycle 167): scratch buffers folded into ephemeral SolveM-allocations, removing the construction-time materialization that misclassified them as internal-parameter storage. |
| [plane rotation stream](./slices/plane_rotation_stream.md) | L3 | 2026-05-26 | L3 negative result: replay-prefix loop is class-(a) sequential obstruction (shared boundary slot read-after-write); per-step extend/apply triple lifts trivially. Canonical small-N obstruction case. |
| [arnoldi step](./slices/arnoldi_step.md) | L4 | 2026-05-26 | Tightening refinement: clarified scope-separation rationale for the small-dense Givens obstruction vs. field-side MGS obstruction in Open questions. Substantive: the two obstructions live on disjoint state (DoF-space `w`-mediated vs. small-dense `H[:,j]`-mediated) and have different variant-dependency profiles. |
| [sparse triangular solve](./slices/sparse_triangular_solve.md) | L0 (obstruction) | 2026-05-26 | Negative result: no Palace-level sparse triangular solve. Palace forwards into MFEM-wrapped SuperLU/STRUMPACK/MUMPS as opaque ksp_solve. L0→L1 rotation declared out-of-scope-obstructed; follow-up slice `sparse_direct_solver_wrapper` proposed. |
| [cg_preconditioning_framework](./slices/cg_preconditioning_framework.md) | L4 v0.3 | 2026-05-26 | L4 v0.3 self-rotation: derived-view hoisting for `OpBinding<E>`. The `finestLevelUnwrap` branch in `setOperators` is hoisted out of the body into a `pcBoundOp(binding, pc)` derived view; `OpBinding<E>` now stores only the primitive operator inputs, eliminating the stored-vs-bound divergence the v0.2 form left as a structural hazard. |
| [polynomial recurrence step](./slices/polynomial_recurrence_step.md) | L1 (self-tightened) | 2026-05-26 | Negative-result catalog at cross-family scope (Chebyshev / GMRES / eigentracking do not unify); within-Chebyshev partial-positive promoted from Open Question 2 to a structurally-documented L1↔L1 self-tightening section with its own falsification surface. |
[new]:| [Orthogonalization (plane-rotation stream)](./slices/orthog.md) | L4 (Gram-Schmidt) + L1 (plane-rotation) | 2026-05-26 | Gram-Schmidt stream at L4 (state-stratified, Solve-monadic, sequential-obstruction at L4). Plane-rotation stream lifted to L1 in same slice; uses `givens` and `trsv` primitives. Open question: split into orthog/gram_schmidt and orthog/plane_rotation once both reach L4. |
| [arnoldi step](./slices/arnoldi_step.md) | L4 | 2026-05-26 | Tightening refinement: clarified scope-separation rationale for the small-dense Givens obstruction vs. field-side MGS obstruction in Open questions. Substantive: the two obstructions live on disjoint state (DoF-space `w`-mediated vs. small-dense `H[:,j]`-mediated) and have different variant-dependency profiles. |
| [polynomial recurrence step](./slices/polynomial_recurrence_step.md) | L1 (self-tightened) | 2026-05-26 | Negative-result catalog at cross-family scope (Chebyshev / GMRES / eigentracking do not unify); within-Chebyshev partial-positive promoted from Open Question 2 to a structurally-documented L1↔L1 self-tightening section with its own falsification surface. |
```

**Slice-count prose update.** The header prose (`book/src/spec/index.md:1-9`) carries NO running count statement — it describes the corpus qualitatively ("grows as a set of slices") without an integer tally, and the "Status as of 2026-05-26" date line is a frozen-corpus marker, not a count. There is therefore **no 9→5 count statement to update** in the header. The status table itself is the only enumerated surface, and the row removals above bring it from 9 rows to 5 rows. No further prose edit is required for the count. (Flagged for the integrator: if a count statement is desired going forward, that is a new addition, out of this removal-only scope.)

### 3. `book/src/concepts/dependency-map.md` — mermaid reachability-GC (removal-only)

All deleted-slug references are `-->` edges (grep-confirmed: no standalone node declarations, no `:::planned` styling, no `classDef` membership for the snake_case slugs). Removing each edge is build-safe — mermaid node-ids are not markdown links so linkcheck2 is unaffected, and every edge *target* (`apply_linop`, `ksp_solve`, `givens`, `solve-monad`, etc.) remains referenced by surviving slices or is an existing concept, so no target is orphaned. Removals are grouped per mermaid block.

**Block: "L1 — mutation-lifted primitives" (`:128-194`).** Remove the `divfree` edges at `:153-155`, the snake_case `plane_rotation_stream --> givens` at `:165`, and the `cg_preconditioning_framework` edge cluster at `:168-173` and the `divfree` cluster at `:182-185`. LEAVE the hyphenated `plane-rotation-stream` edges at `:186-193` (distinct planned/stream node) and all survivor edges.

```edit:book/src/concepts/dependency-map.md
[old]:  orthog --> variant-absorption
  divfree --> ksp_solve
  divfree --> apply_linop
  divfree --> axpy
  chebyshev --> apply_linop
[new]:  orthog --> variant-absorption
  chebyshev --> apply_linop
```

```edit:book/src/concepts/dependency-map.md
[old]:  arnoldi_step --> variant-absorption
  plane_rotation_stream --> givens
  cg --> state-stratification
  gmres --> state-stratification
  cg_preconditioning_framework --> solver-as-operator
  cg_preconditioning_framework --> two_operator_split
  cg_preconditioning_framework --> complex-from-real-lift
  cg_preconditioning_framework --> constructed-operators
  cg_preconditioning_framework --> variant-absorption
  cg_preconditioning_framework --> apply_linop
  solver-as-operator --> apply_linop
[new]:  arnoldi_step --> variant-absorption
  cg --> state-stratification
  gmres --> state-stratification
  solver-as-operator --> apply_linop
```

```edit:book/src/concepts/dependency-map.md
[old]:  polynomial_recurrence_step --> givens
  divfree --> set_subvector_zero
  divfree --> constructed-operators
  divfree --> variant-absorption
  divfree --> state-stratification
  plane-rotation-stream --> givens_generate
[new]:  polynomial_recurrence_step --> givens
  plane-rotation-stream --> givens_generate
```

**Block: "L2 — algebraic decompositions" (`:198-264`).** Remove the `divfree` clusters at `:217-221` and `:245-246`, the snake_case `plane_rotation_stream --> givens` at `:247`, and the `cg_preconditioning_framework` cluster at `:258-263`. (The `solver-as-operator` / `constructed-operator-factory` / `complex-from-real-lift` / `finest-level-unwrap` / `counter-update` nodes at `:248-257` remain — they are concept nodes referenced elsewhere, not deleted slices.)

```edit:book/src/concepts/dependency-map.md
[old]:  ksp_solve --> apply_linop
  divfree --> apply_linop
  divfree --> set_subvector_zero
  divfree --> ksp_solve
  divfree --> axpy
  divfree --> copy
  chebyshev --> copy
[new]:  ksp_solve --> apply_linop
  chebyshev --> copy
```

```edit:book/src/concepts/dependency-map.md
[old]:  cg --> dot
  divfree --> constructed-operators
  divfree --> variant-absorption
  plane_rotation_stream --> givens
  solver-as-operator --> apply_linop
  solver-as-operator --> rotation
[new]:  cg --> dot
  solver-as-operator --> apply_linop
  solver-as-operator --> rotation
```

```edit:book/src/concepts/dependency-map.md
[old]:  counter-update --> state-stratification
  cg_preconditioning_framework --> apply_linop
  cg_preconditioning_framework --> solver-as-operator
  cg_preconditioning_framework --> constructed-operator-factory
  cg_preconditioning_framework --> complex-from-real-lift
  cg_preconditioning_framework --> finest-level-unwrap
  cg_preconditioning_framework --> counter-update
[new]:  counter-update --> state-stratification
```

**Block: "L3 — global tensor-field operations" (`:273-318`).** Remove the `divfree` cluster at `:281-286`, the `cg_preconditioning_framework` cluster at `:309-313`, and the snake_case `plane_rotation_stream` cluster at `:314-317` (which is the final group in this block).

```edit:book/src/concepts/dependency-map.md
[old]:  gmres-L3 --> sequential-obstruction
  divfree --> apply_linop
  divfree --> set_subvector_zero
  divfree --> ksp_solve
  divfree --> axpy
  divfree --> tensor-field-lift
  divfree --> sequential-obstruction
  orthog --> sequential-obstruction
[new]:  gmres-L3 --> sequential-obstruction
  orthog --> sequential-obstruction
```

```edit:book/src/concepts/dependency-map.md
[old]:  cg --> iterate_while
  cg_preconditioning_framework --> apply_linop
  cg_preconditioning_framework --> solver-as-operator
  cg_preconditioning_framework --> complex-from-real-lift
  cg_preconditioning_framework --> build-time-vs-run-time-stratification
  cg_preconditioning_framework --> sequential-obstruction
  plane_rotation_stream --> sequential-obstruction
  plane_rotation_stream --> givens
  plane_rotation_stream --> tensor-field-lift
  plane_rotation_stream --> trsv
[new]:  cg --> iterate_while
```

**Block: "L4 — formal calculus terms" (`:327-392`).** Remove the `divfree` cluster at `:353-358`, the standalone `divfree --> axpy` at `:377`, the `cg_preconditioning_framework` cluster at `:380-389`, and the standalone `divfree --> derived-view-hoisting` at `:391` (final line of the block).

```edit:book/src/concepts/dependency-map.md
[old]:  gmres --> convergence-test
  orthog --> state-stratification
  orthog --> solve-monad
  orthog --> constructed-operators
  orthog --> sequential-obstruction
  divfree --> solve-monad
  divfree --> state-stratification
  divfree --> constructed-operators
  divfree --> apply_linop
  divfree --> set_subvector_zero
  divfree --> ksp_solve
  chebyshev --> solve-monad
[new]:  gmres --> convergence-test
  orthog --> state-stratification
  orthog --> solve-monad
  orthog --> constructed-operators
  orthog --> sequential-obstruction
  chebyshev --> solve-monad
```

```edit:book/src/concepts/dependency-map.md
[old]:  arnoldi_step --> nrm2
  arnoldi_step --> scal
  divfree --> axpy
  cg --> first-iteration-unrolling
  gmres --> derived-view-hoisting
  cg_preconditioning_framework --> solve-monad
  cg_preconditioning_framework --> state-stratification
  cg_preconditioning_framework --> constructed-operators
  cg_preconditioning_framework --> variant-absorption
  cg_preconditioning_framework --> apply_linop
  cg_preconditioning_framework --> solver-as-operator
  cg_preconditioning_framework --> complex-from-real-lift
  cg_preconditioning_framework --> finest-level-unwrap
  cg_preconditioning_framework --> capability-typing
  cg_preconditioning_framework --> derived-view-hoisting
  chebyshev --> derived-view-hoisting
  divfree --> derived-view-hoisting
[new]:  arnoldi_step --> nrm2
  arnoldi_step --> scal
  cg --> first-iteration-unrolling
  gmres --> derived-view-hoisting
  chebyshev --> derived-view-hoisting
```

## Supporting evidence

- **SUMMARY.md anchors** — Read of `book/src/SUMMARY.md:285-309` confirms the 4 deleted rows at `:294`/`:295`/`:298`/`:300` and the 5 survivors at `:292`/`:293`/`:296`/`:297`/`:299`. The two edit blocks bracket the deletions with surviving rows so the survivors are never matched.
- **spec/index.md anchors** — Read of the full file confirms the status table at `:13-23`; deleted rows `:18`/`:19`/`:21`/`:22`, survivors `:15`/`:16`/`:17`/`:20`/`:23`. Header prose (`:1-9`) carries no integer count (qualitative description + frozen date marker only), so no count statement requires the 9→5 update.
- **dependency-map.md edges** — `grep -nE 'divfree|cg_preconditioning_framework|plane_rotation_stream|sparse_triangular_solve'` returns 61 snake_case hits (per-slug: divfree 28, cg_preconditioning_framework 27, plane_rotation_stream 6); ALL are snake_case `-->` edges for `divfree` / `cg_preconditioning_framework` / `plane_rotation_stream`. A second grep confirms NO standalone node declarations, NO `:::planned` styling, NO `classDef` membership for the deleted slugs (so every reference is a removable edge with no orphaning consequence). `sparse_triangular_solve` (snake) returns ZERO mermaid hits.
- **Survivors left intact** — `arnoldi_step`, `cg`, `gmres`, `orthog`, `polynomial_recurrence_step` edges untouched; the hyphenated `plane-rotation-stream` (`:74-75`/`:92-103`/`:186-193`) and `sparse-triangular-solve:::planned` (`:81`/`:99-101`) roadmap/stream nodes are distinct from the deleted slices and are explicitly preserved.

## Open questions / caveats

- **Campaign is staged, not complete.** This is the FIRST tranche (4 of 9 slices). The 5 surviving slices (`arnoldi_step`, `cg`, `gmres`, `orthog`, `polynomial_recurrence_step`) are deferred to c098/c099; their SUMMARY rows, status-table rows, and mermaid edges remain by design. A future tranche will repeat this shared-index removal pattern for them. When the corpus reaches zero slices, the entire `# Phase 1 corpus` SUMMARY Part + `spec/index.md` + the slice mermaid blocks become candidates for wholesale removal (graded-stack P2 end-state).
- **c096 OQ `l4-preconditioning-framework-promotion` is closeable.** Per D1's repointing of `cg_preconditioning_framework`'s material into its firm L4 home(s), the slice's L4-promotion question is resolved by absorption — flag for the meta-phase intake→plan migration to close it. (Confirming the firm-home target is D1's scope, not mine; I only note the closeability signal.)
- **`roadmap-goal-unbuilt-frontier-SUMMARY-grouping-deferred` OQ stays deferred.** No `roadmap_goal` chapter is minted this cycle — all 4 deleted slices absorb into existing firm homes (planner-confirmed; D1–D4 repoint into firm targets, not into new rank-0 chapters). Per the hard constraint, I did NOT add a `## Roadmap goals — unbuilt frontier` SUMMARY grouping. The OQ remains open/deferred for the cycle that first mints a `roadmap_goal` chapter.
- **No count-prose in spec/index.md header.** Noted above: the header has no integer slice tally to decrement, so the "9→5" update reduces to the status-table row removals alone. If the project later wants an explicit running count in the spec/index.md header, that is a net-new addition outside this removal-only dispatch.
- **Ambiguous-edge check: none found.** Every deleted-slug edge was unambiguously attributable to a deleted snake_case slice (verified against the hyphenated survivors). No edge was left in place under the "if ambiguous, leave it" instruction — all 61 snake_case hits are clean removals.
