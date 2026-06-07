---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T143000Z
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

# META: verification of "L4 roadmap_goal cap — mk_matrix_free_operator backend-lowering operator-constructor + pull-chain"

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reports `10 ok, 0 failing`. The five load-bearing L0 construction-site pinpoints were individually `--anchor`-verified on-disk: `palace/fem/libceed/operator.hpp:32` (`class Operator`), `:48` (`AddSubOperator`), `:81-82` (`CeedOperatorFullAssemble`), `palace/fem/bilinearform.cpp:118` + `:143` (`UseFullAssembly`) — all `[ok]`. The report's own "all five self-verified via `citecheck --anchor`" claim is confirmed. No `verified_against:` block is emitted (not a lowering-verifier audit), so that sub-check no-ops. Because this is a `roadmap_goal` (rank-0, claim-free) chapter, the citation discipline formally relaxes per the graded-stack `roadmap_goal` rule — but every anchor the report DID cite is nonetheless correct.

**surface-or-evidence — pass.** This is a `roadmap_goal` intent node, not a refinement-shaped proposal modifying an existing operator/theme; the surface/evidence framing applies as the graded-stack `roadmap_goal` no-op (the chapter carries banner + intent + pulled-by + declared deps, which IS the required shape). Record-definition sub-check: the signature names `FESpace`, `WeakFormTerm`, `GeomFactors`, `LinearOperator` — but these are NOT undefined-by-use here. `GeomFactors` is the firm `geom_factor_build` product (cited, firm c125 D1); `FESpace`/`WeakFormTerm` are the `fe_assemble` construction-stratum vocabulary the chapter cross-links and which `fe_assemble` defines; `LinearOperator` is the standard L4 result type. None is a newly-introduced result record demanding a definition home in THIS chapter (the chapter is explicitly claim-free and defers field-level definition to the firm constituents it composes). No flag warranted.

**rotation-quality — pass (no-op).** A `roadmap_goal` makes no algebraic/structural rotation claim of its own; it is a claim-free intent node. The apply-lowering sketch (`apply (mk_matrix_free_operator ...) v = matrix-free-operator-apply ... v = (Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G) v`) is presented as a SPECULATIVE reconstruction pointing at the firm L2 combinator, not asserted as a verified rotation. No rotation to grade.

**variant-axis-coverage — pass.** Two orthogonal axes are explicitly declared in frontmatter and discussed in prose: `assembly-representation` (partial matrix-free `ceed::Operator` vs full materialized CSR — the `UseFullAssembly` order-threshold dispatch, `bilinearform.cpp:118,:143`, with `mk_matrix_free_operator` scoped as the `partial`/`else` branch) and `differential-operator` (the `WeakFormTerm` 𝒟 selecting the `B_𝒟` EvalMode, absorbed as leaf content consistent with `fe_assemble`/`matrix-free-operator-apply`). The full-materialization branch is explicitly scoped out (it is `CeedOperatorFullAssemble`, the alternative this op is NOT). No hidden branch.

**cross-reference-integrity — pass.** All `[link]` targets resolve on-disk: `book/src/L4/fe_assemble.md`, `book/src/L2/matrix-free-operator-apply.md`, `book/src/L4/index.md`, `book/src/concepts/element-local-tensor.md`, `book/src/concepts/black-box-vs-accelerated-kernels.md`, `book/src/semantics/index.md`, and the four firm L1 substrate ops (`element_restrict`/`basis_apply`/`quad_point_contract`/`geom_factor_build`) all exist. The `semantics/index §1.2` named-shape-group reference is real (§1.2 Shape expressions, named shape group `(S: ...)` at line 62). Maturity-claim integrity: `L2/matrix-free-operator-apply` is on-disk `rank: firm` (matches the "firm" claim); `L4/fe_assemble` is `firmness: firm` (matches the firm-references-rank-0 framing). The two `edit:` blocks are well-targeted: the fe_assemble `reference:` block edit matches lines 11-14 exactly and adds NO pre-existing duplicate (`grep mk_matrix_free_operator book/src/L4/fe_assemble.md` is empty before the edit); the fe_assemble prose-edit `old_string` (the "D2 owns it" paragraph) matches line 160 verbatim. SUMMARY.md insertion is alpha-correct (linear_combination → mk_matrix_free_operator → nrm2); the L4/index row is inserted in alpha position between the `linear_combination` and `nrm2` rows. Build-readiness fence guard: not a firm-body claim, so the firm-body-inside-fence guard does not apply.

