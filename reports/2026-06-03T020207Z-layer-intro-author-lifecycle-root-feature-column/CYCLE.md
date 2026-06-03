---
agent: layer-intro-author
invoked_at: 2026-06-03T02:02:07Z
scope: lifecycle-root feature column (feature/lifecycle.{L4,L1,L0}.md) — the composition-root spine ROOT
status: pending
integrated_at: 2026-06-03T024500Z
integration_commit: 7f211f9
integration_notes: |
  Applied clean cycle-072 (D2; staging row 2/3). Created feature/lifecycle.{L4,L1,L0}.md (status seed (composition-root)) ONLY (D1 sole-owns index/SUMMARY; D1 wired the lifecycle SUMMARY rows by canonical slug, now resolving live to these files). The spine ROOT all 5 per-driver columns hang off (first meta-feature; constituents are other feature columns); the AMR estimate-mark-refine outer fold as fold_solve's state-generated schedule-source form (2nd state-generated fold_solve witness). Composes DOWN to electrostatic+magnetostatic (live links) + eigenmode/driven/transient (plain-text). NOTE: the per-report integrator repaired citation OOB/AMBIG in the LANDED files (main.cpp:158-330->:158-328 + bare-basename main.cpp:->palace/main.cpp: qualifications) -- the book surface is clean; this frozen report CYCLE.md (append-only after integration) still shows the original forms, so a --scan of THIS report will report ~13 'failing' that are fully resolved at the artifact level. 3 OQs promoted (feature-surface-meta-feature-root-sub-kind-and-summary-nesting; fold-solve-state-generated-schedule-source-second-witness-amr-loop; boundarymode-is-sixth-problemtype-branch-reconcile-five-drivers-framing). cargo make book exit 0; all lifecycle live-links resolve; linkcheck2 clean. retroactive-budget global 0; no gate hits.
---

# CYCLE: lifecycle-root feature column

## Summary

Authors the **top-level simulation lifecycle root** feature column — the spine ROOT that the 5 per-driver feature columns specialize. This is a NOVEL feature sub-kind: a **meta-feature that composes other features**. Where a per-driver column (electrostatic, magnetostatic) recomposes vocabulary *ops* into a concrete pipeline, the lifecycle root recomposes (a) the driver-agnostic `main` → `BaseSolver` lifecycle scaffold and (b) the per-driver feature columns themselves into the abstract spine: **config → mesh-construction → (per-driver) Solve → estimate-mark-refine → output products**.

Three chapters authored (full bodies in proposed-changes `create:` fences below):
- `book/src/feature/lifecycle.L0.md` — cited driver source (`main.cpp` + `BaseSolver::SolveEstimateMarkRefine`).
- `book/src/feature/lifecycle.L1.md` — pure-function lifecycle surface (config → output products).
- `book/src/feature/lifecycle.L4.md` — composition-root presenting the lifecycle as the outward backend-lowering entry point; the per-driver dispatch links DOWN to the driver columns; the AMR outer loop composes the firm L4 [`fold_solve`](../L4/fold_solve.md) (state-generated `schedule-source`).

**L0 anchors confirmed on-disk** (palace-codemap `read_range`, this dispatch):
- `palace/main.cpp:228-330` — the lifecycle body: config load `iodata(argv[1],false)` (`:231`), output folder (`:232`), device/library init (`:234-252`), the per-driver dispatch `switch(iodata.problem.type)` (`:257-280`), mesh load/preprocess/partition/refine (`:283-302`), the driver run `solver->SolveEstimateMarkRefine(mesh)` (`:304`), timing/metadata finalize (`:306-324`).
- `palace/drivers/basesolver.cpp:153-276` — `BaseSolver::SolveEstimateMarkRefine`: initial `Solve(mesh)` (`:174`) + error norm (`:175`), the AMR `while` loop (`:190`) {mark `:221-232`, refine `:235-244`, rebalance `:247-261`, re-solve `:266-267`}, completion print (`:269-275`).
- `palace/drivers/basesolver.hpp:31-67` — `class BaseSolver`: the pure-virtual driver dispatch `Solve(...) const = 0` (`:43-44`), `Preprocess` (`:53-54`), `SolveEstimateMarkRefine` (`:59`).

