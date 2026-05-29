---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T110803Z
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
repaired_at: 2026-05-29T111200Z
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

# META: verification of "Formalize nleps_jacobian_action at L1"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing `palace/linalg/nleps.cpp` anchor was verified verbatim against on-disk source via `read_range`. The whole `w = J·v` block reads exactly as cited: `:649` `// Compute w = J * v.`; `:650` `opA2p = (*funcA2)(std::abs(eig.imag()) * (1.0 + delta))`; `:651-652` the `denom = i·δ·|Im λ|`; `:653-654` the divided-difference `opAJ` build; `:655-656` the derivative pencil `opJ` with coefficients `{0, 1, 2λ, 1}`; `:657` `opJ->Mult(v, w)`; `:658` `if (k > 0)`; `:659-660` the deflation comment `w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 - T(l)XS^2 v2` (the source comment reads `XS`/`XS^2`, the prose correctly maps it to `S⁻¹`/`S⁻²` under the documented convention); `:661-662` the re-scoped value pencil `A`; `:663` `S = eig·I − H`; `:664` `Sv2 = S.fullPivLu().solve(v2)`; `:665-666` the two `MatVecMult(X, …)` back-projections (the second wrapping a second `fullPivLu().solve`); `:668-669` the two `AddMult` accumulations. The `δ = √ε` step at `:411-412` (comment "Delta used in to compute divided difference Jacobian" + `std::sqrt(std::numeric_limits<double>::epsilon())`) is exact. The consumer block `:673-675` (`u2_w0` + `delta_eig` dot) and `:676` (`z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)`) verify. The supporting anchors `:177-181` (SetExtraSystemMatrix closure), `:329-347` (MatVecMult real/imag split), `:354-362` (Effenberger 2013 / Jarlebring–Koskela–Mele 2018 / SLEPc-NEP), `:378` (`ComplexVector … w …` declaration), `:542` (`deflated_solve(c, c2, w0, w2)` — confirming `w0`/`w2` are the projection direction, not a Jacobian companion), and `:606-619` (deflation-basis growth: `:610-611` normalization, `:614` resize, `:615` `X[k]=v`, `:619` `k++`) all verify. Despite the batch-noted inline-anchor-drift friction, this report exhibits NO drift on any spot-checked load-bearing anchor. The cross-artifact citations also resolve: `apply_nonlinear_pencil.md:65` is exactly law 5 "Jacobian as derivative-pencil apply" (and it does record the `T'` construction as a deferred follow-up, as the report claims); `:111` is the evidence row citing the `:655` Jacobian build; `:98` is the firm-on-positive-structure status; `nleps_deflated_solve.md:145` is the inherited test-coverage caveat.

**surface-or-evidence — pass.** Not a refinement-shaped proposal; this is a new firm L1 operator entry (a `new:` chapter), not a modification of an existing operator/theme. The check is principally for retroactive-evidence-vs-surface framing on edits to existing surface. The two `edit:` blocks (index.md, SUMMARY.md) are additive registration rows for the new entry, not refinements of existing claims. Not applicable in the refinement sense; pass.

