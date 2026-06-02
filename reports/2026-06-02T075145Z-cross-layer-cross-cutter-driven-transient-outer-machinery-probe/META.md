---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T08:08:04Z
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
repaired_at: 2026-06-02T08:20:00Z
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

# META: verification of "Cross-layer observation — driven/transient outer machinery beyond the characterized solve loops"

## Critique

### Checks run

**citation-validity — warning.** Every load-bearing anchor was verified against on-disk source via `palace-codemap read_range`. The Region-1 candidate spine (the verdict's whole basis) is CLEAN and exact: `drivensolver.cpp:176-177` (`GetSystemMatrix(1+0i, iω, −ω²+0i, K,C,M,A2)`), `:174` (`A2 = GetExtraSystemMatrix<ComplexOperator>(omega, …)`), `:180` (`ksp.SetOperators(*A,*P)`), `:92-94` (K/C/M assembled once before the loop), `spaceoperator.cpp:522-528` (`GetSystemMatrix ≡ BuildParSumOperator({a0,a1,a2,1},{K,C,M,A2})`), `rap.cpp:765-786` (the `SumOperator` + `sum->AddOperator(ops[i]->LocalOperator(), coeff[i])` for `coeff[i]!=0` body — the quoted snippet matches). The firm-vocabulary anchor `L3/linear_combination.md:34-37` matches the quoted `foldl (\acc (a,t) -> acc + scal a t)` signature exactly. Transient anchors all clean: `transientsolver.cpp:30-31`, `:33`, `:35-36`, `:98-99`, `:104`. Book anchors `solve_family.md:65` and `fold_solve.md:61,63,64` all confirm the claims attributed to them. The warning is for two NON-load-bearing drifts in Region 2 (solver-specific, does not touch the verdict): (i) `drivensolver.cpp:207` is cited for `floquet_corr->AddMult` but that call is at line **212** — line 207 is `B *= -1.0/(1i*omega)` (`[DRIFT +5]`); (ii) the curl recovery is attributed to `:202-204` but `Curl.Mult(E.Real(),...)` / `Curl.Mult(E.Imag(),...)` are at lines **205-206** — `:202-204` captures the surrounding comment, not the Mult calls (`[DRIFT ~+2]`). Both are on Region-2 postprocessing anchors classified solver-specific, so neither affects any disposition; flagged as warning rather than pass for line-map accuracy.

**surface-or-evidence — pass.** Observation-only probe; no `book/` surface mutation (confirmed: §Proposed-changes is "None for `book/`", only an append-only OQ intake). This is not a refinement-shaped proposal — it is a coverage-gap observation + LICENSE-FUTURE recommendation, which is the cross-layer-cross-cutter's native shape. The `assemble_frequency_operator` candidate is correctly framed as future-landing-licensed, not asserted as landed surface. Not applicable as a refinement check; the evidence backing the candidate (the `BuildParSumOperator` fold body vs. the firm `linear_combination` fold) is cited and verified.

**rotation-quality — pass (largely not applicable to observation-kind, one structural claim checked).** The report asserts no L_{n+1} surface rotation this dispatch. The one structural assertion — that operator-domain `BuildParSumOperator` is the operand-category lift of the tensor-domain firm `linear_combination` fold — is sound and IS a genuine vocabulary extension (operand monoid = operator-addition / scalar-operator-scaling, vs. tensor-addition), not a 1:1 rename. The anti-mirror disposition (re-express THROUGH an operand-category variant axis on the EXISTING `linear_combination`, replace-and-propagate, NOT a mirrored `operator_linear_combination` chapter) is exactly the 2026-06-01 redirect's prescribed handling. Correct.

**variant-axis-coverage — pass.** The probe explicitly enumerates the orthogonal axes and scopes each: the operand-category axis (`tensor-operand | operator-operand`) is named as the variant axis for the proposed lift; the `A2` term is correctly broken out as an ω-dependent-OPERAND caveat distinct from the ω-dependent-COEFFICIENT `{K,C,M}` basis (verified at source: `A2 = GetExtraSystemMatrix(omega)` carries literal coeff `1` in `BuildParSumOperator({a0,a1,a2,1},…)`). The two harvester-routing options for `A2` ((a) 4th basis operator with coeff-1 = literal source shape; (b) non-affine correction noted separately) are both surfaced — no hidden branch. The cross-pipeline coverage axis (driven vs. transient vs. electro/magnetostatic vs. eigenmode) is fully enumerated to justify the single-pipeline call.

**cross-reference-integrity — pass.** All referenced book entries resolve on disk: `book/src/L3/linear_combination.md` (firm, signature verified), `book/src/L2/linear_combination.md` (firm, exists), `book/src/L4/solve_family.md`, `book/src/L4/fold_solve.md`. The cited skill `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` exists. No `[link]` markdown references to dead targets (observation report, plain-text path citations throughout). No new slug is claimed-as-existing (`assemble_frequency_operator` is named as a FUTURE candidate, not referenced as a live entry). Build-readiness fence guard N/A (no proposed-changes block, no firm-claim body).

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (observation-kind). The report references existing edges descriptively (the unwritten driven-assembly L1>L0 home; the `fold_solve` op-capture-once stratum) and the prose discusses those exact relationships. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared `agent: cross-layer-cross-cutter`, content shape is a coverage-gap/edge-classification observation with one LICENSE-FUTURE recommendation and three spine-complete/solver-specific classifications — exactly the observation kind. No firm-operator placeholders, no mis-tier. The single-witness candidate is correctly NOT promoted to a mine-now (it is licensed-future, single-pipeline-by-design), consistent with the observation-only mandate.

**skill-uptake-survey — pass.** The proposal shape (cross-pipeline combinator candidacy) implies the `disciplined-cross-pipeline-combinator-mining-gate` skill, and the report explicitly invokes it (§Specific finding step-1 single-witness→coverage-finding; §Supporting evidence "Mining-gate skill cited"). The anti-mirror / replace-and-propagate disposition references the 2026-06-01 vocabulary-shift redirect. Skill telemetry present and correctly applied.

### Issues found

1. **`drivensolver.cpp:207` cited for `floquet_corr->AddMult`; actual line is 212** — `reports/.../CYCLE.md` §Specific finding Region 2 (line 46) and §Supporting evidence Region 2 (line 81). Line 207 is `B *= -1.0/(1i*omega)`; the Floquet `floquet_corr->AddMult(E, B, 1.0/omega)` is at line 212. `[DRIFT +5]`. Severity: low — Region 2 is classified solver-specific (non-load-bearing for the verdict); corrected line is 212.

2. **Curl recovery attributed to `drivensolver.cpp:202-204`; the `Curl.Mult` calls are at 205-206** — same two locations (lines 46, 81). The range `:202-204` encloses the `// Compute B = -1/(iω) ∇ x E` comment but not the two `Curl.Mult(E.Real()/E.Imag(), …)` calls, which are lines 205-206 (with `B *= -1/(iω)` at 207). `[DRIFT ~+2]`. Severity: low — same non-load-bearing Region-2 anchor; suggested range `:204-207`.

3. **(Non-defect, for repairer awareness)** No load-bearing issue found in Regions 1/3/4 or in the disposition logic. The witness-count call (fold firm-by-extension via tensor BLAS-1 cohort; driven specialization single-pipeline-by-design; no 2nd-pipeline discharge probe), the anti-mirror replace-and-propagate framing, the `A2` affine-modulo caveat, and the three spine-complete/solver-specific classifications all verify against source and the cited book anchors. The two drifts above are the only correctable findings.

## Repair

### Fixes attempted

- **Finding 1**: `drivensolver.cpp:207` cited for `floquet_corr->AddMult`; actual line is 212.
  - **Decision**: repaired
  - **Action**: Verified via `palace-codemap search_text` + `read_range` that `floquet_corr->AddMult(E, B, 1.0 / omega)` is at `drivensolver.cpp:212` (line 207 is `B *= -1.0 / (1i * omega)`). Corrected `:207` → `:212` in CYCLE.md §Specific finding Region 2 (line 46) and §Supporting evidence Region 2 (line 81). Off-by-+5 line-slip; mechanical citation fix within repair authority.

- **Finding 2**: Curl recovery attributed to `drivensolver.cpp:202-204`; the `Curl.Mult` calls are at 205-206.
  - **Decision**: repaired
  - **Action**: Verified via codemap that `Curl.Mult(E.Real(), B.Real())` / `Curl.Mult(E.Imag(), B.Imag())` are at `drivensolver.cpp:205-206` (the `// Compute B = -1/(iω) ∇ x E` comment is at 204; `B *= -1/(iω)` at 207). Corrected `:202-204` → `:205-206` (with the `:207` scale step noted inline) in CYCLE.md §Specific finding Region 2 (line 46) and §Supporting evidence Region 2 (line 81). Small off-by-~+2 line-slip; mechanical citation fix.

Both fixes are line-slip corrections on NON-load-bearing Region-2 (solver-specific S-parameter/port postprocessing) anchors. Neither touches the verdict — the load-bearing Region-1 `assemble_frequency_operator` candidate-spine anchors were all verified clean by the critic and are untouched. This is an observation-only report (prose does not reach `book/`), but the citations were tightened since they are cheap mechanical fixes.

### Unrepairable findings

None. The sole flagged check (citation-validity) was two mechanical line-slips, both repaired.

## Suggested resolution

`ready`. All eight checks now resolve to pass / repaired / not-needed. Integrator notes: this is an observation-only probe — §Proposed-changes is "None for `book/`" plus an append-only OQ intake; no artifact surface mutation. The LICENSE-FUTURE recommendation (operator-valued `linear_combination` + `assemble_frequency_operator` driven specialization, batch-19 low-priority pull-gated) is a plan/OQ-channel item, not a surface change to apply this cycle.
