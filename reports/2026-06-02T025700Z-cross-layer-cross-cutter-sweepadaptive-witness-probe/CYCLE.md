---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T03:03:38Z
scope: L_n↔L_{n+1} cross-cut — SweepAdaptive fold-vs-map witness probe for the map_solve superset
status: pending
integrated_at: 2026-06-02T050000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-057 (D3). OBSERVATION-ONLY (no book mutation). SweepAdaptive is a reduced-order-model FOLD (double state-thread: sample-location via FindMaxError, sample-result via UpdatePROM Gram-Schmidt-append; online fast-sweep maps over the FROZEN ROM, NOT operator-varying) → NOT a 2nd map_solve witness → map_solve superset STAYS deferred at 1 witness (standard Sweep, c056 D1); SweepAdaptive + transient both in the FOLD family → confirms the two-combinator (MAP/FOLD) factoring. 1 OQ promoted (sweepadaptive-is-rom-fold-map-solve-stays-single-witness, cross-references c056 D1 + c057 D4)."
---

# CYCLE: Cross-layer observation — sweepadaptive-is-a-rom-fold-not-a-map-witness

## Summary

I probed `DrivenSolver::SweepAdaptive` (`palace/drivers/drivensolver.cpp:231-479`) to decide whether it is a **2nd operator-varying-MAP witness** for the deferred `map_solve` superset (which would meet the 2-witness gate) or a **reduced-order-model FOLD** (which would not). The call is unambiguous and load-bearing: **SweepAdaptive is a FOLD, not a map.** The offline-phase greedy-basis construction threads state sample→sample — each adaptive sample's location `omega_star` is *chosen by an error estimator over the accumulated reduced basis* (`prom_op.FindMaxError(...)` at `:389`), and each solve's result is *appended into that basis* (`prom_op.UpdatePROM(...)`/`UpdateMRI(...)` at `:319-321`, body `palace/models/romoperator.cpp:596+`). Sample `n+1` cannot be computed without the basis state produced by samples `0..n`. This is the canonical greedy reduced-order-model fold. **The `map_solve` superset therefore stays DEFERRED at 1 witness** (the standard `DrivenSolver::Sweep`, cycle-056 D1). SweepAdaptive joins the **FOLD family** alongside transient time-stepping — a second `fold_solve`-family witness — confirming the two-combinator-family factoring (independent-MAP `solve_family` vs. sequential-FOLD).

## Observation kind

**Coverage gap** (resolved-negative): the probed candidate does NOT close the gap it was probed for. The 2nd-witness gate for the `map_solve` superset is NOT met by SweepAdaptive; the gap remains open. Secondarily this is a **vocabulary/family-classification finding**: SweepAdaptive is correctly classified into the existing FOLD family, not the MAP family.

## Specific finding

### The structure has THREE loops; the load-bearing one is the offline greedy fold

`SweepAdaptive` (`drivensolver.cpp:231-479`) has two phases:

**Offline phase — PROM construction (the FOLD).** Per excitation (`:344-461`):

1. **Seed samples** (`:366-376`): solve the HDM at the explicit `prom_indices` frequencies, each `prom_op.SolveHDM(...)` followed by `UpdatePROM(...)` which *adds* the solution to the reduced basis `V`. Even this seed loop threads state — each `UpdatePROM` grows `V`.

2. **Greedy adaptive loop** (`:383-410`):
   ```
   double omega_star = prom_op.FindMaxError(excitation_idx)[0];   // :389  — reads accumulated basis
   prom_op.SolveHDM(excitation_idx, omega_star, E);               // :392  — HDM solve at chosen point
   prom_op.SolvePROM(excitation_idx, omega_star, Eh);             // :393  — current-basis PROM solve
   ...
   memory = max_errors.back() < offline_tol ? memory + 1 : 0;     // :398  — convergence state
   UpdatePROM(excitation_idx, omega_star, counter_rom_sample);    // :406  — appends to basis
   ```
   The loop bound itself is state-dependent: `it < max_size_per_excitation && memory < convergence_memory` (`:385`), where `memory` is the running count of consecutive sub-tolerance samples.

The state-threading is **double**, and both directions are fatal to the map reading:

- **Sample LOCATION is state-threaded.** `omega_star` is `prom_op.FindMaxError(excitation_idx)[0]` — `MinimalRationalInterpolation::FindMaxError` (`palace/models/romoperator.cpp:236+`) returns `argmax_z ||u(z) - V y(z)||` computed as `argmin_z |Q(z)|`, where `Q` is the *denominator of the barycentric interpolation built from the already-sampled points* (`:236-241`; `MFEM_VERIFY(S >= 2, "Maximum error can only be found once two sample points have been added...")` at `:243-244`). The next frequency to sample is a pure function of the accumulated sample set. This is the greedy adaptive-sampling state thread.
- **Sample RESULT is state-threaded.** `UpdatePROM` (`drivensolver.cpp:317-340`; `romoperator.cpp:596-693`) appends the HDM solution to basis `V` via Gram–Schmidt orthogonalization against the existing columns (`OrthogonalizeColumn(... V, v, ... dim_V ...)`, `romoperator.cpp:634+`). The basis grows; every subsequent `FindMaxError` and `SolvePROM` reads the grown basis.

**Online phase — fast frequency sweep (a map, but degenerate).** After the basis is frozen, the online loop (`:432-475`) does `prom_op.SolvePROM(excitation_idx, omega, E)` (`:451`) independently per frequency. This *is* an independent map — but it is a map over the **already-constructed reduced operator**, not over the high-dimensional Palace operator family, and it carries none of the `SetOperators`-per-element shape that made the standard `Sweep` an operator-varying map. It is the cheap projected-system solve, structurally the `solve_family`-over-a-fixed-small-operator inner shape, NOT a new operator-varying-map witness. The expensive, characteristic work of SweepAdaptive is the offline fold.

