---
agent: harvester
invoked_at: 2026-05-27T23:45:40Z
scope: L3 operator: scal
status: integrated
integrated_at: 2026-05-28T013333Z
integration_commit: PLACEHOLDER_SHA
integration_notes: cycle-011 wave-1 pass 4; closes BLAS-1 cohort; 8th firm L3 operator landing; L3 firm-operator count reaches 8 — fully closes BLAS-1 cohort portion of OQ l3-backfill-apply-linop-and-blas1-cohort (HIGH CONFIDENCE recommendations from cycle-010 cross-layer-cross-cutter audit); priority #20 second target fully met; 4 proposed-changes applied cleanly; 0 safety-net gate hits; 2 new OQs promoted (scal-mutation-rotation-l1-l0-theme + l3-index-semantics-overlay-blas1-cohort-prose-refresh); cumulative in-line identity-rotation count reaches 7 (exceeds revisit threshold of 6)
inputs:
  - book/src/L1/scal.md (firm; cycle-004)
  - book/src/L3/krylov-step.md (firm L3 precedent; cycle-010 wave-1 backfill)
  - book/src/L3/index.md (L3 vocabulary inventory; dep-map)
  - book/src/L3-L2/krylov-step-body-identity.md:97 (the seven BLAS-1 primitives named L3-native by signature)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:68 (L3 let-chain rendering the BLAS-1 primitives)
  - book/src/concepts/scalar-promotion.md
  - book/src/concepts/scal.md
  - reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md (HIGH CONFIDENCE backfill recommendation, bundle item)
  - CLAUDE.md §Methodology invariants ("Identity-lowerings still require both L levels"; "Layers are defined high→low")
  - scaffolding/priorities.md priority #20 (identity-lowering-both-levels-backfill)
---

# CYCLE: Formalize scal at L3

## Summary

Firm L3 entry for `scal`, the BLAS-1 vector-scalar multiply primitive `y ← α·y` — last of the 4-dispatch BLAS-1 cohort backfill in cycle-011 wave-1 (siblings: #1 apply_linop, #2 axpy/axpby/axpbypcz, #3 dot/nrm2). The L3 form is **value-thread-isomorphic** to the L1 form: `scal` has signature `Scalar -> Tensor[N] -> Tensor[N]`, no element loop is exposed at the signature, and it is an L3-native whole-tensor operation by construction (per `book/src/L3-L2/krylov-step-body-identity.md:97` and `book/src/L3/index.md:13`). The rotation L3 → L1 is identity-in-form on the primitive itself; the surface adjustment is documentary (L3 frames the operator as a whole-tensor field operation in the iteration-rotation layer, whereas L1 frames the same operator as the pure-functional image of the receiver-mutating `*=` source idiom).

Per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md, cycle-009 meta-phase), even though the L3>L1 rotation is identity-in-form, the L3 reader must find `scal` defined in L3 vocabulary at L3. This dispatch lands `book/src/L3/scal.md` using L3 vocabulary (whole-tensor field operation, no element-loop exposed, reduction-free, rank-local), updates the L3 dep-map in `book/src/L3/index.md` to add the row, and proposes the SUMMARY chapter entry.

The signature is the value-threaded pure form. Semantics narrate `scal` at L3 — element-wise scalar multiplication over the length axis with no cross-element coupling, no MPI collective, no iteration view (it is a single whole-tensor field op, not a step body). Algebraic laws are the nine that hold at L1, inherited unchanged (the rotation is identity-in-form). Variant axes are the same two as L1 (element-type, scalar-promotion sub-axis). The **Lifts from** section explicitly notes the L1 form is value-thread-isomorphic to this L3 form; the lowering theme is identity, captured as a thin in-line note (no `L3-L1/` directory exists per the cycle-010 audit OQ; this entry inherits the wave-1 precedent of capturing the identity rotation in the L3 entry itself, pending a layer-intro-author policy decision).

## Proposed changes

