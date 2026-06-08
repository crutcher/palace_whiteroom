---
layer: L1
operator: axpby
rank: firm
# Firm-in-prose fused BLAS-1 leaf — matches three Palace L0 entry points exactly,
# syntactic-identity laws (firm-on-positive-structure). Blocking depends-on =
# rank-terminal POSITIVE L0 SOURCE (cites-evidence) → well-founds the `firm` rank.
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:726-730
      kind: cites-evidence        # AXPBY(double,Vector,double,Vector) → MFEM add(...)
    - target: palace/linalg/vector.cpp:732-737
      kind: cites-evidence        # AXPBY(complex,...) → member form
    - target: palace/linalg/vector.cpp:739-743
      kind: cites-evidence        # AXPBY(double,ComplexVector,...) real-scalar-on-complex
    - target: palace/linalg/vector.hpp:130-131
      kind: cites-evidence        # ComplexVector::AXPBY member decl
    - target: palace/linalg/vector.hpp:309-311
      kind: cites-evidence        # free-function template AXPBY decl
    - target: L1-L0/axpby-mutation-rotation
      kind: lowers-to             # the L1>L0 lowering theme this leaf lowers to
  reference:
    - L1/axpy
    - L1/axpbypcz
    - L1/scal
    - L2/linear_combination
    - concepts/scalar-promotion
---

# axpby

Mutation-lifted fused two-scalar two-vector update: `y_new = α·x + β·y_old`. The fused BLAS-1 primitive that subsumes both `axpy` (β=1) and pure-scaling (α=0). At L1, the fused form is a leaf primitive; the decision against decomposing it as `axpy ∘ scal` is recorded in [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md).

## Context

`axpby` lifts Palace's fused two-scalar two-vector update from two L0 idioms (receiver-mutating `ComplexVector::AXPBY(α, x, β)` and free-function-form `linalg::AXPBY(α, x, β, y)` with three template specialisations: real-real delegating to MFEM `add(α, x, β, y, y)`, complex-complex and real-scalar-on-complex-vector both delegating to the member form) to a single pure-functional operator. The L0 file layout — the AXPBY family in `palace/linalg/vector.{hpp,cpp}` and its place in the AXPY → AXPBY → AXPBYPCZ subsumption chain — is detailed in [`L0/linalg-vector-file`](../L0/linalg-vector-file.md) "The BLAS-1 fused-update family". The receiver-vs-output-arg idiom split is named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md); the free-function template-dispatch pattern over the member form is named in [`L0/linalg-free-functions`](../L0/linalg-free-functions.md) "Pure forward to method-form". The element-type axis (real / complex / scalar-promoted) is named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md). Unlike `axpy`, no constant-folding branches exist in the `AXPBY` family — the L0 surface uniformly delegates without inspecting scalar values, per [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination `y` is overwritten; the prior value of `y` is consumed by the update and inaccessible afterwards. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, `β`, and the pre-update value of `y`, and produces a fresh post-update value. The fusion (single-call combined update rather than the two-pass `y *= β; y += α·x`) is preserved at L1 because it has algebraic meaning — the law `axpby(α, x, β, y) = α·x + β·y` is a primitive statement of the linear combination, not a derived shorthand.

This entry is the firm operator definition for `axpby` at L1. The [`L1-L0/axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) theme is the L1>L0 narrative; this entry is the L1 algebra. The existing `concepts/axpy.md` cross-cutting prose covers `axpy` only.

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

`x` and `y` must share the same length axis `N` and the same element type (both real or both complex). The scalars `α` and `β` share each other's type and the vector element type. When the vectors are complex, real scalars are promoted to complex (all-or-none across the scalar pair) per the [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) typing rule, realised at `palace/linalg/vector.cpp:739-743`.

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

Subsumption (not dependency): `axpy(α, x, y) ≡ axpby(α, x, 1, y)` — both stay in the L1 dep-map as siblings; the L1>L0 lowering theme `axpby-mutation-rotation` covers `axpy`'s sub-patterns A/B/C as the β=1 specialisation of `axpby`'s lowering.

Future siblings (not dependencies): `axpbypcz` (the three-vector generalisation `z = α·x + β·y + γ·z`). The real-path `AXPBYPCZ` at `vector.cpp:749-752` branches on `γ == 0` and delegates to `AXPBY`, confirming the subsumption chain `axpy ≺ axpby ≺ axpbypcz` at L1 (each generalises the prior by one more scalar-vector pair).

## Variant axes

`axpby` has two variant axes at L1:

- **element-type**: `real` | `complex`. The L0 source has separate template specialisations (real-real at `vector.cpp:726-730`; complex-complex at `vector.cpp:732-737`; real-scalar-on-complex-vector at `vector.cpp:739-743`; member form on `ComplexVector` at `vector.hpp:130-131`). At L1 these collapse to one operator parameterised by element type. The semantics are identical across element types — the per-element kernel is just `α·x[i] + β·y[i]` in the appropriate field.
- **scalar promotion** (sub-axis on the complex element-type): see [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `(α, β)` against complex vectors via `vector.cpp:739-743`.

No other variant axes — `axpby` is unconditionally pure, element-local, and reduction-free across all variants. Unlike `axpy` (which has the real-path `α == 1.0` constant-folding specialisation at L0), `axpby` has no L0 constant-folding branches — the AXPBY surface uniformly delegates without inspecting scalar values. Consequently, the L1>L0 lowering for `axpby` does not need an algebraic-sub-rule mechanism; it is purely structural.

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
- Cross-references: `book/src/L1-L0/axpby-mutation-rotation.md` (L1>L0 lowering theme), `book/src/L1/axpy.md` (the β=1 specialisation; sibling L1 leaf).
