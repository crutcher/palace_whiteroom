# Cycle-070 resume notes (SESSION RESTART REQUIRED before cycle-070)

The batch-21 meta-phase (post-cycle-069 finalize) edited **4 `.claude/agents/` role-spec files**. The parent orchestrator **must restart the Claude Code session before dispatching cycle-070**, so the new agent definitions are loaded (per friction-ledger `new-agent-defs-need-session-restart`). The restart also resets the primary conversation context (subsumes the retired per-meta `/compact` step — do NOT run `/compact`).

## Agent-defs changed and why

1. **`.claude/agents/meta-phase.md`** — added §"Standing book targets the meta-phase owns (user directives 2026-06-02)" before §"What you DO NOT do", and amended the first "What you DO NOT do" bullet to carve out the two standing book-write exceptions:
   - **directive-4** — the meta-phase now OWNS the `book/src/methodology/goal-flow.md` GOAL+FLOW chapter as a standing per-batch refresh target (non-authoritative synthesized mirror; source-wins-on-contradiction; refresh each batch with the arc).
   - **directive-3** — the meta-phase owns the one-time mdBook by-kind sub-chapter grouping + global alpha re-sort reorg (a dedicated structural wave) and codifies the convention into the producer specs.

2. **`.claude/agents/integrator-per-report.md`** — added an "Alphabetical-position insert (directive-3)" auto-fix bullet: new SUMMARY chapter entries and index dep-map/API rows go in **alpha position within the kind grouping**, NOT append-after-sibling (changes the prior append convention; alpha-local within cohort until the one-time reorg nests the Parts).

3. **`.claude/agents/integrator-finalize.md`** — added a sentence to the build-repair step: SUMMARY/index inserts at build-repair time (e.g. for stubs) go in alpha position within the kind grouping (matches integrator-per-report's convention).

4. **`.claude/agents/layer-intro-author.md`** — added a "By-kind sub-chapter grouping + alphabetical API/dep-map order (directive-3)" block: sort dep-map/API tables alpha-within-cohort; author the kind-group intro pages when the one-time reorg nests a Part (don't over-structure a Part with too few chapters); maintain alpha order on every list touch; execute the group-intro authoring + table sorting the meta-phase dispatches.

## Cycle-070 frontier (from `scaffolding/priorities.md` CYCLE-070/batch-22 active head)

- **#1 LEAD (HIGH):** `driven-solve-l4-lift` — author the driven pipeline's solve-half L4 form (the meta-phase-decided LIFT; the operator-varying frequency sweep through the firm `L4/assemble_frequency_operator`). Closes the last pipeline-half L4 gap.
- **#2 (MEDIUM, its own structural wave):** `directive-3-mdbook-reorg-wave` — the one-time by-kind sub-chapter grouping + global alpha re-sort (layer-intro-author-executed group intros + sorted tables).
- **#3 (LOW/hygiene):** `l3-dot-nrm2-no-l4-reanchor`.
- **#4 (LOW/cosmetic):** `blackbox-page-l4-fe-assemble-link-upgrade`.
- **#5 (deferred, primitive-gated):** `eliminate_*→L4`.

The batch-22 meta-phase fires after cycle-072's finalize (cycles 070/071/072).

## ⟢⟢ USER DIRECTIVE 2026-06-02 (NEW standing goal, recorded post-batch-21-meta) — FEATURE-SURFACE SPINE

Palace's high-level **entry-point features** (what Palace is *written for*) get **dedicated feature-surface chapters** — a TOP-DOWN composition-root spine **parallel** to the bottom-up vocabulary spine. Full def: project memory `project_feature_surface_spine`; priorities.md batch-22 banner + active-head item #6.

- **Feature set (all four):** (1) the 5 simulation drivers (electrostatic/magnetostatic/eigenmode/driven/transient); (2) the top-level lifecycle (`main`→`BaseSolver`: config→mesh→assemble→solve→postprocess→output); (3) output/postprocess products (S-params/capacitance/inductance/eigenfreq+Q/energy-fields); (4) wave-port/boundary-mode (`boundarymodesolver`).
- **Levels:** L4 + L1 + L0 each (L2/L3 only where the decomposition reshapes).
- **Priority:** run in PARALLEL (co-equal standing goal; interleave by fan-out — NOT a replacement frontier).
- **Cycle-070+:** active-head item #6 `feature-surface-spine-seed` is the first parallel pick (recommended exemplar = the electrostatic feature column at L4+L1+L0). The cycle-planner carries the directive via per-dispatch prompts until the **batch-22 meta-phase codifies** it into role-specs (cycle-planner + layer-intro-author/harvester) + CLAUDE.md §"Extraction goal" + the directive-3 kind list (adds a "feature surfaces / entry points" kind). NO new agent (incremental refinement default-accepted; new-role stays High).
- A feature chapter is a NEW chapter kind (composition-root): the critic's checks adapt (its "surface" IS the feature — evidenced by the L0 driver source range + the constituent-op links, not a single decomposed op).
