---
edges:
  reference:
    - L1/elementwise_product       # authoritative operator entry (definition)
---

# elementwise_product

Base primitive: `y ← x ⊙ z` where `⊙` denotes elementwise (Hadamard) product of two vectors of the same length. The result is the vector `[x_0·z_0, x_1·z_1, …, x_{n-1}·z_{n-1}]`.

## Background

Standard Hadamard / pointwise product. In BLAS-terms this is not a level-1 op (no scaling, no accumulation); in tensor-library terms it's `mul` or `*` on equally-shaped tensors. The operation is local (no cross-element coupling), embarrassingly parallel, and has the algebraic identities of pointwise multiplication: commutative, associative, distributive over addition, identity = `[1, 1, …]`.

## Contract

- Pure with respect to its operands (in-place output into one of the operands is acceptable as a workspace convention).
- Shape: `x, z : V → ℝ` (or ℂ); `y ∈ V` with the same shape.
- Both operand vectors and the output vector share the same shape.

## Role in higher-layer rotations

`elementwise_product` is the diagonal-operator apply primitive at L2: applying a diagonal operator `D` to a vector `x` is `elementwise_product(diag(D), x)`. The Chebyshev smoother uses this for `dinv ⊙ r` where `dinv = 1/diag(A)` is the precomputed reciprocal diagonal preconditioner — the cheapest possible preconditioning step.

At L3 this lifts trivially to a global tensor-field elementwise op; the per-element loop disappears, the algebraic identity is preserved.

## Palace mapping

- `mfem::Vector` has component-wise operators that realize this.
- Palace's Jacobi/Chebyshev smoothers use the precomputed-diagonal reciprocal pattern; the `dinv ⊙ r` step is the elementwise-product realization.
