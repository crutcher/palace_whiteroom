---
agent: cycle-planner
invoked_at: 2026-06-08T193000Z
scope: cycle-142 dispatch plan (batch-46 OPENER, 1/3 of meta-batch-46; the batch-46 meta fires after cycle-144's finalize)
status: pending
---

# Cycle 142 dispatch plan

## Goals selected this cycle

Batch-46 is **WIND TO MAINTENANCE** — the human's FIFTH consecutive §CENTRAL-ASK resolution (2026-06-08; `project_batch46_direction_wind_to_maintenance`). There is **NO substantive in-scope forward frontier** under the standing gates (each front is rectangular-pull-up / gate-blocked / consumer-gated — itemized in §"NO substantive frontier" below). c142 is the batch OPENER, so per the per-batch-sweep cadence (priorities.md item 0, the batch-43 cadence change) it fires the project's **single once-per-batch maintenance-floor cross-cutter** — the full-hygiene sweep that grounds the batch's linter baseline, exactly as c139 D6 did for batch-45. This is an honest maintenance-batch opener: **ONE audit-class dispatch, no build-out**, with the per-cycle two-invariant tripwire left to `integrator-finalize` step-5b (no dedicated dispatch). The linter baseline is forecast to HOLD EXACTLY — a maintenance/audit sweep moves no node/edge/rank.

## Dispatches

### D1 — `cross-layer-cross-cutter` · `maintenance-floor-batch-46-full-hygiene-sweep`

- **agent:** `cross-layer-cross-cutter` (matching how batch-45 ran the once-per-batch sweep at c139 D6 — a cross-layer audit observation, OQ-append only, no artifact mutation).
- **scope:** The **once-per-batch full-hygiene sweep** grounding the batch-46 linter baseline. Six audit checks, all read-only / OQ-append:
  1. **Graded-stack lint `--json` totals re-confirmation.** Run `python3 tools/graded-stack-lint/graded_stack_lint.py --json`; confirm the two hard invariants (`rank_violations == 0`, `unresolved_depends_on_targets == 0`) and record the full totals snapshot. Forecast: HOLDS EXACTLY vs batch-45 terminal (`files 392, typed 331, untyped 61, roots 45, rank_violations 0, unresolved_depends_on_targets 0, promotion_frontier 12, reachable 163, reference_reachable 247, detritus 123, true_detritus 51, expected_unreachable_outside_dag 54`).
  2. **RE-set premise re-check.** Confirm the TERMINAL in-scope RE-set premises HELD across batch-45 and still hold: **RE4** (GMRES running-QR ILS view — consumer-gated; no driven-solver GMRES-variant column in flight), the **sharding-node §2g-extension member** (`L4/sharding-decompose-reduce`, solve-generalization-consumer-gated — DIRECTIVE-1 keeps MPI/distributed OUT), the **RE11** deliberate-reference-only-reachable cohort (§2g-accounted BY DESIGN; the synthesis `expected_unreachable_outside_dag` chapters join this class). Also re-confirm the eigsolve-impl promotion gate is still NON-FIRING (OQ `lanczos_step` arm-A unsatisfiable from `palace/` MINRES enum-only-stub; arm-B blocking-consumer not in flight — recorded NON-FIRING at c139, recheck unchanged).
  3. **Kernel-API/impl integrity (DIRECTIVE 3).** Confirm the 3 `realizes-kernel-api` edges stay `reference`-class on-disk: `eigsolve-impl` (×2: L3 + L4 eigsolve), `libceed-quadrature-kernel-impl`, `multigrid-relaxation-smoother`. Confirm the Synthesis `#extern` leaves still trace to the kernel-API nodes (not claiming an impl).
  4. **Semantic-surface liveness drift.** Confirm `book/src/semantics/index.md` §0.1 discipline intact, no new restatement cohort surfaced this batch (batch-46 is a maintenance batch authoring NO new vocabulary), no source contradiction, `SUMMARY.md` wiring intact. (The cross-surface relocation-drift class — friction-ledger `book-relocation-leaves-scaffolding-role-spec-references-stale` — is `addressed`/recurrence-1; no `book/` relocation this batch, so re-run-clean expected.)
  5. **Opportunistic detritus / edge-typing GC** (`p1-edge-typing-true-detritus-sweep`). `true_detritus` is 51 — dominated by the GMG/AMR + eigsolve-impl/NLEPS **consumer-gated false-detritus cohorts** that GROUND-don't-remove (`feedback_gc_ground_dont_remove_future_deps`) and collapse only when a blocking consumer wires in. Confirm the detritus-count escalate-guard is NOT tripped (count stable at 123/51); flag (do NOT force) any node now cleanly typeable. No removal.
  6. **DIRECTIVE-1 boundary re-confirmation.** Confirm NO plan/dispatch item this batch lifts the MPI-associated version (`linalg/rap.*` RAP, `utils/geodata.cpp` distribution, the MPI collectives) as active work. (Lower live-risk than batch-45's c139 D6, which had a live sharding dispatch (D3) to verify cited-not-lifted; batch-46 dispatches NO sharding work, so this is a clean steady-state re-confirmation.)
- **deps:** none.
- **rationale:** priorities.md batch-46 item 1 (`maintenance-floor-standing-hygiene`) + item 0 cadence (the full-hygiene sweep runs once per BATCH, at most one dedicated cross-cutter dispatch per batch, fired at the OPENER to ground the batch baseline). Working precedent: c139 D6 `maintenance-floor-batch-45-full-hygiene-sweep` (same agent, same six-check shape). **fan-out: LOW/hygiene.** Plan-tag `graded-stack-hygiene`.

## NO substantive frontier dispatched — per-front justification (CLAUDE.md §redirect no-forced-rectangular-pull-up; DIRECTIVE-1; DIRECTIVE-3)

Confirmed: c142 dispatches NO substantive build-out. The four candidate fronts are each foreclosed:

- **Front 1 (geometric-multigrid preconditioner): ALREADY firm/built at batch-39.** `feature/geometric-multigrid-preconditioner.{L4,L1}.md` firm; `L1/multigrid-relaxation-smoother.md` firm (kernel-impl); RE9/RE1/RE5/RE7/RE10 all discharged batch-39. Re-building is a **FORBIDDEN rectangular pull-up** (forcing a standalone L2/L3 V-cycle node when the recursion correctly lives in the feature column composing firm vocabulary).
- **Front 2 (AMR): theme + leaves LANDED.** `L1-L0/amr-estimate-mark-refine.md` firm; `L1/flux_recovery_estimate.md` + `L1/dorfler_mark.md` firm; the AMR watch-item is PRE-RESOLVED (homes refinement-set growth through firm `L4/fold_solve`, case (a), no new combinator). No new AMR vocab node warranted unless the decomposition reshapes — it does not. Re-building = rectangular pull-up.
- **Front 3 (`eigsolve-impl` kernel-impl): promotion GATE-BLOCKED.** Fully-fleshed 227-line rank-0 `roadmap_goal`, re-audited FULLY-SUPPORTED at c139 D4. Promotion is gate-blocked: arm-A (`lanczos_step` positive-structure) **UNSATISFIABLE from `palace/`** (MINRES enum-only-stub — confirmed NON-FIRING at c139, OQ recorded); arm-B (blocking-consumer wiring) **NOT in flight**. Deepening = padding. Not dispatched.
- **Front 4 (`sharding-decompose-reduce`): exploratory rank-0, consumer-gated BY MANDATE.** 33KB rank-0 `roadmap_goal`, extended c139 D3 + audited FULLY-SUPPORTED c140 D1 + citation-hygiene-cleaned c141 D1. The precise p.o.u./RAS form is consumer-gated (the eventual single-machine-valid DD-preconditioner consumer, NOT in flight); DIRECTIVE-1 keeps MPI/distributed OUT (cited-not-lifted). Further deepening has no clean room. Not dispatched.

No OQ-ledger trigger has fired (sharding sibling OQs `sharding-compose-partition-pou-weighting-sketch-level-only` + `sharding-decompose-reduce-solve-generalization-promotion-pull` stay OPEN but consumer-gated; the eigsolve-impl promotion gate is recorded NON-FIRING). No friction-ledger pattern is `escalating` (the KaTeX `$`-sigil class is `addressed`/recurrence-2 with the new c141 triple-guard). No deferred-OQ trigger has newly fired.

## Per-cycle tripwire floor (NO dedicated dispatch)

The per-cycle floor is the **`integrator-finalize` step-5b two-invariant tripwire** (priorities.md item 0): one `graded_stack_lint.py --json` run asserting `rank_violations == 0` + no newly-orphaned node + the detritus-count escalate-guard. This is the existing finalize step — **NO dedicated dispatch**. The full per-batch sweep (D1) does the heavier RE/kernel/semantic/DIRECTIVE-1 checks once at the OPENER; the per-cycle tripwire carries c143/c144.

## Overlap analysis

Only one dispatch (D1). No pair to analyze. D1 is read-only (audit-class, OQ-append only) — it mutates no `book/` artifact, no shared layer index, no dep-map row, no consolidated tally. There is no shared-index / dual-registration / forward-reference-slug coordination concern this cycle (those guards apply only to multi-landing producer waves; this is a single audit dispatch).

## Sequencing schedule

**Wave 1 (single dispatch):** D1 `cross-layer-cross-cutter` maintenance-floor full-hygiene sweep. One `integrator-finalize` at cycle-end (which also runs the per-cycle step-5b tripwire). No second wave — no forward-reference ordering, no producer landings to read.

## Linter-baseline forecast

D1 is audit-class (OQ-append only; no node/edge/rank/status move). The linter baseline is forecast to **HOLD EXACTLY** vs the batch-45 terminal state (verified on-disk by this planner at plan time, `tools/graded-stack-lint/graded_stack_lint.py --json`):

```
files 392, typed 331, untyped 61, roots 45,
rank_violations 0, unresolved_depends_on_targets 0, promotion_frontier 12,
reachable 163, reference_reachable 247,
detritus 123, true_detritus 51, expected_unreachable_outside_dag 54
```

## Deliverable-presence verification

D1 is **open by construction**: it is a fresh per-batch maintenance-floor cross-cutter sweep with no prior-cycle artifact-presence to collide with (its sole output is an OQ-append audit observation, not a named `book/src/<layer>/<slug>.md` deliverable). The four-step deliverable-presence sequence (file-existence / maturity / OQ-RESOLVED-grep / structural-block) targets named-artifact-slug producer dispatches; an audit-class cross-cutter that lands no chapter has no such slug. The MANDATORY-skip is therefore explicit: **D1 skipped — open by construction (audit-class, no named-artifact deliverable; the once-per-batch sweep is fresh each batch by the item-0 cadence; working precedent c139 D6).**

Supporting plan-time verification actually run (pasted inline):
- **Linter on-disk:** `python3 tools/graded-stack-lint/graded_stack_lint.py --json` → `totals: {"files": 392, "typed": 331, "untyped": 61, "roots": 45, "rank_violations": 0, "unresolved_depends_on_targets": 0, "promotion_frontier": 12, "reachable": 163, "reference_reachable": 247, "detritus": 123, ..., "true_detritus": 51, "expected_unreachable_outside_dag": 54}` — matches the task-stated and batch-45-terminal baseline EXACTLY.
- **OQ ledger tail:** the batch-44/45 follow-ups are all `DISCHARGED-c139/c140/c141`; the sharding sibling OQs + the eigsolve-impl promotion gate are recorded OPEN/NON-FIRING (no fired trigger). No frontier opens.
- **Friction-ledger tail:** no `escalating` pattern; the KaTeX `$`-sigil class is `addressed` (recurrence-2, c141 triple-guard); the relocation-drift class is `addressed`/recurrence-1 (no `book/` relocation this batch).

## Open questions / caveats

- **Honest maintenance-batch opener.** This is a deliberately minimal plan (one audit dispatch). The honesty is itself the signal the batch-46 meta (after c144) needs: batch-46 confirms in-scope steady-state completeness for a **6th consecutive batch**. If the human chooses to keep winding to maintenance, c143/c144 will be even thinner (per-cycle tripwire floor only, or one land-clean hygiene touch if a recorded-but-unfixed nuance surfaces — the batch-45 c140/c141 pattern). No §CENTRAL-ASK is re-surfaced mid-batch; the forward-direction decision belongs to the meta-phase + human, not the planner.
- **No mid-batch frontier re-opening.** Per the resolution, fronts (B)/(C)/(D) are re-openable ONLY on explicit future human direction. If a consumer for a gated front materializes mid-batch (a deflate/krylov-iteration view wiring a blocking `depends-on` into `eigsolve-impl`, or a single-machine-valid DD-preconditioner consumer pulling `subdomain_solve`), I would surface it here as a fresh plan candidate — none has this cycle.
- **Session-restart dependency (informational).** The batch-45 meta enacted the c141 KaTeX pre-apply lint into `integrator-per-report.md`; a session restart was required before c142 (per the resume notes). This is an integrator-phase agent-def change and does not affect the D1 cross-cutter dispatch, but is noted so the orchestrator confirms the restart landed before the integrate phase.
