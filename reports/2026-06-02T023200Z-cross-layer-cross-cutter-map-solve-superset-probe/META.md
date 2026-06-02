---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T024500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T030000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of cross-layer observation — map_solve superset shape-classification (fold-vs-map GUARDED)

## Critique

### Checks run

**citation-validity — warning.** `citecheck.py --scan` clears all 16 citations on bounds + path-hygiene (`16 ok, 0 failing`). Anchor-checking the load-bearing pinpoints, however, surfaces a **systematic +1 off-by-one in the `drivensolver.cpp` single-line pinpoints**: `--anchor 'SetOperators'` on `drivensolver.cpp:179` reports the literal `ksp.SetOperators(*A, *P)` is actually at line **180**; `--anchor 'GetExtraSystemMatrix'` on `:174` reports `A2 = ...GetExtraSystemMatrix` is actually at **175**; and the OQ pinpoint `drivensolver.cpp:230` for `SweepAdaptive` resolves to **231**. Codemap `read_range(172-181)` confirms: A2/GetExtraSystemMatrix at 175, A/GetSystemMatrix at 176-177, SetOperators at 180. The cited *ranges* mask the drift where they span it (`175-176` catches GetSystemMatrix at 176; `194-196` catches GetExcitationVector at 194 — both `ok`), but the bare single-line cites (`:174`, `:179`, `:230`) each point one line short of their anchor. The drift is uniform (cited = actual − 1), small, and the surrounding prose is faithful to the source, so the *finding* is unaffected; this is a `warning`, not a `fail`. Note: the OQ's `:230+` is an open-ended region pointer so the `SweepAdaptive` symbol at 231 is arguably "in range," but the precise call line is 231. All non-`drivensolver.cpp` pinpoints are clean: `transientsolver.cpp:93` (Step), `timeoperator.cpp:407-413` (Step → ode->Step), `eigensolver.cpp:367` + `:405` (Solve), `eigensolver.cpp:177-193` (SetOperators) all anchor-verify `ok`. (No `verified_against:` block in this report — round-trip sub-check N/A.)

**surface-or-evidence — pass.** This is an observation-only probe (coverage gap / negative result), not a refinement of an existing operator/theme. It proposes NO surface change (explicitly "do NOT author `map_solve.md`") and authors no rotation_claim. The surface-or-evidence check targets refinement-shaped proposals; not applicable to this report-kind, and the report correctly stays observation-only with no book mutation.

**rotation-quality — pass.** No algebraic/structural rotation is asserted as a landed claim. The recorded superset shape (`map_solve` as the operator-varying generalization of `solve_family`, with `solve_family = map_solve (const A) (const P)`) is explicitly recorded as a *candidate shape only — NOT authored, NOT promoted* (report L114). The specialization relationship stated (solve_family ⊂ map_solve via const-operator) is genuine abstraction, not a 1:1 rename, but it is deferred not claimed. Not applicable as a landed rotation; the deferral is correct.

**variant-axis-coverage — pass.** This check's concern (hidden variant branches folded silently) is exactly inverted-and-honored here: per the gate skill step 2, the report classifies every break-witness as a SCOPE BOUNDARY rather than a variant axis — transient is explicitly held OUT of the map family as a distinct fold combinator (`fold_solve`), not absorbed as a variant of `map_solve`; eigenmode is held out as opaque-library. The SweepAdaptive branch is named as DEFERRED (not silently claimed as covered) with the correct fold-vs-map flag. No hidden branches.

**cross-reference-integrity — pass.** No `[link]` references, no proposed-changes block, no chapter status claim, no SUMMARY.md row (observation-only, no book mutation). The build-readiness firm-body-inside-fence guard is N/A (no fence, no firm claim). Referenced precedents (`solve_family` cycle-054/055; `eigsolve` L3 `partial-obstruction` cycle-024; `obstruction (opaque-library-ownership)`) are real and correctly characterized. The skill `disciplined-cross-pipeline-combinator-mining-gate` resolves on disk.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (this is a cross-pipeline L2/L3 shape-classification probe, not a lowering theme). The prose discusses the driver-tier solve shape and an L3 sequential-obstruction on the transient outer sweep — consistent with the scope line. Not applicable as an edge-labeled lowering.

