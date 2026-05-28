---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T20:11:00Z
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
---

# META: verification of "Audit orthogonalize-mutation-rotation" (lowering-verifier, CONFIRMS-WITH-REFINEMENT)

## Critique

### Checks run

**citation-validity — pass.** I independently re-read every cited range via `palace-codemap`
and all support the report's claims. `get_symbol_def` confirms `OrthogonalizeColumnMGS` spans
`orthog.hpp:41-53` and `OrthogonalizeColumnCGS` spans `:57-89`. `read_range :41-90` confirms
the MGS single interleaved loop (dot → `GlobalSum(1,&H[j])` → `w.Add(-H[j],V[j])`), the CGS
`if (m==0) return;` early return + size-`m` `GlobalSum(m,H)` two-phase split, and the CGS2
`if (refine)` block with `H[j] += dH[j]` and a second `GlobalSum(m, dH.data())`. The MGS
complex-order comment is at `:48` (line 41 = signature; the comment is the line before
`H[j] = dot_op(...)`) — confirmed, no drift. **R1 verified independently**: in `read_range
:307-325` the CGS2 dispatch `OrthogonalizeColumnCGS(comm, V, w, Hj, j + 1, true)` sits at line
322, and `get_call_sites(OrthogonalizeColumnCGS)` independently returns `iterative.cpp:322` —
so the theme's `:321-323` is genuinely correct-but-loose and the `→:322` tightening is sound.
GMRES `:620-633` (`w=V[j+1]`@622, dispatch@630, `Norml2`@631, `*=`@632) and FGMRES `:806-812`
(dispatch@809, `Norml2`@810, `*=`@811) are exact. The empty-basis TEST_CASE is at
`test-orthog.cpp:99` with `GENERATE` over all three variants and `CHECK_THAT(w,
RangeEquals(w_orig))` at `:120`.

**surface-or-evidence — pass.** This is an audit (pure retroactive evidence verification), not
a refinement-shaped surface proposal. The report explicitly does NOT mutate `book/`; it
proposes a `verified_against:` evidence block + two anchor-precision tightenings for a follow-up
dispatch. Retroactive-evidence framing is explicit and allowed.

**rotation-quality — pass.** Not a rotation proposal; this audits an existing firm L1>L0
lowering. The underlying theme is a genuine buffer-rebinding rotation (the L1 pair `(w', H)`
into in-place `w` + raw-pointer `H`), state-hiding, not a 1:1 rename. The audit correctly
upholds it without re-asserting or re-deriving the rotation.

**variant-axis-coverage — pass.** The MGS/CGS/CGS2 variant axis is the load-bearing axis and
the audit verifies all three sub-patterns plus the recognition-set closure. I re-ran the
closure independently: the enum `enum class Orthogonalization : char { MGS, CGS, CGS2 }`
(`labels.hpp:165-170`) has exactly 3 variants; `get_call_sites` returns MGS→3
(iterative.cpp:316, romoperator.cpp:59, test-orthog.cpp:87) and CGS→6 (iterative.cpp:319/322,
romoperator.cpp:62/65, test-orthog.cpp:90/93); CGS2 is `OrthogonalizeColumnCGS(...,true)`, not a
fourth free function. The inner-product hook sub-axis (identity vs B-weighted `dot_op`) is
correctly scoped as a substitution of the firm `dot` dependency, not a hidden branch. No hidden
variant.

**cross-reference-integrity — pass.** The audited theme's `[L1/orthogonalize]`, `[L1/dot]`,
`[L1/axpy]` links all resolve (`book/src/L1/{orthogonalize,dot,axpy}.md` exist). All
operator/function slugs the report names (`OrthogonalizeColumnMGS/CGS`, `OrthogonalizeIteration`,
`OrthogonalizeColumn`) resolve to real symbols. The report's own internal citations all point at
real, in-range source locations.

**edge-label-fidelity — pass.** The report carries the L1>L0 edge throughout; every sub-pattern,
applicability condition, and algebraic-law discussion narrates the L1→L0 rewrite (in-place `w`
overwrite + raw-`H` write ← pure `(w',H)`). The Open-questions section explicitly affirms
direction-of-definition is clean (forward L1→L0, no reverse-lift narration). No edge mismatch.

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit with verdict
CONFIRMS-WITH-REFINEMENT; the content matches exactly — per-citation `supports` verdicts,
recognition-set closure, applicability/law re-verification, and anchor-precision-only refinements
(R1 required, R2 cosmetic). The "firm upheld" verdict does not overreach into re-authoring: the
report defers R1/R2 + the `verified_against:` append to a follow-up `lifter`/`abstractor`
dispatch and performs no `book/` mutation. Correctly scoped.

