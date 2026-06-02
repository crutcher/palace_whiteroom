---
agent: lifter
invoked_at: 2026-06-02T011200Z
scope: L4>L3 index theme-table staleness-fix — 3 stale status cells (krylov/gmres/fgmres) + consolidated 6→7 firm tally reconcile (supersedes D7 edit #2)
status: integrated
integrated_at: 2026-06-02T034000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "D8 cycle-055, corrective lifter for the needs-revision D7 edit #2 flagged. Applied clean — fixed 3 STALE L4-L3 index-table status cells (krylov-step firm c008, gmres firm c020 + slug→live link, fgmres firm c021 — all firm-on-disk but table-stale) + appended the corrected consolidated tally 6→7. Table now consistent at 7 firm; D7's l4-l3-fgmres-firmness-prose-vs-table-divergence OQ RESOLVED (prose was right, table was stale). Root-cause OQ index-table-status-cell-drifts-when-theme-file-promoted routed to batch-17 meta-phase."
inputs:
  - book/src/L4-L3/index.md
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (Status line :291-293, firm)
  - book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md (Status line :196-198, firm)
  - book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md (Status line :191-193, firm)
  - reports/2026-06-02T010800Z-layer-intro-author-c055-count-ownership/CYCLE.md (D7; edit #2 superseded here)
  - log/cycle-008.md:9 (krylov-step promoted rough-in→firm)
  - log/cycle-020.md:24 (gmres PROMOTED rough-in→firm; "L4>L3 firm 1→2, rough-in 2→1")
  - log/cycle-021.md:14 (fgmres PROMOTED rough-in→firm; "L4>L3 firm 2→3, rough-in 1→0")
  - log/cycle-051.md:14 / cycle-052.md:15 / cycle-053.md:12 (finalize records: "L4 firm 6 + 6 firm L4>L3 + 4 outer-driver rows")
---

# CYCLE: Re-anchor / staleness-fix L4-L3/index.md theme-table

## Summary

This is the **corrective dispatch D8** of cycle-055, handling the `needs-revision` follow-up the D7 repairer flagged. D7 (the consolidated-count owner) computed the L4>L3 firm tally from the **stale last-cell status text in the `L4-L3/index.md` theme-table** (which read "3 firm / 3 rough-in") instead of from the theme files' actual `## Status` lines. The table cells for **`krylov-step-typed-wrapper-dissolution`, `gmres-inner-loop-iterate-while-migration`, and `fgmres-inner-loop-iterate-while-migration`** were never updated when those three themes were promoted to firm (c008 / c020 / c021 respectively). All three theme files are `## Status: firm` on disk, and the c051–c053 integrator-finalize records consistently record **"L4 firm 6 + 6 firm L4>L3 + 4 outer-driver rows"** — i.e. **6 firm L4>L3 themes, 0 rough-in, pre-cycle-055**. This dispatch (1) fixes the 3 stale status cells (+ upgrades the gmres row's plain-text slug to a live link, since the anchor file now exists), and (2) supersedes D7's incorrect "3→4" consolidated tally with the correct **6 firm (pre-cycle) → 7 firm (with D2's `solve-family-map-dissolution`)** reconciliation. This is a clean mechanical staleness-fix; no theme content, signature, or rotation shape changes. D7's edits #1 (`L4/index.md`) and #3 (`L1/index.md`) are correct and stand; only D7's edit #2 (the `L4-L3/index.md` tally block) is replaced.

## Verified ground truth (read on-disk this dispatch)

| Theme file | On-disk `## Status` | Promotion provenance | Table cell (stale) |
|---|---|---|---|
| `krylov-step-typed-wrapper-dissolution.md:291-293` | **`firm`** | c008 wave-1 lifter (`log/cycle-008.md:9` "promoted from rough-in to firm") | `rough-in (cycle-006 abstractor; lowering-verifier follow-up candidate cycle-007)` |
| `gmres-inner-loop-iterate-while-migration.md:196-198` | **`firm`** | c020 wave-1 lifter (`log/cycle-020.md:24` "PROMOTED rough-in→firm … L4>L3 firm 1→2, rough-in 2→1") | `rough-in (cycle-008 abstractor; …)` + plain-text slug |
| `fgmres-inner-loop-iterate-while-migration.md:191-193` | **`firm`** | c021 lifter (`log/cycle-021.md:14` "PROMOTED rough-in→firm … L4>L3 firm 2→3, rough-in 1→0") | `rough-in (cycle-011 lifter; …)` |

