---
layer: L4
operator: nrm2
firmness: firm
edges:
  depends-on:
    - L4/inner_product
    - L3/inner_product           # L3/nrm2 leaf eliminated into the combinator (cycle-127, RE-style); this verb is the √∘abs∘inner_product CONSUMER at the diagonal (NOT a fold member — see L3/inner_product §Consumer)
  reference:
    - concepts/black-box-vs-accelerated-kernels
    - concepts/nrm2
variant_axes:
  - element-type (real / complex; collapsed to a single operator — result is always real-valued and non-negative)
---

# nrm2

The L4 **Euclidean-norm verb**: `α = ‖x‖₂ = √⟨x, x⟩`, the named unit a Krylov / eigen
solver description wants written as residual `nrm2(r)` rather than an inlined
`√(inner_product r r)`. `nrm2` is one of the **kept named abstractions** that **rises
to L4 as a named verb** per the
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§2 "Kept named abstraction — rises": it decomposes into a simple combinator
application (`√ ∘ abs ∘ inner_product` at the diagonal `y = x`), **but** its named
definition is literature-standard and aids downstream algorithm clarity and
literature tie-back — it is **not removed** just because its kernel is replaceable.

**`nrm2` is a CONSUMER of [`inner_product`](./inner_product.md), NOT a fold member**
(the do-NOT-merge over-unification guard, carried identically at L2/L3/L4). It
post-composes two scalar maps — the defensive `abs`, then `√` — onto the combinator's
**scalar output**; it does not itself fold over the shape group `S`. Merging `nrm2` into
[`inner_product`](./inner_product.md) would be a category error (a shape-group `S`
homomorphism producing `⟨x, x⟩` vs. the scalar map `α ↦ √|α|` on that output). It
rises as a **consumer verb** alongside the combinator (the permitted dual), not as one
of its members.

The L4 form re-expresses **through** the firm L4 combinator
[`inner_product`](./inner_product.md) at the diagonal (NOT a re-derived fold) and is
value-thread-isomorphic to the firm L3 named abstraction [`L3/nrm2`](../L3/inner_product.md#consumer-nrm2-and-matrix-weighted-norm).

## Context

L4 is **vocabulary, not architecture** (`L4/index.md:7-13`) and the
**backend-lowering target** (project memory `project_l4_is_backend_lowering_target`):
the feature surface whose semantics match the external GPU-tensor backend. `nrm2` is
the named verb every Krylov / eigen solver description reuses at the feature surface in
two distinct roles: the **residual-norm convergence readout** (`outputs.residual_norm =
nrm2(r)` in the recompute-from-residual variants) and the **Arnoldi sub-diagonal
coefficient** (`H[j+1, j] = nrm2(w)` after orthogonalization). The L4 surface names it
as a verb even though it decomposes, because the named form is what makes a convergence
test or an Arnoldi step readable and tied to the literature.

`nrm2` carries **no first-class L4 calculus structure of its own** (no `Solve` monad,
no iteration carry, no convergence predicate) — it is a pure value-producing scalar map
on a pure value-producing reduction. It rises as a **feature-surface verb the backend
wants**, not because it carries iteration structure.

## Semantics (overlay)

The L4 calculus is specified in the strawman
[`../semantics/index.md`](../semantics/index.md). `nrm2` adds **no reduction-rule
extension** — it is the [`inner_product`](./inner_product.md) reduction at the diagonal
`y = x` post-composed with the `√ ∘ abs` scalar map. Pseudo-language is Haskell `::`
signatures inside a `text` fence per the L4/L3 notation invariant.

## Signature

    -- the Euclidean-norm verb: √ ∘ abs ∘ inner_product at the diagonal y = x
    nrm2 :: Tensor[(S: ...)] -> Scalar

    nrm2 x = sqrt (abs (inner_product x x))   -- √ ∘ abs ∘ inner_product at y = x

Shape contract (bunsen-style; named shape groups per
[`l4_calculus`](../semantics/index.md) §1.2.1; identical to the firm L3 / L1
signature — the L4 verb is value-thread-isomorphic to both):

- `x` — `Tensor[(S: ...)]` — read-only; the single operand (shape group `S` of
  arbitrary unknown rank).
- result — `Scalar` — **always real-valued and non-negative** (`nrm2 x ≥ 0`),
  regardless of `x`'s element type; `zero` on the empty tensor (`inner_product` seeds
  `zero`, `√ (abs zero) = zero`).

