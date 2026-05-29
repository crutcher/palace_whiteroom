# Cycle-019 resume notes (post-meta-phase-cycle-018, batch-4 closure)

**Written by**: meta-phase-cycle-018 (batch-4 closure, 2026-05-29).
**Audience**: parent orchestrator preparing the cycle-019 primary cycle (first cycle of meta-batch-5 = cycles 019/020/021).

## Session restart required

Per friction-ledger entry `new-agent-defs-need-session-restart`, **the parent should restart the Claude Code session before cycle-019 begins.** This meta-phase enacted role-spec changes affecting **9 agent definitions**:

**The dispatch-phase write-guard (recurrence-3 escalation) — added as the FIRST Discipline bullet across all 8 specialized specs** (only `layer-intro-author.md` had it before, from cycle-012):

1. **`.claude/agents/harvester.md`** — write-guard bullet + a NEW forward-reference plain-text Discipline bullet (an in-chapter link to a not-yet-authored sibling chapter is a hard `linkcheck2` build error).
2. **`.claude/agents/abstractor.md`** — write-guard bullet.
3. **`.claude/agents/lifter.md`** — write-guard bullet (tailored: re-anchors ARE the deliverable, so they feel like edits but are proposals).
4. **`.claude/agents/lowering-verifier.md`** — write-guard bullet (even when the audit finds a contradiction, propose — never apply).
5. **`.claude/agents/combinator-miner.md`** — write-guard bullet + the HEADLINE parametric/variadic-family detection mode section (see below) + a forward-reference plain-text convention note under `## Proposed changes`.
6. **`.claude/agents/same-layer-cross-cutter.md`** — write-guard bullet (slice-reduction stubs/removals are proposals too).
7. **`.claude/agents/cross-layer-cross-cutter.md`** — write-guard bullet (usually read-only, but edit-implying observations are proposals).

**Integrator split-spec touches:**

8. **`.claude/agents/integrator-per-report.md`** — Process step 7 (STAGING.md append) hardened to a HARD, non-skippable step (cycle-018 staging-log-append gap).
9. **`.claude/agents/integrator-finalize.md`** — Process step 1 gains a staging-row-count cross-check vs dispatched-report-count + reconcile-on-mismatch.

**Plus, from the post-meta user-directed intake→plan refactor (2026-05-28; see §"Intake→plan refactor" below):**

10. **`.claude/agents/meta-phase.md`** — new §Intake→plan migration (standing every-batch pass; OQ + friction → the plan, fan-out-ranked); sole-unifier of `open-questions.md`.
11. **`.claude/agents/cycle-planner.md`** — the plan (`priorities.md`) is now the primary input; dispatch highest-fan-out first; co-owns + may update the plan; OQ/friction reframed as intake.

A session restart ensures all of these definitions are loaded for cycle-019 dispatch.

## HEADLINE enactment — combinator-miner parametric/variadic-family detection mode

