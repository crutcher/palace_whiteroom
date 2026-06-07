## 2026-06-07 cycle-122 — 7 reports applied clean — 117th consecutive cycle under split integrator — **POSITION 2/3 OF META-BATCH-39, THE SECOND PRIMARY CYCLE (cycles 121/122/123; the batch-39 meta-phase fires AFTER cycle-123's finalize, aggregating all three)** — **THE LIFT-THROUGH CAMPAIGN CONTINUES: consumer-wiring + AMR-verb harvest + GMG FIRM; `unresolved_depends_on_targets` 6→0; the REFERENCE-EDGE-LIVENESS SCHEME QUESTION surfaces as the headline batch-39-meta item.** The second cycle of the 2026-06-07 RE-SCOPE (DIRECTIVE-1/2/3); the c121 wide all-fronts fan-out's consumer-wiring + grounding follow-through. 7 dispatches, ALL applied clean. `cargo make book` EXIT 0, ZERO finalize build-repairs; graded-stack linter `rank_violations=0` (HELD) / `unresolved_depends_on_targets=6→0` / `detritus=123→136` (ENTIRELY the reference-edge-liveness accounting, NOT new defects).

# cycle-122 — 2026-06-07 — batch-39 position 2/3 (the SECOND primary cycle)

**Meta-batch-39, position 2/3.** Cycles 121/122/123 form meta-batch-39; the batch-39 meta-phase fires AFTER cycle-123's finalize, aggregating all three as a separate dispatch. The cycle counter does NOT reset at batch boundaries. This finalize ran NO meta-phase housekeeping.

Under the 2026-06-01 VOCABULARY-SHIFT REDIRECT + the 2026-06-04 GRADED RESOLUTION LADDER + FEATURE-ROOT REACHABILITY directive + the 2026-06-05 GROUND-don't-remove directive + the 2026-06-06 SEMANTIC CONSOLIDATION + OPEN-ALL-FEATURE-FRONTS directives + **the 2026-06-07 RE-SCOPE (DIRECTIVE-1/2/3)**.

## Headline

**The lift-through campaign continues — the c121 wide all-fronts fan-out's consumer-wiring + grounding follow-through.** 7 dispatches, ALL applied clean (7/7 staging rows == 7 dispatched-ready; the cycle-018 staging-completeness gap did NOT recur — 103rd consecutive clean staging). Zero deferrals, zero rejections, zero per-report gate-hits, ZERO finalize build-repairs.

Five headline outcomes:
1. **`unresolved_depends_on_targets` 6 → 0** — all 4 libceed shared-substrate ops + both AMR verbs now resolve to live files.
2. **The GEOMETRIC-MULTIGRID PRECONDITIONER column promoted rough-in → FIRM** at L4+L1 (the highest-fan-out lift-through consumer; `feature_root: seed` KEPT) via a faithful `depends-on (composes)` → `reference` edge re-type on the L3/chebyshev + L2/jacobi-smoother iteration-views.
3. **`L2/correction_step` promoted rough-in → FIRM** + replace-and-propagate into `L2/chebyshev-iteration` and `L2/jacobi-smoother` (the combinator is the entry; the smoothers are B-choice specialization notes). L2 firm 21→22.
4. **The `amr-estimate-mark-refine` THEME firm-flipped rough-in → firm** (both L1 endpoints `flux_recovery_estimate` + `dorfler_mark` harvested firm; the MFEM-opaque refine leg stays a documented obstruction sub-leaf that does NOT gate).
5. **The REFERENCE-EDGE-LIVENESS SCHEME QUESTION surfaced as the headline batch-39-meta item** (see below).

## Dispatches (apply-order)

