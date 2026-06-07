---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T120500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-07T122500Z
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

# META: verification of D3 — basis_apply + quad_point_contract promoted roadmap_goal → firm

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck --scan` (20 ok / 3 "failing" — all three are `[AMBIG]` basename collisions, not bounds errors: `integrator.{cpp,hpp}` exist under both `palace/fem/` and `palace/fem/libceed/`, and the report's prose disambiguates with the full `palace/fem/libceed/` path everywhere, so these clear). Anchor-verified every load-bearing pinpoint on full paths via `citecheck --anchor`. The re-anchored `quad_point_contract` apply-QFunction citations all confirm exactly on-disk: `geom_data` `:457-458` OK, `q_w`/`CEED_EVAL_WEIGHT` `:462` OK, `AddOperatorActiveInputFields` `:492` OK, `AddOperatorActiveOutputFields` `:493` OK — the report's correction from the drifted `:483-485`/`:486-490` to `:457-458`/`:462` is on-disk-correct (good catch by the producer). Confirmed: `EvalMode` enum `:14-23`, `CeedBasisCreateTensorH1` `:35`, `CeedBasisCreateHdiv` `:67` / Hcurl `:74` / `CeedBasisCreateH1` `:81`, `InitBasis` `:169`, `f_apply_22` `:260`, `QuadratureDataAssembly` `:220`, `AssembleCeedOperator` `:423`, `trial_basis`/`test_basis` `:68`/`:69`, range `:451-495` in-bounds. **The warning:** two of the four EvalMode sub-line pinpoints in `basis_apply`'s Verified-against drift slightly — `CEED_EVAL_INTERP` cited `:36` anchors at `:39`/`:41` (the `AddInput` call is `:41`, +3/+5), and `CEED_EVAL_GRAD` cited `:48` anchors at `:47`/`:49` (the `AddInput` call is `:49`, ±1). The DIV `:57` and CURL `:65` pinpoints land exactly on their `AddInput` calls. All four fall inside the cited governing range `:25-65` (`AddQFunctionActiveInputs`), which is the load-bearing citation and is correct; the drift is in the illustrative inner pinpoints only and does not affect the claim. Minor.

**surface-or-evidence — pass.** Both chapters modify surface (full firm bodies: Status, L1 form/signature, Algebraic laws, Applicability, Verified-against) AND carry the firm-on-positive-structure evidence justification. Record-definition sub-check: the signatures name `Basis`, `BasisMode`, `GeomData`, and the `Tensor[(E,L)]`/`[(E,P,C)]`/`[(E,P,G)]` shape family. The shape family is routed to a definition home — the co-wave `concepts/element-local-tensor` page (D5) — and the named-shape-group notation is linked to `semantics/index.md §1.2.1`, not restated (semantic-consolidation discipline honored). `Basis`/`BasisMode`/`GeomData` are thin parameter types described at point of use (Basis = the tabulated `CeedBasis`; BasisMode = the `EvalMode` enum, defined in `weak_form_term`); acceptable. No undefined-by-use record gap.

**rotation-quality — pass.** Not a cross-layer rotation entry (these are L1 operator firmings, no L_{n+1}→L_n edge). The substantive claim is a maturity promotion via the element-local rank-tensor vocabulary shift; the shape vocabulary (`[E,L]` ↔ `[E,P,C]`) genuinely carries rank structure the flat `Tensor[N]` BLAS L1 cannot, so the firming rests on a real vocabulary addition, not a rename. No 1:1 mapping smell.

**variant-axis-coverage — pass.** Variant axes are covered: `basis_apply` covers all four `BasisMode` values (Interp/Grad/Curl/Div) via the EvalMode dispatch and the de-Rham family selectors (H1/Hcurl/Hdiv), and scopes out non-de-Rham/non-polynomial integrands explicitly (applicability cond. 2). `quad_point_contract` covers the mass vs grad-grad metric block-shape axis and scopes single-machine (cond. 3). Sum-factorization (tensor vs non-tensor element) is handled as a transparent-trick axis, not a hidden branch.

**cross-reference-integrity — warning.** All `[link]` targets resolve on disk EXCEPT the load-bearing `../concepts/element-local-tensor.md`, which **does not yet exist** — it is the co-wave D5 deliverable. The report flags this explicitly (Open questions, first bullet) and notes the two-wave + single-finalize sequencing makes it present at the one build. This is a real forward-reference-to-nonexistent-file condition: if D5's page is not created before `integrator-finalize` rebuilds the book, `linkcheck2` errors hard. All other targets verified present: `libceed-quadrature-kernel-impl`, `weak_form_term`, `element_restrict`, `geom_factor_build`, `elementwise_product`, `concepts/tensor-field-lift`, `semantics/index.md`. Firm-body-inside-fence guard: PASS — fences balanced (even parity, 4 `edit:` blocks cleanly paired), and the full firm apparatus (Status + signature + Algebraic laws + Verified-against) sits INSIDE each chapter's fence. Maturity-overclaim sub-check (the firm-call rests on the D5 page being firm): see Issues — this is the central judgment call.

**edge-label-fidelity — pass.** No L_{n+1}→L_n lowering edge is claimed (these are in-layer L1 firmings). The `pulled-by` / `realizes` reference edges in the frontmatter are correctly typed as `reference` and the prose discusses exactly those constituent relationships (B/Bᵀ either side of D, D consuming B's output shape). No mislabeled edge.

**plan-kind-consistency — pass.** Declared kind is firm-promotion (roadmap_goal → firm); content shape matches — both chapters carry the full firm apparatus with no rough-in placeholders or TODO sketches. The firm-on-positive-structure escape is invoked correctly (the cited precedents `weak_form_term`, `fe_assemble` are both confirmed `rank: firm` on disk; `elementwise_product` the lifted-from op is confirmed `firm`). Laws are syntactic operator-algebra identities (adjointness, per-element linearity, block-diagonality, pointwise-no-coupling) on read-not-constructed libCEED source — the escape's exact pattern.

**skill-uptake-survey — pass.** Telemetry only. The report self-invoked codemap `read_range` verification and the citation re-anchoring procedure (the re-anchor work IS the producer-citation-drift discipline). No specific skill is mandated by this report's shape that is unreferenced.

### Issues found

1. **(warning, citation) `basis_apply.md` Verified-against — two EvalMode sub-line pinpoints drift.** `CYCLE.md:146` (and the index.md cohort bullet) cite `CEED_EVAL_INTERP :36` (on-disk `:39`/`:41`, `AddInput` at `:41`) and `CEED_EVAL_GRAD :48` (on-disk `:47`/`:49`, `AddInput` at `:49`). DIV `:57` / CURL `:65` are exact. All four fall inside the correct governing range `:25-65`, so the claim holds; the inner pinpoints are off by +3/+5 and −1/−2 respectively. Repair: bump INTERP `:36`→`:41` and GRAD `:48`→`:49` for pinpoint exactness (or restate as the range only). Low severity — does not gate the firm claim.

2. **(warning, cross-reference / maturity) The firm-call rests on `concepts/element-local-tensor` being firm at integrate time, and that page does not yet exist on disk.** `CYCLE.md:80, 95, 209, 224` (and both frontmatters) link `../concepts/element-local-tensor.md` as the firm L1 record-definition home that closes the rank-0-keeping vocabulary gap; the page is the co-wave D5 deliverable. This is the report's own central caveat (Open questions bullets 1–2), with an honest `rough-in (test-coverage-bounded)` fallback offered. Two coupled risks for the integrator to adjudicate: (a) **build-ordering** — D5's concepts page MUST be created before the finalize `linkcheck2` rebuild, else hard link error (the report asks the integrator to order D5 before finalize; the wave schedule does this, but it is a real dependency, not self-resolving within D3); (b) **maturity** — firm-at-integrate-time holds ONLY IF D5's page lands firm. Per the critic role I do not adjudicate repairability, but I flag that the firm verdict is correct *conditional on* D5 landing firm this wave; if D5 slips or lands non-firm, the rank-invariant is violated (a firm node whose closing vocabulary is not firm) and the fallback `rough-in (test-coverage-bounded)` applies. The dependency is expressed as a `reference` edge (which the rank linter ignores), so the mechanical linter will NOT catch a D5-slip — this is a human/integrator-judgment gate, not a lint-caught one.

3. **(informational, no defect) Stale `design/l4_calculus.md` path correctly fixed in the proposed bodies.** The on-disk current chapters still carry `book/src/design/l4_calculus.md §1.2.1` (basis_apply:39, quad_point_contract:42); the report's edit blocks replace this with the live `book/src/semantics/index.md §1.2.1` (`CYCLE.md:94, 224`), and §1.2.1 there is confirmed the Named-shape-groups section. The fix is correct and the full-file `edit:` replacement removes the stale path. No action needed — noting for the integrator that this is an intended correction, not drift.

---

## Repair

### Fixes attempted

- **Finding 1 — citation-validity (low): two EvalMode sub-line pinpoints in `basis_apply` Verified-against drift.** `CEED_EVAL_INTERP` cited `:36`, `CEED_EVAL_GRAD` cited `:48`; DIV `:57` / CURL `:65` exact.
  - **Decision**: repaired.
  - **Action**: Codemap-verified the governing range on-disk (`mcp__palace-codemap__read_range palace/fem/libceed/integrator.cpp:25-66`). The four `CeedQFunctionAddInput(... CEED_EVAL_*)` call lines land at INTERP `:41`, GRAD `:49`, DIV `:57`, CURL `:65`. Corrected both drifted pinpoints surgically in two places in CYCLE.md:
    - `CYCLE.md` *Verified-against* (basis_apply edit block): `CEED_EVAL_INTERP :36`→`:41`, `GRAD :48`→`:49`.
    - `CYCLE.md` *Supporting evidence*: same two pinpoints `:36`→`:41`, `:48`→`:49` (added "(AddInput call lines)" clarifier for posterity).
    - The load-bearing governing citation `integrator.cpp:25-65` (`AddQFunctionActiveInputs`) was already correct and is unchanged; the claim never depended on the inner pinpoints. This is a pure pinpoint-exactness mechanical fix within repair authority (citation line range off by a small offset).

- **Finding 2 — cross-reference-integrity (medium, contingent): the firm call rests on the co-wave D5 `concepts/element-local-tensor` page being firm at integrate time.**
  - **Decision**: not-needed (no content defect; integrator dispatch-ordering note recorded — see below).
  - **Action**: Confirmed the forward-ref slug is the canonical `concepts/element-local-tensor` throughout the report (frontmatter `edges.reference` in both chapters, body links `../concepts/element-local-tensor.md`, Verified-against entries, Related sections, index.md cohort/dep-map rows). No slug drift; no edit needed. D5 DID land that page firm this wave (`reports/2026-06-07T112037Z-layer-intro-author-element-local-tensor/CYCLE.md`). The condition the critic flagged (a) build-ordering and (b) maturity is therefore SATISFIED conditional on the integrator applying D5 before/with D3 in the same finalize build — which the two-wave + single-finalize schedule does. Recorded as an integrator dispatch-ordering note (Suggested resolution), NOT a content defect repairable here.

### Unrepairable findings

None. The one substantive finding (finding 2) is a cross-report dispatch-ordering note resolved by the wave schedule (D5 landed its page firm), not an authoring gap.

## Suggested resolution

`overall_status: ready`. The two drifted pinpoints are corrected to their on-disk AddInput-call lines; all citations now anchor exactly.

**Integrator dispatch-ordering note (finding 2):** D3's two firm chapters link `../concepts/element-local-tensor.md`, the co-wave D5 deliverable (`reports/2026-06-07T112037Z-layer-intro-author-element-local-tensor/`). Apply **D5's concepts-page creation before (or in the same finalize build as) D3** so the single `cargo make book` rebuild sees the file (else `linkcheck2` hard-errors on the live link). The rank-invariant also holds only because D5's page lands `firm` (the `reference`-class edge is lint-invisible, so this is a human/integrator-judgment gate, not a lint-caught one) — D5 confirmed firm, so the firm verdict on both chapters stands. If for any reason D5's page is absent or non-firm at integrate time, the report's own honest fallback (`rough-in (test-coverage-bounded)` for both ops) applies.
