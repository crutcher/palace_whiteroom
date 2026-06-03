---
verifies: ../REPORT.md
critiqued_at: 2026-06-03T05:10:00Z
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
repaired_at: 2026-06-03T05:40:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of cycle-074 D2 capacitance output-product feature column

## Critique

This report is a **feature-surface composition-root** of the output-product sub-kind (a leaf feature column). The four feature-surface adaptations (surface-or-evidence reframed to driver-range + down-links; rotation-quality no-op; variant-axis-coverage no-op; cross-reference-integrity load-bearing) were applied throughout.

### Checks run

**citation-validity — pass.** I independently hand-Read `reference/palace/palace/drivers/electrostaticsolver.cpp:1-145` and re-verified every load-bearing L0 anchor with brace-boundary discipline (not relying on the agent's reported `--anchor` corrections). All confirmed in-range and meaning-correct: `:95` is the `PostprocessTerminals(post_op, laplace_op.GetSources(), V)` call site; `:100` is the def; `:111` is `mfem::DenseMatrix C(V.size()), Cm(V.size())`; `:118` is `M_elec->Mult(V_gf, D_gf)` and `:119` is the diagonal `linalg::Dot` → `Cᵢᵢ`; `:123` is `for (int j = i + 1; ...)`; `:126` is the off-diagonal `C(i,j) = linalg::Dot`; `:132-134` is the lower-triangle mirror loop (132 `for (int j = 0; j < i; j++)`, 134 `C(i,j) = C(j,i)`); `:139-140` is `mfem::DenseMatrix Cinv(C); Cinv.Invert()`; `:21-22` Solve signature + `:97` return all check out. The energy comment range `:105-110` cited in capacitance.L0 §2 (COMSOL manual p.97) is exact. The composition citecheck claim (L4 9/9, L1 7/7, L0 5/5) is consistent with my sample. One sub-anchor imprecision (non-blocking, recorded as issue 1 below): capacitance.L4:36 cites the `gram_reduce` capacitance specialization as "witness 1, named at `book/src/L4/gram_reduce.md:167-171`" — line `:167-171` is the §Specialization "Electrostatic capacitance" bullet, which DOES describe the `gram_reduce M_elec V (\i j -> 1)` capacitance specialization, but the literal label "positive witness 1" lives at `gram_reduce.md:255`. The cited range supports the substantive claim (the capacitance specialization is described there); only the "witness 1" phrasing is anchored to the wrong line. No `verified_against:` block is present (not a lowering-verifier audit), so that sub-check is N/A.

**surface-or-evidence (adapted) — pass.** Per the feature-surface adaptation, the composition-root's evidence is the L0 driver range + constituent down-links, not a single decomposed op's site. All three chapters cite the `electrostaticsolver.cpp:100-140` (`PostprocessTerminals`) driver range AND down-link to real constituents (`electrostatic.{L4,L1}`, `gram_reduce`, `matrix-weighted-norm`, `bilinear-form` — all on disk). The composition is supported; no new per-op algebraic claim is made (the chapters explicitly defer per-op algebra to the linked constituents). Pass.

**rotation-quality (adapted) — pass (not applicable).** A feature chapter rotates nothing — it recomposes already-firm-track vocabulary outward. The chapters correctly make no rotation claim of their own. No-op pass per the kind adaptation.

**variant-axis-coverage (adapted) — pass (not applicable).** No variant axes of its own; the normalization-weight axis lives in `gram_reduce` (and is correctly described as such — `w = 1` voltage vs `w = 1/(IᵢIⱼ)` current, the two specializations named as living on `gram_reduce`'s axis). No-op pass per the kind adaptation.

**cross-reference-integrity (load-bearing for this kind) — warning.** This is the load-bearing check for a composition root, and it is where the only real risk sits. (1) **capacitance live links all resolve**: `electrostatic.L4`/`electrostatic.L1`/`magnetostatic.L4`, `../L4/gram_reduce.md`, `../L1/matrix-weighted-norm.md`, `../L1/bilinear-form.md`, `../L1/fe_assemble.md`, `../L1/ksp_solve.md`, `../L4/solve_family.md`, `../L4/frequency_sweep.md`, `../L4/fold_solve.md` — all verified on disk. (2) **`inductance.*` references are dangling at apply-time**: capacitance.L4:36 carries a live link `[inductance.L4](./inductance.L4.md)`, and the index/SUMMARY blocks reference all three `inductance.{L4,L1,L0}.md` — none of which exist on disk (D3 has not landed). The report DOES carry an explicit "Integrator dependency note" with an ordering instruction (apply D3 first) and a concrete fallback (omit the 3 inductance SUMMARY rows; defang the index inductance row to plain text). This is the correct defensive shape, BUT the fallback is incomplete: it does not mention the live `[inductance.L4](./inductance.L4.md)` link buried in the staged `capacitance.L4.md:36` §2 prose — if D3 does not land, that link is itself a hard `linkcheck2` break that the SUMMARY/index fallback does not cover. Recorded as issue 2. (3) **maturity-claim cross-check**: the constituent table claims `gram_reduce` is `rough-in (test-coverage-bounded)` — on-disk `gram_reduce.md:220` confirms exactly that token; `matrix-weighted-norm` and `bilinear-form` rough-in claims are consistent with the column staying `seed`. No maturity overclaim. (4) **`gram_inverse`/`symmetric_from_upper`/`symmetric_matrix` are prose-only** (not live links) — correct, since those slugs have no files. Net: warning, driven solely by the D3-coupling gap in the documented fallback.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (a feature column links DOWN to constituents, it is not a lowering theme). The "L1 vs L4" and "Lifts to" prose discuss the correct same-feature cross-level relationships and the L1>L0 mutation rotation is correctly deferred to the constituent ops' themes (high→low discipline honored). Pass.

**plan-kind-consistency — pass.** Declared kind is feature-surface / composition-root; content shape matches (config inputs, physical-product output, body = composition of `gram_reduce` over the electrostatic family, DOWN-links). `status: seed` is the bare codified token (no `(exemplar)` qualifier), correctly gated behind the rough-in `gram_reduce`, consistent with the batch-22 codification. The within-column ordering is high→low (L4→L1→L0) and the SUMMARY insertion places the cohort after the 5 leaf drivers and before the lifecycle ROOT — both matching the deliberate non-alpha feature-spine convention. Pass.

**skill-uptake-survey — pass.** The report references citecheck `--scan`/`--anchor` use for the L0 anchors (the verify-citation-range mechanical realization). The composition-root shape has no other strongly-implied skill. Telemetry surfaced; non-blocking.

### Issues found

1. **(minor, citation-precision) "witness 1" anchored to specialization bullet, not the witness label** — `staging/capacitance.L4.md:36`. The text "`gram_reduce`'s witness 1, named at `book/src/L4/gram_reduce.md:167-171`" points at the §Specialization "Electrostatic capacitance" bullet (which describes the `w=1` capacitance specialization) rather than the line carrying the literal "positive witness 1" label (`gram_reduce.md:255`). The cited range substantively supports the capacitance-specialization claim; only the "witness 1" phrasing is mis-anchored. Severity: low (cosmetic anchor fix — either re-point to `:255` or rephrase to "the capacitance specialization, `gram_reduce.md:167-171`").

2. **(integration-risk, build-readiness) D3-fallback omits the live `inductance.L4` link inside the staged capacitance.L4 body** — `staging/capacitance.L4.md:36` (§2 prose: `[inductance.L4](./inductance.L4.md)`). The CYCLE.md "Integrator dependency note" fallback covers only the SUMMARY rows and the index matrix row; it does not cover this in-body live link. If D3's `inductance.L4.md` is not on disk when this report is applied, that link is an independent hard `linkcheck2` failure not addressed by the documented fallback. Severity: medium (clean if D3 lands first per the stated apply-order; a real break if the fallback path is taken as written). The fallback should add: "also defang the `[inductance.L4](./inductance.L4.md)` reference in `capacitance.L4.md:36` §2 to plain text." (Alternatively the in-body reference could be plain-text from the start, since it is a forward-reference to a same-cycle sibling that the fallback already treats as possibly-absent.)

3. **(non-blocking, intra-report pinpoint inconsistency) the three staged files pinpoint the same off-diagonal / mirror stages at slightly different sub-ranges** — `capacitance.L1.md:57` & `:35` cite off-diagonal `:122-127`; `capacitance.L0.md:45` (Status) cites off-diagonal `:124-126` and mirror `:130-135`; CYCLE.md supporting-evidence and `capacitance.L0.md:30,32` cite `:123` (off-diag loop) and `:132-134` (mirror). Every one of these is in-range and source-supported (the off-diag block spans 121-129; the mirror block spans 131-137), so this is not a citation-validity failure — but the inconsistent sub-pinpoints across the column's own three files are a tidiness nit a reader could trip on. Severity: low (optional harmonization to a single canonical sub-range per stage).

4. **(observation, not a defect — surfaced by the report itself) status-token drift on the 6 pre-existing feature columns** — the on-disk electrostatic/magnetostatic/driven/transient/eigenmode/lifecycle columns carry `status: seed (exemplar)` while this column uses the codified bare `status: seed`. The report correctly scopes this out (one-column-per-invocation) and files it as OQ #1. No action required of this report; noted so the repairer/integrator does not mistake the bare token here for an error. Severity: informational.

## Repair

### Fixes attempted

- **Finding (critic issue 2, medium — the real risk): D3-fallback omits the live `inductance.L4` link inside the staged `capacitance.L4.md:~36` body.** The CYCLE.md "Integrator dependency note" covered only the SUMMARY rows + index matrix row; the in-body `[inductance.L4](./inductance.L4.md)` link in §2 prose was an uncovered independent `linkcheck2` target under the fallback path.
  - **Decision**: repaired.
  - **Action**: Rewrote `reports/<id>/CYCLE.md` §"Integrator dependency note (READ BEFORE APPLYING)". The note now enumerates ALL THREE D3-dependent references (SUMMARY rows; index matrix row; the in-body `capacitance.L4.md:~36` `[inductance.L4]` link), splits into an explicit HAPPY PATH (D3-before-D2 — all three resolve, the in-body link stays live, no defanging) and a FALLBACK (D3 absent — all three defanged, including a new item 3: defang the in-body `[inductance.L4]` reference to plain-text). Mechanical completion of an existing integrator instruction; the live link is NOT removed (D3 lands same cycle per the plan ordering, which the note now states explicitly).

- **Finding (critic issue 1, minor/cosmetic): "witness 1" anchored to the §Specialization bullet (`gram_reduce.md:167-171`) rather than the literal "positive witness 1" label (`gram_reduce.md:255`).** The cited range substantively supports the capacitance-specialization claim; only the "witness 1" phrasing was mis-anchored.
  - **Decision**: repaired (trivial precise-anchor fix).
  - **Action**: Verified on-disk that `gram_reduce.md:167-171` is the §Specialization "Electrostatic capacitance" bullet and `:255` carries the literal "positive witness 1" label. Edited `staging/capacitance.L4.md:36` and the matching `CYCLE.md` §"Supporting evidence" line: both now cite the §Specialization bullet as the substantive home (`:167-171`) AND point the precise "positive witness 1" label at `:255`. Both anchors are now correct.

- **Finding (critic issue 3, minor/tidiness): the three staged files pinpoint the same off-diagonal / mirror stages at slightly different (all in-range, all source-supported) sub-ranges.**
  - **Decision**: not-needed (acknowledged-cosmetic, not repaired).
  - **Rationale**: Every cited sub-range is in-range and source-supported (critic confirmed: off-diag block 121-129, mirror block 131-137). Harmonizing to a single canonical sub-range per stage requires choosing which sub-range is canonical and rewriting multiple in-body citations across all three staged files — a content-tidiness judgment, not a mechanical surgical fix. No build or correctness impact. Left as-is per the critic's "acknowledge-not-repair unless trivial".

- **Finding (critic issue 4, informational): status-token drift on the 6 pre-existing feature columns.** Not a defect; report correctly scoped it out and filed it as OQ #1. No action; recorded here so the integrator does not mistake the bare codified `status: seed` token in this column for an error.

### Unrepairable findings

None. The two actionable findings (1, 2) were both mechanical/surgical and are repaired; finding 3 is an acknowledged-cosmetic tidiness nit with no build/correctness impact; finding 4 is informational.

## Suggested resolution

`overall_status: ready`. The sole warning (cross-reference-integrity) was a flagged batch-ordering dependency, not a content defect: D3 (inductance) lands BEFORE D2 (this report) in the same cycle per the plan's per-report ordering, so all three `inductance.*` references — SUMMARY rows, index matrix row, and the in-body `capacitance.L4.md:~36` link — resolve on the happy path. The dependency note is now complete and explicit (all three references enumerated; happy-path + fallback both spelled out, fallback now covers the in-body link too). Integrator notes: (a) apply D3 before D2 to take the no-defang happy path; (b) the bare `status: seed` token (no `(exemplar)`) is the codified batch-22 form, not an error; (c) OQ #1 (re-token the 6 pre-existing columns) is correctly deferred.
