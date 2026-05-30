---
agent: cycle-planner
invoked_at: 2026-05-30T150000Z
scope: cycle-033 dispatch plan
status: pending
---

# Cycle-033 dispatch plan

**THIRD/FINAL primary cycle of meta-batch-9 (cycles 031/032/033; batch-9 meta-phase fires AFTER this cycle-033 integrator-finalize commit).**

## Goals selected this cycle

Close the batch-9 primary cycles with a focused, verified-open cohort: advance the `jacobi-smoother` L1 landing (c032) into its L1>L0 lowering theme (natural continuation), and harvest the two foundational elementwise-vector primitives that complete the diagonal-preconditioner-apply infrastructure stack. All three dispatches are structurally independent, parallel-compatible, low-interaction with prior reports, and deliver measurable vocabulary extension (1 new theme, 2 new L1 primitives). This cycle prioritizes **deliverable-presence verification** (not just file existence) per the cycle-032 orchestrator override signal and integrator-signals friction-ledger candidate.

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|---|---|---|---|
| D1 | abstractor | `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` L1>L0 theme | none | **VERIFIED ABSENT** (file does not exist). Natural next step now that L1 `jacobi-smoother` is firm (c032 landing). Structural sub-patterns A/B/C all sketched in c032 integrator-signals OQ: (A) setup body lift (`dinv` -> pure output), (B) apply body lift (elementwise scale), (C) `omega==0.0` spectral-radius sub-action (identical to `chebyshev-smoother-mutation-rotation` precedent). Precedent: `ksp-solve-mutation-rotation` thin-theme. **Deliverable-presence check:** `ls /home/crutcher/git/palace_whiteroom/book/src/L1-L0/jacobi-smoother-mutation-rotation.md` → NOT found. **Fan-out: MEDIUM-HIGH.** 5 firm consumer sites (jacobi + chebyshev via shared diagonal setup) become the lowering theme's downstream call-site catalog. Routes `jacobi-smoother-mutation-rotation-l1-l0` OQ (c032 filed, TOP routed). |
| D2 | harvester | `book/src/L1/reciprocal.md` L1 primitive | none | **VERIFIED ABSENT** (file does not exist). Lower-layer shared vocabulary: the elementwise reciprocal vector operation (`x[i] -> 1/x[i]`). Source: `ComplexVector::Reciprocal()` **`palace/linalg/vector.cpp:248-261`** (real `Vector` overload adjacent). Element-type variant axis (real/complex). Shared forward-reference by TWO firm L1 chapters: `assemble-diagonal.md` + `jacobi-smoother.md` (c032 landing). Converging-references bar met (≥2 per CLAUDE.md stub-creation invariant threshold). Harvester dispatch preferred over claim-free stubs per CLAUDE.md "Lower-level shared vocabulary takes priority". **Deliverable-presence check:** `ls /home/crutcher/git/palace_whiteroom/book/src/L1/reciprocal.md` → NOT found. **Fan-out: HIGH.** Reused by every firm constructed-operator gate consuming a diagonal-preconditioner chain (current 2 firms; expected expansion). Routes `reciprocal-and-elementwise-product-l1-primitives` OQ (c032 filed; planner selection this cycle). |
| D3 | harvester | `book/src/L1/elementwise_product.md` L1 primitive | none | **VERIFIED ABSENT** (file does not exist). Lower-layer shared vocabulary: the elementwise vector product (`y[i] = x[i] * z[i]`). Source: `Apply(dinv, x, y)` pattern in **`palace/linalg/jacobi.cpp:30-69`** and **`:99-104`** (the diagonally-scaled multiply forms; the pure elementwise-product kernel embedded in the Jacobi apply). Shared forward-reference by TWO firm L1 chapters: `assemble-diagonal.md` + `jacobi-smoother.md` (c032 landing). Converging-references bar met (≥2 per CLAUDE.md stub-creation invariant). Harvester dispatch preferred. **Deliverable-presence check:** `ls /home/crutcher/git/palace_whiteroom/book/src/L1/elementwise_product.md` → NOT found. **Fan-out: HIGH.** Reused by every diagonal-preconditioner and polynomial-smoother consumer. Routes `reciprocal-and-elementwise-product-l1-primitives` OQ (c032 filed; planner selection this cycle). |

## Overlap analysis

**No overlapping artifact regions. Three dispatches operate on disjoint files:**
- D1 writes to `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` (new file) + may update `book/src/L1-L0/index.md` (theme append) + `SUMMARY.md` (theme registration).
- D2 writes to `book/src/L1/reciprocal.md` (new file) + may update `book/src/L1/index.md` (operator append) + `SUMMARY.md` (operator registration).
- D3 writes to `book/src/L1/elementwise_product.md` (new file) + may update `book/src/L1/index.md` (operator append) + `SUMMARY.md` (operator registration).

**Index updates (L1/index and L1-L0/index) are append-only at dep-map level** — D2 and D3 append independent rows to `L1/index.md` dep-map; D1 appends independent row to `L1-L0/index.md` dep-map. No row conflicts. **D1 forward-references D2/D3:** the theme prose will reference the `reciprocal` and `elementwise_product` primitives as plain text (not live links) per `rough-in-forward-reference-must-be-plain-text-not-live-link` discipline — the files do not exist at D1 authoring time. Integrator-per-report may upgrade to live links in-cycle once D2/D3 land (both references will be on-disk + verified before D1 integrates).

