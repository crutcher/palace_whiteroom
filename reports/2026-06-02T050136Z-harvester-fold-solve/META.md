---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T051923Z
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
repaired_at: 2026-06-02T053041Z
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

# META: verification of "Formalize fold_solve at L4" (cycle-058 D1)

## Critique

### Checks run

**citation-validity — pass.** Ran `tools/citecheck/citecheck.py --scan` over the whole report: 33 ok, 0 failing (all bounds + path-hygiene clean). Anchor-verified every load-bearing pinpoint with `--anchor` and confirmed semantics with codemap `read_range`:
- Transient fold witness 1: `transientsolver.cpp:33` (`TimeOperator time_op(...)` built once), `:35` (`delta_t = iodata.solver.transient.delta_t`), `:36` (`n_step = config::GetNumSteps(...)`), `:77` (`for` loop), `:93` (per-step `Step`), `:98/:99` (per-step `GetE/GetB`). `timeoperator.cpp:312` (`op = std::make_unique<TimeDependentFirstOrderOperator>(...)` — constructed once), `:410` (`ode->Step(sol, t, dt)` — confirmed in-place advance of the persistent `sol`, the prior step's output = next input, a genuine `foldl`). The `IMPLICIT` integrator claim (report §Algebraic-laws "`timeoperator.cpp:310`-region") is faithful — `mfem::TimeDependentOperator::Type type = ...::IMPLICIT;` sits at that line region.
- SweepAdaptive fold witness 2: `drivensolver.cpp:73` (adaptive dispatch), `:231` (`SweepAdaptive` entry), `:384` (`for (... it < max_size_per_excitation && memory < convergence_memory; ...)` — state-derived loop bound, confirmed verbatim), `:389` (`double omega_star = prom_op.FindMaxError(excitation_idx)[0]` — state-derived next input, confirmed verbatim), `:398` (`memory = max_errors.back() < offline_tol ? memory + 1 : 0` — state-derived termination counter, confirmed verbatim). The greedy state-generated-schedule claim (next input + loop bound both state-derived) is directly supported by the source.
The report's own §Evidence drift-correction note (codemap `read_range` +1 caught and corrected on `:35`, `timeoperator.cpp:312`, `drivensolver.cpp:241`, `:398`, `transientsolver.cpp:98`) is consistent with what citecheck `--anchor` independently confirms — the corrected lines all anchor cleanly. No `verified_against:` block in this report (harvester, not lowering-verifier), so that sub-check no-ops.

**surface-or-evidence — pass.** This is a new-operator firm entry (`new:book/src/L4/fold_solve.md`), not a refinement of existing surface, so the refinement-shaped-proposal gate is N/A in its strict form; but the entry both *authors* surface (full chapter body) AND carries rotation/evidence (two positive driver-loop witnesses with line-anchored laws). Not a pure rotation_claim. Pass.

**rotation-quality — pass.** The entry asserts a structural abstraction: the L4 `foldl`-combinator form is strictly more abstract/equational than the L0 C++ `for`-loop threading `sol` in place. The operator-capture-once becomes a type-level `readonly` stratum (was a coding convention), the carry-threading becomes a typed `TimeState` thread (was an in-place mutation of `sol`), and the map/fold axis becomes the §3.7 degenerate-vs-non-degenerate distinction. This is genuine state-hiding / structural compression, not a 1:1 rename. The §3.7 `iterate_while`-carry rendering and the direct `foldl` form are presented as equivalent (a presentation rotation), which is correctly labeled as such. Pass.

**variant-axis-coverage — pass, and notably strong.** Four axes declared (schedule-source, per-step-operator, carry-shape, element-type); the load-bearing one (schedule-source: fixed-list vs state-generated) is explicitly named, justified against both witnesses, and the scope-out is explicit (fixed-list = default surface; state-generated recorded as the axis + deferred to OQ `fold-solve-greedy-schedule-source-generalization`). No hidden branch: the SweepAdaptive greedy form is openly the state-generated case, not silently folded into the fixed-`[Time]` signature. The report explicitly states it does NOT force the `foldl-over-[Time]` signature onto SweepAdaptive (which exhibits no fixed `[Time]`) — the correct non-distorting treatment. The classification decision (ONE combinator, schedule-source as variant axis) is stated, justified (both share the state-threaded fold spine; the fixed form is the §3.7-carry special case where next-input = `head remaining`), and non-distorting to both witnesses. Pass.

**cross-reference-integrity — warning.** Most references resolve: `iterate-while.md`, `solve_family.md`, `chebyshev.md`, `eigsolve.md`, `ksp_solve.md` all exist in `book/src/L4/`; `state-stratification.md`, `sequential-obstruction.md`, `derived-view-hoisting.md` all exist in `book/src/concepts/`. Artifact-side anchors verified: `iterate-while.md:9` (names transient time-stepping among iterate_while-folds — the anchor `fold_solve` claims), `ksp_solve.md:153` (element-type cap), `L4/index.md:62/:82/:37` all match their cited content. The firm-body-inside-fence build-readiness guard PASSES: fence enumeration shows 6 fences / 3 balanced blocks; the `new:` block runs 31-218 and fully ENCLOSES `## Status` (186), Signature (66), Algebraic-laws (123), Evidence (199) — no fence-truncation defect; no nested `text` fences inside the body (signatures use 4-space-indented code). The warning is the forward-reference to `book/src/L4-L3/fold-solve-time-step-dissolution.md`, which **does not exist on disk** (it is the D2 sibling theme this same cycle). It appears as a **rendered live link** at report lines 175 (§Lowers-to body) and 222 (index dep-map row) — `[fold-solve-time-step-dissolution](../L4-L3/fold-solve-time-step-dissolution.md)`. Per friction-ledger `rough-in-forward-reference-must-be-plain-text-not-live-link`, a rendered live link to a not-yet-on-disk file is a hard `linkcheck2` build error unless D2 lands first or the integrator materializes a stub. (The `lowers_to:` frontmatter occurrence at line 41 is YAML, not rendered, and matches the `solve_family` precedent — fine.) This is an integration-ordering hazard, not a content error.

**edge-label-fidelity — pass.** The L4>L3 edge label (`fold-solve-time-step-dissolution`, L4→L3) and the in-line rotation-direction prose both consistently discuss L4 fold-combinator → L3 explicit in-place-threading loop. No edge/prose mismatch. The non-adjacent / map-vs-fold contrast prose (vs `solve_family`) is correctly framed as a same-layer sibling contrast, not a lowering edge.

**plan-kind-consistency — pass.** Declared kind is `firm` full L4 operator entry. Content shape matches: complete Signature, Semantics, Algebraic-laws (with explicit non-laws), Specializations, Variant-axes, Status, Evidence — no rough-in placeholders in the firm body. The `firm` status invocation rests on the firm-on-positive-structure escape (laws are read-off syntactic identities on two positive driver loops, not test-gated convergence semantics like `eigsolve`), which is a recognized CLAUDE.md status route and is correctly distinguished from `rough-in (test-coverage-bounded)`. The §3.7 `iterate_while`-child framing (NOT a new parent abstraction) is faithful to batch-17 meta decision 2 — the entry consumes `iterate-while.md` as the shared parent and introduces no third combinator. Consistent.

**skill-uptake-survey — pass.** The `disciplined-cross-pipeline-combinator-mining-gate` skill is cited explicitly for the 2-of-N fold-witness discharge (frontmatter input line 13, §Summary, §Status line 188, §Supporting-evidence line 243). The ≥2-witness bar is invoked correctly (two state-threaded sweeps; the other three pipelines accounted for as map/opaque, not silently dropped). Skill exists at `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md`. Surfaced, not blocking.

### Issues found

1. **[cross-reference-integrity, warning] Rendered live links to a not-yet-existing L4-L3 theme.** `reports/2026-06-02T050136Z-harvester-fold-solve/CYCLE.md` lines 175 (§Lowers-to body of the `new:book/src/L4/fold_solve.md` block) and 222 (the `edit:book/src/L4/index.md` dep-map row) both render `[fold-solve-time-step-dissolution](../L4-L3/fold-solve-time-step-dissolution.md)` as a live link, but `book/src/L4-L3/fold-solve-time-step-dissolution.md` does not exist on disk (it is the D2 sibling authored this same cycle). If D2 has not integrated before this report, `linkcheck2` will hard-fail. Resolution options (repairer/integrator call): (a) integration ordering so D2 lands first; (b) integrator materializes the dissolution-theme stub at apply time (the implied-component stub directive); (c) demote the two rendered occurrences to plain-text per `rough-in-forward-reference-must-be-plain-text-not-live-link`. The line-41 `lowers_to:` YAML occurrence is fine (not rendered; matches the `solve_family` precedent). Severity: low-to-medium — purely a build-ordering hazard; the reference target is clearly implied (≥2 converging references + a named D2 dispatch), so a stub is the preferred resolution.

2. **[informational, no severity] Self-flagged stale-row removal exceeds report authority.** The report (§Open-questions line 249, line 250) correctly notes that the c057 `rough-in` dep-map row at `L4/index.md:82` must be REMOVED (leaving only the new firm live-link row at line 222), and that this sibling-row removal exceeds the harvester's one-row-append authority. This is correctly surfaced for the integrator, not a defect — noted here so the repairer/integrator does not miss that two `fold_solve` dep-map rows would otherwise coexist (one stale `rough-in; no anchor yet`, one firm) and that the `edit:book/src/L4/index.md` block as written only ADDS the firm row without deleting the stale one. The §Vocabulary-cohort prose firmness-count refresh is likewise correctly deferred to layer-intro-author.

## Repair

### Fixes attempted

- **Finding** (cross-reference-integrity, warning): CYCLE.md lines 175 (§Lowers-to body of the `new:book/src/L4/fold_solve.md` block) and 222 (the `edit:book/src/L4/index.md` dep-map row) render `[fold-solve-time-step-dissolution](../L4-L3/fold-solve-time-step-dissolution.md)` as a **live link**, but `book/src/L4-L3/fold-solve-time-step-dissolution.md` does not yet exist on disk.
  - **Decision**: repaired (no-op annotation; NO content mutation, NO downgrade-to-plain-text).
  - **Action**: Verified the target file is authored **this same cycle** by dispatch D2 — `reports/2026-06-02T050136Z-abstractor-fold-solve-dissolution/CYCLE.md:23` carries a `new:book/src/L4-L3/fold-solve-time-step-dissolution.md` proposed-changes block under the **exact** canonical slug `fold-solve-time-step-dissolution` that D1 references. The two reports are mutually consistent (D1 forward-references D2's file at the planner-stated slug; D2 forward-references D1's cap at `../L4/fold_solve.md` and self-documents the same-cycle forward-ref at its line 258). Both land in the same cycle-058 integration, ahead of the single `integrator-finalize` `cargo make book` build, so `linkcheck2` sees both files present and the live links resolve. This is the **correct-by-construction same-cycle cross-report forward-reference** pattern (CLAUDE.md "Integration may materialize implied components as stubs" + the cross-report-forward-reference convention) — the live link is the *correct* form. Downgrading the two occurrences to plain-text would un-link a reference whose target co-lands this cycle, which is the wrong repair. The line-41 `lowers_to:` YAML occurrence is unrendered (matches the `solve_family` precedent) and was already fine. No edit applied to CYCLE.md; the repair is this recorded determination that the warning resolves by D2's co-landing.

### Unrepairable findings

None. The single warning resolved by determination (D2's co-landing makes the live link correct); no substantive authoring was required.

### Integrator-note (informational item 2 — stale c057 dep-map row removal)

The report self-flags (§Open-questions lines 249–250) that the c057 `rough-in` `fold_solve` dep-map row at `book/src/L4/index.md:82` must be **REMOVED** when D1 is applied, leaving only the new `firm` live-link row (the `edit:book/src/L4/index.md` block at CYCLE.md:220–223). As written, that `edit:` block only **ADDS** the firm row and does NOT delete the stale `rough-in; no anchor yet` sibling — removing a sibling row exceeds the harvester's one-row-append authority, so it is correctly surfaced for the integrator, not a defect. **`integrator-per-report`, when applying D1: delete the stale `| `fold_solve` *(rough-in; no anchor yet ...)* |` row (CYCLE.md:221 content, currently `L4/index.md:82`) so the two `fold_solve` dep-map rows do not coexist; keep only the firm `[`fold_solve`](./fold_solve.md)` row.** This is mechanical row-deletion, not authoring. (The §Vocabulary-cohort / §Active-frontier prose firmness-count refresh on `L4/index.md` is correctly deferred to layer-intro-author per the report — out of integrator scope.)

## Suggested resolution

`overall_status: ready`. The single warning (cross-reference-integrity) is resolved correct-by-construction: dispatch D2 authors the live-link target `book/src/L4-L3/fold-solve-time-step-dissolution.md` this same cycle under the exact slug D1 references, so both files land together and the links resolve at the finalize build — no content change to D1 is needed (a downgrade-to-plain-text would have been wrong). All other 7 checks passed. One mechanical integrator-note for `integrator-per-report` (above): delete the stale c057 `rough-in` `fold_solve` dep-map row when applying D1's `edit:book/src/L4/index.md` block, keeping only the new firm row. No blockers.
