---
layer: L3
operator: axpbypcz
firmness: firm
lowers_to:
  - book/src/L2/linear_combination.md (the arity-3 specialization of the firm L3/L2 `linear_combination` fold; `axpbypcz(α,x,β,y,γ,z) = linear_combination [(α,x),(β,y),(γ,z)]`; lowers via the combinator's §"Downward to L2" identity-in-form edge, then the substantive arity-dispatch is the L2>L1 `linear-combination-fold-specialization` theme) → book/src/L1/axpbypcz.md (transitive L3>L1 identity in-line, the fold-specialization picking the `AXPBYPCZ` L0 leaf incl. the γ==0 arity-collapse)
lifts_from:
  - book/src/L3/linear_combination.md (the family combinator this leaf is the arity-3 specialization of — `axpbypcz` speaks through `linear_combination`, not as a re-derived base form, per the 2026-06-01 vocabulary-shift redirect; no L4 entry — the fold is a pure value-producing reduction, not a calculus combinator)
variant_axes:
  - element-type (real | complex)
  - scalar-promotion (sub-axis on complex element-type)
---

# axpbypcz

`axpbypcz` is the **arity-3 specialization of [`linear_combination`](./linear_combination.md)**: `axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z = linear_combination [(α, x), (β, y), (γ, z)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms `scal` / `axpy` / `axpby` / `axpbypcz` speak **through** the combinator, not as re-derived base forms — `axpbypcz` is the combinator at term-list length 3 (the top of Palace's bounded-arity surface; subsuming [`axpby`](./axpby.md) at γ=0 and [`axpy`](./axpy.md) at β=1, γ=0). This chapter is the arity-3 **readout label** for the bounded-arity L0 call shape (`AXPBYPCZ`); its semantics, signature, algebraic laws, iteration-rotation profile, and L3-vs-L1 framing are the combinator's, read at length 3 — see [`linear_combination`](./linear_combination.md) (the §"Arity specializations" notes and the §"Downward to L2" combinator-identity note are the home). What this stub retains below is `axpbypcz`'s **unique L0 surface** (the `AXPBYPCZ` free-function + complex-overload + promotion sites + the `γ==0` arity-collapse branch) and its **one collapsed variant-axis row**.

## Specialization

- **Arity**: 3 (`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`), the top of Palace's bounded-arity L0 surface (there is no `AXPBYPCZPDW`).
- **L0 call shape**: the free-function `AXPBYPCZ` symbol (real-real `AXPBYPCZ` + `ComplexVector::AXPBYPCZ`).
- **Lowering**: routes through the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at length 3, then the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme, which selects the `AXPBYPCZ` L0 leaf, handles the `γ==0` arity-collapse, and records the pinned summation order of each L0 branch. The substantive in-place mutation rotation, reached transitively, is the L1>L0 [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md).
- **Load-bearing `γ==0` arity-collapse + two-branch summation order**: the real-real `AXPBYPCZ` has exactly one specialisation branch — the `γ == 0` constant-fold to MFEM's `add(α, x, β, y, z)` (`palace/linalg/vector.cpp:745-758`, the `:749-751` fast-path), which is the **exact algebraic content of the combinator's zero-coefficient term-drop law** (`L3/linear_combination.md` law 5). The two L0 branches (the `γ==0` fast-path vs the `γ≠0` two-call split `AXPBY(α,x,γ,z); z.Add(β,y)`) use **different summation orders** — a load-bearing IEEE residue recorded by the L2>L1 fold-specialization theme (deferred there, not an L3 law). The `γ==0` branch is a transparent performance trick erased at L1; not an L3 variant axis.
- **Fused-primitive choice**: `axpbypcz` is the fused primitive, mirroring `axpby`'s cycle-003 fused-primitive verdict (`scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects"; inherited unchanged). `axpby` (γ=0) and `axpy` (β=1, γ=0) are subsumptions kept as siblings in the dep-map, not dependencies.

The downward edge, the seven combinator laws read at length 3 (`axpbypcz`'s twelve laws are the length-3 reading; `L1/axpbypcz.md` §Algebraic laws is the firm endpoint), the no-sequential-obstruction profile, and the L3-vs-L1 documentary-framing distinction are all the combinator's — deferred there, not restated here.

## Variant axes

The two variant axes are the combinator's element-type axis read at arity 3 (inherited unchanged from L1; both absorbed at construction, neither in the positional signature):

1. **element-type** (`real | complex`) — separate L0 overloads (real-real `AXPBYPCZ`; complex-complex `ComplexVector::AXPBYPCZ`, `palace/linalg/vector.cpp:760-765`) collapse to one element-type-parameterised operator at L1/L3.
2. **scalar-promotion** (sub-axis on the complex element-type; [`scalar-promotion`](../concepts/scalar-promotion.md)) — real `(α, β, γ)` against complex `x, y, z` promoted to complex with zero imaginary part, all-or-none across the scalar triple (`palace/linalg/vector.cpp:767-772`); typing-rule property, not an operator variant.

The `γ==0` real-real branch is an internal L0 control-flow specialisation (transparent performance trick), **not** an L3 variant axis (see §Specialization).

## Status

`firm` — `axpbypcz` is the arity-3 specialization of the firm L3 combinator [`linear_combination`](./linear_combination.md); its signature, laws, and lowering are the combinator's read at length 3 (firm L1 endpoint `book/src/L1/axpbypcz.md`, cycle-003). The L0 surface retained here is self-verified on-disk this dispatch (`vector.cpp:745-758` real-real incl. the `γ==0` branch at `:749-751`, `:760-765` complex-complex, `:767-772` promotion; `vector.hpp:133-136`, `:313-316`). The fused-primitive choice (`scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects", cycle-003) is inherited unchanged. Reduced to a specialization-stub cycle-052 D2 (the reduce-to-stub completion of the cycle-051 re-expression; semantics deferred to the combinator, duplicated body deleted; file KEPT so inbound links — incl. `L2/axpbypcz.md` → `../L3/axpbypcz.md` — stay live).

## Evidence

`axpbypcz` is the arity-3 fold member; its semantics and laws live at [`linear_combination`](./linear_combination.md) (combinator) and `book/src/L1/axpbypcz.md` (firm L1 endpoint, cycle-003). Anchors retained here are `axpbypcz`'s **unique** L0 surface — the `AXPBYPCZ` free-function + complex-overload + promotion sites + the `γ==0` arity-collapse branch — which the combinator's generic free-function-surface anchors (`vector.hpp:305-316`) do not pinpoint at the arity-3 resolution:

- `palace/linalg/vector.cpp:745-758` — real-real `AXPBYPCZ` including the `γ == 0` branch (`:749-751` `add(α, x, β, y, z)` fast-path — the exact algebraic content of the combinator's zero-coefficient term-drop law 5).
- `palace/linalg/vector.cpp:760-765` — complex-complex `ComplexVector::AXPBYPCZ` (the complex arity-3 overload).
- `palace/linalg/vector.cpp:767-772` — real-α-real-β-real-γ-on-complex-vector promotion site (scalar-promotion sub-axis).
- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl.
- `palace/linalg/vector.hpp:313-316` — free-function template `AXPBYPCZ` decl.

Combinator + firm-L1 anchors (semantics + laws home): `book/src/L3/linear_combination.md` (firm cycle-050; §"Arity specializations" `:50-61`, §"Downward to L2" `:107-113`, the zero-coefficient term-drop law 5 the `γ==0` branch realizes), `book/src/L1/axpbypcz.md` (cycle-003 firm), `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; the lowering's substantive content + the two-branch pinned summation order), `scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects" (cycle-003 fused-primitive choice), `book/src/concepts/scalar-promotion.md` (typing rule).
