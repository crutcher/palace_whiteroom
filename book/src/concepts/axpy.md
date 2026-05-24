# axpy

Base primitive: `y ← α·x + y` for a scalar `α` and conforming vectors `x`, `y`. The BLAS-1 staple. In-place on `y`.

## Contract

- Reads `x` and the prior `y`; writes `y`.
- Reduction-free (element-local); embarrassingly parallel.
- Special-case fusions (`α = 1`, `α = -1`, `y = 0` ⇒ `scal`+copy) are transparent optimizations; the canonical primitive is the general form.

## Role in higher-layer rotations

`axpy` is the dominant primitive in Krylov subspace updates: the solution update `x ← x + Σ y[k] · V[k]` is a sequence of `axpy` calls (or a single batched `gemv`-via-`axpy` chain). The orthogonalisation step in MGS is a `dot` followed by an `axpy`. At L2, named L1 operations like `apply_correction` unfold into `axpy` chains.

## Palace mapping

- `linalg::AXPY` in `palace/linalg/vector.{hpp,cpp}` and its complex analogue.
- MFEM `Vector::Add`.