**All three are independent-dependency, PARALLEL-DISPATCHABLE.**

## Sequencing schedule

**SINGLE WAVE (all parallel):**
- Wave 1: D1, D2, D3 (no forward-blocking dependencies; D1's plain-text forward-references will be upgraded in-cycle once D2/D3 land).

## Deliverable-presence verification (cycle-033 deeper-check enforcement per c032 orchestrator signal)

**Cycle-032 integrator-signals friction-ledger candidate `cycle-planner-stale-priorities-line-recruitment` (recurrence-2-in-batch-9):** the c032 planner's file-existence check was insufficient; c032 demonstrates the need for deliverable-presence verification (firm themes already holding `verified_against:` blocks, slices already audited, promotions already test-gated-blocked, etc.). **This cycle-033 plan applies the deeper check to all three proposed dispatches:**

### D1: jacobi-smoother-mutation-rotation (abstractor, L1>L0 theme)
- **(1) File existence:** `ls book/src/L1-L0/jacobi-smoother-mutation-rotation.md` → **NOT found** ✓
- **(2) Theme already has verified_against block:** N/A (new theme). ✓
- **(3) Recent OQ resolution search:** `grep 'jacobi-smoother-mutation-rotation.*RESOLVED\|CLOSED' scaffolding/open-questions.md` → **NOT found** ✓. OQ `jacobi-smoother-mutation-rotation-l1-l0` filed c032 as TOP cycle-033 routed candidate (currently in integrator-signals "Suggested next dispatches" section).
- **(4) Structural block check:** L1 `jacobi-smoother` is firm (c032 landing); no test-coverage or promotion gates. L0 sources (`palace/linalg/jacobi.cpp:74-95` setup, `:30-69/:99-104` apply) are directly readable. No structural blockage. ✓
- **VERDICT: GENUINELY OPEN, READY TO DISPATCH** ✓

### D2: reciprocal (harvester, L1 primitive)
- **(1) File existence:** `ls book/src/L1/reciprocal.md` → **NOT found** ✓
- **(2) Already-audited check:** No `verified_against:` block exists (it is a new file). ✓
- **(3) Recent OQ resolution search:** `grep 'reciprocal.*RESOLVED\|CLOSED' scaffolding/open-questions.md` → **NOT found** ✓. OQ `reciprocal-and-elementwise-product-l1-primitives` filed c032 as planner-selection candidate (currently in integrator-signals "Suggested next dispatches" section).
- **(4) Structural block check:** L0 source (`palace/linalg/vector.cpp:248-261` ComplexVector::Reciprocal + real overload nearby) is firm API, no unimplemented stubs. Per CLAUDE.md "Unimplemented Palace stub policy", this is directly harvestable. No test-coverage gating (the reciprocal is transparent arithmetic, not a semantically-complex operator). No structural blockage. ✓
- **VERDICT: GENUINELY OPEN, READY TO DISPATCH** ✓

### D3: elementwise_product (harvester, L1 primitive)
- **(1) File existence:** `ls book/src/L1/elementwise_product.md` → **NOT found** ✓
- **(2) Already-audited check:** No `verified_against:` block exists (it is a new file). ✓
- **(3) Recent OQ resolution search:** `grep 'elementwise_product.*RESOLVED\|CLOSED' scaffolding/open-questions.md` → **NOT found** ✓. OQ `reciprocal-and-elementwise-product-l1-primitives` (shared with D2) filed c032 as planner-selection candidate.
- **(4) Structural block check:** L0 source (the `Apply` kernel pattern in `palace/linalg/jacobi.cpp:30-69` + `:99-104`; the pure elementwise-multiply in both arms) is firm. No unimplemented stubs. Per CLAUDE.md, this is directly harvestable. No test-coverage gating. No structural blockage. ✓
- **VERDICT: GENUINELY OPEN, READY TO DISPATCH** ✓

**ALL THREE PASS THE DEEPER DELIVERABLE-PRESENCE CHECK. NO ALREADY-DISCHARGED WORK DETECTED.**

## Open questions / caveats

**None.** The three dispatches are structurally clear, source-verified, and independent. D1 inherits the sketched sub-patterns from the c032 OQ filing + the `chebyshev-smoother-mutation-rotation` precedent. D2/D3 can be authored together by a single harvester dispatch (shared source region, same shape contract, paired forward-references in the artifact).

**Optional co-dispatch consideration:** the integrator-signals suggest D2 and D3 could be **combined into a single harvester dispatch** (one report authoring both leaves in sequence) rather than two separate dispatches. This would reduce wave-mate count to 2 (D1 + D2/D3-combined) while delivering the same vocabulary. The co-dispatch would be titled e.g. `reciprocal-and-elementwise_product L1 primitives` with a unified L0 source anchor and two independent proposed-changes blocks. This is a planning decision; the planner submits both options (separate 3-dispatch plan as above, or combined 2-dispatch plan with D2/D3 merged). **Recommend:** keep as 3 separate dispatches for maximum parallelism and scope clarity (the next integrator can always choose to run them serially if cross-dispatch context is beneficial; dispatch-phase isolation already enforces clean boundaries). The integrator's per-report serial execution will apply them in order regardless.

