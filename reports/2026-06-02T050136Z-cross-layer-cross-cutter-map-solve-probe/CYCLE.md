---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T05:01:36Z
scope: L4 cross-cut — map_solve 2nd-pipeline operator-varying-MAP probe (NON-driven)
status: pending
integrated_at: 2026-06-02T053505Z
integration_commit: f270ba5c4cdec17a20138d66470c423c5c38e001
integration_notes: |
  cycle-058 D3. OBSERVATION-ONLY (no book mutation; no proposed-changes block). Applied by integrator-per-report
  (staging row 3), housekept + committed by integrator-finalize. map_solve 2nd-pipeline probe → NON-DISCHARGE: the
  map_solve superset (operator-VARYING map for driven/transient) does NOT acquire a 2nd witness (consistent with the
  c057 D3 SweepAdaptive=ROM-FOLD finding — SweepAdaptive advances fold_solve, NOT map_solve). map_solve recorded as a
  PERMANENT single-witness spine-coverage finding (1 witness, std Sweep c056 D1), routed to the batch-18 meta-phase for
  formal close (retire-as-single-witness per the batch-17 meta-phase go-decision). The finding
  map-solve-second-pipeline-probe-NON-DISCHARGE was appended to scaffolding/open-questions.md by the dispatch agent.
  No count delta. Gate hits: n/a (no surface mutation).
---

# CYCLE: Cross-layer observation — map_solve stays single-witness (NON-DISCHARGE)

## Summary
I probed the NON-driven solver pipelines for a genuine 2nd operator-VARYING-MAP
witness that would license authoring `book/src/L4/map_solve.md` (the hypothetical
operator-varying-MAP superset of which `solve_family` is the `operator=const`
specialization). All non-driven family-sweep pipelines set their linear-solver
operator ONCE, BEFORE the sweep loop, and vary only the RHS per family-element —
i.e. they are fixed-operator MAP members of `solve_family`, not operator-varying.
The eigenmode pipeline sets its ksp operator once before a single opaque SLEPc EPS
solve (not a family map at all). The driven `Sweep` remains the SOLE
operator-varying-MAP witness (`SetOperators` rebuilt INSIDE the ω-loop). The probe
is a **non-discharge**: `map_solve` is recorded as a permanent single-witness
spine-coverage finding, routed to the batch-18 meta-phase for formal close.

## Observation kind
**Coverage gap** (negative result) — `map_solve` is a referenced/hypothetical L4
superset with exactly ONE positive witness across all 5 pipelines. Per the
`disciplined-cross-pipeline-combinator-mining-gate` skill (step 1), a single witness
is a SPINE-COVERAGE FINDING, not a mineable combinator; do NOT author from it. This
is the redirect's "what a solver can't cleanly say is a finding about the spine."

## Specific finding

Operator-set placement relative to the family-sweep loop, codemap-verified:

| Pipeline | `SetOperators` site | Relative to sweep loop | Per-element variation | Classification |
|---|---|---|---|---|
| **driven** `Sweep` | `drivensolver.cpp:180` (`ksp.SetOperators(*A,*P)`); `A` rebuilt at `:174-176` | **INSIDE** ω-loop (`:169`) | operator `A=(K+iωC−ω²M)` AND RHS | **operator-VARYING MAP** — the sole `map_solve` witness |
| **magnetostatic** | `magnetostaticsolver.cpp:36` (`ksp.SetOperators(*K,*K)`) | **BEFORE** surface-current loop (`:65`) | RHS only (`GetExcitationVector(idx,RHS)` `:76`); operator `K` FIXED | fixed-operator MAP member of `solve_family` |
| **electrostatic** | `electrostaticsolver.cpp:36` (`ksp.SetOperators(*K,*K)`) | **BEFORE** terminal loop (`:60`) | RHS only (`GetExcitationVector(idx,*K,V[step],RHS)` `:67`); operator `K` FIXED | fixed-operator MAP member of `solve_family` |
| **eigenmode** | `eigensolver.cpp:329` (`ksp->SetOperators(*A,*P)`) | single setup before one opaque EPS solve; `eigen->SetOperators` `:177-193` feeds the library | NOT a family map (single opaque SLEPc/library solve) | opaque-library-ownership, not a map at all |
| **transient** | (no driver-level `SetOperators`; time-stepper-owned) | — | state threaded step→step | **fold**, not a map (per batch-17 meta decision 3) |

