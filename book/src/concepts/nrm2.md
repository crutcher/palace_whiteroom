# nrm2

Base primitive: `α ← ‖x‖₂ = √⟨x, x⟩`. The Euclidean norm of a vector.

## Contract

- Reads `x`; writes none.
- Carries the same MPI-collective cost as one `dot`.
- Stability: production implementations use scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow when `|x[i]|` spans a wide range. A naïve `√Σ x[i]²` is not equivalent.

## Role in higher-layer rotations

Used for basis-vector normalisation (`V[j+1] ← w / ‖w‖₂`), for the initial-residual norm `β = ‖r₀‖₂` in GMRES, and as the convergence-test scale in many iterative solvers.

## Palace mapping

- `linalg::Norml2` in `palace/linalg/vector.{hpp,cpp}`.

## Concept: `nrm2`

Euclidean norm of a vector: `‖x‖₂ = √⟨x, x⟩`.

## Background

BLAS-1 `dnrm2` / `dznrm2`. In Palace, `Vector::Norml2` returns a real
scalar (the complex case computes `√Σ |x_k|²`). Used pervasively for
convergence tests against absolute/relative tolerances on `‖b‖`.

## Signature (canonical)

```
nrm2(x) → ℝ
```

## Slices that use this primitive

- [cg](../spec/slices/cg.md) — residual norm `‖r‖` per iteration.
- [gmres](../spec/slices/gmres.md) — initial residual norm `β`, Arnoldi
  sub-diagonal `H[j+1, j] = ‖w‖`, and the incremental `|s[j+1]|`
  residual norm.
