---
agent: abstractor
invoked_at: 2026-06-01T105425Z
scope: TWO adjacent thin-identity lowering themes for axpby — L2>L1 axpby-leaf-identity + L3>L2 axpby-body-identity
status: pending
inputs:
  - reports/2026-06-01T105425Z-cycle-043-harvester-L2-axpby/CYCLE.md (wave-1 D4; the proposed book/src/L2/axpby.md — source-of-truth for the L2 axpby form; co-lands this cycle)
  - book/src/L1/axpby.md (firm cycle-003; the L1 fused two-scalar two-vector leaf — RHS of the L2>L1 edge)
  - book/src/L3/axpby.md (firm cycle-011; the L3 whole-tensor form — LHS of the L3>L2 edge; L3-native by signature shape)
  - book/src/L1-L0/axpby-mutation-rotation.md (firm cycle-002; the onward L1>L0 in-place mutation this pure pair abstracts over)
  - book/src/L2/linear_combination.md:70 (firm cycle-018; fold-parent — axpby(α,x,β,y) = linear_combination [(α,x),(β,y)] arity-2 specialization identity)
  - book/src/L2-L1/dot-leaf-identity.md + book/src/L2-L1/scal-fold-specialization.md (sibling L2>L1 precedents this edge mirrors)
  - book/src/L3-L2/dot-body-identity.md + book/src/L3-L2/scal-body-identity.md (sibling L3>L2 precedents this edge mirrors)
  - book/src/L3-L2/krylov-step-body-identity.md:97 (firm; names axpby among the seven L3-native-by-signature BLAS-1 primitives — the structural justification for both identity edges; self-verified via citecheck --anchor 'axpby' @97)
integrated_at: 2026-06-01T140000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-043 batch integration (cohort-completing L2-floor build); D7 axpby theme pair (L2>L1 axpby-leaf-identity + L3>L2 axpby-body-identity); cross-report rename repair applied; clean; see reports/2026-06-01T140000Z-integrator-finalize-cycle-43/CYCLE.md + cycle-043 STAGING row."
---

# CYCLE: TWO adjacent thin-identity lowering themes for axpby — L2>L1 `axpby-leaf-identity` + L3>L2 `axpby-body-identity`

## Summary

`axpby` (the fused BLAS-1 two-scalar two-vector update `y = α·x + β·y`) is firm at L1
(`book/src/L1/axpby.md`, cycle-003) and L3 (`book/src/L3/axpby.md`, cycle-011), and is being
floored at L2 this cycle by the wave-1 D4 harvester (`book/src/L2/axpby.md`) as a thin
identity-in-form leaf-floor — the **arity-2 member of the firm `linear_combination` fold**
(`linear_combination.md:70`), cited but NOT merged (fold-cohort boundary load-bearing). This
dispatch (D7, wave-2) authors the **two adjacent thin-identity lowering themes** that close
`axpby`'s downward edges across that floor: `axpby-leaf-identity` (L2>L1) and `axpby-body-identity`
(L3>L2). Both are **identity-in-form on the leaf, with no wrapper rotation** — `axpby` is a
quaternary leaf field operation, not a step body, so there is no `(op, K, s)`→`IterState`
consolidation and no outer-loop dissolution to perform (the two adjustments the sibling
`krylov-step-body-identity` carries at its wrapper have no analog here). The single fusion
content `axpby` carries — the arity-2 single-aligned `add(α, x, β, y, y)` pass — is **the
`linear_combination` fold-parent's** (its §"Fusion note"), deferred there, not re-authored on
either leaf edge; the output-aliasing variant axis is likewise the FOLD's. `axpby` is **L3-native
by signature shape** (named explicitly in the seven-primitive list at
`krylov-step-body-identity.md:97`), so the iteration rotation is already complete at the
signature level and the L3>L2 body edge is the identity. The pair mirrors the `dot`/`scal`
sibling precedents exactly, using the dispatch-ratified `-leaf-identity`/`-body-identity` slug
convention uniformly (resolving the cycle-041 `-fold-specialization` slug-split the batch-12
meta-phase flagged as an outlier).

## Proposed changes

