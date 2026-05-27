---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T19:35:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T19:50:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: unrepairable
overall_status: ready
follow_up_agent: null
---

# META: verification of CYCLE — Combinator candidate — check_stop_into_carry (defer)

## Critique

### Checks run

**citation-validity** — Direct verification of the 8 cited source ranges and 4 spec-file citations: (a) GMRES `iterative.cpp:615-650` confirmed (line 645 is the 3-condition break exactly as quoted; line 644 sets `converged`); (b) FGMRES `iterative.cpp:794-828` confirmed (line 824 is the textually-identical break); (c) NLEPS `nleps.cpp:589-647` confirmed (predicate at line 590 `while (it < nleps_it)`; converged break at line 600 `if (res < rtol)`; diverged break at line 636 `if (diverged_it > 10)`; total file length 952 lines matches the claim at line 119); (d) ARPACK `arpack.cpp:315-353` confirmed (RCI `while (true)` with `ido` state machine); (e) SLEPc `slepc.cpp:687-694` confirmed (single `EPSSolve(eps)` call at line 694); (f) Chebyshev `chebyshev.cpp:194,265` confirmed (`for (int it = 0; it < pc_it; it++)` bounded counter at both); (g) Transient `transientsolver.cpp:77` confirmed (`for (int step = 0; step < n_step; step++)` bounded counter); (h) PCG `iterative.cpp:427-464` confirmed (`for (; it < max_it && !converged; it++)` 2-condition stop). All spec-file citations (`gmres.md:3,91,122`, `cg.md:215-219`, `axpbypcz-mutation-rotation.md:127-132,294-297`, `apply-linop-mutation-rotation.md:337`, `axpby-mutation-rotation.md:213`, `gmres.md:129`) check out in-range. **However**, two warning-level issues: (1) the report's line 12 (`The §Status block set a promotion criterion: "defer until a second slice needs it."`) and line 74 (`The cycle-008 theme's status block already records the promotion criterion`) attribute the promotion criterion to the cycle-008 theme file's §Status block; direct inspection of `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:196-202` shows the §Status block does NOT contain this criterion or the phrase "second slice". The criterion actually lives in the cycle-008 abstractor's CYCLE.md at line 71 (and is referenced in `scaffolding/open-questions.md:1316`). The attribution should be to the cycle-008 abstractor report, not the theme file. (2) Internal inconsistency: line 26 cites `axpbypcz-mutation-rotation.md:127-132,295-297` while line 106 cites the same source as `:127-132,294-297`. Both ranges are valid (both contain nleps entries) but the two readings in one report disagree by one line on the start of the second range — minor but suggests a copy/transcription drift. Verdict: **warning** (cited source line ranges all in-range and substantive claims verify; misattribution of criterion-source and one cross-reference inconsistency).

**surface-or-evidence** — The report is explicitly inspection-only with verdict `defer`. The §Proposed changes block (lines 72-84) correctly states "no proposed changes to L4 dep-map" and contains exactly one optional, contingent surgical edit suggestion (append-only paragraph to the cycle-008 theme's §Status section), with an explicit caveat at line 84 routing the §Status-edit decision to the integrator and offering an OQ-shaped alternative. The report is consistent with combinator-miner authority ("just the dep-map entry") and the cycle-009 dispatch-spec ("STRICTLY proposed-changes channel — do NOT directly edit book/"). This is not a refinement-shaped proposal at all — it is a retroactive-evidence dispatch (verdict-only on cycle-008's promotion criterion). The single optional surface edit, if applied, would be a paragraph append to the §Status block that records this dispatch's survey outcome as evidence; it does not modify the speculative-helper signature or any existing semantics. Verdict: **pass**.

**rotation-quality** — Not applicable to this inspection-only dispatch; the report explicitly does not assert a rotation (the cycle-008 theme owns the L4>L3 rotation under examination). The report at line 48 reproduces the cycle-008 signature for context but does not claim any new rotation. Marked **pass** (not applicable to inspection report).

**variant-axis-coverage** — The variant-absorption claim on FGMRES (`gmres.md:3,91,122` `op.flexible`) is sound: `gmres.md:3` explicitly says "Lifts Palace's restarted GMRES and FGMRES solvers"; `gmres.md:91` says "The outer/inner structure is identical for GMRES and FGMRES; the (fixed-vs-flexible) axis is absorbed by the choice of basis (V vs. Z) the correction step closes over"; `gmres.md:122` says "`flexible` — inspected only at the `K.Z[K.j] = z` capture and inside `apply_correction`'s basis selection. FGMRES configures this once at construction." All three citations support the report's "variant-absorbed into one slice" claim. The report also enumerates variant axes for the speculative helper at lines 67-70 (stop-reason set, cardinality, predicate purity) and explicitly flags the parametric-over-`[StopCondition]` over-engineering tradeoff at lines 67-68 and OQ #2 (line 121). The §Open questions / caveats #3 (line 123) reflexively flags the "variant-absorption-vs-instance-counting policy question" as a cross-cutter concern out of combinator-miner scope and routes it to meta-phase. The survey itself enumerates instances and non-instances exhaustively across the 7-slice Krylov/eigenmode/transient surface (lines 18-43). Verdict: **pass**.

**cross-reference-integrity** — The cross-reference to the cycle-008 theme (`book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md`) resolves and the cited line ranges (`:36-58`, `:75-96`, `:130-144`, `:158-164`, `:196-202`) all map to the correct sections (L4 form / L3 form / applicability conditions / speculative L4 operators / status). The `[iterate-while]` link at line 12 resolves to `book/src/L4/iterate-while.md` (exists). The OQ slug references (`iterate-while-l3-rendering-trajectory-accumulation-gap`, `iterate-while-log-effect-vs-trajectory-channel`) both resolve in `scaffolding/open-questions.md`. The slice citations (`gmres.md`, `cg.md`) all exist under `book/src/spec/slices/`. The negative claim "no `book/src/spec/slices/nleps.md`" verified (directory listing shows 10 slices, no nleps). The L1-L0 references (`axpbypcz-mutation-rotation.md`, `apply-linop-mutation-rotation.md`, `axpby-mutation-rotation.md`) all exist. Verdict: **pass**.

**edge-label-fidelity** — Not strictly applicable (the report carries no edge label of its own — it discusses an existing L4>L3 theme without proposing a new edge). The prose at lines 12, 22, 48 is consistent with the cycle-008 theme's L4>L3 placement; the helper is correctly described as L4-layer (line 48 "L4 — where the cycle-008 theme placed the rough-in"; rationale: pure-function combinator over typed records, structural concern, L4 vocabulary). Where the report does discuss layer placement (e.g., line 48 L4 rationale; line 36 "the witness is a single `Bool` carry field, NOT a `Maybe StopReason`" for CG; line 27 "NOT yet in L1+ spec" for NLEPS), the layer references are internally consistent. Verdict: **pass**.

**plan-kind-consistency** — Frontmatter declares `scope: check_stop_into_carry helper-promotion decision (cycle-008 deferred criterion)` and `status: pending`. The content shape is verdict-only (defer); no rough-in / firm / theme content is introduced. The §Proposed changes block (lines 72-84) honors write-authority discipline: no book/ mutations proposed beyond an optional contingent §Status append (with the integrator-routing caveat at line 84). The combinator-miner-authority caveat is explicitly raised at OQ #6 (line 129). The "defer" verdict is appropriately scoped to the cycle-008 criterion (1 strictly-distinct L1+ slice with the multi-reason shape vs. the criterion's "second slice needs it" bar). The verdict matches the content shape — no over-claim, no surface-without-evidence, no surface-with-stale-evidence. Verdict: **pass**.

**skill-uptake-survey** — The report does not reference invocation of any skill, and the dispatch shape (survey across multiple Palace source ranges + multiple spec-file citations) is precisely the territory of `verify-citation-range` (per the 8-check critic checklist, this skill exists). The report cites 7+ source ranges and 8+ spec-file ranges; invoking `verify-citation-range` on each at authoring time would have caught the §Status-block-misattribution issue noted in citation-validity above (the cycle-008 theme's §Status block does not contain the criterion the report attributes to it). The dispatch also touches multi-formulation choice at OQ #2 (parametric vs monomorphic helper signature), where `plan-sideways-concept-emission` may have been applicable but is not referenced. Telemetry-only finding per skill-uptake-survey's pure-presence-check framing. Verdict: **warning** (skill telemetry: `verify-citation-range` not referenced despite a multi-citation survey; one missed catch in citation-validity directly traceable to non-invocation).

### Issues found

1. **CYCLE.md line 12 + line 74: §Status-block misattribution of promotion criterion** (citation-validity, severity: medium). The report attributes the "defer until a second slice needs it" promotion criterion to the cycle-008 theme file's §Status block. Direct inspection of `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:196-202` shows no such criterion text in the §Status block. The criterion's actual home is `reports/2026-05-27T180000Z-abstractor-gmres-inner-loop-iterate-while-migration/CYCLE.md:71` (sourced from the cycle-008 abstractor report's caveats, also recorded in `scaffolding/open-questions.md:1316`). Recommendation: replace "The cycle-008 theme's status block already records the promotion criterion" (line 74) with attribution to the cycle-008 abstractor report (and/or the open-questions ledger entry), or alternatively flag the §Status-block edit at lines 76-82 as the work that would actually first place the criterion in the theme file.

2. **CYCLE.md line 26 vs line 106: cross-reference inconsistency** (citation-validity, severity: low). Line 26 cites `axpbypcz-mutation-rotation.md:127-132,295-297` while line 106 cites the same file as `:127-132,294-297` — both ranges are valid (lines 294 and 295 are both nleps entries) but the two cite-instances disagree by one line. Pick one and use it consistently.

3. **CYCLE.md authoring-time skill non-invocation** (skill-uptake-survey, severity: low / telemetry). The dispatch surveys 7+ Palace source ranges and 8+ spec-file ranges; `verify-citation-range` is the standard skill for this shape and would have caught Issue #1 (§Status-block misattribution). Telemetry-only finding per skill-uptake-survey's pure-presence-check framing. Not blocking.

4. **CYCLE.md §Proposed changes block #1 ambiguity** (plan-kind-consistency, severity: low). The §Proposed changes block at lines 76-82 uses a non-standard `\`\`\`edit:...\`\`\`` fence with brace-bracketed instruction prose `[locate the §Status paragraph...]` rather than a literal append-block. The integrator's STAGING.md ingestion may not parse this shape as a standard CREATE/EDIT proposed-change. Combined with the line 84 caveat ("If the integrator finds the edit out-of-scope for combinator-miner authority..."), the report deliberately leaves the edit-decision to the integrator. Recommend either (a) reshape as a standard EDIT block with literal append-text, or (b) drop the edit entirely and rely solely on the OQ-shaped alternative referenced at line 84 (since the report itself flags the edit as "technically outside the combinator-miner's stated authority" at line 129).

