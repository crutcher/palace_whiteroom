---
agent: abstractor
invoked_at: 2026-06-01T051607Z
scope: L2>L1 + L3>L2 thin-identity nrm2 lowering themes (dispatch D5, wave-2)
status: pending
integrated_at: 2026-06-01T062913Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row D5). L2-L1/nrm2-fold-specialization.md + L3-L2/nrm2-body-identity.md created firm. Repairer fixed edit:->new: + section-anchor §Fold-cohort-boundary->§Consumer-(NOT-an-instance). Rides the design-fork. Kept -fold-specialization slug -> SLUG-NAMING tension vs D4 dot-leaf-identity (rename-reconciliation OQ for batch-12 meta-phase). L2>L1 firm 7->10, L3>L2 firm 2->5."
inputs:
  - reports/2026-06-01T051607Z-cycle-041-harvester-L2-nrm2/CYCLE.md (wave-1 D2 source-of-truth; proposed book/src/L2/nrm2.md body — lands at integration alongside these themes)
  - book/src/L1/nrm2.md (firm cycle-003; the L1 RHS of the L2>L1 theme; authoritative on Palace surface)
  - book/src/L3/nrm2.md (firm cycle-011; the L3 LHS of the L3>L2 theme)
  - book/src/L1-L0/nrm2-mutation-rotation.md (firm; the four-stage L0 chain + std::abs guard classification)
  - book/src/L3-L2/krylov-step-body-identity.md (firm; classifies nrm2 as L3-native/L2-native — §"Applicability conditions" point 3, :97)
  - book/src/L2-L1/inner-product-fold-specialization.md (firm; the -fold-specialization precedent; names nrm2 as a √∘inner_product consumer at the diagonal)
  - book/src/L2-L1/index.md + book/src/L3-L2/index.md (adjacent theme lists; dep-map row format)
  - palace/linalg/vector.hpp:255-260 (L0 anchor; verified on-disk — body line 259 `return std::sqrt(std::abs(Dot(comm, x, x)));`)
---

# CYCLE: L2>L1 + L3>L2 thin-identity nrm2 lowering themes (D5, wave-2)

## Summary