```new:book/src/L2-L1/axpby-leaf-identity.md
# axpby-leaf-identity

The L2>L1 lowering theme for the `axpby` fused two-scalar two-vector update leaf. The rewrite is
**identity-in-form on the leaf**: the L2 [`axpby`](../L2/axpby.md) leaf-floor lowers to the L1
[`axpby`](../L1/axpby.md) primitive with the same signature, the same fused `α·x + β·y` semantics,
and the same algebraic laws — value-thread-isomorphic on the primitive. The L2 layer's
fusion-rotation work for the scalar-weighted-vector-sum family is **not on this leaf**; the only
fusion content `axpby` carries (the arity-2 single-aligned `add(α, x, β, y, y)` pass) is the
arity-2 case of the **fold-parent**'s fusion note, carried by
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) for the
whole arity family. This theme records the identity edge and defers the fusion treatment to the
fold-parent — the direct arity-2 analogue of the sibling
[`scal-fold-specialization`](./scal-fold-specialization.md) (the arity-1 single-term shadow) and
[`dot-leaf-identity`](./dot-leaf-identity.md) (the reduce-to-scalar leaf edge).

## Slug

`axpby-leaf-identity`

## Context

`axpby` at L2 is the **leaf-floor** entry (`book/src/L2/axpby.md`, harvested cycle-043 D4): the
arity-2 member of the L2 fold-parent [`linear_combination`](../L2/linear_combination.md), rendered
as its own same-named L2 chapter so the firm L3 [`axpby`](../L3/axpby.md) leaf (cycle-011) rests on
an adjacent same-named L2 parent (per CLAUDE.md §Methodology invariants **Identity-lowerings still
require both L levels**) rather than skipping a layer to L1. This theme is the L2>L1 edge of that
floor.

The edge is the **identity-in-form** case: the L2 `axpby` leaf and the L1 `axpby` leaf are
value-thread-isomorphic on the primitive (the L1 signature is whole-tensor in / whole-tensor out
with no element loop exposed; the L2 floor is authored value-thread-isomorphic to it). This is the
L2>L1 analogue of the L3>L2 [`axpby-body-identity`](../L3-L2/axpby-body-identity.md) theme (the
other thin edge of the same leaf), and a sibling shape to the arity-1
[`scal-fold-specialization`](./scal-fold-specialization.md) and the reduce-to-scalar
[`dot-leaf-identity`](./dot-leaf-identity.md).

**Why this edge is identity while its fold-parent sibling carries the fusion.** The L2 fusion
rotation for the scalar-weighted-vector-sum cohort — the arity-dispatch selection rule
(length-1/2/2/3 picking `scal`/`axpy`/`axpby`/`axpbypcz`), the `axpy`-vs-`axpby` sub-selection on
the unit-coefficient test, the arity-3 → arity-2 fall-through on the in-source `γ==0` branch, and
the pinned-summation-order table — is **the fold-parent's job**. The firm
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) theme
carries all of it for the whole arity family. `axpby` is the **arity-2 member** of that fold
(`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`, `linear_combination.md:70`,
§Algebraic-laws law 6). Restricting the fold-parent's fusion content to the arity-2 leaf leaves
**one fusion note unique to `axpby`** — the single aligned strided pass computing `α·x[i] + β·y[i]`
per element (the real-real path realized at L0 by MFEM's `add(α, x, β, y, y)` 5-arg in-place
linear-combine, `palace/linalg/vector.cpp:726-730`) — but that note **is itself the arity-2 case
of the fold's §"Fusion note"**, deferred there, not re-authored on this leaf. So the `axpby`
leaf's own L2>L1 edge — the rotation between the L2 `axpby` chapter and the L1 `axpby` chapter — is
the identity, with the fusion treatment deferred to the fold-parent.

## L2 form (LHS)

The L2 form is the `axpby` leaf-floor (`book/src/L2/axpby.md` §Signature, harvested cycle-043 D4) —
the fused two-scalar two-vector linear-combination primitive:

    axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpby α x β y = α·x + β·y

Pure / out-of-place; two scalars `α, β` and two input tensors `x, y` of one shared length axis `N`;
result of the same axis `N` with `result[i] = α·x[i] + β·y[i]` for every `i ∈ [0, N)`.
Element-local, reduction-free, rank-local. At L2 `axpby` is the **base fused two-scalar two-vector
leaf** — and **also** the arity-2 member of the variadic
[`linear_combination`](../L2/linear_combination.md) fold
(`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`, `linear_combination.md:70`,
§Algebraic-laws law 6), cited as fold-parent but NOT merged. The only fusion note the floor entry
carries is the **arity-2 case of the fold's fusion note**: the single aligned strided pass
computing `α·x[i] + β·y[i]` per element (the seed-and-accumulate fold collapsed to two terms).

The L2 form is **pure / out-of-place** (no destination buffer; the result is a fresh `Tensor[N]`).
The output-aliasing forms (`y ← α·x + β·y`, where the `y` term aliases the output buffer) are NOT
in the L2 signature — the output-aliasing variant axis is the **FOLD's**
(`linear_combination.md` §Variant-axes axis 1), orthogonal to arity; in-place reappears only at the
L1>L0 lowering ([`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md)).

## L1 form (RHS)

The L1 form is the firm `axpby` leaf primitive (`book/src/L1/axpby.md` §Signature, firm cycle-003) —
identical in signature, semantics, and laws:

    axpby :: (α: Scalar, x: Tensor[N], β: Scalar, y: Tensor[N]) -> Tensor[N]
    axpby(α, x, β, y) = α·x + β·y

