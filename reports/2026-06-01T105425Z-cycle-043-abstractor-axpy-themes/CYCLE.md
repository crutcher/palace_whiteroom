---
agent: abstractor
invoked_at: 2026-06-01T105425Z
scope: two adjacent thin-identity lowering themes for axpy — L2>L1 (axpy-leaf-identity) + L3>L2 (axpy-body-identity)
status: pending
inputs:
  - reports/2026-06-01T105425Z-cycle-043-harvester-L2-axpy/CYCLE.md (wave-1 D3; the L2 axpy floor — source of truth for the L2 form; co-lands this cycle)
  - book/src/L1/axpy.md (firm cycle-002; the L1 leaf — RHS of the L2>L1 edge)
  - book/src/L3/axpy.md (firm cycle-011; the L3 leaf — LHS of the L3>L2 edge)
  - book/src/L2-L1/scal-fold-specialization.md (firm cycle-041 D6; the arity-family sibling precedent for the L2>L1 edge)
  - book/src/L3-L2/scal-body-identity.md (firm cycle-041 D6; the arity-family sibling precedent for the L3>L2 edge)
  - book/src/L2-L1/dot-leaf-identity.md (firm cycle-041; the `-leaf-identity` slug precedent — RATIFIED convention)
  - book/src/L3-L2/dot-body-identity.md (firm cycle-041; the `-body-identity` slug precedent)
  - book/src/L2/linear_combination.md:69 (firm cycle-018; fold-parent — `axpy(α,x,y) = linear_combination [(α,x),(1,y)]`)
  - book/src/L1-L0/axpby-mutation-rotation.md (firm; the onward L1>L0 in-place form — axpy is sub-pattern A β=1)
  - book/src/L3-L2/krylov-step-body-identity.md:97 (firm; the L3-native-by-signature-shape classification naming axpy)
  - L0 anchors (self-verified via citecheck --anchor, 2026-06-01): palace/linalg/vector.cpp:702-712 (`α==1.0` fast-path at :704), :276-311 (`ComplexVector::AXPY`); vector.hpp:115-118, :305-307
integrated_at: 2026-06-01T140000Z
integration_commit: 3f9a7d0
integration_notes: "cycle-043 batch integration (cohort-completing L2-floor build); D6 axpy theme pair (L2>L1 axpy-leaf-identity + L3>L2 axpy-body-identity); cross-report rename repair (D1 git-mv x pre-rename slug) applied; clean; see reports/2026-06-01T140000Z-integrator-finalize-cycle-43/CYCLE.md + cycle-043 STAGING row."
---

# CYCLE: two adjacent thin-identity lowering themes for `axpy` — `axpy-leaf-identity` (L2>L1) + `axpy-body-identity` (L3>L2)

## Summary

This dispatch (cycle-043 D6, wave-2) authors the **two adjacent thin identity-in-form lowering
themes** that complete the lowering chain for the BLAS-1 `axpy` leaf now that its L2 floor lands
this cycle (wave-1 D3, `book/src/L2/axpy.md`). `axpy` is the **arity-2 member** of the firm
[`linear_combination`](../L2/linear_combination.md) fold (`axpy(α,x,y) = linear_combination [(α,x),(1,y)]`,
second coefficient fixed to 1), cited but NOT merged (the fold-cohort boundary is load-bearing). Per
the wave-1 D3 reading and the established `scal` arity-family precedent, **all L2 fusion content is
deferred to the fold-parent** — the leaf edge carries no leaf-unique fusion, so both edges are pure
identity-in-form on the primitive. The two themes are:

1. **`axpy-leaf-identity`** (`book/src/L2-L1/`) — the L2>L1 edge: the L2 `axpy` floor leaf lowers to
   the firm L1 `axpy` leaf, value-thread-isomorphic on the signature `Scalar -> Tensor[N] -> Tensor[N]
   -> Tensor[N]`, six laws + the fold-specialization identity inherited unchanged. The arity-2 shadow
   of the firm `linear-combination-fold-specialization`, with all fusion deferred to that fold-parent.

