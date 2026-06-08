---
agent: cycle-planner
invoked_at: 2026-06-08T230323Z
scope: cycle-145 dispatch plan (batch-48 OPENER — maintenance-floor full-hygiene sweep)
status: pending
---

# Cycle 145 dispatch plan

## Goals selected this cycle

Cycle-145 is the **OPENER of batch-48** (cycles 145/146/147; meta after 147) and is run **AS the maintenance floor** per the human's direction ("resume with maintenance, drive through the meta"). The batch-47 FINALIZATION DE-BULK campaign is COMPLETE (all 284 `book/src/**` files de-bulked; baseline held; build EXIT 0); the maintenance floor (priorities.md item 1 `maintenance-floor-standing-hygiene`) is the standing surround, and the §CENTRAL ASK on the forward direction is pending the human (not the planner's to resolve). Per the batch-43 cadence codified in item 1, the OPENER fires the **once-per-batch full-hygiene sweep = at most ONE dedicated audit-class dispatch**; the per-cycle floor for c146/c147 is the `integrator-finalize` step-5b two-invariant tripwire (NO dedicated dispatch). **NO substantive producer frontier is dispatched** — every in-scope front is either landed (re-building = forbidden rectangular pull-up) or demand-gated with no consumer in flight; the in-scope FEATURE-SURFACE SPINE is L4-COMPLETE and the Synthesis VIEW is complete + correspondence-audited.

**This cycle = exactly ONE audit-class dispatch (the maintenance-floor full-hygiene sweep). NOT zero-dispatch** (the opener owns the once-per-batch sweep, which fired at the c142 opener of batch-46 and lands here for batch-48). c146/c147 are expected per-cycle-tripwire-only (zero producer dispatch), exactly as c143/c144 ran.

## Dispatches

**D1** — (`cross-layer-cross-cutter`, "batch-48 maintenance-floor full-hygiene sweep — the once-per-batch audit; NO `book/` mutation expected (audit-class, clean-bill or surface a finding)", deps: none)

Scope detail — run the standing per-batch sweep checklist (priorities.md item 1, the c142 D1 precedent is the working template) against on-disk state, and emit a CYCLE.md audit verdict ONLY (audit-class — no proposed-changes / no dep-map / no node/edge/rank/status move unless a genuine land-clean hygiene defect is found, in which case surface it as a finding for the next cycle, do NOT author a substantive frontier):

1. **RE-set re-check** — confirm the residual-live RE premises still HOLD: **RE4** (GMRES running-QR ILS view, consumer-gated) + the **sharding-node §2g-extension member** (`sharding-decompose-reduce` solve-generalization, consumer-gated, DIRECTIVE-1 MPI/distributed OUT) + the **RE11** deliberate reference-only-reachable cohort (§2g-accounted by design, incl. the synthesis `expected_unreachable_outside_dag` chapters). Confirm the **`eigsolve-impl` promotion gate is NON-FIRING** (arm-A positive-structure structurally unsatisfiable in `palace/` — MINRES enum-only-stub; arm-B blocking-consumer not in flight; `lanczos_step` + `eigsolve-impl` stay co-`roadmap_goal`).
2. **Semantic-surface liveness refresh** — confirm `book/src/semantics/index.md` §0.1 active-management discipline intact, untyped-by-design, no source contradiction; a maintenance batch authored NO new vocabulary so expect NO new restatement cohort. The 27-file restatement cohort (OQ `named-shape-groups-general-rule-restatement-cohort-extent`) remains the governed surface; confirm no new restatement detritus introduced by the finalization campaign's prose edits.
3. **Opportunistic detritus / edge-typing GC** (`p1-edge-typing-true-detritus-sweep`) — confirm `true_detritus` 51 / `detritus` 123 HELD; the cohort is dominated by the GMG/AMR + eigsolve-impl/NLEPS consumer-gated false-detritus that GROUND-don't-remove (collapses only when a blocking consumer wires in). Surface any GENUINELY-removable true-detritus as a finding; do NOT remove future-deps of goal nodes (ground-don't-remove invariant).
4. **Kernel-API/impl integrity check** (DIRECTIVE 3) — confirm the 3 (×4 instances) `realizes-kernel-api` edges stay `reference`-class on-disk: `eigsolve-impl` ×2 (L3 + L4 eigsolve), `libceed-quadrature-kernel-impl`, `multigrid-relaxation-smoother`; the Synthesis `#extern` leaves trace to the kernel-API nodes.
5. **DIRECTIVE-1 boundary** — confirm no sharding/MPI work was lifted as active; the MPI-associated version stays OUT.
6. **Graded-stack baseline confirmation** — confirm the on-disk tripwire baseline matches the post-batch-47 (post-data-algebra-reconcile) terminal: `files 392, typed 331, untyped 61, roots 45, rank_violations 0, unresolved_depends_on_targets 0, promotion_frontier 11, detritus 123, true_detritus 51, reference_reachable 72, expected_unreachable 54`. Both hard invariants (`rank_violations 0`, `unresolved 0`) hold. **NOTE the deliberate baseline move from batch-46:** `promotion_frontier 12→11` and `stub 1→0` (the batch-47 `synthesis/data-algebra.md` `stub`→`navigational-container` reconcile); this is the EXPECTED current baseline, not a regression.

