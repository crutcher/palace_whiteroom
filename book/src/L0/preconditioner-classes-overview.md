# Class — preconditioner-classes overview (`palace/linalg/{amg,ams,jacobi,chebyshev,distrelaxation,gmg,blockprecond}.{hpp,cpp}`)

A reference note surveying the preconditioner class hierarchy that the KSP factory ([`ksp-factory-file`](./ksp-factory-file.md)) constructs and that `BaseKspSolver` ([`kspsolver-base-class`](./kspsolver-base-class.md)) composes with. Palace ships **seven preconditioner classes** (plus the wrapper layer that lifts them into the `Solver<OperType>` hierarchy, covered separately in [`mfem-wrapper-solver`](./mfem-wrapper-solver.md)). This chapter is the file-level overview of those seven classes; it is the L0 anchor for the future `L1/apply_preconditioner` operator and for any L1 / L4 entry that needs to refer to "the preconditioner class set" as a whole.

The seven classes split into three groups by inheritance and orchestration shape:

- **Hypre-wrapped algebraic preconditioners** — inherit from `mfem::HypreSolver`, route through `MfemWrapperSolver` for composition into `Solver<OperType>`. `BoomerAmgSolver` (`palace/linalg/amg.{hpp,cpp}`) and `HypreAmsSolver` (`palace/linalg/ams.{hpp,cpp}`).
- **Native `Solver<OperType>` smoothers** — inherit from `palace::Solver<OperType>` directly (templated on real / complex), implement `Mult` in terms of `OperType`'s `Mult` and a stored inverse-diagonal vector. `JacobiSmoother`, `ChebyshevSmoother`, `ChebyshevSmoother1stKind`, `DistRelaxationSmoother`.
- **Composition preconditioners** — wrap a sequence of other `Solver<OperType>` objects and orchestrate them. `GeometricMultigridSolver` (V-cycle over a level hierarchy), `BlockDiagonalPreconditioner` (2-block lower-triangular).

Direct-solver wrappers (`MumpsSolver`, `SuperLUSolver`, `StrumpackSolver`, `StrumpackMixedPrecisionSolver`) are also preconditioner-class members of the `LinearSolver` enum but they inherit from MFEM direct-solver classes and are covered as part of the wrapper-side discussion in [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) §"Where `MfemWrapperSolver` is used"; this chapter focuses on the seven non-direct-solver classes.

## The `LinearSolver` enum and dispatch

The seven preconditioner classes (plus the four direct-solver wrappers) are switched on by the `LinearSolver` enum at `palace/utils/labels.hpp:91-101`:

```cpp
enum class LinearSolver : char
{
  DEFAULT, AMS, BOOMER_AMG, MUMPS, SUPERLU, STRUMPACK, STRUMPACK_MP, JACOBI
};
```

Dispatch lives in `ConfigurePreconditionerSolver` (`palace/linalg/ksp.cpp:125-240`). The switch (lines 136-204) constructs the base preconditioner object — `HypreAmsSolver` / `BoomerAmgSolver` / one of the direct solvers / `JacobiSmoother` — and then post-processes (lines 207-239): if `fespaces.GetNumLevels() > 1`, the base preconditioner is wrapped in a `GeometricMultigridSolver` as the coarse-level solver, with Chebyshev / Distributive-Relaxation as the smoothers at every other level.

**`ChebyshevSmoother`, `ChebyshevSmoother1stKind`, and `DistRelaxationSmoother` are not directly enum-selectable.** They are **constructed implicitly by `GeometricMultigridSolver`'s constructor** (`palace/linalg/gmg.hpp:60-64` parameters `cheby_smooth_it`, `cheby_order`, `cheby_sf_max`, `cheby_sf_min`, `cheby_4th_kind`; selection of distributive-relaxation vs Chebyshev happens inside that constructor based on whether the discrete-gradient hierarchy `G` is non-null, with `G` constructed conditionally on `linear.mg_smooth_aux` at the IIFE in `ksp.cpp:213-232` before being forwarded to the constructor). The L0 surface for these smoothers is therefore the geometric-multigrid composition; their L1 lift would be **subordinate** to whatever lift `GeometricMultigridSolver` gets.