Evidence detail:
- The driven loop assembles `A2`/`A`/`P` fresh per-ω (`drivensolver.cpp:174-179`)
  then `ksp.SetOperators(*A,*P)` at `:180`, before `ksp.Mult(RHS,E)` at `:198`. The
  operator is a function of the loop variable ω — genuinely operator-varying.
- Magnetostatic: `K = curlcurl_op.GetStiffnessMatrix()` (`:30`), `SetOperators(*K,*K)`
  at `:36`, then the boundary loop `for (const auto &[idx,data] : ...GetSurfaceCurrentOp())`
  at `:65` only re-forms `RHS` via `GetExcitationVector(idx,RHS)` (`:76`) and calls
  `ksp.Mult(RHS,A[step])` (`:77`). `K` is loop-invariant — fixed-operator.
- Electrostatic is structurally identical: `SetOperators(*K,*K)` at `:36`, terminal
  loop at `:60`, body re-forms RHS (`:67`) and `ksp.Mult` with fixed `K`.
- Eigenmode `ksp->SetOperators(*A,*P)` at `:329` is the ONE-TIME shift-invert
  preconditioner setup for the SLEPc EPS solve; the `eigen->SetOperators(...)` family
  at `:177-193` hands K/C/M to the opaque library — no per-element user-side map.

Gate (`disciplined-cross-pipeline-combinator-mining-gate`):
- **Step 1 (≥2 positive witnesses):** FAILS for operator-varying-MAP. Only 1
  positive witness (driven). The two non-driven family sweeps are positive witnesses
  of the FIXED-operator `solve_family`, NOT of the operator-varying superset.
- **Step 2 (break-witnesses are scope boundaries):** the non-driven sweeps are not
  break-witnesses of `solve_family`; they are its canonical members. The
  operator-varying driven case is the scope-boundary superset (correctly classified
  at c054 D1). No new break-witness surfaced.
- **Step 3 (deferred pipelines, fold-vs-map):** transient remains a FOLD (state
  threaded), not a 2nd map witness — folding it into `map_solve` would assert the
  concatenation-homomorphism independence law that time-stepping violates. Confirmed
  consistent with batch-17 meta decision 3. No unprobed pipeline remains.

## Recommendation
**Defer to batch-18 meta-phase for formal close.** Do NOT author `book/src/L4/map_solve.md`
(per batch-17 meta decision 3 and gate step 1). Record `map_solve` as a permanent
single-witness spine-coverage finding: the operator-varying-MAP shape is real (driven
`Sweep`) but has no cross-pipeline second witness, so it is NOT promoted to a mined L4
combinator. `solve_family` (the fixed-operator MAP, ≥2 witnesses: electrostatic +
magnetostatic) remains the firm cross-pipeline combinator; the driven case rides it as
the documented operator-varying SCOPE-BOUNDARY superset annotation, authored only IF a
2nd operator-varying witness ever surfaces (none exists in Palace's current 5-pipeline
feature set). This closes the `map_solve` 2nd-pipeline-probe thread opened batch-17.

## Supporting evidence
- `palace/drivers/drivensolver.cpp:160-205` — driven ω-loop; `SetOperators` at :180 INSIDE loop.
- `palace/drivers/magnetostaticsolver.cpp:28-100` — `SetOperators` :36 before loop :65; RHS-only body.
- `palace/drivers/electrostaticsolver.cpp:30-75` — `SetOperators` :36 before loop :60; RHS-only body.
- `palace/drivers/eigensolver.cpp:320-345` (ksp `:329`), `:177-193` (eigen family) — opaque EPS, single solve.
- `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` — gate steps 1–3 applied.
- batch-17 meta decision 3 (commit `3905649` / `26c8b3c`): `map_solve` stays at 1 witness
  unless a NON-driven operator-varying-MAP witness appears; SweepAdaptive/transient are folds;
  eigenmode is opaque single solve.

## Open questions / caveats
- This probe is over Palace's CURRENT feature set (5 pipelines). The redirect permits
  higher-form vocabulary to anticipate feature sets Palace hasn't implemented — but the
  no-witness-for-mining bar still holds: `map_solve` is not authored speculatively.
- The disposition is a meta-phase close, not a per-cycle book mutation. No `book/`
  proposed-changes block is emitted (observation-ONLY dispatch, per batch-17 meta decision 3).
