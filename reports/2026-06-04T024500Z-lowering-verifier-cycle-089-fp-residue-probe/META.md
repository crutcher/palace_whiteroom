---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T030500Z
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
repaired_at: 2026-06-04T031500Z
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

# META: verification of "Audit matrix-weighted-norm — FP-residue law-confidence probe (cycle-089 D1)"

## Critique

### Checks run

**citation-validity — warning.** Every load-bearing citation was re-read at source and confirmed, EXCEPT one false literal claim repeated in the prose and in the proposed edit, plus one off-by-pinpoint inside a YAML annotation:

- `palace/linalg/operator.cpp:599-619` (read_range, on-disk): confirmed EXACTLY. Real branch `:602 B.Mult(x, Bx); :603 double dot = Dot(comm, Bx, x); ... :606 return std::sqrt(dot);`. Complex branch `:614/:615 B.Mult(x.Real()/x.Imag(), ...); :616 std::complex<double> dot = Dot(comm, Bx, x); ... :618 return std::sqrt(dot.real());`. The `√` pinpoints `:606`/`:618` are correct; the **materialize-before-read** crux (`B.Mult` writes `Bx` at :602 BEFORE `Dot` reads it at :603) is correct — this is the disjoint-accumulator witness and it holds.
- `dot.md:79` (reduction-tree associativity non-law), `:80` (strict-CS-in-FP ULP non-law): confirmed verbatim. `dot.md:100` Status = `firm` modulo recorded FP caveats: confirmed.
- `apply_linop.md:62` (bit-determinism across operator representations), `:63` (FP-linearity-strictness): confirmed verbatim. `apply_linop.md:87` Status = `firm` modulo recorded FP caveats: confirmed.
- `nrm2.md:38` ("the square root itself is a deterministic IEEE-754 operation (correctly rounded), so `nrm2`'s non-determinism is **entirely** the `dot`'s"), `:60` strict-CS, `:61` bit-determinism: confirmed verbatim; nrm2 Status = `firm`. The dispositive precedent is real and exactly as quoted.
- `matrix-weighted-norm.md:43` ("The outer `sqrt` is deterministic IEEE-754"), `:69`/`:70` (the two FP sub-claims under probe): confirmed verbatim.

The single substantive citation defect: the report asserts **"the corpus has ZERO `Norml2` references in `test/unit/`"** (Summary L175 of the edit, Open-questions L248, Applicability L141 by implication). This is **literally false** — `grep -rn Norml2 reference/palace/test/unit/` returns **7 hits**: `test-orthog.cpp:191,206` (the **2-arg unweighted** `linalg::Norml2(comm, x)`), `test-vector.cpp:210`, `test-strattonchu.cpp:59,90`, `test-2d-submesh.cpp:225,226` (the `mfem::Vector::Norml2()` **method** form). I read `test-orthog.cpp:185-208` and confirmed those two are the unweighted overload, not the SPD-weighted `Norml2(comm, x, B, Bx)`. So the report's UNDERLYING claim — that the **4-arg SPD-weighted overload** (gate (a)'s exact entry point) is untested — is CORRECT, but the phrasing "ZERO `Norml2` references" overstates it. The correct statement is "ZERO references to the SPD-weighted 4-arg overload `Norml2(comm,x,B,Bx)` in `test/unit/`" (the unweighted/method forms are exercised but are a different operator, `nrm2`). This is a precision defect that lands in artifact-bound prose (the proposed edit-1 text), so it is repair-worthy.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (it modifies `matrix-weighted-norm.md` §Status prose AND appends a `verified_against:` block) framed as retroactive evidence backfill discharging the FP residue — the allowed shape. The crux the task flagged (does the EXTRA `apply_linop` matvec change the FP story vs. `nrm2`?) holds up under scrutiny: the inheritance argument is a legitimate composition, not a gloss. The source ordering `B.Mult(x, Bx)` (:602) fully materializes `Bx` BEFORE `Dot(comm, Bx, x)` (:603) reads it, so the two FP error sources are (i) the rounding in `Bx` (apply_linop's caveat) and (ii) the reduction-order non-associativity of the dot over an already-fixed `Bx` (dot's caveat) — additive across disjoint buffers, with NO shared accumulator coupling them into an emergent third term. The deterministic, correctly-rounded, monotone outer `√` preserves (does not create) divergence. The `nrm2` precedent is genuinely analogous: `nrm2 = √(dot(x,x))` inherits dot's two non-laws while firm; `matrix-weighted-norm = √(dot(Bx,x))` adds exactly `apply_linop`'s caveats on the mapped operand. One subtlety I checked: in matrix-weighted-norm the two dot operands (`Bx`, `x`) are correlated (Bx derives from x), where nrm2's are identical — but that correlation is mathematical, not an FP-accumulator coupling; the dot still sums `conj(Bx[i])·x[i]` over a fixed rounded `Bx` in some tree order, producing no new error term. No surface-or-evidence gap. (Record-definition sub-check: not applicable — no new record named in a signature; `Bx` is an existing workspace, not a record introduced here.)

