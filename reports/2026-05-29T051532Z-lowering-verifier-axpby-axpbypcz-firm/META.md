---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T05:34:23Z
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
repaired_at: 2026-05-29T05:41:00Z
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

# META: verification of "Audit axpby-mutation-rotation + axpbypcz-mutation-rotation"

## Critique

### Checks run

**citation-validity (CRUX) — pass.** I independently `read_range`-verified every make-or-break
classification call and the two corpus censuses against Palace source. All three blocking
findings on `axpbypcz` are CORRECT:
- **slepc.cpp:1986** — `ctx->y1.AXPBYPCZ(ctx->gamma/ctx->sigma, ctx->y2, -ctx->gamma/ctx->sigma, ctx->x1, 0.0)`.
  The 5th (γ) argument is literal `0.0`; `-ctx->gamma/ctx->sigma` is the 4th/β slot. The receiver
  `ctx->y1` is `ComplexVector` (slepc.hpp:83). So this is the ComplexVector member form = **sub-pattern C,
  γ=0** — exactly as the audit reclassifies. The theme's "sub-pattern C, γ≠0 runtime" was wrong.
- **nleps.cpp:343-344** — `linalg::AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(), X[j].Imag(), 1.0, z.Real())`.
  `.Real()`/`.Imag()` return real `Vector&` (vector.hpp:62-63); scalars are `double`. The free-fn
  `AXPBYPCZ<VecType,ScalarType>` (vector.hpp:314-316) deduces `VecType=Vector, ScalarType=double` →
  hits the **real-real specialization at vector.cpp:746 (sub-pattern A)**, NOT the `double`-on-`ComplexVector`
  overload at vector.cpp:768 (sub-pattern D). γ=1.0 literal. Audit reclassification (D→A) is correct.
- **romoperator.cpp:188-189** — `V` is `const std::vector<Vector>&` (signature at romoperator.cpp:178-179);
  `u.Real()` is a `Vector&` half; γ=1.0. Same real-real dispatch → **sub-pattern A**, not D. The odd-`n`
  companion `linalg::AXPY(y(j).real(), V[j], u.Real())` at romoperator.cpp:193 corroborates (hits the
  real-`Vector` AXPY overload). Audit correct.

The corpus census is exact: `search_text "AXPBYPCZ\("` returns precisely the 13 sites the audit
enumerates (timeoperator{139,217,273}, arpack{772,787}, nleps{343,344,471,676,693}, slepc{1986},
romoperator{188,189}); every one passes literal γ in the 5th slot, all `0.0` EXCEPT the two real-real
sites (nleps:343-344, romoperator:188-189) at `1.0` — matching the audit's headline finding that
sub-pattern D is defined-not-used and the only observed γ≠0 path is sub-pattern A's real-real slow-path.
The axpby side also verifies: `linalg::AXPY\(` returns exactly the 5 sites the audit names
(nleps:536, romoperator:193-194, drivensolver:367,394), all `double` alpha → the complex-α free-fn
overload (vector.cpp:720-724) is genuinely defined-not-used. Spot-checked body anchors
(vector.cpp:701-712 real-real AXPY α==1 branch; vector.cpp:745-758 real-real AXPBYPCZ γ==0/γ≠0 split;
vector.cpp:388-435 ComplexVector AXPBYPCZ static body Write-vs-ReadWrite branch) all match the audit
verbatim. No drift in any sampled anchor.

**surface-or-evidence — pass.** This is an audit (retroactive-evidence-backfill shape), explicitly
permitted under the refinement-surface rule. The axpby verdict (fully-supported → FIRM, with the
status-flip + dep-map surface edit) carries the re-confirmed evidence; the axpbypcz verdict
(partially-supported → keep rough-in, GATED) is grounded in the three verified misclassifications +
the corpus census. Both verdicts are evidence-driven, not bare assertions.

**rotation-quality — pass.** Both themes are mutation→pure-function rotations (in-place `Add`/`AXPY`/
`AXPBYPCZ` kernels re-expressed as the L1 `axpy`/`axpbypcz` pure forms). The audit correctly assesses
semantic preservation: the γ==0 fast-path (`add(α,x,β,y,z)`) vs γ≠0 slow-path (`AXPBY; z.Add`) are
recognized as a load-bearing IEEE summation-order divergence, and the audit's correction #5 sharpens
this — because the two real-real γ=1.0 sites DO exercise the slow-path, the cross-branch non-law is a
live (not merely potential) reproduction concern. That is a substantive, correct strengthening of the
rotation's caveat, not a renaming.

