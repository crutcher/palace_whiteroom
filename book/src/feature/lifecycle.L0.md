---
kind: feature-surface
feature: lifecycle
level: L0
status: seed (composition-root)
l0_ground_truth:
  - palace/main.cpp:158-328 (main — the top-level lifecycle: parse, configure, dispatch driver, build mesh, run, finalize)
  - palace/drivers/basesolver.cpp:153-276 (BaseSolver::SolveEstimateMarkRefine — the solve-estimate-mark-refine adaptive outer loop)
  - palace/drivers/basesolver.hpp:31-67 (class BaseSolver — the pure-virtual driver dispatch + the AMR wrapper)
lifts_to:
  - book/src/feature/lifecycle.L1.md (the L1 pure-function lifecycle root)
specializes_to:
  - book/src/feature/electrostatic.L0.md (the electrostatic driver — one ProblemType specialization)
  - book/src/feature/magnetostatic.L0.md (the magnetostatic driver — one ProblemType specialization)
---

# lifecycle — L0 ground-truth surface

The **top-level simulation lifecycle** at L0: the cited Palace source that realizes the composition-root *spine* — `main` (`palace/main.cpp:158-328`) and the adaptive driver wrapper `BaseSolver::SolveEstimateMarkRefine` (`palace/drivers/basesolver.cpp:153-276`). This is the **meta-feature**: the driver-agnostic lifecycle (config → mesh → per-driver solve → estimate-mark-refine → output) that the 5 per-driver feature columns specialize. Every claim is a `(file:start-end)` citation.

`main` is `int main(int argc, char *argv[])` (`palace/main.cpp:158`); the driver wrapper is `void BaseSolver::SolveEstimateMarkRefine(std::vector<std::unique_ptr<Mesh>> &mesh) const` (`palace/drivers/basesolver.cpp:153`; declared `palace/drivers/basesolver.hpp:59`). The driver itself is the pure-virtual `Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const = 0` (`palace/drivers/basesolver.hpp:43-44`), overridden by each per-problem-type subclass — this is the **specialization seam**.

## The lifecycle, in source

The lifecycle runs in two source halves: the `main` scaffold sets everything up and selects the driver; `SolveEstimateMarkRefine` runs the selected driver under the adaptive outer loop. The stages, in order:

1. **Parse config.** After CLI handling (`--help` / `--version` / `--dry-run`, `:177-228`), `IoData iodata(argv[1], false)` (`palace/main.cpp:231`) parses the configuration file into the `iodata` config surface; `MakeOutputFolder(iodata, world_comm)` (`:232`) prepares the output directory. This `iodata` is the **single config input** threaded read-only through the entire lifecycle.

2. **Configure device + libraries.** `mfem::Device device(ConfigureDevice(iodata.solver.device), ...)` (`:237-238`) + `ConfigureCeedBackend(...)` (`:239`) + `hypre::Initialize()` (`:245`) + optional `slepc::Initialize(...)` (`:247`) bring up the CPU/GPU device and numeric libraries from config. (Single-machine scope: the MPI distribution machinery is read as its single-rank equivalent per CLAUDE.md §Scope.)

3. **Dispatch the per-driver specialization.** `const auto solver = [&]() -> std::unique_ptr<BaseSolver> { switch (iodata.problem.type) { ... } }()` (`:256-280`) selects ONE driver by `ProblemType`: `DRIVEN` → `DrivenSolver` (`:261`), `EIGENMODE` → `EigenSolver` (`:264`), `ELECTROSTATIC` → `ElectrostaticSolver` (`:267`), `MAGNETOSTATIC` → `MagnetostaticSolver` (`:270`), `TRANSIENT` → `TransientSolver` (`:273`), `BOUNDARYMODE` → `BoundaryModeSolver` (`:276`). This `switch` is the **specialization seam**: each branch constructs the per-driver subclass whose `Solve` override is the feature column. This is the L0 site the per-driver feature columns (electrostatic, magnetostatic, …) specialize.

4. **Build the mesh.** `auto smesh = mesh::Load(iodata, world_comm)` (`:287`) loads the serial mesh from config; `solver->Preprocess(iodata, smesh, world_comm)` (`:288`) applies driver-specific serial-stage preprocessing + nondimensionalization (the `Preprocess` virtual, `palace/drivers/basesolver.hpp:53-54`); `mesh::Partition(...)` (`:290`) + `mesh::RefineMesh(...)` (`:291`) partition and a-priori-refine; the result is collected into `std::vector<std::unique_ptr<Mesh>> mesh` (`:283`, `:300-302`).

