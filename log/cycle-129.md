# cycle-129 — 2026-06-07 — batch-41 position 3/3 (the BATCH-CLOSING / THIRD & FINAL primary cycle)

**Meta-batch-41, position 3/3 (BATCH-CLOSING).** Cycles 127/128/129 form meta-batch-41; the batch-41 meta-phase fires AFTER this finalize, aggregating all three as a separate dispatch/commit. The cycle counter does NOT reset at batch boundaries. This finalize ran NO meta-phase housekeeping.

(Note: an unrelated slice-vertical-era `cycle-129` log from 2026-05-26 — `forward cg [L2→L3]` — was renamed to `log/cycle-129-slice-era.md` at this finalize to free the filename for the live layered-flow cycle-129; the cycle counter collided across the pre/post-redirect eras, matching the c123/c124/c125/c126/c127/c128 precedent.)

## Summary

A **light consolidation/cleanup cycle** closing the loose ends the c128 (batch-41 MIDDLE) cycle surfaced around the high-order **closure-returning-signature convention**. The convention is now **COMPLETE END-TO-END**: codified as semantics §1.3.1 (c128 D1), the operator-transformer/-constructor adjudication pinned (c129 D1), and the non-compliant cohort swept to the bracketed spelling + 2 stale maturity-tokens corrected (c129 D2).

**2 dispatches, both applied clean** (2/2 staging rows == 2 dispatched-ready — 110th consecutive clean staging), zero deferrals / rejections / per-report gate-hits, ZERO `cargo make book` build-repairs, ZERO within-finalize consistency fixes.

## What landed

- **D1 (layer-intro-author) — `transformer-codomain-adjudication`.** Pinned the operator-transformer/-constructor codomain adjudication into **semantics §1.3.1** (`book/src/semantics/index.md`, the active semantic-management surface): a bracketed `Op[...]` / `LinOp[...]` operator-VALUE codomain is **already compliant**; an opaque `LinearOperator[...]` type-application is **the non-compliant smell** (re-spell-not-wrap). Appended a ruling bullet after the c128 :155 reconciliation paragraph + a "Grouping" column + a third opaque-`LinearOperator[N,N]` row to the §1.3.1 table. EXTENDS the c128 reconciliation clause/table (preserved verbatim) and supplied the scope predicate D2's sweep consumed. **RESOLVES** OQ `oq-highorder-operator-transformer-codomain-convention`.
- **D2 (lifter, WAVE-2 dep D1) — `closure-signature-cohort-sweep`.** Re-spelled the **7 opaque `LinearOperator[...]` high-order/closure codomain sites** to the bracketed `LinOp[(N: ...), $N]` form: `L4/assemble_frequency_operator.md` (:99, :106, :127, :293), `L4/fe_assemble.md` (:60, :71, :35), and the 2 narrative `L4/index.md` rows (:61 eliminate_bc reconcile, :62 fe_assemble). Plus **2 evidenced stale maturity-token corrections** — `mk_matrix_free_operator` `roadmap_goal`→`firm` (c127) in `fe_assemble.md:16,164`; `boundary-mode.L4` `rough-in`→`firm` in `lifecycle.L4.md:72` (both nodes ALREADY firm on disk; the tokens were stale prose). **RESOLVES** OQ `highorder-signature-noncompliant-cohort-c129-lifter-sweep` + the 2 stale-token OQs (`fe-assemble-stale-mk-matrix-free-roadmap-goal-token`, `lifecycle-l4-stale-boundary-mode-rough-in-token`). **DELIBERATE within-chapter dual-spelling PRESERVED** (the plain operator-VALUE record fields stay rank-1 `LinearOperator[N, N]`) → routed to the META-owned §1.2.2 cohort sweep OQ `closure-signature-l4-constructor-restatement-compliance-cohort-sweep`.

## Build + linters

