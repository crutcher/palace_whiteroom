---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T23:55:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: warning
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-28T00:02:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of harvester L3 apply_linop firm entry (cycle-011)

## Critique

### Checks run

**citation-validity** — warning. Spot-checked the major citations against the artifact and reference source. The vast majority verify cleanly:

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:64` renders `let w = apply_linop op.T K.<input_field>` (confirmed by direct read of that line).
- `book/src/L3-L2/krylov-step-body-identity.md:30` renders the same L3 form; line 97 contains the seven-primitive structural argument the report quotes verbatim (confirmed).
- `book/src/L3/index.md:13` does advertise "matvec, axpy, dot, nrm2 as field operations" (confirmed).
- `book/src/L4/krylov-step.md:59` contains `let w = apply_linop op.T K.<input_field>` as the first body line (confirmed at line 59).
- `book/src/L2/krylov-step.md:96, 130-132` — line 96 is the L1 primitives Dependencies list (apply_linop included); line 131 is the "L2 vs L1 distinction" stating L1 contains primitives like `apply_linop`. Confirmed.
- `palace/linalg/operator.hpp:202-206` shows `B.Mult(x, z); A.Mult(z, y);` — direct witness for law 4 (composition). Confirmed.
- `palace/linalg/iterative.cpp:379, :443` are `A->Mult(x, r)` / `A->Mult(p, z)` (CG residual + inner-loop matvec). Confirmed.
- `palace/linalg/rap.cpp:212` is `trial_fespace.GetProlongationMatrix()->Mult(...)` (prolongation-matrix Mult witness). Confirmed.

The warning is on the **five Phase-1 slice instances** section (CYCLE.md lines 230-234):

- `book/src/spec/slices/cg.md:103-115, :172-188, :393-425` — the cg.md file is **165 lines long**. Two of the three sub-ranges (172-188, 393-425) and the upper part of the first (103-115) **exceed the file length** and therefore cannot point to live content. Likely transcribed from a pre-reduction version of the cg slice; per CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is lifted", the slice was likely compacted. The L0-equivalent semantic content is present elsewhere in the slice (the surviving `apply` calls at cg.md:58, 75) but the cited ranges do not.
- `book/src/spec/slices/arnoldi_step.md:99-105` — this range does cover `apply_linop(T, V[j])` at line 99 and following lines through 109 — in-range and the cited content matches.
- `book/src/spec/slices/arnoldi_step.md:285-298` — this range covers the variant-absorption and obstruction-recording prose around the Arnoldi step at L4, not direct `apply_linop` use. The phrase "field-side apply" is in line 302 (out of cited range). The range is loosely supportive but not a direct apply_linop site as the report frames it.
- `book/src/spec/slices/polynomial_recurrence_step.md:119-160` — the range covers the polynomial-recurrence catalog (Chebyshev sites + GMRES Givens) which describes the recurrence shape but **does not textually contain `apply_linop`** — the matvec is implied by `r := residual(x, A, y, …)`. The report's framing "three polynomial-recurrence sites; each calls `apply_linop` once per step" is structurally correct but the cited range does not show the primitive's name.
- `book/src/spec/slices/gmres.md:459-471` — in-range (gmres.md is 671 lines); range covers GMRES L4 `inner_loop` body. Acceptable.
- `book/src/spec/slices/chebyshev.md:354-362` — in-range; covers Chebyshev L4 `innerStep`. Acceptable.

**surface-or-evidence** — pass. The proposal is firm-shaped (new L3 operator entry); the content creates surface (the L3 apply_linop entry, the L3 index dep-map row, the SUMMARY.md insertion) and is appropriately anchored in evidence (the firm L1 entry, the two firm cross-layer themes that render apply_linop as L3-native, the cycle-010 audit's HIGH CONFIDENCE backfill recommendation). This is a layer-coherence backfill (not a refinement of an existing entry), so the surface-or-evidence axis is satisfied by the surface creation itself.

**rotation-quality** — pass. The proposed rotation is **identity-in-form on the primitive's signature** — the report is explicit about this and does not claim a compression / abstraction rotation. The justification is per the methodology invariant "Identity-lowerings still require both L levels" (CLAUDE.md, cycle-009 codification): even when the rotation is value-thread-isomorphic, the L3 entry exists for layer-coherence. The report does not over-claim a substantive rotation; the cycle-010 audit's "identity-in-form on the primitive's signature" framing is honored throughout. The L4>L3 absence (no L4 standalone) is also a deliberate verdict, not a rotation-quality failure.

**variant-axis-coverage** — warning. The proposal claims **four variant axes at L3** (element-type, transpose-mode, accumulate-mode, operator-representation) and asserts "the same four as at L1, inherited unchanged" (CYCLE.md line 170, 180). The **L1 entry, however, frames it as three orthogonal axes plus one collapsed-and-absorbed axis** (`book/src/L1/apply_linop.md:75-83`): the L1 file's exact phrasing is *"`apply_linop` has three orthogonal variant axes at L1; a fourth axis is collapsed and recorded as deliberate absorption."* The four-axis content is the same on both sides, but the report's claim of exact-inheritance ("the same four ... inherited unchanged") elides the orthogonal-vs-absorbed framing distinction the L1 entry took care to make. The frontmatter `variant_axes:` block lists all four uniformly without distinguishing operator-representation as the absorbed axis. This is a framing mismatch with the L1 source rather than a coverage gap (all four axes are addressed in the §"Variant axes" section), but it does mean the report's "inherited unchanged" claim is not literally true at the framing level — it merges the three+one structure into one four. Either the L3 entry should adopt the same three-orthogonal-plus-one-absorbed split as L1, or it should explicitly note the framing change.

**cross-reference-integrity** — pass. All cited concept slugs exist (`apply_BA.md`, `constructed-operators.md`, `variant-absorption.md`, `apply_linop.md` under `concepts/`). All inter-layer references exist (L1/apply_linop.md, L3/krylov-step.md, L4/krylov-step.md, L4-L3/krylov-step-typed-wrapper-dissolution.md, L3-L2/krylov-step-body-identity.md, L1-L0/apply-linop-mutation-rotation.md). SUMMARY.md line 19 is `- [krylov-step](./L3/krylov-step.md)` — the proposed insertion point (after this line) is correct. L3/index.md line 21 is the krylov-step row — the proposed dep-map append after this row is correct. Reports and meta paths resolve.

**edge-label-fidelity** — pass. The proposal carries L3→L1 (direct, via no interposed L3-L2 theme) and L4-(absent)→L3 edge framings. The §"Lowers to" section discusses the L3>L1 hop; the §"Lifts from" section discusses the L4 absence. Both sections discuss the correct edges; no edge-label-vs-prose mismatch.

**plan-kind-consistency** — pass. The report declares `firmness: firm` (in the proposed frontmatter) and the content matches a firm L3 operator shape — full signature, semantics, seven algebraic laws, four non-laws, four-axis variant profile, dependencies, status, two distinction sections (L3 vs L4, L3 vs L1), substantial evidence section. The §"Status" paragraph (line 184) explicitly defends the `firm` classification with the value-thread-isomorphism argument. No rough-in placeholders; no speculative content masquerading as firm.

**skill-uptake-survey** — pass (informational). The dispatch shape — layer-coherence backfill at an adjacent layer where the rotation is identity-in-form — does not match the existing skill set (`classify-variant-axis`, `verify-citation-range`, `skill-selection`, `verify-refinement-surface`, `plan-sideways-concept-emission`, `embed-and-persist-subagent-dispatch`) directly. The closest applicable skill is `verify-citation-range` (would have caught the cg.md out-of-range citation issue); no explicit invocation note appears in the report, but the report does not claim to invoke skills explicitly. Not blocking.

### Issues found

1. **Citation out-of-range (CYCLE.md §"Evidence" lines 230-234, "Five Phase-1 slice instances")** — Severity: **medium**. The cited ranges `book/src/spec/slices/cg.md:103-115, :172-188, :393-425` exceed the file's actual length (165 lines). The slice was likely reduced post-Phase-1 (per the "Phase 1 corpus reduces as material is lifted" methodology); the ranges appear to be inherited from an earlier longer version. The report's framing "Five Phase-1 slice instances where `apply_linop` appears as the per-step matvec" is structurally correct (CG, GMRES, Chebyshev, Arnoldi, polynomial-recurrence all use the primitive), but the cg.md ranges as cited cannot resolve to live content. Suggested fix: update to the current cg.md content (e.g., cg.md:58, :75 are the surviving apply-site lines) or replace with a less-specific "see cg.md sections covering the per-step matvec" reference.

2. **Citation tangential / not directly showing the primitive (CYCLE.md §"Evidence" lines 232-234)** — Severity: **low**. The cited ranges `arnoldi_step.md:285-298` and `polynomial_recurrence_step.md:119-160` are within file bounds but do not textually contain `apply_linop`. The arnoldi range is about variant absorption and obstruction recording; the polynomial-recurrence range is the recurrence catalog where the matvec is referenced as `residual(x, A, y, …)` rather than by the L1 primitive name. The structural content is consistent with the report's claim but the citations don't directly show the primitive's appearance. Suggested fix: replace `arnoldi_step.md:285-298` with the in-range hit at `arnoldi_step.md:99-109` (or extend the existing 99-105 range); for the polynomial-recurrence slice, either tighten the range to a section where `apply_linop` is named (sections elsewhere in the slice may have direct mentions) or rephrase as "where the per-step matvec is referenced structurally".

3. **Variant-axis count framing inconsistency with L1 source (CYCLE.md lines 170-180, frontmatter `variant_axes:`)** — Severity: **medium**. The report frames four variant axes at L3 ("the same four as at L1, inherited unchanged"); the L1 source explicitly frames three orthogonal axes plus one collapsed-and-absorbed axis (`book/src/L1/apply_linop.md:75-83`). The four-axis content is consistent across both files, but the L3 entry's "inherited unchanged" claim is literally false at the orthogonal-vs-absorbed framing level. The L3 entry merges what L1 distinguishes structurally. Either: (a) restructure §"Variant axes" to mirror the L1 three-orthogonal-plus-one-absorbed split (recommended for fidelity to the inheritance claim), or (b) add a one-line note that the L3 entry consolidates the L1 framing's "three orthogonal + one absorbed" into a uniform four (noting the framing change explicitly).

4. **Status block's variant-axis claim "closed at four, inherited unchanged" (CYCLE.md line 184)** — Severity: **low**. This statement also asserts unchanged inheritance; same framing issue as Issue 3. Tracking as a separate touch-point because it's in §"Status" and may be revised in parallel with the §"Variant axes" section.

5. **No `L3-L1/` lowering directory created; in-line identity treatment is chosen (CYCLE.md §"Open questions / caveats" point 1)** — Severity: **low (observational)**. The report deliberately chooses in-line treatment over creating an `L3-L1/apply-linop-identity` theme file, and surfaces the policy decision as an OQ for the cycle-011+ planner. Not a defect; the choice is justified (three reasons given). Recording here so the integrator-per-report agent can surface the OQ to `scaffolding/open-questions.md` per write-authority partition. No fix needed in the report itself.

6. **L4 absence framing — "Lifts from" section content vs frontmatter** — Severity: **low**. The proposed frontmatter `lifts_from:` field reads `(no L4 entry; apply_linop appears inside book/src/L4/krylov-step.md as a let-binding…)` (CYCLE.md line 58). This is a prose value where the format conventionally expects a list of edge references. The L3/krylov-step.md precedent has `lifts_from: - book/src/L4/krylov-step.md (via …)`. Suggested touch-up: either keep prose but mark as `lifts_from: [] # see §"Lifts from" — L4 candidate confirmed-not-needed per cycle-010 audit` for clarity, or leave as-is if the prose-value convention is acceptable across the project. Compare against existing entries' frontmatter conventions during integrate.

