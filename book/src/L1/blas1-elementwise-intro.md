# L1 — BLAS-1 & elementwise

The element-local and reduction primitives of L1: pure-functional lifts of Palace's BLAS-1 vector operations and the elementwise (Hadamard / reciprocal) kernels. Two of the index's six semantic motifs live here — **element-wise pure update** (`axpy`, `axpby`, `axpbypcz`, `scal`, `elementwise_product`, `reciprocal`: every output element depends on one input element per tensor argument, reduction-free) and **mutation-free reduction** (`dot`, `nrm2`, plus the matrix-weighted `matrix-weighted-norm` / `bilinear-form`: reduction over the length axis to a scalar, with reduction-tree non-associativity recorded as a load-bearing non-law). `normalize` is the fused norm-then-scale primitive that returns the norm as a first-class result.

Subsumption is captured as algebraic law, not dep-map edge: `axpy ≺ axpby ≺ axpbypcz`, `scal = axpby(β=0)`, and `scal(α,x) = elementwise_product(broadcast(α,N), x)` — the subsumed and subsuming operators stay as siblings in the table.

The two matrix-weighted reductions (`matrix-weighted-norm` `‖x‖_B = √(xᴴBx)`, `bilinear-form` `xᴴMy`) are the `M`-weighted generalisations of `nrm2` / `dot`; both are `rough-in (test-coverage-bounded)` pending dedicated coverage of the `linalg::` weighted overloads.

Chapters are listed alphabetically.
