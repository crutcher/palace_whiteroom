---
agent: integrator-finalize
cycle: cycle-121
batch: batch-39
batch_position: 1/3 (OPENER)
timestamp: 2026-06-07T054924Z
kind: integration
reports_consumed: 9
reports_applied: 9
reports_deferred: 0
reports_rejected: 0
gate_hits_total: 0
finalize_build_repairs: 1
integration_commit: ae2e2f4
---

# integrator-finalize — cycle-121 (batch-39, position 1/3, THE OPENER)

The **lift-through campaign opener** — the wide all-fronts fan-out that breaks the batch-36/37/38 plateau, enacting the 2026-06-07 RE-SCOPE (DIRECTIVE-1/2/3). 9 dispatches, ALL applied clean. One atomic commit; two-phase SHA patch follows.

## Summary

The first cycle of the lift-through campaign. The LEAD landed the **geometric-multigrid preconditioner** feature column (THE highest-fan-out lift-through consumer, DIRECTIVE-2 consumer-(1)), which grounds RE9/RE1/RE5/RE7. **RE10 was DISCHARGED**, the **constructive-kernel frontier OPENED** (3 roadmap_goal kernel-impls under DIRECTIVE-3), and the **AMR front OPENED** (DIRECTIVE-2 consumer-(2)). The graded-stack `reachable` total jumped **139 → 156 (+17)** — the largest single-cycle reachability jump of the campaign; the plateau is broken.

Build EXIT 0 after one surgical build-repair. `rank_violations: 0` (gate passes). 9/9 staging rows == 9 dispatched-ready (102nd consecutive clean staging).

## Reports consumed

| # | report (scope) | status | overall_status route | follow_up_agent | landing |
|---|---|---|---|---|---|
| D1 | layer-intro-author — geometric-multigrid-preconditioner (LEAD) | applied | needs-revision (sanctioned integration-sequencing exception; D3 forward-ref already landed) | integrator-per-report | GMG L4+L1 columns rough-in + Infrastructure group-intro |
| D3 | harvester — multigrid-relaxation-smoother | applied | ready (repaired) | — | `L1/multigrid-relaxation-smoother` FIRM (kernel-impl) + triangular-solve kernel-api role-label |
| D2 | layer-intro-author — fe-space-hierarchy-concepts-page | applied | ready | — | `concepts/FiniteElementSpaceHierarchy.md` firm + `fe_space_hierarchy` §Record-def trim |
| D9 | layer-intro-author — waveguide-mode-drift-cleanup | applied | ready (critic direct) | — | waveguide-mode `.L0`/index maturity drift cleanup; feature-column firm 12→13 |
| D8 | layer-intro-author — re10-interpolator-ground | applied | ready (critic direct) | — | RE10 DISCHARGED — `L1/interpolator` grounded via 2 `depends-on (uses)` edges |
| D4 | abstractor — libceed-quadrature-kernel-impl | applied | ready (critic direct) | — | `L1/libceed-quadrature-kernel-impl` roadmap_goal (DIRECTIVE-3 dual-surface) |
| D5 | abstractor — eigsolve-kernel-impl | applied | ready (repaired) | — | `L3/eigsolve-impl` + `L3/lanczos_step` roadmap_goal (DIRECTIVE-3) |
| D6 | combinator-miner — kernel-shared-substrate | applied | ready (critic direct) | harvester (replace-and-propagate) | `L2/correction_step` rough-in dep-map row |
| D7 | abstractor — amr-estimate-mark-refine | applied | ready (repaired) | — | `L1-L0/amr-estimate-mark-refine` rough-in theme + 2 L1 rough-in verb rows |

All 9 applied cleanly. Zero deferrals, zero rejections.

## Artifact changes (aggregate, from staging Files-touched)

**New files (9 book chapters/pages):**
- `book/src/L1/multigrid-relaxation-smoother.md` (firm, kernel-impl)
- `book/src/feature/geometric-multigrid-preconditioner.L4.md` + `.L1.md` (rough-in)
- `book/src/feature/infrastructure.md` (group-intro, NEW 4th feature sub-kind)
- `book/src/concepts/FiniteElementSpaceHierarchy.md` (firm record page)
- `book/src/L1/libceed-quadrature-kernel-impl.md` (roadmap_goal)
- `book/src/L3/eigsolve-impl.md` (roadmap_goal) + `book/src/L3/lanczos_step.md` (roadmap_goal)
- `book/src/L1-L0/amr-estimate-mark-refine.md` (rough-in theme)

