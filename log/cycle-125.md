## 2026-06-07 cycle-125 — 3 reports applied clean — 120th consecutive cycle under split integrator — **POSITION 2/3 OF META-BATCH-40, THE MIDDLE PRIMARY CYCLE (cycles 124/125/126; the batch-40 meta-phase fires AFTER cycle-126's finalize, aggregating all three)** — **THE libCEED CONSTRUCTIVE-KERNEL SUBSTRATE SUB-SPINE IS NOW FULLY FIRM (L1 firm 45→47: `element_restrict` + `geom_factor_build` rough-in→firm; the `libceed-quadrature-kernel-impl` rough-in→firm) + A 2ND FAITHFUL SUBSTRATE CONSUMER (the new firm L2 combinator `matrix-free-operator-apply`, L2 firm 22→23 — the matrix-free / burn-GPU backend-lowering surface) GROUNDS IT FURTHER + the last batch-37-era stale `design/l4_calculus` path swept (1→0); `rank_violations` HELD 0; `unresolved_depends_on_targets` HELD 0; `reachable` HELD 157 (no orphaning); `reference_reachable` 235→243.** The batch-40 middle cycle under ASK-2 "A then B" (advance the constructive-kernel layer "A"). 3 dispatches, ALL applied clean. `cargo make book` EXIT 0, ZERO finalize build-repairs; graded-stack linter `rank_violations=0` (HELD) / `unresolved_depends_on_targets=0` (HELD).

# cycle-125 — 2026-06-07 — batch-40 position 2/3 (the MIDDLE primary cycle)

**Meta-batch-40, position 2/3 (MIDDLE).** Cycles 124/125/126 form meta-batch-40; the batch-40 meta-phase fires AFTER cycle-126's finalize, aggregating all three as a separate dispatch. The cycle counter does NOT reset at batch boundaries. This finalize ran NO meta-phase housekeeping.

(Note: an unrelated slice-vertical-era `cycle-125` log from 2026-05-26 — `refinement gmres [Ln→Ln]` — was renamed to `log/cycle-125-slice-era.md` at this finalize to free the filename for the live layered-flow cycle-125; the cycle counter collided across the pre/post-redirect eras, matching the c123/c124 precedent.)

Under the 2026-06-01 VOCABULARY-SHIFT REDIRECT + the 2026-06-04 GRADED RESOLUTION LADDER + FEATURE-ROOT REACHABILITY directive + the 2026-06-05 GROUND-don't-remove directive + the 2026-06-06 SEMANTIC CONSOLIDATION + OPEN-ALL-FEATURE-FRONTS directives + the 2026-06-07 RE-SCOPE (DIRECTIVE-1/2/3) + the 2026-06-07 ASK-2 forward-direction decision ("A then B").

## Headline

**The libCEED constructive-kernel substrate sub-spine is now FULLY FIRM + a 2nd faithful substrate consumer (the first matrix-free L2 combinator) grounds it further + the stale-path sweep is COMPLETE.** 3 dispatches, ALL applied clean (3/3 staging rows == 3 dispatched-ready; the cycle-018 staging-completeness gap did NOT recur — 106th consecutive clean staging). Zero deferrals, zero rejections, zero per-report gate-hits, ZERO finalize build-repairs.

