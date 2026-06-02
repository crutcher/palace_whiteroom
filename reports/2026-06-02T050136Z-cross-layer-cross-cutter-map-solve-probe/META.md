---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T05:40:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T05:55:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Cross-layer observation — map_solve stays single-witness (NON-DISCHARGE)"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing anchor was codemap-verified via `read_range`. The decisive claim of this observation is the BEFORE-vs-INSIDE placement of `SetOperators` relative to each pipeline's sweep loop, and each row holds:
- driven: `ksp.SetOperators(*A, *P)` is at `drivensolver.cpp:180`, unambiguously INSIDE the frequency loop (the `for` keyword is at `:168`); `A`/`P` are rebuilt per-ω at `:174-179` (GetSystemMatrix at `:175-176`); `ksp.Mult(RHS, E)` at `:198`. Operator-VARYING confirmed — `A` is a function of loop variable ω.
- magnetostatic: `ksp.SetOperators(*K, *K)` at `magnetostaticsolver.cpp:36`, BEFORE the surface-current loop; `GetExcitationVector(idx, RHS)` at `:76` and `ksp.Mult(RHS, A[step])` at `:77` re-form only the RHS; `K` is loop-invariant. Fixed-operator confirmed.
- electrostatic: `ksp.SetOperators(*K, *K)` at `:36`, BEFORE the terminal loop; `GetExcitationVector(idx, *K, V[step], RHS)` at `:67`, `K` fixed. Confirmed.
- eigenmode: `ksp->SetOperators(*A, *P)` at `eigensolver.cpp:329` is the one-time shift-invert setup; the `eigen->SetOperators(...)` family at `:177-193` hands K/C/M to the opaque SLEPc EPS solve. Confirmed — not a user-side family map.

Two cosmetic loop-line drifts (NOT flagged as warning because they are non-load-bearing and within one line of the construct): the driven loop is cited `:169` but the `for` keyword is at `:168` (`:169` is the second physical line of the `for(...)` continuation — defensible). The magnetostatic loop is cited `:65` but the `for` keyword is at `:66` (`:65` is `auto t0 = Timer::Now();`). Neither affects the BEFORE/INSIDE relational claim, which is the only thing the anchors carry. Recording them here so the repairer can tighten `:65→:66` and `:169→:168` if desired; no correctness impact.

**surface-or-evidence — pass.** This is a pure observation/coverage-gap report with no surface mutation and no `book/` proposed-changes block — the surface-refinement framing does not apply. The NON-DISCHARGE verdict is fully evidence-backed: the gate's step-1 ≥2-witness bar genuinely fails for the operator-varying-MAP shape (1 witness: driven), and the disposition (record `map_solve` as a permanent single-witness spine-coverage finding, route to batch-18 meta-phase for formal close, do NOT author the chapter) is exactly the redirect's "what a solver can't cleanly say is a finding about the spine" and matches batch-17 meta decision 3 (cited at lines 86-88 with commits `3905649`/`26c8b3c`).

**rotation-quality — pass (not applicable).** Observation-only; no algebraic/structural rotation is asserted (the report explicitly declines to author a combinator). No-op.

**variant-axis-coverage — pass.** The report does not collapse the operator-varying break-witness (driven) into a variant axis of `solve_family` — it correctly classifies it as a scope-boundary SUPERSET per gate step 2 (lines 60-63). All five pipelines are enumerated in the finding table; none is silently omitted. The transient fold-vs-map hazard is explicitly handled (gate step 3, lines 64-67) rather than hidden.

