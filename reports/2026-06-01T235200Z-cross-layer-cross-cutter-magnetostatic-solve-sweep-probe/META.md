---
verifies: ./CYCLE.md
critiqued_at: 2026-06-01T236000Z
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
repaired_at: 2026-06-01T237000Z
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

# META: verification of cross-layer observation — magnetostatic-solve-sweep-probe (CONFIRMS, single-witness gate discharge)

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` (7 ok / 1 OOB) plus `--anchor` on every load-bearing pinpoint. The `Solve`-body citations are clean and accurate: `magnetostaticsolver.cpp:21-109` in-bounds; verified via `read_range` that `:29` = `auto K = curlcurl_op.GetStiffnessMatrix()`, `:30` = `const auto &Curl = ...`, `:35` = `ksp.SetOperators(*K, *K)` (with ksp constructed `:34`), `:67` = `for (const auto &[idx, data] : curlcurl_op.GetSurfaceCurrentOp())`, `:76` = `GetExcitationVector`, `:77` = `ksp.Mult(RHS, A[step])`, `:85` = `Curl.Mult(A[step], B)`. The two `curlcurloperator.cpp` citations are accurate (`:171-210` `CurlCurlIntegrator` anchored at 181; `:212-236` `AddExcitationBdrCoefficients` anchored at 218). The electrostatic cross-witness `electrostaticsolver.cpp:60-89` is accurate (`ksp.Mult` at 69, matching D6's claimed `:69`). **The defect is localized entirely to the `PostprocessTerminals` block**, where the report's line numbers are uniformly ~1-5 lines HIGH and the enclosing range overshoots the file: file is 206 lines; `PostprocessTerminals` body ends at 205, namespace-close at 206. See issues below for the exact drift map. None of the drift changes the *meaning* of any claim (each cited construct exists at the corrected line), so this is `warning`, not `fail` — but the pinpoints feed a cycle-054 combinator-miner dispatch and should be corrected so the miner re-localizes cleanly.

**surface-or-evidence — pass.** Not a refinement-shaped proposal — this is a pure observation-only cross-pipeline probe with `Proposed-changes: NONE` and no `book/` mutation. No operator/theme surface is touched; the deliverable is the CONFIRMS verdict + OQ-ledger appends. The surface-vs-evidence dichotomy does not gate an observation report.

**rotation-quality — pass.** Not applicable to an observation/coverage-gap report — no algebraic/structural rotation is asserted. The report explicitly defers the combinator authoring (which WOULD carry a rotation claim) to a cycle-054 combinator-miner dispatch. The shape it records (assemble-once → map-`ksp_solve`-over-RHS-family-against-fixed-operator → collect → O(n²) energy-product reduce → invert) is a faithful structural description, not a claimed L_{n+1}→L_n compaction.

**variant-axis-coverage — pass.** The probe handles its variant axes well. It explicitly enumerates the leaf-content variant axes that distinguish the two witnesses (curl-curl vs diffusion integrator; surface-current vs terminal excitation; `Mult` vs `AddMult` field recovery; inductance vs capacitance reduction) and correctly scopes them as leaf-level, NOT structural — see verdict-soundness check below. The driven/transient operator-fixed-vs-varying axis is explicitly carried as an open caveat rather than silently assumed, which is the correct treatment of an un-probed branch.

**cross-reference-integrity — pass.** All six spine cross-references resolve on disk: `book/src/L4/ksp_solve.md`, `book/src/L1/apply_linop.md`, `book/src/L1/bilinear-form.md`, `book/src/L1/nrm2.md`, `book/src/L1/dot.md`, `book/src/L2/gram.md`. The `bilinear-form` status claim ("rough-in") matches the file. The D6 cross-witness report (`reports/2026-06-01T223300Z-cross-layer-cross-cutter-electrostatic-solver-probe/CYCLE.md`) exists. No firm-body-inside-fence concern (no proposed-changes block). `git status book/` is clean — observation-only confirmed.

**edge-label-fidelity — pass.** The report's scope edge label is `L1↔L2 cross-cut`. The prose discusses exactly that band: it maps the magnetostatic driver body against existing L1 operators (`ksp_solve` at L4/`apply_linop`/`bilinear-form`/`nrm2`/`dot` at L1) and the L2 `gram` reduction analog, identifying the missing driver-level combinator as a gap across that band. The L4 `ksp_solve` reference is the inner-solve cap, correctly distinguished from the outer sweep. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared as an observation (coverage-gap, confirmed cross-pipeline) with `status: pending` and `Proposed-changes: NONE`. Content shape matches: it is a witness-discharge probe that records a shape and recommends downstream dispatch, authoring no artifact. No mis-classification — it does not masquerade as a firm operator/theme entry.

**skill-uptake-survey — pass (telemetry).** The probe's shape (cross-pipeline structural comparison + single-witness-gate discharge) has no dedicated skill to invoke; the citation-grounding it relies on is the producer's own `read_range` localization, which is appropriate. No missing skill-invocation reference. Surfacing only: this is the second instance of a "solver test-load Nth-witness probe" shape (D6 electrostatic → D1 magnetostatic); if a third lands, a `cross-pipeline-witness-discharge` skill candidate may be worth proposing.

### Issues found

1. **[citation-validity, warning] `PostprocessTerminals` range overshoots file end — `magnetostaticsolver.cpp:110-209` (CYCLE.md §Summary, §Specific-finding step-7 row, §Supporting-evidence bullet 2).** File has 206 lines (`citecheck --scan` OOB). The `PostprocessTerminals` function body ends at line 205; line 206 is `}  // namespace palace`. Corrected range: `:110-205`. Recurs in the §Summary prose (`PostprocessTerminals`, `:110-209`) and the step-7 reduction row.

