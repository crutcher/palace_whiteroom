---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T001411Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-04T021500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Audit solve_family — firm-on-positive-structure law-confidence pass"

## Critique

### Checks run

**citation-validity — pass.** Spot-verified the load-bearing source citations directly via the
codemap, not by trusting the report's pasted `citecheck` table. `palace/linalg/ksp.cpp:297-310`
(`BaseKspSolver<OperType>::Mult`): line 297 = `void BaseKspSolver<OperType>::Mult(const VecType &x,
VecType &y) const`, body is `ksp->Mult(x, y)` (line 300), a non-convergence warning branch, then
`ksp_mult++` (line 308) and `ksp_mult_it += ksp->GetNumIterations()` (line 309), close-brace line 310
— exactly as asserted, `const`, output-only write to `y`, only cross-call mutation is the two
counters. `ksp.hpp:46` confirms `mutable int ksp_mult, ksp_mult_it;` with the "Counters for number of
calls … cumulative number of iterations" comment. Electrostatic hoist: `KspSolver ksp(...)` line 35,
`ksp.SetOperators(*K, *K)` line 36, both before the `for (... : laplace_op.GetSources())` loop at
line 60; `K = GetStiffnessMatrix()` line 30; `std::vector<Vector> V(n_step)` line 46; `MFEM_VERIFY(n_step
> 0, ...)` line 42; `step++` line 89. Magnetostatic hoist: lines 35/36 outside the
`GetSurfaceCurrentOp()` loop at 66; `std::vector<Vector> A(n_step)` line 47 — structurally identical.
Driven negative witness: `GetSystemMatrix(...)` line 176 and `ksp.SetOperators(*A, *P)` line 180, both
INSIDE the frequency loop. Every load-bearing range confirms exact on-disk; no drift. The
`verified_against:` block round-trips under `yaml.safe_load` (8 entries, all `supports`), and no
`note:` value begins with a quote of either kind — the YAML round-trip sub-check passes.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (modifies an existing operator's
surface: the `## Status` re-narration + frontmatter `firmness:` flip) carrying a rotation/law-confidence
evidence claim (the `verified_against:` block). The surface change AND the evidence are both present.
The record-definition sub-check is satisfied for the records named in the cited signatures: `OpParams`
and the `KspSolver`/`Mult` surface are referenced, not newly introduced here, and have definition homes
in the existing firm L4 vocabulary (`ksp_solve.md`, `book/src/L4/index.md`); no signature-named record
is left described only by use.

