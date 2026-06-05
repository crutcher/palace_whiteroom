---
edges:
  reference:
    - L1/eigsolve
    - L2/eigsolve
    - L3/eigsolve
    - L0/eigensolver-wrapper
    - concepts/ksp_solve
    - concepts/solver-as-operator
    - concepts/sequential-obstruction
    - concepts/constructed-operators
    - concepts/variant-absorption
    - concepts/solve-monad
    - concepts/apply_linop
    - L1/apply_nonlinear_pencil
    - L1/nleps_jacobian_action
    - L1/nleps_eigenvalue_correction
    - L1/nleps_deflated_residual
    - L1/nleps_deflated_solve
    - L1-L0/eigsolve-mutation-rotation
    - L1-L0/eigsolve-convergence-reason-mapping
---
# eigsolve

Cross-cutting concept page for the **generalized-eigenproblem solve** and its
`EigSolver[problem]` opaque type. The authoritative operator definitions
(signatures, algebraic laws, variant axes, evidence) live across the three
firm/landed chain entries — [`L1/eigsolve`](../L1/eigsolve.md) (firm),
[`L2/eigsolve`](../L2/eigsolve.md) (firm),
[`L3/eigsolve`](../L3/eigsolve.md) (partial-obstruction) — and the L0 C++
surface is catalogued in [`L0/eigensolver-wrapper`](../L0/eigensolver-wrapper.md).
This page is the **navigational/conceptual home**: the `EigSolver[problem]`
opaque-type framing, the shift-invert composition seam, and the
opaque-library-ownership fact that drives the L3 verdict. It does **not**
restate the algebraic laws — those live in the L_n entries, and if this page
and any L_n entry disagree on a factual claim, the L_n entry wins.

## One-line semantics

`result = eigsolve(E, control)` — apply a construction-bound eigensolver `E`
to a per-call `control` to obtain the converged eigenpairs `(λᵢ, xᵢ)` of the
generalized eigenproblem bound inside `E` (linear `K x = λ M x`, quadratic
`(K + λC + λ²M) x = 0`, or nonlinear `(K + λC + λ²M + A2(λ)) x = 0`). The
result is an `EigResult` record carrying the converged eigenvalues,
eigenvectors, per-pair error, and a sum-typed `status` (`Converged` /
`PartialConverged` / `MaxIterReached` / `LinearSolveFailed`). See the
[L1 entry](../L1/eigsolve.md) for the full `EigSolver` / `EigControl` /
`EigResult` record shapes.

## The `EigSolver[problem]` opaque type

`EigSolver[problem]` is the L1 **opaque, construction-bound eigensolver value**
— the eigenproblem analogue of the `Solver<OperType>` framing in
[`solver-as-operator`](./solver-as-operator.md) and of the `KSP` value behind
[`ksp_solve`](./ksp_solve.md). It binds, at construction time, everything the
per-call surface treats as invariant:

- the **problem operators** — `K`, `M` (linear); `K`, `C`, `M` (quadratic); plus
  the operator-valued nonlinearity `A2 : Complex → ComplexOperator` (nonlinear);
- the **inner linear solver** `E.linear : Solver[A]` (the action of `M⁻¹` or
  `(K − σM)⁻¹` per spectral-transform mode — itself a constructed-operator
  absorption, see the composition seam below);
- the optional **B-matrix** for weighted inner products and the optional
  **divergence-free projector**;
- the **spectral-transform** shift `σ` and mode, the `WhichType` spectrum target
  (one of nine — `palace/linalg/eps.hpp:31-42`), the `ScaleType` Higham scaling
  (`NONE` / `NORM_2` — `palace/linalg/eps.hpp:25-29`), the requested mode count,
  tolerance, and iteration cap.

The phantom `problem` carries the **problem-type tag** (`Linear` / `Quadratic` /
`Nonlinear`) and the square operator axis `N`. At L0, this opaque type is one of
three `EigenvalueSolver` subclasses (`palace/linalg/eps.hpp:57-74` — the three
`SetOperators` overloads, each `MFEM_ABORT` by default); `EigSolver[problem]`
hides which subclass, which solver library, and which internal orchestration was
chosen. `eigsolve` is the **complex-only** operator — Palace's
`EigenvalueSolver` surface takes `ComplexOperator` throughout, with no
real-element overload (the real-symmetric case is promoted to complex).

**`eigsolve` is the second constructed-operator gate** (after `ksp_solve`),
and the first operator to compose *two* layers of solver-as-operator: its inner
`E.linear` is itself an opaque `ksp_solve`-shaped value. The per-step
transformed-operator application performs an `apply_linop` against a
`Solver[A]`-wrapped inverse — structurally the same nesting as a preconditioner
applied inside an iterative solver, composed-not-inherited.

