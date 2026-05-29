---
agent: cycle-planner
invoked_at: 2026-05-29T03:44:41Z
scope: cycle-020 dispatch plan
status: pending
---

# Cycle-020 dispatch plan

## Goals selected this cycle

Cycle-020 is the **SECOND primary cycle of meta-batch-5** (cycles 019/020/021); meta-phase fires after cycle-021, NOT this cycle. Cycle-019 landed 5 major firm promotions (L2 `orthogonalize` + `inner_product`, L2>L1 `inner-product-fold-specialization`, L1 `assemble-diagonal`, L1>L0 `nrm2-mutation-rotation`) + the L0 `fespace-file` anchor. This cycle focuses on **completing the BLAS-1 L1>L0 lowering-theme gap** (3 remaining themes: `dot`, `scal`, `assemble-diagonal` mutation-rotations) **+ auditing the firm fold-specialization theme** + **refreshing the L2 Part intro** (now at 5 firm operators) + **starting the L3 vocabulary-inventory backfill** (gemv/trsv cohort). One large carry-forward (gmres §L4 self-rotation) pairs with smaller independent dispatches for balanced density.

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|-------|-------|------|-----------|
| 1 | `abstractor` | `dot-mutation-rotation` + `scal-mutation-rotation` + `assemble-diagonal-mutation-rotation` L1>L0 themes (BLAS-1 gap closure) | none | The firm L1 leaves (`dot`, `scal`, `assemble-diagonal`) all exist; the L1>L0 stub homes at `book/src/SUMMARY.md` :82 (dot), :84 (scal), + assemble-diagonal stub are ready. Closes the critical BLAS-1 lowering-theme gap identified in integrator-signals. High fan-out: every solver lowering reuses these. Routes as ONE dispatch (3 companion themes, parallel authoring within the dispatch). |
| 2 | `lowering-verifier` | `inner-product-fold-specialization` L2>L1 theme audit (per-line dispatch-rule + summation-order verification) | none | The theme is firm; audit against the L2 `inner_product` + L1 fold-leaves dispatch rules. Per-report integrator flagged this as audit-ready (cycle-019 unblocked section). Companion to #1: parallel execution. |
| 3 | `layer-intro-author` | L2 Part-intro refresh (`book/src/L2/index.md` Working-Notes + dep-map overlay) | 1, 2 | L2 now at 5 firm operators (cycle-019 added `orthogonalize` + `inner_product`; adds narrative coverage for the named-composition + fold-cohort vocabulary growth). Two converging refresh flags fold into one dispatch. Depends on #1 and #2 landing so the Part-intro can survey the full cohort. |
| 4 | `harvester` / `lifter` | `gmres.md §L4 v0.6→v0.7` self-rotation (LARGE carry-forward) | none | Firms both the cycle-008 GMRES + cycle-011 FGMRES sister themes; recurring across batches 2/3/4. Large; carried from cycles 008/011 OQs. Candidate for splitting if density becomes a concern (gmres-self-rotation vs fgmres-self-rotation as separate), but the user's experience suggests unified cycle-008 gmres slice → both L4 + L4>L3 + L4>L2 versions is coherent. Parallel to #1/#2 (distinct artifact region). |
| 5 | `harvester` | `l3-vocabulary-inventory-gap — gemv/trsv L3 cohort growth` (backfill beyond BLAS-1 closed cohort) | none | Lower-layer shared-vocabulary priority per cycle-009 directive. L3 is the iteration-rotation layer; every per-solver L3 lowering reuses these. Routes `harvester` or `cross-layer-cross-cutter` (choose `harvester` as the primary producer for new L3 entries). Pairs with #4 (independent). |
| 6 | `abstractor` | `conjugate-pair-reorder caller-classification` (inner-product fold caller-site real-projected-invisible vs full-complex-observable) | 2 | Companion audit to #2: after the lowering-verifier confirms the theme's per-line rules, scan every `linalg::Dot` call site (palace/linalg and palace/fem) to classify real-projected-invisible vs full-complex-observable. Surfaces the complex-path risk points. Depends on #2's audit findings. Small dispatch (caller inventory). Parallel wave-2 after #2 lands. |

## Overlap analysis

**#1 (dot/scal/assemble-diagonal abstractor)** → creates L1>L0 themes at `book/src/L1-L0/dot-mutation-rotation.md`, `book/src/L1-L0/scal-mutation-rotation.md`, `book/src/L1-L0/assemble-diagonal-mutation-rotation.md`. All three are distinct files, no rewrite collision. Appends proposed-changes blocks for SUMMARY.md de-stub at :82/:84.

