---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T14:56:14Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-28T15:10:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "phase-1 corpus reduction batch-4 — final 2 slices"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing citation in the report resolves to a real, in-range location. Verified independently:
- The section-anchor tables for both slices match the actual file structure exactly. `cg_preconditioning_framework.md` is 533 lines; its H1/H2 boundaries (`## Context` 3, `## Background` 7, `## L0` 17, `## L1` 61, `## L2` 115, `## L3` 221, `## L4` 293, `## L4 v0.2` 413, `## L4 v0.3` 472–533/EOF) all match `grep -n '^#'`. `sparse_triangular_solve.md` is 232 lines; its H1/H2/H3 boundaries (incl. the 6 L0 H3s 31/43/67/79/91/102 and the L1 H3s 116/134, `## Disposition` 146, `### Classification` 154, `## Open questions` 190, `## Methodological status` 202) all match.
- The firm absorbing entries exist: `L1/ksp_solve.md` (confirmed firm at `scaffolding/roadmap.md:183`, "ksp_solve cycle-007"), and all six L0 anchors (`kspsolver-base-class`, `ksp-factory-file`, `mfem-wrapper-solver`, `linalg-operator-file`, `linalg-solver-file`, `preconditioner-classes-overview`).
- The two load-bearing concept-page back-citations were checked at their exact cited lines: `capability-typing.md:55` literally reads "the canonical first use site (TrueOp / PcAssemblyOp brands on the KSP binding)" pointing at the slice's L4 v0.2 — exactly as claimed. `scope-out-obstruction.md:66` "## Canonical instance" / `:68` cites the slice (report cited `:68`). `sequential-obstruction.md:50` "## Sub-kind: out-of-scope-obstruction" / `:53` cites the slice (report cited `:53`). All ten supporting-evidence concept citations (`two_operator_split.md:26`, `constructed-operator-factory.md:34`, `complex-from-real-lift.md:25,31`, `finest-level-unwrap.md:22`, `counter-update.md:20`, `solver-as-operator.md:30`, `build-time-vs-run-time-stratification.md:33`, `capability-typing.md:26`) point to lines that cite the slice back as introducing-slice/use-site.
- `dependency-map.md:168-390` carries **27** `cg_preconditioning_framework` edges — the report's "multiple edges" is accurate.
- The claimed-missing firm L4 entries (`L4/ksp-solve.md`, `L4/preconditioning-framework.md`) are confirmed absent, supporting the L4 "partial"/"none" supersession rows and the OQ.

**surface-or-evidence — pass.** Not a refinement-shaped proposal against an operator/theme; this is a corpus-reduction (slice-stub) audit. The two proposed changes modify slice surface (prepend reduction-status blockquotes) and the evidence is the supersession map + verified back-citations. No pure-rotation-claim concern applies.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted in the L_{n}→L_{n+1} sense. The "reduction" here is corpus reduction (slice → stub-and-pointer), not a layer rotation. The report correctly does NOT claim a rotation.

**variant-axis-coverage — pass.** The report self-labels its observation kind "Variant-axis coverage gap" loosely, but its actual content covers both eligibility outcomes exhaustively: slice 1 reducible-but-not-removable (partial absorption) and slice 2 structurally-non-removable (load-bearing negative result). Both branches are explicit; nothing hidden. The corpus-metric caveat (10/10 annotated-reduced vs 0/2 removed) is the right disambiguation and surfaces the residual axis (removal blocked on firm-L4 lift) rather than burying it. Note: the "Observation kind" label is a slight mis-fit — these are reduction-status verdicts, not a unification/redundancy/contradiction — but that is a labeling nuance, not a coverage gap.

