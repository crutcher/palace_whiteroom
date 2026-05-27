# scal

Mutation-lifted vector-scalar multiplication: `x_new = α · x_old`. The BLAS-1 `dscal` / `zscal` primitive at L1, and the last of the four core BLAS-1 floor primitives (`axpy`, `dot`, `nrm2`, `scal`).

## Context

`scal` lifts Palace's vector-scalar multiplication from the receiver-mutating member form alone — `mfem::Vector::operator*=(double)` on real vectors, `ComplexVector::operator*=(std::complex<double>)` on complex vectors — to a single pure-functional operator. There is no free-function form: the notable absence of any `linalg::Scal` / `linalg::Scale` symbol (and the closest neighbour, `linalg::Normalize`, which is a fused `nrm2 + scal(1/nrm2, ·)` rather than a `scal` wrapper) is named in [`L0/linalg-free-functions`](../L0/linalg-free-functions.md). The receiver-mutating idiom (no output-arg form for `scal`) is named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md). The element-type axis (real / complex / scalar-promoted) and the complex-shape branch (`s.imag() == 0.0`) in `ComplexVector::operator*=` are named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md) and classified as transparent in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination buffer is the receiver `*this`. The L1 form drops the destination-buffer mention: the operator consumes `α` and the pre-update value of `x`, and produces a fresh post-update value. The L0 real-imag-branch fast path in `ComplexVector::operator*=` is a transparent performance trick at L1 — algebraically `(sr + 0i)·x = sr·x` exactly, so eliding the imaginary cross-term when `si == 0.0` is equivalent. It disappears in the L1>L0 lowering.

A cross-cutting prose treatment lives at [`concepts/scal`](../concepts/scal.md) — covering BLAS background and call-site role (basis normalisation, search-direction rescaling). The L1 entry here is the firm operator definition; the concept page is the narrative.

## Signature

```
scal :: (α: Scalar, x: Tensor[N]) -> Tensor[N]
scal(α, x) = α·x
```

Shape contract (bunsen-style, named axes):

- `α` — scalar (real or complex, matching the vector element type).
- `x` — `Tensor[N]` — read-only (the *prior* value).
- result — `Tensor[N]` — same axis `N` as input.

`α` and `x` must share element type (both real or both complex). When `x` is complex, real `α` is promoted to complex per the [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) typing rule. The promotion site here is internal (value-based, not overload-based): `ComplexVector::operator*=` branches on `s.imag() == 0.0` at `palace/linalg/vector.cpp:207-211`.

## Semantics

Element-wise: `result[i] = α · x[i]` for `i ∈ [0, N)`. Reduction-free and element-local — every output element depends on exactly one input element. No cross-element communication, no dependence on iteration order. No MPI collective at any layer (scaling is rank-local; ranks own disjoint slices of `N`).

The operator is pure at L1: the prior `x` and the new `x` are distinct values. The L0 source overwrites the in-place destination buffer; the L1>L0 lowering theme is where that overwrite is reintroduced. At L1 the relationship is purely algebraic.

