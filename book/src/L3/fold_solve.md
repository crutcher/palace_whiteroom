---
layer: L3
operator: fold_solve
firmness: partial-obstruction
lifts_from:
  - book/src/L4/fold_solve.md (the L4 state-threaded fold combinator; the L4>L3 dissolution erases the foldl/readonly-stratum/immutable-carry into this L3 explicit in-place-threading sweep — book/src/L4-L3/fold-solve-time-step-dissolution.md, firm; the per-step body is identity-in-form (one opaque whole-state advance at both layers), the loop is the substantive rotation)
lowers_to:
  - book/src/L2/index.md (no standalone L2/fold_solve entry — the per-step body is an opaque ode->Step leaf that does NOT decompose into L2 primitives, so the L3>L2 hop is the substantive outer-sweep erasure to an L2 fold-by-role, NOT a body-composition rotation; the L3>L2 theme book/src/L3-L2/fold-solve-time-step-body.md narrates the erasure + the opaque per-step leaf staying opaque, structurally parallel to eigsolve-opaque-eigen-iteration)
variant_axes:
  - schedule-source (fixed-list = transient: the carry consumes a precomputed [Time] schedule, the sweep ranges over n_step | state-generated = driven-PROM SweepAdaptive: the carry GENERATES the next input + the loop bound from accumulated state — the load-bearing axis, fixed-list the default surface)
  - per-step-operator (opaque-library: the step bottoms out in a library integrator/sampler — MFEM ODESolver for transient, RomOperator greedy sampler for SweepAdaptive; absorbed into the op closure)
  - carry-shape (single field-state = transient (E, B) | field-state + growing reduced basis + error history = SweepAdaptive; absorbed into the carry, does not shape the sweep spine)
  - element-type (real = transient | complex = driven-PROM; absorbed into op / the carry)
---

# fold_solve

The L3 (iteration-rotation) view of `fold_solve` — the **state-threaded fold outer-driver** rendered as an explicit value-threaded time-sweep. The per-step **body** is one opaque whole-state advance `time_step_op op s t` (it lifts trivially — a single whole-tensor-state transition with no element loop exposed). **The outer time-sweep does NOT lift**: each step's input is the prior step's output (the carry-threading is a genuine [`sequential-obstruction`](../concepts/sequential-obstruction.md)), AND the per-step body bottoms out in an opaque library integrator step (`ode->Step`, `palace/models/timeoperator.cpp:410`) the L3 view quantifies over rather than rendering. This is the `partial-obstruction` shape — body lifts, loop does not — joining L3 [`chebyshev`](./chebyshev.md) and L3 [`eigsolve`](./eigsolve.md). It is the **fold-image** of the L4 [`fold_solve`](../L4/fold_solve.md) combinator (firm), and the iteration-rotation contrast with [`solve_family`](../L4/solve_family.md)'s embarrassingly-parallel map (which has **NO** standalone L3 entry by the NO-ENTRY warrant — its loop lifts).

## Context

L3 is the iteration-rotation layer: where the L2 algebra admits a global tensor-field form, L3 captures it; where no global form exists, the **obstruction** is a first-class output (per [`sequential-obstruction`](../concepts/sequential-obstruction.md)). `fold_solve` at L3 is a **partial-obstruction** case whose obstruction profile is a *combined* shape — distinct from each precedent:

- L3 [`chebyshev`](./chebyshev.md) (`partial-obstruction`) — body lifts, but the inner `k`-recurrence + outer `pc_it` sweep are sequential obstructions rooted in **numerical stability** (a Palace-authored recurrence). `fold_solve` shares the body-lifts-loop-doesn't *shape*, but its sweep obstruction is rooted in **carry-threading** (the in-place state advance, not a numerical recurrence) PLUS an opaque per-step leaf.
- L3 [`eigsolve`](./eigsolve.md) (`partial-obstruction`) — body lifts (the `apply_shift_invert` composition), but the eigen-iteration loop is rooted in **opaque-library-ownership** (Palace authors no loop). `fold_solve` shares the opaque-per-step-body root, but — unlike `eigsolve` — **Palace DOES author the outer sweep** (the `for (int step ...)` loop, `transientsolver.cpp:77`), so the sweep renders as an explicit value-threaded tail recursion (the `ksp_solve` / `chebyshev` rendering, NOT the `eigsolve` un-renderable case). The obstruction is the carry-threading + the opaque per-step leaf, NOT the whole loop being library-owned.