**rotation-quality — pass.** The decisive load-bearing check. The promotion rests on the
firm-on-positive-structure / syntactic-identity escape (the c082/c083 route), and the report's
application is sound. I independently confirmed the disambiguation against the c080 contrast: (1) Law 1
(concatenation-homomorphism) is `map`'s definitional list-homomorphism `map f (a++b) = map f a ++ map f
b` — a syntactic identity, no inner-product/positivity axiom smuggled in; (2) Law 2 (`SetOperators`-hoist)
is a literal placement read off positive source (verified `SetOperators` outside the loop in both
fixed-operator sweeps, inside the loop in driven); (3) Law 3 (element-independence) is discharged by the
positive `Mult` body — `const`, output-only write, only cross-call state is two monotone telemetry
counters that never feed back into a solve, so reorder/split/chunk of the RHS family cannot change any
`V[step]`/`A[step]`. By contrast `matrix-weighted-norm` (c080, escape INAPPLICABLE) carries
norm-axiom laws (triangle / Cauchy–Schwarz / parallelogram) that are theorems conditional on SPD/Hermitian
structure the L0 source only numerically asserts via `MFEM_ASSERT(dot.real() > 0...)` — I checked
`matrix-weighted-norm.md` and confirmed this is genuinely the different situation. No theorem-needing-proof
exists in any of `solve_family`'s laws. The escape is correctly applied; this is not a renaming or a
numerically-asserted property masquerading as syntactic.

**variant-axis-coverage — pass.** The operator-capture axis (fixed vs per-element) is explicitly and
correctly scoped: fixed-operator is witnessed by electrostatic + magnetostatic; per-element (driven)
is the documented superset exclusion, not a hidden branch; transient (fold candidate) and eigenmode
(not a witness) are explicitly catalogued as out-of-witness. The collection-shape and outcome axes are
addressed in the entry. No hidden variant branch.

**cross-reference-integrity — warning.** All `[link]` targets resolve on disk (verified `ksp_solve.md`,
`sparameter_reduce.md`, `eigenfreq_qfactor_reduce.md`, `gram_reduce.md`, `fold_solve.md`,
`matrix-weighted-norm.md`, `assemble_frequency_operator.md`, `electrostatic.L4.md`,
`magnetostatic.L4.md`, `solve-family-map-dissolution.md` all present). The OLD block in the §Status
edit matches the on-disk `solve_family.md:144` paragraph byte-for-byte, so the edit will locate cleanly.
The warning is a **build-readiness / proposed-changes well-formedness** concern: the second `edit:` block
(CYCLE.md lines 225–283) ENCLOSES a NESTED ` ```yaml ... ``` ` fence (lines 248–282) using same-length
three-backtick delimiters. A naive ` ``` `-keyed proposed-changes parser closes the OUTER `edit:` block
at the first bare ` ``` ` (line 282), truncating the NEW payload and leaving line 283's ` ``` ` a stray
opener — the cycle-024 nested-`text`/`yaml`-fence-truncation variant
(`convert-nested-fences-to-indented-code-in-proposed-changes-block`). This is NOT the cycle-019
firm-body-outside-fence defect: the full `## Status` re-narration body IS inside the `edit:` block, and
the firm apparatus is enclosed. It is purely the nested-fence delimiter collision. Flagged so the
repairer can apply the nested-fence→indented-code conversion before integration.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is the subject of this report — it is an
intra-L4 law-confidence audit of one operator. The one edge mention (the L4>L3
`solve-family-map-dissolution` theme) is correctly noted as out-of-scope/unaffected, and the prose does
not mis-describe its direction. Not a lowering-edge proposal; no fidelity issue.

**plan-kind-consistency — pass.** Declared kind is an `audit` (lowering-verifier law-confidence pass).
Content shape matches: per-citation audit table, applicability conditions, a FIRM verdict with a
`verified_against:` block, no rough-in placeholders in the promoted content. The promotion to `firm` is
backed by the audit, consistent with the audit kind.

**skill-uptake-survey — pass (telemetry).** The report references `tools/citecheck/citecheck.py
--anchor`/`--scan` (citation no-drift), the direct-`read_range` range-END confirmation per the cycle-066
FE-source-class caveat, and the `python3 yaml.safe_load` `verified_against:` round-trip — all the
skills its shape implies. The nested-fence situation it produces is the one whose REPAIR skill
(`convert-nested-fences-to-indented-code-in-proposed-changes-block`) it does not self-invoke (correctly
— that is repairer-side), surfaced under cross-reference-integrity above.

### Issues found

1. **Nested same-length fence inside the second `edit:` proposed-changes block — `cross-reference-integrity`
   warning, build-readiness.** `reports/.../CYCLE.md` §Proposed changes, the second block (lines
   225–283): the `edit:book/src/L4/solve_family.md` block encloses a nested ` ```yaml ` … ` ``` ` block
   (lines 248–282) with same-length three-backtick delimiters. Fence enumeration: opens 225, nested-yaml
   opens 248, nested-yaml closes 282, outer closes 283. A naive proposed-changes parser truncates the
   outer block at line 282. Severity: medium (a real integration-time truncation risk, fully mechanical
   to repair via the nested-fence→indented-code conversion; the load-bearing content and verdict are
   otherwise sound). Note this is the nested-fence-truncation variant, NOT the firm-body-outside-fence
   defect — the `## Status` body is correctly enclosed.

### Notes (no issue — recorded for the integrator)