Special algebraic cases — `α = 0` (zero-fill, discards `x`), `α = 1` (identity), `α = -1` (negation) — are not separate operators at L1. They are algebraic identities recorded in the laws below. The L0 source has no constant-folding branches on `α` (unlike `AXPY(double, Vector, Vector)`'s `α == 1.0` fast path); the real-imag branch in `ComplexVector::operator*=` is a complex-scalar-shape specialisation, not a scalar-value specialisation, and disappears at L1.

`scal` and `axpby` are tightly related: `scal(α, x) = axpby(α, x, 0, y)` for any `y` (per `axpby` law 3) and equivalently `axpby(0, y, α, x)` (per law 2). The L1 `axpby` entry records this as the subsumption note. **`scal` is not factored as a dependency of `axpby`** — the harvester decision in `scaffolding/decisions/axpby-as-primitive.md` keeps `axpby` as a leaf primitive. `scal` is a sibling leaf, not a sub-operation.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Identity in `α`**: `scal(1, x) = x`. The neutral element of scalar multiplication.
2. **Absorption in `α`**: `scal(0, x) = 0` (the zero vector of axis `N`), for any `x`.
3. **Absorption in `x`**: `scal(α, 0) = 0`, for any `α`.
4. **Composition (scalar fusion)**: `scal(α, scal(β, x)) = scal(α·β, x)`. Two successive scalings collapse to one with the scalar product. The action of scalars on vectors is multiplicative.
5. **Distributivity over scalar addition**: `scal(α + β, x) = scal(α, x) + scal(β, x)`, where `+` on the right is element-wise vector addition. Linearity in the scalar argument.
6. **Distributivity over vector addition**: `scal(α, x + y) = scal(α, x) + scal(α, y)`. Linearity in the vector argument.
7. **Negation**: `scal(-1, x) = -x`. (Special case of laws 1 + 5: `scal(-1, x) + scal(1, x) = scal(0, x) = 0`.)
8. **Inverse (for non-zero scalar)**: `scal(α⁻¹, scal(α, x)) = x` for `α ≠ 0`. (Special case of law 4 with `β = α⁻¹` and law 1.) This is the rule that makes `Normalize` invertible up to the recovered `α = 1/nrm2(x)`.
9. **Commutativity of scalars (field-inherited)**: `scal(α·β, x) = scal(β·α, x)`. Inherited from the underlying field (`ℝ` or `ℂ`).

Laws that explicitly **do not** hold:

- **Idempotence**: `scal(α, scal(α, x)) ≠ scal(α, x)` in general — the result is `scal(α², x)`, which equals `scal(α, x)` only when `α ∈ {0, 1}` (more broadly when `α² = α`, i.e. `α(α−1) = 0`).
- **Commutativity in argument positions**: `α` and `x` live in distinct types (scalar vs vector). "Commutativity" is not even well-typed for the operator's argument list.
- **Distributivity over vector products**: not applicable — there is no inner-vector multiplication at L1 (`dot` reduces to a scalar; there is no element-wise vector product in the L1 vocabulary). The closest applicable rule is law 6, distributivity over vector **addition**.
- **Bit-level equivalence under fusion**: `scal(α, scal(β, x))` (law 4 LHS) and `scal(α·β, x)` (law 4 RHS) are algebraically equal but may differ at the bit level in IEEE-754 because the two-pass form rounds twice (once per element-multiply) and the fused form rounds once. This is a transparent-trick consideration at L1 (not load-bearing in the CLAUDE.md sense for the algorithms Palace runs) but is worth recording: solvers that depend on bit-determinism across fusion choices must pin the evaluation form.

## Dependencies

None at L1. `scal` is a leaf primitive — the fourth and last of the BLAS-1 floor primitives (`axpy`, `dot`, `nrm2`, `scal`). Its sub-operations are scalar multiplication and element-wise application, both at or below the L1 layer's resolution.

Sibling subsumption (not dependency):
- `scal(α, x) = axpby(α, x, 0, y) = axpby(0, y, α, x)` for any `y`. Per `axpby` laws 2 and 3 at `book/src/L1/axpby.md`. `scal` and `axpby` stay in the L1 dep-map as siblings.
- `Normalize(x) = scal(1 / nrm2(x), x)` paired with the returned norm. The free-function `linalg::Normalize` at `palace/linalg/vector.hpp:262-270` is a fused `nrm2 + scal` construct; at L1 it currently factors as the composition `scal(1/nrm2(x), x)`. Whether to harvest a fused `normalize` L1 primitive is an open question.

Downstream consumers at L1 (cross-reference, not reverse-dependencies): GMRES Arnoldi basis-normalisation `w ← w / Hj[j+1]` (`iterative.cpp:632, 811`), CG search-direction rescaling `p ← (β/β_prev) p` (per `concepts/scal.md`), eigenvector normalisation (`nleps.cpp:486-491`, `operator.cpp:661, 673` via `Normalize`).

## Variant axes

`scal` has one orthogonal variant axis at L1:

- **element-type**: `real` | `complex`. The L0 source has separate overloads (`mfem::Vector::operator*=(double)` from MFEM for real; `ComplexVector::operator*=(std::complex<double>)` at `palace/linalg/vector.cpp:203-227` for complex). At L1 these collapse to one operator parameterised by element type — the semantics are identical (per-element scalar multiplication in the appropriate field).
- **scalar promotion** (sub-axis on the complex element-type): see [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `α` against complex `x` via the internal `s.imag() == 0.0` branch at `vector.cpp:207-211`.

No other variant axes — `scal` is unconditionally pure, element-local, reduction-free, and rank-local across all variants. Unlike `axpy` (which has the real-path `α == 1.0` constant-folding specialisation at L0) and like `axpby` (which has no constant-folding), `scal` has no L0 constant-folding branches on `α` — the branch in `ComplexVector::operator*=` is a complex-scalar-shape branch (`imag == 0`), not a scalar-value branch.

## Status

`firm` — signature is canonical (matches BLAS-1 `dscal` / `zscal` and the Palace `operator*=` surface exactly), evidence is direct from `palace/linalg/vector.{hpp,cpp}` and inlined call sites, and the nine algebraic laws listed are standard scalar-vector-multiplication facts (axioms of a module over the scalar field, plus the field-commutativity inherited rule).

## L1 vs L0 distinction

- **L0**: mutating member methods. `x *= s` on `mfem::Vector` (real, MFEM); `x *= s` on `ComplexVector` (complex, Palace). Writes through `x`. The complex case branches on `imag(s) == 0.0` to a simpler path; that branch is a transparent shape-specialisation. No free-function `linalg::Scal` or `linalg::Scale` symbol exists.
- **L1**: pure functional update. `x_new = scal(α, x_old)`. No destination buffer in the signature. Algebraic laws apply directly. The L0 in-place mutation, the L0 real-imag-shape branch, and the call-site fusion with `nrm2` inside `Normalize` are all L1>L0 lowering concerns, not L1 concerns. The fused `Normalize` construct factors at L1 as `scal(1/nrm2(x), x)` — to be unified into a single operator only if a future harvester proposes a fused `normalize` L1 primitive.

## Evidence

- `palace/linalg/vector.hpp:98-99` — `ComplexVector::operator*=(std::complex<double> s)` declaration with comment `Scale all entries by s.`
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition. Lines 207-211 branch `if (si == 0.0)` to two real `operator*=` calls; lines 212-225 run the general complex-scalar `forall_switch` kernel computing `XR[i] = sr·XR[i] − si·XI[i]; XI[i] = si·XR[i] + sr·XI[i]`.
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template: `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0 / norm; return norm;` — the only Palace-side `scal` use that returns the discarded scalar (the norm). Direct evidence of `scal(1/nrm2(x), x)` as a fused construct.
- `palace/linalg/iterative.cpp:632` — GMRES Arnoldi basis-normalisation `w *= 1.0 / Hj[j + 1];` (real `scal`).
- `palace/linalg/iterative.cpp:811` — GMRES Arnoldi basis-normalisation (second analogous code path) `w *= 1.0 / Hj[j + 1];`.
- `palace/linalg/iterative.cpp:222` — `cs *= w;` — *scalar-scalar* `*=` (not a vector `scal`). Recorded as a *non*-instance for disambiguation.
- `palace/linalg/operator.cpp:661, 673` — `Normalize(comm, u)` and `l = Normalize(comm, u);` call sites in operator-side normalisation flows.
- `palace/linalg/nleps.cpp:486-491` — eigenvector normalisation call sites in nonlinear-EVP code.
- Cycle-003 firm `axpby` entry at `book/src/L1/axpby.md` — laws 2 and 3 establish the subsumption `scal(α, x) = axpby(α, x, 0, y) = axpby(0, y, α, x)`.
- Cycle-003 firm `nrm2` entry at `book/src/L1/nrm2.md` — the `Normalize` construct's `1/nrm2(x)` scalar argument is sourced here.
- `book/src/concepts/scal.md` — pre-existing cross-cutting prose treatment; consistent with this L1 entry.