- **`cargo make book`** (mdbook + linkcheck2 0.12.0) — **EXIT 0**. ZERO build-repairs: D1/D2 made only prose + signature-spelling re-spell + 2 stale-token corrections; NO deletions → no linkcheck2 dead-link hazards; the §1.3.1 table edit and all re-spelled signatures resolve. Only pre-existing benign KaTeX / unclosed-HTML-tag (`<vector>`, `<opertype>`, …) / incomplete-markdown-link WARNs in files NOT touched this cycle (`solve_family.md`, `fe_collection.md`, `L1-L0/*`).
- **Step-5b graded-stack linters** (landed tree, ASK-1 `--reference-reachable` tier active): `rank_violations: 0` (GATE PASSES — nothing changed rank/edge, the invariant held trivially) + NO newly-orphaned node (`reachable` HELD 163) + `unresolved_depends_on_targets: 0` (HELD). **ALL totals HELD vs c127/c128 by design** (NO RE fired; no node maturity/edge changed — D1 semantic-surface prose, D2 signature re-spell + 2 stale-PROSE maturity-token corrections on already-firm-on-disk nodes; no count moved): `files=385, typed=324, untyped=61, roots=45, reachable=163, reference_reachable=247, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=10, detritus=122, true_detritus=50, detritus_reference_reachable_re11_cohort=72, expected_unreachable_outside_dag=48`. Both block-conditions PASS.

## Counts

- NO vocabulary count change (no status/rank flip; no file created/deleted). The 2 maturity-token corrections were stale-PROSE corrections on nodes already firm on disk, not status flips.
- SLICE CORPUS: 0.
- `rank_violations` trend: … → 0 (c126) → 0 (c127) → 0 (c128) → 0 (c129).

## Process

- retroactive-budget global = 0; per-report gates all PASS / N/A; 0 implied-component stubs; 0 OQs newly promoted by the per-report integrators (both reports' OQ actions were RESOLVED-flagging routed to the batch-41 meta's unify-authority, not ledger appends — finalize made no duplicate append).
- `scaffolding/{roadmap,integrator-signals,cycle-record}` + `log/` committed atomically with the 2 consumed-report `integrated_at` touches; two-phase SHA-patch follows.
- NO `.claude/agents/` changes FROM THIS FINALIZE (meta-phase domain — the batch-41 meta fires next, aggregating 127/128/129).

## THE CARRY to the BATCH-41 META (fires next, a SEPARATE dispatch aggregating 127/128/129)

1. **THE CENTRAL JUDGMENT — the ASK-2 "B" L4-COMPLETE CAPSTONE VERDICT** (from c128 D3): the in-scope FEATURE-SURFACE SPINE is **L4-COMPLETE** (all 5 drivers + lifecycle ROOT PASS; 12 named constituents verified firm on disk; 2 tracked opaque-library boundaries are NOT gaps; NO GAP). The audit recommends **DEFER + "wind the in-scope spine to MAINTENANCE"** (the E-fallback direction). The meta renders the maintenance-vs-continue verdict.
2. **The closure-signature convention is COMPLETE** (§1.3.1 codified c128 + transformer adjudication pinned c129 + cohort swept c129 + 2 stale tokens corrected). The meta decides the **2 DEFERRED items**: (a) whether to promote the `op-with-params {...}` introduction form into the §1.3 BNF, and (b) add a harvester/abstractor closure-returning-signature USE+LINK discipline bullet — OQ `closure-signature-introduction-form-into-bnf-and-role-discipline-bullet`.
3. **The meta-owned whole-book L4-constructor §1.2.2 compliance-cohort sweep** — OQ `closure-signature-l4-constructor-restatement-compliance-cohort-sweep`. D2 left the deliberate within-chapter dual-spelling (plain operator-VALUE record fields in rank-1 form) routed here. (Side-note: the `L4/index.md:119` dep-map TABLE cell still narrates `mk_matrix_free_operator` as `roadmap_goal` — out-of-cohort for the c129 prose-token sweep; the meta may fold the index TABLE-cell maturity-snapshot into a later sweep.)
4. **OQs RESOLVED this batch for the meta's unify-authority to CLOSE** in `open-questions.md`: `oq-highorder-operator-transformer-codomain-convention` (c129 D1), `highorder-signature-noncompliant-cohort-c129-lifter-sweep` (c129 D2), `fe-assemble-stale-mk-matrix-free-roadmap-goal-token` (c129 D2), `lifecycle-l4-stale-boundary-mode-rough-in-token` (c129 D2), and `matrix-free-operator-apply-l4-placeholder-now-stale` (DISCHARGED c128 D4).
5. **BATCH-41 "A then B" arc:** "A" (constructive-kernel / matrix-free) FULLY FIRM end-to-end (c127); "B" (5-driver L4-completeness capstone) DONE c128 = ALL-PASS L4-COMPLETE; the closure-signature loose ends ALL CLOSED c129. The meta judges whether to wind to maintenance (E fallback) per the capstone DEFER recommendation; D (P1 edge-typing / true-detritus sweep) opportunistic; C (sharding-math) deferred/gated. The meta reshapes `priorities.md` into the post-batch-41 head.
