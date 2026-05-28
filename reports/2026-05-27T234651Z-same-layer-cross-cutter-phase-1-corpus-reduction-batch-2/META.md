---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T235800Z
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
repaired_at: 2026-05-28T000400Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of "Phase 1 corpus reduction audit — batch 2 (orthog / chebyshev / polynomial_recurrence_step)"

## Critique

### Checks run

**citation-validity (warning)** — Spot-checked all load-bearing citations. Verifiable pointers: `concepts/negative-result-slice.md:46` cites `polynomial_recurrence_step` as the canonical example (verified); `L3-L2/krylov-step-body-identity.md:127` cites `chebyshev.md:354-362` (verified); `L2/krylov-step.md:140, :142` cite chebyshev.md and polynomial_recurrence_step.md (verified); `L4/krylov-step.md:141` lists polynomial-kind as variant axis 3 (verified, but the report says "Variant axes #3" which conflates the heading number with the actual position); `scaffolding/open-questions.md:1804` is the prose line of the L1/orthogonalize OQ (the slug yaml block starts at 1796 — acceptable but the report references should clarify whether it points at the block header or the prose); the slice structure enumerations match `grep -n` output. Minor issues found: (a) the L1-L0 sub-pattern C citation in the report is written as `iterative.cpp:307-326` (line 94, line 261 of CYCLE.md) but the artifact uses `:307-325` (off-by-one); (b) the report claims `concepts/orthogonalization.md`'s "5-line L1 contract section" (line 84) but lines 13-15 of that file contain only 3 lines of contract content (line 13 heading + lines 14-15 prose, no body listing); (c) the report claims `concepts/plane-rotation-stream.md` §"Variants the stream is invariant to" is at "lines 26-33" (line 93) but the heading is at line 25 with content at 27-33. None of these errors are load-bearing for the audit verdicts.

**surface-or-evidence (pass)** — This is an audit-shaped report (per the "Observation kind" framing: variant-axis-coverage-gap-audit). It proposes targeted partial-reductions to existing slice files (legitimate surface mutation, supported by detailed supersession maps for each slice) and surfaces routing/lift OQs (retroactive evidence backfill for the methodology invariant "Phase 1 corpus reduces as material is lifted"). The proposed_changes blocks include concrete textual replacements with rationale. The verdict per slice is grounded in actual evidence-of-supersession (cross-referenced firm entries verified) and evidence-of-non-supersession (unique-material claims spot-checked against the slice contents).

**rotation-quality (pass)** — Not directly applicable to this audit-shape report (no new operator/theme rotations proposed). The audit's per-slice supersession map functions as the inverse direction (identifying material already absorbed into firm entries) which is appropriate for corpus-reduction work. The audit correctly distinguishes the negative-result slice's structural role (the catalog IS the result, not a precursor) from precursor-slice reductions, which is a legitimate observation about the slice corpus's heterogeneous shape.

**variant-axis-coverage (pass)** — The audit explicitly enumerates each slice's structure (via `grep -n`) and tracks the supersession status section-by-section. The orthog.md audit identifies that the file is structurally two slices (Gram-Schmidt + plane-rotation-stream) and correctly defers the plane-rotation-stream sub-slice to batch-3 for joint audit with the sibling `plane_rotation_stream.md`. The chebyshev.md audit identifies both an L1 and an L2 lift target (chebyshev-smoother and chebyshev-iteration) as separate axes. The polynomial_recurrence_step.md audit identifies the cross-family negative-result vs. within-family partial-positive axes correctly. No hidden branches detected.

