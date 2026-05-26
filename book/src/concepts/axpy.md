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

## Concept: `axpy`

Vector-scalar fused update: `y ← α x + y`.

## Background

BLAS-1 `daxpy` / `zaxpy`. The accumulator (`y`) is mutated in place;
the source (`x`) is read-only. Palace's `Vector::Add(α, x)` is the
member-method form of `axpy(α, x, self)`.

## Signature (canonical)

```
axpy(α, x, y)        // y ← α x + y; y mutated
```

## Slices that use this primitive

- [cg](../spec/slices/cg.md) — `x ← x + α p` (`x.Add(α, p)`), `r ← r − α A p`
  (`r.Add(-α, Ap)`).
- [gmres](../spec/slices/gmres.md) — basis-correction sum `x ← x + Σ y_k
  v_k` unfolds at L2 to a sequence of `axpy` calls (or one `gemv`-shaped
  primitive; canonical pinning deferred to L2).
