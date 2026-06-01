# axpy-leaf-identity

The L2>L1 lowering theme for the BLAS-1 `axpy` leaf. The rewrite is **identity-in-form on the leaf**:
the L2 [`axpy`](../L2/axpy.md) floor leaf lowers to the L1 [`axpy`](../L1/axpy.md) primitive with the
same signature `Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`, the same fused `α·x + y` semantics,
and the same six algebraic laws — value-thread-isomorphic on the primitive. `axpy` is the **arity-2
member** of the [`linear_combination`](../L2/linear_combination.md) fold (`axpy(α,x,y) =
linear_combination [(α,x),(1,y)]`, second coefficient fixed to 1), **cited as fold-parent but NOT
merged** (the fold-cohort boundary at `book/src/L2/index.md` §"Fold-cohort boundary" is load-bearing —
the leaf keeps its one-to-one shape with the L0 `AXPY` symbol that the onward L1>L0 mutation rotation
relies on, and the fixed-1 `y`-coefficient that distinguishes it from `axpby`). The L2 layer's
fusion-rotation work for the arity family is **the fold-parent's job**; this leaf carries no
leaf-unique fusion, so its own L2>L1 edge is the identity, with the fusion treatment deferred to
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md). This is the
**arity-2 shadow** of that firm fold-theme, and a direct sibling of the arity-1
[`scal-leaf-identity`](./scal-leaf-identity.md) (renamed cycle-043 from `scal-fold-specialization`).

## Slug

`axpy-leaf-identity`

## Context

`axpy` at L2 is the **floor leaf** entry (`book/src/L2/axpy.md`, harvested cycle-043 wave-1 D3): the
base scalar-vector fused-update primitive, rendered as its own same-named L2 chapter so the firm L3
[`axpy`](../L3/axpy.md) leaf rests on an adjacent same-named L2 parent (per CLAUDE.md §Methodology
invariants **Identity-lowerings still require both L levels**) rather than skipping a layer to L1.
This theme is the L2>L1 edge of that floor.

The edge is the **identity-in-form** case: the L2 `axpy` leaf and the L1 `axpy` leaf are
value-thread-isomorphic on the primitive. This is the L2>L1 analogue of the L3>L2
[`axpy-body-identity`](../L3-L2/axpy-body-identity.md) theme (the other thin edge of the same leaf,
co-authored this cycle), and a sibling shape to the L2>L1
[`scal-leaf-identity`](./scal-leaf-identity.md) (the arity-1 member of the same
`linear_combination` fold) — except here the leaf is arity-2 with the second coefficient fixed to 1.

**Why this edge is identity while its fold-parent carries the fusion.** The L2 fusion rotation for the
scalar-weighted-sum cohort — de-fusing Palace's fused single-aligned-pass kernels into the canonical
`foldl` accumulation, plus the **arity-dispatch selection** (length-1/2/2/3 picking
`scal`/`axpy`/`axpby`/`axpbypcz`), the **`axpy`-vs-`axpby` sub-selection** on the unit-coefficient
test, and the **pinned summation-order table** (the load-bearing-numerical residue) — is **the
fold-parent's job**. The firm
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) theme carries
all of it for the whole arity family. The `axpy` leaf is the arity-2-coeff-1 member of that fold;
restricting the fold-parent's fusion content to this leaf leaves **no fusion structure unique to
`axpy`** (the single fused `α·x + y` pass is the arity-2 case of the fold's single-aligned-pass note,
already covered family-wide). So the `axpy` leaf's own L2>L1 edge — the rotation between the L2 `axpy`
chapter and the L1 `axpy` chapter — is the identity, with the fusion treatment deferred to the
fold-parent theme.

## L2 form (LHS)

The L2 form is the `axpy` floor leaf (`book/src/L2/axpy.md` §Signature, harvested cycle-043 wave-1 D3)
— the mutation-free fused scalar-vector update:

    axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]
    axpy α x y = α·x + y

