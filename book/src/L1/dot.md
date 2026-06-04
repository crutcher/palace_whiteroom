---
layer: L1
operator: dot
rank: firm
edges:
  reference:
    - L1-L0/dot-mutation-rotation
    - concepts/dot
---

# dot

Mutation-free vector inner-product reduction: `α = ⟨x, y⟩`. The canonical BLAS-1 reduction primitive at L1; the workhorse of Krylov coefficient computation and orthogonalisation.

## Context

`dot` lifts Palace's reduction surface (`mfem::Vector::operator*` for real; `ComplexVector::Dot` / `TransposeDot` for complex; the `linalg::LocalDot` / `linalg::Dot` free-function templates over both) to a single pure-functional sesquilinear-reduction operator (with the unconjugated bilinear variant `tdot`). The L0 file layout — the reduction family in `vector.{hpp,cpp}`, including the receiver-vs-argument asymmetry on `ComplexVector::Dot` that determines which side is conjugated — is detailed in [`L0/linalg-vector-file`](../L0/linalg-vector-file.md) "The reduction family". The `linalg::Dot` template-dispatch scaffold (composing `LocalDot` with `Mpi::GlobalSum`) is named in [`L0/linalg-free-functions`](../L0/linalg-free-functions.md) "Composed scaffold". The real / complex element-type split and the `LocalDot` vs `Dot` (single-rank vs MPI-collective) axis are named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md). The self-aliasing fast path (`&y == this`) and reduction-tree non-associativity classification (transparent vs load-bearing) live in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination for `dot` is the return register / a stack scalar. There is no destination buffer to write through. The distinction the mutation rotation is doing here is therefore not about buffer ownership but about **reduction order and collective topology**: the L0 form bakes in a specific tree (the Hypre reduction kernel + MPI_Allreduce); the L1 form treats the reduction as a single semantic step.

A cross-cutting prose treatment lives at [`concepts/dot`](../concepts/dot.md). The L1 entry here is the firm operator definition; the concept page is the narrative pointer plus BLAS-1 heritage framing. The L1 entry is authoritative on every factual claim about the Palace surface.

## Signature

```
dot   :: (x: Tensor[N], y: Tensor[N]) -> Scalar
tdot  :: (x: Tensor[N], y: Tensor[N]) -> Scalar     -- complex-only variant
```

