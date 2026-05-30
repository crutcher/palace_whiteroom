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
status: promoted
promoted_to: skills/partly-constructive-promotion-checklist/SKILL.md
promoted_at: cycle-015 meta-phase / 2026-05-29
promotion_note: promoted on the batch-3 3× lifecycle precedent (eigsolve EXIT cycle-013 + divfree/chebyshev-L4 ENACT cycle-015 + the cycle-014 STAYS case). The "audit cycle-N / enact cycle-N+1" two-dispatch protocol closed cleanly 3×, making the 4-point checklist concretely writable. Enacting-producer pointer added to .claude/agents/abstractor.md §Discipline (the cycle-015 promotion-checklist bullet). See friction-ledger `partly-constructive-lowering-theme-status` (validated-by-use).
---

# partly-constructive-promotion-checklist

**Motivating observation**: cycle-013 ran the FIRST live test of the cycle-012 `partly-constructive`→`firm` promotion mechanism (abstractor on `book/src/L1-L0/eigsolve-mutation-rotation.md` Sub-pattern B `LinearSolveFailed`). The dispatch promoted cleanly and the audit's literal gate (apply Edit 2 / the GetConverged-forwarder snippet fix, do not defer it) was satisfied — but the promotion rested on an interpretive adjudication that resolved a real CLAUDE.md tension in the dispatch's own favor: the constructive sub-part STILL had only negative-anchor support after the pass (Palace's `void`-returning `Mult` unchanged; forward-looking note retained in prose), so the invariant's clause "Do NOT mark such an entry firm (the constructive sub-part isn't [firm])" was dissolved by reading "firm" as "no open promotion condition + structure confirmed." Compounding it: the CLAUDE.md invariant's enumerated lowering-verifier promotion route is "a **per-line** lowering-verifier audit" (an evidence upgrade to a positive site) whereas the theme's own `## Status` gate option (b) — the route actually invoked — was "a lowering-verifier audit that confirms the **shape is acceptable as a methodology-level pattern**" (a methodology-acceptance upgrade). Those are different routes; the producer dispatch folded the choice between them into a citation-refinement bundle without flagging it as a distinct decision.

**Sketch of procedure** (producer-facing for abstractor/lifter enacting a promotion; mirror-check for critic/integrator): before flipping a theme/operator from `partly-constructive` to `firm`, walk an explicit 4-point checklist and RECORD the answers in the promotion-record prose: (1) **Which promotion route?** Name it against the CLAUDE.md invariant's three enumerated routes — upstream positive source site / per-line lowering-verifier audit / literature-anchor upgrade — AND against the theme's own `## Status` gate; if the theme's gate and the invariant's routes are not the same condition, say so and justify which governs. (2) **Did the constructive sub-part's EVIDENCE change, or only the methodology acceptance?** If evidence is unchanged (still negative-anchor-only), state explicitly that "firm" is being read as "no open promotion condition," not "constructive sub-part now positively anchored" — this is the load-bearing interpretation and must be surfaced, not assumed. (3) **Two-dispatch protocol satisfied?** Confirm the UNBLOCK audit ran in a prior pass and the ENACT pass APPLIES (never defers) the audit-identified firming edits. (4) **Does the permanent honest content note survive the status flip?** The forward-looking-reconstruction note + negative anchors stay in prose; only the transient status gate drops. Critic/integrator then ratify the recorded route rather than inheriting it silently.

**Promotion bar check**: friction-ledger entry = none yet, but this is the first exercise of a cycle-012-codified mechanism and the interpretive ambiguity is concrete (two non-identical promotion routes that a producer can silently pick between); sketch concrete enough to write as SKILL.md = ✓; pattern observed ≥2 cycles = NO (single instance so far). Recommend meta-phase batch-2 either promote as a thin checklist skill OR fold the 4 points into the abstractor/lifter + critic agent specs as a promotion-record requirement. Re-evaluate after the next partly-constructive promotion (none other in flight as of cycle-013).

---
slug: classify-variant-axis-gs-orthog-example-drift
proposer: repairer (cycle-019, repair of 2026-05-29T023000Z-harvester-orthogonalize-l2)
proposed_at: cycle-019 / 2026-05-29
status: resolved
resolved_at: cycle-021 meta-phase / 2026-05-29
resolved_by: meta-phase in-place correction of skills/classify-variant-axis/SKILL.md:64-68 — CGS now `[dot×m, allreduce_sum, axpy×m]` (plain w.Add, no fused gemv_basis); CGS2 unconditional second pass (no refine_threshold); state binding drops the threshold scalar. Verified against orthog.hpp:65-89.
kind: skill-friction (example-staleness, not a missing procedure)
target_skill: skills/classify-variant-axis/SKILL.md
target_lines: 64-68 (the gs_orthog worked example block)
---

**Motivating observation**: the cycle-019 critic on the harvester `orthogonalize`-at-L2 report surfaced (drive-by, non-blocking) that the `classify-variant-axis` SKILL's own `gs_orthog` worked example (SKILL.md:64-68) is **stale / inaccurate vs the Palace L0**. The example lists `CGS = [dot×m, allreduce_sum, gemv_basis]` with a load-bearing `gemv_basis (rank-1 fused)`, and `CGS2 = [CGS chain]×2 + [axpy_scalar]` gated by a `refine_threshold` scalar "captured in setup." The actual `OrthogonalizeColumnCGS` (`orthog.hpp:65-89`, re-confirmed this repair via `palace-codemap read_range`) uses plain `w.Add` (an `axpy`, not a fused `gemv_basis`), and the `refine` branch is **unconditional — no threshold scalar is read**. The harvester report correctly diverged from the stale SKILL example toward the faithful L0 shape (`CGS = [dot×m, allreduce, axpy×m]`, `CGS2 = [CGS]×2`, `dH` pass-local, no threshold), so no error propagated into the artifact — but a future producer copying the SKILL example verbatim would import the drift.

**Sketch of fix** (meta-phase, skill-edit authority — NOT repairer; repairer must not modify `skills/`): correct the `classify-variant-axis` SKILL.md:64-68 `gs_orthog` worked example to match the verified L0 shape: `CGS` is `[dot×m, allreduce_sum, axpy×m]` (plain `w.Add`, no fused `gemv_basis`); `CGS2` is `[CGS chain]×2` with the `refine`/second pass **unconditional** (drop the `refine_threshold` scalar + its "captured in setup" state-binding line). The now-firm `book/src/L2/orthogonalize.md` (cycle-019) + the firm L1 leaf + `orthog.hpp:65-89` are the authoritative reference for the corrected example.

**Promotion-bar note**: this is a skill *example correction*, not a new skill or a procedure gap — the procedure (`classify-variant-axis`) is sound; only its worked example drifted from source. Lowest-cost fix is a meta-phase in-place edit of the example block. Considered for a `problems/` skill-friction filing by the critic; logging here instead keeps it on the meta-phase's standing skill-maintenance channel. Pattern observed = 1 instance (cycle-019).

---
slug: verify-intro-firmness-survey-against-on-disk-status-lines
proposer: critic (cycle-020, critique of 2026-05-29T034441Z-layer-intro-author-l2-refresh)
proposed_at: cycle-020 / 2026-05-29
status: promoted-as-role-spec
promoted_to: .claude/agents/layer-intro-author.md §Discipline ("Survey chapter firmness from the on-disk `## Status`, NOT the cycle record" bullet)
promoted_at: cycle-021 meta-phase / 2026-05-29
promotion_note: NOT promoted as a standalone skill. This candidate's root cause (an intro-refresh surveying firmness from the cycle record rather than the on-disk `## Status`) is the DOWNSTREAM symptom of the cycle-019 fence-truncation defect (`firm-chapter-body-authored-outside-proposed-changes-fence`); the high-leverage fix is the UPSTREAM critic build-readiness guard (promoted as `proposed-changes-fence-encloses-full-body-guard`). The downstream survey-check is folded into the layer-intro-author Discipline as a one-line "survey firmness from on-disk `## Status`" bullet rather than a separate skill — the two candidates are two ends of one defect.
---

**Motivating observation**: the cycle-020 L2-intro-refresh report built its dep-map + Vocabulary-cohort split from a firmness survey claimed "verbatim from chapter headers." Six of seven rows were accurate, but `book/src/L2/orthogonalize.md` was surveyed `firm` while on disk it is a 14-line preamble with **no `## Status` line and none of the firm apparatus** (Signature/laws/variant-axis/Evidence) that the other four firm chapters carry. Root cause was an *upstream* cycle-019 integrator landing gap (commit `efb8a0b` stripped the stub banner without landing the firm body; the cycle-019 log still recorded the promotion). An intro-refresh that surveys firmness from the *cycle log / recorded state* rather than the *actual on-disk chapter status line* will faithfully propagate such a landing gap into the navigational source-of-truth. This is the second cycle in a row that `orthogonalize.md` drift surfaced at critique (cycle-019: the `classify-variant-axis` example; cycle-020: the on-disk firm-body gap).

**Sketch of procedure** (producer-facing for layer-intro-author; mirror-check for critic): when an intro/dep-map refresh asserts a maturity status for any chapter, do not trust the cycle record — for each chapter slug, open the file and locate its explicit status declaration (`## Status` section line, or a `> **Status: \`...\`**` stub banner), and copy the literal status from there. If a chapter the record calls `firm` has NO status line and lacks the firm apparatus (Signature + Algebraic-laws + variant-axis + Evidence), do not label it `firm` in the intro — flag the on-disk/record mismatch as an open question (likely an upstream integrator landing gap) and survey it at its actual on-disk maturity. The procedure is a 7-line-per-chapter read; it is exactly the cheap check that would have caught the cycle-019 gap before it propagated into the L2 Part overview.

**Promotion-bar note**: sketch concrete enough to write as a thin SKILL.md = ✓ (a deterministic per-chapter status-line read + apparatus-presence check); pattern observed ≥2 cycles = borderline (the firmness-survey *verification* gap is new this cycle, but `orthogonalize.md` drift is the second consecutive cycle of surface/record divergence on the same file). Recommend meta-phase batch-5 either promote as a thin checklist skill OR fold the "read on-disk status line, not the cycle record" rule into the layer-intro-author + critic specs. Independent of this skill, the underlying cycle-019 `orthogonalize.md` firm-body landing gap should be routed to the plan/OQ for a harvester or integrator backfill.

---
slug: sibling-slice-citation-reanchor-sweep
proposer: critic (cycle-020, critique of 2026-05-29T034441Z-lifter-gmres-l4-self-rotation)
proposed_at: cycle-020 / 2026-05-29
status: promoted-as-skill-extension
promoted_to: skills/verify-citation-range/SKILL.md §"Sibling-slice / inherited-precedent re-anchor sub-case"
promoted_at: cycle-021 meta-phase / 2026-05-29
promotion_note: enacted per the candidate's own recommendation — folded into the existing `verify-citation-range` skill as a THIRD sub-case (after the cycle-012 audit-report/inherited-citation sub-case) rather than a standalone skill. The reduced-slice-drift mechanism is the same one `phase-1-slice-reduction-audit` + the focus-slice sweep already operate on; the gap is specifically the sibling/inherited citation. Friction-ledger `sibling-slice-citation-reanchor-sweep-gap` (addressed).
---

**Motivating observation**: the cycle-020 lifter `gmres` §L4 v0.6→v0.7 dispatch correctly diagnosed that the `gmres` slice was *reduced* (its v0.1 form lifted to firm entries, v0.6 moved `:1067-1078`→`:594-606`) and swept every drifted `gmres.md:NNN` ref in the theme it firmed — a clean, correct re-anchor. But it re-emitted `cg.md:215-219` (the CG `iterate_while` precedent) in three places (one retained, two in NEW v0.7-append content) without checking that `cg.md` had undergone the *same* reduction: `cg.md` is now 166 lines and its v0.4 `iterate_while` form was lifted to `L4/krylov-step.md`, so `cg.md:215-219` is out of range. A reduction-class drift was caught for the focus slice and missed for a *sibling slice* cited in the same paragraphs. The reduced-slice stub-header (every reduced slice carries one, listing which firm entries superseded which sub-ranges) is the signal that a slice's old line-refs are presumptively stale.

**Sketch of procedure** (producer-facing for lifter/abstractor doing a citation re-anchor; mirror-check for critic): when a dispatch's premise is "slice X was reduced, so re-anchor its refs," enumerate ALL `<slice>.md:NNN` citations in the touched/authored content — not just `<focus-slice>.md` refs. For each *distinct* slice cited, open it and check for a reduced-slice stub-header (`# Slice: <name> (reduced)` / "**Firm entries that supersede...**"). If present, treat every numeric line-ref into that slice as presumptively drifted: verify the ref resolves to the claimed content on the *current* file, and if the cited form was lifted away (named in the stub-header's supersedes list), re-anchor to the firm home rather than the dead slice range. A sibling slice cited as a "precedent rendering" is the high-risk case (precedents are exactly the v0.1–v0.4 forms most likely to have been lifted). The check is one read + stub-header scan per distinct cited slice.

