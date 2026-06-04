---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T010500Z
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

# META: verification of "Re-anchor solve_family stale `rough-in (test-coverage-bounded)` references → `firm`"

## Critique

### Checks run

**citation-validity — pass.** The report's single load-bearing L0 citation `reference/palace/palace/linalg/ksp.cpp:297-310` was verified two ways: `citecheck --anchor 'Mult'` returns `[ok]` (anchor at lines 297/300 within range), and a direct read confirms 297-310 is exactly the const `BaseKspSolver<OperType>::Mult` body whose only cross-call mutable state is `ksp_mult++` (line 308) and `ksp_mult_it += ksp->GetNumIterations()` (line 309) — two monotone telemetry counters, precisely as the re-anchor prose asserts. This is **carry-forward context** (the c086 firm-promotion justification), not a NEW positive claim this report originates: solve_family was already firmed at c086 against this evidence; the report only re-narrates the existing firmness. The `citecheck --scan` flagged 3 `[AMBIG]` results on bare `index.md:47/:57/:122` — these are the report's own internal line-number references to its subject file (frontmatter `inputs:` + §1 header + §Discipline notes establish them as `book/src/L4/index.md`); the AMBIG is the basename path-hygiene lint firing on an unqualified `index.md`, not a bounds/anchor defect, and the file is unambiguous in context. No `verified_against:` YAML block is present in this report (it is a lifter re-anchor, not a lowering-verifier audit), so that sub-check is not applicable. The `cycle-record.jsonl` cycle-086 `counts_after` (`L4_firm:17`, `L4_rough_in:1`, `L4_rough_in_test_coverage_bounded:0`) was confirmed and backs the §1a count-header reconciliation.

**surface-or-evidence — pass.** This is a pure maturity re-anchor (a retroactive-evidence/stale-correction pass), not a refinement that modifies operator/theme decomposition. Every site is a status-prose correction supported by the on-disk `solve_family.md:4 firmness: firm` (read this dispatch) + the c086 finalize counts. No record/struct is newly named in any touched signature (the `solve_family :: OpParams -> [Inputs] -> [SimState]` dep-map signature at index.md:122 is unchanged and its records — OpParams/Inputs/SimState — are pre-defined in the firm vocabulary), so the record-definition sub-check no-ops. The surface text changed is exactly the maturity-claim prose, which is the legitimate deliverable of a re-anchor.

**rotation-quality — pass.** No new algebraic/structural rotation is asserted. The one rotation-bearing theme touched (`solve-family-map-dissolution.md`, L4>L3) STAYS firm; only its LHS-maturity narration is updated, and the report explicitly preserves the firm-on-structure reasoning (the §3c re-narration keeps "the rotation shape does not depend on the independence law" intact, updating only the now-discharged LHS-maturity premise). No 1:1 rename is introduced.

**variant-axis-coverage — pass.** No variant axes are introduced or rescoped. The fixed-operator-vs-per-element scope boundary (solve_family vs frequency_sweep) is preserved verbatim across §2a/§2b/§5; the §2b re-narration in particular explicitly PRESERVES the operator-capture axis (fixed-shared-capture vs fresh-per-member-rebuild) while dropping only the now-false maturity contrast. The 2-of-5-pipelines scope of solve_family is carried through every edit unchanged.

**cross-reference-integrity — pass (load-bearing, scrutinized).** All 12 `[old]` anchors were verified `grep -c == 1` (exact-match unique) on disk across the 5 files: index.md (:57 header, :47 status clause, :122 cell tail, :59 bullet implicit in the :57 block), frequency_sweep.md (:69, :506-block), solve-family-map-dissolution.md (:134, :140, :187), feature/index.md (:68), fe_assemble.md (:171). The index.md internal-consistency fix was checked end-to-end: after §1a+§1b, solve_family appears in the firm cohort ONLY (the :47 firm-cohort body re-anchored to `firm`, the :59 rough-in bullet dropped, the :57 header recounted `(1 + 1 test-coverage-bounded)` → `(1)` with only `domain_energy_reduce` remaining) — reconciling to the on-disk `L4_rough_in:1`, `L4_rough_in_test_coverage_bounded:0`. No `[link]` is broken (all targets — solve_family.md, ksp_solve.md, iterate-while.md, chebyshev.md, gram_reduce.md, etc. — exist on disk). No other operator's maturity is altered: domain_energy_reduce stays `rough-in` (preserved verbatim at the new :36 bullet), eigenfreq_qfactor_reduce/sparameter_reduce/fold_solve/frequency_sweep narrations untouched. No feature-column status token flips: feature/index.md:68 re-narrates the *narrowed gate* (gram_reduce alone) but electrostatic/magnetostatic stay `seed`, and the re-narration matches the already-correct canonical sibling `electrostatic.L4.md:56` ("solve_family per-terminal map is now firm (c086) ... gate has narrowed ... to ONE: firming gram_reduce"). This report is not a feature-surface composition-root kind, so the adapted feature-surface checklist does not apply.

