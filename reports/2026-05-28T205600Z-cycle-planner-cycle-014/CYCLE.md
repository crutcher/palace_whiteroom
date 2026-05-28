---
agent: cycle-planner
invoked_at: 2026-05-28T205600Z
scope: cycle-014 dispatch plan
status: pending
---

# Cycle-014 dispatch plan

## Goals selected this cycle

Cycle-014 is the **SECOND primary cycle of meta-batch-3** (cycles 013/014/015; meta-phase fires after 015). The batch-3 opening (cycle-013) landed heavy partly-constructive use (4 instances: eigsolve promotion, divfree entry, eigsolve-convergence-reason-mapping, chebyshev L4 rough-in) + the first live partly-constructive→firm promotion mechanism test, plus cycle-013 integrator-signals flagged three recurring signals for meta-phase: (1) partly-constructive status exercised heavily, (2) citation line-drift recurring across ~6 reports + skill-uptake-survey gap, (3) discovery→authoring plan-kind scope-stretch observation.

This cycle prioritizes: **closing partly-constructive entries and gated dependencies** (divfree verification, chebyshev L4 vocabulary, eigsolve-convergence-reason mapping gate) **+ catching citation line-drift through deliberate codemap-first localization + lowering-verifier audits** (on the 3 new firm L1>L0 themes from cycle-013 + the partly-constructive siblings). This work feeds evidence to the cycle-015 meta-phase on the health of the partly-constructive mechanism and citation discipline. A smaller wave (8 dispatches) balances this against the cycle-013 11-report maximum and leaves cycle-015 room for carry-forward larger items.

## Dispatches

1. **agent: `lowering-verifier`**  
   **scope: `divfree-weakdiv-sign-convention-l0-verify` — audit the MFEM-vendored `MixedVectorWeakDivergenceIntegrator` WeakDiv sign reading; verify-citation-range on `palace/linalg/divfree.cpp:113`**  
   **deps: none**  
   **rationale:** Cycle-013 landed `L1/divfree-projector` as `partly-constructive` with the idempotence law + divergence-free output depending on the unverified `WeakDiv ≈ GᵀM` sign. The lowering-verifier audit is the explicit promotion gate. Closes OQ `divfree-weakdiv-sign-convention-l0-verify` + `divfree-projector-l1-l0-lowering-verifier-followup` (cycle-013).

2. **agent: `lowering-verifier`**  
   **scope: `orthogonalize-mutation-rotation` exhaustiveness audit — the 3 new firm L0 variant loop-structures landed cycle-013; verify-citation-range on `palace/linalg/orthog.hpp` (MGS single / CGS split / CGS2 doubled ranges) + confirm no omitted L0 sites**  
   **deps: none**  
   **rationale:** Cycle-013 abstractor landed `book/src/L1-L0/orthogonalize-mutation-rotation.md` firm with 3 sub-patterns; lowering-verifier audits the sub-pattern recognition exhaustiveness. Codemap-based citation verify on the orthog.hpp:41-53 MGS, :78 CGS, :75-88 CGS2 ranges. Closes OQ `orthogonalize-mutation-rotation-lowering-verifier-audit` (cycle-013).

3. **agent: `lowering-verifier`**  
   **scope: `chebyshev-lowering-themes-lowering-verifier-followup` — audit the 2 new firm L1>L0 + L2>L1 themes; verify sub-patterns (4 sub-patterns on L1>L0 + per-degree-step fusion on L2>L1) against Palace `palace/linalg/chebyshev.cpp` + confirm no coefficient mismatches**  
   **deps: none**  
   **rationale:** Cycle-013 abstractor landed `chebyshev-smoother-mutation-rotation` (firm; 4 sub-patterns) + `chebyshev-iteration-fusion` (firm; first L2-L1 chapter). Lowering-verifier exhaustiveness audit. Closes OQ `chebyshev-lowering-themes-lowering-verifier-followup` (cycle-013).

4. **agent: `combinator-miner`**  
   **scope: `chebyshev-l4-wrapper-iteration-vocabulary-reconcile` — reconcile the L4 chebyshev `forM_`/`foldM` iteration combinators against the firm `iterate_while` family; propose rewrite using `iterate-while-pure` + step-count predicates OR firm the forM/foldM as L4 rows**  
   **deps: none**  
   **rationale:** Cycle-013 harvester landed `L4/chebyshev` as `rough-in` because the wrapper's iteration combinators are un-anchored and compete with the firm `iterate-while` family. The combinator-miner reconciliation proposal flips the entry rough-in → firm. High-value unblock (L4 firm 3→4). Closes OQ `chebyshev-l4-wrapper-iteration-vocabulary-reconcile` (cycle-013). Cited in integrator-signals as highest-priority unblock.

