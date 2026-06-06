---
layer: L2
operator: nrm2
rank: firm
edges:
  depends-on:
    - L2/inner_product
  reference:
    - L1/nrm2
    - L3/nrm2
variant_axes:
  - element-type (real / complex; collapsed to single operator at L2 — result is always real)
---

# nrm2

> **Consumer-stub (reduced cycle-052 D3, vocabulary-shift-redirect refactor pass).**
> `nrm2` at L2 is a **CONSUMER** of the fold combinator [`inner_product`](./inner_product.md)
> (firm cycle-050) — `nrm2(x) = √ (abs (inner_product(x, x)))`, the `√ ∘ abs ∘ inner_product`
> composition at `y = x`. It is **NOT a fold member** (the do-NOT-merge carve-out): it
> post-composes two scalar maps onto the fold's output, it does not itself fold. Merging it into
> `inner_product` would be a category error. Semantics, algebraic laws, and the consumer-identity
> downward note are deferred to the combinator and the kept in-line §"Downward to L1" below; this
> stub retains only the leaf-level facts the combinator does not carry — the load-bearing
> `std::abs` defensive-guard claim and the `vector.hpp:255-260` `Norml2` L0 anchor.

Euclidean-norm reduction at L2 (the fusion-rotation layer): `α = ‖x‖₂ = √⟨x, x⟩`, written as the
algebraic composition `√ ∘ abs ∘ inner_product` over the shape group `S`. Palace's `linalg::Norml2`
is already the one-line unfolded form (`std::sqrt(std::abs(Dot(comm, x, x)))`,
`palace/linalg/vector.hpp:259`), so the L2 fusion rotation has no fused kernel to unfold; the
entry exists primarily as a **layer-coherence floor** — present so the firm L3
[`nrm2`](../L3/nrm2.md) rests on an adjacent L2 parent.

## Consumer of `inner_product`, NOT a fold member (the do-NOT-merge carve-out)

    nrm2(x) = √ (abs (inner_product(x, x)))        -- √ ∘ abs ∘ inner_product at y = x

`nrm2` post-composes the scalar square-root (and the defensive `abs`) onto the
[`inner_product`](./inner_product.md) fold at the diagonal `y = x`; **it does not itself fold and
is NOT a member of the fold cohort**. Merging `nrm2` into `inner_product` would be a category
error — `inner_product` is the shape-group `S` homomorphism producing `dot(x, x)`; `nrm2` is the
scalar map `α ↦ √|α|` applied to that fold's output. The do-NOT-merge boundary is carried in the
[`inner_product`](./inner_product.md) §"Consumer (NOT an instance)" and in [`L2/index`](./index.md)
§"Fold-cohort boundary"; this entry lists `inner_product` under `consumes`, never as a fold it
instantiates. Semantics and the full algebraic-law listing are deferred to the combinator (which
carries the reduce-to-scalar fold) and the firm L1 leaf [`L1/nrm2`](../L1/nrm2.md) (firm cycle-003,
authoritative on every Palace-surface claim); the consumer-specific downward note is kept in-line
at §"Downward to L1" below.

The B-weighted overload `linalg::Norml2(comm, x, B, Bx) = √(xᴴ B x)` is **not** part of this
operator (per `book/src/L1/nrm2.md:13`) — it is the operator-weighted energy norm, a separate L2
candidate consuming the M-weighted member of `inner_product`, tracked as rough-in
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1.

## The `std::abs` defensive guard (the load-bearing leaf-level fact — RETAINED)

