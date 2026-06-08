# Class — `BaseKspSolver<OperType>`

A reference note for L1 / L2 / L4 entries that touch Palace's Krylov-solver surface. The composition class that pairs an iterative solver (`IterativeSolver<OperType>`) with an optional preconditioner (`Solver<OperType>`) and exposes the public "solve `Ax = b` for `x`" entry point. Anchors the L4 `solve-monad` concept to a concrete C++ class and is the call-site target for solver use across Palace's model pipelines (electrostatic, magnetostatic, eigenmode, driven, transient).

## At a glance

The class is declared at `palace/linalg/ksp.hpp:29-72` and templated on `OperType ∈ {Operator, ComplexOperator}`. The two instantiations are aliased at the bottom of the file:

```cpp
using KspSolver = BaseKspSolver<Operator>;
using ComplexKspSolver = BaseKspSolver<ComplexOperator>;
```

`BaseKspSolver` is **not** itself an `Operator` or `Solver` subclass — unlike `IterativeSolver<OperType>` (which inherits from `Solver<OperType>`, which inherits from `OperType`, so an iterative solver is-an operator), `BaseKspSolver` is a free-standing composition. It owns an iterative solver + preconditioner pair (`std::unique_ptr<IterativeSolver<OperType>> ksp` at `ksp.hpp:41`; `std::unique_ptr<Solver<OperType>> pc` at line 42) and a small statistics surface (`ksp_mult`, `ksp_mult_it` counters at line 46).

## The public surface

Three constructors plus a small set of accessors and the central `Mult` method (`ksp.hpp:52-72`):

- **Config-driven constructor** (`ksp.hpp:52-54`, definition at `ksp.cpp:244-255`) — takes a `config::LinearSolverData` reference, a verbosity level, a `FiniteElementSpaceHierarchy &fespaces` (for the multigrid case), and an optional auxiliary-space hierarchy. Delegates to the two factory functions `ConfigureKrylovSolver<OperType>` and `ConfigurePreconditionerSolver<OperType>` (defined in the anonymous namespace; see [`ksp-factory-file`](./ksp-factory-file.md)) to build the iterative-solver and preconditioner objects, then chains to the third constructor.
- **IoData-driven constructor** (`ksp.hpp:55-56`, definition at `ksp.cpp:257-263`) — thin convenience wrapper around the above, pulling `iodata.solver.linear` and `iodata.problem.verbose`.
- **Move-in constructor** (`ksp.hpp:57-58`, definition at `ksp.cpp:265-274`) — accepts pre-built `IterativeSolver` and `Solver` `unique_ptr`s and wires them together. The wiring step at `ksp.cpp:272` calls `this->ksp->SetPreconditioner(*this->pc)` — this is the load-bearing line that registers the preconditioner with the iterative solver's `B` field (see [Composition wiring](#composition-wiring) below).
- **Statistics accessors** (`ksp.hpp:60-61`) — `NumTotalMult()` and `NumTotalMultIterations()` return cumulative-solve and cumulative-iteration counts. The counters are incremented in `Mult` (`ksp.cpp:308-309`).
- **Tolerance forwarding** (`ksp.hpp:64-67`) — `GetRelTol` / `GetAbsTol` / `SetRelTol` / `SetAbsTol` forward to the underlying `ksp` object.
- **`SetOperators(op, pc_op)`** (`ksp.hpp:69`, definition at `ksp.cpp:276-294`) — points the iterative solver at the system operator `op` and the preconditioner at `pc_op`. Includes a multigrid-aware special case: if `pc_op` is a `BaseMultigridOperator<OperType>` and the preconditioner is **not** a `GeometricMultigridSolver`, only the finest-level operator is passed through.
- **`Mult(b, x)`** (`ksp.hpp:71`, definition at `ksp.cpp:296-310`) — the central method. Solves `A · x = b` for `x`; the public entry point all solver-using code in Palace reaches.

## The `Mult` method

The body (`ksp.cpp:296-310`) is compact and reads as the canonical "solve" call:

```cpp
template <typename OperType>
void BaseKspSolver<OperType>::Mult(const VecType &x, VecType &y) const
{
  BlockTimer bt(Timer::KSP, use_timer);
  ksp->Mult(x, y);
  if (!ksp->GetConverged())
  {
    Mpi::Warning(/* ... non-convergence warning ... */);
  }
  ksp_mult++;
  ksp_mult_it += ksp->GetNumIterations();
}
```

Three operational concerns surface here:

1. **Timer wrapping** — `BlockTimer bt(Timer::KSP, use_timer);` is RAII timing for the whole solve. The `use_timer` flag is set to `true` by the config-driven constructor (`ksp.cpp:254`) and `false` by the move-in constructor (`ksp.cpp:268`).
2. **Convergence warning** — if `ksp->GetConverged()` returns false, a warning is logged with the final residual ratio. The solve still returns; non-convergence is **soft-failure**, not an abort. Callers that need hard-failure on non-convergence must check the underlying `ksp->GetConverged()` themselves.
3. **Statistics update** — every `Mult` call increments `ksp_mult` (the number of solves) and adds the inner-iteration count to `ksp_mult_it`. This is the counter the model pipelines read for reporting "total Krylov iterations across the simulation."

The argument-name swap is a load-bearing readability quirk: the **`b` (right-hand side) is in `x`** and the **`x` (solution) is in `y`**. The `Mult` interface is inherited semantically from operator application — "apply this `solver` to vector `x` to produce vector `y`" — so syntactically the solver is being treated as the linear map `A⁻¹`. Mathematically this is correct (`y = A⁻¹ · x` is the same statement as "solve `A · y = x` for `y`"); see [`concepts/solver-as-operator`](../concepts/solver-as-operator.md) for the L1-level treatment.

## Composition wiring

The third constructor (`ksp.cpp:265-274`) is the load-bearing one for the *composition* aspect. It takes ownership of the iterative solver and preconditioner, then calls:

```cpp
if (this->pc)
{
  this->ksp->SetPreconditioner(*this->pc);
}
```

This is the moment the preconditioner is registered with the iterative solver. After this line, `ksp->B` points at `pc` and the iterative solver's per-step `ApplyB(B, r, z, ...)` call (e.g. `iterative.cpp:389` in CG, `iterative.cpp:627` in GMRES through `ApplyBA`) routes to the preconditioner's `Mult`. Without this wiring step the iterative solver would have `B = nullptr` and would run unpreconditioned (which CG and GMRES both handle — they fall through to `z = r` and skip the preconditioner-apply branch).

`SetOperators` (`ksp.cpp:276-294`) wires the system operator and preconditioner-operator into their respective objects. The split between system operator and preconditioner operator allows the preconditioner to be built from a *different* matrix than the system matrix (e.g. an approximate factorisation, a coarser-grid hierarchy, or a different sparsity pattern) — a standard pattern in iterative solvers that the L1 `apply_linop` collapse preserves as two separate `LinearOperator` arguments to the solve.

## Construction flow

Putting it together, a typical call site (e.g. inside a Palace driver) builds a `BaseKspSolver` like this:

1. The driver assembles its system operator `A` (an `Operator` or `ComplexOperator` subclass — `ParOperator`, a `SumOperator` of FE bilinear forms, etc.).
2. The driver constructs an `IoData` (or `config::LinearSolverData`) from the user's JSON config.
3. The driver calls `BaseKspSolver(iodata, fespaces, aux_fespaces)`. This:
   - Calls `ConfigureKrylovSolver<OperType>(linear, verbose, comm)` to build the iterative solver (CG / GMRES / FGMRES per [`ksp-factory-file`](./ksp-factory-file.md)).
   - Calls `ConfigurePreconditionerSolver<OperType>(linear, verbose, comm, fespaces, aux_fespaces)` to build the preconditioner (AMS / BOOMER_AMG / SUPERLU / STRUMPACK / MUMPS / JACOBI; geometric-multigrid wrapping if `fespaces.GetNumLevels() > 1`).
   - Calls the move-in constructor with the two `unique_ptr`s; this performs the composition wiring.
4. The driver calls `solver.SetOperators(A, pc_op)` to point the solver at the system operator and the preconditioner at its operator (often `pc_op == A` for a black-box preconditioner; sometimes a different matrix).
5. The driver calls `solver.Mult(b, x)` once per linear solve (potentially many times across a transient or nonlinear iteration).

The L4 `solve-monad` concept abstracts this whole flow: a constructed solver is a value of type `Solver[A]` parameterised by the operator type `A`; the `Mult(b, x)` call is the monadic "extract" — given `b`, produce the `x` such that `A · x = b` (modulo convergence tolerance and non-convergence soft-failure semantics).

## Notes for higher layers

