# File — `palace/linalg/solver.{hpp,cpp}`

A reference note for L1 / L2 / L4 entries that touch Palace's solver class hierarchy. `palace/linalg/solver.hpp` (138 lines) plus `palace/linalg/solver.cpp` (209 lines) is the **type-axis root** of every Palace solver — preconditioner, iterative, or MFEM-wrapped — through its templated abstract base `Solver<OperType>`. The file declares two classes: `Solver<OperType>` (the abstract base) and `MfemWrapperSolver<OperType>` (the only concrete subclass declared here; covered in depth at [`mfem-wrapper-solver`](./mfem-wrapper-solver.md)). Every other concrete subclass — iterative solvers, smoothers, multigrid containers, block preconditioners — lives in a sibling file and inherits from this `Solver<OperType>` base.

The file is the L0 anchor for the L4 [`solver-as-operator`](../concepts/solver-as-operator.md) concept (Palace's `Solver<OperType>` *is-an* `OperType`, so a solver value behaves as a linear operator at the type level) and for the future `L1/apply_preconditioner` operator (uniform across all eight subclass families through the shared `Mult` interface).

## At a glance

The header (`palace/linalg/solver.hpp:1-138`) declares two classes inside `namespace palace`:

- **`Solver<OperType>`** (lines 21-65) — abstract base; templated on `OperType ∈ {Operator, ComplexOperator}`. **Inherits from `OperType`**, so `Solver<Operator>` *is-an* `Operator` and `Solver<ComplexOperator>` *is-an* `ComplexOperator`. The shape that makes a Palace solver value structurally identical to a linear operator value — the `Mult(x, y)` entry point is inherited from `OperType` and overridden by each concrete subclass.
- **`MfemWrapperSolver<OperType>`** (lines 70-134) — concrete adapter wrapping a `std::unique_ptr<mfem::Solver>` to lift MFEM's real-only solver hierarchy into Palace's templated one. Detailed companion chapter: [`mfem-wrapper-solver`](./mfem-wrapper-solver.md).

The source file (`palace/linalg/solver.cpp:1-209`) defines only the `MfemWrapperSolver` method bodies (the `Solver<OperType>` base class is fully inline / `MFEM_ABORT`-defaulted in the header). Five definitions:

- `MfemWrapperSolver<Operator>::SetOperator` (lines 12-30) — real specialisation.
- `MfemWrapperSolver<ComplexOperator>::SetOperator` (lines 32-136) — complex specialisation with the equivalent-real `2×2` block formulation.
- `MfemWrapperSolver<Operator>::Mult` (lines 138-142) — real specialisation (one-liner forwarding).
- `MfemWrapperSolver<ComplexOperator>::Mult` (lines 144-177) — complex specialisation with the `ArrayMult` fast path and the augmented `2N`-vector path with imaginary-part sign-flip.
- `MfemWrapperSolver<OperType>::DropSmallEntries` (lines 179-207) — the single generic template definition (vs the per-`OperType` specialisations of `SetOperator` and `Mult` above); threshold at `ε²` with MUMPS reorder-reuse interaction.

## `Solver<OperType>` — the abstract base

Declared at `palace/linalg/solver.hpp:21-65`. The class body is small (≈40 lines) and contains:

- **`static_assert`** (lines 24-26) constraining `OperType` to `Operator` or `ComplexOperator` — the same template-parameter constraint as `BaseKspSolver` ([`kspsolver-base-class`](./kspsolver-base-class.md)) and `IterativeSolver` ([`linalg-iterative-file`](./linalg-iterative-file.md)).
- **`using VecType = typename std::conditional<...>::type`** (lines 29-30) — protected type alias resolving to `ComplexVector` for complex, `Vector` for real. The same `std::conditional` pattern as `BaseProductOperator` and the iterative-solver hierarchy; it propagates downward to every subclass via `using VecType = typename Solver<OperType>::VecType;` (see e.g. `jacobi.hpp:21`, `chebyshev.hpp:25`, `iterative.hpp:122`, `blockprecond.hpp:34`).
- **`bool initial_guess`** (line 33) — single piece of subclass-relevant state; whether the second `Mult` argument is to be read as an initial guess (rather than overwritten). Default-false; subclasses opt in via the constructor or `SetInitialGuess`.
- **Constructor + virtual destructor** (lines 36-37).
- **`SetInitialGuess`** (line 40) — virtual setter for the initial-guess flag; `MfemWrapperSolver` overrides it to also set `pc->iterative_mode` (line 125).
- **`SetOperator(const OperType &op)`** (line 43) — pure virtual; every concrete subclass implements this to bind a system operator.
- **`MultTranspose`** (lines 46-49) — overridden from `OperType` with an `MFEM_ABORT` body. Concrete subclasses opt in by re-overriding; the base contract is "transpose not implemented".
- **`Mult2(x, y, r)`** and **`MultTranspose2(x, y, r)`** (lines 52-64) — virtual entry points with a pre-allocated temporary storage vector `r`. Both default to `MFEM_ABORT`; the temporary-storage form is intended for hot-path consumers that want to avoid the per-call workspace allocation in the iterative-solver subclasses. Not currently used outside the immediate hierarchy; harvested when L1 reaches `apply_preconditioner`.

The base class does NOT declare `Mult` itself — `Mult(x, y)` is inherited (pure-virtual) from `OperType`. This is the load-bearing design choice: a `Solver<OperType>` IS-AN `OperType`, so passing a solver where an operator is expected (e.g., as the system operator of an outer iterative solve, in shift-and-invert eigensolvers, or as a preconditioner held by `BaseKspSolver`) requires no adapter. The L4 [`solver-as-operator`](../concepts/solver-as-operator.md) concept names this identification at the methodology level.

## `MfemWrapperSolver<OperType>` — the in-file concrete subclass

Declared at `palace/linalg/solver.hpp:70-134`. The full coverage is in [`mfem-wrapper-solver`](./mfem-wrapper-solver.md); here we record only what makes this class the **canonical place to point** for "where does `Solver<OperType>` get instantiated":

- It is **the only concrete subclass declared in `solver.{hpp,cpp}` itself**. The other seven subclass families (`IterativeSolver`+`CgSolver`/`GmresSolver`/`FgmresSolver`, `JacobiSmoother`, `ChebyshevSmoother`/`ChebyshevSmoother1stKind`, `DistRelaxationSmoother`, `GeometricMultigridSolver`, `BlockDiagonalPreconditioner`) each live in their own file.
- It is the **adapter for MFEM solvers** — `BoomerAMG`, `AMS`, MUMPS, SuperLU, Strumpack all enter Palace through this wrapper. The wrapper carries both an owning `std::unique_ptr<mfem::Solver> pc` (line 77) and an optional owning assembled-matrix `std::unique_ptr<mfem::HypreParMatrix> A` (line 80) preserved across `SetOperator` / `Mult` calls when `save_assembled = true`.
- It hosts the only **single generic template method definition** in `solver.cpp` (vs the per-`OperType` template specialisations of `SetOperator` and `Mult`): `DropSmallEntries` (lines 179-207) — a `ε²`-threshold sparsity-pattern post-process that interacts load-bearingly with MUMPS reorder-reuse.

## The eight `Solver<OperType>` subclass families

For navigation purposes, every concrete subclass of `Solver<OperType>` Palace ships, with its declaring file and the cohort it belongs to:

```text
Solver<OperType>             (palace/linalg/solver.hpp:21-65)
  |
  +-- MfemWrapperSolver<OperType>      (palace/linalg/solver.hpp:70-134)
  |   [the in-file concrete subclass]
  |
  +-- IterativeSolver<OperType>        (palace/linalg/iterative.hpp:25-115)
  |     +-- CgSolver<OperType>         (palace/linalg/iterative.hpp:119-150)
  |     +-- GmresSolver<OperType>      (palace/linalg/iterative.hpp:155-217)
  |           +-- FgmresSolver<OperType>  (palace/linalg/iterative.hpp:222-275)
  |   [iterative cohort; see linalg-iterative-file]
  |
  +-- JacobiSmoother<OperType>         (palace/linalg/jacobi.hpp:19-...)
  +-- ChebyshevSmoother<OperType>      (palace/linalg/chebyshev.hpp:23-...)
  +-- ChebyshevSmoother1stKind<OperType>  (palace/linalg/chebyshev.hpp:86-...)
  +-- DistRelaxationSmoother<OperType> (palace/linalg/distrelaxation.hpp:30-...)
  |   [native-smoother cohort; see preconditioner-classes-overview]
  |
  +-- GeometricMultigridSolver<OperType>  (palace/linalg/gmg.hpp:31-...)
  +-- BlockDiagonalPreconditioner<OperType> (palace/linalg/blockprecond.hpp:32-...)
      [composition-preconditioner cohort; see preconditioner-classes-overview]
```

Eight concrete subclass templates × two `OperType` instantiations = **sixteen concrete classes** total reachable from `Solver<OperType>`. (Three of the eight are further specialised — `CgSolver` and `GmresSolver` from `IterativeSolver`; `FgmresSolver` from `GmresSolver` — adding three more concrete classes per `OperType`.)

The shared shape across all subclasses:

- Templated on `OperType`; static-asserted to `Operator` or `ComplexOperator`.
- Inherits from `Solver<OperType>` (or transitively, via `IterativeSolver<OperType>` / `GmresSolver<OperType>`).
- Carries some configuration state + a workspace pattern (lazy-allocate-on-`SetOperator`-or-`Mult`).
- Implements `Mult(x, y) const` with `mutable` workspace allocation per [`mutable-workspace-pattern`](./mutable-workspace-pattern.md).
- Implements `SetOperator(const OperType &op)` — the pure-virtual contract from the base.

## What's **not** here

The closely-related composition class `BaseKspSolver<OperType>` ([`kspsolver-base-class`](./kspsolver-base-class.md)) lives in `palace/linalg/ksp.{hpp,cpp}` — **not** in `solver.{hpp,cpp}`. `BaseKspSolver` is a peer composition that holds **one** `std::unique_ptr<IterativeSolver<OperType>> ksp` and **one** `std::unique_ptr<Solver<OperType>> pc` (`ksp.hpp:41-42`); it is **not** a `Solver<OperType>` itself (because it's the composition, not the individual). The factory functions that construct `Solver<OperType>` instances (`ConfigureKrylovSolver`, `ConfigurePreconditionerSolver`, `MakeWrapperSolver`) all live in `ksp.cpp` ([`ksp-factory-file`](./ksp-factory-file.md)), not in `solver.cpp`.

The MFEM-side direct solvers (`mfem::MUMPSSolver`, `mfem::SuperLUSolver`, `palace::StrumpackSolver`, `palace::StrumpackMixedPrecisionSolver`) are real-only `mfem::Solver` subclasses; they enter the Palace hierarchy through `MfemWrapperSolver`, not by inheriting from `Solver<OperType>` directly. There is no Palace-side dedicated "direct solver" subclass of `Solver<OperType>`; the direct-vs-iterative split happens one level higher (consumer side: whether the `Solver<OperType>` is given to `BaseKspSolver` as a preconditioner, or used standalone).

## Notes for higher layers

- **`Solver<OperType>` is the type-level realisation of the [`solver-as-operator`](../concepts/solver-as-operator.md) concept.** The `: public OperType` inheritance is the load-bearing line — once a `Solver<OperType>` instance exists, it can be passed wherever an `OperType` is expected without adaptation. This is what lets shift-and-invert eigensolvers consume a Palace KSP solver as their "apply-inverse" operator: the solver value is structurally an operator value.
- **The `OperType` template axis collapses at L1.** The element-type axis from [`mfem-vector-types`](./mfem-vector-types.md) (real / complex) is encoded as the `OperType` template parameter at L0; at L1 the operator-and-solver values are uniform (the element-type axis is a variant on the value-of-the-solver, not on the solver-class). The 16 concrete classes collapse to **eight L1 solver families** (one per subclass template), each with an element-type variant axis.
- **The `Mult2` / `MultTranspose2` "with-preallocated-temporary" virtuals** (lines 52-64) are an L0-specific hot-path optimisation that bypasses the workspace allocation inside the `Mult` body. They abort by default at the base level; concrete subclasses opt in. At L1 these collapse to the same operator as `Mult` — workspace allocation is L0-internal per the [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) erasure rule.
- **The `initial_guess` flag is a state-not-input concern.** At L0 it's a `bool` member; the second argument to `Mult` is interpreted differently based on its value. At L1 this would lift as a variant axis on the solver value (or as an extra input argument to the lifted `solve` function); the obvious L1 form is `ksp_solve :: Solver -> Vector -> Maybe Vector -> Vector` with the optional initial guess. See the `L1/ksp_solve` rough-in note (cycle-007+).
- **There is no `MultHermitianTranspose` declared on `Solver<OperType>`** — only `MultTranspose` and the `Mult2` / `MultTranspose2` variants. The Hermitian-transpose entry point (declared on `ComplexOperator` per [`apply-linop-overload-set`](./apply-linop-overload-set.md)) is therefore inherited at the `OperType` level by `Solver<ComplexOperator>` but not surfaced at the `Solver<OperType>` API. Iterative solvers do not implement Hermitian-transpose solves; only `Solver<OperType>` consumers that pass a transposed operator at construction.

## Referenced from

*Forward-declared. The L1 `ksp_solve` operator (queued cycle-007+) and the L1 `apply_preconditioner` operator (queued post-bundle-6) will reference this chapter when they reach the `Solver<OperType>` type-axis discussion.*

- [`L0/mfem-wrapper-solver`](./mfem-wrapper-solver.md) — the in-file concrete subclass detail.
- [`L0/kspsolver-base-class`](./kspsolver-base-class.md) — sibling chapter; the composition class that holds a `Solver<OperType>` as its preconditioner field.
- [`L0/linalg-iterative-file`](./linalg-iterative-file.md) — the iterative-solver cohort of `Solver<OperType>` subclasses (`IterativeSolver` + `CgSolver` + `GmresSolver` + `FgmresSolver`).
- [`L0/preconditioner-classes-overview`](./preconditioner-classes-overview.md) — the preconditioner-side cohort of `Solver<OperType>` subclasses (`JacobiSmoother`, `ChebyshevSmoother`, `DistRelaxationSmoother`, `GeometricMultigridSolver`, `BlockDiagonalPreconditioner`, plus the Hypre-wrapped algebraic preconditioners that route through `MfemWrapperSolver`).
- [`L0/ksp-factory-file`](./ksp-factory-file.md) — the factory file that constructs concrete `Solver<OperType>` instances via `ConfigureKrylovSolver` / `ConfigurePreconditionerSolver` / `MakeWrapperSolver`.
- [`L0/apply-linop-overload-set`](./apply-linop-overload-set.md) — the method-overload set inherited via `OperType` (the parent class of `Solver<OperType>`).
- [`L0/mutable-workspace-pattern`](./mutable-workspace-pattern.md) — the workspace-allocation pattern shared by every concrete `Solver<OperType>` subclass.
- [`concepts/solver-as-operator`](../concepts/solver-as-operator.md) — the L4 methodology concept that `Solver<OperType>`'s `: public OperType` inheritance realises at the type level.

## Evidence (representative)

- `palace/linalg/solver.hpp:1-138` — the header file (138 lines).
- `palace/linalg/solver.hpp:12-13` — `namespace palace` open.
- `palace/linalg/solver.hpp:15-18` — comment block: "The base Solver<OperType> class is a templated version of mfem::Solver for operation with real- or complex-valued operators."
- `palace/linalg/solver.hpp:21-22` — `template <typename OperType> class Solver : public OperType` declaration.
- `palace/linalg/solver.hpp:24-26` — `static_assert` constraint on `OperType`.
- `palace/linalg/solver.hpp:29-30` — `using VecType = typename std::conditional<...>::type` element-type axis collapse.
- `palace/linalg/solver.hpp:33` — `bool initial_guess` member.
- `palace/linalg/solver.hpp:36-37` — constructor + virtual destructor.
- `palace/linalg/solver.hpp:40` — `virtual void SetInitialGuess(bool guess)`.
- `palace/linalg/solver.hpp:43` — `virtual void SetOperator(const OperType &op) = 0;` (pure virtual contract).
- `palace/linalg/solver.hpp:46-49` — `MultTranspose` `MFEM_ABORT` base implementation.
- `palace/linalg/solver.hpp:52-56` — `Mult2(x, y, r)` virtual with `MFEM_ABORT` body.
- `palace/linalg/solver.hpp:60-64` — `MultTranspose2(x, y, r)` virtual with `MFEM_ABORT` body.
- `palace/linalg/solver.hpp:67-69` — comment block introducing `MfemWrapperSolver` ("This solver wraps a real-valued mfem::Solver for application to complex-valued problems...").
- `palace/linalg/solver.hpp:70-71` — `template <typename OperType> class MfemWrapperSolver : public Solver<OperType>`.
- `palace/linalg/solver.hpp:73` — `using VecType = typename Solver<OperType>::VecType;` (propagation pattern).
- `palace/linalg/solver.hpp:77` — owned `std::unique_ptr<mfem::Solver> pc`.
- `palace/linalg/solver.hpp:80` — owned `std::unique_ptr<mfem::HypreParMatrix> A`.
- `palace/linalg/solver.hpp:84-94` — configuration flags: `save_assembled` (84), `complex_matrix` (88), `drop_small_entries` (91), `reorder_reuse` (94).
- `palace/linalg/solver.hpp:97` — `int num_dropped_entries = 0;` (MUMPS reorder-reuse pattern-change counter).
- `palace/linalg/solver.hpp:100` — `void DropSmallEntries();` declaration.
- `palace/linalg/solver.hpp:103-110` — constructor: `MfemWrapperSolver(std::unique_ptr<mfem::Solver> &&pc, bool save_assembled = true, bool complex_matrix = true, bool drop_small_entries = true, bool reorder_reuse = true)`.
- `palace/linalg/solver.hpp:113` — `const mfem::Solver &GetSolver() { return *pc; }` accessor.
- `palace/linalg/solver.hpp:116-123` — three setter methods: `SetSaveAssembled`, `SetDropSmallEntries`, `SetComplexMatrix`.
- `palace/linalg/solver.hpp:125-129` — `SetInitialGuess` override (forwards to `pc->iterative_mode`).
- `palace/linalg/solver.hpp:131` — `void SetOperator(const OperType &op) override;` (definition in `.cpp`).
- `palace/linalg/solver.hpp:133` — `void Mult(const VecType &x, VecType &y) const override;` (definition in `.cpp`).
- `palace/linalg/solver.cpp:1-209` — the source file (209 lines).
- `palace/linalg/solver.cpp:12-30` — `MfemWrapperSolver<Operator>::SetOperator` real-branch definition.
- `palace/linalg/solver.cpp:32-136` — `MfemWrapperSolver<ComplexOperator>::SetOperator` complex-branch definition.
- `palace/linalg/solver.cpp:56-72` — the equivalent-real block-matrix construction (`A = [Ar, Ai; Ai, -Ar]` via `HypreParMatrixFromBlocks`).
- `palace/linalg/solver.cpp:73-77` — the real-part approximation construction (`A = Ar + Ai` via `mfem::Add`).
- `palace/linalg/solver.cpp:138-142` — `MfemWrapperSolver<Operator>::Mult` real-branch one-liner.
- `palace/linalg/solver.cpp:144-177` — `MfemWrapperSolver<ComplexOperator>::Mult` complex-branch (two paths: `ArrayMult` fast path at 148-157, augmented `2N`-vector path at 158-177 with imaginary-part sign-flip at line 173).
- `palace/linalg/solver.cpp:179-207` — `MfemWrapperSolver<OperType>::DropSmallEntries`; threshold `ε²` at line 183; MUMPS `reorder_reuse` interaction at lines 186-202.
- `palace/linalg/iterative.hpp:26` — `class IterativeSolver : public Solver<OperType>` (the iterative-cohort subclass anchor).
- `palace/linalg/jacobi.hpp:19` — `class JacobiSmoother : public Solver<OperType>`.
- `palace/linalg/chebyshev.hpp:23` — `class ChebyshevSmoother : public Solver<OperType>`.
- `palace/linalg/chebyshev.hpp:86` — `class ChebyshevSmoother1stKind : public Solver<OperType>`.
- `palace/linalg/distrelaxation.hpp:30` — `class DistRelaxationSmoother : public Solver<OperType>`.
- `palace/linalg/gmg.hpp:31` — `class GeometricMultigridSolver : public Solver<OperType>`.
- `palace/linalg/blockprecond.hpp:32` — `class BlockDiagonalPreconditioner : public Solver<OperType>`.
- `palace/linalg/ksp.hpp:42` — `std::unique_ptr<Solver<OperType>> pc;` (the preconditioner field of `BaseKspSolver`; the type-axis sink of the eight subclass families).