Pure / out-of-place (no destination buffer; the result is a fresh `Tensor[N]`); one scalar `α`, two
input tensors `x`, `y` of length axis `N`; `result[i] = α·x[i] + y[i]` for every `i ∈ [0, N)`.
Element-local, reduction-free, rank-local. At L2 `axpy` is the **base scalar-vector fused-update
leaf** — and **also** the arity-2 member of the variadic
[`linear_combination`](../L2/linear_combination.md) fold:

    axpy(α, x, y) = linear_combination [(α, x), (1, y)]      -- second coeff fixed to 1
                                                             -- (linear_combination.md:69)

cited as fold-parent but NOT merged. The only fusion note the floor entry carries is the **arity-2
case of the fold's single-aligned-pass fusion note**: the single strided pass computing `α·x[i] +
y[i]` per element is the seed-and-accumulate `foldl` over `[(α, x), (1, y)]` collapsed to one scaled
accumulate of `x` into `y` as the running sum. The MPI collective does not appear (`axpy` is
rank-local — no reduction over `N`), and the in-place receiver-mutating idiom is NOT in the L2
signature.

## L1 form (RHS)

The L1 form is the firm `axpy` leaf primitive (`book/src/L1/axpy.md` §Signature, firm cycle-002) —
identical in signature, semantics, and laws, the mutation-lifted pure-functional image of the L0
receiver-mutating `y.Add(α, x)` / `y.AXPY(α, x)` (and free-function `AXPY(α, x, y)`) idiom:

    axpy :: (α: Scalar, x: Tensor[N], y: Tensor[N]) -> Tensor[N]
    axpy(α, x, y) = α·x + y

The L1 signature is **textually identical to the L2 signature** modulo notation (curried arrow vs
positional tuple). The six algebraic laws (identity-in-α / identity-in-x / left-distribution-in-y /
scalar-additive-collapse / scalar-absorption / vector-linearity-in-x) hold unchanged at both layers
(`axpy` L1 §Algebraic laws ≡ `axpy` L2 §Algebraic laws). The L1 leaf already erases the L0 destination
buffer and the `α == 1.0` constant-folding fast path (a transparent performance trick); the L1 entry
is authoritative on every Palace-surface fact and the L2 form does not duplicate them. The in-place
mutation is reintroduced only at the L1>L0 lowering
[`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (which covers `axpy` as
the β=1 specialization of `axpby`).

## The rewrite (L2 → L1)

The rewrite is the **identity on the leaf**. Every L2 binding maps to the same L1 binding at the same
position:

    | L2 leaf (`L2/axpy`)                      | L1 leaf (`L1/axpy`)                      | Mapping  |
    |------------------------------------------|------------------------------------------|----------|
    | `axpy :: Scalar -> T[N] -> T[N] -> T[N]` | `axpy :: (α, x, y) -> T[N]`              | Identity. Same signature shape; arrow vs tuple is notational only. |
    | `axpy α x y = α·x + y`                   | `axpy(α, x, y) = α·x + y`                | Identity. Same fused scalar-vector field operation; same per-element kernel `α·x[i] + y[i]`. |
    | second coeff fixed to 1 (`y`-term unscaled) | `y` enters unscaled                   | Identity. The fixed-1 `y`-coefficient is preserved across the edge (the load-bearing difference from `axpby`). |
    | algebraic laws 1–6                       | algebraic laws 1–6                       | Identity. Inherited unchanged (affine-vector-update facts). |
    | fold-specialization identity             | fold-specialization identity             | Identity. `axpy(α,x,y) = linear_combination [(α,x),(1,y)]` holds at both layers (cited, NOT merged). |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the mapping
is total and bijective on the leaf. This is the identity-in-form property.

