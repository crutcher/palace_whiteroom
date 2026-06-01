---
layer: L3
operator: axpbypcz
firmness: firm
lowers_to:
  - book/src/L2/axpbypcz.md (present adjacent L2 floor, cycle-043 D5; identity-in-form on the primitive's signature shape, via the `axpbypcz-body-identity` L3>L2 theme; whole-tensor in / whole-tensor out at both layers) → book/src/L1/axpbypcz.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
lifts_from:
  - (no L4 entry — leaf primitive, not a calculus combinator; per cycle-010 cohort audit verdict)
variant_axes:
  - element-type (real | complex)
  - scalar-promotion (sub-axis on complex element-type)
---

# axpbypcz

Whole-tensor fused three-scalar three-vector update at L3: `axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z`. The L3-native rendering of the fused BLAS-1-extended primitive that subsumes [`axpby`](./axpby.md) (γ=0), [`axpy`](./axpy.md) (β=1, γ=0), and pure-scaling (α=0, β=0), firm at L1 ([`axpbypcz`](../L1/axpbypcz.md)), surfaced here in L3 vocabulary because **each layer is internally coherent** (CLAUDE.md §Methodology invariants).

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, no element loops, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `axpbypcz` at L3 is a whole-tensor three-vector linear-combination primitive consumed by `krylov-step`'s iterate-stratum update for the three-vector slice patterns (Chebyshev, BiCGStab; per [`krylov-step`](./krylov-step.md) §Semantics line 82: `krylov_update` at L3 composes whole-tensor primitives including `axpbypcz`).

The L3 form is **value-thread-isomorphic to the L1 form**: `axpbypcz`'s L1 signature is whole-tensor in / whole-tensor out with no element loop exposed (the L1 entry is written against `Tensor[N]` arguments). The L3 layer's vocabulary requirement is satisfied by L1's signature shape directly. The rotation L3→L1 is the identity on the primitive itself; the per-element semantics that L1 uses to describe the operator (`result[i] = α·x[i] + β·y[i] + γ·z[i]`) is the referent.

This L3 entry is the layer-coherence anchor for the cycle-011 BLAS-1 cohort backfill. One of three sibling firmings in the cycle-011 wave-1 BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`).

`axpbypcz` is the fused-primitive choice (not a decomposition); the decision mirrors `axpby`'s cycle-003 fused-primitive verdict (per `scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects" — explicit invitation for the `axpbypcz` harvester to mirror the fused-primitive choice). Inherited at L3 unchanged.

## Signature

```text
axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
```

Positional value-threading; no monadic effect; no record-typing:

- `α : Scalar` — first scalar coefficient.
- `x : Tensor[N]` — first input tensor; whole-tensor read.
- `β : Scalar` — second scalar coefficient.
- `y : Tensor[N]` — second input tensor; whole-tensor read.
- `γ : Scalar` — third scalar coefficient.
- `z : Tensor[N]` — third input tensor (the *prior* value, when used as a fused update); whole-tensor read.
- result `: Tensor[N]` — output tensor; whole-tensor write (fresh value).

Shape contract (bunsen-style, named axis):

- `N` — length axis; shared across `x`, `y`, `z`, and the result.
- element type — uniform across `x`, `y`, `z`; uniform `Scalar` for `α`, `β`, `γ` matches the vector element type modulo scalar promotion.

`x`, `y`, and `z` must share the same length axis `N` and the same element type. The scalars `α`, `β`, `γ` share each other's type and the vector element type. When the vectors are complex, real scalars are promoted to complex (all-or-none across the scalar triple) per the [`scalar-promotion`](../concepts/scalar-promotion.md) typing rule.

The L3 calculus has no record-typing and no `readonly` annotation; the signature is positional. The argument ordering `(α, x, β, y, γ, z)` interleaves scalars and tensors; this matches both the L1 signature and the upstream L0 Palace API surface (`palace/linalg/vector.cpp:745-772`).

## Semantics

`axpbypcz` at L3 is a single whole-tensor fused three-way linear combination: `axpbypcz(α, x, β, y, γ, z)` produces the tensor `α·x + β·y + γ·z`, computed in a single primitive step (the fusion is preserved at L3 because it has algebraic meaning — the law is a primitive statement of the linear combination).

The operator is **pure at L3**: the prior `z` and the new value (returned positionally) are distinct values; no destination buffer appears in the signature. In-place mutation reappears in the L1>L0 lowering chain via [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md); the L3 form is uniformly out-of-place.

**The operator is reduction-free and element-local at the referent semantics**: the per-element relation `result[i] = α·x[i] + β·y[i] + γ·z[i]` holds at every position independently.

**The operator carries no sequential obstruction**: `axpbypcz` is a leaf primitive at L3 (and at L1); the iteration-rotation marker does not apply to it.

Special algebraic cases — `γ = 0` (recovers `axpby`), `β = 0, γ = 0` (recovers `axpy` with α=α), `β = 1, γ = 0` (recovers `axpy`), `α = 0` (drops `x`, gives `axpby(β, y, γ, z)`), all-zero (zero tensor) — are not separate operators at L3. They are algebraic identities, recorded in §Algebraic laws. The L0 source has exactly one specialisation branch inside the `AXPBYPCZ` family (the real-real path's `γ == 0` constant-fold to MFEM's `add(α, x, β, y, z)`); this is a transparent performance trick at L1 that has already been erased; it does not reappear at L3.

### Iteration-rotation marker

L3 is the iteration-rotation layer, but `axpbypcz` is a **leaf primitive** with no iteration view of its own. The iteration view applies to compositions of `axpbypcz` (notably `krylov-step`'s iterate-stratum update in three-vector slices). At the leaf `axpbypcz` itself, there is no iteration carry, no successor relation, no fold. The L3 layer-coherence reason for this entry is **vocabulary inventory**, not iteration-view content.

## Algebraic laws

Inherited verbatim from L1 (per the identity-in-form rotation). The laws below hold at L3 because they hold at L1.

1. **Subsumption of `axpby`**: `axpbypcz(α, x, β, y, 0, z) = axpby(α, x, β, y)` for any `z`. Load-bearing identity from the L0 `γ == 0` branch. Both stay in the L3 dep-map as siblings.
2. **Subsumption of `axpy`**: `axpbypcz(α, x, 1, y, 0, z) = axpy(α, x, y)` for any `z`. Composition of Law 1 (γ=0 → axpby) and axpby Law 1 (β=1 → axpy).
3. **Identity in `α`**: `axpbypcz(0, x, β, y, γ, z) = β·y + γ·z = axpby(β, y, γ, z)` for any `x`.
4. **Identity in `β`**: `axpbypcz(α, x, 0, y, γ, z) = α·x + γ·z = axpby(α, x, γ, z)` for any `y`.
5. **Identity in `γ`**: see Law 1 (γ=0 subsumption — recovers `axpby(α, x, β, y)`).
6. **All-zero identity**: `axpbypcz(0, x, 0, y, 0, z) = 0` (the zero tensor of axis `N`) for any `x`, `y`, `z`.
7. **Trilinearity in the scalar triple `(α, β, γ)`**: `axpbypcz(α, x, β, y, γ, z)` is linear separately in each of `α`, `β`, `γ` (with the others and all tensors held fixed). Inherited from L1 Law 7.
8. **Right distribution over tensor addition in `x`**: `axpbypcz(α, x₁ + x₂, β, y, γ, z) = axpbypcz(α, x₁, β, y, γ, z) + α·x₂`.
9. **Right distribution over tensor addition in `y`**: `axpbypcz(α, x, β, y₁ + y₂, γ, z) = axpbypcz(α, x, β, y₁, γ, z) + β·y₂`.
10. **Right distribution over tensor addition in `z`**: `axpbypcz(α, x, β, y, γ, z₁ + z₂) = axpbypcz(α, x, β, y, γ, z₁) + γ·z₂`.
11. **Scalar absorption**: `axpbypcz(α·κ, x, β, y, γ, z) = axpbypcz(α, κ·x, β, y, γ, z)` and symmetrically for the `β`/`y` and `γ`/`z` pairs.
12. **Chained-`axpbypcz` collapse on shared `(x, y)`**: `axpbypcz(α₁, x, β₁, y, γ₁, axpbypcz(α₂, x, β₂, y, γ₂, z)) = axpbypcz(α₁ + γ₁·α₂, x, β₁ + γ₁·β₂, y, γ₁·γ₂, z)`. Generalises axpby Law 9.

Laws that explicitly **do not** hold (inherited from L1):

- **Commutativity in the tensor arguments**: `axpbypcz(α, x, β, y, γ, z) ≠ axpbypcz(β, y, α, x, γ, z)` in general unless `α = β` — the operator is symmetric in the inputs only because the linear combination is commutative mathematically; the signature distinguishes argument slots by which scalar pairs with which tensor.
- **Associativity**: `axpbypcz` is six-ary (three scalar-tensor pairs); associativity is not well-typed.
- **Floating-point associativity of the summation**: `α·x + β·y + γ·z` computed in IEEE-754 may differ from any reordering at the bit level. The two L0 branches of the real-real `AXPBYPCZ` (the `γ == 0` fast-path via MFEM `add(α, x, β, y, z)` vs the `γ ≠ 0` slow-path two-call split `AXPBY(α, x, γ, z); z.Add(β, y)`) themselves use different summation orders. The L3 form is order-agnostic algebraically; bit-identical reproduction of L0 output requires matching the L0 branch's evaluation order.
- **Fusion identity with three separate `scal`+`add` passes**: `axpbypcz(α, x, β, y, γ, z) ≠ scal(α, x) + scal(β, y) + scal(γ, z)` in general at the bit level (three-pass rounds three times; fused form rounds once or twice depending on the L0 branch).

The algebraic-law set at L3 is **identical** to the L1 algebraic-law set.

## Dependencies

**Same-layer (L3)**: no other L3 operators (axpbypcz is a leaf primitive). The composition surfaces that consume `axpbypcz` at L3 are the iterate-stratum update inside `krylov-step`'s `krylov_update` (per [`krylov-step`](./krylov-step.md) §Semantics) — particularly the three-vector slice patterns (Chebyshev, BiCGStab).

**Subsumption (not dependency)**: `axpby(α, x, β, y) ≡ axpbypcz(α, x, β, y, 0, z)` and `axpy(α, x, y) ≡ axpbypcz(α, x, 1, y, 0, z)` (for any `z` — the result is independent of `z` when `γ = 0`). All three stay in the L3 dep-map as siblings.

**Cross-cutting concepts** (consumed unchanged across the chain):

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the `real ⊑ complex` typing-rule.
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — underwrites the L3-native-by-signature-shape claim.

No L4 monadic vocabulary; `axpbypcz` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpbypcz` is **CONFIRMED-NOT-NEEDED**. The adjacent L3>L2 rotation passes through the **present** L2 floor [`axpbypcz`](../L2/axpbypcz.md) (cycle-043 D5) via the firm [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md) L3>L2 theme — identity-in-form on the body, no wrapper rotation; onward to L1 [`axpbypcz`](../L1/axpbypcz.md). The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent, per **Identity-lowerings still require both L levels**.

## Variant axes

Inherited unchanged from the L1 entry at two:

1. **element-type** (`real | complex`) — at L3 collapses to one operator parameterised by element type.
2. **scalar-promotion** (sub-axis on the complex element-type) — see [`scalar-promotion`](../concepts/scalar-promotion.md). Real `(α, β, γ)` against complex `x, y, z` is promoted to complex with zero imaginary part (all-or-none across the scalar triple).

**Internal control-flow axis at L0 (not an L3 variant axis)**: the real-real specialisation's `γ == 0` branch is a transparent performance specialisation — algebraically equivalent at L1 — and not visible at L3. Inherited from L1.

The variant-axis profile at L3 matches L1 exactly.

## Status

`firm` — whole-tensor positional signature is canonical at L3; algebraic laws are the twelve that hold at L1 (inherited verbatim under the identity-in-form rotation); non-laws are catalogued explicitly; variant-axis profile is closed at two. Well-attested via L1 (cycle-003 firm; landed as the next harvester target after `axpby`) and via the L3-L2 body-identity theme's §"Applicability conditions" point 3, which explicitly names `axpbypcz` as L3-native by signature shape. This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** per **Identity-lowerings still require both L levels**. One of three sibling firmings in the BLAS-1 linear-update bundle.

## Lowers to

L3 `axpbypcz` lowers to the **present adjacent L2 floor** [`axpbypcz`](../L2/axpbypcz.md) (cycle-043 D5) as **identity-in-form on the primitive's signature shape**, via the firm [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `axpbypcz` is a leaf whole-tensor field operation, not a step body), and onward to L1 [`axpbypcz`](../L1/axpbypcz.md). The three surfaces are textually identical modulo layer-coherence vocabulary (L1 / L2 / L3 all see `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` with the same shape contract, the same twelve algebraic laws, the same four non-laws, and the same variant-axis profile). The L2 floor is the standalone fold-member BLAS-1-extended leaf — landed by the cycle-043 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive rotation in the chain is the L1>L0 [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md).

## Lifts from

No L4 entry exists for `axpbypcz` (CONFIRMED-NOT-NEEDED per cohort audit). Appears inside L4 entries as a let-binding inside `krylov-step`'s body but is not a first-class L4 calculus combinator.

## Evidence

All L0 evidence is inherited via L1 (`book/src/L1/axpbypcz.md` §Evidence). Direct citations:

- `book/src/L2/axpbypcz.md` (cycle-043 D5 firm) — the present adjacent L2 floor this L3 entry lowers into via the `axpbypcz-body-identity` theme; identity-in-form on the primitive's signature.
- `book/src/L3-L2/axpbypcz-body-identity.md` (cycle-043 firm) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation.
- `book/src/L1/axpbypcz.md` (cycle-003 firm) — the L1 form this L3 entry transitively rotates from (L3>L2 ∘ L2>L1). Body shape, semantics, twelve algebraic laws, four non-laws, variant-axis profile.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm) — names `axpbypcz` as L3-native by signature shape.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:67` (firm) — renders `axpbypcz` in the L3 body let-chain identically to L1.
- `book/src/L3/krylov-step.md` (cycle-010 firm; the precedent layer-coherence backfill) — the template this entry follows.
- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` — the cycle-010 audit identifying this cohort as HIGH CONFIDENCE backfill.
- `scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects" (cycle-003) — explicit invitation for the `axpbypcz` harvester to mirror the fused-primitive choice; inherited at L3 unchanged.
- `concepts/scalar-promotion.md` (cycle-005 firm) — the typing-rule for the real-on-complex-vector case.

L0 source ranges (inherited via L1; not consumed as new evidence at L3):

- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl.
- `palace/linalg/vector.hpp:313-316` — free-function template `AXPBYPCZ`.
- `palace/linalg/vector.cpp:745-758` — real-real `AXPBYPCZ` with `γ == 0` branch.
- `palace/linalg/vector.cpp:760-765` — complex-complex `AXPBYPCZ`.
- `palace/linalg/vector.cpp:767-772` — real-α-real-β-real-γ-on-complex-vector promotion site.

## L3 vs L1 distinction

- **L1**: whole-tensor pure-functional update `axpbypcz :: (α, x, β, y, γ, z) -> α·x + β·y + γ·z`. Mutation-lifted from the L0 source's in-place form; the fused primitive subsuming `axpby` and `axpy`.
- **L3**: whole-tensor pure-functional update `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`. The iteration-rotation layer's rendering, value-thread-isomorphic to the L1 form. The L3 entry exists for layer-coherence.

The two layers' entries share the algebraic-law set, the variant-axis profile, the referent semantics, the fused-primitive choice, and the cited L0 evidence. They differ in **layer-coherence framing** only.
