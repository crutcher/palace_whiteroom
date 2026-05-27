---
verifies: ../REPORT.md
critiqued_at: 2026-05-27T174756Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: warning
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T183000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: unrepairable
overall_status: ready
follow_up_agent: null
---

# META: verification of L4>L3 theme sketch — gmres-inner-loop-iterate-while-migration (rough-in)

## Critique

### Checks run

**citation-validity** — Sampled and verified the primary C++ citations against `reference/palace/palace/linalg/iterative.cpp` and the L4 / L4-L3 / spec / concepts anchors. All major Palace L0 ranges line up: `int j = 0` at 614 ✓, `for (;; j++, it++)` at 615 ✓, body sequence ApplyBA/OrthogonalizeIteration/Norml2/ApplyPlaneRotation at 627–640 ✓, `beta = std::abs(s[j + 1])` + `CheckDot` + `converged = (beta < eps)` at 642–644 ✓, break-on-stop disjunction at 645–649 ✓, `s[0] = beta` at 612 ✓. The L4 / spec citations also check: `iterate-while.md:232` ✓ (with the embedded "line 644" sub-claim about *break-on-converged*; the actual break is at 645, while 644 is the `converged = ...` assignment — the report inherits this slightly imprecise wording when quoting iterate-while.md, but the imprecision is in the cited file, not introduced by this report), `gmres.md:459-470` (v0.1) ✓, `gmres.md:1067-1078` (v0.6) ✓, `gmres.md:1060-1065` (`check_stop`) implicit but in-range ✓, `cg.md:215-219` ✓, `krylov-step-typed-wrapper-dissolution.md:156-167` ✓, `concepts/derived-view-hoisting.md` "Worked example: CG residual norm" + §3.8 ✓, `concepts/sequential-obstruction.md` exists ✓, OQ slugs `gmres-inner-loop-iterate-while-migration`, `iterate-while-l3-rendering-trajectory-accumulation-gap`, `iterate-while-log-effect-vs-trajectory-channel` all present in `scaffolding/open-questions.md` ✓. **Warning** because: (a) the report cites `iterative.cpp:613-650` and `:614-705` for the inner loop, both technically overshooting the loop boundaries (the loop body is 614–650; the outer Mult function continues past, and 613 / 651+ are blank or unrelated) — the ranges are still informative but not minimum-bounding; (b) line 92 / 282 cites "`iterative.cpp:617-621`" for "per-iteration printing", which is accurate (the `print_opts.iterations` block is 617–621) but is cited in service of the *log-effect-not-trajectory* claim, which is correct ✓ (not a defect, just confirming).

**surface-or-evidence** — Rough-in shape is upfront in the YAML frontmatter (`status: pending`) and inline (line 25 "**rough-in / speculative**"); the proposal CREATES a new theme file (surface authoring), does NOT mutate the firm `iterate-while.md` or `krylov-step-typed-wrapper-dissolution.md` chapters, and does NOT promote `check_stop_into_carry` to firm (deferred per stated promotion criterion at line 68). The surface (new theme chapter) is paired with evidence (cited L0 + L4 + L4-L3 anchors) per the surface-or-evidence discipline. The dispatch correctly stays in speculative mode and does not over-claim firm semantics. Pass.

**rotation-quality** — L4 LHS (lines 141–178) uses the `iterate_while` combinator with Solve-monad body + predicate `\K -> isNothing K.stop_reason` + carry-augmenting `check_stop_into_carry`; L3 RHS (lines 194–216) uses a tail-recursive worker with explicit `(K, s) -> (K', s')` positional threading + trajectory dropped to nothing. The rotation is genuine: (a) state-monad dissolution (`modify` → let-bound `s'`), (b) combinator dissolution (`iterate_while` → `gmres_inner_loop_L3_worker`), (c) trajectory pruning per §3.8 (extras computation eliminated). L4 form is strictly more compact / abstract / equational than L3 form (combinator-application vs. open-coded tail recursion). Body-primitive sequence is identity-in-form across the rotation (correctly noted at line 188 / 228 / 232). Not a renaming; structural compression. Pass.

**variant-axis-coverage** — GMRES carries four documented variant axes (`pc_side ∈ {LEFT, RIGHT, NONE}`, `gs_orthog ∈ {MGS, CGS, CGS2}`, `flexible ∈ {true, false}`, `max_dim` for restart frequency) per `gmres.md:3` and supporting sections. The report addresses these implicitly: the body-primitive sequence (`apply_BA` / `orthogonalize` / `ls_update_column`) absorbs `pc_side` / `gs_orthog` / `flexible` internally and is identity-in-form across the wrapper rotation; restart-frequency lives at the *outer* `restart_cycle` level (not the inner loop) and is correctly scoped out. The report addresses Form B / first-iteration-unrolling explicitly in OQ #3 (line 106). **Warning** because: the report should make the variant-axis pass-through more explicit — the line at the embedded theme file's "What does NOT change" §232 ("The variant-axis profile is unchanged") is the only point where the four axes are aggregated, and it does not enumerate them or cite `gmres.md:3` / `gmres.md:118` (variant-absorption table) as the basis. A reader of the theme alone (not the report) would not know which axes are claimed to pass through unchanged. Recommend enumerating `pc_side` / `gs_orthog` / `flexible` / `max_dim` in the theme's applicability-conditions or "What does NOT change" section, each with a one-line "absorbed at primitive X" pointer.

