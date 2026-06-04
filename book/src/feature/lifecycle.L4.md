---
kind: feature-surface
feature: lifecycle
level: L4
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: L4/fold_solve
      kind: composes
    - target: palace/main.cpp:158-328
      kind: cites-evidence
    - target: palace/drivers/basesolver.cpp:153-276
      kind: cites-evidence
  reference:
    - feature/electrostatic.L4
    - feature/magnetostatic.L4
    - feature/eigenmode.L4
    - feature/driven.L4
    - feature/transient.L4
    - feature/boundary-mode.L4
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

2. **Dispatch the per-driver specialization** — `dispatch (problem_type cfg)` selects ONE per-driver feature column by `ProblemType`. This is the **specialization seam**: the lifecycle root composes the *feature column*, and each column is itself a full composition root one level down. On disk this cycle: [`electrostatic.L4`](./electrostatic.L4.md) (the `ELECTROSTATIC` branch), [`magnetostatic.L4`](./magnetostatic.L4.md) (the `MAGNETOSTATIC` branch), [`eigenmode.L4`](./eigenmode.L4.md) (the `EIGENMODE` branch), [`driven.L4`](./driven.L4.md) (the `DRIVEN` branch), and [`transient.L4`](./transient.L4.md) (the `TRANSIENT` branch). L0: the `switch (iodata.problem.type)` (`palace/main.cpp:257-280`): `ELECTROSTATIC` `:267`, `MAGNETOSTATIC` `:270`, `EIGENMODE` `:264`, `DRIVEN` `:261`, `TRANSIENT` `:273`, `BOUNDARYMODE` `:276`.

3. **Adaptive estimate-mark-refine outer fold** — [`fold_solve`](../L4/fold_solve.md) (**firm**), in its **state-generated `schedule-source`** form. The L4 state-threaded fold combinator threads the mesh-sequence carry `{mesh, indicators, ntdof, err}` forward: each iterate runs the selected driver `step` (→ indicators + the current product), then **marks** + **refines** + (optionally) **rebalances** the mesh to produce the next iterate, terminating when the indicator norm falls below tolerance or resources exhaust. This is `fold_solve`'s **state-generated** `schedule-source` axis value — the carry GENERATES the next input + the loop bound from accumulated state (the same axis value as the driven-PROM SweepAdaptive witness, `fold_solve.md` §variant-axes), NOT the fixed-list transient form. The carry-threading sequential-obstruction holds (each iterate's input is the prior iterate's output; the iterates do NOT commute — a fold, not a [`solve_family`](../L4/solve_family.md) map). When AMR is disabled (`refinement.max_it == 0`) the fold degenerates to the single initial `Solve` — the [`electrostatic.L4`](./electrostatic.L4.md) exemplar's case. L0: `BaseSolver::SolveEstimateMarkRefine` (`palace/drivers/basesolver.cpp:153-276`): the initial solve `:174`, the `while` carry `:190`, mark `:221-232`, refine `:235-244`, re-solve `:266`.

## Inputs / outputs (the feature surface)

- **Input — config.** `Config` (the `IoData` surface): `problem.type` (→ the driver dispatch discriminant, `palace/main.cpp:258`), the mesh + order (→ `build_mesh`), the per-driver material/boundary/source config (→ the selected column), the refinement config (→ the `fold_solve` mark/refine/terminate, `palace/drivers/basesolver.cpp:154`). All `readonly` construction-stratum inputs; only the mesh-sequence carry threads through the fold. L0 home: `IoData iodata(argv[1], false)` (`palace/main.cpp:231`).
- **Output — the physical product.** `Product` — the driver-selected physical product, a sum over the five per-driver products discriminated by `ProblemType` (capacitance | inductance | S-params | eigenfreq + Q | fields). The lifecycle root's output is exactly what the user ran Palace to compute; `main` itself writes only run metadata (`SaveMetadata`, `palace/main.cpp:314-316`), the product is the selected driver column's output.

## Why this is the spine ROOT (and a novel sub-kind)

