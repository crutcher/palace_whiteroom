---
agent: cycle-planner
cycle: cycle-139
batch: batch-45
position: 1/3 (LEAD/OPENER)
timestamp: 2026-06-08T053000Z
---

# Cycle 139 dispatch plan

**Position 1/3 of meta-batch-45 (cycles 139/140/141; meta fires after c141 finalize). The OPENER of the human-chosen (B) "ALL OF THESE" wide all-fronts shared-exploration fan-out.**

## Reshaping finding (human-ratified 2026-06-08)

The mandatory deliverable-presence sweep found that **fronts 1 (GMG) and 2 (AMR) are already substantially landed** (firm feature columns + firm leaves + RE9/RE1/RE5/RE7/RE10 discharged at batch-39, c121/c122); only **front 3 (eigsolve-impl)** has a real promotion path this batch (via its named blocker `lanczos_step`), and **front 4 (sharding-math)** is exploratory-only behind the hard gate. The human RATIFIED the intent-honoring plan: honor the directive's *intent* (shared-exploration lifting of the substrate the fronts share) via D1's shared-iteration-core mine, advance the genuinely-open fronts 3+4, do NOT re-build GMG/AMR (which would be re-proposing landed work + a forbidden rectangular pull-up).

Verification evidence on disk: GMG `feature/geometric-multigrid-preconditioner.{L4,L1}.md` both `firm` (promoted c122); `L1/multigrid-relaxation-smoother` firm; `L2/correction_step` firm; `L1-L0/amr-estimate-mark-refine` firm; RE9 "DISCHARGED-via-GROUND (c121 GMG)". `L3/lanczos_step` + `L3/eigsolve-impl` both `roadmap_goal` (open); `L4/sharding-decompose-reduce` rank-0 sketch (open, exploratory).

## Dispatches

**D1 — `combinator-miner`** · slug `iterate-while-basis-extension-shared-core`. Shared-iteration-core mine: `iterate_while_L3`-over-basis-extension across the GMG V-cycle recursion + relaxation-smoother GS sweep + eigsolve basis-extension loop. Read instances: GMG `vcycle` (`feature/geometric-multigrid-preconditioner.L1.md:39-49`), `L2/correction_step.md`, `L3/eigsolve-impl.md:65-83`, `L3/chebyshev.md`. VERDICT-FIRST replace-and-propagate OR finding (carry-shapes may genuinely diverge: basis-cols vs level-stack vs GS-color → no shared combinator warranted). Do NOT force a new V-cycle entry. deps: none. WAVE 1.

**D2 — `abstractor`** · slug `lanczos-step-toward-promotion`. Advance `L3/lanczos_step` against its on-disk positive structure (symmetric three-term recurrence; L0 home `L1-L0/minres-iteration`, cited `lanczos_step.md:24-25`). Tighten §Signature/§Semantics as band-3 specialization of firm `L3/krylov-step`, confirm `reorthogonalization` axis, state promotion gate explicitly. DIRECTIVE-3 / no-forced-pull-up: keep `roadmap_goal`/speculative unless MINRES L0 genuinely grounds to `stub`/`rough-in`. deps: none. WAVE 1.

**D3 — `abstractor`** · slug `sharding-decompose-reduce-solve-generalization-sketch`. Extend the rank-0 sketch with the per-sub-domain SOLVE generalization (additive-Schwarz; interface/overlap, partition-of-unity weighting). HARD GATES: stays rank-0 `roadmap_goal`; `reference`-class edges ONLY; MPI/distributed OUT (CITE-as-deferred only); if solve-generalization would re-root a firm reduce node → FINDING not forced sketch. deps: none. WAVE 1.

**D4 — `lowering-verifier`** · slug `eigsolve-impl-realizes-kernel-api-reaudit-lanczos`. Re-audit `L3/eigsolve-impl` (kernel-impl) ↔ `L3/eigsolve` (kernel-api, partial-obstruction), focused on the Hermitian inner-loop arm D2 advances. Confirm: `realizes-kernel-api` stays `reference`-class; kernel-api stays partial-obstruction undowngraded; no semantic restatement. Audit-class. deps: **D2**. WAVE 2.

**D5 — `layer-intro-author`** · slug `synthesis-residual-content-fidelity-followups`. The 3 LOW Synthesis content-fidelity follow-ups: (a) `L4/iterate-while-with-prev.md:233` stale `cg_solve` call → canonical boot/init/steady/cont order; (b) `L4/eigsolve.md:44`/`:97` `initial_state` → `initial_eig_state`; (c) `synthesis/types.md:38-44` add `units : Units` to `IoData` + widen cited-range comment. deps: none. WAVE 1.

**D6 — `cross-layer-cross-cutter`** · slug `maintenance-floor-batch-45-full-hygiene-sweep`. The once-per-batch full-hygiene sweep: graded-stack lint `--json` totals + RE-set premise re-check (RE4 / sharding-node §2g promotion-pull — D3 touches it / RE11 escalate-guard) + kernel-API/impl `realizes-kernel-api` integrity (3 edges stay `reference`-class) + semantic-surface liveness + DIRECTIVE-1 boundary (D3 live risk surface) + opportunistic detritus GC. Audit-class (OQ-append only). deps: none (placed wave 2 to read D1-D5 landings). WAVE 2.

## Sequencing

- **Wave 1 (parallel):** D1 · D2 · D3 · D5 (disjoint writes).
- **Wave 2 (parallel):** D4 (needs D2 on disk) · D6 (reads wave-1 baseline). One `integrator-finalize` at cycle-end.

## Linter baseline to carry (c138 finalize)

`files 392, typed 331, untyped 61, roots 45, reachable 163, reference_reachable 247, detritus 123, true_detritus 51, rank_violations 0, unresolved_depends_on_targets 0, promotion_frontier 12, expected_unreachable_outside_dag 54`. Both step-5b invariants MUST hold: `rank_violations == 0` and no newly-orphaned node.

## Caveats

- D2's lanczos promotion may NOT clear to `stub`/`rough-in` (MINRES L0 is enum-only-stub) → may stay `roadmap_goal` with sharpened gate (a finding, not a failure).
- D3 sharding is the live DIRECTIVE-1 boundary-risk surface — gates written into D3 scope; D6 verifies cited-not-lifted.
- c140/c141 forward: if D2 grounds `lanczos_step` and the eigsolve-impl condition fires, c140 carries an eigsolve-impl `roadmap_goal → stub` promotion + any D1-proposed shared-combinator propagation.
