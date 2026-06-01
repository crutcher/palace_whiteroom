---
agent: cycle-planner
invoked_at: 2026-06-01T210635Z
scope: cycle-051 dispatch plan
status: pending
---

# Cycle 051 dispatch plan

## Goals selected this cycle

Cycle-051 is the **THIRD and FINAL primary cycle of meta-batch-15** (cycles 049/050/051; the batch-15 meta-phase fires AFTER this finalize) and the **last refactor-pass enactment cycle before the meta-phase**. Under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, it lands the remaining refactor-pass slice the cycle-050 finalize hand-off identified (`integrator-signals.md` §cycle-050; `priorities.md` c050 hand-off note):

1. **Fold-family theme demotions** — ABSORB the `scal`/`axpy`/`axpby`/`axpbypcz`-`{body,leaf}-identity` themes into the new firm `L3/linear_combination` + `L2/linear_combination` in-line homes; ABSORB `dot`-`{body,leaf}-identity` into `inner_product`. **`nrm2` stays a do-NOT-merge CONSUMER** (its 2 themes demote-as-consumer onto the `nrm2` entry, NOT into the combinator).
2. **L3-leaf re-expression** — re-express `L3/{scal,axpy,axpby,axpbypcz}.md` through `L3/linear_combination`; `L3/dot.md` through `L3/inner_product` (bundled with each operator's demotion — same files).
3. **DEMOTE-OK c050 D8 verdicts** — `jacobi-smoother` (both edges) + `divfree-projector-body-identity` (L3>L2 ONLY); **KEEP `divfree-projector-leaf-identity` (L2>L1)** reachable from the L3 entry (D8 orphan-avoidance constraint — the one genuine `Grad->AddMult` fusion rotation).

This lands a coherent, complete refactor slice so the meta-phase sees the pass at a clean stopping point. The **leaf-chapter deletions stay HELD** for the batch-15 meta-phase (gated on `collapsed-leaf-disposition-convention-cohort-wide`). The degenerate-cohort demotion denominator is **17, not 18** (the D8 −1 correction: `divfree-projector-leaf-identity` KEEP).

## Deliverable-presence verification

Per the paste-inline-evidence requirement (friction-ledger `cycle-planner-stale-priorities-line-recruitment`). All scopes are refactor-pass demotions/re-expressions of EXISTING firm artifacts (open-by-the-redirect-program, not stale re-proposals); the checks confirm (a) the theme files to delete are PRESENT + firm, (b) the demotion homes (L3/L2 combinators) are PRESENT + firm, (c) the L3 leaves to re-express are firm and NOT yet through-combinator (work genuinely open). STOP-PROPOSING NEGATIVE LIST consulted: NONE of `{scal,axpy,axpby,axpbypcz,dot,nrm2,jacobi-smoother,divfree-projector,linear_combination,inner_product}` match `{lu_solve, back_solve, ls-update-column, 4 NLEPS atoms, apply_nonlinear_pencil-HELD}`.

**D1 (linear_combination family) — themes to DELETE (PRESENT+firm), leaves to RE-EXPRESS (firm, through-combinator=0), home (firm):**
```
L3-L2/scal-body-identity.md      : PRESENT  (## Status :206 "`firm` — identity-in-form L3>L2 edge")
L3-L2/axpy-body-identity.md      : PRESENT  (## Status firm)
L3-L2/axpby-body-identity.md     : PRESENT  (## Status firm)
L3-L2/axpbypcz-body-identity.md  : PRESENT  (## Status firm)
L2-L1/scal-leaf-identity.md      : PRESENT  (## Status firm)
L2-L1/axpy-leaf-identity.md      : PRESENT  (## Status firm)
L2-L1/axpby-leaf-identity.md     : PRESENT  (## Status firm)
L2-L1/axpbypcz-leaf-identity.md  : PRESENT  (## Status firm)
L3/scal.md                       : PRESENT  (## Status :118 firm)  | grep -c linear_combination = 0
L3/axpy.md                       : PRESENT  (## Status firm)       | grep -c linear_combination = 0
L3/axpby.md                      : PRESENT  (## Status firm)       | grep -c linear_combination = 0
L3/axpbypcz.md                   : PRESENT  (## Status firm)       | grep -c linear_combination = 0
L3/linear_combination.md (HOME)  : PRESENT  (## Status :148 "`firm` — propagate half … §Arity specializations the four arity forms")
```

**D2 (inner_product / dot family):**
```
L3-L2/dot-body-identity.md       : PRESENT  (## Status :NN firm — "L2/dot the same-named conjugation-axis leaf-floor of inner_product")
L2-L1/dot-leaf-identity.md       : PRESENT  (## Status firm)
L3/dot.md                        : PRESENT  (## Status :123 firm)  | grep -c inner_product = 0  (re-expression OPEN)
L3/inner_product.md (HOME)       : PRESENT  (## Status :NN firm; §"Downward to L2" pre-built "the pre-built home dot-body-identity demotes into at cycle-051")
```

**D3 (nrm2 consumer-demotion — do-NOT-merge):**
```
L3-L2/nrm2-body-identity.md      : PRESENT  (## Status firm — "CONSUMER of the fold (NOT a fold member)")
L2-L1/nrm2-leaf-identity.md      : PRESENT  (## Status firm)
L3/nrm2.md (in-line home)        : PRESENT  (## Status firm)   | demote-as-consumer (NOT absorbed into inner_product)
```

**D4 (jacobi DEMOTE-OK both edges + divfree L3>L2 DEMOTE-OK, divfree L2>L1 KEEP):**
```
L3-L2/jacobi-smoother-body-identity.md      : PRESENT  (## Status firm)  -> DEMOTE
L2-L1/jacobi-smoother-leaf-identity.md      : PRESENT  (## Status firm)  -> DEMOTE
L3-L2/divfree-projector-body-identity.md    : PRESENT  (## Status firm)  -> DEMOTE
L2-L1/divfree-projector-leaf-identity.md    : PRESENT  (## Status :253 "`firm` — fusion-rotation floor (D6 wave-1) … exactly one genuine fusion rotation Grad->AddMult")  -> **KEEP** (D8 verdict; the −1 denominator correction)
```

**OQ-ledger / structural-block checks:** no RESOLVED/CLOSED grep hits against any c051 demotion slug (these are c050-hand-off-routed forward work, open by construction of the refactor program). No structural-block gate: all endpoints firm; the demotions are vehicle-changes (theme file → in-line note), not promotions. The leaf-chapter-deletion structural gate (`collapsed-leaf-disposition-convention-cohort-wide`, batch-15-meta-gated) is HONORED — this plan touches NO held-for-deletion chapter beyond re-expression-in-place of the firm L3 leaves (which is convention-independent: re-expression keeps the leaf chapters present, whichever disposition the meta-phase ratifies).

## Dispatches

Total: **5 dispatches** (well under the 12 cap). Each fold-member's demotion + L3-leaf re-expression is BUNDLED into ONE dispatch per family (so a given operator's files are touched by exactly one dispatch — avoids the same-file two-writer overlap the task brief flagged). Routing per the hand-off: demotions/re-expressions → `lifter`; consolidated tally → `layer-intro-author` count-owner.

