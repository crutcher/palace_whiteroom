---
agent: lifter
invoked_at: 2026-06-01T223300Z
scope: L3>L2 leaf-chapter reduce-to-stub — L3 linear_combination-family leaves (scal/axpy/axpby/axpbypcz)
status: pending
integrated_at: 2026-06-02T010000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-052 D2 — applied clean (full-body replace reduce-to-stub for 4 L3 linear_combination leaves; frontmatter untouched, unique L0 anchors retained); no build-repair needed; refactor pass COMPLETE."
inputs:
  - book/src/L3/linear_combination.md (the firm L3 family combinator the four leaves speak through; the semantics home)
  - book/src/L3/scal.md (155 ln; reduce to arity-1 stub)
  - book/src/L3/axpy.md (149 ln; reduce to arity-2-coeff-1 stub)
  - book/src/L3/axpby.md (154 ln; reduce to arity-2 stub)
  - book/src/L3/axpbypcz.md (160 ln; reduce to arity-3 stub)
  - book/src/L2-L1/linear-combination-fold-specialization.md (the substantive L2>L1 fusion-selection theme; lowering home)
  - skills/deleted-slug-inbound-live-link-sweep/SKILL.md (zero-dangling verification gate)
---

# CYCLE: Re-anchor (reduce-to-stub) the L3 linear_combination-family leaves

## Summary

