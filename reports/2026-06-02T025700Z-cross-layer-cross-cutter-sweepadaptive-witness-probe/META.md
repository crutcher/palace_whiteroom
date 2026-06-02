---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T03:40:00Z
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
repaired_at: 2026-06-02T04:05:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of cross-layer probe — SweepAdaptive is a ROM-FOLD, not a 2nd map_solve witness

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` returned 10 ok / 0 failing (bounds + path hygiene clean). I then re-read the load-bearing pinpoints against Palace source via codemap and every one confirmed: (a) `drivensolver.cpp:389` `double omega_star = prom_op.FindMaxError(excitation_idx)[0]` lands exactly at line 389 inside the greedy loop, with the "(bounded by the previous samples)" comment directly above it — the sample-LOCATION state-thread; (b) `romoperator.cpp:236-244` `MinimalRationalInterpolation::FindMaxError` is documented as `argmax_z ||u(z) - V y(z)||` = `argmin_z |Q(z)|` over the barycentric interpolant of existing samples, with `MFEM_VERIFY(S >= 2, ...)` at :243-244 — confirms the ≥2-prior-sample precondition; (c) `romoperator.cpp:596-640` `UpdatePROM` does `V.emplace_back(vector)` + `OrthogonalizeColumn(orthog_type, ..., V, v, ..., dim_V, ...)` — Gram-Schmidt append into the growing basis, the sample-RESULT state-thread; (d) loop bound `it < max_size_per_excitation && memory < convergence_memory` (:385) with `memory` running — confirms the state-derived termination; (e) online loop `:432-475` does per-frequency `SolvePROM(excitation_idx, omega, E)` at :451 with NO `SetOperators`; (f) test citations `test-romoperator.cpp:95` (`CHECK_THROWS(mri_1.FindMaxError(1))`) and `:121` (`mri_1.FindMaxError(5)`) match exactly and corroborate the accumulated-state precondition; (g) comparison witness `Sweep`'s `ksp.SetOperators(*A, *P)` confirmed at `drivensolver.cpp:180` (the operator-varying shape). One trivial wording note (below), not a citation defect.

**surface-or-evidence — pass.** Not a refinement-shaped proposal. This is an observation-only probe (a coverage-gap / family-classification finding) with no surface mutation and no proposed-changes block — the report explicitly states "No `book/` edit is implied" (CYCLE.md:58). Pure observation is allowed; nothing to gate here.

**rotation-quality — pass (not applicable as a rotation assertion).** The report asserts no algebraic/structural L_{n+1}→L_n rotation; it makes a fold-vs-map family-membership judgment. The judgment itself is sound: it correctly declines to assert a (false) concatenation-homomorphism/independence law for SweepAdaptive's offline phase, which is the right call given the double state-thread. No compaction claim to grade.

**variant-axis-coverage — pass.** The relevant axis is the fold-vs-map disjunction over the SweepAdaptive structure's loops; the report enumerates all three loops (seed-sample :366-376, greedy adaptive :383-410, online fast-sweep :432-475) and adjudicates each — the two offline loops are state-threaded folds, the online loop is a map but over a frozen operator (scope-excluded with rationale). No hidden branch: the report explicitly addresses the seed loop, which a thinner analysis might have skipped. The per-excitation outer loop is correctly treated as an independent partition over excitations (MAP), not load-bearing to the verdict.

**cross-reference-integrity — pass.** No `[link]` references and no new slugs are introduced (observation-only, no book mutation). The references to prior work (`Sweep` / cycle-056 D1 as the sole `map_solve` witness; transient as the existing FOLD-family member) are textual cross-cycle pointers, not artifact links requiring resolution. Build-readiness fence guard is no-op: there is no proposed-changes block. Nothing to resolve.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried; the report's framing ("L_n↔L_{n+1} cross-cut") is a probe scope, not an edge claim, and the prose stays on the fold/map family question throughout. Not applicable.

**plan-kind-consistency — pass.** Declared as a cross-layer-cross-cutter observation (coverage-gap, resolved-negative). The content shape matches exactly: a single negative finding (candidate does not close the probed gap) plus a family-classification consequence, no authoring, no proposed-changes. This is the canonical observation kind for the role.

**skill-uptake-survey — pass.** The report invokes the `disciplined-cross-pipeline-combinator-mining-gate` step-3 fold-vs-map check by name (CYCLE.md:48) and applies it as the adjudication procedure, and references the step-2 scope-boundary check (CYCLE.md:76). The relevant skill for a fold-vs-map combinator-mining decision is referenced. Surfaced telemetry only.

### Issues found

All eight checks pass; the FOLD classification is sound on source and the scope-boundary distinction (map over a frozen ROM ≠ operator-varying map over the full operator) is correct. Three minor (non-blocking) observations for the repairer's awareness:

1. **(trivial — wording) `UpdatePROM` signature paraphrase.** CYCLE.md:64 and :42 gloss the basis-append as `prom_op.UpdatePROM(E, ...)`. The actual `RomOperator::UpdatePROM` signature is `UpdatePROM(const ComplexVector &u, std::string_view node_label)` (`romoperator.cpp:596`); the `drivensolver.cpp` lambda at :317-340 is what wraps it with `(excitation_idx, omega_star, counter_rom_sample)`. The substance the report relies on (the call appends the solution into the growing basis V) is correct and confirmed; only the argument-list paraphrase conflates the lambda's args with the underlying method's. Severity: cosmetic. Location: CYCLE.md:42, :64.

2. **(trivial — pinpoint precision) `OrthogonalizeColumn` line.** CYCLE.md:42,:69 cite `romoperator.cpp:634+` for the Gram-Schmidt `OrthogonalizeColumn(... V, v, ... dim_V ...)` call. The actual call sits at ~:635 inside the `add_real_vector_to_basis` lambda (the `:596-693` enclosing range is correct and in-bounds). The `+` suffix makes this an open-ended pointer rather than an exact line; harmless given the range citation, noted only for precision. Severity: cosmetic. Location: CYCLE.md:42, :69.

3. **(informational — not a defect) the OQ is legitimately open, not a strandable loose end.** The OQ (CYCLE.md:75) that no remaining driven candidate is an operator-varying map, so a genuine 2nd `map_solve` witness must come from another pipeline (or the superset is a permanent single-witness finding), is a correctly-scoped negative result with a concrete batch-18-planner hand-off. It is not an issue to repair; flagged here only to record that the critic confirmed it as a real, bounded open question rather than an unfinished claim. No action.

## Repair

### Fixes attempted

All eight critic checks returned `pass`. No warning/fail finding exists; the three observations the critic recorded are explicitly cosmetic/informational and non-blocking. Per-finding:

- **Finding**: `UpdatePROM` signature paraphrase (CYCLE.md:42, :64) glosses the lambda's args `(excitation_idx, omega_star, counter_rom_sample)` onto the underlying `RomOperator::UpdatePROM(const ComplexVector &u, std::string_view node_label)` method.
  - **Decision**: not-needed.
  - **Rationale**: The critic confirmed the substance the report relies on (the call appends the solution into the growing basis V) is correct and source-confirmed. The paraphrase is a cosmetic conflation of the wrapping lambda's args with the underlying method's; the critic graded it cosmetic (severity: cosmetic) and the check passed. No claim is wrong, so there is no mechanical citation/dep-map fix to apply — editing the prose paraphrase would be authoring, not surgical repair. Report is observation-only and pre-integration; left as-is.

- **Finding**: `OrthogonalizeColumn` open-ended pinpoint `romoperator.cpp:634+` (CYCLE.md:42, :69); actual call sits at ~:635 inside the `:596-693` range, which is cited and in-bounds.
  - **Decision**: not-needed.
  - **Rationale**: The critic confirmed the enclosing range citation (`:596-693`) is correct and in-bounds and that the `:634+` open-ended pointer is harmless given the range. citecheck returned 10 ok / 0 failing — no bound or path defect. This is not the "citation line range off by a small offset" repair case (the enclosing range is exact); the `+` suffix is a cosmetic pinpoint-precision note, not a citation defect. No edit warranted.

- **Finding**: the OQ (CYCLE.md:75) — no remaining driven candidate is an operator-varying map; a genuine 2nd `map_solve` witness must come from another pipeline or the superset is a permanent single-witness finding.
  - **Decision**: not-needed.
  - **Rationale**: The critic explicitly recorded this as a correctly-scoped, bounded negative result with a concrete batch-18-planner hand-off — informational, not a defect. Nothing to repair.

### Unrepairable findings

None. No finding exceeds repair authority; all three observations are non-blocking and require no edit.

## Suggested resolution

`overall_status: ready` — sound FOLD classification, all eight checks pass, no book mutation.

Notes for the integrator:

- **D3 has NO book mutation** (observation-only probe; CYCLE.md:58 "No `book/` edit is implied"). No proposed-changes block to apply.
- **Promote D3's OQ.** The family-classification finding: `map_solve` stays **DEFERRED at 1 witness** (standard `Sweep`, cycle-056 D1). **SweepAdaptive + transient both join the FOLD family**, confirming the two-combinator factoring (independent-MAP `solve_family` vs sequential-FOLD). A genuine 2nd map witness must come from another pipeline, or `map_solve` is a **permanent single-witness spine-coverage finding** (batch-18 planner decision).
- The three cosmetic/informational observations carry forward as awareness only; none gate integration.
