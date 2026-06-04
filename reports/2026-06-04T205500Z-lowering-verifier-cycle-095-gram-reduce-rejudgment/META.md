---
verifies: ../REPORT.md
critiqued_at: 2026-06-04T211500Z
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

# META: verification of "Audit gram_reduce — firm re-judgment under the discharged bilinear-form gate" (cycle-095 D3)

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` on the report: 28 ok, 2 `[AMBIG]` (basename-only `dot.md:100` / `apply_linop.md:87` matched 5/3 files) — NOT bounds drift; the report's frontmatter and §Citation A cite the **full** paths `book/src/L1/dot.md:100` + `book/src/L1/apply_linop.md:87`, both of which I confirmed `[ok]` via `--anchor 'firm'`. All four L0 Gram witnesses anchor `[ok]` with the report's exact tokens: `electrostaticsolver.cpp:118-119` (`M_elec`@118, `Dot`@119), `:139-140` (`Invert`@140), `magnetostaticsolver.cpp:129-131` (`M_mag`@129, `Dot`@131), `:151-152` (`Invert`@152) — zero drift, reproducing the report's §Citation C claim exactly. The dep status lines anchor `[ok]`: `matrix-weighted-norm.md:110` (`firm`), `solve_family.md:4` (`firm`). All internal gram_reduce line references are accurate on disk: entry fold `:88-90`, §Algebraic laws `:132`, §Status head `:228`, §Context off-diagonal `:58-60`, §Dependencies bilinear-form row `:198-199`. The `verified_against:` block (7 entries) was extracted and `yaml.safe_load`-round-tripped cleanly (7 entries parsed; no `ParserError`); every `note:` value begins with a non-quote prose character, no leading-`'`/`"` scalar hazard.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (flip of an existing chapter's `## Status` + frontmatter). It modifies surface (the §Status block, the §Context/§Dependencies rough-in labels, the typed `edges:` frontmatter) AND carries the supporting evidence (the firm-on-positive-structure escape substrate: §Algebraic laws as syntactic identities on the fold, the two positive PostprocessTerminals witnesses, the four direct-dep firmness reads). Not a pure rotation_claim. Record-definition sub-check: gram_reduce's signature names no new record (`LinearOperator`, `[Tensor]`, `Matrix`, `Scalar` are pre-defined vocabulary; the result is a bare `Matrix[m,m]`, not a named struct) — no definition-home obligation triggered.

**rotation-quality — pass (not the operative kind).** This is a `lowering-verifier` firm re-judgment, not an algebraic/structural rotation proposal. It asserts no new L_{n+1}→L_n compaction; it re-judges an existing L4 verb's maturity. No 1:1-rename smell to evaluate. Marked pass as inapplicable to the audit/re-judgment kind.

**variant-axis-coverage — pass.** The verb's variant axes (normalization-weight unit|current-normalized; operator-source; element-type; family-index-domain) are enumerated in the proposed frontmatter `variant_axes:` and each is dispositioned (absorbed into the `w` closure / `K` / `[Tensor]`, or pinned for the two witnessed pipelines). The load-bearing normalization-weight axis is explicitly named the variant axis (not a break-witness), consistent with the 2-of-N scope. No hidden branch — the firm flip is correctly stated NOT to widen scope (a law-confidence judgment, not a witness-count change).

**cross-reference-integrity — pass.** Every link target in the proposed edits resolves on disk: `../L1/matrix-weighted-norm.md`, `../L1/bilinear-form.md`, `./solve_family.md`, `./inner_product.md`, `./linear_combination.md`, `./domain_energy_reduce.md`, `./eigenfreq_qfactor_reduce.md`, `./sparameter_reduce.md` — all present. Maturity claims on linked siblings verified: `domain_energy_reduce.md:4 firmness: firm` (the c091 same-cascade-family precedent the report leans on), confirming the "materially identical disposition" claim. No firm-body-inside-fence concern: this is a status-flip of an existing chapter with the full apparatus already on disk, not a new firm chapter authored outside a fence.

