---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T041500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: warning
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T035432Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of "Formalize orthogonalize at L1"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing L0 claim was checked against source. `palace/linalg/orthog.hpp` is 93 lines and there is **no** `orthog.cpp` — the "header-only inline, no .cpp" claim is confirmed (`ls` returns ENOENT for `orthog.cpp`). The scope-contract citation `orthog.hpp:18-23` is exact: lines 22-23 read "Assumes that the input vectors are normalized, but does not normalize the output vectors! If done in a loop, normalization has to be managed by hand!" — directly supporting the normalization-excluded design. `OrthogonalizeColumnMGS` body (`H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm); w.Add(-H[j], V[j])`) is at 46-52; `OrthogonalizeColumnCGS` with the `m==0` early return, single `GlobalSum(m, ...)`, and the `refine`/CGS2 second pass is at 57-89; the "Note order is important for complex vectors" comment is at line 48 (cited exactly). The dispatch wrapper `OrthogonalizeIteration` switch over MGS/CGS/CGS2 (CGS2 = `OrthogonalizeColumnCGS(..., true)`) is confirmed at `iterative.cpp:307-325` (report cites 308-325, omitting only the template-parameter line 307 — in tolerance). GMRES/FGMRES call sites at `iterative.cpp:630, 809` are exact, each immediately followed by `Hj[j+1] = Norml2(...)` and `w *= 1.0/Hj[j+1]` (lines 631-632, 810-811) — independently confirming normalization is the caller's step. ROM citations `romoperator.cpp:51-66` (`OrthogonalizeColumn` wrapper), `:224`, `:633` (the B-weighted lambda `dot_op`) all resolve. The OQ slug exists (`open-questions.md:1824`). The slice/arnoldi_step "pending lift" anchors resolve. Minor line-range looseness exists on the test and header sub-citations (catalogued under Issues, severity low) but no citation is out-of-range or unsupported.

**surface-or-evidence — pass.** This is a firm L1 operator entry (a *new surface* creation, not a refinement of an existing operator/theme). It creates `book/src/L1/orthogonalize.md` with full operator text, and carries empirical rotation evidence (the `test-orthog.cpp` parametric suite witnessing law 1 substitutability across all three variants). New-surface + evidence — not a pure rotation_claim backfill. Passes.

**rotation-quality — pass.** The L1 form is strictly more abstract than the L0 form: the mutation rotation drops both destination buffers (`w` overwritten in place, `H` written through a raw pointer) from the signature, drops `comm`, and replaces the per-`j` interleaved-mutation idiom with a pure `(w', H) = orthogonalize(w, V, variant)`. This is genuine state-hiding (buffer ownership + in-place overwrite → fresh-pair return), not a 1:1 rename. The two destination-buffer arguments and the MPI collective are correctly pushed down to the (not-yet-authored) L1>L0 theme. Passes. (See the variant-axis check for a related absorption-level concern that does not change this verdict.)

**variant-axis-coverage — warning.** The two axes the report covers are real: `gs_orthog ∈ {MGS, CGS, CGS2}` (the L0 dispatch, confirmed in `OrthogonalizeIteration`) and the `dot_op` inner-product hook (`IdentityInnerProduct` vs B-weighted, confirmed via the `InnerProductHelper` template at `orthog.hpp:39-43, 55-59` and the ROM lambda at `romoperator.cpp:633`). The element-type axis (real/complex) is correctly noted as fully parametric and absorbed by `dot`. **However:** the governing concept page `variant-absorption.md:131` names a **fourth** orthogonalization variant — Householder — that threads a reflector sequence and breaks level-(c) absorption. Palace's L0 implements only MGS/CGS/CGS2 (the header has exactly two functions), so Householder is genuinely out of scope, but the report does not explicitly scope it out. Per the variant-axis-coverage check (cover each combination OR explicitly scope out), the Householder member is a known axis value left silently uncovered. A one-line "Householder is not present in Palace's L0 (out of scope)" closes this. Warning, not fail — the omission is defensible and the unimplemented-component policy supports the scope-out.

