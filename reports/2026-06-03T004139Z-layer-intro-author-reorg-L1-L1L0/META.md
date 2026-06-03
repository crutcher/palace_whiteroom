---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T010000Z
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
repaired_at: 2026-06-03T011500Z
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

# META: verification of "L1 + L1>L0 directive-3 reorg" (cycle-071 D4)

## Critique

This is a directive-3 STRUCTURAL-REORG dispatch (pure SUMMARY regroup + index table re-sort + 10 new group-intro pages; no new operator/theme claims). The 4 claim-bearing checks (citation-validity, surface-or-evidence, rotation-quality, variant-axis-coverage) no-op — they are marked `pass` as not-applicable-to-reorg below. The load-bearing checks are chapter-preservation, alpha-sort correctness, cross-reference-integrity, and the no-status-touched guard. All were run mechanically against the on-disk `book/src/SUMMARY.md`, `book/src/L1/index.md`, and `book/src/L1-L0/index.md`.

### Checks run

**citation-validity — pass (not applicable to reorg).** No source claims are made or modified; the report's only "citations" are SUMMARY line ranges and the `ls_update_column` path-asymmetry note, all of which were verified against disk. The intro-page bodies (§3/§4) restate already-firm characterizations (e.g. `assemble_frequency_operator` as the `linear_combination` operator-operand specialization) without introducing new file:line claims.

**surface-or-evidence — pass (not applicable).** Not a refinement of operator/theme surface; no rotation_claims involved.

**rotation-quality — pass (not applicable).** No rotation asserted.

**variant-axis-coverage — pass (not applicable).** No new operator with variant axes; the intro prose restates existing axes (de-Rham family, MGS/CGS/CGS2, differential-operator) without new coverage obligations.

**cross-reference-integrity — pass.** All 10 new SUMMARY group-intro links target files authored in §3/§4 of this report (none pre-exist on disk — verified no collision), so the integrator creates them before `linkcheck2` per the OQ. The two index.md anchored `[old]` snippets (`## Operator dep-map` / axpy row; `## Theme list` / axpby row) match disk verbatim. The `index.md` Overview links are preserved in both `[new]` blocks. The `ls_update_column` hyphen-path/underscore-slug asymmetry (`./L1/ls-update-column.md`) is preserved verbatim in SUMMARY and dep-map.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge labels in a structural reorg; the L1>L0 grouping is by theme-kind, and the prose discusses the matching kinds.

**plan-kind-consistency — pass.** Content shape matches the declared directive-3 structural-reorg kind: SUMMARY edits, table re-sorts, group-intro pages, explicit "no status/tally touched" discipline (§"Supporting evidence" line 415, verified — no `## Status` line, status cell, or firm-tally appears in any proposed-changes edit block).

**skill-uptake-survey — pass.** No `summary-md-surgical-insert`-style skill invocation is referenced, but the dispatch authors full-block `[old]→[new]` SUMMARY replacements (not surgical inserts) and the report itself supplies the mechanical preservation accounting, so no skill gap is surfaced. Telemetry only.

#### Chapter-preservation (THE load-bearing check) — PASS, no drops

True on-disk counts (from `grep` of the SUMMARY blocks, excluding the `index.md` Overview line):
- `# L1`: **36 chapters** (on-disk SUMMARY has 37 `./L1/*.md` link targets incl. `index.md`). Report's 36 is correct; the planner's awk-37 counted the Overview.
- `# L1 > L0`: **37 themes** (on-disk SUMMARY has 38 `./L1-L0/*.md` targets incl. `index.md`). Report's 37 is correct; the planner's awk-38 counted the Overview.

Slug-set diffs (`sort`-ed, both Parts):
- **L1 `[old]` vs disk: IDENTICAL.** **L1 `[old]` vs `[new]`: IDENTICAL** — every one of the 36 chapter slugs (+ Overview) appears exactly once in `[new]`. No drop, rename, or re-path.
- **L1>L0 `[old]` vs disk: IDENTICAL.** **L1>L0 `[old]` vs `[new]`: IDENTICAL** — every one of the 37 theme slugs (+ Overview) appears exactly once in `[new]`. No drop, rename, or re-path.

Per-grouping sub-counts confirmed from the `[new]` blocks: L1 = 11+3+6+3+6+4+3 = **36** ✓; L1>L0 = 28+5+4 = **37** ✓. Both borderline placements appear exactly once: `assemble_frequency_operator` (in Operator-application, count 1) and `fe-operator-assemble-mutation-rotation` (in Construction-rotation, count 1) — the placement judgments are acceptable and neither is dropped/duplicated.

#### Alpha-sort correctness — PASS

