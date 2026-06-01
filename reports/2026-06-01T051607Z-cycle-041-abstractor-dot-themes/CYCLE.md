---
agent: abstractor
invoked_at: 2026-06-01T051607Z
scope: TWO adjacent thin-identity lowering themes for `dot` — L2>L1 (`dot-leaf-identity`) + L3>L2 (`dot-body-identity`)
status: pending
integrated_at: 2026-06-01T062913Z
integration_commit: c1f7ea3c651e65ed212aa8500c7c8572aaa2ec92
integration_notes: "Applied clean (staging row D4). L2-L1/dot-leaf-identity.md + L3-L2/dot-body-identity.md created firm. Slug rename dot-fold-specialization->dot-leaf-identity applied (RHS is L1/dot, an identity-leaf-edge NOT a fold-dispatch). PROMOTED the LOAD-BEARING design-fork OQ dot-l2-leaf-floor-vs-fold-only-design prominently for the batch-12 meta-phase. L2>L1 firm 7->10, L3>L2 firm 2->5."
inputs:
  - reports/2026-06-01T051607Z-cycle-041-harvester-L2-dot/CYCLE.md (wave-1 D1 — the proposed `book/src/L2/dot.md` body; NOT yet on disk, lands this cycle's integration)
  - book/src/L1/dot.md (firm L1 leaf — authoritative Palace surface + L0 evidence)
  - book/src/L3/dot.md (firm L3 consumer — identity-in-form framing mirror)
  - book/src/L1-L0/dot-mutation-rotation.md (firm L1>L0 theme — the leaf's own lowering)
  - book/src/L3-L2/krylov-step-body-identity.md §"Applicability conditions" point 3 (the seven-primitive L3-native-by-signature statement; line 97)
  - book/src/L2-L1/inner-product-fold-specialization.md (sibling `-fold-specialization` precedent — fold-parent, do NOT merge)
  - book/src/L2-L1/index.md + book/src/L3-L2/index.md (theme lists — count-ownership: rows only)
  - L0 anchors (self-verified via citecheck this invocation): palace/linalg/vector.cpp:263-267 (Dot @263), :266 (self-dot `this==&y` fast path), :665-672 (hypre_SeqVectorInnerProd @671), :674-685; vector.hpp:247-253 (GlobalSum @251); test/unit/test-vector.cpp:206-207
---

# CYCLE: L2>L1 + L3>L2 thin-identity lowering themes for `dot`

## Summary

`dot` is now (as of wave-1 D1) on its way to a present floor at L2 (`book/src/L2/dot.md`, the
**leaf-floor** realization — the conjugation-axis leaf of the `inner_product` fold, rendered
as its own same-named L2 chapter, NOT merged into the fold-parent). With the firm L3 [`dot`](../../book/src/L3/dot.md)
above and the firm L1 [`dot`](../../book/src/L1/dot.md) below, the BLAS-1 inner-product leaf now
spans L3 → L2 → L1 with a present chapter at every layer — but the two adjacent **lowering
edges** between those chapters have no theme. This dispatch authors both, each
**identity-in-form on the leaf body** (the rotation work is the surrounding context, not the
reduce-to-scalar primitive itself):

- **L2>L1** (`book/src/L2-L1/dot-leaf-identity.md`) — the L2 `dot` leaf-floor lowers to the
  L1 `dot` primitive identity-in-form on the signature. The L2 layer's fusion-rotation work
  (de-fusing Palace's Hypre strided kernel / four-real-dot lift / local-then-collective
  two-step) is **not on the `dot` leaf** — it is carried by the fold-parent
  [`inner-product-fold-specialization`](../../book/src/L2-L1/inner-product-fold-specialization.md)
  for the whole conjugation / element-type / weight family. The `dot` leaf's own L2>L1 edge is
  therefore the identity, with one note deferring the fusion treatment to the fold-parent theme.

- **L3>L2** (`book/src/L3-L2/dot-body-identity.md`) — the L3 whole-tensor reduction lowers to
  the L2 fusion-form leaf identity-in-form on the body, mirroring
  [`krylov-step-body-identity`](../../book/src/L3-L2/krylov-step-body-identity.md): `dot` is one
  of the seven BLAS-1 primitives that are **L3-native by signature shape** (no per-element loop
  visible — `krylov-step-body-identity.md:97`), so the iteration rotation is already done at the
  signature level and the L3>L2 body edge is the identity.

Both narrate FORWARD (L_{n+1} LHS lowers into L_n RHS), per the high→low discipline. Both are
`firm` (the endpoints are firm / firming-this-cycle; the identity mapping is total; no
speculative operator). **No speculative L_{n+1} operators are proposed** — every endpoint is
existing vocabulary on both sides of both edges.

**LIVE DESIGN FRICTION (surfaced for the batch-12 meta-phase, NOT resolved here):** both themes
presuppose the wave-1 **D1 "same-named leaf-floor"** realization of `L2/dot`. Wave-1 D2 argued the
L2 inner-product surface should be ONLY the `inner_product` fold (no `dot` leaf at L2). If the
meta-phase adopts the **fold-only** reading, BOTH themes would need re-anchoring (the L2>L1 theme's
LHS would fold into `inner-product-fold-specialization`; the L3>L2 theme's RHS would point at the
fold-parent, not a same-named L2 `dot`). This is prominent in §Open-questions below.

## Naming decision (flagged for the integrator)

The dispatch proposed `dot-fold-specialization` (L2>L1) and `dot-body-identity` (L3>L2). I am
**adjusting the L2>L1 slug** and confirming the L3>L2 slug:

- **L3>L2: `dot-body-identity`** — KEPT. Mirrors the firm sibling `krylov-step-body-identity`
  exactly: an identity-in-form L3>L2 theme whose label says "the body is the identity." This is
  the correct cohort name for an L3>L2 identity edge.

- **L2>L1: `dot-fold-specialization` → `dot-leaf-identity`** — ADJUSTED. The `-fold-specialization`
  suffix (`inner-product-fold-specialization`, `linear-combination-fold-specialization`,
  `gram-fold-specialization`) names a theme whose **L2 LHS is a fold that DISPATCHES to L1 leaves
  by an axis** (conjugation / arity / matrix-lift). This `dot` L2>L1 theme is the **opposite shape**:
  its L2 LHS is *itself the leaf* `dot`, lowering identity-in-form to the *same* L1 leaf `dot` — no
  fold, no dispatch axis, no specialization. Calling it `dot-fold-specialization` would (a) misname
  an identity-leaf-lowering as a fold-dispatch, and (b) collide conceptually with the EXISTING
  `inner-product-fold-specialization`, whose RHS *is* `L1/dot` (the fold→leaf dispatch that already
  lands on `dot`). `dot-leaf-identity` is the cohort-consistent name: it pairs with
  `dot-body-identity` (both are `dot-*-identity` thin-identity themes for the BLAS-1 leaf, one per
  edge), and it reads as "the L2 leaf is the identity of the L1 leaf." Integrator: use
  `dot-leaf-identity` for the L2>L1 chapter file/slug/registration.

## Proposed changes

```new:book/src/L2-L1/dot-leaf-identity.md
# dot-leaf-identity

The L2>L1 lowering theme for the `dot` inner-product leaf. The rewrite is **identity-in-form on
the leaf**: the L2 [`dot`](../L2/dot.md) leaf-floor lowers to the L1 [`dot`](../L1/dot.md)
primitive with the same signature, the same reduce-to-scalar semantics, and the same algebraic
laws — value-thread-isomorphic on the primitive. The L2 layer's fusion-rotation work (de-fusing
Palace's fused reduction kernels) is **not on this leaf**; it is carried by the fold-parent
[`inner-product-fold-specialization`](./inner-product-fold-specialization.md) for the whole
conjugation / element-type / weight family. This theme records the identity edge and defers the
fusion treatment to the fold-parent.

## Slug

`dot-leaf-identity`

## Context

`dot` at L2 is the **leaf-floor** entry (`book/src/L2/dot.md`, harvested cycle-041 wave-1): the
conjugation-axis leaf of the L2 fold-parent [`inner_product`](../L2/inner_product.md), rendered as
its own same-named L2 chapter so the firm L3 [`dot`](../L3/dot.md) leaf rests on an adjacent
same-named L2 parent (per CLAUDE.md §Methodology invariants **Identity-lowerings still require both
L levels**) rather than skipping a layer to L1. This theme is the L2>L1 edge of that floor.

The edge is the **identity-in-form** case: the L2 `dot` leaf and the L1 `dot` leaf are
value-thread-isomorphic on the primitive. This is the L2>L1 analogue of the L3>L2
[`dot-body-identity`](../L3-L2/dot-body-identity.md) theme (the other thin edge of the same leaf),
and a sibling shape to the L3>L2 [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md)
(identity-in-form on a kernel body) — except here the identity is on a single leaf, not a
multi-primitive body.

**Why this edge is identity while its fold-parent sibling is not.** The L2 fusion rotation for the
inner-product cohort — de-fusing Palace's three fused reduction shapes (the real Hypre
`hypre_SeqVectorInnerProd` strided pass, the complex four-real-dot lift, the local-then-collective
two-step) into the canonical `foldl` reduction, plus the value-level `xᴴ y` ↔ `yᴴ x` conjugate-pair
re-order and the pinned reduction tree — is **the fold-parent's job**. The firm
[`inner-product-fold-specialization`](./inner-product-fold-specialization.md) theme carries all of
it for the whole family (conjugation / element-type / weight). The `dot` leaf is the plain (`M = I`)
Hermitian / symmetric member of that fold; restricting the fold-parent's fusion content to the plain
leaf leaves **no fusion structure unique to `dot`** (wave-1 D1 §"Fusion note" / §Open-questions found
no leaf-unique fusion surplus). So the `dot` leaf's own L2>L1 edge — the rotation between the L2 `dot`
chapter and the L1 `dot` chapter — is the identity, with the fusion treatment deferred to the
fold-parent theme.

## L2 form (LHS)

The L2 form is the `dot` leaf-floor (`book/src/L2/dot.md` §Signature, harvested cycle-041 wave-1) —
the mutation-free reduce-to-scalar reduction, with its unconjugated co-variant `tdot`:

    dot   :: (x: Tensor[N], y: Tensor[N]) -> Scalar
    tdot  :: (x: Tensor[N], y: Tensor[N]) -> Scalar     -- complex-only co-variant

    dot(x, y)  = Σᵢ kernel(x[i], y[i])                  -- Hermitian (complex) / symmetric (real)
    tdot(x, y) = Σᵢ x[i]·y[i]                            -- unconjugated bilinear (complex)

with the conjugation-by-element-type kernel inherited unchanged from the L1 leaf and the fold-parent:

    | element type | operator | per-element kernel        |
    |--------------|----------|---------------------------|
    | real         | dot      | x[i] · y[i]               |
    | complex      | dot      | conj(x[i]) · y[i]         |
    | complex      | tdot     | x[i] · y[i]               |

The L2 form is **pure / out-of-place** (no destination buffer; the result is a fresh `Scalar`), with
the arg-1-conjugated convention `dot(x, y) = xᴴ y` pinned (matching both the L1 leaf and the
fold-parent). The MPI collective and the self-dot `&x == &y` fast path are NOT in the L2 signature —
they reappear only at the L1>L0 lowering (`book/src/L1-L0/dot-mutation-rotation.md`).

## L1 form (RHS)

The L1 form is the firm `dot` leaf primitive (`book/src/L1/dot.md` §Signature, firm cycle-002) —
identical in signature, semantics, and laws:

    dot   :: (x: Tensor[N], y: Tensor[N]) -> Scalar
    tdot  :: (x: Tensor[N], y: Tensor[N]) -> Scalar     -- complex-only variant

    dot(x, y) = Σ_{i ∈ [0, N)} kernel(x[i], y[i])       -- same per-element kernel table

The L1 leaf is the **mutation-rotation** rendering: it already erases the L0 destination buffer
(there is none — `dot` returns a scalar), folds the MPI collective into the L1>L0 lowering, and
erases the L0 receiver-vs-argument conjugation asymmetry (the L1 signature names the conjugated
argument first by convention). The L1 entry is authoritative on every Palace-surface fact; the L2
form does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the leaf**. Every L2 binding maps to the same L1 binding at the
same position:

    | L2 leaf (`L2/dot`)         | L1 leaf (`L1/dot`)        | Mapping  |
    |----------------------------|---------------------------|----------|
    | `dot  :: (x, y) -> Scalar` | `dot  :: (x, y) -> Scalar`| Identity. Same signature shape. |
    | `tdot :: (x, y) -> Scalar` | `tdot :: (x, y) -> Scalar`| Identity. Same signature shape. |
    | `dot(x, y) = Σ conj-kernel`| `dot(x, y) = Σ conj-kernel`| Identity. Same per-element kernel table; same arg-1-conjugated convention. |
    | reduce-to-scalar `foldl`   | reduce-to-scalar `foldl`  | Identity. Same length-axis collapse; same order-agnostic-for-value / pinned-tree-for-bits split. |
    | algebraic laws 1–13        | algebraic laws 1–13       | Identity. Inherited unchanged (sesquilinear / bilinear facts + the IEEE non-law). |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the mapping
is total and bijective on the leaf. This is the identity-in-form property.

**The one note (fusion deferral).** The L2 layer's defining work is kernel-fusion de-fusion. For the
inner-product cohort, that work is carried entirely by the fold-parent
[`inner-product-fold-specialization`](./inner-product-fold-specialization.md): the real Hypre
`hypre_SeqVectorInnerProd` strided pass (`palace/linalg/vector.cpp:665-672`), the complex
four-real-dot lift (`palace/linalg/vector.cpp:674-685`), the local-then-collective two-step
`LocalDot ∘ Mpi::GlobalSum` (`palace/linalg/vector.hpp:247-253`), the `xᴴ y` ↔ `yᴴ x` conjugate-pair
re-order, and the pinned reduction tree. The `dot` leaf restricts that to the plain (`M = I`)
Hermitian / symmetric member; **no fusion structure is unique to the leaf beyond the fold-parent's**.
So this theme's edge is the identity, and bit-reproduction / re-order / reduction-tree concerns are
read off the fold-parent theme's §"Summation-order recording" and §"The conjugate-pair re-order",
not re-derived here.

## Applicability conditions

The identity rewrite is valid when:

1. **The L2 `dot` is the leaf-floor realization** (`book/src/L2/dot.md`, the same-named
   conjugation-axis leaf of `inner_product`) — NOT the fold-parent. If the L2 inner-product surface
   were the fold-only realization (no `dot` leaf at L2 — the wave-1 D2 reading), this theme's LHS
   would not exist as a standalone L2 `dot` chapter, and the L2>L1 edge for `dot` would be subsumed
   into [`inner-product-fold-specialization`](./inner-product-fold-specialization.md)'s conjugation
   dispatch. This condition records the design presupposition explicitly (see this theme's authoring
   report §Open-questions and the batch-12 meta-phase OQ).

2. **The leaf is value-thread-isomorphic across the edge.** The L2 `dot` leaf and the L1 `dot` leaf
   share the signature, the per-element kernel table, the arg-1-conjugated convention, and the
   algebraic laws. Confirmed by construction: `L2/dot` is authored as a thin floor entry whose laws
   are inherited unchanged from `L1/dot` (wave-1 D1 §"Algebraic laws", §Signature).

3. **All fusion content is the fold-parent's.** No fusion structure unique to the `dot` leaf (beyond
   the fold-parent's family-level de-fusion) exists; the leaf's edge is therefore the identity with a
   single deferring note (wave-1 D1 §"Fusion note" / §Open-questions: no leaf-unique fusion surplus
   found).

If a future L2 `dot` variant introduced leaf-specific fusion not absorbed by the fold-parent, the
identity claim would need re-audit — none exists in the current surface.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `dot` leaf's signature shape (`(x: Tensor[N], y: Tensor[N]) ->
Scalar`) is identical to the L1 `dot` leaf's signature shape — a whole-tensor reduce-to-scalar with
no element loop exposed at either layer. The rotation between two value-thread-isomorphic leaves with
identical signatures is the identity by construction; the only L2-layer work (fusion de-fusion) is
carried by the fold-parent, leaving the leaf's own edge a no-op.

**Empirical-match (secondary)**: the L1 leaf is firm on direct Palace evidence (`L1/dot` §Evidence,
including the value-asserting test `test/unit/test-vector.cpp:206-207`, `vec1 * vec2 = 32.0`), and the
L2 leaf-floor was authored as value-thread-isomorphic to it; the two forms agree on every law and
every variant axis by independent transcription. The identity is observational on the two existing
firm/firming chapters, not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `dot` leaf-floor (firming
cycle-041 wave-1, D1), the L1 RHS is the firm `dot` leaf (firm cycle-002, co-defines `dot` + `tdot`).
This theme is the identity edge between existing chapters; it proposes no new operators.

One evidentiary caveat carries over unchanged from the leaves (NOT a status reduction on the theme —
the identity structure is firm):

- **`tdot` is type-API-surface-only.** `ComplexVector::TransposeDot` has zero Palace call sites
  (declaration `palace/linalg/vector.hpp:112` + definition `palace/linalg/vector.cpp:269` only; per
  `L1/dot` and `inner-product-fold-specialization` §"Speculative L1 operators"). The unconjugated arm
  is structurally firm but behaviorally unexercised; the theme's behavioral weight is on the
  Hermitian `dot` arm (CG / orthogonalization / NLEPS sites). The identity edge is unaffected — the
  `tdot` leaf maps identity-in-form whether or not it is exercised.

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/dot.md` (firming cycle-041 wave-1, D1) — the L2 leaf-floor (LHS): the same-named
  conjugation-axis leaf of `inner_product`, value-thread-isomorphic to the L1 leaf, laws inherited
  unchanged. (The chapter lands at this cycle's integration alongside this theme — wave-2 serial
  sequencing applies D1 before this theme.)
- `book/src/L1/dot.md` (firm cycle-002) — the L1 leaf (RHS): signature (`:16-18`), the
  arg-1-conjugated convention (`:43`), the per-element kernel table (`:31-35`), the algebraic laws
  (`:55-81`), the complete L0 evidence list (`:109-119`). Authoritative on every Palace-surface fact.
- `book/src/L2-L1/inner-product-fold-specialization.md` (firm cycle-019) — the fold-parent theme this
  leaf's fusion content defers to: §"The dispatch rewrite (L2 → L1)", §"The conjugate-pair re-order",
  §"Summation-order recording". The `dot` leaf is the plain Hermitian / symmetric member of that
  fold's conjugation dispatch.

L0 evidence (transitive through the firm L1 leaf / the fold-parent; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body (the Hermitian kernel), with the
  `&y == this` self-dot imag=`0.0` fast path at `:266`. **Self-verified (anchor `Dot` @263; `this`
  @266).** Inherited transitively; the leaf's edge is identity so no new L0 claim is made here.
- `palace/linalg/vector.cpp:665-672` — `LocalDot(Vector, Vector)` real path via a single Hypre
  `hypre_SeqVectorInnerProd` (`:671`). **Self-verified (anchor `hypre_SeqVectorInnerProd` @671).**
  Fusion content deferred to the fold-parent.
- `palace/linalg/vector.hpp:247-253` — the `linalg::Dot` template `= Mpi::GlobalSum ∘ LocalDot` (the
  local-then-collective two-step; collective folded out per single-rank scope). **Self-verified
  (anchor `GlobalSum` @251).** Reappears only at the L1>L0 lowering.
- `test/unit/test-vector.cpp:206-207` — real-vector dot value-assertion `vec1 * vec2 = 32.0`;
  L0-equivalent semantic documentation for the real leaf (inherited from `L1/dot`).

## Status

`firm` — the L2 LHS is the firm-this-cycle leaf-floor (D1 wave-1), the L1 RHS is the firm `dot` leaf
(cycle-002), and the rotation between two value-thread-isomorphic leaves with identical signatures is
the identity by construction (§"The rewrite (L2 → L1)" table is total and bijective on the leaf). The
only L2-layer work — kernel-fusion de-fusion — is carried by the firm fold-parent
[`inner-product-fold-specialization`](./inner-product-fold-specialization.md) for the whole family;
no fusion structure is unique to the `dot` leaf (wave-1 D1 found no leaf-unique surplus). No
speculative operator, no negative-anchor reconstruction, no literature inference.

> **Design-presupposition note (not a status reduction).** This theme presupposes the wave-1 **D1
> "same-named leaf-floor"** realization of `L2/dot` (Applicability condition 1). Under the wave-1 D2
> "fold-only" reading (no `dot` leaf at L2), this theme's LHS would not exist standalone and the edge
> would fold into `inner-product-fold-specialization`. Surfaced for the batch-12 meta-phase to
> adjudicate (OQ `dot-l2-leaf-floor-vs-fold-only-design`); the theme is self-coherent under the
> leaf-floor reading it is built on.

> **Member-level caveat (not a status reduction; inherited from the leaves).** `tdot`'s unconjugated
> arm is type-API-surface-only (zero Palace call sites — `vector.hpp:112` decl + `vector.cpp:269` def
> only). The identity edge maps it identity-in-form regardless; behavioral weight is on the Hermitian
> `dot` arm.
```

```new:book/src/L3-L2/dot-body-identity.md
# dot-body-identity

The L3>L2 lowering theme for the `dot` inner-product leaf. The rewrite is **identity-in-form on the
body**: the L3 [`dot`](../L3/dot.md) whole-tensor reduction lowers to the L2 [`dot`](../L2/dot.md)
fusion-form leaf with the same signature, the same reduce-to-scalar semantics, and the same algebraic
laws — value-thread-isomorphic on the primitive. `dot` is one of the seven BLAS-1 primitives that are
**L3-native by signature shape** (no per-element loop visible at either layer), so the iteration
rotation is already complete at the signature level and the L3>L2 body edge is the identity. This is
the BLAS-1-leaf analogue of [`krylov-step-body-identity`](./krylov-step-body-identity.md) (which is
identity-in-form on a multi-primitive kernel body); here the identity is on a single leaf.

## Slug

`dot-body-identity`

## Context

`dot` spans three present chapters — firm L3 [`dot`](../L3/dot.md) (the iteration-rotation rendering,
consumed inside the `krylov-step` body), the L2 [`dot`](../L2/dot.md) leaf-floor (harvested cycle-041
wave-1), and firm L1 [`dot`](../L1/dot.md) (the mutation-rotation leaf). This theme is the **L3>L2
edge** between the top two; the L2>L1 edge below is [`dot-leaf-identity`](../L2-L1/dot-leaf-identity.md).

The edge is the **identity-in-form** case. The firm L3 entry already records its lowering as
identity-in-form (`book/src/L3/dot.md` §"Lowers to"); historically it pointed straight at L1 (no L2
`dot` chapter existed), citing the non-adjacent in-line-identity convention. With the L2 `dot`
leaf-floor now present, this theme supplies the **adjacent-edge** L3>L2 rotation the L3 entry's
§"Lowers to" had to skip — so the L3 leaf can lower to an adjacent same-named L2 parent (per CLAUDE.md
§Methodology invariants **Identity-lowerings still require both L levels**) rather than non-adjacently
to L1.

`dot` is **L3-native by signature shape**. The L3>L2 [`krylov-step-body-identity`](./krylov-step-body-identity.md)
§"Applicability conditions" point 3 (`krylov-step-body-identity.md:97`) names the seven BLAS-1
primitives — `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal` — that "each operates
on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation
identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native
because its signature has no per-element loop visible)." `dot`'s signature
`(x: Tensor[N], y: Tensor[N]) -> Scalar` exposes no element loop; the reduction over the length axis
`N` is a single semantic step at both L3 and L2. The iteration rotation is therefore already done at
the signature level, and the L3>L2 body edge is the identity.

## L3 form (LHS)

The L3 form is the whole-tensor reduction (`book/src/L3/dot.md` §Signature, firm cycle-011):

    dot   :: Tensor[N] -> Tensor[N] -> Scalar
    tdot  :: Tensor[N] -> Tensor[N] -> Scalar     -- complex-only variant

    dot(x, y) = Σ_{i ∈ [0, N)} kernel(x[i], y[i])  -- single semantic step; no element loop

rendered as **one node in the iteration-rotation calculus** (`L3/dot` §"Iteration-rotation marker"):
the reduction over the length axis lifts as a whole-tensor operation with no sequential obstruction
(the independent length-axis indices reduce in parallel in exact arithmetic; the pinned reduction
tree at L0 is a floating-point implementation choice, recorded as a non-law, not a structural element
of the L3 form). The conjugation-by-element-type kernel and the arg-1-conjugated convention are
inherited unchanged from L1.

## L2 form (RHS)

The L2 form is the `dot` leaf-floor (`book/src/L2/dot.md` §Signature, harvested cycle-041 wave-1) —
the fusion-rotation rendering of the same reduce-to-scalar reduction:

    dot   :: (x: Tensor[N], y: Tensor[N]) -> Scalar
    tdot  :: (x: Tensor[N], y: Tensor[N]) -> Scalar     -- complex-only co-variant

    dot(x, y) = Σᵢ kernel(x[i], y[i])                    -- Hermitian (complex) / symmetric (real)

It is the conjugation-axis leaf of the L2 fold-parent [`inner_product`](../L2/inner_product.md), the
plain (`M = I`) Hermitian / symmetric member, rendered as its own same-named L2 chapter. The L2 form's
fusion-rotation content (de-fusing Palace's fused reduction kernels) is the fold-parent's; the leaf
itself is value-thread-isomorphic to the L3 form on the signature.

## The rewrite (L3 → L2)

The rewrite is the **identity on the body**. Every L3 binding maps to the same L2 binding at the same
position:

    | L3 leaf (`L3/dot`)              | L2 leaf (`L2/dot`)             | Mapping  |
    |--------------------------------|--------------------------------|----------|
    | `dot :: Tensor[N] -> ... -> Scalar` | `dot :: (x, y) -> Scalar` | Identity. Same whole-tensor signature; the Haskell-arrow vs tuple presentation is notational only, no shape change. |
    | `tdot :: ... -> Scalar`        | `tdot :: (x, y) -> Scalar`     | Identity. Same signature shape. |
    | `dot(x, y) = Σ conj-kernel`    | `dot(x, y) = Σ conj-kernel`    | Identity. Same per-element kernel table; same arg-1-conjugated convention. |
    | reduce-to-scalar single step   | reduce-to-scalar `foldl`       | Identity. Same length-axis collapse; the L3 "single semantic step" IS the L2 fold over `N`. |
    | algebraic laws 1–13            | algebraic laws 1–13            | Identity. Inherited unchanged across the chain (sesquilinear / bilinear facts + the IEEE non-law). |
    | no sequential obstruction      | no sequential obstruction      | Identity. The reduction lifts as a whole-tensor op at both layers; the pinned tree is an L0 non-law, not an L2/L3 structural element. |

The mapping is total and bijective on the leaf body: every L3 binding has an L2 partner and every L2
binding has an L3 partner. This is the **identity-in-form** property. Unlike
[`krylov-step-body-identity`](./krylov-step-body-identity.md), there is **no wrapper around the
body** to carry a surface adjustment — `dot` is a single leaf, not a kernel body inside an
`IterState`/outer-driver wrapper; the L3>L2 edge is the pure identity with no wrapper-level rotation.

## Applicability conditions

The identity rewrite is valid when:

1. **`dot` is L3-native by signature shape.** Its signature `(x: Tensor[N], y: Tensor[N]) -> Scalar`
   exposes no per-element loop at L2 or L3; the reduction over `N` is a single semantic step at both
   layers. This is the load-bearing condition (per `krylov-step-body-identity.md:97`, which names
   `dot` among the seven L3-native primitives). Satisfied by construction: `dot` is a leaf reduction.

2. **The L2 form is the same-named leaf-floor** (`book/src/L2/dot.md`), value-thread-isomorphic to the
   L3 leaf. If the L2 inner-product surface were the fold-only realization (no `dot` leaf at L2 — the
   wave-1 D2 reading), the L3 leaf's adjacent L2 parent would be the fold-parent `inner_product` (the
   L3>L2 edge would lower to the fold, not to a same-named L2 `dot`), and this theme's RHS would
   re-anchor. This condition records the design presupposition explicitly (see this theme's authoring
   report §Open-questions and the batch-12 meta-phase OQ).

3. **The leaf is value-thread-isomorphic across the edge.** The L3 `dot` leaf and the L2 `dot` leaf
   share the signature, the per-element kernel table, the arg-1-conjugated convention, and the
   algebraic laws. Confirmed by construction: both chapters inherit the laws unchanged from the firm
   L1 leaf.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: `dot`'s signature is whole-tensor reduce-to-scalar with no element loop
exposed at either L2 or L3 — the L3-native-by-signature property (`krylov-step-body-identity.md:97`).
A primitive that is L3-native by signature shape rotates L3→L2 as the identity by construction: there
is no iteration to rotate (the reduction is already a single semantic step at both layers) and no
wrapper around the leaf to adjust. This is the same structural argument the
`krylov-step-body-identity` theme makes for the seven-primitive body, applied to the single `dot`
leaf.

**Empirical-match (secondary)**: the L3 leaf-floor and the L2 leaf-floor were authored independently
(L3 cycle-011, L2 cycle-041 wave-1) as value-thread-isomorphic to the same firm L1 leaf, and they
agree on every law, every variant axis, and every signature row by independent transcription. The
identity is observational on the two existing firm/firming chapters.

## Speculative L2 operators

**None.** Both endpoints are existing vocabulary: the L3 LHS is the firm `dot` leaf (firm cycle-011),
the L2 RHS is the `dot` leaf-floor (firming cycle-041 wave-1, D1). This theme is the identity edge
between existing chapters; it proposes no new operators. (The same `tdot` type-API-surface-only
evidentiary caveat that the sibling [`dot-leaf-identity`](../L2-L1/dot-leaf-identity.md) carries
applies here too — the unconjugated arm maps identity-in-form whether or not it is exercised; not a
status reduction.)

## Verified-against

L3 / L2 anchors (the two endpoints):

- `book/src/L3/dot.md` (firm cycle-011) — the L3 leaf (LHS): the whole-tensor reduce-to-scalar
  signature (`:30-33`), the iteration-rotation marker / no-sequential-obstruction statement
  (`:64-68`), the per-element kernel table (`:46-50`), the L3-native-by-signature note citing
  `krylov-step-body-identity.md:97` (`L3/dot.md:52`). The §"Lowers to" (`:127-131`) currently records
  identity-in-form to L1 via the non-adjacent convention; this theme supplies the now-present adjacent
  L3>L2 edge (downstream-consistency touch on the L3 entry flagged in §Open-questions of the authoring
  report).
- `book/src/L2/dot.md` (firming cycle-041 wave-1, D1) — the L2 leaf-floor (RHS): the same-named
  conjugation-axis leaf of `inner_product`, value-thread-isomorphic to the L1/L3 leaf, laws inherited
  unchanged. (Lands at this cycle's integration alongside this theme.)
- `book/src/L3-L2/krylov-step-body-identity.md:97` — §"Applicability conditions" point 3: the
  load-bearing statement that the seven BLAS-1 primitives (including `dot`) are L3-native by signature
  shape (no per-element loop visible), which is the structural justification for this identity edge.
  **Self-verified (anchor `L3-native` @97).**

L0 evidence (transitive through the firm L1 leaf; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body (the Hermitian kernel), with the
  `&y == this` self-dot imag=`0.0` fast path at `:266`. **Self-verified (anchor `Dot` @263; `this`
  @266).** Inherited transitively; the leaf's edge is identity, no new L0 claim.
- `palace/linalg/vector.hpp:247-253` — the `linalg::Dot` template `= Mpi::GlobalSum ∘ LocalDot` (the
  local-then-collective two-step; collective folded out per single-rank scope; reappears only at the
  L1>L0 lowering). **Self-verified (anchor `GlobalSum` @251).**
- `test/unit/test-vector.cpp:206-207` — real-vector dot value-assertion `vec1 * vec2 = 32.0`;
  L0-equivalent semantic documentation for the real leaf (inherited from `L1/dot`).

## Status

`firm` — the L3 LHS is the firm `dot` leaf (cycle-011), the L2 RHS is the firm-this-cycle leaf-floor
(D1 wave-1), and the rotation between two value-thread-isomorphic leaves with identical whole-tensor
signatures is the identity by construction (§"The rewrite (L3 → L2)" table is total and bijective on
the leaf). `dot` is L3-native by signature shape (`krylov-step-body-identity.md:97`), so the
iteration rotation is already complete at the signature level and there is no wrapper around the leaf
to adjust — the edge is the pure identity. No speculative operator, no negative-anchor reconstruction,
no literature inference.

> **Design-presupposition note (not a status reduction).** This theme presupposes the wave-1 **D1
> "same-named leaf-floor"** realization of `L2/dot` (Applicability condition 2). Under the wave-1 D2
> "fold-only" reading (no `dot` leaf at L2), this theme's RHS would re-anchor to the fold-parent
> `inner_product`. Surfaced for the batch-12 meta-phase to adjudicate (OQ
> `dot-l2-leaf-floor-vs-fold-only-design`); the theme is self-coherent under the leaf-floor reading it
> is built on.
```

```edit:book/src/L2-L1/index.md
| [inner-product-fold-specialization](./inner-product-fold-specialization.md) | `L2/inner_product` (firm) | `L1/dot` (firm; `dot` + `tdot`) + `L1/bilinear-form` (rough-in, M-weighted member) | firm *(algebraic; conjugation-convention / element-type / weight dispatch + value-level `xᴴ y`↔`yᴴ x` conjugate-pair re-order + pinned reduction tree)* |
| [dot-leaf-identity](./dot-leaf-identity.md) | `L2/dot` (firm, cycle-041 leaf-floor) | `L1/dot` (firm; `dot` + `tdot`) | firm *(structural; identity-in-form on the inner-product leaf — value-thread-isomorphic signature; all L2-layer fusion deferred to the fold-parent `inner-product-fold-specialization`; thin floor-edge of the BLAS-1 leaf)* |
```

> **Anchor note for the integrator:** the new `dot-leaf-identity` row is inserted immediately AFTER
> the existing `inner-product-fold-specialization` row in the §"Theme list" table (so the leaf-edge
> sits adjacent to its fold-parent's edge). The anchor block above reproduces the existing
> `inner-product-fold-specialization` row verbatim followed by the new row. **Count-ownership: this
> report does NOT touch the §"Vocabulary cohort" "Firm at L2>L1" running list or any consolidated
> tally — D7 (layer-intro-author) owns those this cycle.** The dep-map row is the only `L2-L1/index.md`
> mutation here.

```edit:book/src/L3-L2/index.md
| [`krylov-step-body-identity`](./krylov-step-body-identity.md) | L3 form per [`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — value-threaded `(op, K, s) -> (K', s', outputs)`, five-primitive-group let-chain (`apply_linop`, optional `op.orthog`/`op.scalars`, `axpy`/`axpby`/`axpbypcz`, `dot`/`nrm2`/`scal`, `derived_views`) plus explicit `s' = s { it = s.it + 1 }` counter-update. | L2 [`krylov-step`](../L2/krylov-step.md) §Semantics — primitive-composition form with consolidated `IterState` record absorbing the L3 `(K, s)` split; same five-primitive-group composition, outer driver referenced by role. | `empirical-match` (cycle-002 combinator-miner claim; cycle-006 audit confirmed-with-refinement) + secondary `structural` (each L1 primitive's signature shape is whole-tensor by construction) | `firm` (cycle-007 abstractor at `firm-rough-in`; promoted cycle-009 via status-inheritance after upstream L4>L3 theme firmed cycle-008) |
| [`dot-body-identity`](./dot-body-identity.md) | L3 [`dot`](../L3/dot.md) §Signature — whole-tensor reduce-to-scalar `dot :: Tensor[N] -> Tensor[N] -> Scalar` (+ `tdot` co-variant), single semantic step, no element loop, no sequential obstruction. | L2 [`dot`](../L2/dot.md) §Signature — the same-named conjugation-axis leaf-floor of `inner_product` (the plain `M=I` Hermitian / symmetric member), value-thread-isomorphic signature; fusion content carried by the fold-parent, not the leaf. | `structural` (`dot` is L3-native by signature shape per `krylov-step-body-identity.md:97` — no element loop, so the iteration rotation is already done at the signature level; no wrapper around the leaf) + secondary `empirical-match` (L3 + L2 leaf-floors independently authored value-thread-isomorphic to the firm L1 leaf) | `firm` (cycle-041 wave-2 abstractor; identity-in-form on the single BLAS-1 leaf — the leaf-level analogue of `krylov-step-body-identity`'s multi-primitive-body identity; presupposes the wave-1 D1 leaf-floor `L2/dot`) |
```

> **Anchor note for the integrator:** the new `dot-body-identity` row is inserted immediately AFTER
> the existing `krylov-step-body-identity` row in the §"Theme list" table. The anchor block above
> reproduces the existing `krylov-step-body-identity` row verbatim followed by the new row.
> **Count-ownership: this report does NOT touch any consolidated theme-count tally in
> `L3-L2/index.md` — D7 (layer-intro-author) owns those this cycle.** The dep-map row is the only
> `L3-L2/index.md` mutation here.

```edit:book/src/SUMMARY.md
- [krylov-step-body-identity](./L3-L2/krylov-step-body-identity.md)
- [dot-body-identity](./L3-L2/dot-body-identity.md)
```

> **SUMMARY anchor note:** under the **L3 > L2 — Lowering** Part, insert the `dot-body-identity`
> chapter line immediately after the `krylov-step-body-identity` line (anchor block reproduces the
> existing line + the new line).

```edit:book/src/SUMMARY.md
- [inner-product-fold-specialization](./L2-L1/inner-product-fold-specialization.md)
- [dot-leaf-identity](./L2-L1/dot-leaf-identity.md)
```

> **SUMMARY anchor note:** under the **L2 > L1 — Lowering** Part, insert the `dot-leaf-identity`
> chapter line immediately after the `inner-product-fold-specialization` line (anchor block
> reproduces the existing line + the new line). Both SUMMARY edits are distinct fenced blocks
> anchored on distinct existing lines, so they apply independently.

## Speculative operators proposed

**None.** Both themes are identity-in-form edges between existing vocabulary on both sides:

- **`dot-leaf-identity` (L2>L1)**: LHS `L2/dot` leaf-floor (firming cycle-041 wave-1, D1) → RHS
  `L1/dot` leaf (firm cycle-002). No new operator.
- **`dot-body-identity` (L3>L2)**: LHS `L3/dot` leaf (firm cycle-011) → RHS `L2/dot` leaf-floor
  (firming cycle-041 wave-1, D1). No new operator.

This is the correct shape for thin-identity leaf-edge themes (cf. `krylov-step-body-identity`, which
also proposes no new vocabulary — it ratifies the identity relationship between existing endpoints).
The harvester has nothing to pick up from these themes.

## Supporting evidence

- **Source of truth for the L2 `dot` form (read this invocation):** wave-1 D1 harvester report
  `reports/2026-06-01T051607Z-cycle-041-harvester-L2-dot/CYCLE.md` — the proposed `book/src/L2/dot.md`
  body (NOT yet on disk; lands at this cycle's integration alongside these themes). Both themes
  reference `L2/dot` as a (firming-this-cycle) endpoint; the wave-2 serial sequencing applies D1
  before these themes integrate.
- **Firm endpoints (read this invocation):** `book/src/L1/dot.md` (firm cycle-002 — authoritative
  Palace surface, signature, laws, variant axes, L0 evidence list); `book/src/L3/dot.md` (firm
  cycle-011 — the iteration-rotation rendering, the L3-native-by-signature note, the §"Lowers to"
  identity-in-form record); `book/src/L1-L0/dot-mutation-rotation.md` (firm — the leaf's own L1>L0
  lowering, where the MPI collective / self-dot fast path / reduction tree reappear).
- **Precedents mirrored (read this invocation):** `book/src/L3-L2/krylov-step-body-identity.md`
  (the firm identity-in-form L3>L2 sibling shape; §"Applicability conditions" point 3 / line 97 is the
  load-bearing L3-native-by-signature anchor); `book/src/L2-L1/inner-product-fold-specialization.md`
  (the firm `-fold-specialization` sibling — the fold-parent whose conjugation dispatch lands on
  `L1/dot`, and to which the `dot` leaf's L2-layer fusion content is deferred).
- **L0 self-verification (this invocation, `tools/citecheck/citecheck.py --anchor`):** four
  load-bearing anchors verified against on-disk `reference/palace/` source — `vector.cpp:263-267`
  (`Dot` @263), `vector.cpp:266` (self-dot `this==&y` fast path @266), `vector.cpp:665-672`
  (`hypre_SeqVectorInnerProd` @671), `vector.hpp:247-253` (`GlobalSum` @251); plus the two book-anchor
  lines `krylov-step-body-identity.md:97` (`L3-native` @97) and `L3/dot.md:52` (`L3-native` @52). Zero
  drift. All L0 ranges are inherited transitively (the leaf edges are identity; no new L0 claim is
  made — the citations anchor the fold-parent-deferred fusion content and the inherited self-dot law).
- **Fence-parity self-check:** both theme bodies use 4-space-indented code blocks for signatures /
  mapping tables (NOT nested ` ```text ` fences) per the
  `convert-nested-fences-to-indented-code-in-proposed-changes-block` discipline; each closing fence
  sits after the last chapter section (§Status). The dep-map and SUMMARY edits are separate fenced
  blocks. No live forward-links to unwritten files: `dot-leaf-identity` links `../L3-L2/dot-body-identity.md`
  and `dot-body-identity` links `../L2-L1/dot-leaf-identity.md` (each other) — both land THIS cycle,
  so they resolve at the post-integration build; `../L2/dot.md` also lands this cycle (D1). If the
  integrator applies these in an order where one link target is momentarily absent, the build runs
  only after all of this cycle's proposed-changes are staged, so all three resolve together.

## Open questions / caveats

- **LOAD-BEARING META-PHASE SIGNAL — `dot-l2-leaf-floor-vs-fold-only-design` (NEW OQ, for batch-12
  meta-phase).** Both themes presuppose the wave-1 **D1 "same-named leaf-floor"** realization of
  `L2/dot`: D1 built `book/src/L2/dot.md` as a same-named conjugation-axis leaf of the `inner_product`
  fold (cited as a leaf-of, explicitly NOT merged). Wave-1 **D2** argued the opposite — that the L2
  inner-product surface should be ONLY the `inner_product` fold, with NO `dot` leaf at L2. **The two
  wave-1 dispatches reached contradictory conclusions about whether `L2/dot` should exist as a
  standalone chapter.** These themes are built on the (b) D1 leaf-floor reading and are self-coherent
  under it. **If the batch-12 meta-phase adopts the D2 fold-only reading, BOTH themes need
  re-anchoring:**
  - `dot-leaf-identity` (L2>L1): its LHS (`L2/dot`) would not exist standalone; the `dot` leaf's
    L2>L1 edge would fold INTO `inner-product-fold-specialization`'s conjugation dispatch (which
    already lands on `L1/dot`). The theme would be **deleted / absorbed**.
  - `dot-body-identity` (L3>L2): its RHS would re-anchor from a same-named `L2/dot` to the fold-parent
    `L2/inner_product` (the L3 `dot` leaf would lower to the fold, not to a same-named L2 leaf). The
    theme would **survive but re-point its RHS** (and likely re-justify the adjacency, since lowering
    a same-named leaf to a differently-named fold-parent is a weaker "identity" claim).

  Each theme records this presupposition explicitly in its §"Applicability conditions" (condition 1 /
  condition 2 respectively) and a §Status "Design-presupposition note." This is **load-bearing
  meta-phase input**: the leaf-floor-vs-fold-only design decision is upstream of both themes AND of
  D1's `L2/dot` chapter itself; the meta-phase should adjudicate the design before these themes (and
  the D1 chapter) are treated as stable. **Recommend the integrator file this as OQ
  `dot-l2-leaf-floor-vs-fold-only-design` for the batch-12 meta-phase**, cross-linked to the wave-1 D1
  and D2 reports. (I did not resolve it — per dispatch directive, capture not resolve.)

- **Downstream-consistency touch on `book/src/L3/dot.md` §"Lowers to" (note only, NOT actioned).** The
  firm L3 `dot` entry's §"Lowers to" (`book/src/L3/dot.md:127-131`) currently records its lowering as
  identity-in-form **directly to L1**, citing "no `book/src/L3-L1/` directory" and the non-adjacent
  in-line-identity convention (because no L2 `dot` chapter existed when it was authored). With the L2
  `dot` leaf-floor now present (D1) and this `dot-body-identity` L3>L2 theme supplying the adjacent
  edge, the L3 entry's §"Lowers to" prose may want a light refresh to point at the new adjacent L2
  `dot` parent + this theme rather than (only) the non-adjacent L1 hop. **Out of scope for this
  abstractor** (modifying the firm L3 operator entry is harvester/lifter scope, not theme-authoring).
  Flagged for a follow-up L3-`dot` re-anchor. The wave-1 D1 harvester report flagged the same touch
  from its side; the two flags converge. (Not a defect in these themes — they are self-coherent; it is
  a downstream-consistency touch on the L3 entry that the new adjacent edge now enables.)

- **Lifting note (reverse direction — working notes only, NOT in the high→low chapter bodies).**
  Lifting an L1 `dot` leaf *up* to L2, or an L2 `dot` leaf *up* to L3, is determinate and trivial:
  each is the same leaf with the same signature, so the lift requires no additional structure (it is
  the identity in both directions). The L1→L2 lift loses (a) the pinned reduction tree and the
  arg-handedness (which live in the L1>L0 lowering, not the L1 leaf) — so re-lowering recovers the
  original Palace call only if the fold-parent's summation-order table + the operand-swap re-order are
  re-applied. The L2→L3 lift loses nothing (both are whole-tensor single-step reductions). These
  reverse-direction notes live here in working notes per the high→low layer-definition discipline; the
  formal chapter bodies narrate only L3 → L2 and L2 → L1.

- **`tdot` type-API-surface-only caveat (inherited; recorded in both theme bodies).** `tdot`'s
  unconjugated arm has zero Palace call sites (`vector.hpp:112` decl + `vector.cpp:269` def only).
  Both identity edges map it identity-in-form regardless of whether it is exercised; the caveat is a
  member-level evidentiary note inherited from the leaves, NOT a status reduction on either theme. The
  themes' behavioral weight is on the Hermitian `dot` arm. (Consistent with how
  `inner-product-fold-specialization` and `L2/dot` carry the same caveat.)

- **Naming adjustment (recorded for the integrator; see §"Naming decision" above).** The L2>L1 slug
  was adjusted from the dispatch-proposed `dot-fold-specialization` to `dot-leaf-identity` (the theme
  is an identity-leaf-lowering, NOT a fold-dispatch — `-fold-specialization` would misname it and
  collide conceptually with the existing `inner-product-fold-specialization` whose RHS already IS
  `L1/dot`). The L3>L2 slug `dot-body-identity` is kept as proposed. Integrator: use file/slug/
  registration names `dot-leaf-identity` (L2>L1) and `dot-body-identity` (L3>L2). The two names form a
  consistent `dot-*-identity` pair for the BLAS-1 leaf's two thin edges.