2. **[citation-validity, warning] `PostprocessTerminals` internal pinpoints drift ~1-5 lines high (CYCLE.md §Specific-finding step-7 row + §Supporting-evidence bullet 2).** Verified via `read_range` + `--anchor`:
   - `M(A.size())` claimed `:123` → actual line 122 (`mfem::DenseMatrix M(A.size()), Mm(A.size());`); drift −1.
   - diagonal kernel claimed `:130-135` → "Diagonal" comment at 124, body `M(i,i)=...` at 125-130; suggested `:125-130`; drift ~−5.
   - off-diagonal `M(i,j)=.../(Iᵢ·Iⱼ)` claimed `:140-141` → actual `I_inc[i]*I_inc[j]` at line 138; drift ~−2.
   - `Minv.Invert()` claimed `:156` → actual line 152; drift −4.
   - the O(n²) double-loop claimed `:124-153` → actual loop spans ~123-149.
   - second `Mm` matrix claimed `:142-153` → the `Mm` off-diagonal/normalization lines are ~139-148.
   None changes a claim's meaning (every cited construct exists at the corrected line; the structural twin claim is honest), but the pinpoints feed the cycle-054 combinator-miner and should be corrected. NOTE: pinpoints OUTSIDE this block are correct — the drift is isolated to `PostprocessTerminals`, suggesting the producer's line offset slipped only in that sub-read.

## Repair

### Fixes attempted

- **Finding**: [citation-validity, warning] `PostprocessTerminals` range overshoots file end (`magnetostaticsolver.cpp:110-209`; file is 206 lines, body ends 205).
  - **Decision**: repaired
  - **Action**: Re-verified via `read_range` that the file ends at line 206 (`}  // namespace palace`) and the `PostprocessTerminals` body closes at 205. Corrected `:110-209` → `:110-205` in all three occurrences: CYCLE.md §Summary prose, §Specific-finding step-7 row, §Supporting-evidence bullet 2.

- **Finding**: [citation-validity, warning] `PostprocessTerminals` internal pinpoints drift ~1-5 lines high (§Specific-finding step-7 row + cross-witness table row + §Supporting-evidence bullet 2 + §Open-questions inductance-reduction OQ).
  - **Decision**: repaired
  - **Action**: Re-confirmed each construct against source via `read_range` and applied corrections:
    - `M(A.size())` `:123` → `:122` (`mfem::DenseMatrix M(A.size()), Mm(A.size());`).
    - diagonal kernel `:130-135` → `:125-130` (comment `Diagonal` at 124, body `M(i,i)=...` at 125-130).
    - off-diagonal `M(i,j)=.../(I_inc[i]*I_inc[j])` `:140-141` → `:138`.
    - `Minv.Invert()` `:156` → `:152`.
    - `O(n²)` double-loop `:124-153` → `:123-149`.
    - second `Mm` matrix `:142-153` → `:139-148`.
    - off-diagonal comment pinpoint `:135` → `:131` (the `Mᵢⱼ` comment line).
    - cross-witness table step-7 reduction `(:123-156)` → `(:122-152)`.
    - §Open-questions inductance-reduction OQ `magnetostatic :123-156` → `:122-152`.
    - §Supporting-evidence CSV-output `:158-208` → `:154-203` (root-write block starts `:154`, ends within body before close at 205).
  - All corrected pinpoints re-verified against `reference/palace/palace/drivers/magnetostaticsolver.cpp`. The drift was isolated to the `PostprocessTerminals` sub-read; pinpoints outside that block (the `Solve` body, `curlcurloperator.cpp`, the electrostatic cross-witness) were verified clean by the critic and left untouched. No claim meaning changed — every cited construct exists at the corrected line; the corrections make the pinpoints clean for the cycle-054 combinator-miner re-localization.