**The one note (fusion deferral).** The L2 layer's defining work is kernel-fusion de-fusion. For the
scalar-weighted-sum cohort, that work is carried entirely by the fold-parent
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md): the
arity-dispatch selection (`scal`/`axpy`/`axpby`/`axpbypcz`), the `axpy`-vs-`axpby` sub-selection on
the unit-coefficient test, the arity-3→2 fall-through on `γ==0`, and the pinned-summation-order table.
The `axpy` leaf is the arity-2-coeff-1 member of that fold; **no fusion structure is unique to the
leaf beyond the fold-parent's**. So this theme's edge is the identity, and bit-reproduction /
arity-dispatch / summation-order concerns are read off the fold-parent theme's §"The
fusion-selection rewrite" and §"pinned-summation-order table", not re-derived here.

Note the contrast with the arity-1 sibling
[`scal-leaf-identity`](./scal-leaf-identity.md): at arity 1 there is **no sum at all** (one
scaled pass, one rounding — value-exact AND bit-exact unconditionally), so its edge is identity with
no numerical residue even *at the fold level*. At arity 2, `axpy` *does* compute a sum (`α·x[i] +
y[i]` is one accumulation per element), so the IEEE summation-order non-law is present (inherited from
L1, recorded below) — but it is the **fold's** residue, carried family-wide by the fold-parent's
pinned-order table, not a leaf-unique fusion this edge must de-fuse.

## Applicability conditions

The identity rewrite is valid (unconditionally, for the firm `axpy` endpoints) when:

1. **The L2 form is the standalone `axpy` floor leaf** (the arity-2-coeff-1 member of the
   `linear_combination` fold), NOT the variadic fold itself. If the source form is the variadic
   `linear_combination`, the governing lowering is
   [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md), not this
   theme — this theme is the single-leaf edge, the fold's arity-2-coeff-1 row factored out under the
   fold-cohort do-NOT-merge boundary.

2. **The leaf is value-thread-isomorphic across the edge.** The L2 `axpy` leaf and the L1 `axpy` leaf
   share the signature, the fused `α·x + y` semantics, the fixed-1 `y`-coefficient, and the six
   algebraic laws. Confirmed by construction: `L2/axpy` is authored as a thin floor entry whose laws
   are inherited unchanged from `L1/axpy` (wave-1 D3 §"Algebraic laws", §Signature).

3. **All fusion content is the fold-parent's.** No fusion structure unique to the `axpy` leaf (beyond
   the fold-parent's family-level de-fusion + arity-dispatch + summation-order table) exists; the
   leaf's edge is therefore the identity with a single deferring note (wave-1 D3 §"Semantics" / the
   arity-2 single-aligned-pass note deferred to `linear_combination` §"Fusion note").

4. **Single length axis, shared element type.** `x, y : Tensor[N]` with one shared length axis; `α`,
   `x`, `y` share element type (`real` or `complex`), with a real `α` against complex `x, y` promoted
   per [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) (the
   `AXPY(double, ComplexVector, ComplexVector)` forwarding overload at
   `palace/linalg/vector.cpp:714-718`, absorbed at construction; not a distinct lowering sub-pattern).
   Inherited unchanged from the L1 leaf.

