---
edges:
  reference:
    - L1/elementwise_product       # authoritative operator entry (definition)
---

# elementwise_product

Base primitive: `y ← x ⊙ z` where `⊙` denotes elementwise (Hadamard) product of two congruent tensors (the same shape group `S`, arbitrary unknown rank — NOT rank-1). The result is the tensor whose value at every multi-index `idx` of `S` is `x[idx]·z[idx]`.

## Background

Standard Hadamard / pointwise product. In BLAS-terms this is not a level-1 op (no scaling, no accumulation); in tensor-library terms it's `mul` or `*` on congruent (equally-shaped) tensors. The operation is local (no cross-element coupling), embarrassingly parallel, and has the algebraic identities of pointwise multiplication: commutative, associative, distributive over addition, identity = the all-ones tensor of shape group `S`.

## Contract

- Pure with respect to its operands (in-place output into one of the operands is acceptable as a workspace convention).
- Shape (named shape groups per [`l4_calculus`](../design/l4_calculus.md) §1.2.1): operands and result share one shape group `S` (arbitrary, unknown rank — NOT rank-1); `x, z : Tensor[(S: ...)] → ℝ` (or ℂ); `y : Tensor[S]`.
- Both operand tensors and the output tensor are congruent (the same shape group `S`).

## Role in higher-layer rotations

`elementwise_product` is the diagonal-operator apply primitive at L2: applying a diagonal operator `D` to a vector `x` is `elementwise_product(diag(D), x)`. The Chebyshev smoother uses this for `dinv ⊙ r` where `dinv = 1/diag(A)` is the precomputed reciprocal diagonal preconditioner — the cheapest possible preconditioning step.

At L3 this lifts trivially to a global tensor-field elementwise op; the per-element loop disappears, the algebraic identity is preserved.

## Palace mapping

- `mfem::Vector` has component-wise operators that realize this.
- Palace's Jacobi/Chebyshev smoothers use the precomputed-diagonal reciprocal pattern; the `dinv ⊙ r` step is the elementwise-product realization.
