---
agent: abstractor
invoked_at: 2026-06-01T063231Z
scope: L2>L1 + L3>L2 thin-identity theme sketches — the elementwise pair (reciprocal + elementwise_product), four themes
status: pending
inputs:
  - reports/2026-06-01T063231Z-cycle-042-harvester-L2-reciprocal/CYCLE.md (D2; proposed book/src/L2/reciprocal.md — source of truth for the L2 reciprocal form)
  - reports/2026-06-01T063231Z-cycle-042-harvester-L2-elementwise-product/CYCLE.md (D3; proposed book/src/L2/elementwise_product.md — source of truth for the L2 elementwise_product form)
  - book/src/L1/reciprocal.md (firm) + book/src/L1/elementwise_product.md (firm cycle-019/032/036) — the L1 leaves
  - book/src/L3/reciprocal.md (firm cycle-038) + book/src/L3/elementwise_product.md (firm cycle-038) — the L3 leaves
  - book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md (firm) — the shared substantive L1>L0 rotation (sub-pattern A reciprocal, sub-pattern B elementwise_product)
  - book/src/L2-L1/dot-leaf-identity.md (firm cycle-041) — L2>L1 thin-identity leaf template
  - book/src/L3-L2/dot-body-identity.md + book/src/L3-L2/scal-body-identity.md (firm cycle-041) — L3>L2 thin-identity body templates (scal = the fold-free "no wrapper to rotate" precedent)
  - book/src/L2-L1/index.md + book/src/L3-L2/index.md (the two lowering-Part dep-maps)
  - L0 anchors (load-bearing, self-verified on-disk via tools/citecheck/citecheck.py --anchor, 2026-06-01, all [ok]):
    palace/linalg/vector.cpp:248-261 (ComplexVector::Reciprocal), :257-259 (XR/XI complex kernel);
    palace/linalg/vector.hpp:20 (using Vector = mfem::Vector);
    palace/linalg/operator.cpp:478-487 (BaseDiagonalOperator<Operator>::Mult), :486 (Y[i]=D[i]*X[i]), :545-568 (MultHermitianTranspose)
integrated_at: 2026-06-01T081245Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-042 batch integration (foundation-first L2-floor build); applied clean; see reports/2026-06-01T081245Z-integrator-finalize-cycle-42/CYCLE.md + cycle-042 STAGING row."
---

# CYCLE: L2>L1 + L3>L2 thin-identity theme sketches — the elementwise pair (reciprocal + elementwise_product)

## Summary

This dispatch (cycle-042 D10, wave-2) authors the **four thin-identity lowering themes** for the
two diagonal-preconditioner-apply elementwise leaves — `reciprocal` (the elementwise multiplicative
inverse `y[i] = 1/x[i]`) and `elementwise_product` (the Hadamard binary product `result = a ⊙ b`).
Each leaf gets its two adjacent-edge identity themes:

- **`reciprocal-leaf-identity`** (L2>L1) + **`reciprocal-body-identity`** (L3>L2)
- **`elementwise-product-leaf-identity`** (L2>L1) + **`elementwise_product-body-identity`** (L3>L2)

All four are **pure pointwise identity-in-form** edges: the L2 floor forms (D2 / D3, co-landing this
cycle) are value-thread-isomorphic to the firm L1 leaves on signature + laws + variant axes, and the
firm L3 leaves are L3-native by signature shape (no per-element loop exposed at any layer). The
narration is **forward, high→low** (the L_{n+1} form dissolves into the L_n form). These complete the
adjacent edges that the firm L3 entries' §"Lowers to" sections had to *skip* (both
`book/src/L3/reciprocal.md:131` and `book/src/L3/elementwise_product.md:149` currently record a
direct L3>L1 identity-in-form rotation "no interposed L2 entry, no L3-L2/L3-L1 theme file" via the
non-adjacent in-line convention; with the D2/D3 L2 floors now present, these themes supply the
adjacent-edge L3>L2 rotation) — exactly the situation `dot-body-identity` / `scal-body-identity`
addressed in cycle-041.

**The load-bearing structural distinction from the cycle-041 BLAS-1-floor themes:** `reciprocal` and
`elementwise_product` are **fold-parent-FREE** (the D2/D3 reports establish this exhaustively). So
unlike `dot-leaf-identity` (which *defers* all its L2-layer fusion content to the fold-parent
`inner-product-fold-specialization`) and `scal-fold-specialization` (the arity-1 row of
`linear-combination-fold-specialization`), the elementwise-pair themes have **no fold-parent to
defer fusion to** — there is simply no multi-operation kernel fusion on these leaves (the L0
`forall_switch` per-element pass is already the unfolded single-pass form). The closest precedent is
therefore `scal-body-identity`'s **"no wrapper to rotate, the body IS the identity"** framing, with
the added observation that there is also **no fold-parent to defer to**. Consequently all four
themes are **design-final on the leaf-vs-fold fork** (`dot-l2-leaf-floor-vs-fold-only-design`,
batch-12 meta-phase): the fork is about how the BLAS-1 *fold-member* leaves relate to their fold
parents; these fold-free elementwise leaves can only ever be standalone same-named floors, so neither
the (a) fold-only nor the (b) same-named-floor reading re-anchors them. No new operators proposed
(all four endpoints — L1, L2, L3 — are existing/co-landing vocabulary). Justification kind:
`structural` (dominant) + `empirical-match` (secondary), matching the four cycle-041 sibling themes.

## Proposed changes

### Theme 1 — `reciprocal-leaf-identity` (L2>L1)

```new:book/src/L2-L1/reciprocal-leaf-identity.md
# reciprocal-leaf-identity

The L2>L1 lowering theme for the elementwise multiplicative-inverse leaf `reciprocal`. The rewrite is
**identity-in-form on the leaf**: the L2 [`reciprocal`](../L2/reciprocal.md) floor lowers to the L1
[`reciprocal`](../L1/reciprocal.md) primitive with the same signature `Tensor[N] -> Tensor[N]`, the
same elementwise `y[i] = 1/x[i]` semantics, the same eight algebraic laws, and the same single
variant axis (element-type) — value-thread-isomorphic on the primitive. Unlike the cycle-041
[`dot-leaf-identity`](./dot-leaf-identity.md) (which defers its L2-layer fusion content to a
fold-parent), `reciprocal` is a **standalone elementwise leaf with NO fold-parent**, so there is no
fusion to defer: the only intra-element factoring (the complex `s = 1/|z|²` intermediate) is a
transparent performance trick already recorded at L1/L2/L3, not a multi-operation kernel fusion. This
theme records the identity edge; it is the L2>L1 analogue of the L3>L2
[`reciprocal-body-identity`](../L3-L2/reciprocal-body-identity.md) (the other thin edge of the same
leaf), and a sibling shape to [`scal-fold-specialization`](./scal-fold-specialization.md) and
[`nrm2-fold-specialization`](./nrm2-fold-specialization.md) — except those defer to a fold-parent or
consume a fold, while this leaf is fold-free.

## Slug

`reciprocal-leaf-identity`

## Context

`reciprocal` at L2 is the **floor** entry (`book/src/L2/reciprocal.md`, harvested cycle-042 D2): the
standalone elementwise multiplicative-inverse leaf, rendered as its own same-named L2 chapter so the
firm L3 [`reciprocal`](../L3/reciprocal.md) (cycle-038) leaf rests on an adjacent same-named L2 parent
(per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**) rather than
skipping a layer to L1. This theme is the L2>L1 edge of that floor.

The edge is the **identity-in-form** case: the L2 `reciprocal` floor and the L1 `reciprocal` leaf are
value-thread-isomorphic on the primitive. This is the L2>L1 analogue of the L3>L2
[`reciprocal-body-identity`](../L3-L2/reciprocal-body-identity.md) theme (the other thin edge of the
same leaf).

**Why this edge is identity AND fold-free (the distinction from `dot-leaf-identity`).** The cycle-041
`dot-leaf-identity` is identity-in-form *because* all its L2-layer fusion content (de-fusing Palace's
three fused reduction shapes) is carried by the fold-parent `inner-product-fold-specialization` — the
leaf's own edge is left a no-op with a single deferring note. `reciprocal` has **no fold-parent at
all** (the D2 report establishes this exhaustively: `reciprocal` is a *nonlinear* elementwise self-map,
`1/(a+b) ≠ 1/a + 1/b`, so it is not a member of the length-axis fold `inner_product` and not a member
of the term-axis fold `linear_combination`). So there is nothing to defer to — and nothing to defer:
`reciprocal` is a leaf elementwise field operation with **no multi-operation kernel fusion to
unfold**. The L0 complex kernel is *already* the unfolded single-pass elementwise reciprocation; the
only intra-element factoring it exhibits — the intermediate scalar `s = 1/|z|²` reused across the two
real components — is a **transparent performance trick** (`(a − bi)/(a² + b²)` factors as `a·s − i·b·s`
with `s = 1/(a²+b²)`; recomputing per component gives the identical value), recorded once at
L1/L2/L3 as the single fusion note, not a fold-level de-fusion. So this theme's edge is the pure
identity with no fusion-deferral note (unlike `dot-leaf-identity`), only the standing transparent-trick
note inherited from the floor entries.

## L2 form (LHS)

The L2 form is the `reciprocal` floor (`book/src/L2/reciprocal.md` §Signature, harvested cycle-042 D2)
— the mutation-free elementwise multiplicative-inverse, parameterised by element type:

    reciprocal :: Tensor[N] -> Tensor[N]
    reciprocal x = (\i -> 1 / x[i])     for i in [0, N)

with the element-type-parameterised per-element kernel inherited unchanged from the L1 leaf:

    | element type | per-element kernel                       |
    |--------------|------------------------------------------|
    | real         | 1 / x[i]               (in ℝ)            |
    | complex      | conj(x[i]) / |x[i]|²   (in ℂ; 1/z = z̄/|z|²) |

The L2 form is **pure / out-of-place** (no destination buffer; the result is a fresh tensor with the
same element type as `x`). It is **partial**: defined only where `x[i] ≠ 0` (the no-zero-guard policy
lifts as a precondition on the input — `L2/reciprocal` §Signature). The in-place receiver-self-overwrite
idiom (`x.Reciprocal()` overwriting `*this`), the `forall_switch` host/device dispatch, and the
no-zero-guard kernel realisation are NOT in the L2 signature — they reappear only at the substantive
L1>L0 rotation ([`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
sub-pattern A).

