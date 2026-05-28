---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T23:55:00Z
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
repaired_at: 2026-05-28T00:00:00Z
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
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of L1>L0 theme sketch — eigsolve-mutation-rotation

## Critique

### Checks run

**citation-validity (warning)** — Spot-checked 6 of the 23+ cited L0 ranges via `mcp__palace-codemap__read_range`. The 10 `opInv->Mult` callsites are exact and exhaustively-enumerated: `mcp__palace-codemap__search_text` for `opInv->Mult` returns exactly the 10 lines `arpack.cpp:574, 580, 761, 778`, `nleps.cpp:514`, `slepc.cpp:1858, 1965, 1978, 2076, 2159` — the report's list matches one-for-one. `palace/linalg/ksp.cpp:297-310` `BaseKspSolver<OperType>::Mult` body confirmed: void return, `ksp->Mult(x, y)`, `Mpi::Warning` on `!ksp->GetConverged()`, counter mutations at 308-309. `palace/linalg/eps.hpp:22-141` `EigenvalueSolver` abstract base confirmed: `WhichType` nine-way enum (with TARGET_REAL / TARGET_IMAGINARY present in the enum but per the source, marked unimplemented in ARPACK at `arpack.cpp:300-304`). `palace/linalg/slepc.cpp:711-716` `GetEigenvalue(i)` returning `l * gamma` confirmed (Higham un-scaling at the accessor). `palace/linalg/arpack.cpp:570-590` `ApplyOp` body confirmed (host-pointer convention; opK->Mult + opInv->Mult non-sinvert at 573-574; opM->Mult + opInv->Mult sinvert at 579-580). `palace/drivers/eigensolver.cpp:280-340` setup composition confirmed (SetShiftInvert at 285 / 305; SetWhichEigenpairs at 291-315; SetLinearSolver at 330-334). One minor imprecision: `palace/models/modeeigensolver.cpp:470, 477` cited for `SetOperators` — line 470 is the `SetOperators` call but line 477 is `SetInitialSpace`, not a `SetOperators` call. The intended cross-reference is the `eigensolver.cpp:177, 185, 189, 193` set of `SetOperators` callsites (verified via `search_text eigen->SetOperators`); the report doesn't cite these. Marked `warning` (not `fail`) because the body-of-the-claim is supported; only the secondary citation line in Sub-pattern A is mis-numbered.

**surface-or-evidence (pass)** — This is a new L1>L0 theme file (not a refinement to an existing one); the proposed-changes block creates the surface (`book/src/L1-L0/eigsolve-mutation-rotation.md`) directly. The proposal adds substantive content (~750 lines of theme prose) plus dep-map row + SUMMARY.md row. Not a pure-rotation-claim shape; not a retroactive-evidence backfill shape — straightforward "create new chapter" surface-emission with full citation backing.

**rotation-quality (pass)** — The theme makes the L1 form **strictly more compact / more abstract** than the L0 form. The L0 surface comprises ~ 3 `Solve()` bodies (`ArpackEPSSolver`, `SlepcEPSSolverBase`, `QuasiNewtonSolver`) ranging from 50 to 450+ lines each, plus the abstract-base setter surface, plus the per-pair extraction triple-accessor + Higham-scaling-factor-getter surface, plus the 10 `opInv->Mult` shell-callback bodies. The L1 form collapses this to `result = eigsolve(E, control) -> EigResult` — one expression, with the orchestration axis (RCI / shell-matrix / direct-Newton) absorbed into `E`'s opaque type. State hiding (Higham scaling at accessor → Higham fields at result; per-pair iteration → tensor stack), coarser substitution (three backend bodies → one abstract eigsolve), and threaded-state compression (counter-return-plus-internal-array → record-return) are all present. Not renaming-only; not 1:1.

**variant-axis-coverage (pass)** — The theme explicitly identifies four variant axes — backend (ARPACK / SLEPc / QuasiNewtonSolver), spectral-transformation (shift-invert vs non-sinvert), problem-type (linear / quadratic / nonlinear), spectrum-target (9-way `WhichType` enum) — and addresses them as follows: (a) backend axis absorbed into `E`'s opaque type (parallels `ksp_solve`'s CG/GMRES/FGMRES collapse), with the recognition set explicitly closed at three families per applicability-condition #1; (b) spectral-transformation axis handled at Stage A2, with both branches in `eigensolver.cpp:285` (1i*target for C / A2 / SLP) and `eigensolver.cpp:305` (target² for linear EVP) explicitly cited; (c) problem-type axis preserved via the `EigSolver[problem]` phantom and the three `SetOperators` overloads at `eps.hpp:57-74` cited; (d) spectrum-target axis covered via Stage A3 with per-backend mapping cited (ARPACK at `arpack.cpp:236-308`, SLEPc at `slepc.cpp:565-600`), and the unimplemented `(ARPACK, TARGET_REAL/TARGET_IMAGINARY)` pairs explicitly scoped out per CLAUDE.md "Unimplemented Palace stub policy" with `arpack.cpp:300-304` MFEM_ABORT cited. The hermitian-vs-generalized sub-axis (mentioned in the dispatch prompt) is covered via the `SetProblemType(GEN_NON_HERMITIAN)` at modeeigensolver.cpp:1047 and the three `SetOperators` overloads on the problem-type tag. No hidden branches.

