---
verifies: ./CYCLE.md
critiqued_at: 2026-05-31T215905Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-31T220500Z
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

# META: verification of "Re-anchor floquet-correction-mutation-rotation AddMult inner-ksp aliasing-tolerance mechanism"

## Critique

### Checks run

**citation-validity — pass.** This is an ENACT re-anchor whose entire purpose is citation correctness, so I re-verified every load-bearing pinpoint on-disk against `reference/palace`, not just by reading the report. All confirmed:
- `iterative.cpp:361` IS `CgSolver<OperType>::Mult(const VecType &b, VecType &x) const`; `:360` is the bare `template <typename OperType>` line. The claimed **+1 drift is real and correctly resolved** — `citecheck.py palace/linalg/iterative.cpp:360 --anchor 'CgSolver'` returns `[DRIFT] anchor at line 361, +1 outside range ... suggested: :361`, and `:361 --anchor 'CgSolver'` is `[ok]`.
- `iterative.cpp:377` is `if (this->initial_guess)` (`citecheck --anchor 'initial_guess'` lit at `:377`).
- The else-branch: `:382` `else`, `:384` `r = b;`, `:385` `x = 0.0;`, `:386` `}`. `--anchor 'r = b'` lit at `:384`; `--anchor 'x = 0.0'` lit at `:385`. The read-before-zero aliasing-safe mechanism is exactly as the report describes. The if-branch `:377-381` (`:379` `A->Mult(x, r)` reads `x` first) is the aliasing-unsafe counterfactual the report cites — confirmed on-disk.
- `floquetcorrection.cpp:61` is `pcg->SetInitialGuess(0);` (`--anchor 'SetInitialGuess'` lit at `:61`); `:60` is the `CgSolver` `make_unique`, `:66` the `BaseKspSolver` wrap — the delegation chain is intact as narrated.
- `ksp.cpp:297` is `BaseKspSolver<OperType>::Mult`, `:300` is `ksp->Mult(x, y)` — a thin delegation wrapper carrying no aliasing logic, as claimed (`:299` is `BlockTimer`). `--anchor 'BaseKspSolver'` lit at `:297`.

The `verified_against:` round-trip sub-check: I extracted the 3 proposed Edit-5 rows and ran `yaml.safe_load` — ROUND-TRIP OK (3 rows, all `supports`). No `note:` value begins with `'` or `"` (the notes open with `BaseKspSolver`, `CgSolver`, `pcg` respectively; em-dashes appear mid-note, which is safe). The OQ-ledger carry-forward at `open-questions.md:948` independently pre-recorded exactly these lines (`iterative.cpp:361`, else-branch `:384-385`, `SetInitialGuess(0)` `floquetcorrection.cpp:61`), so the re-anchor matches the cycle-038 audit's prescribed edits.

**surface-or-evidence — pass.** This is a refinement that BOTH modifies surface (Sub-pattern B prose, Citations list, Applicability condition 2, Verified-against L0 list) AND carries the rotation/lowering evidence — and it is additionally framed as retroactive-evidence-completion (the *conclusion* "aliasing is safe" was always correct; only the *evidence pointer* was misattributed from wrapper to mechanism). Either framing clears this check.

**rotation-quality — pass (not the primary axis for this report-kind).** No new rotation is asserted; the theme's structural AddMult-as-axpy rewrite (`floquetcorrection.cpp:80-86`) is explicitly untouched. The re-anchor only sharpens the *evidence* for an existing applicability condition, making the claim strictly more precise (unconditional → conditional-on-`SetInitialGuess(0)`). That is a refinement, not a rotation, so the check no-ops favorably.

**variant-axis-coverage — pass.** The one variant axis this re-anchor touches — `initial_guess == true` vs `== false` — is covered exhaustively: the report names the else-branch (`:382-386`, the taken path under `SetInitialGuess(0)`) AND the if-branch counterfactual (`:377-381`, which would break aliasing), correctly explaining why the tolerance is conditional. No hidden branch.

**cross-reference-integrity — warning.** Fence parity is clean: 5 `edit:` blocks open/close with balanced ```` ``` ```` (137/178, 182/207, 211/230, 234/245, 255/268); Edit 1's inline `else {...}` snippet is 4-space-indented code (lines 161-165), NOT a nested ```` ```text ```` fence, so the truncation defect is absent. All 5 replacement targets exist verbatim in the artifact (Edit 1 → line 146 prose; Edit 2 → line 175 Citations; Edit 3 → line 314 cond-2; Edit 4 → line 416 V-A list; Edit 5 → the `partially-supports` row at artifact lines 551-554). **However, the re-anchor under-covers:** there are SIX `ksp.cpp:297` mention sites in the artifact (lines 155, 175, 319, 416, 461, 551), and the 5 edits reframe only five of them. **Line 461 — the §Status paragraph — is left untouched** and still asserts the AddMult aliasing applicability "has a positive source site ... (`palace/linalg/ksp.cpp:297` + the L0 calling sequence)", i.e. it still names the *wrapper* as the mechanism-bearing evidence with no `iterative.cpp:361` re-anchor. This is the exact misattribution the dispatch exists to correct, surviving in the firmness-justification paragraph. See Issue 1.

