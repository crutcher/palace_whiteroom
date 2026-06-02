---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T023200Z
scope: L2/L3 cross-cut — map_solve superset shape-classification probe (driven/transient/eigenmode vs solve_family)
status: pending
integrated_at: 2026-06-02T040000Z
integration_commit: a91f0bc
integration_notes: "cycle-056 D1 (OBSERVATION-ONLY, no book mutation). Verdict applied as observation: do NOT author map_solve.md. Three-way solver-family shape classification — driven = operator-varying MAP (1 witness, drivensolver.cpp uniform Sweep with SetOperators-inside-loop); transient = state-threaded FOLD → a DISTINCT future fold_solve/time_step_fold combinator (SPINE FINDING, NOT a 2nd map witness — the fold-vs-map guard correctly refused to over-unify); eigenmode = opaque single solve. With 1 operator-varying-map witness, the map_solve superset is DEFERRED below the 2-witness authoring gate (skills/disciplined-cross-pipeline-combinator-mining-gate); the recorded map_solve Haskell candidate stays unpromoted. DrivenSolver::SweepAdaptive (drivensolver.cpp:231+) is the cheap 2nd-witness probe (batch-18 candidate). 2 OQs promoted to scaffolding/open-questions.md. NO book mutation, NO count delta."
---

# CYCLE: Cross-layer observation — map_solve superset shape-classification (fold-vs-map GUARDED)

