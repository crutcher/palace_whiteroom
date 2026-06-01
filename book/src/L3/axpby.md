---
layer: L3
operator: axpby
firmness: firm
lowers_to:
  - book/src/L2/linear_combination.md (the general arity-2 specialization of the firm L3/L2 `linear_combination` fold; `axpby(α,x,β,y) = linear_combination [(α,x),(β,y)]`; lowers via the combinator's §"Downward to L2" identity-in-form edge, then the substantive arity-dispatch is the L2>L1 `linear-combination-fold-specialization` theme) → book/src/L1/axpby.md (transitive L3>L1 identity in-line, the fold-specialization picking the `AXPBY` L0 leaf)
lifts_from:
  - book/src/L3/linear_combination.md (the family combinator this leaf is the general arity-2 specialization of — `axpby` speaks through `linear_combination`, not as a re-derived base form, per the 2026-06-01 vocabulary-shift redirect; no L4 entry — the fold is a pure value-producing reduction, not a calculus combinator)
variant_axes:
  - element-type (real | complex)
  - scalar-promotion (sub-axis on complex element-type)
---

# axpby

`axpby` is the **general arity-2 specialization of [`linear_combination`](./linear_combination.md)**: `axpby(α, x, β, y) = α·x + β·y = linear_combination [(α, x), (β, y)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms `scal` / `axpy` / `axpby` / `axpbypcz` speak **through** the combinator, not as re-derived base forms — `axpby` is the combinator at term-list length 2 with both coefficients free (subsuming [`axpy`](./axpy.md) at the second-coeff-1 reading and pure-scaling at α=0 or β=0). This chapter is the arity-2 **readout label** for the bounded-arity L0 call shape (`AXPBY`); its semantics, signature, algebraic laws, iteration-rotation profile, and L3-vs-L1 framing are the combinator's, read at length 2 — see [`linear_combination`](./linear_combination.md) (the §"Arity specializations" notes and the §"Downward to L2" combinator-identity note are the home). What this stub retains below is `axpby`'s **unique L0 surface** (the `AXPBY` free-function + complex-overload + promotion sites + the MFEM fused-pass note) and its **one collapsed variant-axis row**.

## Specialization

- **Arity**: 2, both coefficients free (`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`).
- **L0 call shape**: the free-function `AXPBY` symbol (real-real `AXPBY` + `ComplexVector::AXPBY`), realized as MFEM's single aligned in-place `add(α, x, β, y, y)` pass (`palace/linalg/vector.cpp:726-730`).
- **Lowering**: routes through the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at length 2 (both coeffs free), then the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme, which selects the `AXPBY` L0 leaf and records the pinned summation order of the MFEM fused pass. The substantive in-place mutation rotation, reached transitively, is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md).
- **Constant-folding**: `axpby` has **no** L0 constant-folding branch inside the `AXPBY` family (unlike `axpy`'s `α == 1.0` fast-path; the L0 surface uniformly delegates without inspecting scalar values). This no-fast-path fact distinguishes it from `axpy` and `axpbypcz` (which has the `γ==0` collapse).
- **Fused-primitive choice**: `axpby` is the fused primitive `α·x + β·y`, NOT a decomposition of `scal ∘ axpy` (`scaffolding/decisions/axpby-as-primitive.md`, cycle-003; inherited unchanged). `axpy` is the β=1 specialisation (combinator law 6 / the subsumption identity), kept as a sibling in the dep-map, not a dependency.

The downward edge, the seven combinator laws read at length 2 (`axpby`'s nine laws are the both-coeffs-free reading; `L1/axpby.md` §Algebraic laws is the firm endpoint), the no-sequential-obstruction profile, and the L3-vs-L1 documentary-framing distinction are all the combinator's — deferred there, not restated here.

## Variant axes

The two variant axes are the combinator's element-type axis read at arity 2 (inherited unchanged from L1; both absorbed at construction, neither in the positional signature):

1. **element-type** (`real | complex`) — separate L0 overloads (real-real `AXPBY`; complex-complex `ComplexVector::AXPBY`, `palace/linalg/vector.cpp:732-737`) collapse to one element-type-parameterised operator at L1/L3.
2. **scalar-promotion** (sub-axis on the complex element-type; [`scalar-promotion`](../concepts/scalar-promotion.md)) — real `(α, β)` against complex `x, y` promoted to complex with zero imaginary part, all-or-none across the scalar pair (`palace/linalg/vector.cpp:739-743`); typing-rule property, not an operator variant.

## Status

`firm` — `axpby` is the general arity-2 specialization of the firm L3 combinator [`linear_combination`](./linear_combination.md); its signature, laws, and lowering are the combinator's read at length 2 (firm L1 endpoint `book/src/L1/axpby.md`, cycle-003). The L0 surface retained here is self-verified on-disk this dispatch (`vector.cpp:726-730` real-real fused pass, `:732-737` complex-complex, `:739-743` promotion; `vector.hpp:130-131`, `:309-311`). The fused-primitive choice (`scaffolding/decisions/axpby-as-primitive.md`, cycle-003) is inherited unchanged. Reduced to a specialization-stub cycle-052 D2 (the reduce-to-stub completion of the cycle-051 re-expression; semantics deferred to the combinator, duplicated body deleted; file KEPT so inbound links — incl. `L2/axpby.md` → `../L3/axpby.md` — stay live).

## Evidence

`axpby` is the arity-2 fold member; its semantics and laws live at [`linear_combination`](./linear_combination.md) (combinator) and `book/src/L1/axpby.md` (firm L1 endpoint, cycle-003). Anchors retained here are `axpby`'s **unique** L0 surface — the `AXPBY` free-function + complex-overload + promotion sites + the MFEM fused-pass — which the combinator's generic free-function-surface anchors (`vector.hpp:305-316`) do not pinpoint at the arity-2 resolution:

- `palace/linalg/vector.cpp:726-730` — real-real `AXPBY` (MFEM single aligned `add(α, x, β, y, y)` fused pass).
- `palace/linalg/vector.cpp:732-737` — complex-complex `ComplexVector::AXPBY` (the complex arity-2 overload).
- `palace/linalg/vector.cpp:739-743` — real-α-real-β-on-complex-vector promotion site (scalar-promotion sub-axis).
- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member decl.
- `palace/linalg/vector.hpp:309-311` — free-function template `AXPBY` decl.

Combinator + firm-L1 anchors (semantics + laws home): `book/src/L3/linear_combination.md` (firm cycle-050; §"Arity specializations" `:50-61`, §"Downward to L2" `:107-113`), `book/src/L1/axpby.md` (cycle-003 firm), `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; the lowering's substantive content + pinned summation order), `scaffolding/decisions/axpby-as-primitive.md` (cycle-003 fused-primitive choice), `book/src/concepts/scalar-promotion.md` (typing rule).
