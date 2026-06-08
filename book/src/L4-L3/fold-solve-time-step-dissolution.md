# fold-solve-time-step-dissolution

The L4>L3 lowering theme for the [`fold_solve`](../L4/fold_solve.md) **state-threaded fold outer-driver combinator** — the L4 combinator `fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule` that captures the operator once, seeds an immutable field-state carry once, and threads it forward through a schedule by `foldl`, advancing it one opaque per-step operator (`time_step_op`) at a time where **each step's input is the prior step's output**. The theme dissolves the L4 `foldl` combinator (the once-captured `readonly` `op` stratum, the immutable carry threaded functionally, the abstract schedule) into the L3 **explicit imperative time-sweep that threads the field-state `sol` IN PLACE**: a positional `for (int step ...)` loop, the operator construction hoisted by hand outside the loop, the persistent `sol` field-state mutated in place per step, the per-step body bottoming out in the **opaque MFEM `ODESolver` step** (`obstruction (opaque-library-ownership)` sub-leaf). It is the **fold-sibling** of the [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) MAP-shell dissolution: that theme dissolves the independent `map` over an RHS family (embarrassingly parallel, NO obstruction); this theme dissolves the sequential `foldl` of a state-threaded march (each step reads the prior carry — a genuine `sequential-obstruction`, plus an opaque per-step library leaf).

## Slug

`fold-solve-time-step-dissolution`

## Context

[`fold_solve`](../L4/fold_solve.md) is the L4 **state-threaded fold outer-driver combinator**, one coordination shell *above* an opaque per-step solve. The combinator's own §"Lowers to" names the dissolution to L3 as **substantive** (not identity-in-form) and records the rotation *direction* in-line per the high→low discipline, deferring the theme itself to this chapter (canonical slug `fold-solve-time-step-dissolution`).

`fold_solve` and [`solve_family`](../L4/solve_family.md) are the two children of the strawman §3.7 [`iterate-while`](../L4/iterate-while.md) family: a **map is the degenerate fold whose step ignores the accumulator**, `fold_solve` is the **non-degenerate** member that threads it. Their two L4>L3 dissolutions are correspondingly siblings, and this theme is **structurally parallel** to [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) — but the load-bearing difference between the two RHS images IS the map/fold axis:

- [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) — the L4 `map` over an independent RHS family → an L3 positional accumulating `for` that writes each member into its own collection slot. The family loop carries **NO `sequential-obstruction`** (the members are independent — an embarrassingly-parallel sweep written sequentially).
- `fold-solve-time-step-dissolution` (this theme) — the L4 `foldl` of a state-threaded march → an L3 positional `for` that threads the field-state `sol` **in place**, each step reading the prior step's output. The loop carries a **genuine `sequential-obstruction`** (the carry-threading cannot reorder) AND an **opaque-library per-step leaf** (the `ode->Step` integrator boundary). This is the structural contrast the harvester named: the map's RHS is independent-parallel; the fold's RHS is sequential-with-an-opaque-leaf.

The rotation direction is **L4 → L3**, narrated forward per the high→low discipline (CLAUDE.md §Methodology invariants "Layers are defined high→low"). Notes about the reverse lift (how the L3 in-place-threading loop lifts back into the `foldl` combinator, what evidence licenses recovering the immutable carry from the in-place `sol`) live in the cap's §"L4 vs L3 distinction" and in this report's working notes, not in this formal chapter.

This is a **genuine vocabulary translation, not an identity-in-named-terms rename** (CLAUDE.md §Methodology invariants vocabulary-shift redirect; a degenerate identity-in-named-terms lowering is a §1d smell). The L4 vocabulary — `foldl`, the `readonly` once-captured operator stratum, the **immutable carry threaded functionally** (`\s t -> time_step_op op s t` returns a fresh `TimeState`), the abstract `schedule` ranged over, the opaque quantified-over `time_step_op` — is a *different semantic organization* from the L3 vocabulary — an explicit positional `for` over a step counter, a hand-hoisted operator construction, the **persistent `sol` field-state mutated IN PLACE** (`ode->Step(sol, t, dt)` advances `sol` destructively), a concrete `delta_t`/`t` march bounded by `n_step`, and the per-step body resolved to a concrete library CALL. The reorganization — a single combinator naming the whole march with the carry threaded purely, dissolving into an imperative loop that destructively advances a single persistent state vector through an opaque integrator — is the substance of the theme. The three things that change across the vocabularies are catalogued in §"L3 form (RHS)".

