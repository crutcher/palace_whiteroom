---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T200500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: warning
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T201500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of lowering-verifier audit — eigsolve-convergence-reason-mapping (partly-constructive promotion gate)

## Critique

### Checks run

**citation-validity — pass.** Every positive citation re-checked. `read_range slepc.cpp:693-709` independently confirms `EPSGetConverged`@695, the print-guarded `EPSConvergedReasonView`@699 (inside `if (print > 0)`), and `return (int)num_conv`@708 — exact. The PEP/NEP body claims (1178/1182/1191, 1525/1529) are isomorphic in shape and the report's read_range notes are consistent with the search-hit lines. **The load-bearing negative anchor was independently re-run via `palace-codemap search_text` this critique**: `EPS_DIVERGED` → `[]`, `EPS_CONVERGED` → `[]`, `GetConvergedReason` → `[]`, `DIVERGED` → `[]`, and `ConvergedReason` → exactly the three print-only `*ConvergedReasonView` sites `slepc.cpp:{699,1182,1529}`. **Zero materialization independently CONFIRMED.** The partly-constructive status rests on a verified foundation.

**surface-or-evidence — pass.** This is a partly-constructive ENTRY audit (retroactive-evidence backfill, gated). The report proposes no surface edit it enacts; the one tightening (a `verified_against` block) is explicitly GATED to a follow-up dispatch, not applied here. This is the allowed retroactive-evidence shape — the audit confirms the negative anchor that grounds the existing surface rather than asserting a new positive claim without a site. No pure-rotation-without-surface violation.

**rotation-quality — pass (not the primary axis).** No new rotation is asserted; the audit verifies an existing structural (enum-partition + per-family-isomorphism) justification. The report correctly characterizes the kind as `structural` + per-row `partly-constructive`, not an algebraic/reduction rotation. Applicable only insofar as the existing entry's compaction claim (one global gate covering 8 rows, PEP non-additive) is preserved — it is.

**variant-axis-coverage — warning.** The orthogonal axes (EPS / PEP / NEP family × converged/diverged partition) are covered, and ARPACK / `QuasiNewtonSolver` are explicitly scoped out (Applicability Condition 1). The exhaustiveness gate, however, rests on a SLEPc enum the report itself flags as NOT vendored under `reference/` — so the 8-row "EXHAUSTIVE" verdict is checked against documented SLEPc docs, not a positive source site. The caveat IS disclosed (Open-questions §1, the `partially-supports` verdict on that proposed row, and §"Exhaustiveness"). Disclosure is adequate and honest; the warning flags that one axis (enum-completeness) is literature-anchored not source-anchored — a real residual the repairer/integrator should note, not a defect in framing.

**cross-reference-integrity — pass.** `book/src/L1/eigsolve.md` (the `EigStatus` target) and parent `book/src/L1-L0/eigsolve-mutation-rotation.md` (Sub-pattern B/C forwarding) both exist and are referenced consistently with the live artifact; the entry's `EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed` matches. The audit declares the parent cross-reference "accepted as inherited" (not re-read) — acceptable for an audit, transparently flagged.

**edge-label-fidelity — pass.** The theme is L1>L0; all prose discusses the L1 `EigStatus` derivation ← L0 SLEPc reason. Directionality is forward (L1 narrated, L0 source cited); the "Materialisation shape (forward-looking)" section is correctly framed as the not-yet-in-Palace promotion target, not a reverse-lift narration. Open-questions §3 explicitly re-affirms this. No edge mismatch.

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit with verdict NEGATIVE-ANCHOR-CONFIRMED → STAYS-PARTLY-CONSTRUCTIVE. Content shape matches: per-citation audit, applicability conditions, exhaustiveness gate, gated (not enacted) tightening. The verdict correctly does NOT unblock (no positive site exists to firm against) — distinct from cycle-012's UNBLOCK, and the report names that distinction. This is the correct partly-constructive ENTRY verdict and correctly validates the ENTRY mechanism complementing cycle-013's EXIT.

**skill-uptake-survey — warning.** The audit shape implies `verify-citation-range` (extended cycle-012 with an "Audit-report / inherited-citation sub-case") and `verify-refinement-surface`; neither invocation is referenced by name. Telemetry only — non-blocking. MCP-first localization IS evidenced (read_range / search_text), consistent with the codified preference.

### Issues found

