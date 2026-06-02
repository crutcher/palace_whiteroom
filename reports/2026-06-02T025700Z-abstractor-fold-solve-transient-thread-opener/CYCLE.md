---
agent: abstractor
invoked_at: 2026-06-02T025700Z
scope: L4 thread-opener (observation-first) — fold_solve / time_step_fold transient combinator
status: pending
integrated_at: 2026-06-02T050000Z
integration_commit: 26c8b3c
integration_notes: "Applied cycle-057 (D4). 1 rough-in fold_solve/time_step_fold dep-map row + 1 frontier bullet in L4/index.md — the transient state-threaded FOLD outer-driver, the fold-counterpart of solve_family's independent MAP (both children of strawman §3.7 iterate_while). L4 rough-in +1 (L4 firm UNCHANGED 6). Slug plain-text/code-span (no fold_solve.md, no theme, no dangling link). Held rough-in (1 transient witness; opaque MFEM ODESolver per-step body). 3 OQs promoted. Build clean."
inputs:
  - reference/palace/palace/drivers/transientsolver.cpp:24-114 (TransientSolver::Solve, the time-stepping driver loop)
  - reference/palace/palace/models/timeoperator.cpp:300-413 (TimeOperator integrator setup + Init + Step)
  - reference/palace/palace/models/timeoperator.hpp:30-72 (TimeOperator members: Vector E,B,sol; unique_ptr<ODESolver> ode)
  - book/src/L4/solve_family.md (the sibling independent-map combinator)
  - book/src/L4/index.md:59-64 (the L4 frontier prose that anticipates the fold-vs-map transient question)
  - book/src/design/l4_calculus.md:150-184 (strawman §3.7 iterate_while family)
  - scaffolding/open-questions.md:899-910 (cycle-056 D1 finding naming fold_solve / time_step_fold as the spine finding)
---

# CYCLE: L4 thread-opener — `fold_solve` / `time_step_fold` transient combinator

## Summary