**Promotion-bar note**: this overlaps `verify-citation-range` (cycle-012 extension already added an "Audit-report / inherited-citation sub-case"); the cleanest promotion may be a third sub-case in that existing skill ("sibling-slice / inherited-precedent re-anchor: enumerate all distinct cited slices, not just the focus slice; check each for a reduced-slice stub-header") rather than a new standalone skill. Pattern observed = 1 instance (cycle-020), but the reduced-slice-drift mechanism is the same one the cycle-012 `phase-1-slice-reduction-audit` skill and this report's own (correct) `gmres.md` sweep already operate on — the gap is specifically the *sibling/inherited* citation, which the focus-slice sweep structurally skips. Recommend meta-phase batch-5 fold into `verify-citation-range`.

---
slug: proposed-changes-fence-encloses-full-body-guard
proposer: critic (cycle-020, critique of 2026-05-29T034441Z-harvester-orthogonalize-l2-backfill)
proposed_at: cycle-020 / 2026-05-29
status: promoted
promoted_to: skills/proposed-changes-fence-encloses-full-body-guard/SKILL.md
promoted_at: cycle-021 meta-phase / 2026-05-29
promotion_note: promoted as a thin critic build-readiness checklist skill AND folded into the critic's `cross-reference-integrity` check (build-readiness guard) + a producer-spec reinforcement bullet across harvester/abstractor/lifter/lowering-verifier (the agents that author/flip firm bodies). The dispatch-prompt guidance held clean cycle-020/021 (zero recurrence) — promoted so the fix is STRUCTURAL (critic-side, durable) rather than per-dispatch-reminder-dependent. Friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` (addressed). The sibling candidate `verify-intro-firmness-survey-against-on-disk-status-lines` (downstream symptom) is folded into layer-intro-author Discipline; this guards the upstream cause.
---

