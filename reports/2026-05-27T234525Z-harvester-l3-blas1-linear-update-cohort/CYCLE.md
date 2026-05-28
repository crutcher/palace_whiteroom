---
agent: harvester
invoked_at: 2026-05-27T234525Z
scope: L3 operators (bundle): axpy, axpby, axpbypcz — the BLAS-1 linear-update cohort
status: integrated
integrated_at: 2026-05-28T013333Z
integration_commit: 8bb16b7
integration_notes: cycle-011 wave-1 pass 2; first cohort-bundle harvester landing of cycle-011; 3 firm L3 entries via subsumption chain axpy ≺ axpby ≺ axpbypcz; 5 proposed-changes applied cleanly; 0 safety-net gate hits; 1 status update on cycle-010 l3-l1-directory-naming-structure-policy (in-line identity-rotation count → 4)
inputs:
  - book/src/L3/krylov-step.md (cycle-010 wave-1 firm precedent — identity-lowering layer-coherence backfill template)
  - book/src/L1/axpy.md, book/src/L1/axpby.md, book/src/L1/axpbypcz.md (firm L1 entries; algebraic laws inherited)
  - book/src/L2/krylov-step.md (cycle-005 firm L2 entry — names the three BLAS-1 primitives as L1 vocabulary used inside the L2 step body)
  - book/src/L4/krylov-step.md (cycle-006 firm L4 entry — body cites the three primitives in the L4 let-chain)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md §"L3 form (RHS)" lines 55-89 — renders the three primitives in the L3 body let-chain identically to L1
  - book/src/L3-L2/krylov-step-body-identity.md §"Applicability conditions" point 3 (line 97) — explicitly names the seven L1 primitives as L3-native by signature shape
  - book/src/concepts/scalar-promotion.md (cycle-005 firm — typing-rule concept; cycle-006 retroactive-thinning on L1 entries cross-references this page)
  - book/src/L3/index.md lines 11-14 — L3 vocabulary inventory advertising "axpy ... as field operations"
  - reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md — cycle-010 wave-1 audit identifying this cohort as HIGH CONFIDENCE backfill
  - CLAUDE.md §Methodology invariants bullet "Identity-lowerings still require both L levels" (codified cycle-009 meta-phase)
---

# CYCLE: Formalize the BLAS-1 linear-update cohort (axpy + axpby + axpbypcz) at L3

## Summary

Authors three firm L3 entries — `axpy`, `axpby`, `axpbypcz` — as the layer-coherence backfill for the BLAS-1 linear-update cohort, following the cycle-010 wave-1 `book/src/L3/krylov-step.md` template. Each entry's signature, semantics, and algebraic laws are stated in L3 vocabulary (whole-tensor primitives; positional value-threading; no element loop exposed). Each operator's L3 form is **value-thread-isomorphic** to its L1 form — the rotation L3→L1 is identity-in-form on the primitive itself, because each L1 primitive's signature shape is L3-native by construction (whole-tensor inputs, whole-tensor output, no element loop). The entries exist for the methodology-invariant reason: **each layer is internally coherent**; a reader navigating L3 must find these primitives defined in L3 vocabulary without having to reach down to L1.

Algebraic laws are inherited verbatim from the firm L1 entries (linear-combination identities, scalar absorption, subsumption chain `axpy ≺ axpby ≺ axpbypcz`). The L3 form is uniformly out-of-place (whole-tensor functional update); in-place specialisation reappears below L3 via the L1>L0 mutation-rotation chain. Variant-axis profile is closed at two for each operator (element-type, scalar-promotion sub-axis), identical to L1.

This dispatch closes the BLAS-1 cohort portion of OQ `l3-backfill-apply-linop-and-blas1-cohort` (HIGH CONFIDENCE) raised by the cycle-010 cross-layer-cross-cutter audit. The cohort dispatch leaves three more L3 backfills (`dot`, `nrm2`, `scal`) to sibling dispatches in the same cycle.

## Proposed changes

```edit:book/src/L3/axpy.md
[NEW FILE — full content in §"Operator content — axpy" below]
```

```edit:book/src/L3/axpby.md
[NEW FILE — full content in §"Operator content — axpby" below]
```

```edit:book/src/L3/axpbypcz.md
[NEW FILE — full content in §"Operator content — axpbypcz" below]
```

