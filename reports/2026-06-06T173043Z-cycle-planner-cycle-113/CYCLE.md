---
agent: cycle-planner
invoked_at: 2026-06-06T173043Z
scope: cycle-113 dispatch plan
status: pending
---

# Cycle 113 dispatch plan

## Goals selected this cycle

PIVOT off blind lazy-tail typing. The cycle-112 F1 finding re-baselines the LEAD campaign: the `untyped: 60` count does NOT decrement for the remaining L3 mid-nodes (the linter auto-migrates their pre-existing legacy `lowers_to`/`lifts_from` → they are already shim-counted typed), so continued blind typing of the remaining L3 mid-node tail is LOW measurable value (no reachability delta, no untyped-count delta — only a representation upgrade). The clean forward-vocabulary frontier is exhausted (`promotion_frontier: 8` all obstruction-/demand-gated) and all 40 feature columns are off `seed`. The genuinely highest-fan-out move this cycle is therefore an **audit-first cross-cutter sweep** to FIND the next faithful reachability-grounding edges among the 25-member STRONGER GARBAGE SIGNAL set (the find-step that unblocks all further reachability movement), PLUS apply the one already-confirmed faithful grounding edge (a real +1: the `set-subvector-zero-mutation-rotation` theme its c107 op-grounding missed). Two dispatches, one wave.

## Dispatches

### D1 — `cross-layer-cross-cutter` (MEDIUM-HIGH, WAVE-1)
- **scope:** AUDIT-FIRST characterization of the **11 un-baseline-excepted STRONGER GARBAGE SIGNAL members** (the 25-set minus the RE1-RE5-covered subset). The 11: `L1/weak_form_term`; the axpy-family arity-specializations `L2/{axpy,axpby,axpbypcz}` + `L3/{axpy,axpby,axpbypcz}`; the degenerate identity leaves `L2/elementwise_product` + `L3/elementwise_product` + `L3/assemble-diagonal`; the iteration-views `L3/fold_solve` + `L3/krylov-step`. (`L1-L0/set-subvector-zero-mutation-rotation` is the 12th un-excepted member — D2 grounds it; D1 names it as the worked exemplar of the groundable class and confirms.) For EACH member apply §2f FAITHFUL-PATH-OR-FINDING: read the chapter prose, determine whether a FAITHFUL inbound `depends-on` grounding edge exists from a reachable node, vs whether it is an absorbed-below-column / unconsumed-iteration-view that should be RATIFIED as a NEW reachability baseline-exception (RE6+) at the batch-36 meta-phase. **Observation-only — DO NOT author any artifact edge** (writes its own CYCLE.md observation). Route the groundable subset (if any beyond `set-subvector-zero`) as a finding for a c114 grounding dispatch; route the baseline-exception subset as a structured RE6+ recommendation for the batch-36 meta-phase.
- **deps:** none.
- **rationale:** Serves priorities item-1's re-baselined remainder (the LEAD, now audit-first per F1) + the standing graded-stack GC duty. The 25-member STRONGER GARBAGE SIGNAL is the dominant remaining detritus mass; ~14 nodes are already ratified (RE1-RE5), the un-excepted ~11 have never been dispositioned. This is the find-step the redirect mandates ("what a solver/spine can't cleanly say is a finding") — it surfaces the next grounding tranche AND the meta-phase RE-ratification batch, unblocking all further reachability movement. Pre-trace expected partition (the cross-cutter VERIFIES, does not assume): axpy-family = absorbed into the reachable `linear_combination` combinator (combinator-primary — the specializations are leaves nothing composes by name; `L3/axpy.md` prose explicitly "routes through the combinator's identity edge") → RE6 candidate; elementwise/assemble-diagonal = degenerate identity leaves absorbed into the RE1 preconditioner/diagonal-apply bodies → RE1-extension; `L3/{fold_solve,krylov-step}` = RE2-shaped iteration-views (the reachable `L4/krylov-step` composes the L2 surface directly, not the L3 iteration-view) → RE2-extension; `L1/weak_form_term` = consumed only by the garbage `L1-L0/fe-assemble-libceed-boundary-obstruction` (characterize that leg too).

