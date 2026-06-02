---
verifies: ./CYCLE.md
critiqued_at: 2026-06-02T085500Z
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
repaired_at: 2026-06-02T090000Z
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

# META: verification of L1 index §Vocabulary-cohort count prose refresh (count-owner)

## Critique

### Checks run

**citation-validity — pass.** The report makes count claims, not source claims; its "citations" are
on-disk `## Status` lines and dep-map rows. All verified mechanically: I read `book/src/L1/index.md`
in full and confirmed the on-disk dep-map holds exactly **29 `firm` rows** (the report's claimed
pre-D3 count). The 29 enumerate cleanly as 26 main-cohort (`axpy`…`floquet-correction`) + 3 in-table
FE-assembly (`eliminate_rhs`, `eliminate_essential_bc`, `weak_form_term`). All four FE-assembly
chapters (`fe_assemble.md`, `weak_form_term.md`, `eliminate_essential_bc.md`, `eliminate_rhs.md`) carry
`firmness: firm` frontmatter AND a `## Status` line reading ``firm``/`PROMOTE` on disk — the
count-by-`## Status` discipline (c057-meta count-owner guard) is correctly applied, not sourced from
index cells. The two `[old]` anchor strings in the proposed-changes blocks match index.md lines 31 and
70 verbatim, so both edits will apply cleanly.

**surface-or-evidence — pass (not a refinement).** This is a count/prose-hygiene refresh of header text,
not a refinement of an operator/theme surface with a rotation_claim. The retroactive-evidence framing
applies: the edit reconciles already-firm chapter statuses with stale derived header prose. No surface
modification to an algebraic body. No-op for this report-kind.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted by
this report. The `assemble_frequency_operator` rotation (operand-category axis on `linear_combination`)
belongs to D3, which this report explicitly does NOT touch. No-op.

**variant-axis-coverage — pass (not applicable).** No new operator with variant axes is introduced. The
report correctly characterizes `assemble_frequency_operator` as a `linear_combination` operand-category
specialization and `weak_form_term`'s differential-operator axis is D1/D3 surface, not touched here.
No-op.

**cross-reference-integrity — pass.** The live links introduced in the new header prose resolve:
`../L2/linear_combination.md` EXISTS on disk; the FE-assembly subsection's `../L1-L0/fe-operator-assemble-mutation-rotation.md`
and `../L1-L0/fe-assemble-libceed-boundary-obstruction.md` both EXIST (carried over from the `[old]`
text, unchanged). Critically, `assemble_frequency_operator` is rendered as **plain-text backticks**, NOT
a live link, in the new grand-total header — correct, because `L1/assemble_frequency_operator.md` is NOT
yet on disk (D3 not yet applied); a live link would be a `linkcheck2` build break. This respects the
`rough-in-forward-reference-must-be-plain-text` convention. No firm-body-inside-fence concern (this is
prose, not a `## Status`+Signature+Laws+Evidence body).

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried by this report.
No-op.

**plan-kind-consistency — pass.** Declared kind is a count-owner / layer-intro prose refresh, and the
content matches exactly: only the two §Vocabulary-cohort header-prose counts are edited (grand-total
header line 31; FE-assembly sub-spine subsection header line 70). The report correctly does NOT touch
D3's own dep-map row / cohort bullet / SUMMARY lines, nor D1's `weak_form_term` body. Scope discipline
is clean and explicitly stated (§Open questions / caveats "Scope discipline").

**skill-uptake-survey — pass.** No dedicated count-owner / index-tally skill exists under `skills/`
(confirmed by directory scan); the relevant procedure is the c057-meta count-owner guard
(count-by-`## Status`, index-cell anti-drift), which the report references by name and applies. Nothing
blocking; telemetry only.

### Issues found

**Arithmetic verified correct — no blocking issues.** I independently re-derived the grand total by both
routes the report claims:

- **Cohort route:** 27 main-cohort (26 existing main on disk + `assemble_frequency_operator` landing via
  D3) + 4 FE-assembly sub-spine (`fe_assemble` off-table + the 3 in-table) = **31**. ✓
