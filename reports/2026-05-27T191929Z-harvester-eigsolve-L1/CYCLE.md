---
agent: harvester
invoked_at: 2026-05-27T191929Z
scope: L1 operator: eigsolve
status: integrated
integrated_at: 2026-05-27T200036Z
integration_commit: 8259f20
integration_notes: Applied cleanly via integrator-per-report pass 3 of cycle-009. L1 rough-in (test-coverage-bounded) landed; second constructed-operator gate at L1 composing against ksp_solve (first multi-level constructed-operator composition in firm+rough-in L1 vocabulary). New "Rough-in (test-coverage-bounded)" L1 cohort subsection added (cohort-purity preserving — Firm count unchanged at 8). Partially closes cycle-008 OQ eigsolve-l1-operator-rough-in-candidate (status open -> partially-answered); 4 firm-promotion follow-up OQs opened.
inputs:
  - book/src/L0/eigensolver-wrapper.md (cycle-008 bundle-4 L0 anchor)
  - book/src/L1/ksp_solve.md (cycle-007 firm; precedent L1 sister chapter)
  - book/src/L1/index.md (current L1 Part overview + dep-map)
  - reference/palace/palace/linalg/eps.hpp (abstract base — full read)
  - reference/palace/palace/linalg/arpack.cpp (RCI Solve body — sampled)
  - reference/palace/palace/linalg/slepc.cpp (shell-matrix Solve — sampled)
  - reference/palace/palace/linalg/nleps.cpp (QuasiNewtonSolver::Solve — sampled)
  - reference/palace/palace/models/modeeigensolver.cpp (call site — sampled)
  - reference/palace/palace/drivers/eigensolver.cpp (main driver — sampled)
  - reference/palace/test/unit/test-boundarymodeoperator.cpp (indirect-only test coverage)
  - scaffolding/open-questions.md §eigsolve-l1-operator-rough-in-candidate (cycle-008 OQ this dispatch addresses)
---

# CYCLE: Formalize eigsolve at L1 (rough-in)

## Summary