7. **Cycle-id label in proposed L3/index.md row "harvested cycle-011T234502Z"** — Severity: **low**. The label format mixes cycle counter ("cycle-011") with the timestamp ("T234502Z"). The L3/index.md krylov-step row uses "harvested cycle-010T215300Z" — same pattern. The format is consistent with precedent so this may be intentional; flagging as a minor stylistic note in case the integrator-finalize prefers a canonical cycle-id format.

## Repair

### Fixes attempted

**Finding 1 (citation-validity warning, Issue 1): cg.md ranges out-of-range** — Severity medium.
- **Decision**: repaired.
- **Action**: In CYCLE.md §"Evidence" "Five Phase-1 slice instances" list (now retitled "Phase-1 slice instances", since one bullet was consolidated): replaced `book/src/spec/slices/cg.md:103-115, :172-188, :393-425` with `book/src/spec/slices/cg.md:58, :75` (the two surviving apply-call sites inside `cg_first_step` and `cg_steady_step` of the v0.5 form, which is the unique material retained post-cycle-010-reduction). Added a parenthetical note explaining the slice is the reduced-stub form per CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is lifted".
- **Verification**: confirmed by grep that lines 58, 75 of the current cg.md (165 lines total) contain `let Ap = apply opA p'` in both `cg_first_step` and `cg_steady_step` bodies.