**cross-reference-integrity** — Markdown links `[iterate-while](../L4/iterate-while.md)` ✓, `[iterate-while-with-prev](../L4/iterate-while-with-prev.md)` ✓, `[krylov-step-typed-wrapper-dissolution](./krylov-step-typed-wrapper-dissolution.md)` ✓, `[derived-view-hoisting](../concepts/derived-view-hoisting.md)` ✓, `[sequential-obstruction](../concepts/sequential-obstruction.md)` ✓. Section anchors `§Signature`, `§Semantics`, `§"Predicate-on-extras anti-pattern"`, `§Algebraic laws Law 1` all exist in `iterate-while.md` ✓. **Warning** for the line-number references to `krylov-step-typed-wrapper-dissolution.md:156-167` (cited at report lines 91, 167-of-embedded, 222, 294): the parallel cycle-008 lifter dispatch `2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close` is REPLACING the §"What the L3 form for iterate_while looks like" subsection currently at lines 156–167 with an expanded §3.8 preamble + two-form sketch. After the lifter applies, the line numbers will shift and "lines 156-167" will no longer point at the intended content. The section-anchor portion of the cross-refs (`§"What the L3 form for iterate_while looks like"`) is stable across the lifter edit, but the numeric ranges are not. The user prompt explicitly flagged this concern. Recommend dropping the numeric line ranges in favor of section anchors only when referencing files being edited in the same cycle.

**edge-label-fidelity** — The theme is filed under `book/src/L4-L3/` (the L4→L3 lowering Part); the LHS is labeled "L4 form" (lines 137, 191); the RHS is labeled "L3 form" (lines 190, 218); the abstraction-direction note at line 265 explicitly states "The rotation direction is L4 → L3" with L4 = higher-abstraction. Prose discusses exactly the L4→L3 rotation throughout, no L3→L2 or L2→L1 conflation. The justification-kind section at line 259 correctly labels `structural` (dominant) with `reduction-chain` + `empirical-match` secondaries — all appropriate for an L4>L3 hop. Pass.

**plan-kind-consistency** — Frontmatter declares `scope: L4>L3 theme sketch — gmres-inner-loop-iterate-while-migration (rough-in)`; status text repeats `rough-in` at line 25, 308, and 309. Content shape matches: speculative LHS pending upstream gmres.md self-rotation; L4 helper `check_stop_into_carry` flagged as rough-in (line 53, 270); dep-map registration uses plain-text per cycle-006 friction-ledger `rough-in-rows-must-be-plain-text-when-anchor-missing` (line 275, 38). The theme-list row in `book/src/L4-L3/index.md` (proposed-change 2) uses plain-text slug form with the *(rough-in; this dispatch creates the anchor file...)* annotation. Three OQ routes recorded at lines 102, 104, 106. Plan-kind matches content shape. Pass. Side note: the `check_stop_into_carry` helper is described at length and a dep-map row format is shown (line 273) but a `proposed-changes` block to actually APPEND that row to `book/src/L4/index.md` is NOT in the report — this is consistent with the stated promotion criterion (deferred to second-slice-finding-necessity), but the user's prompt mentions "APPEND dep-map row" which I interpret as the L4-L3 theme-list row (proposed-change 2), not the L4 dep-map row for the helper. No defect, but flagging the interpretation in case the integrator expects the helper to be dep-map-registered.

**skill-uptake-survey** — Two skills are clearly applicable to this report shape: `verify-citation-range` (the C++ citation spread is substantial, with multiple cross-cited line ranges) and `classify-variant-axis` (GMRES has four documented variant axes that need pass-through reasoning). The report references neither skill's invocation in its content or process notes. **Warning** as telemetry signal — not blocking. The pattern of skill non-invocation on multi-citation rough-in reports may warrant attention by meta-phase if it recurs.

### Issues found

1. **Stale line numbers under parallel lifter edit (cross-reference-integrity)** — *severity: medium.* Report lines 91, 222, 294 and the embedded theme file's reference (line 167-of-embedded "krylov-step-typed-wrapper-dissolution.md:156-167") cite a numeric range for §"What the L3 form for iterate_while looks like" that the parallel cycle-008 lifter dispatch is replacing/expanding. The section anchor itself survives; the line numbers will not. Recommend replacing numeric ranges with section-anchor-only references for files being edited in the same cycle (specifically: `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`).

