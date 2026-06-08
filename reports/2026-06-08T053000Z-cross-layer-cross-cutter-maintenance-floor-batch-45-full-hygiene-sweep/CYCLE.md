---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-08T053000Z
scope: maintenance-floor — batch-45 once-per-batch full-hygiene sweep
status: integrated
integrated_at: 2026-06-08T165758Z
integration_commit: 292a301
integration_notes: "cycle-139 (batch-45 OPENER, 1/3). MAINTENANCE FLOOR clean-bill, audit-class — NO book mutation (OQ append done in-dispatch); the once-per-batch full-hygiene sweep placed at the OPENER to ground the wide arc's linter baseline. All 12 graded-stack baseline fields reproduce on-disk, both hard invariants hold (rank_violations==0, unresolved==0), 3 realizes-kernel-api edges reference-class, DIRECTIVE-1 boundary intact. Finalize step-5b re-run on the LANDED tree confirmed the forecast (all counts HELD)."
---

# CYCLE: Maintenance-floor full-hygiene sweep — batch-45 (cycle-139 OPENER, wave 2)

## Summary
The single per-batch maintenance dispatch for batch-45. I ran the six-part full-hygiene
sweep against the on-disk book (still the c138 baseline — the c139 wave-1 proposed-changes
apply at integration, not yet on disk) and **forecast** the c139 moves. **CLEAN BILL.** All
12 graded-stack baseline totals match c138 exactly; the two hard invariants
(`rank_violations == 0`, no newly-orphaned node) hold and are forecast to hold after the c139
wave-1 moves (D2/D5 within-chapter → no node/edge move; D3 adds OUTBOUND `reference`-only
edges from a rank-0 node → no rank/liveness move). The 3 `realizes-kernel-api` edges stay
`reference`-class on disk; the semantic surface shows no path/anchor drift and no new
restatement cohort; the DIRECTIVE-1 MPI boundary in the sharding chapter is cited-as-deferred,
not lifted. No flagged residuals requiring meta-phase action. One opportunistic edge-typing
observation recorded (non-blocking) for the GMG/AMR consumer-gated false-detritus cohort.

## Observation kind
**Audit residue** — clean-bill maintenance sweep (no coverage gap, no edge-label mismatch, no
consistency drift, no vocabulary mismatch surfaced). The only forward-looking note is an
opportunistic-GC observation, deferred to the batch-45 all-fronts campaign (which is itself
the consumer-wiring that collapses the noted false-detritus).

## Specific finding

### 1. Graded-stack lint `--json --reference-reachable` totals — BASELINE HOLDS
Ran `tools/graded-stack-lint/graded_stack_lint.py --json --reference-reachable`. All 12
carried c138 baseline fields match the on-disk state EXACTLY:

| field | c138 baseline | on-disk c139 | match |
|---|---|---|---|
| files | 392 | 392 | OK |
| typed | 331 | 331 | OK |
| untyped | 61 | 61 | OK |
| roots | 45 | 45 | OK |
| reachable | 163 | 163 | OK |
| reference_reachable | 247 | 247 | OK |
| detritus | 123 | 123 | OK |
| true_detritus | 51 | 51 | OK |
| **rank_violations** | **0** | **0** | **OK (hard invariant)** |
| **unresolved_depends_on_targets** | **0** | **0** | **OK (hard invariant)** |
| promotion_frontier | 12 | 12 | OK |
| expected_unreachable_outside_dag | 54 | 54 | OK |

**Forecast of the c139 wave-1 moves** (not yet on disk; the only `book/src/` commit since the
c138 finalize is the c138 meta-phase doc-only touch `aa7cf84` to `methodology/goal-flow.md`
(+21 lines, no `status:`/`rank:`/`kind:` line changed) — no frontmatter firmed):
- **D2** (`lanczos_step` 4 sharpening edits, STAYS `roadmap_goal`) — within-chapter content
  only. On-disk frontmatter is `status: roadmap_goal / rank: roadmap_goal / kind:
  kernel-impl-constituent` (`book/src/L3/lanczos_step.md:1-12`). No node/edge move → no totals
  change.
