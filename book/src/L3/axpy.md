---
layer: L3
operator: axpy
firmness: firm
lowers_to:
  - book/src/L1/axpy.md (identity-in-form rotation on the primitive's signature shape; whole-tensor in / whole-tensor out at both layers; no L2 intermediate because the BLAS-1 primitives are L1 leaves not L2 compositions)
lifts_from:
  - (no L4 entry — leaf primitive, not a calculus combinator; per cycle-010 cohort audit verdict "L4 candidate CONFIRMED-NOT-NEEDED" for the BLAS-1 cohort)
variant_axes:
  - element-type (real | complex)
  - scalar-promotion (sub-axis on complex element-type)
---

# axpy

Whole-tensor vector-scalar fused update at L3: `axpy(α, x, y) = α·x + y`. The L3-native rendering of the canonical BLAS-1 linear-update primitive — the same primitive that is firm at L1 ([`axpy`](../L1/axpy.md)), surfaced here in L3 vocabulary because **each layer is internally coherent** (CLAUDE.md §Methodology invariants).

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, no element loops, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `axpy` at L3 is the whole-tensor linear-update primitive consumed by `krylov-step`'s iterate-stratum update (per [`krylov-step`](./krylov-step.md) §Semantics, line 82 of the cycle-010 firm entry: `krylov_update` at L3 composes whole-tensor primitives including `axpy`).

The L3 form is **value-thread-isomorphic to the L1 form**: each L1 BLAS-1 primitive's signature shape is whole-tensor in / whole-tensor out with no element loop exposed (the L1 entries are written against `Tensor[N]` arguments, not against per-element indexing). The L3 layer's vocabulary requirement — whole-tensor primitives, no element loops — is satisfied by L1's signature shape directly. The relationship to the lower layer is therefore the identity rotation on the primitive itself; the per-element semantics that L1 uses to describe the operator (`result[i] = α·x[i] + y[i]`) is the **referent**, not the L1 form's surface — the L1 surface is the whole-tensor signature `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`, which is already L3-native.

This L3 entry is the layer-coherence anchor for the cycle-011 BLAS-1 cohort backfill — a reader navigating L3 (which the L3 index advertises as containing "axpy ... as field operations" at `book/src/L3/index.md:13`) can find `axpy` here, in L3 vocabulary, without having to reach down to L1 to recover the signature. The backfill enacts the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). This entry is one of three sibling firmings in the cycle-011 wave-1 BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`); the cohort precedent is `book/src/L3/krylov-step.md` (cycle-010 wave-1).

A cross-cutting prose treatment lives at [`concepts/axpy`](../concepts/axpy.md) — covering BLAS background, fusions (`α = 1`, `α = -1`), and roll-up usage across slices. The concept page is the narrative; this L3 entry is the firm operator definition at L3.

## Signature

```text
axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]
```

Positional value-threading; no monadic effect (L3 has no `Solve` monad), no record-typing:

- `α : Scalar` — scalar coefficient (real or complex, matching the vector element type).
- `x : Tensor[N]` — input tensor; whole-tensor read.
- `y : Tensor[N]` — input tensor (the *prior* value); whole-tensor read.
- result `: Tensor[N]` — output tensor; whole-tensor write (fresh value, no aliasing with `x` or `y` at L3).

Shape contract (bunsen-style, named axis):

- `N` — length axis; shared across `x`, `y`, and the result.
- element type — uniform across `x`, `y`; uniform `Scalar` matches the vector element type modulo scalar promotion (see Variant axes).

`x` and `y` must share the same length axis `N` and the same element type (both real or both complex). When the vectors are complex, real `α` is promoted to complex per the [`scalar-promotion`](../concepts/scalar-promotion.md) typing rule. The L3 form inherits the `real ⊑ complex` scalar lattice from L1 — the promotion is a typing-rule property, not an operator variant; the L3 signature is `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` where `Scalar` is the lattice-resolved scalar type.

The L3 calculus has no record-typing and no `readonly` annotation; the signature is positional. The discipline that `α` flows in only (never out) is structural (the return position has only one slot, of type `Tensor[N]`, not a scalar).

## Semantics

`axpy` at L3 is a single whole-tensor linear update: `axpy(α, x, y)` produces the tensor `α·x + y`, where `α·x` is the whole-tensor scaling (a single L3-native operation, see [`scal`](./scal.md) when firm) and the `+` is the whole-tensor pointwise sum (an L3-native operation by signature shape — `Tensor[N] -> Tensor[N] -> Tensor[N]`).

The operator is **pure at L3**: the prior `y` and the new value (returned positionally) are distinct values; no destination buffer appears in the signature. The L3 form has no aliasing — both inputs and the output are conceptually distinct tensors. In-place mutation (the L0 source overwrites the destination `y`) reappears in the L1>L0 lowering chain via [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (which covers `axpy` as the β=1 specialisation of `axpby`); the L3 form is uniformly out-of-place.

**The operator is reduction-free and element-local at the referent semantics**: the per-element relation `result[i] = α·x[i] + y[i]` holds at every position independently, with no cross-element communication. This is a property of the referent, observable when the L3 form is lowered to L1 (where the per-element relation is the L1 entry's §Semantics line). At the L3 layer itself, the operator is rendered as a whole-tensor function `Tensor[N] -> Tensor[N]` with no element-index visible — the element-locality is a consequence of the operator's identity, not of its L3 surface.

**The operator carries no sequential obstruction**: `axpy` is a leaf primitive at L3 (and at L1); the L3 iteration-rotation marker (per [`sequential-obstruction`](../concepts/sequential-obstruction.md)) does not apply to it — there is no fold over `axpy`'s output to invoke. `axpy` is a *primitive* that other L3 compositions (notably `krylov-step`) invoke; the sequential obstruction lives at the consuming composition (the outer `iterate_while_L3` loop folding `krylov-step`), not at `axpy` itself.

Special algebraic cases — `α = 0` (identity in the second argument), `α = 1` (vector add), `α = -1` (vector subtract), `x = 0` (identity in the first argument) — are not separate operators at L3. They are algebraic identities, recorded in §Algebraic laws below. L0 specialisations (Palace's `AXPY(double, Vector, Vector)` branches on `α == 1.0`) are transparent performance tricks that have already been erased at L1; they do not reappear at L3.

### Iteration-rotation marker

L3 is the iteration-rotation layer, but `axpy` is a **leaf primitive** with no iteration view of its own — it is a single whole-tensor operation, not a fold over a trajectory. The iteration view applies to compositions of `axpy` (notably `krylov-step`'s iterate-stratum update; per [`krylov-step`](./krylov-step.md) Form A line `let K' = krylov_update K_aux op w`, which composes `axpy` / `axpby` / `axpbypcz`). At the leaf `axpy` itself, there is no iteration carry, no successor relation, no fold. The L3 layer-coherence reason for this entry is **vocabulary inventory**, not iteration-view content.

