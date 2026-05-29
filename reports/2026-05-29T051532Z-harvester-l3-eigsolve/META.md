---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T054500Z
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
repaired_at: 2026-05-29T055000Z
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

# META: verification of "Formalize eigsolve at L3 — DECISION: BLOCKED (prerequisite-surface inventory)"

## Critique

### Checks run

**citation-validity — pass.** This is a BLOCKED inventory report with no `book/` proposed-changes, so citation-validity reduces to verifying the three anchor-check findings and the precedent contrasts. I independently re-verified every load-bearing pointer:

- *Finding 1 (L1 rough-in, laws `unconfirmed`).* `book/src/L1/eigsolve.md:100` carries the exact "treat all laws as `unconfirmed`" caveat. `:166-169` carries `status: rough-in (test-coverage-bounded, cycle-009; …)` and the two-path promotion gate (dedicated `test-eigensolver.cpp` OR a literature-anchor harvester pass). `book/src/L1/index.md:71` dep-map row reads `rough-in (test-coverage-bounded, harvested-by: harvester:2026-05-27T191929Z-…)` verbatim. The "only dedicated witness is `test-boundarymodeoperator.cpp`" framing matches the entry. Confirmed.
- *Finding 2 (no L2 eigsolve).* `ls book/src/L2/` returns exactly 8 files (`chebyshev-iteration`, `incremental-least-squares`, `index`, `inner_product`, `krylov-step`, `ksp_solve`, `linear_combination`, `orthogonalize`) — no `eigsolve.md`. `book/src/L2/index.md:30-53` lists the 5-firm cohort + 2 stubs (`incremental-least-squares`, `ksp_solve`), no eigsolve row. The "two grep hits for eigen are incidental" claim matches the `linear_combination.md`/`orthogonalize.md` mentions. Confirmed missing.
- *Finding 3 (opaque-library driver, no kernel analog).* Re-read all three source ranges via `read_range`: SLEPc `SlepcEPSSolverBase::Solve()` is `Customize(); EPSSolve(eps); EPSGetConverged(…); RescaleEigenvectors(…); return num_conv;` — `EPSSolve` at `:694`, `EPSGetConverged` at `:695`, `RescaleEigenvectors` at `:707`, `return` at `:708`, and `GetEigenvalue → l * gamma` at `:715`. ARPACK `SolveInternal` is the `while(true){ naupd(…); if(ido==±1)ApplyOp; else if(ido==2)ApplyOpB; else if(ido==99)break; }` RCI loop (`ApplyOp` dispatch `:325`, `ApplyOpB` `:329`, `ido==99` break `:331`), with the `TARGET_REAL`/`TARGET_IMAGINARY` `MFEM_ABORT` present. `ArpackEPSSolver::ApplyOp` (`:563-590`) is exactly `opK->Mult(x1,z1); opInv->Mult(z1,y1); y1 *= 1/gamma;` (non-sinvert) + the sinvert + optional `opProj` branches. The "`ApplyOp` = `apply_linop ▷ ksp_solve` composition of already-firm L3 leaves" reading is faithful. Confirmed.
- *Precedent contrasts.* L3 `ksp_solve.md:5-8` frontmatter shows `lifts_from: book/src/L1/ksp_solve.md` (firm — `L1/index.md:70` row reads `firm`) and `lowers_to: book/src/L2/ksp_solve.md (… NOT identity-in-form)`; `:108` states laws "inherited from `L1/ksp_solve` law 3." OQ `open-questions.md:352` carries the cycle-020 harvester's gating caveat verbatim ("after the L1/L2 eigsolve anchors are checked for firmness"; "only an eigsolve *kernel* … would be a clean identity-backfill candidate"). `priorities.md:31` is plan #9 verbatim. `L3/index.md:41` carries the "`ksp_solve` / `eigsolve` if their rotations turn out to be near-identity" flag. `eigsolve-mutation-rotation.md:235` confirms the `nleps.cpp:514` `QuasiNewtonSolver::Solve` cross-reference the sibling-boundary note relies on. All confirmed.