Author the L1 rough-in form for `eigsolve` — the eigenmode-solver analog of cycle-007 firm `ksp_solve`. Anchored at L0 by cycle-008 bundle-4 (`book/src/L0/eigensolver-wrapper.md`), which catalogs the `EigenvalueSolver` abstract base + three concrete branches (ARPACK RCI, SLEPc shell-matrix, Palace's direct-Newton `QuasiNewtonSolver`). The L1 form takes a construction-bound opaque eigensolver value `E : EigSolver[K, M, ...]` plus per-call control (initial-space / target / shift) and returns a structured `EigResult` carrying converged eigenpairs and per-call solve statistics — parallel to `ksp_solve`'s `Solver[A] → SolveResult` rotation.

**Pre-check verdict: rough-in.** No dedicated `test-eigensolver.cpp` in `palace/test/unit/`; only indirect coverage via `test-boundarymodeoperator.cpp` (three `ModeEigenSolver` test cases — a specialized wrapper for port-mode computation). `test-romoperator.cpp`'s "Eigen" mentions are about the C++ Eigen library (`#include <Eigen/Dense>`), not eigenvalue solves. The two L0-level orchestration patterns (RCI / shell-matrix vs direct-Newton) plus the three problem-type cases (linear / quadratic / nonlinear) span a larger variant landscape than `ksp_solve`'s CG/GMRES/FGMRES, and the test-coverage gap makes the load-bearing-vs-transparent classification of several axes (orchestration pattern, shift-invert mode, deflation policy, scaling) less confidently settled than `ksp_solve`'s were. Status is `rough-in (test-coverage-bounded)` — the structural signature is firm enough to anchor the L2 / L4 work referenced in the L0 chapter ("notes for higher layers" §1-§4), but algebraic-law confidence is reduced and `firm` promotion is deferred until either (a) test coverage expands or (b) a cycle-NN harvester invocation gains additional literature-anchored evidence.

## Pre-check (test coverage)

Per the dispatch instruction, mandatory pre-check before authoring:

1. `ls reference/palace/test/unit/` — 29 test files, none matching `*eigen*`, `*eps*`, `*arpack*`, or `*slepc*`. **No dedicated eigensolver test file.**
2. Grep `test-boundarymodeoperator.cpp` for eigen-related symbols → 8 matches (`ModeEigenSolver` instantiation, `EigenvalueSolver::WhichType::LARGEST_REAL`, `mode_solver.GetEigenvalue(i)`, three `TEST_CASE` macros). The tests construct a `ModeEigenSolver` (a thin wrapper around `EigenvalueSolver` for boundary port-mode computation) and assert on the returned `kn` values for PEC, impedance, and conductivity scenarios. **This is meaningful indirect coverage but narrow: only the linear `K x = λ M x` case, only `LARGEST_REAL` spectrum, only the SLEPc / ARPACK linear path (no quadratic / nonlinear; no shift-invert; no deflation behaviour).**
3. Grep `test-romoperator.cpp` for eigen-related → 20+ matches, all `Eigen::MatrixXd` / `toEigenMatrix` / `W_port_eigen` — the C++ Eigen library, not eigenvalue solves. Zero coverage of `EigenvalueSolver`.

**Decision**: `rough-in` per planner. The boundary-mode test coverage is too narrow to underwrite a firm L1 across the variant landscape (linear / quadratic / nonlinear × ARPACK / SLEPc / Newton × shift-invert / standard × deflation policies × eight `Type::` enum values for SLEPc). The structural signature is well-anchored by direct source reading of `eps.hpp` (22 virtuals), the three `Solve()` bodies (`arpack.cpp:513-560`, `slepc.cpp:687-709`, `nleps.cpp:351-805`), and the driver-side dispatch (`drivers/eigensolver.cpp:134-189`, `models/modeeigensolver.cpp:1030-1053`), but several algebraic-law claims that `ksp_solve` could underwrite by composition with `test-orthog.cpp` lack equivalent witnesses here.

## Proposed changes

```edit:book/src/L1/eigsolve.md
[NEW FILE — full content below]
```

```edit:book/src/L1/index.md
[Add eigsolve to the dep-map and vocabulary cohort — diff below]
```

```edit:book/src/SUMMARY.md
[Add `- [eigsolve](./L1/eigsolve.md)` chapter entry under L1 Part — diff below]
```

## Operator content (proposed `book/src/L1/eigsolve.md`)

```markdown
# eigsolve

Mutation-lifted eigenmode solve: `result = eigsolve(E, control)` where `E` is a construction-bound eigensolver value carrying its operator(s), inner linear solver, B-matrix, scaling, tolerances, and iteration cap; `control` is the per-call configuration (initial subspace, spectrum target, shift). The L1 sibling of [`ksp_solve`](./ksp_solve.md) — both realise the *constructed-operator absorption* motif against a stateful solve loop, but `eigsolve` ranges over a larger variant landscape (problem type × orchestration × spectrum target × deflation policy) and consequently carries weaker algebraic-law confidence pending test-coverage expansion.

## Context

The L0 source-side form is one of three concrete `EigenvalueSolver` subclasses' `Solve()` method:

- **ARPACK** — `ArpackEPSSolver::Solve()` / `ArpackPEPSolver::Solve()` (`palace/linalg/arpack.cpp:513-560` and analogous for PEP) running ARPACK's reverse-communication-interface (RCI) loop via `SolveInternal` (`palace/linalg/arpack.cpp:263-358`).
- **SLEPc** — `SlepcEPSSolverBase::Solve()` (`palace/linalg/slepc.cpp:687-709`) calling `EPSSolve(eps)` + `EPSGetConverged(eps, &num_conv)`, with the operator-application path going through PETSc shell-matrix callbacks (`A0`, `A1`).
- **Direct-Newton** — `QuasiNewtonSolver::Solve()` (`palace/linalg/nleps.cpp:351-805`) running a Palace-owned Newton outer loop with `ComplexKspSolver`-backed inner linear solves.

See [`L0/eigensolver-wrapper`](../L0/eigensolver-wrapper.md) for the complete C++ surface: the 22 virtuals on the `EigenvalueSolver` abstract base (`palace/linalg/eps.hpp:22-141`), the three `SetOperators` overloads (linear / quadratic / nonlinear, each `MFEM_ABORT` by default — `palace/linalg/eps.hpp:57-74`), the composition setters (`SetLinearSolver`, `SetDivFreeProjector`, `SetBMat` — `palace/linalg/eps.hpp:92-99`), the `WhichType` nine-way spectrum-target enum (`palace/linalg/eps.hpp:31-42`), the `ScaleType` two-way scaling enum (`palace/linalg/eps.hpp:25-29`), the `SetShiftInvert(σ, precond)` spectral-transformation entry, and the per-call result-extraction surface (`Solve() → int`, `GetEigenvalue(i)`, `GetEigenvector(i, x)`, `GetError(i, ErrorType)`). The L0 chapter also catalogs the three-way orchestration split (RCI / shell-matrix / direct-Newton) and notes that the L1 form would absorb the orchestration axis as transparent dispatch while preserving the problem-type axis.

At L0, `Solve()` returns the number of converged eigenpairs as an `int` and stores eigenpair data in solver-internal arrays (`eig`, `perm`, `V` for ARPACK; SLEPc-owned `EPS` object holding the same; `eigenvalues` / `eigenvectors` for `QuasiNewtonSolver`); per-pair extraction goes through three separate per-pair accessor virtuals (`GetEigenvalue`, `GetEigenvector(i, x)` writing into an out-parameter `ComplexVector`, `GetError(i, type)`). Workspace tensors (`mutable ComplexVector x1, y1, z1` on ARPACK; `x1, y1` on SLEPc and `NonLinearEigenvalueSolver`) back the per-`ApplyOp` callbacks invoked from the RCI loop / shell-matrix callbacks / Newton inner loop. The driver-side `Solve()` body at `palace/drivers/eigensolver.cpp:367` invokes `eigen->Solve()` once, prints the converged-count, and then optionally re-runs against a `QuasiNewtonSolver` refinement (`palace/drivers/eigensolver.cpp:405`). The eigenmode-pipeline call site at `palace/models/modeeigensolver.cpp:470, 477` invokes `eigen->SetOperators(*opB, *opA, ScaleType::NONE)` followed by `eigen->Solve()`. The wave-port eigenmode at `palace/models/waveportoperator.cpp:524` dispatches through the same surface.

The L1 form drops the destination-buffer mutation (`GetEigenvector(i, x)` writes into a caller-provided `x`), structures the converged-count and per-pair extraction into a single `EigResult` record carrying `eigenvalues : Tensor[K, complex]` and `eigenvectors : Tensor[K, N, complex]`, lifts the `Mpi::Print` convergence-status log lines (`palace/linalg/slepc.cpp:696-704` and analogous in `arpack.cpp`) into a structured `EigResult.converged` count, erases the orchestration-axis dispatch (RCI / shell-matrix / Newton are not part of the L1 contract — they are transparent dispatch tricks inside the opaque `EigSolver[…]` value), and erases the per-orchestration workspace tensors entirely (the L1>L0 lowering reintroduces them).

A cross-cutting prose treatment does **not** yet exist at `concepts/eigsolve` (unlike `ksp_solve`, which had a methodology-era concept page predating the firm operator chapter). The forward-target L4 monadic coordination layer the L1 form anchors will be analogous to [`concepts/solve-monad`](../concepts/solve-monad.md) but with sum-typed termination richer than `ksp_solve`'s soft-fail (the eigenvalue iteration can hit max-iter with `0 < converged < requested`, a partial-success case that has no analog in `ksp_solve`). The L1 entry here is the rough-in operator definition; a future concept page would carry the narrative.

## Signature

```text
eigsolve :: (E: EigSolver[problem], control: EigControl) -> EigResult[N, K_max]

EigControl = {
  initial_space  : Maybe (Tensor[N, complex]),  -- optional starting subspace seed
  -- All other per-call control is bound inside E at construction:
  --   spectrum target (WhichType), shift sigma, scaling type, num modes, tolerance, max-iter
}

EigResult[N, K_max] = {
  eigenvalues   : Tensor[K, complex],                -- the K converged eigenvalues
  eigenvectors  : Tensor[K, N, complex],             -- corresponding eigenvectors, unit-norm
                                                     --   (or B-orthonormal if E.B is set)
  converged     : Int,                               -- number of converged pairs (0 <= K <= K_max)
  requested     : Int,                               -- number requested (= K_max)
  error         : Tensor[K, real],                   -- per-pair error norm (per ErrorType bound in E)
  scaling_gamma : Real,                              -- Higham-2008 gamma (1.0 if ScaleType::NONE)
  scaling_delta : Real,                              -- Higham-2008 delta (1.0 if ScaleType::NONE)
  status        : EigStatus
}

EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed
```

Shape contract (bunsen-style, named axes):

- `E` — `EigSolver[problem]` — an opaque construction-bound eigensolver value. `problem` is a phantom carrying the problem-type tag (`Linear[K, M]` / `Quadratic[K, C, M]` / `Nonlinear[K, M, A2]`) and the operator axis `N` shared across all bound operators (`K : LinearOperator[N, N]`; `M : LinearOperator[N, N]`; `C : LinearOperator[N, N]` for quadratic; `A2 : Complex -> LinearOperator[N, N]` for nonlinear). `E` additionally binds the inner linear solver (`linear : Solver[A]` for the action of `M⁻¹` or `(K − σM)⁻¹` or `P(σ)⁻¹` per spectral-transformation mode), the optional divergence-free projector (`projector : Maybe DivFreeSolver[ComplexVector]`), the optional B-matrix for weighted inner products (`B : Maybe LinearOperator[N, N]`), the `ScaleType` (`NONE` / `NORM_2` per Higham 2008), the `WhichType` spectrum target (one of nine: `LARGEST_MAGNITUDE`, `SMALLEST_MAGNITUDE`, `LARGEST_REAL`, `SMALLEST_REAL`, `LARGEST_IMAGINARY`, `SMALLEST_IMAGINARY`, `TARGET_MAGNITUDE`, `TARGET_REAL`, `TARGET_IMAGINARY`), the shift `σ : Complex` (or `Nothing` for no spectral transformation), the requested mode count `K_max : Int`, the tolerance `tol : Real`, and the iteration cap `max_it : Int`. Read-only at the L1 call site. *All* per-method choices (ARPACK vs SLEPc vs `QuasiNewtonSolver`; for SLEPc, the nine-way `Type::` enum — `KRYLOVSCHUR`, `POWER`, `SUBSPACE`, `TOAR`, `STOAR`, `QARNOLDI`, `JD`, `SLP`, `NLEIGS`) are bound inside `E` at construction; the per-call surface is variant-free over the orchestration axis.
- `control` — `EigControl` — per-call configuration. The only field is the optional initial-subspace seed `initial_space` (the L0 `SetInitialSpace(const ComplexVector &v)` virtual at `palace/linalg/eps.hpp:122`); all other tuning lives inside `E`. `initial_space` is rough-in pending a decision on whether it is properly per-call control or another construction-bound axis (open question below).
- result — `EigResult[N, K_max]` — record containing the `K = result.converged` converged eigenvalues (`K ≤ K_max`), the corresponding eigenvectors as a stacked tensor (each unit-norm in the L2 sense, or B-orthonormal if `E.B` is set per `palace/linalg/eps.hpp:130-132` docstring), the per-pair error norm (per the `ErrorType` bound in `E` — `ABSOLUTE` / `RELATIVE` / `BACKWARD` from `palace/linalg/eps.hpp:44-49`), the Higham scaling factors (`γ`, `δ`) for the polynomial / nonlinear cases (both `1.0` when `ScaleType::NONE`), and a sum-typed `status` flag distinguishing the four termination modes (see Algebraic laws §3 for the source-anchored semantics of each).

The operator axis `N` is uniform across the bound operators (`K`, `M`, `C`, and any `A2(λ)` instance share the same domain/codomain) — eigenvalue problems are necessarily square. The element type of all bound operators is `ComplexOperator` at L0 (`palace/linalg/eps.hpp:57-74` shows the three `SetOperators` overloads all take `ComplexOperator` arguments); the L1 form preserves this — `eigsolve` is **complex-only**, unlike `ksp_solve` which has both real and complex element-type variants. This is a deliberate axis collapse, not an oversight: Palace's `EigenvalueSolver` interface does not provide a real-element overload; the only path that reaches `EigenvalueSolver::Solve()` is via the complex-element wrapper, even for real-symmetric problems (the real case is handled by promoting to complex with zero imaginary part).

`EigSolver[problem]` is an *opaque type* at L1: it has a problem-type phantom (linear / quadratic / nonlinear), an operator axis `N`, and is guaranteed to satisfy the convergence-test semantics below. Its internal orchestration (RCI / shell-matrix / Newton), its specific solver library (ARPACK / SLEPc / Palace's own), and its internal workspace representation are not part of the L1 signature.

## Semantics

`eigsolve(E, control)` returns an `EigResult` whose `eigenvalues` and `eigenvectors` fields approximate the solutions `(λᵢ, xᵢ)` of the eigenvalue problem bound inside `E`:

- **Linear**: `K · xᵢ = λᵢ · M · xᵢ` (`palace/linalg/eps.hpp:57-61`).
- **Quadratic**: `(K + λᵢ · C + λᵢ² · M) · xᵢ = 0` (`palace/linalg/eps.hpp:63-67`).
- **Nonlinear**: `(K + λᵢ · C + λᵢ² · M + A2(λᵢ)) · xᵢ = 0` (`palace/linalg/eps.hpp:69-74`), where `A2 : Complex → ComplexOperator` is the operator-valued nonlinearity bound inside `E`.

The approximation quality is governed by `E`'s convergence test: a pair `(λᵢ, xᵢ)` is reported as converged when its per-pair error (per `E`'s `ErrorType` bound) falls below `E.tol`. The iteration terminates and reports `status = Converged` when `K_max` pairs have converged. If the iteration cap `E.max_it` is reached first with `K < K_max` pairs converged, the iteration terminates with `status = PartialConverged` and the returned `eigenvalues` / `eigenvectors` contain exactly the `K` converged pairs (not the un-converged ones). If `K = 0` at max-iter, `status = MaxIterReached`. If the inner linear solver `E.linear` fails inside an `apply_linop` (`opInv->Mult(z1, y1)` at `palace/linalg/arpack.cpp:574` and analogous), `status = LinearSolveFailed`.

**Partial convergence is the L1 form's distinguishing semantic feature relative to `ksp_solve`**: the L0 `Solve() → int` return is a count that can be strictly less than the requested mode count without being an outright failure (`palace/drivers/eigensolver.cpp:369-374` formats `" Found {:d} converged eigenvalue{}{}\n"` — a singular base with a conditional `"s"` suffix appended when `num_conv > 1` — using the count as-returned, no error). The L1 form structures this as a sum-typed `status` field rather than a count-vs-request comparison the caller has to perform; the `Converged` vs `PartialConverged` distinction is load-bearing for downstream pipelines (the eigenmode-pipeline driver uses `num_conv` as a loop bound for postprocessing per `palace/drivers/eigensolver.cpp:367-374`, treating any positive count as "had results to report"; the wave-port operator at `palace/models/waveportoperator.cpp:524` uses similar logic).

The result is determined by `(E, control)` modulo four load-bearing non-determinism sources detailed below (reduction-tree non-associativity in the inner BLAS-1 ops, per-orchestration floating-point ordering, inner linear solver non-determinism propagated to the outer eigensolve, and ARPACK/SLEPc internal RNG for initial-space generation when `control.initial_space = Nothing`). Modulo those, the L1 form is referentially transparent: applying the same `E` to the same `control` returns the same `EigResult`.

The L0 source writes results into solver-internal arrays accessed via per-pair `GetEigenvalue(i)` / `GetEigenvector(i, x)` virtuals. The L1 form structures these into a single `EigResult` record. The L0 `Mpi::Print` convergence-summary log lines (`palace/linalg/slepc.cpp:696-704` printing solver-reason + total-linear-systems + total-linear-iterations; analogous in `arpack.cpp` and `nleps.cpp`) are not part of the L1 operator's semantics — the L1 `EigResult` carries `status`, `converged`, and (transitively, via the inner linear solver's own counters) the linear-system iteration count; any caller-side reporting is the caller's concern. This is the same pattern as the [`ksp_solve`](./ksp_solve.md) treatment of `Mpi::Warning` on non-convergence: the L1 form is single-rank-scope per CLAUDE.md, and the logger / MPI-print surfaces are L1>L0 lowering concerns.

The `BlockTimer bt1(Timer::EPS)` RAII wrap at `palace/drivers/eigensolver.cpp:365` is also dropped at L1 — it is a driver-side concern (the timer mutates a process-wide accumulator) that does not affect the algebraic relationship between `(E, control)` and `EigResult`.

The cumulative inner-linear-solver call counters (`opInv->NumTotalMult()` and `opInv->NumTotalMultIterations()` printed at `palace/linalg/slepc.cpp:702-703`) are not part of the L1 operator — they are driver-side accumulators computed from the inner solver's per-call statistics, analogous to the `ksp_mult` / `ksp_mult_it` treatment in [`ksp_solve`](./ksp_solve.md). The L1 form does not expose them in `EigResult`; reconstructing the L0 counts is `(E.linear.cumulative_calls, E.linear.cumulative_iters)` at the driver layer.

Reduction-tree non-associativity is **load-bearing** in the CLAUDE.md sense, inherited transitively through the inner-loop primitives at three nesting depths: every eigensolver iteration consumes `apply_linop` (matrix-vector products against `K`, `M`, `C`), `dot` (inner products for orthogonalisation and B-weighted inner products), `nrm2` (eigenvector normalisation), and `axpy` / `axpby` (basis updates); every spectral-transformation mode consumes inner `ksp_solve` calls (the `opInv->Mult` callbacks), which transitively consume the same BLAS-1 primitives a second time; and for the `QuasiNewtonSolver` branch, the inner `linear_eigensolver_` provides Newton initial guesses, adding a third nesting depth. The composite effect is recorded here, not erased.

Per-orchestration iteration-step ordering is a second load-bearing non-determinism axis. ARPACK's RCI loop runs Arnoldi on the host (the RCI driver pointers are host pointers — `palace/linalg/arpack.cpp:569-570` notes "The input pointers are always to host memory (ARPACK runs on host)"), so per-step host arithmetic ordering is fixed; SLEPc's shell-matrix orchestration runs on device when configured (per the GPU-backend lift inside SLEPc), with different floating-point ordering. The choice is collapsed into `E`'s opaque state at L1, but the choice affects the bit-level result. Algorithmic correctness is preserved across choices; bit-determinism is not.

A third load-bearing non-determinism axis is **inner-linear-solver non-determinism propagated to the outer eigensolve**. Each shift-invert spectral transformation requires an inner `ksp_solve(E.linear, …)` per RCI / shell-matrix callback (`palace/linalg/arpack.cpp:574, 580` for `opInv->Mult`; SLEPc analog inside the shell-matrix callbacks). The inner `ksp_solve` is itself non-deterministic in its `iterations` and bit-level `x` (per [`ksp_solve`](./ksp_solve.md) "Algebraic laws"), so the outer eigensolve inherits this — the per-RCI-step inner-solve iteration count and the per-step inner solution bit-pattern depend on the reduction tree, and these propagate to the outer Arnoldi basis vectors and hence to the converged eigenpairs.

A fourth non-determinism source, less load-bearing but observable: when `control.initial_space = Nothing`, ARPACK and SLEPc generate their own initial subspace by internal RNG. ARPACK's `info = 0` path at `palace/linalg/arpack.cpp:530-532` initialises a fresh residual vector; SLEPc's internal initialisation goes through PETSc's RNG. Different RNG seeds lead to different Krylov-subspace orbits and (typically) different per-call iteration counts; the converged eigenpairs are the same up to the convergence tolerance.

Per-orchestration variants (RCI / shell-matrix / direct-Newton) are **not** separate L1 operators (per the Variant axes section below). The L1 form collapses across all three; the L1>L0 lowering theme reintroduces the per-orchestration body, structured analogously to [`L1-L0/ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) (cycle-008).