This is a **thread-opening probe** (observation-first abstractor sketch, NOT a forced firm landing), the transient-pipeline analog of the FE-assembly thread-opener (cycle-053 D3). The cycle-056 D1 finding (`open-questions.md:899-910`) classified the three solver-driver pipelines into three distinct solve shapes and named the transient pipeline a **state-threaded FOLD** held OUT of the `solve_family` map family — explicitly tagging `fold_solve` / `time_step_fold` as a **spine finding** the spine will eventually need. This dispatch opens that thread: it maps the transient outer surface, confirms the fold shape against verified L0 evidence, sketches the `fold_solve` combinator and its three speculative rough-in operators (`fold_solve`/`time_step_fold`, `time_step_op`, the `TimeState` carry), and decides the layer (**L4 outer-driver vocabulary**, the state-threaded fold-counterpart of `solve_family`'s independent map — both sit one shell above the per-solve cap).

The load-bearing structural distinction: where `solve_family op rhss = map (ksp_solve op) rhss` collects **independent** members (no carry; cap Law 1 concatenation-homomorphism; embarrassingly parallel), the transient pipeline threads a **persistent field-state vector `sol`** step→step — `time_op.Step(t, dt)` (`transientsolver.cpp:93`) → `ode->Step(sol, t, dt)` (`timeoperator.cpp:410`) advances `sol` **in place**, each step's input being the previous step's output. That is a genuine left-fold `foldl step_op s0 [t_0..t_{n-1}]` with a sequential dependency between steps — the antithesis of the map's element-independence. The L4 index already anticipated exactly this question (`book/src/L4/index.md:61`: "check whether **transient** is a `map`-over-family or a stateful `fold`/`solve_loop` shape (a fold does NOT join the `solve_family` family)"); the evidence answers it decisively: **fold, not map.**

**Anchor decision (judgment): NO theme file authored this cycle.** This dispatch records the sketch as findings + speculative rough-in operators only, and proposes one dep-map rough-in row + one §frontier prose update at `book/src/L4/index.md` so the thread has a registered home. Rationale below (§Anchor decision). The genuinely-new transient vocabulary (the ODE-integrator step + the uniform time-step schedule) is isolated from what reuses the existing spine.

## Anchor decision — why findings + a dep-map rough-in row, NOT a theme file

The FE-assembly precedent (`fe-operator-assemble-mutation-rotation`, an L1>L0 rough-in theme) authored a theme file because FE-assembly bottoms out in a concrete Palace mutation pattern with a clean L0 source range that a theme RHS can target. The transient case is different in a way that argues against a theme file *this cycle*:

1. **`fold_solve` is a combinator, not yet a lowering.** Like its sibling `solve_family`, the natural first landing is an **L4 combinator entry** (the abstraction) — and the L4>L3 / L1>L0 *theme* (the rewrite) is downstream of that, exactly as `solve_family` (L4 entry cycle-055 D1) precedes `solve-family-map-dissolution` (L4>L3 theme, cycle-055 D2). Authoring a lowering theme before the L4 entry exists would invert that order.
2. **The per-step body bottoms out in an opaque library boundary.** The actual integration step `ode->Step(sol, t, dt)` (`timeoperator.cpp:410`) dispatches to an **MFEM-owned `mfem::ODESolver`** (`timeoperator.hpp:37`) — GeneralizedAlpha / SDIRK23 / ARKODE / CVODE (`timeoperator.cpp:314-389`). Palace owns the *outer time sweep* (the `for` loop, the `sol`-threading, the per-step postprocess) but the *single ODE step* is library-owned. This is the same opaque-library shape as `eigsolve`'s eigen-iteration. So the eventual lowering is a **role-naming wrapper over an opaque-library obstruction marker** on the per-step body — which is a finding to confirm with a 2nd witness, not to firm now.
3. **Single witness.** Per the promoted `disciplined-cross-pipeline-combinator-mining-gate` skill, a combinator authored from one pipeline is below the ≥2-witness bar. The transient fold is currently a **1-of-1 witness** (transient only). Authoring a firm/heavy theme would over-commit. A **rough-in dep-map row** (placeholder, plain-text per the missing-anchor convention) is the right weight — it registers the thread, names the operators, and hands off to a later harvester/combinator-miner who lands the L4 entry when a 2nd fold-witness (the cycle-056 D1 `SweepAdaptive` PROM candidate, `open-questions.md:910`) or a downstream pull justifies it.

So the proposed-changes below add (a) one rough-in dep-map row to `book/src/L4/index.md` and (b) one frontier-prose bullet — no new chapter file, no SUMMARY.md entry (a rough-in row with no anchor file gets no SUMMARY chapter). This is the lightest registration that keeps the thread discoverable.

## Sketch — the `fold_solve` / `time_step_fold` shape

### Shape (strawman notation, L4 conventions)

The transient outer driver is a **left-fold of a per-step ODE-advance over a uniform time-step schedule**, threading a persistent field-state carry:

    -- entry point: thread the persistent field-state through the uniform time-step schedule
    fold_solve :: OpParams -> TimeState -> [Time] -> TimeState
    fold_solve op s0 timesteps = foldl (\s t -> time_step_op op s t) s0 timesteps

    -- where one step advances the persistent field-state by one ODE integrator step:
    time_step_op :: OpParams -> TimeState -> Time -> TimeState

    -- equivalently, as a (carry-threading) iterate_while_pure over the step counter
    -- (the strawman §3.7 family; the carry is the field-state + step index, NOT independent members):
    fold_solve op s0 timesteps =
      iterate_while_pure
        { field: s0, step: 0 }                          -- carry = persistent field-state + counter
        (\c -> c.step < length timesteps)               -- continue while steps remain
        (\c -> { field: time_step_op op c.field (timesteps !! c.step)
               , step: c.step + 1 })
      .field

Contrast with the sibling `solve_family` (`book/src/L4/solve_family.md:40-54`):

| aspect | `solve_family` (map) | `fold_solve` (this) |
|---|---|---|
| combinator | `map (ksp_solve op) rhss` | `foldl (time_step_op op) s0 timesteps` |
| carry between members | **none** (independent) | **persistent `TimeState`** threaded step→step |
| member input | the per-index RHS `rhs_i` (independent) | the **previous step's output** `s_{i-1}` |
| result | the collected family `[x_i]` | the **final state** `s_n` (trajectory of per-step extras is pruned-by-default) |
| load-bearing law | concatenation-homomorphism (Law 1; splits/reorders) | **NO** concatenation/reorder law — sequential dependency |
| parallelism | embarrassingly parallel | **sequential-obstruction** (outer time sweep cannot reorder) |
| §3.7 degenerate | pure-`map` degenerate (trajectory IS the family) | genuine carry-threading fold (`iterate_while_pure`, carry = field-state) |

The `solve_family` entry's own §Status scope caveat (`solve_family.md:146`) already flagged this: *"check whether transient is a `map` or a stateful `fold`/`solve_loop` shape — a fold does NOT join this family."* The evidence confirms the fold reading.

### Where it sits in the L4 vocabulary

`fold_solve` is the **state-threaded fold-counterpart of `solve_family`** at the same architectural altitude — one coordination shell *above* the per-solve cap, in the strawman §3.7 `iterate_while` family. The relationship is:

- `solve_loop` (`L4/index.md:74`) — iterate-whiles over **inner** restart cycles of ONE solve (the `ksp_solve` cap's driver).
- `solve_family` (`L4/solve_family.md`) — **maps** the cap over an **independent** RHS family (no carry).
- `fold_solve` (this) — **folds** a per-step advance over a **time-step schedule**, threading a persistent field-state carry (sequential).

`solve_family` chose to render as the **pure-map degenerate** of §3.7 (reusing the firm `iterate-while` family, the `chebyshev` route, rather than a new iteration primitive). `fold_solve` is the **non-degenerate** member of the same §3.7 family — it actually uses the carry (`iterate_while_pure` with the field-state threaded), so it reuses the *same* firm `iterate-while` vocabulary even more directly than `solve_family` did. **This is the key vocabulary-reuse finding: `fold_solve` introduces NO new iteration primitive** — it is `iterate_while_pure` with a field-state carry. What IS genuinely new is the per-step *body* (`time_step_op`) and the *schedule* (the uniform `[Time]` list), not the loop combinator.

### Shared-parent question (surfaced for the meta-phase)

`solve_family` (map) and `fold_solve` (fold) are the **two §3.7 specializations** distinguished solely by whether the step carries state: a map is a fold whose step ignores the accumulator (`foldl (\_ x -> f x)` collected = `map f`). So the candidate shared parent is **the strawman §3.7 `iterate_while` family itself** — both are already specializations of it; neither needs a *new* parent abstraction. The cleaner framing (recommended) is: do NOT introduce a third combinator as a parent; both `solve_family` and `fold_solve` are §3.7-family entries, and the map-vs-fold distinction is the load-bearing axis between them. (See OQ `fold-solve-solve-family-share-iterate-while-parent` below — this is a question for the batch-17 meta-phase to ratify, not for this thread-opener to decide.)

## Speculative operators proposed

Three rough-in placeholders. Harvester/combinator-miner promotes them when the L4 entry lands (2nd witness or downstream pull). Signatures are best-guess in strawman notation.

- **`fold_solve` (alias `time_step_fold`)** — `fold_solve :: OpParams -> TimeState -> [Time] -> TimeState`. The transient outer-driver combinator: a left-fold of `time_step_op` over the uniform time-step schedule, threading the persistent field-state `TimeState` from step to step, returning the final state. The state-threaded fold-counterpart of `solve_family`'s independent map; a non-degenerate member of the strawman §3.7 `iterate_while` family (the carry is the field-state, not a per-member trajectory). **Two candidate slugs** because the cycle-056 D1 finding named both; recommend `fold_solve` as canonical (parallel to `solve_family`'s verb-noun shape) with `time_step_fold` as the descriptive alias. The genuinely-new vocabulary here is the *schedule* (`[Time]`, a uniform `delta_t`-spaced list of length `n_step`) and the *fold-not-map* carry discipline; the loop combinator itself reuses `iterate_while_pure`.

- **`time_step_op`** — `time_step_op :: OpParams -> TimeState -> Time -> TimeState`. One ODE-integrator step: advance the persistent field-state by one `delta_t`. The L4 image of `time_op.Step(t, dt)` (`transientsolver.cpp:93`) → `ode->Step(sol, t, dt)` (`timeoperator.cpp:410`). **This is where the opaque-library boundary lives**: the body dispatches to an MFEM-owned `mfem::ODESolver` (GeneralizedAlpha / SDIRK23 / ARKODE / CVODE; `timeoperator.cpp:314-389`), so the eventual lowering marks a `sequential-obstruction` / opaque-library boundary on this body (the `eigsolve` shape, not the `krylov-step` shape — the step is not a Palace-authored loop). `OpParams` carries the time-dependent operator + the constructed linear solver (`TimeDependentFirstOrderOperator` + its `kspA`, `timeoperator.cpp:319-321`, `:425-429`), captured once at construction (`TimeOperator` ctor) — the `SetOperators`-hoist analog, but the per-step body is opaque. This is the genuinely-new transient operator: the per-step ODE advance does NOT reuse the `ksp_solve` cap directly (the linear solve is *inside* the MFEM integrator's implicit solve, not a Palace-orchestrated Krylov loop).

- **`TimeState` (carry)** — `TimeState = { sol: Vector, t: Time }` (or, exposing the field views: `{ sol: Vector, E: VectorView, B: VectorView, t: Time }`). The persistent field-state carry threaded through the fold. The L4 image of `TimeOperator`'s `Vector E, B, sol` members (`timeoperator.hpp:34`), where `E` and `B` are **aliasing views** into the single backing `sol` vector (`E.MakeRef(sol, size_E, size_E)`, `B.MakeRef(sol, 2*size_E, size_B)`; `timeoperator.cpp:307-308`). The carry is `readwrite`-threaded (advanced in place at L0; threaded as a value at L4) — distinct from `solve_family`'s independent per-member `SimState`. The `E`/`B`-as-views-into-`sol` aliasing is a load-bearing L0 detail (the postprocess reads `E`/`B` which are windows on the same `sol` the integrator advanced) that the L4 `TimeState` makes structural; whether to expose the views or keep them derived is a refinement question for the L4 entry.

What reuses existing spine vs what is new:
- **Reuses**: the §3.7 `iterate_while`/`iterate_while_pure` family (the fold combinator), `state-stratification` (`op` captured once / persistent vs ephemeral carry), the `Outcome`/termination machinery in degenerate form (transient has a fixed `n_step` count, no convergence test — the predicate is a step-count predicate, the `chebyshev` route).
- **Genuinely new**: `time_step_op` (the opaque MFEM ODE-integrator step), the uniform time-step *schedule* (`[Time]`, `n_step = GetNumSteps(0, max_t, delta_t)`, `transientsolver.cpp:36`), and the `TimeState` field-state carry with its `E`/`B`-view aliasing.

## Supporting evidence

All L0 citations self-verified against on-disk source this dispatch via `tools/citecheck/citecheck.py --anchor` (two initial drifts corrected: the `for (int step` loop is `:77` not `:78`; the `n_step` decl is `:36` not `:35`; `space_op`/`time_op` at `:32`/`:33`; `switch` at `timeoperator.cpp:314`; `dt = dt_input` at `:412`).

**Transient driver — the fold surface (`palace/drivers/transientsolver.cpp`, `TransientSolver::Solve`):**
- `:32` (`SpaceOperator space_op(iodata, mesh)`) + `:33` (`TimeOperator time_op(iodata, space_op, dJdt_coef)`) — the operator + time-integrator constructed once, outside the loop (the `OpParams` capture-once analog).
- `:36` (`int n_step = config::GetNumSteps(0.0, iodata.solver.transient.max_t, delta_t)`) — the **uniform time-step schedule** length; `delta_t` from `iodata.solver.transient.delta_t` (`:35`). This is the `[Time]` list the fold ranges over.
- `:77` (`for (int step = 0; step < n_step; step++)`) — the **outer time sweep** (the fold).
- `:89` (`time_op.Init()`) — initial conditions seed the carry (`step == 0` branch; the fold's `s0`).
- `:93` (`time_op.Step(t, delta_t)`) — **the per-step advance** (`step != 0` branch); each call advances the persistent `sol` in place, input = previous step's output. **The load-bearing fold evidence.**
- `:98` (`const Vector &E = time_op.GetE()`) + `:99` (`const Vector &B = time_op.GetB()`) — the per-step readout of the field-state views.
- `:104` (`auto total_domain_energy = post_op.MeasureAndPrintAll(step, E, B, t, J_coef(t))`) — the per-step consumer (postprocess); the fold's per-step extras, consumed immediately (so not pruned in practice).

**Time operator — the per-step body + the persistent carry (`palace/models/timeoperator.cpp` / `.hpp`):**
- `timeoperator.hpp:34` (`Vector E, B, sol;`) — the **persistent field-state carry** (`TimeState`); `E`/`B` are views into `sol`.
- `timeoperator.hpp:37` (`std::unique_ptr<mfem::ODESolver> ode;`) — **the MFEM-owned integrator** (the opaque-library boundary).
- `timeoperator.cpp:307` (`E.MakeRef(sol, size_E, size_E)`) + `:308` (`B.MakeRef(sol, 2*size_E, size_B)`) — `E`/`B` alias windows into the single backing `sol` vector.
- `timeoperator.cpp:314` (`switch (solver.transient.type)`) through `:389` — the integrator variant dispatch (GEN_ALPHA `GeneralizedAlphaSolver`, RUNGE_KUTTA `SDIRK23Solver`, ARKODE, CVODE); all MFEM/SUNDIALS-owned. Variant absorbed into `OpParams` at construction.
- `timeoperator.cpp:400` (`sol = 0.0`, in `Init()`) — zero initial conditions (`s0`).
- `timeoperator.cpp:407` (`void TimeOperator::Step(double &t, double &dt)`) → `:410` (`ode->Step(sol, t, dt)`) → `:412` (`dt = dt_input`) — **the per-step `time_step_op` body**; the in-place advance of `sol` via the opaque `ode` integrator, with the user `dt` restored after (the integrator may sub-step internally).

**Sibling combinator + frontier grounding:**
- `book/src/L4/solve_family.md:40-54` (the independent-map sibling this contrasts with), `:146` (its §Status caveat already naming the fold-vs-map transient question).
- `book/src/L4/index.md:59-64` (the active-frontier prose; `:61` explicitly anticipates the transient fold-vs-map question).
- `book/src/design/l4_calculus.md:150-184` (strawman §3.7 `iterate_while` + `iterate_while_pure` sugar — the family `fold_solve` joins as a non-degenerate carry-threading member), `:186-228` (§3.8 demand-pruning, governing whether the per-step trajectory materializes).
- `scaffolding/open-questions.md:899-910` (cycle-056 D1 finding — the spine-finding classification naming `fold_solve` / `time_step_fold`; note D1 cited `transientsolver.cpp:94` for the advance, the verified line is `:93`).

## Proposed changes

```edit:book/src/L4/index.md
[Append one rough-in dep-map row to the §Operator dep-map table (after the `solve_family` row at :80). Plain-text name per the missing-anchor convention (no anchor file exists yet):]

| `fold_solve` *(rough-in; no anchor yet — thread-opener proposed-by abstractor:2026-06-02T025700Z-fold-solve-transient-thread-opener)* | `fold_solve :: OpParams -> TimeState -> [Time] -> TimeState`; `fold_solve op s0 timesteps = foldl (\s t -> time_step_op op s t) s0 timesteps`. The transient outer-driver **state-threaded fold** combinator: thread a persistent field-state carry `TimeState` through a uniform time-step schedule, advancing it one ODE-integrator step (`time_step_op`) per timestep, returning the final state. The state-threaded **fold-counterpart** of [`solve_family`](./solve_family.md)'s independent **map** (map collects independent members; fold threads the previous step's output as the next step's input — sequential). A non-degenerate member of the strawman §3.7 [`iterate-while`](./iterate-while.md) family (carry = field-state + step counter; `iterate_while_pure` with a step-count predicate, the [`chebyshev`](./chebyshev.md) route — NO new iteration primitive). | Concepts: `state-stratification` (`op` captured once at `TimeOperator` construction; `TimeState` the persistent carry), `solve-monad`, `sequential-obstruction` (the outer time sweep cannot reorder — each step's input is the prior step's output; AND the per-step `time_step_op` body is an **opaque MFEM `ODESolver` step**, `timeoperator.cpp:410`). L4 rows: [`iterate-while`](./iterate-while.md) (the fold combinator, carry-threading non-degenerate form); contrast-sibling [`solve_family`](./solve_family.md). Speculative rough-in operators: `time_step_op` (one opaque ODE step), `TimeState` (the field-state carry). | L1>L0 (eventual): the explicit `for (int step ...)` time sweep threading `sol` in place per `transientsolver.cpp:77-104`, with the per-step body a **role-naming wrapper over the opaque MFEM-integrator step** (the `eigsolve` opaque-library shape, NOT a Palace-authored loop) — theme TBD when the L4 entry lands. | `rough-in` (thread-opener; cycle-057 D4 — observation-first sketch from 1 witness, transient `transientsolver.cpp:24-114` + `timeoperator.cpp:300-413`; NOT firm — single witness, per the `disciplined-cross-pipeline-combinator-mining-gate` ≥2-witness bar; promotion = a 2nd fold-witness (the `SweepAdaptive` PROM candidate, OQ) OR a downstream transient pull. Genuinely-new vocabulary = the opaque `time_step_op` + the uniform `[Time]` schedule; the fold combinator reuses `iterate_while_pure`) |
```

```edit:book/src/L4/index.md
[Append one frontier bullet to the §"Active frontier" list (after the `solve_family` superset bullet at :61, before the `L4/orthogonalize` bullet at :62):]

- `fold_solve` / `time_step_fold` *(rough-in thread-opener; cycle-057 D4)* — the transient pipeline's **state-threaded fold** outer-driver, the fold-counterpart of [`solve_family`](./solve_family.md)'s independent map. Distilled from the transient driver's persistent-`sol`-threading time sweep (`transientsolver.cpp:93` → `timeoperator.cpp:410` `ode->Step(sol, t, dt)` advances `sol` in place, each step's input = the prior step's output → a genuine `foldl`, NOT a `map`). This **answers the `index.md:61` fold-vs-map question for transient: fold** — so transient does NOT join the `solve_family` map family (it is the §3.7 carry-threading sibling). Held at rough-in (1 witness; per-step body is an opaque MFEM `ODESolver` step — the `eigsolve` opaque-library shape). The shared parent of `solve_family` (map) + `fold_solve` (fold) is the strawman §3.7 `iterate_while` family itself; no third parent abstraction is warranted (OQ for the batch-17 meta-phase). Thread continues across batch-18; promotion gated on a 2nd fold-witness (the cycle-056 D1 `SweepAdaptive` PROM candidate) or a downstream transient pull.
```

## Open questions / caveats

- **`fold-solve-solve-family-share-iterate-while-parent`** (NEW; surfaced for the batch-17 meta-phase) — `solve_family` (map) and `fold_solve` (fold) are the two §3.7 `iterate_while`-family specializations distinguished by whether the step carries state (a map is a fold whose step ignores the accumulator). Recommended ratification: the **strawman §3.7 family IS the shared parent** — do NOT author a third combinator as a parent abstraction; both are §3.7-family entries, the map-vs-fold distinction is the load-bearing axis. This is the dispatch-scope's "whether fold_solve and solve_family share a parent abstraction" question; recommend resolving it as "yes — §3.7 itself — no new parent needed."

- **`fold-solve-second-witness-gate`** (NEW; carry-forward to batch-18) — `fold_solve` is a **1-of-1 witness** (transient only), below the `disciplined-cross-pipeline-combinator-mining-gate` ≥2-witness bar; this is why the thread-opener authors a rough-in dep-map row, not a firm L4 entry. The cycle-056 D1 finding already named the **2nd-witness candidate**: `DrivenSolver::SweepAdaptive` (`drivensolver.cpp:231+`, the PROM/adaptive path) may **fold a reduced-order-model state** (a 2nd fold-witness, joining `fold_solve`) rather than present a 2nd operator-varying map. A cheap batch-18 probe of `SweepAdaptive` could meet the gate and license the firm L4 `fold_solve` entry. (Already partly recorded at `open-questions.md:910`; this OQ ties it to the `fold_solve` promotion specifically.)

- **`time-step-op-opaque-mfem-integrator-boundary`** (NEW; upstream-behavior flag) — the per-step `time_step_op` body bottoms out in `ode->Step(sol, t, dt)` → an MFEM/SUNDIALS-owned `mfem::ODESolver` (`timeoperator.hpp:37`; GeneralizedAlpha/SDIRK23/ARKODE/CVODE, `timeoperator.cpp:314-389`). Palace owns the outer time sweep + the `sol`-threading but NOT the single integration step. The eventual lowering is therefore a **role-naming wrapper over an opaque-library obstruction marker** on the per-step body — the `eigsolve` opaque-library shape (`obstruction (opaque-library-ownership)` sub-kind), NOT a Palace-authored loop to render. If the L4 `fold_solve` entry needs the integrator's per-step semantics (e.g. the implicit-solve inside SDIRK23), that is **upstream MFEM behavior** — log as an upstream OQ at that point, do not localize into Palace. Cite Palace's *call* (`timeoperator.cpp:410`), not MFEM's internals.

- **MPI / Par* (single-rank, flagged once)** — the transient driver threads `Mpi::Print` / `space_op.GetComm()` (`transientsolver.cpp:42`, `:101`) and the field vectors are MFEM `Par*`-backed; per project scope (CLAUDE.md §Scope), these are read as single-rank equivalents. The `linalg::Norml2(space_op.GetComm(), E)` (`:101`) is the single-rank norm. No multi-rank distribution in the L4 sketch. Flagged here once.

- **`E`/`B`-as-views-into-`sol` aliasing** (refinement caveat for the eventual L4 entry) — `E` and `B` are `MakeRef` windows into the single backing `sol` (`timeoperator.cpp:307-308`), so the `TimeState` carry could be modeled as either `{ sol }` (with `E`/`B` derived views) or `{ sol, E, B }` (views exposed). The postprocess reads `E`/`B` (`transientsolver.cpp:98-99`), which are windows on the same `sol` the integrator advanced. Whether to expose the views or keep them derived (a `derived-view-hoisting` decision) is a refinement question for whoever lands the firm L4 entry; not resolved by this thread-opener.

- **Caveat: rough-in row uses plain-text name, no SUMMARY entry** — per the missing-anchor convention (`rough-in-rows-must-be-plain-text-when-anchor-missing`), the dep-map row names `fold_solve` in plain text (no live link, no anchor file). No `SUMMARY.md` chapter entry is proposed (there is no chapter file). When a later dispatch lands the firm L4 `fold_solve.md` entry, that dispatch upgrades the row to a live link and adds the SUMMARY entry.