The L1 leaf is the **mutation-rotation** rendering: it already erases the L0 destination buffer (the
receiver-mutating `ComplexVector::AXPBY(α, x, β)` writing through `*this`, and the output-arg
`linalg::AXPBY(α, x, β, y)` writing through `y`), preserves the fused single-pass statement
`α·x + β·y` as a primitive linear combination (not the two-pass `y *= β; y += α·x`), and collapses
the three L0 template specialisations (real-real, complex-complex, real-scalar-on-complex-vector)
into one element-type-parameterised operator. The L1 entry is authoritative on every Palace-surface
fact; the L2 form does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the leaf**. Every L2 binding maps to the same L1 binding at the
same position:

    | L2 leaf (`L2/axpby`)                              | L1 leaf (`L1/axpby`)                              | Mapping  |
    |---------------------------------------------------|---------------------------------------------------|----------|
    | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` | `axpby :: (α, x, β, y) -> Tensor[N]` | Identity. Same quaternary signature shape (curried arrow vs positional-tuple is notational only). |
    | `axpby α x β y = α·x + β·y`                        | `axpby(α, x, β, y) = α·x + β·y`                    | Identity. Same fused two-scalar two-vector body. |
    | per-element kernel `α·x[i] + β·y[i]`              | per-element kernel `α·x[i] + β·y[i]`              | Identity. Same element-local, reduction-free, rank-local relation. |
    | nine algebraic laws (subsumption / three identities / bilinearity / two distributions / scalar absorption / chained-collapse) | nine algebraic laws | Identity. Inherited unchanged (linear-combination facts + the four non-laws). |
    | two variant axes (element-type + scalar-promotion sub-axis) | two variant axes | Identity. Same profile; both absorbed at construction. |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the
mapping is total and bijective on the leaf. This is the identity-in-form property.

**The one note (fusion deferral).** The L2 layer's defining work is kernel-fusion de-fusion. For the
scalar-weighted-vector-sum cohort, that work is carried entirely by the fold-parent
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md): the
arity-dispatch selection rule, the `axpy`-vs-`axpby` sub-selection, the arity-3 → arity-2
fall-through on the in-source `γ==0` branch (`palace/linalg/vector.cpp:745-758`), and the
pinned-summation-order table. `axpby` is the **arity-2 member** of that fold; its single fusion note
(the arity-2 single-aligned `add(α, x, β, y, y)` pass, `palace/linalg/vector.cpp:726-730`) is the
arity-2 case of the fold's §"Fusion note", deferred there. So this theme's edge is the identity, and
bit-reproduction / summation-order concerns are read off the fold-parent theme's pinned-order table,
not re-derived here. **Unlike the arity-1 `scal-fold-specialization`** (value-exact AND bit-exact
unconditionally — one term, one rounding, no sum to re-associate), `axpby`'s arity-2 fused pass IS a
two-term sum: the value is order-agnostic, but bit-identical reproduction of L0 output requires
matching the L0 evaluation order pinned by `add(α, x, β, y, y)` — recorded as a non-law (inherited
from both leaves), the arity-2 shadow of the fold's summation-order load-bearing concern.

## Applicability conditions

The identity rewrite is valid when:

1. **The L2 `axpby` is the leaf-floor realization** (`book/src/L2/axpby.md`, the same-named arity-2
   leaf of `linear_combination`) — NOT the fold-parent. If the L2 scalar-weighted-vector-sum surface
   were the fold-only realization (no `axpby` leaf at L2 — the wave-1 D2 "fold-only" reading), this
   theme's LHS would not exist as a standalone L2 `axpby` chapter, and the L2>L1 edge for `axpby`
   would be subsumed into [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md)'s
   arity-2 row. This condition records the design presupposition explicitly (see this theme's
   authoring report §Open-questions and the batch-12 meta-phase OQ
   `dot-l2-leaf-floor-vs-fold-only-design`).

2. **The leaf is value-thread-isomorphic across the edge.** The L2 `axpby` leaf and the L1 `axpby`
   leaf share the quaternary signature, the fused `α·x + β·y` body, the per-element kernel, the nine
   algebraic laws, the four non-laws, and the two variant axes. Confirmed by construction:
   `L2/axpby` is authored as a thin floor entry whose laws are inherited unchanged from `L1/axpby`
   (D4 §"Algebraic laws", §Signature).

3. **All multi-operation fusion content is the fold-parent's.** The single fusion note unique to
   `axpby` (the arity-2 single-aligned `add(α, x, β, y, y)` pass) is itself the arity-2 case of the
   fold-parent's §"Fusion note"; no fusion structure beyond it exists on the leaf (the fused
   `α·x + β·y` pass is **not** unfolded into a two-pass `scal(β, y)` then `axpy(α, x, ·)` chain — the
   `axpby-as-primitive` decision keeps the leaf firm, fuse don't decompose). The leaf's edge is
   therefore the identity with a single deferring note.

If a future L2 `axpby` variant introduced leaf-specific fusion not absorbed by the fold-parent, the
identity claim would need re-audit — none exists in the current surface.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `axpby` leaf's signature shape
(`Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`) is identical to the L1 `axpby` leaf's
signature shape — a whole-tensor fused two-scalar two-vector update with no element loop exposed at
either layer. The rotation between two value-thread-isomorphic leaves with identical signatures is
the identity by construction; the only L2-layer work (fusion de-fusion) is carried by the
fold-parent, leaving the leaf's own edge a no-op modulo the one deferred fusion note. A secondary
`algebraic` flavour is inherited from the fold-parent: the arity-2 membership identity
`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]` IS `linear_combination.md` law 6 read at
length 2 — but because the leaf's own edge carries no arity dispatch (there is exactly one fixed
arity), the governing justification is the structural identity-in-form on the leaf, with the
fold-membership identity as the secondary anchor.

**Empirical-match (secondary)**: the L1 leaf is firm on direct Palace evidence (`L1/axpby`
§Evidence — three L0 template specialisations in `palace/linalg/vector.{hpp,cpp}`), and the L2
leaf-floor was authored as value-thread-isomorphic to it; the two forms agree on every law and
every variant axis by independent transcription. The identity is observational on the two existing
firm/firming chapters, not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `axpby` leaf-floor (firming
cycle-043 D4), the L1 RHS is the firm `axpby` leaf (firm cycle-003). This theme is the identity
edge between existing chapters; it proposes no new operators. The fold-parent
[`linear_combination`](../L2/linear_combination.md) is firm (cycle-018); `axpby`'s arity-2
membership is a cited fold-specialization, not a new operator.

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/axpby.md` (firming cycle-043 D4) — the L2 leaf-floor (LHS): the same-named arity-2
  leaf of `linear_combination`, value-thread-isomorphic to the L1 leaf, laws inherited unchanged.
  (The chapter lands at this cycle's integration alongside this theme — wave-2 serial sequencing
  applies D4 before this theme.)
- `book/src/L1/axpby.md` (firm cycle-003) — the L1 leaf (RHS): signature (`:16-18`), the fused
  `α·x + β·y` body, the nine algebraic laws (`:42-53`), the four non-laws (`:56-60`), the two variant
  axes (element-type + scalar-promotion sub-axis, `:72-77`), the complete L0 evidence list
  (`:90-99`). Authoritative on every Palace-surface fact.
- `book/src/L2/linear_combination.md:70` (firm cycle-018) — the arity-2 specialization identity
  `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]` (§Signature line 70; §Algebraic-laws
  law 6). The fold-parent membership anchor; cited, NOT merged.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (cycle-018/019 firm) — the fold-parent
  theme this leaf's fusion content defers to: the arity-dispatch selection rule, the
  `axpy`-vs-`axpby` sub-selection, the arity-3 → arity-2 fall-through, the pinned-summation-order
  table. `axpby` is the arity-2 member of that fold's selection.
- `book/src/L2-L1/scal-fold-specialization.md` (cycle-041 D6 firm) + `book/src/L2-L1/dot-leaf-identity.md`
  (cycle-041 firm) — the sibling L2>L1 floor-edge themes this entry's structure mirrors (same
  identity-in-form leaf-floor pattern, same fold-membership-cited-not-merged framing, same
  fusion-deferred-to-fold-parent treatment). `scal` is the arity-1 single-term shadow; `axpby` is
  the arity-2 member of the same fold.
- `book/src/L2/index.md` §"Fold-cohort boundary" — the load-bearing do-NOT-merge boundary between
  the leaf and the fold; line 17 names the BLAS-1 base-primitive vocabulary.

Onward L1>L0 lowering (the in-place mutation this L2/L1 pure edge abstracts over):

- `book/src/L1-L0/axpby-mutation-rotation.md` (firm cycle-002) — the L1>L0 mutation rotation; the
  in-place receiver-mutating / output-arg `AXPBY` idioms the L2 floor and L1 leaf both abstract over
  (the `axpby` LHS is the rough-in row promoted firm at L1 cycle-003).

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — this edge is
identity-in-form, so L0 evidence is transitive through L1; paths relative to `reference/palace/`):

- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member decl (the receiver-mutating
  member form `(*this) = α·x + β·(*this)`).
- `palace/linalg/vector.hpp:309-311` — free-function template `AXPBY(ScalarType α, const VecType &x,
  ScalarType β, VecType &y)` (the bounded-arity surface the fold unifies).
