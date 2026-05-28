---
agent: cycle-planner
invoked_at: 2026-05-28T22:10:14Z
scope: cycle-016 dispatch plan
status: pending
---

# Cycle-016 dispatch plan

**Cycle-016 is the FIRST primary cycle of meta-batch-4** (cycles 016/017/018 form batch-4 under the 3:1 meta cadence; meta-phase fires after cycle-018). Cycle counter continues from cycle-015 without reset.

## Goals selected this cycle

Cycle-015 closed meta-batch-3 with a clean 6-report single wave, two gated promotions enacted, and the first full `partly-constructive` lifecycle demonstrated. The cycle-016 dispatch prioritizes the unblocked items surfaced in the cycle-015 integrator-signals section and addresses the three strongest friction signals from batch-3: (1) **producer-citation-drift** (persistent across all 3 batch cycles, strongest recurring friction, verify-citation-range repeatedly not self-invoked), (2) **slice-removal non-link-prose-reference grep completeness** (new tooling gap identified at cycle-015 critique), (3) **lower-layer-shared-vocabulary bias** (per user directive, prefer L1/L2/L3 firm operators and lowering-theme completion over L4 vocabulary expansion when both eligible). The cycle dispatches the top 5 Suggested next dispatches from cycle-015 integrator-signals, plus one citation-sweep sibling and one lowering-theme completion, holding to 7 dispatches (conservative wave-1 to allow for meta-batch-4 discoveries) and positioning cycle-017/018 for the gmres v0.6→v0.7 self-rotation carry-forward and NLEPS work.

## Dispatches

1. **abstractor** — `divfree-projector L1>L0 mutation-rotation theme` — **deps: none**
   - **rationale**: The firm L1 entry `book/src/L1/divfree-projector.md` (promoted cycle-015) now supports a clean L1>L0 lowering theme. This closes the long-standing divfree L1>L0 gap and is the top-ranked Suggested next dispatch from cycle-015 integrator-signals. Self-verify every citation before emitting per cycle-015 producer-citation-drift signal.

2. **lifter** — `L4 chebyshev residual forM_/foldM prose cleanup (3 sites)` — **deps: none**
   - **rationale**: Three stale `forM_`/`foldM` prose mentions remain in `book/src/L4/chebyshev.md` (~L368/L382/L547) outside the cycle-015 re-anchor blocks; surgical 3-site prose refresh naming `iterate_while_pure`/`iterate_while_pure_L3`. Unblocked and flagged by cycle-015 as a small-scope surgical fix. Closes OQ `l4-chebyshev-residual-formm-foldm-prose-cleanup`.

3. **lifter** — `L3 chebyshev downward-prose iterate-while refresh (1 line)` — **deps: 2**
   - **rationale**: Sibling to dispatch 2; `book/src/L3/chebyshev.md:236-238` names the now-superseded L4 `foldM`/`forM_` combinators; surgical one-line prose refresh, no L3 semantics change. Depends on dispatch 2 to avoid conflicting edits to the same section. Closes OQ `l3-chebyshev-downward-prose-iterate-while-refresh`.

4. **lifter** — `L4 krylov-step cg.md citation sweep (8 pointers)` — **deps: none**
   - **rationale**: The cycle-015 L3 sweep found dangling `cg.md` pointers persist in the distinct `L4/krylov-step.md` operator entry; sibling sweep applying the cycle-013/014/015 lifted-evidence convention. Self-verify relocated pointers land at TERMINAL firm homes (cycle-015 L3 sweep pointed 2 re-anchors at relocated-dangle targets). Closes OQ `l4-krylov-step-cg-md-citation-sweep`.

5. **lifter** — `L2 krylov-step cg.md citation sweep (12 pointers)` — **deps: none**
   - **rationale**: Companion to dispatch 4; `book/src/L2/krylov-step.md` carries same dangling pointers as L4. Non-dependent (L3 sweep does NOT depend on either L4 or L2; re-anchors at L2 terminus). Self-verify relocated pointers land at TERMINAL firm homes (the L3 sweep terminates at L2:138, not transitive-dangling L4 sites). Closes OQ `l2-krylov-step-cg-md-citation-sweep`.

6. **layer-intro-author** — `L0 bundle-6 #5: fem/libceed/operator.cpp chapter` — **deps: none**
   - **rationale**: Bundle-6 #4 (`fem-bilinearform-file`) landed cycle-015; next ranked candidate is `fem/libceed/operator.cpp` (verified callee defs `CeedOperatorFullAssemble` @ palace/fem/libceed/operator.cpp:455 + `CeedOperatorCoarsen` @ :525). This also retires the deliberate plain-text non-link reference in `fem-bilinearform-file.md` (convert it to a live link once the chapter exists). L0 bundle chapters are citation-dense — self-verify each range before emitting proposed-changes blocks, do NOT write `book/` directly. Closes OQ `bundle-6-l0-libceed-operator-file-next-candidate`.