## L1 form (RHS)

The L1 form is the firm `reciprocal` leaf primitive (`book/src/L1/reciprocal.md` §Signature, firm) —
identical in signature, semantics, partiality precondition, and laws:

    reciprocal :: Tensor[N] -> Tensor[N]
    reciprocal(x)[i] = 1 / x[i]                  -- same element-type-parameterised kernel table

The L1 leaf is the **mutation-rotation** rendering: it already erases the L0 receiver-self-overwrite
mutation (the L1 form takes `x` as a value and returns a fresh result), folds the `forall_switch`
host/device dispatch and the no-zero-guard kernel realisation into the L1>L0 lowering, and records the
partiality as a precondition. The L1 entry is authoritative on every Palace-surface fact (the real
`mfem::Vector::Reciprocal()` upstream-MFEM alias, the complex `ComplexVector::Reciprocal()` kernel, the
four consumer call sites, the no-zero-guard policy, the complete L0 evidence list); the L2 form does
not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the leaf**. Every L2 binding maps to the same L1 binding at the same
position:

    | L2 floor (`L2/reciprocal`)         | L1 leaf (`L1/reciprocal`)          | Mapping  |
    |------------------------------------|------------------------------------|----------|
    | `reciprocal :: Tensor[N] -> Tensor[N]` | `reciprocal :: Tensor[N] -> Tensor[N]` | Identity. Same signature shape. |
    | `reciprocal x = (\i -> 1/x[i])`    | `reciprocal(x)[i] = 1/x[i]`        | Identity. Same elementwise map; same element-type kernel table (real `1/x[i]`, complex `z̄/|z|²`). |
    | partial: `x[i] ≠ 0` precondition   | partial: `x[i] ≠ 0` precondition   | Identity. Same partiality, recorded once on the input. |
    | algebraic laws 1–8                 | algebraic laws 1–8                 | Identity. Inherited unchanged (involution, mult-inverse identity, scalar-factor distribution, mult-distributivity, complex closed-form, conjugate-reciprocal commutation, all-ones fixed point, negation). |
    | single variant axis: element-type  | single variant axis: element-type  | Identity. Real/complex collapsed to one parameterised operator; result element type tracks input. |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the mapping
is total and bijective on the leaf. This is the identity-in-form property.

**The one note (transparent-trick, NOT a fusion deferral).** Unlike `dot-leaf-identity`, this theme
has no fold-parent to defer fusion to — and no fusion to defer. The single intra-element factoring is
the complex kernel's reuse of `s = 1/(XR[i]² + XI[i]²) = 1/|z|²`, computed once per element and applied
to both components (`XR[i] *= s; XI[i] *= -s`, `palace/linalg/vector.cpp:257-259`). This is a
transparent performance trick — algebraically identical to the unfused form — recorded once at the
floor entries (`L2/reciprocal` §"Fusion note", `L1/reciprocal`), not a fold-level de-fusion. The L2>L1
edge carries it as the standing transparent-trick note; no de-fusion treatment is performed at this
edge.

## Applicability conditions

The identity rewrite is valid when:

1. **`reciprocal` is treated as a standalone elementwise leaf, not decomposed.** `reciprocal` does
   not decompose into other L2 primitives — elementwise multiplicative inversion is a single field
   operation; its sub-operation (scalar reciprocation `1/x` in the element field) is below the L2
   layer's resolution. It has **no fold-parent** (the D2 report establishes this: a nonlinear
   self-map, not a member of `inner_product` or `linear_combination`), so — unlike
   `dot-leaf-identity` (Applicability condition 1, which presupposes the leaf-floor-vs-fold-only
   design fork) — there is **no design-fork presupposition** here. The leaf-vs-fold fork does not
   touch this fold-free leaf (see §Status).

2. **The leaf is value-thread-isomorphic across the edge.** The L2 `reciprocal` floor and the L1
   `reciprocal` leaf share the signature, the element-type kernel table, the partiality precondition,
   and the eight algebraic laws. Confirmed by construction: `L2/reciprocal` is authored as a thin
   floor entry whose laws are inherited unchanged from `L1/reciprocal` (D2 §"Algebraic laws",
   §Signature).

3. **No fold-level fusion to defer; only the standing transparent-trick note.** No multi-operation
   kernel fusion is unique to (or present on) the `reciprocal` leaf; the complex `s = 1/|z|²`
   intermediate is a transparent factoring recorded once at the floor entries, not a fold-level
   de-fusion (contrast `dot-leaf-identity`, whose fusion content IS the fold-parent's). The leaf's
   edge is therefore the identity with no fusion-deferral note.

If a future L2 `reciprocal` variant introduced leaf-specific fusion not present in the current
surface, the identity claim would need re-audit — none exists.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `reciprocal` floor's signature shape (`Tensor[N] -> Tensor[N]`) is
identical to the L1 `reciprocal` leaf's signature shape — a whole-tensor elementwise self-map with no
element loop exposed at either layer. The rotation between two value-thread-isomorphic leaves with
identical signatures is the identity by construction; there is no fold-parent fusion content to defer
and no leaf-unique fusion, so the leaf's own edge is a no-op modulo the standing transparent-trick
note.

**Empirical-match (secondary)**: the L1 leaf is firm on direct Palace evidence (`L1/reciprocal`
§Evidence: the complex `ComplexVector::Reciprocal()` kernel `palace/linalg/vector.cpp:248-261`, the
four consumer sites), and the L2 floor was authored (D2) as value-thread-isomorphic to it; the two
forms agree on every law and the single variant axis by independent transcription. The identity is
observational on the two firm/firming chapters, not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `reciprocal` floor (firming
cycle-042 D2), the L1 RHS is the firm `reciprocal` leaf (firm cycle-033). This theme is the identity
edge between existing chapters; it proposes no new operators. (The speculative `safe_reciprocal(x, ε)`
threshold-guarded operator named in `L1/reciprocal` §Variant axes / OQ
`safe-reciprocal-threshold-l1-candidacy` is NOT part of this theme — Palace has no zero-guarded
kernel, so no L0 anchor exists; the identity edge maps the unguarded leaf identity-in-form regardless.)

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/reciprocal.md` (firming cycle-042 D2) — the L2 floor (LHS): the standalone elementwise
  multiplicative-inverse leaf, value-thread-isomorphic to the L1 leaf, eight laws + single
  element-type axis inherited unchanged, fold-parent NONE. (The chapter lands at this cycle's
  integration alongside this theme — wave-2 serial sequencing applies D2 before this theme.)
- `book/src/L1/reciprocal.md` (firm cycle-033) — the L1 leaf (RHS): signature, the element-type kernel
  table, the partiality precondition (`x[i] ≠ 0`), the eight algebraic laws, the complete L0 evidence
  list. Authoritative on every Palace-surface fact.
- `book/src/L3-L2/reciprocal-body-identity.md` (firm cycle-042 D10) — the sibling L3>L2 edge of the
  same leaf (the other thin edge); co-dispatched this cycle.
- this L2>L1 leaf-identity edge composes with the firm L1>L0
  `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (firm) — the **substantive**
  rotation in the chain (sub-pattern A), which reintroduces the L0 receiver-self-overwrite mutation,
  the complex kernel decomposition, the `forall_switch` dispatch, and the no-zero-guard policy this
  identity edge abstracts away.

L0 evidence (transitive through the firm L1 leaf; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` body (the closed-form
  `s = 1/(XR²+XI²); XR *= s; XI *= -s` complex kernel realising `1/z = z̄/|z|²`), with the no-zero-guard
  policy. **Self-verified (anchor `Reciprocal` @248).** Inherited transitively; the leaf's edge is
  identity so no new L0 claim is made here.
- `palace/linalg/vector.cpp:257-259` — the three-line per-element kernel (`s` at :257, `XR *= s` at
  :258, `XI *= -s` at :259). **Self-verified (anchor `XR` @257-258).** Witnesses laws 1 and 5 (the
  complex closed form); transparent-trick `s` reuse.
- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` — the real-path alias;
  `Vector::Reciprocal()` resolves to upstream MFEM (the real element-type case). **Self-verified
  (anchor `mfem::Vector` @20).**

## Status

`firm` — the L2 LHS is the firm-this-cycle floor (D2), the L1 RHS is the firm `reciprocal` leaf
(cycle-033), and the rotation between two value-thread-isomorphic leaves with identical signatures is
the identity by construction (§"The rewrite (L2 → L1)" table is total and bijective on the leaf).
`reciprocal` is a **standalone elementwise leaf with no fold-parent** — there is no fold-level fusion
content to defer (contrast `dot-leaf-identity`) and no leaf-unique fusion; the only note is the
standing transparent-trick `s = 1/|z|²` factoring recorded at the floor entries. No speculative
operator, no negative-anchor reconstruction, no literature inference.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition, unlike the BLAS-1-floor themes).**
> The batch-12 meta-phase fork `dot-l2-leaf-floor-vs-fold-only-design` concerns whether the L2 BLAS-1
> *fold-member* leaves (`dot`, `scal`) are same-named floors or are absorbed into their fold-parents.
> **`reciprocal` has no fold-parent**, so neither the (a) fold-only nor the (b) same-named-floor
> reading re-anchors it — its L2 floor can only ever be a standalone same-named leaf. This theme is
> therefore *design-final*, not presuppositional: unlike `dot-leaf-identity` (whose §Status carries a
> design-presupposition note), this theme's identity claim does not depend on the fork's outcome.
```

### Theme 2 — `reciprocal-body-identity` (L3>L2)

```new:book/src/L3-L2/reciprocal-body-identity.md
# reciprocal-body-identity

The L3>L2 lowering theme for the elementwise multiplicative-inverse leaf `reciprocal`. The rewrite is
**identity-in-form on the body** with **no wrapper rotation** — `reciprocal` is a leaf whole-tensor
field operation, not a step body, so the L3 [`reciprocal`](../L3/reciprocal.md) whole-tensor form
lowers into the L2 [`reciprocal`](../L2/reciprocal.md) floor form by the identity on the primitive
itself. There is no `(op, K, s)`→`IterState` consolidation and no outer-loop dissolution to perform
(the two surface adjustments the sibling [`krylov-step-body-identity`](./krylov-step-body-identity.md)
carries at its wrapper); `reciprocal` has no wrapper. The body IS the identity. This is the
leaf-primitive analogue of `krylov-step-body-identity`, the direct sibling of
[`scal-body-identity`](./scal-body-identity.md) and [`dot-body-identity`](./dot-body-identity.md), and
— like `scal-body-identity` and unlike the fold-member BLAS-1 leaves — **fold-parent-free**: there is
no fold-parent at L2 for the leaf's fusion content to belong to (there is no fusion to begin with).

## Slug

`reciprocal-body-identity`

## Context

The `reciprocal` lowering relationships span three adjacent layers, all identity-in-form because
`reciprocal` is an elementwise leaf with no iteration view and no kernel fusion:

- **L3 form** ([`L3/reciprocal`](../L3/reciprocal.md), firm cycle-038) — the whole-tensor field
  operation `reciprocal :: Tensor[N] -> Tensor[N]`, the iteration-rotation rendering. Carries **no
  iteration view** (leaf primitive, not a step body) and **no sequential obstruction** (every element
  independent under the per-element reciprocation). Partial at `x[i] = 0`. The LHS of this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/reciprocal`](../L2/reciprocal.md), firm cycle-042 D2) — the fusion-rotation floor
  leaf, the base elementwise multiplicative-inverse primitive. **No fold-parent** (a nonlinear
  self-map, not a member of `inner_product` or `linear_combination`). The RHS of this theme.
- **L2>L1 form** ([`L2-L1/reciprocal-leaf-identity`](../L2-L1/reciprocal-leaf-identity.md), firm
  cycle-042 D10) — the onward edge into the L1 leaf; also identity-in-form.

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009), and the direct sibling
of [`scal-body-identity`](./scal-body-identity.md) (cycle-041). The `krylov-step` theme establishes the
pattern "identity-in-form on the kernel **body**, with surface adjustments at the **wrapper**"; its
point-3 applicability condition (`krylov-step-body-identity.md:97`) names the seven BLAS-1 primitives
as L3-native by signature shape: "each operates on whole-tensor inputs with no element-loop exposed at
L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step."
`reciprocal` is the **elementwise self-map** realization of the same classification (it is not one of
the named seven, but it is L3-native by the identical signature criterion — `Tensor[N] -> Tensor[N]`
exposes no per-element loop): the body is the identity, **and there is no wrapper at all** —
`reciprocal` is not a step body, so the two wrapper adjustments the `krylov-step` theme carries have no
analog here.

The firm L3 entry (`book/src/L3/reciprocal.md:131` §"Lowers to") currently records its lowering as
direct L3>L1 identity-in-form ("no interposed L2 entry, no L3-L2/L3-L1 theme file") via the
non-adjacent in-line convention, because no L2 `reciprocal` chapter existed. With the L2 `reciprocal`
floor now present (D2), this theme supplies the **adjacent-edge** L3>L2 rotation the L3 entry's
§"Lowers to" had to skip — so the L3 leaf lowers to an adjacent same-named L2 parent (per CLAUDE.md
§Methodology invariants **Identity-lowerings still require both L levels**) rather than non-adjacently
to L1.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/reciprocal`](../L3/reciprocal.md) §Signature, firm cycle-038):

    reciprocal :: Tensor[N] -> Tensor[N]
    reciprocal x = (\i -> 1 / x[i])     for i in [0, N)

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `x : Tensor[N]` a
single length axis, read-only at L3; result `Tensor[N]` of the same axis and element type with
`result[i] = 1/x[i]` for every `i ∈ [0, N)` (real `1/x[i]`; complex `z̄/|z|²`). Partial at `x[i] = 0`
(the precondition `x[i] ≠ 0`, recorded once). The operator carries **no iteration view** (leaf field
operation, not a step body) and **no sequential obstruction** (every element independent —
embarrassingly parallel, fully GPU-friendly). No L4 wrapper machinery applies (leaf primitives appear
inside L4 operator bodies as let-bindings, not first-class L4 typed-wrapper anchors — the cross-layer
"L4 candidate CONFIRMED-NOT-NEEDED" verdict for the elementwise / BLAS-1 cohort).