Two operators in one chapter because they share the entire reduction skeleton (sum over `N`) and differ only by the per-element kernel.

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[N]` — read-only.
- `y` — `Tensor[N]` — read-only.
- result — `Scalar` — element type follows the rule below.
- `x` and `y` must share the length axis `N` and element type.

Element-type rule:

| element type | `dot(x, y)` returns | per-element kernel |
|---|---|---|
| `real`    | `real`    | `x[i] * y[i]` |
| `complex` | `complex` | `conj(x[i]) * y[i]` *(Hermitian, conjugate-linear in first arg)* |
| `complex` (via `tdot`) | `complex` | `x[i] * y[i]` *(unconjugated bilinear)* |

The "real-projected" reading from `concepts/dot.md` (`Re⟨x,y⟩`) is **not** what Palace's `ComplexVector::Dot` returns. The real-projection only enters at the call site when callers take `std::abs(linalg::Dot(...))` (e.g. `palace/linalg/nleps.cpp:487` for a norm) or `std::real(...)` (in algorithms that know the form must be real, like CG's `β = ⟨r, z⟩` for SPD `B`). Those projections are caller-side L1 forms (`abs` and `re`), not part of `dot` itself.

## Semantics

Reduction: `dot(x, y) = Σ_{i ∈ [0, N)} kernel(x[i], y[i])` with the per-element kernel from the table above.

Conjugation convention (complex `dot`): conjugate-linear in the **first** argument, linear in the second. This matches the standard mathematical Hermitian inner product `⟨x, y⟩ = xᴴ y`. *Note* on the C++ surface: `ComplexVector::Dot` is a method on `*this`, so the receiver is the linear argument and the call argument is the conjugated one (`(*this).Dot(y) = yᴴ · (*this)`). At L1 this asymmetry between method-form (`receiver.Dot(arg)`) and free-function-form (`linalg::Dot(comm, x, y)`) is erased — the L1 signature names the conjugated argument first.

Reduction-tree non-associativity is **load-bearing** in the CLAUDE.md sense: floating-point summation is non-associative, so different reduction trees produce different bit-level results. Palace's L0 implementation pins a specific tree (Hypre per-rank kernel + MPI tree-reduce); a different tree gives a different scalar at the bit level even though all are valid implementations of the L1 operator. This is recorded here, not erased.

The MPI collective is **not** in the L1 signature. Single-rank is in scope (`CLAUDE.md` "Scope"); MPI ranks are read as their single-rank equivalents. The reduction at L1 is a single step; the L1>L0 lowering theme is where the local-then-collective two-step reappears (and where bit-deterministic-reduction-order trade-offs are recorded).

The self-dot optimisation `&x == &y` (e.g. `palace/linalg/vector.cpp:266` returning imaginary part `0.0` directly for the Hermitian form; `palace/linalg/vector.cpp:272-273` returning `2 * Imag·Real` for `TransposeDot`) is a transparent performance trick at L1 — algebraically `xᴴ x` always has zero imaginary part exactly, so eliding the cancellation is equivalent. It disappears in the L1>L0 lowering.

## Algebraic laws

The laws below hold; absences are deliberate.

**For `dot` over real element-type (bilinear symmetric form):**

1. **Symmetry**: `dot(x, y) = dot(y, x)`.
2. **Bilinearity (left)**: `dot(α·x₁ + x₂, y) = α·dot(x₁, y) + dot(x₂, y)`.
3. **Bilinearity (right)**: `dot(x, α·y₁ + y₂) = α·dot(x, y₁) + dot(x, y₂)`. (Follows from 1 + 2.)
4. **Positive semi-definite at `y = x`**: `dot(x, x) ≥ 0`, with equality iff `x = 0` (in exact arithmetic).
5. **Zero in either argument**: `dot(0, y) = dot(x, 0) = 0`.

**For `dot` over complex element-type (Hermitian sesquilinear form, conjugate-linear in first arg):**

6. **Hermitian symmetry**: `dot(x, y) = conj(dot(y, x))`.
7. **Conjugate-linearity (left)**: `dot(α·x₁ + x₂, y) = conj(α)·dot(x₁, y) + dot(x₂, y)`.
8. **Linearity (right)**: `dot(x, α·y₁ + y₂) = α·dot(x, y₁) + dot(x, y₂)`.
9. **Positive semi-definite at `y = x`**: `dot(x, x) ∈ ℝ` and `dot(x, x) ≥ 0`, with equality iff `x = 0` (in exact arithmetic). Confirmed by the implementation returning imaginary part `0.0` exactly when `&x == &y` (`palace/linalg/vector.cpp:266`, `palace/linalg/vector.cpp:678`).
10. **Zero in either argument**: `dot(0, y) = dot(x, 0) = 0`.

**For `tdot` over complex element-type (unconjugated bilinear form):**

11. **Symmetry**: `tdot(x, y) = tdot(y, x)`.
12. **Bilinearity in each argument** (analogue of laws 2–3 with no conjugation).
13. **Not positive semi-definite**: `tdot(x, x) ∈ ℂ` in general; in particular `tdot(x, x) = 0` does **not** imply `x = 0` (e.g. `x = (1, i)` gives `tdot(x, x) = 1·1 + i·i = 0`). Recorded as the explicit absence: `tdot` is the indefinite form Palace exposes for algorithms that require it, distinct from `dot`.

Laws that explicitly **do not** hold across both `dot` and `tdot`:

- **Associativity of the reduction-tree** in floating point: different summation orders give different bit-level results. Load-bearing (see Semantics). The mathematical law `(a + b) + c = a + (b + c)` holds in ℝ / ℂ but not in IEEE-754.
- **Sub-additivity / Cauchy–Schwarz strictness in floating point**: `|dot(x, y)|² ≤ dot(x, x) · dot(y, y)` holds mathematically but can fail by ULP-level amounts due to summation ordering; algorithms that depend on it tightly (e.g. some MGS reorthogonalisation heuristics) must guard.
- **Distributivity over vector-multiplication structure**: not applicable — `dot` is not a binary operator on vectors closing back to vectors; it's a reduction to a scalar.

## Dependencies

None at L1. `dot` is a leaf primitive — alongside `axpy`, it is one of the two BLAS-1 floor primitives. Its sub-operations are scalar multiplication, scalar conjugation (complex case only), and scalar addition, all at or below the L1 layer's resolution.

`nrm2` (forthcoming; cycle-003) will depend on `dot` via `nrm2(x) = √dot(x, x)` for real, and `nrm2(x) = √re(dot(x, x))` (equivalent to `√dot(x, x)` since law 9 guarantees the result is real) for complex.

## Variant axes

`dot` has two orthogonal variant axes at L1:

- **element-type**: `real` | `complex`. At L0 these are separate functions / overloads (real via `mfem::Vector::operator*` and `linalg::LocalDot(Vector, Vector)` at `vector.cpp:665-672`; complex via `ComplexVector::Dot` at `vector.cpp:263-267` and `linalg::LocalDot(ComplexVector, ComplexVector)` at `vector.cpp:674-685`). At L1 these collapse to one operator parameterised by element type, with the Hermitian-vs-bilinear distinction handled by the per-element kernel.
- **conjugation convention** (complex element-type only): `hermitian` (the default `dot`) | `unconjugated` (the separate operator `tdot`). At L0: `ComplexVector::Dot` vs `ComplexVector::TransposeDot`. At L1 these are distinct operators (sharing only the reduction skeleton), because the algebraic laws differ — `dot` is positive semi-definite at `y = x`, `tdot` is not.

No other variant axes — the reduction is unconditionally exhaustive over the length axis `N`, with no masking or strided variants in the Palace surface.

## Status

`firm` — signatures are canonical, evidence is direct from the Palace source, and the algebraic laws listed are standard sesquilinear/bilinear facts modulo the explicitly-recorded floating-point caveats.

## L1 vs L0 distinction

- **L0**: free-function `linalg::Dot(MPI_Comm, x, y)` (does a local kernel + MPI_Allreduce), method-form `(*this).Dot(arg)` (no MPI), or `mfem::Vector::operator*` (real, no MPI). The receiver-vs-argument asymmetry on the method form determines which side is conjugated. Reduction tree is pinned (Hypre + MPI). Self-dot is a branched fast path.
- **L1**: pure functional reduction `α = dot(x, y)`. No MPI collective in the signature (folded into the L1>L0 lowering). No receiver-vs-argument asymmetry (first argument is by convention the conjugated one). Reduction-tree non-associativity recorded as a load-bearing algebraic claim, not a separate operator.

## Evidence

- `palace/linalg/vector.hpp:110-113` — `ComplexVector::Dot` declaration with comment `Vector dot product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.` and `TransposeDot` alongside; `operator*` aliased to `Dot`.
- `palace/linalg/vector.hpp:242-244` — `linalg::LocalDot` declarations for both real and complex inputs.
- `palace/linalg/vector.hpp:247-253` — `linalg::Dot` template, `LocalDot` + `Mpi::GlobalSum`.
- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body: real part `(Real()·y.Real()) + (Imag()·y.Imag())`, imag part `(Imag()·y.Real()) - (Real()·y.Imag())` (with `&y == this` fast path returning imag = 0 directly).
- `palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body: real part `(Real()·y.Real()) - (Imag()·y.Imag())`, imag part `(Imag()·y.Real()) + (Real()·y.Imag())` (with `&y == this` fast path returning `2·(Imag()·y.Real())`).
- `palace/linalg/vector.cpp:665-672` — `linalg::LocalDot(Vector, Vector)` via Hypre's `hypre_SeqVectorInnerProd`.
- `palace/linalg/vector.cpp:674-685` — `linalg::LocalDot(ComplexVector, ComplexVector)`: combines four real `LocalDot` calls, with self-dot fast path returning imag = 0.
- `palace/linalg/iterative.cpp:395, 404, 444, 460` — CG using `linalg::Dot` for `β = ⟨z, r⟩` and the α-denominator `⟨z, p⟩`.
- `palace/linalg/nleps.cpp:487, 492, 522, 529, 543, 568, 575, 675` — nonlinear-EVP code using `std::abs(linalg::Dot(...))` and `std::sqrt(std::abs(...))`, confirming the complex case returns complex.
- `test/unit/test-vector.cpp:206-207` — real-vector dot via `operator*`: `double dot = vec1 * vec2; CHECK_THAT(dot, WithinRel(32.0));`. Direct evidence the real form returns `double`.
- `test/unit/test-orthog.cpp:157, 219-220, 271, 313-315, 373-376` — `linalg::Dot` used as the orthogonalisation-coefficient primitive in MGS and CGS.
