---
name: revert-dispatch-phase-book-mutation
description: Cleanly revert a dispatch-phase artifact leak — when a specialized agent wrote directly to `book/` during the dispatch phase (Phase 2) instead of emitting proposed-changes blocks for integrator-per-report to apply in Phase 5. Deterministic seven-step git procedure that restores phase discipline so the integrator can re-apply from the report's proposed-changes channel. Audience: `repairer`.
status: active
---

# revert-dispatch-phase-book-mutation

CLAUDE.md's write-authority partition assigns `book/` to `integrator-per-report` (Phase 5). A specialized dispatch agent that writes to `book/` during Phase 2 violates the no-artifact-mutation-in-dispatch invariant. When the critic flags this (a write-authority phase-boundary violation), the repairer reverts the leaked working-tree edits so the canonical pipeline (integrator applies from CYCLE.md proposed-changes blocks) runs normally. This skill names the reversion procedure (Option A: clean restoration).

This is a **safety net**, not the primary mitigation. The primary mitigation is the prompt-level guard in the affected agent's role spec (`do NOT write to book/; emit proposed-changes blocks only`). Use this skill when a leak gets past the guard.

## When to invoke

- The critic reports a write-authority phase-boundary violation: a dispatch agent (layer-intro-author, abstractor, lifter, etc.) touched `book/` (or another artifact file) during the dispatch phase.
- The leaked edits are present in the working tree (uncommitted), and the report ALSO contains the same edits as proposed-changes `[old]`/`[new]` blocks in its CYCLE.md.

## Procedure (Option A — clean restoration)

1. **Enumerate the dirty artifact files.** `git status --porcelain book/` (and any other artifact paths the critic named). Confirm exactly which files the dispatch leaked into.

2. **Confirm the working-tree diff matches the report's proposed-changes verbatim.** `git diff <file>` each leaked file; compare against the report's `## Proposed changes` `[new]` blocks. The working-tree edits MUST be exactly the proposed changes — no extra edits, no co-mingled cycle work. If the working tree contains MORE than the report proposes, the leak is co-mingled (escalate; do not blindly revert other work).

3. **Confirm no staged changes.** `git diff --cached <file>` for each — must be empty. A staged leak means someone `git add`ed it; investigate before reverting.

4. **Confirm reapply will be possible.** For each proposed-changes block, confirm it is a complete `[old]`/`[new]` pair AND each `[old]` anchor is unique in committed HEAD: `git show HEAD:<file>` and check the `[old]` text appears exactly once. If any `[old]` is missing from HEAD or non-unique, the integrator cannot reapply by anchor — fall back to **Option B** (accept the working tree, instruct integrator via META-SIGNAL to verify-and-skip-as-already-applied) or escalate `revise`.

5. **Revert the leaked files to HEAD.** `git checkout -- <file>` for each leaked artifact file. This restores the clean pre-dispatch state.

6. **Verify clean.** `git status --porcelain book/` — the leaked files should no longer appear as modified.

7. **Write the META repair record + signal.** Set the repair outcome to `pass-after-repair`. Include a META-SIGNAL line for integrator-finalize → integrator-signals → meta-phase: `write-authority-phase-boundary-violation reverted (Option A); <agent> wrote <N> files to book/ during dispatch; restored to HEAD; integrator-per-report applies normally from proposed-changes`. This is how the pattern reaches the friction-ledger.

## Failure modes

- **Co-mingled edits (step 2 fails).** The working tree contains the dispatch's leak PLUS unrelated changes. Do NOT `git checkout` (you would destroy the unrelated work). Escalate: the dispatch did more than it should have; mark `revise` and surface to the orchestrator.
- **Non-unique `[old]` anchor (step 4 fails).** The integrator cannot reapply by literal-string anchor. Fall back to Option B (accept working tree, instruct integrator to verify-and-skip) or escalate `revise`.
- **Staged leak (step 3 fails).** A `git add` happened. `git restore --staged <file>` first, then re-run step 3, then proceed — but investigate why staging happened (it should not in the normal dispatch flow).

## Discipline

- **Option A (revert + reapply from proposed-changes) is preferred** — it restores phase discipline and exercises the canonical pipeline.
- **Verify-before-revert.** Never `git checkout` without first confirming the diff is exactly the proposed changes (step 2) and reapply is possible (step 4). Reverting co-mingled or un-reappliable work destroys it.
- **Always emit the META-SIGNAL** (step 7) so the pattern reaches the friction-ledger. A silently-repaired leak is invisible to the meta-phase and the prompt-guard never gets reinforced.

## Worked example

- **Cycle-012 (layer-intro-author, concept-corrections).** Report #6 wrote 4 `book/src/concepts/` edits directly during dispatch. Critic flagged HIGH (issue 1). Repairer: enumerated the 4 dirty files (step 1), confirmed each diff matched the report's proposed-changes `[new]` blocks (step 2), confirmed no staged edits (step 3), confirmed all 4 `[old]` anchors matched committed HEAD verbatim and uniquely (step 4), `git checkout`ed all 4 (step 5), verified clean (step 6), wrote `pass-after-repair` + META-SIGNAL (step 7). Integrator-per-report then applied normally from the proposed-changes blocks (all 4 `[old]` anchors matched HEAD).

## Cross-references

- Friction-ledger `specialized-agent-direct-write-to-book-during-dispatch` (generalized cycle-012; recurrence-2 across abstractor cycle-008 + layer-intro-author cycle-012).
- Skill-candidates `revert-dispatch-phase-book-mutation` (proposed cycle-012, promoted cycle-012 meta-phase).
- Primary mitigation: `.claude/agents/layer-intro-author.md` §Discipline prompt-guard (do NOT write to book/; emit proposed-changes blocks only).
- CLAUDE.md §Write-authority partition (specialized agents write to `reports/<id>/CYCLE.md` only).

## Provenance

- Promoted: cycle-012 meta-phase (batch-2 closure, 2026-05-28).
- Pattern observed: cycle-008 (abstractor), cycle-012 (layer-intro-author) — recurrence-2 of the generalized write-authority-leak pattern.
- Promotion bar: candidate sketch concrete enough to write as SKILL.md (deterministic seven-step git procedure) AND friction-ledger entry exists. Default-accept under low-bar policy; promoted as the safety-net companion to the prompt-guard primary mitigation.
