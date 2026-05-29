# Cycle-028 resume notes (post-batch-7 meta-phase)

**Session restart REQUIRED before cycle-028 begins.** The batch-7 meta-phase (post-cycle-027) edited agent definitions under `.claude/agents/`. Per friction-ledger `new-agent-defs-need-session-restart`, the session that wrote these edits does NOT see them in its cached agent registry; restart the Claude Code session so the new definitions load before the first cycle-028 dispatch. The restart also resets the primary conversation context (subsuming the retired per-meta `/compact` step — do NOT run `/compact`).

## Agent-defs changed (why each needs the restart)

1. **`.claude/agents/harvester.md`**, **`abstractor.md`**, **`lifter.md`**, **`layer-intro-author.md`**, **`lowering-verifier.md`** — each gained a **"the codemap is localization-only; `citecheck`/on-disk is the citation source of truth"** sub-bullet in its citecheck self-verify block. Reason: the `palace-codemap` `read_range` drifts +1 from the on-disk file on certain comment+`{`-brace boundaries (friction-ledger `codemap-read-range-plus-one-drift-on-brace-boundary`, recurrence-4, confirmed batches 5/6/7 on the `nleps.cpp` deflation block). A *faithful* codemap transcription still lands wrong; the emitted `path:lo-hi` must come from `citecheck --anchor` against on-disk, and when the two disagree on-disk wins. The producers must load the new bullet so they stop citing straight off codemap output.

2. **`.claude/agents/cycle-planner.md`** — gained two §Discipline bullets (friction-ledger `cycle-planner-reproposes-already-landed-work`, recurrence-2): (a) **verify each candidate dispatch is genuinely OPEN** (not already landed) before proposing it — scan `cycle-record.jsonl` `counts_after`/`cycle_character` + the latest STAGING.md + the plan's struck/DONE Backlog markers; (b) **exactly ONE `integrator-finalize` per primary cycle** — waves are dispatch/forward-ref ordering, not multiple finalizes; the book is not rebuilt between waves and measurable count-bumps the prior finalize already applied are not to be re-scheduled. The planner must load these so cycle-028 planning does not repeat the c026 (re-proposed landed cohort) / c027 (over-built on a finalize-between-waves misconception) drifts.

## New skill (loads from disk, no restart needed but noted)

- **`skills/audit-slug-meaning-before-coordinated-cross-report-rename/SKILL.md`** — repairer-facing denote-by-signature gate before applying a coordinated cross-report rename (the cycle-027 D4/D5 inverted-premise trap). Promoted from the cycle-027 D5 repairer's skill-candidate.

## Cycle-028 plan head (from `scaffolding/priorities.md`)

The active head is set for cycle-028 (FIRST primary cycle of meta-batch-8; cycles 028/029/030; meta-phase fires after cycle-030 finalize). Top picks, fan-out-ranked:
1. **(lifter) incremental-least-squares-composition-lowering L2>L1 — re-anchor to firm `back_solve` + reconcile `trsv`↔`back_solve` + promote rough-in→firm** (the c027 D5 deferral; HIGH fan-out — finishes the GMRES/FGMRES restart-machinery lowering; clean lifter-promotion task; optionally harvest the column-streaming `ls_update_column` leaf).
2. **(lifter) batch-7 carry-forward citation-hygiene residual sweep** (`linalg-operator-file.md:22/:87` Category-1 relabel; `incremental-least-squares.md:13` "queued" self-description; residual `gram.md` "(forthcoming)" if any).
3. **(lowering-verifier) batch-7-firm-theme `verified_against:` audits** (`normalize-mutation-rotation`, `back_solve`, post-pick-1 `incremental-least-squares-composition-lowering`).
4. **(lowering-verifier / same-layer-cross-cutter) matrix-weighted-norm L1-entry rough-in→firm gate** (test-coverage/variant-axis; paired with bilinear-form).
5. **(harvester / cross-layer-cross-cutter) general `trsv` L3-inventory gap** (BLOCKED, no L1 anchor; L1-localize first; likely an obstruction-theme target, distinct from `back_solve`).

## Open ASK items for the human (surfaced by the batch-7 meta-phase; NOT enacted)

1. **Pre-harvest slug-collision check as a standing producer-spec bullet.** The cycle-027 D4/D5 collision (`ls_update_column` bound to two meanings) was avoidable — the L2 entry already used both colliding slugs distinctly. A pre-harvest grep of existing artifact vocabulary before a producer introduces a NEW slug would stop the collision at the source (the better *avoidance* fix vs. the repairer-side *gate* skill promoted this batch). Low cost, but a producer-spec change across harvester/abstractor — confirm appetite vs. relying on the repairer gate.
2. **`integrator-signals.md` archival.** The file is ~1550 lines, ~3× over the ~500-line budget, backlogged since ~cycle-007. Needs a human decision on the archival mechanism/cadence (e.g. archive to `scaffolding/integrator-signals-archive.md`, or a per-batch tail-trim keeping the most recent ~3 cycles the cycle-planner actually reads). Recorded with a trigger; not enacted this batch (the cycle-planner only reads the top ~3 entries, so the bloat is not functionally blocking — but the file is unwieldy).