**edge-label-fidelity — pass (load-bearing for the maturity-label re-anchors).** Each re-anchored maturity label was verified genuinely stale on-disk and the re-anchor matches the now-firm state. index.md:47 body read on disk: "Status `rough-in (test-coverage-bounded)` (structure firm; laws stated against strawman §3.7 but test-unconfirmed)" — STALE, sitting INSIDE the firm cohort two lines below the :32 header that narrates "cycle-086 promoted ... solve_family ... → firm" — a genuine internal contradiction, exactly as the report describes. index.md:57 header "Rough-in at L4 (1 + 1 test-coverage-bounded)" + the :59 solve_family rough-in bullet — both STALE (duplicate-listing). index.md:122 dep-map status cell reads `rough-in (test-coverage-bounded)` — STALE. The L4>L3 theme direction in solve-family-map-dissolution.md is preserved (LHS=L4, RHS=L3, narrated forward); the prose discusses exactly the solve_family LHS-maturity edge, not a mislabeled one.

**plan-kind-consistency — pass.** Declared as a lifter land-clean maturity re-anchor; content shape matches — small, surgical, prose-only maturity corrections with structure/signature/rotation untouched, ZERO new files, ZERO SUMMARY change. Appropriately scoped for the LAND-CLEAN cycle's single dispatch.

**skill-uptake-survey — pass (telemetry).** The report's shape (exact-match anchor verification + on-disk staleness confirmation) maps to `verify-citation-range` / the `tools/citecheck/` `--anchor`/`--scan` realization; the report's §Supporting evidence does reference the verification it performed (grep -c uniqueness, --anchor/read_range-equivalent on ksp.cpp). The `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill is not relevant (no plain-text-ref upgrades here). No blocking gap.

### Issues found

None. All 8 checks pass.

The one item flagged for critic attention — the **index.md:47 divergence from the plan's DO-NOT-TOUCH list** — is a **legitimate stale-correction, not an out-of-scope leak**, and is correctly disclosed by the report (§1b + §Discipline notes + §Open-questions). Verification: index.md:47's firm-cohort entry BODY was read on disk and genuinely asserted `rough-in (test-coverage-bounded)`, while the :32 cohort header two lines above narrates the c086 firm promotion — a real internal contradiction in the same maturity-drift class as the 5 plan-named sites. The plan's "correctly-firm → KEEP" rationale rested on the (on-disk-false) assumption that the :47 body "already says `*(firm; cycle-086 D1)*`"; the c086 grep-sweep corrected the :32 header but missed the :47 body in the very same file. The re-anchor is (i) L0-evidenced by `solve_family.md:4 firmness: firm` + the c086 cycle-record counts, (ii) bounded (a status-clause re-anchor, no decomposition/signature/rotation change), and (iii) recorded. Applying it is the correct disposition for a land-clean / self-consistent cycle; declining it would leave a surviving firm-cohort entry asserting `rough-in`. The divergence is justified and within the re-anchor pass's intent.

(Non-blocking, FYI only — not a finding: the report's §Open-questions surfaces a `floor-landing-implies-same-cycle-adjacent-entry-reanchor` drift-pattern signal for the batch-27 meta-phase, namely that the c086 firm-promotion sweep missed sites in the very file it partially edited. This is appropriately routed as an intake signal, not actioned this cycle, and is consistent with the no-shared-context critic surfacing the same observation independently.)