**Down-link strategy:**
- Per-driver columns: `electrostatic.{L4,L1,L0}.md` is on-disk (live link); `magnetostatic.{L4,L1,L0}.md` is D1's this-cycle slug (live link by canonical slug — integrator resolves). The 3 un-authored driver columns (eigenmode, driven, transient) are **plain-text forward-references** (not live links — files don't exist; a live link would be a hard `linkcheck2` build error).
- Constituent lifecycle vocabulary: `fold_solve` (L4, firm — verified on-disk `## Status`), `fe_assemble` / `ksp_solve` (firm) linked read-only.

**Critic-framing note (carry into critique):** the surface-or-evidence check ADAPTS for this kind — the feature's "surface" IS the feature, evidenced by the L0 driver-source range (`main.cpp` + `SolveEstimateMarkRefine`) + the constituent down-links. For the lifecycle ROOT specifically the "constituents" include **the per-driver feature columns it composes** (not only vocabulary ops). Rotation-quality and variant-axis checks **no-op** on a feature chapter (like a stub) — there is no rotation claim and no variant-axis catalogue; the chapter carries only the *compositional* claim.

**Index ownership:** DEFERRED to D1 (sole owner of `feature/index.md` + the SUMMARY `# Feature surfaces` block this cycle). My canonical slug for D1 to wire: `feature/lifecycle.{L4,L1,L0}.md`. I do NOT touch `feature/index.md` or SUMMARY.

## Proposed changes

```create:book/src/feature/lifecycle.L0.md
---
kind: feature-surface
feature: lifecycle
level: L0
status: seed (composition-root)
l0_ground_truth:
  - palace/main.cpp:158-330 (main — the top-level lifecycle: parse, configure, dispatch driver, build mesh, run, finalize)
  - palace/drivers/basesolver.cpp:153-276 (BaseSolver::SolveEstimateMarkRefine — the solve-estimate-mark-refine adaptive outer loop)
  - palace/drivers/basesolver.hpp:31-67 (class BaseSolver — the pure-virtual driver dispatch + the AMR wrapper)
lifts_to:
  - book/src/feature/lifecycle.L1.md (the L1 pure-function lifecycle root)
specializes_to:
  - book/src/feature/electrostatic.L0.md (the electrostatic driver — one ProblemType specialization)
  - book/src/feature/magnetostatic.L0.md (the magnetostatic driver — one ProblemType specialization)
---

# lifecycle — L0 ground-truth surface

The **top-level simulation lifecycle** at L0: the cited Palace source that realizes the composition-root *spine* — `main` (`palace/main.cpp:158-330`) and the adaptive driver wrapper `BaseSolver::SolveEstimateMarkRefine` (`palace/drivers/basesolver.cpp:153-276`). This is the **meta-feature**: the driver-agnostic lifecycle (config → mesh → per-driver solve → estimate-mark-refine → output) that the 5 per-driver feature columns specialize. Every claim is a `(file:start-end)` citation.

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

`seed (composition-root)` — the L0 ground-truth surface for the top-level lifecycle meta-feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). Every stage is a cited range into `palace/main.cpp` + `palace/drivers/basesolver.cpp` / `.hpp`, confirmed on-disk via palace-codemap `read_range` this dispatch (`main.cpp:140-330`, `basesolver.cpp:153-276`, `basesolver.hpp:31-67`). This is a NOVEL feature sub-kind — a **meta-feature whose constituents include other feature columns** (the per-driver specializations) rather than only vocabulary ops; the surface-or-evidence evidence is the driver-agnostic source range + the specialization-seam site map + the per-driver column down-links. Rotation / variant-axis claims no-op (no rotation, no variant-axis catalogue — the chapter carries only the compositional claim).
```

