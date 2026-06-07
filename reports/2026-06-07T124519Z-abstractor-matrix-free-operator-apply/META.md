---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T133000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: pass
# graded-stack additional checks:
#   rank-invariant: warning  (well-foundedness cap unsatisfied on current disk; conditional on sibling D1)
#   reachability: pass
---

# META: verification of L2 `matrix-free-operator-apply` constructive-kernel combinator (cycle-125 D2)

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` over the report: 18 ok, 0 failing. All load-bearing pinpoints anchor-verified on disk this dispatch: `integrator.cpp:422-445` (`AssembleCeedOperator` at :423, in range), `operator.cpp:182-189` (`Mult` at :182,:185), `operator.cpp:483` (`AssembleCOO`), `bilinearform.cpp:77` (`AddSubOperator`). The `libceed-quadrature-kernel-impl.md:102` chain `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` is present on disk (the identity-in-named-terms basis). The `verified_against:` YAML block (the 4-space-indented payload destined for re-fencing) was extracted and run through `yaml.safe_load` — it round-trips cleanly; every `note:` value begins with prose (no leading-quote scalar-open defect).

**surface-or-evidence — pass.** This is a new `firm` chapter, not a refinement-of-existing; its evidence is the positive `AssembleCeedOperator` master + `Operator::Mult` apply, both cited and anchor-verified. Record-definition sub-check: the signature names type aliases (`ElemRestriction`, `Basis`, `GeomData`, `Coefficient`) that are already defined in the linked substrate chapters and `weak_form_term`/`geom_factor_build`, and the result `LinearOperator[(N: ...)]` is typed via `concepts/element-local-tensor` — none is a new record introduced-and-only-used here, so no missing definition home.

**rotation-quality — pass (load-bearing; verified carefully).** The L2 combinator is a genuine abstraction: a NEW named contraction-chain composition over the rank-structured `element-local-tensor` family, distinct from every flat-`Tensor[N]` BLAS cohort (correctly argued in §"Cohort placement"). The combinator hides the five-stage pipeline behind `mk-operator`/`apply` and states composition-LEVEL laws (linearity, `Gᵀ…G` symmetry sandwich, element-additive scatter-add) WITHOUT restating substrate algebra — semantic-consolidation discipline observed (§"Composition-level laws" explicitly defers `element_restrict`/`basis_apply`/`quad_point_contract` own-algebra to those chapters). The L2→L1 edge IS identity-in-named-terms (the kernel-impl names the same chain over the same vocabulary), and the report correctly resolves it as an in-line "Downward to L1" note + a `reference`-class `lifts-kernel-impl` edge — NOT a mirrored degenerate-lowering theme. That is the redirect's degenerate-lowering-smell rule applied correctly; no `L2-L1/` theme is authored. This is the right judgment, not a missing rotation.

**variant-axis-coverage — pass.** The orthogonal axes are explicitly handled: sum-factorization classified a transparent performance trick (algebraically equivalent to the unfolded `B_𝒟`; one note, factoring lives below L2 as a `basis_apply` detail) — correct per CLAUDE.md §Optimization tricks; the matrix-free-vs-assembled-COO representation axis handled as a primary/derived duality (one note, `CeedOperatorAssembleCOO`); and the symmetry-of-`D` axis is handled inside law 2 (symmetric `D` ⟹ self-adjoint `A`; non-symmetric `D` ⟹ non-symmetric `A`, symmetry a property of `D` transported by the sandwich). No hidden branch.

**cross-reference-integrity — pass.** All slugs resolve on disk (`element_restrict`, `basis_apply`, `quad_point_contract`, `geom_factor_build`, `libceed-quadrature-kernel-impl`, `fe_assemble`, `weak_form_term`; concepts `element-local-tensor`, `tensor-field-lift`, `build-time-vs-run-time-stratification`). Every edit anchor exists: SUMMARY.md `reciprocal` line (:165) + `# L2 > L1` (:167); L2/index `elementwise-gate-floors-intro` edge, `divfree-projector` firm bullet, `Partly-constructive at L2` heading, `### Elementwise & gate floors` table, `## Working Notes`, and the count line `22 firm + 1 partly-constructive` (:90). Firm-body-inside-fence guard: fence enumeration shows 8 fences / 4 balanced blocks; the `new:matrix-free-operator-apply.md` block (50→330) encloses the entire firm apparatus (`## Status`, signature, `## Composition-level laws`, evidence) INSIDE the fence — no cycle-019 fence-truncation defect. The firm count 22→23 arithmetic is consistent with the on-disk current value.

