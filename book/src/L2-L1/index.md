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

## Working Notes

- Themes here are heavy with optimization-trick unfolding (transparent performance tricks like fusion, tiling, packing; load-bearing numerical tricks preserved).
