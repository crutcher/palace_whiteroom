# fold-solve-time-step-body

The L3>L2 lowering theme for the [`fold_solve`](../L3/fold_solve.md) **state-threaded fold time-sweep** (`partial-obstruction`) — the L3 explicit value-threaded sweep that threads the persistent field-state `sol` in place through a schedule, advancing it one opaque per-step operator (`time_step_op` → the MFEM `ode->Step` integrator) at a time, where **each step's input is the prior step's in-place write**. The theme dissolves the L3 explicit-tail-recursion iteration view (the value-threaded sweep carrying the **carry-threading `sequential-obstruction`** marker) into the L2 **fold-by-role composition** (the iteration view erased; the obstruction shadowed to L2-vocabulary non-laws), with the **opaque per-step body staying opaque** across the edge. It is the **carry-threaded sibling** of [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md): that theme erases an opaque-library *whole-loop* marker (Palace authors no loop); this theme erases a Palace-authored *carry-threaded sweep* whose per-step body is an opaque-library leaf.

## Slug

`fold-solve-time-step-body`

## Context

The L3 entry [`L3/fold_solve`](../L3/fold_solve.md) — the L3 iteration-rotation view of the state-threaded fold, status `partial-obstruction` — names the L3>L2 hop as **substantive** in its §"Downward to L2" / §"L3 vs L2 distinction"; this chapter is that theme.

**Load-bearing framing.** The per-step body does NOT lower to an L2 composition: unlike L3 [`eigsolve`](../L3/eigsolve.md) — whose per-step body `apply_shift_invert = apply_linop ▷ ksp_solve` IS a visible L2 composition that maps line-for-line (the body-identity-in-form half of [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md)) — `fold_solve`'s per-step body is the **opaque MFEM `ode->Step` integrator leaf** (`palace/models/timeoperator.cpp:410`), which does NOT decompose into L2 base primitives. So the substantive L3>L2 content is **not** a body-composition rotation; it is the **outer-sweep erasure** (the carry-threaded iteration view → an L2 fold-by-role) with the **opaque per-step leaf staying opaque** — the sweep-erasure + the opaque-leaf record, NOT a body decomposition (recorded as the load-bearing scoping in §Justification kind + §"What this lowering does NOT cover").

`fold_solve` and [`solve_family`](../L4/solve_family.md) are the two children of the strawman §3.7 [`iterate_while`](../L4/iterate_while.md) family. `solve_family` has **no L3 entry** (its family loop lifts, embarrassingly parallel), so it has no L3>L2 theme. `fold_solve`'s sweep does NOT lift (carry-threaded + opaque per-step), so it has both an L3 entry and this L3>L2 theme. Among the substantive L3>L2 themes (the erasure-scope taxonomy, `L3-L2/index.md` §Working-Notes), this theme is the **carry-threaded sibling of the opaque-library root**:

- [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md) (firm, **opaque-library** root) — the L3 form names the eigen-iteration `eigen_iterate` by role **with an obstruction marker** (Palace authors no loop), and L2 references the library fold by role only, erasing the marker. The per-step body lifts to a visible L2 composition (identity-in-form).
- `fold-solve-time-step-body` (this theme) — the L3 form renders the carry-threaded sweep as an explicit tail recursion **with a carry-threading `sequential-obstruction` marker** (Palace DOES author the sweep, so it renders), and L2 references the sweep fold by role only, erasing the marker + the obstruction (shadowed to non-laws). The per-step body is an **opaque leaf** that does NOT lower to an L2 composition (the distinguishing contrast with `eigsolve`).

The rotation direction is **L3 → L2**, narrated forward per the high→low discipline (CLAUDE.md §Methodology invariants "Layers are defined high→low"). Notes about the reverse lift (how the L2 fold-by-role lifts to the L3 carry-threaded iteration-view marker) live in the L3 entry's §"L3 vs L2 distinction" and this report's working notes, not this formal chapter.

