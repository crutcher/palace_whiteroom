# Friction ledger

Running list of NAMED friction patterns observed across cycles. One section per pattern.

**Format** (frontmatter per section):

```yaml
---
slug: short-kebab-case
first_observed: cycle-NNN  (or meta-NN)
last_observed: cycle-NNN
recurrence_count: N
status: new | recurring | escalating | addressed | resolved
addressed_by: <commit-sha> | <skill-slug> | <meta-decision> | null
---
```

**Discipline:** meta-phase appends new patterns and updates recurrence counts each cycle. Cycle-planner reads it for priority signals (recurring-but-unaddressed patterns get scheduling priority). Don't delete patterns — change status to `resolved` with `addressed_by` set.

**Status meanings:**
- `new` — observed once, no pattern yet
- `recurring` — observed ≥2 cycles, no specific fix in motion
- `escalating` — recurrence climbing despite an `addressed_by` attempt; needs revision
- `addressed` — meta-phase enacted a fix (cited); watch for recurrence
- `resolved` — `addressed` + no recurrence for ≥10 cycles

## Seed patterns (from lessons.md / meta-reviews 1–25)

The following are bootstrapped from the old loop's accumulated `lessons.md` and meta-review record. The full `lessons.md` (385 entries, 397 lines) stays in place as historical record; this ledger captures the **recurring** patterns worth tracking forward.

---

```yaml
---
slug: refinement-claims-without-surface
first_observed: cycle-115
last_observed: cycle-166
recurrence_count: 8
status: addressed
addressed_by: skills/verify-refinement-surface + prompts/synthesizer.md framework-slice anti-pattern
---
```

Refinement plans (Ln→Ln) emit `rotation_claims` without corresponding surface edits to the slice. The Critic / integrator gate catches them but the producer keeps re-emitting. Concentrated on `cg_preconditioning_framework` (4 of 8 instances). Meta-25 extracted `skills/verify-refinement-surface/` and added a framework-slice anti-pattern worked counter-example to synthesizer.md. Watch cycles 167+ under relaxed-bar and the new skill — if recurrence continues, the framework slice may need a distinct emission template.

---

```yaml
---
slug: sideways-bulk-concept-emission
first_observed: cycle-161
last_observed: cycle-161
recurrence_count: 1
status: addressed
addressed_by: skills/plan-sideways-concept-emission
---
```

SIDEWAYS plans emit many `concept_writes` for already-existing concept slugs, producing N push-back signals at integration time. Meta-25 extracted `skills/plan-sideways-concept-emission/` (pre-emit existing-concept check) and tightened synthesizer prompt. One observation, fix landed — watch for recurrence on next SIDEWAYS.

---

```yaml
---
slug: concept-slug-naming-drift
first_observed: cycle-123
last_observed: cycle-133
recurrence_count: 2
status: addressed
addressed_by: kebab-case convention in prompts/synthesizer.md
---
```

Concept files created with underscored slug duplicating an existing kebab-case slug (`solver_as_operator` + `solver-as-operator`; `complex_from_real_lift` + `complex-from-real-lift`). Resolved by deletion + bulk-rewrite + kebab-case-for-multi-word convention in synthesizer prompt.

---

```yaml
---
slug: cross-cycle-anchor-staleness
first_observed: cycle-166
last_observed: cycle-166
recurrence_count: 1
status: addressed
addressed_by: prompts/synthesizer.md cross-cycle-anchor-staleness subsection
---
```

`file_edits` on accumulating documents (lessons.md, dep-map, index.md) use stale anchors because the planner read disk earlier in the loop. Meta-25 added producer-side rule: must re-read disk at plan-emission time; prefer append-only when possible.

---

```yaml
---
slug: meta-emission-token-saturation
first_observed: cycle-meta-25-attempt-1
last_observed: cycle-meta-25-attempt-2
recurrence_count: 2
status: addressed
addressed_by: c2c0eee (max_tokens 8192→16384 + streaming) + 63af9e8 (schema null)
---
```

Meta-Critic emission tripped JSON parse errors twice on meta-25: token limit too low for new skill_pass field; schema rejected null for no_candidates_reason. Pure infrastructure friction; resolved.

---

```yaml
---
slug: problems-channel-under-utilization
first_observed: cycle-92
last_observed: cycle-166
recurrence_count: 0
status: addressed
addressed_by: 9f05b54 (relax problems/ bar + drive-by category)
---
```

Across two-and-a-half consecutive 12-cycle windows under cap=5 sensitivity, 0 problems were filed. Three escalations didn't move the rate. User intervention 2026-05-26 relaxed the filing bar (drive-by observations now qualify) and reset sensitivity to 3. Calibration in `problems-sensitivity.md`. First window under relaxed bar (152–166) also showed 0 filings but only landed mid-window; cycles 167+ are the clean measurement window.

---

```yaml
---
slug: bookkeeping-vs-substantive-conflation
first_observed: cycle-31
last_observed: cycle-43
recurrence_count: 3
status: resolved
addressed_by: orchestrator bookkeeping-vs-content downgrade fix + per-meta verification
---
```

The Critic's pass/revise/reject verdict was being driven by bookkeeping incompleteness (missing skill_uptake field, missing slice_index_updates) rather than substantive content quality. Meta-9/10 separated bookkeeping_incomplete from content verdicts; downgrades now apply only to substantive failures. Stable since.

---

```yaml
---
slug: skill-formation-under-bias
first_observed: cycle-37
last_observed: cycle-166
recurrence_count: 5
status: escalating
addressed_by: +60% skill priority directive (meta-19) — insufficient
---
```

Across 25 meta-reviews, only 5 skills extracted. The +60% directive raised the rate to ~1/meta but the structural cap (only Meta-Critic can promote) limited it. Meta-25 finally doubled the rate to 2 skills/meta. **Open under the new flow**: the open skill-candidates channel (any-agent appendable) is meant to address this. Watch the new flow's skill-candidate append rate and meta-phase promotion rate during Phase F pilot.

---

```yaml
---
slug: gmres-restart-edge-cases
first_observed: cycle-168
last_observed: cycle-168
recurrence_count: 1
status: new
addressed_by: null
---
```

Cycle 168 (refinement gmres) emitted a revise verdict on restart-boundary edge cases (Hessenberg column extension at restart boundary). Specific to the GMRES restart subtlety — likely needs a dedicated edge-case-aware emission pattern. Watch under future GMRES touches.

---

```yaml
---
slug: subagent-file-write-blocked-general-purpose
first_observed: pilot-1
last_observed: pilot-1
recurrence_count: 1
status: addressed
addressed_by: skills/embed-and-persist-subagent-dispatch/SKILL.md
---
```

General-purpose subagents dispatched via the `Agent` tool from this session cannot write files in the parent's working tree — the harness intercepts and returns content as text. Observed pilot-1 when dispatching `harvester` on `axpy@L1`. Mitigation: `skills/embed-and-persist-subagent-dispatch` documents the pattern (main session persists what the subagent returns). Open `ask`: investigate whether custom `.claude/agents/<name>.md` definitions are active post-Claude-Code-restart — if so, direct subagent_type=<custom-name> dispatch would bypass this friction.
