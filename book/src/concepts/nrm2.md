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
