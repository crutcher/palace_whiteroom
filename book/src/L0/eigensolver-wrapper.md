# Class — `EigenvalueSolver` and its wrappers

A reference note for the eigenmode pipeline's L1 / L4 entries. `EigenvalueSolver` (`palace/linalg/eps.hpp:22-141`) is a pure-abstract base class that fronts three concrete implementation wrappers — **ARPACK** (`palace/linalg/arpack.{hpp,cpp}`), **SLEPc** (`palace/linalg/slepc.{hpp,cpp}`), and **Palace's own quasi-Newton nonlinear** solver (`palace/linalg/nleps.{hpp,cpp}`) — exposing a common interface for generalized linear, quadratic-polynomial, and nonlinear eigenvalue problems.

The wrappers are the eigensolver-side counterpart of the [`kspsolver-base-class`](./kspsolver-base-class.md) composition on the Krylov-solver side: both take a configured preconditioner / linear solver via `Set*` setters and produce a stateful `Solve()` entry point that returns convergence count. The hand-off point between the two is the `EigenvalueSolver::SetLinearSolver(ComplexKspSolver &ksp)` pure-virtual at `palace/linalg/eps.hpp:92` — the eigensolver wrapper holds a non-owning reference to a `ComplexKspSolver` and calls into it to compute the action of `M⁻¹`, `(K − σM)⁻¹`, or `P(σ)⁻¹` per the spectral-transformation mode.

## The abstract surface

`EigenvalueSolver` declares 22 virtual methods covering five primary concerns (plus auxiliary per-solve control setters — `SetNumModes`, `SetTol`, `SetMaxIter`, `SetInitialSpace` at `palace/linalg/eps.hpp:106, 109, 112, 122` — that do not belong to any of the five but are uniform across concrete subclasses):

- **Operator setup**: three overloads of `SetOperators` at `palace/linalg/eps.hpp:57-74` for generalized linear (`K x = λ M x`), quadratic polynomial (`(K + λ C + λ² M) x = 0`), and nonlinear (`K x = λ M x + A2(λ) x`) problems. Each defaults to `MFEM_ABORT` so concrete subclasses opt in to the cases they support — ARPACK and SLEPc-EPS support generalized linear; SLEPc-PEP and ARPACK-PEP support quadratic; SLEPc-NEP and Palace's `QuasiNewtonSolver` support nonlinear.
- **Solver coupling**: `SetLinearSolver`, `SetDivFreeProjector`, `SetBMat` at `palace/linalg/eps.hpp:92-99` — non-owning references to the configured linear solver, divergence-free projector, and weighted-inner-product matrix.
- **Spectral transformation and target**: `SetWhichEigenpairs(WhichType)` at `palace/linalg/eps.hpp:116`, `SetShiftInvert(σ, precond)` at `palace/linalg/eps.hpp:119`. `WhichType` (`palace/linalg/eps.hpp:31-42`) is a nine-way enum: `LARGEST_MAGNITUDE`, `SMALLEST_MAGNITUDE`, `LARGEST_REAL`, `SMALLEST_REAL`, `LARGEST_IMAGINARY`, `SMALLEST_IMAGINARY`, `TARGET_MAGNITUDE`, `TARGET_REAL`, `TARGET_IMAGINARY`. ARPACK aborts on the `TARGET_REAL` / `TARGET_IMAGINARY` cases (`palace/linalg/arpack.cpp:300-304`); SLEPc supports them all.
- **Solve and result extraction**: `Solve()` returns the number of converged eigenpairs; `GetEigenvalue(i)`, `GetEigenvector(i, x)`, `GetError(i, ErrorType)` extract per-pair results. `ErrorType` (`palace/linalg/eps.hpp:44-49`) is three-way: `ABSOLUTE`, `RELATIVE`, `BACKWARD`.
- **Scaling**: `GetScalingGamma()`, `GetScalingDelta()` at `palace/linalg/eps.hpp:102-103`, plus the `ScaleType` enum (`palace/linalg/eps.hpp:25-29`: `NONE` or `NORM_2`). These implement Higham-et-al-2008 IJNME scaling for the polynomial eigenvalue problem; the constants are stored on each concrete subclass.

## The three concrete branches