**cross-reference-integrity (pass)** — All `[link]` references resolve. Verified that the following exist under `book/src/`: `L1/eigsolve.md`, `L1/ksp_solve.md`, `L1/apply_linop.md`, `L1/dot.md`, `L1/nrm2.md`, `L1/axpy.md`, `L1/axpby.md`, `L1-L0/ksp-solve-mutation-rotation.md`, `L1-L0/apply-linop-mutation-rotation.md`, `L0/eigensolver-wrapper.md`, `L0/mutable-workspace-pattern.md`, `L0/output-arg-vs-receiver.md`. The Edit 2 anchor text against `L1-L0/index.md` matches verbatim (verified ksp-solve-mutation-rotation / minres-iteration / bicgstab-iteration sequence). The Edit 3 anchor text against `SUMMARY.md` (lines 51-53) matches verbatim. The cycle-010 lifter report path resolves. The slug `eigsolve-mutation-rotation` does not collide with existing files.

**edge-label-fidelity (pass)** — The proposal carries the edge label L1>L0 (theme file lives under `book/src/L1-L0/`, the SUMMARY.md row places it under the L1-L0 Part, the dep-map row says "L1/eigsolve (rough-in)" on the L1 side and the Palace `.cpp` files on the L0 side). The prose narrates the rewrite forward from L1 (`eigsolve(E, control) -> EigResult`) to L0 (the three subclass bodies + per-pair extraction surface). LHS = L1; RHS = L0. The four sub-pattern decompositions (A setup, B inner-solve, C result-status, D teardown) each narrate the L1-form → L0-form direction. Aligned with "Layers are defined high→low; lifting notes go in working notes" invariant.

**plan-kind-consistency (pass)** — The proposal declares `status: firm (structural; partly-constructive on Sub-pattern B LinearSolveFailed materialisation)`. The content shape matches a `firm` theme entry: complete sub-pattern decomposition (4 sub-patterns each with cited rewrites + Justification-kind paragraph), exhaustive citation backing (the 10 `opInv->Mult` callsites, the three Solve() bodies, the driver-side composition), 6 applicability conditions, an explicit `Speculative L1 operators: None` section, a Verified-against block listing all cited ranges. The `partly-constructive` annotation is well-scoped: it applies *only* to Sub-pattern B's `LinearSolveFailed` materialisation rewrite-shape (which is recorded forward-looking), not to the rest of the theme. The dispatch's "candidate methodology pattern, flagged for cycle-012 meta-phase" is correctly framed as informational telemetry, not as gating the firm status of the structural content.

**skill-uptake-survey (pass)** — The proposal cites verification via `mcp__palace-codemap__read_range` for all 23+ source ranges in the Verified-against block. The 10 `opInv->Mult` callsite enumeration is attributed to cycle-010 lifter's `mcp__palace-codemap__search_text` enumeration (and confirmed during this dispatch via re-running the same search). The L1 `eigsolve` rough-in citation (`book/src/L1/eigsolve.md`) is explicit. No relevant `skills/` candidate that I can identify is missed; the L1>L0 theme-authoring pattern is well-established by `ksp-solve-mutation-rotation` precedent (cycle-008). Pure presence-check pass.

### Issues found

**Issue 1 — minor citation imprecision (Sub-pattern A "Stage A5" citation block).**
Location: `CYCLE.md` Sub-pattern A Citations bullet "`palace/models/modeeigensolver.cpp:470, 477` — `SetOperators` call site for the eigenmode pipeline."
Severity: low.
Detail: line 470 is the `SetOperators` call (`eigen->SetOperators(*opB, *opA, EigenvalueSolver::ScaleType::NONE);` verified via `search_text eigen->SetOperators`), but line 477 is `eigen->SetInitialSpace(*initial_space);` — not a `SetOperators` call. The intended companion cite for the driver-side `SetOperators` callsites is `palace/drivers/eigensolver.cpp:177, 185, 189, 193` (the four `eigen->SetOperators` callsites in the driver eigenmode pipeline covering quadratic-with-scale / quadratic-without-scale / linear branches). The Sub-pattern A body prose itself is supported; only the line-number list in the Citations block is slightly off. Repairable mechanically: either drop the `, 477` suffix to leave just `470`, or replace with the driver-side `eigensolver.cpp:177, 185, 189, 193` cite.

