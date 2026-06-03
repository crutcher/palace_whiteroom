---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T201500Z
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
repaired_at: 2026-06-03T202000Z
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

# META: verification of "Audit eigenfreq_qfactor_reduce — law-confidence / firm-on-positive-structure escape"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck --scan` on CYCLE.md (24 ok, 1 failing) and `--anchor` on every load-bearing pinpoint. The positive structure-side anchors that carry the promotion ALL verify on-disk: `postoperator.cpp:1200-1202` anchors `quality_factor` (the `(kappa==0.0) ? mfem::infinity() : freq_re/std::abs(kappa)` branch read literally, including the totality guard); `:1197` anchors `resistor_power`; `:1180` anchors `GetLumpedPortOp` (the per-port loop with NO inter-mode accumulator); `:1186-1191` anchors the `Q_mj = ω_m / κ_mj` formula comment; `eigensolver.cpp:424-439` anchors `omega` at lines [427, 433, 438] (`std::sqrt` at 433 linear EVP, `omega /= 1i` at 438 quadratic EVP, selector `!C && !has_A2` at 430). I independently read the full `MeasureLumpedPortsEig` body `:1171-1222` and the readout loop `:424-439` — both match the report's transcription exactly. The `verified_against:` YAML block round-trips clean under `yaml.safe_load` (7 entries; no leading-quote scalar break — the report notes it caught+fixed a `: ` colon-space break, and the result parses). **The one warning:** a path-hygiene inconsistency on the carried-forward (NON-firming-basis, `partially-supports`) test citation. Line 91 (Per-citation audit prose) writes the canonical `reference/`-relative form `palace/test/unit/test-postoperator.cpp`, but the proposed-changes that LAND in the artifact (verified_against entries lines 208/212, Status body line 177, index dep-map line 246, feature matrix line 262) drop the leading `palace/` segment and write `test/unit/test-postoperator.cpp`. The file lives at `reference/palace/test/unit/test-postoperator.cpp`; existing chapters cite it canonically as `palace/test/unit/...` (6 occurrences). citecheck still RESOLVES the prefix-dropped form by suffix-match (in-bounds, 672 lines) and both anchors verify there (`mode_port_kappa` at :216, `participation_ratio` at :160-188 — OK at the correct path), so the citation is not broken — but the proposed-changes will land a non-canonical, internally-inconsistent prefix into the artifact (canonical in the audit prose, non-canonical in every applied edit). The `operator.cpp:616-617` scan failure is `[AMBIG]` (basename matches two files), not a bounds failure — it is the inherited matrix-weighted-norm contrast L0 anchor in prose, not part of this verb's evidence; minor but worth a fully-qualified path too.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (a maturity promotion modifying the verb's `## Status` surface) and it carries the rotation/law evidence: the four laws are each tied to positive source + firm folded primitives. Record-definition sub-check: the verb's signature names no undefined record (it folds `ProblemType`/`EvpDegree` axes and scalar maps; the `(f, Q)` table is a per-mode scalar tuple, not a named struct needing a definition home). No record gap.

