---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T011500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-03T005657Z
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

# META: verification of "L4 + L4>L3 structural reorg (directive-3 wave, D1)"

## Critique

This is a directive-3 STRUCTURAL-REORG dispatch: SUMMARY regroup + index table re-sort + 3 new group-intro orientation pages. No new operator/theme claims. The citation/surface/rotation/variant-axis checks largely no-op (per the adapted checklist); the load-bearing checks are chapter-preservation, alpha-sort correctness, the small-Part guard, intro-page soundness, and `[old]`-anchor fidelity.

### Checks run

**citation-validity — pass.** No new operator/theme claims to cite; the dispatch re-orders existing rows verbatim and adds orientation prose. Verified the row contents in the regrouped `L4/index.md` dep-map and the re-sorted `L4-L3/index.md` theme-table are byte-for-byte the existing cells (the report explicitly asserts "row contents verbatim-unchanged; only row order and inserted sub-headers change", confirmed by spot-diffing the `[old]` blocks against disk). The 3 intro pages carry no `file:line` claims (orientation prose only). The §Supporting-evidence count citation (`L4-L3/index.md` tally line: "firm L4>L3 themes: 9 → 10") matches disk (line 50). No `verified_against:` block in this report — round-trip sub-check N/A.

**surface-or-evidence — pass (not applicable to a reorg-kind report).** No refinement of existing operator/theme surface text and no rotation_claims; this is a pure navigation/ordering pass over already-firm entries. The report is explicit that no `## Status` cell is flipped and no maturity changes.

**rotation-quality — pass (not applicable).** No algebraic/structural rotation asserted; the dispatch asserts none.

**variant-axis-coverage — pass (not applicable).** No operator with variant axes is being authored; the existing variant-axis content in the moved rows is untouched.

**cross-reference-integrity — pass.** Chapter-preservation verified mechanically and cleanly:
- **L4 SUMMARY:** all 15 chapter slugs from `[old]` appear exactly once in `[new]` (no dup, no drop), and the on-disk chapter-file set (`ls book/src/L4/*.md` minus `index.md` = 15) is exactly the `[new]` member set. The 3 group-intro pages (`iteration-combinators-intro.md`, `data-algebra-combinators-intro.md`, `outer-driver-combinators-intro.md`) are wired into SUMMARY as the group headers and their filenames match the 3 `newfile:` blocks; all member links in the intro pages resolve to real L4 files.
- **L4>L3 SUMMARY:** all 10 theme slugs preserved (old-set ≡ new-set, set-equal confirmed); flat list re-sorted alphabetically (verified sorted). Kept flat = correct (single kind).
- **Index dep-map (`L4/index.md`):** the 19-row table (15 chapters + 4 non-chapter outer-driver anchors `solve_loop`/`restart_cycle`/`Outcome`/`EigOutcome`) is fully preserved across the 3 regrouped sub-tables (4 + 6 + 9 = 19). The 4 anchor rows are correctly retained as index-only (no SUMMARY entry by design) and placed in the outer-driver sub-table — the report flags this explicitly so their SUMMARY absence is not misread as a dropped chapter.
- **Index theme-table + bullet list (`L4-L3/index.md`):** all 10 theme rows preserved; the 4-bullet §Vocabulary-cohort substantive-themes list preserved (old-set ≡ new-set).
- No `firm`-claim / fence-truncation guard applies (no firm-body authoring; orientation prose only).

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label asserted in this reorg; the moved L4>L3 rows carry their existing edge framing unchanged.

**plan-kind-consistency — pass.** Declared kind (structural-reorg) matches content shape exactly: SUMMARY/index ordering + intro pages, no claims. The small-Part guard is honored: L4's 3 groupings are 4 / 6 / 5 members (each ≥2, no manufactured singletons), and the kinds (iteration & step combinators / data-algebra combinators & named verbs / outer-driver caps & coordination combinators) match the `L4/index.md` §Vocabulary-cohort prose the report cites as the source. L4>L3 kept flat (10 themes, one dissolution kind) is the correct small-Part outcome. The judgment call (nesting 16-chapter L4) is surfaced transparently in §Open-questions with a stated flat-list fallback.

**skill-uptake-survey — warning (non-blocking).** This dispatch's shape (SUMMARY surgical regroup + alpha re-sort) is adjacent to two existing skills — `summary-md-surgical-insert` (cycle-005) and the alphabetical-API/by-kind-grouping directive (`feedback_mdbook_subchapter_grouping_and_alpha_api`) — yet the report references neither a skill invocation nor the grouping/alpha directive by name in its method narration. The work is correct, so this is a pure telemetry surface, not a defect: a `mdbook-by-kind-regroup` / alpha-sort-within-group procedure is the kind of pattern the directive-3 wave implies and that a skill could crystallize. Surfaced for the skill-candidates channel; does not gate.

