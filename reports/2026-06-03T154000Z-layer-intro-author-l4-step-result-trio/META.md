---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T161500Z
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
repaired_at: 2026-06-03T163000Z
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

# META: verification of "concepts/ record-definition trio (step-outputs, prev-carry, solve-result)"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` on the full report: **19 ok, 0 failing** (the report itself claims 16 pinpoints; the scan counts the supporting-evidence-section citations too — no inconsistency, just a different denominator). Bounds + path-hygiene clean on all 19. The two key anchors the report flags as verified both confirm mechanically: `palace/linalg/iterative.hpp:52-55 --anchor 'final_res'` → `[ok]` at line 54; `palace/linalg/iterative.cpp:21-31 --anchor 'CheckDot'` → `[ok]` at lines 22, 28. I also confirmed `iterative.cpp:484 --anchor 'final_res'` (PCG statistic write), `iterative.cpp:642/644` (GMRES LS residual + convergence test), and `iterative.hpp:53-55` (the `converged`/`initial_res`/`final_res`/`final_it` mutable statistics fields) all back the prose. **One sub-line drift found** (see Issues): the `iterative.cpp:395-396` range is asserted to hold `res = std::sqrt(std::abs(beta))`, but `--anchor 'res'` lands at line **397, +1 outside the range** (the `beta = (Br,r)` half of the same claim IS in-range at 395-396). The `--scan` passes because the bare range is in-bounds; only the specific anchor-attribution drifts. Marked `warning` rather than `fail` because the load-bearing anchors verify and the drift is a one-line range tightening, but it recurs in three sites so it is a real finding.

**surface-or-evidence (record-definition sub-check) — pass.** This dispatch's entire purpose is the record-definition obligation (directive-2), so the sub-check is the central check here. Each page defines its record IN ITSELF: `step-outputs.md`, `prev-carry.md`, and `solve-result.md` each carry a `## Record definition` section with a TS brace form + a `field : type — meaning + stratum [+ optionality]` table + a `## L0 source home` + `## Distinct from neighbouring records`. They define data shape, not operator algebra (the algebra is cross-linked to `krylov-step` / `derived-view-hoisting` / `first-iteration-unrolling`, not restated). The `solve-result.md` effect-vs-record disambiguation is handled correctly: it cross-links the `Solve a = StateT SimState Identity a` **effect** to `solve-monad.md` (verified that page owns the effect at `solve-monad.md:8` and the in-monad/out-of-monad rule of thumb at `:35`) and defines only the **record fields** itself — it does not restate the threading discipline. The dedicated `## Distinct from the Solve monad` section makes the overload explicit. Each page also lists the signatures that name the record, matching `krylov-step.md` Form A/Form B (verified `krylov-step.md:24-42` carry exactly the `Solve { sim, krylov, outputs[, carry] }` shapes the pages cite).

**rotation-quality — pass.** Not applicable to this report-kind: these are record-definition concept pages (data-shape pages), not refinement proposals asserting an L_{n+1}→L_n rotation. No rotation claim is made (the pages explicitly defer the rotation that *produces* `PrevCarry` to `first-iteration-unrolling`). No-op.

**variant-axis-coverage — pass.** The records' variant axes (CG vs GMRES/FGMRES presence of `ls_residual`; CG `beta_prev` vs GMRES `H_prev` carry; Form A vs Form B presence of `carry`) are each explicitly covered: `ls_residual` optionality is scoped "present only for restarted-LS Krylov methods (GMRES, FGMRES); absent for CG/Chebyshev"; `breakdown_token` scoped to breakdown-guarding kernels; the `carry` field is marked "Form B only". No hidden branches.

**cross-reference-integrity — pass.** All external cross-link targets resolve on disk: `state-stratification.md`, `solve-monad.md`, `first-iteration-unrolling.md`, `derived-view-hoisting.md`, `rotation.md`, `plane-rotation-stream.md`, `solver-as-operator.md`, `tensor-field-lift.md`, and `L4/krylov-step.md` all exist. The three new files are not yet on disk (expected — they are the proposed-changes payload; their mutual cross-links resolve once applied). All six `[old]` anchor blocks (3 in `index.md`, 3 in `SUMMARY.md`) match the on-disk text exactly, and the three alpha-positions are correct: `prev-carry` between `plane-rotation-stream`/`rotation` (index L94-95, SUMMARY L321-322), `solve-result` between `solve-monad`/`solver-as-operator` (index L101-102, SUMMARY L328-329), `step-outputs` between `state-stratification`/`tensor-field-lift` (index L103-104, SUMMARY L330-331). Verified the `record` Kind value is genuinely ABSENT from the `index.md` §"Kind values" legend (lines 56-61 list only methodology/algorithm/primitive/layer-pattern/auxiliary) — so the report's decision to use `record` without re-authoring the legend, and to flag the D1 legend dependency, is correct: the row inserts will reference a Kind value whose legend line lands via D1 (or integrator backfill). This is a coordination dependency the report flags, not a defect.