**cross-reference-integrity — warning.** All `[link]` targets resolve: `L1/{dot,axpy,nrm2,scal,ksp_solve,matrix-weighted-norm}.md`, `L2/krylov-step.md`, `concepts/{orthogonalization,sequential-obstruction,variant-absorption}.md` all exist. The `sequential-obstruction.md:37-48` range is exact ("Example: MGS as sequential-obstruction"). The index.md / SUMMARY.md edit preconditions hold (`**Firm (8)**` at index L29; `ksp_solve` is the last firm bullet at L38, so "append after ksp_solve" correctly lands inside the Firm cohort; the `bilinear-form` dep-map row at L69 is the last row; SUMMARY's `bilinear-form` line at L52 is the last L1 entry). **The flagged concerns:** (1) The report repeatedly characterizes the `gs_orthog` axis as "**level-(b)** absorption" (Semantics §, Variant-axes §). But `variant-absorption.md:131` states MGS/CGS/CGS2 "absorb at **all three levels** under residual-axis disclosure for the L2 collective shape." So the report *under-claims* the absorption level relative to the governing concept — it should read "(a)/(b)/(c) under residual-axis disclosure" (or justify the narrower (b)-only claim). This is a factual mismatch with the cross-referenced concept, not just phrasing. (2) The contradiction the dispatch flagged is **confirmed and correctly handled** — see edge/contradiction note below. Warning driven by concern (1).

**edge-label-fidelity — pass (n/a-shaped).** This is an L1 operator entry, not a lowering theme carrying an `L_{n+1}→L_n` edge label. The L1-vs-L0 distinction prose (operator content §"L1 vs L0 distinction") discusses the L1↔L0 boundary it claims to, and defers the L1>L0 rewrite to a future theme. No mismatched edge label. Passes.

**plan-kind-consistency — pass.** Declared kind is firm L1 operator. Content shape matches: complete signature with named-axis shape contract, six algebraic laws plus an explicit non-laws block, dependencies, two variant axes, full L0 evidence read, and a firm justification grounded in dedicated parametric test coverage (real/complex/B-weighted + empty-basis + substitutability `⟨w',V[i]⟩≈0`). No rough-in placeholders in a firm entry. The firmness bar matches the cited BLAS-1 floor operators. Passes.

**skill-uptake-survey — warning.** The proposal's shape implies two relevant skills. `classify-variant-axis` is directly applicable (the report makes a two-axis classification call and an implicit Householder scope-out decision; `variant-absorption.md:140` explicitly says this skill makes the residual-axis-vs-sibling-slice call) — its invocation is not referenced. `verify-citation-range` is applicable given the volume of L0/test citations and the slice's stale-citation history the report corrected — also not referenced. The frontmatter notes "L0 (verified via MCP codemap)" which is evidence of localization tooling but not the citation-range skill. Telemetry-only; non-blocking.

### Issues found

1. **Absorption-level under-claim contradicts the governing concept page.** `book/src/L1/orthogonalize.md` Semantics § ("per `variant-absorption` this is level-(b) absorption") and Variant-axes § ("Level-(b) variant-absorption: inspected once at dispatch, never per-column"). `concepts/variant-absorption.md:131` states MGS/CGS/CGS2 "absorb at **all three levels** (a/b/c) under residual-axis disclosure for the L2 collective shape." The report's "(b)"-only label is narrower than — and inconsistent with — the cited concept. Severity: medium (a factual cross-reference mismatch on the entry's own absorption claim; candidate to correct to "(a)/(b)/(c) under residual-axis disclosure" or justify the narrowing).

2. **Householder axis value not explicitly scoped out.** `book/src/L1/orthogonalize.md` Variant-axes § scopes `gs_orthog` as `{MGS, CGS, CGS2}`. `variant-absorption.md:131` names Householder as a fourth orthogonalization variant (reflector-sequence state, breaks level-(c)). Palace's L0 has no Householder path, so the scope-out is correct, but it is silent rather than explicit. Severity: low (add a one-line out-of-scope note; the unimplemented-component policy backs the scope-out).