### Issues found

1. **Alpha-sort defect in the `L4/index.md` outer-driver dep-map sub-table — `eigsolve` ordered before `EigOutcome`** (CYCLE.md §6, proposed `[new]` outer-driver sub-table, report lines 204–205). The group is otherwise alpha-ordered, but `EigOutcome` should precede `eigsolve` under any reasonable collation: case-insensitive, `eigo…` < `eigs…` (the 4th char `o`(111) < `s`(115)); case-sensitive ASCII, `E`(69) < `e`(101) — `EigOutcome` sorts first either way. The report places `eigsolve` first. **Severity: low / cosmetic.** It is an index-table ordering only (no SUMMARY link involved → no `linkcheck2`/build impact; no dropped row). The fix is a one-row swap (move the `EigOutcome` row above the `eigsolve` row in the outer-driver sub-table). Note the SUMMARY outer-driver *group* is unaffected (it has no `EigOutcome` entry — anchor, no chapter), so the discrepancy is confined to this single dep-map sub-table.

   - Scope note for the repairer: this is the ONLY ordering anomaly found. All other alpha orderings are clean — L4 SUMMARY groups (4/6/5, each verified sorted), L4>L3 SUMMARY flat list, the iteration & data-algebra dep-map sub-tables, the L4>L3 theme-table (10 rows), and the L4>L3 substantive-themes bullet list (4 bullets) all verified alpha-correct.

### Positive confirmations (load-bearing, no issue)

- **No dropped/renamed/re-pathed chapters.** L4: 15/15 chapters preserved + 3 intro pages added; L4>L3: 10/10 themes preserved. Index dep-map: 19/19 rows preserved.
- **`[old]`-anchor fidelity is exact.** The L4 + L4>L3 SUMMARY `[old]` blocks diff byte-identical to disk (SUMMARY lines 12–28 and 30–41). The `L4/index.md` dep-map `[old]` header + first data row match disk (lines 79, 81). The `L4-L3/index.md` theme-table `[old]` first row (disk line 15) and the §Vocabulary-cohort bullet `[old]` order (disk lines 45–48) match. The dispatch's reverted initial direct-write left no residue: disk shows NO nested dep-map sub-headers and NONE of the 3 intro pages exist yet — the `[old]` blocks reflect true pre-reorg on-disk state.
- **Small-Part guard honored** (3 groupings each ≥2; one-kind L4>L3 kept flat).
- **Intro pages sound.** Orientation prose describing the cohort + member links (all resolve to real files); no uncited operator claims; wired into SUMMARY as group headers (no dead link).

---

## Repair

### Fixes attempted

- **Finding**: Alpha-sort defect in the `L4/index.md` outer-driver dep-map sub-table — `eigsolve` ordered before `EigOutcome` (CYCLE.md §6, proposed `[new]` outer-driver sub-table).
  - **Decision**: repaired.
  - **Action**: Swapped the two rows in the proposed-changes `[new]` outer-driver sub-table so `EigOutcome` precedes `eigsolve` (CYCLE.md §6, former lines 204–205 — now `EigOutcome` row at 204, `eigsolve` row at 205). Row contents byte-unchanged; only their order is reversed. Mechanical one-row positional swap, fully within repair authority (variant-axis/alpha-classification clearly enumerable from collation — `eigo` < `eigs` case-insensitive; `E` < `e` case-sensitive). No SUMMARY entry involved (the `EigOutcome` anchor has no chapter), so no `linkcheck2`/build impact; the change is confined to this single index-only dep-map sub-table.

- **Finding**: skill-uptake-survey — warning (telemetry surface; the reorg+alpha-sort shape is adjacent to `summary-md-surgical-insert` / the by-kind-grouping directive but neither is named in the method narration).
  - **Decision**: not-needed.
  - **Rationale**: Pure telemetry, explicitly non-blocking and non-defect per the critic; the work is correct. No mechanical fix exists — naming a skill/directive in the producer's narration is not a repairer edit. Left for the skill-candidates channel as the critic intended.

### Unrepairable findings

None. The sole substantive issue (the alpha swap) was mechanically repairable; the remaining check is a non-actionable telemetry warning.

## Suggested resolution

`ready`. Clean structural reorg with no dropped/renamed chapters (15/15 L4 chapters + 3 intro pages; 10/10 L4>L3 themes; 19/19 dep-map rows preserved, per the critic's load-bearing confirmations). The one cosmetic alpha-ordering anomaly is now fixed in the `[new]` block. Integrator note: this is index-only ordering (no SUMMARY/build coupling), so the swap carries no rebuild risk.