```edit:book/src/L3/index.md
[Append three rows to the operator dep-map table, after `krylov-step`; rough-in row not needed (these are first-time firm landings of L3 entries for these operators, per the cohort audit verdict). Working Notes paragraph "Cohort growth candidates" is partially answered by this dispatch — three of the six BLAS-1 candidates now firm at L3.]

The three appended rows (after the existing `krylov-step` row, with whatever ordering the sibling dispatches resolve to):

| [`axpy`](./axpy.md) | `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, y) -> α·x + y`) | L1 [`axpy`](../L1/axpy.md) for the L1-form anchor; concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). | L1 [`axpy`](../L1/axpy.md) via identity-in-form rotation on the primitive's signature shape (whole-tensor in / whole-tensor out at both layers); no element loop exposed. | `firm` (harvested cycle-011T234525Z; identity-lowering backfill per CLAUDE.md §Methodology invariants; closes cohort portion of OQ `l3-backfill-apply-linop-and-blas1-cohort` HIGH CONFIDENCE) |
| [`axpby`](./axpby.md) | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y) -> α·x + β·y`) | L1 [`axpby`](../L1/axpby.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpy`](./axpy.md) at L3 (β=1) — same subsumption-as-identity discipline as L1. | L1 [`axpby`](../L1/axpby.md) via identity-in-form rotation on the primitive's signature shape. | `firm` (harvested cycle-011T234525Z; identity-lowering backfill) |
| [`axpbypcz`](./axpbypcz.md) | `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y, γ, z) -> α·x + β·y + γ·z`) | L1 [`axpbypcz`](../L1/axpbypcz.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpby`](./axpby.md) at L3 (γ=0) and [`axpy`](./axpy.md) (β=1, γ=0) — same subsumption-as-identity discipline as L1. | L1 [`axpbypcz`](../L1/axpbypcz.md) via identity-in-form rotation on the primitive's signature shape. | `firm` (harvested cycle-011T234525Z; identity-lowering backfill) |

Working Notes update — append bullet:

- **Cycle-011 wave-1 cohort growth (BLAS-1 linear-update bundle)**: three of the six BLAS-1 cohort candidates identified by the cycle-010 cross-layer-cross-cutter audit landed firm: `axpy`, `axpby`, `axpbypcz` (the linear-update family, subsumption chain `axpy ≺ axpby ≺ axpbypcz`). Each L3 entry is the layer-coherence backfill per **Identity-lowerings still require both L levels**; the L3 form is value-thread-isomorphic to the L1 form because each primitive's L1 signature is already whole-tensor / no-element-loop. Three more L3 cohort candidates (`dot`, `nrm2`, `scal`) tracked by sibling wave-1 dispatches (#3, #4) and OQ `l3-backfill-apply-linop-and-blas1-cohort`.
```

```edit:book/src/SUMMARY.md
[Append three chapter entries under the L3 Part, after `[krylov-step](./L3/krylov-step.md)`. Natural ordering: axpy, axpby, axpbypcz.]

# L3 — Global Tensor-Field Operations
- [Overview](./L3/index.md)
- [krylov-step](./L3/krylov-step.md)
- [axpy](./L3/axpy.md)
- [axpby](./L3/axpby.md)
- [axpbypcz](./L3/axpbypcz.md)

