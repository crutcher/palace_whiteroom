# Problems channel

This directory is the **out-of-band concern channel** for agents working in this repository. An agent files a problem when it notices something the global process should review — not solve, just review.

**Filing rate is self-tuned.** The bar described below is the *default* (sensitivity 3). The actual sensitivity is set in `scaffolding/problems-sensitivity.md` and ranges 1-5; the orchestrator injects `problems_sensitivity: <N>` into per-cycle agent prompts. Target rate: **1 problem filed per 15 agent runs**. The Meta-Critic recalibrates the sensitivity at each meta-cycle.

## When to file a problem

The channel covers two broad categories:

### (A) Out-of-role conflicts and tooling gaps

- **Out-of-role conflicts** — the agent notices something that belongs to a different role's authority. Example: a Critic notices that the Synthesizer prompt is consistently producing claims at the wrong layer.
- **In-line framing concerns** — the methodology framing, as currently described, doesn't fit the slice in hand, in a way that exceeds the agent's responsibility. Example: an Explorer realizes the L0/L1 boundary is unclear for generated code or heavy macros.
- **Tooling / infrastructure gaps** — the agent hits a wall it can't work around within its own role. Example: tree-sitter returns nothing because the grammar doesn't parse that file's dialect.
- **Skill friction** — a skill the agent invoked consistently fights its task across recurring cases. Single edge-cases aren't skill-friction; recurring mismatch is.

### (B) Observed-but-not-in-focus (added 2026-05-26 from user directive after sensitivity saturated at cap with 0/36)

When reading context for the current cycle's work, the agent notices something **wrong in reference work** that the cycle isn't focused on — a contradiction between two slices, a duplicate definition, a mis-framing in an older concept, a stale cross-reference, an outdated methodology footnote. The agent's authority over their cycle doesn't extend to drive-by fixes on unrelated work, but the observation is real and worth surfacing.

The pattern: **"In reading the context for this work [...]; the following contradiction, duplication, miss-framing, etc in reference work was noticed."**

Examples of qualifying drive-by observations:

- Reading cg.md and gmres.md for cross-slice context, notice they describe the same primitive (e.g., `apply_linop`) with subtly different signatures. File.
- Reading a concept page for definition, notice it cites a slice that has since been renamed or restructured. File.
- Reading the methodology section of CLAUDE.md, notice that two adjacent rules give conflicting guidance for a specific case. File.
- Reading variant-absorption.md for the variant absorption rules, notice the "levels of absorption" section and the "structurally-distinct variants" section partially overlap or contradict. File.
- Reading prior meta-review records, notice a plan item that was supposed to land but doesn't appear in current methodology. File.

**The agent does NOT fix the observed problem** — fixing it would expand the cycle's scope unboundedly. The agent files a problem entry naming the observation; meta-review consumes it.

Do NOT file drive-by observations on the slice/concept the cycle is currently focused on — those are normal in-cycle work. The pattern is specifically for **reference material consulted in passing**.

## When *not* to file a problem

- **Unknowns about the target code** → `questions.md`.
- **Agent mistakes recognized in retrospect** → `lessons.md`.
- **Push-back from a higher layer to a lower one** → normal push-back via the Synthesizer.
- **A single rotation claim that doesn't verify** → normal Critic verdict.
- **Anything the agent can fix within its own role on the cycle's focused work** → just fix it.

If you're not sure, lean toward filing — the relaxed bar (after sensitivity saturated at cap=5 with 0/36 over three windows) reflects user direction that the prior bar was too high.

## When *not* to file a problem

These have their own channels and should not pollute `problems/`:

- **Unknowns about the target code** → `questions.md` (the question ledger).
- **Agent mistakes recognized in retrospect** → `lessons.md` (one-line pattern note).
- **Push-back from a higher layer to a lower one** (e.g. "L1 for this slice forces a labored L2") → normal push-back via the Synthesizer; that's expected process, not an exception.
- **A single rotation claim that doesn't verify** → normal Critic verdict (`revise` / `reject`).
- **Anything the agent can fix within its own role** → just fix it.

If you're not sure, it probably belongs in one of the regular channels. The bar for `problems/` is: **"the right answer to this requires authority I don't have."**

## Filename convention

`${YYYY-MM-DDTHHMMSS}Z.md` — UTC ISO 8601 timestamp with colons stripped. Generate with:

```bash
date -u +%Y-%m-%dT%H%M%SZ
```

If two problems are filed within the same second (rare given the conservative bar), suffix the second one with `-2`.

## File format

```markdown
---
created: 2026-05-23T143500Z
agent_role: critic            # explorer | synthesizer | planner | critic | other
cycle_id: 42                  # the agent cycle this surfaced in; null if outside any cycle
slice: cg_solver              # the algorithm/routine being worked on; or "global"
kind: role-conflict           # role-conflict | framing-concern | tooling-gap | skill-friction | drive-by-observation | other
---

# {one-line title}

## What

What was observed, in 2–5 concrete sentences.

## Why this is out-of-band

Why this can't be handled by the question ledger, lessons, normal push-back, or a regular Critic verdict. What role boundary or framing scope is being exceeded.

## Suggested resolution (optional)

What the agent suspects should happen. Often empty — the point is to raise the concern, not solve it.
```

## Lifecycle

Problems are reviewed **out-of-cycle** by the human, not by the running agent loop. The loop does not consume `problems/` entries. They accumulate until the next **meta-review** pass picks them up — see `book/src/meta-reviews/index.md` for the meta-review procedure and trigger (every 3 completed agent cycles per `config.toml`, or manual). Resolutions land as `BOOTSTRAP.md` updates, prompt revisions, or methodology-doc edits. Nothing in the per-cycle git history acts on them automatically.

When a problem is resolved, mark it by appending `resolved: ${timestamp}` and `resolution:` lines to the frontmatter and committing the update. **Do not delete resolved problems** — they are part of the research record.
