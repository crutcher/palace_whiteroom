---
layer: L2
operator: axpy
firmness: firm
specialization_of:
  - book/src/L2/linear_combination.md (arity-2 member, second coefficient fixed to 1 — the L2 family entry; see its §"Arity specializations")
lowers_to:
  - book/src/L1/axpy.md (identity-in-form; the L1 leaf carries the load-bearing one-to-one L0-symbol shape; L1>L0 in-place form is `axpby-mutation-rotation` sub-pattern A, the β=1 specialization)
variant_axes:
  - element-type (real / complex; scalar-promotion sub-axis real-α-against-complex-x)
  - output-aliasing (the FOLD's axis — see linear_combination §Variant axes)
---

# axpy

**`axpy` is the arity-2 specialization of
[`linear_combination`](./linear_combination.md)** with the **second coefficient fixed to
1** — the L2 entry for the BLAS-1 scalar-weighted-sum family (vocabulary-shift redirect
2026-06-01). The family speaks through the combinator at L2 and above;
`axpy(α, x, y) = linear_combination [(α, x), (1, y)]`, recorded as the arity-2 readout label
in [`linear_combination` §"Arity specializations"](./linear_combination.md). The fixed-1
`y`-coefficient is exactly what distinguishes `axpy` from the free-second-coefficient
`axpby` at the same arity. All semantics, the algebraic laws (the arity-2 shadow of the
combinator's concatenation-homomorphism / multilinearity laws), the fusion note (the
two-term single-aligned pass), and the variant-axis treatment are the combinator's —
**deferred to [`linear_combination`](./linear_combination.md), not re-authored here**.

This chapter is retained as a **specialization-stub** (not a standalone L2 floor): the
arity-2 readout label for the bounded-arity L0 call shape, holding the operator's unique L0
anchors and its variant-axis row. The L1 leaf [`axpy`](../L1/axpy.md) stays firm (it carries
the load-bearing one-to-one L0-symbol shape for the L1>L0 mutation rotation
[`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A).

## Signature

    axpy :: Scalar -> Tensor[(S: ...)] -> Tensor[S] -> Tensor[S]
    axpy α x y = α·x + y = linear_combination [(α, x), (1, y)]

Arity-2 instance (second coeff fixed 1) of the combinator's
`linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[S]`
(`linear_combination.md` §Signature). Named shape groups per
[`l4_calculus`](../design/l4_calculus.md) §1.2.1: `S` is the shared shape group of
arbitrary, unknown rank (NOT rank-1) — the two terms and the result are congruent and
`axpy` is element-local at every position of `S`. The element-type / scalar-promotion
sub-axis is inherited unchanged from the combinator.

## Variant axes

- **element-type** (`real` | `complex`), with the `real ⊑ complex` scalar-promotion
  sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)) — real `α`
  against complex `x, y` via the real-α-on-complex-vector forwarding overload at
  `vector.cpp:714-718`. Inherited from the combinator's element-type axis; absorbed at
  construction.
- **output-aliasing** (in-place `y ← α·x + y` vs fresh-output) is the **FOLD's** variant
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
([`linear_combination`](./linear_combination.md) §Evidence; the shared `vector.cpp:702-712`
real-real `AXPY` site with the `α == 1.0` fast-path and the `vector.hpp:305-307` decl are
carried there). The L0 anchors UNIQUE to the arity-2 readout label (retained here so they
stay navigable):

- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` (and `Add` / `Subtract`
  aliases) member declaration, comment `In-place addition (*this) += alpha * x.`
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition and the element-wise
  `forall_switch` kernels (`YR[i] += ar·XR[i] − ai·XI[i]`).
- `palace/linalg/vector.cpp:714-718` — `AXPY(double, ComplexVector, ComplexVector)`, the
  real-α-on-complex-vector forwarding overload (the scalar-promotion sub-axis L0 anchor).
- `palace/linalg/vector.cpp:720-724` — `AXPY(std::complex<double>, ComplexVector,
  ComplexVector)`, the complex-α overload forwarding to the member `ComplexVector::AXPY`.

(All anchors self-verified on-disk via `tools/citecheck/citecheck.py --anchor`, 2026-06-01.)