## Algebraic laws

**Rough-in status caveat**: the laws below are stated at the level of confidence supported by direct source reading + literature anchors (Higham 2008, Lehoucq-Sorensen, Hernandez-Roman-Vidal). The narrow test coverage (`test-boundarymodeoperator.cpp` only) means several of these laws lack the kind of direct empirical witness that `ksp_solve`'s laws had via `test-orthog.cpp`. Critic / lifter / lowering-verifier dispatches on this entry should treat all laws as `unconfirmed` and either upgrade with additional evidence or downgrade to non-laws as warranted.

All laws are **modulo the convergence tolerance**: equalities are in the limit of `E.tol → 0`, `E.max_it → ∞`, treating each converged `(λᵢ, xᵢ)` as exactly satisfying its eigenvalue equation. Finite-tolerance behaviour is captured by explicit caveats noted with each law.

1. **Eigenvalue defining equation** (modulo tolerance — the defining property): for each converged pair `(λᵢ, xᵢ)` in `EigResult.eigenvalues` / `EigResult.eigenvectors`, the relevant eigenvalue equation holds approximately. For the linear case: `apply_linop(E.K, xᵢ) ≈ λᵢ · apply_linop(E.M, xᵢ)` with the residual `‖K xᵢ − λᵢ M xᵢ‖` bounded by `E.tol` (under the `ABSOLUTE` `ErrorType`). For the quadratic case: `(K + λᵢ C + λᵢ² M) xᵢ ≈ 0`. For the nonlinear case: `(K + λᵢ C + λᵢ² M + A2(λᵢ)) xᵢ ≈ 0`. This is the defining property — `eigsolve` is an approximation to the eigenvalue-equation root-finder. Witnessed by the `RescaleEigenvectors` calls at `palace/linalg/arpack.cpp:555` and `palace/linalg/slepc.cpp:707`, which compute the per-pair residual `‖(K − λM)x‖₂` and store it for later `GetError` retrieval.