```edit:book/src/L3/scal.md
---
layer: L3
operator: scal
firmness: firm
lowers_to:
  - book/src/L1/scal.md (identity-in-form; no `L3-L1/` directory yet — identity rotation noted in-line at "Lifts from")
lifts_from:
  - book/src/L1/scal.md (value-thread-isomorphic; same signature shape; whole-tensor by construction)
variant_axes:
  - element-type (real / complex)
  - scalar-promotion (real-α-against-complex-x via concepts/scalar-promotion)
---

# scal

Vector-scalar multiplication as a whole-tensor field operation at L3 — the **iteration-rotation** rendering of `y ← α·y`. Consumes a scalar `α` and a tensor `x`; produces a fresh tensor of the same length axis whose every element is `α` times the corresponding input element. Companion to L1 [`scal`](../L1/scal.md) (the mutation-lifted form of the same primitive); the rotation L1 → L3 is identity-in-form because the signature exposes no element loop.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `scal` at L3 is the whole-tensor form of vector-scalar multiplication — a single field operation parameterised by a scalar `α` and acting pointwise over the length axis. The operator carries **no iteration view at L3** (it is a leaf primitive, not a step body) and **no sequential obstruction** (every element is independent of every other element under the per-element scalar multiplication).

The relationship to L1 is captured by an **identity-in-form** rotation:

- **Downward** to L1: the L3 form's signature `Scalar -> Tensor[N] -> Tensor[N]` is textually identical to the L1 form's signature; both forms describe pure-functional vector-scalar multiplication with no destination buffer in the signature, no per-element loop visible, no reduction, no MPI collective at the L1 / L3 surface. The L3 → L1 rotation is the identity on the primitive itself. The framing differs: L1 frames `scal` as the *mutation-rotation* image of the L0 receiver-mutating `mfem::Vector::operator*=` / `ComplexVector::operator*=` member-method idiom (the L1 surface drops the destination-buffer mention); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. **The body of `scal` is the identity rotation across this edge.**

This L3 entry is the layer-coherence anchor: a reader at L3 can find `scal` here, in L3 vocabulary, without having to reach down to L1 to recover the field-operation shape. The backfill is the cycle-011 wave-1 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification) on the BLAS-1 cohort, following the wave-1 `krylov-step` L3 backfill precedent (cycle-010). The cross-layer-cross-cutter audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`) HIGH CONFIDENCE recommendation for the BLAS-1 bundle is the load-bearing dispatch rationale: the L3 index (`book/src/L3/index.md:11-14`) already advertises `axpy / dot / nrm2` as whole-tensor field operations, and the seven L1 primitives are explicitly named L3-native by signature shape in the firm L3>L2 body-identity theme (`book/src/L3-L2/krylov-step-body-identity.md:97`). `scal` is the standalone leaf of that bundle; this dispatch closes its L3 entry.

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

The operator is **pure at L3**: the prior `x` and the result are distinct values; the L0 source overwrites the in-place destination buffer via the L1>L0 lowering ([`L1-L0/`](../L1-L0/) — no firm `scal-mutation-rotation` theme yet exists; the L1 entry sketches the lowering content in §"L1 vs L0 distinction" and §Evidence). At L3 the relationship is purely algebraic.

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

