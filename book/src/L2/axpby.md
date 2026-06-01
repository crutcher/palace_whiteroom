---
layer: L2
operator: axpby
firmness: firm
specialization_of:
  - book/src/L2/linear_combination.md (arity-2 member, general second coefficient — the L2 family entry; see its §"Arity specializations")
lowers_to:
  - book/src/L1/axpby.md (identity-in-form; the L1 leaf carries the load-bearing one-to-one L0-symbol shape; L1>L0 in-place form is `axpby-mutation-rotation`)
variant_axes:
  - element-type (real / complex; scalar-promotion sub-axis real-(α,β)-against-complex-vectors)
  - output-aliasing (the FOLD's axis — see linear_combination §Variant axes)
---

# axpby

**`axpby` is the arity-2 specialization of
[`linear_combination`](./linear_combination.md)** (general second coefficient) — the L2
entry for the BLAS-1 scalar-weighted-sum family (vocabulary-shift redirect 2026-06-01). The
family speaks through the combinator at L2 and above;
`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`, recorded as the arity-2 readout
label in [`linear_combination` §"Arity specializations"](./linear_combination.md). The free
second coefficient `β` is what distinguishes `axpby` from the fixed-1 `axpy` at the same
arity. All semantics, the algebraic laws (the arity-2 shadow of the combinator's
concatenation-homomorphism / multilinearity / coefficient-scaling laws — the per-op
bilinearity is the multilinearity law read at list-length 2), the fusion note (the fused
`α·x + β·y` single-aligned `add(α,x,β,y,y)` pass), and the variant-axis treatment are the
combinator's — **deferred to [`linear_combination`](./linear_combination.md), not
re-authored here**.

This chapter is retained as a **specialization-stub** (not a standalone L2 floor): the
arity-2 readout label for the bounded-arity L0 call shape, holding the operator's unique L0
anchors and its variant-axis row. The L1 leaf [`axpby`](../L1/axpby.md) stays firm (it
carries the load-bearing one-to-one L0-symbol shape for the L1>L0 mutation rotation
[`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md)).

## Signature

    axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpby α x β y = α·x + β·y = linear_combination [(α, x), (β, y)]

Arity-2 instance (general second coeff) of the combinator's
`linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`
(`linear_combination.md` §Signature). The element-type / scalar-promotion sub-axis is
inherited unchanged from the combinator.

## Variant axes

- **element-type** (`real` | `complex`), with the `real ⊑ complex` scalar-promotion
  sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)) — real `(α, β)`
  against complex `x, y` (promote all-or-none) via the real-scalar-on-complex-vector overload
  at `vector.cpp:739-743`. Inherited from the combinator's element-type axis; absorbed at
  construction.
- **output-aliasing** (in-place `y ← α·x + β·y` vs fresh-output) is the **FOLD's** variant
  axis (`linear_combination.md` §Variant axes, axis 1), orthogonal to arity; at L2 this
  specialization is pure / out-of-place.

## Status

`firm` — specialization-stub pointing at the firm combinator
[`linear_combination`](./linear_combination.md) (cycle-018). Reduced from a standalone L2
floor to a specialization note cycle-052 (batch-16 refactor) per the vocabulary-shift
redirect (a same-named base-form floor mirrored beside the combinator is the retired
rectangular pattern — [`linear_combination`](./linear_combination.md) §Context).

## Evidence

The semantics / laws / fusion-note evidence is the combinator's
([`linear_combination`](./linear_combination.md) §Evidence; the shared `vector.cpp:726-730`
real-real `AXPBY` → MFEM `add(α,x,β,y,y)` fusion-pass site and the `vector.hpp:309-311` decl
are carried there). The L0 anchors UNIQUE to the arity-2 (general) readout label (retained
here so they stay navigable):

- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member declaration, comment
  `In-place addition (*this) = alpha * x + beta * (*this).` (the receiver-mutating member
  form).
- `palace/linalg/vector.cpp:732-737` — complex-complex specialisation
  `AXPBY(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)`:
  delegates to the member form `y.AXPBY(alpha, x, beta)`.
- `palace/linalg/vector.cpp:739-743` — real-scalar-on-complex-vector specialisation
  `AXPBY(double, ComplexVector, double, ComplexVector)`: also delegates to the member form
  (implicit scalar promotion; the scalar-promotion sub-axis L0 anchor).

(All anchors self-verified on-disk via `tools/citecheck/citecheck.py --anchor`, 2026-06-01.)