This dispatch (cycle-052 D2) reduces the four L3 `linear_combination`-family leaf chapters — `scal` (155 ln), `axpy` (149 ln), `axpby` (154 ln), `axpbypcz` (160 ln) — to thin **specialization-stubs** under the firm L3 family combinator [`linear_combination`](book/src/L3/linear_combination.md). The four were already re-expressed *through* the combinator at cycle-051 (the "arity-N specialization of `linear_combination`" framing is present in each opener, `lifts_from`, `Lowers to`, and `Dependencies`), so the re-expression vocabulary is in place; this pass completes the batch-15-ratified **reduce-to-stub** convention by DELETING the duplicated body (Semantics / Algebraic laws / Iteration-rotation marker / L3-vs-L1 distinction — all of which restate the combinator's content read at a fixed arity) and DEFERRING that content to `L3/linear_combination`'s in-line §"Downward to L2" combinator note. Each stub RETAINS (b) its UNIQUE L0 anchors (the `operator*=` member-method idiom + `Normalize` for `scal`; the per-arity complex-overload defs, free-function decls, and promotion sites the combinator's free-function-surface anchors do not cover) and (b) its ONE collapsed variant-axis row (element-type + the scalar-promotion sub-axis) plus the load-bearing fast-path / pinned-order notes that are arity-specific (the `axpy` `α==1.0` fast-path; the `axpby` no-constant-folding fact; the `axpbypcz` `γ==0` arity-collapse + two-call-split summation-order residue). `## Status: firm` is kept on all four. **No file is deleted** (reduce-to-stub KEEPS the files), so all inbound live links stay LIVE — the `deleted-slug-inbound-live-link-sweep` gate confirms **zero danglers** (see §Discipline notes). `book/src/L3/index.md` rows/narrative are untouched (D4 owns those).

## Proposed changes

### 1. `book/src/L3/scal.md` — reduce to arity-1 specialization-stub

```edit:book/src/L3/scal.md
[old]:
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

[new]:
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
```

### 2. `book/src/L3/axpy.md` — reduce to arity-2 (second-coeff-1) specialization-stub

```edit:book/src/L3/axpy.md
[old]:
# axpy

Whole-tensor vector-scalar fused update at L3: `axpy(α, x, y) = α·x + y` — the **arity-2 specialization of the [`linear_combination`](./linear_combination.md) fold** with the second coefficient fixed to 1: `axpy(α, x, y) = linear_combination [(α, x), (1, y)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms speak **through** the combinator, not as re-derived base forms — `axpy` is the combinator at term-list length 2 with the trailing coefficient pinned to 1. This chapter is the arity-2 readout label for the bounded-arity L0 call shape (`AXPY`); its algebra is the fold's law set read at that fixed length, and its lowering routes through the combinator's §"Downward to L2" identity edge + the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, no element loops, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `axpy` at L3 is the whole-tensor linear-update primitive consumed by `krylov-step`'s iterate-stratum update (per [`krylov-step`](./krylov-step.md) §Semantics, line 82 of the cycle-010 firm entry: `krylov_update` at L3 composes whole-tensor primitives including `axpy`).

The L3 form is **value-thread-isomorphic to the L1 form**: each L1 BLAS-1 primitive's signature shape is whole-tensor in / whole-tensor out with no element loop exposed (the L1 entries are written against `Tensor[N]` arguments, not against per-element indexing). The L3 layer's vocabulary requirement — whole-tensor primitives, no element loops — is satisfied by L1's signature shape directly. The relationship to the lower layer is therefore the identity rotation on the primitive itself; the per-element semantics that L1 uses to describe the operator (`result[i] = α·x[i] + y[i]`) is the **referent**, not the L1 form's surface — the L1 surface is the whole-tensor signature `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`, which is already L3-native.

This L3 entry is the layer-coherence anchor for the cycle-011 BLAS-1 cohort backfill — a reader navigating L3 (which the L3 index advertises as containing "axpy ... as field operations" at `book/src/L3/index.md:13`) can find `axpy` here, in L3 vocabulary, without having to reach down to L1 to recover the signature. The backfill enacts the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). This entry is one of three sibling firmings in the cycle-011 wave-1 BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`); the cohort precedent is `book/src/L3/krylov-step.md` (cycle-010 wave-1).

A cross-cutting prose treatment lives at [`concepts/axpy`](../concepts/axpy.md) — covering BLAS background, fusions (`α = 1`, `α = -1`), and roll-up usage across slices. The concept page is the narrative; this L3 entry is the firm operator definition at L3.

## Signature

```text
axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]
```

Positional value-threading; no monadic effect (L3 has no `Solve` monad), no record-typing:

- `α : Scalar` — scalar coefficient (real or complex, matching the vector element type).
- `x : Tensor[N]` — input tensor; whole-tensor read.
- `y : Tensor[N]` — input tensor (the *prior* value); whole-tensor read.
- result `: Tensor[N]` — output tensor; whole-tensor write (fresh value, no aliasing with `x` or `y` at L3).

Shape contract (bunsen-style, named axis):

- `N` — length axis; shared across `x`, `y`, and the result.
- element type — uniform across `x`, `y`; uniform `Scalar` matches the vector element type modulo scalar promotion (see Variant axes).

`x` and `y` must share the same length axis `N` and the same element type (both real or both complex). When the vectors are complex, real `α` is promoted to complex per the [`scalar-promotion`](../concepts/scalar-promotion.md) typing rule. The L3 form inherits the `real ⊑ complex` scalar lattice from L1 — the promotion is a typing-rule property, not an operator variant; the L3 signature is `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` where `Scalar` is the lattice-resolved scalar type.

The L3 calculus has no record-typing and no `readonly` annotation; the signature is positional. The discipline that `α` flows in only (never out) is structural (the return position has only one slot, of type `Tensor[N]`, not a scalar).

## Semantics

`axpy` at L3 is a single whole-tensor linear update: `axpy(α, x, y)` produces the tensor `α·x + y`, where `α·x` is the whole-tensor scaling (a single L3-native operation, see [`scal`](./scal.md) when firm) and the `+` is the whole-tensor pointwise sum (an L3-native operation by signature shape — `Tensor[N] -> Tensor[N] -> Tensor[N]`).

The operator is **pure at L3**: the prior `y` and the new value (returned positionally) are distinct values; no destination buffer appears in the signature. The L3 form has no aliasing — both inputs and the output are conceptually distinct tensors. In-place mutation (the L0 source overwrites the destination `y`) reappears in the L1>L0 lowering chain via [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (which covers `axpy` as the β=1 specialisation of `axpby`); the L3 form is uniformly out-of-place.

**The operator is reduction-free and element-local at the referent semantics**: the per-element relation `result[i] = α·x[i] + y[i]` holds at every position independently, with no cross-element communication. This is a property of the referent, observable when the L3 form is lowered to L1 (where the per-element relation is the L1 entry's §Semantics line). At the L3 layer itself, the operator is rendered as a whole-tensor function `Tensor[N] -> Tensor[N]` with no element-index visible — the element-locality is a consequence of the operator's identity, not of its L3 surface.

**The operator carries no sequential obstruction**: `axpy` is a leaf primitive at L3 (and at L1); the L3 iteration-rotation marker (per [`sequential-obstruction`](../concepts/sequential-obstruction.md)) does not apply to it — there is no fold over `axpy`'s output to invoke. `axpy` is a *primitive* that other L3 compositions (notably `krylov-step`) invoke; the sequential obstruction lives at the consuming composition (the outer `iterate_while_L3` loop folding `krylov-step`), not at `axpy` itself.

Special algebraic cases — `α = 0` (identity in the second argument), `α = 1` (vector add), `α = -1` (vector subtract), `x = 0` (identity in the first argument) — are not separate operators at L3. They are algebraic identities, recorded in §Algebraic laws below. L0 specialisations (Palace's `AXPY(double, Vector, Vector)` branches on `α == 1.0`) are transparent performance tricks that have already been erased at L1; they do not reappear at L3.

### Iteration-rotation marker

L3 is the iteration-rotation layer, but `axpy` is a **leaf primitive** with no iteration view of its own — it is a single whole-tensor operation, not a fold over a trajectory. The iteration view applies to compositions of `axpy` (notably `krylov-step`'s iterate-stratum update; per [`krylov-step`](./krylov-step.md) Form A line `let K' = krylov_update K_aux op w`, which composes `axpy` / `axpby` / `axpbypcz`). At the leaf `axpy` itself, there is no iteration carry, no successor relation, no fold. The L3 layer-coherence reason for this entry is **vocabulary inventory**, not iteration-view content.

## Algebraic laws

Inherited verbatim from L1 (per the identity-in-form rotation). The laws below hold at L3 because they hold at L1 and the L3 form is value-thread-isomorphic to the L1 form (the laws are statements about the operator's value, not about its surface; the surface rewrite is a no-op on the value).

1. **Identity in `α`**: `axpy(0, x, y) = y` for any `x`.
2. **Identity in `x`**: `axpy(α, 0, y) = y` for any `α`, where `0` is the zero tensor of axis `N`.
3. **Left distribution over tensor addition in `y`**: `axpy(α, x, y₁ + y₂) = axpy(α, x, y₁) + y₂`. Both sides equal `α·x + y₁ + y₂`.
4. **Scalar linearity in α (additive collapse)**: `axpy(α, x, axpy(β, x, y)) = axpy(α + β, x, y)` — two successive axpy's against the same `x` collapse to one with summed scalar.
5. **Scalar absorption**: `axpy(α·β, x, y) = axpy(α, β·x, y)` — the scalar absorbs into either side.
6. **Vector linearity in x (additive expansion)**: `axpy(α, x₁ + x₂, y) = axpy(α, x₁, axpy(α, x₂, y))`. This law underwrites the consuming-composition (e.g., `krylov-step`'s iterate-stratum update inside `krylov_update`) unfolding of GMRES basis-correction sums into axpy chains.

Laws that explicitly **do not** hold (inherited from L1):

- **Commutativity in the tensor arguments**: `axpy(α, x, y) ≠ axpy(α, y, x)`. The second argument `x` enters scaled by `α`; the third argument `y` does not. Swapping them changes the value.
- **Associativity as a binary algebra**: `axpy` is ternary; associativity is not well-typed.
- **Floating-point associativity in the summation**: `α·x + y` in IEEE-754 may differ at the bit level from any reordering when the magnitudes of `α·x` and `y` differ enough to lose precision. The L3 form is order-agnostic algebraically; bit-identical reproduction of L0 output requires matching the L0 evaluation order (pinned by MFEM's kernel). Inherited from L1; recorded here, not erased.

The algebraic-law set at L3 is **identical** to the L1 algebraic-law set. This is structural: the rotation is identity-in-form on the primitive's signature; laws about the primitive's value are unchanged across the rotation. Stating the laws at L3 is not a duplication-explosion concern under the methodology — it is the layer-coherence invariant; an L3 reader can verify the laws against the L3 signature without reaching down to L1.

## Dependencies

**Same-layer (L3)**: no other L3 operators (axpy is a leaf primitive). The composition surfaces that consume `axpy` at L3 are the iterate-stratum update inside `krylov-step`'s `krylov_update` (per [`krylov-step`](./krylov-step.md) §Semantics).

**Cross-cutting concepts** (consumed unchanged across the chain):

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the `real ⊑ complex` typing-rule for scalar promotion on the complex element-type. The L3 form inherits the rule from L1 verbatim; no L3-specific semantics.
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — the methodology concept underwriting the L3-native-by-signature-shape claim for the BLAS-1 primitives.
- [`axpy`](../concepts/axpy.md) — the cross-cutting prose narrative (BLAS background, common fusions, roll-up usage). The L3 entry here is the firm operator definition; the concept page is the narrative.

**Strawman reference**: `book/src/design/l4_calculus.md` §3.7's conventions are not directly invoked here because `axpy` is a leaf primitive, not a calculus combinator. The L3 signature is a plain Haskell-style `::` arrow form.

No L4 monadic vocabulary appears in the L3 signature (no `Solve`, no `modify`, no `do`-block) — neither `axpy` nor the `linear_combination` fold it specializes is a calculus combinator at L4 (the cohort audit verdict for the BLAS-1 cohort at L4 is **CONFIRMED-NOT-NEEDED**; `L3/linear_combination.md:152-154`). The downward rotation passes through the firm L2 [`linear_combination`](../L2/linear_combination.md) via the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at term-list length 2 (second coeff 1) — `axpy` is the arity-2 fold member. The substantive arity-dispatch (length → maximal fused L0 leaf, here the `AXPY` symbol) + the pinned summation order live in the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme, NOT in a per-leaf theme.

## Variant axes

Inherited unchanged from the L1 entry at two:

1. **element-type** (`real | complex`) — the L1 entry distinguishes real-vector and complex-vector overloads; at L3 these collapse to one operator parameterised by element type. Semantics are identical across element types; the per-element kernel referent is `α·x[i] + y[i]` in the appropriate field.
2. **scalar-promotion** (sub-axis on the complex element-type) — see [`scalar-promotion`](../concepts/scalar-promotion.md). Real `α` against complex `x, y` is promoted to complex with zero imaginary part. The promotion is a typing-rule property, not an operator variant.

The variant-axis profile at L3 matches L1 exactly. No new axes introduced by the L3 rendering; no axes merged or split.

## Status

`firm` — whole-tensor positional signature is canonical at L3; algebraic laws are the six that hold at L1 (inherited verbatim under the identity-in-form rotation); non-laws are catalogued explicitly; variant-axis profile is closed at two. The pattern is well-attested via L1 (cycle-002 firm) and via the L3-L2 body-identity theme's §"Applicability conditions" point 3 (`book/src/L3-L2/krylov-step-body-identity.md:97`), which explicitly names `axpy` as L3-native by signature shape. This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** — the L3 form was previously only referenced from `krylov-step`'s body let-chain at L3; it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). One of three sibling firmings in the BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`).

## Lowers to

L3 `axpy` lowers as the **arity-2 specialization of [`linear_combination`](./linear_combination.md)** (second coefficient fixed to 1: `axpy(α, x, y) = linear_combination [(α, x), (1, y)]`). The combinator lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the fold body (`L3/linear_combination.md:107-113` §"Downward to L2"). The substantive rotation in the downward chain is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme: it reads the term-list length (here 2 with the trailing coeff 1) and selects the maximal fused L0 leaf — the `AXPY` symbol, which carries the `α == 1.0` fast-path (`palace/linalg/vector.cpp:702-712`) — and records its pinned summation order. All arity dispatch and summation-order residue are the fold-parent's, not this leaf's.

The **transitive** L3>L1 identity (the combinator's L3>L2 identity ∘ the L2>L1 fold-specialization's value-identity at this list length) is annotated in-line per the cycle-012 non-adjacent-identity convention (lowering directories are per-adjacent-edge only); no `book/src/L3-L1/` directory is created. The substantive in-place mutation rotation, reached transitively, is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (which covers `axpy` as the β=1 specialisation of `axpby`).

## Lifts from

No L4 entry exists for `axpy` (the cohort audit verdict is **CONFIRMED-NOT-NEEDED** for the BLAS-1 cohort at L4 — leaf primitives don't get L4 rows). `axpy` appears inside L4 entries as a let-binding inside `krylov-step`'s body (per `book/src/L4/krylov-step.md` §Semantics), but is not a first-class L4 calculus combinator and carries no monadic effect, no state-stratification typing, no novel calculus content at L4.

## Evidence

All L0 evidence is inherited via L1 (`book/src/L1/axpy.md` §Evidence). Direct citations relevant to this L3 entry:

- `book/src/L3/linear_combination.md` (cycle-050 firm) + `book/src/L2/linear_combination.md` (inverted-to-entry cycle-049 D1) — the family combinator this leaf is the arity-2 specialization of; §"Arity specializations" (`L3/linear_combination.md:50-61`) names `axpy = linear_combination [(α,x),(1,y)]`, §"Downward to L2" (`:107-113`) is the identity-in-form edge this leaf's lowering reads at length 2.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; cycle-049 D1(c) KEEP verdict) — the substantive L2>L1 fusion-selection theme that picks the `AXPY` L0 leaf at this list-length and records its pinned summation order (the lowering's substantive content, deferred here, not in a per-leaf theme).
- `book/src/L1/axpy.md` (cycle-002 firm) — the L1 leaf the fold-specialization recovers at this arity (the L1>L0 one-to-one `AXPY` symbol shape). Body shape, semantics, six algebraic laws, two non-laws, variant-axis profile.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm) — explicitly names `axpy` as one of seven L1 primitives that is "L3-native because its signature has no per-element loop visible". The structural justification for the identity-in-form rotation.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:67` (firm) — renders `axpy` in the L3 body let-chain identically to L1. The empirical evidence that the L3 form of `axpy` already exists in the artifact (as the RHS of the upstream theme's L3 form).
- `book/src/L3/index.md:13` — L3 vocabulary inventory naming `axpy` as a field operation. The advertised L3 vocabulary that this entry backfills.
- `book/src/L3/krylov-step.md` (cycle-010 firm; the precedent layer-coherence backfill) — the template structure this entry follows.
- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` — the cycle-010 audit identifying this cohort as HIGH CONFIDENCE backfill (lines 47-51, 100-132).
- `concepts/scalar-promotion.md` (cycle-005 firm; cycle-006 retroactive-thinned the L1 entry to point here) — the typing-rule for the real-on-complex-vector case at L3 / L1.

L0 source ranges (inherited via L1; not consumed as new evidence at L3):

- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` and `Add`/`Subtract` aliases.
- `palace/linalg/vector.hpp:305-307` — free-function template `AXPY`.
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition.
- `palace/linalg/vector.cpp:702-712` — free-function `AXPY(double, Vector, Vector)` with `α == 1.0` fast-path.
- `palace/linalg/vector.cpp:715-718` — real-α-on-complex-vector promotion site.

## L3 vs L1 distinction

- **L1**: whole-tensor pure-functional update `axpy :: (α, x, y) -> α·x + y`. Mutation-lifted from the L0 source's in-place form; aliasing-free; reduction-free; element-local at the referent semantics. The closest pure-functional layer to the source.
- **L3**: whole-tensor pure-functional update `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`. The iteration-rotation layer's rendering, value-thread-isomorphic to the L1 form because the L1 signature is already whole-tensor / no-element-loop. The L3 entry exists for layer-coherence — a reader at L3 finds `axpy` defined in L3 vocabulary without having to reach down to L1.

The two layers' entries share the algebraic-law set, the variant-axis profile, the referent semantics, and the cited L0 evidence. They differ in **layer-coherence framing**: L1 frames the operator as the mutation-rotation lift from L0; L3 frames the operator as a whole-tensor field operation at the iteration-rotation layer. The body of the operator is the identity rotation across this edge.

[new]:
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
```

### 3. `book/src/L3/axpby.md` — reduce to general arity-2 specialization-stub

```edit:book/src/L3/axpby.md
[old]:
# axpby

Whole-tensor fused two-scalar two-vector update at L3: `axpby(α, x, β, y) = α·x + β·y` — the **general arity-2 specialization of the [`linear_combination`](./linear_combination.md) fold**: `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms speak **through** the combinator, not as re-derived base forms — `axpby` is the combinator at term-list length 2 with both coefficients free (subsuming [`axpy`](./axpy.md) at the second-coeff-1 reading and pure-scaling at α=0). This chapter is the arity-2 readout label for the bounded-arity L0 call shape (`AXPBY`); its algebra is the fold's law set read at that fixed length, and its lowering routes through the combinator's §"Downward to L2" identity edge + the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, no element loops, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `axpby` at L3 is a whole-tensor linear-combination primitive consumed by `krylov-step`'s iterate-stratum update (per [`krylov-step`](./krylov-step.md) §Semantics line 82: `krylov_update` at L3 composes whole-tensor primitives including `axpby`).

The L3 form is **value-thread-isomorphic to the L1 form**: `axpby`'s L1 signature is whole-tensor in / whole-tensor out with no element loop exposed (the L1 entry is written against `Tensor[N]` arguments). The L3 layer's vocabulary requirement — whole-tensor primitives, no element loops — is satisfied by L1's signature shape directly. The rotation L3→L1 is therefore the identity on the primitive itself; the per-element semantics that L1 uses to describe the operator (`result[i] = α·x[i] + β·y[i]`) is the referent, not the surface.

This L3 entry is the layer-coherence anchor for the cycle-011 BLAS-1 cohort backfill. Mirrors the cycle-010 `book/src/L3/krylov-step.md` precedent. One of three sibling firmings in the cycle-011 wave-1 BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`).

`axpby` is the fused-primitive choice (not a decomposition of `scal ∘ axpy`); the decision is recorded in [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md) (cycle-003) and inherited at L3 unchanged — the fusion preserves the algebraic statement `α·x + β·y` as a primitive linear combination, and the L3 layer's whole-tensor discipline is consistent with that primitive shape.

## Signature

```text
axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
```

Positional value-threading; no monadic effect; no record-typing:

- `α : Scalar` — first scalar coefficient.
- `x : Tensor[N]` — first input tensor; whole-tensor read.
- `β : Scalar` — second scalar coefficient.
- `y : Tensor[N]` — second input tensor (the *prior* value, when used as a fused update); whole-tensor read.
- result `: Tensor[N]` — output tensor; whole-tensor write (fresh value).

Shape contract (bunsen-style, named axis):

- `N` — length axis; shared across `x`, `y`, and the result.
- element type — uniform across `x`, `y`; uniform `Scalar` for both `α` and `β` matches the vector element type modulo scalar promotion.

`x` and `y` must share the same length axis `N` and the same element type. The scalars `α` and `β` share each other's type and the vector element type. When the vectors are complex, real scalars are promoted to complex (all-or-none across the scalar pair) per the [`scalar-promotion`](../concepts/scalar-promotion.md) typing rule. The L3 form inherits the `real ⊑ complex` scalar lattice from L1.

The L3 calculus has no record-typing and no `readonly` annotation; the signature is positional. The argument ordering `(α, x, β, y)` interleaves scalars and tensors; this matches both the L1 signature and the upstream L0 Palace API surface (`palace/linalg/vector.cpp:726-743`).

## Semantics

`axpby` at L3 is a single whole-tensor fused linear combination: `axpby(α, x, β, y)` produces the tensor `α·x + β·y`, computed in a single primitive step (the fusion is preserved at L3 because it has algebraic meaning — the law `axpby(α, x, β, y) = α·x + β·y` is a primitive statement of the linear combination, not a derived shorthand).

The operator is **pure at L3**: the prior `y` and the new value (returned positionally) are distinct values; no destination buffer appears in the signature. The L3 form has no aliasing — both inputs and the output are conceptually distinct tensors. In-place mutation reappears in the L1>L0 lowering chain via [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md); the L3 form is uniformly out-of-place.

**The operator is reduction-free and element-local at the referent semantics**: the per-element relation `result[i] = α·x[i] + β·y[i]` holds at every position independently, with no cross-element communication. This is a property of the referent, observable when the L3 form is lowered to L1.

**The operator carries no sequential obstruction**: `axpby` is a leaf primitive at L3 (and at L1); the iteration-rotation marker (per [`sequential-obstruction`](../concepts/sequential-obstruction.md)) does not apply to it. The sequential obstruction lives at the consuming composition (the outer `iterate_while_L3` loop folding `krylov-step`), not at `axpby` itself.

Special algebraic cases — `α = 0` (pure scaling of `y`), `β = 0` (pure scaling of `x`, discards `y`), `α = 1, β = 1` (vector add), `β = 1` (recovers `axpy`), `α = -1, β = 1` (vector subtract) — are not separate operators at L3. They are algebraic identities, recorded in §Algebraic laws. The L0 source has no constant-folding branches inside the `AXPBY` family (unlike `axpy`'s `α == 1.0` fast-path); the L0 surface uniformly delegates without inspecting scalar values, per `book/src/L1/axpby.md` §Semantics.

### Iteration-rotation marker

L3 is the iteration-rotation layer, but `axpby` is a **leaf primitive** with no iteration view of its own — it is a single whole-tensor operation, not a fold over a trajectory. The iteration view applies to compositions of `axpby` (notably `krylov-step`'s iterate-stratum update). At the leaf `axpby` itself, there is no iteration carry, no successor relation, no fold. The L3 layer-coherence reason for this entry is **vocabulary inventory**, not iteration-view content.

## Algebraic laws

Inherited verbatim from L1 (per the identity-in-form rotation). The laws below hold at L3 because they hold at L1 and the L3 form is value-thread-isomorphic to the L1 form.

1. **Subsumption of `axpy`**: `axpby(α, x, 1, y) = axpy(α, x, y) = α·x + y`. Load-bearing identity from `scaffolding/decisions/axpby-as-primitive.md`: [`axpy`](./axpy.md) is the β=1 specialisation of `axpby`, not a dependency. Both stay in the L3 dep-map as siblings.
2. **Identity in `α`**: `axpby(0, x, β, y) = β·y` for any `x`. (When [`scal`](./scal.md) lands at L3, restates as `axpby(0, x, β, y) = scal(β, y)`. Until then, stated as the scalar-times-tensor operation `β·y`.)
3. **Identity in `β`**: `axpby(α, x, 0, y) = α·x` for any `y`. (Likewise restates as `scal(α, x)` once `scal` lands.)
4. **Identities in both**: `axpby(0, x, 0, y) = 0` (the zero tensor of axis `N`).
5. **Bilinearity in the scalar pair `(α, β)`**: `axpby(α, x, β, y)` is linear separately in each of `α` and `β` (with the other scalar and both tensors held fixed). Inherited from L1 Law 5.
6. **Right distribution over tensor addition in `x`**: `axpby(α, x₁ + x₂, β, y) = axpby(α, x₁, β, y) + axpby(α, x₂, 0, y) = α·x₁ + α·x₂ + β·y`. (The `axpby(α, x₂, 0, y)` term is `α·x₂` per Law 3; the `+` is tensor addition. Verbatim form from L1 axpby Law 6.)
7. **Right distribution over tensor addition in `y`**: `axpby(α, x, β, y₁ + y₂) = axpby(α, x, β, y₁) + β·y₂ = α·x + β·y₁ + β·y₂`.
8. **Scalar absorption**: `axpby(α·γ, x, β, y) = axpby(α, γ·x, β, y) = axpby(α, x, β·γ, γ⁻¹·y)` (the latter only for invertible scalar `γ`) — the scalars absorb into their paired tensor.
9. **Chained-`axpby` collapse on shared `x`**: `axpby(α₁, x, β₁, axpby(α₂, x, β₂, y)) = axpby(α₁ + β₁·α₂, x, β₁·β₂, y)`. Two successive `axpby` updates against the same `x` collapse to one with scalars `(α₁ + β₁·α₂, β₁·β₂)`. Generalises Law 4 of `axpy` (the β₁ = β₂ = 1 case). Underwrites the consuming composition's fusion of consecutive coefficient-update lines.

Laws that explicitly **do not** hold (inherited from L1):

- **Commutativity in the tensor arguments**: `axpby(α, x, β, y) ≠ axpby(β, y, α, x)` in general unless `α = β` — the operator is symmetric in the inputs only because `α·x + β·y = β·y + α·x` mathematically, and the signature distinguishes argument slots by which scalar pairs with which tensor.
- **Associativity**: `axpby` is quaternary; associativity is not well-typed.
- **Floating-point associativity of the summation**: `α·x + β·y` computed in IEEE-754 may differ from any reordering at the bit level when the magnitudes of `α·x` and `β·y` differ enough to lose precision. The L3 form is order-agnostic algebraically; bit-identical reproduction of L0 output requires matching the L0 evaluation order (pinned by MFEM's `add(α, x, β, y, y)` kernel). Inherited from L1; recorded here, not erased.
- **Fusion identity with `scal + axpy`**: `axpby(α, x, β, y) ≠ scal(β, axpy(α/β, x, y))` in general at the bit level (the two-pass form rounds twice; the fused form rounds once) even though the values agree mathematically. The L0 form is fused for a reason; the L3 algebra preserves the fused statement.

The algebraic-law set at L3 is **identical** to the L1 algebraic-law set.

## Dependencies

**Same-layer (L3)**: no other L3 operators (axpby is a leaf primitive). The composition surfaces that consume `axpby` at L3 are the iterate-stratum update inside `krylov-step`'s `krylov_update` (per [`krylov-step`](./krylov-step.md) §Semantics).

**Subsumption (not dependency)**: `axpy(α, x, y) ≡ axpby(α, x, 1, y)` — both stay in the L3 dep-map as siblings.

**Cross-cutting concepts** (consumed unchanged across the chain):

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the `real ⊑ complex` typing-rule. Inherited from L1 verbatim; no L3-specific semantics.
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — underwrites the L3-native-by-signature-shape claim.

No L4 monadic vocabulary; neither `axpby` nor the `linear_combination` fold it specializes is a calculus combinator at L4 (the cohort audit verdict is **CONFIRMED-NOT-NEEDED**; `L3/linear_combination.md:152-154`). The downward rotation passes through the firm L2 [`linear_combination`](../L2/linear_combination.md) via the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at term-list length 2 (both coefficients free) — `axpby` is the general arity-2 fold member. The substantive arity-dispatch (length → maximal fused L0 leaf, here the `AXPBY` symbol) + the pinned summation order live in the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme, NOT in a per-leaf theme.

## Variant axes

Inherited unchanged from the L1 entry at two:

1. **element-type** (`real | complex`) — the L1 entry distinguishes real-vector and complex-vector overloads; at L3 these collapse to one operator parameterised by element type. Semantics are identical across element types.
2. **scalar-promotion** (sub-axis on the complex element-type) — see [`scalar-promotion`](../concepts/scalar-promotion.md). Real `(α, β)` against complex `x, y` is promoted to complex with zero imaginary part (all-or-none across the scalar pair). Typing-rule property, not an operator variant.

The variant-axis profile at L3 matches L1 exactly. No new axes introduced; no axes merged or split.

## Status

`firm` — whole-tensor positional signature is canonical at L3; algebraic laws are the nine that hold at L1 (inherited verbatim under the identity-in-form rotation); non-laws are catalogued explicitly; variant-axis profile is closed at two. The pattern is well-attested via L1 (cycle-003 firm) and via the L3-L2 body-identity theme's §"Applicability conditions" point 3, which explicitly names `axpby` as L3-native by signature shape. This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** per **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase). One of three sibling firmings in the BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`).

## Lowers to

L3 `axpby` lowers as the **general arity-2 specialization of [`linear_combination`](./linear_combination.md)** (`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`). The combinator lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the fold body (`L3/linear_combination.md:107-113` §"Downward to L2"). The substantive rotation in the downward chain is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme: it reads the term-list length (here 2, both coefficients free) and selects the maximal fused L0 leaf — the `AXPBY` symbol, realized as MFEM's single aligned `add(α, x, β, y, y)` pass (`palace/linalg/vector.cpp:726-730`) — and records its pinned summation order. All arity dispatch and summation-order residue are the fold-parent's, not this leaf's.

The **transitive** L3>L1 identity (the combinator's L3>L2 identity ∘ the L2>L1 fold-specialization's value-identity at this list length) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive in-place mutation rotation, reached transitively, is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md).

## Lifts from

No L4 entry exists for `axpby` (the cohort audit verdict is **CONFIRMED-NOT-NEEDED** for the BLAS-1 cohort at L4). `axpby` appears inside L4 entries as a let-binding inside `krylov-step`'s body but is not a first-class L4 calculus combinator.

## Evidence

All L0 evidence is inherited via L1 (`book/src/L1/axpby.md` §Evidence). Direct citations relevant to this L3 entry:

- `book/src/L3/linear_combination.md` (cycle-050 firm) + `book/src/L2/linear_combination.md` (inverted-to-entry cycle-049 D1) — the family combinator this leaf is the general arity-2 specialization of; §"Arity specializations" (`L3/linear_combination.md:50-61`) names `axpby = linear_combination [(α,x),(β,y)]`, §"Downward to L2" (`:107-113`) is the identity-in-form edge this leaf's lowering reads at length 2.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; cycle-049 D1(c) KEEP verdict) — the substantive L2>L1 fusion-selection theme that picks the `AXPBY` L0 leaf at this list-length and records its pinned summation order (the lowering's substantive content, deferred here, not in a per-leaf theme).
- `book/src/L1/axpby.md` (cycle-003 firm) — the L1 leaf the fold-specialization recovers at this arity (the L1>L0 one-to-one `AXPBY` symbol shape). Body shape, semantics, nine algebraic laws, four non-laws, variant-axis profile.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm) — names `axpby` as L3-native by signature shape.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:67` (firm) — renders `axpby` in the L3 body let-chain identically to L1.
- `book/src/L3/index.md:13` — L3 vocabulary inventory implicitly covering the linear-update cohort.
- `book/src/L3/krylov-step.md` (cycle-010 firm; the precedent layer-coherence backfill) — the template this entry follows.
- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` — the cycle-010 audit identifying this cohort as HIGH CONFIDENCE backfill.
- `scaffolding/decisions/axpby-as-primitive.md` (cycle-003) — the fused-primitive choice rationale, inherited at L3 unchanged.
- `concepts/scalar-promotion.md` (cycle-005 firm) — the typing-rule for the real-on-complex-vector case at L3 / L1.

L0 source ranges (inherited via L1; not consumed as new evidence at L3):

- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member decl.
- `palace/linalg/vector.hpp:309-311` — free-function template `AXPBY`.
- `palace/linalg/vector.cpp:726-730` — real-real `AXPBY`.
- `palace/linalg/vector.cpp:732-737` — complex-complex `AXPBY`.
- `palace/linalg/vector.cpp:739-743` — real-α-real-β-on-complex-vector promotion site.

## L3 vs L1 distinction

- **L1**: whole-tensor pure-functional update `axpby :: (α, x, β, y) -> α·x + β·y`. Mutation-lifted from the L0 source's in-place form; the fused primitive that subsumes `axpy` and pure-scaling. The closest pure-functional layer to the source.
- **L3**: whole-tensor pure-functional update `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`. The iteration-rotation layer's rendering, value-thread-isomorphic to the L1 form. The L3 entry exists for layer-coherence.

The two layers' entries share the algebraic-law set, the variant-axis profile, the referent semantics, the fused-primitive choice, and the cited L0 evidence. They differ in **layer-coherence framing**: L1 frames the operator as the mutation-rotation lift from L0; L3 frames the operator as a whole-tensor field operation at the iteration-rotation layer. The body of the operator is the identity rotation across this edge.

[new]:
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
```

### 4. `book/src/L3/axpbypcz.md` — reduce to arity-3 specialization-stub

```edit:book/src/L3/axpbypcz.md
[old]:
# axpbypcz

Whole-tensor fused three-scalar three-vector update at L3: `axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z` — the **arity-3 specialization of the [`linear_combination`](./linear_combination.md) fold**: `axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms speak **through** the combinator, not as re-derived base forms — `axpbypcz` is the combinator at term-list length 3 (subsuming [`axpby`](./axpby.md) at γ=0 and [`axpy`](./axpy.md) at β=1, γ=0). This chapter is the arity-3 readout label for the bounded-arity L0 call shape (`AXPBYPCZ`, the top of Palace's bounded-arity surface); its algebra is the fold's law set read at that fixed length, and its lowering routes through the combinator's §"Downward to L2" identity edge + the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, no element loops, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `axpbypcz` at L3 is a whole-tensor three-vector linear-combination primitive consumed by `krylov-step`'s iterate-stratum update for the three-vector slice patterns (Chebyshev, BiCGStab; per [`krylov-step`](./krylov-step.md) §Semantics line 82: `krylov_update` at L3 composes whole-tensor primitives including `axpbypcz`).

The L3 form is **value-thread-isomorphic to the L1 form**: `axpbypcz`'s L1 signature is whole-tensor in / whole-tensor out with no element loop exposed (the L1 entry is written against `Tensor[N]` arguments). The L3 layer's vocabulary requirement is satisfied by L1's signature shape directly. The rotation L3→L1 is the identity on the primitive itself; the per-element semantics that L1 uses to describe the operator (`result[i] = α·x[i] + β·y[i] + γ·z[i]`) is the referent.

This L3 entry is the layer-coherence anchor for the cycle-011 BLAS-1 cohort backfill. One of three sibling firmings in the cycle-011 wave-1 BLAS-1 linear-update bundle (`axpy`, `axpby`, `axpbypcz`).

`axpbypcz` is the fused-primitive choice (not a decomposition); the decision mirrors `axpby`'s cycle-003 fused-primitive verdict (per `scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects" — explicit invitation for the `axpbypcz` harvester to mirror the fused-primitive choice). Inherited at L3 unchanged.

## Signature

```text
axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
```

Positional value-threading; no monadic effect; no record-typing:

- `α : Scalar` — first scalar coefficient.
- `x : Tensor[N]` — first input tensor; whole-tensor read.
- `β : Scalar` — second scalar coefficient.
- `y : Tensor[N]` — second input tensor; whole-tensor read.
- `γ : Scalar` — third scalar coefficient.
- `z : Tensor[N]` — third input tensor (the *prior* value, when used as a fused update); whole-tensor read.
- result `: Tensor[N]` — output tensor; whole-tensor write (fresh value).

Shape contract (bunsen-style, named axis):

- `N` — length axis; shared across `x`, `y`, `z`, and the result.
- element type — uniform across `x`, `y`, `z`; uniform `Scalar` for `α`, `β`, `γ` matches the vector element type modulo scalar promotion.

`x`, `y`, and `z` must share the same length axis `N` and the same element type. The scalars `α`, `β`, `γ` share each other's type and the vector element type. When the vectors are complex, real scalars are promoted to complex (all-or-none across the scalar triple) per the [`scalar-promotion`](../concepts/scalar-promotion.md) typing rule.

The L3 calculus has no record-typing and no `readonly` annotation; the signature is positional. The argument ordering `(α, x, β, y, γ, z)` interleaves scalars and tensors; this matches both the L1 signature and the upstream L0 Palace API surface (`palace/linalg/vector.cpp:745-772`).

## Semantics

`axpbypcz` at L3 is a single whole-tensor fused three-way linear combination: `axpbypcz(α, x, β, y, γ, z)` produces the tensor `α·x + β·y + γ·z`, computed in a single primitive step (the fusion is preserved at L3 because it has algebraic meaning — the law is a primitive statement of the linear combination).

The operator is **pure at L3**: the prior `z` and the new value (returned positionally) are distinct values; no destination buffer appears in the signature. In-place mutation reappears in the L1>L0 lowering chain via [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md); the L3 form is uniformly out-of-place.

**The operator is reduction-free and element-local at the referent semantics**: the per-element relation `result[i] = α·x[i] + β·y[i] + γ·z[i]` holds at every position independently.

**The operator carries no sequential obstruction**: `axpbypcz` is a leaf primitive at L3 (and at L1); the iteration-rotation marker does not apply to it.

Special algebraic cases — `γ = 0` (recovers `axpby`), `β = 0, γ = 0` (recovers `axpy` with α=α), `β = 1, γ = 0` (recovers `axpy`), `α = 0` (drops `x`, gives `axpby(β, y, γ, z)`), all-zero (zero tensor) — are not separate operators at L3. They are algebraic identities, recorded in §Algebraic laws. The L0 source has exactly one specialisation branch inside the `AXPBYPCZ` family (the real-real path's `γ == 0` constant-fold to MFEM's `add(α, x, β, y, z)`); this is a transparent performance trick at L1 that has already been erased; it does not reappear at L3.

### Iteration-rotation marker

L3 is the iteration-rotation layer, but `axpbypcz` is a **leaf primitive** with no iteration view of its own. The iteration view applies to compositions of `axpbypcz` (notably `krylov-step`'s iterate-stratum update in three-vector slices). At the leaf `axpbypcz` itself, there is no iteration carry, no successor relation, no fold. The L3 layer-coherence reason for this entry is **vocabulary inventory**, not iteration-view content.

## Algebraic laws

Inherited verbatim from L1 (per the identity-in-form rotation). The laws below hold at L3 because they hold at L1.

1. **Subsumption of `axpby`**: `axpbypcz(α, x, β, y, 0, z) = axpby(α, x, β, y)` for any `z`. Load-bearing identity from the L0 `γ == 0` branch. Both stay in the L3 dep-map as siblings.
2. **Subsumption of `axpy`**: `axpbypcz(α, x, 1, y, 0, z) = axpy(α, x, y)` for any `z`. Composition of Law 1 (γ=0 → axpby) and axpby Law 1 (β=1 → axpy).
3. **Identity in `α`**: `axpbypcz(0, x, β, y, γ, z) = β·y + γ·z = axpby(β, y, γ, z)` for any `x`.
4. **Identity in `β`**: `axpbypcz(α, x, 0, y, γ, z) = α·x + γ·z = axpby(α, x, γ, z)` for any `y`.
5. **Identity in `γ`**: see Law 1 (γ=0 subsumption — recovers `axpby(α, x, β, y)`).
6. **All-zero identity**: `axpbypcz(0, x, 0, y, 0, z) = 0` (the zero tensor of axis `N`) for any `x`, `y`, `z`.
7. **Trilinearity in the scalar triple `(α, β, γ)`**: `axpbypcz(α, x, β, y, γ, z)` is linear separately in each of `α`, `β`, `γ` (with the others and all tensors held fixed). Inherited from L1 Law 7.
8. **Right distribution over tensor addition in `x`**: `axpbypcz(α, x₁ + x₂, β, y, γ, z) = axpbypcz(α, x₁, β, y, γ, z) + α·x₂`.
9. **Right distribution over tensor addition in `y`**: `axpbypcz(α, x, β, y₁ + y₂, γ, z) = axpbypcz(α, x, β, y₁, γ, z) + β·y₂`.
10. **Right distribution over tensor addition in `z`**: `axpbypcz(α, x, β, y, γ, z₁ + z₂) = axpbypcz(α, x, β, y, γ, z₁) + γ·z₂`.
11. **Scalar absorption**: `axpbypcz(α·κ, x, β, y, γ, z) = axpbypcz(α, κ·x, β, y, γ, z)` and symmetrically for the `β`/`y` and `γ`/`z` pairs.
12. **Chained-`axpbypcz` collapse on shared `(x, y)`**: `axpbypcz(α₁, x, β₁, y, γ₁, axpbypcz(α₂, x, β₂, y, γ₂, z)) = axpbypcz(α₁ + γ₁·α₂, x, β₁ + γ₁·β₂, y, γ₁·γ₂, z)`. Generalises axpby Law 9.

Laws that explicitly **do not** hold (inherited from L1):

- **Commutativity in the tensor arguments**: `axpbypcz(α, x, β, y, γ, z) ≠ axpbypcz(β, y, α, x, γ, z)` in general unless `α = β` — the operator is symmetric in the inputs only because the linear combination is commutative mathematically; the signature distinguishes argument slots by which scalar pairs with which tensor.
- **Associativity**: `axpbypcz` is six-ary (three scalar-tensor pairs); associativity is not well-typed.
- **Floating-point associativity of the summation**: `α·x + β·y + γ·z` computed in IEEE-754 may differ from any reordering at the bit level. The two L0 branches of the real-real `AXPBYPCZ` (the `γ == 0` fast-path via MFEM `add(α, x, β, y, z)` vs the `γ ≠ 0` slow-path two-call split `AXPBY(α, x, γ, z); z.Add(β, y)`) themselves use different summation orders. The L3 form is order-agnostic algebraically; bit-identical reproduction of L0 output requires matching the L0 branch's evaluation order.
- **Fusion identity with three separate `scal`+`add` passes**: `axpbypcz(α, x, β, y, γ, z) ≠ scal(α, x) + scal(β, y) + scal(γ, z)` in general at the bit level (three-pass rounds three times; fused form rounds once or twice depending on the L0 branch).

The algebraic-law set at L3 is **identical** to the L1 algebraic-law set.

## Dependencies

**Same-layer (L3)**: no other L3 operators (axpbypcz is a leaf primitive). The composition surfaces that consume `axpbypcz` at L3 are the iterate-stratum update inside `krylov-step`'s `krylov_update` (per [`krylov-step`](./krylov-step.md) §Semantics) — particularly the three-vector slice patterns (Chebyshev, BiCGStab).

**Subsumption (not dependency)**: `axpby(α, x, β, y) ≡ axpbypcz(α, x, β, y, 0, z)` and `axpy(α, x, y) ≡ axpbypcz(α, x, 1, y, 0, z)` (for any `z` — the result is independent of `z` when `γ = 0`). All three stay in the L3 dep-map as siblings.

**Cross-cutting concepts** (consumed unchanged across the chain):

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the `real ⊑ complex` typing-rule.
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — underwrites the L3-native-by-signature-shape claim.

No L4 monadic vocabulary; neither `axpbypcz` nor the `linear_combination` fold it specializes is a calculus combinator at L4 (the cohort audit verdict is **CONFIRMED-NOT-NEEDED**; `L3/linear_combination.md:152-154`). The downward rotation passes through the firm L2 [`linear_combination`](../L2/linear_combination.md) via the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at term-list length 3 — `axpbypcz` is the arity-3 fold member. The substantive arity-dispatch (length → maximal fused L0 leaf, here the `AXPBYPCZ` symbol, including the `γ==0` arity-collapse to `axpby`) + the pinned summation order live in the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme, NOT in a per-leaf theme.

## Variant axes

Inherited unchanged from the L1 entry at two:

1. **element-type** (`real | complex`) — at L3 collapses to one operator parameterised by element type.
2. **scalar-promotion** (sub-axis on the complex element-type) — see [`scalar-promotion`](../concepts/scalar-promotion.md). Real `(α, β, γ)` against complex `x, y, z` is promoted to complex with zero imaginary part (all-or-none across the scalar triple).

**Internal control-flow axis at L0 (not an L3 variant axis)**: the real-real specialisation's `γ == 0` branch is a transparent performance specialisation — algebraically equivalent at L1 — and not visible at L3. Inherited from L1.

The variant-axis profile at L3 matches L1 exactly.

## Status

`firm` — whole-tensor positional signature is canonical at L3; algebraic laws are the twelve that hold at L1 (inherited verbatim under the identity-in-form rotation); non-laws are catalogued explicitly; variant-axis profile is closed at two. Well-attested via L1 (cycle-003 firm; landed as the next harvester target after `axpby`) and via the L3-L2 body-identity theme's §"Applicability conditions" point 3, which explicitly names `axpbypcz` as L3-native by signature shape. This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** per **Identity-lowerings still require both L levels**. One of three sibling firmings in the BLAS-1 linear-update bundle.

## Lowers to

L3 `axpbypcz` lowers as the **arity-3 specialization of [`linear_combination`](./linear_combination.md)** (`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`). The combinator lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the fold body (`L3/linear_combination.md:107-113` §"Downward to L2"). The substantive rotation in the downward chain is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme: it reads the term-list length (here 3) and selects the maximal fused L0 leaf — the `AXPBYPCZ` symbol, including the `γ == 0` arity-collapse branch (`palace/linalg/vector.cpp:745-758`, the `:749-751` `add(α, x, β, y, z)` fast-path that is the exact algebraic content of the fold's zero-coefficient term-drop law) — and records the pinned summation order of each L0 branch. All arity dispatch and summation-order residue are the fold-parent's, not this leaf's.

The **transitive** L3>L1 identity (the combinator's L3>L2 identity ∘ the L2>L1 fold-specialization's value-identity at this list length) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive in-place mutation rotation, reached transitively, is the L1>L0 [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md).

## Lifts from

No L4 entry exists for `axpbypcz` (CONFIRMED-NOT-NEEDED per cohort audit). Appears inside L4 entries as a let-binding inside `krylov-step`'s body but is not a first-class L4 calculus combinator.

## Evidence

All L0 evidence is inherited via L1 (`book/src/L1/axpbypcz.md` §Evidence). Direct citations:

- `book/src/L3/linear_combination.md` (cycle-050 firm) + `book/src/L2/linear_combination.md` (inverted-to-entry cycle-049 D1) — the family combinator this leaf is the arity-3 specialization of; §"Arity specializations" (`L3/linear_combination.md:50-61`) names `axpbypcz = linear_combination [(α,x),(β,y),(γ,z)]`, §"Downward to L2" (`:107-113`) is the identity-in-form edge this leaf's lowering reads at length 3.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; cycle-049 D1(c) KEEP verdict) — the substantive L2>L1 fusion-selection theme that picks the `AXPBYPCZ` L0 leaf at this list-length, handles the `γ==0` arity-collapse, and records the pinned summation order of each L0 branch (the lowering's substantive content, deferred here, not in a per-leaf theme).
- `book/src/L1/axpbypcz.md` (cycle-003 firm) — the L1 leaf the fold-specialization recovers at this arity (the L1>L0 one-to-one `AXPBYPCZ` symbol shape). Body shape, semantics, twelve algebraic laws, four non-laws, variant-axis profile.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm) — names `axpbypcz` as L3-native by signature shape.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:67` (firm) — renders `axpbypcz` in the L3 body let-chain identically to L1.
- `book/src/L3/krylov-step.md` (cycle-010 firm; the precedent layer-coherence backfill) — the template this entry follows.
- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` — the cycle-010 audit identifying this cohort as HIGH CONFIDENCE backfill.
- `scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects" (cycle-003) — explicit invitation for the `axpbypcz` harvester to mirror the fused-primitive choice; inherited at L3 unchanged.
- `concepts/scalar-promotion.md` (cycle-005 firm) — the typing-rule for the real-on-complex-vector case.

L0 source ranges (inherited via L1; not consumed as new evidence at L3):

- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl.
- `palace/linalg/vector.hpp:313-316` — free-function template `AXPBYPCZ`.
- `palace/linalg/vector.cpp:745-758` — real-real `AXPBYPCZ` with `γ == 0` branch.
- `palace/linalg/vector.cpp:760-765` — complex-complex `AXPBYPCZ`.
- `palace/linalg/vector.cpp:767-772` — real-α-real-β-real-γ-on-complex-vector promotion site.

## L3 vs L1 distinction

- **L1**: whole-tensor pure-functional update `axpbypcz :: (α, x, β, y, γ, z) -> α·x + β·y + γ·z`. Mutation-lifted from the L0 source's in-place form; the fused primitive subsuming `axpby` and `axpy`.
- **L3**: whole-tensor pure-functional update `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`. The iteration-rotation layer's rendering, value-thread-isomorphic to the L1 form. The L3 entry exists for layer-coherence.

The two layers' entries share the algebraic-law set, the variant-axis profile, the referent semantics, the fused-primitive choice, and the cited L0 evidence. They differ in **layer-coherence framing** only.

[new]:
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
```

## Discipline notes

**What changed and why.** Each of the four leaves had its full duplicated body (Semantics, Iteration-rotation marker, Algebraic laws, Dependencies prose, L3-vs-L1 distinction) DELETED and replaced by a thin §Specialization + §Variant-axes + §Status + §Evidence stub. This is the **reduce-to-stub** completion of the cycle-051 re-expression: at c051 the leaves were already re-pointed *through* the combinator (the opener, `lifts_from`, `Lowers to`, §Dependencies all say "arity-N specialization of `linear_combination`"), so this pass is a pure structural shrink — the deleted prose was the combinator's content read at a fixed arity, and per the dispatch's clause (c) it is DEFERRED to `L3/linear_combination`'s §"Downward to L2" + §"Arity specializations" (the combinator note is the home). The YAML frontmatter blocks were left untouched (they already carry the correct `lifts_from`/`lowers_to` combinator routing from c051).

**(b) Uniqueness verified — nothing the combinator lacks was dropped.** I compared each leaf's L0 anchors against the combinator's Evidence section. The combinator cites the **free-function** surface (`vector.cpp:702-712/726-730/745-758`, `vector.hpp:305-316`, + the `nleps`/`romoperator` γ=1 sites). Each leaf carries UNIQUE anchors the combinator does NOT have, all RETAINED in the stub:
- `scal`: the receiver-mutating `operator*=` member-method idiom (`vector.hpp:98-99`, `vector.cpp:203-227` incl. `:206-211`) + `Normalize` (`vector.hpp:262-270`) + consumer sites (`iterative.cpp:632,811`, `operator.cpp:661,673`, `nleps.cpp:486-491`). `scal` is the ONLY family member with a receiver-mutating L0 surface — load-bearing, retained.
- `axpy`: `ComplexVector::AXPY` def (`vector.cpp:276-311`), the `α==1.0` fast-path (`vector.cpp:702-712` — overlaps the combinator's range but the fast-path NOTE is arity-2-specific, retained), promotion (`:715-718`), decls (`hpp:115-118`, `:305-307`).
- `axpby`: complex-complex (`vector.cpp:732-737`), promotion (`:739-743`), the MFEM `add(α,x,β,y,y)` fused-pass note, no-constant-folding fact (load-bearing distinction from `axpy`), decls (`hpp:130-131`, `:309-311`).
- `axpbypcz`: complex-complex (`vector.cpp:760-765`), promotion (`:767-772`), the `γ==0` arity-collapse branch (`:749-751`) + the two-branch summation-order residue (load-bearing IEEE note), decls (`hpp:133-136`, `:313-316`).
Each leaf's ONE collapsed variant-axis row (element-type + scalar-promotion sub-axis) is RETAINED verbatim. `## Status: firm` kept on all four.

**Citation self-verification (citecheck `--anchor`, on-disk).** Every retained L0 anchor was run through `python3 tools/citecheck/citecheck.py <path:lo-hi> --anchor <token>` against on-disk `reference/palace/` BEFORE emission: `scal` (`vector.cpp:203-227` / `hpp:98-99` anchor `operator*=` — ok); `axpy` (`vector.cpp:276-311`/`:702-712`/`:715-718`, `hpp:115-118` anchor `AXPY` — ok); `axpby` (`vector.cpp:732-737`/`:739-743`, `hpp:130-131` anchor `AXPBY` — ok); `axpbypcz` (`vector.cpp:760-765`/`:767-772`, `hpp:133-136` anchor `AXPBYPCZ` — ok). All 11 checked anchors landed ON the cited range (the combinator-shared ranges `vector.cpp:702-712`/`726-730`/`745-758` were verified at c050; not re-run). No drift.

**Zero-dangling gate (`deleted-slug-inbound-live-link-sweep`).** Reduce-to-stub **KEEPS all four files on disk** (no `delete:` fence in this report), so by construction there can be **zero danglers**: every inbound live link continues to resolve to a live file. I enumerated the inbound links anyway as the gate requires: `SUMMARY.md:29-35` (the four nav entries), `L2/axpy.md`/`L2/axpby.md`/`L2/axpbypcz.md` (floor-parent back-refs), `L3-L2/orthogonalize-variant-split.md:134,259,293` (→ `../L3/axpy.md`), `L3/elementwise_product.md`/`normalize.md`/`reciprocal.md` (→ `./scal.md` precedent refs), `L3/index.md:31` (combinator row). **All targets remain on disk → 0 residual danglers.** The stubs' own outbound links (`./linear_combination.md`, `../L2-L1/...`, `../L1-L0/...`, `../concepts/...`) all point at on-disk firm files. Sweep result: **clean — 0 slugs deleted, 0 residual.** Note the stubs intentionally DROP some prior outbound links the deleted prose carried (`./krylov-step.md`, `../concepts/axpy.md` as a §Dependencies link, `./axpy.md`/`./axpby.md` sibling cross-links) — dropping an outbound link cannot create a dangler (it removes a reference, it does not orphan a target), and the dropped targets are all still reachable from the combinator and the L1 endpoints. The combinator (`L3/index.md` D4-owned) and `index.md` rows are NOT touched per scope.

**Layer-definition discipline (high→low).** The stubs narrate the rewrite forward (L3 leaf → combinator → L2 → L1 → L0); no reverse "how L1 lifts to L3" prose was introduced. The §Specialization framing is "this leaf IS the combinator at arity N," consistent with the high→low definition direction. No LHS/RHS inversion.

**Bounded prose-correction check.** None made — this was a pure structural shrink; no convention-backwards / drifted-citation / contradicting-claim was found in the retained content (the c051 re-expression vocabulary was already correct). The deleted body was accurate-but-redundant, not wrong.

## Supporting evidence

- Combinator (semantics home): `book/src/L3/linear_combination.md` (firm cycle-050) — §"Arity specializations" `:50-61`, §"Downward to L2" `:107-113`, law 5 (zero-coefficient term-drop, the `γ==0` realization) `:91`.
- Firm L1 endpoints (laws home): `book/src/L1/scal.md` (c004), `axpy.md` (c002), `axpby.md` (c003), `axpbypcz.md` (c003).
- Lowering home: `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; the substantive fusion-selection + pinned summation order).
- Ratifying provenance: cycle-051 D1 re-expression (the leaves' "speak through the combinator" framing this pass completes); the batch-15 reduce-to-stub convention; the 2026-06-01 vocabulary-shift redirect (CLAUDE.md §Methodology invariants ⟢ — combinator-primary, leaves as specialization notes).
- Sweep skill: `skills/deleted-slug-inbound-live-link-sweep/SKILL.md`.

## Open questions / caveats

- **No abstractor reread needed.** This was a pure structural rewrite — the firmed-up combinator's signature did not change the leaves' LHS shape (the leaves remain `scal`/`axpy`/`axpby`/`axpbypcz` at fixed arity; only the body was deferred upward). No non-trivial content decision was made; the deleted prose was verbatim-redundant with the combinator.
- **`scal` dropped two forward-references that are still rough-in elsewhere** — the prior body's "once the sibling `nrm2` entry lands (wave-1 dispatch #3)" note and the "no firm `scal-mutation-rotation` theme yet exists" note were part of the deleted Semantics/Dependencies prose. These are not lost information: the `Normalize` consumer relationship is retained via the `vector.hpp:262-270` anchor, and the L1>L0 mutation-rotation routing is retained via the combinator's §"Downward to L2" → L2>L1 → L1>L0 chain (the stub points at `linear-combination-fold-specialization`). No live link was broken (both were plain-text/prose, not live links to missing files).
- **Combinator-row count ownership (D4 scope).** `L3/index.md:31` still describes the four leaves as "cycle-051 collapses them into §Arity-specializations notes" — after this pass they ARE collapsed (reduced to stubs). D4 owns the index narrative; flag for D4/integrator that the index row's tense ("collapses" → "collapsed") may want a touch, but it is NOT this dispatch's scope and is not a build-breaker (prose, not a link).
- **Stub-vs-firm tier.** All four keep `## Status: firm` per scope. A specialization-stub that defers semantics to a firm parent while retaining self-verified unique L0 anchors is firm (the operator IS fully specified — by reference to the combinator + its own L0 surface), not a claim-free `stub`-tier placeholder. This matches the batch-15 reduce-to-stub convention (the file is "reduced" in length, not demoted in maturity).