**Finding 2 (citation-validity warning, Issue 2): tangential citations in arnoldi_step.md and polynomial_recurrence_step.md** — Severity low.
- **Decision**: repaired (arnoldi_step.md); repaired-by-removal (polynomial_recurrence_step.md).
- **Action**:
  - `arnoldi_step.md:99-105, :285-298` → replaced with `arnoldi_step.md:99-109, :146, :158, :197`. The four sub-ranges all directly contain the `apply_linop(T, V[j])` text (confirmed by grep): line 99 names it in the procedure step list; line 146 explicitly names it as a pure-functional primitive; line 158 cross-cuts to the concept page; line 197 is the L3-form rendering with the field-side-global comment.
  - `polynomial_recurrence_step.md:119-160` → removed. The cited range textually contains only the polynomial-recurrence catalog where the matvec is implied by `residual(x, A, y, …)` shorthand, not by the `apply_linop` primitive name. The bullet is dropped from the list; the structural-claim narrative is unaffected because the four remaining bullets (cg, gmres, chebyshev, arnoldi_step) carry the canonical evidence.
- **Verification**: confirmed via grep that the new arnoldi_step.md ranges all contain literal `apply_linop` references; confirmed polynomial_recurrence_step.md has no textual `apply_linop` mention anywhere in the file.