**`BlockDiagonalPreconditioner` is constructed at the model-pipeline layer**, not by the KSP factory. It is used in the wave-port / boundary-mode pipelines where the system has a natural 2-block structure (e.g., tangential / normal field components).

## Group 1 — Hypre-wrapped algebraic preconditioners

**`BoomerAmgSolver`** (`palace/linalg/amg.hpp:16-27`) is a thin 12-line class definition (inside a 31-line header file) wrapping `mfem::HypreBoomerAMG`. The constructor takes four parameters (cycle iteration count, smoothing iteration count, aggressive-coarsening flag, print level) and forwards them to MFEM's BoomerAMG. There is no override of any method — the wrapper exists purely to compose the configuration arguments and to provide an `IoData`-aware constructor (lines 21-26) that pulls the parameters out of the parsed configuration. The actual AMG algorithm lives entirely in Hypre; this class is a thin adapter.

**`HypreAmsSolver`** (`palace/linalg/ams.hpp:20-79`) wraps `HYPRE_Solver ams` (a Hypre AMS handle, line 24) inside `mfem::HypreSolver`. AMS (Auxiliary-space Maxwell Solver) is the standard preconditioner for the Nédélec-element Maxwell system; it requires a **discrete gradient matrix** `G` (line 34, non-owning) and **Nédélec interpolation matrices** `Pi, Pix, Piy, Piz` (line 38, owned) constructed at preconditioner-build time from the H1 and Nédélec finite-element spaces. The construction lives in `ConstructAuxiliaryMatrices` (`palace/linalg/ams.cpp:51-134`), which at line 74 instantiates the `ParGridFunction` coordinate fields that become the near-null-space basis — already cited from [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) §"What Palace touches" as the one `Par*` use in `palace/linalg/`. The `InitializeSolver` method (`palace/linalg/ams.cpp:136-197`) wires the auxiliary matrices into Hypre's AMS via `HYPRE_AMSSetDiscreteGradient` and `HYPRE_AMSSetInterpolations` calls. `SetOperator` (`palace/linalg/ams.cpp:199-222`) re-runs the solver setup when the system matrix changes.

Both Hypre-wrapped classes have **MFEM-side `Mult` inherited from `mfem::HypreSolver`** — there is no Palace-side `Mult` body. The L0 algebraic content (the V-cycle or AMS application) lives in Hypre; Palace only owns the construction sequence and the per-`SetOperator` re-setup.

## Group 2 — Native `Solver<OperType>` smoothers

These four classes all template over `OperType ∈ {Operator, ComplexOperator}` and inherit from `Solver<OperType>`. They share a common shape:

- **Construct from `MPI_Comm`** plus a small set of scalar parameters (damping factor, polynomial order, scaling factors, smoothing iteration count).
- **`SetOperator(const OperType &op)`** stores the operator reference and computes an `inverse diagonal` `VecType dinv` member (via `op.AssembleDiagonal(d)` then elementwise inversion).
- **`Mult(const VecType &x, VecType &y) const override`** implements one or more sweeps of the smoothing iteration using `dinv` and additional residual / workspace vectors.

**`JacobiSmoother<OperType>`** (`palace/linalg/jacobi.hpp:18-44`) is the simplest. It stores only `dinv`, `omega` (damping), `sf_max` (max-eigenvalue scaling factor). `Mult` (`palace/linalg/jacobi.cpp:100-104`) delegates to a local `Apply(dinv, x, y)` helper that computes the simple-diagonal Jacobi iteration — pointwise elementwise multiplication with damping, no operator-application calls. Trivially symmetric: `MultTranspose(x, y) { Mult(x, y); }` (header line 43).

**`ChebyshevSmoother<OperType>`** (`palace/linalg/chebyshev.hpp:22-77`) implements Chebyshev smoothing of the 4th kind (Phillips and Fischer, arXiv:2210.03179v1 (2022), cited in the file header at lines 19-20). State: `dinv`, `lambda_max` (estimated max eigenvalue of the operator), `sf_max`, `pc_it` (sweep count), `order` (polynomial order), `mutable VecType d, r` workspaces. `Mult2(x, y, r)` (`palace/linalg/chebyshev.cpp:190-220`) implements the polynomial recurrence; the externally-supplied `r` workspace lets the multigrid V-cycle reuse the level-`l` residual vector without reallocation. The `Mult(x, y)` and `MultTranspose(x, y)` wrappers (lines 51-69) allocate `r` internally if needed and forward to `Mult2`.

