# Cycle-071 integrator staging log

Per-report integrators append one row each (newest LAST, append-only). integrator-finalize reads this to reconcile the cycle.

---

## 2026-06-03T004139Z-layer-intro-author-reorg-L4-L4L3
applied_at: 2026-06-03T010645Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/SUMMARY.md (edit — L4 region nested into 3 by-kind groupings w/ 3 group-intro parent links; L4>L3 region flat alpha re-sort)
- book/src/L4/iteration-combinators-intro.md (create — group-intro page, 4 members)
- book/src/L4/data-algebra-combinators-intro.md (create — group-intro page, 6 members)
- book/src/L4/outer-driver-combinators-intro.md (create — group-intro page, 5 chapter members + 4 anchor notes)
- book/src/L4/index.md (edit — Operator dep-map regrouped into 3 kind sub-tables, alpha within each; repaired EigOutcome-before-eigsolve order applied; 19/19 rows preserved verbatim)
- book/src/L4-L3/index.md (edit — Theme-list table alpha re-sort 10/10 rows; §Vocabulary-cohort substantive-themes bullet list alpha re-sort 4/4 bullets; tally line unchanged)

Gate hits:
- citecheck-scan: AMBIG x1 (integrator.hpp:58-61 — bare basename matches reference/palace/palace/fem/integrator.hpp + .../fem/libceed/integrator.hpp). PRE-EXISTING in committed L4-L3/index.md (cycle-068 D2 landing); verbatim-moved content, NOT introduced by this reorg. Non-blocking here (pure re-order introduces no new citations). Path-hygiene lint for a future repairer/producer pass on the fe-assemble-fold-dissolution row; recorded, not blocked.
- alpha-position-insert: 0 (positions were specified by the report; the EigOutcome/eigsolve swap was repair-pass-specified, applied as the repaired [new] block).
- SUMMARY chapter registration auto-fix: 0 (the 3 new intro pages WERE proposed as SUMMARY group-parent links by the report — no auto-registration needed; verified all 3 filenames match the newfile blocks and are wired as nested group headers).
- implied-component-stub: 0.
- index-placeholder displacement: 0.
- retroactive-budget: 0.

Open questions promoted:
- (none) — the report's §Open-questions are reorg-judgment caveats (nesting judgment call w/ stated flat-list fallback; anchor-row-placement note; no-status-change note; already-landed note), meta-notes for integrator-finalize / meta-phase, not new cross-cycle questions warranting OQ-ledger entries.

Build-relevant: yes

