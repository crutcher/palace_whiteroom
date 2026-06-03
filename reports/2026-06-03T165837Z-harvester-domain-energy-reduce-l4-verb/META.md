---
verifies: ../REPORT.md
critiqued_at: 2026-06-03T173000Z
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
repaired_at: 2026-06-03T174500Z
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

# META: verification of "Formalize domain_energy_reduce at L4"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` on the report: **24 ok, 0 failing**, matching the report's claim. Path-hygiene + range-bounds are clean on every citation. I then `--anchor`-verified the load-bearing pinpoints:

- `postoperator.cpp` (the per-domain loop): ALL correct. `MeasureDomainFieldEnergy` def at `:1021`; the electric guard `std::abs(energy_i) > 0.0` at `:1039` (numerator); the magnetic guard `std::abs(energy) > 0.0` at `:1064` (denominator); the whole-domain totals `:1033`/`:1058`, set-once `:1034`/`:1059`; field selection `:1031-1032`. The report's headline **+1 drift correction** (guards on `:1039`/`:1064`, NOT codemap's `:1038`/`:1063`) is **confirmed accurate** — `--anchor` lands the guard literals exactly on the cited lines. The inconsistent-guard finding is real and faithfully transcribed.
- `domainpostoperator.cpp` (the energy form): range-level citations PASS (`:255-275`, `:255-298`, `:277-297`), and the load-bearing endpoints `return 0.5 * dot` at `:274` (electric) / `:296` (magnetic) are correct. **BUT the fine-grained sub-line pinpoints inside the energy-form body drift +3–4 lines** (the same brace-boundary drift family the report self-corrected for `postoperator.cpp`, but left UNcorrected here):
  - cited `:261-262` for `if (!it->second.first) return 0.0` → on-disk `if` is `:262`, `return 0.0` is `:264`.
  - cited `:261-262`/`:261` for the `it->second.first->Mult(E.Real(), D)` apply + null-return → apply is on-disk `:266`, null guard `:262`.
  - cited `:263` for `double dot = linalg::LocalDot(E.Real(), D)` → on-disk `:267`.
  - cited `:264-268` for the imaginary radicand `if (E.HasImag()) {…}` → `HasImag` is on-disk `:269`; the range `:264-268` actually spans the null-return through the real-`LocalDot`, not the imag block.

  The CITED CODE EXISTS and supports every claim (the form IS `0.5 * LocalDot(field, M·field)` with a null→0 guard and a complex-field radicand sum) — only a few lines lower than the pinpoint says. Meaning is fully backed; the defect is sub-line locator drift on the `domainpostoperator.cpp` fine pinpoints. Hence `warning`, not `fail`. The `verify-citation-range` brace-boundary lesson the report applied to `postoperator.cpp` was not extended to the `domainpostoperator.cpp` body.

No `verified_against:` YAML block in this report (harvester, not lowering-verifier) — that sub-check is not applicable.

**surface-or-evidence — pass.** This is a NEW L4 verb (not a refinement of existing surface), so the refinement-surface fork is not the governing case; the verb is backed by positive source (the `MeasureDomainFieldEnergy` loop + the `GetDomain{Electric,Magnetic}FieldEnergy` form). **Record-definition sub-check: pass.** The signature `domain_energy_reduce :: DomainOpMap -> Field -> Scalar -> [DomainData]` names two records. `DomainOpMap` gets an in-chapter `## Record definition` section (single-consumer case): a field/type/meaning table (key `idx : int`, value `M_idx : (LinearOperator?, LinearOperator?)`), a construction-vs-run-time stratum note (construction-time, readonly), an L0 source home (`domainpostoperator.hpp:42`), and the "signatures that name it" list — well-formed and complete. I verified the L0 backing against source: `std::map<int, std::pair<std::unique_ptr<Operator>, std::unique_ptr<Operator>>> M_i` at hpp:42 — the table's key/value/null-operator semantics mirror it faithfully. The `DomainOpMap`-vs-`DomainData` distinctness claim HOLDS: `M_i` is the INPUT operator map; `DomainData{idx, energy_i, participation_ratio}` (confirmed at `postoperator.cpp:1040-1041`, `:1065-1066`) is the OUTPUT row, defined in `energy-fields.L4.md` and watched by OQ `record-DomainData-needs-definition-home`. The report correctly does NOT re-define `DomainData` here and routes its definition home elsewhere.