- `palace/linalg/vector.cpp:726-730` — real-real `AXPBY` → MFEM `add(α, x, β, y, y)` (the arity-2
  single-aligned fused pass; the fusion-note witness, deferred to the fold-parent).
- `palace/linalg/vector.cpp:732-737` — complex-complex `AXPBY` → member form `y.AXPBY(α, x, β)`.
- `palace/linalg/vector.cpp:739-743` — real-scalar-on-complex-vector `AXPBY` (the scalar-promotion
  sub-axis L0 anchor).

## Status

`firm` — the L2 LHS is the firm-this-cycle leaf-floor (D4 wave-1), the L1 RHS is the firm `axpby`
leaf (cycle-003), and the rotation between two value-thread-isomorphic leaves with identical
quaternary signatures is the identity by construction (§"The rewrite (L2 → L1)" table is total and
bijective on the leaf). The only L2-layer work — kernel-fusion de-fusion for the
scalar-weighted-vector-sum cohort — is carried by the firm fold-parent
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md); `axpby`'s
single fusion note (the arity-2 single-aligned `add(α, x, β, y, y)` pass) is the arity-2 case of the
fold's §"Fusion note", deferred there. No speculative operator, no negative-anchor reconstruction,
no literature inference. The arity-2 member of the BLAS-1 floor-edge cohort: thicker than the arity-1
`scal-fold-specialization` (its fused pass IS a two-term sum, so the summation-order non-law is
non-degenerate), thinner than the fold-parent (it carries no arity dispatch — exactly one fixed
arity).

> **Design-presupposition note (not a status reduction).** This theme presupposes the **(b)
> same-named leaf-floor** realization of `L2/axpby` (Applicability condition 1). Under the wave-1 D2
> "fold-only" reading (no `axpby` leaf at L2), this theme's LHS would not exist standalone and the
> edge would fold into `linear-combination-fold-specialization`'s arity-2 row. The c042 cross-cutter
> audit recommends KEEPING leaf-floor (b) (`book/src/L2/index.md` §Working-Notes). Surfaced for the
> batch-12 meta-phase to adjudicate (OQ `dot-l2-leaf-floor-vs-fold-only-design`); the theme is
> self-coherent under the leaf-floor reading it is built on.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L1 leaf *up* to the L2 floor is the value-thread-isomorphic identity rotation: the L1
  signature has no kernel fusion exposed beyond the single fused pass, no destination buffer, no MPI
  collective — exactly the properties that make it L2-native by construction. No additional structure
  is required for the lift. This reverse-direction note lives here in working notes per the high→low
  layer-definition discipline; the formal chapter narrates only L2 → L1.

- **Leaf-vs-fold fork (batch-12 meta-phase adjudication).** See §Status design-presupposition note;
  recorded as the cross-CYCLE OQ `dot-l2-leaf-floor-vs-fold-only-design`. `axpby` rides the same fork
  as `dot`/`scal` (it is a fold-parented floor); the c042 cross-cutter audit recommends keeping
  leaf-floor (b).
```

```new:book/src/L3-L2/axpby-body-identity.md
# axpby-body-identity

The L3>L2 lowering theme for the BLAS-1 leaf `axpby`. The rewrite is **identity-in-form on the
body** with **no wrapper rotation** — `axpby` is a leaf whole-tensor field operation (the fused
two-scalar two-vector update `α·x + β·y`), not a step body, so the L3 whole-tensor form lowers into
the L2 floor form by the identity on the primitive itself. There is no `(op, K, s)`→`IterState`
consolidation and no outer-loop dissolution to perform (the two surface adjustments that the sibling
[`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper); `axpby` has
no wrapper. The body IS the identity. `axpby` is one of the seven BLAS-1 primitives that are
**L3-native by signature shape** (no per-element loop visible at either layer), so the iteration
rotation is already complete at the signature level and the L3>L2 body edge is the identity. This is
the arity-2 analogue of [`scal-body-identity`](./scal-body-identity.md) (the arity-1 leaf) and
[`dot-body-identity`](./dot-body-identity.md) (the reduce-to-scalar leaf), and the leaf-primitive
counterpart of `krylov-step-body-identity` (which is identity-in-form on a multi-primitive kernel
body); here the identity is on a single leaf.

## Slug

`axpby-body-identity`

## Context

The `axpby` lowering relationships span three adjacent layers, all identity-in-form because `axpby`
is a BLAS-1 leaf with no iteration view and (beyond the deferred arity-2 single-aligned pass) no
kernel fusion:

- **L3 form** ([`L3/axpby`](../L3/axpby.md), firm cycle-011) — the whole-tensor fused field
  operation `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`, the
  iteration-rotation rendering. Carries **no iteration view** (leaf primitive, not a step body) and
  **no sequential obstruction** (every element independent under the per-element `α·x[i] + β·y[i]`).
  The LHS of this theme. Consumed inside `krylov-step`'s iterate-stratum update.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/axpby`](../L2/axpby.md), firming cycle-043 D4) — the fusion-rotation floor leaf,
  the base fused two-scalar two-vector primitive and the arity-2 member of the `linear_combination`
  fold. The RHS of this theme.