Notes:
- Pure directive-3 STRUCTURAL REORG of the L4 + L4>L3 Parts (D1 of 6 disjoint-Part reorg dispatches). NO status flips, NO new operator/theme claims, NO count/tally changes — chapters re-ordered/nested, not added.
- citecheck: 26 ok, 1 failing (the pre-existing AMBIG above). No MISS/OOB. The single AMBIG is not newly-introduced and both candidate paths resolve, so not unrepairable; left for a targeted producer/critic path-hygiene fix on the c068 fe-assemble row.
- SUMMARY nest well-formedness verified: each group is `- [Group name](./L4/<group>-intro.md)` with members indented 2 spaces beneath (valid mdBook nested SUMMARY). L4 = 4 + 6 + 5 chapter members (15/15 chapters preserved + 3 intro parents). L4>L3 kept FLAT (10/10 themes, single dissolution kind) per the small-Part guard.
- L4/index.md dep-map: 19/19 rows preserved (15 chapters + 4 non-chapter outer-driver anchors solve_loop/restart_cycle/Outcome/EigOutcome placed in the outer-driver sub-table, alpha-interleaved). The 4 anchors have NO SUMMARY entry by design (no chapter files) — their SUMMARY absence is NOT a dropped chapter. Applied the repair-pass [new] block (EigOutcome before eigsolve).
- All edits re-read disk before applying; SUMMARY [old] anchors matched verbatim. The two index.md table regroups were assembled by disk-slice splice (preamble + verbatim-reordered rows + trailer) after byte-diffing the on-disk row block against the report's [old] block (IDENTICAL in both cases) — row contents are byte-for-byte unchanged, only order + inserted sub-headers differ.
- Deferred integrated_at to finalize per role-spec. No book rebuild, no commit (finalize's job).
- This is D1; the remaining 5 reorg dispatches touch DISJOINT `# Part` blocks of SUMMARY.md (L3/L3-L2/L2/L2-L1/L1/L1-L0/L0/concepts etc.) — my edits touched only the `# L4` + `# L4 > L3` blocks, leaving sibling regions for the other per-report integrators.

---

## 2026-06-03T004139Z-layer-intro-author-reorg-L3-L3L2
applied_at: 2026-06-03T011704Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/SUMMARY.md (edit — `# L3` region nested into 5 by-kind groupings w/ 5 group-intro parent links; `# L3 > L2` region flat alpha re-sort)
- book/src/L3/blas1-intro.md (create — group-intro page, 8 members)
- book/src/L3/elementwise-intro.md (create — group-intro page, 3 members)
- book/src/L3/operator-apply-intro.md (create — group-intro page, 2 members)
- book/src/L3/smoother-intro.md (create — group-intro page, 3 members)
- book/src/L3/solver-caps-intro.md (create — group-intro page, 5 members)
- book/src/L3/index.md (edit — Operator dep-map regrouped into 5 kind sub-tables, alpha within each; repaired BLAS-1 `axpby,axpbypcz,axpy` order applied; 21/21 rows preserved verbatim; §Vocabulary cohort section added after dep-map)
- book/src/L3-L2/index.md (edit — Theme-list table flat alpha re-sort 6/6 rows; tally line unchanged)

Gate hits:
- citecheck-scan: AMBIG x2 (index.md:12-15 and index.md:49-52). NON-DEFECTS — these are the intro pages' / supporting-evidence prose cross-references to the sibling `L3/index.md` §Semantics overlay (bare-basename `index.md` references heuristically flagged by --scan), NOT file-line source citations. No MISS/OOB. Pure reorg introduces no new source citations; non-blocking.
- alpha-position-insert: 0 (positions were specified by the report; the BLAS-1 `axpby/axpbypcz/axpy` swap was repair-pass-specified, applied as the repaired [new] block per the META repair section).
- SUMMARY chapter registration auto-fix: 0 (the 5 new intro pages WERE proposed as SUMMARY group-parent links by the report — no auto-registration needed; all 5 filenames match the newfile blocks and are wired as nested group headers).
- implied-component-stub: 0.
- index-placeholder displacement: 0.
- retroactive-budget: 0.

Open questions promoted:
- (none) — the report's §Open-questions are reorg-judgment caveats (group-ordering convention alpha-vs-semantic, `normalize` BLAS-1-vs-Elementwise placement, L3>L2 flat-group small-Part decision, intro-page-wiring note), meta-notes for integrator-finalize / meta-phase consistency across the 6 sibling reorg dispatches, not new cross-cycle questions warranting OQ-ledger entries. (Consistent with D1's handling.)

Build-relevant: yes

