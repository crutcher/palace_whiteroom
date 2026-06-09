---
kind: navigational-container (lowering index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2-L1/chebyshev-iteration-fusion
    - L2-L1/deflate-composition-lowering
    - L2-L1/divfree-projector-leaf-identity
    - L2-L1/eigsolve-spectral-transform-composition
    - L2-L1/gram-fold-specialization
    - L2-L1/incremental-least-squares-composition-lowering
    - L2-L1/inner-product-fold-specialization
    - L2-L1/krylov-step-kernel-defusion
    - L2-L1/ksp-solve-outer-driver-unfold
    - L2-L1/linear-combination-fold-specialization
    - L2-L1/orthogonalize-composition-lowering
---

# L2 > L1 — Lowering layer

The transformation from L2 (algebraic decompositions) to L1 (mutation-lifted forms). Batched by **themes**.

## Context

L1 forms are pure-functional but **structurally close to the source loop** — explicit input/output sets, in-place mutation patterns either erased (workspace) or preserved (semantically-meaningful aliasing). L2 unfolds these into composition of base primitives. The lowering captures the formal correspondence.

## Theme list

| theme | L2 anchor | L1 anchor | status |
|---|---|---|---|
| [chebyshev-iteration-fusion](./chebyshev-iteration-fusion.md) | `L2/chebyshev-iteration` (firm) | `L1/chebyshev-smoother` (firm) | firm *(algebraic; recurrence↔polynomial fusion)* |
| [deflate-composition-lowering](./deflate-composition-lowering.md) | `L2/deflate` (partly-constructive) | `L1/dot` + `L2/gram` + `L1/lu_solve` + `L2/linear_combination` + `L1/axpy` (firm leaves; `coords`▷`(schur-)solve`▷`back-project` fan-down) | partly-constructive *(reduction-chain; Schur fan-down firm on positive source `nleps.cpp:533-535`; Galerkin-core single-`lu_solve` fan-down constructive on negative anchor + literature; gate = positive bare-Gram-solve site, NOT closed)* |
| [divfree-projector-leaf-identity](./divfree-projector-leaf-identity.md) | `L2/divfree_projector` (firm, fusion-rotation floor) | `L1/divfree_projector` (firm constructed-operator gate) + `L1/apply_linop` + `L1/axpy` (firm; step-4 re-fusion constituents) | firm *(structural; **standalone constructed-operator gate — NO fold-parent, fork-independent**; mostly identity-in-form on the four-step gate `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` with **exactly ONE genuine fusion rotation**: the L2 de-fused step-4 `apply_linop(P.Grad,ψ) ▷ axpy` RE-FUSES into the L1 fused `Grad->AddMult(ψ,y,1.0)` apply-accumulate (value-preserving, `:185` real / `:180-181` complex); inner-solve `sequential-obstruction` carried BY REFERENCE through firm `ksp_solve` — neither introduced nor erased. Slug `-leaf-identity` (NOT `-fold-specialization`): standalone-gate identity-leaf edge, the one fusion lives HERE not on a fold-parent)* |
| [eigsolve-spectral-transform-composition](./eigsolve-spectral-transform-composition.md) | `L2/eigsolve` (firm) | `L1/apply_linop` + `L1/ksp_solve` (firm leaves; `apply_linop`▷`ksp_solve`▷`scale_untransform` per-step de-fusion) | firm *(structural; two-stage pipeline de-fusion read line-for-line off `arpack.cpp:579-581` explicit + `slepc.cpp:1847-1877` ST-shell faces; `scale_untransform` `γ`/`δ` tail + optional projector tail; eigen-iteration LOOP out of scope — opaque-library sequential-obstruction at L3 `partial-obstruction`)* |
| [gram-fold-specialization](./gram-fold-specialization.md) | `L2/gram` (firm) | `L1/dot` (firm; per-cell Hermitian hook) + `L1/bilinear_form` (firm, B-weighted hook) | firm *(algebraic; matrix-lift of `inner-product-fold-specialization` — double-loop materialization of all-pairs law + per-cell conjugation/element-type/weight dispatch + per-cell conjugate-pair re-order + symmetry-exploitation transparent note + `k²` independent per-cell reduction trees; positive Gram-build site `nleps.cpp:524-531`)* |
| [incremental-least-squares-composition-lowering](./incremental-least-squares-composition-lowering.md) | `L2/incremental_least_squares` (firm) | `L1/back_solve` (firm leaf; terminal back-solve) + `concepts/givens_generate`/`givens_apply` (firm; de-fused 4-sub-step Face 2) + `L2/linear_combination` (firm; back-solve reconstruction) + `ls_update_column` (firm column-streaming leaf) | firm *(algebraic; running-QR fan-down `replay▷generate▷apply▷apply_rhs`▷back-solve; FIXED sub-step sequence — replay-before-generate non-commutative load-bearing; two parametric axes `basis_kind∈{V,Z}` + `variant∈{real,complex}`; reduction-path = rotation-ordering + LAPACK scaling, NO MPI collective; terminal back-solve = firm `back_solve` leaf, NOT general `trsv` (separately blocked))* |
| [inner-product-fold-specialization](./inner-product-fold-specialization.md) | `L2/inner_product` (firm) | `L1/dot` (firm; `dot` + `tdot`) + `L1/bilinear_form` (firm, M-weighted member) | firm *(algebraic; conjugation-convention / element-type / weight dispatch + value-level `xᴴ y`↔`yᴴ x` conjugate-pair re-order + pinned reduction tree)* |
| [krylov-step-kernel-defusion](./krylov-step-kernel-defusion.md) | `L2/krylov_step` (firm) | `L1/apply_linop` + `axpy` + `axpby` + `axpbypcz` + `dot` + `nrm2` + `scal` (seven firm leaves; `L2/krylov_step.md:96`) | firm *(structural; per-step fold-kernel de-fusion — five-primitive-group body expanded into the seven-leaf dataflow-forced sequence + in-place→out-of-place buffer rotation (variant-axis-6, `L2/krylov_step.md:121`); demand-pruning Law 1 + `CheckDot` guard carried by reference; per-leaf in-place mechanics deferred to L1>L0 mutation-rotation themes; CG worked-example `iterative.cpp:427-464`)* |
| [ksp-solve-outer-driver-unfold](./ksp-solve-outer-driver-unfold.md) | `L2/ksp_solve` (firm) | `L1/ksp_solve` (firm) | firm *(structural; the DOWNWARD opacity edge of the firm L2 `ksp_solve` driver — the L2 VISIBLE kernel-fold composition `iterate_while (krylov_step op) …` RE-COLLAPSES into the L1 OPAQUE solver-as-operator `(K, b) -> SolveResult`; the inverse of the L2 §"Lowers from" open; solver-method composition-axis re-absorbs into the L1 `krylov-method` opacity-axis; `SolveResult` boundary byte-identical (rotation body-only); slug parallels the UPWARD `L3-L2/ksp-solve-outer-driver`, closing the per-edge asymmetry — both edges of the L2 driver now dedicated themes; the two edges rotate ORTHOGONAL aspects (this = opacity; the L3>L2 edge = iteration-view))* |
| [linear-combination-fold-specialization](./linear-combination-fold-specialization.md) | `L2/linear_combination` (firm) | `L1/scal` + `axpy` + `axpby` + `axpbypcz` (firm) | firm *(algebraic; arity-dispatch fusion-selection + pinned summation order)* |
| [orthogonalize-composition-lowering](./orthogonalize-composition-lowering.md) | `L2/orthogonalize` (firm) | `L1/orthogonalize` (firm leaf) + `L1/dot` + `L1/axpy` (firm; `project`▷`subtract` de-fusion) | firm *(algebraic; MGS/CGS/CGS2 variant-dispatch = `[dot,axpy]` sequence selection; inner product cites `dot-mutation-rotation` Sub-pattern D; collective shape `m×1`/`1×m`/`2×m`)* |

## Vocabulary cohort

**Firm at L2>L1** (lowering structure fully recognized; exhaustively cited; algebraic-laws complete):

- `chebyshev-iteration-fusion` — three-term-recurrence ↔ scaled-polynomial-evaluation fusion (the load-bearing numerical re-association at the kernel boundary).
- `linear-combination-fold-specialization` — arity-dispatch fusion-selection across `scal` / `axpy` / `axpby` / `axpbypcz` + pinned summation order; the term-axis fold cohort.
- `inner-product-fold-specialization` — conjugation / element-type / weight dispatch across `dot` / `tdot` / `bilinear_form` + value-level conjugate-pair re-order + pinned reduction tree; the length-axis fold cohort (sibling of the term-axis fold, do-NOT-merge).
- `orthogonalize-composition-lowering` — `project ▷ subtract` named composition (`dot` ▷ `axpy`); the MGS / CGS / CGS2 variant-dispatch realized as `[dot, axpy]`-sequence selection + collective-shape disclosure.
- `gram-fold-specialization` — matrix-lift of `inner-product-fold-specialization` (the all-pairs double-loop materialization); per-cell conjugation / weight dispatch + `k²` independent per-cell reduction trees + symmetry-exploitation transparent note.
- `eigsolve-spectral-transform-composition` — two-stage shift-invert pipeline de-fusion `apply_linop(M) ▷ ksp_solve((K−σM)⁻¹) ▷ scale_untransform`; per-step body de-fused, eigen-iteration loop is opaque-library sequential-obstruction (out of theme scope).
- `incremental-least-squares-composition-lowering` — running-QR / Givens-stream fan-down `replay ▷ generate ▷ apply ▷ apply_rhs` ▷ back-solve; FIXED sub-step sequence (replay-before-generate non-commutative load-bearing); two parametric axes `basis_kind ∈ {V, Z}` + `variant ∈ {real, complex}`.

*Substantive driver-tier composition→opacity edge (the DOWNWARD edge of the firm L2 `ksp_solve` driver — NOT a leaf-identity, NOT a fold-specialization; the visible kernel-fold composition re-collapses into the L1 opaque operator):*

- `ksp-solve-outer-driver-unfold` — the L2 `ksp_solve` **outer-driver composition** (the convergence-test fold of the VISIBLE [`krylov_step`](../L2/krylov_step.md) kernel) lowers to the L1 **opaque solver-as-operator** `(K, b) -> SolveResult` by RE-COLLAPSING the kernel-fold composition back into the black-box `Solver[A]` (the inverse of the L2 §"Lowers from" *open*). **Substantive (non-identity)**: the kernel and the fold are visible at L2, opaque at L1; the L2 solver-method composition-granularity axis re-absorbs into the L1 `krylov-method` opacity-axis; the `SolveResult` boundary record is byte-identical (rotation body-only). Slug parallels the UPWARD [`L3-L2/ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md), closing the per-edge asymmetry around the firm L2 driver — both its edges now dedicated themes, rotating ORTHOGONAL aspects (this edge = **opacity**, opened at L2 / closed at L1; the L3>L2 edge = **iteration-view**, rendered at L3 / erased at L2). Driver-tier RANK-1 fan-out (consumed by `eigsolve` / `divfree_projector` / `incremental_least_squares`).
- `krylov-step-kernel-defusion` — the per-step fold-kernel de-fusion: the five-primitive-group L2 step body (`apply_linop` ▷ optional-auxiliary ▷ iterate-update ▷ scalar-update ▷ readout) expanded into the seven firm L1 leaves (`apply_linop`/`axpy`/`axpby`/`axpbypcz`/`dot`/`nrm2`/`scal`) in dataflow-forced order, plus the in-place→out-of-place buffer rotation (variant-axis-6) deferred to the per-leaf L1>L0 mutation-rotation themes; demand-pruning Law 1 + `CheckDot` guard carried by reference; the **kernel half** that `ksp_solve`/`chebyshev-iteration`/`eigsolve` fold (the **outer-driver half** is `ksp-solve-outer-driver-unfold`).

*Standalone constructed-operator-gate edge (NO fold-parent, fork-independent):*

- `divfree-projector-leaf-identity` — the L2 `divfree_projector` four-step gate floor lowers to the L1 gate; mostly identity-in-form with **exactly ONE genuine fusion rotation**: the L2 de-fused step-4 `apply_linop(P.Grad,ψ) ▷ axpy` RE-FUSES into the L1 fused `Grad->AddMult(ψ,y,1.0)` apply-accumulate (the one fusion lives HERE, not on a fold-parent); inner-solve `sequential-obstruction` carried BY REFERENCE through firm `ksp_solve`.

The BLAS-1-floor and other degenerate identity-in-named-terms edges (`dot`/`nrm2`/`scal`/`axpy`/`axpby`/`axpbypcz`/`assemble_diagonal`/`jacobi-smoother`/`reciprocal`/`elementwise-product`/`normalize`-`leaf-identity`) are NOT separate theme files: their L2>L1 rotations are captured in-line as §"Downward to L1" notes on their L2 entries, or (for the `dot`/`scal`/`axpy` family) absorbed into the `inner-product-fold-specialization` / `linear-combination-fold-specialization` fold-parents.

**Partly-constructive at L2>L1** (firm Schur-form pipeline + a constructive bare-Galerkin sub-part with a stated promotion condition):

- `deflate-composition-lowering` — `coords ▷ (schur-)solve ▷ back-project` reduction chain over `dot` + `gram` + `lu_solve` + `linear_combination` + `axpy`. The Schur fan-down is firm on positive site `nleps.cpp:533-535`; the Galerkin-core single-`lu_solve` fan-down is constructive on negative anchor + literature; gate = a positive bare-Gram-solve site (not closed).
