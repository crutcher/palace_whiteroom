---
agent: cycle-planner
invoked_at: 2026-06-07T022759Z
scope: cycle-119 dispatch plan
status: pending
---

# Cycle 119 dispatch plan

## Goals selected this cycle

Batch-38's substantive frontier (the MESH→FE_SPACE substrate lowering + grounding campaign) was **consumed in full by c118** — the 3 L1>L0 construction-rotation themes, the `build_mesh` lifecycle-L1 GROUND edge, the `waveguide_mode_reduce` L4 verb + column promotion, and the record-definition cohort all LANDED. Examining the c118-surfaced tail against the deliverable-presence + trigger checks below, the honest state is: **batch-38 has wound down to its grounding/honest-typing tail** — the remaining items are either (a) ONE clean faithful GROUND-check edge whose trigger fired (the lifecycle.L4 sibling), or (b) trigger-gated work whose trigger has NOT fired (the waveguide-mode field-map L1 homes; the `FiniteElementSpaceHierarchy` concepts-page promote), or (c) one mechanical citation-over-range hygiene fix. Per the redirect's STOP-PROPOSING posture I do **not** manufacture a forced forward-frontier pick. This cycle plans the honest available work: the faithful `lifecycle.L4 → L1/build_mesh` GROUND edge (mirroring c118 D4's L1 disposition; the OQ trigger fired) + the small `interpolator.cpp:282-310`→`:282-306` over-range hygiene fix. Two small, faithful, in-scope dispatches; not padded. This is a deliberate low-fan-out tail cycle (the c115 plateau-posture precedent for a valid small cycle), positioning the batch-38 meta-phase (after c120) to confirm the plateau.

## Linter baseline (c118 finalize, re-confirmed on disk this plan)

`files=369, reachable=139, roots=39, detritus=132, STRONGER=27, rank_violations=0, untyped=61, promotion_frontier=6, expected-unreachable=46`.
Re-run on disk this cycle: matches exactly. `build_mesh` is **NOT in detritus** (D4 grounded it via `lifecycle.L1`) — so the D1 edge below is honest-typing/faithfulness, NOT a reachability flip.

## Deliverable-presence verification

### D1 — `feature/lifecycle.L4 → L1/build_mesh` GROUND edge (the c118 D4-surfaced OQ)
1. **File existence:** `ls book/src/feature/lifecycle.L4.md` → `book/src/feature/lifecycle.L4.md` EXISTS (10304 bytes).
2. **Maturity / already-discharged:** `grep rank:/feature_root:` → `feature_root: seed`, `rank: firm` (line 5/6). The column is a firm spine-ROOT. **Already-carries-edge check:** `grep -c 'target: L1/build_mesh' book/src/feature/lifecycle.L4.md` → **0** (the edge does NOT yet exist — NOT a no-op; dispatch is genuinely open). Current `depends-on` targets: `L4/fold_solve` (composes) + the two `cites-evidence` + `concepts/config-record` (uses-record) — NO `build_mesh`/`fe_assemble`/`ksp_solve` edge, unlike the now-grounded `lifecycle.L1` (which carries `L1/build_mesh`, `L1/fe_assemble`, `L1/ksp_solve`, `L4/fold_solve`).
3. **OQ-ledger RESOLVED-grep:** `grep -c 'lifecycle-l4.*RESOLVED\|lifecycle-l4.*CLOSED' scaffolding/open-questions.md` → **0** (OQ `lifecycle-l4-sibling-analogous-unground-build_mesh-edge` at line 1591 is OPEN; trigger = "a layer-intro-author GROUND-check pass on `feature/lifecycle.L4.md`" — exactly this dispatch).
4. **Structural-block check:** NOT blocked. The faithful target is **on disk** (`L1/build_mesh.md` firm, homed c117, grounded reachable c118). **Cross-layer-composes precedent exists and is firm:** `energy-fields.L4` carries `depends-on → L1/participation_ratio` + `L1/matrix-weighted-norm` (kind: folds) — an L4 feature column legitimately composes an L1 op when no L4 form exists. `build_mesh` has no L4 node (mesh construction does not reshape at L4), so the L4 lifecycle-ROOT genuinely composes the L1 op. Rank: `lifecycle.L4` firm(3) → `L1/build_mesh` firm(3), `rank(u) ≤ rank(v)` = 3≤3 HOLDS. The dep-map row 67 currently masks the genuine constituent as "— (L0 scaffold)" — the edge makes it faithful, matching the L1 disposition.

### D2 — `interpolator-construction-rotation.md` `:282-310`→`:282-306` over-range hygiene fix (c118 integration-tooling flag)
1. **File existence:** `ls book/src/L1-L0/interpolator-construction-rotation.md` → EXISTS.
2. **Maturity:** `grep rank:` → `rank: firm` (line 5). Firm theme; the fix is a mechanical citation trim, not a maturity change.
3. **OQ-ledger:** no OQ slug; the item is a c118 integration-tooling flag ("the `interpolator.cpp:282-310` ~3-line over-range … a producer/critic `--anchor` concern … flagged for a future citation-hygiene `--anchor` sweep").
4. **Structural-block check:** NOT blocked. **Codemap-verified the exact bound this plan:** `read_range interpolator.cpp 300-312` shows the point-list `InterpolateFunction` body closes at `}` on **line 306** (the `#endif` is :305, `}` :306); `ComputeLineIntegral` begins at :308. So `:282-310` over-runs by ~4 lines into the next function. The faithful range is `:282-306`. The over-range appears in the theme at **line 181** (`body \`interpolator.cpp:282-310\``) and **line 238** (`+ \`:282-310\``). Both are the same point-list-body citation — non-load-bearing (passing bounds with exact internal anchors), so this is hygiene, not a correctness gate.

**STOP-PROPOSING negative-list check:** neither D1 nor D2 touches any disqualified vocabulary slug (`lu_solve`/`back_solve`/`ls-update-column`/`nleps_*`); both are grounding/hygiene on already-firm feature/theme files, not forced rectangular vocabulary pull-up.

## Trigger-gated items examined and CORRECTLY DEFERRED (not dispatched — trigger has NOT fired)

- **`waveguide-mode-reduce-field-map-l1-homes` (c118 D5 OQ, OPEN):** the per-mode field maps (`ApplyVDBackTransform`, `ComputePoyntingPower`, discrete-curl `Bz` via `GetDiscreteInterpolator`) lack dedicated firm L1 homes. **Trigger = "a recurrence of the discrete-curl / VD-back-transform / Poynting maps in another pipeline."** On-disk check: `grep -rln 'GetDiscreteInterpolator\|discrete.curl'` over L1/L3/L4 → only `interpolator.md` / `fe_space_hierarchy.md` / `waveguide_mode_reduce.md` (the same boundary-mode/interpolator cohort) — **NO cross-pipeline recurrence.** The verb is firm regardless (firm-on-positive-structure escape, the `eigsolve`-opaque-leaf pattern). DEMAND-GATED; do NOT dispatch.
- **`FiniteElementSpaceHierarchy` concepts-page promote-watch (c118 D6 / `record-FiniteElementSpaceHierarchy-promote-watch`):** in-chapter `## Record definition` at `fe_space_hierarchy.md:120`. **Trigger = a 2nd FIRM consumer surfaces.** On-disk check: mentions are confined to the FE-space construction cohort (the L1>L0 rotation themes + `fe_space`/`fe_collection`/index) — these are lowering-prose mentions, not new firm operator consumers. **No 2nd firm consumer surfaced c118.** WATCH-GATED; do NOT dispatch (KEEP in-chapter).
- **`feature/higher → fe_space_hierarchy`/`interpolator` `depends-on` wiring (RE9/RE10 discharge):** the standing GC-ground-don't-remove follow-on. **Trigger = a faithful inbound consumer (geometric-multigrid preconditioner / divfree-projector / field-probe) lands and composes the node by name.** No such consumer exists on disk this cycle — forcing an edge would be an unfaithful pull-up (the redirect forbids it). RE9/RE10 stay baseline-excepted; do NOT dispatch. (Note for the batch-38 meta after c120: the STRONGER 24→27 climb is fully RE9/RE10-attributed [expected], per the c118 finalize.)

## Dispatches

| # | agent | scope | deps | rationale |
|---|---|---|---|---|
| **D1** | `layer-intro-author` | **`feature/lifecycle.L4` GROUND-check + faithful `build_mesh` edge.** Add `depends-on: { target: L1/build_mesh, kind: composes }` to `feature/lifecycle.L4.md` frontmatter (mirroring `lifecycle.L1`'s grounded disposition; precedented by `energy-fields.L4 → L1/participation_ratio`). Update the §"Constituent down-links" dep-map row 67 (currently "— (L0 scaffold)") to a live `[`build_mesh`](../L1/build_mesh.md)` link reflecting the genuine composes edge, and tighten the §"The composition" / stage-(1) prose to cite the firm L1 op now that it exists. Single-file edit. Rank: `lifecycle.L4` firm(3) → `L1/build_mesh` firm(3), 3≤3 HOLDS. **NOTE this is honest-typing, NOT a reachability flip** — `build_mesh` is already reachable via `lifecycle.L1`; report only the standalone delta (likely reachability-NEUTRAL; finalize re-measures the authoritative cumulative on the landed tree). | none | Discharges the c118 D4-surfaced OQ `lifecycle-l4-sibling-analogous-unground-build_mesh-edge` (priorities batch-38 item; the §2f GROUND-don't-remove faithful-edge disposition). The one clean faithful pick whose trigger fired. **fan-out: LOW** (faithfulness/honest-typing of the L4 sibling — no reachability movement since the L1 column already grounds build_mesh). |
| **D2** | `lowering-verifier` | **`interpolator-construction-rotation.md` citation over-range hygiene.** Trim the point-list-body citation `interpolator.cpp:282-310` → `interpolator.cpp:282-306` at both occurrences (line 181 `body \`interpolator.cpp:282-310\``; line 238 `+ \`:282-310\``). Codemap-verified bound: `InterpolateFunction` point-list body closes `}` at :306; `ComputeLineIntegral` begins :308 — the `-310` over-runs by ~4 lines into the next function. Verify each trimmed anchor against the on-disk source (the `--anchor` check) and confirm no other claim in the theme depends on the over-run lines. Mechanical, non-load-bearing (per c118 critic). | none | Closes the c118 integration-tooling citation-hygiene flag (`interpolator.cpp:282-310` over-range). Routed to `lowering-verifier` (audit-against-evidence is its job — it confirms the trimmed range still supports every claim). **fan-out: LOW** (citation hygiene; no structural change). |

## Overlap analysis

**D1 ↔ D2:** NON-OVERLAPPING → PARALLEL.
- **Distinct files:** D1 edits `book/src/feature/lifecycle.L4.md` only; D2 edits `book/src/L1-L0/interpolator-construction-rotation.md` only. Disjoint paths.
- **No shared operator name / no forward-reference:** D1's edge target (`L1/build_mesh`) is on disk and firm — D1 does not author it and does not reference D2's slug; D2 does not touch any operator D1 names. No canonical-slug coordination needed (no new slug is created this cycle).
- **No shared running-count / consolidated tally:** neither touches a layer index's consolidated Working-Notes count, a `feature/index.md` matrix cell, or a §Vocabulary-cohort tally. D1 touches `feature/lifecycle.L4.md` frontmatter + its own dep-map + prose (self-contained); the `feature/index.md` lifecycle cell already reads firm (the column was firm pre-cycle) and needs no bump. The parallel-blind-shared-index guard does NOT apply (no ≥2-landing-into-one-index situation).
- **No floor-landing / adjacent-reanchor coupling:** neither lands an L_n floor under a firm L_{n+1} entry; the floor-landing-implies-reanchor guard does not apply.

No genuine overlap exists. Both are single-file, self-contained edits.

## Sequencing schedule

**Wave 1 (parallel — both dispatches, no inter-dependencies):**
- D1 (`layer-intro-author`, `feature/lifecycle.L4` GROUND edge)
- D2 (`lowering-verifier`, `interpolator-construction-rotation` over-range hygiene)

One wave. Then: 2 critics (parallel) → repairers as needed → `integrator-per-report` ×2 (serial apply-order, integrator's choice) → ONE `integrator-finalize` (rebuild book + linter step-5b re-measure + commit + push). No forward-reference ordering between the two dispatches, so no wave-2.

## Open questions / caveats

- **This is an honest low-fan-out tail cycle.** Batch-38's substantive frontier was consumed by c118; the c118-surfaced tail is mostly trigger-gated (the waveguide field-map homes + the `FiniteElementSpaceHierarchy` promote + the RE9/RE10 inbound-consumer grounding all await triggers that have NOT fired). I deliberately did NOT manufacture a forced forward pick (STOP-PROPOSING / no-forced-rectangular-pull-up). **Signal for the batch-38 meta-phase (after c120):** the project remains at the batch-36/37 plateau — reachability at its faithful floor (RE1-RE10 fully tracked, only promotion-triggered movement left), the forward-vocabulary frontier exhausted, and now the feature-front demand-gate (fired by directive-B for the all-fronts set) substantially LANDED across c117/c118. The remaining honest movement is (a) trigger-gated grounding (no trigger fired) and (b) hygiene. The meta-phase should weigh whether to (i) re-confirm the plateau + record RE9/RE10's STRONGER 24→27 attribution, (ii) bundle the carried linter-maintenance ask-class items (`--show-stronger` flag; `graded-stack-prose-status-inference-masks-untyped`; `plateau-probe-linter-roots` re-measure to 39; the `semantics/index` matcher note) into a `tools/`-code change cycle, and (iii) surface the now-confirmed terminal-plateau to the human.
- **D1 is reachability-NEUTRAL by my projection** (build_mesh already reachable via lifecycle.L1). If D1's producer reports a reachability *delta*, that is a measurement error to flag — the only legitimate movement would be if `lifecycle.L4` itself were previously unreachable (it is a feature ROOT, so it is reachable by construction). The finalize step-5b re-measure on the landed tree is the authoritative number; I expect `reachable` HELD 139.
- **Optional consolidation if the orchestrator prefers a 1-dispatch cycle:** D2 is a 2-line citation trim and could fold into a future `--anchor` citation-hygiene sweep (the c118 flag explicitly said "if one runs"). I included it as its own small dispatch because it is cheap, in-scope, and clears the only standing hygiene flag — but it is droppable without affecting the substantive D1 pick. I did NOT pad beyond these two.
- **YAML-hygiene flag carried from c118** (producer report-frontmatter): noted for producer awareness; not a dispatch item (it is a report-authoring hygiene reminder for whichever producers run this cycle, not artifact work).
