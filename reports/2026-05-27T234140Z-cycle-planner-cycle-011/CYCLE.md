---
agent: cycle-planner
invoked_at: 2026-05-27T234140Z
scope: cycle-011 dispatch plan (second primary cycle of meta-batch-2)
status: pending
---

# Cycle-011 dispatch plan

## Goals selected this cycle

Cycle-011 capitalizes on cycle-010's unblockers: the krylov-step L3 foundation is complete; the slice-reduction template is proven; MCP codemap is operational. Three strategic goals drive the dispatch selection:

1. **L3 backfill wave** (priority #20 second target) — apply_linop + 6-entry BLAS-1 cohort (axpy, scal, dot, nrm2, axpby, axpbypcz). Cycle-010 wave-1 pass-2 audit surfaced HIGH CONFIDENCE recommendations for this cohort. Bundling by family (linear-update: axpy/axpby/axpbypcz; reduction: dot/nrm2; primitive: scal; plus apply_linop) yields 4 natural dispatch scopes. Delivers concrete progress on the identity-lowering-both-levels directive (priority #20).

2. **Phase-1 corpus reduction continuation** (priority #19) — audit + reduce next slice batch (orthog → chebyshev → polynomial_recurrence_step per cycle-010 priority routing). Demonstrated template is machine-replayable; cycle-011 executes one 2-3 slice batch to sustain momentum on corpus reduction.

3. **Close priority #13 and sequence FGMRES work** — cycle-010 wave-2 pass-5 routed the priority-13 close via OQ `priority-13-now-landed-as-matrix-weighted-norm`. Planner closes it (write-authority partition allows). Cycle-010 wave-2 pass-6 routed FGMRES lifter with explicit sequencing: lifter-before-harvester on the cycle-008 `gmres-inner-loop-iterate-while-migration` theme. Lifter re-anchors the theme against firm `gmres.md §L4 v0.7` vocabulary (ready post-cycle-010 cleanup; not size-blocked).

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|-------|-------|------|-----------|
| 1 | **harvester** | **L3 `apply_linop` backfill** (first of 4-dispatch BLAS-1 cohort bundle) | none | Priority #20 second target, HIGH CONFIDENCE cycle-010 audit recommendation. Single-operator L3 entry for `apply_linop` following krylov-step precedent (identity-lowering-both-levels pattern: L4/apply_linop firm cycle-004; L2/apply_linop firm cycle-005; now backfill L3 with L3-vocabulary entry). Candidate variant axes: representation-axis, transpose-mode, accumulate-mode (from L1>L0 theme scope cycle-002 open question). Uses MCP codemap to localize L3 vocabulary from L2/L4 entries if needed. ~100 lines estimated. |
| 2 | **harvester** | **L3 BLAS-1 linear-update cohort: axpy, axpby, axpbypcz** (second of 4-dispatch BLAS-1 cohort bundle; 3-operator batch) | #1 | Priority #20 second target; cycle-010 audit HIGH CONFIDENCE routing. Bundle-scope decision rationale: axpy/axpby/axpbypcz are three algebraic variants of the same operation family (α·x + β·y + [γ·z]); cycle-003 decision `axpby-as-primitive` established axpby as fused primitive; axpbypcz extends to three-term. Bundling avoids context-switching between similar operators. Identity-lowering-both-levels pattern for all three (firm L4/L2 forms exist; backfill L3). ~80 lines/operator estimated. Uses MCP. |
| 3 | **harvester** | **L3 BLAS-1 reduction cohort: dot, nrm2** (third of 4-dispatch BLAS-1 cohort bundle; 2-operator batch) | #1 | Priority #20 second target; cycle-010 audit HIGH CONFIDENCE routing. Bundle-scope: dot/nrm2 are the two fundamental inner-product-based reductions; L4/L2 forms exist (dot firm cycle-002 L1; nrm2 firm cycle-003 L1). Identity-lowering pattern for both. ~70 lines/operator estimated. Uses MCP. |
| 4 | **harvester** | **L3 BLAS-1 primitive: scal** (fourth of 4-dispatch BLAS-1 cohort bundle; 1-operator) | #1 | Priority #20 second target; cycle-010 audit HIGH CONFIDENCE routing. Final cohort operator: `y ← α·y` scalar multiply. Smallest scope of the bundle (likely ~60 lines; existing L4/L2 forms firm cycle-004). Identity-lowering pattern. Closes priority #20 second target upon landing all four dispatches. |
| 5 | **same-layer-cross-cutter** | **Phase-1 corpus reduction batch: orthog + chebyshev + polynomial_recurrence_step** | none | Priority #19 continuation. Cycle-010 first-instance audit established machine-replayable template (pass 8). Suggested batch-size 2-4 slices; targeting three slices per the OQ routing priority order. Audit + reduce trio following the cycle-010 pattern: verify content fully represented in firm layered entries, propose reduction to stub or removal, surface residual gaps. **Caveat 6** (per cycle-010 dispatch): line-range arithmetic brittleness friction at recurrence-1 — recommend use of `grep -n "^## "` enumeration to locate actual H2 boundaries before line operations. MCP `search_text` useful for locating section headers. |
| 6 | **lifter** | **FGMRES inner-loop iterate-while migration theme** — re-anchor cycle-008 `gmres-inner-loop-iterate-while-migration` L4>L3 theme for FGMRES parameterization | none | Cycle-010 wave-2 pass-6 routed with explicit **lifter-before-harvester sequencing directive** for cycle-011 planner. Prerequisite: re-anchor the existing cycle-008 rough-in theme against firm `gmres.md §L4 v0.7` vocabulary (ready post-cycle-010; the upstream gmres v0.6→v0.7 self-rotation is a large deferred dispatch per integrator-signals; v0.7 form is sufficient for re-anchoring the migration theme). Scope: parameterize the existing L4>L3 theme to cover both GMRES (orthogonal Krylov) and FGMRES (flexible Krylov) variants; the migration pattern differs in restarted outer-loop shape (FGMRES adapts the preconditioner; adds one extra iterate-while parameterization axis). New theme name: `fgmres-inner-loop-iterate-while-migration` (sibling to cycle-008's `gmres-inner-loop-iterate-while-migration`). ~150 lines estimated. Routes to cycle-011+ harvester on `book/src/L4/check_stop_into_carry.md` L4 helper promotion (deferred per cycle-009 "second slice" criterion; NLEPS remains unblocked-but-large). |
| 7 | **abstractor** | **Eigsolve mutation-rotation L1>L0 lowering theme** — materialize the `eigsolve-mutation-rotation` L1>L0 theme | none | Cycle-010 wave-2 pass-7 lifted `eigsolve.md` with `LinearSolveFailed` as L1-constructive (option (b)); the materialising L1>L0 theme is the natural follow-on. Sister-theme to `ksp-solve-mutation-rotation` (cycle-008). Scope: document how the L1 `eigsolve` form lowers into L0 Palace source, with explicit attention to: (a) the `LinearSolveFailed` case body (inner solver coupling refactor per cycle-009 OQ option (c) deferred reading); (b) mutation patterns for the `EigStatus` result-record fields (Converged, Diverged, MaxIt via inner and outer `krylov-step` / `check_stop_into_carry` interactions); (c) the spectral-transformation setup/teardown mechanics. Candidate sub-patterns: A=setup, B=inner-solve mutation-rotation, C=result-status flow, D=teardown (estimate ~400 lines following ksp-solve-mutation-rotation precedent). |
| 8 | **lifter** | **Remaining cycle-009 eigsolve OQs cluster: scaling-coordinate-convention + initial-space-axis-placement + iteration-count-result-field** | #7 | Three small cycle-009 OQs remain open after cycle-010 wave-2 pass-7's lifting of the `LinearSolveFailed` anchor. Per the wave-2 #7 dispatch notes, these are individually tractable as small lifter dispatches. Recommendation: execute as a **single unified lifter dispatch** scoped to all three OQs (rather than three separate dispatches), accepting one shared theme or multiple interlinked notes per OQ (e.g., a joint "Eigsolve L1 variant-axis & result-record inventory" theme covering all three axes in one write). **Dependency on #7**: the `eigsolve-mutation-rotation` theme landing may resolve or clarify some aspects of these OQs; coordinate scoping post-dispatch-7. Estimated ~200 lines total for the three OQs' resolution. |
| 9 | **layer-intro-author** | **L0 bootstrap bundle 6** (deferred from cycle-010; highest-priority candidate: linalg-solver-file) | none | Cycle-010 deferred due to capacity; cycle-009 OQ `l0-bundle-6-candidates` enumerates: `linalg-solver-file` (highest priority — file-level overview of `palace/linalg/solver.{hpp,cpp}`, closes file-overview gap on four `linalg/` anchor files), `tests-as-semantic-supplement` (pending placement decision per OQ `tests-as-semantic-supplement-l0-vs-concepts-decision`), `mutable-workspace-pattern` expansion if new variants surface. Recommend cycle-011 dispatch on `linalg-solver-file` (medium scope ~100 lines; unblocks roadmap §FE-assembly downstream reference anchors). |
| 10 | **cycle-planner** | **Close priority #13 routing OQ in scaffolding/priorities.md** | none | **No artifact mutation; priority-edit only.** Cycle-010 wave-2 pass-5 surfaced routing OQ `priority-13-now-landed-as-matrix-weighted-norm` (status `routing`). Per write-authority partition, cycle-planner authority allows closing this. Action: edit `scaffolding/priorities.md` §"Now (active)" priority #13 → remove the old priority-13 entry (nrm2_B-weighted-energy-norm-L1) and replace with clarifying note that `matrix-weighted-norm` is the canonical name. (Exact edit shown in Open questions / caveats below.) |

## Overlap analysis

**Wave-1 dispatches (#1–#4, BLAS-1 cohort backfill sequence):**
- **Dispatches #1–#4 all write new L3 chapters** and touch `book/src/L3/index.md` + `book/src/SUMMARY.md` (dep-map rows, table-of-contents insertion). 
  - Dispatch #1 (`apply_linop` L3) triggers first index-write and establishes the second firm row in the L3 index (after krylov-step).
  - Dispatches #2, #3, #4 append sibling rows to the same L3/index.md table and add corresponding SUMMARY.md entries.
  - **OVERLAP: YES** — all four dispatches modify the same artifact regions (L3/index.md + SUMMARY.md) and propose insertions to the same table.
  - **SEQUENCING: SERIAL** — must run #1 → #2 → #3 → #4 sequentially per split-integrator design. Dispatch #1 establishes the section; dispatches #2/3/4 append to it under per-report serial-re-read discipline per CLAUDE.md §Cycle structure "integrator-per-report dispatched serially (not parallel — artifact writes naturally serialize)".

**Wave-1 dispatch #5 (Phase-1 corpus reduction batch):**
- **No overlap with #1–#4** — touches only `book/src/spec/slices/{orthog,chebyshev,polynomial_recurrence_step}.md` (reduction edits, no new files written).
- **Inspection-only shape** (similar to cycle-010 wave-1 pass-2, cycle-010 wave-2 pass-6, cycle-010 wave-2 pass-8) — no cross-artifact dependencies on the L3 cohort work.
- **Can run in parallel with #1–#4 wave-1** — different file regions, no read-dependency on L3 writes.

**Wave-1 dispatch #6 (FGMRES lifter):**
- **Writes to** `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md` (new file) and edits `book/src/L4-L3/index.md` + `book/src/SUMMARY.md` (sibling entries).
- **No overlap with #1–#4** (L3 chapters + index differ from L4-L3 themes + index).
- **Possible light overlap with #5** — both touch `book/src/SUMMARY.md`, but at different sections (L4-L3 vs spec/slices). **Zero actual conflict** (appending distinct rows in distinct subsections).
- **Can run in parallel with #1–#4 and #5** — different file regions.

**Wave-1 dispatch #7 (Eigsolve mutation-rotation L1>L0 theme):**
- **Writes to** `book/src/L1-L0/eigsolve-mutation-rotation.md` (new file) and edits `book/src/L1-L0/index.md` + `book/src/SUMMARY.md` (sibling entries).
- **No overlap with #1–#6** (L1>L0 themes are distinct from L3 + L4-L3 work).
- **Can run in parallel with all wave-1** — different file regions.

**Wave-2 dispatch #8 (Eigsolve OQ cluster lifter):**
- **Writes to** `book/src/L1/eigsolve.md` (existing; extends with new sections/subsections per the three OQs).
- **Dependency on #7** — the eigsolve-mutation-rotation theme landing may clarify context for the three OQs. However, **dispatch #8 can start immediately in parallel with #7** and coordinate scoping post-discovery (e.g., if #7's lowering reveals which variant-axis is most tightly coupled to the result-record structure). **Weak forward-dependency, not strict sequencing**.
- **No overlap with other wave-1 dispatches**.

**Wave-2 dispatch #9 (L0 bundle 6: linalg-solver-file):**
- **Writes to** `book/src/L0/<slug>.md` (new file) and `book/src/L0/index.md` (new concept chapter entry).
- **No overlap with any other dispatch** — L0 file-overview chapters are independent.
- **Can run in parallel with all others**.

**Wave-2 dispatch #10 (Priority #13 planner close):**
- **No artifact mutation** — only `scaffolding/priorities.md` edit.
- **Can execute in parallel with all others** — scaffolding writes do not conflict with artifact writes in the same cycle (separate concerns, no data-flow dependency).

## Sequencing schedule

**Wave-1 (4 serial + 3 parallel):**

- **Serial chain (BLAS-1 cohort backfill L3 bundle)**: #1 → #2 → #3 → #4
  - Per split-integrator discipline, these must run sequentially to maintain per-report serial artifact-write discipline on the shared `L3/index.md` and `SUMMARY.md` regions.
  - Estimated total wall-time: ~4–5 hours (each harvester dispatch ~1 hour baseline context + source-reading overhead).

- **Parallel (independent wave-1 work)**:
  - #5 (corpus reduction batch) — **parallel with #1–#4 serial chain**. Inspection-only; no inter-dependency.
  - #6 (FGMRES lifter) — **parallel with #1–#4 serial chain and #5**. Distinct file regions.
  - #7 (eigsolve L1>L0 theme) — **parallel with all wave-1**. Distinct file regions.

**Wave-2 (2 weak-dependency + 2 independent):**

- **Weak forward-dependency**: #8 (eigsolve OQ lifter) has a soft read-dependency on #7 (eigsolve-mutation-rotation theme) landing. **Can start immediately in parallel**, but scoping coordination post-#7 is recommended to avoid rework.
  - Practical strategy: dispatch #8 and #7 in parallel; #8 prefetch cycle-010 eigsolve §Evidence + existing cycle-009 OQs, and plan for a small post-dispatch-#7 scoping re-read if the theme reveals new cross-reference requirements.

- **Independent**: #9 (L0 bundle 6) and #10 (priority #13 close) — both can run in parallel with wave-2 or at any point after dispatch-0.

**Concrete schedule:**

```
WAVE-1 (parallel where noted)
├─ #1 → #2 → #3 → #4 (serial BLAS-1 L3 cohort)  [4–5 hours; occupies integrator serially]
├─ #5 (phase-1 corpus audit, parallel with above)
├─ #6 (FGMRES lifter, parallel)
└─ #7 (eigsolve-mutation-rotation L1>L0, parallel)

WAVE-2 (parallel; #8 soft-dependency on #7)
├─ #8 (eigsolve OQ cluster lifter; start immediately, re-scope post-#7)
├─ #9 (L0 bundle 6)
└─ #10 (priority #13 close; no artifact mutex)
```

**Total estimated dispatch wall-time:**
- Wave-1 serial chain #1–#4: 4–5 hours (integrator per-report serially constrains throughput).
- Wave-1 parallel (#5, #6, #7 concurrent): 2–3 hours each, overlapped.
- Wave-2 parallel (#8, #9, #10 concurrent): 1–2 hours each, overlapped.
- **Critical path**: ~5 hours (wave-1 serial chain #1–#4) + ~2 hours (wave-2) = ~7 hours total elapsed (not calendar hours; assumes continuous dispatch).

## Open questions / caveats

### Priority #13 close edit (dispatch #10)

Exact action for cycle-planner to execute after dispatch-approval (this is low-friction and in-scope per write-authority partition):

**File**: `scaffolding/priorities.md`

**Current state** (lines 30-31):
```
13. **nrm2_B-weighted-energy-norm-L1** — depends on `apply_linop` (now firm) and `dot` (firm cycle-002). Citation: open question `nrm2-B-weighted-energy-norm-harvest`.
```

**Replacement** (edit to):
```
13. **(LANDED cycle-010 as matrix-weighted-norm)** — cycle-010 wave-2 pass 5 merged `nrm2_B-weighted-energy-norm-L1` into the canonical `matrix-weighted-norm` operator (cycle-010 pass 3; 6 identity claims verified). Canonical entry is `book/src/L1/matrix-weighted-norm.md`. Citation: open question `priority-13-now-landed-as-matrix-weighted-norm` (routing).
```

This marks the priority as landed and redirects users to the canonical entry.

### Dispatch #1–#4 bundling rationale & alternative framings

The BLAS-1 cohort is split across 4 dispatches (one per dispatch) rather than bundled into 1–2 large dispatches. **Rationale**:

1. **MCP codemap pilot readiness** — cycle-010 pilot validated MCP tools at 0-permission-denied rate. Specialized agents now routinely use `list_files`, `search_text`, `get_file_subtree`, `read_range` to localize source without blocking on file-reading latency. **Smaller dispatch scopes** (1–3 operators per dispatch) enable efficient localization per-dispatch.

2. **Per-dispatch context budget** — haiku planner delegates to opus agents. Each opus agent has independent context window. Bundling all 7 operators into one dispatch (apply_linop + 6 BLAS-1) would require ~3500 tokens for full L2/L4 source-reading + variant-axis extraction; splitting into 4 dispatches keeps each harvester at ~2000 tokens (source + L2/L4 skeleton + variant inventory). CLAUDE.md §Dispatch target raises the cap to 12 per cycle; 4 dispatches is <40% capacity.

3. **Integration conflict reduction** — apply_linop as dispatch #1 establishes the `L3/index.md` second-row precedent (after krylov-step). Dispatches #2–#4 then append 3 sibling rows under proven integrator-per-report serial discipline. Per-integration-pass latency is ~10 minutes (review + build); 4 passes are 40 minutes total, but overlap cleanly under parallel critic/repair phases.

**Alternative: Bundle apply_linop + linear-update (axpy/axpby/axpbypcz) into 2 dispatches?** Yes, this is feasible. Would reduce dispatch count from 4 → 3 total (apply_linop alone, then linear-update trio, then reduction pair). Trade-off: dispatch #2 would be larger (~300 lines context; still within budget), and applies all three linear-update rows in one per-report pass (faster integration). **Not selected** because: (a) one-operator-per-dispatch fits the MCP-codemap localization pattern better (each operator is a distinct localization task), and (b) cycle-010 split integrator validated 8 reports / 3-wave split without structural friction; 4-dispatch BLAS-1 cohort is well within validated throughput.

### FGMRES lifter sequencing (dispatch #6)

Cycle-010 wave-2 pass-6 explicitly routed: **"lifter-before-harvester sequencing directive for cycle-011 planner"** regarding `gmres-inner-loop-iterate-while-migration` re-anchoring for FGMRES.

**Why lifter, not abstractor?**

- Cycle-008 wave-2 pass-5 authored the initial `gmres-inner-loop-iterate-while-migration` rough-in L4>L3 theme.
- Cycle-010 wave-1 passed on the gmres.md L4 v0.6→v0.7 self-rotation as a large deferred dispatch (out-of-cycle-010 scope).
- The L4 `gmres.md §v0.7` form is now **stable enough to re-anchor against** post-cycle-010 (the artifact reflects v0.7 usage in the krylov-step chain and downstream L3 themes).
- The re-anchoring work is **re-descriptive, not re-authoring** — the cycle-008 theme body is already written; the lifter updates references and parameterization prose to cover FGMRES alongside GMRES.
- **Abstractor is wrong** because abstractor *speculates* new themes; lifter *refines existing rough-ins against firmer vocabulary*.

**MCP usage**: dispatch #6 should use MCP `search_text` to locate FGMRES variant axes in Palace source (`palace/linalg/gmres.cpp` lines relevant to `flexible_gmres_flag` or similar; MCP will be faster than scrolling the full GMRES file).

### Eigsolve OQ cluster scoping (dispatch #8)

The three remaining OQs (`eigsolve-scaling-coordinate-convention`, `eigsolve-initial-space-axis-placement`, `eigsolve-iteration-count-result-field`) are individually small (~50–70 lines each per prior OQ estimates), but represent distinct variant axes on the `eigsolve` L1 operator result-record. 

**Single unified lifter dispatch vs. three separate dispatches?**

Recommended: **single unified dispatch**. Rationale:
- All three OQs are anchored to the same L1 operator (`eigsolve.md`).
- The variant axes are interdependent (the scaling coordinate convention affects the `EigValue` field representation; initial-space axis placement affects the `EigVector` field shape contract; iteration-count result-field is about the `Converged` / `Diverged` `NumIterations` exposure).
- A single lifter dispatch scoped to all three OQs can write a unified theme (e.g., "Eigsolve L1 result-record variant-axis inventory") or three interlinked working-notes entries in `eigsolve.md` itself.
- Three separate dispatches would risk context-fragmentation and redundant source-reading (same Palace source cited three times).

**Soft dependency on #7 (eigsolve-mutation-rotation):** The three OQs are about the L1 form; dispatch #7 is about the L1>L0 lowering. Dispatch #8 should start immediately in parallel, and pre-fetch cycle-009 OQ definitions + cycle-010 pass-7 lift notes to understand the context. If #7's lowering reveals new constraints on the result-record structure, #8 can adjust scoping post-#7 landing (e.g., adding a cross-reference to the lowering-theme notes).

### Dispatch #5 caveat: phase-1 corpus reduction line-range arithmetic brittleness

Cycle-010 wave-2 pass-8 first-instance audit drifted 1–2 lines from actual H2 section boundaries across all 3 audited slices. Repairer corrected via `grep -n "^## "` enumeration per friction-ledger entry `phase-1-corpus-audit-line-range-arithmetic-brittleness` (recurrence-1).

**Recommendation for cycle-011 dispatch #5**: Before proposing line-range edits, enumerate the target file's section boundaries:
```bash
grep -n "^## " /path/to/slice.md
```

This gives accurate H2 line numbers. Use these line numbers for all `book/src/spec/slices/{orthog,chebyshev,polynomial_recurrence_step}.md` reduction proposals.

**Optional MCP usage**: `search_text` with pattern `^## ` (regex) across the three target slices to identify candidate reduction sections before reading the full file. Faster than manual inspection.

### MCP codemap enablement for dispatches #1–#4, #5, #6

Cycle-010 pilot SUCCESS validates MCP codemap usage in sourcing work. **Recommendation**: cycle-011 dispatches #1–#4, #5, #6 should **use MCP codemap tools by default** for C++ source localization:
- `list_files` to verify file paths exist.
- `search_text` to find relevant operators / patterns in Palace source.
- `get_file_subtree` to inspect AST structure.
- `read_range` to read source passages (only tool that returns text).

This speeds up dispatch throughput and reduces permission-denial risk (MCP pilot proved 0 permission-denied across 14 calls).

### Cycle-012 meta-phase batch-2 aggregation critical targets

Cycle-010 integrator-signals §"CRITICAL cycle-012 meta-phase batch-2 aggregation targets" itemizes 9 patterns for cycle-012 meta-phase to consider (MCP rollout completion, planner-side deduplication, dispatch-brief drift, phase-1-corpus audit brittleness, negative-anchor citation pattern, L1 cohort frontmatter divergence, test-coverage-bounded nomenclature, localize-then-read skill, phase-1-slice-reduction-audit skill, index-placeholder displacement pattern formalization, OQ-to-resolution latency). Cycle-011 planner notes these as context for cycle-012 meta-phase batch aggregation decision-making. **No action required cycle-011** — these fire at meta-phase, not primary-cycle.

