# reciprocal

Mutation-lifted elementwise multiplicative-inverse: `result[i] = 1/x[i]`. The L1 lift of the `Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method pair — the elementwise-reciprocal BLAS-1-shape leaf that, composed with [`assemble_diagonal`](./assemble_diagonal.md), produces the inverse diagonal `D⁻¹` consumed by the diagonal-preconditioner-apply chain (Jacobi, Chebyshev). One of the two elementwise primitives ([`reciprocal`](./reciprocal.md) and [`elementwise_product`](./elementwise_product.md)) the `assemble_diagonal` §Dependencies and `jacobi-smoother` §Dependencies blocks reference.

## Context

`reciprocal` lifts the receiver-mutating `Reciprocal()` member-method pair — `mfem::Vector::Reciprocal()` on real vectors (an upstream MFEM method that Palace consumes via the `using Vector = mfem::Vector;` alias at `palace/linalg/vector.hpp:20`) and `ComplexVector::Reciprocal()` on complex vectors (declared `palace/linalg/vector.hpp:108` with the doc-comment "Set all entries to their reciprocal." at line 107; defined at `palace/linalg/vector.cpp:248-261`) — to a single pure-functional operator over `Tensor[N]`. The operator is element-local, reduction-free, and rank-local: every output element depends on exactly one input element, no cross-element communication, no MPI collective at any layer.

There is no free-function form (`linalg::Reciprocal` does not exist) — the only entry to the operation is the receiver-mutating member-method form. The receiver-mutating idiom (no output-arg form, no `linalg::Reciprocal(x, y)` overload) is the same mutation-rotation idiom named for [`scal`](./scal.md) and `linalg::Normalize`; it is an L0 concern, reintroduced in the L1>L0 `reciprocal-mutation-rotation` lowering, not in the L1 signature.

The four Palace call sites are all on the **diagonal-preconditioner-apply** chain or the FE-assembly multiplicity-averaging step:

- `palace/linalg/jacobi.cpp:80` — `dinv.Reciprocal();` (inside `JacobiSmoother::SetOperator` after `op.AssembleDiagonal(dinv)`; the Jacobi inverse diagonal).
- `palace/linalg/chebyshev.cpp:178` — `dinv.Reciprocal();` (inside `ChebyshevSmoother::SetOperator`; the 4th-kind Chebyshev diagonally-scaled inverse).
- `palace/linalg/chebyshev.cpp:241` — `dinv.Reciprocal();` (inside `ChebyshevSmoother1stKind::SetOperator`; the 1st-kind Chebyshev inverse diagonal).
- `palace/fem/bilinearform.cpp:278` — `test_multiplicity.Reciprocal();` (FE-assembly: after accumulating per-true-dof contribution counts in `test_multiplicity`, the reciprocal converts each count `c[i]` into the averaging weight `1/c[i]` consumed by `SetDofMultiplicity` — the dof-shared-element averaging primitive).

The three preconditioner sites realize the `assemble_diagonal → reciprocal → elementwise_product` chain [`assemble_diagonal`](./assemble_diagonal.md) §Dependencies names. The bilinearform site is a different consumer pattern (multiplicity averaging, not preconditioning) that nonetheless reuses the same elementwise-reciprocal primitive.

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
2. **Multiplicative-inverse identity (per element)**: `x[i] · reciprocal(x)[i] = 1` for every `i` where `x[i] ≠ 0`. The defining identity of the multiplicative inverse, applied pointwise. The composition with the [`elementwise_product`](./elementwise_product.md) primitive yields the all-ones vector: `elementwise_product(x, reciprocal(x)) = 𝟙`.
3. **Scalar-factor distribution**: `reciprocal(α · x) = (1/α) · reciprocal(x)` for any nonzero scalar `α`. The reciprocal of a uniformly-scaled vector is the inverse-scaled reciprocal — applied pointwise, `1/(α·x[i]) = (1/α) · (1/x[i])`. This is the law that makes `reciprocal` compose cleanly with [`scal`](./scal.md): the operator-and-scalar composition `(reciprocal ∘ scal(α))` equals `(scal(1/α) ∘ reciprocal)`.
4. **Multiplicative-distributivity (over the elementwise product)**: `reciprocal(elementwise_product(x, y)) = elementwise_product(reciprocal(x), reciprocal(y))` for `x[i], y[i] ≠ 0` everywhere. The reciprocal of an elementwise product is the elementwise product of reciprocals — `1/(x[i] · y[i]) = (1/x[i]) · (1/y[i])`. Pointwise consequence of the field-multiplicative-inverse identity `1/(ab) = (1/a)(1/b)`.
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

- [`elementwise_product`](./elementwise_product.md) `:: (x: Tensor[N], y: Tensor[N]) -> Tensor[N]` — the binary elementwise multiply. The two together — `reciprocal` and `elementwise_product` — complete the diagonal-preconditioner-apply chain `assemble_diagonal → reciprocal → elementwise_product` that [`assemble_diagonal`](./assemble_diagonal.md) §Dependencies and [`jacobi-smoother`](./jacobi-smoother.md) §Dependencies reference.

Downstream consumers at L1 (cross-reference, not reverse-dependencies):

- [`jacobi-smoother`](./jacobi-smoother.md) — `dinv = reciprocal(assemble_diagonal(A))` in the setup chain (`palace/linalg/jacobi.cpp:80`). The damping fold `dinv *= omega` (`palace/linalg/jacobi.cpp:92`) is the only post-`reciprocal` step; the apply itself is `(ω · D⁻¹) ⊙ x`.
- [`assemble_diagonal`](./assemble_diagonal.md) — names the `assemble_diagonal → reciprocal → elementwise_product` chain as its principal §Dependencies forward-reference; the L1 entry exists in part to satisfy that reference.
- `chebyshev-smoother` (Chebyshev 4th-kind via `palace/linalg/chebyshev.cpp:178`; 1st-kind via `:241`) — the same `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup chain consumed by the diagonally-scaled polynomial smoother.
- FE-assembly multiplicity averaging — `test_multiplicity.Reciprocal()` at `palace/fem/bilinearform.cpp:278`, converting the per-test-dof contribution count (accumulated as `h_mult[k] += 1.0` over assembly-loop iterations) into the averaging weight `1/c[i]` for `SetDofMultiplicity`. A non-preconditioner consumer of the same elementwise-reciprocal primitive.