The c021 finalize delta "**L4>L3 firm 2→3, rough-in 1→0**" plus the c047/c047/c048 trio (`iterate-while-dissolution`, `iterate-while-with-prev-dissolution`, `ksp-solve-driver-dissolution`) gives **6 firm / 0 rough-in pre-cycle-055** — corroborated verbatim by the c051/c052/c053 finalize headlines ("L4 firm 6 + **6 firm L4>L3** + 4 outer-driver rows"). D7's "3 firm / 3 rough-in" reading is exactly the stale-table artifact this dispatch repairs.

## Proposed changes

### 1. Fix the 3 stale status cells in `book/src/L4-L3/index.md` theme-table

Each `[old]` anchor targets only the trailing status cell (and, for gmres, the leading slug cell) of the row; the L4-form / L3-form / justification-kind cells are byte-preserved. The anchors are byte-exact against the current on-disk rows (lines 15, 16, 17).

**Row: `krylov-step-typed-wrapper-dissolution` (status cell only)**

```edit:book/src/L4-L3/index.md
[old]: | `structural` + secondary `reduction-chain` (the `modify` to record-update unfolding) | `rough-in` (cycle-006 abstractor; lowering-verifier follow-up candidate cycle-007) |
[new]: | `structural` + secondary `reduction-chain` (the `modify` to record-update unfolding) | `firm` (cycle-006 abstractor; PROMOTED rough-in→firm cycle-008 wave-1 lifter — `log/cycle-008.md`; first L4>L3 theme firmed via lifter) |
```

**Row: `gmres-inner-loop-iterate-while-migration` (leading slug cell → live link; trailing status cell)**

```edit:book/src/L4-L3/index.md
[old]: | `gmres-inner-loop-iterate-while-migration` *(rough-in; this dispatch creates the anchor file at `./gmres-inner-loop-iterate-while-migration.md`)* | L4 migrated GMRES inner-loop form:
[new]: | [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) | L4 migrated GMRES inner-loop form:
```

```edit:book/src/L4-L3/index.md
[old]: | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-008 abstractor; depends on upstream gmres.md §L4 v0.6→v0.7 self-rotation, routed to cycle-008+ lifter on `gmres.md §L4`) |
[new]: | `structural` + secondary `reduction-chain` and `empirical-match` | `firm` (cycle-008 abstractor; PROMOTED rough-in→firm cycle-020 wave-1 lifter — `log/cycle-020.md`; LHS landed the `gmres.md` §L4 v0.6→v0.7 self-rotation via option (a) `check_stop_into_carry`) |
```

**Row: `fgmres-inner-loop-iterate-while-migration` (status cell only)**

```edit:book/src/L4-L3/index.md
[old]: | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-011 lifter; same upstream gmres.md §L4 v0.6→v0.7 dependency as the GMRES sister) |
[new]: | `structural` + secondary `reduction-chain` and `empirical-match` | `firm` (cycle-011 lifter; PROMOTED rough-in→firm cycle-021 lifter — `log/cycle-021.md`; closes the 5-batch `fgmres-inner-loop-iterate-while-migration-lifter-candidate` carry-forward c010→021) |
```

### 2. Reconcile the consolidated L4>L3 firm tally — SUPERSEDES D7 edit #2 (6→7, not 3→4)

D7's edit #2 appends a "Consolidated tally" block + an "On-disk/record divergence" note after D2's `solve-family-map-dissolution` bullet in the `## Vocabulary-cohort` section of `book/src/L4-L3/index.md`. Both halves of D7's appended block are wrong (they assert "3 firm" pre-cycle and flag a non-existent prose-vs-table divergence rooted in the stale cells this dispatch fixes). This edit replaces D7's entire appended block with the correct 6→7 reconciliation.

The integrator should apply this edit AFTER D7's edit #2 has landed (so D7's block exists on disk to anchor against), OR — if D7 edit #2 is dropped at integration as superseded — apply this as the append after D2's bullet. The `[old]` below is byte-exact against D7's report edit-#2 `[new]` text (D7 CYCLE.md `reports/2026-06-02T010800Z-layer-intro-author-c055-count-ownership/CYCLE.md` lines 62-64), which is what will be on disk if D7 edit #2 applies first.

