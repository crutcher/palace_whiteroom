---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T201500Z
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
repaired_at: 2026-05-29T202000Z
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

# META: verification of "Audit back_solve" (lowering-verifier L1 firm-leaf audit)

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` on the full CYCLE.md returns 34 ok / 0 failing — every citation is in-bounds and path-clean. I then ran `citecheck --anchor` on all 17 Palace pinpoints (the load-bearing ones) and all 4 intra-book pinpoint/range citations. Every one of the 17 Palace anchors returns `[ok]` at the exact cited line — **zero drift confirmed mechanically**, matching the report's central no-drift assertion. The cycle-027 codemap +1 brace-boundary hazard did NOT recur: e.g. `:653 for (int i = j` → ok at 653, `:656 s[i] /= Hi[i]` → ok at 656, `:831 Reconstruct the solution` → ok at 831, `:843 x.Add(s[k], Z[k])` → ok at 843. The intra-book anchors also resolve (`L2/incremental-least-squares.md:81-83 back_solve` → ok at 83; `concepts/givens.md:29 trsv` → ok at 29; the two L2 ranges :225-232 and :278-285 in-bounds of a 509-line file). The `verified_against:` block carries 18 rows in correct `relative/path:line` citation format. The tool is the authoritative line-map and it clears every load-bearing pinpoint.

**surface-or-evidence — pass.** This is a pure retroactive-evidence-backfill audit (the explicitly-allowed shape): the proposed change is a `verified_against:` metadata append to an already-firm leaf, with no surface (operator/theme text) modification and no status change. The report frames it exactly as evidence backfill ("no contradictions and no status change … records the per-citation no-drift verdicts"). No rotation_claim-without-surface failure mode applies.

**rotation-quality — pass (not applicable to audit-kind).** No algebraic/structural rotation is asserted; this is an L1-leaf evidence audit, not a lowering-rotation proposal. Marked pass per the inapplicable-check convention.

**variant-axis-coverage — pass.** The operator's variant axes are explicitly covered, not hidden: the GMRES-vs-FGMRES basis axis (law 6, `V` vs `Z`, confirmed byte-identical body), the real/complex element-type axis (`ScalarType` for `H`/`s`/`sn` vs `RealType` for `cs`, anchored at hpp `:192-194`), and the degenerate-shape axis (empty-cycle `j=-1`, single-column `j=0`, law 5). Each combination is named and anchored; the report scopes the downstream basis-lift (`:666`/`:843`) out of the leaf explicitly. No hidden branches.

**cross-reference-integrity — warning.** All `[link]` targets and named slugs resolve: `book/src/L1/back_solve.md` exists; `index.md` carries the claimed `**Firm (21)**` count (`:31`), cohort bullet (`:53`), and dep-map row (`:95`); `SUMMARY.md:85` has the chapter entry; the L2 parent and `givens.md` anchors resolve. The build-readiness fence guard, however, surfaces a concern (see Issues). The proposed-changes block at lines 198–275 nests a same-length (3-backtick) ` ```yaml ` fence (line 200) inside the ` ```edit: ` fence (line 198), closed by two consecutive bare ` ``` ` (lines 274, 275). Fence parity is even (4 fence lines) and the firm apparatus is NOT involved (this is a metadata append, not a firm-body authoring), so this is NOT the cycle-019 firm-body-outside-fence defect. But the nested same-length fence is the cycle-024 nested-`text`-fence truncation variant — and the report's own self-note (line 196: "Code sample inside the fence is 4-space-indented per the nested-fence discipline") is FALSE for this block: the `yaml` payload at 201–273 is a literal nested fence, NOT 4-space-indented. That self-description mismatch is a candidate for the `convert-nested-fences-to-indented-code-in-proposed-changes-block` repair.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (this is an L1-leaf audit, not a lowering edge). The trsv-sibling distinction the dispatch flagged is preserved correctly: the report keeps the `trsv` L3-inventory gap OPEN (OQ `l3-vocabulary-inventory-gap`, confirmed at open-questions.md as "REMAINING: `trsv` ONLY (BLOCKED, no L1 anchor)"), and consistently frames `back_solve` as a *sibling* of — not the *realisation* of — the general `trsv` (matching index.md:53 "a sibling (not the realisation) of the general `trsv`" and the leaf's non-law). The `concepts/givens.md:29` carry-forward is accurately reported: that line does end "enabling `back_solve` via `trsv`" AND uses `ls_update_column` for the distinct column-streaming step in the same sentence — the report's carry-forward note states this precisely and scopes the prose-tightening out as future work.

**plan-kind-consistency — pass.** Declared kind is `lowering-verifier` audit; content shape matches — per-citation audit table, applicability conditions, law re-confirmation, a verdict of fully-supported with no status change, and an evidence-only append. The frontmatter `status: pending` is the pre-integration default (correct for this phase). The audited leaf's own `firm`-on-positive-structure status (with the no-dedicated-test caveat held non-gating per the `lu_solve`/`apply_linop` precedent) is re-confirmed accurately, not silently mis-tiered.

**skill-uptake-survey — pass.** The audit shape implies `verify-citation-range` / the `tools/citecheck` `--anchor`/`--scan` mechanical path, and the report references both explicitly (Supporting evidence + Open questions: "ran `citecheck --anchor` against all 15 `iterative.cpp` pinpoints", "on-disk-wins protocol was applied"). Telemetry present; non-blocking.

### Issues found

