# jacobi-smoother

Mutation-lifted Jacobi (diagonal) preconditioner action: a pure-functional
smoother `y = jacobi_smoother(op, x)` that applies the damped inverse-diagonal
scaling `y = (ω · D⁻¹) ⊙ x` of an SPD operator's diagonal, with the damping
factor `ω` either fixed at construction (default `1.0`) or estimated from the
spectrum (`ω = 0.0` opt-in triggers the spectral-radius-minimizing estimate).
The thinnest constructed-operator gate at L1 — a single elementwise product, no
sweep loop, no workspace. The diagonal-preconditioner-apply primitive of
roadmap §Foundational; the simplest L1 realization of the
`assemble_diagonal` → `reciprocal` → elementwise-product chain
[`assemble-diagonal`](./assemble-diagonal.md) names as its downstream consumer.

## Context

`jacobi_smoother` lifts the `JacobiSmoother<OperType>::Mult` member method
(`palace/linalg/jacobi.cpp:99-104`) — which writes into the destination `y`,
reads the construction-bound inverse diagonal `dinv`, asserts no initial guess,
and dispatches through the namespace-local `Apply(dinv, x, y)` kernel — to a
single pure-functional smoother action over an opaque constructed-operator
closure. The L0 output-arg mutation idiom (`Mult(x, y)` writes through `y`) is
an L0 concern reintroduced in the L1>L0 mutation-rotation theme, not in the L1
signature.

`jacobi_smoother` is a **constructed-operator gate** at L1, in the same family
as [`ksp_solve`](./ksp_solve.md), [`eigsolve`](./eigsolve.md),
[`chebyshev-smoother`](./chebyshev-smoother.md), and
[`divfree-projector`](./divfree-projector.md): its primary argument `op` is a
structured opaque value built once at solver setup (the `SetOperator` step,
`palace/linalg/jacobi.cpp:74-97`), carrying the captured operator `A` only via
its **assembled inverse diagonal** `dinv`, the damping factor `ω`, and the
spectral-bound scaling `sf_max`. It is the **thinnest** such gate at L1: unlike
`chebyshev-smoother` (a fixed-degree polynomial sweep over `pc_it` iterations),
`jacobi_smoother`'s per-call action is **one elementwise product** — no Krylov
update, no polynomial recurrence, no sweep loop. The opaque type carries the
*reduced* operator content (just the inverse diagonal, not the captured `A`
itself), and the apply forgets that the diagonal originated from any operator.

