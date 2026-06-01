---
verifies: ../REPORT.md
critiqued_at: 2026-05-31T235349Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of "Formalize orthogonalize at L3" (L3 partial-obstruction)

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` clears all 36 citations (36 ok, 0 failing) for bounds + path hygiene. The load-bearing pinpoints were anchor-confirmed via the tool and then meaning-read against the on-disk source: `orthog.hpp:41-53` anchors `OrthogonalizeColumnMGS` (line 41) and the meaning-read confirms the per-`j` interleaved `H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm); w.Add(-H[j], V[j])` loop body at `:46-52` — the witnessed MGS sequential obstruction, exactly as claimed. `orthog.hpp:57-89` anchors `OrthogonalizeColumnCGS` (57); meaning-read confirms empty-basis early return `:62-64`, batched dots-against-original-`w` `:66-69`, single `GlobalSum(m, ...)` `:70`, batched `w.Add` `:71-74`, and the `refine`/CGS2 second pass `:75-88` — supporting the CGS/CGS2-lift claim. `orthog.hpp:18-23` anchors `normalize` at `:22` and the meaning-read confirms the "does not normalize the output vectors!" no-output-normalisation contract. `iterative.cpp:308-325` anchors `OrthogonalizeIteration`; the `switch (type)` over MGS/CGS/CGS2 sits at `:313-323` with `CGS2 = OrthogonalizeColumnCGS(..., true)` at `:321-322` exactly as cited. The consumer sites `iterative.cpp:630-632` (GMRES: `OrthogonalizeIteration` + `Norml2` + `w *= 1.0/Hj[j+1]`) and `:809-811` (FGMRES, identical) verify, supporting the "normalisation is the caller's" boundary. Test sites verify: `test-orthog.cpp:99-120` (empty-prefix, all three variants, `CHECK_THAT(w, RangeEquals(w_orig))` at `:120`), `:123-160` (real param, `TEST_CASE` at `:123`, close at `:160`), `:154-159` (orthogonality check, `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` at `:158`), `:234` (complex param TEST_CASE). Concept-page cites verify: `sequential-obstruction.md:37-48` is exactly the "Example: MGS as sequential-obstruction" section and `:22` is the MGS bullet with the "CGS is the parallel-reduction alternative ... `gs_orthog` variant" sentence; `variant-absorption.md:131` covers the orthogonalization variant absorption; `L3/index.md:47` matches the quoted (B)-verdict text; the L1/L2 forecast cites (`L1/orthogonalize.md:200-203`, `L2/orthogonalize.md:133-134, 290-292`) match the report's quotes. No `verified_against:` block is emitted (harvester report), so that sub-check is not applicable. One minor descriptor imprecision noted under Issues (the "check loop 154-159" off-by-one on the loop-start line), non-load-bearing.

**surface-or-evidence — pass.** Not a refinement of an existing operator/theme; this is a *new* L3 chapter (`new`-shaped, expressed as an `edit:` create) with full surface (signature, semantics, laws, status, evidence) plus the substantive iteration-rotation content. It is not a pure rotation_claim. Passes by construction.

**rotation-quality — pass.** The L3 form is a genuine rotation, not a rename. The iteration-rotation makes the variant-dependent loop structure explicit and equational: CGS/CGS2 collapse to the batched global statements `H = Vᴴw` / `w' = w − VH` (the basis index becomes a reduction/broadcast axis — strictly more compact/abstract than the per-column loop), while MGS is recorded as a witnessed sequential obstruction over the basis index with a cited non-removability reason. This is exactly the kind of state-hiding / loop-structure-exposure rotation the check wants. The honest "partial" verdict (one branch lifts, one obstructs) is the correct rotation outcome, not a degenerate 1:1 mapping.

**variant-axis-coverage — pass.** This is the report's strongest dimension and the one flagged for scrutiny. Three axes are declared (`gs_orthog`, `dot-hook`, `element-type`) and each is handled: `gs_orthog` is the *splitting* axis — MGS (non-lifting obstruction), CGS (lifts), CGS2 (`[CGS] × 2`, lifts) — each combination explicitly characterized in §Semantics, §Algebraic-laws (law 6 positive lift + the MGS-loop-lift non-law), and §Status. `dot-hook` (canonical / B-weighted) is scoped as parametric with an invariance claim on the lift split. `element-type` (real/complex) is scoped as fully parametric absorbed by `dot`. Householder is explicitly scoped out with a verified source basis: I independently confirmed `orthog.hpp` defines exactly `OrthogonalizeColumnMGS` and `OrthogonalizeColumnCGS` (no Householder path), so the unimplemented-component scope-out is well-grounded. The variant-conditional obstruction (MGS obstructs, CGS/CGS2 lift) is the correct and fully-disclosed treatment of the split — no hidden branch.