## Algebraic laws

Inherited verbatim from L1 (per the identity-in-form rotation). The laws below hold at L3 because they hold at L1 and the L3 form is value-thread-isomorphic to the L1 form (the laws are statements about the operator's value, not about its surface; the surface rewrite is a no-op on the value).

1. **Identity in `α`**: `axpy(0, x, y) = y` for any `x`.
2. **Identity in `x`**: `axpy(α, 0, y) = y` for any `α`, where `0` is the zero tensor of axis `N`.
3. **Left distribution over tensor addition in `y`**: `axpy(α, x, y₁ + y₂) = axpy(α, x, y₁) + y₂`. Both sides equal `α·x + y₁ + y₂`.
4. **Scalar linearity in α (additive collapse)**: `axpy(α, x, axpy(β, x, y)) = axpy(α + β, x, y)` — two successive axpy's against the same `x` collapse to one with summed scalar.
5. **Scalar absorption**: `axpy(α·β, x, y) = axpy(α, β·x, y)` — the scalar absorbs into either side.
6. **Vector linearity in x (additive expansion)**: `axpy(α, x₁ + x₂, y) = axpy(α, x₁, axpy(α, x₂, y))`. This law underwrites the consuming-composition (e.g., `krylov-step`'s iterate-stratum update inside `krylov_update`) unfolding of GMRES basis-correction sums into axpy chains.

Laws that explicitly **do not** hold (inherited from L1):

- **Commutativity in the tensor arguments**: `axpy(α, x, y) ≠ axpy(α, y, x)`. The second argument `x` enters scaled by `α`; the third argument `y` does not. Swapping them changes the value.
- **Associativity as a binary algebra**: `axpy` is ternary; associativity is not well-typed.
- **Floating-point associativity in the summation**: `α·x + y` in IEEE-754 may differ at the bit level from any reordering when the magnitudes of `α·x` and `y` differ enough to lose precision. The L3 form is order-agnostic algebraically; bit-identical reproduction of L0 output requires matching the L0 evaluation order (pinned by MFEM's kernel). Inherited from L1; recorded here, not erased.

The algebraic-law set at L3 is **identical** to the L1 algebraic-law set. This is structural: the rotation is identity-in-form on the primitive's signature; laws about the primitive's value are unchanged across the rotation. Stating the laws at L3 is not a duplication-explosion concern under the methodology — it is the layer-coherence invariant; an L3 reader can verify the laws against the L3 signature without reaching down to L1.

## Dependencies

**Same-layer (L3)**: no other L3 operators (axpy is a leaf primitive). The composition surfaces that consume `axpy` at L3 are the iterate-stratum update inside `krylov-step`'s `krylov_update` (per [`krylov-step`](./krylov-step.md) §Semantics).

**Cross-cutting concepts** (consumed unchanged across the chain):

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the `real ⊑ complex` typing-rule for scalar promotion on the complex element-type. The L3 form inherits the rule from L1 verbatim; no L3-specific semantics.
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — the methodology concept underwriting the L3-native-by-signature-shape claim for the BLAS-1 primitives.
- [`axpy`](../concepts/axpy.md) — the cross-cutting prose narrative (BLAS background, common fusions, roll-up usage). The L3 entry here is the firm operator definition; the concept page is the narrative.

**Strawman reference**: `book/src/design/l4_calculus.md` §3.7's conventions are not directly invoked here because `axpy` is a leaf primitive, not a calculus combinator. The L3 signature is a plain Haskell-style `::` arrow form.

No L4 monadic vocabulary appears in the L3 signature (no `Solve`, no `modify`, no `do`-block) — `axpy` is not a calculus combinator at L4. The cohort audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`) verdict for the BLAS-1 cohort at L4 is **CONFIRMED-NOT-NEEDED**: leaf primitives don't get L4 rows. The L3>L1 rotation is direct; no L2 intermediate is required because the BLAS-1 primitives are L1 leaves not L2 compositions (per the L2 entry's §Dependencies — the L2 layer lists `axpy` as an L1 vocabulary item it depends on, not as a standalone L2 row).

## Variant axes

Inherited unchanged from the L1 entry at two:

1. **element-type** (`real | complex`) — the L1 entry distinguishes real-vector and complex-vector overloads; at L3 these collapse to one operator parameterised by element type. Semantics are identical across element types; the per-element kernel referent is `α·x[i] + y[i]` in the appropriate field.
2. **scalar-promotion** (sub-axis on the complex element-type) — see [`scalar-promotion`](../concepts/scalar-promotion.md). Real `α` against complex `x, y` is promoted to complex with zero imaginary part. The promotion is a typing-rule property, not an operator variant.

The variant-axis profile at L3 matches L1 exactly. No new axes introduced by the L3 rendering; no axes merged or split.

## Status

`firm` — whole-tensor positional signature is canonical at L3; algebraic laws are the six that hold at L1 (inherited verbatim under the identity-in-form rotation); non-laws are catalogued explicitly; variant-axis profile is closed at two. The pattern is well-attested via L1 (cycle-002 firm) and via the L3-L2 body-identity theme's §"Applicability conditions" point 3 (`book/src/L3-L2/krylov-step-body-identity.md:97`), which explicitly names `axpy` as L3-native by signature shape. This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** — the L3 form was previously only referenced from `krylov-step`'s body let-chain at L3; it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). One of three sibling firmings in the BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`).

## Lowers to

L3 `axpy` lowers to L1 [`axpy`](../L1/axpy.md) via the **identity-in-form rotation on the primitive's signature shape**. The two surfaces are textually identical modulo whatever layer-coherence vocabulary differences exist (e.g., L1 uses `Tensor[N]` axis naming with bunsen-style shape contracts; L3 uses the same axis naming). The rotation does not pass through L2 because the BLAS-1 primitives are L1 leaves, not L2 compositions — the L2 layer references `axpy` by its L1 name (per `book/src/L2/krylov-step.md:96`). The cycle-010 cohort audit's verdict for the L2 candidate on `axpy` was **CONFIRMED-NOT-NEEDED-WITH-CAVEAT** (priority #17 may eventually compel L2 entries; deferred until L2 cohort grows).

A thin L3>L1 identity-in-form theme could be authored to ratify the rotation explicitly (analogous to `book/src/L3-L2/krylov-step-body-identity.md` for the krylov-step body); whether to create a `book/src/L3-L1/` directory is a structural-naming question deferred per OQ `l3-l1-directory-naming-structure-policy` (raised by the cycle-010 cohort audit). The current dispatch documents the rotation in-line at the L3 entry's "Lowers to" section, consistent with the cycle-010 `book/src/L3/krylov-step.md` precedent's treatment of its L3>L2 lowering.

## Lifts from

No L4 entry exists for `axpy` (the cohort audit verdict is **CONFIRMED-NOT-NEEDED** for the BLAS-1 cohort at L4 — leaf primitives don't get L4 rows). `axpy` appears inside L4 entries as a let-binding inside `krylov-step`'s body (per `book/src/L4/krylov-step.md` §Semantics), but is not a first-class L4 calculus combinator and carries no monadic effect, no state-stratification typing, no novel calculus content at L4.

## Evidence

All L0 evidence is inherited via L1 (`book/src/L1/axpy.md` §Evidence). Direct citations relevant to this L3 entry:

- `book/src/L1/axpy.md` (cycle-002 firm) — the L1 form this L3 entry rotates from. Body shape, semantics, six algebraic laws, two non-laws, variant-axis profile.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm) — explicitly names `axpy` as one of seven L1 primitives that is "L3-native because its signature has no per-element loop visible". The structural justification for the identity-in-form rotation.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:67` (firm) — renders `axpy` in the L3 body let-chain identically to L1. The empirical evidence that the L3 form of `axpy` already exists in the artifact (as the RHS of the upstream theme's L3 form).
- `book/src/L3/index.md:13` — L3 vocabulary inventory naming `axpy` as a field operation. The advertised L3 vocabulary that this entry backfills.
- `book/src/L3/krylov-step.md` (cycle-010 firm; the precedent layer-coherence backfill) — the template structure this entry follows.
- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` — the cycle-010 audit identifying this cohort as HIGH CONFIDENCE backfill (lines 47-51, 100-132).
- `concepts/scalar-promotion.md` (cycle-005 firm; cycle-006 retroactive-thinned the L1 entry to point here) — the typing-rule for the real-on-complex-vector case at L3 / L1.

L0 source ranges (inherited via L1; not consumed as new evidence at L3):

- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` and `Add`/`Subtract` aliases.
- `palace/linalg/vector.hpp:305-307` — free-function template `AXPY`.
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition.
- `palace/linalg/vector.cpp:702-712` — free-function `AXPY(double, Vector, Vector)` with `α == 1.0` fast-path.
- `palace/linalg/vector.cpp:715-718` — real-α-on-complex-vector promotion site.

## L3 vs L1 distinction

- **L1**: whole-tensor pure-functional update `axpy :: (α, x, y) -> α·x + y`. Mutation-lifted from the L0 source's in-place form; aliasing-free; reduction-free; element-local at the referent semantics. The closest pure-functional layer to the source.
- **L3**: whole-tensor pure-functional update `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`. The iteration-rotation layer's rendering, value-thread-isomorphic to the L1 form because the L1 signature is already whole-tensor / no-element-loop. The L3 entry exists for layer-coherence — a reader at L3 finds `axpy` defined in L3 vocabulary without having to reach down to L1.

The two layers' entries share the algebraic-law set, the variant-axis profile, the referent semantics, and the cited L0 evidence. They differ in **layer-coherence framing**: L1 frames the operator as the mutation-rotation lift from L0; L3 frames the operator as a whole-tensor field operation at the iteration-rotation layer. The body of the operator is the identity rotation across this edge.