**`ChebyshevSmoother1stKind<OperType>`** (`palace/linalg/chebyshev.hpp:85-142`) is the 1st-kind variant (Adams et al. JCP 2003, lines 82-83). Same shape as the 4th-kind version but with two extra parameters (`theta`, `delta`) derived from `lambda_max` and `lambda_min` estimates. Less commonly used; gated by `linear.mg_smooth_cheby_4th` in the geometric-multigrid constructor.

**`DistRelaxationSmoother<OperType>`** (`palace/linalg/distrelaxation.hpp:29-88`) implements Hiptmair distributive relaxation (Hiptmair, SIAM J. Numer. Anal. 1998, lines 25-27) for Maxwell-type problems. The smoother runs a point smoother on the primary operator `A` **and** on its projection into an auxiliary space `A_G = Gᵀ A G` (where `G` is the discrete gradient). Holds two sub-`Solver<OperType>` instances (`B, B_G`, lines 46-47), each typically a `ChebyshevSmoother`. The dispatch from `GeometricMultigridSolver` to `DistRelaxationSmoother` versus plain `ChebyshevSmoother` is keyed by the presence of the auxiliary-space interpolators `G`: the IIFE at `ksp.cpp:213-232` constructs `G` from the FE-space hierarchy (or passes `nullptr`) and forwards it to the `GeometricMultigridSolver` constructor, which then dispatches to DistRelaxation when `G` is non-null and to plain Chebyshev otherwise (selection logic inside the constructor body, `gmg.cpp`). Note: `SetOperator(const OperType &op)` aborts with `MFEM_ABORT` (lines 57-61) because the distributive-relaxation smoother requires two operators; consumers must call `SetOperators(op, op_G)` instead. The aborting single-operator override is a deliberate contract guard.

## Group 3 — Composition preconditioners

**`GeometricMultigridSolver<OperType>`** (`palace/linalg/gmg.hpp:30-82`) implements the V-cycle / W-cycle multigrid algorithm over a level hierarchy. State:

- `const int pc_it` — V-cycles per preconditioner application (line 37).
- `std::vector<const Operator *> P` — prolongation operators (level-to-finer, line 40, non-owning).
- `std::vector<const OperType *> A` — system matrices per level (line 43, non-owning).
- `std::vector<const mfem::Array<int> *> dbc_tdof_lists` — per-level Dirichlet-tdof lists (line 44).
- `mutable std::vector<std::unique_ptr<Solver<OperType>>> B` — smoothers per level; coarse solver is `B[0]` (lines 46-47).
- `mutable std::vector<VecType> X, Y, R` — per-level workspaces (`X` = input, `Y` = output, `R` = residual; line 51).
- `bool use_timer` — timer-contribution toggle (line 54).

`Mult(x, y)` (`palace/linalg/gmg.cpp:126-142`) sets `X.back() = x` (copy to finest level), runs `pc_it` V-cycles by calling `VCycle(n_levels - 1, (it > 0))`, returns `y = Y.back()`. The V-cycle body (`palace/linalg/gmg.cpp:172-205`) is the canonical recursive structure: pre-smooth on the current level (or coarse-solve when `l == 0`), compute residual via `A[l]->Mult(Y[l], R[l])` and `linalg::AXPBY(1.0, X[l], -1.0, R[l])`, restrict to the next-coarser level via `RealMultTranspose(*P[l - 1], R[l], X[l - 1])`, recursively call `VCycle(l - 1, false)`, prolongate back via `RealMult(*P[l - 1], Y[l - 1], R[l])` and `Y[l] += R[l]`, post-smooth with non-zero initial guess.

The `RealMult` / `RealMultTranspose` helpers in an anonymous namespace (`palace/linalg/gmg.cpp:147-167`) split a `ComplexVector` into its real and imaginary parts and apply the real prolongation operator separately to each — the prolongation operator family is always real-valued, but the multigrid hierarchy carries complex vectors when `OperType = ComplexOperator`. This is the prolongation-side companion to [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) §"The complex specialisation" (the wrapper-side companion in the equivalent-real block formulation).