- **L2>L1 form** ([`L2-L1/axpby-leaf-identity`](../L2-L1/axpby-leaf-identity.md), firming cycle-043
  D7) — the onward edge into the L1 leaf; also identity-in-form (the fold's arity-2 row, fusion
  deferred to the fold-parent). Co-dispatched this cycle.

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009). The `krylov-step`
theme establishes the pattern "identity-in-form on the kernel **body**, with surface adjustments at
the **wrapper**"; its point-3 applicability condition names the seven L1 primitives — including
**`axpby`** — as L3-native by signature shape: "each operates on whole-tensor inputs with no
element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than
requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no
per-element loop visible)" (`krylov-step-body-identity.md:97`, which lists `axpby` explicitly among
`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`). This theme is the standalone-leaf
realization of that classification for `axpby`: the body is the identity, **and there is no wrapper
at all** — `axpby` is not a step body, so the two wrapper adjustments the `krylov-step` theme carries
(the `(op, K, s)`→`IterState` consolidation and the outer-loop-to-driver-by-role dissolution) have
no analog here.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/axpby`](../L3/axpby.md) §Signature):

    axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpby α x β y = α·x + β·y

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `α, β` scalars
(`real` or `complex`, or `real` promoted against complex `x, y`); `x, y : Tensor[N]` a single shared
length axis, read-only at L3; result `Tensor[N]` of the same axis with
`result[i] = α·x[i] + β·y[i]` for every `i ∈ [0, N)`. The operator carries **no iteration view** (it
is a leaf field operation, not a step body) and **no sequential obstruction** (every element is
independent of every other under the per-element fused update — embarrassingly parallel, fully
GPU-friendly). No L4 wrapper machinery applies (leaf primitives appear inside L4 operator bodies as
let-bindings, not as first-class L4 typed-wrapper anchors — the cross-layer-cross-cutter "L4
candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort; `L3/axpby.md` §"Lifts from").

## L2 form (RHS)

The L2 floor form ([`L2/axpby`](../L2/axpby.md) §Signature, firming cycle-043 D4):

    axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpby α x β y = α·x + β·y

The base fused two-scalar two-vector leaf in the fusion-rotation vocabulary — **and** the arity-2
member of the [`linear_combination`](../L2/linear_combination.md) fold
(`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`, `linear_combination.md:70`, cited NOT
merged). The signature is **textually identical to the L3 form** modulo notation; the body is the
same single whole-tensor fused field operation. The nine algebraic laws hold unchanged across the
edge (L3 §Algebraic laws ≡ L2 §Algebraic laws — both inherit the L1 leaf's nine laws). The only
fusion note the L2 floor carries is the arity-2 single-aligned `add(α, x, β, y, y)` pass (the
arity-2 case of the fold's §"Fusion note", deferred to the fold-parent); at L3 even that note is
absent (L3 exposes no element loop at all).

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    axpby α x β y   (L3 whole-tensor field op)   ⇒   axpby α x β y   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow. Every L3 binding
maps to the same L2 binding at the same position:

    | L3 leaf (`L3/axpby`)                              | L2 leaf (`L2/axpby`)                              | Mapping  |
    |---------------------------------------------------|---------------------------------------------------|----------|
    | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` | Identity. Same whole-tensor quaternary signature. |
    | `axpby α x β y = α·x + β·y` (whole-tensor field op; no iteration view) | `axpby α x β y = α·x + β·y` (base fused leaf; arity-2 fold member) | Identity. Same single fused field operation. The only framing difference is documentary: L3 frames `axpby` as a whole-tensor field operation in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive (and the arity-2 fold member). No operational adjustment occurs. |
    | per-element kernel `α·x[i] + β·y[i]`              | per-element kernel `α·x[i] + β·y[i]`              | Identity. Same element-local, reduction-free, rank-local relation. |
    | nine algebraic laws + four non-laws               | nine algebraic laws + four non-laws               | Identity. Inherited unchanged across the chain. |
    | no sequential obstruction                         | no sequential obstruction                         | Identity. Leaf field op at both layers; the pinned summation order of the arity-2 fused pass is an L0 non-law, not an L2/L3 structural element. |

The mapping is total and bijective on the leaf body: every L3 binding has an L2 partner and every L2
binding has an L3 partner. This is the **identity-in-form** property.

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body: (1) the L3 `(op, K, s)` positional tuple
consolidates into the L2 unified `IterState` record (state-hiding), and (2) the L3 tail-recursive
outer loop `iterate_while_L3` collapses to the L2 outer-driver-by-role reference
(abstraction-by-role). **Neither has an analog for `axpby`**: `axpby` is a single leaf field
operation, not a step body with an `(op, K, s)` carrier and an outer loop. There is no `IterState`
(no state record — `axpby` is a pure positional function), and there is no outer driver (no loop
folds `axpby` calls at the operator itself; `axpby` is *called by* step bodies like `krylov-step`'s
`krylov_update`, but those loops belong to the step body, not to `axpby`). The mapping is total and
bijective on a single binding — the degenerate maximal case of the identity-in-form property.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `axpby` endpoints) when:

1. **`axpby` is L3-native by signature shape.** Its signature
   `Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` exposes no per-element loop at L2 or
   L3; the fused update over the length axis `N` is a single semantic step at both layers. This is
   the load-bearing condition (per `krylov-step-body-identity.md:97`, which names `axpby` among the
   seven L3-native primitives). Satisfied by construction: `axpby` is a leaf field operation.

2. **The L2 form is the same-named leaf-floor** (`book/src/L2/axpby.md`), value-thread-isomorphic to
   the L3 leaf. If the L2 scalar-weighted-vector-sum surface were the fold-only realization (no
   `axpby` leaf at L2 — the wave-1 D2 reading), the L3 leaf's adjacent L2 parent would be the
   fold-parent `linear_combination` (the L3>L2 edge would lower to the fold's arity-2 form, not to a
   same-named L2 `axpby`), and this theme's RHS would re-anchor. This condition records the design
   presupposition explicitly (see this theme's authoring report §Open-questions and the batch-12
   meta-phase OQ `dot-l2-leaf-floor-vs-fold-only-design`).

