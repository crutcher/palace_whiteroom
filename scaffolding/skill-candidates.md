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

(none yet — bootstrapped at Phase B; first candidates expected from Phase F pilot)

## Promoted

(existing skills under `skills/` are the prior loop's promotions; they don't need backfilling here. Forward-promoted skills will be listed below as they happen.)

## Rejected

(none yet)