**edge-label-fidelity — pass.** The four `depends-on (composes)` edges are faithful constituent-uses (each substrate op appears at its named pipeline stage: `element_restrict`=G/Gᵀ, `basis_apply`=B_𝒟/B_𝒟ᵀ, `quad_point_contract`=D, `geom_factor_build`=geom carrier). The `reference`-class `lifts-kernel-impl` edge to the L1 kernel-impl is correctly typed free/navigational (the L2 form does not block on the L1 impl). No mislabeled L_{n+1}→L_n edge; the in-line note discusses exactly the L2↔L1 relationship it labels.

**plan-kind-consistency — warning (load-bearing; see Issue 1).** The content shape (full Status/Signature/Laws/Cohort/Justification apparatus) matches a `firm` combinator entry, and the firm-on-positive-structure escape is correctly invoked for the laws (syntactic-identity composition facts on positive source; no test gates a composition identity). HOWEVER the `firm` status rests on a §(h) well-foundedness cap that is NOT satisfied against current on-disk state — see Issue 1. The kind/content shape is internally consistent; the warning is on the firm-claim's dependency precondition, which is conditional on an uncommitted sibling report.

**skill-uptake-survey — pass.** The report references `citecheck --anchor` self-verification throughout (Status line, Verified-against block, Supporting evidence) — appropriate skill uptake for an L0-citing firm harvest.

**(graded check 9) rank-invariant — warning.** Same root as Issue 1: on disk `element_restrict` and `geom_factor_build` are `rank: rough-in` (rank 2; promoted roadmap_goal→rough-in in c124 D4, NOT firmed). A `firm` (rank 3) entry resting on two rank-2 `depends-on` deps violates `rank(u) ≤ min(deps)` against current disk state. It holds ONLY if the sibling D1 report firm-flips them first (see Issue 1).

**(graded check 10) reachability — pass.** Pulled-by chain documented: `fe_assemble` (firm spine consumer) → the fe_assemble fold's feature-column inbound edges → feature root; the `reference`-class lift edge inherits that reachability. Reachable from a feature root over the consumer chain.

### Issues found

**Issue 1 (plan-kind-consistency / rank-invariant; medium severity; sequencing-conditional).** The report's central well-foundedness claim — "the four `depends-on (composes)` substrate deps are all firm … `element_restrict` + `geom_factor_build` (c125 D1)" (CYCLE.md frontmatter scheme-comment, §Status, §Summary "Landed maturity") — is FALSE against current on-disk state: `book/src/L1/element_restrict.md` and `book/src/L1/geom_factor_build.md` are both `rank: rough-in` (rank 2) on disk. `basis_apply` and `quad_point_contract` ARE firm (c124 D3), as claimed. The firming of the other two is the job of the SIBLING report `reports/2026-06-07T124519Z-harvester-substrate-firm-flip/` (same `124519Z` cycle, "L1 firm-flip cohort — element_restrict + geom_factor_build + libceed-quadrature-kernel-impl rough-in → firm"), which is NOT yet integrated. The report is transparent about this — it explicitly sequences itself "wave-2 after D1" and notes "the per-report integrator wires its edges onto the firm-on-disk substrate" — and integrator-per-report runs serially, so the cap WILL hold IFF D1 integrates first. This is a genuine integration-ordering precondition, not a content error, but the `firm` status is conditional on an uncommitted sibling and the on-disk substrate currently contradicts the cap. Surface for the integrator: this report MUST be applied AFTER `harvester-substrate-firm-flip` (and that report must succeed in firming both ops); if D1 is rejected or deferred, this entry's `firm` claim becomes a hard rank-invariant violation and must be downgraded to `rough-in` (or held). The dep-map row and L2/index narrative likewise both assert "all firm after c125 D1" — same conditional.

