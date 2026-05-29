---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T024500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: pass
repaired_at: 2026-05-29T030000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Formalize orthogonalize at L2" (stub→firm)

## Critique

### Checks run

**citation-validity — warning.** I independently read every cited L0 range via `palace-codemap read_range` (not trusting the producer's "Self-verified" annotations, per the verify-citation-range Audit-report sub-case). The core source citations are sound: `orthog.hpp:18-90` (header contract, `IdentityInnerProduct`, `OrthogonalizeColumnMGS`, `OrthogonalizeColumnCGS` incl. the `refine` branch) all match; `iterative.cpp:308-325` (`OrthogonalizeIteration` switch), `:630-632` (GMRES consumer), `:809-811` (FGMRES consumer) all match exactly; `romoperator.cpp:51-66` (ROM wrapper), `:224-226` (canonical-hook consumer), `:631-646` (B-weighted lambda hook) all match; the no-`dot_op`-passed→`IdentityInnerProduct` default claim is confirmed from the actual call sites. The six `test-orthog.cpp` TEST_CASE boundaries (`:99/:123/:164/:234/:276/:333`) verify exactly via `search_text`, and the weighted test (`:276`) genuinely asserts B-weighted orthogonality (`⟨residual, V[i]⟩_B = 0` via `W.Mult` + `linalg::Dot` + `CHECK_THAT(..., WithinAbs(0.0,1e-12))`), backing law 7. The warning is for **two imprecise spot-line pointers** (content correct, line numbers off):
  - the orthogonality-assertion micro-citation is wrong by 2: `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` is at **line 156** (not the claimed 158); the check loop is **153–157** (not 154–159); the TEST_CASE closes at **159** (not 160). The cited *range* `:123-160` still contains the asserted content, so the substance holds — but the precise line claims in Algebraic-laws law 1 and the `:123-160` Evidence bullet are inaccurate.
  - the CGS `m == 0` early-return is cited as `orthog.hpp:62-64` (Signature, law 3, Evidence); the `if (m == 0)` guard is actually at **line 61** (`return;` at 63, brace at 64) — off by 1 on the start.
  - the `orthog.hpp:22` micro-cite for the no-normalise sentence is one line low (the sentence "...does not normalize the output vectors!" is at **line 21**); the `:18-23` range bullet is correct.
  These are all within-range nits, not fabrications — every claim's content is supported by the cited file region.

**surface-or-evidence — pass.** This is a stub→firm promotion (surface IS the body replacement) carrying full L0 + test grounding, not invention. Every semantic claim traces to a verified source/test site. The "exact arithmetic" laws (4, 5, 6) are standard Gram-Schmidt facts explicitly fenced behind the exact-arithmetic precondition with the floating-point failures recorded as non-laws — consistent with the load-bearing-numerical-trick discipline. CGS2's "twice is enough" is attributed (Kahan/Parlett) as literature, not claimed from a Palace site, which is honest.

**rotation-quality — pass.** The L2 form is strictly more abstract than the L1 leaf along the right axis: L1 is the opaque single-dispatch leaf with the GS variant as a parameter and the collective shape recorded as a *property*; L2 names the `project ▷ subtract` composition and **promotes the per-variant primitive-sequence (the collective-shape residual axis `m×1 / 1×m / 2×m`) to first-class content**. This is genuine fusion-rotation (de-fusing the single dispatch into the canonical composition while retaining the synchronisation pattern as a disclosed residual), not a 1:1 rename. High→low discipline is respected: semantics/laws are stated in L2 composition vocabulary referencing L1 leaves as constituents; the lowering is correctly deferred to a forthcoming L2>L1 theme rather than defining the L2 entry in L1-primitive terms.

**variant-axis-coverage — pass.** Two axes closed and matching the firm L1 leaf (gs_orthog `{MGS,CGS,CGS2}` residual-axis disclosure; `dot` hook `{canonical, B-weighted}` parametric), element-type fully parametric and correctly absorbed by `dot`, Householder explicitly scoped out with both the structural reason (reflector-sequence state, `[reflect_apply, reflect_zero]` chain) and the policy reason (no Palace L0 path). The L0 confirms the report's chain framing is the *faithful* one — see the skill-friction note under skill-uptake-survey: the report's `CGS = [dot×m, allreduce, axpy×m]` / `CGS2 = [CGS]×2` (no threshold, `dH` pass-local) matches `orthog.hpp:65-89` exactly (the `refine` branch is unconditional, reads no threshold scalar).

**cross-reference-integrity — pass.** All `[link]` targets resolve: `L1/orthogonalize.md`, `L1/dot.md`, `L1/axpy.md`, `L2/linear_combination.md`, `L2/krylov-step.md`, `L2/inner_product.md`, `concepts/{orthogonalization,variant-absorption,sequential-obstruction}.md` all exist. The forward-reference to `L2-L1/orthogonalize-composition-lowering` is correctly kept as **plain text** (verified the file does NOT exist; the L2-L1 dir holds only chebyshev/inner-product-fold/linear-combination-fold themes), so it will not break linkcheck2. The `krylov-step` §"L2 vs L1 distinction" forecast quote is **verbatim accurate** (krylov-step.md:132). `variant-absorption.md:131` is a precise anchor for the residual-axis + Householder scope-out. The dep-map ADD claim is correct (no existing `orthogonalize` row; insert after `inner_product` at L2/index.md:26) and the SUMMARY replace-target (`- [orthogonalize (stub)](./L2/orthogonalize.md)` at SUMMARY.md:41) is exact.

**edge-label-fidelity — pass.** Not a lowering-theme report (no L_{n+1}→L_n edge label). The dep-map row status flip stub→`firm` matches the body's firmness state, and the proposed row's labels (L1 leaf firm, dot/axpy firm, inner_product "rough-in", krylov-step consumer) all match the verified artifact state. The deferred lowering theme is labelled "forthcoming" consistently.

**plan-kind-consistency — warning.** Declared kind is a firm L2 first-class composition; the content shape matches a firm entry (signature, semantics, 7 laws + 5 non-laws, dependencies, variant axes, evidence) — no rough-in placeholders in the body. The warning is **structural**, on the proposed-changes blocks: the first ` ```edit:book/src/L2/orthogonalize.md ` fence (CYCLE.md line 42) opens the replacement body at line 43 ("# orthogonalize") but **has no visible closing ` ``` ` fence** before "## Context" at line 58 — the entire Context/Signature/Semantics/Laws/etc. narrative appears to fall inside the open edit block, or the closing fence is missing. By contrast the two trailing blocks (`edit:book/src/L2/index.md`, `edit:book/src/SUMMARY.md`) are well-formed. An integrator parsing edit-fences literally would either (a) write the whole report body into `L2/orthogonalize.md`, or (b) fail to find the block terminus. The intended firm-body content is clearly lines 43–56 (the paragraph ending "...basis-extension all consume."), but that boundary is not marked. This needs the repairer to close the fence at the correct line.

**skill-uptake-survey — pass (telemetry).** The producer references `classify-variant-axis` (invokes its output contract for the Variant-axes section) and cites its `gs_orthog` example block as an input. Implicit uptake of the verify-citation-range discipline is visible via the per-bullet "Self-verified via read_range this dispatch" annotations. No blocking issue. **Drive-by skill-friction signal** (surfaced, not blocking): the `classify-variant-axis` SKILL's own `gs_orthog` worked example (SKILL.md:64-68) is **stale/inaccurate vs. the L0** — it lists `CGS = [dot×m, allreduce_sum, gemv_basis]` with load-bearing `gemv_basis (rank-1 fused)`, `CGS2 = [CGS chain]×2 + [axpy_scalar]` with a `refine_threshold` scalar "captured in setup." The actual `OrthogonalizeColumnCGS` (`orthog.hpp:65-89`) uses plain `w.Add` (axpy), no fused gemv, and the `refine` branch is **unconditional with no threshold scalar**. The report correctly diverges from the SKILL example toward the faithful L0 shape; consider filing the SKILL-example drift to `problems/` (kind: skill-friction) so the example is corrected, since future producers may copy it.

### Issues found

1. **[citation-validity, warning] Orthogonality-assertion micro-citation off by 2.** CYCLE.md Algebraic-laws law 1 (~line 220-221) and Evidence bullet `test-orthog.cpp:123-160` (~line 448-452): claims `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` at line 158, loop 154-159, TEST_CASE closes 160. Verified actual: assertion at **156**, loop **153-157**, TEST_CASE closes **159**. Content correct, line pointers wrong. Repair = renumber to 156 / 153-157 / 159 (cited range `:123-160` overshoots the close by 1; `:123-159` is exact).

2. **[citation-validity, warning] `m == 0` early-return cited `orthog.hpp:62-64`, actual guard at 61.** CYCLE.md Signature (~line 144), law 3 (~line 230), Evidence bullet (~line 413): `if (m == 0)` is at **line 61** (return at 63, brace at 64). Off-by-one on the start.

3. **[citation-validity, warning] No-normalise sentence micro-cited `orthog.hpp:22`, actual at 21.** CYCLE.md Semantics (~line 198) and Evidence `:18-23` bullet quote the "...does not normalize the output vectors!" sentence as `:22`; it is at **line 21**. The `:18-23` range bullet is fine.

4. **[plan-kind-consistency, warning] First proposed-changes edit block has no closing fence.** CYCLE.md line 42 opens ` ```edit:book/src/L2/orthogonalize.md `; the intended replacement body is lines 43–56, but there is no ` ``` ` before "## Context" (line 58). The block boundary is ambiguous for the integrator's edit-fence parser. The two later edit blocks (index.md, SUMMARY.md) are well-formed. Repair = insert the closing fence after the line ending "...basis-extension all consume." (line 56).

5. **[skill-uptake-survey, drive-by/non-blocking] `classify-variant-axis` SKILL gs_orthog example is stale vs L0.** SKILL.md:64-68 describes CGS/CGS2 with `gemv_basis`, `axpy_scalar`, and a `refine_threshold` scalar that the actual `OrthogonalizeColumnCGS` (`orthog.hpp:65-89`) does not have (plain `w.Add`, unconditional `refine`, no threshold). The report correctly does not propagate the error. Candidate for a `problems/` skill-friction filing so the example is corrected; out of this report's repair scope.

## Repair

### Fixes attempted

- **Finding** ([plan-kind-consistency] missing closing fence): the first proposed-changes block ` ```edit:book/src/L2/orthogonalize.md ` (CYCLE.md line 42) opened the firm-body replacement at line 43 but had no closing ` ``` ` before "## Context" — the boundary that the integrator's edit-fence parser needs was unmarked, so the parser would either swallow the whole report body into `L2/orthogonalize.md` or fail to find the block terminus.
  - **Decision**: repaired.
  - **Action**: inserted a closing ` ``` ` fence in CYCLE.md immediately after the intended body line ("...eigenmode-ROM basis-extension all consume.", was line 56) and before the blank line preceding "## Context". The block now opens at `edit:book/src/L2/orthogonalize.md`, contains the single "# orthogonalize" intro paragraph (the intended firm body), and closes cleanly. The two later edit blocks (`index.md`, `SUMMARY.md`) were already well-formed and untouched. Purely structural; no content authored.

- **Finding** ([citation-validity] three off-by-small spot-line pointers): critic flagged (a) the orthogonality assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` cited at `test-orthog.cpp:158`, claimed actual 156, loop claimed 153-157, TEST_CASE close claimed 159; (b) the `m == 0` guard cited `orthog.hpp:62-64`, claimed actual guard at 61; (c) the no-normalise sentence cited `orthog.hpp:22`, claimed actual 21.
  - **Decision**: not-needed (the existing citations are already correct; no edit applied).
  - **Rationale**: I independently re-read all three ranges via `palace-codemap read_range` + `search_text` against `reference/palace`. The source confirms the CYCLE.md's **existing** line pointers are accurate, and the critic's proposed "corrections" are the inaccurate ones (the critic appears to have read against a 1–2-line-shifted offset):
    - `search_text` for `CHECK_THAT.*WithinAbs\(0\.0, 1e-12\)` in `test/unit/test-orthog.cpp` returns the orthogonality assertion at **line 158** (matching CYCLE.md), not 156. `read_range 154-161`: comment at 154, `for` header 155, `{` 156, `auto dot = ...` 157, `CHECK_THAT(dot, ...)` **158**, loop-close `}` 159, TEST_CASE-close `}` **160**. So `:123-160` is exact and "158 / loop 154-159" stand. (Note the critic's path `palace/test/unit/...` is also wrong; the file is at `test/unit/test-orthog.cpp`.)
    - `read_range orthog.hpp 59-66`: `MFEM_ASSERT(...)` at **61**, `if (m == 0)` at **62**, `{` 63, `return;` 64, `}` 65. The guard is at 62, so `:62-64` correctly brackets guard→return; "guard at 61" is the MFEM_ASSERT line.
    - `read_range orthog.hpp 20-24`: `//` 21, `// Assumes ... does not normalize the output vectors!` at **22**, `// If done in a loop...` 23. So `:22` is exact; the sentence is not at 21.
  - Applying the critic's renumbering would have **corrupted three correct citations**. Per repair discipline (mechanical fixes only; do not introduce errors), the correct outcome is no edit. The critic's `citation-validity: warning` check value is left untouched (not my authority to override), but the repair is `not-needed` and the disagreement is recorded for the integrator/meta-phase below.

- **Finding** ([skill-uptake-survey, drive-by] `classify-variant-axis` SKILL.md:64-68 `gs_orthog` worked example stale vs L0): the SKILL example lists `gemv_basis`, `axpy_scalar`, and a `refine_threshold` scalar that `OrthogonalizeColumnCGS` (`orthog.hpp:65-89`) does not have (plain `w.Add`, unconditional `refine`, no threshold).
  - **Decision**: unrepairable (out of scope).
  - **Rationale**: this concerns a `skills/` artifact, not this report. Editing skills is meta-phase authority (the repairer must not modify `skills/`), and correcting a worked example is substantive authoring, not a mechanical fix to this report. The report itself correctly diverges from the stale SKILL example toward the faithful L0 shape, so this is not a defect in the report. Surfaced for meta-phase below.

### Unrepairable findings

- **`classify-variant-axis` SKILL gs_orthog worked-example drift** (SKILL.md:64-68 vs `orthog.hpp:65-89`). Routed to: meta-phase (skill-correction authority). This is a skill-friction signal, not a report defect; appended to `scaffolding/skill-candidates.md` for meta-phase pickup so the example is corrected before future producers copy it. No follow-up agent on *this report* is needed for it.

## Suggested resolution

`overall_status: ready`. The one actionable, in-scope finding (missing closing fence on the first proposed-changes block) is repaired — all three edit blocks now parse cleanly, so `integrator-per-report` can apply the firm body to `book/src/L2/orthogonalize.md`, ADD the dep-map row to `L2/index.md` (after the `inner_product` rough-in row), and replace the SUMMARY stub line.

Integrator note: the three `citation-validity` findings are `not-needed` because the report's existing line pointers are correct on re-verification against `reference/palace` — do NOT apply the critic's renumbering (it would corrupt accurate citations). The critic's per-source content verification (the substance behind every claim) stands; only its spot-line offsets were shifted.

Meta-phase note: the `classify-variant-axis` SKILL.md:64-68 `gs_orthog` example needs correcting (filed to skill-candidates). Separately, the critic's citation-line offsets being systematically shifted on this report (3-of-3 spot pointers, all by 1–2 lines, all in the same direction the critic claimed the report was wrong) is itself a possible critic-side line-offset-drift signal worth a friction-window glance if it recurs.
