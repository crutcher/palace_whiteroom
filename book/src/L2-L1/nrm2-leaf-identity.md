# nrm2-leaf-identity

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
L1 `nrm2`. The `-leaf-identity` slug names the identity-in-form lowering of the single L2
floor onto the single L1 leaf (the cycle-043 batch-12 normalization from the cycle-041
`-fold-specialization` outlier; neither edge is a fold-dispatch); `nrm2` is explicitly **not a fold member** (do-NOT-merge
per [`L2/inner_product`](../L2/inner_product.md) §"Consumer (NOT an instance)" and the wave-1 D2
`L2/nrm2` floor's "Consumer of `inner_product`, NOT a fold member"); the namesake "fold" here
is the `inner_product` fold `nrm2` *consumes* at `y = x`, not a fold `nrm2` instantiates.

## Slug

`nrm2-leaf-identity`

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
