# Cycle-007 resume notes

**Written by**: cycle-006 meta-phase (2026-05-27T09:30Z).
**Consumed at**: end of cycle-007 integrator-finalize (delete this file per its own step-4 instruction below; mirrors cycle-005 → cycle-006 + cycle-006 → cycle-007 patterns).

## Why this file exists

The cycle-006 meta-phase edited **9 role specs** under `.claude/agents/`. Per friction-ledger entry `new-agent-defs-need-session-restart`: the Claude Code session that wrote the role-spec edits will NOT see the changes in its cached agent registry. Cycle-007 cycle-planner and dispatched agents see the updated specs only after a session restart.

This file is a checkpoint for the session that resumes after the cycle-006 meta-phase commit + restart, listing what changed and why a restart is needed.

## Role specs edited cycle-006 meta-phase

1. `.claude/agents/same-layer-cross-cutter.md` — CYCLE.md naming (was stale `Output: REPORT.md`) + explicit "Write CYCLE.md to disk yourself" instruction. Reason: cycle-006 subagent did not write CYCLE.md; parent wrote post-hoc (friction-ledger `subagent-write-filter-still-applies-to-some-agents-cycle-md-naming`).
2. `.claude/agents/cross-layer-cross-cutter.md` — same fix (defensive sweep).
3. `.claude/agents/combinator-miner.md` — same fix (defensive sweep).
4. `.claude/agents/harvester.md` — same fix + L4 / L3 strawman + pseudo-language conventions (per user directive `2f5dbc6`).
5. `.claude/agents/abstractor.md` — same fix + rough-in dep-map plain-text discipline (per friction-ledger `rough-in-rows-must-be-plain-text-when-anchor-missing`) + L4 / L3 strawman + pseudo-language conventions.
6. `.claude/agents/lifter.md` — same fix + L4 / L3 strawman + pseudo-language conventions.
7. `.claude/agents/lowering-verifier.md` — same fix.
8. `.claude/agents/layer-intro-author.md` — same fix + rough-in dep-map plain-text discipline + L4 / L3 strawman + pseudo-language conventions.
9. `.claude/agents/integrator-per-report.md` — `integrated_at:` write-authority clarification (per friction-ledger `integrated-at-write-authority-drift`) + index-placeholder displacement gate (per friction-ledger `index-placeholder-displacement-on-first-firm-row`).
10. `.claude/agents/meta-phase.md` — post-meta compactification note + session-restart cadence (per user directive `2f5dbc6`).

## Session-restart action

Before cycle-007 begins:
1. Run `/compact` to reduce primary-conversation context (per user directive `2f5dbc6`).
2. **Restart the Claude Code session** so the cached agent registry picks up the role-spec edits.
3. Sanity check: cycle-007 cycle-planner dispatch should resolve to the updated `.claude/agents/cycle-planner.md` (no edit this cycle but cached state should be fresh); other dispatches should see the updated role specs above.

## MCP reintegration sequence (priority #16)

Per user directive `f661039`, MCP codemap reintegration is **NEXT-UP post-meta-phase**. The sequence (from priorities.md #16):

(a) Verify binary still launches under current rmcp 1.7 / tree-sitter 0.25 deps, rebuild if needed.
(b) Run `cargo test` on smoke suite against `reference/palace/`.
(c) Confirm `.claude/mcp.json` registration loads at next session start (post-restart deferred-tool list should show `mcp__palace-codemap__*` tools).
(d) Update `harvester` / `lowering-verifier` / `cross-layer-cross-cutter` / `same-layer-cross-cutter` / `combinator-miner` role specs to reference these tools as preferred for C++ source-localization (deferred to pilot results per cycle-006 meta-phase decision; do not preemptively edit).
(e) Pilot on one cycle-007 harvester dispatch.
(f) Instrument tool-call count and time vs vanilla baseline.
(g) Surface pilot results to user before broad role-spec rollout.

**Order**: do (a), (b), (c) BEFORE cycle-007 cycle-planner dispatches. Do (e), (f), (g) as part of cycle-007's first harvester dispatch. Do (d) as a cycle-007 meta-phase or cycle-008 meta-phase enactment, depending on pilot results.

## Cycle-006 unresolved follow-up dispatches (input to cycle-007 cycle-planner)

The cycle-006 integrator-finalize promoted these to next-cycle work (excerpted from `scaffolding/integrator-signals.md` cycle-006 §Suggested next dispatches):

1. **`harvester` on `iterate_while` + `iterate_while_with_prev` @ L4** — closes `iterate-while-l4-anchor-missing` OQ; re-firms cycle-006 defanged rough-in dep-map rows.
2. **`abstractor` on `krylov-step-body-identity` @ L3>L2** — short single-theme dispatch closing `krylov-step-body-identity-theme-pending-cycle-007` OQ; symmetric completion of the krylov-step lowering chain.
3. **`layer-intro-author` retroactive-L1-context-thinning sweep** — priority #11 now eligible (≥6 L0 chapters threshold met); broader L0-interpretation thinning across 7 L1 entries.
4. **`layer-intro-author` L0 bootstrap bundle 3** — priority #10 continuation.
5. **`harvester` on `l1-ksp-solve` @ L1** — both concept-page and L0-anchor anchors now exist.
6. **`lowering-verifier` on `iterate_while` L3 trajectory-accumulation reconciliation** — wave-2 abstractor's deferred substantive rotation decision.
7. **MCP codemap reintegration** (priority #16, NOT a planner dispatch — orchestration layer).

Cycle-007 cycle-planner reads `scaffolding/integrator-signals.md` cycle-006 top section as primary input.

## Resuming the session

1. `git pull` — fast-forward to latest main (catches the cycle-006 meta-phase commit if not already locally pulled).
2. `/compact` — reduce primary-conversation context.
3. **Restart Claude Code session.**
4. Delete this file (`rm scaffolding/cycle-007-resume-notes.md`) once cycle-007 integrator-finalize commits — it has served its purpose. Mirrors the cycle-005 → cycle-006 + cycle-006 → cycle-007 pattern.
5. Begin cycle-007 with cycle-planner dispatch.