Rationale: this IS priorities.md item 1 `maintenance-floor-standing-hygiene` (plan-tag `graded-stack-hygiene`, fan-out LOW/hygiene), the no-regret standing default while the §CENTRAL ASK is pending the human. Routing to `cross-layer-cross-cutter` follows the c142 D1 / batch-45 c139 D6 precedent (the cross-cutter is the audit-class role that runs the whole-artifact integrity sweep without authoring).

**Deliverable-presence verification:** D1 is **audit-class, open by construction** — it resolves to NO named `book/src/<slug>.md` deliverable (it emits a CYCLE.md audit verdict + at most a finding; the expected outcome is a CLEAN BILL with NO artifact mutation, exactly as c142 D1). The four-step deliverable-presence sequence is therefore N/A (no slug to stat / grep / OQ-RESOLVED-check / structural-gate). The STOP-PROPOSING negative-list is N/A (no operator authored). The framing is correctly **audit-first** (this is the canonical audit-class dispatch, not a reflexive harvest). Skip is explicit: open by construction (audit-class, no prior-cycle deliverable to be already-discharged).

## Overlap analysis

Single dispatch — no pairwise overlap to analyze. D1 touches NO `book/` artifact region and names NO operator (it is a read-only integrity sweep emitting a CYCLE.md verdict). It cannot conflict with anything because there are no wave-mates and no proposed-changes.

## Sequencing schedule

**Wave 1 (the only wave):** D1 (`cross-layer-cross-cutter`, maintenance-floor full-hygiene sweep).

Pipeline: D1 → critic (8-check) → repairer iff a finding → (if D1 surfaces a genuine artifact defect) integrator-per-report ×≤1 → integrator-finalize ×1 (rebuild + step-5b two-invariant tripwire + step-5c KaTeX assertion + step-5d frontmatter-render guard + commit/push). The EXPECTED outcome is CLEAN BILL with NO integrator-per-report (no STAGING row), exactly as c142.

## Open questions / caveats

- **c145 is a 1-dispatch hygiene-sweep OPENER, NOT zero-dispatch.** The opener owns the once-per-batch full-hygiene sweep (D1). c146 and c147 are expected **per-cycle-tripwire-only (zero producer dispatch)** — their planners should honestly dispatch nothing absent a recorded-but-unfixed land-clean hygiene nuance, exactly as c143/c144 ran in batch-46 (the once-per-batch sweep already fired at the opener; re-running it mid-batch is not the cadence).
- **The §CENTRAL ASK (forward direction) is the human's to set and is OUT of the planner's authority.** The human directed "resume with maintenance, drive through the meta," so batch-48 runs as the maintenance floor; the meta-phase after c147 will surface the §CENTRAL ASK a SEVENTH time (the meta-phase recommendation has been (C) downstream-burn handoff). The planner dispatches NO substantive frontier this batch — re-building the landed GMG/AMR fronts is a forbidden rectangular pull-up, and the gated fronts (RE4, sharding solve-generalization, eigsolve-impl kernel-impl arm) have no consumer in flight.
- **Deferred-cosmetic carry (not a dispatch):** the pre-existing `L2/index.md` fold-cohort KaTeX `\acc`-in-`$`-span render WARN persists (cosmetic, predates the finalization campaign, table-cell not `<pre>` so the step-5c assertion does not trip). NOT worth a producer dispatch; recorded for the meta-phase. If D1's sweep wants to note it, it may, but it is below the bar for a repair.
- **Next-meta-phase codification carry (from cycle-145-resume-notes.md, landed out-of-band — NOT this cycle's work):** the 2 finalization skills (`finalization-debulk`, `heading-metadata-hygiene`), the producer re-accretion discipline, the legal-identifier chapter-naming convention, the frontmatter-render fix as a build invariant (step-5d guard candidate), and the `## Status`-as-sole-rank-carrier subtlety all want proper folding into CLAUDE.md + role-specs at the batch-48 meta-phase. These are meta-phase intake, not planner dispatch — flagged here so the meta after c147 catches them.