**plan-kind-consistency — pass.** Declared as "Coverage gap (negative result)" observation; content shape matches exactly — a witness-count tally below the authoring gate, a verdict to defer, and a recorded-but-unpromoted candidate shape. No firm/rough-in placeholders masquerading as a different kind. The "do not author" verdict + spine-finding record is the correct observation-kind shape.

**skill-uptake-survey — pass.** The report cites `skills/disciplined-cross-pipeline-combinator-mining-gate` (L31, L126) and exhibits all four of its procedure points: (1) ≥2-witness floor applied (1 map witness < 2 → defer); (2) break-witnesses classified as scope boundaries (transient=fold, eigenmode=opaque); (3) the deferred SweepAdaptive pipeline named with an explicit fold-vs-map flag; (4) layer/propagation note (the un-map-able transient surface recorded as a future `fold_solve`/`time_step_fold`, not forced). Per the skill's own critic clause, citation + four-points-present = `pass`.

### Verification of the load-bearing call (fold-vs-map)

The crux is sound and source-confirmed:
- **Driven = operator-varying MAP — confirmed.** `read_range(172-181)`: `A2/GetExtraSystemMatrix` (175), `A = GetSystemMatrix(.., 1i*omega, -omega*omega..)` (176-177), `P = GetPreconditionerMatrix` (178-179), `ksp.SetOperators(*A, *P)` (180) — operator assembled from ω and bound INSIDE the per-frequency loop. `GetExcitationVector(.., omega, RHS)` (194) + `ksp.Mult(RHS, E)` (196): `E` overwritten per iteration; next input is a pure function of the index ω, not of prior `E`. Members independent → map. Correct. (The cited lines are correct in substance; only the integer pinpoints drift +1 — see citation-validity.)
- **Transient = state-threaded FOLD — confirmed, and the guard fires correctly.** `timeoperator.cpp:407-413`: `Step` calls `ode->Step(sol, t, dt)` where `sol` is a persistent member; `Init()` (398-405) sets `sol = 0.0` once. `transientsolver.cpp:77-110`: step 0 calls `Init()`, every later step calls `time_op.Step(t, delta_t)` (94) which advances the SAME `sol` in place. Each step's input = prior step's output → genuine fold, NOT a map. Holding it out of `map_solve` is exactly the step-3 over-unification guard — correct and load-bearing.
- **Eigenmode = single opaque solve — confirmed.** `eigensolver.cpp:367` `int num_conv = eigen->Solve()` — one opaque library call; `:405` is a *second* `Solve()` only on the HYBRID quasi-Newton refine branch (2-stage opaque sequence, not a family map/fold). `SetOperators` bound once at 177-193 before the solve, not inside a sweep. Neither map nor fold at driver tier. Correct.

Witness count is therefore correct: driven = 1 operator-varying-map witness; transient = fold (not a witness); eigenmode = neither → **1 < 2 gate → defer is the correct, disciplined outcome.** The spine finding (record the un-map-able transient as a future `fold_solve`, not forced) is legitimate and aligned with the redirect ("what a solver can't cleanly say is a finding about the spine"). The SweepAdaptive OQ is a legitimate, honestly-scoped second-witness watch — correctly flagged as a cheap follow-up, not enacted. No book mutation: confirmed (no proposed-changes block; report L143-144 states observation-only).

### Issues found

1. **Citation off-by-one (+1) in `drivensolver.cpp` single-line pinpoints — `citation-validity: warning`.** Three pinpoints point one line short of their stated symbol:
   - "Specific finding / Driven" §L39-40 and Supporting-evidence L118: `drivensolver.cpp:174` for `A2 = ...GetExtraSystemMatrix` — actual line **175**.
   - "Specific finding / Driven" §L41 and Supporting-evidence L118: `drivensolver.cpp:179` for `ksp.SetOperators(*A, *P)` — actual line **180**.
   - "Open questions" §L129 and the task's SweepAdaptive OQ: `drivensolver.cpp:230` for `SweepAdaptive` — actual line **231** (the `:230+` open-ended form softens this, but the precise call is 231).
   Severity: low. The drift is uniform (cited = actual − 1), the spanning ranges (`175-176`, `194-196`) still capture their anchors, and the prose semantics are faithful. The finding (fold-vs-map classification, witness count, verdict) is entirely unaffected. Candidate repair: bump the three bare pinpoints by +1 (174→175, 179→180, 230→231); optionally tighten `175-176`→`176-177` for the `GetSystemMatrix` `A` assignment if exactness is wanted.