**edge-label-fidelity — pass.** This report has no L_{n+1}→L_n edge label to mis-target (it is a within-theme L1>L0 re-anchor, single edge). The re-framing of `ksp.cpp:297` as the *call-path delegation wrapper* (rather than removing it) is accurate on-disk: `:300` does forward to the inner solver, and the mechanism IS at `iterative.cpp`. The prose narrates the delegation chain correctly (`BaseKspSolver::Mult` `ksp.cpp:297` → `ksp->Mult` `:300` → `CgSolver::Mult` `iterative.cpp:361`). The theme correctly stays `firm` — the structural rewrite is untouched and the re-anchor only completes evidence for a sub-claim. No edge-label drift.

**plan-kind-consistency — pass.** The declared kind (lowering-verifier ENACT re-anchor of a firm L1>L0 theme) matches the content shape: surgical citation-widening edits + a `partially-supports`→`supports` verdict upgrade + 2 new mechanism rows, with no status change and no new vocabulary. Consistent with an ENACT-the-carry-forward dispatch.

**skill-uptake-survey — warning.** The report references `tools/citecheck/citecheck.py --anchor` repeatedly (the §On-disk re-verification table + §Supporting evidence), which is the mechanical realization of `verify-citation-range`, and the discipline it invokes (codemap-read-range-plus-one-drift) is the right one. But for an ENACT report carrying a `verified_against:` YAML block edited inside an `edit:` fence, two directly-relevant skills are NOT named: `proposed-changes-fence-encloses-full-body-guard` (the report asserts fence balance in prose at lines 130-133 but does not cite invoking the guard) and the YAML-round-trip sub-check. Pure telemetry surface, non-blocking — the work appears to have been done (fences ARE balanced, YAML DOES round-trip), just not attributed.

### Issues found

**Issue 1 (cross-reference-integrity; severity: moderate — residual misattribution at the firmness-justification site).** `book/src/L1-L0/floquet-correction-mutation-rotation.md:461` (§Status, the "No partly-constructive caveat applies" paragraph) is NOT covered by any of the 5 proposed edits and still reads: *"This theme has a positive source site for every step, including the AddMult fusion's load-bearing aliasing applicability (`palace/linalg/ksp.cpp:297` + the L0 calling sequence)."* This is the precise wrapper-as-mechanism misattribution the whole dispatch is correcting. After the 5 edits land, line 461 would be the one surviving site that names `ksp.cpp:297` as the mechanism-evidence for the aliasing sub-claim, contradicting the freshly-reframed Sub-pattern B / Applicability-condition-2 / Verified-against text. The §Status firmness justification would still point at the wrapper. The fix is a sixth surgical edit reframing line 461 to cite `iterative.cpp:361` (+ `floquetcorrection.cpp:61`) as the positive mechanism site, with `ksp.cpp:297` noted as the call-path wrapper — parallel to Edits 1/3/4.

**Issue 2 (cross-reference-integrity / OQ-closure justification; severity: minor — closure claim is slightly over-stated while Issue 1 stands).** The report claims (§Summary, §Open questions) that `floquet-corrector-addmult-aliasing-applicability-audit` "can be CLOSED" with "No residual evidence gap on the aliasing applicability sub-claim." The OQ-ledger carry-forward at `open-questions.md:948` does prescribe exactly these edits and they ARE faithfully enacted, so the closure is *substantially* justified — but Issue 1's untouched §Status line 461 is a residual instance of the very evidence-gap the OQ tracks. Strictly, the OQ should not be marked fully CLOSED until line 461 is also reframed (or the closure note should be scoped to "closed pending the §Status sixth edit"). Low severity because the gap is a single un-reframed sentence, not a substantive evidence hole — the mechanism IS now cited correctly in five of six sites.

**Issue 3 (citation-validity; severity: informational — internal range-label inconsistency, not a defect).** The report uses two range labels for the same mechanism across edits: Edit 5's `verified_against:` row cites `iterative.cpp:360-386` (template-line through close-brace) while Edit 2's Citations-list entry cites `iterative.cpp:361` (signature only) and Edit 4's V-A list cites `iterative.cpp:360-386`. Both are on-disk-correct (the `:360` template line + `:361` signature + `:382-386` branch all resolve), and the report explicitly explains the `:360-386` range encompasses template+signature+branch. Not a drift — but a downstream reader/integrator sees `:361` in one widened citation and `:360-386` in another for the same construct. Optional: harmonize to one convention (the `:360-386` range is the more defensible since it brackets the whole mechanism).

**Note (not an issue):** the pre-existing OQ `floquet-correction-real-vector-instantiation-dead-code` (Sub-pattern D) is correctly left untouched and explicitly retained (report §Open questions; ledger `open-questions.md:898,952`). Scope discipline upheld.

## Repair

### Fixes attempted

