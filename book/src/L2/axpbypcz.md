---
layer: L2
operator: axpbypcz
firmness: firm
specialization_of:
  - book/src/L2/linear_combination.md (arity-3 member — the L2 family entry; see its §"Arity specializations")
lowers_to:
  - book/src/L1/axpbypcz.md (identity-in-form; the L1 leaf carries the load-bearing one-to-one L0-symbol shape; L1>L0 in-place form is `axpbypcz-mutation-rotation`)
variant_axes:
  - element-type (real / complex; scalar-promotion sub-axis real-(α,β,γ)-against-complex-(x,y,z))
  - output-aliasing (the FOLD's axis — see linear_combination §Variant axes)
---

# axpbypcz

**`axpbypcz` is the arity-3 specialization of
[`linear_combination`](./linear_combination.md)** — the L2 entry for the BLAS-1
scalar-weighted-sum family (vocabulary-shift redirect 2026-06-01). The family speaks through
the combinator at L2 and above;
`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`, recorded as the
arity-3 readout label in
[`linear_combination` §"Arity specializations"](./linear_combination.md). It is the maximal
fixed-arity L0 symbol — combinations of more than three terms are open-coded in Palace as
iterated `axpbypcz`-into-output (the `γ=1` accumulate sites), which the variadic combinator
abstracts. All semantics, the algebraic laws (the arity-3 shadow of the combinator's
concatenation-homomorphism / multilinearity laws — the per-op trilinearity is the
multilinearity law read at list-length 3; the `γ==0` subsumption of `axpby` is the
combinator's zero-coefficient term-drop law 5, the exact algebraic content of the in-source
`γ==0` branch at `vector.cpp:749-751`), the fusion note (the arity-3 single-aligned pass /
`γ==0` arity-collapse), and the variant-axis treatment are the combinator's — **deferred to
[`linear_combination`](./linear_combination.md), not re-authored here**.

This chapter is retained as a **specialization-stub** (not a standalone L2 floor): the
arity-3 readout label for the bounded-arity L0 call shape, holding the operator's unique L0
anchors and its variant-axis row. The L1 leaf [`axpbypcz`](../L1/axpbypcz.md) stays firm (it
carries the load-bearing one-to-one L0-symbol shape for the L1>L0 mutation rotation
[`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md)).

## Signature

    axpbypcz :: Scalar -> Tensor[(S: ...)] -> Scalar -> Tensor[S] -> Scalar -> Tensor[S] -> Tensor[S]
    axpbypcz α x β y γ z = α·x + β·y + γ·z = linear_combination [(α, x), (β, y), (γ, z)]

Arity-3 instance of the combinator's
`linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[S]`
(`linear_combination.md` §Signature). Named shape groups per
[`l4_calculus`](../design/l4_calculus.md) §1.2.1: `S` is the shared shape group of
arbitrary, unknown rank (NOT rank-1) — the three terms and the result are congruent and
`axpbypcz` is element-local at every position of `S`. The element-type / scalar-promotion
sub-axis is inherited unchanged from the combinator.

## Variant axes

- **element-type** (`real` | `complex`), with the `real ⊑ complex` scalar-promotion
  sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)) — real
  `(α, β, γ)` against complex `(x, y, z)` (promote all-or-none) via the
  real-scalar-on-complex-vector specialisation at `vector.cpp:767-772`. Inherited from the
  combinator's element-type axis; absorbed at construction.
- **output-aliasing** (in-place `z ← α·x + β·y + γ·z` vs fresh-output) is the **FOLD's**
  variant axis (`linear_combination.md` §Variant axes, axis 1), orthogonal to arity; the
  `γ=1` accumulate-into sites (`nleps.cpp:343-344`, `romoperator.cpp:188-189`) are the
  fold's aliasing case (carried in the combinator's Evidence). At L2 this specialization is
  pure / out-of-place.

## Status

`firm` — specialization-stub pointing at the firm combinator
[`linear_combination`](./linear_combination.md) (cycle-018). Reduced from a standalone L2
floor to a specialization note cycle-052 (batch-16 refactor) per the vocabulary-shift
redirect (a same-named base-form floor mirrored beside the combinator is the retired
rectangular pattern — [`linear_combination`](./linear_combination.md) §Context).

## Evidence

The semantics / laws / fusion-note evidence is the combinator's
([`linear_combination`](./linear_combination.md) §Evidence; the shared `vector.cpp:749-751`
`γ==0` arity-collapse branch, the `vector.hpp:313-316` decl, and the `nleps.cpp:343-344` /
`romoperator.cpp:188-189` / `timeoperator.cpp:217` `γ=1`/`γ=0` live sites are carried there).
The L0 anchors UNIQUE to the arity-3 readout label (retained here so they stay navigable):

- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member declaration, comment
  `In-place addition (*this) = alpha * x + beta * y + gamma * (*this).`
- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double, Vector, double, Vector, double,
  Vector)` real-real specialisation with the `γ == 0` branch: fast-path delegates to MFEM's
  `add(alpha, x, beta, y, z)` (`:749-751`, the arity-collapse the combinator carries);
  slow-path splits into `AXPBY(alpha, x, gamma, z); z.Add(beta, y)` (`:755-756`).
- `palace/linalg/vector.cpp:760-765` — `AXPBYPCZ(std::complex<double>, ComplexVector, …)`
  complex-complex specialisation: delegates to member
  `z.AXPBYPCZ(alpha, x, beta, y, gamma)`.
- `palace/linalg/vector.cpp:767-772` — `AXPBYPCZ(double, ComplexVector, …)`
  real-scalar-on-complex-vector specialisation: also delegates to the member form (implicit
  scalar promotion; the scalar-promotion sub-axis L0 anchor).

(All anchors self-verified on-disk via `tools/citecheck/citecheck.py --anchor`, 2026-06-01.)
