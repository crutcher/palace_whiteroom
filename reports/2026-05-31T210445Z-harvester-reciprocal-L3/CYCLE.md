---
agent: harvester
invoked_at: 2026-05-31T210445Z
scope: L3 operator: reciprocal
status: integrated
integrated_at: 2026-05-31T235900Z
integration_commit: 14e80a66a8e0d6ac68c3fd4a2d3602b0b2d3e239
integration_notes: "Applied clean cycle-038 (D1). NEW firm L3 book/src/L3/reciprocal.md (12th firm L3, elementwise multiplicative-inverse self-map) + SUMMARY + L3-index dep-map row. Enacts an (A) identity-in-form backfill of the c036 D2 audit verdict. Finalize reconciled the L3-index Working-Notes firm-count tally to 14 firm + 2 partial-obstruction (only normalize remaining (A), cycle-039 closer)."
inputs:
  - book/src/L1/reciprocal.md (firm L1 home; cycle-pre-037)
  - book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md (firm L1>L0 leaf-mutation theme; verified_against block added cycle-037)
  - book/src/L3/scal.md, book/src/L3/assemble-diagonal.md, book/src/L3/jacobi-smoother.md (freshest L3 identity-row templates; the thinnest-identity-row form)
  - book/src/L3/index.md:41 (cycle-036 D2 L3-cohort-growth audit — `reciprocal` named one of the six (A) firm identity-in-form backfills)
  - book/src/L3/apply_linop.md, book/src/L3/dot.md, book/src/L3/nrm2.md (sibling identity-in-form precedents)
  - OQ l3-cohort-growth-audit-c036-verdict
---

# CYCLE: Formalize reciprocal at L3

## Summary
Backfill the L3 (iteration-rotation layer) entry for `reciprocal` — the elementwise multiplicative-inverse self-map `result[i] = 1/x[i]`, the firm L1 leaf consumed by the diagonal-preconditioner-apply chain (`assemble_diagonal → reciprocal → elementwise_product`) of the Jacobi/Chebyshev smoothers and by the FE-assembly multiplicity-averaging step. The L1 home (`book/src/L1/reciprocal.md`) is firm; this dispatch is one of the six **(A) identity-in-form** L3 backfills mandated by the cycle-036 D2 L3-cohort-growth audit (`book/src/L3/index.md:41`, OQ `l3-cohort-growth-audit-c036-verdict`). The rotation L1→L3 is **identity-in-form**: the L1 signature `Tensor[N] -> Tensor[N]` exposes no element loop, no reduction, no MPI collective, no cross-element coupling — every output element depends on exactly one input element — so it is L3-native by signature shape, value-thread-isomorphic to its L1 form. The iteration rotation is therefore identity-in-form: a per-element self-map with **no loop-recurrence obstruction**, embarrassingly parallel and GPU-friendly (the sharpest contrast with the `chebyshev`/`eigsolve` `partial-obstruction` rows). The entry lands `firm` per the firm-on-positive-structure precedent (`apply_linop` / `assemble-diagonal`): the eight algebraic laws are syntactic identities on the fully-read complex-elementwise kernel (`palace/linalg/vector.cpp:248-261`), so the absent dedicated `Reciprocal` test does not gate firm. The L0 mutation, the partiality (`x[i] ≠ 0` no-zero-guard), and the complex `s = 1/|z|²` factoring are L1>L0 concerns (the firm `reciprocal-elementwise-product-mutation-rotation` theme), not L3 concerns.

## Proposed changes

```new:book/src/L3/reciprocal.md
---
layer: L3
operator: reciprocal
firmness: firm
lowers_to:
  - book/src/L1/reciprocal.md (identity-in-form on the primitive's signature; no L3-L2 entry, no L3-L1 theme — identity rotation noted in-line at "Lowers to")
lifts_from:
  - book/src/L1/reciprocal.md (value-thread-isomorphic; same signature shape; whole-tensor by construction — no L4 entry, leaf elementwise primitive)
variant_axes:
  - element-type (real | complex; collapsed to a single parameterised operator)
---

# reciprocal

Elementwise **multiplicative-inverse** as a whole-tensor field operation at L3 — the **iteration-rotation** rendering of `result[i] = 1/x[i]`. Consumes a tensor `x`; produces a fresh tensor of the same length axis whose every element is the field-multiplicative-inverse of the corresponding input element. Companion to L1 [`reciprocal`](../L1/reciprocal.md) (the mutation-lifted form of the same `Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method pair); the rotation L1 → L3 is identity-in-form because the signature exposes no element loop. The elementwise leaf that, composed with [`assemble-diagonal`](./assemble-diagonal.md), produces the inverse diagonal `D⁻¹` consumed by the diagonal-preconditioner-apply chain (Jacobi, Chebyshev) at the iteration-rotation layer.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, with no element loop exposed at the layer's vocabulary and with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `reciprocal` at L3 is the whole-tensor form of the elementwise multiplicative-inverse — a single field operation acting pointwise over the length axis `N`. The operator carries **no iteration view at L3** (it is a leaf primitive, not a step body) and **no sequential obstruction** (every output element depends on exactly one input element; there is no cross-element recurrence to obstruct).

Unlike the linear BLAS-1 cohort (`axpy`, `scal`, `dot`, `nrm2`), `reciprocal` is a **nonlinear** elementwise map (`1/(a+b) ≠ 1/a + 1/b`) — but it shares the cohort's defining L3 shape: vector-in / vector-out, element-local, reduction-free, rank-local. Like [`scal`](./scal.md) it is a leaf whole-tensor field operation with no inner structural sub-composition; unlike `scal` it is partial (`reciprocal(x)` is defined only where `x[i] ≠ 0`).

