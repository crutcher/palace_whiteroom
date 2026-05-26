# Skill candidates

Appendable channel for skill proposals. Any agent (sub-agent, critic, repairer, integrator) that notices a procedural pattern recurring or worth crystallizing appends a candidate here. Meta-phase reads each cycle and promotes when the bar is met.

**Format** (one section per candidate):

```yaml
---
slug: short-kebab-case
proposer: <agent-name>
proposed_at: cycle-NNN | meta-NN | YYYY-MM-DD
status: proposed | evaluating | promoted | deferred | rejected
promoted_to: skills/<slug>/SKILL.md  (when status=promoted)
rejected_reason: <one-line>          (when status=rejected)
---
```

Each section: **slug**, **motivating observation** (1 paragraph), **sketch of procedure** (1 paragraph), and **status** with optional rationale.

**Discipline:**
- Any agent appends; never edits existing sections.
- Meta-phase advances status (proposed → evaluating → promoted/deferred/rejected).
- Promotion writes `skills/<slug>/SKILL.md` and sets `promoted_to`.
- Rejection is explicit (not silent abandonment) with reason — the record helps avoid re-proposal.

**Promotion bar (intentionally low):**
- Procedural pattern observed ≥2 cycles, OR
- Candidate sketch is concrete enough to write as a SKILL.md, OR
- Friction-ledger entry exists for a pattern this skill would address.

The cost of a too-eager promotion is an unused SKILL.md; the cost of under-promotion is missed pattern capture across many cycles. **Default-accept** in ambiguous cases.

## Open candidates

(none currently — first candidate from pilot-1 was promoted same-cycle; see Promoted section)

## Promoted

```yaml
---
slug: embed-and-persist-subagent-dispatch
proposer: meta-phase
proposed_at: pilot-1 / 2026-05-26
status: promoted
promoted_to: skills/embed-and-persist-subagent-dispatch/SKILL.md
---
```

**Motivating observation**: pilot-1 dispatched harvester via `Agent(subagent_type=general-purpose, ...)` and the harness blocked the subagent's file writes; subagent returned content as text. Main session persisted manually. Same friction will reoccur every dispatch until `.claude/agents/<name>.md` definitions are active.

**Sketch of procedure**: embed agent prompt + scope in Agent call; receive content as text; persist in parent session via Write tool; record friction in cycle-record.

**Promotion bar check**: candidate sketch is concrete enough to write as SKILL.md (✓); friction-ledger entry exists for `subagent-file-write-blocked-general-purpose` (✓); pattern will recur every dispatch until resolved (✓). Default-accept under low-bar promotion policy.

(Existing skills under `skills/` are the prior loop's promotions; they don't need backfilling here.)

## Rejected

(none yet)
