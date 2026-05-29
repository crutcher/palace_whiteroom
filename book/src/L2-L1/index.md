# L2 > L1 — Lowering layer

The transformation from L2 (algebraic decompositions) to L1 (mutation-lifted forms). Batched by **themes**.

## Context

L1 forms are pure-functional but **structurally close to the source loop** — explicit input/output sets, in-place mutation patterns either erased (workspace) or preserved (semantically-meaningful aliasing). L2 unfolds these into composition of base primitives. The lowering captures the formal correspondence.

## Theme list

| theme | L2 anchor | L1 anchor | status |
|---|---|---|---|
| [chebyshev-iteration-fusion](./chebyshev-iteration-fusion.md) | `L2/chebyshev-iteration` (firm) | `L1/chebyshev-smoother` (firm) | firm *(algebraic; recurrence↔polynomial fusion)* |
| [linear-combination-fold-specialization](./linear-combination-fold-specialization.md) | `L2/linear_combination` (firm) | `L1/scal` + `axpy` + `axpby` + `axpbypcz` (firm) | firm *(algebraic; arity-dispatch fusion-selection + pinned summation order)* |
| [inner-product-fold-specialization](./inner-product-fold-specialization.md) | `L2/inner_product` (firm) | `L1/dot` (firm; `dot` + `tdot`) + `L1/bilinear-form` (rough-in, M-weighted member) | firm *(algebraic; conjugation-convention / element-type / weight dispatch + value-level `xᴴ y`↔`yᴴ x` conjugate-pair re-order + pinned reduction tree)* |
| [orthogonalize-composition-lowering](./orthogonalize-composition-lowering.md) | `L2/orthogonalize` (firm, cycle-019) | `L1/orthogonalize` (firm leaf) + `L1/dot` + `L1/axpy` (firm; `project`▷`subtract` de-fusion) | firm *(algebraic; MGS/CGS/CGS2 variant-dispatch = `[dot,axpy]` sequence selection; inner product cites `dot-mutation-rotation` Sub-pattern D; collective shape `m×1`/`1×m`/`2×m`)* |
| [gram-fold-specialization](./gram-fold-specialization.md) | `L2/gram` (firm, cycle-022) | `L1/dot` (firm; per-cell Hermitian hook) + `L1/bilinear-form` (rough-in, B-weighted hook) | firm *(algebraic; matrix-lift of `inner-product-fold-specialization` — double-loop materialization of all-pairs law + per-cell conjugation/element-type/weight dispatch + per-cell conjugate-pair re-order + symmetry-exploitation transparent note + `k²` independent per-cell reduction trees; positive Gram-build site `nleps.cpp:524-531`)* |
| [deflate-composition-lowering](./deflate-composition-lowering.md) | `L2/deflate` (partly-constructive) | `L1/dot` + `L2/gram` + `L1/lu_solve` + `L2/linear_combination` + `L1/axpy` (firm leaves; `coords`▷`(schur-)solve`▷`back-project` fan-down) | partly-constructive *(reduction-chain; Schur fan-down firm on positive source `nleps.cpp:533-535`; Galerkin-core single-`lu_solve` fan-down constructive on negative anchor + literature; gate = positive bare-Gram-solve site, NOT closed)* |
| [eigsolve-spectral-transform-composition](./eigsolve-spectral-transform-composition.md) | `L2/eigsolve` (firm, cycle-023) | `L1/apply_linop` + `L1/ksp_solve` (firm leaves; `apply_linop`▷`ksp_solve`▷`scale_untransform` per-step de-fusion) | firm *(structural; two-stage pipeline de-fusion read line-for-line off `arpack.cpp:579-581` explicit + `slepc.cpp:1847-1877` ST-shell faces; `scale_untransform` `γ`/`δ` tail + optional projector tail; eigen-iteration LOOP out of scope — opaque-library sequential-obstruction at L3 `partial-obstruction`)* |

## Working Notes

- Themes here are heavy with optimization-trick unfolding (transparent performance tricks like fusion, tiling, packing; load-bearing numerical tricks preserved).
