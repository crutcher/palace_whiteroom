---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T191500Z
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

# META: verification of "Audit matrix-weighted-norm 2nd (test-coverage) gate"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` over the report: 11 ok, 1 ambiguity warning (`operator.cpp:616-617`, an in-prose applicability-condition reference that is basename-only; both candidate files exist and the surrounding prose makes the intended `linalg/operator.cpp` unambiguous — a non-load-bearing path-hygiene nit, not a bounds failure). All 7 load-bearing anchors the report claims `ok` were re-run with `--anchor` and confirmed: `GetElectricFieldEnergy@:83`, `expected_energy_SI@:90`, `WithinRel@:93` (test); `GetElectricFieldEnergy@:219`, `LocalDot@:224`, `0.5@:231` (energy-form body); `std::sqrt@:606` (real Norml2). The complex-specialization `std::sqrt@:618` within `:609-619` also confirmed. I read the two backing source ranges directly: `domainpostoperator.cpp:219-231` returns `0.5 * dot` with no `sqrt` and never calls `Norml2` (exactly as claimed), and `test-domainpostoperator.cpp:75-93` asserts against `0.5·ε₀·E₀²·V` via `WithinRel(..., 0.01)` (exactly as claimed). The `verified_against:` YAML round-trip sub-check: extracted the appended block and ran `yaml.safe_load` — round-trips cleanly (3 entries); each `note:` value begins with prose (`GetElectricFieldEnergy...`/`the named...`), not a leading quote, so no scalar-parse hazard.

**surface-or-evidence — pass.** This is a refinement-shaped proposal that modifies surface (Edit 1 rewrites the §Status gate-(a) bullet + Evidence line + appends `verified_against:`; Edit 2 refines the L4 consumes note) AND carries the audit evidence (the test + body + entry-point citations) — the lowering-verifier audit shape. The record-definition sub-check is N/A: no new record/struct is named in a signature here (the audit touches an existing L1 norm operator and an existing L4 reduce verb, both already defined).

**rotation-quality — pass (not applicable to audit kind).** This is a test-coverage audit of an existing L1 operator entry, not a rotation claim. No L_{n+1}→L_n compaction is asserted, so the rotation-quality bar does not apply. The substance the dispatch asked me to vet — the partially-supported verdict and the firm-on-positive-structure escape-ruling — is sound: I confirmed from source that the energy form covers only the radicand `⟨E, M_elec E⟩` + `½` and omits the outer `√`/`Norml2` entry point, so "radicand covered, √-overload entry point still uncovered" is the correct partial verdict. The escape-ruling is also sound: laws 4/6/7 (triangle, Cauchy–Schwarz, parallelogram) carry genuine inner-product-structure content not verifiable by the source (which neither checks `B` Hermitian nor proves sub-additivity), so they are NOT syntactic identities — correctly the `eigsolve`-convergence-semantics situation, not the `apply_linop` all-syntactic situation. Withholding firm promotion is justified.

**variant-axis-coverage — pass.** The applicability-conditions section enumerates the variant axes (square `B`, Hermitian `B`, SPD `B`) and explicitly scopes which the test exercises vs. leaves uncovered (real-field-only ⇒ imaginary branch `:225-229` untested; SPD-strict guard at the named entry point untested because the energy form never sqrt's). No hidden branch; the complex/Hermiticity and SPD-guard gaps are named, not glossed.

**cross-reference-integrity — pass.** Verified every edit target resolves to the claimed on-disk line: L1 `matrix-weighted-norm.md:113` is the gate-(a) bullet (Edit 1 target), `:143` is the closing "No direct test evidence" Evidence line (Edit 1 target), and the file has no pre-existing `verified_against:` block (so the append is non-colliding). L4 `domain_energy_reduce.md:7` is the `matrix-weighted-norm` consumes line (Edit 2 target), and `:274-283` already correctly state the double-gate (Edit 2 leaves them unchanged, as the report claims — confirmed verbatim). The coupled re-anchor is the single direct critical-path consumer, consistent with "no broad sweep on a non-promotion verdict." Both linked chapters exist; the `participation_ratio.md` and `matrix-weighted-norm.md` cross-links in the L4 consumes block resolve.

**edge-label-fidelity — pass (not applicable).** No lowering-edge label is carried; this is an L1 operator entry audit + a coupled L4 consumer note, not an L_{n+1}→L_n theme. The report explicitly records "No directionality violation" (it is not a rewrite narration).

**plan-kind-consistency — pass.** Declared kind is a `lowering-verifier` audit with verdict "partially-supported — sharpen the warrant, NO firm promotion." Content matches: the status token stays `rough-in (test-coverage-bounded)` (confirmed unchanged on disk), `domain_energy_reduce` stays `rough-in`, and the report asserts +0 firm delta with D2 (harvester) as sole tally owner — consistent with a sharpen-warrant audit, not a promotion. No mis-classification.

**skill-uptake-survey — pass.** The audit's shape implies the citation-range/`citecheck --anchor` procedure (the `verify-citation-range` skill's mechanical realization), which the report invokes throughout (every per-citation entry records its `--anchor ok` result). The `verified_against:` block convention is also followed. Telemetry present; no gap.

### Issues found

None blocking. One non-load-bearing nit for awareness (not a defect requiring repair):

- **CYCLE.md §Applicability conditions** — the in-prose reference `operator.cpp:616-617` is basename-only and `--scan` flags it `[AMBIG]` (two `operator.cpp` files in the tree). The surrounding prose makes the intended `linalg/operator.cpp` clear and the line is descriptive rather than a load-bearing pinpoint, so this does not gate the citation-validity check; noting it only as a path-hygiene observation should the producer wish to fully-qualify it.

All 8 checks pass; the report is clean. `overall_status: ready` set (no repairer will run).