## L2 form (RHS)

The L2 floor form ([`L2/reciprocal`](../L2/reciprocal.md) §Signature, firm cycle-042 D2):

    reciprocal :: Tensor[N] -> Tensor[N]
    reciprocal x = (\i -> 1 / x[i])     for i in [0, N)

The base elementwise multiplicative-inverse leaf in the fusion-rotation vocabulary — a **standalone
elementwise leaf with NO fold-parent** (a nonlinear self-map, `1/(a+b) ≠ 1/a + 1/b`, not a member of
the length-axis fold `inner_product` nor the term-axis fold `linear_combination`). The signature is
**textually identical to the L3 form** modulo notation; the body is the same single whole-tensor field
operation. The eight algebraic laws hold unchanged across the edge (L3 §Algebraic laws ≡ L2 §Algebraic
laws — both inherit the L1 leaf's eight laws). There is **no fold-level fusion note** to carry (no
fold-parent, no multi-operation fusion); the only note either floor records is the transparent
`s = 1/|z|²` complex-intermediate factoring, and at L3 even that drops below the whole-tensor
resolution.

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    reciprocal x   (L3 whole-tensor field op)   ⇒   reciprocal x   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow:

    | L3 form (`L3/reciprocal`)              | L2 form (`L2/reciprocal`)              | Mapping  |
    |----------------------------------------|----------------------------------------|----------|
    | `reciprocal x = (\i -> 1/x[i])` (whole-tensor field op; no iteration view) | `reciprocal x = (\i -> 1/x[i])` (base elementwise floor leaf; NO fold-parent) | Identity. Same signature, same single elementwise field operation. The only framing difference is documentary: L3 frames `reciprocal` as a whole-tensor field op in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive. No operational adjustment. |
    | partial: `x[i] ≠ 0`                    | partial: `x[i] ≠ 0`                    | Identity. Same partiality precondition. |
    | algebraic laws 1–8                     | algebraic laws 1–8                     | Identity. Inherited unchanged across the chain. |
    | element-type variant axis              | element-type variant axis              | Identity. Real/complex collapsed; result element type tracks input. |
    | no iteration view, no obstruction      | no fold-parent, no fusion              | Identity. Nothing to rotate (leaf, no loop) and nothing to de-fuse (no fold, no multi-op fusion). |

The mapping is total and bijective on a single binding — the degenerate maximal case of the
identity-in-form property.

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body — the L3 `(op, K, s)` positional tuple consolidating
into the L2 `IterState` record, and the L3 tail-recursive outer loop collapsing to the L2
outer-driver-by-role reference. **Neither has an analog for `reciprocal`**: it is a single leaf field
operation, not a step body with an `(op, K, s)` carrier and an outer loop. This is identical in shape
to [`scal-body-identity`](./scal-body-identity.md): the body IS the identity, there is no wrapper, and
(additionally) there is no fold-parent to defer to.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `reciprocal` endpoints) when:

1. **`reciprocal` is treated as a leaf primitive, not decomposed.** `reciprocal` does not decompose
   into other L3 or L2 primitives — elementwise multiplicative inversion is a single field operation;
   its sub-operation (scalar reciprocation in the element field) is below both layers' resolution. It
   has **no fold-parent** (a nonlinear self-map; D2 establishes this), so — unlike the fold-member
   BLAS-1 body-identity themes (`dot-body-identity` Applicability condition 2,
   `scal-body-identity` §Status) — there is **no leaf-floor-vs-fold-only design presupposition** for
   this theme's RHS (see §Status).

2. **The signature is whole-tensor at both layers** — `Tensor[N] -> Tensor[N]` with no per-element
   loop exposed at L2 and no iteration view at L3. This is the `krylov-step-body-identity` point-3
   condition applied to the standalone `reciprocal` leaf: its signature has no per-element loop
   visible, so it is L3-native by construction and the rotation is identity-in-form rather than a
   decomposition.

3. **No iteration view, no sequential obstruction, no fold-level fusion.** `reciprocal` is
   element-local, reduction-free, rank-local; every element is independent. There is no outer loop, no
   carry trajectory, no recurrence — nothing for the L3 iteration rotation to have rotated and nothing
   for the L3>L2 lowering to dissolve. There is also no fold-parent and no multi-operation kernel
   fusion (the transparent `s = 1/|z|²` factoring is below the whole-tensor resolution at L3).

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape `Tensor[N] -> Tensor[N]` is whole-tensor by
construction at both layers — no element loop is exposed at L2, no iteration view at L3. The L3
vocabulary at this scope demands whole-tensor field operations with no element loop exposed;
`reciprocal` satisfies this *at L2 already*, so the rotation is the identity. This is the same
structural argument `scal-body-identity` makes (and `krylov-step-body-identity` point-3 makes for each
primitive in the kernel body), here promoted to dominant because there is no kernel body wrapping the
leaf, only the leaf itself.

**Empirical-match (secondary)**: the L3 leaf (firm cycle-038) and the L2 floor (firm cycle-042 D2) were
authored independently as value-thread-isomorphic to the same firm L1 leaf (cycle-033), and they agree
on every law, the single variant axis (element-type), and the partiality precondition by independent
transcription. The cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit
(`book/src/L3/index.md:41`) classified `reciprocal` as an **(A) identity-in-form** backfill candidate;
this theme's L3>L2 edge is the standalone-leaf realization of that audited classification, now that the
L2 floor entry exists for the rotation to target.