2. **L0 citation ranges overshoot the inner loop boundary (citation-validity)** — *severity: low.* Range `iterative.cpp:613-650` includes a blank line at 613 (loop opens at 614); range `:614-705` extends beyond the inner loop's end-brace at 650 into the back-substitution and restart-handling code. Neither is wrong (the wider ranges are still informative context) but they are not minimum-bounding. The user prompt's "`iterative.cpp:614-705`" framing matches the cycle-007 audit's framing, so this is consistent with prior conventions; still worth noting.

3. **Variant-axis pass-through claim is too aggregated in the theme body (variant-axis-coverage)** — *severity: low.* Only the embedded theme file's §"What does NOT change" subsection mentions variant-axis preservation, and it does so in one line without enumerating the four axes (`pc_side`, `gs_orthog`, `flexible`, `max_dim`) or citing `gmres.md:3` / `gmres.md:118` as the variant-absorption basis. A reader of the theme alone (not the parent report) cannot verify which axes the theme claims pass through unchanged. Recommend enumerating the four axes with one-line absorbed-at-primitive pointers in either the applicability-conditions or "What does NOT change" section.

4. **No skill invocations recorded (skill-uptake-survey)** — *severity: low / telemetry.* `verify-citation-range` and `classify-variant-axis` are both applicable to this report shape; neither is referenced. Not blocking; flagged for meta-phase trend analysis.

5. **Sub-claim "break-on-converged at line 644" inherited from `iterate-while.md:232`** — *severity: very low / not introduced by this report.* The embedded quote at report line 86 reproduces iterate-while.md's slightly imprecise wording: line 644 is the `converged = (beta < eps)` assignment; the break-on-stop check is at line 645. The report itself uses the correct line numbers elsewhere (e.g., line 79 cites 645-649 for the break). Quoting the upstream file faithfully is correct behavior; flagging only so the upstream `iterate-while.md` can be tightened on a future pass.

6. **Speculative L4 helper `check_stop_into_carry` is named and signature-sketched but NOT registered in the L4 dep-map (plan-kind-consistency / proposed-changes completeness)** — *severity: low / by-design.* The report describes the L4 dep-map row format (line 273) but does not include a `proposed-changes` block to APPEND it to `book/src/L4/index.md`. The omission is internally justified by the stated promotion criterion at line 68 (promote only when a second slice finds the witness-hoist necessary). The user-prompt phrase "APPEND dep-map row (plain-text per rough-in discipline)" appears to refer to the L4-L3 theme-list row (proposed-change 2), not the L4 dep-map row for the helper. Flagging the interpretation in case the integrator expected the helper to be dep-map-registered as a rough-in row.

### Skill candidate observation

No new skill candidate from this critique; the patterns (citation-line-number-fragility-under-parallel-edits, variant-axis-pass-through-claim-needs-enumeration) are already implicitly covered by `verify-citation-range` and `classify-variant-axis` respectively. The recurrence may warrant meta-phase attention as a skill-uptake-friction signal rather than a new skill.

## Repair

### Fixes attempted

1. **Finding**: Stale line numbers `156-167` for `krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for `iterate_while` looks like" will go stale when the parallel cycle-008 lifter dispatch (`2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close`) replaces/expands that subsection. **MOST ACTIONABLE per user prompt.**
   - **Decision**: repaired
   - **Action**: Replaced all three numeric line-range references (CYCLE.md report-prose §Supporting evidence "L4>L3 source" bullet; embedded theme file §"L3 form (RHS)" structural-difference 2; embedded theme file §Verified-against "L4>L3 precedent" bullet) with section-anchor-only references to §"What the L3 form for `iterate_while` looks like". Added one-line note at the two prose-bullet sites explaining the section-anchor-only choice (stable across parallel-cycle lifter edit). Verified via grep that no `156-167` references remain in CYCLE.md. The section anchor itself exists in the target file (verified via `grep ^# book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — line 156, heading text unchanged).

2. **Finding**: L0 citation ranges overshoot the inner-loop boundary. `iterative.cpp:613-650` includes blank-line 613 (loop opens at 614); YAML frontmatter `iterative.cpp:614-705` extends past the inner-loop end-brace at 650 into back-substitution / restart-handling / summary-print code.
   - **Decision**: repaired
   - **Action**: (a) Replaced all `iterative.cpp:613-650` occurrences (three sites in CYCLE.md §Supporting evidence and embedded theme file §Verified-against) with `iterative.cpp:614-650` — the actual minimum-bounding loop body verified against `reference/palace/palace/linalg/iterative.cpp:614-650` (loop opens at 614 with `int j = 0;`, loop closing-brace at 650). (b) Tightened YAML frontmatter `iterative.cpp:614-705` to `iterative.cpp:614-650` and added parenthetical noting that the outer Mult continues 651-705 with back-substitution + restart-handling + summary print, out-of-scope for this theme. The inner-Arnoldi-loop description in the frontmatter `inputs:` entry now matches the cited range exactly.