**`BlockDiagonalPreconditioner<OperType>`** (`palace/linalg/blockprecond.hpp:31-61`) is a 2-block lower-triangular preconditioner:

```text
P = [P0      0 ]
    [L10    P1 ]
```

State: `int block0_size`, two sub-`Solver<OperType>` instances `pc0, pc1` (line 38), an optional non-owning `const OperType *L10` for the lower off-diagonal (line 39), and five workspace vectors `mutable VecType x0, y0, x1, y1, t1` (line 40). `Mult` applies the forward solve `z0 = P0⁻¹ r0; z1 = P1⁻¹ (r1 - L10 z0)`. When `L10` is null (the default), the preconditioner reduces to block-diagonal.

Two type aliases at lines 63-64: `BlockDiagonalPreconditionerReal = BlockDiagonalPreconditioner<Operator>;` and `BlockDiagonalPreconditionerComplex = BlockDiagonalPreconditioner<ComplexOperator>;`. The class is the wave-port pipeline's preconditioner for the tangential / normal field-component split.

## State shape and workspace patterns

Across the seven classes, the workspace patterns map onto [`mutable-workspace-pattern`](./mutable-workspace-pattern.md):

- **Category 2 (composition-class workspaces)** — `SumOperator::z` shape: `JacobiSmoother` (none — pointwise iteration), `ChebyshevSmoother::d, r` (lines 44 / 108), `DistRelaxationSmoother::x_G, y_G, r_G, r` (line 50), `BlockDiagonalPreconditioner::x0, y0, x1, y1, t1` (line 40), `GeometricMultigridSolver::X, Y, R` (line 51).
- **Category 1 (Hypre handles + owned matrices)** — `HypreAmsSolver::Pi, Pix, Piy, Piz, x, y, z` (lines 38-39); the `HypreParVector x, y, z` are workspace vectors for the Hypre AMS solver's internal use (cited from [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) line 39).

Reference state (non-owning operator / projector references) is uniform across the smoother classes: `const OperType *A` (system matrix, set via `SetOperator`), plus auxiliary references where applicable (`const Operator *G` for `DistRelaxationSmoother`, `const OperType *A_G` for the auxiliary projection).

## Test coverage

There is **no dedicated `test-preconditioner.cpp`** or per-class smoother test under `palace/test/unit/`. The preconditioner classes are exercised:

- **Indirectly via Krylov solver tests** — every CG / GMRES test (`test-orthog.cpp` exercises the orthogonalization paths that GMRES uses; the iterative solvers themselves are tested end-to-end). The preconditioner is composed via `BaseKspSolver`'s constructor and applied per `Mult` call.
- **End-to-end via `reference/palace/test/examples/`** — the regression-test pipeline runs full electrostatic / magnetostatic / driven / eigenmode / transient solves with the configured preconditioner stack (BoomerAMG for electrostatic, AMS + GMG + Chebyshev for magnetostatic/driven/eigenmode). These tests assert on physics outputs (field energies, Q-factors, eigenvalues) and are the canonical empirical authority for the preconditioner-stack semantics.

This is a **test-coverage gap of the same shape as [`eigensolver-wrapper`](./eigensolver-wrapper.md)** — the preconditioner classes' algebraic claims lean on direct source reading and on the literature citations (Phillips-Fischer 2022 for 4th-kind Chebyshev, Adams et al. 2003 for 1st-kind, Hiptmair 1998 for distributive relaxation, the Hypre AMS / BoomerAMG manuals for the algebraic preconditioners) rather than on test linkages.

## Notes for higher layers

