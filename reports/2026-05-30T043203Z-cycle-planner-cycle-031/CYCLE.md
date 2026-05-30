---
agent: cycle-planner
invoked_at: 2026-05-30T043203Z
scope: cycle-031 dispatch plan
status: pending
---

# Cycle 031 dispatch plan

**FIRST primary cycle of meta-batch-9 (cycles 031/032/033; meta-phase fires after cycle-033 finalize).**

## Goals selected this cycle

Cycle-031 executes the batch-8-finalized follow-up plan (priorities.md Now active head, carryover from c030 integrator-signals suggested dispatches) plus one open slot for a substantive operator landing. The batch-8 meta-phase (firing between c030 finalize and c031 dispatch, after this plan) will enact: (i) channel-format codification (verified_against note no-leading-quote-of-either-kind), (ii) obstruction sub-kind codification (enum-only-stub vs opaque-library-ownership), (iii) skill promotions (establish-negative-finding-exhaustiveness) + (iv) OQ-ledger unification + (v) ask on dispatch-resilience iterative.cpp region pre-localization strategy. Cycle-031 then executes the follow-ups, which are continuity-heavy (audits + narrative repair + hygiene folds) but high-value for closing batch-8's GMRES-restart cohort audit window and cross-layer link-hygiene. The open slot (item #6) routes a new substantive landing to continue forward momentum; candidates ranked by fan-out: L2 firm operator harvest (L2 cohort stagnant since c026), L3 firm-or-obstruction backfill (L3 stagnant since c020), or L1 new BLAS-like primitive (candidates: `apply_linop` lift, `spectrum_estimate`).

## Dispatches

1. **lowering-verifier** — `book/src/L1-L0/ls-update-column-mutation-rotation.md` cycle-031 `verified_against:` audit
   - **Rationale:** Standard firm-L1>L0-theme follow-up. The theme landed c030 D1 (firm, no issues); the additive `verified_against:` audit block confirms surface-form exhaustiveness and per-line evidence mapping. Precedent: `back-solve-mutation-rotation` c030 / `normalize-mutation-rotation` c028 / `back_solve` c028 — each firm L1>L0 theme gets its next-cycle audit a cycle after landing.
   - **Fan-out:** LOW-MEDIUM (per-line evidence census; one theme per dispatch; closes audit-row of the c030-landed theme).
   - **Deps:** none.

2. **lifter** — `book/src/L1-L0/back-solve-mutation-rotation.md` Sub-pattern B brace-placement narrative repair
   - **Rationale:** Real content defect (narrative-only, theme stays firm). The c029-landed theme's Sub-pattern B prose claims "+1-line brace-placement shift" between GMRES `palace/linalg/iterative.cpp:653-660` and FGMRES `:832-839`. However, direct `diff` on the two arms returns ZERO BYTES — they are byte-identical, not "+1-line-shifted". This was **independently confirmed 3× across c030**: (i) D4 abstractor's own `ls-update-column-mutation-rotation` direct read; (ii) D1 lowering-verifier's audit Finding A. The correct narrative: both arms use identical `iterative.cpp` code pattern with +5-line preceding-code offset (source-location, not brace placement).
   - **Fan-out:** LOW-MEDIUM (corrects a firm c029-landed misclaim with three independent confirmations; affects readers & downstream lifters consuming the theme as authoritative).
   - **Deps:** none.

3. **lifter** — `book/src/L2-L1/incremental-least-squares-composition-lowering.md` bounded prose-rework pass (4-item fold)
   - **Rationale:** Hygiene-heavy continuation after c030's theme-landing work. Four distinct bounded prose items on the same chapter file, natural to batch into one small lifter pass: (a) three remaining `ls_update_column-mutation-rotation` plain-text mentions at `:85`/`:466`/`:480` with adjacent stale "forthcoming" framing (now obsolete — the theme landed c030); (b) §Status historical paragraph at `:429-438` (c027-authored, superseded by c028 firm + c029 leaf + c030 live-link upgrades); (c) §Open-questions historical-judgment entries at `:448-456`/`:458-467`/`:495-499` (similarly obsolete). All four are non-mechanical prose edits; the `:85`/`:466`/`:480` mentions require careful reframing that relinks the now-on-disk theme — moving from conditional "forthcoming" to assertive "the" + updating any intro sentences that assumed the theme was off-disk.
   - **Fan-out:** LOW / hygiene. Companion to the c030 integrator's partial-upgrade (3 of 6 mechanical refs upgraded; these 3 need prose touch).
   - **Deps:** none (precedent work c030 D1 on the target theme landing).