If a future L2 `axpy` variant introduced leaf-specific fusion not absorbed by the fold-parent, the
identity claim would need re-audit — none exists in the current surface.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `axpy` leaf's signature shape (`Scalar -> Tensor[N] -> Tensor[N] ->
Tensor[N]`) is identical to the L1 `axpy` leaf's signature shape — a whole-tensor fused scalar-vector
update with no element loop exposed at either layer. The rotation between two value-thread-isomorphic
leaves with identical signatures is the identity by construction; the only L2-layer work (fusion
de-fusion + arity-dispatch) is carried by the fold-parent, leaving the leaf's own edge a no-op. A
secondary `algebraic` flavour is inherited from the fold-parent: the arity-2-coeff-1 row **is**
`linear_combination.md` law 6 (the specialization identity `axpy(α,x,y) = linear_combination
[(α,x),(1,y)]`) read at the two-term-with-fixed-second-coeff case; because the leaf's own edge has no
arity dispatch to make (it is a fixed-arity leaf), the structural identity-in-form dominates.

**Empirical-match (secondary)**: the L1 leaf is firm on direct Palace evidence (`L1/axpy` §Evidence,
including the `AXPY(double, Vector, Vector)` free function with the `α == 1.0` fast-path at
`palace/linalg/vector.cpp:702-712`, and `ComplexVector::AXPY` at `:276-311`), and the L2 floor leaf
was authored as value-thread-isomorphic to it; the two forms agree on every law and every variant axis
by independent transcription. The identity is observational on the two existing firm/firming chapters,
not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `axpy` floor leaf (firming
cycle-043 wave-1 D3), the L1 RHS is the firm `axpy` leaf (firm cycle-002). This theme is the identity
edge between existing chapters; it proposes no new operators. The fold-parent
[`linear_combination`](../L2/linear_combination.md) is firm (cycle-018); `axpy`'s arity-2-coeff-1
membership is a cited fold-specialization, not a new operator.

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/axpy.md` (firming cycle-043 wave-1 D3) — the L2 floor leaf (LHS): the base
  scalar-vector fused-update primitive, value-thread-isomorphic to the L1 leaf, six laws + the
  fold-specialization identity inherited unchanged, two variant axes (element-type + scalar-promotion
  sub-axis). (The chapter lands at this cycle's integration alongside this theme — wave-2 serial
  sequencing applies D3 before this theme.)
- `book/src/L1/axpy.md` (firm cycle-002) — the L1 leaf (RHS): signature (`:16-18`), the six algebraic
  laws (`:41-46`), the two non-laws (`:50-51`), the variant axes (`:59-62`), the complete L0 evidence
  list (`:77-83`). Authoritative on every Palace-surface fact.
- `book/src/L2/linear_combination.md:69` (firm cycle-018) — the arity-2-coeff-1 specialization
  identity `axpy(α, x, y) = linear_combination [(α, x), (1, y)]` (§Signature line 69; §Algebraic-laws
  law 6). The fold-parent membership anchor; cited, NOT merged.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm cycle-018/019) — the fold-parent's
  own specialization theme; this theme is its arity-2-coeff-1 single-term shadow. The arity-2 row
  there (and the `axpy`-vs-`axpby` sub-selection on the unit-coefficient test) is the same edge this
  theme records standalone.
- `book/src/L2-L1/scal-leaf-identity.md` (firm cycle-041 D6; renamed cycle-043 from
  `scal-fold-specialization`) — the arity-1 sibling precedent; the exact template structure this theme mirrors
  (floor-edge framing, fold-membership-cited-not-merged, identity-in-form, fusion deferred to
  fold-parent), adapted arity-1 → arity-2 (the `y`-term with fixed-1 coefficient + the IEEE summation
  non-law are the arity-2-specific content absent at arity 1).
- `book/src/L2-L1/dot-leaf-identity.md` (firm cycle-041) — the `-leaf-identity` slug + structure
  precedent (RATIFIED convention; the §"The rewrite (L2 → L1)" total-and-bijective mapping table
  format).
- `book/src/L2/index.md` §"Fold-cohort boundary" — the load-bearing do-NOT-merge boundary between the
  leaf and the fold; line 17 names `axpy` in the L2 base-primitive vocabulary.