**rotation-quality — pass (not applicable).** This is an L1-verb law-confidence probe, not a lowering rotation between layers. No algebraic/structural rotation is asserted; the probe argues FP-caveat inheritance within L1. No rotation to grade.

**variant-axis-coverage — pass.** The probe is scoped strictly to the two FP sub-claims (`:69-70`); the verb's variant axes (element-type real|complex; output-arg vs return-value) are already covered in the existing chapter and are explicitly out of this probe's scope (Open-questions L263-266). The FP argument covers BOTH the real (`:602-606`) and complex (`:614-618`) L0 specializations — the complex branch's split `B.Mult(Real)/B.Mult(Imag)` is the same materialize-before-read pattern. No hidden branch.

**cross-reference-integrity — pass.** All cross-references resolve: `dot.md`, `apply_linop.md`, `nrm2.md`, `matrix-weighted-norm.md` all exist with the cited content; `operator.cpp` lines confirmed on-disk. The proposed edits touch `matrix-weighted-norm.md` ONLY (no cascade) — consistent with the firm-token-unchanged constraint. Not a feature-surface chapter; the standard check applies and passes.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; this is a same-layer (L1) verb audit. Directionality is correctly marked "not applicable" by the report (L261-262).

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit/probe with verdict DISCHARGE; content matches. CRITICALLY confirmed per the task: the proposed-changes does NOT flip the `## Status` token (stays `rough-in (test-coverage-bounded)` — the edit-1 replacement text explicitly retains it and names gate (a) as the sole remaining driver), and touches `matrix-weighted-norm.md` ONLY (no cascade). The second `verified_against:` YAML block **round-trips**: I extracted the appended block and ran `yaml.safe_load` → PARSE OK, 6 entries; no `note:` value begins with a quote character of either kind (the round-trip sub-check passes). The firm-flip + cascade is correctly deferred to a recommended batch-29 LEAD, not enacted here.

**skill-uptake-survey — pass.** The report references `citecheck --anchor` for the operator.cpp pinpoints and the `python3 -c "import yaml..."` round-trip for the YAML block (L188-189) — appropriate tooling uptake for a citation-heavy probe. No missing-skill signal.

### Issues found

1. **citation-validity (substantive, repair-worthy)** — `CYCLE.md` Summary/proposed edit-1 (L175 of the embedded edit) + Open-questions L248: the claim **"the corpus has ZERO `Norml2` references in `test/unit/` (verified cycle-088)"** is literally false. `grep -rn Norml2 reference/palace/test/unit/` returns 7 hits (`test-orthog.cpp:191,206` = unweighted 2-arg `linalg::Norml2(comm,x)`; `test-vector.cpp:210`, `test-strattonchu.cpp:59,90`, `test-2d-submesh.cpp:225,226` = `mfem::Vector::Norml2()` method form). The report's intended claim — that the **4-arg SPD-weighted overload `Norml2(comm,x,B,Bx)`** (gate (a)'s entry point) is untested — IS correct (none of the 7 hits is the weighted overload; verified by reading `test-orthog.cpp:185-208`). The defect is precision: the phrasing must be narrowed to "ZERO references to the SPD-weighted 4-arg overload `Norml2(comm,x,B,Bx)`" wherever it appears (edit-1 artifact prose AND the Open-questions recommendation), since the bare "ZERO Norml2 references" would mislead a future firm-flip-wave planner who greps and finds 7. Severity: medium (lands in artifact-bound prose; the underlying disposition is unaffected).

