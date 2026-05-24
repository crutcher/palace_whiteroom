# Question ledger

Questions surface **unknowns** about the target source. They are not the to-do list; that comes from push direction (see *Planner* prompt). The Planner reads this ledger to ground its push choices and to surface things that need source-level exploration before the next push is possible.

The seed below names one question per solver plus shared-infrastructure and mesh/FE-space anchors, so the Planner can interleave them rather than getting stuck in one solver's silo. Path hints are starting points — Explorers verify and narrow before reading.

## Open

### Phase 6 smoke-test target — PRIORITY

- **Q-gmres-phase6.** **PHASE 6 SMOKE-TEST.** Push the GMRES slice end-to-end through the layer stack as the inaugural full-loop exercise of the methodology. Prefer this as the next forward push when scheduling cycles, until GMRES has reached L4 (or surfaced a principled obstruction).
  - **Source target:** `palace/palace/linalg/iterative.cpp` — `GmresSolver<Operator>::Mult` and its helper methods (Arnoldi-step inner loop, Hessenberg-matrix update, Givens-rotation application, restart logic). Also `palace/palace/linalg/iterative.hpp` for the declaration.
  - **Slice shape:** GMRES is **large**; use the multi-file slice subdirectory convention from the start: `book/src/spec/slices/gmres/` with per-aspect files (best Synthesizer judgment — likely `step.md`, `arnoldi.md`, `restart.md`, `convergence.md` or similar). See `book/src/spec/index.md`.
  - **Cross-cuts:** GMRES should reuse the existing CG-slice concepts (`axpy`, `dot`, `matvec`, `apply_linop`) and propose new ones (`arnoldi_step`, `givens_rotation`, `hessenberg_extend`) — that cross-slice unification is part of the Phase 6 DONE criteria.
  - **Negative-L3 expected:** the outer iteration and the per-step Arnoldi orthogonalization sequence are likely L2→L3 obstructions (sequentiality). Record them as such; obstructions are first-class output.

### Shared infrastructure (cross-solver)

- **Q-shared-1.** What is the top-level entry point in Palace, and how does it dispatch between solvers? (Starting point: `palace/main.cpp`; the dispatched solvers live under `palace/drivers/`, base class likely `palace/drivers/basesolver.cpp`.)
- **Q-shared-2.** How are FE spaces constructed and registered? What is the assembled-operator interface that all five solvers consume? (Starting point: `palace/fem/`; MFEM `BilinearForm` / `MixedBilinearForm` are the upstream surface.)
- **Q-shared-3.** Which Krylov / preconditioner / eigensolver machinery is shared across solvers, and which is per-solver? (Starting point: `palace/linalg/`.)

### Mesh / FE-space construction (in scope per CLAUDE.md *Scope*)

- **Q-mesh-1.** How is the mesh loaded, partitioned (locally — MPI is out of scope), and refined? What basis types are supported (H1, Nédélec, Raviart-Thomas, L2) and how do they compose into mixed forms?
- **Q-mesh-2.** What does the FE assembly pipeline look like end-to-end — from `BilinearForm` declaration through quadrature-rule selection and geometric-factor computation to the assembled (sparse or partial-assembly) operator? Where are libCEED's exascale kernels invoked vs. MFEM's local-assembly paths?

### Per-solver

- **Q-electrostatic.** What is the electrostatic solver's top-level algorithm and what variational form drives it? (`palace/drivers/electrostaticsolver.cpp`.)
- **Q-magnetostatic.** Same for magnetostatic. (`palace/drivers/magnetostaticsolver.cpp`.)
- **Q-eigenmode.** Which eigensolver is used (LOBPCG, Arnoldi, …), what shift / spectral transformation, what preconditioning? (`palace/drivers/eigensolver.cpp`; also `palace/models/modeeigensolver.cpp` for the mode-decomposition step. Note: `palace/drivers/boundarymodesolver.cpp` is a related solver; clarify whether it's a sub-component of the eigenmode pipeline or independent.)
- **Q-driven.** What does the per-frequency sweep look like, and how is the linear solve structured? (`palace/drivers/drivensolver.cpp`.)
- **Q-transient.** What time-stepping scheme (Newmark, Runge-Kutta, …), what update structure, what stability / consistency conditions? (`palace/drivers/transientsolver.cpp`.)

## Closed

(none)
