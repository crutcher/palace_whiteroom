# Problems channel

This directory is the **out-of-band concern channel** for agents working in this repository. An agent files a problem when it notices something *outside its own role's scope* that the global process should review — not solve, just review.

**Filing rate is self-tuned.** The bar described below is the *default* (sensitivity 3). The actual sensitivity is set in `scaffolding/problems-sensitivity.md` and ranges 1-5; the orchestrator injects `problems_sensitivity: <N>` into per-cycle agent prompts. Target rate: **1 problem filed per 15 agent runs**. The Meta-Critic recalibrates the sensitivity at each meta-cycle based on the actual rate over the last 2 windows.

## When to file a problem

The temperature for filing here is **conservative**. The channel exists for cross-cutting concerns that don't fit any of the regular per-cycle channels. Specifically:

- **Out-of-role conflicts** — the agent notices something that belongs to a different role's authority. Example: a Critic notices that the Synthesizer prompt is consistently producing claims at the wrong layer; that's a Synthesizer-prompt issue, not a per-claim Critic verdict.
- **In-line framing concerns** — the agent notices that the methodology framing, as currently described, doesn't fit the slice in hand, in a way that exceeds the agent's responsibility to handle. Example: an Explorer realizes the L0/L1 boundary is unclear for a particular file (generated code, heavy macros, language extensions) and is being asked to make a judgment call the prompt doesn't address.
- **Tooling / infrastructure gaps** — the agent hits a wall it can't work around within its own role. Example: a tree-sitter query that should localize a region returns nothing because the grammar doesn't parse that file's dialect; a citation comes back empty for a reason the prompt didn't anticipate.
- **Skill friction** — a skill the agent invoked (per `skills/<name>/SKILL.md`) consistently fights its task: the procedure doesn't fit recurring cases, its output format forces awkward fits, the schema it produces is structurally inadequate, or the assumed MCP tools don't behave as expected. Per-cycle agents do not modify skills (skill management is Meta-Critic / meta-review work, Medium cascade); they flag. Example: the Critic invokes `verify-rotation-citation` and finds the `kind` enum in `critic_verdict.json` has no category for the failure they're observing. **Single-edge-case is not skill-friction; recurring mismatch is** — the conservative-temperature rule still applies.

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
kind: role-conflict           # role-conflict | framing-concern | tooling-gap | skill-friction | other
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
