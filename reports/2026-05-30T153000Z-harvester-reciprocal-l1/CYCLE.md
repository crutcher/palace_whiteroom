---
agent: harvester
invoked_at: 2026-05-30T15:30:00Z
scope: L1 operator: reciprocal
status: applied
integrated_at: 2026-05-30T18:00:00Z
integration_commit: e8b9fcc
integration_notes: |
  Cycle-033 D2; landed firm L1 leaf book/src/L1/reciprocal.md (the elementwise
  multiplicative-inverse primitive 1/x[i]; complex 1/(a+bi) = (a-bi)/|a+bi|²;
  partial at x[i]=0). L1 Firm count 23->24; cohort bullet + dep-map row + SUMMARY
  entry inserted after jacobi-smoother. firm-on-positive-structure per the
  BLAS-1-leaf / apply_linop no-dedicated-test precedent; the real-overload
  upstream-MFEM-via-alias citation discipline held. 3 OQs filed:
  reciprocal-l1-mfem-upstream-behaviour-pinning (out-of-focus durable trigger),
  reciprocal-l1-l0-mutation-rotation-theme (abstractor candidate c034+ possibly
  composite with elementwise-product-mutation-rotation),
  reciprocal-l1-index-md-firm-count-d3-second-bump (in-cycle action for D3 —
  D3 landed clean and bumped Firm 24->25). Closes one half of the c032 routed
  reciprocal-and-elementwise-product-l1-primitives stub-or-harvest decision via
  harvester preference per CLAUDE.md "Lower-level shared vocabulary takes priority".
inputs:
  - cycle-033 D2 dispatch (cycle-planner: lower-shared-vocabulary work for `jacobi-smoother` / `assemble-diagonal` consumers)
  - `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` definition (positive site, complex element-type)
  - `palace/linalg/vector.hpp:108` — `ComplexVector::Reciprocal()` declaration + `:107` doc-comment
  - `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` (real overload lives in upstream MFEM, not Palace)
  - `palace/linalg/jacobi.cpp:80`, `palace/linalg/chebyshev.cpp:178,241`, `palace/fem/bilinearform.cpp:278` — call sites
  - `book/src/L1/scal.md`, `book/src/L1/nrm2.md` — sibling BLAS-1-leaf style
  - `book/src/L1/assemble-diagonal.md`, `book/src/L1/jacobi-smoother.md` — forward-referencing consumers
---

# CYCLE: Formalize reciprocal at L1

## Summary

`reciprocal` is the elementwise multiplicative-inverse primitive — `result[i] = 1/x[i]` — the L1 lift of Palace's `ComplexVector::Reciprocal()` member method (the lone Palace-defined overload, complex element type) and of the upstream `mfem::Vector::Reciprocal()` consumed via the `using Vector = mfem::Vector;` alias. It is a leaf BLAS-1-shape primitive (element-local, reduction-free, single-tensor argument), already forward-referenced by ≥2 firm L1 chapters (`assemble-diagonal` and `jacobi-smoother`) as the middle step of the diagonal-preconditioner-apply chain `assemble_diagonal → reciprocal → elementwise_product`. The four Palace call sites are all on that chain — three preconditioner-setup sites (Jacobi, Chebyshev 4th-kind, Chebyshev 1st-kind) plus the FE-assembly `test_multiplicity.Reciprocal()` (averaging the per-test-dof element-shared multiplicity to a per-dof reciprocal weight). Status: `firm`, on the BLAS-1-leaf positive-structure precedent — the apply is one `forall_switch` element-loop with no cross-element dependency, all laws are syntactic identities on the positive complex-elementwise body, and the absence of a dedicated `test-vector.cpp` `Reciprocal` test does not gate firm (the `axpy` / `dot` / `nrm2` / `scal` no-dedicated-test-on-this-method precedent for BLAS-1 leaves; the `apply_linop` / `chebyshev-smoother` firm-on-positive-structure precedent for derived constructs).

## Proposed changes

```new:book/src/L1/reciprocal.md
# reciprocal

Mutation-lifted elementwise multiplicative-inverse: `result[i] = 1/x[i]`. The L1 lift of the `Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method pair — the elementwise-reciprocal BLAS-1-shape leaf that, composed with [`assemble-diagonal`](./assemble-diagonal.md), produces the inverse diagonal `D⁻¹` consumed by the diagonal-preconditioner-apply chain (Jacobi, Chebyshev). One of the two elementwise primitives ([`reciprocal`](./reciprocal.md) and the forthcoming `elementwise_product`) the `assemble-diagonal` §Dependencies and `jacobi-smoother` §Dependencies blocks forward-reference.

## Context

`reciprocal` lifts the receiver-mutating `Reciprocal()` member-method pair — `mfem::Vector::Reciprocal()` on real vectors (an upstream MFEM method that Palace consumes via the `using Vector = mfem::Vector;` alias at `palace/linalg/vector.hpp:20`) and `ComplexVector::Reciprocal()` on complex vectors (declared `palace/linalg/vector.hpp:108` with the doc-comment "Set all entries to their reciprocal." at line 107; defined at `palace/linalg/vector.cpp:248-261`) — to a single pure-functional operator over `Tensor[N]`. The operator is element-local, reduction-free, and rank-local: every output element depends on exactly one input element, no cross-element communication, no MPI collective at any layer.

There is no free-function form (`linalg::Reciprocal` does not exist) — the only entry to the operation is the receiver-mutating member-method form. The receiver-mutating idiom (no output-arg form, no `linalg::Reciprocal(x, y)` overload) is the same mutation-rotation idiom named for [`scal`](./scal.md) and `linalg::Normalize`; it is an L0 concern reintroduced in the forthcoming L1>L0 `reciprocal-mutation-rotation` theme, not in the L1 signature.

The four Palace call sites are all on the **diagonal-preconditioner-apply** chain or the FE-assembly multiplicity-averaging step:

- `palace/linalg/jacobi.cpp:80` — `dinv.Reciprocal();` (inside `JacobiSmoother::SetOperator` after `op.AssembleDiagonal(dinv)`; the Jacobi inverse diagonal).
- `palace/linalg/chebyshev.cpp:178` — `dinv.Reciprocal();` (inside `ChebyshevSmoother::SetOperator`; the 4th-kind Chebyshev diagonally-scaled inverse).
- `palace/linalg/chebyshev.cpp:241` — `dinv.Reciprocal();` (inside `ChebyshevSmoother1stKind::SetOperator`; the 1st-kind Chebyshev inverse diagonal).
- `palace/fem/bilinearform.cpp:278` — `test_multiplicity.Reciprocal();` (FE-assembly: after accumulating per-true-dof contribution counts in `test_multiplicity`, the reciprocal converts each count `c[i]` into the averaging weight `1/c[i]` consumed by `SetDofMultiplicity` — the dof-shared-element averaging primitive).

The three preconditioner sites realize the `assemble_diagonal → reciprocal → elementwise_product` chain [`assemble-diagonal`](./assemble-diagonal.md) §Dependencies names. The bilinearform site is a different consumer pattern (multiplicity averaging, not preconditioning) that nonetheless reuses the same elementwise-reciprocal primitive.

