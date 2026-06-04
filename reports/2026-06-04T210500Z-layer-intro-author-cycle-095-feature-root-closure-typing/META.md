---
verifies: ../REPORT.md
critiqued_at: 2026-06-04T214500Z
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

# META: verification of "P1 feature-root closure typing — the non-cascade feature columns + the spine-ROOT" (cycle-095 D5)

## Critique

This report is a **feature-surface composition-root typing pass** (not a per-operator entry), so the adapted-checks-for-the-FEATURE-SURFACE-kind apply (rotation-quality / variant-axis-coverage no-op; cross-reference-integrity load-bearing). It is additionally a GRADED-STACK edge-typing pass, so the rank-invariant and reachability axes are checked alongside the 8.

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` over the report: 43 ok, 6 "failing". Inspected all 6 — they are book-internal location pointers of the form `<feature>.LN:line` (`energy-fields.L4:7`, `energy-fields.L1:7,43`, `lifecycle.L4:7`, `driven.L4:97`, `eigenmode.L4:40`) that the report uses to *name where a stale mention lives* (CYCLE.md:59-60, 781, 784). They are not Palace source-range claim citations; citecheck cannot resolve the `.L4`/`.L1` filename-suffix form, so these are tool-shape false negatives, not citation drift. Verified the load-bearing Palace `cites-evidence` ranges by `--anchor`: `drivensolver.cpp:77-229` (anchor `SweepUniform`, ok), `eigensolver.cpp:424-439` (ok), `postoperator.cpp:1246-1307` (anchor `MeasureSParameter`, ok), `main.cpp:276-278` (ok). The headline `L1/eigsolve` claim is confirmed on disk: `book/src/L1/eigsolve.md:165` §Status = `firm` (cycle-022 route-(b), promoted from `rough-in (test-coverage-bounded)`) — so the report's resolution of the planner's "verify at typing" OQ is correct, and the three eigsolve-chain rank "violations" are genuine stale-edge false positives. No `verified_against:` block in this report (n/a). All real citations are valid and in range.

**surface-or-evidence — pass (feature-surface adaptation).** Each typed column rests on its L0 driver/reduction source range(s) as `cites-evidence` `depends-on` edges + resolving constituent down-links — the adapted composition-root evidence shape. No new per-op algebraic claim is made (the report is explicit: "the chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters"). No record is newly named in a signature here (this is a frontmatter-typing + prose-re-anchor pass, not a signature-authoring pass), so the record-definition sub-check is n/a. The composition is supported: every claimed constituent exists (see cross-reference-integrity).

**rotation-quality — pass (not applicable to feature-surface kind).** A feature column recomposes already-firm vocabulary outward; it rotates nothing. No-op per the adapted checklist.

**variant-axis-coverage — pass (not applicable to feature-surface kind).** Variant axes live in the constituent ops, not the composition root. No-op per the adapted checklist.

**cross-reference-integrity — pass (load-bearing for this kind).** Verified all `depends-on` vocabulary-op targets resolve on disk (17 checked: `L4/fe_assemble`, `L4/assemble_frequency_operator`, `L4/frequency_sweep`, `L4/ksp_solve`, `L4/eigsolve`, `L4/fold_solve`, `L4/eigenfreq_qfactor_reduce`, `L4/sparameter_reduce`, `L4/domain_energy_reduce`, `L1/{fe_assemble,assemble_frequency_operator,ksp_solve,eigsolve,eigenvalue-untransform,participation_ratio,port_projection,matrix-weighted-norm}` — all OK). Verified all `reference:` sibling-column targets resolve (15 checked incl. `feature/sparameters.{L4,L1}`, `feature/eigenfrequency-qfactor.{L4,L1}`, `feature/eigenmode.{L4,L1}`, `feature/electrostatic.{L4,L1,L0}`, `feature/magnetostatic.{L4,L1}`, etc. — all OK). Maturity-overclaim sub-check: the report re-anchors several down-link cells / prose to `firm` for `electrostatic`/`magnetostatic`, which are still `status: seed` on disk *at the time of this critique* — BUT D4 (this same cycle, Wave 2) flips them seed→firm (confirmed in `reports/2026-06-04T205500Z-...-four-column-reeval/CYCLE.md` scope line 4 + body), and D5 explicitly flags the serial-ordering dependency (CYCLE.md:792: "If the integrator serializes D4 before D5, D4's electrostatic/magnetostatic firm flips are on disk when D5's reference edges + re-anchored cells apply"). Under the documented integrator serial-per-report ordering this resolves to firm; this is a flagged cross-report ordering precondition, not a D5 integrity defect. The 5 D4-handed stale-`(seed)` mention sites are all confirmed at exactly the cited lines (`energy-fields.L4:7`, `energy-fields.L1:7` and `:43`, `lifecycle.L4:7` and `:8`), each carrying the stale `seed` qualifier the report removes/re-anchors.

**edge-label-fidelity — pass.** The `composes:`→`edges:` migration follows scheme §4(c) exactly (verified `graded-stack-scheme.md:137-184`): vocabulary op → `depends-on`; sibling feature column → `reference` (OWN-COMPOSITION, scheme §3); `l0_ground_truth:`/L0 source → `depends-on kind: cites-evidence`; `lifts_to:`/level-sibling → `reference`; free-text maturity qualifiers dropped from edges. The `feature_root: seed` + `rank:` SPLIT matches scheme §3 (`seed` = permanent root marker, parallel axis; `rank:` = own composition-maturity). Each direction/edge-type assignment matches the prose discussion of that edge.

**plan-kind-consistency — pass.** Declared as a typing/edge-classification pass ("Typing ≠ promotion"); content matches — frontmatter `rank:`/`edges:` writes + stale-mention re-anchors, no `## Status`-word changes, no new operator authoring. The rank tokens are honest, derived from each file's OWN on-disk `## Status` (surveyed independently: 7 columns read `firm`, boundary-mode reads `seed`). The `boundary-mode → rank: rough-in` map is the one judgment call and it is defensible: boundary-mode's own stage-(3) readout reduces into an unhomed waveguide-mode product (confirmed in `boundary-mode.L4.md` §Status:77 own-readout gate) — solve corner firm, readout unhomed, so `rough-in` (NOT `firm`, NOT the non-rank `seed`). Rank-invariant holds: every `firm` column's `depends-on` deps are firm vocab ops (rank 3) + ground-truth `cites-evidence` ranges; boundary-mode's `rough-in`(2) ≤ its firm deps; `reference:` sibling edges constrain nothing. Reachability: every typed node carries `feature_root: seed` (root-set membership), so all are roots — trivially reachable.

**skill-uptake-survey — pass.** The report cites palace-codemap `read_range` + `citecheck --anchor` for on-disk anchor verification (CYCLE.md:427, 513, 543). The pass shape (composition-root typing under the graded-stack scheme) has no more-specific skill it omits; telemetry only, non-blocking.

### Issues found

No blocking issues. Two non-defect observations recorded for downstream awareness (neither is a finding against this report):

1. **Serial-ordering precondition (already flagged by the report, CYCLE.md:792).** D5's `firm` re-anchors of `electrostatic`/`magnetostatic` sibling cells presuppose D4's seed→firm flips have landed first. On disk at critique time those columns are still `status: seed`. This is correct under integrator serial-per-report ordering (D4 before D5) and the report acknowledges it explicitly; surfaced here only so the integrator confirms the ordering when staging. Not a citation/integrity defect in D5.

2. **`cites-evidence` linter-exemption convention (open question, raised identically by D4 and D5, CYCLE.md:788).** All `depends-on kind: cites-evidence` edges target `palace/...:lo-hi` ranges, not book slugs; the rank/reachability linters must special-case `cites-evidence` as slug-resolution/rank-check exempt. This is a shared cross-cycle convention question for the batch-30 meta-phase / D7 baseline, not a defect in this report.