## Speculative L2 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/reciprocal`](../L3/reciprocal.md)) is firm (cycle-038), and the L2 RHS
([`L2/reciprocal`](../L2/reciprocal.md)) is firm (cycle-042 D2). No new L2 vocabulary is introduced.
`reciprocal` does not get its own L4 typed-wrapper anchor (leaf primitives appear inside L4 operator
bodies as let-bindings — the cross-layer "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the
elementwise cohort), so there is no upstream L4>L3 theme for `reciprocal` either; the L3 form is
L3-native by signature and this theme closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/reciprocal.md` (firm cycle-038) — the L3 whole-tensor form (LHS). Signature (:31),
  semantics (element-local, reduction-free, rank-local, no iteration view, no sequential obstruction),
  eight algebraic laws (:63-84), the single element-type variant axis (:105-119), the §"Lowers to"
  currently recording direct L3>L1 identity via the non-adjacent convention (:129-135) — this theme
  supplies the now-present adjacent L3>L2 edge (downstream-consistency touch on the L3 entry flagged in
  §Open-questions of the authoring report).
- `book/src/L2/reciprocal.md` (firm cycle-042 D2) — the L2 floor form (RHS). Identical signature and
  eight laws; the standalone elementwise leaf framing + the no-fold-parent / design-final
  determination. (Lands at this cycle's integration alongside this theme.)
- `book/src/L3-L2/scal-body-identity.md` (firm cycle-041) — the direct sibling shape: a fold-free leaf
  body-identity edge, "no wrapper to rotate, the body IS the identity". The structure of this theme is
  inherited from it.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm cycle-007/009) — §"Applicability conditions"
  point 3: the L3-native-by-signature-shape classification (no per-element loop visible) that is the
  structural justification for this identity edge. **Self-verified (anchor `L3-native` @97 — confirmed
  by the firm `dot-body-identity` / `scal-body-identity` themes that cite the same line).**

L0 evidence (transitive through the firm L1 leaf; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` body (the closed-form
  `s = 1/(XR²+XI²); XR *= s; XI *= -s` complex kernel). **Self-verified (anchor `Reciprocal` @248).**
  Inherited transitively; the leaf's edge is identity, no new L0 claim.
- `palace/linalg/vector.cpp:257-259` — the three-line per-element kernel. **Self-verified (anchor `XR`
  @257-258).**
- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` — the real-path alias (real
  element-type case). **Self-verified (anchor `mfem::Vector` @20).**

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/reciprocal`](../L3/reciprocal.md)) is firm (cycle-038); the L2 RHS
([`L2/reciprocal`](../L2/reciprocal.md)) is firm (cycle-042 D2). The body is the identity rotation on a
single leaf field operation; **there is no wrapper to rotate** (no `(op, K, s)`→`IterState`
consolidation, no outer-loop dissolution — `reciprocal` is a leaf, not a step body) and **no
fold-parent to defer fusion to** (a nonlinear self-map). The structural justification (whole-tensor
signature, no element loop, no iteration view) is the `krylov-step-body-identity` point-3 condition
specialized to the standalone leaf and promoted to dominant; the empirical-match anchor is the firm
L1/L2/L3 value-thread-isomorphic chain + the cycle-036 cross-layer (A) identity-in-form classification.
No speculative operator, no negative-anchor reconstruction, no sequential obstruction. The direct
sibling of `scal-body-identity` — the leaf-primitive counterpart of `krylov-step-body-identity`,
additionally fold-free.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition).** The batch-12 meta-phase fork
> `dot-l2-leaf-floor-vs-fold-only-design` concerns the L2 *fold-member* BLAS-1 leaves. `reciprocal`
> has **no fold-parent**, so its L2 RHS can only ever be a same-named standalone floor — neither the
> (a) fold-only nor the (b) same-named-floor reading re-anchors it. Unlike `dot-body-identity` /
> `scal-body-identity` (whose §Status carries a design-presupposition note), this theme's RHS is
> design-final; the identity claim does not depend on the fork's outcome.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the value-thread-isomorphic identity
  rotation: the L2 signature has no element loop exposed, which is exactly what makes it L3-native by
  construction. No additional structure is required for the lift. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter narrates only
  L3 → L2.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `reciprocal-leaf-identity` identity) is annotated in-line at the
  `reciprocal` entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are
  annotated in-line, not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This
  theme + the co-dispatched `reciprocal-leaf-identity` compose to capture it. The firm L3 entry's
  §"Lowers to" still records the historical direct L3>L1 identity; a downstream-consistency touch
  re-anchoring it to the now-present adjacent edges is a follow-up (flagged in the authoring report).
```

### Theme 3 — `elementwise-product-leaf-identity` (L2>L1)

```new:book/src/L2-L1/elementwise-product-leaf-identity.md
# elementwise-product-leaf-identity

The L2>L1 lowering theme for the Hadamard binary product leaf `elementwise_product`. The rewrite is
**identity-in-form on the leaf**: the L2 [`elementwise_product`](../L2/elementwise_product.md) floor
lowers to the L1 [`elementwise_product`](../L1/elementwise_product.md) primitive with the same
signature `(Tensor[N], Tensor[N]) -> Tensor[N]`, the same per-element `result[i] = a[i]·b[i]`
semantics, the same ten algebraic laws, and the same two variant axes (element-type + conjugation
sub-axis on the complex side) — value-thread-isomorphic on the primitive. Like
[`reciprocal-leaf-identity`](./reciprocal-leaf-identity.md) and unlike the cycle-041 fold-member
BLAS-1 floor edges, `elementwise_product` is **fork-INDEPENDENT — it has NO fold-parent**: it is a
binary `(Tensor[N], Tensor[N]) -> Tensor[N]` field operation, neither the length-axis fold
`inner_product` (reduce-to-`Scalar`) nor the term-axis fold `linear_combination`
(reduce-to-`Tensor[N]`). So there is no fusion to defer (the L0 `forall_switch` per-element multiply is
already the unfolded single-pass form). This theme records the identity edge; it is the L2>L1 analogue
of the L3>L2 [`elementwise_product-body-identity`](../L3-L2/elementwise_product-body-identity.md) (the
other thin edge of the same leaf).

## Slug

`elementwise-product-leaf-identity`

## Context

`elementwise_product` at L2 is the **floor** entry (`book/src/L2/elementwise_product.md`, harvested
cycle-042 D3): the standalone Hadamard binary field operation, the diagonal-operator-apply primitive,
rendered as its own same-named L2 chapter so the firm L3
[`elementwise_product`](../L3/elementwise_product.md) (cycle-038) leaf rests on an adjacent same-named
L2 parent (per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**)
rather than skipping a layer to L1. This theme is the L2>L1 edge of that floor.

The edge is the **identity-in-form** case: the L2 `elementwise_product` floor and the L1
`elementwise_product` leaf are value-thread-isomorphic on the primitive. This is the L2>L1 analogue of
the L3>L2 [`elementwise_product-body-identity`](../L3-L2/elementwise_product-body-identity.md) theme
(the other thin edge of the same leaf).

**Why this edge is identity AND fork-independent (the distinction from `dot-leaf-identity`).** The
cycle-041 `dot-leaf-identity` is identity-in-form *because* all its L2-layer fusion content is carried
by the fold-parent `inner-product-fold-specialization` — the leaf's own edge is left a no-op with a
deferring note. `elementwise_product` has **no fold-parent at all** (the D3 report establishes this
exhaustively: it is a binary field operation consuming two full-length operands and producing a
full-length result, with no fold skeleton — no reduction to a scalar, no variadic term list to
accumulate). The closest relationship is the *inverse* subsumption with `scal`
(`scal(α, x) = elementwise_product(broadcast(α, N), x)`; D3 law 7) — `elementwise_product` strictly
*generalises* `scal`, which is a sibling-subsumption identity, **not** a fold membership. So there is
nothing to defer to — and nothing to defer: `elementwise_product` is a leaf binary field operation
with **no multi-operation kernel fusion to unfold** (the L0 `forall_switch` per-element multiply —
real single-multiply `Y[i] = D[i]*X[i]`, complex six-multiply-add, conjugate two-sign-flip variant —
is already the unfolded single-pass form). The leaf's edge is therefore the pure identity with no
fusion-deferral note.

## L2 form (LHS)

The L2 form is the `elementwise_product` floor (`book/src/L2/elementwise_product.md` §Signature,
harvested cycle-042 D3) — the mutation-free Hadamard binary product, parameterised by element type:

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b               -- result[i] = a[i] · b[i]

with the conjugate variant (complex element-type only) as a sub-axis (NOT a separate primitive):

    elementwise_product_conj :: (a: ComplexTensor[N], b: ComplexTensor[N]) -> ComplexTensor[N]
    elementwise_product_conj(a, b) = ā ⊙ b

