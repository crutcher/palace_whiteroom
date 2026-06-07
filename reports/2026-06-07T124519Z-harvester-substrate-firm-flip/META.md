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
repaired_at: 2026-06-07T131500Z
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

# META: verification of "Firm-flip the libCEED contraction substrate — element_restrict + geom_factor_build + libceed-quadrature-kernel-impl (45 → 47)"

## Critique

### Checks run

**citation-validity — warning.** `citecheck --scan` over the report returns `34 ok, 0 failing` (bounds + path hygiene clean, no doubled `reference/palace/palace/...` paths). All seven load-bearing L0 anchors the firm-on-positive-structure escape rests on were re-confirmed via `citecheck --anchor` on-disk this dispatch: `InitRestriction` (restriction.cpp:389 ✓), `CeedElemRestrictionCreate` (:200 ✓), `trial_restr` (bilinearform.cpp:64 ✓), `AssembleCeedGeometryData` (integrator.cpp:335 ✓), `geom_data_size` (:395 ✓), `AssembleCeedOperator` (:423 ✓), `Assemble` (integrator.hpp:58 ✓) — every anchor literal resolves at the cited line. The `verified_against:` YAML block round-trips cleanly under `yaml.safe_load` (no leading-quote-of-either-kind defect — each `note:` begins with prose). The ONE drift: the precondition note at report `:49` and the supporting-evidence note at `:657` cite `concepts/element-local-tensor.md` `## Status` at `:155`, but on-disk the `## Status` heading is at `:153` (a +2 drift). This is an internal-artifact working-note pointer (NOT a proposed-changes-block citation and NOT an L0 anchor), so its blast radius is cosmetic, but it is a genuine off-by-two on a stated line and warrants a warning. The `frontmatter :2` half of the same pointer is correct (`rank: firm` is at `:2`).

**surface-or-evidence — pass.** This is a refinement-shaped proposal (rough-in → firm status flip on three existing operators). Each flip modifies surface (the §Status paragraph + frontmatter `rank:` + the algebraic-laws framing) AND carries evidence: the firm-on-positive-structure escape is invoked with re-checked positive L0 anchors for each operator, plus the well-foundedness lift from the now-firm shape home. The signatures name no undefined record — the shape carriers (`Tensor[(E, L)]` / `[E, P, C]` / `[E, P, G]`) have their definition home at the firm `concepts/element-local-tensor` page (verified on disk), which each operator references via a `depends-on (shape-vocabulary)` edge + a §Related link. Record-definition obligation satisfied (defined-elsewhere-and-referenced case, not described-only-by-use).

**rotation-quality — pass (no-op).** Not applicable to this report's shape — it is a maturity-tier flip + an index tally reconcile, not an algebraic/structural rotation claim. No L_{n+1}→L_n rotation is asserted; the operators stay at L1.

**variant-axis-coverage — pass.** The variant axes the operators carry (lexicographic-vs-native restriction ordering; the `𝒟`-determined geometry-metric shape `|J|` vs `J⁻ᵀJ⁻¹|J|`; partial-vs-full assembly; oriented H(curl)/H(div) dofs) are each explicitly named and either folded as interior details or scoped out (multi-rank `ParMesh` overlap read single-rank per DIRECTIVE-1). No hidden branch surfaced.

**cross-reference-integrity — pass.** All twelve distinct link/slug targets referenced in the proposed-changes resolve on disk (element_restrict, geom_factor_build, libceed-quadrature-kernel-impl, basis_apply, quad_point_contract, fe_assemble, weak_form_term, interpolator, concepts/element-local-tensor, concepts/tensor-field-lift, concepts/build-time-vs-run-time-stratification, L1-L0/fe-assemble-libceed-boundary-obstruction). All five `book/src/L1/index.md` edit-target anchors are unique on disk (grep count = 1 each: the 4a Firm header, the 4b kernel-impl bullet, the 4c substrate sub-spine header, the 4d AMR cross-ref, and each of the three 4e dep-map rows) — the edits will apply cleanly. **Build-readiness / firm-body-inside-fence guard: pass** — fence parity is even (22 fences); each of the three firm-operator `edit:` blocks fully ENCLOSES its `## Status` + Signature + Algebraic-laws + Verified-against (Status headings at report lines 107, 234, 391 sit inside their respective edit fences). No fence-truncation defect. **Maturity-claim integrity (load-bearing here):** the well-foundedness invariant holds — all four kernel-impl `depends-on (composes)` deps are firm on disk (`basis_apply` `rank: firm`, `quad_point_contract` `rank: firm`, plus `element_restrict` + `geom_factor_build` firmed in THIS report), and the shape-home `concepts/element-local-tensor` reads `rank: firm` (`:2`) — so `rank(impl) ≤ min(deps) = firm` is satisfied. The kept kernel-api obstruction surface (`fe-assemble-libceed-boundary-obstruction.md`) still reads `status: obstruction` on disk and is untouched by the proposed-changes (not downgraded), and the `realizes-kernel-api` edge is correctly placed under the `reference:` block (free, navigational), NOT `depends-on:`.