3. **`axpby` is treated as a leaf primitive, not decomposed.** `axpby` does not decompose into other
   L3 or L2 primitives — the fused `α·x + β·y` pass is a single field operation; its sub-operations
   (two scalar multiplies, one element-wise add) are below both layers' resolution, and the fusion
   preserves the algebraic statement `α·x + β·y` as a primitive linear combination (the
   `axpby-as-primitive` decision,
   [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md);
   fuse, don't decompose into `scal ∘ axpy`).

4. **No iteration view, no sequential obstruction.** `axpby` is element-local, reduction-free,
   rank-local; every element is independent. There is no outer loop, no carry trajectory, no
   recurrence — so there is nothing for the L3 iteration rotation to have rotated and nothing for the
   L3>L2 lowering to dissolve.

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape
`Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` is whole-tensor by construction at both
layers — no element loop is exposed at L2, no iteration view at L3. The L3 vocabulary at this scope
demands whole-tensor field operations with no element loop exposed; `axpby` satisfies this *at L2
already*, so the rotation is the identity. This is the same structural argument the
`krylov-step-body-identity` theme makes as its point-3 condition for each primitive in the kernel
body — here promoted to dominant because there is no kernel body wrapping the leaf, only the leaf
itself.

**Empirical-match (secondary)**: the cross-layer-cross-cutter identity-in-form audit
(`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) the
BLAS-1 cohort") classified the `axpby` L3↔L1 rotation as identity-in-form by inspection of the firm
L3 entry and the firm `krylov-step-body-identity`; the firm `krylov-step-body-identity` names
`axpby` L3-native at line 97. This theme's L3>L2 edge is the standalone-leaf realization of that
audited classification, now that the L2 floor entry exists (cycle-043 D4) for the rotation to target.
The L3 LHS and L2 RHS were authored independently (L3 cycle-011, L2 cycle-043 D4) as
value-thread-isomorphic to the same firm L1 leaf, and they agree on every law and every variant axis
by independent transcription.

## Speculative L2 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/axpby`](../L3/axpby.md)) is firm (cycle-011), and the L2 RHS ([`L2/axpby`](../L2/axpby.md)) is
firming (cycle-043 D4). No new L2 vocabulary is introduced. `axpby` does not get its own L4
typed-wrapper anchor (leaf primitives appear inside L4 operator bodies as let-bindings — the
cross-layer-cross-cutter "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort), so there
is no upstream L4>L3 theme for `axpby` either; the L3 form is L3-native by signature and this theme
closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/axpby.md` (cycle-011 firm) — the L3 whole-tensor form (LHS). Signature (`:30-32`),
  semantics (element-local, reduction-free, rank-local, no iteration view, no sequential
  obstruction; `:51-65`), nine algebraic laws (`:67-88`), the leaf-not-step-body
  §"Iteration-rotation marker" (`:63-65`), two variant axes (`:103-110`). The §"Lowers to"
  (`:116-120`) currently records identity-in-form to L1 (no L2 chapter existed); this theme supplies
  the now-present adjacent L3>L2 edge (downstream-consistency touch on the L3 entry's §"Lowers to"
  framing flagged in §Open-questions of the authoring report — the c044 L3-staleness sweep).
- `book/src/L2/axpby.md` (firming cycle-043 D4) — the L2 floor form (RHS): the same-named arity-2
  leaf of `linear_combination`, value-thread-isomorphic to the L1/L3 leaf, laws inherited unchanged.
  (Lands at this cycle's integration alongside this theme.)
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-007/009 firm) — §"Applicability
  conditions" point 3: the load-bearing statement that the seven BLAS-1 primitives (including
  **`axpby`**, named explicitly) are L3-native by signature shape (no per-element loop visible),
  which is the structural justification for this identity edge. **Self-verified (anchor `axpby`
  @97 via `tools/citecheck/citecheck.py`).**
- `book/src/L2/linear_combination.md:70` (cycle-018 firm) — the arity-2 specialization identity
  `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`. The fold-parent membership anchor; cited,
  NOT merged.
- `book/src/L3-L2/scal-body-identity.md` (cycle-041 firm) + `book/src/L3-L2/dot-body-identity.md`
  (cycle-041 firm) — the sibling L3>L2 body-identity themes this entry's structure mirrors (same
  no-wrapper leaf-primitive analogue of `krylov-step-body-identity`). `scal` is the arity-1 leaf;
  `axpby` is the arity-2 member of the same fold.

Cross-layer audit (the empirical-match anchor):

- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) the
  BLAS-1 cohort" — the HIGH CONFIDENCE classification of the `axpby` rotation as identity-in-form,
  the dispatch rationale for the cycle-011 L3 `axpby` backfill and (now) this L3>L2 edge.

Onward edges (cross-reference, not this theme's content):

- `book/src/L2-L1/axpby-leaf-identity.md` (cycle-043 D7) — the onward L2>L1 edge into the L1 leaf;
  also identity-in-form (the fold's arity-2 row, fusion deferred to the fold-parent). Co-dispatched
  this cycle.
- `book/src/L1/axpby.md` (cycle-003 firm) + `book/src/L1-L0/axpby-mutation-rotation.md` (firm
  cycle-002) — the L1 leaf and its in-place L0 mutation rotation, reached via the onward edge.

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — identity-in-form edge,
L0 evidence transitive through L1; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:726-730` — real-real `AXPBY` → MFEM `add(α, x, β, y, y)` (the arity-2
  single-aligned fused pass).
- `palace/linalg/vector.cpp:732-737` — complex-complex `AXPBY` → member form `y.AXPBY(α, x, β)`.
- `palace/linalg/vector.hpp:130-131,309-311` — `ComplexVector::AXPBY` member decl + the free-function
  template `AXPBY` decl.

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/axpby`](../L3/axpby.md)) is firm (cycle-011); the L2 RHS ([`L2/axpby`](../L2/axpby.md)) is
firming (cycle-043 D4). The body is the identity rotation on a single leaf field operation; **there
is no wrapper to rotate** (no `(op, K, s)`→`IterState` consolidation, no outer-loop dissolution —
`axpby` is a leaf, not a step body). The structural justification (whole-tensor quaternary signature,
no element loop, no iteration view) is the `krylov-step-body-identity` point-3 condition specialized
to the standalone leaf and promoted to dominant; the empirical-match anchor is the firm cross-layer
audit + the `krylov-step-body-identity:97` L3-native classification (which names `axpby` explicitly).
No speculative operator, no negative-anchor reconstruction, no sequential obstruction. The arity-2
member of the BLAS-1-leaf L3>L2 cohort — the leaf-primitive counterpart of `krylov-step-body-identity`
alongside `dot-body-identity` (reduce-to-scalar) and `scal-body-identity` (arity-1).

> **Design-presupposition note (not a status reduction).** This theme presupposes the wave-1 **(b)
> same-named leaf-floor** realization of `L2/axpby` (Applicability condition 2). Under the wave-1 D2
> "fold-only" reading (no `axpby` leaf at L2), this theme's RHS would re-anchor to the fold-parent
> `linear_combination` (the arity-2 form). The c042 cross-cutter audit recommends KEEPING leaf-floor
> (b) (`book/src/L2/index.md` §Working-Notes). Surfaced for the batch-12 meta-phase to adjudicate (OQ
> `dot-l2-leaf-floor-vs-fold-only-design`); the theme is self-coherent under the leaf-floor reading it
> is built on.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the value-thread-isomorphic identity
  rotation: the L2 signature has no element loop exposed, which is exactly what makes it L3-native by
  construction. No additional structure is required for the lift. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter narrates only
  L3 → L2.

- **Leaf-vs-fold fork (batch-12 meta-phase adjudication).** See §Status design-presupposition note;
  recorded as the cross-CYCLE OQ `dot-l2-leaf-floor-vs-fold-only-design`. `axpby` rides the same fork
  as `dot`/`scal` (fold-parented floor); the c042 cross-cutter audit recommends keeping leaf-floor
  (b).

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `axpby-leaf-identity` identity) is annotated in-line at the
  `axpby` entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are
  annotated in-line, not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This
  theme + the co-dispatched `axpby-leaf-identity` compose to capture it.

- **L3/axpby §"Lowers to" staleness (c044 sweep, NOT here).** The firm `book/src/L3/axpby.md`
  (cycle-011) §"Lowers to" (`:116-120`) records identity-in-form straight to L1 ("no L2 intermediate
  because the BLAS-1 primitives are L1 leaves not L2 compositions"), which predates the L2 floor. Now
  that the adjacent L2 `axpby` floor + this L3>L2 edge exist, that framing is stale — the L3 form
  should lower to the present adjacent L2 floor, not skip to L1. This is the same c044 L3-staleness
  sweep item the D4 harvester surfaced (re-anchor the L3 BLAS-1 cohort `lowers_to` framing to the new
  L2 floors); **not in scope here** (modifying the L3 entry is the harvester's job, not the
  abstractor's). Surfaced for the OQ ledger.
```

```edit:book/src/L2-L1/index.md
| [scal-fold-specialization](./scal-fold-specialization.md) | `L2/scal` (firm, cycle-041 D3) | `L1/scal` (firm leaf, cycle-004) | firm *(structural; identity-in-form floor edge — the degenerate arity-1 single-term shadow of `linear-combination-fold-specialization`; no arity dispatch, no pinned-summation-order residue (one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged)* |
| [axpby-leaf-identity](./axpby-leaf-identity.md) | `L2/axpby` (firming, cycle-043 D4 floor) | `L1/axpby` (firm leaf, cycle-003) | firm *(structural; identity-in-form floor edge — the **arity-2 member** of `linear-combination-fold-specialization` (cited NOT merged); thicker than `scal-fold-specialization` (its arity-2 fused `add(α,x,β,y,y)` pass IS a two-term sum, so the summation-order non-law is non-degenerate), thinner than the fold-parent (no arity dispatch — one fixed arity); single fusion note (the arity-2 single-aligned pass) is the fold's §"Fusion note", deferred there; output-aliasing axis is the FOLD's; rides the batch-12 leaf-vs-fold fork (c042 audit recommends keeping leaf-floor (b)))* |
```

```edit:book/src/L2-L1/index.md
- `scal-fold-specialization` — the L2 `scal` floor lowers to the L1 `scal` leaf; the degenerate **arity-1 single-term shadow** of `linear-combination-fold-specialization` (no arity dispatch, no pinned-summation-order residue — one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged.
- `axpby-leaf-identity` — the L2 `axpby` floor lowers to the L1 `axpby` leaf identity-in-form; the **arity-2 member** of `linear-combination-fold-specialization` (cited NOT merged) — thicker than `scal-fold-specialization` (its arity-2 fused `add(α,x,β,y,y)` pass IS a two-term sum, so the summation-order non-law is non-degenerate), thinner than the fold-parent (no arity dispatch — one fixed arity); the single fusion note (the arity-2 single-aligned pass) is the fold's §"Fusion note", deferred there; output-aliasing axis is the FOLD's; rides the batch-12 leaf-vs-fold fork (c042 audit recommends keeping leaf-floor (b)).
```

```edit:book/src/L3-L2/index.md
| [`scal-body-identity`](./scal-body-identity.md) | L3 [`scal`](../L3/scal.md) §Signature — the whole-tensor field operation `scal :: Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`scal`](../L2/scal.md) §Signature — the base scalar-vector-multiply floor leaf (arity-1 member of `linear_combination`, cited NOT merged); identical signature. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-041 D6 abstractor; identity-in-form on the body, **no wrapper to rotate** — the leaf-primitive counterpart of `krylov-step-body-identity`) |
| [`axpby-body-identity`](./axpby-body-identity.md) | L3 [`axpby`](../L3/axpby.md) §Signature — the whole-tensor fused two-scalar two-vector field operation `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`axpby`](../L2/axpby.md) §Signature — the base fused-linear-combination floor leaf (arity-2 member of `linear_combination`, cited NOT merged); identical signature. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf; `krylov-step-body-identity.md:97` names `axpby` among the seven L3-native primitives) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-043 D7 abstractor; identity-in-form on the body, **no wrapper to rotate** — the arity-2 leaf-primitive counterpart of `krylov-step-body-identity` alongside `scal-body-identity`; rides the batch-12 leaf-vs-fold fork, c042 audit recommends keeping leaf-floor (b)) |
```