## The shift-invert spectral-transform composition seam

The L2/L3 layers open the **per-step body** of the eigensolve into a single
named composition — the **shift-invert spectral transformation**. The
generalized eigenproblem `K x = λ M x` is hard to solve directly for interior or
clustered spectra; the Krylov-eigensolver remedy is to iterate against a
*spectrally-transformed* operator whose dominant eigenvalues correspond to the
target eigenvalues of the original problem. Palace uses **shift-and-invert**:
iterate against `(K − σM)⁻¹ M`, whose eigenvalues `1/(λ − σ)` are largest for
`λ` nearest the shift `σ`.

That transformed-operator application is the composition seam — an
[`apply_linop`](./apply_linop.md) against `M` (or the PEP/NEP operand) fed into
an inner [`ksp_solve`](./ksp_solve.md) inverting the shifted operator
`(K − σM)`:

```text
apply_shift_invert op v =
  let w  = apply_linop op.operand v        -- apply against M (linear) / K (none) / PEP block L₁ (quadratic)
  let y  = ksp_solve op.inv w              -- inner ksp_solve inverting the shifted operator (K − σM)
  in scale_untransform op y                -- per-backend γ / δ un-scale (informational coordinate bookkeeping)
```

This `apply_linop ▷ ksp_solve` composition is the firm L2/L3 content. The
shift-invert *setup* binds it: `SetShiftInvert(σ, precond)`
(`palace/linalg/eps.hpp:119` abstract; `palace/linalg/slepc.cpp:379-394` SLEPc)
selects the spectral-transform mode (`STSINVERT` exact-inverse vs `STPRECOND`
approximate-inverse), and `SetLinearSolver(ksp)` binds the inner solver
(`palace/linalg/arpack.cpp:191-194` / `palace/linalg/slepc.cpp:364-367`, both
`opInv = &ksp`). The returned eigenvalues are **un-transformed back to
original-problem coordinates** at the extraction boundary
(`palace/linalg/slepc.cpp:711-716`, `return l * gamma`); the caller never sees
the `1/(λ − σ)`-space values the iteration works in. See the
[L2 entry](../L2/eigsolve.md) for the full composition treatment and the
[`constructed-operators`](./constructed-operators.md) framing of the shifted
operand.

## Opaque-library ownership — why L3 is a partial-obstruction

The composition seam above is the **body** of the eigensolve. The **loop** that
folds it — Krylov-Schur restart, Arnoldi/Lanczos basis extension, Rayleigh-Ritz
extraction, the convergence test — is **entirely library-owned**, and this is
the load-bearing fact for the L3 verdict:

- **SLEPc**: the whole iteration is one opaque call `EPSSolve(eps)`
  (`palace/linalg/slepc.cpp:694`). Palace supplies only a PC-shell callback and
  the original-operator shell matvecs; there is no Palace loop at all.
- **ARPACK**: the iteration is a **reverse-communication-interface (RCI)** loop.
  Palace's `while` loop calls the ARPACK driver `naupd`
  (`palace/linalg/arpack.cpp:318`) and dispatches the per-step matvec only when
  `naupd` requests it — the loop body is a callback dispatcher, not an algorithm;
  all eigen-iteration logic is inside `naupd`.
- **direct-Newton**: `QuasiNewtonSolver::Solve()` (`palace/linalg/nleps.cpp:351`)
  runs a Palace-owned Newton outer loop — the one orchestration that *is*
  Palace-authored, but for the nonlinear problem-type, where the per-step body
  is itself the NEP-interior cohort (see below).

Because Palace authors **no eigen-iteration kernel/driver pair** analogous to the
([`krylov-step`](../L3/krylov-step.md), [`ksp_solve`](../L3/ksp_solve.md)) pair,
the L3 iteration rotation **cannot render the loop** — there is nothing to
rotate. The body lifts cleanly to a global tensor-field expression; the loop is
a witnessed [`sequential-obstruction`](./sequential-obstruction.md) rooted in
opaque-library-ownership. This is the **canonical opaque-library
partial-obstruction** (distinct from L3 [`chebyshev`](../L3/chebyshev.md), whose
obstruction is numerical-stability of an in-house recurrence). See the
[L3 entry](../L3/eigsolve.md) for the full obstruction treatment.

## The eigsolve cohort

The chain composes against a cluster of cohort entries — the layers and
operators that reference this concept:

