# axpby

Mutation-lifted fused two-scalar two-vector update: `y_new = α·x + β·y_old`. The fused BLAS-1 primitive that subsumes both `axpy` (β=1) and pure-scaling (α=0). At L1, the fused form is a leaf primitive; the decision against decomposing it as `axpy ∘ scal` is recorded in [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md).

## Context

The L0 source-side forms are:

- `ComplexVector::AXPBY(std::complex<double> α, const ComplexVector &x, std::complex<double> β)` — member call mutating `*this` in place to `α·x + β·(*this)` (`palace/linalg/vector.hpp:130-131`). The destination is the receiver; there is no output argument.
- `linalg::AXPBY<VecType, ScalarType>(ScalarType α, const VecType &x, ScalarType β, VecType &y)` — free-function template (`palace/linalg/vector.hpp:309-311`) with three explicit specialisations:
  - `AXPBY(double, Vector, double, Vector)` (`palace/linalg/vector.cpp:726-730`) delegates to MFEM's `add(α, x, β, y, y)` — MFEM's 5-argument in-place additive combine which writes its last argument from the linear combination of its first four.
  - `AXPBY(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)` (`palace/linalg/vector.cpp:732-737`) delegates to `y.AXPBY(α, x, β)`, i.e. the member form.
  - `AXPBY(double, ComplexVector, double, ComplexVector)` (`palace/linalg/vector.cpp:739-743`) — real-scalar overload on complex vectors; promotes scalars implicitly and delegates to the same member form.

At L0, the in-place destination `y` is overwritten; the prior value of `y` is consumed by the update and inaccessible afterwards. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, `β`, and the pre-update value of `y`, and produces a fresh post-update value. The fusion (single-call combined update rather than the two-pass `y *= β; y += α·x`) is preserved at L1 because it has algebraic meaning — the law `axpby(α, x, β, y) = α·x + β·y` is a primitive statement of the linear combination, not a derived shorthand.

This entry is the firm operator definition for `axpby` at L1; it supersedes the rough-in row in `book/src/L1/index.md` (originally proposed by the cycle-002 abstractor `axpby-mutation-rotation` theme — see [`L1-L0/axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md)). The lowering theme remains the L1>L0 narrative; this entry is the L1 algebra. No `concepts/axpby.md`-style cross-cutting prose exists yet for `axpby` (the existing `concepts/axpy.md` covers `axpy` only); if one is authored, it should cross-reference this entry.

## Signature

```
axpby :: (α: Scalar, x: Tensor[N], β: Scalar, y: Tensor[N]) -> Tensor[N]
axpby(α, x, β, y) = α·x + β·y
```

Shape contract (bunsen-style, named axes):

- `α` — scalar.
- `x` — `Tensor[N]` — read-only.
- `β` — scalar.
- `y` — `Tensor[N]` — read-only (the *prior* value).
- result — `Tensor[N]` — same axis `N` as inputs.

`x` and `y` must share the same length axis `N` and the same element type (both real or both complex). The scalars `α` and `β` share each other's type and the vector element type, with one allowed promotion: real scalars may be passed against complex vectors and the scalars are promoted to complex (zero imaginary part). This mirrors Palace's `AXPBY(double, ComplexVector, double, ComplexVector)` overload at `palace/linalg/vector.cpp:739-743`. Mixed real/complex scalar pairs (one of α, β real and the other complex) are not exposed by Palace and are not part of the L1 signature — promote both or neither.

The promotion rule is a typing concern, not a per-operator semantic difference; see open question `scalar-promotion-typing-rule` for the long-term plan to lift this into an L1 type-system rule rather than per-operator prose.

## Semantics

Element-wise: `result[i] = α·x[i] + β·y[i]` for `i ∈ [0, N)`. Reduction-free and element-local — every output element depends on exactly one input element from each of `x` and `y`. No cross-element communication, no dependence on iteration order.

The operator is pure at L1: the prior `y` and the new `y` are distinct values. The L0 source overwrites the in-place destination buffer; that overwrite is an L1>L0 lowering concern (see [`L1-L0/axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md)). At L1 the relationship is purely algebraic.