**edge-label-fidelity — pass.** The report carries no L_{n+1}→L_n lowering edge label; the `realizes-kernel-api` / `realizes-leaf` / `pulled-by` reference labels each have prose that discusses the exact edge (impl→api correspondence; impl as constructive interior of fe_assemble's opaque leaf; the consumer pull). No mislabeled edge.

**plan-kind-consistency — pass.** Declared kind is a harvester firm-flip (rough-in → firm) + a sole-owned index tally reconcile; the content shape matches — three full firm apparatus bodies (Status + Signature + firm Algebraic-laws + Verified-against) with no rough-in placeholders, plus the arithmetic-reconciling index edits. No mis-classification.

**skill-uptake-survey — pass.** The report references the relevant procedural skill invocations it implies: `citecheck --anchor` for the anchor re-checks (the firm-on-positive-structure escape re-verification) and the firm-on-positive-structure escape itself (the partly-constructive/firm-flip promotion discipline). The well-foundedness reasoning is shown explicitly. Pure presence check, satisfied.

### Issues found

1. **citation-validity (warning, cosmetic):** `reports/.../CYCLE.md:49` precondition note and `:657` supporting-evidence note cite `concepts/element-local-tensor.md` `## Status` at `:155`; the on-disk `## Status` heading is at `:153` (+2 drift). This is a working-note/internal-artifact pointer, not a proposed-changes-block citation or an L0 source anchor — corrected line is `:153`. Severity low (no claim or build artifact rests on it; the `rank: firm` half of the pointer, `:2`, is correct). Candidate for a one-character repair (155 → 153) in both notes.

No load-bearing issue found. The three firm flips are well-founded (all deps firm on disk), the firm-on-positive-structure escape's anchors all re-confirm via `citecheck --anchor`, the 45→47 tally arithmetic is correct (33+4+5+1+4=47) and the new 4a header drains the stale 45/43 multi-era count-history to a single clean current 47, the `realizes-kernel-api` edge stayed reference-class, the kept obstruction surface is untouched, and the owed lowering-verifier empirical-match re-audit (against `test-libceed.cpp:284 TestCeedOperatorFullAssemble`) is correctly flagged-not-dispatched (non-blocking; the firm-flip changes only rank, the c124 D2 structural audit already confirmed the correspondence faithful).

---

## Repair

### Fixes attempted

- **Finding**: citation-validity (warning, cosmetic) — CYCLE.md `:49` precondition note and `:657` supporting-evidence note cite `concepts/element-local-tensor.md` `## Status` at `:155`; on-disk the `## Status` heading is at `:153` (+2 drift).
- **Decision**: repaired
- **Action**: Verified on-disk first (`grep -n "^## Status" book/src/concepts/element-local-tensor.md` → `153:## Status`). Corrected the off-by-two in both working-note pointers in CYCLE.md: `:49` (`## Status` `:155` → `:153`) and `:657` (`concepts/element-local-tensor.md:2,155` → `:2,153`). Both are internal-artifact working-note pointers, not proposed-changes-block citations or L0 source anchors — purely cosmetic, blast radius nil. The correct `:2` frontmatter half of each pointer was left untouched.

### Unrepairable findings

None.

## Suggested resolution

`ready`. The sole finding was a cosmetic +2 line-offset on a working-note pointer, now corrected (verified against on-disk). All other checks passed at critique. No content authoring was required; the firm-flip apparatus, anchors, tally arithmetic, and edge-class placement were all clean at critique. Integrator may apply.
