---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-07T203807Z
scope: MAINTENANCE FLOOR standing hygiene + c134 re-baseline duty (batch-43, D2)
status: pending
integrated_at: 2026-06-07T214500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied clean as the batch-43 c134 D2 maintenance-floor audit (AUDIT-CLASS — NO book mutation; touched only scaffolding/open-questions.md append). Verdict: clean-bill + RE-BASELINE CONFIRMED. The c133-baseline forecast (files→386, roadmap_goal 3→4, rank_violations=0/unresolved=0 held) CONFIRMED on disk by the D1 sharding-sketch landing earlier this cycle. The 3 realizes-kernel-api kernel-impl edges stay reference-class; semantic surface clean; RE4 consumer-gated (premise holds), RE11 premises hold + the new sharding-decompose-reduce node joins the RE11 deliberate-reference-only-reachable cohort (§2g) BY DESIGN. integrator-finalize ran the AUTHORITATIVE post-landing lint per the report's recommendation and re-baselined the scaffolding/-held running counts (files=386, roadmap_goal=4, detritus=123, true_detritus=51; rank_violations=0, unresolved=0) — the c133 files=385 snapshot is SUPERSEDED. The FORMAL held-baseline-exceptions re-baseline + RE-set disposition for the new node is the batch-43 meta's to own. Promoted OQ maintenance-floor-re-baseline-CONFIRMED-c134-sharding-sketch-landed. Per-report integrator: integrator-per-report (staging row #2). Cycle-end housekeeping + commit: integrator-finalize cycle-134.
---

# CYCLE: Cross-layer observation — c134 maintenance-floor clean-bill + re-baseline disposition

## Summary
Ran the four standing maintenance-floor checks plus the c134-specific re-baseline duty. **Clean bill on all four standing checks.** The graded-stack hard invariants hold: `rank_violations=0`, `unresolved_depends_on_targets=0`. D1's new `roadmap_goal` chapter (`book/src/L4/sharding-decompose-reduce.md`) was **NOT yet on disk** at lint time (parallel dispatch), so the linter reports the EXACT held c133 baseline — no deltas this run. The re-baseline must be re-confirmed at finalize once D1's chapter lands; the disposition (what the counts SHOULD move to, and the tripwire) is recorded below so integrator-finalize can confirm the landing is the expected sharding-sketch shift and not a regression.

## Observation kind
**Audit residue** — standing-hygiene re-check, no new cross-layer defect surfaced. (Audit-class dispatch; no book mutation; no stale token found.)

## Specific finding

### (i) RE-set re-check — PASS
- **RE4 stays consumer-gated.** `book/src/feature/` contains only `driven.{L0,L1,L4}.md` — the standard driven driver column, `feature_root: seed`, `rank: firm`. **No GMRES-variant driven-solver column was added at c134.** RE4's consumer-gate premise holds (no consumer wired in → RE4 stays a tracked baseline-exception, not a regression).
- **RE11 deliberate-reference-only-reachable cohort premises hold.** Linter: `reference_reachable=247`, `detritus_reference_reachable_re11_cohort=72` — both at the held c133 values. §2g escalate-guard not tripped (no monotonic reference-reachable growth this run; counts static because D1's chapter not yet landed).

### (ii) kernel-API/impl integrity — PASS
All three `realizes-kernel-api` edges are typed `reference`-class on disk (under `edges.reference:`, NOT `edges.depends-on:`):
- `book/src/L1/libceed-quadrature-kernel-impl.md:21-23` — `reference:` block, `kind: realizes-kernel-api` → `L1-L0/fe-assemble-libceed-boundary-obstruction`. (depends-on block at line 28 holds only the four firm `composes` substrate deps — correctly separated.)
- `book/src/L3/eigsolve-impl.md:19-23` — `reference:` block, two `realizes-kernel-api` edges → `L3/eigsolve` + `L4/eigsolve`. (depends-on block at lines 8-17 holds only `folds`/`composes` constituents.)
- `book/src/L1/multigrid-relaxation-smoother.md:24-26` — `reference:` block, `kind: realizes-kernel-api` → `L1-L0/triangular-solve-obstruction`. (depends-on block at lines 15-22 holds only the four firm `uses` constituents.)

No mis-typing. The reviewable-correspondence-not-build-dependency semantics are intact for all three founding kernels.

### (iii) semantic-surface liveness — PASS
`book/src/semantics/index.md` (51210 bytes, present). All relative `.md` link targets (`../` up-links and `./` same-dir) resolve to existing files — **no stale path/anchor drift**.

### (iv) c134 re-baseline duty — BASELINE STILL HELD (re-baseline DEFERRED to finalize)
`book/src/L4/sharding-decompose-reduce.md` **does not yet exist** at lint time (D1 dispatched in parallel; chapter not on disk). Linter output is therefore the **exact held c133 baseline, unchanged**:

| metric | c133 held | c134 this run | delta |
|---|---|---|---|
| files | 385 | 385 | 0 |
| typed | 324 | 324 | 0 |
| untyped | 61 | 61 | 0 |
| roots | 45 | 45 | 0 |
| reachable | 163 | 163 | 0 |
| reference_reachable | 247 | 247 | 0 |
| **rank_violations** | **0** | **0** | **0 ✓** |
| **unresolved** | **0** | **0** | **0 ✓** |
| promotion_frontier | 10 | 10 | 0 |
| detritus | 122 | 122 | 0 |
| true_detritus | 50 | 50 | 0 |

**Hard invariants confirmed: `rank_violations=0`, `unresolved_depends_on_targets=0`.** No tripwire fired (no mistyped `depends-on` edge from D1, because D1's chapter is not yet present).

**Expected re-baseline disposition once D1's chapter lands** (for integrator-finalize to confirm): a NEW rank-0 `roadmap_goal` node + its `reference`-class edges to firm roots. Expected count movement:
- `files` 385 → **386** (+1, the new chapter).
- `roadmap_goal` rank-histogram bucket 3 → **4** (+1).
- `typed`/`untyped`: the new node carries typed edges → `typed` likely → **325** (+1) if the chapter has an `edges:` block; `untyped` unchanged at 61.
- `reference_reachable` and/or `detritus` shift per how the `reference` edges to firm roots wire the node into the reference-reachable closure (a rank-0 node reached only by `reference` edges is NOT `reachable` over `depends-on`; whether it counts `reference_reachable` depends on inbound vs outbound direction — D1's edges point FROM the new node TO firm roots, so the new node is itself likely `detritus`/`true_detritus` unless a root references it back, which is the EXPECTED sharding-sketch disposition).
- **CRITICAL TRIPWIRE (unchanged):** `rank_violations` MUST stay **0** and `unresolved` MUST stay **0**. If `rank_violations > 0` after D1 lands, D1 mistyped a `depends-on` edge (a rank-0 node `depends-on` a firm root would violate `rank(u) ≤ rank(v)` only in the reverse — but a firm node `depends-on` the new rank-0 node would be the violation). Per OQ `maintenance-floor-baseline-re-baseline-on-sharding-sketch-landing`, the count MOVEMENT is EXPECTED-by-design; only a nonzero `rank_violations`/`unresolved` is a regression.

## Recommendation
**Defer the authoritative re-baseline to integrator-finalize.** This run records the c133 baseline as still-held (D1 not yet landed). integrator-finalize will run the post-landing lint authoritatively; it should:
1. Confirm `files=386`, `roadmap_goal`-bucket=4 (the expected +1 sharding-sketch landing).
2. Confirm `rank_violations=0` and `unresolved=0` (the hard tripwire — flag HARD to repairer if either is nonzero, indicating D1 mistyped an edge).
3. Re-baseline `scaffolding/` held-baseline to the new counts.

No other follow-up. No coverage gap, no edge-label mismatch, no vocabulary mismatch surfaced. **Clean bill** on standing hygiene.

## Supporting evidence
- Lint command: `python3 tools/graded-stack-lint/graded_stack_lint.py --json` (totals block).
- `book/src/L1/libceed-quadrature-kernel-impl.md:18-28` — `edges.reference` vs `edges.depends-on` partition.
- `book/src/L3/eigsolve-impl.md:6-32` — frontmatter `depends-on` vs `reference` blocks.
- `book/src/L1/multigrid-relaxation-smoother.md:13-31` — frontmatter `depends-on` vs `reference` blocks.
- `book/src/semantics/index.md` — present, 51210 bytes, all relative `.md` links resolve.
- `book/src/feature/driven.L4.md:1-3` — `feature_root: seed`, `rank: firm` (standard driven column; no GMRES-variant sibling).

## Open questions / caveats
- **Re-baseline is provisional this run.** Because D2 dispatched in parallel with D1, the lint did NOT see the sharding chapter. The authoritative post-landing lint is owed at finalize (OQ `maintenance-floor-baseline-re-baseline-on-sharding-sketch-landing`). This report's expected-disposition table is a forecast, not a confirmed re-baseline.
- The exact `reference_reachable`/`detritus`/`true_detritus` movement depends on D1's edge DIRECTION (new-node→root vs root→new-node). A `roadmap_goal` reached only by outbound `reference` edges to roots is itself detritus/true_detritus by the GC semantics — that is the EXPECTED, GROUND-don't-remove disposition for an exploratory sharding-MATH sketch (it is a deferred future-direction node, gated, reference-class to firm roots, intentionally not depends-on-reachable). integrator-finalize should NOT flag the new node's detritus status as a regression.
