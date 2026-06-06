---
layer: L3
operator: dot
rank: firm
edges:
  depends-on:
    - L2/inner_product
  reference:
    - L4/dot
variant_axes:
  - element-type (real / complex)
  - conjugation-convention (hermitian / unconjugated `tdot` — complex element-type only)
---

# dot

> **Specialization-stub (reduced cycle-052 D3, vocabulary-shift-redirect refactor pass).**
> `dot` at L3 is the **`M = I` Hermitian/symmetric specialization** of the L3 combinator
> [`inner_product`](./inner_product.md) (firm cycle-050) — the combinator IS the L3 entry for
> the reduce-to-scalar inner-product family; `dot` is a **specialization note** under it (per
> CLAUDE.md §Methodology invariants ⟢ — the combinator is the entry, members are
> specialization notes). This chapter is reduced to the leaf-level facts the combinator does
> not carry: the value-bearing conjugation choice (`dot` Hermitian vs `tdot` unconjugated) and
> the leaf's consumption inside the `krylov-step` body. Semantics, algebraic laws, the
> no-sequential-obstruction verdict, and the downward lowering are **deferred** to the
> combinator [`inner_product`](./inner_product.md) §"Specializations" + §"Downward to L2".

Whole-tensor inner-product reduction at L3: `α = ⟨x, y⟩`, rendered as the Hermitian/symmetric
specialization of the L3 [`inner_product`](./inner_product.md) combinator at the conjugated
kernel value with `M = I`:

    dot(x, y)  = inner_product x y          -- Hermitian (complex) / symmetric (real)
    tdot(x, y) = inner_product x y          -- with the unconjugated kernel (complex-only)

The combinator carries the reduce-to-scalar base form, the algebraic laws, and the
no-sequential-obstruction verdict; this `dot` chapter adds only the leaf-level conjugation /
consuming-context framing. **Do NOT merge into `inner_product`** — the named-specialization
presence is what lets a reader navigating the `krylov-step` body or the L3 vocabulary inventory
find `dot` in L3 vocabulary (CLAUDE.md §Methodology invariants **Identity-lowerings still
require both L levels**).

## Signature

    dot   :: Tensor[(S: ...)] -> Tensor[S] -> Scalar
    tdot  :: Tensor[(S: ...)] -> Tensor[S] -> Scalar     -- complex-only variant

The combinator's signature read at the plain (`M = I`) conjugation value (named shape groups
per [`l4_calculus`](../design/l4_calculus.md) §1.2.1 — both operands congruent over one shape
group `S` of arbitrary unknown rank, NOT rank-1). Full shape contract:
[`inner_product`](./inner_product.md) §Signature.

## Conjugation variant-axis (the leaf-level fact, value-bearing for complex vectors)

The conjugation convention is **value-bearing for complex vectors** and is the one fact this
specialization carries beyond the combinator. `dot` is **conjugate-linear in the first
argument**, linear in the second (`⟨x, y⟩ = xᴴ y`); `tdot` is the unconjugated co-variant. The
per-element kernel by element-type:

| element type | `dot(x, y)` returns | per-element kernel |
|---|---|---|
| `real`    | `real`    | `x[idx] * y[idx]` |
| `complex` | `complex` | `conj(x[idx]) * y[idx]` *(Hermitian, conjugate-linear in first arg)* |
| `complex` (via `tdot`) | `complex` | `x[idx] * y[idx]` *(unconjugated bilinear)* |

`dot` and `tdot` are distinct operators because their laws differ — `dot` is PSD-at-diagonal
(`dot(x, x) ≥ 0`), `tdot` is the indefinite form (`tdot(x, x) = 0` does not imply `x = 0`). The
L0 free-function asymmetry — `linalg::Dot(comm, x, y) = yᴴ x = conj(xᴴ y)` — and its reconciling
re-order are the genuine translation carried by the KEPT L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme (firm
cycle-019, KEPT cycle-049 D2; documented at `book/src/L1/dot.md:43, 104-105`), not L3 content.
L3 sees the convention pinned at arg-1.

## Consuming context (the other leaf-level fact)

`dot` is **consumed inside** larger L3 forms — most notably the `krylov-step` body's
iterate-and-scalar update sub-composition (CG's `α = dot(r, z) / dot(Ap, p)`; GMRES's
orthogonalization coefficients `dot(v_i, w)`; per `book/src/L3-L2/krylov-step-body-identity.md:30-37`).
At L3 `dot` is a leaf reduction with no iteration view of its own; the iteration view is what the
surrounding `krylov-step` body provides.

## Status

