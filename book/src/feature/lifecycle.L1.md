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
  - palace/main.cpp:158-328 (main — the top-level lifecycle)
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
| build mesh | `mesh::Load`/`Partition`/`RefineMesh` (driver-agnostic mesh scaffold) | — (L0 scaffold) | `palace/main.cpp:287-302` |
| per-driver dispatch (electrostatic) | [`electrostatic.L1`](./electrostatic.L1.md) | seed (exemplar) | `palace/main.cpp:267` |
| per-driver dispatch (magnetostatic) | [`magnetostatic.L1`](./magnetostatic.L1.md) | seed (exemplar) | `palace/main.cpp:270` |
| per-driver dispatch (eigenmode / driven / transient) | eigenmode.L1 / driven.L1 / transient.L1 *(forthcoming — not yet authored)* | not yet authored | `palace/main.cpp:264, 261, 273` |
| adaptive estimate-mark-refine fold | the `fold_solve` state-generated carry (see L4) | firm (L4) | `palace/drivers/basesolver.cpp:153-276` |

## Status

`seed (composition-root)` — the L1 pure-function composition root for the lifecycle meta-feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: the mesh-build + estimate-mark-refine fold are driver-agnostic scaffold (the fold is the firm [`fold_solve`](../L4/fold_solve.md) state-generated shape at L4); the per-driver dispatch composes the per-column pure functions (2 on disk — [`electrostatic.L1`](./electrostatic.L1.md), [`magnetostatic.L1`](./magnetostatic.L1.md); 3 forthcoming). This chapter carries the compositional claim only (lifecycle = dispatch-over-driver-columns under the adaptive fold), not the per-column algebraic claims (those live in the per-driver columns) nor the per-op claims (those live in the vocabulary chapters). Evidence: the L0 driver-agnostic range `palace/main.cpp:158-328` + `palace/drivers/basesolver.cpp:153-276` realizing the composition, plus the per-driver column down-links.
