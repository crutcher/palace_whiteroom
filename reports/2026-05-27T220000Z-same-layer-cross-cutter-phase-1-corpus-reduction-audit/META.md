---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T22:30:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: warning
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-27T23:00:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: repaired
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Phase 1 corpus reduction audit — krylov-step chain overlap (first instance)"

## Critique

### Checks run

**citation-validity** — `warning`. Slice line-counts and section anchors verified against the on-disk files. All firm-entry paths cited resolve (L1/ksp_solve.md, L1-L0/ksp-solve-mutation-rotation.md, L2/krylov-step.md, L4/krylov-step.md, L3-L2/krylov-step-body-identity.md, L4-L3/krylov-step-typed-wrapper-dissolution.md, L1-L0/minres-iteration.md, L1-L0/bicgstab-iteration.md). The Palace bug-flag in cg.md (the `!B && initial_guess` branch at `iterative.cpp:399-412` computing `initial_res = (b·b)^{1/4}`) is faithfully extracted from cg.md:95 and cg.md:286 — not fabricated. Several boundary citations are off-by-1 (cosmetic) but one citation is materially off: the report's "(lines 549-789 of that file)" anchor for the L1-L0/ksp-solve-mutation-rotation Verified-against table — the actual Verified-against section spans lines 547-687, and the file ends at line 788, not 789. The "549-789" range is wrong on both endpoints. Gmres.md line count given as 1145, actual is 1144 (off by 1; cosmetic). The slice section-boundary line numbers in the supersession map are nearly all off by 1 in a systematic way (cited as "lines 38-125", "lines 243-330", "lines 332-495", "lines 497-631" etc., where the actual `## H2` headers land at 36, 243, 332, 497 and the section just-before-next-header endings are 125, 331, 496, 632 — i.e., the report's line ranges are systematically off by 1-2 lines at the boundaries).

**surface-or-evidence** — `pass`. This is an audit-shaped dispatch ("observation kind: variant-axis coverage gap (audit-scoped)"); no surface mutation is asserted, and the residual-gap claims about gmres.md L4 v0.2-v0.6 (lines 497-1143) are spot-verified — the v0.2 self-rotation derivation at gmres.md:497 onward is materially distinct from `concepts/derived-view-hoisting.md` content and the (non-existent) candidate `concepts/witness-typed-dispatch.md`. The slice content for v0.6 closing at line 1144 with the explicit "candidate methodology concept ('witness-typed dispatch') that may warrant extraction if it recurs in other slices" further confirms the slice carries unique not-yet-lifted methodology evidence.

**rotation-quality** — `pass`. Not applicable to audit dispatch (no algebraic rotation asserted). Marked pass per critic rubric.

**variant-axis-coverage** — `pass`. The audit explicitly enumerates which axes are covered by firm entries (krylov-method axis collapsed into opaque `Solver[A]` at L1, preconditioner-side at L2 `op.BA`, orthogonalization variant `gs_orthog ∈ {MGS, CGS, CGS2}` at L2 `op.orthog` with arnoldi_step.md MPI-allreduce shape cited as variant-evidence), and which axes (e.g., the GMRES Givens-rotation primitive vocabulary) are noted as elided in firm entries — that elision is verified against L2/krylov-step.md:40-67, which indeed stays at the five-group level and contains no Givens enumeration. Variant-axis coverage of the audit itself is complete: krylov-method, preconditioner-side, orthogonalization variant, first-iteration-unrolling, polynomial-recurrence (referenced for cycle-011+ batch).

**cross-reference-integrity** — `warning`. All cited firm-entry file paths exist under `book/src/`. All cited concept slugs exist under `book/src/concepts/` (`derived-view-hoisting.md`, `first-iteration-unrolling.md`, `sequential-obstruction.md`, `state-stratification.md`, `solve-monad.md`, `convergence-test.md`, `variant-absorption.md`, `apply_BA.md`, `orthogonalization.md`, `givens_apply.md`, `givens_generate.md`). All cited L0 chapters exist (`ksp-factory-file.md`, `kspsolver-base-class.md`, `linalg-iterative-file.md`). However: the report's recommended-action for cg.md says "Stub sections that are fully superseded: ... §'L2→L3 rotation claims (retroactive)' (move to methodology-history)" — but the proposed_change for cg.md is "Replace lines 1-339; retain lines 367-506" which leaves lines 340-366 (the actual L2→L3 retroactive section spanning lines 341-367) **in-file unchanged**. The recommended-action narrative and the proposed_change line range disagree about whether the L2→L3 retroactive section is stubbed or retained. Also: the report claims `book/src/concepts/givens_generate.md` and `givens_apply.md` "are NOT in firm entries" by implication (it says the L2 entry's Givens-vocab is mentioned by reference only), but those concept pages do exist — the report's "Lifting target" for #3 of gmres.md residual gaps may be partially wrong if it intended to assert no firm vocabulary exists at all. (The L2 `krylov-step.md` entry indeed elides Givens — that part is correct — but the concept pages exist, which softens the residual-gap claim.)