**variant-axis-coverage — pass.** The sub-pattern taxonomy is the variant axis here (operand element-type
real/complex × scalar real/complex = A/B/C/D; orthogonal γ=0/γ≠0 syntactic axis). The audit applies it
correctly: it catches that the theme conflated the *operand-type* axis (real `Vector` halves vs
`ComplexVector`) with sub-pattern D, and that the γ-value axis was misread at slepc:1986. Post-correction,
every axis combination is accounted for: A observed (γ=0 and the two γ=1.0 sites), C observed (γ=0 only),
B and D both defined-not-used. No hidden branch.

**cross-reference-integrity — pass.** The proposed axpby `verified_against:` replacement and the
gated axpbypcz block are both fenced ```yaml. The axpby firm-proposal (status flip rough-in→firm +
dep-map row at index.md:18) is well-formed and the edit-target line numbers resolve (the current raw-YAML
block sits at axpby file lines 173-209; the `## Status` body at 224-229; dep-map row at index.md:18 —
all confirmed). The axpbypcz theme correctly stays rough-in with firming routed to cycle-022 under
explicit UNBLOCK-not-ENACT discipline. One minor refinement (non-blocking): the audit re-cites the current
file's combined `714-723` range as two ranges `714-718`/`720-724`, which is more precise (matches the
real-α vs complex-α overload boundaries) — an improvement, not a mismatch.

**edge-label-fidelity — pass.** Both themes are L1>L0 edges; the prose discusses exactly the L1→L0
lowering (L1 `axpy`/`axpbypcz` pure forms ↔ L0 `Add`/`AXPBYPCZ` kernels). No edge-label/prose mismatch.

**plan-kind-consistency — pass.** The split verdict is correctly shaped: axpby is proposed `firm` and its
content fully supports firm (no constructive sub-part, no negative-anchor reconstruction — purely
structural recognition rules, all verified). axpbypcz is correctly held at `rough-in` rather than
mislabeled `firm` or `partly-constructive` — the audit explicitly invokes the cycle-012 gated-promotion
discipline (the structure IS firm but the theme carries known-wrong content, so it cannot ship `firm`
as-written; the auditor unblocks with exact edits but does not enact). This is the right maturity call.

**skill-uptake-survey — warning.** The report's shape (citation-range re-verification of an inherited
`verified_against:` block, plus a refinement-surface audit) maps directly onto two available skills:
`verify-citation-range` (extended cycle-012 with an "Audit-report / inherited-citation sub-case" section,
which is *exactly* this report's situation) and `verify-refinement-surface`. The report performs work
fully consistent with both but does not name an explicit skill invocation anywhere. Telemetry-only,
non-blocking — surfacing for the meta-phase's skill-uptake tracking.

### Assessment of the SPLIT verdict (firm axpby / gate axpbypcz)

The split is **sound and well-calibrated** — neither too conservative nor too lax.
- **axpby FIRM is justified, not lax.** Every cited range re-verified line-exact; the only residual
  (exhaustive indexing of ~25 more axpy-shaped sites) is correctly framed as a completeness nicety, not a
  correctness gate — the recognition rules are firm and the cited set is illustrative. Firming is the
  right call.
- **Gating axpbypcz is justified, not over-conservative.** A theme that asserts observed γ≠0 and
  sub-pattern-D call sites when the corpus contains neither is making positive claims unsupported by any
  positive source site — that genuinely blocks `firm`. The auditor correctly declines to firm it and
  routes the exact corrections to cycle-022. This is not timidity; it is the correct application of "no
  positive claim without a positive site."

The three classification errors are real, independently confirmed, and correctly diagnosed. The audit is
the higher-quality artifact here: it caught substantive misclassifications that the original theme author
got backwards.

### Issues found

1. **[low severity — skill-uptake telemetry] No explicit skill invocation named.**
   CYCLE.md (whole report). The audit's work matches `verify-citation-range` (audit/inherited-citation
   sub-case) and `verify-refinement-surface` but neither is referenced. Non-blocking; surfaced for
   meta-phase skill-uptake tracking only.

2. **[low severity — cosmetic, already self-noted by the author] `## Status` edit line-range label.**
   CYCLE.md §"Proposed changes / Theme 1", the second axpby edit block says "current lines 226-229" for
   the `## Status` body. The `## Status` header is at line 224; body text is 226-229. The label points at
   the body correctly, but a repairer applying the edit should preserve the header at 224. Trivial.

