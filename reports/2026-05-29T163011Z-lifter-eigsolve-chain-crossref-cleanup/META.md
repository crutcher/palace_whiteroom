---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T16:55:21Z
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
repaired_at: 2026-05-29T17:02:00Z
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

# META: verification of "Re-anchor eigsolve-chain cross-references" (cycle-026 dispatch-7)

## Critique

This is a pure cross-reference cleanup: 8 plain-text-forward-reference → live-link upgrades across 4 files (`L1/eigsolve.md` ×2, `L2/eigsolve.md` ×2, `L3/eigsolve.md` ×1, `L2/gram.md` ×3), plus one bounded one-adjective prose correction in block 1a. No structure / semantics / signature / L0-claim changes. The checks are adapted accordingly; the load-bearing check is cross-reference-integrity (do the three live-link targets exist and resolve under linkcheck2).

### Checks run

**citation-validity — pass.** Ran `tools/citecheck/citecheck.py --scan` on the CYCLE.md: **7 ok / 0 failing (7 citations checked)**, exit 0 — reproduces the report's "7 ok / 0 failing" claim exactly. The two load-bearing pinpoint citations were confirmed in-range and on-anchor: `L2-L1/eigsolve-spectral-transform-composition.md:362-365` lands on `## Status` (line 362) with ``firm`` at 364 (file is 437 lines); `L2-L1/gram-fold-specialization.md:386-389` lands on `## Status` (line 386) with ``firm`` at 388 (file is 532 lines). The `gram-fold-specialization.md:11-17` (points a/d) and `concepts/eigsolve.md:1-14` evidence citations both resolve in-range and the cited content matches the report's characterization.

**surface-or-evidence — pass (not a refinement-shaped proposal).** This is an explicitly-scoped pure cross-ref re-anchor, not a modification of operator/theme algebraic surface and not a rotation_claim. The one prose touch (block 1a "rough-in" → "firm") is a stale-self-description correction backed by the entry's own `## Status` (see plan-kind-consistency below). No surface/rotation obligation applies.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted; this is a reference-firming pass. Marked pass per the inapplicable-check convention.

**variant-axis-coverage — pass (not applicable).** No operator with variant axes is being authored or modified. Marked pass per the inapplicable-check convention.

**cross-reference-integrity — pass (LOAD-BEARING, fully verified).** All three live-link targets exist on-disk AND are wired into SUMMARY.md:
- `book/src/concepts/eigsolve.md` — exists; `SUMMARY.md:189` (`  - [eigsolve](./concepts/eigsolve.md)`). Targeted by blocks 1a/1b (from L1), 1c (from L2), 1d (from L3) via `../concepts/eigsolve.md`.
- `book/src/L2-L1/eigsolve-spectral-transform-composition.md` — exists; `SUMMARY.md:59`. Targeted by block 2 (from L2) via `../L2-L1/eigsolve-spectral-transform-composition.md`.
- `book/src/L2-L1/gram-fold-specialization.md` — exists; `SUMMARY.md:57`. Targeted by blocks 3a/3b/3c (from gram.md) via `../L2-L1/gram-fold-specialization.md`.

The report cited `SUMMARY.md:57,59,189` — all three confirmed at exactly those lines. Relative-path depth is correct: `book/src/L{1,2,3}/` → `../concepts/` and `../L2-L1/` (the same convention as the in-file `../concepts/solve-monad.md` links); `book/src/L2/gram.md` → `../L2-L1/`. No live link points at a missing file, so linkcheck2 will not break. The two deliberately-left-plain-text targets were confirmed genuinely absent: `book/src/L4/eigsolve.md` MISSING; no `eigsolve` theme in `book/src/L3-L2/` (the L3>L2 reference). Leaving those plain-text is correct, not a missed upgrade.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is asserted by this report. The block headers name the file/section being edited, and each block's new prose names the correct adjacent edge (L2>L1 spectral-transform in block 2; L2>L1 gram-fold-specialization in blocks 3a-c) — consistent with the targets. No mismatch.

