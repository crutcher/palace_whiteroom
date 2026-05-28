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
status: promoted
promoted_to: skills/phase-1-slice-reduction-audit/SKILL.md
promoted_at: cycle-012 meta-phase / 2026-05-28
---
```

**Motivating observation**: cycle-010's first-instance Phase 1 corpus reduction audit (priority #19) established a four-part template (Supersession map / Residual gaps / Recommended action / Proposed changes per slice). Critic review surfaced three recurring friction points likely to repeat at cycle-011+ replay: (a) slice line-range citations drift by 1-2 lines from actual `## H2` boundaries unless anchored by an upfront `grep -n "^## "` enumeration; (b) Recommended-action narrative and proposed_change line ranges are produced separately and can disagree (the first instance's cg.md had a section the narrative said to stub but the line range retained); (c) the slice's section table-of-contents is implicit in long supersession-map prose, making cross-section audit harder. Each will recur on the remaining 7 slices unless the template is crystallized.

**Sketch of procedure**: a `same-layer-cross-cutter`-facing skill that prescribes: (1) enumerate slice section anchors first via `grep -n "^## " <slice>` and emit them as a fixed table at the top of the dispatch report; (2) for each section, populate four columns — section name, actual line range, supersession status (full / partial / none), firm-entry pointer(s); (3) Residual gaps section enumerates only the partial / none rows; (4) proposed_change line ranges are derived mechanically from the section-anchor table, not from prose; (5) a final reconciliation step verifies narrative-and-range agreement before report emission.

