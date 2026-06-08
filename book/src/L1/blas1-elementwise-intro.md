---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/axpby
    - L1/axpbypcz
    - L1/axpy
    - L1/bilinear_form
    - L1/dot
    - L1/eigenvalue_untransform
    - L1/elementwise_product
    - L1/matrix_weighted_norm
    - L1/normalize
    - L1/nrm2
    - L1/participation_ratio
    - L1/reciprocal
    - L1/scal
---

# L1 — BLAS-1 & elementwise

The element-local and reduction primitives of L1: pure-functional lifts of Palace's BLAS-1 vector operations and the elementwise (Hadamard / reciprocal) kernels. Two of the index's six semantic motifs live here — **element-wise pure update** (`axpy`, `axpby`, `axpbypcz`, `scal`, `elementwise_product`, `reciprocal`: every output element depends on one input element per tensor argument, reduction-free) and **mutation-free reduction** (`dot`, `nrm2`, plus the matrix-weighted `matrix_weighted_norm` / `bilinear_form`: reduction over the length axis to a scalar, with reduction-tree non-associativity recorded as a load-bearing non-law). `normalize` is the fused norm-then-scale primitive that returns the norm as a first-class result.

Subsumption is captured as algebraic law, not dep-map edge: `axpy ≺ axpby ≺ axpbypcz`, `scal = axpby(β=0)`, and `scal(α,x) = elementwise_product(broadcast(α,N), x)` — the subsumed and subsuming operators stay as siblings in the table.

The two matrix-weighted reductions (`matrix_weighted_norm` `‖x‖_B = √(xᴴBx)`, `bilinear_form` `xᴴMy`) are the `M`-weighted generalisations of `nrm2` / `dot`. Both are `firm` under the firm-on-positive-structure escape.

Chapters are listed alphabetically.