The load-bearing structural fact this entry records: **`fold_solve` at L3 has a lifting body (one opaque whole-state advance) and a non-lifting Palace-authored sweep, where the sweep is non-lifting for TWO reasons — the carry-threading cannot reorder (each step reads the prior in-place write) and the per-step body is an opaque library leaf.** This is the carry-threaded sibling of the embarrassingly-parallel [`solve_family`](../L4/solve_family.md) map: where `solve_family`'s family loop lifts (independent members → NO standalone L3 entry), `fold_solve`'s sweep does not lift (carry-threaded → this `partial-obstruction` entry).

The relationship to the adjacent layers:

- **Upward** to L4: [`fold_solve`](../L4/fold_solve.md) (firm) is the `foldl` combinator `fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule`, the non-degenerate member of the strawman §3.7 [`iterate_while`](../L4/iterate_while.md) family (the carry-threading fold; the map is the degenerate fold). The L4>L3 dissolution (the `foldl` collapsing to an explicit `for`-loop threading the field-state `sol` IN PLACE; the once-captured `readonly` `op` stratum → the hand-hoisted `TimeOperator` construction; the immutable functional carry → the in-place-mutated persistent `sol`; the abstract `schedule` → the concrete `delta_t`/`n_step` march; the opaque quantified-over `time_step_op` → the concrete `ode->Step` library call) is **substantive** and is the dedicated L4>L3 theme [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md) (firm). The per-step body is **identity-in-form** between the L4 form and this L3 form (one opaque whole-state advance at both layers); the wrapper rewrite is the substantive part — the same shape `chebyshev`/`eigsolve` lower by.
- **Downward** to L2: there is **no standalone `L2/fold_solve` entry**, and crucially **the per-step body does NOT decompose into L2 primitives** — it is the opaque `ode->Step` integrator leaf (`timeoperator.cpp:410`). So the L3>L2 hop is NOT a body-composition rotation (the `eigsolve` body-identity-on-`apply_shift_invert` shape does not apply — there is no L2 composition the body maps to). Instead the L3>L2 hop is the **substantive outer-sweep erasure**: the L3 explicit in-place-threading `for`-loop (carrying the carry-threading `sequential-obstruction` marker) lowers to an L2 fold-by-role composition (iteration view erased; the obstruction shadowed to non-laws), with the opaque per-step leaf staying opaque across the edge. This is the dedicated L3>L2 theme [`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md), structurally parallel to [`eigsolve-opaque-eigen-iteration`](../L3-L2/eigsolve-opaque-eigen-iteration.md) (the `structural` + secondary `obstruction (opaque-library-ownership)` shape), strengthened by the additional carry-threading obstruction.

**Non-adjacent identity (in-line, no directory).** No non-adjacent L3↔L1 identity is annotated: the per-step body is an opaque library leaf (not a composition of L1 primitives), so there is no body-level value-thread-isomorphism to L1 to record (the `chebyshev`/`krylov_step` transitive-identity pattern does not apply). No `book/src/L3-L1/` directory is created (and none would be warranted — per the `l3-l1-inline-identity-rotation-convention`, lowering directories are per-adjacent-edge only, and there is no non-adjacent identity here).

## Signature

    fold_solve :: (op, s0, schedule) -> s_final

Shape contract (positional values; L3 has no `readonly` annotation and no monadic effect):

- **`op`** — operator-parameters value, closure-captured by the sweep (first positional argument, never in the return position; the L3 image of the L4 `readonly` once-captured `OpParams` stratum, hoisted outside the loop). The sweep reads:
  - `op.time_op` — the per-step operator the sweep folds, constructed **once** outside the loop (`TimeOperator time_op(iodata, space_op, dJdt_coef)`, `palace/drivers/transientsolver.cpp:33`; its ODE integrator `op = std::make_unique<TimeDependentFirstOrderOperator>(...)`, `palace/models/timeoperator.cpp:312`). Threaded *unchanged* into every per-step `time_step_op` call.
- **`s0`** — the seed field-state (transient: the initial `(E, B)` field bundle set in place by `time_op.Init()`, `palace/drivers/transientsolver.cpp:89`). Read once at the sweep head.
- **`schedule`** — the fixed precomputed schedule (default surface): a uniform `delta_t` (`palace/drivers/transientsolver.cpp:35`) march of `n_step` (`:36`) steps. The `schedule-source` variant axis carries the state-generated generalization (SweepAdaptive).
- **result `s_final`** — the final field-state after the whole schedule is threaded. The per-step `(E, B)` is consumed for postprocessing each step (`time_op.GetE()` `:98` / `time_op.GetB()` `:99`), so the trajectory materializes in practice; the sweep's terminal product is `s_final`.

There is **no per-step `outputs` record** in the body signature: unlike L3 [`krylov_step`](./krylov_step.md) (whose `(K', s', outputs)` carries a demand-prunable readout), the per-step `time_step_op` produces the next field-state directly; the per-step `(E, B)` readout is an external postprocessing consumer of the *current* `sol`, not a sweep-internal readout.

L4 wrapper machinery absent at L3 (structural for the layer; same dissolution shape as `chebyshev` / `eigsolve`):

1. **No `Solve` monad / no `foldl` combinator.** The L4 `fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule` dissolves into the explicit value-threaded `(op, s0, schedule) -> s_final` form rendered as a tail recursion over the step counter (the `ksp_solve` / `chebyshev` rendering — Palace authors the outer loop, so it renders, unlike `eigsolve`).
2. **No `readonly` capability typing.** The L4 once-captured `readonly` `op : OpParams` stratum (the operator built once, threaded unchanged) demotes at L3 to a documented invariant verified by reading the sweep (the `TimeOperator` / integrator construction sits outside the `for` loop; nothing type-enforces it).
3. **No immutable functional carry.** The L4 immutable carry (each `\s t -> ...` returns a fresh `TimeState`) demotes at L3 to the **in-place-mutated persistent `sol` vector** (`ode->Step(sol, t, dt)` advances `sol` destructively; the next step reads the mutated `sol`). The functional carry-threading becomes the imperative read-after-write on the shared `sol`.

## Semantics

`fold_solve` at L3 is the complete state-threaded march expressed as an explicit value-threaded sweep of the opaque per-step operator `time_step_op` over the schedule, seeded by `s0`, with a single shared operator capture hoisted outside the loop, with the iteration view rendered as a **lifting per-step body folded by a non-lifting Palace-authored sweep**.

### The per-step body (lifts)

Fix the per-step body that runs once for each schedule element. With the captured operator `op.time_op` and the carried field-state `s : TimeState`, the body is one opaque whole-state advance:

$$ s_{k+1} = \texttt{time\_step\_op}(op, s_k, t_k) $$

This is a single whole-tensor-state transition (the persistent `sol` field bundle advances by one integrator step) — **whole-state by signature shape**, no element loop exposed at L3's vocabulary. It **lifts trivially** in the sense that the body is one atomic state advance, not a composition with internal per-element dependence. But — unlike `eigsolve`'s body, which lifts to a *visible L2 composition* (`apply_linop ▷ ksp_solve`) — `fold_solve`'s per-step body is an **opaque library leaf** the L3 view quantifies over (the MFEM `ODESolver` step, `palace/models/timeoperator.cpp:410`); it does not decompose into L3-native field primitives. The body "lifts" only in that it is one whole-state advance with no L3-visible internal loop; its interior is library-owned.

### The outer sweep (does not lift)

The outer time-sweep — `s_{k+1} = time_step_op(op, s_k, t_k)` threaded over the schedule — does **not** lift to a global tensor-field operation, for two reasons:

- **Carry-threading.** Each step's input `s_k` is the prior step's output. At L3 this is the read-after-write on the persistent `sol` vector: `ode->Step(sol, t, dt)` (`palace/models/timeoperator.cpp:410`) mutates `sol` in place, and the next step reads the mutated `sol`. The schedule does **not** commute (reordering the steps changes the trajectory); a closed-form global statement `s_final = (whole-march op)(s0)` exists symbolically but evaluating it re-derives the sequential march. Recorded as a [`sequential-obstruction`](../concepts/sequential-obstruction.md) rooted in **carry-threading** (the load-bearing non-law of the L4 cap).
- **Opaque per-step body.** Each step is an opaque MFEM `ODESolver` integrator step (`obstruction (opaque-library-ownership)`); the sweep folds opaque steps, it does not fuse them into one closed-form whole-schedule operator.

Unlike L3 [`eigsolve`](./eigsolve.md) (where Palace authors NO loop — the eigen-iteration is entirely inside SLEPc/ARPACK, so the L3 form cannot even render the loop), **Palace authors the `fold_solve` outer sweep** (`for (int step = 0; step < n_step; step++)`, `palace/drivers/transientsolver.cpp:77`). So the sweep renders as an explicit value-threaded tail recursion (the `ksp_solve` / `chebyshev` rendering) — the carry-threading obstruction is recorded on a Palace-authored, L3-renderable loop, with the opaque per-step leaf inside it.

### Value-threaded form (L3 rendering)

    fold_solve op s0 schedule =
      let time_op = build_time_operator op    -- TimeOperator built ONCE, outside the sweep (op-capture hoist)
          _       = construct_integrator op    -- ODE integrator constructed ONCE (op captured once)
          n_step  = num_steps schedule         -- concrete fixed schedule length (transient)
      in step_loop 0 (init_field s0)           -- tail recursion over the step counter; sol threaded IN PLACE
      where
        step_loop step sol =                   -- tail recursion over step = 0 .. n_step - 1
          if step >= n_step then sol
          else let sol' = if step == 0
                            then time_op.Init()           -- seed: set sol IN PLACE (initial conditions)
                            else time_op.Step(t, delta_t) -- ode->Step(sol, t, dt): opaque library step, advances sol IN PLACE
                   _    = consume (time_op.GetE()) (time_op.GetB())  -- per-step (E, B) postprocess of current sol
               in step_loop (step + 1) sol'    -- the prior step's IN-PLACE write to sol IS the next step's input

The `if step >= n_step` tail recursion is the L3 rendering of the L4 [`fold_solve`](../L4/fold_solve.md)'s `foldl` over the schedule (the non-degenerate §3.7 [`iterate_while`](../L4/iterate_while.md) member) — the iteration view that L3 makes load-bearing. The body inside `step_loop` is the opaque per-step advance `time_op.Step` → `ode->Step(sol, t, dt)`; the carry `sol` is threaded by the explicit tail recursion, and the read-after-write on `sol` is the L3 realization of the cap's carry-threading non-law.

The sweep is **stateless across calls** — `op` is closure-captured but never rebuilt per step; `s0` is read once; `s_final` flows out. The carry `sol` is threaded positionally through the tail recursion (in Palace, destructively in place; the L3 value-thread vocabulary records the data-dependence as the read-after-write).

### Iteration-rotation marker

L3 is the iteration-rotation layer. `fold_solve`'s iteration view is the relationship between successive field-states `s_k -> s_{k+1} = time_step_op(op, s_k, t_k)`.

- **The body lifts.** Each per-step `time_step_op` is one whole-state advance (whole-state by signature shape, no L3-visible element loop). It is identity-in-form between the L4 form and this L3 form (one opaque advance at both layers). But its interior is an opaque library leaf — it does not decompose into L3-native field primitives (the contrast with `eigsolve`'s body, which lifts to a visible `apply_linop ▷ ksp_solve` composition).
- **The outer sweep does not lift** — the carry-threading is a `sequential-obstruction` (each step reads the prior step's in-place write to `sol`; the schedule does not commute), AND the per-step body is an opaque-library leaf. Palace authors the sweep (`transientsolver.cpp:77`), so it renders as an explicit tail recursion (unlike `eigsolve`); the obstruction is the carry-threading + the opaque leaf, not the whole loop being library-owned.

This is a **combined partial-obstruction** shape — carry-threading-sequential-obstruction + opaque-per-step-leaf — distinct from `chebyshev` (numerical-stability recurrence, body lifts to L2 composition) and `eigsolve` (opaque-library whole-loop, body lifts to L2 composition). It is the carry-threaded sibling of the embarrassingly-parallel [`solve_family`](../L4/solve_family.md) (whose loop lifts, NO standalone L3 entry).

## Algebraic laws

The laws below hold; absences are deliberate. They are the L4 cap's fold laws restated in L3 vocabulary (the per-step body is identity-in-form), with the obstruction structure made explicit at L3. Every law is a **syntactic identity on the read sweep** (read off the positive transient driver loop), NOT a test-gated convergence claim — the firm-on-positive-structure basis the cap carries.

1. **Sweep-threading associativity / schedule-split** (the load-bearing law, restated from cap Law 1). `fold_solve op s0 (a ++ b) = fold_solve op (fold_solve op s0 a) b`. The sweep of a concatenated schedule is the sweep of the second segment seeded by the sweep of the first — the `foldl (a ++ b) = foldl b . foldl a` checkpoint-resume law. A march can be checkpointed and resumed (split the schedule, sweep the prefix, sweep the suffix from the prefix's final state). It is the fold analog of [`solve_family`](../L4/solve_family.md)'s concatenation-homomorphism — but `fold_solve` *threads* through `++` (sequential) whereas `solve_family` *distributes* over it (independent).

2. **Operator-capture-once / construction-hoist** (restated from cap Law 2). The `op`-dependent integrator construction is invariant across the sweep and hoists outside the loop (computed once, before the schedule is threaded). The L3 realization of `TimeOperator` / the ODE integrator built once outside the time loop (`transientsolver.cpp:33` / `timeoperator.cpp:312`, outside `:77`).

3. **Seed identity on the empty schedule** (restated from cap Law 3). `fold_solve op s0 [] = s0`. The empty schedule threads the seed unchanged — a calculus-level total-definition convenience; Palace's transient march always has `n_step > 0` (`transientsolver.cpp:36`).

Laws that explicitly **do not** hold:

- **Sweep lift to a single tensor-field op.** The per-step `time_step_op` invocations do not fuse into one closed-form whole-schedule operator — each is an opaque library integrator step with its own internal state advance. **Carry-threading + opaque per-step `sequential-obstruction`** — see Iteration-rotation marker. (The load-bearing non-law driving the `partial-obstruction` status.)
- **Commutativity / element-independence / distribution over `++`** (the map/fold distinction). Reordering the schedule changes the trajectory (each step's input is the prior step's output). This is precisely what distinguishes `fold_solve` from [`solve_family`](../L4/solve_family.md) (whose map IS distribution + commutativity → its loop lifts → no L3 entry). A fold is not embarrassingly parallel.
- **Per-step body decomposition into L3-native field primitives.** Unlike `eigsolve`'s body (`apply_linop ▷ ksp_solve`, which decomposes), `fold_solve`'s per-step `ode->Step` is an opaque-library leaf — the L3 view quantifies over it, it does not lower to a composition.
- **Linearity of the final state in the seed or schedule.** `time_step_op` is in general a nonlinear/implicit integrator step (the transient solver is `IMPLICIT`, `timeoperator.cpp:310`-region); the final state is not linear in `s0` nor in the schedule.
- **Bit-determinism across integrator / schedule-source variants.** A different MFEM integrator (GeneralizedAlpha / SDIRK23 / ARKStep) or a state-generated vs fixed schedule gives a bit-different trajectory. Load-bearing per CLAUDE.md §"Optimization tricks".

## Dependencies

**Same-layer (L3)**: none directly. `fold_solve`'s per-step body is an opaque library leaf (the MFEM `ODESolver` step) that does NOT decompose into L3-native field primitives — there is no L3 operator the body calls (the contrast with L3 [`eigsolve`](./eigsolve.md), whose body's direct constituent is the firm L3 [`ksp_solve`](./ksp_solve.md), and with L3 [`chebyshev`](./chebyshev.md), whose body references `apply_linop`/`axpy`/`axpby`). The sweep folds the opaque step; it has no L3 same-layer dependency.

**Cross-cutting concepts:**

- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the classification for the outer sweep; here rooted in **carry-threading** (the in-place state advance; each step reads the prior step's write) PLUS the opaque per-step leaf.
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — the body-lifts-but-loop-doesn't partial case.
- [`state-stratification`](../concepts/state-stratification.md) — the captured `op` operator stratum (hoisted outside the sweep) + the threaded persistent field-state carry.
- [`constructed-operators`](../concepts/constructed-operators.md) — the `TimeOperator` / ODE integrator the sweep captures is a constructed operator built once at setup.

**Adjacent-layer siblings:**

- L4: [`fold_solve`](../L4/fold_solve.md) (firm) — the `foldl` combinator this entry lifts from; the per-step body is identity-in-form, the wrapper rewrite substantive (the L4>L3 theme [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md)).
- L4: [`solve_family`](../L4/solve_family.md) (firm) — the **map** sibling whose loop lifts (NO standalone L3 entry, NO-ENTRY); the iteration-rotation contrast (independent map vs carry-threaded fold).
- L2: no standalone `L2/fold_solve` entry; the L3>L2 hop is the outer-sweep erasure to a fold-by-role ([`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md)).

