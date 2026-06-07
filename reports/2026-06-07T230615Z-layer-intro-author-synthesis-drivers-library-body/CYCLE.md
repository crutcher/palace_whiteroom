---
agent: layer-intro-author
invoked_at: 2026-06-07T230615Z
scope: synthesis/drivers library body (the deferred 6th Synthesis chapter — the topological-LAST library)
status: pending
integrated_at: 2026-06-07T231500Z
integration_commit: e24d757
integration_notes: |
  cycle-137 (batch-44 position 2/3). Applied clean by integrator-per-report (STAGING row 1).
  Filled synthesis/drivers.md stub-shell -> rendered implementation VIEW (13 composition defs:
  6 sim drivers + 6 output products + lifecycle ROOT; + 6 IoData-projection-view config type
  aliases) + 2 synthesis/index.md edits (drivers matrix row + Status completeness line).
  COMPLETES the `# Synthesis` Part 6/6. Finalize NORMALIZED the index 5-library matrix
  (iteration/data-algebra/coordination rows stale `stub (Wave 2)` -> `navigational (rendered)`).
  cargo make book EXIT 0, ZERO build-repairs; step-5c KaTeX `$`-sigil assertion PASS; graded-stack
  rank_violations=0, no newly-orphaned node, all 6 synthesis chapters classify
  expected_unreachable_outside_dag (NOT detritus).
---

# CYCLE: Synthesis `drivers` library body

## Summary

Fills the deferred `drivers` library body in `book/src/synthesis/drivers.md` — the topological-LAST Synthesis chapter, the LEAD of cycle-137 (batch-44). It RENDERS the entry-point surfaces lifted from the firm Feature L4 spine as synthesized library code that **composes** the already-rendered calculus libraries (`types` / `iteration` / `data-algebra` / `coordination`) BY NAME. In topological order: (1) the per-driver config records (rendered as `IoData` projection-views, clustered with their utility API before each driver, back-linked to `concepts/config-record.md` — NO field-schema restatement); (2) the **5 sim-driver composition defs** (`electrostatic` / `magnetostatic` / `driven` / `transient` / `eigenmode`) + the **6th boundary-mode driver**; (3) the **6 output-product composition defs** (`capacitance` / `inductance` / `sparameters` / `eigenfrequency_qfactor` / `energy_fields` / `waveguide_mode`) composing the c136-rendered reduce verbs by name; (4) the **lifecycle ROOT** LAST (the spine-ROOT meta-feature, dispatching on `problem.type` over the 6 driver defs, folding the AMR estimate-mark-refine schedule via `fold_solve`).

The chapter is flipped off `status: stub` to the c136-normalized filled-implementation-VIEW convention (NO `status:` field — kind-only `navigational-container`, no `rank:`; verified against `types.md`/`coordination.md`/`data-algebra.md` frontmatter, all of which carry no `status:` field). It is an implementation VIEW: `reference`-class navigational edges ONLY, no `depends-on`; link-don't-restate (renders the synthesized code form, back-links to `feature/`/`L4`/`semantics` for the authoritative compositional + algebraic claims). All `$`-sigil pseudocode is inside ` ```text ` fences (the KaTeX `$`-sigil-fence rule); the outer proposed-changes fence below is 4 backticks (the c136 cycle-019 nested-fence truncation-hazard fix).

This completes the `# Synthesis` Part: **6/6 library chapters bodied.**

## Proposed changes

One edit MERGING-WITH the existing `drivers.md` stub shell: keep the chapter's orientation intent, replace the `status: stub` frontmatter + the stub body with the rendered composition defs + the filled-VIEW frontmatter/intro.

````edit:book/src/synthesis/drivers.md
[old]:
---
status: stub
kind: navigational-container (synthesis library — drivers; body deferred to a later batch-44 cycle)
# Intro shell. No `rank:` — implementation VIEW, reference-class links only.
edges:
  reference:
    - feature/index
    - feature/lifecycle.L4
    - synthesis/types
    - synthesis/iteration
    - synthesis/data-algebra
    - synthesis/coordination
    - synthesis/index
---

# Library `drivers` — entry-point surfaces (lifted from the Feature spine)

> **Status: `stub`.** This is the library intro shell; the body is **deferred to a later batch-44 cycle**. Per the directive's LEAD-sequencing, `drivers` composes everything (the calculus libraries + the shared types) and therefore comes **last** in topological order — it is authored after the 3 calculus libraries' def bodies land.

The top bracket of the [Synthesis](./index.md) library partition: the synthesized rendering of the entry-point surfaces — the **5 simulation drivers** (electrostatic / magnetostatic / driven / transient / eigenmode), the **lifecycle ROOT** (`main` → `BaseSolver` dispatch), and the **output products** (capacitance / inductance / S-parameters / eigenfrequency+Q / energy-fields / waveguide-mode) — rendered as library code that **composes** the [`types`](./types.md), [`iteration`](./iteration.md), [`data-algebra`](./data-algebra.md), and [`coordination`](./coordination.md) libraries.

These are the same composition roots the [Feature surfaces](../feature/index.md) spine presents top-down; the `drivers` library is the **implementation rendering** of those entry points (the synthesized code that realizes them), parallel to the Feature spine's entry-point VIEW.

## What this library will hold (topological order — composes everything below it)

The expected contents (refine by use): the per-driver config records cluster **before** their driver def, bundled with the config's utility API ([type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group)); then the per-driver composition def; then the output-product reductions; finally the lifecycle ROOT that dispatches on `IoData.problem.type`. Authoring is deferred so the def bodies compose the already-rendered calculus-library defs by name.

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order (this library is topologically last); per-driver config records placed before their driver, bundled with utility API; deep-linked-unchanged lower artifacts inline; Haskell `where` for private helpers; code-doc per def; link to the Feature columns + the composed calculus-library defs, do not re-cite L0.