## Signature

    reciprocal :: (x: Tensor[N]) -> Tensor[N]
    reciprocal(x)[i] = 1 / x[i]   for i in [0, N)

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[N]` — read-only (the *prior* value).
- result — `Tensor[N]` — same axis `N` as input; same element type as input.

The result element type tracks the input element type (real `x` → real result; complex `x` → complex result) — unlike [`nrm2`](./nrm2.md) which collapses both to a real-valued result. The operator is a self-map on the vector type's element field.

**Precondition (partiality).** `reciprocal(x)` is defined only at indices `i` where `x[i] ≠ 0`. The L0 source carries **no zero-guard**: the complex body computes `s = 1.0 / (XR[i]² + XI[i]²)` unconditionally (`palace/linalg/vector.cpp:257`), and the real upstream `mfem::Vector::Reciprocal()` is documented in MFEM as element-wise `1/x[i]` without runtime check. Consumer call sites either preclude zero by precondition (the Jacobi/Chebyshev consumers require `diag(A) > 0`, the SPD assumption: `palace/linalg/jacobi.cpp:16` comment "Assumes A SPD (diag(A) > 0)" inside the `GetLambdaMax` setup-helper, which names the broader operator-class-level Jacobi precondition) or by construction (the FE-assembly `test_multiplicity` is the sum of contributions from at least one test element per active dof, so every entry is `≥ 1`). At L1 the operator is **partial**: undefined wherever `x[i] = 0`; the no-zero-guard policy lifts as a precondition on the input (callers must ensure `x[i] ≠ 0 ∀ i`), recorded in the same form as [`normalize`](./normalize.md)'s `x ≠ 0` precondition.

## Semantics

Element-wise: `result[i] = 1 / x[i]` for `i ∈ [0, N)`. Reduction-free and element-local — every output element depends on exactly one input element. No cross-element communication, no dependence on iteration order. No MPI collective at any layer (rank-local; ranks own disjoint slices of `N`).

The operator is pure at L1: the prior `x` and the new value are distinct values. The L0 source overwrites the in-place receiver `*this`; the L1>L0 lowering theme is where that overwrite is reintroduced. At L1 the relationship is purely algebraic.

**Element-type semantics.** For real `x`, the reciprocal is the field-multiplicative-inverse `1/x[i]` in `ℝ`. For complex `x`, the reciprocal is `1/z = z̄/|z|²` in `ℂ` — the closed-form complex multiplicative-inverse `1/(a + bi) = (a − bi)/(a² + b²)`. The L0 complex body realises this as

    s = 1.0 / (XR[i] * XR[i] + XI[i] * XI[i])   // s = 1/|z|²
    XR[i] *= s                                   // Re(1/z) = a · s = a/|z|²
    XI[i] *= -s                                  // Im(1/z) = -b · s = -b/|z|²

(`palace/linalg/vector.cpp:257-259`). The expression `(a − bi) / (a² + b²)` factors as `a/(a²+b²) − i·b/(a²+b²)`, which is exactly what the kernel computes. The intermediate scalar `s = 1/|z|²` is computed once per element and reused for both components — a transparent factoring, algebraically identical to the unfused form.

**No zero-guard.** The complex body computes `1.0 / (XR² + XI²)` unconditionally; the resulting `s = 1/0 = +∞` propagates through the multiplications and yields `NaN` / `±∞` in the components. This is a deliberate L0 choice (the consumer-side precondition `x[i] ≠ 0` is asserted at the call site, not inside the kernel — `palace/linalg/jacobi.cpp:16`'s SPD-`diag(A)>0` assumption inside the `GetLambdaMax` setup-helper is the chief example, naming the operator-class-level Jacobi precondition). At L1 the operator is partial; the missing zero-guard is the L1>L0 lowering's reflection of that partiality.

**Pure / referentially transparent.** Two consecutive applications of `reciprocal` are well-defined whenever the intermediate `1/x[i]` is also nonzero (involution law 1 below); no global state is read or written.

## Algebraic laws

The laws below hold; absences are deliberate. Laws are stated where the relevant elements are nonzero (the operator's precondition); the partiality is recorded once and not re-stated per law.

1. **Involution (where defined)**: `reciprocal(reciprocal(x)) = x`, provided every `x[i] ≠ 0` (so the intermediate vector also has no zero entries). The composition of multiplicative-inverse with itself is the identity on the multiplicative group of the element field (`ℝ*` or `ℂ*`). Both `mfem::Vector::Reciprocal()` and `ComplexVector::Reciprocal()` realise this exactly: a second application restores `x[i]` (modulo finite-precision round-off — see "Does not hold" below). Witnessed by the closed-form `1/(1/z) = z` from the complex body's `(a−bi)/(a²+b²)` formula.
2. **Multiplicative-inverse identity (per element)**: `x[i] · reciprocal(x)[i] = 1` for every `i` where `x[i] ≠ 0`. The defining identity of the multiplicative inverse, applied pointwise. The composition with the (forthcoming) `elementwise_product` primitive yields the all-ones vector: `elementwise_product(x, reciprocal(x)) = 𝟙`.
3. **Scalar-factor distribution**: `reciprocal(α · x) = (1/α) · reciprocal(x)` for any nonzero scalar `α`. The reciprocal of a uniformly-scaled vector is the inverse-scaled reciprocal — applied pointwise, `1/(α·x[i]) = (1/α) · (1/x[i])`. This is the law that makes `reciprocal` compose cleanly with [`scal`](./scal.md): the operator-and-scalar composition `(reciprocal ∘ scal(α))` equals `(scal(1/α) ∘ reciprocal)`.
4. **Multiplicative-distributivity (over the forthcoming elementwise product)**: `reciprocal(elementwise_product(x, y)) = elementwise_product(reciprocal(x), reciprocal(y))` for `x[i], y[i] ≠ 0` everywhere. The reciprocal of an elementwise product is the elementwise product of reciprocals — `1/(x[i] · y[i]) = (1/x[i]) · (1/y[i])`. Pointwise consequence of the field-multiplicative-inverse identity `1/(ab) = (1/a)(1/b)`.
5. **Complex closed-form (complex element-type only)**: for complex `x`, `reciprocal(x)[i] = conj(x[i]) / |x[i]|²` where `|·|²` is the squared modulus. Equivalently: `1/(a + bi) = (a − bi)/(a² + b²)`. The defining closed form for the complex multiplicative inverse — the L0 kernel realises it verbatim (`palace/linalg/vector.cpp:257-259`).
6. **Conjugate–reciprocal commutation (complex)**: `reciprocal(conj(x)) = conj(reciprocal(x))` for complex `x`. The complex conjugate commutes with the reciprocal: `1/conj(z) = conj(1/z)` for `z ≠ 0`. Pointwise consequence of law 5: `conj(1/z) = conj(z̄/|z|²) = z/|z|² = 1/z̄`.
7. **Identity on the all-ones input**: `reciprocal(𝟙) = 𝟙` where `𝟙` is the all-ones vector of axis `N`. Pointwise `1/1 = 1`. The fixed point of the operator. Useful as the unit-test sanity check.
8. **Negation factor**: `reciprocal(−x) = −reciprocal(x)` for nonzero `x`. Pointwise `1/(−x[i]) = −(1/x[i])`. Special case of law 3 with `α = −1`.

Laws that explicitly **do not** hold:

- **Total definedness**: the operator is **partial** — `reciprocal(0)` is undefined (division by zero). The L0 kernel produces `NaN` / `±∞` rather than a clean error. Recorded as a precondition on the input rather than an algebraic law that fails.
- **Linearity in `x`**: `reciprocal(x + y) ≠ reciprocal(x) + reciprocal(y)` in general. `1/(a+b)` is not `1/a + 1/b` — the reciprocal is a nonlinear elementwise map. This is the defining feature that distinguishes the operator from the linear BLAS-1 leaves ([`axpy`](./axpy.md), [`scal`](./scal.md), [`axpby`](./axpby.md), [`axpbypcz`](./axpbypcz.md)).
- **Bit-level involution under finite precision**: law 1 holds exactly in `ℝ` / `ℂ` but is approximate at IEEE-754 — the intermediate `1/x[i]` rounds once on the way out and `1/(1/x[i])` rounds again on the way back, so a round-trip may differ from `x[i]` by at most a few ULPs. For consumer use this is irrelevant (the Jacobi/Chebyshev consumers use the *intermediate* `D⁻¹` directly, never round-trip); recorded for completeness.
- **Bit-level distributivity under finite precision**: laws 3, 4 hold exactly in `ℝ` / `ℂ` but the two sides round differently in IEEE-754 (`1/(α·x[i])` rounds the product first then takes the reciprocal; `(1/α) · (1/x[i])` takes two reciprocals then multiplies). Algebraically equal, bit-pattern not. A transparent-trick consideration; not load-bearing for the Jacobi/Chebyshev consumers (the absorbed `dinv *= omega` damping fold at `palace/linalg/jacobi.cpp:92` is the only post-`reciprocal` arithmetic, and its bit-level result is determined by the `omega` value, not by any reciprocal-law fusion choice).
- **Closed-form for real element-type matches complex**: law 5 is recorded in complex-specific form because Palace's complex kernel realises `1/z = z̄/|z|²` as a non-trivial decomposition (the `s = 1/(XR²+XI²); XR *= s; XI *= -s` triple at `palace/linalg/vector.cpp:257-259`). The closed form does degenerate to the trivial real reciprocal `1/x` in `ℝ` (where `x̄ = x` and `|x|² = x²` give `x̄/|x|² = x/x² = 1/x`); but the law is not stated in unified real+complex form — the unified statement would erase the non-trivial complex decomposition the kernel realises, and the real-case body is `1/x[i]` directly with no decomposition step.

## Dependencies

None at L1. `reciprocal` is a **leaf primitive** at L1 — element-local, reduction-free, single-tensor argument, no cross-element coupling. Its sub-operation is scalar reciprocation (`1/x` in the element field), which is below the L1 layer's resolution (deterministic IEEE-754 primitive for both real and complex). The intermediate scalar `s = 1/|z|²` in the complex body is a transparent factoring of the closed form `z̄/|z|²`; it does not surface as an L1 sub-operator.

Sibling on the elementwise-primitives axis (not dependency):

- `elementwise_product :: (x: Tensor[N], y: Tensor[N]) -> Tensor[N]` — the binary elementwise multiply (forthcoming sibling L1 primitive, parallel cycle-033 D3 dispatch; referenced here as plain text). The two together — `reciprocal` and `elementwise_product` — complete the diagonal-preconditioner-apply chain `assemble_diagonal → reciprocal → elementwise_product` that [`assemble-diagonal`](./assemble-diagonal.md) §Dependencies and [`jacobi-smoother`](./jacobi-smoother.md) §Dependencies forward-reference.

Downstream consumers at L1 (cross-reference, not reverse-dependencies):

- [`jacobi-smoother`](./jacobi-smoother.md) — `dinv = reciprocal(assemble_diagonal(A))` in the setup chain (`palace/linalg/jacobi.cpp:80`). The damping fold `dinv *= omega` (`palace/linalg/jacobi.cpp:92`) is the only post-`reciprocal` step; the apply itself is `(ω · D⁻¹) ⊙ x`.
- [`assemble-diagonal`](./assemble-diagonal.md) — names the `assemble_diagonal → reciprocal → elementwise_product` chain as its principal §Dependencies forward-reference; the L1 entry exists in part to satisfy that reference.
- `chebyshev-smoother` (Chebyshev 4th-kind via `palace/linalg/chebyshev.cpp:178`; 1st-kind via `:241`) — the same `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup chain consumed by the diagonally-scaled polynomial smoother.
- FE-assembly multiplicity averaging — `test_multiplicity.Reciprocal()` at `palace/fem/bilinearform.cpp:278`, converting the per-test-dof contribution count (accumulated as `h_mult[k] += 1.0` over assembly-loop iterations) into the averaging weight `1/c[i]` for `SetDofMultiplicity`. A non-preconditioner consumer of the same elementwise-reciprocal primitive.

