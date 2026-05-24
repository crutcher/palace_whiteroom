# Skills

Agent-invocable procedures. Verbs, where `scaffolding/` is nouns.

A skill is a procedure for a recurring kind of task — "audit episodic.jsonl for unresolved push-back signals," "verify a rotation_claim's citation chain end-to-end," "scan concepts/ for near-duplicates." Skills are *derived from* the methodology in `CLAUDE.md`, applied to specific tasks. They are not the methodology, and they are not role prompts.

## Authority

Skill creation, refinement, and retirement is **Meta-Critic / meta-review work** (Medium cascade). Per-cycle agents *invoke* skills; they do not create or modify them.

Pre-orchestrator (now): this Claude Code session acts in the meta-cycle capacity. Skill development is permitted here and committed alongside other meta-pass work.

**Small-scope speculative skills are default-accepted.** A skill that fits a felt need now — even if it'll be refined later — is preferred over no skill. Friction from use teaches better than design from imagination.

## Layout

Each skill is a directory containing `SKILL.md`:

```
skills/<skill-name>/SKILL.md
```

Additional files in the same directory are permitted: helper scripts (`*.sh`, `*.py`), reference data (`*.json`), worked examples (`example-*.md`).

## SKILL.md format

Claude-Code-compatible frontmatter:

```markdown
---
name: skill-name
description: One-line summary used by callers to decide whether this skill applies. Be specific — vague descriptions cause mis-routing.
status: active                  # active | retired
superseded_by: other-skill-name # only if status: retired
---

# <skill-name>

<body — the procedure>
```

The `description` field is load-bearing: it's what an invoker reads to decide whether to apply the skill. Write descriptions that say *when this applies*, not just *what it does*.

## Discipline

- **Append-only structurally.** New skills may be added freely. Existing skill bodies may be refined in-place (wording fixes, clarification). Renames, deletions, and shape changes go through explicit meta-review.
- **Retire by marking, not deleting.** A skill that has been superseded gets `status: retired` and `superseded_by: <name>` in its frontmatter. The file is not removed — the body remains as the canonical reference for what the skill used to mean.
- **Refinement is incremental.** A skill's first version usually misses cases. The expected pattern: write small, use it, observe friction, refine. Refinements are committed alongside the cycles that exposed the friction.

## Invocation

- **In Claude Code sessions** (development phase): I read skills directly and name which I'm applying when I use one. Skills are not auto-invoked.
- **Under the future orchestrator**: each role's system prompt lists the skills available to that role with bodies inlined or referenced. The Critic gets a narrower skill set than the Synthesizer.

## What skills are NOT

- **Not the methodology.** Methodology lives in `CLAUDE.md` and the book. Skills are procedures *applying* the methodology.
- **Not role prompts.** A role's system prompt (`prompts/<role>.md`, forthcoming in Phase 4) is the role contract. Skills are tools the role may apply within that contract.
- **Not scaffolding.** A speculative idea about how to do something belongs in `scaffolding/` until it stabilizes into an applicable procedure. Premature crystallization into a skill is its own anti-pattern.
