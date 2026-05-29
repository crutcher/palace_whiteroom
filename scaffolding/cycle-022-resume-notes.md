# Cycle-022 resume notes (post-meta-phase-cycle-021, batch-5 closure)

**Written by**: meta-phase-cycle-021 (batch-5 closure, 2026-05-29).
**Audience**: parent orchestrator preparing the cycle-022 primary cycle (first cycle of meta-batch-6 = cycles 022/023/024). The next meta-phase fires after cycle-024 finalize.

## Session restart required

Per friction-ledger `new-agent-defs-need-session-restart`, **the parent should restart the Claude Code session before cycle-022 begins.** This meta-phase edited **7 agent definitions**:

1. **`.claude/agents/critic.md`** — `cross-reference-integrity` check gains the **build-readiness guard (firm-body-inside-fence)**: when a report (or its dep-map/SUMMARY row) claims a chapter is `firm`, verify the firm apparatus (`## Status` + Signature + laws + Evidence) sits INSIDE the `edit:`/`new:` proposed-changes fence. This catches the cycle-019 fence-truncation defect at critique time.
2. **`.claude/agents/harvester.md`** — new Discipline bullet: author the FULL firm chapter body INSIDE the proposed-changes fence (do not author chapter sections as the report's own top-level sections; confirm closing fence after last section + balanced nested fences).
3. **`.claude/agents/abstractor.md`** — same fence-encloses-full-body bullet (theme bodies).
4. **`.claude/agents/lifter.md`** — same bullet, tailored to `rough-in`→`firm` flips (the fgmres-firm shape).
5. **`.claude/agents/lowering-verifier.md`** — same bullet, tailored to status-flip proposals (the axpby-firm shape; enclose the `verified_against:` block + apparatus inside the fence).
6. **`.claude/agents/layer-intro-author.md`** — new Discipline bullet: **survey chapter firmness from the on-disk `## Status`, NOT the cycle record** (the downstream symptom of the fence-truncation defect; a refresh that trusts the cycle log propagates a landing gap into the navigational source-of-truth).
7. **`.claude/agents/combinator-miner.md`** — new subsection **"Constructed-operator-action family (a non-fold parametric class)"**: closes the cycle-019 Qualification-B mode-gap — a reportable family class for action-shaped cohorts (smoothers/preconditioners) unified by a shared `Solver<OperType>::Mult` contract rather than a fold-law.

A session restart ensures all 7 definitions load for cycle-022 dispatch.

## Compactification

Per CLAUDE.md §Methodology invariants "Compactify primary context after every meta-phase", **the parent should run `/compact`** after the meta-phase commit lands + pushes. With the 3:1 cadence this fires roughly every 3 primary cycles (this is the fifth such firing, closing batch-5).

## ASK items awaiting user decision

**ONE new this batch (the leading ASK) + ONE carried-held (no new action).**

1. **(NEW — go-recommended) Mechanical codemap-backed citation-range checker tool under `tools/`.** This is the **recurrence-4 escalation** of friction-ledger `producer-citation-drift-verify-not-self-invoked`. The batch-3 meta-phase ASK'd for this tool and deferred it; batch-4 held clean (defer-confirmed); **batch-5 (019/020/021) shows the inline-anchor drift RETURNED as a stable 3-cycle pattern** despite the producer self-verify bullets — exactly the agreed recurrence-4 trigger ("build the checker only if drift returns in batch-5+"). The drift is mechanical (pinpoint citations land ±1-2 lines off while wide ranges stay correct), always-caught-downstream (repairer/critic/verifier independent re-reads) but costing a repair/re-read round each time AND occasionally producing critic↔repairer↔verifier disagreement. The tool would validate every `path:lo-hi` in a CYCLE.md's proposed-changes against `reference/` source via the codemap (`get_symbol_def`/`search_text`/`read_range`) as a pre-integration lint, emitting a per-citation OK/DRIFT(±N) report. It is **ask-class** because it requires writing code under `tools/` (outside meta-phase write-authority). The enabling conditions are all met: recurrence-4 fired; the codemap MCP is in routine zero-permission-denied use (it can back the checker); the drift is mechanical (what a lint catches, a prose bullet does not). **Recommendation: build it** (the user enacts the code, or directs the parent to). If declined, the producer-self-verify bullets remain the only defense and the drift-repair-round cost is accepted as standing overhead.

2. **(CARRIED — HELD, no new action) integrator-per-report pre-dispatch clean-tree gate.** The `specialized-agent-direct-write-to-book-during-dispatch` watch clause's option (b), held since batch-4. **No book-leak occurred in batch-5** (the universal prompt-guard held), so the recurrence-4 escalation condition for THIS gate is NOT met. It stays held; enact only on a fourth book-leak despite the universal prompt-guard. No action needed.

## Cycle-022 active head (the plan; fan-out-ranked)

From `scaffolding/priorities.md` §Now (the meta-phase migrated the batch-5 carry-forward intake into this slate). Planner finalizes scope/ordering; pick highest-fan-out first.

1. **(lowering-verifier/abstractor) `axpbypcz-mutation-rotation` callsite-correction + firm** — enact the 3 drafted callsite corrections + correction (6) + the drafted `verified_against:`, flip rough-in→firm. **CLOSES the BLAS-1 L1>L0 floor 8/8.** (The auditor already drafted the firm body — enact-the-drafted-corrections dispatch.)
2. **(harvester) NEW `lu_solve` L1 dense-solve primitive** — the HIGH-fan-out blocker for `deflate`/`gram`; small-dense `k×k` `fullPivLu().solve`.
3. **(harvester) `eigsolve` L1 rough-in→firm** — first step of the strict eigsolve prerequisite chain (L1-firm → L2-entry → L3-backfill).
4. **(harvester) `nleps_deflated_residual` L1** — next deferred NLEPS piece; now unblocked by the cycle-021 deflate/gram L2 shape.
5. **(harvester) `deflate`/`gram` L2 combinator firm** — gated on #2 (`lu_solve`); wave-2 after it lands; creates `L2/gram.md`+`deflate.md`.
6. **(lifter/lowering-verifier) L3-entry citation-drift sweep** — L3 `ksp_solve` `:464`→`:463`/`:564`→`:563` + inner-product-fold `operator.cpp` `:624`/`:634`/`:616` in one pass.
7. **(abstractor) `orthogonalize-composition-lowering` L2>L1 theme** — carry from cycle-019; cite `dot-mutation-rotation` Sub-pattern D for the inner-product realization.
8. **(layer-intro-author) L2-index prose refresh** — drop the stale "L3/ksp_solve not yet on disk" clause; upgrade to live link; refresh `ksp_solve` row prose; fold the two L2-intro-refresh flags.

Backlog (Medium/Low) holds: `incremental-least-squares` stub→firm; the sibling-pair lowering-verifier audits (fgmres-gmres L3 consistency + the `verified_against:` audits for dot/scal/nrm2/assemble-diagonal themes); matrix-weighted-norm + bilinear-form firm-promotion; normalize-l1-harvest; the low-fan-out hygiene sweeps. See `priorities.md` for the full ranked list.

## Skills this meta-phase

- **Promoted (2):** `proposed-changes-fence-encloses-full-body-guard` (NEW critic build-readiness skill); `verify-citation-range` extended with a third sub-case (sibling-slice/inherited-precedent re-anchor).
- **Folded into role-spec (1):** `verify-intro-firmness-survey-against-on-disk-status-lines` → layer-intro-author Discipline bullet (not a standalone skill; it is the downstream symptom of the fence defect, the upstream cause of which is now critic-guarded).
- **Corrected in place (1):** `classify-variant-axis` SKILL.md gs_orthog worked example (cycle-019 stale-example fix: CGS uses plain `axpy×m` not fused `gemv_basis`; CGS2 second pass is unconditional, no `refine_threshold`).
- **Retired:** none.

## OQ-ledger unification this meta-phase

21 OQs closed to the Closed index (the batch-5 resolutions + all 4 methodology-agenda items + the Qualification-B mode-gap); 8 actionable items migrated into the cycle-022 plan (fan-out-ranked); ~40 deferred/contingent kept compacted with triggers. `open-questions.md` maintenance-note header updated (last-unified 2026-05-29).

## Friction-ledger churn this meta-phase

5 updates: 2 NEW entries (`firm-chapter-body-authored-outside-proposed-changes-fence` addressed; `sibling-slice-citation-reanchor-sweep-gap` addressed) + 3 status flips (`producer-citation-drift-verify-not-self-invoked` addressed→escalating, recurrence 3→4, citation-checker ASK; `skill-uptake-survey-non-invocation-cycle-wide` recurrence 4→5, benign-telemetry continued, no-go; `combinator-miner-arity-blind-parametric-family-detection` validated-by-use + extended with the non-fold class).

## Estimated cycle-022 wave-1 candidate dispatches (suggestive, not prescriptive)

Per the active head + fan-out ranking:
- **lowering-verifier/abstractor** on `axpbypcz-mutation-rotation` (enact drafted corrections + firm; closes BLAS-1 8/8).
- **harvester** on the NEW `lu_solve` L1 dense-solve primitive (the `deflate` blocker).
- **harvester** on `eigsolve` L1 rough-in→firm (first step of the eigsolve chain).
- **harvester** on `nleps_deflated_residual` L1 (now unblocked).
- **lifter/lowering-verifier** citation-drift sweep (L3 ksp_solve + inner-product-fold).
- **abstractor** on `orthogonalize-composition-lowering` L2>L1 theme.

Wave-2 (after `lu_solve` lands): **harvester** on `deflate`/`gram` L2 firm. Planner judgment for final scope and ordering (wave-cap up to 12). **The next meta-phase fires after cycle-024 finalize** (batch-6 = cycles 022/023/024; cycle counter does NOT reset).