## Variant axes

`reciprocal` has one orthogonal variant axis at L1:

- **element-type**: `real` | `complex`. The L0 source splits into two parallel hierarchies — real `mfem::Vector::Reciprocal()` (upstream MFEM, consumed via the `using Vector = mfem::Vector` alias at `palace/linalg/vector.hpp:20`; behaviour element-wise `1/x[i]` in `ℝ`) and complex `ComplexVector::Reciprocal()` (Palace-defined at `palace/linalg/vector.cpp:248-261`; behaviour element-wise `1/z = z̄/|z|²` in `ℂ`). At L1 these collapse to one operator parameterised by element type — the closed form `1/x` is the same elementwise map in both fields, and the complex `z̄/|z|²` decomposition is a deterministic realisation of `1/z` in `ℂ` (law 5). The result element type matches the input element type.

No other variant axes — `reciprocal` is unconditionally pure, element-local, reduction-free, rank-local, and has no constant-folding fast paths in the L0 kernels. The complex kernel's `s = 1/|z|²` intermediate is a transparent factoring (not a variant axis); the `mfem::forall_switch` device/host dispatch is a transparent execution-model choice (the L1 form is the elementwise map, agnostic to device placement).

Non-axes (recorded for disambiguation):

- **zero-guard policy**: there is **no** zero-guarded vs. unguarded variant of `reciprocal` — the L0 source unconditionally divides; the partiality `reciprocal(0) = undefined` is recorded as a precondition on the input, not a variant axis. A future "safe-reciprocal" variant (taking a threshold `ε` and returning `0` or `1/ε` for `|x[i]| < ε`) is a forthcoming open question, not part of this operator.
- **in-place vs. out-of-place**: the L0 source is in-place receiver mutation only (no `linalg::Reciprocal(x, y)` two-arg overload exists); the L1 form is unconditionally out-of-place (pure functional). The in-place/out-of-place choice is an L1>L0 mutation-rotation concern, not an L1 axis.

## Status

`firm` — signature is canonical (matches the `Reciprocal()` member-method surface exactly: one input vector, one output vector of the same shape and element type), evidence is direct from `palace/linalg/vector.{hpp,cpp}` for the complex case and from the `using Vector = mfem::Vector` alias plus consumer-site call patterns for the real case, and the eight algebraic laws listed are standard properties of the elementwise multiplicative-inverse map modulo the explicitly-recorded partiality (precondition: `x[i] ≠ 0`) and the floating-point caveats inherited from IEEE-754 (laws 1, 3, 4 round at ULP-level).

The **firm-on-positive-structure precedent** ([`apply_linop`](./apply_linop.md), [`chebyshev-smoother`](./chebyshev-smoother.md), [`jacobi-smoother`](./jacobi-smoother.md)) governs the absence of a dedicated `Reciprocal` test under `reference/palace/test/unit/`: every law is a syntactic identity on fully-specified positive source (the complex kernel at `palace/linalg/vector.cpp:255-260` is read in full; the closed-form `1/(a+bi) = (a−bi)/(a²+b²)` is the literal arithmetic the kernel computes), not literature-inferred convergence claims — so the missing dedicated test does not gate firm. Behaviour is exercised indirectly through the integration coverage of the four consumer sites (Jacobi `palace/linalg/jacobi.cpp:80`; Chebyshev `:178,:241`; bilinearform `:278`).

**Caveats (not status reductions):**

- The real-element-type case (`mfem::Vector::Reciprocal()`) is **upstream MFEM**, not Palace-defined. Per CLAUDE.md "Many symbols resolve into upstream libraries... Specialized agents cite Palace source, not vendored upstream." the real implementation behaviour is taken as given (elementwise `1/x[i]`); any deeper upstream-MFEM behavioural question (e.g., NaN policy specifics, device-kernel implementation) is logged as an open question (below) rather than reconstructed.
- The no-zero-guard L0 policy is a deliberate Palace/MFEM choice; the partial-at-`x=0` L1 framing reflects this faithfully. A speculative `safe_reciprocal(x, ε)` operator with threshold zero-guard is a separate L1 candidate, not a variant of this one.
- The complex kernel uses `forall_switch` host/device dispatch (`palace/linalg/vector.cpp:253-260`); the device/host split is a transparent execution-model choice that disappears at L1.