**#2 (lowering-verifier inner-product-fold audit)** → audits the EXISTING firm `book/src/L2-L1/inner-product-fold-specialization.md` (no write, verification only). Reports findings in the CYCLE.md META.md audit section.

**#3 (layer-intro-author L2 refresh)** → rewrites `book/src/L2/index.md` (Part intro, Working-Notes prose, dep-map). Depends on #1 and #2 being DISPATCHED (not yet integrated, but themes proposed in #1's CYCLE.md give the intro author the text to cite). Safe to dispatch after #1/#2 because the intro author works from the proposed-changes blocks, not the integrated artifact.

**#4 (harvester/lifter gmres self-rotation)** → produces L4 `book/src/L4/gmres.md` (or re-anchors if cycle-008 rough-in exists), L4>L3 themes, L4>L2 themes. Distinct from #1/#2/#3 (different artifact regions, no overlap with BLAS-1 or L2 intro).

**#5 (harvester l3-vocab gemv/trsv)** → produces L3 entries like `book/src/L3/gemv.md`, `book/src/L3/trsv.md` or extends existing stubs. Distinct from #4 (gmres is a krylov-solver-layer component, not shared gemv/trsv vocabulary). No overlap.

**#6 (abstractor conjugate-pair-reorder)** → writes findings to CYCLE.md (no artifact write). Depends on #2's audit output (the per-line dispatch rules). Wave-2 after #2 lands.

**Summary:** #1, #2, #4, #5 can run in parallel (no artifact write collisions). #3 depends on #1/#2 DISPATCHED (proposed-changes visible), so wave-2. #6 depends on #2 CYCLE.md output, so wave-2 after #2.

## Sequencing schedule

**Wave 1 (parallel):**
- #1 (abstractor: dot/scal/assemble-diagonal themes)
- #2 (lowering-verifier: inner-product-fold audit)
- #4 (harvester/lifter: gmres self-rotation)
- #5 (harvester: l3-vocab gemv/trsv)

**Wave 2 (parallel, after wave-1 reports land):**
- #3 (layer-intro-author: L2 refresh) — depends on #1/#2 proposed-changes blocks
- #6 (abstractor: conjugate-pair-reorder) — depends on #2 audit findings

## Open questions / caveats

- **#4 gmres carry-forward scope:** The current plan says "gmres.md §L4 v0.6→v0.7 self-rotation" — this is shorthand for "re-anchor the existing rough-in gmres.md to the current L4 strawman vocabulary" (likely `iterate_while` + state-threading rewrite) PLUS "firm the cycle-011 FGMRES sister theme(s)." Confirm with the dispatch author (harvester/lifter) whether the cycle-008 gmres slice and cycle-011 FGMRES slice both exist and whether they can be co-authored in one dispatch, OR if they should be separate. If scope exceeds context budget, split into gmres-self-rotation (#4a) and fgmres-self-rotation (#4b, held for cycle-021).

- **#5 l3-vocab gemv/trsv specifics:** The backlog item is sparse — "gemv/trsv L3 cohort growth." Confirm which L3 entries are ready (firm L2 anchors exist?) and how many to dispatch this cycle. If >2 entries, consider splitting into wave-2 (density). If no L2 anchors exist yet, this item may be blocked and should be held.

- **#3 L2-intro refresh:** Depends on #1/#2 proposed-changes being PROPOSED by the reports. If #1 or #2 has a report-phase failure (e.g., repairer finds unfixable issues), the intro author's input is degraded. In that case, the intro author should defer specific vocabulary-coverage prose until the next cycle when integrations land.

- **Codemap verification:** Paths verified for `palace/linalg/vector.hpp` (Dot, Scal sites) and `palace/linalg/iterative.hpp` (GmresSolver). No L0 path verification for GMRES yet — dispatcher should confirm `palace/linalg/iterative.cpp` contains GMRES impl. Ditto for l3-vocab gemv/trsv L0 sites (likely `palace/linalg/operator.hpp` or similar — verify at dispatch).

- **#2 lowering-verifier audit scope:** The theme has a per-line dispatch-rule + re-order-rule + summation-order table. Confirm with the lowering-verifier that the reported theme includes these sub-patterns and that the audit can exhaust them in one dispatch (not a multi-cycle work).