3. **Concept-page coefficient/normalization contradiction — confirmed, correctly handled, but the concept page is also internally inconsistent.** The dispatch's flag is verified: `concepts/orthogonalization.md:3` defines the output coefficient vector as `h = (h_0, …, h_{j+1})` "with `h_{j+1} = ‖w'‖`", folding the normalization sub-diagonal into the coefficient vector — which contradicts the report's length-`m` `H` with `‖w'‖` as the caller's `nrm2` step. The report correctly (a) declares this entry authoritative on the boundary (operator content §Context, §Evidence L347-350, §Open-questions L391-395), (b) does NOT edit the concept page (respecting one-operator discipline + layer-intro-author authority), and (c) cites the call-site evidence (`iterative.cpp:631-632, 810-811`: `Hj[j+1] = Norml2(...); w *= 1/Hj[j+1]`) that the normalization is the caller's. Additional observation for the future concept-page refresh: `orthogonalization.md` is **internally** inconsistent — its first concept block (L3) folds in `h_{j+1}=‖w'‖`, while its second stacked concept block (L29-30) defines `h_{0..j-1}` and `w' = w − Σ h_i v_i` with **no** normalization fold-in. The report flags only the L3 version. Severity: low (the report's handling is correct; this is an enrichment of the already-flagged caveat for whoever does the concept refresh).

4. **Minor citation-range looseness (low).** Several sub-citations bracket their target slightly loosely (no out-of-range, no unsupported claim):
   - `orthog.hpp:25-36` for `IdentityInnerProduct` + concept comment — the struct closes at line 37 (range clips the closing `};`).
   - `orthog.hpp:41-52` for `OrthogonalizeColumnMGS` — function template opens at 39, body closes at 53 (range starts at the function-name line and clips the closing brace).
   - `orthog.hpp:54-90` for `OrthogonalizeColumnCGS` — function spans 55-89 (line 54 blank, 90 blank).
   - `test-orthog.cpp:123-156` and the `:147-156` law-1 substitutability witness — the actual orthogonality assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` lands at line 158, just past 156. The cited range clips the assertion line itself.
   - `test-orthog.cpp:70-95` for the `orthogonalize_wrapper` GENERATE harness — the wrapper class spans 72-97 (range starts on the blank/comment lines and clips the closing `};`).
   Severity: low (cosmetic ±1-3 line tightening; the cited content is present and supports each claim).

5. **`skill-uptake-survey` telemetry (low/non-blocking).** No reference to `classify-variant-axis` (despite making a variant-axis classification + scope-out call) or `verify-citation-range` (despite correcting the slice's stale citations and carrying a high citation volume). Frontmatter's "verified via MCP codemap" indicates localization tooling use but not the citation-range skill. Surfaces telemetry only.

## Repair

### Fixes attempted

- **Finding (issue 1, medium)**: Absorption-level under-claim — the entry labels `gs_orthog` as "level-(b)" absorption, but `concepts/variant-absorption.md:131` states MGS/CGS/CGS2 absorb at **all three levels (a/b/c) under residual-axis disclosure** for the L2 collective shape.
  - **Decision**: repaired.
  - **Action**: Re-read `variant-absorption.md:120-192` to confirm the (a)/(b)/(c) definitions and the canonical-example line at `:131`. Rewrote the absorption claim in `CYCLE.md` (the embedded `book/src/L1/orthogonalize.md` content) at three sites: §Semantics ("per `variant-absorption` … all three levels (a/b/c) under residual-axis disclosure" with the per-level breakdown — (a) invariant unifies via law 1, (b) inspected once at dispatch, (c) same `[dot, axpy]` chain; residual = per-variant collective shape m×1/1×m/2×m); §Variant-axes (`gs_orthog` bullet, same correction with `:131` citation); and §Dependencies reverse-direction note (L2 krylov-step now references orthogonalization as an "all-three-level-absorbed (residual-axis-disclosed)" component rather than "level-(b)-absorbed"). This is a mechanical alignment to the governing concept page, not a content re-judgment — the (b)-only label was a typo-class under-claim contradicted by the cited concept.

- **Finding (issue 2, low)**: Householder axis value (a 4th orthogonalization variant named at `variant-absorption.md:131`) silently uncovered.
  - **Decision**: repaired.
  - **Action**: Added an explicit scope-out note to `CYCLE.md` §Variant-axes (`gs_orthog` bullet): Householder threads a reflector sequence (different state, `[reflect_apply, reflect_zero]` chain, breaks level-(c)); Palace's L0 has no Householder path (`orthog.hpp` defines exactly `OrthogonalizeColumnMGS` / `OrthogonalizeColumnCGS`), so it is out of scope per the unimplemented-component policy. The axis enumeration was clearly available from the concept page, so this is a mechanical scope-out closure (the "cover OR explicitly scope out" alternative), not substantive authoring.

- **Finding (issue 3, low)**: `concepts/orthogonalization.md` internal inconsistency (its L3 block folds `h_{j+1}=‖w'‖` into the coefficient vector; its L29-30 block does not).
  - **Decision**: not-needed (informational).
  - **Rationale**: This is a defect in the **concept page** (artifact), not the report, and the critic already noted the report handles the boundary correctly (declares itself authoritative, does not edit the concept page, cites the call-site evidence). The report's existing §Open-questions caveat (`CYCLE.md` L391-395) already flags the drift for a future concept refresh. No report edit warranted; concept-page repair is layer-intro-author territory, outside repair authority and outside this report.