- **Dep-map route:** 29 on-disk in-table firm rows + 1 (D3's `assemble_frequency_operator` row) = 30
  in-table firm rows, + 1 off-table `fe_assemble` (firm, no dep-map row) = **31**. ✓

Both routes agree at 31, with no double-counting (the 3 in-table FE rows are counted under "FE-assembly
4", not under "main 27"; the off-table `fe_assemble` is the +1 reconciler). The "was 30 after cycle-061"
intermediate (26 main + 4 FE) is consistent with the lag the report fixes: the on-disk header still read
29/3 while the actual firm count was already 30 after `weak_form_term` firmed at c061.

**(b) FE-assembly sub-spine = 4 — confirmed.** `fe_assemble` (c054), `weak_form_term` (c061),
`eliminate_essential_bc` (c055), `eliminate_rhs` (c055) all `firm` on disk. `assemble_frequency_operator`
correctly EXCLUDED — D3's report confirms it is the operator-operand specialization of
`linear_combination` (a fixed-operator-basis affine-in-ω fold), not a weak-form-term assembler; it is a
main-cohort operator, not FE-assembly. Exclusion rationale in the cohort narrative is accurate.

**(c) Reconciliation finding — accurate.** `fe_assemble` is referenced 9× in index.md (prose + links)
but has **no dep-map table row** (confirmed: it is absent from the enumerated firm-row list). So the
in-table firm-row count is genuinely one short of the grand total, and the +1 off-table reconciliation
is a real, correctly-described condition. The report's flag that a future pass add a `fe_assemble`
dep-map row (to make the table self-summing) is correctly scoped OUT of this count-owner dispatch
(adding a table row is not header-prose maintenance). Accurate and appropriately deferred.

**Minor (non-blocking) observation — the supporting-evidence dep-row enumeration count.** §Supporting
evidence line "**Dep-map firm-row count (on-disk, pre-D3):** ... → 29 firm rows" lists the 26 main
slugs then "+ `eliminate_rhs`, `eliminate_essential_bc`, `weak_form_term` (3 FE-assembly sub-spine
in-table)" = 29. This matches disk exactly. No discrepancy; noting only that the enumeration is correct
and complete (I cross-checked all 29 slugs against the grep). Not an issue.

**Frontmatter note (cosmetic, for repairer awareness).** The report frontmatter `status: pending`
(line 5) is the pre-critique value; no action needed from the critique side — flagged only so the
repairer/integrator pipeline tracks it. Not a content defect.

No warnings or failures. The report is arithmetically sound, scope-disciplined, and introduces no dead
links.

## Repair

### Fixes attempted

No findings to repair. All 8 critic checks returned `pass`. This is a status-setting pass only — clean
count-owner refresh, arithmetic independently re-verified by the critic (31 via both cohort and dep-map
routes, no double-counting). No mechanical fix was applicable; nothing in scope.

### Unrepairable findings

None.

## Suggested resolution

`overall_status: ready`. Integrator may apply the two §Vocabulary-cohort header-prose edits (grand-total
header line 31; FE-assembly sub-spine subsection header line 70) as-is.

**Integrator notes (no mutation by repairer):**

1. **Frontmatter `status: pending` (cosmetic).** The CYCLE.md frontmatter `status: pending` is the
   pre-critique value; the normal integrator/flow updates it. Carried for pipeline awareness only — not a
   content defect.

2. **OQ-intake note — `fe_assemble` has no dep-map row.** The critic correctly flagged (finding (c)) that
   `fe_assemble` is referenced 9× in `book/src/L1/index.md` but carries no dep-map table row, so the
   in-table firm-row count is one short of the grand total and is reconciled by the +1 off-table
   `fe_assemble`. This is real and correctly scoped OUT of this count-owner dispatch (adding a table row
   is not header-prose maintenance). The clean future fix is to add a `fe_assemble` dep-map row so the
   table self-sums to the grand total (30 in-table firm rows after D3's `assemble_frequency_operator`
   lands, plus the `fe_assemble` row = 31, eliminating the off-table reconciler). Suitable for
   open-questions intake; not blocking this report.