- `scal(α, x) = axpby(α, x, 0, y) = axpby(0, y, α, x)` for any `y`, per `axpby` laws 2 and 3 at `book/src/L1/axpby.md`. The subsumption is inherited from L1; at L3, once the sibling `axpby` entry lands (wave-1 dispatch #2 — `book/src/L3/axpby.md`), it will also be a leaf whole-tensor primitive. `scal` stays in the L3 dep-map as a sibling, not a sub-operation of `axpby` (per the harvester decision at `scaffolding/decisions/axpby-as-primitive.md`).
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

L3 `scal` lowers to L1 [`scal`](../L1/scal.md) via an **identity-in-form** rotation: the signature `Scalar -> Tensor[N] -> Tensor[N]` is textually identical at both layers; the body is the same whole-tensor field operation. No `L3-L1/` directory exists in the artifact (the cycle-010 audit OQ `l3-l1-directory-naming-structure-policy` tracks the broader policy question of whether identity L3>L1 rotations get thin sibling themes or in-line notes); per the wave-1 `krylov-step` L3 backfill precedent this entry captures the identity rotation in-line. The L0 in-place mutation is reintroduced at the L1>L0 lowering (no firm `scal-mutation-rotation` theme yet; the L1 entry sketches the content in its §"L1 vs L0 distinction" and §Evidence).

## Lifts from

L1 `scal` lifts to this L3 entry via the **value-thread-isomorphic** identity rotation: the L1 form's signature has no element loop exposed, no destination buffer, no MPI collective, no iteration view — these are exactly the properties that make it L3-native by construction. The cross-layer-cross-cutter audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) `axpy` / `axpby` / `axpbypcz` / `dot` / `nrm2` / `scal` (the BLAS-1 cohort)") HIGH CONFIDENCE recommendation classifies the rotation as identity-in-form, citing the firm L3>L2 body-identity theme's line 97 ("each L1 primitive is *also* L3-native because its signature has no per-element loop visible") and the firm L4>L3 typed-wrapper-dissolution theme's line 68 (which renders the BLAS-1 primitives in the L3 body let-chain identically to L1). **This L3 entry exists for layer-coherence reasons** — a reader navigating L3 must find `scal` defined in L3 vocabulary, not have to reach down to L1 to recover the field-operation shape.

The wave-1 `krylov-step` L3 backfill (`book/src/L3/krylov-step.md`, cycle-010) is the structural precedent: identity-in-form rotation on the body, layer-coherence backfill, methodology invariant enacted. The BLAS-1 cohort (this dispatch + the three sibling dispatches in cycle-011 wave-1) is the broader enactment per the audit's recommendation.

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
```

```edit:book/src/L3/index.md
# L3 — Global tensor-field operations

L2 algebraic decompositions re-expressed as global tensor-field / convolution-over-space operations: whole-tensor ops, no element loops. The **iteration rotation** layer.

## Context

Where the L2 algebra admits a global form, L3 captures it. Where no global form exists (Gauss-Seidel-flavored smoothers, certain triangular solves, sequentially-reordered preconditioners), the **obstruction** is recorded as a first-class output — negative L3 results are part of the deliverable.

## Semantics (overlay)

L3 expresses:
- Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)
- Field transitions: state evolution over a single algorithmic step expressed as `state' = f(state, params)`
- Convolution-like patterns where applicable (stencil sweeps, restriction/prolongation)
- Sequential obstructions: explicit markers where global form is unavailable, with reason

## Operator dep-map