**rotation-quality — pass (the load-bearing check).** I independently adjudicated each of the 4 laws against the source I read, testing whether any smuggles in an unverified mathematical-property axiom: (1) concatenation-homomorphism — the full-body read confirms NO inter-mode accumulator (each `vi` keyed on its own port `idx`, computed only from that mode's `data`/`I_RLC`); the homomorphism is a structural read-off of the list-map spine, not a derived theorem. (2) un-transform purity — `std::sqrt`/`/= 1i` are closed-form scalar inverses folding firm L1 `eigenvalue-untransform` (c080) + a bare `.real()`. (3) Q scalar ratio — `freq_re / std::abs(mode_port_kappa)` is bare division over firm L1 `participation_ratio` (c077); no bilinear, rank-1 not a Gram grid (c074 D6). (4) lossless totality — `κ=0 ⇒ Q=∞` read literally off the `== 0.0 ? mfem::infinity() :` branch. NONE carries inner-product-axiom-class content. The decisive contrast is verified on-disk: `matrix-weighted-norm.md:143` explicitly states "the firm-on-positive-structure escape does not apply" because its laws 4/6/7 are triangle/Cauchy–Schwarz/parallelogram theorems conditional on SPD/Hermitian structure the L0 source only numerically asserts. The discrimination is sound — same auditor test, opposite outcome, correctly separated. The promotion is a genuine maturity rotation (rough-in → firm) backed by strictly-more-warranted evidence, not a rename.

**variant-axis-coverage — pass.** The load-bearing variant axis (linear vs quadratic EVP `ProblemType`/`EvpDegree` un-transform, `√μ` vs `λ/i`) is explicitly covered: the report walks the `!C && !has_A2` selector at `eigensolver.cpp:430` and records the wrong-arm case as a load-bearing NON-law ("no cross-branch identity"). The κ=0 lossless edge is covered as Law 4 (a total scalar-map edge, not a hidden branch). The resistive-vs-inductive port distinction in the source is correctly scoped to the resistive `mode_port_kappa` path. No hidden branches.

**cross-reference-integrity — pass.** All link targets resolve on-disk: the verb chapter, both folded primitives (`eigenvalue-untransform`, `participation_ratio`), the contrast `matrix-weighted-norm`, the precedent escapes (`assemble_frequency_operator`, `frequency_sweep`), the sibling reduction verbs (`gram_reduce`, `sparameter_reduce`, `domain_energy_reduce`, `inner_product`), the feature column files, and `eigenmode.L4` all exist. Edit-target anchors verified: index.md line 32 (`Firm at L4 (14 + 4 outer-driver)`), line 48 (`fe_assemble` bullet), line 56 (`Rough-in at L4 (2)`), line 100/101 (dep-map row), and the feature-column lines 8/55/62/64/68 all match the report's cited line numbers and current content. Count-delta arithmetic is sound: `domain_energy_reduce` is on-disk `rough-in` (gated on its rough-in `matrix-weighted-norm` primitive) and `solve_family` is `rough-in (test-coverage-bounded)`, so "rough-in 2 → 1 + 1 test-coverage-bounded" is accurate, and firm 14→15 follows from this single promotion. **The non-promotion reasoning is verified correct:** `eigenmode.L4` is on-disk `status: seed`, so the feature column `eigenfrequency-qfactor.L4` correctly STAYS `seed` (a feature column promotes past seed only when ALL constituents firm; the verb firms but the eigenmode driver-column constituent remains seed). A wrongly-promoted column would have been a defect; the report avoids it and routes the residual blocker to a new OQ.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is asserted (this is an L4-verb law-confidence audit, not a lowering-theme edit). The verb's downward lowering is correctly described as identity-in-form on the body via the in-line-marker route (no dedicated L4>L3 theme), consistent with the eigsolve/chebyshev precedent. Not applicable beyond that; pass.

**plan-kind-consistency — pass.** Declared kind = lowering-verifier law-confidence audit producing a firm promotion. The content shape matches: per-citation audit + applicability conditions + per-law verdicts + a `verified_against:` block, terminating in a firm `## Status` with the escape reasoning. No rough-in placeholders remain in the promoted body. The firm-on-positive-structure escape is applied with the same rigor that RULED IT OUT for the sibling matrix-weighted-norm — the audit does not over-reach (it explicitly leaves the carried test citations at `partially-supports` rather than upgrading them to manufacture a firming basis). Classification is correct.

**skill-uptake-survey — pass.** The report references `tools/citecheck/citecheck.py --anchor` (the citation-range verification realization) and palace-codemap `read_range` for on-disk re-verification — the relevant procedures for a law-confidence audit. Telemetry present; no gap.

### Issues found

1. **citation-validity (warning) — non-canonical / internally-inconsistent test-citation path in the APPLIED edits.** CYCLE.md lines 177, 208, 212, 246, 262 (Status body, both `verified_against:` test entries, the index dep-map row, the feature-column constituent matrix) cite the postprocess test as `test/unit/test-postoperator.cpp`, dropping the leading `palace/` segment. The canonical `reference/`-relative form (CLAUDE.md citation-format invariant) is `palace/test/unit/test-postoperator.cpp` — which is also how line 91 of this same report and the 6 existing on-disk chapter citations write it. The file is at `reference/palace/test/unit/test-postoperator.cpp`; the prefix-dropped form does NOT resolve under `reference/` by path, though citecheck's suffix-match still finds it in-bounds and both anchors (`mode_port_kappa` :216, `participation_ratio` :160-188) verify at the correct path. Severity: low — the citation points to a real, in-range, anchor-confirming location and is non-firming (`partially-supports`); but the applied edits would land an inconsistent prefix into the artifact (canonical in this report's prose, non-canonical in every edit it applies). Repair = normalize the 5 applied-edit occurrences to `palace/test/unit/test-postoperator.cpp`.

