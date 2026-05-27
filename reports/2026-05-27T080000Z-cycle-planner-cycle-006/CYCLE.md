---
agent: cycle-planner
invoked_at: 2026-05-27T08:00:00Z
scope: cycle-006 dispatch plan
status: pending
---

# Cycle-006 dispatch plan

## Goals selected this cycle

Cycle-005 landed `krylov-step` firm at L2 and recommended L4 dual-placement with lowering edges (L4 > L3 > L2). The cross-cutter identified this as a high-priority forward-frontier work. Simultaneously, L0 bootstrap (priority #10) is a multi-cycle buildout, and scalar-promotion retroactive L1 thinning (cycle-005 unblocked) offers a concrete small-scope cleanup opportunity. This cycle targets the `krylov-step` L4 stack + continuing the L0 bootstrap + the scalar-promotion thinning, while maintaining capacity for cross-cutting methodological observations.

## Dispatches

1. **harvester** — `krylov-step @ L4` (primary, unblocked by cross-cutter cycle-005 recommendation)
   - Scope: formalize L4 krylov-step with state-stratification / solve-monad framing; 6 variant axes absorbed at construction; algebraic-laws section; "Lowers to" edge stub pointing to L4>L3 abstractor dispatch; no Palace L0 citation (methodology-level concept).
   - Dependencies: none (cycle-005 L2 firm landing is prior context, not a blocking dep)
   - Rationale: cross-cutter explicitly routed; L2 `krylov-step` firm last cycle means the L4 canonical form can now be anchored. Unblocks L4>L3 abstractor and L4 dep-map refresh.

2. **abstractor** — `L4>L3 lowering theme for krylov-step (state-stratification to value-threading or equiv.)` (secondary, can parallel wave-1)
   - Scope: the lowering from L4 state-threaded wrapper to L3 value-threaded body (or identity-in-form if combinator-miner's assertion holds). Per cross-cutter open question `krylov-step-l3-identity-in-form-audit`, if the rotation is non-identity, promote an L3 krylov-step entry as well.
   - Dependencies: (1) — awaits L4 harvester signature to anchor the lowering
   - Rationale: secondary follow-up from cross-cutter recommendation; characterizes the L4>L2 rotation chain. Can run in parallel if L4 harvester is early (wave-1 dispatch completes fast enough).

3. **layer-intro-author** — `L0 reference-bootstrap bundle 2` (priority #10 continuation)
   - Scope: 4-6 new L0 reference chapters. Candidates per priority #10 backlog: `apply_linop` overload-set / preconditioner-application summary page; `kspsolver-base-class` solver-interface page; possibly 2-3 more file-overview pages (e.g., `operator-file.md`, `solver-cpp.md`). Parallel to dispatch (1) or (2).
   - Dependencies: none (continuation of cycle-005 bundle 1, self-contained)
   - Rationale: priority #10 is multi-cycle; bundle 2 advances the L0 overlay. Enables future cycle's retroactive-L1-context-thinning (priority #11 requires ≥6 chapters per priority spec).

4. **same-layer-cross-cutter** — `concepts/index.md duplicate-rows housekeeping` (small surgical fix)
   - Scope: remove duplicate rows in `book/src/concepts/index.md`: `complex-from-real-lift` (lines 70-71), `solver-as-operator` (lines 98-99). Per cycle-005 integrator-signals §Integration-tooling friction, these pre-existing rows block any future concept-page append and clutter the index.
   - Dependencies: none (pure housekeeping)
   - Rationale: pre-flagged by cycle-005 integrator; low-cost fix to unblock future concept work. Can pair with dispatch (3) or run solo.

5. **layer-intro-author** — `scalar-promotion retroactive L1 thinning` (unblocked by cycle-005, small scope)
   - Scope: replace per-operator scalar-promotion prose in `book/src/L1/axpy.md`, `book/src/L1/axpby.md`, `book/src/L1/axpbypcz.md`, `book/src/L1/scal.md` with one-line concept backlinks (keeping evidence citation in place). Update variant-axes bullets to backlinks instead of full restatements. Estimated ~600 words savings across four entries per cycle-005 estimate.
   - Dependencies: none (cycle-005 concept page already landed)
   - Rationale: unblocked by cycle-005; straightforward cleanup enabled by the new concept page. Bundles cleanly with the L0 bootstrap or runs solo in wave-2.

## Overlap analysis

**Dispatch (1) vs (2):** Sequential by dependency — (2) awaits (1)'s L4 signature. However, the two can **run in parallel if L4 harvester is fast**: if harvester completes cycle-start + early and posts its signature to its CYCLE.md early, abstractor can begin reading and drafting while (1) is still finishing its algebraic laws. Mark **SEQUENTIAL** as designed (dependency enforced), but flag as **LOW-CONFLICT parallel candidate** if cycle-planner wants to risk overlap.

**Dispatch (1) vs (3) vs (4) vs (5):** Non-overlapping. (1) creates L4/krylov-step.md; (3) appends L0 chapters; (4) edits concepts/index.md; (5) edits existing L1 entries. No shared files, no shared operator names. Mark **PARALLEL**.

**Dispatch (2) vs (3) vs (4) vs (5):** Sequential to (1) in design, but non-overlapping with (3/4/5). If (2) is deferred to wave-2, it runs cleanly in parallel with the L0/concepts/L1 work. Mark **PARALLEL among 3,4,5** and **SEQUENTIAL (2) after (1)**.

**Dispatch (3) vs (4) vs (5):** Fully parallel. No shared files or edit targets.

## Sequencing schedule

**Wave 1 (parallel):**
- (1) harvester — krylov-step @ L4
- (3) layer-intro-author — L0 bootstrap bundle 2
- (4) same-layer-cross-cutter — concepts/index.md duplicate-rows
- (5) layer-intro-author — scalar-promotion retroactive L1 thinning

**Wave 2 (parallel, after wave-1 reports land):**
- (2) abstractor — L4>L3 lowering theme for krylov-step (reads wave-1 dispatch (1)'s signature)

**Rationale:** Dispatch (2) is the only true sequential dependency; all others are independent. Running (1,3,4,5) in wave-1 maximizes parallelism. (2) in wave-2 ensures it has the L4 signature to anchor on and avoids the risk of (2) drafting against a provisional signature that changes.

## Open questions / caveats

1. **L4 vocab pre-staging question** (from cycle-005 cross-cutter open question `state-stratification-as-l4-concept-or-l4-row`): Should `state-stratification`, `iterate_while`, and `solve-monad` be harvested as L4 firm entries **before** or **alongside** the `krylov-step @ L4` dispatch? The cross-cutter noted that if krylov-step becomes the first L4 dep-map entry, the L4 layer intro may also need these concepts promoted to L4 rows simultaneously so that `krylov-step` has firm L4 vocabulary to depend on. Current dispatch (1) assumes these can live as concepts (already exist in `book/src/concepts/`) and the krylov-step entry links to them. If integration reveals that L4 rows should depend on L4 rows (not concepts), a follow-up cycle may promote these three to firm L4 entries. **For cycle-006: proceed with dispatch (1) as-is; if repairer flags the vocab-dependency issue, defer L4 dep-map refresh (potential dispatch (1b)) to cycle-007.** Decision belongs to (1)'s harvester and repairer.

2. **L3 krylov-step promotion contingency** (from cycle-005 cross-cutter open question `krylov-step-l3-identity-in-form-audit`): The combinator-miner (cycle-002) asserted that L4>L3 rotation on the krylov-step body is identity-in-form. Dispatch (2) will audit this. If the rotation is non-identity (e.g., the `Krylov` ephemeral bundle dissolves on the way to L3), dispatch (2) should propose a **follow-up cycle-007 L3 entry**. If identity, no L3 entry needed. **Noted for (2) so it surfaces the result for cycle-007 planner input.**

3. **L0 bootstrap bundle 2 scope** (prioritizing among candidates): Dispatch (3) has several options per priority #10 backlog. The cycle-005 integrator suggested: `apply_linop` overload-set page (medium scope; supports L1>L0 lowering audits), `kspsolver-base-class` page (medium), additional file-overview pages (high breadth, high count). **Recommendation for (3): prioritize `apply_linop` and `kspsolver-base-class` (two medium-scope chapters) to maintain momentum and unblock future L1>L0 audits. Defer the broad file-overview sweep to a future cycle if time permits.** Repairer can adjust scope if needed.

4. **Mixing of two `layer-intro-author` roles in one wave** (dispatches 3 and 5): Both are layer-intro-author, both non-blocking independently. The role can handle multiple dispatches; no coordination friction anticipated. If token budget becomes tight under wave-1 size, (5) can defer to cycle-007 with low cost (it's a cleanup operation, not forward-frontier).

5. **concepts/index.md vs problem filing** (dispatch 4): The duplicate rows are housekeeping and have low friction to fix. Cycle-planner is marking this as a dispatch-scope task rather than a problems/ filing (per the relaxed bar, drive-by observations are filings; the duplicates are noted and fixable at zero cost). If integration reveals scope creep (e.g., duplicate-row fix cascades into broader concepts-index restructuring), repairer can downgrade and file as a problems/ item for future meta-phase triage.

## Dispatch count and sizing

**Total dispatches: 5** (well under the 8-dispatch cap per user directive 2026-05-27).

**Wave-1: 4 dispatches** (same count as cycle-005's 6 total under split integrator: cycle-004 ran 7 in one wave; cycle-005 ran 6 across serial per-report; cycle-006 targets 4+1 = 5 total, with 4 in wave-1 for reasonable integrator-per-report load). Per-report integrator context budget at 4-dispatch wave-size is well-proven (cycle-005); adding a 5th in wave-2 is conservative and safe.

**Confidence in wave-1 parallelism:** High. Dispatches (3,4,5) are fully independent; (1) is primary and needs no wave-mate input. No file conflicts, no edit races.

**Confidence in wave-2 ordering:** High. (2) is only true dependency; can safely read (1)'s CYCLE.md for the signature.