(No other issues. The NO-L2-L1-theme decision, sum-factorization transparent-trick classification, matrix-free/assembled-COO duality framing, the speculative L4 placeholder being held as an Open-question rather than a stranded roadmap_goal — all verified correct. The L4 placeholder reasoning, in particular, is sound: no inbound blocking consumer reaches a feature root yet, so a roadmap_goal would strand; deferring to the c126/batch-41 L4 backend-lowering dispatch is the right call.)

---
repaired_at: 2026-06-07T130940Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

## Repair

### Fixes attempted

- **Finding** (Issue 1 — plan-kind-consistency / rank-invariant, sequencing-conditional): the `firm` claim rests on four `depends-on (composes)` substrate deps described as firm "after c125 D1," but `element_restrict` + `geom_factor_build` are still `rank: rough-in` on disk (D1 firms them, not yet integrated). So the §(h) well-foundedness cap `rank(firm) ≤ min(deps)` holds only if D1 integrates BEFORE D2.
- **Decision**: repaired (as an integrator-ordering instruction; not a content fix).
- **Action**:
  1. Verified the CYCLE.md dep-firmness wording is already correctly conditioned on D1 throughout — every load-bearing assertion attributes the firmness of `element_restrict` + `geom_factor_build` explicitly to "c125 D1" (frontmatter scheme-comment line 9; §Status lines 44–45, 58–59, 69; §Summary lines 109–110; dep-map row line 348 "all firm after c125 D1"; L2/index narrative line 340; line 419). The report is transparent that it is sequenced "wave-2 after D1" and that "the per-report integrator wires its edges onto the firm-on-disk substrate." No CYCLE.md content edit was required — the conditional-on-D1 wording is already present and accurate as a description of the intended post-D1 state. (The bare "are all firm" in the line-58 comment is immediately qualified in the same parenthetical by the c124-D3 / c125-D1 attribution, so it is not a misstatement of current disk state in isolation.)
  2. Recorded the integration-ordering precondition for the integrator (see Suggested resolution).
- **Rationale for treating this as repaired-via-ordering, not unrepairable**: the precondition is *satisfiable by serial integration ordering* — it is not a contradiction with existing artifact content, not a missing surface/rotation/variant-axis argument, and requires no substantive authoring. The sibling D1 report IS ready, and `integrator-per-report` runs serially, so the cap WILL hold once D1 lands first. This is a mechanical sequencing constraint, in scope for repair, not a content defect for the abstractor to re-author.

### Unrepairable findings

None. (Issue 1 is resolved by an integration-ordering instruction; no deferral needed.)

## Suggested resolution

`overall_status: ready`. Integrator instructions (load-bearing ordering precondition):

1. **Apply D1 before D2 in the serial integration.** This report (D2, `reports/2026-06-07T124519Z-abstractor-matrix-free-operator-apply/`) MUST be applied AFTER the sibling D1 report `reports/2026-06-07T124519Z-harvester-substrate-firm-flip/` (same `124519Z` cycle — the L1 firm-flip cohort: `element_restrict` + `geom_factor_build` + `libceed-quadrature-kernel-impl` rough-in → firm). Apply D1 first so the four `depends-on (composes)` substrate deps are firm on disk when D2's `firm` edges land — that satisfies the §(h) well-foundedness cap `rank(firm) ≤ min(deps)`.
2. **Contingency.** If D1 is rejected or deferred (i.e. `element_restrict` / `geom_factor_build` remain `rough-in` on disk), then D2's `firm` status becomes a hard rank-invariant violation and MUST be downgraded to `rough-in` (or held) at integration — do not land the `firm` claim against a rough-in substrate. The same conditional applies to the dep-map row and the L2/index narrative ("all firm after c125 D1").
3. After applying both in order, the rank-invariant linter (`tools/graded-stack-lint`) should pass on the new `firm` D2 edges; if it flags, D1 did not land first and the apply order is wrong.
