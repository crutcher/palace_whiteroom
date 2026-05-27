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
status: addressed
addressed_by: cycle-006 meta-phase (`.claude/agents/integrator-per-report.md` role-spec clarification — `integrated_at:` deferral to finalize)
---
```

**Pattern.** Cycle-006 per-report integrator dispatch #1 (harvester-krylov-step-L4) set `integrated_at: 2026-05-27T09:00:00Z` in its CYCLE.md frontmatter at per-report integration time — outside CLAUDE.md write-authority partition, which assigns `integrated_at` touches to integrator-finalize. The other 4 per-report dispatches in cycle-006 deferred correctly. Integrator-finalize timestamp `2026-05-27T09:08:49Z` overwrote dispatch #1's earlier value; all 5 reports now carry the same finalize timestamp + `integration_commit: <sha>` (via two-phase SHA pattern).

**Surfaced by**: cycle-006 integrator-finalize CYCLE.md §"Per-report `integrated_at:` inconsistency (caveat (b) for meta-phase)" + integrator-signals.md cycle-006 §Integration-tooling friction.

**Mitigation (cycle-006 meta-phase, this entry):** Role-spec clarification in `.claude/agents/integrator-per-report.md` — add explicit "do NOT touch `integrated_at:` — that is integrator-finalize's responsibility" to the "What you DO NOT do" section. Also add to staging-log Notes a one-line "deferred integrated_at to finalize per role-spec" boilerplate to make the convention visible.

**Watch:** if a future per-report integrator dispatch sets `integrated_at:` despite the clarification, escalate to recurrence-2 and consider a tooling solution (auto-strip pre-finalize, or YAML frontmatter validator gate).

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