```create:book/src/feature/lifecycle.L1.md
---
kind: feature-surface
feature: lifecycle
level: L1
status: seed (composition-root)
composes:
  - book/src/feature/electrostatic.L1.md (the electrostatic driver — one ProblemType specialization)
  - book/src/feature/magnetostatic.L1.md (the magnetostatic driver — one ProblemType specialization)
  - book/src/L1/fe_assemble.md (firm — driver-agnostic mesh→operator assemble, used by every driver)
  - book/src/L1/ksp_solve.md (firm — the solve cap every driver's per-step body bottoms out in)
l0_ground_truth:
  - palace/main.cpp:158-330 (main — the top-level lifecycle)
  - palace/drivers/basesolver.cpp:153-276 (BaseSolver::SolveEstimateMarkRefine)
---

# lifecycle — L1 composition-root

The **top-level simulation lifecycle** at L1, presented as a pure function `config → output products`. This is the **meta-feature** pure-function surface: where a per-driver L1 column (e.g. [`electrostatic.L1`](./electrostatic.L1.md)) is a concrete `config → capacitance` pure function, the lifecycle root is the **abstract spine** — a driver-agnostic `config → product` pure function that **dispatches** to the per-driver column selected by the config's problem type, all of it run under the adaptive estimate-mark-refine outer loop.

At L1 the lifecycle is a pure function with the mutation already lifted (the L0 in-place mesh refinement + the driver's in-place solves are lifted to value-returning forms per the constituent ops' L1>L0 mutation rotations).

## The composition

    -- inputs = config; output = the physical product (driver-selected)
    lifecycle :: Config -> Product
    lifecycle cfg =
      let mesh0 = build_mesh cfg                          -- (1) load + partition + a-priori-refine
          drv   = dispatch (problem_type cfg)             -- (2) select the per-driver column by ProblemType
          step  = \m -> drv cfg m                         --     one driver Solve = one feature-column body
      in  estimate_mark_refine_fold step mesh0            -- (3) adaptive outer fold → final product

1. **Build the mesh** — a driver-agnostic pure `build_mesh :: Config -> Mesh` (load → preprocess → partition → a-priori-refine). Pure: consumes config, produces the initial mesh sequence. L0: `mesh::Load` / `Preprocess` / `Partition` / `RefineMesh` (`palace/main.cpp:287-302`).

2. **Dispatch the per-driver specialization** — `dispatch :: ProblemType -> (Config -> Mesh -> Product)` selects ONE per-driver feature column by `problem_type cfg`. Each branch is a per-driver feature column's L1 root: [`electrostatic.L1`](./electrostatic.L1.md), [`magnetostatic.L1`](./magnetostatic.L1.md) on disk; eigenmode / driven / transient forthcoming (not yet authored). The selected driver `Solve` is the **specialization** of this spine — the lifecycle composes the *column*, not the column's internal ops (those are the column's own down-links). L0: the `switch (iodata.problem.type)` (`palace/main.cpp:257-280`).

3. **Adaptive estimate-mark-refine fold** — `estimate_mark_refine_fold :: (Mesh -> (Indicators, Product)) -> Mesh -> Product`: thread the mesh forward, at each iterate running the selected driver `Solve` (→ error indicators + the current product), then **mark** the high-error elements + **refine** + (optional) **rebalance** → the next mesh, terminating when the error indicator norm falls below tolerance OR resources are exhausted. The carry `{mesh, indicators, product}` is **state-generated** (the carry both produces the next mesh AND determines termination), so each iterate's input is the prior iterate's output — a **fold, not a map** (no commuting family). When AMR is disabled the fold is the single initial `Solve` (the electrostatic exemplar's degenerate case). L0: `BaseSolver::SolveEstimateMarkRefine` (`palace/drivers/basesolver.cpp:153-276`): initial solve `:174`, the `while` `:190`, mark `:221-232`, refine `:235-244`, re-solve `:266`.

## Inputs / outputs (the feature surface)

- **Input — config.** `Config` (the `IoData` surface): the problem type (→ driver dispatch), the mesh + order (→ `build_mesh`), the material + boundary + source config (→ the selected driver), the refinement config (→ the fold's mark/refine/terminate). All read-only.
- **Output — the physical product.** `Product` — the driver-selected physical product (capacitance for electrostatic, inductance for magnetostatic, S-params for driven, eigenfreq + Q for eigenmode, fields for transient). The lifecycle root's output type is the *sum* over the per-driver products, discriminated by `ProblemType`.

## L1 vs L4

The L1 and L4 lifecycle roots express the **same meta-feature**; they differ in vocabulary:
- **L1** (this chapter): the per-driver dispatch is an explicit `dispatch (problem_type cfg)` selecting a per-column pure function; the adaptive loop is an explicit recursive `estimate_mark_refine_fold` threading the mesh.
- **L4** ([`lifecycle.L4`](./lifecycle.L4.md)): the adaptive loop is the firm [`fold_solve`](../L4/fold_solve.md) combinator's **state-generated `schedule-source`** form (the carry generates the next iterate + the termination bound — the same axis value as driven-PROM SweepAdaptive); the per-driver dispatch links DOWN to the driver columns as the spine's specializations.

The L1→L0 direction (how the mesh-refine + driver solves lower to the in-place driver writes) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 constituent | Status | L0 site |
|---|---|---|---|
| build mesh | `mesh::Load`/`Partition`/`RefineMesh` (driver-agnostic mesh scaffold) | — (L0 scaffold) | `main.cpp:287-302` |
| per-driver dispatch (electrostatic) | [`electrostatic.L1`](./electrostatic.L1.md) | seed (exemplar) | `main.cpp:267` |
| per-driver dispatch (magnetostatic) | [`magnetostatic.L1`](./magnetostatic.L1.md) | seed (exemplar) | `main.cpp:270` |
| per-driver dispatch (eigenmode / driven / transient) | eigenmode.L1 / driven.L1 / transient.L1 *(forthcoming — not yet authored)* | not yet authored | `main.cpp:264, 261, 273` |
| adaptive estimate-mark-refine fold | the `fold_solve` state-generated carry (see L4) | firm (L4) | `basesolver.cpp:153-276` |

## Status

`seed (composition-root)` — the L1 pure-function composition root for the lifecycle meta-feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: the mesh-build + estimate-mark-refine fold are driver-agnostic scaffold (the fold is the firm [`fold_solve`](../L4/fold_solve.md) state-generated shape at L4); the per-driver dispatch composes the per-column pure functions (2 on disk — [`electrostatic.L1`](./electrostatic.L1.md), [`magnetostatic.L1`](./magnetostatic.L1.md); 3 forthcoming). This chapter carries the compositional claim only (lifecycle = dispatch-over-driver-columns under the adaptive fold), not the per-column algebraic claims (those live in the per-driver columns) nor the per-op claims (those live in the vocabulary chapters). Evidence: the L0 driver-agnostic range `main.cpp:158-330` + `basesolver.cpp:153-276` realizing the composition, plus the per-driver column down-links.
```

