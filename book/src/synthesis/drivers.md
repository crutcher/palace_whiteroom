---
kind: navigational-container (synthesis library — drivers)
# Implementation VIEW, reference-class links only. No `rank:`, no `status:` (the
# filled implementation-VIEW convention): it RENDERS the synthesized code form of
# the firm Feature L4 composition roots; the authoritative compositional claims
# live in the linked ../feature/<column>.L4.md chapters and the authoritative
# per-op algebra in the ../L4/<op>.md chapters. Adds no `depends-on` blocking
# edge; constrains no rank/liveness (scheme §4/§5).
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

A def appears after everything it uses. The realized order: the per-driver config records (each a thin `IoData` projection-view, rendered immediately before its driver and bundled with its utility API per the [type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group)); then the 6 sim-driver composition defs; then the 6 output-product composition defs (each composing a rendered reduce verb from [`data-algebra`](./data-algebra.md) over a driver's solution family); finally the lifecycle ROOT, which dispatches on `IoData.problem.type` over the 6 driver defs and folds the AMR estimate-mark-refine schedule via [`fold_solve`](./coordination.md).

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

Each output product is a one-reduction tail on a producing driver column: it consumes the driver's solution family and composes a rendered reduce verb from [`data-algebra`](./data-algebra.md) by name. The reduce verbs are NOT re-rendered here (they live in `data-algebra`); the products *compose* them.

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

Renders [`sparameters.L4`](../feature/sparameters.L4.md). The port-projection reduction [`sparameter_reduce`](./data-algebra.md) over the `driven` driver's per-ω solution family — projecting each per-ω field onto the configured port modes (NOT a Gram self-fold — the do-NOT-over-unify distinction).

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

`navigational-container` (rendered library chapter — the filled implementation-VIEW convention: no `status:`/`rank:`). Holds the synthesized composition defs of the 6 sim drivers + 6 output products + the lifecycle ROOT (topologically last), each composing the already-rendered calculus-library defs ([`types`](./types.md) / [`iteration`](./iteration.md) / [`data-algebra`](./data-algebra.md) / [`coordination`](./coordination.md)) BY NAME and lifting the composition from the firm Feature L4 columns. The compositional claims live in the linked [`../feature/<column>.L4.md`](../feature/index.md) chapters; the per-op algebra lives in the [`../L4/<op>.md`](../L4/index.md) chapters; this chapter LINKS to both and renders only the synthesized code form (link-don't-restate, semantic-consolidation). `reference`-class navigational edges only — it adds no `depends-on` blocking edge and constrains no firm node's rank/liveness.
