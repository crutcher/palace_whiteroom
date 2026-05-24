# scal

Base primitive: `x ← α · x` — scalar multiplication of a vector in place.

## Contract

- Reads and writes `x`.
- Element-local; no reduction; embarrassingly parallel.
- The `α = 0` case (zero-fill) is a transparent specialisation.

## Role in higher-layer rotations

`scal` appears in basis-vector normalisation (`scal(1/β, V[0])`), in re-normalisation after orthogonalisation, and as the zero-fill primitive when an iterate is reset (e.g., GMRES with `initial_guess = false`).

## Palace mapping

- `linalg::Scale` / `mfem::Vector::operator*=`.
