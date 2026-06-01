---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T201500Z
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
repaired_at: 2026-06-01T203000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of cross-layer verify-body audit of divfree-projector + jacobi-smoother gate themes

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing claim carries a pointer and the pointers resolve in-range. I confirmed the three source anchors directly via the codemap: `palace/linalg/divfree.cpp:185` is the real-branch `Grad->AddMult(psi, y, 1.0)` and `:180-181` are the complex Re/Im branches (both inside the `Mult` four-step apply at `:155-187`); `palace/linalg/jacobi.cpp:38` is `Y[i] = DI[i] * X[i]`, the single elementwise-multiply kernel. The artifact pinpoints also check out: `L2-L1/divfree-projector-leaf-identity.md:3-4` (the "mostly identity-in-form … with exactly one genuine fusion rotation" opening), `:113` (the step-4 RE-FUSION row), `:178-182` (the "structural fusion rotation … canonical L2>L1 rotation content" justification); `L3-L2/divfree-projector-body-identity.md:97` (step 4 "Identity (at this resolution)" with fusion deferred to the L2>L1 edge); `L3/divfree-projector.md:210-219` and `L2/divfree-projector.md:114-134` (four-step composition explicit at both layers, step 4 fused-shaped at L3 / flagged-for-unfolding at L2). Jacobi pinpoints likewise: `L3/jacobi-smoother.md:38` and `L2/jacobi-smoother.md:96` are both literally `jacobi_smoother op x = op.dinv ⊙ x`; the L3>L2 single-row identity table and the L2>L1 row-for-row identity table with "total and bijective on the gate" are present. A few cited line numbers are off by 1–3 (the report cites the jacobi-leaf table as `:102-107` where the data rows are `104-107` under a header at `102-103`; the L3-L2 jacobi table is cited `:110-112` where the data row is `112`) — these are within-range header/body framing slips, not drift to the wrong content, so they do not change the verdict. No `verified_against:` block is emitted by this observation-only report, so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass (not a refinement proposal).** This is an observation-only verdict-quality audit, not a refinement that touches operator/theme surface. No surface is modified (confirmed: no proposed-changes block, no `book/` mutation). The single substantive assertion that overturns a prior classification — `divfree-projector-leaf-identity` is KEEP — rests on existing-evidence reading (the step-4 re-fusion row + the cpp:185/:180-181 anchors), which is the correct evidentiary basis for a verify-body audit. Not applicable in the refinement sense; the evidence-grounding it does carry is sound.

**rotation-quality — pass.** The check bites on the KEEP verdict: the report claims `divfree-projector-leaf-identity` carries a genuine fusion rotation. Verified — the L2 form's de-fused `axpy(1.0, apply_linop(P.Grad, ψ), y)` (two base primitives) re-fuses at L1 into the single `Grad->AddMult(ψ, y, 1.0)` MFEM apply-accumulate idiom (`L2-L1/...-leaf-identity.md:113`), and the L1 form is strictly more compact / more fused than the L2 form (one fused call vs. an apply ▷ accumulate pair with a materialized intermediate `g = P.Grad · ψ`). That is a real fusion rotation, not a 1:1 rename. The report also correctly classifies the three DEMOTE-OK themes as degenerate (no vocabulary shift): jacobi both edges are `op.dinv ⊙ x` → `op.dinv ⊙ x` (textually identical, confirmed), and the divfree L3>L2 edge keeps the four-step composition identity-mapped at both layers with step 4 explicitly deferred to L2>L1. The boundary-witness reasoning ("degenerate = no vocabulary shift, NOT body simplicity"; a four-step composition can still be a degenerate identity) is sound and is exactly the right distinction.

**variant-axis-coverage — pass.** The audit treats each of the four themes as a separate verdict and covers all four (3 DEMOTE-OK / 1 KEEP) with no hidden branch. The variant axes internal to the operators (jacobi element-type / damping-mode / operator-representation; divfree real vs. complex) are noted as absorbed into the gate / inherited unchanged, and the complex Re/Im branch of the divfree step-4 fusion is explicitly covered by the `:180-181` anchor alongside the real `:185`. No combination left implicit.

