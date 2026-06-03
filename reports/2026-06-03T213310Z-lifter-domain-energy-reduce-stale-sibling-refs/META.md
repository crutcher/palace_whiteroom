---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T214500Z
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

# META: verification of "Re-anchor domain_energy_reduce stale sibling-verb maturity refs"

## Critique

### Checks run

**citation-validity — pass.** The report asserts no L0 `path:lo-hi` pinpoint was touched (the two edits are artifact-internal prose about sibling-chapter maturity; the only line-number references in the edited spans are `c080`/`c077`/`c082` cross-cycle provenance tags, not source ranges), so `citecheck --anchor` was correctly not invoked. I confirmed both `[old]` blocks match on-disk EXACTLY: the line-212 parenthetical (`book/src/L4/domain_energy_reduce.md:212-215`) and the line-290 §Status contrast (`:289-291`) are byte-for-byte the on-disk text. The supporting status reads cited as evidence are accurate: `eigenfreq_qfactor_reduce.md:4` is `firmness: firm`, and `:185-211` carries the firm-on-positive-structure reasoning naming both folded L1 primitives (eigenvalue-untransform c080, participation_ratio c077) as firm. No `verified_against:` block is emitted, so that sub-check no-ops. No citation was altered.

**surface-or-evidence — pass.** This is a refinement-shaped change (modifies existing chapter prose). It is a pure retroactive-correctness / hygiene rewrite — correcting stale and factually-wrong sibling-maturity prose against the new on-disk reality (c082/c083 promotions) — which is the allowed retroactive-evidence-backfill shape; it asserts no new per-op algebraic claim of its own. The supporting status-read citations back the correction. Record-definition sub-check: no NEW record is named in a signature by these edits (the chapter's `DomainOpMap`/`DomainData` definition homes are untouched and already on-disk), so the sub-check no-ops.

**rotation-quality — pass.** Not applicable. This is an L4-chapter prose-hygiene pass; it asserts no algebraic/structural/reduction rotation and changes no lowering relationship.

**variant-axis-coverage — pass.** Not applicable. The edits touch only sibling-maturity prose; the chapter's variant axes (field-kind, element-type, partition-coverage) are untouched.

**cross-reference-integrity — pass.** All `[link]` targets in the `[new]` blocks resolve on disk: `./eigenfreq_qfactor_reduce.md`, `../L1/eigenvalue-untransform.md`, `../L1/participation_ratio.md`, `../L1/matrix-weighted-norm.md` all exist. No build-readiness fence guard applies (this is an `edit:` prose patch, not a firm-body authoring; no `## Status` body is enclosed/re-authored). The incompleteness sub-concern (a MISSED stale ref) was spot-checked and cleared: line 298's `sparameter_reduce` reference is purely a scope-SHAPE claim ("single-witness-driven-by-design scope") carrying NO maturity token, so it is maturity-neutral and correctly left untouched (the report's honest "optional polish, not a correctness fix" framing); the gram_reduce refs at lines 31, 132, 178-180, 216-217 are all rank-2 / over-unification-guard SHAPE claims (the `(reduce-to-matrix)` at :216 is a rank descriptor, not a maturity token) — gram_reduce is genuinely still rough-in on disk, and none of these refs overclaims it as firm. No stale ref was missed.

**edge-label-fidelity — pass (load-bearing, verified).** The sibling maturities are correct on disk: `eigenfreq_qfactor_reduce` `firmness: firm` (c082), `sparameter_reduce` `firmness: firm` (c083), `gram_reduce` `firmness: rough-in (test-coverage-bounded)`, `participation_ratio` `firmness: firm` (c077), `matrix-weighted-norm` body §Status `rough-in (test-coverage-bounded)` (the L1 file has no YAML frontmatter; its status is stated at `:108-110`, with the cycle-080 √-overload-entry-point gate at `:143`). The re-narrated gating logic at line 290 is accurate: `domain_energy_reduce` stays rough-in because its OWN folded `matrix-weighted-norm` energy form is rough-in (the √-entry-point gate), NOT because firm siblings are rough-in — this is consistent with the chapter's own §Status point 1 (`:274-278`) and frontmatter (`:7`), and the firm sibling's firm-on-positive-structure escape (both its folded primitives firm) is correctly stated against `eigenfreq_qfactor_reduce.md:185-211`. The old line-290 text ("also rough-in for the same primitive-maturity + no-dedicated-test reasons") was indeed factually wrong on current on-disk maturity and on the gating logic; the correction is faithful.

**plan-kind-consistency — pass (scope bound honored).** The declared kind is a LOW/hygiene pure-rewriting pass, and the content matches: two surgical prose edits, no structural/signature/decomposition change. The critical scope bound is honored — `domain_energy_reduce`'s OWN `## Status` token (`:268` `rough-in`) and frontmatter `firmness: rough-in` (`:4`) are UNCHANGED (neither edit touches them). The column-promotion USER DIRECTIVE was not pre-empted; no feature column was touched (the `energy-fields` references are not modified). No promotion occurred.

**skill-uptake-survey — pass.** The report's shape (sibling-maturity reference re-anchoring) does not strongly imply a dedicated skill invocation; the report correctly notes citecheck `--anchor` was not required (no L0 pinpoint changed) and that `verify-citation-range`'s inherited-precedent re-anchor sub-case would be the nearest relevant procedure but is unnecessary here since no source range moved. Telemetry only; non-blocking.

### Issues found

None. All eight checks pass. The two edits are byte-accurate against on-disk `[old]` text, the corrected sibling maturities match disk, the re-narrated gating logic is factually correct and internally consistent with the chapter's own §Status, all new cross-links resolve, the scope bound (no own-status promotion, no column touched) is honored, and the claimed-untouched refs (line 298 sparameter_reduce, the gram_reduce shape refs) are genuinely maturity-neutral with no missed stale reference. Clean hygiene pass.
