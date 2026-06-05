---
edges:
  reference: []                    # no book home: L1/trsv does not exist; the back-solve loop
                                   # (iterative.cpp:669-706) is an L0 source citation, not a book node.
                                   # Non-node pointer page; no outbound book edges.
---

# trsv

Base primitive: triangular solve `T · y = b` for a triangular matrix `T` and conforming vectors `b`, `y`. The BLAS-2 routine `?trsv`.

## Contract

- Reads `T` and `b`; writes `y` (or, by in-place convention, overwrites `b` with `y`).
- The triangle (upper/lower) and the diagonal (unit/non-unit) are parameters.
- Sequentially dependent: solving for `y[k]` requires `y[0..k-1]` (for lower triangular). At L3 this is an obstruction — `trsv` does not lift to a tensor-field operation without algorithmic change (e.g., level-set or block-Jacobi triangular preconditioning).
- Numerical: ill-conditioned or near-singular `T` produces large `y`; the caller is responsible for guarding against it.

## Role in higher-layer rotations

In GMRES, `back_solve` is one `trsv` against the upper-triangular block of `H̄_j` (produced by replayed Givens rotations) with RHS `s[0..j]`. The size is `O(max_dim)`, which is small (default 30), so the primitive's serial cost is irrelevant.

## Palace mapping

- Inline back-substitution loop in `palace/linalg/iterative.cpp:669–706`.
- For preconditioners that themselves require triangular solves (ILU, SSOR), see the relevant slice.
