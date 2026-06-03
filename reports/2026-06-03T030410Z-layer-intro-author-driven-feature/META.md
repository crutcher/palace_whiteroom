---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T034500Z
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
---

# META: verification of "driven feature-surface column (FEATURE-SURFACE SPINE)"

## Critique

This report is a **feature-surface composition-root** of the **leaf feature column** sub-kind (per-driver; stage-2 constituents are vocabulary ops), at the operator-VARYING corner. The adapted feature-surface checklist (CLAUDE.md §Adapted-checks; critic role-spec) governs: surface-or-evidence is adapted to (L0 driver range + constituent down-links), rotation-quality and variant-axis-coverage are formal no-ops, and cross-reference-integrity is load-bearing (the column's value IS its down-links). All three chapter bodies (`driven.L4.md`, `driven.L1.md`, `driven.L0.md`) were read in full; the report also acts as **sole index/SUMMARY owner** for the driven/transient/eigenmode driver cohort, which is the source of the one warning.

### Checks run

**citation-validity — pass.** Every load-bearing L0 citation into `palace/drivers/drivensolver.cpp` was verified on-disk (palace-codemap `read_range` + grep line-map). All matched exactly: basis assemble before the loop `K :91`/`C :92`/`M :93`, curl `:94`, solver-built-once `:98`, the frequency loop `:168-170`, per-ω rebuild `A2 :175` / `A :176-177` / `P :178-179`, the **load-bearing `ksp.SetOperators(*A, *P)` INSIDE the loop `:180`** (the operator-varying witness — confirmed inside the `for (omega_i...)` body, not hoisted), per-ω RHS `:194`, per-ω solve `ksp.Mult(RHS, E) :196`, B-field recovery `:205-207`, measurement `MeasureAndPrintAll :215-216`, error-estimate `:220`, loop close brace `:221`, `MeasureFinalize :227`, `return indicator :228`, function close `:229`. The config-surface citations `:41`/`:42`/`:45`/`:47`/`:80`/`:153`/`:172` and the hpp class declaration `:22-34` (incl. `Solve` override `:29-30`, `SweepUniform`/`SweepAdaptive` `:25`/`:27`) all verified. `SweepAdaptive :231` confirmed. The only cross-file inconsistency is a benign ±1 boundary convention on the `Solve` definition: CYCLE.md and `driven.L4.md` frontmatter cite `:37-75`, while `driven.L0.md` body cites `:36-75` — line 36 is the return-type line, line 37 is the `DrivenSolver::Solve(` signature; both legitimately point at the same function definition, so this does not rise to a drift. No `verified_against:` YAML block is present, so the round-trip sub-check is inapplicable. Pass.

**surface-or-evidence (adapted) — pass.** For the feature-surface kind, the evidence is the L0 driver-source range + the constituent-op down-links, not a single decomposed op's source site. The composition is fully supported: the L0 range `drivensolver.cpp:77-229` (`SweepUniform`) + `:37-75` (`Solve` dispatch) is cited and verified, and all four claimed firm constituents (`fe_assemble`, `assemble_frequency_operator`, `frequency_sweep`, `ksp_solve` at L4; `fe_assemble`, `assemble_frequency_operator`, `ksp_solve` at L1) exist on disk and carry `firmness: firm` / `## Status: firm`. The chapter makes no new per-op algebraic claim of its own — it carries the compositional claim only, with per-op claims explicitly delegated to the linked chapters. The one unsupported-by-design constituent is the stage-3 S-parameter reduction (`sparameter_reduce` / `sparameter_response`), which is correctly framed as a plain-text forward-ref to a not-yet-authored output-product column (the reason the column stays `seed`). Pass.

**rotation-quality (adapted) — pass.** Formal no-op for the feature-surface kind: a composition-root rotates nothing — it recomposes already-firm vocabulary outward. The chapter explicitly states it "does not introduce a new combinator." Not applicable to feature-surface kind; marked pass.

**variant-axis-coverage (adapted) — pass.** Formal no-op for the feature-surface kind: the variant axes live in the constituent ops, not the feature chapter. Worth noting (not a defect): the report is conscientious about the uniform-vs-adaptive split — it scopes `SweepAdaptive` OUT as the `fold_solve` state-generated sibling (NOT this column's composition), which is the correct disposition of the one branch a naive reader might expect this column to cover. Marked pass (not applicable).

**cross-reference-integrity (load-bearing for this kind) — warning.** Every live link in the three chapter bodies resolves on disk: all L4 constituents (`fe_assemble`, `assemble_frequency_operator`, `frequency_sweep`, `ksp_solve`, `solve_family`, `fold_solve`), all L1 constituents, the `L1-L0/assemble-frequency-operator-rotation.md` rotation, and all sibling feature columns (`electrostatic.*`, `magnetostatic.*`, `lifecycle.L4`). The maturity claims on the down-link tables match on-disk `## Status` (all four firm constituents verified firm) — a correct `seed` column composing firm vocabulary held back only by an un-authored stage-3 reduction. The `driven.*` index.md / SUMMARY.md rows resolve to the files created in changes 1–3. **The warning is the sole-owner cohort dependency:** the report (as cohort index/SUMMARY owner) adds `transient.*` and `eigenmode.*` rows to BOTH `feature/index.md` (live `[...](./transient.L4.md)` etc.) and `SUMMARY.md` — those targets are authored by D3/D4 **this same cycle** and do NOT exist on disk now. A SUMMARY.md entry pointing at a missing file is a hard mdBook build break; a dead index.md table link is a `linkcheck2` error. This is correctly a build-readiness integrator-ordering hazard rather than an authoring error: the report carries explicit, well-specified integrator dependency notes (defang the index table rows to plain-text; OMIT the SUMMARY blocks) for exactly the case where D3/D4 do not land in the same finalize batch. The warning surfaces the cross-report ordering dependency so the integrator does not apply the transient/eigenmode rows blind.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (this is a composition-root, not a lowering theme). The directional framing that is present — L0 "lifts to" L1/L4, L1↔L4 "same feature, different vocabulary," and the high→low discipline note deferring the L1→L0 per-write lifts to the constituent rotation themes — is internally consistent and points at the correct surfaces. Pass.

**plan-kind-consistency — pass.** Declared kind is feature-surface / `status: seed`, and the content shape matches: composition-root body, inputs=config / output=physical product (FrequencyResponse / S-parameters), DOWN-links to constituents, no new combinator. The uniform `status: seed` token carries no `(exemplar)`/`(composition-root)` qualifier (correct per the codified convention; the leaf-feature-column sub-kind is named in prose). The `seed`-not-promoted rationale (stage-3 reduction not yet a firm authored constituent) is stated consistently across all three bodies and the CYCLE summary. Pass.

**skill-uptake-survey — pass.** The report documents on-disk self-verification of all L0 ranges via palace-codemap `read_range` + direct `Read` with close-brace discipline (the relevant procedure for the citation-heavy L0 surface). No feature-surface-specific authoring skill is mandated for this kind. Pure presence check; nothing missing. Pass.

### Issues found

1. **[warning] cross-reference-integrity / build-readiness — cohort index+SUMMARY rows for un-landed sibling columns.** `CYCLE.md` change 4 (`feature/index.md`, lines 92–93) adds live links `[transient](./transient.L4.md)` and `[eigenmode](./eigenmode.L4.md)` (+ L1/L0 cells), and change 5 (`SUMMARY.md`, lines 141–146) adds `transient.*` / `eigenmode.*` SUMMARY entries, whose target files are authored by cycle-073 D3/D4 and are NOT on disk at critique time. If D3/D4 do not land in the same finalize batch, the SUMMARY entries are a hard mdBook break and the index links are a `linkcheck2` error. **Mitigating:** the report supplies precise integrator dependency notes (defang index rows to plain-text; OMIT SUMMARY blocks; soften the index "Planned" prose) for the not-landed-together case. This is a flagged-for-the-integrator ordering dependency, not an authoring defect — surfaced here so the repairer/integrator handle the batch-ordering contingency rather than applying the sibling rows blind. The `driven.*` rows are always safe (their files are in this report).

2. **[informational, sub-warning] citation-validity — benign ±1 boundary inconsistency on the `Solve` definition range.** `driven.L0.md` body (line 24) cites `DrivenSolver::Solve ... (drivensolver.cpp:36-75)` while `CYCLE.md` and `driven.L4.md` frontmatter cite `:37-75`. Line 36 is the return-type line, line 37 is the `DrivenSolver::Solve(` signature line; both point at the same function and neither is out-of-range, so this is a convention difference, not a drift. Optional repairer cleanup: pick one boundary for consistency across the three files. Not blocking.

No other issues. The composition-root shape is correct (composes, does not replace; inputs=config, output=physical product), the operator-VARYING witness (`SetOperators` inside the loop) is precisely cited, and the all-firm-constituent claim is verified on disk.

---
repaired_at: 2026-06-03T040000Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

## Repair

### Fixes attempted

- **Finding**: [warning] cross-reference-integrity / build-readiness — cohort index+SUMMARY rows for un-landed sibling columns (`transient.*` / `eigenmode.*` live in `feature/index.md` change 4 + `SUMMARY.md` change 5; target files authored by cycle-073 D3/D4 same cycle, absent on disk at critique time).
  - **Decision**: repaired (batch-ordering dependency confirmed well-formed; dependency notes sharpened — NOT a row removal).
  - **Action**: `reports/2026-06-03T030410Z-layer-intro-author-driven-feature/CYCLE.md` — rewrote the change-4 (index.md table) integrator dependency note and the change-5 (SUMMARY.md) integrator dependency note to lead with the **expected happy-path ordering requirement** (apply D2's cohort index/SUMMARY block AFTER D3/D4's chapter files exist — last among the three reports, or in a single all-three-present finalize) before the per-failure-mode fallback. Made the asymmetry explicit and unambiguous: index-table fallback = defang the un-landed rows to plain-text (`linkcheck2` error only); SUMMARY fallback = OMIT the un-landed block(s) entirely, per-column-independent (a missing-file SUMMARY row is a HARD mdBook break, no plain-text defang). Confirmed the `driven.*` rows are always-safe and explicitly excluded from any defang/omit. The `transient.*` / `eigenmode.*` rows themselves are LEFT IN PLACE (correct — D3/D4 land same cycle, per the dispatch plan).
  - **Rationale for repaired-not-deferred**: this is a cross-report finalize-ordering contingency the report already flagged and handled; the repair is purely making the integrator instructions crisp/unambiguous (mechanical note-sharpening), not authoring content or removing correct rows. No substantive authoring; in repair scope (append-by-slug / integrator-hint clarity class).

- **Finding**: [informational, sub-warning] citation-validity — benign ±1 boundary inconsistency on the `DrivenSolver::Solve` definition range (`driven.L0.md` body cited `:36-75`; CYCLE.md / `driven.L4.md` frontmatter / the `driven.L0.md` frontmatter `l0_ground_truth` block all cite `:37-75`).
  - **Decision**: repaired (trivial citation-offset harmonization).
  - **Action**: `reports/2026-06-03T030410Z-layer-intro-author-driven-feature/driven.L0.md` line 24 — changed the single `drivensolver.cpp:36-75` body citation to `:37-75`. Verified on-disk via palace-codemap `read_range` (`drivensolver.cpp:34-42`): line 36 is the return-type line (`std::pair<ErrorIndicator, long long int>`), line 37 is the `DrivenSolver::Solve(...)` signature line. The `:37-75` (signature-line start) form is the one used everywhere else in this report and the two sibling chapters, so harmonized to it. No other `:36-75` occurrence in the staged files.
  - **Rationale for repaired**: small citation off-by-one with the correct form already established elsewhere and confirmed on disk — squarely in the "citation line range off by a small offset" repair-authority class.

### Unrepairable findings

None. Both flagged items were repairable (one note-clarity sharpening, one trivial citation-offset harmonization); the critic's 7 `pass` checks need no action.

## Suggested resolution

`integrate`. The one `warning` was a flagged-and-handled cross-report finalize-ordering dependency, now with crisp happy-path + fallback integrator notes; the informational sub-warning is harmonized. **Integrator action required (not a blocker):** apply this report's cohort index/SUMMARY block (changes 4–5) AFTER cycle-073 D3 (transient) and D4 (eigenmode) chapter files are on disk — last among the three reports, or in a single finalize where all three land — so every `transient.*` / `eigenmode.*` cell is a live link. If either D3/D4 does not land in this batch, follow the per-column fallback in the (now-sharpened) change-4/change-5 dependency notes (index: defang the absent column's rows to plain-text; SUMMARY: omit the absent column's block). The `driven.*` rows/files are self-contained in this report and always safe to apply.