**Motivating observation**: the cycle-019 `orthogonalize` L2 harvester authored a fully-vetted firm chapter body but left only the 14-line intro INSIDE the `edit:book/src/L2/orthogonalize.md` fenced block — the `## Context` … `## Evidence` sections were authored as the *report's own* top-level sections, OUTSIDE the fence. The integrator landed only the intro, so `book/src/L2/orthogonalize.md` shipped as a 14-line intro-only chapter while the dep-map row and `SUMMARY.md:41` both said `firm`. The cycle-019 critic+repairer validated the *content* (citations correct) but did not catch that most of the content never entered the artifact, because the report's prose carried it and the critique focused on claim/citation correctness, not on which lines sat inside the proposed-changes fence. This is a producer-side fencing-discipline defect, structurally distinct from the citation-drift family: a well-formed, well-cited body that is *partially outside the apply boundary*. The cycle-020 backfill (this report) recovers it correctly — closing fence after Evidence, verified — but the original defect went undetected for a full cycle.

**Sketch of procedure** (critic-facing build-readiness guard; also a producer self-check): for any report carrying a `\`\`\`edit:<path>\`\`\`` (or `new:`) proposed-changes block that purports to land a *full* chapter, verify the block's closing fence sits AFTER the last content section the report intends to land — concretely: (1) enumerate the fence lines (`grep -n '\`\`\`'`); confirm even parity and that nested `\`\`\`text`/`\`\`\`` code fences inside the block are balanced; (2) identify the LAST section header the report's prose treats as part of the chapter (typically `## Evidence`) and confirm the block-closing fence is on a line AFTER it, not before `## Context`; (3) cross-check the maturity claim: if the report (or the dep-map/SUMMARY it relies on) asserts `firm`, the enclosed block must contain the firm apparatus (`## Status` + Signature + Algebraic-laws + Evidence) INSIDE the fence — not merely in the report's surrounding prose. A `firm` claim whose proposed-changes block carries only an intro is the signature of this defect. The check is a fence-enumeration + one "is `## Status` inside the block?" scan.

