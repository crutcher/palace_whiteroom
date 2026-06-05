---
edges:
  reference:
    - L1/nrm2                      # authoritative operator entry (definition)
    - L2/krylov-step               # use-site cross-link (residual norm / Arnoldi sub-diagonal)
---

# nrm2

Base primitive: `α ← ‖x‖₂ = √⟨x, x⟩`. The Euclidean norm of a vector.

## Contract

- Reads `x`; writes none.
- Carries the same MPI-collective cost as one `dot`.
- Stability: Palace's `linalg::Norml2` computes the naïve `√⟨x, x⟩` via `Dot` (one-line body `std::sqrt(std::abs(Dot(comm, x, x)))`); it does **not** use scaled summation. There is no Palace-level overflow/underflow guarantee — Palace inherits whatever the underlying `dot` reduction provides. BLAS-style scaled-summation `nrm2` (which would avoid overflow/underflow when `|x[i]|` spans a wide range, at the cost of extra arithmetic) is **not present** in Palace. If a caller needs scaling, that is a caller-side concern, not a variant of this operator. See [`L1/nrm2`](../L1/nrm2.md) (authoritative — §Variant axes "Stability variants" and the §Context correction note).

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

- [`krylov-step` (CG instance)](../L2/krylov-step.md) — residual norm `‖r‖` per iteration.
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — initial residual norm `β`, Arnoldi
  sub-diagonal `H[j+1, j] = ‖w‖`, and the incremental `|s[j+1]|`
  residual norm.