The L2 form is **pure / out-of-place** (no destination buffer; the result is a fresh tensor with the
same axis `N` and element type as the operands). `a` and `b` must share the length axis and the element
type. The in-place output-arg mutation idiom (`Y[i] = D[i]·X[i]` writing through the `y` output
argument of `BaseDiagonalOperator::Mult`), the operator-class wrapping, the consumer-local inline
duplicate (`jacobi.cpp` `Apply`), and the `forall_switch` host/device dispatch are NOT in the L2
signature — they reappear only at the substantive L1>L0 rotation
([`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
sub-pattern B).

## L1 form (RHS)

The L1 form is the firm `elementwise_product` leaf primitive (`book/src/L1/elementwise_product.md`
§Signature, firm cycle-019/032/036) — identical in signature, semantics, laws, and variant axes:

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b               -- same per-element kernel; same conjugation sub-axis

The L1 leaf is the **mutation-rotation** rendering: it already erases the L0 output-arg destination
mutation (the L1 form takes `a, b` as values and returns a fresh result), unwraps the operator-class
(the `BaseDiagonalOperator` wrapping; the operator-action form is recovered as L1 law 9
`apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`), erases the consumer-local
inline-duplication (`jacobi.cpp` `Apply`), and folds the `forall_switch` dispatch into the L1>L0
lowering. The L1 entry is authoritative on every Palace-surface fact (the canonical
`BaseDiagonalOperator::Mult` site, the `MultHermitianTranspose` conjugate variant, the `jacobi.cpp`
inline consumer duplicate, the absence of any free-function `linalg::ElementwiseProduct` symbol, the
ten algebraic laws, the complete L0 evidence list); the L2 form does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the leaf**. Every L2 binding maps to the same L1 binding at the same
position:

    | L2 floor (`L2/elementwise_product`)            | L1 leaf (`L1/elementwise_product`)             | Mapping  |
    |------------------------------------------------|------------------------------------------------|----------|
    | `elementwise_product :: (a, b) -> Tensor[N]`   | `elementwise_product :: (a, b) -> Tensor[N]`   | Identity. Same binary signature shape. |
    | `elementwise_product(a, b) = a ⊙ b`            | `elementwise_product(a, b) = a ⊙ b`            | Identity. Same per-element multiply `result[i] = a[i]·b[i]`. |
    | conjugate variant `elementwise_product_conj`   | conjugate variant `elementwise_product_conj`   | Identity. Same `ā ⊙ b` complex-side sub-axis. |
    | algebraic laws 1–10                            | algebraic laws 1–10                            | Identity. Inherited unchanged (commutativity, associativity, all-ones identity, all-zeros absorption, distributivity, scalar absorption, broadcast-subsumption-of-`scal`, negation, diagonal-operator-action identity, conjugation involution). |
    | two variant axes: element-type + conjugation   | two variant axes: element-type + conjugation   | Identity. Real/complex collapsed; conjugation sub-axis on the complex side. |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the mapping
is total and bijective on the leaf. This is the identity-in-form property.

**No fusion-deferral note (the fork-independence consequence).** Unlike `dot-leaf-identity`, this
theme has no fold-parent to defer fusion to — and no fusion to defer. The L0 `forall_switch`
per-element multiply pass (canonical `BaseDiagonalOperator::Mult` real `Y[i] = D[i]*X[i]`, complex
six-multiply-add, conjugate `MultHermitianTranspose` two-sign-flip) is already the unfolded single-pass
form. The L2>L1 edge therefore carries no de-fusion treatment; the substantive content (destination
buffer, operator-class unwrapping, consumer-duplicate erasure, device dispatch) is reintroduced only at
the L1>L0 rotation (sub-pattern B).

## Applicability conditions

The identity rewrite is valid when:

1. **`elementwise_product` is treated as a standalone binary leaf, not decomposed.**
   `elementwise_product` does not decompose into other L2 primitives — the Hadamard binary multiply is
   a single field operation; its sub-operation (per-element scalar multiplication of two operand
   vectors) is below the L2 layer's resolution. It has **no fold-parent** (fork-INDEPENDENT; the D3
   report establishes this: a binary `(Tensor[N], Tensor[N]) -> Tensor[N]` field op, neither
   reduce-to-`Scalar` nor a variadic term-fold), so — unlike `dot-leaf-identity` (Applicability
   condition 1, which presupposes the leaf-floor-vs-fold-only design fork) — there is **no
   design-fork presupposition** here. The leaf-vs-fold fork does not touch this fork-independent leaf
   (see §Status).

2. **The leaf is value-thread-isomorphic across the edge.** The L2 `elementwise_product` floor and the
   L1 `elementwise_product` leaf share the binary signature, the per-element multiply, the ten
   algebraic laws, and the two variant axes (element-type + conjugation sub-axis). Confirmed by
   construction: `L2/elementwise_product` is authored as a thin floor entry whose laws are inherited
   unchanged from `L1/elementwise_product` (D3 §"Algebraic laws", §Signature).

3. **No fold-level fusion to defer; the per-element pass is already unfolded.** No multi-operation
   kernel fusion is unique to (or present on) the `elementwise_product` leaf; the L0 `forall_switch`
   per-element multiply is the unfolded single-pass form (contrast `dot-leaf-identity`, whose fusion
   content IS the fold-parent's). The leaf's edge is therefore the identity with no fusion-deferral
   note.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `elementwise_product` floor's signature shape
(`(a: Tensor[N], b: Tensor[N]) -> Tensor[N]`) is identical to the L1 leaf's signature shape — a
whole-tensor binary field operation with no element loop exposed at either layer. The rotation between
two value-thread-isomorphic leaves with identical signatures is the identity by construction; there is
no fold-parent fusion content to defer and no leaf-unique fusion, so the leaf's own edge is a no-op.

**Empirical-match (secondary)**: the L1 leaf is firm on direct Palace evidence
(`L1/elementwise_product` §Evidence: the canonical `BaseDiagonalOperator::Mult` real
`palace/linalg/operator.cpp:478-487` / complex `:489-507` sites, the conjugate `MultHermitianTranspose`
`:545-568`, the `jacobi.cpp` consumer duplicate), and the L2 floor was authored (D3) as
value-thread-isomorphic to it; the two forms agree on every law and both variant axes by independent
transcription. The identity is observational on the two firm/firming chapters, not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `elementwise_product` floor
(firming cycle-042 D3), the L1 RHS is the firm `elementwise_product` leaf (firm cycle-019/032/036
chain). This theme is the identity edge between existing chapters; it proposes no new operators.

One evidentiary caveat carries over unchanged from the leaves (NOT a status reduction — the identity
structure is firm):

- **Conjugate-variant consumer duplicate is dead code (recognition rule).** The consumer-local
  `Apply<Transpose=true>` complex kernel (`palace/linalg/jacobi.cpp:61-69`) is unreachable under
  Palace's symmetric `MultTranspose → Mult` wiring (`jacobi.hpp:43`); the canonical
  `MultHermitianTranspose` (`palace/linalg/operator.cpp:545-568`) is live. The conjugation variant axis
  IS live at the canonical site; the identity edge maps it identity-in-form regardless of the
  consumer-duplicate dead branch (per `reciprocal-elementwise-product-mutation-rotation` §Status
  caveats). Not a status reduction.

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/elementwise_product.md` (firming cycle-042 D3) — the L2 floor (LHS): the standalone
  Hadamard binary field operation, value-thread-isomorphic to the L1 leaf, ten laws + two variant axes
  inherited unchanged, fold-parent NONE (fork-INDEPENDENT). (The chapter lands at this cycle's
  integration alongside this theme — wave-2 serial sequencing applies D3 before this theme.)
- `book/src/L1/elementwise_product.md` (firm cycle-019/032/036) — the L1 leaf (RHS): the binary
  signature, the per-element kernel, the conjugation sub-axis (§Variant axes), the ten algebraic laws
  (the diagonal-operator-action law 9, the `scal` broadcast-subsumption law 7), the complete L0
  evidence list. Authoritative on every Palace-surface fact.
- `book/src/L3-L2/elementwise_product-body-identity.md` (firm cycle-042 D10) — the sibling L3>L2 edge
  of the same leaf (the other thin edge); co-dispatched this cycle.
- this L2>L1 leaf-identity edge composes with the firm L1>L0
  `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (firm) — the **substantive**
  rotation in the chain (sub-pattern B), which reintroduces the L0 output-arg destination mutation, the
  operator-class wrapping, the consumer-duplicate kernel, the conjugation kernel-template choice, and
  the device dispatch this identity edge abstracts away.

L0 evidence (transitive through the firm L1 leaf; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/operator.cpp:478-487` — real canonical `BaseDiagonalOperator<Operator>::Mult`, the
  per-element body `Y[i] = D[i] * X[i]` at `:486`. **Self-verified (anchor `Mult` @479; `Y[i] = D[i] *
  X[i]` @486).** Inherited transitively; the leaf's edge is identity so no new L0 claim is made here.
- `palace/linalg/operator.cpp:545-568` — complex conjugate-variant canonical
  `DiagonalOperatorHelper<…>::MultHermitianTranspose`, the two-sign-flip kernel realising `d̄ ⊙ x`.
  **Self-verified (anchor `MultHermitianTranspose` @548).** Witnesses the conjugation sub-axis.

## Status

`firm` — the L2 LHS is the firm-this-cycle floor (D3), the L1 RHS is the firm `elementwise_product`
leaf (cycle-019/032/036), and the rotation between two value-thread-isomorphic leaves with identical
binary signatures is the identity by construction (§"The rewrite (L2 → L1)" table is total and
bijective on the leaf). `elementwise_product` is a **standalone binary field operation — fork-INDEPENDENT,
NO fold-parent** — there is no fold-level fusion content to defer (contrast `dot-leaf-identity`) and no
leaf-unique fusion; the L0 `forall_switch` per-element multiply is already the unfolded single-pass
form. No speculative operator, no negative-anchor reconstruction, no literature inference.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition, unlike the BLAS-1-floor themes).**
> The batch-12 meta-phase fork `dot-l2-leaf-floor-vs-fold-only-design` concerns whether the L2 BLAS-1
> *fold-member* leaves (`dot`, `scal`) are same-named floors or are absorbed into their fold-parents.
> **`elementwise_product` has no fold-parent** (it is the inverse-subsumption *generalisation* of
> `scal`, not a fold member), so neither the (a) fold-only nor the (b) same-named-floor reading
> re-anchors it — its L2 floor can only ever be a standalone same-named leaf. This theme is therefore
> *design-final*, not presuppositional: unlike `dot-leaf-identity` (whose §Status carries a
> design-presupposition note), this theme's identity claim does not depend on the fork's outcome.
```

### Theme 4 — `elementwise_product-body-identity` (L3>L2)

```new:book/src/L3-L2/elementwise_product-body-identity.md
# elementwise_product-body-identity

The L3>L2 lowering theme for the Hadamard binary product leaf `elementwise_product`. The rewrite is
**identity-in-form on the body** with **no wrapper rotation** — `elementwise_product` is a leaf
whole-tensor binary field operation, not a step body, so the L3
[`elementwise_product`](../L3/elementwise_product.md) whole-tensor form lowers into the L2
[`elementwise_product`](../L2/elementwise_product.md) floor form by the identity on the primitive
itself. There is no `(op, K, s)`→`IterState` consolidation and no outer-loop dissolution to perform
(the two surface adjustments the sibling [`krylov-step-body-identity`](./krylov-step-body-identity.md)
carries at its wrapper); `elementwise_product` has no wrapper. The body IS the identity. This is the
leaf-primitive analogue of `krylov-step-body-identity`, the direct sibling of
[`scal-body-identity`](./scal-body-identity.md) and [`reciprocal-body-identity`](./reciprocal-body-identity.md),
and — like those — **fold-parent-free** at L2: `elementwise_product` is fork-INDEPENDENT, neither a
member of `inner_product` nor of `linear_combination`.

## Slug

`elementwise_product-body-identity`

> **Filename-convention note.** This chapter uses the **underscore** spelling
> `elementwise_product-body-identity.md`, matching the underscore operator-chapter convention of the
> L1/L2/L3 `elementwise_product.md` entries (per the dispatch directive). The L2>L1 sibling uses the
> **hyphen** spelling `elementwise-product-leaf-identity.md` (matching the `dot-leaf-identity` /
> `nrm2-fold-specialization` L2>L1 sibling convention, which is hyphenated). The underscore-vs-hyphen
> split (underscore operator chapters + body-identity theme; hyphen concept page + leaf-identity theme)
> is consistent within the `elementwise_product` family but heterogeneous across the L2>L1 / L3>L2
> theme slugs; surfaced for the batch-12 meta-phase to normalize (see this theme's authoring report
> §Open questions).

## Context

The `elementwise_product` lowering relationships span three adjacent layers, all identity-in-form
because `elementwise_product` is a binary elementwise leaf with no iteration view and no kernel fusion:

- **L3 form** ([`L3/elementwise_product`](../L3/elementwise_product.md), firm cycle-038) — the
  whole-tensor binary field operation `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]`, the
  iteration-rotation rendering. Carries **no iteration view** (leaf primitive, not a step body) and
  **no sequential obstruction** (every element independent under the per-element multiply). The LHS of
  this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/elementwise_product`](../L2/elementwise_product.md), firm cycle-042 D3) — the
  fusion-rotation floor leaf, the base Hadamard-binary-multiply primitive and the diagonal-operator
  apply primitive. **No fold-parent (fork-INDEPENDENT).** The RHS of this theme.
- **L2>L1 form** ([`L2-L1/elementwise-product-leaf-identity`](../L2-L1/elementwise-product-leaf-identity.md),
  firm cycle-042 D10) — the onward edge into the L1 leaf; also identity-in-form.

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009), and the direct sibling
of [`scal-body-identity`](./scal-body-identity.md) and
[`reciprocal-body-identity`](./reciprocal-body-identity.md). The `krylov-step` theme establishes the
pattern "identity-in-form on the kernel **body**, with surface adjustments at the **wrapper**"; its
point-3 applicability condition (`krylov-step-body-identity.md:97`) names the seven BLAS-1 primitives as
L3-native by signature shape ("each operates on whole-tensor inputs with no element-loop exposed at
L2"). `elementwise_product` is the **binary Hadamard** realization of the same classification (it is not
one of the named seven, but it is L3-native by the identical signature criterion —
`(Tensor[N], Tensor[N]) -> Tensor[N]` exposes no per-element loop): the body is the identity, **and
there is no wrapper at all** — `elementwise_product` is not a step body, so the two wrapper adjustments
the `krylov-step` theme carries have no analog here.

The firm L3 entry (`book/src/L3/elementwise_product.md:149` §"Lowers to") currently records its
lowering as direct L3>L1 identity-in-form ("no interposed L2 entry, no L3-L2/L3-L1 theme file") via the
non-adjacent in-line convention, because no L2 `elementwise_product` chapter existed. With the L2
`elementwise_product` floor now present (D3), this theme supplies the **adjacent-edge** L3>L2 rotation
the L3 entry's §"Lowers to" had to skip — so the L3 leaf lowers to an adjacent same-named L2 parent
(per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**) rather than
non-adjacently to L1.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/elementwise_product`](../L3/elementwise_product.md) §Signature, firm
cycle-038):

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b               -- result[i] = a[i] · b[i]