4. **repairer** — `book/src/L1/back_solve.md` three minor off-by-one cross-anchor imprecisions
   - **Rationale:** Cosmetic cleanup from c030 D1 audit's Finding B. Three citations have small off-by-one errors: `:78` should cite `:77-78`; `:218-221` should cite `:217-221`; `:466-540` is correct-as-is. The auditor deferred these as non-blocking and appropriate for repairer (mechanical, safe).
   - **Fan-out:** LOW / hygiene. Can batch with item #3 in the same wave if convenient.
   - **Deps:** none.

5. **same-layer-cross-cutter** — `book/src/spec/slices/sparse_triangular_solve.md` Phase-1 slice-reduction candidacy
   - **Rationale:** Carry-forward from c029. The Phase-1 corpus is migrating to firm layered representation. The `trsv` leaf was resolved-by-obstruction (Palace has no standalone trsv primitive); the c029 `book/src/L1-L0/triangular-solve-obstruction.md` theme (the FIRST opaque-library-ownership obstruction, distinct from the c004 enum-only stubs) is now on disk, giving the resolved leaf its citable home. The slice may now be reduced to a stub (claim-free placeholder + provenance + SUMMARY-registration) pointing at the firm layered evidence (the L3 leaf `:7` + the L1>L0 obstruction theme). Low-fan-out cohort completion (Phase-1 removals 9/10 → 10/10 if successful).
   - **Fan-out:** LOW / cohort completion.
   - **Deps:** none (the obstruction theme landed c029).