## L1 vs L0 distinction

- **L0**: two parallel member-method forms — real `mfem::Vector::Reciprocal()` (upstream MFEM, consumed via the alias at `palace/linalg/vector.hpp:20`; element-wise `1/x[i]`) and complex `ComplexVector::Reciprocal()` (declared `palace/linalg/vector.hpp:108` with doc-comment `:107` "Set all entries to their reciprocal."; defined `palace/linalg/vector.cpp:248-261` as a `forall_switch` element-loop computing `s = 1/(XR²+XI²); XR *= s; XI *= -s` — realising the closed form `1/z = z̄/|z|²` via the intermediate squared modulus). Writes through the receiver `*this`. No zero-guard. No `linalg::Reciprocal` free-function form, no two-arg `Reciprocal(x, y)` out-of-place overload.
- **L1**: pure functional elementwise multiplicative-inverse. `result = reciprocal(x)`. No destination buffer in the signature, no in-place receiver. One operator parameterised by element type (real / complex); the complex closed-form decomposition is recorded as a law (law 5), not as a variant. Partiality (`x[i] ≠ 0` precondition) is the L1 reflection of the L0 no-zero-guard policy. The L0 in-place mutation, the `forall_switch` host/device split, the `s = 1/|z|²` intermediate factoring, and the receiver-vs-argument idiom are all L1>L0 lowering concerns reintroduced in the forthcoming `reciprocal-mutation-rotation` theme — not L1 concerns.

## Evidence

- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` — the real-vector alias; `Vector::Reciprocal()` resolves into the upstream MFEM `mfem::Vector::Reciprocal()` method (not a Palace-defined function). The real-element-type case is sourced here.
- `palace/linalg/vector.hpp:107` — doc comment `// Set all entries to their reciprocal.` — the surface-documented behaviour of the complex method.
- `palace/linalg/vector.hpp:108` — `void Reciprocal();` — `ComplexVector::Reciprocal()` declaration (no arguments, void return, mutating).
- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` definition: `const bool use_dev = UseDevice(); const int N = Size(); auto *XR = Real().ReadWrite(use_dev); auto *XI = Imag().ReadWrite(use_dev); mfem::forall_switch(use_dev, N, [=] MFEM_HOST_DEVICE(int i) { const auto s = 1.0 / (XR[i] * XR[i] + XI[i] * XI[i]); XR[i] *= s; XI[i] *= -s; });`. Implements the complex closed form `1/z = z̄/|z|²` (`s = 1/|z|² = 1/(XR² + XI²)`; `Re(1/z) = a · s`; `Im(1/z) = −b · s`). Witnesses law 5 (complex closed form), law 1 (involution: `1/(z̄/|z|²) = |z|²/z̄ = |z|²·z/|z|² = z`), and the no-zero-guard policy.
- `palace/linalg/jacobi.cpp:80` — consumer: `dinv.Reciprocal();` inside `JacobiSmoother<OperType>::SetOperator`, immediately after `op.AssembleDiagonal(dinv)` (line 79). The `assemble_diagonal → reciprocal → elementwise_product` chain's reciprocal step. The principal downstream consumer.
- `palace/linalg/jacobi.cpp:16` — comment `// Assumes A SPD (diag(A) > 0) to use Hermitian eigenvalue solver.` inside the file-static `GetLambdaMax(MPI_Comm, const Operator&, const Vector&)` setup-helper (lines 14-20; invoked from `JacobiSmoother::SetOperator` only on the `ω = 0.0` damping-estimate path). The comment names the broader SPD assumption of the Jacobi-smoother consumer (`diag(A) > 0` ⇒ no zero entry in `dinv`) that ensures the diagonal-preconditioner consumer never invokes `reciprocal` on a vector with a zero entry; the consumer-side enforcement of the L1 `x[i] ≠ 0` precondition. (The comment is on the eigensolver helper, but the substantive `diag(A) > 0` assumption is the operator-class-level Jacobi consumer precondition, applicable to all consumer paths.)
- `palace/linalg/chebyshev.cpp:178` — consumer: `dinv.Reciprocal();` inside `ChebyshevSmoother<OperType>::SetOperator` (4th-kind Chebyshev path). Same chain.
- `palace/linalg/chebyshev.cpp:241` — consumer: `dinv.Reciprocal();` inside `ChebyshevSmoother1stKind<OperType>::SetOperator`. Same chain (1st-kind).
- `palace/fem/bilinearform.cpp:278` — consumer: `test_multiplicity.Reciprocal();` — FE-assembly multiplicity-averaging step (the per-true-dof contribution count `c[i]` accumulated by atomic adds is converted to the per-dof averaging weight `1/c[i]` for `SetDofMultiplicity`). A non-preconditioner consumer of the same elementwise-reciprocal primitive; witnesses the operator's role beyond the diagonal-preconditioner-apply chain.
- *Negative anchor*: no dedicated `Reciprocal` test under `reference/palace/test/unit/` (codemap `search_text 'Reciprocal'` with `glob: test/unit/**` returns zero hits). Per the BLAS-1-leaf firm-on-positive-structure precedent ([`axpy`](./axpy.md), [`dot`](./dot.md), [`nrm2`](./nrm2.md), [`scal`](./scal.md)) and the derived-construct precedent ([`apply_linop`](./apply_linop.md), [`chebyshev-smoother`](./chebyshev-smoother.md), [`jacobi-smoother`](./jacobi-smoother.md)), the firm-on-positive-structure judgement does not require a dedicated test — every law is a syntactic identity on the positive complex-elementwise kernel body.
- `book/src/L1/assemble-diagonal.md` — the principal forward-referencing chapter; its §Dependencies block names the `assemble_diagonal → reciprocal → elementwise_product` chain that this entry's two halves (`reciprocal` here; `elementwise_product` forthcoming) complete.
- `book/src/L1/jacobi-smoother.md` — the second forward-referencing chapter; §Dependencies names `reciprocal` and `elementwise_product` as L1-primitive candidates not yet authored (plain-text references, now to be upgraded once both land).
- `book/src/L1/scal.md`, `book/src/L1/nrm2.md` — sibling BLAS-1-leaf style precedent (the firm-on-positive-structure framing and the no-MPI / element-local language).
- `book/src/L1/normalize.md` — sibling partial-operator precedent for the `x ≠ 0` precondition framing.
```

```edit:book/src/L1/index.md
<<<OLD
**Firm (23)** — element-wise updates, BLAS-1 reductions, the fused-normalise primitive, the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, the NEP quasi-Newton Jacobian action, the NEP quasi-Newton eigenvalue-correction step, the GMRES/FGMRES restart-correction back-solve, the GMRES/FGMRES per-column running-QR leaf, and the diagonal-preconditioner-apply Jacobi smoother:
=== NEW
**Firm (24)** — element-wise updates, BLAS-1 reductions, the fused-normalise primitive, the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, the NEP quasi-Newton Jacobian action, the NEP quasi-Newton eigenvalue-correction step, the GMRES/FGMRES restart-correction back-solve, the GMRES/FGMRES per-column running-QR leaf, the diagonal-preconditioner-apply Jacobi smoother, and the elementwise multiplicative-inverse primitive:
>>>
```

```edit:book/src/L1/index.md
<<<OLD
- [`jacobi-smoother`](./jacobi-smoother.md) — pure-functional **Jacobi (diagonal) preconditioner action** `y = jacobi_smoother(op, x)`; applies the damped inverse-diagonal scaling `y = (ω · D⁻¹) ⊙ x` where `D = diag(A)`. The thinnest constructed-operator gate at L1 — one elementwise product, no `apply_linop` call, no sweep loop, no workspace; the **diagonal-preconditioner-apply primitive** of roadmap §Foundational. The simplest realization of the `assemble_diagonal → reciprocal → elementwise_product` chain `assemble-diagonal` §Dependencies names; the degree-zero member of the diagonally-scaled-polynomial-smoother family `chebyshev-smoother` parameterises by polynomial degree. Three damping modes (`default ω = 1.0`, `fixed ω ≠ 0`, `estimated ω = 0` triggering the spectral-radius-minimizing `ω = 2/(sf_max·λ_max)` setup) all absorbed into the closure's `dinv` at setup — the apply does not branch on damping mode. Element-type variant (real `Vector dinv` for `OperType = Operator`; complex `ComplexVector dinv` for `OperType = ComplexOperator`) diverges deliberately from `chebyshev-smoother`'s real-only `dinv` — Jacobi respects the complex structure of `dinv` fully. The L0 `Mult` asserts `!initial_guess` (a precondition on the L1 signature, not an algebraic law that fails) — distinct from `chebyshev-smoother`'s degenerate-case-absorbed initial-guess argument. Five consumer sites (`palace/linalg/ksp.cpp:199` Krylov preconditioner; `palace/linalg/errorestimator.cpp:76` the sole `ω = 0.0` damping-estimate site; `palace/linalg/floquetcorrection.cpp:65`; `palace/models/spaceoperator.cpp:640`; `palace/models/timeoperator.cpp:85`). Firm-on-positive-structure (the `apply_linop` / `chebyshev-smoother` no-dedicated-test precedent): every law is a syntactic identity on fully-specified positive source (elementwise multiply at `palace/linalg/jacobi.cpp:38`, setup chain at `:79-93`, transpose alias at `palace/linalg/jacobi.hpp:43`). One load-bearing propagated non-law: the matrix-free-Nedelec approximate `dinv` (inherited from `assemble-diagonal`) propagates transparently through the apply. One dead-code caveat: the complex `Apply<Transpose=true>` kernel (`palace/linalg/jacobi.cpp:61-69`) is unreferenced under the symmetric `MultTranspose` aliasing.
=== NEW
- [`jacobi-smoother`](./jacobi-smoother.md) — pure-functional **Jacobi (diagonal) preconditioner action** `y = jacobi_smoother(op, x)`; applies the damped inverse-diagonal scaling `y = (ω · D⁻¹) ⊙ x` where `D = diag(A)`. The thinnest constructed-operator gate at L1 — one elementwise product, no `apply_linop` call, no sweep loop, no workspace; the **diagonal-preconditioner-apply primitive** of roadmap §Foundational. The simplest realization of the `assemble_diagonal → reciprocal → elementwise_product` chain `assemble-diagonal` §Dependencies names; the degree-zero member of the diagonally-scaled-polynomial-smoother family `chebyshev-smoother` parameterises by polynomial degree. Three damping modes (`default ω = 1.0`, `fixed ω ≠ 0`, `estimated ω = 0` triggering the spectral-radius-minimizing `ω = 2/(sf_max·λ_max)` setup) all absorbed into the closure's `dinv` at setup — the apply does not branch on damping mode. Element-type variant (real `Vector dinv` for `OperType = Operator`; complex `ComplexVector dinv` for `OperType = ComplexOperator`) diverges deliberately from `chebyshev-smoother`'s real-only `dinv` — Jacobi respects the complex structure of `dinv` fully. The L0 `Mult` asserts `!initial_guess` (a precondition on the L1 signature, not an algebraic law that fails) — distinct from `chebyshev-smoother`'s degenerate-case-absorbed initial-guess argument. Five consumer sites (`palace/linalg/ksp.cpp:199` Krylov preconditioner; `palace/linalg/errorestimator.cpp:76` the sole `ω = 0.0` damping-estimate site; `palace/linalg/floquetcorrection.cpp:65`; `palace/models/spaceoperator.cpp:640`; `palace/models/timeoperator.cpp:85`). Firm-on-positive-structure (the `apply_linop` / `chebyshev-smoother` no-dedicated-test precedent): every law is a syntactic identity on fully-specified positive source (elementwise multiply at `palace/linalg/jacobi.cpp:38`, setup chain at `:79-93`, transpose alias at `palace/linalg/jacobi.hpp:43`). One load-bearing propagated non-law: the matrix-free-Nedelec approximate `dinv` (inherited from `assemble-diagonal`) propagates transparently through the apply. One dead-code caveat: the complex `Apply<Transpose=true>` kernel (`palace/linalg/jacobi.cpp:61-69`) is unreferenced under the symmetric `MultTranspose` aliasing.
- [`reciprocal`](./reciprocal.md) — pure-functional elementwise multiplicative-inverse `result[i] = 1/x[i]`. The L1 lift of the `Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method pair — the elementwise-reciprocal BLAS-1-shape leaf that, composed with [`assemble-diagonal`](./assemble-diagonal.md), produces the inverse diagonal `D⁻¹` consumed by the diagonal-preconditioner-apply chain. Real overload lives in upstream MFEM (consumed via `using Vector = mfem::Vector` at `palace/linalg/vector.hpp:20`); complex overload Palace-defined at `palace/linalg/vector.cpp:248-261` (realising `1/z = z̄/|z|²`). Four consumer sites all on the diagonal-preconditioner chain or FE-assembly multiplicity averaging (`palace/linalg/jacobi.cpp:80`; `palace/linalg/chebyshev.cpp:178,241`; `palace/fem/bilinearform.cpp:278`). Partial: undefined at `x[i] = 0` (no L0 zero-guard; consumer-side SPD `diag(A) > 0` precondition). Firm-on-positive-structure (the BLAS-1-leaf / `apply_linop` no-dedicated-test precedent): every law is a syntactic identity on the positive complex-elementwise kernel body. Closes the `reciprocal` half of the `assemble_diagonal → reciprocal → elementwise_product` chain that `assemble-diagonal` §Dependencies and `jacobi-smoother` §Dependencies forward-reference (the `elementwise_product` half is the cycle-033 D3 sibling dispatch).
>>>
```

