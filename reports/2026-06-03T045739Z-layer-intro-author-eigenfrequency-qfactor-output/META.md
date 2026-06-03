---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T052450Z
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

# META: verification of "eigenfrequency-qfactor output-product feature column (L4+L1+L0)"

## Critique

This report is a **feature-surface composition-root** of the output-product leaf-column
sub-kind (FEATURE-SURFACE SPINE, batch-22 codification). The 8 checks are run with the
feature-surface adaptations from my role-spec: rotation-quality and variant-axis-coverage
are formal no-ops for this kind; surface-or-evidence is adapted to the driver-range +
down-link form; cross-reference-integrity is load-bearing.

### Checks run

**citation-validity — pass.** All L0 anchors were spot-checked on-disk via palace-codemap
`read_range`. `palace/drivers/eigensolver.cpp:424-475` verifies exactly: the readout loop
`for (int i = 0; i < num_conv; i++)` at `:424`, `GetEigenvalue(i)` at `:427`, the linear-EVP
`if (!C && !has_A2)` / `omega = std::sqrt(omega)` branch at `:430-434`, the quadratic-EVP
`omega /= 1i` branch at `:435-439`, `GetEigenvector(i, E)` at `:443`, the `B = -1/(iω)∇×E`
field readout + Floquet correction at `:445-455`, `MeasureAndPrintAll(...)` at `:457-458`,
loop close `:471`, `MFEM_VERIFY(num_conv >= ...n)` at `:472-475`. `postoperator.cpp:1171-1217`
verifies exactly: template `:1171` / def `:1172`, the `if constexpr (... == EIGENMODE)` guard
`:1175`, `freq_re = measurement_cache.freq.real()` `:1177`, the `if (std::abs(data.R) > 0.0)`
resistive test `:1192`, `resistor_power` `:1196-1198`, `mode_port_kappa` copysign `:1199-1200`,
`quality_factor` `:1201-1203`, and the inductive-port EPR sibling `if (std::abs(data.L) > 0.0)`
arm beginning `:1213` (D4's self-correction to `:1204-1217` for the EPR sibling is correct —
that arm IS distinct from the Q-factor and is correctly framed as "NOT a Q"). This is a
feature-surface chapter (compositional claim only; no new per-op algebraic claim), so the
citation bar is the site-map-resolves bar, which is met. No `verified_against:` YAML block is
present, so that sub-check does not apply. (One sub-range imprecision noted under Issues; it
is in-range, not drift.)

**surface-or-evidence — pass (feature-surface adaptation).** Per the adapted rule, a
composition-root's evidence is the L0 driver-source range + the constituent down-links, NOT a
single decomposed-op source site. Both are present and resolve: the L0 driver range
`eigensolver.cpp:424-439` (+ the `postoperator.cpp:1171-1203` Q-factor range) is cited and
backs the feature, and the down-links resolve to real constituent chapters (eigenmode column
on disk; `eigenfreq_qfactor_reduce` lands same-cycle via D3). The chapter makes no new per-op
algebraic claim of its own — it explicitly defers per-op claims to the linked
`eigenfreq_qfactor_reduce` + `eigenmode` chapters (stated in all three §Status blocks and the
L0 closing line). The composition is supported, so this passes.

**rotation-quality — pass (not applicable to feature-surface kind).** A feature chapter
rotates nothing — it recomposes already-firm vocabulary outward (analogous to the `stub`
no-op). Formal pass. (The report correctly avoids asserting a rotation; it frames the L1-vs-L4
difference as a vocabulary difference of the *same* product, not a rotation between layers.)

**variant-axis-coverage — pass (not applicable to feature-surface kind).** A feature chapter
has no variant axes of its own; the axes live in the composed constituent ops. Formal pass.
Note for completeness: the report DOES surface the load-bearing problem-type un-transform axis
(linear-EVP `√μ` vs quadratic-EVP `λ/i`) and correctly attributes it to the
`eigenfreq_qfactor_reduce` constituent's `untransform` dispatch rather than claiming to cover
it here — exactly the right disposition for the composition-root kind.

**cross-reference-integrity — pass (load-bearing for this kind).** Every constituent down-link
was checked on-disk. Resolves: `./eigenmode.L4.md` / `.L1` / `.L0`, `./capacitance.L4.md` /
`.L0`, `./inductance.L4.md`, `../L4/gram_reduce.md`, `../L4/eigsolve.md`, `../L1/eigsolve.md`,
`../L4/fe_assemble.md`, `../L1/fe_assemble.md`, `../L4/solve_family.md`. The one not-yet-on-disk
target is `../L4/eigenfreq_qfactor_reduce.md` (the load-bearing LIVE link): it is D3's
same-cycle `create`, and the report explicitly documents the ordering dependency + a plain-text
fallback in §Open-questions. This is the coupled-same-cycle case the dispatch scope describes
(integrator applies D3 before D4, or both before the finalize build) — the link is valid GIVEN
D3 lands, and the report's contingency (demote to plain-text if D3 does not land) is correctly
specified. Maturity-claim check: the chapters claim `eigenfreq_qfactor_reduce` is `rough-in`
and `eigenmode` is `seed`; eigenmode's on-disk `## Status` is `seed` (confirmed), and a `seed`
column composing a `rough-in` constituent is the correct/expected output-product state (the
column stays `seed` until all constituents firm) — no maturity overclaim. **Canonical-slug
check:** the slug `eigenfrequency-qfactor` matches exactly what `feature/eigenmode.{L4,L1,L0}.md`
forward-reference (confirmed on-disk: `eigenmode.L4.md:40,45,55,70`,
`eigenmode.L1.md:36,41,57,61`, `eigenmode.L0.md:29,36`) — so D2's consolidated index/SUMMARY
rows and the eigenmode forward-refs will resolve to this column. The `solve_family.md:146`
non-membership anchor cited in the L4/L1 chapters resolves (file is 170 lines; `:146` is inside
the §Status block discussing the eigenmode non-membership). Pass.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (this is a feature column,
not a lowering theme). The within-column `L0 → L1 / L4` "lifts to" prose in the L0 chapter
discusses exactly the L1 and L4 chapters it names. No mismatch.