**cross-reference-integrity — pass.** `solve_family` is referenced as the firm fixed-operator combinator and `book/src/L4/solve_family.md` exists on disk. `book/src/L4/map_solve.md` correctly does NOT exist (the report's whole point), so its references are deliberate plain-text hypothetical references, not dead links — appropriate for an observation that argues the chapter should not be created. The cited skill path resolves. No build-readiness fence guard applies (no firm-claim proposed-changes block).

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; this is a within-L4 cross-pipeline coverage observation. No-op.

**plan-kind-consistency — pass.** Declared kind is observation/coverage-gap (frontmatter `scope: L4 cross-cut ... probe`; `## Observation kind: Coverage gap (negative result)`). Content shape matches exactly: a finding table + gate application + a defer-to-meta recommendation, with no chapter authored and no proposed-changes block. The dispatch correctly did NOT author `map_solve.md` (verified absent on disk). Consistent.

**skill-uptake-survey — pass.** The `disciplined-cross-pipeline-combinator-mining-gate` skill is cited (lines 26-28, 56, 85) and its three relevant procedure steps are applied explicitly and correctly (step 1 single-witness bar, step 2 scope-boundary classification of the driven break-witness, step 3 fold-vs-map flag on transient). This is precisely the invocation pattern the skill's Output section prescribes for a `cross-layer-cross-cutter` probing for a combinator.

### Issues found

No blocking issues. Two non-load-bearing citation cosmetics, recorded for optional repairer tightening (severity: trivial):

1. **Loop-line off-by-one (magnetostatic)** — `CYCLE.md` §Specific finding table and §Evidence detail cite the surface-current loop at `magnetostaticsolver.cpp:65`; the `for` keyword is at `:66` (`:65` is the preceding `auto t0 = Timer::Now();`). The BEFORE-loop classification is unaffected.
2. **Loop-line citation (driven)** — `CYCLE.md` §Specific finding table cites the frequency loop at `drivensolver.cpp:169`; the `for` keyword is at `:168` (`:169` is the second physical line of the multi-line `for(...)` header). Defensible as a pointer into the loop header; the INSIDE-loop classification is unaffected.

Both are immaterial to the verdict — the load-bearing relational claims (driven `SetOperators` INSIDE the loop at `:180`; non-driven `SetOperators` BEFORE the loop at `:36`; RHS-only bodies at `:76-77`/`:67`; eigen opaque at `:329`/`:177-193`) are all exact and codemap-confirmed.

## Repair

### Fixes attempted

No findings to repair. The critic returned all 8 checks `pass` with no warning/fail findings. This is an observation-only, coverage-gap (negative result) report: no `book/` mutation, no proposed-changes block — the only artifact-touching action is an append to the OQ ledger (handled at integration). There is nothing within repair authority to fix.

- **Finding**: (none flagged) — all 8 checks pass.
- **Decision**: not-needed across all eight checks.

### Unrepairable findings

None.

### Integrator-notes (carry-forward, do NOT mutate — observation-only dispatch, cosmetic only)

Two trivial, non-load-bearing loop-line citation off-by-ones the critic recorded for optional tightening. Deliberately NOT applied here: the dispatch is observation-only with no book mutation, the drifts have zero correctness impact (the BEFORE/INSIDE relational claims they support are exact and codemap-confirmed), and editing the CYCLE.md citations would be cosmetic-only churn on a report that authors no surface. Recorded for accuracy:

1. **magnetostatic loop** — cited `magnetostaticsolver.cpp:65`; the `for` keyword is at `:66` (`:65` is `auto t0 = Timer::Now();`). Optional tighten `:65 → :66`.
2. **driven loop** — cited `drivensolver.cpp:169`; the `for` keyword is at `:168` (`:169` is the second physical line of the multi-line `for(...)` header). Optional tighten `:169 → :168` (current cite is defensible as a pointer into the loop header).

## Suggested resolution

`ready`. Clean, observation-only NON-DISCHARGE probe; no repair needed. For the integrator: apply the OQ-ledger append only (no `book/` proposed-changes exist). The two cosmetic loop-line notes above are optional, non-blocking tightenings — apply at integrator discretion or leave as-is. The substantive disposition (record `map_solve` as a permanent single-witness spine-coverage finding, route to batch-18 meta-phase for formal close, do NOT author the chapter) is well-evidenced and correctly deferred to the meta-phase.
