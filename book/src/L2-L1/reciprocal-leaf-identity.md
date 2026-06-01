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
leaf), and a sibling shape to [`scal-leaf-identity`](./scal-leaf-identity.md) and
[`nrm2-leaf-identity`](./nrm2-leaf-identity.md) — except those defer to a fold-parent or
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