The relationship to L1 is captured by an **identity-in-form** rotation:

- **Downward** to L1: the L3 form's signature `Tensor[N] -> Tensor[N]` is textually identical to the L1 form's signature; both forms describe pure-functional elementwise reciprocation with no destination buffer in the signature, no per-element loop visible, no reduction, no MPI collective at the L1 / L3 surface. The L3 → L1 rotation is the identity on the primitive itself. The framing differs: L1 frames `reciprocal` as the *mutation-rotation* image of the L0 receiver-self-overwriting `mfem::Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method idiom (the L1 surface drops the receiver-mutation mention); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. **The body of `reciprocal` is the identity rotation across this edge.** There is **no interposed L2 entry and no `L3-L2`/`L3-L1` theme file** — the rotation carries no algebraic novelty, mirroring the BLAS-1 / `apply_linop` / `assemble-diagonal` L3>L1 discipline. The identity-in-form annotation lives in-line here, per the cycle-012 non-adjacent-identity convention (precedent: `scal`, `dot`, `apply_linop`, `assemble-diagonal`); no non-adjacent lowering directory is created. The **substantive** rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme.

- **Upward** to L4: there is **no standalone L4 entry** for `reciprocal`. It is a leaf elementwise primitive carrying no monadic effect, no state-stratification typing, no novel calculus content at L4 — the same `CONFIRMED-NOT-NEEDED` verdict the cycle-010 cross-layer audit reached for the BLAS-1 cohort, `apply_linop`, and `assemble-diagonal`. At L4 it appears (where consumed) inside operator bodies as a let-binding feeding the diagonal-preconditioner-apply chain, not as first-class L4 vocabulary.

This L3 entry is the **layer-coherence anchor**: a reader navigating L3 (the iteration-rotation layer that composes whole-tensor primitives into smoother / preconditioner bodies) can find `reciprocal` here, in L3 vocabulary, without having to reach down to L1 to recover the field-operation shape. The backfill is the cycle-038 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:41`): `reciprocal` is listed as the "elementwise self-map" member of the six firm (A) backfills, alongside the cycle-037-landed `assemble-diagonal` and `jacobi-smoother`.

## Signature

    reciprocal :: Tensor[N] -> Tensor[N]
    reciprocal x = (\i -> 1 / x[i])   for i in [0, N)

Shape contract (bunsen-style, named axes; positional values, no monadic effect, no destination buffer):

- **`x`** — `Tensor[N]` — the input tensor with a single length axis `N`. Read-only at L3 (the L3 form is pure; the L0 receiver self-overwrite is reintroduced only at the L1>L0 lowering).
- **result** — `Tensor[N]` — same axis `N` as `x`; same element type as `x`. Every output element equals the field-multiplicative-inverse of the corresponding input element. The result element type **tracks** the input element type (real `x` → real result; complex `x` → complex result) — unlike [`nrm2`](./nrm2.md), which collapses both to a real-valued result. `reciprocal` is a self-map on the vector type's element field.

**Precondition (partiality).** `reciprocal(x)` is defined only at indices `i` where `x[i] ≠ 0`. The L0 source carries **no zero-guard** (the complex body computes `s = 1.0 / (XR[i]² + XI[i]²)` unconditionally; the real upstream `mfem::Vector::Reciprocal()` divides without runtime check). At L3 the operator is **partial**: undefined wherever `x[i] = 0`; the no-zero-guard policy lifts as a precondition on the input (callers must ensure `x[i] ≠ 0 ∀ i`), recorded in the same form as [`normalize`](../L1/normalize.md)'s `x ≠ 0` precondition. Consumer call sites preclude zero by precondition (the Jacobi/Chebyshev consumers require `diag(A) > 0`, the SPD assumption) or by construction (the FE-assembly `test_multiplicity` is `≥ 1` per active dof). The partiality is the L3 reflection of the L0 no-zero-guard policy; it is **not** a variant axis and **not** a sequential obstruction — it is a precondition on the input domain.

The L3 signature is **identical to the L1 signature** modulo notation; the rotation is identity-in-form. No L4 wrapper machinery is needed at L3: `reciprocal` is a leaf field operation, not a step body, and the L4 monadic / typed-record / `readonly`-typing apparatus (which serves wrapper-bearing operators like `krylov-step`) does not apply to leaf primitives — the same discipline the L3 `scal`, `apply_linop`, and `assemble-diagonal` entries record.

## Semantics

`reciprocal` at L3 is a single whole-tensor field operation: a value-threaded transformation `x -> y` where `y[i] = 1 / x[i]` for every element index `i ∈ [0, N)`. The operator is **element-local** (every output element depends on exactly one input element), **reduction-free** (no cross-element communication), and **rank-local** (no MPI collective at any layer; ranks own disjoint slices of `N` and apply the reciprocation independently).

