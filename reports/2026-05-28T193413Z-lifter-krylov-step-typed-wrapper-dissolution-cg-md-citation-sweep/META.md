---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T19:42:16Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T20:05:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of lifter cg.md citation-sweep on krylov-step-typed-wrapper-dissolution

## Critique

### Checks run

**citation-validity — pass.** The dangling-pointer premise is verified: `book/src/spec/slices/cg.md` is the cycle-009 reduced 165-line stub (header line 1 "(reduced)"; supersedessor list lines 5-14), so every `cg.md` pointer at lines 341-362 / 347-350 / 351-362 is out-of-range and dangles. Both re-anchor TARGETS carry the referenced content (verified below). `arnoldi_step.md` is 302 lines; its `:178-213` / `:185-188` / `:194-213` co-anchors are in-range and correctly left untouched. All 8 `[old]` strings match the theme file verbatim at the cited lines (98/109/126/200/204/210/231/233).

**surface-or-evidence — pass.** Pure retroactive citation re-anchor (allowed): no claim, no LHS/RHS shape, no applicability condition changes; status stays `firm`. The historical `cg.md` ranges are retained as parenthetical provenance, so the audit trail survives the reduction. No rotation_claim is asserted without surface — this is evidence-pointer maintenance, the explicitly-allowed backfill case.

