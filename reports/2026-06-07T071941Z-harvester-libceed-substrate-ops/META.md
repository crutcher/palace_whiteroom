---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T084500Z
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

# META: verification of "Formalize the 4 libCEED contraction-substrate ops at L1 (cohort)"

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reports 19 ok / 0 failing (bounds + path hygiene clean). I anchor-verified every load-bearing pinpoint via `citecheck --anchor`: `restriction.cpp:389` `InitRestriction` [ok], `:200` `CeedElemRestrictionCreate` [ok]; `bilinearform.cpp:64-70` `trial_restr` [ok] (codemap read confirms `trial_restr`/`test_restr` at :64/:66 and `trial_basis`/`test_basis` at :68/:69, matching the row anchors); `integrator.cpp:25` `AddQFunctionActiveInputs` [ok]; `integrator.hpp:14-23` `EvalMode` [ok]; `basis.cpp:169` `InitBasis` [ok], `:15` `InitTensorBasis` [ok], `:35` `CeedBasisCreateTensorH1` [ok]; `integrator.cpp:340-419` `f_build_geom_factor_*` [ok, anchors at :352-377], `:423` `AssembleCeedOperator` [ok], `:451-512` `AddOperatorActiveInputFields` (at :492) [ok], `:215-308` `QuadratureDataAssembly` (at :220) [ok]. I additionally read the geom-factor build inputs (`integrator.cpp:384-398`) directly: the prose claims (`attr`/CEED_EVAL_INTERP, `q_w`/CEED_EVAL_WEIGHT, `grad_x`/CEED_EVAL_GRAD, `geom_data`/CEED_EVAL_NONE, `geom_data_size == 2 + space_dim*dim` MFEM_VERIFY contract) are all confirmed at source. The doubled-path convention (`reference/palace/palace/...` cited as `palace/...`) resolves correctly under citecheck. Every claim carries a pointer and every pointer is in-range and anchor-resolved.

**surface-or-evidence — pass.** This is a NEW-chapter cohort (4 `new:` blocks), all rank-0 `roadmap_goal`. A `roadmap_goal` makes no firm claim, so the surface/evidence bar is the graded-stack reachability + grounding bar, which is met: each carries intent (one-line role), pulled-by provenance (→ `libceed-quadrature-kernel-impl`), declared deps, accreting constructive sketch, AND a cited `## Verified-against` evidence block (the disposition is honest: the *decomposition* is read off Palace source, only the *existence of firm L1 substrate* is speculative). Record-definition sub-check: the signature-named types (`ElemRestriction`/`Basis` = opaque libCEED handles, used opaquely; `BasisMode` = the `EvalMode` enum, pinned in-line and source-cited; `GeomData` = `Tensor[(E,P,G)]`, defined in-line in `geom_factor_build`) are appropriately handled at rank-0, and the report explicitly flags `record-element-local-tensor-needs-definition-home-at-firming` for the firm flip — correct deferral, not a gap.

**rotation-quality — pass (not a rotation claim — no-op).** This cohort asserts no L_{n+1}→L_n rotation; it formalizes 4 same-layer L1 substrate ops at rank-0. The named-shape-group machinery (`Tensor[(E,L)]` etc.) is the vocabulary the consumer's pipeline rests on, not a compaction claim over a lower form. No rotation to grade; marked pass per "inapplicable to this report-kind."

**variant-axis-coverage — pass.** The relevant orthogonal axes are addressed, not hidden: the de-Rham family axis (H1/Hcurl/Hdiv/L2 via `CeedBasisCreateH1`/`Hcurl`/`Hdiv`) and the EvalMode axis (`Interp`/`Grad`/`Curl`/`Div`) are enumerated in `basis_apply`; the lexicographic-vs-native restriction ordering is explicitly scoped as an interior index-map detail; the oriented (sign-carrying H(curl)/H(div)) restriction variant is cited (`CeedElemRestrictionCreateOriented`); the tensor-vs-non-tensor basis path is named; the build vs run-time stratum split (geom_factor_build vs quad_point_contract) is explicit; and the single-machine / cross-rank scatter-add boundary is scoped out per DIRECTIVE-1. No hidden branch.