**Issue 2 — informational: partly-constructive theme-status flag is appropriately surfaced but the meta-phase forwarding mechanism should be double-checked.**
Location: `CYCLE.md` §Open questions/caveats bullet 1 + §Status second paragraph.
Severity: informational (per dispatch prompt's "note as informational").
Detail: The report flags `partly-constructive lowering` as a candidate theme-status for cycle-012 meta-phase consideration, citing cycle-010 lifter as recurrence-1 and this dispatch as recurrence-2. This is well-framed — both the L1 entry (`L1/eigsolve.md`) and this L1>L0 theme record the constructive-introduction pattern with the same vocabulary ("L1-constructive", "negative anchor", "rewrite shape recorded forward-looking"). The meta-phase forwarding (via the `Open questions / caveats` block being lifted to `scaffolding/open-questions.md` by integrator-per-report) is the expected channel; the dispatch correctly does not pre-empt the methodology decision. No action required of repairer or integrator; flagging for cycle-012 meta-phase telemetry.

**Issue 3 — informational: driver-side double-solve composition correctly flagged out-of-scope.**
Location: `CYCLE.md` §Open questions/caveats bullet 4.
Severity: informational.
Detail: The report flags `palace/drivers/eigensolver.cpp:377-407` (QuasiNewton refinement consuming the linear eigensolve's result as initial guesses) as a higher-level composition that is more naturally an L2 / L4 monadic-composition pattern, out of scope for this L1>L0 theme. Verified by direct read of `eigensolver.cpp:365-410` — the refinement is indeed a `qn = make_unique<QuasiNewtonSolver>(... std::move(eigen), num_conv, ...)` composition that takes the prior eigen-solver's result count as a parameter, then re-invokes Solve(). This is correctly identified as eigsolve-composition (an L2/L4 monad-bind pattern), not a single-eigsolve lowering. The cycle-012+ same-layer-cross-cutter routing is appropriate.

**Issue 4 — informational: zero speculative L1 operators (confirmed).**
Location: `CYCLE.md` §Speculative operators proposed + §Speculative L1 operators.
Severity: informational.
Detail: The dispatch is explicit that zero speculative L1 operators are introduced. Verified by inspection — the theme uses only `eigsolve` (LHS, rough-in cycle-009), `ksp_solve` (recursed into via Sub-pattern B), `apply_linop` (per-step `opK->Mult` / `opM->Mult` / `opC->Mult` inside `ApplyOp` bodies), `dot` / `nrm2` / `axpy` / `axpby` (transitively). The `LinearSolveFailed` variant is internal to the existing `eigsolve` form's `EigStatus` sum type (already annotated as L1-constructive at the L1 entry per cycle-010 lifter). This matches the "promote a speculative L1 operator to firm only when small AND when it simplifies the semantics of higher forms" invariant — no promotion is attempted, and the theme operates entirely within firm/rough-in L1 vocabulary.

**Issue 5 — minor consistency: backend-axis recognition set wording.**
Location: `CYCLE.md` §Applicability conditions condition #1 and Sub-pattern A bullet "Backend selection (Stage A1)".
Severity: low.
Detail: The recognition-set claim ("the only three concrete subclass families in the corpus") is correct per direct source inspection — `ArpackEigenvalueSolver` (with `ArpackEPSSolver` / `ArpackPEPSolver` subclasses), `SlepcEigenvalueSolver` (with `SlepcEPSSolverBase` / various SLEPc subclasses), and `NonLinearEigenvalueSolver::QuasiNewtonSolver`. However, the report alternates between "three subclass families" and listing four families (e.g., the §Open questions bullet enumerates "ARPACK / SLEPc / `SlepcNEPSolver` / `QuasiNewtonSolver`" — treating `SlepcNEPSolver` as a fourth family). Suggest tightening to the three top-level recognition families with `SlepcNEPSolver` noted as a SLEPc-family subclass. Minor; cosmetic.

**Issue 6 — observation (not a defect): the per-pair extraction Loop in Sub-pattern C is correctly identified as the same destination-binding pattern as `apply-linop-mutation-rotation` sub-pattern A.**
Location: `CYCLE.md` Sub-pattern C, the per-pair extraction code block.
Severity: none — verification.
Detail: The cross-theme reuse claim — that `GetEigenvector(i, x)`'s out-parameter `x` is the same destination-binding pattern as `apply_linop`'s `out` parameter — is correct. Confirmed at `eps.hpp:128-129` (`virtual void GetEigenvector(int i, ComplexVector &x) const = 0;`) — out-parameter form, matching `apply_linop`'s `Mult(x, y)` form. No issue.

## Repair

### Fixes attempted

- **Finding (Issue 1)**: `palace/models/modeeigensolver.cpp:470, 477` cited as a `SetOperators` callsite pair; line 470 is the `SetOperators` call but line 477 is `eigen->Solve()` (and the adjacent `SetInitialSpace` is at line 474). The critic suggested the companion cite is the driver-side `eigensolver.cpp:177, 185, 189, 193` `SetOperators` callsite group.
  - **Decision**: repaired.
  - **Action**: Two edits to `CYCLE.md` Sub-pattern A:
    1. Stage A5 code-block comment (line 146 region) — replaced `(modeeigensolver.cpp:470, 477)` with `(modeeigensolver.cpp:470; driver-side overloads at eigensolver.cpp:177, 185, 189, 193)`.
    2. Citations bullet (line 233-234 region) — split into two bullets: one for `modeeigensolver.cpp:470` (linear EVP `(opB, opA)` binding) and one for the four driver-side `eigensolver.cpp:177, 185, 189, 193` callsites (SLP nonlinear / quadratic-with-A2-scale / quadratic-without-A2 / linear branches). Confirmed against direct read of both files (modeeigensolver.cpp:465-484 and eigensolver.cpp:170-195) — all five line numbers are exact `SetOperators` callsite anchors.
  - **Rationale**: mechanical citation fix — drop a wrong line number, add the verified companion citation. Body-of-claim was already supported by the critic's read; this only corrects the secondary citation line.

- **Finding (Issue 2)**: partly-constructive theme-status pattern flagged for cycle-012 meta-phase (recurrence-2 with cycle-010 lifter as recurrence-1).
  - **Decision**: not-needed.
  - **Rationale**: critic marked as informational, no action required. The Open-questions block already routes this to cycle-012 meta-phase via the integrator-per-report OQ-promotion channel.

- **Finding (Issue 3)**: driver-side double-solve composition (`eigensolver.cpp:377-407`) flagged out-of-scope for this L1>L0 theme; appropriate L2/L4 monad-bind pattern.
  - **Decision**: not-needed.
  - **Rationale**: critic verified out-of-scope routing is correct; the OQ block already routes to cycle-012+ same-layer-cross-cutter.

- **Finding (Issue 4)**: zero speculative L1 operators (confirmed).
  - **Decision**: not-needed.
  - **Rationale**: verification only, no defect.

- **Finding (Issue 5)**: minor consistency in backend-axis recognition-set wording (three top-level families vs four when `SlepcNEPSolver` is enumerated as separate).
  - **Decision**: not-needed (cosmetic).
  - **Rationale**: critic explicitly marked low/cosmetic. The Applicability conditions §1 and the Coverage note in Verified-against both correctly say "three concrete subclass families"; the lone Open-questions bullet listing "SlepcNEPSolver" alongside "SLEPc" reflects a SLEPc-family subclass-level callout, not a redefinition of the recognition set. Repairer authority for "rewriting prose for consistency" is borderline; given the critic flagged as cosmetic and the structural recognition set is already correct in the canonical Applicability §1 wording, declining the rewrite.

- **Finding (Issue 6)**: cross-theme destination-binding reuse to `apply-linop-mutation-rotation` sub-pattern A — verification confirms claim.
  - **Decision**: not-needed.
  - **Rationale**: verification only, no defect.

### Unrepairable findings

None. The only defect-level finding (Issue 1 citation imprecision) was repairable mechanically.

## Suggested resolution

`pass-after-repair` — overall_status is `ready` (under the standard schema; using `pass-after-repair` per the dispatch prompt for visibility). The integrator may apply the proposed-changes block in CYCLE.md as-is; the repaired citations are now consistent with direct source verification.

Notes for integrator:
- The three create/edit operations in CYCLE.md proposed-changes are non-overlapping with other wave-2 reports (verified by report-scope: `book/src/L1-L0/eigsolve-mutation-rotation.md` is a new file; `book/src/L1-L0/index.md` and `book/src/SUMMARY.md` are append-shaped insertions that should not conflict with sister wave-2 dispatches if they touch other Parts).
- The Open-questions block carries three forward-routed items (partly-constructive theme-status meta-phase-2, three sibling eigsolve OQs, slepc-convergence-reason-lift sub-theme candidate, driver-side double-solve L2 composition candidate) — these are integrator-per-report's responsibility to promote to `scaffolding/open-questions.md`.