### D2 — `layer-intro-author` (MEDIUM, WAVE-1)
- **scope:** Apply the **one already-confirmed faithful grounding edge** — `L1/set_subvector_zero → L1-L0/set-subvector-zero-mutation-rotation`, a `lowers-to`-kind `depends-on` edge (the c108-codified §5 L1-op-points-at-theme asymmetric convention). Currently the theme is a `reference` (navigational) edge only in `L1/set_subvector_zero.md`'s frontmatter; UPGRADE it to a `depends-on (kind: lowers-to)` edge (keep/relocate the `reference` per the scheme). Single-file frontmatter edit to `book/src/L1/set_subvector_zero.md`. **CAUTION — the existing frontmatter prose in that file asserts a `depends-on` to the theme would be a "rank-direction error"; that prose predates the c108 §5 L1-op→theme grounding convention and must be UPDATED in the same edit, not worked around** (cite the c108 `bc-elimination-post-composition-dissolution` / `divfree-projector-mutation-rotation` precedent + the `book/src/methodology/graded-stack-scheme.md` §5 note). Re-run the linter; confirm the theme flips reachable (`reachable` 123→124, `detritus` −1, STRONGER GARBAGE SIGNAL 25→24), `rank_violations` HOLDS 0.
- **deps:** none (the edge faithfulness is already confirmed by the planner's trace; D1 corroborates in parallel but does not gate D2).
- **rationale:** A real +1 on the reachability axis — the residual half of the `set-subvector-zero-cluster-reachability` (the OP was grounded c107 via the divfree leg; its L1>L0 THEME was missed). This is the exact `lowering-chain-liveness-not-propagated-to-l1-ops` pattern c108 D1 resolved for the BC/divfree chains, applied to the one chain the c108 sweep didn't reach. Demonstrates the L1>L0-theme-grounding move D1's audit may surface more of (so c114 can apply the rest). The chain is on disk: `feature/eigenmode.L4 → L3/divfree-projector → L1/set_subvector_zero` (reachable); the theme is `rank: firm` → `rank(op=3) ≤ rank(theme=3)` holds.

## Deliverable-presence verification

Per the MANDATORY pre-dispatch four-step check (paste-inline evidence).

### D1 (`cross-layer-cross-cutter`) — OPEN BY CONSTRUCTION
This is a fresh observation dispatch (no prior-cycle history; the 25-member STRONGER GARBAGE SIGNAL set has never been audited for un-excepted-member disposition). Cross-cutter writes only CYCLE.md (no named-artifact-slug deliverable under `book/src/`). The four-step file-presence/maturity check does not apply. The 25-set + RE-coverage partition that scopes D1 is pasted below (linter + baseline-exceptions cross-check), so D1 is precisely targeted, not speculative.

**Live linter STRONGER GARBAGE SIGNAL (25), measured on the clean landed tree this invocation:**
```
L1-L0/set-subvector-zero-mutation-rotation   L1/normalize   L1/weak_form_term
L2/axpby   L2/axpbypcz   L2/axpy   L2/elementwise_product   L2/jacobi-smoother
L2/normalize   L2/reciprocal   L2/scal   L3/assemble-diagonal   L3/axpby
L3/axpbypcz   L3/axpy   L3/chebyshev   L3/elementwise_product   L3/fold_solve
L3/jacobi-smoother   L3/krylov-step   L3/normalize   L3/orthogonalize
L3/reciprocal   L3/scal   L4/preconditioning-framework
```
**RE1-RE5 baseline-excepted subset (14, from `scaffolding/graded-stack-baseline-exceptions.md`):** `L4/preconditioning-framework`, `L2/jacobi-smoother`, `L3/jacobi-smoother`, `L3/chebyshev` (RE1); `L3/orthogonalize` (RE2); `L1/normalize`, `L2/normalize`, `L3/normalize`, `L2/reciprocal`, `L3/reciprocal`, `L2/scal`, `L3/scal` (RE5, "normalize/reciprocal/scal internal-utility chain").
**→ Un-excepted residual (11) = D1's target list:** `L1/weak_form_term`, `L2/{axpy,axpby,axpbypcz}`, `L3/{axpy,axpby,axpbypcz}`, `L2/elementwise_product`, `L3/elementwise_product`, `L3/assemble-diagonal`, `L3/fold_solve`, `L3/krylov-step` (+ `L1-L0/set-subvector-zero-mutation-rotation` handed to D2).

### D2 (`layer-intro-author`) — target `book/src/L1/set_subvector_zero.md`
1. **File existence:**
```
-rw-rw-r-- 1 crutcher crutcher 24662 Jun  6 03:56 book/src/L1/set_subvector_zero.md   → EXISTS
-rw-rw-r-- 1 crutcher crutcher 25284 Jun  6 03:56 book/src/L1-L0/set-subvector-zero-mutation-rotation.md   → THEME EXISTS
```
2. **Maturity / already-discharged check:** `L1/set_subvector_zero.md` reads `rank: firm`. The deliverable is NOT a maturity promotion — it is an edge-kind UPGRADE (`reference` → `depends-on (kind: lowers-to)` to the theme). Confirmed NOT already present:
```
$ grep -A2 "kind: lowers-to" book/src/L1/set_subvector_zero.md | grep -i "set-subvector-zero-mutation-rotation"
   → NO lowers-to depends-on edge to theme present → D2 is OPEN (not a no-op)
```
The theme currently appears ONLY in the `reference:` bucket (verified in the edges block: `- L1-L0/set-subvector-zero-mutation-rotation   # ... downward navigational pointer, NOT a rank-blocking dependency`).
3. **OQ-ledger RESOLVED-grep:**
```
$ grep -iE "set-subvector-zero.*(RESOLVED|CLOSED|grounding)" scaffolding/open-questions.md
- `set-subvector-zero-mutation-rotation-theme-forthcoming` — CLOSED c105 D4 (theme authored firm) ...
- `set-subvector-zero-cluster-reachability-not-rescued-by-reference-backlink` (c106 D4) — CLOSED grounded-and-rescued (c107 D1) via the divfree leg ... The c106 `reference` back-link carried no liveness; the `depends-on` edges do.
```
The c107 closure grounded the OP only; the THEME's reachability is a DISTINCT residual not closed by either entry (the theme is still `[GARBAGE*]` on the live tree — confirmed in the STRONGER GARBAGE SIGNAL list above). D2 is OPEN.
4. **Structural-block check:** No methodology gate blocks D2. The opposite — the c108 batch-34 meta-phase CODIFIED the §2f GROUND-don't-remove disposition + the `graded-stack-scheme.md` §5 L1-op→theme grounding convention precisely to enable this edge. The only friction is the stale in-file prose ("rank-direction error"), which the dispatch scope explicitly directs the producer to update (with the c108 precedent citation), not work around. Well-foundedness holds (firm op ≤ firm theme).

**Reachability trace confirming faithfulness (`--show-inbound`, this invocation):**
```
L1/set_subvector_zero  <-  L1-L0/set-subvector-zero-mutation-rotation, L3/divfree-projector
L3/divfree-projector   <-  feature/eigenmode.L4
```
→ `L1/set_subvector_zero` is reachable from root `feature/eigenmode.L4`; the theme points UP at the op (so it does NOT receive liveness today); adding the op→theme `lowers-to depends-on` makes the theme a dep of the reachable op → flips reachable. Faithful, rank-clean.

## Overlap analysis

- **D1 × D2:** D1 is OBSERVATION-ONLY (writes its own `reports/<id>/CYCLE.md`; mutates NO `book/` artifact). D2 writes exactly one file, `book/src/L1/set_subvector_zero.md`. **No artifact-region overlap; no shared operator-entry mutation; no shared theme-body rewrite.** D1's audit will name `set-subvector-zero-mutation-rotation` as the worked exemplar of the groundable class — a verdict CONSISTENT with D2's action, not conflicting. **PARALLEL-SAFE.**
- **Consolidated-tally / shared-index:** none. D2 is per-page frontmatter; no cohort count, no `feature/index.md` matrix, no layer-index Working-Notes tally touched. The parallel-blind-shared-index guard does not apply.
- **New-slug forward-reference:** none. Every edge target D2 names (`L1-L0/set-subvector-zero-mutation-rotation`) and every node D1 audits is an EXISTING stable on-disk slug (verified). No cross-report forward-reference slug to coordinate.
- **Contamination-friction (`parallel-dispatch-reachability-measurement-contamination`, ledger-and-monitor):** D1 measures nothing it mutates (observation-only), so there is NO cross-dispatch reachability-measure contamination this cycle. D2 reports ONLY its own standalone +1; the authoritative cumulative is the `integrator-finalize` step-5b re-measure on the landed tree. This is the safest possible shape for the friction (one observer, one single-edge mutator).

## Sequencing schedule

**Single wave (both parallel):**
- **Wave 1:** D1 (`cross-layer-cross-cutter`, audit-only) ‖ D2 (`layer-intro-author`, one-file grounding edge).

No forward-reference ordering dependency (every edge target is on-disk). No second wave. After both reports land: N critics → N repairers → `integrator-per-report` ×2 (serial) → ONE `integrator-finalize` (rebuild book + step-5b linter re-measure + commit + push + housekeeping).

## Open questions / caveats

- **D1 is expected to land mostly findings, not edges — that is success, not a failed dispatch.** Under the redirect, "what the spine can't cleanly say is a finding about the spine." The likely outcome is a RE6+ baseline-exception recommendation (axpy-family-absorbed-into-combinator + elementwise/assemble-diagonal-absorbed-into-preconditioner + fold_solve/krylov-step-iteration-views) routed to the batch-36 meta-phase, plus possibly one or two more groundable L1>L0 themes for a c114 grounding dispatch. The cross-cutter should be dispatched with the explicit understanding that a faithful-path-or-finding partition (not a forced flip) is the deliverable.
- **Stale in-file prose on `L1/set_subvector_zero.md` is a recurring class.** The "a depends-on to the theme would be a rank-direction error" comment is a pre-c108 artifact. If D1's audit finds MORE L1 ops carrying the same stale prose while their L1>L0 themes are garbage (the `weak_form_term`/elementwise legs may), that is a small systematic re-anchor sweep worth surfacing to the batch-36 meta-phase (candidate friction `l1-op-frontmatter-asserts-stale-pre-c108-rank-direction-error-on-theme-edge`). Flagging here for the meta-phase since the friction-ledger entry does not yet exist.
- **F1 re-baseline carried forward.** This plan acts on F1 (the `untyped`-count is illusory for legacy-edged files) by NOT proposing further blind L3 mid-node typing. The batch-36 meta-phase should formally re-baseline the `graded-stack-lazy-tail-typing` LEAD's success metric from "untyped count" to "faithful grounds + representation upgrades" (OQ `lazy-tail-untyped-no-decrement-for-legacy-edged-files`, already promoted c112).
- **The 25→24 STRONGER GARBAGE SIGNAL movement (D2) is the only mechanical reachability delta this cycle;** D1's value is informational (the audit), realized next cycle / next batch. This is the correct shape given the forward frontier is exhausted — the higher-fan-out work IS the find-step, even though its measurable count-move is deferred.