[new]:
---
kind: navigational-container (synthesis library — drivers; entry-point composition defs rendered)
# Implementation VIEW, reference-class links only. No `rank:`, no `status:` — this
# is the filled implementation-VIEW convention the c136 finalize normalized the
# calculus libraries to: it RENDERS the synthesized code form of the firm Feature
# L4 composition roots; the authoritative compositional claims live in the linked
# ../feature/<column>.L4.md chapters and the authoritative per-op algebra in the
# ../L4/<op>.md chapters. Adds no `depends-on` blocking edge; constrains no
# rank/liveness (scheme §4/§5).
edges:
  reference:
    - feature/index
    - feature/spine-root
    - feature/electrostatic.L4
    - feature/magnetostatic.L4
    - feature/driven.L4
    - feature/transient.L4
    - feature/eigenmode.L4
    - feature/boundary-mode.L4
    - feature/capacitance.L4
    - feature/inductance.L4
    - feature/sparameters.L4
    - feature/eigenfrequency-qfactor.L4
    - feature/energy-fields.L4
    - feature/waveguide-mode.L4
    - feature/lifecycle.L4
    - concepts/config-record
    - synthesis/types
    - synthesis/iteration
    - synthesis/data-algebra
    - synthesis/coordination
    - synthesis/index
---

# Library `drivers` — entry-point surfaces (lifted from the Feature spine)

The top bracket of the [Synthesis](./index.md) library partition: the synthesized rendering of the entry-point surfaces — the **6 simulation drivers** (electrostatic / magnetostatic / driven / transient / eigenmode / boundary-mode), the **6 output products** (capacitance / inductance / S-parameters / eigenfrequency+Q / energy-fields / waveguide-mode), and the **lifecycle ROOT** (`main` → `BaseSolver` dispatch) — rendered as library code that **composes** the [`types`](./types.md), [`iteration`](./iteration.md), [`data-algebra`](./data-algebra.md), and [`coordination`](./coordination.md) libraries.

These are the same composition roots the [Feature surfaces](../feature/index.md) spine presents top-down; the `drivers` library is the **implementation rendering** of those entry points (the synthesized code that realizes them), parallel to the Feature spine's entry-point VIEW. This is the implementation VIEW — it renders the synthesized **composition** of the firm calculus-library defs; the **compositional** claim for each driver/product (driver = this composition of these constituents) lives ONCE in its [`../feature/<column>.L4.md`](../feature/index.md) chapter, and the constituents' **per-op algebra** lives ONCE in the [`../L4/<op>.md`](../L4/index.md) chapters — this chapter LINKS to both (it does not restate either).

## What this library holds (topological order — composes everything below it)