The closely-parallel sibling is [`chebyshev-smoother`](./chebyshev-smoother.md):
both lift the same `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup chain
(`palace/linalg/jacobi.cpp:79-80`; cf. `palace/linalg/chebyshev.cpp:177-178`),
both share the optional `GetLambdaMax` spectral-bound estimation
(`palace/linalg/jacobi.cpp:14-28` is the **same** namespace-local
`GetLambdaMax` definition as `palace/linalg/chebyshev.cpp:13-27`, with the
overloads matching line-for-line). The Jacobi smoother is, in this sense, the
*degree-zero* member of the diagonally-scaled-polynomial-smoother family that
chebyshev parameterises by degree. The L2 unification (a `polynomial_smoother`
combinator subsuming Jacobi as `order=0` and chebyshev as `order≥1`) is a
candidate but **not pursued here** — Jacobi's per-call action is a *plain
elementwise scaling*, not a polynomial action, and the unification would
obscure the apply's identity with the underlying L2 elementwise-product
primitive.

## Signature

    jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]

    jacobi_smoother(op, x) = op.dinv ⊙ x
                           = (ω · diag(A)⁻¹) ⊙ x

Shape contract (bunsen-style; named axes):

- `op` — `JacobiSmoother[N]` — the constructed smoother closure. Bound at
  setup; immutable across calls. Carries:
    - `op.dinv : Tensor[N]` — the damped inverse diagonal `ω · diag(A)⁻¹`.
      Same element-type as `op` (real for `OperType = Operator`, complex for
      `OperType = ComplexOperator` — see Variant axes; this is the chief
      shape-contract divergence from `chebyshev-smoother`, where `dinv` is
      real-valued even for a complex operator).
    - `op.omega : Real` — the damping factor (default `1.0`; `0.0` triggers
      the spectral-radius-minimizing estimate at construction). At apply
      time `omega` is already absorbed into `dinv` (`palace/linalg/jacobi.cpp:90-93`);
      it is carried in the closure for introspection only.
    - `op.sf_max : Real` — spectral-bound scaling factor; consumed only by
      the estimated-damping setup (`omega == 0.0` path).
- `x` — `Tensor[N]` — the input (residual / RHS to smooth). Read-only.
- result — `Tensor[N]` — the post-smoothing output (the L0 `y` after `Mult`
  returns). Same length axis `N`.

`JacobiSmoother[N]` is an *opaque constructed type* at L1: the variant
(real / complex `dinv`) is absorbed; the L1 contract sees only the
smoother-action interface. Setup — the construction of `JacobiSmoother[N]`
from `(A, omega, sf_max)` — is itself a pure function of those inputs modulo
the opaque `spectrum_estimate(A, dinv)` sub-action that estimates `lambda_max`
on the `omega == 0.0` path (see Dependencies); it is described as a separate
setup action, mirroring the L0 `SetOperator` / `Mult` split.

The setup action takes the form

    jacobi_setup :: (A: LinearOperator[N, N], omega: Real, sf_max: Real)
                 -> JacobiSmoother[N]

    jacobi_setup(A, 1.0,   sf_max) = JacobiSmoother{ dinv = reciprocal(diag(A)),         omega = 1.0,   sf_max }
    jacobi_setup(A, ω≠0,   sf_max) = JacobiSmoother{ dinv = ω · reciprocal(diag(A)),     omega = ω,     sf_max }
    jacobi_setup(A, 0.0,   sf_max) = let d = reciprocal(diag(A))
                                         λ = spectrum_estimate(A, d)
                                         ω = 2 / ((sf_max - 1)·λ + λ) = 2 / (sf_max · λ)
                                     in  JacobiSmoother{ dinv = ω · d, omega = ω, sf_max }

The `omega == 0.0` path's `ω = 2/(λ_min + λ_max)` is the optimal damping for
the symmetric stationary Jacobi iteration over the spectral interval
`[λ_min, λ_max]`; with the Palace convention `λ_min = (sf_max−1)·λ_max`
(`palace/linalg/jacobi.cpp:87`) this collapses to `ω = 2 / (sf_max · λ_max)`.
The `sf_max = 1.0` default leaves `λ_min = 0` (no shift), `ω = 2/λ_max`. The
literature anchor for the optimal-`ω` formula is the standard Jacobi-iteration
convergence analysis (Saad, *Iterative Methods for Sparse Linear Systems*,
§4.1) — recorded here as an algorithmic precondition (the SPD assumption is
required for the Hermitian spectral-norm primitive).

## Semantics

`jacobi_smoother(op, x)` returns the elementwise product of `x` with the
damped inverse diagonal `op.dinv = ω · D⁻¹`. The result is a pure function of
`(op, x)`; the same inputs return the same value. The L0 source overwrites the
destination `y` in place; the L1 form drops that — the smoother consumes `x`
and produces a fresh output.

The apply is **inner-product-free** and **iteration-free**: unlike
`chebyshev-smoother` (a `pc_it`-sweep `apply_linop`-residual loop) and
`ksp_solve` (a convergence-tested Krylov method), the Jacobi apply is a
**single elementwise multiplication** — no `apply_linop` call, no residual
recomputation, no reduction. This is the smoother's defining communication
profile: linear-cost, embarrassingly parallel, zero collective. The L0 kernel
(`palace/linalg/jacobi.cpp:30-39` real; `:41-70` complex) realizes the apply
as a single `mfem::forall_switch` element-loop with no cross-element
dependency. The complex apply (`palace/linalg/jacobi.cpp:41-70`) realizes
elementwise complex multiplication componentwise; the `Transpose = true`
template branch (lines 61-69) computes the conjugate-`dinv` apply (it negates
the off-diagonal terms `DII` in the real part and the `XR` term in the
imaginary part — algebraically the conjugate of the forward apply).

**The `Mult` body asserts `!this->initial_guess`** (`palace/linalg/jacobi.cpp:102`)
— Palace forbids calling the Jacobi smoother with an initial guess. This is
distinct from `chebyshev-smoother`, which carries `initial_guess` as a
per-call argument and degenerate-case-absorbs the `false` path
(`palace/linalg/chebyshev.cpp:201-205`). Algebraically the no-initial-guess
restriction is consistent: the Jacobi apply is the linear operator `Y = M·X`
with `M = diag(dinv)` (law 1 below); folding a non-zero initial guess `y₀`
into the apply would require the smoother to compute `y₀ + M·(x − A·y₀)`, an
`apply_linop` call the diagonal smoother explicitly avoids. The restriction
is recorded as a **precondition** on the L1 signature: callers must clear `y`
before invocation, which composes cleanly with the L0 convention that
preconditioners are used as linear maps.

`MultTranspose` aliases `Mult` (`palace/linalg/jacobi.hpp:43`): the Jacobi
smoother is its own transpose. For real `dinv` this is trivially `M = Mᵀ`
(diagonal matrices commute with transpose); for complex `dinv` this is
mathematically the *transpose* (not conjugate-transpose) — the aliasing
implicitly assumes `dinv = dinv` rather than `conj(dinv)`, which is the
correct identity for the *transpose* but **not** the Hermitian transpose. The
conjugate-`dinv` Hermitian-transpose kernel exists in the source
(`palace/linalg/jacobi.cpp:61-69`, the `Transpose = true` template branch) but
is dead code under the current symmetric wiring (no consumer instantiates
`Apply<true>`). Recorded as a non-law caveat; the symmetric-wiring assumption
matches the SPD precondition the smoother is consumed under.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Linearity in `x`.** `jacobi_smoother(op, ·)` is the linear operator
   `M : Tensor[N] -> Tensor[N]` with `M = diag(op.dinv)`. Concretely:
   `jacobi_smoother(op, α·x + β·z) = α · jacobi_smoother(op, x)
                                    + β · jacobi_smoother(op, z)`
   for any scalars `α`, `β` and vectors `x`, `z`. Witnessed directly by the
   elementwise-multiply kernel (`Y[i] = DI[i] · X[i]`,
   `palace/linalg/jacobi.cpp:38`): the apply is the elementwise product `dinv
   ⊙ x`, and elementwise multiplication is linear in each argument. This is
   the structural law that makes `jacobi_smoother` an `apply_linop`-shaped
   operation (it consumes a vector and returns its action under the linear
   map `M = diag(dinv)`).

2. **Diagonal-operator round-trip with `assemble_diagonal`.** For the
   default-damping setup (`omega = 1.0`):
   `jacobi_smoother(jacobi_setup(A, 1.0, sf_max), x)
        = reciprocal(assemble_diagonal(A)) ⊙ x = D⁻¹ ⊙ x`
   where `D = diag(A)`. Witnessed by the setup chain
   `op.AssembleDiagonal(dinv); dinv.Reciprocal();` (`palace/linalg/jacobi.cpp:79-80`).
   Composes the firm
   [`assemble-diagonal`](./assemble-diagonal.md) law 5 (the diagonal of a
   diagonal operator recovers its defining vector) with the elementwise
   reciprocal: `jacobi_smoother(jacobi_setup(Diag(d), 1.0, ·), x) = d⁻¹ ⊙ x`.
   This is the law that names `jacobi_smoother` as the explicit realization
   of the diagonal-preconditioner-apply chain
   `assemble_diagonal → reciprocal → elementwise_product` that the L1
   `assemble-diagonal` chapter's §Dependencies block forward-references.

3. **Damping absorption (`omega`-into-`dinv`).** For any `ω ≠ 0`:
   `jacobi_setup(A, ω, sf_max) = scale(ω, jacobi_setup(A, 1.0, sf_max))`,
   meaning the damping factor is *absorbed into the closure's `dinv`* and
   does not surface in the apply. Witnessed by
   `if (omega != 1.0) { dinv *= omega; }`
   (`palace/linalg/jacobi.cpp:90-93`). Operationally:
   `jacobi_smoother(jacobi_setup(A, ω, ·), x) = ω · (D⁻¹ ⊙ x) = (ω · D⁻¹) ⊙ x`,
   reducing the damped Jacobi to its plain form with a pre-scaled inverse
   diagonal. This is the *closure-internal absorption* sibling of the
   `chebyshev-smoother` law 5 degenerate-case absorption (`initial_guess =
   false` → fold `y = 0` into the apply): Jacobi absorbs the damping at
   *setup time* rather than at apply time. The `omega == 1.0` fast path
   (skip the `dinv *= omega` element loop) is a transparent performance
   trick — algebraically identical to `dinv *= 1.0`.

4. **Estimated-damping degenerate case (`omega = 0.0`).** When `omega = 0.0`,
   the setup substitutes `ω = 2 / (sf_max · lambda_max)` where `lambda_max =
   spectrum_estimate(A, reciprocal(diag(A)))` is the spectral radius of
   `D⁻¹·A` (`palace/linalg/jacobi.cpp:84-89`). The apply law is identical to
   the `omega ≠ 0` case (law 1 + law 3 with the substituted `ω`):
   `jacobi_smoother(jacobi_setup(A, 0.0, sf_max), x) = (ω* · D⁻¹) ⊙ x`
   for the substituted optimal `ω* = 2/(sf_max · λ_max(D⁻¹A))`. This is a
   *setup-side specialization*, not an apply-time branch — at the L1 apply
   the smoother has already committed to a fixed `op.dinv`.

5. **Self-transpose under symmetric wiring.** `jacobi_smoother_transpose(op,
   x) = jacobi_smoother(op, x)`. Witnessed by
   `MultTranspose(x, y) const override { Mult(x, y); }`
   (`palace/linalg/jacobi.hpp:43`). For real `dinv` this is the mathematical
   identity `M = Mᵀ` for any diagonal matrix; for complex `dinv` this is the
   *transpose* (not conjugate-transpose) — see Semantics paragraph on the
   dead-code conjugate-`dinv` Hermitian kernel.

6. **Variant-axis collapse with `assemble_diagonal`'s representation
   axis.** The Jacobi smoother is *representation-agnostic*: whether `A`'s
   diagonal was assembled exactly (sparse CSR) or approximately (matrix-free
   high-order Nedelec), the smoother applies the assembled `dinv` as-is. The
   load-bearing matrix-free-Nedelec approximation
   ([`assemble-diagonal`](./assemble-diagonal.md) non-law)
   propagates *transparently* through the Jacobi apply: `dinv` may be an
   approximate inverse diagonal, but the smoother *as a preconditioner*
   tolerates this (`palace/linalg/jacobi.hpp:15-16` comment: "which allows
   for (approximate) diagonal construction for matrix-free operators"). The
   smoother's correctness as a *linear map* is unaffected; the precondition
   *quality* may be reduced. Recorded as a propagated non-law, not a fresh
   one.

Laws that explicitly **do not** hold:

- **Hermitian-transpose identity for complex `dinv`.** For complex `dinv`,
  `jacobi_smoother_hermitian_transpose(op, x) = jacobi_smoother(op_conj, x)`
  where `op_conj.dinv = conj(op.dinv)` — but Palace's `MultTranspose` aliases
  the *transpose* (not Hermitian) kernel
  (`palace/linalg/jacobi.hpp:43` calls `Mult`, not `Apply<true>`), so the
  Palace-realized `MultTranspose` is the **transpose** for complex `dinv`,
  not the Hermitian. The conjugate-`dinv` Hermitian kernel exists in
  `Apply<Transpose=true>` (`palace/linalg/jacobi.cpp:61-69`) but is **dead
  code** under the current symmetric wiring. Recorded as a non-law because
  the law one might *expect* (Hermitian-transpose = conj-`dinv` apply) is
  not the law the source *realises* (transpose = same apply). Aligns with
  the SPD precondition under which the smoother is consumed
  (`palace/linalg/jacobi.cpp:16` comment: "Assumes A SPD (diag(A) > 0)").

- **Initial-guess absorption.** Unlike `chebyshev-smoother` (law 5: absorbs
  `initial_guess = false` as `y = 0`), `jacobi_smoother` does **not** carry
  an `initial_guess` argument — the `Mult` body asserts
  `!this->initial_guess` (`palace/linalg/jacobi.cpp:102`). Callers must
  zero `y` before invocation. This is a precondition on the L1 signature,
  not an algebraic law that fails.

- **Iteration / multi-sweep equivalence.** `jacobi_smoother` is a
  *single-step* application: there is no `pc_it` parameter (contrast
  `chebyshev-smoother`'s `op.pc_it` outer sweeps). Two consecutive
  applications `M·M·x = M²·x = D⁻²·x` (with `ω = 1`) is *not* a Jacobi
  sweep on the residual (which would be `M·(x − A·M·x)`); it is the
  *square* of the preconditioner map. The Jacobi *iteration* (the
  Richardson sweep `y ← y + M·(x − A·y)`) is the consumer's
  responsibility, realized by wrapping `jacobi_smoother` in a Krylov or
  multigrid loop — the bare L1 operator is just the preconditioner action,
  not the iteration. The standalone-Jacobi-iteration form is the
  conventional Jacobi *as a solver*, not how Palace uses it (Palace consumes
  the smoother as a preconditioner inside a Krylov solver,
  `palace/linalg/ksp.cpp:199`, or as a level-smoother inside multigrid).

- **Bit-determinism across operator representations.** Inherited from
  [`assemble-diagonal`](./assemble-diagonal.md) non-law: a matrix-free
  high-order Nedelec `A` yields a *value-approximate* `dinv` (face-dof
  sharing in 3D), so the apply value differs from the assembled-`A` case.
  Load-bearing per CLAUDE.md.

## Dependencies

`jacobi_smoother` depends (at L1) on:

- [`assemble-diagonal`](./assemble-diagonal.md) — the
  `op.AssembleDiagonal(dinv)` setup step (`palace/linalg/jacobi.cpp:79`).
  Reads the operator's main diagonal once at setup, then the operator `A`
  itself is **dropped** — the closure carries only `dinv`. This is the
  decisive *forgetting* that makes the Jacobi gate the thinnest constructed
  operator at L1.

- [`reciprocal`](./reciprocal.md) and [`elementwise_product`](./elementwise_product.md)
  (the diagonal-preconditioner-apply chain in
  [`assemble-diagonal`](./assemble-diagonal.md) §Dependencies). At L1 the apply *is* a
  single elementwise multiply, so the operator's body is one elementwise-multiply call;
  the setup-side `dinv.Reciprocal()` (`palace/linalg/jacobi.cpp:80`) is one
  elementwise-reciprocal call.

- `spectrum_estimate` (setup only, `omega == 0.0` path) — the
  dominant-eigenvalue estimate of `D⁻¹·A`, via the Hermitian spectral-norm
  primitive shared with `chebyshev-smoother`. At L0 this is the
  namespace-local `GetLambdaMax(comm, A, dinv)` (`palace/linalg/jacobi.cpp:14-28`)
  → `linalg::SpectralNorm(comm, DinvA, hermitian)` (line `:19` real
  passes literal `true`; line `:27` complex passes `A.IsReal()`) — the
  **identical** definition to `palace/linalg/chebyshev.cpp:13-27`. Opaque at
  L1 — it is a setup sub-action producing the scalar `lambda_max`, not part
  of the per-call action. A firm `spectrum_estimate` (the
  `SpectralNorm` power-iteration sibling) is the same open L1 candidate
  named in `chebyshev-smoother`'s dependencies; promotion is out of scope
  for this entry.

The per-call action has **no L1 operator dependencies** in the strict sense:
it is one elementwise product. Where `chebyshev-smoother` lists
`apply_linop` as a direct dependency (the residual `r = x − A·y` and
direction-image `A·d` per sweep), `jacobi_smoother` has *no* `apply_linop`
call in its apply — that is the smoother's defining lightness.

## Variant axes

`jacobi_smoother` has two orthogonal variant axes at L1; both are absorbed
into the constructed-operator closure (level (c) of
[`variant-absorption`](../concepts/variant-absorption.md)).

- **element-type**: `real` | `complex`. The L0 source instantiates both
  (`template class JacobiSmoother<Operator>;` and `<ComplexOperator>`,
  `palace/linalg/jacobi.cpp:106-107`). The smoother action is identical in
  form — one elementwise product — and the per-element kernel dispatches on
  element type (`palace/linalg/jacobi.cpp:30-39` real; `:41-70` complex).
  **Divergence from `chebyshev-smoother`**: chebyshev carries `dinv` as
  real-valued even for a complex `A` (`palace/linalg/chebyshev.hpp:37`
  comment: "real-valued for now"); Jacobi carries `dinv` as the *full
  element-type of OperType* — a complex `A` yields a complex `dinv`
  (`palace/linalg/jacobi.hpp:28` `VecType dinv;` with `VecType =
  ComplexVector` for `OperType = ComplexOperator`). The complex
  `ComplexVector::Reciprocal` implements the full complex reciprocal
  `1/(a+bi) = (a−bi)/|a+bi|²` (`palace/linalg/vector.cpp:248-261`), giving
  a true complex inverse diagonal. This is a *deliberate* divergence from
  chebyshev (the diagonally-scaled Chebyshev recurrence needs only the
  magnitude information; the Jacobi apply respects the complex structure
  fully).

- **damping-mode**: `default (ω = 1.0)` | `fixed (ω ≠ 0)` | `estimated
  (ω = 0)`. The L0 source carries the three modes as ctor-argument
  branches (`palace/linalg/jacobi.hpp:34` ctor with `omega = 1.0` default
  + `sf_max = 1.0` default; `palace/linalg/jacobi.cpp:84-93` the setup
  branch on `omega == 0.0` vs `omega != 1.0` vs `omega == 1.0`). At L1 these
  collapse to one operator parameterised by `op.dinv`'s *committed*
  damping value (the `setup` action computes the absorbed `dinv`; the
  apply does not branch on damping mode). Witnessed by the five call
  sites: `LinearSolver::JACOBI` dispatch (`palace/linalg/ksp.cpp:199`),
  Floquet-correction (`palace/linalg/floquetcorrection.cpp:65`),
  space-operator (`palace/models/spaceoperator.cpp:640`),
  time-operator (`palace/models/timeoperator.cpp:85`) — all four use the
  default `omega = 1.0`; the error-estimator
  (`palace/linalg/errorestimator.cpp:75-77`) opts into the estimated
  `omega = 0.0` mode with the comment "Use eigenvalue estimate to compute
  optimal Jacobi damping parameter."

The **`sf_max` spectral-bound scaling factor** is a construction parameter
carried in `op.sf_max`, *not* a variant axis — it parameterises one
operator (per call site), not selection among operators. It surfaces only
in the `omega = 0.0` setup arithmetic (`palace/linalg/jacobi.cpp:87-88`,
`λ_min = (sf_max − 1) · λ_max`); on the `omega = 1.0` default path it is
unused.

The **representation axis of the underlying `A`** (sparse-CSR /
matrix-free / parallel-wrapped / complex-wrapped) is *collapsed at setup*
through the [`assemble-diagonal`](./assemble-diagonal.md) operator's own
representation-axis absorption — by the time `dinv` is committed to the
closure, the representation distinction has been erased. The
matrix-free-Nedelec approximation propagates as a non-law (law 6 above);
the variant absorption itself is inherited, not re-stated.

## L1 vs L0 distinction

- **L0**: one template class `JacobiSmoother<OperType>` deriving
  `Solver<OperType>`. `Mult(x, y) const` writes through `y` (one
  `mfem::forall_switch` element-loop, `palace/linalg/jacobi.cpp:30-39` real;
  `:41-70` complex), reads the construction-bound `dinv`, asserts
  `!this->initial_guess` (`palace/linalg/jacobi.cpp:102`).
  `MultTranspose(x, y) const override` aliases `Mult` directly
  (`palace/linalg/jacobi.hpp:43`). `SetOperator(op)` computes `dinv`
  in-place: `dinv.SetSize(op.Height()); op.AssembleDiagonal(dinv);
  dinv.Reciprocal();` (`palace/linalg/jacobi.cpp:77-80`), then on the
  `omega == 0.0` branch invokes `GetLambdaMax(comm, op, dinv)`
  (`palace/linalg/jacobi.cpp:86`) and computes the optimal damping; on the
  `omega != 1.0` branch folds the damping into `dinv` by `dinv *= omega`
  (`palace/linalg/jacobi.cpp:92`).
- **L1**: one pure-functional smoother action `y = jacobi_smoother(op, x)`
  over an opaque constructed closure `op` carrying `(dinv, omega, sf_max)`.
  No destination buffer in the signature, no `initial_guess` parameter
  (precondition: caller zeros `y`), no workspace. Element-type and
  damping-mode collapsed into the closure (the apply does not branch on
  either). The spectral-bound estimation is a setup sub-action. The
  closure carries the *reduced* operator content — the underlying `A` is
  forgotten once `dinv` is committed.

## Evidence

- `palace/linalg/jacobi.hpp:14-16` — class doc comment: "Simple Jacobi
  smoother using the diagonal vector from OperType::AssembleDiagonal(),
  which allows for (approximate) diagonal construction for matrix-free
  operators." — the source-comment witness for the
  matrix-free-approximate-diagonal propagation (law 6).
- `palace/linalg/jacobi.hpp:19` — `class JacobiSmoother : public
  Solver<OperType>` — the class declaration; the `Solver<OperType>` base
  binds `initial_guess` and the `Mult` / `MultTranspose` virtuals.
- `palace/linalg/jacobi.hpp:28` — `VecType dinv;` — the inverse-diagonal
  member (`VecType = Vector` for real `OperType = Operator`, `=
  ComplexVector` for complex `OperType = ComplexOperator`); the chief
  shape-contract divergence from `chebyshev-smoother`.
- `palace/linalg/jacobi.hpp:31` — `double omega, sf_max;` — damping factor
  and spectral-bound scaling members.
- `palace/linalg/jacobi.hpp:34` — `JacobiSmoother(MPI_Comm comm, double
  omega = 1.0, double sf_max = 1.0)` — ctor signature; the three damping
  modes are selected by ctor-argument values.
- `palace/linalg/jacobi.hpp:43` — `void MultTranspose(const VecType &x,
  VecType &y) const override { Mult(x, y); }` — the transpose self-alias
  (law 5); also the source of the dead-code conjugate-`dinv` Hermitian
  caveat.
- `palace/linalg/jacobi.cpp:14-28` — `GetLambdaMax` (real + complex
  overloads): builds `DinvA = Dinv·A` and returns `linalg::SpectralNorm(comm,
  DinvA, hermitian)` — the **identical** namespace-local definition to
  `palace/linalg/chebyshev.cpp:13-27`. The opaque `spectrum_estimate`
  setup sub-action.
- `palace/linalg/jacobi.cpp:30-39` — real `Apply<Transpose>(dinv, x, y)`:
  `mfem::forall_switch(use_dev, N, [=] (int i) { Y[i] = DI[i] * X[i]; });`
  — the elementwise-multiply kernel that realises the L1 apply (law 1
  witness). The `Transpose` template parameter is unused for real `dinv`
  (transpose of a diagonal map is itself).
- `palace/linalg/jacobi.cpp:41-70` — complex `Apply<Transpose>(dinv, x, y)`:
  the forward branch (lines 52-60) computes elementwise complex
  multiplication; the `Transpose = true` branch (lines 61-69) computes the
  conjugate-`dinv` apply (algebraically `conj(dinv) ⊙ x`). The dead-code
  Hermitian-transpose kernel; unreferenced under symmetric wiring.
- `palace/linalg/jacobi.cpp:74-97` — `JacobiSmoother<OperType>::SetOperator(op)`:
  the setup body. `dinv.SetSize(op.Height())` (line 77),
  `op.AssembleDiagonal(dinv)` (line 79), `dinv.Reciprocal()` (line 80) —
  the [`assemble-diagonal`](./assemble-diagonal.md) consumption +
  elementwise reciprocal. Then on `omega == 0.0` (lines 84-89): `auto
  lambda_max = GetLambdaMax(comm, op, dinv); auto lambda_min = (sf_max -
  1.0) * lambda_max; omega = 2.0 / (lambda_min + lambda_max);` — the
  spectral-radius-minimizing optimal damping (law 4). On `omega != 1.0`
  (lines 90-93): `dinv *= omega;` — the damping absorption (law 3); the
  `omega == 1.0` skip is a transparent performance trick. Final
  `this->height = op.Height(); this->width = op.Width();` (lines 95-96)
  matches the `Solver<OperType>` base contract.
- `palace/linalg/jacobi.cpp:99-104` — `JacobiSmoother<OperType>::Mult(x, y)
  const`: the apply body. `MFEM_ASSERT(!this->initial_guess,
  "JacobiSmoother does not use initial guess!");` (line 102) — the
  no-initial-guess precondition. `Apply(dinv, x, y);` (line 103) —
  dispatches to the namespace-local kernel. The entire per-call action is
  this single dispatch.
- `palace/linalg/jacobi.cpp:106-107` — `template class
  JacobiSmoother<Operator>; template class
  JacobiSmoother<ComplexOperator>;` — the element-type variant axis
  instantiation.
- `palace/linalg/solver.hpp:32-33` — `// Whether or not to use the second
  argument of Mult() as an initial guess. bool initial_guess;` — the
  `Solver<OperType>` base member the Jacobi `Mult` asserts negation of.
- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()`:
  realises the full complex reciprocal `1/(a+bi) = (a−bi)/|a+bi|²` as
  componentwise updates `XR[i] *= s; XI[i] *= -s;` with `s =
  1/(XR[i]² + XI[i]²)`. The element-type variant axis witness for the
  complex-dinv case (divergence from chebyshev's real-only `dinv`).
- `palace/linalg/ksp.cpp:198-200` — consumer: `case LinearSolver::JACOBI: pc
  = std::make_unique<JacobiSmoother<OperType>>(comm); break;` — the
  default-damping (`omega = 1.0`) preconditioner-instantiation site
  inside `ConfigurePreconditioner`. The principal Jacobi consumer; routes
  the Jacobi smoother into the Krylov-solver preconditioner slot.
- `palace/linalg/errorestimator.cpp:75-77` — consumer: `// Use eigenvalue
  estimate to compute optimal Jacobi damping parameter. pc =
  std::make_unique<JacobiSmoother<OperType>>(fespaces.GetFinestFESpace().GetComm(),
  0.0);` — the **only** `omega = 0.0` estimated-damping call site;
  witnesses the variant axis's third value.
- `palace/linalg/floquetcorrection.cpp:65` — consumer: `auto jac =
  std::make_unique<JacobiSmoother<OperType>>(rt_fespace.GetComm());` —
  default-damping consumer (uses ctor default `omega = 1.0`).
- `palace/models/spaceoperator.cpp:640` — consumer: `auto jac =
  std::make_unique<JacobiSmoother<Operator>>(comm);` — default-damping
  real-`OperType` consumer.
- `palace/models/timeoperator.cpp:85` — consumer: `auto jac =
  std::make_unique<JacobiSmoother<Operator>>(comm);` — default-damping
  real-`OperType` consumer; the transient-solver path.
- `palace/linalg/chebyshev.cpp:177-178` — sibling-precedent: the
  *identical* `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup chain
  inside `ChebyshevSmoother::SetOperator` — establishes
  `jacobi_smoother` as the degree-zero member of the
  diagonally-scaled-polynomial-smoother family.
- `palace/linalg/chebyshev.cpp:13-27` — sibling-precedent: the line-for-line
  *identical* `GetLambdaMax` definition shared between
  `chebyshev.cpp` and `jacobi.cpp` — the same `spectrum_estimate` opaque
  sub-action.
- `book/src/L1/assemble-diagonal.md` — the sibling firm L1 operator;
  `jacobi-smoother` realizes the
  `assemble_diagonal → reciprocal → elementwise_product` chain that
  `assemble-diagonal` §Dependencies forward-references.
- `book/src/L1/chebyshev-smoother.md` — the sibling firm
  constructed-operator gate; the structural template for the L1 entry
  shape. The diagonally-scaled-polynomial-smoother sibling.
- *Negative anchor*: no Jacobi-specific unit test under
  `reference/palace/test/unit/` (`grep -rn 'Jacobi' test/unit/` returns
  one unrelated `// MFEM's GradientIntegrator only supports square
  Jacobians` match at `test-libceed.cpp:1128`). Per the
  `chebyshev-smoother` firm-without-dedicated-test precedent, the
  firm-on-positive-structure judgement does not require a dedicated test
  here either.

## Status

`firm` — the signature is a direct transcription of the `Mult` member method.
