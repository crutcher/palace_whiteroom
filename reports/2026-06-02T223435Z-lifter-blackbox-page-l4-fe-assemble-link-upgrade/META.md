---
verifies: ./CYCLE.md
critiqued_at: 2026-06-02T22:48:08Z
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
repaired_at: 2026-06-02T22:55:00Z
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

# META: verification of "Re-anchor black-box-vs-accelerated-kernels page → L4/fe_assemble"

## Critique

### Checks run

**citation-validity — pass.** `python3 tools/citecheck/citecheck.py --scan` over CYCLE.md returns `5 ok, 0 failing`; no bounds/path drift. The two load-bearing pinpoints both clear `--anchor`: `L4/fe_assemble.md:167-171 --anchor 'firm'` (anchor at lines 169/171, in-range — `## Status: firm` confirmed) and `L4/fe_assemble.md:169 --anchor 'canonical L4 assemble-construction shape'` (in-range). The "firm since cycle-068" provenance is corroborated by the file's own `## Status` prose (line 169: "This dispatch (cycle-068 D1)…rank-1 FE-cohort→L4 lift"). The supporting-evidence claim that `L4/fe_assemble.md` frontmatter `consumes:` names the concept page is true (line 7: `book/src/concepts/black-box-vs-accelerated-kernels.md (… disposition, case 1)`), so the back-link this pass completes is already declared from the L4 side. No `verified_against:` block in this report, so that sub-check is not applicable. Every claim carries a citation that resolves in-range.

**surface-or-evidence — pass (not a refinement proposal).** This is a cosmetic cross-reference link-upgrade on a concept page, not a modification to an operator/theme's surface text and not a rotation_claim. No rotation evidence is owed; the "risen" word-tightening is a one-word prose touch on a concept page, backed by the cited L4 rise claim (`L4/fe_assemble.md:169`). Check no-ops on this report shape.

**rotation-quality — pass (not applicable to a link-upgrade).** The report asserts no algebraic/structural/reduction rotation; it re-points two existing forward-references. No L_{n+1}→L_n compaction claim is made.

**variant-axis-coverage — pass (not applicable).** No operator/theme with orthogonal variant axes is introduced or modified. The two upgraded references are the complete set of `../L1/fe_assemble.md` links on the page (`grep` confirms exactly lines 69 and 143 carry `L1/fe_assemble`), so there is no hidden third occurrence left un-upgraded.

**cross-reference-integrity — pass.** Both upgraded targets resolve: `book/src/L4/fe_assemble.md` exists on disk (45 KB, mtime 2026-06-02). The `[old]` strings match the page byte-for-byte at lines 68-73 (case-1 sibling list) and 143-144 (See-also). The page convention is confirmed: the three sibling case-1 black-box kernels link `../L4/` — `eigsolve` (`../L4/eigsolve.md`, line 62), `ksp_solve` (`../L4/ksp_solve.md`, line 67), `fold_solve` (`../L4/fold_solve.md`, line 74) — so re-pointing `fe_assemble` at `../L4/` makes the case-1 set uniform rather than introducing an outlier. The old `../L1/fe_assemble.md` remains reachable via the L4 entry's own lowering chain (not orphaned). No firm-body-inside-fence concern — this report makes no `firm` chapter claim; it consumes an already-firm chapter.

**edge-label-fidelity — pass (not applicable).** No lowering edge label (L_{n+1}→L_n) is carried; this is a concept-page edit, and the report's own discipline note correctly observes there is no high→low direction concern.

**plan-kind-consistency — pass.** Declared as a lifter re-anchor / link-upgrade ("Pure cross-ref completion; no structural change"). The content shape — two `[old]/[new]` link swaps plus a one-word tightening — matches a cosmetic re-anchor exactly. No firm/rough-in placeholder mismatch.

**skill-uptake-survey — pass.** The report cites the relevant skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (Summary + per-occurrence judgment). The shape (existing reference re-pointed to a now-on-disk firm target) is precisely that skill's domain; uptake is surfaced. (Telemetry note: the skill name literally reads "plain-text-ref-to-live-link," whereas this case upgrades a live-link L1 target to a live-link L4 target — a sibling sub-case of the same procedure, not the verbatim plain-text→link case. Non-blocking; the skill is the right family.)

### Issues found

No blocking or substantive issues. All eight checks pass.

Minor / informational (candidates, not defects):

1. **Skill-name vs. operation mismatch (informational, `book/src/concepts/black-box-vs-accelerated-kernels.md`, CYCLE.md Summary).** The invoked skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` names the *plain-text → live-link* case, but both edits here re-point an *existing live link* (`../L1/fe_assemble.md` → `../L4/fe_assemble.md`). The skill family is correct (on-disk target now reachable), but the precise sub-case is "live-link re-anchor to a newly-firm higher target," not plain-text upgrade. Surfacing only — does not affect correctness of the edit.

2. **Judgment soundness — confirmed, not an issue.** Per the verification ask: both occurrences sit in case-1 of the black-box/accelerated taxonomy (ops that RISE to L4), and the surrounding prose at both sites explicitly narrates the rise ("rises as an opaque-surface **input** to the assemble combinator" at :68-73; "the assemble fold (combinator, **rises**)" at :143-144). The L4 feature surface is the intended referent at both spots, not the L1 pure-function cap. The `../L4/fe_assemble.md` rise claim (`:169`, "canonical L4 assemble-construction shape" + the combinator-rises / leaf-rises-as-input disposition at `:173`) backs the "risen assemble combinator" tightening. No site was found where the L1 cap was specifically meant. The L1 cap is not orphaned (still the firm lower home, reachable via the L4 lowering chain).

## Repair

### Fixes attempted

The critic passed all 8 checks (no warning/fail findings). No finding is in scope for repair.

- **Finding**: Skill-name vs. operation mismatch (informational) — `upgrade-plain-text-ref-to-live-link-when-target-on-disk` names the plain-text→live-link case, while these edits re-point an existing live link L1→L4.
  - **Decision**: not-needed
  - **Rationale**: The critic explicitly classified this as informational/telemetry, NOT a defect — the skill is the correct family (on-disk target now reachable), only a slightly-off sub-case name. No edit is owed; touching the report to "fix" a non-defect would author content, not repair it.

All 8 checks → `pass` (from critic); no repairable findings → repairs frontmatter records `not-needed` across the board.

### Unrepairable findings

None.

## Suggested resolution

`ready`. This is a clean cosmetic cross-reference link-upgrade (two `../L1/fe_assemble.md` → `../L4/fe_assemble.md` re-points + a one-word "risen" tightening), all citations resolve in-range, and the case-1 sibling set is now uniform on `../L4/`. The integrator may apply the report's proposed-changes as-is. The single informational skill-name note is telemetry for the meta-phase (whether the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill should grow an explicit "live-link re-anchor to newly-firm higher target" sub-case), not a blocker.
