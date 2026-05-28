---
agent: lowering-verifier
invoked_at: 2026-05-28T03:43:11Z
scope: L1>L0 theme audit — eigsolve-mutation-rotation
status: integrated
integrated_at: 2026-05-28T072500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-012 (report 3 of 8). Lowering-verifier audit of eigsolve-mutation-rotation; verdict confirms-with-refinement. Only Edit 1 (verified_against YAML) applied; Edits 2-3 NOT applied (routed to GATED cycle-013 abstractor via OQ eigsolve-getconverged-forwarder-fix-and-gated-promotion). Sub-pattern B partly-constructive -> firm promotion UNBLOCKED but NOT enacted; ## Status caveat retained. ORCHESTRATOR CORRECTION: this row was originally mis-filed to a cycle-013-staging dir; relocated to cycle-012; backward cycle-013 refs corrected; forward-refs to the gated cycle-013 abstractor intentionally retained. 0 gate hits."
inputs:
  - book/src/L1-L0/eigsolve-mutation-rotation.md
  - reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md
  - palace/linalg/arpack.cpp:236-308, 513-560, 563-589, 733-797
  - palace/linalg/nleps.cpp:500-540, 780-806
  - palace/linalg/slepc.cpp:565-600, 687-716, 1847-1872, 1942-2000, 2060-2095, 2125-2170
  - palace/linalg/ksp.cpp:297-310
  - palace/linalg/ksp.hpp:30-72
  - palace/linalg/eps.hpp:57-141
  - palace/linalg/iterative.hpp:98
  - palace/drivers/eigensolver.cpp:280-340
  - palace/models/modeeigensolver.cpp:1020-1054
---

# CYCLE: Audit eigsolve-mutation-rotation

## Summary

Per-line audit of the cycle-011 `eigsolve-mutation-rotation` L1>L0 theme
(`book/src/L1-L0/eigsolve-mutation-rotation.md`) against concrete Palace
L0 evidence, using MCP codemap `read_range` / `search_text`. Top-level
verdict: **partially-supported (confirms-with-refinement)**. The theme's
core structural claims hold: all **ten `opInv->Mult` callsites are
exhaustively confirmed** at the cited line numbers and are exhaustive
across the Palace corpus (a fresh `search_text "opInv->Mult"` returns
exactly these ten, no others); each callsite's per-step semantics match
the source comments; the negative anchor (`ksp.cpp:297-310`) confirms
`BaseKspSolver::Mult` is `void`-return with warning-only on
non-convergence; the setup surface, per-pair extraction surface, and all
three backend `Solve` bodies match.

Two **confirms-with-refinement** findings and one **material refinement**
on Sub-pattern B:
1. **(Sub-pattern B, material)** The partly-constructive materialisation
   writes `if (!opInv->GetConverged())`, but `GetConverged()` does **not
   exist** on `opInv`'s type (`ComplexKspSolver = BaseKspSolver<ComplexOperator>`).
   The accessor exists only on the *private* `IterativeSolver` member
   (`iterative.hpp:98`), reached internally via `ksp->GetConverged()`
   inside `BaseKspSolver::Mult` (`ksp.cpp:301`). The materialisation
   therefore understates (slightly) the required upstream change: it
   needs a public `GetConverged()` forwarder on `BaseKspSolver` (a
   one-line addition mirroring the existing `GetRelTol()` forwarder at
   `ksp.hpp:64`), OR `Mult` to return status instead of `void`. This
   does **not** invalidate the partly-constructive verdict — it
   *confirms* it (the change is mechanical and small, as the theme
   claims) — but the rewrite snippet should be corrected so it compiles
   against the named type.
2. **(Sub-pattern A, minor)** The theme attributes the per-`WhichType`
   switch with the `MFEM_ABORT` to `ArpackEigenvalueSolver::SetWhichEigenpairs`.
   The actual `SetWhichEigenpairs` body is a trivial field-set
   (`arpack.cpp:236-239`); the per-`WhichType` switch and the
   `MFEM_ABORT` on TARGET_REAL/TARGET_IMAGINARY live in
   `SolveInternal` (`arpack.cpp:~280-307`, abort at ~302-304). The cited
   *range* (236-308) covers both functions, so the citation is in-range;
   only the function-name label in the prose is imprecise.
3. **(applicability-condition 4, minor)** The ncv-clamp cite
   `arpack.cpp:521-525` points a few lines off — the actual clamp
   (`if (ncv > N) { ncv = ...; }`) is at `arpack.cpp:518-520` (with the
   global dimension fetched as `N = GlobalSize(...)` at 517); lines
   522-525 are the `arpack_it` default. In-range at the function level,
   off by a few lines at the statement level.