**`palace::arpack::ArpackEigenvalueSolver`** (`palace/linalg/arpack.hpp:29-170`) wraps ARPACK / PARPACK with a reverse-communication-interface (RCI) loop. The RCI body is `SolveInternal` at `palace/linalg/arpack.cpp:263-358`: it calls ARPACK's `naupd` driver (line 318), and when `ido ∈ {-1, 1}` invokes `ApplyOp` (line 325) — a pure-virtual that the concrete `ArpackEPSSolver` / `ArpackPEPSolver` subclasses implement using the configured `opInv` (the `ComplexKspSolver`) and the operators `opK` / `opM` / `opC`. Two concrete subclasses: `ArpackEPSSolver` (generalized linear, `palace/linalg/arpack.hpp:173-201`) and `ArpackPEPSolver` (quadratic polynomial, `palace/linalg/arpack.hpp:204-236`). Both are conditionally compiled under `PALACE_WITH_ARPACK` (`palace/linalg/arpack.hpp:7`).

**`palace::slepc::SlepcEigenvalueSolver`** (`palace/linalg/slepc.hpp:54-198`) wraps SLEPc, which itself wraps PETSc. Adds SLEPc-specific enums: `ProblemType` (8-way: `HERMITIAN`, `NON_HERMITIAN`, `GEN_HERMITIAN`, …) and `Type` (9-way solver: `KRYLOVSCHUR`, `POWER`, `SUBSPACE`, `TOAR`, `STOAR`, `QARNOLDI`, `JD`, `SLP`, `NLEIGS`). The implementation routes through SLEPc shell matrices (`A0`, `A1`, …) that delegate `Mat`-application back to Palace's `ComplexOperator` via PETSc shell-matrix callbacks. Three problem-type-specific subclass hierarchies:

- EPS (linear): `SlepcEPSSolverBase` + `SlepcEPSSolver` (`palace/linalg/slepc.hpp:201-249` and the corresponding `slepc.cpp:687-757`). `Solve()` at `palace/linalg/slepc.cpp:687-709` calls `EPSSolve(eps)` and then `EPSGetConverged` for the convergence count.
- PEP (quadratic): `SlepcPEPSolverBase` / `SlepcPEPSolver` / `SlepcPEPLinearSolver` (uses linearization to lift PEP to linear EPS), defined further down the same file.
- NEP (nonlinear): `SlepcNEPSolverBase` / `SlepcNEPSolver` for general nonlinear eigenvalue problems.

Conditionally compiled under `PALACE_WITH_SLEPC` (`palace/linalg/slepc.hpp:7`) and additionally requires PETSc compiled with complex scalars (`palace/linalg/slepc.hpp:11-13`).

**`palace::NonLinearEigenvalueSolver`** (`palace/linalg/nleps.hpp:24-144`) is Palace's own quasi-Newton implementation for nonlinear eigenvalue problems of the form `(K + λ C + λ² M + A2(λ)) x = 0`. Concrete subclass `QuasiNewtonSolver` (`palace/linalg/nleps.hpp:147-227`) implements `Solve()` directly (no external library wrapper). It holds an inner `linear_eigensolver_` of type `std::unique_ptr<EigenvalueSolver>` (`palace/linalg/nleps.hpp:166`) — typically a `SlepcEPSSolver` or `ArpackEPSSolver` — to provide initial guesses to the Newton iteration. Two helper-class hierarchies in the same file: `Interpolation` / `NewtonInterpolationOperator` for approximating the nonlinear `A2(λ)` operator with Newton polynomial interpolation.

## Shared state and the workspace pattern

All three concrete branches carry the same `mutable ComplexVector` workspace pattern (Category 3 of [`mutable-workspace-pattern`](./mutable-workspace-pattern.md)):

- ARPACK: `mutable ComplexVector x1, y1, z1;` at `palace/linalg/arpack.hpp:88`; `ArpackPEPSolver` adds `mutable ComplexVector x2, y2;` at `palace/linalg/arpack.hpp:215`.
- SLEPc: `mutable ComplexVector x1, y1;` at `palace/linalg/slepc.hpp:83`.
- Nonlinear: `mutable ComplexVector x1, y1;` at `palace/linalg/nleps.hpp:72`; `NewtonInterpolationOperator` adds `mutable ComplexVector rhs;` at `palace/linalg/nleps.hpp:265`.

