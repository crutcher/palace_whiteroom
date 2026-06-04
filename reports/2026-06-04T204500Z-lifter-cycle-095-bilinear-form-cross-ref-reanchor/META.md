---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T211546Z
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
overall_status: ready
---

# META: verification of "Re-anchor — bilinear-form firm-flip whole-book cross-reference sweep"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck --scan` on the report: **19 ok, 0 failing**. I additionally spot-verified every `[old]` block against on-disk content at the cited line: `L2/inner_product.md:178-180`, `L2/index.md:89`, `L2-L1/index.md:17/:19`, `L2-L1/inner-product-fold-specialization.md:366`, `L2-L1/gram-fold-specialization.md` leaf-list, `L3/inner_product.md:164`, `L3/index.md:91`, `L0/linalg-operator-file.md:73`, `L1-L0/dot-mutation-rotation.md:305`, `L1-L0/bilinear-form-mutation-rotation.md:4/:31/:569`, `L1-L0/index.md:28`, `L1/blas1-elementwise-intro.md:7`, `L1/matrix-weighted-norm.md:124`. Every `[old]` text matches the file exactly at the cited line. No drift. No `verified_against:` YAML block is emitted by this report (it is a maturity-label re-anchor, not a lowering audit), so that sub-check no-ops.

**surface-or-evidence — pass.** This is a pure maturity-label re-anchoring pass coupled to the D1 firm-flip — every edit propagates the `rough-in`→`firm` token downstream of the operator's own promotion (which lands in D1, not here). No new per-operator algebraic claim is made; the evidence is the D1 flip (citing `bilinear-form.md:321` §Status + the c092 DISCHARGE) plus the firm-on-positive-structure escape precedent chain, both cited in §Supporting evidence. This is the explicitly-allowed downstream-of-promotion propagation shape, not a surface change requiring its own rotation_claim. The bilinear-form record/signature is unchanged by the flip (stated in Discipline notes), so the record-definition sub-check is not triggered.

**rotation-quality — pass (not applicable to maturity-re-anchor kind).** The report asserts no algebraic/structural/reduction rotation — it changes maturity tokens only, with no LHS/RHS shape, decomposition, or signature touched. No rotation_claim to grade.

**variant-axis-coverage — pass (not applicable).** No operator/theme variant axes are introduced or modified; the bilinear-form variant axes (Hermitian/non-Hermitian `M`, real/complex element-type) live in the D1-owned operator entry, untouched here.

**cross-reference-integrity — pass (load-bearing for this report; verified by independent grep).** I re-ran `grep -rn 'bilinear-form' book/src | grep -i 'rough-in'` and audited every surviving hit against dispatch ownership. **No genuine "bilinear-form is rough-in" maturity narration survives inside D2's scope.** Every surviving rough-in co-mention falls into one of: (a) a file owned by another dispatch — `L1/index.md:67/:101/:113` (D1), `feature/*.{L1,L4}.md` + `feature/index.md:55/:68/:69` (D4/D5), `L4/gram_reduce.md:7/:198/:251` (D3), `L4/domain_energy_reduce.md:311` (D3 — the planner explicitly assigns `domain_energy_reduce` to D3), `methodology/goal-flow.md:263` + `methodology/resolution-ladder.md:132` (meta-phase); (b) a non-maturity hit D2 correctly enumerated as left-untouched and which I verified is genuinely a nav-link / forward-ref / slug-collision: `L2/gram.md:244`, `L2/dot.md:57`, `L2/folds-intro.md:14`, `L0/mpi-globalsum-and-collectives.md:119`, `L0/linalg-operator-file.md:88`, `L1-L0/index.md:52` (the `bilinearform.cpp` FE `BilinearForm`-class slug-collision — a different object). All 13 edited cross-refs resolve to real chapters (verified the link targets exist on disk). I confirmed the **planner-listed-but-not-edited** files (`L2/gram.md`, `L2/dot.md`, `L2/folds-intro.md`, `L0/mpi-globalsum-and-collectives.md`) carry only nav-links — D2 was correct to leave them, this is not a missed edit. The `L1-L0/matrix-weighted-norm-mutation-rotation.md:317` hit (which the planner DID list for D2) is a **matrix-weighted-norm** maturity drift, not a bilinear-form one ("operator (rough-in, test-coverage-bounded)" refers to mwn); D2 correctly found no bilinear-form maturity claim there and flagged the residual mwn drift as adjacent OQ-intake rather than silently editing it.

**edge-label-fidelity — pass (the HARD constraint, verified on disk).** D2's hard constraint is to NOT touch any L1-L0 (or L2-L1) theme's OWN `## Status` VERDICT, re-anchoring only references to the operator's maturity. I verified on disk: `bilinear-form-mutation-rotation.md:550` reads `firm` and is not among the edits; `inner-product-fold-specialization.md:456` reads `firm` and is not edited; `gram-fold-specialization.md:388` reads `firm` and is not edited. The edits to those theme files touch only the leaf-list / Verified-against / caveat / intro / upstream-note prose — all references to the OPERATOR's maturity, not the theme's status. The `bilinear-form-mutation-rotation.md:569` "Note on the upstream L1 gate" re-anchor is correctly a reference-to-operator-maturity edit (it narrated the operator as rough-in), distinct from the theme's own firm verdict. Constraint satisfied.

**plan-kind-consistency — pass.** The report is shaped as a coupled cross-reference re-anchor (lifter kind): 13 maturity-label edits, no structural authoring, explicit "no structural rewrites" discipline note, and a clean routing of out-of-scope sites. Content shape matches a lifter re-anchor pass exactly.

**skill-uptake-survey — pass (telemetry).** The report invokes the `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` discipline by name and follows the batch-29 mwn-cascade precedent it cites as the model. The implied procedure (whole-book grep + genuine-maturity-claim test per hit) is referenced and executed. No missing skill reference.

### Issues found

None blocking. All 8 checks pass. The report is a clean, well-scoped maturity re-anchor.

Two observations recorded as telemetry (NOT issues against this report — both correctly handled or out-of-scope):

1. **Out-of-scope routing is correct and complete.** D2 flagged exactly the right four out-of-scope stale sites for coordination/OQ-intake: `methodology/goal-flow.md:263` + `methodology/resolution-ladder.md:130-136` (meta-phase-owned; the actual hit is at `:132`), `L4/index.md:101` (D3 gram_reduce row), `L4/solve_family.md:154` (D3/D4 coordination). Per the task's specific concern, `resolution-ladder.md` was authored THIS batch (c094) and its worked rank-ladder example uses bilinear-form rough-in — D2 correctly identified it as becoming stale on this cycle's flip and routed it to the batch-30 meta-phase rather than editing the meta-owned page. The forward-looking illustration at `:132` ("the off-diagonal `bilinear-form` primitive, which is still `rough-in`") is exactly the stale narration D2 flagged. This is the correct disposition.

2. **One adjacent stale site outside the bilinear-form cascade entirely:** `L1-L0/matrix-weighted-norm-mutation-rotation.md:317` carries a `matrix-weighted-norm` rough-in drift (a residue the c091 mwn cascade missed). The planner had listed this file in D2's scope (for the bilinear-form re-anchor), and D2 correctly determined there is no bilinear-form maturity claim in it and flagged the mwn drift as OQ-intake for a separate mwn land-clean follow-up. Correctly out of this dispatch's scope; noted only so the downstream mwn residue is not lost.
