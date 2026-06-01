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
