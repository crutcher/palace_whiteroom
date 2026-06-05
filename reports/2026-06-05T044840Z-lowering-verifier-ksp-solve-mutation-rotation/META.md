---
verifies: ../REPORT.md
critiqued_at: 2026-06-05T04:55:35Z
critic_version: 1
checks:
  citation-validity: fail
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-05T05:10:00Z
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

# META: verification of "Audit ksp-solve-mutation-rotation"

## Critique

### Checks run

**citation-validity — FAIL.** Re-read every load-bearing cited L0 range via codemap `read_range` against the on-disk Palace source. The outer rewrite and the per-step cites are mostly exact, but the report carries a **false-positive drift flag that would corrupt a correct citation** — see Issue 1. Verified exact (no drift): `ksp.cpp:296-310` (line 296 = `BaseKspSolver<OperType>::Mult` signature, 299 BlockTimer, 300 inner `ksp->Mult(x,y)`, 301-307 `Mpi::Warning` block, 308-309 counters, **310 = `}`** END close-brace exact; 312-313 = template instantiations) — the report's END-bound claim holds. CG per-step (window 440-464): 440 AXPBY, 443 `A->Mult(p,z)`, 444 `denom = linalg::Dot(comm,z,p)`, 448 `x.Add(alpha,p)`, 449 `r.Add(-alpha,z)`, 460 `beta = linalg::Dot(comm,z,r)`, 463 `converged = (res<eps)` — all line-exact. GMRES per-step (window 625-641): 627 `ApplyBA`, 630 `OrthogonalizeIteration`, 636-640 Givens (`ApplyPlaneRotation` replay loop + `GeneratePlaneRotation` + two `ApplyPlaneRotation`), 703-704 `final_res = beta; final_it = it;` — all line-exact. Switch (`ksp.cpp:34-58`): CG arm at 36, GMRES `case` at 39, FGMRES at 46, MINRES/BICGSTAB/DEFAULT at 53/54/55, `MFEM_ABORT` at 56 — exact. The pre-existing YAML defect at on-disk line 802 is **REAL**: `python3 -c "import yaml; yaml.safe_load(...)"` on the existing `case MINRES: case BICGSTAB: ...` note fails with `yaml.scanner.ScannerError: mapping values are not allowed here` (column 22, the first mid-string colon) — the report correctly identifies this and the integrator-action flag is well-founded. The 10 proposed appended rows round-trip cleanly (verified by extracting and `yaml.safe_load` — `APPENDED-ROWS-PARSE-OK`); no appended note begins with a leading quote and none introduces a `: `-scanner trap. The FAIL is driven solely by Issue 1.

**surface-or-evidence — PASS.** This is a lowering-theme firm-promotion audit, not a surface-modifying proposal; its evidence is the re-read of the cited L0 ranges plus the per-step sister-theme cross-check, which is the correct evidence shape for a `lowering-verifier` discharge of a deferred per-step gate. No record-definition gap: `SolveResult` is defined in the L1 `ksp_solve` chapter (referenced, not newly named here); the theme references it, it does not introduce an undefined signature record.

**rotation-quality — PASS.** The verdict rests on the firm-on-positive-structure / syntactic-identity escape, applied to a structural mutation-rotation (in-place `Mult(b,x)` → pure `ksp_solve(K,b) → SolveResult`). The four-surface-concern absorption (timer-erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding) is a genuine state-hiding / threaded-state compression, not a 1:1 rename. The rank-invariant treatment of the rough-in `apply-linop` sister theme as a per-step `reference` recognition edge (not a blocking `depends-on`) is sound under the graded-stack §1b reading: the per-step `A->Mult(p,z)` is a one-line syntactic identity on fully-specified positive source (line 443, confirmed), and the firm verdict rests on that escape, not on apply-linop's own promotion. The report's own note that D1 is independently firming apply-linop this cycle further de-risks the watch-item. Judgment accepted.

**variant-axis-coverage — PASS.** The four sub-patterns (A outer / B CG / C GMRES / D FGMRES) plus the six applicability conditions cover the implemented-method axis exhaustively; the MINRES/BICGSTAB/DEFAULT complement is explicitly scoped out and routed to the sibling obstruction themes (confirmed `MFEM_ABORT` at `ksp.cpp:56`). No hidden branch. The audit confirms the recognition set is closed (1 outer `BaseKspSolver` entry + exactly 3 implemented `IterativeSolver` subclasses).