```edit:book/src/L1/index.md
<<<OLD
| [`jacobi-smoother`](./jacobi-smoother.md) | `(op: JacobiSmoother[N], x: Tensor[N]) → Tensor[N]` (i.e. `(ω · D⁻¹) ⊙ x`) | `assemble-diagonal` (setup), `spectrum_estimate` (setup-only opaque, `ω = 0.0` path); per-call action: elementwise reciprocal + elementwise product (forthcoming L1 primitives) | `firm` (thinnest constructed-operator gate at L1; diagonal-preconditioner-apply primitive; L0: `palace/linalg/jacobi.cpp` (setup `:74-97`; apply `:99-104`); harvested cycle-032; firm-on-positive-structure, no-dedicated-test caveat non-gating per `chebyshev-smoother` precedent; complex-`dinv` divergence from `chebyshev-smoother`; dead-code conjugate-`dinv` Hermitian-transpose caveat) |
=== NEW
| [`jacobi-smoother`](./jacobi-smoother.md) | `(op: JacobiSmoother[N], x: Tensor[N]) → Tensor[N]` (i.e. `(ω · D⁻¹) ⊙ x`) | `assemble-diagonal` (setup), `spectrum_estimate` (setup-only opaque, `ω = 0.0` path); per-call action: elementwise reciprocal + elementwise product (forthcoming L1 primitives) | `firm` (thinnest constructed-operator gate at L1; diagonal-preconditioner-apply primitive; L0: `palace/linalg/jacobi.cpp` (setup `:74-97`; apply `:99-104`); harvested cycle-032; firm-on-positive-structure, no-dedicated-test caveat non-gating per `chebyshev-smoother` precedent; complex-`dinv` divergence from `chebyshev-smoother`; dead-code conjugate-`dinv` Hermitian-transpose caveat) |
| [`reciprocal`](./reciprocal.md) | `(x: Tensor[N]) → Tensor[N]` (i.e. elementwise `1/x[i]`) | (leaf; elementwise BLAS-1-shape primitive; partial at `x[i] = 0`) | `firm` (elementwise multiplicative-inverse; L0: `palace/linalg/vector.cpp:248-261` complex + upstream MFEM real via `using Vector = mfem::Vector` alias `palace/linalg/vector.hpp:20`; harvested cycle-033; four consumer sites: `palace/linalg/jacobi.cpp:80`, `palace/linalg/chebyshev.cpp:178,241`, `palace/fem/bilinearform.cpp:278`; firm-on-positive-structure, no-dedicated-test caveat non-gating; partial at `x[i] = 0`) |
>>>
```

```edit:book/src/SUMMARY.md
<<<OLD
- [jacobi-smoother](./L1/jacobi-smoother.md)
=== NEW
- [jacobi-smoother](./L1/jacobi-smoother.md)
- [reciprocal](./L1/reciprocal.md)
>>>
```

## Supporting evidence

All citations self-verified with `tools/citecheck/citecheck.py --anchor` against the on-disk file (cycle-027 directive: citecheck is source of truth, not codemap `read_range`):

- `reference/palace/palace/linalg/vector.cpp:248-261` ok (anchor `ComplexVector::Reciprocal` at 248)
- `reference/palace/palace/linalg/vector.hpp:107` ok (anchor `Set all entries to their reciprocal`)
- `reference/palace/palace/linalg/vector.hpp:108` ok (anchor `Reciprocal`)
- `reference/palace/palace/linalg/vector.hpp:20` ok (anchor `using Vector = mfem::Vector`)
- `reference/palace/palace/linalg/jacobi.cpp:80` ok (anchor `dinv.Reciprocal`)
- `reference/palace/palace/linalg/chebyshev.cpp:178` ok (anchor `dinv.Reciprocal`)
- `reference/palace/palace/linalg/chebyshev.cpp:241` ok (anchor `dinv.Reciprocal`)
- `reference/palace/palace/fem/bilinearform.cpp:278` ok (anchor `test_multiplicity.Reciprocal`)