1. **Nested same-length ` ```yaml ` fence inside the ` ```edit: ` proposed-changes block; self-note mis-describes it as 4-space-indented.** `reports/.../CYCLE.md` §Proposed changes, lines 196–275. Severity: warning (build-readiness / parser-robustness). The block opens ` ```edit:book/src/L1/back_solve.md ` (198), then ` ```yaml ` (200), closing with bare ` ``` ` at 274 and 275. Parity is even and no firm apparatus is at stake (metadata append only), so the cycle-019 fence-truncation FAIL condition does not apply. But the nested 3-backtick fence is the cycle-024 truncation-hazard variant, and the report's line-196 claim that the sample is "4-space-indented per the nested-fence discipline" is contradicted by the literal block — the YAML is a nested fence, not indented. Candidate for `convert-nested-fences-to-indented-code-in-proposed-changes-block`, or for the integrator to confirm its block-parser extracts the `verified_against:` payload (201–273) intact before applying.

2. **`verified_against:` row 8 collapses 4 distinct FGMRES pinpoints into one range citation.** `reports/.../CYCLE.md` line 230 (`citation: palace/linalg/iterative.cpp:831-840`). Severity: minor / cosmetic. The Per-citation audit section audits `:831`, `:835`, `:838`, `:843` as four separate anchors (lines 84–102), but the appended metadata row records a single range `:831-840` with the four pinpoints named only in the prose note. The :843 lift is actually OUTSIDE that range (843 > 840). This is internally consistent (the note says ":831/:835/:838/:843 anchors zero-drift" and the byte-identity range is genuinely :831-840 with :843 being the downstream lift) and all four anchors are independently verified ok, so it is not a citation-validity failure — but the range label `:831-840` does not enclose the :843 anchor it claims in its own note. A pedantic reader of the metadata alone would find the :843 pinpoint unrepresented as a row. Flagged for completeness; not blocking.

3. **No pre-existing `verified_against:` block on the leaf — append is additive, safe.** `book/src/L1/back_solve.md` (no current `verified_against` key). Severity: informational. Confirms the proposed append does not collide with or duplicate existing audit metadata; the integrator applies it as a clean end-of-file addition. No issue, recorded for the integrator's benefit.

## Repair

### Fixes attempted

- **Finding** (cross-reference-integrity, warning): Nested same-length ` ```yaml ` fence (CYCLE.md:200) inside the ` ```edit: ` proposed-changes block (CYCLE.md:198) — the cycle-024 nested-fence truncation variant; parity even and metadata-append-only (NOT the cycle-019 firm-body FAIL), but the report's line-196 self-note FALSELY claimed the sample was "4-space-indented per the nested-fence discipline" when the YAML was a literal nested fence.
  - **Decision**: repaired.
  - **Action**: Applied skill `convert-nested-fences-to-indented-code-in-proposed-changes-block`, preferred option (b) from its "Note on `verified_against:` YAML blocks" (render 4-space-indented rather than fenced). In CYCLE.md §Proposed changes: deleted the inner ` ```yaml ` opening line (was line 200) and the inner closing ` ``` ` (was line 274), and 4-space-indented the entire `verified_against:` payload (now CYCLE.md:200-272) inside the outer `edit:` block. The outer block now opens at CYCLE.md:198 and closes with a single bare ` ``` ` at CYCLE.md:273 — fence count is exactly 2 (one paired open/close per `grep -c '^```'`), no nested same-length collision. This choice makes the line-196 self-note ("4-space-indented per the nested-fence discipline") literally TRUE, so no separate self-note edit was required — the content now matches the note rather than the note being patched to match content. The downstream `cross-layer-cross-cutter` parser keys on the `verified_against:` leading text, which survives the indent form (per the skill note). Byte content of every YAML row preserved; only the fence mechanism changed (fenced → indented).

- **Finding** (Issue 2, minor/cosmetic): `verified_against:` row 8 (was CYCLE.md:230) labels the FGMRES range `:831-840` while its own note names a `:843` anchor that sits OUTSIDE that range. All four FGMRES anchors (`:831/:835/:838/:843`) are independently verified ok in the Per-citation audit; the range `:831-840` is the genuine byte-identical body range and `:843` is the downstream Z-basis lift. Critic flagged as optional, not blocking.
  - **Decision**: repaired (trivial label tightening).
  - **Action**: Tightened the row-8 note in CYCLE.md (the indented `verified_against:` row for `palace/linalg/iterative.cpp:831-840`) to state explicitly "body range :831-840 … :831/:835/:838 body anchors + :843 downstream Z-basis lift (outside the body range) all zero-drift." Chose note-clarification over widening the `citation:` range to `:831-843`, because widening would conflate the byte-identical body with the downstream lift and muddy the law-6 byte-identity claim. The four pinpoints are now unambiguously accounted for at the row level. No range field changed.

- **Finding** (Issue 3, informational): No pre-existing `verified_against:` block on the leaf — clean additive append.
  - **Decision**: not-needed.
  - **Rationale**: No defect; the critic recorded it for the integrator's benefit. Nothing to repair.

### Unrepairable findings

None. The single warning was the mechanically-repairable nested-fence variant covered by a promoted skill; all other checks passed.

## Suggested resolution

`ready`. Notes for the integrator: the proposed `verified_against:` block is now a clean 4-space-indented append inside a single paired `edit:` block — extract the indented payload (CYCLE.md:200-272) and append it to `book/src/L1/back_solve.md`. Per the landed-precedent convention (`book/src/L2-L1/deflate-composition-lowering.md:343` keeps the block as a ` ```yaml ` fence in the chapter file, satisfying the `lowering-verifier-yaml-in-prose-channel-format` requirement), the integrator should land the appended block as a fenced ` ```yaml ` block in the leaf even though the report carries it indented — the indent form in the report is purely to avoid the same-length-fence mis-toggle in the proposed-changes extraction, not a directive to drop the chapter-file fence. This is an additive metadata-only change: no `## Status` flip, no surface modification, no dep-map/SUMMARY touch.
