---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T05:18:47Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T05:31:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of L4>L3 theme — fold-solve-time-step-dissolution

## Critique

### Checks run

**citation-validity — pass.** `tools/citecheck/citecheck.py --scan` reports `17 ok, 0 failing (17 citations checked)` — all bounds + path-hygiene clean. I independently meaning-read the load-bearing pinpoints via codemap `read_range`:
- `timeoperator.cpp:410` = `ode->Step(sol, t, dt)` — CONFIRMED on-disk (this is the abstractor's flagged -2-drift-corrected anchor; the on-disk line is 410, and the §"opaque per-step sub-leaf" `TimeOperator::Step` body range `407-413` also matches: 407 = the `void TimeOperator::Step(double &t, double &dt)` signature, 413 = closing brace, 410 = the `ode->Step` forwarder). The drift-correction the report claims is real and correctly resolved.
- `timeoperator.cpp:312` = `op = std::make_unique<TimeDependentFirstOrderOperator>(...)` — CONFIRMED (the integrator-construction-once hoist; line 310 is the "Create ODE solver" comment).
- `transientsolver.cpp:33` = `TimeOperator time_op(iodata, space_op, dJdt_coef)`, `:35` = `delta_t = iodata.solver.transient.delta_t`, `:36` = `n_step = config::GetNumSteps(...)`, `:77` = `for (int step = 0; step < n_step; step++)`, `:89` = `time_op.Init()` (step==0 initial-conditions branch), `:93` = `time_op.Step(t, delta_t)` (the else/per-step branch), `:98` = `time_op.GetE()`, `:99` = `time_op.GetB()` — all CONFIRMED, and the prose's semantic reading of each (operator-hoist outside loop, seed-in-place vs per-step branch split, trajectory readout) matches the source exactly.
- `drivensolver.cpp:73` = the `adaptive ? SweepAdaptive : SweepUniform` dispatch, `:231` = `ErrorIndicator DrivenSolver::SweepAdaptive(...)`, `:384` = the `for (... && memory < convergence_memory; it++)` state-derived bound, `:389` = `omega_star = prom_op.FindMaxError(excitation_idx)[0]` — all CONFIRMED. The state-generated-schedule framing (loop bound is a state-derived predicate, per-step input drawn from accumulated error) is faithful to source.
No `verified_against:` fenced-YAML block is emitted (the §Verified-against here is prose, not a YAML round-trip payload), so that sub-check no-ops. citation-validity is clean.

**surface-or-evidence — pass.** This is a new L4>L3 lowering theme (a fresh `new:` file), not a refinement of an existing operator/theme surface. It introduces a chapter with full rotation evidence (positive Palace source for every shell-piece rewrite) rather than backfilling rotation_claims onto existing text. The surface-or-evidence gate is about refinement-shaped proposals; a net-new theme with cited evidence satisfies it trivially. Not the degenerate "pure rotation_claim without surface" failure mode.

**rotation-quality — pass.** The L4→L3 dissolution is a genuine vocabulary translation, NOT an identity-in-named-terms rename. Three distinct, non-trivial vocabulary shifts are catalogued and each is source-witnessed: (1) the `foldl` combinator + `readonly` once-captured operator stratum → the hand-hoisted `TimeOperator`+integrator construction outside the `for` (type-level capture-once demoted to a coding convention); (2) the **immutable functional carry** (`\s t -> time_step_op op s t` returns a fresh `TimeState`) → **in-place destructive mutation of a single persistent `sol` vector** (`ode->Step(sol, t, dt)` advances the same vector; the prior write IS the next read) — this is the load-bearing fold-specific shift and is exactly the functional-carry→in-place-mutation translation the vocabulary-shift redirect demands a lowering narrate; (3) the abstract `[Time]` schedule + opaque quantified-over `time_step_op` → the concrete `delta_t`/`n_step` counting march + the concrete `ode->Step` library CALL. The L_{n+1} (L4) form is strictly more abstract/equational (a single `foldl` naming the whole march with a pure carry) than the L_n (L3) imperative loop. This is the opposite of a 1:1 rename. Pass.

**variant-axis-coverage — pass.** The orthogonal axis is the **schedule-source** axis (`fixed-list` vs `state-generated`). The theme explicitly scopes its RHS to the fixed-schedule (transient) form and explicitly scopes OUT the state-generated SweepAdaptive greedy march (cited as the parallel fold-spine witness only, gated on OQ `fold-solve-greedy-schedule-source-generalization`, batch-18). The §Applicability-conditions condition 4 makes the scope boundary a stated precondition rather than a hidden branch. The per-step-body axis (Palace-authored-loop-that-lowers vs opaque-library-leaf) is likewise explicitly handled: the fold's per-step body is scoped as the `obstruction (opaque-library-ownership)` sub-leaf, contrasted against the map sibling's `ksp.Mult` body which DOES lower. No hidden branches. Pass.

**cross-reference-integrity — pass (one expected same-cycle forward-link noted, not a defect).** All `[link]` targets resolve on disk: `solve-family-map-dissolution.md`, `iterate-while-dissolution.md`, `ksp-solve-driver-dissolution.md`, `triangular-solve-obstruction.md`, the three concept pages (`state-stratification`, `sequential-obstruction`, `variant-absorption`), `L4/solve_family.md`, `L4/iterate-while.md`, `L4/eigsolve.md` (the `../L4/eigsolve.md` path resolves), `L3/chebyshev.md`. The lone non-resolving link is `../L4/fold_solve.md` — the same-cycle D1 (LEAD) forward-reference, which the report flags explicitly (frontmatter, §Context, §Open-questions) as landing at integration before the single finalize build per the "Integration may materialize implied components" / same-cycle-sibling pattern. This is the documented acceptable case, not a dangling-link defect. Dual-registration verified against the actual on-disk anchors: the index.md theme-list row append targets line 21 (the `solve-family-map-dissolution` row — confirmed last row), the §Vocabulary-cohort bullet append targets line 42 (confirmed), and the tally edit targets line 44 which on-disk reads "(firm L4>L3 themes: 6 → 7 this cycle)" / "**7 firm**" — the report's edit to "7 → 8" / "**8 firm**" is the correct increment. SUMMARY.md insertion after the `solve-family-map-dissolution` line (line 24) is the correct location. The new theme is wired into SUMMARY. No build-readiness fence defect (see plan-kind-consistency). Pass.

**edge-label-fidelity — pass.** The declared edge is L4→L3 (LHS = L4 `fold_solve` combinator, RHS = L3 in-place time-sweep), narrated forward. Every section honors this: §"L4 form (LHS)" is the `foldl` combinator, §"L3 form (RHS)" is the imperative sweep, §"Abstraction-direction note" + §Justification + §"L4 vs L3 distinction" all consistently narrate L4→L3. No drift to a different edge (no L3→L2 or L2→L1 content leaks in). The reverse-lift notes are correctly deferred to working notes per the high→low discipline. Pass.

**plan-kind-consistency — pass.** Declared kind is an L4>L3 lowering theme with status `firm` (on the outer-sweep structural rotation) carrying an `obstruction (opaque-library-ownership)` per-step sub-leaf. The content shape matches: the outer-sweep rotation is read off positive source (every shell-piece rewrite cited), justifying `firm`; the per-step opaque-leaf is correctly NOT used to demote the whole theme (the structure IS firm) NOR claimed-lowered (it is recorded as a boundary). The sub-leaf treatment follows the codified `obstruction (opaque-library-ownership)` sub-kind exactly — the negative anchor is recorded at Palace's CALL (`timeoperator.cpp:410`), NOT MFEM internals, which is the correct ownership-boundary placement (the functionality IS available to Palace but only through the MFEM `ODESolver` library boundary; NONE-promotion-route). The body is fully authored INSIDE the `new:`/`edit:` fences (the chapter body is within the ```new:...``` block; §Status, §Signature-equivalent, §Algebraic-laws transport, §Verified-against all enclosed) — no firm-body-outside-fence defect. No rough-in placeholders in a firm-claimed entry. Pass.

**skill-uptake-survey — pass.** The report's shape implies the citation-verification skill family; the abstractor references `tools/citecheck/citecheck.py --anchor` invocation explicitly (frontmatter inputs, §Supporting-evidence) including the codemap-vs-on-disk drift-resolution discipline (`verify-citation-range`'s mechanical realization). The `establish-negative-finding-exhaustiveness` companion for the opaque-library obstruction sub-kind is implicitly satisfied by the single-call negative anchor (the `ode->Step` boundary), appropriate to an inherited-sub-kind rather than a fresh obstruction theme. Telemetry surfaced; no blocking finding.