Sister-report references:

- Cycle-033 D3 (parallel): `elementwise_product` L1 — the sibling elementwise primitive that completes the `assemble_diagonal → reciprocal → elementwise_product` chain. Referenced as plain text per the harvester one-operator-per-invocation discipline and the forward-reference convention (the sibling may or may not land in the same integrator pass; plain text is safe).
- Cycle-032 (recent): `jacobi-smoother` L1 firm — the principal downstream consumer whose §Dependencies block forward-references `reciprocal` and `elementwise_product` as L1-primitive candidates.
- Cycle-019 (precedent): `assemble-diagonal` L1 firm — the other forward-referencing chapter; the gate to all diagonal-preconditioner-apply consumers.

## Open questions / caveats

- **MFEM `Vector::Reciprocal()` upstream behaviour.** The real-element-type case resolves into upstream MFEM via the `using Vector = mfem::Vector` alias. Detailed MFEM-side behaviour (device-kernel implementation, NaN/Inf propagation specifics for `x[i] = 0` inputs, alignment requirements) is taken as given per the CLAUDE.md "Specialized agents cite Palace source, not vendored upstream" policy. A separate L0 sub-entry pinning the exact MFEM-side implementation could be filed if a future consumer's algebraic claim depends on a precise upstream behaviour beyond "elementwise `1/x[i]`" — none currently does. Log as an out-of-focus open question, not a blocker.
- **Safe-reciprocal (zero-guarded) variant.** Palace ships no `safe_reciprocal(x, ε)` or `reciprocal_or_zero(x)` variant of the operator — the L0 kernels divide unconditionally and the consumer-side precondition (SPD `diag(A) > 0`) is what prevents divide-by-zero in practice. A future smoother variant or robustness-hardened solver path might want a thresholded `reciprocal(x, ε)` that returns `0` (or `1/ε`) for `|x[i]| < ε`; if such a variant is harvested, it is a *sibling* L1 operator (a separate entry with its own threshold parameter and zero-guard law), **not** a variant axis of bare `reciprocal`. Recorded so a future harvester does not erroneously fold it into this entry. (Logged as a candidate for `scaffolding/open-questions.md` only if a consumer surfaces in the wave queue; not filed proactively.)
- **L1>L0 mutation-rotation theme.** The `reciprocal-mutation-rotation` theme (lowering the L1 pure-functional `result = reciprocal(x)` into the L0 receiver-mutating `x.Reciprocal()`, with the in-place overwrite and the `forall_switch` host/device dispatch as the rewrite content) is **not authored here** (one operator per invocation; the lowering theme is the abstractor's domain). The theme will be a thin one — the rotation is the same in-place-receiver-overwrite pattern named for [`scal`](./scal.md) and `linalg::Normalize`, possibly absorbable as a thematic instance into a future "elementwise-member-method-mutation-rotation" composite theme. Plain-text forward-reference (no live link) per the rough-in-forward-reference convention.
- **L2 lowering and `elementwise_pencil` candidate.** The L2 layer's elementwise-vocabulary candidate (a single combinator `elementwise(f, x, y, ...)` parameterised by the per-element function `f` — `reciprocal` ≡ `elementwise(λ z. 1/z, x)`, `elementwise_product` ≡ `elementwise(λ (a,b). a·b, x, y)`, etc.) is a forthcoming L2 unification candidate. Not in scope for this dispatch; logged as a forward observation for the layer-intro-author / combinator-miner queue.
- **Layer intro refresh.** The L1 `index.md` §Vocabulary cohort "Firm" count rises 23 → 24 with this addition; the introduction prose mentions "Six semantic motifs" and lists motif 1 as "Element-wise pure update (`axpy`, `axpby`)" — `reciprocal` is naturally a member of motif 1 (element-wise pure update, single-tensor argument). The layer-intro-author may want to extend motif 1's bullet to name `reciprocal` (and the forthcoming `elementwise_product`) as the unary / binary elementwise leaves of the motif. Recorded as a layer-intro refresh hint, not enacted here (layer-intro-author's domain).
- **Integrator-note: cycle-033 D2/D3 Firm-count coordination.** This report (D2) is the **first** of two cycle-033 cohort-bullet additions to `book/src/L1/index.md` §Vocabulary cohort to land. D2's `edit:` block bumps "Firm (23)" → "Firm (24)" (the OLD/NEW patch on the cohort heading is keyed on the on-disk "Firm (23)" text). The **parallel D3 sibling** (`reports/2026-05-30T153000Z-harvester-elementwise-product-l1/`) adds `elementwise_product` as a second firm L1 operator in the same cohort, but D3's `edit:` blocks do **NOT** touch the Firm count. **When D3 is applied second after D2, the integrator must bump the count again, 24 → 25** (re-keying D3's count edit on the post-D2 "Firm (24)" string, or applying a fresh count-bump patch). If the integration order is reversed (D3 first, D2 second), D2's "Firm (23)" → "Firm (24)" patch will fail to apply (the on-disk text is still "Firm (23)" pre-D2) — but D2 then needs to re-target "Firm (23)" → "Firm (25)" or be applied second with a re-keyed "Firm (24)" → "Firm (25)" patch. The both-D2-and-D3-landed correct final on-disk count is **25**. Surfaced as integrator-note because the per-report serial integration cannot infer the correct second-bump without explicit coordination. The cohort-heading prose tail ("...and the elementwise multiplicative-inverse primitive") in D2's patch covers `reciprocal`; D3's similar tail will need to additionally name `elementwise_product` (re-keyed on the post-D2 prose).