2. **`axpy-body-identity`** (`book/src/L3-L2/`) — the L3>L2 edge: the L3 whole-tensor `axpy` field
   operation lowers to the L2 floor leaf, identity-in-form on the body with **no wrapper to rotate**
   (`axpy` is a leaf, not a step body; no `(op,K,s)`→`IterState`, no outer loop). `axpy` is L3-native
   by signature shape (`krylov-step-body-identity.md:97`), so the iteration rotation is already done
   at the signature level.

Both use the **RATIFIED `-leaf-identity` / `-body-identity` slug convention** (batch-12 meta-phase;
the `scal`/`nrm2` `-fold-specialization` slugs are being renamed to `-leaf-identity` by D1 this cycle,
so I use `-leaf-identity` for axpy from the start). Both narrate FORWARD (L_{n+1} LHS → L_n RHS),
high→low. Both are `firm` (identity edge between firm/firming endpoints; no speculative operator, no
negative-anchor reconstruction). They compose to capture the transitive non-adjacent L3>L1 identity
in-line (per the CLAUDE.md non-adjacent-in-line-identity invariant).

## Proposed changes

```new:book/src/L2-L1/axpy-leaf-identity.md
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
[`scal-fold-specialization`](./scal-fold-specialization.md) (being renamed `scal-leaf-identity` this
cycle).

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
[`scal-fold-specialization`](./scal-fold-specialization.md) (the arity-1 member of the same
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
[`scal-fold-specialization`](./scal-fold-specialization.md): at arity 1 there is **no sum at all** (one
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
- `book/src/L2-L1/scal-fold-specialization.md` (firm cycle-041 D6; being renamed `scal-leaf-identity`
  this cycle) — the arity-1 sibling precedent; the exact template structure this theme mirrors
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
boundary; a direct sibling of the arity-1 [`scal-fold-specialization`](./scal-fold-specialization.md)
(renamed `scal-leaf-identity` this cycle).

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
```

```new:book/src/L3-L2/axpy-body-identity.md
# axpy-body-identity

The L3>L2 lowering theme for the BLAS-1 leaf `axpy`. The rewrite is **identity-in-form on the body**
with **no wrapper rotation** — `axpy` is a leaf whole-tensor field operation, not a step body, so the
L3 whole-tensor form `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` lowers into the L2 floor
form by the identity on the primitive itself. There is no `(op, K, s)`→`IterState` consolidation and
no outer-loop dissolution to perform (the two surface adjustments that the sibling
[`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper); `axpy` has no
wrapper. The body IS the identity. `axpy` is one of the seven BLAS-1 primitives that are **L3-native
by signature shape** (no per-element loop visible at either layer; `krylov-step-body-identity.md:97`),
so the iteration rotation is already complete at the signature level and the L3>L2 body edge is the
identity. This is the arity-2-fold-member analogue of [`scal-body-identity`](./scal-body-identity.md)
(the arity-1 member), and the leaf-primitive counterpart of `krylov-step-body-identity` (which is
identity-in-form on a multi-primitive kernel body, with wrapper adjustments).

## Slug

`axpy-body-identity`

## Context

The `axpy` lowering relationships span three adjacent layers, all identity-in-form because `axpy` is a
BLAS-1 leaf with no iteration view and no leaf-unique kernel fusion:

