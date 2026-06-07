---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T114310Z
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
repaired_at: 2026-06-07T120000Z
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

# META: verification of "Formalize element_restrict + geom_factor_build at L1" (cycle-124 D4)

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck --scan` (8 ok / 2 "failing" — both `[AMBIG]` basename-only, `integrator.cpp`/`integrator.hpp` matching `fem/` and `fem/libceed/`; the report prose consistently uses the full `palace/fem/libceed/...` path, so these are not real drift) and `--anchor` on every load-bearing pinpoint. All 16 anchors verify on-disk: `restriction.cpp` `InitRestriction` 389-426 (END 426 = the function's closing brace; line 425 is the inner `}` — the `:425→:426` END off-by-one correction is correct), `CeedElemRestrictionCreate :200`, oriented `:192`/`:372`, lexico `:113`, native `:207`; `bilinearform.cpp:64-70` (`trial_restr :64`/`test_restr :66`); `integrator.cpp` `AssembleCeedGeometryData` 335-421 (END 421 = closing brace; the prior `:340-419` did truncate both ends), `switch :348`, `attr :387`, `q_w :388`, `grad_x :389-390`, `MFEM_VERIFY :395`, `geom_data` output 397-398 (397 = `CeedQFunctionAddOutput(..."geom_data"...)`, 398 = `CEED_EVAL_NONE`), `AssembleCeedOperator :423`, geom_data field-set 483-484 (`CeedOperatorSetField(..."geom_data"...)`); `integrator.hpp:14-23` (`enum EvalMode`). Every drift correction the report claims is real and lands on the right line. No `verified_against:` YAML block in this report (the *Verified-against* sections are prose, not a fenced YAML payload), so that sub-check no-ops.

**surface-or-evidence — pass.** This is a roadmap_goal→rough-in promotion of two existing operator chapters: it modifies surface (full `## Status` / `## L1 form` / `## Algebraic laws` rewrites) AND carries exhaustive positive-source evidence (the *Verified-against* ranges). Record-definition sub-check: the signatures name `ElemRestriction`, `MeshNodes`, `QuadWeights`, and the `Tensor[(E, L)]` / `Tensor[(E, P, G)]` element-local rank tensors. The rank-tensor shape carrier's definition home is `concepts/element-local-tensor` (the `depends-on` shape-vocabulary edge), which the report explicitly routes to D5 and flags in Open questions — so it is a flagged-and-routed record, not an undefined "described only by USE" gap. `ElemRestriction`/`MeshNodes`/`QuadWeights` are thin opaque handle/field types (libCEED/MFEM-owned, not project record types carrying field structure), consistent with how the existing roadmap_goal chapters and the broader L1 vocabulary treat them; no in-chapter record section is owed for them at this maturity. No record gap.

