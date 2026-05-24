# Meta-Reviews

Out-of-cycle friction-integration passes. The normal agent loop produces work; the meta-review consolidates **what didn't fit** the per-cycle channels — open `problems/` entries, push-back signals in the episodic log, patterns in `lessons.md` — into structural changes to the methodology, prompts, or layer designs.

## Trigger

Meta-review runs when **any** of the following is true:

- **3 completed agent cycles** since the last meta-review (per `config.toml`'s `meta_review_every_n_cycles`; tunable — tight cadence during shake-down, looser later).
- The human invokes one manually.

When a meta-review is triggered, the normal loop **pauses** until the meta-review is fully enacted. No new exploration cycles run during analysis → plan → human approval → enactment. The pause is load-bearing: it prevents the agents from drifting further while the deliberation is in progress.

## Roles

A meta-review is driven by a **Meta-Critic** — a role distinct from the per-cycle Critic. The per-cycle Critic verifies individual rotation claims; the Meta-Critic reviews patterns of friction across cycles, with its own **incremental project history** drawn from prior meta-review records. Its prompt, persona, and authority are separate. Same model class as the per-cycle Critic (Opus, per the project's model assignment in `BOOTSTRAP.md`), but a different system prompt and a different context.

The Meta-Critic is **empowered to make adjustments with medium cascade impact** — see the table below. Higher-impact changes are surfaced to the human as escalations rather than acted on.

## Cascade impact

The Meta-Critic categorizes each surfaced issue as Low / Medium / High before deciding how to handle it.

| Category | Examples | Meta-Critic authority |
|----------|----------|-----------------------|
| **Low** | Typo fixes; single-file clarifications; minor prompt-wording polish; closing duplicate `problems/` entries | Apply directly; note in the meta-review record. No plan required. |
| **Medium** | Prompt revisions that change agent behavior; methodology adjustments **within** the established framework; updates to `BOOTSTRAP.md` workflow steps; restructuring of slice conventions; new `concepts/` entries promoted from inline definitions; modifications to per-edge equivalence-check criteria | **Bundle into a refinement plan; require human approval before enactment.** |
| **High** | Changes to the layer count or layer semantics; revisions to the L4 calculus design; changes to "what the spec is for" or the core push-forward/push-back process; introduction of new agent roles | **Surface as escalation.** The Meta-Critic does not propose changes here — it describes what it sees and why it exceeds its authority. Design-level conversation with the human follows. |

The Meta-Critic should err toward Medium-as-escalation rather than Medium-as-direct-action when the cascade trace is uncertain. The bar is "the human would want to weigh in."

## Procedure

1. **Trigger fires.** The orchestrator pauses the normal loop and invokes the Meta-Critic.
2. **Meta-Critic analyzes.** Reads, in order:
   - All open entries in `problems/`.
   - The episodic log (`episodic.jsonl`) since the last meta-review, attending especially to push-back signals from the Synthesizer and friction-flagged verdicts from the per-cycle Critic.
   - New entries in `lessons.md` since the last meta-review.
   - All prior `book/src/meta-reviews/*.md` records — the Meta-Critic's incremental project history. Patterns that recur across meta-reviews are first-class signal (a problem resolved once that recurs is a sign the resolution didn't stick).
3. **Categorization.** Each surfaced issue is tagged Low / Medium / High per the table above. Recurring patterns are weighted: a third recurrence of the same issue may escalate from Medium to High.
4. **Direct action on Low.** Low-impact changes are applied immediately. Affected `problems/` entries are annotated `resolved:` and `resolution:`. Recorded in the meta-review record under *Direct actions*.
5. **Refinement plan drafted for Medium.** Bundled into a structured plan with:
   - Issues addressed, grouped by theme.
   - **Proposed change per issue** — concretely: which file, what edit. Not "consider revising X" but "in `prompts/explorer.md` line 12, replace 'foo' with 'bar' because of issue Y."
   - **Cascade trace** — what slices, prompts, docs, or concepts are affected by each change.
   - **Application order** — dependencies between changes (e.g., update concept first, then revise the prompts that link to it).
   - **Risk and human-attention flags** — anything the Meta-Critic wants the human to look at especially carefully.
6. **High-impact escalations.** Listed in the plan under *Escalations*. The Meta-Critic does not propose changes; it describes what's accumulating, why it's High, and what conversation it expects to need.
7. **Human review.** The human reads the plan, optionally edits it, and finalizes. The plan as finalized is the source of truth for what gets enacted.
8. **Enactment.** Approved changes are applied. `problems/` entries get `resolved:` / `resolution:` annotations. Each applied change is recorded in the meta-review record under *Applied changes*. Escalations are surfaced into the human ↔ Claude conversation for design-level work, separate from the meta-review.
9. **Record committed.** `book/src/meta-reviews/<YYYY-MM-DD>.md` captures: cycles covered, what was reviewed, categorizations, direct actions, the plan + any human edits, applied changes, escalations, and any new patterns the Meta-Critic noticed for future meta-reviews to inherit.
10. **Normal loop resumes.**

## File conventions

- **`book/src/meta-reviews/<YYYY-MM-DD>.md`** — the meta-review record. Immutable once committed (subsequent meta-reviews create new files; do not edit priors). The accumulating record set *is* the Meta-Critic's incremental project history.
- **`book/src/meta-reviews/<YYYY-MM-DD>-plan.md`** — the refinement plan for that meta-review. Lives alongside the record; captures the Meta-Critic's proposal and the human's final edits. Plan and record are kept as separate files (rather than folded together) so that the *as-proposed* and *as-enacted* are both readable historically.
- **`book/src/meta-reviews/index.md`** — this file. Procedure documentation and the records index below.

## Suggested record-file structure

```markdown
---
date: YYYY-MM-DD
cycles_covered: [N..M]
plan_file: YYYY-MM-DD-plan.md          # null if no plan was needed (all-Low)
trigger: cycle-count | manual
---

# Meta-Review — YYYY-MM-DD

## What was reviewed
- Problems: <list>
- Episodic friction signals: <count, summary>
- Lessons since last review: <count, summary>
- Recurring patterns from prior reviews: <list>

## Categorization
- Low: <list>
- Medium: <list> → see plan file
- High (escalations): <list>

## Direct actions (Low)
- <action> — applied to <file>; resolves problems/<id>

## Plan summary (Medium)
- <link to plan file>; summary of accepted vs. revised vs. rejected proposals

## Applied changes
- <file>: <one-line change description>; references plan item N

## Escalations (High)
- <summary>; surfaced to conversation on <date>

## Carry-forward
- Patterns the Meta-Critic noted for the next review.
```

## Records

| Date | Cycles covered | Direct actions | Plan items | Escalations | Notes |
|------|---------------|----------------|------------|-------------|-------|
| _(none yet)_ | — | — | — | — | — |
