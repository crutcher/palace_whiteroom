---
agent: abstractor
invoked_at: 2026-06-02T061737Z
scope: L3>L2 theme sketch + L3 entry — fold_solve L3-image (partial-obstruction) + fold-solve-time-step-body
status: pending
inputs:
  - book/src/L4/fold_solve.md (firm c058 D1; the L4 cap whose L3-image this dispatch warrants)
  - book/src/L4-L3/fold-solve-time-step-dissolution.md (firm c058 D2; the forward framing to re-anchor)
  - book/src/L3/chebyshev.md (partial-obstruction precedent — nested sequential folds)
  - book/src/L3/eigsolve.md (partial-obstruction precedent — opaque-library loop)
  - book/src/L4/solve_family.md (cycle-057 D1 NO-ENTRY warrant — the embarrassingly-parallel contrast)
  - book/src/L3-L2/eigsolve-opaque-eigen-iteration.md (the structurally-parallel L3>L2 opaque-library theme)
  - palace/drivers/transientsolver.cpp:33-99 (transient fixed-schedule fold-sweep)
  - palace/models/timeoperator.cpp:312,410 (op-construct-once + opaque ode->Step per-step body)
  - palace/drivers/drivensolver.cpp:231-398 (SweepAdaptive state-generated fold-spine second witness)
integrated_at: 2026-06-02T061737Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-059 D1. Applied clean (12 proposed-changes blocks, 0 defers/rejects). NEW book/src/L3/fold_solve.md (partial-obstruction — the 4th L3 partial-obstruction, the L3 fold-image of the firm L4 fold_solve; carry-threading sequential-obstruction + opaque per-step ode->Step body both resist the rotation while the body lifts) + NEW book/src/L3-L2/fold-solve-time-step-body.md (firm — the 5th substantive L3>L2 theme; consolidated firm-theme count 5->6). L3/index single authoritative count tally 17 firm + 3 -> 17 firm + 4 partial-obstruction + obstruction-profile shape (f) added; L3-L2/index tally 5->6; SUMMARY.md x2; 3 coupled re-anchors resolved to live links. Resolves OQ fold-solve-l3-entry-vs-dissolution-home (verdict L3-ENTRY). citecheck --scan 29 ok / 0 failing. Build cargo make book exit 0; no build-repair needed."

# CYCLE: L3>L2 theme sketch + L3 entry — fold_solve L3-image (partial-obstruction)

## Summary

**Warrant verdict: L3-ENTRY (YES), `partial-obstruction`.** `fold_solve`'s L3 image is a genuine concise iteration-rotation form, NOT a degenerate mirror of the L4 cap or the c058 D2 L4>L3 dissolution theme. The decisive distinction from the `solve_family` cycle-057 D1 NO-ENTRY verdict is the obstruction profile of the resulting L3 loop: `solve_family`'s family loop is **embarrassingly parallel** (independent RHS members, no carry → "the loop lifts" is the L3 content, fully said by the dissolution theme's RHS), so a standalone L3 chapter would mirror it. `fold_solve`'s time-sweep loop carries **TWO genuine obstructions** the dissolution theme's L4→L3 narration cannot be the authoritative home for: (1) a carry-threading `sequential-obstruction` (step n's in-place write to `sol` IS step n+1's input — the schedule cannot reorder), and (2) an opaque-library per-step body (`ode->Step`, `palace/models/timeoperator.cpp:410`). This is exactly the `chebyshev` (c013) / `eigsolve` (c024) shape — body/loop split where the loop does not lift — so the L3 entry records the `partial-obstruction` in L3 iteration-rotation vocabulary, the layer-coherent home for the obstruction structure. The L3 entry sits in the obstruction-carrying region of the L3 obstruction-profile spectrum (a NEW combined shape: carry-threading-sequential-obstruction + opaque-per-step-leaf — distinct from `eigsolve`'s opaque-only loop and `chebyshev`'s numerical-stability recurrence).

I author two artifacts:
- **`book/src/L3/fold_solve.md`** — status `partial-obstruction`. The L3 iteration-rotation view: the per-step body lifts (it is a single opaque whole-state advance) but the outer time-sweep does NOT lift (carry-threading + opaque per-step), recorded in L3 vocabulary structurally parallel to `chebyshev`/`eigsolve`.
- **`book/src/L3-L2/fold-solve-time-step-body.md`** — canonical slug — the L3>L2 hop. **Honest re-framing (load-bearing, recorded in §Open questions):** unlike `eigsolve` (whose per-step body `apply_linop ▷ ksp_solve` IS an L2 composition that lowers), `fold_solve`'s per-step body is the **opaque `ode->Step` leaf** that does NOT decompose into L2 primitives. So the substantive L3>L2 content is the **outer-sweep erasure** (the L3 explicit in-place-threading `for`-loop + carry-threading obstruction marker → an L2 fold-by-role with the obstruction shadowed to non-laws + the opaque per-step leaf staying opaque) — structurally parallel to `eigsolve-opaque-eigen-iteration` (`structural` + secondary `obstruction (opaque-library-ownership)`), strengthened by the additional carry-threading obstruction.

Coupled re-anchor: the firm `L4/fold_solve.md` §"Lowers to" + the c058 D2 `L4-L3/fold-solve-time-step-dissolution.md` §"What this lowering does NOT cover" / §Verified-against, which currently say the standalone-L3-entry question is "a batch-18 judgment / deferred (OQ `fold-solve-l3-entry-vs-dissolution-home`)", are re-anchored to the live L3 entry this dispatch lands. OQ `fold-solve-l3-entry-vs-dissolution-home` is resolved (verdict: L3-ENTRY).

## Warrant reasoning (the anti-mirror call)

The 2026-06-01 vocabulary-shift redirect anti-mirror principle: an L3 chapter must SHIFT vocabulary, not mirror the dissolution theme's RHS. The test the planner set: is `fold_solve`'s L3 image a genuine iteration-rotation form, or a degenerate mirror?

**`solve_family` (NO-ENTRY, c057 D1) — why it failed the test:** its family loop is embarrassingly parallel; the L3 iteration-rotation content is the *negative* finding "the loop lifts" (the members are independent, no `sequential-obstruction`). That finding is already stated, in L3 vocabulary, in the dissolution theme's §"L3 form (RHS)" + §"What does NOT change". A separate L3 chapter would reproduce the dissolution RHS without shifting vocabulary → mirror → NO-ENTRY.

**`fold_solve` (L3-ENTRY, this dispatch) — why it passes:** the time-sweep loop is NOT obstruction-free. It carries:
1. **Carry-threading `sequential-obstruction`** — `time_step_op op s_k t` reads `s_k` (the prior step's output); at L3 this is the read-after-write on the persistent `sol` vector (`ode->Step(sol, ...)` mutates `sol`; the next step reads it). The schedule does not commute. This is a genuine sequential obstruction (the cap's load-bearing non-law).
2. **Opaque-library per-step leaf** — the per-step body bottoms out in `ode->Step` (`timeoperator.cpp:410`), an MFEM `ODESolver` step Palace never exposes standalone (`obstruction (opaque-library-ownership)`).

The L3 iteration-rotation layer's job (per `L3/index.md:7,15`) is to record where the global form is unavailable as a first-class obstruction. `fold_solve` is body-lifts-loop-doesn't — the `partial-obstruction` shape (`chebyshev`/`eigsolve`). The L3 entry expresses this in iteration-rotation vocabulary (the explicit value-threaded sweep, the carry-threading obstruction marker, the opaque per-step leaf), which is a genuine vocabulary the dissolution theme's L4→L3 narration is not the authoritative home for: the dissolution theme's job is to record the L4→L3 rewrite *direction* (forward), not to be the standing L3-vocabulary definition of the obstruction structure. The L3 entry IS that definition, structurally parallel to `chebyshev`/`eigsolve`.

This is exactly the prediction the c058 D1 cap §"Lowers to" already recorded: "unlike `solve_family`'s family loop (which lifts cleanly — no obstruction), `fold_solve`'s loop carries BOTH a carry-threading sequential-obstruction AND an opaque-library per-step body, so an L3 entry recording the `partial-obstruction` (the `chebyshev` / `eigsolve` shape) is the likelier outcome." This dispatch enacts that likely outcome.

## Proposed changes

```new:book/src/L3/fold_solve.md
---
layer: L3
operator: fold_solve
firmness: partial-obstruction
lifts_from:
  - book/src/L4/fold_solve.md (the L4 state-threaded fold combinator; the L4>L3 dissolution erases the foldl/readonly-stratum/immutable-carry into this L3 explicit in-place-threading sweep — book/src/L4-L3/fold-solve-time-step-dissolution.md, firm cycle-058 D2; the per-step body is identity-in-form (one opaque whole-state advance at both layers), the loop is the substantive rotation)
lowers_to:
  - book/src/L2/index.md (no standalone L2/fold_solve entry — the per-step body is an opaque ode->Step leaf that does NOT decompose into L2 primitives, so the L3>L2 hop is the substantive outer-sweep erasure to an L2 fold-by-role, NOT a body-composition rotation; the L3>L2 theme book/src/L3-L2/fold-solve-time-step-body.md, cycle-059, narrates the erasure + the opaque per-step leaf staying opaque, structurally parallel to eigsolve-opaque-eigen-iteration)
variant_axes:
  - schedule-source (fixed-list = transient: the carry consumes a precomputed [Time] schedule, the sweep ranges over n_step | state-generated = driven-PROM SweepAdaptive: the carry GENERATES the next input + the loop bound from accumulated state — the load-bearing axis, fixed-list the default surface)
  - per-step-operator (opaque-library: the step bottoms out in a library integrator/sampler — MFEM ODESolver for transient, RomOperator greedy sampler for SweepAdaptive; absorbed into the op closure)
  - carry-shape (single field-state = transient (E, B) | field-state + growing reduced basis + error history = SweepAdaptive; absorbed into the carry, does not shape the sweep spine)
  - element-type (real = transient | complex = driven-PROM; absorbed into op / the carry)
---

# fold_solve

The L3 (iteration-rotation) view of `fold_solve` — the **state-threaded fold outer-driver** rendered as an explicit value-threaded time-sweep. The per-step **body** is one opaque whole-state advance `time_step_op op s t` (it lifts trivially — a single whole-tensor-state transition with no element loop exposed). **The outer time-sweep does NOT lift**: each step's input is the prior step's output (the carry-threading is a genuine [`sequential-obstruction`](../concepts/sequential-obstruction.md)), AND the per-step body bottoms out in an opaque library integrator step (`ode->Step`, `palace/models/timeoperator.cpp:410`) the L3 view quantifies over rather than rendering. This is the `partial-obstruction` shape — body lifts, loop does not — joining L3 [`chebyshev`](./chebyshev.md) (c013) and L3 [`eigsolve`](./eigsolve.md) (c024). It is the **fold-image** of the L4 [`fold_solve`](../L4/fold_solve.md) combinator (firm c058 D1), and the iteration-rotation contrast with [`solve_family`](../L4/solve_family.md)'s embarrassingly-parallel map (which has **NO** standalone L3 entry by the c057 D1 NO-ENTRY warrant — its loop lifts).

## Context

L3 is the iteration-rotation layer: where the L2 algebra admits a global tensor-field form, L3 captures it; where no global form exists, the **obstruction** is a first-class output (per [`sequential-obstruction`](../concepts/sequential-obstruction.md)). `fold_solve` at L3 is a **partial-obstruction** case whose obstruction profile is a *combined* shape — distinct from each precedent:

- L3 [`chebyshev`](./chebyshev.md) (`partial-obstruction`) — body lifts, but the inner `k`-recurrence + outer `pc_it` sweep are sequential obstructions rooted in **numerical stability** (a Palace-authored recurrence). `fold_solve` shares the body-lifts-loop-doesn't *shape*, but its sweep obstruction is rooted in **carry-threading** (the in-place state advance, not a numerical recurrence) PLUS an opaque per-step leaf.
- L3 [`eigsolve`](./eigsolve.md) (`partial-obstruction`) — body lifts (the `apply_shift_invert` composition), but the eigen-iteration loop is rooted in **opaque-library-ownership** (Palace authors no loop). `fold_solve` shares the opaque-per-step-body root, but — unlike `eigsolve` — **Palace DOES author the outer sweep** (the `for (int step ...)` loop, `transientsolver.cpp:77`), so the sweep renders as an explicit value-threaded tail recursion (the `ksp_solve` / `chebyshev` rendering, NOT the `eigsolve` un-renderable case). The obstruction is the carry-threading + the opaque per-step leaf, NOT the whole loop being library-owned.

The load-bearing structural fact this entry records: **`fold_solve` at L3 has a lifting body (one opaque whole-state advance) and a non-lifting Palace-authored sweep, where the sweep is non-lifting for TWO reasons — the carry-threading cannot reorder (each step reads the prior in-place write) and the per-step body is an opaque library leaf.** This is the carry-threaded sibling of the embarrassingly-parallel [`solve_family`](../L4/solve_family.md) map: where `solve_family`'s family loop lifts (independent members → NO standalone L3 entry, c057 D1), `fold_solve`'s sweep does not lift (carry-threaded → this `partial-obstruction` entry).

The relationship to the adjacent layers:

- **Upward** to L4: [`fold_solve`](../L4/fold_solve.md) (firm c058 D1) is the `foldl` combinator `fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule`, the non-degenerate member of the strawman §3.7 [`iterate-while`](../L4/iterate-while.md) family (the carry-threading fold; the map is the degenerate fold). The L4>L3 dissolution (the `foldl` collapsing to an explicit `for`-loop threading the field-state `sol` IN PLACE; the once-captured `readonly` `op` stratum → the hand-hoisted `TimeOperator` construction; the immutable functional carry → the in-place-mutated persistent `sol`; the abstract `schedule` → the concrete `delta_t`/`n_step` march; the opaque quantified-over `time_step_op` → the concrete `ode->Step` library call) is **substantive** and is the dedicated L4>L3 theme [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md) (firm c058 D2). The per-step body is **identity-in-form** between the L4 form and this L3 form (one opaque whole-state advance at both layers); the wrapper rewrite is the substantive part — the same shape `chebyshev`/`eigsolve` lower by.
- **Downward** to L2: there is **no standalone `L2/fold_solve` entry**, and crucially **the per-step body does NOT decompose into L2 primitives** — it is the opaque `ode->Step` integrator leaf (`timeoperator.cpp:410`). So the L3>L2 hop is NOT a body-composition rotation (the `eigsolve` body-identity-on-`apply_shift_invert` shape does not apply — there is no L2 composition the body maps to). Instead the L3>L2 hop is the **substantive outer-sweep erasure**: the L3 explicit in-place-threading `for`-loop (carrying the carry-threading `sequential-obstruction` marker) lowers to an L2 fold-by-role composition (iteration view erased; the obstruction shadowed to non-laws), with the opaque per-step leaf staying opaque across the edge. This is the dedicated L3>L2 theme [`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md) (cycle-059), structurally parallel to [`eigsolve-opaque-eigen-iteration`](../L3-L2/eigsolve-opaque-eigen-iteration.md) (the `structural` + secondary `obstruction (opaque-library-ownership)` shape), strengthened by the additional carry-threading obstruction.