## Repair

### Fixes attempted

- **Finding 1**: CYCLE.md line 12 + line 74 misattribute the "defer until a second slice needs it" promotion criterion to the cycle-008 theme file's §Status block; criterion actually lives in the cycle-008 abstractor's CYCLE.md line 71 (and OQ entry at `scaffolding/open-questions.md:1316`).
  - **Decision**: repaired
  - **Action**: Edited CYCLE.md §Summary (line 12) to re-attribute the criterion to `reports/2026-05-27T180000Z-abstractor-gmres-inner-loop-iterate-while-migration/CYCLE.md:71` (cross-referenced in `scaffolding/open-questions.md:1316`); and rewrote CYCLE.md §Proposed changes (lines 74-76) to state that the criterion is recorded in the abstractor report (and OQ) but is NOT yet recorded in the theme file's §Status block, and that placing it there is itself a follow-up edit out of combinator-miner authority. Surgical re-attribution; no substantive content added beyond pointer reshuffling.

- **Finding 2**: CYCLE.md line 26 cites `axpbypcz-mutation-rotation.md:127-132,295-297`; line 106 cites `:127-132,294-297`. One-line drift on the start of the second range.
  - **Decision**: repaired
  - **Action**: Verified both ranges by reading `book/src/L1-L0/axpbypcz-mutation-rotation.md`. Line 294 is `palace/linalg/nleps.cpp:343-344` (sub-pattern D, γ=1.0); lines 295-297 are the three sub-pattern-C γ=0 nleps entries that mirror the 127-132 block. The `:294-297` range is the more inclusive choice (covers all 4 nleps L0 call-site citations in that section). Aligned line 26 to `:127-132,294-297` to match line 106.

