---
layer: L3
operator: scal
firmness: firm
lowers_to:
  - book/src/L2/linear_combination.md (the arity-1 specialization of the firm L3/L2 `linear_combination` fold; `scal(α,x) = linear_combination [(α,x)]`; lowers via the combinator's §"Downward to L2" identity-in-form edge, then the substantive arity-dispatch is the L2>L1 `linear-combination-fold-specialization` theme) → book/src/L1/scal.md (transitive L3>L1 identity in-line; no `L3-L1/` directory)
lifts_from:
  - book/src/L3/linear_combination.md (the family combinator this leaf is the arity-1 specialization of — `scal` speaks through `linear_combination`, not as a re-derived base form, per the 2026-06-01 vocabulary-shift redirect)
variant_axes:
  - element-type (real / complex)
  - scalar-promotion (real-α-against-complex-x via concepts/scalar-promotion)
---

# scal

Vector-scalar multiplication as a whole-tensor field operation at L3 — the **arity-1 specialization of the [`linear_combination`](./linear_combination.md) fold**: `scal(α, x) = linear_combination [(α, x)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms `scal` / `axpy` / `axpby` / `axpbypcz` speak **through** the combinator, not as re-derived base forms — `scal` is the combinator at term-list length 1. This chapter is the arity-1 readout label for the bounded-arity L0 call shape (`operator*=`); its algebra is the fold's law set read at length 1, and its lowering routes through the combinator's §"Downward to L2" identity edge + the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `scal` at L3 is the whole-tensor form of vector-scalar multiplication — a single field operation parameterised by a scalar `α` and acting pointwise over the length axis. The operator carries **no iteration view at L3** (it is a leaf primitive, not a step body) and **no sequential obstruction** (every element is independent of every other element under the per-element scalar multiplication).

The relationship to the lower layer is the **combinator route**: `scal` is the arity-1 specialization of [`linear_combination`](./linear_combination.md), so its downward edge is the combinator's downward edge read at length 1. The L3 fold lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the combinator body (`L3/linear_combination.md:107-113` §"Downward to L2"); the substantive rotation — which L0 leaf each list-length pins, and its summation order — is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme. At length 1 there is **no sum and no arity dispatch** (one term computes one scaled pass, one rounding per element — value- and bit-exact), so `scal`'s lowering is the degenerate single-term reading of the fold's downward edge. The framing across layers differs only documentarily: L1 frames `scal` as the *mutation-rotation* image of the L0 receiver-mutating `mfem::Vector::operator*=` / `ComplexVector::operator*=` member-method idiom; L2/L3 frame it as the arity-1 fold member.

This L3 entry is the layer-coherence anchor: a reader at L3 finds `scal` here, in L3 vocabulary, as the arity-1 fold member, without re-deriving the base form. It was backfilled cycle-011 (wave-1 BLAS-1 cohort, per the cross-layer-cross-cutter audit `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` HIGH CONFIDENCE recommendation) and re-expressed through the combinator cycle-051 D1 (the propagate half of the cycle-049 replace-and-propagate map). The L3 index (`book/src/L3/index.md:11-14`) advertises the BLAS-1 cohort as whole-tensor field operations.

A cross-cutting prose treatment lives at [`concepts/scal`](../concepts/scal.md) — covering BLAS background (BLAS-1 `dscal` / `zscal`) and call-site role (basis normalisation, search-direction rescaling). The scalar-promotion sub-axis (real `α` against complex `x`) is covered at [`concepts/scalar-promotion`](../concepts/scalar-promotion.md). The L3 entry here is the firm operator definition at the iteration-rotation layer; the concept pages are the narrative and the typing rule.

## Signature

```text
scal :: Scalar -> Tensor[N] -> Tensor[N]
scal α x = α·x
```

Shape contract (bunsen-style, named axes; positional values, no monadic effect, no destination buffer):

- **`α`** — scalar (`real` or `complex`, matching the tensor element type per the element-type variant axis; or promoted from `real` to `complex` against complex `x` per the scalar-promotion sub-axis).
- **`x`** — `Tensor[N]` — the input tensor with a single length axis `N`. Read-only at L3 (the L3 form is pure; the L0 in-place mutation is reintroduced only at the L1>L0 lowering).
- **result** — `Tensor[N]` — same axis `N` as `x`. Every output element equals `α` times the corresponding input element.

The L3 signature is **identical to the L1 signature** modulo notation; the rotation is identity-in-form. No L4 wrapper machinery is needed at L3: `scal` is a leaf field operation, not a step body, and the L4 monadic / typed-record / readonly-typing apparatus (which serves wrapper-bearing operators like `krylov-step`) does not apply to leaf primitives. The L4 strawman (`book/src/design/l4_calculus.md`) does not give `scal` a dedicated L4 entry — leaf primitives are referenced at L4 inside L4 operator bodies (e.g., the `krylov_update` composition inside `book/src/L4/krylov-step.md:59`'s body); they do not get their own L4 typed-wrapper anchor (per the cross-layer-cross-cutter audit's "L4 candidate (CONFIRMED-NOT-NEEDED)" verdict for the BLAS-1 cohort).

## Semantics

`scal` at L3 is a single whole-tensor field operation: a value-threaded transformation `(α, x) -> y` where `y[i] = α · x[i]` for every element index `i ∈ [0, N)`. The operator is **element-local** (every output element depends on exactly one input element and the shared scalar `α`), **reduction-free** (no cross-element communication), and **rank-local** (no MPI collective at any layer; ranks own disjoint slices of `N` and apply the scalar multiplication independently).

At L3 the operator carries **no iteration view** — it is not a step body; the iteration-rotation layer composes whole-tensor primitives like `scal` into step bodies (e.g., the `krylov_update` sub-composition inside `book/src/L3/krylov-step.md`'s body uses `scal` for basis normalisation and search-direction rescaling). The whole-tensor field-operation framing is what the L3 index (`book/src/L3/index.md:13`) calls a "field operation" — the L3 vocabulary's primitive shape, with no element-loop exposed.

The operator is **pure at L3**: the prior `x` and the result are distinct values; the L0 source overwrites the in-place destination buffer via the L1>L0 lowering ([`L1-L0/`](../L1-L0/index.md) — no firm `scal-mutation-rotation` theme yet exists; the L1 entry sketches the lowering content in §"L1 vs L0 distinction" and §Evidence). At L3 the relationship is purely algebraic.

The body has **no structural sub-composition** — `scal` is a leaf primitive, so the L3 form does not decompose into other L3 primitives. The five primitive groups that a wrapper-bearing operator like `krylov-step` has (operator-apply, optional auxiliary, iterate-and-scalar update, output readout, counter increment) have no analog here: `scal`'s body is one whole-tensor field operation.

Special algebraic cases — `α = 0` (zero-fill, discards `x`), `α = 1` (identity), `α = -1` (negation), `α⁻¹` (inverse for non-zero `α`) — are not separate operators at L3. They are algebraic identities recorded in the laws below, inherited from L1. The L0 source has no constant-folding branches on the value of `α` (the `s.imag() == 0.0` branch in `ComplexVector::operator*=` at `palace/linalg/vector.cpp:207-211` is a complex-scalar-*shape* specialisation, not a scalar-*value* specialisation, and disappears at L1 per the transparent-vs-load-bearing-tricks discipline).

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `scal`'s iteration view is **degenerate**: `scal` is a leaf primitive, not a step body, so the operator carries no iteration view of its own. It composes into step bodies (e.g., the GMRES Arnoldi basis-normalisation `w *= 1.0 / Hj[j + 1]` inside `book/src/L3/krylov-step.md`'s `krylov_update`) where the surrounding step kernel carries the iteration view; the `scal` call site itself is a single whole-tensor field operation per step. There is **no sequential obstruction** in `scal` — every element is independent of every other element under the per-element multiplication; the operator is embarrassingly parallel and fully GPU-friendly.

The relationship between `scal` and the surrounding step body is what the L3 form preserves: a step body like `krylov-step` at L3 uses `scal` as one of the L3-native whole-tensor primitives in its `krylov_update` sub-composition, and the step body's own iteration-rotation is at the granularity of the *step*, not at the granularity of the per-element multiplication inside `scal`. This is consistent with the L3 form's design: leaf field operations have no inner iteration view; iteration views appear only at the level of step bodies that compose multiple leaf operations.

## Algebraic laws

The nine laws that hold at L1 (per `book/src/L1/scal.md` §Algebraic laws) hold unchanged at L3. The rotation L3 → L1 is identity-in-form on the operator's body and signature, so the algebraic properties of vector-scalar multiplication (axioms of a module over the scalar field, plus field-commutativity inherited rule) transport without modification. Absences are deliberate and inherited.

1. **Identity in `α`**: `scal(1, x) = x`. The neutral element of scalar multiplication.
2. **Absorption in `α`**: `scal(0, x) = 0` (the zero vector of axis `N`), for any `x`.
3. **Absorption in `x`**: `scal(α, 0) = 0`, for any `α`.
4. **Composition (scalar fusion)**: `scal(α, scal(β, x)) = scal(α·β, x)`. Two successive scalings collapse to one with the scalar product. The action of scalars on vectors is multiplicative.
5. **Distributivity over scalar addition**: `scal(α + β, x) = scal(α, x) + scal(β, x)`, where `+` on the right is element-wise vector addition. Linearity in the scalar argument.
6. **Distributivity over vector addition**: `scal(α, x + y) = scal(α, x) + scal(α, y)`. Linearity in the vector argument.
7. **Negation**: `scal(-1, x) = -x`. (Special case of laws 1 + 5.)
8. **Inverse (for non-zero scalar)**: `scal(α⁻¹, scal(α, x)) = x` for `α ≠ 0`. (Special case of law 4 with `β = α⁻¹` and law 1.) This is the rule that makes `Normalize` invertible up to the recovered `α = 1/nrm2(x)`.
9. **Commutativity of scalars (field-inherited)**: `scal(α·β, x) = scal(β·α, x)`. Inherited from the underlying field (`ℝ` or `ℂ`).

Laws that explicitly **do not** hold:

- **Idempotence**: `scal(α, scal(α, x)) ≠ scal(α, x)` in general — the result is `scal(α², x)`, which equals `scal(α, x)` only when `α² = α`, i.e. `α ∈ {0, 1}` (or `α(α−1) = 0` more broadly).
- **Commutativity in argument positions**: `α` and `x` live in distinct types (scalar vs tensor). "Commutativity" is not well-typed for the operator's argument list.
- **Distributivity over vector products**: not applicable at L3 — there is no inner-vector multiplication in the L3 whole-tensor vocabulary (`dot` reduces to a scalar; there is no element-wise vector product). The closest applicable rule is law 6, distributivity over vector **addition**.
- **Bit-level equivalence under fusion**: `scal(α, scal(β, x))` (law 4 LHS) and `scal(α·β, x)` (law 4 RHS) are algebraically equal but may differ at the bit level in IEEE-754 because the two-pass form rounds twice (once per element-multiply) and the fused form rounds once. Transparent-trick consideration inherited from L1; not load-bearing in CLAUDE.md's sense for the algorithms Palace runs, but worth recording for solvers that depend on bit-determinism across fusion choices.
- **Step composition / outer-loop lift to a single tensor-field op**: not applicable — `scal` is a leaf primitive, not a step body. There is no outer loop folding `scal` calls and no trajectory of carries; the inapplicability is structural, not a non-law in the usual sense. Compare with `krylov-step` at L3 (`book/src/L3/krylov-step.md` §Algebraic laws "Outer-loop lift to a single tensor-field op"), which *does* have a step-body structure and explicitly catalogues the outer-loop sequential obstruction.

## Dependencies

**Same-layer (L3)**: none. `scal` is a leaf primitive at L3 just as it is at L1 — vector-scalar multiplication does not decompose into other L3 whole-tensor primitives. The body is a single field operation; the sub-operations (scalar multiplication and per-element application) are below the L3 layer's resolution.

**Cross-cutting concepts**:

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the implicit-coercion typing rule for real `α` against complex `x`. Internal promotion at L0 via the `s.imag() == 0.0` branch in `ComplexVector::operator*=`; collapsed at L1 / L3 into a single operator parameterised by the `real ⊑ complex` scalar lattice.
- [`scal` (concept)](../concepts/scal.md) — cross-cutting prose treatment; BLAS-1 background and call-site role (basis normalisation, search-direction rescaling).

**Sibling subsumption (not dependency)**:

- `scal(α, x) = axpby(α, x, 0, y) = axpby(0, y, α, x)` for any `y`, per `axpby` laws 2 and 3 at `book/src/L1/axpby.md`. The subsumption is inherited from L1; once the sibling `axpby` entry lands (wave-1 dispatch #2 — `book/src/L3/axpby.md`), it will also be a leaf whole-tensor primitive. `scal` stays in the L3 dep-map as a sibling, not a sub-operation of `axpby` (per the harvester decision at `scaffolding/decisions/axpby-as-primitive.md`).
- `Normalize(x) = scal(1 / nrm2(x), x)` paired with the returned norm. The free-function `linalg::Normalize` at `palace/linalg/vector.hpp:262-270` is a fused `nrm2 + scal` construct; at L3 it factors as the composition `scal(1/nrm2(x), x)` over the L3 `nrm2` and `scal` primitives. Once the sibling `nrm2` entry lands (wave-1 dispatch #3 — `book/src/L3/nrm2.md`), it will be linked here. Whether to harvest a fused `normalize` L3 primitive is an open question inherited from L1.

**Downstream consumers at L3** (cross-reference, not reverse-dependencies):

- GMRES Arnoldi basis-normalisation `w ← w / Hj[j+1]` inside the `krylov_update` sub-composition of [`krylov-step`](./krylov-step.md) — sourced from `palace/linalg/iterative.cpp:632, 811`.
- CG search-direction rescaling `p ← (β/β_prev) p` inside the `krylov_update` sub-composition of [`krylov-step`](./krylov-step.md) — sourced from `concepts/scal.md` and the CG slice corpus.
- Eigenvector normalisation in operator-side normalisation flows and nonlinear-EVP code — sourced from `palace/linalg/operator.cpp:661, 673` and `palace/linalg/nleps.cpp:486-491` via `Normalize`.

**Strawman reference**: `book/src/design/l4_calculus.md` is the conventions source for the L4 / L3 pseudo-language (Haskell-style `::` arrows for signatures, fenced as `text`). `scal` does not get its own L4 entry per the cross-layer-cross-cutter audit's "L4 candidate (CONFIRMED-NOT-NEEDED)" verdict — leaf primitives appear inside L4 operator bodies as let-bindings, not as first-class L4 vocabulary.

## Variant axes

The two variant axes are inherited unchanged from L1. Both are absorbed at construction time (the element-type axis through overload selection at L0; the scalar-promotion sub-axis through the internal `s.imag() == 0.0` branch); neither appears in the L3 positional signature.

1. **element-type** (`real` | `complex`). The L0 source has separate overloads (`mfem::Vector::operator*=(double)` from MFEM for real; `ComplexVector::operator*=(std::complex<double>)` at `palace/linalg/vector.cpp:203-227` for complex). At L1 / L3 these collapse to one operator parameterised by element type — the semantics are identical (per-element scalar multiplication in the appropriate field). At L3 the absorption is a documented invariant (no `readonly` typing in the L3 calculus).
2. **scalar-promotion** (sub-axis on the complex element-type). See [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `α` against complex `x` via the internal `s.imag() == 0.0` branch at `vector.cpp:207-211`. Value-based (not overload-based) promotion: the L0 caller passes `std::complex<double>` with zero imaginary part, and Palace recognises the special case to dispatch to two real `operator*=` calls. At L1 / L3 this is one operator with `α` typed through the `real ⊑ complex` scalar lattice.

No other variant axes — `scal` is unconditionally pure, element-local, reduction-free, and rank-local across all variants. Unlike `axpy` (which has the real-path `α == 1.0` constant-folding specialisation at L0) and like `axpby` (which has no constant-folding), `scal` has no L0 constant-folding branches on the value of `α`; the branch in `ComplexVector::operator*=` is a complex-scalar-shape branch (`imag == 0`), not a scalar-value branch.

The variant-axis count matches the L1 entry exactly (two axes; element-type with scalar-promotion as sub-axis). No new axes introduced by the L3 rendering; no axes merged or split.

## Status

`firm` — signature is canonical (matches BLAS-1 `dscal` / `zscal` and the Palace `operator*=` surface exactly; identical to the L1 form), evidence is direct from the L1 entry and the L3 vocabulary inventory, and the nine algebraic laws are standard scalar-vector-multiplication facts (axioms of a module over the scalar field, plus the field-commutativity inherited rule). The pattern is well-attested: the L1 firm-up landed cycle-004; the L3-native-by-signature classification is named explicitly in the firm L3>L2 body-identity theme (`book/src/L3-L2/krylov-step-body-identity.md:97`, cycle-009) and rendered in the firm L4>L3 typed-wrapper-dissolution theme's L3 let-chain (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:68`, cycle-008). This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** — the L3 form was previously referenced only inside the `krylov_update` sub-composition of `krylov-step`'s body; it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md, cycle-009 meta-phase).

