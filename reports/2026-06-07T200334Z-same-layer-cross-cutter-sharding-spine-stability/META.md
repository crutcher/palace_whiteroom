---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T201500Z
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

# META: verification of "L4/L3/L2 firm-combinator stability set — sharding-MATH decomposition-abstraction"

## Critique

### Checks run

**citation-validity — pass.** This is a within-book firm-cohort audit; every load-bearing citation is a `book/src/` line ref, so I verified each by direct on-disk Read (no `reference/palace/` L0 claim to citecheck). All five load-bearing pinpoints check out and support the ALL-GREEN claim: (a) `L3/inner_product.md:233-238` carries exactly the "Split-additivity / shape-concatenation-homomorphism (the defining law)" with the `inner_product (x₁ ++ x₂)(y₁ ++ y₂) = ... + ...` monoid-homomorphism and the "licenses parallel/blocked evaluation" sentence — verbatim what the report leans on (the law text runs 233-238, extending to 240; both the `:233-238` and `:233-240` forms the report uses are in-range and correct). (b) `L3/linear_combination.md:103` is the "Concatenation-homomorphism (the defining law)" with the `([(Scalar,Tensor)], ++, []) → (Tensor, +, zeros)` monoid hom — exact. (c) `L2/gram.md:154-159` is the "Concatenation block law" explicitly named "the basis-index-axis analogue of `inner_product`'s split-additivity" — exact. (d) `L4/gram_reduce.md:119` is the "Each grid entry is independent (the upper-triangle `map` is a list homomorphism over pairs)" law, and `:158` is "embarrassingly parallel over pairs" — both exact. (e) `book/src/L4/domain_energy_reduce.md:147-152` is law 1 "Map-independence / concatenation-homomorphism … Embarrassingly parallel over domains", and the supporting `:57-59` (domain-restricted energy form), `:172-178` (config-conditional `Σ pᵢ = 1`), and `:16` (`partition-coverage` variant axis) all resolve and say what the report attributes to them. Frontmatter edge-structure claims (`:6-8` `depends-on`, `:9-12` `reference`) verified against the file head. `L4/inner_product.md:147` is the one slightly-soft pinpoint: line 147 is the "Carried up **unchanged** from the firm L3 inner_product" paragraph head, while the numbered split-additivity law sits at 154-157; but the report's prose claim ("split-additivity carried up unchanged to L4") is precisely what line 147 asserts, so the citation backs the claim and is in-range — not drift. No `verified_against:` YAML block in this report, so that sub-check no-ops.

**surface-or-evidence — pass.** This is an audit-class observation that proposes NO book mutation (no operator/theme surface change). It is not a refinement-shaped proposal, so the surface-AND-rotation-evidence requirement does not apply; the "pure observation" shape is the legitimate same-layer-cross-cutter output. Record-definition sub-check: the report names no new record/struct in any signature it proposes to add (it cites existing verbs by name only), so no definition-home obligation is triggered. Not applicable to this audit-observation kind beyond the citation backing, which is solid.

**rotation-quality — pass (not applicable).** The report asserts no algebraic/structural/reduction rotation of its own — it is a stability cross-check that catalogues existing firm laws and concludes none must re-root. No L_{n+1}/L_n compaction claim to grade.

**variant-axis-coverage — pass.** No new operator/theme with variant axes is proposed. The report does correctly surface the relevant existing axis (`domain_energy_reduce`'s `partition-coverage`, `:16`) and flags partition-of-unity as a precondition the future abstraction must state rather than assume — appropriate axis-awareness, not an uncovered branch. Not applicable as a blocking check to this kind.

**cross-reference-integrity — pass.** Every named firm node (`inner_product` L4/L3/L2, `linear_combination` L4/L3, `gram` L2, `gram_reduce` L4, `domain_energy_reduce` L4, plus the surveyed `fold_solve`/`solve_family`/`iterate-while`/`krylov-step`/`fe_assemble`) resolves to a real chapter on disk, and the cited line ranges land inside them. The `reference`-class edge taxonomy claim is consistent with CLAUDE.md §GRADED RESOLUTION LADDER as quoted. The graded-stack baseline the report cites (`RESULT: 0 rank violation(s)`) reproduces on a fresh lint run this verification — confirmed intact.

**edge-label-fidelity — pass (not applicable).** The report carries no L_{n+1}→L_n lowering-edge label; it is a same-layer (L4/L3/L2 lateral) cohort audit. No edge-label-to-prose mismatch possible.

**plan-kind-consistency — pass.** Declared shape is an audit/observation (same-layer-cross-cutter, "Observation kind: Shared sub-pattern", "Recommendation: Defer to plan as the CLEAR-lateral input"). The content matches: a single shared-pattern observation (the split/concatenation monoid-homomorphism as the decomposition core) delivered as a GREEN/RED disposition set with no firm-node mutation. No firm/rough-in mis-classification; no placeholder-bearing "firm operator" entry.

**skill-uptake-survey — pass.** The report's shape (within-book firm-cohort audit, no L0 claim) does not strongly imply a specific skill invocation, and the report explicitly reasons about why no `citecheck --anchor` run was needed (no NEW L0 claim). Telemetry-only check; nothing blocking.

### Issues found

No issues. All eight checks pass.

One nit for the record (NOT a finding, no repair required): the `L4/inner_product.md:147` pinpoint targets the "carried up unchanged" paragraph head rather than the numbered split-additivity law body at `:154-157`. The citation is in-range and backs the exact prose claim ("carried up unchanged to L4"), so it is correct as written; an author tightening the ref later could point at 154-157 for the law text itself, but this is a polish nicety, not drift and not a defect.
