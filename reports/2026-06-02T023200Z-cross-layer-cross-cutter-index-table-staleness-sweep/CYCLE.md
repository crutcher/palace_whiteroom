---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T023200Z
scope: L3-L2 ↔ L2-L1 index-table-staleness sweep — index-status-cell-vs-theme-file-Status-line audit (cycle-055 D8 OQ)
status: pending
integrated_at: 2026-06-02T040000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-056 D2 (OBSERVATION-ONLY, no book mutation). Verdict applied as observation: CONFIRM-CLEAN — all 16/16 L3-L2 + L2-L1 index-table status cells MATCH their theme-file ## Status lines (row/file reconciliation 5/5 + 11/11); the cycle-055 L4-L3 in-place-promotion drift did NOT propagate to these deletion-swept tables (the deletion-sweep mechanism leaves no desync window). PARTIAL CLOSURE of the cycle-055 D8 OQ index-table-status-cell-drifts-when-theme-file-promoted for the L3-L2 + L2-L1 tables (D8 stays OPEN for L1/L1-L0/L4/L3/L2/L0); a finalize-time re-sweep would flag 0/16 here → the lightweight promotion-time guard preferred over a heavyweight finalize-time re-sweep (batch-17 meta-phase input). 3 OQs promoted to scaffolding/open-questions.md. NO book mutation, NO count delta."
---

# CYCLE: Cross-layer observation — L3-L2/L2-L1 index-table-staleness sweep (CONFIRM-CLEAN)

## Summary

Per the cycle-055 D8 OQ `index-table-status-cell-drifts-when-theme-file-promoted`, I swept the theme-list status cells of `book/src/L3-L2/index.md` (5 rows) and `book/src/L2-L1/index.md` (11 rows) against each theme file's actual `## Status` line on disk. **All 16 rows MATCH** their theme files. The L4-L3 index-table drift found in cycle-055 (3 stale rough-in cells for krylov-step/gmres/fgmres) **did NOT propagate** to the L3-L2 and L2-L1 tables — the cycle-050/051 mass refactor-demotion sweep that rewrote these two tables left their surviving status cells consistent with the theme files. The row counts also match the file counts exactly on both tables (5/5 and 11/11) — no orphan rows for deleted themes, no untable'd files. This closes the D8 OQ for these two tables.

## Observation kind

**Consistency drift — NEGATIVE RESULT (no drift found).** This is an audit confirming the *absence* of the consistency-drift class the cycle-055 L4-L3 finding raised. Recorded as a clean sweep, not a coverage gap / edge-mismatch / vocabulary-mismatch.

## Specific finding

Per-row table-says-vs-file-says comparison (ground truth = theme-file `## Status` line; **none of the 16 theme files carries YAML frontmatter** — they all begin with the `#` H1 heading, so there is no `firmness:` frontmatter field to compare; the `## Status` line is the sole ground truth).

### `book/src/L3-L2/index.md` — Theme list (rows 13–17), Status column

| # | Theme | Index table-says | Theme-file `## Status` says | Verdict |
|---|---|---|---|---|
| 1 | `krylov-step-body-identity` | `firm` (index.md:13) | `firm` (krylov-step-body-identity.md:154) | MATCH |
| 2 | `ksp-solve-outer-driver` | `firm` (index.md:14) | `firm` (ksp-solve-outer-driver.md:171) | MATCH |
| 3 | `orthogonalize-variant-split` | `firm` (index.md:15) | `firm` (orthogonalize-variant-split.md:387) | MATCH |
| 4 | `eigsolve-opaque-eigen-iteration` | `firm` (index.md:16) | `firm` (eigsolve-opaque-eigen-iteration.md:410) | MATCH |
| 5 | `chebyshev-nested-recurrence` | `firm` (index.md:17) | `firm` (chebyshev-nested-recurrence.md:425) | MATCH |

### `book/src/L2-L1/index.md` — Theme list (rows 13–23), status column

| # | Theme | Index table-says | Theme-file `## Status` says | Verdict |
|---|---|---|---|---|
| 1 | `chebyshev-iteration-fusion` | `firm` (index.md:13) | `firm` (chebyshev-iteration-fusion.md:198) | MATCH |
| 2 | `linear-combination-fold-specialization` | `firm` (index.md:14) | `firm` (linear-combination-fold-specialization.md:280) | MATCH |
| 3 | `inner-product-fold-specialization` | `firm` (index.md:15) | `firm` (inner-product-fold-specialization.md:456) | MATCH |
| 4 | `orthogonalize-composition-lowering` | `firm` (index.md:16) | `firm` (orthogonalize-composition-lowering.md:361) | MATCH |
| 5 | `gram-fold-specialization` | `firm` (index.md:17) | `firm` (gram-fold-specialization.md:388) | MATCH |
| 6 | `deflate-composition-lowering` | `partly-constructive` (index.md:18) | `partly-constructive` (deflate-composition-lowering.md:29) | MATCH |
| 7 | `eigsolve-spectral-transform-composition` | `firm` (index.md:19) | `firm` (eigsolve-spectral-transform-composition.md:364) | MATCH |
| 8 | `divfree-projector-leaf-identity` | `firm` (index.md:20) | `firm` (divfree-projector-leaf-identity.md:257) | MATCH |
| 9 | `incremental-least-squares-composition-lowering` | `firm` (index.md:21) | `firm` (incremental-least-squares-composition-lowering.md:417) | MATCH |
| 10 | `ksp-solve-outer-driver-unfold` | `firm` (index.md:22) | `firm` (ksp-solve-outer-driver-unfold.md:158) | MATCH |
| 11 | `krylov-step-kernel-defusion` | `firm` (index.md:23) | `firm` (krylov-step-kernel-defusion.md:303) | MATCH |