7. **abstractor** — `eigsolve-convergence-reason-mapping L1>L0 partly-constructive theme (8-row enum)** — **deps: none**
   - **rationale**: Cycle-014 lowering-verifier audited this theme and confirmed 8 EigStatus mappings are literature-anchored but materialization sites remain zero (per cycle-014 negative-anchor verification). The theme structure is firm; the enum mappings are partly-constructive (evidence-grounded via literature, not materialised in Palace source). This is the second partly-constructive entry to be newly emitted in the artifact after eigsolve's full lifecycle (cycle-013 ENTRY, 014 audit, 015 EXIT→firm) and divfree's ENTRY (cycle-013) + audit (cycle-014) + EXIT→firm (cycle-015). Will validate the cycle-012-codified transient-gate mechanism by a third demonstration. OQ carry-forward from cycle-014 lowering-verifier findings. Self-verify before emitting.

## Overlap analysis

| Pair | Overlap | Sequencing note |
|---|---|---|
| 1 vs 2–7 | none | abstractor on divfree theme (new file create) does not touch any file modified by lifter/layer-intro-author dispatches |
| 2 vs 3 | **yes** | both edit `L4/chebyshev.md` and `L3/chebyshev.md` respectively, plus dispatch 2 may touch L4 prose outside dispatch 3's scope; marked sequential (2→3) |
| 2 vs 4–7 | none | L4 chebyshev prose touches only L4/chebyshev.md; L4/L2 krylov-step and L0 bundle chapters are distinct files |
| 3 vs 4–7 | none | L3 chebyshev prose touches only L3/chebyshev.md; non-overlapping with lifter and layer-intro-author scopes |
| 4 vs 5 | none | L4/krylov-step.md vs L2/krylov-step.md; distinct files; both are citation-refinement-only, no structural changes |
| 4,5 vs 6,7 | none | krylov-step citation sweeps (L4, L2) vs L0 bundle chapter creation vs eigsolve theme creation; no file overlap |
| 6 vs 7 | none | layer-intro-author on `fem/libceed/operator.cpp` L0 chapter (new file) vs abstractor on `eigsolve-convergence-reason-mapping` L1>L0 theme (new file); distinct files |

## Sequencing schedule

**Wave 1 (parallel, no dependencies):**
- Dispatch 1: abstractor on `divfree-projector L1>L0 mutation-rotation theme`
- Dispatch 4: lifter on `L4 krylov-step cg.md citation sweep`
- Dispatch 5: lifter on `L2 krylov-step cg.md citation sweep`
- Dispatch 6: layer-intro-author on `bundle-6 #5 fem/libceed/operator.cpp`
- Dispatch 7: abstractor on `eigsolve-convergence-reason-mapping partly-constructive theme`

**Wave 2 (after wave-1 reports land, sequential dependency):**
- Dispatch 2: lifter on `L4 chebyshev residual forM_/foldM prose cleanup` (no dependency, but positioned wave-2 to preserve tight sequencing with dispatch 3)
- Dispatch 3: lifter on `L3 chebyshev downward-prose iterate-while refresh` (depends on dispatch 2 for non-conflicting edits)

**Rationale**: The dependency edge (2→3) requires serial ordering; dispatching both in wave-2 ensures wave-1 reports land before either chebyshev prose editor runs, allowing them to see the full artifact state at their read-time and avoiding edit conflicts from simultaneous L3/L4 prose updates.

## Open questions / caveats

1. **dispatch 7 (eigsolve-convergence-reason-mapping) novelty risk** — This is the second new partly-constructive theme to be emitted (after cycle-015's divfree/chebyshev enactments). The cycle-012-codified transient-gate mechanism is validated by the divfree ENTRY→AUDIT→EXIT→firm lifecycle and divfree/chebyshev enactments at cycle-015. The eigsolve-convergence-reason-mapping variant (literature-anchored enum with zero materialization sites) is structurally similar to the partly-constructive sub-pattern B that survived in `eigsolve-mutation-rotation` until cycle-015. Proceeding with confidence that the same pattern can be emitted; if critic rejects on "partly-constructive without firming path" grounds, the promotion condition ("literature sources to Palace implementation evidence OR confirmed zero materialization → stay partly-constructive as artifact of Palace's current incompleteness") should be re-articulated in the emission.

2. **slice-removal grep tooling (process friction, not dispatch-blocking)** — Cycle-015 integrator-signals flagged a tooling gap: markdown-link checks miss non-link prose references when slices are removed. The `phase-1-slice-reduction-audit` skill was extended (cycle-015 meta-phase codification) but the batch-3 signal suggests a dedicated non-link-reference grep may be warranted before the next major slice removal. This does not block dispatch-7 or future removals (repairer can still grep manually), but is flagged for possible meta-phase cycle-018 tooling decision.

3. **divfree.hpp doc-tension OQ** — Carry-forward from cycle-015; listed as priority #5 (lifter/cross-layer-cross-cutter). Not selected for cycle-016 to keep wave count at 7 and reserve capacity for meta-batch-4 discoveries. Routed to cycle-017/018 if no higher-priority friction emerges.

---

**Report prepared by cycle-planner at 2026-05-28T22:10:14Z for cycle-016 dispatch.**
