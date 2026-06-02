# Cycle-58 resume notes (post-batch-17 meta-phase)

**SESSION RESTART REQUIRED before cycle-058.** The batch-17 meta-phase enacted role-spec changes to `.claude/agents/`. The parent orchestrator must restart the Claude Code session before dispatching cycle-058 so the new agent definitions load. The restart also resets the primary conversation context (subsumes the retired `/compact` step — do not run a separate compaction).

## Agent-defs changed (why the restart)

1. **`.claude/agents/lifter.md`** — NEW §Discipline bullet: when a re-anchor / firm-flip flips a chapter/theme `## Status`, the SAME proposed-changes pass must also update the matching `L*-L*/index.md` (or `L*/index.md`) row's status cell (or flag it for a co-dispatched count-owner). The lightweight promotion-time index-cell anti-drift guard. Addresses friction `index-table-status-cell-drifts-when-theme-file-promoted` (the c055 D7/D8 silent-drift incident).

2. **`.claude/agents/layer-intro-author.md`** — sharpened the count-owner survey bullet: count firm from each linked chapter's `## Status` line, **NEVER** from the drift-prone index-table cells (the c055 D7 mis-projection read `3 firm / 3 rough-in` off stale cells, forcing a corrective D8 lifter). Added a count-owner sub-bullet: the index cell flips together with the consolidated tally when the count-owner promotes.

Both edits codify the c056-D2-recommended promotion-time guard over a heavyweight finalize-time re-sweep. Same friction-ledger entry, recurrence-1, addressed.

## No other agent-defs changed

The 12 other agent definitions (cycle-planner, harvester, abstractor, combinator-miner, same-layer-cross-cutter, cross-layer-cross-cutter, lowering-verifier, critic, repairer, integrator-per-report, integrator-finalize, meta-phase) are UNCHANGED this batch.

## Cycle-058 frontier (already reshaped into the plan)

See `scaffolding/priorities.md` §CYCLE-058 / batch-18 active head (fan-out-ranked):
1. `fold-solve-promotion` (LEAD-if-gate-fires; the 2-fold-witness gate IS met — transient + SweepAdaptive's offline greedy phase) — full L4 `fold_solve` entry + L4>L3 lowering, a §3.7-`iterate_while`-child (NOT a new parent abstraction).
2. `weak-form-term-fe-cohort` — the genuinely-new FE differential-operator vocabulary; clean-gated (author only as a pipeline pull-up needs a non-diffusion term).
3. `map-solve-second-pipeline-probe` (low-priority) — ONE cheap non-driven multi-operator-sweep probe; discharge licenses batch-19 authoring, non-discharge records `map_solve` as a permanent single-witness spine-coverage finding.
4. `l1-l1-l0-index-staleness-audit` (hygiene) — sweep L1/L1-L0 index tables for historical status-cell residue (the promotion-time guard prevents NEW drift; this checks the back-catalogue).

## Ratifications this batch (do not re-litigate)

- The strawman §3.7 `iterate_while` family IS the shared parent of `solve_family` (map) + `fold_solve` (fold). No third parent abstraction.
- `solve_family` L3 = NO-ENTRY (anti-mirror; the L4>L3 dissolution theme is the authoritative L3-form home). Added to the STOP-PROPOSING negative list — do NOT re-propose an `L3/solve_family` backfill.
- `disciplined-cross-pipeline-combinator-mining-gate` skill confirmed working — cite it at the `map-solve-second-pipeline-probe` + the `fold-solve` 2nd-witness discharge.
