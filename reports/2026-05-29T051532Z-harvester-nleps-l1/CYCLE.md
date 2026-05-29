---
agent: harvester
invoked_at: 2026-05-29T051532Z
scope: L1 operator: apply_nonlinear_pencil
status: integrated
integrated_at: 2026-05-29T06:14:03Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-021 finalize (staging row #2). apply_nonlinear_pencil NEW firm L1 operator (Write) — the NLEPS interior atom r=T(λ)v for T(λ)=K+λC+λ²M+A2(λ); read from the positive GetResidualNorm site nleps.cpp:807-821 + 4 corroborating sites; nonlinearity localised in the opaque A2:Real→LinearOperator closure (read not reconstructed), so firm on positive structural citation — the apply_linop firm-on-structure precedent, NOT the eigsolve convergence-semantics rough-in precedent. L1/index cohort 12→13 + cohort bullet; SUMMARY :68 register after assemble-diagonal. L1/L2 boundary CLEAN against the sibling combinator-miner-deflate-gram (this owns the L1 pencil-apply; the sibling owns the L2 deflate/gram). 4 deferred NLEPS pieces consolidated into one fan-out-ordered carry-forward OQ. retroactive-budget 0; clean build. L1 firm 12→13."
inputs:
  - palace/linalg/nleps.cpp (QuasiNewtonSolver — SLEPc-NEP-style quasi-Newton NEP solver)
  - palace/linalg/nleps.hpp (NonLinearEigenvalueSolver / QuasiNewtonSolver class decls)
  - palace/linalg/eps.hpp:57-86 (nonlinear SetOperators / SetExtraSystemMatrix virtuals)
  - book/src/L1/eigsolve.md (the outer eigsolve gate that absorbs QuasiNewtonSolver as an orchestration variant)
  - book/src/L0/eigensolver-wrapper.md (NLEPS L0 reference note)
  - sibling: reports/2026-05-29T051532Z-combinator-miner-deflate-gram (L2 deflate/gram combinator — running concurrently; coordinate, do not duplicate)
  - cycle-020 dot-callers census (deflation structure :522,:529,:568; Newton ratio :674-675) — localization aid
---

# CYCLE: Formalize apply_nonlinear_pencil at L1

## Summary

Palace's `QuasiNewtonSolver` (`palace/linalg/nleps.cpp`, 952 lines) is a Palace-owned quasi-Newton nonlinear eigenvalue solver for `(K + λC + λ²M + A2(λ)) x = 0`, using the SLEPc-NEP deflation scheme (Effenberger 2013) layered over the Jarlebring–Koskela–Mele quasi-Newton method (2018). The whole `Solve()` body (351-805) is far too large for one L1 operator. I bound the scope to the **single most foundational L1 primitive** that all four candidate pieces (deflated solve, deflated residual, Jacobian action, Newton-eigenvalue update) are built on: the **nonlinear-pencil residual apply**, `T(λ)·v = (K + λC + λ²M + A2(λ))·v`. This is the matrix-free evaluation of the parameter-dependent operator pencil at a fixed `λ` against a vector `v`. I formalize it as `apply_nonlinear_pencil` (firm). It is read from a clean **positive** source site (`QuasiNewtonSolver::GetResidualNorm`, 807-821) and reappears at four other sites (496-499 solver setup, 556-559 deflated residual, 729 lagged system-operator `opA` rebuild, plus the Jacobian variant at 654-655) — confirming it as the recurrent atom. Because `A2(λ)` is a black-box closure (`std::function`), the operator is firm in structure but its semantics is parameterized over an opaque `A2`; I record the `A2`-evaluation as an opaque sub-call (a leaf at L1), not a reconstruction, so no `partly-constructive` caveat is needed — the pencil apply itself is read directly from source. The deflation extension `U(λ)·v₂` and the Jacobian `T'(λ)·v` are deferred to follow-ups (the deflation extension is the L1 primitive the sibling combinator-miner's L2 `deflate` builds on; the Jacobian is `apply_nonlinear_pencil` with the derivative coefficient vector).

## Proposed changes

```edit:book/src/L1/apply_nonlinear_pencil.md
# apply_nonlinear_pencil

Mutation-lifted nonlinear-pencil residual application: `r = T(λ)·v` for the parameter-dependent operator pencil `T(λ) = K + λC + λ²M + A2(λ)` of a nonlinear eigenvalue problem, evaluated at a fixed eigenvalue estimate `λ` against a vector `v`. The interior atom of Palace's quasi-Newton nonlinear eigensolver (`QuasiNewtonSolver`): every residual, every preconditioner-operator build, and (with a different coefficient vector) the Jacobian action are this one apply.

## Context

Palace's `QuasiNewtonSolver` (`palace/linalg/nleps.cpp`) solves the nonlinear eigenvalue problem (NEP)

```text
(K + λ C + λ² M + A2(λ)) x = 0,   x ≠ 0
```

for a complex eigenvalue `λ` and eigenvector `x`. The left-hand operator `T(λ) = K + λC + λ²M + A2(λ)` is the **operator pencil**: a function from a complex parameter `λ` to a linear operator `LinearOperator[N, N]`. The first three terms `K + λC + λ²M` are the standard quadratic matrix polynomial (the polynomial-eigenproblem part); the fourth term `A2(λ)` is a genuinely nonlinear, frequency-dependent operator supplied as a black-box closure (`funcA2`, a `std::function<std::unique_ptr<ComplexOperator>(double)>` — `palace/linalg/nleps.cpp:177-181`). Inside the solver `A2` is always evaluated at `|Im(λ)|` (Palace's NEP arises from a frequency sweep where the imaginary part of `λ` is the angular frequency).

`apply_nonlinear_pencil` lifts the recurrent code shape that evaluates `T(λ)·v` — assemble the parameter-dependent terms at `λ`, then apply the resulting sum operator to `v`. At L0 this appears as either an explicit term-by-term accumulation into an output buffer (the cleanest positive site, `QuasiNewtonSolver::GetResidualNorm`, `palace/linalg/nleps.cpp:807-821`) or a `BuildParSumOperator` construction of the coefficient-weighted operator sum followed by a `Mult` (the in-`Solve` sites at `palace/linalg/nleps.cpp:496-499` and `palace/linalg/nleps.cpp:556-559`). The two forms are algebraically identical (operator-sum-then-apply = sum-of-applies, by the linearity of `apply_linop`); the L1 form names the apply.

This operator is the **interior** of the [`eigsolve`](./eigsolve.md) gate, not a competitor to it. `eigsolve` treats `QuasiNewtonSolver` as one opaque orchestration variant (`direct_newton`, see `eigsolve` §Variant axes); `apply_nonlinear_pencil` is the per-Newton-step atom that the `direct_newton` orchestration is composed of. It is to the NEP Newton loop what [`apply_linop`](./apply_linop.md) is to the linear Krylov loop: the unit of operator-cost accounting. The L0 NLEPS reference note is [`L0/eigensolver-wrapper`](../L0/eigensolver-wrapper.md).

## Signature

```text
apply_nonlinear_pencil
  :: (T: NonlinearPencil[N], λ: Complex, v: Tensor[N]) -> Tensor[N]
apply_nonlinear_pencil(T, λ, v) = T(λ) · v
                                = K·v + λ·(C·v) + λ²·(M·v) + (A2(λ))·v
```

Shape contract (bunsen-style, named axes):

- `T` — `NonlinearPencil[N]` — an opaque construction-bound pencil value. It binds four operators over a shared square axis `N`: `T.K : LinearOperator[N, N]` (stiffness / curl-curl term), `T.M : LinearOperator[N, N]` (mass term), `T.C : Maybe LinearOperator[N, N]` (damping term; `Nothing` for the no-damping NEP), and the nonlinear closure `T.A2 : Real -> LinearOperator[N, N]` (the frequency-dependent extra-system matrix). Read-only.
- `λ` — `Complex` — the eigenvalue estimate at which the pencil is instantiated. The polynomial terms use `λ` and `λ²` directly; the nonlinear closure is evaluated at `|Im(λ)|` (the frequency argument; see Semantics).
- `v` — `Tensor[N]` — the input vector. Read-only. Must match the pencil's domain axis `N`.
- result — `Tensor[N]` — the residual / pencil-apply output. Same axis `N`.

The axis `N` is uniform across all four bound operators and the input/output (an eigenvalue problem is necessarily square; the four operators `K`, `C`, `M`, and every `A2(·)` instance share the same domain and codomain). The element type is **complex-only** — the bound operators are all `ComplexOperator` at L0 (`palace/linalg/eps.hpp:57-74` shows the nonlinear `SetOperators` overload takes `ComplexOperator` arguments, corroborating the pencil *shape* and complex-only element type; that overload's `A2` is a complex-argument closure `std::function<const ComplexOperator &(std::complex<double>)>` — the real-argument operative closure the solver actually uses is `SetExtraSystemMatrix` at `palace/linalg/nleps.cpp:177-181`, see below), matching the complex-only restriction already noted on [`eigsolve`](./eigsolve.md).

`NonlinearPencil[N]` is an *opaque type* at L1 in the same sense as `apply_linop`'s `LinearOperator`: its representation (which terms are present, how `A2` is realised) is not part of the L1 signature. The `A2` closure is a genuine black box at L1 — `apply_nonlinear_pencil` does not see inside it; it sees a function `Real -> LinearOperator[N, N]` and an evaluation point. The nonlinearity of the whole NEP lives entirely in `A2`; the rest of the pencil is a quadratic matrix polynomial.

## Semantics

`apply_nonlinear_pencil(T, λ, v)` instantiates the pencil at `λ` and applies it to `v`. The result is the vector

```text
r = K·v + λ·(C·v) + λ²·(M·v) + (A2(|Im(λ)|))·v
```

with the `C` term omitted when `T.C = Nothing`. This is exactly the eigenpair residual `T(λ)·x` of the NEP: when `(λ, x)` is an exact eigenpair the result is the zero vector, and `‖apply_nonlinear_pencil(T, λ, x)‖₂` is the residual norm the Newton loop drives to zero (`palace/linalg/nleps.cpp:820`, `linalg::Norml2(comm, r)` over the accumulated `r`). The L1 form is pure-functional: the same `(T, λ, v)` yields the same value. The L0 source overwrites an output buffer `r` (`opK->Mult(x, r)` then three `AddMult` accumulations, `palace/linalg/nleps.cpp:812-819`); that destination buffer and the in-place accumulation order are L1>L0 lowering concerns, not L1 signature.

Three semantic points are load-bearing and recorded rather than smoothed:

**(1) The frequency argument is `|Im(λ)|`, not `λ`.** The nonlinear closure is *not* evaluated at the complex `λ`; it is evaluated at the real number `|Im(λ)|` (`palace/linalg/nleps.cpp:818`, `(*funcA2)(std::abs(l.imag()))`; identically at the `BuildParSumOperator` sites `:497` and `:556`). This reflects Palace's NEP convention that the eigenvalue's imaginary part carries the angular frequency at which the frequency-dependent material/boundary operator `A2` is assembled. The polynomial coefficients, by contrast, are the full complex `λ` and `λ²`. This asymmetry (`A2` takes `|Im(λ)|`; the polynomial takes complex `λ`) is part of the operator's contract — it is *not* an algebraic identity recoverable from a "uniform `λ`" form, so it is pinned in the signature (the closure type is `Real -> LinearOperator`, and the application point is `|Im(λ)|`).

**(2) `A2(λ)` is an opaque, non-linear-in-`λ` black box.** `apply_nonlinear_pencil` is **linear in `v`** (see Algebraic laws) but **not** linear or polynomial in `λ` — the whole point of a NEP is that `A2` introduces arbitrary `λ`-dependence (in Palace's electromagnetics use the frequency-dependent surface impedance / lumped-port admittance is the source). The L1 form treats each `A2(·)` instance as an `apply_linop`-shaped leaf: `apply_nonlinear_pencil` is a composition of (at most) four `apply_linop` calls plus an `axpbypcz`-family accumulation, where one of the operators is produced on-the-fly by `A2`. The cost of evaluating `A2(|Im(λ)|)` (re-assembling the frequency-dependent operator) is real and is why the solver caches the built `A2` operator across a line search (`palace/linalg/nleps.cpp:550-552` carries `A2_out` back to the caller); that caching is a transparent performance trick at L1 (the value is identical) and is an L1>L0 lowering concern.

**(3) The pencil apply is the shared atom of residual, preconditioner-build, and Jacobian.** The same `K + λC + λ²M + A2` shape, with coefficient vector `{1, λ, λ², 1}`, is built at five L0 sites for three distinct purposes — residual evaluation (`:807-821`, `:556-559`), linear-solver operator setup (`:496-499`), and the lagged system-operator refresh (`opA` rebuild at the committed `λ`, `:729`; the preconditioner `opP` is built separately by `funcP`). The **Jacobian** action `T'(λ)·v = (C + 2λM + A2'(λ))·v` (`palace/linalg/nleps.cpp:655`, coefficient vector `{0, 1, 2λ, 1}` with `A2'` the divided-difference derivative of `A2`) is the *same operator* with a different coefficient vector and `A2` replaced by its finite-difference derivative. The Jacobian is therefore **not** a separate L1 operator — it is `apply_nonlinear_pencil` over the derivative pencil `T'`, recoverable by substituting the coefficient/closure (recorded as an algebraic relationship, see Algebraic laws law 5, and the deferred follow-up).

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Linearity in `v`**: `apply_nonlinear_pencil(T, λ, α·u + β·w) = α·apply_nonlinear_pencil(T, λ, u) + β·apply_nonlinear_pencil(T, λ, w)` for any scalars `α, β` and vectors `u, w` in the domain `N`. Holds because at fixed `λ` the pencil `T(λ)` is a fixed linear operator (a coefficient-weighted sum of linear operators), and each term is an `apply_linop` which is linear in its vector argument. This is the defining property — it is what makes `T(λ)` a *linear operator* for fixed `λ` even though the pencil is nonlinear *in `λ`*.
2. **Zero-vector annihilation**: `apply_nonlinear_pencil(T, λ, 0) = 0`. Special case of law 1 with `α = β = 0`.
3. **Term decomposition (sum-of-applies)**: `apply_nonlinear_pencil(T, λ, v) = apply_linop(T.K, v) + λ·apply_linop(T.C, v) + λ²·apply_linop(T.M, v) + apply_linop(T.A2(|Im λ|), v)` (with the `C` term dropped when `T.C = Nothing`). This is the exact L0 accumulation shape (`palace/linalg/nleps.cpp:812-819`: `opK->Mult(x, r)`, then `opC->AddMult(x, r, l)`, `opM->AddMult(x, r, l*l)`, `A2->AddMult(x, r, 1.0)`). It is the bridge law to the BLAS-1 / `apply_linop` floor — the L2 decomposition of `apply_nonlinear_pencil` unfolds into four `apply_linop` calls plus a scaled accumulation. Equivalent at L0 to the `BuildParSumOperator({1, λ, λ², 1}, {K, C, M, A2})` + single `Mult` form (`:498-499`, `:557-559`) by the operator-sum-distributes law of `apply_linop` (`apply_linop` law 5).
4. **Polynomial-part homogeneity in the operator coefficients** (coefficient-vector linearity): instantiating the pencil with coefficient vector `c = (c_K, c_C, c_M, c_A2)` gives `c_K·(K·v) + c_C·(C·v) + c_M·(M·v) + c_A2·(A2(|Im λ|)·v)`; this is linear in `c`. Witnessed by the shared `BuildParSumOperator(coeffs, {opK, opC, opM, A2}, true)` construction reused with `{1, λ, λ², 1}` for the pencil (`:498`, `:557`, `:729`) and `{0, 1, 2λ, 1}` for the Jacobian (`:655`). This is what makes law 5 a substitution rather than a new operator.
5. **Jacobian as derivative-pencil apply**: the NEP Jacobian action satisfies `T'(λ)·v = apply_nonlinear_pencil(T', λ, v)` where `T'` is the derivative pencil with coefficient vector `{0, 1, 2λ, 1}` and nonlinear closure `A2'(λ) ≈ (A2((1+δ)|Im λ|) − A2(|Im λ|)) / (i·δ·|Im λ|)` (the divided-difference approximation, `palace/linalg/nleps.cpp:653-655`). Recorded as an algebraic relationship, not as a dep-map edge: the Jacobian is the *same* L1 operator applied to a derived pencil value. (The construction of `T'` — assembling the finite-difference `A2'` — is deferred to a follow-up; see Open questions.)

Laws that explicitly **do not** hold:

- **Linearity / polynomiality in `λ`**: `apply_nonlinear_pencil(T, ·, v)` is **not** a linear or polynomial function of `λ` in general. The quadratic-polynomial part (`K + λC + λ²M`) is polynomial in `λ`, but `A2(λ)` introduces arbitrary nonlinearity (it is a black-box closure). This is the defining feature of a *nonlinear* eigenvalue problem and the reason the solver is iterative (quasi-Newton) rather than a single polynomial-eigenproblem solve. Recorded as an absence because callers must not assume a polynomial structure across `λ`.
- **Closure evaluation commutes with the real/imaginary split**: `A2` is evaluated at `|Im(λ)|`, a lossy projection of `λ` to a single real argument. `apply_nonlinear_pencil(T, λ₁, v) = apply_nonlinear_pencil(T, λ₂, v)` does **not** imply `λ₁ = λ₂` (two `λ` with the same `|Im|` and matched polynomial contributions could coincide; more importantly `Re(λ)` enters only through the polynomial terms, not through `A2`). The map is not injective in `λ`. Recorded so the eigenvalue-correction step does not over-read the residual.
- **Bit-determinism across the two L0 build forms**: the term-by-term `Mult`+`AddMult` accumulation (`:812-819`) and the `BuildParSumOperator`+`Mult` form (`:498-499`/`:557-559`) are algebraically identical but may differ at the bit level (different accumulation order across the four terms, and matrix-free `A2` inherits reduction-tree non-associativity from `apply_linop`). Load-bearing per the CLAUDE.md taxonomy; the mathematical law-3 identity holds, its floating-point realisation is exact modulo accumulation-order noise.
- **`A2`-recompute idempotence at the bit level**: re-evaluating `A2(|Im λ|)` to rebuild the operator is mathematically idempotent but, for a matrix-free / re-assembled `A2`, may not reproduce the previous assembly bit-for-bit; this is why the solver caches the built operator within a line search rather than rebuilding. The *value* is the same (transparent trick); bit-reproduction across rebuilds is not guaranteed.

## Dependencies

- [`apply_linop`](./apply_linop.md) — direct. Each of the (up to) four pencil terms is an `apply_linop` against the corresponding bound operator; the `A2(|Im λ|)` term applies the just-assembled nonlinear operator. Law 3 makes this explicit.
- [`axpbypcz`](./axpbypcz.md) / [`axpby`](./axpby.md) — transitive (via the coefficient-weighted accumulation of the four term-applies into the output; the L0 `AddMult(x, r, c)` calls are the fused `r ← r + c·(op·x)` form, which is `axpby(c, apply_linop(op, x), 1, r)` per `apply_linop`'s accumulate-mode treatment).
- [`nrm2`](./nrm2.md) — adjacent, not a dependency of the apply itself: the residual *norm* `‖T(λ)·v‖₂` used by the Newton convergence test is `nrm2(apply_nonlinear_pencil(T, λ, v))`. The L0 `GetResidualNorm` site fuses the apply and the norm (`:807-821`); at L1 they are two composed operators, not one.

The nonlinear closure `A2 : Real -> LinearOperator[N, N]` is an **opaque leaf** at L1 — its internal assembly (frequency-dependent surface impedance, lumped-port admittance, Newton-polynomial interpolation via `NewtonInterpolationOperator`) is below the L1 resolution and surfaces only in the L1>L0 lowering and in the `A2`-construction follow-up.

`apply_nonlinear_pencil` is the per-step operator-cost atom that the L2 NEP-Newton vocabulary (the deflated quasi-Newton step, and the sibling combinator-miner's `deflate`/`gram` L2 combinator) will depend on, exactly as `apply_linop` is the per-step atom of `krylov-step`.

## Variant axes

`apply_nonlinear_pencil` has the following variant axes at L1; two are collapsed and recorded as deliberate absorption.

- **damping-present**: `with-C` | `without-C`. The L0 source exposes two `SetOperators` overloads — `(K, M, type)` (`palace/linalg/nleps.cpp:191`, no damping) and `(K, C, M, type)` (`palace/linalg/nleps.cpp:221`, with damping). At L1 this is the `T.C : Maybe LinearOperator[N, N]` axis — `Nothing` drops the `λ·(C·v)` term (the L0 `GetResidualNorm` guards `if (opC)` at `:813-816`). One operator, parameterised; the term-presence is a property of the bound pencil.
- **purpose / coefficient-vector**: `residual {1, λ, λ², 1}` | `jacobian {0, 1, 2λ, 1}`. Per law 4–5 these are the same operator over different coefficient vectors (and, for the Jacobian, the `A2'` derivative closure). At L1 they are **not** separate operators — the Jacobian is `apply_nonlinear_pencil(T', λ, v)`. Recorded as an absorbed axis (the L0 source builds both via the same `BuildParSumOperator`).

Collapsed (absorbed) axes:

- **A2-representation**: `frequency-dependent-assembly` | `newton-polynomial-interpolation` | `... ` — the nonlinear closure's realisation. At L0, `A2` is supplied either as a direct re-assembly closure or approximated by a `NewtonInterpolationOperator` (`palace/linalg/nleps.hpp:232-283`, `Interpolation` class at `:232` / `NewtonInterpolationOperator` class at `:246`). At L1 these collapse to a single opaque `A2 : Real -> LinearOperator[N, N]` — the L1 contract sees a function and an evaluation point; the interpolation/assembly choice is an L0 concern (variant absorption, per [`concepts/variant-absorption`](../concepts/variant-absorption.md)).
- **L0-build-form**: `term-by-term AddMult` | `BuildParSumOperator + Mult` — the two algebraically-identical accumulation shapes (`:812-819` vs `:498-499`). Collapsed at L1 by law 3; the choice is an L1>L0 lowering / transparent-performance concern.

## Status

`firm` — the operator's structure is read directly from a **positive** Palace source site (`QuasiNewtonSolver::GetResidualNorm`, `palace/linalg/nleps.cpp:807-821`) and corroborated at four further sites (`:496-499`, `:556-559`, `:655`, `:729`); the signature's pencil shape matches the nonlinear `SetOperators` virtual (`palace/linalg/eps.hpp:69-74`) and the real-argument `A2`-closure contract matches the `SetExtraSystemMatrix` closure type (`palace/linalg/nleps.cpp:177-181`, the operative closure; the `eps.hpp:69-74` overload's `A2` is a distinct complex-argument closure corroborating only the shape); the algebraic laws are standard properties of a fixed-`λ` linear operator (linearity in `v`, term decomposition) modulo the explicitly-recorded floating-point and `λ`-nonlinearity non-laws. The nonlinearity is fully localised in the opaque `A2` closure, which is read (not reconstructed) from source — so unlike the larger NEP algorithm (which is SLEPc-NEP-literature-anchored), the *pencil apply itself* needs no `partly-constructive` caveat. Note: the surrounding `eigsolve` gate is `rough-in (test-coverage-bounded)` because there is no `test-eigensolver.cpp`; the same absence applies here (NLEPS has zero dedicated unit tests — confirmed via `search_text` over `test/unit/**`). `apply_nonlinear_pencil` is nonetheless firm on the strength of exhaustive positive structural citation, because every law is a syntactic identity on fully-specified source (it is the `apply_linop` situation, not the `eigsolve`-convergence-semantics situation): the laws do not depend on convergence behaviour, so the missing convergence test does not gate them. (Should the NEP-orchestration test gap later prove to surface a contract issue in the apply, this can be revisited — but the apply's laws are operator-algebra facts, not iteration facts.)

## L1 vs L0 distinction

- **L0**: either (a) a term-by-term in-place accumulation into an output buffer — `opK->Mult(x, r)` then `opC->AddMult(x, r, l)`, `opM->AddMult(x, r, l*l)`, `A2->AddMult(x, r, 1.0)` (`palace/linalg/nleps.cpp:812-819`), with `A2` freshly assembled by `auto A2 = (*funcA2)(std::abs(l.imag()))` at `:818`; or (b) a `BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, opA2.get()}, true)` construction of a `ComplexOperator` followed by `A->Mult(v, r)` (`palace/linalg/nleps.cpp:556-559`). The damping term is conditional (`if (opC)`). The output buffer is reused/overwritten; the built `A2` operator is cached across a line search (`:550-552`). The pencil shape is duplicated at five sites.
- **L1**: pure-functional `r = apply_nonlinear_pencil(T, λ, v)`. No output buffer in the signature, no `A2`-caching, no build-form choice. One operator parameterised by the `Maybe C` damping axis and the coefficient/closure (residual vs Jacobian). The nonlinear `A2` is an opaque `Real -> LinearOperator[N, N]` evaluated at `|Im λ|`. Linearity in `v` and the term-decomposition law hold; `λ`-nonlinearity and the two-build-form bit-difference are recorded as explicit non-laws.

## Evidence

- `palace/linalg/nleps.cpp:807-821` — `QuasiNewtonSolver::GetResidualNorm` — the clean **positive** site: `opK->Mult(x, r)` (812), `if (opC) opC->AddMult(x, r, l)` (813-816), `opM->AddMult(x, r, l*l)` (817), `auto A2 = (*funcA2)(std::abs(l.imag()))` (818) then `A2->AddMult(x, r, 1.0)` (819), `return linalg::Norml2(comm, r)` (820). Direct witness of the term-decomposition (law 3), the `|Im λ|` closure argument (semantics point 1), and the damping-present axis. The fused norm is `nrm2 ∘ apply_nonlinear_pencil`.
- `palace/linalg/nleps.cpp:496-499` — in-`Solve` linear-solver setup: `opA2 = (*funcA2)(std::abs(eig.imag()))` (497) and `opA = BuildParSumOperator({1.0+0.0i, eig, eig*eig, 1.0+0.0i}, {opK, opC, opM, opA2.get()}, true)` (498-499). The `{1, λ, λ², 1}` coefficient vector + the `BuildParSumOperator` build form (law 3 alternate form; law 4 coefficient-vector).
- `palace/linalg/nleps.cpp:556-559` — inside the `compute_residual` lambda (the deflated residual): `A2_out = (*funcA2)(std::abs(lam.imag()))` (556) and `auto A = BuildParSumOperator({1.0+0.0i, lam, lam*lam, 1.0+0.0i}, {opK, opC, opM, A2_out.get()}, true)` (557-558), then `A->Mult(vv, rr)` (559). The bare pencil apply is the `k == 0` (no-deflation) part of the deflated residual; the deflation extension `U(λ)v₂` (560-570) is the deferred follow-up.
- `palace/linalg/nleps.cpp:550-552` — `A2_out` carried back to the caller so the built `A2` operator can be reused at the same `λ` across a line search — the transparent `A2`-caching performance trick (non-law: bit-reproduction across rebuilds).
- `palace/linalg/nleps.cpp:655` — the Jacobian build: `auto opJ = BuildParSumOperator({0.0+0.0i, 1.0+0.0i, 2.0*eig, 1.0+0.0i}, {opK, opC, opM, opAJ.get()}, true)` then `opJ->Mult(v, w)` (657) — the same operator with coefficient vector `{0, 1, 2λ, 1}`; `opAJ` (653-654) is the finite-difference `A2'` from `opA2p = (*funcA2)(|Im λ|·(1+δ))`. Witnesses law 5 (Jacobian as derivative-pencil apply) and the purpose/coefficient-vector variant axis.
- `palace/linalg/nleps.cpp:729` — the lagged **system-operator** refresh: rebuilds the same `{1, λ, λ², 1}` pencil into `opA` at the committed `λ` (the preconditioner `opP` is the separate `(*funcP)(...)` build feeding `opInv->SetOperators(*opA, *opP)`). Fifth occurrence of the shape.
- `palace/linalg/nleps.cpp:177-181` — `QuasiNewtonSolver::SetExtraSystemMatrix(std::function<std::unique_ptr<ComplexOperator>(double)> A2) { funcA2 = A2; }` — the nonlinear closure type `Real -> ComplexOperator` (the `A2 : Real -> LinearOperator[N, N]` of the signature); confirms the closure takes a single real argument (the frequency), grounding the `|Im λ|` evaluation convention.
- `palace/linalg/eps.hpp:69-74` — the nonlinear `SetOperators(K, M, A2, type)` virtual overload (the `(K + λM + A2(λ))`-shaped problem at the abstract-interface level) — corroborates the **pencil shape** and the complex-only element type. Note this overload's `A2` parameter is a *complex-argument* closure (`std::function<const ComplexOperator &(std::complex<double>)>`); it does **not** establish the real-argument closure contract the `A2 : Real -> LinearOperator[N, N]` signature rests on — that contract is the `SetExtraSystemMatrix` closure at `palace/linalg/nleps.cpp:177-181` (`std::function<std::unique_ptr<ComplexOperator>(double)>`, the closure the solver actually evaluates at `|Im λ|`).
- `palace/linalg/nleps.hpp:146` — class comment "Quasi-Newton nonlinear eigenvalue solver for (K + λ C + λ² M + A2(λ)) x = 0" — the pencil equation in the source's own words (immediately preceding the `class QuasiNewtonSolver` decl at `:147`).
- `palace/linalg/nleps.hpp:232-283` — `Interpolation` (class at `:232`) / `NewtonInterpolationOperator` (class at `:246`) — one concrete `A2`-representation (Newton-polynomial interpolation), grounding the collapsed A2-representation axis.
- `palace/linalg/nleps.cpp:191-219`, `:221-252` — the two `SetOperators` overloads (`without-C`, `with-C`) — the damping-present variant axis.
- No dedicated unit test: `search_text` for `QuasiNewton|nleps|NonLinearEigen|GetResidualNorm|funcA2` over `test/unit/**` returns zero hits (confirms the test-coverage caveat inherited from `eigsolve`; the firm decision rests on positive structural citation, not on a test).
```

```edit:book/src/L1/index.md
| [`assemble-diagonal`](./assemble-diagonal.md) | `(A: LinearOperator[N, N]) → Tensor[N]` (i.e. `diag(A)`) | (leaf; opaque square operator; sibling to `apply_linop`, NOT a dependency) | `firm` (operator-to-data gate; L0: `palace/linalg/{operator,rap,hypre}.cpp` + `palace/fem/libceed/operator.cpp`; harvested cycle-019; matrix-free high-order-Nedelec approximate-diagonal load-bearing non-law) |
| [`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md) | `(T: NonlinearPencil[N], λ: Complex, v: Tensor[N]) → Tensor[N]` (i.e. `T(λ)·v = K·v + λ·C·v + λ²·M·v + A2(\|Im λ\|)·v`) | `apply_linop` (direct, per-term); `axpby`/`axpbypcz` (transitive, coefficient-weighted accumulation); `nrm2` (adjacent, for the residual norm) | `firm` (NEP interior atom; L0: `palace/linalg/nleps.cpp:807-821` positive site + `:496-499,:556-559,:655,:729`; harvested cycle-021; nonlinearity localised in opaque `A2` closure; `eigsolve`-inherited no-dedicated-test caveat) |
```

```edit:book/src/SUMMARY.md
- [assemble-diagonal](./L1/assemble-diagonal.md)
- [apply_nonlinear_pencil](./L1/apply_nonlinear_pencil.md)
```

## Operator content

(The full firm entry is in the `edit:book/src/L1/apply_nonlinear_pencil.md` block above. Summary of the load-bearing pieces:)

- **Slug + one-line**: `apply_nonlinear_pencil` — nonlinear-pencil residual application `r = T(λ)·v` for `T(λ) = K + λC + λ²M + A2(λ)`; the interior atom of Palace's quasi-Newton NEP solver.
- **Signature**: `apply_nonlinear_pencil :: (T: NonlinearPencil[N], λ: Complex, v: Tensor[N]) -> Tensor[N]`. `T` binds `K`, `Maybe C`, `M` over square axis `N` plus an opaque nonlinear closure `A2 : Real -> LinearOperator[N, N]` evaluated at `|Im λ|`. Complex-only element type.
- **Semantics**: instantiate the pencil at `λ`, apply to `v`. Three load-bearing points: (1) `A2` is evaluated at `|Im λ|` (frequency), not complex `λ`; the polynomial terms use complex `λ`/`λ²`. (2) `A2` is an opaque non-linear-in-`λ` black box — the apply is linear in `v` but not in `λ`. (3) the same apply (different coefficient vector) is the residual, the linear-solver system-operator build, and the Jacobian.
- **Algebraic laws**: linearity in `v`; zero-annihilation; term decomposition (sum-of-applies, law 3 — the bridge to the `apply_linop` floor); coefficient-vector linearity (law 4); Jacobian as derivative-pencil apply (law 5). Non-laws: no linearity/polynomiality in `λ`; `A2`-arg non-injective in `λ`; two-build-form bit-difference; `A2`-recompute non-idempotent at the bit level.
- **Dependencies**: `apply_linop` (direct), `axpby`/`axpbypcz` (transitive), `nrm2` (adjacent, for the residual norm). `A2` is an opaque leaf.
- **Status**: `firm`.
- **Evidence**: positive site `nleps.cpp:807-821` + four corroborating sites; closure type `:177-181`; abstract overload `eps.hpp:69-74`; pencil equation `nleps.hpp:146`.

### Which piece I chose and why it is the most foundational

The dispatch listed four candidates: the deflated quasi-Newton residual/Jacobian step, the nonlinear residual `T(λ)v`, the deflation step, and the Newton-update/eigenvalue-correction step. **I chose the bare nonlinear-pencil apply `T(λ)v`** because it is the *common sub-expression of all four*:

- The **deflated residual** (`compute_residual`, `:553-575`) is `apply_nonlinear_pencil(T, λ, v)` plus a deflation extension `T(λ)·X·(λI−H)⁻¹·v₂` — the bare apply is literally the `k == 0` branch (`:559`).
- The **deflated solve** (`deflated_solve`, `:497-536`) solves `T(σ)⁻¹` — its operator `opA` is built by the same pencil construction (`:498-499`).
- The **Jacobian action** (`:655`) is `apply_nonlinear_pencil` over the derivative pencil (law 5).
- The **Newton-eigenvalue update** (`:673-675`) consumes the residual `u` (the pencil apply output) in its ratio `Δλ = −⟨u, w₀⟩/⟨w, w₀⟩`.

It is also (a) the **smallest** — a four-term coefficient-weighted operator sum applied to a vector, four `apply_linop`s and an accumulation — and (b) **most unblocking**: it is read from a clean positive source site (`GetResidualNorm`), so it is firm with no literature reconstruction, and it gives the higher L2 forms (the sibling combinator-miner's `deflate`/`gram`, the future deflated-quasi-Newton-step L2 combinator) their per-step cost atom, exactly as `apply_linop` underwrites `krylov-step`. Per CLAUDE.md "promote a speculative L1 operator to firm only when small AND when it simplifies the semantics of higher forms," this is the right grain.

## Supporting evidence

- All citations self-verified against source via `mcp__palace-codemap__read_range` at emit time (per `verify-citation-range` producer self-verification): `nleps.cpp:807-821` (GetResidualNorm body, re-read after an initial 2-line drift), `:496-499` / `:556-559` / `:655` / `:729` (the BuildParSumOperator sites, line-pinned via `search_text`), `:177-181` (SetExtraSystemMatrix), `:191`/`:221` (the two SetOperators overloads), `:550-552` (A2 caching), `:653-655` (Jacobian / A2'), `:673-675` (Newton ratio). `eps.hpp:69-74` (nonlinear overload) and `nleps.hpp:146` (class comment / pencil equation) read directly.
- Coordination with sibling `reports/2026-05-29T051532Z-combinator-miner-deflate-gram` (concurrent, no CYCLE.md yet): the combinator-miner owns the **L2** `deflate`/`gram` combinator; this harvester owns the **L1** pencil-apply primitive that the deflated residual/solve build on. No overlap — the deflation *extension* (`U(λ)v₂` = `T(λ)·X·(λI−H)⁻¹·v₂`) is explicitly deferred here (Open questions) precisely because it is the L1 primitive the combinator-miner's L2 combinator sits on, and should be harvested in its own dispatch after the combinator-miner's L2 shape lands so the L1/L2 boundary is drawn from the combinator's needs.
- Variant axes classified per `classify-variant-axis`: damping-present (`Maybe C`, runtime/construction), purpose/coefficient-vector (residual vs Jacobian, absorbed by law 5), A2-representation (absorbed), L0-build-form (absorbed by law 3).
- `find-tests-for-region`: no dedicated NLEPS unit test exists (`search_text` over `test/unit/**` for `QuasiNewton|nleps|NonLinearEigen|GetResidualNorm|funcA2|A2(` → 0 hits). The firm decision rests on positive structural citation, not test coverage; the no-test caveat is inherited from `eigsolve` and recorded in Status.

## Open questions

1. **NLEPS deferred pieces (the rest of the carry-forward).** This dispatch harvested only the bare pencil apply. The remaining NLEPS L1 primitives, in suggested fan-out order:
   - **`nleps_deflated_residual`** — `apply_nonlinear_pencil(T, λ, v)` + the deflation extension `T(λ)·X·(λI−H)⁻¹·v₂` with `r₂ = Xᴴv` (`palace/linalg/nleps.cpp:553-575`). This is the L1 primitive the sibling combinator-miner's L2 `deflate`/`gram` combinator builds on — **harvest after the combinator-miner's L2 shape lands** so the L1/L2 boundary follows the combinator's needs (avoid pre-committing the deflation decomposition).
   - **`nleps_deflated_solve`** — the block solve `[[T(σ), U(σ)], [Aᴴ, B]]⁻¹` via the Schur-complement formula (`palace/linalg/nleps.cpp:497-536`). Builds on `ksp_solve` (the `opInv->Mult` inner solve, `:514`) + the deflation linear algebra. Depends on `nleps_deflated_residual`'s deflation vocabulary.
   - **`nleps_jacobian_action`** (or fold into `apply_nonlinear_pencil` per law 5) — the derivative pencil `T'(λ)·v` with the finite-difference `A2'` (`:653-667`). Open sub-question: is this a *distinct* L1 operator or just `apply_nonlinear_pencil(T', ·, ·)` with `T'`-construction (the `A2'` divided-difference build, `:653-654`) being the only new content? Law 5 argues for the latter; the `A2'` finite-difference build (`δ = √ε`) may itself deserve a small `divided_difference_operator` primitive. **Defer the decision to the harvest that needs it.**
   - **`nleps_eigenvalue_correction` / Newton-update step** — `Δλ = −(⟨u, w₀⟩ + u₂ᴴw₂)/⟨w, w₀⟩` then the coupled `(λ, v)` update with Armijo backtracking (`:673-714`). This is the genuinely-quasi-Newton step; SLEPc-NEP / Jarlebring-Koskela-Mele literature-anchored, likely `partly-constructive` for the line-search/convergence sub-parts. Highest reconstruction risk; harvest last.
   - **A2 closure family** — `NewtonInterpolationOperator` (decl `palace/linalg/nleps.hpp:246-283`; defs `palace/linalg/nleps.cpp:868-925`) as a concrete `A2`-representation; may warrant a `concepts/nonlinear-operator-interpolation` page rather than an L1 operator (it is below the `A2`-opaque-leaf boundary). Layer-intro-author / concepts territory.

2. **`check_stop_into_carry` / eigsolve unblock relationship.** The NEP Newton loop's convergence test (`if (res < rtol)` at `:599`, the divergence counter `diverged_it` at `:631-643`, the restart/max-restart logic at `:429-443`) is the NEP analogue of the `check_stop_into_carry` reuse the combinator-miner mined for the linear Krylov loop (`reports/2026-05-27T192047Z-combinator-miner-check-stop-into-carry-reuse`). Once `apply_nonlinear_pencil` (residual) + a residual-norm + a stop predicate are firm, the NEP Newton loop can be expressed in the same `iterate_while` / `check_stop_into_carry` L4 vocabulary as the Krylov loop — which would let `eigsolve`'s `direct_newton` orchestration variant unfold at L2/L4 the same way the `krylov-step` body does. This is the path to promoting `eigsolve` from `rough-in` toward firm on the NEP branch: the missing pieces are the per-step atoms (this dispatch lands the first one) and the stop-predicate reuse, not new convergence semantics. Tracked as the link between this L1 work and the standing `eigsolve` rough-in.

3. **`NonlinearPencil[N]` as a new opaque L1 type — concept page?** `apply_nonlinear_pencil` introduces a new construction-bound opaque type (`NonlinearPencil[N]`, binding `K`/`Maybe C`/`M`/`A2`), parallel to `Solver[A]` (`ksp_solve`) and `EigSolver[problem]` (`eigsolve`). It may warrant a `concepts/nonlinear-pencil` page (and/or a `concepts/constructed-operator-factory` cross-reference) once a second consumer (the deflated residual/solve) lands. Not blocking the firm-up; flagged for layer-intro-author.

## Open questions / caveats

- **Layer-intro refresh needed** (layer-intro-author territory, not mine): `book/src/L1/index.md` §Vocabulary cohort currently lists "Firm (12)"; with `apply_nonlinear_pencil` this becomes 13, and a one-line cohort entry should be added under the firm list (the dep-map row is proposed above; the prose-cohort bullet is the layer-intro-author's to write). The new operator also introduces the first NEP-interior atom, worth a sentence in the cohort framing (it is the `apply_linop`-of-the-NEP-loop).
- **`eigsolve` cross-reference**: `book/src/L1/eigsolve.md` should eventually gain a "Dependencies" or "Variant axes" cross-reference to `apply_nonlinear_pencil` (the `direct_newton` orchestration's per-step atom). I did not propose that edit (one-operator-per-dispatch discipline; it is an edit to a *different* operator's entry). Flagged for a follow-up or for the integrator to note.
- **Firm-vs-rough-in judgment call**: I rated `apply_nonlinear_pencil` `firm` despite the zero-test situation that holds `eigsolve` at `rough-in`. The distinction (recorded in Status): `eigsolve`'s rough-in is driven by *convergence-semantics* uncertainty (the `PartialConverged` / iteration-count behaviour that needs a test or literature); `apply_nonlinear_pencil`'s laws are *operator-algebra* facts on fully-specified positive source (linearity in `v`, term decomposition) that do not depend on convergence behaviour — the `apply_linop` / `chebyshev-smoother` precedent (firm on structural grounds despite thin/absent dedicated tests), not the `eigsolve` precedent. If the critic disagrees, the fallback is `rough-in (test-coverage-bounded)` with the same body; the laws stand either way.