The lifecycle root is the **spine ROOT**: every per-driver feature column is a *specialization* of this one composition. It is a **meta-feature** — its stage (2) constituent is not a vocabulary combinator but **another feature column**. Two of those columns are on disk this cycle (electrostatic, magnetostatic); the lifecycle root composes them by canonical slug and forward-references the three not-yet-authored columns in plain text. The driver-agnostic stages (1) mesh-build + (3) the adaptive fold are firm: stage (3) IS the firm [`fold_solve`](../L4/fold_solve.md) in its state-generated form (no new combinator needed — the AMR loop is exactly the `schedule-source = state-generated` axis value the `fold_solve` SweepAdaptive witness already covers).

The whole run therefore lowers cleanly outward to the L4 backend surface as `lifecycle = fold_solve (dispatch (problem_type cfg)) ∘ build_mesh` — a fold over driver specializations, the form an external GPU-tensor / distributed backend wants to consume (the feature spine ROOT, not the unfolded `main` + the virtual-dispatch driver loop).

## Constituent down-links

| Stage | L4 constituent | Status | L0 site |
|---|---|---|---|
| build mesh | driver-agnostic mesh scaffold (`mesh::Load`/`Partition`/`RefineMesh`) | — (L0 scaffold) | `palace/main.cpp:287-302` |
| dispatch → electrostatic column | [`electrostatic.L4`](./electrostatic.L4.md) (sibling reference) | firm | `palace/main.cpp:267` |
| dispatch → magnetostatic column | [`magnetostatic.L4`](./magnetostatic.L4.md) (sibling reference) | firm | `palace/main.cpp:270` |
| dispatch → eigenmode / driven / transient / boundary-mode columns | [eigenmode.L4](./eigenmode.L4.md) / [driven.L4](./driven.L4.md) / [transient.L4](./transient.L4.md) / [boundary-mode.L4](./boundary-mode.L4.md) (sibling references) | firm / firm / firm / rough-in | `palace/main.cpp:264, 261, 273, 276` |
| adaptive estimate-mark-refine fold | [`fold_solve`](../L4/fold_solve.md) (state-generated `schedule-source`) | firm | `palace/drivers/basesolver.cpp:153-276` |

## Status

`firm` — the spine ROOT composition root, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the first **meta-feature** of the feature-surface kind (constituents include other feature columns, not only vocabulary combinators).

**Promotion under the OWN-COMPOSITION rule** (USER DIRECTIVE 2026-06-03; CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE). This column promotes off `seed` because its **OWN driver-agnostic composition + its directly-owned constituents** are firm; the per-driver dispatch (stage 2) is over **sibling feature columns**, which are **references, NOT blocking constituents** (the spine-ROOT sub-kind: stage-(2) constituents are *other feature columns*). The directly-owned driver-agnostic constituents are: the mesh-build L0 scaffold (stage 1) + the firm [`fold_solve`](../L4/fold_solve.md) state-generated adaptive estimate-mark-refine outer fold (stage 3) — verified firm from `fold_solve.md` frontmatter `firmness: firm` on-disk this dispatch. The per-driver columns ([`electrostatic.L4`](./electrostatic.L4.md), [`magnetostatic.L4`](./magnetostatic.L4.md), [`eigenmode.L4`](./eigenmode.L4.md), [`driven.L4`](./driven.L4.md), [`transient.L4`](./transient.L4.md)) are the specializations this ROOT dispatches over; their own `status:` does not gate the ROOT's (each promotes on its own composition, the reciprocal of this rule). This supersedes the earlier "promote past `seed` only once all five driver columns are firm" gating, which (with the directive-3 reciprocal cross-linking) created the mutual-blocking `seed` deadlock the directive exists to break.

This chapter carries the *compositional* claim only (lifecycle = adaptive-fold-over-driver-dispatch), not the per-column or per-op claims (those live in the linked columns / chapters). Evidence: the L0 driver-agnostic range `palace/main.cpp:158-328` + `palace/drivers/basesolver.cpp:153-276` realizing the composition, plus the firm [`fold_solve`](../L4/fold_solve.md) constituent down-link + the per-driver column down-links. Rotation / variant-axis claims no-op (no rotation, no variant-axis catalogue — the compositional claim only).