**Promotion-bar note**: sketch concrete enough to write as a thin SKILL.md = ✓ (deterministic fence-parity + last-section-inside-block + apparatus-inside-block scan); pairs naturally with the `verify-intro-firmness-survey-against-on-disk-status-lines` candidate above (that one catches the *downstream* dep-map/SUMMARY-vs-on-disk divergence; this one catches the *upstream* cause — the body that never entered the artifact). The report itself recommends a friction-ledger entry + a critic `cross-reference-integrity`/build-readiness guard for the same pattern. Pattern observed = 1 root instance (cycle-019), surfaced via the cycle-020 backfill. Recommend meta-phase batch-5 either promote as a thin critic checklist skill OR fold the fence-encloses-full-body rule into the critic's `cross-reference-integrity` check + a producer-spec reinforcement ("the firm body must be INSIDE the proposed-changes fence; do not author chapter sections as the report's own top-level sections").

```yaml
---
slug: upgrade-plain-text-ref-to-live-link-when-target-on-disk
proposer: repairer
proposed_at: cycle-022 / 2026-05-29
status: promoted
promoted_to: skills/upgrade-plain-text-ref-to-live-link-when-target-on-disk/SKILL.md
promoted_at: cycle-024 meta-phase / 2026-05-29
promotion_note: promoted as a thin repairer skill (default-accept under low-bar). The in-cycle live-link-upgrade pattern recurred across all three batch-6 cycles (cycle-022 ×2, cycle-024 ×2), well above the single-instance the candidate noted. The skill is the deterministic on-disk-partition + convention-survey + relative-path-upgrade + re-verify procedure behind that upgrade.
---
```