```create:book/src/feature/lifecycle.L4.md
---
kind: feature-surface
feature: lifecycle
level: L4
status: seed (composition-root)
composes:
  - book/src/feature/electrostatic.L4.md (seed (exemplar) — the ELECTROSTATIC ProblemType specialization)
  - book/src/feature/magnetostatic.L4.md (seed (exemplar) — the MAGNETOSTATIC ProblemType specialization)
  - book/src/L4/fold_solve.md (firm — the state-generated adaptive estimate-mark-refine outer fold)
l0_ground_truth:
  - palace/main.cpp:158-330 (main — the top-level lifecycle)
  - palace/drivers/basesolver.cpp:153-276 (BaseSolver::SolveEstimateMarkRefine)
---

# lifecycle — L4 composition-root

The **top-level simulation lifecycle**, presented at L4 as the **spine ROOT** — the composition root that the 5 per-driver feature columns specialize. This is the **outward backend-lowering entry point** for a whole Palace run: `config → physical product`. It is a NOVEL feature sub-kind — a **meta-feature whose constituents include other feature columns** (the per-driver specializations) rather than only vocabulary combinators. It does not introduce a new combinator; it wires the driver-agnostic lifecycle scaffold + the firm L4 [`fold_solve`](../L4/fold_solve.md) outer fold + a dispatch over the per-driver columns, and links DOWN to each.

Where the [`electrostatic.L4`](./electrostatic.L4.md) column is a concrete three-stage pipeline (`fe_assemble` → `solve_family` → capacitance-reduce), the lifecycle root is the **abstract spine** above all five: it presents the common `config → mesh → (per-driver) Solve → estimate-mark-refine → product` composition and **dispatches** to the driver column selected by the config's problem type.

## The composition

At L4 the whole run is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the physical product (driver-selected)
    lifecycle :: Config -> Product
    lifecycle cfg =
      let mesh0 = build_mesh cfg                          -- (1) mesh scaffold: load + partition + a-priori-refine
          drv   = dispatch (problem_type cfg)             -- (2) select the per-driver feature column
          step  = \m -> drv cfg m                         --     one driver Solve = one feature-column body
      in  fold_solve step mesh0                           -- (3) adaptive estimate-mark-refine outer fold → product

Three composed stages, each a link DOWN to firm L4 vocabulary or to a per-driver feature column:

1. **Build the mesh (driver-agnostic scaffold).** `build_mesh cfg` loads, preprocesses, partitions, and a-priori-refines the mesh sequence — the `readonly` construction stratum every driver consumes. L0: `mesh::Load` / `Preprocess` / `Partition` / `RefineMesh` (`palace/main.cpp:287-302`).

2. **Dispatch the per-driver specialization** — `dispatch (problem_type cfg)` selects ONE per-driver feature column by `ProblemType`. This is the **specialization seam**: the lifecycle root composes the *feature column*, and each column is itself a full composition root one level down. On disk this cycle: [`electrostatic.L4`](./electrostatic.L4.md) (the `ELECTROSTATIC` branch) and [`magnetostatic.L4`](./magnetostatic.L4.md) (the `MAGNETOSTATIC` branch). The other three branches — eigenmode, driven, transient — are forthcoming feature columns (not yet authored). L0: the `switch (iodata.problem.type)` (`palace/main.cpp:257-280`): `ELECTROSTATIC` `:267`, `MAGNETOSTATIC` `:270`, `EIGENMODE` `:264`, `DRIVEN` `:261`, `TRANSIENT` `:273`, `BOUNDARYMODE` `:276`.

3. **Adaptive estimate-mark-refine outer fold** — [`fold_solve`](../L4/fold_solve.md) (**firm**), in its **state-generated `schedule-source`** form. The L4 state-threaded fold combinator threads the mesh-sequence carry `{mesh, indicators, ntdof, err}` forward: each iterate runs the selected driver `step` (→ indicators + the current product), then **marks** + **refines** + (optionally) **rebalances** the mesh to produce the next iterate, terminating when the indicator norm falls below tolerance or resources exhaust. This is `fold_solve`'s **state-generated** `schedule-source` axis value — the carry GENERATES the next input + the loop bound from accumulated state (the same axis value as the driven-PROM SweepAdaptive witness, `fold_solve.md` §variant-axes), NOT the fixed-list transient form. The carry-threading sequential-obstruction holds (each iterate's input is the prior iterate's output; the iterates do NOT commute — a fold, not a [`solve_family`](../L4/solve_family.md) map). When AMR is disabled (`refinement.max_it == 0`) the fold degenerates to the single initial `Solve` — the [`electrostatic.L4`](./electrostatic.L4.md) exemplar's case. L0: `BaseSolver::SolveEstimateMarkRefine` (`palace/drivers/basesolver.cpp:153-276`): the initial solve `:174`, the `while` carry `:190`, mark `:221-232`, refine `:235-244`, re-solve `:266`.

## Inputs / outputs (the feature surface)

- **Input — config.** `Config` (the `IoData` surface): `problem.type` (→ the driver dispatch discriminant, `main.cpp:258`), the mesh + order (→ `build_mesh`), the per-driver material/boundary/source config (→ the selected column), the refinement config (→ the `fold_solve` mark/refine/terminate, `basesolver.cpp:154`). All `readonly` construction-stratum inputs; only the mesh-sequence carry threads through the fold. L0 home: `IoData iodata(argv[1], false)` (`main.cpp:231`).
- **Output — the physical product.** `Product` — the driver-selected physical product, a sum over the five per-driver products discriminated by `ProblemType` (capacitance | inductance | S-params | eigenfreq + Q | fields). The lifecycle root's output is exactly what the user ran Palace to compute; `main` itself writes only run metadata (`SaveMetadata`, `main.cpp:314-316`), the product is the selected driver column's output.

## Why this is the spine ROOT (and a novel sub-kind)

The lifecycle root is the **spine ROOT**: every per-driver feature column is a *specialization* of this one composition. It is a **meta-feature** — its stage (2) constituent is not a vocabulary combinator but **another feature column**. Two of those columns are on disk this cycle (electrostatic, magnetostatic); the lifecycle root composes them by canonical slug and forward-references the three not-yet-authored columns in plain text. The driver-agnostic stages (1) mesh-build + (3) the adaptive fold are firm: stage (3) IS the firm [`fold_solve`](../L4/fold_solve.md) in its state-generated form (no new combinator needed — the AMR loop is exactly the `schedule-source = state-generated` axis value the `fold_solve` SweepAdaptive witness already covers).

The whole run therefore lowers cleanly outward to the L4 backend surface as `lifecycle = fold_solve (dispatch (problem_type cfg)) ∘ build_mesh` — a fold over driver specializations, the form an external GPU-tensor / distributed backend wants to consume (the feature spine ROOT, not the unfolded `main` + the virtual-dispatch driver loop).

## Constituent down-links

| Stage | L4 constituent | Status | L0 site |
|---|---|---|---|
| build mesh | driver-agnostic mesh scaffold (`mesh::Load`/`Partition`/`RefineMesh`) | — (L0 scaffold) | `main.cpp:287-302` |
| dispatch → electrostatic column | [`electrostatic.L4`](./electrostatic.L4.md) | seed (exemplar) | `main.cpp:267` |
| dispatch → magnetostatic column | [`magnetostatic.L4`](./magnetostatic.L4.md) | seed (exemplar) | `main.cpp:270` |
| dispatch → eigenmode / driven / transient columns | eigenmode.L4 / driven.L4 / transient.L4 *(forthcoming — not yet authored)* | not yet authored | `main.cpp:264, 261, 273` |
| adaptive estimate-mark-refine fold | [`fold_solve`](../L4/fold_solve.md) (state-generated `schedule-source`) | firm | `basesolver.cpp:153-276` |

## Status

`seed (composition-root)` — the spine ROOT composition root, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the first **meta-feature** of the feature-surface kind (constituents include other feature columns, not only vocabulary combinators). The composition is sound: the mesh-build + adaptive-fold stages are driver-agnostic, and stage (3) IS the firm [`fold_solve`](../L4/fold_solve.md) in its state-generated `schedule-source` form (verified firm from on-disk `## Status` this dispatch); stage (2) dispatches over the per-driver feature columns ([`electrostatic.L4`](./electrostatic.L4.md), [`magnetostatic.L4`](./magnetostatic.L4.md) on disk; eigenmode/driven/transient forthcoming, plain-text). This chapter carries the *compositional* claim only (lifecycle = adaptive-fold-over-driver-dispatch), not the per-column or per-op claims (those live in the linked columns / chapters). Evidence: the L0 driver-agnostic range `main.cpp:158-330` + `basesolver.cpp:153-276` realizing the composition, plus the firm [`fold_solve`](../L4/fold_solve.md) constituent down-link + the per-driver column down-links. Rotation / variant-axis claims no-op (no rotation, no variant-axis catalogue — the compositional claim only).
```

## Supporting evidence

- **L0 ground truth confirmed on-disk** (palace-codemap `read_range`, this dispatch):
  - `palace/main.cpp:140-330` read — confirms `main` at `:158`, config-load `:231`, output-folder `:232`, device/library config `:234-252`, the `switch(iodata.problem.type)` driver dispatch `:257-280` (all 6 ProblemType branches confirmed verbatim), mesh build `:283-302`, `solver->SolveEstimateMarkRefine(mesh)` `:304`, finalize `:306-324`.
  - `palace/drivers/basesolver.cpp:153-276` read — confirms `SolveEstimateMarkRefine` body: `use_amr` guard `:155-164`, initial `Solve(mesh)` `:174` + `Norml2` `:175`, `ExhaustedResources` `:177-184`, the AMR `while` `:190`, mark (Dörfler) `:221-232`, refine `:235-244`, rebalance `:247-261`, re-solve `:266-267`, completion print `:269-275`.
  - `palace/drivers/basesolver.hpp:31-67` read — confirms `class BaseSolver` `:31`, the pure-virtual `Solve(...) const = 0` `:43-44` (the specialization seam), `Preprocess` virtual `:53-54`, `SolveEstimateMarkRefine` `:59`.
- **Constituent firmness verified from on-disk `## Status`** (not from cycle record or index cells):
  - `book/src/L4/fold_solve.md` — `## Status: firm` (firm-on-positive-structure escape; 2-of-5 fold witnesses transient + driven-PROM SweepAdaptive; the **state-generated `schedule-source`** axis value is exactly the AMR loop shape). This is the load-bearing down-link for stage (3) and it is genuinely firm on disk.
  - `book/src/L1/fe_assemble.md`, `book/src/L1/ksp_solve.md` — both `## Status: firm` (referenced as driver-agnostic vocabulary).
  - `book/src/feature/electrostatic.{L4,L1,L0}.md` — on disk, `seed (exemplar)`; live-linked as the `ELECTROSTATIC` specialization.