**edge-label-fidelity** — `warning`. The supersession map prose generally tracks the L_{n+1}>L_n edge labels correctly (slice §L3 → firm L3/krylov-step + firm L3-L2/krylov-step-body-identity; slice §L4 → firm L4/krylov-step). However, the partial-reduction proposed_change line ranges have boundary issues that, at integration, would cause structural problems: (a) cg.md's "Replace lines 1-339" leaves the §"L2→L3 — rotation claims (retroactive, cycle 116)" section (lines 341-367) intact in-file, contradicting the recommended-action narrative; (b) gmres.md's "Replace lines 1-495" — verified — leaves line 496 (a blank line) stranded, which is operationally fine but worth noting; (c) the proposed_change for cg.md says "retain lines 367-506" but §"L4 v0.5" actually starts at line 368, so lines 367 is the trailing blank of the L2→L3 section just before the v0.5 header. The line arithmetic is brittle; the integrator-per-report will need to reconcile the narrative intent against the line ranges. Also: the L1-L0/ksp-solve-mutation-rotation cite "(lines 549-789)" for the Verified-against table is wrong (actual range 547-687); the L1>L0 lowering edge prose is intact, but the citation pointer is wrong.

**plan-kind-consistency** — `pass`. The dispatch correctly declares itself an audit (`same-layer-cross-cutter`-scoped per priority #19) and does NOT mutate any slice file directly — all reductions are encoded as `proposed_changes` for downstream integrator-per-report dispatches. The Caveat-7 ("no slice file is mutated by this dispatch") is faithful. The status is "pending" rather than asserting any partial-reduction has happened. The Recommendation section correctly defers the mutation work to integrator-per-report. Plan-kind matches content shape.

**skill-uptake-survey** — `pass`. The audit template established (Supersession map / Residual gaps / Recommended action / Proposed changes per slice) is recognizably structured for cycle-011+ replay. Caveat-6 explicitly addresses skill-uptake by noting "the audit template established here ... is machine-replayable. Subsequent cycle-011+ slice audits should reuse this template directly." The dispatch correctly surfaces a batch-bounding observation ("the per-cycle batch should bound to 2-4 slices to keep dispatches within context budget"). One observation: the template would benefit from being lifted into a skill (`skills/phase-1-corpus-reduction-audit/`) — see also the skill-candidates appendix below. No skill currently exists for this audit shape; the cycle-009 meta-batch closure created priority #19 but did not pre-register a skill, so absence of skill-uptake is methodologically consistent with current state.

### Issues found

**Issue 1 — citation off in L1-L0/ksp-solve-mutation-rotation Verified-against range** (CYCLE.md:42, "Verified-against (lines 549-789 of that file)"). Actual span is lines 547-687; file ends at 788. The cite mis-states both endpoints. Severity: medium (substantive citation error). Repairable by patch.

**Issue 2 — proposed_change for cg.md narrative/range mismatch** (CYCLE.md:82-84, the Recommended-action prose says §"L2→L3 rotation claims (retroactive)" should be stubbed/moved-to-methodology-history; the proposed_change at CYCLE.md:152-153 replaces "lines 1-339" and retains "lines 367-506" — leaving lines 340-366 (the actual §"L2→L3 rotation claims" section at lines 341-367) unchanged in-file). The integrator-per-report cannot resolve this without a narrative-or-range fix. Severity: medium-high (structural inconsistency that blocks clean integration). Repairable by adjusting the proposed_change line range OR adjusting the recommended-action narrative; one of the two must yield.

**Issue 3 — slice-section boundary line numbers systematically off-by-1 in supersession maps** (CYCLE.md:42-48 for gmres.md; CYCLE.md:65-73 for cg.md; CYCLE.md:91-96 for arnoldi_step.md). Cited boundaries like "lines 38-125" / "lines 243-330" / "lines 332-495" / "lines 497-631" etc. consistently start 1-2 lines after the actual `## H2` header (the actual headers land at 36, 243, 332, 497) and end 1-2 lines before the next section's header. Each range is wrong by ~1-2 lines on both endpoints. Severity: low (cosmetic; supersession-map prose is still recognizable). Repairable by per-section boundary recalibration.

**Issue 4 — gmres.md line count claim** (CYCLE.md:8, "1145 lines"; CYCLE.md:208, "1145 lines"; CYCLE.md:119, "retain lines 497-1145"). Actual file is 1144 lines. The proposed_change "retain lines 497-1145" would index past EOF — operationally harmless but technically incorrect. Severity: low (cosmetic). Repairable.

**Issue 5 — Givens-vocab residual-gap claim potentially over-broad** (CYCLE.md:53, "the `givens_generate` / `givens_apply` L2 primitive vocabulary is mentioned in firm entries by reference only"). The concept pages `book/src/concepts/givens_generate.md` and `book/src/concepts/givens_apply.md` exist on disk; the L2/krylov-step.md entry indeed elides them at the operator level, but the residual-gap framing should distinguish "no firm L1 operator" from "no firm vocabulary anywhere." Severity: low (clarification only). Repairable.

**Issue 6 — Slice-section coverage claim for cg.md §"L4" sections inconsistent with actual structure** (CYCLE.md:70, "§'L4' v0.1–v0.5"; CYCLE.md:71-74 references v0.4 / v0.5 derivations). The actual cg.md has §"L4" as a single monolithic section (lines 139-282), then §"Working Notes" (283-294), then §"L4 v0.4 — derived-view hoisting (self-rotation)" (295-340), then §"L2→L3" retroactive (341-367), then §"L4 v0.5" (368-483), then §"L4 v0.5 ... claim ratification" (484-506). The slice does NOT have separate v0.1/v0.2/v0.3 sub-sections — the report's phrasing "L4 v0.1-v0.4" suggests multiple sub-sections, but cg.md's L4 is monolithic. This is a presentation-only confusion. Severity: low. Repairable by tightening the phrasing.

**Issue 7 — Caveat-1 sequencing dependency is correctly recorded** (CYCLE.md:221). The L3/krylov-step backfill from cycle-010 wave-1 is identified as pending-integration as of this dispatch; the directory listing confirms `book/src/L3/` contains only `index.md`. The dispatch correctly flags this and recommends sequencing the L3/krylov-step landing before slice reductions. No issue here; called out as a strength.

**Issue 8 — initial-residual Palace bug-flag faithfully extracted** (CYCLE.md:67-68 + CYCLE.md:76; cg.md:95 + cg.md:286 + cg.md Working Notes). Verified verbatim against the slice's Working Notes. Not a fabrication. No issue; called out as a strength.

**Issue 9 — first-instance audit template structural critique**. The template (Supersession map / Residual gaps / Recommended action / Proposed changes) is mostly clean, but exhibits the following friction points that will recur at cycle-011 replay if not crystallized into a skill:
- Line-range arithmetic is brittle: the dispatch repeatedly cites slice line ranges that drift by 1-2 lines from actual `## H2` boundaries (Issue 3). A skill-form would prescribe a `grep -n "^## "` step to anchor line numbers before claiming ranges.
- The Recommended-action narrative and the proposed_change line ranges are produced separately and can drift (Issue 2 demonstrates this). A skill-form would prescribe a final reconciliation pass: "for each section the narrative says to stub, the proposed_change must include that section's actual line range; verify before emission."
- The slice's table-of-contents (the `^## ` sections) should be enumerated once upfront and referenced in the supersession map by section name + actual line range; the report instead interleaves section name + cited range + claimed-supersession-target in long prose paragraphs, which is harder to audit. Severity: medium (this is the first-instance precedent; pre-empting drift at cycle-011 is worth a skill promotion). Repairable by tightening the template into a skill.

**Issue 10 — OQs 2-4 are well-grounded; OQ 1 has a verifiable false-precision** (CYCLE.md:221, OQ-1 references "the harvester-l3-krylov-step CYCLE.md at reports/2026-05-27T215300Z-harvester-l3-krylov-step/"). The report path stub form is plausible but not verified by this critic against the live `reports/` directory state. (Verifying directly would exceed inspection-only scope; flagged as a hedge.) The other OQs (initial-residual quirk lift path; L1/orthogonalize promotion; cycle-011+ batch priority list; audit template machine-replayability) are well-grounded in audit evidence and not speculative. Severity: low. No repair needed.

**Issue 11 — Caveat-7 ("no slice file is mutated by this dispatch") is faithful and load-bearing**. The dispatch correctly identifies that all proposed reductions are encoded as `proposed_changes` blocks for downstream integrator-per-report, not as direct in-place mutation. This is correctly scoped to the same-layer-cross-cutter authority. No issue; called out as a strength.

## Repair

### Fixes attempted

- **Finding 1 — citation-validity warning (Issue 1 — `L1-L0/ksp-solve-mutation-rotation` Verified-against range mis-cited as "549-789"; actual is 547-687, file ends at 788)**.
  - **Decision**: repaired.
  - **Action**: edited CYCLE.md line 42 (supersession map for gmres.md §L0) to change "(lines 549-789 of that file)" → "(lines 547-687 of that file)"; edited supporting-evidence line 212 to change "(789 lines; ... `verified_against` rows at lines 700-789)" → "(788 lines; ... `verified_against` rows at lines 547-687 (§"Verified-against" header at line 547, body through line 687, §"Status" at line 688))". Verified against `book/src/L1-L0/ksp-solve-mutation-rotation.md` headers (§"Verified-against" at line 547; §"Status" at line 688; file ends at line 788).

- **Finding 1 — citation-validity warning (Issue 4 — gmres.md line count cited as 1145, actual is 1144; "retain lines 497-1145" would index past EOF)**.
  - **Decision**: repaired.
  - **Action**: replaced all "1145" → "1144" in inputs frontmatter, Summary, Slice 1 heading, proposed_change 1 (the "retain lines 497-1145" → "retain lines 497-1144"), and supporting-evidence. Verified `wc -l book/src/spec/slices/gmres.md` = 1144. Also tightened the §"L4 v0.2"-§"L4 v0.6" supersession-map line ranges to use actual `## H2` boundaries (497-632, 733-818, 819-905, 906-1011, 1012-1144) per `grep -n "^## " gmres.md`. Updated OQ-2's "lines 497-1143" → "lines 497-1144".

- **Finding 1 — citation-validity warning (Issue 3 — slice-section H2 boundaries systematically off-by-1)**.
  - **Decision**: repaired (cosmetic alignment).
  - **Action**: ran `grep -n "^## "` on `gmres.md`, `cg.md`, `arnoldi_step.md` and rewrote supersession-map line ranges to match actual H2 header positions. For gmres.md: §L1 38-125 → 36-125 (header at 36); §"Open questions" 127-133 → 126-134; §L3 243-330 → 243-331; §L4 v0.1 332-495 → 332-496. For cg.md: §L1 40-95 → 40-96; §L2 97-123 → 97-122; §L3 124-138 → 123-138; §L4 (monolithic) 140-281 → 139-282; §"L4 v0.4" 295-339 → 295-340; §"L2→L3" 341-366 → 341-367; §"L4 v0.5" 367-482 → 368-483. For arnoldi_step.md: §L0 36-69 → 36-71; §L1 70-119 → 72-120; §L2 121-176 → 121-177; §L3 178-245 → 178-246. Annotated each range with its `## H2` header line in parentheses to ease future audit replay.

- **Finding 1 — citation-validity warning (Issue 6 — cg.md §L4 sub-section structure misrepresented as "v0.1-v0.5"; actual L4 is a single monolithic section)**.
  - **Decision**: repaired.
  - **Action**: rewrote the cg.md supersession-map §L4 bullet (CYCLE.md:70) to describe L4 as "monolithic" with sub-sections at §"Working Notes" (283), §"L4 v0.4 derived-view hoisting (self-rotation)" (295), §"L2→L3" (341), §"L4 v0.5" (368), and §"L4 v0.5 claim ratification" (484). The original "v0.1-v0.5" phrasing was a presentation-only confusion and is now explicit about the structure.

- **Finding 2 + 3 — cross-reference-integrity warning + edge-label-fidelity warning (Issue 2 — cg.md narrative says §"L2→L3 rotation claims (retroactive)" should be stubbed/moved-to-methodology-history, but the proposed_change "Replace lines 1-339; retain lines 367-506" leaves lines 340-366 (the L2→L3 retroactive section at 341-367) stranded in-file)**.
  - **Decision**: repaired.
  - **Action**: extended the replace range to include §"L2→L3" — proposed_change 2 now reads "Replace lines 1-366; retain lines 367-506". This matches the recommended-action narrative ("move to methodology-history"). The retained range 367-506 begins at line 367 (the blank line trailing §"L2→L3"), preserving the original separator before §"L4 v0.5" at line 368. Stub header text already correctly described §"Working Notes" as "now-stubbed" and §"L4 v0.1-v0.4" as superseded — the bullet list of stub/retain sections at CYCLE.md:81-84 was inconsistent with the stub header text + range (it claimed Working Notes + L4 v0.4 retained, but proposed_change had them inside 1-339); rewrote the bullet list to match the stub header text + new range (Working Notes' unique findings hoisted into the stub header's "Open questions still pending lift" subsection; L4 v0.4 superseded by `concepts/derived-view-hoisting.md` + the v0.5 self-rotation). All three statements (bullet list, stub header, proposed_change line range) are now internally consistent: replace 1-366, retain 367-506 (the L4 v0.5 first-iteration-unrolling derivation + claim ratification only).

- **Finding 3 — edge-label-fidelity warning (Issue 3 boundary cleanup for arnoldi_step.md proposed_change "Replace lines 36-69")**.
  - **Decision**: repaired.
  - **Action**: changed proposed_change 3's "Replace lines 36-69" → "Replace lines 36-71" (§"L0 — palace source" actually spans lines 36-71; line 72 starts §"L1"). Also updated "lines 70-119 (§L1)" → "lines 72-120 (§L1)" in the retain enumeration. Also updated the inner "The replacement for lines 36-69 §L0" reference inside the proposed_change to "lines 36-71".

- **Finding (Issue 5) — Givens-vocab residual-gap framing potentially over-broad**.
  - **Decision**: repaired.
  - **Action**: clarified the gmres.md residual-gap #3 (CYCLE.md:53) to distinguish "concept pages `givens_generate.md` / `givens_apply.md` exist as firm vocabulary" from "no firm L1 operator entry exists" — explicit about which kind of firmness is present and which is not.

- **Finding (Issue 9) — first-instance audit template friction (line-range arithmetic brittleness, narrative-vs-range drift, table-of-contents enumeration discipline)**.
  - **Decision**: not directly repairable by this repairer; the friction is addressed via a skill promotion which is meta-phase work.
  - **Action**: verified `scaffolding/skill-candidates.md` already contains a `phase-1-slice-reduction-audit` skill candidate proposed by the critic (skill-candidates.md:114-115). No edit from repairer authority. Meta-phase will judge promotion at the next 3rd-cycle boundary; the friction is durably captured for that judgment.

- **Finding (Issue 7, 8, 10, 11) — strengths called out by critic (no repair needed)**.
  - **Decision**: not-needed.

### Unrepairable findings

None. All warning-graded findings (citation-validity, cross-reference-integrity, edge-label-fidelity) were mechanically repairable by reading the actual cited files (gmres.md / cg.md / arnoldi_step.md / L1-L0/ksp-solve-mutation-rotation.md) and patching line ranges + reconciling the cg.md narrative-vs-range mismatch. Issue 9 is informational (skill-uptake friction); it is captured in scaffolding/skill-candidates.md and is meta-phase work, not repairer work.

## Suggested resolution

`ready`. All citation-range errors patched against actual file content; cg.md narrative-vs-range mismatch reconciled by extending the replace range to include §"L2→L3" (matching the recommended-action narrative); arnoldi_step.md proposed_change boundaries tightened; cosmetic H2-boundary drift across all three slices systematically corrected. The proposed_change blocks are now internally consistent (narrative + line ranges agree) and ready for integrator-per-report application.

Integrator-per-report can apply the three proposed_changes in any order; the cycle-010 wave-1 `harvester-l3-krylov-step` report should be applied first per Caveat-1 (the stub-header text references `book/src/L3/krylov-step.md` as firm; that file must exist on disk before the slice reductions land or the cross-references will dangle). Integrator-finalize for cycle-010 should sequence: harvester-l3-krylov-step → other wave-1 reports → wave-2 reports including this audit's three slice reductions.