**rotation-quality — pass.** Not a lowering/rotation proposal — it is a within-layer maturity promotion (rank 0 → rank 2) of two L1 operators. The check is structural here: the rough-in disposition is the honest well-foundedness outcome (capped at the to-be-firm shape home's maturity), the structural decomposition is exhaustively cited, and the laws are stated as syntactic identities on positive source. No 1:1 rename masquerading as a rotation. Applicable-but-satisfied.

**variant-axis-coverage — pass.** The variant axes present (lexicographic vs native restriction ordering `InitLexicoRestr`/`InitNativeRestr`; oriented vs unoriented restriction for H(curl)/H(div); the `𝒟`-determined metric form `|J|·w` vs `J⁻ᵀJ⁻¹|J|·w`; the `(dim, space_dim)` QFunction dispatch) are each acknowledged and correctly scoped as interior index-map / build-QFunction details. The single-machine / multi-rank shared-dof axis is explicitly scoped out (Applicability condition 2 / the DIRECTIVE-1 boundary). No hidden branch.

**cross-reference-integrity — warning.** Most references resolve: `book/src/semantics/index.md` §1.2.1 exists (the live named-shape-groups surface; the stale `book/src/design/l4_calculus.md` §1.2.1 path is genuinely on-disk in both chapters today, so the re-point is a real fix, correctly applied USE+LINK not restated), `concepts/tensor-field-lift.md`, `concepts/build-time-vs-run-time-stratification.md`, and all linked L1 chapters (`libceed-quadrature-kernel-impl`, `basis_apply`, `quad_point_contract`, `weak_form_term`, `fe_assemble` via the consumer) exist; the index member-bullet + dep-map table-row edit targets all match on-disk lines (103/106/188/191). **The single unresolved reference is the load-bearing one:** `concepts/element-local-tensor` does NOT exist on disk — it is the D5-authored forward-reference. The report handles it correctly per the forward-reference-must-be-plain-text rule (plain inline-code span in prose, NOT a live markdown link — verified: the only `[...]( )` links in the edit blocks are to `element_restrict.md`/`geom_factor_build.md`/`libceed-quadrature-kernel-impl.md`, never to `element-local-tensor`; the `depends-on` frontmatter target is the bare slug the linter reads) and flags it in Open questions. Reachability (#10) holds: `pulled-by libceed-quadrature-kernel-impl` → `realizes-leaf fe_assemble` (firm, reaches the feature root via its feature-column inbound edges). The warning is that, at critique time, the chapter's sole `depends-on` edge resolves to a not-yet-existent file — its on-disk landing (and thus the maturity coupling below) depends entirely on D5 succeeding this wave.

**edge-label-fidelity — pass.** The `depends-on (shape-vocabulary)` edge to `concepts/element-local-tensor` is correctly typed and the prose discusses exactly that edge (the element-local rank-tensor shape home the signature contracts over). The `reference`/`pulled-by` edge to `libceed-quadrature-kernel-impl` and the `reference` edges to `concepts/tensor-field-lift` / `concepts/build-time-vs-run-time-stratification` are correctly classed as free navigational (`reference`), matching the prose ("this node does not depend on its consumer"). Edge classes and prose agree.

**plan-kind-consistency — pass.** Declared kind is rough-in (rank 2), and the content matches: structurally-anchored decomposition with syntactic-identity laws stated as rough-in, an explicit firm-promotion route (the firm-on-positive-structure escape, gated only on the shape home firming), and an honest well-foundedness cap (rough-in may rest on a to-be-firm dep; firm may not). This is precisely the one-rank honest climb from roadmap_goal the rough-in tier is for — no firm-claim-with-placeholders mis-classification, and the report pre-empts the "rough-in = failed promotion" misread for the integrator.

**skill-uptake-survey — pass.** The citation-drift-correction shape implies the citecheck `--anchor` workflow; the report states "All anchors citecheck-verified on-disk (`--anchor` pass, 16/16 clean)" — the relevant tooling is referenced. Telemetry only.

### Issues found

1. **`concepts/element-local-tensor` is an unresolved forward-reference (cross-reference-integrity, warning).** `reports/.../CYCLE.md` — both chapter frontmatters (`depends-on` edge) + prose + both index table rows. The file does not exist on disk at critique time; it is the D5-authored shape-vocabulary home this wave. The report handles it correctly (plain inline-code, bare-slug edge target, Open-questions flag), so this is not a defect in *this* report's authoring — it is an intra-wave cross-report dependency the integrator must reconcile in dispatch order (D5 before / alongside D4, or this report's `depends-on` edge lands as a dangling slug + the prose inline-code resolves to nothing until D5 lands). If D5 does not land `concepts/element-local-tensor` this wave, the rough-in promotion is left resting on a non-existent dep. Severity: medium — wholly contingent on D5; no independent fix available to this report.

2. **Rank-invariant (#9) cannot be mechanically confirmed at critique time (coupled to issue 1).** The chapters claim rough-in (rank 2) with a sole `depends-on` edge to `concepts/element-local-tensor`, whose rank is undefined on disk. The well-foundedness invariant `rank(u) ≤ rank(dep)` is *satisfiable* (holds iff D5 lands the page at ≥ rough-in, which the report assumes — "to-be-firm shape home") and the report's reasoning is internally consistent and honestly capped. But it is unverifiable until D5's page exists with a declared rank. If D5 were to land the page below rough-in (stub/roadmap_goal), these two would over-claim. Severity: low — the report's cap is the conservative choice and explicitly defers firm; flagging for the integrator to confirm the D5 page's landed rank is ≥ 2 before treating these as cleanly rough-in.

3. **Stale-semantic-path drift sweep candidate (not a defect in this report; flagged by the report itself for meta-phase).** The report notes the `design/l4_calculus.md §1.2.1 → semantics/index.md §1.2.1` move (batch-37) likely left the same stale path in other batch-37-era files beyond the four libceed-substrate chapters. Confirmed in-scope here (both target chapters currently carry the stale path on-disk; the edits fix them). This is a correct drive-by observation for a meta-phase semantic-surface drift sweep — no action owed by this report. Severity: informational.

## Repair

### Fixes attempted

- **Finding**: `concepts/element-local-tensor` is an unresolved forward-reference (cross-reference-integrity, warning) — the sole `depends-on (shape-vocabulary)` edge resolves to a D5-authored page not on disk at critique time; rank-invariant (#9) unverifiable until D5 lands.
  - **Decision**: not-needed (no content edit; contingent ordering note now satisfied).
  - **Rationale**: This is not a defect in *this* report's authoring — the critic confirmed the report handles the forward-reference correctly (plain inline-code span, bare-slug `depends-on` target the linter reads, Open-questions flag). The warning is wholly contingent on D5 succeeding this wave; no independent fix is available to D4. Verified D5 DID land the page firm this wave: `reports/2026-06-07T112037Z-layer-intro-author-element-local-tensor/CYCLE.md` authors `book/src/concepts/element-local-tensor.md` as a `record`-kind page at rank `firm`, slug exactly `concepts/element-local-tensor` (matches D4's `depends-on` edge target verbatim). With D5's page at rank firm ≥ rough-in (rank 2), the well-foundedness invariant `rank(u) ≤ rank(dep)` holds — the rough-in promotion rests on a firm shape home. No content edit owed; recorded as an integrator dispatch-ordering note.

- **Finding**: Rank-invariant (#9) cannot be mechanically confirmed at critique time (coupled to issue 1), severity low.
  - **Decision**: not-needed (resolved by the D5 confirmation above).
  - **Rationale**: D5's `concepts/element-local-tensor.md` lands at rank `firm`, which is ≥ rough-in (2), so the rank cap is satisfied — the chapters' rough-in does NOT over-claim. No edit; same integrator ordering note covers it.

- **Finding**: Stale-semantic-path drift sweep candidate (informational; flagged by the report for meta-phase).
  - **Decision**: not-needed.
  - **Rationale**: Explicitly a meta-phase semantic-surface drift-sweep candidate (`design/l4_calculus.md §1.2.1 → semantics/index.md §1.2.1` batch-37 residue in other files). No action owed by this report or by repair; the report's in-scope fixes already correct the two target chapters' stale paths.

### Unrepairable findings

None. The sole warning was a contingent cross-report dispatch-ordering note, now satisfied by D5 landing `concepts/element-local-tensor` firm this wave.

## Suggested resolution

`ready`. Integrator note: **dispatch D5 (`layer-intro-author-element-local-tensor`) before / alongside D4** so `book/src/concepts/element-local-tensor.md` exists on disk before D4's two chapters' `depends-on (shape-vocabulary)` edge + prose inline-code resolve. D5 lands the page at rank `firm`; with the shape home firm, D4's `element_restrict` + `geom_factor_build` rough-in (rank 2) rests on a firm dep — well-foundedness (`rank(u) ≤ rank(dep)`) holds, and the chapters will further promote rough-in → firm once the rank-propagation flips through (per the firm-on-positive-structure escape the report documents). No content defects; both chapters are clean rough-in promotions.