**cross-reference-integrity (pass)** — All cited firm entries exist: `book/src/L2/krylov-step.md`, `book/src/L3/krylov-step.md`, `book/src/L4/krylov-step.md`, `book/src/L3-L2/krylov-step-body-identity.md`, `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`, `book/src/L1/ksp_solve.md`, `book/src/L1-L0/ksp-solve-mutation-rotation.md`. All concept pages cited exist: `orthogonalization.md`, `plane-rotation-stream.md`, `givens.md`, `givens_generate.md`, `givens_apply.md`, `sequential-obstruction.md`, `chebyshev-iteration.md`, `negative-result-slice.md`, `derived-view-hoisting.md`, `state-stratification.md`, `solve-monad.md`, `constructed-operators.md`, `variant-absorption.md`, `first-iteration-unrolling.md`. OQ slug `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog` exists at `scaffolding/open-questions.md:1796`. Priority #19 (`phase-1-corpus-reduction-audit`) exists at `scaffolding/priorities.md:44`. Cycle-010 precedent report exists at the cited path.

**edge-label-fidelity (pass)** — Not applicable to this report (no lowering edge labels proposed). The audit discusses cross-references between slices and firm L_n/L_{n+1}>L_n entries; all direction-of-reference statements (e.g., "slice's L3 section lifted into concepts/sequential-obstruction.md") are consistent with the actual artifact structure.

