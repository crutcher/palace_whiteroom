---
verifies: ../CYCLE.md
critiqued_at: 2026-06-08T060000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-08T061500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "synthesis residual content-fidelity follow-ups (3 fixes)"

## Critique

### Checks run

**citation-validity — pass.** All three fixes' citations verified on-disk + mechanically.
- Fix (a): the canonical Form B call shape is at `book/src/L4/krylov-step.md:192-199` exactly as the `[new]` text reproduces (bootstrap-closure `(\_ -> pure { state: s1, prev: s0.beta })` / init-carry `s1` / steady-step `(\(s, beta_prev) -> ...)` / cont-predicate last). The `[old]` text matches `iterate-while-with-prev.md:233` verbatim, and the `:192-199` pin the `[new]` text adds is in-range and accurate.
- Fix (b): every `[old]` string matches its on-disk line (44, 69, 70, 97, 109, 180, 189) — confirmed by grep; the seven `[old]`/`[new]` pairs are exact.
- Fix (c): `config-record.md:69-74` widening is correct — `citecheck --anchor 'units'` confirms `units : Units` sits at line 74 inside the range (1 ok, 0 failing); the 5 sub-records occupy 69-73. The field-table `units` row is at `config-record.md:85`. The L0 backing `palace/utils/iodata.hpp:38` is `Units units;` — confirmed via codemap `read_range` (line 30 `// Configuration file objects.`, lines 31-35 the five `config::*Data` members, line 37 the comment, line 38 `Units units;`). The `types.md` `[old]` block matches lines 33-44 verbatim.

**surface-or-evidence — pass.** All three are content-staleness / completeness edits to existing firm surface (the report frames them explicitly as upstream-chapter polish bringing the L4 chapters / synthesis render into line with the already-correct audited Synthesis forms), not new algebraic claims. No record is newly named-in-signature without a home: `IoData` already has its definition home at `concepts/config-record.md` (the `types.md` block links to it as authoritative and is a VIEW), and fix (c) merely completes the rendered field list to match that authoritative schema. No rotation_claim shape. The record-definition obligation is satisfied (the home pre-exists; the edit adds a field to a render, not a new undefined record).

**rotation-quality — pass.** No algebraic/structural/reduction rotation is asserted by any of the three fixes; they are surface-text refreshes. Not applicable to a content-fidelity-followup report.

**variant-axis-coverage — pass.** No orthogonal variant axes are introduced or modified. Not applicable to this report kind.

**cross-reference-integrity — warning.** See Issues found. The fix (b) rename `initial_state → initial_eig_state` is complete *within* `L4/eigsolve.md` (all 7 occurrences flip), but the same EigState-threaded eigsolve-cap constructor token appears UN-FLIPPED in two cross-files that the report asserts do not exist, leaving a mixed-naming state across the eigsolve-cap surface. All `[link]`/slug references in the edits themselves resolve.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried by these content edits. The report's claim that no `synthesis/index.md` matrix-cell flip is needed is correct — these are within-bodied-chapter content edits with no rendered-status shell→bodied transition, so the index-cell-drift guard does not fire. (Distinct from the cross-file *text* occurrences flagged below, which are not matrix cells.)

**plan-kind-consistency — pass.** Declared as 3 LOW content-fidelity follow-ups (layer-intro-author dispatch); content shape (surgical `edit:` blocks against existing firm chapters, no new chapters/claims) matches. No mis-classification.

**skill-uptake-survey — pass (telemetry).** The report's shape (a multi-occurrence in-file rename + a cross-file consistency question) is exactly the situation a "rename-completeness / cross-file-occurrence sweep" skill would serve; none is referenced. Pure presence check, non-blocking — surfaced as telemetry for the meta-phase (see skill-candidates note below).

### Issues found

**Issue 1 (cross-reference-integrity, warning) — un-flipped eigsolve-cap `initial_state` in `L4/index.md` (2 occurrences).** `book/src/L4/index.md:56` (the eigsolve bullet) and `:132` (the eigsolve dep-map row) both carry the eigsolve cap as `eigsolve op inp = execState (solve_loop op inp) initial_state` / `... (initial_state inp)` — the SAME EigState-threaded cap whose constructor fix (b) renames to `initial_eig_state` for consistency. The report's §Open-questions states "No L3-kernel or L4-sibling cross-file occurrence exists" and "No `eigsolve.md` occurrence was left un-flipped"; the first clause is FALSE — `L4/index.md` is the L4 sibling index and carries two eigsolve-cap occurrences of the exact token. Leaving them creates the mixed `initial_state` / `initial_eig_state` naming across the eigsolve-cap surface that the driving OQ (`l4-eigsolve-initial-state-vs-initial-eig-state-seed-inconsistency`) names. NOTE for the repairer/integrator scoping: `index.md:53/135/140` are the `ksp_solve` / generic `solve_loop` rows (SimState-threaded) and correctly STAY `initial_state` — only the two eigsolve-cap occurrences (56, 132) share the rename rationale. Location: report §Open-questions bullet 2 + §Supporting-evidence (b) ("No L3-kernel or L4-sibling cross-file occurrence exists").

