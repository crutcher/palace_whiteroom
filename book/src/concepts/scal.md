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

## Concept: `scal`

Vector scaling: `x ← α x`.

## Background

BLAS-1 `dscal` / `zscal`. In-place; Palace's `Vector::operator*=(α)` is
the member-method form. Used for normalizing Krylov basis vectors
(`v ← v / ‖v‖`) and rescaling search directions (`p *= β/β_prev` in CG).

## Signature (canonical)

```
scal(α, x)           // x ← α x; x mutated
```

## Slices that use this primitive

- [cg](../spec/slices/cg.md) — `p ← (β/β_prev) p` before adding `z`
  (fused at L0 with the subsequent `p += z`).
- [gmres](../spec/slices/gmres.md) — basis normalization `v_{j+1} ←
  v_next / H[j+1, j]`.
