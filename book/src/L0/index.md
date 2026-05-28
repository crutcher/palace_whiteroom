# L0 — Cited Palace source ranges + reference notes

Ground truth and its short interpretation overlay. L0 is **citations** that anchor higher layers to concrete code, **plus** a small set of cross-cutting reference notes that explain what L1 entries are actually referring to when they cite L0.

## Context

L0 is the evidence floor. Every claim higher in the stack carries an L0 citation as its anchor. Historically (slice-era), L0 also accumulated line-level prose duplication of source — too robust. The current organisation keeps L0 lean: **citations remain the primary content**, with a small companion set of reference-note chapters that capture cross-cutting Palace / MFEM idioms once, so L1 operator entries can point at them rather than re-state them inline.

The reference notes are not source paraphrases. They name conventions (output-arg vs receiver mutation, MFEM-vector type duality, free-function vs method-form symbols, transparent vs load-bearing optimisation tricks) and give file-level overviews of the two anchor files L1 references repeatedly (`linalg/vector.{hpp,cpp}`, `linalg/ksp.cpp`). Each chapter is 2–4 paragraphs of interpretation plus representative citations; no line-by-line transcription.

## Reference-note cohort

**Conventions** — cross-cutting Palace / MFEM idioms referenced by L1 entries:

- [`output-arg-vs-receiver`](./output-arg-vs-receiver.md) — `A.Mult(x, y)` writes `y` vs receiver-mutating `y.Add(α, x)` / `y *= s`; how L1 lifts both into pure-functional form.
- [`mfem-vector-types`](./mfem-vector-types.md) — `Vector` / `ComplexVector` duality (element-type axis); brief intro to `Par*` types (see also `par-types-single-rank-reading`).
- [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) — the `Par*` MFEM type family (`ParMesh`, `ParFiniteElementSpace`, `ParGridFunction`, `ParBilinearForm`, `HypreParVector`, `HypreParMatrix`) and the single-rank reading rule per `CLAUDE.md` "Scope". Also covers `palace::Mpi::` collective wrappers (`GlobalSum` / `GlobalMin` / …) and how they reduce under single-rank reading.
- [`linalg-free-functions`](./linalg-free-functions.md) — `linalg::AXPY` / `linalg::Dot` / `linalg::Norml2` as template-dispatch wrappers over the method-form surface; the wrapping pattern Palace uses across `vector.hpp`.
- [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — Operational L0 classification (lifted from `CLAUDE.md`): `α == 1.0` branch in `AXPY` is transparent; reduction-tree non-associativity is load-bearing. Worked examples from the BLAS-1 family.
- [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) — `mutable Vector z` workspace members on operator subclasses and iterative-solver subclasses; lazy-allocate-on-first-use, reuse-across-calls discipline. The L0 substrate for L1>L0 mutation-rotation themes' "workspace mention and erase" rewrite.

**File overviews** — anchor files L1 references repeatedly:

- [`linalg-vector-file`](./linalg-vector-file.md) — `palace/linalg/vector.{hpp,cpp}` at a glance. The home of `ComplexVector`, the `AXPY/AXPBY/AXPBYPCZ` family, `Dot`/`TransposeDot`/`LocalDot`, `Norml2`, `Normalize`.
- [`linalg-operator-file`](./linalg-operator-file.md) — `palace/linalg/operator.{hpp,cpp}` at a glance. The home of `ComplexOperator`, `ComplexWrapperOperator`, `SumOperator`, the `BaseProductOperator` / `BaseDiagonalOperator` / `BaseMultigridOperator` template families, and the `palace::linalg::` matrix-weighted norm / bilinear-form free functions. The file-level companion to [`apply-linop-overload-set`](./apply-linop-overload-set.md).
- [`ksp-factory-file`](./ksp-factory-file.md) — `palace/linalg/ksp.cpp` Krylov-solver factory. Enum-routed dispatch: CG / GMRES / FGMRES implemented; MINRES / BICGSTAB / DEFAULT abort. Anchor for the "advertised-but-unimplemented" pattern that drives the MINRES / BiCGStab obstruction themes.
- [`linalg-iterative-file`](./linalg-iterative-file.md) — `palace/linalg/iterative.{hpp,cpp}` at a glance. The home of `IterativeSolver<OperType>` base class plus the three concrete subclasses `CgSolver`, `GmresSolver`, `FgmresSolver`. The L0 anchor for the cycle-007+ `L1/ksp_solve` operator and for the per-step body that the L2 `krylov-step` entry instantiates.
- [`linalg-orthog-file`](./linalg-orthog-file.md) — `palace/linalg/orthog.hpp` (header-only, 93 lines) at a glance. The home of the vector-against-basis Gram-Schmidt family: `OrthogonalizeColumnMGS` (modified) and `OrthogonalizeColumnCGS` (classical, with `refine` → CGS2), plus the `IdentityInnerProduct` default inner-product policy. The L0 anchor for the firm `L1/orthogonalize` operator's `MGS | CGS | CGS2` variant axis; sibling to [`linalg-iterative-file`](./linalg-iterative-file.md) (which holds the `OrthogonalizeIteration` runtime dispatch).
- [`linalg-solver-file`](./linalg-solver-file.md) — `palace/linalg/solver.{hpp,cpp}` at a glance. The home of the abstract `Solver<OperType>` base class (the type-axis root of every Palace solver — preconditioner, iterative, or MFEM-wrapped) plus `MfemWrapperSolver<OperType>` (the in-file concrete adapter). Eight concrete subclass families inherit from `Solver<OperType>`; this chapter is the file-level overview and the navigation hub for the subclass hierarchy. Detailed companion: [`mfem-wrapper-solver`](./mfem-wrapper-solver.md).
- [`linalg-rap-file`](./linalg-rap-file.md) — `palace/linalg/rap.{hpp,cpp}` at a glance. The home of the **R·A·P (Galerkin) parallel-operator** family: `ParOperator` (real-valued) and `ComplexParOperator` (complex-valued, real/imag-split into two owned `ParOperator`s), plus the `BuildParSumOperator` weighted-summation family. Turns a local (L-vector) FE operator into a parallel (true-dof) one either matrix-free (prolongate-apply-restrict sandwich) or assembled (one `HypreParMatrix` triple product); the two paths are an algebraically-equivalent performance dual. The L0 file-level home for the `ParOperator` member of the [`apply-linop-overload-set`](./apply-linop-overload-set.md) family.
- [`fem-bilinearform-file`](./fem-bilinearform-file.md) — `palace/fem/bilinearform.{hpp,cpp}` at a glance. The home of the **finite-element assembly entry point**: `BilinearForm` (integrator-list → assembled operator) and `DiscreteLinearOperator` (interpolator-list → inter-space interpolation operator). The load-bearing surface is the **partial-assembly (matrix-free libCEED `ceed::Operator`) vs full-assembly (`hypre::HypreCSRMatrix`)** dual, dispatched by polynomial order against `pa_order_threshold`, plus the FE-space-hierarchy multigrid-operator-stack producer. The local-operator producer feeding [`linalg-rap-file`](./linalg-rap-file.md)'s `ParOperator` (`rap.cpp:100` calls `BilinearForm::FullAssemble`).
- [`mpi-globalsum-and-collectives`](./mpi-globalsum-and-collectives.md) — `palace/utils/communication.hpp` (header-only, 429 lines). The single file housing every MPI collective Palace performs: the `palace::mpi::DataType<T>` template family for type-discovery and the `palace::Mpi` singleton class wrapping `MPI_Allreduce` / `MPI_Bcast` / `MPI_Allgather` / `MPI_Barrier` / `MPI_Abort` plus rank-gated `Print` / `Warning` formatters. File-level companion to [`par-types-single-rank-reading`](./par-types-single-rank-reading.md)'s §"MPI collectives and the `palace::Mpi` namespace".

**Overload sets and class interfaces** — multi-overload / multi-subclass surfaces referenced by L1 / L2 / L4 entries:

- [`apply-linop-overload-set`](./apply-linop-overload-set.md) — the `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult` family on the `Operator` / `ComplexOperator` hierarchy, plus the concrete-subclass family (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`). The L0 anchor for `L1/apply_linop`'s 12-method-overload collapse and for the `apply-linop-mutation-rotation` lowering theme.
- [`kspsolver-base-class`](./kspsolver-base-class.md) — `BaseKspSolver<OperType>` in `palace/linalg/ksp.{hpp,cpp}`. The composition class pairing an `IterativeSolver` with a `Solver` (preconditioner) and exposing the public `Mult(b, x)` "solve `Ax = b`" entry point. Anchors the L4 `solve-monad` concept to concrete C++ and is the call-site target for solver use across Palace's model pipelines.
- [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) — `MfemWrapperSolver<OperType>` in `palace/linalg/solver.{hpp,cpp}`. The adapter that lifts MFEM's real-only `mfem::Solver` hierarchy into Palace's templated `Solver<OperType>` hierarchy. Every preconditioner Palace uses — `BoomerAMG`, `AMS`, `MUMPS`, `SuperLU`, `Strumpack` — comes through this wrapper before composition into a `BaseKspSolver`. The L0 substrate for the L4 `complex-from-real-lift` concept on the preconditioner side.
- [`eigensolver-wrapper`](./eigensolver-wrapper.md) — `EigenvalueSolver` abstract base in `palace/linalg/eps.hpp` plus three concrete wrappers: `ArpackEigenvalueSolver` (RCI), `SlepcEigenvalueSolver` (shell-matrix), and `NonLinearEigenvalueSolver` / `QuasiNewtonSolver` (Palace's own direct-Newton). The eigensolver-side composition with `ComplexKspSolver` for spectral-transformation inverse application, dispatched by the eigenmode pipeline at `palace/models/modeeigensolver.cpp:1029-1047`. The L0 anchor for the future `L1/eigsolve` operator and for the L4 eigensolve-monad composition that the [strawman calculus](../design/l4_calculus.md)'s `iterate_while` primitive instantiates.
- [`preconditioner-classes-overview`](./preconditioner-classes-overview.md) — survey of Palace's seven preconditioner classes (`BoomerAmgSolver`, `HypreAmsSolver`, `JacobiSmoother`, `ChebyshevSmoother`, `ChebyshevSmoother1stKind`, `DistRelaxationSmoother`, `GeometricMultigridSolver`, `BlockDiagonalPreconditioner`) across `palace/linalg/{amg,ams,jacobi,chebyshev,distrelaxation,gmg,blockprecond}.{hpp,cpp}`. Three-group classification (Hypre-wrapped algebraic / native `Solver<OperType>` smoothers / composition preconditioners). The L0 anchor for the future `L1/apply_preconditioner` operator and for L2 work on the V-cycle algebra.

## Source organization

The target repository is `reference/palace/` (gitignored, local clone of <https://github.com/awslabs/palace>). Major regions:

- `palace/linalg/` — Krylov solvers (CG, GMRES, BICGSTAB), preconditioners, smoothers, orthogonalization
- `palace/fem/` — Finite-element discretization (assembly, integration, basis evaluation)
- `palace/models/` — Solver pipelines (electrostatic, magnetostatic, eigenmode, driven, transient)
- `palace/utils/` — IO, configuration, mesh handling
- `palace/main/` — Entry points per solver
- `palace/test/unit/` — Topic-keyed unittests (often the most authoritative semantic statement; see `scaffolding/test-linkages/`)

## Citation format

Plain text `relative/path/file.ext:start-end` (relative to `reference/`), e.g., `palace/linalg/cg.cpp:42-67`. Editors with line-aware navigation resolve against local clones. No markdown links in citations — grep/IDE workflow is the navigation.

## Working Notes

- L0 cited-evidence pointers also live in the L1>L0 lowering theme entries (per-theme `evidence:` field).
- Negative-result citations (regions explicitly out of scope: MPI, `Par*` types) get noted in `scaffolding/decisions/` rather than the lowering themes.
- The reference-note cohort is **discipline-bound**: 2–4 paragraphs of interpretation + 3–6 representative citations per chapter; no line-by-line source duplication. When a reference note would need to grow past that, split it into a new chapter rather than expand the existing one.
- L1 operator `Context` sections that re-state any of the conventions chapters above are candidates for the cycle-005 retroactive-thinning sweep (priority #11) — the convention chapters' `Referenced from:` backlinks identify them.