`nrm2` is the BLAS-1 Euclidean-norm reduction `α = ‖x‖₂ = √⟨x, x⟩`. The firm L3 `nrm2` (cycle-011) and the wave-1 D2 L2 `nrm2` floor (this cycle) are both **identity-in-form** on the primitive — a BLAS-1 leaf with no HPC/SIMD trick to unfold at L2 and no element loop to lift at L3 (`linalg::Norml2` is already the one-line unfolded composition `√ ∘ abs ∘ Dot`). This dispatch authors the **two adjacent thin-identity lowering themes** that complete the `nrm2` adjacent-edge chain below the firm L3 anchor: (a) `L2-L1/nrm2-fold-specialization` — how the L2 `nrm2` floor form lowers into the L1 `nrm2` primitive (identity-in-form on the primitive's signature; the only L2>L1 content is the disclosure that the `√` and `abs` scalar post-steps drop below the L1 layer's resolution and that the `std::abs` load-bearing guard, *preserved* as an explicit L2 algebraic claim, *disappears* at L1 subsumed by the non-negativity claim); (b) `L3-L2/nrm2-body-identity` — how the L3 `nrm2` whole-tensor norm lowers into the L2 `nrm2` fusion form (identity-in-form; mirrors `krylov-step-body-identity`'s point-3 classification of `nrm2` as L3-native/L2-native by signature shape). Both themes carry the **`√ ∘ inner_product` at `y=x` consumer framing** — `nrm2` is a CONSUMER of `inner_product`, NOT a fold member — through the rewrite, narrated forward high→low. Both land `firm`: the rotations are identity-in-form on positively-anchored, fully-specified source, with no constructive sub-part.

## Proposed changes

```new:book/src/L2-L1/nrm2-fold-specialization.md
# nrm2-fold-specialization

The thin-identity rotation for the BLAS-1 Euclidean-norm reduction at the fusion→mutation
edge. Lowers the L2 `nrm2` floor form (`book/src/L2/nrm2.md`, firm cycle-041) into its L1
leaf [`nrm2`](../L1/nrm2.md) (firm cycle-003). The rotation is **identity-in-form on the
primitive's signature** — the L2 and L1 forms are value-thread-isomorphic — so this theme
records not a decomposition but the two things the L2→L1 hop *does* erase: the scalar `√`
and `abs` post-steps (already below the L1 layer's resolution at both levels, but framed
*as preserved algebraic structure* at L2 and *as resolved-away IEEE-754 primitives* at L1),
and the `std::abs` load-bearing defensive guard (kept as an explicit L2 algebraic claim,
subsumed at L1 by the non-negativity claim). Narrated forward: the one L2 fusion form
**re-fuses** downward onto the single L1 leaf, carrying the `√ ∘ inner_product`-at-`y=x`
consumer framing unchanged.

This is the BLAS-1-leaf sibling of
[`inner-product-fold-specialization`](./inner-product-fold-specialization.md): that theme
dispatches a reduce-to-`Scalar` *fold* by conjugation convention onto a bounded family of
distinct L1 reduction leaves; this one lowers a *consumer* of that fold (the `√`-post-step
at the diagonal `y = x`) onto a single L1 leaf with **no dispatch** — there is exactly one
L1 `nrm2`. The `-fold-specialization` slug is carried for sibling-naming continuity (the
BLAS-1 reduce-to-scalar cohort), but `nrm2` is explicitly **not a fold member** (do-NOT-merge
per [`L2/inner_product`](../L2/inner_product.md) §"Consumer (NOT an instance)" and the wave-1 D2
`L2/nrm2` floor's "Consumer of `inner_product`, NOT a fold member"); the namesake "fold" here
is the `inner_product` fold `nrm2` *consumes* at `y = x`, not a fold `nrm2` instantiates.

## Slug

`nrm2-fold-specialization`

## L2 form (LHS)

The L2 form is the fusion-rotation composition (`L2/nrm2` §Signature / §Semantics), the
principal non-negative square root of the defensively sign-stripped Hermitian
self-inner-product at the diagonal `y = x`:

    nrm2 :: Tensor[N] -> Scalar
    nrm2 x = √ (abs (inner_product x x))        -- √ ∘ abs ∘ inner_product at y = x; always real, non-negative

The form is pure / out-of-place: it consumes a read-only `x` and produces a fresh real
`Scalar`; there is no destination buffer (the L0 in-place destination is the return register
/ a stack scalar — `nrm2-mutation-rotation` records the "mutation rotation" is essentially a
no-op on the buffer side). At L2 the reduction is the `inner_product` fold's single semantic
step over the length axis; `nrm2` **post-composes two scalar maps** (`abs`, then `√`) onto
the fold output at `y = x`. The element-type axis is already collapsed at L2 — a single
operator `nrm2 :: Tensor[N] -> Scalar(real)` regardless of whether `x` is real or complex,
because the post-composed `abs` projects the complex self-inner-product `{re, 0.0}` onto its
real magnitude before `√` (`L2/nrm2` §"Variant axes"). The `std::abs` guard is **preserved at
L2 as an explicit load-bearing numerical claim** (it implements the non-negativity invariant
for the square root under floating point; full classification at
[`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive
guard — classification").

## L1 form (RHS)

The L1 form is the **single leaf primitive** [`nrm2`](../L1/nrm2.md) (firm cycle-003) — there
is no L1 family to dispatch into (contrast the inner-product cohort's `dot`/`tdot`/`bilinear-form`):

    nrm2 :: (x: Tensor[N]) -> Scalar
    nrm2 x = √dot(x, x)                          -- L1 defining identity (algebraic law 8)

At L1 the defining identity is stated as `nrm2(x) = √dot(x, x)` (L1 algebraic law 8), where
`dot` is the firm L1 Hermitian inner product ([`L1/dot`](../L1/dot.md)). The scalar `abs` and
`√` are **below the L1 layer's resolution** — deterministic IEEE-754 primitives operating on
the single scalar the `dot` leaf produces ([`L1/nrm2`](../L1/nrm2.md) §Dependencies: "the
outer `sqrt` and `abs` are scalar operations below the L1 layer's resolution"). The element-type
axis is collapsed identically at L1 (one operator, always-real result). The L1 leaf adopts the
same `√⟨x, x⟩` defining identity as the L2 form, so the LHS→RHS rotation is
convention-preserving at the L1/L2 representation level; the L1>L0 expansion into the
four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain is the separate firm
[`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) theme, not this one.

## The rewrite (L2 → L1)

The lowering is **identity-in-form on the primitive's signature** — the L2 form and the L1
form are value-thread-isomorphic. There is **no dispatch** (one L1 leaf), **no decomposition**
(the L2 fusion rotation is a no-op for this leaf — `linalg::Norml2` is already the one-line
unfolded composition), and **no destination-buffer concern** (the result is a returned scalar).
What the rotation does is exactly two surface adjustments, both of which leave the value
unchanged:

    nrm2 x  =  √ (abs (inner_product x x))     -- L2 fusion form
            =  √dot(x, x)                       -- L1 leaf form (defining identity, law 8)

1. **The `inner_product` fold at `y = x` refuses to the `dot` leaf at the diagonal.** The L2
   form names its inner reduction as the length-axis `inner_product` fold (the firm L2 fold,
   cycle-019); at L1 the same diagonal self-inner-product is the `dot(x, x)` leaf. This is the
   *consumer's* view of the same edge the [`inner-product-fold-specialization`](./inner-product-fold-specialization.md)
   theme lowers for the fold itself: that theme's §"The diagonal degeneration (`y = x`)"
   names `nrm2` precisely as the consumer entry point (`√ ∘ inner_product` at `y = x`,
   composing an outer `√` post-step "downstream of this lowering, not a dispatch within it").
   This theme **is** that downstream composition: the inner `inner_product(x, x) → dot(x, x)`
   refusion is inherited from the inner-product theme; the `nrm2`-specific content is the
   outer `√ ∘ abs` post-step. The diagonal triggers the `&x == &y` self-dot fast path at L0
   (transparent trick — `palace/linalg/vector.cpp` returns imag `= 0.0` for the Hermitian
   self-dot), which makes `inner_product(x, x)` exactly real; the L2/L1 forms elide it
   (algebraically `xᴴ x` is non-negative real for both element types — L1 dot laws 4 / 9).

2. **The two scalar post-steps change framing, not value.** At L2 the `abs` guard is
   **preserved as an explicit load-bearing numerical claim** (the L2 fusion-rotation discipline
   keeps load-bearing numerical tricks as algebraic claims); the `√` is the principal
   non-negative real square root composed onto the fold output. At L1 both `abs` and `√` drop
   **below the layer's resolution**: the `abs` guard **disappears**, subsumed by the L1
   algebraic claim that `dot(x, x)` is non-negative real (so `abs` of it equals it exactly in
   exact arithmetic), and the `√` is a deterministic IEEE-754 scalar primitive on the leaf's
   output. Both treatments are consistent — the guard *implements* the non-negativity claim
   under floating point; it is a no-op in exact arithmetic and is **not erasable** in floating
   point without introducing a NaN failure mode on numerically-zero vectors (the full
   load-bearing-defensive classification, with the property it buys — domain-safety /
   non-negativity invariant for `√`, no NaN — lives at
   [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive
   guard — classification"). The rotation does not change the value at either resolution;
   it changes whether the guard is named (L2) or absorbed (L1).

The mapping is total and trivial on the kernel content: the single L2 `nrm2` form maps to the
single L1 `nrm2` leaf, at the same signature, producing the same value. This is the
**identity-in-form** property; the rotation is at the *framing* (fusion-rotation view of the
preserved `abs` guard at L2 → mutation-rotation view of the absorbed guard at L1), not on the
primitive.

## Applicability conditions

The rewrite preserves the L2 value when:

1. **Read-only `x`, no destination buffer.** `nrm2` never writes `x`; the L0 chain only reads
   it (the `Dot` leaf takes `const VecType &x`). There is no aliasing or destination-buffer
   applicability condition — the result is a returned scalar. This is the structurally
   simplest BLAS-1 lowering: no in-place-mutation conditions at all
   ([`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"Applicability conditions"
   point 1).

2. **Diagonal `y = x` (the consumer precondition).** The L2 form consumes the `inner_product`
   fold *at the diagonal*; the L1 leaf is `dot(x, x)`. The lowering is the `nrm2` consumer's
   instance of the inner-product theme's diagonal-degeneration entry — valid because the
   self-inner-product is exactly real and non-negative (L1 dot laws 4 / 9), so the outer
   `abs ∘ √` composition is well-defined for both element types.

3. **Element type real or complex, result always real.** The element-type axis is absorbed
   entirely by the `inner_product`/`dot` leaf and the meaning of `abs`; the surrounding scalar
   post-steps are element-type-agnostic. At L2 / L1 the axis collapses to one operator
   (`L2/nrm2` / `L1/nrm2` §"Variant axes").

4. **The `abs` guard's L2-preserved / L1-absorbed treatments are consistent.** The rotation is
   value-preserving under both the **algebraic-correctness** reading (the guard is a no-op in
   exact arithmetic, so its absorption at L1 changes nothing) and the **floating-point**
   reading (the guard implements the non-negativity invariant; bit-reproduction of the L0
   `√(abs(Dot))` requires re-introducing it at the L1>L0 edge, where
   [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) records it as stage 3 of the
   four-stage chain). This theme's value-preservation claim holds under the algebraic-correctness
   reading; the bit-reproduction caveat (the reduction-tree non-associativity inherited from
   `dot`, and the guard's NaN-avoidance role) is the load-bearing residue recorded at the
   L1>L0 leaf and at [`L1/dot`](../L1/dot.md) §Semantics.

## Justification kind

**`structural`** — the rewrite is the identity refusion of one pure L2 form onto one L1 leaf;
there is no algebraic transformation of the value (the defining identity `nrm2(x) = √dot(x,x)`,
L1 law 8, is shared verbatim across L2 and L1) and no reduction-chain content beyond the inner
`inner_product → dot` refusion inherited from the sibling fold theme. The one substantive
structural fact this theme records is the **resolution change** on the two scalar post-steps:
the `√` and `abs` are named L2 fusion-composition steps (with `abs` a preserved load-bearing
claim) and resolve to below-L1-resolution IEEE-754 primitives (with `abs` absorbed by the
non-negativity claim) across the hop. The fused reduction kernel under the `inner_product`
fold (the single Hypre pass / the four-real-dot complex lift) is a transparent-performance
trick recorded at the sibling inner-product theme's §"Summation-order recording"; this `nrm2`
consumer theme inherits that pinned reduction tree unchanged (the `√ ∘ abs` post-step does
not alter the tree).

## Speculative L1 operators

**None.** The RHS leaf [`nrm2`](../L1/nrm2.md) is existing firm vocabulary (cycle-003); the
LHS [`L2/nrm2`](../L2/nrm2.md) is firm (harvested this cycle, wave-1 D2). This theme proposes
no new operators — it is the identity-in-form lowering edge between existing vocabulary on
both sides. The B-weighted overload `linalg::Norml2(comm, x, B, Bx) = √(xᴴ B x)`
(`palace/linalg/operator.cpp:600-619`, declared `palace/linalg/operator.hpp:372-374`) shares the L0 symbol
via overloading but is a **different operator** with a different L1 referent
([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md), rough-in) — it consumes the
M-weighted member of `inner_product` (`xᴴ M y`), requires the operator-application primitive
and a workspace `Bx`, and is the subject of a separate forthcoming theme. Named here only to
mark the boundary; **not** part of this theme.

## Verified-against

L1 / L2 anchors:

- [`book/src/L2/nrm2.md`](../L2/nrm2.md) (firm cycle-041, wave-1 D2) — the L2 LHS: the
  fusion-rotation form `√ ∘ abs ∘ inner_product` at `y = x`, the consumer-not-fold-member
  boundary, the preserved `std::abs` load-bearing claim, the always-real element-type collapse.
- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — the L1 RHS leaf: defining identity
  law 8 (`nrm2(x) = √dot(x, x)`, `:53`), the `abs`/`√`-below-resolution framing (§Dependencies,
  `:66`), the always-real element-type collapse (§"Variant axes", `:74`), the `abs`-guard-disappears-at-L1
  note (§Semantics, `:36`).
- [`book/src/L1-L0/nrm2-mutation-rotation.md`](../L1-L0/nrm2-mutation-rotation.md) (firm) — the
  full `std::abs` defensive-guard classification (load-bearing-defensive; property bought =
  non-negativity invariant for the square root, no NaN); the four-stage L0 chain the L1>L0 edge
  re-introduces (NOT this theme's content).
- [`book/src/L2-L1/inner-product-fold-specialization.md`](./inner-product-fold-specialization.md)
  (firm) — the sibling reduce-to-scalar fold theme whose §"The diagonal degeneration (`y = x`)"
  names `nrm2` as the consumer entry point (`√ ∘ inner_product` at `y = x`); this theme is the
  downstream `√ ∘ abs` composition that entry point references.

L0 anchor (verified on-disk via `sed`/read this invocation — producer-self-verification):

- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is
  `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing line; the one-line
  unfolded composition that makes the L2→L1 fusion rotation a no-op. (Path relative to
  `reference/palace/`; the full L0 evidence list lives at [`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Status

`firm` — the L2 LHS is firm (harvested this cycle, wave-1 D2), the L1 RHS leaf is firm
(cycle-003), and the rotation is identity-in-form on the primitive's signature: one L2 form,
one L1 leaf, same value, same defining identity (law 8). No dispatch (single leaf), no
decomposition (the fusion rotation is a no-op — `linalg::Norml2` is already the one-line
unfolded composition), no destination buffer (returned scalar), no speculative operator, no
constructive sub-part (every claim is positively anchored on fully-specified source; the
`std::abs`-guard classification it cites is itself firm at the L1>L0 leaf). The only L2>L1
content is the resolution change on the two scalar post-steps (`√`/`abs` named at L2 → below
L1 resolution; `abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1).
This is a BLAS-1-leaf thin-identity theme — the consumer sibling of the
[`inner-product-fold-specialization`](./inner-product-fold-specialization.md) fold theme — under
the 2026-05-31 `l2-floor-under-l3-blas1-cohort` foundation-first directive: it completes the
adjacent-edge chain below the firm L3 [`nrm2`](../L3/nrm2.md) anchor. A `lowering-verifier`
audit attaching a `verified_against:` block (per the sibling-theme convention) confirming the
identity-in-form rotation against the L0 corpus is the standard follow-up, not a status reduction.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in the high→low chapter body).**
  Lifting the L1 `nrm2` leaf *up* to the L2 floor form is determinate: the L1 leaf IS the L2
  form with the `√ ∘ abs` post-step re-named as preserved fusion-composition structure and the
  inner `dot(x, x)` re-named as the `inner_product` fold at the diagonal. The lift requires no
  additional structure (no dispatch to resolve, no buffer to thread). The lift loses (a) the
  pinned reduction tree (inherited from the `inner_product`/`dot` leaf — the L2 form is
  order-agnostic for value) and (b) nothing on the conjugation/handedness axis (the diagonal
  self-inner-product is convention-blind — `xᴴ x = xᵀ x = Σ|x[i]|²`), so the lift is
  value-faithful but NOT bit-faithful — re-lowering recovers the original Palace call only if
  the inner-product theme's summation-order table is re-applied. This reverse-direction note
  lives here per the high→low layer-definition discipline; the formal chapter narrates only
  L2 → L1.

- **The nrm2 floor's existence rides the `l2-floor-under-l3-blas1-cohort` design decision
  (live meta-phase friction — captured, not resolved here).** The wave-1 D2 harvester (this
  theme's L2 source-of-truth) framed `nrm2` as a consumer-of-fold and separately argued that
  **no `L2/dot` leaf is needed** (the L2 inner-product surface is the `inner_product` *fold*,
  not a `dot` leaf). The leaf-vs-fold fork is under meta-phase adjudication. **This theme is
  unaffected by the `dot` question** — `nrm2` consumes `inner_product` (the fold) either way,
  and there is exactly one L1 `nrm2` leaf to lower onto regardless — but the existence of the
  L2 `nrm2` *floor* (and therefore this L2>L1 theme's LHS) rides the same
  `l2-floor-under-l3-blas1-cohort` decision. If the meta-phase rules that BLAS-1 leaves should
  NOT get L2 floors (the identity-in-form floor is redundant with the L3 anchor + the L1
  leaf), this theme's LHS would dissolve and the theme would re-home as an in-line identity
  note at `L3/nrm2` (per the non-adjacent-identity in-line-annotation convention). Flagged for
  the meta-phase; no action in this dispatch.

- **`-fold-specialization` slug vs consumer framing (recorded for the integrator / lowering-verifier).**
  The slug `nrm2-fold-specialization` is carried for sibling-naming continuity with the BLAS-1
  reduce-to-scalar cohort (`inner-product-fold-specialization`,
  `linear-combination-fold-specialization`), but `nrm2` is a CONSUMER of the `inner_product`
  fold, not a fold member, and there is no L1 family to "specialize" into (single leaf). The
  body makes this explicit (intro + §"The rewrite" point 1). If a future audit prefers a
  slug that names the consumer relationship (e.g. `nrm2-norm-consumer-identity` or
  `nrm2-body-identity` symmetric with the L3>L2 sibling), that is a rename follow-up — the
  body content is slug-agnostic. Defer.
```

```new:book/src/L3-L2/nrm2-body-identity.md
# nrm2-body-identity

The L3>L2 lowering theme for the BLAS-1 Euclidean-norm reduction. Lowers the L3 `nrm2`
whole-tensor norm (`book/src/L3/nrm2.md`, firm cycle-011) into the L2 `nrm2` fusion form
(`book/src/L2/nrm2.md`, firm cycle-041). The rewrite is **identity-in-form on the kernel** —
the L3 whole-tensor reduction and the L2 fusion-rotation composition are value-thread-isomorphic
on the primitive's signature; there is no element loop at either layer (the reduction over the
length axis `N` is a single semantic step at both L3 and L2), and the `√ ∘ abs ∘ inner_product`
consumer framing is shared verbatim. This theme is the BLAS-1-leaf analogue of
[`krylov-step-body-identity`](./krylov-step-body-identity.md), whose §"Applicability conditions"
point 3 names `nrm2` among the seven L1 primitives that are **L3-native / L2-native by signature
shape** (no per-element loop visible). Narrated forward: the L3 whole-tensor norm **dissolves**
into the L2 fusion composition with no decomposition and no wrapper rotation — `nrm2` is a leaf
reduction, so unlike `krylov-step` there is no surrounding `(op, K, s)` consolidation or
outer-loop collapse; the identity is total.

## Slug

`nrm2-body-identity`

## Context

`nrm2` is one of the seven L1 primitives that the cycle-002 combinator-miner argument (preserved
verbatim in [`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Verified-against"
bullet 1) and the cycle-006 audit established as **L3-native / L2-native by signature shape**:
each operates on whole-tensor inputs with no element loop exposed at L2, which is what makes the
L3>L2 rotation identity-in-form rather than requiring a decomposition step
([`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Applicability conditions"
point 3, `:97`: "The seven L1 primitives used (`apply_linop`, `axpy`, `axpby`, `axpbypcz`,
`dot`, `nrm2`, `scal`) ... each operates on whole-tensor inputs with no element-loop exposed at
L2 ... each L1 primitive is *also* L3-native because its signature has no per-element loop
visible"). Where `krylov-step-body-identity` ratifies that classification for the *composite*
kernel body (the five-primitive-group let-chain) with two wrapper-level surface adjustments,
this theme ratifies it for the *single leaf* `nrm2` — and the leaf case is strictly simpler:
there is no surrounding wrapper to rotate (no `(op, K, s)` tuple to consolidate, no outer
tail-recursive loop to collapse), so the identity is total on both the kernel and its (absent)
wrapper.

The L3 `nrm2` (firm cycle-011) and the L2 `nrm2` floor (firm cycle-041, wave-1 D2) are both
**layer-coherence entries** per the methodology invariant **Identity-lowerings still require
both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009): each layer is coherent
within itself, so the reduction is defined in L3 vocabulary at L3 and L2 vocabulary at L2, and
this theme is the adjacent-edge identity rotation between them. The L2 floor exists under the
2026-05-31 `l2-floor-under-l3-blas1-cohort` foundation-first directive so the firm L3 anchor
rests on a present adjacent L2 parent; this theme completes that adjacent edge.

## L3 form (LHS)

The L3 form is the whole-tensor Euclidean-norm reduction (`L3/nrm2` §Signature / §Semantics),
rendered as an L3 field operation:

    nrm2 :: Tensor[N] -> Scalar
    nrm2 x = √dot(x, x)                          -- whole-tensor reduction; √ ∘ dot at the diagonal

The signature `Tensor[N] -> Scalar` exposes no element loop — the reduction over `i ∈ [0, N)`
is a single semantic step in the L3 iteration-rotation calculus (`L3/nrm2` §"Iteration-rotation
marker"). There is **no sequential obstruction**: the reduction over independent length-axis
indices is a parallel operation in exact arithmetic; the load-bearing pinned reduction tree at
L0 is a floating-point implementation choice (a recorded non-law), not an algebraic obstruction
at L3. At L3 `nrm2` is **consumed inside** larger forms in two roles — the convergence-test
readout `outputs.residual_norm` and the Arnoldi sub-diagonal `H[j+1,j] = nrm2(w)` (`L3/nrm2`
§"Iteration-rotation marker" points 1-2) — but those iteration views belong to the surrounding
`krylov-step` body / outer convergence-test consumer, not to the `nrm2` leaf itself, which has
no iteration view of its own. The defining identity `nrm2(x) = √dot(x, x)` (L1 law 8, inherited
unchanged at L3) is the structural link to the inner-product surface.

## L2 form (RHS)

The L2 form is the fusion-rotation composition (`L2/nrm2` §Signature / §Semantics), the same
reduction written as `√ ∘ abs ∘ inner_product` at the diagonal `y = x`:

    nrm2 :: Tensor[N] -> Scalar
    nrm2 x = √ (abs (inner_product x x))        -- √ ∘ abs ∘ inner_product at y = x; consumer, NOT a fold member

The L2 form's inner reduction is the firm `inner_product` fold (cycle-019) over the length
axis; `nrm2` post-composes the scalar `abs` and `√` onto the fold output at `y = x` as a
**consumer**, NOT a fold member (do-NOT-merge per [`L2/inner_product`](../L2/inner_product.md)
§"Consumer (NOT an instance)"). The `std::abs` defensive guard is **preserved at L2 as an explicit
load-bearing numerical claim** (the fusion-rotation discipline keeps load-bearing numerical
tricks as algebraic claims); the signature is identical to the L3 form. The only textual
difference from the L3 form is the **inner-reduction name**: L3 writes the defining identity
through `dot(x, x)` (the L3 same-layer leaf, `L3/nrm2` §Dependencies), while L2 writes it
through the `inner_product` fold at the diagonal — these denote the same self-inner-product
value (`dot(x, x) = inner_product(x, x)` at `y = x`; the inner-product fold's diagonal
degeneration, [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
§"The diagonal degeneration (`y = x`)").

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf** — the L3 whole-tensor norm and the L2 fusion
composition are value-thread-isomorphic, with **no wrapper rotation** (the leaf case, simpler
than `krylov-step`):

    nrm2 x  =  √dot(x, x)                        -- L3 whole-tensor reduction (LHS)
            =  √ (abs (inner_product x x))       -- L2 fusion composition (RHS)

The mapping is total and trivial:

| L3 element | L2 element | Mapping |
|---|---|---|
| `nrm2 :: Tensor[N] -> Scalar` | `nrm2 :: Tensor[N] -> Scalar` | Identity. Same signature; no element loop exposed at either layer (`nrm2` is L3-native / L2-native by signature shape per [`krylov-step-body-identity`](./krylov-step-body-identity.md) point 3). |
| `√dot(x, x)` (defining identity through the L3 `dot` leaf) | `√ (abs (inner_product x x))` (defining identity through the L2 `inner_product` fold at `y = x`) | Identity on value. The inner self-inner-product is the same value (`dot(x, x) = inner_product(x, x)` at the diagonal); the L2 form names it as the `inner_product` fold (the L2 inner-product surface) where L3 names it as the `dot` same-layer leaf. The outer `√` is shared; the `abs` is implicit in the L3 form (subsumed by the non-negativity claim) and **preserved-as-explicit** at L2 (load-bearing numerical claim). |
| consumed-inside roles: `outputs.residual_norm`, Arnoldi `H[j+1,j] = nrm2(w)` | consumed by [`krylov-step`](../L2/krylov-step.md) (residual-norm readout + Arnoldi sub-diagonal) | Identity. The surrounding consumer is the same `krylov-step` body at both layers; the consumer's iteration view is wrapper content, not `nrm2` content. **No wrapper rotation on the `nrm2` leaf itself.** |

There is **no surface adjustment** of the kind `krylov-step-body-identity` carries (no
`(op, K, s)` → `IterState` consolidation, no outer-loop collapse) because `nrm2` is a leaf
reduction with no surrounding wrapper of its own — the iteration view is entirely the
*consuming* context's, and that context's rotation is `krylov-step`'s, not `nrm2`'s. The only
textual difference between the L3 and L2 forms is the inner-reduction name (`dot` leaf at L3 vs
`inner_product` fold at L2), which denotes the same diagonal self-inner-product value. This is
the **identity-in-form** property: every L3 element maps to an L2 element at the same position
with the same value, and the leaf carries no wrapper to rotate.

## Applicability conditions

The rewrite is valid when (all hold for the firm L3 form by construction):

1. **`nrm2` is L3-native / L2-native by signature shape.** The signature `Tensor[N] -> Scalar`
   exposes no per-element loop at either layer; the reduction over the length axis is a single
   semantic step at both L3 and L2. This is the condition
   [`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Applicability conditions"
   point 3 (`:97`) names for the whole seven-primitive cohort including `nrm2`; it is what makes
   the rotation identity-in-form rather than requiring a decomposition. Currently satisfied.

2. **The inner self-inner-product denotes the same value at both layers.** The L3 form's
   `dot(x, x)` and the L2 form's `inner_product(x, x)` at the diagonal `y = x` are the same
   Hermitian self-inner-product `Σ_i |x[i]|²` (real, non-negative — L1 dot laws 4 / 9). The L2
   inner-product surface is the *fold* (firm cycle-019); the L3 surface is the *leaf* `dot`
   (firm). Both denote the diagonal degeneration of the same reduction; the L2>L1 sibling theme
   [`nrm2-fold-specialization`](../L2-L1/nrm2-fold-specialization.md) lowers the L2 form the rest
   of the way to the L1 `dot(x, x)` leaf. Currently satisfied.

3. **The `√ ∘ abs` post-step is shared (modulo the abs-preserved/abs-absorbed framing).** The
   outer `√` is identical at both layers (principal non-negative real square root, deterministic
   IEEE-754); the `abs` guard is implicit at L3 (subsumed by the non-negativity claim — `L3/nrm2`
   inherits the L1 treatment) and **preserved as an explicit load-bearing claim** at L2. Both
   treatments are consistent (the guard implements the non-negativity invariant under floating
   point); the framing difference does not change the value. Currently satisfied.

4. **No surrounding wrapper to rotate.** `nrm2` is a leaf reduction; unlike `krylov-step` it has
   no `(op, K, s)` tuple, no outer tail-recursive loop, no `IterState` record. The iteration view
   belongs entirely to the consuming `krylov-step` body / outer convergence-test, whose rotation
   is captured by [`krylov-step-body-identity`](./krylov-step-body-identity.md) /
   [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md), not by this theme. The leaf identity
   is total. Currently satisfied.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: each L1/L2/L3 form of `nrm2` has the signature shape
`Tensor[N] -> Scalar` — a whole-tensor reduction with no element loop exposed at L2 or L3. The
L3 vocabulary at this scope demands whole-tensor operations with no element loop; `nrm2`
satisfies this requirement *at L2*, so the rotation is the identity. This is a structural
argument about the `nrm2` signature shape — the same structural argument
[`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Justification kind" gives as its
secondary justification for the whole cohort, applied here to the single leaf.

**Empirical-match (secondary)**: the cycle-002 combinator-miner claim — that L2's primitive
vocabulary (including `nrm2`) is already L3-native by inspection of the slice corpus's L2 and L3
prose — is the original empirical evidence, re-confirmed by the cycle-006 audit and ratified at
[`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Verified-against" bullet 1 (the
terminal firm home of the cycle-002 Claim 2). The L2>L3 lift of `nrm2` is the identity rotation;
therefore the L3>L2 lowering — running the same edge in the opposite direction — is also the
identity rotation. For the *leaf* `nrm2` the empirical-match is even cleaner than for the
composite body: there is no wrapper whose rotation the empirical observation must exclude, so the
observation is total.

**Abstraction-direction note**: L3 is the higher-abstraction layer for this edge (it has the
iteration rotation already done by the L4>L3 hop and speaks about whole-tensor field operations);
L2 is the lower-abstraction layer (it speaks about the primitive composition — here the
`√ ∘ abs ∘ inner_product` fusion form). The rotation direction is L3 → L2: the L3 whole-tensor
norm lowers to the L2 fusion composition by re-naming the inner reduction from the `dot` leaf to
the `inner_product` fold at the diagonal and surfacing the `abs` guard as an explicit
load-bearing claim. There is no wrapper rotation (the leaf has no wrapper); the rotation is the
identity on the leaf. This matches the methodology's lowering direction.

## Speculative L2 operators

**None.** This theme is the identity rotation; no new L2 vocabulary is introduced. The L3 form
referenced in the LHS is the firm [`L3/nrm2`](../L3/nrm2.md) (cycle-011); the L2 form referenced
in the RHS is the firm [`L2/nrm2`](../L2/nrm2.md) (cycle-041, wave-1 D2). Both endpoints exist in
the artifact; the theme ratifies their identity-in-form relationship. The B-weighted overload
(the operator-weighted energy norm, [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
rough-in at L1) is a separate operator consuming the M-weighted member of `inner_product`, not a
variant of this `nrm2`; named here only to mark the boundary.

## Verified-against

L3 / L2 anchors:

- [`book/src/L3/nrm2.md`](../L3/nrm2.md) (firm cycle-011) — the L3 LHS: whole-tensor reduction
  `√dot(x, x)`, the no-sequential-obstruction iteration-rotation marker, the two consumed-inside
  roles (residual-norm readout + Arnoldi sub-diagonal), the always-real element-type collapse,
  the L1-inherited algebraic laws.
- [`book/src/L2/nrm2.md`](../L2/nrm2.md) (firm cycle-041, wave-1 D2) — the L2 RHS: the
  fusion-rotation form `√ ∘ abs ∘ inner_product` at `y = x`, the consumer-not-fold-member
  boundary, the preserved `std::abs` load-bearing claim.
- [`book/src/L3-L2/krylov-step-body-identity.md`](./krylov-step-body-identity.md)
  §"Applicability conditions" point 3 (`:97`) — the load-bearing statement that the seven L1
  primitives (including `nrm2`) are L3-native / L2-native by signature shape (no per-element
  loop visible). The structural justification this theme applies to the single leaf.
- [`book/src/L2-L1/inner-product-fold-specialization.md`](../L2-L1/inner-product-fold-specialization.md)
  §"The diagonal degeneration (`y = x`)" — the inner-product fold's diagonal degeneration, where
  `dot(x, x) = inner_product(x, x)`; the basis for the inner-reduction-name equivalence in
  §"The rewrite" condition 2.
- [`book/src/L2-L1/nrm2-fold-specialization.md`](../L2-L1/nrm2-fold-specialization.md) (this
  cycle, sibling D5 theme) — the adjacent L2>L1 hop that lowers the L2 `nrm2` form the rest of
  the way to the L1 `nrm2` leaf; together the two D5 themes complete the `nrm2` adjacent-edge
  chain below the firm L3 anchor.

L0 anchor (transitive through L1; verified on-disk this invocation):

- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is
  `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing line; the one-line
  unfolded composition that makes both the L3>L2 and the L2>L1 rotations identity-in-form. (Path
  relative to `reference/palace/`; full L0 evidence at [`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Status

`firm` — the L3 LHS is firm (cycle-011), the L2 RHS is firm (cycle-041, wave-1 D2), and the
rotation is identity-in-form on the leaf: one L3 whole-tensor norm, one L2 fusion composition,
same signature, same value, same defining identity (`nrm2(x) = √dot(x, x)`, L1 law 8 inherited
unchanged). No decomposition (the reduction is a single semantic step at both layers — `nrm2` is
L3-native / L2-native by signature shape), no wrapper rotation (the leaf has no surrounding
`(op, K, s)` tuple or outer loop — strictly simpler than `krylov-step-body-identity`), no
speculative operator, no constructive sub-part (every claim is positively anchored on
fully-specified source). The only textual difference between the L3 and L2 forms is the
inner-reduction name (`dot` leaf at L3 vs `inner_product` fold at L2 at the diagonal), which
denotes the same value. This is the BLAS-1-leaf analogue of
[`krylov-step-body-identity`](./krylov-step-body-identity.md), under the 2026-05-31
`l2-floor-under-l3-blas1-cohort` foundation-first directive: it completes the adjacent edge
below the firm L3 [`nrm2`](../L3/nrm2.md) anchor. A `lowering-verifier` audit attaching a
`verified_against:` block confirming the identity-in-form rotation is the standard follow-up,
not a status reduction.

## L3>L2 vs L2>L1 distinction (the two D5 nrm2 themes)

The two `nrm2` themes landed this cycle (D5) divide the adjacent-edge chain below the firm L3
anchor cleanly, both identity-in-form:

- **L3>L2 (this theme; `nrm2-body-identity`)**: the L3 whole-tensor norm dissolves into the L2
  fusion composition. Identity on the leaf; the only textual change is the inner-reduction name
  (`dot` leaf → `inner_product` fold at the diagonal) and the surfacing of the `abs` guard as an
  explicit L2 claim. No wrapper rotation.
- **L2>L1 (`nrm2-fold-specialization`)**: the L2 fusion composition re-fuses onto the single L1
  `nrm2` leaf. Identity on the primitive's signature; the only change is the resolution drop of
  the `√`/`abs` scalar post-steps (named L2 fusion steps → below-L1-resolution IEEE-754
  primitives) and the absorption of the preserved `abs` guard into the L1 non-negativity claim.

Together they constitute the full L3>L1 lowering chain for `nrm2`, identity-in-form at every hop
(both are no-ops on the buffer side — there is no destination buffer; the result is a returned
scalar). The L1>L0 expansion into the four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt`
chain is the separate firm [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) theme,
where the `abs` guard re-materializes as stage 3 and the MPI collective re-appears.
```

```edit:book/src/L2-L1/index.md
| [nrm2-fold-specialization](./nrm2-fold-specialization.md) | `L2/nrm2` (firm cycle-041) | `L1/nrm2` (firm cycle-003; single leaf — no L1 family to dispatch) | firm *(structural; thin-identity — BLAS-1-leaf consumer sibling of `inner-product-fold-specialization`; `nrm2` = `√ ∘ abs ∘ inner_product` CONSUMER at `y=x`, NOT a fold member; no dispatch / no decomposition / no destination buffer; `√`/`abs` scalar post-steps drop below L1 resolution + `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1)* |
```

```edit:book/src/L3-L2/index.md
| [`nrm2-body-identity`](./nrm2-body-identity.md) | L3 [`nrm2`](../L3/nrm2.md) §Signature — whole-tensor Euclidean-norm reduction `nrm2 x = √dot(x, x)`, signature `Tensor[N] -> Scalar` with no element loop; consumed-inside roles (residual-norm readout + Arnoldi sub-diagonal) belong to the surrounding `krylov-step` body, not the leaf. | L2 [`nrm2`](../L2/nrm2.md) §Signature — fusion-rotation form `nrm2 x = √ (abs (inner_product x x))` at `y=x`; `√ ∘ abs ∘ inner_product` CONSUMER of the fold (NOT a fold member), `std::abs` guard preserved as explicit load-bearing claim. | `structural` (each form is `Tensor[N] -> Scalar` — whole-tensor by construction, no per-element loop; `nrm2` L3-native/L2-native by signature shape per [`krylov-step-body-identity`](./krylov-step-body-identity.md) point 3) + secondary `empirical-match` (cycle-002 combinator-miner claim re cycle-006 audit) | `firm` (cycle-041 wave-2 abstractor D5; BLAS-1-leaf analogue of `krylov-step-body-identity` — leaf case, NO wrapper rotation; completes the adjacent edge below the firm L3 anchor under the `l2-floor-under-l3-blas1-cohort` directive) |
```

```edit:book/src/SUMMARY.md
- [nrm2-body-identity](./L3-L2/nrm2-body-identity.md)
```

```edit:book/src/SUMMARY.md
- [nrm2-fold-specialization](./L2-L1/nrm2-fold-specialization.md)
```

## Speculative operators proposed

**None** (both themes). Both are identity-in-form lowering edges between *existing* firm
vocabulary:

- L2>L1 (`nrm2-fold-specialization`): LHS `L2/nrm2` (firm cycle-041, wave-1 D2) → RHS `L1/nrm2`
  (firm cycle-003, single leaf). No new L1 operator; no dispatch family (there is exactly one
  L1 `nrm2`, unlike the inner-product cohort's `dot`/`tdot`/`bilinear-form`).
- L3>L2 (`nrm2-body-identity`): LHS `L3/nrm2` (firm cycle-011) → RHS `L2/nrm2` (firm cycle-041,
  wave-1 D2). No new L2 operator; the leaf carries no wrapper to introduce vocabulary for.

The harvester has nothing to promote from these themes — they are pure identity ratifications.

## Supporting evidence

- **`palace/linalg/vector.hpp:255-260`** — verified on-disk this invocation: the `linalg::Norml2`
  template; body line 259 `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing
  line; the one-line unfolded composition that makes BOTH rotations (L3>L2 and L2>L1)
  identity-in-form (no HPC/SIMD trick to unfold at L2, no element loop to lift at L3). Full L0
  evidence list lives at `book/src/L1/nrm2.md` §Evidence (not duplicated in the themes).
- **`book/src/L3-L2/krylov-step-body-identity.md:97`** — verified this invocation: §"Applicability
  conditions" point 3 names `apply_linop, axpy, axpby, axpbypcz, dot, nrm2, scal` as the seven L1
  primitives that are L3-native / L2-native by signature shape (no per-element loop visible). The
  structural justification both themes rest on; the L3>L2 theme is the single-leaf analogue of
  this composite-body theme.
- **`book/src/L2-L1/inner-product-fold-specialization.md` §"The diagonal degeneration (`y = x`)"**
  — names `nrm2` as the consumer entry point (`√ ∘ inner_product` at `y = x`, "composing an outer
  `√` post-step — that composition is downstream of this lowering, not a dispatch within it"). The
  L2>L1 `nrm2` theme IS that downstream `√ ∘ abs` composition; the consumer-not-fold-member
  framing is carried verbatim.
- **`reports/2026-06-01T051607Z-cycle-041-harvester-L2-nrm2/CYCLE.md`** (wave-1 D2; the L2 source
  of truth) — the proposed `book/src/L2/nrm2.md` floor body these themes lower from/to; the
  consumer-not-fold-member framing, the preserved `std::abs` load-bearing claim, and the
  always-real element-type collapse all originate there and are carried through both themes.
- **`book/src/L1/nrm2.md` (firm cycle-003) + `book/src/L1-L0/nrm2-mutation-rotation.md` (firm)** —
  the L1 leaf (defining identity law 8) and the `std::abs` defensive-guard classification
  (load-bearing-defensive; property bought = non-negativity invariant for the square root). The
  L2>L1 theme cites these for the abs-absorbed-at-L1 framing and the load-bearing residue at the
  L1>L0 edge.

## Open questions / caveats

- **The nrm2 floor's existence rides the `l2-floor-under-l3-blas1-cohort` design decision (live
  meta-phase friction — captured per dispatch instruction, NOT resolved here).** The wave-1 D2
  harvester (the L2 source of truth for both themes) framed `nrm2` as a consumer-of-fold AND
  separately argued **no `L2/dot` leaf is needed** (the L2 inner-product surface is the
  `inner_product` *fold*, not a `dot` leaf). The leaf-vs-fold fork is under meta-phase
  adjudication. **Both `nrm2` themes are unaffected by the `dot` question** — `nrm2` consumes
  `inner_product` (the fold) either way, the L3>L2 theme's inner-reduction-name equivalence holds
  at the diagonal regardless (`dot(x,x) = inner_product(x,x)`), and there is exactly one L1 `nrm2`
  leaf to lower onto — but the existence of the L2 `nrm2` *floor* (the LHS of the L2>L1 theme /
  the RHS of the L3>L2 theme) rides the same `l2-floor-under-l3-blas1-cohort` decision. If the
  meta-phase rules that BLAS-1 leaves should NOT get L2 floors, both themes would re-home (the
  L2>L1 theme dissolves; the L3>L2 theme becomes a non-adjacent in-line identity note at
  `L3/nrm2` per the in-line-annotation convention). Flagged for the meta-phase; no action in this
  dispatch.

- **`-fold-specialization` slug vs consumer framing (L2>L1 theme; recorded for the integrator /
  lowering-verifier).** The L2>L1 slug `nrm2-fold-specialization` is carried for sibling-naming
  continuity with the BLAS-1 reduce-to-scalar cohort (`inner-product-fold-specialization`,
  `linear-combination-fold-specialization`), per the dispatch instruction to mirror the
  `-fold-specialization` precedents. But `nrm2` is a CONSUMER of the `inner_product` fold, NOT a
  fold member, and there is no L1 family to "specialize" into (single leaf). The body makes this
  explicit (intro + §"The rewrite" point 1). The L3>L2 sibling uses the symmetric
  `-body-identity` slug (mirroring `krylov-step-body-identity`). If a future audit prefers a
  consumer-naming slug for the L2>L1 theme (e.g. `nrm2-norm-consumer-identity`), that is a rename
  follow-up — the body content is slug-agnostic. Defer.

- **COUNT-OWNERSHIP honored.** I appended ONLY my two theme rows (one to `L2-L1/index.md` theme
  list, one to `L3-L2/index.md` theme list), my two SUMMARY.md chapter registrations, and my two
  theme bodies. I did NOT touch the consolidated theme-count tallies / Vocabulary-cohort prose /
  Working-Notes cohort-growth logs in either index (D7 owns the consolidated counts this cycle).
  The `L2-L1/index.md` §"Vocabulary cohort" and §"Working Notes" cohort-growth log, and the
  `L3-L2/index.md` §"Working Notes", are left for D7 / a future layer-intro-author pass — in
  particular, naming the BLAS-1-leaf thin-identity *floor* themes as a distinct cohort category
  (a third category alongside named-compositions and fold-cohorts) is layer-intro-author scope.

- **Lifting notes (reverse direction, working notes only — NOT in the high→low chapter bodies).**
  Both themes' formal chapters narrate only the forward (high→low) rotation. The reverse-direction
  lifting note for the L2>L1 theme is in that theme's §"Open questions / caveats" (the L1 leaf
  lifts to the L2 floor with the `√ ∘ abs` post-step re-named as preserved fusion structure; the
  lift is value-faithful but not bit-faithful — re-lowering needs the inner-product summation-order
  table). The L3>L2 lift is symmetric and trivial: the L2 fusion form lifts to the L3 whole-tensor
  norm by re-naming the `inner_product` fold as the `dot` same-layer leaf and the surrounding
  consumer's iteration view; no additional structure required (the leaf has no wrapper). Both lifts
  are determinate and lossless except for the pinned reduction tree (inherited from the
  `inner_product`/`dot` leaf, order-agnostic at L2/L3).

- **`verified_against:` blocks deferred to a `lowering-verifier` cycle.** Per the sibling-theme
  convention (`inner-product-fold-specialization` carries a `lowering-verifier`-authored
  `verified_against:` YAML block), both `nrm2` themes leave the trailing `verified_against:` block
  for a future `lowering-verifier` dispatch — its authorship, not the abstractor's. The themes are
  `firm` on positively-anchored fully-specified source; the audit block is corroboration, not a
  promotion gate.
