# Cycle-130 resume notes — SESSION RESTART REQUIRED before c130

**Written by:** the batch-41 meta-phase (post-cycle-129 finalize), 2026-06-07.

**Why a restart:** the batch-41 meta-phase enacted `.claude/agents/` role-spec changes. Per friction-ledger `new-agent-defs-need-session-restart`, the parent orchestrator must **restart the Claude Code session** before cycle-130 begins so the new agent definitions load. The restart also resets the primary conversation context (subsuming the retired per-meta `/compact` step — do NOT run a separate compaction).

## Agent-defs that changed (and why)

1. **`.claude/agents/harvester.md`**, **`.claude/agents/abstractor.md`**, **`.claude/agents/combinator-miner.md`** — **NEW closure-returning-signature producer-discipline bullet** (the explicit ask in USER DIRECTIVE 2026-06-07; memory `project_closure_returning_signature_convention`). When a producer writes a high-order signature whose codomain yields a closure: group a bare returned function in parens `foo -> (bar -> baz)`; spell a returned operator instance with closed `!`-params as `Op[τ_in → τ_out]` / `LinOp[(N: ...), $N]` (already compliant, no outer parens); NEVER write the opaque `LinearOperator[N,N]` type-application form (the non-compliant smell — re-spell, don't wrap). USE + LINK semantics §1.3.1; do not restate.

2. **ALL 9 role-specs** (`cycle-planner`, `harvester`, `abstractor`, `lifter`, `lowering-verifier`-adjacent NONE, `combinator-miner`, `same-layer-cross-cutter`, `cross-layer-cross-cutter`, `layer-intro-author`, `meta-phase`) — **semantic-surface path corrected** `book/src/design/l4_calculus.md` → `book/src/semantics/index.md` (the live surface since the cycle-116 relocation; the book artifact was swept then, the role-specs were not). Friction `semantic-surface-path-drift-in-role-specs-after-relocation`. A "relocated from the former …" provenance note is preserved in each.

   (Note: `lowering-verifier.md` carried no stale path — not edited. The 9 edited files are: cycle-planner, harvester, abstractor, lifter, combinator-miner, same-layer-cross-cutter, cross-layer-cross-cutter, layer-intro-author, meta-phase.)

## What c130 should know going in

- **The in-scope FEATURE-SURFACE SPINE is L4-COMPLETE** (ASK-2 "B" capstone, c128 — no gap). The ASK-2 "A then B" arc is COMPLETE.
- **The batch-42 forward direction is RESOLVED (human decision 2026-06-07): the §1.2.2 / closure-signature POLISH PASS** (chosen over wind-to-maintenance and over the gated sharding-math; memory `project_batch42_direction_polish_pass`). The c130 planner LEADS with `closure-signature-l4-constructor-§1.2.2-compliance-sweep` (folding in the two migrated LOW items — the residual dissolution-theme LHS sweep + the `op-with-params` §1.3 BNF-promotion), running the MAINTENANCE FLOOR (priorities.md items 1-4) as the surrounding steady-state. Bounded consolidation of the EXISTING calculus surface to fully-consistent — NOT a forced vocabulary frontier. (C) sharding-math stays DEFERRED/gated. See `scaffolding/priorities.md` CYCLE-130 / batch-42 head (reshaped post-decision).
- **CLAUDE.md stale-path ask — DONE.** The 3 stale `book/src/design/l4_calculus.md` refs in CLAUDE.md (§SEMANTIC CONSOLIDATION + the 2 L4-strawman invariant bullets) were corrected to `book/src/semantics/index.md` by the orchestrator (commit `ef6498b`) — an objective, reversible path fix. No longer pending.
- **No RE fired the way that needs a c130 consumer.** RE4 stays consumer-gated; the residual RE11 is deliberate-reference-only-reachable (§2g). Linter baseline HELD: `files=385, typed=324, untyped=61, roots=45, reachable=163, reference_reachable=247, rank_violations=0, unresolved=0, promotion_frontier=10, detritus=122, true_detritus=50`.

## Commits
- c129 integrator-finalize artifact commit: `f153841`.
- batch-41 meta-phase methodology commit: (this commit — see `git log`).
