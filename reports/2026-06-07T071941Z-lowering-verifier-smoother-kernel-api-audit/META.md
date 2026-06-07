---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T074500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-07T075500Z
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

# META: verification of "Audit multigrid-relaxation-smoother realizes-kernel-api triangular-solve-obstruction"

## Critique

### Checks run

**citation-validity — warning.** I independently re-verified the two load-bearing
off-by-one corrections this audit proposes, NOT from a codemap `read_range` (per the
documented +1-brace-drift hazard) but via `citecheck --anchor` plus a direct on-disk
`Read` of `distrelaxation.cpp:98-155`:
- DRIFT-1: `for (int it = 0; it < pc_it; it++)` is on line **102** (line 103 is the
  opening `{`). `citecheck --anchor 'for (int it'` ⇒ `anchor at line 102`. The report's
  `:103`→`:102` correction is **correct**.
- DRIFT-2: `MultTranspose2`'s closing brace is on line **151** (line 152 is blank;
  template instantiations at 153-154). The report's `:121-152`→`:121-151` correction is
  **correct**.

The four chapter citation sites the corrections target (chapter lines 223, 231, 310, 316)
were confirmed on disk to contain the exact stale text the proposed edits match. The
correspondence anchors `chebyshev.hpp:82` (`polynomial`) and `amg.cpp:24` (`relax_type`)
both citecheck-ok at the cited lines. The `verified_against:` block's 8 citations are all
in-range / on-disk-correct. **However**, a mechanical `citecheck --scan` of the report
surfaced **two over-range provenance citations**: `distrelaxation.cpp:1-157` (file has
**156** lines) and `distrelaxation.hpp:1-93` (file has **92** lines) — each cited END is
+1 past EOF. These appear in the report frontmatter `inputs:` (lines 9-10) and the
Supporting-evidence section (lines 368, 371) as "full file read" provenance ranges, NOT in
any proposed-change citation, and the report's own body correctly states the substantive
anchors end at 151/154. The defect is confined to two whole-file provenance ranges; it does
not touch the proposed edits or the verdict. Marked **warning** (a real bounds drift, low
severity — provenance-only, not load-bearing).

**surface-or-evidence — pass.** This is an audit report, not a refinement of operator/theme
surface; the proposed changes are a retroactive-evidence `verified_against:` backfill plus
two citation carry-forward corrections. Pure retroactive-evidence framing is explicitly
allowed, so the rotation_claim-without-surface failure mode does not apply. Record-definition
sub-check: the audit references the `DistRelaxSmoother[N,M]` record but it is *defined* in
the impl chapter under audit (the record-definition anchors `distrelaxation.hpp:34-51` are
verified here), not newly named-by-use in this report — no missing definition home.

**rotation-quality — pass (not applicable to audit-report kind).** An audit asserts no new
algebraic/structural rotation of its own; it verifies an existing impl↔api correspondence.
No-op.

**variant-axis-coverage — pass (not applicable to audit-report kind).** The audit carries no
operator with orthogonal variant axes of its own. The scoped-coverage analysis it DOES
perform (the impl realizes the Hiptmair distributive sub-case; chebyshev/jacobi siblings
realize the point-smoother cases of the same slot) is correctly disclosed in the proposed
`verified_against` note and Open-questions, not hidden — but this is a correspondence-scope
observation, not a missed variant branch.

**cross-reference-integrity — pass.** All on-disk targets resolve: the four firm `depends-on`
constituents (`L1/chebyshev-smoother`, `L1/apply_linop`, `L1/axpby`, `L1/interpolator` — all
confirmed `firm` on disk, so the rank-invariant `firm-impl ≤ min(firm-deps)` claim holds),
the three `reference:` targets (`L1/set_subvector_zero`, `concepts/sequential-obstruction`,
`L4/preconditioning-framework`), and the kernel-api target
`L1-L0/triangular-solve-obstruction` all exist. The `verified_against:` block round-trips
clean under `yaml.safe_load` (`YAML OK`); no `note:` value begins with a quote of either kind
(the YAML-round-trip sub-check passes). The impl chapter has no pre-existing
`verified_against` block, so the append is conflict-free.