- **1-of-2-gates honesty: clean.** The report does NOT claim or schedule an electrostatic/magnetostatic
  column `status: seed` flip. It explicitly states `gram_reduce` (verified on disk as still `rough-in
  (test-coverage-bounded)`, folding the c080-NO-GO-HELD `matrix-weighted-norm`) remains the second
  own-constituent gate, and routes the column weighing to the batch-27 meta-phase. The feature columns
  are confirmed `status: seed` on disk. The honest non-flip is correctly observed, and the D2 hand-off
  instruction even reiterates "D2 must NOT flip either column's `status: seed`."
- **Scope discipline: clean.** The proposed changes touch ONLY `book/src/L4/solve_family.md`
  (frontmatter firmness + §Status re-narration + appended `verified_against:`). Consumer re-anchors
  (`gram_reduce.md`, `electrostatic.L4.md`, `magnetostatic.L4.md`) are explicitly deferred to D2; the
  stale-after-promotion §Evidence/§Provenance lines are flagged in Open questions as a bounded follow-on
  rather than expanded into this edit's blast radius. No feature/consumer file is mutated.

---

## Repair

### Fixes attempted

- **Finding**: Nested same-length ` ```yaml ` fence inside the second `edit:book/src/L4/solve_family.md`
  proposed-changes block (the `verified_against:` block) — a naive ` ``` `-keyed proposed-changes parser
  truncates the OUTER `edit:` block at the first bare inner ` ``` `, stranding the remainder of the NEW
  payload (the cycle-024 nested-fence-truncation variant; `cross-reference-integrity` / build-readiness
  warning).
  - **Decision**: repaired.
  - **Action**: Applied skill `convert-nested-fences-to-indented-code-in-proposed-changes-block` to
    `reports/2026-06-04T013000Z-lowering-verifier-cycle-086-solve-family/CYCLE.md` §Proposed changes,
    second `edit:` block. Converted the nested ` ```yaml … ``` ` `verified_against:` block (formerly
    enclosed by three-backtick delimiters) to CommonMark 4-space-indented-code form: deleted the opening
    ` ```yaml ` line and the matching closing ` ``` ` line, and prefixed every content line of the
    8-entry `verified_against:` block with 4 spaces. The content is preserved byte-for-byte (only the
    delimiter mechanism changed, fence → indent; not a character of the YAML text altered). Re-added the
    outer `edit:` block's closing ` ``` ` fence (which had coincided with the now-removed nested closing
    fence) before the trailing "Note on the §Evidence section:" prose, restoring the block's intended
    boundary. The human-readable `verified_against:` lead-in label (the bare-text line preceding the old
    fence) is retained as-is.
  - **Verification**: Fence enumeration now yields exactly the two paired proposed-changes-block fences
    (`edit:` opens 215 / closes 223; `edit:` opens 225 / closes 281) — `2 × 2 = 4` paired delimiters, no
    stray opener. The remaining two fences (309 / 337) are the §Supporting evidence citecheck table in
    the report narrative, NOT a proposed-changes block. The full §Status firm re-narration body AND the
    indented `verified_against:` content now both sit INSIDE the second `edit:` block (between its open at
    225 and close at 281) — the block parses to its full length, so the integrator applies the complete
    §Status promotion payload + the `verified_against:` evidence. Content (frontmatter firmness flip,
    §Status re-narration, the verified_against entries) untouched — the FIRM verdict and all citations are
    exactly as the producer authored them.

### Unrepairable findings

None. The single warning was the mechanical nested-fence-truncation defect, fully repairable under
repair authority (delimiter re-mechanism, content preserved verbatim). All other 7 checks passed at
critique.

## Suggested resolution

`ready`. The fix is purely mechanical (fence → indented-code re-delimiting; content byte-preserved). The
content verdict — promote `solve_family` `rough-in (test-coverage-bounded)` → `firm` via the
firm-on-positive-structure / syntactic-identity escape (the c082/c083 route) — was independently verified
sound by the critic (rotation-quality pass, the decisive check) and is not touched by this repair. The
integrator may apply the second `edit:` block to its full length; no follow-up agent is required.
