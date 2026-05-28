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

```yaml
---
slug: cycle-planner-discipline-read-role-spec-first
proposer: meta-phase
proposed_at: cycle-002 / 2026-05-26
status: deferred
deferred_at: cycle-004 / 2026-05-27
deferred_reason: cycle-003 + cycle-004 cycle-planner runs both honoured one-operator-per-invocation; the user-directive 8fc3a07 (parallel-when-in-doubt) + cycle-planner.md Discipline updates absorbed the constraint check at the role-spec level. Skill is unnecessary unless recurrence climbs.
---
```

**Motivating observation**: cycle-002 haiku cycle-planner proposed a multi-operator harvester dispatch (`dot`, `nrm2`, `scal` in one invocation), violating harvester's "one operator per invocation" role spec. Parent corrected at dispatch time. Friction-ledger entry `haiku-cycle-planner-over-scopes-harvester` (recurrence-1).

**Sketch of procedure**: Before emitting any `(agent, scope, deps)` tuple, the cycle-planner reads the target agent's `.claude/agents/<name>.md` and checks for "one X per invocation" / "single-scope" / "atomic dispatch" constraints. Rejects multi-target scopes for atomic agents. Emits one tuple per atomic dispatch.

**Cycle-004 deferral rationale**: cycle-003 + cycle-004 cycle-planner emissions both produced atomic per-operator dispatches without over-scoping (cycle-004 plan: 7 dispatches, one operator each). The user-directive philosophy (parallel-when-in-doubt) appears to have absorbed the previous over-caution. If `haiku-cycle-planner-over-scopes-harvester` recurs in cycle-005+, revisit promotion.

## Open candidates (cycle-004 additions)

```yaml
---
slug: vocabulary-cohort-subsection-template
proposer: layer-intro-author (cycle-004)
proposed_at: cycle-004 / 2026-05-27
status: promoted-as-role-spec-template
promoted_to: .claude/agents/layer-intro-author.md §Vocabulary-cohort subsection
---
```

**Motivating observation**: cycle-004 L1 layer-intro refresh introduced a "Vocabulary cohort" subsection that split the dep-map into Firm-at-L_n / Queued-at-L_n cohorts. The pattern is transferable to L2, L3, L4 layer intros when each reaches ≥3 firm operators with rough-ins coexisting. Flagged by layer-intro-author as transferable.

**Sketch of procedure**: documented as a template in `.claude/agents/layer-intro-author.md` rather than as a standalone skill, because the procedure is intrinsic to the role rather than cross-role-invocable. Reuse mechanism: future layer-intro-author invocations read the role spec, see the template, apply when the threshold (≥3 firm + ≥1 queued) is met.

**Promotion bar check**: pattern observation = 1 instance (cycle-004); friction-ledger entry = none (this is positive-pattern, not friction); sketch concrete enough = ✓. Default-accept under low-bar policy; promoted as **role-spec template** rather than as standalone skill because the procedure is intrinsic to the layer-intro-author role and does not need cross-role invocation. Watch for L2/L3/L4 application as those layers reach the threshold.



## Open candidates (cycle-005 additions)

```yaml
---
slug: summary-md-surgical-insert
proposer: meta-phase (cycle-005)
proposed_at: cycle-005 / 2026-05-27
status: promoted
promoted_to: skills/summary-md-surgical-insert/SKILL.md
---
```

**Motivating observation**: across cycles 003–005, multi-writer waves on `book/src/SUMMARY.md` (2 → 5 → 5 concurrent writers) have scaled without conflict given a specific discipline: each per-report integrator re-reads SUMMARY.md fresh at apply time, uses literal-string anchors for the insert location (sibling-chapter row under a Part, or H1 heading), and the first per-report integrator in a cycle documents the "preserve append-points for subsequent in-cycle integrators" rule in their STAGING Notes — which subsequent integrators echo. Friction-ledger entry `summary-md-serial-write-discipline` (recurrence-3).

