# Cycle-049 resume notes (post-batch-14 meta-phase)

## SESSION RESTART REQUIRED before cycle-049

The batch-14 meta-phase enacted **role-spec changes to 3 agent definitions**. The parent orchestrator must **restart the Claude Code session** before dispatching cycle-049 so the new agent definitions load. (The restart also resets the primary conversation context — there is no separate `/compact` step.)

**Agent-defs changed (why):**
- `.claude/agents/cycle-planner.md` — NEW dispatch-design §Discipline clause: when one dispatch forward-references a sibling-dispatch's not-yet-existing chapter/theme that will land THIS cycle, state the **canonical slug** explicitly in BOTH dispatch scopes (the referencing one and the authoring one), so neither producer has to invent a working slug.
- `.claude/agents/harvester.md` — NEW producer bullet: when forward-referencing a sibling-dispatch's same-cycle chapter/theme, use the **planner-stated canonical slug** verbatim; if the planner did not state one, write a plain-text backtick slug + flag for integrator reconciliation (do NOT invent a live link to a guessed name).
- `.claude/agents/abstractor.md` — NEW producer bullet: the matching convention (your theme is the typical authoring-half of a cap↔theme forward-reference pair).

All three trace to the friction-ledger entry enacted this batch: `cross-report-forward-reference-slug-divergence` (the c048 D1↔D3 slug divergence `ksp-solve-outer-driver-dissolution` vs canonical `ksp-solve-driver-dissolution` — caught by both critics, repaired clean, but cleanly preventable).

## Cycle-049 lead frontier (from the reshaped plan)

The 2026-05-31 uniform-pull-up climb reached its top: the **L4 frontier is SUBSTANTIALLY COMPLETE** (cycles 046–048: L4 firm 4→6 with `ksp_solve`+`eigsolve` caps; L4>L3 firm 3→6; outer-driver vocab 3→4). The stack is rectangular through L0–L3 + L4 substantially capped (13 of 18 L3 ops no-L4-by-design; only R5 `L4/orthogonalize` deferred-marginal). **The forward-frontier construction phase is winding down.**

Cycle-049 is a **low-cost L4-consolidation pass** while the human considers the strategic pivot (see below). Active head (see `scaffolding/priorities.md` §CYCLE-049 active head):
1. `l4-native-combinator-denominator-completeness-survey` (LEAD, Medium) — `combinator-miner`/`cross-layer-cross-cutter` survey: settle the L4-cap denominator definitionally + prove the L4 frontier exhausted (the evidence input to the human's pivot decision). No `book/` mutation.
2. L4 width/depth consolidation audit (Low, optional) — `same-layer-cross-cutter`/`layer-intro-author` L4-index/L4>L3-index coherence audit (EigOutcome ratification reflected; in-line-by-design eigsolve/chebyshev notes coherent).
3. Open slot fallback — marginal R5 ONLY if pick #1 surfaces a firm L4 Arnoldi consumer; else a Phase-1 slice-reduction audit OR the `matrix-weighted-norm`/`bilinear-form` L1-promotion track. **Do NOT propose new forward-frontier L4 caps beyond R5** — the frontier is assessed complete.

## ASK ITEMS FOR THE HUMAN (batch-14 meta-phase — surfaced, NOT enacted)

**STRATEGIC SCOPE-DIRECTION DECISION — is the layer-construction phase done? Do we pivot toward the downstream burn-component effort?**

With the layered spec substantially complete (L0–L3 rectangular + L4 capped), the forward-frontier construction work that has driven every cycle is winding down. The question is which direction the project takes next:

- **(A) Continue consolidation/audit/hygiene of the layered spec** — depth-fill: more `verified_against:` audits, Phase-1 slice-reduction, concept-page coverage, residual citation hygiene, the L4 denominator survey. Low-risk, keeps the existing cadence + roles. Finite runway (the spec is mostly built).
- **(B) Pivot toward the downstream burn-component effort** the calculus vocabulary was built to serve (CLAUDE.md §"What this system is": "No port is produced. The output is a layered specification; a separate downstream effort uses it to incrementally build burn components"). This is a **NEW phase** — likely **new roles** + possibly a new cycle structure (a downstream-consumer that reads the spec and emits burn components). This is **High-cascade** — the meta-phase cannot self-authorize it.
- **(C) Some mix** — e.g. keep the cycle cadence on consolidation while standing up a pilot downstream-consumer dispatch to surface what the spec is missing for the burn effort.

The cycle-049 consolidation pass (pick #1 survey) is a **safe no-regret next cycle regardless of the answer** — it produces the L4-completeness evidence that informs the decision. The human's answer reshapes batch-15+.

Evidence pointers: `scaffolding/priorities.md` §CYCLE-049 active head + §Strategic ASK; `book/src/L4/index.md` §"Queued at L4 (0 — substantially complete)"; the cycle-046 L4-survey read ("L4 mostly intentionally complete"); OQ `l4-near-exhaustion-assessment-batch-14`.

## No other asks.

The OUTCOME-CONVENTION ratification (b) (`Outcome` + per-cap `*Outcome` rows; polymorphic declined) and the cross-report-slug-divergence friction codification were both `go` (enacted this batch). The only open ask is the strategic scope-direction decision above.