**edge-label-fidelity — pass.** The typed `edges:` block declares `depends-on: [L1/matrix-weighted-norm, L1/bilinear-form, L4/solve_family]` + `reference: [L4/inner_product, L4/linear_combination]`. I verified these are the **direct** folds/consumes of the gram_reduce body (`:88-90` folds `matrix_weighted_norm`/`bilinear_form`; consumes `solve_family`) and the two siblings are genuinely navigational. The report's deliberate divergence from the dispatch brief's literal transitive list (`dot`/`apply_linop`) is CORRECT: `dot`/`apply_linop` are deps **of** bilinear-form, reached transitively; restating them as direct gram_reduce edges would create false first-class edges for the rank/GC linters. The rank invariant holds: `rank(gram_reduce = firm = 3) ≤ min(matrix-weighted-norm = 3, bilinear-form = 3, solve_family = 3) = 3`. The `reference`-edge-constrains-nothing rule is respected (the siblings are not rank inputs).

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit yielding a DISCHARGE → firm re-judgment; content shape matches (per-citation audit, applicability-conditions table, algebraic-law re-derivation, proposed status-flip + typed-frontmatter + `verified_against:` block). The escape applied (firm-on-positive-structure, c083 two-condition narrowed form) is correctly invoked: condition-(i) all folded primitives firm — satisfied; condition-(ii) the absent dedicated test gates no law lacking other evidence — satisfied (laws 1-4 are syntactic identities on the fold over firm halves). No firm/rough-in misclassification: the verb genuinely promotes (the sole residual gate, bilinear-form, is discharged by D1).

**skill-uptake-survey — pass (telemetry).** The report's shape implies the citation-range / anchor skill and the partly-constructive/firm-promotion skill family; the report explicitly records citecheck `--anchor` `[ok]` runs on all four L0 witnesses and applies the firm-on-positive-structure / c083 narrowed-escape promotion rule by name with its four sibling precedents. Skill uptake is present and load-bearing. Non-blocking.

### Issues found

No blocking issues. Two non-defect observations surfaced for downstream awareness (the report already self-discloses both; recording here so the integrator does not treat them as critic-missed):

- **Serial-integration sequencing precondition (already flagged by the producer; not a report defect).** `book/src/L1/bilinear-form.md:4` reads `firmness: rough-in` on disk at audit time. This D3 firm flip is rank-valid ONLY after D1 (Wave 1) lands the bilinear-form rough-in→firm flip first. The report discloses this thoroughly (§Per-citation-audit Citation A note; Open-questions "bilinear-form on-disk frontmatter still rough-in"). If D1 does NOT land before D3, applying D3 would create a transient rank violation (firm gram_reduce on rough-in bilinear-form) — the rank linter is the intended safety net. This is correct disclosure of an ordering dependency, not a citation/evidence defect. Severity: informational (integrator sequencing).
- **Pre-existing cross-file staleness correctly routed out-of-scope (not this report's to fix).** The report flags `book/src/L4/solve_family.md:154` (stale "matrix-weighted-norm √-cascade NO-GO-HELD" + "plain-rough-in matrix-weighted-norm" narrative, both overturned by c091/c095) and `book/src/L4/index.md:101` (gram_reduce dep-map cell still `rough-in (test-coverage-bounded)` + bilinear-form "(rough-in…residual gate)" label). I confirmed both locations carry exactly the stale text described. Both are correctly OUTSIDE the report's HARD scope (gram_reduce.md own status/frontmatter only) and correctly FLAGGED for D4/integrator rather than edited. Note for the integrator: applying this D3 flip without the coupled `index.md:101` cell update + `solve_family.md:154` re-anchor leaves the index/narrative momentarily inconsistent with the chapter — these are the producer's flagged carry-forward items, not silent gaps.

Separately noted (not attributable to this report): `book/src/L1/matrix-weighted-norm.md` has a frontmatter/§Status discrepancy — `:4 firmness: rough-in` vs `:110` §Status `firm`. The report correctly cites `:110` (the authoritative §Status) for the firmness claim, so its rank-invariant input is sound; the stale frontmatter line is a defect in a *different* file outside this report's scope (worth an integrator/D4 awareness ping but not a finding against D3).