**Sketch of procedure**: a per-report-integrator-facing skill that codifies the four-step discipline: (1) re-read SUMMARY.md just-in-time, (2) locate sibling-chapter anchor under the relevant Part, (3) Edit using literal-string anchor (not byte offset), (4) record the insert in STAGING Notes including the "preserve append-points" hint when other in-cycle integrators may follow.

**Promotion bar check**: pattern observation = 3 cycles (recurrence-3 in friction-ledger); friction-ledger entry exists (`summary-md-serial-write-discipline`); sketch concrete enough = ✓. Default-accept under low-bar policy. **Promoted this meta-phase.**

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

## Open candidates (cycle-010 additions)

```yaml
---
slug: phase-1-slice-reduction-audit
proposer: critic (cycle-010, audit of 2026-05-27T220000Z-same-layer-cross-cutter-phase-1-corpus-reduction-audit)
proposed_at: cycle-010 / 2026-05-27
status: proposed
---
```

**Motivating observation**: cycle-010's first-instance Phase 1 corpus reduction audit (priority #19) established a four-part template (Supersession map / Residual gaps / Recommended action / Proposed changes per slice). Critic review surfaced three recurring friction points likely to repeat at cycle-011+ replay: (a) slice line-range citations drift by 1-2 lines from actual `## H2` boundaries unless anchored by an upfront `grep -n "^## "` enumeration; (b) Recommended-action narrative and proposed_change line ranges are produced separately and can disagree (the first instance's cg.md had a section the narrative said to stub but the line range retained); (c) the slice's section table-of-contents is implicit in long supersession-map prose, making cross-section audit harder. Each will recur on the remaining 7 slices unless the template is crystallized.

**Sketch of procedure**: a `same-layer-cross-cutter`-facing skill that prescribes: (1) enumerate slice section anchors first via `grep -n "^## " <slice>` and emit them as a fixed table at the top of the dispatch report; (2) for each section, populate four columns — section name, actual line range, supersession status (full / partial / none), firm-entry pointer(s); (3) Residual gaps section enumerates only the partial / none rows; (4) proposed_change line ranges are derived mechanically from the section-anchor table, not from prose; (5) a final reconciliation step verifies narrative-and-range agreement before report emission.

**Promotion bar check**: pattern observed = 1 instance (cycle-010 first instance); friction-ledger entry = candidate-creation pending (the template-drift pattern hasn't fired twice yet); sketch concrete enough = ✓ (four-step procedure could be written as SKILL.md). Falls below the "≥2 cycles" promotion bar but well above the "candidate sketch concrete enough" bar. Recommend default-accept under low-bar policy because the remaining 7 slices are queued and template drift will compound across them.

**Cycle-011 uptake-note (appended by repairer of `2026-05-27T234651Z-same-layer-cross-cutter-phase-1-corpus-reduction-batch-2`):** cycle-011's batch-2 audit dispatch is the **second instance** of the cycle-010 template execution. The dispatch directly followed the four-part template, applied the cycle-010 friction-signal mitigation (`grep -n "^## "` H2 enumeration before line-range arithmetic), and still produced ~10 minor citation off-by-ones (4 of which were citation/line-range drift — the same shape this skill candidate is designed to prevent). This confirms recurrence-2 of the template-drift pattern, clearing the "≥2 cycles" promotion bar. In addition, the cycle-011 critic surfaced the proposed_changes-block bracketed-prose syntax as a separate template-friction signal (issue 10 in `META.md` critique) — a likely **cycle-012 meta-phase template-improvement candidate** that may extend this skill's scope (mechanical-not-interpretive proposed_changes blocks). Meta-phase batch-2 (after cycle-012 integrator-finalize) should promote this candidate to firm `skills/phase-1-slice-reduction-audit/SKILL.md` and consider whether to fold the proposed_changes-block format-friction into the same skill or a sibling.

## Rejected

(none yet)