- **L3 form** ([`L3/axpy`](../L3/axpy.md), firm cycle-011) — the whole-tensor field operation `axpy ::
  Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`, the iteration-rotation rendering consumed inside the
  `krylov-step` body's iterate-stratum update. Carries **no iteration view** (leaf primitive, not a
  step body) and **no sequential obstruction** (every element independent under the fused per-element
  `α·x[i] + y[i]`). The LHS of this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/axpy`](../L2/axpy.md), firm cycle-043 wave-1 D3) — the fusion-rotation floor leaf,
  the base scalar-vector fused-update primitive and the arity-2 member of the `linear_combination`
  fold (second coeff fixed to 1, cited NOT merged). The RHS of this theme.
- **L2>L1 form** ([`L2-L1/axpy-leaf-identity`](../L2-L1/axpy-leaf-identity.md), firm cycle-043 D6) —
  the onward edge into the L1 leaf; also identity-in-form (the arity-2 shadow of the fold's
  fusion-selection, with all fusion deferred to the fold-parent). Co-authored this cycle.

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009). The `krylov-step` theme
establishes the pattern "identity-in-form on the kernel **body**, with surface adjustments at the
**wrapper**"; its point-3 applicability condition names the seven L1 primitives — including **`axpy`**
— as L3-native by signature shape: "each operates on whole-tensor inputs with no element-loop exposed
at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition
step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)"
(`krylov-step-body-identity.md:97`). This theme is the standalone-leaf realization of that
classification for `axpy`: the body is the identity, **and there is no wrapper at all** — `axpy` is
not a step body, so the two wrapper adjustments the `krylov-step` theme carries (the
`(op, K, s)`→`IterState` consolidation and the outer-loop-to-driver-by-role dissolution) have no
analog here.

`axpy` differs from the arity-1 sibling [`scal-body-identity`](./scal-body-identity.md) only in arity:
`axpy` is the arity-2-coeff-1 fold member (one scaled term `α·x` plus one unit-coeff term `y`), `scal`
the arity-1 member (one scaled term). Both are identity-in-form on the body with no wrapper; the
arity-2-vs-arity-1 difference is entirely the fold-parent's content, not this edge's.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/axpy`](../L3/axpy.md) §Signature, firm cycle-011):

    axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]
    axpy α x y = α·x + y

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `α` a scalar
(`real` or `complex`, or `real` promoted against complex `x, y`); `x, y : Tensor[N]` a single shared
length axis, read-only at L3; result `Tensor[N]` of the same axis with `result[i] = α·x[i] + y[i]` for
every `i ∈ [0, N)`. The operator carries **no iteration view** (it is a leaf field operation, not a
step body) and **no sequential obstruction** (every element is independent of every other under the
fused per-element scaled add — embarrassingly parallel, fully GPU-friendly). No L4 wrapper machinery
applies (leaf primitives appear inside L4 operator bodies as let-bindings — e.g. inside
`krylov-step`'s `krylov_update` — not as first-class L4 typed-wrapper anchors; the
cross-layer-cross-cutter "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort).

## L2 form (RHS)

The L2 floor form ([`L2/axpy`](../L2/axpy.md) §Signature, firm cycle-043 wave-1 D3):

    axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]
    axpy α x y = α·x + y

The base scalar-vector fused-update leaf in the fusion-rotation vocabulary — **and** the arity-2
member of the [`linear_combination`](../L2/linear_combination.md) fold (`axpy(α,x,y) =
linear_combination [(α,x),(1,y)]`, second coeff fixed to 1, cited NOT merged). The signature is
**textually identical to the L3 form** modulo notation; the body is the same single whole-tensor fused
field operation. The six algebraic laws hold unchanged across the edge (L3 §Algebraic laws ≡ L2
§Algebraic laws — both inherit the L1 leaf's six affine-vector-update laws). The only fusion note the
L2 floor carries is the arity-2 single-aligned pass (the arity-2 case of the fold's fusion note,
deferred to the fold-parent); at L3 even that note is absent (L3 exposes no element loop at all).

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    axpy α x y   (L3 whole-tensor field op)   ⇒   axpy α x y   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow:

    | L3 form                                  | L2 form                                  | Mapping |
    |------------------------------------------|------------------------------------------|---------|
    | `axpy α x y = α·x + y` (whole-tensor field op; no iteration view) | `axpy α x y = α·x + y` (base scalar-vector fused-update floor leaf; arity-2 fold member) | Identity. Same signature, same single fused field operation. The only framing difference is documentary: L3 frames `axpy` as a whole-tensor field operation in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive (and the arity-2 fold member). No operational adjustment occurs. |
    | second coeff fixed to 1 (`y` unscaled)   | second coeff fixed to 1 (`y` unscaled)   | Identity. The fixed-1 `y`-coefficient is preserved across the edge. |
    | algebraic laws 1–6                       | algebraic laws 1–6                       | Identity. Inherited unchanged across the chain (affine-vector-update facts + the IEEE summation non-law). |
    | no sequential obstruction                | no sequential obstruction                | Identity. The fused add lifts as a whole-tensor op at both layers; every element independent. |

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body: (1) the L3 `(op, K, s)` positional tuple
consolidates into the L2 unified `IterState` record (state-hiding), and (2) the L3 tail-recursive
outer loop `iterate_while_L3` collapses to the L2 outer-driver-by-role reference (abstraction-by-role).
**Neither has an analog for `axpy`**: `axpy` is a single leaf field operation, not a step body with an
`(op, K, s)` carrier and an outer loop. There is no `IterState` (no state record — `axpy` is a pure
positional function), and there is no outer driver (no loop folds `axpy` calls at the operator itself;
`axpy` is *called by* step bodies like `krylov-step`'s `krylov_update`, but those loops belong to the
step body, not to `axpy`). The mapping is total and bijective on a single binding — the degenerate
maximal case of the identity-in-form property.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `axpy` endpoints) when:

1. **`axpy` is L3-native by signature shape.** Its signature `Scalar -> Tensor[N] -> Tensor[N] ->
   Tensor[N]` exposes no per-element loop at L2 or L3; the fused scaled add over `N` is a single
   semantic step at both layers. This is the load-bearing condition (per
   `krylov-step-body-identity.md:97`, which names `axpy` among the seven L3-native primitives).
   Satisfied by construction: `axpy` is a leaf field operation.

2. **`axpy` is treated as a leaf primitive, not decomposed.** `axpy` does not decompose into other L3
   or L2 primitives (it is NOT `scal` + tensor-add — it is the *fused* primitive, kept whole per the
   `axpby-as-primitive` fuse-don't-decompose decision
   ([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))).
   The de-fused two-pass form is the fold's seed-and-accumulate realization, recorded as the
   fold-parent's fusion note, not as an L3 or L2 decomposition.

3. **The L2 form is the same-named floor leaf** (`book/src/L2/axpy.md`), value-thread-isomorphic to
   the L3 leaf. The leaf-vs-fold fork (`dot-l2-leaf-floor-vs-fold-only-design`) is **resolved keep-(b)**
   (batch-12 meta-phase, per the c042 cross-cutter audit) — the L3 leaf lowers to an adjacent
   same-named L2 floor. Under the superseded (a) fold-only reading, the L3 leaf's adjacent L2 parent
   would be the fold-parent `linear_combination` and this theme's RHS would re-anchor; this condition
   records the resolved design presupposition explicitly.

4. **No iteration view, no sequential obstruction.** `axpy` is element-local, reduction-free,
   rank-local; every element is independent. There is no outer loop, no carry trajectory, no
   recurrence — so there is nothing for the L3 iteration rotation to have rotated and nothing for the
   L3>L2 lowering to dissolve.

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape `Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`
is whole-tensor by construction at both layers — no element loop is exposed at L2, no iteration view at
L3. The L3 vocabulary at this scope demands whole-tensor field operations with no element loop exposed;
`axpy` satisfies this *at L2 already*, so the rotation is the identity. This is a structural argument
about the leaf's signature, and it is the same structural argument the `krylov-step-body-identity`
theme makes as its secondary justification for each primitive in the kernel body (point-3 condition) —
here promoted to dominant because there is no kernel body wrapping the leaf, only the leaf itself.