**edge-label-fidelity — pass (load-bearing, verified carefully).** The two pull-chain edges carry explicit labels and the prose discusses exactly those edges. (i) Inbound `fe_assemble (firm) → mk_matrix_free_operator (rank-0)` is labelled `reference`/`constructs-via`+`pulled-by` and the §Pull-chain prose + the fe_assemble frontmatter edit + the fe_assemble prose edit all consistently describe it as a navigational `reference`, NOT `depends-on` — the well-foundedness argument (`rank(fe_assemble)=firm > rank(mk)=0`, so a blocking `depends-on` would be a rank_violation) is stated correctly in all three places. (ii) Downward `mk_matrix_free_operator → L2/matrix-free-operator-apply (firm)` is labelled `reference`/`lowers-to` and the prose discusses exactly the apply-to-L2-contraction-chain lowering. No edge-label/prose mismatch; the directions and classes are consistent across frontmatter, prose, index row, and OQ closure.

**plan-kind-consistency — pass (load-bearing, verified carefully).** Declared kind = `roadmap_goal` (rank 0). The content matches: claim-free (`⟢ roadmap_goal (rank 0) — claim-free intent` banner; every L4 form explicitly flagged SPECULATIVE), an Intent section, a pulled-by provenance, declared deps, and accreting working context — the canonical `roadmap_goal` chapter shape. It does NOT over-claim: the report's §Open-questions records the deliberate maturity judgment (the firm-on-positive-structure escape was considered and DEFAULTED-DOWN to `roadmap_goal` because the inbound pull is `reference`-class, not a blocking `depends-on` from a firm consumer — so no blocking pull-chain to a root licenses a firm claim). This is exactly the rank-0/`roadmap_goal` discipline; the cap is correctly classified.

**skill-uptake-survey — pass.** The report references `citecheck --anchor` (the citation-verification tool) for its L0 anchors — the relevant procedure for this shape was invoked. No further skill is implied by a claim-free roadmap_goal landing.

**Graded-stack additions.** (9) **rank-invariant — holds.** Both pull-chain edges are `reference`-class (navigational, free, NOT rank-constrained per scheme §1g), so neither imposes a rank floor: the firm `fe_assemble` does not blocking-`depends-on` the rank-0 node (it `reference`s it), and the rank-0 node does not impose a floor on the firm L2 combinator (it `reference`s it rather than `depends-on`). `rank_violations: 0` is preserved. The frontmatter records no `depends-on` edge at all — only `reference` — which is the correct encoding for a rank-0 node whose blocking deps are all higher-rank (recorded as `reference` precisely so the rank-0 node imposes nothing). (10) **reachability — holds.** The node is pulled by firm `fe_assemble`, which reaches a feature root via its 7 feature-column inbound edges (confirmed: fe_assemble carries the absorbed-post-composition grounding edge + driver-column reachability). The pulled-by chain terminates at a root, so the node is live / not-garbage.

### Issues found

No blocking or warning issues. Two minor observations, both NON-blocking and within `roadmap_goal` tolerance (recorded for the repairer/integrator, not requiring a fix):

1. **(observation, non-blocking) Pseudo-language uses 4-space indented code rather than fenced ` ```text `.** The strawman notation invariant (semantics/index §1.2 / the L4/L3 pseudo-language convention) prescribes fenced ` ```text ` for L4 Haskell `::` signatures. The chapter uses 4-space indented code blocks for both the signature and the apply-lowering. This is a pragmatic adaptation (the body lives inside a `new:` proposed-changes fence, where a nested ` ```text ` fence would require fence-escaping), the content is claim-free SPECULATIVE roadmap_goal material, and the Haskell `::` form + definitional `=` rules themselves follow convention. The reduction is rendered as definitional equalities (`= ...`), not small-step `$$` semantics — appropriate for an apply-lowering correspondence sketch (no small-step rule is being stated, so `$$` is not required). Flagging only as telemetry; not a fidelity defect for a rank-0 node.

2. **(observation, non-blocking) SUMMARY/index edit `old_string` context is a 3-line insertion anchor.** The SUMMARY edit block shows `linear_combination`/`mk`/`nrm2` as the insertion context; the on-disk file also has `inner_product` above and `sparameter_reduce` below, but the chosen 3-line anchor is unambiguous and alpha-correct, so the insertion point is well-defined. No action needed.

This report is clean (all 8 checks pass; both graded-stack invariants hold). `overall_status: ready` set per the all-pass clean-report rule.