The result is always real even for a complex `x`, because the diagonal
`inner_product x x` is real-and-non-negative by law 5 (PSD at the diagonal) of the
combinator, and `√ ∘ abs` maps it to a non-negative real.

### The `abs` defensive guard (load-bearing scalar-map detail)

The defining identity is `nrm2 x = √ (inner_product x x)`; the `abs` is a **load-bearing
defensive non-negativity guard** against floating-point round-off pushing the reduction
sum slightly negative on a numerically-zero vector (it strips a sign that round-off could
have flipped, buying domain-safety for `√` — no NaN). It is a no-op in exact arithmetic
(law 5 guarantees `inner_product x x ≥ 0`) but load-bearing in floating point. The full
classification lives at the L1>L0
[`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive
guard — classification"; at L4 it is preserved as an explicit part of the scalar map
(the L0 source is the one-line `std::sqrt(std::abs(Dot(comm, x, x)))`).

## Algebraic laws

`nrm2` is a **scalar map on the combinator's diagonal output**, so its laws are the
square-root norm-axioms over the PSD diagonal, NOT the fold's homomorphism laws (the
do-NOT-merge boundary at the law level — `nrm2` does NOT inherit split-additivity,
because `√` is not additive). The laws that hold:

1. **Non-negativity.** `nrm2 x ≥ 0` (real-valued); `= 0` iff `x = 0` (exact arithmetic,
   from combinator law 5 PSD-at-the-diagonal + `√` monotone). The `abs` guard makes the
   non-negativity hold defensively in floating point too.
2. **Empty-tensor identity.** `nrm2` over an empty tensor is `zero` (`√ (abs zero)`).
3. **Absolute homogeneity (the norm-scaling law).** `nrm2 (scal α x) = |α| · nrm2 x`
   for a scalar `α` — follows from combinator multilinearity at the diagonal
   (`inner_product (αx) (αx) = |α|² ⟨x, x⟩`) and `√`.
4. **Triangle inequality.** `nrm2 (x + y) ≤ nrm2 x + nrm2 y` (the norm axiom; the
   `inner_product` Cauchy–Schwarz fact under the square-root).
5. **Defining-identity / diagonal-consume.** `nrm2 x = √ (abs (inner_product x x))` —
   the `√ ∘ abs ∘ inner_product` composition at `y = x`; this is the law that ties the
   consumer verb to the rising combinator.

Laws that explicitly **do not** hold (deferred / category-distinct, NOT restated):

- **Split-additivity / shape-concatenation-homomorphism does NOT hold for `nrm2`.**
  `nrm2 (x₁ ++ x₂) ≠ nrm2 x₁ + nrm2 x₂` in general (it is `√(nrm2 x₁² + nrm2 x₂²)`) —
  `√` is not additive. This is exactly **why `nrm2` is a consumer, not a fold member**:
  the homomorphism is a property of [`inner_product`](./inner_product.md)'s reduction,
  lost under the post-composed `√`.
- **Reduction-tree associativity under IEEE-754** — the inner `inner_product x x`
  carries the same load-bearing non-law as the combinator (pinned reduction tree for
  bit-reproduction; deferred to the L2>L1 fold-specialization theme). The outer `abs`/`√`
  scalar map is order-independent.

## Variant axes

1. **Element-type** — `real | complex`, **collapsed to a single operator** at L4 (as at
   L3): the result is always real-valued and non-negative regardless of `x`'s element
   type (the diagonal `inner_product x x` is real by combinator law 5). No conjugation
   variant axis surfaces at the `nrm2` verb level (it is absorbed into the diagonal
   consume — `inner_product x x` is Hermitian-self).

The **B-weighted overload** `linalg::Norml2(comm, x, B, Bx) = √(inner_product_M x B x)`
for SPD `B` is **NOT part of this operator** — it is the `matrix-weighted-norm` consumer
of the combinator's weighted member `inner_product_M` (tracked rough-in at L1
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md), L1-promotion-gated). `nrm2`
pins the weight at `M = I` through the plain `inner_product` (the same pinning that makes
`dot` the plain-weight named specialization).

## Relationship to inner_product (CONSUMER, NOT a fold member — the do-NOT-merge guard)

`nrm2` **consumes** [`inner_product`](./inner_product.md)'s scalar output at the diagonal
and post-composes `√ ∘ abs`; it is **NOT a member of the fold cohort** and does **NOT**
merge into the combinator. This is the **over-unification guard**, carried identically at
L2/L3/L4: the combinator [`inner_product`](./inner_product.md) §"Consumer (NOT an
instance)" lists `nrm2` as a consumer; the L4 frontmatter lists `inner_product` under
`consumes`, never as a fold `nrm2` instantiates. Combinator law 5 (PSD at the diagonal)
is exactly what makes the consumer square-root well-defined. `nrm2` rises as a kept named
abstraction (the **permitted dual** — a consumer verb alongside the general combinator),
distinct from [`dot`](./dot.md), which is a *specialization* of the same combinator (at
`M = I`) rather than a consumer of its output.

## Downward to L3

The L4 `nrm2` verb lowers to the firm L3 [`nrm2`](../L3/inner_product.md#consumer-nrm2-and-matrix-weighted-norm) as **identity-in-form on
the body**: both forms are value-thread-isomorphic — the same `Tensor[(S: ...)] -> Scalar`
signature, the same `√ (abs (inner_product x x))` skeleton (L3 writes the defining
identity through the same-layer `dot(x, x)` leaf; both denote the same Hermitian
self-inner-product value at the diagonal), the same five laws, the same do-NOT-merge
consumer carve-out, the same load-bearing `abs` defensive guard.

**There is no dedicated L4>L3 theme file** — the identity-in-form annotation lives in-line
here, per the cycle-012 non-adjacent-identity / in-line-marker convention (CLAUDE.md
§Methodology invariants "Identity rotations across non-adjacent layers are annotated
in-line"). This is the **same in-line-marker route** the combinator
[`inner_product`](./inner_product.md) and the sibling named verb [`dot`](./dot.md) take to
their L3 forms (and that [`eigsolve`](./eigsolve.md)/[`chebyshev`](./chebyshev.md) take):
there is **no monadic wrapper, no `Solve` monad, no convergence predicate, no outer
driver** to dissolve across the L4>L3 edge — `nrm2` is a pure value-producing scalar map
on a pure reduction at both layers, so the rotation is the identity on the verb body. An
`L4-L3/nrm2-*-dissolution.md` would be a **degenerate identity-in-named-terms theme** (the
§1d smell), so it is correctly an in-line note.

The **substantive** content in the downward chain is (a) the L1>L0
[`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) — the four-stage L0 chain
`linalg::Norml2` → `std::sqrt(std::abs(Dot(comm, x, x)))` and the full `abs`-guard
classification — and (b) the inner reduction's L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
(the pinned reduction tree the `inner_product x x` inherits). The transitive
L4>L3>L2>L1 identity-then-substantive chain composes this in-line L4>L3 identity with the
firm L3>L2 identity (the L3 entry's §"Downward to L2 (consumer identity-in-form)") and the
substantive L1>L0 rotation — annotated in-line per the per-adjacent-edge directory
convention (no `L4-L2`/`L4-L1` directory).

## Status

`firm` — the L4 form is the calculus-level named verb re-expressing the diagonal consume
of the combinator [`inner_product`](./inner_product.md) (firm cycle-068 D3) under the
`√ ∘ abs` scalar map, value-thread-isomorphic to the firm L3 [`nrm2`](../L3/inner_product.md#consumer-nrm2-and-matrix-weighted-norm) (firm
cycle-011, consumer-stub cycle-052 D3): the same `Tensor[(S: ...)] -> Scalar` `√(abs(inner_product
x x))` skeleton, identity-in-form across the L4>L3 edge (no monadic wrapper to dissolve —
§"Downward to L3"). The five algebraic laws are the square-root norm-axioms over the PSD
diagonal (each a syntactic identity or a standard norm fact); the homomorphism non-law is
the **defining reason `nrm2` is a consumer, not a fold member**; the inner reduction-tree
IEEE non-law is deferred to the firm L2>L1 fold-specialization theme (NOT restated as an
L4 law); the `abs` defensive guard is preserved as an explicit part of the scalar map; the
element-type axis is collapsed (result always real). It carries **no first-class L4
calculus structure of its own** (no `Solve` monad, no iteration carry) — it rises as a
**kept named abstraction / feature-surface verb the backend wants** per
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2,
alongside the rising combinator (the permitted dual; as a *consumer* verb, the do-NOT-merge
boundary the over-unification guard). The L0 anchors are **inherited transitively through
the firm L3/L1 leaf** (the firm L1 [`nrm2`](../L1/nrm2.md) carries the complete L0 evidence
list; the `vector.hpp:255-260` `Norml2` one-line composition was re-verified on disk at the
L3 entry this batch), not re-localized this pass. The empirical-match witness is the
`test-vector.cpp:209-211` `Norml2` value test (`norm = √14` for `(1,2,3)`, inherited
transitively); the missing dedicated L4 test does not gate firm because every L4 law is a
syntactic identity / standard norm fact carried up from the firm combinator / leaf below
(the firm-on-positive-structure / syntactic-identity escape, the same bar
[`inner_product`](./inner_product.md) cleared).

## Evidence

Combinator + L3/L1 endpoints (firm; the value-isomorphism this L4 named verb rests on):

- `book/src/L4/inner_product.md` (firm cycle-068 D3) — the L4 combinator this verb
  consumes; §"Consumer (NOT an instance): nrm2 / matrix-weighted-norm" already records
  `nrm2(x) = √ (abs (inner_product x x))` at the diagonal as a consumer, NOT a member, with
  combinator law 5 (PSD) as the well-definedness witness.
- [`L3/inner_product`](../L3/inner_product.md) §"Consumer (NOT an instance)" (the firm L3
  `nrm2` consumer this verb is value-thread-isomorphic to — the standalone `L3/nrm2` leaf,
  firm cycle-011, was eliminated cycle-127 RE-style, its signature + defining identity +
  consuming-context roles + the `std::abs` defensive-guard note folded into the combinator's
  §"Consumer (NOT an instance)"; do-NOT-merge boundary preserved — NOT a fold member). Its L0
  anchor `palace/linalg/vector.hpp:255-260` re-verified on-disk this batch.
- `book/src/L1/nrm2.md` (firm cycle-003) — authoritative on Palace surface, signature,
  algebraic laws, variant axes, the defining identity `nrm2(x) = √dot(x, x)`, the
  B-weighted-overload boundary, and the complete L0 evidence list (inherited transitively):
  `palace/linalg/vector.hpp:255-260`, `palace/linalg/vector.hpp:262-270`,
  `palace/linalg/operator.cpp:600-619`.
- `book/src/L1-L0/nrm2-mutation-rotation.md` (firm) — the four-stage L0 chain and the full
  `std::abs` defensive-guard classification (the substantive downward content home).
- `book/src/L4/dot.md` (this cycle, sibling) — the sibling named verb (`nrm2(x) = √dot(x, x)`
  is the L3-internal defining identity; both rise through the same combinator as the
  permitted dual).

L0 transitive anchors (verified on-disk this dispatch via `citecheck --anchor`, not
re-localized — inherited through the firm leaves above):

- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template (anchor confirmed at
  `:257`); body line `:259` is `return std::sqrt(std::abs(Dot(comm, x, x)));` — the one-line
  `√ ∘ abs ∘ inner_product` composition. (Path relative to `reference/palace/`.)
- `palace/linalg/iterative.cpp:408, 568, 578, 582, 631, 756, 762, 810` — CG and GMRES using
  `linalg::Norml2` for the initial RHS norm, the true residual norm, and the Arnoldi
  sub-diagonal coefficients (the residual `nrm2(r)` / `H[j+1,j] = nrm2(w)` named-verb use),
  inherited transitively. (Paths relative to `reference/palace/`.)
- `test/unit/test-vector.cpp:209-211` — the `Norml2` value test (`norm = √14` for `(1,2,3)`),
  the positive empirical witness, inherited transitively. (Path relative to `reference/palace/`.)

Classification / methodology anchors:

- `book/src/concepts/black-box-vs-accelerated-kernels.md` (cycle-067 D3) — §2 "Kept named
  abstraction — rises" (`:88-109`) names `nrm2` as a confirmed keep, the 2-norm named verb
  (`residual nrm2(r)`) that rises to L4 alongside the rising combinator (the permitted dual).
- `book/src/concepts/nrm2.md` — the BLAS-1 heritage cross-cutting framing. (Note: its
  scaled-summation stability claim is incorrect per the L1 correction-pending note at
  `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)
- `book/src/semantics/index.md` — the strawman; `nrm2` adds no reduction rule (the
  combinator's diagonal consume + a `√ ∘ abs` scalar map).

Provenance: harvester:2026-06-02T205715Z (cycle-069 D2) — the `l4-dot-nrm2-named-verb-rise`
plan-tag enactment; rises the kept named abstraction `nrm2` to L4 as a named *consumer* verb
through the firm `L4/inner_product`, per directive-2 disposition-2 (keep-and-rise) and
`concepts/black-box-vs-accelerated-kernels.md` §2 (the do-NOT-merge over-unification guard
preserved: consumer, not fold member).
