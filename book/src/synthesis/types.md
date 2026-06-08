---
kind: navigational-container (synthesis library — types)
# Navigational container, not a DAG node: no `rank:`. This library RENDERS the
# synthesized form of shared record types; the authoritative defs (with their
# L0 `depends-on` evidence edges) live in the linked `concepts/<record>.md`
# pages. The rendering carries `reference` edges to those homes — it re-cites
# nothing (the concept page owns the citation) and constrains no rank/liveness.
edges:
  reference:
    - concepts/config-record
    - concepts/sim-state
    - concepts/op-params
    - synthesis/index
---

# Library `types` — shared cross-cutting type defs

The foundational bracket of the [Synthesis](./index.md) library partition: the **genuinely shared / cross-cutting** record/type defs — the types referenced across **≥2** of the implementation-API groups (`iteration` / `data-algebra` / `coordination` / `drivers`). They are rendered here, ahead of all the groups that use them, so the overall library order stays topological (a type precedes its consumers).

This is a rendered library chapter (the implementation VIEW), **not** a record-definition page. Each type's authoritative field schema — fields, types, meaning, construction-vs-run-time stratum, L0 source home — lives ONCE in its [`concepts/`](../concepts/index.md) record-definition page (semantic-consolidation: define once). This chapter renders the **synthesized type-def form** in the L4 pseudo-language with a code-doc block, and **links** to the authoritative home. It does not restate field semantics and does not re-cite L0.

> **Type placement (the rule that scopes this library).** Only types shared across **≥2** API groups live here. A type that **clusters with one** API group (e.g. `Krylov` / `StepOutputs` / `PrevCarry` ↔ `iteration`; `DofSet` / `WaveguideModeTable` ↔ `data-algebra`; `SolveResult` / `EigState` ↔ `coordination`; a per-driver config record ↔ its `drivers` column) is placed **immediately before that API group**, bundled with the type's utility API — see the [Synthesis overview](./index.md#type-placement--cluster-a-type-with-its-api-group). This library holds only the cross-cutting remainder.

The three cross-cutting types, in topological order (`IoData` first — it is the construction-time input every solve reads; `OpParams` and `SimState` are the construction-time-readonly and run-time-evolved strata both the iteration kernel and the coordination caps thread):

## `IoData` — the parsed configuration record

Shared across **every** `drivers` column and the `coordination` caps (every solve reads it). The single immutable **construction-stratum** input — one object, parsed once from the user's JSON config, that selects the driver (`problem.type`) and supplies mesh / materials / boundaries / solver knobs. Authoritative field schema: [`config-record`](../concepts/config-record.md).

```text
-- The aggregate parsed once at startup; readonly across the whole solve.
-- Authoritative schema + field strata + L0 home: concepts/config-record.md
-- The five sub-record type names below are the synthesized (clean-room) renderings
-- of the authoritative `config::*Data` types, plus the `Units` scale converter
-- (config-record.md:69-74):
--   ProblemConfig ≡ config::ProblemData,  ModelConfig ≡ config::ModelData,
--   DomainConfig  ≡ config::DomainData,   BoundaryConfig ≡ config::BoundaryData,
--   SolverConfig  ≡ config::SolverData.
IoData = {
  problem    : ProblemConfig,     -- driver selector (problem.type) + solver-pipeline knobs
  model      : ModelConfig,       -- mesh file + refinement + material assignment
  domains    : DomainConfig,      -- per-domain materials + postprocessing energy regions
  boundaries : BoundaryConfig,    -- BC surfaces (PEC/PMC/impedance/lumped-port/wave-port/…)
  solver     : SolverConfig,      -- linear/eigen/driven/transient solver settings + tolerances
  units      : Units              -- SI ↔ nondimensional scale converter (set by nondimensionalization)
}

-- # Arguments / # Returns (utility API — construction-stratum only)
-- parseConfig :: FilePath -> IoData          -- parse the JSON config tree once
-- problemType :: IoData -> ProblemType       -- the driver-dispatch selector (a trivial projection)
```

## `OpParams` — operator-internal parameters (construction-time, readonly)

Shared across `iteration` (the `krylov-step` kernel reads it through closed-over surfaces) and `coordination` (`ksp_solve` / `solve_family` / `fold_solve` capture it once at solve construction). The readonly variant-selector + constructed-operator-surface closure, fixed across the whole `Mult` call. Authoritative field schema: [`op-params`](../concepts/op-params.md).

```text
-- readonly; captured once at solve construction, never re-inspected per step.
-- Authoritative schema + field strata + L0 home: concepts/op-params.md
OpParams = {
  -- constructed-operator surfaces (the kernel touches OpParams ONLY through these)
  T          : ConstructedOp,        -- the apply surface (preconditioned operator)
  orthog?    : OrthogSurface,        -- GMRES/Arnoldi only; absent (no-op) for CG
  scalars?   : ScalarSurface,        -- Chebyshev polynomial-recurrence scalars; absent otherwise
  eps        : Convergence,          -- the stopping-predicate surface

  -- variant selectors (closed over by the surfaces above; not read by the kernel body)
  pc_side    : PreconditionerSide,
  gs_orthog  : Orthogonalization,
  flexible   : Bool,
  poly_kind? : PolynomialKind,
  restart    : RestartMode,

  -- termination knobs (close into eps)
  max_dim    : Int,
  max_it     : Int,
  rel_tol    : Scalar,
  abs_tol    : Scalar
}
```

## `SimState` — sim-state stratum (run-time-evolved)

Shared across `iteration` (the `krylov-step` kernel's monadic effect *is* the `SimState` transition) and `coordination` (the `Solve = StateT SimState Identity` caps thread it; `solve_family` collects it). The externally-visible quantities a Krylov-shaped solve evolves and reports; **uniform across all slices** (CG / GMRES / FGMRES / Chebyshev share this exact five-field shape). Authoritative field schema: [`sim-state`](../concepts/sim-state.md).

```text
-- the value threaded by `Solve a = StateT SimState Identity a`; every field run-time.
-- the iterate `x` is named with shape group S (semantics/index.md §1.2.1), not a rank-1 axis.
-- Authoritative schema + field strata + L0 home: concepts/sim-state.md
SimState = {
  x           : Tensor[(S: ...)],   -- the current iterate (the solve's primary product)
  it          : Int,                -- iteration count
  converged   : Bool,               -- convergence flag
  final_res   : Scalar,             -- final (absolute) residual, possibly an estimate
  initial_res : Scalar              -- initial (absolute) residual, captured at solve entry
}
```

The `Solve` monad (`Solve a = StateT SimState Identity a`) that threads `SimState` is the coordination surface — its rendered form lives in the [`coordination`](./coordination.md) library; here we render only the state type the two groups share.

## Status

`navigational-container` (rendered library chapter). Holds the rendered synthesized form of the three cross-cutting shared types (`IoData`, `OpParams`, `SimState`); the authoritative field schemas live in the linked `concepts/` record-definition pages. Single-group-clustering types are deliberately absent (placed before their API group in Wave 2 per the type-placement rule).
