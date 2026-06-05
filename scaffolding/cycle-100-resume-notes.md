# Cycle-100 resume notes (batch-31 meta-phase → batch-32 kickoff)

**SESSION RESTART REQUIRED before cycle-100.** The batch-31 meta-phase (post-cycle-099)
enacted `.claude/agents/` + CLAUDE.md + `skills/` changes; the parent must restart the
Claude Code session so the new agent definitions + operational guide load before cycle-100
begins. (The restart also resets the primary conversation context — there is no separate
`/compact` step.)

## What changed + why a restart is needed

### `.claude/agents/` edits (the load-bearing restart reason)
- **`.claude/agents/combinator-miner.md`** — the opening "search surfaces" sentence no longer
  names the Phase-1 slice corpus (`book/src/spec/slices/`) as a live search surface (the corpus
  was fully lifted and DELETED, 9→0, cycles 097/098/099). It now points the miner at the firm
  layered + feature-spine + concept surfaces and Palace source. A combinator-miner dispatched
  with the OLD definition would be told to search a directory that no longer exists.

### `skills/` edits
- **`skills/phase-1-slice-reduction-audit/` → `skills/_retired/phase-1-slice-reduction-audit/`**
  — ARCHIVED (campaign complete; no slices remain to audit). The skill carries a retirement
  banner. Do NOT invoke it.
- **`skills/deleted-slug-inbound-live-link-sweep/SKILL.md`** — REFINED: folded in the
  "exclude the target file by SOURCE-PATH prefix, NEVER by link-target text" grep-bug warning
  (the c098-D1 defect that swallowed 8 inbound links), and broadened "When to invoke" from
  slice-deletion-only to ANY `book/src/**` file deletion (steady-state, not slice-scoped).
- **`skills/verify-dispatch-scope-not-already-discharged/SKILL.md`** — the "slice-reduction
  audit" deliverable-presence check step is RETIRED (no slices left to audit; directory gone).

### CLAUDE.md edits
- §Repository-status: the Phase-1 slice corpus line now states the corpus was lifted and DELETED
  (9→0), and `book/src/spec/` no longer exists.
- §Layout: removed the `spec/` line (added `feature/`); removed the `orchestrator/` / `lessons.md`
  / `questions.md` Layout lines (deleted this batch); added the `mcp/codemap/` line + a note on
  the non-book-orphan deletions.
- §Decommissioned: now states the pre-redirect orchestrator + `prompts/` + `schemas/` + the legacy
  ledgers + stale root `README.md` were DELETED (recoverable from git).
- §Methodology-invariants "Phase 1 corpus reduces as material is lifted" → "Phase 1 corpus was
  lifted and deleted": the `annotated-and-retained` carve-out is RETIRED; the
  `phase-1-slice-reduction-audit` skill is archived; the rank-0 `roadmap_goal` chapter is the
  in-discipline replacement.

## Non-restart-blocking changes (FYI; no session-load impact)
- DELETED non-book orphans (ride this meta-phase commit, recoverable from git): `README.md`,
  `lessons.md`, `questions.md`, `episodic.jsonl.README.md`, `orchestrator/`, `prompts/`, `schemas/`.
- `scaffolding/open-questions.md` — batch-31 unification (12 closed / 2 migrated / 2 kept-deferred;
  1649→1471 lines).
- `scaffolding/priorities.md` — CYCLE-100/batch-32 active head prepended.
- `scaffolding/friction-ledger.md` — new entry `slice-deletion-inbound-link-sweep-self-exclusion-grep-bug`.
- `scaffolding/skill-candidates.md` — `inbound-link-sweep-before-slice-delete` marked rejected (duplicate).
- `book/src/methodology/goal-flow.md` + `resolution-ladder.md` — campaign-complete refresh (build exit 0).

## Two ASK items surfaced to the human (await disposition; NOT enacted)
1. **`BOOTSTRAP.md` (53KB) + `MIGRATION.md` (71KB)** — borderline keep-as-historical. Both are
   currently referenced by CLAUDE.md / memory as the canonical historical/redirect record (KEEP),
   but are large; the question is retain-as-is vs compact-to-a-history-stub-once-fully-internalized.
   Conservative default: KEEP (a live process reference exists). Human to decide if a compaction is wanted.
2. **`.env.example`** — orchestrator-era API-key template, but also documents the codemap server's
   `RUST_LOG` env var. Borderline retain-vs-delete. Conservative default: KEEP. Human to decide.

## Batch-32 frontier (cycles 100/101/102)
The graded-stack campaign is fully discharged; the LEAD returns to the standing forward frontier
(bottom-up vocabulary + 5-driver→L4 backend-lowering completeness + the last `seed` feature column
`boundary-mode`, demand-gated). Fold in the batch-32 candidates: the Class-B slice-range residue
cleanup (one LOW micro-sweep) + the orphan-review follow-ons (the 5 dead orchestrator-era skills =
a batch-32 skill-retirement candidate).
