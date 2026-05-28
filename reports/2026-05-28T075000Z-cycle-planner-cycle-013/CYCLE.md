---
agent: cycle-planner
invoked_at: 2026-05-28T075000Z
scope: cycle-013 dispatch plan
status: pending
---

# Cycle-013 dispatch plan

**Cycle context**: cycle-013 is the **first primary cycle of meta-batch-3** (cycles 013/014/015; meta-phase fires after cycle-015). It immediately follows cycle-012, which closed meta-batch-2. The cycle counter is continuous — no reset at batch boundaries.

**Roadmap/priorities status**: Cycle-012 landed L1 firm 8→10 (orthogonalize + chebyshev-smoother; addressing priority #1 GATED promotion + priority #2 HEADLINE divfree unblocking). Lower-layer-shared-vocabulary priority #7 is substantially discharged (L3 now 8 firm; L2 now 2 firm). Phase-1 corpus reduction at 8/10 slices — final 2 eligible for batch-4 in this cycle.

**Highest priority this cycle**: the GATED cycle-013 abstractor on `eigsolve-getconverged-forwarder-fix-and-gated-promotion` (priority #1) must clear before other work starts. The lowering-verifier audit from cycle-012 unblocked but gated the partly-constructive → fully-firm promotion; the cycle-013 abstractor applies two specific edits (GetConverged forwarder + Sub-pattern A attribution), then drops the caveat.

## Goals selected this cycle

Cycle-013 is **batch-3 opening**; priority targets from cycle-012 integrator-signals:

1. **GATED eigsolve promotion (priority #1)** — close the Sub-pattern B partly-constructive gate by applying the lowering-verifier's identified edits. First test of the partly-constructive promotion mechanism.
2. **HEADLINE divfree harvesting (priority #2)** — lift the divergence-free projector from the now-reduced divfree slice into a firm L1 entry, unblocking further slice reduction.
3. **HEADLINE concept-page re-pointing (priority #6)** — 3 firm concept pages still cite the orthog plane-rotation sub-slice as canonical; re-point to the surviving canonical surfaces after cycle-012's corpus reduction.
4. **Lower-layer vocabulary continuation** — harvest L3/L4 chebyshev rows (identity backfill), author orthogonalize + chebyshev lowering themes (mutuation-rotation + fusion), promote L0 bundle-6 candidates if discovered.
5. **Phase-1 corpus batch-4 (final 2 slices)** — complete the slice-reduction batches (cg_preconditioning_framework + sparse_triangular_solve); 8/10 is the batching threshold.

## Dispatches

**Up to 11 dispatches** (well under the 12-dispatch cap; cycle-012 ran 8 in one wave; cycle-013 spreads across 2 waves to respect the GATED priority #1 sequencing).

### Wave 1 (6 dispatches, parallel)

1. **abstractor** — `eigsolve-getconverged-forwarder-fix-and-gated-promotion`
   - **Scope**: Apply the cycle-012 lowering-verifier audit's Edits 2+3 to `book/src/L1-L0/eigsolve-mutation-rotation.md`, drop the partly-constructive caveat, test/witness the first partly-constructive promotion gate close.
   - **Rationale**: Priority #1; unblocked-but-GATED by cycle-012; must clear first per the gated invariant.
   - **Dependencies**: none
   - **Dispatch prompt must explicitly state "cycle-013"** (per cycle-012 integrator-signals friction-ledger signal #8 — the per-report integrator should write to the correct staging directory).

2. **harvester** — `l1-divfree-projector-promotion`
   - **Scope**: Harvest the divergence-free projector operator into a firm L1 entry, lifting it from the cycle-012-reduced `book/src/spec/slices/divfree.md` into `book/src/L1/divfree-projector.md`.
   - **Rationale**: Priority #2 HEADLINE; 6 firm entries cite the divfree slice as load-bearing evidence; landing unblocks further divfree reduction and addresses the lower-layer-vocabulary signal.
   - **Dependencies**: none (independent from abstractor wave-1)
   - **Notes**: The divfree slice is now reduced; the projector is a mathematically distinct operation (applies the divergence-free projection to a given tensor field via the complementary projection mechanism); cite the reduced-slice evidence anchors. This harvester is the pathway to finally promoting divfree past the bottleneck phase-1 corpus phase.

3. **harvester** — `l3-l4-chebyshev-rows-eligible`
   - **Scope**: Author `book/src/L3/chebyshev.md` (identity-in-form backfill to L2 form per cycle-012 chebyshev-iteration firm landing) and `book/src/L4/chebyshev.md` (the ChebOp monadic wrapper operator), applying the identity-lowerings-still-require-both-L-levels invariant.
   - **Rationale**: Priority #3 (lower-layer-shared-vocabulary continuation); unblocked by cycle-012 chebyshev-iteration firm landing; L3/L4 rows gate full `chebyshev.md` slice reduction per the OQ.
   - **Dependencies**: none (parallel to dispatches 1–2)
   - **Notes**: Per cycle-012 integrator-signals, use the in-line non-adjacent identity-rotation convention (do NOT create a `book/src/L3-L1/` directory for the L3↔L1 identity relationship); annotate in-line in the L3 entry + dep-map.

4. **layer-intro-author** — `plane-rotation-concept-page-canonical-pointer-repoint`
   - **Scope**: Update 3 firm concept pages (`plane-rotation`, and 2 sibling concept pages that reference plane-rotation as canonical, TBD by scope-reading) to re-point their canonical-reference anchors from the now-reduced `book/src/spec/slices/orthog.md` plane-rotation sub-slice to the surviving canonical `plane_rotation_stream.md`.
   - **Rationale**: Priority #6 HEADLINE; cycle-012 batch-3 reduced the orthog plane-rotation sub-slice (merged into plane_rotation_stream); 3 firm concept pages still cite the orthog slice. **Do NOT write to `book/` directly — emit proposed-changes blocks only** (per cycle-012 layer-intro-author write-authority violation correction).
   - **Dependencies**: none (parallel to dispatches 1–3)
   - **Notes**: This is a surgical three-page repoint, not a full concept-page rewrite. Scope is small and specific.

5. **same-layer-cross-cutter** — `phase-1-corpus-reduction-batch-4-remaining-slices`
   - **Scope**: Audit the final 2 Phase-1 slices: `book/src/spec/slices/cg_preconditioning_framework.md` + `book/src/spec/slices/sparse_triangular_solve.md`. Apply the `phase-1-slice-reduction-audit` skill (cycle-012 promotion candidate; START+END boundary verification + unique-text anchors) and emit reduction verdicts (expected: cg_preconditioning_framework partially-absorbed by L1/L2/L4 entries; sparse_triangular_solve out-of-scope or minimal reduction).
   - **Rationale**: Priority #5; phase-1 corpus at 8/10 — final 2 eligible this cycle; cycle-012 batch-3 audit template is precedent.
   - **Dependencies**: none (parallel to dispatches 1–4)
   - **Notes**: **Invoke skill `phase-1-slice-reduction-audit` explicitly** (cycle-012 promoted at recurrence-3 + severity escalation). The cg_preconditioning_framework overlaps `L1/ksp_solve` + `L4/krylov-step` Form A + chebyshev consumer pattern — coordinate with other dispatches to avoid cross-wave overlap surprises. Sparse_triangular_solve is expected obstruction (low coverage in Palace).

6. **abstractor** — `orthogonalize-mutation-rotation-l1-l0-theme`
   - **Scope**: Author `book/src/L1-L0/orthogonalize-mutation-rotation.md` lowering theme, decomposing the L1 Gram-Schmidt orthogonalisation (any variant: MGS/CGS/CGS2) into its L0 mutation patterns (Palace's `linalg::Orthog` free-function family at `palace/linalg/orthog.hpp`).
   - **Rationale**: Unblocked by cycle-012 orthogonalize firm L1 landing; analogous to firm `axpby-mutation-rotation` / `apply-linop-mutation-rotation` themes; lower-layer coverage.
   - **Dependencies**: none (parallel to dispatches 1–5)
   - **Notes**: Per the partly-constructive invariant, if a sub-pattern relies on reconstructed evidence (negative anchors), mark that sub-part explicitly with `partly-constructive` and its promotion condition. The theme should cite the orthog.hpp location explicitly.

### Wave 2 (5 dispatches, after wave-1 completion, parallel with each other)

These depend on successful wave-1 landing (they reference or depend on wave-1 artifacts):

7. **abstractor** — `chebyshev-l1-l0-and-l2-l1-lowering-themes`
   - **Scope**: Author `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` (lowering the L1 fixed-degree polynomial action into L0 chebyshev-smoother calls + coefficient-computation patterns) and `book/src/L2-L1/chebyshev-iteration-fusion.md` (lowering the L2 explicit three-term recurrence back into the L1 closed-form polynomial action, showing the fusion).
   - **Rationale**: Unblocked by cycle-012 chebyshev L1+L2 firm landings; completes the lower-layer theme coverage for chebyshev.
   - **Dependencies**: dispatch #3 (L3/L4 chebyshev rows should land first to ground the lowering themes)
   - **Notes**: The fusion direction (L2>L1) is the rewrite direction per the high→low invariant. The L1>L0 mutation-rotation follows the same pattern as dispatch #6 orthogonalize.

8. **lifter** — `krylov-step-theme-body-no-l3-row-drift-cycle-013`
   - **Scope**: Re-anchor theme-body lines 20 + 220 in `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`, striking the stale cycle-006 "no L3 row needed" verdict (superseded by the cycle-009 meta-phase identity-lowerings invariant + the cycle-010 firm `L3/krylov-step.md` backfill). The cycle-012 lifter cleaned the L4/index.md:40 cross-reference; these theme-body residuals remain.
   - **Rationale**: Low-priority carry-forward from cycle-012 integrator-signals (signal #8); small, mechanical cleanup.
   - **Dependencies**: dispatch #3 (the L3/chebyshev harvest proves the identity-lowerings invariant is in force)
   - **Notes**: Single-edit, short dispatch. Mechanical text update; no new OQs expected.

9. **layer-intro-author** — `L0-bundle-6-candidates-discovery-and-ranking`
   - **Scope**: **Discovery dispatch**: search the Palace source tree for additional L0 reference-note candidates (chapters in the style of bundle-1–5 and the landing bundle-6 #1). Focus on solver-infrastructure files that haven't yet been chunked into layer intros (e.g., preconditioner base classes, eigensolver wrappers, multigrid scaffolding). Emit proposed-changes blocks for promising candidates (#2 + #3 per the OQ); if additional candidates surface, propose them for future scheduling.
   - **Rationale**: Priority carry-forward; cycle-009 OQ `l0-bundle-6-candidates`; #1 landed cycle-011; #2 + #3 still open. Cycle-012 integrator-signals surface additional unblocked candidates for discovery.
   - **Dependencies**: none (independent)
   - **Notes**: This is a scoping / discovery dispatch, not a full authorship. The goal is to surface candidates and prioritize them for a future cycle-013+ slot or cycle-014.

10. **lifter** — `slepc-convergence-reason-lift-sub-theme`
    - **Scope**: Author a sub-theme detailing the full SLEPc `EPSConvergedReason` → `EigStatus` mapping table, including diverged-reason cases (`EPS_DIVERGED_BREAKDOWN` / `EPS_DIVERGED_SYMMETRY_LOST` → `LinearSolveFailed`). Relate to the firm `eigsolve-mutation-rotation` parent theme + cycle-011 `eigsolve-iteration-count-result-field` landing.
    - **Rationale**: Carry-forward from cycle-011 integrator-signals (strongly unblocked); cycle-012 integrator-signals re-surface it as unblocked by the SLEPc-NEP audit. Completes the status-field coverage for eigensolvers.
    - **Dependencies**: dispatch #1 (the GATED eigsolve promotion should land first to ensure the parent theme is fully firm)
    - **Notes**: This is a sub-theme within the eigsolve lowering family, not a top-level new theme. Medium-scope dispatch.

11. **same-layer-cross-cutter** — `concepts-orthogonalization-coefficient-normalisation-drift`
    - **Scope**: Audit `book/src/concepts/orthogonalization.md` for stale pre-layered-era framing and coordinate-convention drift (the concept page likely predates the cycle-012 orthogonalize firm L1 harvest and may reference normalised vs non-normalised variants). Emit proposed corrections aligning with the L1 entry's "does not normalize output" contract.
    - **Rationale**: Carry-forward from cycle-012 report #1 (harvester orthogonalize) follow-up agent note. Small, surgical audit. Part of the "concepts-sweep" pattern (analogous to cycle-004 dot.md rewrite).
    - **Dependencies**: none (independent)
    - **Notes**: This is a pre-emptive alignment dispatch, not a blocking issue. Can be small or merged into another cycle's concept sweep if it's minimal.

## Overlap analysis

**Wave 1 (6 parallel dispatches):**

- **Dispatches 1–2 (abstractor eigsolve + harvester divfree)**: No overlap. Different layers (L1-L0 vs L1 firm); different slices (eigsolve mutation-rotation vs divfree projector).
- **Dispatch 3 (harvester chebyshev L3/L4)**: No overlap with 1–2. Independent L3/L4 entries. May use the chebyshev-iteration L2 firm landing from cycle-012, but doesn't write to it.
- **Dispatch 4 (layer-intro-author concept-page repointing)**: No overlap. Three concept-page edits. Does NOT touch `book/src/spec/slices/` directly (only re-points references).
- **Dispatch 5 (same-layer-cross-cutter batch-4)**: No overlap. Reads two slices (cg_preconditioning_framework + sparse_triangular_solve); does NOT write to them yet (audit only). Proposed-changes blocks emit verdicts; integrator decides reduction scope.
- **Dispatch 6 (abstractor orthogonalize mutation-rotation)**: No overlap with 1–5. New L1>L0 theme file.

**Between wave 1 and wave 2:**

- **Dispatch 7 (abstractor chebyshev lowering themes)** depends on dispatch 3 (L3/L4 chebyshev rows), so sequencing is correct.
- **Dispatch 8 (lifter theme-body re-anchor)** depends on dispatch 3 conceptually (the identity-lowerings invariant), but can actually land in parallel with 7; marked sequential for clarity.
- **Dispatch 9 (layer-intro-author L0-bundle discovery)** is independent; parallel to all wave-2 mates.
- **Dispatch 10 (lifter slepc-convergence sub-theme)** depends on dispatch 1 (GATED eigsolve promotion landing), so sequencing is correct.
- **Dispatch 11 (same-layer-cross-cutter concept-audit)** depends on dispatch 6 (orthogonalize harvest) conceptually, but can run in parallel; marked parallel.

**Cross-wave no-conflicts summary:**
- L1 index touched by dispatches 2 (divfree firm append) and 3 (chebyshev already landed cycle-012, so no new append here) — divfree appends after chebyshev is already there.
- L1-L0 index touched by dispatches 6 + 7 (orthogonalize + chebyshev lowering themes; two distinct rows; append cleanly).
- L4-L3 index touched by dispatch 3 (chebyshev landing) + dispatch 8 (lifter theme-body re-anchor) — same file, but dispatch 8 is a theme-body correction, not an index row append.
- Concept pages touched by dispatch 4 (three repoints) + dispatch 11 (orthogonalization audit) — orthogonalization is a different page; no collision.

**No genuine overlaps.**

## Sequencing schedule

**Wave 1 (6 parallel, 1st)**: Dispatches 1, 2, 3, 4, 5, 6 — fire in parallel.
- Expected completion: all 6 reports ready within one cycle phase.

**Wave 2 (5 parallel, 2nd)**: Dispatches 7, 8, 9, 10, 11 — fire in parallel after wave-1 reports integrate.
- Sequencing justification:
  - Dispatch 1 (eigsolve abstractor) must complete before dispatch 10 (slepc-convergence sub-theme) to ensure the parent theme is firm.
  - Dispatch 3 (chebyshev L3/L4) should complete before dispatch 7 (chebyshev lowering themes) for consistency.
  - Dispatch 6 (orthogonalize mutation-rotation) should complete before dispatch 11 (orthogonalization concept audit) for coordinated scope.
  - Dispatches 8 + 9 are independent and can fire with wave-2 mates.

**Total cycles projected**: 2 phase-2 cycles (wave-1 + wave-2) — realistic for 11 dispatches under the split-integrator design.

## Open questions / caveats

1. **L0-bundle-6 candidates #2 + #3 remain unscoped.** Dispatch 9 is a discovery phase to surface and prioritize them; the actual authorship may defer to cycle-014 depending on the discovered scope.

2. **cg_preconditioning_framework reduction verdict is speculative.** Dispatch 5's audit will determine whether the slice is substantially absorbed by L1/L2/L4 entries (expected) or whether significant uncovered content remains (unlikely). Verdict will feed into priority #5 completion and OQ routing.

3. **The partly-constructive promotion gate (dispatch 1) is the first cycle-013 test of the CLAUDE.md partly-constructive invariant.** If the gate-close edits apply cleanly but the theme's status-line caveat removal surfaces inconsistency or follow-up work, that will be valuable signal for the meta-phase batch-3.

4. **Orthogonalize concept-audit (dispatch 11) is speculative.** If the concepts/orthogonalization.md page is actually well-aligned with the L1 harvest, the dispatch will surface no issues and the OQ closes trivially. Conversely, if the page has stale normalisation assumptions, the repoint will be non-trivial.

5. **Codemap path verification:** This plan defers explicit Palace path verification to dispatch briefs. Dispatch #2 (divfree harvester), #3 (chebyshev L3/L4), and #6 (orthogonalize mutation-rotation) should cite Palace L0 paths explicitly; the codemap MCP was unavailable in planner context, so briefs should verify paths (e.g., chebyshev.hpp, orthog.hpp locations) before work starts.

---

**Dispatch plan summary**: 11 dispatches across 2 waves, addressing priorities #1–#7 with emphasis on the GATED eigsolve promotion (highest priority) + HEADLINE divfree + HEADLINE concept-page repointing + lower-layer vocabulary continuation + phase-1 corpus batch-4 closure. All dispatches are unblocked by cycle-012 landings. Expected to run in two phase-2 cycles under the split-integrator design. No genuine overlaps; sequencing respects gate dependencies.