**Non-adjacent identity (in-line, no directory).** No non-adjacent L3↔L1 identity is annotated: the per-step body is an opaque library leaf (not a composition of L1 primitives), so there is no body-level value-thread-isomorphism to L1 to record (the `chebyshev`/`krylov-step` transitive-identity pattern does not apply). No `book/src/L3-L1/` directory is created (and none would be warranted — per the cycle-012 `l3-l1-inline-identity-rotation-convention`, lowering directories are per-adjacent-edge only, and there is no non-adjacent identity here).

## Signature

    fold_solve :: (op, s0, schedule) -> s_final

Shape contract (positional values; L3 has no `readonly` annotation and no monadic effect):

- **`op`** — operator-parameters value, closure-captured by the sweep (first positional argument, never in the return position; the L3 image of the L4 `readonly` once-captured `OpParams` stratum, hoisted outside the loop). The sweep reads:
  - `op.time_op` — the per-step operator the sweep folds, constructed **once** outside the loop (`TimeOperator time_op(iodata, space_op, dJdt_coef)`, `palace/drivers/transientsolver.cpp:33`; its ODE integrator `op = std::make_unique<TimeDependentFirstOrderOperator>(...)`, `palace/models/timeoperator.cpp:312`). Threaded *unchanged* into every per-step `time_step_op` call.
- **`s0`** — the seed field-state (transient: the initial `(E, B)` field bundle set in place by `time_op.Init()`, `palace/drivers/transientsolver.cpp:89`). Read once at the sweep head.
- **`schedule`** — the fixed precomputed schedule (default surface): a uniform `delta_t` (`palace/drivers/transientsolver.cpp:35`) march of `n_step` (`:36`) steps. The `schedule-source` variant axis carries the state-generated generalization (SweepAdaptive).
- **result `s_final`** — the final field-state after the whole schedule is threaded. The per-step `(E, B)` is consumed for postprocessing each step (`time_op.GetE()` `:98` / `time_op.GetB()` `:99`), so the trajectory materializes in practice; the sweep's terminal product is `s_final`.

There is **no per-step `outputs` record** in the body signature: unlike L3 [`krylov-step`](./krylov-step.md) (whose `(K', s', outputs)` carries a demand-prunable readout), the per-step `time_step_op` produces the next field-state directly; the per-step `(E, B)` readout is an external postprocessing consumer of the *current* `sol`, not a sweep-internal readout.

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

The `if step >= n_step` tail recursion is the L3 rendering of the L4 [`fold_solve`](../L4/fold_solve.md)'s `foldl` over the schedule (the non-degenerate §3.7 [`iterate-while`](../L4/iterate-while.md) member) — the iteration view that L3 makes load-bearing. The body inside `step_loop` is the opaque per-step advance `time_op.Step` → `ode->Step(sol, t, dt)`; the carry `sol` is threaded by the explicit tail recursion, and the read-after-write on `sol` is the L3 realization of the cap's carry-threading non-law.

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

