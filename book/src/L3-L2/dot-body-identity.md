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