Notes:
- Pure directive-3 STRUCTURAL REORG of the L3 + L3>L2 Parts (D2 of 6 disjoint-Part reorg dispatches). NO `## Status` flips, NO new operator/theme claims, NO count/tally changes — chapters re-ordered/nested, not added. Tally unchanged at 17 firm + 4 partial-obstruction (21 L3 chapters; 6 L3>L2 themes).
- citecheck: 14 ok, 2 failing — both the index.md AMBIG prose-reference non-defects above. No MISS/OOB, nothing unrepairable. (The repair-pass already corrected the stale "22 chapters" → "21" prose and the BLAS-1 alpha order in the report; both repaired versions applied.)
- SUMMARY nest well-formedness verified: each L3 group is `- [Group name](./L3/<group>-intro.md)` with members indented 2 spaces beneath (valid mdBook nested SUMMARY). L3 = 8 + 3 + 2 + 3 + 5 = 21 chapter members preserved + 5 intro parents. L3>L2 kept FLAT (6/6 themes, single dissolution-kind Part) per the small-Part guard.
- L3/index.md dep-map: the report's piecemeal anchor-edit blocks (#7-a/#7-b) were structurally incomplete as literal anchors (only header→BLAS-1-header + apply_linop-row→remainder; would have orphaned the middle rows). Applied a single disk-slice splice instead — extracted all 21 on-disk rows by slug, re-emitted them under the 5 alpha sub-table headers in the report-specified grouping/order, byte-for-byte preserved (only order + inserted sub-headers + preamble + §Vocabulary-cohort differ). Verified 21 row-lines round-trip and the {axpby,axpbypcz,axpy,...} grouping is exactly the on-disk slug set. Preserved the on-disk `inner_product` row wording ("...do-NOT-merge **boundary**)") which the report's [new] copy had trimmed to "...do-NOT-merge)" — kept the on-disk bytes to stay a faithful pure reorder.
- L3-L2/index.md theme-table: 6 rows alpha re-sorted (chebyshev-nested-recurrence < eigsolve-opaque-eigen-iteration < fold-solve-time-step-body < krylov-step-body-identity < ksp-solve-outer-driver < orthogonalize-variant-split) via the report's [old]→[new] block; rows byte-preserved.
- All edits re-read disk before applying; SUMMARY + L3-L2 [old] anchors matched verbatim. My region (the `# L3` + `# L3 > L2` SUMMARY blocks) was unaffected by D1's already-landed `# L4` edit.
- Cross-dispatch grouping-order convention (alpha-by-display-name here, matching D1's L4 choice) is a coherence question for integrator-finalize / meta-phase across the 6 sibling reorg dispatches — surfaced by the report's §Open-questions, no action required of this report.
- Deferred integrated_at to finalize per role-spec. No book rebuild, no commit (finalize's job).

---

## 2026-06-03T004139Z-layer-intro-author-reorg-L2-L2L1
applied_at: 2026-06-03T012730Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/SUMMARY.md (edit — `# L2` region nested into 5 by-kind groupings w/ 5 group-intro parent links; `# L2 > L1` region flat alpha re-sort)
- book/src/L2/step-kernels-intro.md (create — group-intro page, 2 members)
- book/src/L2/folds-intro.md (create — group-intro page, 3 members)
- book/src/L2/fold-family-stubs-intro.md (create — group-intro page, 6 members)
- book/src/L2/named-compositions-intro.md (create — group-intro page, 5 members)
- book/src/L2/elementwise-gate-floors-intro.md (create — group-intro page, 6 members)
- book/src/L2/index.md (edit — Operator dep-map regrouped into 5 kind sub-tables, alpha within each; preamble grouping note added; 22/22 rows preserved verbatim)
- book/src/L2-L1/index.md (edit — Theme-list table flat alpha re-sort 11/11 rows; rows byte-preserved)

Gate hits:
- citecheck-scan: 0 failing (22 ok, 0 failing — no MISS/AMBIG/OOB). Clean; pure reorg introduces no new source citations and the transported rows' embedded citations all resolve.
- fence-parity: 0 (18 fences = 9 balanced `edit:` blocks; clean).
- alpha-position-insert: 0 (positions specified by the report; no integrator position choice needed).
- SUMMARY chapter registration auto-fix: 0 (the 5 new intro pages WERE proposed as SUMMARY group-parent links by the report — no auto-registration needed; all 5 filenames match the create blocks and are wired as nested group headers).
- implied-component-stub: 0.
- index-placeholder displacement: 0.
- retroactive-budget: 0.

Open questions promoted:
- (none) — the report's §Open-questions are reorg-judgment caveats (group-ordering convention alpha-vs-reading-flow; `deflate` placed in Named-compositions vs Folds; `gram` placed in Fold-combinators vs Named-compositions; §Vocabulary-cohort prose left intact / not alpha-sorted), meta-notes for integrator-finalize / meta-phase coherence across the 6 sibling reorg dispatches, not new cross-cycle questions warranting OQ-ledger entries. (Consistent with D1/D2 handling.)

Build-relevant: yes

Notes:
- Pure directive-3 STRUCTURAL REORG of the L2 + L2>L1 Parts (D3 of 6 disjoint-Part reorg dispatches). NO `## Status` flips, NO new operator/theme claims, NO count/tally changes — chapters re-ordered/nested, not added. Tally unchanged at **21 firm + 1 partly-constructive (`deflate`)** at L2; 11 L2>L1 themes (10 firm + 1 partly-constructive `deflate-composition-lowering`).
- Chapter preservation VERIFIED: all **22 L2 chapters** preserved (set-equality vs disk EXACT — diff empty: 2 step-kernels + 3 fold-combinators + 6 fold-family-stubs + 5 named-compositions + 6 elementwise-gate-floors = 22 + 5 intro parents) and all **11 L2>L1 themes** preserved (set-equality EXACT). No slug dropped/renamed/re-pathed. The critic's count-reconciliation note (planner awk 23/12 over-counted the index.md Overview row; true is 22/11) confirmed — the report's 22/11 matches disk exactly.
- SUMMARY nest well-formedness verified via cat -A: each L2 group is `- [Group](./L2/<group>-intro.md)` with members indented exactly 2 spaces beneath (valid mdBook nested SUMMARY). L2>L1 kept FLAT (11 themes; 10-vs-1 composition-vs-standalone-gate split — no natural ≥2-kind partition, flat-alpha is the correct over-structuring-guard call) per the report.
- L2/index.md dep-map: re-read disk before editing; byte-diffed all 22 on-disk dep-map rows against the report's [new]-block rows (sorted) — IDENTICAL byte-for-byte. Applied the report's [old]→[new] edit (which anchored cleanly — `## Operator dep-map` header matched disk verbatim, unlike D2 where a disk-slice splice was needed). Post-apply re-verified: 22/22 row-leading slug set identical to pre-edit; 5 alpha-clean sub-sections (2/3/6/5/6).
- L2-L1/index.md theme-table: re-read disk; byte-diffed all 11 on-disk rows against the report's [new] block (sorted) — IDENTICAL byte-for-byte. Applied [old]→[new]; post-apply alpha-order verified clean (`sort -c` passed) and 11/11 rows round-trip.
- All edits re-read disk before applying; SUMMARY + both index [old] anchors matched verbatim. My region (the `# L2` + `# L2 > L1` SUMMARY blocks + the L2/L2-L1 index tables) was disjoint from D1's already-landed `# L4`/`# L4 > L3` and D2's `# L3`/`# L3 > L2` edits — left the 3 pending sibling regions (L1/L1-L0/L0/concepts) untouched.
- Cross-dispatch grouping-order convention (reading-flow order of the 5 L2 groupings vs alpha-by-group-title; alpha-within-each-group either way) is a coherence question for integrator-finalize / meta-phase across the 6 sibling reorg dispatches — surfaced by the report's §Open-questions, no action required of this report.
- Deferred integrated_at to finalize per role-spec. No book rebuild, no commit (finalize's job).

---

## 2026-06-03T004139Z-layer-intro-author-reorg-L1-L1L0
applied_at: 2026-06-03T013820Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/SUMMARY.md (edit — `# L1` region nested into 7 by-kind groupings w/ 7 group-intro parent links; `# L1 > L0` region nested into 3 theme-kind groupings w/ 3 group-intro parent links)
- book/src/L1/blas1-elementwise-intro.md (create — group-intro page, 11 members)
- book/src/L1/operator-application-intro.md (create — group-intro page, 3 members)
- book/src/L1/constructed-operator-gates-intro.md (create — group-intro page, 6 members)
- book/src/L1/krylov-least-squares-intro.md (create — group-intro page, 3 members)
- book/src/L1/nep-interior-intro.md (create — group-intro page, 6 members)
- book/src/L1/fe-assembly-intro.md (create — group-intro page, 4 members)
- book/src/L1/fe-space-intro.md (create — group-intro page, 3 members)
- book/src/L1-L0/mutation-rotation-intro.md (create — group-intro page, 28 members)
- book/src/L1-L0/construction-rotation-intro.md (create — group-intro page, 5 members)
- book/src/L1-L0/obstruction-intro.md (create — group-intro page, 4 members)
- book/src/L1/index.md (edit — Operator dep-map regrouped into 7 kind sub-tables + trailing Rough-in(obstruction) block, alpha within each; 42/42 rows preserved verbatim (36 main + 6 obstruction); disk-slice splice of full table body)
- book/src/L1-L0/index.md (edit — Theme-list table regrouped into 3 kind sub-tables (mutation 28 / construction 5 / obstruction 4), alpha within each; 37/37 rows preserved verbatim; disk-slice splice of full table body)

Gate hits:
- citecheck-scan: 0 failing (1 ok, 0 failing — no MISS/AMBIG/OOB). Clean; pure reorg introduces no new source citations and the transported rows' embedded citations resolve.
- fence-parity: 0 (all `edit:`/`create:` blocks balanced; the 2 full-table index edits applied as disk-slice splices, not the report's structurally-incomplete header-only anchors).
- alpha-position-insert: 0 (group order + within-group order fully specified by the report; no integrator position choice needed).
- SUMMARY chapter registration auto-fix: 0 (the 10 new intro pages WERE proposed as SUMMARY group-parent links by the report — no auto-registration needed; all 10 filenames match the create blocks and are wired as nested group headers).
- implied-component-stub: 0.
- index-placeholder displacement: 0.
- retroactive-budget: 0.

Open questions promoted:
- (none) — the report's §Open-questions are reorg-judgment caveats (intro-pages-as-new-files creation note; `assemble_frequency_operator` placed in Operator-application vs BLAS-1; `fe-operator-assemble-mutation-rotation` content-kind placed in Construction-rotation despite `-mutation-rotation` slug suffix; mixed-transitional-state-elsewhere note), meta-notes for integrator-finalize / meta-phase coherence across the 6 sibling reorg dispatches, not new cross-cycle questions warranting OQ-ledger entries. (Consistent with D1/D2/D3 handling.)

Build-relevant: yes

Notes:
- Pure directive-3 STRUCTURAL REORG of the L1 + L1>L0 Parts (D4 of 6 — THE HEAVIEST: the two largest Parts, 36 + 37 chapters, 10 new intro pages). NO `## Status` flips, NO new operator/theme claims, NO count/tally change — chapters re-ordered/nested, not added. L1 firm grand-total (34) + rough-in/obstruction tallies unchanged; L1>L0 firm/obstruction tally unchanged.
- **SLUG-SET DIFF RESULT (the cycle's biggest drop-risk; explicit per-Part):**
  - **L1: NO DROP.** git-HEAD pre-edit slug set vs post-edit, four independent diffs all IDENTICAL — SUMMARY 36 chapters (pre==post), L1/index.md dep-map 42 rows (pre==post; 36 main + 6 obstruction), and cross-check SUMMARY-members(36)==dep-map-main-rows(36). Every chapter slug present exactly once.
  - **L1>L0: NO DROP.** git-HEAD pre-edit slug set vs post-edit, all IDENTICAL — SUMMARY 37 themes (pre==post), L1-L0/index.md theme-table 37 rows (pre==post), and cross-check SUMMARY-members(37)==theme-table-rows(37). Every theme slug present exactly once.
- **ROW-BODY byte-preservation VERIFIED** for both index tables: set-sorted diff of all PRE rows vs all POST rows is EMPTY — only row ORDER + inserted `| **<grouping>** | | | |` sub-header rows differ; no row text rewritten. (The report's index `[old]` anchors were header-only/structurally-incomplete as D1/D2/D3 found; applied a full-table-body disk-slice splice instead, byte-diffing against committed HEAD.)
- SUMMARY nest well-formedness verified: each group is `- [Group](./L1{,-L0}/<group>-intro.md)` with members indented exactly 2 spaces beneath (valid mdBook nested SUMMARY). L1 groups alpha-clean sizes [11,3,6,3,6,4,3]=36; L1>L0 groups alpha-clean sizes [28,5,4]=37 — all 10 groupings pass `diff <list> <sort list>`.
- 10 new intro files all exist on disk (verified) before finalize's linkcheck2; bodies authored from the report's create blocks (real authored pages, not stubs). The two borderline placements appear exactly once each: `assemble_frequency_operator` in L1 Operator-application; `fe-operator-assemble-mutation-rotation` in L1>L0 Construction-rotation.
- The §5 integrator-note arithmetic was repair-corrected to "42 data rows (36 main + 6 obstruction)" per META; I confirmed 42 rows on disk independently. Repaired figure matched.
- All edits re-read disk before applying; SUMMARY `[old]` anchors matched verbatim. My region (the `# L1` + `# L1 > L0` SUMMARY blocks + L1/L1-L0 index tables) is disjoint from D1's landed `# L4`/`# L4>L3`, D2's `# L3`/`# L3>L2`, D3's `# L2`/`# L2>L1` edits — left the L0/concepts/etc. regions untouched.
- Deferred integrated_at to finalize per role-spec. No book rebuild, no commit (finalize's job).

---

## 2026-06-03T004139Z-layer-intro-author-reorg-L0-phase1
applied_at: 2026-06-03T015010Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/SUMMARY.md (edit — `# L0` region nested into 3 source-area groupings w/ 3 group-intro parent links; `# Phase 1 corpus` region flat alpha re-sort of the 9 slice sub-entries)
- book/src/L0/conventions-intro.md (create — group-intro page, 6 members)
- book/src/L0/file-overviews-intro.md (create — group-intro page, 11 members)
- book/src/L0/overload-sets-and-classes-intro.md (create — group-intro page, 5 members)

Gate hits:
- citecheck-scan: 0 failing (no citations found in the report — pure structural reorg, no source citations introduced). Clean; no MISS/AMBIG/OOB.
- fence-parity: 0 (4 balanced blocks: 1 `edit:` + 3 `create:`; clean).
- alpha-position-insert: 0 (group order + within-group order fully specified by the report; no integrator position choice needed).
- SUMMARY chapter registration auto-fix: 0 (the 3 new intro pages WERE proposed as SUMMARY group-parent links by the report — no auto-registration needed; all 3 filenames match the create blocks and are wired as nested group headers).
- implied-component-stub: 0.
- index-placeholder displacement: 0 (no L0/index.md table exists — the report correctly found L0/index.md is prose-only, no dep-map/API table; no in-index re-sort in scope).
- retroactive-budget: 0.

Open questions promoted:
- (none) — the report's §Open-questions are reorg-judgment caveats (L0/index.md bullet-list ordering not touched / flagged-not-bundled; group-intro slug-convention reconciliation; Phase-1 `spec/index.md` retained as group index; dispatch-phase-edit-reverted note). The slug-vs-title sort-key cross-dispatch question (surfaced by the critic as a meta-phase coherence note across D1–D6) is ALREADY tracked in the OQ ledger (open-questions.md line 873: `concepts-list-global-alpha-resort-vs-local-cluster-insert` + `l4-summary-and-index-insert-position-alpha-vs-chronological-pending-reorg`, closed-SEQUENCED to THIS directive-3 batch-22 reorg wave). No new OQ-ledger entry warranted — meta-phase already owns slug-vs-title uniformity across the 6 sibling dispatches. (Consistent with D1/D2/D3/D4 "promoted none" handling.)

Build-relevant: yes

Notes:
- Pure directive-3 STRUCTURAL REORG of the L0 + Phase-1-corpus Parts (D5 of 6 — last-but-one). NO `## Status` flips, NO new operator/theme claims, NO count/tally change — chapters re-ordered/nested, not added.
- **CHAPTER PRESERVATION VERIFIED:** all **22 L0 chapters** preserved (6 Conventions + 11 File-overviews + 5 Overload-sets-&-classes = 22; on-disk `book/src/L0/` = 23 `.md` = 22 + index.md, set-equality EXACT) and all **9 Phase-1 slices** preserved (on-disk `book/src/spec/slices/` = exactly 9 `.md`, set-equality EXACT). The dispatch directive's "planner awk said 10" Phase-1 count is WRONG; on-disk is 9 (the critic's reconciliation note confirmed). No slug dropped/renamed/re-pathed.
- LINK RESOLUTION VERIFIED: all 31 chapter links + 3 intro-parent links in the `# L0` + `# Phase 1 corpus` region resolve to on-disk files (Phase-1 slices point at `./spec/slices/*.md` + the retained `./spec/index.md` group index — verified on disk, NOT relocated into L0/). Each intro page's only internal link is `./index.md` → resolves to `book/src/L0/index.md`. No dead links.
- SUMMARY nest well-formedness verified: each L0 group is `- [Group](./L0/<group>-intro.md)` with members indented exactly 2 spaces beneath (valid mdBook nested SUMMARY; per-group sizes [6,11,5]=22). Phase-1 kept FLAT (9 slices, alpha-sorted, nested under the existing `spec/index.md` Index chapter) per the report — raw-material reference list, not a vocabulary layer, correctly NOT kind-grouped.
- 3 new intro files all exist on disk (verified) before finalize's linkcheck2; bodies authored from the report's create blocks (real authored 1-screen orientation pages, not stubs); each condenses the matching `L0/index.md` §Reference-note cohort paragraph and links back to `./index.md`.
- The L0 chapters are alpha-sorted BY SLUG within each grouping (the report's declared key). Critic flagged (low-severity observation) that File-overviews + Overload-sets groups are slug-key-sorted, NOT visible-title-sorted — self-consistent + defensible, surfaced ONLY for meta-phase to settle slug-vs-title uniformity across D1–D6 (already in the OQ ledger as noted above). Applied as-specified; no per-report sort-key change (out of repair/integration authority).
- All edits re-read disk before applying; SUMMARY `[old]` anchor (on-disk lines 217–251) matched the report's `[old]` block VERBATIM (incl. the original non-alpha order). My region (the `# L0` + `# Phase 1 corpus` SUMMARY blocks) is disjoint from D1's landed `# L4`/`# L4>L3`, D2's `# L3`/`# L3>L2`, D3's `# L2`/`# L2>L1`, D4's `# L1`/`# L1>L0` edits — left the `# Concepts` region (D6 pending) untouched.
- Deferred integrated_at to finalize per role-spec. No book rebuild, no commit (finalize's job).

---

## 2026-06-03T004139Z-layer-intro-author-reorg-concepts-small-parts
applied_at: 2026-06-03T020310Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/SUMMARY.md (edit — `# Concepts` block flat alpha re-sort: 44 content slugs C-locale sorted by file slug; 2 nav rows `Index`/`Dependency map` kept at top; NO nesting — flat shared-library reference list)

Gate hits:
- citecheck-scan: 0 failing (no citations found — pure structural reorg, no source citations introduced). Clean; no MISS/AMBIG/OOB.
- fence-parity: 0 (single balanced `edit:` block).
- alpha-position-insert: 0 (full order specified by the report; no integrator position choice needed — pure re-sort, not an insert).
- SUMMARY chapter registration auto-fix: 0 (no new chapter files — reorder-only; no new concepts/*.md created, so no SUMMARY-registration or concepts-section auto-fix triggered).
- index-placeholder displacement: 0.
- implied-component-stub: 0.
- retroactive-budget: 0.

Open questions promoted:
- concepts-index-table-vs-summary-membership-drift-two-missing-rows (the pre-existing `concepts/index.md` table is missing 2 rows — `nested-constructed-operator-gate` + `black-box-vs-accelerated-kernels` — that exist in SUMMARY + on disk; routed to batch-22 meta-phase / cycle-072 hygiene per the report's repair-corrected §Open-question)

Build-relevant: yes

Notes:
- Pure directive-3 STRUCTURAL REORG of the `# Concepts` Part (D6 of 6 — the LAST per-report integration of cycle-071; for finalize). This dispatch changed ONLY ONE Part. NO status flips, NO new operator/theme/concept claims, NO count change — the 44 content links were re-ordered (chronological-by-extraction → flat alpha by file slug), not added/dropped/renamed.
- **SLUG-SET PRESERVATION VERIFIED:** `set(old) == set(new)` — empty symmetric difference, 44↔44 content slugs (excluding the 2 nav rows). New order is C-locale slug-sorted (`.md` suffix stripped, per the report's declared key: `givens` < `givens_apply` < `givens_generate`; `scal` < `scalar-promotion` collation holds). All 44 concept files resolve on disk (verified) — no dead links for finalize's linkcheck2.
- **CRITICAL GUARD HONORED — `# Feature surfaces` UNTOUCHED:** verified on disk after my edit that the within-column level ordering is still `electrostatic.L4 → .L1 → .L0` (high→low, NOT alphabetized) — my Concepts edit is in a disjoint SUMMARY block; the standing batch-22-meta OQ ordering is intact. The other 4 Parts in D6's scope (Meta-Reviews chronological, Methodology, Feature surfaces, Design) were left UNCHANGED by the report and by this apply — only the `# Concepts` block was edited.
- **`concepts/index.md` 2-missing-row reconciliation NOT performed** (out of scope for this reorder-only dispatch, per task directive + critic/repair note) — routed via the promoted OQ above to batch-22 meta-phase / cycle-072 hygiene. Do NOT treat as a dropped concept: both slugs ARE in SUMMARY + on disk; the index table is the lagging derived surface.
- `[old]` anchor matched disk verbatim (SUMMARY lines 255–301, incl. the original chronological order + the 2 nav rows); edit re-read from disk before applying. My region (`# Concepts`) is disjoint from D1–D5's already-landed `# L4`/`# L4>L3`/`# L3`/`# L3>L2`/`# L2`/`# L2>L1`/`# L1`/`# L1>L0`/`# L0`/`# Phase 1 corpus` blocks.
- Deferred integrated_at to finalize per role-spec. No book rebuild, no commit (finalize's job). **This is the LAST per-report integration of cycle-071 — finalize may now reconcile the full 6-dispatch reorg wave (D1–D6) + rebuild + commit.**

---
