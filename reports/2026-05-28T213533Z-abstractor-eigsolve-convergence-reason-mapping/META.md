---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T215500Z
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
repaired_at: 2026-05-28T214740Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L1>L0 theme sketch — eigsolve-convergence-reason-mapping (partly-constructive re-verification)"

## Critique

### Checks run

**citation-validity — pass.** This was the CRITICAL focus. I independently re-ran all six negative-anchor searches and re-read all three positive citation ranges via codemap. Every claim holds:
- Negative anchors: `EPS_DIVERGED` → 0 hits; `EPS_CONVERGED` → 0 hits; `GetConvergedReason` → 0 hits; `DIVERGED` → 0 hits. `ConvergedReason` → exactly the three print-only `*ConvergedReasonView` sites at `slepc.cpp:{699,1182,1529}` (snippets confirm each is fed to `PETSC_VIEWER_STDOUT_`). `GetConverged` → count-readers only: `slepc.cpp:{276,310,695,1178,1525}` plus the unrelated `ksp.cpp:301` and `iterative.hpp:98`. No `*GetConvergedReason` accessor exists anywhere. The negative anchor is real and complete — Palace prints the reason, never binds/branches/returns it.
- Positive citations, all line-exact: EPS `EPSGetConverged@695` + `EPSConvergedReasonView@699` (inside `if (print > 0)`) + `return (int)num_conv@708`; PEP `PEPGetConverged@1178` + `PEPConvergedReasonView@1182` + `return (int)num_conv@1191`; NEP `NEPGetConverged@1525` + `NEPConvergedReasonView@1529`, then the eigenpair-ordering loop with no early return (the entry correctly asserts NO NEP return-line citation — this restraint is itself accurate).
- L1 anchor `book/src/L1/eigsolve.md:51` reads exactly `EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed` (4 variants). Confirmed.
The single precision note (recorded under Issues, non-blocking): the `GetConverged` count-reader list `{276,310,695,1178,1525}` lumps `SVDGetConverged@310` (an SVD spectral-estimation helper) and `EPSGetConverged@276` (a separate helper) in with the three `Solve()`-body sites without disambiguating them. This is conservative (extra count-reader sites do not weaken "no `*GetConvergedReason`") and does not affect the verdict.

**surface-or-evidence — pass.** This is a refinement-shaped proposal against an existing theme. It is framed explicitly as **pure retroactive evidence backfill** (an append-only `### Re-verification (cycle-016 abstractor)` subsection under `## Verified-against`, with a `verified_against` YAML block), with NO status change, NO semantic-surface edit, NO SUMMARY/index edit. Retroactive evidence backfill without surface change is the allowed case per the check definition. The report is unambiguous on this (Summary lines 61-66; Proposed-changes lines 70-74, 132-136).

**rotation-quality — pass (not applicable as a fresh rotation).** No new algebraic/structural rotation is asserted; the L1>L0 reason→status rotation already exists (cycle-013) and the report proposes no change to it. The proposal only re-confirms the existing partly-constructive negative anchor. Marked pass as inapplicable to a re-verification-only report.

**variant-axis-coverage — pass.** The three SLEPc backend families (EPS / PEP / NEP) are the variant axis; all three are covered by separate positive citations, and the report correctly records PEP as isomorphic-to-EPS (non-additive) and NEP's no-early-return distinction. The 8 diverged-family rows + 2 count-anchored converged rows + the `*_CONVERGED_ITERATING` sentinel are all enumerated. No hidden branch. (SVD is not a variant of this theme — the SVD path is a separate spectral helper, correctly out of scope, though see the count-reader-list precision note below.)

