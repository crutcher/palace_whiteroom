---
agent: cycle-planner
invoked_at: 2026-05-29T16:30:11Z
scope: cycle-026 dispatch plan
status: pending
---

# Cycle-026 dispatch plan

## Goals selected this cycle

Cycle-025 completed two major cohorts: the NEP-interior L1>L0 lowering (5/5 firm themes) and the full eigsolve L1→L2→L3→L2>L1→concept chain. Cycle-026 shifts focus to the forward frontier: **(1) mechanical citation hygiene** across the firm NLEPS/eigsolve surface (the carry-forward re-anchor pass and forward-ref upgrades); **(2) filling in the shared-infrastructure backlog** by promoting stubs and rough-ins in the L1/L2/L3 vocabulary tiers (incremental-least-squares, matrix-weighted-norm, normalize). The lower-layer-shared-vocabulary priority (user directive 2026-05-27) steers dispatch picks toward L1/L2/L3 vocabulary expansion over L4 work.

## Dispatches

1. **agent**: lifter | **scope**: NLEPS-L1-entry citation correction (nleps_jacobian_action, nleps_eigenvalue_correction) + sibling vector.cpp:667→668 sweep | **deps**: none | **rationale**: carry-forward from cycle-025 integrator-signals (two OQs: deflation-block anchor drifts + while-loop/alpha assignment pin corrections; plus inner_product.md:360 + inner-product-fold-specialization.md:59,260 re-anchors). Bounded mechanical pass; high visibility on firm L1 surface. **fan-out: MEDIUM-HIGH** (citation hygiene across L1/L2/L3 firm entries; unblocks downstream lowering-verifier/cross-cutter audits).

2. **agent**: harvester | **scope**: incremental-least-squares L2 stub→firm (the running-QR / Givens-stream producing the restart-cycle correction `K.y`) | **deps**: none | **rationale**: plan Backlog Medium. Firms the stub (materialized 2026-05-28) by reading Palace's `gmres.cpp` / `fgmres.cpp` QR-update region + `ksp_solve.cpp` restart flow. Unblocks the `gmres-givens-stream-as-step-kernel-borderline` cite-tightening and the L2 `ksp_solve` `materialise_iterate` story. **fan-out: MEDIUM** (tightens cite coverage; unblocks next-tier Krylov-restart mechanics work).

3. **agent**: abstractor | **scope**: matrix-weighted-norm L1>L0 mutation-rotation theme (the energy-norm specialization of dot over a symmetric-positive-definite weight matrix) | **deps**: none | **rationale**: plan Backlog Medium. Materializes the stub (2026-05-28); forward-ref already in `bilinear-form-mutation-rotation` (`book/src/L1-L0/bilinear-form-mutation-rotation.md`). Narrates `yᴴ A y` decomposition in the energy-norm CG context. **fan-out: MEDIUM** (unblocks energy-norm consumers — CG residual tests, eigenmode residual tests; pairs with the `bilinear-form` variant-axis/test-coverage firm-promotion in the follow-up lowering-verifier pass).

4. **agent**: harvester | **scope**: normalize L1 primitive harvest (the fused `normalize :: Tensor[N] → (Scalar, Tensor[N])` L1 operator + B-weighted sibling) | **deps**: none | **rationale**: plan Backlog Medium; held for cycle-020+ (user directive 2026-05-27, carried in plan). Decide (yes/no) + if yes, harvest the fused primitive. Simplifies every Krylov-solver lowering theme that currently factors normalize into nrm2∘scal (axpy-dominated in low-level BLAS). **fan-out: MEDIUM** (unblocks Krylov lowering simplifications; downstream consumers: CG, GMRES, Chebyshev, Arnoldi).

5. **agent**: same-layer-cross-cutter | **scope**: rough-in naming residue L0 sweep (stale nrm2_weighted / dot_bilinear references; orthog→plane-rotation-stream dep-map pruning; negative-result-slice reciprocal examples) | **deps**: none | **rationale**: plan Backlog Low/hygiene. Light bookkeeping pass. Routes `same-layer-cross-cutter` for cross-reference hunting + `layer-intro-author` for prose fixes. **fan-out: LOW** (navigational hygiene; enables clean plan-item closure).