6. **[OPEN SLOT — cycle-planner chosen]** — Pick ONE of: (a) L2 firm operator harvest (medium-high fan-out); (b) L3 firm-or-partial-obstruction operator backfill (medium fan-out); (c) L1 new BLAS-like primitive (lower fan-out but fills vocabulary gap).
   - **Candidate (a) — L2 firm operator harvest:** The L2 cohort (9 firm + 1 partly-constructive) has been static since c026. The roadmap (§Intermediate-tier) and the priorities backlog suggest `normalize-l1-primitive-harvest` or `incremental-least-squares-composition-lifting` (the latter is the theme-lift of the firm c028 L2>L1 theme to a canonical L2-level form; the former would firm a fused dual of the existing L1 normalize via BLAS test coverage). Alternatively, a new harvest target from the L2 stub cohort (inner_product, orthogonalize, ksp_solve, incremental-least-squares were stubbed c028) could be refined in place.
   - **Candidate (b) — L3 firm-or-partial-obstruction backfill:** The L3 cohort (9 firm + 2 partial-obstruction) has been static since c020 (the chebyshev partial-obstruction landed c013). The roadmap (§Shared infrastructure) and OQ ledger suggest revisiting the predicted `trsv` (now resolved-by-obstruction c029) and checking for other L3 operators whose obstruction / partial-obstruction status is ripe for codification. The `apply_linop` L3 lift (from its firm L1+L2 base) is a straightforward candidate if the vote is to grow L3 vocabulary.
   - **Candidate (c) — L1 new BLAS-like primitive:** The L1 rough-in stubs (matrix-weighted-norm, bilinear-form) are not eligible for new harvest (they already exist and are deferred behind test-coverage gates). The open bids in the backlog are `apply_linop` lift / `spectrum_estimate` rough-in / `normalize` fused dual. Of these, `normalize` (a fused `(Scalar, Tensor)` return pairing nrm2 + scal) has the lowest barrier — it would simplify every Krylov lowering that currently factors the pair. Medium fan-out.
   - **Decision:** Given the batch-8 momentum (GMRES restart-cohort complete, 3-audit window closed), **recommend candidate (a) — an L2 firm operator harvest**. The lowest-friction target is refinement of one of the c028-stubbed pieces (`orthogonalize` or `incremental-least-squares` or `inner_product` — pick the one with clearest firm-promotion gate closure). Rationale: L2 has been the slowest-growing layer and is a critical bottleneck for higher-layer composition work. **Secondary fallback (if the chosen L2 target hits gating issues): candidate (c) — `normalize` fused dual** (side-by-side with item #1 lowering-verifier work, a natural sibling primitive).

## Overlap analysis

**Dispatch pairs and overlap check:**

| D1 (lowering-verifier, ls-update-column-mutation-rotation audit) | D2 (lifter, back-solve-mutation-rotation narrative) | **INDEPENDENT** — different L1>L0 themes, no shared artifact regions. |
| D1 | D3 (lifter, incremental-least-squares-composition-lowering prose) | **INDEPENDENT** — D1 is an L1>L0 leaf audit; D3 is an L2>L1 theme prose refresh. Different files. |
| D1 | D4 (repairer, back_solve L1 leaf citations) | **INDEPENDENT** — D1 audits back-solve-MR; D4 repairs back_solve citations in the L1 entry. Shared operator name (`back_solve`) but distinct files (L1>L0 theme vs L1 entry); the repairer edits the L1 entry's citation anchors in-place, no conflict with the audit's per-line verification. |
| D1 | D5 (same-layer-cross-cutter, sparse_triangular_solve slice) | **INDEPENDENT** — different file, different scope (a Phase-1 slice vs L1>L0 audit). |
| D1 | D6 (open slot) | **POTENTIAL VERY-MINOR OVERLAP if D6 is an L1>L0 theme** (shares `book/src/L1-L0/index.md` + `book/src/SUMMARY.md` ledger files with D1's theme audit landing). Mitigated by per-report integrators re-reading disk before each edit. **If D6 is an L2 or L3 operator, no overlap.** |
| D2 | D3 | **INDEPENDENT** — D2 edits one L1>L0 theme chapter (back-solve-mutation-rotation); D3 edits one L2>L1 theme chapter. No shared regions. |
| D2 | D4 | **INDEPENDENT** — D2 edits the back-solve-mutation-rotation theme (L1>L0 chapter); D4 edits the back_solve L1 entry. Shared semantic (both about back_solve) but distinct files, distinct artifact regions. |
| D2 | D5 | **INDEPENDENT** — different files, different scope. |
| D2 | D6 | **INDEPENDENT** unless D6 touches the same L1>L0 theme region; unlikely (D6 is forward-looking substantive landing). |
| D3 | D4 | **INDEPENDENT** — D3 edits L2>L1 composition theme; D4 edits L1 entry. Different files. |
| D3 | D5 | **INDEPENDENT** — D3 edits L2>L1 theme; D5 edits Phase-1 slice. No overlap. |
| D3 | D6 | **INDEPENDENT** unless D6 happens to be an L2-L1 theme; unlikely. |
| D4 | D5 | **INDEPENDENT** — D4 edits L1 entry citations; D5 edits Phase-1 slice. Different files. |
| D4 | D6 | **INDEPENDENT** — D4 is maintenance on an existing L1 entry; D6 is new landing. |
| D5 | D6 | **INDEPENDENT** — D5 is Phase-1 slice reduction; D6 is new operator landing. Different artifact regions. |

**Summary:** Dispatches D1–D5 form a **clean dependency-free set** suitable for parallel execution. Dispatch D6 (open slot, not yet assigned) depends on its scope once determined, but is expected to be **PARALLEL** with D1–D5 assuming it targets a new chapter (not an existing one being modified by D1–D5). Minor per-report integrator collision tolerance on the shared `book/src/SUMMARY.md` ledger (per the role-spec "re-read disk before each Edit" discipline).

**Recommendation: Wave-1 (all 6 dispatches in parallel) if D6 is an L2/L3/L4 operator landing; Wave-1 (D1–D5 in parallel) + Wave-2 (D6 after Wave-1 reports integrate) if D6 is an L1>L0 theme and requires live-link care.**

## Sequencing schedule

**Wave-1 (parallel, non-blocking on each other):**
- D1: lowering-verifier (ls-update-column-mutation-rotation audit)
- D2: lifter (back-solve-mutation-rotation narrative repair)
- D3: lifter (incremental-least-squares-composition-lowering prose rework)
- D4: repairer (back_solve L1 leaf citations)
- D5: same-layer-cross-cutter (sparse_triangular_solve slice reduction)

**Wave-2 (if needed; post-Wave-1 integration):**
- D6: [open slot — TBD agent/scope]

**Rationale:** Dispatches D1–D5 are independent continuity items stemming from c030's landing work. All five can execute in parallel; there are no data dependencies between them. Dispatch D6 (the new substantive landing) depends on its final assignment. **If D6 is an operator that needs SUMMARY registration and will reference c030's already-landed L1>L0 theme**, Wave-2 sequencing allows the theme to integrate first, then D6's integrator can wire a live link (per the in-cycle live-link upgrade pattern from c022/c024/c029). **If D6 is independent (e.g., a brand-new L2 operator on orthogonalize), Wave-1 is fine.** The recommendation: assume **Wave-1 for all 6 if clarity exists on D6 by dispatch time; otherwise D1–D5 in Wave-1 and hold D6 for Wave-2 decision after the meta-phase commit**.

## Open questions / caveats

1. **D6 assignment pending batch-8 meta-phase completion.** The meta-phase (firing between c030 finalize and c031 dispatch, after this plan is authored) will enact several codifications (obstruction sub-kind, channel-format, skill promotions, OQ unification) that may re-rank the L2/L3/L1-new-operator candidates. This plan lists three candidates; the human or the next cycle-planner session (post-restart) should confirm the pick. Current ranking by fan-out: **L2 harvest (highest) > L3 backfill > L1 new primitive**, with L2 `orthogonalize` stub refinement as the lowest-friction L2 target.

2. **Cycle-031 is the FIRST of meta-batch-9.** The batch-8 meta-phase fires **after c030 finalize, before c031 dispatch**. The new role-spec versions (lowering-verifier.md, critic.md, abstractor.md) + the new CLAUDE.md invariant (obstruction sub-kind codification) + the 2 promoted skills will be loaded in the session restart that follows the meta-phase commit. This plan is authored pre-meta-phase, so it cites the current (batch-8) role-specs. Dispatch agents will see post-meta-phase specs once dispatched post-restart.

3. **The known-heavy `palace/linalg/iterative.cpp` running-QR region surfaces in c030 integrator-signals as a dispatch-resilience ASK.** The c030 notes record 3 retries across batch-8 (c029 D5+D6 + c030 D4), all on the same source region (GMRES/FGMRES Givens-stream / restart machinery). The c030 D4 abstractor's `ls-update-column-mutation-rotation` dispatch was successfully scoped with pre-localized anchor ranges (`:634-640` GMRES, `:813-819` FGMRES per the user directive 2026-05-30, enacted in commit f582a66). **This plan does not propose any new dispatch on that region for c031** (D1 is an audit on the c030-landed theme, not re-authoring the region). If a future cycle targets a different section of iterative.cpp (e.g., a FGMRES restart-cycle orthogonalization / preconditioner-apply variant audit), the cycle-planner should pre-fetch the codemap anchors and embed them in the dispatch scope per the user directive.

4. **Item #2 (back-solve-mutation-rotation narrative repair) is "narrative-only" but NOT repairer-only.** The integration-signals notes it was independently confirmed 3 times. A **lifter** is proposed (not repairer) because the prose rewrite requires reframing the offset story (from "brace-placement +1-line" to "source-location +5-line preceding-code offset"), which is substantive prose work — beyond the repairer's mechanical-fix scope. However, a **repairer could also take this dispatch** if the human prefers a repair-phase assignment (repairer can do surgical prose rewrites on findings). The proposed agent is a suggestion; the orchestrator may reassign.

5. **The open-slot D6 is a forward-momentum decision point.** If the human has a preference (L2 vs L3 vs L1), or if the meta-phase produces a clear steering signal, D6 should be assigned explicitly in the dispatch phase. If no strong signal exists, the **L2 operator harvest** (either `orthogonalize` or `incremental-least-squares` stub → firm) is the planner's default pick for batch-9 momentum.