Headline outcomes:
1. **The substrate sub-spine is now FULLY FIRM (ASK-2 "A").** D1 (harvester) flipped the two libCEED substrate ops `L1/element_restrict` + `L1/geom_factor_build` rough-in→FIRM (their sole blocking dep `concepts/element-local-tensor` is firm on disk since c124 D5 → `rank(u) ≤ min(deps) = firm`), COMPLETING the substrate sub-spine: `element_restrict` + `basis_apply` + `quad_point_contract` + `geom_factor_build` are now all firm. L1 firm tally **45→47** (33 main + 4 FE-assembly + 5 FE-space + 1 Mesh-construction + 4 libCEED-substrate). D1 also flipped the libCEED kernel-IMPL node `L1/libceed-quadrature-kernel-impl` rough-in→FIRM (all four `depends-on (composes)` substrate deps now firm). The `realizes-kernel-api` edge to the kept obstruction surface `L1-L0/fe-assemble-libceed-boundary-obstruction.md` stays `reference`-class; that kernel-api obstruction surface is UNTOUCHED (still `status: obstruction` / `sub_kind: opaque-library-ownership`) — DIRECTIVE-3 integrity preserved.
2. **A 2nd faithful substrate consumer — the first matrix-free L2 combinator.** D2 (abstractor) landed `book/src/L2/matrix-free-operator-apply.md` FIRM (L2 firm **22→23**) — the matrix-free / burn-GPU backend-lowering surface, a 2nd faithful `depends-on (composes)` consumer of the firm substrate (further grounding it). It introduced a new L2 by-kind group `Constructive-kernel compositions` + its navigational-container group-intro `constructive-kernel-compositions-intro.md`, both SUMMARY-registered. The L2↔L1 rotation is identity-in-named-terms (a degenerate-lowering smell per the vocabulary-shift redirect) → NO L2-L1 theme authored; resolved as the chapter's in-line "Downward to L1" note + a `reference`-class `lifts-kernel-impl` frontmatter edge (which constrains no rank, carries no liveness — correct per the kernel-api/impl + identity-in-named-terms discipline).
3. **GMG cross-ref hygiene — the stale-path sweep is COMPLETE.** D3 (combinator-miner) re-pointed `L1/multigrid-relaxation-smoother.md:113`'s last stale `design/l4_calculus.md §1.2.2` reference → live `semantics/index.md §1.2.1` (double-correction: path AND section — §1.2.2 is "Operator shapes", the rule lives at §1.2.1 "Named shape groups"). `grep -rn 'design/l4_calculus' book/src/` is now **0** (was 1). The batch-37-era drift residual is CLEARED; OQ `batch-37-era-stale-design-l4-calculus-path-drift-sweep` is flagged for the batch-40 meta to CLOSE. D3 also recorded two NEGATIVE-finding combinator-miner records (V-cycle do-not-mine — single instance `gmg.cpp:172`, AMG/aux-space speculation refuted; GMG-smoother-L3-home already-covered — body = firm `L2/correction_step` with L3 views, outer loop already homed as `L3/chebyshev` partial-obstruction).

## Build + step-5b (landed tree)

`cargo make book` (mdbook + linkcheck2 0.12.0) EXIT 0, **ZERO finalize build-repairs** (the new L2 chapter + group-intro + their SUMMARY/index inserts + the three firm-flips + the stale-path re-point ALL resolve clean; 0 dead links). Only the pre-existing benign `Potential incomplete link` / KaTeX-adjacent markdown-bracket WARNs in unrelated files (false positives on `[j]`/`[k+1]` array subscripts and the like).

**No deleted-slug frontmatter-edge class this cycle.** The c124 finalize was forced into two surgical build-repairs by D6's RE6 leaf-deletions leaving stale frontmatter `depends-on` edges (lint-invisible to linkcheck2, caught only by the graded-stack linter). This cycle had NO file deletions, so that gap did NOT recur. The "deleted-slug frontmatter-edge sweep" remains an owed codification into the destructive-refactor checklist (carried to the batch-40 meta).

**Step-5b graded-stack linters on the LANDED tree (ASK-1 `--reference-reachable` tier active):**
- **`rank_violations: 0`** (baseline fully discharged c096 → ANY violation NEW + BLOCK; NONE — GATE PASSES; the two substrate firm-flips rest on the firm `concepts/element-local-tensor`; the kernel-impl firm rests on its four-firm substrate; the new L2 combinator firm rests on its four-firm substrate constituents).
- **NO newly-orphaned node** (`reachable` HELD 157 — no previously-reachable node went dark; the three firm-flips are promotions of already-reachable nodes, and the new L2 combinator + group-intro added new reachable nodes).
- **`unresolved_depends_on_targets: 0`** (HELD; no deletions this cycle).
- TRUE CUMULATIVE: `files=385 (+2: the new L2 chapter + group-intro), typed=324 (+2), untyped=61 (HELD), roots=43 (HELD), reachable=157 (HELD), reference_reachable=243 (235→243, +8 — the new firm L2 chapter + substrate navigational reach), rank_violations=0 (HELD), unresolved_depends_on_targets=0 (HELD), promotion_frontier=10, detritus=128 (true_detritus=53; detritus_no_typed_edges_pre_p1_artifact=107, detritus_with_typed_edges_stronger_signal=21, detritus_reference_reachable_re11_cohort=75, stronger_signal_reference_reachable=14, stronger_signal_true_detritus=7), expected_unreachable_outside_dag=48, rank_histogram={firm:224, roadmap_goal:3, typed-no-rank:84, rough-in:4, partly-constructive:3, obstruction:2, partial-obstruction:4}`.
- **Both block-conditions PASS.**