One **non-load-bearing line-attribution drift**: the body cites the ARPACK `naupd` call at "`:315-316`" (Supporting-evidence) and "`:318`" (Evidence list) and "`:312-330`" (OQ); the actual `naupd(…)` call spans `:317-318`. Every variant lands inside the broader cited window (`:263-358` / `:312-340`) and the structural claim (RCI loop dispatching opaque `naupd`) is exact. No claim is unsupported; flagged below as a minor consistency nit only.

**surface-or-evidence (CRUX) — pass.** This is the load-bearing check. The report's shape is a *blocked-with-prerequisite-surface inventory* (the trsv-style outcome), not a refinement-shaped proposal, so the question is whether the BLOCKED decision is sound — i.e. whether the anchors are *genuinely* insufficient such that forcing an L3 entry would violate the firm-anchor discipline. My independent verification confirms all three blocking grounds hold simultaneously: (1) the L1 anchor is `rough-in` with laws explicitly self-flagged `unconfirmed` — inheriting them into a fresh L3 layer (the ksp_solve precedent inherits from a *firm* L1) would propagate unconfirmed status; (2) there is no L2 `eigsolve` entry, not even a stub, so an L3 entry would have no `lowers_to` target and would either break the high→low lowering-direction discipline or emit a dead in-prose reference; (3) the linear-EVP iteration is opaque-library-owned (SLEPc single `EPSSolve` call; ARPACK RCI dispatching opaque `naupd` callbacks), and the only Palace-authored per-step body (`ApplyOp`) is a composition of *already-firm* L3 leaves — there is no `krylov-step`-shaped eigen-kernel to factor. Each ground is independently sufficient; all three are evidence-backed. The harvester COULD NOT have backfilled a defensible L3 entry: doing so would have forced an unanchored entry against the firm-anchor discipline and the dispatch's own conditional clause. This is a correct "blocked, surface the prerequisite" outcome, not a premature give-up — the report does the localization work, identifies the exact prerequisite chain, and emits two well-formed OQ appends. Pass.

**rotation-quality — pass (not applicable).** No L_{n+1}→L_n rotation is asserted because no L3 entry is authored. The report does make a *forward-looking* rotation prediction (the eventual linear-EVP L3 entry is "most likely a sequential-obstruction / partial-obstruction record, NOT a clean kernel+driver pair") — this is correctly framed as a prediction gated on the prerequisite chain, not an asserted rotation, and it is well-grounded in Finding 3's opaque-library evidence. Nothing to score against the rotation-quality bar in this report.

