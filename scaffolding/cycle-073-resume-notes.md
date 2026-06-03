# Cycle-073 resume notes (SESSION RESTART REQUIRED before cycle-073)

The batch-22 meta-phase (post-cycle-072 finalize; cycles 070/071/072) edited **4 `.claude/agents/` role-spec files + CLAUDE.md**. The parent orchestrator **must restart the Claude Code session before dispatching cycle-073**, so the new agent definitions (and the CLAUDE.md §Extraction-goal feature-spine description) are loaded (per friction-ledger `new-agent-defs-need-session-restart`). The restart also resets the primary conversation context (subsumes the retired per-meta `/compact` step — do NOT run `/compact`).

## What changed and why — the FEATURE-SURFACE SPINE role-spec codification (the headline GO)

The 2026-06-02 FEATURE-SURFACE SPINE directive (memory `project_feature_surface_spine`) routed its role-spec codification to the batch-22 meta-phase. The composition-root feature-surface chapter kind is now codified:

1. **`CLAUDE.md` §"Extraction goal — what the spec is for"** — added the **FEATURE-SURFACE SPINE** description (the top-down composition-root spine parallel to the bottom-up vocabulary: the feature set, the leaf-vs-meta-feature-ROOT sub-kinds, the uniform `seed` token, L4+L1+L0 levels, the flat `feature/<name>.{L4,L1,L0}.md` layout + high→low within-column ordering, run-in-parallel-by-fan-out priority).

2. **`.claude/agents/cycle-planner.md`** — added a §Discipline bullet: the FEATURE-SURFACE SPINE is a **co-equal standing goal — pick feature-surface work by fan-out**, interleaved with the bottom-up frontier (NOT necessarily the lead); clean-gated like any landing (constituents on disk, paste-inline-evidence); route to `layer-intro-author` (primary) / `harvester` (secondary); single-index-owner when ≥2 columns land; levels wired high→low.

3. **`.claude/agents/layer-intro-author.md`** — added the §FEATURE-SURFACE composition-root block (the PRIMARY authoring role) carrying the FULL convention: path/layout, SUMMARY Part placement, high→low level ordering (the deliberate alpha exception), the leaf-feature-column vs meta-feature/spine-ROOT sub-kinds (ROOT nests above leaves), uniform `status: seed`, the single-index-owner rule + read-only down-links, the boundary-mode = co-equal-leaf-column taxonomy. Also added a `feature surfaces / entry points` kind to the directive-3 kind-grouping note.

4. **`.claude/agents/harvester.md`** — added a §redirect-adjacent block: harvester is the SECONDARY feature-column author (a feature column is composition, not new operator algebra — layer-intro-author is the closer fit); points to the layer-intro-author §FEATURE-SURFACE for the full convention; status `seed`, cite the L0 driver range + constituent down-links as evidence.

5. **`.claude/agents/critic.md`** — added a §"Adapted checks for the FEATURE-SURFACE composition-root kind": **surface-or-evidence** adapts (evidence = L0 driver-source range + constituent down-links, NOT a single decomposed op); **rotation-quality** + **variant-axis-coverage** formally no-op (like a stub); **cross-reference-integrity** is load-bearing (the down-links + their maturity); the uniform `seed` status token (no qualifier).

This closes the OQs `feature-surface-kind-adapted-check-codification`, `feature-surface-part-path-layout-and-within-column-level-ordering-ratification`, `feature-surface-kind-batch-22-codification-and-seed-promotion-question` (incl. the `seed` / `seed (exemplar)` token sub-item), `feature-surface-meta-feature-root-sub-kind-and-summary-nesting`, and `boundarymode-is-sixth-problemtype-branch-reconcile-five-drivers-framing` (all CLOSED-by-this-meta-phase in the OQ ledger).

## Not agent-def edits (no restart needed for these, but landed this meta-phase)

- **`book/src/methodology/goal-flow.md`** — directive-4 GOAL+FLOW chapter refreshed with the batch-22 arc (both halves reach L4 across all 5 pipelines; the feature-spine note; the reorg). `cargo make book` exit 0.
- **`scaffolding/friction-ledger.md`** — `codemap-read-range-plus-one-drift-on-brace-boundary` last_observed→c072, recurrence HELD at 6 (batch-22 corroboration: c072 feature columns clean; `solve_family.md` §Specializations residue routed not fresh).
- **`scaffolding/priorities.md`** — reshaped into the CYCLE-073/batch-23 active head.
- **`scaffolding/open-questions.md`** — OQ unification (9 closed / 3 migrated / 4 kept-deferred).

## Cycle-073 frontier (from `scaffolding/priorities.md` CYCLE-073/batch-23 active head)

- **#1 LEAD (HIGH):** `shared-energy-reduce-combinator-mine` — mine the shared L4 `energy_reduce`/`gram_reduce` combinator (≥2-witness gate MET: electrostatic capacitance + magnetostatic inductance share the operator-weighted Gram `map`-then-`reduce`); replace-and-propagate into both feature L4 chapters.
- **#2 (MEDIUM-HIGH, the PARALLEL standing goal):** `feature-spine-scaling` — scale the feature spine by fan-out (the remaining driver columns eigenmode/driven/transient + the output-product feature surfaces + wave-port/boundary-mode). The **eigenmode column** is the first clean test of the `seed`→promote status-aggregation question (may compose only firm ops).
- **#3 (LOW/hygiene):** `solve-family-specializations-reanchor-hygiene` — re-anchor `L4/solve_family.md` §Specializations `:30/:35/:36`→`:29/:34/:35` + the `L4-L3/index.md` `integrator.hpp:58-61` bare-basename lint.
- **#4 (LOW, observation-routed):** `fold-solve-amr-second-witness-foldin` — a `fold_solve` lifter folds the AMR `SolveEstimateMarkRefine` loop in as the 2nd state-generated-fold witness.

The batch-23 meta-phase fires after cycle-075's finalize (cycles 073/074/075).