Special algebraic cases — `α = 0` (pure scaling of `y`), `β = 0` (pure scaling of `x`, discards `y`), `α = 1, β = 1` (vector add), `β = 1` (recovers `axpy`), `α = -1, β = 1` (vector subtract) — are not separate operators at L1. They are algebraic identities, recorded in the laws below. The L0 source has no specialisation branches inside the `AXPBY` family (unlike the real-path `AXPY` at `vector.cpp:704-706`, which branches on `α == 1.0`); the AXPBY surface is uniformly a single delegation, so there are no L0 sub-patterns to recognise — the L1>L0 lowering for `axpby` is structural (re-bind destination), not algebraic.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Subsumption of `axpy`**: `axpby(α, x, 1, y) = axpy(α, x, y) = α·x + y`. This is the load-bearing identity from `scaffolding/decisions/axpby-as-primitive.md`: `axpy` is a β=1 specialisation of `axpby`, not a dependency.
2. **Identity in `α`**: `axpby(0, x, β, y) = β·y` for any `x`. (When a future `scal :: (β, y) → β·y` primitive lands at L1, this restates as `axpby(0, x, β, y) = scal(β, y)`. Until then, the right-hand side is stated as the scalar-times-vector operation `β·y`.)
3. **Identity in `β`**: `axpby(α, x, 0, y) = α·x` for any `y`. (Likewise restates as `scal(α, x)` once `scal` lands.)
4. **Identities in both**: `axpby(0, x, 0, y) = 0` (the zero vector of axis `N`).
5. **Bilinearity in the scalar pair `(α, β)`**: for scalars `α₁, α₂, β`:
   - `axpby(α₁ + α₂, x, β, y) = axpby(α₁, x, β, y) + axpby(α₂, x, 0, y) - β·y + β·y = α₁·x + α₂·x + β·y` (i.e., the result is linear in `α` with `(x, β, y)` held fixed).
   - Symmetrically linear in `β` with `(α, x, y)` held fixed.
   - Combined: `axpby(α, x, β, y)` is linear separately in each of `α` and `β`.
6. **Right distribution over vector addition in `x`**: `axpby(α, x₁ + x₂, β, y) = axpby(α, x₁, β, y) + axpby(α, x₂, 0, y) = α·x₁ + α·x₂ + β·y`. (The `axpby(α, x₂, 0, y)` term is `α·x₂` per law 3; the `+` is vector addition.)
7. **Right distribution over vector addition in `y`**: `axpby(α, x, β, y₁ + y₂) = axpby(α, x, β, y₁) + β·y₂ = α·x + β·y₁ + β·y₂`.
8. **Scalar absorption**: `axpby(α·γ, x, β, y) = axpby(α, γ·x, β, y) = axpby(α, x, β·γ, γ⁻¹·y)` (the latter only for invertible scalar `γ`) — the scalars absorb into their paired vector.
9. **Chained-`axpby` collapse on shared `x`**: `axpby(α₁, x, β₁, axpby(α₂, x, β₂, y)) = axpby(α₁ + β₁·α₂, x, β₁·β₂, y)`. Two successive `axpby` updates against the same `x` collapse to one with scalars `(α₁ + β₁·α₂, β₁·β₂)`. This generalises law 4 of `axpy` (`axpy(α, x, axpy(β, x, y)) = axpy(α+β, x, y)`, which is the β₁ = β₂ = 1 case) and underwrites the L2 fusion of consecutive coefficient-update lines in Krylov solvers.

Laws that explicitly **do not** hold:

- **Commutativity in the vector arguments**: `axpby(α, x, β, y) ≠ axpby(β, y, α, x)` in general unless `α = β` — but even then the result is symmetric in the inputs only because the operator is structurally `α·x + β·y`. The signature distinguishes "the `x` argument" from "the `y` argument" by which slot pairs with which scalar; swapping both pairs simultaneously preserves the value (because `α·x + β·y = β·y + α·x`), but swapping vectors without swapping scalars does not.
- **Associativity**: `axpby` is quaternary; "associativity" is not well-typed.
- **Floating-point associativity of the summation**: `α·x + β·y` computed in IEEE-754 may differ from `β·y + α·x` at the bit level when the magnitudes of `α·x` and `β·y` differ enough to lose precision in one ordering. Palace's L0 form pins the ordering via MFEM's `add(α, x, β, y, y)` kernel — the L1 algebra is order-agnostic, but bit-identical reproduction of L0 output requires matching the L0 evaluation order. This is recorded here, not erased.
- **Fusion identity with `scal + axpy`**: `axpby(α, x, β, y) ≠ scal(β, axpy(α/β, x, y))` in general at the bit level (the two-pass form rounds twice; the fused form rounds once) even though the values agree mathematically. The L0 form is fused for a reason; the L1 algebra preserves the fused statement. The lowering theme records the fusion choice as load-bearing for performance, not for numerics.

## Dependencies

None at L1. `axpby` is a leaf primitive — the harvester decision (`scaffolding/decisions/axpby-as-primitive.md`) is explicit on this point. Its sub-operations are two scalar multiplications and one element-wise addition, all at or below the L1 layer's resolution.