**Motivating observation**: cycle-022 critic flagged (finding 2) that the `nleps_deflated_residual` L1 harvest referenced `linear_combination` as plain-text on the rationale "it's an L2 operator, cited upward per high→low discipline" — and lumped it with three *genuinely-absent* forward-refs (`deflate`/`gram`/`lu_solve`). But `book/src/L2/linear_combination.md` is on disk (firm, 23 KB), so the plain-text choice was a missed live-link, and the §Supporting-evidence prose risked telling the integrator the file was missing. The repair required (a) verifying which referenced slugs are actually on disk vs absent, (b) surveying the artifact convention (other firm L1 entries — `ksp_solve`, `chebyshev-smoother`, `orthogonalize` — already live-link UPWARD to existing L2 chapters; the high→low discipline governs how semantics are *defined*, not whether a cross-reference *link* is live), and (c) upgrading only the on-disk reference to a live link while leaving the genuinely-absent ones plain-text. This is the inverse of the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention: that convention forbids live-linking a MISSING target; this case is an on-disk target needlessly left plain-text. The two are easy to conflate ("don't define downward" gets misread as "don't link downward"), which is exactly the producer error here.

**Sketch of procedure** (repairer-facing; also a producer self-check): for each cross-reference a report keeps plain-text on a "forward-ref / upward-discipline" rationale, (1) `ls`/`test -f` the candidate target path to partition references into on-disk vs absent; (2) for on-disk targets, check whether the artifact already live-links the same KIND of reference (e.g. `grep -rn '../L2/' book/src/L1/*.md` to confirm L1→existing-L2 upward live-links are conventional); (3) if conventional, upgrade the plain-text mention to a live link at the canonical declaration site (the §Dependencies row + any dep-map cell) using the correct relative path, and re-verify the path resolves (no dead-link risk); (4) leave genuinely-absent targets plain-text and, if the report-prose lumped the on-disk one with them, correct the prose so the integrator is not misled. Net: a deterministic on-disk partition + convention-survey + relative-path upgrade, bounded and safe (the dead-link direction is the only hazard and step 3's path re-verification closes it).

**Promotion-bar note**: sketch concrete enough to write as a thin SKILL.md = ✓ (on-disk partition + convention grep + relative-path upgrade + re-verify). Pattern observed = 1 instance so far (cycle-022). Recommend meta-phase either promote as a thin repairer skill OR fold the "on-disk → live-link, absent → plain-text" partition rule into `verify-citation-range`/`verify-rotation-citation` as a cross-reference sub-case. Distinct from the existing fence-discipline candidates (those concern whether content lands at all; this concerns link maturity of references that DO land).

```yaml
---
slug: convert-nested-fences-to-indented-code-in-proposed-changes-block
proposer: repairer
proposed_at: cycle-023 / 2026-05-29
status: promoted
promoted_to: skills/convert-nested-fences-to-indented-code-in-proposed-changes-block/SKILL.md
promoted_at: cycle-024 meta-phase / 2026-05-29
promotion_note: promoted as the repair-side counterpart to the detection guard `proposed-changes-fence-encloses-full-body-guard`. The root defect (firm body outside the apply boundary) recurred in a fresh nested-`text`-fence variant cycle-023 (recurrence-2 of friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence`); detection held (the critic guard caught it) but the repair is identical every time. Also enacted: a producer-spec bullet (use 4-space-indented code, not nested fences) across the 4 firm-body-authoring producers + lowering-verifier.
---
```

**Motivating observation**: cycle-023's `lu-solve-mutation-rotation` L1>L0 abstractor authored its firm chapter body inside a `\`\`\`new:book/src/L1-L0/lu-solve-mutation-rotation.md\`\`\`` block, but rendered the four code samples (L1 signature, L0 skeleton, Sub-pattern A, Sub-pattern B) as **nested `\`\`\`text … \`\`\`` fenced blocks** rather than the 4-space-indented code blocks the landed L1>L0 siblings (`dot-mutation-rotation.md`, `assemble-diagonal-mutation-rotation.md`) use. Under flat CommonMark fence-toggle parsing the first bare inner `\`\`\`` closed the `new:` block early, leaving `## Status` and the entire firm apparatus OUTSIDE the captured content — the cycle-019 fence-truncation defect signature (friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence`, marked `addressed`) recurring in a **new variant form**. Notably the promoted critic guard `proposed-changes-fence-encloses-full-body-guard` WORKED — the critic caught it (`cross-reference-integrity: fail`, with the fence-pairing arithmetic spelled out) — so detection is solid; what recurs is the *repair*, which is identical every time: convert each nested `\`\`\`text` block to a 4-space-indented block (strip the open/close fence lines, indent each content line by 4 spaces), preserving content verbatim, so the `new:`/`edit:` block has exactly one open + one close bare fence.

**Sketch of procedure** (repairer-facing; mechanical, surgical): (1) `grep -n '\`\`\`'` the report; if a `new:`/`edit:` proposed-changes block contains inner `\`\`\`lang … \`\`\`` fences, the block will mis-toggle. (2) For each nested fenced code block inside the proposed-changes block: delete the opening ` \`\`\`lang ` and closing ` \`\`\` ` lines, and prefix every content line (including blank-but-significant lines as appropriate) with 4 spaces — this is the CommonMark indented-code-block form the landed siblings use. (3) Preserve all code content byte-for-byte; only the fence mechanism changes. (4) Re-run `grep -c '\`\`\`'`: confirm the count dropped to exactly 2 × (number of proposed-changes blocks), all paired, and that `## Status` / the firm apparatus now sit inside the relevant `new:`/`edit:` block (header line-number < the block's closing-fence line-number). The sibling reference to copy the exact indent pattern from is `book/src/L1-L0/dot-mutation-rotation.md`.

**Promotion-bar note**: sketch concrete enough to write as a thin SKILL.md = ✓ (deterministic fence-enumeration + per-block strip-fence/indent-4 + re-count-and-locate-`## Status`). This is the **repair-side counterpart** to the promoted detection guard `proposed-changes-fence-encloses-full-body-guard` (that skill/critic-check finds the defect; this one fixes it). Recurrence note: friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` is marked `addressed` (critic guard promoted batch-5), but cycle-023 is a fresh producer-side recurrence in the nested-`\`\`\`text` variant — meta-phase may want to (a) note the recurrence on that ledger entry, and (b) reinforce the producer-spec bullet for harvester/abstractor to use 4-space-indented code inside proposed-changes blocks (NOT nested fences) when authoring firm bodies, per the landed-sibling convention. Pattern observed: the repair shape recurs (cycle-019 top-level-sections variant + cycle-023 nested-fence variant = 2 instances of the same root defect needing a mechanical fence-mechanism repair).

```yaml
---
slug: audit-slug-meaning-before-coordinated-cross-report-rename
proposer: repairer
proposed_at: cycle-027 / 2026-05-29
status: promoted
promoted_to: skills/audit-slug-meaning-before-coordinated-cross-report-rename/SKILL.md
promoted_at: cycle-027 meta-phase / 2026-05-29
promotion_note: promoted as a thin repairer skill (default-accept under low-bar). The cycle-027 D4/D5 slug collision produced a coordinated-rename instruction whose premise was INVERTED relative to the artifact; the D5 repairer's denote-by-signature audit caught it, applied zero edits, and routed the real (inverse) gap as unrepairable. Concrete + high-cost hazard (an inverted rename corrupts correct references while missing the real gap). Friction-ledger `coordinated-cross-report-rename-premise-inversion`. A companion ASK (pre-harvest slug-collision check as a standing producer-spec bullet) is surfaced to the human in the cycle-027 meta-phase report.
---
```

**Motivating observation**: cycle-027 dispatch-5 (`incremental-ls-composition-lowering` L2>L1 theme) was handed a coordinated cross-report rename: dispatch-4's terminal back-solve leaf was renamed `ls_update_column` → `back_solve` (collision — `ls_update_column` already named the column-streaming step `(K,j,h_new)→K'` in `L2/incremental-least-squares.md:412` + `concepts/incremental-least-squares.md:14`, while the back-solve is `back_solve` at `L2/...:81-83`). The dispatch told the repairer "this theme forward-references the **terminal back-solve leaf** as `ls_update_column` (Face-1); rename those → `back_solve`, but do NOT touch column-streaming-step references." An exhaustive grep of every `ls_update_column` occurrence in the theme showed the **opposite**: every `ls_update_column` reference meant the *column-streaming step* (signature `ls_update_column :: (K, j, h_new) -> Krylov'`, Face-1), NONE meant the back-solve leaf — and the back-solve target was referenced under a DIFFERENT slug (`trsv` / `back_solve` / `trsv_upper`). So the literal rename target set was **empty** (the CAUTION protected exactly the references that existed), and the genuine consistency gap was the *inverse* (`trsv` back-solve-target vs dispatch-4's landed `back_solve` slug) — a cross-report content reclassification dispatch-4's own critic had already flagged, hence `unrepairable`, routed to the integrator. Blindly trusting the dispatch premise would have corrupted the theme (renaming correct streaming-step refs) while leaving the real gap unfixed.

**Sketch of procedure** (repairer-facing; mechanical, surgical): when handed a coordinated cross-report rename of a slug whose name is overloaded/colliding, BEFORE applying any edit: (1) read the *landing* report to confirm what slug it actually creates on-disk (`grep -n '\`\`\`new:' <landing>/CYCLE.md`) and the leaf's signature — establish ground truth, not the dispatch's paraphrase; (2) `grep -n '<old-slug>'` every occurrence in the report under repair and classify each by the *operation it denotes* (read the signature / surrounding prose), partitioning into rename-target meaning vs protected meaning; (3) if the partition contradicts the dispatch's stated premise (e.g. zero references match the rename target, or the references all fall under the CAUTION's protected meaning), the literal rename is a **no-op** — apply zero edits and record `not-needed` for the rename, then assess whether a *different* slug carries the real consistency gap; (4) if the real gap is a content reclassification (which slug IS the lowering/landing target — an overload disambiguation, not a 1:1 string swap), mark it `unrepairable` and route to the integrator/follow-up, citing the landing report's own critic flag if present. Net: an exhaustive denote-by-signature audit gates the rename; the dispatch premise is verified against the artifact, not assumed.