- **Finding (issue 4, low)**: Citation sub-range clips (header struct/function closing braces; test law-1 assertion past the cited range).
  - **Decision**: repaired.
  - **Action**: Verified each range against source via MCP codemap (`read_range`) and tightened in `CYCLE.md` (Evidence §, inline citations, frontmatter inputs, Status §):
    - `orthog.hpp:25-36` → `25-37` (struct `IdentityInnerProduct` closes `};` at 37; also fixed the inline copy in §Variant-axes).
    - `orthog.hpp:41-52` → `41-53` (MGS function-name line through closing brace at 53).
    - `orthog.hpp:54-90` → `57-89` (CGS spans function-name line 57 through closing brace 89; 54 and 90 blank).
    - `test-orthog.cpp:70-95` → `71-96` (wrapper class: comment at 71 through closing `};` at 96).
    - `test-orthog.cpp:123-156` → `123-160` (full parametric-real TEST_CASE; closes at 160).
    - `test-orthog.cpp:147-156` (law-1 witness) → `154-159` (the orthogonality-check loop; the `⟨w',V[i]⟩≈0` assertion is at line 158, which the old range clipped).
    - Status § `99-156` → `99-160`; frontmatter inputs `70-156` → `71-160`.

- **Finding (issue 5, low)**: `skill-uptake-survey` telemetry — no reference to `classify-variant-axis` / `verify-citation-range`.
  - **Decision**: not-needed (informational/telemetry).
  - **Rationale**: Telemetry-only; the critic marked it non-blocking. Skill-uptake is a reporting concern, not a content defect to repair surgically.

### Unrepairable findings

None. All blocking and warning findings were either mechanically repaired (issues 1, 2, 4) or are informational/telemetry (issues 3, 5). Issue 3 is a concept-page (artifact) defect already correctly handled by the report and flagged in its Open-questions; it routes to a future layer-intro-author concept refresh, not to a report revision.

## Suggested resolution

`overall_status: pass-after-repair`. The report is ready for the integrator. Two informational items survive for downstream attention (neither blocks application):

- **Concept-page refresh** (issue 3): `concepts/orthogonalization.md` is internally inconsistent on the coefficient/normalisation fold-in (L3 block vs L29-30 block). Route to a future `layer-intro-author` dispatch; the report's Open-questions caveat already carries the flag, and the firm L1 entry is authoritative on the boundary in the meantime.
- **Skill-uptake telemetry** (issue 5): no `classify-variant-axis` / `verify-citation-range` invocation recorded. Telemetry only; meta-phase aggregation, not per-report action.