Subsumption (not dependency): `axpy(α, x, y) ≡ axpby(α, x, 1, y)` — both stay in the L1 dep-map as siblings; the L1>L0 lowering theme `axpby-mutation-rotation` covers `axpy`'s sub-patterns A/B/C as the β=1 specialisation of `axpby`'s lowering (per the abstractor's "Subsumption relation" paragraph).

Future siblings (not dependencies): `axpbypcz` (the three-vector generalisation `z = α·x + β·y + γ·z`) is the next harvester target — see open question `axpby-axpbypcz-next-harvest`. The real-path `AXPBYPCZ` at `vector.cpp:749-752` branches on `γ == 0` and delegates to `AXPBY`, confirming the subsumption chain `axpy ≺ axpby ≺ axpbypcz` at L1 (each generalises the prior by one more scalar-vector pair).

## Variant axes

`axpby` has two variant axes at L1:

- **element-type**: `real` | `complex`. The L0 source has separate template specialisations (real-real at `vector.cpp:726-730`; complex-complex at `vector.cpp:732-737`; real-scalar-on-complex-vector at `vector.cpp:739-743`; member form on `ComplexVector` at `vector.hpp:130-131`). At L1 these collapse to one operator parameterised by element type. The semantics are identical across element types — the per-element kernel is just `α·x[i] + β·y[i]` in the appropriate field.
- **scalar promotion** (sub-axis on the complex element-type): when `α` and `β` are real but vectors are complex, Palace permits implicit promotion via the dedicated overload at `vector.cpp:739-743`. At L1 this is a typing-rule concern (subtype broadcasting), not a separate operator. The long-term plan is to formalise this as an L1 type-system rule rather than per-operator prose — tracked at open question `scalar-promotion-typing-rule`.

No other variant axes — `axpby` is unconditionally pure, element-local, and reduction-free across all variants. Unlike `axpy` (which has the real-path `α == 1.0` constant-folding specialisation at L0), `axpby` has no L0 constant-folding branches — the AXPBY surface uniformly delegates without inspecting scalar values. Consequently, the L1>L0 lowering for `axpby` does not need an algebraic-sub-rule mechanism; it is purely structural.

## Status

`firm` — signature is canonical (matches three Palace L0 entry points exactly), evidence is direct from the Palace source, the algebraic laws listed are standard linear-combination facts, and the decomposition decision is recorded in `scaffolding/decisions/axpby-as-primitive.md`.

## L1 vs L0 distinction

- **L0**: mutating member method (`ComplexVector::AXPBY(α, x, β)` writes through `*this`) or free-function template (`linalg::AXPBY(α, x, β, y)` writes through `y`). Delegates to MFEM's `add(α, x, β, y, y)` for the real-real path or to the member form for the complex paths. No constant-folding branches on `α` or `β`. The evaluation order of `α·x` and `β·y` is pinned by the underlying kernel.
- **L1**: pure functional update. `y_new = axpby(α, x, β, y_old)`. No destination buffer in the signature. Algebraic laws apply directly. The L0 in-place mutation and the L0 fusion choice are both L1>L0 lowering concerns. Floating-point evaluation-order non-associativity is recorded as an explicit non-law, classified as load-bearing for bit-reproduction but not for algorithmic correctness.

## Evidence

- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member decl with comment `In-place addition (*this) = alpha * x + beta * (*this).`
- `palace/linalg/vector.hpp:309-311` — free-function template `AXPBY(ScalarType alpha, const VecType &x, ScalarType beta, VecType &y)` declared with comment `Addition y = alpha * x + beta * y.`
- `palace/linalg/vector.cpp:726-730` — `AXPBY(double, Vector, double, Vector)` specialisation: delegates to `add(alpha, x, beta, y, y)` (MFEM's 5-arg in-place linear combine).
- `palace/linalg/vector.cpp:732-737` — `AXPBY(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)` specialisation: delegates to member `y.AXPBY(alpha, x, beta)`.
- `palace/linalg/vector.cpp:739-743` — `AXPBY(double, ComplexVector, double, ComplexVector)` specialisation: real-scalar-on-complex-vector overload; also delegates to the member form (implicit promotion).
- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double, ...)` real-path with `γ == 0` branch to `add(alpha, x, beta, y, z)` (confirms the subsumption `axpbypcz(α, x, β, y, 0, z) = axpby(α, x, β, y)` at L0).
- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl (forward reference for the next harvester target).
- `palace/linalg/vector.hpp:313-316` — free-function template `AXPBYPCZ` decl (forward reference).
- Decision record: [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md) — fused-primitive choice rationale.
- Cross-references: `book/src/L1-L0/axpby-mutation-rotation.md` (L1>L0 lowering theme, cycle-002), `book/src/L1/axpy.md` (the β=1 specialisation; sibling L1 leaf).
