---
layer: L3
operator: axpby
firmness: firm
lowers_to:
  - book/src/L2/axpby.md (present adjacent L2 floor, cycle-043; identity-in-form on the primitive's signature shape, via the `axpby-body-identity` L3>L2 theme; whole-tensor in / whole-tensor out at both layers) → book/src/L1/axpby.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
lifts_from:
  - (no L4 entry — leaf primitive, not a calculus combinator; per cycle-010 cohort audit verdict)
variant_axes:
  - element-type (real | complex)
  - scalar-promotion (sub-axis on complex element-type)
---

# axpby

Whole-tensor fused two-scalar two-vector update at L3: `axpby(α, x, β, y) = α·x + β·y`. The L3-native rendering of the fused BLAS-1 primitive that subsumes [`axpy`](./axpy.md) (β=1) and pure-scaling (α=0), firm at L1 ([`axpby`](../L1/axpby.md)), surfaced here in L3 vocabulary because **each layer is internally coherent** (CLAUDE.md §Methodology invariants).

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, no element loops, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `axpby` at L3 is a whole-tensor linear-combination primitive consumed by `krylov-step`'s iterate-stratum update (per [`krylov-step`](./krylov-step.md) §Semantics line 82: `krylov_update` at L3 composes whole-tensor primitives including `axpby`).

The L3 form is **value-thread-isomorphic to the L1 form**: `axpby`'s L1 signature is whole-tensor in / whole-tensor out with no element loop exposed (the L1 entry is written against `Tensor[N]` arguments). The L3 layer's vocabulary requirement — whole-tensor primitives, no element loops — is satisfied by L1's signature shape directly. The rotation L3→L1 is therefore the identity on the primitive itself; the per-element semantics that L1 uses to describe the operator (`result[i] = α·x[i] + β·y[i]`) is the referent, not the surface.

This L3 entry is the layer-coherence anchor for the cycle-011 BLAS-1 cohort backfill. Mirrors the cycle-010 `book/src/L3/krylov-step.md` precedent. One of three sibling firmings in the cycle-011 wave-1 BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`).

`axpby` is the fused-primitive choice (not a decomposition of `scal ∘ axpy`); the decision is recorded in [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md) (cycle-003) and inherited at L3 unchanged — the fusion preserves the algebraic statement `α·x + β·y` as a primitive linear combination, and the L3 layer's whole-tensor discipline is consistent with that primitive shape.

## Signature

```text
axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
```

Positional value-threading; no monadic effect; no record-typing:

- `α : Scalar` — first scalar coefficient.
- `x : Tensor[N]` — first input tensor; whole-tensor read.
- `β : Scalar` — second scalar coefficient.
- `y : Tensor[N]` — second input tensor (the *prior* value, when used as a fused update); whole-tensor read.
- result `: Tensor[N]` — output tensor; whole-tensor write (fresh value).

Shape contract (bunsen-style, named axis):

- `N` — length axis; shared across `x`, `y`, and the result.
- element type — uniform across `x`, `y`; uniform `Scalar` for both `α` and `β` matches the vector element type modulo scalar promotion.

`x` and `y` must share the same length axis `N` and the same element type. The scalars `α` and `β` share each other's type and the vector element type. When the vectors are complex, real scalars are promoted to complex (all-or-none across the scalar pair) per the [`scalar-promotion`](../concepts/scalar-promotion.md) typing rule. The L3 form inherits the `real ⊑ complex` scalar lattice from L1.

The L3 calculus has no record-typing and no `readonly` annotation; the signature is positional. The argument ordering `(α, x, β, y)` interleaves scalars and tensors; this matches both the L1 signature and the upstream L0 Palace API surface (`palace/linalg/vector.cpp:726-743`).

## Semantics

`axpby` at L3 is a single whole-tensor fused linear combination: `axpby(α, x, β, y)` produces the tensor `α·x + β·y`, computed in a single primitive step (the fusion is preserved at L3 because it has algebraic meaning — the law `axpby(α, x, β, y) = α·x + β·y` is a primitive statement of the linear combination, not a derived shorthand).

The operator is **pure at L3**: the prior `y` and the new value (returned positionally) are distinct values; no destination buffer appears in the signature. The L3 form has no aliasing — both inputs and the output are conceptually distinct tensors. In-place mutation reappears in the L1>L0 lowering chain via [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md); the L3 form is uniformly out-of-place.

**The operator is reduction-free and element-local at the referent semantics**: the per-element relation `result[i] = α·x[i] + β·y[i]` holds at every position independently, with no cross-element communication. This is a property of the referent, observable when the L3 form is lowered to L1.

**The operator carries no sequential obstruction**: `axpby` is a leaf primitive at L3 (and at L1); the iteration-rotation marker (per [`sequential-obstruction`](../concepts/sequential-obstruction.md)) does not apply to it. The sequential obstruction lives at the consuming composition (the outer `iterate_while_L3` loop folding `krylov-step`), not at `axpby` itself.

Special algebraic cases — `α = 0` (pure scaling of `y`), `β = 0` (pure scaling of `x`, discards `y`), `α = 1, β = 1` (vector add), `β = 1` (recovers `axpy`), `α = -1, β = 1` (vector subtract) — are not separate operators at L3. They are algebraic identities, recorded in §Algebraic laws. The L0 source has no constant-folding branches inside the `AXPBY` family (unlike `axpy`'s `α == 1.0` fast-path); the L0 surface uniformly delegates without inspecting scalar values, per `book/src/L1/axpby.md` §Semantics.

### Iteration-rotation marker

L3 is the iteration-rotation layer, but `axpby` is a **leaf primitive** with no iteration view of its own — it is a single whole-tensor operation, not a fold over a trajectory. The iteration view applies to compositions of `axpby` (notably `krylov-step`'s iterate-stratum update). At the leaf `axpby` itself, there is no iteration carry, no successor relation, no fold. The L3 layer-coherence reason for this entry is **vocabulary inventory**, not iteration-view content.

## Algebraic laws

Inherited verbatim from L1 (per the identity-in-form rotation). The laws below hold at L3 because they hold at L1 and the L3 form is value-thread-isomorphic to the L1 form.

1. **Subsumption of `axpy`**: `axpby(α, x, 1, y) = axpy(α, x, y) = α·x + y`. Load-bearing identity from `scaffolding/decisions/axpby-as-primitive.md`: [`axpy`](./axpy.md) is the β=1 specialisation of `axpby`, not a dependency. Both stay in the L3 dep-map as siblings.
2. **Identity in `α`**: `axpby(0, x, β, y) = β·y` for any `x`. (When [`scal`](./scal.md) lands at L3, restates as `axpby(0, x, β, y) = scal(β, y)`. Until then, stated as the scalar-times-tensor operation `β·y`.)
3. **Identity in `β`**: `axpby(α, x, 0, y) = α·x` for any `y`. (Likewise restates as `scal(α, x)` once `scal` lands.)
4. **Identities in both**: `axpby(0, x, 0, y) = 0` (the zero tensor of axis `N`).
5. **Bilinearity in the scalar pair `(α, β)`**: `axpby(α, x, β, y)` is linear separately in each of `α` and `β` (with the other scalar and both tensors held fixed). Inherited from L1 Law 5.
6. **Right distribution over tensor addition in `x`**: `axpby(α, x₁ + x₂, β, y) = axpby(α, x₁, β, y) + axpby(α, x₂, 0, y) = α·x₁ + α·x₂ + β·y`. (The `axpby(α, x₂, 0, y)` term is `α·x₂` per Law 3; the `+` is tensor addition. Verbatim form from L1 axpby Law 6.)
7. **Right distribution over tensor addition in `y`**: `axpby(α, x, β, y₁ + y₂) = axpby(α, x, β, y₁) + β·y₂ = α·x + β·y₁ + β·y₂`.
8. **Scalar absorption**: `axpby(α·γ, x, β, y) = axpby(α, γ·x, β, y) = axpby(α, x, β·γ, γ⁻¹·y)` (the latter only for invertible scalar `γ`) — the scalars absorb into their paired tensor.
9. **Chained-`axpby` collapse on shared `x`**: `axpby(α₁, x, β₁, axpby(α₂, x, β₂, y)) = axpby(α₁ + β₁·α₂, x, β₁·β₂, y)`. Two successive `axpby` updates against the same `x` collapse to one with scalars `(α₁ + β₁·α₂, β₁·β₂)`. Generalises Law 4 of `axpy` (the β₁ = β₂ = 1 case). Underwrites the consuming composition's fusion of consecutive coefficient-update lines.

Laws that explicitly **do not** hold (inherited from L1):

- **Commutativity in the tensor arguments**: `axpby(α, x, β, y) ≠ axpby(β, y, α, x)` in general unless `α = β` — the operator is symmetric in the inputs only because `α·x + β·y = β·y + α·x` mathematically, and the signature distinguishes argument slots by which scalar pairs with which tensor.
- **Associativity**: `axpby` is quaternary; associativity is not well-typed.
- **Floating-point associativity of the summation**: `α·x + β·y` computed in IEEE-754 may differ from any reordering at the bit level when the magnitudes of `α·x` and `β·y` differ enough to lose precision. The L3 form is order-agnostic algebraically; bit-identical reproduction of L0 output requires matching the L0 evaluation order (pinned by MFEM's `add(α, x, β, y, y)` kernel). Inherited from L1; recorded here, not erased.
- **Fusion identity with `scal + axpy`**: `axpby(α, x, β, y) ≠ scal(β, axpy(α/β, x, y))` in general at the bit level (the two-pass form rounds twice; the fused form rounds once) even though the values agree mathematically. The L0 form is fused for a reason; the L3 algebra preserves the fused statement.

The algebraic-law set at L3 is **identical** to the L1 algebraic-law set.

## Dependencies

**Same-layer (L3)**: no other L3 operators (axpby is a leaf primitive). The composition surfaces that consume `axpby` at L3 are the iterate-stratum update inside `krylov-step`'s `krylov_update` (per [`krylov-step`](./krylov-step.md) §Semantics).

**Subsumption (not dependency)**: `axpy(α, x, y) ≡ axpby(α, x, 1, y)` — both stay in the L3 dep-map as siblings.

**Cross-cutting concepts** (consumed unchanged across the chain):

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the `real ⊑ complex` typing-rule. Inherited from L1 verbatim; no L3-specific semantics.
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — underwrites the L3-native-by-signature-shape claim.

No L4 monadic vocabulary; `axpby` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpby` is **CONFIRMED-NOT-NEEDED** (leaf primitives don't get L4 rows). The adjacent L3>L2 rotation passes through the **present** L2 floor [`axpby`](../L2/axpby.md) (cycle-043) via the firm [`axpby-body-identity`](../L3-L2/axpby-body-identity.md) L3>L2 theme — identity-in-form on the body, no wrapper rotation; onward to L1 [`axpby`](../L1/axpby.md). The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent, per **Identity-lowerings still require both L levels**.

## Variant axes

Inherited unchanged from the L1 entry at two:

1. **element-type** (`real | complex`) — the L1 entry distinguishes real-vector and complex-vector overloads; at L3 these collapse to one operator parameterised by element type. Semantics are identical across element types.
2. **scalar-promotion** (sub-axis on the complex element-type) — see [`scalar-promotion`](../concepts/scalar-promotion.md). Real `(α, β)` against complex `x, y` is promoted to complex with zero imaginary part (all-or-none across the scalar pair). Typing-rule property, not an operator variant.

The variant-axis profile at L3 matches L1 exactly. No new axes introduced; no axes merged or split.

## Status

`firm` — whole-tensor positional signature is canonical at L3; algebraic laws are the nine that hold at L1 (inherited verbatim under the identity-in-form rotation); non-laws are catalogued explicitly; variant-axis profile is closed at two. The pattern is well-attested via L1 (cycle-003 firm) and via the L3-L2 body-identity theme's §"Applicability conditions" point 3, which explicitly names `axpby` as L3-native by signature shape. This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** per **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase). One of three sibling firmings in the BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`).

## Lowers to

L3 `axpby` lowers to the **present adjacent L2 floor** [`axpby`](../L2/axpby.md) (cycle-043) as **identity-in-form on the primitive's signature shape**, via the firm [`axpby-body-identity`](../L3-L2/axpby-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `axpby` is a leaf whole-tensor field operation, not a step body), and onward to L1 [`axpby`](../L1/axpby.md). The three surfaces are textually identical modulo layer-coherence vocabulary (L1 / L2 / L3 all see `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` with the same shape contract, the same nine algebraic laws, the same four non-laws, and the same variant-axis profile). The L2 floor is the standalone fold-member BLAS-1 leaf — landed by the cycle-043 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive rotation in the chain is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md).

## Lifts from

No L4 entry exists for `axpby` (the cohort audit verdict is **CONFIRMED-NOT-NEEDED** for the BLAS-1 cohort at L4). `axpby` appears inside L4 entries as a let-binding inside `krylov-step`'s body but is not a first-class L4 calculus combinator.

## Evidence

All L0 evidence is inherited via L1 (`book/src/L1/axpby.md` §Evidence). Direct citations relevant to this L3 entry:

- `book/src/L2/axpby.md` (cycle-043 firm) — the present adjacent L2 floor this L3 entry lowers into via the `axpby-body-identity` theme; identity-in-form on the primitive's signature.
- `book/src/L3-L2/axpby-body-identity.md` (cycle-043 firm) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation.
- `book/src/L1/axpby.md` (cycle-003 firm) — the L1 form this L3 entry transitively rotates from (L3>L2 ∘ L2>L1). Body shape, semantics, nine algebraic laws, four non-laws, variant-axis profile.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm) — names `axpby` as L3-native by signature shape.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:67` (firm) — renders `axpby` in the L3 body let-chain identically to L1.
- `book/src/L3/index.md:13` — L3 vocabulary inventory implicitly covering the linear-update cohort.
- `book/src/L3/krylov-step.md` (cycle-010 firm; the precedent layer-coherence backfill) — the template this entry follows.
- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` — the cycle-010 audit identifying this cohort as HIGH CONFIDENCE backfill.
- `scaffolding/decisions/axpby-as-primitive.md` (cycle-003) — the fused-primitive choice rationale, inherited at L3 unchanged.
- `concepts/scalar-promotion.md` (cycle-005 firm) — the typing-rule for the real-on-complex-vector case at L3 / L1.

L0 source ranges (inherited via L1; not consumed as new evidence at L3):

- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member decl.
- `palace/linalg/vector.hpp:309-311` — free-function template `AXPBY`.
- `palace/linalg/vector.cpp:726-730` — real-real `AXPBY`.
- `palace/linalg/vector.cpp:732-737` — complex-complex `AXPBY`.
- `palace/linalg/vector.cpp:739-743` — real-α-real-β-on-complex-vector promotion site.

## L3 vs L1 distinction

- **L1**: whole-tensor pure-functional update `axpby :: (α, x, β, y) -> α·x + β·y`. Mutation-lifted from the L0 source's in-place form; the fused primitive that subsumes `axpy` and pure-scaling. The closest pure-functional layer to the source.
- **L3**: whole-tensor pure-functional update `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`. The iteration-rotation layer's rendering, value-thread-isomorphic to the L1 form. The L3 entry exists for layer-coherence.

The two layers' entries share the algebraic-law set, the variant-axis profile, the referent semantics, the fused-primitive choice, and the cited L0 evidence. They differ in **layer-coherence framing**: L1 frames the operator as the mutation-rotation lift from L0; L3 frames the operator as a whole-tensor field operation at the iteration-rotation layer. The body of the operator is the identity rotation across this edge.