3. **[informational — not a defect in this report, a flagged downstream item] axpby theme covers the
   `axpy` family, not the fused `AXPBY` form.**
   CYCLE.md §"Open questions / caveats" #3. The auditor correctly flags (does not firm-block on) that the
   theme named `axpby-mutation-rotation` actually covers the `axpy`-shaped family (α·x + y); the fused
   2-scalar `AXPBY` L0 surface (vector.cpp:315-360, 727-743) is a separate, uniformly-delegating lowering.
   This is an accurate observation and the right disposition (flag as OQ `axpby-theme-covers-axpy-family-naming`,
   firm the theme for what it covers). Recorded here so the integrator/meta-phase does not lose the
   naming-vs-scope nuance: firming this theme `firm` is correct for its actual content, but the dep-map
   "firm" label inherits a name that misdescribes scope. Not a blocker.

4. **[informational] MFEM `add(α,x,β,y,z)` alias-safety remains unverifiable from Palace source.**
   CYCLE.md §OQ #4 + applicability-condition #1 (timeoperator:139, z aliases x with γ=0). Correctly carried
   as an out-of-Palace-scope OQ per CLAUDE.md's "symbols resolving into MFEM are logged as open questions."
   Not a firm-blocker for either theme; the per-element value-correctness is self-evident, only the
   bit-level ordering is unverified. Noted for completeness.

## Repair

### Fixes attempted

- **Finding**: [skill-uptake telemetry] No explicit skill invocation named (`verify-citation-range` /
  `verify-refinement-surface` match the report's shape but neither is referenced).
  - **Decision**: not-needed
  - **Rationale**: Telemetry-only, non-blocking, already surfaced for the meta-phase's skill-uptake
    tracking by the critic. There is no mechanical fix — a repairer cannot retroactively author a skill
    invocation into a completed audit, and doing so would be substantive authoring, not a surgical fix.
    Correctly left for meta-phase consumption.

- **Finding**: [cosmetic, author-adjacent] The `## Status` edit line-range label in
  CYCLE.md §"Proposed changes / Theme 1" — the second axpby edit block says "current lines 226-229" for
  the `## Status` body; the critic noted the `## Status` header sits at line 224 and an applying
  integrator should preserve it.
  - **Decision**: not-needed
  - **Rationale**: Verified against the target file (`book/src/L1-L0/axpby-mutation-rotation.md`): the
    `## Status` header is at line 224, line 225 is blank, and the body text is lines 226-229. The report's
    edit-block label "current lines 226-229" therefore **already targets the body correctly and preserves
    the header at 224** — there is no off-by-N error in the label. The critic's note was a forward-looking
    instruction to the integrator (preserve the header), not a defect in the report's label. No edit to
    apply.

- **Finding** (informational, left as-is per dispatch instruction): axpby theme covers the `axpy` family,
  not the fused `AXPBY` form (critique §"Issues found" #3); and MFEM `add` alias-safety OQ (#4).
  - **Decision**: not-needed
  - **Rationale**: These are correctly-surfaced auditor observations (OQs `axpby-theme-covers-axpy-family-naming`
    and the MFEM-scope alias-safety carry), explicitly flagged by the critic as NOT defects in this report.
    The substance (axpby→firm; axpbypcz gated-to-cycle-022) is sound. Nothing to repair.

### Unrepairable findings

None. No finding required substantive authoring or exceeded repair authority — the two flagged items are
telemetry and a non-defect label note, and the informational items are correctly-surfaced observations.

## Suggested resolution

`ready`. This is a strong, self-consistent audit: 7 pass + 1 telemetry-only warning, with the critic
independently `read_range`-confirming all three `axpbypcz` classification errors and endorsing the SPLIT
verdict as well-calibrated. No mechanical repair was warranted (the one cosmetic candidate turned out to
be a correct label, not an error).

Notes for the integrator:
- **axpby-mutation-rotation** is proposed `firm` with a full re-audited `verified_against:` block, a
  `## Status` flip (rough-in→firm), and the `book/src/L1-L0/index.md:18` dep-map row update. All edit-block
  line ranges resolve against the current files (verified: status body at 226-229, header preserved at 224).
- **axpbypcz-mutation-rotation** stays `rough-in`, GATED — apply NO status flip and leave its dep-map row
  unchanged. The auditor UNBLOCKS (exact corrections (1)-(6) specified) but does not ENACT, per the
  cycle-012 gated-promotion discipline. Firming is routed to a cycle-022 follow-up dispatch under plan item
  `axpbypcz-mutation-rotation-callsite-correction-and-firm` (CYCLE.md OQ #1).
- The BLAS-1 L1>L0 floor (`blas1-l1-l0-lowering-theme-gap`) reaches 7/8 with this report; it closes on the
  one corrected-then-firmed axpbypcz dispatch.