**plan-kind-consistency — pass.** Declared kind = feature-surface, `status: seed`, content
shape = composition-root (inputs=config, output=(f,Q) table, body=compose-DOWN, links DOWN to
constituents). The status token is the uniform `seed` with no `(exemplar)`/`(composition-root)`
qualifier — correct per the batch-22 codification (the leaf-column sub-kind is named in prose,
not the token). All three frontmatters carry `kind: feature-surface`. Content matches the
declared kind.

**skill-uptake-survey — pass (telemetry only).** The report's shape (large citation-dense
bodies staged as sibling files to avoid the nested-`text`-fence truncation defect) explicitly
invokes the rationale behind `proposed-changes-fence-encloses-full-body-guard` /
`convert-nested-fences-to-indented-code-in-proposed-changes-block` — and the chosen mitigation
(verbatim sibling-file copy rather than inline-fenced `create` bodies) is the cleaner
side-stepping of that defect. The on-disk L0-citation self-verification is the
`verify-citation-range` mechanical realization. Adequate skill awareness surfaced; non-blocking.

### Issues found

1. **(minor, in-range — NOT drift) κ/Q-formula comment sub-range slightly under-shoots.**
   The L4 down-link table (`eigenfrequency-qfactor.L4.md:64`) cites the folded κ-participation
   comment as `postoperator.cpp:1188-1203`, the L4 §composition (`:38`) cites it as
   `:1185-1191`, while the L0 chapter (`:27`) and L1 chapter (`:60`) cite `:1186-1191`. On-disk
   the formula comment block (`κ_mj = 1/2 R_j I_mj² / E_m` … `Q_mj = ω_m / κ_mj`) sits at
   `:1184-1190`, inside the `MeasureLumpedPortsEig` body. Every cited range ENCLOSES the formula
   lines (`:1188` and `:1190` are both inside all the cited spans), so this is an in-range
   imprecision, not a `[DRIFT ±N]`. The minor inconsistency is that the same comment is cited
   with three slightly different bracketings across the three chapters (`:1185-1191` /
   `:1186-1191` / `:1188-1203`); harmonizing them to the actual `:1184-1190` block would be
   tidier but is not required for citation-validity to pass. Location: `L4.md:38,64`, `L1.md:60`,
   `L0.md:27`. Severity: cosmetic.

2. **(informational — not a defect; build-reachability flag for finalize) the three new
   chapters are NOT yet SUMMARY-reachable.** The report correctly DEFERS all `feature/index.md`
   + `# Feature surfaces` SUMMARY.md rows to D2 (confirmed: the report emits zero index/SUMMARY
   edits, and `feature/index.md` on-disk carries no `eigenfrequency-qfactor` row — the deferral
   is honored, not silently emitted). This is the correct parallel-blind-shared-index guard.
   However, until D2's consolidated SUMMARY block enumerates the three
   `eigenfrequency-qfactor.{L4,L1,L0}` rows, these three files are orphaned (not in SUMMARY.md →
   not built by mdBook). The report itself raises this as the "SUMMARY.md orphan-row guard"
   (§Ownership partition + §Open-questions) and flags it for integrator-finalize to verify the
   three rows are present (high→low L4→L1→L0 order) after D2 applies, adding them at build-repair
   if D2's scope omitted them. This is a correct, well-scoped hand-off, not a defect in THIS
   report — surfaced here so the integrator does not miss it. Location: `CYCLE.md:70-92,157-161`.
   Severity: informational (cross-dispatch coordination, resolved at finalize).

3. **(informational — coupled-dependency on D3) the load-bearing LIVE link
   `../L4/eigenfreq_qfactor_reduce.md` is not yet on disk.** Verified: the target does not exist
   in `book/src/L4/` at critique time (D3 authors it this cycle). The report documents the
   ordering dependency and the plain-text-demote fallback explicitly (§Open-questions, CYCLE.md
   :140-149). This is the intended coupled-same-cycle arrangement; flagged only so the integrator
   confirms D3's `create` is applied before (or in the same finalize build as) this column —
   otherwise it is a `linkcheck2` hard error. Not a defect in this report. Location:
   `L4.md:16,18,24,32,...`, `L1.md:50,59,60`, `L0.md:27,40`; `CYCLE.md:140-149`. Severity:
   informational.

### Summary

No `warning`/`fail` on any of the 8 checks. The report is a clean feature-surface
composition-root: the composition is sound and rank-correctly framed (rank-1 per-mode
scalar-ratio table, explicitly NOT a `gram_reduce` family-PAIR grid per c074 D6), the L0
site-map citations verify on-disk, the canonical slug matches the eigenmode forward-references,
within-column ordering is high→low (L4→L1→L0), the index/SUMMARY deferral to D2 is honored
(zero index/SUMMARY edits emitted), and the two cross-dispatch couplings (D3's same-cycle verb
file; D2's SUMMARY rows) are correctly documented with fallbacks. The three issues are one
cosmetic citation-bracketing inconsistency and two informational cross-dispatch coordination
flags that the report itself already raised for the integrator.
