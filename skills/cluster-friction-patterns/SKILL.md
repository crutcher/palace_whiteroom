---
name: cluster-friction-patterns
description: At meta-review time, scan accumulated friction signals (episodic.jsonl, lessons.md, problems/) since the last meta-review; cluster by topic/layer/role; categorize by cascade (LOW/MEDIUM/HIGH); produce refinement-plan inputs. Invoke at the start of each Meta-Critic session.
status: active
---

# cluster-friction-patterns

The Meta-Critic's analytical move. The per-cycle agents produce friction signals locally; this skill aggregates them into project-level patterns and routes them by cascade.

## When to invoke

- **Meta-Critic**, at the start of every meta-review session (every 3 cycles per `config.toml`, or manual).

## Inputs

Read across the **window since the last meta-review record** in `book/src/meta-reviews/`:

- `episodic.jsonl` — `friction_observed`, `structural_change`, `push_back_signals` fields.
- `lessons.md` — entries added since the last meta-review.
- `problems/` — open entries (resolved entries from prior reviews are read for context).
- The current state of `BOOTSTRAP.md`, `CLAUDE.md`, role prompts (`prompts/<role>.md`), and skills (`skills/<name>/SKILL.md`).
- **Prior meta-review records** — your incremental project history. A pattern that resolved in a prior review but is recurring now is first-class signal: on the third recurrence, escalate from Medium to High.

## Procedure

1. **Enumerate signals.** From episodic.jsonl: every non-empty `friction_observed` and every push-back signal in the window. From lessons.md: every entry. From problems/: every open entry. Don't summarize yet — list raw.

2. **Cluster by axis.** Group signals along axes:
   - **By layer**: L1 mutation issues, L2 algebraic issues, L3 sequentiality issues, L4 calculus issues, cross-layer.
   - **By role**: Explorer issues, Synthesizer issues, Critic issues, Planner issues, infrastructure.
   - **By slice**: per-slice issues vs. methodology issues.
   - **By topic**: concept-collisions, citation-quality, test-coverage gaps, prompt-wording, schema rigidity.
   
   Same signal may belong to multiple clusters; that's expected — it strengthens the case for action.

3. **Identify recurrence.** Compare clusters against prior meta-review records. A cluster that matches a prior review's *Medium-resolved* item is a recurrence. On the second recurrence, the prior resolution didn't stick — restate the issue with the failure mode noted. On the third recurrence, escalate from Medium to High.

4. **Categorize each cluster by cascade.**
   - **LOW** — typos, single-file wording polish, single-prompt clarity fixes. Apply directly; note in the meta-review record.
   - **MEDIUM** — prompt revisions, methodology adjustments within the framework, slice-convention changes, new `concepts/` extractions, new `skills/` entries, restructuring of an existing skill, scaffolding-channel changes. **Bundle into the refinement plan; requires human approval.**
   - **HIGH** — changes to layer count or layer semantics, L4 calculus design revisions, core process-model changes, new agent roles, fundamental shifts in the methodology framing. **Surface as escalation; do not propose changes.**

5. **Triage err toward Medium-as-escalation.** When uncertain between Medium-direct-action and Medium-as-escalation (i.e., should this be applied or should the human weigh in), prefer escalation. The bar is "the human would want to weigh in."

6. **Build the plan structure.** Emit a `refinement_plan` JSON (per `schemas/refinement_plan.json`) with:
   - `categorized_issues`: the LOW/MEDIUM/HIGH breakdown with brief descriptions.
   - `direct_actions`: enumerated LOW items with file/change_summary.
   - `plan_items`: enumerated MEDIUM items with proposed_change, cascade_trace (why this is Medium not Low or High), risk_notes, and any depends_on dependencies.
   - `escalations`: HIGH items with why_high.

## After human review

- LOW items: already applied (in step 6's emission). Note in the meta-review record.
- MEDIUM items approved: enact, write the meta-review record reflecting as-enacted.
- MEDIUM items deferred: re-categorize or drop; note rationale in the record.
- HIGH items: design-level conversation with the human; the meta-review record captures the conversation's outcome.

## Output artifacts

Two files in `book/src/meta-reviews/`:

- `<YYYY-MM-DD>.md` — the immutable meta-review record. Includes: window, signals enumerated, clusters identified, cascade categorization, plan as-proposed and as-enacted, human conversations on HIGH items.
- `<YYYY-MM-DD>-plan.md` — the refinement plan as a standalone file. Useful for diffing against next review's plan.

## Friction → `problems/`

If applying this skill produces structural ambiguity that prevents categorization (e.g., a cluster has signals from both Critic and Synthesizer prompts in a way that the cascade framework doesn't separate cleanly; the refinement_plan schema's structure forces awkward fits), file as a `problems/` entry for the human-readable methodology to evolve.