**rotation-quality — pass (not the report's job to assert).** The report asserts no new rotation; it re-points citations on an existing firm rotation. The underlying L4>L3 wrapper-dissolution rotation is firm and unchanged. Inapplicable to a re-anchor sweep.

**variant-axis-coverage — pass.** No variant axes are in play for a citation re-anchor; the six-axis profile of the theme is untouched. Not applicable to this report-kind.

**cross-reference-integrity — pass.** All four relative-link targets resolve from `book/src/L4-L3/`: `../L3/krylov-step.md`, `../L3-L2/krylov-step-body-identity.md`, `../concepts/sequential-obstruction.md`, `../L2/krylov-step.md`. **Target-content verified (the key risk per the dispatch brief)**: (a) `L3-L2/krylov-step-body-identity.md:125` (§Verified-against, opens line 121) carries the verbatim Claim-2 quote *"The L2→L3 rotation on the step body is therefore the identity in form..."* preserving `cg.md:341-362` — correct home for the body-identity family. (b) `L3/krylov-step.md` §"Algebraic laws" non-law #7 (line 129, "Outer-loop lift to a single tensor-field op") plus the §"Iteration-rotation marker" line 108 narrate the outer-loop `sequential-obstruction` in L3 vocabulary — correct home for the outer-loop family. Neither re-anchor points at a wrong target.

**edge-label-fidelity — pass.** The theme is L4>L3; the re-anchors touch only narrative citation pointers and add no reverse-direction (L3→L4 lift) prose. High→low direction preserved (Discipline note 5). The two firm homes are correctly at lower edges (L3, L3>L2) consistent with where lifted evidence lives.

**plan-kind-consistency — pass.** Declared a `lifter` re-anchor sweep; content is exactly 8 citation-pointer swaps applying the cycle-013 convention verbatim. No authoring, no structure change. Shape matches kind.

**skill-uptake-survey — warning (non-blocking telemetry).** The report's shape (verifying citation ranges resolve / dangle) is squarely the domain of the `verify-citation-range` skill — extended cycle-012 meta-phase with an "Audit-report / inherited-citation sub-case" section that this sweep exercises directly (re-anchoring inherited audit citations to firm homes). The report does not reference invoking it. Pure presence check; surfaces telemetry only.

### Issues found

1. **(minor, content-touch beyond pure re-anchor) Re-anchors 6/7/8 silently re-attribute the audit.** `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Audit ... Evidence reviewed" item 1 (line 210), §Verified-against L3-evidence rows (lines 231, 233): the `[new]` strings change "Re-read for **this** audit" → "Re-read for the **cycle-006** audit" (and Re-anchor 6 changes "re-read for this audit" → "re-read for the cycle-006 audit"). This is a factual sharpening (the audit was authored cycle-006), but it is a prose edit, not a citation-pointer swap — slightly exceeding the "pure citation re-anchor, no claim change" framing in Discipline note 1. Severity: low. Defensible as accuracy, but the report should have flagged it as an incidental attribution-fix (it flagged the analogous link-hygiene upgrade in Discipline note 6 but not this one).

2. **(observation, correctly deferred) Sibling dangling pointers in `L3/krylov-step.md` are real.** Verified: with `cg.md` at 165 lines, `L3/krylov-step.md` lines 108/129 (`cg.md:341-349`), 188 (`cg.md:341-362`), 196 (`:103-115`/`:172-188`/`:393-425`), 204 (`:208-220`/`:430-446`) all dangle. The report's §"Open questions" flags this as out-of-scope (different file: an L3 operator entry, not this L4>L3 theme) and recommends a sibling cycle-015 lifter. **Assessment: the deferral is correct, not a should-have-been-in-scope miss.** Dispatch scope is the single theme file; touching `L3/krylov-step.md` would be an unscoped `book/` mutation in the dispatch phase (forbidden). However, note the mild reflexivity tension the report itself acknowledges (line 107 parenthetical): Re-anchors 1/4/8 designate `L3/krylov-step.md` §Algebraic-laws as the *firm narrative home* for the outer-loop family while that target's own `cg.md` pointers dangle. The narrative home is valid (the obstruction claim lives there in L3 vocabulary regardless of the target's own citation hygiene); the sibling sweep should follow to fully close the loop. Recommend the new OQ the report proposes (`l3-krylov-step-cg-md-citation-sweep`) be filed rather than holding the current OQ open. Severity: informational.

3. **(observation) `skill-uptake-survey` warning, item above.** No `verify-citation-range` invocation referenced despite the report being a textbook instance of its inherited-citation sub-case. Non-blocking.

### Per-check one-liner

citation-validity pass (premise + both targets + all 8 `[old]` verified); surface-or-evidence pass (allowed retroactive backfill); rotation-quality / variant-axis-coverage pass (n/a to re-anchor); cross-reference-integrity pass (4 links resolve, both firm homes carry the content; family-split faithful to Claim 1 vs Claim 2); edge-label-fidelity pass (high→low preserved); plan-kind-consistency pass; skill-uptake-survey warning (`verify-citation-range` not referenced).

## Repair

### Fixes attempted

- **Finding (Issue 1, low)**: Re-anchors 6/7/8 silently re-attribute "this audit" → "the cycle-006 audit" — a defensible accuracy sharpening undisclosed beyond the "pure citation re-anchor" framing.
  - **Decision**: repaired (disclosure-note path; re-attribution kept).
  - **Action**: Added a Discipline note to `CYCLE.md` §"Discipline notes" (after the `sequential-obstruction.md`-link note) disclosing the "this audit" → "the cycle-006 audit" change as an intentional incidental attribution-fix. Verified "the cycle-006 audit" is FACTUALLY CORRECT before keeping it: the theme's own §"Audit of cycle-002 identity-in-form claim" section is the cycle-006 wave audit — confirmed by `krylov-step-typed-wrapper-dissolution.md:218` ("the cycle-006 verdict"), the §"Verified-against" provenance comment at line 247 ("the narrative §'Verified-against' list above carries the **cycle-006** evidence registry"), and lines 253/257/293 all attributing the audit content to cycle-006. Because the sharpening is factually right and the original author's "this audit" was only a stale local self-reference (not wrong-in-context), the dispatch-brief's "keep it + disclose" branch applies. No claim/structure/status change.

- **Finding (Issue 2, skill telemetry)**: `skill-uptake-survey` warning — `verify-citation-range` not referenced despite the report being a textbook instance of its inherited-citation sub-case.
  - **Decision**: not-needed (acknowledge only).
  - **Rationale**: Pure non-blocking telemetry. The skill exists and was exercised in spirit (the sweep is exactly the cycle-012-extended "Audit-report / inherited-citation sub-case"); the report simply did not name-reference it. No mechanical fix; not a content defect. Acknowledged for the skill-uptake telemetry channel.

- **Finding (Issue 2/observation, correctly-deferred)**: Sibling dangling `cg.md` pointers in `L3/krylov-step.md` (lines 108/129/188/196/202/204) are real but out-of-scope for this single-theme dispatch.
  - **Decision**: repaired (promoted the deferred OQ).
  - **Action**: Promoted the report's §"Open questions / caveats" item 1 to `scaffolding/open-questions.md` as a new `open` OQ `l3-krylov-step-cg-md-citation-sweep` (opened_at cycle-014, recommending a cycle-015 sibling lifter applying the cycle-013/014 lifted-evidence annotation convention). The critic confirmed the deferral is correct (touching `L3/krylov-step.md` would be an unscoped dispatch-phase `book/` mutation), so the residual is routed via the ledger rather than absorbed into this dispatch. The theme-side OQ `krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` is closed in full by this report (integrator may mark it `answered`); the new OQ is the explicitly-separate residual rather than holding the original open.

### Unrepairable findings

None. All findings are either pass (critic), repaired, or non-blocking telemetry acknowledged.

## Suggested resolution

`ready` — integrator notes:
- The 8 re-anchors apply cleanly; all `[old]` strings verified verbatim by the critic and the re-attribution sharpening (Re-anchors 6/7/8) is now disclosed in `CYCLE.md` Discipline notes.
- On integration, mark theme-side OQ `krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` `answered` (answer-link this CYCLE.md), contingent on the 8 re-anchors landing.
- New residual OQ `l3-krylov-step-cg-md-citation-sweep` is already filed (append-only) for a cycle-015 sibling lifter on `L3/krylov-step.md`'s own dangling `cg.md` pointers — do NOT hold the theme-side OQ open for it.
- The §3.8/`iterate-while` Law-1 narrative and `firm` status are unchanged; this is a pure citation-hygiene sweep.