## Variant axes

Four axes, one load-bearing (schedule-source) and three absorbed; none appear in the per-step body's positional signature (absorbed at construction per [`variant-absorption`](../concepts/variant-absorption.md)). Same profile as the L4 cap §Variant axes:

1. **schedule-source** (`fixed-list | state-generated`) — **THE load-bearing axis**. `fixed-list` (the default surface, transient): the sweep ranges over a precomputed uniform `delta_t`/`n_step` march (`transientsolver.cpp:35-36,77`). `state-generated` (driven-PROM SweepAdaptive, `drivensolver.cpp:231`): the carry **generates** the next input (`omega_star = FindMaxError(state)` `:389`) AND the loop bound (`memory < convergence_memory` `:384,398`) from accumulated state. Both share the carry-threaded sweep spine (prior output = next input); the fixed-list form is the default L3 surface, the state-generated form the recorded generalization (the SweepAdaptive dissolution is gated on the cap's OQ `fold-solve-greedy-schedule-source-generalization`, batch-18).
2. **per-step-operator** (`opaque-library`) — the per-step body bottoms out in a library boundary (MFEM `ODESolver` for transient `timeoperator.cpp:410`; `RomOperator` greedy sampler for SweepAdaptive `drivensolver.cpp:389`). Absorbed into `op`; the opacity is the `obstruction (opaque-library-ownership)` per-step leaf.
3. **carry-shape** (`single field-state | field-state + reduced-basis + error-history`) — transient threads a single `(E, B)`; SweepAdaptive threads a richer carry. Absorbed into the carry; does not shape the sweep spine.
4. **element-type** (`real | complex`) — transient real; driven-PROM complex. Absorbed into `op` / the carry.

## Status

`partial-obstruction` — the per-step body lifts (one opaque whole-state advance, whole-state by signature shape, no L3-visible element loop; identity-in-form between the L4 form and this L3 form); the **outer time-sweep is a witnessed [`sequential-obstruction`](../concepts/sequential-obstruction.md)** rooted in **carry-threading** (each step's input is the prior step's in-place write to `sol`, `ode->Step(sol, ...)` `palace/models/timeoperator.cpp:410`; the schedule does not commute) PLUS an **opaque-library per-step leaf** (the MFEM `ODESolver` step). The status reflects the **loop structure, not the body**. A **combined-obstruction** case — carry-threading + opaque-per-step-leaf — distinct from L3 [`chebyshev`](./chebyshev.md) (numerical-stability recurrence; body lifts to an L2 composition) and L3 [`eigsolve`](./eigsolve.md) (opaque-library *whole-loop*; body lifts to an L2 composition). **Palace authors the `fold_solve` outer sweep** (`for (int step ...)` `palace/drivers/transientsolver.cpp:77`), so the sweep RENDERS as an explicit value-threaded tail recursion (the `ksp_solve`/`chebyshev` rendering, NOT the `eigsolve` un-renderable case). The sweep-structure laws (schedule-split, operator-capture-once, seed identity) are syntactic identities on the positive transient driver loop (`transientsolver.cpp:33-99` + `timeoperator.cpp:312,410`); no dedicated unit test exercises the integration-level driver, but the read-off laws do not gate, so this is not `rough-in (test-coverage-bounded)`.

## L3 vs L2 distinction

- **L3**: value-threaded explicit time-sweep — a tail recursion over the step counter threading the persistent `sol` field-state in place, the operator construction hoisted outside the loop, the per-step body the opaque `ode->Step` integrator leaf. The iteration view is load-bearing — the carry-threading `sequential-obstruction` + the opaque per-step leaf are both made explicit at L3.
- **L2**: there is no standalone `L2/fold_solve` entry. The L3>L2 hop is the **substantive outer-sweep erasure** — the L3 explicit tail recursion (carrying the carry-threading obstruction marker) lowers to an L2 fold-by-role composition (iteration view erased; obstruction shadowed to non-laws), with the opaque per-step leaf staying opaque. Because the per-step body is an opaque library leaf (NOT an L2 composition), this is NOT the `eigsolve` body-identity-on-`apply_shift_invert` shape — there is no L2 body composition the per-step maps to.

The L3>L2 hop erases the explicit iteration view and is the dedicated L3>L2 theme [`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md), structurally parallel to [`eigsolve-opaque-eigen-iteration`](../L3-L2/eigsolve-opaque-eigen-iteration.md), strengthened by the carry-threading obstruction.

## L3 vs L4 distinction

- **L4**: the `foldl` combinator `fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule`. The operator-capture-once is *structural* (`op : OpParams` `readonly`, bound once outside the fold); the carry-threading is *typed* (`TimeState` threaded forward immutably, the step reads the prior carry); the per-step `time_step_op` is opaque, quantified-over; the §3.7 map/fold axis is the degenerate-vs-non-degenerate distinction.
- **L3**: value-threaded explicit time-sweep. The `foldl` has dissolved to a tail recursion over the step counter; the operator-capture-once is a coding convention (`TimeOperator` built outside the `for`), not a type-level stratification; the immutable carry has materialized into the destructively-advanced persistent `sol`; the opaque per-step operator resolves to the `ode->Step` library boundary. The per-step body's whole-state advance is value-thread-isomorphic to L4; the wrapper differs (and is the substantive L4>L3 rotation).

## Evidence

The L3 sweep is read directly from the Palace transient driver loop + the per-step operator construction/dispatch; the carry-threading + opaque-per-step obstructions are read from the in-place `sol` advance and the `ode->Step` MFEM boundary.

- **Transient fixed-schedule fold-sweep (positive; the default L3 surface)** (`palace/drivers/transientsolver.cpp` + `palace/models/timeoperator.cpp`):
  - `palace/drivers/transientsolver.cpp:33` — `TimeOperator time_op(iodata, space_op, dJdt_coef)` (operator built once, outside the loop — the operator-capture hoist).
  - `:35` — `delta_t = iodata.solver.transient.delta_t` (the uniform timestep — the concrete schedule's step).
  - `:36` — `n_step = config::GetNumSteps(0.0, iodata.solver.transient.max_t, delta_t)` (the fixed schedule length — the concrete loop bound).
  - `:77` — `for (int step = 0; step < n_step; step++)` (the sweep — Palace authors it; the L3 tail recursion renders it, the `ksp_solve`/`chebyshev` rendering, NOT the `eigsolve` un-renderable case).
  - `:89` — `time_op.Init()` (the seed `s0` set IN PLACE — the `step == 0` initial conditions).
  - `:93` — `time_op.Step(t, delta_t)` (the per-step body call — the `step != 0` branch).
  - `:98` — `time_op.GetE()` (per-step `(E, B)` readout of the persistent `sol` — the external trajectory consumer).
  - `:99` — `time_op.GetB()` (per-step readout).
  - `palace/models/timeoperator.cpp:312` — `op = std::make_unique<TimeDependentFirstOrderOperator>(...)` (the per-step ODE operator constructed once — the integrator-construction hoist).
  - `:410` — `ode->Step(sol, t, dt)` (the **opaque MFEM `ODESolver` step** advancing the persistent `sol` field-state IN PLACE; the prior step's `sol` is the next step's input — the carry-threading `sequential-obstruction`; the `obstruction (opaque-library-ownership)` per-step leaf — the negative anchor is Palace's CALL, NOT MFEM internals).
- **Driven-PROM SweepAdaptive state-generated greedy fold-sweep (positive; the second fold-spine witness, the state-generated variant — NOT the default L3 surface):** (`palace/drivers/drivensolver.cpp`):
  - `:231` — `ErrorIndicator DrivenSolver::SweepAdaptive(SpaceOperator &space_op) const` (the greedy state-threaded march entry).
  - `:384` — `for (std::size_t it0 = it; it < max_size_per_excitation && memory < convergence_memory; it++)` (the state-derived loop bound — the schedule generated from the carry).
  - `:389` — `omega_star = prom_op.FindMaxError(excitation_idx)[0]` (the state-derived per-step input — the schedule-source variant).
- **Map contrast-sibling (negative for the fold-obstruction):**
  - [`solve_family`](../L4/solve_family.md) (electrostatic + magnetostatic) is the independent-**map** sibling — its loop lifts (no carry, embarrassingly parallel), so it has NO standalone L3 entry (NO-ENTRY). Cited for the carry-threaded-fold vs embarrassingly-parallel-map iteration-rotation distinction.
- **Adjacent firm entries:**
  - `book/src/L4/fold_solve.md` (firm) — the L4 cap this entry lifts from; §Signature (the `foldl` shape), §"Algebraic laws" (the fold laws this entry restates), §"Lowers to" (the in-line rotation-direction record this entry realizes), §Status (the firm-on-positive-structure basis).
  - `book/src/L4-L3/fold-solve-time-step-dissolution.md` (firm) — the L4>L3 dissolution; the per-step body is identity-in-form, the wrapper rewrite substantive.
  - `book/src/L3/chebyshev.md` (partial-obstruction) — the precedent partial-obstruction L3 entry (body lifts, loop does not; numerical-stability root). Structural template for this entry's §Iteration-rotation marker + §Status.
  - `book/src/L3/eigsolve.md` (partial-obstruction) — the precedent opaque-library partial-obstruction; the contrast (eigsolve's whole loop is library-owned and un-renderable; fold_solve's outer sweep is Palace-authored and renders, only the per-step body + carry-threading are the obstruction).
  - `book/src/L3-L2/eigsolve-opaque-eigen-iteration.md` (firm) — the structurally-parallel L3>L2 theme this entry's L3>L2 hop follows (`structural` + secondary `obstruction (opaque-library-ownership)`).
- **No dedicated test** exercises the transient march or the SweepAdaptive greedy loop (integration-level drivers, no `reference/palace/test/unit/` coverage); the L0 evidence is the driver source above. This does NOT gate the sweep-structure laws (read-off syntactic identities — the firm-on-positive-structure escape).