**Promotion-bar note**: sketch concrete enough to write as a thin SKILL.md = ✓ (landing-report ground-truth read + per-occurrence denote-by-signature partition + premise-contradiction gate + reclassification→unrepairable routing). Pattern observed: 1 instance (cycle-027). This is a *generalization* of the existing `verify-citation-range` "verify the claim against on-disk source, not the producer's paraphrase" discipline, applied to slug-rename coordination rather than citation ranges. Recommend meta-phase either promote as a thin repairer skill OR fold the "verify rename premise against the artifact before applying" gate into the repairer role-spec's cross-reference-repair authority bullet. The hazard it guards is specific and high-cost: a coordinated rename whose dispatcher premise is inverted relative to the artifact, which (if trusted) corrupts correct references while missing the real gap.

```yaml
---
slug: establish-negative-finding-exhaustiveness
proposer: critic
proposed_at: cycle-028 / 2026-05-29
status: promoted
promoted_to: skills/establish-negative-finding-exhaustiveness/SKILL.md
promoted_at: cycle-030 meta-phase (batch-8) / 2026-05-30
promotion_note: promoted as a thin producer- and critic-facing skill (default-accept under low-bar). The negative-localization-with-routing shape recurs across the unimplemented-stub / opaque-library obstruction family (≥3 prior instances: cycle-004 minres/bicgstab, cycle-024 eigsolve opaque-library, cycle-028 trsv, cycle-029 triangular-solve-obstruction). The skill is the deterministic 5-step bar: stated-terms + broadened-sweep + residual-token accounting + positive-API confirmation + critic re-run. Companion to `verify-citation-range` (positive pinpoints) — this one sets the bar for the *absence* claim. Friction-ledger entry NOT opened (the procedure is captured in the skill; no recurring failure to ledger).
---
```