**Edited files:**
- `book/src/L1-L0/triangular-solve-obstruction.md` + `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` + `book/src/L3/eigsolve.md` — `kernel-api` role-labels (DIRECTIVE-3; all KEEP their obstruction/partial-obstruction status)
- `book/src/L1/fe_space_hierarchy.md` (§Record-def trim + back-link), `book/src/L1/divfree-projector.md` + `book/src/L4/waveguide_mode_reduce.md` (RE10 interpolator edges)
- `book/src/feature/waveguide-mode.L0.md` + `book/src/feature/output-product.md` + `book/src/feature/index.md` (D9 drift cleanup + D1 GMG matrix row)
- `book/src/L2/index.md` (correction_step row), `book/src/L3/index.md`, `book/src/L1/index.md`, `book/src/L1-L0/index.md`, `book/src/SUMMARY.md` (the 9-chapter registrations + dep-map rows, all alpha-within-kind)

**Finalize build-repair:** `book/src/L3/eigsolve-impl.md` — two dead `[lowering-verifier](../../README.md)` links de-linked to plain inline-code (the root README.md was deleted batch-31; `lowering-verifier` is a pipeline agent role with no in-book chapter target; de-link fallback, NOT stub-creation — an agent role is not a clearly-implied spec component).

## Safety-net gate results (aggregated)

- **retroactive-budget global = 0** (no report carried retroactive per-slice claims; D6 explicitly 0). PASS.
- **rank linter (Axis 1): `rank_violations: 0`** on the landed tree. Baseline fully discharged c096 → ANY violation would be NEW and BLOCK; there are NONE. **GATE PASSES.** Every new firm/rough-in node rests on ≥-its-rank `depends-on` deps; the 3 roadmap_goals rest-on-anything vacuously.
- **reachability GC (Axis 2): NO newly-orphaned node** — `reachable` CLIMBED 139→156. The 3 intentional `[GARBAGE*]` roadmap_goal kernel-impls are grounded-future per DIRECTIVE-3 + `feedback_gc_ground_dont_remove_future_deps`, NOT orphaned. Second block-condition does NOT fire. **GATE PASSES.**
- **commit atomicity** — single commit (book + scaffolding + log + reports + staging + consumed-report frontmatter). PASS.
- **consumed-report frontmatter integrity** — 9 `integrated_at` touches applied (see below). PASS.
- Per-report gates (citecheck, edge-label, realizes-kernel-api edge-class, append-on-missing-slug, SUMMARY-registration, alpha-position) all PASS across the 9 reports (per the staging rows).

## Build status

`cargo make book` (mdbook + linkcheck2 0.12.0): initial EXIT 105 (two `File not found: ../../README.md` linkcheck errors in the new `L3/eigsolve-impl.md`); after the surgical de-link build-repair, **EXIT 0**. All 9 new chapters + their SUMMARY/index inserts resolve. Only pre-existing benign `Potential incomplete link` / `j+1` KaTeX-adjacent WARNs remain.

## Graded-stack linter (step-5b, on the landed tree)

```
files=378 (+9)   typed=317 (+9)   untyped=61 (HELD)   roots=41 (+2)
reachable=156 (+17)   rank_violations=0 (HELD)   unresolved_depends_on_targets=6
promotion_frontier=11
detritus=123 (−9)
  detritus_no_typed_edges_pre_p1_artifact=101
  detritus_with_typed_edges_stronger_signal=22 (−5)
  expected_unreachable_outside_dag=47
rank_histogram: firm=218 typed-no-rank=82 roadmap_goal=3 rough-in=5
                partly-constructive=3 obstruction=2 partial-obstruction=4
```

`unresolved_depends_on_targets` (6, all WARNING-non-strict declared-future deps, linter exit 0):
- `L1/libceed-quadrature-kernel-impl` → `element_restrict` / `basis_apply` / `quad_point_contract` / `geom_factor_build` (4 substrate ops, the D6/D4 shared-substrate harvest targets)
- `L1-L0/amr-estimate-mark-refine` → `dorfler_mark` / `flux_recovery_estimate` (the 2 AMR rough-in verbs)

**RE-DISCHARGE DELTAS (the central signal for the c122 RE-recheck + the batch-39 meta):**
- **RE10 = DISCHARGED** — `L1/interpolator` LIVE (inbound: divfree-projector, multigrid-relaxation-smoother, waveguide_mode_reduce + the construction-rotation theme, which is transitively live). Off the STRONGER garbage list.
- **RE9/RE1/RE5/RE7 = GROUNDED** — the GMG column composes `fe_space_hierarchy`(RE9)/chebyshev+jacobi-smoother(RE1)/normalize(RE5)/reciprocal(RE7) as firm `depends-on`; `L1/fe_space_hierarchy` LIVE via both GMG levels. Under DIRECTIVE-2 the RE set is a discharge target, not a floor.
- **CONSTRUCTIVE-KERNEL FRONTIER OPENED** — 3 roadmap_goal kernel-impls grounded-future, awaiting c122 consumers + the D6 shared-substrate harvest.

