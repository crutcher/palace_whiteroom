---
agent: cycle-planner
invoked_at: 2026-05-27T18:50:00Z
scope: cycle-009 dispatch plan (final primary cycle of meta-batch-1 under 3:1 cadence)
status: pending
meta_batch: batch-1 (cycles 007/008/009; meta-phase fires after cycle-009 finalize, NOT after this cycle)
---

# Cycle 009 dispatch plan

## Goals selected this cycle

**Cycle-009 is the final primary cycle of meta-batch-1 before meta-phase aggregation fires.** The dispatch plan prioritizes:

1. **PRIORITY mechanical promotion of L3>L2 `krylov-step-body-identity` status** (1–2 dispatch slots) — cycle-008 lifted upstream L4>L3 `krylov-step-typed-wrapper-dissolution` to firm; the downstream L3>L2 theme's `firm-rough-in` status is now auto-eligible for mechanical promotion to plain `firm` via status-inheritance. Smallest-cost cycle-009 dispatch; validates the cross-edge status-promotion convention.

2. **L0 bootstrap bundle 5** (1 dispatch, light scope) — cycle-008 opened OQ `l0-bundle-5-candidates` enumerating 3 remaining candidates (`mpi-globalsum-and-collectives`, `tests-as-semantic-supplement`, `preconditioner-classes-overview`). Verify which are truly unlanded; if only 1–2 remain, bundle small rather than large.

3. **L1 rough-ins or forward-frontier work** (2–3 dispatch slots if cycles remain) — cycle-008 unblocked `eigsolve` L1 rough-in (test-coverage gated); matrix-weighted-norm / bilinear-form L1 rough-ins (lower priority, extends BLAS cohort for AMS/curl-curl); or continuation of existing open-frontier work.

4. **Write-authority discipline hardening** — every dispatch prompt must include explicit "proposed-changes-only channel; do NOT directly edit `book/`" warning. If cycle-009 sees a second write-authority violation (pattern repeat from cycle-008 pass-4), the cycle-009 meta-phase will enact a role-spec wording-prominence boost at `.claude/agents/abstractor.md:23`.

## Dispatches

1. **lifter** (or **integrator-per-report** mechanical-inheritance update) — `book/src/L3-L2/krylov-step-body-identity.md` status promotion
   - **Scope**: promote `firm-rough-in` → `firm` via status-inheritance now that upstream L4>L3 `krylov-step-typed-wrapper-dissolution` is firm (landed cycle-008 wave-1)
   - **Deps**: none (depends on cycle-008 finalize artifacts now on disk)
   - **Rationale**: cycle-008 integrator-signals identified this as a cycle-009 mechanical follow-up. Single `Status:` cell edit + inheritance-note paragraph. Smallest-cost dispatch; validates the cross-edge status-inheritance convention. If `integrator-per-report` is used, only frontmatter Status + brief paragraph edit needed; if `lifter` is used, allows for any additional substantive refinement if discovered, though none is expected.
   - **Write-authority discipline warning**: STRICTLY proposed-changes channel. Do NOT directly edit `book/`. All changes must flow through CYCLE.md `proposed_changes:` blocks.

2. **layer-intro-author** — L0 bootstrap bundle 5 (small scope)
   - **Scope**: author 1–2 remaining L0 reference-note chapters from cycle-008 OQ `l0-bundle-5-candidates` (candidates: `mpi-globalsum-and-collectives`, `tests-as-semantic-supplement`, `preconditioner-classes-overview`)
   - **Deps**: none (all L0 source anchors firm from prior cycles)
   - **Rationale**: cycle-008 L0 bundle 4 landed 3 chapters (14 total); bundle 5 completes priority #10 on a lighter scope if only 1–2 candidates remain unlanded. Pre-check `book/src/L0/index.md` to verify which are truly pending before authoring.
   - **Write-authority discipline warning**: STRICTLY proposed-changes channel. Do NOT directly edit `book/`. All changes must flow through CYCLE.md `proposed_changes:` blocks.