**cross-reference-integrity — pass.** Every cross-reference resolves: `book/src/SUMMARY.md:68` (chapter entry present), `book/src/L1-L0/index.md:23` (dep-map row present with `partly-constructive` annotation and the `{699,1182,1529}` print-only citations), parent `book/src/L1-L0/eigsolve-mutation-rotation.md` forwarding link to this sub-theme present at lines 341-344 (cited as `:332-344` — in-range, the surrounding SLEPc-elaboration paragraph spans 330-344), the cycle-014 audit report at `reports/2026-05-28T193309Z-lowering-verifier-.../CYCLE.md` exists, and the carry-forward OQ slug `partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping` is present at `scaffolding/open-questions.md:2689` (status `open`). The insertion point is precise: cycle-014 audit YAML block closes at line 310, `## Status` heading is at line 312 — the new subsection lands between them, inside `## Verified-against` (section at line 235). The slight naming variation (Summary says "append to `## Verified-against`"; Proposed-changes says "after the cycle-014 audit block") is internally consistent, not contradictory — the cycle-014 block is the terminal content of `## Verified-against`.

**edge-label-fidelity — pass.** The edge label is L1>L0; the prose discusses exactly the L1 `EigStatus` (the L1 form) lowering to L0 SLEPc source patterns (the reason print-sites + count-readers). The lowering direction is narrated forward (L1 reason→status map lowering into L0 source), consistent with the high→low invariant. No edge mismatch.

**plan-kind-consistency — pass.** This was a focus question. The declared work product is a `partly-constructive` re-verification / audit-record append — NOT a fresh `theme` authoring. The content shape matches exactly: the file already exists (cycle-013 authored, cycle-014 integrated), so re-authoring would duplicate. The producer's chosen kind — an append-only re-verification subsection with a `verified_against` block, no status change — is the correct shape given the discovery that the target already exists. The partly-constructive discipline is honored: (i) constructive sub-part named (the per-row `EigStatus` assignment for the 8 diverged-family rows; the 2 converged rows are count-anchored, NOT constructive); (ii) negative-anchor citations given and re-confirmed; (iii) a single global promotion condition stated (a `EPSGetConvergedReason` read feeding outer-loop status, currently absent). The negative-anchor-vs-positive-claim distinction is explicitly honored (lines 167-171, 161-171): the report states the negative anchor is "evidence FOR the reconstruction being faithful; it does NOT license asserting Palace produces the reason→status discrimination today." The status correctly STAYS `partly-constructive` (no positive site exists to gate promotion against). The `verified_against` block is fenced YAML per cycle-003 format discipline (mirroring the cycle-014 audit block's same convention; zero-width-space-guarded in the report, real triple-backtick `yaml` fences in the emitted file).

**skill-uptake-survey — pass.** The report's shape (citation re-verification of an existing partly-constructive entry) implies `verify-citation-range` and the partly-constructive audit machinery. The producer references `mcp__palace-codemap__read_range` / `search_text` for the re-reads (MCP-first localization, per the codified invariant) and follows the abstractor §Discipline partly-constructive 4-point checklist explicitly (lines 138-187). Pure presence check; telemetry positive. No skill-friction surfaced.

### Issues found

1. **`GetConverged` count-reader list mixes solver-family and SVD/helper sites without disambiguation** — `reports/.../CYCLE.md` §Summary point 2 (lines 49-51), §"Partly-constructive sub-part" (ii) (lines 164-166), §"Supporting evidence" (lines 217-219), and the proposed `verified_against` note (line 113). The list `slepc.cpp:{276,310,695,1178,1525}` is presented as the eigensolver count-readers, but line 310 is `SVDGetConverged` (an SVD spectral-estimation helper, line 305-312 context confirms `SVDSolve`/`SVD_STANDARD`) and line 276 is an `EPSGetConverged` in a separate helper distinct from the line-695 `SlepcEPSSolverBase::Solve` body site. **Severity: low / cosmetic.** The negative-anchor claim ("no `*GetConvergedReason` accessor anywhere") is fully upheld — including extra `*GetConverged` count-reader sites is conservative and does not weaken the anchor. A one-clause disambiguation (e.g., "{695,1178,1525} in the three Solve() bodies; {276,310} in spectral-estimation helpers (276 EPS, 310 SVD)") would make the citation list self-documenting. Candidate for repair but does not change any verdict.