**Trend:** `rank_violations` HELD 0 (22 c094 → 0 c096 → … → 0 c120 → 0 c121); `reachable` 36 → … → 139 → 139 → **156 (+17, plateau BROKEN)**; STRONGER 27 → 22.

## Wave-conflict observations

- **The intentional D3→D1 serial apply-order worked exactly as designed.** D3 integrated FIRST so D1's GMG forward-`depends-on` resolves; `L1/multigrid-relaxation-smoother` was transiently `[GARBAGE*]` after D3's apply (only a `reference` consumer) and flipped LIVE the moment D1's hard `depends-on` edges landed. Confirmed at finalize.
- **Shared-file `feature/index.md` (D1 + D9) — no collision.** D1's NEW Infrastructure grouping + GMG matrix row (after the waveguide-mode row) vs D9's waveguide-mode-row + firm/seed-prose edits were byte-disjoint; the 12→13 firm-count arithmetic was reconciled (GMG is a SEPARATE rough-in Infrastructure kind, participating in neither the feature-column firm split nor the seed split).
- **Shared-node `L1/fe_space_hierarchy` (D1's RE9 edge vs D2's promotion) — no double-registration.** D1 authored the RE9 `depends-on` in GMG frontmatter; D2 added only a `reference` back-link + the §Record-def trim. D2's Part-1 was VERIFY-ONLY.

## Open questions promoted (aggregated — 32 across the 9 reports, by the per-report integrators)

Routed to `scaffolding/open-questions.md`. Highest-leverage for c122 / the batch-39 meta:
- `record-FiniteElementSpaceHierarchy-promote-watch-wording-reconcile` — the c118 watch said "2nd FIRM consumer"; GMG landed rough-in; D2 promoted under the live "≥2 consumers" rule. Reconcile.
- `geometric-multigrid-preconditioner-rough-in-promotion-smoother-leg-gated` + `record-MultigridConfig-needs-definition-home` + `vcycle-level-recursive-combinator-mining-candidate` (D1).
- `eigsolve-impl-c122-consumer-wiring-grounding-trigger` (RE3/RE8) + `libceed-quadrature-kernel-impl-reachability-grounding-confirm` (the intended grounded-future, confirm-not-swept).
- The DIRECTIVE-3 `realizes-kernel-api` correspondence-audit cohort (lowering-verifier): `multigrid-relaxation-smoother-lowering-verifier-realizes-kernel-api-audit` + `libceed-quadrature-kernel-impl-realizes-api-faithfulness-audit` + `eigsolve-impl-lowering-verifier-correspondence-audit`.
- `amr-estimate-mark-refine-theme-firmness-gate` (harvest `dorfler_mark` + `flux_recovery_estimate`) + `correction-step-replace-and-propagate-scope` (D6→harvester).
- `interpolator-re10-discharge-c122-linter-re-measure` (the authoritative STRONGER-delta re-measure is the c122 planner's standing RE-recheck).

## Next-cycle priorities (c122, batch-39 position 2/3)

1. **WIRE THE CONSUMERS** — the constructive-kernel consumers + the D6-routed shared-substrate ops (`element_restrict`/`basis_apply`/`quad_point_contract`/`geom_factor_build` for libceed; the eigsolve-impl consumer for RE3/RE8) that FIRE the roadmap_goal grounding triggers + the remaining RE promotion conditions. (resolves the 6 `unresolved_depends_on_targets`)
2. **HARVEST the AMR verbs** (`dorfler_mark`, `flux_recovery_estimate`) to firm the `amr-estimate-mark-refine` theme.
3. **RE-RECHECK** — the standing RE1-RE10 baseline re-measure (RE10 discharged, RE9/RE1/RE5/RE7 grounded; the c122 planner re-runs `--show-inbound` to authoritatively confirm).
4. The GMG rough-in→firm promotion gate (smoother-leg-gated) + the `FiniteElementSpaceHierarchy` promote-watch reconcile.
5. The DIRECTIVE-3 `realizes-kernel-api` correspondence-audit cohort (lowering-verifier).
6. `MultigridConfig` record page + the V-cycle recursive-combinator mine + `correction_step` chapter formalization (replace-and-propagate).

## Process

- 9/9 staging rows == 9 dispatched-ready (the cycle-018 staging-completeness gap did NOT recur; 102nd consecutive clean staging).
- 1 finalize build-repair (the README de-link — a de-link, not a stub); 0 implied-component stubs created.
- The staging log was authoritative this cycle (rows == dispatched; no reconciliation-from-working-tree needed).
- Single atomic commit + push; two-phase SHA patch follows (step 13 canonical pattern).
- NO `.claude/agents/` changes from this finalize.
