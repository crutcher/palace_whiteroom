---
name: skill-selection
description: Meta-skill applied at the start of every cycle (Synthesizer pre-emission and Critic pre-verdict) — given the cycle's content shape, identify which skills' trigger conditions hold, consult those skills and cite them in output (log_synthesis for Synthesizer; skill_uptake field for Critic), and explain non-applicability when no triggers fire. Codifies the procedural step the per-cycle agents must take to make skill uptake observable in episodic.
status: active
---

# skill-selection

A meta-skill: a procedure for selecting and citing other skills. Per-cycle agents (Synthesizer and Critic) apply this skill before emitting their primary output so that skill uptake is recorded in observable data (log_synthesis for Synthesizer, `skill_uptake` array for Critic) rather than left as "silently consulted vs silently ignored."

## When to apply

Apply this skill at the start of every cycle, BEFORE the primary work begins. The result is a structured record of which skills the cycle considered and what came of each.

## Procedure

### Step 1 — Survey active skills

List the skills currently in `skills/` (other than this one). At meta-19 time:

- `classify-variant-axis` — variant-axis classification with `## Variant axes` block output.
- `verify-citation-range` — L0 citation range cross-symbol-boundary check.

Read each `SKILL.md`'s `description` field to know its trigger conditions.

### Step 2 — Check triggers

For each skill, determine whether the cycle's content matches its trigger:

- `classify-variant-axis`: the L0 source has ≥2 variant axis values (template parameters, runtime flags, enums selecting between implementations).
- `verify-citation-range`: the cycle emits or modifies an L0 citation `<path>:<lo>-<hi>`.

### Step 3 — Apply triggered skills

For each skill whose trigger fires:

- Read the skill's full SKILL.md.
- Apply the procedure to this cycle's content.
- Emit the prescribed artifact (e.g., `## Variant axes` block in slice prose; citation-range narrowing in L0 list).

### Step 4 — Record the survey

**Synthesizer**: in `log_synthesis`, include a `skills_consulted` array naming each skill that fired AND each skill considered-but-not-applicable. Use either form:

- String form (legacy): `log_synthesis: "...; skills_consulted: [classify-variant-axis (applied), verify-citation-range (n/a — no L0 edits)]"`
- Structured form (preferred): `log_synthesis: {summary: "...", skills_consulted: [{skill, decision: "applied" | "not_applicable", note: "..."}]}`

**Critic**: populate the `skill_uptake` array on the verdict (per `schemas/critic_verdict.json`):

```json
"skill_uptake": [
  {"skill_name": "classify-variant-axis", "triggered": true, "artifact_present": true, "log_explanation_present": true, "decision": "artifact_landed"},
  {"skill_name": "verify-citation-range", "triggered": false, "artifact_present": false, "log_explanation_present": true, "decision": "explained_non_applicable"}
]
```

### Step 5 — Handle conflicts

If two skills both fire and have conflicting prescribed artifacts (rare), apply both and note the composition in `log_synthesis`. If a skill's procedure would be expensive (e.g., re-reading all L0 ranges to check boundaries on a cycle that didn't change L0), record `decision: "deferred — scope mismatch"` and explain.

## Why this is a meta-skill

`skill-selection` is a *skill about applying other skills*. The methodology explicitly allows meta-skills (per `prompts/meta_critic.md` *Skill propose/modify/split*). The reason this one is warranted: skill uptake had been unmeasurable for ~7 meta-cycles after the first skill extraction, and the meta-18 structured-field promotion of check #15 still produced zero observable data because the verdict path through escalate cycles bypassed the Critic entirely. Codifying the selection procedure as a skill — invocable by both Synthesizer and Critic — makes the uptake measurement structural, not incidental.

## Cross-references

- [`classify-variant-axis`](../classify-variant-axis/SKILL.md) — variant-axis classification.
- [`verify-citation-range`](../verify-citation-range/SKILL.md) — L0 citation boundary check.
- `prompts/critic.md` check #15 — verdict-level skill-uptake recording.
- `prompts/meta_critic.md` *Skill propose/modify/split* — skill lifecycle management.