**rotation-quality — pass.** Not the governing concern for an L4 verb authored as the entry of an algebra-of-folds (the verb COMPOSES firm/rough-in L1 primitives into a new combinator surface; the lowering is identity-in-form on the body, in-line-marker route — the same pattern as the firm `eigenfreq_qfactor_reduce`/`inner_product`/`gram_reduce`). The verb makes the per-domain readout structural (a `map`-then-collect list-homomorphism over the domain set, replacing the explicit C++ `emplace_back` loop) — a genuine abstraction step, not a rename. No dedicated L4>L3 theme is authored, consistent with the cited sibling precedent. Pass.

**variant-axis-coverage — pass.** Three axes are declared in frontmatter and each is dispositioned: field-kind (electric/magnetic — the load-bearing axis, absorbed into the `(M_idx, field)` pair, reduction runs twice, both source loops cited); element-type (complex field → real-≥0 energy via real+imag radicand sum, source-cited); partition-coverage (config-conditional, gates `Σ pᵢ = 1` only, NOT the verb shape). No hidden branch — the electric/magnetic guard inconsistency is surfaced explicitly (not silently collapsed) and resolved with stated rationale. Pass.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `eigenfreq_qfactor_reduce.md`, `gram_reduce.md`, `sparameter_reduce.md`, `inner_product.md`, `dot.md`, `participation_ratio.md`, `matrix-weighted-norm.md`, `energy-fields.L4.md`, `concepts/black-box-vs-accelerated-kernels.md` — all present. The dep-map alpha-insertion is internally consistent: the on-disk `L4/index.md` dep-map row order is `…assemble_frequency_operator, dot, eigenfreq_qfactor_reduce…`, and `domain_energy_reduce` correctly sorts before `dot` (dom < dot at char 3), so "after `assemble_frequency_operator`, before `dot`" is right. The rough-in cohort header REPLACE-from text ("**Rough-in at L4 (1)** — the first solver-test-load-driven combinator, awaiting law confirmation:") matches the on-disk line `:56` verbatim, and the 1→2 tally + `solve_family`-anchored append are coherent. The SUMMARY.md alpha-position note is consistent. The energy-fields forward-refs at `:8,48,62,134,156` were confirmed to reference this slug as plain text (the integrator-upgrade-to-live-link note is well-founded). **Build-readiness fence guard: pass** — the report has 8 `^```` fence markers (4 balanced pairs); the `new:book/src/L4/domain_energy_reduce.md` block (lines 59–428) ENCLOSES the full firm/rough-in apparatus (frontmatter, `## Status`, Signature, Algebraic laws, Record definition, Evidence) INSIDE the fence; code samples use 4-space-indented blocks with no nested triple-backtick fences. No firm-body-outside-fence defect.