## Lowers to

L3 `scal` lowers as the **arity-1 specialization of [`linear_combination`](./linear_combination.md)**. The combinator lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the fold body (`L3/linear_combination.md:107-113` §"Downward to L2"); read at term-list length 1 this is `scal(α, x) = linear_combination [(α, x)]`. The substantive rotation in the downward chain is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme (it reads the term-list length and selects the maximal fused L0 leaf — length 1 → `scal`'s `operator*=` — and records each lowered call's pinned summation order). At length 1 the summation order is degenerate (one term, one rounding per element — value- and bit-exact), so `scal`'s lowering carries no pinned-order residue. The transitive L3>L1 identity (the combinator's L3>L2 identity ∘ the L2>L1 fold-specialization's value-identity at length 1) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory. The L0 in-place mutation is reintroduced at the L1>L0 lowering (the L1 entry sketches the content in its §"L1 vs L0 distinction" and §Evidence).

## Lifts from

`scal` is the **arity-1 member of the [`linear_combination`](./linear_combination.md) fold** — it speaks through the combinator at L3 and above, not as a re-derived base form (the propagate half of the cycle-049 replace-and-propagate map, per the 2026-06-01 vocabulary-shift redirect). The combinator carries no L4 entry (it is a pure value-producing reduction over a term list, not a calculus combinator with monadic state-threading or a convergence predicate; `L3/linear_combination.md:152-154`); `scal` appears inside L4 operator bodies as a let-binding (the cohort audit's "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort). This L3 entry exists for layer-coherence — a reader at L3 finds `scal` defined as the arity-1 fold member without re-deriving the base form.

## Evidence

The L3 form is value-thread-isomorphic to the L1 form (per the cross-layer-cross-cutter audit and the firm L3>L2 / L4>L3 themes' explicit naming); all L0 evidence is transitive through L1. Direct citations relevant to this L3 entry:

- `book/src/L1/scal.md` (cycle-004 firm) — the L1 form this L3 entry value-thread-rewrites. Body shape, signature, semantics (element-local, reduction-free, rank-local), algebraic laws (nine that hold), variant axes (two: element-type, scalar-promotion sub-axis), and L0 evidence chain (`palace/linalg/vector.{hpp,cpp}`, `palace/linalg/iterative.cpp`, `palace/linalg/operator.cpp`, `palace/linalg/nleps.cpp`).
- `book/src/L3/index.md:11-14` — L3 vocabulary inventory naming "matvec, axpy, dot, nrm2" as field operations. `scal` is the standalone leaf of the BLAS-1 family the index advertises (the index lists three of the six BLAS-1 primitives by name; the others, including `scal`, are implied by the "etc." reading and by the firm L3>L2 theme's explicit naming).
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-009 firm) — the firm theme that explicitly names the seven L1 primitives (including `scal`) as L3-native by signature shape: "each operates on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)."
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:68` (cycle-008 firm) — the firm theme that renders `scal` in the L3 body let-chain inside the `krylov_update` sub-composition.
- `book/src/L3/krylov-step.md` (cycle-010 firm; wave-1 backfill precedent) — the first firm L3 operator, also an identity-in-form backfill enacting the same methodology invariant.
- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` (HIGH CONFIDENCE backfill recommendation) — the audit identifying `scal` as a member of the BLAS-1 bundle backfill, with rationale tied to the L3 vocabulary inventory gap and the methodology invariant.
- `book/src/concepts/scal.md` — pre-existing cross-cutting prose treatment; consistent with this L3 entry's framing.
- `book/src/concepts/scalar-promotion.md` — the typing rule for the scalar-promotion sub-axis (`vector.cpp:207-211` anchor).

**Transitive L0 evidence (inherited from L1 entry; not re-cited here)**:

- `palace/linalg/vector.hpp:98-99` — `ComplexVector::operator*=(std::complex<double> s)` declaration.
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition; lines 207-211 are the `s.imag() == 0.0` branch (scalar-promotion sub-axis).
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template (fused `nrm2 + scal`).
- `palace/linalg/iterative.cpp:632, 811` — GMRES Arnoldi basis-normalisation.
- `palace/linalg/operator.cpp:661, 673` — `Normalize` call sites.
- `palace/linalg/nleps.cpp:486-491` — eigenvector normalisation call sites.

## L3 vs L1 distinction

- **L1**: mutation-lifted pure functional update. `x_new = scal(α, x_old)`. Frames the operator as the pure-functional image of the L0 receiver-mutating `*=` member-method idiom; emphasises the *mutation rotation* against the source. The L1 entry's §"L1 vs L0 distinction" focuses on the destination-buffer drop and the real-imag-shape branch erasure.
- **L3**: whole-tensor field operation. `y = scal(α, x)`. Frames the operator as a leaf primitive in the iteration-rotation layer's whole-tensor vocabulary; emphasises element-locality, reduction-freedom, rank-locality, and the absence of an iteration view at the operator itself. The L3 form is **identical in body and signature to L1** — the framing differs, but no operational adjustment occurs.

The L3 → L1 rotation is identity-in-form on the body and signature; the surface adjustment is documentary (the framing rotates from "mutation rotation against L0 source" at L1 to "field operation in the iteration-rotation layer's vocabulary" at L3). Both framings are correct; they describe the same operator at adjacent layers. The methodology invariant **each layer is coherent within itself** is what compels the L3 entry to exist as its own anchor.