- **D3** (`L4/sharding-decompose-reduce` solve-generalization extension) — adds three firm
  SOLVE roots (`L4/ksp_solve`, `L4/fold_solve`, `L4/krylov-step`) under `reference:` ONLY
  (never `depends-on`), per the abstractor report's proposed-changes block. The node STAYS
  rank-0 `roadmap_goal`. Three structural consequences, all forecast-clean:
  - `rank_violations` stays 0 — the rank linter constrains only `depends-on` edges; a
    `reference` edge from a rank-0 node to a firm (rank-3) node carries no rank constraint.
  - No newly-orphaned node — the edits are additive (new reference targets) + content; no
    inbound edge to any existing node is removed.
  - `detritus` / `true_detritus` counts UNCHANGED — `L4/sharding-decompose-reduce` is
    presently in the `true_detritus (51)` set (`[garbage?]` in the reference-reachable
    split). Adding OUTBOUND `reference` edges does NOT make the sharding node itself
    reachable (reachability flows root→node along edges; an outbound reference from sharding
    confers no inbound reach to sharding). It stays true-detritus BY-DESIGN (rank-0
    `roadmap_goal`, DD-preconditioner-consumer-gated) — this is the expected RE11/consumer-gated
    posture, NOT decay.
- **D5** (3 Synthesis content-fidelity edits, within-chapter) — no node/edge move → no totals
  change.

Rank histogram on disk: `firm 224, rough-in 4, partly-constructive 3, obstruction 2,
partial-obstruction 4, roadmap_goal 4, stub 1, typed-no-rank 89` — consistent with the
batch-44-complete state.

### 2. RE-set premise re-check — ALL PREMISES HOLD
- **No book frontmatter status changed this batch.** The only `book/src/` commit since the
  c138 finalize is the c138 meta-phase doc-only touch `aa7cf84` to `methodology/goal-flow.md`
  (+21 lines; an untyped doc surface outside the typed dep-graph, no `status:`/`rank:`/`kind:`
  line changed), so every RE baseline-exception's "no faithful inbound `depends-on` consumer"
  premise is unchanged from c138. Nothing firmed → no RE promotion-condition fired on disk.
- **RE4** (consumer-gated; no GMRES-variant column) — premise holds; no GMRES-variant column
  exists on disk; `concepts/gmres` remains true-detritus (`[garbage?]`), consumer-gated.
- **`L4/sharding-decompose-reduce` §2g-extension member (D3 touches it)** — re-verified:
  STAYS `reference`-class-only-reachable, solve-generalization-consumer-gated, does NOT promote
  off rank-0 this cycle. Frontmatter on disk `rank: roadmap_goal` (`book/src/L4/sharding-
  decompose-reduce.md:3-4`); the report confirms the `...solve-generalization-promotion-pull`
  OQ STAYS DEFERRED (no single-machine-valid DD-preconditioner consumer in flight). ✓
- **RE11 deliberate-reference-only-reachable cohort (72) escalate-guard** — detritus count
  123 / true_detritus 51 / ref-reachable §2g 72 all match c138; no climb beyond the BY-DESIGN
  (zero) moves this cycle. The guard does NOT trip.

### 3. Kernel-API/impl `realizes-kernel-api` integrity — ALL 3 EDGES `reference`-CLASS ON DISK
Cross-checked all three `realizes-kernel-api` edges; each is under `reference:` with
`kind: realizes-kernel-api`, never `depends-on`:
- `book/src/L1/libceed-quadrature-kernel-impl.md` — `edges.reference: target:
  L1-L0/fe-assemble-libceed-boundary-obstruction, kind: realizes-kernel-api` (free,
  navigational; the impl is `rank: firm`, its blocking `depends-on` edges go to its four firm
  tensor-contraction constituents).