```edit:book/src/L4-L3/index.md
[old]: **Consolidated tally (firm L4>L3 themes: 3 → 4 this cycle).** Counted from the on-disk theme-list table above: **4 firm** themes — `iterate-while-dissolution` (c047), `iterate-while-with-prev-dissolution` (c047), `ksp-solve-driver-dissolution` (c048), and `solve-family-map-dissolution` (cycle-055 D2, this cohort); **3 rough-in** — `krylov-step-typed-wrapper-dissolution` (c006), `gmres-inner-loop-iterate-while-migration` (c008), `fgmres-inner-loop-iterate-while-migration` (c011). The cycle-055 D2 landing is **substantive** (a `map`-combinator → explicit-accumulating-loop translation with operator-hoist, not an identity-in-named-terms rename — honoring the vocabulary-shift redirect). The full L4 `solve_family` combinator lowers to the full L3 family-sweep by composing this theme (the outer map shell) above `ksp-solve-driver-dissolution` (each per-member solve) above `iterate-while-dissolution` + `krylov-step-typed-wrapper-dissolution` (the inner fold + per-step body) — a 4-shell stratified hop.

> **On-disk/record divergence (flagged for the integrator/finalize, NOT my fix).** The cycle-055 dispatch projected this layer at "6 → 7 firm". The on-disk theme-list table carries only **3 firm** rows pre-cycle (→ 4 with D2). The projected "6" likely conflated the L4 Part-overview prose at [`../L4/index.md`](../L4/index.md) "L4>L3 lowering themes" (which mis-labels `fgmres-inner-loop-iterate-while-migration` as *firm*) with this authoritative L4-L3 table (where that row is **rough-in**, line ~17). The two surfaces disagree on `fgmres-inner-loop` (and `gmres-inner-loop`) firmness. This consolidated tally is computed from the **on-disk table** (the authoritative dep-map), per the count-owner discipline. The L4-index-prose-vs-L4-L3-table firmness mismatch is an upstream landing-gap (OQ `l4-l3-fgmres-firmness-prose-vs-table-divergence`).
[new]: **Consolidated tally (firm L4>L3 themes: 6 → 7 this cycle).** Counted from the on-disk theme-list table above (status cells corrected cycle-055 D8): **7 firm** themes — `krylov-step-typed-wrapper-dissolution` (c006 abstractor, firm c008 lifter), `gmres-inner-loop-iterate-while-migration` (c008 abstractor, firm c020 lifter), `fgmres-inner-loop-iterate-while-migration` (c011 lifter, firm c021), `iterate-while-dissolution` (c047), `iterate-while-with-prev-dissolution` (c047), `ksp-solve-driver-dissolution` (c048), and `solve-family-map-dissolution` (cycle-055 D2, this cohort); **0 rough-in** (the krylov/gmres/fgmres trio was promoted to firm in c008/c020/c021 per `log/cycle-021.md` "L4>L3 firm 2→3, rough-in 1→0" + the c051/c052/c053 finalize records "6 firm L4>L3"; the table's last-cell status text was stale until this cycle's D8 fix). The cycle-055 D2 landing is **substantive** (a `map`-combinator → explicit-accumulating-loop translation with operator-hoist, not an identity-in-named-terms rename — honoring the vocabulary-shift redirect). The full L4 `solve_family` combinator lowers to the full L3 family-sweep by composing this theme (the outer map shell) above `ksp-solve-driver-dissolution` (each per-member solve) above `iterate-while-dissolution` + `krylov-step-typed-wrapper-dissolution` (the inner fold + per-step body) — a 4-shell stratified hop.
```

## Discipline notes