## RE disposition (carried, owed to the batch-40 meta)

No RE change THIS cycle (the RE3/RE11/RE6 dispositions were the c124 outcomes). The batch-40 META STILL MUST update `scaffolding/graded-stack-baseline-exceptions.md` (meta write-territory) to record RE3 FIRED + the `eigsolve-impl`/`lanczos_step` RE11 rows GROUNDED + RE6 DISCHARGED per the rebuilt graph — the per-report integrators FLAGGED these but the file is meta-phase write-territory and remains un-updated.

## Counts

- L1 firm **45→47** (`element_restrict` + `geom_factor_build` rough-in→firm) — the substrate sub-spine COMPLETE.
- `libceed-quadrature-kernel-impl` rough-in→firm (kernel-impl kind, tracked separately).
- L2 firm **22→23** (`matrix-free-operator-apply`).
- +1 new L2 navigational-container group-intro (`constructive-kernel-compositions-intro`; no rank).
- SLICE CORPUS: 0.
- `rank_violations` trend 22 (c094) → 0 (c096) → … → 0 (c123) → 0 (c124) → 0 (c125).
- `reachable` 158 (c123) → 157 (c124) → 157 (c125, HELD); `reference_reachable` 235 (c124) → 243 (c125).

## Process

- retroactive-budget global = 0 (well below the ≥4 block); per-report gates all PASS/N/A; 0 implied-component stubs.
- 3 reports applied clean (3/3 staging rows == 3 dispatched-ready; 106th consecutive clean staging); zero deferrals / rejections / per-report gate-hits.
- ZERO finalize build-repairs.
- OQs promoted/closed by the per-report integrators (finalize made no duplicate append): CLOSED `libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup` (D1, executed exactly) + `batch-37-era-stale-design-l4-calculus-path-drift-sweep` RESIDUAL-CLEARED flag (D3, count 1→0, flagged for meta CLOSE); PROMOTED `matrix-free-operator-apply-l2-l1-no-theme-deliberate`, `matrix-free-operator-apply-role-vs-vocabulary-distinction`, `mk_matrix_free_operator-l4-backend-lowering-placeholder`, `matrix-free-operator-apply-amr-rebuild-consumer-forward-note` (D2); two NEGATIVE-finding resolution notes (V-cycle do-not-mine, GMG-smoother-L3-home already-covered — D3).
- `scaffolding/{roadmap,integrator-signals,cycle-record}` + `log/` committed atomically + the 3 consumed-report `integrated_at` touches; two-phase SHA-patch follows.
- NO `.claude/agents/` changes FROM THIS FINALIZE.

## The carry to c126 (batch-40 position 3/3, the BATCH-CLOSING cycle) + the batch-40 meta

1. **UPDATE `graded-stack-baseline-exceptions.md`** for RE3/RE11/RE6 (meta write-territory, carried from c124 — still un-updated).
2. **The L2/index prose-vs-dep-map-row firm-count gap** — D2 surfaced that the L2/index prose narrative firm count (now ~23) and the dep-map TABLE row count (~19–20 firm rows) have diverged; a pre-existing count-reconcile hygiene candidate for the meta.
3. **The owed lowering-verifier re-audit of the now-firm kernel-impl empirical-match** — the DIRECTIVE-3 impl-realizes-API correspondence audit should be re-run now that `libceed-quadrature-kernel-impl` is FIRM.
4. **The speculative L4 `mk_matrix_free_operator` placeholder** (OQ `mk_matrix_free_operator-l4-backend-lowering-placeholder`) — land as a roadmap_goal once the L4 backend-lowering feature surface provides the pull (c126/batch-41).
5. **CLOSE the discharged OQs** — `batch-37-era-stale-design-l4-calculus-path-drift-sweep` (count→0, sweep COMPLETE) + `libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup` (executed this cycle).
6. **CODIFY the "deleted-slug frontmatter-edge sweep"** into the destructive-refactor checklist (combinator-miner / integrator-per-report) — the c124 gap; did NOT recur this cycle (no deletions) but remains owed.
7. **ASK-2 "A then B" forward direction** — the constructive-kernel substrate layer + the first matrix-free L2 combinator are now firm; c126 advances toward the matrix-free assembly build + the 5-driver L4-completeness audit capstone ("B").

Written by `integrator-finalize` (split integrator-per-report ×3 + finalize ×1).
