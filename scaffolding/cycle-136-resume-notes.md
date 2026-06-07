# Cycle-136 resume notes (post batch-43 meta-phase)

**SESSION RESTART REQUIRED before cycle-136** — the batch-43 meta-phase enacted agent-def changes; restart so the new definitions load. (The restart also resets primary context — there is NO separate `/compact` step.)

## Agent-defs that changed (why a restart is needed)

1. **`.claude/agents/integrator-finalize.md`** — added **step 5c: post-build KaTeX-`$`-sigil-collision assertion.** After `cargo make book`, assert no `<pre>` block in any built HTML contains `class="katex"` (the signature of an indented `$`-sigil pseudocode block whose `$...$` was eaten by the `[preprocessor.katex]` math delimiter). A hit blocks; the surgical repair is indented→fenced ` ```text `. This makes the scan the integrator already ran informally at c134/c135 a standing build-readiness gate. (friction-ledger `katex-dollar-sigil-eaten-in-indented-pseudocode`; memory `project_katex_dollar_sigil_fence_requirement`.)

2. **`.claude/agents/harvester.md`, `abstractor.md`, `lifter.md`, `layer-intro-author.md`** — appended a `$`-sigil-MUST-be-fenced clause to each producer's `**Fenced**` notation bullet: `$`-sigil pseudocode (`Tensor[$S]`, `LinOp[$S,$S]`, `$N`) MUST be inside a ` ```text ` fence, NEVER a 4-space-indented code block (KaTeX skips fenced/inline code but NOT indented code). The clause explicitly notes this does NOT conflict with the batch-6 "4-space-indent inside a proposed-changes block" rule (that rule is about nested-fence parser-toggle inside the *proposed-changes* fence; this is about the *landed chapter body*).

## Why a restart (not just an edit)

The agent harness loads `.claude/agents/*.md` at session start; a running session uses the definitions loaded at its start. The new step-5c gate + the producer `$`-sigil bullets only take effect for dispatches/finalizes in a fresh session.

## What did NOT change

- No new agent roles; no cycle-structure change; no tooling/code change (the KaTeX guard is a post-build assertion in the integrator role-spec + producer reminders, NOT a new `tools/` binary).
- The graded-stack baseline-exceptions ledger gained the batch-43 §2g-extension disposition (scaffolding, not an agent-def).
- `scaffolding/priorities.md` reshaped to the CYCLE-136 / batch-44 head (the maintenance-floor cadence change + the §CENTRAL ASK) — scaffolding, not an agent-def.

## Batch-44 posture (the cycle-136 planner reads this)

- **The §CENTRAL ASK is UNRESOLVED and awaits the human** (3rd consecutive batch of in-scope completeness). Absent a human substantive choice, the DEFAULT is the MAINTENANCE FLOOR on the new cadence.
- **NEW cadence (item 0 of the batch-44 head):** the full-hygiene sweep is now **per-BATCH** (folded into the meta-phase's standing duties + at most one dedicated maintenance-floor cross-cutter dispatch per batch), NOT per-cycle. The **per-cycle floor** is the existing `integrator-finalize` step-5b two-invariant tripwire (`rank_violations==0` + no newly-orphaned node) + the detritus escalate-guard — one command, no dedicated dispatch. The cycle-136 planner should NOT dispatch a dedicated maintenance-floor cross-cutter every cycle.
- If the human chooses a substantive direction, the planner reshapes around it; if (E)/silence, the steady-state floor is the standing posture.