**skill-uptake-survey — warning (non-blocking).** The report's shape directly matches two
existing skills — `verify-citation-range` (it audits citation ranges, and the cycle-012
meta-phase added an "Audit-report / inherited-citation sub-case" section precisely for this) and
`verify-rotation-citation` — yet neither is referenced by name in the report. The audit clearly
performs the equivalent procedure (independent `read_range` + `get_symbol_def` bounds, treating
bulk-read offset as an artifact), so this is telemetry only, not a defect. Surfacing for
skill-uptake tracking.

### Issues found

No blocking issues. The audit is sound, well-scoped, and its single required refinement (R1)
verifies correct independently.

- **(telemetry, low) Skill-invocation not referenced** — `CYCLE.md` (whole report):
  performs `verify-citation-range`-style range auditing (including the inherited-citation
  sub-case the cycle-012 meta-phase added) without naming the skill. No content impact;
  skill-uptake-survey telemetry only.

- **(observation, informational) R2 is cosmetic and self-flagged** — `CYCLE.md` §Proposed
  changes / Sub-pattern C: the report proposes optionally extending the CGS2 body cite
  `orthog.hpp:75-88` → `:75-89` to include the function-closing brace. `get_symbol_def` confirms
  the function ends at `:89` and the load-bearing content (`:75-87`) is fully inside the existing
  `:75-88`, so this is genuinely optional, not a citation defect. Correctly classified by the
  report as cosmetic. Recorded here only so the repairer/integrator can disposition it as
  no-action without re-investigating.

- **(scope caveat, not a defect) Applicability condition 1 audited only for GMRES/FGMRES** —
  `CYCLE.md` §Applicability conditions / §Open questions: the "no observer of prior `w`" condition
  is proven lexically only for the GMRES/FGMRES sites; the ROM greedy-sampling consumer is not
  audited (the cited `romoperator.cpp:51-66` is the dispatch wrapper, not the consumer). The
  report correctly frames this as an audit-scope caveat matching the theme's own GMRES/FGMRES
  scoping, not a refutation. Noted for completeness; no action required for this verdict.

---
repaired_at: 2026-05-28T20:31:00Z
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

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey — warning (telemetry only). The audit performs
  `verify-citation-range`-style range auditing (including the cycle-012 inherited-citation
  sub-case) and `verify-rotation-citation`-style work without naming either skill.
  - **Decision**: not-needed. The critic explicitly classed this as telemetry only, no content
    impact. Acknowledged for skill-uptake tracking. The procedure was performed correctly
    (independent `read_range` + `get_symbol_def` bounds, treating bulk-read offset as an
    artifact); only the by-name reference is absent, which is not a defect the repairer authors
    into the report.

- **Finding**: R2 is cosmetic and self-flagged (informational observation) — optional extension
  of CGS2 body cite `orthog.hpp:75-88` → `:75-89` to include the function-closing brace.
  - **Decision**: not-needed. `get_symbol_def` confirms the load-bearing content `:75-87` is
    fully inside the existing `:75-88`; the report correctly classifies this as optional/cosmetic
    and routes it to a follow-up dispatch. No mechanical defect to fix.

- **Finding**: Applicability condition 1 audited only for GMRES/FGMRES (scope caveat, not a
  defect) — ROM greedy-sampling consumer not audited.
  - **Decision**: not-needed. Correctly framed by the report as an audit-scope caveat matching
    the theme's own GMRES/FGMRES scoping. No action required.

### Unrepairable findings

None. No blocking issues; no mechanical defects.

## Suggested resolution

`ready` — no repairs needed. The single critic warning is telemetry-only (skill-uptake) with no
content impact.

Integrator note: the R1/R2 anchor-precision refinements and the `verified_against:` evidence block
in `CYCLE.md` §Proposed changes are a clean, well-formed proposed-changes block, explicitly deferred
(audit-only dispatch; no `book/` mutation here). For the follow-up `lifter`/`abstractor` dispatch
against `book/src/L1-L0/orthogonalize-mutation-rotation.md`:
- **R1 (required)**: tighten the sub-pattern C dispatch citation `iterative.cpp:321-323` → `:322`
  (CGS2 = `OrthogonalizeColumnCGS(..., true)`). Independently confirmed correct by the critic via
  `get_call_sites` (returns `iterative.cpp:322`).
- **R2 (cosmetic, optional)**: `orthog.hpp:75-88` → `:75-89` (closing brace); may be left as-is.
- Append the `verified_against:` YAML block (emit `~~~` as triple-backtick fence per the report's
  in-line note).