**cross-reference-integrity — pass.** All cross-ref targets resolve on disk: `libceed-quadrature-kernel-impl.md`, `weak_form_term.md`, `elementwise_product.md`, `fe_assemble.md` (L1/), `fe-assemble-libceed-boundary-obstruction.md` (L1-L0/), and concepts `tensor-field-lift.md` + `build-time-vs-run-time-stratification.md` all exist. The 4 new chapters mutually inter-link (G→B→D, geom_factor_build→quad_point_contract) consistently. The SUMMARY.md insertion anchor (line 230) and both index.md edit anchors (the line-99 kernel-impl bullet, the line-176 dep-map row) exist and match. NOTE (not a defect): the first dep-map `edit:` block (CYCLE.md:486) reproduces existing index.md row 176 verbatim — it is a no-op anchor for the 4 appended rows, so the row's pre-existing "(rough-in roadmap-deps; NOT firm yet)" phrasing is preserved unchanged; the producer flags this loose phrasing as stale and defers its re-anchoring to D6 (same-file collision avoidance), which is a deliberate flagged deferral.

**edge-label-fidelity — pass.** No L_{n+1}→L_n lowering edge label is carried; all edges are same-layer `reference`/`pulled-by` (consumer↔substrate) plus concept references. Each `pulled-by` edge's prose accurately describes the pipeline stage it names (G/Gᵀ for element_restrict, B/Bᵀ for basis_apply, D for quad_point_contract, the build-pass feeding D for geom_factor_build) — labels match prose throughout.

**plan-kind-consistency — pass.** Declared kind is rank-0 `roadmap_goal` (×4) and the content shape matches: claim-free placeholders with constructive sketches, laws explicitly marked "sketch — to be confirmed at promotion" (NOT asserted firm), Status sections stating the clean-gate ROADMAP_GOAL justification + promotion route. No firm apparatus masquerading at rank-0 and no firm claim leaking in. Rank-invariant: the consumer correctly STAYS `roadmap_goal` (rank-0 ≤ rank-0, vacuous) — no over-claim above a dep's rank. Reachability: each node is pulled-by the consumer, which reaches the feature root via the fe_assemble fold — live, not garbage. The disposition judgment ("none forced firm") is sound on independent review: the firm L1 algebra is flat-vector BLAS over `Tensor[N]`, and all 4 ops fundamentally require the `[E,L]`/`[E,P,C]`/`[E,P,G]` element/quad-point rank structure that no firm op carries; the closest call (`quad_point_contract`, whose pointwise `⊙` IS firm as `elementwise_product`) is correctly kept rank-0 because elementwise_product is firm only over flat `Tensor[N]` and the `[E,P,C]` diagonal lift is the genuine substrate gap. The sum-factorization classification as a transparent performance trick is correct: `InitTensorBasis`/`CeedBasisCreateTensorH1` factors the dense per-element basis contraction into 1-D contractions — algebraically equivalent, changing only contraction order — matching CLAUDE.md §Optimization-tricks (one-line note, not a separate algebraic claim).

**skill-uptake-survey — pass.** The report references its citation-verification tooling explicitly (`palace-codemap read_range` + `citecheck.py --anchor`, §Supporting evidence), the governing semantic surface (`l4_calculus.md §1.2.1` named shape groups, USE+LINK not restate), and the resolved OQ for the sum-factorization classification. Telemetry surfaces the relevant procedural uptake; nothing missing for this report-kind.

### Issues found

None. All 8 checks pass. The cohort is a clean rank-0 `roadmap_goal` formalization: citations fully anchor-verified at source, the roadmap_goal disposition is independently honest for all four (none cleanly firmable in flat-vector-BLAS L1 vocabulary), the named-shape-group rank structure is correctly load-bearing, well-foundedness holds (consumer stays roadmap_goal), the sum-factorization-as-transparent-trick call is correct, and all cross-references + edit anchors resolve. Producer-flagged deferrals (the consumer's stale dep-edge NOTE comment re-anchoring → D6; the `record-element-local-tensor-needs-definition-home-at-firming` flag → firm flip) are deliberate and appropriately routed, not critic defects.