3. **harvester** — `eigsolve` L1 rough-in
   - **Scope**: author `book/src/L1/eigsolve.md` (eigenmode-solver analog of cycle-007 `ksp_solve`)
   - **Deps**: dispatch #2 (L0 bundle 5) preferred-before, to ensure `eigensolver-wrapper.md` anchor exists; however, the anchor was firmed cycle-008, so dispatch #3 can run in parallel with #2
   - **Rationale**: cycle-008 OQ `eigsolve-l1-operator-rough-in-candidate` unblocked by L0 bundle 4 landing `eigensolver-wrapper.md` anchor. Test-coverage constraint flagged: pre-check `reference/palace/test/unit/` for eigensolver tests (`eps_*` pattern) before deciding firm vs rough-in. If test coverage is sparse, rough-in only with OQ routing for test-coverage future coverage.
   - **Write-authority discipline warning**: STRICTLY proposed-changes channel. Do NOT directly edit `book/`. All changes must flow through CYCLE.md `proposed_changes:` blocks. Proposed-changes must be anchored to `book/src/L1/index.md` dep-map row append, not inline file creates.

4. **harvester** (optional, if cycle capacity allows) — matrix-weighted-norm / bilinear-form L1 rough-ins
   - **Scope**: author rough-in L1 entries for `nrm2_weighted :: (x, B) → √(xᴴ B x)`, `dot_bilinear :: (x, M, y) → xᴴ M y`, `power_iterate :: (A, x_init) → λ_dom`
   - **Deps**: dispatch #3 (eigsolve harvester) or #2 (L0 bundle 5), preferred-before, to establish pattern consistency on the new BLAS-1-like cohort extension
   - **Rationale**: cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` extends BLAS-1-like cohort with bilinear-form-aware analogs needed by AMS / curl-curl projector / multigrid level recurrences. Lower priority than `eigsolve` (less direct test coverage); rough-in only. Bundleable into one dispatch if scope allows.
   - **Write-authority discipline warning**: STRICTLY proposed-changes channel. Do NOT directly edit `book/`. All changes must flow through CYCLE.md `proposed_changes:` blocks.

5. **combinator-miner** (optional, if cycle capacity allows) — `check_stop_into_carry` helper-promotion decision
   - **Scope**: review `gmres-inner-loop-iterate-while-migration.md` §Status caveat (b) promotion criterion: "defer until a second slice needs it." Scan downstream GMRES-family slices (FGMRES, IRBL, IDR(s)) for reuse.
   - **Deps**: none (inspection-only on existing slices)
   - **Rationale**: cycle-008 rough-in L4>L3 theme flagged this as a defer-until-second-reuse decision. Low-cost observation; routes to cycle-009+ lifter if reuse is found, or defer if not.
   - **Write-authority discipline warning**: STRICTLY proposed-changes channel. Do NOT directly edit `book/`. All changes must flow through CYCLE.md `proposed_changes:` blocks.

## Overlap analysis

- **Dispatches #1 (L3>L2 promotion) + #2 (L0 bundle 5)**: No overlap. Dispatch #1 edits `book/src/L3-L2/krylov-step-body-identity.md` only (Status cell); dispatch #2 authors new L0 chapters + edits `book/src/L0/index.md` + appends to SUMMARY.md. **PARALLEL**.

- **Dispatches #1 + #3 (eigsolve harvester)**: No overlap. Dispatch #1 touches L3>L2 layer only; dispatch #3 touches L1 layer + L1/index. **PARALLEL**.

- **Dispatches #1 + #4 (matrix-weighted-norm rough-ins)**: No overlap. Dispatch #1 touches L3>L2; dispatch #4 touches L1 + L1/index. **PARALLEL**.

- **Dispatches #2 (L0 bundle 5) + #3 (eigsolve harvester)**: Minor potential overlap on SUMMARY.md if both propose Chapter inserts. Dispatch #2 is light (1–2 L0 chapters); dispatch #3 is L1 chapter (separate Part). Per-report serial re-read discipline will handle cleanly. **PARALLEL** (prefer to mark PARALLEL per conflict-tolerance philosophy; integrator's surgical edit discipline is load-bearing at this scale).

- **Dispatches #2 (L0 bundle 5) + #4 (matrix-weighted-norm)**: No overlap. Different layers. **PARALLEL**.

- **Dispatches #3 (eigsolve) + #4 (matrix-weighted-norm)**: Both may append to `book/src/L1/index.md` dep-map table. If both dispatches are in cycle, mark **SEQUENTIAL** (dispatch #3 then #4; eigsolve is higher-priority per OQ age and test-coverage clarity). Alternatively, if capacity is tight, defer #4 to cycle-010. Recommend **SEQUENTIAL** if both run; otherwise **defer #4**.

- **Dispatch #5 (combinator-miner, optional)**: Inspection-only; no artifact edits unless findings route to a follow-up lifter. No overlap with other dispatches. **PARALLEL** if included.

## Sequencing schedule

**Wave 1 (parallel)**: dispatches #1, #2, #3, #5 (if included)

**Wave 2 (after wave 1)**: dispatch #4 (if included) — depends on dispatch #3 finishing to establish L1 cohort pattern consistency

**Wave structure**: 4–5 dispatches total; 4 in parallel wave-1, optionally 1 sequential wave-2. Aim for 4–5 total to stay under the 12-dispatch cap and leave headroom for meta-phase aggregation. Conservative default: **run dispatches #1–#3 + #5 in wave 1; defer #4 unless capacity confirmed**.

## Open questions / caveats

1. **Dispatch #1 implementation choice**: The cycle-008 signals suggested either `lifter` or `integrator-per-report` for the L3>L2 status promotion. The `integrator-per-report` path (mechanical inheritance update) is lower-cost (no full subagent session, just a frontmatter edit). However, using `lifter` allows for discovery of any additional refinement opportunities and aligns with the broader lifter-role pattern for status promotions. Recommend **`lifter`** for consistency; if context budget is tight, **`integrator-per-report`** (mechanical) is acceptable.

2. **L0 bundle 5 scope verification**: Before dispatch #2 runs, pre-check `book/src/L0/index.md` dep-map to verify which of `mpi-globalsum-and-collectives`, `tests-as-semantic-supplement`, `preconditioner-classes-overview` are truly unlanded. If all 3 exist, bundle is empty and dispatch should be skipped. If 1–2 exist, scope is light; if all 3 are unlanded, scope is normal. OQ text suggests only 1–2 remain.

3. **Eigsolve test-coverage pre-check**: Dispatch #3 harvester should pre-check `reference/palace/test/unit/` for eigensolver test coverage (grep `eps_*` pattern and `eigenmode`-related tests) before deciding whether to author as `firm` or `rough-in`. The cycle-008 signal flagged test-coverage constraint; the decision should be grounded in actual test evidence, not speculative.

4. **Write-authority violation pattern contingency**: If cycle-009 dispatch #3 or #4 (harvester agents) repeats the cycle-008 write-authority violation (direct `book/` writes during dispatch, not proposed-changes), **stop immediately, revert, and surface to human**. This would be recurrence-2 of the pattern; per cycle-008 integrator-signals and friction-ledger, meta-phase would then enact a role-spec wording-prominence boost. Do NOT silently repair a second instance; escalate.

5. **Cycle-009 → meta-phase transition**: After cycle-009 integrator-finalize commits + pushes, meta-phase fires (not after this planner dispatch). Meta-phase will aggregate evidence across all 3 cycles of batch-1 (cycles 007/008/009) and address the critical OQ `abstractor-write-authority-violation-cycle-008` (and any new violations). `/compact` fires after meta-phase finalize.

6. **Defer-to-cycle-010 candidates** (in priority order if cycle-009 capacity is exhausted): `gmres.md §L4 v0.6 → v0.7 self-rotation` (abstractor or lifter, large), open-questions.md section-drift cleanup (same-layer-cross-cutter, meta-phase), dep-map `Lowers to` column back-application to L1/L2/L3 (layer-intro-author, meta-phase).