| Operator | Signature | Dependencies | Lowers to | Status |
|---|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | Form A: `(op, K, s) -> (K', s', outputs)`. Form B: `krylov-step-first :: (op, K, s) -> (K', s', carry, outputs)` + `krylov-step-steady :: (op, K, s, carry) -> (K', s', carry', outputs)`. | L1 primitives (used as L3-native whole-tensor ops): `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`. Concepts: `sequential-obstruction`, `state-stratification`, `derived-view-hoisting`, `variant-absorption`, `first-iteration-unrolling`, `convergence-test`, `solve-monad`, `apply_BA`, `orthogonalization`. L4 lift via `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (identity-in-form on body). | L2 [`krylov-step`](../L2/krylov-step.md) via [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) (identity-in-form on body; surface adjustments consolidate `(K, s)` into `IterState`). | `firm` (harvested cycle-010T215300Z; first firm L3 operator; identity-lowering backfill per CLAUDE.md §Methodology invariants — supersedes cycle-006 "no L3 row needed" verdict) |
| [`scal`](./scal.md) | `scal :: Scalar -> Tensor[N] -> Tensor[N]` (`α, x → α·x`) | (leaf; sibling-subsumed by `axpby` β=0). Concepts: `scalar-promotion`. L1 lift via identity-in-form rotation (signature is identical; whole-tensor field operation by construction). | L1 [`scal`](../L1/scal.md) via identity-in-form rotation (no `L3-L1/` directory yet; noted in-line). | `firm` (harvested cycle-011 wave-1 #4; BLAS-1 cohort identity-lowering backfill per CLAUDE.md §Methodology invariants and cycle-010 cross-layer-cross-cutter HIGH CONFIDENCE recommendation) |

## Working Notes

- This layer is the destination of the L2-L1 lowering pipeline output AND the source for L4-L3 lowering verification.
- `concepts/sequential-obstruction.md` is the canonical write-up of when L3 lifts fail.
- **First firm L3 operator landed cycle-010**: `krylov-step` (identity-lowering backfill per CLAUDE.md §Methodology invariants new bullet **Identity-lowerings still require both L levels**, codified cycle-009 meta-phase). The L3 form is value-thread-isomorphic to the L4 body per the L4>L3 typed-wrapper-dissolution theme; the entry exists for layer-coherence reasons — each layer is coherent within itself, and the L3 reader must find `krylov-step` defined in L3 vocabulary. Supersedes cycle-006 audit verdict "no L3 row needed for krylov-step".
- **Cohort growth in flight (cycle-011 wave-1)**: per priority #20 cross-layer-cross-cutter audit (cycle-010), the BLAS-1 cohort (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) is being backfilled at L3 across 4 parallel harvester dispatches. `scal` landed in dispatch #4 (this row); sibling rows for `apply_linop`, the linear-update family (`axpy` / `axpby` / `axpbypcz`), and the reduction family (`dot` / `nrm2`) land via dispatches #1–#3 of the same wave. All four are identity-in-form rotations from L1 — the L3 form's signature is textually identical to L1 because the L1 signatures already expose no element loop. The framing rotates from "mutation rotation against L0 source" (L1) to "field operation in the iteration-rotation layer's vocabulary" (L3); no operational adjustment occurs across the rotation.
- **Cohort growth candidates (cycle-012+)**: other operators in the artifact (`ksp_solve`, `eigsolve`) may eventually warrant L3 placement, but their rotations are NOT identity-in-form (they would carry substantive outer-driver / partial-convergence content). These are tracked separately under the cross-layer-cross-cutter audit's "MEDIUM CONFIDENCE" / "DEFER" findings and routed through future planner cycles.
- **OQ `l3-l1-directory-naming-structure-policy`** (cycle-010): the BLAS-1 cohort backfills capture their identity-in-form L3>L1 rotations in-line at the L3 entry (in the "Lowers to" / "Lifts from" sections), pending a layer-intro-author policy decision about whether thin `L3-L1/` identity themes are warranted. The wave-1 `krylov-step` L3 backfill set this precedent.
```

```edit:book/src/SUMMARY.md
# Summary

[Introduction](./introduction.md)
# Methodology
- [Overview](./methodology/overview.md)
# L4 — Graph-Evaluation Calculus
- [Overview](./L4/index.md)
- [krylov-step](./L4/krylov-step.md)
- [iterate-while](./L4/iterate-while.md)
- [iterate-while-with-prev](./L4/iterate-while-with-prev.md)

# L4 > L3 — Lowering
- [Overview](./L4-L3/index.md)
- [krylov-step-typed-wrapper-dissolution](./L4-L3/krylov-step-typed-wrapper-dissolution.md)
- [gmres-inner-loop-iterate-while-migration](./L4-L3/gmres-inner-loop-iterate-while-migration.md)

# L3 — Global Tensor-Field Operations
- [Overview](./L3/index.md)
- [krylov-step](./L3/krylov-step.md)
- [scal](./L3/scal.md)

# L3 > L2 — Lowering
- [Overview](./L3-L2/index.md)
- [krylov-step-body-identity](./L3-L2/krylov-step-body-identity.md)

# L2 — Algebraic Decompositions
- [Overview](./L2/index.md)
- [krylov-step](./L2/krylov-step.md)

# L2 > L1 — Lowering
- [Overview](./L2-L1/index.md)

# L1 — Mutation-Lifted Forms
- [Overview](./L1/index.md)
- [axpy](./L1/axpy.md)
- [dot](./L1/dot.md)
- [nrm2](./L1/nrm2.md)
- [axpby](./L1/axpby.md)
- [scal](./L1/scal.md)
- [apply_linop](./L1/apply_linop.md)
- [axpbypcz](./L1/axpbypcz.md)
- [ksp_solve](./L1/ksp_solve.md)
- [eigsolve](./L1/eigsolve.md)
- [matrix-weighted-norm](./L1/matrix-weighted-norm.md)
- [bilinear-form](./L1/bilinear-form.md)

# L1 > L0 — Lowering
- [Overview](./L1-L0/index.md)
- [axpby-mutation-rotation](./L1-L0/axpby-mutation-rotation.md)
- [axpbypcz-mutation-rotation](./L1-L0/axpbypcz-mutation-rotation.md)
- [apply-linop-mutation-rotation](./L1-L0/apply-linop-mutation-rotation.md)
- [ksp-solve-mutation-rotation](./L1-L0/ksp-solve-mutation-rotation.md)
- [bicgstab-iteration](./L1-L0/bicgstab-iteration.md)
- [minres-iteration](./L1-L0/minres-iteration.md)
```