2. **Internal naming variation for the append target (cosmetic)** — §Summary (line 62, "append-only edit … to `## Verified-against`") vs §Proposed changes (lines 77-80, "after the closing ``` of the cycle-014 `### Lowering-verifier audit (cycle-014)` YAML block"). **Severity: very low.** These are consistent (the cycle-014 audit block is the terminal content under `## Verified-against`, lines 269-310, immediately before `## Status` at 312), but a reader scanning quickly might think two different targets are named. Optional repair: state both facts in one place ("under `## Verified-against`, after the cycle-014 audit block at line 310"). No correctness impact.

No citation-validity, surface, rotation, variant-coverage, cross-reference, edge-label, or plan-kind failures or warnings found. Both issues are cosmetic precision/clarity notes on an otherwise clean, fully-verified re-verification report.

## Repair

### Fixes attempted

- **Finding 1**: `GetConverged` count-reader list `slepc.cpp:{276,310,695,1178,1525}` lumps `SVDGetConverged@310` and the separate-helper `EPSGetConverged@276` in with the three `Solve()`-body sites without disambiguation (critic Issue 1; low / cosmetic; does not weaken the anchor).
  - **Decision**: repaired.
  - **Action**: Applied a one-clause disambiguating split to all four occurrences of the count-reader list in `CYCLE.md` — §Summary point 2 (lines ~49-53), §"Partly-constructive sub-part" (ii) (lines ~166-170), §"Supporting evidence" Negative-anchor block (lines ~217-221), and the `verified_against` YAML note (line ~113, the text the integrator emits into the artifact). Each now reads "{695,1178,1525} in the three `Solve()` bodies, plus {276,310} in spectral-estimation helpers — 276 EPS, 310 SVD". The disambiguation facts came directly from the critic's own independently-verified findings (META line 23 / Issue 1), so this was mechanical — no new content authored.
  - **Rationale**: in scope as a "citation line range / list self-documenting" mechanical clarification; the set membership is unchanged, only the per-element provenance is now annotated.

- **Finding 2**: internal naming variation for the append target — §Summary says "to `## Verified-against`"; §Proposed-changes says "after the cycle-014 audit block (line 310)" (critic Issue 2; very low; consistent but could be stated once).
  - **Decision**: repaired.
  - **Action**: Edited the `edit:`-directive header in §Proposed-changes (`CYCLE.md` lines ~76-81) to state both facts in one place — "append under `## Verified-against` — specifically, immediately AFTER the closing of the cycle-014 audit YAML block (the terminal content of `## Verified-against`, current line 310)". No change to the insertion point itself (line 310, before `## Status` at 312); only the description now unifies the two phrasings.
  - **Rationale**: in scope as a trivial clarity/consistency fix to the report's own prose; the append target was always one location, the edit just makes that explicit.

### Unrepairable findings

None. Both flagged issues were optional cosmetic polish and were trivially surgical to apply; the critic found all 8 checks `pass` with no verdict-changing concerns.

## Suggested resolution

`ready`. Integrator notes:
- The single proposed change is an append-only `### Re-verification (cycle-016 abstractor)` subsection under `## Verified-against` in `book/src/L1-L0/eigsolve-convergence-reason-mapping.md`, inserted between the cycle-014 audit YAML block (closes line 310) and the `## Status` heading (line 312). No status change; status correctly STAYS `partly-constructive`.
- Emit the `verified_against` block with real triple-backtick `yaml` fences (the report's fences are zero-width-space-guarded per the cycle-014 audit-block convention).
- Per §Open-questions, mark OQ `partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping` (`scaffolding/open-questions.md:2689`) closed/answered — this dispatch is the third independent confirmation of the negative anchor (ENTRY case).
- No edit to `book/src/SUMMARY.md` or `book/src/L1-L0/index.md` (both already present/correct, cycle-013/014).