**Promotion bar check**: pattern observed = 1 instance (cycle-010 first instance); friction-ledger entry = candidate-creation pending (the template-drift pattern hasn't fired twice yet); sketch concrete enough = ✓ (four-step procedure could be written as SKILL.md). Falls below the "≥2 cycles" promotion bar but well above the "candidate sketch concrete enough" bar. Recommend default-accept under low-bar policy because the remaining 7 slices are queued and template drift will compound across them.

**Cycle-011 uptake-note (appended by repairer of `2026-05-27T234651Z-same-layer-cross-cutter-phase-1-corpus-reduction-batch-2`):** cycle-011's batch-2 audit dispatch is the **second instance** of the cycle-010 template execution. The dispatch directly followed the four-part template, applied the cycle-010 friction-signal mitigation (`grep -n "^## "` H2 enumeration before line-range arithmetic), and still produced ~10 minor citation off-by-ones (4 of which were citation/line-range drift — the same shape this skill candidate is designed to prevent). This confirms recurrence-2 of the template-drift pattern, clearing the "≥2 cycles" promotion bar. In addition, the cycle-011 critic surfaced the proposed_changes-block bracketed-prose syntax as a separate template-friction signal (issue 10 in `META.md` critique) — a likely **cycle-012 meta-phase template-improvement candidate** that may extend this skill's scope (mechanical-not-interpretive proposed_changes blocks). Meta-phase batch-2 (after cycle-012 integrator-finalize) should promote this candidate to firm `skills/phase-1-slice-reduction-audit/SKILL.md` and consider whether to fold the proposed_changes-block format-friction into the same skill or a sibling.

**Cycle-012 uptake-note (appended by repairer of `2026-05-28T034141Z-same-layer-cross-cutter-phase-1-corpus-reduction-batch-3`):** cycle-012's batch-3 audit is the **third instance** and produced the **most severe** manifestation yet of the line-range-brittleness pattern this candidate targets — a HIGH-severity defect (META Issue 1), not the usual minor off-by-ones. The dispatch mis-identified a **sub-slice's START boundary**: it scoped the orthog plane-rotation sub-slice as "lines 311-376" (the §"Open questions" + the SECOND of two near-duplicate L1 entries) when the sub-slice actually begins at line 225 (the `## Context` heading introducing the `# Orthogonalization (plane-rotation stream)` H1) and spans 225-376. The "full reduction" proposed_change as written would have orphaned ~86 lines (225-310: Context, the section H1, Background, Variant axes, L0 citations, and the FIRST L1 entry) beneath a stub claiming the content had moved. Notably the dispatch DID run a `grep` enumeration (the cycle-010 mitigation) but ran it against a mis-scoped window ("lines 300+"), so it caught the sub-slice's tail but not its head — the mitigation as currently practiced verifies the END boundary far more reliably than the START. **Refinement this surfaces for the SKILL.md**: step (1)'s anchor enumeration must verify a sub-slice's START boundary (not just enumerate headings near where the producer expects the content), and step (5)'s reconciliation must confirm that a "full reduction" edit's START anchor sits at the section's true first heading. For multi-section sub-slices (a `## Context` + H1 + several H2s, as here), prefer a unique-text START anchor (e.g. a one-of-a-kind H1) over a line number, and confirm anchor uniqueness with `grep -c`. This confirms recurrence-3 and a severity escalation; meta-phase batch-2 promotion of `skills/phase-1-slice-reduction-audit/SKILL.md` should bake in the START-boundary-verification + unique-text-anchor refinement.

## Rejected

(none yet)

## Open candidates (cycle-012 additions)

```yaml
---
slug: revert-dispatch-phase-book-mutation
proposer: repairer (cycle-012, repair of 2026-05-28T034221Z-layer-intro-author-concept-corrections)
proposed_at: cycle-012 / 2026-05-28
status: promoted
promoted_to: skills/revert-dispatch-phase-book-mutation/SKILL.md
promoted_at: cycle-012 meta-phase / 2026-05-28
promotion_note: promoted as the safety-net companion to the PRIMARY mitigation, which is the layer-intro-author prompt-level guard (`.claude/agents/layer-intro-author.md` §Discipline). See friction-ledger `specialized-agent-direct-write-to-book-during-dispatch`.
---
```

**Motivating observation**: cycle-012 dispatch #7 (layer-intro-author, concept corrections) wrote its four `book/src/concepts/` edits DIRECTLY to the working tree during the DISPATCH phase, violating the no-artifact-mutation-in-dispatch invariant and the write-authority partition (`book/` belongs to integrator-per-report in Phase 5). The critic flagged it HIGH (issue 1). The repair was a clean, mechanical, repeatable shape: verify the working-tree diff matches the report's proposed-changes `[new]` blocks verbatim → verify each `[old]` anchor is unique in HEAD (so reapply is possible) → verify no co-mingled/staged edits → `git checkout` the files to restore clean state → flag for meta-phase via integrator-signals. This is recurrence-1 for layer-intro-author specifically; if any specialized dispatch agent repeats the leak, the same five-step repair applies identically.

**Sketch of procedure** (repairer-facing): when the critic reports a write-authority phase-boundary violation (dispatch agent touched `book/`): (1) `git status --porcelain book/...` to enumerate exactly which artifact files are dirty; (2) `git diff` each against the report's proposed-changes `[new]` blocks — confirm verbatim match (no extra edits, no co-mingled cycle work); (3) confirm no staged changes for those files (`git diff --cached`); (4) confirm each proposed-changes block is a complete `[old]`/`[new]` pair AND each `[old]` anchor is unique in `git show HEAD:<file>` (so integrator can reapply) — if any `[old]` is missing/non-unique, fall back to Option B (accept working tree, instruct integrator to verify-and-skip) or escalate `revise`; (5) `git checkout -- <files>` to revert; (6) verify clean (`git status`); (7) write META repair with `pass-after-repair` and a META-SIGNAL line for integrator-finalize → integrator-signals → meta-phase.

**Promotion bar check**: pattern observed = 1 instance (cycle-012 first instance); friction-ledger entry = none yet (this is the first artifact-leak-during-dispatch occurrence); sketch concrete enough to write as SKILL.md = ✓ (deterministic seven-step git procedure). Falls below the "≥2 cycles" bar but clears the "candidate sketch concrete enough" bar. Recommend meta-phase batch-2 weigh promotion alongside considering a layer-intro-author PROMPT-LEVEL guard (the better fix is preventing the leak, not repairing it — an explicit "do NOT write to book/; emit proposed-changes blocks only" reinforcement in the agent spec). If the prompt guard lands, this repair skill becomes a safety net for residual leaks rather than the primary mitigation.

```yaml
---
slug: audit-report-inherited-miscitation-lint
proposer: repairer (cycle-012, repair of 2026-05-28T034311Z-lowering-verifier-slepc-nep-coordinate-convention)
proposed_at: cycle-012 / 2026-05-28
status: promoted-as-skill-extension
promoted_to: skills/verify-citation-range/SKILL.md §"Audit-report / inherited-citation sub-case"
promoted_at: cycle-012 meta-phase / 2026-05-28
promotion_note: enacted per the candidate's own recommendation (a) — extended the existing firm `verify-citation-range` skill with an audit-report / inherited-citation section rather than creating a wholly new skill. The gap was uptake + the audit-specific duty, not a missing procedure. A lint note also added to `.claude/agents/lowering-verifier.md` §Discipline (independent read_range confirmation of every asserted-verified anchor).
---
```

**Motivating observation**: cycle-012 dispatch (lowering-verifier, SLEPc-NEP coordinate-convention audit) inherited an `arpack.cpp:387` miscitation verbatim from the artifact it was auditing (`book/src/L1/eigsolve.md:116,222`) and **asserted "no drift" over its own anchors** while propagating the inherited error — the un-scale `eig[i] = eig[i] * gamma;` is actually at `arpack.cpp:383` (line 387 is a sort-branch condition). The report was internally inconsistent: §Supporting-evidence cited the correct enclosing range `383-392` while body + `verified_against:` pinned `:387`. This is the **specific failure mode** `verify-citation-range` exists to prevent, and it is sharper than generic citation drift: a *verification-shaped* report (lowering-verifier, lowering-verifier, critic-audit) carries an unusually high duty to land its own anchors precisely, because its entire output is a no-drift assertion. An audit that copies a citation from the artifact under audit and re-asserts it without independently confirming the line range defeats the purpose of the audit.

**Sketch of procedure** (producer-facing, fold into / sibling `verify-citation-range`): for any report whose deliverable INCLUDES a "no-drift / citations-verified" claim (lowering-verifier audits, citation-validity critic checks, slice-reduction audits), every citation the report ASSERTS as verified — especially ones copied from the artifact under audit — must be independently `read_range`-confirmed against source, not transcribed from the artifact. Concretely: (1) enumerate every `(file:line)` the report claims to have verified; (2) for each, `read_range` the cited line ±a few lines; (3) confirm the asserted code/construct is on the cited line (not merely "in the neighborhood"); (4) when the citation was copied from the audited artifact, flag any drift as BOTH a report-anchor fix AND an integrator carry-forward (the artifact also needs correcting). Internal-consistency check: if the report cites the same construct at two different ranges (a precise line in one section, an enclosing range in another), reconcile them before asserting "no drift."

**Promotion bar check**: pattern observed = this is a refinement of an existing firm skill (`verify-citation-range`) for the audit-report sub-case, not a wholly new candidate; friction-ledger entry = none specific to inherited-miscitation, but the skill-uptake-survey warning recurs (cycle-012 critic flagged `verify-citation-range` non-uptake on this very report); sketch concrete enough = ✓. Recommend meta-phase batch-2 either (a) extend `verify-citation-range`'s SKILL.md with an "audit-report / inherited-citation" section, or (b) add a thin lint note to the lowering-verifier + critic agent specs reinforcing independent `read_range` confirmation of every asserted-verified anchor. Lower-cost than a new skill; the gap is uptake + the audit-specific duty, not a missing procedure.

---
slug: partly-constructive-promotion-checklist
proposer: critic
proposed_at: cycle-013
status: proposed
---

# partly-constructive-promotion-checklist

**Motivating observation**: cycle-013 ran the FIRST live test of the cycle-012 `partly-constructive`→`firm` promotion mechanism (abstractor on `book/src/L1-L0/eigsolve-mutation-rotation.md` Sub-pattern B `LinearSolveFailed`). The dispatch promoted cleanly and the audit's literal gate (apply Edit 2 / the GetConverged-forwarder snippet fix, do not defer it) was satisfied — but the promotion rested on an interpretive adjudication that resolved a real CLAUDE.md tension in the dispatch's own favor: the constructive sub-part STILL had only negative-anchor support after the pass (Palace's `void`-returning `Mult` unchanged; forward-looking note retained in prose), so the invariant's clause "Do NOT mark such an entry firm (the constructive sub-part isn't [firm])" was dissolved by reading "firm" as "no open promotion condition + structure confirmed." Compounding it: the CLAUDE.md invariant's enumerated lowering-verifier promotion route is "a **per-line** lowering-verifier audit" (an evidence upgrade to a positive site) whereas the theme's own `## Status` gate option (b) — the route actually invoked — was "a lowering-verifier audit that confirms the **shape is acceptable as a methodology-level pattern**" (a methodology-acceptance upgrade). Those are different routes; the producer dispatch folded the choice between them into a citation-refinement bundle without flagging it as a distinct decision.

**Sketch of procedure** (producer-facing for abstractor/lifter enacting a promotion; mirror-check for critic/integrator): before flipping a theme/operator from `partly-constructive` to `firm`, walk an explicit 4-point checklist and RECORD the answers in the promotion-record prose: (1) **Which promotion route?** Name it against the CLAUDE.md invariant's three enumerated routes — upstream positive source site / per-line lowering-verifier audit / literature-anchor upgrade — AND against the theme's own `## Status` gate; if the theme's gate and the invariant's routes are not the same condition, say so and justify which governs. (2) **Did the constructive sub-part's EVIDENCE change, or only the methodology acceptance?** If evidence is unchanged (still negative-anchor-only), state explicitly that "firm" is being read as "no open promotion condition," not "constructive sub-part now positively anchored" — this is the load-bearing interpretation and must be surfaced, not assumed. (3) **Two-dispatch protocol satisfied?** Confirm the UNBLOCK audit ran in a prior pass and the ENACT pass APPLIES (never defers) the audit-identified firming edits. (4) **Does the permanent honest content note survive the status flip?** The forward-looking-reconstruction note + negative anchors stay in prose; only the transient status gate drops. Critic/integrator then ratify the recorded route rather than inheriting it silently.

**Promotion bar check**: friction-ledger entry = none yet, but this is the first exercise of a cycle-012-codified mechanism and the interpretive ambiguity is concrete (two non-identical promotion routes that a producer can silently pick between); sketch concrete enough to write as SKILL.md = ✓; pattern observed ≥2 cycles = NO (single instance so far). Recommend meta-phase batch-2 either promote as a thin checklist skill OR fold the 4 points into the abstractor/lifter + critic agent specs as a promotion-record requirement. Re-evaluate after the next partly-constructive promotion (none other in flight as of cycle-013).
