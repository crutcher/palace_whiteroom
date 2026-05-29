---
agent: integrator-finalize
invoked_at: 2026-05-29T061403Z
scope: cycle-021 cycle-end finalize (batch CYCLE.md, book rebuild, commit, housekeeping) — THIRD/FINAL primary cycle of meta-batch-5
status: complete
cycle_id: cycle-021
meta_batch: batch-5
meta_batch_position: 3 (closure — batch-5 meta-phase fires AFTER this commit)
staging_log: reports/cycle-021-integrator-staging/STAGING.md
integration_commit: PLACEHOLDER_SHA
---

# Cycle-021 batch CYCLE.md — report of records

THIRD / FINAL primary cycle of meta-batch-5 (cycles 019/020/021). **The batch-5 meta-phase fires immediately after this finalize commit.** Eight `integrator-per-report` dispatches landed; this finalize reconciled the staging log, rebuilt the book, repaired one cohort-list inconsistency, updated roadmap + cycle-record + log + integrator-signals, marked the 8 consumed reports, and committed atomically.

## Summary

Vocabulary-buildup cycle. **Five firm landings spanning the full L1/L2/L3>L2/L4>L3/L1>L0 stack** plus two rough-in L2 dep-map rows, one additive L1>L0 sub-pattern, and one BLOCKED-inventory observation. The marquee result is a complete vertical: the ksp_solve outer-driver story now has a firm L2 operator (#4) AND its firm substantive L3>L2 rotation (#5), resolving the cycle-020 maturity-gradient inversion (a firm L3 entry above an L2 stub). The 5-batch fgmres carry-forward (cycle-010→021) closed. The BLAS-1 L1>L0 floor advanced to 7/8 (axpby firm; axpbypcz gated to cycle-022 with a drafted firm body).

## Reports consumed (8)

| # | report | agent | status | follow_up_agent / next |
|---|---|---|---|---|
| 1 | `2026-05-29T051532Z-lifter-fgmres-theme-firm` | lifter | applied | lowering-verifier (fgmres/gmres L3 pairwise consistency) |
| 2 | `2026-05-29T051532Z-harvester-nleps-l1` | harvester | applied | harvester (4 deferred NLEPS L1 pieces); layer-intro-author (eigsolve backref + concept page) |
| 3 | `2026-05-29T051532Z-lowering-verifier-axpby-axpbypcz-firm` | lowering-verifier | **partially-applied** (by design) | lowering-verifier/abstractor cycle-022 (axpbypcz callsite-correction + firm) |
| 4 | `2026-05-29T051532Z-harvester-l2-ksp-solve-firm` | harvester | applied | lifter/lowering-verifier (L3 ksp_solve :463/:563 citation-drift sweep) |
| 5 | `2026-05-29T051532Z-abstractor-l3-l2-ksp-solve-outer-driver` | abstractor | applied | (refinement niceties — cross-link tightening; fgmres coverage-symmetry note) |
| 6 | `2026-05-29T051532Z-combinator-miner-deflate-gram` | combinator-miner | applied | harvester (lu_solve L1 primitive, THEN deflate/gram L2 firm) |
| 7 | `2026-05-29T051532Z-same-layer-cross-cutter-orthog-dot-surface` | same-layer-cross-cutter | applied | abstractor (orthogonalize-mutation-rotation L1>L0 should cite Sub-pattern D) |
| 8 | `2026-05-29T051532Z-harvester-l3-eigsolve` | harvester | applied (BLOCKED-inventory; no book change) | harvester (eigsolve prerequisite chain L1-firm→L2-entry→L3) |

**Status counts:** 7 applied + 1 partially-applied (axpby firm / axpbypcz gated, by design) = 8 staging rows. One of the 8 (eigsolve, BLOCKED-inventory) made no book changes (`Build-relevant: no`). **Staging reconcile: clean — 8 rows == 8 dispatched ready reports.** The cycle-018 staging-completeness gap did NOT recur (3rd consecutive cycle).

## Artifact changes (aggregated from staging Files-touched)

**New files (2):**
- `book/src/L1/apply_nonlinear_pencil.md` (firm L1; #2)
- `book/src/L3-L2/ksp-solve-outer-driver.md` (firm L3>L2; #5)

**Modified book files:**
- `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md` (rough-in→firm; #1) + `book/src/L4/index.md` (firm theme row added :44; #1)
- `book/src/L1/index.md` (L1 cohort 12→13; #2) + `book/src/SUMMARY.md` (#2 :68, #4 :44 de-stub, #5 :34)
- `book/src/L1-L0/axpby-mutation-rotation.md` (rough-in→firm; #3) + `book/src/L1-L0/index.md` (:18 row firm; #3)
- `book/src/L2/ksp_solve.md` (stub→firm; #4) + `book/src/L2/index.md` (:53 dep-map row firm #4; 2 rough-in rows gram/deflate #6; cohort-bullet consistency-repair by finalize)
- `book/src/L3-L2/index.md` (dep-map row; #5)
- `book/src/L1-L0/dot-mutation-rotation.md` (Sub-pattern D additive; #7) + `book/src/L2-L1/inner-product-fold-specialization.md` (bypass-surface paragraph; #7)

**Append-only scaffolding:** `scaffolding/open-questions.md` (all 8 reports appended intake; 3 recorded `...-RESOLVED` entries for meta-phase Closed-index migration).

## Safety-net gate results (aggregated, finalize-owned)

- **retroactive-budget global = 0** (sum across all 8 rows; well below the ≥4 block threshold). Per-slice all 0 (per-report gates).
- **build-breakage = none** — `cargo make book` exit 0, no `linkcheck2` dead-link errors. ONE cohort-list consistency-repair (not a content build-repair, see Build-status).
- **commit atomicity = single commit** (artifact + scaffolding + log + book output + staging log + consumed-report frontmatter + the uncommitted planner plan/priorities).
- **consumed-report frontmatter integrity = all 8 marked** `integrated_at` + `integration_commit: PLACEHOLDER_SHA` (two-phase SHA patch follows) + `integration_notes`.

## Build-status

`cargo make book` → exit 0, `linkcheck2` no dead-link errors. **ONE consistency-repair (finalize):** per-report #4 flipped the `L2/index.md:53` dep-map `ksp_solve` row stub→firm but left the §"Vocabulary cohort" prose bullets stale (`ksp_solve` still under "Queued at L2 (stub)" while the dep-map said firm — an internal cross-reference-integrity drift). Finalize moved the `ksp_solve` bullet into the "Firm at L2" list to match. This is a surgical cross-reference-integrity repair, not new authoring. The `gram`/`deflate` rough-in rows were verified plain-text inline-code (not live links); `book/src/L2/gram.md` and `book/src/L2/deflate.md` are correctly absent on disk — no `linkcheck2` break, no stub created (the clearly-implied bar is NOT met: single-algorithm concentration, all 5 sites in `nleps.cpp`; plain-text is the correct shape per the rough-in convention). The `katex` "Potential incomplete link" warnings are all pre-existing math-display false-positives (carried since cycle-015); none in a cycle-021-touched file.

## Wave-conflict observations

- **Intra-cycle load-bearing ordering chain (the key one this cycle):** #4 (L2 ksp_solve stub→firm) landed BEFORE #5 (L3>L2 ksp-solve-outer-driver), which cites the firm L2 form; the per-report integrator confirmed `firmness: firm` on disk before applying #5. Clean serial handoff — the canonical "promote the lower-layer anchor, then author the lowering theme that cites it" pattern.
- **L2/index dep-map adjacent-append after an in-cycle firm-flip:** #6 (gram/deflate rows) re-read disk FRESH and anchored "after the `ksp_solve` row (:53)" which #4 had just flipped firm; the row was still the table tail, so the append composed cleanly. Zero collision.
- **open-questions.md append-only multi-report concurrency:** all 8 reports appended; serial per-report dispatch + append-only discipline serialized cleanly. Three `...-RESOLVED` append-only entries (per-report integrators do NOT edit existing OQ entries in place).

## Open questions promoted (aggregated — for the meta-phase intake→plan migration)

**RESOLVED this cycle (recorded as append-only `...-RESOLVED`; meta-phase migrates to Closed index):**
- `fgmres-inner-loop-iterate-while-migration-lifter-candidate` (5-batch carry-forward cycle-010→021) + the cycle-020 trigger `fgmres-inner-loop-iterate-while-migration-firm-against-gmres-sibling`
- `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion`
- `ksp-solve-l2-promotion-non-identity-substantive-gap`
- `orthog-hpp-localdot-globalsum-unfused-dot-surface`
- `inner-product-conjugate-pair-reorder-caller-classification` (cycle-020)

**New blockers / carry-forward (for the plan):**
- `axpbypcz-mutation-rotation-callsite-correction-and-firm` (BLOCKER → cycle-022; closes BLAS-1 8/8) + `blas1-l1-l0-lowering-floor-7-of-8-axpbypcz-remains`
- `deflate-needs-small-dense-lu-solve-primitive` (HIGH fan-out; the `deflate` firm-promotion blocker — a NEW `lu_solve` L1 dense-solve primitive)
- `l3-eigsolve-blocked-on-l1-firm-and-l2-entry` + `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` (the strict prerequisite chain; meta-phase reframes plan item #9)
- `nleps-deferred-l1-primitives-carry-forward` (4 pieces, fan-out-ordered; deflated-residual now unblocked by the deflate/gram shape)
- `l3-ksp-solve-citation-drift-463-563-correction` + the inner-product-fold `operator.cpp` `:624`/`:634`/`:616` drift (a one-pass citation-drift sweep)
- `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d`; `nonlinear-pencil-opaque-type-concept-page-candidate`; the deflate factoring/scope-review OQs

## Next-cycle priorities (cycle-022)

1. `axpbypcz-mutation-rotation` callsite-correction + firm — enact the auditor's drafted corrections; closes the BLAS-1 L1>L0 floor 8/8.
2. NEW `lu_solve` L1 dense-solve primitive (the `deflate` blocker), then `deflate`/`gram` L2 combinator firm.
3. `eigsolve` prerequisite chain: L1 eigsolve rough-in→firm → L2 eigsolve entry → THEN L3 backfill (BLOCKED until both anchors exist).
4. `nleps_deflated_residual` L1 (next deferred NLEPS piece; now unblocked by the L2 deflate/gram shape).
5. L3-entry citation-drift sweep (L3 ksp_solve :463/:563 + inner-product-fold operator.cpp).
6. `orthogonalize-composition-lowering` L2>L1 theme (carry from cycle-019); the orthogonalize-mutation-rotation L1>L0 theme should cite Sub-pattern D.

## Roadmap deltas (firm-count ledger)

| layer | before | after | delta |
|---|---|---|---|
| L1 firm | 12 | **13** | +`apply_nonlinear_pencil` |
| L2 firm | 5 | **6** | +`ksp_solve` (outer-driver) |
| L3 firm | 9 | 9 | unchanged (eigsolve BLOCKED) |
| L4 firm | 4 | 4 | unchanged |
| L1>L0 themes firm | 15 | **16** | +`axpby` (BLAS-1 floor 7/8) |
| L2>L1 firm | 3 | 3 | unchanged |
| L3>L2 firm | 1 | **2** | +`ksp-solve-outer-driver` (FIRST L3>L2 growth this batch) |
| L4>L3 firm | 2 | **3** | +`fgmres` theme; rough-in 1→0 |
| L0 chapters | 22 | 22 | unchanged |

Phase-1 corpus removals stay 9/10. Roadmap prose updated on the GMRES/FGMRES Krylov line + the Eigenmode pipeline line.

## Note for the batch-5 meta-phase (fires next)

The comprehensive batch-5 (019/020/021) integration-tooling-friction picture is written in `scaffolding/integrator-signals.md` cycle-021 §Integration-tooling friction. Headlines: (a) the cycle-019 fence-truncation defect was corrected cycle-020 and the GUIDANCE HELD cycle-021 (all bodies enclosed in fences; no recurrence) — decide on promoting the two filed skill-candidates; (b) inline-anchor drift is now a stable 3-cycle pattern → the codemap-backed citation-checker ASK is increasingly justified (re-evaluate the defer-confirmed status); (c) sibling-slice re-anchor gap; (d) critic-vs-verifier independent-re-read cost; (e) pervasive skill-uptake-survey telemetry. The eigsolve BLOCKED-inventory routed a plan-item-#9 reframe to the meta-phase (priorities.md is meta/cycle-planner co-owned — not edited by finalize).