2. **Eigenvector normalisation** (exact, not modulo tolerance): each `xᵢ` in `EigResult.eigenvectors` satisfies `‖xᵢ‖₂ = 1` when `E.B = Nothing`, and `xᵢᴴ B xᵢ = 1` when `E.B = Just B` (per `palace/linalg/eps.hpp:130-132` docstring). The L0 implementations enforce this in their `RescaleEigenvectors` step. This is a *post-condition* on `EigResult`, not a property of the iteration itself; the L1 form encodes it in the type-level docstring on `eigenvectors`.

3. **Termination semantics** — the four `EigStatus` values correspond directly to L0 termination cases:
   - `Converged` ↔ `Solve()` returns `K_max` (all requested pairs converged within tolerance and iteration budget). Witnessed: `palace/drivers/eigensolver.cpp:367-374` printing "Found {:d} converged" with no distinction between cases at L0 — the count vs request comparison is implicit. At L1 the comparison is structured into the status type.
   - `PartialConverged` ↔ `Solve()` returns `0 < K < K_max`. Same source witness; the L1 form makes the partial-success case explicit.
   - `MaxIterReached` ↔ `Solve()` returns `0`. Same source witness.
   - `LinearSolveFailed` ↔ an inner `opInv->Mult` callback returns a non-converged result. **Note**: at L0 this is not currently a distinct return-code case from `MaxIterReached` — the inner solve's non-convergence (an `Mpi::Warning` from `ksp_solve`'s `palace/linalg/ksp.cpp:301-307`) propagates as continued use of a poorly-converged inverse, which typically manifests as outer-eigensolve non-convergence. The L1 form's `LinearSolveFailed` is a *constructive distinction* that the L1>L0 lowering theme would need to plumb explicitly; in the current Palace source, the `LinearSolveFailed` case is **not directly observable**. This is a rough-in promotion candidate — either drop the case (collapsing to `MaxIterReached`) or carry it forward with an explicit "constructed by the L1 form" annotation. Routes to open question below.

4. **Eigenvalue invariance under shift** (modulo tolerance): when `E` is configured with shift-invert at `σ` (`SetShiftInvert(σ, precond)` at `palace/linalg/eps.hpp:119`), the returned `eigenvalues` are the **untransformed** eigenvalues `λᵢ` of the original problem, not the shifted-and-inverted `1/(λᵢ − σ)` that the inner Krylov method sees. The transformation is undone at the result-extraction surface (`GetEigenvalue` for SLEPc at `palace/linalg/slepc.cpp:711-716` performs the inverse transform). This is a load-bearing convention: the L1 caller sees the original-problem eigenvalues regardless of spectral-transformation mode.

5. **Scaling invariance** (modulo tolerance, for the polynomial / nonlinear cases): when `E.ScaleType = NORM_2`, the eigenvalues `λᵢ` returned in `EigResult.eigenvalues` are scaled per Higham 2008 (γ = √(‖K‖₂ / ‖M‖₂); δ = 2 / (‖K‖₂ + γ‖C‖₂ + γ²‖M‖₂)); the un-scaled eigenvalues of the original problem are recovered by multiplying by γ. **At L1, the returned `eigenvalues` are in the scaled coordinate system**; the `EigResult.scaling_gamma` / `EigResult.scaling_delta` fields are provided for downstream un-scaling. (This matches the L0 surface: `GetScalingGamma()` / `GetScalingDelta()` at `palace/linalg/eps.hpp:102-103` are part of the interface specifically because callers need to un-scale.) **Open question**: should L1 instead un-scale at the result-extraction boundary, so that `EigResult.eigenvalues` are always in the original coordinate system regardless of `E.ScaleType`? This is a coordinate-system convention; the current L0 surface leaves it to the caller. Rough-in.

6. **Operator-application linearity at the inner level** (modulo tolerance, by transitive inheritance): the per-step matrix-vector products inside the eigensolver iteration are `apply_linop` calls, and inherit `apply_linop`'s linearity in the vector argument. This is a non-law at the `eigsolve` level (eigenvalue problems are non-linear in `λ`) but is the algebraic substrate the L4 calculus's `iterate_while` primitive composes against (per `book/src/design/l4_calculus.md`).

Laws that explicitly **do not** hold:

- **Bit-determinism across reduction-tree variants** — inherited from `apply_linop`, `dot`, `nrm2`, `axpy`, and propagated through the inner `ksp_solve` (when shift-invert is configured). The outer eigensolve sees the cumulative bit-noise.
- **Bit-determinism across orchestration variants** (ARPACK / SLEPc / Newton) — different orchestrations produce different per-step floating-point ordering, hence different bit-level eigenpairs.
- **Bit-determinism across initial-space variants** — both ARPACK and SLEPc generate their own initial subspace via internal RNG when `control.initial_space = Nothing`; different RNG seeds (in particular, different runs against the same `E`) lead to different per-call iteration counts and bit-different eigenpairs. The mathematical eigenvalues are the same up to tolerance; the floating-point realisation differs.
- **Bit-determinism across spectrum-target variants** — for problems with eigenvalues clustered near multiple `WhichType` targets (e.g., a problem with `LARGEST_REAL` eigenvalues at +3.0, +2.9, +2.8), the orchestration may converge in different orders, leading to different *ordering* of `EigResult.eigenvalues`; the L0 sort in `modeeigensolver.cpp:484-492` is downstream re-ordering, not a property of `eigsolve` itself.
- **Determinism across `K_max` choices** — increasing the requested mode count from `K_max = K` to `K_max = K + 1` does **not** preserve the first `K` returned eigenpairs (in general the Arnoldi basis is re-built differently for a larger requested count, leading to different per-pair convergence trajectories).
- **Eigenvalue ordering** — `EigResult.eigenvalues` are returned in the orchestration's internal convergence order, **not** sorted by any specific criterion. Downstream re-ordering is performed in two distinct sites within the eigenmode pipeline: the ARPACK backend internally re-sorts by Real / Imag / Abs (per its configured `WhichType`) after the RCI loop completes (`palace/linalg/arpack.cpp:374-398`), producing a `perm` array consumed by `GetEigenvalue`/`GetEigenvector`; and `ModeEigenSolver::Solve` builds a second permutation sorted by proximity to the shift-target to harmonize backend ordering across ARPACK vs SLEPc (`palace/models/modeeigensolver.cpp:479-492`). The L1 `eigsolve` form does not perform either re-ordering — both are downstream caller-side concerns.
- **Composition with `apply_linop`** (`apply_linop(E.K, xᵢ) = λᵢ · apply_linop(E.M, xᵢ)` exactly): does not hold at finite tolerance — the equality is approximate within `E.tol`. The exact composition is recovered only in the formal limit. Algorithms that assume zero residual (e.g., post-eigensolve verification that re-checks the eigenvalue equation) must guard.
- **Strict positive-iteration termination** — for problems where `control.initial_space` is set to the exact eigenvector basis, the iteration may converge in zero or near-zero iterations; callers that assume `EigResult.iterations ≥ 1` are wrong. (Note: `iterations` is not currently a field of the proposed `EigResult` — it could be added if downstream consumers need it; routes to open question.)
- **Sum-type completeness of `EigStatus`** — as noted in §3 above, the `LinearSolveFailed` case is constructively introduced by the L1 form and is not directly observable in the current L0 surface. Until the L1>L0 lowering plumbs it explicitly, treating the four-way `EigStatus` as exhaustive over L0 termination cases is **not** a sound L0-grounded claim.

## Dependencies

At L1, `eigsolve` depends on three primitives plus the transitively-used BLAS-1 leaves:

- [`ksp_solve`](./ksp_solve.md) — the inner linear solver `E.linear` is a construction-bound Krylov solver, invoked per RCI / shell-matrix callback for spectral-transformation modes (`opInv->Mult` at `palace/linalg/arpack.cpp:574, 580` and analogous in SLEPc shell-matrix callbacks; the `QuasiNewtonSolver` branch calls into `ksp_solve` per Newton iteration via the `linear_eigensolver_` member at `palace/linalg/nleps.hpp:166`). Direct dependency. **This is the second L1 operator (after `ksp_solve` itself depending on `apply_linop`) whose primary dependency is itself a constructed-operator type**, making `eigsolve` the first L1 operator to compose two layers of constructed-operator absorption.
- [`apply_linop`](./apply_linop.md) — the system-operator action against the bound `K`, `M`, `C`, and `A2(λ)` operators is per-step matrix-vector products inside the eigensolver iteration (ARPACK's `opK->Mult(x1, z1)` at `palace/linalg/arpack.cpp:573`; SLEPc shell-matrix callbacks routing back to `ComplexOperator::Mult`). Direct dependency.
- [`dot`](./dot.md), [`nrm2`](./nrm2.md), [`axpy`](./axpy.md), [`axpby`](./axpby.md) — transitively present in every eigensolver iteration (orthogonalisation coefficients, residual norms, basis updates, eigenvector normalisation). Recorded as transitive rather than direct because they appear inside the per-orchestration body the L1 `eigsolve` opaquely wraps.

`eigsolve` is the **second constructed-operator gate at L1**, after `ksp_solve`. It composes against `ksp_solve` (rather than being a sibling) — the inner `E.linear` is an opaque `Solver[A]` whose internal Krylov method is itself a constructed-operator absorption. The two-layer constructed-operator composition is the L1 substrate for the eigenmode pipeline's L4 representation: an `eigsolve` is a stateful loop that, at each step, performs an `apply_linop` on a `Solver[A]`-wrapped operator (the shift-invert action). This is structurally the same nesting pattern as preconditioner application inside an iterative solver — composed-not-inherited.

The construction of `EigSolver[problem]` from a problem-type tag, system operators, an inner linear solver, a B-matrix, and convergence-control parameters is the [`constructed-operator-factory`](../concepts/constructed-operator-factory.md) concept; the absorption of per-orchestration variants into the opaque type is the [`variant-absorption`](../concepts/variant-absorption.md) concept; the L4 calculus's `iterate_while` primitive (per `book/src/design/l4_calculus.md`) is the natural composition target for the RCI / shell-matrix branches' outer iteration.

## Variant axes

`eigsolve` has four orthogonal variant axes at L1; three further axes are collapsed and recorded as deliberate absorption.

- **problem-type**: `linear` | `quadratic` | `nonlinear`. The L0 source splits this into the three `SetOperators` overloads (`palace/linalg/eps.hpp:57-74`), each defaulting to `MFEM_ABORT` so concrete subclasses opt in. ARPACK and SLEPc-EPS support linear; SLEPc-PEP and ARPACK-PEP support quadratic; SLEPc-NEP and `QuasiNewtonSolver` support nonlinear. At L1 the problem-type tag is part of `EigSolver[problem]`'s phantom type, distinguishing the three eigenvalue equations in §Semantics §1. The choice affects the dimensionality of `EigResult.eigenvalues` (linear: `K_max` complex; quadratic: `2 · K_max` complex; nonlinear: `K_max` complex with branch-cut semantics per the nonlinearity `A2`).
- **spectrum-target** (`WhichType` from `palace/linalg/eps.hpp:31-42`): nine-way enum — `LARGEST_MAGNITUDE`, `SMALLEST_MAGNITUDE`, `LARGEST_REAL`, `SMALLEST_REAL`, `LARGEST_IMAGINARY`, `SMALLEST_IMAGINARY`, `TARGET_MAGNITUDE`, `TARGET_REAL`, `TARGET_IMAGINARY`. Bound inside `E` at construction. ARPACK aborts on **2 of 9** values — `TARGET_REAL` and `TARGET_IMAGINARY` (`palace/linalg/arpack.cpp:300-304`: `MFEM_ABORT("ARPACK eigenvalue solver does not implement TARGET_REAL or TARGET_IMAGINARY for SetWhichEigenpairs!")`); SLEPc supports all nine. Per CLAUDE.md "Unimplemented Palace stub policy" (analogous to the `KrylovSolver::MINRES` / `KrylovSolver::BICGSTAB` `MFEM_ABORT` stubs at `palace/linalg/ksp.cpp:53-57`), the `(ARPACK, TARGET_REAL)` and `(ARPACK, TARGET_IMAGINARY)` orchestration × spectrum-target combinations are **unimplemented stubs**, not transparent dispatch. The L1 form preserves the nine-way spectrum-target axis (it is a load-bearing input to the convergence-test semantics) and treats the 2 ARPACK-unsupported pairs as a constructor-time validity constraint on the `EigSolver[problem]` opaque type — an `E` constructed with ARPACK + `TARGET_REAL` or ARPACK + `TARGET_IMAGINARY` is ill-formed; constructor-side rejection is part of the `EigSolver[problem]` construction contract. **Obstruction note for L1>L0**: the constructor-side rejection contract is not anchored in any current L0 surface (the L0 `EigenvalueSolver` constructor does not pre-check this; the failure surfaces at `Solve()` time via `MFEM_ABORT`). The L1>L0 lowering theme for `eigsolve` (a future cycle's `eigsolve-mutation-rotation`) will need to either (a) plumb the pre-check explicitly, or (b) document the constructor-time contract as an L1-introduced safety property analogous to the `KrylovSolver::MINRES` obstruction treatment in [`L1-L0/minres-iteration`](../L1-L0/minres-iteration.md).
- **spectral-transformation** (`SetShiftInvert(σ, precond)` from `palace/linalg/eps.hpp:119`): `none` | `shift_invert(σ, precond)`. Bound inside `E`. The choice determines whether the inner `E.linear` solver computes `M⁻¹` (no transformation) or `(K − σM)⁻¹` (shift-invert) per the comment at `palace/linalg/eps.hpp:88-91`.
- **scaling** (`ScaleType` from `palace/linalg/eps.hpp:25-29`): `NONE` | `NORM_2`. Bound inside `E`. Per Higham 2008 — `NORM_2` rescales operators by `γ = √(‖K‖₂ / ‖M‖₂)` and `δ = 2 / (‖K‖₂ + γ‖C‖₂ + γ²‖M‖₂)` for ill-conditioned polynomial / nonlinear cases. `EigResult.eigenvalues` are returned in the scaled coordinate system per Algebraic-law §5; `EigResult.scaling_gamma` / `EigResult.scaling_delta` provide the un-scaling factors.

Collapsed (absorbed) axes:

- **orchestration-pattern**: `arpack_rci` | `slepc_shell_matrix` | `direct_newton`. At L0 these are the three concrete subclass families (`ArpackEigenvalueSolver`, `SlepcEigenvalueSolver`, `NonLinearEigenvalueSolver` / `QuasiNewtonSolver`). At L1 these **collapse to a single `EigSolver[problem]` opaque type** — the L1 contract sees only the construction-bound solver and its convergence semantics; the per-orchestration body is an L0 (and L1>L0 lowering) concern. This parallels `ksp_solve`'s collapse of CG / GMRES / FGMRES.
- **slepc-internal-method** (`SlepcEigenvalueSolver::Type` from `palace/linalg/slepc.hpp:69-80`): nine-way — `KRYLOVSCHUR`, `POWER`, `SUBSPACE`, `TOAR`, `STOAR`, `QARNOLDI`, `JD`, `SLP`, `NLEIGS`. Bound at construction (via `SetType`); not visible at the L1 call site. Subsumed in the `orchestration-pattern` collapse above; named separately because it is a substantial-cardinality sub-axis that the L1 form deliberately erases.
- **slepc-problem-type** (`SlepcEigenvalueSolver::ProblemType` from `palace/linalg/slepc.hpp:57-67`): eight-way — `HERMITIAN`, `NON_HERMITIAN`, `GEN_HERMITIAN`, etc. Bound at construction via `SetProblemType`; not visible at L1. This is a *hint* to SLEPc about expected structure (driving choice of orthogonalisation and convergence-test details); the eigenvalue equation it represents is captured by the L1 `problem-type` axis.

Out of scope for this operator (deliberate exclusions):

- **Real-element eigenvalue problems** — the `EigenvalueSolver::SetOperators` overloads all take `ComplexOperator` arguments (`palace/linalg/eps.hpp:57-74`); there is no real-element `EigenvalueSolver` instantiation in Palace. The L1 form is correspondingly complex-only.
- **Per-pair iterative refinement** — Palace's `QuasiNewtonSolver::Solve()` (`palace/linalg/nleps.cpp:351-805`) invokes `SetInitialGuess()` (`palace/linalg/nleps.cpp:254-323`) at line 366 to consume the inner `linear_eigensolver_` results as initial guesses for Newton refinement; the L1 `eigsolve` form treats `QuasiNewtonSolver` as one orchestration variant whose internal initial-guess consumption is transparent (the outer L1 form sees only the final refined eigenpairs). The driver-side double-`Solve()` pattern at `palace/drivers/eigensolver.cpp:367, 405` (run linear eigensolve, then construct `QuasiNewtonSolver` on top, then re-`Solve()`) is a *higher-level composition* that the L1 `eigsolve` operator does not capture; it would be an L2 / L4 monadic-composition pattern.
- **MPI distribution** — `EigenvalueSolver` is MPI-aware (the SLEPc backend uses `PetscCommunicator` from `MPI_COMM`), but per CLAUDE.md "Scope" the L1 form is single-rank; the MPI surface lifts to the L1>L0 lowering.

## Status

`rough-in (test-coverage-bounded, cycle-009)` — the structural signature (input/output shape, the four-way `EigStatus`, the `EigResult` record fields) is well-anchored by direct source reading of `eps.hpp` and the three `Solve()` bodies. The `Converged` / `PartialConverged` / `MaxIterReached` cases are directly source-witnessed (`palace/drivers/eigensolver.cpp:367-374`); the `LinearSolveFailed` case is constructively introduced and **does not currently have an L0 anchor** (the inner-solver non-convergence is silent at the eigensolver level — see Algebraic laws §3 caveat).

Promotion to `firm` is gated on (a) addition of dedicated test coverage (e.g., a `test-eigensolver.cpp` exercising the linear / quadratic / nonlinear surfaces against known small problems), **or** (b) a future harvester invocation that adds literature-anchored evidence sufficient to underwrite the algebraic-law claims at `ksp_solve`-equivalent confidence (i.e., per-law literature anchors for Higham scaling, Lehoucq-Sorensen ARPACK convergence, Hernandez-Roman-Vidal SLEPc convergence, Jarlebring-Koskela-Mele quasi-Newton). Either path is plausible for a later cycle; rough-in is the appropriate status today.

The variant-axis collapses (orchestration-pattern, SLEPc-Type, SLEPc-ProblemType) are not at issue — they are direct analogs of `ksp_solve`'s krylov-method collapse and are well-grounded by the L0 anchor.

## L1 vs L0 distinction

- **L0**: `EigenvalueSolver` abstract base (`palace/linalg/eps.hpp:22-141`) with 22 virtuals. Three concrete subclass families: ARPACK (RCI loop, two subclasses for linear / quadratic), SLEPc (shell-matrix callbacks, three subclasses for linear / quadratic / nonlinear, each with 8-way `ProblemType` and 9-way `Type` sub-axes), `NonLinearEigenvalueSolver` / `QuasiNewtonSolver` (direct Newton, with composed inner `linear_eigensolver_`). `Solve()` returns `int` (converged count); per-pair extraction via `GetEigenvalue(i)`, `GetEigenvector(i, x)` (writes into out-parameter), `GetError(i, type)`. Workspace tensors (`mutable ComplexVector x1, y1, z1` for ARPACK; `x1, y1` for SLEPc / nonlinear) back per-`ApplyOp` callbacks. Three `MFEM_ABORT`-default `SetOperators` overloads. `Mpi::Print` convergence-summary log lines. `BlockTimer bt1(Timer::EPS)` RAII wrap at the driver level. Driver-side cumulative inner-solver counters (`opInv->NumTotalMult`, `opInv->NumTotalMultIterations`).
- **L1**: pure functional eigensolve. `result = eigsolve(E, control)`. No destination buffers (eigenpairs structured into `EigResult`). Convergence status structured into `EigResult.status` (sum-typed: `Converged | PartialConverged | MaxIterReached | LinearSolveFailed`) rather than counter-return + log lines. Orchestration-axis collapsed (RCI / shell-matrix / Newton not visible at L1). Problem-type axis preserved (linear / quadratic / nonlinear in the `EigSolver[problem]` phantom). Spectrum-target, spectral-transformation, scaling axes preserved. Higham scaling factors exposed in `EigResult` for downstream un-scaling. Algebraic laws: eigenvalue defining equation, eigenvector normalisation, termination semantics, eigenvalue invariance under shift, scaling invariance — all modulo convergence tolerance + the rough-in caveat on `LinearSolveFailed` constructibility. Non-laws: bit-determinism across reduction-tree / orchestration / initial-space variants; eigenvalue ordering; determinism across `K_max`; exact eigenvalue-equation composition; sum-type completeness of `EigStatus` (rough-in).

## Evidence

- `palace/linalg/eps.hpp:22-141` — `EigenvalueSolver` abstract base class definition (full surface).
- `palace/linalg/eps.hpp:25-29` — `ScaleType` enum (`NONE`, `NORM_2`).
- `palace/linalg/eps.hpp:31-42` — `WhichType` enum (nine-way spectrum-target).
- `palace/linalg/eps.hpp:44-49` — `ErrorType` enum (`ABSOLUTE`, `RELATIVE`, `BACKWARD`).
- `palace/linalg/eps.hpp:57-74` — three `SetOperators` overloads (linear / quadratic / nonlinear), each defaulting to `MFEM_ABORT`.
- `palace/linalg/eps.hpp:92-99` — `SetLinearSolver`, `SetDivFreeProjector`, `SetBMat` pure-virtuals (composition with inner linear solver / projector / inner-product matrix).
- `palace/linalg/eps.hpp:102-103` — `GetScalingGamma` / `GetScalingDelta` Higham-2008 scaling accessors.
- `palace/linalg/eps.hpp:116, 119` — `SetWhichEigenpairs` and `SetShiftInvert` spectral-transformation setters.
- `palace/linalg/eps.hpp:122` — `SetInitialSpace(const ComplexVector &v)` — the per-call control entry the L1 `EigControl.initial_space` field maps to.
- `palace/linalg/eps.hpp:124-140` — `Solve()`, `GetEigenvalue`, `GetEigenvector`, `GetError`, `RescaleEigenvectors` result-extraction surface.
- `palace/linalg/eps.hpp:130-132` — eigenvector normalisation docstring (the `‖x‖₂ = 1` or `xᴴ B x = 1` post-condition).
- `palace/linalg/arpack.cpp:263-358` — `SolveInternal` RCI loop body; `naupd` driver call at line 318; `ApplyOp` at line 325; `ApplyOpB` at line 329.
- `palace/linalg/arpack.cpp:300-304` — `MFEM_ABORT` for `TARGET_REAL` / `TARGET_IMAGINARY` (ARPACK does not implement these).
- `palace/linalg/arpack.cpp:513-560` — `ArpackEPSSolver::Solve()` body: defaults, RCI invocation via `SolveInternal` at line 552, then `RescaleEigenvectors` at line 555.
- `palace/linalg/arpack.cpp:569-580` — `ArpackEPSSolver::ApplyOp`: host-pointer convention, `opK->Mult` + `opInv->Mult` for the non-shift-invert case (line 573-574), `opM->Mult` + `opInv->Mult` for shift-invert (line 579-580). Direct evidence of the inner-`ksp_solve` dependency.
- `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve()` body: `EPSSolve(eps)` (line 694), `EPSGetConverged` (line 695), `RescaleEigenvectors(num_conv)` (line 707).
- `palace/linalg/slepc.cpp:696-704` — `Mpi::Print` convergence-summary log lines (`EPSConvergedReasonView` + total-linear-systems + total-linear-iterations) — the side-effect surface the L1 form drops.
- `palace/linalg/slepc.cpp:711-716` — `SlepcEPSSolverBase::GetEigenvalue(i)`: returns `l * gamma` — the un-scaling at the result-extraction boundary (the basis for Algebraic-law §5's rough-in question about which coordinate system L1 should expose).
- `palace/linalg/nleps.cpp:351-805` — `QuasiNewtonSolver::Solve()` body: Newton outer loop, deflation scheme (Effenberger 2013), inner linear-eigensolver initial guess (`SetInitialGuess` at line 366), per-Newton-step inner `ksp_solve` calls.
- `palace/models/modeeigensolver.cpp:470, 477` — `eigen->SetOperators(*opB, *opA, EigenvalueSolver::ScaleType::NONE)` + `eigen->Solve()` call sites inside `ModeEigenSolver::Solve()`.
- `palace/models/modeeigensolver.cpp:484-492` — driver-side eigenvalue re-sort by shift-target distance (proof that L1 `EigResult.eigenvalues` is not guaranteed sorted — the sort is downstream re-ordering).
- `palace/models/modeeigensolver.cpp:1030-1053` — eigensolver-backend dispatch site (the construction of the opaque `EigSolver[problem]` value; ARPACK branch lines 1030-1040, SLEPc branch lines 1041-1053).
- `palace/models/waveportoperator.cpp:524` — wave-port eigenmode dispatch through the same surface.
- `palace/drivers/eigensolver.cpp:86` — `std::unique_ptr<EigenvalueSolver> eigen` declaration (the driver-side eigensolver field).
- `palace/drivers/eigensolver.cpp:134-189` — `SetType` / `SetProblemType` configuration of the SLEPc subtype; problem-type-conditional `SetOperators` dispatch.
- `palace/drivers/eigensolver.cpp:172-189` — `ScaleType` setting + problem-type-conditional `SetOperators` (linear / quadratic) calls.
- `palace/drivers/eigensolver.cpp:291-315` — `WhichType` setting per the configured target-spectrum mode (`SMALLEST_IMAGINARY`, `TARGET_MAGNITUDE`, `TARGET_IMAGINARY`, `LARGEST_REAL`, `TARGET_REAL`).
- `palace/drivers/eigensolver.cpp:365-374` — `BlockTimer bt1(Timer::EPS)` + `eigen->Solve()` + `Mpi::Print("\n Found {:d} converged eigenvalue{}{}…")`. The driver-side outer composition the L1 form structures.
- `palace/drivers/eigensolver.cpp:377-407` — optional `QuasiNewtonSolver` refinement step: construct `qn` consuming the prior `eigen` as initial guess (line 380), reconfigure operators / preconditioner / shift-invert, then `qn->Solve()` (line 405). Direct evidence of the driver-side double-solve composition (out of scope for L1 `eigsolve`; would be an L2 / L4 monadic composition).
- `book/src/L0/eigensolver-wrapper.md` — cycle-008 bundle-4 L0 anchor chapter for `EigenvalueSolver` and its three wrappers (the direct source-of-truth for what L1 wraps).
- `book/src/L1/ksp_solve.md` — sister L1 chapter (cycle-007); the precedent for the constructed-operator absorption pattern and the L1 chapter shape.
- `book/src/L1/index.md` — L1 Part overview + dep-map (where this entry is to be added).
- `book/src/L1/apply_linop.md`, `book/src/L1/dot.md`, `book/src/L1/nrm2.md`, `book/src/L1/axpy.md`, `book/src/L1/axpby.md` — BLAS-1 leaves transitively used inside the eigensolver iteration.
- `book/src/concepts/constructed-operators.md`, `book/src/concepts/variant-absorption.md`, `book/src/concepts/constructed-operator-factory.md` — methodology concepts the L1 entry's opaque-type treatment rests on.
- `book/src/concepts/solver-as-operator.md`, `book/src/concepts/solve-monad.md` — sister concepts inherited from `ksp_solve`; a future `concepts/eigsolve.md` would extend the pattern to the eigenvalue case with sum-typed termination.
- `book/src/design/l4_calculus.md` — L4 strawman; `iterate_while` is the natural composition target for the RCI / shell-matrix orchestrations.
- `reference/palace/test/unit/test-boundarymodeoperator.cpp:line-numbers-vary` — three `TEST_CASE` macros (`ModeEigenSolver PEC`, `ModeEigenSolver Impedance shifts kn`, `ModeEigenSolver Conductivity adds loss`) exercising the linear-EPS path with `WhichType::LARGEST_REAL`. The narrow coverage motivating the rough-in classification.
- `scaffolding/open-questions.md:1342-1351` — cycle-008 OQ `eigsolve-l1-operator-rough-in-candidate` (the dispatch target).
```

## Diff for `book/src/L1/index.md`

Two changes:

**(1)** Add `eigsolve` to a new "Rough-in (test-coverage-bounded)" subsection parallel to the existing "Rough-in (obstruction)" subsection — keeping the Firm cohort and its `Firm (8)` count unchanged. Insertion point is immediately after the Firm bullet list ends (current `index.md` line 38, after the `ksp_solve` bullet) and before the existing "Rough-in (obstruction)" heading (current line 40):

```diff
 - [`ksp_solve`](./ksp_solve.md) — pure preconditioned Krylov solve `(x, status) = ksp_solve(K, b)`; constructed-operator gate. The first L1 operator whose primary argument is itself a structured value (`Solver[A]`) rather than a raw tensor or scalar.

+**Rough-in (test-coverage-bounded)** — operators whose structural signature is well-anchored at L0 but whose algebraic-law confidence is reduced pending dedicated test coverage or expanded literature anchoring:
+
+- [`eigsolve`](./eigsolve.md) — pure eigenmode solve `result = eigsolve(E, control)`; the second constructed-operator gate at L1, composing against `ksp_solve` for spectral-transformation modes. Rough-in status motivated by absence of a dedicated `test-eigensolver.cpp` (only indirect coverage via `test-boundarymodeoperator.cpp`'s three `ModeEigenSolver` cases, exercising the linear path with `LARGEST_REAL` only). Promotion to firm gated on either expanded test coverage or additional literature anchoring (Higham 2008, Lehoucq-Sorensen, Hernandez-Roman-Vidal, Jarlebring-Koskela-Mele).
+
 **Rough-in (obstruction)** — speculative L1 operators emitted by `L1>L0` obstruction themes (no Palace L0 anchor; harvester promotion gated on appearance of an anchor):
```

**(2)** Add the `eigsolve` row to the dep-map table (lines 51-66), inserted after the `ksp_solve` row and before the `lanczos_step` rough-in row:

```diff
 | [`ksp_solve`](./ksp_solve.md) | `(K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) → SolveResult[N]` | `apply_linop` (direct); `dot`, `nrm2`, `axpy` (transitive via per-method body) | `firm` (L1>L0: [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md), cycle-008) |
+| [`eigsolve`](./eigsolve.md) | `(E: EigSolver[problem], control: EigControl) → EigResult[N, K_max]` | `ksp_solve` (direct, inner linear solver); `apply_linop` (direct, per-step matrix-vector); `dot`, `nrm2`, `axpy`, `axpby` (transitive via per-orchestration body) | `rough-in (test-coverage-bounded, harvested-by: harvester:2026-05-27T191929Z-harvester-eigsolve-L1)` |
 | [`lanczos_step`](../L1-L0/minres-iteration.md) | `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` | `apply_linop`, `dot`, `axpy`, `nrm2` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0)` |
```

**(3)** Append a working-note bullet under the "Working Notes" section (lines 68-76):

```diff
 - **Cycle-008**: the L1>L0 mutation-rotation theme for `ksp_solve` landed at [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) — the first L1>L0 theme whose LHS takes a structured opaque primary argument (`Solver[A]`). The theme decomposes into the firm sister themes per-step ([`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md), [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md), [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md)) plus four outer-composition absorption rules (timer erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding). The "Constructed-operator absorption" motif registered cycle-007 with the `ksp_solve` L1 firming now has the closing-the-loop L1>L0 anchor.
+- **Cycle-009**: the `eigsolve` rough-in lands as the **second constructed-operator gate at L1**, composing against `ksp_solve` (the inner linear solver is itself a constructed-operator absorption). Per the cycle-008 OQ `eigsolve-l1-operator-rough-in-candidate` and the pre-check verdict (no dedicated `test-eigensolver.cpp`; narrow indirect coverage via `test-boundarymodeoperator.cpp` only), status is rough-in pending either expanded test coverage or additional literature anchoring. The rough-in introduces the **partial-convergence** semantic (`PartialConverged` status) as a distinguishing feature relative to `ksp_solve`'s soft-fail — the eigenvalue iteration can converge `0 < K < K_max` pairs without being an outright failure, a case `ksp_solve` has no analog for.
```

## Diff for `book/src/SUMMARY.md`

Add a chapter entry under the L1 Part. Insertion point is line 40 (immediately after the `ksp_solve` entry):

```diff
 - [ksp_solve](./L1/ksp_solve.md)
+- [eigsolve](./L1/eigsolve.md)

 # L1>L0 — Mutation rotation
```

## Supporting evidence

**Pre-check artifacts** (raw command output, for verification by critic):

- `ls /home/crutcher/git/palace_whiteroom/reference/palace/test/unit/*eigen*` → exit 2 (no match).
- `ls /home/crutcher/git/palace_whiteroom/reference/palace/test/unit/*eps*` → exit 2 (no match).
- `ls /home/crutcher/git/palace_whiteroom/reference/palace/test/unit/*arpack*` → exit 2 (no match).
- `ls /home/crutcher/git/palace_whiteroom/reference/palace/test/unit/*slepc*` → exit 2 (no match).
- `grep -i "eigen\|eps\|arpack\|slepc\|krylovschur\|lanczos\|arnoldi" reference/palace/test/unit/test-boundarymodeoperator.cpp` → 8 matches: `ModeEigenSolver` instantiation (with `EigenvalueSolver::WhichType::LARGEST_REAL`), 3 `TEST_CASE` macros (`ModeEigenSolver PEC`, `ModeEigenSolver Impedance shifts kn`, `ModeEigenSolver Conductivity adds loss`), plus `mode_solver.GetEigenvalue(i)` accessor calls.
- `grep -i ... reference/palace/test/unit/test-romoperator.cpp` → 20+ matches but **all are about the C++ Eigen library** (`#include <Eigen/Dense>`, `Eigen::MatrixXd`, `toEigenMatrix`, `W_port_eigen`, `Eigen::IOFormat`), zero about eigenvalue solves.

**Source-citation spot-checks** (verifying ranges in the proposed L1 entry):

- `palace/linalg/eps.hpp:22-141`: verified by direct read — the abstract base class spans lines 22 (`class EigenvalueSolver`) to 141 (closing `};`).
- `palace/linalg/eps.hpp:25-29`: verified — `enum class ScaleType { NONE, NORM_2 };`.
- `palace/linalg/eps.hpp:31-42`: verified — nine `WhichType` cases.
- `palace/linalg/eps.hpp:44-49`: verified — three `ErrorType` cases.
- `palace/linalg/eps.hpp:57-74`: verified — three `SetOperators` overloads, each with `MFEM_ABORT("SetOperators not defined!");` default body.
- `palace/linalg/eps.hpp:92-99`: verified — `SetLinearSolver`, `SetDivFreeProjector`, `SetBMat` pure virtuals.
- `palace/linalg/arpack.cpp:513-560`: verified — `ArpackEPSSolver::Solve()` body with `SolveInternal` call at line 552, `RescaleEigenvectors` at line 555.
- `palace/linalg/arpack.cpp:573-574`: verified — `opK->Mult(x1, z1); opInv->Mult(z1, y1);` (the non-shift-invert ApplyOp path).
- `palace/linalg/slepc.cpp:687-709`: verified — `SlepcEPSSolverBase::Solve()` with `EPSSolve(eps)` at line 694, `EPSGetConverged` at line 695.
- `palace/linalg/slepc.cpp:711-716`: verified — `GetEigenvalue` returning `l * gamma`.
- `palace/linalg/nleps.cpp:351`: verified — `int QuasiNewtonSolver::Solve()` signature start.
- `palace/models/modeeigensolver.cpp:470, 477`: verified — `eigen->SetOperators(...)` at line 470, `eigen->Solve()` at line 477.
- `palace/drivers/eigensolver.cpp:367`: verified — `int num_conv = eigen->Solve();`.
- `palace/drivers/eigensolver.cpp:405`: verified — second `eigen->Solve()` call (the `QuasiNewtonSolver` refinement step).

All cited line ranges are concrete (no ellipsis ranges), per the cycle-008 bundle-4 repair pattern.

## Open questions / caveats

1. **`EigStatus::LinearSolveFailed` is constructively introduced and has no direct L0 anchor.** At L0, an inner-solver non-convergence is silent at the eigensolver level (the inner `ksp_solve` emits `Mpi::Warning` per `palace/linalg/ksp.cpp:301-307` but the eigensolver continues with the poorly-converged inverse). The L1 `EigStatus::LinearSolveFailed` case is constructed by the L1 form to plumb this case explicitly. Critic should consider whether to (a) drop the case (collapsing to `MaxIterReached`), (b) accept the constructive introduction with an explicit "constructed by the L1 form" annotation, or (c) require the L1>L0 lowering theme to plumb the case via a refactor of the inner-solver coupling. Recommendation from this dispatch: keep the case but mark it `unconfirmed` until the L1>L0 lowering theme is harvested. Slug: `eigsolve-linear-solve-failed-status-anchor`.

2. **Coordinate-system convention for `EigResult.eigenvalues` under `ScaleType::NORM_2`.** Algebraic-law §5 above flags two coherent conventions: (a) return scaled eigenvalues (matches L0 `EPSGetEigenvalue` raw return), expose `scaling_gamma` / `scaling_delta` for downstream un-scaling; or (b) un-scale at the L1 boundary, return original-coordinate eigenvalues, drop the gamma/delta fields. The L0 `GetEigenvalue` virtual already un-scales for SLEPc (`palace/linalg/slepc.cpp:715` returns `l * gamma`); inconsistent across orchestrations. The rough-in entry adopts convention (a) but flags this for harvester / lifter review. Slug: `eigsolve-scaling-coordinate-convention`.

3. **`control.initial_space` placement — per-call or construction-bound?** The L0 `SetInitialSpace` virtual (`palace/linalg/eps.hpp:122`) is on the eigensolver value (so construction-bound), but the call pattern at `palace/models/modeeigensolver.cpp:472-475` shows the driver setting it per `Solve()` invocation:
   ```cpp
   if (initial_space) {
     eigen->SetInitialSpace(*initial_space);
   }
   ```
   The rough-in entry puts it in `EigControl` (per-call) on the grounds that the call-site pattern is per-call; this could equally be construction-bound (the `initial_space` is a construction parameter that the driver re-binds at solve time). Routes to lifter / lowering-verifier review. Slug: `eigsolve-initial-space-axis-placement`.

4. **`EigResult.iterations` field placement.** The proposed `EigResult` does not currently carry an `iterations` field (unlike `ksp_solve`'s `SolveResult.iterations`). The L0 `EigenvalueSolver` interface does not expose a per-call iteration count — only the converged eigenpair count. Adding it to L1 would be constructive (similar to `EigStatus::LinearSolveFailed`); the question is whether downstream consumers (e.g., the L2 `eigenmode-pipeline` operator, the L4 monadic composition) need it. Leave out for now; harvester promotion to firm should re-evaluate. Slug: `eigsolve-iteration-count-result-field`.

5. **L2 / L4 forward-targets.** The L0 chapter `eigensolver-wrapper.md` "Notes for higher layers" §1-§4 lists four downstream tasks: (1) the L1 `eigsolve` operator (closed by this dispatch as rough-in); (2) the L2 `eigenmode-pipeline` operator (open); (3) the L4 `eigensolve-monad` composition (open); (4) the literature-anchored algebraic laws (open — partially addressed by this dispatch's law statements, but the literature anchoring is at the strawman level only). Tasks 2-4 are out-of-scope for this dispatch but should be tracked for cycle-010+.

6. **Partial-convergence handling at the L2 / driver level.** The L1 form's `EigResult.status = PartialConverged` case is structurally distinct from `Converged`, but Palace's drivers do not currently treat them differently (per `palace/drivers/eigensolver.cpp:367-374`, the driver prints the count and proceeds with postprocessing regardless). The L1 distinction is mathematically meaningful but may not surface as a driver-level branch. This is a methodology question for the L2 `eigenmode-pipeline` harvester: does the L2 form make the `PartialConverged` vs `Converged` distinction load-bearing, or does it absorb the distinction back into a single `converged_count` accessor matching the L0 surface? Cross-reference to OQ `eigsolve-linear-solve-failed-status-anchor` (the two are related: both are about whether L1's structurally-distinct termination cases should propagate or collapse downstream).

7. **L1 intro refresh needed.** The L1 Part overview's "Constructed-operator absorption" semantic motif §4 (line 22-23) references `ksp_solve` as the singular example. With `eigsolve` landing as the second constructed-operator gate, the motif description should generalize. Recommend layer-intro-author dispatch to refresh L1 intro after this entry integrates. Per harvester role spec, this is noted here rather than authored — out of scope for this dispatch.

8. **L0 chapter update.** The L0 `eigensolver-wrapper.md` "Referenced from" section (lines 90-94) currently notes the L1 / L4 entries as forward-targets. After this dispatch integrates, the L1 forward-target line should update to point at the firm rough-in. Recommend integrator handles this as part of the per-report apply, or routes to a small follow-up dispatch. Per harvester role spec, not modifying the L0 chapter here.

This dispatch **partially closes** OQ `eigsolve-l1-operator-rough-in-candidate` (the L1 rough-in operator is now authored). Full closure requires firm promotion, which is gated on the test-coverage / literature-anchoring path described in §Status.