**edge-label-fidelity — pass.** The verb carries the in-line "Lowers to" L4→(per-domain scalar maps) edge; the prose discusses exactly that downward direction (identity-in-form on the body to the folded scalar maps, no dedicated L4>L3 theme, substantive downward content living in the L0 postoperator + the folded L1 primitives' own rotations). No mismatched edge label. Pass.

**plan-kind-consistency — pass.** Declared kind is a NEW L4 operator at `firmness: rough-in`. The content shape matches: the structure is read off positive source (firm-on-positive-structure approached) but explicitly gated to `rough-in` by (1) the folded `matrix-weighted-norm` being `rough-in (test-coverage-bounded)` — least-firm-folded-primitive governs — and (2) no dedicated per-domain participation test. The `Σ pᵢ = 1` law is correctly stated config-conditional (partition-precondition), not an unconditional identity. The uniform-guard choice (denominator guard, subsuming the numerator-guard case) is coherent and the subsumption reasoning is sound (under positive `e_total`, a zero `energy_i` yields `0/e_total = 0` regardless). No firm-claim/rough-in-placeholder mismatch. Consistent with the sibling `eigenfreq_qfactor_reduce` (also rough-in for the same two reasons). Pass.

**skill-uptake-survey — pass.** The report invokes `tools/citecheck/citecheck.py --anchor` for the citation self-verification (and surfaces the codemap drift correction through it) — the expected procedure for this report's shape. The fence-parity guard is referenced (heeded in-prose). Telemetry only; no blocking finding. (Telemetry note: had the `verify-citation-range` brace-boundary procedure been applied to the `domainpostoperator.cpp` body sub-anchors as it was to `postoperator.cpp`, the drift in citation-validity would have been caught at authoring time.)

### Issues found

1. **Sub-line citation drift in the `domainpostoperator.cpp` energy-form pinpoints** (severity: low–moderate; `citation-validity` warning). In §Algebraic laws law 2 and §Evidence "Domain-restricted energy form" bullet, the fine-grained sub-anchors are shifted +3–4 lines from on-disk:
   - `:261-262` cited for `if (!it->second.first) return 0.0` → on-disk `if` at `:262`, `return 0.0` at `:264`.
   - `it->second.first->Mult(E.Real(), D)` cited near `:261-262` → on-disk `:266`.
   - `:263` cited for `double dot = linalg::LocalDot(E.Real(), D)` → on-disk `:267`.
   - `:264-268` cited for the imaginary radicand `if (E.HasImag())` block → on-disk `HasImag` at `:269`; the `:264-268` range actually spans the null-return through the real `LocalDot`.

   The enclosing RANGE citations (`:255-275`, `:255-298`, `:277-297`) and the endpoint `return 0.5 * dot` (`:274` electric / `:296` magnetic) are CORRECT, so `--scan` passes and the claims are fully supported by the cited code — the code is present, a few lines below the pinpoint. Repair is mechanical: bump the affected sub-line pinpoints by the brace-boundary offset (`:262`/`:264`/`:266`/`:267`/`:269…`). The report self-corrected this exact drift family for `postoperator.cpp` (the +1 brace correction) but did not extend the check to the `domainpostoperator.cpp` body.

2. **No second issue of substance.** All other checks pass cleanly. The verb's warrant (DISTINCT-VERB-WARRANTED, two folded primitives, the `participation_ratio.md:188-191` "named not authored" disclaimer this verb realizes), the record-definition home, the variant-axis dispositions, the config-conditional `Σ pᵢ = 1`, the uniform-guard choice, the alpha-insertion wiring, and the fence parity are all verified correct against source and on-disk artifact state.

---

## Repair

### Fixes attempted

- **Finding**: Sub-line citation drift (+3–4 lines) in the `domainpostoperator.cpp` energy-form fine pinpoints (`citation-validity` warning). The enclosing RANGE citations (`:255-275`, `:255-298`, `:277-297`) and the `return 0.5 * dot` endpoints (`:274`/`:296`) are correct (so `--scan` passes 24/24); only the brace-boundary sub-anchors inside the body drift below the cited lines.
  - **Decision**: repaired.
  - **Action**: Bumped the affected sub-line pinpoints in the `new:book/src/L4/domain_energy_reduce.md` proposed-changes block (so the firm artifact lands with correct anchors), verified each against on-disk `reference/palace/palace/models/domainpostoperator.cpp`:
    - §Record definition (CYCLE.md line 298–299): `it->second.first` `:261-262`→`:262-266`; magnetic `it->second.second` `:283-284`→`:284-288`; null-operator-returns-0 `:261, :283`→`:262-264, :284-286`. (On-disk: electric `if (!it->second.first)` at `:262`, `return 0.0` at `:264`, `Mult` at `:266`; magnetic guard at `:284`, return at `:286`, `Mult` at `:288`.)
    - §Evidence "Domain-restricted energy form" bullet (CYCLE.md line 386–390): null-guard `:261-262`→`:262-264`; split out the `Mult(E.Real(), D)` `M_idx·field` apply to its own pinpoint `:266` (was conflated near `:261-262`); `LocalDot` `:263`→`:267`; imaginary radicand block `:264-268`→`:268-272` (on-disk `if (E.HasImag())` at `:269`, block body `:270-271`).
  - **Rationale for leaving the rest**: the enclosing ranges `:255-275`/`:255-298`/`:277-297`, the endpoints `:274`/`:296`, the Signature shape-contract range `:267-272` (real `LocalDot` at `:267` through imag block at `:272`), and the Algebraic-laws law-2 range `:262-274`/`:284-296` (full energy-form spans) all verify correct on-disk — left untouched. The `postoperator.cpp` `:1039`/`:1064` guard anchors were already self-corrected by the report (critic confirmed via `--anchor`) — left untouched.

### Unrepairable findings

None. The single warning was mechanical sub-line locator drift of the brace-boundary family — exactly the in-scope "citation line range off by a small offset" repair. All four affected pinpoints verified against on-disk source and bumped; the claims were always fully supported (the cited code exists a few lines below the pinpoint). The other 7 checks passed at critique.

## Suggested resolution

`ready`. Integrator note: the proposed-changes block authors `new:book/src/L4/domain_energy_reduce.md` plus three `edit:` blocks (`L4/index.md` dep-map alpha-insert before `dot`, `SUMMARY.md` alpha-insert, `L4/index.md` rough-in cohort tally 1→2). The Open-questions block CLOSEs `domain_energy_reduce-l4-verb-needs-authoring` and opens three NEW OQs (`domain_energy_reduce-promotion-double-gated`, `record-DomainOpMap-promote-watch`, `domain-field-energy-participation-guard-inconsistency` — the last a possible `problems/` drive-by, budget-permitting). All citation anchors now land on-disk.
