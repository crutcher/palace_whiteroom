---
name: embed-and-persist-subagent-dispatch
description: When dispatching a specialized agent via the Agent tool, embed the agent's prompt + scope in the invocation and persist returned content in the parent session. Use when the Claude Code subagent harness blocks subagent file writes (the default behavior for general-purpose subagents).
status: active
promoted_at: pilot-1 / 2026-05-26
promoted_by: meta-phase
---

# Embed-and-persist subagent dispatch

## When to invoke this skill

You're orchestrating a cycle of the new 6-phase flow and need to dispatch one of the 13 specialized agents (harvester, abstractor, lifter, etc.). You're using `Agent(subagent_type=general-purpose, ...)` because:

- The `.claude/agents/<name>.md` definitions don't appear in the available-subagent-type list (typically because they were added mid-session and Claude Code hasn't reloaded), OR
- You're verifying agent prompts work as documented before relying on direct subagent dispatch.

## What the harness does

A general-purpose subagent invoked from this session **cannot write files in the parent's working tree**. The harness intercepts file-write attempts and returns content as text in the subagent's final response.

This is friction pattern `subagent-file-write-blocked-general-purpose` in `scaffolding/friction-ledger.md`.

## The pattern

Three steps:

### 1. Embed

In your `Agent(prompt=...)` call, embed:

- A pointer to the agent definition: `"You are the <name> subagent. Your full role definition is at /home/crutcher/git/palace_whiteroom/.claude/agents/<name>.md — read it first."`
- A pointer to the project spec: `"Project context: /home/crutcher/git/palace_whiteroom/MIGRATION.md (especially §2 Cycle structure)."`
- The concrete scope: which operator / theme / observation.
- The exact target file paths: where the REPORT.md will land, what files to read.
- A closing instruction: `"When done, print the REPORT.md path you wrote to and a brief (under 200 words) summary of what you produced."`

### 2. Receive

The subagent returns text. Look for:

- The REPORT.md content (often inside a fenced markdown block).
- The agent's self-summary at the end.
- Any meta-commentary (e.g., "harness blocked file write; returning content as text").

### 3. Persist

In the parent session:

- Create the report directory: `mkdir -p reports/<timestamp>-<agent>-<scope>/`
- Write the REPORT.md content via `Write` tool.
- Record the friction observation (one line in `cycle-record.jsonl` `friction_observed` field).

Then proceed with the next phase (critic on the persisted report).

## Anti-pattern

Don't try to make the subagent write the file by passing it a fake-permission instruction or by chaining tool invocations. The harness will block; you'll waste a dispatch.

## When the friction is gone

Once `.claude/agents/<name>.md` definitions are active (verifiable by `Agent(subagent_type=harvester, ...)` working directly), this skill's invocation becomes optional — the subagent can write directly. Keep the skill until the friction-ledger entry's status flips to `resolved`.

## Worked example (pilot-1)

Dispatched harvester on `axpy@L1` via `Agent(subagent_type=general-purpose, ...)`. Subagent returned a complete REPORT.md as text + meta-commentary about the harness block. Parent session persisted to `reports/2026-05-26T223039Z-harvester-axpy-L1/REPORT.md`. Downstream phases (critic, repairer, integrator) ran normally on the persisted file. Cycle completed cleanly.