- **D4 (harvester, `libceed-substrate-ops`)** — landed the 4 shared-substrate ops `element_restrict` / `basis_apply` / `quad_point_contract` / `geom_factor_build` (all rank-0 `roadmap_goal`; the G/Gᵀ · B/Bᵀ · D · geometry-factor stages of the matrix-free FE contraction). `unresolved_depends_on_targets` 6→2. The libceed-quadrature-kernel-impl consumer's stale "Speculative L1 operators" prose was re-anchored to live links.
- **D6 (lowering-verifier, `libceed+eigsolve-kernel-api-audit`)** — appended `verified_against:` structured-audit YAML to `L1/libceed-quadrature-kernel-impl` (8 entries) + `L3/eigsolve-impl` (7 entries); the DIRECTIVE-3 impl-realizes-API correspondence audit. Both `realizes-kernel-api` edges confirmed `reference`-class; both kernel-api statuses preserved (`obstruction` / `partial-obstruction`). Also applied the D4-confirmed stale-prose re-anchor on the libceed impl.
- **D5 (lowering-verifier, `smoother-kernel-api-audit`)** — appended an 8-entry `verified_against:` block to `L1/multigrid-relaxation-smoother` + 2 carry-forward off-by-one citation corrections (`distrelaxation.cpp:103→:102`, `:121-152→:121-151`).
- **D3 (harvester, `correction_step`)** — PROMOTED `L2/correction_step` rough-in→FIRM (the `y + B·(x − A·y)` step-kernel combinator; depends-on `L1/apply_linop` + `L1/axpby`) + REPLACE-AND-PROPAGATE into `L2/chebyshev-iteration` (`B = p_order(D⁻¹A)`) + `L2/jacobi-smoother` (`B = ω·D⁻¹`). L2 firm 21→22; 3 c121 OQs settled.
- **D7 (layer-intro-author, `gmg-promotion-eval`)** — PROMOTED the GMG preconditioner column rough-in→FIRM at L4+L1 (`feature_root: seed` KEPT) + the central faithful edge re-type: `L3/chebyshev` + `L2/jacobi-smoother` `depends-on (composes)` → `reference` (sibling iteration-VIEWS, not blocking deps; the firm grounding is via the smoother chain → `L1/chebyshev-smoother`). RE1 re-stated.
- **D1 (harvester, `flux_recovery_estimate`)** — landed `L1/flux_recovery_estimate` FIRM (the ZZ flux-recovery a-posteriori AMR estimate verb; depends-on ksp_solve/apply_linop/nrm2). `unresolved` 2→1.
- **D2 (harvester, `dorfler_mark`)** — landed `L1/dorfler_mark` FIRM (the Dörfler bulk-marking verb). `unresolved` 1→**0** + FIRED the `amr-estimate-mark-refine` theme firm-flip. Both AMR verbs registered FLAT in SUMMARY (the by-kind group-intro deferred to c123).

## Build + step-5b linters (landed tree)

- **`cargo make book`** (mdbook + linkcheck2 0.12.0) **EXIT 0**, NO finalize build-repair. The FLAT AMR-verb SUMMARY fallback (`grep -c amr-estimate-mark-intro SUMMARY.md = 0` — NO dangling group link; the group-intro is deferred to a c123 layer-intro-author pick) + the 4 libceed substrate cohort entries + the correction_step alpha-insert + the GMG firm flip all resolve clean; 0 dead links. Only the pre-existing benign `Potential incomplete link` / `j+1` KaTeX-adjacent WARNs in `concepts/plane-rotation-stream.md` + `concepts/step-outputs.md` (NOT cycle-122 files) remain.
- **Graded-stack linters — both step-5b block-conditions PASS:**
  - **`rank_violations: 0`** (baseline fully discharged c096 → ANY violation would be NEW + BLOCK; NONE — GATE PASSES). correction_step/flux_recovery_estimate/dorfler_mark firm rest on firm deps; the 4 substrate roadmap_goals rest-on-anything vacuously; the GMG firm flip is well-founded (all 5 depends-on constituents firm, the 2 demoted edges now reference-class).
  - **NO newly-orphaned node** — no previously-reachable node went dark; the firm/root nodes flagged this cycle are reachable-via-reference, NOT previously-depends-on-reachable-now-gone.
- **Totals (re-measured on the landed tree):** `files=385 (+7), typed=324 (+7), untyped=61 (HELD), roots=41 (HELD), reachable=150, rank_violations=0 (HELD), unresolved_depends_on_targets=0 (6→0), promotion_frontier=12, detritus=136 (no_typed_edges=108, stronger=28), expected_unreachable_outside_dag=47, rank_histogram={firm:224, roadmap_goal:7, typed-no-rank:82, rough-in:2, partly-constructive:3, obstruction:2, partial-obstruction:4}`.
- **Trend:** `rank_violations` HELD 0 (… → 0 c120 → 0 c121 → 0 c122); `unresolved_depends_on_targets` 6 → **0**; `detritus` 123 → 136 (+13, ENTIRELY the reference-edge-liveness accounting, NOT new defects).

## ⟢ The headline batch-39-meta item — the reference-edge-liveness scheme question

Multiple genuinely-firm c122 nodes — `correction_step`, `flux_recovery_estimate`, `dorfler_mark`, the `amr-estimate-mark-refine` theme, the 4 libceed substrate `roadmap_goal`s, and the GMG-re-typed `L3/chebyshev` + `L2/jacobi-smoother` iteration-views — are flagged `[GARBAGE*]` by the **depends-on-only** reachability GC because they reach the feature roots ONLY via `reference`-class edges:
- the **combinator-primary specialization-note edges** (an entry's specializations `reference` their combinator; the combinator is not `depends-on`'d by its specializations);
- the **`realizes-kernel-api` edges** (DIRECTIVE-3 dual-surface; deliberately free `reference`-class so the impl does not block on the opaque API);
- the **kernel-impl realizes edges**.