**Integrator note for SUMMARY.md edit**: the proposed-changes block above shows the section for the L3 chapter additions only — the rest of the file (L0 sections, Phase 1 corpus, Concepts, Design Artifacts, Meta-Reviews) is unchanged. The integrator should apply only the single-line insertion `- [scal](./L3/scal.md)` after the existing `- [krylov-step](./L3/krylov-step.md)` line at the L3 — Global Tensor-Field Operations Part, after the wave-1 sibling dispatches (#1 apply_linop, #2 axpy/axpby/axpbypcz, #3 dot/nrm2) have added their own chapter entries. Wave-1 chapter ordering convention: parallel to the L1 ordering (apply_linop, axpy, dot, nrm2, axpby, scal, apply_linop, axpbypcz), but since wave-1 lands these four dispatches in parallel, the integrator should adopt the order of dispatch IDs (#1 apply_linop, #2 axpy/axpby/axpbypcz, #3 dot/nrm2, #4 scal) — placing `scal` last in the L3 BLAS-1 cohort. If an alternative ordering is preferred (e.g., grouping by algebraic family), the integrator may reorder, but the precondition is only that `scal` appears in the L3 Part.

## Supporting evidence

**Direct read of:**

- `book/src/L1/scal.md` — firm L1 entry; source of body shape, signature, semantics, algebraic laws, variant axes, and L0 evidence chain for the L3 entry.
- `book/src/L3/krylov-step.md` — firm L3 entry (cycle-010 wave-1 backfill); the structural precedent for this L3 entry's framing (layer-coherence anchor, identity-in-form rotation, methodology invariant enacted).
- `book/src/L3/index.md` — current state with one operator row; updated to add the `scal` row.
- `book/src/L3-L2/krylov-step-body-identity.md:97` — explicit naming of the seven L1 primitives (including `scal`) as L3-native by signature shape.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:68` — L3 body let-chain rendering `scal` identically to L1.
- `book/src/concepts/scalar-promotion.md` — typing rule for the scalar-promotion sub-axis; backlinked from §Variant axes.
- `book/src/concepts/scal.md` — cross-cutting prose treatment; consistent with the L3 entry's framing.
- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` — HIGH CONFIDENCE backfill recommendation identifying `scal` as a BLAS-1 bundle backfill candidate.

**Wave-1 sibling dispatch awareness:**

- Sibling dispatch #1 (`reports/2026-05-27T234502Z-harvester-l3-apply-linop/`) is authoring `book/src/L3/apply_linop.md` in parallel.
- Sibling dispatch #2 (`reports/2026-05-27T234525Z-harvester-l3-blas1-linear-update-cohort/`) is authoring the linear-update family (`axpy` / `axpby` / `axpbypcz`).
- Sibling dispatch #3 (reduction family `dot` / `nrm2`; report ID not yet visible in this dispatch's working set) is authoring those entries.
- This dispatch (#4) is the standalone leaf `scal`. The four dispatches share the same rotation rationale (identity-in-form from L1, layer-coherence anchor at L3, methodology invariant enacted) and structurally mirror the wave-1 `krylov-step` L3 backfill precedent.

**MCP codemap tool usage**: this dispatch did **not** invoke `mcp__palace-codemap__*` tools — the L3 entry is value-thread-isomorphic to L1 by construction (identity-in-form rotation), and the L0 evidence chain is fully captured in the L1 entry's §Evidence (which this L3 entry cites transitively rather than re-walking the Palace source). No fresh L0 line-range verification was needed for the rotation to L3. If a future refinement adds substantive L3 content beyond the L1 rendering (which would no longer be identity-in-form), MCP codemap usage would be warranted.

## Open questions / caveats

1. **`L3-L1/` directory does not exist.** Per the cycle-010 cross-layer-cross-cutter audit's Open Question 1, the broader policy question of whether identity L3>L1 rotations get thin sibling themes (in a hypothetical `book/src/L3-L1/` directory) or are captured in-line at the L3 entry remains unresolved. This dispatch follows the wave-1 `krylov-step` L3 backfill precedent of capturing the identity rotation in-line; the layer-intro-author role spec would benefit from a per-cycle policy decision. **Forwarded to cycle-011 finalize / cycle-012 meta-phase**: if multiple BLAS-1 cohort backfills land in cycle-011 wave-1, the count of identity L3>L1 rotations grows from 1 (wave-1 krylov-step had no L3>L1 rotation since L1 has no `krylov-step` entry) to 4+ (this wave's BLAS-1 cohort), and the policy question's pressure increases.

2. **Sibling dispatch coordination on `book/src/L3/index.md`.** All four wave-1 BLAS-1 cohort dispatches will propose adding rows to the L3 dep-map and chapter entries to `book/src/SUMMARY.md`. The integrator-per-report serial dispatch pattern (CLAUDE.md §Phase 5) ensures these edits compose correctly when applied one at a time, but the per-dispatch edit diffs may conflict at the table-edit level. **This dispatch's edit assumes the integrator can merge multiple row-insertion proposed-changes into the same L3 index file**; if conflicts arise, the integrator may need to retry or reorder.

3. **`SUMMARY.md` ordering convention.** This dispatch proposes inserting `- [scal](./L3/scal.md)` immediately after the existing `- [krylov-step](./L3/krylov-step.md)` line in the L3 Part. The wave-1 sibling dispatches (#1–#3) will also propose insertions. The integrator should adopt a conventional ordering (alphabetical, or matching the L1 ordering); this dispatch is agnostic.

4. **No firm `scal-mutation-rotation` L1>L0 theme.** The L1 entry sketches the L1>L0 lowering content in §"L1 vs L0 distinction" and §Evidence (the in-place mutation, the real-imag-shape branch erasure, the `Normalize` fused construct), but no firm `book/src/L1-L0/scal-mutation-rotation.md` theme exists. The L3 entry's `Lowers to` chain (L3 → L1 → L0) therefore reaches firm coverage only down to L1; the L1 → L0 hop is currently informal. This is **not a new gap** introduced by this dispatch — the same gap exists at L1. Forwarded as a watch-list item for future cycle planners (analogous to the firm `axpby-mutation-rotation` and `axpbypcz-mutation-rotation` themes that have already landed at L1>L0).

5. **`scal` is not advertised by name in `book/src/L3/index.md:11-14`'s vocabulary inventory.** The current L3 index lists "matvec, axpy, dot, nrm2 as field operations" as L3 vocabulary; `scal` is implied by the BLAS-1-cohort reading and by the firm L3>L2 body-identity theme's line 97, but not literally named. This dispatch does not update the L3 index's §"Semantics (overlay)" prose to add `scal` to the inventory — the dep-map row addition is sufficient for the layer-coherence anchor. A future layer-intro-author refresh dispatch may want to bring the §"Semantics (overlay)" prose into line with the dep-map; flagged for cycle-012+ planner.

6. **Frontmatter convention.** This L3 entry inherits the 6-field YAML frontmatter convention from the wave-1 `krylov-step` L3 backfill (which introduced the convention as the first L_n entry to carry frontmatter). The cycle-011 wave-1 BLAS-1 cohort adopts the same convention. **Future-normalization candidate**: cycle-012 meta-phase may want to codify the frontmatter convention as a per-layer policy or extend it to L1/L2/L4 entries; this dispatch defers that decision.
