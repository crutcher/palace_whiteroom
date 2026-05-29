---
agent: cycle-planner
invoked_at: 2026-05-29T151441Z
scope: cycle-025 dispatch plan (first primary cycle of meta-batch-7)
status: pending
---

# Cycle-025 dispatch plan

## Goals selected this cycle

**Discharge the two remaining NEP-interior L1>L0 lowering themes** (`nleps_jacobian_action`, `nleps_eigenvalue_correction`; the L1 atoms landed firm cycle-024, closing the 5-atom NEP-interior cohort). **Complete the eigsolve L2>L1 lowering chain** (the spectral-transform-composition theme + the absent `concepts/eigsolve` page now fully anchored with L1/L2/L3 all firm). **Audit the batch-6 firm themes** (the four new L2>L1 / L1>L0 themes landed cycle-023/024 now face standard lowering-verifier audits). **Refresh L1/L2/L3 index narrative** post-batch-6 completions. This cycle unblocks the shared-vocabulary forward-frontier: with eigenmode (eigsolve + NEP) substantially covered at L1–L3, the planner can shift weight to a different solver pipeline or the remaining shared-infrastructure backlog.

**Cycle-025 is FIRST primary cycle of meta-batch-7** (cycles 025/026/027; meta-phase fires after cycle-027). **Zero deferrals / rejections through batch-6 — split integrator resilience validated twice (cycles 023/024 both crash-recovered cleanly).** Batch-6 closed 6 High-fan-out items to the plan's Closed index; the two NEP-interior L1>L0 themes + eigsolve L2>L1 + concept page move from active-head to dispatch.

## Dispatches

| Ordinal | Agent | Scope | Deps | Rationale |
|---------|-------|-------|------|-----------|
| 1 | abstractor | `nleps_jacobian_action` L1>L0 mutation-rotation lowering theme | none | High fan-out: closes the NEP-interior L1>L0 cohort (deflation+bare-pencil landed c023/c024; the per-step Jacobian derivative lands here). Anchor: `nleps.cpp:649-669` the divided-difference chain realizing the `T'` pencil. OQ `nleps-jacobian-action-mutation-rotation-l1-l0-lowering-theme`. |
| 2 | abstractor | `nleps_eigenvalue_correction` L1>L0 mutation-rotation lowering theme | none | High fan-out: sibling to dispatch 1; the per-step `δλ` Rayleigh-functional correction over firm BLAS-1 leaves. Anchor: `nleps.cpp:672-677`. OQ `nleps-eigenvalue-correction-mutation-rotation-l1-l0-lowering-theme`. |
| 3 | abstractor | L2>L1 `eigsolve-spectral-transform-composition` lowering theme | none | Medium fan-out: narrates the firm L2 `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K−σM)⁻¹)` composition forward into L1 leaves. L1/L2/L3 eigsolve chain now fully anchored on both ends (L2 firm c023, L3 partial-obstruction c024). OQ `eigsolve-l2-l1-spectral-transform-composition-lowering-theme-needed`. |
| 4 | layer-intro-author | `concepts/eigsolve` page | none | Medium fan-out: still absent despite the full L1→L3 eigsolve chain firm (c022→c024). A second-consumer concept candidate (`EigSolver[problem]` opaque type, sibling to `Solver[A]`/`NonlinearPencil[N]`). Routes the integrator's navigational-cohort-home signal. OQ `concepts-eigsolve-page-still-absent`. |
| 5 | lowering-verifier | `apply-nonlinear-pencil-mutation-rotation` (L1>L0) audit | none | Low-medium fan-out: standard post-landing audit; the firm L1 atom `apply_nonlinear_pencil` (c024) now gets its lowering theme (c024-firm) verified per-line. OQ `apply-nonlinear-pencil-mutation-rotation-lowering-verifier-audit-followup`. |
| 6 | lowering-verifier | `deflate-composition-lowering` (L2>L1) audit | none | Low-medium fan-out: the partly-constructive theme (c024) may UNBLOCK the shared bare-Galerkin-core promotion gate without ENACTING (the gate is triple-referenced: L2 `deflate` + L1>L0 `nleps-deflated-solve` + this L2>L1 `deflate-composition-lowering`; all promote together on a positive bare-Gram-solve site outside the Schur wrapping). Standard audit or an explicit "NLEPS-scoped is acceptable" verdict either way. OQ `deflate-composition-lowering-mutation-rotation-lowering-verifier-audit-followup`. |
| 7 | lowering-verifier | `gram-fold-specialization` (L2>L1) audit | none | Low-medium fan-out: standard post-landing audit; the firm L2 `gram` atom + its L2>L1 lowering theme (c024-firm) anchored on the double-`dot` loop fusion at `nleps.cpp:524-531`. OQ `gram-fold-specialization-l2-gram-forward-reference-closure-followup`. |
| 8 | lowering-verifier | `orthogonalize-composition-lowering` three-way-delegation-boundary audit | none | Low-medium fan-out: carried from cycle-022 active-head (not picked c023/c024); the standard `verified_against:` audit + non-duplication confirmation across stage-selection ⟂ Sub-pattern D inner-product unfusing ⟂ orthogonalize-mutation-rotation in-place `w.Add`. OQ `orthogonalize-composition-lowering-three-way-delegation-boundary-audit`. |
| 9 | layer-intro-author | L1/L2/L3 index cohort-prose refresh | none | Low fan-out: deferred navigational/bookkeeping work from cycle-022; L1 §Semantics fifth/sixth motif framing + the eigsolve-firm (c022) narrative bullet; L2/L3 dep-map prose for the eigsolve + deflate rows post-batch-6. OQs `lu-solve-layer-intro-count-refresh-and-fifth-motif`, `eigsolve-firm-stale-cycle-009-narrative-bullet-routes-to-layer-intro-author`. |