2. **(Informational, not a defect) The recorded `map_solve` candidate shape is correctly un-promoted.** The fenced Haskell shape at L105-113 is a recorded candidate, explicitly NOT authored/promoted (L114). No issue — noting only that if a future cycle lands the SweepAdaptive 2nd witness, the rotation-quality check should re-run on the then-real `solve_family ⊂ map_solve` abstraction (it is a genuine generalization, not a rename).

This report is an honest fold-vs-map classification and a disciplined sub-gate defer — the CORRECT outcome. The single warning is a small, uniform, finding-immaterial citation drift confined to the driven-solver pinpoints.

---

## Repair

### Fixes attempted

- **Finding**: Uniform +1 off-by-one in the three `drivensolver.cpp` single-line pinpoints (citation-validity warning; `citecheck --anchor` caught it where spanning ranges masked it).
  - **Decision**: repaired
  - **Action**: Bumped each bare pinpoint by +1 in `CYCLE.md` after codemap `read_range` re-verification (`palace/drivers/drivensolver.cpp`; line 172 = `omega = omega_sample[omega_i]` anchors the loop body):
    - §"Specific finding / Driven": `A2 = GetExtraSystemMatrix` `:174`→`:175` (verified at 175); the `GetSystemMatrix` `A` assignment span `175-176`→`176-177` (verified `A = GetSystemMatrix(...)` spans 176-177); `ksp.SetOperators(*A, *P)` `:179`→`:180` (verified at 180).
    - §"Supporting evidence": driven operator-assembly span `:169-179`→`:170-180` (aligned to the corrected pinpoints; the prior range trailed by 1 at both ends).
    - §"Open questions": `DrivenSolver::SweepAdaptive` `:230+`→`:231+` (verified the function definition begins at 231).
    - The load-bearing fold-vs-map classification (driven = operator-varying map, transient = state-threaded fold, eigenmode = opaque single solve) was NOT touched — the critic verified it SOUND and source-confirmed.

- **Finding** (telemetry, not a defect): skill-uptake-survey — the critic noted the report cites and exhibits all four points of `disciplined-cross-pipeline-combinator-mining-gate`.
  - **Decision**: not-needed — `pass` from the critic; recorded here only as telemetry that the gate skill was exercised correctly (1-witness defer, scope-boundary classification of break-witnesses, named deferred pipeline, spine-finding propagation note).

### Unrepairable findings
None. The single warning was a mechanical, codemap-verifiable +1 pinpoint drift fully within repair authority. All other checks passed.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

- **NO book mutation.** D1's verdict is explicitly "do NOT author `map_solve.md`" (1 operator-varying-map witness < 2-witness gate). There is no proposed-changes block; nothing lands in `book/`. The integrator-per-report pass on D1 applies zero artifact edits and only promotes the OQs below.
- **Promote D1's open questions** to the plan / OQ ledger:
  1. **Spine finding** — record the un-map-able transient state-threaded surface as a future `fold_solve` / `time_step_fold` combinator (distinct from the `map_solve` family; outer time sweep is a sequential-obstruction at L3). This is the redirect's "what a solver can't cleanly say is a finding about the spine" — observation-first; authoring is a separate combinator-miner dispatch.
  2. **`DrivenSolver::SweepAdaptive` 2nd-witness probe** (`drivensolver.cpp:231+`, PROM/adaptive path) — cheap follow-up: does it present a second operator-varying-map instance (which would meet the ≥2 gate and license authoring `map_solve.md`), or does it fold a reduced-order-model state (making it a fold, not a 2nd map witness)? Batch-18 candidate.