- **L1 has no `apply_preconditioner` operator yet.** It is an open question whether the preconditioner application should be lifted as a single `apply_preconditioner :: Pc -> VecType -> VecType` operator (uniform across all seven classes since they all implement `Mult` with the same signature) or as a per-class family (`apply_jacobi`, `apply_chebyshev`, `apply_amg`, `apply_ams`, `apply_gmg_vcycle`, `apply_block_lower_tri`). The uniform lift is the natural starting point: the dispatch to the concrete class is an L0 implementation detail handled by the `Solver<OperType>` polymorphism.
- **`GeometricMultigridSolver` is the only class with non-trivial L1 algebraic structure.** The other six are either Hypre-internal (`BoomerAmgSolver`, `HypreAmsSolver` — algebra lives in Hypre, not Palace), pointwise (`JacobiSmoother`), polynomial recurrence (`ChebyshevSmoother`, lifted at [`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md)), or composition of others (`DistRelaxationSmoother`, `BlockDiagonalPreconditioner`). The V-cycle's recursive smooth / restrict / coarse-solve / prolongate / smooth structure is the most algorithmically substantive of the seven and would lift as an L2 `v_cycle` combinator over a `multigrid_hierarchy` data structure.
- **The Chebyshev smoothers reuse the same arithmetic structure as the L2 `chebyshev-iteration` concept** (per [`concepts/chebyshev-iteration`](../concepts/chebyshev-iteration.md)). The smoother-vs-iteration distinction is contextual (a Chebyshev smoother is a Chebyshev iteration applied as one or two sweeps inside a multigrid level, with the eigenvalue estimates carrying the level-local operator's spectrum). The L2 lift could share the same combinator.
- **The `BoomerAmgSolver` and `HypreAmsSolver` algebraic content is out of scope for direct dissection** — the V-cycle and AMS algorithms live inside Hypre / MFEM. The L1 surface for these two is "call Hypre's solver with the constructed auxiliary matrices"; the auxiliary-matrix construction in `HypreAmsSolver::ConstructAuxiliaryMatrices` is the only Palace-side algebra and it is itself a sequence of MFEM `ParBilinearForm` assemblies. The L1 lift records this as an "Hypre black-box preconditioner" obstruction, similar in spirit to the [`L1-L0/minres-iteration`](../L1-L0/minres-iteration.md) "advertised-but-unimplemented" obstruction (here it is "implemented but in vendored code").
- **The `BlockDiagonalPreconditioner` is the only class with no `OperType` discriminator at the algorithm level** — the 2-block forward solve has the same shape regardless of whether the sub-solvers are real or complex. Its L1 lift would be `apply_block_lower_tri :: Solver -> Solver -> Maybe Op -> Vec -> Vec` with the `OperType` axis as a transparent type parameter.

## Dependencies

- [`ksp-factory-file`](./ksp-factory-file.md) — the dispatch site that constructs these classes from the `LinearSolver` enum and composes them with `GeometricMultigridSolver` when a level hierarchy is present.
- [`kspsolver-base-class`](./kspsolver-base-class.md) — the composition class that holds a `std::unique_ptr<Solver<OperType>> pc` field; the preconditioner classes here are what populates that field.
- [`mfem-wrapper-solver`](./mfem-wrapper-solver.md) — the adapter that lifts `BoomerAmgSolver` and `HypreAmsSolver` (both inherit from `mfem::HypreSolver`) into `Solver<OperType>` for composition with `BaseKspSolver`. Also the home of the direct-solver wrapper discussion (`MumpsSolver`, `SuperLUSolver`, `StrumpackSolver`, `StrumpackMixedPrecisionSolver`).
- [`linalg-operator-file`](./linalg-operator-file.md) — `BaseMultigridOperator<OperType>` is the *operator-side* container for the multigrid level hierarchy; `GeometricMultigridSolver` is the *solver-side* algorithm that consumes it.
- [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) — the workspace patterns across the seven classes are Categories 1 and 2 of the cross-cutting workspace classification.
- [`par-types-single-rank-reading`](./par-types-single-rank-reading.md) — `HypreAmsSolver`'s `HypreParVector` workspaces and `ParGridFunction` coordinate fields collapse under this rule.

## Referenced from

- [`L0/ksp-factory-file`](./ksp-factory-file.md) — the dispatch into `ConfigurePreconditionerSolver` names these classes by enum case.
- [`L0/mfem-wrapper-solver`](./mfem-wrapper-solver.md) — already names `BoomerAMG` and `HypreAmsSolver` in passing; this chapter is the full per-class file-level survey.
- [`L0/mutable-workspace-pattern`](./mutable-workspace-pattern.md) — workspace-pattern reference forwards here for the smoother-class examples.
- Higher-layer L1 / L4 entries (forward-target): future `L1/apply_preconditioner` operator anchors here; L4 representation of the iterative solver loop names "the preconditioner application" abstractly and resolves to this set.

## Evidence (representative)

- `palace/utils/labels.hpp:91-101` — `LinearSolver` enum (eight cases including `DEFAULT`).
- `palace/linalg/ksp.cpp:125-240` — `ConfigurePreconditionerSolver<OperType>` function body; the switch over `LinearSolver` enum spans lines 136-204.
- `palace/linalg/ksp.cpp:198-200` — `JACOBI` branch construction.
- `palace/linalg/ksp.cpp:207-239` — geometric-multigrid composition when `fespaces.GetNumLevels() > 1`.
- `palace/linalg/amg.hpp:1-31` — `BoomerAmgSolver` header file (31 lines total, including license / include).
- `palace/linalg/amg.hpp:16-27` — `BoomerAmgSolver` class definition (wrapper around `mfem::HypreBoomerAMG`).
- `palace/linalg/amg.cpp:1-36` — `BoomerAmgSolver` implementation (36 lines).
- `palace/linalg/ams.hpp:20-79` — `HypreAmsSolver` class (wrapper around Hypre AMS, inheriting from `mfem::HypreSolver`).
- `palace/linalg/ams.hpp:34` — `const mfem::HypreParMatrix *G;` (discrete gradient, non-owning).
- `palace/linalg/ams.hpp:38` — `std::unique_ptr<mfem::HypreParMatrix> Pi, Pix, Piy, Piz;` (Nédélec interpolation matrices).
- `palace/linalg/ams.hpp:39` — `std::unique_ptr<mfem::HypreParVector> x, y, z;` (workspace).
- `palace/linalg/ams.hpp:42-43` — `ConstructAuxiliaryMatrices` private helper declaration.
- `palace/linalg/ams.hpp:46` — `InitializeSolver` private helper declaration.
- `palace/linalg/ams.cpp:51-134` — `ConstructAuxiliaryMatrices` implementation.
- `palace/linalg/ams.cpp:74` — `mfem::ParGridFunction x_coord(&h1_fespace.Get()), y_coord(...), ...;` coordinate-field construction.
- `palace/linalg/ams.cpp:136-197` — `InitializeSolver` implementation (Hypre AMS wiring).
- `palace/linalg/ams.cpp:199-222` — `SetOperator` (re-runs setup when system matrix changes).
- `palace/linalg/jacobi.hpp:18-44` — `JacobiSmoother<OperType>` class.
- `palace/linalg/jacobi.hpp:28` — `VecType dinv;` (inverse diagonal scaling).
- `palace/linalg/jacobi.hpp:31` — `double omega, sf_max;` (damping factor + scaling).
- `palace/linalg/jacobi.cpp:100-104` — `Mult` body (delegates to local `Apply(dinv, x, y)` for pointwise `y = omega · dinv ⊙ x`).
- `palace/linalg/chebyshev.hpp:22-77` — `ChebyshevSmoother<OperType>` (4th-kind Chebyshev).
- `palace/linalg/chebyshev.hpp:19-20` — Phillips-Fischer 2022 reference.
- `palace/linalg/chebyshev.hpp:32` — `const int pc_it, order;` parameters.
- `palace/linalg/chebyshev.hpp:38` — `VecType dinv;`.
- `palace/linalg/chebyshev.hpp:41` — `double lambda_max, sf_max;`.
- `palace/linalg/chebyshev.hpp:44` — `mutable VecType d, r;` workspace.
- `palace/linalg/chebyshev.hpp:71-76` — `Mult2(x, y, r)` declaration; `MultTranspose2` assumes symmetry (line 75 `Mult2(x, y, r);  // Assumes operator symmetry`).
- `palace/linalg/chebyshev.hpp:85-142` — `ChebyshevSmoother1stKind<OperType>` (1st-kind Chebyshev, Adams et al. 2003 — lines 82-83 reference).
- `palace/linalg/chebyshev.cpp:190-220` — `ChebyshevSmoother::Mult2` body (polynomial recurrence).
- `palace/linalg/chebyshev.cpp:260-293` — `ChebyshevSmoother1stKind::Mult2` body.
- `palace/linalg/distrelaxation.hpp:29-88` — `DistRelaxationSmoother<OperType>` (Hiptmair 1998).
- `palace/linalg/distrelaxation.hpp:25-27` — Hiptmair reference.
- `palace/linalg/distrelaxation.hpp:39` — `const Operator *G;` (discrete gradient).
- `palace/linalg/distrelaxation.hpp:42` — `const OperType *A, *A_G;` (primary + auxiliary-space system matrices).
- `palace/linalg/distrelaxation.hpp:46-47` — `mutable std::unique_ptr<Solver<OperType>> B; std::unique_ptr<Solver<OperType>> B_G;` (sub-smoothers).
- `palace/linalg/distrelaxation.hpp:50` — `mutable VecType x_G, y_G, r_G, r;` workspace.
- `palace/linalg/distrelaxation.hpp:57-61` — `SetOperator(const OperType &op)` aborts with `MFEM_ABORT` (contract guard requiring `SetOperators(op, op_G)`).
- `palace/linalg/distrelaxation.cpp:98-119` — `Mult2` body.
- `palace/linalg/gmg.hpp:30-82` — `GeometricMultigridSolver<OperType>` class.
- `palace/linalg/gmg.hpp:37` — `const int pc_it;` (V-cycles per application).
- `palace/linalg/gmg.hpp:40` — `std::vector<const Operator *> P;` (prolongation operators).
- `palace/linalg/gmg.hpp:43-44` — `std::vector<const OperType *> A; std::vector<const mfem::Array<int> *> dbc_tdof_lists;`.
- `palace/linalg/gmg.hpp:46-47` — `mutable std::vector<std::unique_ptr<Solver<OperType>>> B;` (per-level smoothers; `B[0]` is coarse solver).
- `palace/linalg/gmg.hpp:51` — `mutable std::vector<VecType> X, Y, R;` (per-level workspaces).
- `palace/linalg/gmg.hpp:57` — `void VCycle(int l, bool initial_guess) const;` private method.
- `palace/linalg/gmg.hpp:60-64` — primary constructor with Chebyshev / distributive-relaxation parameters.
- `palace/linalg/gmg.cpp:66-123` — `SetOperator` (recursively sets operators on all levels).
- `palace/linalg/gmg.cpp:126-142` — `Mult` (sets `X.back() = x`, runs `pc_it` V-cycles, returns `Y.back()`).
- `palace/linalg/gmg.cpp:147-167` — anonymous-namespace `RealMult` / `RealMultTranspose` helpers (split-on-element-type prolongation application).
- `palace/linalg/gmg.cpp:172-205` — `VCycle` recursive body (pre-smooth, residual, restrict, recurse, prolongate, post-smooth).
- `palace/linalg/gmg.cpp:207-208` — `template class GeometricMultigridSolver<Operator>; template class GeometricMultigridSolver<ComplexOperator>;`.
- `palace/linalg/blockprecond.hpp:31-61` — `BlockDiagonalPreconditioner<OperType>` (2-block lower-triangular).
- `palace/linalg/blockprecond.hpp:16-23` — comment block specifying the `P = [P0 0; L10 P1]` shape.
- `palace/linalg/blockprecond.hpp:38` — `std::unique_ptr<Solver<OperType>> pc0, pc1;`.
- `palace/linalg/blockprecond.hpp:39` — `const OperType *L10 = nullptr;` (lower off-diagonal, non-owning).
- `palace/linalg/blockprecond.hpp:40` — `mutable VecType x0, y0, x1, y1, t1;` workspace.
- `palace/linalg/blockprecond.hpp:51` — `SetBlockOperators(op0, op1)` block-aware operator setter.
- `palace/linalg/blockprecond.hpp:55` — `SetOffDiagonalOperator(op10)` lower-triangular setter (when null, reduces to block-diagonal).
- `palace/linalg/blockprecond.hpp:63-64` — `BlockDiagonalPreconditionerReal` / `BlockDiagonalPreconditionerComplex` type aliases.
