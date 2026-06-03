---
kind: feature-surface
feature: transient
level: L4
status: firm
composes:
  - book/src/L4/fe_assemble.md (firm — assemble the time-domain operators K/C/M once: the assemble-fold combinator)
  - book/src/L4/fold_solve.md (firm — the state-threaded time-march FOLD; transient is its default/primary witness)
l0_ground_truth:
  - palace/drivers/transientsolver.cpp:24-116 (TransientSolver::Solve)
  - palace/models/timeoperator.cpp:65-67 (K/C/M assembled once), :407-413 (TimeOperator::Step → ode->Step)
---

# transient — L4 composition-root

The **transient simulation feature**, presented at L4 as a single composition of firm L4 combinators — the **outward backend-lowering entry point** for the time-domain pipeline. This chapter is a *composition root* (the **leaf feature column** sub-kind, per-driver): it does not introduce a new combinator; it wires the already-firm L4 vocabulary into the user-facing feature (config → time-domain field evolution), and links DOWN to each composed piece.

Transient is the **FOLD-pipeline driver** — the **fold-sibling** of the map-style fixed-operator drivers. Where [electrostatic](./electrostatic.L4.md) and [magnetostatic](./magnetostatic.L4.md) compose [`solve_family`](../L4/solve_family.md) (an *independent map* over an RHS family, no carry between elements), transient composes [`fold_solve`](../L4/fold_solve.md) — a *state-threaded fold* where **each step's input is the prior step's output**. The two are siblings under the one strawman §3.7 `iterate_while` parent (a map is the degenerate fold whose step ignores the accumulator; the time-march is the non-degenerate fold that threads it). Transient is in fact `fold_solve`'s **default / primary witness** — the fixed-list time-march that gives the combinator its default signature surface (`book/src/L4/fold_solve.md:113`).

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the time-domain field-state trajectory (the physical product)
    transient :: TransientConfig -> FieldTrajectory
    transient cfg =
      let space    = nd_space cfg                              -- the Nédélec H(curl) finite-element space (readonly construction stratum)
          (k,c,m)  = ( fe_assemble space [ curl_curl (reluctivity cfg) ]   -- (1) assemble K (stiffness)
                     , fe_assemble space [ conductivity_term cfg ]         --     assemble C (damping)
                     , fe_assemble space [ permittivity_mass cfg ] )       --     assemble M (mass) — ALL once
          op       = time_operator (k,c,m) (dJdt cfg)          -- the captured ODE operator (readonly; op : OpParams)
          s0       = init_state cfg                            -- the seed field-state (zero IC)
          schedule = uniform_steps (delta_t cfg) (n_step cfg)  -- the FIXED [Time] schedule
      in  fold_solve op s0 schedule                            -- (2) the state-threaded time-march FOLD → trajectory

Two composed stages, each a link DOWN to firm L4 vocabulary:

1. **Assemble the time-domain operators K / C / M once** — [`fe_assemble`](../L4/fe_assemble.md) (**firm**). The L4 assemble-fold combinator `fe_assemble space terms = sum (map (assemble_term space) terms)` folds each weak-form term list into a global operator. Transient is a **second-order-in-time** wave system, so it assembles **three** operators once: the stiffness `K`, the damping `C`, and the mass `M` (the `M s'' + C s' + K s = -dJ/dt` first-order-IVP form). All three are assembled ONCE at `TimeOperator` construction, outside the time loop — the operator-capture-once stratum (`fe_assemble`'s single/multi-term fold per operator). L0: `K = space_op.GetStiffnessMatrix(...)`, `C = space_op.GetDampingMatrix(...)`, `M = space_op.GetMassMatrix(...)` (`palace/models/timeoperator.cpp:65-67`).

2. **The state-threaded time-march fold** — [`fold_solve`](../L4/fold_solve.md) (**firm**). The L4 state-threaded fold combinator `fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule` captures the ODE operator `op` once, seeds the persistent field-state `s0` once, and threads the carry through the fixed schedule. Transient is `fold_solve`'s **default surface** (named at `book/src/L4/fold_solve.md:113`): `op` = the `TimeOperator` built once (`timeoperator.cpp:312`), `s0` = the initial field-state (`time_op.Init()`, `transientsolver.cpp:89`), the schedule = a **fixed uniform** `[Time]` list of `n_step` steps of `delta_t` (`transientsolver.cpp:35-36`). The fold body is `time_op.Step(t, delta_t)` (`transientsolver.cpp:93`) → the opaque MFEM `ode->Step(sol, t, dt)` (`timeoperator.cpp:410`), which advances the persistent `sol` field-state in place — **the prior step's `sol` is the next step's input**, the genuine `foldl`. The per-step `(E, B)` is consumed for postprocessing (`transientsolver.cpp:98-99`), so the trajectory materializes. L0: the loop `transientsolver.cpp:77`, the seed `:89`, the step `:93`.

The per-step body `time_step_op` bottoms out in an **opaque library step** (the MFEM `ODESolver::Step`, which internally performs an implicit linear solve per step) — the L4 entry quantifies over it rather than rendering it. This is recorded at the lowering layer as `obstruction (opaque-library-ownership)` ([`fold_solve`](../L4/fold_solve.md) §Lowers-to); the transient feature column does NOT expose a per-step `ksp_solve` cap (the implicit solve is inside the opaque integrator step, not a user-visible map element as in the fixed-operator drivers).

## Inputs / outputs (the feature surface)

- **Input — config.** `TransientConfig`: the Nédélec H(curl) space construction (mesh + order → `nd_space`), the material coefficients (reluctivity / conductivity / permittivity → the K / C / M term coefficients), the time-domain excitation pulse `J(t)` and its derivative `dJ/dt` (→ the per-step forcing, `GetTimeExcitation`, `transientsolver.cpp:30-31`), and the schedule parameters (`delta_t` and `max_t` → the fixed `[Time]` schedule, `transientsolver.cpp:35-36`). All `readonly` construction-stratum inputs; none threads mutably *except* the field-state carry, which is the fold's threaded carry, not a config input. L0 home: `SpaceOperator space_op(iodata, mesh)` (`transientsolver.cpp:32`) + `TimeOperator time_op(iodata, space_op, dJdt_coef)` (`:33`) — `iodata` is the config surface.
- **Output — the physical product.** A **time-domain field-state trajectory** — the sequence of `(E, B)` field bundles measured per step (`time_op.GetE()` / `time_op.GetB()`, `transientsolver.cpp:98-99`), reduced by the per-step postprocess (`post_op.MeasureAndPrintAll(step, E, B, t, J_coef(t))`, `:104`) and finalized (`post_op.MeasureFinalize(indicator)`, `:114`). This is what the user ran the transient solver to compute: the time-domain response (port voltages/currents, fields, energy) over the simulated interval, plus the returned error indicator + global dof count (`{indicator, space_op.GlobalTrueVSize()}`, `:115`).

## Why this composes cleanly (the fold-sibling witness)

The transient feature composes cleanly because **both stages compose firm L4 combinators with no obstruction at the composition level**:

- The assemble is three single-term `fe_assemble` folds (K / C / M), each the operator-capture-once stratum — assembled once at `TimeOperator` construction, outside the loop.
- The march is `fold_solve`'s **default / fixed-list** corner — the state-threaded fold whose default signature surface transient *is* (the primary fold witness). The carry-threading is a [`sequential-obstruction`](../concepts/sequential-obstruction.md) (the schedule does NOT commute — reordering timesteps changes the trajectory), and the per-step body is an opaque-library integrator step; BOTH obstructions are absorbed by the firm `fold_solve` combinator (it quantifies over the opaque step and types the carry-threading) and recorded at the lowering layer. The composition level introduces neither.

The whole feature therefore lowers cleanly outward to the L4 backend surface: `transient = fold_solve ∘ fe_assemble` — a two-stage pipeline of firm combinators with a single shared operator capture and a threaded field-state carry. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary (`fe_assemble` + `fold_solve`, both firm) composes without forcing the spine. The transient column is the spine's first **fold-pipeline** witness — the structural complement to the electrostatic/magnetostatic map-pipeline columns.

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| assemble K / C / M once | [`fe_assemble`](../L4/fe_assemble.md) | firm | `timeoperator.cpp:65-67` |
| state-threaded time-march fold | [`fold_solve`](../L4/fold_solve.md) | firm | `transientsolver.cpp:77, 89, 93`; `timeoperator.cpp:312, 410` |
| per-step body (opaque ODE step) | quantified-over by `fold_solve`; `obstruction (opaque-library-ownership)` at lowering | — | `timeoperator.cpp:407-413` |

## Status

`firm` — the **leaf feature column** (per-driver sub-kind) for the transient pipeline, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the spine's first **fold-pipeline** witness (sibling of the [electrostatic](./electrostatic.L4.md) / [magnetostatic](./magnetostatic.L4.md) map-pipeline columns). **Promoted `seed → firm` cycle-085** under the OWN-COMPOSITION promotion rule (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. The composition is sound and rests on **firm** directly-owned constituents end-to-end: stage (1) composes the firm [`fe_assemble`](../L4/fe_assemble.md) (three operators, K/C/M), stage (2) composes the firm [`fold_solve`](../L4/fold_solve.md) (transient is its default/primary witness). Transient owns no separate output-product sibling column (its product is the field trajectory itself, materialized in-column), so the column has no cross-link blocker; both directly-owned constituents being firm is the full promotion warrant. The per-step body remains an opaque-library integrator step quantified over rather than rendered — an obstruction the firm `fold_solve` combinator absorbs (it quantifies over the opaque step), recorded at the lowering layer, NOT a composition-level gate. This chapter carries the *compositional* claim (transient = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `transientsolver.cpp:24-116` (`Solve`) + the K/C/M assembly and ODE-step sites in `timeoperator.cpp` realizing the composition, plus the firm constituent down-links. All L0 line ranges self-verified on-disk via palace-codemap `read_range` (close-brace discipline applied: `Solve` ends `:116`, the loop spans `:77-109`).