5. **agent: `lowering-verifier`**  
   **scope: `eigsolve-convergence-reason-mapping-promotion` — single global gate on the 8 partly-constructive diverged-row EigStatus map in the new L1>L0 sub-theme; verify no additional undocumented reason-code mappings exist in Palace; confirm the 8-row count is exhaustive**  
   **deps: none**  
   **rationale:** Cycle-013 lifter landed `eigsolve-convergence-reason-mapping.md` partly-constructive with negative anchors (whole-tree zero EPSGetConvergedReason callsites). The lowering-verifier gate determines whether a future promotion can drop the partly-constructive caveat. Closes OQ `eigsolve-convergence-reason-mapping-promotion` (cycle-013).

6. **agent: `layer-intro-author`**  
   **scope: `linalg-rap-file` (L0 bundle-6 candidate #2) — author chapter overviewing `palace/linalg/rap.cpp` + `palace/linalg/rap.hpp`; RAP = Restrictive Additive Schwarz Preconditioner; single-rank reading + reference-note overlay; apply same discovery→authoring safety-net gates as cycle-013 bundle-6 #3**  
   **deps: none**  
   **rationale:** Cycle-013 integrator-signals unblocked L0 bundle-6 #2 as the next-ranked candidate (OQ `l0-bundle-6-candidates` discovery-update). The file is single-layer, small enough for discovery+authoring in one dispatch (like cycle-013 linalg-orthog-file). Carries the L0 chapter inventory toward fuller coverage. Closes OQ `l0-bundle-6-candidates` partial (#2 landing).

7. **agent: `lifter`**  
   **scope: `krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` — re-anchor the 8 dangling `cg.md` pointers in the L4>L3 krylov-step theme to the firm `L3-L2/krylov-step-body-identity.md`; verify no other cg.md-era pointers linger in L4/L3 entries**  
   **deps: none**  
   **rationale:** Cycle-013 lifter cleaned 2 line-20/line-220 residuals but identified 8 remaining dangling `cg.md` pointers at theme lines 98/109/126/200/204/210/218/231/233. Clean-up dispatch re-anchors them to the firm identity theme (already extant since cycle-009 promotion). Closes OQ `krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` (cycle-013).

8. **agent: `same-layer-cross-cutter`**  
   **scope: `chebyshev-phase1-slice-reduction` — audit the now-fully-lifted `book/src/spec/slices/chebyshev.md` slice; verify that the L3 partial-obstruction + L4 rough-in entries + 4 concept-page touches + L1/L2 firm operators have absorbed all substantive content; propose reduction to stub-and-pointer or removal per the phase-1-corpus-reduction-audit skill**  
   **deps: none**  
   **rationale:** Cycle-013 harvester landed L3/L4 chebyshev rows (previously a blocker); chebyshev.md is now fully lifted. The same-layer-cross-cutter audit (using skill `phase-1-slice-reduction-audit` promoted cycle-012, START+END boundary verification) determines the reduction verdict. Closes OQ `chebyshev-phase1-slice-reduction` (cycle-013).

## Overlap analysis

| Pair | Overlaps? | Reason |
|------|-----------|--------|
| 1 ↔ 2 | NO | Different scope: divfree vs. orthogonalize |
| 1 ↔ 3 | NO | Different scope: divfree vs. chebyshev |
| 1 ↔ 4 | NO | Different operator families |
| 1 ↔ 5 | NO | Different scope: divfree vs. eigsolve mapping |
| 1 ↔ 6 | NO | Different scope: divfree verify vs. L0 bundle |
| 1 ↔ 7 | NO | Different scope: divfree vs. krylov-step pointers |
| 1 ↔ 8 | NO | Different scope: divfree vs. chebyshev slice |
| 2 ↔ 3 | NO | orthogonalize and chebyshev are independent theme families |
| 2 ↔ 4 | NO | orthogonalize verify vs. chebyshev combinator |
| 2 ↔ 5 | NO | orthogonalize vs. eigsolve mapping |
| 2 ↔ 6 | NO | orthogonalize vs. L0 bundle |
| 2 ↔ 7 | NO | orthogonalize vs. krylov-step cleanup |
| 2 ↔ 8 | NO | orthogonalize vs. chebyshev slice |
| 3 ↔ 4 | NO | chebyshev lowering-verifier vs. L4 vocabulary (different artifacts) |
| 3 ↔ 5 | NO | chebyshev vs. eigsolve; different families |
| 3 ↔ 6 | NO | chebyshev vs. L0 bundle |
| 3 ↔ 7 | NO | chebyshev vs. krylov-step; no overlap |
| 3 ↔ 8 | YES | **Both touch the chebyshev family**: dispatch 3 audits the firm themes, dispatch 8 reduction-audits the phase-1 slice. The lowering-verifier audit (3) lands its audit findings without artifact mutation; the same-layer-cross-cutter (8) reads those audits as context but does not edit the same files. Dispatch 3 completes first (audit-only), then dispatch 8 runs. **SEQUENTIAL: 3 → 8**. |
| 4 ↔ 5 | NO | chebyshev L4 vocabulary vs. eigsolve mapping |
| 4 ↔ 6 | NO | chebyshev vocabulary vs. L0 bundle |
| 4 ↔ 7 | NO | chebyshev vocabulary vs. krylov-step citations |
| 4 ↔ 8 | NO | chebyshev L4 combinator vs. phase-1 slice audit (dispatch 4 is vocabulary, 8 is reduction audit; no artifact edit overlap) |
| 5 ↔ 6 | NO | eigsolve audit vs. L0 bundle |
| 5 ↔ 7 | NO | eigsolve vs. krylov-step citations |
| 5 ↔ 8 | NO | eigsolve vs. chebyshev slice |
| 6 ↔ 7 | NO | L0 bundle vs. krylov-step citations |
| 6 ↔ 8 | NO | L0 bundle vs. chebyshev slice |
| 7 ↔ 8 | NO | krylov-step citations vs. chebyshev slice |

**Summary:** One genuine sequential edge: dispatch 3 (chebyshev lowering-verifier) must land before dispatch 8 (chebyshev-phase1-slice-reduction audit), as the audit context depends on the lowering-verifier findings being in the artifact. All other pairs are independent.

## Sequencing schedule

**Wave 1 (parallel, all independent except the 3→8 dependency noted below):**
- Dispatches 1, 2, 4, 5, 6, 7 (6 independent lower-verifier / combinator-miner / layer-intro-author / lifter dispatches)

**Wave 2 (after Wave 1 completes):**
- Dispatch 3 (chebyshev lowering-verifier audit; completes and lands findings)

**Wave 3 (after Wave 2 completes):**
- Dispatch 8 (chebyshev-phase1-slice-reduction audit; reads lowering-verifier findings from dispatch 3 as context)

**Rationale for 3-wave structure:** Dispatch 3's audit findings inform dispatch 8's reduction verdict (the slice audit needs to see whether the lowering-verifier confirmed the lowering themes or flagged issues). By design, dispatch 3 is audit-only (no artifact mutation beyond CYCLE.md), so it lands findings synchronously at integration; dispatch 8 then reads those findings and produces its verdict. This keeps the dependency clear and bounded.

## Open questions / caveats

1. **Codemap path confidence — RAP file size**: The `linalg-rap-file` dispatch (dispatch 6) is a discovery+authoring task. Codemap confirmed the file exists (`palace/linalg/rap.cpp` + `palace/linalg/rap.hpp`). No size-bound check was done; if the file is substantially larger than the ~93-line orthog.hpp from cycle-013, the scope may need re-scoping. The integrator safety-gate (word-count + citation density check) will flag if the authored chapter exceeds reasonable bounds.

2. **Partly-constructive signal aggregation for meta-phase**: Cycle-014 is designed to close (divfree, chebyshev L4, eigsolve-convergence-mapping) or audit (cycle-013's 3 new firm themes) partly-constructive entries. The evidence will feed the cycle-015 meta-phase's assessment of the promotion-route mechanism. If any of the lowering-verifier audits (1, 2, 3, 5) flag unexpected issues with sub-pattern recognition, escalate early rather than deferring to the meta-phase.

3. **Citation-line-drift watch**: All three lowering-verifier dispatches (1, 2, 3) are expected to involve codemap-grounded citation verification. The cycle-013 integrator-signals flagged that producers skip `verify-citation-range` skill self-invocation; these dispatches are the lowering-verifier's opportunity to demonstrate tight citation discipline at the exact lines they audit. Producers (dispatches 1-3-5 lowering-verifiers) should cite verified line ranges from the codemap, not trust memory.

4. **Dispatch 4 (combinator-miner) scope uncertainty**: The chebyshev L4 wrapper reconciliation could result in either (a) a rewrite of the existing L4/chebyshev.md using `iterate-while` primitives, or (b) a proposal to firm the `forM_`/`foldM` combinators as new L4 entries. The dispatch scope does not pre-commit to either outcome. The combinator-miner's proposal section will lay out the options; the integrator will evaluate and route the decision (likely to a cycle-015 abstractor for implementation if the L4 vocabulary-refresh route is chosen).

---

**Cycle-013 carry-over OQs explicitly addressed by this plan:**
- `divfree-weakdiv-sign-convention-l0-verify` (dispatch 1)
- `divfree-projector-l1-l0-lowering-verifier-followup` (dispatch 1)
- `orthogonalize-mutation-rotation-lowering-verifier-audit` (dispatch 2)
- `chebyshev-lowering-themes-lowering-verifier-followup` (dispatch 3)
- `chebyshev-l4-wrapper-iteration-vocabulary-reconcile` (dispatch 4)
- `eigsolve-convergence-reason-mapping-promotion` (dispatch 5)
- `linalg-rap-file` bundle-6 #2 (dispatch 6)
- `krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` (dispatch 7)
- `chebyshev-phase1-slice-reduction` (dispatch 8)
