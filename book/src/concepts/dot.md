# dot

Base primitive: `α ← ⟨x, y⟩` — inner product of two conforming vectors. For real spaces, `α = Σ x[i] · y[i]`; for complex, `α = Σ x̄[i] · y[i]` (conjugate-linear in the first argument by Palace convention; check the slice's L0 citations for the exact convention in use).

## Contract

- Reads both operands; writes none.
- **Reduction.** In a distributed setting, `dot` carries a load-bearing MPI collective (typically `MPI_Allreduce` on a partial sum). The collective is implicit at L2 — slices that care about its cost or scheduling state that explicitly.
- **Associativity.** Floating-point summation order is non-associative; different reduction trees give different bit-level results. When this matters (deterministic builds, bit-reproducibility) the slice flags it as a load-bearing numerical claim.

## Role in higher-layer rotations

`dot` is the workhorse of orthogonalisation and convergence tests. MGS uses one `dot` per basis vector; CGS uses `j+1` `dot`s as a batch (one collective); CGS2 doubles that. `nrm2(x) = √dot(x, x)`.

## Palace mapping

- `linalg::Dot` and `linalg::Dotc` in `palace/linalg/vector.{hpp,cpp}`.
- The complex-conjugate version is `Dotc`; the un-conjugated bilinear version is `Dot`.