**cross-reference-integrity — warning.** All `[link]`/path references in the proposed stubs resolve (every L0/L1/concept slug cited exists; `negative-result-slice.md`, `scope-out-obstruction.md`, `sequential-obstruction.md` all present). The reduction shape (prepend blockquote, delete no section) preserves the slice filename anchors and H2 headings, so the ten inbound concept-page citations (which reference the slice by path + prose section label, not by line number) survive intact — scrutiny point (d) is satisfied for the inbound links. **One asymmetry:** the slice-2 stub asserts "this slice is a **negative-result slice** (`concepts/negative-result-slice.md` family)", but `negative-result-slice.md` §"Examples in this spec" lists ONLY `polynomial_recurrence_step` (`:46`) and contains zero mentions of `sparse_triangular_solve`; the slice itself does not currently reference the `negative-result-slice` concept either. This differs from the cited `polynomial_recurrence_step.md` precedent, whose stub points at a *reciprocal* citation (`negative-result-slice.md:46`). The classification is sound in spirit and the genuinely load-bearing reciprocal citations (`scope-out-obstruction.md:68`, `sequential-obstruction.md:53`) are real and verified — so the retention verdict stands — but the "family" framing overstates a one-directional membership that `negative-result-slice.md` does not document. Issue I1 below.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; this is a same-layer (slice-corpus) audit. The supersession-map "section → firm-entry" arrows are absorption pointers, not lowering edges, and the prose discusses exactly those absorptions.

**plan-kind-consistency — pass.** The declared shape is an audit/observation (same-layer-cross-cutter reduction verdict), and the content matches: two verdicts (`partially-absorbed`, `not-yet-eligible`), supersession maps, residual-gaps, proposed reduction-status headers that delete no body. No firm-operator or rough-in mis-classification. The two reduction shapes (stub-and-pointer vs negative-result annotation) correctly match their cited precedents (`divfree`/`chebyshev`/`gmres` for slice 1; `polynomial_recurrence_step` for slice 2).

**skill-uptake-survey — pass.** The `phase-1-slice-reduction-audit` skill is referenced by name and its procedure was genuinely applied — scrutiny point (c) confirmed. The report emits section-anchor tables with BOTH start AND end columns (skill step 1, START+END boundary verification — the refinement that motivated promotion), enumerates H1+H2 (slice 1) and H1+H2+H3 (slice 2) covering intra-slice sub-sections, builds supersession maps (one row/section, 4 columns — step 2), has a Residual-gaps section enumerating only partial/none rows (step 3), and confirms `grep -c = 1` for both START anchors (step 5 reconciliation; both verified independently = 1). The negative-result failure-mode ("the slice IS the artifact") is correctly invoked for slice 2 matching the skill's documented `polynomial_recurrence_step` recovery.

### Scrutiny-point findings (per dispatch instructions)

- **(a) `cg_preconditioning_framework` `partially-absorbed` verdict — sound.** The absorbing firm entries all exist and cover the cited blocks: `L1/ksp_solve.md` independently re-cites the same ksp.cpp/ksp.hpp/iterative.hpp ranges (verified via its §Context/Evidence prose); the six L0 anchors exist; the nine concept pages exist and each was verified to cite the slice back. The "retain §L4 v0.2/v0.3 verbatim" recommendation is justified: `capability-typing.md:55` names §L4 v0.2 as "the canonical first use site" (the brand machinery lives ONLY in the slice), and `derived-view-hoisting.md`'s worked examples are CG-residual + Chebyshev-initial-guess — it does NOT contain the `pcBoundOp` stored-vs-bound-divergence derived view that §L4 v0.3 carries (confirmed: zero `pcBoundOp`/`cg_preconditioning` mentions in that page). The slice is genuinely the sole detailed source for both sections; removing them would orphan the two concept back-citations. Verdict upheld.

- **(b) `sparse_triangular_solve` `not-yet-eligible`/permanent-retain verdict — sound.** The "load-bearing negative-result slice" framing holds: the slice IS reciprocally cited as the canonical instance by `scope-out-obstruction.md:68` and `sequential-obstruction.md:53` (both verified at the exact lines), and there is by construction no firm L0–L4 entry to absorb it (a negative result has no positive form). The `polynomial_recurrence_step` precedent (annotation-only, retained verbatim) is the correct template. Verdict upheld; see I1 for the one-directional "family" attribution nuance.

- **(c) skill START+END boundary verification — applied.** See skill-uptake-survey above. Both ends verified for every section; START anchors `grep -c`-confirmed unique.

- **(d) proposed stub preserves unique-text anchors — yes.** Both proposed changes are blockquote prepends after the H1 with no section deletion, so the slice filename and all H2/H3 headings persist; the inbound concept citations reference by path + prose section label (not line number), so they remain resolvable. The report's own §"Open questions / caveats" already flags the within-stub absolute-line-number drift (413/472/533 are pre-insert) and recommends section-heading-relative reading — a correct self-catch.

