---
agent: layer-intro-author
invoked_at: 2026-05-27T08:10:50Z
scope: L0 reference-notes bootstrap, bundle 2
status: integrated
integrated_at: 2026-05-27T09:08:49Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Cycle-006 wave-1 L0 bootstrap bundle 2 (2 of 5 applied this cycle). Per-report integrator
  applied 4 proposed-changes blocks: 2 new L0 chapter files, L0/index.md grouping addition,
  SUMMARY.md double-row insertion. Per-report deferred integrated_at to finalize per role-spec.
---

# CYCLE: L0 reference-notes bootstrap, bundle 2

## Summary

Bundle 2 of the multi-cycle L0 reference-notes buildout (priority #10). Adds two medium-scope chapters per the cycle-006 planner's recommendation in §Open questions / caveats item 3:

1. `book/src/L0/apply-linop-overload-set.md` — the `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult` overload set across the `Operator` / `ComplexOperator` hierarchy, plus the concrete-subclass family (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator` / `ComplexParOperator`). This is the L0 anchor that the L1 `apply_linop` entry references repeatedly and that future L1>L0 audits on `apply-linop-mutation-rotation` will read.
2. `book/src/L0/kspsolver-base-class.md` — the `BaseKspSolver<OperType>` solver-interface class that composes an iterative solver + preconditioner and exposes `Mult(b, x)` as the public "solve `Ax = b` for `x`" entry point. Anchors the L4 `krylov-step` / `solve-monad` concepts to the concrete C++ surface.

Both chapters follow bundle 1 style: 2–4 paragraphs of interpretation per region, representative citations only (no line-by-line transcription), forward-declared `Referenced from:` blocks for the L1 / L4 entries that will be thinned in the retroactive sweep (priority #11). Index update folds the two new entries into the existing reference-note cohort.

## Proposed changes

### New file 1 — `book/src/L0/apply-linop-overload-set.md`

```edit:book/src/L0/apply-linop-overload-set.md
[old]: (new file)
[new]: # Overload set — `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult`

A reference note for L1 entries (and the L1>L0 `apply-linop-mutation-rotation` theme). The L0 home of operator application in Palace: a family of virtual methods on the `Operator` / `ComplexOperator` interface, implemented across a deep concrete-subclass hierarchy. L1 collapses this entire family to one operator (`apply_linop`); this overview names the L0 shape so an L1 entry or lowering theme can refer to "the `Mult` family" without re-citing every overload.

## At a glance

**Two interface hierarchies, same shape.** Palace exposes operator application through two parallel abstract base classes:

- `mfem::Operator` (re-exported as `palace::Operator` via `using Operator = mfem::Operator;` at `palace/linalg/operator.hpp:21`) — the real-valued base. The pure-virtual `Mult(const Vector &x, Vector &y) const` is inherited from MFEM.
- `palace::ComplexOperator` (declared at `palace/linalg/operator.hpp:24-68`) — the complex-valued base, defined inside Palace (not MFEM). The pure-virtual `Mult(const ComplexVector &x, ComplexVector &y) const = 0` is declared at line 54.

Both bases declare `Height()` / `Width()` accessors (real at `operator.hpp:36-39` for `ComplexOperator`; inherited from `mfem::Operator` for the real branch). Both expose the same overload-set shape; the element-type axis is the only difference.

**The overload set has three orthogonal sub-axes**:

1. **Transpose mode** — `Mult`, `MultTranspose`, `MultHermitianTranspose`. The forward apply, the transpose apply, and (complex only) the Hermitian-transpose apply. Declarations for `ComplexOperator` at `operator.hpp:54-58`; for `Operator` inherited from `mfem::Operator`. The Hermitian-transpose method exists only on the complex branch — on the real branch it collapses to the plain transpose. The `MultTranspose` and `MultHermitianTranspose` methods on `ComplexOperator` are **non-pure** virtuals with default implementations, declared but defined elsewhere; only `Mult` is pure.
2. **Accumulate mode** — `Mult` (overwrites `y`) vs `AddMult` (accumulates `a · A · x` into `y`). For `ComplexOperator` these are at `operator.hpp:60-67`; both forms exist for transpose and hermitian-transpose. The `a` parameter defaults to `1.0` (real or complex per template instantiation).
3. **Element type** — `Operator` (real, `double` scalar, `Vector` argument) vs `ComplexOperator` (complex, `std::complex<double>` scalar, `ComplexVector` argument). At L1 these collapse via parametric polymorphism over the element type (see [`mfem-vector-types`](./mfem-vector-types.md) and [`L1/apply_linop`](../L1/apply_linop.md) Variant axes).

The full set therefore has up to 12 entries per concrete subclass on the complex branch (3 transpose modes × 2 accumulate modes × forward / templated paths) and 4 on the real branch (2 transpose modes × 2 accumulate modes). Most subclasses override a subset — typically `Mult`, `MultTranspose`, and `AddMult` for the forward direction, deferring Hermitian-transpose to a helper template ([`ProductOperatorHelper`](#dispatch-helper-templates) below).

## Concrete-subclass family

The hierarchy is broad. Each concrete subclass realises the abstract interface for a specific operator-construction pattern; the same `Mult` virtual is overridden across all of them. The L1 `LinearOperator` opaque type collapses all of them.

- **`ComplexWrapperOperator`** (`operator.hpp:73-113`) — wraps a pair of real operators `(Ar, Ai)` as a complex operator via the equivalent-real block formulation `[Ar -Ai; Ai Ar]`. The bridge between the real and complex hierarchies; relevant to the [`complex-from-real-lift`](../concepts/complex-from-real-lift.md) concept.
- **`SumOperator`** (`operator.hpp:116-136`) — represents `Σᵢ cᵢ · Aᵢ` for a collection of operators with scalar coefficients (`std::vector<std::pair<const Operator *, double>> ops`, line 119). Real-branch only; the `Mult` definition at `operator.cpp:428-441` has a single-operator fast path and otherwise zeros `y` then calls `AddMult`. The `AddMult` body at `operator.cpp:458-466` is the canonical witness of operator-side linearity (loop accumulating `op->Mult(x, z); y.Add(a * c, z)`).
- **`BaseProductOperator<OperType>`** (`operator.hpp:178-226`) — operator composition `A · B`. Templated over `OperType ∈ {Operator, ComplexOperator}`; aliased as `ProductOperator` (real) and `ComplexProductOperator` (complex) at `operator.hpp:228-229`. The `Mult` definition at `operator.hpp:202-206` is the two-step `B.Mult(x, z); A.Mult(z, y)` — direct L0 witness of the L1 composition law. Workspace `z` is a mutable member (`operator.hpp:192`).
- **`BaseDiagonalOperator<OperType>`** (`operator.hpp:256-291`) — element-wise scaling by a vector `d` (the "diagonal of a diagonal matrix"). The forward and transpose forms coincide (`MultTranspose` delegates to `Mult` at `operator.hpp:279`). Real and complex specialisations of `Mult` at `operator.cpp:478-507` (real at 478-487, complex at 489-507).
- **`BaseMultigridOperator<OperType>`** (`operator.hpp:298-367`) — a hierarchy of operators (one per multigrid level) plus optional auxiliary-space operators. The `Mult` family dispatches to the finest-level operator (`operator.hpp:347, 349-352, 354-357`), so the multigrid hierarchy is invisible at the apply-time interface; the level structure is consumed by the geometric-multigrid solver, not by the operator-application path.
- **`ParOperator`** / **`ComplexParOperator`** (defined in `palace/linalg/rap.hpp`, implementations in `palace/linalg/rap.cpp`) — parallel wrappers that apply prolongation around the inner operator and restriction after it, with optional Dirichlet-BC tdof masking. The `ParOperator::Mult` body at `palace/linalg/rap.cpp:195-234` is the canonical wrapper-apply pattern. Per the single-rank reading (CLAUDE.md §Scope), the prolongation / restriction collapses to identity and the masking is the only remaining concern at L1.

A non-exhaustive list. Other operator-shaped types in Palace (preconditioners under `palace/linalg/`, FE assembly closures under `palace/fem/`, Jacobian-action operators) all implement the same interface; the overload-set shape is uniform.

## Dispatch helper templates

Two templated helper-class hierarchies factor out the Hermitian-transpose dispatch:

- **`ProductOperatorHelper<ProductOperator, OperType>`** (`operator.hpp:140-176`) — partial specialisations for `OperType = Operator` (empty body) and `OperType = ComplexOperator` (defines `MultHermitianTranspose` and `AddMultHermitianTranspose` via two-step apply on the inner `A` and `B`). The real branch inherits no extra methods; the complex branch gets the Hermitian-transpose method synthesised from the inner operators' Hermitian-transposes.
- **`DiagonalOperatorHelper<DiagonalOperator, OperType>`** (`operator.hpp:232-254`) — same pattern for `BaseDiagonalOperator`: the complex branch declares `MultHermitianTranspose` and `AddMultHermitianTranspose`; the real branch does not.

These helpers exist because the Hermitian-transpose method is only meaningful on `ComplexOperator` and would be empty on `Operator`. CRTP (Curiously Recurring Template Pattern) plus partial specialisation produces the desired branch-by-branch interface without virtual-method bloat on the real side.

## The L1 collapse

L1 `apply_linop` collapses this entire overload set to one operator: `y = apply_linop(A, x)`. The three sub-axes are handled as follows (per [`L1/apply_linop`](../L1/apply_linop.md) Variant axes):

- **Transpose mode** — recoverable via algebraic transforms `Aᵀ`, `Aᴴ`; not separate L1 operators. The dedicated virtual methods at L0 exist for representation-aware specialisation (a sparse-matrix `A` may transpose efficiently in-place; a matrix-free `A` may have a separate transpose-action implementation), but at L1 the rotation `apply_linop(A, x) → apply_linop(Aᵀ, x)` is a one-argument-substitution.
- **Accumulate mode** — `AddMult(A, x, a, y) → y + a · A · x` is the L1 composition `axpby(a, apply_linop(A, x), 1, y)`. Not a separate operator; the L0 fusion is recorded as a transparent performance trick in the L1>L0 lowering theme [`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md).
- **Element type** — the `Operator` / `ComplexOperator` split collapses to parametric polymorphism over the element type. The semantics are identical across element types — the linear-map relationship is the same; only the underlying scalar field differs.
- **Operator representation** (the implicit fourth axis, fully absorbed) — `SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`, all preconditioners, all FE assembly closures, all Jacobian-action operators — all collapse to a single opaque `LinearOperator[M, N]` type at L1. This is the canonical *variant absorption* application (per [`concepts/variant-absorption`](../concepts/variant-absorption.md)).

## Referenced from

*The L1 / L1>L0 entries below already cite this overload set inline. The retroactive-thinning sweep (priority #11) will replace those inline citations with backlinks here.*

- [`L1/apply_linop`](../L1/apply_linop.md) — collapses the entire overload set to one operator parameterised by element type.
- [`L1-L0/apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) — the L1>L0 lowering theme that reintroduces the destination-buffer mention and selects between the `Mult` and `AddMult` forms per sub-pattern.
- [`concepts/constructed-operators`](../concepts/constructed-operators.md) — narrative for the `BaseProductOperator` / `SumOperator` family.
- [`concepts/complex-from-real-lift`](../concepts/complex-from-real-lift.md) — narrative for the `ComplexWrapperOperator` real-imag block formulation.
- [`L0/ksp-factory-file`](./ksp-factory-file.md) — uses `Operator` / `ComplexOperator` as the `OperType` template parameter throughout the KSP construction surface.
- [`L0/kspsolver-base-class`](./kspsolver-base-class.md) — the `BaseKspSolver<OperType>` wraps an operator of this hierarchy and exposes a `Mult` of the same interface shape.

## Evidence (representative)

- `palace/linalg/operator.hpp:21` — `using Operator = mfem::Operator;` — real branch type alias.
- `palace/linalg/operator.hpp:24-68` — `ComplexOperator` abstract class: declares pure-virtual `Mult` (line 54), non-pure `MultTranspose` (56), `MultHermitianTranspose` (58), `AddMult` (60), `AddMultTranspose` (63), `AddMultHermitianTranspose` (66).
- `palace/linalg/operator.hpp:36-39` — `Height()` / `Width()` accessors on `ComplexOperator`.
- `palace/linalg/operator.hpp:73-113` — `ComplexWrapperOperator` (equivalent-real block formulation).
- `palace/linalg/operator.hpp:116-136` — `SumOperator` (real-only sum-of-operators).
- `palace/linalg/operator.hpp:140-176` — `ProductOperatorHelper` partial specialisations (Hermitian-transpose synthesis).
- `palace/linalg/operator.hpp:178-226` — `BaseProductOperator<OperType>` template (operator composition).
- `palace/linalg/operator.hpp:202-206` — `BaseProductOperator::Mult` body: two-step `B.Mult(x, z); A.Mult(z, y)`. Direct L0 witness of L1 composition law.
- `palace/linalg/operator.hpp:228-229` — `ProductOperator` / `ComplexProductOperator` aliases.
- `palace/linalg/operator.hpp:232-291` — `DiagonalOperatorHelper` + `BaseDiagonalOperator<OperType>` (element-wise scaling).
- `palace/linalg/operator.hpp:298-367` — `BaseMultigridOperator<OperType>` (hierarchy; `Mult` dispatches to finest level).
- `palace/linalg/operator.cpp:428-441` — `SumOperator::Mult` body: single-op fast path + multi-op `y = 0; AddMult(x, y)` dispatch.
- `palace/linalg/operator.cpp:458-466` — `SumOperator::AddMult` body: loop `op->Mult(x, z); y.Add(a * c, z)`.
- `palace/linalg/operator.cpp:478-507` — `BaseDiagonalOperator<Operator>::Mult` (478-487) + `BaseDiagonalOperator<ComplexOperator>::Mult` (489-507) definitions.
- `palace/linalg/rap.cpp:195-234` — `ParOperator::Mult` body (prolongation + inner-op + restriction + BC masking).
- `palace/linalg/rap.cpp:236-275` — `ParOperator::MultTranspose` body (swaps prolongation/restriction roles; representation-aware transpose).
- `palace/linalg/rap.cpp:481-517` — `ComplexParOperator::Mult` body.
- `palace/linalg/iterative.cpp:379, 443` — CG using `A->Mult(p, z)` per step (downstream use site, demonstrates the `Mult` family is the per-step iterative-solver primitive).
```

### New file 2 — `book/src/L0/kspsolver-base-class.md`

```edit:book/src/L0/kspsolver-base-class.md
[old]: (new file)
[new]: # Class — `BaseKspSolver<OperType>`

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

- **`BaseKspSolver` is the natural anchor for the L1 `ksp_solve` operator** (not yet authored — `L1/ksp_solve.md` does not currently exist; only the methodology concept page [`concepts/ksp_solve`](../concepts/ksp_solve.md) is present; harvester firm-up anticipated cycle-007+) — `ksp_solve(solver, b) = x where A · x = b`. The L1 form drops the in-place destination `y`, the statistics counters, and the convergence-warning side-channel; the pure functional form returns the solution vector. Non-convergence in the L1 form would be modelled either as a sentinel return value or as a separate `convergence-status` output, per the L1 design discussion in [`concepts/convergence-test`](../concepts/convergence-test.md).
- **The composition pattern (iterative + preconditioner) is what the L4 `solve-monad` lifts** — at L4 a "solver" is a value parameterised by an operator type and a (possibly empty) preconditioner type. The `BaseKspSolver` class is one concrete realisation; `MfemWrapperSolver` (also at `palace/linalg/solver.hpp:70-134`) is another. Both are `Solver<OperType>` subclasses; both expose a `Mult` of the same shape.
- **The unimplemented branches in the factory** (`MINRES` / `BICGSTAB` / `DEFAULT`) are documented in [`ksp-factory-file`](./ksp-factory-file.md). `BaseKspSolver` itself has no enum-based dispatch — the abort happens upstream during factory construction; once the `BaseKspSolver` exists, the iterative solver inside it is always one of the implemented kinds.

## Referenced from

*Forward-declared. The L1 `ksp_solve` operator (queued, not yet firm — no `L1/ksp_solve.md` chapter exists yet; harvester firm-up anticipated cycle-007+), the L2 `krylov-step` entry, and the L4 `solve-monad` / `solver-as-operator` concept pages will all reference this chapter when they expand.*

- [`L2/krylov-step`](../L2/krylov-step.md) — the per-step body that `BaseKspSolver::Mult` invokes (via `ksp->Mult`) when the inner iterative solver is one of CG / GMRES / FGMRES.
- [`L1/apply_linop`](../L1/apply_linop.md) — `BaseKspSolver` owns an `OperType` reference (the system operator) and dispatches `apply_linop` calls into it from inside the iterative solver.
- [`L0/ksp-factory-file`](./ksp-factory-file.md) — the factory functions that construct the `IterativeSolver` and `Solver` objects passed to the `BaseKspSolver` constructor.
- [`L0/apply-linop-overload-set`](./apply-linop-overload-set.md) — the `OperType` template parameter resolves to one of `Operator` / `ComplexOperator`, whose `Mult` family is the per-step primitive.
- [`concepts/solver-as-operator`](../concepts/solver-as-operator.md) — the methodology concept (a solver "is" a linear operator under the algebraic identification `A → A⁻¹`).
- [`concepts/solve-monad`](../concepts/solve-monad.md) — the L4 abstraction over the construction-then-apply flow.
- [`concepts/ksp_solve`](../concepts/ksp_solve.md) — the L1-shaped pure-functional solve operator (concept page only; `L1/ksp_solve.md` chapter not yet authored — anticipated cycle-007+).

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
```

### Edit — `book/src/L0/index.md` (update reference-note cohort list)

```edit:book/src/L0/index.md
[old]: **File overviews** — anchor files L1 references repeatedly:

- [`linalg-vector-file`](./linalg-vector-file.md) — `palace/linalg/vector.{hpp,cpp}` at a glance. The home of `ComplexVector`, the `AXPY/AXPBY/AXPBYPCZ` family, `Dot`/`TransposeDot`/`LocalDot`, `Norml2`, `Normalize`.
- [`ksp-factory-file`](./ksp-factory-file.md) — `palace/linalg/ksp.cpp` Krylov-solver factory. Enum-routed dispatch: CG / GMRES / FGMRES implemented; MINRES / BICGSTAB / DEFAULT abort. Anchor for the "advertised-but-unimplemented" pattern that drives the MINRES / BiCGStab obstruction themes.
[new]: **File overviews** — anchor files L1 references repeatedly:

- [`linalg-vector-file`](./linalg-vector-file.md) — `palace/linalg/vector.{hpp,cpp}` at a glance. The home of `ComplexVector`, the `AXPY/AXPBY/AXPBYPCZ` family, `Dot`/`TransposeDot`/`LocalDot`, `Norml2`, `Normalize`.
- [`ksp-factory-file`](./ksp-factory-file.md) — `palace/linalg/ksp.cpp` Krylov-solver factory. Enum-routed dispatch: CG / GMRES / FGMRES implemented; MINRES / BICGSTAB / DEFAULT abort. Anchor for the "advertised-but-unimplemented" pattern that drives the MINRES / BiCGStab obstruction themes.

**Overload sets and class interfaces** — multi-overload / multi-subclass surfaces referenced by L1 / L2 / L4 entries:

- [`apply-linop-overload-set`](./apply-linop-overload-set.md) — the `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult` family on the `Operator` / `ComplexOperator` hierarchy, plus the concrete-subclass family (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`). The L0 anchor for `L1/apply_linop`'s 12-method-overload collapse and for the `apply-linop-mutation-rotation` lowering theme.
- [`kspsolver-base-class`](./kspsolver-base-class.md) — `BaseKspSolver<OperType>` in `palace/linalg/ksp.{hpp,cpp}`. The composition class pairing an `IterativeSolver` with a `Solver` (preconditioner) and exposing the public `Mult(b, x)` "solve `Ax = b`" entry point. Anchors the L4 `solve-monad` concept to concrete C++ and is the call-site target for solver use across Palace's model pipelines.
```

### Edit — `book/src/SUMMARY.md` (register the two new chapters)

```edit:book/src/SUMMARY.md
[old]: # L0 — Cited Palace Source + Reference Notes
- [Overview](./L0/index.md)
- [Convention — output-arg vs receiver](./L0/output-arg-vs-receiver.md)
- [Convention — MFEM vector types](./L0/mfem-vector-types.md)
- [Convention — linalg:: free-function wrappers](./L0/linalg-free-functions.md)
- [Convention — transparent vs load-bearing tricks](./L0/transparent-vs-load-bearing-tricks.md)
- [File — palace/linalg/vector.{hpp,cpp}](./L0/linalg-vector-file.md)
- [File — palace/linalg/ksp.cpp](./L0/ksp-factory-file.md)
[new]: # L0 — Cited Palace Source + Reference Notes
- [Overview](./L0/index.md)
- [Convention — output-arg vs receiver](./L0/output-arg-vs-receiver.md)
- [Convention — MFEM vector types](./L0/mfem-vector-types.md)
- [Convention — linalg:: free-function wrappers](./L0/linalg-free-functions.md)
- [Convention — transparent vs load-bearing tricks](./L0/transparent-vs-load-bearing-tricks.md)
- [File — palace/linalg/vector.{hpp,cpp}](./L0/linalg-vector-file.md)
- [File — palace/linalg/ksp.cpp](./L0/ksp-factory-file.md)
- [Overload set — Mult / MultTranspose / AddMult](./L0/apply-linop-overload-set.md)
- [Class — BaseKspSolver](./L0/kspsolver-base-class.md)
```

## Supporting evidence

**Bundle 1 chapters reviewed for style match:**
- `book/src/L0/output-arg-vs-receiver.md` — convention page; 2-paragraph idiom explanation + L1 lift + idiom rationale + Referenced-from forward-declarations + Evidence.
- `book/src/L0/linalg-free-functions.md` — convention page; wrapping pattern + three shape examples + closing notes on non-wrappers + notable absence + Referenced-from + Evidence.
- `book/src/L0/linalg-vector-file.md` — file overview; At-a-glance regions + thematic sub-sections (BLAS-1 family, reduction family) + Referenced-from + Evidence.
- `book/src/L0/ksp-factory-file.md` — file overview; At-a-glance + thematic sub-sections (the enum dispatch, the implemented branches, the advertised-but-unimplemented pattern) + Referenced-from + Evidence.

**Source files anchored:**
- `palace/linalg/operator.hpp` (407 lines) — read lines 1-120 and 120-240 to confirm the `ComplexOperator` overload set and the concrete-subclass family hierarchy. Citations target lines 21, 24-68, 36-39, 73-113, 116-136, 140-176, 178-226, 202-206 (load-bearing), 228-229, 232-291, 298-367.
- `palace/linalg/operator.cpp` (698 lines) — read lines 420-510 to confirm the `SumOperator::Mult` / `AddMult` and `BaseDiagonalOperator<...>::Mult` bodies cited at lines 428-441, 458-466, 478-507.
- `palace/linalg/rap.cpp` (882 lines, sampled) — grep-verified `ParOperator::Mult` at line 195, `ParOperator::MultTranspose` at line 236, `ComplexParOperator::Mult` at line 481.
- `palace/linalg/ksp.hpp` (79 lines) — full file read; all `BaseKspSolver` citations target lines 29-72 with sub-line specifics (32-34, 36-37, 41-42, 46, 49, 52-58, 60-61, 64-67, 69, 71, 74-75).
- `palace/linalg/ksp.cpp` (315 lines) — full file read; `BaseKspSolver` definitions target lines 244-255, 257-263, 265-274 (load-bearing 272), 276-294 (multigrid special case 283-288), 296-310, 312-313.
- `palace/linalg/iterative.hpp` (279 lines) — full file read; `IterativeSolver<OperType>` base class at lines 25-115 cited for the `A`, `B`, tolerance / iteration state surface.
- `palace/linalg/iterative.cpp` (882 lines, sampled) — read lines 280-360 and 340-460 to confirm `ApplyB` / `ApplyBA` helpers (used in the "Composition wiring" prose) and the `CgSolver<OperType>::Mult` body (used for the "the iterative solver's per-step `ApplyB` routes to the preconditioner" claim).
- `palace/linalg/solver.hpp` (138 lines) — full file read; `Solver<OperType>` base at lines 21-65 cited.

**Cross-references into existing artifact:**
- `book/src/L1/apply_linop.md` (firm at L1, cycle-004) — reviewed in full; the new `apply-linop-overload-set.md` chapter is the explicit L0 anchor that L1/apply_linop's Context section and Evidence section currently cite inline. The retroactive-thinning sweep (priority #11) will replace those inline citations with backlinks.
- `book/src/L1-L0/apply-linop-mutation-rotation.md` (theme, cycle-005) — touches the same overload-set surface from the mutation-rotation angle; the new chapter is its evidence-walk target.
- `book/src/L2/krylov-step.md` (firm at L2, cycle-005) — referenced in the kspsolver chapter as the per-step body the iterative-solver `Mult` invokes.
- `book/src/concepts/solver-as-operator.md` — referenced in the kspsolver chapter for the "solver is-a operator under `A → A⁻¹`" identification.
- `book/src/concepts/solve-monad.md` — referenced in the kspsolver chapter as the L4 abstraction over the construction-then-apply flow.
- `book/src/L0/ksp-factory-file.md` (bundle 1) — the new kspsolver chapter complements it: the factory file covers the *construction* path (which iterative solver + which preconditioner gets built); the new chapter covers the *composition class* that holds them.

**Cycle-006 planner guidance followed:**
- Per planner's §Open questions / caveats item 3: "prioritize `apply_linop` and `kspsolver-base-class` (two medium-scope chapters) to maintain momentum and unblock future L1>L0 audits. Defer the broad file-overview sweep to a future cycle if time permits." → Bundle 2 ships exactly these two; no broad file-overview sweep attempted.
- Per role-spec sizing guidance: 2 chapters (within the 3-chapter cap per the dispatch directive). No deferral needed; both candidates fit comfortably within the bundle-2 budget.

## Skills invoked

*Telemetry note added by repairer (cycle-006 critic skill-uptake-survey warning). The producing layer-intro-author dispatch performed the following skill-shaped procedures without explicit naming; recorded here for skill-uptake telemetry:*

- **`verify-citation-range`** — performed informally on the ~35 cited line ranges. The agent's Open Question #2 describes the procedure: "grep-verified the function signatures exist at the cited start-lines but did not read every line." Load-bearing citations (`ksp.cpp:272`, `operator.hpp:202-206`, `solver.hpp:22`, `ksp.cpp:296-310`) were read in full; surrounding-context citations were grep-verified at start-lines. One inexactness surfaced in critique (`operator.cpp:478-503` truncated to function signatures only; widened to `:478-507` in repair).
- **`summary-md-surgical-insert`** — implicitly performed for the two new SUMMARY.md entries appended after the existing `ksp-factory-file` line under the L0 Part. Edit is mechanical (two appended bullets at the end of the L0 section); no SUMMARY.md restructuring.

No skills explicitly invoked in the producing dispatch; both candidate skills exist in `skills/` and were performed in spirit.

## Open questions / caveats

1. **`apply-linop-overload-set` chapter slug naming.** I chose `apply-linop-overload-set` to match the planner's verbatim slug (`apply_linop` overload-set). Alternative names considered: `operator-mult-family` (clearer about the C++ scope but loses the L1-operator association) or `mult-overload-set` (terser but ambiguous — `Mult` is generic). Decision: planner's slug wins; the prose makes the alias clear in the first paragraph ("the L0 home of operator application"). No promotion needed.

2. **The chapter cites lines I didn't read in full.** Specifically `palace/linalg/rap.cpp:236-275` (ParOperator::MultTranspose) and `palace/linalg/operator.cpp:478-503` (BaseDiagonalOperator template specialisations). I grep-verified the function signatures exist at the cited start-lines but did not read every line. For the L0 reference-note discipline (2-4 paragraphs of interpretation + representative citations, no line-by-line transcription) this is sufficient — the citations point at function bodies whose presence is established. If a future cross-layer-cross-cutter or lowering-verifier audits these citations, they would need to re-read the bodies in full; the chapter does not make line-specific claims about their contents beyond what the function signatures establish (e.g., "the transpose form swaps prolongation/restriction roles" is a one-line interpretive claim, not a line-by-line transcription).

3. **`kspsolver-base-class.md` mentions `MfemWrapperSolver` as "another Solver<OperType> subclass" in the Notes section but does not cite it heavily.** `MfemWrapperSolver` is in `palace/linalg/solver.hpp:70-134` — declared but I haven't characterised it in depth. If a future bundle-3 candidate wants to cover the preconditioner-side construction surface (currently spread across `palace/linalg/{amg,ams,jacobi,mumps,strumpack,superlu,gmg}.{hpp,cpp}` and routed through `MfemWrapperSolver`), `MfemWrapperSolver` would naturally anchor it. Logged as a forward-note, not a deferral — bundle 2 is self-contained.

4. **The L1 `ksp_solve` operator is referenced as "forthcoming firm-up" in `kspsolver-base-class.md`'s "Referenced from" block.** This operator does not currently exist in `book/src/L1/` — only the concept page at `book/src/concepts/ksp_solve.md` exists. The forward-reference is sound (the L0 chapter anchors a future L1 entry), but bundles 3+ may want to surface this as a harvester-target priority candidate. Logged as a forward-note for cycle-006 integrator-finalize's Next-cycle-priorities / integrator-signals append.

5. **The "Composition wiring" section in `kspsolver-base-class.md` references `iterative.cpp:389` (CG ApplyB) and `iterative.cpp:627` (GMRES ApplyBA) as examples of the per-step preconditioner-apply.** These are correct call-site citations (verified by grep at lines 389 and 627 — `ApplyB(B, r, z, this->use_timer);` and `ApplyBA(pc_side, A, B, V[j], w, r, this->use_timer);` respectively). The interpretive prose ("the iterative solver's per-step `ApplyB` routes to the preconditioner's `Mult`") is one inferential step above the citation; this is within the L0 reference-note discipline (interpretation, not transcription).

6. **No `Referenced from:` backlinks updated on L1 / L2 / L4 pages yet.** Per the L0 reference-note discipline, the forward-declared `Referenced from:` blocks in the new chapters point at L1/apply_linop, L1-L0/apply-linop-mutation-rotation, L2/krylov-step, etc. — but those upstream pages do not yet have *backlinks* to the new L0 chapters. This is intentional and consistent with bundle 1 (the bundle-1 chapters all carry forward-declared `Referenced from:` blocks awaiting the retroactive-thinning sweep at priority #11). When ≥6 chapters land (we are now at 8 total: 6 from bundle 1 + 2 from bundle 2), priority #11 unblocks and a future cycle's `layer-intro-author` retroactively thins the L1 entries to use the L0 backlinks.

7. **Chapter ordering in `SUMMARY.md` introduces a third grouping ("Overload sets and class interfaces") under L0.** Bundle 1 organised L0 into "Conventions" and "File overviews". The new chapters don't fit cleanly into either — `apply-linop-overload-set.md` is a multi-overload / multi-subclass surface, not a single file or a convention; `kspsolver-base-class.md` is a class-interface deep-dive, not a file overview. I introduced the third grouping in `L0/index.md` rather than force-fitting. This is consistent with the role-spec discipline "When you encounter operators that don't fit cleanly under any layer-level semantic theme, **flag them**; don't force-fit." Flagged here for cycle-006 critic / repairer; alternative would be to extend "File overviews" to "File overviews / overload sets" (less crisp) or fold both into "Conventions" (semantically wrong — these are surface descriptions, not idiom conventions).