At L3 the operator carries **no iteration view** — it is not a step body; the iteration-rotation layer composes whole-tensor primitives like `reciprocal` into step / setup bodies (e.g. the Jacobi smoother's setup chain `dinv = assemble_diagonal(A); dinv = reciprocal(dinv)`). The whole-tensor field-operation framing is what the L3 index (`book/src/L3/index.md:12`) calls a "field operation" — the L3 vocabulary's primitive shape, with no element-loop exposed.

The operator is **pure at L3**: the prior `x` and the result are distinct values; the L0 source overwrites the in-place receiver `*this` via the L1>L0 lowering ([`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md), firm). At L3 the relationship is purely algebraic.

The body has **no structural sub-composition** — `reciprocal` is a leaf primitive, so the L3 form does not decompose into other L3 primitives. The five primitive groups a wrapper-bearing operator like `krylov-step` has (operator-apply, optional auxiliary, iterate-and-scalar update, output readout, counter increment) have no analog here: `reciprocal`'s body is one whole-tensor field operation.

**Element-type semantics.** For real `x`, the reciprocal is the field-multiplicative-inverse `1/x[i]` in `ℝ`. For complex `x`, the reciprocal is `1/z = z̄/|z|²` in `ℂ` — the closed-form complex multiplicative-inverse `1/(a + bi) = (a − bi)/(a² + b²)`. The complex closed-form decomposition is recorded as a law (law 5 below), not as a variant — the same elementwise map in both fields. The L0 complex kernel realises `1/z = z̄/|z|²` via the intermediate squared modulus `s = 1/|z|²` (`palace/linalg/vector.cpp:257-259`); the intermediate is a transparent factoring of the closed form, not an L3 sub-operator.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `reciprocal`'s iteration view is **degenerate**: `reciprocal` is a leaf primitive, not a step body, so the operator carries no iteration view of its own. It composes into setup / step bodies (e.g. the `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup chain inside the Jacobi/Chebyshev smoother bodies) where the surrounding kernel carries the iteration view; the `reciprocal` call site itself is a single whole-tensor field operation. There is **no sequential obstruction** in `reciprocal` — every element is independent of every other element under the per-element reciprocation; the operator is embarrassingly parallel and fully GPU-friendly. This is the structural distinction from the `partial-obstruction` L3 operators ([`chebyshev`](./chebyshev.md), [`eigsolve`](./eigsolve.md)), whose bodies lift but whose loops do not: `reciprocal` has no loop to obstruct. It is one of the layer's clean whole-tensor field operations.

The partiality (`x[i] ≠ 0`) is **not** an obstruction: it is a precondition on the input domain, not an un-liftable loop. The L0 no-zero-guard (`1/0 → ±∞ → NaN`) is the source realisation of a partial map, reintroduced at the L1>L0 lowering, not an L3 sequencing concern.

## Algebraic laws

The eight laws that hold at L1 (per `book/src/L1/reciprocal.md` §"Algebraic laws") transport **unchanged** to L3, because the L3 form is value-thread-isomorphic to the L1 form. These are properties of the elementwise multiplicative-inverse map. The laws are reproduced here so the L3 reader does not have to reach to L1 for the listing; they are stated where the relevant elements are nonzero (the operator's precondition), and the partiality is recorded once (above) and not re-stated per law.

1. **Involution (where defined)**: `reciprocal(reciprocal(x)) = x`, provided every `x[i] ≠ 0` (so the intermediate vector also has no zero entries). The composition of multiplicative-inverse with itself is the identity on the multiplicative group of the element field (`ℝ*` or `ℂ*`). Witnessed by the closed-form `1/(1/z) = z` from the complex body's `(a−bi)/(a²+b²)` formula.
2. **Multiplicative-inverse identity (per element)**: `x[i] · reciprocal(x)[i] = 1` for every `i` where `x[i] ≠ 0`. The defining identity of the multiplicative inverse, applied pointwise. Composed with the `elementwise_product` primitive it yields the all-ones vector: `elementwise_product(x, reciprocal(x)) = 𝟙`.
3. **Scalar-factor distribution**: `reciprocal(scal(α, x)) = scal(1/α, reciprocal(x))` for any nonzero scalar `α`. The reciprocal of a uniformly-scaled vector is the inverse-scaled reciprocal — pointwise `1/(α·x[i]) = (1/α)·(1/x[i])`. This is the law that makes `reciprocal` compose cleanly with [`scal`](./scal.md): `(reciprocal ∘ scal(α)) = (scal(1/α) ∘ reciprocal)`.
4. **Multiplicative-distributivity (over the elementwise product)**: `reciprocal(elementwise_product(x, y)) = elementwise_product(reciprocal(x), reciprocal(y))` for `x[i], y[i] ≠ 0` everywhere. The reciprocal of an elementwise product is the elementwise product of reciprocals — pointwise `1/(x[i]·y[i]) = (1/x[i])·(1/y[i])`.
5. **Complex closed-form (complex element-type only)**: for complex `x`, `reciprocal(x)[i] = conj(x[i]) / |x[i]|²` where `|·|²` is the squared modulus. Equivalently `1/(a + bi) = (a − bi)/(a² + b²)`. The L0 kernel realises it verbatim (`palace/linalg/vector.cpp:257-259`).
6. **Conjugate–reciprocal commutation (complex)**: `reciprocal(conj(x)) = conj(reciprocal(x))` for complex `x ≠ 0`. The complex conjugate commutes with the reciprocal: `1/conj(z) = conj(1/z)`. Pointwise consequence of law 5.
7. **Identity on the all-ones input**: `reciprocal(𝟙) = 𝟙` where `𝟙` is the all-ones vector of axis `N`. Pointwise `1/1 = 1`. The fixed point of the operator.
8. **Negation factor**: `reciprocal(scal(−1, x)) = scal(−1, reciprocal(x))` for nonzero `x`. Pointwise `1/(−x[i]) = −(1/x[i])`. Special case of law 3 with `α = −1`.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Total definedness**: the operator is **partial** — `reciprocal(0)` is undefined (division by zero). The L0 kernel produces `NaN` / `±∞` rather than a clean error. Recorded as a precondition on the input rather than an algebraic law that fails.
- **Linearity in `x`**: `reciprocal(x + y) ≠ reciprocal(x) + reciprocal(y)` in general. `1/(a+b)` is not `1/a + 1/b` — the reciprocal is a **nonlinear** elementwise map. This is the defining feature distinguishing it from the linear BLAS-1 leaves ([`axpy`](./axpy.md), [`scal`](./scal.md), [`axpby`](./axpby.md), [`axpbypcz`](./axpbypcz.md)) at L3.
- **Bit-level involution under finite precision**: law 1 holds exactly in `ℝ` / `ℂ` but is approximate at IEEE-754 — a round-trip `1/(1/x[i])` rounds twice and may differ from `x[i]` by a few ULPs. Transparent-trick consideration; not load-bearing for the Jacobi/Chebyshev consumers (which use the *intermediate* `D⁻¹` directly, never round-trip).
- **Bit-level distributivity under finite precision**: laws 3, 4 hold exactly in `ℝ` / `ℂ` but the two sides round differently in IEEE-754. Algebraically equal, bit-pattern not. Transparent-trick; not load-bearing.
- **Closed-form unification of real and complex**: law 5 is recorded in complex-specific form because the complex kernel realises `1/z = z̄/|z|²` as a non-trivial `s = 1/(XR²+XI²); XR *= s; XI *= -s` decomposition (`palace/linalg/vector.cpp:257-259`); it degenerates to the trivial `1/x` in `ℝ` but is not stated in unified form (the unified statement would erase the non-trivial complex decomposition the kernel realises).

The law set and non-law set are **inherited unchanged** from L1; the L3 rendering introduces no new laws or non-laws. This is what makes the L3>L1 hop identity-in-form on the primitive's signature: not only does the signature transport unchanged, the entire algebraic profile transports unchanged.

## Dependencies

**Same-layer (L3)**: none. `reciprocal` is a **leaf elementwise primitive** at L3 just as it is at L1 — element-local, reduction-free, single-tensor argument, no cross-element coupling, no decomposition into other L3 whole-tensor primitives. Its sub-operation is scalar reciprocation (`1/x` in the element field), below the L3 layer's resolution (a deterministic IEEE-754 primitive for both real and complex). The intermediate scalar `s = 1/|z|²` in the complex body is a transparent factoring of the closed form `z̄/|z|²`; it does not surface as an L3 sub-operator.

**Sibling on the elementwise-primitives axis (not dependency)**:

- `elementwise_product` — the binary elementwise multiply (`(x, y) -> x ⊙ y`); an **(A) firm L3 backfill candidate** per the cycle-036 D2 audit (`book/src/L3/index.md:41`), not yet authored at L3 — referenced here as plain text. The two together — `reciprocal` and `elementwise_product` — complete the diagonal-preconditioner-apply chain `assemble_diagonal → reciprocal → elementwise_product` that [`assemble-diagonal`](./assemble-diagonal.md) §Dependencies and [`jacobi-smoother`](./jacobi-smoother.md) name.

**Consumers (L3)** (cross-reference, not reverse-dependencies) — the diagonal-preconditioner-apply fan-out, transported to L3:

- [`jacobi-smoother`](./jacobi-smoother.md) — `dinv = reciprocal(assemble_diagonal(A))` in the setup chain (`palace/linalg/jacobi.cpp:80`). The damping fold `dinv *= omega` (`palace/linalg/jacobi.cpp:92`) is the only post-`reciprocal` step; the apply itself is `(ω·D⁻¹) ⊙ x` (one whole-tensor `elementwise_product`).
- [`assemble-diagonal`](./assemble-diagonal.md) — names the `assemble_diagonal → reciprocal → elementwise_product` chain as its principal §Dependencies forward-reference; this L3 entry is the `reciprocal` step of that chain.
- Chebyshev smoother (4th-kind via `palace/linalg/chebyshev.cpp:178`; 1st-kind via `:241`) — the same `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup feeding the diagonally-scaled polynomial smoother.
- FE-assembly multiplicity averaging — `test_multiplicity.Reciprocal()` at `palace/fem/bilinearform.cpp:278`, converting the per-true-dof contribution count `c[i]` into the averaging weight `1/c[i]` for `SetDofMultiplicity`. A non-preconditioner consumer of the same elementwise-reciprocal primitive.

**L1 anchor**: [`L1/reciprocal`](../L1/reciprocal.md) (firm) — authoritative on the Palace surface details (the real `mfem::Vector::Reciprocal()` upstream-MFEM alias and the complex `ComplexVector::Reciprocal()` kernel, the four consumer call sites, the no-zero-guard policy, the complete L0 evidence list). This L3 entry does not duplicate those details; the L3>L1 rotation is identity-in-form on the primitive itself.

**Strawman reference**: `book/src/design/l4_calculus.md` is the L4/L3 conventions source; this L3 entry follows the strawman's Haskell `::` signature notation. `reciprocal` does not get its own L4 entry (per the leaf-primitive / `CONFIRMED-NOT-NEEDED` verdict the cycle-010 audit reached for the BLAS-1 and operator-to-data cohorts).

## Variant axes

`reciprocal` has **one orthogonal variant axis at L3** — the same framing as L1 (`book/src/L1/reciprocal.md` §"Variant axes"), transported unchanged.

- **element-type** (`real` | `complex`) — collapsed to a single parameterised operator at L3. The L0 source splits into two parallel hierarchies — real `mfem::Vector::Reciprocal()` (upstream MFEM, consumed via the `using Vector = mfem::Vector` alias at `palace/linalg/vector.hpp:20`; element-wise `1/x[i]` in `ℝ`) and complex `ComplexVector::Reciprocal()` (Palace-defined at `palace/linalg/vector.cpp:248-261`; element-wise `1/z = z̄/|z|²` in `ℂ`). At L3 these collapse to one operator parameterised by element type; the result element type matches the input element type (law 5 records the complex closed form as a law, not a variant).

No other variant axes — `reciprocal` is unconditionally pure, element-local, reduction-free, and rank-local across all variants, with no constant-folding fast paths in the L0 kernels.

Non-axes (recorded for disambiguation, inherited from L1):

- **zero-guard policy**: there is **no** zero-guarded vs. unguarded variant — the L0 source unconditionally divides; the partiality `reciprocal(0) = undefined` is recorded as a precondition on the input, not a variant axis. A speculative `safe_reciprocal(x, ε)` (threshold-guarded) is a separate L1 candidate / open question, not a variant of this operator.
- **in-place vs. out-of-place**: the L0 source is in-place receiver self-overwrite only (no two-arg `Reciprocal(x, y)` overload, no `linalg::Reciprocal` free function); the L3 form is unconditionally out-of-place (pure functional). The in-place/out-of-place choice is an L1>L0 mutation-rotation concern, not an L3 axis.
- **complex `s = 1/|z|²` intermediate**: a transparent factoring of the closed form (not a variant axis); the `mfem::forall_switch` host/device dispatch (`palace/linalg/vector.cpp:253-260`) is a transparent execution-model choice that disappears at L1 / L3.

The variant-axis count matches the L1 entry exactly (one orthogonal axis: element-type). No new axes introduced by the L3 rendering; no axes merged or split.

## Status

`firm` — value-threaded positional signature is the canonical iteration-rotation form for the elementwise multiplicative-inverse leaf (`Tensor[N] -> Tensor[N]`, identical to the L1 form); algebraic laws are the same eight that hold at L1 (involution, multiplicative-inverse identity, scalar-factor distribution, multiplicative-distributivity over the elementwise product, complex closed-form, conjugate–reciprocal commutation, all-ones fixed point, negation factor); non-laws are catalogued explicitly (the partiality / no-total-definedness, the nonlinearity, the IEEE-754 bit-level caveats on laws 1/3/4, the non-unified real/complex closed-form); the single orthogonal variant axis (element-type) is inherited unchanged from L1.

The rotation is value-thread-isomorphic on a firm L1 home, and the laws are syntactic identities on the elementwise multiplicative-inverse map (operator-algebra on the fully-read complex kernel `palace/linalg/vector.cpp:248-261` and the upstream-aliased real method) — so the entry is `firm`, not `rough-in`: the absent dedicated `Reciprocal` test under `reference/palace/test/unit/` does not gate syntactic-identity laws (the `apply_linop` / `assemble-diagonal` firm-on-positive-structure situation, not the `eigsolve`-convergence-semantics situation). The partiality (`x[i] ≠ 0`) is recorded as a precondition (a documented, consumer-enforced property), not a status reduction. Behaviour is exercised indirectly through the integration coverage of the four consumer sites (Jacobi `palace/linalg/jacobi.cpp:80`; Chebyshev `:178, :241`; bilinearform `:278`).

The pattern is well-attested via the chain: L1 firm-up (the elementwise leaf harvested with full L0 evidence — the complex kernel read in full + the consumer call sites); cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:40-45`) classified `reciprocal` as an **(A) identity-in-form** backfill ("elementwise self-map", line 41). This dispatch (cycle-038 D1) is the **layer-coherence backfill** — the L3 form was previously implicit in the diagonal-preconditioner-apply chain consumed by the smoother bodies; it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification). It follows the cycle-037-landed `assemble-diagonal` and `jacobi-smoother` (A)-backfills on the same diagonal-preconditioner-apply chain.

## Lowers to

L3 `reciprocal` lowers to L1 [`reciprocal`](../L1/reciprocal.md) as **identity-in-form on the primitive's signature** — **no interposed L2 entry, no `L3-L2`/`L3-L1` theme file**. Both L1 and L3 see `reciprocal :: Tensor[N] -> Tensor[N]` with the same shape contract, the same eight algebraic laws, the same non-law set (partiality, nonlinearity, IEEE-754 caveats), and the same single-orthogonal-axis variant profile (element-type). The L2 layer hosts no standalone `reciprocal` entry (mirroring the BLAS-1 / `apply_linop` / `assemble-diagonal` L2 verdict — leaf primitives are referenced from L2 compositions but do not get standalone L2 entries when the rotation carries no algebraic novelty); the L3>L1 hop is therefore direct.

No `book/src/L3-L1/` directory exists in the artifact; per the cycle-010 `krylov-step`, cycle-011 BLAS-1 / `apply_linop`, and cycle-037 `assemble-diagonal` precedents this entry captures the identity rotation **in-line** (per the cycle-012 meta-phase non-adjacent-identity convention — lowering directories are per-adjacent-edge only). The substantive rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme — it lowers the L1 pure-functional form into Palace's L0 in-place receiver-self-overwrite `Reciprocal()` member-method pair (the real upstream `mfem::Vector::Reciprocal()` and the complex `ComplexVector::Reciprocal()` kernel `s = 1/(XR²+XI²); XR *= s; XI *= -s`, the `forall_switch` host/device dispatch, and the no-zero-guard policy). The L3>L1 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one.

**Practical reading**: an algorithm written at L3 that calls `reciprocal` (e.g. the diagonal-preconditioner-apply setup `dinv = reciprocal(assemble_diagonal(A))` of a Jacobi or Chebyshev smoother body) is reading the L1 entry's algebraic content (laws, non-laws, signature, the `x[i] ≠ 0` precondition) one layer down; the L3 entry's role is to anchor the primitive in the L3 vocabulary inventory of whole-tensor field operations.

## Lifts from

`reciprocal` has **no L4 entry** — leaf elementwise primitives are not first-class L4 vocabulary (the same `CONFIRMED-NOT-NEEDED` verdict the cycle-010 cross-layer audit reached for the BLAS-1 cohort, `apply_linop`, and `assemble-diagonal`: leaf primitives carry no monadic effect, no state-stratification typing, no novel calculus content at L4). At L4 it appears (where consumed) inside larger composed entries as a let-binding feeding the diagonal-preconditioner-apply chain; the rotation from any such L4 mention to this L3 entry is the identity.

L1 `reciprocal` lifts to this L3 entry via the **value-thread-isomorphic** identity rotation: the L1 form's signature has no element loop exposed, no destination buffer, no MPI collective, no iteration view — exactly the properties that make it L3-native by construction. **This L3 entry exists for layer-coherence reasons** — a reader navigating L3 must find `reciprocal` defined in L3 vocabulary, not have to reach down to L1 to recover the field-operation shape.

The cycle-037 `assemble-diagonal` and `jacobi-smoother` L3 backfills (`book/src/L3/assemble-diagonal.md`, `book/src/L3/jacobi-smoother.md`) are the freshest structural precedents on the same diagonal-preconditioner-apply chain: identity-in-form rotation on the primitive's signature, layer-coherence backfill, methodology invariant enacted. `reciprocal` is the elementwise `D⁻¹`-forming step between them; this dispatch closes its L3 entry. It is the **first of the four remaining (A) backfills** (`reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`) to land after the cycle-037 pair.

## Evidence

The L3 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L3 entry:

- `book/src/L1/reciprocal.md` (firm) — the L1 entry whose signature, semantics (element-local, reduction-free, rank-local), eight algebraic laws, single variant axis (element-type), partiality precondition, and complete L0 evidence chain are transported unchanged to L3. The laws and non-laws cited above are reproduced from the L1 entry's §"Algebraic laws".
- `book/src/L3/assemble-diagonal.md` (cycle-037 firm) — the operator-to-data L3 backfill precedent on the same diagonal-preconditioner-apply chain; `reciprocal` is the elementwise step following `assemble_diagonal`. The L3>L1 identity-in-form discipline, the no-L2-entry / no-theme-file rotation shape, and the firm-on-positive-structure status judgement are inherited from this sibling.
- `book/src/L3/scal.md` (cycle-011 firm) — the leaf whole-tensor field-operation precedent; `reciprocal` shares its leaf-primitive / no-sub-composition / identity-in-form shape (differing in nonlinearity and partiality).
- `book/src/L3/index.md:12` — the L3 vocabulary inventory ("Whole-tensor field operations — primitives that act on whole tensors with no element loop exposed at the layer's vocabulary, L3-native by signature shape"); `reciprocal` is the elementwise field operation this entry adds to the inventory.
- `book/src/L3/index.md:40-45` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; line 41 lists `reciprocal` ("elementwise self-map") among the six **(A) identity-in-form** L3 backfills. This entry is the enactment of that verdict.
- `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (firm; `verified_against` block added cycle-037) — the substantive L1>L0 rotation in the chain, which reintroduces the L0 receiver-self-overwrite mutation, the complex kernel decomposition, and the no-zero-guard policy that the L3 entry abstracts away.

**Transitive L0 evidence (via the L1 entry; load-bearing citations re-verified on-disk for this dispatch with `tools/citecheck/citecheck.py --anchor`, not duplicated in detail)**:

- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` — the real-vector alias; `Vector::Reciprocal()` resolves into upstream `mfem::Vector::Reciprocal()` (the real-element-type case).
- `palace/linalg/vector.hpp:107-108` — doc comment `// Set all entries to their reciprocal.` (:107) and `void Reciprocal();` (:108) — the complex `ComplexVector::Reciprocal()` declaration.
- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` definition (the `forall_switch` element-loop computing `s = 1.0 / (XR[i]² + XI[i]²); XR[i] *= s; XI[i] *= -s` at `:257-259`) — realises the complex closed form `1/z = z̄/|z|²`; witnesses laws 1, 5 and the no-zero-guard policy.
- `palace/linalg/jacobi.cpp:80` — consumer: `dinv.Reciprocal();` inside `JacobiSmoother::SetOperator`, immediately after `op.AssembleDiagonal(dinv)`. The principal downstream consumer; the `assemble_diagonal → reciprocal → elementwise_product` chain's reciprocal step.
- `palace/linalg/jacobi.cpp:16` — comment `// Assumes A SPD (diag(A) > 0) ...` — the operator-class-level Jacobi consumer precondition (`diag(A) > 0` ⇒ no zero entry in `dinv`) enforcing the L3 `x[i] ≠ 0` precondition.
- `palace/linalg/chebyshev.cpp:178` — consumer: `dinv.Reciprocal();` inside `ChebyshevSmoother::SetOperator` (4th-kind); `:241` — inside `ChebyshevSmoother1stKind::SetOperator` (1st-kind). Same chain.
- `palace/fem/bilinearform.cpp:278` — consumer: `test_multiplicity.Reciprocal();` — FE-assembly multiplicity-averaging step (a non-preconditioner consumer of the same elementwise-reciprocal primitive).
- *Negative anchor*: no dedicated `Reciprocal` test under `reference/palace/test/unit/`. Per the firm-on-positive-structure precedent (`apply_linop`, `assemble-diagonal`, the BLAS-1 leaves), the firm judgement does not require a dedicated test — every law is a syntactic identity on the positive complex-elementwise kernel body.

## L3 vs L4 distinction

- **L4**: no standalone `reciprocal` entry. The primitive appears (where consumed) inside L4 operator entries as a let-binding within a do-block, carrying no monadic effect of its own. The surrounding wrapper (the do-block, the typed records, the `readonly` typing) is what makes the consuming entry L4-distinct — not the `reciprocal` call itself.
- **L3**: standalone entry (this file). Positional value-threading: `reciprocal x = (\i -> 1/x[i])`. No monadic effect, no typed records, no `readonly` typing, no do-block. The primitive's signature is the L4 let-binding's RHS type, lifted out of any monadic context.

## L3 vs L1 distinction

- **L1**: mutation-lifted pure functional update. `x_new = reciprocal(x_old)`. Frames the operator as the pure-functional image of the L0 receiver-self-overwriting `Reciprocal()` member-method idiom; emphasises the *mutation rotation* against the source (the receiver-mutation drop, the no-zero-guard partiality, the complex `s = 1/|z|²` factoring).
- **L3**: whole-tensor field operation. `y = reciprocal(x)`. Frames the operator as a leaf primitive in the iteration-rotation layer's whole-tensor vocabulary; emphasises element-locality, reduction-freedom, rank-locality, and the absence of an iteration view / sequential obstruction at the operator itself. The L3 form is **identical in body and signature to L1** — the framing differs, but no operational adjustment occurs.

The two layers' entries are **value-thread-isomorphic** on the primitive itself, sharing signature, algebraic laws (eight), non-laws (partiality, nonlinearity, IEEE-754 caveats), the single variant axis (element-type), and the cited L0 evidence (transitive). They differ in **layer interpretation**: L1 frames the primitive as the mutation-rotated form of the L0 `Reciprocal()` member-method; L3 frames it as one of the elementwise field operations the iteration-rotation layer enumerates as canonical vocabulary. The two framings are complementary — they read the same primitive from different layer roles — and the layer-coherence invariant (CLAUDE.md §Methodology invariants "Identity-lowerings still require both L levels") requires both entries to exist.
```

```edit:book/src/L3/index.md
| [`reciprocal`](./reciprocal.md) | `reciprocal :: Tensor[N] -> Tensor[N]` (whole-tensor elementwise multiplicative-inverse self-map; `x -> (1/x[i])ᵢ`; **nonlinear**, **partial** at `x[i]=0`; result element-type tracks input). | (leaf elementwise primitive at L3 — element-local, reduction-free, no sub-composition; sibling of the forthcoming `elementwise_product` on the elementwise-primitives axis). Concepts: (none new). L1 anchor via [`L1/reciprocal`](../L1/reciprocal.md) (identity-in-form on the primitive's signature; eight laws + the partiality precondition + nonlinearity non-law inherited unchanged). | L1 [`reciprocal`](../L1/reciprocal.md) directly (no interposed L2 entry, no L3-L2/L3-L1 theme — leaf primitive whose L1 form is L3-native by signature shape; identity-in-form annotation in-line per cycle-012 non-adjacent-identity convention). Substantive rotation is the L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md). | `firm` (harvested cycle-038T210445Z; identity-lowering backfill per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**; enacts the cycle-036 D2 L3-cohort-growth audit **(A) identity-in-form** verdict at `book/src/L3/index.md:41` — "elementwise self-map"; the `reciprocal` step of the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner-apply chain, following the cycle-037 `assemble-diagonal`/`jacobi-smoother` pair; carries **NO obstruction** at L3 — embarrassingly parallel; first of the four remaining (A) backfills to land) |
```

```edit:book/src/SUMMARY.md
- [scal](./L3/scal.md)
- [reciprocal](./L3/reciprocal.md)
```

## Operator content

The full firm chapter body is authored inside the `new:book/src/L3/reciprocal.md` fence above. Key shape decisions:

- **Signature** (L3 vocabulary, Haskell `::` arrow per the L4/L3 strawman): `reciprocal :: Tensor[N] -> Tensor[N]`, `reciprocal x = (\i -> 1 / x[i])`. Shape contract names the single length axis `N`; result element-type tracks input (not collapsed to real, unlike `nrm2`). Partiality (`x[i] ≠ 0`) stated as a precondition on the input domain.
- **Status: `firm`** — value-thread-isomorphic to the firm L1 home; eight algebraic laws are syntactic identities on the fully-read complex kernel (`palace/linalg/vector.cpp:248-261`), so the absent dedicated `Reciprocal` test does not gate firm (the `apply_linop`/`assemble-diagonal` firm-on-positive-structure situation).
- **Algebraic laws** (eight, transported unchanged from L1): involution-where-defined, multiplicative-inverse identity, scalar-factor distribution, multiplicative-distributivity over elementwise product, complex closed-form, conjugate–reciprocal commutation, all-ones fixed point, negation factor. Laws 3 & 8 are re-expressed in L3 vocabulary using `scal(α, ·)` (a firm L3 sibling) rather than bare `α·`. Non-laws: total-definedness (partiality), linearity (nonlinearity), the IEEE-754 bit-level caveats, non-unified real/complex closed-form.
- **Variant axes**: one orthogonal (element-type real|complex). Non-axes: zero-guard policy, in-place/out-of-place, complex `s=1/|z|²` intermediate.
- **Iteration-rotation marker**: NO sequential obstruction, NO iteration view — leaf primitive, embarrassingly parallel; the sharpest contrast with `chebyshev`/`eigsolve` `partial-obstruction`. Partiality is a domain precondition, not an obstruction.
- **Dependencies**: leaf (none same-layer). Sibling `elementwise_product` (plain text — MISSING at L3). Consumers: `jacobi-smoother`, `assemble-diagonal`, Chebyshev, FE-assembly multiplicity averaging.

## Supporting evidence

- L1 home: `book/src/L1/reciprocal.md` (firm) — source of all eight laws, the partiality precondition, the variant axis, and the L0 evidence chain.
- Cohort verdict: `book/src/L3/index.md:40-45` (cycle-036 D2 audit) — line 41 lists `reciprocal` ("elementwise self-map") among the six (A) firm identity-in-form L3 backfills; line 53 records four remaining after the cycle-037 `assemble-diagonal`/`jacobi-smoother` pair.
- Freshest templates: `book/src/L3/assemble-diagonal.md` + `book/src/L3/jacobi-smoother.md` (cycle-037 firm; same diagonal-preconditioner-apply chain), `book/src/L3/scal.md` (leaf-primitive precedent).
- L1>L0 substantive rotation: `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (firm; `verified_against` block added cycle-037).
- All load-bearing L0 citations re-verified on-disk via `tools/citecheck/citecheck.py --anchor` (all `[ok]`): `palace/linalg/vector.cpp:248-261` (anchor `Reciprocal`), `:257-259` (`s = 1.0`), `:253-260` (`forall_switch`); `vector.hpp:20` (`using Vector`), `:107` (`reciprocal`), `:108` (`Reciprocal`); `jacobi.cpp:80` (`Reciprocal`), `:16` (`SPD`); `chebyshev.cpp:178`, `:241` (`Reciprocal`); `palace/fem/bilinearform.cpp:278` (`Reciprocal`).

**Forward-reference / link hygiene** (verified via `ls book/src/L3/<slug>.md`):
- `elementwise_product`, `normalize`, `divfree-projector` are MISSING at L3 → referenced as **plain text** only (no live links), per `rough-in-forward-reference-must-be-plain-text-not-live-link` (linkcheck2 hard-fails on dead links).
- `scal`, `nrm2`, `dot`, `assemble-diagonal`, `jacobi-smoother`, `apply_linop`, `chebyshev`, `eigsolve` EXIST at L3 → live links (`./<slug>.md`).
- `../L1/reciprocal.md`, `../L1/normalize.md`, `../L1-L0/reciprocal-elementwise-product-mutation-rotation.md`, `../concepts/sequential-obstruction.md` all exist on disk → live links.

**Fence discipline**: the full chapter body (frontmatter → `## Status` → `## Evidence` → `## L3 vs L1 distinction`) sits inside the single `new:book/src/L3/reciprocal.md` block; inner code samples (signature, kernel snippet) are 4-space-indented blocks, NOT nested ```` ```text ```` fences.

## SUMMARY insertion note

The SUMMARY edit inserts `- [reciprocal](./L3/reciprocal.md)` immediately after the existing `- [scal](./L3/scal.md)` line (SUMMARY.md:29), keeping `reciprocal` adjacent to the BLAS-1/leaf elementwise cohort and before the `jacobi-smoother` constructed-operator gate. The integrator wires this via `summary-md-surgical-insert`.

## Open questions / caveats

- **`elementwise_product` / `normalize` / `divfree-projector` L3 backfills remain** (the other three of the four (A) candidates after this dispatch). `reciprocal` references `elementwise_product` as plain text; once `elementwise_product` lands at L3, the §Dependencies sibling reference and the law-2/law-4 mentions can be upgraded to live links (skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`). Tracked under OQ `l3-cohort-growth-audit-c036-verdict`.
- **Speculative `safe_reciprocal(x, ε)`** (threshold-guarded reciprocal returning `0` or `1/ε` for `|x[i]| < ε`) remains an open L1 candidate inherited from the L1 entry; it is NOT a variant axis of `reciprocal` and NOT in scope here. If it ever firms at L1 it would get its own L3 entry, not a variant row on this one.
- **Layer-intro refresh (deferred to layer-intro-author, not in my scope)**: `book/src/L3/index.md` §"Working Notes" line 53 records the L3 firm-operator count as "11 firm + 2 partial-obstruction" with four (A) backfills remaining; after this `reciprocal` landing it becomes 12 firm with three (A) remaining. The dep-map row I append is in-scope; the Working-Notes count tally + a "third firm L3 identity-in-form backfill landed cycle-038" bullet are a layer-intro-author concern — noted here for the integrator/next planner.