**variant-axis-coverage — pass.** No operator entry is authored, so there are no variant-axis combinations to cover. The report nonetheless handles the one axis distinction that matters for *scoping*: linear-EVP (SLEPc-EPS / ARPACK-EPS — the named dispatch scope) vs nonlinear-EVP (`QuasiNewtonSolver`, the sibling NLEPS dispatch's scope). The boundary is kept clean throughout (Finding 3 parenthetical, the prerequisite-chain step 3, and the Caveats section all scope to linear-EVP and explicitly hand nonlinear-EVP to the sibling). The "even there, the L1 form absorbs the three orchestrations into one opaque type" note correctly references the L1 entry's collapsed orchestration-pattern axis (`L1/eigsolve.md:155`). No hidden branch.

**cross-reference-integrity — pass.** All internal references resolve: `book/src/L1/eigsolve.md`, `book/src/L1/index.md`, `book/src/L2/index.md`, `book/src/L1-L0/eigsolve-mutation-rotation.md`, `book/src/L3/ksp_solve.md`, `book/src/L3/krylov-step.md`, `book/src/L3/index.md`, `scaffolding/open-questions.md`, `scaffolding/priorities.md` all exist and the cited line content matches. Named slugs (`apply_linop`, `ksp_solve`, `krylov-step` at L3; `eigsolve`, `ksp_solve` at L1) all resolve. The report references *non-existent* targets (`book/src/L2/eigsolve.md`, an L3 `eigsolve.md`) only as the prerequisites it is documenting as missing — these are correctly framed as not-yet-existing, not asserted as live links. No dead reference introduced.

**edge-label-fidelity — pass.** No `L_{n+1}→L_n` edge label is carried (no theme authored). The directional discipline the report *invokes* is correct: it correctly argues the would-be L3 entry needs both a firm L1 to lift from and an L2 to lower to, and that the high→low discipline forbids defining an L3 entry against a non-existent L2 target. The prerequisite chain's directionality (L1 firm → L2 entry → L3) is sound.

**plan-kind-consistency — pass.** The frontmatter declares `decision: BLOCKED (anchors insufficient) — inventory observation, no L3 backfill` and `status: pending`. The content shape matches exactly: an anchor-check inventory + prerequisite chain + two OQ appends, zero `book/` proposed-changes. This is the correct kind for a blocked-localization outcome — not mis-classified as a firm operator or rough-in entry. The two OQs are well-formed (slug, severity tag, citations, explicit trigger, route). Consistent.

**skill-uptake-survey — warning.** The report's shape (citation verification of a blocked anchor-check, plus the trsv-style blocked-prerequisite outcome) implies two relevant skills. The report DOES reference `verify-citation-range` ("self-verified … via `mcp__palace-codemap__read_range` per the `verify-citation-range` producer-self-verification discipline") — good uptake, and the producer-self-verification it claims is borne out by my independent re-check. However, the report does NOT reference `verify-rotation-citation` or `propose-rotation` (arguably n/a here since no rotation is authored), and more notably does not invoke the `verify-citation-range` **"Audit-report / inherited-citation sub-case"** for the precedent citations it inherits from the L1 entry and the cycle-020 ksp_solve report — this is precisely the sub-case (codified cycle-012) meant to catch the kind of inherited narrow-line drift that produced the `naupd :315-316` vs `:317-318` slip. Pure telemetry, non-blocking: uptake is partial (one skill cited, the inherited-citation sub-case not run).

### Issues found

1. **[minor / consistency] `naupd` call-line attribution drifts across the report.** `reports/2026-05-29T051532Z-harvester-l3-eigsolve/CYCLE.md` Supporting-evidence (`:206-207`) cites the ARPACK `naupd` driver call at "`:315-316`"; the Evidence list (`:191`) says "line 318"; the OQ (`:266`) says "`arpack.cpp:312-330`". The actual `naupd(…)` call spans `palace/linalg/arpack.cpp:317-318` (verified via `read_range`). Every variant falls inside the broader cited RCI-loop window and the structural claim is exact, so no claim is unsupported — but the three different narrow line numbers for the same call are internally inconsistent. This is the inherited-narrow-line drift pattern the `verify-citation-range` audit sub-case targets. Severity: minor (cosmetic; non-load-bearing).

2. **[telemetry] inherited-citation sub-case of `verify-citation-range` not invoked.** The report inherits precedent citations from `L1/eigsolve.md` and the cycle-020 ksp_solve report (e.g. the `:108` law-inheritance pointer, the OQ `:352` caveat) without running the cycle-012 inherited-citation audit sub-case on them. All such inherited pointers happen to verify correctly here, so no defect resulted — surfaced as uptake telemetry only, per the skill-uptake-survey check. Severity: telemetry (non-blocking).

3. **[no-op confirmation, not a defect] BLOCKED decision soundness — CONFIRMED, no issue.** Recording explicitly for the repairer/integrator: the crux check passes. The three blocking grounds are each independently verified and independently sufficient; the harvester correctly did NOT force an unanchored L3 entry; the prerequisite chain (L1 firm → L2 entry → THEN L3, likely sequential-obstruction not clean kernel+driver) is sound; the plan-#9 reframe recommendation ("next L3 inventory backfill" → "blocked-pending-L1-firm+L2-entry") is an accurate plan correction grounded in the verified anchors; the linear-EVP vs nonlinear-EVP boundary is kept clean throughout. There is no substantive issue for the repairer to act on beyond the cosmetic line-number reconciliation in issue 1.

## Repair

### Fixes attempted

- **Finding 1** — `naupd` call-line attribution drifts across the report (`:315-316` Supporting-evidence; `:312-330` OQ; the broad-window references are accurate). The actual `naupd(…)` call spans `palace/linalg/arpack.cpp:317-318`.
  - **Decision**: repaired
  - **Action**: Re-verified the call site via `mcp__palace-codemap__read_range` on `palace/linalg/arpack.cpp:310-335` — the `naupd(fcomm, ido, …, ainfo);` call statement spans lines 317–318 (statement begins line 317, continues onto line 318). Reconciled both flagged narrow-line variants in `reports/2026-05-29T051532Z-harvester-l3-eigsolve/CYCLE.md`:
    - §Supporting evidence (line 205): `naupd` driver call `:315-316` → `:317-318`.
    - §Open questions, `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` OQ (line 266): `palace/linalg/arpack.cpp:312-330` → `palace/linalg/arpack.cpp:317-318`, with the RCI-loop window relabelled `:312-340` (the loop body) for clarity.
    - The broad-window references (`:263-358` in inputs + Supporting-evidence; `:312-340` in Finding 3 body line 105) already contain `:317-318` and remain accurate — left intact. The critic's "line 318" mention (Evidence-list) is already consistent with `:317-318`; no stray narrow-`:318` attribution remains (grep-confirmed).

- **Finding 2** — `[telemetry]` inherited-citation sub-case of `verify-citation-range` not invoked.
  - **Decision**: not-needed
  - **Rationale**: Pure skill-uptake telemetry (the `skill-uptake-survey: warning`). All inherited pointers verified correctly; no defect resulted. Telemetry is not a repairable artifact defect — surfaced to the meta-phase via the critic's survey, not the repairer's authority.

- **Finding 3** — `[no-op confirmation]` BLOCKED decision soundness CONFIRMED.
  - **Decision**: not-needed
  - **Rationale**: Explicitly a no-op confirmation, not a defect. The crux `surface-or-evidence` check passes; the three blocking grounds, the prerequisite chain, the plan-#9 reframe, and the linear-EVP/nonlinear-EVP boundary all verified sound by the critic. The two proposed OQ appends are well-formed and route to the meta-phase / integrator — left intact (not the repairer's to author or alter).

### Unrepairable findings

None. The single substantive finding (the cosmetic citation drift) was mechanically repairable; the remaining items are telemetry / no-op confirmation requiring no edit.

## Suggested resolution

`ready`. This is a BLOCKED-with-prerequisite-surface inventory report with NO `book/` proposed-changes — its deliverable is the anchor-check inventory + the prerequisite dispatch chain + two OQ appends. The crux check (BLOCKED decision soundness) passed on all three grounds; the only artifact defect was the cosmetic `naupd` line-ref drift, now reconciled to `:317-318`.

Notes for the integrator:
- **No `book/` changes to apply.** Do not materialize an L3 `eigsolve` stub from this report — the report's whole point is that the L3 backfill is blocked on missing L1-firm + L2-entry anchors; a stub would have no `lowers_to` target and would lift `unconfirmed` laws.
- **Promote the two OQs** to `scaffolding/open-questions.md`: `l3-eigsolve-blocked-on-l1-firm-and-l2-entry` (HIGH-fan-out-blocker) and `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` (structural).
- **Plan-#9 reframe** (`priorities.md:31`): the first OQ recommends the meta-phase reframe plan #9 from "next L3 inventory backfill" → "blocked-pending-L1-firm+L2-entry." That is a meta-phase action (plan co-ownership), surfaced via the OQ — not for the integrator to enact directly.
