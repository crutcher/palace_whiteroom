---
edges:
  reference:
    - L1/dot                       # authoritative operator entry (definition); pointer-to, not blocking
    - L2/krylov_step               # use-site cross-link (CG/GMRES inner-product role)
---

# dot

Cross-cutting concept page for the inner-product reduction primitive. The
authoritative operator definition (signatures, algebraic laws, variant
axes, evidence) lives at [`L1/dot`](../L1/dot.md); this page is the
narrative pointer plus the BLAS-heritage framing.

## One-line semantics

`α = dot(x, y) = Σ_i kernel(x[i], y[i])` — a pure reduction of two
conforming vectors to a scalar. The per-element kernel depends on the
element type and on the conjugation convention; see the [L1
entry](../L1/dot.md) for the full element-type → return-type table.

## Background: BLAS-1 heritage

Palace's dot family inherits its shape from BLAS-1 `ddot` / `zdotc` /
`zdotu`. The real case is the textbook bilinear form `Σ x[i] · y[i]`;
the complex case has two distinct flavours, which Palace exposes as
separate methods:

- **`ComplexVector::Dot`** (`palace/linalg/vector.hpp:111`) — the
  Hermitian sesquilinear inner product `yᴴ x`, conjugate-linear in the
  argument `y` and linear in the receiver `*this`. Returns
  `std::complex<double>`. Body at `palace/linalg/vector.cpp:263-267`.
  Analogous to BLAS-1 `zdotc`.
- **`ComplexVector::TransposeDot`** (`palace/linalg/vector.hpp:112`) —
  the unconjugated bilinear form `yᵀ x`. Returns
  `std::complex<double>`. Body at `palace/linalg/vector.cpp:269-274`.
  Analogous to BLAS-1 `zdotu`. Method-form only; there is no free
  function `linalg::TransposeDot`.

The header comment at `palace/linalg/vector.hpp:110` summarises both:
"Vector dot product (yᴴ x) or indefinite dot product (yᵀ x) for complex
vectors."

The real case is `mfem::Vector::operator*(const Vector &) → double` and
the parallel free function `linalg::Dot(MPI_Comm, x, y)` template
(`palace/linalg/vector.hpp:247-253`) which dispatches `LocalDot` plus
`Mpi::GlobalSum` (a Palace wrapper over `MPI_Allreduce`). The real `LocalDot` is at
`palace/linalg/vector.cpp:665-672`; the complex `LocalDot` is at
`palace/linalg/vector.cpp:674-685`.

## Return type — the L1 element-type rule

| element type | `dot(x, y)` returns | per-element kernel | Palace mapping |
|---|---|---|---|
| `real`    | `real`    | `x[i] * y[i]`       | `mfem::Vector::operator*`, `linalg::Dot<Vector>` |
| `complex` | `complex` | `conj(x[i]) * y[i]` *(Hermitian)* | `ComplexVector::Dot`, `linalg::Dot<ComplexVector>` |
| `complex` (`tdot`) | `complex` | `x[i] * y[i]` *(unconjugated)* | `ComplexVector::TransposeDot` (method only) |

The complex case returns a complex scalar, not a real one. The
"real-projection" view (e.g. `std::real(dot(x, x))`, `std::abs(dot(x, y))`)
arises only at call sites that know algebraically the result must be
real (CG's `β = ⟨r, z⟩` for SPD problems) or that want a norm
(`palace/linalg/nleps.cpp:487` uses `std::abs(linalg::Dot(...))`). That
projection is caller-side, not built into `dot`.

## Caveats and load-bearing facts

- **MPI reduction.** The free function `linalg::Dot` carries an
  `MPI_Allreduce` over the partial sums. Out of scope for single-rank
  builds per CLAUDE.md "Scope"; recorded in the L1>L0 lowering.
- **Reduction non-associativity.** Floating-point summation order is
  non-associative; different reduction trees give different bit-level
  results. Load-bearing for deterministic builds; see the L1 entry's
  "Semantics" section for the algebraic claim.
- **Self-dot fast path.** When `&x == &y`, the imaginary part is zero
  exactly (Hermitian case) and the code elides the cancellation
  (`vector.cpp:266`, `vector.cpp:678`). Transparent performance trick.

## Slices that use this primitive

- [`krylov_step` (CG instance)](../L2/krylov_step.md) — `⟨r, z⟩` (β numerator) and `⟨p, A p⟩` (α
  denominator).
- [`krylov_step` (GMRES instance)](../L2/krylov_step.md) — orthogonalization coefficients
  `⟨v_i, w⟩` (CGS/MGS), at the L2 unfolding of `orthogonalize`.

## See also

- [`L1/dot`](../L1/dot.md) — authoritative operator entry: full
  signatures, algebraic laws, variant axes, complete L0 evidence list.
  **If this page and the L1 entry disagree on any factual claim about
  the Palace surface, the L1 entry wins.**
