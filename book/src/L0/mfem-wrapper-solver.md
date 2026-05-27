# Class — `MfemWrapperSolver<OperType>`

A reference note for L1 / L4 entries that touch Palace's preconditioner-side construction surface. `MfemWrapperSolver<OperType>` is the adapter that lifts MFEM's real-only `mfem::Solver` hierarchy into Palace's templated `Solver<OperType>` hierarchy (where `OperType ∈ {Operator, ComplexOperator}`). Every preconditioner Palace uses — `BoomerAMG`, `AMS`, `MUMPS`, `SuperLU`, `Strumpack` — comes through this wrapper before being handed to a `BaseKspSolver` for composition.

## At a glance

Two abstract layers sit between MFEM and the iterative-solver consumers:

- `palace::Solver<OperType>` (`palace/linalg/solver.hpp:21-65`) — abstract base templated on `OperType`. Inherits from `OperType` (so `Solver<Operator>` is-an `Operator`, and `Solver<ComplexOperator>` is-an `ComplexOperator`). Declares the abstract `SetOperator(const OperType &op)` and inherits a pure-virtual `Mult` from `OperType`. The composition target of [`BaseKspSolver`](./kspsolver-base-class.md) (the `pc` field).
- `palace::MfemWrapperSolver<OperType>` (`palace/linalg/solver.hpp:70-134`) — concrete adapter wrapping a `std::unique_ptr<mfem::Solver>` and routing `Mult` and `SetOperator` through it after `OperType`-aware adaptation (real direct, or complex via the equivalent-real block formulation).

The wrapper has four template-specialised method bodies in `palace/linalg/solver.cpp` (two `SetOperator` specialisations + two `Mult` specialisations); the rest is inline in `solver.hpp`.

## The real specialisation

The real-branch `MfemWrapperSolver<Operator>::SetOperator` (`solver.cpp:12-30`) is short: dynamic-cast the incoming `Operator` to `mfem::HypreParMatrix` (the assembled-sparse form) or to `palace::ParOperator` (which can produce a `HypreParMatrix` via `ParallelAssemble` / `StealParallelAssemble`), then call `pc->SetOperator(*hA)` on the wrapped `mfem::Solver`. The corresponding `Mult` specialisation (`solver.cpp:138-142`) is a one-liner:

```cpp
template <>
void MfemWrapperSolver<Operator>::Mult(const Vector &x, Vector &y) const
{
  pc->Mult(x, y);
}
```

Pure forwarding. The real-branch wrapping has zero algebraic content — the only purpose is to wear the `Solver<Operator>` type so the wrapped MFEM solver can compose into `BaseKspSolver<Operator>` (which expects a `Solver<Operator> *` as its preconditioner field).

## The complex specialisation

The complex-branch is where the wrapper earns its name. `mfem::Solver` is fundamentally real-only — it has no notion of `std::complex<double>` element type. The complex specialisation (`solver.cpp:33-136`) bridges this gap in two distinct ways selected by the `complex_matrix` flag (`solver.hpp:88`):

- **Equivalent-real block formulation** (`complex_matrix = true`, the default; `solver.cpp:54-74`) — assembles a `2×2` `HypreParMatrix` block:

  ```text
  A = [ Ar   Ai ]
      [ Ai  -Ar ]
  ```

  This is the "augmented system" form. The wrapped MFEM solver solves `A · [xr; -xi] = [br; bi]` over real arithmetic; the complex `Mult` specialisation post-processes the block-vector result. The construction goes through `mfem::HypreParMatrixFromBlocks` (`solver.cpp:71`).

- **Real-part approximation** (`complex_matrix = false`; `solver.cpp:74-77`) — assembles `A = Ar + Ai` and ignores the complex structure entirely. The preconditioner is built against this real sum; it's an approximation that's faster to construct but algebraically distinct from the exact equivalent-real form.

Either way, the resulting `A` is then forwarded to `pc->SetOperator(*A)` (`solver.cpp:90, 102, 119`) and the wrapped MFEM solver becomes a real-arithmetic preconditioner for a complex-system iterative solve.

The complex `Mult` specialisation (`solver.cpp:144-177`) has two branches keyed on whether `pc->Height() == x.Size()` (an MFEM `ArrayMult`-shaped solver that operates on `(real, imag)` arrays directly — the fast path at lines 148-157) or the augmented `2N`-sized block-vector form (lines 158-176, which packs `[xr, xi]` into a single `2N` vector, calls the real solver, splits the result, and **negates the imaginary part** at line 173 to undo the augmented-system sign convention).

## The `DropSmallEntries` optimisation

`DropSmallEntries` (`solver.cpp:179-207`) is a per-`SetOperator` post-processing pass that zeroes entries of the assembled matrix smaller than `ε²` (machine-epsilon squared, line 183). The motivation is symbolic: many preconditioners (especially direct-solver MUMPS / SuperLU / Strumpack) have factorisation cost proportional to the sparsity-pattern density, and fill-in tends to be dominated by entries that are numerically negligible.