with the conjugate variant (complex element-type only) as a sub-axis:

    elementwise_product_conj(a, b) = ā ⊙ b

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `a, b : Tensor[N]`
share a single length axis and element type, read-only at L3; result `Tensor[N]` of the same axis with
`result[i] = a[i]·b[i]` for every `i ∈ [0, N)`. The operator carries **no iteration view** (leaf binary
field operation, not a step body) and **no sequential obstruction** (every element independent —
embarrassingly parallel, fully GPU-friendly). No L4 wrapper machinery applies (the cross-layer
audit's "L4 candidate CONFIRMED-NOT-NEEDED" verdict for `elementwise_product`,
`book/src/L3/elementwise_product.md:26`).

## L2 form (RHS)

The L2 floor form ([`L2/elementwise_product`](../L2/elementwise_product.md) §Signature, firm cycle-042
D3):

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b

The base Hadamard-binary-multiply leaf in the fusion-rotation vocabulary — a **standalone binary field
operation, fork-INDEPENDENT, NO fold-parent** (neither the length-axis fold `inner_product`
reduce-to-`Scalar` nor the term-axis fold `linear_combination` reduce-to-`Tensor[N]`). The signature is
**textually identical to the L3 form** modulo notation; the body is the same single whole-tensor binary
field operation. The ten algebraic laws and the two variant axes (element-type + conjugation sub-axis)
hold unchanged across the edge (L3 §Algebraic laws ≡ L2 §Algebraic laws — both inherit the L1 leaf's
ten laws). There is **no fold-level fusion note** to carry (no fold-parent, no multi-operation fusion);
the L0 `forall_switch` per-element multiply is already the unfolded single-pass form.

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    elementwise_product(a, b)   (L3 whole-tensor field op)   ⇒   elementwise_product(a, b)   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow:

    | L3 form (`L3/elementwise_product`)             | L2 form (`L2/elementwise_product`)             | Mapping  |
    |------------------------------------------------|------------------------------------------------|----------|
    | `elementwise_product(a, b) = a ⊙ b` (whole-tensor binary field op; no iteration view) | `elementwise_product(a, b) = a ⊙ b` (base Hadamard floor leaf; NO fold-parent) | Identity. Same signature, same single binary field operation. The only framing difference is documentary: L3 frames it in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive (and the diagonal-operator apply primitive, law 9). No operational adjustment. |
    | conjugate variant `ā ⊙ b`                      | conjugate variant `ā ⊙ b`                      | Identity. Same complex-side conjugation sub-axis. |
    | algebraic laws 1–10                            | algebraic laws 1–10                            | Identity. Inherited unchanged across the chain. |
    | two variant axes: element-type + conjugation   | two variant axes: element-type + conjugation   | Identity. Real/complex collapsed; conjugation sub-axis on the complex side. |
    | no iteration view, no obstruction              | no fold-parent, no fusion                      | Identity. Nothing to rotate (leaf, no loop) and nothing to de-fuse (no fold, the per-element pass is already unfolded). |

The mapping is total and bijective on a single binding — the degenerate maximal case of the
identity-in-form property.

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body — the L3 `(op, K, s)` positional tuple consolidating
into the L2 `IterState` record, and the L3 tail-recursive outer loop collapsing to the L2
outer-driver-by-role reference. **Neither has an analog for `elementwise_product`**: it is a single
leaf binary field operation, not a step body with an `(op, K, s)` carrier and an outer loop. This is
identical in shape to [`scal-body-identity`](./scal-body-identity.md) and
[`reciprocal-body-identity`](./reciprocal-body-identity.md): the body IS the identity, there is no
wrapper, and (additionally) there is no fold-parent to defer to.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `elementwise_product` endpoints)
when:

1. **`elementwise_product` is treated as a leaf primitive, not decomposed.** `elementwise_product` does
   not decompose into other L3 or L2 primitives — the Hadamard binary multiply is a single field
   operation; its sub-operation (per-element scalar multiplication of two operands) is below both
   layers' resolution. It has **no fold-parent** (fork-INDEPENDENT; D3 establishes this), so — unlike
   the fold-member BLAS-1 body-identity themes (`dot-body-identity` Applicability condition 2,
   `scal-body-identity` §Status) — there is **no leaf-floor-vs-fold-only design presupposition** for
   this theme's RHS (see §Status). (Note the inverse-subsumption sibling relationship
   `scal(α, x) = elementwise_product(broadcast(α, N), x)` is a derived identity, not a fold membership;
   `elementwise_product` *generalises* `scal`.)

2. **The signature is whole-tensor at both layers** — `(Tensor[N], Tensor[N]) -> Tensor[N]` with no
   per-element loop exposed at L2 and no iteration view at L3. This is the `krylov-step-body-identity`
   point-3 condition applied to the standalone `elementwise_product` leaf: its signature has no
   per-element loop visible, so it is L3-native by construction and the rotation is identity-in-form
   rather than a decomposition.

3. **No iteration view, no sequential obstruction, no fold-level fusion.** `elementwise_product` is
   element-local, reduction-free, rank-local; every element is independent. There is no outer loop, no
   carry trajectory, no recurrence — nothing for the L3 iteration rotation to have rotated and nothing
   for the L3>L2 lowering to dissolve. There is also no fold-parent and no multi-operation kernel
   fusion (the L0 `forall_switch` per-element multiply is the unfolded single-pass form).

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape `(Tensor[N], Tensor[N]) -> Tensor[N]` is
whole-tensor by construction at both layers — no element loop is exposed at L2, no iteration view at L3.
The L3 vocabulary at this scope demands whole-tensor field operations with no element loop exposed;
`elementwise_product` satisfies this *at L2 already*, so the rotation is the identity. This is the same
structural argument `scal-body-identity` / `reciprocal-body-identity` make (and
`krylov-step-body-identity` point-3 makes for each primitive in the kernel body), here promoted to
dominant because there is no kernel body wrapping the leaf, only the leaf itself.

**Empirical-match (secondary)**: the L3 leaf (firm cycle-038) and the L2 floor (firm cycle-042 D3) were
authored independently as value-thread-isomorphic to the same firm L1 leaf (cycle-019/032/036), and
they agree on every law, both variant axes (element-type + conjugation sub-axis), and the
diagonal-operator-action law 9 by independent transcription. The cycle-036 D2 cross-layer-cross-cutter
L3-cohort-growth audit (`book/src/L3/index.md:41`) classified `elementwise_product` ("Hadamard binary")
as an **(A) identity-in-form** backfill candidate; this theme's L3>L2 edge is the standalone-leaf
realization of that audited classification, now that the L2 floor entry exists for the rotation to
target.