```edit:book/src/L3-L2/index.md
- `scal-body-identity` — the L3 whole-tensor `scal` field operation lowers to the L2 base scalar-vector-multiply floor leaf (arity-1 fold member); the body IS the identity, there is no wrapper to rotate.
- `axpby-body-identity` — the L3 whole-tensor `axpby` fused two-scalar two-vector field operation lowers to the L2 base fused-linear-combination floor leaf (arity-2 fold member); the body IS the identity, no wrapper to rotate; `axpby` is L3-native by signature shape (`krylov-step-body-identity.md:97` names it among the seven), so the iteration rotation is already done at the signature level; rides the batch-12 leaf-vs-fold fork (c042 audit recommends keeping leaf-floor (b)).
```

```edit:book/src/SUMMARY.md
- [scal-fold-specialization](./L2-L1/scal-fold-specialization.md)
- [axpby-leaf-identity](./L2-L1/axpby-leaf-identity.md)
```

```edit:book/src/SUMMARY.md
- [scal-body-identity](./L3-L2/scal-body-identity.md)
- [axpby-body-identity](./L3-L2/axpby-body-identity.md)
```

## Speculative operators proposed

**None.** Both themes are identity-in-form edges between existing vocabulary on both sides:

- `axpby-leaf-identity` (L2>L1): L2 LHS = `axpby` leaf-floor (firming cycle-043 D4, co-lands); L1 RHS
  = firm `axpby` leaf (cycle-003). No new L1 operator.