## L4 form (LHS)

The L4 [`fold_solve`](../L4/fold_solve.md) combinator — the firm-structure D1 fold shape (the firm entry §Signature). The entry point (default fixed-list surface), transcribed from the firm cap:

    -- entry point (default surface): fixed-list state-threaded fold
    -- capture op once, seed s0 once, thread the IMMUTABLE carry through a precomputed schedule
    fold_solve :: OpParams -> TimeState -> [Time] -> TimeState
    fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule

    -- the opaque per-step operator the combinator quantifies over (advances the field-state one step;
    -- bottoms out in a library integrator the L4 entry does NOT render):
    time_step_op :: OpParams -> TimeState -> Time -> TimeState

    -- equivalently, the NON-degenerate member of the strawman §3.7 iterate_while family
    -- (carry = field-state + schedule-state; the step reads the PRIOR carry to advance it):
    fold_solve op s0 schedule =
      (iterate_while
         { field: s0, remaining: schedule }       -- carry: persistent field-state + schedule-state
         (\c -> not (null c.remaining))            -- continue while schedule remains
         (\c -> let t  = head c.remaining
                    s' = time_step_op op c.field t -- prior FIELD read: this is the fold, not a map
                in { state: { field: s', remaining: tail c.remaining } }))
        .final_state.field                         -- == foldl (\s t -> time_step_op op s t) s0 schedule

The fold-shell machinery this theme dissolves is **three** pieces (the same three the map-sibling dissolves — but the fold's carry-threading makes each translate differently):

1. **The once-captured `readonly` operator stratum.** `op : OpParams` is bound *once, outside the `foldl`*, per [`state-stratification`](../concepts/state-stratification.md); it is the shared `readonly` stratum threaded *unchanged* into every per-step `time_step_op`. The `op`-dependent integrator construction (the L4 image of `TimeOperator` built once with its ODE integrator constructed once) is **invariant across the fold and hoists out of it** — the same operator-capture-once law the map sibling has.

2. **The immutable field-state carry threaded by `foldl`.** `foldl (\s t -> time_step_op op s t) s0 schedule` threads the carry `s : TimeState` forward, each step producing a *fresh* carry `s'` from the prior `s`. **This is what makes the combinator a fold and not a map**: the step `time_step_op op s t` reads `s` (the prior step's output), so the steps are strictly sequential and do not commute. The carry is **functional/immutable** at L4 (each `time_step_op` returns a new `TimeState`).

3. **The abstract schedule + the opaque per-step operator.** `schedule : [Time]` is the abstract list the fold ranges over (the default fixed-list surface); `time_step_op` is the opaque per-step operator the combinator only **quantifies over** — at L4 the entry names it by role and does not render its body.

The load-bearing L4 properties this lowering must transport are the cap's fold identities (the firm cap §"Algebraic laws"): **Law 1 (fold-threading associativity / schedule-split)** — `fold_solve op s0 (a ++ b) = fold_solve op (fold_solve op s0 a) b`, the `foldl (a++b) = foldl b . foldl a` checkpoint-resume law (the fold analog of the map's concatenation-homomorphism, but *threading* not *distributing*); **Law 2 (operator-capture-once / construction-hoist)** — the `op`-dependent integrator construction is invariant across the fold and hoists out of it; **Law 3 (seed left-identity on the empty schedule)** — `fold_solve op s0 [] = s0`. And the load-bearing **non-law** (the map/fold distinction): **NO commutativity / distribution / element-independence** — reordering the schedule changes the trajectory (the carry-threading is a `sequential-obstruction`).

## L3 form (RHS)

The L4>L3 dissolution produces the L3 **explicit imperative time-sweep threading the field-state `sol` IN PLACE** — the Palace C++ transient shape (the firm cap §Specializations, transient witness). The L3 rendering (using the L3 value-thread vocabulary, with the per-step body delegated to the opaque library integrator):

    -- L3 explicit time-sweep: operator hoisted outside the loop, the persistent field-state
    -- threaded IN PLACE through a concrete delta_t/t march, the per-step body an opaque library call
    fold_solve_L3 :: (op, s0, schedule_params) -> sol_final
    fold_solve_L3 op s0 schedule_params =
      let time_op  = build_time_operator op    -- 1. build TimeOperator ONCE, outside the loop
      let _        = construct_integrator op    --    ODE integrator constructed ONCE (op captured once)
      let delta_t  = schedule_params.delta_t     -- 2. concrete uniform timestep
      let n_step   = num_steps schedule_params    --    concrete fixed schedule length
      let sol      = init_field s0               -- the persistent field-state, set IN PLACE by Init()
      let t        = 0
      let _ =                                     -- 3. positional for-loop threading sol IN PLACE
            for_step (0 .. n_step - 1) (\step ->
              if step == 0
                then time_op.Init()              -- seed: set sol IN PLACE (initial conditions)
                else time_op.Step(t, delta_t))   -- per-step: ode->Step(sol, t, dt) advances sol IN PLACE
                                                 --   == the opaque MFEM ODESolver step (library boundary)
      in time_op.GetE()  -- final field-state read out (E, B) of the persistent sol

where:

- **`build_time_operator op` + `construct_integrator op`** are the L3 image of the operator-capture hoist — `TimeOperator time_op(iodata, space_op, dJdt_coef)` (`transientsolver.cpp:33`) with its ODE integrator constructed once (`op = std::make_unique<TimeDependentFirstOrderOperator>(...)`, `timeoperator.cpp:312`), placed *outside* the `for` loop by hand. The L4 `readonly` once-captured stratum dissolves into this explicit placement; there is no type-level enforcement at L3 that the operator is not rebuilt per step — it is a *coding convention* (the construction sits outside the loop).
- **`delta_t` + `n_step`** are the concrete schedule — `delta_t = iodata.solver.transient.delta_t` (the uniform timestep, `transientsolver.cpp:35`) and `n_step = config::GetNumSteps(0.0, max_t, delta_t)` (the fixed schedule length, `:36`). The L4 abstract `[Time]` schedule dissolves into the concrete `delta_t`/`t` march bounded by the integer `n_step`.
- **`for_step (0 .. n_step - 1)`** is the explicit `for (int step = 0; step < n_step; step++)` (`transientsolver.cpp:77`) — the L4 `foldl` collapsed to a positional loop over a step counter.
- **`time_op.Init()`** (`transientsolver.cpp:89`) sets the seed `sol` IN PLACE (the `step == 0` initial conditions branch); **`time_op.Step(t, delta_t)`** (`:93`) is the per-step body, dispatching to `ode->Step(sol, t, dt)` (`timeoperator.cpp:410`) — the **opaque MFEM `ODESolver` step** that advances the persistent `sol` field-state IN PLACE. This theme treats `ode->Step` as one opaque per-step library call (the `obstruction (opaque-library-ownership)` sub-leaf, §"The opaque per-step sub-leaf"); it does NOT render the integrator interior.
- the per-step `(E, B)` readout (`time_op.GetE()` `:98`, `time_op.GetB()` `:99`) reads the *current* persistent `sol` for postprocessing — the L4 trajectory consumer.

The dissolution is **three** coordinated rewrites, one per piece of L4 fold-shell machinery — and each is a genuine vocabulary translation, NOT a rename:

### 1. Once-captured `readonly` operator stratum → operator construction hoisted outside the `for`

The L4 once-captured `op : OpParams` (the `readonly` stratum bound outside the `foldl`) dissolves into the L3 `TimeOperator time_op(...)` + the ODE integrator construction placed *by hand* outside the `for` loop. This is the cap's Law 2 (the `op`-dependent integrator construction is invariant across the fold and hoists out of it) realized as a coding convention: in Palace the placement is witnessed directly — `TimeOperator time_op(iodata, space_op, dJdt_coef)` (`transientsolver.cpp:33`) and the integrator construction (`timeoperator.cpp:312`) are *outside* the `for` (`transientsolver.cpp:77`). The L4 type-level guarantee (the `readonly` stratum forbids per-step operator mutation) dissolves into a coding convention at L3: the construction sits outside the loop, but nothing at L3 type-enforces it. (This is the **same** translation as the map sibling's rewrite 1 — the operator-capture hoist is shared by the whole §3.7 family; the fold and the map differ in the *carry*, not the operator-capture.)

### 2. Immutable functional carry → persistent field-state `sol` threaded IN PLACE

**The load-bearing fold-specific translation.** The L4 `foldl (\s t -> time_step_op op s t) s0 schedule` threads an **immutable** carry — each step's `\s t -> ...` consumes the prior `s : TimeState` and returns a *fresh* `TimeState`. This dissolves into the L3 **in-place mutation of a single persistent field-state `sol`**: there is no fresh state per step; instead `ode->Step(sol, t, dt)` (`timeoperator.cpp:410`) advances the *same* `sol` vector destructively, and the next step reads that mutated `sol`. The functional carry-threading `s_{k+1} = time_step_op op s_k t` becomes the imperative `sol` is mutated in place; the prior step's mutation IS the next step's input. This is the precise vocabulary shift the redirect demands a lowering narrate: **functional immutable carry → in-place mutation of `sol`**. The sequential data-dependence the L4 fold makes structural (the step reads the prior carry) survives as the L3 read-after-write on the shared `sol` vector — a `sequential-obstruction` (the loop cannot reorder; each iteration reads the prior iteration's write to `sol`). This is exactly what distinguishes the fold's RHS from the map sibling's RHS: the map writes each member into its **own** collection slot (no cross-iteration dependence, NO obstruction); the fold rewrites the **same** `sol` (cross-iteration read-after-write, a genuine obstruction).

### 3. Abstract schedule + opaque per-step operator → concrete `delta_t`/`t` march + the `ode->Step` library boundary

The L4 abstract `schedule : [Time]` dissolves into the concrete uniform `delta_t`/`t` march: `delta_t` (`transientsolver.cpp:35`) the uniform timestep, `n_step` (`:36`) the fixed loop bound, the loop counter `step` (`:77`) advancing `t += delta_t` per iteration. The abstract list ranged over by `foldl` becomes a concrete integer-bounded counting loop. And the L4 opaque quantified-over `time_step_op` dissolves into the concrete per-step library CALL `ode->Step(sol, t, dt)` (`timeoperator.cpp:410`) — the **opaque MFEM `ODESolver` step**. At L4 the entry only names `time_step_op` by role and quantifies over it; at L3 the per-step body resolves to a concrete library boundary the theme records as an `obstruction (opaque-library-ownership)` sub-leaf (§"The opaque per-step sub-leaf"). The abstract `time_step_op` → the `ode->Step` library boundary is the third vocabulary shift.

### The opaque per-step sub-leaf — `obstruction (opaque-library-ownership)`

The per-step body bottoms out in an **opaque library step that lives entirely outside Palace** — Palace's `TimeOperator::Step` (`timeoperator.cpp:407-413`) is a thin forwarder whose sole act is `ode->Step(sol, t, dt)` (`:410`), dispatching into the MFEM `ODESolver` (`GeneralizedAlphaSolver` / `SDIRK23Solver` / `ARKStepSolver`, selected at construction `timeoperator.cpp:312`+). The integrator's step semantics — the implicit-stage Newton solves, the Butcher-tableau stage combination, the internal sub-state — are **MFEM-owned, not Palace-owned**. This is the **`obstruction (opaque-library-ownership)`** sub-kind (CLAUDE.md §Methodology invariants "Obstruction themes have two sub-kinds"; the [`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) precedent, the sibling [`eigsolve`](../L4/eigsolve.md) opaque-library shape): the functionality IS available to Palace but ONLY through a library boundary; Palace never exposes the per-step integrator as a standalone callable; there is nothing for Palace to fix upstream. **The negative anchor is Palace's CALL `ode->Step(sol, t, dt)` (`timeoperator.cpp:410`), NOT MFEM internals** (per the `time-step-op-opaque-mfem-integrator-boundary` framing) — the obstruction is recorded at the Palace/MFEM ownership boundary, and the theme does not (and cannot) cite or lower the MFEM integrator interior. The promotion route is NONE in the conventional sense (the theme stays an opaque-leaf record unless Palace re-architects its consumption of the MFEM integrator — highly unlikely); the value is *documenting the boundary* so future producers do not waste cycles re-localizing the per-step body inside MFEM.

This makes the fold dissolution **distinct from the map sibling** at the per-step level: the map's per-member solve (`ksp.Mult`) delegates to the firm [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) (the per-member body *does* lower); the fold's per-step body does NOT lower — it is an opaque library leaf the theme records, not delegates. The whole-theme status remains `firm` on the *outer-sweep* structural rotation (which IS read off positive source); only the per-step leaf is the opaque-library obstruction.

### What does NOT change in the rotation

The **per-step dataflow position** survives the rotation unchanged — each step's "advance the field-state by one `time_step_op`" passes through unchanged in dataflow position (one opaque step per schedule element); the rotation touches only the **fold-shell vocabulary**: the `readonly` once-captured stratum becomes the hand-hoisted `TimeOperator` construction, the immutable functional carry becomes the in-place-mutated `sol`, the abstract `foldl`-over-`[Time]` becomes the concrete `for`-over-`n_step` with the opaque `ode->Step` per-step body. The **sequential carry-dependence** survives at L3 (the cap's non-law): the loop reads `sol` after the prior step wrote it, so the sweep is a `sequential-obstruction` — it cannot be reordered or parallelized (the structural contrast with the map sibling's embarrassingly-parallel family loop).

### What this lowering does NOT cover

- **The per-step integrator interior** — it is the `obstruction (opaque-library-ownership)` sub-leaf (§"The opaque per-step sub-leaf"). The theme records the per-step body as the opaque `ode->Step` library boundary (`timeoperator.cpp:410`) and does NOT lower the MFEM `ODESolver` interior. This is the explicit scope boundary — the per-step body is library-owned, not a Palace-authored loop the theme rotates.
- **The state-generated-schedule (greedy SweepAdaptive) variant.** This theme's RHS is the **fixed-list** form (transient `transientsolver.cpp:77`-march). The driven-PROM SweepAdaptive state-generated greedy march (`drivensolver.cpp:231`, where the schedule is generated from the carry: `omega_star = prom_op.FindMaxError(...)` `:389`, bound `memory < convergence_memory` `:384`) shares the fold spine but generates its schedule from accumulated state — its dedicated dissolution is a deferred candidate. This theme covers the **fixed-schedule** fold dissolution only; the greedy form is the explicit scope boundary (§Applicability conditions).
- **The L3>L2 hop.** A standalone `L3/fold_solve` entry IS warranted — status `partial-obstruction` (the carry-threading sequential-obstruction + the opaque per-step body, the [`chebyshev`](../L3/chebyshev.md) / `eigsolve` shape). Unlike the map sibling (whose family loop lifts cleanly, NO-ENTRY warrant), the fold loop carries BOTH obstructions, so the L3 [`fold_solve`](../L3/fold_solve.md) entry is the standing iteration-rotation home, and its L3>L2 hop is the dedicated theme [`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md) (the outer-sweep erasure to an L2 fold-by-role + the opaque per-step leaf staying opaque). This L4>L3 theme records only the L4→L3 rewrite *direction*; the L3 entry + its L3>L2 theme are the lower-edge homes.

## Applicability conditions

The rewrite is valid when all four of the following hold (the first three are the fold-shell conditions; the fourth is the schedule-source condition that is the scope boundary):

1. **The operator is captured once, shared across the march.** `op : OpParams` is bound once, outside the `foldl`, and threaded unchanged into every per-step `time_step_op` — the `readonly` once-captured stratum (the firm cap §Signature). This is what lets the L3 `TimeOperator` construction + integrator construction hoist outside the `for` loop (`transientsolver.cpp:33` / `timeoperator.cpp:312`, outside `:77`).

2. **The carry is threaded sequentially — each step reads the prior step's output.** The fold's defining data-dependence: `time_step_op op s_k t` reads `s_k` (the prior carry), so the steps do not commute (the firm cap §"Algebraic laws" non-law). This is what makes the L3 form thread the persistent `sol` IN PLACE with a read-after-write per iteration, and is the source of the L3 loop carrying a **`sequential-obstruction`** (the §"What does NOT change" verdict — the contrast with the map sibling).

3. **The per-step body is an opaque per-step operator the combinator quantifies over.** `time_step_op` is not rendered at L4; at L3 it resolves to a single library CALL (the `ode->Step` integrator step). This is what licenses the `obstruction (opaque-library-ownership)` per-step sub-leaf treatment (§"The opaque per-step sub-leaf"); if the per-step body were a Palace-authored loop it would lower instead of being recorded as an opaque leaf.

4. **The schedule is a fixed precomputed list (Palace transient), NOT state-generated.** The schedule is a uniform `delta_t`/`n_step` march known before the loop (`transientsolver.cpp:35-36`); the loop bound is the integer `n_step`, not a state-derived predicate. **When the schedule is generated from the carry (SweepAdaptive greedy, `drivensolver.cpp:389`), this rewrite does not apply** — that is the state-generated superset (§"What this lowering does NOT cover"). This theme covers the **fixed-schedule** fold only.

## Justification kind

**`structural`** with secondary **`reduction-chain`**.

- **Structural** (dominant): the L4 fold-shell machinery (the once-captured `readonly` operator stratum, the immutable functional carry, the abstract schedule + opaque per-step operator) dissolves into the L3 explicit in-place-threading time-sweep; the fold shell is preserved by construction (every L4 shell piece becomes an L3 shell piece at the same dataflow position — capture-once → hoisted construction, immutable carry → in-place `sol`, abstract schedule + opaque step → concrete march + `ode->Step` library call). The dissolution is read **directly off positive Palace source** — the operator-hoist placement (construction outside the `for`), the in-place `sol` threading, and the opaque per-step call are all witnessed exactly by the transient sweep (`transientsolver.cpp:33-99` + `timeoperator.cpp:312,410`); the driven-PROM SweepAdaptive sweep (`drivensolver.cpp:231-389`) is the structurally-parallel second witness of the fold spine.
- **Reduction-chain** (secondary): the `foldl (\s t -> time_step_op op s t) s0 schedule` desugars to the explicit positional `for` with the carry threaded (the standard `foldl`-to-imperative-loop reduction); the non-degenerate member of the strawman §3.7 `iterate_while` family (the cap's alternate rendering) desugars to the same in-place-threading loop with the carry `{ field, remaining }` becoming the mutated `sol` + the loop counter (`book/src/semantics/index.md:150-184`). The per-step opaque leaf does NOT participate in the reduction chain — it is the obstruction boundary.

**Abstraction-direction note**: L4 is the higher-abstraction layer (the `foldl` combinator, the typed `readonly` once-captured operator stratum, the immutable functional carry, the abstract schedule). L3 is the lower-abstraction layer (the explicit positional `for`, the hand-hoisted operator construction, the in-place-mutated persistent `sol`, the concrete `delta_t`/`n_step` march, the opaque `ode->Step` per-step library call). The rotation direction is **L4 → L3**, narrated forward per the high→low discipline.

## Speculative L4 operators

None. This theme lowers an already-firm L4 combinator ([`fold_solve`](../L4/fold_solve.md)) assembled from the already-firm [`iterate-while`](../L4/iterate-while.md) §3.7 family. The per-step `time_step_op` and the `TimeState` carry are speculative rough-in sub-operators already named in the firm cap's §Dependencies (not introduced here); the per-step `time_step_op` is recorded as the opaque-library obstruction sub-leaf at L0 (`timeoperator.cpp:410`). No new speculative operator is introduced.

## Evidence

L4 source (the LHS of this rewrite):

- `book/src/L4/fold_solve.md` — the L4 state-threaded fold combinator: §Signature (the `fold_solve` / `foldl (\s t -> time_step_op op s t) s0 schedule` shape + the §3.7 carry-form rendering), §Semantics (the direct-fold form + the §3.7 non-degenerate-member rendering), §"Algebraic laws" (Law 1 fold-threading associativity / schedule-split, Law 2 operator-capture-once / construction-hoist, Law 3 seed left-identity, and the load-bearing NON-law: no commutativity / distribution — the map/fold distinction — the transported properties), §"Lowers to" (the in-line rotation-direction record this theme realizes), §Specializations (the two state-threaded sweeps — transient fixed-schedule + SweepAdaptive state-generated), §"The opaque per-step body" (the `obstruction (opaque-library-ownership)` deferral this theme realizes).
- `book/src/L4/iterate-while.md` — the §3.7 family whose non-degenerate carry-threading member the combinator IS (the alternate LHS rendering).
- `book/src/L4/solve_family.md` — the **map sibling** whose dissolution this theme is structurally parallel to (operator-capture hoist shared; the carry/no-carry axis the load-bearing difference).

L3 source (the RHS of this rewrite):

- **`book/src/L3/fold_solve.md` (`partial-obstruction`)** — the standalone L3 entry IS warranted: the carry-threading sequential-obstruction + the opaque per-step body make the L3 form a genuine iteration-rotation `partial-obstruction` (the [`chebyshev`](../L3/chebyshev.md) shape), so the L3 entry — not this dissolution theme — is the authoritative L3-form home, and its L3>L2 hop is the dedicated theme [`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md).
- `book/src/L4-L3/solve-family-map-dissolution.md` — the **map-sibling dissolution** this theme is structurally parallel to; the load-bearing contrast is the RHS obstruction (the map's family loop carries NONE; this fold's loop carries a `sequential-obstruction` + an opaque per-step leaf).
- `book/src/L4-L3/iterate-while-dissolution.md` — the inner-fold combinator dissolution the §3.7 family shares (referenced for the family-parent rendering).

L0 evidence (the fixed-schedule fold-sweep witness):

- **Transient fixed-schedule time-march (positive, the default surface):** (`palace/drivers/transientsolver.cpp` + `palace/models/timeoperator.cpp`):
  - `palace/drivers/transientsolver.cpp:33` — `TimeOperator time_op(iodata, space_op, dJdt_coef)` (operator built once, **outside** the loop — the operator-capture hoist).
  - `:35` — `delta_t = iodata.solver.transient.delta_t` (the uniform timestep — the concrete schedule's step).
  - `:36` — `n_step = config::GetNumSteps(0.0, iodata.solver.transient.max_t, delta_t)` (the fixed schedule length — the concrete loop bound).
  - `:77` — `for (int step = 0; step < n_step; step++)` (the fold loop dissolved to the positional `for`).
  - `:89` — `time_op.Init()` (the seed `s0` — the `step == 0` initial conditions set IN PLACE).
  - `:93` — `time_op.Step(t, delta_t)` (the per-step fold body call — the `step != 0` branch).
  - `:98` — `time_op.GetE()` (per-step `(E, B)` readout of the persistent `sol` — the trajectory consumer).
  - `:99` — `time_op.GetB()` (per-step readout).
  - `palace/models/timeoperator.cpp:312` — `op = std::make_unique<TimeDependentFirstOrderOperator>(...)` (the per-step ODE operator constructed once — the integrator-construction hoist).
  - `:410` — `ode->Step(sol, t, dt)` (the **opaque MFEM `ODESolver` step** advancing the persistent `sol` field-state IN PLACE; the prior step's `sol` is the next step's input — the genuine in-place carry-threading; the `obstruction (opaque-library-ownership)` per-step sub-leaf negative anchor — Palace's CALL, NOT MFEM internals).
- **Driven-PROM SweepAdaptive state-generated greedy march (positive, the second fold-spine witness — NOT covered by this theme's RHS, cited for the structural-parallel fold spine):** (`palace/drivers/drivensolver.cpp`):
  - `:73` — `adaptive ? SweepAdaptive(space_op) : SweepUniform(space_op)` (the adaptive dispatch).
  - `:231` — `ErrorIndicator DrivenSolver::SweepAdaptive(SpaceOperator &space_op) const` (the greedy state-threaded march entry — the second fold witness).
  - `:384` — `for (std::size_t it0 = it; it < max_size_per_excitation && memory < convergence_memory; it++)` (the state-derived loop bound — the schedule generated from the carry, the scope-boundary contrast with this theme's fixed `n_step`).
  - `:389` — `omega_star = prom_op.FindMaxError(excitation_idx)[0]` (the state-derived per-step input — the schedule-source variant the fixed-schedule RHS does NOT cover).

Concept-page references:

- [`state-stratification`](../concepts/state-stratification.md) — the `op` shared `readonly` operator stratum captured once at `TimeOperator` construction; the capture-once typing that dissolves to the hand-hoisted operator construction.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the carry-threading IS a sequential obstruction (each step reads the prior step's in-place write to `sol`; the schedule does not commute) — the load-bearing contrast with the map sibling's commuting family loop. Additionally the per-step body is an opaque-library step (the second obstruction, the per-step sub-leaf).
- [`variant-absorption`](../concepts/variant-absorption.md) — the schedule-source axis (`fixed-list | state-generated`, the scope boundary) and the absorbed element-type / carry-shape axes.

## Status

`firm` — on the **structural rotation**. The fold-shell dissolution (the once-captured `readonly` operator stratum → the `TimeOperator` + integrator construction hoisted outside the `for`; the immutable functional carry → the persistent `sol` field-state threaded IN PLACE; the abstract schedule + opaque per-step operator → the concrete `delta_t`/`n_step` march + the opaque `ode->Step` library call) is read **directly off positive Palace source** — every piece of the outer-sweep rotation shape is witnessed exactly by the transient sweep (`transientsolver.cpp:33-99` + `timeoperator.cpp:312,410`), with the driven-PROM SweepAdaptive sweep (`drivensolver.cpp:231-389`) the structurally-parallel second fold-spine witness. Justification is `structural` + secondary `reduction-chain`. This theme is the **fold-sibling** of [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) — same operator-capture hoist, opposite carry axis (the map's RHS carries NO obstruction; this fold's RHS carries a `sequential-obstruction` + an opaque per-step leaf).

**On the per-step opaque-library sub-leaf (load-bearing scoping).** The per-step body `ode->Step(sol, t, dt)` (`timeoperator.cpp:410`) is an `obstruction (opaque-library-ownership)` sub-leaf — the MFEM `ODESolver` interior is library-owned, never exposed by Palace as a standalone callable, with NO conventional promotion route. This does **NOT** demote the whole theme to obstruction: the theme is `firm` on the *outer-sweep structural rotation*; only the *per-step body* is the opaque leaf, and the theme **records** that boundary (the negative anchor is Palace's CALL `:410`, NOT MFEM internals) rather than lowering it. The distinction from the map sibling: the map's per-member `ksp.Mult` *does* lower (delegated to [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md)); the fold's per-step `ode->Step` does NOT lower (opaque library leaf).

**Scope (load-bearing)**: this theme covers the **fixed-schedule** fold dissolution, witnessed by the **transient** pipeline (the fixed `delta_t`/`n_step` march). The **driven-PROM SweepAdaptive** state-generated greedy march (`drivensolver.cpp:231-389`) shares the fold spine but generates its schedule from the carry (the next sample `omega_star = FindMaxError(state)` `:389`, the state-derived bound `:384`) — its dedicated dissolution is a deferred candidate, NOT covered here. The other three pipelines: electrostatic + magnetostatic are the independent-**map** [`solve_family`](../L4/solve_family.md) (no carry — the map sibling, NOT folds); eigenmode's eigen-iteration is opaque-library-owned ([`eigsolve`](../L4/eigsolve.md), not probed as a fold). Do NOT claim cross-pipeline generality beyond the fixed-schedule transient fold + the SweepAdaptive fold-spine parallel.

## L4 vs L3 distinction

- **L4**: the `foldl`-combinator fold shell. `fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule`; the operator `op : OpParams` is a `readonly` stratum captured **once, outside the fold** (the capture-once is *structural*, type-enforced); the field-state carry is **immutable**, threaded functionally (each step returns a fresh `TimeState`); the schedule is an abstract `[Time]`; the per-step `time_step_op` is opaque, quantified-over; the fold is sequential (each step reads the prior carry — a typed data-dependence).
- **L3**: the value-threaded explicit time-sweep. The `foldl` has dissolved to an explicit positional `for (int step ...)` over a step counter; the operator construction (`TimeOperator time_op(...)` + the integrator) is hoisted outside the loop **by hand** (a coding convention, not a type-level stratification); the field-state is a **persistent `sol` vector mutated IN PLACE** (`ode->Step(sol, t, dt)` advances it destructively); the schedule is the concrete `delta_t`/`n_step` march; the per-step body is the opaque MFEM `ODESolver` library call; the sequential carry-dependence survives as the read-after-write on the shared `sol` — a `sequential-obstruction`.

The two layers share the per-step dataflow position (each `ode->Step` ≡ one `time_step_op op s t`) and the operator-capture-once placement (outside the loop / outside the fold); they differ in **the combinator vocabulary (`foldl` vs explicit `for`), the carry representation (immutable functional `TimeState` vs in-place-mutated persistent `sol`), the schedule representation (abstract `[Time]` vs concrete `delta_t`/`n_step` march), the operator-capture enforcement (`readonly` stratum vs hand-placed construction), and the per-step body (opaque quantified-over `time_step_op` vs the concrete `ode->Step` library call)**. The rotation erases the `foldl` combinator into the explicit in-place-threading loop, demotes the type-level capture-once to a hand-hoisted coding convention, materialises the immutable carry into the destructively-advanced `sol`, and resolves the opaque per-step operator to the MFEM library boundary — narrated forward L4→L3. The time-sweep carries a **`sequential-obstruction`** (unlike the map sibling's embarrassingly-parallel family loop): the carry-threading reads the prior step's in-place write, so the sweep cannot be reordered or parallelized — the load-bearing structural contrast with [`solve-family-map-dissolution`](./solve-family-map-dissolution.md).