These workspaces back the per-`ApplyOp` / `ApplyOpB` `Mult`-shaped routines invoked from the RCI loop (ARPACK) or shell-matrix callback (SLEPc). The lift to L1 erases them per the [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) "workspace mention and erase" rewrite.

Reference state (non-owning) is also uniform across the three branches:

- `opInv` — the `ComplexKspSolver *` for spectral-transformation inverse application. ARPACK: `palace/linalg/arpack.hpp:77`. SLEPc: `palace/linalg/slepc.hpp:106`. Nonlinear: `palace/linalg/nleps.hpp:61`.
- `opProj` — the `DivFreeSolver<ComplexVector> *` for divergence-free projection (used in the eigenmode pipeline to enforce `div E = 0` for the electric-field eigenpairs). ARPACK: `palace/linalg/arpack.hpp:81`. SLEPc: `palace/linalg/slepc.hpp:110`. Nonlinear: `palace/linalg/nleps.hpp:65`.
- `opB` — optional weighted-inner-product `Operator *`. All three branches' fields.

Owned state is the per-branch result storage (`eig`, `perm`, `res`, `xscale`, `V`/`eigenvectors`) backed by `std::unique_ptr<…[]>` (ARPACK, Nonlinear) or SLEPc-owned `EPS` / `PEP` / `NEP` objects (SLEPc).

## The RCI vs shell-matrix vs direct-Newton split

The three branches realize three distinct linear-algebra orchestration patterns:

- **ARPACK** uses **reverse communication**: ARPACK owns the iteration state; Palace's `SolveInternal` is a `while (true)` loop that calls back into Palace's `ApplyOp` / `ApplyOpB` when ARPACK requests an operator application. The Krylov-step semantics are inside ARPACK; Palace only provides operator action.
- **SLEPc** uses **shell matrices**: Palace registers `Mat` shell-matrix callbacks (`A0`, `A1`) that route SLEPc's internal operator applications back to Palace's `ComplexOperator` hierarchy. The Krylov-step semantics are inside SLEPc; Palace only provides operator action. The setup is heavier (a `Customize()` step at `palace/linalg/slepc.cpp:418-468` and at `palace/linalg/slepc.cpp:671-685` for problem-type-specific configuration) but the runtime hand-off is similar to ARPACK's.
- **`QuasiNewtonSolver`** owns the iteration itself: Palace's `Solve()` body at `palace/linalg/nleps.cpp` runs a Newton outer loop with `ComplexKspSolver`-backed inner linear solves at each iteration. There is no external eigensolver library in the loop; the wrapping is purely a concrete implementation of `EigenvalueSolver`'s interface.

L1 would name a single `eigsolve` operator (or split by problem type) and absorb the RCI / shell / direct distinction as a transparent dispatch trick; the only load-bearing axis is the problem type (linear / quadratic / nonlinear) and the spectral-transformation mode (`SetShiftInvert`).

## The `palace/models/modeeigensolver` call site

The eigenmode pipeline composes one of these wrappers via dispatch on configuration (`palace/models/modeeigensolver.cpp:1029-1047`):

- ARPACK branch (line 1033): `std::make_unique<arpack::ArpackEPSSolver>(comm, print);`.
- SLEPc branch (line 1044): `std::make_unique<slepc::SlepcEPSSolver>(comm, print);` followed by `slepc->SetType(slepc::SlepcEigenvalueSolver::Type::KRYLOVSCHUR);` (line 1045) and `slepc->SetProblemType(slepc::SlepcEigenvalueSolver::ProblemType::GEN_NON_HERMITIAN);` (line 1046).

The resulting `std::unique_ptr<EigenvalueSolver>` is stored as the `eigen` field of `ModeEigenSolver` (`palace/models/modeeigensolver.hpp:209`) and called from `ModeEigenSolver`'s `Solve()` body via `eigen->SetOperators(*opB, *opA, EigenvalueSolver::ScaleType::NONE);` (`palace/models/modeeigensolver.cpp:470`) and the subsequent `eigen->Solve()`. The wave-port eigenmode also dispatches through the same surface (`palace/models/waveportoperator.cpp:524`).