## Speculative L2 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/elementwise_product`](../L3/elementwise_product.md)) is firm (cycle-038), and the L2 RHS
([`L2/elementwise_product`](../L2/elementwise_product.md)) is firm (cycle-042 D3). No new L2 vocabulary
is introduced. `elementwise_product` does not get its own L4 typed-wrapper anchor (the cross-layer "L4
candidate CONFIRMED-NOT-NEEDED" verdict, `book/src/L3/elementwise_product.md:26`), so there is no
upstream L4>L3 theme for `elementwise_product` either; the L3 form is L3-native by signature and this
theme closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/elementwise_product.md` (firm cycle-038) — the L3 whole-tensor form (LHS). Signature
  (:34-45), semantics (element-local, reduction-free, rank-local, no iteration view, no sequential
  obstruction), ten algebraic laws (:74-87), the two variant axes (element-type + conjugation sub-axis,
  :124-137), the §"Lowers to" currently recording direct L3>L1 identity via the non-adjacent convention
  (:147-151) — this theme supplies the now-present adjacent L3>L2 edge (downstream-consistency touch on
  the L3 entry flagged in §Open-questions of the authoring report).
- `book/src/L2/elementwise_product.md` (firm cycle-042 D3) — the L2 floor form (RHS). Identical
  signature and ten laws; the standalone Hadamard binary field operation framing + the
  fork-INDEPENDENT / no-fold-parent / design-final determination. (Lands at this cycle's integration
  alongside this theme.)
- `book/src/L3-L2/scal-body-identity.md` + `book/src/L3-L2/reciprocal-body-identity.md` (firm cycle-041
  / cycle-042 D10) — the direct sibling shapes: fold-free leaf body-identity edges, "no wrapper to
  rotate, the body IS the identity". The structure of this theme is inherited from them.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm cycle-007/009) — §"Applicability conditions"
  point 3: the L3-native-by-signature-shape classification (no per-element loop visible) that is the
  structural justification for this identity edge. **Self-verified (anchor `L3-native` @97 — confirmed
  by the firm `dot-body-identity` / `scal-body-identity` themes that cite the same line).**

L0 evidence (transitive through the firm L1 leaf; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/operator.cpp:478-487` — real canonical `BaseDiagonalOperator<Operator>::Mult`, the
  per-element body `Y[i] = D[i] * X[i]` at `:486`. **Self-verified (anchor `Mult` @479; `Y[i] = D[i] *
  X[i]` @486).** Inherited transitively; the leaf's edge is identity, no new L0 claim.
- `palace/linalg/operator.cpp:545-568` — complex conjugate-variant
  `DiagonalOperatorHelper<…>::MultHermitianTranspose`, the two-sign-flip kernel realising `d̄ ⊙ x`.
  **Self-verified (anchor `MultHermitianTranspose` @548).** Witnesses the conjugation sub-axis.

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/elementwise_product`](../L3/elementwise_product.md)) is firm (cycle-038); the L2 RHS
([`L2/elementwise_product`](../L2/elementwise_product.md)) is firm (cycle-042 D3). The body is the
identity rotation on a single leaf binary field operation; **there is no wrapper to rotate** (no
`(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — `elementwise_product` is a leaf,
not a step body) and **no fold-parent to defer fusion to** (fork-INDEPENDENT). The structural
justification (whole-tensor signature, no element loop, no iteration view) is the
`krylov-step-body-identity` point-3 condition specialized to the standalone leaf and promoted to
dominant; the empirical-match anchor is the firm L1/L2/L3 value-thread-isomorphic chain + the
cycle-036 cross-layer (A) identity-in-form classification. No speculative operator, no negative-anchor
reconstruction, no sequential obstruction. The direct sibling of `scal-body-identity` /
`reciprocal-body-identity` — the leaf-primitive counterpart of `krylov-step-body-identity`,
additionally fork-independent.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition).** The batch-12 meta-phase fork
> `dot-l2-leaf-floor-vs-fold-only-design` concerns the L2 *fold-member* BLAS-1 leaves.
> `elementwise_product` has **no fold-parent** (it is the inverse-subsumption *generalisation* of
> `scal`, not a fold member), so its L2 RHS can only ever be a same-named standalone floor — neither
> the (a) fold-only nor the (b) same-named-floor reading re-anchors it. Unlike `dot-body-identity` /
> `scal-body-identity` (whose §Status carries a design-presupposition note), this theme's RHS is
> design-final; the identity claim does not depend on the fork's outcome.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the value-thread-isomorphic identity
  rotation: the L2 signature has no element loop exposed, which is exactly what makes it L3-native by
  construction. No additional structure is required for the lift. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter narrates only
  L3 → L2.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `elementwise-product-leaf-identity` identity) is annotated in-line
  at the `elementwise_product` entries per the CLAUDE.md invariant "Identity rotations across
  non-adjacent layers are annotated in-line, not via a dedicated lowering directory" — no
  `book/src/L3-L1/` directory. This theme + the co-dispatched `elementwise-product-leaf-identity`
  compose to capture it. The firm L3 entry's §"Lowers to" still records the historical direct L3>L1
  identity; a downstream-consistency touch re-anchoring it to the now-present adjacent edges is a
  follow-up (flagged in the authoring report).

- **Filename underscore-vs-hyphen split (for the meta-phase).** This theme is `_`-spelled
  (`elementwise_product-body-identity.md`, matching the operator chapters); the L2>L1 sibling is
  `-`-spelled (`elementwise-product-leaf-identity.md`, matching the hyphenated L2>L1 theme-slug
  convention). Heterogeneous but each link resolves on disk; surfaced for the batch-12 meta-phase to
  normalize the operator-chapter / theme-slug / concept-page slug spelling across the artifact.
```

### Dep-map append — L2-L1/index.md (two new rows)

```edit:book/src/L2-L1/index.md
| [dot-leaf-identity](./dot-leaf-identity.md) | `L2/dot` (firm, cycle-041 leaf-floor) | `L1/dot` (firm; `dot` + `tdot`) | firm *(structural; identity-in-form on the inner-product leaf — value-thread-isomorphic signature; all L2-layer fusion deferred to the fold-parent `inner-product-fold-specialization`; thin floor-edge of the BLAS-1 leaf)* |
| [reciprocal-leaf-identity](./reciprocal-leaf-identity.md) | `L2/reciprocal` (firm, cycle-042 D2 floor) | `L1/reciprocal` (firm cycle-033 leaf) | firm *(structural; identity-in-form on the elementwise multiplicative-inverse leaf — value-thread-isomorphic signature + eight laws + single element-type axis; **fold-parent-FREE** — a nonlinear self-map, NOT a member of `inner_product`/`linear_combination`, so NO fusion to defer (contrast `dot-leaf-identity`); only the transparent `s = 1/|z|²` complex-intermediate note; **design-final on the leaf-vs-fold fork — no fold-parent to re-anchor into**)* |
| [elementwise-product-leaf-identity](./elementwise-product-leaf-identity.md) | `L2/elementwise_product` (firm, cycle-042 D3 floor) | `L1/elementwise_product` (firm cycle-019/032/036 leaf) | firm *(structural; identity-in-form on the Hadamard binary leaf — value-thread-isomorphic signature + ten laws + two variant axes (element-type + conjugation sub-axis); **fork-INDEPENDENT — NO fold-parent** (a binary field op, neither `inner_product` reduce-to-`Scalar` nor `linear_combination` reduce-to-`Tensor[N]`; the inverse-subsumption generalisation of `scal`), so NO fusion to defer — the L0 `forall_switch` per-element multiply is already unfolded; **design-final on the leaf-vs-fold fork**)* |
```

### Dep-map append — L3-L2/index.md (two new rows)

```edit:book/src/L3-L2/index.md
| [`scal-body-identity`](./scal-body-identity.md) | L3 [`scal`](../L3/scal.md) §Signature — the whole-tensor field operation `scal :: Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`scal`](../L2/scal.md) §Signature — the base scalar-vector-multiply floor leaf (arity-1 member of `linear_combination`, cited NOT merged); identical signature. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-041 D6 abstractor; identity-in-form on the body, **no wrapper to rotate** — the leaf-primitive counterpart of `krylov-step-body-identity`) |
| [`reciprocal-body-identity`](./reciprocal-body-identity.md) | L3 [`reciprocal`](../L3/reciprocal.md) §Signature — the whole-tensor field operation `reciprocal :: Tensor[N] -> Tensor[N]` (elementwise `1/x[i]`, partial at `x[i]=0`); leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`reciprocal`](../L2/reciprocal.md) §Signature — the base elementwise multiplicative-inverse floor leaf; **standalone, NO fold-parent** (nonlinear self-map); identical signature + eight laws + element-type axis. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 specialized to the standalone fold-free leaf) + secondary `empirical-match` (firm L1/L2/L3 value-thread-isomorphic chain + cycle-036 (A) identity-in-form classification) | `firm` (cycle-042 D10 abstractor; identity-in-form on the body, **no wrapper to rotate AND no fold-parent to defer to** — direct sibling of `scal-body-identity`; **design-final on the leaf-vs-fold fork**) |
| [`elementwise_product-body-identity`](./elementwise_product-body-identity.md) | L3 [`elementwise_product`](../L3/elementwise_product.md) §Signature — the whole-tensor binary field operation `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` (Hadamard `a ⊙ b`); leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`elementwise_product`](../L2/elementwise_product.md) §Signature — the base Hadamard-binary-multiply floor leaf; **fork-INDEPENDENT, NO fold-parent**; identical signature + ten laws + two variant axes (element-type + conjugation sub-axis). | `structural` (whole-tensor binary signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 specialized to the standalone fork-independent leaf) + secondary `empirical-match` (firm L1/L2/L3 value-thread-isomorphic chain + cycle-036 (A) identity-in-form classification) | `firm` (cycle-042 D10 abstractor; identity-in-form on the body, **no wrapper to rotate AND no fold-parent to defer to** — direct sibling of `scal-body-identity`/`reciprocal-body-identity`; **design-final on the leaf-vs-fold fork**) |
```

### SUMMARY.md registrations (four chapter entries)

```edit:book/src/SUMMARY.md
- [dot-body-identity](./L3-L2/dot-body-identity.md)
- [reciprocal-body-identity](./L3-L2/reciprocal-body-identity.md)
- [elementwise_product-body-identity](./L3-L2/elementwise_product-body-identity.md)
```