### Verdict: reduced-order-model FOLD

Per the `disciplined-cross-pipeline-combinator-mining-gate` step-3 fold-vs-map check, SweepAdaptive's load-bearing offline phase **threads state between elements** (both the next sample location and the accumulated basis). Folding it into a map would falsely assert the concatenation-homomorphism / independence law: it does NOT hold — sample `n+1`'s very *existence and location* depend on samples `0..n`. SweepAdaptive is a **FOLD** (greedy reduced-order-model construction).

Consequences:
- The **`map_solve` superset stays DEFERRED at 1 witness** (`DrivenSolver::Sweep`, c056 D1). SweepAdaptive does NOT meet the 2-witness gate.
- SweepAdaptive is a **2nd member of the FOLD family** (the `fold_solve` / `iterate_while`-shaped family), alongside transient time-stepping. This **confirms the two-combinator-family factoring**: an independent-MAP `solve_family` (with the deferred `map_solve` operator-varying superset) vs. a sequential-FOLD family (transient time-step; greedy ROM basis construction). SweepAdaptive's fold is a *greedy-with-error-driven-termination* shape — a richer fold than transient's fixed-step march (the loop bound and the per-step input are both state-derived), which is itself a useful sub-distinction for a future fold-family miner.

## Recommendation

- **Defer the `map_solve` superset** — record this negative result; the superset stays at 1 witness. Do NOT author it. A genuine 2nd operator-varying-map witness must come from elsewhere (candidate: a magnetostatic or electrostatic multi-RHS/multi-operator sweep, if any exists — unprobed).
- **Record SweepAdaptive in the FOLD family** for a future fold-family combinator-miner (batch-18+), noting it as the *greedy / error-terminated* fold sub-shape distinct from transient's fixed-march fold. Observation-first; the authoring is a separate dispatch.
- No `book/` edit is implied by this dispatch (observation-only, negative result). No proposed-changes block.

## Supporting evidence

- `palace/drivers/drivensolver.cpp:231-479` — `DrivenSolver::SweepAdaptive` full body.
  - `:240-244` — PROM params (`adaptive_tol`, `adaptive_memory`, `adaptive_max_size`, `prom_indices`).
  - `:317-340` — `UpdatePROM` lambda: `prom_op.UpdatePROM(E, ...)` + `prom_op.UpdateMRI(...)` append solution to basis.
  - `:366-376` — seed-sample loop (state-threading via `UpdatePROM`).
  - `:383-410` — **greedy adaptive fold**: `:389` `FindMaxError` (location from accumulated state), `:392-393` HDM+PROM solve, `:398` `memory` convergence state, `:406` `UpdatePROM`. Loop bound `:385` depends on running `memory`.
  - `:432-475` — online fast-sweep map over the *frozen* reduced operator (`:451` `SolvePROM`); degenerate w.r.t. the operator-varying-map question.
- `palace/models/romoperator.cpp:236-244` — `MinimalRationalInterpolation::FindMaxError`: next sample = `argmin_z |Q(z)|` over barycentric interpolant of *existing* samples; `MFEM_VERIFY(S >= 2, ...)` requires ≥2 prior samples.
- `palace/models/romoperator.cpp:596-693` — `RomOperator::UpdatePROM`: appends solution to basis `V` via `OrthogonalizeColumn(... V, v, ... dim_V ...)` (`:634+`) — basis grows monotonically across samples.
- Comparison witness (not re-read this dispatch): standard `DrivenSolver::Sweep` operator-varying MAP, per cycle-056 D1 (`SetOperators` inside the per-frequency loop, members independent) — the sole current `map_solve`-superset witness.
- Test L0-evidence: `test/unit/test-romoperator.cpp:95,121` exercise `FindMaxError` over a populated MRI (`CHECK_THROWS(mri_1.FindMaxError(1))` confirms the ≥2-sample-state precondition; `mri_1.FindMaxError(5)` after population) — corroborates that `FindMaxError` is a function of accumulated sample state.

## Open questions / caveats

- **OQ (genuine 2nd map witness still unfound).** The `map_solve` operator-varying-map superset now has 1 confirmed witness (`Sweep`) and 1 confirmed NON-witness (`SweepAdaptive` = fold). No remaining driven-pipeline candidate is an operator-varying map. A 2nd witness, if it exists, must come from another pipeline's multi-operator/multi-RHS solve. If none surfaces, the superset may be a **single-witness spine-coverage finding permanently** (record `Sweep` as operator-varying but do not generalize). Suggest the batch-18 planner weigh whether to keep probing or to retire the superset as single-witness.
- **Caveat (online phase is a map, but the wrong kind).** The online fast-sweep loop IS an independent map over frequencies, but over the *frozen reduced* operator — it does not exhibit the operator-varying / `SetOperators`-per-element shape that defines the `map_solve` superset. I have NOT counted it as a witness; treating it as one would be a step-2 scope-boundary violation (different operator-class). Flagging explicitly so a later miner does not mis-read the online loop as the 2nd witness.
- **Caveat (fold sub-shape).** SweepAdaptive's fold has a state-derived loop bound AND state-derived per-step input (`omega_star`), making it a *greedy / error-terminated* fold — strictly richer than transient's fixed-step march. A future fold-family combinator should not assume transient's simpler `iterate_while`-with-fixed-schedule shape covers it. Recorded as a sub-distinction, not resolved here.
- **MPI/Par* single-rank.** `space_op.GetComm()`, `linalg::Norml2(comm, ...)`, `Mpi::Print` read as single-rank per project scope; the fold/map structure is rank-independent (the state-thread is in the basis, not the comm).