**plan-kind-consistency — pass.** Declared shape is a lifter cross-ref re-anchor sweep; content matches (mechanical plain-text→live-link upgrades + tense adjustment). The one content correction (block 1a: "The L1 entry here is the **rough-in** operator definition" → "**firm**") is accurate and in-scope: `book/src/L1/eigsolve.md:167` `## Status` is ``firm`` (cycle-022 route-(b) law-confidence re-eval, promoted from `rough-in (test-coverage-bounded)`), so the old "rough-in" self-description was a genuinely stale/drifted claim in a firm entry. The fix is one adjective in the same sentence already being re-anchored, disclosed explicitly in §Discipline-notes under `lifter-scope-content-correction-boundary` — bounded, evidenced, not silent, not a re-architecture. This is within lifter scope, not an overreach.

**skill-uptake-survey — pass.** The report references the relevant skill discipline (`upgrade-plain-text-ref-to-live-link-when-target-on-disk` is the governing skill for this exact shape; the OQ entries that scheduled this work name it by slug, and the report's §Discipline-notes invoke the `lifter-scope-content-correction-boundary` discipline). Skill uptake is surfaced. Telemetry only; non-blocking.

### Issues found

No blocking issues. All 8 `[old]` strings verified verbatim single-occurrence on-disk (grep count = 1 each), and the multi-line blocks (3a at `gram.md:35-38`, 3b at `:174-176`, 3c at `:242-246`) match byte-for-byte including indentation — so the exact-string apply will match. All three OQ closures are justified (see below).

Two minor, non-blocking notes for the repairer/integrator (neither is a defect; recorded for completeness):

1. **`concepts/eigsolve.md` has no `status:` frontmatter field.** The report's frontmatter line 11 labels the target "firm", and §"Verification record" calls it "`status: firm`-equivalent". Verified: `concepts/eigsolve.md` carries no `status:` field at all (concept pages are navigational, not status-bearing — the page's own prose at `:1-14` says "does **not** restate the algebraic laws ... if this page and any L_n entry disagree ... the L_n entry wins"). The report's own §Verification-record correctly hedges this as "firm-equivalent (firm chain navigational home)", so this is loose-but-harmless wording in the frontmatter, not a false claim. No edit required; the new prose ("navigational/conceptual home") is accurately grounded by the page.

2. **OQ closures span a superset of the named OQ line-anchors (justified, not over-reach).** The third OQ (`concepts-eigsolve-page-still-absent` residual, open-questions.md:736) names the L1 §Context, L2 §Dependencies/§Cross-cutting, and L3 §Context mentions — blocks 1a/1c/1d. The report ALSO upgrades block 1b (an additional `concepts/eigsolve.md` mention in L1 §Supporting-evidence) under the same close. Similarly the gram OQ (:802) names `:176` + `:242-246`; the report also catches a third "forthcoming theme" mention at `gram.md:38` (block 3a). Both are supersets that fully discharge the named OQ and additionally clear sibling stale mentions in the same file — strictly correct and within the cleanup's intent (leaving a residual stale mention of the now-existing target would itself be drift). Closures justified; the integrator should note the superset when migrating the OQs to the Closed index so no orphan stale mention is assumed to remain.

The report correctly LEFT plain-text: the L4-surface mentions (`L4/eigsolve.md` unauthored — MISSING confirmed) and the L3>L2 eigsolve theme reference (no `L3-L2/eigsolve*` on disk — confirmed). Those are genuine absences, so plain-text-defer is the right call there, not a missed upgrade.

## Repair

All 8 critic checks are `pass`. No warning/fail findings to repair. This pass records the per-check disposition, applies the one mechanical frontmatter fix in repair scope (stale report-pointer), and confirms the critic's two non-blocking notes require no action.

### Fixes attempted