5. **Run the driver under the adaptive outer loop.** `solver->SolveEstimateMarkRefine(mesh)` (`:304`) runs the selected driver. Inside (`palace/drivers/basesolver.cpp:153-276`):
   - **Initial solve + estimate.** `auto [indicators, ntdof] = Solve(mesh)` (`:174`) calls the per-driver `Solve` override (the feature-column body) ONCE; `double err = indicators.Norml2(comm)` (`:175`) reduces the error indicators to a scalar.
   - **The adaptive `while` loop** (`:190`): `while (use_amr && !ExhaustedResources(it, ntdof) && err >= refinement.tol)` — the loop guard is **state-generated** (the carry `{mesh, indicators, ntdof, err, it}` both produces the next iterate AND determines termination; `ExhaustedResources` at `:177-184`). Per iteration: **mark** the high-error elements (Dörfler thresholding, `:221-232`), **refine** the marked elements (`fine_mesh.GeneralRefinement(...)`, `:235-244`), optionally **rebalance** (`mesh::RebalanceMesh(...)`, `:247-261`), then **re-solve + estimate** `std::tie(indicators, ntdof) = Solve(mesh)` (`:266`) + `err = indicators.Norml2(comm)` (`:267`). The body threads the refined mesh + indicators forward — each iteration's input is the prior iteration's output.
   - **Completion** print (`:269-275`). When AMR is disabled (`refinement.max_it == 0`) the loop never enters and the lifecycle is the single initial `Solve` (the electrostatic exemplar's case).

6. **Finalize → output products.** Back in `main`: timing summary + memory stats (`:306-313`), `solver->SaveMetadata(...)` (`:314-316`) writes the run metadata, `ceed::Finalize()` (`:320`) + optional `slepc::Finalize()` (`:324`) tear down. The **physical products** themselves (capacitance / inductance / S-params / eigenfreq + Q / fields) are written by each driver's `Solve` / postprocess (the per-driver feature columns' output stage), not by `main`.

## Inputs / outputs (the lifecycle surface, in source)

- **Input — config.** The single `IoData iodata(argv[1], false)` (`palace/main.cpp:231`) config surface, threaded read-only through device-config, driver-dispatch, mesh-build, and the per-driver `Solve`. `iodata.problem.type` (`:258`) is the discriminant that selects the driver specialization.
- **Output — the physical products.** Per-driver: each `Solve` override computes its product (capacitance, inductance, S-parameters, eigenfrequencies + Q, fields) + writes it; `main` writes only run metadata (`SaveMetadata`, `:314-316`). The lifecycle root's "output" is therefore the *union* of the per-driver products, selected by `ProblemType`.

## Lifts to / specializes to

This L0 lifecycle surface lifts to the L1 pure-function lifecycle root [`lifecycle.L1`](./lifecycle.L1.md) (the config → output-products pure function) and the L4 composition-root [`lifecycle.L4`](./lifecycle.L4.md) (the per-driver `switch` → a dispatch over the driver feature columns; the AMR `while` → the firm L4 [`fold_solve`](../L4/fold_solve.md) state-generated fold). It **specializes to** the per-driver feature columns at the `ProblemType` seam: [`electrostatic.L0`](./electrostatic.L0.md), [`magnetostatic.L0`](./magnetostatic.L0.md) on disk; eigenmode / driven / transient columns are forthcoming (not yet authored — plain-text here). Each per-driver column's L0 surface is the `Solve` override that the `switch` selects; this lifecycle surface records the driver-agnostic scaffold + the specialization seam.

## Status

`seed (composition-root)` — the L0 ground-truth surface for the top-level lifecycle meta-feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). Every stage is a cited range into `palace/main.cpp` + `palace/drivers/basesolver.cpp` / `.hpp`, confirmed on-disk via palace-codemap `read_range` this dispatch (`palace/main.cpp:140-328`, `palace/drivers/basesolver.cpp:153-276`, `palace/drivers/basesolver.hpp:31-67`). This is a NOVEL feature sub-kind — a **meta-feature whose constituents include other feature columns** (the per-driver specializations) rather than only vocabulary ops; the surface-or-evidence evidence is the driver-agnostic source range + the specialization-seam site map + the per-driver column down-links. Rotation / variant-axis claims no-op (no rotation, no variant-axis catalogue — the chapter carries only the compositional claim).