**cross-reference-integrity — PASS.** Dep-map row `index.md:36` confirmed on disk (status cell `rough-in *(firmed cycle-008)*`, the Edit-3 target). L1 endpoint `L1/ksp_solve.md:104` confirmed `firm` (rank check). `apply-linop-mutation-rotation.md:344` confirmed `## Status` = `rough-in` (the report's per-step-reference cite). Sister-theme links (`axpby-`, `dot-`) resolve. No broken slug.

**edge-label-fidelity — PASS.** Theme is an L1>L0 edge; the prose, the dep-map row, and the proposed edits all discuss the L1→L0 lowering consistently. The dep-map row flip at `index.md:36` is the same L1>L0 edge.

**plan-kind-consistency — PASS.** Declared kind is a `lowering-verifier` audit producing a firm-promotion verdict; content matches (per-citation re-read, sister-theme cross-check, rank-invariant check, verdict + coupled proposed edits). No rough-in placeholders in a firm-claimed body.

**skill-uptake-survey — WARNING.** The audit re-verified citations entirely by hand via codemap `read_range` and did not invoke `tools/citecheck/citecheck.py` (the mechanical line-map adjudicator) for the load-bearing pinpoints. Had the report run `citecheck --anchor 'SetRestartDim'` on `ksp.cpp:42`, the false-positive drift flag (Issue 1) would have been caught mechanically before it reached the integrator. Telemetry only — not blocking — but directly implicated in the citation-validity failure.

### Issues found

**Issue 1 (HIGH; citation-validity FAIL) — false-positive drift flag that would corrupt a correct citation.** CYCLE.md "Per-citation audit" (lines 88-93) and "Open questions / caveats" (lines 397-407) assert the theme's body-prose citation `palace/linalg/ksp.cpp:42` for the GMRES `SetRestartDim(linear.max_size)` factory line is an off-by-one and the actual line is **:41**, and routes the integrator to "carry-forward-correct `:42`→`:41`". This is WRONG. Codemap `read_range` on `ksp.cpp:39-45` shows: line 39 = `case KrylovSolver::GMRES:`, 40 = `{`, 41 = `auto gmres = std::make_unique<GmresSolver<OperType>>(comm, print);`, **42 = `gmres->SetRestartDim(linear.max_size);`**. The theme's on-disk `:42` (chapter body line 397) is CORRECT; the report's audit is the one off-by-one. Applying the proposed correction would INJECT an off-by-one into a currently-correct citation. This is exactly the cycle-024 `nleps.cpp:810-811` false-drift pattern the friction-ledger `producer-citation-drift-verify-not-self-invoked` entry warns about — an unconfirmed hand-asserted off-by-one. The report is also internally inconsistent: its own per-citation section reads "41" while the theme reads "42"; ground truth is 42. The drift flag and the integrator carry-forward instruction must both be dropped (no edit to the theme's `:42`).

**Issue 2 (LOW; informational, not a defect in this report) — pre-existing YAML parse defect at theme line 802 is real and correctly flagged.** Confirmed by `yaml.safe_load`: the existing `note: case MINRES: case BICGSTAB: case DEFAULT: MFEM_ABORT(...)` row fails with `ScannerError: mapping values are not allowed here`. The report's integrator-action flag (single-quote the note value) is well-founded and the appended rows themselves parse cleanly. Noted for the integrator; not a fault of this report. (Recorded here only so the downstream repairer/integrator does not mistake the existing-block parse failure for a defect introduced by the proposed appended rows.)

## Repair

### Fixes attempted

- **Finding**: citation-validity FAIL (HIGH) — Issue 1: false-positive drift flag asserting the theme's `ksp.cpp:42` GMRES `SetRestartDim` citation is an off-by-one that should be `:41`, with an integrator carry-forward instruction to correct `:42`→`:41`.
  - **Decision**: repaired
  - **Action**: Re-confirmed via codemap `read_range` on `palace/linalg/ksp.cpp:38-45` that `gmres->SetRestartDim(linear.max_size);` is at **line 42** — the theme's `:42` is line-exact and correct; the report's audit was the off-by-one. Removed the false drift flag and the integrator carry-forward instruction from both sites in CYCLE.md: (1) the "Per-citation audit" Notes block for `ksp.cpp:34-58` (was CYCLE.md lines 88-93), and (2) the "Open questions / caveats" first bullet (was lines 397-407). Both now record that `:42` is correct and that the integrator must NOT touch it. (`reports/.../CYCLE.md` — Per-citation audit + Open questions/caveats.) This is the cycle-024 `nleps.cpp` false-drift pattern (friction-ledger `producer-citation-drift-verify-not-self-invoked`); dropping a would-corrupt-a-correct-citation instruction is squarely mechanical/surgical repair authority. The firm-promotion verdict (independently sound per the critic — outer rewrite + per-step cites all verified clean) is preserved unchanged.

- **Finding**: skill-uptake-survey WARNING — a `citecheck --anchor 'SetRestartDim'` run would have mechanically caught the false drift before it reached the integrator.
  - **Decision**: not-needed
  - **Rationale**: Informational telemetry only; not blocking. The underlying defect it implicated (the false drift flag) is fully repaired above, so the warning's content concern is resolved. No edit warranted — leaving the critic's `warning` token intact.

- **Finding**: Issue 2 (LOW; informational) — pre-existing unquoted-mid-string-colon YAML defect at the theme's on-disk line 802 (`case MINRES: ...`).
  - **Decision**: not-needed (left for integrator)
  - **Rationale**: Real but PRE-EXISTING (cycle-007 row), not introduced by this report, and the defect lives in the artifact (`book/src/L1-L0/ksp-solve-mutation-rotation.md`) which is out of repairer write-scope. The report already carries a well-founded integrator-action flag to single-quote the note value; not trivially fixable from within the report, so not expanded into repair scope per instructions. Integrator should single-quote that note value when applying the firm-promotion edits.

### Unrepairable findings

None. The sole blocking finding (citation-validity Issue 1) was mechanically repairable — it was a removal of a false instruction, requiring no substantive authoring. Verdict preserved intact.

## Suggested resolution

`ready`. The false-positive drift flag and its integrator carry-forward instruction have been removed; the theme's correct `:42` citation is now protected. Notes for the integrator:
1. **Do NOT apply any `:42`→`:41` correction** to `book/src/L1-L0/ksp-solve-mutation-rotation.md` — the theme's `:42` is line-exact (codemap-confirmed `SetRestartDim` at ksp.cpp:42).
2. When applying the firm-promotion edits (Status flip + appended `verified_against:` rows + index dep-map row flip), **single-quote the pre-existing note value at theme line 802** (`case MINRES: case BICGSTAB: case DEFAULT: MFEM_ABORT(...)`) so the YAML block parses — a bounded, evidenced make-machine-readable fix the report already flags. The 10 appended rows themselves parse cleanly.