**edge-label-fidelity — pass.** The audit's central edge-typing confirmation is sound and
independently verified: in the impl frontmatter the `realizes-kernel-api` edge
(`target: L1-L0/triangular-solve-obstruction`) is under the `reference:` key (lines 24-26),
NOT under `depends-on:` (lines 15-23) — so it is correctly `reference`-class (free,
navigational; constrains neither rank nor liveness), exactly as DIRECTIVE-3 specifies. The
audit's claim that the API surface stays `obstruction (opaque-library-ownership)` with the
`kernel-api` role-label added (NOT downgraded/promoted) is confirmed: the API chapter Status
line (545) reads `obstruction (opaque-library-ownership)` — **kernel-api**. The `[garbage?]`
graded-stack-lint flag on the kernel-api node is correctly characterized as by-design (its
only inbound is the free reference edge).

**plan-kind-consistency — pass.** The report is shaped as an audit (verdict FAITHFUL,
per-citation audit table, correspondence assessment, integrity gate) and declares no status
flip — content shape matches the lowering-verifier audit kind. No firm-with-rough-in-
placeholder mis-classification.

**skill-uptake-survey — pass.** The audit references `citecheck.py` (`--anchor` on every
load-bearing anchor) and `graded_stack_lint.py`, the relevant procedures for a kernel-API/impl
correspondence audit. Telemetry only.

### Issues found

1. **Over-range provenance citations (citation-validity, low severity).** Report frontmatter
   `inputs:` lines 9-10 and Supporting-evidence lines 368, 371 cite
   `reference/palace/palace/linalg/distrelaxation.cpp:1-157` (file is **156** lines) and
   `reference/palace/palace/linalg/distrelaxation.hpp:1-93` (file is **92** lines). Both END
   bounds are +1 past EOF. These are whole-file "read on disk" provenance ranges, not
   proposed-change citations, and the report body cites the correct in-range substantive
   anchors. Candidate carry-forward: `:1-157`→`:1-156`, `:1-93`→`:1-92`. Does not affect the
   FAITHFUL verdict or the three proposed changes.

No other issues. The two off-by-one carry-forward corrections the report proposes
(DRIFT-1 `:103`→`:102`, DRIFT-2 `:121-152`→`:121-151`) were independently confirmed correct
against on-disk source; the `verified_against:` block is well-formed and YAML-clean; the
edge-typing and API-status integrity claims are sound.

## Repair

### Fixes attempted

- **Finding**: Over-range provenance citations (citation-validity, low) — `distrelaxation.cpp:1-157`
  (file = 156 lines) and `distrelaxation.hpp:1-93` (file = 92 lines); each cited END is +1 past EOF.
  Whole-file "read on disk" provenance ranges in frontmatter `inputs:` + Supporting-evidence; NOT in
  any proposed-change citation.
  - **Decision**: repaired
  - **Action**: Verified file line counts via `wc -l` (cpp = 156, hpp = 92, each +1 below the cited END,
    confirming the +1 over-range). Applied four surgical END-line fixes in CYCLE.md:
    - `inputs:` (lines 9-10): `distrelaxation.cpp:1-157`→`:1-156`, `distrelaxation.hpp:1-93`→`:1-92`.
    - Supporting-evidence (lines 368, 371): same two END-line corrections.
  - This is exactly the in-scope "citation line range off by a small offset" repair class — purely
    bounds-mechanical, no content authored.

The four PROPOSED off-by-one corrections in the audit's proposed-changes (`:103`→`:102` ×2,
`:121-152`→`:121-151` ×2) are the audit's verified deliverable and were left untouched.

### Unrepairable findings

None.

## Suggested resolution

`ready`. The sole warning was a low-severity provenance-only bounds drift (two whole-file END ranges,
not load-bearing, not in any proposed-change citation). Both fixed surgically; the FAITHFUL verdict and
all three proposed changes are unaffected. No follow-up agent needed.
