---
layer: L2
operator: scal
firmness: firm
specialization_of:
  - book/src/L2/linear_combination.md (arity-1 member — the L2 family entry; see its §"Arity specializations")
lowers_to:
  - book/src/L1/scal.md (identity-in-form; the L1 leaf carries the load-bearing one-to-one L0-symbol shape)
variant_axes:
  - element-type (real / complex; scalar-promotion sub-axis real-α-against-complex-x)
  - output-aliasing (the FOLD's axis — see linear_combination §Variant axes)
---

# scal

**`scal` is the arity-1 specialization of
[`linear_combination`](./linear_combination.md)** — the L2 entry for the BLAS-1
scalar-weighted-sum family (vocabulary-shift redirect 2026-06-01). The family speaks
through the combinator at L2 and above; `scal(α, x) = linear_combination [(α, x)]` (the
single-term list), recorded as the arity-1 readout label in
[`linear_combination` §"Arity specializations"](./linear_combination.md). All
semantics, the algebraic laws (the arity-1 shadow of the combinator's multilinearity /
coefficient-scaling laws), the fusion note (the degenerate single-term seed-and-accumulate),
and the variant-axis treatment are the combinator's — **deferred to
[`linear_combination`](./linear_combination.md), not re-authored here**.

This chapter is retained as a **specialization-stub** (not a standalone L2 floor): the
arity-1 readout label for the bounded-arity L0 call shape, holding the operator's unique L0
anchors and its variant-axis row so the family's per-arity L0 navigation stays resolvable
from a real file. The L1 leaf [`scal`](../L1/scal.md) stays firm (it carries the
load-bearing one-to-one L0-symbol shape for the L1>L0 mutation rotation
[`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md)).

## Signature

    scal :: Scalar -> Tensor[(S: ...)] -> Tensor[$S]
    scal α x = α·x = linear_combination [(α, x)]

Arity-1 instance of the combinator's
`linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]`
(`linear_combination.md` §Signature). Named shape groups per
[`l4_calculus`](../design/l4_calculus.md) §1.2.1: `S` is the shared shape group of
arbitrary, unknown rank (NOT rank-1) — `scal` is element-local at every position of `S`,
and the result is congruent to `x`. The element-type / scalar-promotion sub-axis is
inherited unchanged from the combinator.

## Variant axes

- **element-type** (`real` | `complex`), with the `real ⊑ complex` scalar-promotion
  sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)) — real `α`
  against complex `x` via the internal `si == 0.0` branch at `vector.cpp:207-211`. Inherited
  from the combinator's element-type axis; absorbed at construction, not in the positional
  signature.
- **output-aliasing** (in-place `x *= α` vs fresh-output) is the **FOLD's** variant axis
  (`linear_combination.md` §Variant axes, axis 1), orthogonal to arity; at L2 this
  specialization is pure / out-of-place, aliasing being an L2>L1 lowering concern.

## Status

`firm` — specialization-stub pointing at the firm combinator
[`linear_combination`](./linear_combination.md) (cycle-018). Reduced from a standalone L2
floor to a specialization note cycle-052 (batch-16 refactor) per the vocabulary-shift
redirect: a same-named base-form floor mirrored beside the combinator was the retired
rectangular pattern ([`linear_combination`](./linear_combination.md) §Context).

## Evidence

The semantics / laws / fusion-note evidence is the combinator's
([`linear_combination`](./linear_combination.md) §Evidence). The L0 anchors UNIQUE to the
arity-1 readout label (those the combinator's Evidence does not already carry; retained here
so they stay navigable):

- `palace/linalg/vector.hpp:98-99` — `ComplexVector::operator*=(std::complex<double> s)`
  declaration with comment `Scale all entries by s.` (the arity-1 L0 symbol).
- `palace/linalg/vector.cpp:207-211` — the `if (si == 0.0)` real fast-path branch inside
  `ComplexVector::operator*=` (`vector.cpp:203-227`, the arity-1 site the combinator
  Evidence carries) — the internal scalar-promotion site (real-into-complex), the L0 anchor
  for the scalar-promotion sub-axis.
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template
  (`auto norm = Norml2(comm, x); … x *= 1.0 / norm; return norm;`) — the fused `nrm2 + scal`
  construct that the firm L2 [`normalize`](./normalize.md) composite factors as
  `scal(1/nrm2(x), x)`; the arity-1 `scal` site in the wild.

(All anchors self-verified on-disk via `tools/citecheck/citecheck.py --anchor` + `--show`,
2026-06-01. The shared arity-1 site `vector.cpp:203-227` and `iterative.cpp:632` are in the
combinator's Evidence.)