- **Finding**: Stale `verifies:` frontmatter pointer — META.md line 2 read `verifies: ../REPORT.md`, but the per-dispatch report file is `CYCLE.md` (the cycle-004 rename convention; this dir contains `CYCLE.md`, not `REPORT.md`).
  - **Decision**: repaired
  - **Action**: `META.md` frontmatter line 2 — `verifies: ../REPORT.md` → `verifies: ../CYCLE.md`. Mechanical pointer fix within repair authority (trivial cross-reference fix to a renamed file); does not touch any check value or report content.

- **Finding** (critic note 1): `concepts/eigsolve.md` has no `status:` frontmatter field; the report's frontmatter line 11 labels the target "firm".
  - **Decision**: not-needed
  - **Rationale**: The critic explicitly graded this loose-but-harmless and "No edit required" — concept pages are navigational, not status-bearing, and the report's §Verification-record correctly hedges the label as "firm-equivalent (firm chain navigational home)". The `inputs:` frontmatter line is a descriptive provenance annotation on a producer report, not a claim in the artifact, and is not edited post-critique. Correcting it would be cosmetic churn on a non-defect; out of mechanical repair scope and not a defect to fix.

- **Finding** (critic note 2): OQ closures span a justified superset of the named OQ line-anchors (blocks 1b/3a clear additional same-file stale mentions beyond the literal anchors).
  - **Decision**: not-needed
  - **Rationale**: The critic graded the superset "strictly correct and within the cleanup's intent" — leaving a residual stale mention of a now-existing target would itself be drift, so the broader sweep is the right outcome, not an over-reach. This is an integrator hand-off note for the Closed-index migration (so no orphan stale mention is assumed to remain), not a repairable defect. OQ-ledger writes are integrator authority, not repairer authority.

### Per-check dispositions

- citation-validity: not-needed (pass; citecheck 7 ok / 0 failing reproduced; two pinpoint citations on-anchor)
- surface-or-evidence: not-needed (pass; pure re-anchor, no refinement-shaped proposal)
- rotation-quality: not-needed (pass; no rotation asserted)
- variant-axis-coverage: not-needed (pass; no operator authored/modified)
- cross-reference-integrity: not-needed (pass; LOAD-BEARING — all 3 live-link targets on-disk + SUMMARY.md 57/59/189; both deliberately-plain-text targets confirmed absent)
- edge-label-fidelity: not-needed (pass; adjacent-edge labels in new prose consistent with targets)
- plan-kind-consistency: not-needed (pass; bounded "rough-in"→"firm" prose correction accurate per `L1/eigsolve.md:167` §Status and within lifter scope)
- skill-uptake-survey: not-needed (pass; `upgrade-plain-text-ref-to-live-link-when-target-on-disk` discipline surfaced)

### Unrepairable findings

None. No finding exceeds repair authority; nothing routed for follow-up.

## Suggested resolution

`overall_status: ready` — all 8 checks pass; the single mechanical fix (stale `verifies:` pointer) is applied; the critic's two notes are non-defects requiring no edit.

Notes for the integrator (carried forward from the critic, not repair actions):
- This is a pure cross-ref re-anchor: 8 `[old]`→`[new]` live-link upgrades across 4 files (`L1/eigsolve.md` ×2, `L2/eigsolve.md` ×2, `L3/eigsolve.md` ×1, `L2/gram.md` ×3) + one bounded in-scope "rough-in"→"firm" prose correction (block 1a). All 8 `[old]` strings verified verbatim single-occurrence on-disk, so the exact-string apply matches.
- The three OQ closures are justified, and **blocks 1b / 3a discharge a superset** beyond the literal OQ line-anchors (an extra `concepts/eigsolve.md` mention in L1 §Supporting-evidence; an extra "forthcoming theme" mention at `gram.md:38`). When migrating these OQs to the Closed index, note the superset so no orphan stale mention is assumed to remain in those files.
- The L4-surface mentions (`L4/eigsolve.md` unauthored) and the L3>L2 `eigsolve` theme reference are correctly left plain-text (genuine absences) — not missed upgrades; the L4 eigsolve-surface OQ stays open pending a future L4 dispatch.