**cross-reference-integrity — pass.** All live `[link]` targets resolve on disk: `L3/dot.md`, `L3/axpy.md`, `L3/nrm2.md`, `L3/scal.md`, `L3/chebyshev.md`, `L3/eigsolve.md`, `L2/orthogonalize.md`, `L1/orthogonalize.md`, `L2/krylov-step.md`, `concepts/{sequential-obstruction,tensor-field-lift,variant-absorption,orthogonalization}.md`, `L1-L0/orthogonalize-mutation-rotation.md`, `L2-L1/orthogonalize-composition-lowering.md` all exist. `L4/orthogonalize.md` is absent on disk, but all three references to it are inline code spans (backticks), never live links — no dead-link build hazard, and the absence is correctly narrated ("unauthored"). The named slugs (`gs_orthog`, `partial-obstruction`, the three precedent operators) all resolve. Build-readiness fence guard: 6 top-level fence markers = 3 balanced `edit:` blocks (`orthogonalize.md` `:41`→`:634`, `index.md` `:636`→`:639`, `SUMMARY.md` `:641`→`:644`); the full firm apparatus (`## Status` `:483`, `## Signature` `:162`, `## Algebraic laws` `:332`, `## Evidence` `:528`) sits INSIDE the `orthogonalize.md` fence — no cycle-019 fence-truncation defect. Math (`$$`) and signature/value-thread forms use 4-space indentation rather than nested fences, so no nested-fence imbalance. The index.md context-anchor `normalize` row matches the on-disk `L3/index.md:37` verbatim (2355 chars, exact), so the integrator's anchored insert of the `orthogonalize` row lands cleanly. SUMMARY edit is a clean anchor (`normalize`, already on disk at SUMMARY `:37`) + new `orthogonalize` line.

**edge-label-fidelity — pass.** The frontmatter declares `lifts_from: L2/orthogonalize.md` and `lowers_to: L2/orthogonalize.md`; the prose (§Downward, §"L3 vs L2 distinction", §Dependencies, law 5) discusses exactly the L3↔L2 edge (body identity-in-form) and the transitive L3↔L1 consequence, both narrated in the declared direction. The substantive rotation is correctly attributed downward to the existing L1>L0 theme, not mislabeled. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is `partial-obstruction` (frontmatter `firmness: partial-obstruction`), and the content shape matches the cycle-021 invariant precisely: the per-step body lifts (whole-tensor `dot`+`axpy`, identity-in-form to the firm L2/L1 leaf), and the obstruction lives in the *loop structure* — here variant-conditionally, on the MGS `j`-loop — with a cited non-removability reason (numerical-stability; `sequential-obstruction.md:37-48`). The frontmatter key (`firmness:`) matches the precedent L3 partial-obstruction entries (`chebyshev`, `eigsolve`). High→low discipline holds: the L3 body is stated in L3 vocabulary (whole-tensor `dot`/`axpy`, `op.variant` dispatch), the lowering is narrated downward (L3→L2→L1), and the variant-split obstruction is rendered as an L3 iteration-rotation verdict rather than borrowed L0 mechanics. Not a mis-classified firm-with-placeholders entry.

**skill-uptake-survey — pass (telemetry).** The report references `tools/citecheck/citecheck.py --anchor` self-verification of the L0 citations (§Supporting evidence, lines 669-683), which is the expected procedure for a citation-heavy harvester entry. The `proposed-changes-fence-encloses-full-body-guard` is a critic-side guard (applied here), not a producer obligation. No skill invocation is conspicuously missing.

### Issues found

1. **Minor descriptor off-by-one on the test check-loop start line — `CYCLE.md` §Evidence (line ~562-563) and Algebraic-laws law 1 (line ~343).** The report describes "the per-rank orthogonality-check loop" / "inside the check loop 154-159". On disk, `test-orthog.cpp:154` is the comment `// Check full orthogonalization`; the `for` loop opens at `:155` and runs `155-159`. The load-bearing pinpoint — `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` at `:158` — is correct and anchor-confirmed, and `:154-159` is in-range, so this is a non-load-bearing descriptor imprecision (the cited range merely includes the preceding comment line). Severity: trivial. Candidate tightening: describe the loop as `:155-159` (or keep `:154-159` and call it "the check loop with its leading comment").

2. **No firm-defect issues.** Citation-validity, the partial-obstruction classification, the variant-axis split, count-ownership discipline, fence parity, and high→low discipline all clear. Specifically on the two items flagged for scrutiny in the dispatch: (a) the `partial-obstruction` status is correctly applied per cycle-021 with the variant-conditional split fully disclosed (MGS obstructs / CGS/CGS2 lift), and (b) count-ownership is respected — the report's `book/src/L3/index.md` edit is the dep-map row only (context-anchored on the on-disk `normalize` row) and explicitly defers the §Working-Notes consolidated tally (currently the authoritative "15 firm + 2 partial-obstruction" bullet at `L3/index.md:59`) to the D2 layer-intro-author, exactly as the count-ownership convention requires. The §Working-Notes tally will need a 2→3 partial-obstruction refresh, but that is correctly out-of-scope for this report and is flagged for the index-owner (report §Open-questions item 3).