**Motivating observation**: cycle-028's `harvester-trsv-l1-localization` dispatch is a **negative-localization-with-routing** report — its entire deliverable is "Palace has NO standalone `trsv` primitive, therefore route the OQ leaf to obstruction rather than leaving it BLOCKED." The load-bearing claim is a negative ("zero hits"), which is exactly the shape that needs an exhaustiveness standard: a negative finding routes a real methodology decision (obstruction-theme target vs perpetually-blocked-pending-anchor), so a sloppy or term-narrow search that *missed* a hit would mis-route. This report did it well by hand — two stated codemap searches with explicit terms, plus an implicit accounting that every residual `triangular` token in the tree is a known non-`trsv` red herring — and a critic re-running the searches reproduced zero-hit and confirmed all 8 `triangular` mentions are accounted-for. But there is no skill naming the bar, and the same shape recurs across the unimplemented-stub / opaque-library obstruction pattern (the `minres`/`bicgstab` stubs, the `eigsolve` opaque-library loop, any future "does Palace expose X?" routing dispatch). Crystallizing the procedure would give producers and critics a consistent exhaustiveness bar instead of re-deriving it per dispatch.

**Sketch of procedure** (producer- and critic-facing): to establish a negative finding strong enough to route a methodology decision: (1) state the search terms explicitly and include casing/synonym variants of the target symbol (`trsv|trsm|TriSolve|TriangularSolve|SpTrSV` + a broadened bare-stem case-insensitive sweep, e.g. `triangular`); (2) run the searches against the in-scope tree (Palace source, not vendored upstream) and record the hit count; (3) **account for every residual hit** of the broadened sweep — classify each as either a genuine hit (negative finding fails) or a named non-target (red herring / different-family object), so no token is hand-waved; (4) confirm the relevant public-API surface positively (e.g. enumerate `densematrix.hpp`'s exported functions) to show the absence is structural, not a search miss; (5) the critic re-runs the producer's stated searches and the broadened sweep and confirms the count + that every residual token is positively accounted-for. The negative finding is established only when steps (3) and (4) leave no unexplained token.

**Promotion-bar note**: sketch concrete enough to write as a thin SKILL.md = ✓ (stated-terms + broadened-sweep + residual-token accounting + positive-API confirmation + critic re-run). Pattern observed: the negative-localization-routing shape recurs across the unimplemented-stub / opaque-library obstruction family (≥2 prior instances: `minres`/`bicgstab` obstruction themes, `eigsolve` opaque-library partial-obstruction). Companion to `verify-citation-range` (which verifies positive pinpoints); this one sets the bar for the *absence* claim. Meta-phase may fold into the critic's `surface-or-evidence` check guidance (the negative-evidence sub-case) rather than a standalone skill.

```yaml
---
slug: verified-against-note-no-leading-quote-of-either-kind
proposer: repairer
proposed_at: cycle-030 / 2026-05-30
status: promoted
promoted_to: skills/verified-against-note-no-leading-quote-of-either-kind/SKILL.md
promoted_at: cycle-030 meta-phase (batch-8) / 2026-05-30
promotion_note: promoted as a thin producer/critic/repairer-facing channel-format skill (default-accept under low-bar; concrete + recurrence-2). The c028 leading-double-quote-only rule was too narrow — c030 single-quote variant slipped past the producer self-check that named only the narrower form. The generalized predicate (note value's first non-whitespace character ∈ {`'`, `"`}) is the leverage point. Three sites updated: (a) lowering-verifier role-spec `verified_against:` Discipline bullet (generalized rule + producer self-check + yaml.safe_load mechanical check); (b) critic role-spec `citation-validity` check (YAML round-trip sub-check on extracted `verified_against:` blocks); (c) this skill (deterministic repair pattern). Friction-ledger entry opened: `verified-against-note-no-leading-quote-of-either-kind` (recurrence-2 generalizing the c028 narrower hazard).
---
```

**Motivating observation**: cycle-028 surfaced the `verified_against:` YAML channel-format hazard "no `note:` value may begin with a literal DOUBLE quote (`"`)" because a leading `"` opens a double-quoted scalar and the trailing prose after the closing `"` causes `yaml.safe_load` to fail with `ParserError: expected <block end>, but found '<scalar>'`. Cycle-030 (this repair) caught the **same defect in the single-quote variant**: the `bilinear-form-mutation-rotation` audit's proposed `verified_against:` block had two rows whose `note:` values began with a literal SINGLE quote (`'`), producing the identical `ParserError` at the second occurrence. The producer self-check in the report Summary explicitly claimed "no leading-double-quote note values (yaml.safe_load hazard avoided)" — exactly the narrower form of the c028 rule — and the single-quote variant slipped past. The repair was mechanical (rephrase each note to not begin with any quote character), but the recurrence shows the rule as codified after c028 is **too narrow**: the hazard is "begins with `'` OR `"`", not just `"`.

**Sketch of procedure** (producer- and critic- and repairer-facing): the channel-format rule for `verified_against:` `note:` values should be: **"no `note:` value may begin with a quote character of either kind (single `'` or double `"`)"** — because YAML's plain-scalar parser interprets a leading quote of either kind as opening a quoted scalar, and any trailing unquoted prose after the closing quote breaks the block. (1) Producer self-check: before emitting a `verified_against:` block, scan each `note:` value's first non-whitespace character; if it is `'` or `"`, rephrase the note to start with a non-quote character (e.g. `note: section header "X" — ...` instead of `note: 'X'; ...`). (2) Critic check: extract the proposed `~~~yaml ... ~~~` block, run `python3 -c "import yaml; yaml.safe_load(open(...))"`, flag `citation-validity: fail` if it doesn't parse, and identify the failing row by line+column from the `ParserError`. (3) Repairer fix: rephrase each affected note so the scalar begins with prose, preserving the quoted term inside the body of the note rather than at its start. The cycle-030 fix-shape for examples: `note: 'X — content'; ...` → `note: section header "X" — content; ...` (adds a non-quote prefix that converts the scalar to a plain string YAML reading, with any inner quoted term safely embedded).

**Promotion-bar note**: this is a **refinement** of the c028-flagged leading-DOUBLE-quote hazard. Pattern observed: 2 instances now (c028 = double-quote variant; c030 = single-quote variant). The batch-8 meta-phase (firing after this c030 cycle) should codify the broadened rule in the channel-format spec — promotion route is most naturally an update to the `verified_against:` channel-format spec wherever the c028 rule landed (or, if it wasn't landed as a written rule, codify both in one go), plus a producer-self-check bullet in `lowering-verifier.md` and an extracted-block `yaml.safe_load` parse check in the critic role-spec (or in `verify-citation-range` as a sub-step for audit reports). The narrower c028 phrasing is what allowed c030 to slip — the producer's Summary said exactly "no leading-double-quote note values" and faithfully avoided that — so the channel-format spec update is the leverage point, not a new skill per se.