A def appears after everything it uses. The realized order: the per-driver config records (each a thin `IoData` projection-view, rendered immediately before its driver and bundled with its utility API per the [type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group)); then the 6 sim-driver composition defs; then the 6 output-product composition defs (each composing a c136-rendered reduce verb from [`data-algebra`](./data-algebra.md) over a driver's solution family); finally the lifecycle ROOT, which dispatches on `IoData.problem.type` over the 6 driver defs and folds the AMR estimate-mark-refine schedule via [`fold_solve`](./coordination.md).

The composed constituents already rendered in the calculus libraries (composed BY NAME here): from [`data-algebra`](./data-algebra.md) — `fe_assemble`, `assemble_frequency_operator`, `gram_reduce`, `sparameter_reduce`, `eigenfreq_qfactor_reduce`, `domain_energy_reduce`, `waveguide_mode_reduce`; from [`coordination`](./coordination.md) — `ksp_solve`, `eigsolve`, `solve_family`, `frequency_sweep`, `fold_solve`; from [`types`](./types.md) — `IoData` (the parsed config every driver projects).

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order (this library is topologically last); per-driver config records placed before their driver, bundled with utility API; deep-linked-unchanged lower artifacts inline; Haskell `where` for private helpers; code-doc per def (`# Arguments` / `# Returns`); `$`-sigil pseudocode inside ` ```text ` fences; `#extern NAME` after the type signature for opaque-kernel boundaries (the MFEM `ODESolver` time-step is the `time_step_op` `#extern` rendered in [`coordination`](./coordination.md) under `fold_solve`, composed here by reference, not re-rendered); LINK to the Feature columns + the composed calculus-library defs, do NOT re-cite L0 (the L4 chapter + concept pages own the citations). This Part adds `reference`-class navigational edges only — no `depends-on` blocking edges.

---

## Per-driver config records (the `IoData` projection-views)

The per-driver config records named in the driver signatures (`ElectrostaticConfig`, `MagnetostaticConfig`, `DrivenConfig`, `TransientConfig`, `EigenmodeConfig`, `BoundaryModeConfig`) are **NOT distinct data shapes** — they are **projection-views of the one [`IoData`](./types.md)** (the single parsed config object), each selecting the construction-stratum sub-records the driver reads. The authoritative schema + the per-driver projection table is [`config-record`](../concepts/config-record.md) §"per-driver views" (`there is ONE IoData type; the per-driver config records are projections of it`). Rendered here as type aliases over `IoData` (the projection is the utility API — a trivial accessor), clustered before the driver group per the type-placement rule, NOT a field-schema restatement.

```text
-- The per-driver config records are PROJECTION-VIEWS of the one IoData (types.md);
-- authoritative schema + projection table: concepts/config-record.md §per-driver views.
-- Rendered as type aliases (one IoData, several views) — NO field-schema restatement.
type ElectrostaticConfig = IoData    -- the ELECTROSTATIC projection: model + domains.ε + boundaries.terminals + solver.linear
type MagnetostaticConfig = IoData    -- the MAGNETOSTATIC projection: model + domains.ν + boundaries.surface_currents + solver.linear
type DrivenConfig        = IoData    -- the DRIVEN projection:        model + domains.{ν,σ,ε} + boundaries.ports + solver.driven (ω sweep)
type TransientConfig     = IoData    -- the TRANSIENT projection:     model + domains.{ν,σ,ε} + boundaries.J(t) + solver.transient (Δt, max_t)
type EigenmodeConfig     = IoData    -- the EIGENMODE projection:     model + domains.{ν,σ,ε} + solver.eigenmode (n, target) + solver.linear
type BoundaryModeConfig  = IoData    -- the BOUNDARYMODE projection:  model + boundaries.attributes + solver.boundary_mode (freq, n, target)

-- # Arguments / # Returns (utility API — the projection accessors, the only intrinsic namespace)
-- problemType :: IoData -> ProblemType   -- the driver-dispatch discriminant (config-record.md §problem.type); a trivial projection
-- electrostatic_cfg / magnetostatic_cfg / driven_cfg / transient_cfg / eigenmode_cfg / boundary_mode_cfg
--   :: IoData -> <ThatConfig>            -- the per-driver view selectors (each ≡ id; the view is the same IoData)
```

---

## `electrostatic` — fixed-operator driver

Renders the [`electrostatic.L4`](../feature/electrostatic.L4.md) composition root (firm). The cleanest driver: assemble the stiffness operator `K` ONCE, map the fixed-operator solve over the per-terminal RHS family, reduce to the capacitance matrix. Composes [`fe_assemble`](./data-algebra.md) + [`solve_family`](./coordination.md) (which folds [`ksp_solve`](./coordination.md)) + the [`gram_reduce`](./data-algebra.md) `w = 1` voltage specialization.

> Compositional claim (electrostatic = `gram_reduce(w≡1) ∘ solve_family ∘ fe_assemble`): owned by [`electrostatic.L4`](../feature/electrostatic.L4.md). Per-op algebra: the linked `../L4/<op>.md` chapters.

```text
-- # Arguments
--   cfg : ElectrostaticConfig   -- the IoData electrostatic projection (H1 space, ε, terminal sources, linear solver)
-- # Returns
--   CapacitanceMatrix           -- the n_terminal × n_terminal Maxwell capacitance matrix (the physical product)
electrostatic :: ElectrostaticConfig -> CapacitanceMatrix
electrostatic cfg =
  let space = h1_space cfg                                  -- the H1 FE space (readonly construction stratum)
      k     = fe_assemble space [ diffusion (permittivity cfg) ]    -- (1) assemble K ONCE  ── data-algebra/fe_assemble
      rhss  = [ excitation cfg idx | idx <- terminal_sources cfg ]  -- per-terminal RHS family
      vs    = solve_family k rhss                           -- (2) fixed-operator per-terminal map  ── coordination/solve_family
  in  gram_reduce k vs (\i j -> 1)                          -- (3) Cᵢⱼ = Vⱼᵀ K Vᵢ  (w = 1 voltage)  ── data-algebra/gram_reduce
```

The capacitance reduction is presented as a feature in [`capacitance`](#capacitance--voltage-w--1-gram-output-product) (the `w = 1` Gram output product) below; the inverse `Cinv = gram_inverse C` is the consumer tail, kept out of the reduction.

## `magnetostatic` — fixed-operator driver (current-normalized sibling)

Renders the [`magnetostatic.L4`](../feature/magnetostatic.L4.md) composition root (firm). The fixed-operator sibling of `electrostatic`, structurally identical down to the operator-capture-once hoist; the curl-curl stiffness `K` is assembled once, swept over the surface-current family, reduced to the inductance matrix at the `w = 1/(IᵢIⱼ)` current-normalized weight.

> Compositional claim (`magnetostatic = gram_reduce(w=1/(IᵢIⱼ)) ∘ solve_family ∘ fe_assemble`): owned by [`magnetostatic.L4`](../feature/magnetostatic.L4.md).

```text
-- # Arguments
--   cfg : MagnetostaticConfig   -- the IoData magnetostatic projection (Nédélec H(curl) space, ν, surface-current sources, currents Iᵢ)
-- # Returns
--   InductanceMatrix            -- the n_source × n_source Maxwell inductance matrix (the physical product)
magnetostatic :: MagnetostaticConfig -> InductanceMatrix
magnetostatic cfg =
  let space = nd_space cfg                                  -- the Nédélec H(curl) FE space (readonly construction stratum)
      k     = fe_assemble space [ curl_curl (reluctivity cfg) ]     -- (1) assemble K ONCE  ── data-algebra/fe_assemble
      rhss  = [ excitation cfg idx | idx <- surface_current_sources cfg ]
      as    = solve_family k rhss                           -- (2) fixed-operator per-source map  ── coordination/solve_family
      is    = currents cfg                                  -- the per-source excitation currents Iᵢ
  in  gram_reduce k as (\i j -> 1 / (is!!i * is!!j))        -- (3) Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)  ── data-algebra/gram_reduce
```

The inductance reduction is presented as a feature in [`inductance`](#inductance--current-normalized-gram-output-product) below; same shared `gram_reduce`, only the weight differs from `electrostatic`.

## `driven` — operator-varying frequency-sweep driver

Renders the [`driven.L4`](../feature/driven.L4.md) composition root (firm). The operator-VARYING sibling: assemble the fixed operator basis `{K, C, M}` once, then REBUILD `A(ω)` inside the per-ω map (the [`assemble_frequency_operator`](./data-algebra.md) verb) and run one [`ksp_solve`](./coordination.md) per swept frequency — the [`frequency_sweep`](./coordination.md) map (`SetOperators` *inside* the loop, the non-hoist). Reduced to the scattering matrix by `sparameter_reduce`.

> Compositional claim (`driven = sparameter_reduce ∘ frequency_sweep ∘ fe_assemble(×3)`): owned by [`driven.L4`](../feature/driven.L4.md). The `FrequencyOperatorFamily[N]` basis record is rendered in [`data-algebra`](./data-algebra.md) under `assemble_frequency_operator`.

```text
-- # Arguments
--   cfg : DrivenConfig   -- the IoData driven projection (Nédélec H(curl) space, {ν,σ,ε}, ports, ω sweep, linear solver)
-- # Returns
--   FrequencyResponse    -- the per-ω frequency response / S-parameters (the physical product)
driven :: DrivenConfig -> FrequencyResponse
driven cfg =
  let space  = nd_space cfg                                          -- the Nédélec H(curl) FE space (readonly construction stratum)
      fam    = FrequencyOperatorFamily                               -- the fixed basis {K, C, M, A2}, assembled ONCE
                 { K  = fe_assemble space [ curl_curl (reluctivity cfg) ]   -- (1a) stiffness, ONCE  ── data-algebra/fe_assemble
                 , C  = fe_assemble space [ damping cfg ]                   -- (1b) damping, ONCE
                 , M  = fe_assemble space [ mass (permittivity cfg) ]       -- (1c) mass, ONCE
                 , A2 = \omega -> extra_system_matrix space cfg omega }     --      ω-dependent extra term (closure)
      omegas = sample_frequencies cfg                                -- the swept ω family (the [Scalar] the map ranges over)
      es     = frequency_sweep fam omegas                            -- (2) operator-VARYING per-ω solve map  ── coordination/frequency_sweep
  in  sparameter_reduce (ports cfg) (driving_columns es)             -- (3) per-ω port-projection → frequency response
```

The per-ω rebuild `assemble_frequency_operator fam ω` and the per-member `ksp_solve` are inside `frequency_sweep` (rendered in [`coordination`](./coordination.md), not re-rendered here — the driver *composes* it). The S-parameter reduction is presented as a feature in [`sparameters`](#sparameters--port-projection-output-product) below.

## `transient` — fold-pipeline driver

Renders the [`transient.L4`](../feature/transient.L4.md) composition root (firm). The FOLD sibling of the map-style drivers: assemble the second-order-in-time operators `K`/`C`/`M` once, capture the ODE operator, seed the field-state, and thread it through the fixed timestep schedule by [`fold_solve`](./coordination.md) — a state-threaded `foldl` where each step's input is the prior step's output. The per-step body is the opaque MFEM `ODESolver::Step` rendered `#extern time_step_op` in [`coordination`](./coordination.md) under `fold_solve` (composed by reference here, not re-rendered).

> Compositional claim (`transient = fold_solve ∘ fe_assemble`): owned by [`transient.L4`](../feature/transient.L4.md). The carry-threading is a `sequential-obstruction` and the per-step body an opaque-library step — both absorbed by the firm `fold_solve` combinator.

```text
-- # Arguments
--   cfg : TransientConfig   -- the IoData transient projection (Nédélec H(curl) space, {ν,σ,ε}, J(t), Δt + max_t schedule)
-- # Returns
--   FieldTrajectory         -- the time-domain field-state trajectory (the physical product)
transient :: TransientConfig -> FieldTrajectory
transient cfg =
  let space    = nd_space cfg                                       -- the Nédélec H(curl) FE space (readonly construction stratum)
      (k,c,m)  = ( fe_assemble space [ curl_curl (reluctivity cfg) ]   -- (1) assemble K (stiffness)
                 , fe_assemble space [ conductivity_term cfg ]         --     assemble C (damping)
                 , fe_assemble space [ permittivity_mass cfg ] )       --     assemble M (mass) — ALL once  ── data-algebra/fe_assemble
      op       = time_operator (k,c,m) (dJdt cfg)                   -- the captured ODE operator (readonly; op : OpParams — types.md)
      s0       = init_state cfg                                     -- the seed field-state (zero IC)
      schedule = uniform_steps (delta_t cfg) (n_step cfg)           -- the FIXED [Time] schedule
  in  fold_solve op s0 schedule                                     -- (2) state-threaded time-march FOLD → trajectory  ── coordination/fold_solve
```

`transient` owns no separate output-product column — its product is the field trajectory itself (and per-step field energies feed the driver-agnostic [`energy_fields`](#energy_fields--per-domain-energy-table-output-product-driver-agnostic) postprocess).

## `eigenmode` — black-box-kernel driver

Renders the [`eigenmode.L4`](../feature/eigenmode.L4.md) composition root (firm). The minimal-shape driver: assemble the `(K, C, M)` pencil once, hand it to the opaque [`eigsolve`](./coordination.md) black-box cap ONCE (no `solve_family` map, no `fold_solve` march — the single black-box call IS the entire solve; the SLEPc EPS loop is `#extern eigen_iterate` in [`coordination`](./coordination.md)), then a pure per-mode readout map. The eigenfrequency/Q reduction is `eigenfreq_qfactor_reduce`.

> Compositional claim (`eigenmode = map readout ∘ eigsolve ∘ eig_pencil ∘ fe_assemble(×3)`): owned by [`eigenmode.L4`](../feature/eigenmode.L4.md). The divergence-free projector wired into the eigensolver is a directly-wired absorbed constituent (the eigenmode driver's `constrains-eigvec` edge), absorbed into the `eig_pencil` / cap, not the composition shape.

```text
-- # Arguments
--   cfg : EigenmodeConfig   -- the IoData eigenmode projection (Nédélec H(curl) space, {ν,σ,ε}, n modes + target, divfree projector, linear solver)
-- # Returns
--   EigenmodeResult         -- per-mode (eigenfrequency ω, quality factor Q, mode fields (E, B)) — the physical product
eigenmode :: EigenmodeConfig -> EigenmodeResult
eigenmode cfg =
  let space  = nd_space cfg                                         -- the Nédélec H(curl) FE space (readonly construction stratum)
      k      = fe_assemble space [ curl_curl (reluctivity cfg) ]    -- (1a) assemble K ONCE  ── data-algebra/fe_assemble
      c      = fe_assemble space [ conductivity_term cfg ]          -- (1b) assemble C ONCE (damping; empty ⇒ linear EVP)
      m      = fe_assemble space [ mass_term (permittivity cfg) ]   -- (1c) assemble M ONCE
      pencil = eig_pencil k c m (target cfg) (n_modes cfg)          -- the (K, C, M) pencil + spectral-transform target
      eigs   = eigsolve pencil (initial_space cfg)                  -- (2) ONE opaque black-box eigen-solve  ── coordination/eigsolve
  in  map (readout cfg) eigs                                        -- (3) per-mode readout map → ω, Q, B = -1/(iω)∇×E
```

The `(f, Q)` scalar reduction is presented as a feature in [`eigenfrequency_qfactor`](#eigenfrequency_qfactor--per-mode-f-q-table-output-product) below.

## `boundary_mode` — 2D-submesh black-box-kernel driver

Renders the [`boundary-mode.L4`](../feature/boundary-mode.L4.md) composition root (firm). The 6th `ProblemType` branch (`palace/main.cpp:276`): the SAME `eigsolve` corner as `eigenmode`, but over a boundary-extracted 2D submesh — a distinguishing stage-(0) `extract_boundary_2d_submesh` preface, then assemble the `ND ⊕ H1` block GEP pencil, one `eigsolve`, a per-mode readout reduced to the waveguide-mode table.

> Compositional claim (`boundary_mode = map readout ∘ eigsolve ∘ eig_pencil ∘ fe_assemble ∘ extract_boundary_2d_submesh`): owned by [`boundary-mode.L4`](../feature/boundary-mode.L4.md). The 2D-submesh extraction is a driver-local preface (no standalone combinator yet).

```text
-- # Arguments
--   cfg : BoundaryModeConfig   -- the IoData boundary_mode projection (boundary attributes, freq ω, n modes + target, linear solver)
-- # Returns
--   BoundaryModeResult         -- per-mode (propagation constant kn, n_eff, mode fields (Et, En, Bz)) — the physical product
boundary_mode :: BoundaryModeConfig -> BoundaryModeResult
boundary_mode cfg =
  let mesh2d = extract_boundary_2d_submesh (parent_mesh cfg) (surface_attrs cfg)  -- (0) 3D-boundary → 2D submesh (driver-local preface)
      space  = mode_space mesh2d cfg                              -- the combined ND ⊕ H1 block FE space on the 2D submesh
      opA    = fe_assemble space [ block_system (omega cfg) (sigma cfg) ]   -- (1a) assemble block system A  ── data-algebra/fe_assemble
      opB    = fe_assemble space [ mass_block ]                            -- (1b) assemble RHS block B
      pencil = eig_pencil opA opB (sigma cfg) (n_modes cfg)       -- the (A, B) GEP pencil + shift-invert σ = -kn_target²
      eigs   = eigsolve pencil (initial_space cfg)               -- (2) ONE opaque black-box eigen-solve  ── coordination/eigsolve (SAME corner as eigenmode)
  in  map (readout cfg (omega cfg)) eigs                          -- (3) per-mode readout map → kn, n_eff, (Et, En, Bz)
```

The per-mode propagation-mode reduction is presented as a feature in [`waveguide_mode`](#waveguide_mode--per-mode-propagation-mode-table-output-product) below.

---

## Output products (composing the reduce verbs)

Each output product is a one-reduction tail on a producing driver column: it consumes the driver's solution family and composes a c136-rendered reduce verb from [`data-algebra`](./data-algebra.md) by name. The reduce verbs are NOT re-rendered here (they live in `data-algebra`); the products *compose* them.

### `capacitance` — voltage (`w = 1`) Gram output product

Renders [`capacitance.L4`](../feature/capacitance.L4.md). The `w = 1` voltage specialization of [`gram_reduce`](./data-algebra.md) over the `electrostatic` driver's solution family; the inverse is the `gram_inverse` consumer tail.

```text
-- # Arguments
--   cfg : ElectrostaticConfig   -- inherited from the producing electrostatic driver column
-- # Returns
--   CapacitanceMatrix           -- { matrix : Cᵢⱼ = Vⱼᵀ K Vᵢ, inverse : Cinv = C⁻¹ }
capacitance :: ElectrostaticConfig -> CapacitanceMatrix
capacitance cfg =
  let (k, vs) = electrostatic_family cfg          -- (1) the electrostatic driver: K once + per-terminal solve_family → [Vᵢ]
      c       = gram_reduce k vs (\i j -> 1)       -- (2) symmetric-Gram at w = 1 (voltage)  ── data-algebra/gram_reduce
  in  { matrix = c, inverse = gram_inverse c }     -- the alternate Maxwell form (gram_inverse consumer tail)
```

### `inductance` — current-normalized Gram output product

Renders [`inductance.L4`](../feature/inductance.L4.md). The `w = 1/(IᵢIⱼ)` current-normalized specialization of the SAME [`gram_reduce`](./data-algebra.md) over the `magnetostatic` driver's family; only the weight differs from `capacitance`.

```text
-- # Arguments
--   cfg : MagnetostaticConfig   -- inherited from the producing magnetostatic driver column (incl. the excitation currents Iᵢ)
-- # Returns
--   InductanceMatrix            -- { matrix : Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ), inverse : Minv = M⁻¹ }
inductance :: MagnetostaticConfig -> InductanceMatrix
inductance cfg =
  let (k, as) = magnetostatic_solution cfg               -- (1) the magnetostatic driver: K once + per-source solve_family → [Aᵢ]
      is      = currents cfg                              -- the per-source excitation currents Iᵢ
      m       = gram_reduce k as (\i j -> 1 / (is!!i * is!!j))   -- (2) symmetric-Gram at w = 1/(IᵢIⱼ)  ── data-algebra/gram_reduce
  in  { matrix = m, inverse = gram_inverse m }            -- the alternate Maxwell form (gram_inverse consumer tail)
```

### `sparameters` — port-projection output product

Renders [`sparameters.L4`](../feature/sparameters.L4.md). The port-projection reduction [`sparameter_reduce`](./data-algebra.md) over the `driven` driver's per-ω solution family — projecting each per-ω field onto the configured port modes (NOT a Gram self-fold — the c074/c075 do-NOT-over-unify distinction).

```text
-- # Arguments
--   cfg : DrivenConfig   -- inherited from the producing driven driver column (ports + frequency sweep)
-- # Returns
--   ScatteringMatrix     -- the per-ω complex n_port × n_port scattering matrix S(ω)
sparameters :: DrivenConfig -> ScatteringMatrix
sparameters cfg =
  let es = driven_family cfg                       -- (1) the driven driver: {K,C,M} once + operator-VARYING per-ω map → [Eᵢ]
  in  sparameter_reduce (ports cfg) es             -- (2) per-ω port-mode projection → scattering matrix  ── data-algebra/sparameter_reduce
                                                   --     Sᵢⱼ(ω) = ⟨port_mode_i, Eⱼ(ω)⟩ (+ self-reflection −1, de-embed/normalize)
```

### `eigenfrequency_qfactor` — per-mode `(f, Q)` table output product

Renders [`eigenfrequency-qfactor.L4`](../feature/eigenfrequency-qfactor.L4.md). The per-mode scalar-ratio reduction [`eigenfreq_qfactor_reduce`](./data-algebra.md) over the `eigenmode` driver's converged eigenpair family — a rank-1 per-mode table, NOT a Gram grid.

```text
-- # Arguments
--   cfg : EigenmodeConfig   -- inherited from the producing eigenmode driver column (problem-type un-transform + resistive-port κ)
-- # Returns
--   [(Scalar, Scalar)]      -- per mode: (fₘ = Re ωₘ, Qₘ = ωₘ / κₘ)
eigenfrequency_qfactor :: EigenmodeConfig -> [(Scalar, Scalar)]
eigenfrequency_qfactor cfg =
  let eigs  = eigenmode_eigenpairs cfg             -- (1) the eigenmode driver: pencil once + ONE eigsolve → converged [(λᵢ, Eᵢ)]
      ptype = problem_type cfg                     -- the eigenvalue→ω un-transform selector (the variant axis)
      kappa = loss_rate cfg                        -- the per-mode loss-rate closure κₘ = ½R|Iₘⱼ|²/Eₘ
  in  eigenfreq_qfactor_reduce ptype kappa eigs    -- (2) per mode (fₘ, Qₘ)  ── data-algebra/eigenfreq_qfactor_reduce
```

### `energy_fields` — per-domain energy table output product (driver-agnostic)

Renders [`energy-fields.L4`](../feature/energy-fields.L4.md). The driver-AGNOSTIC per-domain energy-table reduction [`domain_energy_reduce`](./data-algebra.md) over a single solution field from ANY field-bearing driver — the shared postprocess all field-bearing drivers point at (no single producing driver to 1:1-reciprocate). Rank-1 per-domain table.

```text
-- # Arguments
--   cfg   : PostprocessConfig   -- the energy-postprocess domain set (IoData.domains.postpro.energy; config-record.md sub-record)
--   field : Field               -- a solved field from any field-bearing driver (V/E electric, A/B magnetic)
-- # Returns
--   [DomainData]                -- per domain: (idx, energyᵢ = ½⟨field, M_idx field⟩, pᵢ = energyᵢ / e_total)
energy_fields :: PostprocessConfig -> Field -> [DomainData]
energy_fields cfg field =
  let doms    = energy_domains cfg                 -- the configured domain-attribute set {idx → M_idx}
      e_total = field_energy field                 -- the whole-domain total energy (the shared denominator)
  in  domain_energy_reduce doms field e_total      -- (2) per-domain energy table  ── data-algebra/domain_energy_reduce
```

### `waveguide_mode` — per-mode propagation-mode table output product

Renders [`waveguide-mode.L4`](../feature/waveguide-mode.L4.md). The field-carrying per-mode reduction [`waveguide_mode_reduce`](./data-algebra.md) over the `boundary_mode` driver's converged eigenpair family — un-transform to `kn`, divide to `n_eff`, VD-back-transform + power-normalize to `(Et, En)`, form `Bz` for propagating modes.

```text
-- # Arguments
--   cfg : BoundaryModeConfig   -- inherited from the producing boundary-mode driver column (boundary attributes + operating frequency ω)
-- # Returns
--   WaveguideModeTable         -- per mode: {kn, n_eff, (Et, En, Bz)}  (WaveguideModeTable: concepts/WaveguideModeTable.md)
waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable
waveguide_mode cfg =
  let eigs = boundary_mode_eigenpairs cfg          -- (1) the boundary-mode driver: 2D submesh + (A,B) pencil + ONE eigsolve → eigenpair family
  in  waveguide_mode_reduce eigs (omega cfg)       -- (2) per-mode propagation-mode reduce → {kn, n_eff, (Et,En,Bz)}  ── data-algebra/waveguide_mode_reduce
```

---

## `lifecycle` — the spine ROOT (composes the driver defs)

Renders the [`lifecycle.L4`](../feature/lifecycle.L4.md) composition root (firm) — the topologically-LAST def, the spine-ROOT **meta-feature** whose constituents are the driver defs above (plus driver-agnostic firm vocabulary). It builds the mesh, dispatches on `IoData.problem.type` to ONE driver def, and threads the adaptive estimate-mark-refine schedule through [`fold_solve`](./coordination.md) in its state-generated `schedule-source` form (the AMR loop; degenerates to the single initial solve when AMR is disabled).

> Compositional claim (`lifecycle = fold_solve (dispatch (problem_type cfg)) ∘ build_mesh`): owned by [`lifecycle.L4`](../feature/lifecycle.L4.md). The mesh scaffold `build_mesh` is the driver-agnostic stage-1 constituent (`L1/build_mesh`); the AMR estimate-mark-refine leaf is composed by reference (its synthesized impl is not a Synthesis deliverable — AMR is in active scope per DIRECTIVE-2 but un-rendered here, so the fold quantifies over `estimate_mark_refine` as a driver-agnostic step rather than fabricating a def).

```text
-- # Arguments
--   cfg : IoData   -- the parsed config (types.md); problem.type selects the driver, refinement config drives the AMR fold
-- # Returns
--   Product        -- the driver-selected physical product (capacitance | inductance | S-params | (f,Q) | trajectory | fields | modes)
lifecycle :: IoData -> Product
lifecycle cfg =
  let mesh0 = build_mesh cfg                        -- (1) mesh scaffold: load + partition + a-priori-refine (driver-agnostic; L1/build_mesh)
      drv   = dispatch (problemType cfg)            -- (2) select the per-driver feature def (the specialization seam)
      step  = \m -> estimate_mark_refine cfg (drv cfg m)  -- one iterate: run the driver Solve, then mark/refine the mesh
  in  fold_solve_amr step mesh0 (refinement cfg)    -- (3) adaptive estimate-mark-refine outer FOLD → product  ── coordination/fold_solve (state-generated)
  where
    -- the dispatch over the 6 driver defs above, by ProblemType (palace/main.cpp:257-280):
    dispatch ELECTROSTATIC = electrostatic
    dispatch MAGNETOSTATIC = magnetostatic
    dispatch DRIVEN        = driven
    dispatch TRANSIENT     = transient
    dispatch EIGENMODE     = eigenmode
    dispatch BOUNDARYMODE  = boundary_mode
    -- the state-generated fold: the carry {mesh, indicators, ...} GENERATES the next input + loop bound
    -- from accumulated error (fold_solve's schedule-source = state-generated axis). When AMR is disabled
    -- (refinement.max_it == 0) it degenerates to the single initial driver Solve. The estimate-mark-refine
    -- leaf is composed by reference (AMR's synthesized impl is not rendered in Synthesis); the per-step
    -- body otherwise bottoms out in coordination/fold_solve's #extern time_step_op / the driver Solve.
    fold_solve_amr step m0 refcfg = fold_solve (amr_op refcfg) m0 (amr_schedule refcfg)
```

The per-driver dispatch is over the driver defs rendered above (references, the specialization seam); `build_mesh` is the driver-agnostic mesh scaffold; the adaptive fold IS [`fold_solve`](./coordination.md) in its state-generated form (no new combinator). `main` itself writes only run metadata — the product is the selected driver def's output.

## Status

`navigational-container` (rendered library chapter — the filled implementation-VIEW convention: no `status:` field, no `rank:`, the same convention the c136 finalize normalized `types`/`iteration`/`data-algebra`/`coordination` to). Holds the synthesized composition defs of the 6 sim drivers + 6 output products + the lifecycle ROOT (topologically last), each composing the already-rendered calculus-library defs ([`types`](./types.md) / [`iteration`](./iteration.md) / [`data-algebra`](./data-algebra.md) / [`coordination`](./coordination.md)) BY NAME and lifting the composition from the firm Feature L4 columns. The compositional claims live in the linked [`../feature/<column>.L4.md`](../feature/index.md) chapters; the per-op algebra lives in the [`../L4/<op>.md`](../L4/index.md) chapters; this chapter LINKS to both and renders only the synthesized code form (link-don't-restate, semantic-consolidation). `reference`-class navigational edges only — it adds no `depends-on` blocking edge and constrains no firm node's rank/liveness. With this body landed, the `# Synthesis` Part is complete: **6/6 library chapters bodied.**
````

## Supporting evidence

- **Feature L4 composition roots lifted from** (all firm, all on-disk, read this dispatch): `book/src/feature/{electrostatic,magnetostatic,driven,transient,eigenmode,boundary-mode}.L4.md` (the 6 drivers); `book/src/feature/{capacitance,inductance,sparameters,eigenfrequency-qfactor,energy-fields,waveguide-mode}.L4.md` (the 6 output products); `book/src/feature/lifecycle.L4.md` (the spine ROOT). Each rendered def's composition (the `-- (1)/(2)/(3)` stages + the constituent down-link table) is transcribed faithfully from its column's "## The composition" block.
- **Calculus-library defs composed BY NAME** (rendered c136, on-disk): from `book/src/synthesis/data-algebra.md` — `fe_assemble` (`fe_assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinOp[(N: ...), $N]`), `assemble_frequency_operator` (+ the `FrequencyOperatorFamily[N]` record), `gram_reduce` (`gram_reduce k xs w`, with the `w` weight closure the capacitance/inductance specializations supply), `sparameter_reduce` (`sparameter_reduce ports family`), `eigenfreq_qfactor_reduce` (`eigenfreq_qfactor_reduce ptype kappa eigs`), `domain_energy_reduce` (`domain_energy_reduce doms field e_total`), `waveguide_mode_reduce` (`waveguide_mode_reduce res w`); from `book/src/synthesis/coordination.md` — `ksp_solve`, `eigsolve` (with the `#extern eigen_iterate` SLEPc loop), `solve_family` (`solve_family op rhss = map (ksp_solve op) rhss`), `frequency_sweep`, `fold_solve` (with the `#extern time_step_op` MFEM ODESolver step); from `book/src/synthesis/types.md` — `IoData`.
- **Per-driver config-record homing:** the per-driver config records (`ElectrostaticConfig` etc.) are **projections of the one `IoData`**, authoritatively defined in `book/src/concepts/config-record.md:107-126` ("There is ONE IoData type; the per-driver config records are projections of it" + the per-driver projection table). Rendered here as type aliases over `IoData` with the projection accessor as the utility API — NOT a field-schema restatement (record-definition obligation satisfied: the schema lives once, in `config-record.md`; this is a use-site projection-view). No new record needs a definition home — all 6 are projection-views of the already-homed `IoData`.
- **Status-convention verification:** read `book/src/synthesis/{types,coordination,data-algebra}.md` frontmatter — `types.md` carries `kind: navigational-container ... ` with NO `status:` field; `data-algebra.md` / `coordination.md` likewise carry `kind:`-only frontmatter (their `> **Status: \`seed\`**` body banners are a c136 residual the finalize normalization left in the body, NOT the frontmatter convention). The drivers frontmatter is flipped to the matching no-`status:` filled-VIEW convention (resolves the `drivers` arm of OQ `synthesis-coordination-chapter-status-seed-token-reconciliation-c136`).
- **SUMMARY:** `book/src/SUMMARY.md:16` already carries the `drivers` row (`Library — drivers (entry-point surfaces)`) — no SUMMARY edit needed (the c136 shell wired it).
- **Index-cell flip:** `book/src/synthesis/index.md:40` carries the 5-library partition matrix with the `drivers` row Status cell = `stub (deferred)`. This dispatch flips that cell to `navigational (rendered)` (matching the other rendered libraries' cells) — see the second edit below.

````edit:book/src/synthesis/index.md
[old]:
| [`drivers`](./drivers.md) | (lifted from [Feature surfaces](../feature/index.md)) | the entry-point surfaces — 5 sim drivers + lifecycle ROOT + output products — composing the calculus libraries | stub (deferred) |
[new]:
| [`drivers`](./drivers.md) | (lifted from [Feature surfaces](../feature/index.md)) | the entry-point surfaces — 6 sim drivers + 6 output products + lifecycle ROOT — composing the calculus libraries | navigational (rendered) |
````

Also flip the §Status line of `index.md` (the per-library completeness note) so it no longer calls `drivers` `stub`:

````edit:book/src/synthesis/index.md
[old]:
`navigational-container` (Part index). This page makes no resolution claim — it is the orientation + dep-map for the Synthesis implementation VIEW. The per-library chapters carry their own status (`types` rendered; `iteration` / `data-algebra` / `coordination` / `drivers` `stub` pending Wave-2 def rendering).
[new]:
`navigational-container` (Part index). This page makes no resolution claim — it is the orientation + dep-map for the Synthesis implementation VIEW. All six per-library chapters are now rendered (the filled implementation-VIEW convention: `kind`-only frontmatter, no `status:`/`rank:`) — `types` + the three calculus libraries (`iteration` / `data-algebra` / `coordination`) + the topologically-last `drivers` library (cycle-137). The `# Synthesis` Part is complete: 6/6 library chapters bodied.
````

## Open questions / caveats

- **`record-WaveguideModeTable` / `record-DomainData` already homed.** `WaveguideModeTable` is named in the `waveguide_mode` signature; it has a `concepts/WaveguideModeTable.md` home (≥2-consumer, promoted c118 D6) — back-linked, not restated. `DomainData` (named in `energy_fields`) is a single-consumer in-chapter record (`feature/energy-fields.L4.md §Record definition`) flagged OQ `record-DomainData-needs-definition-home` for cross-cutter re-check; this Synthesis render does NOT create a 2nd consumer requiring promotion (it composes `domain_energy_reduce` whose result element is `DomainData` — the same single authoritative consumer surface). No new record-definition flag from this dispatch.
- **`build_mesh` / `estimate_mark_refine` / AMR leaf rendered by reference, not as filled defs.** The lifecycle ROOT composes `build_mesh` (`L1/build_mesh`, firm — a mesh scaffold, not an L4 calculus op, so it has no synthesized calculus-library def) and the AMR `estimate_mark_refine` leaf (in active scope per DIRECTIVE-2 but with NO synthesized impl rendered — AMR's constructive impl is not a Synthesis deliverable this batch). Both are composed by reference (named in the `lifecycle` def + its `where` block) rather than fabricating a def, per the directive's `#extern`/deep-link discipline (a non-rendered constituent is named, not invented). If a future cycle renders the AMR estimate-mark-refine impl (a `library` def, likely in a future `coordination`/`drivers` extension), the `fold_solve_amr` `where`-helper here should compose it by name. Flag: `synthesis-lifecycle-amr-estimate-mark-refine-rendered-by-reference` — surfaced for the batch-44 meta / a future AMR-impl cycle; NOT blocking (the lifecycle ROOT's compositional claim is the AMR fold over driver dispatch, which IS rendered; the AMR leaf's *internal* impl is a separate future deliverable).
- **`#extern` boundaries are in the calculus libraries, composed here by reference.** The two opaque-kernel `#extern` leaves the drivers touch — `time_step_op` (MFEM ODESolver, under `fold_solve` in `coordination.md`) and `eigen_iterate` (SLEPc EPS loop, under `eigsolve` in `coordination.md`) — are rendered `#extern` in `coordination.md` and composed here by reference (the `transient`/`eigenmode`/`boundary_mode` defs name `fold_solve`/`eigsolve`, which carry the `#extern` internally). The drivers library renders NO new `#extern` (correct — the kernel boundaries belong to the operators that own them, not the composition roots). No kernel-API/impl gap from this dispatch.
- **Per-driver config records as `IoData` projection-views — a deliberate clean-room rendering choice.** I rendered the six per-driver config records (`ElectrostaticConfig` etc.) as `type X = IoData` projection aliases with the projection accessor as the utility API, per `config-record.md:107` ("the per-driver config records are projections of [the one IoData]"). This is the faithful synthesized form (one parsed config, several driver views) and satisfies the type-placement rule (clustered before the driver group, bundled with the projection utility API). An alternative rendering — distinct narrowed record types per driver — was rejected because it would invent a data shape the spec does not carry (the spec is explicit there is ONE `IoData`); the projection-view is the non-over-structured choice. Flag for the lowering-verifier / meta if a future use wants the narrowed-record form, but the projection-view matches the authoritative `config-record.md` framing.
- **Single-file LEAD sizing — landed as one dispatch.** The plan flagged the ~13-def single-file render as a potential token-budget split candidate. It rendered cleanly in one pass (the defs are short compositions of already-rendered firm vocabulary, the layer-intro-author's wheelhouse). No sub-split needed; no token-budget pressure to escalate.