1. **Enum exhaustiveness is literature-anchored, not source-anchored** (CYCLE.md §"Exhaustiveness of the 8-row count" + Open-questions §1). The "8-row count HELD / EXHAUSTIVE" verdict is verified against SLEPc's *documented* enum because SLEPc/PETSc headers are not vendored under `reference/`. Severity: low. Adequately disclosed (caveat stated three times; the proposed `verified_against` row carries `partially-supports`). It does not weaken the partly-constructive status (which rests on the Palace-side negative anchor, independently re-confirmed here) — it bounds only the enum-coverage half. Candidate for the repairer only as a disclosure-tightening, not a correctness fix.

2. **Inherited cross-references not re-verified** (CYCLE.md §"Supporting evidence": `book/src/L1/eigsolve.md` and parent `eigsolve-mutation-rotation.md` "not re-read this audit"). Severity: very low. Both targets exist and are internally consistent with the entry; flagged transparently. Acceptable for an audit-scoped dispatch.

3. **No explicit skill-invocation reference** for the audit-citation sub-case of `verify-citation-range` / `verify-refinement-surface`. Severity: informational (telemetry). Non-blocking.

**Independent confirmation statement:** I re-ran all four negative-anchor `search_text` queries (`EPS_DIVERGED`, `EPS_CONVERGED`, `GetConvergedReason`, `DIVERGED` → all zero; `ConvergedReason` → only the 3 print-only Views) and re-read `slepc.cpp:693-709`. Zero materialization sites independently CONFIRMED; the STAYS-PARTLY-CONSTRUCTIVE verdict is correct and the partly-constructive ENTRY mechanism is validly demonstrated.

## Repair

### Fixes attempted

- **Finding**: variant-axis-coverage (warning) — the 8-row enum-exhaustiveness "HELD / EXHAUSTIVE" verdict is literature-anchored (checked vs SLEPc's documented enum, not a vendored header). The caveat was disclosed downstream (§"Exhaustiveness", Open-questions §1, the `partially-supports` proposed row) but the top-level Summary/verdict stated the count "HELD as exhaustive over SLEPc's documented enum" without flagging that the enum-coverage half is a literature anchor rather than a source anchor.
  - **Decision**: repaired.
  - **Action**: surgical wording tightening in `CYCLE.md` §Summary. The verdict now states the 8-row count was "checked against SLEPc's DOCUMENTED enum (a literature anchor; SLEPc/PETSc headers are not vendored under `reference/`), NOT a vendored positive source site," explicitly contrasts the literature-anchored enum-coverage half against the source-confirmed Palace-side negative anchor, and adds an explicit cycle-015 meta-phase flag for the ENTRY+EXIT validation pairing. No content authored — only made the already-disclosed basis-of-exhaustiveness visible at verdict level (where the integrator/meta-phase reads it). Axes themselves were already correctly enumerated (EPS/PEP/NEP × converged/diverged, ARPACK/QuasiNewtonSolver scoped out); no classification change.

- **Finding**: skill-uptake-survey (warning) — no explicit by-name reference to `verify-citation-range` (audit/inherited sub-case) or `verify-refinement-surface`.
  - **Decision**: not-needed (telemetry only, non-blocking per critique). MCP-first localization is already evidenced (read_range / search_text). No edit; no fabricated skill-invocation claim.

### Unrepairable findings
None. Both warnings are disclosure-level; the substantive verdict (NEGATIVE-ANCHOR-CONFIRMED → STAYS-PARTLY-CONSTRUCTIVE) was independently re-confirmed by the critic (zero materialization). No substantive authoring or contradiction-resolution required; no follow-up agent.

## Suggested resolution

`ready`. Notes for the integrator:
- This report does NOT enact any artifact edit — the verdict is "STAYS partly-constructive, promotion NOT unblocked." The single proposed `verified_against` block is explicitly GATED (route to a follow-up abstractor/lifter dispatch); the integrator should NOT apply it as part of this report's proposed-changes, and should preserve the gating note when staging.
- Surface the cycle-015 meta-phase flag (now in the CYCLE.md Summary): this is the partly-constructive ENTRY case (status correctly STAYS), complementing cycle-013's eigsolve EXIT case (status promoted) — together they validate the partly-constructive mechanism as a working transient gate.
- Residual to carry forward: enum exhaustiveness is literature-anchored (SLEPc headers not vendored). Low risk; bounds only the enum-coverage half, not the partly-constructive status. A candidate OQ if not already tracked.