- L4: [`fold_solve`](../L4/fold_solve.md) (firm c058 D1) — the `foldl` combinator this entry lifts from; the per-step body is identity-in-form, the wrapper rewrite substantive (the L4>L3 theme [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md)).
- L4: [`solve_family`](../L4/solve_family.md) (firm c055 D1) — the **map** sibling whose loop lifts (NO standalone L3 entry, c057 D1 NO-ENTRY); the iteration-rotation contrast (independent map vs carry-threaded fold).
- L2: no standalone `L2/fold_solve` entry; the L3>L2 hop is the outer-sweep erasure to a fold-by-role ([`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md)).

## Variant axes

Four axes, one load-bearing (schedule-source) and three absorbed; none appear in the per-step body's positional signature (absorbed at construction per [`variant-absorption`](../concepts/variant-absorption.md)). Same profile as the L4 cap §Variant axes:

1. **schedule-source** (`fixed-list | state-generated`) — **THE load-bearing axis**. `fixed-list` (the default surface, transient): the sweep ranges over a precomputed uniform `delta_t`/`n_step` march (`transientsolver.cpp:35-36,77`). `state-generated` (driven-PROM SweepAdaptive, `drivensolver.cpp:231`): the carry **generates** the next input (`omega_star = FindMaxError(state)` `:389`) AND the loop bound (`memory < convergence_memory` `:384,398`) from accumulated state. Both share the carry-threaded sweep spine (prior output = next input); the fixed-list form is the default L3 surface, the state-generated form the recorded generalization (the SweepAdaptive dissolution is gated on the cap's OQ `fold-solve-greedy-schedule-source-generalization`, batch-18).
2. **per-step-operator** (`opaque-library`) — the per-step body bottoms out in a library boundary (MFEM `ODESolver` for transient `timeoperator.cpp:410`; `RomOperator` greedy sampler for SweepAdaptive `drivensolver.cpp:389`). Absorbed into `op`; the opacity is the `obstruction (opaque-library-ownership)` per-step leaf.
3. **carry-shape** (`single field-state | field-state + reduced-basis + error-history`) — transient threads a single `(E, B)`; SweepAdaptive threads a richer carry. Absorbed into the carry; does not shape the sweep spine.
4. **element-type** (`real | complex`) — transient real; driven-PROM complex. Absorbed into `op` / the carry.

## Status

`partial-obstruction` — the per-step body lifts (one opaque whole-state advance, whole-state by signature shape, no L3-visible element loop; identity-in-form between the L4 form and this L3 form per the firm L4>L3 dissolution); the **outer time-sweep is a witnessed [`sequential-obstruction`](../concepts/sequential-obstruction.md)** rooted in **carry-threading** (each step's input is the prior step's in-place write to `sol`, `ode->Step(sol, ...)` `palace/models/timeoperator.cpp:410`; the schedule does not commute — the cap's load-bearing non-law) PLUS an **opaque-library per-step leaf** (the MFEM `ODESolver` step). The status reflects the **loop structure, not the body** (the L3 `partial-obstruction` definition per CLAUDE.md §Methodology invariants "Two rough-in qualifiers are first-class"). It is a **combined-obstruction** case — carry-threading-sequential-obstruction + opaque-per-step-leaf — distinct from the precedents: L3 [`chebyshev`](./chebyshev.md) (numerical-stability recurrence; body lifts to an L2 composition) and L3 [`eigsolve`](./eigsolve.md) (opaque-library *whole-loop*; body lifts to an L2 composition). Crucially, **Palace authors the `fold_solve` outer sweep** (`for (int step ...)` `palace/drivers/transientsolver.cpp:77`), so the sweep RENDERS as an explicit value-threaded tail recursion (the `ksp_solve`/`chebyshev` rendering, NOT the `eigsolve` un-renderable case); the obstruction is the carry-threading + the opaque per-step leaf inside a Palace-authored, L3-renderable loop.

**Caveat (not a status reduction):** the sweep-structure laws (schedule-split, operator-capture-once, seed identity) are **syntactic identities on the positive transient driver loop** (`transientsolver.cpp:33-99` + `timeoperator.cpp:312,410`), the firm-on-positive-structure basis the L4 cap carries; the `partial-obstruction` status is the honest L3 verdict for the loop, not a confidence reduction on the sweep structure. No dedicated unit test exercises the transient march or the SweepAdaptive greedy loop (the drivers are integration-level); the L0 evidence is the driver source. This does NOT gate the sweep-structure laws (read-off syntactic identities) — so this is **not** `rough-in (test-coverage-bounded)`.

This entry **resolves OQ `fold-solve-l3-entry-vs-dissolution-home`** (verdict: L3-ENTRY) — the c058 D1 cap's likely-outcome prediction enacted. It is the iteration-rotation operator definition for the state-threaded fold; the dissolution theme [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md) records the L4→L3 rewrite *direction* (forward), this entry is the standing L3-vocabulary definition of the obstruction structure (the `chebyshev`/`eigsolve` division of labor). Distinct from [`solve_family`](../L4/solve_family.md)'s NO-ENTRY (c057 D1): that loop lifts (embarrassingly parallel), so its L3 content is the negative finding stated in its dissolution theme's RHS; `fold_solve`'s loop does not lift, so the obstruction structure earns a standing L3 chapter.

## L3 vs L2 distinction

- **L3**: value-threaded explicit time-sweep — a tail recursion over the step counter threading the persistent `sol` field-state in place, the operator construction hoisted outside the loop, the per-step body the opaque `ode->Step` integrator leaf. The iteration view is load-bearing — the carry-threading `sequential-obstruction` + the opaque per-step leaf are both made explicit at L3.
- **L2**: there is no standalone `L2/fold_solve` entry. The L3>L2 hop is the **substantive outer-sweep erasure** — the L3 explicit tail recursion (carrying the carry-threading obstruction marker) lowers to an L2 fold-by-role composition (iteration view erased; obstruction shadowed to non-laws), with the opaque per-step leaf staying opaque. Because the per-step body is an opaque library leaf (NOT an L2 composition), this is NOT the `eigsolve` body-identity-on-`apply_shift_invert` shape — there is no L2 body composition the per-step maps to.

The L3>L2 hop erases the explicit iteration view and is the dedicated L3>L2 theme [`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md) (cycle-059), structurally parallel to [`eigsolve-opaque-eigen-iteration`](../L3-L2/eigsolve-opaque-eigen-iteration.md), strengthened by the carry-threading obstruction.

## L3 vs L4 distinction

- **L4**: the `foldl` combinator `fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule`. The operator-capture-once is *structural* (`op : OpParams` `readonly`, bound once outside the fold); the carry-threading is *typed* (`TimeState` threaded forward immutably, the step reads the prior carry); the per-step `time_step_op` is opaque, quantified-over; the §3.7 map/fold axis is the degenerate-vs-non-degenerate distinction.
- **L3**: value-threaded explicit time-sweep. The `foldl` has dissolved to a tail recursion over the step counter; the operator-capture-once is a coding convention (`TimeOperator` built outside the `for`), not a type-level stratification; the immutable carry has materialized into the destructively-advanced persistent `sol`; the opaque per-step operator resolves to the `ode->Step` library boundary. The per-step body's whole-state advance is value-thread-isomorphic to L4; the wrapper differs (and is the substantive L4>L3 rotation).

## Evidence

The L3 sweep is read directly from the Palace transient driver loop + the per-step operator construction/dispatch; the carry-threading + opaque-per-step obstructions are read from the in-place `sol` advance and the `ode->Step` MFEM boundary. All citations self-verified against on-disk source this dispatch via `palace-codemap` `read_range` + `tools/citecheck/citecheck.py --anchor`.

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
  - [`solve_family`](../L4/solve_family.md) (electrostatic + magnetostatic) is the independent-**map** sibling — its loop lifts (no carry, embarrassingly parallel), so it has NO standalone L3 entry (c057 D1 NO-ENTRY). Cited for the carry-threaded-fold vs embarrassingly-parallel-map iteration-rotation distinction.
- **Adjacent firm entries:**
  - `book/src/L4/fold_solve.md` (firm c058 D1) — the L4 cap this entry lifts from; §Signature (the `foldl` shape), §"Algebraic laws" (the fold laws this entry restates), §"Lowers to" (the in-line rotation-direction record this entry realizes), §Status (the firm-on-positive-structure basis).
  - `book/src/L4-L3/fold-solve-time-step-dissolution.md` (firm c058 D2) — the L4>L3 dissolution; the per-step body is identity-in-form, the wrapper rewrite substantive.
  - `book/src/L3/chebyshev.md` (partial-obstruction, c013) — the precedent partial-obstruction L3 entry (body lifts, loop does not; numerical-stability root). Structural template for this entry's §Iteration-rotation marker + §Status.
  - `book/src/L3/eigsolve.md` (partial-obstruction, c024) — the precedent opaque-library partial-obstruction; the contrast (eigsolve's whole loop is library-owned and un-renderable; fold_solve's outer sweep is Palace-authored and renders, only the per-step body + carry-threading are the obstruction).
  - `book/src/L3-L2/eigsolve-opaque-eigen-iteration.md` (firm c045) — the structurally-parallel L3>L2 theme this entry's L3>L2 hop follows (`structural` + secondary `obstruction (opaque-library-ownership)`).
- **No dedicated test** exercises the transient march or the SweepAdaptive greedy loop (integration-level drivers, no `reference/palace/test/unit/` coverage); the L0 evidence is the driver source above. This does NOT gate the sweep-structure laws (read-off syntactic identities — the firm-on-positive-structure escape).
```

```new:book/src/L3-L2/fold-solve-time-step-body.md
# fold-solve-time-step-body

The L3>L2 lowering theme for the [`fold_solve`](../L3/fold_solve.md) **state-threaded fold time-sweep** (`partial-obstruction`, cycle-059) — the L3 explicit value-threaded sweep that threads the persistent field-state `sol` in place through a schedule, advancing it one opaque per-step operator (`time_step_op` → the MFEM `ode->Step` integrator) at a time, where **each step's input is the prior step's in-place write**. The theme dissolves the L3 explicit-tail-recursion iteration view (the value-threaded sweep carrying the **carry-threading `sequential-obstruction`** marker) into the L2 **fold-by-role composition** (the iteration view erased; the obstruction shadowed to L2-vocabulary non-laws), with the **opaque per-step body staying opaque** across the edge. It is the **carry-threaded sibling** of [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md): that theme erases an opaque-library *whole-loop* marker (Palace authors no loop); this theme erases a Palace-authored *carry-threaded sweep* whose per-step body is an opaque-library leaf.

## Slug

`fold-solve-time-step-body`

## Context

The cycle-059 D1 abstractor landed [`L3/fold_solve`](../L3/fold_solve.md) — the L3 iteration-rotation view of the state-threaded fold, status `partial-obstruction` (resolving OQ `fold-solve-l3-entry-vs-dissolution-home`, verdict L3-ENTRY). The L3 entry's §"Downward to L2" / §"L3 vs L2 distinction" name the L3>L2 hop as **substantive** and defer the theme itself to this chapter (canonical slug `fold-solve-time-step-body`, cycle-059). This chapter is that theme.

**Load-bearing framing correction (vs the planner's working description).** The planner's scope described this theme as "how the L3 per-step **body** lowers to L2." On inspection the per-step body does NOT lower to an L2 composition: unlike L3 [`eigsolve`](../L3/eigsolve.md) — whose per-step body `apply_shift_invert = apply_linop ▷ ksp_solve` IS a visible L2 composition that maps line-for-line (the body-identity-in-form half of [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md)) — `fold_solve`'s per-step body is the **opaque MFEM `ode->Step` integrator leaf** (`palace/models/timeoperator.cpp:410`), which does NOT decompose into L2 base primitives. So the substantive L3>L2 content is **not** a body-composition rotation; it is the **outer-sweep erasure** (the carry-threaded iteration view → an L2 fold-by-role) with the **opaque per-step leaf staying opaque**. The theme is named `fold-solve-time-step-body` per the planner's canonical slug, but its content is the sweep-erasure + the opaque-leaf record, NOT a body decomposition (this is recorded as the load-bearing scoping in §Justification kind + §"What this lowering does NOT cover").

`fold_solve` and [`solve_family`](../L4/solve_family.md) are the two children of the strawman §3.7 [`iterate-while`](../L4/iterate-while.md) family. `solve_family` has **no L3 entry** (c057 D1 NO-ENTRY — its family loop lifts, embarrassingly parallel), so it has no L3>L2 theme. `fold_solve`'s sweep does NOT lift (carry-threaded + opaque per-step), so it has both an L3 entry and this L3>L2 theme. Among the substantive L3>L2 themes (the erasure-scope taxonomy, `L3-L2/index.md` §Working-Notes), this theme is the **carry-threaded sibling of the opaque-library root**:

- [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md) (firm c045, **opaque-library** root) — the L3 form names the eigen-iteration `eigen_iterate` by role **with an obstruction marker** (Palace authors no loop), and L2 references the library fold by role only, erasing the marker. The per-step body lifts to a visible L2 composition (identity-in-form).
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

None. This theme lowers the already-firm-structure L3 [`fold_solve`](../L3/fold_solve.md) (`partial-obstruction`, cycle-059 D1) to the L2 fold-by-role form. The per-step `time_step_op` is the opaque-library leaf already recorded at L0 (`palace/models/timeoperator.cpp:410`); no new speculative operator is introduced.

## Verified-against

L3 source (the LHS of this rewrite):

- `book/src/L3/fold_solve.md` (cycle-059 D1, `partial-obstruction`; **same-cycle sibling** — authored by D1, lands at integration before the single finalize build) — the L3 state-threaded fold time-sweep: §Signature, §Semantics (the per-step body lifts / the outer sweep does not lift), §"Value-threaded form (L3 rendering)" (the `step_loop` tail recursion — the LHS), §"Algebraic laws" (Law 1 schedule-split, Law 2 operator-capture-once, Law 3 seed identity, the carry-threading + opaque-per-step non-law — the transported properties), §"Downward to L2" / §"L3 vs L2 distinction" (the in-line rotation-direction record this theme realizes), §Status (the `partial-obstruction` basis).

L2 source (the RHS of this rewrite):

- **No `book/src/L2/fold_solve.md`** — there is no standalone L2 entry (the per-step body is an opaque leaf that does not decompose into L2 primitives; the L2 RHS is the fold-by-role form the iteration-rotation erasure produces). The fold-by-role treatment follows L2 [`eigsolve`](../L2/eigsolve.md) (the eigen-iteration fold named by role; the model for the L2 RHS shape).
- `book/src/L3-L2/eigsolve-opaque-eigen-iteration.md` (firm c045) — the **structurally-parallel** L3>L2 theme this theme follows; the load-bearing contrast is the per-step body (eigsolve's lifts to a visible L2 composition — body-identity-in-form; fold_solve's stays opaque — no body half).
- `book/src/L3-L2/index.md` §"Erasure-scope taxonomy" — the substantive-L3>L2 axis this theme joins (the carry-threaded sibling of the opaque-library root).

L0 evidence (the fixed-schedule fold-sweep witness; self-verified exact against on-disk source this dispatch via `palace-codemap` `read_range` + `tools/citecheck/citecheck.py --anchor`):

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

`firm` — on the **structural rotation** (the outer-sweep erasure). The iteration-view erasure (the L3 explicit carry-threaded tail recursion + first-class `sequential-obstruction` marker → the L2 fold-by-role composition with the obstruction shadowed to non-laws) is read **directly off** the structural relationship between the firm-structure L3 entry's §"Value-threaded form" and the fold-by-role L2 form, witnessed exactly by the transient driver loop (`palace/drivers/transientsolver.cpp:33-99` + `palace/models/timeoperator.cpp:312,410`), with the driven-PROM SweepAdaptive sweep (`palace/drivers/drivensolver.cpp:231-389`) the structurally-parallel second carry-threaded-spine witness. The operator-capture hoist, the in-place `sol` threading, and the opaque per-step call are positive source facts. Justification is `structural` + secondary `obstruction (opaque-library-ownership)` on the per-step leaf. No speculative operator introduced. This theme is the **carry-threaded sibling** of the firm [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md) (c045) — same iteration-view erasure, but where `eigsolve`'s L3 marker is "Palace authors no loop" and its per-step body lifts to an L2 composition (body-identity half), `fold_solve`'s L3 marker is the carry-threading obstruction on a Palace-authored sweep and its per-step body is an opaque leaf (no body half).

**On the per-step opaque-library sub-leaf (load-bearing scoping).** The per-step body `ode->Step(sol, t, dt)` (`palace/models/timeoperator.cpp:410`) is an `obstruction (opaque-library-ownership)` sub-leaf — the MFEM `ODESolver` interior is library-owned, never exposed by Palace standalone, with NO conventional promotion route. This does **NOT** demote the whole theme to obstruction: the theme is `firm` on the *outer-sweep structural rotation* (the iteration-view erasure, read off positive source); only the *per-step body* is the opaque leaf, recorded (negative anchor = Palace's CALL `:410`) rather than lowered. Unlike the `eigsolve` sibling (whose per-step body DOES open to an L2 composition), `fold_solve`'s per-step body stays opaque — so this theme has no body-identity half; its whole substantive content is the sweep erasure.

**Scope (load-bearing)**: this theme covers the **fixed-schedule** fold erasure, witnessed by the **transient** pipeline. The **driven-PROM SweepAdaptive** state-generated greedy march (`palace/drivers/drivensolver.cpp:231-389`) shares the carry-threaded sweep spine but generates its schedule from the carry — its dedicated treatment (if warranted) is gated on the cap's OQ `fold-solve-greedy-schedule-source-generalization` (batch-18), NOT covered here. The other three pipelines: electrostatic + magnetostatic are the independent-**map** [`solve_family`](../L4/solve_family.md) (no carry — no L3 entry, no L3>L2 theme); eigenmode's eigen-iteration is the opaque-library [`eigsolve`](../L3/eigsolve.md). Do NOT claim cross-pipeline generality beyond the fixed-schedule transient fold + the SweepAdaptive carry-threaded-spine parallel.

This dispatch (cycle-059 D1) is the **L3>L2 outer-sweep erasure** for the `fold_solve` chain, landed alongside the L3 entry it lowers (cycle-059 D1, same dispatch). It realizes the in-line rotation direction the L3 entry's §"Downward to L2" records and is the authoritative home for the carry-threaded sweep-erasure stratum, structurally parallel to the opaque-library [`eigsolve-opaque-eigen-iteration`](./eigsolve-opaque-eigen-iteration.md).
```

```edit:book/src/L3/index.md
| [`orthogonalize`](./orthogonalize.md) | `(op, w, V) -> { residual, coeffs }` (variant-split Gram-Schmidt orthogonalize-against-basis; removes `span(V)`-component of `w`, returns orthogonal residual + Hessenberg-column coefficients; one runtime variant axis `gs_orthog ∈ {MGS, CGS, CGS2}` — the axis the L3 lift verdict SPLITS along). | **Same-layer L3** (per-step body, NOT a leaf): [`dot`](./dot.md) (the projection coefficient `H_j = op.dot(w_eff(j), V[j])` / the batched `coeffs = Vᴴw` for CGS/CGS2), [`axpy`](./axpy.md) (the residual update `w − H_j·V[j]` / the batched `w − V·coeffs`). NOT `nrm2`/`scal` (caller's normalisation, excluded by the L0 no-output-normalisation contract). Concepts: `sequential-obstruction` (the MGS `j`-loop obstruction), `tensor-field-lift` (the variant-split body-lifts/MGS-loop-doesn't case), `variant-absorption` (the `gs_orthog` axis, residual-axis disclosure `:131`). No firm L4 `orthogonalize` (the Arnoldi-step-monad surface is unauthored); lifts from L2 only. | L2 [`orthogonalize`](../L2/orthogonalize.md) (body identity-in-form on the per-step `dot`+`axpy`; the surface adjustment makes the MGS `j`-recurrence explicit as a `sequential-obstruction` marker and the CGS/CGS2 batched form explicit as a clean lift; no L3-L2 theme file — in-line annotation per cycle-012 non-adjacent-identity convention, precedent `chebyshev`/`eigsolve`). Transitive L3>L1 body identity in-line (L3>L2 ∘ L2>L1 identity); no `L3-L1/` directory. Substantive rotation is the L1>L0 [`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md). | `partial-obstruction` (harvested cycle-040T235349Z; **third L3 `partial-obstruction`** after `chebyshev` c013 + `eigsolve` c024 — the substantive **(B)** member of the cycle-036 D2 audit verdict at `book/src/L3/index.md:48`; the per-step body lifts whole-tensor for all variants and CGS/CGS2 lift entirely to the batched `H = Vᴴw` / `w' = w − VH` global statements — but the **MGS `j`-loop is a witnessed `sequential-obstruction`** (field-side loop-carried candidate `w^(j)`, basis-index recurrence, numerical-stability-rooted: the batched form *is* CGS, losing MGS's roundoff-orthogonality; `concepts/sequential-obstruction.md:37-48`). DISTINGUISHING feature: the obstruction is **variant-conditional** — present for MGS, absent for CGS/CGS2 — so the partial-obstruction verdict SPLITS along the `gs_orthog` axis, a structure neither precedent exhibits (`chebyshev`/`eigsolve` obstructions are unconditional). MGS-obstruction root parallels `chebyshev` (numerical stability), not `eigsolve` (opaque-library). Carries dedicated all-three-variant test coverage `test-orthog.cpp:99-160, 234` — exceeds the `chebyshev` test bar; **firm-on-positive-structure** body laws on the `orthog.hpp:41-89` MGS/CGS bodies; layer-coherence backfill per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** + **partial-obstruction is first-class** (cycle-021); OQ `l3-cohort-growth-audit-c036-verdict` (B) member) |
| [`fold_solve`](./fold_solve.md) | `(op, s0, schedule) -> s_final` (value-threaded state-threaded fold time-sweep; the per-step body is one opaque whole-state advance `time_step_op op s t`, the outer sweep threads the persistent field-state in place over a schedule). | **No same-layer L3 dependency** — the per-step body is an opaque MFEM `ode->Step` integrator leaf (`palace/models/timeoperator.cpp:410`) that does NOT decompose into L3 field primitives (the contrast with `eigsolve`, whose body's constituent is the firm L3 `ksp_solve`). Concepts: `sequential-obstruction` (the carry-threading obstruction this operator carries), `tensor-field-lift`, `state-stratification`, `constructed-operators`, `variant-absorption`. Lifts from L4 [`fold_solve`](../L4/fold_solve.md) (firm c058 D1) via [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md) (firm c058 D2; per-step body identity-in-form, wrapper substantive). | L2 fold-by-role (NO standalone `L2/fold_solve` entry — the per-step body is an opaque leaf that does NOT decompose into L2 primitives; the L3>L2 hop is the substantive outer-sweep erasure to a fold-by-role, NOT a body-composition rotation) via the L3>L2 theme [`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md) (cycle-059; structurally parallel to `eigsolve-opaque-eigen-iteration`, strengthened by the carry-threading obstruction). | `partial-obstruction` (abstracted cycle-059T061737Z D1; the **fourth L3 `partial-obstruction`** after `chebyshev` c013, `eigsolve` c024, `orthogonalize` c040 — the **fold-image** of the L4 `fold_solve` combinator. Body lifts (one opaque whole-state advance, identity-in-form to the L4 form), but the outer sweep does NOT lift for TWO reasons: the **carry-threading `sequential-obstruction`** (each step's input is the prior step's in-place write to `sol`, `timeoperator.cpp:410`; the schedule does not commute — the cap's load-bearing non-law) AND an **opaque-library per-step leaf** (the MFEM `ODESolver` step). A NEW combined-obstruction shape — carry-threading + opaque-per-step — distinct from `chebyshev` (numerical-stability recurrence) and `eigsolve` (opaque-library WHOLE-loop). Crucially Palace AUTHORS the outer sweep (`transientsolver.cpp:77`), so it RENDERS as an explicit tail recursion (the `ksp_solve`/`chebyshev` rendering, NOT `eigsolve`'s un-renderable case) — the obstruction is the carry-threading + opaque leaf, not the whole loop being library-owned. The carry-threaded sibling of the embarrassingly-parallel [`solve_family`](../L4/solve_family.md) (whose loop lifts → NO standalone L3 entry, c057 D1 NO-ENTRY). Resolves OQ `fold-solve-l3-entry-vs-dissolution-home` (verdict L3-ENTRY); enacts the c058 D1 cap's likely-outcome prediction. **firm-on-positive-structure** — the sweep-structure laws are syntactic identities on the positive transient driver loop, missing dedicated test does not gate; the `partial-obstruction` status reflects the loop, not the body) |

## Working Notes
```

### L3 count tally bump (I own this — sole L3-touching dispatch this cycle, per the count-ownership convention). Surgical replace, OLD→NEW — replaces the trailing sentences of the `orthogonalize`-landing count-tally bullet (from "It is enumerated as **shape (e)**" through the OQ-resolution sentence):

```edit:book/src/L3/index.md
REPLACE (exact match) — OLD then NEW:

OLD:
It is enumerated as **shape (e)** in the §Semantics-overlay obstruction-profile spectrum (the variant-conditional sibling of `chebyshev`'s numerical-stability shape (b)). **L3 firm-operator count is now 17 firm + 3 `partial-obstruction`** (cycle-050 update below; was 15 firm + 3 at cycle-040) — firm (17): `krylov-step` c010; `apply_linop` + `axpy` + `axpby` + `axpbypcz` + `dot` + `nrm2` + `scal` c011; `ksp_solve` c020; `assemble-diagonal` + `jacobi-smoother` c037; `reciprocal` + `elementwise_product` + `divfree-projector` c038; `normalize` c039; **`linear_combination` + `inner_product` c050** — partial-obstruction (3): `chebyshev` c013, `eigsolve` c024, `orthogonalize` c040. This bullet is the **single authoritative count tally** (cycle-040 D2 layer-intro-author sole-owned it per the cycle-039 meta-phase count-ownership convention, friction-ledger `parallel-blind-shared-index-count-divergence`; cycle-050 D7 layer-intro-author re-owned it as the wave's sole count-owner — D1 (`linear_combination`) + D2 (`inner_product`) each deferred the tally entirely, writing only their own dep-map rows); the per-cycle running counts in the c024/c037/c039 bullets above are **superseded snapshots** (kept as narrative of what landed each cycle, not as the live count). The §Semantics-overlay taxonomy now enumerates **five** non-trivial obstruction shapes (a)/(b)/(c)/(d)/(e) — the fifth being `orthogonalize`'s variant-conditional partial-obstruction profile — plus the obstruction-free-end `fused-composite-obstruction-free` profile (`normalize`), resolving OQ `l3-index-fifth-obstruction-profile-fused-composite-obstruction-free` and OQ `l3-index-working-notes-stale-snapshot-compaction-candidate`.

NEW:
It is enumerated as **shape (e)** in the §Semantics-overlay obstruction-profile spectrum (the variant-conditional sibling of `chebyshev`'s numerical-stability shape (b)). **L3 firm-operator count is now 17 firm + 4 `partial-obstruction`** (cycle-059 update; was 17 firm + 3 at cycle-050) — firm (17): `krylov-step` c010; `apply_linop` + `axpy` + `axpby` + `axpbypcz` + `dot` + `nrm2` + `scal` c011; `ksp_solve` c020; `assemble-diagonal` + `jacobi-smoother` c037; `reciprocal` + `elementwise_product` + `divfree-projector` c038; `normalize` c039; **`linear_combination` + `inner_product` c050** — partial-obstruction (4): `chebyshev` c013, `eigsolve` c024, `orthogonalize` c040, **`fold_solve` c059**. This bullet is the **single authoritative count tally** (cycle-040 D2 layer-intro-author sole-owned it per the cycle-039 meta-phase count-ownership convention, friction-ledger `parallel-blind-shared-index-count-divergence`; cycle-050 D7 layer-intro-author re-owned it; cycle-059 D1 abstractor re-owned it as the sole L3-touching dispatch — landing `fold_solve` as the fourth `partial-obstruction`, no other L3 entry this cycle); the per-cycle running counts in the c024/c037/c039 bullets above are **superseded snapshots** (kept as narrative of what landed each cycle, not as the live count). The §Semantics-overlay taxonomy now enumerates **five** non-trivial obstruction shapes (a)/(b)/(c)/(d)/(e) — the fifth being `orthogonalize`'s variant-conditional partial-obstruction profile — plus the obstruction-free-end `fused-composite-obstruction-free` profile (`normalize`), resolving OQ `l3-index-fifth-obstruction-profile-fused-composite-obstruction-free` and OQ `l3-index-working-notes-stale-snapshot-compaction-candidate`. **`fold_solve` (c059) adds a SIXTH non-trivial obstruction shape (f): the combined carry-threading-sequential-obstruction + opaque-per-step-leaf on a Palace-authored, L3-rendered sweep** — distinct from (b) `chebyshev` (numerical-stability recurrence, body→L2 composition), (c) `eigsolve` (opaque-library WHOLE-loop, un-renderable, body→L2 composition), and (e) `orthogonalize` (variant-conditional). The distinguishing facts of (f): the obstruction is the *carry-threading* (not a numerical recurrence, not a library-owned whole-loop), the loop IS Palace-authored and renders (the `ksp_solve`/`chebyshev` rendering, unlike `eigsolve`), and the per-step body is an opaque leaf with NO L2 composition (unlike `chebyshev`/`eigsolve`, whose bodies decompose).
```

### L3>L2 index: my table row + my cohort bullet + tally bump (I own all three — sole L3-L2-touching dispatch this cycle)

```edit:book/src/L3-L2/index.md
| [`chebyshev-nested-recurrence`](./chebyshev-nested-recurrence.md) | L3 [`chebyshev`](../L3/chebyshev.md) §"Value-threaded form (L3 rendering)" — the value-threaded `(op, x, y, initial_guess) -> y'` with **two nested** `iterate_while_pure_L3` tail recursions over step-count predicates (inner `kloop` over `k <= order-1`, outer `itloop` over `it <= pc_it`), each carrying a first-class `sequential-obstruction` (the **first** `partial-obstruction` L3 operator, c013). | L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) §Semantics — the `sweep` base-algebra composition with the inner `for k in 1 .. order-1` loop referenced **as a composition driver** + the outer `pc_it`-sweep **named by role** (iteration view erased; the two obstructions shadow to the §"Algebraic laws" step-reordering / `pc_it`-commutativity / polynomial-expansion non-laws). | `structural` (the nested iteration-view erasure + two-obstruction-to-non-law shadow is a layer-surface-shape fact) + secondary `reduction-chain` (the two `iterate_while_pure_L3` → loop-as-driver/role-reference consolidations re-fold the strawman §3.7 reduction sequences) | `firm` (cycle-045 cross-cutter; the **third substantive / non-identity** L3>L2 theme and the **unconditional-nested-double-loop** member of the erasure-scope axis — the sibling of the unconditional-single-loop `ksp-solve-outer-driver` and the variant-conditional-single-loop `orthogonalize-variant-split`; body identity-in-form retained in-line) |
| [`fold-solve-time-step-body`](./fold-solve-time-step-body.md) | L3 [`fold_solve`](../L3/fold_solve.md) §"Value-threaded form (L3 rendering)" — the value-threaded `(op, s0, schedule) -> s_final` with the carry-threaded sweep rendered as an **explicit `step_loop` tail recursion** carrying the first-class **carry-threading `sequential-obstruction`** marker (Palace authors the sweep, so it renders — the `ksp_solve`/`chebyshev` rendering), the per-step body the **opaque `ode->Step` integrator leaf** (NOT a composition). | L2 **fold-by-role** (NO standalone `L2/fold_solve` entry) — the carry-threaded sweep referenced as a composition driver (`time_sweep_fold (time_step_op op) s0 schedule`, the iteration view erased; the carry-threading obstruction shadowed to the no-commutativity / no-whole-march-fusion non-laws), the per-step body the **same opaque leaf** (NOT opened — the distinguishing contrast with `eigsolve`, whose body DOES open to `apply_linop ▷ ksp_solve`). | `structural` (the iteration-view erasure of the Palace-authored carry-threaded sweep is a layer-surface-shape fact) + secondary `obstruction` (sub-kind `opaque-library-ownership`: the per-step `ode->Step` is an MFEM library leaf; negative anchor `timeoperator.cpp:410` is Palace's CALL, NOT MFEM internals) | `firm` (cycle-059 D1 abstractor; the **carry-threaded sibling** of the opaque-library `eigsolve-opaque-eigen-iteration` — same iteration-view erasure, but `fold_solve`'s L3 marker is the carry-threading obstruction on a Palace-authored sweep (NOT "Palace authors no loop") and its per-step body is an opaque leaf with NO body-identity half (the per-step `ode->Step` does NOT open to an L2 composition); landed alongside the L3 entry it lowers) |
```

```edit:book/src/L3-L2/index.md
- `eigsolve-opaque-eigen-iteration` (cycle-045) — the **third substantive** L3>L2 theme and the **third erasure-scope root: opaque-library**. The L3 `eigsolve` (`partial-obstruction`, cycle-024) per-step body `apply_shift_invert = apply_linop ▷ ksp_solve` lifts cleanly (identity-in-form to the L2 body), while its eigen-iteration loop is **opaque-library-owned** (SLEPc folds inside `EPSSolve(eps)`; ARPACK inside the `naupd` RCI driver). The L3 form names `eigen_iterate` by role **with an obstruction marker** — it cannot render the loop as a tail recursion because **Palace authors no loop** — and the L2 form references the library fold by role only, **erasing the marker** (it shadows to the L2 "Opening of the eigen-iteration fold at L2" + "Fold-merge / restart associativity" non-laws). **Opaque-library** — the loop lives *entirely outside Palace*; unlike the other two themes, L3 cannot even render the loop. The two erasure scopes (unconditional / variant-conditional) are now three (unconditional / variant-conditional / opaque-library); the meta-phase-flagged "substantive erasure scope" axis now has its third corner.
- `fold-solve-time-step-body` (cycle-059) — the **carry-threaded sibling** of the opaque-library root. The L3 `fold_solve` (`partial-obstruction`, cycle-059) carry-threaded sweep renders as an explicit `step_loop` tail recursion carrying the first-class **carry-threading `sequential-obstruction`** marker (Palace AUTHORS the sweep `transientsolver.cpp:77`, so unlike `eigsolve` it RENDERS — the `ksp_solve`/`chebyshev` rendering); it lowers to the L2 fold-by-role composition with the obstruction marker erased to the no-commutativity / no-whole-march-fusion non-laws. **Distinguishing structural facts vs the `eigsolve` sibling**: (i) `fold_solve`'s L3 marker is the *carry-threading* obstruction on a *Palace-authored* sweep (NOT "Palace authors no loop"); (ii) `fold_solve`'s per-step body is an **opaque leaf** (`ode->Step`) that does NOT open to an L2 composition — so this theme has **no body-identity-in-form half** (the `eigsolve` body lifts to `apply_linop ▷ ksp_solve`; the `fold_solve` body stays opaque), and its whole substantive content is the sweep erasure. Obstruction sub-kind `opaque-library-ownership` on the per-step leaf (per CLAUDE.md). The substantive-erasure axis now spans: unconditional-single-loop (`ksp-solve-outer-driver`), unconditional-nested-double-loop (`chebyshev-nested-recurrence`), variant-conditional-single-loop (`orthogonalize-variant-split`), opaque-library-whole-loop (`eigsolve-opaque-eigen-iteration`), and carry-threaded-Palace-authored-sweep-with-opaque-leaf (`fold-solve-time-step-body`, this theme).
```

Surgical replace, OLD→NEW — the cohort-growth count line (replaces only the leading count clause + adds the cycle-059 sentence + coverage note; the rest of the long prior bullet is preserved by matching only its opening segment up to "**17 → 13 → 5**." and re-appending the cycle-059 content before the surviving-themes sentence):

```edit:book/src/L3-L2/index.md
REPLACE (exact match) — OLD then NEW:

OLD:
- **Cohort growth (firm 17 → 13 cycle-050 → 5 cycle-051; CONSOLIDATED post-cohort count — degenerate-theme demotion COMPLETE).** The refactor-pass enactment under the 2026-06-01 VOCABULARY-SHIFT REDIRECT (`METHODOLOGY-REDIRECT.md`) demoted **twelve thin `-body-identity` L3>L2 themes** to in-line / combinator-home notes across two cycles. **Cycle-050 (4, D3–D6):** `assemble-diagonal-body-identity`, `elementwise-product-body-identity`, `reciprocal-body-identity`, `normalize-body-identity` (standalone / fused-composite floors, NO fold-parent — demoted to in-line §"Downward to L2" notes on their L3 entries). **Cycle-051 (8, D1–D4):** the `linear_combination` family `scal`/`axpy`/`axpby`/`axpbypcz`-body-identity (D1 — collapsed into the firm [`linear_combination`](../L3/linear_combination.md) combinator's §"Downward to L2" note, the four L3 leaves re-expressed through the combinator), `dot-body-identity` (D2 — collapsed into the firm [`inner_product`](../L3/inner_product.md) combinator's §"Downward to L2" note), `nrm2-body-identity` (D3 — demoted to an in-line CONSUMER note on `L3/nrm2.md`, do-NOT-merge), and the two gated constructed-operator-gate pairs `jacobi-smoother-body-identity` + `divfree-projector-body-identity` (D4 — DEMOTE-OK per the D8 verify-body audit `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`, demoted to in-line §"Downward to L2" notes on their L3 entries). Each was a degenerate identity-in-named-terms lowering (the §1d smell the redirect names); the theme files are deleted and the rotations captured in-line / through the combinator homes (no operator chapter collapses — the leaf CHAPTERS are re-expressed-in-place / retained, only the THEME files delete). **The L3>L2 rotation for each operator remains captured** — the coverage-gap is unaffected in *kind*; only the firm-theme COUNT drops, **17 → 13 → 5**. The **5 surviving firm L3>L2 themes** are all substantive or the lone multi-primitive body-identity: `krylov-step-body-identity` (the five-primitive-group body identity + wrapper-surface adjustments — the one identity-theme that survives, distinct from the demoted single-leaf/gate degenerates), `ksp-solve-outer-driver`, `orthogonalize-variant-split`, `eigsolve-opaque-eigen-iteration`, `chebyshev-nested-recurrence` (the four substantive / non-identity iteration-rotation themes across the four erasure-scope roots).

NEW:
- **Cohort growth (firm 17 → 13 cycle-050 → 5 cycle-051 → 6 cycle-059; CONSOLIDATED post-cohort count).** The refactor-pass enactment under the 2026-06-01 VOCABULARY-SHIFT REDIRECT (`METHODOLOGY-REDIRECT.md`) demoted **twelve thin `-body-identity` L3>L2 themes** to in-line / combinator-home notes across two cycles. **Cycle-050 (4, D3–D6):** `assemble-diagonal-body-identity`, `elementwise-product-body-identity`, `reciprocal-body-identity`, `normalize-body-identity` (standalone / fused-composite floors, NO fold-parent — demoted to in-line §"Downward to L2" notes on their L3 entries). **Cycle-051 (8, D1–D4):** the `linear_combination` family `scal`/`axpy`/`axpby`/`axpbypcz`-body-identity (D1 — collapsed into the firm [`linear_combination`](../L3/linear_combination.md) combinator's §"Downward to L2" note, the four L3 leaves re-expressed through the combinator), `dot-body-identity` (D2 — collapsed into the firm [`inner_product`](../L3/inner_product.md) combinator's §"Downward to L2" note), `nrm2-body-identity` (D3 — demoted to an in-line CONSUMER note on `L3/nrm2.md`, do-NOT-merge), and the two gated constructed-operator-gate pairs `jacobi-smoother-body-identity` + `divfree-projector-body-identity` (D4 — DEMOTE-OK per the D8 verify-body audit `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`, demoted to in-line §"Downward to L2" notes on their L3 entries). Each was a degenerate identity-in-named-terms lowering (the §1d smell the redirect names); the theme files are deleted and the rotations captured in-line / through the combinator homes (no operator chapter collapses — the leaf CHAPTERS are re-expressed-in-place / retained, only the THEME files delete). **The L3>L2 rotation for each operator remains captured** — the coverage-gap is unaffected in *kind*; only the firm-theme COUNT drops, **17 → 13 → 5**, then **cycle-059 adds the sixth surviving firm theme** — `fold-solve-time-step-body` (D1 abstractor), the **fifth substantive / non-identity** L3>L2 theme and the **carry-threaded sibling of the opaque-library erasure root** (landed alongside the new L3 [`fold_solve`](../L3/fold_solve.md) `partial-obstruction` entry it lowers; `fold_solve` is the first NEW L3 operator above the c036-era 18-operator cohort to land both an L3 entry and an L3>L2 theme since the refactor pass — it does NOT affect the `l3-l2-rotation-theme-coverage-gap` denominator, it is the L4-combinator-image frontier, fully covered on landing). The **6 surviving firm L3>L2 themes** are all substantive or the lone multi-primitive body-identity: `krylov-step-body-identity` (the five-primitive-group body identity + wrapper-surface adjustments — the one identity-theme that survives, distinct from the demoted single-leaf/gate degenerates), `ksp-solve-outer-driver`, `orthogonalize-variant-split`, `eigsolve-opaque-eigen-iteration`, `chebyshev-nested-recurrence`, **`fold-solve-time-step-body`** (the five substantive / non-identity iteration-rotation themes — `fold-solve-time-step-body` joins the four erasure-scope roots as the carry-threaded-Palace-authored-sweep variant).
```

### SUMMARY.md registration (my new L3 chapter + my new L3>L2 chapter — always mine)

```edit:book/src/SUMMARY.md
- [orthogonalize](./L3/orthogonalize.md)
- [fold_solve](./L3/fold_solve.md)
```

```edit:book/src/SUMMARY.md
- [chebyshev-nested-recurrence](./L3-L2/chebyshev-nested-recurrence.md)
- [fold-solve-time-step-body](./L3-L2/fold-solve-time-step-body.md)
```

### Coupled re-anchor 1 — the firm L4 cap §"Lowers to" (currently defers the standalone-L3-entry question; re-anchor to the live L3 entry). Surgical replace, OLD→NEW:

```edit:book/src/L4/fold_solve.md
REPLACE the existing sentence (exact match) — OLD then NEW:

OLD:
This entry records the rotation *direction* (L4 fold combinator → L3 explicit in-place-threading loop with an opaque per-step body) in-line per high→low discipline; it does **not** author the theme. Whether a standalone `L3/fold_solve` entry is warranted (vs. the dissolution theme being the authoritative L3-form home, as for [`solve_family`](./solve_family.md)) is a batch-18 judgment: unlike `solve_family`'s family loop (which lifts cleanly — no obstruction), `fold_solve`'s loop carries BOTH a carry-threading sequential-obstruction AND an opaque-library per-step body, so an L3 entry recording the `partial-obstruction` (the `chebyshev` / `eigsolve` shape) is the likelier outcome — but that is the D2 theme's + a future L3 dispatch's call, not this entry's (OQ `fold-solve-l3-entry-vs-dissolution-home`).

NEW:
This entry records the rotation *direction* (L4 fold combinator → L3 explicit in-place-threading loop with an opaque per-step body) in-line per high→low discipline; it does **not** author the theme. The standalone L3 entry question is **RESOLVED (cycle-059 D1, verdict L3-ENTRY)**: a standalone [`L3/fold_solve`](../L3/fold_solve.md) entry IS warranted (status `partial-obstruction`), because — unlike `solve_family`'s family loop (which lifts cleanly — no obstruction, so its dissolution theme is the authoritative L3-form home, NO-ENTRY c057) — `fold_solve`'s loop carries BOTH a carry-threading sequential-obstruction AND an opaque-library per-step body, so the L3 form is a genuine iteration-rotation `partial-obstruction` (the `chebyshev` / `eigsolve` shape) with its own standing L3-vocabulary home. The L3 entry is the standing iteration-rotation definition of the obstruction structure; this dissolution theme records the L4→L3 rewrite *direction* (forward) — the `chebyshev`/`eigsolve` division of labor. (Resolves OQ `fold-solve-l3-entry-vs-dissolution-home`.)
```

### Coupled re-anchor 2 — the c058 D2 L4>L3 theme §"What this lowering does NOT cover" (the L3>L2-hop bullet defers the standalone-L3-entry question; re-anchor). Surgical replace, OLD→NEW:

```edit:book/src/L4-L3/fold-solve-time-step-dissolution.md
REPLACE the existing bullet (exact match) — OLD then NEW:

OLD:
- **The L3>L2 hop.** Whether a standalone `L3/fold_solve` entry is warranted (likely `partial-obstruction` — the carry-threading sequential-obstruction + the opaque per-step body, the [`chebyshev`](../L3/chebyshev.md) / `eigsolve` shape) vs. this theme being the authoritative L3-form home is the cap's OQ `fold-solve-l3-entry-vs-dissolution-home` (batch-18). Unlike the map sibling (whose family loop lifts cleanly, NO-ENTRY warrant), the fold loop carries BOTH obstructions, so an L3 `partial-obstruction` entry is the likelier outcome — but that is a future L3 dispatch's call, not this theme's.

NEW:
- **The L3>L2 hop.** A standalone `L3/fold_solve` entry **IS warranted (RESOLVED cycle-059 D1, verdict L3-ENTRY)** — status `partial-obstruction` (the carry-threading sequential-obstruction + the opaque per-step body, the [`chebyshev`](../L3/chebyshev.md) / `eigsolve` shape), per OQ `fold-solve-l3-entry-vs-dissolution-home` (now CLOSED). Unlike the map sibling (whose family loop lifts cleanly, NO-ENTRY warrant), the fold loop carries BOTH obstructions, so the L3 [`fold_solve`](../L3/fold_solve.md) entry is the standing iteration-rotation home, and its L3>L2 hop is the dedicated theme [`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md) (cycle-059; the outer-sweep erasure to an L2 fold-by-role + the opaque per-step leaf staying opaque). This L4>L3 theme records only the L4→L3 rewrite *direction*; the L3 entry + its L3>L2 theme are the lower-edge homes.
```

### Coupled re-anchor 3 — the c058 D2 L4>L3 theme §Verified-against L3-source note (currently says "No `book/src/L3/fold_solve.md` (yet)"; re-anchor to the live entry). Surgical replace, OLD→NEW:

```edit:book/src/L4-L3/fold-solve-time-step-dissolution.md
REPLACE the existing bullet (exact match) — OLD then NEW:

OLD:
- **No `book/src/L3/fold_solve.md` (yet)** — the standalone-L3-entry question is the cap's OQ `fold-solve-l3-entry-vs-dissolution-home` (batch-18; likely `partial-obstruction` — the carry-threading obstruction + the opaque per-step body, the [`chebyshev`](../L3/chebyshev.md) shape). Until decided, this theme's §"L3 form (RHS)" is the authoritative L3-form home for the fixed-schedule fold shell.

NEW:
- **`book/src/L3/fold_solve.md` (cycle-059 D1, `partial-obstruction`)** — the standalone L3 entry IS warranted (the standalone-L3-entry question RESOLVED cycle-059 D1, verdict L3-ENTRY, per OQ `fold-solve-l3-entry-vs-dissolution-home`, now CLOSED): the carry-threading sequential-obstruction + the opaque per-step body make the L3 form a genuine iteration-rotation `partial-obstruction` (the [`chebyshev`](../L3/chebyshev.md) shape), so the L3 entry — not this dissolution theme — is the authoritative L3-form home, and its L3>L2 hop is the dedicated theme [`fold-solve-time-step-body`](../L3-L2/fold-solve-time-step-body.md) (cycle-059).
```

## Speculative operators proposed

None. This dispatch lands an L3 entry + an L3>L2 theme for the already-firm L4 `fold_solve` combinator (firm c058 D1). The per-step `time_step_op` and the `TimeState` / `sol` carry are speculative rough-in sub-operators already named in the firm L4 cap's §Dependencies (not introduced here); the per-step `time_step_op` is recorded as the opaque-library obstruction sub-leaf at L0 (`palace/models/timeoperator.cpp:410`). No new speculative operator is introduced at L3.

## Supporting evidence

All L0 citations self-verified against on-disk source this dispatch via `palace-codemap` `read_range` + `tools/citecheck/citecheck.py --anchor` (citecheck `[ok]` on all eight load-bearing anchors: `transientsolver.cpp:33,77,89,93`, `timeoperator.cpp:312,410`, `drivensolver.cpp:231,384,389`).

- **Transient fixed-schedule fold-sweep (positive, the LHS witness):** `palace/drivers/transientsolver.cpp:33` (`TimeOperator` built once, outside the loop), `:35` (`delta_t` uniform timestep), `:36` (`n_step` fixed bound), `:77` (`for (int step ...)` the Palace-authored sweep — renders, unlike `eigsolve`), `:89` (`time_op.Init()` seed `s0` in place), `:93` (`time_op.Step(t, delta_t)` per-step body call), `:98`/`:99` (`GetE`/`GetB` per-step `(E,B)` readout of `sol`). `palace/models/timeoperator.cpp:312` (`op = std::make_unique<TimeDependentFirstOrderOperator>(...)` constructed once), `:410` (`ode->Step(sol, t, dt)` the opaque MFEM `ODESolver` step advancing `sol` IN PLACE — the carry-threading `sequential-obstruction` + the `obstruction (opaque-library-ownership)` per-step leaf; negative anchor = Palace's CALL, NOT MFEM internals).
- **Driven-PROM SweepAdaptive state-generated fold-spine second witness:** `palace/drivers/drivensolver.cpp:231` (`SweepAdaptive` greedy march entry), `:384` (`for (... it < max_size_per_excitation && memory < convergence_memory ...)` state-derived loop bound), `:389` (`omega_star = prom_op.FindMaxError(...)` state-derived per-step input).
- **Precedent + contrast entries:** `book/src/L3/chebyshev.md` (partial-obstruction precedent, numerical-stability recurrence), `book/src/L3/eigsolve.md` (partial-obstruction precedent, opaque-library whole-loop), `book/src/L4/solve_family.md` §"Lowers to" (the c057 D1 NO-ENTRY warrant — embarrassingly-parallel map contrast), `book/src/L3-L2/eigsolve-opaque-eigen-iteration.md` (the structurally-parallel L3>L2 opaque-library theme), `book/src/L4/fold_solve.md` + `book/src/L4-L3/fold-solve-time-step-dissolution.md` (the firm c058 cap + dissolution this lifts from).

## Open questions / caveats

1. **The planner's `fold-solve-time-step-body` slug describes a body-lowering that does NOT exist.** The planner scope framed the L3>L2 theme as "how the L3 per-step **body** lowers to L2." On inspection, `fold_solve`'s per-step body is the **opaque `ode->Step` integrator leaf** — it does NOT decompose into L2 primitives (the contrast with `eigsolve`, whose per-step body `apply_shift_invert = apply_linop ▷ ksp_solve` IS a visible L2 composition). I retained the planner's canonical slug `fold-solve-time-step-body` (per the cross-report slug-divergence convention — do not self-invent), but the theme's substantive content is the **outer-sweep erasure** (the carry-threaded iteration view → an L2 fold-by-role) + the **opaque per-step leaf staying opaque**, NOT a body decomposition. This is recorded as load-bearing scoping in the theme's §Context framing-correction + §Justification kind + §"What this lowering does NOT cover." The integrator / meta-phase may wish to note the slug name slightly mis-describes the content (the "body" in the slug refers to the per-step body that is recorded opaque, not lowered) — a rename to e.g. `fold-solve-sweep-erasure` would be more accurate, but I did not rename (slug-stability + the planner stated it). Flag for reconciliation.

2. **No `L2/fold_solve` RHS entry exists.** The L3>L2 theme's RHS is a fold-by-role L2 form (modeled on L2 `eigsolve`'s eigen-iteration-fold-by-role) rather than a citation to a standalone L2 entry. This is consistent with the `eigsolve` precedent (whose L2 entry DOES exist, but whose eigen-iteration fold is named by role) — but `fold_solve` has no L2 entry at all. Whether the transient march warrants a standalone `L2/fold_solve` entry (the fusion-rotation view) is a downstream question; for now the L3>L2 theme is the authoritative L2-form home for the fold-by-role shape, analogous to how `solve_family`'s dissolution theme is the authoritative L3-form home for the map. Not opened as a formal OQ (low fan-out until a downstream L2 consumer pulls); recorded here.

3. **Sixth obstruction-profile shape (f) added to the L3 §Semantics-overlay taxonomy.** `fold_solve`'s combined carry-threading + opaque-per-step obstruction on a Palace-authored, L3-rendered sweep is a genuinely new profile (recorded in the L3 count-tally bump). I added it as shape (f) inline in the count tally rather than rewriting the §Semantics-overlay spectrum prose (that prose is long and the count-tally bullet is the authoritative count home); a layer-intro-author follow-up may wish to fold shape (f) into the §Semantics-overlay obstruction-profile spectrum prose at `book/src/L3/index.md:15` for completeness. Low priority (the count-tally bullet carries the authoritative enumeration).