## Variant axes

`reciprocal` has one orthogonal variant axis at L1:

- **element-type**: `real` | `complex`. The L0 source splits into two parallel hierarchies — real `mfem::Vector::Reciprocal()` (upstream MFEM, consumed via the `using Vector = mfem::Vector` alias at `palace/linalg/vector.hpp:20`; behaviour element-wise `1/x[i]` in `ℝ`) and complex `ComplexVector::Reciprocal()` (Palace-defined at `palace/linalg/vector.cpp:248-261`; behaviour element-wise `1/z = z̄/|z|²` in `ℂ`). At L1 these collapse to one operator parameterised by element type — the closed form `1/x` is the same elementwise map in both fields, and the complex `z̄/|z|²` decomposition is a deterministic realisation of `1/z` in `ℂ` (law 5). The result element type matches the input element type.

No other variant axes — `reciprocal` is unconditionally pure, element-local, reduction-free, rank-local, and has no constant-folding fast paths in the L0 kernels. The complex kernel's `s = 1/|z|²` intermediate is a transparent factoring (not a variant axis); the `mfem::forall_switch` device/host dispatch is a transparent execution-model choice (the L1 form is the elementwise map, agnostic to device placement).

Non-axes (recorded for disambiguation):

- **zero-guard policy**: there is **no** zero-guarded vs. unguarded variant of `reciprocal` — the L0 source unconditionally divides; the partiality `reciprocal(0) = undefined` is recorded as a precondition on the input, not a variant axis. A "safe-reciprocal" variant (taking a threshold `ε` and returning `0` or `1/ε` for `|x[i]| < ε`) is a separate candidate operator, not part of this one.
- **in-place vs. out-of-place**: the L0 source is in-place receiver mutation only (no `linalg::Reciprocal(x, y)` two-arg overload exists); the L1 form is unconditionally out-of-place (pure functional). The in-place/out-of-place choice is an L1>L0 mutation-rotation concern, not an L1 axis.