**cross-reference-integrity — pass.** All named slugs and links resolve: the four themes, the four endpoint entries, both L1 endpoints (`L1/divfree-projector.md`, `L1/jacobi-smoother.md`), and the two kept-substantive cohort comparisons (`L2-L1/chebyshev-iteration-fusion.md`, `L2-L1/deflate-composition-lowering.md`) all exist on disk. The inherited OQ slug `divfree-mult-doc-irrotational-vs-divfree-stale` is a real open-questions ledger entry. The build-readiness fence guard is not applicable — this is an observation-only report with no proposed-changes block and no firm-body claim to enclose.

**edge-label-fidelity — pass.** Every edge label matches the prose discussing it: the jacobi `body-identity` (L3>L2) and `leaf-identity` (L2>L1) edges, and the divfree `body-identity` (L3>L2) and `leaf-identity` (L2>L1) edges, are each discussed at the layers their slug names. The load-bearing asymmetry claim — the one fusion lives on the L2>L1 edge, the L3>L2 edge is pure identity — is stated about the correct edges (fusion at L2>L1 where kernel fusion lives; identity at L3>L2). No edge/prose mismatch.

**plan-kind-consistency — pass.** Declared shape is an observation-only verify-body audit (frontmatter `scope`, "Observation kind: Consistency drift / degenerate-cohort denominator correction"). Content matches: a classification audit emitting verdicts + a recommendation handed forward to cycle-051, with no artifact mutation. No firm/rough-in placeholder mismatch.

**skill-uptake-survey — warning (telemetry only, non-blocking).** The report's shape implies relevant procedures the audit could have referenced: the degenerate-lowering / vocabulary-shift smell classification is the kind of recurring procedure `cluster-friction-patterns` / the §1d degenerate-lowering treatment supports, and the §Caveat explicitly notes citecheck (`tools/citecheck/` / `verify-citation-range`) was NOT re-run on the L0 ranges, relying instead on the themes' authoring-cycle `--anchor` self-verification plus a direct body read. That is a defensible scoping decision for a body-structure verdict (and I independently confirmed the load-bearing cpp anchors), but the report references no skill invocation for either the classification or the citation spot-check. Surfacing as telemetry, not a defect.

### Issues found

1. **Minor citation line-number slips (severity: low, citation-validity).** Several artifact pinpoints cite a slightly wider/shifted range than the exact data row: `CYCLE.md:62` cites the jacobi-leaf rewrite table as `:102-107` (data rows are `104-107`; `102-103` is the header); `CYCLE.md:55-56` cites the jacobi `body-identity` table as `:110-112` (data row is `112`; `110-111` is the header). All land on the correct content within-range — no drift to a wrong location — so this is cosmetic, not a correctness problem. Candidate for a one-character repair if the repairer chooses to tighten ranges.

2. **Denominator-correction claim (18→17) is asserted but not independently cross-checked against the cycle-051 plan source (severity: low, cross-reference-integrity / consistency).** The report states the degenerate-cohort denominator drops from 18 to 17 and flags it for the cycle-051 plan and batch-15 meta-phase intake (`CYCLE.md:38`, `:120-121`, `:161-164`). The arithmetic follows correctly from this audit's own 3-of-4 verdict, but the report does not cite where the "18" originated (the cycle-049 D3 audit) with a file:lines pointer, so the −1 correction is internally consistent but not pinned to the artifact it corrects. Not a defect in the verdict; a forward-handoff item the cycle-051 integrator must reconcile.