```edit:book/src/SUMMARY.md
- [dot-leaf-identity](./L2-L1/dot-leaf-identity.md)
- [reciprocal-leaf-identity](./L2-L1/reciprocal-leaf-identity.md)
- [elementwise-product-leaf-identity](./L2-L1/elementwise-product-leaf-identity.md)
```

## Speculative operators proposed

**None across all four themes.** Every endpoint is existing or co-landing vocabulary:

- L2 `reciprocal` (D2, co-landing this cycle) / L1 `reciprocal` (firm cycle-033) / L3 `reciprocal`
  (firm cycle-038).
- L2 `elementwise_product` (D3, co-landing this cycle) / L1 `elementwise_product` (firm
  cycle-019/032/036) / L3 `elementwise_product` (firm cycle-038).

All four themes are pure identity edges between existing firm/firming chapters. The speculative
`safe_reciprocal(x, ε)` zero-guarded operator named in `L1/reciprocal` §Variant axes (OQ
`safe-reciprocal-threshold-l1-candidacy`) is NOT proposed here — it is unrelated to the identity edge
and has no L0 anchor.

## Supporting evidence

- **L0 anchors self-verified on-disk this invocation** via `tools/citecheck/citecheck.py --anchor`
  (2026-06-01), all `[ok]`:
  - `palace/linalg/vector.cpp:248-261` (anchor `Reciprocal` @248) + `:257-259` (anchor `XR` @257-258)
    — the complex `ComplexVector::Reciprocal()` kernel (reciprocal themes).
  - `palace/linalg/vector.hpp:20` (anchor `mfem::Vector` @20) — the real-path `using Vector` alias
    (reciprocal themes).
  - `palace/linalg/operator.cpp:478-487` (anchor `Mult` @479) + `:486` (anchor `Y[i] = D[i] * X[i]`
    @486) — the real canonical `BaseDiagonalOperator::Mult` site (elementwise_product themes).
  - `palace/linalg/operator.cpp:545-568` (anchor `MultHermitianTranspose` @548) — the complex
    conjugate-variant site (elementwise_product themes).
  - `--scan` bounds/path pre-emit pass: all theme L0 citations are full paths, in-range, no `OOB` /
    `MISS` / `AMBIG`.
- **Templates copied**: `book/src/L2-L1/dot-leaf-identity.md` (L2>L1 thin-identity leaf structure) +
  `book/src/L3-L2/scal-body-identity.md` (L3>L2 fold-free "no wrapper to rotate" body-identity
  structure — the closest precedent, since `scal-body-identity` is the existing fold-free leaf
  body-identity edge) + `book/src/L3-L2/dot-body-identity.md` (L3>L2 fold-member body-identity, for the
  L3-native-by-signature classification citing `krylov-step-body-identity.md:97`).
- **Source of truth for the L2 forms**: the D2 report
  `reports/2026-06-01T063231Z-cycle-042-harvester-L2-reciprocal/CYCLE.md` (proposed
  `book/src/L2/reciprocal.md`) + the D3 report
  `reports/2026-06-01T063231Z-cycle-042-harvester-L2-elementwise-product/CYCLE.md` (proposed
  `book/src/L2/elementwise_product.md`). Both establish the fold-parent-free / fork-independent
  determination this dispatch's themes carry forward.
- **The shared substantive L1>L0 rotation**:
  `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (firm) — sub-pattern A
  (reciprocal receiver-self-overwrite) + sub-pattern B (elementwise_product output-arg + operator-class
  wrapping + consumer-duplicate). The four identity edges abstract away exactly the L0 content this
  theme reintroduces.

## Open questions / caveats

1. **COUNT-OWNERSHIP (deferred to D11, per dispatch directive).** This report appends ONLY its four
   theme rows: two to the L2-L1/index dep-map (`reciprocal-leaf-identity` +
   `elementwise-product-leaf-identity`), two to the L3-L2/index dep-map (`reciprocal-body-identity` +
   `elementwise_product-body-identity`), plus four SUMMARY.md chapter registrations and four theme
   bodies. I have **NOT** touched the consolidated tallies — neither the L2-L1/index §"Vocabulary
   cohort" firm count ("firm 7 → 10" at `book/src/L2-L1/index.md:50`) / §"Identity-in-form BLAS-1-floor
   edges" sub-list, nor the L3-L2/index §"Vocabulary cohort" firm count ("firm 2 → 5" /
   `l3-l2-rotation-theme-coverage-gap` "5-of-18" at `book/src/L3-L2/index.md:35`) / §"Identity-in-form
   BLAS-1-leaf body edges" sub-list. D11 owns the consolidated counts this cycle (this landing would
   raise L2>L1 firm 10 → 12 and L3>L2 firm 5 → 7, and the `l3-l2-rotation-theme-coverage-gap` to
   7-of-18 — but I do NOT assert those absolute numbers, to avoid the
   `parallel-blind-shared-index-count-divergence` friction). D11 should also add the four themes to the
   two §"Identity-in-form …" sub-lists, flagging both pairs as the **fold-free / fork-independent**
   members (distinct from the cycle-041 fold-member / fold-consumer edges).

2. **Filename slug split within the `elementwise_product` family (for the meta-phase).** Per the
   dispatch directive I used `elementwise_product-body-identity.md` (**underscore**, matching the L3
   operator-chapter convention) for the L3>L2 theme and `elementwise-product-leaf-identity.md`
   (**hyphen**, matching the hyphenated L2>L1 theme-slug convention — `dot-leaf-identity`,
   `nrm2-fold-specialization`) for the L2>L1 theme. So the L2>L1/L3>L2 sibling pair for the SAME leaf
   has *different* spellings (`elementwise-product-…` vs `elementwise_product-…`). This is internally
   consistent with each layer's sibling convention but creates a same-leaf spelling split; combined
   with the pre-existing operator-chapter (underscore) vs concept-page (hyphen) split the D3 report
   flagged, the `elementwise_product` family now has three slug spellings in play. **Flagged for the
   batch-12 meta-phase** to decide whether to normalize the `elementwise_product` family slug spelling
   artifact-wide (every link in these themes resolves on disk — not build-blocking). The `reciprocal`
   pair has no such split (both `reciprocal-leaf-identity` / `reciprocal-body-identity` are hyphen, and
   `reciprocal` is already single-word).

3. **Design-final, NOT design-presupposing (the key difference from the cycle-041 sibling themes).**
   All four themes are recorded as **design-final on the leaf-vs-fold fork**
   (`dot-l2-leaf-floor-vs-fold-only-design`, batch-12 meta-phase), not design-presupposing. The
   cycle-041 `dot-leaf-identity` / `dot-body-identity` / `scal-*` themes carry a design-presupposition
   note in §Status (their identity claim depends on the (b) same-named-floor reading; under (a)
   fold-only their LHS/RHS re-anchor to the fold-parent). `reciprocal` and `elementwise_product` are
   **fold-parent-free** (D2 / D3 establish this exhaustively: nonlinear self-map / fork-independent
   binary op), so neither (a) nor (b) re-anchors them — their floors can only ever be standalone
   same-named leaves. This is a **data point FOR the meta-phase adjudication**: the floor/identity-edge
   cohort is heterogeneous — fold-member leaves (`dot`, `scal`), a fold-consumer (`nrm2`), and now
   fold-free elementwise leaves (`reciprocal`, `elementwise_product`) whose stability does NOT depend
   on the fork outcome. Worth the meta-phase noting that the `l2-floor-under-l3-blas1-cohort`
   foundation-first directive now has two fully fork-independent members whose identity edges are
   design-final.

4. **Downstream-consistency touch on the firm L3 entries (flagged, not applied — out of abstractor
   write-scope).** Both `book/src/L3/reciprocal.md:131` and `book/src/L3/elementwise_product.md:149`
   §"Lowers to" currently record a direct L3>L1 identity-in-form rotation ("no interposed L2 entry, no
   L3-L2/L3-L1 theme file") because no L2 floor / L3>L2 theme existed when they were authored
   (cycle-038). With the D2/D3 L2 floors + these L3>L2 themes now present, those §"Lowers to" sections
   are stale (they should re-anchor to the now-present adjacent L2 parent + this L3>L2 edge, with the
   transitive L3>L1 identity annotated in-line per the non-adjacent convention). This is a `lifter`
   re-anchor follow-up (re-anchoring firm L3 entries to firmed-up adjacent vocabulary is the lifter's
   job, not the abstractor's) — flagged here as an OQ, not applied. Same situation `dot-body-identity`
   flagged for `book/src/L3/dot.md:127-131` in cycle-041 (it remained a deferred downstream touch).
   Filing OQ `l3-elementwise-pair-lowers-to-stale-after-l2-floor-landing`.

5. **L2>L1 reciprocal forward-reference now resolves.** The D2 report's §Open-questions flagged that
   `L2/reciprocal` §"Lowers to" forward-references a not-yet-existing `L2-L1/reciprocal-elementwise-identity`
   theme as plain text, and asked D10 to pick the slug; D2 suggested `-elementwise-identity` or
   `-leaf-identity`. I chose **`reciprocal-leaf-identity`** (matching the `dot-leaf-identity` sibling
   convention — the edge is an identity-leaf-lowering, NOT a fold→leaf dispatch, so `-leaf-identity` is
   the correct family slug and `-fold-specialization` would be doubly mis-naming for a fold-free leaf).
   The D2 entry's in-line plain-text reference needs no edit (it is plain text); a downstream
   upgrade-to-live-link is a finalize/lifter nicety, not required (the D2 §"Lowers to" reference is
   prose, not a dep-map row).

6. **Both pairs are standalone / fork-independent — no fold-parent dispatch row.** Unlike
   `scal-fold-specialization` (the arity-1 row of `linear-combination-fold-specialization`) or
   `dot-leaf-identity` (deferring to `inner-product-fold-specialization`), neither
   `reciprocal-*-identity` nor `elementwise-product-*-identity` has a fold-parent theme to cross-cite
   for deferred fusion content. This is correct and load-bearing (the D2/D3 fold-free determination),
   not a missing cross-reference. Recorded so a future `same-layer-cross-cutter` does not read the
   absent fold-parent cross-cite as a coverage gap.