3. **Forward-dependency note for the integrator (not a defect of this report).** The "single authoritative count tally" at `L3/index.md:59` and the §Semantics-overlay taxonomy at `L3/index.md:15` currently say "15 firm + 2 partial-obstruction" / "four firm obstruction shapes ... (b) and (c) are the two partial-obstruction operators". Once this `orthogonalize` row lands, those become stale (a third partial-obstruction operator exists). The report correctly does not edit them (D2's ownership); flagging here so the integrator confirms the D2 layer-intro-author report in this cycle actually performs the tally/taxonomy refresh — otherwise the index will carry an internally-inconsistent count after this row lands. This is a cross-report coordination dependency, surfaced for the integrator, not a repairable defect in this report.

---
verifies: ../REPORT.md
critiqued_at: 2026-05-31T235349Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T001316Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

## Repair

### Fixes attempted

- **Finding (Issue 1)**: Minor descriptor off-by-one on the test check-loop start line — `CYCLE.md` §Algebraic-laws law 1 (~line 342) and §Evidence (~line 563) describe "the per-rank orthogonality-check loop" / "inside the check loop 154-159"; on disk `test-orthog.cpp:154` is the leading comment `// Check full orthogonalization`, the `for` opens at `:155`, body runs `:155-159`, and the load-bearing `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` is at `:158`.
  - **Decision**: repaired (under citation-validity).
  - **Action**: Tightened the two prose descriptors in-place. Law 1 (CYCLE.md §Algebraic-laws, ~`:342`) now reads "the per-rank orthogonality-check loop — leading comment at `:154`, the `for` opens at `:155`, body runs `:155-159`". §Evidence (CYCLE.md, ~`:563`) now reads "inside the check loop (leading comment `:154`, `for` opens `:155`, body `:155-159`)". The load-bearing pinpoint `:158` is unchanged (it was correct), and the §Supporting-evidence citation `test-orthog.cpp:154-159` (anchor `CHECK_THAT` at `:158`, ~`:677`) is correct and in-range, so it was left untouched. Verified against `reference/palace/test/unit/test-orthog.cpp:154-160` directly: `:154` comment, `:155` `for`, `:158` `CHECK_THAT`, `:160` closing brace — confirms the tightening is exact. This is a mechanical citation-descriptor tightening; no content authored.

- **Finding (Issue 2)**: No firm-defect issues — affirmative note that citation-validity, partial-obstruction classification, variant-axis split, count-ownership discipline, fence parity, and high→low discipline all clear.
  - **Decision**: not-needed (informational, no defect).

- **Finding (Issue 3)**: Forward-dependency / cross-report coordination note for the integrator — the §Working-Notes tally (`L3/index.md:59`, "15 firm + 2 partial-obstruction") and the §Semantics-overlay taxonomy (`L3/index.md:15`) go stale once this `orthogonalize` row lands (a 3rd partial-obstruction operator). The report correctly does NOT edit them (D2 layer-intro-author owns the consolidated tally/taxonomy per the count-ownership convention).
  - **Decision**: not-needed / not-repairable (carried forward as an integrator coordination note — see Suggested resolution). Editing the §Working-Notes tally or §Semantics taxonomy from this repairer pass would be both a partition violation (those bullets are D2's, not D1's) and a content decision (the 2→3 refresh + taxonomy re-labeling), so it is explicitly out of repair authority.

### Unrepairable findings

None. Issue 1 was a mechanical descriptor fix (applied). Issues 2 and 3 are not defects in this report — Issue 2 is an affirmative no-defect note and Issue 3 is a cross-report coordination dependency owned by the D2 layer-intro-author report, carried forward to the integrator below.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

1. **Count-ownership coordination (carry-forward of Issue 3).** This report's `book/src/L3/index.md` edit is the dep-map `orthogonalize` row only (context-anchored on the on-disk `normalize` row), and it correctly defers the consolidated §Working-Notes tally (`L3/index.md:59`, "15 firm + 2 partial-obstruction") and the §Semantics-overlay taxonomy (`L3/index.md:15`) to the D2 layer-intro-author report. Once this row lands, `orthogonalize` is a **third** partial-obstruction operator, so confirm the D2 report in this cycle actually performs the 2→3 partial-obstruction tally refresh + the taxonomy re-label — otherwise `L3/index.md` will carry an internally-inconsistent count after the D1 row lands. This is the standard D1-row / D2-tally count-ownership partition; the report's §Open-questions item 3 already names it.

2. The two descriptor tightenings touched only CYCLE.md prose; the proposed `book/` `edit:` blocks (orthogonalize.md create, index.md row, SUMMARY.md line) are unaffected. Fence parity (3 balanced `edit:` blocks) and the anchored inserts are as the critic verified.