**Promotion outcome:** the audit **unblocks** (but does **not enact**)
the partly-constructive → fully-firm promotion of Sub-pattern B. The
partly-constructive shape is sound and the upstream change is confirmed
mechanical; this satisfies the theme's promotion gate (b) ("a
lowering-verifier audit that confirms the partly-constructive shape is
acceptable"). **The promotion is GATED on Edit 2 landing first:** the
`GetConverged()` forwarder snippet correction must be applied to the
theme by a follow-up **abstractor dispatch** (cycle-013) *before* the
partly-constructive caveat is dropped. Do **not** promote to fully-firm
in the same pass that defers the snippet fix — the verdict couples a
status promotion to a surface edit this audit did not apply (Edits 2-3
are proposed for abstractor reread, not enacted by this verifier per
role discipline). **Integrator note:** the eigsolve-mutation-rotation
theme should NOT be auto-promoted to firm this cycle; schedule a
cycle-013 abstractor dispatch to apply the GetConverged forwarder
correction, then promote. The cycle-012 meta-phase codification of the
partly-constructive theme-status is supported by this evidence
(recurrence-2). No obstruction surfaced; the three refinements are
proposed as edits, not blockers.

## Per-citation audit

### Sub-pattern B — the ten `opInv->Mult` callsites (core)

- **Citation**: `palace/linalg/arpack.cpp:574`
  - **Theme claim**: `ArpackEPSSolver::ApplyOp` non-sinvert branch; after
    `opK->Mult(x1,z1)`; computes `y = M⁻¹ K x`.
  - **Found**: `opInv->Mult(z1, y1)` at 574, preceded by `opK->Mult(x1, z1)`
    at 573, in the `if (!sinvert)` branch; source comment "Case 1:
    `y = M⁻¹ K x`".
  - **Verdict**: supports.
  - **Notes**: actual args `(z1, y1)` not the theme's generic `(b, x)`
    placeholder — placeholder is fine for the narrative.

- **Citation**: `palace/linalg/arpack.cpp:580`
  - **Theme claim**: sinvert branch; after `opM->Mult(x1,z1)`; computes
    `y = (K − σM)⁻¹ M x`.
  - **Found**: `opInv->Mult(z1, y1)` at 580, preceded by `opM->Mult(x1, z1)`
    at 579, in the `else` (sinvert) branch; source comment "Case 2:
    `y = (K - σ M)⁻¹ M x`".
  - **Verdict**: supports.

- **Citation**: `palace/linalg/arpack.cpp:761`
  - **Theme claim**: `ArpackPEPSolver::ApplyOp` non-sinvert; PEP
    linearised; `y₂ = M⁻¹ K x₁` component.
  - **Found**: `opInv->Mult(z1, y2)` at 761 in `if (!sinvert)`; source
    comment "Case 1: `y = L₁⁻¹ L₀ x`" with `L₀ = [-K 0; 0 M]`,
    `L₁ = [C M; M 0]`.
  - **Verdict**: supports.
  - **Notes**: theme's `M⁻¹ K` gloss is a component-level simplification
    of the linearised `L₁⁻¹ L₀`. Acceptable as a component sketch; the
    full block form is in the source comment.

- **Citation**: `palace/linalg/arpack.cpp:778`
  - **Theme claim**: sinvert branch; `(L₀ − σL₁)⁻¹` component.
  - **Found**: `opInv->Mult(z1, y1)` at 778 in `else`; source comment
    "Case 2: `y = (L₀ - σ L₁)⁻¹ L₁ x`".
  - **Verdict**: supports.