(integrator-finalize: order alongside sibling dispatches #1 (apply_linop), #3 (dot, nrm2), #4 (scal) per natural cohort ordering — leaf-primitive cohort then composite cohort. Suggested final ordering under the L3 Part: `krylov-step`, `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`. The integrator may use a different ordering; the entries themselves do not depend on order.)
```

## Operator content — axpy

The exact text written into `book/src/L3/axpy.md`:

```markdown
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
```

## Operator content — axpby

The exact text written into `book/src/L3/axpby.md`:

```markdown
---
layer: L3
operator: axpby
firmness: firm
lowers_to:
  - book/src/L1/axpby.md (identity-in-form rotation on the primitive's signature shape; whole-tensor in / whole-tensor out at both layers; no L2 intermediate because the BLAS-1 primitives are L1 leaves not L2 compositions)
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

No L4 monadic vocabulary; `axpby` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpby` is **CONFIRMED-NOT-NEEDED** (leaf primitives don't get L4 rows). The L3>L1 rotation is direct; no L2 intermediate is required because `axpby` is an L1 leaf, not an L2 composition (per `book/src/L2/krylov-step.md:96` — the L2 layer references `axpby` by its L1 name).

## Variant axes

Inherited unchanged from the L1 entry at two:

1. **element-type** (`real | complex`) — the L1 entry distinguishes real-vector and complex-vector overloads; at L3 these collapse to one operator parameterised by element type. Semantics are identical across element types.
2. **scalar-promotion** (sub-axis on the complex element-type) — see [`scalar-promotion`](../concepts/scalar-promotion.md). Real `(α, β)` against complex `x, y` is promoted to complex with zero imaginary part (all-or-none across the scalar pair). Typing-rule property, not an operator variant.

The variant-axis profile at L3 matches L1 exactly. No new axes introduced; no axes merged or split.

## Status

`firm` — whole-tensor positional signature is canonical at L3; algebraic laws are the nine that hold at L1 (inherited verbatim under the identity-in-form rotation); non-laws are catalogued explicitly; variant-axis profile is closed at two. The pattern is well-attested via L1 (cycle-003 firm) and via the L3-L2 body-identity theme's §"Applicability conditions" point 3, which explicitly names `axpby` as L3-native by signature shape. This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** per **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase). One of three sibling firmings in the BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`).

## Lowers to

L3 `axpby` lowers to L1 [`axpby`](../L1/axpby.md) via the **identity-in-form rotation on the primitive's signature shape**. The two surfaces are textually identical modulo layer-coherence vocabulary. The rotation does not pass through L2 because `axpby` is an L1 leaf, not an L2 composition.

A thin L3>L1 identity-in-form theme could be authored to ratify the rotation explicitly; whether to create a `book/src/L3-L1/` directory is a structural-naming question deferred per OQ `l3-l1-directory-naming-structure-policy` (raised by the cycle-010 cohort audit). The current dispatch documents the rotation in-line at the L3 entry's "Lowers to" section, consistent with the cycle-010 `book/src/L3/krylov-step.md` precedent.

## Lifts from

No L4 entry exists for `axpby` (the cohort audit verdict is **CONFIRMED-NOT-NEEDED** for the BLAS-1 cohort at L4). `axpby` appears inside L4 entries as a let-binding inside `krylov-step`'s body but is not a first-class L4 calculus combinator.

## Evidence

All L0 evidence is inherited via L1 (`book/src/L1/axpby.md` §Evidence). Direct citations relevant to this L3 entry:

- `book/src/L1/axpby.md` (cycle-003 firm) — the L1 form this L3 entry rotates from. Body shape, semantics, nine algebraic laws, four non-laws, variant-axis profile.
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
```

## Operator content — axpbypcz

The exact text written into `book/src/L3/axpbypcz.md`:

```markdown
---
layer: L3
operator: axpbypcz
firmness: firm
lowers_to:
  - book/src/L1/axpbypcz.md (identity-in-form rotation on the primitive's signature shape; whole-tensor in / whole-tensor out at both layers; no L2 intermediate because the BLAS-1 primitives are L1 leaves not L2 compositions)
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

No L4 monadic vocabulary; `axpbypcz` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpbypcz` is **CONFIRMED-NOT-NEEDED**. The L3>L1 rotation is direct; no L2 intermediate is required.

## Variant axes

Inherited unchanged from the L1 entry at two:

1. **element-type** (`real | complex`) — at L3 collapses to one operator parameterised by element type.
2. **scalar-promotion** (sub-axis on the complex element-type) — see [`scalar-promotion`](../concepts/scalar-promotion.md). Real `(α, β, γ)` against complex `x, y, z` is promoted to complex with zero imaginary part (all-or-none across the scalar triple).

**Internal control-flow axis at L0 (not an L3 variant axis)**: the real-real specialisation's `γ == 0` branch is a transparent performance specialisation — algebraically equivalent at L1 — and not visible at L3. Inherited from L1.

The variant-axis profile at L3 matches L1 exactly.

## Status

`firm` — whole-tensor positional signature is canonical at L3; algebraic laws are the twelve that hold at L1 (inherited verbatim under the identity-in-form rotation); non-laws are catalogued explicitly; variant-axis profile is closed at two. Well-attested via L1 (cycle-003 firm; landed as the next harvester target after `axpby`) and via the L3-L2 body-identity theme's §"Applicability conditions" point 3, which explicitly names `axpbypcz` as L3-native by signature shape. This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** per **Identity-lowerings still require both L levels**. One of three sibling firmings in the BLAS-1 linear-update bundle.

## Lowers to

L3 `axpbypcz` lowers to L1 [`axpbypcz`](../L1/axpbypcz.md) via the **identity-in-form rotation on the primitive's signature shape**. The two surfaces are textually identical modulo layer-coherence vocabulary. The rotation does not pass through L2 because `axpbypcz` is an L1 leaf, not an L2 composition.

A thin L3>L1 identity-in-form theme could be authored to ratify the rotation explicitly; whether to create a `book/src/L3-L1/` directory is deferred per OQ `l3-l1-directory-naming-structure-policy`. The current dispatch documents the rotation in-line at the L3 entry's "Lowers to" section.

## Lifts from

No L4 entry exists for `axpbypcz` (CONFIRMED-NOT-NEEDED per cohort audit). Appears inside L4 entries as a let-binding inside `krylov-step`'s body but is not a first-class L4 calculus combinator.

## Evidence

All L0 evidence is inherited via L1 (`book/src/L1/axpbypcz.md` §Evidence). Direct citations:

- `book/src/L1/axpbypcz.md` (cycle-003 firm) — the L1 form this L3 entry rotates from. Body shape, semantics, twelve algebraic laws, four non-laws, variant-axis profile.
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
```

## Supporting evidence

This bundled dispatch's recommendations rest on the following load-bearing evidence:

1. **Cycle-010 wave-1 precedent** (`book/src/L3/krylov-step.md`, firm cycle-010T215300Z) — the first cycle-010 enactment of the methodology invariant **Identity-lowerings still require both L levels**. The template structure (frontmatter; Context; Signature; Semantics; iteration-rotation marker; Algebraic laws; Dependencies; Variant axes; Status; Lowers to; Lifts from; Evidence; L3 vs L1 distinction) is followed verbatim in each of the three new entries below.

2. **Cycle-010 cross-layer-cross-cutter audit** (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`, integrated 2026-05-27T230802Z) — identifies the BLAS-1 cohort (including `axpy`, `axpby`, `axpbypcz`) as HIGH CONFIDENCE backfill, with the structural rationale "L3-native by signature shape — each is a whole-tensor / reduction operation with no element loop exposed" (line 49). The audit's suggested bundling pattern (lines 124-127) explicitly suggests grouping by algebraic shape: "(a) axpy + axpby + axpbypcz (the linear-update family; shared subsumption laws)" — exactly the bundling this dispatch enacts.

3. **L3-L2 body-identity theme** (`book/src/L3-L2/krylov-step-body-identity.md`, firm cycle-009) §"Applicability conditions" point 3 (line 97) — explicit statement that the seven L1 primitives "operate on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)." The structural justification for the identity-in-form rotation is published evidence and need not be re-derived by this dispatch.

4. **L4-L3 typed-wrapper-dissolution theme** (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`, firm cycle-008) §"L3 form (RHS)" lines 55-89 — renders `axpy` / `axpby` / `axpbypcz` in the L3 body let-chain identically to L1. The L3 form of each operator is already published (as the RHS of this theme); this dispatch lifts each operator into its own L3 entry per the layer-coherence invariant.

5. **CLAUDE.md §Methodology invariants** — the **Identity-lowerings still require both L levels** bullet (codified cycle-009 meta-phase, supersedes cycle-006 "no L3 row needed for krylov-step"). The cycle-010 wave-1 backfill on `krylov-step` is the first enactment; the cycle-011 wave-1 BLAS-1 cohort backfill (this dispatch + siblings #1, #3, #4) is the second cohort-level enactment.

6. **L1 firm entries** (`book/src/L1/axpy.md`, `book/src/L1/axpby.md`, `book/src/L1/axpbypcz.md`, all firm post-cycle-003 with cycle-006 retroactive scalar-promotion thinning) — the algebraic laws and variant-axis profiles inherited verbatim in each L3 entry. No new algebraic content is introduced at L3; the entries are layer-coherence backfills.

7. **`scaffolding/decisions/axpby-as-primitive.md`** (cycle-003) — the fused-primitive choice for `axpby` (and by §"Knock-on effects" §, for `axpbypcz`). Inherited at L3 unchanged.

8. **`concepts/scalar-promotion.md`** (cycle-005 firm; cycle-006 retroactive-thinned the L1 entries) — the cross-cutting typing-rule concept. Each L3 entry cross-references this page (per the cycle-005 thinning pattern).

## Open questions / caveats

1. **L3>L1 lowering theme directory naming** — none of the three new entries author a sibling `L3-L1/<operator>-identity-rotation.md` theme; instead, each entry documents the identity-in-form rotation in-line at its "Lowers to" section. This matches the cycle-010 wave-1 `book/src/L3/krylov-step.md` precedent (which also handled its L3>L2 lowering in-line via the existing `L3-L2/krylov-step-body-identity.md`; no L3>L2 sibling theme was created by the cycle-010 backfill — the entry simply pointed at the existing firm theme). The cycle-010 cohort audit raised OQ `l3-l1-directory-naming-structure-policy` (`scaffolding/open-questions.md` per the integrator-per-report pass) to track whether `book/src/L3-L1/` should be created for these identity rotations; this dispatch is consistent with deferring that decision and does not enact a directory creation. **Recommendation to cycle-011 finalize/cycle-012 planner**: if `book/src/L3-L1/` is created (either retroactively for `krylov-step`'s L3-L1 rotation if such a thing exists, or proactively for the BLAS-1 cohort), each of the three new L3 entries' "Lowers to" sections should be updated to point at the appropriate sibling theme. The current in-line documentation is the layer-coherence-preserving alternative.

2. **The L2 candidate for the BLAS-1 cohort remains contested** (per the cycle-010 audit's Open Question 2; verdict: CONFIRMED-NOT-NEEDED-WITH-CAVEAT). The cycle-010 audit deferred the L2 question to the cycle-010 planner. **This dispatch does NOT author L2 entries** for `axpy` / `axpby` / `axpbypcz` — staying consistent with the existing L2 layer's role ("compositions of L1 primitives, not naming them anew" per `book/src/L2/index.md`). If priority #17's "lower-layer shared vocabulary priority" eventually compels L2 entries for these primitives, that would be a separate dispatch (likely a same-layer-cross-cutter audit followed by a harvester wave).

3. **The cycle-010 cohort audit's broader L3 vocabulary inventory gap** (the audit's "Latent observation" §, lines 67-69) is partially addressed by this dispatch (three of the six BLAS-1 cohort candidates). Sibling wave-1 dispatches (#1 `apply_linop`, #3 `dot` + `nrm2`, #4 `scal`) cover the remaining three. After all four wave-1 sibling dispatches integrate, the L3 vocabulary inventory should match the L3 index's advertised contents (matvec/axpy/dot/nrm2 as field operations), closing the latent-observation gap.

4. **No L1 retroactive-thinning is proposed in this dispatch.** The cycle-006 pattern was to retroactively thin L1 entries to cross-reference `concepts/scalar-promotion.md` rather than restate the typing rule verbatim. The cycle-011 BLAS-1 L3 entries do *not* propose any further thinning of the L1 entries; they simply cross-reference the same concept page. This is consistent with the cycle-010 `book/src/L3/krylov-step.md` precedent (which did not retroactively thin the L4 / L2 / L1 entries it built upon).

5. **No `tensor-field-lift` concept page authoring is proposed.** Each L3 entry cross-references `concepts/tensor-field-lift.md` (existing per `book/src/concepts/tensor-field-lift.md`). The cross-reference is a citation, not an authoring; no concept-page edit is proposed by this dispatch.

6. **The `scal` cohort sibling** (`book/src/L3/scal.md`, dispatched in sibling #4) is the natural completion of this linear-update family at L3 — the algebraic-law section of `axpby` at L3 references `scal` as the natural restatement of the Identity-in-α and Identity-in-β laws once `scal` lands. If sibling #4 lands `scal` at L3, the algebraic-law cross-references in `book/src/L3/axpby.md` and `book/src/L3/axpbypcz.md` should be valid; if sibling #4 does not land `scal`, the cross-references remain as forward-looking restatements (consistent with the L1 axpby's similar treatment per `book/src/L1/axpby.md` Law 2-3).

7. **Variant-axis count discipline** — each L3 entry's variant-axis profile is two (element-type + scalar-promotion), matching the L1 entry exactly. No new axes are introduced by the L3 rendering. The L3 layer's own iteration-rotation variant axes (e.g., the six on `krylov-step`) do NOT apply to leaf primitives — `axpy`/`axpby`/`axpbypcz` are unconditionally pure, element-local, reduction-free across all variants, with no iteration view of their own.

## File paths (absolute) for the integrator

Three new files to create:
- `/home/crutcher/git/palace_whiteroom/book/src/L3/axpy.md`
- `/home/crutcher/git/palace_whiteroom/book/src/L3/axpby.md`
- `/home/crutcher/git/palace_whiteroom/book/src/L3/axpbypcz.md`

Two files to edit:
- `/home/crutcher/git/palace_whiteroom/book/src/L3/index.md` — append three dep-map rows + one Working Notes bullet
- `/home/crutcher/git/palace_whiteroom/book/src/SUMMARY.md` — append three L3 chapter entries

This report file (already written):
- `/home/crutcher/git/palace_whiteroom/reports/2026-05-27T234525Z-harvester-l3-blas1-linear-update-cohort/CYCLE.md`