**The `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim** (L2
discipline: load-bearing numerical tricks survive the fusion rotation as explicit algebraic
claims, per [`L2/index`](./index.md) §Semantics). It is a no-op in exact arithmetic (the
self-inner-product `inner_product(x, x)` is non-negative real, so `abs` of it equals it) but
**load-bearing in floating point**, where it strips a sign that round-off in the reduction could
have flipped negative on a numerically-zero vector, buying **domain-safety for `√` (no NaN)**. It
is **NOT erasable in floating point** without introducing that NaN failure mode. The full
classification (load-bearing-defensive; property bought = non-negativity invariant for the square
root) lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The
`std::abs` defensive guard — classification", where the guard re-materializes as stage 3 of the
four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain.

## Signature

    nrm2 :: Tensor[(S: ...)] -> Scalar
    nrm2(x) = √⟨x, x⟩ = √ (abs (inner_product(x, x)))

Result is **always real-valued** and non-negative (`nrm2(x) ≥ 0`), regardless of `x`'s element
type — the element-type axis collapses to a single operator (the post-composed `abs` projects the
complex self-inner-product onto its real magnitude before `√`). The operand is one shape group
`S` of arbitrary unknown rank (see [`l4_calculus`](../semantics/index.md) §1.2.1). Full shape contract +
algebraic-law listing: the combinator [`inner_product`](./inner_product.md) + the firm L1 leaf
[`L1/nrm2`](../L1/nrm2.md).

## Status

`firm` — consumer-stub. `nrm2` at L2 is a CONSUMER of the firm L2 [`inner_product`](./inner_product.md)
combinator (`√ ∘ abs ∘ inner_product` at `y = x`), **not a fold member** (the do-NOT-merge
carve-out). Semantics and algebraic laws are inherited from the combinator / the firm L1 leaf
[`L1/nrm2`](../L1/nrm2.md) unchanged; this chapter retains only the load-bearing `std::abs`
defensive-guard claim and the consumer-identity downward note. The L2 fusion rotation is a no-op
for this leaf (`linalg::Norml2` is already the one-line unfolded composition). The entry exists as
a **layer-coherence floor** per CLAUDE.md §Methodology invariants **Identity-lowerings still
require both L levels** (cycle-009 codification) under the 2026-05-31 foundation-first directive
`l2-floor-under-l3-leaf-cohort`: it gives the firm L3 [`nrm2`](../L3/nrm2.md) (cycle-011) a present
adjacent L2 parent. Harvested cycle-041 wave-1 (D2); reduced to a consumer-stub cycle-052 D3
(vocabulary-shift-redirect refactor pass).

## Downward to L1 (consumer identity-in-form; no theme file)

L2 `nrm2` re-fuses downward onto the single L1 leaf [`nrm2`](../L1/nrm2.md) (firm cycle-003) as
**identity-in-form on the primitive's signature** — value-thread-isomorphic, with **no dispatch**
(one L1 leaf), **no decomposition** (the L2 fusion rotation is a no-op — `linalg::Norml2` is
already the one-line unfolded composition), and **no destination-buffer concern** (the result is a
returned scalar). The hop does two value-preserving surface adjustments:

1. **The `inner_product` fold at `y = x` re-fuses to the `dot` leaf at the diagonal.** L2 names the
   inner reduction as the shape-group `S` `inner_product` fold (firm cycle-019); at L1 the same
   diagonal self-inner-product is the `dot(x, x)` leaf (the defining identity `nrm2(x) = √dot(x, x)`,
   L1 algebraic law 8, `book/src/L1/nrm2.md:53`). This is the **consumer's** view of the edge
   [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The
   diagonal degeneration (`y = x`)" lowers for the fold itself — that theme names `nrm2` precisely
   as the consumer entry point (`√ ∘ inner_product` at `y = x`, the outer `√` a post-step
   "downstream of this lowering, not a dispatch within it"). The inner `inner_product(x, x) →
   dot(x, x)` re-fusion is inherited from the inner-product theme; the `nrm2`-specific content is
   the outer `√ ∘ abs` post-step. **`nrm2` is a CONSUMER of `inner_product`, not a fold member**
   (do-NOT-merge per [`L2/inner_product`](./inner_product.md) §"Consumer (NOT an instance)").
2. **The two scalar post-steps change framing, not value.** At L2 the `abs` guard is **preserved as
   an explicit load-bearing numerical claim** and the `√` is the principal non-negative real square
   root composed onto the fold output. At L1 both drop **below the layer's resolution**: the `abs`
   guard **disappears**, subsumed by the L1 algebraic claim that `dot(x, x)` is non-negative real,
   and the `√` is a deterministic IEEE-754 scalar primitive on the leaf's output. Both treatments
   are consistent — the guard *implements* the non-negativity claim under floating point; full
   classification at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The
   `std::abs` defensive guard — classification".

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`):
`palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is
`return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the
L2>L1 fusion rotation a no-op. (Path relative to `reference/palace/`; full L0 evidence at
[`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Lifts from

L2 `nrm2` lifts from / to L3 [`nrm2`](../L3/nrm2.md) (firm cycle-011) as **identity-in-form**; the
L3>L2 rotation on the primitive is identity-in-form (in-line at the L3 entry's §"Downward to L2").
`nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010
audit verdict); at L4 it appears inside larger composed entries (e.g.
`book/src/L4/krylov-step.md` §Semantics, `outputs.residual_norm`) as a let-binding.

## Evidence

`nrm2`'s deferred-to homes + retained leaf-level anchors. All semantics/laws evidence is the
combinator's / the firm L1 leaf's:

- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — authoritative on Palace surface,
  signature, algebraic laws, variant axes, the defining identity `nrm2(x) = √dot(x, x)`, the
  B-weighted-overload boundary, and the complete L0 evidence list.
- [`book/src/L1-L0/nrm2-mutation-rotation.md`](../L1-L0/nrm2-mutation-rotation.md) (firm) — the
  four-stage L0 chain `Dot → MPI_Allreduce → std::abs → std::sqrt` and the full `std::abs`
  defensive-guard classification (RETAINED leaf-level fact; the L2 stub preserves the guard as an
  explicit algebraic claim and cites this theme for the classification).
- [`book/src/L2/inner_product.md`](./inner_product.md) (firm cycle-050) — the fold `nrm2`
  CONSUMES (`√ ∘ abs ∘ inner_product` at `y=x`); §"Consumer (NOT an instance)" carries the
  do-NOT-merge boundary.
- [`book/src/L2/index.md`](./index.md) §"Fold-cohort boundary" — the consumer-not-member framing
  and the L2-vocabulary home.
- [`book/src/L3/nrm2.md`](../L3/nrm2.md) (firm cycle-011) — the L3 consumer this floor sits under.
- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template definition: full body (line 259)
  is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing line — the RETAINED L0
  anchor for the `std::abs` guard. (Path relative to `reference/palace/`; **self-verified via
  `citecheck --anchor Norml2`, anchor at :257 within :255-260** this dispatch.)
- [`book/src/concepts/nrm2.md`](../concepts/nrm2.md) — the cross-cutting concept page; BLAS-1
  heritage framing. (Note: its scaled-summation stability claim is incorrect per the L1
  correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)
