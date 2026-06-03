---
agent: layer-intro-author
invoked_at: 2026-06-03T004139Z
scope: cycle-071 D4 — directive-3 mdBook structural reorg of the L1 + L1>L0 Parts (by-kind sub-chapter grouping + global alpha re-sort)
status: integrated
integrated_at: 2026-06-03T021500Z
integration_commit: e0fae18eddb2b5c842d260d5e2a79258d43a6a70
integration_notes: |
  cycle-071 D4 (THE HEAVIEST), applied clean by integrator-per-report (STAGING row 4), finalized by
  integrator-finalize. PURE STRUCTURAL directive-3 reorg of the two largest Parts (L1 36 + L1>L0 37 chapters).
  L1 SUMMARY nested into 7 by-kind groupings (blas1-elementwise 11 / operator-application 3 /
  constructed-operator-gates 6 / krylov-least-squares 3 / nep-interior 6 / fe-assembly 4 / fe-space 3 = 36)
  with 7 new book/src/L1/*-intro.md pages; L1>L0 SUMMARY nested into 3 theme-kind groupings (mutation-rotation 28
  / construction-rotation 5 / obstruction 4 = 37) with 3 new book/src/L1-L0/*-intro.md pages. Both index tables
  regrouped via full-table disk-slice splice (42 L1 rows = 36 main + 6 obstruction; 37 L1>L0 rows; all byte-preserved).
  SLUG-SET DROP-RISK (the cycle's biggest): NO DROP — git-HEAD pre/post slug sets all IDENTICAL across four
  independent diffs per Part (SUMMARY 36+37, dep-map 42+37, cross-checked members==rows). NO count changes, NO
  status flips. citecheck 1 ok / 0 fail (clean). cargo make book exit 0, linkcheck2 clean, all 10 intro pages render.
---

# CYCLE: L1 + L1>L0 directive-3 reorg

## Summary

D4 of the cycle-071 directive-3 structural-reorg wave: the two largest Parts.
This report

1. **Regroups `# L1`'s 36 flat chapters into 7 by-kind sub-chapter groupings** in `book/src/SUMMARY.md`, each with an authored group-intro page (`book/src/L1/<group>-intro.md`), alpha-sorted within each grouping. The groupings are the index's own documented `## Vocabulary cohort` cohorts.
2. **Regroups `# L1 > L0`'s 37 lowering themes into 3 theme-kind groupings** (mutation-rotation / construction-rotation / obstruction — the obstruction group carries both sub-kinds enum-only-stub + opaque-library-ownership), each with a group-intro page, alpha-sorted within each.
3. **Re-sorts the `L1/index.md` operator dep-map table** into the same 7 kind groupings, alpha-within-grouping.
4. **Re-sorts the `L1-L0/index.md` theme-list table** into the same 3 kind groupings, alpha-within-grouping.

**Chapter-preservation accounting (load-bearing — this is the highest drop-risk dispatch):**
- `# L1`: **36 chapters** preserved (SUMMARY lines 122–157) + Overview → 7 groupings totalling **11 + 3 + 6 + 3 + 6 + 4 + 3 = 36**. No chapter dropped, renamed, or re-pathed. 7 new group-intro pages ADDED.
- `# L1 > L0`: **37 themes** preserved (SUMMARY lines 161–197) + Overview → 3 groupings totalling **28 + 5 + 4 = 37**. No theme dropped, renamed, or re-pathed. 3 new group-intro pages ADDED.

### L1 kind groupings (7)

| grouping | intro page | members (alpha) | n |
|---|---|---|---|
| BLAS-1 & elementwise | `L1/blas1-elementwise-intro.md` | axpby, axpbypcz, axpy, bilinear-form, dot, elementwise_product, matrix-weighted-norm, normalize, nrm2, reciprocal, scal | 11 |
| Operator application & assembly | `L1/operator-application-intro.md` | apply_linop, assemble-diagonal, assemble_frequency_operator | 3 |
| Constructed-operator gates | `L1/constructed-operator-gates-intro.md` | chebyshev-smoother, divfree-projector, eigsolve, floquet-correction, jacobi-smoother, ksp_solve | 6 |
| Krylov least-squares leaves | `L1/krylov-least-squares-intro.md` | back_solve, ls_update_column, orthogonalize | 3 |
| Dense-coordinate / NEP interior atoms | `L1/nep-interior-intro.md` | apply_nonlinear_pencil, lu_solve, nleps_deflated_residual, nleps_deflated_solve, nleps_eigenvalue_correction, nleps_jacobian_action | 6 |
| FE-assembly sub-spine | `L1/fe-assembly-intro.md` | eliminate_essential_bc, eliminate_rhs, fe_assemble, weak_form_term | 4 |
| FE-space sub-spine | `L1/fe-space-intro.md` | essential_dofs, fe_collection, fe_space | 3 |

### L1>L0 theme-kind groupings (3)

| grouping | intro page | members (alpha) | n |
|---|---|---|---|
| Mutation-rotation | `L1-L0/mutation-rotation-intro.md` | (28 — see SUMMARY edit) | 28 |
| Construction-rotation | `L1-L0/construction-rotation-intro.md` | essential-dofs-construction-rotation, fe-collection-construction-rotation, fe-operator-assemble-mutation-rotation, fe-space-construction-rotation, weak-form-term-rotation | 5 |
| Obstruction | `L1-L0/obstruction-intro.md` | bicgstab-iteration, fe-assemble-libceed-boundary-obstruction, minres-iteration, triangular-solve-obstruction | 4 |

Small-Part / over-structuring guard observed: smallest grouping is 3 chapters (no 1-item or 2-item groupings manufactured); each of the 7 L1 groupings is a documented `## Vocabulary cohort` motif with ≥3 members; the 3 L1>L0 theme-kinds are the directive's own named theme-kind axes (mutation / construction / obstruction-incl-sub-kinds).

## Proposed changes

### 1. SUMMARY.md — `# L1` Part regrouped (one fenced edit, full block)

```edit:book/src/SUMMARY.md
[old]:
# L1 — Mutation-Lifted Forms
- [Overview](./L1/index.md)
- [axpy](./L1/axpy.md)
- [dot](./L1/dot.md)
- [nrm2](./L1/nrm2.md)
- [axpby](./L1/axpby.md)
- [scal](./L1/scal.md)
- [normalize](./L1/normalize.md)
- [apply_linop](./L1/apply_linop.md)
- [axpbypcz](./L1/axpbypcz.md)
- [ksp_solve](./L1/ksp_solve.md)
- [eigsolve](./L1/eigsolve.md)
- [matrix-weighted-norm](./L1/matrix-weighted-norm.md)
- [bilinear-form](./L1/bilinear-form.md)
- [fe_assemble](./L1/fe_assemble.md)
- [weak_form_term](./L1/weak_form_term.md)
- [fe_space](./L1/fe_space.md)
- [fe_collection](./L1/fe_collection.md)
- [eliminate_essential_bc](./L1/eliminate_essential_bc.md)
- [essential_dofs](./L1/essential_dofs.md)
- [orthogonalize](./L1/orthogonalize.md)
- [chebyshev-smoother](./L1/chebyshev-smoother.md)
- [divfree-projector](./L1/divfree-projector.md)
- [assemble-diagonal](./L1/assemble-diagonal.md)
- [apply_nonlinear_pencil](./L1/apply_nonlinear_pencil.md)
- [nleps_deflated_residual](./L1/nleps_deflated_residual.md)
- [lu_solve](./L1/lu_solve.md)
- [nleps_deflated_solve](./L1/nleps_deflated_solve.md)
- [nleps_jacobian_action](./L1/nleps_jacobian_action.md)
- [nleps_eigenvalue_correction](./L1/nleps_eigenvalue_correction.md)
- [back_solve](./L1/back_solve.md)
- [ls_update_column](./L1/ls-update-column.md)
- [jacobi-smoother](./L1/jacobi-smoother.md)
- [reciprocal](./L1/reciprocal.md)
- [elementwise_product](./L1/elementwise_product.md)
- [floquet-correction](./L1/floquet-correction.md)
- [eliminate_rhs](./L1/eliminate_rhs.md)
- [assemble_frequency_operator](./L1/assemble_frequency_operator.md)
[new]:
# L1 — Mutation-Lifted Forms
- [Overview](./L1/index.md)
- [BLAS-1 & elementwise](./L1/blas1-elementwise-intro.md)
  - [axpby](./L1/axpby.md)
  - [axpbypcz](./L1/axpbypcz.md)
  - [axpy](./L1/axpy.md)
  - [bilinear-form](./L1/bilinear-form.md)
  - [dot](./L1/dot.md)
  - [elementwise_product](./L1/elementwise_product.md)
  - [matrix-weighted-norm](./L1/matrix-weighted-norm.md)
  - [normalize](./L1/normalize.md)
  - [nrm2](./L1/nrm2.md)
  - [reciprocal](./L1/reciprocal.md)
  - [scal](./L1/scal.md)
- [Operator application & assembly](./L1/operator-application-intro.md)
  - [apply_linop](./L1/apply_linop.md)
  - [assemble-diagonal](./L1/assemble-diagonal.md)
  - [assemble_frequency_operator](./L1/assemble_frequency_operator.md)
- [Constructed-operator gates](./L1/constructed-operator-gates-intro.md)
  - [chebyshev-smoother](./L1/chebyshev-smoother.md)
  - [divfree-projector](./L1/divfree-projector.md)
  - [eigsolve](./L1/eigsolve.md)
  - [floquet-correction](./L1/floquet-correction.md)
  - [jacobi-smoother](./L1/jacobi-smoother.md)
  - [ksp_solve](./L1/ksp_solve.md)
- [Krylov least-squares leaves](./L1/krylov-least-squares-intro.md)
  - [back_solve](./L1/back_solve.md)
  - [ls_update_column](./L1/ls-update-column.md)
  - [orthogonalize](./L1/orthogonalize.md)
- [Dense-coordinate / NEP interior atoms](./L1/nep-interior-intro.md)
  - [apply_nonlinear_pencil](./L1/apply_nonlinear_pencil.md)
  - [lu_solve](./L1/lu_solve.md)
  - [nleps_deflated_residual](./L1/nleps_deflated_residual.md)
  - [nleps_deflated_solve](./L1/nleps_deflated_solve.md)
  - [nleps_eigenvalue_correction](./L1/nleps_eigenvalue_correction.md)
  - [nleps_jacobian_action](./L1/nleps_jacobian_action.md)
- [FE-assembly sub-spine](./L1/fe-assembly-intro.md)
  - [eliminate_essential_bc](./L1/eliminate_essential_bc.md)
  - [eliminate_rhs](./L1/eliminate_rhs.md)
  - [fe_assemble](./L1/fe_assemble.md)
  - [weak_form_term](./L1/weak_form_term.md)
- [FE-space sub-spine](./L1/fe-space-intro.md)
  - [essential_dofs](./L1/essential_dofs.md)
  - [fe_collection](./L1/fe_collection.md)
  - [fe_space](./L1/fe_space.md)
```

### 2. SUMMARY.md — `# L1 > L0` Part regrouped (one fenced edit, full block)

```edit:book/src/SUMMARY.md
[old]:
# L1 > L0 — Lowering
- [Overview](./L1-L0/index.md)
- [axpby-mutation-rotation](./L1-L0/axpby-mutation-rotation.md)
- [axpbypcz-mutation-rotation](./L1-L0/axpbypcz-mutation-rotation.md)
- [apply-linop-mutation-rotation](./L1-L0/apply-linop-mutation-rotation.md)
- [ksp-solve-mutation-rotation](./L1-L0/ksp-solve-mutation-rotation.md)
- [eigsolve-mutation-rotation](./L1-L0/eigsolve-mutation-rotation.md)
- [eigsolve-convergence-reason-mapping](./L1-L0/eigsolve-convergence-reason-mapping.md)
- [orthogonalize-mutation-rotation](./L1-L0/orthogonalize-mutation-rotation.md)
- [bicgstab-iteration](./L1-L0/bicgstab-iteration.md)
- [minres-iteration](./L1-L0/minres-iteration.md)
- [triangular-solve-obstruction](./L1-L0/triangular-solve-obstruction.md)
- [fe-assemble-libceed-boundary-obstruction](./L1-L0/fe-assemble-libceed-boundary-obstruction.md)
- [weak-form-term-rotation](./L1-L0/weak-form-term-rotation.md)
- [fe-space-construction-rotation](./L1-L0/fe-space-construction-rotation.md)
- [essential-dofs-construction-rotation](./L1-L0/essential-dofs-construction-rotation.md)
- [fe-collection-construction-rotation](./L1-L0/fe-collection-construction-rotation.md)
- [chebyshev-smoother-mutation-rotation](./L1-L0/chebyshev-smoother-mutation-rotation.md)
- [jacobi-smoother-mutation-rotation](./L1-L0/jacobi-smoother-mutation-rotation.md)
- [reciprocal-elementwise-product-mutation-rotation](./L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
- [floquet-correction-mutation-rotation](./L1-L0/floquet-correction-mutation-rotation.md)
- [assemble-frequency-operator-rotation](./L1-L0/assemble-frequency-operator-rotation.md)
- [divfree-projector-mutation-rotation](./L1-L0/divfree-projector-mutation-rotation.md)
- [dot-mutation-rotation](./L1-L0/dot-mutation-rotation.md)
- [nleps-deflated-residual-mutation-rotation](./L1-L0/nleps-deflated-residual-mutation-rotation.md)
- [nrm2-mutation-rotation](./L1-L0/nrm2-mutation-rotation.md)
- [scal-mutation-rotation](./L1-L0/scal-mutation-rotation.md)
- [assemble-diagonal-mutation-rotation](./L1-L0/assemble-diagonal-mutation-rotation.md)
- [matrix-weighted-norm-mutation-rotation](./L1-L0/matrix-weighted-norm-mutation-rotation.md)
- [bilinear-form-mutation-rotation](./L1-L0/bilinear-form-mutation-rotation.md)
- [fe-operator-assemble-mutation-rotation](./L1-L0/fe-operator-assemble-mutation-rotation.md)
- [normalize-mutation-rotation](./L1-L0/normalize-mutation-rotation.md)
- [back-solve-mutation-rotation](./L1-L0/back-solve-mutation-rotation.md)
- [ls-update-column-mutation-rotation](./L1-L0/ls-update-column-mutation-rotation.md)
- [lu-solve-mutation-rotation](./L1-L0/lu-solve-mutation-rotation.md)
- [nleps-deflated-solve-mutation-rotation](./L1-L0/nleps-deflated-solve-mutation-rotation.md)
- [apply-nonlinear-pencil-mutation-rotation](./L1-L0/apply-nonlinear-pencil-mutation-rotation.md)
- [nleps-jacobian-action-mutation-rotation](./L1-L0/nleps-jacobian-action-mutation-rotation.md)
- [nleps-eigenvalue-correction-mutation-rotation](./L1-L0/nleps-eigenvalue-correction-mutation-rotation.md)
[new]:
# L1 > L0 — Lowering
- [Overview](./L1-L0/index.md)
- [Mutation-rotation themes](./L1-L0/mutation-rotation-intro.md)
  - [apply-linop-mutation-rotation](./L1-L0/apply-linop-mutation-rotation.md)
  - [apply-nonlinear-pencil-mutation-rotation](./L1-L0/apply-nonlinear-pencil-mutation-rotation.md)
  - [assemble-diagonal-mutation-rotation](./L1-L0/assemble-diagonal-mutation-rotation.md)
  - [assemble-frequency-operator-rotation](./L1-L0/assemble-frequency-operator-rotation.md)
  - [axpby-mutation-rotation](./L1-L0/axpby-mutation-rotation.md)
  - [axpbypcz-mutation-rotation](./L1-L0/axpbypcz-mutation-rotation.md)
  - [back-solve-mutation-rotation](./L1-L0/back-solve-mutation-rotation.md)
  - [bilinear-form-mutation-rotation](./L1-L0/bilinear-form-mutation-rotation.md)
  - [chebyshev-smoother-mutation-rotation](./L1-L0/chebyshev-smoother-mutation-rotation.md)
  - [divfree-projector-mutation-rotation](./L1-L0/divfree-projector-mutation-rotation.md)
  - [dot-mutation-rotation](./L1-L0/dot-mutation-rotation.md)
  - [eigsolve-convergence-reason-mapping](./L1-L0/eigsolve-convergence-reason-mapping.md)
  - [eigsolve-mutation-rotation](./L1-L0/eigsolve-mutation-rotation.md)
  - [floquet-correction-mutation-rotation](./L1-L0/floquet-correction-mutation-rotation.md)
  - [jacobi-smoother-mutation-rotation](./L1-L0/jacobi-smoother-mutation-rotation.md)
  - [ksp-solve-mutation-rotation](./L1-L0/ksp-solve-mutation-rotation.md)
  - [ls-update-column-mutation-rotation](./L1-L0/ls-update-column-mutation-rotation.md)
  - [lu-solve-mutation-rotation](./L1-L0/lu-solve-mutation-rotation.md)
  - [matrix-weighted-norm-mutation-rotation](./L1-L0/matrix-weighted-norm-mutation-rotation.md)
  - [nleps-deflated-residual-mutation-rotation](./L1-L0/nleps-deflated-residual-mutation-rotation.md)
  - [nleps-deflated-solve-mutation-rotation](./L1-L0/nleps-deflated-solve-mutation-rotation.md)
  - [nleps-eigenvalue-correction-mutation-rotation](./L1-L0/nleps-eigenvalue-correction-mutation-rotation.md)
  - [nleps-jacobian-action-mutation-rotation](./L1-L0/nleps-jacobian-action-mutation-rotation.md)
  - [normalize-mutation-rotation](./L1-L0/normalize-mutation-rotation.md)
  - [nrm2-mutation-rotation](./L1-L0/nrm2-mutation-rotation.md)
  - [orthogonalize-mutation-rotation](./L1-L0/orthogonalize-mutation-rotation.md)
  - [reciprocal-elementwise-product-mutation-rotation](./L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
  - [scal-mutation-rotation](./L1-L0/scal-mutation-rotation.md)
- [Construction-rotation themes](./L1-L0/construction-rotation-intro.md)
  - [essential-dofs-construction-rotation](./L1-L0/essential-dofs-construction-rotation.md)
  - [fe-collection-construction-rotation](./L1-L0/fe-collection-construction-rotation.md)
  - [fe-operator-assemble-mutation-rotation](./L1-L0/fe-operator-assemble-mutation-rotation.md)
  - [fe-space-construction-rotation](./L1-L0/fe-space-construction-rotation.md)
  - [weak-form-term-rotation](./L1-L0/weak-form-term-rotation.md)
- [Obstruction themes](./L1-L0/obstruction-intro.md)
  - [bicgstab-iteration](./L1-L0/bicgstab-iteration.md)
  - [fe-assemble-libceed-boundary-obstruction](./L1-L0/fe-assemble-libceed-boundary-obstruction.md)
  - [minres-iteration](./L1-L0/minres-iteration.md)
  - [triangular-solve-obstruction](./L1-L0/triangular-solve-obstruction.md)
```

### 3. New L1 group-intro page bodies (7)

```edit:book/src/L1/blas1-elementwise-intro.md
[old]:
[new]:
# L1 — BLAS-1 & elementwise

The element-local and reduction primitives of L1: pure-functional lifts of Palace's BLAS-1 vector operations and the elementwise (Hadamard / reciprocal) kernels. Two of the index's six semantic motifs live here — **element-wise pure update** (`axpy`, `axpby`, `axpbypcz`, `scal`, `elementwise_product`, `reciprocal`: every output element depends on one input element per tensor argument, reduction-free) and **mutation-free reduction** (`dot`, `nrm2`, plus the matrix-weighted `matrix-weighted-norm` / `bilinear-form`: reduction over the length axis to a scalar, with reduction-tree non-associativity recorded as a load-bearing non-law). `normalize` is the fused norm-then-scale primitive that returns the norm as a first-class result.

Subsumption is captured as algebraic law, not dep-map edge: `axpy ≺ axpby ≺ axpbypcz`, `scal = axpby(β=0)`, and `scal(α,x) = elementwise_product(broadcast(α,N), x)` — the subsumed and subsuming operators stay as siblings in the table.

The two matrix-weighted reductions (`matrix-weighted-norm` `‖x‖_B = √(xᴴBx)`, `bilinear-form` `xᴴMy`) are the `M`-weighted generalisations of `nrm2` / `dot`; both are `rough-in (test-coverage-bounded)` pending dedicated coverage of the `linalg::` weighted overloads.

Chapters are listed alphabetically.
```

```edit:book/src/L1/operator-application-intro.md
[old]:
[new]:
# L1 — Operator application & assembly

The opaque-operator surface of L1: forms that take a `LinearOperator[N, N]` as an opaque value and either apply it, introspect it, or assemble one. `apply_linop` (`y = A·x`) is the operator/action gate to the L2 `krylov-step` vocabulary; `assemble-diagonal` (`d = diag(A)`) is its operator/data sibling — same opaque argument, opposite side of the operator/data divide (it consumes no vector, so it is explicitly **not** an `apply_linop` variant). `assemble_frequency_operator` (`A(ω) = K + iω·C − ω²·M + A2(ω)`) is the driven per-ω **operator-operand specialization of `linear_combination`** — a scalar-weighted sum of a fixed operator basis under affine-in-ω weights, single-pipeline-by-design (driven only), NOT a new fold.

Chapters are listed alphabetically.
```

```edit:book/src/L1/constructed-operator-gates-intro.md
[old]:
[new]:
# L1 — Constructed-operator gates

The **constructed-operator absorption** motif (index motif 4): forms whose primary argument is a structured opaque value — a `Solver[A]`, `EigSolver`, `ChebSmoother`, `JacobiSmoother`, `DivFreeProjector`, or `FloquetCorrector` — whose per-method body, preconditioner, tolerances, and iteration cap are bound at construction. The L1 signature is variant-free; the per-method body unfolds at L2 (`krylov-step`). Results are structured values, not L0 in-place destinations + side-effect loggers + mutating counters.

The six gates, in increasing internal richness: `jacobi-smoother` (thinnest — one elementwise product, no sweep), `chebyshev-smoother` (fixed-degree polynomial action), `ksp_solve` (solve-to-convergence), `eigsolve` (composes `ksp_solve` for spectral-transform modes — first two-layer constructed-operator absorption), `divfree-projector` and `floquet-correction` (the `nested-constructed-operator-gate` shape — the closure carries another `Solver[·]` as a sub-field).

Chapters are listed alphabetically.
```

```edit:book/src/L1/krylov-least-squares-intro.md
[old]:
[new]:
# L1 — Krylov least-squares leaves

The per-column and restart-close leaves of the GMRES/FGMRES Krylov state advance — the L1 projections of the firm L2 named composition `incremental-least-squares`. `orthogonalize` is the basis-streaming leaf (Gram–Schmidt of a candidate against a stored basis, `MGS | CGS | CGS2` variant axis); `ls_update_column` is the factorisation-streaming producer (one running-QR column: replay ▷ generate ▷ apply, exposing the LS residual norm as a unitary byproduct); `back_solve` is the terminal consumer (the upper-triangular `R·y = s` restart-correction back-solve). The producer/consumer relation `ls_update_column ▷ back_solve` and the per-column co-invocation with `orthogonalize` inside `krylov-step` are dep-map siblings, not dependencies.

`back_solve` is explicitly **not** a general `trsv` (the unanchored sparse-triangular smoother kernel; that obstruction stays open) and is small-dense-triangular only.

Chapters are listed alphabetically.
```

```edit:book/src/L1/nep-interior-intro.md
[old]:
[new]:
# L1 — Dense-coordinate & NEP interior atoms

The coordinate-space dense-direct primitive `lu_solve` (index motif 6 — a small dense `k×k` matrix in *coordinate* space, `k` = deflation rank / ROM basis size, with a load-bearing factorization-kernel variant axis: full-pivot LU / full-pivot QR / LDLT) and the five interior atoms of Palace's quasi-Newton nonlinear-eigenvalue-problem (NEP) solver, which compose against it. The per-step quasi-Newton chain is `residual → jacobian-action → eigenvalue-correction → deflated-solve → line-search`: `apply_nonlinear_pencil` (the NEP `apply_linop`), `nleps_deflated_residual` (deflation-extension residual), `nleps_jacobian_action` (derivative-pencil Jacobian action), `nleps_eigenvalue_correction` (the scalar Newton half), and `nleps_deflated_solve` (the block Schur-complement solve). All five factor through firm BLAS-1 leaves and `lu_solve`; their `k = 0` cases degenerate to the bare big-space forms.

Chapters are listed alphabetically.
```

```edit:book/src/L1/fe-assembly-intro.md
[old]:
[new]:
# L1 — FE-assembly sub-spine

The finite-element **assembly** surface (the MFEM-equivalent assembly sub-spine, in scope per CLAUDE.md mesh/FE). `fe_assemble` is the integrator-fold assembler `K = Σ_i A(space, term_i)`; `weak_form_term` is its element type, the `(coefficient, differential-operator)` pair with the `Gradient | Identity | Curl | Divergence` differential-operator variant axis. `eliminate_essential_bc` and `eliminate_rhs` are the two **separable BC-treatment post-compositions** that compose AFTER the fold (NOT part of it) — one pins the operator's essential rows/cols per a diagonal policy, one lifts inhomogeneous Dirichlet data into the RHS.

The per-term assembly leaf `A(space, ·)` inside the fold is libCEED-owned (the `fe-assemble-libceed-boundary-obstruction` theme, `opaque-library-ownership`) — a strict sub-term below the fold's leaf, which does NOT downgrade `fe_assemble` from firm. This sub-spine sits downstream of the FE-space sub-spine, which constructs the space the fold folds over.

Chapters are listed alphabetically.
```

```edit:book/src/L1/fe-space-intro.md
[old]:
[new]:
# L1 — FE-space sub-spine

The finite-element **space-construction** surface — the shared substrate every assembled-operator pipeline stands on, upstream of the FE-assembly sub-spine. Where FE-assembly folds weak-form terms into an operator over a space, this sub-spine constructs the space itself and the boundary-condition dof-set on it. The three members form a small producer→consumer DAG: `fe_collection` schedules the finest-to-coarsest `[FECollection]` p-multigrid order list (`(p, dim, mg_max_levels, coarsening, family) → [FECollection]`); `fe_space` constructs each typed `(mesh, FECollection) → FiniteElementSpace[N]` (de-Rham family variant axis H1/H(curl)/H(div)/L2); `essential_dofs` marks the essential-true-dof set `(space, bdr_attrs, bdr_attr_max) → DofSet[N]` on a constructed space.

These de-opaque the bare typed `space` / `N` / `DofSet[N]` parameters that `fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, and `eliminate_rhs` previously took opaquely. The dof-numbering / ordering / conformity / prolongation-restriction internals are MFEM-owned-read-as-given (no `dof_map` mirror — that would be the identity-in-named-terms smell).

Chapters are listed alphabetically.
```

### 4. New L1>L0 group-intro page bodies (3)

```edit:book/src/L1-L0/mutation-rotation-intro.md
[old]:
[new]:
# L1 > L0 — Mutation-rotation themes

The bulk of the L1>L0 lowering: themes that rewrite a pure-functional L1 form into its L0 in-place-mutation C++ source pattern. The recurring rewrite shapes are the ones the Part overview names — in-place axpy as `x.Add(α, y)`, operator application as `A.Mult(x, y)` (output-arg convention), workspace-buffer reuse as mention-and-erase, and the constructed-operator absorption rules (timer erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding). Each theme carries `palace/<file>.cpp:<lines>` evidence and records load-bearing numerical tricks (pinned reduction-tree non-associativity, descending back-substitution order) as explicit non-laws.

Themes are listed alphabetically.
```

```edit:book/src/L1-L0/construction-rotation-intro.md
[old]:
[new]:
# L1 > L0 — Construction-rotation themes

The FE-construction lowerings: themes that rewrite a pure declarative L1 construction value (a space, a collection schedule, an assembled operator, a weak-form term, an essential-dof set) into the imperative MFEM/Palace build sequence at L0. Each carries a **construction-lowers / bookkeeping-read-as-given split** — the Palace-side pairing / case-selection / schedule lowers here, while the MFEM-owned dof bookkeeping (numbering, ordering, conformity, prolongation/restriction) or the libCEED-owned per-term quadrature kernel is read-as-given at its boundary (the analogue of the libCEED-leaf boundary). These are genuine vocabulary translations — declarative value → imperative build loop — not 1:1 named-term renames.

Themes are listed alphabetically.
```

```edit:book/src/L1-L0/obstruction-intro.md
[old]:
[new]:
# L1 > L0 — Obstruction themes

Claim-free obstruction documentation: themes where the L1 form has **no positive Palace L0 realisation**, with negative-anchor citations cataloguing the boundary so future producers don't re-localize. Two sub-kinds (per CLAUDE.md §Methodology invariants):

- **`enum-only-stub`** — Palace names the functionality in its configuration surface but the method body is `MFEM_ABORT` / `// TODO`: `minres-iteration`, `bicgstab-iteration` (both route to `MFEM_ABORT` at `palace/linalg/ksp.cpp:53-57`). Promotion route: a future Palace upstream change fills the body.
- **`opaque-library-ownership`** — the functionality is available to Palace only through a library boundary, never as a standalone Palace callable: `triangular-solve-obstruction` (HYPRE GS/SSOR relax-types + external direct-solver wrappers) and `fe-assemble-libceed-boundary-obstruction` (the libCEED element-local quadrature kernel below the firm `fe_assemble` fold). Promotion route: none conventional — the theme's value is documenting the boundary.

Themes are listed alphabetically.
```

### 5. L1/index.md — operator dep-map table re-sorted by kind grouping, alpha-within

The dep-map table (current lines 102–145) is re-sorted into the 7 kind groupings, alpha-within-grouping, with a `**<grouping>**` sub-header row before each block. Every existing row is preserved verbatim (signature / dependencies / status cells unchanged); only row ORDER changes and group sub-headers are inserted. The header row + the obstruction rough-in rows (`lanczos_step` … `stabilisation_update`) move into a trailing **Rough-in (obstruction)** block.

```edit:book/src/L1/index.md
[old]:
## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
[new]:
## Operator dep-map

Sorted by kind grouping (mirroring the SUMMARY sub-chapter groupings), alphabetically within each grouping.

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| **BLAS-1 & elementwise** | | | |
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
```

The integrator should then MOVE the existing rows so the final table body reads in this exact order (rows copied verbatim from the current table; sub-header rows are the only insertions):

- **BLAS-1 & elementwise**: `axpy`, `axpby`, `axpbypcz`, `bilinear-form`, `dot`, `elementwise_product`, `matrix-weighted-norm`, `normalize`, `nrm2`, `reciprocal`, `scal`
- **Operator application & assembly**: `apply_linop`, `assemble-diagonal`, `assemble_frequency_operator`
- **Constructed-operator gates**: `chebyshev-smoother`, `divfree-projector`, `eigsolve`, `floquet-correction`, `jacobi-smoother`, `ksp_solve`
- **Krylov least-squares leaves**: `back_solve`, `ls_update_column`, `orthogonalize`
- **Dense-coordinate / NEP interior atoms**: `apply_nonlinear_pencil`, `lu_solve`, `nleps_deflated_residual`, `nleps_deflated_solve`, `nleps_eigenvalue_correction`, `nleps_jacobian_action`
- **FE-assembly sub-spine**: `eliminate_essential_bc`, `eliminate_rhs`, `fe_assemble`, `weak_form_term`
- **FE-space sub-spine**: `essential_dofs`, `fe_collection`, `fe_space`
- **Rough-in (obstruction)**: `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`, `bicgstab_step`, `omega_update`, `stabilisation_update`

> **Integrator note (mechanical move, no content change):** every row body (signature / dependencies / status cells) is identical to the current table — this is a pure re-ordering of the existing 42 data rows + insertion of 8 `| **<grouping>** | | | |` sub-header rows. No row text is rewritten. The current table has exactly these 42 data rows (36 firm/rough-in main + 6 obstruction); after the move the table has 42 data rows + 8 sub-headers. The first row (`axpy`) is already placed under the `**BLAS-1 & elementwise**` sub-header by the anchored edit above; the remaining 36 data rows move beneath their sub-headers in the order listed.

### 6. L1-L0/index.md — theme-list table re-sorted by kind grouping, alpha-within

The theme table (current lines 16–54) is re-sorted into the 3 theme-kind groupings, alpha-within, with a `**<grouping>**` sub-header row before each block. Every existing row preserved verbatim.

```edit:book/src/L1-L0/index.md
[old]:
## Theme list

| theme | L1 anchor | L0 anchor | status |
|---|---|---|---|
| [axpby-mutation-rotation](./axpby-mutation-rotation.md) | `L1/axpy` (+ `axpby`/`axpbypcz` fwd-ref) | `palace/linalg/vector.{hpp,cpp}`, `operator.cpp`, `rap.cpp` | firm *(structural; 3 sub-patterns A/B/C; `α==1`/`α==-1` algebraic sub-rules; complex-α + Subtract forms defined-not-used)* |
[new]:
## Theme list

Sorted by theme-kind grouping (mutation-rotation / construction-rotation / obstruction), alphabetically within each grouping.

| theme | L1 anchor | L0 anchor | status |
|---|---|---|---|
| **Mutation-rotation** | | | |
| [axpby-mutation-rotation](./axpby-mutation-rotation.md) | `L1/axpy` (+ `axpby`/`axpbypcz` fwd-ref) | `palace/linalg/vector.{hpp,cpp}`, `operator.cpp`, `rap.cpp` | firm *(structural; 3 sub-patterns A/B/C; `α==1`/`α==-1` algebraic sub-rules; complex-α + Subtract forms defined-not-used)* |
```

The integrator should then MOVE the existing theme rows so the final table body reads in this exact order (rows copied verbatim; sub-header rows are the only insertions):

- **Mutation-rotation** (28): `apply-linop-mutation-rotation`, `apply-nonlinear-pencil-mutation-rotation`, `assemble-diagonal-mutation-rotation`, `assemble-frequency-operator-rotation`, `axpby-mutation-rotation`, `axpbypcz-mutation-rotation`, `back-solve-mutation-rotation`, `bilinear-form-mutation-rotation`, `chebyshev-smoother-mutation-rotation`, `divfree-projector-mutation-rotation`, `dot-mutation-rotation`, `eigsolve-convergence-reason-mapping`, `eigsolve-mutation-rotation`, `floquet-correction-mutation-rotation`, `jacobi-smoother-mutation-rotation`, `ksp-solve-mutation-rotation`, `ls-update-column-mutation-rotation`, `lu-solve-mutation-rotation`, `matrix-weighted-norm-mutation-rotation`, `nleps-deflated-residual-mutation-rotation`, `nleps-deflated-solve-mutation-rotation`, `nleps-eigenvalue-correction-mutation-rotation`, `nleps-jacobian-action-mutation-rotation`, `normalize-mutation-rotation`, `nrm2-mutation-rotation`, `orthogonalize-mutation-rotation`, `reciprocal-elementwise-product-mutation-rotation`, `scal-mutation-rotation`
- **Construction-rotation** (5): `essential-dofs-construction-rotation`, `fe-collection-construction-rotation`, `fe-operator-assemble-mutation-rotation`, `fe-space-construction-rotation`, `weak-form-term-rotation`
- **Obstruction** (4): `bicgstab-iteration`, `fe-assemble-libceed-boundary-obstruction`, `minres-iteration`, `triangular-solve-obstruction`

> **Integrator note (mechanical move, no content change):** every theme row body (L1-anchor / L0-anchor / status cells) is identical to the current table — pure re-ordering of the existing 37 data rows + insertion of 3 `| **<grouping>** | | | |` sub-header rows. `axpby-mutation-rotation` is placed under `**Mutation-rotation**` by the anchored edit above; the remaining 36 data rows move beneath their sub-headers in the order listed. After the move: 37 data rows + 3 sub-headers.

## Supporting evidence

- L1 chapters surveyed from `book/src/SUMMARY.md` lines 122–157 (36 chapters) and `book/src/L1/index.md` §Vocabulary cohort (lines 31–98) + dep-map (lines 102–145). The 7 kind groupings are the index's own documented cohorts: BLAS-1 / elementwise (motifs 1–2), operator-application (motifs 4-feeder + 5), constructed-operator gates (motif 4), Krylov least-squares leaves, NEP interior atoms (motif 6 + the 5 nleps atoms), FE-assembly sub-spine (index §"Firm (FE-assembly sub-spine)"), FE-space sub-spine (index §"Firm (FE-space sub-spine)").
- L1>L0 themes surveyed from `book/src/SUMMARY.md` lines 161–197 (37 themes) and `book/src/L1-L0/index.md` theme table (lines 16–54). The 3 theme-kinds (mutation / construction / obstruction-incl-sub-kinds) are the directive's own named theme-kind axes and align with the CLAUDE.md obstruction-sub-kind invariant.
- Path note verified: `ls_update_column`'s file path is `./L1/ls-update-column.md` (hyphen in path, underscore in slug) — preserved verbatim in both the SUMMARY entry and the dep-map row.
- Count discipline: this dispatch does NOT touch any chapter `## Status` line, dep-map status cell text, or the §Vocabulary-cohort consolidated firm tally — it is a pure structural reorg (re-order + nest + add intros). No status flip, no tally re-projection. The §Vocabulary-cohort bullet lists in `index.md` are orientation prose (NOT the alpha-sorted API table) and are left unchanged per the directive's "list-of-API / dep-map tables" scope.

## Open questions / caveats

- **Group-intro pages are new files; SUMMARY references them as live links.** Per CLAUDE.md "Integration may materialize implied components as stubs" the converse holds here: the intro bodies are authored in §3/§4 of this report, so the integrator should create the 10 new files (`book/src/L1/{blas1-elementwise,operator-application,constructed-operator-gates,krylov-least-squares,nep-interior,fe-assembly,fe-space}-intro.md` + `book/src/L1-L0/{mutation-rotation,construction-rotation,obstruction}-intro.md`) from the provided bodies BEFORE the `linkcheck2` rebuild, so the new SUMMARY links resolve. These are real authored pages, not stubs.
- **`assemble_frequency_operator` placement.** Placed in "Operator application & assembly" (it assembles a `LinearOperator[N,N]` and its operands/result are opaque square operators) rather than BLAS-1 (despite being the operator-operand specialization of `linear_combination`). Rationale: the operator-domain codomain groups it with `apply_linop` / `assemble-diagonal`, and the BLAS-1 group is already the largest (11). Borderline; flagged for the integrator/critic if a different home is preferred.
- **`fe-operator-assemble-mutation-rotation` placement.** Its slug carries `-mutation-rotation` but it is the FE-operator-assembly construction rewrite (LHS = `fe_assemble` + `eliminate_essential_bc` + `eliminate_rhs`), so it is grouped under **Construction-rotation** with its FE siblings rather than the generic mutation-rotation block. This is a content-kind judgment over a slug-name match; flagged in case strict slug-suffix grouping is preferred.
- **Mixed transitional state elsewhere is untouched.** Other Parts (L0, L2, L3, L4 and the other lowerings) remain flat per-Part lists in the transitional mixed alpha/chronological state; the 5 sibling dispatches of this wave own those. This report touches ONLY the `# L1` and `# L1 > L0` SUMMARY blocks + `L1/index.md` + `L1-L0/index.md`.
