# Agent definitions

13 Claude Code subagent definitions for the layered-specification migration. See `../../MIGRATION.md` for the full migration plan and cycle structure.

## Cycle structure

A cycle is 6 phases. Agents that fire each phase:

| Phase | Agents | Granularity |
|---|---|---|
| 1. plan | `cycle-planner` | 1 serial |
| 2. dispatch | 8 specialized (below) | parallel waves per plan |
| 3. critique | `critic` | scatter/gather (1 per report) |
| 4. repair | `repairer` | scatter/gather (1 per report with findings) |
| 5. integrate | `integrator` | 1 serial |
| 6. meta | `meta-phase` | 1 serial |

## The 13 agents

**Pre-dispatch (1):**
- [`cycle-planner.md`](./cycle-planner.md) — serial dispatch planner.

**Specialized dispatch (8):** — each writes one REPORT.md per invocation; never modifies the artifact directly.
- [`layer-intro-author.md`](./layer-intro-author.md) — L_n intros + dep-maps.
- [`harvester.md`](./harvester.md) — formalizes one L_n operator per invocation.
- [`abstractor.md`](./abstractor.md) — sketches one L_{n+1}>L_n theme + speculative L_{n+1} operators.
- [`lifter.md`](./lifter.md) — re-anchors a theme to firmed-up vocabulary.
- [`lowering-verifier.md`](./lowering-verifier.md) — audits one theme against evidence.
- [`combinator-miner.md`](./combinator-miner.md) — finds one recurrent pattern, proposes a combinator.
- [`same-layer-cross-cutter.md`](./same-layer-cross-cutter.md) — one unification/redundancy/contradiction observation.
- [`cross-layer-cross-cutter.md`](./cross-layer-cross-cutter.md) — one cross-layer coverage-gap/edge-mismatch observation.

**Post-dispatch validation (2):**
- [`critic.md`](./critic.md) — runs 8-check checklist per report; writes META.md critique section.
- [`repairer.md`](./repairer.md) — attempts in-place fixes per critic finding; writes META.md repair section; sets overall_status.

**Application (1):**
- [`integrator.md`](./integrator.md) — applies ready reports; runs safety-net gates; rebuilds book; commits + pushes.

**Methodology (1):**
- [`meta-phase.md`](./meta-phase.md) — examines cycle evidence; records trends; proposes/judges/decides methodology adjustments; enacts go-items.

## Write-authority partition

- 8 specialized agents → `reports/<id>/REPORT.md` + supporting docs only.
- critic → `reports/<id>/META.md` critique section.
- repairer → `reports/<id>/META.md` repair section + in-place edits to REPORT.md / supporting docs in same dir.
- integrator → `book/`, `scaffolding/roadmap.md`, `scaffolding/cycle-record.jsonl`, `scaffolding/open-questions.md`, `log/`.
- meta-phase → `.claude/agents/`, `skills/`, `scaffolding/priorities.md`, `scaffolding/friction-ledger.md`, `scaffolding/skill-candidates.md`, `scaffolding/problems-sensitivity.md`, channel-format specs.
- cycle-planner → `reports/<id>/REPORT.md` (its own plan report).

## Open append channels

Any agent (sub-agent, critic, repairer, integrator) may append to:
- `scaffolding/skill-candidates.md` — propose a skill when a procedural pattern is observed.
- `scaffolding/open-questions.md` — surface a question (the integrator also promotes per-report Open questions here).
- `scaffolding/decisions/` — log a persistent-dual trade-off.
- `scaffolding/test-linkages/` — record a source↔test mapping.

These are append-only: agents add sections, never edit existing sections.

## Invocation

The main Claude Code session orchestrates the cycle. Two dispatch patterns are currently supported:

### Direct subagent dispatch (preferred, when supported)

```
Agent(subagent_type="<name>", description="<scope>", prompt="<scope+inputs>")
```

Where `<name>` is one of the 13 agents below. The subagent gets isolated context, reads/writes files directly via its tools, and writes its REPORT.md to disk. The main session does NOT itself write to the artifact — it dispatches, waits for reports, dispatches the verify phases, dispatches the integrator (which mutates the artifact), then dispatches meta-phase.

### Embed-and-persist dispatch (fallback)

When `subagent_type=<custom-name>` doesn't resolve (e.g., custom agent definitions not yet picked up by Claude Code), use `subagent_type=general-purpose` and embed the agent's prompt + scope in the `Agent(prompt=...)` call. The subagent returns content as text; the main session persists it to disk via `Write`.

See `../../skills/embed-and-persist-subagent-dispatch/SKILL.md` for the procedure. This fallback was introduced by pilot-1 meta-phase after the harness blocked subagent file writes.

To verify direct dispatch is available, try `Agent(subagent_type="harvester", description="test", prompt="echo hi")` — if it errors with "unknown subagent type," the fallback is required for this session.
