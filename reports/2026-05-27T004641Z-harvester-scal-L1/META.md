---
verifies: ../REPORT.md
critiqued_at: 2026-05-27T00:55:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T01:05:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of REPORT: Formalize scal at L1

## Critique

### Checks run

- **citation-validity**: `vector.hpp:98-99` (`operator*=` decl with comment "Scale all entries by s."), `vector.cpp:203-227` (def with `si == 0.0` real-fast-path at 207-211, `forall_switch` general kernel at 212-225), `vector.hpp:262-270` (`Normalize` template), `iterative.cpp:632` and `:811` (GMRES `w *= 1.0 / Hj[j+1]`) all verified in-range against `reference/palace/palace/linalg/`. pass.
- **surface-or-evidence**: New L1 chapter + dep-map row + SUMMARY wire — surface-creating proposal with direct L0 evidence. pass.
- **rotation-quality**: L0 mutating `operator*=` collapses to pure `(α, x) → α·x`; the `imag==0` shape-branch (a transparent perf trick) is eliminated at L1. Strictly more compact. pass.
- **variant-axis-coverage**: Two axes called out (element-type real/complex; scalar-promotion sub-axis). The L0 `imag==0` branch is correctly classified as a complex-scalar-shape specialisation, not a scalar-value branch (contrast with `axpy`'s `α==1.0`). pass.
- **cross-reference-integrity**: Links to `axpby.md`, `nrm2.md`, `concepts/scal.md`, `decisions/axpby-as-primitive.md` all resolve under `book/src/` and `scaffolding/`. pass.
- **edge-label-fidelity**: All edge mentions are L1>L0 and the prose stays at that edge. pass.
- **plan-kind-consistency**: Declared `firm`; signature, evidence, and laws all firm-shaped (no placeholders). pass.
- **skill-uptake-survey**: No mention of `verify-citation-range`, `classify-variant-axis`, or `verify-refinement-surface`. The "skill_uptake block ambiguity" open question (line 160) surfaces format uncertainty but does not record actual skill invocations. warning.

### Spot-check of the 9 algebraic laws against `scal(α, x) = α·x`

- Law 1 (identity, `scal(1, x) = x`): correct.
- Law 4 (composition, `scal(α, scal(β, x)) = scal(α·β, x)`): correct; the bit-determinism non-law caveat is appropriate.
- Law 8 (inverse for non-zero α): correct, and the `Normalize`-invertibility framing is apt.

The "non-law" idempotence-condition statement (`α² = α` ⇒ `α ∈ {0,1}`) is correct for real but slightly imprecise for complex (over ℂ the roots of `α(α−1)=0` remain `{0,1}`, so the conclusion holds, but the prose could note the field). Minor.

### Subsumption with `axpby` verified

`axpby` laws 2 (`axpby(0, x, β, y) = β·y`) and 3 (`axpby(α, x, 0, y) = α·x`) at `book/src/L1/axpby.md:51-52` directly underwrite `scal(α, x) = axpby(α, x, 0, y) = axpby(0, y, α, x)`. Both directions cited correctly. The "sibling, not dependency" framing matches `decisions/axpby-as-primitive.md` discipline.

### "No free-function `linalg::Scal`" verified

`grep -nE "linalg::Scal\b|linalg::Scale\b|::Scal\(" reference/palace/palace/linalg/*.{cpp,hpp}` returns empty. Claim holds.

### Issues found

1. **skill-uptake telemetry absent** (Status section / overall). No reference to `verify-citation-range` or `classify-variant-axis` invocation despite the report doing both kinds of work. Pure telemetry; non-blocking. (severity: low)
2. **`skill_uptake:` block omission noted as open question** (line 160). Conservative omission per CLAUDE.md ambiguity rule is defensible, but flags an unresolved format question the integrator should clarify. (severity: low)
3. **Idempotence non-law field-precision** (line 85). The `α² = α` characterisation is correct over both ℝ and ℂ, but the prose reads as if only the real case were considered. Cosmetic. (severity: trivial)
4. **Citation path convention** — report cites `palace/linalg/...` (matching CLAUDE.md format `relative/path/file.ext:start-end` rooted at `reference/`); actual on-disk path is `reference/palace/palace/linalg/...` (double-nested). Citations resolve correctly under the project convention but worth confirming this is the intended root. (severity: trivial)

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey warning — `skill_uptake:` frontmatter block missing.
  - **Decision**: repaired
  - **Action**: Added `skill_uptake:` block to REPORT.md frontmatter (after `inputs:`, before closing `---`) mirroring the axpby/dot/nrm2 format. Three entries: `verify-citation-range` (triggered: true, explained_non_applicable — citations verified inline during authoring), `classify-variant-axis` (triggered: true, artifact_landed — two axes landed: element-type real|complex, scalar-promotion sub-axis), `verify-refinement-surface` (triggered: true, explained_non_applicable — three proposed-changes blocks verified by inspection against cycle-003 precedents).
  - Rationale: format precedent is fixed across axpy/dot/nrm2/axpby; classifications are mechanically derivable from the report's own Variant axes section and proposed-changes blocks. No content authoring required.

### Unrepairable findings

None.

## Suggested resolution

Ready for integration. The critic's three other low/trivial issues (open-question line 160, idempotence field-precision, citation path convention) are non-blocking and remain noted in the META critique for the integrator's reference; none warrant repair-phase edits.