- `axpby-body-identity` (L3>L2): L3 LHS = firm `axpby` leaf (cycle-011); L2 RHS = `axpby` leaf-floor
  (firming cycle-043 D4, co-lands). No new L2 operator.

The fold-parent `linear_combination` (firm cycle-018) is cited, not extended; `axpby`'s arity-2
membership is a cited fold-specialization identity (`linear_combination.md:70`), not a new operator.

## Supporting evidence

- **Source-of-truth for the L2 `axpby` form**: `reports/2026-06-01T105425Z-cycle-043-harvester-L2-axpby/CYCLE.md`
  (wave-1 D4) — the proposed `book/src/L2/axpby.md` leaf-floor: arity-2 member of `linear_combination`
  (cited NOT merged), identity-in-form to L1, nine laws + four non-laws + two variant axes inherited,
  fusion deferred to the fold-parent, output-aliasing axis the FOLD's, firm-on-positive-structure.
- **Sibling precedents mirrored exactly**: `book/src/L2-L1/dot-leaf-identity.md` +
  `book/src/L2-L1/scal-fold-specialization.md` (L2>L1); `book/src/L3-L2/dot-body-identity.md` +
  `book/src/L3-L2/scal-body-identity.md` (L3>L2). `axpby` is the arity-2 member of the same
  fold-parented BLAS-1-leaf floor-edge cohort `scal` (arity-1) and `dot` (reduce-to-scalar) belong
  to.
- **Load-bearing structural anchor (self-verified this invocation)**:
  `book/src/L3-L2/krylov-step-body-identity.md:97` names `axpby` explicitly among the seven L3-native
  BLAS-1 primitives — `python3 tools/citecheck/citecheck.py book/src/L3-L2/krylov-step-body-identity.md:97 --anchor 'axpby'`
  → `[ok] anchor 'axpby' at line 97`.
- **Fold-parent membership anchor (self-verified this invocation)**: `book/src/L2/linear_combination.md:70`
  carries `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]` (confirmed on-disk via `sed -n
  '68,72p'`: line 70 is the `axpby` row of the §Signature specialization table).
- **L0 evidence transitive through the firm L1 leaf** (`book/src/L1/axpby.md` §Evidence): the three
  `AXPBY` template specialisations + the member form in `palace/linalg/vector.{hpp,cpp}`. Both edges
  are identity-in-form, so L0 evidence is inherited, not re-localized.

## Open questions / caveats

- **COUNT-OWNERSHIP (deferred to D2, per dispatch).** This report appends ONLY the two theme rows
  (one to `L2-L1/index.md` after the `scal-fold-specialization` row, one to `L3-L2/index.md` after the
  `scal-body-identity` row), the two SUMMARY registrations, and the two theme bodies. It does **NOT**
  touch the consolidated firm running-count tallies / cohort-growth-log totals in either lowering
  Part's §"Working Notes" — D2 owns the consolidated tallies this cycle. The integrator should
  reconcile the absolute firm counts (L2-L1: 15 firm + 1 partly-constructive → 16 firm + 1 with
  `axpby-leaf-identity`; L3-L2: 10 firm → 11 firm with `axpby-body-identity`) when D2's tally lands;
  do not increment from this report.

- **Slug convention (ratified `-leaf-identity`/`-body-identity`).** Per dispatch, both themes use the
  uniform `-leaf-identity`/`-body-identity` slugs (mirroring `dot-leaf-identity`/`dot-body-identity`),
  NOT the `-fold-specialization` slug `scal` used at L2>L1. This is consistent with the batch-12
  meta-phase signal flagging the cycle-041 `-fold-specialization` slugs (`scal`/`nrm2`) as the
  outliers among structurally-similar identity edges; the cycle-042 cohort used `-leaf-identity`
  uniformly, and this dispatch continues that normalization. (Whether to retroactively rename the two
  cycle-041 `-fold-specialization` files is a meta-phase normalization decision, not in scope here.)

- **Leaf-vs-fold fork (`dot-l2-leaf-floor-vs-fold-only-design`).** Both themes presuppose the **(b)
  same-named leaf-floor** realization of `L2/axpby` (the realization D4 builds). `axpby` is a
  fold-parented floor (arity-2 member of `linear_combination`), so it rides the same batch-12 fork as
  `dot`/`scal` — under the (a) fold-only reading, `axpby-leaf-identity` would dissolve into
  `linear-combination-fold-specialization`'s arity-2 row and `axpby-body-identity`'s RHS would
  re-anchor to the fold-parent. The c042 cross-cutter audit recommends KEEPING leaf-floor (b)
  (`book/src/L2/index.md` §Working-Notes). Each theme carries the design-presupposition note inline;
  no NEW OQ is opened (the existing `dot-l2-leaf-floor-vs-fold-only-design` OQ already governs the
  fold-parented BLAS-1 floor-edge cohort, of which `axpby` is now a member).

- **L3/axpby §"Lowers to" staleness → c044 sweep (NOT here).** The firm `book/src/L3/axpby.md`
  §"Lowers to" (`:116-120`) records lowering straight to L1 with "no L2 intermediate," which predates
  the L2 floor + this L3>L2 edge. Re-anchoring it to the present adjacent L2 floor is the same c044
  L3-staleness sweep item the D4 harvester surfaced (re-anchor the L3 BLAS-1 cohort `lowers_to`
  framing) — a harvester/lifter follow-up on the L3 entry, **not in this abstractor's scope** (I do
  not modify L_n operator entries). Surfaced for the OQ ledger; `axpby-body-identity` notes the
  to-be-superseded framing in its §Verified-against so the downstream sweep has the pointer.

- **Forward-references resolved as live links.** `linear-combination-fold-specialization.md`,
  `scal-fold-specialization.md`, `dot-leaf-identity.md`, `scal-body-identity.md`,
  `dot-body-identity.md`, `krylov-step-body-identity.md`, and the co-dispatched-this-cycle
  `axpby-leaf-identity.md` ↔ `axpby-body-identity.md` cross-links all point at on-disk files (the two
  new files land together this cycle, applied serially). The L2 `axpby.md` and the L1/L3 `axpby.md`
  endpoints are on-disk (L1/L3 firm; L2 co-lands via D4 ahead of these themes in wave-2 serial
  sequencing). All links are live, none plain-text-deferred.