### Issues found

- **I1 (cross-reference-integrity, low severity).** Slice-2 proposed stub (CYCLE.md §"Proposed changes" Change 2, the `> ... negative-result slice (concepts/negative-result-slice.md family)` line) asserts membership in the `negative-result-slice.md` family, but `book/src/concepts/negative-result-slice.md` §"Examples in this spec" (`:46`) lists only `polynomial_recurrence_step` and does not mention `sparse_triangular_solve` (the slice does not back-reference the concept either). This is one-directional, unlike the reciprocal `polynomial_recurrence_step.md:1` precedent the report leans on. The load-bearing reciprocal citations (`scope-out-obstruction.md:68`, `sequential-obstruction.md:53`) are real, so the retention verdict is unaffected; the fix is either (i) soften the stub wording from "family" to the verified reciprocal citations only, or (ii) propose a parallel "Examples" row in `negative-result-slice.md` to make the membership reciprocal. Candidate for repair.

- **I2 (variant-axis-coverage / labeling, very low severity).** The §"Observation kind" header labels both verdicts a "Variant-axis coverage gap," but the body content is reduction-status eligibility verdicts, not variant-axis observations (and the report itself notes "Neither is a unification/redundancy/contradiction"). The mis-fit is cosmetic — the integrator reads the verdicts, not the kind label — but a more accurate label would be "reduction-status verdict / same-layer corpus observation." Candidate for a trivial repair.

- **I3 (citation-validity, informational — not a defect).** `L1/ksp_solve.md` carries no `status:` frontmatter field (it opens directly with `# ksp_solve`); the report's "(status `firm`)" claim in §"Supporting evidence" is corroborated by `scaffolding/roadmap.md:183` rather than by an in-file frontmatter field. The claim is true; flagging only because the cohort-frontmatter divergence is a known carried item (roadmap notes "L1 cohort frontmatter divergence still noted"). No action needed in this report.

## Repair

### Fixes attempted

- **Finding (I1, cross-reference-integrity, low):** slice-2 stub asserts `negative-result-slice.md` family membership, but that concept page's §"Examples in this spec" (`:46`) lists only `polynomial_recurrence_step` — the membership is one-directional, unlike the reciprocal `polynomial_recurrence_step` precedent.
  - **Decision:** repaired.
  - **Action:** CYCLE.md §"Proposed changes" Change 2 — softened the stub's family-membership wording. Changed "(`concepts/negative-result-slice.md` family)" to "(in the spirit of `concepts/negative-result-slice.md`; that concept page does not yet list this slice in its §"Examples in this spec")". Chose the lighter correct option (a — soften wording) over (b — author a new Examples row into the concept page), since the load-bearing reciprocal citations (`scope-out-obstruction.md:68`, `sequential-obstruction.md:53`) already carry the retention verdict and (b) would author content into an artifact concept page outside this report's slice scope.

- **Finding (I2, variant-axis-coverage / labeling, very low):** §"Observation kind" labels both verdicts a "Variant-axis coverage gap," but the body content is reduction-status eligibility verdicts (the report itself notes "Neither is a unification/redundancy/contradiction").
  - **Decision:** repaired.
  - **Action:** CYCLE.md §"Observation kind" — relabeled the lead-in from "Variant-axis coverage gap" to "Reduction-status verdict / same-layer corpus observation" (the critic's suggested accurate label). Trailing prose unchanged.

- **Finding (I3, citation-validity, informational — not a defect):** `L1/ksp_solve.md` firm status corroborated by `scaffolding/roadmap.md:183` rather than in-file frontmatter; the claim is true.
  - **Decision:** not-needed (acknowledged).
  - **Rationale:** the critic flagged this as informational/non-defect; the claim is correct and the frontmatter divergence is a known carried cohort item, not a per-report fix.

### Unrepairable findings

None. Both flagged candidates (I1, I2) were mechanical wording fixes within repair authority; I3 required no action.

## Suggested resolution

`ready`. Both repairs are surgical wording changes to CYCLE.md proposed-changes / observation-kind label; no body content authored, no artifact mutated. Integrator note: Change 2's stub now correctly states one-directional membership — the integrator need not add an Examples row to `concepts/negative-result-slice.md` to make the stub accurate. If a future cycle wants reciprocal membership, that is a separate concept-page edit (defer as optional).
