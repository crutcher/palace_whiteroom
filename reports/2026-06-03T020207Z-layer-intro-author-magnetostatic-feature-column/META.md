---
verifies: ../REPORT.md
critiqued_at: 2026-06-03T02:08:26Z
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
repaired_at: 2026-06-03T02:12:00Z
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

# META: verification of "magnetostatic feature column (L4 + L1 + L0)"

## Critique

This report authors the 2nd instance of the **feature-surface composition-root chapter kind** (FEATURE-SURFACE SPINE directive, 2026-06-02). The adapted-check framing is applied (per the report's own §Critic-framing note and the c070 electrostatic exemplar precedent): surface-or-evidence ADAPTS (evidence = L0 driver range + constituent down-links), rotation-quality + variant-axis-coverage NO-OP (a composition root makes no rotation/variant claim), cross-reference-integrity is load-bearing.

### Checks run

**citation-validity — pass.** Verified every L0 anchor against `palace/drivers/magnetostaticsolver.{cpp,hpp}` via codemap `read_range`. All land exactly: `Solve` sig `:22` (return type `:21`), body `:22-108`; `curlcurl_op` `:28`; `GetStiffnessMatrix()` `:29`; `GetCurlMatrix()` `:30`; `KspSolver` `:34`; `SetOperators(*K,*K)` `:35`; `post_op` `:39`; `n_step` `:40`; `MFEM_VERIFY` `:41-42`; `Vector RHS/B` `:46`; `A(n_step)` `:47`; `I_inc(n_step)` `:48`; loop `:66`; `GetExcitationVector` `:76`; `ksp.Mult` `:77`; `Curl.Mult(...B)` `:85`; `GetExcitationCurrent` `:88`; `MeasureAndPrintAll` `:91`; `step++` `:99`; `PostprocessTerminals` call `:108`, def `:110`. Inside `PostprocessTerminals`: `DenseMatrix M(A.size())` `:122`; diagonal `M_mag->Mult` `:129` + `Dot/(I_inc[i]²)` `:130-131`; off-diagonal `:135-138`; `Minv(M); Minv.Invert()` `:151-152`; COMSOL comment `:115-121`. hpp class decl `:24-39` (class line at `:25`, `PostprocessTerminals` decl `:28-31`, `Solve` override `:33-34`). NO drift in this report's own citations — notably the report cites the correct on-disk `:29/:34/:35` for the assemble/solver-build/capture sites, sidestepping the +1 drift that lives in `solve_family.md` (see cross-reference note). The c070 electrostatic column's 1-3 line anchor drifts did NOT recur here.

**surface-or-evidence — pass (adapted).** Applying the feature-surface-kind adaptation: the chapters carry the *compositional* claim (magnetostatic = `inductance_reduce ∘ solve_family ∘ fe_assemble`), evidenced by (a) the L0 driver range `magnetostaticsolver.cpp:22-108` + `:110-204` realizing the composition, and (b) the constituent-op down-links to firm/rough-in chapters. Both halves are present and verified. There is no single decomposed-op source site to demand here; the per-op algebraic claims correctly live in the linked chapters, not restated. Composition faithfulness confirmed against source: `K` assembled once `:29` then `SetOperators` `:35` OUTSIDE the `:66` loop (the fixed-operator `solve_family` `fixed` corner, 2nd witness — matches source); inductance reduction `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` matches the `PostprocessTerminals` source comment + the `M(i,j) = Dot(...)/(I_inc[i]*I_inc[j])` body exactly; diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²` matches.

**rotation-quality — pass (no-op).** Not applicable to the feature-surface kind: a composition root introduces no algebraic/structural/reduction rotation — it wires existing firm vocabulary. The report correctly asserts no rotation claim. No mis-flag.

**variant-axis-coverage — pass (no-op).** Not applicable to the feature-surface kind: the composition root introduces no new variant axis; the variant axes (operator-capture fixed/per-element, family-index domain, element-type) are owned and covered by the linked `solve_family` chapter, where magnetostatic is correctly placed on the `fixed` / `surface-current-boundary` / `real` corner. No hidden branch.

**cross-reference-integrity — pass (load-bearing).** All down-links resolve to on-disk chapters and the labeled firmness matches each target's on-disk `## Status` line exactly: `L4/fe_assemble` firm ✓, `L4/solve_family` rough-in (test-coverage-bounded) ✓, `L4/ksp_solve` firm ✓, `L1/fe_assemble` firm ✓, `L1/ksp_solve` firm ✓, `L1/matrix-weighted-norm` rough-in (test-coverage-bounded) ✓ (CORRECTLY labeled — the electrostatic column's initial firm mislabel did NOT recur), `L1/bilinear-form` rough-in (lower-layer-shared-vocabulary) ✓. The 2nd-witness cross-reference into `solve_family.md` resolves: line 109 (§Specializations "Magnetostatic surface-current sweep" bullet — the report's "around `:113`") names the magnetostatic sibling, and `:137` (the load-bearing `operator-capture` axis) names magnetostatic as a `fixed` witness — both real. Index/SUMMARY ownership coherent: `feature/index.md` matrix + both `edit:` `[old]` anchors match on-disk (matrix header line 18, status paragraph line 32); SUMMARY `[old]` block matches lines 7-11; D2's lifecycle rows wired by the exact slug `feature/lifecycle.{L4,L1,L0}.md`; within-column ordering L4→L1→L0 (high→low, not alphabetized); no by-kind nesting (small-Part guard honored).

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label carried (these are same-level feature chapters linking down to constituent ops, not lowering themes). The L0→L1→L4 lift prose discusses the correct directions. Not applicable in the lowering-edge sense; no mismatch.

**plan-kind-consistency — pass.** Declared kind `feature-surface` / `status: seed` matches the content shape: a composition-root that composes firm+rough-in vocabulary with no new algebraic claim. `seed` is the appropriate maturity tier (stage-3 reduction rests on rough-in L1 primitives, so not promotable past `seed` — the report reasons this correctly). No firm-with-placeholders mis-classification.

**skill-uptake-survey — pass.** The report references its localization procedure (codemap `read_range` for every L0 anchor, explicitly re-confirmed on-disk rather than trusted from the planner scope or the drifted `solve_family.md` note) — the appropriate citation-verification discipline for this shape. Telemetry only; no blocking.

### Issues found

No defects in this report. Two items are correctly ROUTED OUT (not defects in this report's surface):

1. **(Not this report's defect — well-routed finding) Pre-existing +1 anchor drift in `book/src/L4/solve_family.md` §Specializations.** Confirmed on-disk: `solve_family.md:109` cites `GetStiffnessMatrix() (:30)`, `KspSolver ksp(...) (:35)`, `ksp.SetOperators(*K,*K) (:36)`; the on-disk sites are `:29/:34/:35` (the `:60`/`:66`-region loop anchors `:47/:66/:76/:77/:99` in that note are correct). The electrostatic note in the same file shares the off-by-one (e.g. line 58 cites magnetostatic `:36` for SetOperators). This report's own feature chapters cite the correct `:29/:34/:35`. The report flags this in Open question 1 and recommends a lifter/repairer re-anchor pass — correct routing; it is a finding about another file, in scope for a follow-up dispatch, not a flaw to repair in this report.

2. **(Well-routed forward findings, not defects.)** Open question 2 (the 2-witness `gram_reduce`/`energy_reduce` L4 combinator-mine candidate — electrostatic capacitance + magnetostatic inductance share the `Xⱼᵀ K Xᵢ` map-then-reduce shape modulo the scalar normalization; meets the ≥2-witness mining gate) is a correctly-surfaced combinator-miner / cycle-planner item. Open question 4 (the `status: seed` vs `seed (exemplar)` token-uniformity question) is a correctly-surfaced meta-phase normalization item. Both are routed to the right consumers and explicitly NOT authored here (one feature column per dispatch); they are well-routed, not defects.

### Note on overall disposition

All 8 checks pass under the feature-surface-kind adaptation. The report is a clean near-mechanical mirror of the c070 electrostatic exemplar with the citation-drift and firmness-label defects of that exemplar NOT recurring (both were honored at authoring time). The repairer's fix-surface here is empty; the two routed-out findings are follow-up dispatches, not repairs to this report.

## Repair

### Fixes attempted

All 8 critic checks returned `pass` with no defects flagged in this report's own surface. There is nothing mechanical to repair.

- **Finding**: citation-validity — every L0 anchor against `magnetostaticsolver.{cpp,hpp}` lands exactly; report cites correct on-disk `:29/:34/:35` (no +1 drift in this report).
  - **Decision**: not-needed (check passed)
- **Finding**: surface-or-evidence (adapted) — compositional claim evidenced by L0 driver range + constituent down-links; both halves present and verified.
  - **Decision**: not-needed (check passed)
- **Finding**: rotation-quality — no-op for the feature-surface kind; no rotation claim made, no mis-flag.
  - **Decision**: not-needed (check passed)
- **Finding**: variant-axis-coverage — no-op for the feature-surface kind; axes owned by the linked `solve_family` chapter.
  - **Decision**: not-needed (check passed)
- **Finding**: cross-reference-integrity — all down-links resolve and labeled firmness matches on-disk `## Status` exactly (incl. `matrix-weighted-norm` correctly rough-in); SUMMARY/index `[old]` anchors match.
  - **Decision**: not-needed (check passed)
- **Finding**: edge-label-fidelity — no lowering-edge label carried; lift-direction prose correct.
  - **Decision**: not-needed (check passed)
- **Finding**: plan-kind-consistency — declared `feature-surface` / `seed` matches the composition-root shape; `seed` maturity correctly reasoned.
  - **Decision**: not-needed (check passed)
- **Finding**: skill-uptake-survey — telemetry only; appropriate citation-verification discipline referenced.
  - **Decision**: not-needed (check passed)

### Unrepairable findings

None. The two routed-out items are correctly-routed follow-up dispatches, not defects in this report, and are intentionally left in the report's Open-questions section:

1. **Pre-existing +1 anchor drift in `book/src/L4/solve_family.md` §Specializations** (`:30/:35/:36` should be `:29/:34/:35`). This is a finding about ANOTHER file, routed via the report's Open question 1 for a follow-up lifter/repair pass. This report's own citations use the correct on-disk numbers, so there is nothing to repair here. Left as the routed OQ.
2. **Forward findings** — Open question 2 (the 2-witness `gram_reduce`/`energy_reduce` L4 combinator-mine candidate) routes to combinator-miner / cycle-planner; Open question 4 (`seed` vs `seed (exemplar)` status-token uniformity) routes to meta-phase. Both correctly surfaced and explicitly not authored here. Left as the routed OQs.

## Suggested resolution

`ready`. No repairs applied; `book/` and the report's proposed-changes are untouched. The integrator may apply this report's proposed-changes as-is. The routed-out items (solve_family.md re-anchor; `gram_reduce` mine; status-token normalization) are separate follow-up dispatches, not preconditions for integrating this clean magnetostatic feature column.