### Issues found

No fail- or warning-level issues. Two low-severity observations for the repairer/integrator (informational, not blocking):

1. **(very-low / informational) Tally-edit replacement scope, `CYCLE.md` Proposed-changes line 230 → `book/src/L4-L3/index.md:44`.** The report's tally-bump `edit:` replaces the consolidated-tally text but the on-disk line 44 carries additional trailing prose after the theme-list enumeration (the "(the krylov/gmres/fgmres trio was promoted to firm in c008/c020/c021 ... a 4-shell stratified hop.)" parenthetical). The report's replacement reproduces the theme-list portion and the "substantive" justification but recasts the trailing narrative around the new fold/map sibling pair. This is a deliberate rewrite of the tally paragraph (the report claims sole index-ownership this cycle, which is plausible — `solve-family-map-dissolution` at c055 was the last index touch), not a truncation. The integrator should confirm the old c055 4-shell-composition sentence is intentionally superseded by the new fold/map §3.7-children framing rather than accidentally dropped; if the 4-shell `solve_family` composition note is still wanted it can be retained alongside. Mechanical/editorial only — no correctness impact.

2. **(very-low / informational) Same-cycle forward-link dependency, `book/src/L4/fold_solve.md`.** The theme's correctness as a `firm` LHS-bearing chapter is contingent on D1 (LEAD) landing `L4/fold_solve.md` in the same cycle. The report handles this correctly per the documented same-cycle-sibling live-link pattern, but the integrator-finalize build will break if D1's report is rejected/deferred and this one is applied. Recommend the integrator apply D1 before D2 (the report's stated dependency order) or defer D2 if D1 does not land. Flagged for ordering awareness only — not a content defect in this report.

## Repair

### Fixes attempted

No findings to repair. The critic returned all 8 checks `pass` with zero fail- or warning-level issues. There are no `repaired` or `unrepairable` findings; every `repairs:` entry is `not-needed`. This was a status-setting pass only.

### Unrepairable findings

None.

## Suggested resolution

`overall_status: ready`. The report is clean and applicable. Two integrator-notes carried forward from the critic's low-severity informational observations (both editorial/ordering, neither a content defect):

1. **Tally-paragraph rewrite at `book/src/L4-L3/index.md:44`.** The report's tally-bump `edit:` deliberately recasts the trailing narrative paragraph around the new fold/map sibling pair (sole index-ownership this cycle is plausible — `solve-family-map-dissolution` at c055 was the last index touch). The integrator should confirm the old c055 4-shell `solve_family` composition sentence is intentionally superseded by the new fold/map §3.7-children framing rather than accidentally dropped; retain the 4-shell composition note alongside if still wanted. Mechanical/editorial — no correctness impact.

2. **Apply-order dependency on D1.** This theme's `firm` LHS-bearing chapter requires D1 (LEAD, wave-1, already reported) landing `book/src/L4/fold_solve.md` before/with D2 so the single finalize build resolves the `../L4/fold_solve.md` live link. Apply D1 first per the report's stated dependency order (or defer D2 if D1 does not land). Ordering awareness only.