- **What changed and why.** Three table status cells were promoted `rough-in (...)` → `firm (...)` to match the on-disk theme-file `## Status` lines (all three are `firm`), and the gmres row's plain-text slug was upgraded to a live link because the anchor file now exists on disk (per the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill — the gmres anchor file was created when the theme was authored, and the cell's parenthetical "this dispatch creates the anchor file" is itself stale). The consolidated firm tally was corrected from D7's "3→4" to "6→7". This is a **pure mechanical staleness-fix** — no L4-form / L3-form / rotation-kind cell, no theme body, no signature, no applicability condition is touched. The high→low rewrite direction of each theme is unchanged.
- **Bounded prose-correction recorded (consolidated tally block).** D7's appended "Consolidated tally" + "On-disk/record divergence" block asserted a wrong count ("3 firm" pre-cycle) and flagged a non-existent prose-vs-table divergence. Both are artifacts of the stale table cells. Per the lifter `L0-evidence-driven prose correction is in-scope when bounded + evidenced + recorded` discipline (cycle-012 `lifter-scope-content-correction-boundary`): (i) the correction is supported by the on-disk theme-file `## Status` lines + the c008/c020/c021 cycle logs + the c051/c052/c053 finalize records, all read this dispatch; (ii) it is bounded (fixing a wrong count + drifted status cells, not re-architecting any theme's decomposition or rotation shape); (iii) it is recorded here explicitly. D7's superseded "divergence" OQ (`l4-l3-fgmres-firmness-prose-vs-table-divergence`) is **resolved by this fix, not migrated** — the L4-index prose was correct (it labeled gmres/fgmres firm, which they are); the L4-L3 table cells were the stale surface. The two surfaces now agree.
- **D7 partition.** D7's edits #1 (`L4/index.md` cohort/frontier reword) and #3 (`L1/index.md` FE sub-spine flip + grand-total) are correct and unaffected; only D7's `L4-L3/index.md` tally block (edit #2) is replaced. Disjoint from D1–D6.
- **Citation self-verification.** The provenance citations here are project-internal (theme-file `## Status` lines + `log/cycle-NNN.md` finalize lines), verified by direct `grep -n` / `sed -n` read this dispatch (not `reference/` source, so `citecheck --anchor` does not apply). The three theme files' Status lines were read verbatim (`firm` confirmed in all three); the c008/c020/c021/c051/c052/c053 log lines were read verbatim.

## Supporting evidence

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:291-293` — `## Status` … `` `firm` `` (firm c008 wave-1).
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:196-198` — `## Status` … `` `firm` `` (firm c020 wave-1).
- `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md:191-193` — `## Status` … `` `firm` `` (firm c021).
- `log/cycle-008.md:9` — krylov-step "promoted from rough-in to firm" (first L4>L3 firmed via lifter).
- `log/cycle-020.md:24` — gmres "PROMOTED rough-in→firm … L4>L3 firm 1→2, rough-in 2→1".
- `log/cycle-021.md:14` — fgmres "PROMOTED rough-in→firm … L4>L3 firm 2→3, rough-in 1→0".
- `log/cycle-051.md:14`, `log/cycle-052.md:15`, `log/cycle-053.md:12` — finalize records: "L4 firm 6 + **6 firm L4>L3** + 4 outer-driver rows" (authoritative pre-c055 count).
- D7 report `reports/2026-06-02T010800Z-layer-intro-author-c055-count-ownership/CYCLE.md:54-64` — the superseded edit #2 (its `[new]` text is the `[old]` anchor for this dispatch's tally edit).

## Open questions / caveats

- **OQ `index-table-status-cell-drifts-when-theme-file-promoted` (NEW; root-cause, for batch-17 meta-phase).** This defect's root cause is that the `L4-L3/index.md` theme-table's last-cell status text is **manually maintained separately from each theme file's `## Status` line**, so when a theme is promoted rough-in→firm (the promotion edits land in the theme file + the finalize record), the index-table cell is silently left stale. Three cells drifted across c008→c021 (~3 batches undetected) and were only surfaced when D7 trusted the cells for a count. Candidate fixes for the meta-phase to weigh: (a) a **finalize-time consistency check** that greps each theme file's `## Status` and diffs it against the index-table last-cell (and against the L4-index prose firmness labels); (b) a **layer-intro-author / lifter standing audit** when a theme is promoted, to update the index cell in the same dispatch; (c) a `tools/citecheck`-adjacent lint that flags index-table status cells disagreeing with their linked theme file's `## Status`. The same drift class likely exists in other `L*-L*/index.md` and `L*/index.md` tables (the L3-L2 / L2-L1 tables were mass-edited in c050/c051 and may carry similar residue) — a one-time sweep is warranted. (The D7-flagged `l4-l3-fgmres-firmness-prose-vs-table-divergence` OQ is **resolved by this fix**, not carried — the prose was right, the table was stale.)
- **No abstractor reread needed.** This is pure rewriting (status-cell text + a count), so the "stop if making non-trivial content decisions" gate is not tripped; all three themes' firm status is already settled on disk and in the finalize records.
- **Anchor-ordering caveat for the integrator.** The tally edit's `[old]` anchors against D7 edit #2's `[new]` text. If the integrator applies D7 edit #2 first (as expected — D7's report is also in this batch), the anchor resolves. If D7 edit #2 is dropped as superseded before this applies, the integrator should instead append this dispatch's `[new]` tally paragraph after D2's `solve-family-map-dissolution` bullet in the `## Vocabulary-cohort` section (the same insertion point D7 used). Either way the resulting on-disk tally must read "6 → 7 firm".