## Test coverage

There is **no dedicated `test-eigensolver.cpp`** under `palace/test/unit/`. The eigensolver wrappers are exercised only indirectly:

- `test-boundarymodeoperator.cpp` (boundary-mode operator) and `test-romoperator.cpp` (ROM operator) construct `EigenvalueSolver` instances as part of larger pipelines; they assert on end-to-end physics outputs rather than on eigensolver behavior in isolation.
- The end-to-end regression tests under `reference/palace/test/examples/` exercise the eigenmode pipeline at the application level (`eigenmode` solver type), giving system-level coverage of the SLEPc / ARPACK branches.

This is a **test-coverage gap relative to the `linalg/iterative.{hpp,cpp}` family**, which has direct unit tests (`test-orthog.cpp` for the orthogonalization helpers; the iterative solvers themselves are exercised via the same end-to-end regressions). The wrappers' algebraic claims must therefore lean more heavily on direct source reading and on the literature (Higham 2008 for the scaling, Lehoucq-Sorensen for ARPACK, Hernandez-Roman-Vidal for SLEPc) than on test linkages.

## Notes for higher layers

- **Three concrete branches share a uniform interface but realize three distinct orchestration patterns** (RCI / shell-matrix / direct-Newton). The L1 `eigsolve` operator would name only the problem-type axis (linear / quadratic / nonlinear) and the spectral-transformation mode; the orchestration axis is transparent (a dispatch trick).
- **The eigensolver-wrapper-to-`ComplexKspSolver` coupling is the substrate for the eigenmode pipeline's L4 representation**: an eigensolve is a stateful loop that calls an inner linear solve at each step (or that's queried via RCI). The inner-solve hand-off goes through `SetLinearSolver` and `opInv->Mult(…)` callbacks. This is structurally the same pattern as preconditioner application inside an iterative solver (see [`kspsolver-base-class`](./kspsolver-base-class.md)) — the inner solver is composed-not-inherited.
- **Nonlinear eigenvalue support is mixed**: SLEPc-NEP (via SLEPc), `QuasiNewtonSolver` (Palace's own). ARPACK does not provide a nonlinear branch. The `EigenvalueSolver` interface's `SetExtraSystemMatrix` and `SetPreconditionerUpdate` virtuals (`palace/linalg/eps.hpp:76-86`) are the nonlinear-only setters; both default to `MFEM_ABORT` and are overridden only by the nonlinear concrete subclasses.
- **The `ScaleType` axis is load-bearing** for the polynomial / nonlinear cases — without scaling, the operator norms `‖K‖`, `‖C‖`, `‖M‖` differ by many orders of magnitude in physically realistic problems and the eigenvalue extraction becomes ill-conditioned. The default `NORM_2` scaling implements `γ = √(‖K‖₂ / ‖M‖₂)` and `δ = 2 / (‖K‖₂ + γ ‖C‖₂ + γ² ‖M‖₂)` per Higham 2008 (the scaling-factor accessors are `GetScalingGamma` / `GetScalingDelta`). At L1 the scaling is a pre-processing transform on the operator triple, not a separate operator.

## Dependencies

- [`kspsolver-base-class`](./kspsolver-base-class.md) — `ComplexKspSolver` is the inner-linear-solver type passed to `SetLinearSolver`.
- [`apply-linop-overload-set`](./apply-linop-overload-set.md) — the `ComplexOperator` hierarchy whose `Mult` is invoked from the RCI / shell-matrix callbacks.
- [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) — the eigensolver wrappers' workspace-vector members are Category 3 (solver workspaces).

## Referenced from

- [`L0/kspsolver-base-class`](./kspsolver-base-class.md) — the linear-solver side that the eigensolver wraps and calls into via `opInv`.
- [`L0/mutable-workspace-pattern`](./mutable-workspace-pattern.md) — Category 3 entry cites these wrappers' `mutable ComplexVector` workspace members.
- Eigenmode-pipeline L1 / L4 entries (forward-target): the future `L1/eigsolve` operator and the L4 `eigensolve-monad` composition will anchor here. The L4 calculus's `iterate_while` primitive (per `book/src/design/l4_calculus.md`) will instantiate against the `Solve()` body of the three branches.

## Evidence (representative)

- `palace/linalg/eps.hpp:22-141` — `EigenvalueSolver` abstract base class definition.
- `palace/linalg/eps.hpp:25-29` — `ScaleType` enum (`NONE`, `NORM_2`).
- `palace/linalg/eps.hpp:31-42` — `WhichType` enum (nine-way spectrum-target).
- `palace/linalg/eps.hpp:44-49` — `ErrorType` enum (`ABSOLUTE`, `RELATIVE`, `BACKWARD`).
- `palace/linalg/eps.hpp:57-74` — three `SetOperators` overloads (linear / quadratic / nonlinear), each defaulting to `MFEM_ABORT`.
- `palace/linalg/eps.hpp:92-99` — `SetLinearSolver`, `SetDivFreeProjector`, `SetBMat` pure-virtuals (composition with linear solver / projector / inner-product matrix).
- `palace/linalg/eps.hpp:102-103` — `GetScalingGamma` / `GetScalingDelta` Higham-2008 scaling accessors.
- `palace/linalg/eps.hpp:116, 119` — `SetWhichEigenpairs` and `SetShiftInvert` spectral-transformation setters.
- `palace/linalg/eps.hpp:125-140` — `Solve()`, `GetEigenvalue`, `GetEigenvector`, `GetError`, `RescaleEigenvectors` result-extraction surface.
- `palace/linalg/arpack.hpp:29-170` — `ArpackEigenvalueSolver` abstract subclass (RCI orchestration).
- `palace/linalg/arpack.hpp:77-89` — non-owning references (`opInv`, `opProj`, `opB`) + workspace `mutable ComplexVector x1, y1, z1`.
- `palace/linalg/arpack.hpp:173-201` — `ArpackEPSSolver` (generalized linear).
- `palace/linalg/arpack.hpp:204-236` — `ArpackPEPSolver` (quadratic polynomial), with extra workspace `mutable ComplexVector x2, y2` at line 215.
- `palace/linalg/arpack.cpp:263-358` — `SolveInternal` RCI loop body; `naupd` driver call at line 318; `ApplyOp` at line 325; `ApplyOpB` at line 329.
- `palace/linalg/arpack.cpp:300-304` — `MFEM_ABORT` for `TARGET_REAL` / `TARGET_IMAGINARY` (ARPACK does not implement these).
- `palace/linalg/arpack.cpp:513-560` — `ArpackEPSSolver::Solve()` body: ncv / arpack_it defaults, RCI invocation via `SolveInternal` at line 552, then `RescaleEigenvectors`.
- `palace/linalg/slepc.hpp:54-198` — `SlepcEigenvalueSolver` abstract subclass (shell-matrix orchestration).
- `palace/linalg/slepc.hpp:57-67` — `ProblemType` enum (eight-way).
- `palace/linalg/slepc.hpp:69-80` — `Type` enum (nine-way solver method).
- `palace/linalg/slepc.hpp:83` — workspace `mutable ComplexVector x1, y1`.
- `palace/linalg/slepc.hpp:201-249` — `SlepcEPSSolverBase` for linear problems.
- `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve()` body: `EPSSolve(eps)` (line 694), `EPSGetConverged` (line 695).
- `palace/linalg/nleps.hpp:24-144` — `NonLinearEigenvalueSolver` abstract subclass.
- `palace/linalg/nleps.hpp:72` — workspace `mutable ComplexVector x1, y1`.
- `palace/linalg/nleps.hpp:147-227` — `QuasiNewtonSolver` concrete (direct-Newton).
- `palace/linalg/nleps.hpp:166` — inner `linear_eigensolver_` (typically SLEPc-EPS or ARPACK-EPS).
- `palace/models/modeeigensolver.cpp:1029-1047` — dispatch site that constructs ARPACK or SLEPc wrapper based on configuration.
- `palace/models/modeeigensolver.cpp:470` — `eigen->SetOperators(*opB, *opA, EigenvalueSolver::ScaleType::NONE)` call.
- `palace/models/modeeigensolver.hpp:209` — `std::unique_ptr<EigenvalueSolver> eigen;` field declaration.
- `palace/models/waveportoperator.cpp:524` — wave-port eigenmode dispatch through the same `EigenvalueSolver` interface.