**Empirical-match (secondary)**: the L3 leaf-floor and the L2 floor leaf were authored independently
(L3 cycle-011, L2 cycle-043 wave-1 D3) as value-thread-isomorphic to the same firm L1 leaf, and they
agree on every law, every variant axis, and every signature row by independent transcription. The
cross-layer-cross-cutter identity-in-form audit
(`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) the
BLAS-1 cohort") classified the `axpy` L3↔L1 rotation as identity-in-form; the firm
`krylov-step-body-identity` names `axpy` L3-native at line 97. This theme's L3>L2 edge is the
standalone-leaf realization of that audited classification, now that the L2 floor entry exists
(cycle-043 D3) for the rotation to target.

## Speculative L2 operators

**None.** Both endpoints are existing vocabulary: the L3 LHS is the firm `axpy` leaf (firm cycle-011),
the L2 RHS is the `axpy` floor leaf (firming cycle-043 wave-1 D3). This theme is the identity edge
between existing chapters; it proposes no new operators. `axpy` does not get its own L4 typed-wrapper
anchor (leaf primitives appear inside L4 operator bodies as let-bindings — the
cross-layer-cross-cutter "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort), so there
is no upstream L4>L3 theme for `axpy` either; the L3 form is L3-native by signature and this theme
closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/axpy.md` (cycle-011 firm) — the L3 whole-tensor form (LHS). Signature (`:30-32`),
  semantics (element-local, reduction-free, rank-local, no iteration view, no sequential obstruction;
  §"Iteration-rotation marker" `:62-64`), six algebraic laws (`:70-75`), two non-laws + the IEEE
  summation non-law (`:79-81`), two variant axes (`:101-104`). The §"Lowers to" (`:112-116`) currently
  records identity-in-form to L1 via the non-adjacent convention ("no L2 intermediate because the
  BLAS-1 primitives are L1 leaves not L2 compositions"); this theme supplies the now-present adjacent
  L3>L2 edge (downstream-consistency touch on the L3 entry flagged in §Open-questions of the authoring
  report).
- `book/src/L2/axpy.md` (firming cycle-043 wave-1 D3) — the L2 floor leaf (RHS). Identical signature
  and six laws; the base scalar-vector fused-update leaf framing + the arity-2 fold-membership identity
  (second coeff fixed to 1). (Lands at this cycle's integration alongside this theme.)
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-007/009 firm) — §"Applicability conditions"
  point 3: the load-bearing statement that the seven BLAS-1 primitives (including `axpy`) are L3-native
  by signature shape (no per-element loop visible), which is the structural justification for this
  identity edge. **Self-verified (anchor `L3-native` @97).**
- `book/src/L3-L2/scal-body-identity.md` (cycle-041 D6 firm; the arity-1 sibling precedent) — the
  exact template structure this theme mirrors (leaf-not-step-body framing, no-wrapper-to-rotate, the
  §"Rewrite shape" mapping table), adapted arity-1 → arity-2.

Cross-layer audit (the empirical-match anchor):

- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) the
  BLAS-1 cohort" — the HIGH CONFIDENCE classification of the `axpy` rotation as identity-in-form, the
  dispatch rationale for the cycle-011 L3 `axpy` backfill and (now) this L3>L2 edge.

Onward edges (cross-reference, not this theme's content):

- `book/src/L2-L1/axpy-leaf-identity.md` (cycle-043 D6) — the onward L2>L1 edge into the L1 leaf; also
  identity-in-form (the arity-2 shadow of the fold's fusion-selection, all fusion deferred to the
  fold-parent). Co-dispatched this cycle.
- `book/src/L1/axpy.md` (cycle-002 firm) + `book/src/L1-L0/axpby-mutation-rotation.md` (firm,
  sub-pattern A β=1) — the L1 leaf and its in-place L0 mutation rotation, reached via the onward edge.

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — identity-in-form edge, L0
evidence transitive through L1; self-verified via `tools/citecheck/citecheck.py --anchor` this
invocation; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:702-712` — free function `AXPY(double, Vector, Vector)` with the `α == 1.0`
  fast-path at `:704`. **Self-verified (anchor `AXPY` @702; `1.0` @704).**
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition and the element-wise
  `forall_switch` kernels. **Self-verified (anchor `AXPY` @276-281).**
- `palace/linalg/vector.hpp:115-118,305-307` — `ComplexVector::AXPY` member decl + the free-function
  template `AXPY` decl. **Self-verified (anchor `AXPY` @116-118, @307).**

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS ([`L3/axpy`](../L3/axpy.md)) is
firm (cycle-011); the L2 RHS ([`L2/axpy`](../L2/axpy.md)) is firm-this-cycle (wave-1 D3). The body is
the identity rotation on a single leaf field operation; **there is no wrapper to rotate** (no
`(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — `axpy` is a leaf, not a step body).
The structural justification (whole-tensor signature, no element loop, no iteration view) is the
`krylov-step-body-identity` point-3 condition specialized to the standalone leaf and promoted to
dominant; the empirical-match anchor is the firm cross-layer audit + the
`krylov-step-body-identity:97` L3-native classification. No speculative operator, no negative-anchor
reconstruction, no sequential obstruction. The arity-2-fold-member counterpart of the arity-1
[`scal-body-identity`](./scal-body-identity.md); the thinnest tier of the L3>L2 lowering family
alongside it.

> **Slug convention note.** This theme uses the RATIFIED `-body-identity` slug (batch-12 meta-phase),
> matching `dot-body-identity` / `scal-body-identity` and the cycle-042 standalone-floor cohort.

> **Design-presupposition note (not a status reduction).** This theme presupposes the **(b)
> same-named L2 leaf-floor** RHS (Applicability condition 3). The leaf-vs-fold fork
> (`dot-l2-leaf-floor-vs-fold-only-design`) is **resolved keep-(b)** (batch-12 meta-phase, per the
> c042 cross-cutter audit). Under the superseded (a) fold-only reading, the L2 RHS would re-point from
> the same-named `axpy` leaf to the fold-parent `linear_combination`, weakening the "identity" claim
> (a same-named leaf → a differently-named fold-parent is a weaker identity). The theme is
> self-coherent under the resolved (b) reading it is built on.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the value-thread-isomorphic identity
  rotation: the L2 signature has no element loop exposed, which is exactly what makes it L3-native by
  construction. No additional structure is required for the lift. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter narrates only
  L3 → L2.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `axpy-leaf-identity` identity) is annotated in-line at the `axpy`
  entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are annotated
  in-line, not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This theme + the
  co-dispatched `axpy-leaf-identity` compose to capture it.
```

```edit:book/src/L2-L1/index.md
| [dot-leaf-identity](./dot-leaf-identity.md) | `L2/dot` (firm, cycle-041 leaf-floor) | `L1/dot` (firm; `dot` + `tdot`) | firm *(structural; identity-in-form on the inner-product leaf — value-thread-isomorphic signature; all L2-layer fusion deferred to the fold-parent `inner-product-fold-specialization`; thin floor-edge of the BLAS-1 leaf)* |
| [axpy-leaf-identity](./axpy-leaf-identity.md) | `L2/axpy` (firm, cycle-043 D3 floor) | `L1/axpy` (firm leaf, cycle-002) | firm *(structural; identity-in-form on the arity-2 scalar-vector fused-update leaf — value-thread-isomorphic signature `Scalar -> T[N] -> T[N] -> T[N]` + six laws + fold-specialization identity (`axpy(α,x,y) = linear_combination [(α,x),(1,y)]`, second coeff fixed to 1, cited NOT merged); arity-2 shadow of `linear-combination-fold-specialization` — all fusion (arity-dispatch + summation-order table) deferred to that fold-parent, no leaf-unique surplus; IEEE summation non-law present (arity-2 computes a sum) but it is the fold's residue carried family-wide; sibling of arity-1 `scal-fold-specialization`; leaf-vs-fold fork resolved keep-(b))* |
```

> **Integrator note (count-ownership):** this is a single-ROW insertion (the `axpy-leaf-identity`
> row, placed immediately after `dot-leaf-identity`). Do NOT touch the L2-L1 §"Vocabulary cohort"
> running tallies or the §"Working Notes" cohort-growth-log counts — those belong to D2
> (layer-intro-author) this cycle. (Optionally, D2 may also fold a one-line cohort-log entry for the
> two `axpy` edges; that is D2's call, not this row.)

```edit:book/src/L3-L2/index.md
| [`scal-body-identity`](./scal-body-identity.md) | L3 [`scal`](../L3/scal.md) §Signature — the whole-tensor field operation `scal :: Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`scal`](../L2/scal.md) §Signature — the base scalar-vector-multiply floor leaf (arity-1 member of `linear_combination`, cited NOT merged); identical signature. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-041 D6 abstractor; identity-in-form on the body, **no wrapper to rotate** — the leaf-primitive counterpart of `krylov-step-body-identity`) |
| [`axpy-body-identity`](./axpy-body-identity.md) | L3 [`axpy`](../L3/axpy.md) §Signature — the whole-tensor fused field operation `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`axpy`](../L2/axpy.md) §Signature — the base scalar-vector fused-update floor leaf (arity-2 member of `linear_combination`, second coeff fixed to 1, cited NOT merged); identical signature + six laws. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf; **fold-member but all fusion is the fold-parent's**) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-043 D6 abstractor; identity-in-form on the body, **no wrapper to rotate** — the arity-2-fold-member counterpart of the arity-1 `scal-body-identity`) |
```

> **Integrator note (count-ownership):** this is a single-ROW insertion (the `axpy-body-identity`
> row, placed immediately after `scal-body-identity`). Do NOT touch the L3-L2 §"Vocabulary cohort"
> lists or the §"Working Notes" cohort-growth / coverage-gap (`l3-l2-rotation-theme-coverage-gap`
> `10-of-18` → ...) counts — those belong to D2 (layer-intro-author) this cycle.

```edit:book/src/SUMMARY.md
- [dot-body-identity](./L3-L2/dot-body-identity.md)
- [axpy-body-identity](./L3-L2/axpy-body-identity.md)
- [nrm2-body-identity](./L3-L2/nrm2-body-identity.md)
```

```edit:book/src/SUMMARY.md
- [dot-leaf-identity](./L2-L1/dot-leaf-identity.md)
- [axpy-leaf-identity](./L2-L1/axpy-leaf-identity.md)
- [nrm2-fold-specialization](./L2-L1/nrm2-fold-specialization.md)
```

## Speculative operators proposed

**None.** Both themes are identity edges between **existing firm/firming vocabulary** on every side:

| theme | LHS endpoint | RHS endpoint | new operators |
|---|---|---|---|
| `axpy-leaf-identity` (L2>L1) | `L2/axpy` (firming cycle-043 D3) | `L1/axpy` (firm cycle-002) | none |
| `axpy-body-identity` (L3>L2) | `L3/axpy` (firm cycle-011) | `L2/axpy` (firming cycle-043 D3) | none |

`axpy`'s arity-2-coeff-1 membership in the firm `linear_combination` fold (cycle-018) is a **cited
fold-specialization, not a new operator**. No harvester promotion is needed for either theme.

## Supporting evidence

- **Source of truth for the L2 form**: `reports/2026-06-01T105425Z-cycle-043-harvester-L2-axpy/CYCLE.md`
  (wave-1 D3) — the proposed `book/src/L2/axpy.md` floor. Both themes target it as the L2 endpoint and
  inherit its framing (floor-presence, fold-membership-cited-not-merged, in-line identity-rotation,
  firm-on-positive-structure, output-aliasing-is-the-fold's-axis).
- **Arity-family precedents mirrored** (the exact template structure, adapted arity-1 → arity-2):
  `book/src/L2-L1/scal-fold-specialization.md` (firm cycle-041 D6) for the L2>L1 edge;
  `book/src/L3-L2/scal-body-identity.md` (firm cycle-041 D6) for the L3>L2 edge. The arity-2-specific
  content not present at arity-1 is: the `y`-term with fixed-1 coefficient (the load-bearing difference
  from `axpby`), and the IEEE summation non-law (arity-2 computes a per-element sum `α·x[i] + y[i]`,
  whereas arity-1 `scal` has no sum at all — value+bit-exact unconditionally).
- **Slug convention precedents** (RATIFIED `-leaf-identity` / `-body-identity`):
  `book/src/L2-L1/dot-leaf-identity.md` + `book/src/L3-L2/dot-body-identity.md` (firm cycle-041) — also
  fold-members with all fusion deferred to the fold-parent, so the same-slug + same-structure choice.
- **Fold-parent anchor**: `book/src/L2/linear_combination.md:69` —
  `axpy(α, x, y) = linear_combination [(α, x), (1, y)]` (second coeff fixed to 1; §Signature line 69 +
  §Algebraic-laws law 6). Verified by `sed` read this invocation. The fold-parent's own L2>L1
  specialization theme `book/src/L2-L1/linear-combination-fold-specialization.md` (firm) carries the
  arity-dispatch + `axpy`-vs-`axpby` sub-selection + pinned-summation-order content this leaf defers.
- **L3-native classification anchor**: `book/src/L3-L2/krylov-step-body-identity.md:97` — names the
  seven BLAS-1 primitives (including `axpy`) as L3-native by signature shape (no per-element loop
  visible). Verified by `sed` read this invocation (anchor `L3-native` @97).
- **L0 anchors self-verified 2026-06-01** via `tools/citecheck/citecheck.py --anchor` (all `[ok]`):
  `palace/linalg/vector.cpp:702-712` (anchor `AXPY` @702; `1.0` fast-path @704), `:276-311`
  (`ComplexVector::AXPY` @276-281), `vector.hpp:115-118` (member decl @116-118), `:305-307`
  (free-fn template decl @307). Inherited transitively (identity-in-form edges; L0 evidence is
  transitive through the firm L1 leaf — not re-localized as new claims).
- **Onward L1>L0**: `book/src/L1-L0/axpby-mutation-rotation.md` (firm) sub-pattern A covers `axpy` as
  the β=1 specialization of `axpby` — the in-place mutation both pure edges abstract over.
- **Directive / fork**: `l2-floor-under-l3-leaf-cohort` (2026-05-31); leaf-vs-fold fork
  `dot-l2-leaf-floor-vs-fold-only-design` **resolved keep-(b)** (batch-12 meta-phase per the c042
  cross-cutter audit `reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/`).

## Open questions / caveats

- **The firm L3 `axpy` entry (`book/src/L3/axpy.md`) §"Lowers to" goes stale once the L2 floor +
  these themes land.** `L3/axpy.md:5-6` (frontmatter `lowers_to`), `:97`, and `:112-116` currently
  assert a direct L3>L1 identity rotation with "no L2 intermediate because the BLAS-1 primitives are
  L1 leaves not L2 compositions." With the L2 floor present (wave-1 D3) and the adjacent `axpy-body-identity`
  L3>L2 edge authored here, the L3 leaf now rests on an adjacent same-named L2 parent; the L3 entry's
  §"Lowers to" should re-anchor its lowering target L1 → L2 (pointing at `axpy-body-identity`). **Route
  to the c044 L3-re-anchor sweep — NOT fixed here** (one operator/theme per invocation; the L3 entry
  is out of this dispatch's scope; same staleness the cycle-041 `scal` floor created for `L3/scal.md`,
  track together). This is the **same OQ the wave-1 D3 harvester already surfaced** for `L3/axpy.md` —
  these two themes are its adjacent-edge complement, so the re-anchor sweep should touch all of
  `L3/axpy` §Lowers-to, frontmatter, and the in-line non-adjacent-identity note in one pass.

- **Count-ownership deferred to D2.** Per dispatch instruction, I appended ONLY: two theme bodies
  (`new:`), two single dep-map ROWS (one each in L2-L1/index + L3-L2/index, with explicit integrator
  notes NOT to touch consolidated tallies), and two SUMMARY registrations. The L2-L1 §"Vocabulary
  cohort" firm-count (currently "15 firm + 1 partly-constructive"), the L3-L2 §"Vocabulary cohort"
  lists, and the `l3-l2-rotation-theme-coverage-gap` `10-of-18` coverage tally are **D2's to update
  this cycle** — deferred, not written here.

- **SUMMARY placement.** Registered `axpy-leaf-identity` after `dot-leaf-identity` (in the
  identity-in-form BLAS-1-floor-edge group) and `axpy-body-identity` after `dot-body-identity` /
  before `nrm2-body-identity` (keeping the BLAS-1-leaf `-body-identity` cohort contiguous and roughly
  fold-arity-ordered: `dot` reduce-to-scalar, then the `axpy`/`scal` reduce-to-Tensor leaves). If D2 /
  the integrator prefers strict alphabetical or a different grouping, that is a cosmetic re-order — the
  chapter content is order-independent.

- **Slug-uniformity note (cohort hygiene, for D2 / meta-phase awareness).** I used `-leaf-identity`
  for the L2>L1 `axpy` edge per the RATIFIED convention, even though the L2>L1 row sits adjacent to the
  cycle-041 `nrm2-fold-specialization` / (pre-rename) `scal-fold-specialization` outliers. Once D1's
  rename lands (`scal`/`nrm2` `-fold-specialization` → `-leaf-identity`), the L2>L1 BLAS-1-floor-edge
  cohort will be slug-uniform (`dot`/`axpy`/`scal`/`nrm2` all `-leaf-identity`). No action for this
  dispatch; flagged so the rename sweep includes the new `axpy-leaf-identity` in its consistency check
  (it already conforms).

- **Lifting notes (reverse direction)** for both edges live in each theme's own §"Open questions /
  caveats" working-notes block (NOT in the high→low chapter body), per the layer-definition discipline.
  Both lifts are the value-thread-isomorphic identity rotation (the L1/L2 signature has no kernel
  fusion / element loop exposed, making it L2-native / L3-native by construction; no additional
  structure required for the lift).