**rotation-quality — pass.** Not a cross-layer rotation proposal — this is an L1 operator formalization (mutation rotation already lifted; the explicit L1>L0 mutation-rotation theme is correctly deferred to the abstractor's domain, §Open questions). The L1-vs-L0 distinction section does state the rotation that landed: in-place destination buffer `w` + `A2n` line-search cache + build-form choice collapse to a pure-functional `w = nleps_jacobian_action(T, λ, P, v, v₂)`. That is a genuine state-hiding / build-form-erasure compression (more abstract at L1), not a 1:1 rename. Insofar as the check applies, pass.

**variant-axis-coverage — pass.** Two live variant axes are enumerated and each combination is addressed: **deflation-present** (`k = 0` bare derivative-pencil apply | `k > 0` with the product-rule coupling — gated by the `:658` `if (k > 0)` guard, both branches covered, `k = 0` pinned as law 1) and **damping-present** (`with-C` | `without-C`, absorbed by the bound pencil `T.C : Maybe LinearOperator`). Three axes are explicitly scoped out as collapsed-at-L1 with rationale: A2-representation (inherited opaque closure), finite-difference-`δ` + `A2n`-cache (load-bearing-numerical-constant / L1>L0 concern), and L0-build-form (`Mult`+2×`AddMult` vs single combined apply). No hidden branches: the `if (k > 0)` is the only conditional in the source block and it maps to the deflation axis. Pass.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: the in-chapter links `./apply_nonlinear_pencil.md`, `./nleps_deflated_residual.md`, `./nleps_deflated_solve.md`, `./lu_solve.md`, `./ksp_solve.md`, `./apply_linop.md`, `./eigsolve.md`, `../L2/linear_combination.md`, `../L0/eigensolver-wrapper.md` all exist; the new target `./nleps_jacobian_action.md` is correctly absent (created by this report). The index.md/SUMMARY.md insertion anchors are accurate: index.md line 31 is `**Firm (17)**`, line 49 is the `nleps_deflated_solve` cohort bullet, line 87 is the `nleps_deflated_solve` dep-map row (with `lanczos_step` at 88 as claimed); SUMMARY.md line 78 is exactly `- [nleps_deflated_solve](./L1/nleps_deflated_solve.md)`. **Build-readiness guard (firm-body-inside-fence): pass.** The report claims `firm`; its `## Status` + Signature + Algebraic-laws + Evidence apparatus is ENCLOSED inside the `new:book/src/L1/nleps_jacobian_action.md` fence (opens line 39, closes line 213) — the full firm body is the fenced chapter content, NOT authored as the report's own top-level sections outside the fence. This is the integration-proven structure of the cycle-023 `nleps_deflated_solve` sibling (which used the identical outer-`new:`-enclosing-nested-`text` pattern and integrated cleanly). Fence enumeration: 18 backtick fences total (even parity); the nested ` ```text ` blocks (52/68, 87/90, 94/108) sit inside the outer `new:` block and pair correctly, matching the sibling precedent. No cycle-019 fence-truncation signature. Pass.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (this is a single-layer L1 operator entry, not a lowering theme). The "derivative sibling / apply-vs-inverse-vs-derivative" framing relative to `nleps_deflated_residual` / `nleps_deflated_solve` is a same-layer relationship, correctly narrated as such. Not applicable to this report-kind; pass.

**plan-kind-consistency — pass.** Declared kind is a `firm` L1 operator entry; the content shape matches. The firm claim rests on the firm-on-positive-structure escape, and that escape is correctly invoked: (i) the structure is read from a single positive site (`:649-669`) with every constituent read-not-constructed; (ii) the laws (1-5) are syntactic operator-algebra identities — deflation-reduction is the `:658` branch, linearity is a fixed-`(λ,T,P)` composition of firm linear maps (`apply_nonlinear_pencil` law 1, `lu_solve` law 2, `linear_combination`), the product-rule coupling is the read `∂_λ S⁻¹ = −S⁻²` structure; (iii) the one non-syntactic point — the divided-difference `A2'` quasi-Newton approximation — is correctly recorded as an explicit **non-law** (not a gating unconfirmed law), so it does not pull the entry to `rough-in (test-coverage-bounded)` or `partly-constructive`. The distinction from the `eigsolve`-convergence-semantics situation is correctly drawn (the laws do not depend on convergence behaviour). The NLEPS no-dedicated-test caveat is correctly carried as inherited-and-non-gating. No rough-in placeholders in a firm entry. Pass.

**skill-uptake-survey — warning (non-blocking).** The report's shape implies several available skills whose invocation is not referenced. `verify-citation-range` is the obvious one given the batch's live inline-anchor-drift friction and the dense `:NN`-anchor evidence list (20+ single-line anchors) — the report describes its verification narratively in §Supporting evidence (read_range over `:640-700`/`:648-670`, `search_text` for `delta\s*=`) but does not name the skill. `classify-variant-axis` is implied by the two-axis + three-collapsed-axis enumeration. This is a pure presence-telemetry surface, not a content defect — the verification was clearly performed (and independently re-confirmed correct here); the skill names simply are not cited. Surfaced for telemetry.

### Issues found

No blocking issues. The report is citation-clean (verbatim-verified, no anchor drift), the firm decision is correctly grounded on the firm-on-positive-structure escape with the divided-difference `A2'` correctly demoted to a recorded non-law, the variant axes are covered, the cross-references resolve, and the firm body is correctly enclosed inside the proposed-changes fence (build-readiness guard passes). The following are minor / informational only:

1. **Frontmatter/body line-range discrepancy on the positive site (cosmetic).** `reports/.../CYCLE.md:10` (frontmatter `inputs`) cites the site as `palace/linalg/nleps.cpp:649-670`; the body (e.g. §Summary :19, §Status :169, §Evidence :184) consistently uses `:649-669`. On disk, `:669` is the last statement (`A->AddMult(XSSv2, w, -1.0);`) and `:670` is the closing `}` of the `if (k > 0)` block, so both are defensible (the frontmatter includes the closing brace). Not a correctness defect; purely a tidiness inconsistency between frontmatter and body. (CYCLE.md:10 vs :19/:169/:184.)

2. **Shared-file coordination is well-specified but carries an integrator-reconciliation dependency.** The index.md Firm-count bump is claimed as `17→18` here, with an explicit NOTE-for-integrator (§Index edits (1), CYCLE.md:223; §Open questions, :250) that the parallel `nleps_eigenvalue_correction` harvester also bumps additively and the integrator must reconcile to `17→19` if both land. The cohort bullet and dep-map row are anchored AFTER `nleps_deflated_solve` (this report) with the sibling anchoring after this entry — textually non-overlapping as required. This is correct per the established shared-file convention, but flagged so the integrator-per-report is aware the count cell is a known co-edit reconciliation point (not an overlap defect). (CYCLE.md:28, :223, :250.)

3. **skill-uptake (telemetry, non-blocking).** `verify-citation-range` and `classify-variant-axis` are implied by the report's shape but not named; verification was performed (narrated in §Supporting evidence) and independently confirmed correct. Surfaced per the skill-uptake-survey check; no action required. (CYCLE.md:237-242, §Supporting evidence.)

## Repair

### Fixes attempted

- **Finding**: Frontmatter/body line-range discrepancy on the positive site (cosmetic) — frontmatter `inputs` (CYCLE.md:10) cited `palace/linalg/nleps.cpp:649-670` (including the `:670` closing brace) while the body (§Summary :19, §Status :169, §Evidence :184) consistently uses `:649-669` (the last statement).
  - **Decision**: repaired
  - **Action**: Edited CYCLE.md:10 frontmatter `inputs` from `palace/linalg/nleps.cpp:649-670` → `palace/linalg/nleps.cpp:649-669`, harmonizing the frontmatter to the body's range (which ends on the last statement `:669` `A->AddMult(XSSv2, w, -1.0);` rather than the `:670` closing brace). Both ranges were critic-confirmed defensible; this is a small-offset citation-range tidy within repair authority (mechanical single-token edit; no content authored). The body range was already self-consistent across all three body sites and is the more precise of the two, so the frontmatter was moved to it.

- **Finding**: Shared-file coordination carries an integrator-reconciliation dependency — the index.md Firm-count bump is claimed `17→18` here with a NOTE-for-integrator that the parallel `nleps_eigenvalue_correction` harvester also bumps additively, requiring reconciliation to `17→19` if both land (CYCLE.md:28, :223, :250).
  - **Decision**: not-needed
  - **Rationale**: Critic flagged this explicitly as "an integrator-reconciliation point, not an overlap defect" and "not a repair" — it is correct per the established shared-file convention. The cohort bullet and dep-map row are textually non-overlapping (anchored after `nleps_deflated_solve`, with the sibling anchoring after this entry). No repair authority is exercised; the NOTE-for-integrator is left intact for `integrator-per-report` awareness. Surfaced in §Suggested resolution below for integrator visibility.

- **Finding**: skill-uptake-survey telemetry warning (non-blocking) — `verify-citation-range` and `classify-variant-axis` implied by the report's shape but not named.
  - **Decision**: not-needed
  - **Rationale**: Pure presence-telemetry, explicitly non-blocking. The critic confirmed the underlying verification was performed (narrated in §Supporting evidence) and independently re-confirmed it correct. No content or citation defect; nothing to repair surgically. The warning rides through as telemetry per the check's design.

### Unrepairable findings

None. The single actionable finding (the cosmetic line-range discrepancy) was within repair authority and is repaired; the other two findings were explicitly no-action (integrator-coordination note + non-blocking telemetry).

## Suggested resolution

`ready` for the integrator. Two notes for `integrator-per-report`:

1. **Firm-count co-edit reconciliation (carried from critic finding 2).** This report bumps `book/src/L1/index.md` Firm count `17→18`. The parallel `nleps_eigenvalue_correction` harvester (cycle-024) also bumps the same cell additively. If both reports land in the same batch, reconcile the count to `17→19` (the two cohort bullets and dep-map rows are non-overlapping and anchor sequentially after `nleps_deflated_solve`; only the single count cell needs the additive reconciliation). This is a known shared-file convention point, not a conflict.

2. The frontmatter `inputs` line-range was harmonized to `:649-669` (matching the body and the on-disk last statement); no other citation ranges were touched.