**Issue 2 (cross-reference-integrity, warning) — `synthesis/coordination.md` NOTE becomes stale/self-contradictory after fix (b).** `book/src/synthesis/coordination.md:225-229` carries a deliberate NOTE: *"The authoritative L4 chapter (book/src/L4/eigsolve.md:44) writes `initial_state inp`; … the L4 chapter's reuse of `initial_state` for the EigState-threaded cap is a latent inconsistency to reconcile upstream — lowering-verifier."* Fix (b) IS that upstream reconciliation. Once it lands, `L4/eigsolve.md:44` no longer writes `initial_state inp`, so the NOTE's factual premise ("the L4 chapter writes `initial_state inp`") is false and its "latent inconsistency to reconcile upstream" call is discharged-but-still-asserted. The report does not address this NOTE; it is the explicit pre-existing record of the inconsistency the fix resolves, and is left dangling. Location: not covered anywhere in the report (the report's §Supporting-evidence (b) asserts no cross-file occurrence exists, which this NOTE contradicts directly — it even pins `eigsolve.md:44`).

### Note on severity

Both issues are `warning`, not `fail`: the three proposed edits are themselves correct and well-cited, and nothing in them is wrong on disk. The defect is *scope under-coverage* of the fix (b) rename — a real but bounded completeness gap (4 additional occurrences across 2 files: `index.md:56`, `index.md:132`, and the `coordination.md:225-229` NOTE which needs a re-phrase, not a token-flip). The report's own internal claim that no such occurrences exist is the false assertion to correct; the repairer can enumerate the additional occurrences mechanically (`grep -n 'initial_state' book/src/L4/index.md book/src/synthesis/coordination.md`).

## skill-candidates note

Appending a `proposed` candidate to `scaffolding/skill-candidates.md` for a cross-file rename-completeness sweep (the gap that produced Issues 1+2: an in-file multi-occurrence rename whose cross-file sibling/index/synthesis-NOTE occurrences were asserted-absent rather than grepped).

---

## Repair

### Fixes attempted

- **Finding (cross-reference-integrity, warning, Issue 1)**: fix (b)'s `initial_state → initial_eig_state` rename is complete within `L4/eigsolve.md` but two eigsolve-cap occurrences in `L4/index.md` (bullet :56, dep-map row :132) are left un-flipped; the report's "no L4-sibling cross-file occurrence exists" claim is false.
  - **Decision**: repaired.
  - **Action**: extended fix (b) in `reports/<id>/CYCLE.md` §Proposed changes ("Fix (b) cross-file completion" block) with two `edit:book/src/L4/index.md` Replace blocks flipping the eigsolve bullet (:56) and dep-map row (:132). Verified on-disk via `grep -n 'initial_state' book/src/L4/index.md` that lines 53/68/135/140 are the `ksp_solve` / generic `solve_loop` **SimState** rows — these are CORRECTLY left as `initial_state` (NOT flipped); only the two eigsolve-cap occurrences flip. Both anchor strings confirmed unique on-disk (the line-56 `eigsolve op inp = …` prefix distinguishes it from line-53's `solve op inp = …`; line-132's `(initial_state inp)` is unique). Also corrected the report's now-false §Open-questions assertion with a REPAIRER CORRECTION note.
  - **Scope rationale**: a scoped rename-completion (mechanical token flip on a clearly-enumerable occurrence set, with the SimState carve-out grep-verified) — squarely within repair authority (forgotten cross-file occurrences of a rename the original agent already applied in-file).

- **Finding (cross-reference-integrity, warning, Issue 2)**: `synthesis/coordination.md:225-229` is a deliberate NOTE pinning `eigsolve.md:44` and calling its `initial_state` reuse "a latent inconsistency to reconcile upstream"; fix (b) IS that reconciliation, so the NOTE's premise goes stale/self-contradictory once the rename lands.
  - **Decision**: repaired.
  - **Action**: read the NOTE on-disk first (lines 218-237 of `book/src/synthesis/coordination.md`), then added an `edit:book/src/synthesis/coordination.md` Replace block to the same "Fix (b) cross-file completion" report block. The re-phrase (NOT a token-flip) preserves the NOTE's "deliberately eigen-specific / StateT EigState discharge" rationale, updates the factual premise to state the L4 chapter now also writes `initial_eig_state inp`, and records that the formerly-latent inconsistency has been reconciled upstream (discharging the dangling "reconcile upstream — lowering-verifier" call). Minimal and accurate to the post-fix-(b) state.
  - **Scope rationale**: a stale-note de-staling that follows mechanically from the rename the report already makes — no new content authored, only the note's premise brought into line with the edit landing alongside it. Within repair authority (surgical fix of a record made stale by an in-report change).

### Unrepairable findings

None. Both warnings are the same scope-under-coverage of fix (b)'s rename and were mechanically completable (a scoped token-flip with a grep-verified carve-out + a stale-note re-phrase).

## Suggested resolution

`ready`. The two cross-reference-integrity warnings are fully repaired: the eigsolve-cap rename is now complete across all three files (`L4/eigsolve.md` 7 occurrences + `L4/index.md` 2 occurrences), the `ksp_solve` / generic `solve_loop` SimState rows are correctly left as `initial_state`, and the `coordination.md` NOTE is de-staled to reflect the discharged reconciliation. The three driving OQs are discharged by the (now cross-file-complete) edits. Integrator note: apply all blocks together so no intermediate mixed-naming or stale-note state is committed.