3. **Finding**: Variant-axis pass-through claim is too aggregated in the theme body. Only one line ("The variant-axis profile is unchanged") in §"What does NOT change", without enumerating the four GMRES axes (`pc_side`, `gs_orthog`, `flexible`, `max_dim`) or citing the `gmres.md:3` / `gmres.md:118-124` variant-absorption basis.
   - **Decision**: repaired
   - **Action**: Enumerated all four variant axes in the embedded theme file's §"What does NOT change in the rotation" section. Each axis gets a one-line entry naming its value-domain, citing the `gmres.md` line that documents its single-dispatch-site, and stating which body-primitive absorbs it (so the wrapper rotation is identity-on-that-axis). Closed with explicit citation of `gmres.md:118-124` as the variant-absorption basis. Reader of the theme alone (not the parent report) can now verify the pass-through claim without external context. Axes enumerated per the prose at `gmres.md:3` and the dispatch-site table at `gmres.md:118-124`.

4. **Finding**: No skill invocations recorded (`verify-citation-range`, `classify-variant-axis`). Telemetry signal; not blocking.
   - **Decision**: unrepairable
   - **Rationale**: Skill-invocation telemetry is a property of the original dispatch session; the repairer cannot retroactively cause the producer to have invoked skills. This is correctly flagged for meta-phase trend analysis (per the critic's own framing). The substantive content the skills would have verified (citation ranges, variant-axis enumeration) has now been verified during repair, but the *invocation record* itself is not back-fillable.

5. **Finding**: Sub-claim "break-on-converged at line 644" inherited from `iterate-while.md:232`. Very-low severity; not introduced by this report; flagged for upstream tightening on a future pass.
   - **Decision**: not-needed
   - **Rationale**: Critic explicitly noted this is inherited from upstream `iterate-while.md` (where line 644 is the `converged = (beta < eps)` assignment and line 645 is the break check), not introduced by this report. The report itself uses the correct line numbers elsewhere (645-649 for the break). Mutating `book/src/L4/iterate-while.md` is out of repairer scope (repairer cannot mutate book/). Defer to a future harvester/lifter pass on iterate-while.md.

6. **Finding**: Speculative L4 helper `check_stop_into_carry` is named but NOT registered in the L4 dep-map. By-design omission per the report's stated promotion criterion.
   - **Decision**: not-needed
   - **Rationale**: Critic flagged this as "by-design" (severity: low) and explicitly noted the omission is internally justified by the report's stated promotion criterion (promote only when a second slice finds the witness-hoist necessary). The user prompt did not list this finding in the four to repair. No action needed.

### Unrepairable findings

- **skill-uptake-survey**: telemetry-only finding; not back-fillable by the repairer. Surfaces for meta-phase trend analysis (recurrence across cycle-007/008 may signal a skill-invocation-friction pattern; meta-phase decides whether to address via skill-prompt-tightening or by adjusting agent-role specs).

## Suggested resolution

`ready` — all three blocking warnings (cross-reference-integrity, variant-axis-coverage, citation-validity) are repaired by mechanical fixes that did not author substantive content:

- The cross-reference fix is pure annotation rewrite (numeric line range → existing section anchor) on already-cited content.
- The variant-axis fix enumerates axes already documented at `gmres.md:3` and `gmres.md:118-124`; no new claims, no new analysis — just spelling out the four axes the prior single-line claim covered.
- The citation-validity fix tightens ranges to minimum-bounding extents verified directly against the source file (`reference/palace/palace/linalg/iterative.cpp:614-650`).

The remaining `skill-uptake-survey: unrepairable` is telemetry and non-blocking per the critic's own framing. The two `not-needed` findings (inherited iterate-while.md imprecision; missing L4 dep-map row for the speculative helper) are out-of-scope for repair (the former requires book/ mutation; the latter is correctly deferred per the report's stated promotion criterion).

**Integrator note**: when applying the proposed-changes block, the `[gmres-inner-loop-iterate-while-migration]` row in `book/src/L4-L3/index.md` (proposed-change 2) currently references `krylov-step-typed-wrapper-dissolution` by slug-form (plain text, per the rough-in-rows-must-be-plain-text-when-anchor-missing discipline). The actual theme-file content (embedded in CYCLE.md §"Theme file content") now uses section-anchor references only when citing the parallel-edited target file; integrator should preserve this convention if it post-processes the markdown links.
