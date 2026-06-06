---
layer: L3
operator: scal
rank: firm
edges:
  depends-on:
    - L2/linear_combination
  reference:
    - L3/linear_combination
    - L1/scal
    - L2-L1/linear-combination-fold-specialization
variant_axes:
  - element-type (real / complex)
  - scalar-promotion (real-α-against-complex-x via concepts/scalar-promotion)
---

# scal

`scal` is the **arity-1 specialization of [`linear_combination`](./linear_combination.md)**: `scal(α, x) = linear_combination [(α, x)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms `scal` / `axpy` / `axpby` / `axpbypcz` speak **through** the combinator, not as re-derived base forms — `scal` is the combinator at term-list length 1 (one term, no sum). This chapter is the arity-1 **readout label** for the bounded-arity L0 call shape; its semantics, signature, algebraic laws, iteration-rotation profile, and L3-vs-L1 framing are the combinator's, read at length 1 — see [`linear_combination`](./linear_combination.md) (the §"Arity specializations" notes and the §"Downward to L2" combinator-identity note are the home). What this stub retains below is `scal`'s **unique L0 surface** (the receiver-mutating member-method idiom + `Normalize`, distinct from the free-function `AXPY`/`AXPBY`/`AXPBYPCZ` surface the combinator cites) and its **one collapsed variant-axis row**.

## Specialization

- **Arity**: 1 (`scal(α, x) = linear_combination [(α, x)]`).
- **L0 call shape**: the receiver-mutating `mfem::Vector::operator*=(double)` (real) / `ComplexVector::operator*=(std::complex<double>)` (complex) member-method idiom — distinct from the free-function `AXPY`/`AXPBY`/`AXPBYPCZ` surface the combinator's L0 anchors cover. This is the only family member whose L0 surface is a receiver-mutating `*=`, not a free function.
- **Lowering**: routes through the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at length 1, then the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme. **No load-bearing summation-order residue**: at length 1 there is one term and one rounding per element — value- and bit-exact, no sum, no arity dispatch. (Contrast `axpy`/`axpby`/`axpbypcz`, whose multi-term sums pin a summation order.)
- **Constant-folding**: `scal` has **no** L0 constant-folding branch on the value of `α` (unlike `axpy`'s `α == 1.0` fast-path). The `s.imag() == 0.0` branch in `ComplexVector::operator*=` (`palace/linalg/vector.cpp:206-211`) is a complex-scalar-*shape* branch (the scalar-promotion sub-axis), **not** a scalar-*value* branch — this distinction is load-bearing for classifying the branch as transparent (a shape specialisation that disappears at L1), not a value specialisation.

The downward edge, the seven combinator laws read at length 1 (`scal`'s nine module-axioms are the length-1 reading; `L1/scal.md` §Algebraic laws is the firm endpoint), the no-sequential-obstruction profile, and the L3-vs-L1 documentary-framing distinction are all the combinator's — deferred there, not restated here.

## Variant axes

The two variant axes are the combinator's element-type axis read at arity 1 (inherited unchanged from L1; both absorbed at construction, neither in the positional signature):

1. **element-type** (`real` | `complex`) — separate L0 overloads (`mfem::Vector::operator*=(double)` real; `ComplexVector::operator*=(std::complex<double>)` complex, `palace/linalg/vector.cpp:203-227`) collapse to one element-type-parameterised operator at L1/L3.
2. **scalar-promotion** (sub-axis on the complex element-type; [`scalar-promotion`](../concepts/scalar-promotion.md)) — real `α` against complex `x` via the internal `s.imag() == 0.0` branch at `vector.cpp:206-211`; value-based (not overload-based) promotion under the `real ⊑ complex` lattice.

## Status

`firm` — `scal` is the arity-1 specialization of the firm L3 combinator [`linear_combination`](./linear_combination.md); its signature, laws, and lowering are the combinator's read at length 1 (firm L1 endpoint `book/src/L1/scal.md`, cycle-004). The L0 surface retained here is self-verified on-disk this dispatch (`vector.hpp:98-99` `operator*=` decl; `vector.cpp:203-227` def incl. the `:207-211` shape branch; `vector.hpp:262-270` `Normalize`). Reduced to a specialization-stub cycle-052 D2 (the reduce-to-stub completion of the cycle-051 re-expression; semantics deferred to the combinator, duplicated body deleted; file KEPT so inbound links stay live).

## Evidence

`scal` is the arity-1 fold member; its semantics and laws live at [`linear_combination`](./linear_combination.md) (combinator) and `book/src/L1/scal.md` (firm L1 endpoint, cycle-004). Anchors retained here are `scal`'s **unique** L0 surface — the receiver-mutating `*=` member-method idiom + `Normalize` + the consumer call sites — which the combinator's free-function-surface anchors (`vector.cpp:702-758`, `vector.hpp:305-316`) do NOT cover:

- `palace/linalg/vector.hpp:98-99` — `ComplexVector::operator*=(std::complex<double> s)` declaration (the arity-1 receiver-mutating L0 surface).
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition; lines 206-211 are the `s.imag() == 0.0` complex-scalar-shape branch (`si = s.imag()` read at 206, the `if (si == 0.0)` body at 207-211; scalar-promotion sub-axis).
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template (fused `nrm2 + scal`; the `Normalize(x) = scal(1/nrm2(x), x)` consumer).
- `palace/linalg/iterative.cpp:632, 811` — GMRES Arnoldi basis-normalisation consumer (`w *= 1/Hj[j+1]`).
- `palace/linalg/operator.cpp:661, 673` — `Normalize` call sites.
- `palace/linalg/nleps.cpp:486-491` — eigenvector normalisation call sites.

Combinator + firm-L1 anchors (semantics + laws home): `book/src/L3/linear_combination.md` (firm cycle-050; §"Arity specializations" `:50-61`, §"Downward to L2" `:107-113`), `book/src/L1/scal.md` (cycle-004 firm), `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; the lowering's substantive content), `book/src/concepts/scal.md` + `book/src/concepts/scalar-promotion.md` (cross-cutting prose + typing rule).
