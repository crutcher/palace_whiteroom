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

## Concept: `dot`

Inner product of two vectors: `⟨x, y⟩` (returns a scalar).

## Background

BLAS-1 `ddot` / `zdotc`. The complex case is subtle: the canonical BLAS
Hermitian inner product `⟨x, y⟩ = x^H y` returns a complex scalar.
Palace's `Vector::Dot` and `ComplexVector::Dot` both return a **real**
scalar — for the real case the natural definition, for the complex
case the real-projected form `Re⟨x, y⟩` (suitable when the recurrence
requires only the SPD form, as in CG).

This projection is a deliberate API choice, not a primitive deficiency:
Krylov recurrences for SPD or self-adjoint problems use only the real
form; recurrences that require the full complex inner product (e.g.,
GMRES residual-norm computations on complex iterates) compose multiple
dot calls. See
[palace/linalg/vector.cpp:142-178](../../../reference/palace/linalg/vector.cpp#L142-L178)
for the projection definition.

## Signature (canonical)

```
dot(x, y) → ℝ                    // real-projected for complex case
```

## Variant axes

- **Scalar field**: absorbed at the contract level (return type is
  always real). The complex case projects via `std::real`.
- **Conjugation convention**: Palace fixes `Re x^H y` for complex; other
  libraries may expose both `cdotc` and `cdotu`. Out of scope here.

## Slices that use this primitive

- [cg](../spec/slices/cg.md) — `⟨r, z⟩` (β numerator) and `⟨p, A p⟩` (α
  denominator).
- [gmres](../spec/slices/gmres.md) — orthogonalization coefficients
  `⟨v_i, w⟩` (CGS/MGS), at the L2 unfolding of `orthogonalize`.