**Finding 3 (variant-axis-coverage warning, Issue 3): "inherited unchanged" framing mismatch** — Severity medium.
- **Decision**: repaired.
- **Action**: In the proposed L3 entry §"Variant axes" section (CYCLE.md "Operator content" block): restructured to mirror the L1 entry's framing — "three orthogonal axes at L3, plus one collapsed-and-absorbed axis" (matching `book/src/L1/apply_linop.md:75-83` exactly). The three orthogonal axes (element-type, transpose-mode, accumulate-mode) are listed first; the collapsed (absorbed) axis (operator-representation) is listed under a separate sub-heading. The closing paragraph now reads "The variant-axis profile (three orthogonal + one absorbed) matches the L1 entry exactly" rather than the previous "The variant-axis count of four matches the L1 entry exactly." Also updated the frontmatter `variant_axes:` block to nest under `orthogonal:` and `absorbed:` keys (rather than the flat list).
- **Verification**: the orthogonal-vs-absorbed split now matches L1's framing literally; the "inherited unchanged" claim is now structurally true (not merging three+one into a uniform four).

**Finding 4 (Issue 4): §"Status" block's "closed at four, inherited unchanged"** — Severity low.
- **Decision**: repaired.
- **Action**: Replaced "variant-axis profile is closed at four, inherited unchanged" with "variant-axis profile is three orthogonal + one absorbed (the same framing as L1), inherited unchanged".

**Finding 5 (Issue 5): No `L3-L1/` directory created (observational)** — Severity low (observational, not a defect).
- **Decision**: not-needed. The report's §"Open questions / caveats" point 1 already surfaces this as an OQ for the cycle-011+ planner; no edit needed.

**Finding 6 (Issue 6): `lifts_from:` prose-value vs list-format** — Severity low.
- **Decision**: unrepairable (out of repair authority — frontmatter convention decision should be made by integrate or meta-phase, not mechanically by the repairer; the prose-value is informative and self-documenting; restructuring it to a list with a `# see §"Lifts from"` comment changes the convention across the project).
- **Rationale**: Per critic's own framing, the suggested touch-up is "compare against existing entries' frontmatter conventions during integrate." This is properly an integrator decision (which precedent to follow project-wide); not a mechanical-surgical fix the repairer should apply unilaterally.

**Finding 7 (Issue 7): Cycle-id label format consistency** — Severity low.
- **Decision**: not-needed. The critic acknowledges "the format is consistent with precedent so this may be intentional"; matches the L3/krylov-step.md cycle-010T215300Z pattern. No edit.

Also: I made the following derived edits to keep the document internally consistent with the variant-axis framing fix:
- The §"L3 vs L1 distinction" paragraph's "variant-axis count (four)" rephrased to "variant-axis profile (three orthogonal + one absorbed)".
- §"Open questions / caveats" point 5's "four axes" rephrased to "three orthogonal + one absorbed" to match.

### Unrepairable findings

- Finding 6 (`lifts_from:` frontmatter format): deferred to integrator-per-report — this is a project-wide convention decision (prose-value vs list-form-with-comment), not a mechanical fix. Recommend the integrator either accept the prose-value as is (it is self-documenting and informative) or surface as a separate OQ for project-wide frontmatter-convention codification.

## Suggested resolution

`overall_status: pass-after-repair`. All `warning` findings the critic flagged have been mechanically repaired (citation-validity Issues 1+2; variant-axis-coverage Issue 3 + the derived Issue 4); the three low-severity observational findings (Issues 5, 6, 7) are appropriately deferred:
- Issue 5 (no L3-L1 directory) is the report's own surfaced OQ — integrator should route to `scaffolding/open-questions.md`.
- Issue 6 (frontmatter prose vs list) is an integrator-convention decision, not a repair.
- Issue 7 (cycle-id format) is consistent with precedent.

The report is ready for integration. The integrator-per-report should:
1. Apply the proposed-changes blocks (L3/apply_linop.md create + L3/index.md row append + SUMMARY.md insert) — the variant-axes framing in the embedded entry now correctly mirrors L1's three-orthogonal-plus-one-absorbed split, and the evidence-section citations now resolve cleanly against the current (reduced) Phase-1 slice corpus.
2. Surface the L3-L1 directory policy decision (Issue 5 / report OQ 1) to `scaffolding/open-questions.md`.
3. Note the frontmatter prose-vs-list convention question (Issue 6) for either integrator-finalize decision or as a project-wide OQ.