- **Citation**: `palace/linalg/nleps.cpp:514`
  - **Theme claim**: `QuasiNewtonSolver::Solve` inline-lambda
    `deflated_solve` inner Newton-step solve; `x₁ = T(σ)⁻¹ b₁`.
  - **Found**: `opInv->Mult(b1, x1)` at 514 inside the `deflated_solve`
    lambda (defined at 505); source comment block "x1 = T^-1 b1" for the
    block system `|T(σ) U(σ); A(σ) B(σ)|`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/slepc.cpp:1858`
  - **Theme claim**: `__pc_apply_EPS`; `y = M⁻¹ x` or `(K − σM)⁻¹ x`.
  - **Found**: `ctx->opInv->Mult(ctx->x1, ctx->y1)` at 1858; function-doc
    comment "y = M⁻¹ x, or shift-and-invert: y = (K - σ M)⁻¹ x".
  - **Verdict**: supports.

- **Citation**: `palace/linalg/slepc.cpp:1965`
  - **Theme claim**: `__pc_apply_PEPLinear` non-sinvert; `y₂ = M⁻¹ x₂`.
  - **Found**: `ctx->opInv->Mult(ctx->x2, ctx->y2)` at 1965 in
    `if (!ctx->sinvert)`; function-doc "y = L₁⁻¹ x" with
    `L₁ = [I 0; 0 M]` — lower block solve = `M⁻¹ x₂`.
  - **Verdict**: supports.
  - **Notes**: theme's `M⁻¹ x₂` gloss correctly identifies the lower
    block of `L₁⁻¹` (the `M` block).

- **Citation**: `palace/linalg/slepc.cpp:1978`
  - **Theme claim**: sinvert branch; `(L₀ − σL₁)⁻¹ x`.
  - **Found**: `ctx->opInv->Mult(ctx->y1, ctx->y2)` at 1978 in `else`;
    function-doc "shift-and-invert: y = (L₀ - σ L₁)⁻¹ x".
  - **Verdict**: supports.

- **Citation**: `palace/linalg/slepc.cpp:2076`
  - **Theme claim**: `__pc_apply_PEP` direct quadratic; `y = M⁻¹ x` or
    `P(σ)⁻¹ x`.
  - **Found**: `ctx->opInv->Mult(ctx->x1, ctx->y1)` at 2076; function-doc
    "y = M⁻¹ x, or shift-and-invert: y = P(σ)⁻¹ x".
  - **Verdict**: supports.

- **Citation**: `palace/linalg/slepc.cpp:2159`
  - **Theme claim**: `__pc_apply_NEP`; per-λ preconditioner update
    (2140-2158) + `opInv->Mult`.
  - **Found**: per-λ PC reconfiguration block at 2141-2158
    (`opA2_pc`/`opA_pc`/`opP_pc` rebuild + `opInv->SetOperators` at 2152
    when `new_lambda && !first_pc`), then `ctx->opInv->Mult(ctx->x1, ctx->y1)`
    at 2159.
  - **Verdict**: supports.
  - **Notes**: confirms the spectral-transformation-lifecycle branch the
    theme's Sub-pattern D also cites at the same range.

- **Exhaustiveness check**: fresh `search_text "opInv->Mult"` over the
  whole corpus returns exactly these ten hits and no others. The theme's
  "ten callsites exhaustive" claim is **confirmed independently** (not
  just inherited from the cycle-010 lifter).

### Sub-pattern B — negative anchor

- **Citation**: `palace/linalg/ksp.cpp:297-310`
  - **Theme claim**: `BaseKspSolver<OperType>::Mult` is `void`-return,
    emits only `Mpi::Warning` on non-convergence; none of the ten
    callsites query convergence after the call.
  - **Found**: `void BaseKspSolver<OperType>::Mult(...)`; body calls
    `ksp->Mult(x,y)`, then `if (!ksp->GetConverged()) { Mpi::Warning(...); }`
    (301-307), then `ksp_mult++; ksp_mult_it += ksp->GetNumIterations();`.
    No status returned; no out-parameter for status.
  - **Verdict**: supports. **Strong** negative anchor — the convergence
    bit is computed (`ksp->GetConverged()`) and immediately discarded
    after the warning.

### Sub-pattern B — the `GetConverged()` accessor (materialisation correctness)

- **Citation**: theme materialisation snippet `if (!opInv->GetConverged())`
  vs `palace/linalg/ksp.hpp:30-72` + `palace/linalg/iterative.hpp:98`
  - **Theme claim**: "the `GetConverged()` accessor exists on
    `IterativeSolver` and is already used inside `BaseKspSolver::Mult`
    ... so the upstream behaviour change is mechanical and small."
  - **Found**: `GetConverged()` is declared on `IterativeSolver`
    (`iterative.hpp:98`: `bool GetConverged() const { ... }`). The
    `BaseKspSolver` public surface (`ksp.hpp:54-69`) exposes
    `NumTotalMult`, `NumTotalMultIterations`, `GetRelTol/GetAbsTol`,
    `SetRelTol/SetAbsTol`, `SetOperators`, `Mult` — **but NOT
    `GetConverged`**. The `IterativeSolver ksp` member is `protected`
    (`ksp.hpp:40`). `opInv` in every callsite is a `ComplexKspSolver`
    (= `BaseKspSolver<ComplexOperator>`).
  - **Verdict**: partially-supports. The factual claim ("`GetConverged`
    exists on `IterativeSolver`, used inside `Mult`") is TRUE; but the
    materialisation *calls it on `opInv`*, which is the `BaseKspSolver`
    wrapper, not the `IterativeSolver`. As written the snippet does not
    compile. The upstream change is one of: (a) add a public
    `bool GetConverged() const { return ksp->GetConverged(); }` forwarder
    to `BaseKspSolver` (one line, exactly parallel to the existing
    `GetRelTol()` forwarder), or (b) change `Mult` to return status.
  - **Notes**: this *strengthens* the partly-constructive verdict — the
    change is genuinely mechanical (the forwarder pattern already exists
    on the class). Proposed prose/snippet refinement below.

### Sub-pattern A — setup surface

- **Citation**: `palace/linalg/eps.hpp:57-74` (three `SetOperators` +
  problem-type dispatch)
  - **Theme claim**: three `SetOperators` overloads with `MFEM_ABORT`
    defaults dispatching on problem-type tag.
  - **Found**: three `virtual void SetOperators(...)` overloads (K,M /
    K,C,M / K,M,A2-function), each body `MFEM_ABORT("SetOperators not
    defined!")`. Confirmed.
  - **Verdict**: supports.
  - **Notes**: `eps.hpp:76-86` additionally has `SetExtraSystemMatrix`
    and `SetPreconditionerUpdate` virtuals (also `MFEM_ABORT` defaults) —
    these are the sub-axis bindings the abstractor's check-item (i) asks
    about; they exist and are part of the setup surface.

- **Citation**: `palace/linalg/eps.hpp:116-119` (`SetWhichEigenpairs` /
  `SetShiftInvert`)
  - **Theme claim**: setter virtuals.
  - **Found**: `SetWhichEigenpairs(WhichType)` and
    `SetShiftInvert(complex, bool precond=false)` pure-virtuals at
    ~117/120; `SetInitialSpace`, `Solve`, `GetEigenvalue`,
    `GetEigenvector`, `GetError`, `RescaleEigenvectors` follow (124-140).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/arpack.cpp:236-308` (`SetWhichEigenpairs`
  body)
  - **Theme claim**: per-`WhichType` switch with `MFEM_ABORT` for
    unimplemented TARGET_REAL/TARGET_IMAGINARY.
  - **Found**: `ArpackEigenvalueSolver::SetWhichEigenpairs` is a trivial
    field-set (`{ which_type = type; }`, 236-239). The per-`WhichType`
    switch (mapping to `::arpack::which::*`) and the `MFEM_ABORT` on
    TARGET_REAL/TARGET_IMAGINARY are in `SolveInternal` (~280-307, abort
    at ~302-304).
  - **Verdict**: partially-supports. The `MFEM_ABORT` stub claim is TRUE
    and within the cited range; the prose mis-attributes the switch to
    `SetWhichEigenpairs` (it is in `SolveInternal`). Proposed prose
    refinement below.

- **Citation**: `palace/linalg/arpack.cpp:241-247` (`SetShiftInvert`)
  - **Theme claim**: binds `sigma`, sets `sinvert = true`, rejects
    `precond = true`.
  - **Found**: `MFEM_VERIFY(!precond, ...)`; `sigma = s; sinvert = true;`.
    Exact match.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/slepc.cpp:565-600` (`SetWhichEigenpairs`)
  - **Theme claim**: nine-way switch with SLEPc EPS token mapping.
  - **Found**: full nine-case switch
    (`EPS_LARGEST_MAGNITUDE`...`EPS_TARGET_IMAGINARY`), all implemented
    (no `MFEM_ABORT`).
  - **Verdict**: supports.
  - **Notes**: surfaces a real asymmetry the theme correctly flags —
    SLEPc implements TARGET_REAL/TARGET_IMAGINARY; ARPACK aborts on them.
    Confirms the recognition-note in Sub-pattern A's spectrum-target
    bullet.

- **Citation**: `palace/drivers/eigensolver.cpp:280-340` (driver-side
  setup)
  - **Theme claim**: five-stage composition (shift-invert +
    which-eigenpairs + linear-solver binding); A builds against
    `(K + iσC − σ²M + A2)`.
  - **Found**: `SetShiftInvert(1i*target)` (quadratic/nonlinear/SLP) or
    `SetShiftInvert(target*target)` (linear EVP); backend-and-problem-
    conditional `SetWhichEigenpairs` (ARPACK→SMALLEST_IMAGINARY/LARGEST_REAL,
    SLP→TARGET_MAGNITUDE, else→TARGET_IMAGINARY/TARGET_REAL);
    `A = GetSystemMatrix(1, iσ, -σ², K, C, M, A2)`; `ksp->SetOperators(*A,*P)`;
    `eigen->SetLinearSolver(*ksp)`.
  - **Verdict**: supports (with simplification note).
  - **Notes**: the actual spectrum-target mapping is a 2×(branch) ×
    backend matrix richer than the theme's inline Stage-A3 pseudocode
    (which shows only the SMALLEST_IMAGINARY/TARGET_IMAGINARY pair). The
    theme labels it "backend-conditional" and cites the full range, so
    the inline example is illustrative, not a completeness claim — but a
    one-line note acknowledging the linear-EVP (LARGEST_REAL/TARGET_REAL)
    and SLP (TARGET_MAGNITUDE) branches would sharpen it. Confirms
    applicability-condition 3.

- **Citation**: `palace/models/modeeigensolver.cpp:1020-1054` (backend
  dispatch)
  - **Theme claim**: ARPACK-vs-SLEPc construction; build-time
    `#if defined` + runtime `type ==` selection; SLEPc sets
    `KRYLOVSCHUR` + `GEN_NON_HERMITIAN`.
  - **Found**: build-time default `#if PALACE_WITH_SLEPC / #elif
    PALACE_WITH_ARPACK`; runtime `if (type == EigenSolverBackend::ARPACK)`
    branch; ARPACK path `SetNumModes/SetTol/SetWhichEigenpairs/SetLinearSolver`;
    SLEPc path `SetType(KRYLOVSCHUR)` + `SetProblemType(GEN_NON_HERMITIAN)`
    + same setters.
  - **Verdict**: supports. (Correct file `palace/models/modeeigensolver.cpp`,
    not the planner's `palace/eigensolver/...` mis-cite.)

### Sub-pattern C — result-status flow

- **Citation**: `palace/linalg/eps.hpp:57-141` (per-pair surface +
  scaling accessors)
  - **Theme claim**: `Solve()→int`, three per-pair accessors,
    `GetScalingGamma/Delta`.
  - **Found**: `virtual int Solve()`, `GetEigenvalue(int)→complex`,
    `GetEigenvector(int, ComplexVector&)`, `GetError(int, ErrorType)→double`,
    `RescaleEigenvectors(int)`, `GetScalingGamma/GetScalingDelta` (102-103).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/slepc.cpp:687-709` (`Solve` body)
  - **Theme claim**: `EPSSolve`+`EPSGetConverged` (694-695); convergence
    summary (696-704); `RescaleEigenvectors(num_conv)` (707);
    `return (int)num_conv` (708).
  - **Found**: exact — `EPSSolve(eps)` (694), `EPSGetConverged(eps, &num_conv)`
    (695), print block with `EPSConvergedReasonView` (699) +
    `NumTotalMult/NumTotalMultIterations` (703), `RescaleEigenvectors(num_conv)`
    (707), `return (int)num_conv` (708).
  - **Verdict**: supports.
  - **Notes**: line 699 `EPSConvergedReasonView` is inside the
    `if (print > 0)` block — confirms the theme's "currently print-only,
    never queried" claim about the SLEPc convergence-reason path
    (Sub-pattern B SLEPc elaboration).

- **Citation**: `palace/linalg/slepc.cpp:711-716` (`GetEigenvalue`)
  - **Theme claim**: returns `l * gamma` (Higham un-scaling at accessor).
  - **Found**: `EPSGetEigenvalue(eps, i, &l, nullptr); return l * gamma;`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/arpack.cpp:513-560` (`ArpackEPSSolver::Solve`)
  - **Theme claim**: `SolveInternal` at 552, `RescaleEigenvectors(nev)` at
    555, `info = 0` reset at 558, `return num_conv` at 559.
  - **Found**: `SolveInternal(...)` invocation (552), `RescaleEigenvectors(nev)`
    (555), `info = 0;` (558), `return num_conv;` (559). Confirmed.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/nleps.cpp:780-806` (QuasiNewton
  result-construction)
  - **Theme claim**: eigenvalue/eigenvector accumulation; permutation sort
    by imag; `RescaleEigenvectors`; `return nev`.
  - **Found**: target-range recovery loop populating `eigenvalues`/
    `eigenvectors`; `perm` allocation + `std::sort` by `imag()` ascending
    (798-800); `RescaleEigenvectors(nev)` (803); `return nev` (805).
  - **Verdict**: supports.

### Sub-pattern D — teardown

- **Citation**: `palace/linalg/arpack.cpp:558` (`info = 0` reset)
  - **Found**: `info = 0;` at 558 with comment "Reset for next solve.".
  - **Verdict**: supports.

- **Citation**: `palace/linalg/slepc.cpp:2140-2158` (NEP per-λ PC
  reconfiguration)
  - **Found**: the per-λ rebuild block inside `__pc_apply_NEP`
    (`opA2_pc`/`opA_pc`/`opP_pc` + `opInv->SetOperators`).
  - **Verdict**: supports. (Same range cited under Sub-pattern B
    callsite 2159 — consistent dual-citation.)

## Applicability conditions

1. **Backend recognition set = {ARPACK, SLEPc, QuasiNewton}.**
   - **Verifiable**: yes — corpus has exactly `ArpackEigenvalueSolver`,
     `SlepcEigenvalueSolver`, `NonLinearEigenvalueSolver::QuasiNewtonSolver`
     subclass families; the ten callsites span exactly these three files.
   - **Found counter-example?**: no.

2. **No aliasing between `result.eigenvectors[i]` slice and any input
   buffer.**
   - **Verifiable**: partially — `GetEigenvector(int, ComplexVector&)`
     out-parameter convention confirmed (`eps.hpp:~133`); aliasing is a
     caller obligation, not statically checkable from the cited ranges.
     No observed aliasing in driver sites.
   - **Found counter-example?**: no.

3. **`E.linear`'s system operator matches the spectral-transformation
   shape.**
   - **Verifiable**: yes — `eigensolver.cpp:326-334` builds
     `A = GetSystemMatrix(1, iσ, -σ², K, C, M, A2)` and binds it to `*ksp`
     before `SetLinearSolver(*ksp)`. Directly confirmed.
   - **Found counter-example?**: no.

4. **`E.K_max ≤ N`.**
   - **Verifiable**: yes — `arpack.cpp:518-520` clamps `ncv` against
     global dimension `N` (`if (ncv > N) { ncv = ...; }`, with `N =
     GlobalSize(...)` fetched at 517). NOTE: the theme cites `521-525`
     for this, which is actually the `arpack_it` default (522-525); the
     clamp is at 518-520. In-range at function level, off by a few lines
     at statement level.
   - **Found counter-example?**: no (citation-drift only).

5. **Single-rank scope.**
   - **Verifiable**: by-convention (CLAUDE.md scope); the theme defers
     MPI surface to `apply_linop`/`dot`/`nrm2` sister themes. Not
     contradicted by cited ranges.
   - **Found counter-example?**: N/A.

6. **`LinearSolveFailed` materialisation requires upstream behaviour
   change.**
   - **Verifiable**: yes — confirmed by the negative anchor
     (`ksp.cpp:297-310`, void return) AND by the accessor finding
     (`GetConverged` not on `BaseKspSolver` public surface). The
     condition is correctly stated; the *materialisation snippet* needs
     the forwarder correction (see Proposed changes) but the *condition*
     is sound.
   - **Found counter-example?**: no — but the snippet refinement
     sharpens the "(a) future Palace refactor capturing `ksp->GetConverged()`"
     wording to make explicit that the refactor also needs a public
     forwarder (or a `Mult` return-type change) so the eigensolver body
     can observe the bit.

## Algebraic laws (if cited)

The theme cites no standalone algebraic-law steps; the per-callsite
semantics are reduction-chain delegations to the firm
`ksp-solve-mutation-rotation` sister theme (each `opInv->Mult` rewrites
by that theme's sub-pattern A). The per-step source comments
(`y = M⁻¹ K x`, `y = (K − σM)⁻¹ M x`, `y = L₁⁻¹ L₀ x`,
`y = (L₀ − σL₁)⁻¹ L₁ x`, `x1 = T^-1 b1`) all match the theme's stated
per-callsite semantics, so the reduction-chain delegation is sound at
the callsite-identification level. Full per-primitive decomposition of
each `ApplyOp` body into `dot`/`axpy`/`apply_linop` is out of this
audit's scope (and the theme correctly defers it to the sister themes).

The one law-like claim worth flagging: the theme's Sub-pattern C status
derivation
`match num_conv with | n==K_max -> Converged | n>0 -> PartialConverged | _ -> MaxIterReached`
holds against the L0 observable (the `int` return is a converged-count;
`eigensolver.cpp:367-374` formats it without an error path for
`0 < n < K_max`). Confirmed consistent — the three-way discrimination is
a faithful hoist of the L0 implicit count-vs-request comparison.

## Proposed changes

The audit found no contradictions that invalidate the theme; it found
three refinements (one material on the Sub-pattern B snippet, two minor
citation/attribution drifts). Emit the `verified_against:` block, and —
because Finding 1 is a snippet that would not compile as written —
propose the targeted snippet/prose refinements below for an abstractor
reread (per discipline: lowering-verifier proposes, does not unilaterally
rewrite).

### Edit 1: append `verified_against:` block to the theme

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/arpack.cpp:574
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: ApplyOp non-sinvert; opK->Mult then opInv->Mult; y=M⁻¹Kx
  - citation: palace/linalg/arpack.cpp:580
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: ApplyOp sinvert; opM->Mult then opInv->Mult; y=(K-σM)⁻¹Mx
  - citation: palace/linalg/arpack.cpp:761
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: PEP non-sinvert; source comment y=L₁⁻¹L₀x (theme M⁻¹K gloss is component-level)
  - citation: palace/linalg/arpack.cpp:778
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: PEP sinvert; y=(L₀-σL₁)⁻¹L₁x
  - citation: palace/linalg/nleps.cpp:514
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: deflated_solve lambda; x1=T(σ)⁻¹b1
  - citation: palace/linalg/slepc.cpp:1858
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: __pc_apply_EPS; y=M⁻¹x or (K-σM)⁻¹x
  - citation: palace/linalg/slepc.cpp:1965
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: __pc_apply_PEPLinear non-sinvert; lower block M⁻¹x₂
  - citation: palace/linalg/slepc.cpp:1978
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: __pc_apply_PEPLinear sinvert; (L₀-σL₁)⁻¹x
  - citation: palace/linalg/slepc.cpp:2076
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: __pc_apply_PEP; y=M⁻¹x or P(σ)⁻¹x
  - citation: palace/linalg/slepc.cpp:2159
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: __pc_apply_NEP; per-λ PC rebuild 2141-2158 then opInv->Mult
  - citation: palace/linalg/ksp.cpp:297-310
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: BaseKspSolver::Mult void return + Mpi::Warning only; strong negative anchor
  - citation: palace/linalg/ksp.hpp:30-72
    verdict: partially-supports
    audited_at: 2026-05-28T034311Z
    note: GetConverged NOT on BaseKspSolver public surface — materialisation needs a public forwarder (one line, mirrors GetRelTol) or Mult status return
  - citation: palace/linalg/iterative.hpp:98
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: GetConverged() defined here on IterativeSolver; reached only via the protected ksp member
  - citation: palace/linalg/eps.hpp:57-74
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: three SetOperators overloads with MFEM_ABORT defaults; plus SetExtraSystemMatrix/SetPreconditionerUpdate at 76-86
  - citation: palace/linalg/eps.hpp:102-103
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: GetScalingGamma/GetScalingDelta accessors
  - citation: palace/linalg/arpack.cpp:236-308
    verdict: partially-supports
    audited_at: 2026-05-28T034311Z
    note: MFEM_ABORT stub TRUE and in-range, but per-WhichType switch is in SolveInternal not SetWhichEigenpairs (236-239 is a trivial field-set)
  - citation: palace/linalg/arpack.cpp:241-247
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: SetShiftInvert binds sigma, sinvert=true, rejects precond
  - citation: palace/linalg/slepc.cpp:565-600
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: nine-way SLEPc EPS token switch; all implemented (asymmetry vs ARPACK abort)
  - citation: palace/linalg/slepc.cpp:687-709
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: EPSSolve+EPSGetConverged; EPSConvergedReasonView print-only at 699; return (int)num_conv
  - citation: palace/linalg/slepc.cpp:711-716
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: GetEigenvalue returns l*gamma (Higham un-scaling at accessor)
  - citation: palace/linalg/arpack.cpp:513-560
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: SolveInternal 552, RescaleEigenvectors 555, info=0 reset 558, return 559
  - citation: palace/linalg/nleps.cpp:780-806
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: target-range recovery + sort-by-imag perm + RescaleEigenvectors + return nev
  - citation: palace/drivers/eigensolver.cpp:280-340
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: full setup composition; spectrum-target richer than inline Stage-A3 example (linear-EVP LARGEST_REAL/TARGET_REAL + SLP TARGET_MAGNITUDE branches); confirms applicability-condition 3
  - citation: palace/models/modeeigensolver.cpp:1020-1054
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: backend dispatch; build-time #if + runtime type==; SLEPc KRYLOVSCHUR+GEN_NON_HERMITIAN
  - citation: palace/linalg/arpack.cpp:518-520
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: ncv-clamp against N (N=GlobalSize fetched at 517; applicability-condition 4 cited 521-525 — off by a few lines; clamp is 518-520, arpack_it default is 522-525)
audit_verdict: confirms-with-refinement
audit_note: >
  All 10 opInv->Mult callsites confirmed exhaustive + per-step semantics
  match source comments. Negative anchor (ksp.cpp:297-310) confirms void
  return. Sub-pattern B materialisation snippet refinement: GetConverged()
  is not on opInv's type (BaseKspSolver); needs a public forwarder
  (one-line, mirrors GetRelTol) or a Mult status-return — strengthens the
  partly-constructive verdict (change is mechanical, as claimed) but the
  snippet should be corrected. Two minor citation-drift refinements
  (SetWhichEigenpairs switch is in SolveInternal; ncv-clamp at 518-520 not
  521-525, with N=GlobalSize at 517 and arpack_it default at 522-525).
  UNBLOCKS but does NOT enact the partly-constructive → fully-firm
  promotion of Sub-pattern B: promotion is GATED on a cycle-013 abstractor
  dispatch applying the GetConverged forwarder snippet correction (Edit 2)
  to the theme first — do not drop the partly-constructive caveat in the
  same pass that defers the snippet fix. Supports cycle-012 meta-phase
  codification of partly-constructive theme-status (recurrence-2).
~~~
```

### Edit 2 (proposed for abstractor reread — Sub-pattern B snippet correction)

The materialisation snippet in Sub-pattern B currently reads
`if (!opInv->GetConverged())`. Because `GetConverged()` is not on
`BaseKspSolver`'s public surface, propose correcting the snippet to make
the required upstream addition explicit:

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
[old]:// After (L1-constructive materialisation; not yet in Palace source):
opInv->Mult(b, x);
if (!opInv->GetConverged()) {
  inner_failed = true;          // capture per-step inner failure
  break;                        // bubble out of the eigensolver outer loop
}
[new]:// After (L1-constructive materialisation; not yet in Palace source):
//   Requires first adding a public forwarder to BaseKspSolver (one line,
//   mirroring the existing GetRelTol() forwarder at ksp.hpp:64):
//     bool GetConverged() const { return ksp->GetConverged(); }
//   OR changing BaseKspSolver::Mult to return a status instead of void.
opInv->Mult(b, x);
if (!opInv->GetConverged()) {     // forwarder added per the note above
  inner_failed = true;            // capture per-step inner failure
  break;                          // bubble out of the eigensolver outer loop
}
```

And in the prose immediately after the snippet, propose tightening
"the `GetConverged()` accessor exists on `IterativeSolver` and is already
used inside `BaseKspSolver::Mult`" to add: "— though it is not currently
exposed on the `BaseKspSolver`/`ComplexKspSolver` public surface
(`ksp.hpp:54-69`), so the materialisation also adds a one-line public
forwarder (parallel to the existing `GetRelTol()` forwarder)."

### Edit 3 (proposed for abstractor reread — Sub-pattern A attribution fix)

In Sub-pattern A's spectrum-target bullet and the citation list, the
per-`WhichType` switch with the `MFEM_ABORT` is attributed to
`ArpackEigenvalueSolver::SetWhichEigenpairs`. It is actually in
`ArpackEigenvalueSolver::SolveInternal` (the `SetWhichEigenpairs` body at
`arpack.cpp:236-239` is a trivial `which_type = type` field-set).
Propose changing the citation annotation from
"`ArpackEigenvalueSolver::SetWhichEigenpairs` body (per-`WhichType` switch
with `MFEM_ABORT` ...)" to "`ArpackEigenvalueSolver::SolveInternal`
per-`WhichType` `::arpack::which` switch (with `MFEM_ABORT` for
unimplemented TARGET_REAL / TARGET_IMAGINARY at ~302-304);
`SetWhichEigenpairs` itself (236-239) only records `which_type`."

(These are proposals for an abstractor reread; not applied by this
audit per role discipline.)

## Supporting evidence

Source files consulted (all via `mcp__palace-codemap__read_range` /
`search_text` against the target repo root):

- `palace/linalg/arpack.cpp` — 236-308 (SetWhichEigenpairs/SetShiftInvert/
  SetInitialSpace/SolveInternal switch), 513-526 (Solve + ncv clamp),
  563-589 (ArpackEPSSolver::ApplyOp), 733-797 (ArpackPEPSolver::ApplyOp).
- `palace/linalg/nleps.cpp` — 500-540 (deflated_solve lambda), 780-806
  (result-construction).
- `palace/linalg/slepc.cpp` — 565-600 (SetWhichEigenpairs), 687-716
  (Solve + GetEigenvalue), 1847-1872 (__pc_apply_EPS), 1942-2000
  (__pc_apply_PEPLinear), 2060-2095 (__pc_apply_PEP), 2125-2170
  (__pc_apply_NEP).
- `palace/linalg/ksp.cpp` — 297-310 (BaseKspSolver::Mult, negative anchor).
- `palace/linalg/ksp.hpp` — 30-72 (BaseKspSolver public surface —
  GetConverged finding).
- `palace/linalg/iterative.hpp` — 98 (IterativeSolver::GetConverged).
- `palace/linalg/eps.hpp` — 57-141 (abstract base setter/accessor surface).
- `palace/drivers/eigensolver.cpp` — 280-340 (driver-side setup).
- `palace/models/modeeigensolver.cpp` — 1020-1054 (backend dispatch).
- `search_text "opInv->Mult"` — exhaustiveness check (exactly 10 hits).

Book cross-references (not re-read this audit; cited by the theme):
- `book/src/L1/eigsolve.md` (LHS), `book/src/L1-L0/ksp-solve-mutation-rotation.md`
  (firm sister), `book/src/L1-L0/apply-linop-mutation-rotation.md` (sister).

## Open questions / caveats

- **Directionality (high→low): PASS.** The theme narrates the rewrite
  forward (L1 `eigsolve` form → L0 `EigenvalueSolver::Solve` + subclass
  bodies). The LHS is L1, the RHS is L0; prose narrates the lowering, not
  the upward lift. No direction-of-definition violation. The
  forward-looking `LinearSolveFailed` materialisation is framed as "what
  the L1>L0 rewrite *would* specify when Palace ships the refactor" —
  this is still a lowering-direction statement (how the L1 status case
  lowers), not an upward-lift narrative. Compliant with the high→low
  invariant.

- **Sub-pattern B promotion verdict (GATED — not enacted this cycle).**
  The partly-constructive shape is **sound** and the audit **unblocks
  promotion** of Sub-pattern B to fully-firm — but the promotion is
  **gated on Edit 2 landing first** and is **not** enacted by this audit.
  The condition (upstream behaviour change required) is real and
  correctly stated; the only defect is that the snippet as written calls
  `GetConverged()` on a type that does not expose it. The required
  sequence is: (1) a **cycle-013 abstractor dispatch** applies the
  GetConverged forwarder correction (Edit 2) to the theme; (2) only then
  is the partly-constructive caveat dropped and the theme promoted to
  fully-firm per the theme's own gate (b). The integrator must NOT
  auto-promote the eigsolve-mutation-rotation theme to firm in the same
  pass that defers the snippet fix. I recommend the cycle-012 meta-phase
  treat this as positive evidence for codifying `partly-constructive` as
  a first-class theme-status (recurrence-2 confirmed: cycle-010 lifter
  recurrence-1, this theme recurrence-2).

- **SLEPc convergence-reason path is richer than the L1 status sum-type.**
  Confirmed `EPSConvergedReasonView` at `slepc.cpp:699` is print-only
  (inside `if (print > 0)`). The SLEPc-side `EPSConvergedReason` enum
  (BREAKDOWN / SYMMETRY_LOST / etc.) is never consumed. The theme's
  deferral of the full reason→`EigStatus` mapping to a future
  `slepc-convergence-reason-lift` sub-theme is appropriate and remains an
  open sub-theme candidate (already an OQ from the abstractor dispatch).
  Not blocking.

- **Spectrum-target mapping inline example understates the branch matrix.**
  `eigensolver.cpp:291-315` has a 2(problem-branch) × backend mapping
  (quadratic/nonlinear/SLP → SMALLEST_IMAGINARY/TARGET_MAGNITUDE/TARGET_IMAGINARY;
  linear-EVP → LARGEST_REAL/TARGET_REAL). The theme's inline Stage-A3
  pseudocode shows only one pair. The cited range covers the full logic
  and the prose labels it "backend-conditional", so this is an
  illustrative-example tightening (not a contradiction). Flagged for the
  abstractor reread but not gating.

- **Per-primitive decomposition of `ApplyOp` bodies deferred.** This
  audit confirmed callsite identity and per-step semantics (matching
  source comments) but did not decompose each `ApplyOp` body into its
  `apply_linop`/`axpy`/`dot` primitive sequence. That decomposition is
  the proper scope of the firm `apply-linop-mutation-rotation` /
  `ksp-solve-mutation-rotation` sister themes the theme delegates to;
  consistent with the theme's stated structural-level coverage. No
  obstruction surfaced at the callsite level.