The human-raised BLAS-1 prong-(a). `.claude/agents/combinator-miner.md` gained a **"Parametric / variadic-family detection mode"** section: the miner now runs instance-counting in TWO complementary modes on every scan — same-shape mode (the default) AND parametric-family mode (detect a set of operators differing only along a structured parameter axis — arity / element-type / conjugation / weight-presence — that share one *folding* combining step; propose the single variadic parent, not N leaves). The proximate cause was that the default heuristic is arity-blind: the BLAS-1 `linear_combination` fold (`scal`/`axpy`/`axpby`/`axpbypcz` = arity-1/2/3/4 specializations) was represented 3× at fixed arity but unified 0×, invisible to instance-counting, so it had to be human-raised. **First live test: cycle-019+ combinator-miner (active priority #7)** — the obvious near-term candidate is the `inner_product` conjugation-convention cohort. Family-mode bar: ≥2 siblings sharing a stateable fold-law (the law is the evidence); over-unification guard required (e.g. `dot` reduce-to-scalar is a DIFFERENT fold — do not subsume).

## Compactification

Per CLAUDE.md §Methodology invariants "Compactify primary context after every meta-phase", **the parent should run `/compact`** after the meta-phase commit lands + pushes. With the 3:1 cadence this fires roughly every 3 primary cycles (this is the fourth such firing, closing batch-4).

## ASK items awaiting user decision

**TWO this cycle.**

1. **integrator-per-report pre-dispatch clean-tree gate (HELD).** The `specialized-agent-direct-write-to-book-during-dispatch` watch clause's option (b). With the prompt-guard now universal across all 8 specialized specs (the prevention layer) and the `revert-dispatch-phase-book-mutation` repairer skill (the recovery layer), a third backstop — a gate that checks `git status book/` is clean before applying a report and refuses/flags if a dispatch already mutated `book/` — is **held, NOT enacted**. It is ask-class (tooling/structural; changes the per-report apply preconditions). **Recommendation: enact ONLY on recurrence-4** (a fourth book-leak despite the universal prompt-guard), mirroring the citation-checker logic — if the universal prompt-guard shows its ceiling, the structural gate becomes warranted. No action needed unless the user wants the gate pre-emptively.

2. **open-questions.md lazy de-dup / index rebuild — RESOLVED 2026-05-28 (user directive).** The user directed a fuller fix than option (a): unify the ledger AND empower the meta-phase to own the unification going forward (see §"Intake→plan refactor" below). The founding unification pass ran (3040 → 237 lines; 142 entries triaged) and the meta-phase now holds unify/edit authority over `open-questions.md`. No further action needed.

## Carried-forward ASK that did NOT escalate

The batch-3 **mechanical codemap-backed citation-range checker tool** ASK (`tools/`) stays `reviewed: defer-confirmed`. Batch-4 was its test window: the producer self-verify bullets HELD (no new producer-emit drift across 016/017/018 despite heavy citation surface; recurrence-4 did NOT fire). Build the checker only if drift returns in batch-5+. No new decision needed.

## Intake→plan refactor (post-meta user directive, 2026-05-28)

After the batch-4 meta-phase landed, the user directed a structural change to how open questions and friction are managed. **Read this before planning cycle-019 — it changes what `priorities.md` is.**

- **`scaffolding/priorities.md` is now THE PLAN** — the project's single ongoing, fan-out-ranked work backlog (`Now (active head)` + uncapped `Backlog — ranked by fan-out impact`). It is co-owned by meta-phase + cycle-planner. The cycle-019+ active picks (the seven above) are its `Now` head; the Backlog holds the migrated work.
- **`open-questions.md` + `friction-ledger.md` are INTAKE channels, not holding pens.** Issues/friction are reported there; their *resolution is migration into the plan*. The meta-phase runs a standing every-batch §Intake→plan migration pass; the cycle-planner reads the plan and may append fresh candidates.
- **`roadmap.md` is the coverage map + fan-out impact model that RANKS the plan** — not a task list.
- **Planner consequence for cycle-019:** pick dispatches from the plan **highest-fan-out first**. The Backlog's High-fan-out tier (l2-named-composition-lifts, ksp-solve-l2-promotion, l3-vocabulary-inventory-gap, blas1-l1-l0-lowering-theme-gap) is now visible alongside the `Now` head — weigh those for slots not taken by the headline carry-forwards.

## New / updated CLAUDE.md §Methodology invariants

**One added (post-meta, 2026-05-28 user directive):** "The plan is the single ongoing work artifact; intake channels feed it, they don't hold work" — codifies the intake→plan→fan-out flow above. The batch-4 meta-phase enactments themselves added no invariants (role-spec + ledger + priorities only).

## New priorities surface (cycle-019+ active — see scaffolding/priorities.md §Now)

1. **(harvester — HEADLINE) `inner_product` L2 firm operator** — author off the cycle-018 rough-in row; pin conjugation/arg-order convention.
2. **(abstractor) `L2-L1/inner-product-fold-specialization` theme + `linear-combination-fold-specialization-theme-followups`**.
3. **(lifter/abstractor — large) `gmres.md §L4 v0.6→v0.7` self-rotation** (carry-forward; firms GMRES + FGMRES sisters).
4. **(harvester — large) NLEPS at L1+** (carry-forward).
5. **(layer-intro-author) bundle-6 #6 `fespace.{hpp,cpp}`** — input-side FE-space L0 anchor. **Citation-dense; proposed-changes blocks only (write-guard).**
6. **(lifter/cross-layer-cross-cutter) divfree.hpp doc-tension OQ** (`divfree-mult-doc-irrotational-vs-divfree-stale`).
7. **(combinator-miner — try the NEW family-mode)** — scan for the next parametric family; first live exercise of the cycle-018 detection mode.

Carry-forward (Near/queued #8-10): lower-layer-vocabulary bias guidance; bootstrap-L4-state-stratification; residual large carry-forwards (slepc-convergence-reason-lift, spectrum_estimate, chebyshev anchor/Mult2 sweep).

## Skills

**No skill promotions, retirements, or updates this meta-phase.** All batch-4 frictions were addressed via role-spec touches (the existing `revert-dispatch-phase-book-mutation` skill remains the repairer safety-net for any residual book-leak). The skill-candidates channel had no new candidates crossing the bar this batch.

## Friction-ledger churn this meta-phase

6 updates: 3 new entries (`combinator-miner-arity-blind-parametric-family-detection` addressed; `rough-in-forward-reference-must-be-plain-text-not-live-link` addressed; `staging-log-append-completeness-gap` addressed) + 3 status flips (`specialized-agent-direct-write-to-book-during-dispatch` recurrence 2→3, watch-clause fired, guard enacted across all 8 specs; `producer-citation-drift-verify-not-self-invoked` batch-4-held-clean, recurrence-4 did NOT fire; `skill-uptake-survey-non-invocation-cycle-wide` batch-4 benign-telemetry continues, no-go on recalibration). Cycle-019 planner does not need the full friction-ledger; the priorities + this resume-note are the planning surface.

## Estimated cycle-019 wave-1 candidate dispatches (suggestive, not prescriptive)

Per priorities #1–#7 + carry-forward integrator-signals:
- **harvester** on `inner_product` L2 firm operator (HEADLINE; off the rough-in row; pin conjugation).
- **abstractor** on the `L2-L1/inner-product-fold-specialization` theme + `linear-combination-fold-specialization` follow-ups.
- **lifter/abstractor** on `gmres.md §L4 v0.6→v0.7` self-rotation (large carry-forward).
- **layer-intro-author** on bundle-6 #6 `fespace.{hpp,cpp}` (proposed-changes only; self-verify citations).
- **combinator-miner** exercising the NEW parametric/variadic-family detection mode on the next candidate family.

Planner judgment for final scope and ordering. **Meta-phase fires next after cycle-021 finalize** (batch-5 = cycles 019/020/021).