- **Finding 3**: `verify-citation-range` skill not referenced despite multi-citation survey shape; would have caught Finding 1.
  - **Decision**: unrepairable
  - **Rationale**: Telemetry-only finding about authoring-time skill invocation. The critic explicitly marked this as "Non-blocking; mark unrepairable" in the user's repair brief and as "Telemetry-only finding per skill-uptake-survey's pure-presence-check framing. Not blocking." in the META.md issue list. Skill-invocation telemetry is a producer-side authoring concern; the repairer cannot retroactively cause an agent to have invoked a skill. The procedural pattern (skill-uptake-survey warnings on multi-citation surveys when `verify-citation-range` is not invoked) is already on the friction-ledger / skill-candidates radar and is appropriately surfaced to meta-phase.

- **Finding 4**: CYCLE.md §Proposed changes block uses non-standard `\`\`\`edit:...\`\`\`` fence with brace-bracketed instruction prose that may not parse through STAGING.md ingestion; report deliberately defers the edit-decision to the integrator and offers an OQ-shaped alternative.
  - **Decision**: repaired
  - **Action**: Dropped the non-standard `\`\`\`edit:...\`\`\`` block from CYCLE.md (lines 76-84 in pre-repair form) per option (b) of the critic's recommendation, since the report itself flagged the edit as "technically outside the combinator-miner's stated authority" (CYCLE.md OQ #6, line 129). Replaced the block with a prose paragraph stating that no §Status edit is proposed and naming the two natural channels (Open-question entry, or lifter/abstractor dispatch on the cycle-008 theme) for any future incorporation. The §Proposed changes section now contains zero proposed-changes blocks, consistent with the `defer` verdict and the combinator-miner-authority caveat.

### Unrepairable findings

- **Finding 3** (skill-uptake-survey telemetry): `verify-citation-range` non-invocation. Telemetry-only, non-blocking. No follow-up routing needed — meta-phase already aggregates skill-uptake-survey trends as part of every-3rd-cycle methodology review.

## Suggested resolution

`overall_status: ready`. The two substantive findings (1, 4) are repaired with surgical, content-preserving edits: Finding 1 fixes the criterion-source attribution (pointer reshuffle, no semantic change to the verdict or evidence); Finding 4 drops a non-standard proposed-changes block that the report itself flagged as out-of-authority. Finding 2 is a one-line range alignment. Finding 3 is non-blocking telemetry. The report is consistent with combinator-miner authority (inspection-only, verdict `defer`, no dep-map row) and ready for integrator-per-report application — which will be a no-op on `book/` (the report proposes no book/ changes) and may surface OQ-shaped follow-ups per CYCLE.md §Open questions / caveats.