- **`BaseKspSolver` is the natural anchor for the L1 `ksp_solve` operator** (the methodology concept page [`concepts/ksp_solve`](../concepts/ksp_solve.md) carries the pure-functional shape) — `ksp_solve(solver, b) = x where A · x = b`. The L1 form drops the in-place destination `y`, the statistics counters, and the convergence-warning side-channel; the pure functional form returns the solution vector. Non-convergence in the L1 form would be modelled either as a sentinel return value or as a separate `convergence-status` output, per the L1 design discussion in [`concepts/convergence-test`](../concepts/convergence-test.md).
- **The composition pattern (iterative + preconditioner) is what the L4 `solve-monad` lifts** — at L4 a "solver" is a value parameterised by an operator type and a (possibly empty) preconditioner type. The `BaseKspSolver` class is one concrete realisation; `MfemWrapperSolver` (also at `palace/linalg/solver.hpp:70-134`) is another. Both are `Solver<OperType>` subclasses; both expose a `Mult` of the same shape.
- **The unimplemented branches in the factory** (`MINRES` / `BICGSTAB` / `DEFAULT`) are documented in [`ksp-factory-file`](./ksp-factory-file.md). `BaseKspSolver` itself has no enum-based dispatch — the abort happens upstream during factory construction; once the `BaseKspSolver` exists, the iterative solver inside it is always one of the implemented kinds.

## Referenced from

- [`L1/ksp_solve`](../L1/ksp_solve.md) — the pure-functional solve operator anchored on this class's `Mult` entry point.
- [`L2/krylov_step`](../L2/krylov_step.md) — the per-step body that `BaseKspSolver::Mult` invokes (via `ksp->Mult`) when the inner iterative solver is one of CG / GMRES / FGMRES.
- [`L1/apply_linop`](../L1/apply_linop.md) — `BaseKspSolver` owns an `OperType` reference (the system operator) and dispatches `apply_linop` calls into it from inside the iterative solver.
- [`L0/ksp-factory-file`](./ksp-factory-file.md) — the factory functions that construct the `IterativeSolver` and `Solver` objects passed to the `BaseKspSolver` constructor.
- [`L0/apply-linop-overload-set`](./apply-linop-overload-set.md) — the `OperType` template parameter resolves to one of `Operator` / `ComplexOperator`, whose `Mult` family is the per-step primitive.
- [`concepts/solver-as-operator`](../concepts/solver-as-operator.md) — the methodology concept (a solver "is" a linear operator under the algebraic identification `A → A⁻¹`).
- [`concepts/solve-monad`](../concepts/solve-monad.md) — the L4 abstraction over the construction-then-apply flow.
- [`concepts/ksp_solve`](../concepts/ksp_solve.md) — the L1-shaped pure-functional solve operator concept page.

## Evidence (representative)

- `palace/linalg/ksp.hpp:29-72` — `BaseKspSolver<OperType>` template class declaration.
- `palace/linalg/ksp.hpp:32-34` — `static_assert` restricting `OperType` to `Operator` or `ComplexOperator`.
- `palace/linalg/ksp.hpp:36-37` — `VecType` deduced from `OperType` (`ComplexVector` for complex, `Vector` for real).
- `palace/linalg/ksp.hpp:41-42` — owned `ksp` (iterative solver) and `pc` (preconditioner) `unique_ptr`s.
- `palace/linalg/ksp.hpp:46` — `ksp_mult`, `ksp_mult_it` cumulative statistics counters.
- `palace/linalg/ksp.hpp:49` — `use_timer` flag.
- `palace/linalg/ksp.hpp:52-58` — three constructor declarations (config-driven, iodata-driven, move-in).
- `palace/linalg/ksp.hpp:60-61` — `NumTotalMult()` / `NumTotalMultIterations()` accessors.
- `palace/linalg/ksp.hpp:64-67` — tolerance accessor / mutator forwarding to `ksp`.
- `palace/linalg/ksp.hpp:69` — `SetOperators(op, pc_op)` declaration.
- `palace/linalg/ksp.hpp:71` — `Mult(x, y) const` declaration.
- `palace/linalg/ksp.hpp:74-75` — `KspSolver` / `ComplexKspSolver` type aliases.
- `palace/linalg/ksp.cpp:244-255` — config-driven constructor definition (calls the two factories).
- `palace/linalg/ksp.cpp:257-263` — iodata-driven constructor definition.
- `palace/linalg/ksp.cpp:265-274` — move-in constructor: load-bearing composition-wiring step at line 272 (`this->ksp->SetPreconditioner(*this->pc)`).
- `palace/linalg/ksp.cpp:276-294` — `SetOperators` definition with the multigrid-finest-operator special case at lines 283-288.
- `palace/linalg/ksp.cpp:296-310` — `Mult` definition (the central "solve" entry point).
- `palace/linalg/ksp.cpp:312-313` — explicit template instantiations for `Operator` and `ComplexOperator`.
- `palace/linalg/iterative.hpp:25-115` — `IterativeSolver<OperType>` base class declaration (the type of the `ksp` member); declares `A`, `B`, tolerance / iteration state, and the abstract `Mult` to be overridden by `CgSolver` / `GmresSolver` / `FgmresSolver`.
- `palace/linalg/solver.hpp:21-65` — `Solver<OperType>` base class declaration (the type of the `pc` member); inherits from `OperType` (so a `Solver` is-an `Operator`).