The pass is configured by the `drop_small_entries` flag (default `true`, `solver.hpp:91`). When MUMPS is the wrapped solver, an additional `reorder_reuse` interaction (`solver.cpp:185-202`) decides whether MUMPS can keep its previous column-reordering across solves — only if the symmetric sparsity pattern didn't change. This is the load-bearing reason the wrapper tracks `num_dropped_entries` as state: to detect pattern changes between consecutive `SetOperator` calls.

`DropSmallEntries` is a transparent performance optimisation — at L1 it disappears (the matrix is unchanged modulo sub-`ε²` perturbations). The L1>L0 lowering theme for `MfemWrapperSolver`-routed preconditioners would record it as a one-line note alongside the wrapping.

## Where `MfemWrapperSolver` is used

A full grep of `reference/palace/` (`std::make_unique<MfemWrapperSolver<...>>` over `palace/`) finds eleven construction sites:

- `palace/linalg/ksp.cpp:120` — inside `MakeWrapperSolver`, the template helper that constructs the preconditioner objects routed through `ConfigurePreconditionerSolver` (the KSP factory; see [`ksp-factory-file`](./ksp-factory-file.md)). This is the central call site — every preconditioner Palace's `BaseKspSolver` uses flows through this line.
- `palace/linalg/divfree.cpp:120` — divergence-free projection's inner AMG preconditioner.
- `palace/linalg/hcurl.cpp:92` — H(curl) auxiliary-space preconditioner (AMS).
- `palace/linalg/errorestimator.cpp:88, 94` — flux-recovery error estimator's inner solver.
- `palace/models/modeeigensolver.cpp:666, 733, 742, 749, 761, 774` — six call sites in the eigenmode pipeline for various shift-and-invert preconditioner constructions.

The wrapper is therefore the **uniform L0 hand-off point** between MFEM-side direct/algebraic solvers and Palace-side iterative composition. Three distinct preconditioner-class hierarchies bottom out through it:

- **Direct sparse solvers** — `mfem::MUMPSSolver`, `mfem::SuperLUSolver`, `palace::StrumpackSolver`, `palace::StrumpackMixedPrecisionSolver` (all subclasses of `mfem::Solver`). These do exact LU/QR factorisation of the assembled matrix.
- **Algebraic multigrid** — `mfem::HypreBoomerAMG`, `palace::HypreAmsSolver` (BoomerAMG and AMS, both subclasses of `mfem::HypreSolver` which subclasses `mfem::Solver`).
- **Simple iterative** — `mfem::HypreSmoother` and the Jacobi family.

All collapse to "a `Solver<OperType>` instance" at the [`BaseKspSolver`](./kspsolver-base-class.md) level; the wrapper makes them all type-compatible regardless of MFEM's real-only convention.

## Notes for higher layers

- **The wrapper is a concrete subclass of `Solver<OperType>`** alongside [`BaseKspSolver`](./kspsolver-base-class.md) (which is itself **not** a `Solver<OperType>` but a composition class — distinct role). `MfemWrapperSolver` is the "wrap an MFEM solver" subclass; sibling subclasses include the iterative solvers `CgSolver` / `GmresSolver` / `FgmresSolver` (which inherit through `IterativeSolver<OperType>`, see [`linalg-iterative-file`](./linalg-iterative-file.md)).
- **The complex specialisation is the load-bearing one** — it implements the equivalent-real block formulation `A = [Ar, Ai; Ai, -Ar]` that lets a real preconditioner be used for a complex system. This is the L0 substrate for the L4 [`complex-from-real-lift`](../concepts/complex-from-real-lift.md) concept on the preconditioner side; [`apply-linop-overload-set`](./apply-linop-overload-set.md) covers the operator-side wrapping pattern (`ComplexWrapperOperator`). Together they make complex-system preconditioning expressible as a layered real solve.
- **`DropSmallEntries` is the only non-trivial transformation** — it modifies the assembled matrix by zeroing sub-`ε²` entries. Classified as transparent per [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md); at L1 the preconditioner is the un-modified one. The MUMPS `reorder_reuse` interaction (preserve column ordering when sparsity pattern is unchanged) is a transparent performance trick on top of a transparent transformation; both fold out at L1.
- **The L1 view of preconditioner application** collapses `MfemWrapperSolver::Mult(b, x)` to a function-shaped `pc_apply :: (Solver, Vector) → Vector` (`x = pc(b)`). The wrapping disappears; the equivalent-real block formulation appears at L1 only as "the preconditioner is constructed from real parts of a complex operator" — a construction note on the L1 `Solver` value, not a runtime operation.