## Overlap analysis

**Dispatch overlaps (file regions / shared operators):**

- **Dispatches 1 + 2** (both abstractor, `nleps_jacobian_action` + `nleps_eigenvalue_correction` L1>L0 themes): **OVERLAPPING on `book/src/L1-L0/index.md` + `SUMMARY.md`** (both will append rows + entries to the same two files). Distinct L1>L0 theme slugs; append-only pattern. Must be **SEQUENTIAL** (dispatch 2 re-reads disk after dispatch 1 applies, matches anchors, inserts at distinct upstream/downstream positions). Standard serial handoff precedent (cycles 023/024 wave pattern).

- **Dispatches 1–4** (abstractor ×3 + layer-intro-author ×1): No overlap to dispatches 5–9 (the lowering-verifier audits and the L1/L2/L3 index refresh are on distinct files). These can run **PARALLEL** to the verifiers.

- **Dispatches 5–8** (lowering-verifier ×4): Each audits a **distinct theme** and appends to distinct `<theme>-[L1-L0|L2-L1]/<slug>.md` files (or to `book/src/SUMMARY.md` shared citation sections, which are append-only). The four reports are **non-overlapping by construction** (they operate on four different theme files) **→ PARALLEL**. If report B's `verified_against:` anchor happens to reference a detail in report A's theme, report B will re-read disk and match; no clobbering.