## Summary
Probed whether the remaining 3 Palace solver pipelines (driven, transient, eigenmode) witness a
general `map_solve_over_(operator,rhs)_family` SUPERSET of the cycle-054/055 fixed-operator
`solve_family` combinator. Result: the superset has only **1** confirming witness. **Driven** is a
genuine operator-varying map (`SetOperators` is inside the per-frequency loop; the operator `A(ω)` is
a pure function of the family index ω, and the members are independent — no field-state threaded
member→member). **Transient** is a **state-threaded FOLD, NOT a map** — `time_op.Step` advances a
persistent solution vector `sol` step→step, so each step's input is the previous step's output; it
does NOT join the `map_solve` family. **Eigenmode** is neither map nor fold at the driver level — it
is a single opaque-library `eigen->Solve()` over the whole spectral problem (no family iteration in
Palace's own code). Verdict: **do NOT author `map_solve.md` this cycle** (1 map witness < 2). Record
the shape-classification; the un-map-able transient surface is a SPINE FINDING (a distinct future
`fold_solve` / `time_step_fold` combinator the spine will eventually need), not a forced land.

## Observation kind
**Coverage gap (negative result)** — a hypothesized L2 combinator (`map_solve` superset) lacks the
≥2-witness floor under the disciplined-cross-pipeline-combinator-mining-gate, AND the probe surfaces a
distinct, separately-shaped combinator need (`fold_solve`) that the transient pipeline witnesses.

## Specific finding

Per `skills/disciplined-cross-pipeline-combinator-mining-gate`: the load-bearing call is whether each
pipeline's per-member solve is **independent** (map: `solve(A_i, rhs_i)` with no state thread) or
**stateful** (fold: member output feeds member input). Evidence per pipeline:

### Driven → OPERATOR-VARYING MAP (joins a map_solve superset; 1 witness)
`palace/drivers/drivensolver.cpp` frequency loop:
- The per-frequency operator is assembled FROM ω **inside** the loop:
  `auto A = space_op.GetSystemMatrix(1.0+0.0i, 1i*omega, -omega*omega+0.0i, K.get(), C.get(), M.get(), A2.get())`
  — `drivensolver.cpp:176-177`, with `A2 = space_op.GetExtraSystemMatrix<ComplexOperator>(omega, ...)`
  at `drivensolver.cpp:175`.
- `ksp.SetOperators(*A, *P)` is **inside** the loop — `drivensolver.cpp:180`. The operator VARIES per
  step (operator-varying map), confirming the probe hypothesis.
- The RHS also varies per ω: `space_op.GetExcitationVector(excitation_idx, omega, RHS)` —
  `drivensolver.cpp:194`.
- The solve is `ksp.Mult(RHS, E)` — `drivensolver.cpp:196`. The output `E` is **overwritten** each
  iteration; the next iteration's input (`A(ω_{i+1})`, `RHS(ω_{i+1})`) is a function of the index only,
  **not** of the previous `E`. Members are INDEPENDENT → map, not fold. (The `indicator`
  ErrorIndicator and the paraview collection accumulate as a side-channel reduction, but that is a
  post-processing fold over outputs, NOT a state thread into the next solve's input.)
- Shape: `map (\ω -> ksp_solve(A(ω), P(ω), rhs(ω))) omega_sample` — an **operator-varying map**:
  superset of `solve_family` (which fixes the operator and maps over rhs only). The outer loop over
  `port_excitations` (`drivensolver.cpp:153`) is a second independent map dimension (excitation index),
  reinforcing the map shape.

### Transient → STATE-THREADED FOLD (does NOT join map_solve; distinct combinator)
`palace/drivers/transientsolver.cpp` main time-integration loop (`:77-110`):
- `time_op.Step(t, delta_t)` — `transientsolver.cpp:93`.
- `TimeOperator::Step` is `palace/models/timeoperator.cpp:407-413`:
  `void TimeOperator::Step(double &t, double &dt) { double dt_input = dt; ode->Step(sol, t, dt); dt = dt_input; }`
  — it calls `ode->Step(sol, t, dt)` where **`sol` is a persistent member vector** advanced in place.
  Step 0 sets initial conditions (`time_op.Init()` → `sol = 0.0`, `timeoperator.cpp:398-405`), and
  every subsequent `Step` reads-and-overwrites the SAME `sol`. Each step's input depends on the
  previous step's output. This is a **stateful fold over time** (`fold (\sol -> ode_step sol) sol0
  [t_0..t_n]`), NOT a map. It does **not** join the `map_solve` family.
- This is the GUARD firing exactly as the dispatch anticipated: refusing to over-unify a fold into a
  map. The shape is `fold_solve` / `time_step_fold` — a distinct combinator (sequential-obstruction
  on the outer time sweep at L3).

### Eigenmode → SINGLE OPAQUE LIBRARY SOLVE (neither map nor fold at driver level)
`palace/drivers/eigensolver.cpp`:
- `int num_conv = eigen->Solve();` — `eigensolver.cpp:367` (and the HYBRID-refine variant
  `num_conv = eigen->Solve();` at `:405`). A **single** opaque library call (SLEPc EPS / quasi-Newton)
  over the whole generalized EVP. There is no family-of-solves iteration in Palace's own driver code —
  the iteration lives inside the library boundary (cf. CLAUDE.md `obstruction (opaque-library-ownership)`
  + the cycle-024 `eigsolve` L3 `partial-obstruction`). `SetOperators(*K, *C, *M, ...)` is called once
  before the solve (`eigensolver.cpp:177-193`), not inside a sweep. → does NOT join the map_solve family;
  it is not a map and not a fold at the driver tier.

### Witness count for the map_solve superset
| Pipeline | Operator per member | State threaded member→member? | Shape | Joins map_solve superset? |
|---|---|---|---|---|
| electrostatic | fixed (captured once) | no | fixed-operator map | already `solve_family` |
| magnetostatic | fixed (captured once) | no | fixed-operator map | already `solve_family` |
| driven | varies `A(ω)` per step | no (independent members) | operator-varying map | YES (1 witness) |
| transient | per-step `ode` op | **yes** (`sol` threaded) | state-threaded fold | NO — `fold_solve` |
| eigenmode | set once | n/a (single solve) | opaque library solve | NO |

Operator-varying-map confirming witnesses = **1** (driven). Floor for authoring = 2. **Not met.**

## Recommendation
- **Defer `map_solve.md` authoring** — the superset has 1 operator-varying-map witness (driven); below
  the ≥2 gate. Do NOT generalize `solve_family` into `map_solve` this cycle. (If batch-18 surfaces a
  second operator-varying-map witness — e.g. an adaptive frequency sweep or a parametric sweep reusing
  the same loop shape — re-open with the recorded shape below.)
- **Record the transient FOLD as a spine finding** (distinct future combinator). Recommendation for a
  later cycle: "Dispatch combinator-miner on the transient time-integration loop to characterize a
  `fold_solve` / `time_step_fold` combinator (state-threaded sequential fold; outer time sweep is a
  sequential-obstruction at L3)." This is observation-first — authoring is a separate dispatch, and the
  un-map-able surface is itself the finding (per the redirect: what a solver can't cleanly say is a
  finding about the spine).
- **Eigenmode**: no combinator action — it is opaque-library-owned at the driver tier (already covered
  by the `eigsolve` opaque-library / `partial-obstruction` precedents). Defer.

## Recorded superset shape (for a future cycle-057/batch-18 combinator-miner, IF a 2nd witness lands)
```
-- operator-varying map: superset of solve_family (which fixes A)
map_solve :: (i -> Operator) -> (i -> Operator) -> (i -> Rhs) -> [i] -> [Sol]
map_solve mkA mkP mkRhs family =
  map (\i -> ksp_solve (mkA i) (mkP i) (mkRhs i)) family
-- solve_family is the specialization mkA = const A, mkP = const P:
--   solve_family A P mkRhs family = map_solve (const A) (const P) mkRhs family
-- driven instantiates mkA = \ω -> GetSystemMatrix(.., 1i*ω, -ω²..), mkRhs = \ω -> GetExcitationVector(ω)
```
NOTE this is recorded as a candidate shape only — NOT authored, NOT promoted. The gate is unmet.

## Supporting evidence
- Driven operator-varying map: `palace/drivers/drivensolver.cpp:153` (excitation loop),
  `:170-180` (per-ω operator assembly + `SetOperators` inside loop), `:194-196` (per-ω RHS + solve).
- Transient state-threaded fold: `palace/drivers/transientsolver.cpp:77-110` (time loop, `Step` at `:93`);
  `palace/models/timeoperator.cpp:407-413` (`TimeOperator::Step` → `ode->Step(sol, ...)`, `sol` persistent);
  `:396-405` (`Init` sets `sol = 0.0` once).
- Eigenmode single opaque solve: `palace/drivers/eigensolver.cpp:177-193` (`SetOperators` once),
  `:367` + `:405` (`eigen->Solve()`).
- Existing fixed-operator combinator: `solve_family` (cycle-054/055; electrostatic + magnetostatic
  witnesses).
- Gate procedure: `skills/disciplined-cross-pipeline-combinator-mining-gate`.

## Open questions / caveats
- **OQ (map_solve 2nd-witness watch):** Does `DrivenSolver::SweepAdaptive` (`drivensolver.cpp:231+`, the
  PROM/adaptive path) present a SECOND operator-varying-map instance, or does it fold a reduced-order
  model state (which would make it a fold, not a 2nd map witness)? Not probed this cycle (out of scope;
  the dispatch named the uniform `Sweep` loop). Worth a cheap follow-up probe — if it is a clean second
  operator-varying-map it would meet the ≥2 gate and license authoring `map_solve.md`. Surfacing for the
  plan, not enacting.
- **Caveat (fold side-channels in driven):** the driven loop accumulates `indicator` (AddEstimate) and
  paraview output across iterations. These are post-processing reductions over independent solve OUTPUTS,
  not state threaded into the next solve's INPUT — they do not change the map classification of the solve
  core. The combinator boundary should be drawn around the `ksp.Mult` solve, with the estimate-reduction
  as a separate `fold`/`reduce` over outputs (a `map`-then-`reduce`, classic).
- **Caveat (eigenmode HYBRID branch):** the quasi-Newton refine at `eigensolver.cpp:383-407` calls
  `Solve()` a second time on a refined operator. This is a 2-stage opaque sequence, not a family map/fold;
  it does not change the eigenmode classification.
- This is an observation-only probe. NO `book/` mutation performed. No proposed-changes block (the verdict
  is "do not author"). The transient `fold_solve` finding is recorded for plan migration, not authored.
