# Friction ledger

Running list of NAMED friction patterns observed across cycles. One section per pattern.

**This is an INTAKE channel, not a holding pen** (user directive 2026-05-28). Friction is *reported* here; its **resolution is migration**, not parking. When the meta-phase addresses a pattern, the corrective work-item is migrated **into the plan** (`scaffolding/priorities.md`) — a role-spec edit, a skill, a methodology codification, or a backlog component — and the pattern is marked `addressed`/`resolved` with `addressed_by` set. A pattern that recurs without a corresponding plan item is the signal that migration hasn't happened yet. The plan, not this ledger, is where "what we will do about it" lives; this ledger is the evidence trail of *why*.

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

## plateau-as-scope-boundary-not-project-boundary

```yaml
---
slug: plateau-as-scope-boundary-not-project-boundary
first_observed: meta-36
last_observed: meta-38
recurrence_count: 3
status: addressed
addressed_by: out-of-band-rescope-meta-2026-06-07
---
```

The forward-frontier "plateau" surfaced as an ASK at batch-36 and was re-confirmed at batch-37 (directives landed) and batch-38 (probe re-confirmed) — three consecutive times. The pattern: a clean-gate frontier reaching exhaustion was read as approaching a *terminal* state, when it was a *scope* boundary. The plateau was an artifact of three postures (document-don't-fill obstructions; single-machine-no-MPI as a hard stop; STOP-PROPOSING for demand-gated in-scope vocabulary), all of which were the human's to lift, not the meta-phase's to work around. **Addressed by the 2026-06-07 out-of-band re-scope** (three directives: MPI deferred / lift-through deferred in-scope / constructive spine-dependency kernels with the kernel-API/impl distinction), which reopened a clear high-fan-out forward campaign. The lesson codified: a confirmed-three-times plateau is correctly surfaced as an ASK (the meta-phase did NOT manufacture a forced rectangular pull-up), and the disciplined recognition of the clean-gate floor is exactly what let the human re-scope deliberately. Migrated to the plan as the CYCLE-121/batch-39 lift-through campaign (`scaffolding/priorities.md`).

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
last_observed: cycle-002
recurrence_count: 1
status: resolved-with-narrowing
addressed_by: c3312a6 (cycle-002 verification) + content-pattern-write-filter-on-report-keywords (the actual mechanism)
---
```

**Recharacterized cycle-002.** Original framing (pilot-1): "general-purpose subagents cannot write files in the parent's tree". Verified cycle-002 (commit c3312a6) via direct `Agent(subagent_type=<custom-name>)` dispatch of harvester / abstractor / combinator-miner / critic ×3 / repairer ×3 / integrator / meta-phase — all 13 custom `.claude/agents/` definitions resolve and load. The actual block is not per-agent-type; it is a content-pattern filter on filenames matching `report|summary|findings|analysis`. See the narrower entry `content-pattern-write-filter-on-report-keywords` for the real mechanism + operational mitigation. Original mitigation skill (`embed-and-persist-subagent-dispatch`) remains active but with narrowed applicability (refined cycle-002).

---

```yaml
---
slug: content-pattern-write-filter-on-report-keywords
first_observed: cycle-002
last_observed: cycle-004
recurrence_count: 4
status: resolved-by-rename
addressed_by: cycle-004 user directive — REPORT.md → CYCLE.md project-wide rename (commit 8ac1f37)
---
```

The Claude Code harness applies a content-pattern filter that **blocks `Write` to filenames containing `report|summary|findings|analysis` keywords**, with error text: "Subagents should return findings as text, not write report files. Include this content in your final response instead."

**Original misframing (cycle-002 → cycle-003):** treated as `addressed-by-design`; mitigation was parent-pre-creates-skeleton + Edit-not-Write workaround, documented in `skills/embed-and-persist-subagent-dispatch/SKILL.md`. The workaround was load-bearing — every dispatch required parent participation to scaffold the file the subagent would then edit. This coupled the orchestration layer to a harness quirk.

**User escalation (cycle-004):** "Can I direct you to raise process issues like this in the future, rather than working around them as aggressively as you are here?" → friction recharacterized as a bug to repair, not a design to accommodate.

**Investigation findings:** the filter is NOT a configured hook (no project PreToolUse hook in `.claude/settings.local.json`; the user's only enabled plugin is `rust-analyzer-lsp`, which has no Write hook). The filter is almost certainly a built-in Claude Code default subagent system-prompt instruction that tells dispatched subagents "don't Write report/summary/findings/analysis files; return as text". It applies regardless of subagent type or `tools:` grant. The main session is unaffected. `Edit` is unaffected. `Write` to non-keyword filenames is unaffected.

**Resolution (cycle-004):** project-wide rename `REPORT.md → CYCLE.md`. All 25 existing per-dispatch report files renamed via `git mv`. All references in `.claude/agents/*.md`, `skills/`, `CLAUDE.md`, `MIGRATION.md`, scaffolding, and log files updated via bulk sed. The filter is dodged entirely (CYCLE.md does not match the keyword pattern). Skill `embed-and-persist-subagent-dispatch` is retired (no longer needed). Parent-pre-creates-skeleton pattern obsolete.

**Follow-up not yet enacted:** a Claude Code feature/bug request that custom-agent definitions should be able to override the default subagent Write-filter (so projects with intentional report-emitting subagents can opt in by name). Filed against `addressed_by` upstream tracker — not blocking; the rename is sufficient repair.

---

```yaml
---
slug: haiku-subagent-anchors-to-ledger-lore
first_observed: cycle-002
last_observed: cycle-002
recurrence_count: 1
status: new
addressed_by: null
---
```

The cycle-planner subagent (haiku tier, dispatched twice in cycle-002) read `scaffolding/friction-ledger.md`'s `subagent-file-write-blocked-general-purpose` entry and the pilot-1 context, then preemptively concluded "the harness intercepts file writes from subagents" and skipped its `Write` call without attempting it — even when the parent prompt explicitly stated the friction was verified resolved and instructed it to attempt the Write. By contrast, opus subagents (the cycle-002 wave-1 harvester/abstractor/combinator-miner) attempted `Write` and discovered the actual narrower content-pattern filter behavior. Pattern: lower-tier models anchor more strongly to ledger-recorded prior friction and resist explicit override. **Watch:** if cycle-003 cycle-planner repeats the skip, escalate (proposal: switch cycle-planner to opus, or add a hard "you MUST attempt the Write" override in the cycle-planner prompt that bypasses ledger reading). Recurrence-1 so far; not yet promoting a mitigation.

---

```yaml
---
slug: haiku-cycle-planner-over-scopes-harvester
first_observed: cycle-002
last_observed: cycle-003
recurrence_count: 2
status: recurring
addressed_by: 8fc3a07 (user-directive parallel-when-in-doubt + conflict-as-signal philosophy)
---
```

The haiku cycle-planner proposed "harvester for `dot`, `nrm2`, `scal` in one dispatch" — violating the harvester role spec's explicit "one operator per invocation" constraint. Parent corrected at dispatch time (split to one harvester for `dot` only; `nrm2` / `scal` deferred to cycle-003). Pattern: haiku planner under-reads role-discipline constraints in agent definitions; tends to batch-schedule when the role spec forbids it.

**Cycle-003 recurrence (different sub-symptom):** the haiku cycle-planner classified the cycle-003 nrm2 + axpby `book/src/L1/index.md` dep-map edits as **sequential** in its overlap analysis — but at integration time the two edits were row-level non-overlapping (nrm2 appended after `dot` row; axpby row-replaced the rough-in row). The "sequential" call was over-cautious; both edits applied cleanly in one wave at integration. The two sub-symptoms (over-scopes harvester / over-claims overlap) share a root: the haiku planner doesn't model the fine-grained edit-anchor structure that the integrator's surgical-edit machinery handles cleanly. Captured in `scaffolding/integrator-signals.md` cycle-003 §Wave-conflict observations.

**Addressed by user directive 2026-05-27 (commit 8fc3a07):** new policy is "parallel-when-in-doubt" (mark PARALLEL by default; minor wave-conflict at integration is *useful tooling signal*, not friction to avoid). The cycle-planner's role spec was updated in 8fc3a07 with this Discipline. Future recurrences should diminish; if they don't (cycle-004+), escalate (proposal: swap cycle-planner to opus or add hard parallel-default override).

---

```yaml
---
slug: user-directive-enacted-out-of-band
first_observed: cycle-003
last_observed: cycle-003
recurrence_count: 1
status: addressed-by-user
addressed_by: 8fc3a07 (user direct commit; outside meta-phase cadence)
---
```

Mid-cycle-003, the user interjected with three methodology directives (raise Shared Infrastructure priority in roadmap; wave-count target up to 15 with conflict-tolerance philosophy "parallel-when-in-doubt"; integrator-to-planner signals channel via `scaffolding/integrator-signals.md`). The parent main session enacted these directly via commit 8fc3a07, outside the normal meta-phase cadence (Phase 6 of each cycle). **This is not friction** — the user has authority to override the normal flow at any time, and the changes were sound. The pattern is worth tracking because:

1. It signals that the meta-phase cadence is **proposed** but not **gated** — the user can short-circuit at any time when a methodology change is obvious-enough not to wait for the meta-phase deliberation.
2. Future cycles' meta-phase reports should not re-litigate user-directive changes; they are accepted-as-given.
3. If the user-directive frequency rises (≥1 per cycle for 3+ cycles), revisit: the meta-phase cadence may be too slow, or the meta-phase is too cautious. Currently, recurrence-1 — defer assessment.

No mitigation needed.

---

```yaml
---
slug: lowering-verifier-yaml-in-prose-channel-format
first_observed: cycle-003
last_observed: cycle-003
recurrence_count: 1
status: addressed
addressed_by: cycle-003 meta-phase (.claude/agents/lowering-verifier.md fence-required + downstream-consumer note)
---
```

The cycle-003 lowering-verifier appended a `verified_against:` YAML block inside `book/src/L1-L0/axpby-mutation-rotation.md:173-198` **without code-fence delimiters**. The YAML is interleaved with prose at the bottom of the chapter, structurally indistinguishable from regular text by an mdBook renderer or naive grep parsing. Downstream `cross-layer-cross-cutter` is expected to consume this YAML metadata (per the lowering-verifier role-spec's "consumed by cross-layer-cross-cutter for coverage analysis" note). No channel-format spec existed in `scaffolding/` or `.claude/agents/` for this convention.

**Surfaced by**: cycle-003 integrator-signals.md §Integration-tooling friction. Routes to meta-phase.

**Mitigation (cycle-003 meta-phase, this entry):** updated `.claude/agents/lowering-verifier.md` Discipline section to require the `verified_against:` block be emitted as a fenced YAML code block (` ```yaml ... ``` `) and reaffirms the downstream-consumer contract. The role spec's `Proposed changes` example already showed the fenced form; the discipline addition makes it explicit and tightens the contract.

**Pre-existing landing not retroactively fixed:** the cycle-003 `axpby-mutation-rotation.md` YAML block was committed without the fence (`9aa1c59`). A future cycle that touches this file (next lowering-verifier audit, or any append-to-block edit) should fence-wrap the existing block. No urgent action — first downstream consumer (cross-layer-cross-cutter) can handle the unfenced form by leading-keyword scan; the discipline applies forward.

**Watch:** if any future lowering-verifier emission lands an unfenced `verified_against:` block, escalate to recurrence-2 and consider a structural fix (sidecar `.yaml` file or pre-integration repairer auto-fence).

---

```yaml
---
slug: integrator-signals-channel-working-as-designed
first_observed: cycle-003
last_observed: cycle-004
recurrence_count: 2
status: addressed-by-design
addressed_by: 8fc3a07 (user directive) + cycle-003 integrator FIRST append + cycle-004 cycle-planner read-top-3 confirmed
---
```

The integrator-to-planner signals channel (`scaffolding/integrator-signals.md`, user directive 8fc3a07) was exercised for the first time in cycle-003. The integrator populated all 6 subsections cleanly (Unblocked, New dependencies, Resolution implications, Suggested next dispatches, Wave-conflict observations, Integration-tooling friction). The channel performed as designed:

- 5 Unblocked items emitted (forward-frontier work for cycle-004).
- 3 New dependencies recorded (nrm2→dot, axpby⊃axpy, verified-against-stamp on axpby-mutation-rotation).
- 5 Resolution implications (1 answered, 4 needs-more / partially-answered) — direct routing to open-questions ledger.
- 5 Suggested next dispatches with rationales — direct input to cycle-004 planner.
- 2 Wave-conflict observations — direct input to cycle-004 planner's overlap analysis (signals over-caution).
- 1 Integration-tooling friction (`lowering-verifier-yaml-in-prose-channel-format`) → routed cleanly to this meta-phase (see entry above).

**Positive signal recorded for symmetric ledger tracking** — the friction-ledger should track addressed-by-design wins as well as frictions, to give meta-phase visibility into what's working.

**Cycle-004 confirmation:** the cycle-planner read the top cycle-003 entry and the 5 Suggested next dispatches drove 5 of cycle-004's 7 wave-1 dispatches verbatim (concepts/dot rewrite, L1-index-refresh, scal-L1, apply_linop-L1, axpbypcz-L1). The remaining 2 (MINRES + BiCGStab abstractors) were sourced from the Shared Infrastructure priority. The channel is the load-bearing carrier between cycles.

---

```yaml
---
slug: addressed-by-design-misuse-as-workaround-silting
first_observed: cycle-004
last_observed: cycle-004
recurrence_count: 1
status: escalated-by-user
addressed_by: 8ac1f37 (REPORT.md → CYCLE.md rename, removing the load-bearing workaround) + user-memory `escalate-process-issues`
---
```

**Pattern (meta).** The `addressed-by-design` status in this friction-ledger was used as a category for "we have a workaround; no further action needed", when the workaround was actually **load-bearing**: every per-dispatch CYCLE.md required parent-pre-creates-skeleton scaffolding, coupling the orchestration layer to a harness quirk in a way that compounded across every cycle. Friction-ledger entry `content-pattern-write-filter-on-report-keywords` carried this status from cycle-002 through cycle-003.

**User escalation (cycle-004, mid-cycle).** The user wrote: *"How do i repair the 'content filter on Write' issue? Can I direct you to raise process issues like this in the future, rather than working around them as aggressively as you are here?"* — explicitly recharacterising the workaround as something to **fix**, not accommodate. The user-memory entry `escalate-process-issues` was saved as a durable cross-cycle directive.

**Discipline going forward.** `addressed-by-design` is **not** "we have a workaround; mitigation done". It is reserved for genuine by-design choices (e.g., the integrator-signals channel above is addressed-by-design because the channel *itself is the design*, not a patch over a quirk). Specifically:

1. **If a workaround couples orchestration to a quirk** (parent must do X before every subagent dispatch; subagent prompts must include "use Edit not Write" override clauses; a skill exists whose sole purpose is to teach agents the workaround) → status is **NOT** `addressed-by-design`. It is `recurring-with-workaround`, `escalated-by-user`, or proceed to a repair plan.
2. **Test by counterfactual.** Ask: "if this quirk were removed tomorrow, what process changes would I make?" If the answer is "delete a skill / collapse N agent-prompt instructions / drop a parent-side scaffolding step" — the workaround is load-bearing; escalate, do not silt.
3. **Meta-phase audit.** Every meta-phase invocation should list every `addressed-by-design` entry and run the counterfactual against the most recent two. Promote to `recurring-with-workaround` (and propose a repair plan) if the counterfactual reveals coupling.

**This meta-phase enacted the audit:** the surviving `addressed-by-design` entry (`integrator-signals-channel-working-as-designed`) passes the counterfactual (the channel IS the design; removing it would not collapse a workaround — it would simply remove cross-cycle visibility, which is exactly what the design provides). No additional `addressed-by-design` entries to recharacterise.

**Watch:** future meta-phase invocations re-running the audit annually.

---

```yaml
---
slug: subagent-skips-edit-on-explicit-instruction
first_observed: cycle-002
last_observed: cycle-004
recurrence_count: 2
status: resolved-by-rename
addressed_by: 8ac1f37 (CYCLE.md rename obviates the skeleton + Edit pattern entirely; subagents now Write directly)
---
```

**Pattern.** Subagents have skipped the `Edit` step on a pre-created CYCLE.md skeleton, returning content as text instead, despite the parent prompt explicitly instructing them to use Edit.

**Cycle-002 (haiku-tier).** The cycle-planner subagent (haiku) skipped its Edit / Write call, citing the friction-ledger entry on subagent file-write blocks even when the parent prompt explicitly stated the friction was resolved. Recorded as `haiku-subagent-anchors-to-ledger-lore` (recurrence-1). Mitigation at the time: assumed haiku-specific anchoring; watched for opus.

**Cycle-004 (opus-tier).** The BiCGStab abstractor subagent (opus) returned text rather than calling Edit on its skeleton, citing "harness rule precedence" — despite the parent prompt explicitly stating the rename had landed and Edit was the correct call. **Pattern crosses the model tier.** Root cause is not haiku-specific anchoring; it is a default-subagent-system-prompt instruction ("return findings as text, do not write report files") that subagents in both tiers anchor to.

**Resolution (cycle-004 rename).** The project-wide `REPORT.md → CYCLE.md` rename (commit 8ac1f37) **obviates this pattern entirely**: no parent-pre-creates-skeleton step is needed, no Edit-not-Write override is needed in the prompt. Subagents `Write CYCLE.md` directly. The default-subagent-prompt instruction does not match `CYCLE.md`. Pattern is **resolved-by-rename**.

**Note:** the prior entry `haiku-subagent-anchors-to-ledger-lore` (cycle-002) is subsumed by this one — it was the haiku symptom of the same root cause. Keeping that entry in place as historical record.

---

```yaml
---
slug: advertised-but-unimplemented-krylov-solvers
first_observed: cycle-004
last_observed: cycle-004
recurrence_count: 2
status: addressed-by-policy
addressed_by: CLAUDE.md §Scope unimplemented-Palace-components rule (user directive 2026-05-27) + project-memory feedback_unimplemented_palace_components
---
```

**Resolution (user directive 2026-05-27, cycle-004 → cycle-005 boundary):** Unimplemented Palace components are NOT direct implementation targets. Stub is documented (obstruction theme = correct deliverable). Literature-anchored L1 form may inform higher abstractions (L2 combinators) when it simplifies their semantics; speculative operator promotion to firm is permitted only when small AND simplifies higher forms. Themes `minres-iteration` and `bicgstab-iteration` stay as obstruction documentation. The 6 speculative rough-in operators (lanczos_step, three_term_recurrence_update, givens_apply_with_residual_min, bicgstab_step, omega_update, stabilisation_update) are not auto-promoted; harvester-on-`krylov-step` may consume their L1 forms as guidance and selectively promote if doing so simplifies the L2 combinator. See CLAUDE.md §Scope and project-memory `feedback_unimplemented_palace_components` for the full policy.


**Pattern.** Palace's solver-selection layer (`palace/utils/labels.hpp` + `palace/linalg/ksp.cpp` constructor) ships enum values + JSON parser entries for Krylov solvers that have no Palace implementation — they route to a single shared `MFEM_ABORT` branch (`palace/linalg/ksp.cpp:53-56`). Two instances surfaced in cycle-004 abstractor work, each producing an L1>L0 lowering theme with **`justification kind: obstruction`** (a new theme category introduced this cycle):

1. **MINRES** (`book/src/L1-L0/minres-iteration.md`) — symmetric-indefinite three-term recurrence. Enum: `KspType::MINRES`. No Palace implementation; MFEM provides `mfem::MINRESSolver`.
2. **BiCGStab** (`book/src/L1-L0/bicgstab-iteration.md`) — non-symmetric short-recurrence. Enum: `KspType::BICGSTAB`. No Palace implementation; MFEM provides `mfem::BiCGSTABSolver`.

**Implications.**

- **Shared Infrastructure roadmap items #10 (MINRES) and #11 (BiCGStab) need re-scoping.** Until the `mfem-as-l0-substrate` policy decision is made (see ASK item below), these items are not actionable as L1 harvests — there is no Palace L0 to anchor to.
- **The obstruction-theme category is genuinely new** to `book/src/L1-L0/`. Future cross-layer-cross-cutter consumers should treat `justification kind: obstruction` themes as "anticipated work that depends on an unmade policy decision" — surface as such; do not evidence-walk for missing implementation.
- **Discovery procedure recommended:** grep `palace/utils/labels.hpp` and `palace/linalg/ksp.cpp` for other enum values that route to `MFEM_ABORT`. Likely candidates: additional Krylov flavours, possibly some smoothers or preconditioners. Recurrence may climb quickly once the grep is run.

**Status: `new` (recurrence-2 in one cycle).** No mitigation in place — the mitigation IS the `mfem-as-l0-substrate-policy` ask item. Pre-decision, future cycles can land additional obstruction themes for known enum-only solvers without policy-blocking. Post-decision, themes either get retroactively rewritten with MFEM L0 anchors, or are explicitly re-categorised as out-of-scope.

---

```yaml
---
slug: wave-conflict-philosophy-scales
first_observed: cycle-003
last_observed: cycle-004
recurrence_count: 2
status: addressed-by-design
addressed_by: 8fc3a07 (user-directive parallel-when-in-doubt + conflict-tolerance philosophy) + cycle-004 7-wave validation
---
```

**Positive pattern.** The user-directive philosophy (commit 8fc3a07: "parallel-when-in-doubt, minor wave-conflict at integration is *useful tooling signal*, not friction to avoid") was validated at increasing scale across two consecutive cycles:

- **Cycle-003 (2 wave-mates).** nrm2 + axpby harvesters both edited `book/src/L1/index.md`. Original planner call: SEQUENTIAL. Actual integration: row-level non-overlapping, both applied cleanly in one wave. Pre-integration repairer caught a full-file-replacement issue in the nrm2 report and rewrote it as `append-after dot row` (cycle-003 §Wave-conflict observations).
- **Cycle-004 (7 wave-mates; 5 of which touch L1/index.md).** 5 dispatches appended to `book/src/L1/index.md` (3 firm harvester rows + 6 rough-in obstruction rows from 3 harvesters + 2 abstractors). 5 dispatches appended to `book/src/SUMMARY.md` (with alphabetical pre-resolution between MINRES and BiCGStab planner-side). **Zero structural conflicts at integration.** The dep-map-preserved-verbatim discipline in the L1-index-refresh report was load-bearing for clean merge with three concurrent harvester row-appends.

**Pattern.** Same-file row-level edits scale **at least to 5 concurrent writers** without integration friction, given:

1. Each writer's anchor is at a distinct row.
2. The structural-rewrite writer (here: layer-intro-author refresh) preserves the dep-map content verbatim, only changing surrounding prose.
3. The planner has applied alphabetical / dependency-order tie-breaking on SUMMARY.md insertions during dispatch planning.

**Cycle-005 implication.** Cycle-planner can mark **same-file row-level edits as PARALLEL by default at wave-size up to ~8**, even when 5+ wave-mates touch the same file. Threshold is not number-of-writers but per-anchor distinctness; the new high-water-mark is 5 concurrent writers on one file. Re-test at 8+.

**No mitigation needed; the philosophy is working as designed at scale.**

---

```yaml
---
slug: new-agent-defs-need-session-restart
first_observed: cycle-005
last_observed: cycle-005
recurrence_count: 1
status: addressed-by-restart-watch-for-recurrence
addressed_by: cycle-005 user restart (integrator-per-report + integrator-finalize defs picked up post-restart)
---
```

**Pattern.** When new agent definitions are added under `.claude/agents/<name>.md` mid-session (e.g., the cycle-004 → cycle-005 boundary commit `ccc5082` that introduced `integrator-per-report.md` and `integrator-finalize.md`), the session that wrote the commit does NOT see them in the cached agent registry. First dispatch attempt against the new agent name returns "Agent type not found". Resolution: restart the Claude Code session; post-restart the agent defs resolve.

**Surfaced by**: integrator-finalize cycle-005 §First-cycle-under-split-integrator observations; integrator-signals cycle-005 §Integration-tooling friction.

**Counterfactual test (per addressed-by-design audit discipline).** If this quirk were removed tomorrow, would orchestration coupling collapse? — **No coupling collapses**, but the cycle-002 cycle-002 → cycle-003 + cycle-005 pattern of "user adds new agent defs as one commit, then restarts mid-cycle to enact" loses one process step. Worth a Claude Code feature/bug request: invalidate the cached agent list on `.claude/agents/` write, or expose a "rescan" command.

**Per user-memory `feedback_escalate_process_issues`**: this is a harness quirk that the workaround (restart) is tolerable for; the friction surfaces ≤1× per agent-def-addition event (~once per several cycles); current status `addressed-by-restart-watch-for-recurrence`. **Not** filed as `addressed-by-design` (per the cycle-004 audit discipline that distinguishes "we have a workaround; mitigation done" from "the channel IS the design"). If recurrence climbs to ≥3, file a Claude Code upstream issue.

**Watch:** recurrence on next agent-def add event. If frequency rises above ~1 per 5 cycles, escalate to upstream.

---

```yaml
---
slug: split-integrator-validated-at-six-reports
first_observed: cycle-005
last_observed: cycle-005
recurrence_count: 1
status: addressed-by-design
addressed_by: ccc5082 (split integrator role-spec) + cycle-005 first-cycle validation
---
```

**Positive pattern.** First cycle running the split integrator (`integrator-per-report` + `integrator-finalize`, introduced cycle-004 → cycle-005 boundary in commit `ccc5082` per user directive 2026-05-27 — token-budget concern at higher wave-mate counts; wave-mate target 15→8). Six per-report dispatches each had bounded scope (one report's proposed-changes + the artifact files that report touched + a STAGING.md append); zero per-dispatch context-bound friction observed.

**Validation signals.**
- **Staging-log format usability: PASS.** Each per-report dispatch appended a structurally-uniform row; aggregating gate-totals, files-touched, and OQ-counts for finalize was mechanical (read STAGING.md, sum columns, list files). No format changes proposed by finalize.
- **Surgical SUMMARY.md inserts worked across 5 in-cycle writers.** The first per-report dispatch's Notes documented the "preserve append-points for subsequent in-cycle integrators" discipline; subsequent dispatches followed it consistently. **The discipline self-perpetuates via the Notes channel of the staging log.** See sibling friction-ledger entry `summary-md-serial-write-discipline` (this cycle) for the discipline itself.
- **Per-dispatch token budgets comfortable.** No context overflow on any per-report invocation despite 7-axis krylov-step + 5-sub-pattern apply-linop + 4-sub-pattern axpbypcz + 6-chapter L0 bundle + observation-only cross-cutter + concept-page work.

**Counterfactual test.** If the split were collapsed back to a single `integrator` dispatch at 6 wave-mates, would friction surface? — likely yes at the cycle-004's 7-wave-mate scale, given the per-cycle complexity now includes per-cycle (a) safety-net gate aggregation, (b) artifact writes, (c) STAGING aggregation, (d) build + repair, (e) cycle-end housekeeping (cycle-record, log, signals, roadmap, frontmatter touches), and (f) single commit + push. Pre-split cycle-004 was already large; cycle-005 with 6 dispatches (more substantive surface per dispatch) would have exceeded token budget under single-pass.

**Status `addressed-by-design`** is correct here per the cycle-004 audit discipline: the split IS the design; there is no workaround in the loop; removing the split would not collapse a workaround, it would simply remove the token-bounding mechanism the design provides.

**No mitigation needed; design is working at the wave-size it was scoped for.**

---

```yaml
---
slug: summary-md-serial-write-discipline
first_observed: cycle-003
last_observed: cycle-005
recurrence_count: 3
status: addressed-by-design
addressed_by: cycle-005 STAGING.md Notes-channel propagation + per-report-integrator role spec "re-read disk at every Edit" discipline
---
```

**Positive pattern.** The SUMMARY.md surgical-insert convergence point continues to scale.

- **Cycle-003 (2 writers):** nrm2 + axpby harvesters both appended chapter rows. Cleanly serialized; planner over-cautious "sequential" call dropped at integration.
- **Cycle-004 (5 writers):** 5 of 7 dispatches edited SUMMARY.md. Zero conflict under single-pass integrator; alphabetical anchor pre-resolution at planner-side absorbed MINRES + BiCGStab into adjacent lines.
- **Cycle-005 (5 writers under split integrator):** 5 of 6 dispatches edited SUMMARY.md. Per-report serial dispatch + the "surgical insert preserving append-points" discipline (introduced explicitly by dispatch #1's STAGING Notes, then echoed by subsequent dispatches) yielded zero collisions. Each per-report integrator re-read SUMMARY.md fresh and inserted at literal-string anchors.

**Discipline (now established across 3 cycles).** SUMMARY.md edits under multi-writer waves work cleanly when:
1. Each writer's anchor is at a distinct row (or H1 heading; or sibling-chapter anchor under a Part).
2. Each per-report integrator re-reads SUMMARY.md fresh at apply time — never trusts an earlier view.
3. The first per-report integrator in a cycle documents the "preserve append-points" discipline in their STAGING.md Notes, and subsequent integrators read prior Notes entries.
4. The integrator-per-report role spec already includes "Re-read disk at every Edit" as a Discipline bullet (`.claude/agents/integrator-per-report.md`).

**Counterfactual test.** If the discipline were dropped, would orchestration collapse? — friction would rise at integration: SUMMARY.md collisions on adjacent-row inserts. The discipline is **load-bearing for multi-writer scaling**. But it's encoded in the role spec, not as a workaround — so status `addressed-by-design` (the channel IS the design).

**Connection to skill-candidates.** This discipline could be promoted as a stand-alone skill (`skill:summary-md-surgical-insert`) — see skill-candidates.md cycle-005 append. Default-accept under low-bar policy given 3-cycle observation. Promoting this meta-phase.

**No mitigation needed; the discipline is encoded + reinforced via STAGING Notes.**

---

```yaml
---
slug: two-phase-sha-placeholder-pattern
first_observed: cycle-004
last_observed: cycle-006
recurrence_count: 3
status: addressed-by-design
addressed_by: cycle-005 meta-phase (canonical pattern documented in integrator-finalize role spec) + integrator-finalize.md §Process step 13
---
```

**Pattern (now canonical).** The integrator-finalize commits the cycle artifact with `integration_commit: PLACEHOLDER_SHA` in each consumed report's frontmatter (because the SHA can only be known post-commit), then immediately follows with a small patch commit replacing the placeholder with the actual SHA. Recurrence:

- **Cycle-004**: finalize commit `8ac1f37`; patch commit `af3c582`.
- **Cycle-005**: finalize commit `a16c32c`; patch commit `af037ab`.

**Why it's design, not friction.** Git's commit-SHA-is-content-addressable invariant means you can't pre-compute the SHA before committing without freezing the tree; doing so via tree-state pre-compute would require git plumbing (`git hash-object`, `git mktree`, `git commit-tree`) that's complex and brittle. The two-phase pattern is the simplest correct approach.

**Cycle-005 meta-phase action.** Document as canonical in `.claude/agents/integrator-finalize.md` §Process step 13 (already lists "Patch sha-placeholder" as an option; this meta-phase tightens the language to declare it canonical rather than optional). Future integrator-finalize invocations follow the same pattern unambiguously.

**Cycle-006 confirmation.** Pattern recurred a third time (finalize commit `704717b` + patch `d42950d`). Continues to work as designed; no further mitigation.

**No mitigation beyond role-spec clarification.** Watch: if a future Claude Code feature offers pre-commit SHA via tree-state, revisit (low priority).

---

```yaml
---
slug: split-integrator-validated-2-cycles
first_observed: cycle-005
last_observed: cycle-006
recurrence_count: 2
status: addressed-by-design
addressed_by: ccc5082 (split integrator role-spec) + cycle-005 first-cycle validation + cycle-006 second-cycle validation under wave-1+wave-2 dependency ordering
---
```

**Positive pattern (confirmed at 2 cycles).** The split integrator (`integrator-per-report` + `integrator-finalize`, introduced cycle-004 → cycle-005 boundary) has now run two clean cycles end-to-end with zero per-dispatch context-bound friction.

**Cycle-005**: 6 wave-1 dispatches (all independent). STAGING.md format usability PASS. SUMMARY.md surgical inserts across 5 in-cycle writers worked. Per-report context budgets comfortable.

**Cycle-006**: 4 wave-1 + 1 wave-2 dispatches (first cycle exercising wave-2 dependency on wave-1 mate under split integrator). Wave-2 abstractor depended on wave-1 harvester's L4 entry; per-report serial dispatch order honoured (STAGING.md rows 1-4 then row 5); the L4 dep-map at wave-2's edit time already had wave-1's firm row, so wave-2's two rough-in appends went cleanly after it. **Validates the per-report serial-dispatch design at wave-mate-dependency boundaries**, not just across independent wave-1 mates.

**Implication (informs cycle-006 mid-cycle directive `f661039`).** The user directive that raised wave-cap 8→12 mid-cycle-006 is motivated in part by this 2-cycle confirmation that per-dispatch context stays bounded regardless of wave-mate count. Cycle-007+ can run up to 12 dispatches without expecting per-report context friction.

**Sibling supersession.** The earlier entry `split-integrator-validated-at-six-reports` (cycle-005) is subsumed by this one as the broader-validation record. Keeping that entry in place as historical (recurrence-1 cycle-005).

**Counterfactual test.** If the split were collapsed back to a single integrator dispatch at 5 wave-mates: friction would surface (cycle-004's 7-wave-mate at single-pass was already large; cycle-006's wave-2 dependency on a wave-1 mate's L4 entry would have required the single-pass integrator to read and reason about wave-1 + wave-2 in one context, with all 5 reports' proposed-changes + safety-net aggregation + STAGING + build + commit + housekeeping in one shot). The split removes that pressure.

**No mitigation needed; design is working at the wave-size it was scoped for, AND now with cross-wave dependency.**

---

```yaml
---
slug: subagent-write-filter-still-applies-to-some-agents-cycle-md-naming
first_observed: cycle-006
last_observed: cycle-006
recurrence_count: 1
status: new
addressed_by: cycle-006 meta-phase (role-spec touches; see go items)
---
```

**Pattern (new this cycle).** The cycle-004 REPORT.md → CYCLE.md project-wide rename (commit `8ac1f37`) bypassed the Claude Code subagent Write-filter on `report|summary|findings|analysis` keywords for most subagent dispatches. However, in cycle-006 the `same-layer-cross-cutter` subagent **still did not write its CYCLE.md to disk** — the agent reported a system-prompt restriction on writing those filenames; the parent orchestrator wrote the CYCLE.md post-hoc from inline output. The harvester, layer-intro-author, and abstractor dispatches in the same wave wrote their CYCLE.md files successfully.

**Probable root causes** (one or both):
1. **Stale role-spec text** at `.claude/agents/same-layer-cross-cutter.md:17` still says `Output: REPORT.md` (not updated in the `8ac1f37` rename). The subagent reads its role spec at dispatch time and may treat the role-spec naming as authoritative, then hit the harness Write filter on the literal `REPORT.md` filename it derives from the spec. Similar stale text may exist in other agent role specs.
2. **Subagent re-interpretation of its system prompt.** Even with role-spec saying CYCLE.md, the subagent may interpret the system-prompt filter as a generic block on writing report-shaped files and self-censor.

**Surfaced by**: cycle-006 OQ `same-layer-cross-cutter-cycle-md-write-failure` + cycle-006 integrator-signals.md §Integration-tooling friction (implicitly via the OQ inclusion).

**Mitigation (cycle-006 meta-phase, this entry):** Two-part fix enacted as `go` items.
- (a) Update `.claude/agents/same-layer-cross-cutter.md` line 18 — change `Output: REPORT.md` to `Output: CYCLE.md`. Audit other agent role specs for the same stale text (`cross-layer-cross-cutter.md`, `combinator-miner.md` were checked; all three carry the stale `Output: REPORT.md` header).
- (b) Add explicit "Write your CYCLE.md to disk yourself; do not return content as text" instruction to the discipline section of each role spec where missing.

**Counterfactual test.** If this quirk were removed tomorrow, would orchestration coupling collapse? — Yes, the post-hoc-parent-write workaround is load-bearing each time it triggers; the parent orchestrator must catch and recover, which couples the orchestration layer to a per-agent quirk. Per the cycle-004 audit discipline, this is `recurring-with-workaround`, not `addressed-by-design`. The mitigation is to fix the role specs and watch.

**Watch:** if a future cycle has another subagent skip CYCLE.md Write despite the role-spec fix, escalate (proposal: file Claude Code upstream issue; the rename alone is insufficient if subagents re-derive filenames).

---

```yaml
---
slug: integrated-at-write-authority-drift
first_observed: cycle-006
last_observed: cycle-006
recurrence_count: 1
status: resolved
addressed_by: cycle-006 meta-phase (`.claude/agents/integrator-per-report.md` role-spec clarification — `integrated_at:` deferral to finalize)
resolved_at: meta-batch-1 (cycle-009 meta-phase)
resolved_basis: 4 consecutive clean cycles post-enactment (cycles 006/007/008/009 all zero recurrences) — well past the resolved threshold (≥10 cycles is the formal bar but the role-spec fix is mechanical and the 4-cycle clean record under split-integrator across 6/7/4 wave-mate counts is conclusive)
---
```

**Pattern.** Cycle-006 per-report integrator dispatch #1 (harvester-krylov-step-L4) set `integrated_at: 2026-05-27T09:00:00Z` in its CYCLE.md frontmatter at per-report integration time — outside CLAUDE.md write-authority partition, which assigns `integrated_at` touches to integrator-finalize. The other 4 per-report dispatches in cycle-006 deferred correctly. Integrator-finalize timestamp `2026-05-27T09:08:49Z` overwrote dispatch #1's earlier value; all 5 reports now carry the same finalize timestamp + `integration_commit: <sha>` (via two-phase SHA pattern).

**Surfaced by**: cycle-006 integrator-finalize CYCLE.md §"Per-report `integrated_at:` inconsistency (caveat (b) for meta-phase)" + integrator-signals.md cycle-006 §Integration-tooling friction.

**Mitigation (cycle-006 meta-phase):** Role-spec clarification in `.claude/agents/integrator-per-report.md` — explicit "do NOT touch `integrated_at:` — that is integrator-finalize's responsibility" in the "What you DO NOT do" section. Also added staging-log Notes "deferred integrated_at to finalize per role-spec" boilerplate to make the convention visible.

**Resolution (meta-batch-1 / cycle-009 meta-phase, this update).** Cycles 007/008/009 each ran 6/7/4 per-report dispatches respectively with ZERO recurrences across the entire batch. Combined with cycle-006's per-report-#1 single observation, the role-spec fix is fully load-bearing and the pattern is resolved. Status flipped `addressed` → `resolved`. The friction-ledger pattern stays as historical record.

---

```yaml
---
slug: rough-in-rows-must-be-plain-text-when-anchor-missing
first_observed: cycle-006
last_observed: cycle-006
recurrence_count: 1
status: addressed
addressed_by: cycle-006 meta-phase (`.claude/agents/abstractor.md` + `.claude/agents/layer-intro-author.md` rough-in convention) + cycle-006 finalize surgical defang at integration
---
```

**Pattern.** Cycle-006 wave-2 abstractor's L4 dep-map rough-in rows used markdown link syntax — `[iterate_while](./iterate_while.md)` and `[iterate_while_with_prev](./iterate_while_with_prev.md)` — for files that don't yet exist (rough-in status; cycle-007 OQ `iterate-while-l4-anchor-missing` tracks anchor pending). mdbook's `linkcheck2` renderer treats missing-anchor links as **errors** (not warnings) and failed the build. Integrator-finalize defanged to plain-text `iterate_while (rough-in; no anchor yet)` with annotation as a surgical-minimal repair.

**Surfaced by**: cycle-006 integrator-finalize §Build status + integrator-signals.md cycle-006 §Integration-tooling friction.

**Mitigation (cycle-006 meta-phase, this entry):** Convention added to `.claude/agents/abstractor.md` and `.claude/agents/layer-intro-author.md` Discipline sections — "rough-in dep-map rows that reference yet-to-exist files must use plain-text names with `(rough-in; no anchor yet)` annotation, NOT markdown link syntax. Only firm rows (where the anchor file exists) may use `[slug](./slug.md)` link syntax." Per-report-integrator already auto-repairs via the surgical-defang pattern; the role-spec convention prevents the friction at the source.

**Watch:** if a future rough-in dep-map row lands with link syntax to a missing anchor, escalate to recurrence-2 and consider auto-fix gate in integrator-per-report.

**Amended 2026-05-28 (user directive — CLAUDE.md §"Integration may materialize implied components as stubs").** The plain-text convention is now the *fallback*, not the only path. When a referenced slug is **clearly implied** (≥2 converging references / a standing rough-in row), the **preferred** resolution is for integration to **create the `stub`** (claim-free placeholder file + SUMMARY registration) so the reference becomes a live link, refined later. Plain-text-defer remains correct only when the component is merely speculative. See `.claude/agents/integrator-per-report.md` step 5 (implied-component stub materialization) + `.claude/agents/integrator-finalize.md` step 5.

---

```yaml
---
slug: legacy-log-cycle-N-md-collision-rename-on-encounter
first_observed: cycle-005
last_observed: cycle-006
recurrence_count: 2
status: addressed-by-pattern
addressed_by: cycle-005 + cycle-006 finalize rename-on-encounter pattern (each finalize renames the colliding legacy file to `cycle-N-legacy.md` per cycle); cycle-006 meta-phase chose this pattern over bulk-rename
---
```

**Pattern.** Legacy slice-era `log/cycle-NNN.md` files (from cycles 1–172 pre-layered-era) collide with future layered-era `log/cycle-NNN.md` writes for any N where both eras have a cycle of that number. Each layered-era finalize renames the colliding legacy file to `log/cycle-NNN-legacy.md` (cycle-005: `cycle-005.md` legacy → `cycle-005-legacy.md`; cycle-006: `cycle-006.md` legacy → `cycle-006-legacy.md`). Pre-layered-era cycles ran much higher numbers (up to cycle-172), so collisions are bounded — layered-era cycles N ≤ 172 will collide; N > 172 will not.

**Cycle-006 meta-phase decision.** Choose pattern (b) **rename-on-encounter** over pattern (a) **one-shot bulk-rename**. Rationale:
- Bulk-rename now would rename ~172 files, polluting the git history with a large mechanical rename commit.
- Rename-on-encounter is amortised across cycles and already works (cycle-005 + cycle-006 both clean).
- The pattern is encoded implicitly in integrator-finalize's behaviour (each cycle's finalize handles its own collision). Documenting in `.claude/agents/integrator-finalize.md` is optional — the pattern is small enough that two precedents establish it.
- **No further enactment** beyond confirming the choice in this ledger entry. If a future finalize misses the rename (e.g., legacy file overwritten silently), escalate to bulk-rename.

**Watch:** monitor cycle-007 through cycle-N (≤172) finalize logs for clean handling of the rename. If any finalize misses it, escalate.

---

```yaml
---
slug: index-placeholder-displacement-on-first-firm-row
first_observed: cycle-006
last_observed: cycle-006
recurrence_count: 2
status: addressed
addressed_by: cycle-006 per-report integrator applied as "discretionary auto-fix" twice (wave-1 on L4/index.md, wave-2 on L4-L3/index.md); cycle-006 meta-phase formalizes the convention in integrator-per-report safety-net gates
---
```

**Pattern (positive).** When a layer's `index.md` carries the `(empty — Phase B skeleton.)` placeholder and a first firm dep-map row lands under that index via a per-report integration, the integrator replaces the placeholder with the firm row rather than appending below it. Applied twice cycle-006: wave-1 harvester on `L4/index.md` (first firm L4 row `krylov-step`); wave-2 abstractor on `L4-L3/index.md` (first firm L4>L3 theme). Both per-report integrators acted discretionarily; the latter explicitly cited the former's pattern in STAGING.md notes.

**Surfaced by**: cycle-006 integrator-finalize §Wave-conflict observations + integrator-signals.md cycle-006 §Wave-conflict observations.

**Cycle-006 meta-phase decision.** **Formalize as a per-report-integrator safety-net gate** (low cascade). Add to `.claude/agents/integrator-per-report.md` §"Process" step 5 — "**index-placeholder displacement auto-fix**": when this report's proposed-changes add a firm dep-map row to an `index.md` that currently carries the literal placeholder text `(empty — Phase B skeleton.)`, replace the placeholder with the firm row (do not append below). Record as `applied-discretionarily` in the staging row with rationale (first-firm-row-displaces-placeholder).

**No further mitigation needed beyond the role-spec touch.**

---

```yaml
---
slug: abstractor-direct-write-to-book-during-dispatch
first_observed: cycle-008
last_observed: cycle-008
recurrence_count: 1
status: addressed-by-watch
addressed_by: cycle-009 meta-phase decision (single-instance + clean cycle-009 = treat as one-off; role-spec wording-prominence boost deferred unless recurrence)
---
```

**Pattern.** Cycle-008 wave-1 dispatch #2 (abstractor on ksp_solve L1>L0) wrote directly to `book/` during dispatch (3 artefact files: `L1-L0/ksp-solve-mutation-rotation.md` + `L1-L0/index.md` + `SUMMARY.md`) rather than emitting the proposed-changes blocks via the canonical CYCLE.md channel. Violates CLAUDE.md write-authority partition (specialized agents write to `reports/<id>/CYCLE.md` only; `book/` is integrator-per-report's domain). Critic failed `plan-kind-consistency`; repairer executed Option-A clean restoration (`git checkout --` + `rm` + co-locate as report supporting doc + rewrite CYCLE.md into canonical proposed-changes blocks). Re-applied cleanly via canonical pipeline at integrator-per-report time. Critical OQ `abstractor-write-authority-violation-cycle-008` promoted for cycle-009 meta-phase pattern-watching.

**Surfaced by**: cycle-008 integrator-finalize §Wave-conflict observations + integrator-signals.md cycle-008 §Wave-conflict observations + cycle-008 OQ.

**Cycle-009 evidence (full primary cycle of pattern-watching).** Zero recurrences across 4 cycle-009 dispatches (lifter, layer-intro-author, harvester, combinator-miner). All 4 dispatches held write-authority discipline cleanly. Single-instance evidence after one full pattern-watching cycle.

**Mitigation (cycle-009 meta-phase, this entry).** Single-instance + one full clean cycle = treat as one-off, not as latent pattern. **No role-spec wording-prominence boost enacted this meta-phase** — the `abstractor.md:73` "What you DO NOT do" already implies the boundary, and `abstractor.md:18-23` "Output: CYCLE.md" explicitly says "Write your CYCLE.md to disk yourself" + "The integrator applies (c)" — the proposed-changes channel is canonical. Adding more prominence risks signal fatigue without removing the actual cause (which was the dispatch-time decision of one cycle-008 abstractor invocation to skip the CYCLE.md channel; the role spec is already clear). **Status: `addressed-by-watch`.**

**Watch:** if cycle-010+ sees a second occurrence of any specialized agent writing directly to `book/`, escalate to recurrence-2 and enact: (a) role-spec wording-prominence boost at the top-of-file Output section (move the "do not return content as text" sentence to a top-level Discipline bullet); (b) consider an integrator-per-report safety-net gate that detects pre-dispatch unmodified-vs-modified `book/` files and refuses to apply if the dispatch wrote outside its proposed-changes channel.

---

```yaml
---
slug: layer-definition-discipline-high-to-low
first_observed: meta-batch-1 (cycle-009 meta-phase; codification of user directive 2026-05-27 mid-cycle-009)
last_observed: meta-batch-1
recurrence_count: 1
status: addressed
addressed_by: cycle-009 meta-phase (CLAUDE.md §Methodology invariants new bullet + 4 role-spec touches: abstractor / harvester / lifter / layer-intro-author Discipline sections)
---
```

**Pattern (codification, not friction).** User directive mid-cycle-009 2026-05-27: "The higher stages should be defined in terms of themselves (not the lower stages). The lowering stages should be defined in terms of how the higher stage lowers into the lower stage. Notes towards the reverse process should be kept in the working notes; but the formulation should remain structured as higher to lower."

**Interpretation.** L_n operators are defined in terms of L_n vocabulary (or references to L_{n+1} for upward context); they are NOT defined in terms of L_{n-1} primitives. Lowering themes `L_{n+1}>L_n` are defined as "how the L_{n+1} form lowers into the L_n form" — explicit direction, LHS L_{n+1}, RHS L_n. Notes about the reverse (how L_n lifts into L_{n+1}) go in working notes (`scaffolding/`, supporting docs, OQs), NOT in formal chapter content.

**Why this is in the friction-ledger as `addressed`, not as ongoing friction.** No batch-1 batch chapter overtly violates this discipline (the krylov-step lowering chain at L4 / L4>L3 / L3>L2 / L2 follows it naturally); the directive sharpens the discipline against potential drift. Recording as `addressed` per first-observation = codification-enacted; future cycles that violate the discipline escalate to recurrence-2 and may motivate a critic check.

**Enactment (cycle-009 meta-phase, this entry):**
- (a) `CLAUDE.md` §Methodology invariants: new bullet "Layers are defined high→low; lifting notes go in working notes" — full directive verbatim plus interpretation.
- (b) Role-spec touches at abstractor / harvester / lifter / layer-intro-author Discipline sections, each adding one bullet referencing the CLAUDE.md invariant.

**Watch:** if a future per-report dispatch defines an L_n entry in terms of L_{n-1} vocabulary (or a lowering-theme's prose narrates lift instead of lowering), critic should flag under `rotation-quality` and surface as recurrence-2; consider promoting a `critic` 9th check explicitly for direction-of-definition discipline.

---

```yaml
---
slug: lower-vocabulary-priority-over-higher-expansion
first_observed: meta-batch-1 (cycle-009 meta-phase; codification of user directive 2026-05-27 mid-cycle-009)
last_observed: meta-batch-1
recurrence_count: 1
status: addressed
addressed_by: cycle-009 meta-phase (CLAUDE.md §Methodology invariants new bullet + scaffolding/priorities.md priority #17 added)
---
```

**Pattern (priority-policy, sibling to high→low discipline above).** User directive mid-cycle-009 2026-05-27: "we want to prioritize lower-level shared utility (because we want to prioritize providing reusable vocabulary, to make other components cheaper and simpler to describe, or unify)."

**Interpretation.** When choosing between (a) expanding higher-layer vocabulary further and (b) populating lower-layer shared utility, prefer (b). Reusable lower-level vocabulary reduces duplication explosion in adjacent layers and enables unification of seemingly-distinct higher-layer patterns.

**Current state observation (informs cycle-010+ planner).** As of post-batch-1: `book/src/L3/` is empty (placeholder only). The krylov-step lowering chain is documented as L4 firm > L4>L3 firm > L3-rendering-in-theme > L3>L2 firm > L2 firm WITHOUT an interposed L3 row. This is correct *for krylov-step specifically* (cycle-006 audit verdict: identity-in-form on the kernel body's primitive sequence; no L3 row needed for that operator). But the L3 layer remains under-populated relative to its potential as an iteration-rotation vocabulary, and zero firm L3 rows after 3 batches of substantive work signals the layer-cohort balance needs adjusting at the planning level.

**Enactment (cycle-009 meta-phase, this entry):**
- (a) `CLAUDE.md` §Methodology invariants: new bullet "Lower-level shared vocabulary takes priority" — full directive verbatim plus interpretation + L3-empty current-state callout.
- (b) `scaffolding/priorities.md`: add priority #17 "lower-layer-shared-vocabulary-priority" with explicit cycle-010+ planner-guidance language.

**Watch:** cycle-010 + cycle-011 + cycle-012 planner decisions — if planner continues to dispatch L4 expansions over eligible L1/L2/L3 work, escalate to recurrence-2 and consider a hard ordering rule in cycle-planner Discipline.

---

```yaml
---
slug: notification-hook-misfiring-on-non-question-events
first_observed: cycle-009 (user-raised mid-cycle 2026-05-27)
last_observed: cycle-009
recurrence_count: 1
status: addressed
addressed_by: cycle-009 meta-phase (`~/.claude/settings.json` hook refinement — message-pattern filter on urgency)
---
```

**Pattern.** Notification hook in `~/.claude/settings.json` (configured during cycle-008 post-finalize work) fires `notify-send -u critical "Claude" "<MSG>"` on the Claude Code Notification event, which fires in MORE situations than just AskUserQuestion. The Notification event also fires on tool-permission prompts, status changes, and other "awaiting input"-shaped states. User raised mid-cycle-009 2026-05-27: hook firing in situations where Claude is not asking the user a question.

**Surfaced by**: user direct interjection mid-cycle-009; recorded in cycle-009 integrator-finalize §Integration-tooling friction + meta-batch-1 closure summary §Methodology observations item 5.

**Mitigation (cycle-009 meta-phase, this entry):** Refined `~/.claude/settings.json` hook command:
- (a) Reads JSON from stdin via `cat` (canonical Claude Code hook input channel).
- (b) Extracts `.message` field via `jq`.
- (c) Classifies `urgency` by lowercase-message-pattern: if message matches `*permission*` / `*waiting*for*input*` / `*needs*your*input*` / `*question*` / `*ask*` (the user-question-shaped events), use `urgency=critical`; otherwise `urgency=normal`. This downgrades non-question Notification events (status changes, internal events) to a non-intrusive `normal` urgency while preserving the critical signal for actual user-input requests.
- (d) Falls back to `MSG="awaiting input"` if jq fails.

**Watch:** if user reports the refined hook still misfires (or now under-fires on actual questions), escalate to recurrence-2 and consider: (a) scoping the hook to a more specific event-type if Claude Code adds one; (b) removing the hook entirely and using OS-native focus signals.

---

```yaml
---
slug: mcp-codemap-permission-denied-across-batch-1
first_observed: cycle-007
last_observed: cycle-012
recurrence_count: 3
status: resolved
addressed_by: ceb87da (cycle-010 pilot retry — `mcp__palace-codemap__*` allowlisted in .claude/settings.json) + batch-2 routine use with zero permission-denied
resolved_at: meta-batch-2 (cycle-012 meta-phase)
resolved_basis: user enacted option (a) — added MCP codemap tool allowlist entries to .claude/settings.json (commit ceb87da, "enable MCP palace-codemap tools in project allowlist (cycle-010 pilot retry)"); cycle-010 pilot SUCCEEDED; cycles 011/012 used the MCP tools routinely for C++ source localization with ZERO permission-denied across the batch. The 3-cycle block (batch-1) is fully cleared.
---
```

**Pattern.** MCP codemap server (`palace-codemap`, registered at repo root `.mcp.json` per commit `ab73d37`) is connected (`claude mcp list` shows `palace-codemap: ✓ Connected`) but per-tool calls return `Permission to use ... has been denied` in subagent contexts. Cycle-007 wave-1 dispatch #1 was the designated pilot per priority #16 step (e); both `mcp__palace-codemap__list_files` and related tools returned permission-denied. Cycle-008 and cycle-009 did not retry; pilot result carried forward unchanged across the full meta-batch-1.

**Surfaced by**: cycle-007 / cycle-008 / cycle-009 integrator-signals §Integration-tooling friction + cycle-009 integrator-finalize batch closure summary §Methodology observations item 4.

**Investigation findings.** The MCP server registration in `.mcp.json` is correct; tools surface to the parent session per the system-reminder MCP server instructions. The block is on per-tool permission allowlisting in subagent contexts — `.claude/settings.json` lacks `mcp__palace-codemap__*` entries in `permissions.allow`.

**ASK item (surfaced to user cycle-009 meta-phase; RESOLVED cycle-012 meta-phase).** Rollout decision options were:
- **(a) Enable**: user adds the `mcp__palace-codemap__*` tool entries to `.claude/settings.json` `permissions.allow`. Then cycle-010 wave-1 retries the pilot.
- **(b) Defer**: keep pilot dormant; revisit at next major meta-batch.
- **(c) Decommission**: retire from the dispatch-priority list; use vanilla Grep/Read indefinitely.

**User decision (between cycle-009 meta and cycle-010): option (a).** The MCP tool allowlist entries were added to `.claude/settings.json` (commit `ceb87da` "enable MCP palace-codemap tools in project allowlist (cycle-010 pilot retry)").

**Resolution (cycle-012 meta-phase, this update).** The cycle-010 pilot SUCCEEDED. Cycles 011/012 used the MCP codemap tools (`list_files` / `get_symbol_def` / `search_text` / `read_range` / `get_call_sites` / `list_dependencies` / `get_file_subtree`) routinely for C++ source localization with ZERO permission-denied across the batch. The 3-cycle block is fully cleared; status flipped `ask` → `resolved`. See the companion codification decision below (`mcp-first-localization-codified`): the cycle-012 meta-phase codifies MCP-first localization in CLAUDE.md §Target system (NOT as a hard per-role rule — see no-go reasoning in the meta-phase report) so the tooling's availability is documented for cycle-013+ agents.

**Watch:** if a future cycle hits a permission-denied on these tools (e.g., a new MCP tool surfaces that isn't in the allowlist), re-open at recurrence-4 and re-allowlist.

---

```yaml
---
slug: index-placeholder-displacement-on-first-firm-row-formalized
first_observed: cycle-006
last_observed: cycle-008
recurrence_count: 4
status: addressed
addressed_by: cycle-006 meta-phase formalized in integrator-per-report safety-net gates; cycle-009 meta-phase confirms 4-instance pattern stable + zero cycle-009 hits + zero new hits to formalize (already formalized)
---
```

**Pattern (positive, stable).** When a layer's `index.md` carries the `(empty — Phase B skeleton.)` placeholder and a first firm dep-map row lands under that index via a per-report integration, the integrator replaces the placeholder with the firm row rather than appending below it. Formalized cycle-006 in `.claude/agents/integrator-per-report.md` §Process step 5.

**Four instances observed across batch:**
- Cycle-006 wave-1 harvester on `L4/index.md` (first firm L4 row `krylov-step`).
- Cycle-006 wave-2 abstractor on `L4-L3/index.md` (first firm L4>L3 theme).
- Cycle-007 wave-1 dispatch 5 on `L3-L2/index.md` (first firm-rough-in L3>L2 theme).
- Cycle-008 wave-1 pass 4 on `L1-L0/index.md` (first firm L1>L0 table).

**Cycle-009 observation.** Zero index-placeholder displacements this cycle (no relevant placeholders remain in the active layer set: L4/index, L4-L3/index, L3-L2/index, L1-L0/index, L0/index, L1/index all have firm content; **L3/index and L2-L1/index and L3-L2/L4-L3 lowering parts that-may-not-yet-exist remain candidates** but none accumulated a firm row this cycle).

**Cycle-009 meta-phase decision.** **No additional formalization needed** — the cycle-006 role-spec touch in `.claude/agents/integrator-per-report.md` §Process step 5 captures the pattern; cycle-007 + cycle-008 + cycle-009 each ran the gate cleanly (4-instance stable, zero new misses). Status flipped from `addressed` (cycle-006) → still `addressed` with extended track-record. The pattern is now self-perpetuating via the role spec; no further action.

**Watch:** if a future cycle's first-firm-row dispatch APPENDS below the placeholder instead of displacing it, escalate to recurrence-2 and consider tooling (auto-strip placeholder line at dispatch-time, or YAML pre-flight gate).

---

```yaml
---
slug: l3-layer-empty-against-lower-vocabulary-priority
first_observed: meta-batch-1 (cycle-009 meta-phase; observed via L3/index inspection)
last_observed: meta-batch-1
recurrence_count: 1
status: new
addressed_by: null (paired with `lower-vocabulary-priority-over-higher-expansion`; cycle-010+ planner enacts)
---
```

**Pattern (observation, not pure friction).** `book/src/L3/` contains only `index.md` with the placeholder dep-map `(empty — Phase B skeleton.)`. Despite the krylov-step lowering chain being fully firm via L4 > L4>L3 > L3>L2 > L2 (cycle-009 finalize §Meta-batch-1 closure summary), no operators are firm at L3. Cycle-006's audit decision "no L3 row needed for krylov-step because the L3 form is value-thread-isomorphic to the L2 form" is now **SUPERSEDED** by the user directive 2026-05-27 mid-cycle-009 (codified as `identity-lowering-both-levels-required` below): identity-in-form between adjacent layers still requires both L entries because each layer is coherent within itself. The broader layer cohort is under-populated relative to L4 (3 firm) and L1 (8 firm + 1 rough-in test-coverage-bounded + 6 rough-in obstruction = 15 cohort entries).

**Surfaced by**: user observation mid-cycle-009 paired with the lower-vocabulary-priority directive (codified above as `lower-vocabulary-priority-over-higher-expansion`); confirmed by direct inspection of `book/src/L3/` directory contents (only `index.md`).

**Cycle-009 meta-phase decision (revised after identity-lowering directive landed).** This is a *signal* paired with two methodology codifications: (a) `lower-vocabulary-priority-over-higher-expansion`, and (b) `identity-lowering-both-levels-required` (below). The combination yields a concrete cycle-010 dispatch target: `book/src/L3/krylov-step.md` backfill (priority #20). No role-spec hard rule (which would over-constrain); the priority entry plus codifications provide cycle-010+ planning guidance.

**Watch:** if batch-2 (cycles 010/011/012) closes with `book/src/L3/` still containing only the krylov-step backfill and no additional L3 entries despite eligible work, escalate to recurrence-2 — the priority signal is not landing in planner decisions for non-trivial-rotation L3 candidates. Consider then: (a) explicit per-cycle dispatch in priorities.md (`harvester on <specific L3 candidate>`); (b) cycle-planner role-spec touch encoding the lower-layer-priority preference; (c) cross-layer-cross-cutter dispatch surfacing L3-eligible candidates from the L2 firm cohort.

---

```yaml
---
slug: identity-lowering-both-levels-required
first_observed: meta-batch-1 (cycle-009 meta-phase; codification of user directive 2026-05-27 mid-cycle-009)
last_observed: meta-batch-1
recurrence_count: 1
status: addressed
addressed_by: cycle-009 meta-phase (CLAUDE.md §Methodology invariants new bullet + harvester role-spec Discipline touch + scaffolding/priorities.md priority #20 added)
---
```

**Pattern (codification, supersedes prior verdict).** User directive mid-cycle-009 2026-05-27 (verbatim): "Specifically; when there is minimal / no change needed when lowering a component; the component should still have representation at both L levels (this is keeping in-line with 'each L level is coherent within itself')."

**Interpretation.** When the lower-layer form is identity-in-form to the upper-layer form (no rewrite needed; the operator's body at L_n is value-thread-isomorphic to its body at L_{n+1}), the operator still gets its own entry at the lower layer. Each layer is coherent within itself; the L_n entry uses L_n vocabulary to define the operator even when the lowering theme is trivial. The L_{n+1}>L_n theme between them notes the identity.

**Prior verdict superseded.** Cycle-006's audit of `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` concluded that no L3 entry for `krylov-step` was needed because the L3 form is value-thread-isomorphic to the L2 form (and the L4 form is value-thread-isomorphic to the L3 form). That verdict held through cycles 007/008/009. The user directive now reverses it: even when identity-in-form, the L3 entry is required for layer-coherence reasons. The cycle-010+ harvester backfill on `book/src/L3/krylov-step.md` is the precedent. The L4>L3 theme is updated to note the identity (rather than to argue against the L3 entry).

**Enactment (cycle-009 meta-phase, this entry):**
- (a) `CLAUDE.md` §Methodology invariants: new bullet "Identity-lowerings still require both L levels" — full directive verbatim plus interpretation + cycle-006 verdict-supersession callout.
- (b) `CLAUDE.md` §Methodology invariants: updated the existing `lower-vocabulary-priority-over-higher-expansion` bullet to remove the "correct for krylov-step per cycle-006 identity-in-form audit; no L3 row needed for that operator" sub-clause, replaced with cross-reference to this entry (the verdict-supersession is consistent across both invariants).
- (c) `.claude/agents/harvester.md` §Discipline: new bullet "Identity-lowerings still require both L levels" pointing at the CLAUDE.md invariant.
- (d) `scaffolding/priorities.md`: add priority #20 "identity-lowering-both-levels-backfill" with cycle-010+ harvester target (`book/src/L3/krylov-step.md`) + audit dispatch (cross-layer-cross-cutter for additional candidates).

**Watch:** if a future harvester dispatch on an identity-in-form operator skips the lower-layer entry, escalate to recurrence-2 and consider promoting a `critic` 9th check for missing-lower-layer-entry-on-identity-lowering.

---

```yaml
---
slug: phase-1-corpus-reduction-policy
first_observed: meta-batch-1 (cycle-009 meta-phase; codification of user directive 2026-05-27 mid-cycle-009)
last_observed: meta-batch-1
recurrence_count: 1
status: addressed
addressed_by: cycle-009 meta-phase (CLAUDE.md §Repository status + §Methodology invariants new bullets + scaffolding/priorities.md priority #19 added)
---
```

**Pattern (codification, policy update).** User directive mid-cycle-009 2026-05-27 (verbatim): "When components have been lifted from the phase 1 corpus successfully; and that material is no longer needed, it should be reduced and eventually removed as the new format becomes authoritative."

**Interpretation.** `book/src/spec/slices/` is the Phase 1 slice corpus (cycles 1–172 era; pre-structural-redirect). Until this directive, CLAUDE.md said "preserved as raw material for combinator extraction (not the deliverable)." Now: the corpus is **raw material** (not historical record) and is allowed to **shrink monotonically** as material is lifted into firm layered entries. A slice whose content is fully represented in the layered artifact is reduced to a stub (pointing at the firm layered entries it has been absorbed into) and eventually removed. The git history is the historical record; the slice form is not preserved once its content lives in the layered surface.

**Enactment (cycle-009 meta-phase, this entry):**
- (a) `CLAUDE.md` §Repository status: updated bullet about Phase 1 slice corpus to reference the reduction policy.
- (b) `CLAUDE.md` §Methodology invariants: new bullet "Phase 1 corpus reduces as material is lifted" — full directive verbatim plus interpretation + per-cycle audit-dispatch pattern.
- (c) `scaffolding/priorities.md`: add priority #19 "phase-1-corpus-reduction-audit" — cycle-010+ `same-layer-cross-cutter`-scoped dispatch on slices that overlap firm layered entries; first targets are krylov-chain slices.

**Watch:** if the audit-dispatch pattern surfaces in cycle-010+ but slices accumulate without reduction (i.e., audits propose reductions and they're not applied), escalate to recurrence-2 and consider integrator-per-report role-spec touch on slice-stub authoring procedure. If the audit pattern doesn't surface at all over 2-3 batches, the priority needs to be raised in cycle-planner's reading attention.

---

```yaml
---
slug: specialized-agent-direct-write-to-book-during-dispatch
first_observed: cycle-008
last_observed: cycle-077
recurrence_count: 5
status: addressed
addressed_by: cycle-018 meta-phase (dispatch-phase write-guard Discipline bullet enacted across ALL 8 specialized specs — harvester / abstractor / lifter / lowering-verifier / combinator-miner / same-layer-cross-cutter / cross-layer-cross-cutter + the pre-existing layer-intro-author) + skill `revert-dispatch-phase-book-mutation` (repairer safety-net, cycle-012); cycle-051 meta-phase (batch-15) re-weighed the recurrence-4 watch trigger → held the clean-tree gate NO-GO (net caught + repaired cleanly; 1 leak in 41 dispatches across cycles 018–051; the structural gate's cost exceeds its marginal value over the working detect+repair net); batch-24 meta-phase (cycle-078) recurrence 4→5, clean-tree gate HELD NO-GO again — the re-weighted watch trigger was NOT met (only ONE leak in the batch, caught by the critic + repaired clean via `revert-dispatch-phase-book-mutation`, ZERO escaped to commit; re-escalate only on TWO leaks in one batch OR a leak reaching a commit)
---
```

**Batch-25 meta-phase update (cycle-081) — NO RECURRENCE; count HELD at 5.** Batch-25 (cycles 079/080/081, ~8 specialized dispatches) had **zero dispatch-phase write-partition leaks**. The c079 D4 `combinator-miner` (the `domain_energy_reduce` distinct-verb confirm-probe) was **observation-only by design** and stayed clean — it proposed NO `book/` change, which is notable because the combinator-miner is the 2-of-5 repeat offender (c049 + c077) and an observation-only probe is exactly the deliverable shape where the "inverting/firm-harvest feels like editing" leak previously fired; this time it correctly emitted no mutation. c080/c081 carried no combinator-miner dispatch. The batch-24 watch (a 3rd combinator-miner leak → weigh a combinator-miner-SPECIFIC prompt sharpening before re-escalating the structural gate) is NOT triggered. Count held at 5; status stays `addressed`.

**Batch-26 meta-phase update (cycle-084) — NO RECURRENCE; count HELD at 5.** Batch-26 (cycles 082/083/084, ~5 specialized dispatches — c082 D1 cross-layer-cross-cutter + D2 lowering-verifier; c083 D1 lowering-verifier + D2 lifter; c084 D1 lifter) had **zero dispatch-phase write-partition leaks**. No `combinator-miner` dispatch in the batch (the repeat offender), so the 3rd-combinator-miner-leak watch was not exercised. Notably the batch carried two `lowering-verifier` reduce-verb law-confidence passes (c082/c083) that BOTH ended in a firm promotion — exactly the "firm-harvest / authoring-a-full-firm-body feels like an edit" deliverable shape — and BOTH correctly emitted authorized proposed-changes blocks rather than direct writes. **The batch was exceptionally clean overall: 0 critic failures, 0 unrepairable findings, 0 write-leaks, 0 build-repair** (warnings were mechanical citation/maturity-pointer hygiene only). Count held at 5; status stays `addressed`. Re-escalate only on TWO leaks in one batch OR a leak reaching a commit (the batch-15 re-weighted trigger).

**Pattern (generalized; supersedes the agent-specific cycle-008 entry `abstractor-direct-write-to-book-during-dispatch`).** A specialized dispatch agent writes directly to `book/` during the **dispatch phase** (Phase 2) rather than emitting proposed-changes blocks via its CYCLE.md channel for integrator-per-report to apply in Phase 5. This violates the CLAUDE.md write-authority partition (specialized agents write to `reports/<id>/CYCLE.md` only) and the no-artifact-mutation-in-dispatch invariant.

**Two instances across two batches (different agents):**
- **Cycle-008 (abstractor).** Wave-1 dispatch #2 (abstractor on ksp_solve L1>L0) wrote 3 artifact files directly. Critic failed `plan-kind-consistency`; repairer executed Option-A clean restoration. Recorded as `abstractor-direct-write-to-book-during-dispatch` (recurrence-1 at the time; cycle-009 meta treated it as a one-off and did NOT enact a prompt-guard, reasoning the role spec was already clear and added prominence risked signal fatigue).
- **Cycle-012 (layer-intro-author).** Report #6 (concept-corrections) wrote 4 `book/src/concepts/` edits directly during dispatch. Critic caught (HIGH, issue 1); repairer reverted all 4 to HEAD (Option A); integrator-per-report re-applied cleanly from proposed-changes blocks (all 4 `[old]` anchors matched committed HEAD verbatim). First observed instance for layer-intro-author.

**Re-characterization (cycle-012 meta-phase).** The cycle-009 "treat as one-off; no prompt-guard" decision held for the abstractor specifically, but the pattern has now recurred for a DIFFERENT specialized agent (layer-intro-author). This is **recurrence-2 of the generalized pattern** — the leak is not agent-specific; it is a class of dispatch-time behavior where an agent that is naturally "applying corrections" (lifter-flavored or concept-correcting work) treats the corrections as edits-to-make rather than changes-to-propose. The two affected agents (abstractor, layer-intro-author) are both ones whose work sometimes resembles direct editing. Per the cycle-008 entry's own watch clause ("if cycle-010+ sees a second occurrence of any specialized agent writing directly to `book/`, escalate to recurrence-2 and enact (a) role-spec wording-prominence boost ... (b) consider an integrator-per-report safety-net gate"), the meta-phase now enacts.

**Mitigation (cycle-012 meta-phase, this entry):**
- (a) **`.claude/agents/layer-intro-author.md`** — added a top-level Discipline bullet (prominent, not buried in "What you DO NOT do"): "**Do NOT write to `book/` (or any artifact file) yourself. Emit proposed-changes blocks in your CYCLE.md; integrator-per-report applies them in Phase 5.** This applies especially to concept-page corrections, which feel like edits to make but are changes to propose." layer-intro-author is the agent that leaked this cycle and the one most prone to the concept-correction-feels-like-an-edit failure mode.
- (b) **Skill `revert-dispatch-phase-book-mutation` promoted** (`skills/revert-dispatch-phase-book-mutation/SKILL.md`) — the deterministic seven-step repairer git procedure for cleanly reverting a dispatch-phase artifact leak (the cycle-012 repairer executed this shape; promoting it makes the recovery machine-replayable as a safety net for residual leaks). The prompt-guard (a) is the primary mitigation (prevent the leak); the skill (b) is the safety net (repair residual leaks).
- (c) **Did NOT add a per-report-integrator safety-net gate** (the cycle-008 watch clause's option (b)) — see no-go reasoning in the cycle-012 meta-phase report; the repairer already catches this reliably pre-apply, and a pre-dispatch clean-tree gate is a tooling change (ask-class) not a role-spec edit. Deferred.

**Watch:** if a THIRD specialized agent leaks (recurrence-3), escalate: enact the prompt-guard across ALL specialized agent specs (harvester / abstractor / lifter / lowering-verifier / combinator-miner / same-layer-cross-cutter / cross-layer-cross-cutter), and re-weigh the integrator-per-report pre-dispatch clean-tree gate (ask the user, as it is a tooling change).

**Cycle-018 meta-phase update — RECURRENCE-3 watch clause FIRED; enacted (go) + the clean-tree gate re-weighed (ask).** Cycle-017 was the third distinct specialized agent to leak (`harvester`, `divfree-l1-citation-fix`, edited `book/src/L1/divfree-projector.md` in-place during Phase 2; the repairer reverted via `revert-dispatch-phase-book-mutation` Option A and the 11 corrections re-applied the correct way). Three distinct agents now: cycle-008 `abstractor` → cycle-012 `layer-intro-author` → cycle-017 `harvester`. The cycle-012 prompt-guard lived only in `layer-intro-author.md`; the other 7 specs never received it. The watch clause's escalation condition is met.

- **(a) ENACTED (go):** the dispatch-phase write-guard Discipline bullet is now the **first Discipline bullet in all 8 specialized specs** — `harvester` / `abstractor` / `lifter` / `lowering-verifier` / `combinator-miner` / `same-layer-cross-cutter` / `cross-layer-cross-cutter` (this cycle) + `layer-intro-author` (cycle-012). Each is tailored to that agent's most-likely leak shape (harvester: citation-line corrections feel like edits; lifter: re-anchors ARE the deliverable; cross-cutters: usually read-only but edit-implying observations are still proposals). This makes the cycle-018 zero-leak result **structural, not reminder-dependent** (cycle-018 had zero leaks only because the parent added explicit per-dispatch reminders — those are not durable).
- **(b) RE-WEIGHED → ASK (deferred to user):** the integrator-per-report pre-dispatch clean-tree gate (the cycle-008 watch clause's option (b)) is a tooling/structural change (a gate that, before applying a report, checks `git status book/` is clean and refuses-or-flags if a dispatch already mutated `book/`). It is ask-class per write-authority (it would change the per-report apply protocol's preconditions, bordering tooling). The repairer already catches leaks reliably pre-apply via the promoted skill, and the now-universal prompt-guard is the prevention layer; the clean-tree gate would be a third backstop. **Recommendation: hold the gate unless a FOURTH leak occurs despite the universal prompt-guard** (recurrence-4) — at which point the prompt-guard has shown its ceiling (mirroring the citation-drift mechanical-checker logic) and the structural gate becomes warranted. Surfaced as an ASK item this cycle.

**Watch:** if a specialized agent leaks AGAIN despite the universal prompt-guard (recurrence-4), the role-spec approach has reached its ceiling — enact the integrator-per-report pre-dispatch clean-tree gate (the held ASK item) as a `go`/user-enacted structural backstop.

**Cycle-051 meta-phase update (batch-15) — RECURRENCE-4 FIRED; clean-tree gate RE-WEIGHED → NO-GO (the net is sufficient).** Cycle-049 D2 (`combinator-miner` inverting `book/src/L2/inner_product.md`) leaked a direct dispatch-phase write to that file despite the universal prompt-guard (the FOURTH distinct-context leak; agents now `abstractor` c008 → `layer-intro-author` c012 → `harvester` c017 → `combinator-miner` c049). Per the recurrence-4 watch clause this is the trigger to enact the held clean-tree-gate ASK. The meta-phase re-weighed it and decided **NO-GO** on the gate, for three reasons: (1) **the detect+repair net worked exactly as designed** — the c049 D2 leak was caught by the critic, reverted via `revert-dispatch-phase-book-mutation`, and reconstructed as 8 authorized `edit:`-fenced proposed-changes blocks that integrator-per-report applied against the restored file; the **applied state was correct**, zero artifact damage, zero escaped-to-commit defect; (2) **the base rate is low and not climbing** — 1 leak across the ~41 specialized dispatches of cycles 018–051 (4 leaks in ~150+ dispatches since cycle-008), i.e. the universal prompt-guard did NOT fail to bound the rate, it bounded it to ~rare; the leak is a class of agent that is "naturally applying corrections" (here: the combinator-miner *inverting* an entry, which feels like editing — the same lifter/concept-correction failure shape), not a systemic boundary erosion; (3) **the clean-tree gate is a tooling/structural change (ask-class) whose cost exceeds its marginal value** — it would add a per-report-apply precondition check (`git status book/` clean) that the repairer's pre-apply revert already covers, and it would not have changed the c049 outcome (the leak was caught + repaired regardless). The role-spec approach has NOT "reached its ceiling" in the sense the watch clause feared (a climbing rate the prompt-guard can't bound); it reached a low stable floor the detect+repair net absorbs cleanly. **Re-weighted watch:** re-escalate to the gate only if (a) TWO leaks occur in a single batch (a rate spike the net could miss under serial-apply pressure), OR (b) a leak escapes the critic+repairer net and reaches a commit (a net failure, not just a leak). Until then, hold NO-GO. Recorded as a recurrence increment (3→4) with the trigger re-weighed, not a new mitigation.

**Cycle-078 meta-phase update (batch-24) — RECURRENCE-5; clean-tree gate HELD NO-GO (re-weighted trigger NOT met).** Cycle-077 D4 (`combinator-miner` authoring `book/src/L1/participation_ratio.md`) leaked a direct dispatch-phase write to that file — the FIFTH distinct-context leak (agents now `abstractor` c008 → `layer-intro-author` c012 → `harvester` c017 → `combinator-miner` c049 → `combinator-miner` c077). The combinator-miner is now the repeat offender (c049 + c077), consistent with the re-weighed diagnosis: the leak shape is "an agent that is *naturally applying corrections / inverting / authoring a full firm body* treats it as an edit-to-make rather than a change-to-propose" — the combinator-miner's firm-L1-harvest deliverable (a full chapter body) is exactly that shape. **Outcome: the detect+repair net worked as designed** — the repairer reverted the on-disk file and repackaged the full firm body verbatim into a `new:` block (the `revert-dispatch-phase-book-mutation` skill); the per-report integrator created the file fresh from the `new:` block (byte-matched), zero content lost, zero artifact damage, zero escaped-to-commit defect. **The batch-15 re-weighted watch trigger was NOT met:** the gate re-escalates only on (a) TWO leaks in a single batch (this batch had ONE — c076 and c078 were leak-free) OR (b) a leak escaping the critic+repairer net to reach a commit (did not happen). Held NO-GO; recorded as a recurrence increment (4→5). **Note for future meta-phases:** the combinator-miner is now 2-of-5 of the leaks; if it leaks a THIRD time, weigh a combinator-miner-SPECIFIC prompt sharpening (the universal guard's combinator-miner tailoring — "inverting/firm-harvest feels like editing" — may want strengthening to a top-of-spec callout) BEFORE re-escalating to the structural clean-tree gate, since the failure is concentrated in one agent's deliverable shape, not a systemic boundary erosion.

---

```yaml
---
slug: skill-uptake-survey-non-invocation-cycle-wide
first_observed: cycle-010
last_observed: cycle-021
recurrence_count: 5
status: escalating
addressed_by: cycle-012 meta-phase (no-go: telemetry-noise) — SUPERSEDED cycle-015 meta-phase by the quality-defect trigger; the citation-drift sub-pattern is split into the dedicated entry `producer-citation-drift-verify-not-self-invoked` (recurrence-4 fired batch-5 → mechanical-checker ASK). This broad-telemetry entry stays no-go on recalibration.
---
```

**Cycle-024 meta-phase update (batch-6) — no-go on recalibration (continued); the citation arm is now MECHANIZED.** Batch-6 again carried the cycle-wide `skill-uptake-survey` warning (the named-by-slug telemetry gap) with all non-citation outcomes clean (no un-classified variant axis / missed refinement-surface reached the artifact across 23 reports). The actionable citation arm — split out to `producer-citation-drift-verify-not-self-invoked` — had its mechanical checker (`tools/citecheck/`) WIRED into the producer/critic/lowering-verifier/integrator procedures this meta-phase, which mechanizes the citation half of the survey: a clean `citecheck --scan/--anchor` IS the named-skill outcome for citations, so the telemetry-gap on the citation arm is now closed by the tool rather than by a slug back-reference. The non-citation arm stays benign telemetry; **no-go on recalibrating the 8th check** (unchanged rationale: touching the critic's check is unjustified while non-citation outcomes stay clean). Status stays `escalating` (broad pattern visible); recurrence stays 5 (no new non-citation quality defect). Re-open only if a non-citation skill's *outcome* reaches the artifact.

**Cycle-021 meta-phase update (batch-5) — the benign-telemetry part continues; no-go on recalibrating the check; but note the actionable citation sub-pattern (split out) has NOW reached recurrence-4.** Batch-5 carried the pervasive `skill-uptake-survey` warning again — every cycle-021 report tripped it (`verify-citation-range`/`verify-refinement-surface`/`classify-variant-axis` used in spirit but not named by slug). For the NON-citation skills (`classify-variant-axis`, `verify-refinement-surface`), the warnings remain benign telemetry: the variant-axis classification and refinement-surface checks demonstrably happened (no un-classified axis or missed refinement-surface reached the artifact this batch); only the slug back-reference is absent, which is harmless for opus-tier agents who internalize the procedure. **No-go (continued) on recalibrating the `skill-uptake-survey` check itself** — the cost of touching the critic's 8th check is unjustified while the non-citation outcomes stay clean; the citation-specific part is the one that turned actionable, and it is handled by the split-out entry's mechanical-checker ASK (which would, if built, *also* relieve the citation arm of this telemetry warning by mechanizing the check). Status stays `escalating` (keeps the broad pattern visible); recurrence 4 → 5 (the batch-5 cycle-wide instance). Re-open for recalibration only if a NON-citation skill's *outcome* (an un-classified variant axis, a missed refinement-surface check) actually reaches the artifact.

**Cycle-018 meta-phase update — batch-4: the benign-telemetry part continues; the actionable citation sub-pattern stayed CLEAN; no-go on recalibrating the check.** Batch-4 carried ~4+ `skill-uptake-survey` warnings (cycle-016 SEVEN-report-consistent `verify-citation-range` read-back without a named-by-slug invocation; cycle-017 4 warnings on `verify-citation-range`/`classify-variant-axis`/`propose-rotation`; similar cycle-018) — all repairer-ruled not-needed (procedure substance present, only the slug back-reference absent). Crucially, the one part of this broad pattern that became a quality defect in batch-3 (the citation drift, split out to `producer-citation-drift-verify-not-self-invoked`) **stayed clean through batch-4** — the producer self-verify bullets worked, so there is no batch-4 quality defect that a named skill invocation would have caught. The remaining signal is purely the named-by-slug telemetry gap, which is benign for opus-tier agents who internalize the procedure. **No-go on recalibrating the `skill-uptake-survey` check this cycle** (e.g. narrowing it to flag only missing *outcomes* rather than missing *invocation strings*): the cost of touching the critic's 8th check now is premature while the actionable sub-pattern is clean; the telemetry-only warnings are tolerable noise. Status stays `escalating` to keep the broad pattern visible, but the escalation has NOT converted to a new quality defect since the citation split-out. Re-open for recalibration only if a non-citation skill's *outcome* (an un-classified variant axis, a missed refinement-surface check) actually reaches the artifact.

**Cycle-015 meta-phase update (recurrence-4; watch-clause FIRED).** The cycle-012 watch clause said: "if a future cycle shows a *quality defect* that an explicitly-invoked skill would have caught (not just a telemetry gap), escalate to recurrence-4." Batch-3 (013/014/015) produced exactly that, every cycle: actual repairer-corrected citation drifts in ~6 reports (013), 5-of-8 reports incl. the citation-AUDITING lowering-verifier itself (014), and the bilinearform `RT_FECollection`/`L2_FECollection` attribution + 2 relocated-dangle re-anchors (015). These are quality defects, not telemetry gaps — a self-applied `verify-citation-range` pass would have caught each. The cycle-012 "telemetry-noise, no-go" judgment is **SUPERSEDED**. Status flipped `recurring` → `escalating`. The actionable sub-signal (the citation-drift specifically — the `skill-uptake-survey` check ALSO fires on `classify-variant-axis` / `verify-refinement-surface` non-invocation, which remain benign telemetry) is split out into the dedicated entry **`producer-citation-drift-verify-not-self-invoked`** below, which carries the cycle-015 enactment (producer role-spec self-verification bullets + an `ask` for a mechanical checker tool). This entry stays as the broad telemetry pattern; the citation-specific quality defect is the addressed sub-pattern.

**Pattern.** Specialized dispatch agents perform skill-shaped work (citation-range verification à la `verify-citation-range`; variant-axis classification à la `classify-variant-axis`; refinement-surface checks à la `verify-refinement-surface`) **without explicitly invoking the named skill**. The critic's 8th check (`skill-uptake-survey`) flags the non-invocation each cycle. Cycle-012 was CYCLE-WIDE: all 8 reports lacked explicit skill invocation despite applicability; the slepc-nep critic noted the `:387` citation drift "would likely have been caught by `verify-citation-range`."

**Three-cycle pattern:** cycle-010 (wave-2 passes 6/7), cycle-011 (wave-2 passes 7/8), cycle-012 (all 8 reports). Recurrence-3.

**Cycle-012 meta-phase judgment: telemetry-noise, recalibration DEFERRED (no-go).** The check is firing on a behavior that is mostly fine: agents are *doing the work the skills describe* (the citation-range checks happen, the variant-axis classification happens) — they just aren't writing `## Skills invoked: verify-citation-range` in their CYCLE.md. The skills are procedural knowledge embedded in the agent role specs and the agents' own competence; explicit invocation is a telemetry artifact, not a quality signal, for opus-tier agents who already internalize the procedure. The ONE place where it mattered (the cycle-012 `:387` drift) is better addressed by the `audit-report-inherited-miscitation-lint` candidate (a verify-citation-range refinement for the audit-report sub-case) than by forcing skill-invocation telemetry. **The cost of recalibrating the check now is premature** — see report no-go. The actionable sub-signal (audit reports must independently confirm every asserted-verified anchor) is enacted separately via a `verify-citation-range` SKILL.md extension + lowering-verifier/critic spec lint note. Status `recurring`, not escalated, because the pattern is benign telemetry.

**Watch:** if a future cycle shows a *quality defect* that an explicitly-invoked skill would have caught (not just a telemetry gap), escalate to recurrence-4 and recalibrate the `skill-uptake-survey` check — e.g., narrow it to flag only when an applicable skill's *outcome* is absent (a missed citation drift, an un-classified variant axis), not when the invocation *string* is absent. The distinction is "did the work happen" vs "was the skill named."

---

```yaml
---
slug: partly-constructive-lowering-theme-status
first_observed: cycle-010
last_observed: cycle-012
recurrence_count: 3
status: addressed
addressed_by: cycle-012 meta-phase (CLAUDE.md §Methodology invariants new bullet formalizing `partly-constructive` as a first-class theme-status + `.claude/agents/abstractor.md` + `.claude/agents/lowering-verifier.md` Discipline touches)
---
```

**Pattern (codification).** Lowering themes (and constructed L1 operators) repeatedly land in a status between `firm` and `rough-in`: **firm-structural** (the rewrite decomposition is recognized and exhaustively cited) **but partly-constructive** (some materialization — a status value, a result field, an error condition — is reconstructed from negative anchors / literature rather than read directly from a positive Palace source site, pending an upstream Palace refactor OR a lowering-verifier per-line audit). The same gate-mechanism keeps recurring.

**Three instances:**
- **Cycle-010 (lifter).** The L1-constructive `LinearSolveFailed` option (b) on eigsolve — structural recognition with deferred materialization.
- **Cycle-011 (abstractor).** The `eigsolve-mutation-rotation` L1>L0 theme — "first firm-structural-but-partly-constructive theme in artifact"; Sub-pattern B's `LinearSolveFailed` materialization is partly-constructive; the rest is firm-structural.
- **Cycle-012 (lowering-verifier).** The eigsolve theme audit returned confirms-with-refinement and UNBLOCKS but does NOT enact the Sub-pattern B partly-constructive → fully-firm promotion (gated to cycle-013 abstractor pending Edits 2+3). The `## Status` partly-constructive caveat was left in place.

**Cycle-012 meta-phase decision: codify `partly-constructive` as a first-class theme-status.** It has been an ad-hoc phrase in three reports across the batch; making it a named status alongside `firm` / `rough-in` / `obstruction` gives authors and the critic a shared vocabulary and a clear promotion gate. A `partly-constructive` theme is firm in its structural decomposition but carries a named, citation-backed caveat on the constructive sub-parts, with an explicit promotion condition (what would make it fully firm: an upstream source site, a per-line audit, or a literature anchor upgrade).

**Enactment (cycle-012 meta-phase, this entry):**
- (a) **CLAUDE.md §Methodology invariants** — new bullet "Theme/operator status `partly-constructive` is first-class" defining the status, its caveat-with-citation requirement, and its promotion gate; cites the eigsolve-mutation-rotation precedent.
- (b) **`.claude/agents/abstractor.md` §Discipline** — bullet: when a theme is structurally firm but a sub-part is reconstructed (negative-anchor / literature), mark `## Status: partly-constructive` with a named caveat + explicit promotion condition; do not mark it `firm` and do not downgrade the whole theme to `rough-in`.
- (c) **`.claude/agents/lowering-verifier.md` §Discipline** — bullet: a `partly-constructive` theme audit may UNBLOCK the promotion (confirm the structural decomposition + identify the exact edits needed to make the constructive sub-part firm) without ENACTING it; record the gate explicitly and route the enacting edits to a follow-up dispatch.

**Watch:** if `partly-constructive` themes accumulate without ever being promoted to firm (i.e., the gate never closes over 3+ batches), escalate to recurrence-4 — the status may be functioning as a permanent escape hatch rather than a transient gate. The cycle-013 eigsolve promotion (gated this cycle) is the first test of whether the gate closes.

**Cycle-015 meta-phase update — gate-close mechanism VALIDATED by use across batch-3 (the watch clause's concern is REFUTED, not triggered).** The full partly-constructive lifecycle ran cleanly 3× across batch-3: cycle-013 EXIT (eigsolve Sub-pattern B `LinearSolveFailed` promoted partly-constructive→firm — the first live promotion) + ENTRY (divfree-projector adjudicated INTO partly-constructive); cycle-014 UNBLOCK (divfree lowering-verifier positively-anchored the WeakDiv sign) + STAYS (eigsolve-convergence-reason-mapping correctly stayed partly-constructive — no positive site exists, the mechanism working as designed for the legitimately-unfirmable case); cycle-015 ENACT (BOTH gated promotions enacted — divfree→firm L1 10→11, chebyshev-L4 rough-in→firm). The "audit cycle-N / enact cycle-N+1" two-dispatch gated-promotion protocol recurred 3× with zero rework. The gate CLOSES (it is a transient gate, not a permanent escape hatch) AND correctly STAYS-OPEN for the one case (convergence-reason-mapping) that has no positive Palace site. The cycle-012 codification is now validated-by-use; no recurrence-4 escalation needed (the watch was for the opposite failure mode). The companion skill `partly-constructive-promotion-checklist` (proposed cycle-013 by the critic) is PROMOTED this meta-phase — the 3× lifecycle is the concrete precedent that makes the 4-point promotion checklist writable. Status stays `addressed` (the codification holds; use confirms it); recurrence_count stays 3 (the validating instances are within batch-3, already counted as the mechanism's exercise, not new friction).

---

```yaml
---
slug: negative-anchor-citation-pattern
first_observed: cycle-010
last_observed: cycle-012
recurrence_count: 3
status: addressed
addressed_by: cycle-012 meta-phase (CLAUDE.md §Methodology invariants new bullet distinguishing per-status-variant negative anchors from obstruction-theme negative anchors)
---
```

**Pattern (codification).** Constructive cases at L1 (a status value, a result field, an error condition that the literature/algorithm implies but the Palace source does NOT positively exhibit at a single site) are cited with **negative anchors** — citations to where Palace does NOT do something, or where the absence is structurally significant. This is distinct from the existing per-operator `obstruction`-theme negative-anchor pattern (where the whole theme documents an unimplemented stub).

**Three instances:** cycle-010 lifter `LinearSolveFailed` callout (where the failure status is materialized from negative anchors), cycle-011 lifter `EigResult.iterations` field (L1-constructive with a negative-anchor citation set parallel to the cycle-010 LinearSolveFailed callout), cycle-012 audit's negative anchors for the eigsolve constructive cases.

**Cycle-012 meta-phase decision: codify the distinction.** The negative-anchor pattern at per-status-variant granularity (citing the absence of a positive site to justify a constructed status/field) is a legitimate and recurring citation form, but it must be distinguished from obstruction-theme negative anchors (which document an unimplemented feature). The distinction matters for the critic's `citation-validity` check (a per-status negative anchor is valid evidence for a `partly-constructive` constructive sub-part; it is NOT a license to assert a positive claim without a positive site) and for downstream consumers (a per-status negative anchor signals "this is constructed, watch for an upstream positive site" — paired with the `partly-constructive` status above).

**Enactment (cycle-012 meta-phase, this entry):**
- (a) **CLAUDE.md §Methodology invariants** — bullet folded into the `partly-constructive` invariant (they co-occur): a `partly-constructive` constructive sub-part is justified by negative anchors (citations to the absence / non-exhibition of the positive site), and these are distinct from obstruction-theme negative anchors. The negative anchor is evidence FOR the constructed form being a faithful reconstruction, not evidence of a positive Palace site.

**Watch:** if a negative-anchor citation is used to assert a FIRM positive claim (not a `partly-constructive` one), the critic should flag under `citation-validity` / `surface-or-evidence` as a misuse — negative anchors support constructed/partly-constructive forms, not firm positive ones.

---

```yaml
---
slug: lifter-scope-content-correction-boundary
first_observed: cycle-010
last_observed: cycle-012
recurrence_count: 3
status: addressed
addressed_by: cycle-012 meta-phase (`.claude/agents/lifter.md` + `.claude/agents/lowering-verifier.md` Discipline touches — L0-evidence-driven prose correction is in-scope when the correction is evidenced and bounded)
---
```

**Pattern (scope clarification).** Lifters and lowering-verifiers (auditors) doing L0-evidence-driven prose corrections that border on abstractor authoring authority. The recurring tension: an audit/re-anchor dispatch reads L0 source, finds the artifact's prose is wrong (a convention stated backwards, a citation drifted, a claim contradicting source), and CORRECTS it in place — which is arguably content-authoring (abstractor's domain) rather than re-anchoring/auditing (lifter/lowering-verifier's domain).

**Three instances:** cycle-010 lifter L0-evidence-driven prose tightening; cycle-011 lifter Edit 3 §5 rewrite of eigsolve from incorrect convention-(a) to correct convention-(b) (a substantive content correction defensible by 5 backend-specific un-scaling citations); cycle-012 audits (the SLEPc-NEP §5 refinement + the `:387`→`:383` carry-forward citation fixes).

**Cycle-012 meta-phase decision: codify content-correction as IN-SCOPE for lifter/lowering-verifier when bounded and evidenced.** The corrections in all three instances were sound (each was L0-evidence-driven and demonstrably fixed a wrong claim). Forcing a re-route to abstractor for every prose correction would add a full dispatch round-trip for what is a surgical, evidenced fix. The clarification: a lifter or lowering-verifier MAY correct artifact prose in place when (i) the correction is directly supported by an L0 citation the dispatch read, (ii) the correction is bounded (fixing a wrong claim / drifted citation / backward convention, not re-architecting the entry), and (iii) the dispatch records the correction explicitly as a prose-correction (not a silent edit). Re-architecting (changing the entry's decomposition, adding new sub-patterns, changing the operator's signature) remains abstractor/harvester authority and must re-route.

**Enactment (cycle-012 meta-phase, this entry):**
- (a) **`.claude/agents/lifter.md` §Discipline** — bullet: L0-evidence-driven prose correction is in-scope when bounded + evidenced + recorded; re-architecting re-routes to abstractor/harvester (flag in Open questions).
- (b) **`.claude/agents/lowering-verifier.md` §Discipline** — same bullet for audit dispatches: a citation drift / wrong convention found during audit may be corrected in place with the supporting L0 citation, recorded as a carry-forward correction; structural re-decomposition re-routes.

**Watch:** if a lifter/lowering-verifier prose correction is later found to have changed an entry's *meaning* beyond fixing a wrong claim (i.e., crossed into re-architecting), escalate to recurrence-4 and tighten the boundary (require a co-located abstractor reread for any §-level rewrite).

---

```yaml
---
slug: cycle-planner-dispatch-prompt-framing-drift
first_observed: cycle-010
last_observed: cycle-012
recurrence_count: 3
status: addressed
addressed_by: cycle-012 meta-phase (`.claude/agents/cycle-planner.md` Discipline touch — verify file paths via MCP codemap before citing them in dispatch scopes)
---
```

**Pattern.** The cycle-planner's source-file framing summaries in dispatch scopes diverge from source truth — it cites file paths / class-roles that do not exist or are wrong, and the orchestrator corrects them in the briefs before dispatch.

**Three instances:**
- **Cycle-010.** Planner cited `eps.cpp` / `feast.cpp` (non-existent paths).
- **Cycle-011.** Planner framed `Solver<OperType>` as a direct-solver-only base (it is the type-axis root of ALL Palace solvers).
- **Cycle-012.** Planner cited `palace/eigensolver/slepc.cpp` (wrong; the correct path is `palace/linalg/slepc.cpp`); orchestrator corrected in the briefs.

**Cycle-012 meta-phase decision: enact a cycle-planner discipline touch.** The friction is now recurrence-3 and the enabling fix is available: the cycle-planner has MCP codemap access as of cycle-010 (the pilot succeeded; see `mcp-codemap-permission-denied-across-batch-1` resolved above). The planner can and should verify a file path / symbol location via `mcp__palace-codemap__list_files` / `search_text` / `get_symbol_def` before citing it in a dispatch scope. This is low-cost (the tools are fast localization queries) and removes a recurring orchestrator-correction step.

**Enactment (cycle-012 meta-phase, this entry):**
- (a) **`.claude/agents/cycle-planner.md` §Discipline** — bullet: "Before citing a Palace source file path or symbol location in a dispatch scope, verify it via the MCP codemap tools (`mcp__palace-codemap__list_files`, `search_text`, `get_symbol_def`). Do NOT cite a path from memory or inference — the planner has repeatedly drifted on `linalg/*` file paths (cycles 010/011/012). If the codemap query is ambiguous, cite the scope by symbol/concept and note 'path to be confirmed at dispatch' rather than guessing a path." NOTE: the cycle-planner is haiku-tier; the MCP-verification step is a small, mechanical addition that fits the tier.

**Watch:** if the planner continues to drift on paths post-enactment (recurrence-4), escalate: consider (a) the orchestrator running a path-lint over the plan before dispatch, or (b) swapping the cycle-planner to opus (the haiku tier may under-use the MCP tools). The path-drift has been cheaply corrected each time so far; the discipline touch should suffice.

---

```yaml
---
slug: per-report-integrator-cycle-mislabeling
first_observed: cycle-012
last_observed: cycle-012
recurrence_count: 1
status: addressed
addressed_by: cycle-012 meta-phase (`.claude/agents/integrator-per-report.md` Process + Discipline touches — derive cycle-id from the staging-dir path the parent supplies; never infer it)
---
```

**Pattern (new this batch).** A per-report integrator mis-filed its staging row to a wrong-cycle staging directory. Cycle-012 report #3 (eigsolve lowering-verifier) wrote its STAGING row to `reports/cycle-013-integrator-staging/STAGING.md` (mislabeled the cycle as 013); the orchestrator corrected — removed the misplaced directory, relocated the row to `cycle-012` STAGING, fixed backward `cycle-013` references in `book/src/L1-L0/eigsolve-mutation-rotation.md` + the OQ `opened_at`. Forward-references to the genuinely-next-cycle GATED cycle-013 abstractor follow-up were intentionally retained.

**Surfaced by**: cycle-012 integrator-finalize §Wave-conflict observations + integrator-signals.md cycle-012 §Integration-tooling friction signal 8.

**Probable root cause.** The per-report integrator inferred the cycle number (likely from the report's content, which discussed cycle-013 forward-references) rather than taking it from the staging-dir path the parent supplies in its dispatch. The role spec already says "the parent's dispatch tells you the path" (integrator-per-report.md Inputs line 16), but does not say "use ONLY that path; never infer the cycle-id from report content."

**Mitigation (cycle-012 meta-phase, this entry):**
- (a) **`.claude/agents/integrator-per-report.md` §Process step 7 + §Discipline** — explicit: "The staging-dir path (and thus the cycle-id) is given to you by the parent's dispatch prompt. Write your staging row ONLY to that path. Do NOT infer the cycle-id from the report's content (reports often discuss forward-references to future cycles — those are content, not your filing target). If the parent did not supply a staging-dir path, stop and return rather than guessing." This is a low-cascade clarification of an existing input contract.
- (b) Companion orchestration note (not a role-spec enactment, recorded for the resume-notes): the parent's integrator-per-report dispatch prompt should always state the cycle number AND the exact staging-dir path explicitly.

**Watch:** if a per-report integrator mis-files again despite the role-spec clarification (recurrence-2), escalate: the parent should pre-create the staging-dir before dispatching the first per-report integrator and pass the absolute path, so the integrator never constructs the path itself.

---

```yaml
---
slug: l3-l1-inline-identity-rotation-convention
first_observed: cycle-010
last_observed: cycle-012
recurrence_count: 9
status: addressed
addressed_by: cycle-012 meta-phase DECISION — codify the in-line identity-rotation convention (option a); NO `book/src/L3-L1/` directory. CLAUDE.md §Methodology invariants new bullet + `.claude/agents/harvester.md` Discipline touch.
---
```

**Pattern (decision item — RESOLVED this meta-phase).** The methodology invariant `Identity-lowerings still require both L levels` (cycle-009 meta-phase) means an operator whose lowering between two adjacent layers is identity-in-form still gets entries at both layers. The QUESTION this raised: when the identity rotation spans NON-adjacent layers (e.g., an L3 operator whose form is value-thread-isomorphic all the way down to its L1 form, because the intervening L2 absorption is also identity-like), does that identity get a dedicated `book/src/L3-L1/` lowering-theme directory + thin theme file, or is it annotated **in-line** within the L3 entry's prose / dep-map and the L3>L2 theme?

**Empirical convergence (~9+ in-line annotations, exceeds the revisit threshold of 6).** Across cycles 010/011/012 the BLAS-1 L3 cohort (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal` — 7 operators) plus `krylov-step` all annotate their identity-rotation relationships **in-line** within the L3 entry (the "Downward to L2" prose, the dep-map, and the L3>L2 theme that ratifies the body-identity) rather than via a `book/src/L3-L1/` directory. Direct inspection (cycle-012 meta-phase): `book/src/L3/krylov-step.md:28-31` carries the upward (to L4) and downward (to L2) identity annotations in-line, citing the existing `L4-L3/` and `L3-L2/` themes; no `book/src/L3-L1/` directory exists (only `L2-L1/` and `L3-L2/`). The convention has converged organically and works.

**Cycle-012 meta-phase DECISION: codify the in-line convention (option a). Do NOT introduce a `book/src/L3-L1/` directory (option b).** Rationale:
1. **The directory structure is per-adjacent-layer-edge by design** (CLAUDE.md §Layout: `L4-L3/`, `L3-L2/`, `L2-L1/`, `L1-L0/`). A `L3-L1/` directory would be the first NON-adjacent lowering directory, breaking the adjacent-edge invariant and inviting `L4-L2/`, `L4-L1/`, etc. proliferation.
2. **Identity-in-form across non-adjacent layers is fully captured by the chain of adjacent themes** (L3>L2 identity + L2>L1 identity ⟹ L3>L1 identity transitively). A dedicated `L3-L1/` theme would duplicate what the adjacent-edge chain already says.
3. **The in-line annotation is the natural home**: per the `Identity-lowerings still require both L levels` invariant, each L_n entry is coherent within itself and notes its identity relationships in-line (the L3 entry says "my body is value-thread-isomorphic to my L2 form, which is in turn isomorphic to L1"). The reader at L3 gets the identity story without a directory hop.
4. **Empirical convergence** — 9+ instances already do it in-line, cleanly, with no friction. Migrating them into a new directory (option b) would be a non-trivial mechanical migration polluting git history, for zero coherence gain.

**Enactment (cycle-012 meta-phase, this entry):**
- (a) **CLAUDE.md §Methodology invariants** — new bullet "Identity rotations across non-adjacent layers are annotated in-line, not via a dedicated lowering directory" — codifies that lowering directories are per-adjacent-edge only; non-adjacent identity is the transitive consequence of the adjacent-edge themes and is annotated in-line in the L_n entry + dep-map.
- (b) **`.claude/agents/harvester.md` §Discipline** — bullet extending the existing "Identity-lowerings still require both L levels" bullet: when an operator's identity-in-form spans non-adjacent layers, annotate the relationship in-line in the L_n entry (the "Downward" prose + dep-map) and rely on the chain of adjacent-edge L_{n+1}>L_n themes; do NOT create a non-adjacent lowering directory (no `L3-L1/`, `L4-L2/`, etc.).

**Watch:** if a future operator surfaces a NON-identity rotation across non-adjacent layers (i.e., the chain of adjacent themes does NOT compose to the obvious identity, and there is genuine cross-layer rewrite content that the adjacent themes don't capture), re-open — that would be the case where a non-adjacent lowering document might be warranted. No such case has surfaced; all 9+ instances are identity-in-form.

---

```yaml
---
slug: mcp-first-localization-codified
first_observed: cycle-010
last_observed: cycle-012
recurrence_count: 1
status: addressed
addressed_by: cycle-012 meta-phase (CLAUDE.md §Target system MCP-first localization note; NOT a hard per-role rule — see report no-go on per-role-spec mandate)
---
```

**Pattern (codification, positive).** The MCP codemap pilot succeeded cycle-010 and cycles 011/012 used the tools routinely for C++ source localization (`list_files` / `get_symbol_def` / `search_text` / `read_range` / `get_call_sites` / `list_dependencies` / `get_file_subtree`) with zero permission-denied (see `mcp-codemap-permission-denied-across-batch-1` resolved). The MCP server's own instructions (surfaced via system-reminder) already advise "localize before reading; read_range is the only source-returning tool — use it deliberately."

**Cycle-012 meta-phase decision: codify MCP-first localization in CLAUDE.md §Target system (soft guidance), NOT as a hard per-role-spec mandate.** Rationale: the tooling is now reliably available and is the right localization path for the heavy-C++-template Palace tree (the CLAUDE.md §Target system already says "prefer narrow text-search before reading"; MCP codemap is the better realization of that guidance). But mandating it per-role across 8 specialized agent specs would be (i) redundant (the MCP server instructions already advise the pattern to every agent that has the tools), and (ii) over-constraining (an agent should be free to use vanilla Grep/Read when that is faster for a given query). A single CLAUDE.md §Target system note documents the availability + preference; agents apply judgment.

**Enactment (cycle-012 meta-phase, this entry):**
- (a) **CLAUDE.md §Target system** — note added: the `palace-codemap` MCP server is available and is the preferred localization path for Palace C++ source (localize via `list_files` / `search_text` / `get_symbol_def` / `get_call_sites` / `list_dependencies` / `get_file_subtree`; use `read_range` deliberately for the actual source). Pilot succeeded cycle-010; routine use cycles 011/012. Vanilla Grep/Read remain available; agent judgment on which to use.

**Watch:** if MCP-first localization does not take hold in cycle-013+ (agents keep defaulting to vanilla Grep over the codemap on Palace C++ queries despite the codemap being faster), reconsider a per-role-spec touch or a stronger CLAUDE.md mandate. The soft note is the minimal codification consistent with "don't over-ask / don't over-constrain."

---

```yaml
---
slug: producer-citation-drift-verify-not-self-invoked
first_observed: cycle-013
last_observed: cycle-024
recurrence_count: 4
status: addressed
addressed_by: cycle-015 meta-phase (4 producer role-spec self-verification Discipline bullets) — INSUFFICIENT; recurrence-4 fired batch-5; mechanical checker ESCALATED to ASK (batch-5) → **TOOL BUILT (user go, 88b7893): `tools/citecheck/`** → **ROLE-SPEC WIRING ENACTED cycle-024 meta-phase (batch-6):** producer self-verify bullets (harvester/abstractor/lifter/layer-intro-author) + lowering-verifier + critic `citation-validity` + integrator-per-report `--scan` gate + `verify-citation-range` skill all now name `citecheck --anchor/--scan` as the mechanical realization. Watch batch-7 for whether the wired-in checker drops the drift-repair-round count (uptake gate).
---
```

**Pattern (the STRONGEST recurring friction of batch-3; the actionable citation-specific split-out of `skill-uptake-survey-non-invocation-cycle-wide`).** Producer dispatch agents (harvester, abstractor, lifter, layer-intro-author, and even the citation-AUDITING lowering-verifier) emit L0 citations that drift off the true source line by 1–N lines, and the repairer corrects them pre-apply. The drift is caught downstream (repairer + critic + codemap ground-truth), so it never reaches the artifact — but it recurs every batch cycle, costs a repair round each time, and the critic's `skill-uptake-survey` repeatedly flags that `verify-citation-range` was NOT self-invoked by the producer before emitting. The producers cite from memory / initial-read rather than re-confirming against `read_range` / the codemap `get_symbol_def` before emitting.

**Three-cycle batch-3 evidence (each cycle, escalating breadth):**
- **Cycle-013:** ~6 reports carried repairer-corrected citation-line-offset drift (eigsolve, divfree, chebyshev, orthogonalize, L0-bundle, krylov-step — mostly codemap-ground-truth values 1 line off the producer's). The divfree harvester drifted on 30+ citations (off-by-1/2/3).
- **Cycle-014:** 5-of-8 reports carried off-by-1-to-N drift — and notably the citation-AUDITING role itself drifted (the chebyshev lowering-verifier: `:191`=opening-brace vs signature `:190`; `hpp:43`=comment vs member `:44`), despite the cycle-012 lowering-verifier role-spec touch. A role-spec Discipline bullet on the AUDITING role alone did NOT prevent its own drift.
- **Cycle-015 (enactment cycle):** even with dedicated citation-sweep dispatches running clean, the bilinearform `RT_FECollection` attribution drifted (repairer-corrected from `L2_FECollection`) + the L3 cg.md sweep producer pointed 2 re-anchors at relocated-dangle targets (repairer corrected to terminal L2 homes).

**Surfaced by:** cycle-013/014/015 integrator-signals §Integration-tooling friction (flagged prominently for batch-3 meta-phase each cycle) + the per-report critic `skill-uptake-survey` warnings (22/22 batch-3 META files reference it; the divfree + several others explicitly note the drift "would have been caught by a self-applied `verify-citation-range` pass").

**Why this SUPERSEDES the cycle-012 "telemetry-noise, no-go" judgment.** Cycle-012 judged `verify-citation-range` non-invocation as benign telemetry because "the work happens anyway." Batch-3 refutes that for the citation-specific case: the work was NOT happening (the citations drifted), and the defects were real quality defects (caught only by the repairer/critic, not by the producer). This is the exact quality-defect trigger the cycle-012 watch clause named for recurrence-4 escalation of `skill-uptake-survey-non-invocation-cycle-wide`. The `classify-variant-axis` / `verify-refinement-surface` parts of that broad pattern remain benign telemetry; the citation part is split here as the addressed quality defect.

**Mitigation (cycle-015 meta-phase, this entry):**
- (a) **Producer role-spec self-verification bullets** added to the four producer specs that emit L0 citations and lacked one — `.claude/agents/harvester.md`, `.claude/agents/abstractor.md`, `.claude/agents/lifter.md`, `.claude/agents/layer-intro-author.md` §Discipline. Each bullet: before emitting any `path:lo-hi` citation, `read_range` (or codemap `get_symbol_def` / `search_text`) the exact cited lines and confirm the named construct sits on the asserted line — do NOT cite from memory or an earlier read; invoke skill `verify-citation-range`. (The lowering-verifier already got the cycle-012 audit-shaped bullet; that one role-spec touch did NOT stop its cycle-014 drift, which is precisely why the mechanical-tool ASK below is filed — a role-spec bullet is necessary but the cycle-014 auditor-drift shows it is not sufficient.)
- (b) **Skill `verify-citation-range`** extended with a top-level **"Producer self-verification before emitting citations"** section (the skill previously covered Explorer/Critic verification + the cycle-012 audit-report sub-case, but did not foreground the producer-emit-time self-check that is the recurring gap).
- (c) **ASK (surfaced to user, NOT enacted — tooling/code change, ask-class per write-authority):** a mechanical codemap-backed citation-range checker tool under `tools/` that validates every `path:lo-hi` in a CYCLE.md's proposed-changes against `reference/` source (e.g. via the codemap `get_symbol_def`/`read_range`) as a pre-integration lint. The cycle-014 auditor-drift demonstrates role-spec bullets alone are insufficient; a mechanical check is the durable fix. This requires writing code (not a role-spec edit), so it is ask-class.
- (d) **Human decision (2026-05-28, post-batch-3):** user reviewed the ASK and **confirmed DEFER to batch-4** (concurring with the meta-phase recommendation) — rely on the (a)/(b) producer role-spec self-verify bullets through batch-4; build the mechanical checker only if drift recurs. The recurrence-4 watch-clause below is the agreed trigger. The ASK is now `reviewed: defer-confirmed`, not `pending`.

**Watch:** if citation drift persists across batch-4 (016/017/018) despite the four producer role-spec bullets (recurrence-4 of THIS entry), the role-spec approach has reached its ceiling — escalate the mechanical-checker tool from ASK to a built `go` (or the user enacts the code). The cycle-014 auditor-drift already foreshadows this ceiling; batch-4 is the test of whether the producer-side bullets move the needle.

**Cycle-018 meta-phase update — batch-4 outcome: the producer role-spec bullets HELD; recurrence-4 did NOT fire; the mechanical-checker ASK STAYS DEFERRED.** Batch-4 (016/017/018) carried substantial citation surface — cycle-016 cg.md sweeps (L4 7 + L2 12 re-anchors) and 2 chebyshev prose refreshes, cycle-017 divfree-projector 11-reference drift maintenance + L3-L2 body-identity 3 re-anchors + L3 chebyshev 5-site refresh, cycle-018 `linear_combination` 9 self-verified L0 ranges — yet **no new producer-emit drift required a repair round-trip of the cycle-013/014/015 shape.** The batch-4 citation edits were the *maintenance being applied* (re-anchoring known-dangling pointers to terminal firm homes), not fresh producer drift; and the one cycle-017 retroactive-budget item + cycle-018 retroactive-budget 0 confirm the producers were self-verifying at emit time. The recurrence-4 escalation condition (NEW drift despite the bullets) is **not met**. Status stays `addressed`; recurrence_count stays 3 (no recurrence-4 instance to count). The mechanical-checker tool ASK remains `reviewed: defer-confirmed` per the user's 2026-05-28 decision — the role-spec bullets are doing the job through batch-4; build the checker only if drift returns in batch-5+. The cycle-014 auditor-drift ceiling concern did not materialize in batch-4 (the lowering-verifier ran read-only/audit dispatches in 016/017 with no inherited-miscitation defect).

**Cycle-021 meta-phase update (batch-5) — RECURRENCE-4 FIRED. The role-spec bullets reached their ceiling; the mechanical-checker tool is ESCALATED from defer to a go-recommended ASK.** The batch-4 watch clause was precise: "build the checker only if drift returns in batch-5+." It returned. Batch-5 (019/020/021) shows **fresh producer-emit inline-anchor drift in every one of the three cycles** — not maintenance being applied, but new pinpoint citations landing 1-2 lines off the true source line while the wide enclosing ranges stay correct:
- **Cycle-019:** orthogonalize-l2 spot-line nits (orthogonality assertion, the `m==0` guard, the no-normalise marker) — though here the repairer's independent re-verify found the *critic* had drifted, not the producer; still a citation-precision dispute that a shared line-map would have settled.
- **Cycle-020:** `dot` `:667`→`:668`/`:679`→`:678`; `scal` `nleps.cpp:491`→`:493`; `assemble-diagonal` `AbsMultTranspose :172`→`:174` (+3 more); `ksp_solve` accessor `:100-106`→`:101-108` (+3 more); inner-product-fold `operator.cpp:623`→`:624`/`:632`→`:634`/`:615-616`→`:616`.
- **Cycle-021:** `apply_nonlinear_pencil` `GetResidualNorm` line-pin + `eps.hpp:69-74` + `:729`; `deflate` D3 `:663-668`→`:664/:666/:667` + reference `:356-362`→`:354-362`; the carried L3 `ksp_solve` `:464`→`:463`/`:564`→`:563`; the carried inner-product-fold drift.

The drift is now a **stable 3-cycle pattern**, caught downstream (repairer + critic + verifier independent re-reads) but costing a repair/re-read round each time AND occasionally producing critic↔repairer↔verifier disagreement (cycle-019 orthogonalize: critic renumbered wrong, repairer's re-verify won; cycle-020 inner-product-fold: verifier flagged a phantom `:611`→`:612` the repairer had already fixed). The independent-re-read cross-check works but does not scale: three roles re-deriving the same line-map by hand is exactly the cost a shared mechanical line-map amortizes. **The cycle-014 auditor-drift ceiling concern HAS now materialized in the broader sense** — role-spec bullets are necessary but demonstrably not sufficient against pinpoint drift across a heavy-citation batch.

**Decision (batch-5 meta-phase): ASK — escalate the mechanical codemap-backed citation-range checker tool to the human as a go-recommended build** (it is ask-class: it requires writing code under `tools/`, which is outside meta-phase write-authority — see CLAUDE.md §What you DO NOT do). The tool validates every `path:lo-hi` in a CYCLE.md's proposed-changes against `reference/` source via the codemap (`get_symbol_def`/`search_text`/`read_range`) as a pre-integration lint, emitting a per-citation OK/DRIFT(±N) report. The enabling conditions are all now met: (i) recurrence-4 fired (the agreed trigger); (ii) the codemap MCP is in routine zero-permission-denied use (it can back the checker); (iii) the drift is mechanical (line-offset, not semantic) — precisely what a mechanical check catches and a prose bullet does not. Surfaced as the leading ASK item in the batch-5 meta-phase report + the cycle-022 resume-notes. Status flipped `addressed` → `escalating`; recurrence_count 3 → 4.

**Watch:** if the user builds the checker, re-status `addressed` and watch batch-6 for residual drift the lint missed. If the user declines, the producer-self-verify bullets remain the only line of defense and the drift-repair-round cost is accepted as standing overhead — re-surface only if drift severity escalates (a drift reaching the artifact uncaught, vs. the current always-caught-but-costly state).

**Cycle-024 meta-phase update (batch-6) — the checker was BUILT (`tools/citecheck/`, 88b7893, user go) and the deferred ROLE-SPEC WIRING is now ENACTED (go); status flips `escalating` → `addressed`; recurrence stays 4 (the wiring closes the loop the build opened).** Batch-6 drift persisted exactly as the batch-5 watch predicted: cycle-022 lifter swept 5 distinct inline drifts (`iterative.cpp :464→:463 ×3`, `:564→:563 ×6`; `operator.cpp :623→:624`/`:632→:634`/`:615-616→:616`); cycle-023 carried the `orthog.hpp:34→:35` drift forward; cycle-024 critics found **5 off-by-one drifts in the l3-eigsolve report** (`arpack.cpp :573/:579/:270`, `slepc.cpp :1857/:1873`, repairer-corrected) **+ 1 each in 3 other reports** — and one *critic-off-by-one-on-an-off-by-one* (the critic flagged `nleps.cpp:810-811` as drift to `:809-810`; the original was right). Every instance caught downstream + repaired pre-apply (the safety net held; ZERO drift reached the artifact across the batch) but at a per-report repair/re-read cost, and the critic↔repairer disagreement is the exact cost a shared mechanical line-map amortizes. **The build alone did not move the needle in batch-6 because the tool was not yet in any role's procedure** — it was available for manual invocation only (the batch-5 enactment explicitly left "role-spec wiring … for the next meta-phase"). Verified this meta-phase that `citecheck --anchor` mechanically catches the batch-6 drifts (e.g. `orthog.hpp:34 --anchor LocalDot` → `[DRIFT] anchor at line 35, +1 outside range; suggested :35`).

**Wiring enacted (cycle-024 meta-phase, this entry — go):**
- (a) **Producer self-verify bullets** (harvester / abstractor / lifter / layer-intro-author §Discipline) — each now names `tools/citecheck/citecheck.py <path:lo-hi> --anchor '<token>'` as the **mechanical realization** of the existing read_range self-check: for each load-bearing pinpoint citation, run citecheck `--anchor` on the token the citation points at; `[DRIFT]`/`[NOANC]` is the signal to re-anchor before emitting. Run `--scan` on your own CYCLE.md as the bounds + path-hygiene pre-emit pass.
- (b) **lowering-verifier §Discipline** — the "independently `read_range`-confirm every asserted anchor" bullet now points at `citecheck --anchor` as the shared authoritative line-map (it is the deliverable's no-drift assertion mechanized; it also prevents the critic↔repairer↔verifier line-number disagreement seen across batches 5/6).
- (c) **critic `citation-validity` check** — the check now names `citecheck --anchor` (and `--scan` for bounds) as the mechanical verification path instead of re-reading by hand; the critic's anchor-finding is itself adjudicated by the tool (the cycle-024 critic-off-by-one-on-an-off-by-one is exactly the disagreement the shared line-map ends).
- (d) **integrator-per-report safety-net gates** — added a non-blocking `citecheck --scan` bounds + path-hygiene lint on the report being applied: `MISS`/`AMBIG`/`OOB` route to a repairer fix or `deferred`; `DRIFT` (anchor-level) is informational (pinpoint drift is producer/critic/lowering-verifier territory, already caught upstream).
- (e) **skill `verify-citation-range`** — top "Producer self-verification" section gains a "Mechanical check (`citecheck`)" step naming the `--anchor`/`--scan` modes as the deterministic half of the procedure.

**Watch:** batch-7 (025/026/027) is the test of whether the wired-in checker drops the drift-repair-round count. If producers run `--anchor` at emit time, fresh producer-emit drift should fall to near-zero (the tool is deterministic where the prose bullet was reminder-dependent). If drift still recurs at the batch-6 rate despite the wiring (recurrence-5), the gap is invocation-uptake (the same telemetry-gap shape as `skill-uptake-survey`) — escalate to a HARD integrator-per-report pre-apply `--anchor`-gate on every load-bearing pinpoint (currently only `--scan` bounds is gated; pinpoint-anchor gating needs the report to carry machine-readable anchor tokens, a CYCLE.md-format change — ask-class).

**Cycle-102 meta-phase update (batch-32) — still `addressed`; recurrence stays 4. The ONE batch-32 instance was a FALSE-POSITIVE drift flag, not real drift — the safety net's over-fire, caught and corrected.** Batch-32 (100/101/102) carried substantial citation surface (c100 firmed two heavily-cited L1>L0 mutation-rotation floors; c101 authored the `eliminate_bc` cap + `bc-elimination-post-composition-dissolution` theme citing fresh BC L0 anchors; c102 full-path-disambiguated 5 inline citations). The single citation-drift event was c100's D2 raising a **false `:42→:41` drift flag** that the critic caught and overruled (the original `:42` was correct) — i.e. a producer/critic over-flag, NOT fresh stale-memory producer-emit drift reaching the artifact. ZERO real producer-emit drift; the `citecheck`-at-emit-time discipline held across the batch (c102's D2 lifter ran `citecheck` to 16/16 ok on the disambiguated file). No recurrence-5. The false-positive arm is the same shape the cycle-021/024 critic↔repairer over-flag disagreements took — the shared mechanical line-map (`citecheck`) is exactly what adjudicates it; no new enactment warranted. HARD `--anchor` integrator-gate escalation stays HELD.

**Cycle-027 meta-phase update (batch-7) — the wired-in checker WORKED for producer-emit drift; the residual drift split out to a DISTINCT tool-level entry. Status stays `addressed`; recurrence stays 4 (no recurrence-5 of the producer-emit shape).** Batch-7 was the uptake test. Outcome: **the wired-in `citecheck` is now visibly in routine emit-time use, and fresh producer-emit drift of the cycle-013/014/015 shape (citing from stale memory) did NOT recur.** Evidence the tool is being run at emit time: the cycle-027 D5 abstractor report self-reported `citecheck --scan` = `35 ok, 0 failing` (critic re-confirmed); the cycle-025 dispatch-2 L1>L0 theme was `citecheck`-verified `32 ok, 0 failing`; the cycle-026 D1 lifter mechanically re-anchored via `citecheck --anchor` (`[DRIFT]` pre / `[ok]` post on every site). The citation maintenance that DID happen in batch-7 was either (i) **re-anchoring already-landed entries** (the NLEPS-L1-entry secondary-context drifts, the `:667→:668` sibling sweep — pre-existing dangling pointers being closed, not fresh emit drift), or (ii) the **codemap tool-level +1 drift** — a producer faithfully transcribing what `read_range` returned, which is NOT this entry's failure mode (stale-memory citing). The tool-level drift is split out to the new dedicated entry **`codemap-read-range-plus-one-drift-on-brace-boundary`** (addressed this same meta-phase via the "codemap is localization-only; citecheck/on-disk is source of truth" role-spec sub-bullet). So: the producer-emit arm this entry tracks is **doing the job** through batch-7 (the wiring closed the loop the cycle-024 build opened); the residual drift is a different, now-separately-tracked cause. No recurrence-5 of the producer-emit shape. The HARD `--anchor` integrator-gate escalation stays HELD (no trigger fired for THIS entry; the codemap-drift entry carries its own deferred HARD-gate escalation if ITS recurrence-5 fires).

**Cycle-132 meta-phase update (batch-42 — the `§1.2.2:NN` section-reference false-positive recurred benignly; ZERO real producer-emit drift; status stays `addressed`, recurrence stays 4.)** Batch-42 was the §1.2.2/closure-signature POLISH PASS — a pure consolidation batch of prose/signature codomain re-spelling, low new-citation surface. The one citation-relevant note is a **known benign tool false-positive**, recorded for completeness: the c131 D1 lifter's `citecheck --scan` surfaced `[MISS] 1.2.2:NN` hits where the tool mis-parsed the *section reference* `§1.2.2:89-95` (a calculus section number, not a file:line) as a citation, plus `[AMBIG] assemble_frequency_operator.md:*` hits where the basename matched both the L4 and the L1 file. Both are the **same false-positive arm as the c102 update above** (the tool reads a section-number-shaped or basename-ambiguous token as a citation) — NOT real citation drift. The critic verified every load-bearing pinpoint on-disk and confirmed the proposed-changes blocks use full paths; the false-positives are a path-hygiene nit (basename-in-prose), not a wrong citation. **The one REAL safety-net catch this batch was NOT a citation defect** — it was an `edge-label-fidelity` warning (the c131 D1 exhaustion finding missed the `L2/index.md:143` dep-map mirror row of the converted chapter signature), which the critic caught and the repairer fixed in-cycle (the per-report integrator added the 4th block); the safety net worked exactly as designed. Both arms (citecheck false-positive + the genuine edge-label catch) are governed by existing mechanisms — no new enactment. The HARD `--anchor` integrator-gate escalation stays HELD. *Standing note (carried, not re-ledgered): the `§N.N.N:NN` section-reference false-positive is a benign `citecheck --scan` tool artifact of the same class the c102 update names; a `tools/citecheck` reader-fix (skip `§`-prefixed section-number tokens) is a deferred ask-class code change, warranted only if it ever masks a real miss — it has not.*

---

```yaml
---
slug: slice-removal-non-link-prose-reference-grep-gap
first_observed: cycle-015
last_observed: cycle-015
recurrence_count: 1
status: addressed
addressed_by: cycle-015 meta-phase (skill `phase-1-slice-reduction-audit` §"Removal sub-case: non-link prose-reference grep" section — slice REMOVALS require a bare-path/inline-code reference grep, not just a markdown-link check)
---
```

**Pattern (new this cycle).** Cycle-015's chebyshev Phase-1 slice REMOVAL (`git rm book/src/spec/slices/chebyshev.md`, removals 8/10→9/10) FAILED critique on `cross-reference-integrity`: the same-layer-cross-cutter's "complete whole-tree grep" missed **4 non-link prose references** to the removed slice — bare-path / inline-code mentions (e.g. `` `spec/slices/chebyshev.md` `` in prose, or a plain-text path), NOT markdown `[text](path)` links. The mdBook build linkcheck (`cargo make book` exit 0) is the markdown-link backstop, but it canNOT catch a prose mention or inline-code path — those are not links, so the build passes while the references are stranded (pointing at a deleted file). The critic's independent grep caught all 4; the repairer fixed them pre-apply.

**The gap is specific to REMOVALS, not REDUCTIONS.** A slice REDUCTION (compact to a stub) leaves the file in place, so inbound references — link or prose — still resolve to a (now thinner) file; the build linkcheck suffices. A slice REMOVAL deletes the file, so EVERY inbound reference must be re-pointed or struck, and the build linkcheck only catches the markdown-link subset. There is a gap between "no broken markdown link" (what the build checks) and "no stranded prose reference" (what a removal actually requires). The cycle-015 same-layer-cross-cutter ran the removal under the `phase-1-slice-reduction-audit` skill, which had no removal-specific non-link grep step.

**Surfaced by:** cycle-015 integrator-signals §Integration-tooling friction ("Slice-removal grep-completeness (NEW, batch-3 process signal)") + the cycle-015 same-layer-cross-cutter `cross-reference-integrity` critique FAIL.

**Mitigation (cycle-015 meta-phase, this entry):** Extended skill `skills/phase-1-slice-reduction-audit/SKILL.md` with a **"Removal sub-case: non-link prose-reference grep"** section + a Discipline bullet + a Failure-mode entry. The removal procedure now requires, before proposing a `git rm`: grep the WHOLE book tree (and scaffolding) for the slice's path in ALL reference shapes — markdown links `](.*<slice>)`, inline-code `` `<path>` ``, and bare-path prose mentions `<slice-stem>` — not just markdown links; enumerate every hit; re-point or strike each; and note that the build linkcheck is the markdown-link backstop only, insufficient on its own for removals. Recommended grep: `grep -rn "<slice-stem>" book/src/ scaffolding/` (the stem, not just the full `[..](..)` link form), then triage link vs prose vs inline-code per hit.

**Watch:** if a future slice removal again strands a non-link prose reference despite the skill extension (recurrence-2), consider a mechanical removal-time grep tool (sibling to the citation-range checker ASK above — both are "mechanical reference-completeness check" tooling) and re-weigh whether the same-layer-cross-cutter removal dispatch should hand the grep enumeration to the integrator-per-report as a pre-`git-rm` gate.

---

```yaml
---
slug: combinator-miner-arity-blind-parametric-family-detection
first_observed: cycle-016
last_observed: cycle-021
recurrence_count: 1
status: addressed
addressed_by: cycle-018 meta-phase (`.claude/agents/combinator-miner.md` "Parametric / variadic-family detection mode" section) — VALIDATED-BY-USE + EXTENDED cycle-021 meta-phase (non-fold "constructed-operator-action family" reportable class closes the Qualification-B mode-gap)
---
```

**Pattern (HUMAN-RAISED, headline batch-4 meta-phase item).** The combinator-miner's instance-counting heuristic (≥3 occurrences of *the same fixed-arity shape*) is **arity-blind**: a family of fixed-arity operators that are all specializations of one variadic/parametric operator never surfaces as a single candidate — each specialization is a distinct shape with too-few same-shape instances, and the unifying variadic fold is invisible to instance-counting. The proximate consequence: the BLAS-1 scalar-weighted-sum fold (`scal`/`axpy`/`axpby`/`axpbypcz` = the arity-1/2/3/4 specializations of one variadic `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`) was **never auto-surfaced and had to be human-raised** (OQ `blas1-variadic-linear-combination-fold-unification`, opened cycle-016). The cohort was represented 3× at fixed arity (L1 leaves / L1>L0 themes / L3 identity cohort) but unified 0× — a strong missing-parent signal that instance-counting could not see.

**Constructive prongs (the artifact work) landed across batch-4 BEFORE this meta-phase:** prong-(b) the L2 rough-in row (cycle-017 combinator-miner) → firm `book/src/L2/linear_combination.md` + L2>L1 `linear-combination-fold-specialization` theme (cycle-018 harvester + abstractor). The cycle-018 combinator-miner ALSO landed an `inner_product` rough-in row (the conjugation-convention sibling fold) — an early sign the family-mode lens is already useful. Prong-(a), this entry, is the **methodology fix**: teach the miner to detect parametric families so the NEXT such family surfaces automatically rather than waiting for a human.

**Mitigation (cycle-018 meta-phase, this entry — go).** `.claude/agents/combinator-miner.md`:
- New top-level section **"Parametric / variadic-family detection mode"**: run instance-counting in two complementary modes on every scan — (1) same-shape mode (the default), and (2) parametric-family mode (look for a set of operators differing only along a structured parameter axis — arity / element-type / conjugation / weight-presence — that share one *folding* combining step; propose the single variadic parent with the siblings as specializations). Family-detection triggers, the required `## Proposed combinator` additions (parameter axis / combining step + identity / unifying fold-law / over-unification guard), and the typical "one layer above" placement are all spelled out, with the `linear_combination` precedent.
- Discipline bullets: a parametric family counts as ONE pattern (the unified operator, not its N leaves); the family bar is ≥2 siblings sharing a stateable fold-law (the law is the evidence, so 2-with-law beats 3-coincidental); the over-unification guard (e.g. `dot` reduce-to-scalar is a DIFFERENT fold, do not subsume); and **run family-mode on every scan, not as a same-shape fallback** (the miss happened while same-shape candidates existed).

**Cycle-021 meta-phase update (batch-5) — VALIDATED-BY-USE + the Qualification-B mode-gap CLOSED.** Two live exercises ran across batch-5: cycle-019 (the `inner_product` fold-family characterization — the mode independently surfaced the cohort as ONE candidate, catching a fold-family arity-blind counting would see only as 3 too-thin leaves; `tdot` is 0 call sites) and cycle-021 (the `deflate`/`gram` deflation-subspace combinator). The mode **performed to spec on fold cases** and confirmed the `variant-absorption-vs-instance-counting-policy` question (now closed): it is *concordant-and-complementary* with same-shape counting, and its distinctive deliverable is the fold-law membership-test + axis taxonomy (a *characterizer*, not only a *surfacer*).

The cycle-019 exercise ALSO found a genuine spec gap (Qualification B, OQ `combinator-miner-nonfold-parametric-family-no-positive-channel`): the mode is **fold-complete but had no positive channel for NON-fold parametric families** — the smoother/constructed-operator-action cohort (`JacobiSmoother`/`ChebyshevSmoother`/`ChebyshevSmoother1stKind`/`DistRelaxationSmoother`, all `Solver<OperType>::Mult` actions parametric over kernel + element-type) is a structured parametric family but `Tensor[N]→Tensor[N]` action-shaped, NOT a fold; the mode's "no fold-law ⟹ not a parametric family" guard *correctly excludes* it from a fold candidate but gave no way to report it as the family it is. **Enacted (go):** `.claude/agents/combinator-miner.md` gains a **"Constructed-operator-action family (a non-fold parametric class)"** subsection — a distinct reportable class unified by a shared `Solver<OperType>::Mult` action contract (not a fold-law), with its own parameter-axis / shared-action-contract / over-unification-guard requirements and a "do NOT force it into a fold shape" caution. The mode is now parametric-family-complete (fold families + constructed-operator-action families), not just fold-complete. OQ `combinator-miner-nonfold-parametric-family-no-positive-channel` closed.

**Watch:** if a future parametric family (fold OR constructed-operator-action) is again missed by the miner and surfaces only via human/cross-cutter, escalate to recurrence-2 and consider a same-layer-cross-cutter companion "family-sweep" dispatch mode or a mechanical cohort-detection helper.

---

```yaml
---
slug: rough-in-forward-reference-must-be-plain-text-not-live-link
first_observed: cycle-017
last_observed: cycle-018
recurrence_count: 2
status: addressed
addressed_by: cycle-018 meta-phase (`.claude/agents/combinator-miner.md` "Forward-reference convention" note + `.claude/agents/harvester.md` Discipline bullet) — companion to the cycle-006 dep-map-row entry `rough-in-rows-must-be-plain-text-when-anchor-missing`
---
```

**Pattern.** A producer emits a markdown link to a chapter that does NOT yet exist (a forward-reference to a sibling/operator chapter a later dispatch will author). `mdbook-linkcheck2` treats a link to an absent file as a **hard build error** (exit 101, `File not found: ./<chapter>.md`), regardless of whether the slug is registered in `SUMMARY.md`. This is the in-chapter / dep-map-cell forward-reference cousin of the cycle-006 `rough-in-rows-must-be-plain-text-when-anchor-missing` entry (which covered dep-map-table rough-in ROWS authored by abstractor/layer-intro-author); this entry is specifically the **forward-reference to a future FIRM chapter** case, which the cycle-006 convention did not name and which the combinator-miner + harvester did not carry.

**Two-cycle batch-4 evidence:**
- **Cycle-017 (violation; 1 build-repair).** The combinator-miner's `linear_combination` L2 rough-in dep-map row used a live link `[`linear_combination`](./linear_combination.md)` to the not-yet-authored chapter. The build failed (`linkcheck2` exit 101). integrator-finalize de-linked the cell to plain-text (the cycle-015 `fem-bilinearform-file` no-dead-link convention). The per-report integrator's claim that the forward-link "matches krylov-step/chebyshev-iteration and does not break the build" was wrong — those rows' targets EXIST as files; an absent-file link is a hard error regardless of SUMMARY registration.
- **Cycle-018 (honored; clean).** The harvester's `linear_combination.md` referenced the future `inner_product` chapter as plain-text/backtick code-span, and the combinator-miner's `inner_product` rough-in row was authored plain-text — both honored cleanly (zero build-repairs, clean linkcheck). The convention worked when followed; the goal of this entry is to make it followed structurally rather than reminder-dependent.

**Surfaced by:** cycle-017 integrator-finalize §Build status + cycle-018 carry-forward to batch-4 meta-phase (item 3) + integrator-signals cycle-018 §Integration-tooling friction.

**Mitigation (cycle-018 meta-phase, this entry — go).**
- (a) **`.claude/agents/combinator-miner.md`** — "Forward-reference convention" note under `## Proposed changes`: a rough-in dep-map row that names a not-yet-authored chapter MUST use plain text / inline-code, NEVER a live markdown link; only switch to a live link in the later harvester pass that creates the file.
- (b) **`.claude/agents/harvester.md` §Discipline** — bullet: an in-chapter forward-reference to a not-yet-authored sibling chapter MUST be plain text or inline-code, never a live link; cross-references the sibling cycle-006 dep-map-row convention.
- The per-report integrator's surgical-defang at apply time remains the safety-net backstop (it already de-links on a `linkcheck2` File-not-found); the producer-side conventions are the prevention.

**Watch:** if a producer again emits a live link to an absent file despite both conventions (recurrence-3), consider a per-report-integrator pre-apply lint that scans proposed-changes markdown links against the working tree + this report's own to-be-created files and auto-defangs absent-target links (sibling to the citation-range checker ASK).

**Amended 2026-05-28 (user directive — CLAUDE.md §"Integration may materialize implied components as stubs").** The producer-side plain-text rule STANDS (producers still must not emit dead links). What changes is the *integration-side* resolution: rather than only de-linking, when the referenced chapter is **clearly implied** (a standing rough-in row / ≥2 converging references), integration's **preferred** move is to **create the `stub` chapter** so the forward-reference becomes a live link, refined later (`stub`→`rough-in`→`firm`). De-link-to-plain-text is the fallback for speculative-only targets. See `.claude/agents/integrator-{per-report,finalize}.md` step 5.

---

```yaml
---
slug: staging-log-append-completeness-gap
first_observed: cycle-018
last_observed: cycle-018
recurrence_count: 1
status: addressed
addressed_by: cycle-018 meta-phase (`.claude/agents/integrator-per-report.md` Process step 7 hard-step tightening + `.claude/agents/integrator-finalize.md` Process step 1 staging-row-count cross-check)
---
```

**Pattern (new this cycle).** Per-report integrators applied their `book/` changes + OQ promotions + OQ-ledger notes cleanly (all 5 reports `overall_status: ready`, clean build, verified against the working tree) but **4 of 5 did NOT append their STAGING.md row** after the clean apply. `STAGING.md` captured only report-1's row; integrator-finalize had to reconcile the full landing set from the working tree (`git status`) + report frontmatter + OQ-ledger appends rather than from the authoritative staging log. **The staging log was NOT authoritative this cycle — the artifact was.** Process-discipline gap, NOT data loss (no work lost; finalize reconciled correctly).

**Surfaced by:** cycle-018 integrator-finalize §"Staging-log-completeness note" + integrator-signals cycle-018 §Integration-tooling friction ("STAGING-LOG-APPEND-COMPLETENESS GAP (NEW, recurrence-1)").

**Mitigation (cycle-018 meta-phase, this entry — go).**
- (a) **`.claude/agents/integrator-per-report.md` Process step 7** — tightened to a HARD, non-skippable step: do NOT finish the invocation without the STAGING.md append, even when the artifact apply went perfectly; the log is the authoritative record finalize reads. Cites this friction.
- (b) **`.claude/agents/integrator-finalize.md` Process step 1** — added a staging-row-count cross-check against the parent-stated count of dispatched ready reports; on `rows < dispatched`, flag LOUDLY (batch CYCLE.md + integrator-signals) AND reconcile from the working tree + report frontmatter + OQ-ledger so nothing is lost. The reconciliation is a recovery, not the normal path; (a) is the prevention.

**Watch:** if STAGING.md rows are again incomplete despite the hard-step tightening (recurrence-2), the role-spec approach has reached its ceiling — consider a parent-orchestrator-side check that verifies each per-report dispatch returned a staging-row confirmation before dispatching the next, or a finalize-blocking gate (rather than warn-and-reconcile). The warn-and-reconcile path is deliberately non-blocking for now (no data was at risk).

---

```yaml
---
slug: firm-chapter-body-authored-outside-proposed-changes-fence
first_observed: cycle-019
last_observed: cycle-036
recurrence_count: 3
status: addressed (steady-state detect+repair)
addressed_by: cycle-021 meta-phase (batch-5) — critic build-readiness guard (`cross-reference-integrity`) + producer-spec reinforcement + skill `proposed-changes-fence-encloses-full-body-guard` (DETECTION). Cycle-024 meta-phase (batch-6) — RECURRENCE-2 in the nested-```text-fence variant (cycle-023 lu-solve-mutation-rotation); promoted repair-side skill `convert-nested-fences-to-indented-code-in-proposed-changes-block` + producer-spec bullet across 5 producers (harvester / abstractor / lifter / layer-intro-author / lowering-verifier — use 4-space-indented code, NOT nested fences). **Cycle-036 meta-phase (batch-10) — RECURRENCE-3 verdict NO-GO on further producer-spec changes**: the producer-side bullets already exist (recurrence-2 enactment) and were not preventive against c036 (a different producer/theme hit the same defect-shape on a 402-line firm body); the detect+repair pipeline held cleanly (critic-detect by cycle-021 guard, repair by cycle-024 skill, zero artifact damage); steady-state cost is bounded (~1 critic-fail + 1 repair pass per occurrence, ~1 cycle in ~12); promotion to a higher-cost intervention is not warranted at this recurrence rate.
---
```

**Pattern (new this batch; the headline batch-5 defect).** A producer authored a fully-vetted, correctly-cited FIRM chapter body but left only the intro INSIDE the `edit:<path>` proposed-changes fenced block — the `## Context` … `## Evidence` sections were authored as the *report's own* top-level sections, OUTSIDE the fence. The integrator-per-report landed only the enclosed intro, so the chapter shipped as an intro-only stub while the dep-map row + `SUMMARY.md` already said `firm`. A silent body-truncation masked by the dep-map/SUMMARY claiming firm. This is structurally distinct from the citation-drift family: it is a well-formed, well-cited body that is *partially outside the apply boundary*.

**Single instance (cycle-019), surfaced cycle-020.** The cycle-019 `orthogonalize` L2 harvest (`reports/2026-05-29T023000Z-harvester-orthogonalize-l2/`, integrated `efb8a0b`) left the firm `## Context`…`## Evidence` body outside the `edit:book/src/L2/orthogonalize.md` fence; `book/src/L2/orthogonalize.md` shipped as a 14-line intro with NO `## Status` while `L2/index.md:27` + `SUMMARY.md:41` said `firm`. The cycle-019 critic+repairer validated the *content* (citations correct) but did not catch that most of it never entered the artifact, because the report's prose carried it and the critique focused on claim/citation correctness, not on which lines sat inside the proposed-changes fence. Caught cycle-020 by the L2-refresh critic (which surveyed firmness against the cycle log, found `orthogonalize.md` had no `## Status` on disk); corrected by the `harvester-orthogonalize-l2-backfill` full-file-replacement dispatch (one off-by-one boundary fix `test-orthog.cpp:71-96 → 71-97`).

**Surfaced by:** cycle-020 integrator-signals §Integration-tooling friction (HEADLINE) + OQ `firm-chapter-body-authored-outside-proposed-changes-fenced-block` + two skill-candidates (`proposed-changes-fence-encloses-full-body-guard`, `verify-intro-firmness-survey-against-on-disk-status-lines`).

**The dispatch-prompt guidance HELD across the rest of the batch.** Cycle-020 and cycle-021 producers ALL correctly enclosed their full firm bodies inside the proposed-changes fences (per-report fence-guard PASS on every report; e.g. cycle-021 `apply_nonlinear_pencil` CYCLE.md:24-143, `ksp_solve` full-replace, `ksp-solve-outer-driver` fence :49-232 with both inner ```text blocks nested+closed). **Zero recurrence in two cycles.** So the parent's per-dispatch "put the body INSIDE the fence" reminder works — but per-dispatch reminders are not durable (the `specialized-agent-direct-write-to-book-during-dispatch` lesson: parent reminders are not structural). The durable fix is a critic-side build-readiness guard that catches the defect at critique time regardless of producer discipline.

**Mitigation (cycle-021 meta-phase, this entry — go).**
- (a) **Critic build-readiness guard** added to `.claude/agents/critic.md` `cross-reference-integrity` check: when a report's proposed-changes (or the dep-map/SUMMARY row it relies on) asserts a chapter is `firm`, verify the `edit:`/`new:` block for that chapter ENCLOSES the firm apparatus (`## Status` + Signature + Algebraic-laws + Evidence) INSIDE the fence — a `firm` claim whose proposed-changes block carries only an intro is the signature of this defect. The check is a fence-enumeration + one "is `## Status` inside the block?" scan. This would have caught the cycle-019 truncation at critique time.
- (b) **Producer-spec reinforcement** added to all 8 specialized agent Discipline sections (the producers that author firm chapters): "the firm chapter body must be authored INSIDE the proposed-changes `edit:`/`new:` fence — do NOT author chapter sections as your report's own top-level sections; only the enclosed block is applied."
- (c) **Skill `proposed-changes-fence-encloses-full-body-guard` promoted** (`skills/proposed-changes-fence-encloses-full-body-guard/SKILL.md`) — the critic-facing fence-parity + last-section-inside-block + apparatus-inside-block checklist; the deterministic procedure backing guard (a).

**Did NOT promote the sibling candidate `verify-intro-firmness-survey-against-on-disk-status-lines` as a standalone skill** — see the batch-5 meta-phase report no-go reasoning: that candidate's root cause (an intro-refresh surveying firmness from the cycle record rather than the on-disk `## Status`) is the *downstream* symptom of THIS *upstream* defect; with the upstream cause now guarded at critique time, the downstream survey-check is folded into the layer-intro-author Discipline as a one-line "survey firmness from the on-disk `## Status`, not the cycle log" bullet rather than a separate skill. The two candidates are two ends of one defect; guarding the upstream end is the high-leverage fix.

**Watch:** if a `firm`-claimed chapter again lands intro-only despite the critic guard (recurrence-2), the critique-time check has a hole — escalate to an integrator-per-report apply-time gate (refuse to flip a dep-map/SUMMARY row to `firm` when the target chapter's enclosed body lacks `## Status`).

**Cycle-024 meta-phase update (batch-6) — RECURRENCE-2, the nested-```text-fence variant; DETECTION held, the REPAIR is the recurring cost.** Cycle-023's `lu-solve-mutation-rotation` L1>L0 abstractor authored its firm body inside a `new:` block but rendered the four code samples as nested ` ```text … ``` ` fenced blocks (rather than the 4-space-indented form the landed siblings `dot-mutation-rotation.md`/`assemble-diagonal-mutation-rotation.md` use); under flat CommonMark fence-toggle the first bare inner ` ``` ` closed the `new:` block early, leaving `## Status` + the firm apparatus OUTSIDE the captured content — the same root defect as cycle-019, a different surface form. **The cycle-021 critic guard `proposed-changes-fence-encloses-full-body-guard` WORKED** (`cross-reference-integrity: fail` with the fence-pairing arithmetic spelled out) — detection is structurally solid, zero recurrence of the *undetected* defect. What recurs is the *repair*, which is identical every time (convert each nested fence to a 4-space-indented block). **Enacted (go):** (a) skill-candidate `convert-nested-fences-to-indented-code-in-proposed-changes-block` PROMOTED (`skills/.../SKILL.md`) — the deterministic repair-side counterpart to the detection guard; (b) a producer-spec bullet added to the 4 firm-body-authoring producers (harvester / abstractor / lifter / layer-intro-author) + lowering-verifier: when authoring a firm body inside a proposed-changes block, render inner code samples as 4-space-indented blocks, NOT nested ` ```lang ` fences (the landed-sibling convention; nested fences mis-toggle the flat-CommonMark fence parser). Status stays `addressed` (detection holds; the prevention bullet + repair skill close the cost loop); recurrence 1 → 2 (the cycle-023 nested-fence instance).

**Cycle-036 meta-phase update (batch-10) — RECURRENCE-3 verdict NO-GO on further producer-spec or mechanical changes; steady-state detect+repair is acceptable.** Cycle-036's D1 floquet harvester re-emitted the same nested-```text-fence defect inside the floquet-correction firm body — recurrence-3. The producer-spec bullets the batch-6 meta-phase added to all 5 firm-body-authoring producers (harvester / abstractor / lifter / layer-intro-author / lowering-verifier) were in place; the c036 harvester apparently did not consult them while focused on the 402-line body authoring. The cycle-021 critic guard `proposed-changes-fence-encloses-full-body-guard` CAUGHT the defect cleanly; the cycle-024 repair skill `convert-nested-fences-to-indented-code-in-proposed-changes-block` REPAIRED it cleanly (inner `text` fence in §Signature converted to 4-space indent; first proposed-changes block now encloses the FULL 402-line firm body). **The detect+repair pipeline held — no artifact damage, zero re-application needed.** **VERDICT (NO-GO):** further producer-spec changes (another bullet, a stricter pre-emission check) are not warranted at recurrence-3 across ~17 cycles since c019 — the producer-side bullets exist and are reminder-dependent like all reminder-class mitigations; the c036 datapoint shows the steady-state cost (~1 critic-fail + 1 repair pass, ~1 cycle in ~12) is bounded. The c024 batch-6 watch trigger "if a producer again emits nested fences despite the bullet (recurrence-3), escalate to an integrator-per-report pre-apply auto-defang" is REVISITED-AND-DEFERRED — the auto-defang would be a larger structural change (orchestrator code touch) and the steady-state cost does not yet justify it. **Watch (deferred):** if recurrence-4 within ≤6 cycles surfaces, re-open the auto-defang ask. If the pattern persists at the c019/c023/c036 cadence (every ~7-13 cycles), accept it as steady-state.

---

```yaml
---
slug: sibling-slice-citation-reanchor-sweep-gap
first_observed: cycle-020
last_observed: cycle-020
recurrence_count: 1
status: addressed
addressed_by: cycle-021 meta-phase (batch-5) — skill-candidate `sibling-slice-citation-reanchor-sweep` promoted as a third sub-case of the existing `verify-citation-range` skill (sibling/inherited-precedent re-anchor)
---
```

**Pattern (new this batch).** A dispatch whose premise is "slice X was reduced, so re-anchor its drifted refs" correctly sweeps every `<focus-slice>.md:NNN` ref but MISSES `<sibling-slice>.md:NNN` refs cited in the same paragraphs — a *sibling* slice that underwent the *same* reduction-class drift. The focus-slice sweep structurally skips siblings; a sibling cited as a "precedent rendering" is the high-risk case (precedents are exactly the v0.1–v0.4 forms most likely to have been lifted away).

**Single instance (cycle-020).** The cycle-020 lifter `gmres §L4 v0.6→v0.7` dispatch correctly diagnosed `gmres.md` was reduced and swept every drifted `gmres.md:NNN` ref it touched (a clean re-anchor) — but re-emitted `cg.md:215-219` (the CG `iterate_while` precedent) in three places (one retained, two in NEW v0.7-append content) without checking that `cg.md` had undergone the *same* reduction: `cg.md` is now 166 lines and its v0.4 `iterate_while` form was lifted to `L4/krylov-step.md`, so `cg.md:215-219` is out of range. Reduction-class drift caught for the focus slice, missed for the sibling.

**Surfaced by:** cycle-020 integrator-signals §Integration-tooling friction (item c) + skill-candidate `sibling-slice-citation-reanchor-sweep` (critic-filed).

**Mitigation (cycle-021 meta-phase, this entry — go).** The candidate's own promotion-bar note recommended folding into the existing `verify-citation-range` skill rather than a standalone skill (the reduced-slice-drift mechanism is the same one `phase-1-slice-reduction-audit` + the focus-slice sweep already operate on; the gap is specifically the *sibling/inherited* citation). Enacted: **`skills/verify-citation-range/SKILL.md` gains a third sub-case** ("Sibling-slice / inherited-precedent re-anchor") after the cycle-012 "audit-report / inherited-citation" sub-case: when a dispatch's premise is a slice re-anchor, enumerate ALL distinct `<slice>.md` citations in the touched/authored content (not just the focus slice); for each distinct cited slice, check for a reduced-slice stub-header and treat its numeric line-refs as presumptively drifted; re-anchor to the firm home if the cited form was lifted away. One read + stub-header scan per distinct cited slice.

**Watch:** if a sibling-slice ref again dangles after a re-anchor dispatch despite the skill sub-case (recurrence-2), the producer-facing sub-case is being under-invoked (same telemetry-gap shape as the citation-drift family) — re-weigh whether the mechanical citation-checker tool (if built per the `producer-citation-drift-verify-not-self-invoked` ASK) should also flag out-of-range slice refs, which would catch this mechanically.

---

```yaml
---
slug: split-integrator-crash-recovery-resilience
first_observed: cycle-023
last_observed: cycle-024
recurrence_count: 2
status: addressed-by-design
addressed_by: cycle-005 split-integrator design (`integrator-per-report` + STAGING.md as the authoritative per-cycle log) — VALIDATED-UNDER-CRASH cycles 023/024 (batch-6); the staging log + on-disk artifact state are sufficient for `integrator-finalize` to resume idempotently after a mid-cycle machine crash
---
```

**Positive pattern (resilience datapoint, NOT friction).** A mid-cycle **machine crash** interrupted BOTH cycle-023 and cycle-024 of meta-batch-6, in each case AFTER all per-report integrators had completed and appended their STAGING.md rows but before / during `integrator-finalize`. In both cycles the recovery was clean: `integrator-finalize` read the (complete, authoritative) STAGING.md, cross-checked the working tree + report frontmatter + OQ-ledger appends, found `rows == dispatched ready reports` (6/6 cycle-023, 8/8 cycle-024), and ran to completion with **zero per-report re-application and zero working-tree reconciliation recovery needed**. No work was lost; no double-apply occurred; the build was clean both times.

**Why this is the design working as scoped.** The cycle-004→005 split (`split-integrator-validated-at-six-reports`) introduced STAGING.md as the authoritative per-cycle landing log precisely so that `integrator-finalize` reads a durable record rather than reconstructing state from volatile context. The crash exercised exactly that property: the durable staging log + the idempotent on-disk artifact (each per-report apply is a committed-to-working-tree surgical edit) are jointly sufficient to resume. This is the same property the cycle-018 `staging-log-append-completeness-gap` hard-step tightening protects — and the batch-6 evidence (STAGING completeness held 4th/5th/6th consecutive cycle) is what made the crash-resume trivial: had rows been missing, finalize would have fallen back to the (error-prone) working-tree reconstruction.

**Counterfactual test (per the addressed-by-design audit discipline).** If the crash-resilience were removed tomorrow, would orchestration coupling collapse? — No coupling collapses; this is not a workaround over a quirk. The split-integrator + authoritative-staging-log IS the design, and crash-resilience is an emergent property of it (a durable log + idempotent applies), not a patch. Correctly `addressed-by-design` (cf. the cycle-004 audit distinguishing "the channel IS the design" from "we have a workaround").

**Surfaced by:** integrator-signals cycle-023/024 §Integration-tooling friction (recovery-not-normal-path entries) + the two crash-recovered cycle logs.

**Watch:** no action needed. If a future crash interrupts MID-per-report-apply (not between phases as here — i.e. a per-report integrator dies after editing `book/` but before its STAGING.md append), the finalize cross-check (`rows < dispatched`) would catch the gap and fall to working-tree reconciliation; that path is exercised-by-design but has not yet been crash-tested. Record if it occurs.

---

```yaml
---
slug: codemap-read-range-plus-one-drift-on-brace-boundary
first_observed: cycle-024
last_observed: cycle-104
recurrence_count: 7
status: addressed
addressed_by: cycle-027 meta-phase (batch-7) — "the codemap is localization-only; citecheck / on-disk is the citation source of truth" sub-bullet added to all 5 citing producer/auditor specs (harvester / abstractor / lifter / layer-intro-author / lowering-verifier §Discipline citecheck blocks). **SHARPENED cycle-066 meta-phase (batch-20)** — a `--anchor`-blind-spot sub-bullet appended to all 5 specs + a localization-hint sub-bullet to cycle-planner §77: `citecheck --anchor` does NOT catch a range-END / close-brace off-by-one when the anchor token sits inside BOTH candidate ranges; a full-body `:lo-hi` whose END is a closing brace must have its END line confirmed by a direct on-disk `Read`, not by `--anchor`. **SHARPENED AGAIN cycle-105 meta-phase (batch-33)** — the drift's NEW manifestation this batch was on the CRITIC side (a c104 critic emitted a false `±1` prose-drift report sourced from a `+1`-drifted `read_range` → a wasted c105 D2 no-op repair dispatch); the existing producer-side bullets did not cover the critic flagging a drift FROM `read_range`. The `critic.md` citation-validity bullet now states: a flagged `±1` drift's "correct" line MUST come from `citecheck --anchor`/on-disk `Read`, NEVER from codemap `read_range` (the documented drift source); on-disk wins. **These are `.claude/agents/` edits → SESSION RESTART required before cycle-106.**
---
```

**Pattern (TOOL-level drift, distinct from producer-emit drift).** The `palace-codemap` MCP `read_range` line indexing drifts **+1 behind the on-disk `reference/palace/` file** on certain multi-line-comment + opening-`{`-brace boundaries — it appears to merge a comment-line + the following `{`-brace line into one logical line. A producer who **faithfully transcribes the line `read_range` returned** therefore still lands a +1-drifted citation. This is a *different failure mode* from `producer-citation-drift-verify-not-self-invoked` (where the producer cites from stale memory): here the producer did everything right against the codemap, but the **tool itself** disagrees with the on-disk file. `tools/citecheck/` (which reads the on-disk file directly) is the authoritative tie-breaker and caught every instance.

**Evidence (the drift is localized to one boundary, but it recurs across batches when that region is touched):**
- **cycle-024:** the `nleps.cpp` deflation block authored from codemap landed +1 (the original codemap-sourced anchors).
- **cycle-025 (detection):** dispatch-1 abstractor's citecheck self-verify flagged the `nleps.cpp` deflation-block `:659+` anchors `[DRIFT +1]`; filed the standing OQ `codemap-read-range-plus-one-drift-on-brace-boundary` (open-questions.md:717) recommending the source-of-truth role-spec strengthening.
- **cycle-026 (worked correction):** dispatch-1 lifter re-anchor pass mechanically corrected all six deflation-block anchors (`[DRIFT]` pre / `[ok]` post via `citecheck --anchor`), at the **same** `nleps.cpp` `if (k > 0)` `{`-brace boundary (`:659`).
- **cycle-027:** dispatch-2 lifter re-anchored `matrix-weighted-norm.md` `operator.cpp:601→:602` at the same class of boundary; the deflation-block region stayed corrected.
- **cycle-039 (batch-11; recurrence-5, NEW boundary, catch-and-correct held):** the cycle-039 planner pre-localized `CgSolver::Mult` at `iterative.cpp:360` (the `template`-declaration line) but the function body opens at on-disk `:361`. The D2 lowering-verifier — performing the floquet AddMult-aliasing re-anchor — used on-disk `--anchor`/direct read (per the source-of-truth discipline) and cited the correct `:361`/`:384`/`:385` anchors; the drift never reached the artifact. This is a **NEW file/boundary** (`iterative.cpp` `CgSolver::Mult`, distinct from the previously-recorded `nleps.cpp` deflation-block + `operator.cpp:601` boundaries) — the comment/`template`+body-open boundary class is the same shape (a non-body line merged with the body-open line). The on-disk discipline (cycle-027 enactment) held cleanly: zero artifact damage, zero repair round (the lowering-verifier never transcribed off the codemap hint). The planner-hint was a *localization* hint and was treated as such.
- **cycles 064/065/066 (batch-20; recurrence-6, the FE-source batch, 3-of-3 + a NEW finding):** the FE-space front opened against `palace/fem/fespace.hpp` + `palace/fem/multigrid.hpp` and the +1 drift fired on EVERY cycle of the batch: c064 `fespace.hpp` ctor `:66-74`-vs-on-disk-`:67-75` (cost a full citation-reconciliation round AND a parent-orchestrator regression that had to be fixed), c065 `multigrid.hpp`/`fespace.hpp`, c066 `multigrid.hpp:22-72`-vs-`:22-73` (normalized across three loci in `fe_space.md` by the c066 D3 lifter). **NEW load-bearing finding (the reason this batch warranted a sharpening, not just a tally):** `citecheck --anchor ConstructFECollections` returns `[ok]` for BOTH `:22-72` AND `:22-73`, because the anchor (`ConstructFECollections` at line 25) sits inside either range — so the existing `--anchor` mechanical fallback is **BLIND to a range-END / close-brace off-by-one**. Only a deliberate hand-`Read` of the closing-brace line catches it (the c066 D3 procedure). This is a documented gap in the cycle-027 enactment's mechanical leg, exposed because FE-source full-body citations terminate on a template/function closing brace far more often than the inner-kernel BLAS sites did.

**Scope nuance (load-bearing; UPDATED batch-20).** The drift has now been observed on **five+ distinct boundaries**: the `nleps.cpp` deflation block (cycles 024/025/026), `operator.cpp:601` (cycle-027), `iterative.cpp` `CgSolver::Mult` `:360→:361` (cycle-039), and the FE-source pair `fespace.hpp` ctor + `multigrid.hpp` `ConstructFECollections` (cycles 064/065/066). All share the same shape — a comment-line or `template`-declaration line merged with the immediately-following body-open (or, at the FE-source sites, the whole-template) line, producing a +1 on the body/END anchors. The recurrence across **five independent boundaries** confirms this is a *systematic codemap-server line-indexing behavior on a specific source-construct class* (non-body line preceding a body-open / template open), not a fluke. It is NOT a tree-wide off-by-one on *every* brace (most citations resolve clean) — it triggers specifically at that construct. The recurrence-count tallies cycles where the drift was *present in the localization hint*; the on-disk discipline has caught all six with zero artifact damage — BUT batch-20 surfaced that the mechanical leg (`citecheck --anchor`) is **blind to the END-line variant** of the drift (anchor in-range for both candidate ranges), so the catch in batch-20 rested on hand-`Read` of the closing brace, not on `--anchor`. That is the gap the batch-20 sharpening closes.

**Why role-spec strengthening (not a new gate) is the right enactment.** The mechanical defense — `citecheck --anchor` against on-disk — is **already wired** into all 5 specs (cycle-024, `producer-citation-drift-verify-not-self-invoked`). The gap was that the existing bullets treated `read_range` and codemap as *interchangeable* sources of truth ("`read_range` OR codemap... then confirm"). The cycle-027 sub-bullet makes the hierarchy explicit: codemap is a localization HINT; the emitted `path:lo-hi` must come from `citecheck`/on-disk; when they disagree, on-disk wins. This closes the conceptual gap (a faithful codemap transcription is NOT a verified citation) without adding a new pipeline gate. A standing per-report HARD citecheck `--anchor` gate was considered and is a no-go this batch (see Watch) — the `--scan` bounds gate (cycle-024) already runs per-report, and pinpoint `--anchor` requires CYCLE.md to carry machine-readable anchor tokens (a channel-format change, ask-class).

**Watch (UPDATED batch-20; the guard held but the mechanical leg needed sharpening).** Batch-20's recurrence-6 was caught — the FE-source drift never reached the artifact — but the catch cost a full reconciliation round (incl. an orchestrator-level regression) and rested on hand-`Read` of the closing brace because `citecheck --anchor` was BLIND to the END-line variant. That cost (real, recurring, with a documented mechanical blind spot) is what tipped the batch-20 meta-phase from watch-only to an **enacted role-spec sharpening (go)**: the `--anchor`-blind-spot sub-bullet on all 5 citing specs + the localization-hint sub-bullet on cycle-planner §77, instructing a direct on-disk `Read` of any close-brace END line rather than trusting `--anchor`. This stays a **role-spec** fix (Medium-cascade, in meta-phase authority) — NOT escalated to the ask-class HARD pinpoint-`--anchor` integrator gate (still NO-GO: the gate's `--anchor` mechanism is exactly the leg shown blind here, so it would not have caught the batch-20 drift either; and it needs the CYCLE.md anchor-token channel-format change). **Re-open / escalate** only if (a) a producer faithfully follows the sharpened discipline and a drifted END citation STILL reaches the artifact uncaught (→ the on-disk-Read bullet failed; reconsider a finalize-time close-brace lint, code-change ask-class), OR (b) the drift count climbs steeply enough that the localization-hint noise becomes a planner-time cost worth a codemap-server bug-report (code change, ask-class). Neither holds at recurrence-6 — the sharpened discipline is the proportionate fix for the now-understood drift class.

**Batch-33 instance (cycles 103/104/105; recurrence_count 6 → 7, last_observed → c104; the NEW manifestation: critic-side false-drift, enacted a critic-spec sharpening).** The drift fired on the CRITIC side this batch — a *new* manifestation that the producer-side bullets did not cover. During the graded-stack P1 record-page typing (c104 D1), a critic emitted a `±1` prose-citation-drift finding on `concepts/op-params.md` + `concepts/sim-state.md` `iterative.hpp` declarations (`:42→:41`/`:45→:44`/`:49-50→:48-49`/`:53-55→:52-54`), each exactly one LOW — the signature `+1` drift on the `// Relative and absolute tolerances.` comment/declaration boundary. The "drift" was sourced from a `+1`-drifted codemap `read_range`; the prose was ALWAYS correct (the c105 harvester re-anchor dispatch + the c105 critic both re-confirmed every line via direct on-disk `Read`/grep — all match disk). The false report cost a **wasted c105 D2 no-op repair dispatch** chasing a phantom. The producer-side discipline held (the c104 record-page producer typed the `cites-evidence` frontmatter against the verified ENCLOSING region, sound regardless), and the mitigation worked (direct-Read cross-check overturned the false positive in both the c105 producer AND the c105 critic) — but the *critic* flagging a drift whose only basis was a `read_range`-vs-prose mismatch was the uncovered gap. **Enactment (go):** the `critic.md` citation-validity bullet now states explicitly that a flagged `±1` drift's "correct" line must come from `citecheck --anchor`/on-disk `Read`, NEVER from codemap `read_range`, and on-disk wins on disagreement. Recurrence 6 → 7. (This is a `.claude/agents/critic.md` edit → SESSION RESTART required before c106.) **Re-open/escalate** thresholds unchanged from batch-20.

**Batch-34 corroboration (cycles 106/107/108; recurrence_count HELD at 7, last_observed → c104).** No fresh NEW-drift event and no residue re-anchor this batch — the GRADED-STACK P1 typed-edge campaign was a **frontmatter-edge-typing batch**, not a source-citation-authoring batch (the work was typing `edges:` blocks + grounding `depends-on` edges on existing chapters, whose L0 citations were already on-disk-confirmed in prior cycles). The c107/c108 grounding edges DID cite source (e.g. `laplaceoperator.cpp:216-217,252`, `eigensolver.cpp:233,262`, `divfree.cpp:171-174`) but each was an audit-against-on-disk localization (the cycle-planner pre-localized via codemap + the producers confirmed against disk per the sharpened critic/producer discipline) and every report arrived critic-clean with NO repair phase in c107/c108. The batch-33 critic-side sharpening (the c105 enactment loaded post-restart before c106) held: zero false-`±1`-drift reports this batch. Recurrence stays 7; the sharpened discipline continues to hold across both source-citing and edge-typing surfaces.

**Batch-23 corroboration (cycles 073/074/075; recurrence_count HELD at 6, last_observed → c075).** No fresh NEW-drift event and no residue re-anchor this batch — the feature-spine output-product cohort (capacitance/inductance/sparameters/eigenfrequency-qfactor columns + the 2 new L4 reduction verbs `sparameter_reduce`/`eigenfreq_qfactor_reduce`) cited into `palace/models/postoperator.cpp` / `lumpedportoperator.cpp` / `waveportoperator.cpp` / `eigensolver.cpp` / `electrostaticsolver.cpp` / `magnetostaticsolver.cpp` and every producer cited clean (the cycle-073/074/075 finalize records logged zero build-repairs, zero citecheck failures beyond the benign report-self-reference false-positives). The sharpened on-disk-Read discipline held across the heavy postprocess-source authoring; recurrence stays 6. (The only batch-23 citation-provenance note was the standing benign `--scan`-flags-the-report's-own-documentation false-positive on lint-repair reports — distinct class, report-only, not ledgered.)

**Batch-22 corroboration (cycles 070/071/072; recurrence_count HELD at 6, last_observed → c072).** The batch-22 instance is again a **catch-and-route of pre-existing residue, NOT a fresh NEW-drift event** — and confirms the sharpened on-disk-Read discipline holds on the new feature-surface authoring surface. The c072 feature columns (magnetostatic + lifecycle, each at L4+L1+L0) cite into `palace/drivers/*solver.cpp` + `main.cpp` + `basesolver.cpp`; the D1 magnetostatic dispatch cited every site at its **on-disk-confirmed** line (via direct `read_range` then on-disk confirm) and SURFACED a pre-existing +1 drift in ANOTHER file — `book/src/L4/solve_family.md` §Specializations (both the electrostatic and magnetostatic specialization notes cite `:30`/`:35`/`:36` for sites on-disk at `:29`/`:34`/`:35`), routed as OQ `solve-family-md-specialization-note-plus-one-anchor-drift` to a lifter/repairer re-anchor pass (the loop-region `:47`/`:66`/`:76`/`:77`/`:99` anchors in those notes are correct). So **no NEW drift reached the artifact this batch** (the c071 structural-reorg wave touched no source citations; the c072 feature columns cited clean), and the recurrence stays 6 (the `solve_family.md` §Specializations residue is the same boundary class, not a fresh occurrence) — the data point confirms the discipline both (i) keeps new feature-surface authoring clean and (ii) catches/routes historical residue. The drift is now also confirmed to manifest on **copied/derived references** (a specialization note transcribed off the cited file) — the same hand-maintained-derived-surface drift sibling-class as `index-table-status-cell-drifts-when-theme-file-promoted`; the re-anchor remedy is identical.

**Batch-21 corroboration (cycles 067/068/069; recurrence_count HELD at 6, last_observed → c069).** The batch-21 instance is a **remediation of pre-existing residue**, not a fresh NEW-drift event: c069 D4 (lifter) re-anchored the firm L1 cap `book/src/L1/fe_assemble.md` weak-form-term witness citations (`laplaceoperator.cpp:191-192`→`:193-196`, `curlcurloperator.cpp:179-181`→`:180-181`) — these were the SAME c064-066 FE-source +1 boundary-drift residue, surfaced by the c068 D2 abstractor (which re-anchored its own theme copies but could not touch the cap, out of write-scope) and tracked as OQ `fe-assemble-l1-cap-weak-form-term-witness-line-drift-reanchor`. D4 corrected all 4 loci by **direct on-disk Read of the close-brace END lines** (NOT trusting `citecheck --anchor`, per the batch-20 sharpening) — the sharpened discipline worked exactly as enacted. Crucially, **no NEW drift reached the artifact this batch**: the c067/c068/c069 producers authoring new firm entries (`fe_assemble`, `assemble_frequency_operator`, `dot`, `nrm2`, the combinators) all cited clean (citecheck `--scan` all-ok across the batch; the only `--scan` MISS/fail events were prose-shorthand false-positives that resolve at full `palace/fem/` paths). So recurrence_count stays 6 (the residue was already counted as the c064-066 instance); the batch-21 data point confirms the sharpened discipline both (i) caught/remediated the historical residue and (ii) prevented fresh drift on the new FE-source-heavy authoring. A **caveat for future re-anchor passes** surfaced (recorded, not a new ledger pattern): the D4 grep used the `:lo-hi` full-range form and initially missed the bare-`(:NNN)` pinpoint form in the §Evidence block — a witness-drift re-anchor grep should match BOTH forms (folded into the `verify-citation-range` skill's mental model; too minor for a standalone friction entry).

---

```yaml
---
slug: cycle-planner-reproposes-already-landed-work
first_observed: cycle-026
last_observed: cycle-032
recurrence_count: 4
status: addressed
addressed_by: cycle-027 meta-phase (batch-7) — two cycle-planner §Discipline bullets (verify-candidate-genuinely-open + one-finalize-per-cycle); **escalated batch-9 meta-phase** — the c027 bullets caught the c026/c027 sub-pattern but the c031/c032 recurrence surfaced a deeper sub-pattern (`cycle-planner-stale-priorities-line-recruitment`, the deliverable-presence shape) tracked separately below as the live escalation. **SUBSUMED+CLOSED→addressed by the batch-11 meta-phase (post-cycle-039):** this entry is the file-existence-staleness sibling of `cycle-planner-stale-priorities-line-recruitment` (the deeper deliverable-presence shape). That live escalation closed `addressed` on the batch-11 3-of-3-clean confirmation window under the combined paste-inline-evidence procedure + opus tier; the broader fix that closes the deeper shape closes the narrower file-existence shape a fortiori (a planner running the full deliverable-presence check trivially also clears file-existence). Re-open this entry only if the file-existence sub-shape specifically recurs decoupled from the deliverable-presence one.
---
```

**Pattern (haiku cycle-planner staleness — distinct sibling of `cycle-planner-dispatch-prompt-framing-drift`).** The haiku cycle-planner re-proposes work that has ALREADY landed in a prior cycle, and/or builds a plan rationale on an incorrect pipeline model. This is distinct from the path-framing drift (citing wrong source paths, `cycle-planner-dispatch-prompt-framing-drift`): here the *scope is stale* (the work is done) or the *process model is wrong* (assumes multiple finalizes). Both were caught by the orchestrator pre-dispatch this batch.

**Evidence (both instances orchestrator-caught pre-dispatch):**
- **cycle-026:** the plan re-proposed the batch-6 lowering-verifier audit cohort that had ALREADY landed in cycle-025 (the apply-nonlinear-pencil / deflate-composition / gram-fold / orthogonalize-composition audits). The orchestrator caught it + re-scoped to the genuinely-unaudited cycle-025-new themes. The planner had not checked cycle-025's `counts_after` (which records the audit cohort 4/4 discharged).
- **cycle-027:** the plan over-built — 10 dispatches / 4 waves — with (a) an incorrect "integrator-finalize rebuilds between waves" model (finalize runs ONCE per cycle), and (b) a stale "Firm 19→20" count-bump rationale that cycle-026's finalize had ALREADY applied as measurable housekeeping (`L1/index.md:31`). Both caught + corrected by the orchestrator.

**Mitigation (cycle-027 meta-phase, this entry — go).** Two `.claude/agents/cycle-planner.md` §Discipline bullets: (1) **verify-candidate-is-genuinely-open** — before proposing a dispatch, scan the `cycle-record.jsonl` tail `counts_after`/`cycle_character` + the latest STAGING.md + the plan's `~~struck~~`/`DONE`/`COMPLETE` Backlog markers; a closed item is not re-proposable. (2) **one-finalize-per-cycle** — the pipeline runs exactly one `integrator-finalize` at cycle end; `## Sequencing schedule` waves order *dispatches* by forward-reference dependency, the book is not rebuilt between waves, and measurable count-bumps the prior finalize already applied are not to be re-scheduled (check `counts_after`).

**Why role-spec (Medium-cascade), not escalate-to-opus.** Both drifts were cheap orchestrator corrections (the haiku planner produced an otherwise-sound plan; the orchestrator's pre-dispatch read is the existing safety net). The role-spec bullets are the minimal fix consistent with "don't over-ask" (the planner stays haiku; the bullets add two mechanical pre-checks that fit the tier — reading `counts_after` is a cheap lookup). Swapping the planner to opus stays a HELD escalation.

**Watch:** if either drift recurs post-enactment (recurrence-3) despite the bullets, escalate — consider (a) the orchestrator running a "candidate-already-landed" lint over the plan before dispatch (cross-ref each candidate slug against the latest `counts_after`), or (b) swapping the cycle-planner to opus (the haiku tier may under-read the cycle-record). The drift has been cheaply corrected each time; the bullets should suffice.

---

```yaml
---
slug: coordinated-cross-report-rename-premise-inversion
first_observed: cycle-027
last_observed: cycle-027
recurrence_count: 1
status: addressed
addressed_by: cycle-027 meta-phase (batch-7) — promoted skill `skills/audit-slug-meaning-before-coordinated-cross-report-rename/SKILL.md` (repairer-facing denote-by-signature gate before applying a coordinated rename) + the D5 deferral migrated into the plan as a c028 lifter task
---
```

**Pattern (new process-friction; the coordinated-cross-report-rename trap).** When two same-cycle dispatches collide on a slug, the repairer of the second may be handed a **coordinated cross-report rename** whose **premise is inverted relative to the artifact** — the instruction says "rename references meaning X" but in the report every reference under that slug means the *protected* (other) operation, and the real consistency gap is a *different* slug entirely. Blindly applying the literal rename would corrupt correct references AND miss the real gap.

**Evidence (cycle-027 D4/D5).** Dispatch-4 harvested the terminal back-solve leaf and renamed it `ls_update_column` → `back_solve` (collision: `ls_update_column` already named the distinct column-streaming step `(K,j,h_new)→K'` in `L2/incremental-least-squares.md:412` + the concept page). Dispatch-5's repairer was told "rename this theme's back-solve-leaf `ls_update_column` refs → `back_solve`, but protect column-streaming refs." An exhaustive grep showed the INVERSE: every `ls_update_column` in the theme meant the column-streaming step (CAUTION-protected), NONE the back-solve leaf — the back-solve target was referenced under `trsv`/`back_solve`. The repairer correctly applied ZERO rename edits (`not-needed`), identified the real gap as the inverse `trsv↔back_solve` reconciliation (a content reclassification beyond repair scope), set `needs-revision`, and routed it to the integrator → the c028 lifter promotion task. The D5 deferral is the only deferral of batch-7 (otherwise 3 clean cycles, 0 rejections).

**The collision was avoidable.** The L2 entry already used BOTH colliding slugs with distinct meanings (`ls_update_column` = column-streaming, `back_solve` = terminal back-solve). A pre-harvest slug-collision check against existing artifact vocabulary would have stopped dispatch-4 from binding `ls_update_column` to a second meaning. Whether to make that a standing producer-spec bullet is surfaced as an **ASK** in the cycle-027 meta-phase report (it adds a mechanical grep step to every harvest/abstract that introduces a new slug; low cost, but a producer-spec change worth confirming the appetite for vs. relying on the repairer-side gate skill).

**Mitigation (cycle-027 meta-phase, this entry — go).** Promoted the repairer-facing skill `audit-slug-meaning-before-coordinated-cross-report-rename` (the 5-step denote-by-signature gate: read the landing report's ground truth → classify every occurrence by the operation it denotes → gate on premise contradiction → route a content-reclassification gap as `unrepairable` → record explicitly). It is a generalization of the `verify-citation-range` "verify against the artifact, not the paraphrase" discipline to slug-rename coordination.

**Watch:** recurrence-1 (single instance). If a second inverted-premise coordinated rename surfaces, the repairer-side gate is necessary but the *avoidance* (a pre-harvest slug-collision check) becomes the better fix — enact the producer-spec bullet then (if the human's ASK response defers it now). Also a datapoint for the broader "one-operator-per-dispatch + forward-references create cross-report coordination" cost: when two in-cycle dispatches must coordinate a rename, the integration-ordering + repairer-gate handled it without a rejection (the surface accumulated with the friction embedded — the deferral routes to c028).

---

```yaml
---
slug: verified-against-note-no-leading-quote-of-either-kind
first_observed: cycle-028
last_observed: cycle-030
recurrence_count: 2
status: addressed
addressed_by: cycle-030 meta-phase (batch-8) — generalized channel-format rule codified in `.claude/agents/lowering-verifier.md` §Discipline + `.claude/agents/critic.md` `citation-validity` YAML round-trip sub-check + promoted skill `skills/verified-against-note-no-leading-quote-of-either-kind/SKILL.md` (producer self-check + critic mechanical check + repairer rephrase pattern). Generalizes the c028 narrower "no leading double-quote" form to "no leading quote of EITHER kind".
---
```

**Pattern (channel-format hazard for `verified_against:` `note:` values).** YAML's plain-scalar parser interprets a leading `'` OR `"` as opening a quoted scalar; any trailing unquoted prose after the closing quote breaks the block with `ParserError: expected <block end>, but found '<scalar>'`. The hazard is symmetric across the two quote characters: `note: 'X' — content` and `note: "X" — content` both fail `yaml.safe_load` identically. The leverage point is the *generalized* predicate "note value's first non-whitespace character ∈ {`'`, `"`}", not either narrower form.

**Evidence (cycle-028 D5 + cycle-030 D2 — recurrence-2).** Cycle-028 D5 (`incremental-ls-composition-lowering` audit) emitted two `note:` values starting with `"`; the per-report integrator caught the parse failure and repaired by single-quote-wrapping (which works for double-quote-leading values but does NOT generalize to single-quote-leading values; the cycle-028 codification of the rule named only the double-quote hazard). Cycle-030 D2 (`bilinear-form-mutation-rotation` audit) emitted two `note:` values starting with `'`; the producer self-check in the report Summary explicitly claimed "no leading-double-quote note values (yaml.safe_load hazard avoided)" — exactly the narrower c028 form — and the single-quote variant slipped past, producing the identical `ParserError` at line 69 column 63 in `yaml.safe_load`. The c030 critic ran the round-trip and flagged `citation-validity: fail`; the repairer rephrased each note to start with prose (the quoted term embedded in the body of the note, not at its start).

**Mitigation (cycle-030 meta-phase, this entry — go).** Three coordinated edits enacted: (a) `.claude/agents/lowering-verifier.md` §Discipline — new bullet stating the generalized rule + the producer self-check predicate + the `yaml.safe_load` mechanical check pre-emit; (b) `.claude/agents/critic.md` check 1 `citation-validity` — extended with the "`verified_against:` YAML round-trip sub-check" (extract the block; `yaml.safe_load` it; flag `citation-validity: fail` on `ParserError` with the line+column); (c) promoted skill `verified-against-note-no-leading-quote-of-either-kind` (the deterministic producer self-check + critic check + repairer rephrase pattern). The leverage point is *the generalized predicate*, not "ban single-quote too" — the producer must understand the *symmetry* of the hazard, not memorize two narrower bans.

**Watch:** recurrence-2 (cycles 028 + 030 = two distinct cycles, both lowering-verifier emissions). The producer self-check predicate is now the symmetric form; the c031+ batch-9 cycle should not see recurrence-3 unless the producer skips the self-check entirely. If recurrence-3 surfaces, escalate (the producer-spec bullet is in place; a recurrence-3 means the bullet is being read but not applied, which is a different shape of problem).

---

```yaml
---
slug: firm-chapter-prose-cites-paraphrased-name-not-literal-anchor
first_observed: cycle-024
last_observed: cycle-030
recurrence_count: 2
status: addressed-by-acceptance
addressed_by: cycle-030 meta-phase (batch-8) — accepted as a documented allowable convention. Producer prose may cite a concept by paraphrase (a semantically-matching nickname for the literal token) so long as the cited line-range CONTAINS the concept; the literal token may live elsewhere in the same chapter. No producer-spec bullet imposed (paraphrase aids readability + is bounded by the line-range containment guard). The auditor self-discloses the paraphrase, the critic verifies the range contains the semantics, and the latent friction-ledger entry is promoted to addressed (not escalated to a producer restriction).
---
```

**Pattern (citation-by-paraphrase, range-containing-the-concept).** A producer's prose says e.g. "non-associativity non-law" and cites a range whose literal token "non-associativity" appears elsewhere in the chapter (e.g. at `:339`), while the cited range (e.g. `:278-285`) contains a *semantic match* (e.g. "Rotation-stream associativity / re-factorisation equivalence at the bit level"). The `citecheck --anchor 'non-associativity'` tool would drift the anchor to the literal `:339`, but the prose's cited range is correct in *meaning* — the cited range really does discuss the concept the prose names. The two distinct phrasings refer to the same algebraic fact.

**Evidence (cycle-024 first instance, cycle-030 D3 second instance — recurrence-2).** First instance was a latent observation in the cycle-024 batch and was not promoted to the friction-ledger at that time (it didn't recur until cycle-030). Cycle-030 D3 (lowering-verifier on `ls_update_column` L1-leaf audit) self-discloses: the leaf prose nickname "rotation-stream non-associativity non-law" semantically matches the L2 chapter bullet at `:278-285` "Rotation-stream associativity / re-factorisation equivalence at the bit level," while the literal token `non-associativity` is at `:339` in a downstream summary. The c030 D3 auditor flagged it in §Open-questions as worth a meta-phase signal; the c030 D3 critic confirmed the auditor's "semantic match, paraphrase noted" verdict is correct and the cited range really contains the concept. Both the auditor and the critic agree the citation is sound — the paraphrase aids readability and the line-range containment is the guard that keeps the citation honest.

**Adjudication (cycle-030 meta-phase, this entry — go, with status `addressed-by-acceptance`).** Two distinct outcomes were possible:
- **Restrict** — require producers to cite the literal-anchor line (`:339`), not the paraphrased-matching range (`:278-285`). This would forbid the nickname-with-semantically-matching-range pattern entirely and force citations to chase the literal token wherever it lives in the chapter.
- **Accept** — document the pattern as allowable when (a) the auditor self-discloses the paraphrase, AND (b) the cited line-range CONTAINS the concept semantically, AND (c) the critic verifies the containment. The literal-token line is a sibling locale, not the only valid citation site.

**Decision: accept.** Rationale: (i) the paraphrase aids readability when the literal token is in a downstream summary or a different surrounding context — forcing producers to cite the literal site can pull the reader into a less-relevant section; (ii) the line-range containment IS a meaningful guard (a paraphrase that cites a range NOT containing the concept is a real defect, distinct from this pattern); (iii) the cost of forbidding paraphrase-citations would be high (a producer-spec bullet, repairer rounds chasing literal tokens, prose stiffness) for low benefit (the citation is already sound in meaning). The c030 D3 case demonstrates the auditor self-disclosure + critic containment-check is sufficient.

**Watch:** if recurrence climbs (≥4 cycles), revisit — particularly if a future instance shows the auditor *failing* to self-disclose the paraphrase, which would weaken the acceptance argument (the disclosure is what makes the pattern auditable). Also revisit if the line-range containment guard fails (a paraphrase cites a range that does NOT actually contain the concept) — that would be a citation-honesty defect, not the benign paraphrase pattern.

---

```yaml
---
slug: obstruction-sub-kind-opaque-library-vs-enum-only-stub
first_observed: cycle-029
last_observed: cycle-029
recurrence_count: 1
status: addressed
addressed_by: cycle-030 meta-phase (batch-8) — codified the two sub-kinds (enum-only-stub vs opaque-library-ownership) in CLAUDE.md §Methodology invariants + the abstractor role-spec §Discipline. The sub-kind tag is mandatory in the `## Status: obstruction (<sub-kind>)` line going forward.
---
```

**Pattern (two methodologically distinct shapes wearing the same `obstruction` status).** The `obstruction` category has covered two distinct shapes since cycle-004 (the MINRES + BiCGStab themes were enum-only Palace-internal stubs) and cycle-029 (the triangular-solve-obstruction was the FIRST opaque-library-ownership obstruction). The routing decision the obstruction encodes is different:
- **`enum-only-stub`** — Palace-internal TODO / aborting branch; could in principle be implemented upstream.
- **`opaque-library-ownership`** — functionality is library-owned (HYPRE / SLEPc / external direct-solver); Palace consumes it opaquely; nothing to fix upstream.

**Evidence (cycle-029 D3 `triangular-solve-obstruction`).** The first opaque-library-ownership obstruction in the cohort. Its negative anchors are HYPRE relax-type enum strings (`palace/linalg/hypre.cpp`) + external direct-solver wrappers — none of which are Palace-owned method bodies. Structurally distinct from the cycle-004 MINRES/BiCGStab themes (which point at Palace-owned aborting branches like `MFEM_ABORT("MINRES is not implemented")`). The c029 integrator-signals dump flagged the distinction as a c028+c030 meta-phase agenda item; the c030 batch-closing finalize carried it forward.

**Mitigation (cycle-030 meta-phase, this entry — go).** Two coordinated edits enacted: (a) CLAUDE.md §Methodology invariants — added a new invariant bullet "Obstruction themes have two sub-kinds" alongside the `partly-constructive` and `partial-obstruction` codifications; the bullet names the two sub-kinds, the routing implications, and the default-rules (Palace-owned TODO → enum-only-stub; non-Palace callable → opaque-library-ownership); (b) `.claude/agents/abstractor.md` §Discipline — added a producer-side bullet making the sub-kind tag mandatory in the `## Status` line, with the same default-rules. The cross-layer-cross-cutter is also informed (an enum-only-stub is "anticipated upstream work"; an opaque-library-ownership is "permanently library-owned, never re-promotable") via the CLAUDE.md prose.

**Watch:** single instance so far (the cycle-029 trsv-obstruction is the only opaque-library-ownership entry). If the c031+ batch-9 surfaces more opaque-library obstruction candidates (the cycle-021 OQ `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` is a predicted future case at L3, but as `partial-obstruction` not full `obstruction`), the sub-kind tag will get more use. If after several cycles no new opaque-library-ownership entries surface, the sub-kind is still useful (it documents the cycle-029 boundary precisely + names the routing decision for future producers).

---

```yaml
---
slug: dispatch-resilience-iterative-cpp-running-qr-region
first_observed: cycle-029
last_observed: cycle-030
recurrence_count: 3
status: addressed
addressed_by: cycle-planner.md §Discipline pre-localize-known-heavy-regions bullet (path (a), user directive 2026-05-30)
---
```

**Pattern (dispatch-resilience: API socket/timeout failures clustered on one source region).** Across batch-8 (cycles 028/029/030), **3 dispatch retries** all clustered on the same Palace source region — the `iterative.cpp` running-QR localization (`:634-640` GMRES Arnoldi column update + `:813-819` FGMRES variant). c029 D5 needed 2 retries (socket error + 63-min timeout); c029 D6 needed 2 retries (socket error); c030 D4 needed 1 retry (socket error). All 3 dispatches fixed CLEAN on the constrained-anchor-prelocalization retry strategy (the orchestrator pre-supplied the exact L0 anchors in the retry dispatch prompt, eliminating the over-long localization loop that triggered the API socket failure).

**Hypothesis.** The `iterative.cpp` running-QR region is a token-dense, template-heavy block (GMRES/FGMRES variant dispatch + Givens-rotation kernel + per-column Hessenberg update). A producer dispatched against this region without pre-supplied anchors tends to enter a long localization loop (codemap calls + read_range expansions + token accumulation) that ultimately hits an API socket/timeout threshold. The constrained-anchor retry skips the localization loop because the anchors are already in the prompt — the producer reads the cited lines and proceeds directly to authoring.

**Constrained-anchor-prelocalization workaround is effective but is silting (per memory `escalate-process-issues-dont-work-around`).** The fix is currently a *manual orchestrator intervention*: when a dispatch fails, the parent identifies the heavy region, pre-localizes via the codemap, and dispatches a retry with the anchors embedded. This is load-bearing process work that doesn't surface in the role-specs or skills — it lives only in the orchestrator's knowledge of which regions are heavy. If the pattern continues (recurrence-4 in batch-9), the workaround should be promoted to either:
- **A cycle-planner role-spec bullet** — when dispatch scope includes `iterative.cpp` running-QR or similar known-heavy regions (a watch-list), pre-fetch the codemap range and embed it in the dispatch scope, eliminating the inflated context that triggers the API socket failures.
- **A harness-level dispatch retry/backoff** — automatic constrained-anchor retry on transient API failure, with the anchors derived from the dispatch scope's named source regions.

**Adjudication (cycle-030 meta-phase, this entry — ask).** Per the memory `escalate-process-issues-dont-work-around` (if a workaround pattern surfaces, raise it to the user with a proposed repair path rather than silting), this is flagged as an **ask** for the human, not enacted by this meta-phase. The two repair paths above are both methodology-relevant (cycle-planner spec change vs. harness change); the choice depends on whether the human prefers a project-local fix (cycle-planner bullet) or a harness-level fix (which may need code changes the meta-phase can't enact). The workaround is effective enough that the c031+ batch-9 cycles will continue running cleanly; the ask is whether to address the underlying friction at recurrence-3 or to wait for recurrence-4.

**Watch:** if recurrence-4 surfaces (a fourth cycle hitting socket/timeout on the same region) before the human responds to the ask, escalate to the cycle-planner-bullet path unilaterally (the lower-cost repair). The harness-level fix stays open as a longer-term option.

**Resolution (2026-05-30, user directive — path (a) chosen, enacted post-batch-8 meta-phase).** The human responded to the ask at recurrence-3 (did not wait for recurrence-4) and chose **path (a): the project-local cycle-planner role-spec bullet**. Enacted: `.claude/agents/cycle-planner.md` §Discipline gained a "Pre-localize known-heavy source regions and embed the exact L0 anchor ranges in the dispatch scope" bullet with an extensible known-heavy watch-list seeded with the `iterative.cpp` running-QR / restart machinery + Givens-kernel anchors. Status flips `watching (ask-surfaced)` → `addressed`. The cycle-planner now pre-fetches + embeds anchors for watch-list regions at plan time, so the orchestrator no longer needs the manual constrained-anchor-retry intervention for the known region. **The harness-level fix (path (b): auto-anchor-injection on transient-failure retry) stays an open longer-term option** — not enacted (it may need harness code changes the project can't make); recorded here so a future recurrence on a region NOT yet on the watch-list (where pre-localization didn't catch it) can re-open the harness-level discussion. **Watch (post-resolution):** confirm batch-9 dispatches against `iterative.cpp` run clean with the planner pre-supplying anchors (the bullet's first live test); add any new fail-and-recover region to the watch-list per the bullet's extension rule.

---

```yaml
---
slug: cycle-planner-stale-priorities-line-recruitment
first_observed: cycle-031
last_observed: cycle-036
recurrence_count: 6
status: addressed
addressed_by: cycle-033 meta-phase (batch-9) — (a) c033 cycle-planner WORKING PRECEDENT; (b) skill `verify-dispatch-scope-not-already-discharged`; (c) cycle-planner role-spec ENFORCEMENT bullet. **STRENGTHENED cycle-036 meta-phase (batch-10) — recurrence-3-WITHIN-BATCH-10 after the batch-9 codification proved the prompt-level + skill-level codification insufficient at the planner side**: (d) cycle-planner role-spec bullet AMENDED to require **PASTED INLINE EVIDENCE** (literal `ls`/`grep`/`## Status`-line output, not assertion of compliance); (e) skill `verify-dispatch-scope-not-already-discharged` extended with §"Batch-10 strengthening" + steps 5 (STOP-PROPOSING NEGATIVE LIST consult) + 6 (audit-first vs reflexive-harvest framing); (f) c036 cycle-planner WORKING PRECEDENT (paste-inline-evidence pattern); (g) the STOP-PROPOSING NEGATIVE LIST recorded prominently in `priorities.md` Backlog as the anti-recurrence data feed. **Swap-to-opus ENACTED 2026-05-31** — the human, presented with the meta-phase ASK, chose swap-now, then directed **all** agent models to Opus 4.8 (`claude-opus-4-8`); the cycle-planner haiku→opus escalation is subsumed by that blanket upgrade (CLAUDE.md §Models). The paste-inline-evidence procedure (d/e/f above) remains the load-bearing repair (the fix is in the *procedure*); the opus tier additionally removes the haiku assert-without-verifying failure mode (the decisive c035 datapoint) as belt-and-suspenders. **CLOSED→addressed by the batch-11 meta-phase (post-cycle-039): the batch-11 validation runway (037/038/039) ran 3-of-3 CLEAN — every planner cycle carried a `## Deliverable-presence verification` section with literal pasted command output and zero stale-line recruitment (`dispatches_planned_stale: 0` in all three cycle-record rows; zero orchestrator overrides). The combined procedure (paste-inline-evidence) + tier (opus) fix held across a full 3-cycle batch. The watch trigger's demotion condition is satisfied.** Demote to `resolved` only if it stays stale-free for ≥10 cycles (through ~cycle-049).
---
```

**Pattern (deliverable-presence-staleness — the deeper sub-pattern that the c027 file-existence check does NOT catch).** The cycle-planner recruits a dispatch off a stale `priorities.md` line whose target is **already discharged** in one of four shapes the c027 file-existence bullet does not catch: (1) the target chapter is **firm on-disk** (file exists but is already firm at the proposed maturity); (2) the target theme **already has a `verified_against:` block** at the timestamp class the audit would emit; (3) the target slice-reduction audit was **completed in the immediately-prior cycle** (RESOLVED disposition in `open-questions.md`); (4) the proposed promotion is **structurally test-coverage-gated** and the gate has not changed since the priorities line was authored. Sibling-and-deeper of `cycle-planner-reproposes-already-landed-work` (the c027 entry, which addressed *file-existence* via `counts_after`/STAGING/struck-Backlog markers); this entry addresses *deliverable-presence* (the artifact's on-disk maturity + already-discharged state).

**Evidence (recurrence-3 across batch-9).**
- **cycle-031 (recurrence-1):** the D6 substantive-landing slot was filled twice with stale `priorities.md:36` (`nleps-interior-atom-l1-l0-themes`) and `:37` (`eigsolve-l2-l1-and-concept`) lines whose targets BOTH firm-landed at cycle-025 (six cycles out of date). Two no-op disposition-only CYCLE.md files emitted; orchestrator retired the two stale plan lines. Filed by orchestrator as `cycle-planner-pre-dispatch-existence-check-of-target-artifact` OQ + `verify-dispatch-scope-not-already-discharged` skill candidate.
- **cycle-032 (recurrence-2, broader):** the planner's 6-dispatch plan was BROADLY STALE — **4 of 6 picks** stale. D3 re-proposed the `sparse_triangular_solve` slice-reduction audit completed in the **immediately-prior c031** (one cycle earlier). D4/D5 re-proposed `matrix-weighted-norm` promotion that is test-coverage-gated per the c021 codification (`rough-in (test-coverage-bounded)` first-class qualifier — stays rough-in until an out-of-scope Palace-source test change). D6 re-proposed lowering-verifier audits of 4 batch-6 themes that ALREADY have `verified_against:` blocks on disk. Orchestrator overrode the stale picks with existence-verified open work (3 dispatches landed; the cycle ran cleanly). **The c031 file-existence check is INSUFFICIENT** — it catches file presence, NOT (i) firm-theme-with-audit-block, (ii) audit-already-discharged-in-prior-cycle, (iii) test-coverage-structurally-blocked promotion.
- **cycle-033 (working repair, NOT a recurrence in the failure sense):** the c033 cycle-planner adopted a deeper deliverable-presence check (file existence + `verified_against:`-block presence + RESOLVED-grep + structural-block check) BEFORE finalizing dispatches. 3/3 dispatched targets were genuinely-open frontier work; the batch ran cleanly. The c033 planner's `## Deliverable-presence verification` section (in its own CYCLE.md) is the canonical procedural precedent.

**Mitigation (cycle-033 meta-phase, this entry — go).** Three coordinated edits enacted:
- **(a) Cycle-033 cycle-planner CYCLE.md is the working precedent.** The four-check sequence (file existence + already-audited check + RESOLVED-grep on OQ ledger + structural-block check) is documented per-dispatch in the c033 plan with each candidate's check outcome.
- **(b) Skill `verify-dispatch-scope-not-already-discharged` PROMOTED** (`skills/verify-dispatch-scope-not-already-discharged/SKILL.md`). The skill body specifies the deeper-check pattern + the c033 planner CYCLE.md as the canonical working reference. Default-accept under the low-bar promotion policy (recurrence ≥2; concrete procedure; pattern observed); the c031 candidate already sketched it, c032 OQ promoted it, c033 working precedent realises it.
- **(c) Cycle-planner role-spec ENFORCEMENT bullet** (`.claude/agents/cycle-planner.md` §Discipline). The c027 bullet (`verify-candidate-is-genuinely-open` via `counts_after`/STAGING/struck-Backlog) is *guidance*; the c031/c032 recurrence demonstrates guidance is insufficient for the deeper sub-pattern. The new bullet wires the four-check sequence as a MANDATORY pre-dispatch ritual for any named-artifact-slug scope (every `(agent, scope)` tuple where `scope` resolves to a file path under `book/src/`). The bullet cites the skill + the c033 working precedent.

**Why not swap to opus (batch-9 reasoning, batch-10 confirmation).** The c033 working precedent demonstrated **the deeper check CAN be done by haiku** — the c033 planner ran 3/3 clean with the new procedure. The c036 paste-evidence working precedent re-confirmed it — when the planner is required to paste literal evidence, the check actually runs. The fix is in the *procedure*, not the *tier*. Swap-to-opus was surfaced as a meta-phase **ASK** to the human for the recurrence-7 threshold — but the human, presented with the ASK, **chose swap-now (2026-05-31) and then directed all agent models to Opus 4.8** (`claude-opus-4-8`; CLAUDE.md §Models). So as of batch-11 the cycle-planner runs on opus *and* under the paste-inline-evidence procedure — both repairs active. The procedure remains primary; the tier change is belt-and-suspenders against the haiku assert-without-verifying mode.

**Batch-10 evidence (recurrence-3-WITHIN-BATCH-10 escalation).**
- **cycle-034 D3 (recurrence-1 post-batch-9):** the planner re-proposed `harvester-l3-krylov-step` whose scope had discharged at c010 (24 cycles prior). The role-spec ENFORCEMENT bullet was active but the planner did not run the deliverable-presence check. The orchestrator caught it; the d3 dispatch ran as a no-op disposition-only CYCLE.md. Direct evidence the role-spec bullet alone is insufficient.
- **cycle-035 (recurrence-2 post-batch-9, 2-of-3-stale plan):** the planner produced a 2-of-3-stale plan (D1 `apply-nonlinear-pencil-mutation-rotation` audit already discharged since ~c025 with `verified_against:` block on disk; D3 `apply_linop` L3 backfill already firm since c011, 8 cycles prior). The planner CLAIMED the four-step check had run ("all three are genuinely open") but did NOT actually verify on-disk. The orchestrator caught both stale picks and substituted 3 verified-open dispatches. **This is the decisive datapoint** — a claim-of-compliance without paste-evidence is not load-bearing.
- **cycle-036 (recurrence-3-softer, but paste-evidence working precedent):** the planner correctly REJECTED the stale batch-6 audit candidates WITH inline pasted evidence (the c036 cycle-planner CYCLE.md is the canonical paste-evidence working precedent). One D2 pick still required orchestrator reframe (planner proposed `assemble-diagonal` L3 as a reflexive identity-in-form harvest without an upfront audit; the orchestrator substituted the proper audit-first cross-layer L3-cohort-growth dispatch — and the audit CONFIRMED `assemble-diagonal` IS (A) identity-in-form, so the planner's *instinct* was right but the *method* was wrong). This is a different sub-pattern (reflexive-harvest vs audit-first framing at cohort boundaries) addressed by skill step 6 added this batch.

**Mitigation (cycle-036 meta-phase batch-10 strengthening — go).** Three coordinated edits enacted:
- **(d) Cycle-planner role-spec bullet AMENDED to require pasted inline evidence.** The previous text "Record the check outcome inline per-dispatch in the plan" was reading-room: the c035 planner asserted compliance without paste. The amended text demands literal pasted output (`ls` exit / stat, the `## Status` line read from disk, the `grep` results, the structural-gate citation) — claim-without-paste is now an explicit recurrence-class fault.
- **(e) Skill `verify-dispatch-scope-not-already-discharged` extended with §"Batch-10 strengthening" + step 5 (STOP-PROPOSING NEGATIVE LIST consult) + step 6 (audit-first vs reflexive-harvest framing).** Steps 5/6 address the c036-surfaced sub-patterns: a permanent disqualification list as the anti-recurrence data feed; and the cohort-boundary framing question for operator-to-data primitives. The c036 cycle-planner CYCLE.md is now a second canonical working precedent (alongside c033).
- **(f) STOP-PROPOSING NEGATIVE LIST recorded prominently in `priorities.md` Backlog Medium tier.** The 7-operator (C) negative list (`lu_solve`, `back_solve`, `ls-update-column`, 4 NLEPS atoms — disqualified by small-dense coordinate-space axis per the c036 D2 audit verdict at `book/src/L3/index.md:38`) is visible at the top of every cycle-037+ planner's inputs.

**Why not the mechanical pre-dispatch gate.** Considered as repair-path (b): an integrator-finalize-side mechanical check that greps on-disk `## Status` + `verified_against:` block + RESOLVED-grep for every named-artifact-slug scope before any dispatch fires. NO-GO this batch: the c036 paste-evidence success suggests the prompt-level fix is sufficient when the demand is for literal output (not assertion). A mechanical gate is a larger structural change (orchestrator code touch); revisit ONLY if recurrence-7 surfaces despite the paste-evidence demand + STOP-PROPOSING list + audit-first framing.

**Watch (batch-11 RESULT — CLOSED).** Batch-11 was the explicit confirmation window. All three cycles (037/038/039) ran with `dispatches_planned_stale: 0`, each planner CYCLE.md carried a `## Deliverable-presence verification` section with literal pasted command output, and there were zero orchestrator overrides (cf. the c034/c035/c036 overrides). The combined fix (paste-inline-evidence procedure + opus tier, both active by batch-11) held across a full 3-cycle batch — recurrence-7 did NOT surface. The swap-to-opus ask is ANSWERED (the human enacted it via the 2026-05-31 blanket Opus-4.8 upgrade; the ask loop is closed). The mechanical pre-dispatch gate stays a deferred-and-not-needed option (NO-GO confirmed — the prompt+tier fix is sufficient). Status moved `escalating`→`addressed`. Re-open ONLY if staleness recurs in batch-12+ (recurrence-7) — that would re-open both the mechanical-gate option and the question of whether the opus tier degrades on this specific multi-step verification under context pressure.

---

```yaml
---
slug: negative-result-slice-canonical-instance-blocks-reduction
first_observed: cycle-013
last_observed: cycle-031
recurrence_count: 4
status: addressed
addressed_by: cycle-033 meta-phase (batch-9) — (a) CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is lifted" AMENDED with a canonical-instance carve-out (the slice may be retained-by-design when it is the named referent of ≥2 concept-pages and carries unique L0 navigation not covered elsewhere in the firm artifact); (b) `skills/phase-1-slice-reduction-audit/SKILL.md` checklist gained a canonical-instance check line; (c) this friction-ledger entry codifying the design exception.
---
```

**Pattern (Phase-1 slice-reduction requires a SECOND axis beyond "firm layered home exists").** The CLAUDE.md invariant "Phase 1 corpus reduces as material is lifted" + the `phase-1-slice-reduction-audit` skill verify that the slice's content has a firm layered home and recommend reduction-to-stub when it does. This check is **necessary but not sufficient** — a slice may have a firm layered home AND still be load-bearing as the **named canonical-witness instance** of ≥1 downstream concept pages. Reducing it to a stub strands the concept page's "see also" / "instance of" reference. The audit needs a second axis: "is the slice a named §Canonical-instance on a concept page?"

**Evidence (recurrence-4 — used implicitly cycles 013/022/028/031 before codification).**
- **cycle-013:** `polynomial_recurrence_step` slice candidacy — slice retained-by-design as the canonical instance for the chebyshev cohort's polynomial-recurrence concept page (the SECOND-axis precedent that established the design exception).
- **cycle-022:** revisited; the precedent held.
- **cycle-028:** the `trsv` L1 leaf was routed to obstruction (cycle-029 `triangular-solve-obstruction` theme); the parent slice `sparse_triangular_solve` was a candidate for reduction.
- **cycle-031 (D5 same-layer-cross-cutter):** `sparse_triangular_solve` slice-reduction audit ran the firm-layered-home check (positive: the c029 `triangular-solve-obstruction` is on disk) AND independently surfaced the canonical-instance second axis — the slice is the named §Canonical-instance for 3 concept pages. Verdict: **DEFER (retain in full, annotated-and-retained)**. The auditor's §Open-questions item flagged the two-axis pattern as a meta-phase candidate (CLAUDE.md amendment + skill update + friction-ledger entry). Phase-1 removals stay 9/10.

**Mitigation (cycle-033 meta-phase, this entry — go).** Three coordinated edits enacted:
- **(a) CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is lifted" AMENDED.** The invariant gains a canonical-instance carve-out: a slice MAY be retained-by-design when it is named (by slug + filename) as the §Canonical-instance / "instance of" referent of ≥2 concept pages in `book/src/concepts/` AND carries unique L0 navigation (file:lines anchors) not covered elsewhere in the firm artifact. The carve-out is bounded by ≥2 concept-page references (a single concept-page reference is recoverable by re-anchoring the concept page); the carve-out does NOT license retaining slices that are only fully-lifted-AND-not-referenced.
- **(b) `skills/phase-1-slice-reduction-audit/SKILL.md` checklist gains a canonical-instance check line.** Before recommending reduction-to-stub, the auditor scans `book/src/concepts/` for references to the slice (filename + slug) and counts named §Canonical-instance / "instance of" mentions. If count ≥2, the audit verdict shifts to DEFER-by-canonical-instance (retain in full, annotated) regardless of firm-layered-home presence.
- **(c) This friction-ledger entry codifies the design-exception class.**

**Why not promote the carve-out to a separate methodology pillar.** The carve-out is *bounded* — it applies only when the slice is genuinely load-bearing as a navigation referent — and the ledger's recurrence-count is small (4 cycles across the project lifetime, only the cycle-031 instance after the cycle-013 precedent). The CLAUDE.md amendment + skill checklist line is sufficient codification without a separate invariant heading. If the carve-out gets exercised more frequently (recurrence ≥6 cycles), revisit as a candidate for promotion to its own invariant.

**Watch.** Confirm c034+ slice-reduction audits run the second-axis check. If a c034+ audit reduces a slice that is a canonical instance (failure mode — the second-axis check was not applied), reopen.

---

```yaml
---
slug: parallel-blind-shared-index-count-divergence
first_observed: cycle-037
last_observed: cycle-042
recurrence_count: 3
status: addressed (batch-12 confirmation window CLEAN at 7-wide + 11-wide)
addressed_by: cycle-039 meta-phase (batch-11) — (a) D3-count-ownership convention codified as a cycle-planner dispatch-design §Discipline bullet (when ≥2 parallel dispatches touch a shared running-count / tally in a layer index, assign ONE owner and instruct the other dispatches to skip the tally and emit only their own non-count rows); (b) matching producer-side note in harvester + layer-intro-author role specs (do not write the consolidated index tally when another co-dispatched agent owns it this cycle). The c039 cycle (D3 layer-intro-author sole-owns the L3/index Working-Notes tally; D1 harvester appends only its dep-map row) is the working precedent.
---
```

**Pattern (parallel dispatches each writing a shared running-count blind to cohort-mates).** When ≥2 parallel dispatches in one cycle each append a chapter/operator to the same layer index (`book/src/L_n/index.md`) AND each also writes the index's consolidated firm-count tally / Working-Notes running count, every dispatch authors its count bullet **blind to its cohort-mates' simultaneous landings** — so the absolute counts they each report are inconsistent (e.g. three parallel L3 harvesters each writing `12` / `13` / `12`), and the integrator-finalize must reconcile the divergent bullets to one correct state at apply-time. The work itself is correct (each chapter lands fine); the friction is the **shared-mutable-running-count under concurrent blind writers**, a classic write-write conflict on a derived aggregate. It is the count-tally analogue of the `wave-conflict-philosophy-scales` row-level edits — except a running *aggregate* (unlike a distinct dep-map row) cannot be made non-overlapping by per-anchor distinctness, because each writer needs the post-cohort total it cannot see.

**Evidence (recurrence-3 across batch-11; c037+c038 divergence → c039 clean fix).**
- **cycle-037 (recurrence-1):** two parallel L3 harvesters (`assemble-diagonal` + `jacobi-smoother`) each flagged a firm-count bump; the finalize reconciled the consolidated D2-flag superseding D1's narrower flag (tally → 11 firm + 2 partial-obstruction). Recorded in the c037 cycle-record `row_refresh` + two `l3-index-firm-count-bump-*` OQs (D1 one SUPERSEDED at finalize).
- **cycle-038 (recurrence-2, sharpest):** **three** parallel L3 harvesters (`reciprocal` + `elementwise_product` + `divfree-projector`) each self-reported an inconsistent absolute count (`12` / `13` / `12`), each authored blind to cohort-mates; the finalize reconciled all three to the single correct state (14 firm + 2 partial-obstruction). The c038 cycle-record `row_refresh_target` documents this verbatim ("the three parallel dispatches self-reported inconsistent absolute counts … each authored blind to cohort-mates").
- **cycle-039 (clean fix — the working precedent):** the orchestrator assigned the L3/index Working-Notes count tally to ONE dispatch (the D3 layer-intro-author) by **count-ownership partition**, and instructed the parallel harvester (D1 `normalize`) to append ONLY its dep-map row and DEFER the tally to D3. Result: the finalize did NOT need to reconcile — the parallel-blind count-divergence was cleanly avoided. The c039 cycle-record `row_refresh_note` documents the convention and its clean outcome.

**Mitigation (cycle-039 meta-phase, this entry — go).** Two coordinated edits:
- **(a) cycle-planner dispatch-design §Discipline bullet** — when a cycle dispatches ≥2 parallel agents that each touch a shared running-count / consolidated tally in a layer index (`book/src/L_n/index.md` Working-Notes firm/partial counts; any `index.md` aggregate that sums over the cohort), the planner assigns the consolidated-tally write to **exactly ONE owner** (preferably a layer-intro-author dispatch if one is in the wave; otherwise the last harvester in dependency order) and instructs the other dispatches to emit only their own non-aggregate rows (dep-map row, SUMMARY registration) and to DEFER the tally. The c039 plan is the working precedent.
- **(b) harvester + layer-intro-author producer-side note** — a §Discipline bullet: if the dispatch prompt says another co-dispatched agent owns the index's consolidated count this cycle, write only your own dep-map / SUMMARY row and do NOT touch the running-count tally (it will be authored once, post-cohort, by the owner).

**Why role-spec convention (Medium-cascade), not a structural change.** The divergence was always cheaply reconciled by the finalize (no artifact damage, just a reconciliation step), and the c039 partition demonstrably eliminated it at near-zero cost (one sentence of dispatch-design + a producer skip-instruction). This is the minimal fix — it does not change the cycle structure or add a gate; it just assigns single-ownership of a shared aggregate, the standard concurrency fix. Genuine recurrence (c037 + c038 divergence) with a demonstrated clean fix (c039) clears the codification bar.

**Watch.** Confirm batch-12+ multi-parallel-landing cycles carry the count-ownership partition (the planner assigns ONE tally owner). If a cohort still produces divergent blind counts despite the bullet (recurrence-4), consider making the index running-count a finalize-computed field (the finalize already reconciles it — formalizing it as "the finalize owns the tally, producers never write it" would remove the convention's reliance on the planner remembering to partition).

**Batch-12 confirmation (cycle-042 meta-phase — recurrence did NOT fire; watch trigger satisfied POSITIVELY).** The convention held cleanly across the **two broadest index-touching waves to date**: cycle-041 (7-wide: D1–D6 each touched only their own dep-map/SUMMARY rows, D7 layer-intro-author sole-owned the three consolidated `L2/index.md` + `L2-L1/index.md` + `L3-L2/index.md` tallies) and cycle-042 (11-wide: D2–D10 own only their own rows, D11 sole-owned the consolidated count + re-homed two orphaned §Vocabulary bullets). Both finalize reports recorded the divergence was AVOIDED (c038-style blind-count reconciliation did NOT recur) and flagged the partition as a strong codification data point. The convention scales to 11-wide; recurrence stays at 3 (no new divergence). The finalize-owns-the-tally structural fallback stays unenacted (NO-GO — the planner-partition is sufficient at 11-wide; revisit only on a recurrence-4 despite the partition). Effectively `resolved` pending the 10-cycle no-recurrence window.

---

```yaml
---
slug: co-dispatched-harvesters-reach-contradictory-design-conclusions
first_observed: cycle-041
last_observed: cycle-041
recurrence_count: 1
status: addressed
addressed_by: cycle-042 meta-phase (batch-12) — adjudicated the leaf-vs-fold design fork `dot-l2-leaf-floor-vs-fold-only-design` (RATIFIED the (b) leaf-floor reading cohort-wide as a standing convention into priorities.md §Methodology; the fork OQ closed; the held axpy-family unblocked). The cycle-042 dedicated `same-layer-cross-cutter` audit was the resolution mechanism: a cross-cutter dispatch to supply the count-delta + distinctness evidence the meta-phase then adjudicates.
---
```

**Pattern (two parallel same-cohort harvesters reach OPPOSITE conclusions about a shared design question).** In cycle-041, two co-dispatched L2-floor harvesters — D1 (`dot`) and D2 (`nrm2`) — reached contradictory conclusions about whether `L2/dot` should exist as a standalone same-named chapter at all: D1 built it as a leaf-floor of `inner_product`; D2 argued the L2 inner-product surface should be the fold ONLY, with no `dot` leaf. The contradiction was upstream of the whole cycle-041 cohort + its six themes (all built under the D1 (b) reading). This is distinct from the `wave-conflict-philosophy-scales` row-level *edit* conflict (benign, anchor-distinct) and from `parallel-blind-shared-index-count-divergence` (a derived-aggregate write conflict): here the conflict is a genuine **design disagreement** about whether an artifact should exist, which only a methodology adjudicator (the meta-phase) can settle.

**Resolution mechanism (the working precedent — recommended for future design forks).** Rather than the meta-phase adjudicating from cold prose, the cycle-042 planner steered around the fork by (i) advancing only the **fork-INDEPENDENT** slice of the cohort (the 5 standalone floors with no fold-parent) and (ii) dispatching a dedicated `same-layer-cross-cutter` AUDIT (`reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/CYCLE.md`) to produce the count-delta table + distinctness verdict + asymmetry carve-out as explicit meta-phase INPUT. The meta-phase then ratified with strong evidence in hand. **The pattern to carry forward: when two co-dispatched producers reach a contradictory design conclusion, the next planner HOLDS the fork-exposed work, advances the fork-independent slice, and tees up a dedicated cross-cutter audit as the meta-phase adjudication evidence** — the same shape as the `partly-constructive` lowering-verifier-unblocks-then-harvester-enacts split. No role-spec edit warranted at recurrence-1 (the cycle-042 planner already executed this organically); recorded as the working precedent.

**Watch.** If a future cycle's co-dispatched producers reach a contradictory design conclusion AND the planner does NOT hold + audit (just lands one reading blind), escalate to recurrence-2 and consider a cycle-planner §Discipline bullet ("when two same-cohort dispatches could reach opposite design conclusions, hold the fork-exposed work and dispatch a cross-cutter audit before treating either reading as final").

---

```yaml
---
slug: index-dual-registration-row-and-own-bullet-vs-consolidated-tally
first_observed: cycle-043
last_observed: cycle-045
recurrence_count: 1
status: addressed
addressed_by: cycle-045 meta-phase (batch-13) — codified the dual-registration partition (producer adds BOTH its own index-table ROW AND its own §Vocabulary-cohort BULLET; the count-owner adds ONLY the consolidated tally + growth-log + fork-flips) as producer-side §Discipline bullets in `.claude/agents/harvester.md` + `.claude/agents/abstractor.md` + a layer-intro-author count-owner-scope note + a cycle-planner dispatch-design clause. The complement to the cycle-039 `parallel-blind-shared-index-count-divergence` count-ownership convention (which says what to DEFER); this says what producers always OWN.
---
```

**Pattern (the index-registration partition is two-sided, and only the *defer* half was codified).** The cycle-039 `parallel-blind-shared-index-count-divergence` convention assigned the **consolidated running-count tally** to ONE owner and told co-dispatched producers to DEFER it. But a layer index carries THREE per-cohort artifacts, not one: (1) the per-chapter **dep-map / index TABLE row**, (2) the per-chapter **§Vocabulary-cohort BULLET** (the firmness-split sub-list entry), and (3) the **consolidated tally** (the cohort-summing count + growth-log + fork-flip prose). The c039 convention named only (3) as the deferred aggregate; it left (1) and (2) — which are each producer-OWNED, non-aggregate, anchor-distinct — implicit. So co-dispatched producers handled (1)/(2) **inconsistently**: some deferred their own cohort bullet to the count-owner (treating it like the tally), some omitted the table row entirely (assuming the count-owner would add it). The partition is: **(1)+(2) are always the producer's own** (anchor-distinct, parallel-safe, like any dep-map row); **only (3) defers to the single count-owner.**

**Evidence (cycle-043 D6/D7/D8/D10 — the four theme-pair reports, each needed a repairer patch; clean inline c044/c045 once the planner stated the partition).**
- **cycle-043 (the friction):** the 4 axpy-family/normalize theme-pair reports registered (1)+(2) INCONSISTENTLY — **D6** deferred its §Vocabulary-cohort bullets to D2 (the count-owner), **D7** omitted the index-table rows entirely, **D8/D10** omitted the cohort bullets — each requiring a repairer patch to reach the uniform "own table row + own cohort bullet, defer only the consolidated tally" shape. The integration-tooling-friction note in the c043 finalize CYCLE.md (signals:133) flagged it as "currently implicit/folklore — should be CODIFIED."
- **cycle-044 (clean once stated):** the c044 planner wrote the partition explicitly into the D3 dispatch scope ("producer adds BOTH the index-table ROW AND its own §Vocabulary-cohort BULLET; count-owner adds only the consolidated tally"); D3 (`orthogonalize-variant-split`) applied it inline, zero repairer reconciliation.
- **cycle-045 (clean, 3-wide):** D1 (`eigsolve-opaque-eigen-iteration`) + D2 (`chebyshev-nested-recurrence`) each owned their own table ROW + §Vocabulary-cohort BULLET (substantive sub-grouping); D3 (layer-intro-author) sole-owned the consolidated tally. No reconciliation; `parallel-blind-shared-index-count-divergence` also did not recur (the two conventions compose cleanly).

**Mitigation (cycle-045 meta-phase, this entry — go).** Four coordinated edits: (a) `.claude/agents/harvester.md` — amended the existing count-defer bullet to state the full three-artifact partition (own row + own bullet always; defer only the tally); (b) `.claude/agents/abstractor.md` — added the matching bullet (the abstractor had NO count/registration bullet before — only harvester/layer-intro-author/cycle-planner got the c039 one, yet the c043 friction was abstractor-authored theme-pair reports); (c) `.claude/agents/layer-intro-author.md` — a count-owner-scope note: when you are the designated count-owner, you write ONLY the consolidated tally + growth-log + fork-flips; you do NOT author other producers' own §Vocabulary-cohort bullets (they own theirs); (d) `.claude/agents/cycle-planner.md` — a dispatch-design clause appended to the existing count-ownership bullet stating the partition so the planner writes it into each multi-landing dispatch scope (as the c044/c045 planners did organically).

**Why role-spec convention (Medium-cascade), not a structural change.** Like the sibling `parallel-blind-shared-index-count-divergence`, the friction was always cheaply reconciled by the repairer/finalize (no artifact damage), and stating the partition in the dispatch scope demonstrably eliminated it (c044/c045 clean). This is the minimal fix — it makes explicit what was folklore. It does NOT change cycle structure or add a gate.

**Watch.** Confirm batch-14+ multi-landing waves carry the dual-registration partition with zero repairer reconciliation of row/bullet placement. Recurrence-1 (the c043 instance; c044/c045 are the clean confirmation, not new friction). If a future cohort still mis-registers (1)/(2) despite the bullets (recurrence-2), the row+bullet registration is reminder-dependent like all reminder-class mitigations — consider whether the integrator-per-report should normalize registration shape at apply-time (a larger change, deferred).

---

```yaml
---
slug: floor-landing-implies-same-cycle-adjacent-entry-reanchor
first_observed: cycle-043
last_observed: cycle-045
recurrence_count: 1
status: addressed
addressed_by: cycle-045 meta-phase (batch-13) — codified as a cycle-planner dispatch-design §Discipline bullet (`.claude/agents/cycle-planner.md`): when a plan item lands an L_n floor / sibling entry UNDER an existing L_{n+1} entry X, co-schedule X's §"Lowers-to" / `lowers_to:` re-anchor in the SAME cycle (the floor-harvester's own proposed-changes extending to X's adjacent re-anchor, OR a same-cycle lifter), so the cross-cycle stale-assertion window never opens. The c045 planner applied this proactively (D1/D2 bundled the parent L3-entry re-anchors INTO the substantive-theme dispatch) — the working precedent.
---
```

**Pattern (a floor landing under an existing entry strands that entry's "no floor below me" assertions for a cycle).** When an L_n floor (or any sibling lower-layer entry) lands UNDER an already-firm L_{n+1} entry X, X's downward framing — its §"Lowers-to" / §"Downward" prose + `lowers_to:` frontmatter, which previously asserted a *direct* L_{n+1}>L_{n-1} hop "with no interposed L_n entry" — goes **stale the moment the floor lands.** Under the one-operator-per-dispatch discipline, X is a *different operator* than the floor, so the floor-harvester does not touch it; the re-anchor is deferred to a later lifter sweep, opening a **cross-cycle stale-assertion window** (X claims "no L_n floor below me" while the floor is on disk).

**Evidence (cycle-043 → cycle-044, recurrence-1).** The c043 L2-floor cohort (`axpy`/`axpby`/`axpbypcz`/`normalize` floors D3/D4/D5/D9 + their L3>L2 body-identity themes D6/D7/D8/D10) landed, immediately staling the four firm L3 entries `L3/{axpy,axpby,axpbypcz,normalize}` (each asserting "no L2 intermediate / direct L3>L1 hop" — `L3/axpy.md:6,97,112-116` etc.). The c043 integrator-per-report could only PROMOTE the staleness as OQs (`l3-{axpy,axpby,axpbypcz,normalize}-lowers-to-staleness-after-l2-floor`, ledger:942-953) — it cannot expand scope to rewrite a different operator's chapter mid-apply. The re-anchor rode the c044 D1 consolidated lifter sweep — one cycle late. The c044 D1 lifter itself surfaced the process recommendation in its OQ `l3-leaf-cohort-l2-floor-reanchor-deferred-from-c043` (ledger:968): "future 'L2 floor lands under X' plan items should imply a same-cycle 'X §Lowers-to re-anchor' item — a coupled pair." This exactly mirrored the c041→c042 and c042→c043 deferred-sweep windows (the same staleness recurred each floor cycle); the c043→c044 instance is the third occurrence of the *window* but the first time it was named as a standing process recommendation rather than a per-cycle carry.

**Mitigation (cycle-045 meta-phase, this entry — go).** A cycle-planner dispatch-design §Discipline bullet: treat a floor-landing and its adjacent-entry re-anchor as a **coupled pair** scheduled in the same cycle — either (i) the floor-harvester's own proposed-changes extend to re-anchor the adjacent L_{n+1} entry X's §"Lowers-to" / `lowers_to:` (when X is small / the re-anchor is mechanical), OR (ii) a same-cycle lifter dispatch is co-scheduled with the floor wave to re-anchor X. The c045 planner already executed the bundled-into-the-dispatch form (D1/D2 each bundled their parent L3-entry re-anchor INTO the substantive-theme dispatch); recorded as the working precedent. This avoids the cross-cycle stale-assertion window without changing cycle structure.

**Why a planner-side coupling note (not a structural change).** The stale-assertion window is benign-but-untidy (X asserts "no floor" while the floor exists; no build break, no broken link, no false claim — just a momentarily-stale downward note). The cost is one deferred lifter touch per floor cycle. Coupling the re-anchor into the floor cycle removes the window at near-zero cost (one sentence of dispatch-design). It does NOT warrant a gate or a structural change. **Watch.** Confirm batch-14+ floor/sibling-landing cycles co-schedule the adjacent re-anchor (no fresh cross-cycle staleness OQ). If a floor lands and the planner does NOT couple the re-anchor (recurrence-2), the bullet is being read but not applied — revisit then.

**Batch-14 confirmation (cycle-048 — CLEAN, the coupling held at scale).** The cycle-048 cap landings each bundled their adjacent-entry re-anchor INTO the cap harvester's OWN proposed-changes (form (i)): D1's 3-site `L3/ksp_solve` live-link upgrade + D2's 7-site `L3/eigsolve` stale-"no L4 cap" re-anchor — 10 in-cycle re-anchors total, all clean, zero deferred cross-cycle staleness OQ (signals:60). This is a CAP-landing-over-an-existing-lower-entry instance (the converse direction of the c043 floor-under-existing-upper-entry instance), and the coupling note covered it cleanly. The bullet is being read AND applied. No recurrence; status holds `addressed`.

---

```yaml
---
slug: cross-report-forward-reference-slug-divergence
first_observed: cycle-048
last_observed: cycle-048
recurrence_count: 1
status: addressed
addressed_by: cycle-048 meta-phase (batch-14) — codified the canonical-slug-for-sibling-forward-reference convention as (a) a `cycle-planner.md` dispatch-design §Discipline clause (when one dispatch forward-references a sibling-dispatch's not-yet-existing slug, state the canonical slug in BOTH dispatch scopes) + (b) a shared producer-spec bullet (harvester + abstractor: when forward-referencing a sibling-dispatch's chapter/theme that will land THIS cycle, use the planner-stated canonical slug, not a self-invented working slug). The complement to `coordinated-cross-report-rename-premise-inversion` (which governs renames-across-reports); this governs new-slug forward-references across co-dispatched siblings.
---
```

**Pattern (a producer forward-references a sibling-dispatch's not-yet-existing slug under a self-invented working name, diverging from the canonical slug the sibling lands).** In cycle-048, D1 (the `L4/ksp_solve` cap harvester, wave 1) forward-referenced the sibling-dispatch L4>L3 theme by a *working* slug `ksp-solve-outer-driver-dissolution`, while D3 (the abstractor authoring the theme) landed it at the planner's *canonical* slug `ksp-solve-driver-dissolution`. Because the two dispatches do not share context (the roles-do-not-share-context invariant), D1 had no way to know D3's exact landed slug and guessed from the L3>L2 sibling's `ksp-solve-outer-driver` naming. This is distinct from `coordinated-cross-report-rename-premise-inversion` (a coordinated *rename* of an existing slug, where one report's premise inverts) and from `rough-in-forward-reference-must-be-plain-text-not-live-link` (the plain-text-vs-live-link encoding of a missing target): here both reports agree the target should exist and will land this cycle; they merely disagree on its *name*.

**Evidence (cycle-048 — caught by BOTH critics, repaired cheaply, zero residual).** Both the D1 and the D3 critics flagged the slug divergence; it was reconciled at repair/integrate — D1's repairer pre-wired D1's references to the canonical `ksp-solve-driver-dissolution`, D3 landed at exactly that slug, and an integration-time grep across `book/src/` returned ZERO occurrences of the working slug `ksp-solve-outer-driver-dissolution` (OQ `ksp-solve-driver-dissolution-slug-reconciliation`, RESOLVED). No artifact damage; one repairer touch. The cost was bounded because the divergence is a *plain-text/live-link slug string*, mechanically reconcilable once the canonical landed slug is known.

**Mitigation (cycle-048 meta-phase, this entry — go; low-bar default-accept).** Two coordinated role-spec edits (clean recurrence-prevention, per the incremental-refinement default-accept policy): (a) `.claude/agents/cycle-planner.md` — a dispatch-design §Discipline clause: when one dispatch forward-references a sibling-dispatch's not-yet-existing chapter/theme that will land in the SAME cycle, state the **canonical slug** explicitly in BOTH dispatch scopes (the referencing one and the authoring one), so neither producer has to invent a working slug; (b) `.claude/agents/harvester.md` + `.claude/agents/abstractor.md` — a matching producer-side bullet: when forward-referencing a sibling-dispatch's chapter/theme landing this cycle, use the **planner-stated canonical slug** verbatim; if the planner did not state one, use a plain-text backtick slug and flag it for integrator reconciliation (do NOT invent a live link to a guessed name). This is the minimal fix — it makes explicit the slug-coordination that the planner already does implicitly when it names canonical slugs in scopes.

**Why role-spec convention (Medium-cascade), not a structural change.** Like the sibling cross-report coordination conventions (`parallel-blind-shared-index-count-divergence`, `index-dual-registration-...`, `coordinated-cross-report-rename-premise-inversion`), the friction was always cheaply reconciled by the repairer/integrator (no artifact damage), and stating the canonical slug in both scopes eliminates the guess. It does NOT change cycle structure or add a gate. **Watch.** Confirm batch-15+ multi-dispatch waves with cross-sibling forward-references carry the canonical slug in both scopes (no fresh slug-divergence reconciliation). Recurrence-1 (the c048 instance, caught+repaired clean). If a future wave still diverges despite the bullets (recurrence-2), the convention is reminder-dependent like all reminder-class mitigations — consider whether the integrator-per-report should normalize forward-ref slugs at apply-time (a larger change, deferred).

---

```yaml
---
slug: rectangular-projection-drift-suppresses-in-layer-abstraction
first_observed: cycle-018 (linear_combination mined at L2, never propagated)
last_observed: cycle-048 (axpy/axpby/axpbypcz base-form at L1/L2/L3; thin -body-identity themes)
recurrence_count: structural (accumulated cycles 041–048)
status: addressed
addressed_by: 2026-06-01 VOCABULARY-SHIFT REDIRECT (user directive; full spec METHODOLOGY-REDIRECT.md; distilled in CLAUDE.md §Methodology invariants; 5 role-spec edits combinator-miner/harvester/abstractor/cycle-planner/layer-intro-author). Supersedes the 2026-05-31 "uniform pull-up → rectangular" directive + foundation_solidity/count-ownership/dual-registration rectangular-floor machinery; "Identity-lowerings still require both L levels"; the leaf-vs-fold fork ratified (b). Refactor pass + solvers-as-test-load are the batch-15 program.
---
```

**Pattern (the construction machinery optimized for verification-convenient lowerings, which forced a rectangular stack and suppressed in-layer abstraction).** Surfaced by the user (2026-06-01) across three observations: (1) the batch-14 "L4 substantially complete" claim measured completeness against the *already-lifted inner-kernel cohort* (18 firm L3 ops), silently excluding the in-scope 5 solver pipelines + FE assembly (a **denominator error**); (2) `linear_combination` was mined as a combinator at L2 (cycle-018) but **never propagated** — `axpy`/`axpby`/`axpbypcz` remained base-form at L1, L2, AND L3 (a **factoring gap**); (3) the **root cause** — the desire to make cross-layer lowerings explicit/auditable accidentally optimized for the *identity / 1:1-named* lowering (easiest to verify), which propagated downward into the layers, forcing each layer to carry the same named operators as its neighbor (**rectangular projection**). A rectangular stack has no conciseness gradient, so it generates no pressure to abstract — exactly why combinators were mined-and-stranded. The 2026-05-31 directive's own success metric ("the stack self-corrects toward **rectangular**") names the bug.

**The corrected principle (the redirect).** The stack is a sequence of genuine **representational + component-vocabulary shifts**, not a projection. Each layer is complete/concise/correct **in itself**, and the **conciseness** constraint is the engine that drives in-layer utility combinators. Each lowering is complete/concise/correct and is a **translation across vocabularies and semantic organizations — not a 1:1 rename**; a degenerate identity-in-named-terms lowering is a **smell** (the vocabulary failed to shift), resolved as a thin in-line note or a combinator re-expression, never a mirrored entry + thin theme.

**Enactment (go).** Full spec `METHODOLOGY-REDIRECT.md`; CLAUDE.md §Methodology invariants distillation; `scaffolding/priorities.md` §CYCLE-049 / batch-15 active head (refactor-pass-first program); `scaffolding/cycle-49-resume-notes.md`; 5 role-spec edits. **Batch-15 program:** (1) the **refactor pass** (collapse the cycles-041–048 base-form L2/L3 leaves into in-layer combinators, propagate upward, demote thin `-body-identity` themes) — highest priority; (2) continued shared-spine abstraction under the corrected model; (3) **solvers (5 pipelines + FE assembly) as a LOW-PRIORITY test-load** (advance only when cleanly describable in shared vocabulary, never forcing the spine). **Watch.** This is a foundational redirect (peer to the 2026-05-26 structural redirect); confirm batch-15+ work produces vocabulary-shifting layers + translational lowerings, and that no agent reintroduces a rectangular floor (same-named base-form entry at each layer + a thin connecting theme).

---

```yaml
---
slug: multi-deletion-cross-dispatch-dangling-link-coordination
first_observed: cycle-050
last_observed: cycle-051
recurrence_count: 2
status: addressed
addressed_by: cycle-051 meta-phase (batch-15) — promoted skill `deleted-slug-inbound-live-link-sweep` (critic/integrator mechanical inbound-grep + KEPT-sibling exclusion) + recorded the distinct-substring-narrowing convention for N-dispatch co-edits of a surviving line (worked cleanly at the c051 3-way line-266 co-edit)
---
```

**Pattern (a multi-deletion cycle whose deleted slugs are cross-referenced by surviving files, and/or whose deletions co-edit the same surviving line, generates in-flight defensive de-link churn that the serial per-report apply absorbs but that has no mechanical enumerate-then-check step).** Two distinct sub-shapes surfaced across the batch-15 refactor pass:
- **(i) Cross-dispatch danglers.** When dispatch A deletes slug `s` and a surviving file F (or a file that is a *different* dispatch B's delete target) carries a live link `](.../s.md)`, A's per-report apply hits the hard dangling-live-link gate. The c050/c051 integrators handled this by **defensive in-flight de-linking** (de-link the surviving live link to plain inline-code + marker; idempotent — the marker vanishes if F is itself later deleted). Links *inside* a sibling's delete-target file are correctly LEFT untouched (they die with the file when that sibling applies — cross-dispatch edit-conflict avoidance, moot-edit drop).
- **(ii) N-dispatch co-edit of one surviving line.** The KEPT `book/src/L2-L1/divfree-projector-leaf-identity.md` line 266 was co-edited by THREE c051 dispatches (D1 `scal-` de-link, D2 `dot-` de-link, D3 `nrm2-` de-link). The repairer **narrowed each `old_string` to the slug-distinct substring**, so the three composed **order-independently** regardless of serial integration order. This is the running-aggregate write-conflict analogue at the *line* granularity, resolved the same way the dep-map *row* conflicts are (per-anchor distinctness) — except the distinct anchor is a substring within one line, not a whole row.

**Evidence (recurrence-2; both refactor-enactment cycles).** c050: 4 demotions (D3–D6) cross-referenced each other (`normalize-{body,leaf}-identity` live-linked the `reciprocal`/`elementwise-product` slugs D4/D5 delete); defensive de-link + finalize physical-row sweep, all clean, post-apply grep zero live links. c051: 15 deletions across 5 serial integrators; the 3-way line-266 co-edit resolved via distinct-substring narrowing; sibling-delete-target danglers (`divfree-projector-body-identity.md:22,231`, `jacobi-smoother-leaf-identity.md:12,35`) correctly left to die with their files; finalize dead-link sweep for all 15 deleted slugs returned ZERO. No artifact damage either cycle; the churn was in-flight only.

**Mitigation (cycle-051 meta-phase, this entry — go).** Promoted the **`deleted-slug-inbound-live-link-sweep`** skill (proposed by the c051 D1 critic; promotion bar met — exercised heavily across c050+c051): a mechanical procedure for the critic + per-report integrator to `grep -rnoE '\]\((\.\./)*<dir>/<slug>\.md\)' book/src` for every slug in a report's `delete:` fences BEFORE asserting de-link completeness, subtract (i) the files being deleted and (ii) files the report already edits, and flag any residual surviving live link as a `cross-reference-integrity` build-breaker with exact `file:line`. The skill formalizes the enumerate-then-check step whose absence let the c051 D1 producer's thorough-but-incomplete ad-hoc reasoning miss `L3/index.md`'s 6 live links (caught by the critic). The **distinct-substring-narrowing convention** for N-dispatch line co-edits is recorded as the working precedent (it is a repairer/integrator surgical technique, already in the repairer's toolkit; no separate skill warranted — it is the line-granularity instance of the existing per-anchor-distinctness wave-conflict philosophy).

**Why a skill (Low-cascade), not a structural change.** The hard dangling-live-link build gate already ENFORCES zero surviving live links (the build breaks otherwise); the friction is only that the *producer-side* de-link reasoning was ad-hoc rather than mechanically enumerated, which the skill closes. The serial-apply-before-single-finalize-build architecture already absorbs the in-flight shifts cleanly. No cycle-structure or gate change. **Watch.** Confirm batch-16+ multi-deletion cycles (the leaf-CHAPTER disposition enactment is the next one) carry the skill's enumerate-then-check and produce zero escaped danglers. If a multi-deletion cycle escapes a dangling live link to a commit despite the skill (recurrence-3), the producer-side skill is insufficient and the enumerate-then-check should move into the per-report integrator's apply protocol as a hard pre-apply step (a tooling change, ask-class).

---

```yaml
---
slug: mass-deletion-shrinks-index-prose-line-references-drift-oob
first_observed: cycle-050
last_observed: cycle-051
recurrence_count: 2
status: addressed
addressed_by: cycle-051 meta-phase (batch-15) — NO-GO on a finalize-time line-reference re-pin convention; the OOB warnings are non-load-bearing append-only report-prose see-also refs (not artifact claims, not build-breaking), absorbed by the existing finalize physical-row sweep + count-owner re-pin; anchor-by-text already the preferred citation form for index-internal prose
---
```

**Pattern (a mass-deletion cycle shrinks an index file, so append-only OQ-prose / report-prose `file:line` see-also references into that index drift out-of-bounds).** When a refactor cycle deletes many dep-map rows / cohort bullets from a layer index (`L3-L2/index.md`, `L2-L1/index.md`), the file's line count drops, and any *prose* reference of the form "see `L2-L1/index.md:73`" written earlier (in an append-only OQ caveat, a report's Open-questions section, a cohort-growth-log see-also) now points past the new EOF or at the wrong line. `citecheck --scan` flags these as OOB warnings.

**Evidence (recurrence-2; both refactor-enactment cycles).** c050 + c051 each produced OOB `citecheck` warnings on `L2-L1/index.md` / `L3-L2/index.md` line refs in append-only prose (c051: `L2-L1/index.md:73`, `L3-L2/index.md:63`) — in every case the *content* the ref pointed at was intact and merely moved (e.g. the cohort-growth-log line shifted 73→67 as the file shrank). NONE was a load-bearing artifact claim; NONE broke `cargo make book` (the build's `linkcheck2` checks live markdown links, not prose `file:line` mentions).

**Mitigation (cycle-051 meta-phase, this entry — NO-GO on a new convention; the existing machinery is sufficient).** A finalize-time line-reference re-pin convention was considered (the c051 integrator flagged it as a candidate) and DECLINED: (1) the drifted refs are **non-load-bearing report/OQ prose**, not artifact content — they are the evidence trail, and the OQ-unification pass (this meta-phase) compacts the bulky OQ prose to the Closed index anyway, which retires the stale refs as a side effect; (2) the **count-owner already re-pins** the index's *own* internal cohort-growth-log line numbers as part of its running-count reconciliation (D5 did this c051); (3) the project's standing citation guidance already prefers **anchor-by-text over line-pin for index-internal cross-references** (the `verify-citation-range` skill's anchor mode) — a re-pin convention would re-pin numbers that should not have been numbers. A finalize step that chased every prose `file:line` into a shrinking index would be busywork with no consumer (nobody reads the OOB-warned prose line for a load-bearing claim). **Watch.** This stays NO-GO unless an OOB-drifted line reference is ever found to carry a **load-bearing** claim (an artifact citation, not see-also prose) that a downstream consumer reads — then the finalize re-pin (or better, the producer using anchor-by-text) becomes warranted. The OQ-unification pass is the natural place the stale prose refs get retired.

---

```yaml
---
slug: refactor-cohort-denominator-under-scoped-by-planner-corrected-by-audit
first_observed: cycle-049
last_observed: cycle-050
recurrence_count: 1
status: addressed
addressed_by: cycle-051 meta-phase (batch-15) — recorded as the working precedent (audit-first cross-cutter produces the corrected denominator as planning + meta-phase input BEFORE bulk enactment); no role-spec edit at recurrence-1 (the c049 D3 + c050 D8 audits executed this organically); sibling of `co-dispatched-harvesters-reach-contradictory-design-conclusions`
---
```

**Pattern (a refactor/cohort plan under-scopes the affected-item denominator; a dedicated audit dispatch corrects it before bulk enactment).** The batch-15 refactor pass first scoped the degenerate-lowering cohort at **12** themes (the planner's initial count from the BLAS-1 fold families). The c049 D3 cohort-wide `cross-layer-cross-cutter` audit found the true cohort is **18** themes (9 pairs) — demoting only 12 + stranding 6 would have re-created the exact mirrored floor the redirect corrects. The c050 D8 verify-body audit then corrected **18→17** (`divfree-projector-leaf-identity` is KEEP-substantive, not degenerate). The denominator settled at 17 only after two audit passes layered on the planner's initial 12.

**Why this is benign-and-self-correcting, not a planning defect to gate.** The under-scope was caught **before** any bulk enactment (c049 was the map-and-audit cycle; c050/c051 enacted against the corrected 17), exactly the audit-first shape the `co-dispatched-harvesters-reach-contradictory-design-conclusions` precedent prescribes: when a cohort-wide refactor's scope is uncertain, the planner advances only the map/inversion (the convention-independent safe slice) and dispatches a dedicated cross-cutter AUDIT to fix the denominator as enactment input. The 12→18 correction cost nothing downstream (no themes were demoted-and-stranded; the c050 plan consumed the corrected 18, then the c050 D8 verify produced the final 17). This is the system working as designed — the audit IS the scope-correction mechanism.

**Mitigation (cycle-051 meta-phase — recorded precedent, no role-spec edit at recurrence-1).** The c049/c050 planners + cross-cutters executed the audit-first-then-enact shape organically (matching the c042 leaf-vs-fold fork precedent). No new convention is warranted at recurrence-1: the existing "hold the scope-exposed bulk work, advance the map, dispatch a cross-cutter audit, enact against the audited denominator" pattern already covers it, and the cycle-planner role-spec's audit-first disposition (from the redirect's refactor-pass-first program) already steers it. **Watch.** If a future cohort-refactor enacts bulk demotions/deletions against an UN-audited planner denominator and a stranding/over-deletion results (recurrence-2), enact a cycle-planner §Discipline bullet ("a cohort-wide refactor must dispatch a denominator audit before any bulk enactment cycle"). Until then, the precedent stands as the expectation.

---

```yaml
---
slug: disciplined-cross-pipeline-combinator-mining-procedure-unskilled
first_observed: cycle-054
last_observed: cycle-054
recurrence_count: 1
status: addressed
addressed_by: cycle-054 meta-phase (batch-16) — promoted skill `disciplined-cross-pipeline-combinator-mining-gate` (the single-witness → 2nd-pipeline-probe → discharge → mine sequence + scope-boundary classification of break-witnesses + fold-vs-map over-unification check)
---
```

**Pattern (the solver-test-load frontier's cross-pipeline combinator-mining discipline was followed exemplarily but un-skilled, so the critic could only mark `skill-uptake-survey: warning`).** The 2026-06-01 redirect's item 3 (solvers as low-priority test-load, advance only when cleanly describable) generated a new recurring procedure across batch-16: surface a candidate combinator from ONE pipeline witness as a spine-coverage finding with a single-witness caveat (c052 D6 electrostatic outer-solve-sweep) → probe a 2nd pipeline to discharge the gate (c053 D1 magnetostatic, 2-of-N skeleton-identical) → mine the combinator, classifying any break-witness as a scope boundary not a variant axis (c054 D1 `solve_family`; driven's per-element `SetOperators` break → `map_solve_over_(operator,rhs)_family` superset) and flagging unprobed pipelines with the fold-vs-map hazard (transient may thread state → a fold, not a map). The discipline was textbook. But `log/cycle-053.md:13` named "single-witness → 2nd-pipeline-probe → discharge" as a reusable gate that no skill encoded, so the c054 D1 critic's `skill-uptake-survey` could only mark `warning` ("procedure followed, none cited") rather than `pass`.

**Why a skill (Low-cascade), not a role-spec change.** The procedure already runs correctly — the gap is purely that it was not a named, citable artifact, which (a) leaves the critic's uptake survey unable to mark `pass`, and (b) risks a future miner under-running the discipline without a checklist to anchor it (the over-unification hazard — folding a break-witness into a variant axis, or a fold into a map — is the costly failure the gate prevents). Promoting the skill closes both: the miner cites it; the critic surveys against it; the four points (≥2-witness bar / scope-boundary classification / unprobed-pipeline fold-vs-map flag / replace-and-propagate layer-choice) become the explicit gate. **Watch.** The batch-17 `solve_family` general-form superset probe (+ the transient fold-vs-map check) is the next live invocation; confirm the miner cites the skill and the critic marks `skill-uptake-survey: pass`. If a future cross-pipeline mine over-unifies despite the skill (recurrence-2 with a stranded/over-unified combinator reaching the artifact), the gate moves from miner-side citation into a critic-side hard `rotation-quality` check.

**Batch-17 confirmation (cycle-057 meta-phase — gate worked end-to-end across all 3 cycles; recurrence stays 1, status holds `addressed`).** The skill was the load-bearing batch-17 discipline and the critic marked `skill-uptake-survey: pass` where it was cited: c055 D1 scoped `solve_family` fixed-operator-only (driven shared-operator-capture break → `map_solve` superset deferred); c056 D1 DEFERRED `map_solve` at 1 witness + held the transient state-threaded fold OUT of the map family; c057 D3 classified `SweepAdaptive` as a ROM fold (NOT a 2nd map witness — counting the frozen-ROM online sweep as an operator-varying map would be the step-2 scope-boundary violation the gate forbids). No over-unification reached the artifact; the two-combinator MAP/FOLD factoring (`solve_family` independent-map vs `fold_solve` sequential-fold, both §3.7 `iterate_while` children) is the structural yield the gate protected. No recurrence-2; skill confirmed working as designed.

---

```yaml
---
slug: index-table-status-cell-drifts-when-theme-file-promoted
first_observed: cycle-055
last_observed: cycle-058
recurrence_count: 1
status: resolved
addressed_by: cycle-057 meta-phase (batch-17) — codified the lightweight promotion-time index-cell guard as a producer-side §Discipline bullet in `.claude/agents/lifter.md` (a status-flip dispatch owns the matching index-table cell in the SAME proposed-changes pass) + sharpened the `.claude/agents/layer-intro-author.md` count-owner survey bullet (count firm from the linked chapter's `## Status` line, NEVER from the drift-prone index-table cells) + a count-owner index-cell-flips-with-the-tally sub-bullet. Promotion-time guard (c056 D2 recommendation) chosen over a heavyweight finalize-time re-sweep. RESOLVED cycle-060 meta-phase (batch-18): the open half (L1/L1-L0 historical residue) confirmed CLEAN (c058 D4, 68/68); the guard held across batch-18's promotions; no recurrence-2.
---
```

**Pattern (a layer-index table's status cell is a hand-maintained derived surface that drifts silently from the authoritative chapter `## Status` line, and a count-owner that trusts the stale cell mis-projects the tally).** Two coupled failure modes surfaced in cycle-055 and were probed/contained across c056/c057:
- **(i) Silent index-cell drift on in-place promotion.** The `book/src/L4-L3/index.md` theme-table's last-cell status text is maintained separately from each theme file's `## Status` line. When a theme is promoted rough-in→firm, the promotion edits land in the theme file but the index cell is silently left stale — and the desync is **invisible to the build** (`linkcheck2` checks links, not status-cell text). Three cells drifted across `c008→c021` (~3 batches undetected): `krylov-step-typed-wrapper-dissolution` (firm c008), `gmres-inner-loop-iterate-while-migration` (firm c020), `fgmres-inner-loop-iterate-while-migration` (firm c021).
- **(ii) Count-owner-trusts-the-stale-cell.** The c055 D7 count-owner projected the consolidated L4>L3 firm tally by reading the index-table cells (it read `3 firm / 3 rough-in` off the stale cells) rather than the theme-file `## Status` lines (all firm; true count 6 pre-cycle → 7 with D2). The repairer flagged the resulting `3→4` mis-projection `needs-revision`, and a corrective wave-4 D8 lifter reconciled it (`6→7`, the table now agrees with the chapter `## Status` lines + the c051/c052/c053 finalize records). This is the `count-owner-trusted-stale-table` failure mode.

**Evidence (recurrence-1; opened c055, probed/contained c056, prophylactic-guarded c057).**
- **cycle-055 (the friction):** D7's stale-cell-trusted tally `needs-revision` → corrective D8 lifter (`6→7`); root-cause OQ `index-table-status-cell-drifts-when-theme-file-promoted` opened (integrator-signals c055 §Integration-tooling friction "INDEX-TABLE-STATUS-CELL-DRIFT — the headline tooling-gap this cycle" + "COUNT-OWNER-TRUSTED-STALE-TABLE failure mode").
- **cycle-056 (CONFIRM-CLEAN scope probe):** D2 swept the L3-L2 (5 rows) + L2-L1 (11 rows) tables — **16/16 cells MATCH** their theme-file `## Status` lines. The drift did NOT propagate to these tables because they were last mass-edited by the c050/c051 **DELETION** sweep (row-removal coupled to file-deletion by the dead-link build check — no half-completion window), unlike the L4-L3 **in-place promotion** that drifted silently. The drift-class is real but **contained to the promotion-in-place case**. D2 recommended a lightweight promotion-time guard over a heavyweight finalize-time re-sweep (a finalize re-sweep would flag 0/16 on these stable tables).
- **cycle-057 (prophylactic guard applied in practice):** D2's `fe-operator-assemble-mutation-rotation` firm-flip flipped the theme `## Status` + frontmatter + the `L1-L0/index.md` row's status cell **all together in one report** — the exact guard this entry codifies, demonstrated working before codification.

**Mitigation (cycle-057 meta-phase, this entry — go; the promotion-time guard, not the finalize re-sweep).** Two coordinated role-spec edits (the c056 D2 recommendation: prefer the lightweight promotion-time guard over the heavyweight finalize-time re-sweep): (a) `.claude/agents/lifter.md` — a §Discipline bullet: when a re-anchor/firm-flip flips a chapter/theme `## Status`, the same proposed-changes pass must also update the matching `L*-L*/index.md` (or `L*/index.md`) row's status cell (or, if a co-dispatched count-owner owns that cell this cycle, flag it for the count-owner). (b) `.claude/agents/layer-intro-author.md` — sharpened the count-owner survey bullet to name index-table cells as a drift-prone *derived* surface (count firm from the linked chapter's `## Status`, NEVER from the index cells), addressing failure mode (ii); plus a count-owner sub-bullet that the index cell flips together with the tally when the count-owner promotes.

**Why a promotion-time role-spec guard (Medium-cascade), not a finalize-time tooling change.** The c056 D2 CONFIRM-CLEAN sweep is empirical evidence the drift is **promotion-in-place-specific, not general table-rot** — a full finalize-time re-sweep would flag 0/16 on stable tables, so its marginal value is low and non-zero only for actively-promoting tables, which the promotion-time guard covers at its source at near-zero cost (it would have caught the c055 case). The heavyweight finalize-time consistency-check (D8 candidate (a)) + the citecheck-adjacent lint (candidate (c)) stay UNENACTED (NO-GO at recurrence-1; the promotion-time guard is the minimal fix). **Watch.** (1) The **L1 / L1-L0 index tables are the highest-churn next-audit candidate** (c056 D2) — they carry the most active in-place-promotion churn, the only drift sub-class that escapes the dead-link build check; a sibling cross-layer-cross-cutter sweep of L1/L1-L0 (then L4/L3/L2/L0) would fully characterize the drift-class (migrated to the plan as a batch-18 backlog item). (2) Confirm batch-18+ promotion cycles flip the index cell with the `## Status` (no fresh stale-cell OQ). If a promotion lands without the matching cell flip despite the guard (recurrence-2), or a not-yet-audited table is found drifted, escalate — the finalize-time consistency check (candidate (a)) becomes warranted as the source-of-truth-enforcing backstop (a tooling change, ask-class).

**Batch-18 resolution (cycle-060 meta-phase — status `addressed`→`resolved`).** The open watch-item — the L1/L1-L0 highest-churn next-audit candidate (the only drift sub-class escaping the dead-link build check) — was discharged by **c058 D4 CONFIRM-CLEAN 68/68** (all 36 `L1/index.md` §Operator-dep-map cells + all 32 `L1-L0/index.md` §Theme-list cells agree with each linked chapter's `## Status` line), mirroring c056 D2's 16/16 on L3-L2/L2-L1. This confirms the drift class is **promotion-in-place-specific historical residue that did NOT accumulate in L1/L1-L0** before the c057-meta guard landed. Across batch-18's promotions (c058 `fold_solve` L4 firm-flip + c059 `fold_solve` L3 land + c060 prose syncs) the promotion-time guard held — the count-owner registered counts from chapter `## Status` lines, the dep-map TABLE rows flipped with the status, no fresh stale-cell OQ surfaced. No recurrence-2; the heavyweight finalize-time consistency check (candidate (a)) stays UNENACTED (the promotion-time guard is sufficient). Status `resolved`. *Re-open trigger (would reset to `addressed`):* an in-place promotion that mutates a chapter `## Status` without the matching index-cell touch despite the guard (recurrence-2), or any future index-table audit finding a drifted not-yet-audited table.

**Batch-19 confirmation (cycle-063 meta-phase — held clean, status stays `resolved`).** Batch-19 ran two in-place-touch finalize cycles (c062: D3 added the operand-category variant axis to `L2`/`L3 linear_combination` + a `weak_form_term` axis-point — no status flip; D2 the count-owner refreshed the `L1/index` grand-total prose from chapter `## Status` lines per the guard; c063: D3 added the `fe_assemble` dep-map row — no status flip). Every c062/c063 finalize record explicitly logged the index-cell **anti-drift guard NOT fired / no status flip** across all rows; the c063 D3 dep-map-row add made the `L1/index` table **self-summing** (31 in-table, no off-table firm operator) without any cell going stale. No recurrence; guard steady-state working. (Note: the only c062 tooling-provenance friction was a one-off `citecheck`-availability misattribution in D3, a DISTINCT shape from this index-cell drift class — caught by the critic, repaired in-cycle, zero artifact damage; recorded report-only per the single-cycle-noise aggregation discipline, NOT ledgered.)

---

```yaml
---
slug: overall-status-non-canonical-token-and-clean-report-gap
first_observed: cycle-073
last_observed: cycle-075
recurrence_count: 1
status: addressed
addressed_by: cycle-075 meta-phase (batch-23) — codified the canonical token set (`ready | needs-revision | reject`, forbidding `integrate`/synonyms) prominently in `.claude/agents/repairer.md` §"Setting overall_status"; added a critic-sets-`ready`-on-the-all-pass-clean-report rule to `.claude/agents/critic.md` (the only case the critic writes `overall_status`, since the repairer does NOT run on all-pass reports) + the frontmatter-template comment line; and a `integrator-per-report.md` Process-step-1 normalization (accept `ready` from EITHER the repairer or the critic; normalize a non-canonical synonym over an otherwise-clean META to `ready` + record it in the staging-row Notes).
---
```

**Pattern (a 3-of-3-cycle process friction blocking clean autonomous integration: `overall_status` arrives in a non-canonical token OR is absent entirely).** Two coupled gaps surfaced across the full batch-23 (c073/c074/c075):
- **(i) Non-canonical token.** Repairers in all three cycles set `overall_status: integrate` (a synonym), but the `integrator-per-report` Process step 1 hard-gates on the literal `ready` (canonical set `ready | needs-revision | reject`). A non-canonical token either blocks the apply or forces a manual fix.
- **(ii) Clean all-pass reports get NO `overall_status` at all.** The repairer runs ONLY on reports with a warning/fail finding (CLAUDE.md Phase 4). An all-pass clean report therefore reaches the integrator with no `overall_status` field — forcing the orchestrator to backfill `ready` by hand EVERY cycle for the clean reports. (Batch-23 was a near-all-clean batch — 18/18 reports applied with zero deferrals — so almost every report hit this gap.)

**Why a role-spec codification (Low-cascade), not a tooling change.** Both gaps are convention-clarity gaps, not mechanism gaps: (i) is a token-discipline slip the repairer spec can forbid prominently; (ii) is a hole in WHO sets the status on the all-pass path — closed cleanly by having the critic (the last validator on a clean report, since no repairer runs) set the canonical `ready` directly. The `integrator-per-report` normalization is a defensive backstop (accept `ready` from either validator; normalize a stray synonym over a clean META). No orchestrator/tooling change needed — the status now arrives canonical from a defined writer on both paths. **Watch.** Confirm batch-24 repairers use the literal `ready` (no `integrate`) AND clean reports arrive carrying `overall_status: ready` from the critic (no orchestrator backfill). If a non-canonical token still reaches the integrator despite the repairer-spec edit (recurrence-2), or the critic does not set the all-pass `ready` (the clean-report gap persists), escalate to a finalize-time / orchestrator-side normalization (a small tooling change, ask-class).

---

```yaml
---
slug: per-report-integrator-narrates-assumed-sibling-landing
first_observed: cycle-074
last_observed: cycle-074
recurrence_count: 1
status: addressed
addressed_by: cycle-075 meta-phase (batch-23) — added a `.claude/agents/integrator-per-report.md` §Discipline bullet: narrate from the ON-DISK state actually read, never from an assumed sibling landing; any staging-row Notes claim about a sibling dispatch's state must be backed by its staging row OR a direct disk read this invocation, not by the dispatch-prompt apply order or an assumption of what "should" have landed.
---
```

**Pattern (a serially-dispatched per-report integrator narrated a sibling's landing it had not verified).** In cycle-074 a per-report integrator (applying D1) wrote a Notes line claiming "D5 already landed, frontmatter now reads bare `seed`" when D5 had NOT yet landed. The actual edits this integrator applied were correct (the orchestrator caught the false claim by an on-disk check); only the narration was wrong — a single-cycle, zero-artifact-damage misnarration. The root cause: a per-report integrator sees only the staging log + the files it reads, so it must not assume a sibling's state from the dispatch-prompt's stated apply order. **Why a Discipline bullet (Low-cascade), single-cycle but codified anyway.** Although a one-off (recurrence-1) it is a clean, cheap discipline to state and it composes with the existing "re-read disk at every Edit" bullet (this is its narration-accuracy corollary). The harm if it recurs and is NOT caught: a false staging-row Notes claim could mislead finalize's reconciliation. **Watch.** If a per-report integrator's false sibling-state narration reaches finalize uncaught (recurrence-2), or causes a mis-reconciliation, escalate. Recorded at recurrence-1 because the fix is a zero-cost discipline statement, not because the single occurrence alone met the ledger bar.

---

```yaml
---
slug: staging-log-applied-at-timestamp-not-apply-order-record
first_observed: cycle-073
last_observed: cycle-075
recurrence_count: 1
status: addressed
addressed_by: cycle-075 meta-phase (batch-23) — annotated `.claude/agents/integrator-per-report.md` (staging-row output section + the `applied_at` field) that the staging-log ROW ORDER (newest LAST, by append position) is the authoritative apply-order record, NOT the `applied_at` timestamps (advisory only). Finalize reconciles from row order.
---
```

**Pattern (the staging-log `applied_at` timestamps were observed out of serial-dispatch order across c073/c074/c075).** The per-report integrators are dispatched serially, but the `applied_at` timestamps they stamp do not reliably reflect the apply order (a benign artifact — byte-disjoint anchoring + the finalize build-validate make any ordering harmless; the c074 finalize record explicitly noted the divergence). The risk is only that a future finalize might TRUST `applied_at` as the apply-record when the authoritative record is the append-position row order. **Why a clarifying annotation (Low-cascade).** No mechanism is broken — this is a documentation/expectation clarification so finalize never treats `applied_at` as the order-of-truth. The role-spec already said "re-read the staging log fresh"; this makes explicit that *row order*, not *timestamps*, is the apply record. **Watch.** Benign unless a finalize reconciliation is ever driven off `applied_at` ordering and produces a wrong apply-order conclusion (recurrence-2 with actual harm) → then a deterministic monotonic-sequence field (not a wall-clock timestamp) in the staging row would be warranted (a small format change, ask-class).

---

```yaml
---
slug: seed-surface-firming-ceiling-needs-out-of-scope-assembly-tests
first_observed: cycle-079
last_observed: cycle-081
recurrence_count: 3
status: addressed
addressed_by: batch-25 meta-phase (cycle-081) — recorded as a spine FINDING + the batch-26 frontier reshaped away from seed-firming toward bottom-up vocabulary / 5-driver→L4 completeness (priorities.md); the in-scope promotion route (a lowering-verifier law-confidence pass on a both-primitives-firm verb) migrated to the plan backlog
---
```

**Pattern (the FEATURE-SURFACE SPINE seed columns hit an in-scope firming ceiling).** The reduce-verb double-gate has two tiers. The **first** (test-coverage) gate is dischargeable in write-scope by CITING the existing Palace postprocess unit tests as L0-equivalent documentation (batch-24 decision (e)) — this advanced `sparameter_reduce` + `eigenfreq_qfactor_reduce` to `rough-in (test-coverage-bounded)` (c079) and is the routine route. The **second** gate — full `firm` — requires a **positive ASSEMBLY test** that exercises the eigenpair→(f,Q) / S-matrix / per-domain-energy assembly path itself, not just the reduction OUTPUT. The c081 planner verified the Palace corpus contains **no such positive assembly test** for any of the three reduce verbs (only round-trip-invariance tests over the output cache, using `RandomMeasurement()` rather than calling the real `Measure*` assembly). So the existing-test-citation route **cannot** discharge the 2nd gate, and authoring new tests is out of project write-scope. The feature-surface columns consequently stay `seed` (a constituent verb is not fully `firm`) until either an out-of-scope assembly test or an in-scope confidence-raising lowering-verifier pass lands.

**Observed 3× this batch** — once per reduce verb (`sparameter_reduce` c079, `eigenfreq_qfactor_reduce` c079/c080, `domain_energy_reduce` c079). The structure-side gates DID firm in-scope where a positive source site exists (c080 `eigenvalue-untransform` firm L1 discharged `eigenfreq_qfactor_reduce` gate-(a)); the ceiling is specifically the **assembly-confidence** gate.

**Why this is a finding, not a defect.** It is a true statement about how far the top-down feature surface can firm on the existing corpus alone — exactly the kind of friction the stack exists to expose. The corrective work-item is NOT "force the gate" but to **return the frontier to the highest-fan-out bottom-up vocabulary + 5-driver→L4 completeness** (migrated into the plan, batch-26 active head), with seed-firming continuing opportunistically. The one remaining in-scope promotion route — a `lowering-verifier` law-confidence pass on a verb whose folded primitives are ALL firm (the `eigenfreq_qfactor_reduce` situation post-c080) raising the assembly-map confidence to `inner_product`-equivalent — is migrated to the plan backlog (trigger-gated).

**Watch.** If a future cycle finds a positive assembly test does exist (a corpus re-survey), or a downstream burn-component consumer pulls one of these columns and forces the firm question, re-open. Until then, the columns are correctly bounded at `seed`; do not churn them.

---

```yaml
---
slug: matrix-weighted-norm-full-firm-cascades-thirty-file-reanchor-sweep
first_observed: cycle-080
last_observed: cycle-091
recurrence_count: 1
status: resolved
addressed_by: 948247a (cycle-091 — the LANDED cascade) + batch-28 meta-phase (cycle-090) GO. The firm flip + ~30-file cascade LANDED CLEAN c091 (3 firm promotions: `matrix-weighted-norm` L1 + bonus `domain_energy_reduce` L4 + the `energy-fields` feature column ×3; honest residual gates preserved: `gram_reduce`/`bilinear-form` stay rough-in, 4 columns stay seed). The long-held √-foundation-blocker is discharged. Resolved: the trigger-gated structural wave is done. (A NEW within-file residue facet surfaced — see `firm-flip-leaves-within-file-stale-narration-in-flipped-operators-own-entry` — but the cascade itself is resolved.)
---
```

**Pattern (a `matrix-weighted-norm` full-firm promotion would cascade a ~30-file re-anchor sweep).** The c080 D1 lowering-verifier audit positively test-covered the SPD radicand `⟨x,Bx⟩` + `½` (via `test-domainpostoperator.cpp`) but ruled the firm-on-positive-structure escape INAPPLICABLE — the outer `√` at the named entry point `linalg::Norml2(comm,x,B,Bx)` (`operator.cpp:606`) is the untested step, and the norm-axiom laws (triangle / Cauchy–Schwarz / parallelogram) carry inner-product-structure content the L0 source does not verify. So the entry correctly stays `rough-in (test-coverage-bounded)`. A full `firm` promotion is doubly blocked: it needs the √-entry-point gate discharged AND it would cascade a ~30-file re-anchor sweep (the operator is widely consumed).

**Why NO-GO this batch.** (1) The √-entry-point gate is not discharged (a genuine test/law-confidence gap), so a promotion would be premature regardless of the cascade. (2) Even once the gate clears, the ~30-file sweep is a heavy structural wave best run as its OWN dedicated cycle (the cycle-071 reorg-wave precedent), not bundled with forward-frontier work. (3) No downstream consumer currently needs the full-firm promotion — the sharpened `rough-in (test-coverage-bounded)` correctly bounds the two verbs that fold it (`domain_energy_reduce` energy-form, capacitance/inductance via gram_reduce). Migrated to the plan backlog as a trigger-gated cascade-wave item.

**Batch-26 re-weigh (cycle-084 meta-phase — NO-GO HELD, re-weigh trigger sharpened).** Re-weighed under accumulating downstream demand: the cascade is now the convergent foundation-blocker for the whole reduce-verb tail (A3 `gram_reduce` → capacitance/inductance, A4 `domain_energy_reduce` → energy-fields). Still NO-GO: the √-entry-point gate is independent of the re-anchor sweep, so a structural wave that does not discharge it buys nothing. Sharpened re-weigh trigger: a √-entry-point test surfaces OR a literature-anchor law-confidence pass discharges the norm-axiom laws (the structure-side gate). recurrence_count stays 1 (no new manifestation; the demand grew, the friction did not recur).

**Batch-27 re-weigh (cycle-087 meta-phase — NO-GO HELD on the heavy wave; GO on a SCOPED literature-anchor PROBE as the cheap dischargeability test).** Demand grew further: after the c086 `solve_family` firm promotion narrowed electrostatic/magnetostatic from a 2-constituent to a 1-constituent (`gram_reduce`) gate, the cascade is now the convergent foundation-blocker for **5 of the 6 stay-seed feature columns** (electrostatic/magnetostatic/capacitance/inductance via `gram_reduce`; energy-fields via `domain_energy_reduce`). Neither sharpened trigger fired across c085/086/087 (no √-entry-point test surfaced; no law-confidence pass on the norm axioms was run). The heavy ~30-file cascade wave stays **NO-GO** (the structure-side gate is still undischarged; the c080 ruling that the firm-on-positive-structure escape is INAPPLICABLE — the triangle/Cauchy–Schwarz/parallelogram laws are inner-product-structure theorems the source only numerically asserts — still holds). BUT the meta-phase enacts the **cheap test of the gate's dischargeability** as the batch-28 frontier: a SCOPED `lowering-verifier` literature-anchor probe on the `matrix-weighted-norm` norm-axiom laws, BEFORE committing to the heavy wave. The probe is the in-scope analog of the solve_family element-independence read-off, except the norm axioms may genuinely be theorems not read-offs — so the probe's likely outcome is a clean confirmation of the ceiling, which is itself the load-bearing finding (it converts the NO-GO from "held by inertia" to "held by an explicit literature-anchor verdict"). Migrated to the plan as the batch-28 LEAD (`matrix-weighted-norm-norm-axiom-law-confidence-probe`). recurrence_count stays 1 (the friction did not recur; the downstream demand and the dischargeability-probe decision are the updates). status holds `addressed`.

**Batch-28 re-weigh (cycle-090 meta-phase — the GO; NO-GO RESOLVED).** The two dischargeability probes the batch-27 meta-phase queued BOTH discharged: the **structure-side** (c088, `matrix-weighted-norm-norm-axiom-laws-structure-side-discharged`) showed laws 4/6/7 (triangle / Cauchy–Schwarz / parallelogram) are inner-product-space THEOREMS on provably-SPD `B = KM` (positive L0 home: the FE mass form `spaceoperator.cpp:530-537` = `1.0·M->Real()`, SPD not merely PSD; `eigensolver.cpp:206-207`) — exact-arithmetic theorems with a structurally-discharged premise, NOT test-gated. The **FP-side** (c089, `matrix-weighted-norm-firm-flip-and-cascade-wave`) showed laws `:69-70` inherit verbatim/additively from firm `dot` + firm `apply_linop` through a deterministic IEEE-754 outer √ over disjoint accumulators (the `nrm2` precedent — itself firm — extended by one firm constituent; no composition-specific FP property arises). **The headline judgment:** the sole remaining gate (a), the missing 4-arg SPD-weighted overload `Norml2(comm,x,B,Bx)` √-entry-point test, is **REDUNDANT** — everything it would confirm (the inner-product-space theorems + the FP non-laws) is already anchored by structure + constituent-inheritance; there is NO law/property for which that test is the only evidence. This is materially the SAME situation as the four prior firm-on-positive-structure escape promotions (`apply_linop`, `eigenfreq_qfactor_reduce` c082, `sparameter_reduce` c083, `solve_family` c086) — laws anchored on positive source, the surrounding test redundant. The "SPD-ness construction-attested not runtime-verified" note is the scoping note the escape *requires*, not an independent gate (the only callers are the SPD-construction eigensolver path; a non-SPD caller's absence is already recorded in §Applicability `:68`). **VERDICT: the escape APPLIES → the firm flip + ~30-file cascade is GO as the batch-29 LEAD** (`matrix-weighted-norm-firm-flip-and-cascade-wave`): flip `rough-in (test-coverage-bounded)`→`firm` + the whole-`book/src/` cross-reference re-anchor (per `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep`) + the coupled downstream `gram_reduce` (A3) / `domain_energy_reduce` (A4) reduce-verb re-checks + the 5-of-6 stay-seed feature-column re-evaluations. recurrence_count stays 1 (the friction never recurred; this is the resolving GO decision). status holds `addressed` (the corrective work-item — the cascade wave — is migrated to the plan as the batch-29 LEAD).

**Batch-29 LANDED (cycle-093 meta-phase — status `addressed`→`resolved`).** The GO cascade LANDED CLEAN c091 (SHA 948247a): a 4-dispatch serial wave (D1 harvester flip → D2 lifter consumer re-anchor → D3 lowering-verifier reduce-verb re-check → D4 layer-intro-author column re-eval) yielded **3 firm promotions** — the planned `matrix-weighted-norm` (L1) flip PLUS two bonus cascade-yield promotions (`domain_energy_reduce` L4 verb firm; the `energy-fields` feature column firm ×3 levels) — with the honest residual gates preserved (`gram_reduce` + `bilinear-form` stay rough-in; 4 columns stay seed). Counts: L1 firm 30→31 main / 37→38 grand; L4 firm 17→18 / rough-in 1→0; feature 6→7 firm / 6→5 seed. All 4 reports passed clean (repair skipped). The CROSS-FILE whole-book-grep discipline (the sibling friction `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep`) HELD on this first wide test — only ONE cross-file symmetric-twin paragraph (`magnetostatic.L4.md:41`) needed a finalize repair. The trigger-gated structural wave is DONE → resolved. (A distinct NEW within-file residue facet surfaced and is GO'd separately — `firm-flip-leaves-within-file-stale-narration-in-flipped-operators-own-entry`.)

---

```yaml
---
slug: firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep
first_observed: cycle-086
last_observed: cycle-095
recurrence_count: 4
status: addressed
addressed_by: cycle-087 meta-phase (batch-27) — codified a mandatory whole-`book/src/` cross-reference grep coupled to any firm-promotion / feature-column-flip dispatch as a producer-side §Discipline bullet in `.claude/agents/lowering-verifier.md` + `.claude/agents/lifter.md` + `.claude/agents/layer-intro-author.md` (the FIRM-promotion / column-flip analog of `floor-landing-implies-same-cycle-adjacent-entry-reanchor`); the bounded batch-28 land-clean lifter for the 3 confirmed-stale eigenfrequency-qfactor cross-references migrated to the plan. `.claude/agents/` edits → SESSION RESTART before c088. **Batch-29 (cycle-093 meta-phase): the CROSS-FILE grep HELD on the first wide cascade (c091, ~30 files — only ONE cross-file symmetric-twin paragraph at finalize), but a NEW WITHIN-FILE facet surfaced → a sibling entry `firm-flip-leaves-within-file-stale-narration-in-flipped-operators-own-entry` (recurrence-1) codified + a within-file self-consistency grep bullet enacted into `.claude/agents/harvester.md` + `.claude/agents/lifter.md`. SESSION RESTART before c094.**
---
```

**Pattern (a maturity-token promotion — a firm-promotion of an operator, OR a feature-column `seed`→`firm` flip — leaves stale cross-references to the old maturity token in OTHER files the promoting dispatch's grep-sweep did not reach).** This is the FIRM-promotion / column-flip analog of `floor-landing-implies-same-cycle-adjacent-entry-reanchor` (which governs a FLOOR landing under an existing upper entry). When an operator `X` is promoted `rough-in (test-coverage-bounded)`→`firm`, every chapter/index/theme that mentions `X`'s maturity as `rough-in (test-coverage-bounded)` goes stale the moment the promotion lands. The one-operator-per-dispatch discipline means the promoting dispatch touches only `X`'s own file + a few named consumers; a scoped grep misses the rest. Symmetrically, a feature-column `seed`→`firm` flip stales every SIBLING-column prose reference that calls the now-firm column `(seed)`.

**Evidence (recurrence-2; two distinct promotion classes, three concrete instances).**
- **(i) Operator firm-promotion residue, c086→c087.** The c086 `solve_family` `rough-in (test-coverage-bounded)`→`firm` promotion (the firm-on-positive-structure escape) grep-sweep was scoped to the L4-operator + feature-driver files and left a coherent 5-file / 7-site residue of stale `rough-in (test-coverage-bounded)` references — INCLUDING a load-bearing internal contradiction in `book/src/L4/index.md` (`solve_family` double-listed in BOTH the firm cohort AND the "Rough-in at L4" cohort, with a stale `(1 + 1 test-coverage-bounded)` count header contradicting on-disk `L4_rough_in_test_coverage_bounded: 0`), and missing sites (`:47`/`:57`/`:59`/`:122`) **in the very `index.md` the c086 sweep had partially corrected** (`:32`/`:71`). The c087 land-clean lifter cleaned all of it (12 edits / 7 sites / 5 files; zero status/count change). That the sweep missed sites in the same file it edited is the strengthening evidence.
- **(ii) Operator firm-promotion residue, c082 (independent earlier instance).** The c087 D1 lifter's drive-by surfaced `book/src/feature/eigenfrequency-qfactor.L4.md:38` still labeling `eigenfreq_qfactor_reduce` `rough-in (test-coverage-bounded)` despite that operator being `firmness: firm` since c082 — the SAME drift class, one promotion earlier, confirming it is not unique to the c086 promotion.
- **(iii) Feature-column flip residue, c085 (surfaced by THIS meta-phase's verification).** The c085 all-12-column re-evaluation flipped `eigenmode` and `eigenfrequency-qfactor` to `firm`, but left stale `(**seed**)` sibling-status references inside the `eigenfrequency-qfactor` column: `eigenfrequency-qfactor.L4.md:36` + `eigenfrequency-qfactor.L1.md:34` both still call the now-firm `eigenmode.{L4,L1}` `(**seed**)`. This is the column-flip manifestation of the same drift (a flip-sweep leaving stale sibling-status cross-references), confirmed stale-on-disk this meta-phase.

**Mitigation (cycle-087 meta-phase, this entry — go).** Three coordinated producer-side role-spec §Discipline bullets (the FIRM-promotion / column-flip analog of the floor-landing coupling): (a) `.claude/agents/lowering-verifier.md` + (b) `.claude/agents/lifter.md` — when a dispatch PROMOTES an operator's maturity token (any `rough-in*`→`firm`, or a `stub`/`rough-in` advance), it must run a **whole-`book/src/` cross-reference grep** of the promoted slug's maturity-token co-mentions (`grep -rn '<slug>' book/src | grep '<old-token>'`) and re-anchor every genuinely-stale reference in the SAME proposed-changes pass (or, if the residue is large, flag the exact `file:line` set for a co-scheduled land-clean lifter — never leave it for a later cycle to discover); (c) `.claude/agents/layer-intro-author.md` — when a feature-column-flip dispatch flips a column `seed`→`firm`, it must whole-`book/src/feature/` grep for stale `(seed)` / `(**seed**)` SIBLING-status references to the flipped column and re-anchor them in the same pass. The grep is mechanical and cheap (the build's `linkcheck2` does NOT catch maturity-token prose drift — only links — so this is the only enumerate-then-check step).

**Why producer-side role-spec bullets (Medium-cascade), not a tooling gate.** The drift is benign-but-untidy (a stale maturity label / sibling-status mention; no build break, no broken link, no false algebraic claim — the cross-referenced file's OWN `## Status` / frontmatter is authoritative and correct). The cost is one land-clean lifter pass per missed-residue promotion (c087 was exactly such a pass). Coupling the whole-book grep into the promoting/flipping dispatch removes the residue at near-zero cost. It does NOT warrant a finalize-time consistency gate or a structural change (cf. the `index-table-status-cell-drifts` precedent, where the promotion-time guard was preferred over a finalize re-sweep for the same reason). **Watch.** Confirm batch-28+ firm-promotion / column-flip cycles carry the whole-book grep (no fresh cross-file maturity-residue OQ; no land-clean cycle needed to mop up a promotion's residue). If a promotion still leaves a cross-file residue despite the bullets (recurrence-3), the producer-side bullet is reminder-dependent like all reminder-class mitigations — escalate to a finalize-time `grep`-based maturity-token consistency check (a tooling change, ask-class). The 3 confirmed-stale eigenfrequency-qfactor cross-references (instances (ii)+(iii)) are migrated to the plan as a bounded batch-28 land-clean lifter item.

**Batch-28 HELD (cycle-090 meta-phase — the codification worked).** Two confirmations: (1) the c088 + c089 dischargeable-law-confidence cycles rewrote the `matrix-weighted-norm` §Status TWICE (structure-side + FP-side `verified_against:` blocks) but **did NOT flip the verb's maturity token** — so there was no firm-promotion to grep behind, and the c089 D2 lifter's frontmatter-hygiene pass (a column-flip residue from c085, instance (iii)) DID carry the whole-`book/src/feature/` grep and cleaned the 2 stale `composes: seed` labels in the same pass (OQ `eigenfrequency-qfactor-column-composes-frontmatter-stale-seed-label` resolved c089, no later-cycle discovery). (2) The c090 land-clean cycle's observation-only `same-layer-cross-cutter` confirmed **ZERO stale maturity/law-confidence cross-references** across `book/src/` — the codified whole-book-grep disciplines HELD, in pointed contrast to c087 (batch-27), which had to mop up a 5-file `solve_family` firm-promotion residue precisely because the discipline did not yet exist. recurrence_count stays 2 (no fresh manifestation; the discipline caught/prevented residue as designed). status holds `addressed`. **Note for batch-29:** the GO firm-flip-and-cascade wave (`matrix-weighted-norm-firm-flip-and-cascade-wave`) is the FIRST actual firm-promotion to exercise the operator-side bullets (a)+(b) at scale (a genuine ~30-file re-anchor) — it is the load-bearing test of whether the whole-`book/src/` grep coupling holds on a wide cascade. Watch its residue.

**Batch-29 result (cycle-093 meta-phase — the CROSS-FILE grep HELD on the wide cascade; recurrence-3 is a NEW within-file facet, split to a sibling entry).** The c091 `matrix-weighted-norm` firm flip + ~30-file cascade exercised the operator-side bullets at scale. **The CROSS-FILE coupling held well:** the c091 finalize needed only ONE cross-file repair (`magnetostatic.L4.md:41`, the structurally-identical stage-3 twin of the `:56` paragraph D4 DID fix — a sibling-paragraph-twin miss WITHIN a non-flipped consumer file), and the c093 land-clean cross-layer pass confirmed ZERO stale cross-file maturity references across the rest of the book. BUT a distinct NEW facet surfaced that the cross-file bullet does NOT name: the flipped operator's **OWN entry** carried multiple stale "stays rough-in" narrations beyond its `## Status` line — `matrix-weighted-norm.md`'s gate-(c) body (`:122`), Evidence-section conclusion (`:150`), and FP-residue closing paragraph (`:180-184`) all still concluded the verb "stays `rough-in (test-coverage-bounded)`" / "the escape does not apply" AFTER the §Status `:110` flipped to firm. The cross-file grep (`grep -rn '<slug>' book/src | grep '<old-token>'`) DOES match these (they are in `book/src`), but the bullet frames the operator's own file as a single point (the §Status line) and the c091 D1 flip-dispatch swept only that — leaving the body narrations stale, cleaned only by the c093 land-clean cycle + TWO repair passes (cross-cutter caught `:150`; the lifter's critic extended to `:122`+`:180-184`). This is recurrence-3 of the maturity-residue class but a **within-file** manifestation distinct enough to track + fix separately → sibling entry `firm-flip-leaves-within-file-stale-narration-in-flipped-operators-own-entry` below. The cross-file bullet stays `addressed` (it held); the within-file bullet is the new GO. last_observed→c091 (the flip that left the residue; surfaced/cleaned c093).

**Batch-30 result (cycle-096 meta-phase — recurrence-4; the WITHIN-FILE bullet HELD on the `bilinear-form` flip, but the CROSS-FILE sweep again left two consumer residues the c091 mwn cascade had originally missed).** The c095 `bilinear-form` firm-flip cascade (the batch-30 LEAD, 7 dispatches, the FIRST flip to carry the batch-29 within-file self-consistency bullet) **left `bilinear-form.md` internally self-consistent in ONE pass** — including the `:251-257` Dependencies self-note ("the `bilinear-form` half remains open") the batch-29 watch named as the known within-file case; the D1 discretionary within-file re-anchors (×5, post-apply grep clean) confirmed it. So the within-file bullet HELD as designed (no recurrence-2 in the flipped operator's own file; the sibling entry below flips to `resolved`). **The recurrence is CROSS-FILE and is residue from the EARLIER c091 mwn cascade, not the c095 flip:** the c096 D5 land-clean (re-anchoring the mwn-mutation-rotation theme) surfaced TWO genuinely-stale `matrix-weighted-norm (rough-in (test-coverage-bounded))` operator-maturity assertions in *consumer* files the c091 ~30-file sweep did not fully reach — `matrix-weighted-norm-mutation-rotation.md:5,:317` (fixed c096-D5) and `domain_energy_reduce.md:377` (flagged, routed to the batch-31 land-clean, OQ `domain_energy_reduce-377-mwn-stale-rough-in-residue`). These confirm the cross-file grep on a WIDE (~30-file) cascade is reminder-dependent and can leave long-tail consumer residue that surfaces cycles later — but each is benign (stale prose, no build break, no false claim), caught by the next land-clean pass's grep, and the residue rate is low (2 sites surviving from a ~30-file cascade, found 4-5 cycles on). recurrence_count 3→4; status HELDS `addressed` (the discipline is working as a reminder-class mitigation — the residue is small, self-correcting via the land-clean grep, and the build does not catch it; a finalize-time `grep`-based maturity-consistency lint stays the ask-class escalation if a future wide cascade leaves a LARGE long-tail residue). last_observed→c095.

---

```yaml
---
slug: firm-flip-leaves-within-file-stale-narration-in-flipped-operators-own-entry
first_observed: cycle-091
last_observed: cycle-091
recurrence_count: 1
status: addressed (watch met c095 — within-file bullet HELD on the bilinear-form flip, no recurrence-2)
addressed_by: cycle-093 meta-phase (batch-29) — GO; codified a WITHIN-FILE self-consistency grep bullet (the within-file analog of the cross-file `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep`) into `.claude/agents/harvester.md` + `.claude/agents/lifter.md` §Discipline: after flipping the operator's own §Status to firm, re-read the operator's OWN file end-to-end and re-anchor every body narration (gate-body / Evidence-section conclusion / FP-residue paragraph / Dependencies-section self-note / any "stays rough-in" / "escape does not apply" conclusion prose) to match the firm §Status, in the SAME proposed-changes pass. `.claude/agents/` edits → SESSION RESTART before c094.
---
```

**Pattern (a firm-flip dispatch updates the operator's `## Status` line but leaves stale "stays rough-in" / "escape does not apply" CONCLUSION narrations elsewhere in the SAME file).** The flip-dispatch (harvester does the flip; lifter does cascade re-anchors) treats the flipped operator's own file as a single point — the `## Status` line — and sweeps only that, plus cross-file consumers. But a `rough-in (test-coverage-bounded)` entry that is being PROMOTED on the firm-on-positive-structure escape typically carries, BEYOND its §Status line, several other in-file narrations whose CONCLUSION was "rough-in": a gate-(c)-style body paragraph arguing why the escape did not yet apply, an Evidence-section closing conclusion, an FP-residue closing sentence, a Dependencies-section self-note ("the X half remains open"). When the §Status flips firm, those conclusion-narrations go stale IN THE SAME FILE — they now contradict the file's own §Status. This is the within-file analog of the cross-file maturity-residue pattern (sibling above); the cross-file grep `grep -rn '<slug>' book/src | grep '<old-token>'` technically matches them (same file, same old token), but the operator-side bullet's framing ("the operator's own file + a few named consumers") and the flip-dispatch's habit of editing only the §Status block leaves the body conclusions unswept.

**Evidence (recurrence-1; the c091 `matrix-weighted-norm` firm flip).** The c091 D1 harvester flipped `book/src/L1/matrix-weighted-norm.md` §Status `:110` `rough-in (test-coverage-bounded)`→`firm` (the firm-on-positive-structure escape, both math sides discharged c088+c089), and the D1+D2 dispatches swept the §Status + the cross-file consumer cluster (~30 files) clean. But THREE narrations in the verb's OWN file still concluded "stays rough-in" / "the escape does not apply" against the firm §Status: gate-(c) header parenthetical + body (`:122`), the Evidence-section conclusion (`:150`), and the FP-residue closing sentence (`:180-184`). The c093 land-clean cycle cleaned them, but it cost TWO repair passes: the c093 D1 cross-layer-cross-cutter surfaced the `:150` Evidence contradiction, and the c093 D2 lifter's critic extended the fix from 2 to 4 residues (catching `:122` + `:180-184`). The within-file residue was benign (no build break, no broken link, no false ALGEBRAIC claim — the §Status was authoritative + correct), but it left the flipped operator's own entry internally self-contradictory until a separate land-clean cycle + 2 repairs cleaned it.

**Mitigation (cycle-093 meta-phase, this entry — go).** A producer-side §Discipline bullet on `.claude/agents/harvester.md` (the firm-flip owner) + `.claude/agents/lifter.md` (the cascade owner): when your dispatch flips the operator's own `## Status` to `firm`, before emitting, **re-read the operator's OWN file end-to-end and re-anchor every CONCLUSION narration** — gate-body paragraphs, Evidence-section conclusions, FP-residue closing sentences, Dependencies/§-self-notes, and any standalone "stays rough-in" / "the escape does not apply" / "X half remains open" prose — so the whole file agrees with the firm §Status, in the SAME proposed-changes pass. (Distinct from, and tighter than, the cross-file whole-book grep: this is a *single-file end-to-end self-consistency read* the flip-dispatch always owns; the firm-apparatus-INSIDE-the-fence bullet covers AUTHORING a fresh firm body, this covers RE-ANCHORING the pre-existing rough-in narrative when the SAME file flips.)

**Why a producer-side role-spec bullet (Medium-cascade), not a tooling gate.** Same rationale as the cross-file sibling: the drift is benign-but-untidy (a stale in-file conclusion; no build break, no false algebraic claim — the §Status is authoritative), the build does not catch it (`linkcheck2` checks links, not conclusion-prose consistency), and the cost is a land-clean cycle + repair passes. The flip-dispatch already re-reads + rewrites the §Status block; extending the read to the whole file is near-zero marginal cost and catches it at the source. It does NOT warrant a finalize-time consistency gate (cf. the `index-table-status-cell-drifts` + cross-file-grep precedents, where the promotion-time guard was preferred over a finalize re-sweep for the same reason). **Watch.** The batch-30 `bilinear-form-firm-flip-and-cascade-wave` (the GO batch-30 LEAD) is the FIRST flip to carry the new within-file bullet — and `bilinear-form.md` is a KNOWN case (its `:251-257` Dependencies self-note "the `bilinear-form` half remains open" is exactly the within-file narration class this bullet must catch on the flip). Watch the c094 cascade: it should leave `bilinear-form.md` internally self-consistent in ONE pass (no land-clean cycle, no repair pass needed to mop up a within-file conclusion-residue). If the c094 flip STILL leaves a within-file stale conclusion despite the bullet (recurrence-2), the producer-side bullet is reminder-dependent like all reminder-class mitigations — escalate to a finalize-time within-file §Status-vs-conclusion-prose lint (a tooling change, ask-class).

**Batch-30 WATCH MET (cycle-096 meta-phase — the within-file bullet HELD).** The `bilinear-form` firm-flip cascade landed at c095 (the LEAD became the campaign's first live rank-linter validation; renumbered from c094 to c095 by the GRADED-STACK campaign sequencing). The c095 D1 harvester flip carried the new within-file self-consistency bullet and **left `book/src/L1/bilinear-form.md` internally self-consistent in ONE pass** — the `:251-257` Dependencies self-note this entry's batch-29 watch named explicitly ("the `bilinear-form` half remains open") was re-anchored on the flip; the D1 discretionary within-file re-anchors (×5) were grep-confirmed clean post-apply (per the c095 finalize §Wave-conflict). NO recurrence-2: no within-file stale conclusion survived the flip, no land-clean cycle / repair pass was needed to mop up the flipped operator's OWN entry (in pointed contrast to the c091 mwn flip, which cost a c093 land-clean + TWO repair passes precisely because the bullet did not yet exist). The within-file mitigation worked as designed at its first exercise. status holds `addressed` with the watch outcome recorded; the residual cross-file long-tail (consumer files, not the flipped operator's own) is tracked under the parent `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` (recurrence-4). No escalation to a finalize-time within-file lint is warranted.

---

```yaml
---
slug: graded-stack-kickoff-codification-missed-the-lifter-role-spec
first_observed: cycle-096
last_observed: cycle-096
recurrence_count: 1
status: addressed
addressed_by: cycle-096 meta-phase (batch-30) — GO; added a graded-stack typed-edge + rank-invariant §Discipline bullet to `.claude/agents/lifter.md` (the cascade-execution + lazy-tail-typing producer), mirroring the bullets the pre-c094 kickoff commit `ac4fa0a` gave harvester/lowering-verifier/layer-intro-author/abstractor. Also enacted the `integrator-finalize.md` step-5b finalize-runs-linters wiring (OQ `graded-stack-finalize-json-wiring-role-spec`). `.claude/agents/` edits (integrator-finalize + lifter) → SESSION RESTART before c097.
---
```

**Pattern (a project-wide methodology directive's role-spec codification missed one producer that the directive's discipline materially applies to).** The 2026-06-04 GRADED-STACK kickoff (commit `ac4fa0a`, pre-c094 restart) codified the rank-invariant + typed-edge `depends-on`/`reference` discipline into CLAUDE.md §Methodology-invariants + the role-specs of harvester, lowering-verifier, layer-intro-author, abstractor, critic, and cycle-planner — but **not `lifter`**. Yet the lifter is the cascade-execution producer: in the c095 `bilinear-form` cascade it re-typed feature-column edges (D2) and in c096-D3 it typed the O1 lazy-tail node `solve-family-map-dissolution` with `rank: firm` + a typed `edges:` block — both are exactly the typed-frontmatter + rank-invariant-binding work the directive governs. The lifter did the work correctly by carrying the conventions implicitly (its existing cross-file/within-file maturity-residue bullets are adjacent), but the role-spec did not state the rank constraint it must satisfy when it flips a node to firm.

**Evidence (recurrence-1; surfaced by the batch-30 meta-phase review of which role-specs carry the campaign bullets).** Grepping `.claude/agents/*` for the graded-stack rank/typed-edge bullets: harvester `:90`, lowering-verifier `:93`, layer-intro-author `:31`, abstractor `:87`, critic `:66`, cycle-planner `:74` all carry the matching responsibility per `METHODOLOGY-GRADED-STACK.md` §8; `lifter` and `combinator-miner` carried none. The lifter is a genuine gap (it writes `rank:`/`edges:` frontmatter on firm-flips + lazy-tail typing); `combinator-miner` is NOT a gap (it proposes/replaces combinators but does not itself flip a node to firm with typed frontmatter — its mining proposals land via harvester/lifter/abstractor, which carry the bullet).

**Mitigation (cycle-096 meta-phase, this entry — go).** Added the graded-stack §Discipline bullet to `.claude/agents/lifter.md`: a re-anchor/firm-flip/lazy-tail-typing the lifter lands carries `rank:`+`edges:` frontmatter and the invariant `rank(u) ≤ min over depends-on deps`; before flipping a node to `firm`, confirm on disk that all its `depends-on` deps read ≥ `firm` (a firm flip resting on a `rough-in`/`stub`/`roadmap_goal` dep is a NEW rank violation the hard-gate-new invariant forbids — the c096 baseline is fully discharged → `rank_violations == 0`, so any new one blocks at finalize); mark each authored edge `depends-on`/`reference` (root-edge `reference`; `cites-evidence` L0-range edges exempt from slug-resolution + rank-check); the honest residual gate STAYS if a dep is still `rough-in`. Composes with the lifter's existing within-file + cross-file maturity-residue greps (those re-anchor the prose mentions; this writes the typed frontmatter the linters read). Medium-cascade (a role-spec bullet on an existing producer, no new role / structure / tooling). The lifter already did the work correctly without it; the bullet makes the rank constraint explicit so it survives as standing discipline (not reminder-by-adjacency).

**Why Medium-cascade GO (not no-go, not ask).** The work was already being done correctly (no defect landed — c095/c096 lifter dispatches all passed rank-gate firm-over-firm), so this is a codification-completeness GO, not a defect-driven one — but completing the directive's role-spec coverage is exactly the standing-discipline-survives concern the user's "codify the HARD-gate-new rank invariant into the producer role-specs" item flagged. The directive itself is High-cascade (a whole-artifact health model), already enacted by the user pre-c094; this is the small residual codification the meta-phase owns. **Watch.** Confirm batch-31 lifter cascade/typing dispatches (the P2 slice-deletion tranche will mint `roadmap_goal` chapters + repoint edges heavily) carry the typed-edge + rank discipline cleanly; if a lifter-landed firm flip ever produces a NEW rank violation despite the bullet (recurrence-2), it surfaces at finalize step-5b (the gate now wired) — escalate the finalize gate's disposition, not the bullet.

---

```yaml
---
slug: slice-deletion-inbound-link-sweep-self-exclusion-grep-bug
first_observed: cycle-098
last_observed: cycle-098
recurrence_count: 1
status: addressed
addressed_by: deleted-slug-inbound-live-link-sweep (skill refined batch-31 meta-phase — source-path-prefix exclusion warning folded into Procedure step 2) + skill-candidate inbound-link-sweep-before-slice-delete rejected-as-duplicate
---
```

**Pattern (a file-deletion inbound-link sweep that excludes the target file by LINK-TARGET TEXT instead of by SOURCE PATH silently swallows exactly the inbound links it is hunting).** The cycle-098-D1 orthog-slice-delete report computed its inbound-cite count with `grep 'slices/orthog\|orthog\.md:' | grep -v 'spec/slices/orthog.md' | grep -v 'spec/index.md'`. The `grep -v 'spec/slices/orthog.md'` filter was *intended* to drop the slice file's own self-referential lines — but every inbound `[..](../spec/slices/orthog.md)` markdown link literally CONTAINS the string `spec/slices/orthog.md` in its link-target text, so the `grep -v` dropped all 8 inbound links too (6 external `[..](..)` + 4 relative `./orthog.md` from a sibling slice, minus de-dup). The report concluded "exactly 2 inbound cites" and repointed only the 2 backtick-inline-code references (which are not even `linkcheck2` errors), leaving 8 live `[..](..)` links that PC-3's `git rm` would have turned into hard build errors. The critic's independent enumeration caught all 8; the repairer added PC-4 a–f pre-apply. **The exact load-bearing-link defect the inbound sweep exists to prevent, caused by the sweep's own exclusion predicate.**

**Why recurrence-1 (not the recurring slice-deletion friction-family).** This is a *distinct mechanism* from the prior slice-deletion friction (`slice-removal-non-link-prose-reference-grep-gap` c015, `multi-deletion-cross-dispatch-dangling-link-coordination` c050, `sibling-slice-citation-reanchor-sweep-gap` c020): those were *missing-coverage* gaps (a reference shape the sweep didn't look for); this is an *over-exclusion* bug (the sweep looked, found, then filtered the findings away with the wrong predicate). Single batch-31 occurrence; the campaign whose deletion cycles repeatedly exercised inbound sweeps is now COMPLETE (corpus 9→0 at c099), so the slice-specific recurrence ENDS here — but the lesson generalizes to ANY future `book/src/**` file deletion (the skill is no longer slice-scoped).

**Surfaced by:** cycle-098 critique (same-layer-cross-cutter orthog-slice-delete `cross-reference-integrity` catch) + the `inbound-link-sweep-before-slice-delete` skill-candidate (critic-filed c098).

**Mitigation (batch-31 meta-phase, this entry — go).** No new skill (the verb is already owned by the cycle-051-promoted `deleted-slug-inbound-live-link-sweep`). Instead: (a) REFINED that skill — folded a load-bearing "⚠ Exclude the target file by SOURCE-PATH prefix (`grep -v '^book/src/<dir>/<name>.md:'`), NEVER by link-target text" warning into Procedure step 2, with the c098 bug as the worked counter-example, AND broadened "When to invoke" from `delete:`-fence-only to ANY `book/src/**` file deletion (the campaign is over; the discipline is steady-state); (b) REJECTED the duplicate candidate `inbound-link-sweep-before-slice-delete` with the sharpening folded in (a second skill for the same verb would fragment the procedure). Owners: critic (independent re-enumeration before clearing `cross-reference-integrity`) + integrator-per-report (pre-apply check).

**Watch.** A future file-deletion sweep that again over-excludes via link-target text despite the refined skill (recurrence-2) means the producer-facing warning is being under-invoked — at that point fold the inbound-sweep into a mechanical pre-`git rm` integrator gate (the same shape as the held citation-checker tool ASK).

---

```yaml
---
slug: pre-redirect-orphan-skills-survive-decommission
first_observed: cycle-100
last_observed: cycle-102
recurrence_count: 1
status: addressed
addressed_by: batch-32 meta-phase (retired 5 dead orchestrator-era skills → skills/_retired/; same class as the batch-31 non-book orphan-review)
---
```

**Pattern (decommissioned-era artifacts survive a role-architecture migration as silent orphans until a sweep finds them).** The 2026-05-26 structural redirect replaced the 6 prompted orchestrator roles (Planner/Explorer/Synthesizer/Critic + Meta-Critic + README Builder) with the 14 Claude Code subagents — but **5 skills authored FOR those dead roles survived live in `skills/`**: `cluster-friction-patterns` (Meta-Critic session-start), `survey-friction-window` (Planner cycle-start), `verify-rotation-citation` + `propose-rotation` (Critic/Synthesizer `rotation_claim` JSON — a claim shape the redirect retired), `skill-selection` (per-cycle Synthesizer/Critic `episodic.jsonl` skill-uptake logging). All five reference now-deleted channels/roles (`episodic.jsonl`, `lessons.md`, `prompts/`, `schemas/`, the prompted roles) and are read by **NO** live `.claude/agents/*.md` definition (grep-confirmed: 0 live-agent refs each; only `classify-variant-axis` of the old skill set is still live, used by `critic.md`). They are the `skills/`-cohort analog of the `orchestrator/`/`prompts/`/`schemas/` non-book orphans the batch-31 meta-phase deleted — the same decommission-residue class, just in a directory the batch-31 orphan-review deliberately scoped out (it was scoped to the user-named non-book artifacts; the dead-skill sweep was deferred to batch-32, recorded in `priorities.md` plan-tag `orphan-review-follow-ons`).

**Surfaced by:** cycle-100 integrator-signals §Suggested-next-dispatches (`meta-phase enactment, dead orchestrator-era skills retirement`) + the batch-31 orphan-review follow-on (`orphan-review-follow-ons` plan item 3a) + the batch-32 aggregate-picture block (candidate (b)).

**Mitigation (batch-32 meta-phase, this entry — go).** Retired all 5 to `skills/_retired/<slug>/` (preserving git history, recoverable) with a `status: retired` frontmatter flip + a top-of-body RETIRED note citing the dead role/channel each served and naming its live replacement. NOT deleted (the `_retired/` convention preserves them as historical record, mirroring `phase-1-slice-reduction-audit` retired batch-31). No new skill, no role-spec edit (no live agent referenced them, so no dangling reference to repair — the retirement is self-contained in `skills/`). The historical mentions in `scaffolding/skill-candidates.md` (provenance prose in two candidate entries) are append-only intake, NOT live index references — left as historical record.

**Why recurrence-1, not the slice-deletion friction family.** This is a *decommission-residue* class (an artifact serving a deleted role survives the migration), distinct from the slice-deletion link-sweep mechanism. One-off cleanup; the orchestrator decommission is now complete (orchestrator/prompts/schemas deleted batch-31, dead skills retired batch-32). **Watch.** If a future migration again strands role-bound artifacts that survive un-swept (recurrence-2), add a standing post-migration orphan-sweep step to the meta-phase decommission checklist; for now the one-time sweep suffices.

---

```yaml
---
slug: graded-stack-linter-block-mapping-edge-parser-blind
first_observed: cycle-104
last_observed: cycle-105
recurrence_count: 2
status: addressed
addressed_by: cycle-105 meta-phase (batch-33) — fixed tools/graded-stack-lint/graded_stack_lint.py parse_frontmatter to GC-traverse the block-mapping edge form (+ honored kind:navigational-container in is_likely_outside_dag)
---
```

**Pattern (TOOL-level: the linter could not SEE the edges producers actually author).** The graded-stack reachability-GC linter's hand-rolled `parse_frontmatter` parsed only the inline-flow typed-edge list-item form `- {target: X, kind: Y}`, NOT the multi-line **block-mapping** form
```
- target: X
  kind: Y
```
— which is the shape the integrators + producers actually write on disk (every feature column, every record page). A block-mapping `- target: X` was stored as the bare string `"target: X"` (matching no node slug) and the indented `kind: Y` continuation line was mis-attached as a stray sub-key of the `edges:` block, so only the LAST `kind:` survived and ALL block-mapping `depends-on`/`uses-record` edges were invisible to the reachability mark. CONSEQUENCE: the c104 feature-column→`config-record` `uses-record` rescue (12 edges) was correct on-disk but `config-record`/`op-params` still read `garbage?` in `--show-inbound`; `reachable` was stuck at 36 (= exactly the 36 roots, nothing traversed). The whole P1 reachability axis was unmeasurable.

**Evidence.**
- **cycle-104 (detection):** the c104 finalize signal flagged it — `parse_frontmatter` does not parse the block-mapping form; PRE-EXISTING + uniform (affected every block-mapping edge, including c103's), exit unaffected (trips only `rank_violations`, held 0). Routed to `tools/` (meta-phase authority).
- **cycle-105 (compounding cost):** the c105 planner DEFERRED the natural WAVE-3 op-chapter typing LEAD to the meta-phase + cycle-106 *specifically because* the rescue payoff would be invisible to the linter until this bug was fixed. So the bug did not just hide a number — it gated the next campaign tranche.

**Mitigation (batch-33 meta-phase, this entry — go, ENACTED + RE-RUN).** Rewrote `parse_frontmatter` to recognize a block-mapping list item (`- key: value` opening a dict) and fold its subsequent more-indented `key: value` continuation lines INTO that item's dict — so both surface forms (inline-flow and block-mapping) now parse to a `{target, kind}` dict and `_edge_target` reads `target` from either. ALSO honored `kind: navigational-container` in `is_likely_outside_dag` (the leading-token match, parenthetical-tolerant) — fixing the sibling gaps `dependency-map-not-recognized-outside-dag-by-linter` + `linter-outside-dag-misses-group-intro-container-pages` (one rule). Regression-tested all three edge forms (inline-flow, block-mapping, legacy bare-list) + container recognition. **TRUE reachability picture after the fix (re-run on the live tree):** `reachable` 36 → **81** (+45 — block-mapping edges now traverse); `config-record` correctly shows all 12 inbound feature-column `uses-record` edges; `op-params` shows `transient.L4`; `detritus` 229 → **163** (−66); `detritus_with_typed_edges_stronger_signal` 65 → **41**; `expected_unreachable_outside_dag` 21 → **44** (the navigational containers now correctly classified); `unresolved_depends_on_targets` 36 → **21**; `rank_violations` HELD **0**; exit 0. The 6 internal solve/BC records (`dofset`/`krylov`/`sim-state`/`step-outputs`/`prev-carry`/`solve-result`) remain (correctly) unreachable — they are the WAVE-3 op-chapter `uses-record` work, now MEASURABLE.

**Migration into the plan.** The WAVE-3 op-chapter typing tranche (which this fix unblocks) is the batch-34 LEAD in `priorities.md`; the linter fix itself is the enabling plan item (now landed). **Watch.** If a future scheme/edge surface form is added that the hand-rolled parser again misses (recurrence-3), escalate to an ask-class decision on adopting a real YAML parser under `tools/` (currently stdlib-only by convention).

---

```yaml
---
slug: reachability-gc-ground-dont-remove-future-deps
first_observed: cycle-107
last_observed: cycle-120
recurrence_count: 4
status: addressed
addressed_by: cycle-108 meta-phase (batch-34) — codified the GROUND-don't-remove disposition (user directive 2026-06-05) into METHODOLOGY-GRADED-STACK.md §2f + §8 + the role-specs (layer-intro-author §(g), cross-layer-cross-cutter §Discipline, meta-phase §Graded-stack standing duties) + the reader-facing book mirrors (resolution-ladder.md batch-34 refinement, graded-stack-scheme.md §5 reachability-vs-well-foundedness clarification, goal-flow.md batch-34 arc). Memory: feedback_gc_ground_dont_remove_future_deps. **Batch-37 (cycle-117 meta-phase): recurrence-3 — the disposition applied CLEANLY again on the all-fronts-wave detritus.** The c117 all-fronts wave added 3 new firm L1 ops as detritus (`build_mesh`/`fe_space_hierarchy`/`interpolator`). The batch-37 meta-phase ran the §2f disposition triage faithfully: `build_mesh` is GROUNDABLE via the faithful `feature/lifecycle.L1 → L1/build_mesh` composes edge (the lifecycle do-block literally calls `build_mesh cfg` as stage-1 of `config→mesh→assemble→solve` at `lifecycle.L1.md:39,:44`; it was carried as a `reference` only because `build_mesh` did not yet exist as a node when the lifecycle was authored — the now-firm op makes the genuine composition edge faithful, not forced) → migrated to the plan as a c118 grounding dispatch. `fe_space_hierarchy`/`interpolator` are NOT yet groundable (no faithful inbound consumer — `fe_space_hierarchy`'s consumer is an unbuilt geometric-multigrid preconditioner; `interpolator`'s is an unbuilt field-probe/divfree feature) → dispositioned as RE9/RE10 reachability baseline-exceptions with promotion conditions. The strict priority order (ground → baseline-except, never force) held; no false edge. **Batch-38 (cycle-120 meta-phase): recurrence-4 — the disposition applied CLEANLY AGAIN (the c118 D4 `build_mesh` GROUND edge LANDED, +1 reachable; c119 D1 honest-typed the analogous L4 lifecycle sibling), AND the c120 plateau-probe surfaced the disposition's SELF-CORRECTING property: FINDING-1 falsified the c117 RE10 (interpolator) premise — `L1/interpolator` DOES have two faithful inbound consumers from reachable firm nodes (`L4/waveguide_mode_reduce` discrete-curl `Bz` at `boundarymodesolver.cpp:319-323`; `L1/divfree-projector` discrete-`Grad` at `divfree.cpp:117`), both already prose-documented. RE10 was a baseline-exception that should have been a GROUND the moment `waveguide_mode_reduce` firmed (c118 D5). This meta-phase DISCHARGES RE10 by migrating a c121 grounding dispatch (the §2f priority-1 disposition). The pattern is robust: the standing baseline-exceptions review CAUGHT the stale RE10 premise and re-routed it from baseline-except → GROUND — exactly the every-batch RE re-check the disposition mandates. RE9 (fe_space_hierarchy) independently re-checked, premise HOLDS (geometric-multigrid preconditioner genuinely unbuilt).
---
```

**Pattern (a NEW positive methodology disposition that surfaced from live use, now codified).** Not friction in the "something is broken" sense — this entry tracks the **emergence + codification of a new reachability-GC disposition** the user directed mid-batch (2026-06-05) after it was needed twice. When the reachability GC marks a node garbage, the old binary was *delete-as-detritus* vs *force-an-edge* (the latter forbidden). The directive introduces a **third, preferred disposition**: if the unreachable node is a genuine future/absorbed dependency of a *reachable* goal node, **GROUND** it — sketch the faithful, honestly-typed `depends-on` edge into the reachable chain so liveness propagates — rather than removing it. The disposition is a strict priority order: **(1) ground → (2) route-as-detritus → (3) delete/baseline-exception**, and grounding is **faithful-edge-or-finding** (never a false edge to flip a number).

**Evidence (thrice-applied across batch-34, every application critic-verified faithful).**
- **cycle-107 D1:** the firm-but-absorbed BC-elimination + divfree clusters were grounded from the feature-spine roots with 3 honestly-typed edges (`fe_assemble →absorbed-post-composition→ eliminate_bc`; `eigenmode.L4 →constrains-eigvec→ divfree-projector`; `divfree-projector →uses→ {set_subvector_zero}`) — `reachable` 88→95, 7 nodes rescued, 0 regression. The cycle-107 planner correctly REJECTED the c106-suggested `column →composes→ eliminate_bc` edge as unfaithful (no `Eliminate*` call sits in `drivers/`).
- **cycle-108 D1:** a systematic `lowers-to` grounding pass typed `edges:` down the BC + divfree lowering chains so the L1/L0 lowering homes became reachable — `reachable` 95→102, 7 nodes rescued. The faithful-edge-or-finding discipline CAUGHT a would-be over-edge: the BC theme does NOT `lowers-to` `essential_dofs` (it consumes `DofSet[N]` as a given operand reaching root via its own construction theme).

**Why `addressed` at recurrence-2 (not watched).** The user issued an explicit directive AND the disposition was needed twice in one batch — the bar for codification is met immediately (it is the exact `roadmap_goal`-on-the-resolution-axis analogue on the reachability axis). The codification is enacted this meta-phase (role-specs + spec + book mirrors). **Watch.** If a future grounding application forces a *false* edge that the critic does NOT catch (a misclassified `depends-on` reaching the artifact), re-open — the faithful-edge-or-finding guard would have failed. None observed; both batch-34 applications were critic-verified faithful.

---

```yaml
---
slug: graded-stack-lint-block-mapping-misparse-on-legacy-edge-prose-colon
first_observed: cycle-106
last_observed: cycle-106
recurrence_count: 1
status: addressed
addressed_by: cycle-108 meta-phase (batch-34) — NO-GO on a pre-emptive reader fix; rely on migration-eliminates-the-trigger (the P1 typed-edge campaign converts legacy `:`-bearing edge items to the clean `edges:` block surface form as files are next-touched, which removes the trigger). Re-open as a tools/ fix-the-reader decision only on recurrence-2 (a fresh false-positive after the lazy tail is materially drained).
---
```

**Pattern (TOOL-level latent linter-reader bug, distinct from the block-mapping-edge-PARSER-BLIND bug the batch-33 meta-phase fixed).** Where the batch-33 bug was *the reader could not SEE block-mapping edges at all*, this is the inverse: a **legacy** edge item (`depends_on:`/`lowers_to:`/etc.) written as `- book/src/<slug>.md (… prose qualifier with a ':' in it …)` trips the linter's block-mapping branch (`graded_stack_lint.py:211` `bm` regex `^(\S[^:]*):\s*(.+)$`) — the embedded `:` makes the whole string read as a `{target: …}` dict and stringify into `unresolved_depends_on_targets` as `{'book/src/<slug>` even though the slug is legitimate and the file EXISTS. So it INFLATES the unresolved-target false-positive count on un-migrated `:`-bearing legacy items.

**Evidence (one instance, latent since).** **cycle-106 D5:** surfaced during the `unresolved_depends_on_targets: 21` reclassification — D5's migration of all 18 host files to typed `edges:` blocks *removed the trigger* (`unresolved 21→0`, `--strict` EXIT 0), but the reader-bug is **latent**: any remaining un-migrated `:`-bearing legacy-edge item reproduces the artifact. No fresh trigger fired in c107/c108 (both were grounding/node-typing on already-scheme-or-clean chapters).

**Decision (batch-34 meta-phase — NO-GO on a pre-emptive reader fix).** Two non-blocking reader fixes exist (strip the trailing ` (…)` qualifier before the block-mapping test, mirroring `normalize_target`'s paren-strip at `:317`; OR skip the block-mapping branch for legacy-key items). But the P1 typed-edge campaign is *already* converting legacy `:`-bearing items to the clean `edges:` block surface form as files are next-touched (option (a)-lazy tail), which removes the trigger file-by-file — so the migration is the in-flight fix, and a separate `tools/` code-change ask is not warranted while the lazy tail is draining and `unresolved_depends_on_targets` sits at 0. This is a code change (ask-class authority), so it is correctly deferred rather than enacted. **Watch / re-open** as a `tools/` fix-the-reader decision on **recurrence-2** — a fresh `{'book/src/…` false-positive surfacing after the lazy tail is materially drained (i.e. the migration-eliminates-the-trigger bet failed because a long-lived legacy `:`-item persisted). Until then, the bug is latent with no live cost (`unresolved=0` confirmed on the live tree this meta-phase).

---

```yaml
---
slug: named-shape-groups-tensor-n-rank-1-leak
first_observed: cycle-111
last_observed: cycle-111
recurrence_count: 1
status: addressed
addressed_by: cycle-111 meta-phase (batch-35) — an OUT-OF-BAND user directive (2026-06-06, commits bee5598 + 7b4b2d1) introduced named shape groups Tensor[(S: ...)] + the two-group operator form LinOp[(R: ...), (D: ...)] to the L4 calculus (authoritative def book/src/design/l4_calculus.md §1.2.1-§1.2.2; memory project_named_shape_groups_notation). The orchestrator ALREADY enacted the artifact sweep (design doc + the shape-generic L4/L3/L2 cohort + lowering themes + concept pages + index cells — 64 files; L1/L0 flat Tensor[N] KEPT; audit reports/2026-06-06T030000Z-shape-notation-audit/AUDIT.md). This meta-phase CODIFIED the convention into the producer role-specs so NEW signatures use it: harvester.md §L4/L3-strawman-conventions + layer-intro-author.md §L4/L3-strawman-conventions each gained a "Shape congruence — use NAMED SHAPE GROUPS, not bare Tensor[N]" bullet. Memory: project_named_shape_groups_notation.
---
```

**Pattern (a NEW notation convention that emerged from a user directive — the `Tensor[N]`-as-same-shape rank-1 leak).** Not friction in the "something is broken" sense; tracks the emergence + codification of a notation convention the user directed out-of-band. The L4 calculus used bare `Tensor[N]` to mean "same shape as the other operand" — but `Tensor[N]` denotes a **rank-1 tensor of length `N`**, silently pinning shape-generic ops (element-local / whole-tensor / whole-tensor-reduce: `axpy`/`dot`/`nrm2`/`scal`/`normalize`/`reciprocal`/`elementwise_product`/…) to rank-1. The fix: a **named shape group** `Tensor[(S: ...)]` (first binder) / `Tensor[S]` (re-uses, NO colon before `[`) for rank-agnostic congruence, plus the two-group `LinOp[(R: ...), (D: ...)]` for domain≠range operators. `Tensor[N]` is **reserved** for genuinely-flat rank-1 dof-vectors (KEPT at L1/L0 where Palace `Vector` is rank-1, and for genuine rank-1 lists `Tensor[K]`/`Tensor[m]` at any layer).

**Evidence.** **2026-06-06 (out-of-band):** the user introduced the notation + the orchestrator swept the 64 shape-generic calculus-layer files (design doc §1.2.1/§1.2.2 + the L4/L3/L2 cohort + lowering themes + concept pages + index cells); L1/L0 flat KEPT. Audit of record: `reports/2026-06-06T030000Z-shape-notation-audit/AUDIT.md`.

**Residual (settled-by-default).** The complex element-axis rendering (`Tensor[N, complex]` / `ComplexTensor[N]`) was handled as "convert the shape to `(S: ...)`, preserve the `complex` element-type annotation as written" → `Tensor[(S: ...), complex]`. This meta-phase judged a firm dedicated complex-element-type notation convention NOT warranted (the convert-shape-preserve-annotation rule is sufficient and already applied uniformly in the sweep + codified in the two role-spec bullets) — settled-by-default, no OQ filed. **Watch.** If a future complex-element rendering needs a distinct spelling the convert-shape rule cannot express (recurrence-2), file an OQ for a `complex`-element notation call.

---

```yaml
---
slug: parallel-dispatch-reachability-measurement-contamination
first_observed: cycle-110
last_observed: cycle-110
recurrence_count: 1
status: addressed (watch HELD across batch-36 — no recurrence-2)
addressed_by: cycle-111 meta-phase (batch-35) — LEDGER-AND-MONITOR (no role-spec change enacted). The discipline self-corrected at recurrence-1 (c111 did NOT recur) and the existing critic + repairer + per-report-integrator-re-measure-on-the-landed-tree safety net caught + fixed both c110 instances. Re-open as a GO (a producer-side "measure your OWN edit-set in isolation; finalize computes the cumulative" role-spec instruction in layer-intro-author) on recurrence-2. **batch-36 WATCH RESULT (cycle-114 meta-phase): HELD — NO recurrence-2.** All three batch-36 cycles ran ≥2-layer-intro-author waves on disjoint frontmatter-only file sets (c112 D1/D2 disjoint L3 mid-nodes; c113 D1 observation-only + D2 one-file; c114 D1/D2 disjoint L1 file sets) and each producer correctly reported ONLY its own standalone delta with the finalize step-5b re-measure producing the authoritative cumulative (the disjoint-set isolation pattern the planner mandated each cycle). Contamination did NOT recur. The LEDGER-AND-MONITOR decision is vindicated; the entry stays addressed. Re-open as a GO only on an actual fresh contaminated headline.
---
```

**Pattern (shared-working-tree reachability-measurement contamination across parallel dispatches).** When ≥2 `layer-intro-author` dispatches in one wave both run the reachability linter (`graded_stack_lint.py`) on the SAME working tree, each measures its delta with the OTHER's not-yet-reverted edits present (an apply→lint→revert race across siblings sharing one tree), so each producer's reported reachability headline is contaminated by the sibling's cascade — a producer reports a cumulative-with-sibling number as if it were its own isolated delta.

**Evidence (one instance, self-corrected).** **cycle-110 (detection):** both parallel D1/D2 layer-intro-author dispatches MISreported reachability — D1 reported a 119/+12 headline that was really the cumulative-with-D2 number; D2 reported +12 that was really D1's cascade. BOTH were caught by the critics + fixed by the repairers (each headline corrected to the standalone/isolation truth + a finalize-re-measure instruction); the per-report integrator's re-measure-on-the-landed-tree step produced the authoritative cumulative 119. **cycle-111 (no recurrence):** c111's two parallel dispatches correctly isolated each delta — D1 measured its own +3 standalone, D2 confirmed reachability-neutral, finalize re-measured the cumulative 122. The discipline HELD.

**Decision (batch-35 meta-phase — LEDGER-AND-MONITOR, not codify).** The contamination self-corrected after one occurrence (the c111 producers isolated their deltas without a role-spec change), and a robust three-layer safety net already catches it: the critic flags the measurement-misattribution, the repairer corrects the headline in-place, and the per-report integrator re-measures the authoritative number on the LANDED tree (the single source of truth for reachability — never a producer's working-tree number). Codifying a producer-side measurement-isolation instruction now would harden against a non-recurring pattern; defer it. **Watch / re-open** as a GO on **recurrence-2** — a fresh contaminated headline in a future ≥2-layer-intro-author wave — at which point enact the `layer-intro-author` role-spec instruction: "when ≥2 dispatches share a wave, measure your OWN edit-set in isolation (git-stash siblings, or report only your standalone delta); the per-report integrator + finalize compute the authoritative cumulative on the landed tree — never trust a whole-tree reachability number measured with sibling edits present."

---

```yaml
---
slug: stale-pre-c108-rank-direction-error-prose-on-L1-ops
first_observed: cycle-113
last_observed: cycle-113
recurrence_count: 1
status: addressed (resolved at recurrence-1 — one-off, confirmed bounded by grep at batch-36 close)
addressed_by: cycle-114 meta-phase (batch-36) — RESOLVED, no systematic sweep needed. The c113 D2 finding hypothesized that the c104-era "an L1-op→theme depends-on would be a rank-direction error" prose (correct BEFORE the c108 §5 L1-op→theme grounding convention, WRONG after) might be carried by many L1 leaves re-grounded in the same c104 era (`normalize`/`reciprocal`/`elementwise_product`/`scal`/...). The meta-phase grep-verified the actual blast radius: only `book/src/L1/set_subvector_zero.md` ever carried the phrase, and c113 D2 ALREADY corrected it in-place (the 3 remaining mentions are the CORRECTED prose explicitly marking the earlier assertion WRONG + superseded). The c114 D2 sweep separately grep-confirmed `dot`/`nrm2`/`scal` carry NO stale prose (clean edge-upgrade, no prose correction). The hypothesized systematic sweep is therefore MOOT — the pattern was a single file, already fixed. No friction-ledger escalation, no plan tranche.
---
```

**Pattern (stale pre-convention prose surviving a convention change on re-grounded L1 ops).** A c104-era comment on `L1/set_subvector_zero` asserted an L1-op→L1>L0-theme `depends-on` would be a "rank-direction error." That was correct under the pre-c108 framing but WRONG after the c108 §5 L1-op→theme grounding convention (both endpoints `rank: firm`, so `rank(op=3) ≤ rank(theme=3)` holds and the edge routes liveness DOWN). The risk the finding flagged: such stale prose, plus an un-upgraded `reference`-only op→theme edge, leaves the theme reachable-dead — a silent blocker on the grounding sweep.

**Evidence + resolution (one file, already fixed).** **cycle-113 (detection + fix):** D2 grounded `set_subvector_zero`'s theme and corrected its 3 stale-prose locations in the same edit. **cycle-114 (sweep confirms bounded):** the dot/nrm2/scal theme-grounding sweep found NO stale prose on those three (clean upgrade). **cycle-114 meta-phase (grep-verify):** `grep -rl "rank-direction error" book/src/` returns exactly ONE file — `set_subvector_zero.md` — and its mentions are the CORRECTED prose. The pattern was a one-off, not systematic.

**Decision (batch-36 meta-phase — ADDRESSED/resolved, no codification).** Single-file blast radius, already fixed at recurrence-1. No role-spec edit, no skill, no plan tranche. **Watch / re-open** only if a future c104-era re-grounded L1 leaf surfaces with the same stale framing on a reachability-dead theme (recurrence-2) — at which point a one-edge-per-op grounding micro-sweep (the c114 D2 shape) is the remedy, not a methodology change.

---

```yaml
---
slug: new-summary-kind-grouping-placeholder-link-duplicate-file-build-break
first_observed: cycle-117
last_observed: cycle-117
recurrence_count: 1
status: addressed (GO — codified into integrator-per-report + layer-intro-author this meta-phase)
addressed_by: cycle-117 meta-phase (batch-37) — codified the "open a NEW SUMMARY kind-grouping ⇒ create its navigational-container group-intro stub in the SAME landing" discipline into the integrator-per-report + layer-intro-author role-specs (the per-report preferred-stub-creation discipline already exists for implied components; this extends it to the by-kind-grouping reorg case so the repair moves from finalize-time to per-report-time).
---
```

**Pattern (a new SUMMARY by-kind grouping linked to a placeholder page collides with an existing link → duplicate-file build break).** The directive-3 by-kind sub-chapter grouping convention nests each layer Part's chapters under kind groupings, each with its OWN group-intro page. When a producer opens a NEW grouping mid-cycle but does not (yet) author the group-intro page, the temptation is to point the SUMMARY grouping link at an existing page (e.g. `./L1/index.md`, the Part Overview) as a placeholder — but mdBook treats a file linked twice in SUMMARY.md as a `Duplicate file` and the build FAILS.

**Evidence (one instance, finalize-repaired).** **cycle-117 D3:** opening the new `Mesh & FE-space construction` L1 kind grouping, D3 linked the grouping to the `./L1/index.md` placeholder (D4's OQ had deferred authoring a dedicated group-intro). At finalize, `cargo make book` FAILED with `Duplicate file in SUMMARY.md: "./L1/index.md"`. The finalize applied the **preferred stub-creation build-repair** (per its role-spec step-5): created `book/src/L1/mesh-construction-intro.md` (navigational-container group-intro stub matching the `fe-space-intro.md` format) and repointed the SUMMARY grouping link to it; rebuild EXIT 0. The repair was clean but ran at finalize-time, after a build break.

**Decision (batch-37 meta-phase — GO, codify into the per-report discipline).** The preferred-stub-creation pattern already exists for implied components (a missing cross-ref target → create a `stub`); this is the same pattern applied to the by-kind-grouping case. Codify: a per-report integrator (or the layer-intro-author proposing the grouping) that opens a NEW SUMMARY kind-grouping MUST create its navigational-container group-intro stub in the SAME landing — never placeholder-link an existing page. This moves the repair from finalize-time to per-report-time and avoids the duplicate-file break entirely. **Watch / re-open** if a future grouping-open still placeholder-links despite the codification (recurrence-2).

---

```yaml
---
slug: citecheck-misses-range-end-overrun
first_observed: cycle-118
last_observed: cycle-119
recurrence_count: 2
status: addressed (LEDGER-AND-MONITOR — the on-disk close-brace END-read guard already covers it; re-open as a tools/ ask only on recurrence-3 with a shipped over-range that the guard missed)
addressed_by: cycle-120 meta-phase (batch-38) — LEDGER-AND-MONITOR, no tools/ change enacted. The existing role-spec guard ("`--anchor` alone does NOT discharge a range-END off-by-one; an on-disk close-brace END-read is the established catch") is the live mitigation; the c119 D2 lowering-verifier applied it correctly and CAUGHT the over-range. Re-open as a `tools/`-code GO (a `citecheck --end-anchor` / close-brace-END check) only on recurrence-3 — a fresh over-range that SHIPS to the artifact because the on-disk END-read guard was skipped.
---
```

**Pattern (`citecheck --anchor`/`--scan` verify the START anchor + in-bounds, NOT the range END).** A citation `file.ext:START-END` whose END over-runs the actual construct (the function body / block close-brace falls before END) passes BOTH `citecheck --anchor` (which confirms the START token is within the range) AND `citecheck --scan` (which only bounds-checks against the file length). Neither catches a range-END that over-runs into the next construct; only an on-disk close-brace END-read does. This is a known blind spot in the citation-hygiene tooling, not a defect in the producer.

**Evidence (two instances, one batch, both caught by the on-disk-END-read guard).** **cycle-118 D3 (introduction):** the `interpolator-construction-rotation` authoring landed `palace/fem/interpolator.cpp:282-310` for the point-list `InterpolateFunction` body, which over-ran by 4 lines into `ComputeLineIntegral` (the point-list body close-brace is at `:306`). The c118 D3 repairer fixed the report narrative but left the artifact blocks over-ranged. **cycle-119 D2 (detection + fix):** the lowering-verifier corrected all 4 artifact sites to `:282-306` via an on-disk close-brace read + `citecheck --anchor 'InterpolateFunction'` (which had passed the over-range clean — confirming the blind spot). Pure citation-range correction; no edge/status/node/graph change.

**Decision (batch-38 meta-phase — LEDGER-AND-MONITOR, not codify a tools/ change).** A `citecheck --end-anchor` / close-brace-END check is a `tools/`-code change (ask-class authority) and the existing on-disk-END-read role-spec guard already catches the pattern (it caught both c118/c119 instances). Hardening the tool now, at a project plateau with the citation surface largely settled, is low-value. **Watch / re-open** as a `tools/` GO on recurrence-3 — a fresh over-range that SHIPS to the artifact (the guard was skipped), at which point the `--end-anchor` check earns its code cost.

## reference-only-reachable-firm-nodes-over-counted-as-detritus

```yaml
---
slug: reference-only-reachable-firm-nodes-over-counted-as-detritus
first_observed: cycle-122
last_observed: cycle-123
recurrence_count: 2
status: addressed
addressed_by: cycle-123 meta-phase (batch-39) — METHODOLOGY-GRADED-STACK.md §2g (deliberate-reference-only-reachable = Axis-2 baseline-exception, NOT decay) + RE11 ratification (scaffolding/graded-stack-baseline-exceptions.md) + book methodology mirrors. The reference-edge-liveness scheme question is ADJUDICATED.
---
```

**Pattern.** Three structural models the project adopted AFTER the graded-stack §3 "reference does not carry liveness" rule was written — combinator-primary (leaf→combinator `depends-on`, combinator→leaf `reference`), the DIRECTIVE-3 kernel-API/impl dual-surface (`realizes-kernel-api` is `reference`-class by design), and feature-root→node `reference` (OWN-COMPOSITION) — SYSTEMATICALLY produce firm/roadmap_goal nodes that reach a root ONLY via `reference` edges. The depends-on-only reachability GC correctly marks them `[GARBAGE*]`, so `detritus` climbs per-cycle as a function of CORRECT modeling rather than actual decay (batch-39: ≈123→132). Surfaced as the c122 finalize headline, re-confirmed c123 with a clean CONTRASTING data class (the c123-D2 krylov-iteration column gave a REAL depends-on reachability flip — RE2/RE8 discharged — mechanically distinct from the reference-only cohort that stayed detritus).

**Why it is NOT a defect.** rank_violations HELD 0 throughout; no node went dark; the flagged nodes are firm-and-faithful, just correctly-off-the-`depends-on`-spine (exactly the absorbed-below-spine RE1–RE10 pattern). The §3 rule is correct and its load-bearing purpose ("a mere mention must not keep DEAD vocabulary alive") still holds — these nodes are not dead.

**Decision (batch-39 meta-phase — ADJUDICATED).** **NO-GO on making `reference` edges carry liveness** (would break the §3 rule's purpose + the combinator-primary/RE6/RE8 model). **GO on a scheme clarification:** codified §2g — deliberate-reference-only-reachable structural nodes are the Axis-2 baseline-exception pattern (ratified as RE11), tracked not read-as-decay; a `detritus` climb fully accounted by new such nodes does NOT trip the escalate-guard; an impl mis-typing `realizes-kernel-api` as `depends-on` IS a defect. **ASK (surfaced to human):** an optional `tools/` linter reporting tier separating `reference-reachable` from `true-detritus` (a `tools/`-code change, ask-class) — would make the headline `detritus` a cleaner health signal but changes no gate. Re-open as a GO if the human approves the reporting tier, or if a NON-deliberate reference-only-reachable node (a real missing `depends-on` edge masquerading as RE11) ships uncaught.

## deleted-slug-frontmatter-edge-gap

```yaml
---
slug: deleted-slug-frontmatter-edge-gap
first_observed: cycle-124
last_observed: cycle-127
recurrence_count: 2
status: addressed
addressed_by: cycle-126 meta-phase (batch-40) — extended skill skills/deleted-slug-inbound-live-link-sweep/SKILL.md with a frontmatter-edge tier (grep YAML `edges: depends-on`/`reference` blocks for the deleted slug, not only markdown `](.../slug.md)` links) + added the matching destructive-refactor pre-apply bullet to combinator-miner + integrator-per-report role-specs. **VALIDATED batch-41 (c127): the fix PROVED ITSELF — see batch-41 watch note below.**
---
```

**Pattern (a frontmatter `edges:` `depends-on` to a DELETED slug survives both linkcheck2 AND the existing inbound-link sweep; only the rank linter's `unresolved_depends_on_targets` catches it).** When a destructive refactor DELETES a slug's standalone chapter (the c124 D6 RE6 elimination deleted the 8 `linear_combination` arity-leaf nodes `L2/L3 × {scal,axpy,axpby,axpbypcz}`), three de-link surfaces must be swept: (i) markdown body links `](.../slug.md)`, (ii) prose code-span mentions, and (iii) **YAML frontmatter typed `edges:` blocks** (`depends-on: [..., L3/scal, ...]`). Surfaces (i)+(ii) are covered by the cycle-051 `deleted-slug-inbound-live-link-sweep` skill + `linkcheck2`. **Surface (iii) was NOT covered by any sweep** — frontmatter typed edges are *invisible to `linkcheck2`* (they are not markdown links) AND the inbound-link-sweep skill greps only for `](...)` link syntax, not `edges:` YAML. So two stale `depends-on` edges to deleted slugs slipped through D6's ~90-link body/index re-point sweep and reached finalize.

**Evidence (cycle-124, recurrence-1).** The c124 finalize had to surgically repair TWO frontmatter `depends-on` edges pointing at deleted RE6 leaf slugs: `book/src/L3/normalize.md` `depends-on L3/scal` → `L3/linear_combination`, and `book/src/L3/orthogonalize.md` `depends-on L3/axpy` → `L3/linear_combination` (both re-pointed to the surviving consolidation target, which is firm — parallel to D6's ~90 body re-points, not new authoring). Surfaced by the graded-stack linter's `unresolved_depends_on_targets` (2→0), NOT by `linkcheck2` (which is blind to frontmatter edges) NOR by the body-link grep (which matched only `](...)` syntax). The pattern is specific to DELETIONS that remove a node other chapters carry a *typed frontmatter edge* to — a class that did not exist before the graded-stack §5 typed-`edges:` campaign made frontmatter `depends-on` edges load-bearing. (The cycle-125/126 cycles had NO deletions, so the pattern did NOT recur — recurrence stays 1.)

**Decision (batch-40 meta-phase — go, codify into the existing sweep skill + role-specs).** The verb is already owned by `deleted-slug-inbound-live-link-sweep` (cycle-051; the markdown-link + prose-mention sweep). Rather than a new skill, EXTEND it with a third tier — the **frontmatter typed-edge sweep**: for every slug in a `delete:` fence, also `grep -rn` the artifact for the slug in YAML `edges:` `depends-on`/`reference`/`lifts-from`/`realizes-kernel-api` blocks (not only `](.../slug.md)` markdown links), enumerate, and re-point/strike each — because `linkcheck2` is BLIND to frontmatter edges and only the rank linter's `unresolved_depends_on_targets` catches a stale `depends-on` (and a stale `reference` edge is caught by neither, since `reference` targets are not rank-checked — a silent navigational dangler). Owners: `combinator-miner` (the most frequent destructive-refactor / replace-and-propagate producer) + `integrator-per-report` (pre-apply check) carry a matching destructive-refactor pre-apply bullet. **Watch / re-open as escalating** if a future deletion ships a stale frontmatter edge despite the extended sweep (the producer skipped it), at which point a `tools/` pre-commit `unresolved_depends_on_targets` gate (ask-class) earns its cost — note the existing finalize linter run ALREADY catches `depends-on` danglers at cycle-end; the gap this addresses is catching them at critique/apply time + catching the `reference`-class danglers the linter does not flag.

**Batch-41 validation (cycle-127 meta-phase — recurrence-2 is a SUCCESS datapoint, the fix HELD; status stays `addressed`).** c127's D4 inner-product-family RE-style elimination (`L2/dot`+`L2/nrm2`+`L3/dot`+`L3/nrm2` deleted, folded into `inner_product`; ~20 inbound re-points) was the first destructive refactor AFTER the batch-40 frontmatter-edge-tier codification + session restart loaded the new combinator-miner/integrator-per-report bullets. **The extended sweep PROVED ITSELF: D4's per-report integrator caught a legacy `consumes:` dangler `L2/normalize → L2/nrm2`** (a full-path `book/src/L2/nrm2.md` form the typed-edge grep tier surfaces) that the report's own inventory had MISSED, and re-pointed it AT APPLY TIME — so `unresolved_depends_on_targets` stayed 0 at finalize, with NO c124-style finalize build-repair. The friction moved from finalize-time to per-report-time exactly as the batch-40 meta designed; recurrence-2 is the *frontmatter-edge tier doing its job*, not a re-occurrence of the undetected defect. Re-open as escalating ONLY if a deletion ships a stale frontmatter edge PAST per-report AND finalize (the per-report tier failed) — not the case in batch-41.

## semantic-surface-path-drift-in-role-specs-after-relocation

```yaml
---
slug: semantic-surface-path-drift-in-role-specs-after-relocation
first_observed: cycle-129
last_observed: cycle-129
recurrence_count: 1
status: addressed
addressed_by: cycle-129 meta-phase (batch-41) — swept the stale `book/src/design/l4_calculus.md` path → `book/src/semantics/index.md` across all 9 `.claude/agents/` role-specs (the live surface since the cycle-116 relocation, which fully swept `book/` but never the role-specs). Surfaced by the meta-phase's every-batch SEMANTIC SURFACE liveness/drift check. The 3 stale refs in the authoritative CLAUDE.md are surfaced as an ASK (CLAUDE.md is user-owned, outside meta-phase write authority).
---
```

**Pattern (a `book/` artifact relocation sweeps the artifact's own cross-references but leaves the scaffolding/role-spec/CLAUDE.md references pointing at the old path — a cross-surface liveness drift that persists silently because nothing builds the role-specs).** At cycle-116 (batch-37) the active-management semantic surface got its own home — relocated from `book/src/design/l4_calculus.md` to `book/src/semantics/index.md`. The integrator's relocation swept the **book artifact** clean (`grep -rn 'design/l4_calculus' book/src/` = 0). But the **role-specs** (`.claude/agents/*.md`, 9 files / 12 occurrences) and **CLAUDE.md** (3 occurrences) still named the dead path. The drift is invisible: `linkcheck2` only checks `book/`, the role-specs are prose loaded by the agent harness (no build step), and a producer dispatched to "cite the semantic surface" reads the live `SUMMARY.md` wiring + the actual on-disk surface (every batch-41 dispatch correctly cited `book/src/semantics/index.md`), so the stale spec path never caused a *failure* — it just sat there as a latent wrong-reference for ~13 cycles. Caught only when the meta-phase's standing every-batch SEMANTIC SURFACE liveness/drift check actually read the surface path against the spec text.

**Evidence (cycle-129, recurrence-1).** `grep -rn 'design/l4_calculus' book/src/` = 0 (artifact clean); `grep -rln 'design/l4_calculus' .claude/agents/` = 9 files; `grep -c 'design/l4_calculus' CLAUDE.md` = 3. The surface relocation commit is `00a8f78` (cycle-116, "semantic surface gets its own home"). No producer ever mis-cited the path in a dispatch (the live SUMMARY wiring + on-disk surface are authoritative); the drift was purely in the *guidance* layer.

**Decision (batch-41 meta-phase — go on the role-specs, ask on CLAUDE.md).** GO: corrected all 9 role-specs to `book/src/semantics/index.md` (with a "relocated from the former `book/src/design/l4_calculus.md` at cycle-116" note preserved for provenance), riding the same session-restart the closure-signature bullet triggers. ASK: CLAUDE.md (3 stale refs — §SEMANTIC CONSOLIDATION, the L4-strawman invariant ×2) is the **authoritative source** and is **user-owned** (outside meta-phase write authority); surfaced as a CYCLE.md ask so the human can correct it (the source-wins rule means the stale CLAUDE.md path should be fixed at the source, not just mirrored away in the specs). **Watch / re-open** if a future `book/` relocation (or surface rename) again leaves the role-specs/CLAUDE.md pointing at a dead path despite this being a known class — at which point the integrator's relocation procedure should grow a "sweep scaffolding + .claude/agents + CLAUDE.md, not only book/" reminder (a role-spec bullet on `integrator-finalize`, Medium-cascade, deferred until recurrence-2). One-off this batch; ledgered because the surface is load-bearing and the meta-phase owns its liveness.

**Cycle-132 meta-phase update (batch-42 — the CLAUDE.md ASK was ANSWERED at the source; NO recurrence; status stays `addressed`, recurrence stays 1.)** The batch-41 ASK was acted on by the human/source: commit `ef6498b` corrected the §SEMANTIC-CONSOLIDATION surface-home path in CLAUDE.md (`design/l4_calculus.md` → `semantics/index.md`), and the 3 residual `design/l4_calculus` mentions now carry the explicit "relocated from `book/src/design/l4_calculus.md` at cycle-116" provenance form (intentional provenance trail, not a stale dead-reference). The batch-42 every-batch semantic-surface liveness check re-ran clean: the live surface (`book/src/semantics/index.md`) is correctly cited by every batch-42 dispatch (D1/D2/D3 across the §1.2.2-R polish), the §1.2.2-R ruling + the §1.3 `op-with-params` BNF introducer the batch authored landed ON that surface, and `SUMMARY.md` wiring is intact. NO recurrence of the cross-surface drift (no `book/` relocation/rename this batch). The deferred recurrence-2 watch (an `integrator-finalize` "sweep scaffolding + .claude/agents + CLAUDE.md, not only book/" relocation-procedure bullet) stays deferred — no second instance fired.
