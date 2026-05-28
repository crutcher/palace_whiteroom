---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T23:35:00Z
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
repaired_at: 2026-05-27T23:45:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: unrepairable
overall_status: ready
follow_up_agent: null
---

# META: critique of harvester L3 BLAS-1 reduction-cohort (dot + nrm2) backfill

## Critique

### Checks run

**citation-validity** — Spot-checked the citations to L0 Palace source (`palace/linalg/iterative.cpp:631, 810` — confirmed `Hj[j+1] = linalg::Norml2(comm, w)` at both lines in the GMRES Arnoldi inner loops), the L1 entries (`book/src/L1/dot.md` is firm cycle-002 and `book/src/L1/nrm2.md` is firm cycle-003 — both present, content matches), the L3-L2 body-identity theme line 97 (verbatim text confirmed — "no element-loop exposed at L2" and "each L1 primitive is *also* L3-native"), the L3 index line 13 ("Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)" — exact match), the cycle-010 audit at `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" (2) — HIGH CONFIDENCE bundle recommendation confirmed verbatim, and the `concepts/nrm2.md:8-9` stability claim (line 9 "Stability: production implementations use scaled summation (BLAS `nrm2` algorithm)..." — exact match, the OQ extraction is faithful). The `book/src/L1/nrm2.md:11` cross-reference points at the paragraph containing the correction-pending note (the text "the concept page claims Palace uses 'scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow'. This is **not** what `linalg::Norml2` actually does" begins on that line). All citations resolve to real, in-range locations. `pass`.

**surface-or-evidence** — The report creates two NEW firm L3 entries (`book/src/L3/dot.md`, `book/src/L3/nrm2.md`) plus dep-map and SUMMARY.md updates. This is fresh surface authoring, not a refinement-shape proposal mutating existing operator surface without evidence. The L3 entries cite their L1 anchors, the L3-L2 body-identity theme line 97 (structural justification), the cycle-010 audit (origin of the dispatch), the L4-L3 typed-wrapper-dissolution theme, and direct Palace source ranges where the consuming context is direct. `pass`.

**rotation-quality** — The asserted rotation is **identity-in-form** (L3→L1), justified by the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md, cycle-009 codification). This is an explicit identity-rotation per the invariant — it is NOT claiming a strictly-more-compact representation; it is claiming the L3 form is value-thread-isomorphic to the L1 form and the L3 entry exists for layer-coherence reasons. The check is satisfied because (a) the rotation is correctly labelled as identity-in-form, not as a substantive compression that fails 1:1; (b) the precedent (`L3/krylov-step.md`, cycle-010) is correctly cited; (c) the structural justification (whole-tensor signature, no element loop exposed) is anchored in the L3-L2 theme line 97; (d) the relevant invariant explicitly permits identity rotation as the rotation type here. The rotation work is at the surrounding `krylov-step` wrapper, not on the primitive — correctly stated. `pass`.

**variant-axis-coverage** — For `dot`: 2 axes (element-type, conjugation-convention) declared at L3 — inherited unchanged from L1 (`book/src/L1/dot.md` §Variant axes lists the same 2 axes). The `tdot` complex-unconjugated variant is explicitly covered (laws 11–13). For `nrm2`: 1 axis (element-type, collapsed to a single operator producing real-valued result) — inherited unchanged from L1 (`book/src/L1/nrm2.md` §Variant axes lists the same 1 axis with the same collapse rationale). B-weighting explicitly scoped out at L3 (deferred to a separate operator `matrix-weighted-norm` rough-in at L1 — file exists). Stability-variants (scaled-summation) explicitly scoped out (not present in Palace's `linalg::Norml2`). No hidden branches; coverage is complete. `pass`.

**cross-reference-integrity** — Spot-checked the cross-references: `book/src/L1/dot.md` (exists, firm), `book/src/L1/nrm2.md` (exists, firm), `book/src/L3/krylov-step.md` (exists, firm cycle-010), `book/src/L3-L2/krylov-step-body-identity.md` (exists, firm), `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (exists, firm), `book/src/L2/krylov-step.md` (exists), `book/src/L4/krylov-step.md` (exists), `book/src/concepts/dot.md` (exists), `book/src/concepts/nrm2.md` (exists), `book/src/concepts/sequential-obstruction.md` (exists), `book/src/concepts/convergence-test.md` (exists), `book/src/L1/matrix-weighted-norm.md` (exists, rough-in). SUMMARY.md "after line 19" anchor is correct (line 19 = `- [krylov-step](./L3/krylov-step.md)`). L3 index "after line 19-21" anchor for dep-map rows checks out (line 21 is the existing `krylov-step` dep-map row). No broken slugs, no dangling paths. `pass`.