- **Findings (issues 3 & 4)**: CONFIRMS verdict-soundness + driven-caveat soundness — both marked SOUND (informational, no severity) by the critic.
  - **Decision**: not-needed (no defect; positive confirmations carried forward).

### Unrepairable findings

None. The single warning (citation-validity, pinpoint drift) was mechanical and entirely repairable — the constructs exist at the corrected lines, so this was a copy-offset correction, not substantive re-authoring. No `book/` mutation (observation-only report; `Proposed-changes: NONE` preserved).

## Suggested resolution

`ready`. Notes for the integrator:
- Observation-only — no `book/` proposed-changes to apply.
- The deliverable carrying forward is (a) the **CONFIRMS verdict** — the shared-operator parametric solve-sweep is now 2-of-N witnessed (electrostatic + magnetostatic), the fixed-operator solve-family combinator is mineable; and (b) the **driven-caveat** — driven re-assembles the system matrix `(K+iωC−ω²M)` per frequency step (critic confirmed source-definite at `drivensolver.cpp:176`/`:180`), so the combinator is fixed-operator-only, with the operator-varying form as the general case and fixed-operator as a specialization. These feed a **cycle-054 combinator-miner** dispatch.
- Promote the three §Open-questions entries (`solve-family-combinator-confirmed-2-of-n-mine-now`, `solve-sweep-shared-operator-capture-invariant-needs-driven-transient-check`, `inductance-capacitance-reduction-now-2-witness-gram-hypothesis`) to `scaffolding/open-questions.md` at integration.

3. **[no severity — informational, CONFIRMS verdict is SOUND] Verdict-soundness audit passed.** Verified the load-bearing structural-twin claim directly against source: the operator is genuinely fixed once (`K` assembled `:29`, `Curl` `:30`, `SetOperators` `:35`, all outside the loop at `:67`; nothing in the loop body `:67-99` re-assembles `K` or re-calls `SetOperators` — confirmed by full `read_range` of `:21-109`). The inner solve `ksp.Mult(RHS, A[step])` `:77` is the same `ksp_solve` cap against the shared `K`. The collection (`std::vector<Vector> A(n_step)` `:44`, indexed `A[step]`) and the O(n²) energy-product reduce + LAPACK `Invert()` match. The four differences D1 labels "leaf-content" ARE genuinely leaf-level: `CurlCurlIntegrator` vs `DiffusionIntegrator` (integrand, not assembly shape), surface-current vs terminal excitation (RHS-construction detail, not sweep structure), `Curl.Mult` (non-accumulating) vs `Grad.AddMult` (accumulating) field recovery (a variant axis OUTSIDE the sweep combinator — D1 correctly flags it should not be folded in), inductance vs capacitance (physical meaning of the same Gram-shaped reduction). None is a structural difference. The CONFIRMS-at-2-of-N gate discharge for the fixed-operator case is sound.

4. **[no severity — informational, driven-caveat is SOUND and if anything understated] driven operator-varying caveat confirmed against source.** The report flags driven's matrix `(K+iωC−ω²M)` as changing per frequency step "plausibly". Verified at `drivensolver.cpp:176` — `space_op.GetSystemMatrix(1.0 + 0.0i, 1i * omega, -omega * omega + 0.0i, ...)` IS exactly `(K + iωC − ω²M)`, and `ksp.SetOperators(*A, *P)` at `:180` is INSIDE the frequency loop (the source comment states "The operators are constructed for each frequency step"). So driven definitively breaks shared-operator-capture — the caveat is not just plausible but source-confirmed. This correctly gates the mined combinator to fixed-operator-only (`map_solve_over_rhs_family[fixed A]`) with the operator-varying sibling (`map_solve_over_(operator,rhs)_family`) as the more general form. The caveat's "near-certain operator-varying counter-shape" phrasing is, if anything, conservative — it is certain. (No correction required; recorded as positive confirmation for the repairer/integrator.)
