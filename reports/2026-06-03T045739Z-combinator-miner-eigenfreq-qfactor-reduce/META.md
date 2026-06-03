---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T05:10:00Z
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
repaired_at: 2026-06-03T05:30:00Z
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

# META: verification of "Combinator candidate — eigenfreq_qfactor_reduce"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` (29 ok / 0 failing on bounds + path-hygiene) and `--anchor` on every load-bearing pinpoint. The eigensolver un-transform anchors all clear cleanly: `eigensolver.cpp:424-439` (`GetEigenvalue` @427), `:430-434` (`sqrt` @433, brace-bounded linear-EVP `if` arm), `:435-439` (`1i` @438, the `else` quadratic arm), `:458` (`MeasureAndPrintAll`), `:471-475` (loop close + `MFEM_VERIFY`) — all confirmed in-range by hand-Read with correct brace boundaries. On the postoperator side: `:1171-1172` (`MeasureLumpedPortsEig` def), `:1177` (`freq_re`), `:1188-1191` (`Q_mj` formula comment), `:1196-1198` (`resistor_power`), `:1215-1219` (`inductive_energy_participation`) all clear. **One DRIFT and one borderline citation found** (see Issues) — both on the `quality_factor` assignment statement, which the on-disk source spans lines **1200-1202** (a multi-line ternary `vi.quality_factor = (cond) ? mfem::infinity() : freq_re/...`), not the `:1201-1203` the report cites in two places. The `:1201-1203` range captures `mfem::infinity()` (1201) and the `freq_re/std::abs` arm (1202) and the closing brace (1203) but **misses the `vi.quality_factor =` LHS token at line 1200** and includes an off-target brace line. This is a real ±1 drift (`--anchor 'quality_factor'` ⇒ DRIFT, suggested `1200-1202`), not a hand-asserted off-by-one. The meaning is unaffected (the ternary IS the quality-factor computation and the guard IS at 1201), so the load is light — but the line-map is off and the integrator should land the corrected range.

**surface-or-evidence — pass.** This is a NEW combinator entry (combinator-as-entry per the VOCABULARY-SHIFT redirect), not a refinement of an existing operator/theme, so the refinement-surface gate is the new-vocabulary warrant rather than rotation_claim-on-existing-surface. The warrant is grounded: two positive readout sites (eigenvalue→ω un-transform + Q-factor body) are cited and verified on-disk, and the over-unification guard (NOT a `gram_reduce` rank-2 specialization) is backed by the c074-discharged OQ (`scaffolding/open-questions.md:943`, DISCHARGED NEGATIVE — neither candidate is a symmetric-Gram witness). The `rough-in` status is correctly warranted by the two stated gates (folded κ-participation + un-transform primitives are not yet firm L1; no dedicated eigenmode-postprocess unit test), both independently confirmed (no `L1/eigenfreq_qfactor_reduce` or κ-participation primitive on disk; the body is integration-level only).

**rotation-quality — pass.** The proposal asserts no NEW cross-layer rotation theme — it explicitly takes the in-line-marker route (identity-in-form on the body, no dedicated L4>L3 theme, §"Lowers to"), the same disposition `inner_product`/`gram_reduce` use. The L4 entry IS a genuine abstraction lift: the eigenmode driver's per-mode readout, scattered across the `eigensolver.cpp` readout loop (un-transform) and the `postoperator.cpp` `MeasureLumpedPortsEig` body (Q-factor), is recompressed into ONE reduction over the eigenpair family. This is state-hiding / scatter-compression, not a 1:1 rename — pass.

**variant-axis-coverage — pass.** Three axes are named and each is dispositioned: **problem-type** (linear/quadratic/nonlinear-EVP — the load-bearing un-transform axis, absorbed into the `untransform` dispatch, witnessed at `:430-439` for the first two; nonlinear-EVP is named but the un-transform branch for it is not source-witnessed, which is honest and consistent with `rough-in`); **loss-source** (resistive-lumped-port witnessed `:1188-1203`, inductive-EPR the participation sibling `:1215-1219` explicitly scoped as NOT-a-Q, absorbed into the κ closure); **element-type** (complex, pinned). No hidden branches — the inductive-port and surface-dielectric participation paths are explicitly carved out as future κ-primitive material, not silently folded in.