- `scaffolding/decisions/axpby-as-primitive.md` — the fused-leaf decision (keep leaves firm, fuse up
  into the fold, don't merge) governing the leaf-vs-decompose choice.

Onward L1>L0 lowering (the in-place mutation this L2/L1 pure edge abstracts over):

- `book/src/L1-L0/axpby-mutation-rotation.md` (firm) — the L1>L0 mutation rotation; sub-pattern A
  covers `axpy` as the β=1 specialization of `axpby` — the in-place `y.Add(α, x)` / `y.AXPY(α, x)`
  receiver-mutating idiom the L2 floor and L1 leaf both abstract over.

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — this edge is
identity-in-form, so L0 evidence is transitive through L1; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:702-712` — free function `AXPY(double, Vector, Vector)` (the real-real
  arity-2-coeff-1 leaf), with the `α == 1.0` fast-path branch at `:704` (`y += x` else
  `y.Add(alpha, x)`) — the transparent constant-folding trick erased at L1. **Self-verified (anchor
  `AXPY` @702; `1.0` @704).**
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition and the element-wise
  `forall_switch` kernels (`YR[i] += ar·XR[i] − ai·XI[i]`). **Self-verified (anchor `AXPY` @276-281).**
- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` and `Add` / `Subtract` aliases declared
  (`In-place addition (*this) += alpha * x.`). **Self-verified (anchor `AXPY` @116-118).**
- `palace/linalg/vector.hpp:305-307` — free-function template `AXPY(ScalarType, const VecType &,
  VecType &)` declared (`Addition y += alpha * x.`). **Self-verified (anchor `AXPY` @307).**

## Status

`firm` — the L2 LHS is the firm-this-cycle floor leaf (D3 wave-1), the L1 RHS is the firm `axpy` leaf
(cycle-002), and the rotation between two value-thread-isomorphic leaves with identical signatures is
the identity by construction (§"The rewrite (L2 → L1)" table is total and bijective on the leaf). The
only L2-layer work — kernel-fusion de-fusion + arity-dispatch — is carried by the firm fold-parent
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) for the whole
arity family; no fusion structure is unique to the `axpy` leaf. No speculative operator, no
negative-anchor reconstruction, no literature inference. The arity-2 shadow of that firm fold-theme,
factored out as the standalone leaf's own edge under the load-bearing fold-cohort do-NOT-merge
boundary; a direct sibling of the arity-1 [`scal-leaf-identity`](./scal-leaf-identity.md)
(renamed cycle-043 from `scal-fold-specialization`).

> **Slug convention note.** This theme uses the RATIFIED `-leaf-identity` slug (batch-12 meta-phase;
> the cycle-041 `scal`/`nrm2` `-fold-specialization` outliers are being renamed `-leaf-identity` by
> D1 this cycle for cohort uniformity with the cycle-042 standalone-floor edges). `axpy` is a
> fold-member (unlike the fold-free `reciprocal`/`elementwise_product`), but the edge is an
> identity-leaf-lowering, not a fold→leaf dispatch — so `-leaf-identity` is the correct slug, matching
> the `dot-leaf-identity` precedent (also a fold-member with all fusion deferred to its fold-parent).

> **Design-presupposition note (not a status reduction).** This theme presupposes the **(b)
> same-named leaf-floor** realization of `L2/axpy` (Applicability condition 1). The leaf-vs-fold fork
> (`dot-l2-leaf-floor-vs-fold-only-design`) is **resolved keep-(b)** (batch-12 meta-phase, per the
> c042 cross-cutter audit `reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/`).
> Under the superseded (a) fold-only reading, this theme's LHS would not exist standalone and the edge
> would fold into `linear-combination-fold-specialization`'s arity-2 row. The theme is self-coherent
> under the resolved leaf-floor reading it is built on.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L1 leaf *up* to the L2 floor is the value-thread-isomorphic identity rotation: the L1
  signature has no kernel fusion exposed (beyond the arity-2 single-aligned pass), no destination
  buffer, no MPI collective — exactly the properties that make it L2-native by construction. No
  additional structure is required for the lift. This reverse-direction note lives here in working
  notes per the high→low layer-definition discipline; the formal chapter narrates only L2 → L1.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (the
  co-authored `axpy-body-identity` L3>L2 identity ∘ this `axpy-leaf-identity` L2>L1 identity) is
  annotated in-line at the `axpy` entries per the CLAUDE.md invariant "Identity rotations across
  non-adjacent layers are annotated in-line, not via a dedicated lowering directory" — no
  `book/src/L3-L1/` directory. This theme + the co-dispatched `axpy-body-identity` compose to capture
  it.