- **Down-link convention honored:** electrostatic (on disk) + magnetostatic (D1's slug this cycle) are live links by canonical slug; eigenmode / driven / transient are **plain-text** forward-references (files don't exist — a live link is a hard `linkcheck2` error per friction-ledger `rough-in-rows-must-be-plain-text-when-anchor-missing`).

## Open questions / caveats

- **NOVEL feature sub-kind: meta-feature composing features (for batch-22 meta-phase).** The lifecycle root is the FIRST feature chapter whose stage-(2) constituent is **another feature column** (the per-driver specializations), not a vocabulary combinator. The electrostatic exemplar's down-link table rows are vocabulary ops (`fe_assemble`, `solve_family`, …); the lifecycle root's stage-(2) rows are *feature columns* (`electrostatic.L4`, `magnetostatic.L4`). This needs a name in the batch-22 codification of the feature-surface kind (suggest: **composition-root spine ROOT** / **meta-feature** sub-kind, vs. the per-driver **leaf feature column** sub-kind). The critic's surface-or-evidence adaptation extends naturally (constituents = feature columns + the driver-agnostic fold), but the by-kind grouping (directive-3) should likely nest the ROOT *above* the per-driver columns in the Feature Part's SUMMARY ordering — flagged for D1 (index owner) + the meta-phase.
- **`status: seed (composition-root)` vs `seed (exemplar)`.** I used a distinct status string `seed (composition-root)` for the ROOT to mark the meta-feature sub-kind (the per-driver columns use `seed (exemplar)`). If the meta-phase prefers a single `seed` umbrella string, this is a trivial rename — flagged so the chapter-kind status vocabulary is codified consistently in batch-22.
- **The `fold_solve` state-generated `schedule-source` axis now has a SECOND witness.** Before this cycle, `fold_solve`'s state-generated form was witnessed only by driven-PROM SweepAdaptive (`drivensolver.cpp:231-398`). The AMR `SolveEstimateMarkRefine` loop (`basesolver.cpp:153-276`) is a **second, driver-agnostic** state-generated-fold witness (the carry generates the next mesh + the termination bound). This strengthens `fold_solve`'s state-generated axis from 1 to 2 witnesses and suggests the OQ `fold-solve-greedy-schedule-source-generalization` (whether the state-generated form warrants its own dedicated combinator) now has more evidence to weigh — flagged for the meta-phase / a future `fold_solve` lifter. I did NOT edit `fold_solve.md` (read-only down-link; out of my one-chapter-column scope).
- **`BoundaryModeSolver` is a 6th `ProblemType` branch** (`main.cpp:276`) beyond the "5 sim drivers" framing. The FEATURE-SURFACE SPINE directive scope names "5 sim drivers + wave-port/boundary-mode" separately; `BOUNDARYMODE` dispatches like the others through the same `switch`, so the lifecycle root composes it identically (it is a 6th specialization branch, plain-text forward-referenced alongside eigenmode/driven/transient). Noted so the directive-scope's "5 drivers + boundary-mode" split is reconciled when those columns land.
- **Mesh-build stage has no firm vocabulary home yet.** Stage (1) `build_mesh` (`mesh::Load`/`Partition`/`RefineMesh`, `main.cpp:287-302`) is cited as L0 scaffold with no L1/L4 vocabulary chapter (the FE-assembly/mesh cohort is the stranded-at-L1 hole per memory `project_l4_is_backend_lowering_target`). I left it as an L0-scaffold row (no down-link) rather than forcing a vocabulary chapter that doesn't exist. When the mesh-construction cohort firms up, this row gains a down-link — flagged for the planner as a foundation-gap the lifecycle root surfaces.
