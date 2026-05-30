---
agent: cycle-planner
invoked_at: 2026-05-30T052756Z
scope: cycle-032 dispatch plan
status: pending
---

# Cycle-032 dispatch plan

**SECOND primary cycle of meta-batch-9 (cycles 031/032/033). Meta-phase fires after cycle-033 finalize.**

## Goals selected this cycle

This cycle consolidates the GMRES restart-cycle L1>L0 cohort housekeeping from cycle-031 (the first batch-9 cycle, post-batch-8-meta). The cycle-031 integrator routed three concrete candidates: (1) small lifter on the L2>L1 theme's residual "forthcoming" mentions (now stale since the L1>L0 theme landed c030); (2) next-cycle `verified_against` audit on the back-solve L1>L0 theme post-narrative-repair; (3) TBD substantive landing to fill the D6 slot (the CRITICAL lesson from c031 is pre-dispatch existence-checking to avoid re-recruiting stale plan targets). This cycle applies the first two routed candidates and fills the D6 slot with a genuinely-open high-fan-out work item from the plan's backlog.

## Dispatches

1. **Agent: `lifter`** · **Scope:** `book/src/L2-L1/incremental-least-squares-composition-lowering.md` residual "forthcoming" prose rework
   - **Deps:** none
   - **Rationale:** cycle-030 D5 lifter omitted 4 residual "forthcoming" mentions at `:114/:276/:300/:306` from the plain-text→live-link upgrade pass (the 3 upgraded mentions at `:69/:87-88/:307` landed clean; the residual 4 all carry adjacent stale "forthcoming" word that requires non-mechanical prose rewrite per integrator NOTE). The 4 OTHER mentions at `:15/:145/:204/:541` are correctly-quoted historical references and must NOT be touched. Bounded, single-file touch; low fan-out/hygiene closure. Citations: integrator-signals section "Unblocked" + routed-next-dispatches list item #1.

