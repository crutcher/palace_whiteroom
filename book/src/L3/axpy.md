---
layer: L3
operator: axpy
firmness: firm
lowers_to:
  - book/src/L2/linear_combination.md (the arity-2 specialization of the firm L3/L2 `linear_combination` fold, second coeff fixed to 1; `axpy(α,x,y) = linear_combination [(α,x),(1,y)]`; lowers via the combinator's §"Downward to L2" identity-in-form edge, then the substantive arity-dispatch is the L2>L1 `linear-combination-fold-specialization` theme) → book/src/L1/axpy.md (transitive L3>L1 identity in-line, the fold-specialization picking the `AXPY` L0 leaf)
lifts_from:
  - book/src/L3/linear_combination.md (the family combinator this leaf is the arity-2 specialization of — `axpy` speaks through `linear_combination`, not as a re-derived base form, per the 2026-06-01 vocabulary-shift redirect; no L4 entry — the fold is a pure value-producing reduction, not a calculus combinator)
variant_axes:
  - element-type (real | complex)
  - scalar-promotion (sub-axis on complex element-type)
---

# axpy

`axpy` is the **arity-2 specialization of [`linear_combination`](./linear_combination.md)** with the second coefficient fixed to 1: `axpy(α, x, y) = α·x + y = linear_combination [(α, x), (1, y)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms `scal` / `axpy` / `axpby` / `axpbypcz` speak **through** the combinator, not as re-derived base forms — `axpy` is the combinator at term-list length 2 with the trailing coefficient pinned to 1. This chapter is the arity-2-coeff-1 **readout label** for the bounded-arity L0 call shape (`AXPY`); its semantics, signature, algebraic laws, iteration-rotation profile, and L3-vs-L1 framing are the combinator's, read at length 2 — see [`linear_combination`](./linear_combination.md) (the §"Arity specializations" notes and the §"Downward to L2" combinator-identity note are the home). What this stub retains below is `axpy`'s **unique L0 surface** (the `AXPY` free-function + complex-overload + promotion sites, plus the load-bearing `α == 1.0` fast-path) and its **one collapsed variant-axis row**.

## Specialization

- **Arity**: 2, second coefficient fixed to 1 (`axpy(α, x, y) = linear_combination [(α, x), (1, y)]`).
- **L0 call shape**: the free-function `AXPY` symbol (real `AXPY(double, Vector, Vector)` + `ComplexVector::AXPY`).
- **Lowering**: routes through the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at length 2 (trailing coeff 1), then the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme, which selects the `AXPY` L0 leaf and records its pinned summation order. The substantive in-place mutation rotation, reached transitively, is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (`axpy` as the β=1 specialisation of `axpby`).
- **Load-bearing fast-path**: the real-path `AXPY(double, Vector, Vector)` carries an `α == 1.0` constant-fold fast-path (`palace/linalg/vector.cpp:702-712`) — the one constant-folding branch distinguishing `axpy` from `axpby`/`axpbypcz` (which have none) and `scal` (which has none). The fast-path is a transparent performance trick erased at L1; the L2>L1 fold-specialization theme is where its selection is recorded.

The downward edge, the seven combinator laws read at length 2 (`axpy`'s six laws are the length-2-coeff-1 reading; `L1/axpy.md` §Algebraic laws is the firm endpoint), the no-sequential-obstruction profile (`L3/linear_combination.md` §Semantics; this leaf is the cohort obstruction-free precedent), and the L3-vs-L1 documentary-framing distinction are all the combinator's — deferred there, not restated here.

## Variant axes

The two variant axes are the combinator's element-type axis read at arity 2 (inherited unchanged from L1; both absorbed at construction, neither in the positional signature):

1. **element-type** (`real | complex`) — separate L0 overloads (real `AXPY`; `ComplexVector::AXPY`, `palace/linalg/vector.cpp:276-311`) collapse to one element-type-parameterised operator at L1/L3.
2. **scalar-promotion** (sub-axis on the complex element-type; [`scalar-promotion`](../concepts/scalar-promotion.md)) — real `α` against complex `x, y` promoted to complex with zero imaginary part (`palace/linalg/vector.cpp:715-718`); typing-rule property, not an operator variant.

## Status

`firm` — `axpy` is the arity-2-coeff-1 specialization of the firm L3 combinator [`linear_combination`](./linear_combination.md); its signature, laws, and lowering are the combinator's read at length 2 (firm L1 endpoint `book/src/L1/axpy.md`, cycle-002). The L0 surface retained here is self-verified on-disk this dispatch (`vector.cpp:276-311`, `:702-712` incl. the `α==1.0` fast-path, `:715-718`; `vector.hpp:115-118`, `:305-307`). Reduced to a specialization-stub cycle-052 D2 (the reduce-to-stub completion of the cycle-051 re-expression; semantics deferred to the combinator, duplicated body deleted; file KEPT so inbound links — incl. `L3-L2/orthogonalize-variant-split.md` → `../L3/axpy.md`, `L2/axpy.md` → `../L3/axpy.md` — stay live).

## Evidence

`axpy` is the arity-2 fold member; its semantics and laws live at [`linear_combination`](./linear_combination.md) (combinator) and `book/src/L1/axpy.md` (firm L1 endpoint, cycle-002). Anchors retained here are `axpy`'s **unique** L0 surface — the `AXPY` free-function + complex-overload + promotion sites incl. the `α==1.0` fast-path — which the combinator's generic free-function-surface anchors (`vector.hpp:305-316`) do not pinpoint at the arity-2 resolution:

- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition (the complex arity-2 overload).
- `palace/linalg/vector.cpp:702-712` — free-function `AXPY(double, Vector, Vector)` with the **`α == 1.0` fast-path** (the load-bearing arity-2-only constant-fold branch).
- `palace/linalg/vector.cpp:715-718` — real-α-on-complex-vector promotion site (scalar-promotion sub-axis).
- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` + `Add`/`Subtract` aliases decl.
- `palace/linalg/vector.hpp:305-307` — free-function template `AXPY` decl.

Combinator + firm-L1 anchors (semantics + laws home): `book/src/L3/linear_combination.md` (firm cycle-050; §"Arity specializations" `:50-61`, §"Downward to L2" `:107-113`), `book/src/L1/axpy.md` (cycle-002 firm), `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; the lowering's substantive content + pinned summation order), `book/src/concepts/axpy.md` + `book/src/concepts/scalar-promotion.md` (cross-cutting prose + typing rule).
