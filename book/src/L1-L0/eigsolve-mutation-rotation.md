# eigsolve-mutation-rotation

The mutation rotation for the constructed-operator eigensolve. Lowers the
pure L1 form `eigsolve(E, control) -> EigResult[N, K_max]`
(see [`L1/eigsolve`](../L1/eigsolve.md)) into Palace's in-place
L0 entry `int EigenvalueSolver::Solve()` together with the per-subclass
body (one of `ArpackEigenvalueSolver::Solve` /
`SlepcEPSSolverBase::Solve` / `QuasiNewtonSolver::Solve`) and the per-pair
extraction surface `GetEigenvalue(i) / GetEigenvector(i, x) / GetError(i, t)`.

This is the **second L1>L0 mutation-rotation theme for a structured
opaque primary argument**, after
[`ksp-solve-mutation-rotation`](./ksp-solve-mutation-rotation.md): the
L1 input `E: EigSolver[problem]` is a construction-bound value carrying
the system operators (`K`, `M`, optional `C`, optional `A2(λ)`), the
inner linear solver (`E.linear`), the optional divergence-free projector
(`opProj`), the optional B-matrix, the scaling type, the spectrum target,
the spectral-transformation mode, the requested mode count, the tolerance,
and the iteration cap. The theme decomposes into **four sub-patterns** —
backend setup (A), inner-solve mutation-rotation (B), result-status flow
(C), and teardown (D) — mirroring the four-sub-concern shape of
`ksp-solve-mutation-rotation`'s outer `BaseKspSolver::Mult` body, but
elaborated for the eigensolver's substantially larger variant landscape
(three backend orchestrations × nine spectrum targets × two spectral
transformations × three problem types).

## Slug

`eigsolve-mutation-rotation`

## L1 form (LHS)

The pure-functional eigensolve ([`L1/eigsolve`](../L1/eigsolve.md)):

    result = eigsolve(E, control)          -- result : EigResult[N, K_max]

    EigControl = {
      initial_space : Maybe (Tensor[N, complex])
    }

    EigResult[N, K_max] = {
      eigenvalues   : Tensor[K, complex],
      eigenvectors  : Tensor[K, N, complex],
      converged     : Int,
      requested     : Int,
      error         : Tensor[K, real],
      scaling_gamma : Real,
      scaling_delta : Real,
      status        : EigStatus
    }

    EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed

`E : EigSolver[problem]` is a construction-bound, opaque eigensolver value
whose internal orchestration (RCI / shell-matrix / direct-Newton), specific
solver library (ARPACK / SLEPc / Palace's own `QuasiNewtonSolver`),
spectrum-target, spectral-transformation mode, scaling type, problem-type
phantom (`Linear[K, M]` / `Quadratic[K, C, M]` / `Nonlinear[K, M, A2]`),
and convergence-control parameters are all bound at construction. The
per-call signature is variant-free over the orchestration axis; only
`(E, control)` enters and only `EigResult[N, K_max]` leaves. The
`LinearSolveFailed` variant of `EigStatus` is **L1-constructive** — see
Sub-pattern C below for the constructive-introduction treatment in the rewrite.

## L0 form (RHS)

The rewrite is layered: an outer composition rewrite at
`EigenvalueSolver::Solve()` plus a per-subclass body rewrite, each with
its own setup, inner-loop coupling, result mapping, and teardown phases.
The four sub-patterns A–D below are orthogonal to the backend axis (each
applies to each of the three backend orchestrations), with backend-specific
elaborations recorded per sub-pattern.

### Sub-pattern A — setup (backend selection + spectral-transformation + spectrum target)

The L1 `E` opaque construction binds at L0 to a specific
`EigenvalueSolver` subclass instance, configured through a sequence of
setter calls before any `Solve()` invocation. The driver-side setup
appears as a five-stage composition at `palace/drivers/eigensolver.cpp`
and `palace/models/modeeigensolver.cpp:1020-1054`:

```cpp
// Stage A1: backend selection (modeeigensolver.cpp:1030-1053)
if (type == EigenSolverBackend::ARPACK) {
  auto arpack = std::make_unique<arpack::ArpackEPSSolver>(comm, print);
  // ...
  eigen = std::move(arpack);
} else {  // EigenSolverBackend::SLEPC
  auto slepc = std::make_unique<slepc::SlepcEPSSolver>(comm, print);
  slepc->SetType(slepc::SlepcEigenvalueSolver::Type::KRYLOVSCHUR);
  slepc->SetProblemType(slepc::SlepcEigenvalueSolver::ProblemType::GEN_NON_HERMITIAN);
  // ...
  eigen = std::move(slepc);
}

// Stage A2: spectral-transformation (eigensolver.cpp:285, 305)
eigen->SetShiftInvert(1i * target);          // shift-invert mode (quadratic / nonlinear)
//   or
eigen->SetShiftInvert(target * target);      // shift-invert mode (linear EVP, μ = ω²)

// Stage A3: spectrum target (eigensolver.cpp:291-315, backend-conditional)
if (type == EigenSolverBackend::ARPACK) {
  eigen->SetWhichEigenpairs(EigenvalueSolver::WhichType::SMALLEST_IMAGINARY);  // shifted-problem target
} else {
  eigen->SetWhichEigenpairs(EigenvalueSolver::WhichType::TARGET_IMAGINARY);    // original-problem target
}

// Stage A4: inner linear solver binding (eigensolver.cpp:330-334)
eigen->SetLinearSolver(*ksp);                // bind ComplexKspSolver

// Stage A5: operator binding (modeeigensolver.cpp:470; driver-side overloads at eigensolver.cpp:177, 185, 189, 193)
eigen->SetOperators(*opB, *opA, EigenvalueSolver::ScaleType::NONE);
```

Five L0 surface concerns absorb at L1, each rewriting distinctly:

- **Backend selection (Stage A1)** — the choice between ARPACK and SLEPc
  (and, for nonlinear problems, between `SlepcNEPSolver` and
  `QuasiNewtonSolver`) is a build-time-vs-run-time stratification: a
  build-time check (`#if defined(PALACE_WITH_ARPACK)`) determines
  availability; a runtime flag (`type == EigenSolverBackend::ARPACK`)
  selects between available backends. At L1 the backend is **absorbed
  into `E`'s opaque type** — the L1 contract sees only the constructed
  eigensolver and its convergence semantics; the orchestration axis
  (RCI / shell-matrix / direct-Newton) is not visible. This parallels
  `ksp_solve`'s collapse of CG / GMRES / FGMRES.
- **Shift-invert spectral transformation (Stage A2)** — at L0,
  `SetShiftInvert(σ)` binds a shift `σ` and toggles a `sinvert = true`
  flag on the subclass (e.g., `palace/linalg/arpack.cpp:241-247`). The
  effect is that subsequent `ApplyOp` callbacks compute
  `(K − σM)⁻¹` (or `P(σ)⁻¹` for polynomial) rather than `M⁻¹`. At L1
  the spectral transformation is a construction-bound parameter on `E`
  (`E.shift = Just σ` or `Nothing`); the L1>L0 rewrite reinstantiates
  it as the `SetShiftInvert` setter call plus the eventual `ApplyOp`
  branch on `sinvert`.
- **Spectrum target (Stage A3)** — the `WhichType` nine-way enum maps
  per-backend to backend-specific tokens (ARPACK's
  `::arpack::which::largest_real`, SLEPc's `EPS_LARGEST_REAL`, etc.).
  At L1 the spectrum target is a construction-bound parameter on `E`;
  the L1>L0 rewrite is the `SetWhichEigenpairs` setter call with the
  per-backend mapping. For ARPACK, `SetWhichEigenpairs`
  (`palace/linalg/arpack.cpp:236-239`) is a **trivial field-set**
  (`which_type = type;`); the actual per-`WhichType` token mapping —
  the `switch (which_type)` including the `MFEM_ABORT` for `TARGET_REAL`
  / `TARGET_IMAGINARY` — lives in `SolveInternal` at
  `palace/linalg/arpack.cpp:279-305`. For SLEPc the per-`WhichType`
  switch is in `SetWhichEigenpairs` itself
  (`palace/linalg/slepc.cpp:565-600`), an asymmetry vs ARPACK.
  **Recognition note**: the `(ARPACK, TARGET_REAL)` and
  `(ARPACK, TARGET_IMAGINARY)` pairs are *unimplemented stubs* per the
  ARPACK `MFEM_ABORT` at `palace/linalg/arpack.cpp:301-304`; per
  CLAUDE.md "Unimplemented Palace stub policy" the L1 form treats
  these as constructor-time validity constraints — a `K`-construction
  attempting `ARPACK × TARGET_REAL` is ill-formed; the L1>L0 rewrite
  does **not** materialise this case.
- **Inner linear solver binding (Stage A4)** — `SetLinearSolver(*ksp)`
  binds the construction-side `ComplexKspSolver` as the
  shift-invert / generalized inverse provider (`opInv` in the subclass
  bodies). The L1 `E.linear : Solver[A]` field is the L1 mirror of
  this binding; the L1>L0 rewrite is the `SetLinearSolver` setter
  call. The L1 inner-solver value composes against `eigsolve` per the
  composed-not-inherited pattern; see
  [`L1/eigsolve`](../L1/eigsolve.md) Dependencies §`ksp_solve`.
- **Operator binding (Stage A5)** — the three `SetOperators` overloads
  on `EigenvalueSolver` (`palace/linalg/eps.hpp:57-74`, each defaulting
  to `MFEM_ABORT` so concrete subclasses opt in) dispatch on the
  problem-type tag (linear `K, M` / quadratic `K, C, M` / nonlinear
  `K, M, A2(λ)`). At L1 the operator bindings are construction-bound
  fields on `E` constrained by the `problem` phantom; the L1>L0
  rewrite is the appropriate `SetOperators` setter call. The
  `ScaleType` argument to `SetOperators` is the source of the
  load-bearing Higham scaling factors (`gamma`, `delta`) that the
  per-pair extraction surface returns; see Algebraic-laws §5 on the
  L1 entry.

Justification kind: **structural** — the five-stage setup is a
straight-line composition; each stage rewrites by re-binding the L1
construction parameter into the corresponding L0 setter call.

Citations:
- `palace/linalg/eps.hpp:22-141` — `EigenvalueSolver` abstract base
  (the full surface the setters drive).
- `palace/linalg/eps.hpp:57-74` — three `SetOperators` overloads with
  `MFEM_ABORT` defaults.
- `palace/linalg/eps.hpp:116-119` — `SetWhichEigenpairs` /
  `SetShiftInvert` setters.
- `palace/linalg/arpack.cpp:236-239` — `ArpackEigenvalueSolver::SetWhichEigenpairs`
  body (trivial field-set `which_type = type;`).
- `palace/linalg/arpack.cpp:279-305` — `ArpackEigenvalueSolver::SolveInternal`
  per-`WhichType` `switch` (the actual ARPACK-token mapping, with
  `MFEM_ABORT` for unimplemented TARGET_REAL / TARGET_IMAGINARY at
  `301-304`).
- `palace/linalg/arpack.cpp:241-247` —
  `ArpackEigenvalueSolver::SetShiftInvert` body (binds `sigma`, sets
  `sinvert = true`; rejects `precond = true`).
- `palace/linalg/slepc.cpp:565-600` —
  `SlepcEPSSolverBase::SetWhichEigenpairs` body (nine-way switch with
  SLEPc EPS token mapping).
- `palace/linalg/slepc.cpp:379` — `SlepcEigenvalueSolver::SetShiftInvert`.
- `palace/drivers/eigensolver.cpp:280-330` — driver-side setup
  composition (shift-invert + which-eigenpairs + linear solver
  binding).
- `palace/models/modeeigensolver.cpp:1020-1054` — backend dispatch site
  (ARPACK vs SLEPc construction; calls SetNumModes, SetTol,
  SetWhichEigenpairs, SetLinearSolver).
- `palace/models/modeeigensolver.cpp:470` — `SetOperators` call site
  for the eigenmode pipeline (linear EVP, (opB, opA) binding).
- `palace/drivers/eigensolver.cpp:177, 185, 189, 193` — driver-side
  `SetOperators` callsites covering the four problem-type branches
  (SLP nonlinear, quadratic-with-A2-scale, quadratic-without-A2, linear).

### Sub-pattern B — inner-solve mutation-rotation (the `opInv->Mult` couplings)

This is the **core sub-pattern** of the theme: the L1 `E.linear` inner
solver's involvement in the eigensolver iteration. The L0 source has
**ten `opInv->Mult(b, x)` call sites** across three orchestration
families, each invoking
`BaseKspSolver<ComplexOperator>::Mult(const VecType &b, VecType &x) const`
(`palace/linalg/ksp.cpp:297-310`) — the firm L1>L0
[`ksp-solve-mutation-rotation`](./ksp-solve-mutation-rotation.md)
sub-pattern A outer body. The ten call sites are:

**ARPACK (4 sites)**:
- `palace/linalg/arpack.cpp:574` — `ArpackEPSSolver::ApplyOp` non-sinvert
  branch (after `opK->Mult(x1, z1)`; computes `y = M⁻¹ K x`).
- `palace/linalg/arpack.cpp:580` — `ArpackEPSSolver::ApplyOp` sinvert
  branch (after `opM->Mult(x1, z1)`; computes `y = (K − σM)⁻¹ M x`).
- `palace/linalg/arpack.cpp:761` — `ArpackPEPSolver::ApplyOp` non-sinvert
  branch (PEP linearised problem; computes `y₂ = M⁻¹ K x₁` component).
- `palace/linalg/arpack.cpp:778` — `ArpackPEPSolver::ApplyOp` sinvert
  branch (PEP shift-invert; computes `(L₀ − σL₁)⁻¹` component).

**NLEPS (1 site)**:
- `palace/linalg/nleps.cpp:514` — `QuasiNewtonSolver::Solve`'s
  inline-lambda `deflated_solve` (the inner Newton-step linear solve;
  `opInv->Mult(b1, x1)` computes `x₁ = T(σ)⁻¹ b₁`).

**SLEPc shell-matrix callbacks (5 sites)**:
- `palace/linalg/slepc.cpp:1858` — `__pc_apply_EPS` (PETSc shell PC
  callback for linear EPS; `y = M⁻¹ x` or `(K − σM)⁻¹ x`).
- `palace/linalg/slepc.cpp:1965` — `__pc_apply_PEPLinear` non-sinvert
  branch (PEP via L₁ linearisation; `y₂ = M⁻¹ x₂`).
- `palace/linalg/slepc.cpp:1978` — `__pc_apply_PEPLinear` sinvert branch
  (`(L₀ − σL₁)⁻¹ x`).
- `palace/linalg/slepc.cpp:2076` — `__pc_apply_PEP` (direct quadratic
  PEP shell PC; `y = M⁻¹ x` or `P(σ)⁻¹ x`).
- `palace/linalg/slepc.cpp:2159` — `__pc_apply_NEP` (NEP shell PC; per-λ
  preconditioner update + `opInv->Mult`).

Each `opInv->Mult(b, x)` rewrites by the firm
[`ksp-solve-mutation-rotation`](./ksp-solve-mutation-rotation.md) theme
(sub-pattern A outer composition). At L1 the eigensolver iteration's
per-step inner solve appears as a `ksp_solve(E.linear, b)` call inside
the opaque eigensolver body; the L1 form does not expose the per-step
inner-solve count, but transitively inherits the inner solver's
non-determinism (per [`L1/eigsolve`](../L1/eigsolve.md) Semantics §"third
load-bearing non-determinism axis").

**The `LinearSolveFailed` constructive-introduction at this sub-pattern.**
Each of the ten `opInv->Mult` callsites discards the inner solver's
convergence status — `BaseKspSolver<ComplexOperator>::Mult` has a `void`
return (`palace/linalg/ksp.cpp:297`) and emits only an `Mpi::Warning` on
`!ksp->GetConverged()` (lines 301-307). **None** of the ten callsites
query `ksp->GetConverged()` after the call. The L1 `EigStatus::LinearSolveFailed`
variant has therefore no direct L0 anchor at this sub-pattern — it is
constructively introduced by the L1 form (see
[`L1/eigsolve`](../L1/eigsolve.md) §Signature callout).

The materialisation that the L1>L0 lowering would specify (when Palace
ships the refactor) consists of two upstream changes: a one-line
accessor on `BaseKspSolver` plus a status-capture at each callsite.

**Accessor prerequisite (the snippet's load-bearing correction).**
`GetConverged()` is **not** callable on `opInv`'s type. `opInv` is a
`BaseKspSolver<ComplexOperator>` whose public surface
(`palace/linalg/ksp.hpp:50-71`) exposes only `NumTotalMult`,
`NumTotalMultIterations`, the `GetRelTol` / `GetAbsTol` / `SetRelTol` /
`SetAbsTol` tolerance forwarders, `SetOperators`, and `Mult`. The
convergence flag lives on `IterativeSolver::GetConverged`
(`palace/linalg/iterative.hpp:98`), reachable only through the
**protected** `ksp` member (`palace/linalg/ksp.hpp:41`). So the
materialisation first needs **either** a one-line public forwarder on
`BaseKspSolver`, mirroring the existing `GetRelTol` accessor
(`palace/linalg/ksp.hpp:64` — `double GetRelTol() const { return
ksp->GetRelTol(); }`), **or** a `Mult` status-return:

```text
// Prerequisite (option 1): a one-line public forwarder on BaseKspSolver,
//   added next to the existing GetRelTol forwarder (ksp.hpp:64):
bool GetConverged() const { return ksp->GetConverged(); }

// Prerequisite (option 2, alternative): give Mult a status return
//   (changes the void signature at ksp.cpp:297 — larger surface change).
bool Mult(const VecType &b, VecType &x) const;   // returns ksp->GetConverged()
```

```text
// Before (current Palace; status silently dropped):
opInv->Mult(b, x);              // void return; warning logged only

// After (L1-constructive materialisation; not yet in Palace source).
//   Assumes the option-1 forwarder above is present:
opInv->Mult(b, x);
if (!opInv->GetConverged()) {   // <- the new public forwarder
  inner_failed = true;          // capture per-step inner failure
  break;                        // bubble out of the eigensolver outer loop
}
// Plus, at the eigensolver outer loop terminator:
//   if (inner_failed) return LinearSolveFailed;
//   else if (num_conv == nev) return Converged;
//   else if (num_conv > 0)   return PartialConverged;
//   else                     return MaxIterReached;
```

The materialisation is a **forward-looking reconstruction**: the L1 form
names a status case the current L0 surface does not produce. The shape
is nonetheless well-defined and the upstream behaviour change is
mechanical and small — `IterativeSolver::GetConverged`
(`palace/linalg/iterative.hpp:98`) already exists and is already used
inside `BaseKspSolver::Mult` to guard the warning emission
(`palace/linalg/ksp.cpp:301-307`); the only missing piece on the public
surface is the one-line forwarder (or the `Mult` status-return). The
L1>L0 theme records this as a **rewriting requires upstream behaviour
change** note; the rewrite
shape is recorded forward-looking, with the current L0 surface noted as
silent-on-this-case. This reconstruction is grounded in the
negative anchor `palace/linalg/ksp.cpp:297-310` (the `void` return) —
the negative anchor is evidence FOR the faithful reconstruction, not a
positive claim that Palace produces the status today.

For the SLEPc shell-matrix path, the materialisation has an additional
elaboration: SLEPc internally exposes `EPSConvergedReason` via
`EPSConvergedReasonView` (`palace/linalg/slepc.cpp:699` — currently
*print-only*, never queried). The materialisation here would consume
the reason code and map the `EPS_DIVERGED_BREAKDOWN` /
`EPS_DIVERGED_SYMMETRY_LOST` family to `LinearSolveFailed` (rather than
collapsing all SLEPc-side diverged reasons into `MaxIterReached`).
The full `EPSConvergedReason` -> `EigStatus` mapping — across all three
SLEPc solver families (EPS / PEP / NEP), with the converged/diverged
partition and per-row reconstruction notes — is carried in the sibling
sub-theme
[`eigsolve-convergence-reason-mapping`](./eigsolve-convergence-reason-mapping.md)
(`partly-constructive`, gated downstream of this Sub-pattern B).

Justification kind: **structural** with embedded reduction-chain
sub-rewrites. The ten callsites are structural (each binds to the firm
`ksp-solve-mutation-rotation` sub-pattern A); the constructive
`LinearSolveFailed` annotation is a reduction-chain claim (negative-anchor
evidence pattern). The per-pattern rewrites delegate to the firm sister theme.

Citations:
- `palace/linalg/ksp.cpp:297-310` — `BaseKspSolver<OperType>::Mult` body
  (the firm `ksp-solve-mutation-rotation` sub-pattern A target). Void
  return + `Mpi::Warning` on non-convergence. Negative anchor for
  `LinearSolveFailed` constructive-introduction.
- `palace/linalg/arpack.cpp:563-589` — `ArpackEPSSolver::ApplyOp` body
  (host-pointer convention; `opInv->Mult` at lines 574 and 580).
- `palace/linalg/arpack.cpp:733-797` — `ArpackPEPSolver::ApplyOp` body
  (PEP linearisation; `opInv->Mult` at lines 761 and 778).
- `palace/linalg/nleps.cpp:500-540` — `QuasiNewtonSolver::Solve`'s
  `deflated_solve` lambda (block linear system; `opInv->Mult` at line
  514).
- `palace/linalg/slepc.cpp:1847-1872` — `__pc_apply_EPS` body
  (`opInv->Mult` at line 1858).
- `palace/linalg/slepc.cpp:1942-2000` — `__pc_apply_PEPLinear` body
  (`opInv->Mult` at lines 1965 and 1978).
- `palace/linalg/slepc.cpp:2060-2095` — `__pc_apply_PEP` body
  (`opInv->Mult` at line 2076).
- `palace/linalg/slepc.cpp:2125-2170` — `__pc_apply_NEP` body
  (per-λ preconditioner update at lines 2140-2158 plus `opInv->Mult` at
  line 2159).
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` — the firm sister
  theme that each `opInv->Mult` callsite rewrites by.

### Sub-pattern C — result-status flow (`int` count → `EigResult` record)

The L0 `Solve()` virtual returns `int` (the converged-pair count) and
deposits per-pair data in solver-internal arrays accessed via three
per-pair accessor virtuals (`GetEigenvalue(i)`, `GetEigenvector(i, x)`,
`GetError(i, type)`). The L1 form structures this into a single
`EigResult` record. Four L0 surface concerns rewrite distinctly:

- **Convergence-count return → `EigResult.converged` field** — the
  `Solve()` `int` return is a positive count that can be strictly less
  than the requested `K_max` without being an outright failure
  (`palace/drivers/eigensolver.cpp:367-374` formats
  `" Found {:d} converged eigenvalue{}{}\n"` using the count as-returned,
  no error). At L1, the count is structured as `result.converged : Int`
  alongside `result.requested : Int`; the comparison the L0 callers
  perform implicitly (count vs request) is hoisted into `result.status`
  via the `Converged | PartialConverged | MaxIterReached`
  three-way discrimination.
- **Per-pair extraction via three accessor virtuals →
  `EigResult.{eigenvalues, eigenvectors, error}` tensors** — at L0 the
  caller invokes `GetEigenvalue(i)`, `GetEigenvector(i, x)` (writing
  into out-parameter), and `GetError(i, type)` in a loop indexed by
  `i ∈ [0, num_conv)`. At L1 the three tensors are populated together
  as part of the `EigResult` construction. The rewrite reads:

  ```text
  // L0 (caller-side, after Solve() returns num_conv):
  for (int i = 0; i < num_conv; i++) {
    auto lambda = eigen->GetEigenvalue(i);
    ComplexVector x_i;
    eigen->GetEigenvector(i, x_i);
    double err = eigen->GetError(i, EigenvalueSolver::ErrorType::ABSOLUTE);
    // ... consume per-pair ...
  }

  // L1 (eigsolve-internal):
  result.eigenvalues  = stack [eigen.GetEigenvalue(i) for i in 0..num_conv]
  result.eigenvectors = stack [eigen.GetEigenvector(i)  for i in 0..num_conv]
  result.error        = stack [eigen.GetError(i, abs)   for i in 0..num_conv]
  ```

  The destination-buffer for `GetEigenvector(i, x)` (the out-parameter `x`)
  binds to the per-pair slice of `result.eigenvectors`; this is the same
  destination-binding pattern as
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
  sub-pattern A, applied once per pair.

- **Status sum-type derivation from L0 count semantics —
  `EigResult.status`** — the three L0-observable cases (`num_conv ==
  K_max`, `0 < num_conv < K_max`, `num_conv == 0`) map directly to
  `Converged | PartialConverged | MaxIterReached`. The
  fourth `LinearSolveFailed` variant is **L1-constructive** (per
  Sub-pattern B); current L0 instantiations of `eigsolve` will produce
  only the three observable variants. The L1>L0 rewrite for the three
  observable variants is:

  ```text
  match num_conv with
  | n when n == E.K_max -> Converged
  | n when n > 0        -> PartialConverged
  | _                   -> MaxIterReached
  ```

  When (and only when) the Sub-pattern B materialisation lands, the
  rewrite extends to:

  ```text
  if inner_failed then LinearSolveFailed
  else (match num_conv with ...)
  ```

- **Higham scaling factors → `EigResult.scaling_gamma` /
  `EigResult.scaling_delta`** — at L0 the scaling factors are exposed via
  `GetScalingGamma()` / `GetScalingDelta()` accessors
  (`palace/linalg/eps.hpp:102-103`); at L1 they are populated into the
  `EigResult` fields. **Open question**: whether L1 should un-scale at
  the result-extraction boundary (so `result.eigenvalues` are in the
  original coordinate system regardless of `E.ScaleType`) is a sibling
  OQ (`eigsolve-scaling-coordinate-convention`); out of scope
  for this theme. The current rewrite preserves the L0 convention — the
  L0 `SlepcEPSSolverBase::GetEigenvalue` at
  `palace/linalg/slepc.cpp:711-716` returns `l * gamma`, indicating
  un-scaling is performed at the accessor; the L1 form mirrors this.

- **Side-channel emissions absorbed at L1** — the L0 `Mpi::Print`
  convergence-summary log lines
  (`palace/linalg/slepc.cpp:696-704` printing solver-reason +
  total-linear-systems + total-linear-iterations; analogous at
  `palace/linalg/arpack.cpp:344-351`) and the driver-side
  `BlockTimer bt1(Timer::EPS)` RAII wrap at
  `palace/drivers/eigensolver.cpp:365` are **transparent
  performance/instrumentation concerns** with no L1 semantic content.
  At L1 they erase entirely. The driver-side cumulative inner-solver
  counters (`opInv->NumTotalMult()`,
  `opInv->NumTotalMultIterations()`) are driver-side accumulators
  over the inner solver's per-call statistics; reconstructing them
  is `(E.linear.cumulative_calls,
  E.linear.cumulative_iters)` outside the L1 operator.

Justification kind: **structural** (per-pair extraction rewrite + status
sum-type derivation + Higham-scaling-factor passthrough), with the
`LinearSolveFailed` branch deferring to Sub-pattern B's
partly-constructive materialisation.

Citations:
- `palace/linalg/eps.hpp:124-140` — `Solve()`, `GetEigenvalue`,
  `GetEigenvector`, `GetError`, `RescaleEigenvectors` per-pair
  extraction surface.
- `palace/linalg/eps.hpp:102-103` — `GetScalingGamma` /
  `GetScalingDelta` accessors.
- `palace/linalg/arpack.cpp:513-560` — `ArpackEPSSolver::Solve()` body;
  `SolveInternal` invocation at line 552; `RescaleEigenvectors(nev)` at
  line 555; `return num_conv` at line 559.
- `palace/linalg/arpack.cpp:344-351` — ARPACK `Mpi::Print` convergence
  summary (eigenpair count, iterations, total linear systems /
  iterations).
- `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve()`
  body; `EPSSolve` + `EPSGetConverged` at lines 694-695; convergence
  summary at 696-704; `RescaleEigenvectors(num_conv)` at 707;
  `return (int)num_conv` at 708.
- `palace/linalg/slepc.cpp:711-716` —
  `SlepcEPSSolverBase::GetEigenvalue(i)` returning `l * gamma` (Higham
  un-scaling at the accessor).
- `palace/linalg/nleps.cpp:780-806` — `QuasiNewtonSolver::Solve`
  result-construction body (eigenvalue / eigenvector accumulation;
  permutation sort by imag; `RescaleEigenvectors`; `return nev`).
- `palace/drivers/eigensolver.cpp:365-374` — driver-side outer
  composition (BlockTimer + `eigen->Solve()` + `Mpi::Print` of count).
- `palace/models/modeeigensolver.cpp:484-492` — driver-side
  eigenvalue re-sort by shift-target distance (out-of-scope at L1; L1
  `EigResult.eigenvalues` ordering is per the L0 backend convention,
  not sorted).
- `book/src/L1/eigsolve.md` — §Signature for the `EigResult` record
  field-by-field mapping.

### Sub-pattern D — teardown (spectral-transformation reset + workspace lifecycle)

After `Solve()` returns, three teardown concerns absorb at L1:

- **Internal state reset for next solve** — `ArpackEigenvalueSolver::Solve`
  at `palace/linalg/arpack.cpp:558` resets `info = 0` to clear the
  initial-space marker for the next call. `SlepcEPSSolverBase::Solve`
  does not reset internal state (SLEPc owns the EPS object lifetime
  internally). At L1 this state-reset is **absorbed into `E`'s opaque
  lifetime** — the L1 form is referentially transparent: calling
  `eigsolve(E, control)` twice with the same arguments produces (modulo
  non-determinism) the same result; the L0 reset is the mechanism that
  realises this property.
- **Workspace tensor lifecycle** — the `mutable ComplexVector x1, y1,
  z1` workspace on `ArpackEPSSolver` (and analogous on SLEPc /
  `NonLinearEigenvalueSolver`) backs the per-`ApplyOp` callbacks
  invoked from the RCI loop / shell-matrix callbacks / Newton inner
  loop. The workspace is allocated lazily on first `SetOperators` call
  and reused across `Solve()` invocations. At L1 the workspace is
  erased per the [`mutable workspace
  pattern`](../L0/mutable-workspace-pattern.md) L0 convention; the L1
  form does not expose intermediate buffers.
- **Spectral-transformation lifecycle** — when `SetShiftInvert(σ)`
  binds a shift, the inner `opInv` is reconfigured (per
  `palace/linalg/slepc.cpp:2140-2158` for the NEP per-λ
  preconditioner-update branch). Subsequent `Solve()` calls with a
  different shift would require a re-`SetShiftInvert` (and, for NEP,
  the per-λ refactor of `opA_pc` and `opP_pc`). At L1 the shift is
  construction-bound on `E`, so changing the shift means constructing a
  new `E`; the L1 form does not expose the per-call shift mutation
  surface.

Justification kind: **structural** (state-reset, workspace, and
spectral-transformation lifecycle are absorption-into-`E` rewrites; none
of them carry L1-visible semantic content).

Citations:
- `palace/linalg/arpack.cpp:558` — `info = 0` reset for next solve.
- `palace/linalg/arpack.cpp:617-628` —
  `ArpackPEPSolver::SetOperators` workspace setup (canonical lazy
  allocation point for `mutable ComplexVector` workspace).
- `palace/linalg/slepc.cpp:2140-2158` — NEP per-λ preconditioner
  reconfiguration inside `__pc_apply_NEP` (the spectral-transformation
  lifecycle branch the L1 form absorbs).
- `book/src/L0/mutable-workspace-pattern.md` — the workspace-erase L0
  convention this sub-pattern cites once and does not re-state.

## Applicability conditions

For all four sub-patterns the rewrite preserves semantics when:

1. **`E`'s bound backend is one of ARPACK / SLEPc / `QuasiNewtonSolver`.**
   The recognition set is exhaustive over Palace's `EigenvalueSolver`
   subclass families — these are the only three concrete subclass
   families in the corpus (`ArpackEigenvalueSolver`,
   `SlepcEigenvalueSolver`, `NonLinearEigenvalueSolver::QuasiNewtonSolver`).
   For ARPACK, the `(TARGET_REAL, TARGET_IMAGINARY)` spectrum-target
   pairs are unimplemented stubs (`palace/linalg/arpack.cpp:300-304`);
   per CLAUDE.md "Unimplemented Palace stub policy" these are
   constructor-time validity constraints on `E`, not recognition-set
   members.

2. **No aliasing between `result.eigenvectors[i]` slice and any input
   buffer.** Sub-pattern C's per-pair extraction writes through
   `GetEigenvector(i, x)`'s out-parameter; if the caller arranges aliasing
   between the destination and any input buffer (e.g., the workspace
   tensors on the solver), behaviour is undefined. Palace never aliases
   `GetEigenvector` arguments in observed sites; this is an applicability
   condition, not a known failure.

3. **`E.linear`'s bound system operator matches the spectral-transformation
   shape.** When `E.shift = Just σ`, the inner `E.linear` must be
   configured against `(K − σM)` (linear case) or `P(σ)` (polynomial /
   nonlinear case); this is the L0 caller's obligation
   (`palace/drivers/eigensolver.cpp:326-334` shows the driver building
   `A` against `(K + iσ C − σ² M + A2)` and binding it to `*ksp` before
   passing to `eigen->SetLinearSolver`). At L1 this is a precondition on
   `E`'s opaque type — the `E.linear` field's bound system operator
   matches `E.shift` per construction.

4. **`E.K_max ≤ N`.** The requested mode count cannot exceed the
   operator dimension; `palace/linalg/arpack.cpp:518-521` clamps
   `ncv` (ARPACK's basis-size parameter) against the global dimension
   `N` (fetched via `N = linalg::GlobalSize(...)` at
   `palace/linalg/arpack.cpp:517`; the `arpack_it` default is set
   immediately after at `522-525`). At L1 this is a precondition on
   `E`'s opaque type.

5. **Single-rank scope.** Per CLAUDE.md "Scope", the L1 form is
   single-rank; the MPI surface (`ParMesh` distributions,
   `Mpi::GlobalSum` reductions inside `linalg::Dot` /
   `linalg::Norml2`) lifts to the L1>L0 rewrite at the
   `apply_linop` / `dot` / `nrm2` sister-theme level. The
   `eigsolve-mutation-rotation` theme itself is MPI-transparent.

6. **`LinearSolveFailed` materialisation requires upstream behaviour
   change.** Per Sub-pattern B's constructive-introduction treatment,
   the rewrite that produces `LinearSolveFailed` is **partly-constructive**:
   current Palace L0 surface does not produce it; the rewrite shape is
   recorded forward-looking. Applicability is conditional on either
   (a) a future Palace refactor capturing `ksp->GetConverged()` at the
   ten `opInv->Mult` callsites, or (b) a caller-side wrap that captures
   the inner-solver state externally. The current L1 form treats this
   case as not-yet-materialised; the rewrite reduces to the three
   observable variants until the refactor lands.

## Justification kind

- **Sub-pattern A (setup)** — `structural`. The five-stage setter
  composition is straight-line; each stage rewrites by re-binding an L1
  construction parameter into the corresponding L0 setter call.
- **Sub-pattern B (inner-solve mutation-rotation)** — `structural`
  with embedded `reduction-chain` sub-rewrites. The ten `opInv->Mult`
  callsites each rewrite by the firm
  [`ksp-solve-mutation-rotation`](./ksp-solve-mutation-rotation.md)
  theme; the `LinearSolveFailed` annotation is a reduction-chain
  claim grounded in the negative-anchor evidence pattern.
- **Sub-pattern C (result-status flow)** — `structural`. The
  per-pair extraction rewrite + status sum-type derivation + Higham
  scaling-factor passthrough are all destination-binding /
  field-population structural rewrites, with the
  `LinearSolveFailed` branch deferring to Sub-pattern B's
  partly-constructive materialisation.
- **Sub-pattern D (teardown)** — `structural`. State-reset,
  workspace, and spectral-transformation lifecycle are
  absorption-into-`E` rewrites with no L1-visible semantic content.

The theme as a whole is `structural`. Sub-pattern B's
`LinearSolveFailed` materialisation is a **forward-looking
reconstruction** (the L0 surface does not currently produce the
variant; the rewrite shape is recorded forward-looking, grounded in
the negative anchor `palace/linalg/ksp.cpp:297-310`); this is a
permanent property of the rewrite, not an open status gate. Sub-pattern
recognition is exhaustive over the eigensolver L0 corpus, specifically that:

- (i) the four-stage setup absorption (Sub-pattern A) is consistent with
  the per-backend `SetType` / `SetProblemType` / `SetExtraSystemMatrix` /
  `SetPreconditionerUpdate` sub-axis bindings the
  driver-side composition uses;
- (ii) the ten `opInv->Mult` callsites are exhaustive across the
  Palace corpus (there are no other eigensolver-side callsites);
- (iii) the per-pair extraction rewrite (Sub-pattern C) is
  consistent across the three backend orchestrations (each backend's
  `GetEigenvalue`, `GetEigenvector`, `GetError` returns values in
  the same coordinate convention modulo the Higham scaling factor).

## Speculative L1 operators

**None.**

The theme decomposes into existing firm L1 vocabulary:
[`eigsolve`](../L1/eigsolve.md) (the LHS),
[`ksp_solve`](../L1/ksp_solve.md) (the inner solver per Sub-pattern B),
[`apply_linop`](../L1/apply_linop.md) (per-step
`opK->Mult`, `opM->Mult`, `opC->Mult` callsites inside the `ApplyOp`
bodies), and transitively
[`dot`](../L1/dot.md) / [`nrm2`](../L1/nrm2.md) /
[`axpy`](../L1/axpy.md) / [`axpby`](../L1/axpby.md).

No new L1 operators are speculated. The `LinearSolveFailed`
constructive-introduction is **internal to the existing `eigsolve` L1
form** (the `EigStatus` sum type already has the variant); the theme
materialises the lowering of this case, not a new operator.

This is the same structural property as `ksp-solve-mutation-rotation`'s
"no speculative operators" verdict: when the L1 form is the firm
cohort's gate point (`eigsolve` as the constructed-eigensolver gate;
`ksp_solve` as the constructed-linear-solver gate), the variant-axis
collapse design lets the L1>L0 lowering operate entirely within
existing L1 vocabulary.

## Evidence

L0 evidence ranges:

- `palace/linalg/ksp.cpp:297-310` — `BaseKspSolver<OperType>::Mult`
  body (void return, Mpi::Warning, counter mutations). The firm
  `ksp-solve-mutation-rotation` outer composition target; the negative
  anchor for `LinearSolveFailed` constructive-introduction.
- `palace/linalg/eps.hpp:22-141` — `EigenvalueSolver` abstract base
  class (full surface; 22 virtuals).
- `palace/linalg/eps.hpp:57-74` — three `SetOperators` overloads with
  `MFEM_ABORT` defaults (problem-type axis dispatch).
- `palace/linalg/eps.hpp:102-103` — Higham scaling-factor accessors.
- `palace/linalg/eps.hpp:116-132` — `SetWhichEigenpairs`,
  `SetShiftInvert`, `SetInitialSpace`, `Solve`, `GetEigenvalue`,
  `GetEigenvector`, `GetError`, `RescaleEigenvectors` surface.
- `palace/linalg/arpack.cpp:236-308` —
  `ArpackEigenvalueSolver::SetWhichEigenpairs` body (per-`WhichType`
  switch with `MFEM_ABORT` for unimplemented TARGET_REAL /
  TARGET_IMAGINARY at 300-304).
- `palace/linalg/arpack.cpp:241-247` —
  `ArpackEigenvalueSolver::SetShiftInvert` body.
- `palace/linalg/arpack.cpp:249-260` —
  `ArpackEigenvalueSolver::SetInitialSpace` body.
- `palace/linalg/arpack.cpp:263-358` —
  `ArpackEigenvalueSolver::SolveInternal` (RCI loop body; `naupd`
  driver at 318; `ApplyOp` at 325; `ApplyOpB` at 329; per-`WhichType`
  ARPACK-token switch at 280-308).
- `palace/linalg/arpack.cpp:513-560` — `ArpackEPSSolver::Solve()` body
  (defaults, `SolveInternal` invocation at 552, `RescaleEigenvectors`
  at 555, `info = 0` reset at 558, `return num_conv` at 559).
- `palace/linalg/arpack.cpp:563-589` — `ArpackEPSSolver::ApplyOp` body
  (host-pointer convention, `opK->Mult` + `opInv->Mult` non-sinvert at
  573-574, `opM->Mult` + `opInv->Mult` sinvert at 579-580).
- `palace/linalg/arpack.cpp:733-797` — `ArpackPEPSolver::ApplyOp` body
  (PEP linearisation; `opInv->Mult` non-sinvert at 761, sinvert at
  778).
- `palace/linalg/nleps.cpp:351-805` — `QuasiNewtonSolver::Solve` body
  (Newton outer loop; deflation; `SetInitialGuess` at 366;
  `deflated_solve` lambda at 505-538; `opInv->Mult` at 514;
  result-construction at 780-806).
- `palace/linalg/slepc.cpp:565-600` —
  `SlepcEPSSolverBase::SetWhichEigenpairs` (nine-way SLEPc EPS-token
  switch).
- `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve` body
  (`EPSSolve` + `EPSGetConverged` at 694-695; convergence summary at
  696-704; `RescaleEigenvectors(num_conv)` at 707;
  `return (int)num_conv` at 708).
- `palace/linalg/slepc.cpp:711-716` —
  `SlepcEPSSolverBase::GetEigenvalue(i)` (returns `l * gamma`; Higham
  un-scaling at the accessor).
- `palace/linalg/slepc.cpp:1847-1872` — `__pc_apply_EPS` PETSc shell
  PC callback (`opInv->Mult` at 1858; sinvert/non-sinvert scaling at
  1860-1865; opProj at 1867-1871).
- `palace/linalg/slepc.cpp:1942-2000` — `__pc_apply_PEPLinear` shell
  PC callback (`opInv->Mult` non-sinvert at 1965; sinvert at 1978).
- `palace/linalg/slepc.cpp:2060-2095` — `__pc_apply_PEP` shell PC
  callback (`opInv->Mult` at 2076).
- `palace/linalg/slepc.cpp:2125-2170` — `__pc_apply_NEP` shell PC
  callback (per-λ preconditioner reconfiguration at 2140-2158;
  `opInv->Mult` at 2159).
- `palace/drivers/eigensolver.cpp:280-340` — driver-side setup
  composition (shift-invert at 285; spectrum target at 291-315; inner
  linear solver binding at 330-334).
- `palace/drivers/eigensolver.cpp:365-410` — driver-side
  `Solve()` invocation + double-solve refinement (`BlockTimer
  bt1(Timer::EPS)` at 365; `eigen->Solve()` at 367; `Mpi::Print` of
  count at 370-374; QuasiNewton refinement at 377-407).
- `palace/models/modeeigensolver.cpp:1020-1054` — backend dispatch
  site (ARPACK vs SLEPc construction).
- `palace/models/modeeigensolver.cpp:484-492` — driver-side
  eigenvalue re-sort by shift-target distance.

L1 anchor:
- `book/src/L1/eigsolve.md` — the L1 operator that all four
  sub-patterns lower from (carries the `LinearSolveFailed` L1-constructive
  annotation).

Sibling lowering themes (recursed into by per-step body rewrites):
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` — the ten
  `opInv->Mult` callsites rewrite by this firm sister theme
  (sub-pattern A outer body).
- `book/src/L1-L0/apply-linop-mutation-rotation.md` — the per-step
  `opK->Mult`, `opM->Mult`, `opC->Mult` callsites inside the
  `ApplyOp` bodies rewrite by this firm sister theme.

L0 convention anchors:
- `book/src/L0/eigensolver-wrapper.md` — the L0 chapter for
  `EigenvalueSolver` and its three wrappers.
- `book/src/L0/mutable-workspace-pattern.md` — the workspace-erase L0
  convention that Sub-pattern D cites once.
- `book/src/L0/output-arg-vs-receiver.md` — the receiver-vs-output-arg
  L0 convention that the per-pair extraction rewrite cites once.

Coverage note: this theme cites the **three concrete `EigenvalueSolver`
subclass families** (`ArpackEigenvalueSolver`, `SlepcEigenvalueSolver`,
`NonLinearEigenvalueSolver::QuasiNewtonSolver`) at the inner sub-pattern
level. The Palace corpus contains only these three families plus the
abstract base; the cited set is exhaustive at the backend level. The
ten `opInv->Mult` callsites are exhaustive across the corpus.

## Status

`firm (structural)` — the four sub-pattern recognition rules and the
per-backend ARPACK / SLEPc / `QuasiNewtonSolver` bodies are cited at the
section level; the ten `opInv->Mult` callsites are exhaustively cited; the
per-pair extraction rewrite and the status sum-type derivation are
structurally complete.

The `LinearSolveFailed` materialisation is a **forward-looking
reconstruction** — the L0 source does not currently produce the variant
(negative anchor `palace/linalg/ksp.cpp:297-310`: `void`-returning
`Mult`); the rewrite shape requires the one-line `BaseKspSolver::GetConverged`
forwarder (or a `Mult` status-return) per Sub-pattern B. The negative anchors
are evidence FOR the faithful reconstruction and do not license a positive
claim; a future upstream Palace refactor shipping the forwarder + status-capture
would turn it into a positively-anchored rewrite. This is a permanent honest
property of the rewrite, not a status gate.

The three sibling eigsolve OQs
(`eigsolve-scaling-coordinate-convention`,
`eigsolve-initial-space-axis-placement`,
`eigsolve-iteration-count-result-field`) are **out of scope** for this
theme — they affect the L1 entry's signature / algebraic-laws fidelity
but not the L1>L0 rewrite shape.