- `book/src/L3/eigsolve-impl.md` — `edges.reference:` carries TWO `realizes-kernel-api` edges
  (→ `L3/eigsolve` AND → `L4/eigsolve`), both `reference`-class; the node is itself rank-0
  `roadmap_goal` (the batch-45 D4 front). D4 re-audits these; on the c138 baseline they are
  correctly typed. ✓
- `book/src/L1/multigrid-relaxation-smoother.md` — `edges.reference: target:
  L1-L0/triangular-solve-obstruction, kind: realizes-kernel-api` (free, NOT depends-on); node
  is `rank: firm`, blocking deps go to its firm point-smoother / matvec / interpolator
  constituents.

All three impls correctly keep the opaque kernel-API as a reviewed CORRESPONDENCE
(reference-class), not a build dependency — DIRECTIVE-3 mechanics intact.

### 4. Semantic-surface liveness drift — NO DRIFT, NO NEW RESTATEMENT COHORT
- Intra-book link scan of `book/src/semantics/index.md` — every relative `](../…)` /
  `](./…)` link resolves to an existing file; zero broken paths/anchors.
- `semantics/index` appears in the `untyped (61)` set, as expected — the semantic surface is a
  documentation surface outside the typed dep-graph (part of `expected_unreachable_outside_dag
  = 54`), not a node-decay signal.
- No new restatement cohort surfaced. The c138 whole-Synthesis-Part correspondence audit
  confirmed Synthesis USEs+LINKs (does not restate); `synthesis/data-algebra` shows as
  `[FRONTIER] untyped` (a library-intro documentation surface), consistent with that audit. No
  general semantic rule/def restated at a functional-unit scope appeared in this sweep.

### 5. DIRECTIVE-1 boundary check — MPI PATHS CITED-AS-DEFERRED, NOT LIFTED
The sharding chapter (`book/src/L4/sharding-decompose-reduce.md`) is the live DIRECTIVE-1 risk
surface this cycle (D3 extends it). On-disk verification:
- The frontmatter STATUS banner (`:33-35`) states "MPI/distributed mechanics are the
  deferred-future *mechanism*, cited but NOT lifted (DIRECTIVE-1)."
- A dedicated section "**The deferred-future MECHANISM (cited, NOT lifted — DIRECTIVE-1)**"
  (`:187-204`) gathers ALL MPI-path citations under an explicit OUT-of-active-scope /
  may-be-DESTRUCTIVE-to-the-spine frame: `Partition(...)` + `GetMeshPartitioning(...)`
  (`utils/geodata.cpp:262, :3230-3242`); `ParOperator` + the `R·A·P` Galerkin product
  (`linalg/rap.hpp:24`, `linalg/rap.cpp:116-126`); the MPI collectives (the reduction
  communication leg).
- The active content is the decomposition MATH; the coupling/overlap handling is explicitly
  carried as "mechanism, NOT a structural law of the bare abstraction" (`:160-165, :204-218`).
- The D3 proposed-changes block (per the abstractor report) preserves this framing for the
  solve-generalization (RAP cited as the eventual `restrict_op_to_block` realization, flagged
  "DEFERRED mechanism"; "no native additive-Schwarz / domain-decomposition preconditioner"
  confirmed by codemap search). DIRECTIVE-1 boundary is intact on disk and forecast-intact
  after D3.

