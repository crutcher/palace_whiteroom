---
layer: L3
operator: dot
firmness: firm
lowers_to:
  - book/src/L2/inner_product.md (dot is the Hermitian/symmetric specialization of the inner_product combinator; identity-in-form on the body — see §"Downward to L2 (through inner_product)")
lifts_from:
  - (none) — `dot` is a reduction specialization; no L4 entry exists (folds/leaves are not first-class L4 vocabulary per cycle-010 audit verdict; the combinator appears inside L4 composed entries like krylov-step §Semantics as a let-binding)
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

    dot   :: Tensor[N] -> Tensor[N] -> Scalar
    tdot  :: Tensor[N] -> Tensor[N] -> Scalar     -- complex-only variant

The combinator's signature read at the plain (`M = I`) conjugation value; identical to the L1
signature. Full shape contract: [`inner_product`](./inner_product.md) §Signature.

## Conjugation variant-axis (the leaf-level fact, value-bearing for complex vectors)

The conjugation convention is **value-bearing for complex vectors** and is the one fact this
specialization carries beyond the combinator. `dot` is **conjugate-linear in the first
argument**, linear in the second (`⟨x, y⟩ = xᴴ y`); `tdot` is the unconjugated co-variant. The
per-element kernel by element-type:

| element type | `dot(x, y)` returns | per-element kernel |
|---|---|---|
| `real`    | `real`    | `x[i] * y[i]` |
| `complex` | `complex` | `conj(x[i]) * y[i]` *(Hermitian, conjugate-linear in first arg)* |
| `complex` (via `tdot`) | `complex` | `x[i] * y[i]` *(unconjugated bilinear)* |

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

`dot` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010
audit verdict). At L4, `dot` appears inside larger composed entries (e.g.,
`book/src/L4/krylov-step.md` §Semantics) as a let-binding consuming the L3-native primitive
surface.

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