This is a **genuine vocabulary translation, not an identity-in-named-terms rename** (the §1d smell the redirect names). The L3 vocabulary — an explicit value-threaded tail recursion threading the persistent `sol` in place, a first-class carry-threading `sequential-obstruction` marker on the Palace-authored sweep, the opaque per-step `ode->Step` leaf — is a *different semantic organization* from the L2 vocabulary — a fold-by-role composition with the iteration view erased and the obstruction surviving only as L2-vocabulary non-laws (no commutativity, no whole-march fusion). The reorganization — an explicit obstruction-marked carry-threaded sweep dissolving into a fold-by-role with the obstruction demoted to non-laws and the per-step leaf left opaque — is the substance of the theme.

## L3 form (LHS)

The L3 [`fold_solve`](../L3/fold_solve.md) `partial-obstruction` form (the firm-structure D1 §"Value-threaded form (L3 rendering)"). Transcribed from the L3 entry:

    -- L3 explicit value-threaded time-sweep: operator hoisted, sol threaded IN PLACE,
    -- the carry-threading + opaque per-step leaf made EXPLICIT as the partial-obstruction
    fold_solve :: (op, s0, schedule) -> s_final
    fold_solve op s0 schedule =
      let time_op = build_time_operator op    -- TimeOperator built ONCE, outside the sweep
          _       = construct_integrator op    -- ODE integrator constructed ONCE
          n_step  = num_steps schedule         -- concrete fixed schedule length
      in step_loop 0 (init_field s0)           -- explicit tail recursion; sol threaded IN PLACE
      where
        step_loop step sol =                   -- the SEQUENTIAL-OBSTRUCTION-marked sweep (Palace authors it)
          if step >= n_step then sol
          else let sol' = if step == 0
                            then time_op.Init()           -- seed: sol set IN PLACE
                            else time_op.Step(t, delta_t) -- ode->Step(sol, t, dt): OPAQUE library leaf, advances sol IN PLACE
                   _    = consume (time_op.GetE()) (time_op.GetB())
               in step_loop (step + 1) sol'    -- prior step's IN-PLACE write to sol IS the next step's input

The L3 machinery this theme dissolves is **two** pieces:

1. **The explicit carry-threaded sweep with the `sequential-obstruction` marker.** The `step_loop` tail recursion renders the Palace-authored `for (int step ...)` loop (`palace/drivers/transientsolver.cpp:77`), threading the persistent `sol` in place. The L3 form makes the carry-threading obstruction first-class (each step reads the prior step's in-place write to `sol`; the schedule does not commute). Palace authors this loop, so L3 RENDERS it (the `ksp_solve`/`chebyshev` rendering, NOT the `eigsolve` un-renderable case).

2. **The opaque per-step leaf.** `time_op.Step(t, delta_t)` → `ode->Step(sol, t, dt)` (`palace/models/timeoperator.cpp:410`) is the per-step body — an opaque MFEM `ODESolver` integrator step the L3 view quantifies over, NOT a composition of L3 primitives.

The load-bearing L3 properties this lowering must transport are the L3 entry's laws: **Law 1 (sweep-threading associativity / schedule-split)**, **Law 2 (operator-capture-once / construction-hoist)**, **Law 3 (seed identity on the empty schedule)**, and the load-bearing **non-law** (the carry-threading + opaque-per-step `sequential-obstruction` — no commutativity, no whole-march fusion, no per-step body decomposition).

## L2 form (RHS)

The L3>L2 dissolution produces the L2 **fold-by-role composition** with the iteration view erased. There is **no standalone `L2/fold_solve` entry** (per the L3 entry's §"L3 vs L2 distinction"); the L2 RHS is the fold-by-role form the iteration-rotation erasure produces — the same shape L2 [`eigsolve`](../L2/eigsolve.md) takes for its eigen-iteration fold (named by role, opened only at the body). The L2 rendering:

    -- L2 fold-by-role composition: the carry-threaded sweep referenced AS A COMPOSITION DRIVER
    -- (iteration view erased), the per-step body the opaque integrator leaf (NOT opened)
    fold_solve_L2 :: (op, s0, schedule) -> s_final
    fold_solve_L2 op s0 schedule =
      time_sweep_fold (time_step_op op) s0 schedule    -- the carry-threaded fold NAMED BY ROLE; iteration view erased
      -- where time_step_op = the opaque MFEM ODESolver step (NOT decomposed into L2 primitives)
      -- the operator-capture-once is a composition-setup concern (op bound before the fold)

where:

- **`time_sweep_fold (time_step_op op) s0 schedule`** — the carry-threaded sweep referenced **by role** as an L2 composition driver. The L3 explicit `step_loop` tail recursion (with the carry-threading `sequential-obstruction` marker) collapses to this fold-by-role; the iteration view is **erased** (the obstruction survives only as the L2 non-laws below). This is the same fold-by-role treatment L2 [`eigsolve`](../L2/eigsolve.md) gives its eigen-iteration.
- **`time_step_op`** — the opaque per-step integrator leaf, the SAME at L2 as at L3 (it does NOT decompose into L2 base primitives — the distinguishing contrast with `eigsolve`, whose per-step body opens to `apply_linop ▷ ksp_solve` at L2). The per-step leaf stays opaque across the edge.

The dissolution is **one substantive rewrite** (the outer-sweep erasure) + **one identity** (the opaque per-step leaf, unchanged):

### 1. Explicit carry-threaded sweep + obstruction marker → fold-by-role + obstruction shadowed to non-laws (substantive)

**The load-bearing rotation.** The L3 explicit `step_loop` tail recursion — threading the persistent `sol` in place, carrying the first-class carry-threading `sequential-obstruction` marker — dissolves into the L2 `time_sweep_fold ... by role` composition driver, with the iteration view **erased**. The carry-threading obstruction the L3 form names explicitly survives at L2 only as the **non-laws**: no schedule-commutativity (reordering the steps changes the trajectory), no whole-march fusion (the sweep folds opaque steps, it does not collapse them). This is the **iteration-view erasure** the substantive L3>L2 themes share (`L3-L2/index.md` §"Erasure-scope taxonomy"): L3 makes the obstruction first-class; L2 erases the iteration view and demotes the obstruction to a non-law. It is structurally parallel to [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md)'s marker-erasure — but where `eigsolve`'s L3 marker is "Palace authors no loop" (the loop is un-renderable), `fold_solve`'s L3 marker is the carry-threading obstruction on a Palace-authored, L3-rendered sweep (the carry-threaded root, NOT the opaque-whole-loop root).

### 2. Opaque per-step leaf → opaque per-step leaf (identity, stays opaque)

The per-step body `ode->Step(sol, t, dt)` (`palace/models/timeoperator.cpp:410`) is an **opaque MFEM `ODESolver` integrator leaf** at L3, and it **stays opaque** at L2 — it does NOT open into a composition of L2 base primitives. This is the **distinguishing contrast** with [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md): `eigsolve`'s per-step body lifts to a visible L2 composition (`apply_linop ▷ ksp_solve`, the body-identity-in-form half of that theme), whereas `fold_solve`'s per-step body is an opaque leaf with NO L2 composition (the per-step `ode->Step` does not decompose). So this theme has **no body-identity-in-form half** — the per-step leaf is recorded as opaque at both layers (`obstruction (opaque-library-ownership)`), and the whole substantive content of the theme is the outer-sweep erasure (rewrite 1).

### The opaque per-step sub-leaf — `obstruction (opaque-library-ownership)`

The per-step body bottoms out in an **opaque library step that lives entirely outside Palace** — Palace's `TimeOperator::Step` (`palace/models/timeoperator.cpp:407-413`) is a thin forwarder whose sole act is `ode->Step(sol, t, dt)` (`:410`), dispatching into the MFEM `ODESolver` (selected at construction `palace/models/timeoperator.cpp:312`+). This is the **`obstruction (opaque-library-ownership)`** sub-kind (CLAUDE.md §Methodology invariants "Obstruction themes have two sub-kinds"; the [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md) sibling, the L4>L3 [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md) per-step-leaf precedent): the functionality IS available to Palace but ONLY through a library boundary; Palace never exposes the per-step integrator as a standalone callable. **The negative anchor is Palace's CALL `ode->Step(sol, t, dt)` (`palace/models/timeoperator.cpp:410`), NOT MFEM internals.** The promotion route is NONE in the conventional sense (the theme stays an opaque-leaf record unless Palace re-architects its consumption of MFEM); the value is documenting the boundary so future producers do not waste cycles re-localizing the per-step body inside MFEM.

### What does NOT change in the rotation

The **per-step dataflow position** survives the rotation unchanged — each step's "advance the field-state by one `time_step_op`" passes through unchanged in dataflow position (one opaque step per schedule element). The rotation touches only the **iteration-view vocabulary**: the L3 explicit carry-threaded tail recursion (with the obstruction marker) becomes the L2 fold-by-role composition (obstruction shadowed to non-laws). The **carry-threading sequential-obstruction** is NOT erased in *substance* (the sweep still cannot reorder) — only its *first-class marker* is erased; it survives at L2 as the no-commutativity / no-fusion non-laws.

### What this lowering does NOT cover

- **The per-step integrator interior** — it is the `obstruction (opaque-library-ownership)` sub-leaf. The theme records the per-step body as the opaque `ode->Step` library boundary (`palace/models/timeoperator.cpp:410`) and does NOT lower the MFEM `ODESolver` interior. This is the explicit scope boundary; the per-step body does NOT open into an L2 composition (the contrast with `eigsolve`).
- **No body-composition rotation.** This theme is NOT the `eigsolve` body-identity-on-`apply_shift_invert` shape — `fold_solve`'s per-step body has no L2 composition. The substantive content is the outer-sweep erasure ONLY; the per-step leaf is recorded opaque, not lowered.
- **The state-generated-schedule (greedy SweepAdaptive) variant.** This theme's LHS is the **fixed-list** transient form. The driven-PROM SweepAdaptive state-generated greedy march (`palace/drivers/drivensolver.cpp:231`, schedule generated from the carry: `omega_star = prom_op.FindMaxError(...)` `:389`, bound `:384`) shares the carry-threaded sweep spine but generates its schedule from accumulated state — its dedicated treatment (if warranted) is gated on the cap's OQ `fold-solve-greedy-schedule-source-generalization` (batch-18). This theme covers the fixed-schedule fold only.

## Applicability conditions

The rewrite is valid when all four of the following hold:

1. **The operator is captured once, shared across the sweep.** `op` is bound once, outside the sweep, threaded unchanged into every per-step `time_step_op` (the L3 entry's Law 2). This is what lets the L2 operator-capture be a composition-setup concern (bound before the fold).
2. **The sweep is carry-threaded — each step reads the prior step's output.** `time_step_op op s_k t` reads `s_k` (the L3 entry's load-bearing non-law). This is the source of the L3 carry-threading `sequential-obstruction` marker that the L2 form erases to non-laws.
3. **The per-step body is an opaque per-step operator the sweep quantifies over.** `time_step_op` resolves to a single opaque library CALL (`ode->Step`), NOT a composition of L2 primitives. This is what makes the per-step leaf stay opaque across the edge (and why there is no body-composition rotation — the contrast with `eigsolve`).
4. **The schedule is a fixed precomputed list (Palace transient), NOT state-generated.** The schedule is a uniform `delta_t`/`n_step` march known before the sweep (`palace/drivers/transientsolver.cpp:35-36`). **When the schedule is generated from the carry (SweepAdaptive greedy, `palace/drivers/drivensolver.cpp:389`), this rewrite does not apply** — that is the state-generated superset, batch-18-gated.

## Justification kind

**`structural`** with secondary **`obstruction`** (sub-kind `opaque-library-ownership` on the per-step leaf).

- **Structural** (dominant): the L3 explicit carry-threaded iteration view (the value-threaded tail recursion + the first-class carry-threading `sequential-obstruction` marker) dissolves into the L2 fold-by-role composition (the iteration view erased; the obstruction shadowed to L2-vocabulary non-laws). This is a layer-surface-shape fact — read directly off the structural relationship between the L3 entry's §"Value-threaded form" and the fold-by-role L2 form (the same iteration-view erasure the substantive L3>L2 themes share; `L3-L2/index.md` §"Erasure-scope taxonomy"). The outer-sweep structure is witnessed exactly by the transient driver loop (`palace/drivers/transientsolver.cpp:33-99` + `palace/models/timeoperator.cpp:312,410`).
- **Obstruction** (secondary, `opaque-library-ownership`): the per-step body `ode->Step` is an opaque MFEM library leaf the theme records (negative anchor = Palace's CALL `palace/models/timeoperator.cpp:410`, NOT MFEM internals) rather than lowering — the same sub-kind as the sibling [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md) and the L4>L3 [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md) per-step leaf.

**Abstraction-direction note**: L3 is the higher-abstraction layer (the explicit carry-threaded iteration view with the first-class obstruction marker). L2 is the lower-abstraction layer (the fold-by-role composition with the iteration view erased and the obstruction surviving only as non-laws). The rotation direction is **L3 → L2**, narrated forward per the high→low discipline.

## Speculative L3 operators

None. This theme lowers the firm-structure L3 [`fold_solve`](../L3/fold_solve.md) (`partial-obstruction`) to the L2 fold-by-role form. The per-step `time_step_op` is the opaque-library leaf already recorded at L0 (`palace/models/timeoperator.cpp:410`); no new speculative operator is introduced.

## Evidence

L3 source (the LHS of this rewrite):

- `book/src/L3/fold_solve.md` (`partial-obstruction`) — the L3 state-threaded fold time-sweep: §Signature, §Semantics (the per-step body lifts / the outer sweep does not lift), §"Value-threaded form (L3 rendering)" (the `step_loop` tail recursion — the LHS), §"Algebraic laws" (Law 1 schedule-split, Law 2 operator-capture-once, Law 3 seed identity, the carry-threading + opaque-per-step non-law — the transported properties), §"Downward to L2" / §"L3 vs L2 distinction" (the in-line rotation-direction record this theme realizes), §Status (the `partial-obstruction` basis).

L2 source (the RHS of this rewrite):

- **No `book/src/L2/fold_solve.md`** — there is no standalone L2 entry (the per-step body is an opaque leaf that does not decompose into L2 primitives; the L2 RHS is the fold-by-role form the iteration-rotation erasure produces). The fold-by-role treatment follows L2 [`eigsolve`](../L2/eigsolve.md) (the eigen-iteration fold named by role; the model for the L2 RHS shape).
- `book/src/L3-L2/eigsolve-opaque-eigen-iteration.md` (firm) — the **structurally-parallel** L3>L2 theme this theme follows; the load-bearing contrast is the per-step body (eigsolve's lifts to a visible L2 composition — body-identity-in-form; fold_solve's stays opaque — no body half).
- `book/src/L3-L2/index.md` §"Erasure-scope taxonomy" — the substantive-L3>L2 axis this theme joins (the carry-threaded sibling of the opaque-library root).

L0 evidence (the fixed-schedule fold-sweep witness):

- **Transient fixed-schedule time-march (positive, the LHS witness):** (`palace/drivers/transientsolver.cpp` + `palace/models/timeoperator.cpp`):
  - `palace/drivers/transientsolver.cpp:33` — `TimeOperator time_op(iodata, space_op, dJdt_coef)` (operator built once, outside the sweep — the operator-capture hoist).
  - `:35` — `delta_t = iodata.solver.transient.delta_t` (the uniform timestep).
  - `:36` — `n_step = config::GetNumSteps(0.0, iodata.solver.transient.max_t, delta_t)` (the fixed loop bound).
  - `:77` — `for (int step = 0; step < n_step; step++)` (the Palace-authored sweep the L3 tail recursion renders + this theme erases to the L2 fold-by-role).
  - `:89` — `time_op.Init()` (the seed `s0` set IN PLACE).
  - `:93` — `time_op.Step(t, delta_t)` (the per-step body call).
  - `:98` — `time_op.GetE()` (per-step `(E, B)` readout of the persistent `sol`).
  - `:99` — `time_op.GetB()` (per-step readout).
  - `palace/models/timeoperator.cpp:312` — `op = std::make_unique<TimeDependentFirstOrderOperator>(...)` (the per-step ODE operator constructed once).
  - `:410` — `ode->Step(sol, t, dt)` (the **opaque MFEM `ODESolver` step** advancing `sol` IN PLACE; the carry-threading `sequential-obstruction` + the `obstruction (opaque-library-ownership)` per-step leaf — negative anchor = Palace's CALL, NOT MFEM internals).
- **Driven-PROM SweepAdaptive state-generated greedy march (positive, the carry-threaded-spine second witness — NOT covered by this theme's fixed-list LHS, cited for the structural-parallel sweep spine):** (`palace/drivers/drivensolver.cpp`):
  - `:231` — `ErrorIndicator DrivenSolver::SweepAdaptive(SpaceOperator &space_op) const` (the greedy state-threaded march entry).
  - `:384` — `for (std::size_t it0 = it; it < max_size_per_excitation && memory < convergence_memory; it++)` (the state-derived loop bound — the scope-boundary contrast with this theme's fixed `n_step`).
  - `:389` — `omega_star = prom_op.FindMaxError(excitation_idx)[0]` (the state-derived per-step input — the schedule-source variant the fixed-list LHS does NOT cover).

Concept-page references:

- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the carry-threading IS a sequential obstruction (each step reads the prior step's in-place write to `sol`); the L3 form names it first-class, the L2 form erases it to non-laws. Additionally the per-step body is an opaque-library step (the second obstruction, the per-step leaf).
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — the body-lifts-but-loop-doesn't partial case the L3 entry records.
- [`state-stratification`](../concepts/state-stratification.md) — the captured operator stratum (hoisted outside the sweep) the L2 operator-capture realizes as a composition-setup concern.

## Status

`firm` — on the **structural rotation** (the outer-sweep erasure). The iteration-view erasure (the L3 explicit carry-threaded tail recursion + first-class `sequential-obstruction` marker → the L2 fold-by-role composition with the obstruction shadowed to non-laws) is read **directly off** the structural relationship between the firm-structure L3 entry's §"Value-threaded form" and the fold-by-role L2 form, witnessed exactly by the transient driver loop (`palace/drivers/transientsolver.cpp:33-99` + `palace/models/timeoperator.cpp:312,410`), with the driven-PROM SweepAdaptive sweep (`palace/drivers/drivensolver.cpp:231-389`) the structurally-parallel second carry-threaded-spine witness. The operator-capture hoist, the in-place `sol` threading, and the opaque per-step call are positive source facts. Justification is `structural` + secondary `obstruction (opaque-library-ownership)` on the per-step leaf. No speculative operator introduced. This theme is the **carry-threaded sibling** of the firm [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md) — same iteration-view erasure, but where `eigsolve`'s L3 marker is "Palace authors no loop" and its per-step body lifts to an L2 composition (body-identity half), `fold_solve`'s L3 marker is the carry-threading obstruction on a Palace-authored sweep and its per-step body is an opaque leaf (no body half).

**On the per-step opaque-library sub-leaf (load-bearing scoping).** The per-step body `ode->Step(sol, t, dt)` (`palace/models/timeoperator.cpp:410`) is an `obstruction (opaque-library-ownership)` sub-leaf — the MFEM `ODESolver` interior is library-owned, never exposed by Palace standalone, with NO conventional promotion route. This does **NOT** demote the whole theme to obstruction: the theme is `firm` on the *outer-sweep structural rotation* (the iteration-view erasure, read off positive source); only the *per-step body* is the opaque leaf, recorded (negative anchor = Palace's CALL `:410`) rather than lowered. Unlike the `eigsolve` sibling (whose per-step body DOES open to an L2 composition), `fold_solve`'s per-step body stays opaque — so this theme has no body-identity half; its whole substantive content is the sweep erasure.

**Scope (load-bearing)**: this theme covers the **fixed-schedule** fold erasure, witnessed by the **transient** pipeline. The **driven-PROM SweepAdaptive** state-generated greedy march (`palace/drivers/drivensolver.cpp:231-389`) shares the carry-threaded sweep spine but generates its schedule from the carry — its dedicated treatment (if warranted) is gated on the cap's OQ `fold-solve-greedy-schedule-source-generalization` (batch-18), NOT covered here. The other three pipelines: electrostatic + magnetostatic are the independent-**map** [`solve_family`](../L4/solve_family.md) (no carry — no L3 entry, no L3>L2 theme); eigenmode's eigen-iteration is the opaque-library [`eigsolve`](../L3/eigsolve.md). Do NOT claim cross-pipeline generality beyond the fixed-schedule transient fold + the SweepAdaptive carry-threaded-spine parallel.

This theme is the **L3>L2 outer-sweep erasure** for the `fold_solve` chain. It realizes the in-line rotation direction the L3 entry's §"Downward to L2" records and is the authoritative home for the carry-threaded sweep-erasure stratum, structurally parallel to the opaque-library [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md).