## Referenced from

*Forward-declared. The L1 `pc_apply` / `solver-as-operator` story and the future L4>L1 `complex-from-real-lift` lowering will reference this chapter.*

- [`L0/kspsolver-base-class`](./kspsolver-base-class.md) — the composition class that holds an `MfemWrapperSolver` (or another `Solver<OperType>` subclass) as its `pc` field.
- [`L0/ksp-factory-file`](./ksp-factory-file.md) — the factory that constructs `MfemWrapperSolver` instances through `MakeWrapperSolver` / `ConfigurePreconditionerSolver`.
- [`L0/apply-linop-overload-set`](./apply-linop-overload-set.md) — sibling reference note for the *operator-side* `ComplexWrapperOperator` (which is to `Operator` what `MfemWrapperSolver` is to `mfem::Solver`).
- [`concepts/complex-from-real-lift`](../concepts/complex-from-real-lift.md) — the methodology concept that the complex specialisation realises on the preconditioner side.
- [`concepts/solver-as-operator`](../concepts/solver-as-operator.md) — the methodology concept (a solver "is" a linear operator); `MfemWrapperSolver` is a concrete carrier of this identification.

## Evidence (representative)

- `palace/linalg/solver.hpp:21-65` — `Solver<OperType>` abstract base class declaration: templated, inherits `OperType`, declares `SetOperator` pure-virtual, inherits `Mult` pure-virtual from `OperType`.
- `palace/linalg/solver.hpp:46-49` — base-class `MultTranspose` `MFEM_ABORT` (unimplemented at base level — concrete subclasses opt in).
- `palace/linalg/solver.hpp:52-64` — `Mult2` and `MultTranspose2` "with-temporary-storage" virtuals (also `MFEM_ABORT` at base — overridden by specific iterative solvers; see [`linalg-iterative-file`](./linalg-iterative-file.md)).
- `palace/linalg/solver.hpp:70-134` — `MfemWrapperSolver<OperType>` template class declaration.
- `palace/linalg/solver.hpp:77` — owned `pc` (the wrapped `mfem::Solver` `unique_ptr`).
- `palace/linalg/solver.hpp:80` — owned `A` (the assembled `mfem::HypreParMatrix` retained across `SetOperator` / `Mult` calls when `save_assembled = true`).
- `palace/linalg/solver.hpp:84-94` — configuration flags: `save_assembled` (84), `complex_matrix` (88), `drop_small_entries` (91), `reorder_reuse` (94). Related stateful counter `num_dropped_entries` is declared just below at line 97 (used by the MUMPS reorder-reuse pattern-change detection — see §"DropSmallEntries optimisation").
- `palace/linalg/solver.hpp:103-110` — constructor: takes a `unique_ptr<mfem::Solver>` and the four configuration flags.
- `palace/linalg/solver.hpp:125-129` — `SetInitialGuess` override (forwards to `pc->iterative_mode`).
- `palace/linalg/solver.hpp:131-133` — `SetOperator` and `Mult` virtual declarations (definitions in `solver.cpp`).
- `palace/linalg/solver.cpp:12-30` — `MfemWrapperSolver<Operator>::SetOperator` real-branch definition (HypreParMatrix or ParOperator dynamic-cast and forward).
- `palace/linalg/solver.cpp:33-136` — `MfemWrapperSolver<ComplexOperator>::SetOperator` complex-branch definition (equivalent-real block formulation or real-part approximation).
- `palace/linalg/solver.cpp:54-74` — equivalent-real block-matrix construction (`A = [Ar, Ai; Ai, -Ar]` via `HypreParMatrixFromBlocks`).
- `palace/linalg/solver.cpp:74-77` — real-part approximation construction (`A = Ar + Ai`).
- `palace/linalg/solver.cpp:138-142` — `MfemWrapperSolver<Operator>::Mult` real-branch definition (one-liner forwarding).
- `palace/linalg/solver.cpp:144-177` — `MfemWrapperSolver<ComplexOperator>::Mult` complex-branch definition; line 173 negates the imaginary part to undo the augmented-system sign convention.
- `palace/linalg/solver.cpp:179-207` — `DropSmallEntries` template definition; line 183 threshold (`ε²`); lines 185-202 MUMPS-specific reorder-reuse interaction.
- `palace/linalg/ksp.cpp:103-123` — `MakeWrapperSolver` template helper (the central wrapper-construction call site for the KSP factory).
- `palace/linalg/divfree.cpp:120` — divergence-free projection inner AMG construction.
- `palace/linalg/hcurl.cpp:92` — H(curl) AMS construction.
- `palace/linalg/errorestimator.cpp:88, 94` — error-estimator inner solver construction.
- `palace/models/modeeigensolver.cpp:666, 733, 742, 749, 761, 774` — six eigenmode-pipeline call sites.