2. **citation-validity (minor, same warning) — ambiguous-basename contrast anchor.** The inherited matrix-weighted-norm contrast L0 anchor `operator.cpp:616-617` (CYCLE.md line 85) is `[AMBIG]` under citecheck (basename matches `linalg/operator.cpp` and `fem/libceed/operator.cpp`). It is a contrast citation, not this verb's evidence, so non-blocking; fully-qualifying it to `palace/linalg/operator.cpp:616-617` would clear the scan.

## Repair

### Fixes attempted

- **Finding 1**: citation-validity (warning) — non-canonical / internally-inconsistent test-citation path in the 5 APPLIED edits (`test/unit/test-postoperator.cpp`, dropping the leading `palace/` segment) at CYCLE.md lines 177, 208, 212, 246, 262.
  - **Decision**: repaired.
  - **Action**: Verified on-disk that the file lives at `reference/palace/test/unit/test-postoperator.cpp`, so the canonical `reference/`-relative form (CLAUDE.md citation-format invariant) is `palace/test/unit/test-postoperator.cpp` — confirmed against the 6 existing canonical on-disk chapter citations and line 91's audit prose in this same report. Normalized all 5 applied-edit occurrences (CYCLE.md §Status body line 177, the two `verified_against:` test entries lines 208/212, the index dep-map row line 246, the feature-column constituent matrix line 262) to the canonical `palace/test/unit/test-postoperator.cpp` prefix. Post-fix grep confirms zero non-canonical occurrences remain in CYCLE.md and all 6 (5 edits + audit prose) are now uniform. Purely a prefix-consistency fix — anchors already verified via suffix-match; the landed artifact text is now internally consistent.

- **Finding 2**: citation-validity (minor, same warning) — ambiguous-basename contrast anchor `operator.cpp:616-617` (CYCLE.md line 85) is `[AMBIG]` under citecheck (basename matches `palace/linalg/operator.cpp` and `palace/fem/libceed/operator.cpp`).
  - **Decision**: repaired.
  - **Action**: This anchor sits in the report's own §Per-citation-audit contrast-citation prose (line 85), NOT in any `~~~edit:` proposed-changes block — so it does not itself land in the artifact, but it is the report author's own citation (not inherited chapter text), and the disambiguation is a trivial one-token add. Verified on-disk the two basename collisions (`palace/linalg/operator.cpp` + `palace/fem/libceed/operator.cpp`) and that the referenced `matrix-weighted-norm.md` chapter cites this anchor canonically as `palace/linalg/operator.cpp:616-617`. Fully-qualified the in-prose anchor to `palace/linalg/operator.cpp:616-617`, clearing the `[AMBIG]` scan flag.

### Unrepairable findings

None. Both findings were mechanical path-hygiene normalizations within repair authority; the load-bearing rotation-quality / plan-kind-consistency promotion-soundness check passed unmodified.

## Suggested resolution

`ready`. The single critic warning was a purely cosmetic citation-path-prefix inconsistency (the cited anchors all verify on-disk by suffix-match; the file content and line ranges were never in question). Both occurrences are now normalized to the canonical `reference/`-relative form. Note for the integrator: the report's §Edit-3 trailing note already flags that the L1/L0 feature-column files (`eigenfrequency-qfactor.L1.md` / `.L0.md`) carry the same verb-gate prose and the same non-canonical `test/unit/...` form in pre-existing chapter text; those are existing-artifact occurrences outside this report's applied edits (out of repair scope), and the integrator's parallel mechanical refresh of those two files should adopt the canonical `palace/test/unit/...` form to keep the artifact uniform.