`detritus` climbed ≈123→136 across the cycle (127→128 [D3 correction_step] → 134 [D7 GMG re-type] → 135 [D1 flux] → 136 [D2 dorfler + AMR theme], per the staging rows' own linter runs).

**This is NOT a new rank violation (HELD 0) and NOT a per-report defect.** It is a genuine SCHEME QUESTION the batch-39 meta-phase MUST adjudicate: **do `reference`-class edges to firm / root-reachable nodes count toward liveness?** The combinator-primary model + the DIRECTIVE-3 dual-surface model SYSTEMATICALLY produce correctly-modelled-but-GC-unreachable firm nodes, so `detritus` is now climbing per-cycle as a function of correct modelling rather than actual decay. The accounting decision (e.g. a `reference`-to-reachable-node liveness rule, or a separate "reference-reachable" tier distinct from true detritus) is the batch-39-meta's headline.

## RE-discharge deltas (the central signal for the c123 RE-recheck + the batch-39 meta)

- **`unresolved_depends_on_targets` 6 → 0** — all 4 libceed substrate ops + both AMR verbs now resolve to live files.
- **RE1 RE-STATED** — GMG promoted firm; the L2/L3 chebyshev/jacobi iteration-views are now reference-class sibling-views absorbed-below-spine, like RE5/RE7 after the faithful re-type. A classification correction, NOT a regression; the firm grounding is the `L1/chebyshev-smoother` chain.
- **c122 OQ-resolutions:** 3 c121 `correction_step` OQs SETTLED (one-vs-two-operator → one conjugated combinator; divfree-projector-borderline → kept out of core roster; replace-and-propagate-scope → L2 leg done, wider set is a new c123 OQ); the `amr-estimate-mark-refine-theme-firmness-gate` DISCHARGED (both endpoints firm → theme flipped); the `FiniteElementSpaceHierarchy` 2nd-FIRM-consumer trigger now literally SATISFIED by the GMG firm flip (operationally inert — page already firm on disk).
- Remaining **RE2/RE3/RE6/RE8** gated on eigsolve-impl consumers / combinator-arity-notes / the L3 iteration-views column; the c123 planner re-runs the standing RE-recheck; the batch-39 meta ratifies.

## Counts

- +2 L1 firm (`flux_recovery_estimate`, `dorfler_mark` — the AMR estimate/mark vocabulary group, tracked separately from the 43-member main grand total per the new cohort heading).
- +1 L2 firm (`correction_step`, 21→22).
- GMG column rough-in → FIRM (Infrastructure kind, tracked separately).
- The `amr-estimate-mark-refine` L1>L0 theme rough-in → firm.
- +4 L1 roadmap_goal (libceed substrate).
- SLICE CORPUS: 0.

## Process

- retroactive-budget global = 0; per-report gates all PASS / N/A; 0 implied-component stubs; ZERO finalize build-repairs.
- OQs promoted by the per-report integrators this cycle (finalize made no duplicate append): the new ones include `amr-estimate-mark-group-intro-needs-authoring`, `correction-step-wider-replace-and-propagate-set-l1-and-feature-column`, `record-RefinementData-needs-concept-definition-home`, `dorfler-coarsening-threshold-sibling-verb`, `libceed-substrate-element-local-rank-tensor-l1-vocabulary-front`, `kernel-impl-realizes-leaf-vs-realizes-kernel-api-label-vocabulary`, and more.
- `scaffolding/{roadmap,integrator-signals,cycle-record}` + `log/` committed atomically + the 7 consumed-report `integrated_at` touches.
- Two-phase SHA-patch follows.
- NO `.claude/agents/` changes FROM THIS FINALIZE.

## The carry to c123 (batch-39 position 3/3, THE BATCH-CLOSING cycle)

1. **The REFERENCE-EDGE-LIVENESS SCHEME QUESTION** — the batch-39-meta headline adjudication (does a `reference`-class edge to a firm/root-reachable node count toward liveness? the combinator-primary + DIRECTIVE-3-dual-surface models systematically produce reference-only-reachable firm nodes).
2. **The DEFERRED `amr-estimate-mark-intro.md` by-kind group-intro authoring** + the SUMMARY re-nest of the 2 flat AMR verbs + the `index.md` "Rough-in (AMR estimate/mark vocabulary)" header rename — one coordinated c123 layer-intro-author follow-up.
3. **The wider correction_step replace-and-propagate set** (L1 multigrid-relaxation-smoother / GMG V-cycle column / distributive-relaxation — a c123 same-layer-cross-cutter).
4. The remaining RE set (RE2/RE3/RE6/RE8) gated on eigsolve-impl consumers / combinator-arity-notes / the L3 iteration-views column.
5. The V-cycle recursive-combinator + MultigridConfig record-definition mining candidates (now-firm GMG column unblocks them).
6. 2 new record-definition home OQs (`RefinementData`; `element-local-tensor` gated on the libceed substrate firm flip) + the libceed-substrate element-local rank-tensor L1 vocabulary front (a batch-39-meta scheduling pick).

Written by `integrator-finalize` (split integrator-per-report ×7 + finalize ×1).