**edge-label-fidelity — pass.** No lowering edge label is carried (these are concept pages, not lowering themes). The L0-source-home sections narrate L4-record ↔ L0-C++-site backing, and the prose discusses exactly those sites. No-op / pass.

**plan-kind-consistency — pass.** Content shape matches the declared kind (record-definition concept pages, directive-2 cross-cutting ≥2-consumer tier). The ≥2-consumer bar holds for each: `StepOutputs` named by `krylov-step` + `solve-result` (+ consumed by `solve-monad` Outcome classifier); `PrevCarry` named by `krylov-step` Form B `first_step`/`steady_step` + `first-iteration-unrolling` + `solve-result`; the `Solve{...}` result record named by `krylov-step` Form A + Form B. All three clear the cross-cutting bar. Status tokens are `firm` and justified by positive citations (`StepOutputs`/`solve-result`) or stated-and-cited negative-anchoring (`PrevCarry` — Palace does not unroll, the carry is a reified rotation artifact); the lone open sub-part (`BreakdownTag` enum) is correctly noted without downgrading the record shape. Consistent.

**skill-uptake-survey — pass.** The report references `citecheck --scan` / `--anchor` (the verify-citation-range mechanical realization) — the relevant skill for a citation-heavy record-definition dispatch. Telemetry present.

### Issues found

1. **(citation-validity, warning) Sub-line anchor drift on `iterative.cpp:395-396` → `res` attribution.** The `res = std::sqrt(std::abs(beta))` quantity attributed to range `395-396` actually sits at **line 397** (`--anchor 'res'` reports `+1 outside range 395-396`, suggested `395-397`). The `beta = (Br,r)` half of the claim IS in-range (395, 396). This recurs in three sites:
   - `CYCLE.md` §"New file: step-outputs.md" → `## L0 source home`, `residual_norm` bullet: "computes `res = std::sqrt(std::abs(beta))` from `beta = (Br, r)` each step (`palace/linalg/iterative.cpp:395-396`)".
   - `CYCLE.md` §"New file: solve-result.md" → `## L0 source home`, `outputs` bullet: "`res = √|beta|` at `iterative.cpp:395-396`".
   - `CYCLE.md` §"Supporting evidence" → "`palace/linalg/iterative.cpp:395-396` — PCG residual `res = √|beta|`, `beta = (Br,r)`".
   Repair is a one-line range widening to `395-397` (covers both `beta` and `res`) wherever the `res` quantity is the cited fact. Severity: low — the citation is in-bounds and the verb-level claim is true of the cited locality; only the exact line attribution of `res` is off by one. (The bare `--scan` passes; this surfaces only under `--anchor 'res'`.)

### Notes (non-blocking, not defects)

- The three new files (`step-outputs.md`, `prev-carry.md`, `solve-result.md`) are NOT yet on disk despite the report prose "Full content is on disk". This is normal for the dispatch phase (the content lives in the proposed-changes `file:` blocks for the integrator to apply); noting only so the integrator does not expect to find them pre-applied. Not a critic defect.
- `prev-carry.md` generalizes `state-stratification.md`'s "fourth stratum" (authored there for the Chebyshev scalar-recurrence) to the CG/GMRES recurrence carry. This is a faithful extension — `state-stratification.md:63`'s criterion ("threaded across an inner loop but reborn at each top-level call") covers it — not an overreach. Mentioned for the integrator's awareness, not flagged.

## Repair

### Fixes attempted

- **Finding**: (citation-validity, warning) Sub-line anchor drift on `iterative.cpp:395-396` → `res` attribution; `res = std::sqrt(std::abs(beta))` is at line 397, +1 outside the cited range. Recurs in 3 sites.
- **Decision**: repaired
- **Action**: Verified on-disk via `palace-codemap read_range` lines 393-399: line 395 = `beta = linalg::Dot(comm, z, r);`, line 396 = `CheckDot(beta, ...);`, line 397 = `res = std::sqrt(std::abs(beta));`. Widened the cited range `395-396` → `395-397` (covers both the `beta = (Br,r)` half and the `res = √|beta|` half) at all three sites in `CYCLE.md`:
  - §"New file: step-outputs.md" → `## L0 source home`, `residual_norm` bullet.
  - §"New file: solve-result.md" → `## L0 source home`, `outputs` bullet.
  - §"Supporting evidence" list, PCG-residual line.
  Left the breakdown-token / `CheckDot` anchor `iterative.cpp:396` untouched — that anchor correctly points at the guard site (line 396), which is in-bounds and verified, not at `res`.

### Unrepairable findings

None. The single warning was a mechanical sub-line range widening within repair authority.

## Suggested resolution

`ready`. The lone citation-validity warning is repaired (one-line range widening verified on-disk). Notes for the integrator:
- The three concept pages are NOT yet on disk; they land from the proposed-changes `file:` blocks (confirmed absent — no dispatch-phase artifact leak to revert).
- The `record` Kind-legend dependency on the parallel D1 dispatch (flagged in the report's Open questions) is a real coordination item: if D1's `record` legend line does not land this cycle, the integrator should add the one-line legend entry itself before/alongside applying these three `record`-Kind rows. Not a blocking defect for this report.