Every grouping is alpha-clean (mechanically verified `diff <list> <sort list>`):
- 7 L1 groupings: BLAS-1 (11), Operator-application (3), Constructed-gates (6), Krylov-LS (3), NEP (6), FE-assembly (4), FE-space (3) — all ALPHA-OK.
- 3 L1>L0 groupings: Mutation (28), Construction (5), Obstruction (4) — all ALPHA-OK.
- Index dep-map / theme-table re-sort target enumerations (§5/§6) cover the full disk row-sets IDENTICALLY (L1 dep-map: all 36 main + 6 obstruction rows; L1-L0 theme table: all 37 rows), and the listed within-group orders are alpha-clean.

#### Small-Part guard — PASS

The 7 L1 cohorts map to `L1/index.md` §Vocabulary-cohort documented motifs (main-cohort motifs + the two named FE sub-spines "Firm (FE-assembly sub-spine)" / "Firm (FE-space sub-spine)"); smallest grouping is 3 members (no 1-/2-item groupings manufactured). The L1>L0 3-way (mutation 28 / construction 5 / obstruction 4) is a genuine ≥2-kind split aligned with the CLAUDE.md obstruction-sub-kind invariant.

#### New group-intro pages — PASS

10 total (7 L1 + 3 L1>L0), all wired into SUMMARY as live links, none pre-existing on disk (no collision), all bodies authored in §3/§4 with sound orientation prose that restates firm characterizations only. The OQ correctly instructs the integrator to create them before the `linkcheck2` rebuild.

#### `[old]` anchor fidelity / no-status-touched — PASS

Both SUMMARY `[old]` blocks match disk verbatim (the earlier line-offset confusion the report notes is resolved — confirmed). Both index.md anchored-edit `[old]` snippets match disk verbatim. No `## Status` line, status cell, or running firm/partial-obstruction tally appears in any proposed-changes edit — pure structural reorg confirmed.

### Issues found

1. **(low / cosmetic — prose count slip in the §5 integrator note, CYCLE.md line 378)** The integrator note states the L1/index.md dep-map "has exactly these 37 data rows (31 firm/rough-in main + 6 obstruction)". The actual on-disk dep-map has **42 data rows = 36 main + 6 obstruction** (verified by enumeration). The "31 main / 37 total" arithmetic is wrong. **This is prose-only and does NOT affect correctness:** the §5 re-sort enumeration (lines 369–376) lists all 36 main + 6 obstruction operators and diffs IDENTICAL against the disk dep-map row-set, so the actual re-ordering instruction is complete — every row is accounted for. The risk is only that the integrator might trust the "37 data rows" sanity-figure and under-count during the mechanical move. Recommend correcting the note's figure to "42 data rows (36 main + 6 obstruction) + 8 sub-header rows". (The companion §6 note for L1-L0 says "37 data rows + 3 sub-headers" which IS correct — 28+5+4=37.)

No drops, no rename, no re-path, no dead link, no alpha violation, no status/tally mutation found. The single issue is a non-load-bearing arithmetic typo in an advisory integrator note, fully contradicted by the report's own correct re-sort enumeration.

## Repair

### Fixes attempted

- **Finding**: §5 integrator note (CYCLE.md ~line 378) states the L1/index.md dep-map "has exactly these 37 data rows (31 firm/rough-in main + 6 obstruction)" — actual count is 42 (36 main + 6 obstruction).
  - **Decision**: repaired
  - **Action**: Edited the §5 integrator note in `reports/2026-06-03T004139Z-layer-intro-author-reorg-L1-L1L0/CYCLE.md` — replaced both wrong figures ("37 data rows (31 firm/rough-in main + 6 obstruction)" and "after the move the table has 37 data rows") with "42 data rows (36 firm/rough-in main + 6 obstruction)" / "42 data rows + 8 sub-headers". Purely a wrong sanity-figure in an advisory prose note; the §5 re-sort enumeration (lines 369–376) already lists all 36 main + 6 obstruction rows and diffs IDENTICAL to disk, so no row was ever at risk. The §6 L1>L0 "37 rows" note is correct and was left untouched.
  - **Rationale**: In-scope mechanical prose-figure correction (no content authoring; the correct count was independently established by the report's own enumeration and the critic).

### Unrepairable findings

None. The sole finding was a cosmetic prose-count typo, repaired in place. All eight critic checks `pass`; the heaviest L1 + L1>L0 reorg is confirmed clean (no chapter/theme drops, alpha-clean, all guards honored, 10 intro pages wired, no status/tally touched).

## Suggested resolution

`ready`. Integrator note for the finalizer: the corrected §5 sanity-figure (42 data rows = 36 main + 6 obstruction) now matches the disk dep-map; the §5 re-sort enumeration was already complete and IDENTICAL to disk regardless. No `book/` mutation performed by the repairer.
