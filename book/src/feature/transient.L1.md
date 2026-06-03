---
kind: feature-surface
feature: transient
level: L1
status: firm
composes:
  - book/src/L1/fe_assemble.md (firm — assemble the time-domain operators K/C/M once)
  - book/src/L4/fold_solve.md (firm — the state-threaded time-march fold; no separate L1 fold entry, see note)
l0_ground_truth:
  - palace/drivers/transientsolver.cpp:24-116 (TransientSolver::Solve)
  - palace/models/timeoperator.cpp:65-67 (K/C/M), :407-413 (TimeOperator::Step)
---

# transient — L1 composition-root

The **transient simulation feature**, presented at L1 as a pure-function composition of firm L1 operators. This is the **pure-function feature surface**: the same composition root as the [L4 chapter](./transient.L4.md), but expressed in L1 vocabulary (explicit per-operator pure functions, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole feature do these L1 operators add up to?"

At L1 the transient feature is a pure function `config → field trajectory` built from the firm L1 [`fe_assemble`](../L1/fe_assemble.md) operator plus a **pure state-threaded fold** over a pure per-step advance, with the **mutation already lifted** (the L0 in-place `ode->Step(sol, t, dt)` field-state advance is lifted to a value-returning `step :: State -> Time -> State` per the L1>L0 mutation rotation; the persistent `sol` carry becomes the fold's threaded accumulator).

## The composition

    -- inputs = config; output = the field-state trajectory (the physical product)
    transient :: TransientConfig -> FieldTrajectory
    transient cfg =
      let space    = nd_space cfg
          k        = fe_assemble space [ curl_curl (reluctivity cfg) ]   -- (1) assemble K
          c        = fe_assemble space [ conductivity_term cfg ]         --     assemble C
          m        = fe_assemble space [ permittivity_mass cfg ]         --     assemble M (all once)
          op       = time_operator (k,c,m) (dJdt cfg)                    -- captured ODE operator (read-only)
          s0       = init_state cfg                                      -- seed field-state
          schedule = uniform_steps (delta_t cfg) (n_step cfg)            -- fixed [Time] schedule
      in  scanl_state (\s t -> step op s t) s0 schedule                  -- (2) pure state-threaded march → trajectory

1. **Assemble K / C / M once** — [`fe_assemble`](../L1/fe_assemble.md) (**firm**). The L1 assemble fold `K = Σ_i A(space, termᵢ)` (and likewise C, M), each over its weak-form term list. Pure: consumes the Nédélec space + term list, produces a fresh operator. Transient assembles three (the second-order wave-equation `M s'' + C s' + K s = -dJ/dt` form). L0: `space_op.GetStiffnessMatrix(...)` / `GetDampingMatrix(...)` / `GetMassMatrix(...)` (`palace/models/timeoperator.cpp:65-67`).

2. **Pure state-threaded time-march** — the pure fold `scanl_state (step op) s0 schedule`. Each `step op s t` is the **mutation-lifted pure per-step advance** `s' = step(op, s, t)` — the L1 form of the L0 in-place `ode->Step(sol, t, dt)` (the persistent `sol` field-state advance lifted to a value-returning function: read the prior state, return the next). The fixed-operator reuse (the same `op` across all steps) is explicit: `op` is bound once in the `let` and read by every `step`. The **carry-threading** is the defining shape — `step op s_k t_{k+1}` reads `s_k` (the prior step's output), so the steps are strictly sequential and do not commute. The trajectory is the `scanl` of intermediate states (each `(E, B)` consumed per step for postprocessing, `transientsolver.cpp:98-99`). L0: the loop `transientsolver.cpp:77`, the seed `time_op.Init()` `:89`, the per-step `time_op.Step(t, delta_t)` `:93`.

   The per-step `step op` bottoms out in an **opaque library integrator step** (the MFEM ODE solver, internally an implicit linear solve) — at L1 the pure function quantifies over the opaque step rather than rendering it; the opacity is recorded at the lowering layer as `obstruction (opaque-library-ownership)`. There is no per-step `ksp_solve` cap in the transient surface (unlike the fixed-operator map drivers): the implicit solve lives *inside* the opaque step, not as a user-visible map element.

## Inputs / outputs (the feature surface)

- **Input — config.** `TransientConfig` (mesh + order → Nédélec H(curl) space; material coefficients → K/C/M terms; time-domain excitation `J(t)` + `dJ/dt` → per-step forcing; `delta_t` + `max_t` → fixed `[Time]` schedule). All read-only.
- **Output — the physical product.** The **time-domain field-state trajectory** — the per-step `(E, B)` field bundles (`time_op.GetE()` / `GetB()`, `transientsolver.cpp:98-99`) measured by the per-step postprocess (`:104`) and finalized (`:114`), plus the returned error indicator + global dof count (`:115`).

## L1 vs L4

The L1 and L4 composition roots express the **same feature**; they differ in vocabulary:
- **L1** (this chapter): the firm [`fe_assemble`](../L1/fe_assemble.md) wired by a `let`, plus an explicit pure state-threaded fold (`scanl_state`) over a pure per-step advance; the fixed-operator reuse is a value bound once and read by every step; the carry-threading is the explicit accumulator of the fold.
- **L4** ([`transient.L4`](./transient.L4.md)): the march is the [`fold_solve`](../L4/fold_solve.md) combinator (the state-threaded fold made *structural* — the operator-capture-once typed `readonly`, the carry-threading typed, the map/fold axis the strawman §3.7 degenerate-vs-non-degenerate distinction); the assemble is the [`fe_assemble`](../L4/fe_assemble.md) fold combinator. The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinator names.

**Note on the fold operator's home.** There is no separate `book/src/L1/fold_solve.md` — the state-threaded fold is named as a firm combinator at [L4](../L4/fold_solve.md) (firm c058) and has an L3 standing entry ([`L3/fold_solve`](../L3/fold_solve.md), `partial-obstruction`); at L1 the fold appears as the plain pure `scanl_state` over the mutation-lifted per-step advance (no dedicated L1 operator chapter is warranted — the L1 march is the generic pure fold, with the per-step advance the only operator, and that bottoms out opaque). This column therefore links the fold DOWN to the firm L4 combinator and records the L1 form inline.

The L1→L0 direction (how each pure operator lowers to the in-place driver writes) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 operator | Status | L0 site |
|---|---|---|---|
| assemble K / C / M once | [`fe_assemble`](../L1/fe_assemble.md) | firm | `timeoperator.cpp:65-67` |
| state-threaded march fold | [`fold_solve`](../L4/fold_solve.md) (L4 combinator; L1 = pure `scanl_state`) | firm | `transientsolver.cpp:77, 89, 93`; `timeoperator.cpp:410` |
| per-step body (opaque ODE step) | quantified-over; `obstruction (opaque-library-ownership)` at lowering | — | `timeoperator.cpp:407-413` |

## Status

`firm` — the L1 pure-function composition root for the transient feature, the spine's first **fold-pipeline** witness, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic.L1](./electrostatic.L1.md) / [magnetostatic.L1](./magnetostatic.L1.md) exemplars but composing a *fold* rather than a *map*. **Promoted `seed → firm` cycle-085** under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers). Both directly-owned constituents are firm: the assemble constituent ([`fe_assemble`](../L1/fe_assemble.md), three operators) and the march constituent (the firm [`fold_solve`](../L4/fold_solve.md) combinator, transient is its default/primary witness, rendered at L1 as a pure `scanl_state` over a mutation-lifted per-step advance whose body bottoms out in an opaque-library integrator step — quantified over, not rendered). Transient owns no output-product sibling column (its product is the trajectory itself), so there is no cross-link blocker. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 driver range `transientsolver.cpp:24-116` + the K/C/M assembly and ODE-step sites in `timeoperator.cpp` realizing the composition, plus the firm L1/L4 constituent down-links. All L0 line ranges self-verified on-disk via palace-codemap `read_range`.