**D1 — `lifter` — `linear_combination` family: demote 8 themes + re-express 4 L3 leaves.**
- **scope:** ABSORB-into-combinator-note the fold-family `linear_combination` member themes: delete `book/src/L3-L2/{scal,axpy,axpby,axpbypcz}-body-identity.md` (4 L3>L2) + `book/src/L2-L1/{scal,axpy,axpby,axpbypcz}-leaf-identity.md` (4 L2>L1) = **8 theme files deleted**, their identity-in-form content absorbed into the pre-built §"Arity specializations" / §"Downward to L2" homes in `book/src/L3/linear_combination.md` + `book/src/L2/linear_combination.md` (do NOT re-author the homes' substance — the c050/c049 maps already pre-built them; add only the per-arity absorption pointer if a home lacks it). **Re-express** `book/src/L3/{scal,axpy,axpby,axpbypcz}.md` to speak THROUGH `L3/linear_combination` (the arity-N specialization framing: `scal = linear_combination [(α,x)]`, etc.) rather than re-deriving the base form — replace each leaf's §"Downward to L1" base-form derivation + its `lowers_to:`/§"Lowers-to" references to the now-deleted `*-body-identity` theme with the combinator-routed framing (`L3/<op>` is the arity-N specialization of `L3/linear_combination`; the substantive arity-dispatch translation lives in the KEPT `L2-L1/linear-combination-fold-specialization` theme). Re-anchor all inbound live links to the 8 deleted slugs (defensive de-link per the c050 multi-deletion pattern; the cross-references map: `axpy/axpby/axpbypcz-body-identity` link to `scal-body-identity` + `dot-body-identity`, all within the demotion set — de-link in-flight). **Remove D1's OWN 8 SUMMARY.md lines** (`SUMMARY.md:52,53,56` body-identity `axpy/axpby/scal` + `:92,95,96,97` leaf-identity + the `axpy-body-identity` line) AND **its OWN dep-map ROWS** in `L3-L2/index.md` + `L2-L1/index.md` (per the c050 friction note: de-link AND physically remove the row in one step — do NOT leave de-linked-but-present rows for finalize). **DEFER the consolidated tally** in all three indexes to D5.
- **deps:** none (combinator homes already firm on disk; D2/D3/D4 touch disjoint operators).
- **rationale:** the highest-fan-out refactor-pass item this cycle (4 of the 5 fold members + their 8 themes). Serves `refactor-pass-c051-fold-family-demotions` + `refactor-pass-l3-leaf-re-expression`. The bundling (demotion + re-expression in one dispatch) keeps each L3 leaf file single-writer.

**D2 — `lifter` — `inner_product`/`dot` family: demote 2 themes + re-express `L3/dot`.**
- **scope:** ABSORB-into-combinator-note the `dot` fold-member themes: delete `book/src/L3-L2/dot-body-identity.md` (L3>L2) + `book/src/L2-L1/dot-leaf-identity.md` (L2>L1) = **2 theme files deleted**, absorbed into the pre-built §"Downward to L2" home in `book/src/L3/inner_product.md` ("the pre-built home dot-body-identity demotes into at cycle-051") + `book/src/L2/inner_product.md`. **Re-express** `book/src/L3/dot.md` to speak THROUGH `L3/inner_product` (`dot` = the Hermitian/symmetric conjugation specialization of `inner_product` at `M=I`; `tdot` = the unconjugated bilinear specialization) rather than re-deriving the reduce-to-scalar base form — replace `L3/dot.md`'s §"Downward to L1" base-form framing + its references to the deleted `dot-body-identity` with the combinator-routed framing (the substantive conjugation/weight-dispatch translation lives in the KEPT `L2-L1/inner-product-fold-specialization` theme). Re-anchor inbound live links to the 2 deleted slugs (defensive de-link; note `divfree-projector-body-identity` (D4) + the `axpy/axpby` themes (D1) link to `dot-body-identity` — cross-dispatch dangling resolves via per-report defensive de-link). **Remove D2's OWN SUMMARY.md lines** (`:50` dot-body-identity + `:94` dot-leaf-identity) + its OWN dep-map ROWS in both indexes (de-link AND remove in one step). **DEFER the consolidated tally** to D5.
- **deps:** none (parallel-safe with D1: disjoint operators + disjoint combinator homes — D1 owns `linear_combination`+`L3/{scal,axpy,axpby,axpbypcz}`, D2 owns `inner_product`+`L3/dot`).
- **rationale:** the `inner_product` fold member (`dot`). Serves `refactor-pass-c051-fold-family-demotions` + `refactor-pass-l3-leaf-re-expression`.

**D3 — `lifter` — `nrm2` consumer-demotion (do-NOT-merge).**
- **scope:** DEMOTE-as-CONSUMER the `nrm2` themes: delete `book/src/L3-L2/nrm2-body-identity.md` (L3>L2) + `book/src/L2-L1/nrm2-leaf-identity.md` (L2>L1) = **2 theme files deleted**, their content demoted to in-line §"Downward to L2" / §"Downward to L1" notes ON the `book/src/L3/nrm2.md` + `book/src/L2/nrm2.md` operator entries themselves — **NOT absorbed into `inner_product`** (`nrm2` is the `√ ∘ abs ∘ inner_product` CONSUMER at `y=x`, NOT a fold member; the do-NOT-merge consumer carve-out, ledger `:595` / hand-off note (1)). The in-line note records: the body is identity-in-form across the L3>L2 / L2>L1 edges; `nrm2` consumes `inner_product` but is not a specialization of it; the `std::abs` load-bearing guard preserved as an explicit claim. Re-anchor inbound live links to the 2 deleted slugs (defensive de-link; `divfree-projector-body-identity` (D4) links to `nrm2-body-identity`). **Remove D3's OWN SUMMARY.md lines** (`:54` nrm2-body-identity + `:98` nrm2-leaf-identity) + its OWN dep-map ROWS in both indexes (de-link AND remove). **DEFER the consolidated tally** to D5.
- **deps:** none (disjoint operator from D1/D2/D4; `nrm2` entry single-writer).
- **rationale:** the consumer half of the BLAS-1 reduction cohort — demoted-as-consumer, the carve-out the redirect + c049 D2/D3 reconciliation pinned. Serves `refactor-pass-c051-fold-family-demotions` (consumer slice).

**D4 — `lifter` — jacobi-smoother (both edges) + divfree-projector L3>L2 demote, divfree L2>L1 KEEP.**
- **scope:** Enact the c050 D8 DEMOTE-OK verdicts (`reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`): **(a)** `jacobi-smoother` BOTH edges DEMOTE-OK — delete `book/src/L3-L2/jacobi-smoother-body-identity.md` + `book/src/L2-L1/jacobi-smoother-leaf-identity.md` (2 files), demote to in-line §"Downward" notes on `book/src/L3/jacobi-smoother.md` + `book/src/L2/jacobi-smoother.md`. **(b)** `divfree-projector-body-identity` (L3>L2) DEMOTE-OK — delete `book/src/L3-L2/divfree-projector-body-identity.md` (1 file), demote to an in-line §"Downward to L2" note on `book/src/L3/divfree-projector.md`. **(c) CRITICAL — KEEP `book/src/L2-L1/divfree-projector-leaf-identity.md` (L2>L1) — do NOT delete it.** It is the one genuine `Grad->AddMult` step-4 fusion rotation (anchored `divfree.cpp:185`/`:180-181`). The c051 divfree L3>L2 demotion MUST keep the L2 floor (`L2/divfree-projector.md`) + that KEPT L2>L1 fusion theme **reachable from the L3 entry** (D8 orphan-avoidance constraint, OQ `divfree-l3-l2-demotion-must-keep-l2-floor-and-l2-l1-fusion-reachable`): the new in-line §"Downward to L2" note on `L3/divfree-projector.md` (replacing the deleted-body-identity reference at `:6`,`:92`,`:106`,`:476`) must point onward to the L2 floor AND its KEPT `L2-L1/divfree-projector-leaf-identity` fusion theme, so the genuine rotation is not stranded. **Total deleted by D4: 3 theme files** (jacobi ×2 + divfree-body-identity ×1). Re-anchor inbound live links to the 3 deleted slugs (defensive de-link; `jacobi-smoother-body-identity` links to `scal-body-identity` (D1); `divfree-projector-body-identity` links to `dot/nrm2/scal-body-identity` (D2/D3/D1)). **Remove D4's OWN SUMMARY.md lines** (`:57` jacobi-body-identity, `:58` divfree-body-identity, `:99` jacobi-leaf-identity — do NOT touch the `divfree-projector-leaf-identity` SUMMARY line, it survives) + its OWN dep-map ROWS in both indexes for the 3 deleted slugs (keep the divfree-leaf-identity row). **DEFER the consolidated tally** to D5.
- **deps:** none (disjoint operators; `jacobi-smoother`/`divfree-projector` entries single-writer).
- **rationale:** closes the c050 D8 verify-body worklist; the KEEP constraint is the one non-mechanical subtlety this cycle. Serves `refactor-pass-c051-jacobi-divfree-demotion`.

**D5 — `layer-intro-author` — SOLE consolidated-tally owner this cycle.**
- **scope:** SOLE owner of the **consolidated firm-count tallies** in `book/src/L3-L2/index.md` + `book/src/L2-L1/index.md` + `book/src/L3/index.md` (count-ownership convention; D1–D4 defer ALL tallies to D5 and write only their own SUMMARY lines + own dep-map rows). After this cycle's deletions: **L3>L2 firm 13 → 13 − 7 = 6** (deleted: `scal/axpy/axpby/axpbypcz/dot/nrm2/jacobi-smoother-body-identity` (7) + `divfree-projector-body-identity` (1) = **8** L3>L2 deletions → 13 − 8 = **5**; recompute against on-disk post-D1–D4 state, do NOT trust this arithmetic blind — count the surviving `L3-L2/*.md` firm entries directly); **L2>L1 firm 17 → 17 − 7 = 10** (deleted: `scal/axpy/axpby/axpbypcz/dot/nrm2/jacobi-smoother-leaf-identity` (7) L2>L1 deletions; **`divfree-projector-leaf-identity` SURVIVES** — KEEP); **L3 firm 17 (UNCHANGED** — the L3 leaves are re-expressed in place, not deleted; the 2 combinators already counted in the c050 17). Reconcile the §Working-Notes degenerate-cohort narrative: the 17-denominator cohort is now **fully discharged** (15 demoted this cycle: 10 fold + 2 nrm2-consumer + 2 jacobi + 1 divfree-L3>L2; the 16th member `divfree-projector-leaf-identity` KEPT-substantive as the lone genuine fusion rotation; `krylov-step-body-identity` was never a degenerate-cohort member — it is the substantive multi-primitive KEEP). Record that the refactor-pass theme-demotion sweep is COMPLETE at the clean batch-15-meta stopping point; the leaf-chapter deletions remain HELD/meta-gated. **Compute every absolute count from on-disk reality** (`ls`/`grep` the surviving entries after D1–D4 land) — the per-report integrators apply D1–D4 serially before D5, so D5 reads the settled state.
- **deps:** D1, D2, D3, D4 (must read the post-demotion on-disk state to write correct consolidated tallies).
- **rationale:** the count-ownership convention (cycle-039 meta; held clean at 8-wide in c050). Exactly one consolidated-tally writer avoids the parallel-blind divergence. Serves `refactor-pass-c051-count-ownership`.

## Overlap analysis

Pairwise (the overlap reasoning IS the plan):

- **D1 × D2:** Disjoint at the operator + combinator-home level — D1 owns `L3/linear_combination` + `L3/{scal,axpy,axpby,axpbypcz}` + the 8 `linear_combination`-family theme files; D2 owns `L3/inner_product` + `L3/dot` + the 2 `dot` theme files. **Shared files:** SUMMARY.md, `L3-L2/index.md`, `L2-L1/index.md` (each removes its OWN anchor-distinct lines/rows — parallel-safe per the distinct-rows convention). **Cross-deletion dangling:** D1's `axpy/axpby-body-identity` link to `dot-body-identity` (D2-deleted); resolves via the c050 per-report defensive-de-link pattern. **Verdict: PARALLEL** (conflict-tolerance: anchor-distinct index/SUMMARY edits + validated defensive-de-link; minor merge is cheap signal).
- **D1 × D3:** Disjoint operators (`nrm2` ≠ linear_combination members). Shared SUMMARY/indexes (anchor-distinct). Cross-deletion: none of D1's deletions link to nrm2 themes; `nrm2-body-identity` (D3) is referenced by `divfree-projector-body-identity` (D4), not D1. **Verdict: PARALLEL.**
- **D1 × D4:** Disjoint operators. Cross-deletion: D4's `jacobi-smoother-body-identity` + `divfree-projector-body-identity` link to `scal-body-identity` (D1-deleted) — defensive de-link. Shared SUMMARY/indexes anchor-distinct. **Verdict: PARALLEL.**
- **D2 × D3:** Disjoint operators; `inner_product` (D2) vs `nrm2`-entry-in-line (D3, do-NOT-merge so D3 does NOT touch `inner_product`). **Verdict: PARALLEL.**
- **D2 × D4:** Disjoint operators. Cross-deletion: `divfree-projector-body-identity` (D4) links to `dot-body-identity` (D2-deleted) — defensive de-link. **Verdict: PARALLEL.**
- **D3 × D4:** Disjoint operators. Cross-deletion: `divfree-projector-body-identity` (D4) links to `nrm2-body-identity` (D3-deleted) — defensive de-link. **Verdict: PARALLEL.**
- **D5 × {D1,D2,D3,D4}:** D5 (count-owner) writes ONLY the consolidated tallies in the three indexes; D1–D4 write ONLY their own SUMMARY lines + own dep-map rows and DEFER the tally. Anchor-distinct on the index files (tally aggregate vs individual rows). But D5 must read the SETTLED post-demotion state to compute correct absolute counts. **Verdict: D5 is SEQUENTIAL AFTER D1–D4** (count-ownership + read-settled-state dependency).

The brief's same-file two-writer concern is structurally avoided: each fold-member operator's demotion + re-expression is in ONE dispatch (no L3 leaf touched twice); the only genuinely shared mutable derived value (the consolidated index tally) has exactly ONE owner (D5).

## Sequencing schedule

- **Wave 1 (PARALLEL):** D1, D2, D3, D4 — the four demotion/re-expression dispatches. All operator-disjoint; shared SUMMARY/index edits are anchor-distinct (own-row removal); cross-deletion dangling links handled by the validated c050 per-report defensive-de-link pattern. **Deletion-ordering hint for the per-report integrators** (signal from c050 §Wave-conflict): the demotion targets cross-reference each other densely — apply in the order **D1 → D2 → D3 → D4** if the integrator prefers a deletion-order over defensive-de-link, since `divfree-projector-body-identity` (D4) holds inbound links to the most other deleted slugs (de-link-last minimizes in-flight de-links); either mechanism is clean.
- **Wave 2 (after wave-1 reports land):** D5 — `layer-intro-author` consolidated-tally owner, reading the settled post-demotion on-disk state.

Per-report integration is serial within each wave (artifact writes serialize); ONE `integrator-finalize` runs once at cycle end (rebuild + commit + push + the finalize-time physical dep-map-row sweep if any de-linked-but-present rows survive — though this cycle instructs each producer to de-link AND remove its own rows in one step, per the c050 friction note, so the finalize sweep should find zero residual rows).

## What lands c051 vs carries to batch-16 vs stays HELD

**LANDS this cycle (the complete refactor-pass theme-demotion slice):**
- 15 degenerate theme files deleted (10 fold-family + 2 nrm2-consumer + 2 jacobi + 1 divfree-L3>L2), content demoted to in-line notes.
- `L3/{scal,axpy,axpby,axpbypcz,dot}` re-expressed THROUGH the L3 combinators.
- `divfree-projector-leaf-identity` (L2>L1) KEPT + kept reachable from `L3/divfree-projector` (orphan-avoidance).
- Consolidated tallies reconciled (L3>L2 13→~5, L2>L1 17→~10, L3 17 unchanged — D5 computes from on-disk).

**HELD for the batch-15 meta-phase (do NOT propose/enact c051):**
- The leaf-chapter deletions / redirect-stubs (`L2/{dot,scal,axpy,axpby,axpbypcz}.md`, `L3/{...}.md`, the D1 `scal` redirect-stub) — gated on the meta-phase ratifying `collapsed-leaf-disposition-convention-cohort-wide`. c051 keeps every leaf chapter PRESENT (re-expressed in place); the delete-vs-redirect-stub disposition is the meta-gated step.
- Closing `linear-combination-fork-OQs-superseded-by-2026-06-01-redirect`; the `inner-product-fold-specialization-citation-drift` firming touch; the `specialized-agent-direct-write-to-book-during-dispatch` recurrence assessment; the de-linked-but-present-dep-map-row tooling/convention gap (c050 friction note).
- `apply_nonlinear_pencil` L3 stays HELD (folds into a future eigsolve-variant pass).

**Carries to batch-16 (post-meta, if it does not fit cleanly this cycle):** any re-expression nuance that the per-report critics flag as needing more than a mechanical re-anchor (e.g. if a leaf's algebraic-laws section needs substantive rework to speak through the combinator rather than a framing swap) — do NOT force it into c051; flag and carry. The redirect program item 2 (continued shared-spine combinator-miner abstraction) + item 3 (solvers as low-priority test-load) are post-refactor-pass and are the batch-16 frontier the meta-phase reshapes the active head toward.

## priorities.md update

Marked the c051 dispatches in the c050 active head's §"Sequenced to cycle-051" line as DISPATCHED (D1–D5) and reaffirmed the HELD leaf-chapter-deletion gate + the 17-not-18 denominator. No new backlog candidates surfaced this cycle (the refactor-pass worklist is fully enumerated by the c049 D3 audit + c050 D8 verdicts).

## Open questions / caveats

- **D5 absolute-count arithmetic must be computed on-disk, not from this plan's projections.** I gave projected deltas (L3>L2 13→~5, L2>L1 17→~10) but the exact firm counts depend on which entries the L3-L2/index currently tallies as "firm" vs the substantive KEEPs (`krylov-step-body-identity`, `ksp-solve-outer-driver`, `orthogonalize-variant-split`, `chebyshev-nested-recurrence`, `eigsolve-opaque-eigen-iteration`, the 4 non-fold demotions already done c050). D5's scope explicitly instructs counting surviving on-disk firm entries directly — flagged so the orchestrator's brief reinforces it.
- **Meta-phase pre-flag (batch-15 fires after this finalize):** the c050 §Integration-tooling-friction note (de-linked-but-present dep-map rows are a foreseeable multi-deletion residual) recurs structurally in this cycle's 4-way deletion. I have instructed each producer to de-link AND physically remove its own dep-map rows in one step (the c050 recommended convention). If the per-report critics/integrators show this still leaks residual rows to finalize, the meta-phase should codify the "de-link-and-remove-in-one-step" OR "count-owner-scope-includes-row-removal" convention (friction-ledger candidate). Surfacing here per the cadence note since the friction-ledger entry is not yet written.
- **Refactor-pass completeness for the meta-phase:** after c051, the theme-demotion half of the refactor pass is COMPLETE (all 17 degenerate-cohort members dispositioned: 16 demoted across c050+c051, 1 KEPT). The OPEN refactor-pass remainder for the meta-phase + batch-16 is exclusively the leaf-chapter disposition (the meta-gated `collapsed-leaf-disposition-convention-cohort-wide`) + any L4-propagation-depth follow-up (`l4-propagation-depth-linear-combination`, "flag don't force" low-priority). The pass is at a clean stopping point.