## Status

`firm` — signature matches the `Reciprocal()` member-method surface exactly; evidence is direct from `palace/linalg/vector.{hpp,cpp}` for the complex case and from the `using Vector = mfem::Vector` alias plus consumer-site call patterns for the real case; the eight algebraic laws are standard properties of the elementwise multiplicative-inverse map, modulo the recorded partiality (precondition `x[i] ≠ 0`) and IEEE-754 caveats. Firm-on-positive-structure: every law is a syntactic identity on the fully-read positive complex kernel (`palace/linalg/vector.cpp:255-260`), so the absence of a dedicated `Reciprocal` test does not gate it.

**Caveats:**

- The real-element-type case (`mfem::Vector::Reciprocal()`) is **upstream MFEM**, not Palace-defined; the real implementation behaviour is taken as given (elementwise `1/x[i]`).
- The no-zero-guard L0 policy is a deliberate Palace/MFEM choice; the partial-at-`x=0` L1 framing reflects this. A `safe_reciprocal(x, ε)` operator with threshold zero-guard is a separate L1 candidate, not a variant of this one.
- The complex kernel uses `forall_switch` host/device dispatch (`palace/linalg/vector.cpp:253-260`); the device/host split is a transparent execution-model choice that disappears at L1.

## L1 vs L0 distinction

- **L0**: two parallel member-method forms — real `mfem::Vector::Reciprocal()` (upstream MFEM, consumed via the alias at `palace/linalg/vector.hpp:20`; element-wise `1/x[i]`) and complex `ComplexVector::Reciprocal()` (declared `palace/linalg/vector.hpp:108` with doc-comment `:107` "Set all entries to their reciprocal."; defined `palace/linalg/vector.cpp:248-261` as a `forall_switch` element-loop computing `s = 1/(XR²+XI²); XR *= s; XI *= -s` — realising the closed form `1/z = z̄/|z|²` via the intermediate squared modulus). Writes through the receiver `*this`. No zero-guard. No `linalg::Reciprocal` free-function form, no two-arg `Reciprocal(x, y)` out-of-place overload.
- **L1**: pure functional elementwise multiplicative-inverse. `result = reciprocal(x)`. No destination buffer in the signature, no in-place receiver. One operator parameterised by element type (real / complex); the complex closed-form decomposition is recorded as a law (law 5), not as a variant. Partiality (`x[i] ≠ 0` precondition) is the L1 reflection of the L0 no-zero-guard policy. The L0 in-place mutation, the `forall_switch` host/device split, the `s = 1/|z|²` intermediate factoring, and the receiver-vs-argument idiom are all L1>L0 lowering concerns (the `reciprocal-mutation-rotation` lowering) — not L1 concerns.

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
- *Negative anchor*: no dedicated `Reciprocal` test under `reference/palace/test/unit/`. Per the BLAS-1-leaf firm-on-positive-structure precedent ([`axpy`](./axpy.md), [`dot`](./dot.md), [`nrm2`](./nrm2.md), [`scal`](./scal.md)) and the derived-construct precedent ([`apply_linop`](./apply_linop.md), [`chebyshev-smoother`](./chebyshev-smoother.md), [`jacobi-smoother`](./jacobi-smoother.md)), the firm-on-positive-structure judgement does not require a dedicated test — every law is a syntactic identity on the positive complex-elementwise kernel body.
- `book/src/L1/assemble_diagonal.md` — its §Dependencies block names the `assemble_diagonal → reciprocal → elementwise_product` chain that this entry's `reciprocal` half (with `elementwise_product`) completes.
- `book/src/L1/jacobi-smoother.md` — §Dependencies names `reciprocal` and `elementwise_product` as the L1-primitive constituents of the diagonal-preconditioner-apply chain.
- `book/src/L1/scal.md`, `book/src/L1/nrm2.md` — sibling BLAS-1-leaf style precedent (the firm-on-positive-structure framing and the no-MPI / element-local language).
- `book/src/L1/normalize.md` — sibling partial-operator precedent for the `x ≠ 0` precondition framing.