`firm` — specialization-stub. `dot` at L3 is the `M = I` Hermitian/symmetric specialization of
the firm L3 [`inner_product`](./inner_product.md) combinator (firm cycle-050); the
reduce-to-scalar base form, algebraic laws, no-sequential-obstruction verdict, and downward
lowering are inherited from the combinator unchanged. This chapter retains only the
value-bearing conjugation variant-axis and the consuming-context framing. Originally harvested
cycle-011 wave-1 (BLAS-1 reduction cohort backfill); re-expressed through the combinator
cycle-051 (the degenerate `dot-body-identity` / `dot-leaf-identity` themes demoted into the
combinator's homes the same cycle); reduced to a specialization-stub cycle-052 D3
(vocabulary-shift-redirect refactor pass). The named-leaf presence is retained per CLAUDE.md
§Methodology invariants **Identity-lowerings still require both L levels** and as the named
workhorse specialization the combinator's §"Specializations" points back at (⟢).

## Downward to L2 (through inner_product)

L3 `dot` lowers **through the L3 [`inner_product`](./inner_product.md) combinator** — the
combinator lowers to L2 [`inner_product`](../L2/inner_product.md) as identity-in-form on the body
(in-line §"Downward to L2" at the combinator, per the cycle-012 non-adjacent-identity
convention). There is no separate `dot`-specific L3>L2 theme (the former degenerate
`dot-body-identity` theme was demoted into the combinator's §"Downward to L2" home cycle-051).
The genuine translation in the chain is the KEPT L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme
(conjugation/element-type/weight dispatch + the `xᴴ y` ↔ `yᴴ x` re-order + per-call pinned
reduction trees). Bit-reproduction / re-order / reduction-tree concerns are read off the
fold-specialization theme, not re-derived here.

## Lifts from

L3 `dot` lifts to the firm L4 [`dot`](../L4/dot.md) (firm cycle-069 D2) by **identity-in-form on
the body** — the L4 form is the calculus-level named verb re-expressing the [`inner_product`](../L4/inner_product.md)
combinator at `M = I` with the Hermitian/symmetric kernel; it is value-thread-isomorphic to this
L3 specialization-stub (the same `Tensor[(S: ...)] -> Tensor[S] -> Scalar` reduction at the plain-weight
conjugation value), so there is **no dedicated L4>L3 theme** (the in-line-marker route, the
`inner_product`/`eigsolve`/`chebyshev` shape — no monadic wrapper / `Solve` monad / convergence
predicate to dissolve). `dot` is one of the **kept named abstractions** that rise to L4 as named
verbs *alongside* the general combinator (the permitted dual per
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2 — the
literature-standard unit a CG/GMRES description spells `dot(p, Ap)` / `dot(r, z)` rather than an
inlined application). At L4 `dot` also still appears *inside* larger composed entries (e.g.
`book/src/L4/krylov-step.md` §Semantics) as a let-binding consuming the primitive surface.

> **Superseded.** This entry formerly recorded `dot` as having **no L4 entry** — "leaf
> primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict); at L4 `dot`
> appears only inside larger composed entries as a let-binding." That blanket "no-L4-by-design"
> reading was **superseded cycle-069 D2** when `dot` rose to a firm L4 named verb. Under the
> 2026-06-01 VOCABULARY-SHIFT REDIRECT (L4 is the outward backend-lowering target) the per-case
> disposition of [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
> §2 governs: the `inner_product` combinator rises regardless, and the **kept named abstractions
> `dot` / `nrm2` rise alongside it as named verbs** (distinct from the *pure accelerated kernels*
> `scal` / `axpy` / `axpby` / `axpbypcz`, which correctly stay low). The cycle-010 verdict was
> right for accelerated-kernel leaves; `dot` is a kept named abstraction, not such a leaf.

## Evidence

`dot`'s deferred-to homes + leaf-level anchors (RETAINED). All semantics/laws/lowering evidence
is the combinator's / the firm L1 leaf's:

- [`book/src/L3/inner_product.md`](./inner_product.md) (firm cycle-050) — the combinator this
  entry specializes; §"Specializations" (`:133`) names this `dot` chapter as the workhorse
  Hermitian/symmetric specialization; authoritative on the base form, laws, and
  no-sequential-obstruction verdict (all deferred here).
- [`book/src/L2-L1/inner-product-fold-specialization.md`](../L2-L1/inner-product-fold-specialization.md) (firm cycle-019, KEPT cycle-049 D2) — the genuine L2>L1 translation; the conjugation/element-type/weight dispatch + `xᴴ y` ↔ `yᴴ x` re-order + pinned reduction trees.
- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — authoritative on Palace surface,
  signature, algebraic laws, variant axes, and the complete L0 evidence list (`vector.hpp:110-113`,
  `vector.cpp:263-274`, `vector.cpp:665-685`, etc.).
- [`book/src/L3/krylov-step.md`](./krylov-step.md) §Semantics + [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 — the consuming context + the structural justification (`dot` L3-native by signature shape).
- `palace/linalg/iterative.cpp:395, 404, 444, 460` — CG using `linalg::Dot` for `β = ⟨z, r⟩` and the α-denominator `⟨z, p⟩`; the consuming context at L0, inherited transitively. (Path relative to `reference/palace/`.)
- [`book/src/concepts/dot.md`](../concepts/dot.md) — the cross-cutting concept page; BLAS-1 heritage framing.