**cross-reference-integrity — pass.** All sibling links resolve on disk: `gram_reduce.md`, `inner_product.md`, `eigsolve.md`, `solve_family.md`, `frequency_sweep.md`, `dot.md`, `fe_assemble.md`, `index.md`, the `black-box-vs-accelerated-kernels` concept, and all six `feature/{eigenmode,lifecycle}.{L4,L1,L0}.md` files. The target chapter `L4/eigenfreq_qfactor_reduce.md` is correctly absent (it is a `create:`, not an `edit:`). Maturity claims verify: `eigsolve` is `firmness: firm` (the consume claim is accurate); `gram_reduce` is `rough-in (test-coverage-bounded)` (the report's contrast comparison is accurate). The `gram_reduce.md:178-189` non-subsume anchor resolves with "eigenmode" present. The house style parallels the reduce-family (`gram_reduce`/`inner_product`).

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is asserted (the entry routes its downward content in-line rather than via a theme). The over-unification distinction the report leans on — rank-1 per-mode scalar-ratio table vs `gram_reduce`'s rank-2 family-PAIR Gram grid — is consistently stated throughout (§Pattern-instances, §Algebraic-laws law 3, §Status, §Evidence) and matches the c074 D6 closed-negative discharge. No edge mis-labeling.

**plan-kind-consistency — pass.** Declared `rough-in`, and the content shape matches: structure read off positive sites, laws stated as syntactic identities on the per-mode map, but two explicit promotion gates (un-firm folded primitives + no test) hold it back from firm. The report correctly does NOT claim the firm-on-positive-structure escape (it explains why the escape is approached but blocked by primitive-maturity). The dep-map row, SUMMARY entry, and chapter body all carry the same `rough-in` token — no mis-classification.

**skill-uptake-survey — pass.** The report states all L0 citations were self-verified via the codemap (`mcp__palace-codemap__read_range` + `search_text`), consistent with MCP-first localization. No skill invocation was strictly implied beyond that; the combinator-mining disciplined-cross-pipeline-gate is referenced and correctly scoped-out (single-pipeline output-product verb). Telemetry only — no blocking.

### Issues found

1. **[citation drift — `quality_factor` range, ±1] `book/src/L4/eigenfreq_qfactor_reduce.md` create-block §Evidence (CYCLE.md:398) and §Pattern-instances (CYCLE.md:48).** Both cite `postoperator.cpp:1201-1203` for the `quality_factor = (κ==0) ? mfem::infinity() : freq_re/|κ|` assignment. On-disk the assignment statement spans **1200-1202** — the `vi.quality_factor =` LHS is at line **1200**, the `? mfem::infinity()` at 1201, the `: freq_re / std::abs(...)` at 1202; line 1203 is the closing `}` of the `if (std::abs(data.R) > 0.0)` block. `citecheck --anchor 'quality_factor'` reports DRIFT (anchor at 1200, outside 1201-1203; suggested `1200-1202`). Severity: low (the cited range still overlaps the computation and the `mfem::infinity()` guard genuinely sits at 1201, so the claim is supported in meaning) — but the line-map is off by one at the start and the corrected range is `1200-1202`.

2. **[borderline citation — `mode_port_kappa` range] §Pattern-instances (CYCLE.md:47-48) / §Evidence (CYCLE.md:397) cite `postoperator.cpp:1199-1200` for `mode_port_kappa = copysign(resistor_power/energy_electric_all, …)`.** The `vi.mode_port_kappa =` ASSIGNMENT actually spans **1198-1199** (`vi.mode_port_kappa =` at 1198, the `std::copysign(...)` continuation at 1199). Line **1200** is `vi.quality_factor = (vi.mode_port_kappa == 0.0)` — `mode_port_kappa` appears there only as the ternary *condition*, not as the assignment target. `--anchor 'mode_port_kappa'` passes on `:1199-1200` (the token is present at 1200), so this is not a hard DRIFT, but the range under-shoots the assignment start (1198) and over-reaches into the quality_factor line. Severity: low. Suggested precise range for the kappa assignment: `1198-1199`. (Co-located with issue 1; a repairer correcting both will land `1198-1202` cleanly covering both statements.)

3. **[no-issue confirmations — recorded for the repairer/integrator, not defects]**
   - **D1 collision check CLEARS.** D3 anchors both its index.md dep-map row and its SUMMARY bullet TIGHTLY on the `fe_assemble` alpha-neighbor. D1 (`sparameter_reduce`) anchors on `nrm2`. `eigenfreq_qfactor_reduce` sorts between `dot`(95) and `fe_assemble`(96) in the dep-map and between `dot`(SUMMARY 42) and `fe_assemble`(43); `sparameter_reduce` sorts after `nrm2` — a DIFFERENT alpha position / different anchor line. No anchor collision; the two surgical Edits are independent. The coordination note (CYCLE.md:422-431) correctly flags the integrator to re-verify alpha order after both apply.
   - **Fence parity CLEARS.** Six fences = three balanced pairs (`edit:index.md` 140-143, `edit:SUMMARY.md` 156-158, `create:chapter` 171-420). The `create:` block ENCLOSES the full chapter body including `## Status` (351) and `## Evidence` (381) INSIDE the fence — no firm-body-outside-fence / nested-`text`-fence truncation defect. The chapter uses 4-space indented code blocks for the signature (not nested ` ``` ` fences), so the nested-fence-truncation hazard does not arise.
   - **L4 strawman notation CLEARS.** Signatures use Haskell `::` arrow form; the do-notation-free comprehension body is consistent with the strawman's `text`-fence convention (here realized as indented code). No invented notation.
   - **Over-unification guard CLEARS.** The "rank-1 scalar-ratio table, NOT a `gram_reduce` rank-2 specialization" framing is grounded: the OQ `gram-reduce-third-witness-probe-eigenmode-driven-postprocess` is DISCHARGED NEGATIVE at `scaffolding/open-questions.md:943` (c074), and `gram_reduce.md:178-189` carries the matching non-subsume text. `rough-in` is warranted (un-firm folded primitives + no eigenmode-postprocess test, both independently confirmed on disk).

## Repair

### Fixes attempted

- **Finding**: [citation drift, ±1] `quality_factor` assignment cited `postoperator.cpp:1201-1203` in two places (§Pattern-instances CYCLE.md:48; §Evidence in the `create:` chapter block CYCLE.md:398). On-disk the `vi.quality_factor =` statement spans 1200-1202 (LHS at 1200, `? mfem::infinity()` at 1201, `: freq_re/std::abs(...)` at 1202; line 1203 is the closing brace). `--anchor 'quality_factor'` reported DRIFT (anchor at 1200, outside 1201-1203).
  - **Decision**: repaired
  - **Action**: Corrected both occurrences `:1201-1203` → `:1200-1202` (CYCLE.md §Pattern-instances Instance-2; CYCLE.md §Evidence positive-site-2 inside the `create:book/src/L4/eigenfreq_qfactor_reduce.md` block). Mechanical line-range correction — the `vi.quality_factor =` LHS at line 1200 is now inside the range; line 1203 (closing brace, off-target) dropped.

- **Finding**: [borderline citation] `mode_port_kappa` assignment cited `postoperator.cpp:1199-1200` (§Pattern-instances CYCLE.md:48; §Evidence CYCLE.md:397). The `vi.mode_port_kappa =` assignment actually spans 1198-1199 (`vi.mode_port_kappa =` at 1198, `std::copysign(...)` continuation at 1199); line 1200 is the `vi.quality_factor =` line where `mode_port_kappa` appears only as the ternary condition. Range under-shot the assignment start (1198) and over-reached into the quality_factor line.
  - **Decision**: repaired
  - **Action**: Corrected both occurrences `:1199-1200` → `:1198-1199` (same two report sections). The two co-located corrections together land `:1198-1202` covering the kappa + quality_factor statements cleanly (the critic-predicted combined region).

### Verification

- Hand-Read `reference/palace/palace/models/postoperator.cpp:1195-1206` confirmed brace boundaries: `mode_port_kappa =` (1198) + `std::copysign` (1199); `quality_factor =` (1200) + `? mfem::infinity()` (1201) + `: freq_re/std::abs(...)` (1202); `}` (1203).
- `citecheck.py --anchor 'quality_factor' palace/models/postoperator.cpp:1200-1202` → ok (anchor at 1200 in range, no drift).
- `citecheck.py --anchor 'mode_port_kappa' palace/models/postoperator.cpp:1198-1199` → ok (anchor at 1198 in range, no drift).
- `citecheck.py --scan CYCLE.md` → 29 ok, 0 failing (no new bounds issues introduced).
- The broad body-spanning ranges (`postoperator.cpp:1188-1203`, `:1171-1203`, `:1188-1191`, `:1196-1198`) and the `κ=0 ⇒ Q=∞` guard pinpoint `:1201-1202` were NOT touched — the critic cleared those (the `mfem::infinity()` guard genuinely sits at 1201); surgical discipline limits the fix to the two flagged assignment pinpoints.

### Unrepairable findings

None. The single warning check (citation-validity) was two low-severity co-located line-range drifts, both mechanically repairable. All other 7 checks passed at critique.

## Suggested resolution

`ready`. Both pinpoint drifts corrected and re-verified with citecheck `--anchor` (no drift) and `--scan` (29 ok / 0 failing). Integrator notes: the report stages an `index.md` dep-map row + `SUMMARY.md` bullet + a new `book/src/L4/eigenfreq_qfactor_reduce.md` chapter `create:` block; the corrected `:1198-1199` / `:1200-1202` pinpoints now live in the staged chapter §Evidence — they land in `book/` when the create-block is materialized. The D1 alpha-position / anchor-collision coordination note (CYCLE.md §Coordination-with-D1) stands — sequence D1 and D3 serially and re-verify L4 alpha order after both apply, per the critic's cleared D1-collision check.