### 6. Opportunistic detritus / edge-typing GC — ONE NON-BLOCKING NOTE
The `true_detritus (51)` set is dominated by two recognizable consumer-gated cohorts that a
future opportunistic edge-typing pass — OR, more naturally, the batch-45 all-fronts
consumer-wiring itself — will collapse from detritus to reachable. These are NOT decay; flagged
for awareness, NOT for fix this cycle:
- **GMG / AMR consumer-gated cohort** (the `[GARBAGE*]` "detritus-with-typed-edges /
  stronger-signal" subset, the more meaningful false-detritus): `L1-L0/amr-estimate-mark-refine`,
  `L1/dorfler_mark`, `L1/flux_recovery_estimate` (AMR front-2), and the multigrid-leg nodes
  (`L2/correction_step`, the `L1/L2/L3 jacobi-smoother` / `reciprocal` / `normalize` chains).
  These become reachable as the batch-45 GMG (`feature/geometric-multigrid-preconditioner.*`
  already a root) and AMR fronts wire their `depends-on` consumers. **GROUND-don't-remove
  applies** — every one of these is a genuine future-dependency of a reachable goal (the GMG /
  AMR feature columns), NOT detritus to delete.
- **eigsolve-impl front cohort**: `L3/eigsolve-impl`, `L3/lanczos_step`,
  `L3/nleps-deflated-eigensolve` — the batch-45 eigsolve-impl / NLEPS (RE3) fronts; become
  reachable as the eigenmode driver wires the constructive impl by name.
- **The libCEED kernel-impl** `L1/libceed-quadrature-kernel-impl` shows `[GARBAGE*]` despite
  being firm + spine-realizing — its inbound is via `realizes-leaf` (`reference`-class to
  `fe_assemble`) so it is reference-reachable (it appears in the §2g ref-reachable list, NOT
  true_detritus); a candidate for a future opportunistic typed-edge review only if a faithful
  `depends-on` consumer ever wants it blocking. NO action.

## Recommendation
**Defer — clean-bill maintenance sweep; no immediate action required of the batch-45
meta-phase.** The two hard invariants hold on disk and are forecast to hold after c139 wave-1
integration. The opportunistic-GC note (§6) is informational: the batch-45 all-fronts campaign
(GMG + AMR + eigsolve-impl) is itself the consumer-wiring that will collapse the noted
false-detritus cohorts from detritus to reachable — so NO standalone edge-typing dispatch is
warranted; re-check the detritus split after the batch-45 consumer fronts land.

## Supporting evidence
- Linter: `tools/graded-stack-lint/graded_stack_lint.py --json --reference-reachable` (run
  2026-06-08; totals table §1).
- `book/src/L4/sharding-decompose-reduce.md:1-24` (frontmatter, rank-0, reference-only edges),
  `:33-35` (DIRECTIVE-1 banner), `:150-218` (config-conditional non-law + deferred-MECHANISM
  section).
- `book/src/L1/libceed-quadrature-kernel-impl.md` (`edges.reference` realizes-kernel-api,
  rank firm); `book/src/L3/eigsolve-impl.md` (two realizes-kernel-api reference edges, rank-0
  roadmap_goal); `book/src/L1/multigrid-relaxation-smoother.md` (realizes-kernel-api reference
  edge, rank firm).
- `book/src/L3/lanczos_step.md:1-12` (roadmap_goal on disk; D2 keeps it there).
- `book/src/semantics/index.md` (intra-book links resolve; untyped-by-design).
- `git log f1b69f1..HEAD -- book/src/`: only commit is the c138 meta-phase doc-only touch
  `aa7cf84` to `methodology/goal-flow.md` (+21 lines, no `status:`/`rank:`/`kind:` changed —
  untyped doc surface outside the dep-graph) → RE premises unchanged.
- Wave-1 reports forecast: `reports/2026-06-08T053000Z-abstractor-sharding-decompose-reduce-
  solve-generalization-sketch/CYCLE.md` (D3 proposed-changes: reference-only, MPI deferred),
  `reports/2026-06-08T053000Z-abstractor-lanczos-step-toward-promotion/CYCLE.md` (D2 stays
  roadmap_goal).

## Open questions / caveats
- The on-disk state is the c138 baseline; the c139 wave-1 moves are FORECAST clean (not
  yet applied). The integrator-finalize step-5b tripwire (the per-cycle floor for c140/c141)
  should re-confirm `rank_violations == 0` + no detritus climb AFTER c139 integration actually
  lands — the forecast is structural (reference-only / within-chapter) but the post-integration
  re-run is the authoritative confirmation.
- D4 (eigsolve-impl re-audit) runs in this same wave; its on-disk `L3/eigsolve-impl.md`
  realizes-kernel-api edges are correctly `reference`-class at the c138 baseline — D4 should
  confirm the post-edit state preserves that (cross-checked here, not blocking).