2. **Agent: `lowering-verifier`** · **Scope:** `book/src/L1-L0/back-solve-mutation-rotation.md` cycle-032 `verified_against:` additive audit
   - **Deps:** 1 (must apply after D1 so the theme's current on-disk state is stable)
   - **Rationale:** standard next-cycle firm-theme audit follow-up (precedent: `ls-update-column-mutation-rotation` c031, `normalize-mutation-rotation` c028, `back_solve` c028). The c031 D2 lifter's narrative repair re-anchored 5 sites + flipped 1 `verified_against` row to `supports`; the existing c029 + c030 audit blocks (43 rows total) remain valid for the OTHER 21 rows; the fresh audit confirms F1 row is correctly re-claimed post-narrative-repair, upholding the firm status. Standard audit cadence; HIGH continuity. Citations: integrator-signals routed-next-dispatches list item #2 + precedent citations.

3. **Agent: `same-layer-cross-cutter`** · **Scope:** Phase-1 slice-reduction audit on `book/src/spec/slices/sparse_triangular_solve.md`
   - **Deps:** none (parallel with 1 and 2)
   - **Rationale:** carried-forward from cycle-029 and cycle-030 (the c029 L1>L0 obstruction theme `triangular-solve-obstruction` is now on disk). The slice has been retained-by-design by c031 finalize as the canonical-instance witness for 3 downstream concept pages (the `polynomial_recurrence_step` precedent + reciprocal cross-link system landing). This is a verdict-confirmation audit: verify the slice may stay (concept-page citations do NOT permit reduction) and surface any novel cross-link candidates. LOW fan-out / cohort completion (Phase-1 removals stay 9/10 IF reduction blocked; candidate for eventual closure IF structure changes). Citations: integrator-signals cycle-031 "Resolution implications" item 5 + integrator-signals cycle-031 "Integration-tooling friction" `negative-result-slice-canonical-instance-blocks-reduction`.

4. **Agent: `harvester`** · **Scope:** L1 `matrix-weighted-norm` firm operator promotion from rough-in
   - **Deps:** none (parallel)
   - **Rationale:** HIGH fan-out (energy-norm consumers: CG/eigenmode residual tests). The L1 rough-in entry is test-coverage-bounded per the `book/src/L1/matrix-weighted-norm.md` §Status line. This dispatch author confirms current test coverage is adequate (or explicitly notes what additional test assertions would firm the entry), re-evaluates algebraic-law confidence against the element-type variant axis, and if coverage is confirmed, re-ranks the entry `rough-in (test-coverage-bounded)` → `firm` and appends a status audit note (precedent: `eigsolve` cycle-022 test-coverage-confidence lift). The c028 / c029 / c030 cohort work sharpened the rough-in promotion gates (element-type variant axis noted in c028; the test-coverage bar explicitly tracked in the status line). Candidate from priorities.md Medium backlog (plan line, migrated from OQ `matrix-weighted-norm-mixed-element-type-variant`). Citation: priorities.md Medium fan-out section "matrix-weighted-norm + bilinear-form firm-promotion".

5. **Agent: `abstractor`** · **Scope:** `book/src/L1-L0/matrix-weighted-norm-mutation-rotation` L1>L0 lowering theme (rough-in launch)
   - **Deps:** 4 (proof-of-concept: if D4 confirms the L1 entry is ready, this dispatch authors the mutation-rotation theme; if D4 surfaces blockers, the dispatch may re-scope or defer)
   - **Rationale:** HIGH fan-out (unblocks the broader matrix-weighted-norm ecosystem for the spectral-norm / bilinear-form / energy-norm stack). The L1 leaf exists as rough-in since cycle-018; the c028/c029/c030 batch closed several variant-axis and test-coverage gates on the corresponding `bilinear-form` rough-in. Once D4 confirms the L1 entry's promotion readiness, this dispatch provides the L1>L0 lowering theme (the multiplication-rotation and element-type variant rewrite chain). If D4 defers the L1 promotion, this dispatch is conditional-deferred (noted in the plan for c033 if needed). Citation: priorities.md "matrix-weighted-norm + bilinear-form firm-promotion".

6. **Agent: `lowering-verifier`** · **Scope:** batch-6-firm-theme audit cohort: `apply-nonlinear-pencil-mutation-rotation` + `deflate-composition-lowering` + `gram-fold-specialization` + `orthogonalize-composition-lowering`
   - **Deps:** none (parallel)
   - **Rationale:** MEDIUM-HIGH fan-out (4 firm themes from cycle-021/cycle-022, all now need sibling-pair `verified_against:` audits to confirm their firm status is upheld and identify any missing coverage). Each theme already has 1–2 `verified_against` blocks from cycle-022/cycle-023 landings, but the standard audit cadence (each firm theme gets an additive block per the lowering-verifier discipline) calls for a second round. The `deflate-composition-lowering` theme's audit may also UNBLOCK the shared Galerkin-core promotion gate (per the partly-constructive promotion condition in the plan). Precedent: the GMRES restart-cycle cohort (cycles 028–031) received multiple sibling audits across batch-8. Citation: priorities.md Medium backlog "batch-6-firm-theme lowering-verifier audits"; open-questions ledger migrations across c028–c030.

## Overlap analysis

**D1 (lifter) and D2 (lowering-verifier)** — TOUCHING same file `book/src/L2-L1/incremental-least-squares-composition-lowering.md`:
- D1 modifies prose at `:114/:276/:300/:306` (4 residual "forthcoming" mentions)
- D2 does NOT touch this file (D2 is on `book/src/L1-L0/back-solve-mutation-rotation.md`)
- Result: NO CONFLICT (distinct files; D2 is on back-solve theme, not incremental-least-squares theme)

**D3 (same-layer-cross-cutter)** and others — DISTINCT file `book/src/spec/slices/sparse_triangular_solve.md`; no conflict.

**D4 (harvester on matrix-weighted-norm L1)** and D5 (abstractor on matrix-weighted-norm-mutation-rotation L1>L0) — RELATED but SEQUENTIAL:
- D4 is the proof-of-concept: confirms the L1 entry is promotion-ready (test-coverage + variant-axis audit)
- D5 conditionally launches the L1>L0 theme (ONLY if D4 confirms readiness)
- Result: SEQUENTIAL; D5 must see D4's disposition before authoring

**D6 (lowering-verifier on 4-theme cohort)** and others — Touches 4 distinct chapter files in `book/src/L1-L0/` and `book/src/L2-L1/`; appends to existing `verified_against:` blocks or creates new blocks if absent. No overlap with D1 (which is on a prose "forthcoming" rewrite, not a lowering-verifier audit).

**Summary:** D1 and D3 fully parallel with each other; D4→D5 is a **forward-reference dependency** (D5 needs D4 to land first to confirm the L1 entry is promotion-ready); D2 and D6 are fully parallel with all others (each is a distinct theme / leaf).

## Sequencing schedule

**Wave 1 (parallel, no forward-reference constraints):**
- D1 (lifter, incremental-least-squares prose rework)
- D3 (same-layer-cross-cutter, sparse_triangular_solve slice audit)
- D6 (lowering-verifier, 4-theme cohort audit)

**Wave 2 (after Wave 1; includes forward-reference dependency):**
- D2 (lowering-verifier, back-solve audit; depends on D1 so the target file is stable)
- D4 (harvester, matrix-weighted-norm L1 promotion confirmation)

**Wave 3 (after Wave 2):**
- D5 (abstractor, matrix-weighted-norm-mutation-rotation L1>L0 theme; conditional on D4's disposition)

**Rationale:**
- D1/D3/D6 are independent and can fire in parallel (Wave 1)
- D2 re-reads the incremental-least-squares file after D1 lands, so it must wait for D1's integrator-per-report pass to commit; D4 is independent and can wait alongside
- D5 (the conditional abstractor) must wait for D4's report to see whether the L1 entry is promotion-ready before authoring the theme

## Open questions / caveats

1. **Cycle-031 routed candidates: ON-DISK existence pre-verified.** All three cycle-031 routed candidates have been existence-checked via file-system queries:
   - `book/src/L2-L1/incremental-least-squares-composition-lowering.md` ✓ EXISTS (41183 bytes, c030 live)
   - `book/src/L1-L0/back-solve-mutation-rotation.md` ✓ EXISTS (54168 bytes, firm status confirmed)
   - All 4 batch-6-firm-theme audit targets ✓ ALL EXIST and are FIRM (apply-nonlinear-pencil-MR, deflate-composition-lowering, gram-fold-specialization, orthogonalize-composition-lowering)

2. **D4 conditional launch.** The D5 (abstractor on matrix-weighted-norm-mutation-rotation) dispatch is conditioned on D4's report. If D4 surfaces blockers to L1 promotion (e.g., missing test assertion, variant-axis gate still open), the c032 integration may defer D5 to c033 or re-scope it as a lower-priority follow-up. The dispatch plan marks D5 as "conditional"; the integrator-per-report gate will re-read the plan and D4's report disposition.

3. **D2 serial ordering.** The back-solve `verified_against:` audit (D2) must run AFTER the incremental-least-squares prose rework (D1) is applied, so D2 sees a stable on-disk state when it re-reads the L2>L1 theme. This is captured in the Wave 2 sequencing.

4. **D6 bath-6-cohort audit scope.** The 4-theme batch-6 audit cohort (D6) bundles 4 distinct themes. Each theme already carries 1–2 `verified_against:` blocks from prior cycles. The c032 audit is an additive round (standard sibling-audit cadence per the lowering-verifier discipline). If any of the 4 themes surfaces a firm-status reduction risk (e.g., a finding contradicts a prior audit), the integrator will flag it for human review.

5. **Priority.md post-c031 state.** The orchestrator already retired 2 stale priority lines (`:36` and `:37`, both from cycle-025 active head) after the c031 no-op dispatches. The cycle-032 planner has read the current post-c031 plan and is dispatching from the Updated backlog. Future cycles should continue the pre-dispatch existence check (friction-ledger candidate `cycle-planner-pre-dispatch-existence-check-of-target-artifact` is now a routine planner discipline bullet).

6. **D6 combined batch-6 audit risk.** Batching 4 firm-theme audits into one dispatch risks token-budget overshoot if any theme has dense `verified_against:` content. If the dispatch context limit is hit, the integrated will split it (e.g., 2 themes per dispatch in a follow-on wave). Precedent: cycle-030 ran 4 lowering-verifier dispatches as separate reports; cycle-032 is attempting a combined 4-theme report to test bundling efficiency.

---

## Dispatch summary

| # | Agent | Scope | Wave | Deps | Status |
|---|-------|-------|------|------|--------|
| D1 | lifter | incremental-least-squares-composition-lowering prose rework (4 "forthcoming" sites) | 1 | none | pending |
| D2 | lowering-verifier | back-solve-mutation-rotation verified_against audit | 2 | D1 | pending |
| D3 | same-layer-cross-cutter | sparse_triangular_solve slice-reduction candidacy audit | 1 | none | pending |
| D4 | harvester | matrix-weighted-norm L1 firm-promotion (test-coverage gate confirmation) | 2 | none | pending |
| D5 | abstractor | matrix-weighted-norm-mutation-rotation L1>L0 theme (conditional on D4 readiness) | 3 | D4 | conditional |
| D6 | lowering-verifier | batch-6-firm-theme audit cohort (4 themes) | 1 | none | pending |

**Total dispatches: 6 pending + 1 conditional = 7 total (6 baseline, 5–6 likely to fire).**