- **Chain**: [`L1/eigsolve`](../L1/eigsolve.md) (firm) →
  [`L2/eigsolve`](../L2/eigsolve.md) (firm) →
  [`L3/eigsolve`](../L3/eigsolve.md) (partial-obstruction). L0 surface:
  [`L0/eigensolver-wrapper`](../L0/eigensolver-wrapper.md).
- **Inner-solve dependency**: [`ksp_solve`](./ksp_solve.md) — the inner
  `E.linear` inverting `(K − σM)`; the first layer of solver-as-operator the
  eigensolve composes against.
- **NEP-interior cohort** (the nonlinear problem-type body): the L1 atoms
  [`apply_nonlinear_pencil`](../L1/apply_nonlinear_pencil.md),
  [`nleps_jacobian_action`](../L1/nleps_jacobian_action.md),
  [`nleps_eigenvalue_correction`](../L1/nleps_eigenvalue_correction.md),
  [`nleps_deflated_residual`](../L1/nleps_deflated_residual.md),
  [`nleps_deflated_solve`](../L1/nleps_deflated_solve.md) — the constituents of
  the `QuasiNewtonSolver` direct-Newton orchestration.
- **L1>L0 themes**: [`eigsolve-mutation-rotation`](../L1-L0/eigsolve-mutation-rotation.md)
  (the per-orchestration body reintroduction; constructive treatment of
  `LinearSolveFailed` / `iterations`),
  [`eigsolve-convergence-reason-mapping`](../L1-L0/eigsolve-convergence-reason-mapping.md).

## Caveats and load-bearing facts

- **Constructed result fields.** `EigStatus::LinearSolveFailed` and
  `EigResult.iterations` are **L1-constructive** — introduced by the L1 form to
  make inner-solver coupling and iteration count visible at the L1 surface; they
  have no direct L0 anchor (the inner `opInv->Mult` is `void`-returning and never
  queries `GetConverged`; no iteration-count accessor exists on the
  `EigenvalueSolver` virtual surface). The L1>L0
  [`eigsolve-mutation-rotation`](../L1-L0/eigsolve-mutation-rotation.md) theme
  records the materialisation shape. See the L1 entry's §Signature callouts.
- **Partial convergence is the distinguishing semantic feature** relative to
  `ksp_solve`: the L0 `Solve() → int` count can be `0 < K < K_max` without being
  an outright failure (`palace/drivers/eigensolver.cpp:367`). The L1 form
  structures this as the `Converged` vs `PartialConverged` status distinction.
- **Coordinate convention.** Returned eigenvalues are in **original-problem
  coordinates** uniformly across all four backends (ARPACK / SLEPc-EPS /
  SLEPc-PEP via solve-scaled-then-un-scale; SLEPc-NEP via solve-and-return-
  un-scaled). The `scaling_gamma` / `scaling_delta` fields are informational. See
  L1 law 5 for the per-backend un-scale anchors.
- **Load-bearing non-determinism.** The result is referentially transparent in
  `(E, control)` only modulo four non-determinism sources (reduction-tree
  non-associativity in the inner BLAS-1 ops, per-backend floating-point ordering,
  inner-`ksp_solve` non-determinism propagated to the outer eigensolve, and
  library-internal RNG for initial-space generation). Cited in full in the L1
  entry's §Semantics.

## See also

- [`L1/eigsolve`](../L1/eigsolve.md) — authoritative L1 operator entry: full
  `EigSolver` / `EigControl` / `EigResult` shapes, the five algebraic laws,
  variant axes, complete L0 evidence. **If this page and the L1 entry disagree on
  any factual claim about the Palace surface, the L1 entry wins.**
- [`L2/eigsolve`](../L2/eigsolve.md) — the named shift-invert composition
  (`apply_linop ▷ ksp_solve`), composition-identity laws on positive source.
- [`L3/eigsolve`](../L3/eigsolve.md) — the iteration-rotation view; the
  body-lifts / loop-doesn't partial-obstruction.
- [`ksp_solve`](./ksp_solve.md) — the inner linear solve; the first
  constructed-operator gate `eigsolve` composes against.
- [`solver-as-operator`](./solver-as-operator.md) — the type-level rotation the
  `EigSolver[problem]` / `Solver[A]` framing rests on.
- [`sequential-obstruction`](./sequential-obstruction.md) — the classification
  for the opaque-library-owned eigen-iteration loop.
- [`constructed-operators`](./constructed-operators.md) /
  [`variant-absorption`](./variant-absorption.md) — the shifted-operand
  construction and the backend-orchestration absorption.
- [`solve-monad`](./solve-monad.md) — the future L4 outer-coordination surface
  the L1 eigsolve anchors (with sum-typed termination richer than `ksp_solve`'s
  soft-fail).
