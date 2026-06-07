---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T130000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of cycle-124 D5 — concepts/element-local-tensor record page + kernel-impl promotion + L1/index tally

## Critique

### Checks run

**citation-validity — warning.** All three L0 axis-layout citations verify exactly on-disk: `palace/fem/libceed/restriction.cpp:200-203` = `CeedElemRestrictionCreate(ceed, num_elem, P, fespace.GetVDim(), comp_stride, fespace.GetVDim() * fespace.GetNDofs(), ...)` (the `num_elem=E, P=L, vdim=C` layout); `palace/fem/libceed/basis.cpp:25-37` = `CeedBasisCreateTensorH1(ceed, dim, num_comp, P, Q, ...)` at :35-37 preceded by the `qW` weight-normalization loop :25-33, with `P=ndof` (nodes, spec `L`) and `Q=nqpt` (quad-points, spec `P`) confirming the noted libCEED param-name inversion; `palace/fem/libceed/integrator.cpp:393-398` = `CeedElemRestrictionGetNumComponents` :393-394, `MFEM_VERIFY(geom_data_size == 2 + space_dim * dim, ...)` :395-396, `CeedQFunctionAddOutput(build_qf, "geom_data", geom_data_size, CEED_EVAL_NONE)` :397-398 (the `G = 2 + space_dim*dim` axis). `citecheck --scan` reports the L0 citations clean (the 3 `[AMBIG]` hits are bare `integrator.cpp` tokens in prose/comments where the report's actual citations carry the full unambiguous `palace/fem/libceed/integrator.cpp` path). The warning is for ONE non-L0 issue: the kernel-impl `## Status` proposed-new-text (Proposed changes §(2), edit #2) attributes an **in-quotes** phrasing to `CLAUDE.md §Methodology-invariants "a composition-root's \`rank\` is CAPPED by its least-resolved blocking dep"` — that exact quoted string does NOT appear in CLAUDE.md; the actual well-foundedness phrasing is "an entry is at most as resolved as its least-resolved dependency" (verified `grep`). The substance and the rule application are correct; only the quoted attribution is a paraphrase presented as a verbatim quote of a project doc.

**surface-or-evidence — pass.** Record-definition obligation is the load-bearing sub-check here, and it is met: `concepts/element-local-tensor.md` defines the DATA SHAPE (5 named axes with meaning/stratum/L0-binding table; 3 shape tuples `[E,L]`/`[E,P,C]`/`[E,P,G]`; build-vs-run stratification; L0 source home) and explicitly does NOT restate operator algebra — the opening blockquote routes the contraction behaviour to the four consumer chapters ("this page does NOT restate that contraction algebra. It defines only the *shape*"), and the "Signatures / chapters that name this family" section lists each consumer's *signature only* with the algebra deferred to its chapter. The ≥2-consumer bar is correctly fired (all 4 substrate ops + the kernel-impl). The `firm` call on a data-shape page is justified as the data-shape analog of the firm-on-positive-structure escape — every axis is a syntactic read-off of a positive libCEED construction arg (no test gates a shape definition). The `RefinementData.md` (c123) precedent for the `kind: record` format exists on-disk.

**rotation-quality — pass.** Not a rotation proposal. The record page is a data-shape definition home, the kernel-impl promotion is a rank adjustment, the semantic §1.2.3 is a convention statement, and the L1/index tally is bookkeeping — none asserts an algebraic/structural rotation. No-op (not applicable to a record-page + rank-promotion + tally report).

**variant-axis-coverage — pass.** No orthogonal variant axes in a data-shape definition. The `EvalMode`-selected `C` component count is documented as a per-term-selected axis but is a property of the consumer ops, not a hidden branch of this page. Not applicable.

**cross-reference-integrity — pass.** All links resolve on-disk: the four substrate ops (`L1/basis_apply.md`, `quad_point_contract.md`, `element_restrict.md`, `geom_factor_build.md`), `L1/libceed-quadrature-kernel-impl.md`, `concepts/build-time-vs-run-time-stratification.md`, `L1-L0/fe-assemble-libceed-boundary-obstruction.md`, and `semantics/index.md` all exist. The SUMMARY.md alpha insertion is correct: `eigsolve` < `element-local-tensor` < `elementwise-product` (the `element-` vs `elementw` divergence is `-` (0x2d) < `w` (0x77)), and the proposed-edit anchor (concepts lines 345-346) matches on-disk. The three L1/index `edit:` anchors (grand-total line 47, kernel-impl bullet line 99, cohort header line 101) all match on-disk exactly; the semantic-surface anchor (lines 95-97) matches; the three kernel-impl `edit:` anchors (frontmatter rank comment + `rank: roadmap_goal`, `## Status` block, `## Substrate L1 operators` header) all match. The `realizes-kernel-api` / `realizes-leaf` `reference` edges (kernel-impl frontmatter lines 19-23) and the `depends-on (composes)` block (lines 26+) are NOT touched by any of the three kernel-impl edits — DIRECTIVE-3 edge integrity preserved as claimed. NOTE (not a defect, ordering observation — see Issues): all four substrate ops + the kernel-impl are currently `roadmap_goal` on-disk; the report's firm/rough-in maturity claims about them depend on sibling reports D3/D4 applying first in the same cycle.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label on this report (it is a record-page + promotion + tally, not a lowering theme). The `realizes-kernel-api` / `realizes-leaf` reference labels are correctly described and left untouched. Not applicable.

**plan-kind-consistency — pass.** The declared shapes match content: the record page is authored as a `kind: record` `firm` page with full apparatus (definition table, shapes, stratification, L0 home, status); the kernel-impl is a rank promotion `roadmap_goal → rough-in` with the well-foundedness cap correctly applied (`rank(impl) ≤ min(deps)` = min(2 firm, 2 rough-in) = rough-in — promoting to firm would violate well-foundedness, rough-in is exactly right); the semantic §1.2.3 is a USE+LINK convention sub-section; the L1/index edits are tally bookkeeping. No mis-classification.

**Rank-invariant (graded-stack check 9) — pass.** Record page `firm`: its only blocking edges are `cites-evidence depends-on` to L0 source (rank-terminal ground truth), so `rank(u) ≤ rank(v)` holds; consumer edges are `reference` and constrain nothing. Kernel-impl `rough-in`: its 4 `composes depends-on` deps post-D3/D4 are 2 firm (rank 3) + 2 rough-in (rank 2), `min = 2 = rough-in`, so the rough-in cap is correct and a firm claim would be a violation. The arithmetic on the L1/index grand-total bump is correct: 33 main + 4 FE-assembly + 5 FE-space + 1 Mesh-construction + 2 libCEED-substrate = 45 (verified). The semantic §1.2.3 addition states the convention and links to the record page for definitions — it does NOT restate the axis table or the substrate ops' algebra (verified against the proposed-new-text), satisfying the semantic-consolidation USE+LINK discipline.

**Reachability (graded-stack check 10) — pass.** The kernel-impl carries pulled-by provenance (`fe_assemble`, firm, reaches the feature root via feature-column inbound edges); the record page is reachable as the shape home referenced by the four reachable substrate ops + the kernel-impl.

**skill-uptake-survey — pass.** The report references codemap `read_range` on-disk verification for all three L0 citations. (Note the c105 sharpening: `read_range` is not a citation source-of-truth; the critic's own verification here was a direct on-disk `Read`, which confirmed every line — so the producer's read_range-based self-verification did not introduce drift.) No mandatory skill un-invoked.

### Issues found

1. **`CYCLE.md` Proposed changes §(2) edit #2 (kernel-impl `## Status` new-text) — in-quotes attribution to a non-existent CLAUDE.md string.** Severity: low. The new `## Status` text reads `(CLAUDE.md §Methodology-invariants "a composition-root's \`rank\` is CAPPED by its least-resolved blocking dep")`. This exact quoted string is not in CLAUDE.md; `grep` confirms the project's actual well-foundedness phrasing is "an entry is at most as resolved as its least-resolved dependency" (and the graded-stack `rank(u) ≤ rank(v)` invariant). The rule applied is correct and the substance is faithful — this is a precision issue only: a paraphrase presented inside quotation marks as a verbatim quote of a project document. Candidate repair: either drop the quotation marks (cite the invariant by name without quoting) or replace the quoted text with the actual CLAUDE.md phrasing.

2. **Same-cycle cross-report ordering dependency (observation, not a blocking defect).** Severity: informational. All four substrate ops (`basis_apply`, `quad_point_contract`, `element_restrict`, `geom_factor_build`) and `libceed-quadrature-kernel-impl` are `roadmap_goal` on-disk *now*; the report's firm (D3) / rough-in (D4) maturity claims — and hence the kernel-impl rough-in cap and the L1/index 43→45 tally — are correct only *after* sibling reports D3 and D4 apply earlier in the same cycle's serial integration. The report explicitly flags this coupling (Open questions: cross-report rank-propagation; the integrator handles ordering) and the maturity claims are honest given that ordering. No critic action required, but the integrator must apply D3/D4 before D5 for the tally arithmetic and the rough-in cap to hold; if D3/D4 do not land firm/rough-in as expected, the 43→45 bump and the rough-in cap would be premature. Surfaced for the integrator's serial-ordering attention.

---
repaired_at: 2026-06-07T133000Z
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

## Repair

### Fixes attempted

- **Finding 1**: `CYCLE.md` Proposed changes §(2) edit #2 (kernel-impl `## Status` new-text) presents a paraphrase inside quotation marks as a verbatim quote of CLAUDE.md — `"a composition-root's \`rank\` is CAPPED by its least-resolved blocking dep"` — but that exact string does NOT appear in CLAUDE.md (the actual well-foundedness phrasing is "an entry is at most as resolved as its least-resolved dependency").
  - **Decision**: repaired
  - **Action**: Edited `CYCLE.md` §(2) kernel-impl `## Status` new-text block (the well-foundedness-cap paragraph). Dropped the fabricated in-quotes string and replaced the parenthetical with the real CLAUDE.md phrasing as an unattributed paraphrase plus the named invariant: `(CLAUDE.md §Methodology-invariants: an entry is at most as resolved as its least-resolved dependency — the graded-stack `rank(u) ≤ rank(v)` invariant)`. This is in-scope (trivial citation/attribution precision fix); the substance — the rough-in cap and its arithmetic — was already correct and is untouched.

- **Finding 2**: Same-cycle cross-report ordering dependency — the firm/rough-in maturity claims, the rough-in cap, and the 43→45 tally hold only after sibling D3/D4 apply earlier in the same cycle's serial integration.
  - **Decision**: not-needed (no edit)
  - **Action**: Recorded as an integrator-ordering note (below). The report already flags the coupling in its Open questions; the critic marked it informational with no critic/repair action required. No CYCLE.md edit — this is a serial-ordering instruction for the integrator, not a content defect.

### Unrepairable findings

None. The single warning-level finding was a mechanical attribution fix (in scope); the informational finding requires no edit.

### Integrator-ordering note

**Apply D3 + D4 before D5 in this cycle's serial integration.** D5's maturity claims depend on the sibling reports landing first: `basis_apply` + `quad_point_contract` firm (D3) and `element_restrict` + `geom_factor_build` rough-in (D4). All five nodes are `roadmap_goal` on-disk *now*. If D5 is applied before D3/D4, the rough-in cap on `libceed-quadrature-kernel-impl` (`min(deps)` = rough-in) and the L1/index 43→45 firm grand-total bump would be premature/incorrect. The report's Open questions also flag the downstream cross-report rank-propagation: once D5's record page lands firm, D4's two rough-in ops firm-flip (their cap rises), and the impl re-caps to firm — a c125 tally follow-up (43→45→47) the report explicitly defers and does NOT do this wave (correct, since those nodes are rough-in on-disk now). The integrator handles cross-report rank propagation per the planner's note.

## Suggested resolution

`ready`. The one warning-level finding (fabricated in-quotes attribution) is fixed surgically; substance was already correct. Note for the integrator: apply D3/D4 before D5 (see integrator-ordering note above) so the rough-in cap and the 43→45 tally arithmetic hold; the downstream firm-flip + 43→45→47 follow-up is correctly deferred to c125.
