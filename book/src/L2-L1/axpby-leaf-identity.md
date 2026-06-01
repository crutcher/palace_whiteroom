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
[`scal-leaf-identity`](./scal-leaf-identity.md) (the arity-1 single-term shadow) and
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
[`scal-leaf-identity`](./scal-leaf-identity.md) and the reduce-to-scalar
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
not re-derived here. **Unlike the arity-1 `scal-leaf-identity`** (value-exact AND bit-exact
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
- `book/src/L2-L1/scal-leaf-identity.md` (cycle-041 D6 firm) + `book/src/L2-L1/dot-leaf-identity.md`
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
`scal-leaf-identity` (its fused pass IS a two-term sum, so the summation-order non-law is
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