### Row-count / file-count reconciliation (no orphan rows, no untable'd files)

- `L3-L2/`: 5 theme files (excl. `index`) ↔ 5 table rows. MATCH.
- `L2-L1/`: 11 theme files (excl. `index`) ↔ 11 table rows. MATCH.

This matters because the cycle-050/051 demotion sweep *deleted* 12 L3-L2 thin themes and 11 L2-L1 thin themes. A stale table would most plausibly show as either (a) a surviving table row pointing at a now-deleted theme file (orphan row → `linkcheck2` build error), or (b) a status cell left at the pre-demotion value. Neither occurred: the lifters who enacted the demotions (provenance `reports/2026-06-01T195100Z-lifter-demote-*` D3–D6 cycle-050; the cycle-051 D1–D4 dispatches) correctly removed the table rows alongside the theme files, and every surviving cell tracks its file.

## Why the L4-L3 drift did NOT propagate here

The cycle-055 L4-L3 drift arose because three themes were **promoted firm in-place** (krylov-step c008, gmres c020, fgmres c021) and the promotion edits touched the theme files' `## Status` lines but not the index-table cells — a *promotion-time* desync. The L3-L2 and L2-L1 tables, by contrast, were last touched by the cycle-050/051 **demotion sweep**, which is a *deletion* operation (remove row + delete file together) — a deletion is harder to half-complete than an in-place status flip, because a left-behind row produces a dead link the build catches. The surviving rows in these two tables have not been individually promoted since they were authored at their current status, so there was no promotion-time desync window. The drift-class is therefore real (cycle-055 witnessed it) but **contained to the promotion-in-place case**, which these two tables happen not to have exercised post-authoring.

## Recommendation

- **Close the D8 OQ `index-table-status-cell-drifts-when-theme-file-promoted` for the L3-L2 and L2-L1 tables** — CONFIRM-CLEAN, no follow-up lifter needed for these two. (The OQ may remain open for any tables not yet swept; this dispatch covered only L3-L2 + L2-L1 per scope. The L4-L3 table was already swept + fixed in cycle-055.)
- **Defer — no `book/` mutation from this dispatch.** All rows match; there is nothing to fix.
- **Input to the batch-17 meta-phase on the proposed promotion-time / finalize-time index-consistency check:** this sweep is evidence that the drift is **promotion-in-place-specific**, not a general table-rot. A targeted guard — "when an integrator/lifter flips a theme file's `## Status` line, it must also update the matching index-table status cell" — would have caught the cycle-055 L4-L3 case at its source and is cheaper than a full finalize-time re-sweep. A full finalize-time sweep (re-derive every index status cell from the theme files at `cargo make book` time) is the heavier alternative; this audit found it would have flagged 0 of 16 rows here, so its marginal value is low for already-demoted tables but non-zero for tables with active in-place promotions (L1, L1-L0, L0 frontier work). RECOMMEND the meta-phase weigh the lightweight promotion-time guard (in the lifter/integrator-per-report spec) over the heavyweight finalize-time sweep.

## Supporting evidence

- `book/src/L3-L2/index.md:11-17` — theme-list table (header + 5 rows).
- `book/src/L2-L1/index.md:11-23` — theme-list table (header + 11 rows).
- Theme-file `## Status` lines: cited per-row in the tables above (file:line).
- Row/file count reconciliation: `ls book/src/L3-L2/*.md` (5 + index), `ls book/src/L2-L1/*.md` (11 + index); table-row grep counts 5 and 11 respectively.
- Cycle-050/051 demotion provenance (context for why these tables were last mass-edited): `book/src/L3-L2/index.md:51-53` §Working-Notes; `book/src/L2-L1/index.md:65` §Working-Notes cohort-growth log; `reports/2026-06-01T195100Z-lifter-demote-{assemble-diagonal,elementwise-product,reciprocal,normalize}/CYCLE.md` (D3–D6); `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md` (D8).

## Open questions / caveats

- **Scope boundary:** this sweep covered only the two tables in scope (L3-L2, L2-L1). The L1, L1-L0, L4, L4-L3 (already fixed c055), L3, L2, L0 index tables were NOT swept by this dispatch. If the meta-phase wants the drift-class fully characterized across the artifact, a sibling sweep of the L1 / L1-L0 tables (the layers with the most active in-place promotion churn) would be the highest-value next audit — those are the tables most likely to carry promotion-in-place desync, by the propagation argument above. Surfacing as a candidate, not parking.
- **Frontmatter caveat:** none of the 16 theme files carries YAML frontmatter, so the scope's `firmness:` frontmatter comparison was vacuous — the `## Status` line is the only ground truth, and that is what I compared. If a future convention adds `firmness:` frontmatter to lowering themes, a *third* desync surface (frontmatter vs `## Status` line vs index cell) would open; not a present concern.
- **No verified_against cross-check performed:** the scope asked for index-cell-vs-status-line; I did not re-audit the `verified_against:` metadata blocks for these themes (that is lowering-verifier work). The status-cell audit stands independent of audit-residue.
