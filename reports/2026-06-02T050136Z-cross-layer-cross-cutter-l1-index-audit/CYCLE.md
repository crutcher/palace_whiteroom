---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T050136Z
scope: L1↔L1-L0 cross-cut — L1 + L1-L0 index-table status-cell staleness audit
status: pending
integrated_at: 2026-06-02T053505Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-058 D4. OBSERVATION-ONLY (no book mutation; no proposed-changes block). Applied by integrator-per-report
  (staging row 4, last), housekept + committed by integrator-finalize. L1 + L1-L0 index-table status-cell staleness
  sweep → CONFIRM-CLEAN 68/68 (all 68 cells MATCH their chapter ## Status lines). Closes the L1/L1-L0 half of friction
  index-table-status-cell-drifts-when-theme-file-promoted (mirrors the c056 D2 16/16 CONFIRM-CLEAN on L3-L2/L2-L1). The
  qualifier-dropping coarse-cell/fine-chapter convention (firm (structural)→firm, obstruction (opaque-library-ownership)
  →obstruction) correctly judged a MATCH not drift. One optional batch-18 meta-phase codification intake routed (the
  minres/bicgstab umbrella-obstruction-vs-sub-tier index-cell wording — chapter-side cosmetic phrasing variance, out of
  scope for an index-staleness audit). Both D4 intake entries appended to scaffolding/open-questions.md by the dispatch
  agent. No count delta. Gate hits: n/a (no surface mutation).
---

# CYCLE: Cross-layer observation — L1 / L1-L0 index-table status-cell staleness audit

## Summary
Swept every index-table row in `book/src/L1/index.md` (the §"Operator dep-map" table, 36 rows) and `book/src/L1-L0/index.md` (the §"Theme list" table, 32 rows) and compared each row's status cell against the linked chapter's actual `## Status` line. **Verdict: CONFIRM-CLEAN — 68/68 rows agree.** Every index-cell status word matches its chapter's `## Status` category word. This closes the open L1 / L1-L0 half of friction `index-table-status-cell-drifts-when-theme-file-promoted`, mirroring c056 D2's 16/16 CONFIRM-CLEAN result on the L3-L2 / L2-L1 index tables. No `book/` mutation; no c059 lifter follow-up required.

## Observation kind
Consistency drift — **none found** (audit confirms clean). This is the highest in-place-promotion-churn drift sub-class: a stale status *word* in a table cell escapes the dead-link build check (`linkcheck2` catches dead links, not stale words), so it is the only index-drift class the build cannot self-detect. The c057-meta promotion-time guard prevents NEW drift prospectively; this audit confirms no historical residue accumulated before the guard landed.

## Specific finding
**L1/index.md §Operator dep-map (lines 84-119): 36 rows, all clean.** 30 rows link to L1 chapters; 6 obstruction rough-in rows link to L1-L0 themes. All match:
- 28 `firm` cells ↔ `firm` chapter Status (`axpy`, `dot`, `nrm2`, `axpby`, `scal`, `normalize`, `apply_linop`, `axpbypcz`, `ksp_solve`, `eigsolve`, `orthogonalize`, `chebyshev-smoother`, `divfree-projector`, `assemble-diagonal`, `apply_nonlinear_pencil`, `nleps_deflated_residual`, `lu_solve`, `nleps_deflated_solve`, `nleps_jacobian_action`, `nleps_eigenvalue_correction`, `back_solve`, `ls_update_column`, `jacobi-smoother`, `reciprocal`, `elementwise_product`, `floquet-correction`, `eliminate_rhs`, `eliminate_essential_bc`).
- `matrix-weighted-norm`: cell `rough-in (test-coverage-bounded, harvested-by: ...)` ↔ chapter `rough-in (test-coverage-bounded)` (`matrix-weighted-norm.md:110`). Match.
- `bilinear-form`: cell `rough-in (lower-layer-shared-vocabulary, harvested-by: ...)` ↔ chapter `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)` (`bilinear-form.md:321`). Match.
- 6 obstruction rough-in rows (`lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`, `bicgstab_step`, `omega_update`, `stabilisation_update`, lines 114-119): cell `rough-in (obstruction, proposed-by: ...)` ↔ parent obstruction-theme chapters. Match.

**L1-L0/index.md §Theme list (lines 18-49): 32 rows, all clean.**
- 26 `firm` cells ↔ `firm` chapter Status (every mutation-rotation theme except the obstruction/rough-in set). Note: several chapter Status lines carry a parenthetical qualifier the cell drops by table convention — e.g. `eigsolve-mutation-rotation` chapter says `firm (structural)` (`eigsolve-mutation-rotation.md:935`), cell says `firm`; `fe-operator-assemble-mutation-rotation` cell says `firm` (+ inline `*(firm c057; opened c053)*`), chapter says `firm` (`fe-operator-assemble-mutation-rotation.md:23`). The category word agrees in every case; the dropped parenthetical is the established cell-vs-chapter convention, not drift.
- `apply-linop-mutation-rotation`: cell `rough-in` ↔ chapter `rough-in` (`apply-linop-mutation-rotation.md:346`). Match.
- `ksp-solve-mutation-rotation`: cell `rough-in *(firmed cycle-008)*` ↔ chapter `rough-in` (`ksp-solve-mutation-rotation.md:764`). Match (the `*(firmed cycle-008)*` inline note refers to the L1 *operator* firming, not the *theme* status — the theme is genuinely still `rough-in`; this is a pre-existing semantic-note quirk, NOT a status-word mismatch).
- `eigsolve-convergence-reason-mapping`: cell `partly-constructive` ↔ chapter `partly-constructive (structural decomposition firm; per-row status...)` (`eigsolve-convergence-reason-mapping.md:352`). Match.
- `triangular-solve-obstruction`: cell `obstruction` ↔ chapter `obstruction` (`triangular-solve-obstruction.md:479`). Match.
- `fe-assemble-libceed-boundary-obstruction`: cell `obstruction` ↔ chapter `obstruction (opaque-library-ownership)` (`fe-assemble-libceed-boundary-obstruction.md:30`). Match (sub-kind qualifier dropped in cell per convention).
- `minres-iteration`: cell `obstruction` ↔ chapter `rough-in — sketched as obstruction ...` (`minres-iteration.md:153`). **See caveat below — judged a match (dual-classification convention), not drift.**
- `bicgstab-iteration`: cell `obstruction` ↔ chapter `rough-in (obstruction)` (`bicgstab-iteration.md:84`). **See caveat below — judged a match.**

## Recommendation
**Defer — no action.** Audit confirms clean; no c059 lifter dispatch needed. The friction `index-table-status-cell-drifts-when-theme-file-promoted` L1 / L1-L0 half is confirmed-clean and can be marked closed for these two tables (the c057-meta promotion-time guard now covers prospective drift). The one judgment call (minres/bicgstab umbrella-vs-sub-tier wording, below) is recorded as an OQ-ledger intake entry for the meta-phase to optionally codify — it is a naming-convention clarification, not a defect.

## Supporting evidence
- `book/src/L1/index.md:82-119` — §Operator dep-map table (status cells).
- `book/src/L1-L0/index.md:16-49` — §Theme list table (status cells).
- Chapter `## Status` lines confirmed via grep across `book/src/L1/*.md` and `book/src/L1-L0/*.md` (31 + 32 files; line anchors per file: e.g. `matrix-weighted-norm.md:108`, `bilinear-form.md:319`, `eigsolve-mutation-rotation.md:933`, `minres-iteration.md:151`, `bicgstab-iteration.md:82`, `fe-assemble-libceed-boundary-obstruction.md:28` — the `## Status` header line; the status word is on the +2 line).

## Open questions / caveats
- **minres-iteration / bicgstab-iteration umbrella-vs-sub-tier wording (judged match, flagged for optional codification).** The two index cells say `obstruction`; the two chapters say `rough-in — sketched as obstruction` (`minres-iteration.md:153`) and `rough-in (obstruction)` (`bicgstab-iteration.md:84`). I judge this a **match, not drift**, on two grounds: (1) `obstruction` is the established **umbrella category** word (CLAUDE.md "Obstruction themes have two sub-kinds" + L1/index.md §Vocabulary-cohort groups these under "Rough-in (obstruction)"); the chapters carry the finer `rough-in (obstruction)` sub-tier, and the cell carries the umbrella word — the same coarse-cell/fine-chapter convention the table already applies to `firm (structural)`→`firm` and `obstruction (opaque-library-ownership)`→`obstruction`. (2) The L1-L0 table column header is `status` and these two rows sit in the obstruction-theme cluster (rows 46-47, immediately above `triangular-solve-obstruction`), so the cell word is doing category-grouping work, not fine-status work. The minor inconsistency is that the *two* obstruction-theme chapters disagree with *each other* on phrasing (`rough-in — sketched as obstruction` vs `rough-in (obstruction)`) — a cosmetic chapter-side variance, not an index-cell-vs-chapter divergence, and therefore out of scope for this index-staleness audit. If the meta-phase wants the index cells to mirror the sub-tier exactly (`rough-in (obstruction)`), that is a convention change applying uniformly to the qualifier-dropping rows, not a one-off fix. Recorded as OQ intake.
- The `ksp-solve-mutation-rotation` cell's inline `*(firmed cycle-008)*` note is potentially misleading to a future reader (it could be misread as claiming the *theme* is firm, when the theme Status is genuinely `rough-in` and the note refers to the L1 *operator*). This is not status-cell drift (the status word `rough-in` is correct) — flagging only as a possible future clarity tidy, not an action item.