**plan-kind-consistency (pass)** — The report is correctly typed as an `audit` observation: it proposes reductions (which the integrator would apply mechanically) and surfaces residual gaps as OQs (which separate harvester/abstractor dispatches will address). Per-slice verdicts are explicitly labeled (partial-reduction / blocked-minimal-reduction); proposed_changes are mechanical text replacements, not new content authoring. The classification matches the dispatch shape (same-layer-cross-cutter doing a corpus audit per priority #19).

**skill-uptake-survey (warning)** — A `phase-1-slice-reduction-audit` skill candidate is recorded at `scaffolding/skill-candidates.md:114-115` (per the cycle-010 audit's integration_notes); this report explicitly follows the cycle-010 template but does NOT invoke or reference any formal skill, nor does it propose advancing the candidate to a real SKILL.md. Given that this is the second execution of the same audit template (the first to declare the template machine-replayable), advancing the skill candidate from "proposed" to firm should be considered — at minimum, this dispatch is a use-case data point for the candidate. The report does cite the friction-signal mitigation (`grep -n` H2-enumeration before line-range arithmetic) which is partial evidence of an implicit procedure being followed.

### Issues found

1. **Off-by-one citation: `iterative.cpp:307-326` vs `:307-325`.** The report (CYCLE.md lines 94 and 261) cites `iterative.cpp:307-326` for `OrthogonalizeIteration` in Sub-pattern C of `L1-L0/ksp-solve-mutation-rotation.md`. The actual citation in `L1-L0/ksp-solve-mutation-rotation.md:373` uses `:307-325`. **Location**: CYCLE.md §"Slice 1" line 94, §"Proposed change 1" line 261. **Severity**: minor (off-by-one; not load-bearing for the audit verdict).

2. **Summary inconsistency: "Two new OQs" vs. five-six in body.** The Summary states "Two new OQs are surfaced for material that needs lifting before further reduction is safe" (CYCLE.md line 45) and enumerates two items (L1/orthogonalize continuation + firm Chebyshev row). However, the Recommendation section (lines 236-241) enumerates 5 follow-up items including 4 new OQs, and the §"Open questions / caveats" section (lines 357-379) enumerates 6 new OQs to add. **Location**: CYCLE.md line 45 vs. lines 236-241 and 357-379. **Severity**: minor (presentation inconsistency; the underlying observations are individually well-supported, but the summary undercounts the audit's actual output).

3. **`concepts/orthogonalization.md` "5-line L1 contract" claim is imprecise.** The report (CYCLE.md line 84) describes `concepts/orthogonalization.md`'s "5-line L1 contract section" as more granular than needed. The actual §"L1 contract" at lines 13-15 of that file is 3 lines (heading + 2-line prose; no signature block). **Location**: CYCLE.md §"Slice 1 — Supersession map" line 84. **Severity**: minor (the comparative claim that the slice's L1 contract is more granular than the concept page is still valid; only the count is off).

4. **`concepts/plane-rotation-stream.md` "Variants" line range off-by-one.** The report cites "lines 26-33" (CYCLE.md line 93) for §"Variants the stream is invariant to" of the concept page; the actual heading is at line 25 with content lines 27-33. **Location**: CYCLE.md §"Slice 1 — Supersession map" line 93. **Severity**: minor.

5. **"Variant axes #3" label conflates ordinal with section number.** The report uses "Variant axes #3" (CYCLE.md lines 137, 144, 284, 367) when referencing `L4/krylov-step.md`'s polynomial-kind. The actual structure is `## Variant axes` (one section, line 135 of that file) containing a 6-item enumerated list; polynomial-kind is item 3 (line 141), not "axis #3" as a heading. This is style/citation-form, not factual error. **Location**: multiple in CYCLE.md. **Severity**: very minor.

6. **First L1 entry framing: "supersedes" overstates the relation.** The report (CYCLE.md line 95) claims the first L1 entry (lines 364-398 of `orthog.md`) supersedes the second L1 entry (lines 405-464) "since the latter is a refinement of the former". Re-reading both entries: both are about the plane-rotation stream, the first has slightly different content (includes a `back_solve` procedure at line 395 of `orthog.md` that the second does not), and the scope note at line 407 frames the second as "structurally distinct from the **block Gram-Schmidt orthogonalization** dissected in the earlier sections". The relation between the two L1 entries is "near-duplicate-with-divergent-content", not a strict supersession. The report's own §"Recommended action" item ("the two L1 entries should be merged") is the more accurate framing. **Location**: CYCLE.md §"Slice 1 — Supersession map" line 95-96. **Severity**: framing inconsistency; the recommendation (merge) is correct but the supersession label in the map is imprecise.

7. **L1-L0/ksp-solve-mutation-rotation firmness label.** The report's inputs list (CYCLE.md line 11) labels `L1-L0/ksp-solve-mutation-rotation.md` as "rough-in; cycle-008". The L1-L0 index status at line 21 of `book/src/L1-L0/index.md` records it as "rough-in *(firmed cycle-008)*" — i.e., post-cycle-008 it is effectively firm. The report's "rough-in" label could be read as ignoring the cycle-008 firm-up. **Location**: CYCLE.md inputs list line 11. **Severity**: minor (the audit logic uses the entry as a firm reference correctly elsewhere; only the inputs label is loose).

8. **Skill-candidate uptake not explicitly progressed.** This is the second execution of the cycle-010 audit template, and the cycle-010 audit explicitly declared the template "machine-replayable" and filed a `phase-1-slice-reduction-audit` skill candidate at `scaffolding/skill-candidates.md:114-115`. This report follows the template directly and applies the cycle-010 friction-signal mitigation, but does NOT propose advancing the skill candidate to firm or invoke a formal skill. With recurrence-2 of the same template, the skill candidate has stronger ground for promotion than at recurrence-1. **Location**: report-level (no specific line). **Severity**: telemetric (per skill-uptake-survey check spec, this is surface-only — not a blocker).

9. **OQ deduplication: "L1/orthogonalize continuation" is partial duplication.** The report enumerates `L1/orthogonalize` promotion both in §"Open questions / caveats" item 2 (as an update to the existing OQ at `scaffolding/open-questions.md:1804`) and references it from the Summary as a "new OQ" (CYCLE.md line 46). The actual existing OQ is open and should be amended (not re-filed). The report's intent is to amend, but the framing in the Summary as "new" is potentially confusing. **Location**: CYCLE.md line 46. **Severity**: minor (the §"Open questions / caveats" section correctly frames as "OQ update recommendation").

10. **Proposed_changes block syntax may not match integrator expectations.** The proposed_changes blocks use a custom `edit:book/src/spec/slices/<slice>.md` syntax with `[Replace lines X-Y with...]` bracketed prose descriptions of the edit rather than literal before/after diff blocks. Per the cycle-010 precedent, the integrator does accept this shape, but the bracketed prose ("[Replace lines 7-109...]") is interpretation-required rather than mechanical. This is a structural property of the audit-template's proposed_changes block shape established in cycle-010, not an error introduced here. **Location**: CYCLE.md §"Proposed changes" lines 249-332. **Severity**: structural (carried from cycle-010 template; would benefit from skill-candidate-promotion to standardize the block format).

## Repair

### Fixes attempted

- **Finding 1 (off-by-one `iterative.cpp:307-326` vs `:307-325`)**
  - **Decision**: repaired
  - **Action**: CYCLE.md line 94 (Slice 1 §"Sub-pattern C" reference) and line 261 (Proposed change 1 stub-header text) — `iterative.cpp:307-326` → `iterative.cpp:307-325` (matches `book/src/L1-L0/ksp-solve-mutation-rotation.md:373`).

- **Finding 2 (Summary "Two new OQs" vs five-six in body)**
  - **Decision**: repaired
  - **Action**: CYCLE.md §Summary lines 45-47 — rewrote the OQ-count framing to "Six OQ actions are surfaced (1 amendment to an existing OQ + 5 new OQs) ... Two headline blockers: ..." with explicit pointer to §"Open questions / caveats" items 1, 4, 5, 6 for the remaining four. Distinguishes the amendment (item 2 below) from the new-OQ filings, addressing Finding 9 in the same edit.

- **Finding 3 (`concepts/orthogonalization.md` "5-line L1 contract" — actually 3 lines)**
  - **Decision**: repaired
  - **Action**: CYCLE.md §"Slice 1 — Supersession map" line 84 — `"`concepts/orthogonalization.md`'s 5-line "L1 contract" section"` → `"`concepts/orthogonalization.md`'s "L1 contract" section (3 lines: heading at :13 + 2-line prose at :14-15; no signature block in the concept page)"`. Preserves the comparative claim (slice contract is more granular) while correcting the line count.

- **Finding 4 (`concepts/plane-rotation-stream.md` "Variants" line range off-by-one)**
  - **Decision**: repaired
  - **Action**: CYCLE.md §"Slice 1 — Supersession map" line 93 — `"(lines 26-33 of that file)"` → `"(heading at line 25, content at lines 27-33 of that file)"`. Disambiguates heading vs content line ranges.

- **Finding 5 ("Variant axes #3" ordinal conflation)**
  - **Decision**: repaired
  - **Action**: replaced all 4 occurrences of `"Variant axes #3"` with the disambiguated form `"§Variant axes list-item 3"` (with the specific line number where useful):
    - CYCLE.md line 137 (Slice 2 §intro supersession-map row) — `"variant axis 3, polynomial-kind {4th, 1st}"` → `"the single ## Variant axes section at line 135 with a 6-item list; the polynomial-kind axis is list-item 3 at line 141 — {4th, 1st}"`.
    - CYCLE.md line 172 (Slice 2 header-note text) — `"Variant axes #3 (polynomial-kind)"` → `"§Variant axes list-item 3 (polynomial-kind at line 141)"`.
    - CYCLE.md line 284 (Proposed change 2 header-note quote) — same form.
    - CYCLE.md line 340 (Supporting evidence row for `L4/krylov-step.md`) — same form.
    - CYCLE.md line 367 (OQ-to-add proposed text for Chebyshev row promotion) — same form.

- **Finding 6 (First-L1-supersedes-second-L1 framing imprecise)**
  - **Decision**: repaired
  - **Action**: CYCLE.md §"Slice 1 — Supersession map" line 95 — `"(lines 364-398, supersedes lines 405-464 since the latter is a refinement of the former)"` → `"(lines 364-398, near-duplicate of lines 405-464 — the two L1 entries diverge slightly in content; see the next bullet for the precise relation)"`. Aligns with the next bullet's already-correct "near-duplicate" framing and the Recommended-action's "merge" verdict.

- **Finding 7 (L1-L0/ksp-solve-mutation-rotation "rough-in" label loose)**
  - **Decision**: repaired
  - **Action**: CYCLE.md inputs frontmatter line 11 — `"(rough-in; cycle-008)"` → `"(firmed cycle-008; status: rough-in *(firmed cycle-008)* per L1-L0/index.md:21)"`. Records the L1-L0 index entry's exact firmness phrasing.

- **Finding 8 (Skill-candidate `phase-1-slice-reduction-audit` recurrence-2 uptake)**
  - **Decision**: repaired
  - **Action**: appended a "Cycle-011 uptake-note" paragraph to `scaffolding/skill-candidates.md` immediately after the existing `## Open candidates (cycle-010 additions)` block for slug `phase-1-slice-reduction-audit`. The note records: (a) cycle-011 batch-2 is the second instance of the cycle-010 template execution, clearing the "≥2 cycles" promotion bar; (b) the cycle-011 critic-flagged proposed_changes-block bracketed-prose syntax (Finding 10) is a likely cycle-012 meta-phase template-improvement candidate that may extend the skill's scope; (c) meta-phase batch-2 (after cycle-012 integrator-finalize) should promote the candidate to firm `skills/phase-1-slice-reduction-audit/SKILL.md`. This is an append to an any-agent-appendable channel, in scope for repairer authority.

- **Finding 9 (OQ deduplication: "L1/orthogonalize continuation" framed as "new" in Summary)**
  - **Decision**: repaired
  - **Action**: addressed in the same edit as Finding 2 (CYCLE.md §Summary lines 45-47): the rewrite explicitly labels item 1 as `"**L1/orthogonalize firm promotion** (amendment of cycle-010 OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog`; ...). See §"Open questions / caveats" item 2 for the amendment recommendation."`. The "amendment vs new" distinction is now load-bearing in the Summary framing.

- **Finding 10 (Proposed_changes block bracketed-prose syntax — cycle-010 template friction)**
  - **Decision**: unrepairable (in scope to flag, out of scope to mechanically rewrite)
  - **Rationale**: rewriting the three proposed_changes blocks (§"Proposed changes" lines 249-332) into literal before/after diff blocks would (a) require reading and exactly transcribing ~300 lines of slice content per block, (b) authoring substantive content (the actual replacement text is not yet committed by the producer agent — the bracketed prose is intentionally interpretation-deferred to the integrator), and (c) risk changing the audit's intent. The repairer authority is mechanical-and-surgical only. **Routing**: cycle-012 meta-phase template-improvement candidate. The cycle-011 uptake-note appended to `scaffolding/skill-candidates.md` (per Finding 8 repair) explicitly flags this template-friction signal for meta-phase consideration — the proposed_changes-block format may fold into the `phase-1-slice-reduction-audit` skill's scope or become a sibling skill.

### Unrepairable findings

- **Finding 10**: proposed_changes-block bracketed-prose syntax (carried-from-cycle-010 template friction). Routing: cycle-012 meta-phase template-improvement candidate; flagged in `scaffolding/skill-candidates.md` cycle-011 uptake-note. Not a blocker — the cycle-010 precedent confirms the integrator accepts this shape; this is a template-quality improvement opportunity, not a content error.

## Suggested resolution

`overall_status: pass-after-repair`. All citation-validity warnings are fixed surgically (off-by-ones and ordinal conflations corrected; framing imprecisions softened to match the rest of the report's own internal language). The skill-uptake-survey warning is addressed by appending an explicit cycle-011 uptake-note to the candidate's any-agent-appendable channel entry, recording recurrence-2 and routing meta-phase batch-2 for promotion. The one unrepairable finding (proposed_changes-block format) is non-blocking template-improvement work routed to cycle-012 meta-phase. Integrator-per-report can proceed with the three slice partial-reductions as proposed.