2. **citation-validity (minor, YAML annotation)** — `CYCLE.md` edit-2 YAML note for `palace/linalg/operator.cpp:599-619` (L225): "the radicand dot=Dot(comm,Bx,x) at :603/:614". The complex-branch `Dot` is at **:616**, not :614 (:614/:615 are the two `B.Mult` calls; :616 is `std::complex<double> dot = Dot(comm, Bx, x)`). The real-branch :603 is correct. The load-bearing pinpoints (√ at :606/:618; materialize-before-read at :602-603) are all correct, so this is cosmetic, but the :614→:616 fix tightens the annotation. Severity: low.

### Disposition

The DISCHARGE verdict and the inheritance-argument crux are sound — the extra `apply_linop` matvec does NOT introduce a composition-specific FP property (disjoint accumulators witnessed in source at :602-603; deterministic monotone √; `nrm2` precedent genuinely analogous). The status-token / no-cascade / YAML-round-trip constraints are all satisfied. The only defects are two citation-precision issues (one substantive false "ZERO references" overstatement that lands in artifact prose, one cosmetic :614→:616 pinpoint in a YAML note), both surgically repairable without touching the disposition. Leaving `overall_status` for the repairer.

## Repair

### Fixes attempted

- **Finding 1 (citation-validity, substantive/medium)**: artifact-bound edit-1 §Status prose claimed "the corpus has ZERO `Norml2` references in `test/unit/`" — literally false (grep returns 7 hits).
  - **Decision**: repaired.
  - **Action**: Verified independently — `grep -rn Norml2 reference/palace/test/unit/` returns 7 hits, all the **unweighted 2-arg** `linalg::Norml2(comm,x)` (`test-orthog.cpp:191,206`) or the `mfem::Vector::Norml2()` **method** form (`test-vector.cpp:210`, `test-strattonchu.cpp:59,90`, `test-2d-submesh.cpp:225,226`); the **4-arg SPD-weighted overload** `Norml2(comm,x,B,Bx)` (operator.cpp:599-619, read on-disk) has NO test call. Narrowed the claim in BOTH locations it lands: (a) the edit-1 artifact-bound §Status prose (`CYCLE.md` proposed-changes block) — now reads "ZERO references to the **SPD-weighted 4-arg overload** `Norml2(comm,x,B,Bx)`" naming the unweighted/method forms as a different operator; (b) the Open-questions firm-flip-wave recommendation — same narrowing so a future planner who greps and finds 7 is not misled. Bumped the verification provenance `cycle-088`→`cycle-089` (re-verified here).
- **Finding 2 (citation-validity, minor/low)**: edit-2 `verified_against:` YAML note pinpointed the complex-branch `Dot` at `:614`.
  - **Decision**: repaired.
  - **Action**: Read `operator.cpp:599-619` on-disk. The complex-branch radicand `std::complex<double> dot = Dot(comm, Bx, x)` is at **:615** (`:613`/`:614` are the two `B.Mult(x.Real/Imag, ...)` calls). Note: the critic wrote `:616`, but the on-disk read confirms `:615` (the doubled `palace/palace/linalg/` path; the assert is at :616). Fixed `:603/:614` → `:603/:615` in the edit-2 YAML note. Re-validated the YAML block with `yaml.safe_load` → PARSE OK. The load-bearing pinpoints (√ at :606/:618, materialize-before-read at :602-603) were already correct and untouched.

### Unrepairable findings

None. Both findings were citation-precision fixes inside the proposed-changes blocks; neither touched the DISCHARGE disposition, the `## Status` token, or the deferred cascade.

## Suggested resolution

`ready`. Both citation-precision defects repaired surgically in the `CYCLE.md` proposed-changes blocks; the DISCHARGE verdict, the unchanged `rough-in (test-coverage-bounded)` token, and the no-cascade constraint are all preserved. Integrator note: the edit-1 narrowed phrasing ("SPD-weighted 4-arg overload") is the load-bearing precision fix that lands in artifact prose — apply as-is.
