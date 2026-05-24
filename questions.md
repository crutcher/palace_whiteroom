# Question ledger

Questions surface **unknowns** about the target source. They are not the to-do list; that comes from push direction (see *Planner* prompt). The Planner reads this ledger to ground its push choices and to surface things that need source-level exploration before the next push is possible.

The seed below names one question per solver plus shared-infrastructure and mesh/FE-space anchors, so the Planner can interleave them rather than getting stuck in one solver's silo. Path hints are starting points — Explorers verify and narrow before reading.

## Open

### Phase 6 smoke-test target — PRIORITY

- **Q-gmres-phase6.** **PHASE 6 SMOKE-TEST.** Push the GMRES slice end-to-end through the layer stack. Treat as one of several priority targets; **interleave with leaf-support slices** (see below) rather than running GMRES-only — interleaving (a) builds vocabulary that simplifies subsequent GMRES rotations, (b) enables SIDEWAYS unification, and (c) prevents same-slice grind (cycles 2–9 grinding on GMRES alone produced zero accumulated surface).
  - **Source target:** `palace/palace/linalg/iterative.cpp` — `GmresSolver<Operator>::Mult` and its helper methods (Arnoldi-step inner loop, Hessenberg-matrix update, Givens-rotation application, restart logic). Also `palace/palace/linalg/iterative.hpp` for the declaration.
  - **Slice shape:** GMRES is **large**; use the multi-file slice subdirectory convention from the start: `book/src/spec/slices/gmres/` with per-aspect files (best Synthesizer judgment — likely `step.md`, `arnoldi.md`, `restart.md`, `convergence.md` or similar). See `book/src/spec/index.md`.
  - **Cross-cuts:** GMRES should reuse leaf-support concepts (`axpy`, `dot`, `matvec`, `apply_linop`, `orthog*` from Q-orthog-leaf) and propose new ones (`arnoldi_step`, `givens_rotation`, `hessenberg_extend`).
  - **Negative-L3 expected:** the outer iteration and the per-step Arnoldi orthogonalization sequence are likely L2→L3 obstructions (sequentiality). Record them as such; obstructions are first-class output.

### Leaf-support slices — PRIORITY (enable SIDEWAYS)

Small, well-bounded slices that each target a single support primitive. Their L0→L1 should be tractable in one cycle. They build the vocabulary that bigger slices (GMRES, solvers) reuse. The Planner should interleave these with Q-gmres-phase6 to enable SIDEWAYS comparisons and unblock Phase 6 DONE.

- **Q-divfree-leaf.** Divergence-free projection: given a vector, project onto the divergence-free subspace (kernel of the divergence operator). Used by driven/transient solvers for current and field projection.
  - **Source target:** `palace/palace/linalg/divfree.cpp` and `palace/palace/linalg/divfree.hpp`.
  - **Slice shape:** small; single file `book/src/spec/slices/divfree.md`.
  - **Expected concept extractions (L1):** `divfree_projection` (the operation itself), possibly `gradient_correction` if the implementation uses a Helmholtz-decomposition pattern. May reuse `matvec`, `apply_linop` if those have been extracted by then.

- **Q-orthog-leaf.** Gram-Schmidt orthogonalization variants: given a basis `V[0..k-1]` and a new vector `w`, produce `w'` orthogonal to the basis plus coefficients. Three variants: MGS (modified, sequential), CGS (classical, batched), CGS2 (CGS + one refinement pass). **High value**: this is the exact substitution interface GMRES needs at L2 (per `rotation.md` criterion 2 worked example); resolving orthog as its own slice gives GMRES the L2 substitution primitive cleanly.
  - **Source target:** `palace/palace/linalg/orthog.hpp` (likely header-only / template-only).
  - **Slice shape:** small; single file `book/src/spec/slices/orthog.md`.
  - **Expected concept extractions (L1):** `mgs_orthog`, `cgs_orthog`, `cgs2_orthog`, and possibly a unifying `orthogonalize` primitive that takes a variant parameter (test of `variant-absorption.md` *Levels of absorption* — likely satisfies all three levels via constructed-operator absorption).
  - **Cross-cut with GMRES:** once `orthog.md` lands, GMRES's L1→L2 should reference these primitives directly rather than re-deriving them.

- **Q-chebyshev-leaf.** Chebyshev polynomial smoother: given an operator `A` with bounded spectrum `[λ_min, λ_max]`, apply a polynomial `p_k(A)` tuned to damp high-frequency error. Used as a smoother in multigrid preconditioners.
  - **Source target:** `palace/palace/linalg/chebyshev.cpp` and `palace/palace/linalg/chebyshev.hpp`.
  - **Slice shape:** small; single file `book/src/spec/slices/chebyshev.md`.
  - **Expected concept extractions (L1):** `chebyshev_polynomial_step`, `spectrum_estimate` (eigenvalue bound), possibly `polynomial_acceleration` as a more general pattern that Chebyshev specializes.

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