3. **Citecheck not re-run on cited L0 ranges (severity: low, surfaced by the report itself).** §Caveat (`CYCLE.md:169-173`) discloses no fresh citecheck on the L0 ranges, relying on the themes' inherited `verified-against` self-verification plus a direct body read. I independently confirmed the three load-bearing cpp anchors (`divfree.cpp:185`, `:180-181`; `jacobi.cpp:38`) via the codemap, so the load-bearing path is sound. Recorded as transparency telemetry, not a blocking finding.

No high- or medium-severity issues. The load-bearing KEEP verdict on `divfree-projector-leaf-identity` is well-supported (real fusion rotation, correct anchors), the three DEMOTE-OK verdicts are correctly classified as degenerate (no vocabulary shift), the boundary-witness reasoning is sound, and observation-only / no-`book/`-mutation is confirmed.

## Repair

### Fixes attempted

- **Finding 1**: Minor citation line-number slips — jacobi-leaf table cited `:102-107` (data rows `104-107`, header `102-103`); jacobi `body-identity` table cited `:110-112` (data row `112`, header `110-111`).
  - **Decision**: repaired
  - **Action**: Tightened the pinpoints to the data rows in both the §"Specific finding" prose and the §"Supporting evidence" list of `CYCLE.md`. `jacobi-smoother-body-identity` table `:110-112` → `data row :112`; `jacobi-smoother-leaf-identity` table `:102-107` → `data rows :104-107`. Verified the data-row boundaries directly against `book/src/L3-L2/jacobi-smoother-body-identity.md` (table at `110-112`, header `110-111`, data row `112`) and `book/src/L2-L1/jacobi-smoother-leaf-identity.md` (table at `102-107`, header `102-103`, data rows `104-107`). Within-range/cosmetic — the verdict was unaffected. (Codemap/`tools/citecheck/ --anchor` not strictly needed for a within-file header-vs-body boundary; confirmed by direct read.) The divfree-leaf KEEP-verdict pinpoints (`:107-115` table, `:113` step-4 RE-FUSION row) and divfree body-identity pinpoints (`:91-100`, `:97`) were spot-checked and are already exact — left unchanged.

- **Finding 2**: 18→17 denominator correction internally consistent but not pinned to its cycle-049 D3 source.
  - **Decision**: repaired
  - **Action**: Added the file:lines pointer to the D3 worklist source in three places in `CYCLE.md` (§"Observation kind", §"Recommendation" denominator bullet, §"Open questions / caveats" denominator OQ): `reports/2026-06-01T190900Z-cross-layer-cross-cutter-refactor-pass-degenerate-lowering-audit/CYCLE.md:80-93` (§"(1c) SCOPE-BOUNDARY: the degenerate cohort is 18, not 12"), with the two verify-body-gated pairs at `:88` (divfree-projector) and `:92` (jacobi-smoother). Confirmed the "18" originates at that section by reading the D3 report. The −1 arithmetic stands as the report wrote it; the repair only pins its source for the cycle-051 forward handoff.

- **Finding 3**: skill-uptake-survey warning (telemetry only) + citecheck not re-run on L0 ranges (§Caveat, transparency).
  - **Decision**: not-needed
  - **Action**: none. Telemetry-only, non-blocking. The critic independently confirmed the three load-bearing cpp anchors (`divfree.cpp:185`, `:180-181`; `jacobi.cpp:38`) via the codemap; the load-bearing path is sound. No mechanical fix applies.

### Unrepairable findings

None. All three findings were low-severity; two were mechanically repairable (citation-pinpoint tightening, source-pointer addition) and one was telemetry-only requiring no action.

## Suggested resolution

`ready`. This is an observation-only verify-body audit with no `book/` mutation; all eight verdict checks pass and the load-bearing KEEP verdict on `divfree-projector-leaf-identity` (the one genuine L2>L1 fusion rotation in the projector chain) stands. Note for the cycle-051 integrator: the demotion-enactment denominator is **17, not 18** (the D3 source now carries an explicit pointer), and the divfree L3>L2 demotion must keep the L2 floor + L2>L1 fusion theme reachable so the one genuine rotation is not orphaned (per §Recommendation final bullet).