**edge-label-fidelity** — Both entries assert L3→L1 identity-in-form. The prose discusses precisely that edge: "the L3 form is value-thread-isomorphic to the L1 form" (Context §); the §"L3 vs L1 distinction" section makes the L3-vs-L1 contrast explicit; the §"Lowers to" section names L1 [`dot`] / [`nrm2`] as the target. The frontmatter `lowers_to:` field cites the L1 file paths. No mismatch — edge label and prose both speak about L3→L1. The report correctly notes that the **rotation work** for the cohort lives elsewhere (the surrounding `krylov-step` body wrapper, via the L3-L2 body-identity theme), but this is not a label/prose mismatch — it is a correctly-attributed locus statement. `pass`.

**plan-kind-consistency** — Declared kind: `firm` L3 operator entries (frontmatter `firmness: firm`). Content shape: complete §Context, §Signature with `text`-fenced type signatures (matching the CLAUDE.md §Methodology invariant "L4 and L3 pseudo-language is Haskell + TypeScript notation in fenced code blocks"), §Semantics, §Algebraic laws (13 for dot — 5 real + 5 complex-Hermitian + 3 complex-unconjugated for `tdot`; 10 for nrm2 plus 4 non-laws), §Dependencies, §Variant axes, §Status, §Lowers to, §Lifts from, §Evidence, §L3 vs L1 distinction. No rough-in placeholders, no unfilled stubs. Algebraic-law content is verifiable against the L1 entries (laws 1–13 for dot are the same set as L1 dot laws 1–13; laws 1–10 for nrm2 are the same set as L1 nrm2 laws 1–10). The Haskell `::` arrow form is used throughout. Pseudo-language is fenced as `text`. Matches the "firm operator entry" content profile. `pass`.

**skill-uptake-survey** — The dispatch involved verifying citations across many file ranges (8+ files, 30+ specific citation pointers). The `verify-citation-range` skill would have been a natural fit for the harvester's citation-verification work, but the report does not reference its invocation. Similarly, `verify-refinement-surface` could have applied since this is fresh-surface authoring (verification that the new surface matches its evidence). The `classify-variant-axis` skill would have applied to the variant-axis inheritance work. None of these skill invocations are surfaced in the report. Pure presence check; not a blocker. `warning` (surfaces telemetry only).

### Issues found

1. **(low severity, plan-kind-consistency adjacent) Algebraic-law numbering across multiple element-types lacks an explicit "type-conditional law selector".** In §"Algebraic laws" for `dot`, laws 1–5 apply to real element-type, laws 6–10 to complex element-type, laws 11–13 to the `tdot` variant. The numbering is continuous (1–13) and the section headers (in **bold**) name the applicable case for each block. This is fully inherited from `book/src/L1/dot.md` (same continuous-numbering convention there). No correction needed — flagged for repairer awareness that the L1 inheritance is faithful and the numbering style is consistent with the firm precedent. Not a defect; potential aesthetic improvement deferred to layer-intro-author for a future cohort-wide consistency pass.

2. **(low severity, skill-uptake-survey) Three relevant skills were not invoked by name.** `verify-citation-range`, `verify-refinement-surface`, `classify-variant-axis` would all have applied to the dispatch's citation-validity and variant-axis-coverage work. The report's verification work appears to have been performed (the cited line numbers are accurate, the variant axes are correctly inherited), but the skills were not explicitly cited. Telemetry-only finding; surfaces a pattern for meta-phase observation.

3. **(informational) The "post-batch-1 / cycle-009" timing reference in the cohort-backfill rationale is consistent across the L3/dot.md and L3/nrm2.md §Status sections — both correctly attribute the precedent to cycle-010 wave-1 and the methodology codification to cycle-009 meta-phase.** No issue; flagged for repairer awareness that the historical attribution is internally consistent and matches the CLAUDE.md §Methodology invariants entry ("Identity-lowerings still require both L levels" codified cycle-009 mid-cycle; first enacted cycle-010 wave-1).

