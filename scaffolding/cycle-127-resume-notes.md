# Cycle-127 resume notes — SESSION RESTART REQUIRED before c127

**Written by:** batch-40 meta-phase (post-cycle-126 finalize), 2026-06-07.

## Why a restart is needed

The batch-40 meta-phase enacted **role-spec changes under `.claude/agents/`**. Per the friction pattern `new-agent-defs-need-session-restart`, the parent orchestrator must **restart the Claude Code session before the c127 cycle begins**, so the new agent definitions are loaded. The restart also resets the primary conversation context (subsuming the retired per-meta `/compact` step — do NOT run a separate compaction).

## Agent-defs that changed (and why)

1. **`.claude/agents/combinator-miner.md`** — added a Discipline bullet: a destructive replace-and-propagate sweep that ELIMINATES a standalone node must sweep THREE de-link surfaces, not two — markdown body links, prose code-spans, AND **YAML frontmatter typed `edges:` blocks** (`depends-on`/`reference`/`lifts-from`/`realizes-kernel-api`). Run skill `deleted-slug-inbound-live-link-sweep` step 7 and re-point each frontmatter edge in proposed-changes. Motivation: friction `deleted-slug-frontmatter-edge-gap` — the c124 RE6 arity-leaf elimination shipped 2 stale frontmatter `depends-on` edges past the body-link sweep + linkcheck2; only the rank linter caught them at finalize.

2. **`.claude/agents/integrator-per-report.md`** — added a per-report safety-net gate: when a report `delete:`s any `book/src/**` chapter, run the frontmatter-edge sweep as a pre-apply check and defensively re-point any residual `depends-on`/`reference` edge to the surviving consolidation target. Motivation: same friction — move the catch from finalize-time to per-report-time, AND catch the `reference`-class danglers that neither linkcheck2 nor the rank-linter flags.

(Also edited, NOT agent-defs — no restart implication, but loaded fresh anyway: `skills/deleted-slug-inbound-live-link-sweep/SKILL.md` gained the frontmatter-edge tier + Procedure step 7; `scaffolding/friction-ledger.md`, `scaffolding/graded-stack-baseline-exceptions.md`, `scaffolding/priorities.md`, `scaffolding/open-questions.md`, `book/src/methodology/goal-flow.md`.)

## After restart — the c127 head

`scaffolding/priorities.md` CYCLE-127 / batch-41 active head (ASK-2 "A then B"): item-1 (element-local rank-tensor deepening) is the LEAD; item-2 (firm `mk_matrix_free_operator` off roadmap_goal) couples; item-3 (5-driver L4-completeness audit) is the "B" capstone, sequenced after "A"; items 4-6 (inner-product RE-style refactor, P1 edge-typing/true-detritus sweep, L2/index count-reconcile) are D-opportunistic/hygiene.
