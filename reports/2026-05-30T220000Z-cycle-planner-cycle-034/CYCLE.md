---
agent: cycle-planner
invoked_at: 2026-05-30T220000Z
scope: cycle-034 dispatch plan
status: pending
---

# Cycle-034 dispatch plan

**FIRST primary cycle of meta-batch-10 (cycles 034/035/036; batch-10 meta-phase fires after cycle-036 finalize). Batch-9 meta-phase enacted: friction-ledger entry `cycle-planner-stale-priorities-line-recruitment` codified + skill `verify-dispatch-scope-not-already-discharged` promoted + role-spec MANDATORY pre-dispatch deliverable-presence ENFORCEMENT bullet; cycle-034 is the first test of the deeper-check enforcement.**

## Goals selected this cycle

Build immediately on batch-9's diagonal-preconditioner-apply consolidation by composing the `reciprocal` + `elementwise_product` L1 primitives (landed c033) into their shared L1>L0 lowering theme. Then surface a substantive candidate from the open backlog, applying the mandatory deeper deliverable-presence check to confirm genuinely-open frontier work (file existence + `verified_against:`-block presence + RESOLVED-grep + structural-block check). Two dispatches minimum; up to 12 if backlog candidates pass the deeper check.

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|---|---|---|---|
| D1 | abstractor | `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` composite L1>L0 theme (POSSIBLE SPLIT INTO TWO IF NEEDED) | none | **VERIFIED ABSENT** (file does not exist). Natural next step now that both L1 `reciprocal` + `elementwise_product` are firm (c033 landing). Integrator-signals suggests **possible composite single-theme co-authoring**: the two L1 leaves share the in-place-receiver-overwrite L0 mutation shape and differ only in the scalar kernel (simple real multiply vs complex reciprocal inverse-norm-squared). Precedent: `ksp-solve-mutation-rotation` thin-theme demonstrates single-theme co-authoring of a paired-kernel family. **Deliverable-presence check:** file does not exist; no `verified_against:` block yet (new theme). Recent OQ resolution search: `reciprocal-l1-l0-mutation-rotation-theme` + `elementwise-product-l1-l0-mutation-rotation-theme` filed c033 as cycle-034 routed follow-ups (integrator-signals). Structural block check: both L1 leaves are firm (c033); L0 sources (`palace/linalg/jacobi.cpp:30-69 Apply` kernel for elementwise multiply + `palace/linalg/vector.cpp:248-261 ComplexVector::Reciprocal` for reciprocal) directly readable. No test-coverage gating. No structural blockage. **Fan-out: MEDIUM-HIGH.** Both leaves are consumed across diagonal-preconditioner-apply + smoothers + polynomial-preconditioner cohorts. Routes c033-filed OQs. |
| D2 | lowering-verifier | `jacobi/chebyshev/axpby dead-code complex-transpose kernel cohort audit` (verdict-only) | none | **VERIFIED OPEN** (thin housekeeping audit, no firm theme to audit — the audit is a **negative-finding verdict on dead code**). Thin verdict-only sweep across the smoother-cohort dead-code complex-transpose kernels: jacobi `:61-69` + chebyshev `:101-110, :150-159` + axpby `ComplexVector::Subtract` variants. Confirms (a) each is unreachable from Palace consumer code, (b) the symmetric-wiring alias is the load-bearing reason (complex overwrites share the same dispatch as their real counterparts when actual complex vectors are sparse in Palace), (c) each is correctly recorded as a recognition-rule caveat in the respective firm themes. **Deliverable-presence check:** not applicable (negative-finding verdict, not a chapter to audit). Recent OQ resolution: `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit` filed c033 D1 report. Structural block check: all source regions directly readable + already firm themes documented. No blockage. **Fan-out: LOW** (audit confirmation only; no chapter-body changes expected, only a verdict-only CYCLE.md). Routed per c033 integrator-signals. |
| D3 | harvester | `book/src/L3/krylov-step.md` L3 identity-in-form operator backfill (per CLAUDE.md invariant "Identity-lowerings still require both L levels") | none | **VERIFIED ABSENT** (L3 krylov-step file does not exist; L4/L2/L1 forms are firm; L3 stub materialized c028 → identity-form confirmed by cross-layer-verifier c030, still awaits harvester refinement to firm). **CANDIDATE from open backlog per deeper-deliverable-presence check**: the cycle-009-codified lower-vocabulary-priority invariant and the identity-lowering-both-levels CLAUDE.md invariant together demand that even when a lower-layer form is value-thread-isomorphic to an upper-layer form, both layers receive an entry (using that layer's vocabulary; the lowering theme notes the identity). The L3 cohort has been static since c020 (only the firm L4-era `krylov-step.md` stub exists at `book/src/L3/` as a placeholder). **Deliverable-presence check:** `ls book/src/L3/krylov-step.md` → NOT found (stub materialized c028 at L3/index.md rough-in row; does not exist as standalone file). Recent OQ resolution search: `krylov-step-l3-identity-lowering-harvester-candidate` is not yet filed; this dispatch proposes it as a backlog surfacing (LOW-priority methodology work, not HIGH-fan-out vocabulary). Structural block check: all source anchors are firm (L2 `book/src/L2/krylov-step.md` firm c020; L4 form fully specified in `book/src/L4/krylov-step.md`; L3 identity-form confirmed at c030 cross-layer-verifier pass). Per CLAUDE.md invariant, the identity-in-form entry still requires authoring in L3 vocabulary. No test-coverage gating. **Fan-out: LOW** (identity-in-form → no downstream unblocking; methodology-priority only). Rationale: batch-10 opening is an opportunity to advance the L3 vocabulary tier (lowest since c020) per the lower-vocabulary-priority directive. Routes proposed new OQ `krylov-step-l3-identity-harvester-backfill`. |

## Overlap analysis

**No overlapping artifact regions. Three dispatches operate on disjoint files:**
- D1 writes to `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (new file, or two separate `reciprocal-mutation-rotation.md` + `elementwise-product-mutation-rotation.md` if split) + may update `book/src/L1-L0/index.md` (theme append) + `SUMMARY.md` (theme registration).
- D2 writes only to the dispatch CYCLE.md (verdict-only; no artifact chapters involved).
- D3 writes to `book/src/L3/krylov-step.md` (new file; replaces the c028-materialized rough-in row in L3/index.md with a firm entry) + may update `SUMMARY.md` (operator registration) + L3/index.md (rough-in → firm promotion).

**Index updates (L1-L0/index, L3/index) are append-only or promotion-only** — D1 appends a row to L1-L0/index.md dep-map; D3 promotes an existing rough-in row in L3/index.md to firm (in-place status change, not append). No row conflicts between D1 and D3. **D1 is independently scoped from D2/D3.**

**All three are independent-dependency, PARALLEL-DISPATCHABLE.**

## Sequencing schedule

**SINGLE WAVE (all parallel):**
- Wave 1: D1, D2, D3 (no forward-blocking dependencies; all operate on disjoint regions).

## Deliverable-presence verification (cycle-034 application of the MANDATORY deeper-check enforcement)

**Cycle-032 integrator-signals friction-ledger candidate `cycle-planner-stale-priorities-line-recruitment` (escalated recurrence-3 across batch-9; batch-9 meta-phase codified it):** the c033 cycle-planner CYCLE.md documented the deeper deliverable-presence check applied to all three c033 dispatches (3/3 genuinely-open, WORKING PRECEDENT). This cycle-034 plan applies the same deeper check to the three proposed dispatches. The four-step check: **(1) File existence** (`ls book/src/<layer>/<slug>.md`); **(2) Audited already** (for L1>L0 themes / audited operators, grep for `verified_against:` blocks); **(3) OQ-RESOLVED-grep** (scan `scaffolding/open-questions.md` for recent RESOLVED/CLOSED dispositions on the target slug); **(4) Structural-block check** (test-coverage gates, promotion blockers, unimplemented Palace stubs, unanchored forwards-references).

### D1: reciprocal-elementwise-product-mutation-rotation (abstractor, L1>L0 theme)
- **(1) File existence:** `ls book/src/L1-L0/reciprocal-mutation-rotation.md` → **NOT found** ✓; `ls book/src/L1-L0/elementwise-product-mutation-rotation.md` → **NOT found** ✓
- **(2) Theme already has verified_against block:** N/A (new theme). ✓
- **(3) Recent OQ resolution search:** `grep 'reciprocal-l1-l0-mutation-rotation\|elementwise-product-l1-l0-mutation-rotation.*RESOLVED\|CLOSED' scaffolding/open-questions.md` → **NOT found** ✓. OQs `reciprocal-l1-l0-mutation-rotation-theme` + `elementwise-product-l1-l0-mutation-rotation-theme` filed c033 as cycle-034 routed follow-ups (integrator-signals "Suggested next dispatches" section).
- **(4) Structural block check:** Both L1 `reciprocal` + `elementwise_product` are firm (c033 landing); no test-coverage or promotion gates. L0 sources verified via codemap (ComplexVector::Reciprocal `palace/linalg/vector.cpp:248-261`, Apply kernels `palace/linalg/jacobi.cpp:30-69/:99-104`) are directly readable. No structural blockage. ✓
- **VERDICT: GENUINELY OPEN, READY TO DISPATCH** ✓

### D2: jacobi/chebyshev/axpby dead-code complex-transpose kernel audit (lowering-verifier, verdict-only)
- **(1) File existence:** N/A (verdict-only; no new chapter file to exist). The source regions already exist and are firm-themed. ✓
- **(2) Audited already:** N/A (verdict-only; no `verified_against:` block being authored — the verdict confirms the existing caveats in firm themes). ✓
- **(3) Recent OQ resolution search:** `grep 'jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit.*RESOLVED\|CLOSED' scaffolding/open-questions.md` → **NOT found** ✓. OQ `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit` filed c033 D1 report as cycle-034+ candidate.
- **(4) Structural block check:** All source regions (jacobi `:61-69`, chebyshev `:101-110` + `:150-159`, axpby ComplexVector::Subtract) are firm code (already cited in firm themes). The verdict is a static-analysis/reachability check against Palace consumer call-sites (all existing, no Palace changes needed). No structural blockage. ✓
- **VERDICT: GENUINELY OPEN, READY TO DISPATCH** ✓

### D3: krylov-step L3 identity-form backfill (harvester, L3 operator)
- **(1) File existence:** `ls book/src/L3/krylov-step.md` → **NOT found** ✓ (the L3/index.md rough-in row exists per c028 materialization; the standalone file does not).
- **(2) Audited already:** N/A (new operator file; no `verified_against:` blocks exist yet). ✓
- **(3) Recent OQ resolution search:** `grep 'krylov-step-l3.*RESOLVED\|CLOSED' scaffolding/open-questions.md` → **NOT found** ✓. OQ is not yet filed; this dispatch surfaces it as a backlog candidate `krylov-step-l3-identity-harvester-backfill`.
- **(4) Structural block check:** L2 `book/src/L2/krylov-step.md` is firm (c020); L4 `book/src/L4/krylov-step.md` is firm (c006). L3 form is identified as identity-in-form per the c030 cross-layer-cross-cutter verb ("both `iterate_while` and the body are identical across L4/L3/L2" in cross-layer-cross-cutter c030 report). Per CLAUDE.md "Identity-lowerings still require both L levels" invariant, the L3 entry must exist (even in identity form). No Palace-component dependency (identity form is constructed from existing vocabulary). No test-coverage gating. No structural blockage. ✓
- **VERDICT: GENUINELY OPEN, READY TO DISPATCH** ✓

**ALL THREE PASS THE DEEPER DELIVERABLE-PRESENCE CHECK. NO ALREADY-DISCHARGED WORK DETECTED.**

## Open questions / caveats

**D1 composite-vs-split decision:** The integrator-signals suggested D2/D3 (c033 dispatch) could be **combined into a single harvester dispatch** (two leaves in one report); D1 (abstractor) faces the same decision: **reciprocal-elementwise-product-mutation-rotation could be authored as a single thin composite theme** (two kernels, shared in-place-receiver-overwrite shape, differ only in scalar operation) **or as two separate narrow themes** (one-kernel each). The `ksp-solve-mutation-rotation` precedent (cycle-010, `book/src/L2-L1/ksp-solve-mutation-rotation.md`) demonstrates a thin two-sub-pattern theme can be authored as a single coherent chapter. **Recommendation:** author as a **single composite theme** titled `reciprocal-elementwise-product-mutation-rotation` with two sub-patterns (A: reciprocal, B: elementwise-product) — this mirrors the precedent, keeps the cohort unified, and signals the shared L1>L0 mutation shape. The repairer can split if integration surfaces a reason (unlikely).

**D3 backlog rationale:** L3 has been static (only stubs) since c020; the lower-vocabulary-priority invariant (CLAUDE.md §"Lower-level shared vocabulary takes priority") argues that L3 operator backfill (identity-in-form or otherwise) should be prioritized over further L4 expansion. The krylov-step L3 entry is a low-fan-out, low-cost identity-in-form backfill that discharges an invariant. It is ranked LOW-priority (does not unblock downstream work), but batch-10 opening is an opportunity to re-balance the vocabulary tiers. If a higher-fan-out candidate surfaces from the backlog, demote D3 in favor of that.

**D3 will become an OQ:** This dispatch surfaces `krylov-step-l3-identity-harvester-backfill` as a fresh OQ for the backlog; the plan should be updated if the planner wishes to retain it as a candidate for future cycles (vs retiring it if another L3 candidate takes priority).

