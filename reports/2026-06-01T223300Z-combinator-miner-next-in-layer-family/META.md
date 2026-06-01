---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T23:55:00Z
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
repaired_at: 2026-06-02T00:10:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of "Combinator candidate — next-in-layer-family (NEGATIVE / spine-coverage result)"

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` on the report returns `18 ok, 0 failing`. All load-bearing pinpoints were anchor-confirmed against source: jacobi-smoother `:73-78` (the `polynomial_smoother` "candidate but not pursued here", Jacobi apply is plain elementwise scaling — quoted verbatim) and `:160-185` (the "Negative fusion observation": degree-zero fixed point, no fused multi-operation kernel); chebyshev-iteration `:78-100` (anchor `recurrence` hits line 89 — the genuine three-term recurrence contrast is real); deflate `:248-276` (the "Do NOT collapse them into one combinator" over-unification guard) and `:230-234` (the `(XᴴX)⁻¹`/Schur load-bearing non-law); divfree-projector `:47-59` (standalone-gate-no-fold-parent, sibling to ksp_solve/eigsolve) and `:114-134` (four-step WeakDiv → Z_bdr → ksp_solve → Grad composition with nested iterative ksp_solve); krylov-step `:73` (`fold kernel, not an algebra`) and `:85-89` (the explicit commutativity/associativity/identity/linearity non-laws); L2/index `:21-26`/`:29` (the named-compositions + fold-cohort do-NOT-merge boundaries + the fork-INDEPENDENT standalone-floor cohort). One cosmetic note (below) on a generic anchor token; not a drift.

**surface-or-evidence — pass.** Not a refinement: the report authors NO surface change. It is an explicit negative/observation finding ("**No artifact changes.** (A negative finding produces no dep-map row.)", §Proposed changes). The negative finding is framed as a spine-coverage result with citation backing throughout. No surface-without-evidence and no rotation-claim-without-surface defect can arise. Pass (negative-finding shape).

**rotation-quality — pass (n/a).** No algebraic/structural/reduction rotation is asserted — the report's load-bearing claim is the *absence* of a conciseness-positive in-layer combinator. The negative arguments correctly invoke the conciseness criterion in the redirect's own terms (a forced `polynomial_smoother`/`subspace_project` would special-case bodies and add vocabulary "without simplifying anything upstream" = the mine-and-strand anti-pattern). Not applicable to a negative-finding report.

**variant-axis-coverage — pass.** The candidate adjudication is exhaustive across the three named candidate families AND across all three mining modes (same-shape, parametric/fold, constructed-operator-action-family) in §"Why this is a spine-coverage result". Each candidate's rejection axis is named: (a) the smoother degree-zero/recurrence split + the retired Richardson gap; (b) the projector tri-axis parameterization (basis-storage / solve-kind / coordinate-extraction) yielding no shared combining step; (c) the krylov inner-products being consumers of the existing fold. No hidden un-surveyed family branch.

**cross-reference-integrity — pass.** Every cited file exists on disk (jacobi-smoother, chebyshev-iteration, deflate, divfree-projector, krylov-step, L2/index, open-questions). The OQ slug `polynomial-smoother-l2-combinator-from-jacobi-and-chebyshev` resolves and its CLOSED-BLOCKED-RETIRED status is confirmed at both `open-questions.md:578` and `:628` (anchor `BLOCKED-RETIRED` hits 578). No firm-body-inside-fence guard applies (no `firm` proposed-changes block — there is no proposed-changes block at all). The two newly-named OQ slugs are well-formed and append-only-channel appropriate.

**edge-label-fidelity — pass (n/a).** No lowering-edge label is carried (in-layer combinator survey, not a lowering theme). Not applicable.

**plan-kind-consistency — pass.** Declared shape is a NEGATIVE finding / spine-coverage result with `status: pending` and "NEGATIVE finding" in the scope line; the content matches exactly — no combinator proposed, no dep-map row, an OQ surfaced for the meta-phase. This is the correct classification for a deliberate no-mine result; there is no mis-stated "firm combinator" entry hiding rough-in content.

**skill-uptake-survey — warning.** The report's shape (combinator-family survey + citation-pinpoint verification) plausibly implies the `propose-rotation` / `verify-rotation-citation` skills and the combinator-mining survey procedure, but the report references no skill invocation by name. This is a pure-telemetry, non-blocking surface: the survey methodology (three modes, fold-law guard) is clearly applied, just not skill-attributed. Surfaced for meta-phase visibility only.

### The load-bearing check: is the negative finding sound?

Verified each candidate's rejection against the cited source — none re-buries a real opportunity:

- **(a) smoother.** `L2/jacobi-smoother.md:73-78` states verbatim that `polynomial_smoother` "is a candidate but **not pursued here**" because "Jacobi's per-call action is a plain elementwise scaling, not a polynomial action." `:160-185` confirms the Jacobi apply is the degree-zero fixed point with "**no fused multi-operation kernel to unfold**", contrasted against chebyshev-iteration's genuine three-term recurrence (`:78-100`, confirmed). The Richardson-sibling retirement is REAL: `open-questions.md:578`/`:628` show `polynomial-smoother-l2-combinator-from-jacobi-and-chebyshev` closed BLOCKED-RETIRED at the cycle-036 meta-phase (Palace ships no third Richardson sibling; out of scope per unimplemented-Palace-components policy). D5 did NOT re-propose the retired form. Sound.
- **(b) projector/gate.** `L2/deflate.md:248-276` is the explicit "Do NOT collapse them into one combinator" guard; `:230-234` confirms the `(XᴴX)⁻¹`/Schur correction is load-bearing (erasing it "silently assumes an orthonormal basis and changes the algorithm"). `divfree-projector.md:47-59` confirms it is a standalone constructed-operator gate with NO fold-parent (sibling to ksp_solve/eigsolve), and `:114-134` confirms its subspace solve is a nested iterative `ksp_solve`, not a dense `lu_solve` and not an MGS subtraction — a genuinely third thing. A `subspace_project` union over the three would have no shared combining step. Sound.
- **(c) krylov inner-fold.** `L2/krylov-step.md:50, :60` confirm the scalar-stratum updates are `dot`/`nrm2` reductions; `:73` confirms krylov-step is "a fold kernel, not an algebra in its own right"; `:85-89` confirm the explicit non-laws. These inner products are consumers of the already-firm `inner_product`/`dot`/`nrm2` fold, not a new fold. Sound.

**spine-coverage signal — well-supported.** The OQ `firm-l2-l3-surface-is-combinator-complete-for-in-layer-conciseness` is corroborated by `L2/index.md:21-26, :29`: the two folds (`inner_product`, `linear_combination`) are the named fold cohorts with load-bearing do-NOT-merge boundaries, and the standalone-floor cohort is design-final (no fold-parent to fold into). The "surface is saturated for in-layer mining" claim is a legitimate, evidence-grounded finding, not a cop-out. The accompanying plan implication (re-point combinator-miner at newly-lifted solver test-load material rather than re-scanning the saturated surface) is consistent with the 2026-06-01 redirect's solvers-as-test-load framing.

**no book mutation — confirmed.** §"Proposed combinator" = NONE; §"Proposed changes" = "No artifact changes." Correctly NOT forcing a combinator (would be mine-and-strand). The report touches only its own CYCLE.md plus the append-only OQ channel.

### Issues found

- **(cosmetic, citation-validity, low severity)** §Supporting evidence cites `scaffolding/open-questions.md:543, :578, :628` for the polynomial-smoother OQ. The substance is correct (`:543` is the deferred entry; `:578` and `:628` are the two BLOCKED-RETIRED closure notes — both confirmed via `--anchor 'BLOCKED-RETIRED'`). A mechanical `--anchor 'CLOSED'` probe at `:628` reports a drift to line 582 only because the generic token "CLOSED" first appears at the section heading on 582; the BLOCKED-RETIRED closure text genuinely sits at 628. This is NOT a real off-by-one — all three line refs land in-range and support the claim. No repair needed; noted for completeness.

- **(skill-uptake, informational, non-blocking)** No skill invocation is referenced (see skill-uptake-survey check). Telemetry only.

No blocking issues. The negative finding is sound on all three candidates, the spine-coverage signal is well-supported, and declining to force a combinator is the correct result under the redirect — this report is NOT penalized for not mining one.

---

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey — warning. Report applies a combinator-family survey methodology (three mining modes + the fold-law do-NOT-merge guard) and citation-pinpoint verification, but references no skill invocation by name. Pure telemetry, non-blocking.
  - **Decision**: repaired (telemetry-only note; no content change).
  - **Action**: recorded below in §Skill-uptake telemetry — the survey shape maps to the combinator-mining survey procedure + `verify-rotation-citation` / `propose-rotation` (the latter declined-by-design, since the result is negative). No edit to REPORT.md content — a negative-finding survey carries no claim that a skill attribution would change, and editing the report body to back-fill skill names would be content authoring outside repair authority. The attribution is captured here in META.md for meta-phase visibility.

- **Finding**: (cosmetic, citation-validity, low severity) — `--anchor 'CLOSED'` probe at `open-questions.md:628` reports drift to line 582 because "CLOSED" is a generic token first appearing at the section heading; the actual `BLOCKED-RETIRED` closure text is at 628 and the critic confirmed all three line refs (`:543`, `:578`, `:628`) land in-range.
  - **Decision**: not-needed.
  - **Rationale**: the critic explicitly confirmed the line refs support the claim (`--anchor 'BLOCKED-RETIRED'` lands correctly); the `CLOSED`-token drift is a probe artifact, not an off-by-one in the report. No edit warranted.

### Skill-uptake telemetry

- **Applied (un-attributed in report)**: the combinator-mining survey procedure (three modes — same-shape / parametric-fold / constructed-operator-action-family — adjudicated across the three candidate families) and citation-pinpoint verification equivalent to `verify-rotation-citation` (18 ok / 0 failing on `citecheck --scan`).
- **Declined by design**: `propose-rotation` — the result is a NEGATIVE finding (no conciseness-positive in-layer combinator on the firm L2/L3 surface), so no rotation/combinator is proposed. Declining is correct, not a miss.
- **Not invoked**: no slice-reduction / lowering-verifier procedures (out of this dispatch's scope).

### Unrepairable findings

None. All critic findings are either `pass`, or the lone `warning` is telemetry-only (addressed by the note above with no content change). The deliberate negative finding is a sound PASS — declining to force a combinator avoids the mine-and-strand anti-pattern.

## Suggested resolution

`ready`. Notes for the integrator:

- **D5 authored no artifact changes.** Its deliverable is (1) the negative / spine-coverage finding (no genuine un-mined in-layer combinator family on the current firm L2/L3 surface — smoother retired-gap re-confirmed, projector/gate already-mined with load-bearing do-NOT-merge guards, Krylov inner-products are consumers of the existing fold) and (2) the OQ `firm-l2-l3-surface-is-combinator-complete-for-in-layer-conciseness`. No `book/` mutation to apply.
- **Promote the OQ at integration** (append-only channel; well-supported by `L2/index.md:21-26, :29`).
- **Batch-16 frontier signal**: D5 converges with D6's electrostatic probe — the next in-layer combinator must come from newly-lifted solver test-load material, not from re-scanning the saturated firm surface. Consistent with the 2026-06-01 solvers-as-test-load redirect. Worth surfacing to the meta-phase as a re-point-combinator-miner signal.
