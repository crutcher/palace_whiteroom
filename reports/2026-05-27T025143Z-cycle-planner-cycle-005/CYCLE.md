---
agent: cycle-planner
invoked_at: 2026-05-27T025143Z
scope: cycle-005 dispatch plan
status: pending
---

# Cycle 005 dispatch plan

## Goals selected this cycle

L0 reference-notes layer bootstrap + L1 operator harvest unblock + L1>L0 lowering-theme substantial work. Priorities #1, #10, #2, #3 constitute the forward-frontier: krylov-step is L2-ready (all L1 deps firm); L0 layer is priority-flagged and major infrastructure gap; apply-linop and axpbypcz lowering themes are unblocked and constitute major scope expansion from pilot-1's axpby-only baseline. Cycle-004 cleared the integrator-per-report machinery; cycle-005 validates it scales to high-parallelism dispatch (up to 8 dispatches, same-file row-level non-overlapping per friction-ledger updated philosophy).

## Dispatches

1. **harvester-krylov-step-L2** — Promote cycle-002 combinator-miner rough-in to firm L2 operator. Scope: 6 deliverables per open question `krylov-step-harvester-deliverables` (apply-linop/axpy/dot/nrm2 deps now firm; deliver krylov-step laws + variant axes + L1>L2 forms). Routes to `harvester`. Deps: none. Rationale: highest-value L2 forward work; unblocked cycle-004; krylov-step is the anchor for shared-infrastructure layer-placement decision (#5).

2. **abstractor-apply-linop-mutation-rotation-L1-L0** — Write L1>L0 lowering theme for `apply_linop` (representation-axis + transpose-mode + accumulate-mode + parallel-wrapper). Substantially larger than axpby-mutation-rotation. Routes to `abstractor`. Deps: none (parallel). Rationale: integrator-signals cycle-004 flags as top unblocked work; cycle-004 harvester's open question `apply-linop-lowering-theme-scope` signals large scope; lowers integration risk by bundling scope with explicit variant caveats.

3. **abstractor-axpbypcz-mutation-rotation-L1-L0** — Write L1>L0 lowering theme for `axpbypcz` (first theme to mix structural-rebind with algebraic-constant-folding, the γ==0 sub-rule). Routes to `abstractor`. Deps: none (parallel to #2). Rationale: integrator-signals cycle-004 lists as unblocked; companion to #2; closes open question `axpbypcz-mutation-rotation-abstractor-target`.

4. **layer-intro-author-L0-reference-bootstrap-bundle-1** — Populate first cohort of L0 reference-notes layer chapters. Scope: ~6 chapters from priority #10 (Conventions + File overviews + Tests note; planner bundles them under one invocation to manage integration row-count). Routes to `layer-intro-author`. Deps: none (distinct from L1 edits). Rationale: priority #10 user-directive (2026-05-27); L0 is 30-line stub; reference-notes infrastructure clears retroactive-L1-context-thinning path (priority #11); bundling chapters reduces integration overhead.

5. **cross-layer-cross-cutter-krylov-step-layer-placement** — Decide L2 vs L4 vs both for `krylov-step` per open question `krylov-step-layer-placement`. Co-informed by #1's L2 firm-up (reads #1's proposed-changes but not integrated artifact yet per integrator-per-report model). Routes to `cross-layer-cross-cutter`. Deps: #1 (marked for co-coherent dispatch, but runs in parallel with understanding that reads in-flight CYCLE.md). Rationale: integrator-signals cycle-004 lists as co-bundled scope; policy decision (L2 only vs L4 too) gates downstream krylov-consumer coverage (MINRES/BiCGStab upgrade decision, etc.).

6. **same-layer-cross-cutter-concepts-sweep-bundle-1** — Replay cycle-004 concepts/dot rewrite pattern over remaining concepts pages. Scope: ~4–5 concept pages (axpy, nrm2, orthogonalization, scal, others per planner triage). Routes to `same-layer-cross-cutter`. Deps: none (concepts distinct from L0/L1/L2). Rationale: priority #8; cycle-004 dot-rewrite establishes template; sweep unblocked; cycle-003 open question `concepts-pre-layered-era-sweep` bundled with cycle-004 `concepts-sweep-cycle-005-candidate`.

7. **layer-intro-author-scalar-promotion-typing-rule-lift** — Author `book/src/concepts/scalar-promotion.md` (pulling the rule that now appears in 5 operators: axpy, dot, axpby, axpbypcz, scal). Routes to `layer-intro-author`. Deps: none (concepts work distinct). Rationale: priority #9; integrator cycle-004 signals well-past-threshold for promotion (recurrence-5 per-operator); concept-page extraction consolidates vocabulary.

8. **combinator-miner-L2-intermediate-tier-search** — Scan L1 vocabulary (7 firm operators + apply_linop's three-axis disclosure) for intermediate-tier recurrent patterns (e.g., "normalize via nrm2+dot+scal", "project via dot+apply_linop chaining"). Rough-in one L2 combinator candidate per roadmap Intermediate-tier section rationale. Routes to `combinator-miner`. Deps: none. Rationale: L1 vocabulary now substantially populated; roadmap §Intermediate-tier flagged intermediate-pattern mining as "bang-for-buck" forward work; one small rough-in combinator unblocks downstream (CG preconditioner, eigenmode restarts, etc.). Speculative; low-integration-friction.

## Overlap analysis

**Dispatch parallelism within waves:**

- **Dispatches 1 & 5 (krylov-step harvest + layer-placement cross-cut):** #5 reads #1's proposed-changes for krylov-step substance but integrator-per-report model means disk-fresh on each; marking PARALLEL per integrator-signals cycle-004 philosophy. #5 writes its own CYCLE.md, no artifact mutation, zero file contention.
- **Dispatches 2 & 3 (apply-linop + axpbypcz L1>L0):** Distinct L1>L0 themes; L1-L0/index.md append-after anchors (both append new theme rows); row-anchors differ; no file-region overlap. Cycle-004 §Wave-conflict observations validated this scales to 2+ theme appends. Mark PARALLEL.
- **Dispatch 4 (L0 reference bootstrap):** Creates new `book/src/L0/<chapters>`, distinct files. L0/index.md row-appends for new chapter links (distinct anchors from L1/L2/L3/L4 intros). Zero conflict with any other dispatch. PARALLEL.
- **Dispatches 6 & 7 (concepts sweep + scalar-promotion lift):** Both edit `book/src/concepts/` but to distinct pages (sweep hits multiple concept/*.md files; scalar-promotion creates new `scalar-promotion.md`). No single-file multi-writer scenario. PARALLEL.
- **Dispatch 8 (combinator-miner):** Writes `book/src/L2/index.md` rough-in row(s). Dispatch #1 (harvester-krylov-step) also writes L2/index.md (the firm krylov-step row + dep updates). **These OVERLAP** — both touch the L2 dep-map. Sequencing: #1 lands first (firm row appended), then #8 runs (reads the post-#1 artifact to avoid stale anchors for its rough-in combinator proposal).

**Summary of conflicts:** Only dispatches #1 and #8 have file-region overlap (both write L2/index.md rows). Sequencing: wave-1 is #1–#7 (parallel); wave-2 is #8 (after #1 integrates and disk reflects the firm krylov-step row).

## Sequencing schedule

**Wave 1 (parallel, all start immediately after plan approval):**
1. harvester-krylov-step-L2
2. abstractor-apply-linop-mutation-rotation-L1-L0
3. abstractor-axpbypcz-mutation-rotation-L1-L0
4. layer-intro-author-L0-reference-bootstrap-bundle-1
5. cross-layer-cross-cutter-krylov-step-layer-placement
6. same-layer-cross-cutter-concepts-sweep-bundle-1
7. layer-intro-author-scalar-promotion-typing-rule-lift

**Wave 2 (after wave-1 landing + #1 integrator-per-report commit; one dispatch):**
8. combinator-miner-L2-intermediate-tier-search

**Total dispatch count: 8 (hitting the user-directed up-to-8 target; validates the wave model at scale).**

## Open questions / caveats

1. **Integrator-per-report model — first cycle run.** This is cycle-005's first invocation under the new split (integrator-per-report serial applies + integrator-finalize once at cycle-end housekeeping). Wave-1 dispatches will see per-report integration after each CYCLE.md lands (disk-fresh read). Dispatch #5 (cross-layer-cross-cutter) may read #1's in-flight CYCLE.md if #1 is slow; this is acceptable per the model's design but worth monitoring for staleness. Flag to human: if cross-cutter output on #5 references assumptions about #1's firm rows that diverge from actual integration (race condition on CYCLE.md read timing), this signals the integrator-per-report model needs tighter synchronization gates.

2. **Pre-grep for Householder QR and Jacobi smoother.** Priorities #6 and #7 are deferred one cycle (not in wave-1) per cycle-004 friction-ledger and user directive: both need `palace/utils/labels.hpp` + relevant solver-selection points grepped for stub status before reliable routing (harvester vs. abstractor). Cycle-006 planner should schedule the discovery grep first, or the human can pre-grep and surface findings before cycle-006 planning.

3. **L0 bootstrap bundle scope.** Dispatch #4 is marked "bundle-1" (~6 chapters) with the intent of leaving room for bundle-2 (remaining L0 chapters) in cycle-006 or later. The 13-chapter starter set in priority #10 is the target; bundling aggressively in one dispatch risks token overload on the layer-intro-author invocation. If the human prefers smaller bundles (3–4 chapters per dispatch), cycle-005 planner can split #4 into two sequential dispatches (both in wave-1, back-to-back) with distinct anchors on L0/index.md. Current plan assumes single large bundle.

4. **Combinator-miner scope / feasibility.** Dispatch #8 is speculative (one rough-in combinator per roadmap guidance); the actual surface of "recurrent patterns from 7 firm L1 operators + 3-axis apply_linop" is unknown. If the combinator-miner finds no clear candidates in a reasonable reading, it should surface this as an open question (`no-candidate-surface-at-L1-scale`) rather than force-inventing. Low-friction landing expected.

5. **Cross-layer-cross-cutter on obstruction themes.** Dispatch #5 will encounter cycle-004's MINRES and BiCGStab obstruction themes in L1-L0/index.md. The friction-ledger entry `advertised-but-unimplemented-krylov-solvers` and integrator-signals §Integration-tooling friction flag that obstruction-theme treatment is undefined. The user has not yet decided the `mfem-as-l0-substrate-policy` (ASK item from cycle-004 meta-phase). Dispatch #5 should document its approach (skip evidence-walking, surface as "anticipated work / policy-gated"?) in an open question / caveat section of its CYCLE.md. Meta-phase will formalize the treatment after this cycle.

6. **Cycle-005 dispatch count at 8 is the user-directed limit.** Cycles 003–004 ran 7 and 7 respectively under the user's up-to-8 target. This cycle uses all 8 (4 wave-1 parallel + 3 wave-1 parallel + 1 wave-2 sequential after bottleneck). If any dispatch over-scopes during execution, the integrator will surface via META.md during repair phase. Planner accepts this as designed risk (conflict-tolerance philosophy).