- **Dispatch 9** (layer-intro-author, L1/L2/L3 index refresh): Appends to `book/src/L1/index.md`, `book/src/L2/index.md`, `book/src/L3/index.md` (three separate files). Does NOT overlap with dispatches 1–8 (which write to theme files). **Can run PARALLEL to dispatches 1–8, or SEQUENTIAL after dispatch 4** (if dispatch 4's `concepts/eigsolve` page landing is relevant to the index prose context; conservative: sequence after dispatch 4).

**Wave sequencing recommendation:**
- **Wave 1 (parallel)**: Dispatches 1, 3, 4, 5, 6, 7, 8 (6 independent work items: 3 abstractors, 1 concept page, 4 lowering-verifier audits). These have zero mutual conflicts and can scatter/apply in any order.
- **Wave 2 (after wave-1 reports land)**: Dispatch 2 (the second NEP-interior L1>L0 theme, depends on dispatch 1's disk-landing), then dispatch 9 (the index refresh, which benefits from seeing dispatches 1–4 on disk but is not strictly blocked by them).

Rationale: Wave-1 scatters 7 non-overlapping reports. Dispatch 2 serializes after dispatch 1 per the two-abstractor-on-the-same-index pattern (cycle-023 L1>L0 wave-1 success; cycle-024 L2>L1 wave-1 success). Dispatch 9 finishes post-wave-1 as a cleanup pass refreshing the three layer intros with the batch-6-landed cohort context. **Total: 2 waves, 9 dispatches (3 within the 12-dispatch cap).**

## Sequencing schedule

```
Wave 1 (parallel, 7 reports):
  - dispatch 1: abstractor — nleps_jacobian_action L1>L0
  - dispatch 3: abstractor — eigsolve-spectral-transform-composition L2>L1
  - dispatch 4: layer-intro-author — concepts/eigsolve
  - dispatch 5: lowering-verifier — apply-nonlinear-pencil-mutation-rotation audit
  - dispatch 6: lowering-verifier — deflate-composition-lowering audit
  - dispatch 7: lowering-verifier — gram-fold-specialization audit
  - dispatch 8: lowering-verifier — orthogonalize-composition-lowering audit

(all wave-1 reports integrate)

Wave 2 (serial, 2 reports):
  - dispatch 2: abstractor — nleps_eigenvalue_correction L1>L0 (reads disk, matches anchors post-dispatch-1)
  - dispatch 9: layer-intro-author — L1/L2/L3 index cohort-prose refresh (reads disk post-dispatches-1-4)
```

## Open questions / caveats

**None at the dispatch-level.** All seven active-head priorities are unblocked and ready to dispatch. The plan's Backlog tiers (Medium / Low fan-out) remain available for cycle-026/027 scheduling:

- **forward-frontier candidate (active-head #6)**: The planner has not allocated a dispatch this cycle for the "shift to a different solver pipeline's shared infrastructure or shared-vocabulary backlog" forward-frontier item. This is intentional: the three Meta-batch-7 primary cycles (025/026/027) should discharge the high-fan-out eigsolve/NLEPS cohort closure work without over-committing. Cycle-026/027 can pick from the Backlog (Medium tier: `incremental-least-squares` stub→firm, `matrix-weighted-norm`/`bilinear-form` promotion, `normalize` decision; Low tier: BLAS-1 `verified_against:` audits, Phase-1 corpus reductions, etc.). The forward-frontier SURVEY (which solver pipeline / shared-vocab backlog item to prioritize next) is a meta-phase responsibility after batch-7 closes, not a cycle-025 dispatch.

- **trsv L1-localization triage (active-head #7, optional)**: Marked optional in priorities.md. Not dispatched this cycle (no fan-out urgency vs the other items). If a lowering-verifier or same-layer-cross-cutter in a future cycle surfaces the need, promote to active backlog then.

- **Citecheck invocation/uptake (friction-ledger flag from cycle-024 meta)**: Batch-6 meta-phase noted that inline-anchor drifts continued (5 drifts in l3-eigsolve report + 1 each in 3 others), and flagged the cycle-024 repairer's mention that the mechanical `tools/citecheck` codemap-backed checker was enacted (`88b7893`). The meta-phase asked: "is `citecheck` being invoked by producers/critics, and should it be a per-report gate?" This cycle-025 plan does not allocate a dispatch to check the tool's status; it is a meta-phase follow-up (tooling invocation / process gate, not content work). The producers' self-verify bullets (harvester/abstractor/lifter/layer-intro-author) include `verify-citation-range` skill mention; the skill carries a subsection noting the mechanical checker. Empirically: if drifts continue at cycle-025 reports' repair time, the meta-phase will have evidence to propose a HARD pinpoint-anchor integrator gate (a channel-format change requiring CYCLE.md anchor tokens). This is a watch-list item, not a dispatch blocker.

---

**Plan modifications this cycle:** The cycle-025 active-head priorities.md entry is now fully dispatched. All 6–9 picks are engaged. No new plan candidates from integrator-signals or friction-ledger surfaced fresh work above the Backlog tiers (the Backlog's Medium/Low items remain available for cycle-026/027 dispatch if capacity allows; the forward-frontier survey is deferred to meta-batch-7 closure).