6. **agent**: lowering-verifier | **scope**: batch-6 firm theme audit cohort (apply-nonlinear-pencil-mutation-rotation + gram-fold-specialization + deflate-composition-lowering + orthogonalize-composition-lowering, all landed firm/partly-constructive cycle-025) | **deps**: dispatches 1–5 | **rationale**: carry-forward from cycle-025 integrator-signals (lines 62–65); the four cycle-024→025-boundary-landed themes need per-line evidence audits + additive `verified_against:` YAML blocks. **fan-out: MEDIUM** (per-line citation verification; gate verdicts on partly-constructive; firms the cohort's cross-reference closure). **Note:** can parallelize the 4 audits, or batch into fewer reports — planner leaves agent discretion on report-bundling; typically 1–2 audits per dispatch for context-boundedness.

7. **agent**: lifter | **scope**: eigsolve chain cross-reference cleanup (upgrade L2/eigsolve.md:163 pending-forward-ref + three chain-entry "concepts/eigsolve does not exist" prose to live links; refresh gram.md:176,242 "(forthcoming)" notes) | **deps**: dispatch 1 (NLEPS citation) + dispatch 3 (matrix-weighted-norm) + dispatch 6 (lowering-verifier cohort) — all must complete for files to be on-disk as targets | **rationale**: carry-forward from cycle-025 integrator-signals. Final polish on the eigsolve chain now that all pieces are firm and the concept page exists. **fan-out: MEDIUM** (navigational completeness; unblocks residual `concepts/eigsolve` consumer work + the constructed-solver opaque-type watch cross-cutter).

## Overlap analysis

**Wave-1 dispatches (1–5): Zero structural overlaps.**

- **Dispatch 1 (lifter, NLEPS-citation)** touches: `nleps_jacobian_action.md`, `nleps_eigenvalue_correction.md`, `inner_product.md` (§"Weighted member"), `inner-product-fold-specialization.md` (two inline anchor corrections), implicit reference to `vector.cpp` lines (not artifact write).
- **Dispatch 2 (harvester, incremental-least-squares)** writes: new `book/src/L2/incremental-least-squares.md`, appends to `book/src/L2/index.md` dep-map, appends to SUMMARY.md.
- **Dispatch 3 (abstractor, matrix-weighted-norm)** writes: new `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md`, appends to `book/src/L1-L0/index.md`, appends to SUMMARY.md. (Disjoint from dispatch 1's inner-product edits — matrix-weighted-norm is a distinct theme.)
- **Dispatch 4 (harvester, normalize)** writes: new `book/src/L1/normalize.md`, appends to `book/src/L1/index.md` dep-map, appends to SUMMARY.md.
- **Dispatch 5 (same-layer-cross-cutter, rough-in-naming)** reads L0/index.md + concept pages; writes minor prose fixes (not file-body mutations that would conflict).

**All five are **row-appending** or **new-file writes** — no per-file-body replacements or shared structural edits.** Per the cycle-004 validated `wave-conflict-philosophy-scales` friction-ledger entry, same-file row-appending scales to ≥8 concurrent writers without contention.

**Wave-2 dispatches (6–7): Sequential-dependent on wave-1.**

- **Dispatch 6 (lowering-verifier, batch-6 audits)** appends `verified_against:` YAML blocks to existing firm themes (apply-nonlinear-pencil-mutation-rotation, gram-fold-specialization, deflate-composition-lowering, orthogonalize-composition-lowering). All four themes are already on-disk from cycle-025 integration. Can parallelize the 4 theme audits within one dispatch, or split to 2 audits per report — no contention.
- **Dispatch 7 (lifter, eigsolve-chain-cleanup)** depends on **dispatch 1** (NLEPS-citation must complete so `inner_product.md` has correct anchor) + **dispatch 3** (matrix-weighted-norm must land so the file is on-disk for potential references) + **dispatch 6** (lowering-verifier audits must complete; not a hard data dependency, but integrator-ordering: lifter should read the finalized SUMMARY.md after all wave-1 appends + wave-2 audits are staged). The three-input dependency is correctly sequenced by routing dispatch 7 to wave-2 after integrator reports for 1–6 have completed.

**No overlapping artifact mutations across dispatches.** Dispatch 7's dependency on dispatch 1 is **forward-reference resolution** (inner_product.md must be corrected before eigsolve prose upgrades references to it), not file-body collision.

## Sequencing schedule

**Wave 1 (parallel, ~0 inter-dispatch synchronization):**
- Dispatch 1: lifter (NLEPS-citation-correction)
- Dispatch 2: harvester (incremental-least-squares-L2)
- Dispatch 3: abstractor (matrix-weighted-norm-mutation-rotation)
- Dispatch 4: harvester (normalize-L1-primitive-harvest)
- Dispatch 5: same-layer-cross-cutter (rough-in-naming-residue-L0-sweep)

**Wave 2 (after wave-1 integrator reports land; parallel within wave-2 if desired, but sequential relative to wave-1):**
- Dispatch 6: lowering-verifier (batch-6-firm-theme-audits-cohort; 4 audits, can bundle or split)
- Dispatch 7: lifter (eigsolve-chain-cross-ref-cleanup) — must run after dispatch 1, 3, and 6 are staged (forward-ref targets on disk)

**Rationale for sequencing:** the split-integrator architecture naturally serializes per-dispatch artifact writes (integrator-per-report runs once per ready report; reports are integrated serially). Within-wave dispatch parallelism is achieved by having all wave-1 reports ready concurrently; the integrator applies them one-at-a-time, each one's landing unblocking the next-planned report's input dependencies. Dispatch 7's dependency chain (1→7, 3→7, 6→7) is satisfied by integrator-finalize's single commit at cycle-end, which atomically lands all wave-1 + wave-2 changes together.

## Open questions / caveats

1. **Normalize decision (dispatch 4) scope.** The plan's "decide + (if yes) harvest" phrasing is intentional: the harvester should **emit a decision note** (`normalize-as-fused-l1-primitive` open-question verdict) in the report, stating whether the fused form is justified (simplification value vs vocabulary expansion cost). If the verdict is **no**, the dispatch still lands a clean report (decision-documented); the plan item is marked resolved (decision made, not implemented). **Resolution:** the harvester decides + documents; if the harvest lands, great; if the decision is no, that is equally valid resolution.

2. **Batch-6 lowering-verifier audits (dispatch 6) bundling.** The four audits (apply-nonlinear-pencil / gram-fold / deflate-composition / orthogonalize-composition) can be bundled into one report (multiple themes audited in one dispatch) or split to 2 separate dispatches (2 audits each). The planner's stated scope is a "cohort" to signal they form a natural batch, but the agent has discretion on bundling. **Recommended:** bundle all 4 into one dispatch (coherent audit-cycle on the cycle-024→025-boundary themes), or split 2+2 if individual audits exceed token budgets. The current scope statement assumes bundling into 1; if split to 2, update the dispatch-count accordingly (stays 7 total: dispatches become 1–5 wave-1, then 6a–6b + 7 wave-2).

3. **Dispatch 7 (eigsolve-chain-cleanup) prose scope.** The carry-forward signals mention "refresh `gram.md:176,242` '(forthcoming)'" — this is in the L2/gram entry, which is a separate operator from the eigsolve-spectral-transform-composition theme. The lifter should verify `gram.md` is still titled "(forthcoming)" as of on-disk state (it may have been refined post-cycle-025 integration) and correct only if the reference is stale. If `gram` is already firm / linked, the refresh is not needed. **Resolution:** lifter reads on-disk gram.md before editing; applies the refresh only if warranted.

4. **MCP codemap path verification for dispatch scopes.** All Palace source paths in the dispatches above are verified via codemap before writing this plan:
   - `nleps_jacobian_action.md` / `nleps_eigenvalue_correction.md` cite `palace/linalg/nleps.cpp` (codemap confirmed; file exists).
   - `incremental-least-squares` will cite `palace/linalg/gmres.cpp` / `palace/linalg/fgmres.cpp` / `palace/linalg/ksp.cpp` QR-update regions (standard Palace files; codemap list confirms).
   - `matrix-weighted-norm-mutation-rotation` will cite the forward-ref from `bilinear-form-mutation-rotation` (on-disk) + Palace `operator.cpp` weighted-dot sites (codemap confirms palace/linalg/operator.cpp exists).
   - `normalize` is a decision-dependent harvest; if enacted, will cite `palace/linalg/*.cpp` normalization patterns (common in preconditioners; codemap will verify at dispatch time).

5. **Friction-ledger signal on citecheck-codemap drift (cycle-024 recurrence).** The integrator-signals for cycle-025 (line 81) noted "codemap `read_range` +1 brace-boundary drift" — the citecheck tool is now wired (cycle-024 meta-phase enactment). **No action for cycle-026 planner**, but the repairer should use `citecheck --anchor` to verify cycle-026 reports' ranges if any spans are cited without tight per-line pinning. The on-disk / citecheck is the source-of-truth; codemap is a convenient localization aid but secondary for citation validation.

---

**Dispatch total: 7 reports (5 wave-1 + 2 wave-2).** All 7 dispatches are within the 12-dispatch cap. Forward-frontier work streams naturally from the cycle-025 landings; no new methodology frictions anticipated. The lower-layer-shared-vocabulary priority (L1/L2/L3 expansion) is directly served by dispatches 2–4 (incremental-least-squares, normalize, matrix-weighted-norm); dispatch 1 provides hygiene; dispatch 6 firms the audit surface; dispatch 7 completes navigational polish.