- **Finding**: Issue 1 (cross-reference-integrity, moderate) — the §Status firmness-justification paragraph (on-disk ~line 461) is the SIXTH `ksp.cpp:297` mention site and the 5 proposed edits leave it untouched; it still names the delegation wrapper `ksp.cpp:297` as the positive mechanism-evidence for the AddMult aliasing applicability — the exact misattribution this dispatch exists to correct, surviving in the firmness justification.
  - **Decision**: repaired
  - **Action**: Added **Edit 6** to CYCLE.md §Proposed changes (mechanical citation re-anchor, parallel to Edits 1/3/4). Read the on-disk §Status text first (`book/src/L1-L0/floquet-correction-mutation-rotation.md:459-463`) for a verbatim-bracketed replacement target; the new region keeps the anchor sentence stem and the firm-on-positive-structure closing verbatim, changing only the middle clause to cite the true mechanism `CgSolver::Mult` (`iterative.cpp:361`, else-branch `:382-386`, `r = b;` `:384` before `x = 0.0;` `:385`) gated by `SetInitialGuess(0)` (`floquetcorrection.cpp:61`), with `ksp.cpp:297` re-framed as the delegation wrapper (forwards `ksp->Mult(x, y)` at `:300`). Theme stays `firm`. Also corrected the §Proposed-changes preamble count ("Four" → "Six" surgical edits). All Edit-6 citations verified on-disk with `citecheck` (`iterative.cpp:361`/`:382-386`/`:384`/`:385`, `floquetcorrection.cpp:61`, `ksp.cpp:297`/`:300` — all `[ok]`/anchor-lit). Fence parity re-verified: 6 `edit:`-open fences (CYCLE.md 142/187/216/239/260/293) each paired with a bare ``` close (183/212/235/250/273/304); Edit 6 body carries no nested ```text fence and no indented-code block.

- **Finding**: Issue 2 (OQ-closure justification, minor) — the report claims OQ `floquet-corrector-addmult-aliasing-applicability-audit` can be CLOSED with "no residual evidence gap," but that was over-stated while the §Status line-461 misattribution stood.
  - **Decision**: repaired
  - **Action**: With Edit 6 now reframing the sixth/last site, the closure IS justified. Updated the closure note in CYCLE.md §Summary and §Open questions to state the re-anchor covers **all six** `ksp.cpp:297` mention sites (including the §Status firmness-justification paragraph via Edit 6), leaving no surviving wrapper-as-mechanism attribution — making the closure claim accurate relative to the now-complete edit set.

- **Finding**: Issue 3 (citation-validity, informational) — `:361` (signature-only) vs `:360-386` (whole-mechanism range) range-label inconsistency across edits; both on-disk-correct.
  - **Decision**: not-needed
  - **Rationale**: Explicitly flagged light/optional and not load-bearing. The report's own §Per-citation-audit rationale deliberately distinguishes the two uses (cite `:361` for the precise signature anchor; cite `:360-386` for the range bracketing template-line + signature + branch). Both forms citecheck-clean; the distinction is intentional, not a drift. Normalizing would introduce churn without correctness benefit. Edit 6 follows the §-prose convention (`:361` signature + `:382-386` else-branch), consistent with Edits 1/2/3.

- **Finding**: skill-uptake-survey (warning) — telemetry-only; `proposed-changes-fence-encloses-full-body-guard` and the YAML-round-trip sub-check were exercised but not attributed in the report.
  - **Decision**: not-needed
  - **Rationale**: Pure telemetry surface, explicitly non-blocking per the critic. The underlying work was correct (fences balanced, YAML round-trips). Attributing skill names is substantive report authoring, outside mechanical repair authority; not load-bearing for integration.

### Unrepairable findings

None. Both blocking findings (Issue 1 moderate, Issue 2 minor) were mechanically repairable — Issue 1 is a forgotten sixth mention-site that the report's own established pattern (Edits 1/3/4) trivially extends to, and Issue 2 follows automatically once Issue 1's edit lands. No substantive authoring was required.

## Suggested resolution

`ready` for the integrator. Notes:
- Edit 6 is a verbatim-bracketed replacement of the §Status "No partly-constructive caveat applies." paragraph (on-disk `book/src/L1-L0/floquet-correction-mutation-rotation.md:459-463`). The anchor stem and the firm-on-positive-structure closing sentence are preserved verbatim; only the aliasing-applicability clause changes from the `ksp.cpp:297`-wrapper attribution to the true `CgSolver::Mult` (`iterative.cpp:361`) + `SetInitialGuess(0)` (`floquetcorrection.cpp:61`) mechanism.
- After all 6 edits land, no surviving site in the theme names `ksp.cpp:297` as the aliasing mechanism-evidence; the OQ `floquet-corrector-addmult-aliasing-applicability-audit` closure is now fully justified (integrator promotes).
- Theme remains `firm` throughout; the structural AddMult-as-axpy rewrite is untouched. The pre-existing OQ `floquet-correction-real-vector-instantiation-dead-code` (Sub-pattern D) stays open by design.