4. **(informational, cross-cutting) The §Evidence section for L3/dot.md lists transitive test citations (`test/unit/test-orthog.cpp:157, 219-220, 271, 313-315, 373-376`) and source citations (`palace/linalg/iterative.cpp:395, 404, 444, 460`) WITHOUT direct re-verification.** The CYCLE.md §"Open questions / caveats" item 7 explicitly notes "Direct test re-verification was not done — the L1 entries' citations are taken as authoritative per the firm-status carried forward." This is consistent with the methodology — L3 is value-thread-isomorphic to L1, so transitive citations are acceptable — but the disclosure should be visible to the integrator for staging notes.

5. **(informational, OQ extraction) Both Open questions are correctly extracted and well-formed.** OQ #1 (`l3-l1-identity-in-form-annotation-policy-formalization`) accurately surfaces an open methodology-policy question — whether identity-in-form L3>L1 rotations should be recorded in-line (current cycle-011 wave-1 convention; sets precedent across the BLAS-1 cohort) or as dedicated `L3-L1/` theme files; the cycle-010 audit's open question #1 is correctly referenced as the upstream. OQ #2 (`concepts-nrm2-stability-claim-correction`) accurately extracts the `concepts/nrm2.md:8-9` false claim — the concept page line 9 says "Stability: production implementations use scaled summation (BLAS `nrm2` algorithm)" which contradicts the firm L1 entry's finding at `book/src/L1/nrm2.md:11` that "`linalg::Norml2` actually... computes the naive `√⟨x, x⟩` via `Dot`". The OQ is faithfully extracted and the line numbers are correct.

6. **(informational, integrator-merge awareness) The §"Open questions / caveats" item 3 surfaces wave-1 coordination concerns explicitly.** Sibling dispatches #1 (apply_linop), #2 (axpy cohort), #4 (scal) will each propose Working Notes bullet additions to `book/src/L3/index.md` referencing the cohort backfill in flight, plus their own dep-map row insertions and SUMMARY.md chapter entries. Per the integrator-per-report serial-dispatch model, this should naturally serialize, but the integrator may need to merge the bullet content. Flagged for integrator awareness; no defect in this report.

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey warning — three relevant skills (`verify-citation-range`, `verify-refinement-surface`, `classify-variant-axis`) were not invoked by name during the dispatch's citation-validity and variant-axis-coverage work.
  - **Decision**: unrepairable
  - **Rationale**: This is telemetry-only — the critic explicitly classified it as "pure presence check; not a blocker" and notes that "the report's verification work appears to have been performed (the cited line numbers are accurate, the variant axes are correctly inherited), but the skills were not explicitly cited." The repairer cannot retroactively annotate skill invocation history in the producer's CYCLE.md — that would be authoring substantive content about how the work was performed, not a mechanical surgical fix. Skill-uptake patterns are aggregated cross-cycle by meta-phase via `skill-uptake-survey` checks; this single-cycle warning is signal for the running aggregate, not a defect requiring repair.

- **Finding**: Issues 1, 3, 4, 5, 6 — all low-severity / informational; the critic flagged each as not requiring correction (Issue 1 explicitly "Not a defect"; Issues 3–6 explicitly "informational" with "no issue" / "no defect" framing).
  - **Decision**: not-needed
  - **Rationale**: The critic's prose itself classifies these as "flagged for repairer awareness" or "flagged for integrator awareness" — they are evidence surfacing, not findings requiring repair. No mechanical fix is in scope; passing through to the integrator with the critic's notes attached is the correct disposition.

### Unrepairable findings

- **skill-uptake-survey warning** — informational telemetry; not actionable at repair-authority level. Aggregates at meta-phase across the 3-cycle batch via the standing `skill-uptake-survey` check. No follow-up agent named (the meta-phase already consumes this signal as part of its standard cross-cycle aggregation).

## Suggested resolution

`ready`. The report's 8 checks pass except for the `skill-uptake-survey` warning, which the critic explicitly classified as "telemetry only" and the repairer classifies as unrepairable-but-not-blocking. The 6 issues raised by the critic are all explicitly informational / awareness notes, with no substantive defect requiring repair. The 2 valid OQs (`l3-l1-identity-in-form-annotation-policy-formalization`, `concepts-nrm2-stability-claim-correction`) are well-formed and should be promoted to `scaffolding/open-questions.md` by `integrator-per-report` per standard flow. Integrator awareness items (transitive test citations per Issue 4; sibling dispatch wave-1 merge coordination per Issue 6) are surfaced for STAGING.md context but require no pre-staging repair.
