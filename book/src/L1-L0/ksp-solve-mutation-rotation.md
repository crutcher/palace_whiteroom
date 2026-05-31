# ksp-solve-mutation-rotation

The mutation rotation for the preconditioned Krylov solve. Lowers the pure
L1 form `ksp_solve(K, b) → SolveResult[N]` (cycle-007 firm; see
[`L1/ksp_solve`](../L1/ksp_solve.md)) into Palace's in-place L0 entry
`BaseKspSolver<OperType>::Mult(b, x)` at `palace/linalg/ksp.cpp:296-310`
together with the inner per-method `IterativeSolver<OperType>::Mult` body
(one of `CgSolver` / `GmresSolver` / `FgmresSolver`).

This is the **first L1>L0 mutation-rotation theme for a structured opaque
primary argument**: the L1 input `K: Solver[A]` is itself a
construction-bound value (carrying the system operator, the optional
preconditioner, the convergence-control parameters, and the per-method
choice of CG / GMRES / FGMRES with all per-method state). The earlier
themes [`axpby-mutation-rotation`](./axpby-mutation-rotation.md) (value-type
primary), [`axpbypcz-mutation-rotation`](./axpbypcz-mutation-rotation.md)
(value-type primary), and
[`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
(opaque-but-stateless `LinearOperator` primary) all sit beneath this one:
the per-step body inside the inner `ksp->Mult` is built from `apply_linop`,
`axpy`, `axpby`, `dot`, `nrm2` calls — each lowered by its own sister
theme. `ksp-solve-mutation-rotation` is the layer above that names the
*compositional whole* (workspace allocation + initial-guess threading +
inner iteration + counter mutation + warning side-channel) as one rewrite.

## Slug

`ksp-solve-mutation-rotation`

## L1 form (LHS)

The pure-functional preconditioned Krylov solve
([`L1/ksp_solve`](../L1/ksp_solve.md)):

    result = ksp_solve(K, b)               -- result : SolveResult[N]

    SolveResult[N] = {
      x          : Tensor[N],   -- approximate solution to A · x = b
      converged  : Bool,        -- convergence flag
      iterations : Int,         -- per-call iteration count
      initial_res: Real,        -- initial residual norm (per the solver's residual proxy)
      final_res  : Real         -- final residual norm (per the solver's residual proxy)
    }

`K : Solver[A]` is a construction-bound, opaque solver value whose internal
Krylov method (CG / GMRES / FGMRES), preconditioner, convergence tolerances
(`rel_tol`, `abs_tol`), iteration cap (`max_it`), restart dimension (for
restarted methods), preconditioner side, orthogonalisation method, and
initial-guess policy are all bound at construction. The per-call signature
is variant-free: only `(K, b)` enter and only `SolveResult[N]` leaves.

The four `SolveResult` fields correspond one-to-one with `mutable` per-solve
state on the L0 `IterativeSolver<OperType>` base class
(`palace/linalg/iterative.hpp:53-55`): `converged`, `initial_res`,
`final_res`, `final_it` — see
[`L1/ksp_solve`](../L1/ksp_solve.md) Signature §"result" for the field-by-field
mapping.

## L0 form (RHS)

The rewrite is layered: an outer composition rewrite at `BaseKspSolver::Mult`
plus an inner per-method body rewrite (CG / GMRES / FGMRES), each with its
own workspace allocation and initial-guess threading. The two
unimplemented `KrylovSolver` enum cases (`MINRES`, `BICGSTAB`) are
documented as separate L1>L0 obstruction themes
([`minres-iteration`](./minres-iteration.md),
[`bicgstab-iteration`](./bicgstab-iteration.md)) and are **not** part of
this theme's recognition set — see Applicability conditions §1.

### Sub-pattern A — outer composition (`BaseKspSolver::Mult`)

The outer L0 entry point is the compact composition body
(`palace/linalg/ksp.cpp:296-310`):

```cpp
template <typename OperType>
void BaseKspSolver<OperType>::Mult(const VecType &x, VecType &y) const
{
  BlockTimer bt(Timer::KSP, use_timer);
  ksp->Mult(x, y);
  if (!ksp->GetConverged())
  {
    Mpi::Warning(
        ksp->GetComm(),
        "Linear solver did not converge, norm(Ax-b)/norm(b) = {:.3e} (norm(b) = {:.3e})!\n",
        ksp->GetFinalRes() / ksp->GetInitialRes(), ksp->GetInitialRes());
  }
  ksp_mult++;
  ksp_mult_it += ksp->GetNumIterations();
}
```

Four L0 surface concerns surround the inner per-method `ksp->Mult(x, y)`
call, and each rewrites distinctly:

- **Destination buffer `y`** (the second parameter) — the L0 output slot
  that holds the solution after return. At L1 this binds to
  `result.x`; the destination disappears from the signature. Identical to
  the destination-binding rewrite in the
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
  sub-pattern A, applied one layer up (the receiver is now the solver
  composition class, not a raw operator).
- **The `BlockTimer bt(Timer::KSP, use_timer);` RAII line** — wraps the
  solve in a scoped timer that records to a Palace-global `Timer::KSP`
  bucket via the `BlockTimer` destructor. This is a transparent
  performance / instrumentation concern with no L1 semantic content. At
  L1 the timer mention erases entirely; the L1 form is referentially
  transparent and is timed by the caller's choice (or not at all). See
  [`transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md)
  for the convention; this is a transparent-side instance.
- **The non-convergence `Mpi::Warning` side channel** (lines 301-307) —
  on `!ksp->GetConverged()` the body logs a formatted residual-ratio
  warning through Palace's MPI-aware logger and returns the (presumably
  unconverged) iterate regardless. At L1 the same information is carried
  structurally by `result.converged : Bool` plus `result.initial_res` /
  `result.final_res` (the same two numbers the warning prints). The
  warning emission itself is a caller-side concern at L1 — any L1-driven
  caller that needs warning-on-non-convergence reads
  `result.converged` and emits its own log. See
  [`L1/ksp_solve`](../L1/ksp_solve.md) Semantics paragraph 4 for the
  rationale.
- **The cumulative counter updates** (lines 308-309) — `ksp_mult++` and
  `ksp_mult_it += ksp->GetNumIterations()` are per-instance running
  sums accumulated across many `Mult` calls on the same `BaseKspSolver`
  instance. At L1 these counters are **driver-side accumulators**, not
  part of the operator: each `ksp_solve` call contributes
  `result.iterations` to the running iteration sum and `1` to the
  running call sum. Reconstructing the L0 counters is `Σ_calls 1` and
  `Σ_calls result.iterations` outside the operator. This is the
  [`counter-update`](../concepts/counter-update.md) concept applied at
  the solver-composition layer.

Justification kind: **structural** — the rewrite re-binds the L1 output
record into the L0 destination buffer + inner state mutations; the four
surface concerns rewrite by the three patterns called out above (timer
erase, warning-to-structured-field, counter-to-driver-accumulator) plus
the destination-binding rewrite shared with
[`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md).

Citations:
- `palace/linalg/ksp.cpp:296-310` — `BaseKspSolver<OperType>::Mult`
  definition (the full outer composition body).
- `palace/linalg/ksp.cpp:299` — `BlockTimer bt(Timer::KSP, use_timer);`
  (transparent timer mention).
- `palace/linalg/ksp.cpp:300` — `ksp->Mult(x, y);` — the inner per-method
  dispatch site (recurses into one of CG / GMRES / FGMRES sub-patterns
  B / C / D below).
- `palace/linalg/ksp.cpp:301-307` — non-convergence `Mpi::Warning`
  side-channel.
- `palace/linalg/ksp.cpp:308-309` — cumulative counter mutations
  (`ksp_mult++`, `ksp_mult_it += ksp->GetNumIterations()`).
- `palace/linalg/ksp.hpp:60-61` — `NumTotalMult()` / `NumTotalMultIterations()`
  accessors that the driver reads to recover the cumulative sums.
- `palace/linalg/iterative.hpp:53-55` — `mutable` per-solve statistics
  (`converged`, `initial_res`, `final_res`, `final_it`) on the
  `IterativeSolver` base; these are the L0 slots whose values are
  copied into the L1 `SolveResult` fields by the rewrite.

### Sub-pattern B — inner CG body (`CgSolver<OperType>::Mult`)

The inner per-method body for the `CG` arm of the
`KrylovSolver` enum is `CgSolver<OperType>::Mult` at
`palace/linalg/iterative.cpp:360-486`. Three L0 sub-concerns of the inner
body recur in all three methods and rewrite in the same way:

- **Workspace allocation** (`palace/linalg/iterative.cpp:369-374`):

  ```cpp
  r.SetSize(A->Height());
  z.SetSize(A->Height());
  p.SetSize(A->Height());
  r.UseDevice(true);
  z.UseDevice(true);
  p.UseDevice(true);
  ```

  The three `mutable VecType r, z, p` members (`palace/linalg/iterative.hpp:144`)
  are the per-iteration workspace: residual, preconditioned residual,
  search direction. Allocated lazily on first `Mult`, reused on subsequent
  calls (no-op `SetSize` when sizes match). At L1 the workspace is
  erased — internal storage for `apply_linop` / `axpy` / `dot`
  intermediates is below the L1 abstraction; the [`mutable workspace
  pattern`](../L0/mutable-workspace-pattern.md) chapter is the L0
  convention this rewrite cites once and does not re-state per theme.

- **Initial-guess threading** (`palace/linalg/iterative.cpp:377-386`):

  ```cpp
  if (this->initial_guess)
  {
    A->Mult(x, r);
    linalg::AXPBY(1.0, b, -1.0, r);   // r = b - A·x
  }
  else
  {
    r = b;
    x = 0.0;                          // zero-init the destination
  }
  ```

  The `initial_guess` flag on `IterativeSolver<OperType>` selects
  whether `x` arrives carrying a warm-start initial guess (in which case
  the residual is `r = b - A·x`) or is zero-initialised (in which case
  the residual is `r = b`). At L1 the initial-guess policy is bound
  inside `K`'s opaque state (see [`L1/ksp_solve`](../L1/ksp_solve.md)
  Variant axes §"initial-guess-policy"); the per-call signature does
  not expose an initial guess. The L1>L0 rewrite reintroduces the
  threading: if `K`'s bound policy is `warm-start`, the L0 destination
  buffer `y` (= L1 `result.x`) must arrive carrying the initial guess
  value, witnessed by the explicit `A->Mult(x, r)` + `linalg::AXPBY`
  pair; if the policy is `cold-start`, the L0 body does
  `r = b; x = 0.0`. **Either way the post-call `result.x` value is the
  same algebraic solution** modulo the convergence tolerance
  (the iterations and final residual differ; see law 4 in
  [`L1/ksp_solve`](../L1/ksp_solve.md) Algebraic laws).

- **Per-step inner kernel + convergence test** (`iterative.cpp:427-464`):
  the for-loop is the L2 [`krylov-step`](../L2/krylov-step.md) kernel
  instantiation for CG, built from one `A->Mult(p, z)` per step (the
  `apply_linop` invocation), two `dot` calls (`linalg::Dot(comm, z, p)`
  at line 444; `linalg::Dot(comm, z, r)` at line 460), two
  `axpy`-shaped updates (`x.Add(alpha, p)` at line 448;
  `r.Add(-alpha, z)` at line 449 — sub-patterns A and C of
  [`axpby-mutation-rotation`](./axpby-mutation-rotation.md)
  respectively), one `linalg::AXPBY` (line 440), one preconditioner
  apply when `B` is set (`ApplyB(B, r, z, ...)` at line 454), and the
  scalar convergence test (`converged = (res < eps)` at line 463). At L1
  the loop is opaque — the L1 form sees only the final
  `(x, converged, iterations, initial_res, final_res)` tuple. The
  L1>L0 rewrite reintroduces the iteration as a `for`-loop whose body
  composes the cited sister-theme rewrites.

- **Final-state write-out** (`iterative.cpp:484-485`):
  `final_res = res;` and `final_it = it;` populate the `mutable`
  output fields. After the outer
  `BaseKspSolver::Mult` returns, the `result.final_res` /
  `result.iterations` fields read from these same `mutable` members
  via `ksp->GetFinalRes()` / `ksp->GetNumIterations()`. (The
  `converged` and `initial_res` fields are also `mutable`-written
  inside the body — `converged` at line 418 and again at 463, in
  the loop; `initial_res` at lines 411 / 415.)

Justification kind: **structural** with embedded algebraic sub-rewrites.
The for-loop is a structural rewrite of the L1 opaque iteration; the
per-step `Mult` / `axpy` / `dot` / `AXPBY` calls each rewrite by their
own sister themes
([`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md),
[`axpby-mutation-rotation`](./axpby-mutation-rotation.md),
[`axpbypcz-mutation-rotation`](./axpbypcz-mutation-rotation.md)).

Recognition note: a `CheckDot` helper
(`palace/linalg/iterative.cpp:21-32`, called at lines 396, 410, 445, 461)
guards against the preconditioner becoming non-SPD or the operator
becoming non-positive-definite — `(Br, r) ≤ 0` or `(Ap, p) ≤ 0` aborts
the solve with an explanatory error message. This is a **load-bearing
algebraic precondition** of CG (CG requires SPD `A` and SPD
preconditioner `B`); the check is not transparent. At L1 the SPD
contract lives on `K`'s opaque type as a precondition not visible in the
signature — the `Solver[A]` type tag elides the SPD requirement, but
constructing `K` with `KrylovSolver::CG` carries the obligation.
Violating the obligation at runtime trips the `CheckDot` abort. Lifting
the SPD precondition into the type system is an L4 typing-rule question;
see [`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md)
notes-for-higher-layers §3 and [`L1/ksp_solve`](../L1/ksp_solve.md)
"L1 vs L0 distinction" for the discussion.

Recognition note (initial-residual `Norml2`-vs-`Dot` asymmetry —
**likely Palace bug; upstream confirmation pending**): the
`initial_guess`-branch initial-residual computation at
`palace/linalg/iterative.cpp:398-411` exhibits a structural asymmetry
between the preconditioned (`B`) and unpreconditioned (`!B`) arms that
makes the L1 `initial_res` field's reconstruction quirky in the
`!B && initial_guess` case. The two arms write `beta_rhs` differently
before the shared `initial_res = std::sqrt(std::abs(beta_rhs));`
collapse at line 411:

    // B (preconditioned) arm — iterative.cpp:401-405
    ApplyB(B, b, p, this->use_timer);
    beta_rhs = linalg::Dot(comm, p, b);     // = (B·b, b) = ⟨b, b⟩_B

    // !B (unpreconditioned) arm — iterative.cpp:406-409
    beta_rhs = linalg::Norml2(comm, b);     // = ‖b‖₂ = sqrt(|b·b|)

The mechanical cause is `linalg::Norml2`'s body at
`palace/linalg/vector.hpp:257-260`:

    template <typename VecType>
    inline auto Norml2(MPI_Comm comm, const VecType &x)
    {
      return std::sqrt(std::abs(Dot(comm, x, x)));
    }

`Norml2` **already** square-roots-of-dot internally, so on the `!B` arm
`beta_rhs = sqrt(|b·b|)` rather than the symmetry-consistent `b·b` the
`B` arm produces. Then line 411 takes a **second** square root —
`initial_res = sqrt(|beta_rhs|) = sqrt(sqrt(|b·b|)) = (b·b)^{1/4}` —
where the algorithm's intent (the `B` arm reconstructs as
`sqrt(⟨b, b⟩_B) = ‖b‖_B`, and in the `B == identity` limit this should
collapse to `‖b‖₂ = (b·b)^{1/2}`) demands `initial_res = ‖b‖₂`. The
two arms therefore disagree at `B == identity` by a missing inner
square root: the `!B` arm produces the fourth root of `b·b`, not the
square root. The downstream consumer is `eps = std::max(rel_tol *
initial_res, abs_tol);` at line 417 — the convergence tolerance is
quirky-scaled in the `!B && initial_guess` case, biasing
relative-tolerance convergence for cold-vs-warm-start asymmetrically.
The bug does not affect the unpreconditioned cold-start case (line 415
falls through to `initial_res = res;` where `res = sqrt(|b·b|) = ‖b‖₂`
correctly via the line-395-396 path), and does not affect the
preconditioned warm-start case (the `B` arm computes the intended
`‖b‖_B`). It affects **only** `!B && initial_guess`. The faithful L1>L0
recognition rule is: the `!B && initial_guess` branch's `initial_res`
field is `(b·b)^{1/4}` as written, not `‖b‖₂`; L1 consumers that
interpret `initial_res` as `‖b‖₂` are reading the L1 abstraction's
intended semantics rather than the L0 reality. **This is recorded as a
likely Palace bug** (the symmetric form, by analogy with the `B` arm
and the consistent `iterative.cpp:395-396` unpreconditioned cold-start
`res` computation, would be `beta_rhs = linalg::Dot(comm, b, b);` at
line 408); upstream confirmation that the asymmetry is unintentional is
pending. The corresponding warm-vs-cold initial-residual computation in
`GmresSolver` is factored into the `InitialResidual` helper
(`palace/linalg/iterative.cpp:252-285`, called at
`iterative.cpp:566-567`, noted in Sub-pattern C) which uses a different
internal control flow and is **not** affected by this asymmetry — the
bug is local to `CgSolver<OperType>::Mult`. See OQ
`cg-initial-residual-quirk-palace-bug-flag-lift-path` (narrowed to
upstream-confirmation; the lift annotation now lives here in the firm
artifact).

Citations:
- `palace/linalg/iterative.hpp:117-150` — `CgSolver<OperType>` declaration;
  `mutable VecType r, z, p` workspace at line 144.
- `palace/linalg/iterative.cpp:360-486` — `CgSolver<OperType>::Mult`
  definition (the full inner body).
- `palace/linalg/iterative.cpp:369-374` — workspace lazy-allocation +
  device-residency annotations.
- `palace/linalg/iterative.cpp:377-386` — initial-guess threading.
- `palace/linalg/iterative.cpp:418-419` — short-circuit on zero
  initial residual (`converged = (res < eps)` with `res == 0` ⇒
  immediate convergence; supports law 2 "zero RHS gives zero solution"
  on the L1 entry).
- `palace/linalg/iterative.cpp:427-464` — inner for-loop (the per-step
  body).
- `palace/linalg/iterative.cpp:443` — `A->Mult(p, z)` — the per-step
  `apply_linop` invocation; rewrites by
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
  sub-pattern A.
- `palace/linalg/iterative.cpp:448-449` — `x.Add(alpha, p)` (sub-pattern
  A of [`axpby-mutation-rotation`](./axpby-mutation-rotation.md))
  followed by `r.Add(-alpha, z)` (sub-pattern C of same).
- `palace/linalg/iterative.cpp:440` — `linalg::AXPBY(ScalarType(1.0), z,
  beta / beta_prev, p)` — rewrites by
  [`axpby-mutation-rotation`](./axpby-mutation-rotation.md) (axpby
  speculative-operator form; harvester promotion pending).
- `palace/linalg/iterative.cpp:484-485` — `final_res = res;
  final_it = it;` — the `mutable`-state write-out that the outer
  `BaseKspSolver::Mult` reads via `GetFinalRes()` /
  `GetNumIterations()`.
- `palace/linalg/iterative.cpp:398-411` — `initial_guess`-branch
  `initial_res` computation; the `B` arm uses `linalg::Dot(comm, p, b)`
  at line 404 (where `p = B·b`), the `!B` arm uses
  `linalg::Norml2(comm, b)` at line 408 — the asymmetric form
  documented in the "initial-residual `Norml2`-vs-`Dot` asymmetry"
  recognition note above (likely Palace bug; upstream confirmation
  pending).
- `palace/linalg/vector.hpp:257-260` — `linalg::Norml2` definition:
  `std::sqrt(std::abs(Dot(comm, x, x)))`. The internal square root is
  the mechanical cause of the `initial_res = (b·b)^{1/4}` outcome on
  the `!B && initial_guess` branch (line 411 takes the second square
  root over `beta_rhs`).

### Sub-pattern C — inner GMRES body (`GmresSolver<OperType>::Mult`)

The inner per-method body for the `GMRES` arm of the `KrylovSolver` enum
is `GmresSolver<OperType>::Mult` at `palace/linalg/iterative.cpp:543-705`.
Same four-sub-concern rewrite as sub-pattern B, with three GMRES-specific
elaborations:

- **Workspace allocation is factored into a virtual `Initialize()` method**
  (`palace/linalg/iterative.cpp:488-516`) called once per restart cycle
  (entry point at `iterative.cpp:553`), plus a per-step
  `Update(j)` method (`iterative.cpp:518-541`) that lazily extends the
  Arnoldi basis vectors. The `mutable` workspace is larger
  (`std::vector<VecType> V` for the Arnoldi basis,
  `mutable VecType r`, `mutable std::vector<ScalarType> H` for the
  Hessenberg, `mutable std::vector<ScalarType> s, sn` and
  `mutable std::vector<RealType> cs` for the Givens-rotation state
  — `palace/linalg/iterative.hpp:190-194`). At L1 all of this erases
  identically to sub-pattern B's `r, z, p`.

- **Restarted outer loop** (`palace/linalg/iterative.cpp:563-683`):
  GMRES has an outer restart loop indexed by `restart` and an inner
  Arnoldi loop indexed by `j`. The combined iteration count `it`
  bounds against `max_it` exactly as in CG. The outer loop is a
  structural rewrite of the same opaque `iterations` field in
  `SolveResult`. The restart parameter `max_dim` is bound inside `K`'s
  opaque state at construction (set via `SetRestartDim` from the
  factory at `palace/linalg/ksp.cpp:42`).

- **Initial-guess threading via `InitialResidual` helper**
  (`palace/linalg/iterative.cpp:252-285`, called at
  `iterative.cpp:566-567`): the same warm-vs-cold initial-residual
  computation as in CG, with the additional twist that
  `PreconditionerSide::LEFT` vs `RIGHT` selects whether the residual
  is `r = b - A·x` or `r = B·(b - A·x)`. The preconditioner-side choice
  is bound inside `K`'s opaque state (set at the factory,
  `palace/linalg/ksp.cpp:73-86`). At L1 this is absorbed into the
  opaque `Solver[A]` type.

- **Per-step inner kernel includes orthogonalisation dispatch**
  (`palace/linalg/iterative.cpp:627-643`): the `ApplyBA` call at line
  627 is a fused `B·A·x` or `A·B·x` (per `pc_side`); the
  `OrthogonalizeIteration` call at line 630 dispatches on
  `gs_orthog ∈ {MGS, CGS, CGS2}` to one of the
  `linalg::OrthogonalizeColumn{MGS,CGS}` helpers; the Givens-rotation
  application at lines 636-640 maintains the rotated RHS as the
  residual proxy. The orthogonalisation choice is bound inside `K`'s
  opaque state at construction (set at the factory,
  `palace/linalg/ksp.cpp:92-94`); see
  [`L1/ksp_solve`](../L1/ksp_solve.md) Semantics paragraph 6 for the
  bit-determinism non-law this introduces. The per-step rewrites
  delegate to the same sister themes as CG plus
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
  sub-pattern B (transpose-mode is not used here but the fused
  preconditioner-and-operator apply is the same overload family).

Justification kind: **structural** with embedded algebraic sub-rewrites
(same as sub-pattern B; the per-step body decomposes into the same
sister-theme primitives).

Citations:
- `palace/linalg/iterative.hpp:152-217` — `GmresSolver<OperType>`
  declaration with `mutable` workspace (lines 190-194), `max_dim`
  (180), `gs_orthog` (184), `pc_side` (187).
- `palace/linalg/iterative.cpp:488-516` — `GmresSolver::Initialize`
  (per-restart workspace allocation).
- `palace/linalg/iterative.cpp:518-541` — `GmresSolver::Update(j)`
  (per-step basis-vector lazy resize).
- `palace/linalg/iterative.cpp:543-705` — `GmresSolver<OperType>::Mult`
  definition (the full inner body).
- `palace/linalg/iterative.cpp:563-683` — outer restart loop and inner
  Arnoldi loop.
- `palace/linalg/iterative.cpp:252-285` — `InitialResidual` helper
  (the initial-guess threading factored out from the per-method bodies;
  shared with FGMRES).
- `palace/linalg/iterative.cpp:287-305` — `ApplyBA` helper (combined
  preconditioner + operator apply for the inner step; `pc_side`-aware).
- `palace/linalg/iterative.cpp:307-325` — `OrthogonalizeIteration`
  helper (MGS / CGS / CGS2 dispatch).
- `palace/linalg/iterative.cpp:703-704` — `final_res = beta;
  final_it = it;` write-out (`beta` is the GMRES residual proxy from
  the rotated-RHS magnitude).

### Sub-pattern D — inner FGMRES body (`FgmresSolver<OperType>::Mult`)

The inner per-method body for the `FGMRES` arm of the `KrylovSolver` enum
is `FgmresSolver<OperType>::Mult` at `palace/linalg/iterative.cpp:733-870`.
Structurally a specialisation of sub-pattern C with one workspace
extension: the additional `mutable std::vector<VecType> Z`
(`palace/linalg/iterative.hpp:256`) records the preconditioned vector at
each Arnoldi step (`Z[j] = B⁻¹·V[j]`) rather than only the
un-preconditioned basis. The flexible-preconditioner extension allows the
preconditioner to be non-constant across iterations (e.g. a nested
iterative solver whose tolerance varies per outer step); the cost is
`O(m)` extra vectors of storage.

The `Initialize` / `Update` overrides
(`palace/linalg/iterative.cpp:707-731`) allocate and lazily-resize the
`Z` array alongside the inherited `V` array; otherwise the outer
restart loop, inner Arnoldi loop, initial-guess threading, and Givens
machinery are inherited from `GmresSolver`. The constructor
(`palace/linalg/iterative.hpp:262-266`) fixes
`pc_side = PreconditionerSide::RIGHT` (FGMRES only supports
right-preconditioning algebraically); the overridden
`SetPreconditionerSide` (`iterative.hpp:268-272`) aborts on any attempt
to change this — a **load-bearing algebraic precondition** that the L1
opaque type elides at construction time but the L0 enforces.

Justification kind: **structural** (same shape as sub-pattern C with
one additional `mutable` workspace member; per-step body rewrites
delegate to the same sister themes).

Citations:
- `palace/linalg/iterative.hpp:219-275` — `FgmresSolver<OperType>`
  declaration; additional `mutable std::vector<VecType> Z` workspace
  at line 256; right-preconditioning constraint at lines 263-272.
- `palace/linalg/iterative.cpp:707-731` — `FgmresSolver::Initialize`
  and `Update(j)` (extend GMRES's workspace with `Z` bookkeeping).
- `palace/linalg/iterative.cpp:733-870` — `FgmresSolver<OperType>::Mult`
  definition.

## Applicability conditions

For all four sub-patterns the rewrite preserves semantics when:

1. **`K`'s bound Krylov method is one of CG / GMRES / FGMRES.** The
   recognition set for this theme excludes the three enumerated cases
   `MINRES`, `BICGSTAB`, `DEFAULT` that route to `MFEM_ABORT` at the
   factory (`palace/linalg/ksp.cpp:53-57`). Per CLAUDE.md
   "Unimplemented Palace stub policy", those three cases are documented
   as separate L1>L0 obstruction themes
   ([`minres-iteration`](./minres-iteration.md),
   [`bicgstab-iteration`](./bicgstab-iteration.md)) and are
   **not** part of this implemented-Krylov theme. A `K` constructed
   with one of the unimplemented enum tags aborts at factory time
   before any `ksp_solve` call site is reached, so the L1 form is
   never witnessed for those tags. This implemented theme is the
   symmetric companion for the implemented Krylov methods — the
   obstruction themes carry the speculative L1 operators
   (`lanczos_step`, `bicgstab_step`, `three_term_recurrence_update`,
   `omega_update`, `stabilisation_update`, etc.); this theme carries
   only the firm L1 `ksp_solve` and decomposes into firm sister-theme
   primitives.

2. **No aliasing between `b` and the destination buffer used to receive
   the result.** The L0 inner bodies read `b` element by element while
   writing `x` (initialisation phase) and subsequently mutating the
   workspace and `x`. If `b` and `x` alias, the L0 behaviour is
   undefined (the initialisation `r = b; x = 0.0` at
   `palace/linalg/iterative.cpp:384-385` would zero `b` before the
   first `Dot`). The L1 form takes `b` as a separate input value, so
   the lowering must guarantee non-aliased buffers. Palace never
   aliases `Mult` arguments in observed sites; this is an
   applicability condition, not a known failure. Shared with the sister
   themes.

3. **No observer of the prior destination value after the call** unless
   `K`'s initial-guess policy is `warm-start`, in which case the prior
   destination value is consumed (as the warm-start initial guess), not
   destroyed-and-discarded. In the `cold-start` case the prior value is
   discarded (zeroed at line 385 of `iterative.cpp`); in the
   `warm-start` case the prior value is read once to compute `r = b -
   A·x` and then overwritten. The L1>L0 rewrite must respect the
   policy: if the L1 form arose by composition with a prior
   `ksp_solve` whose `result.x` is the warm start, the L0 destination
   buffer holds that value pre-call and the policy on `K` is
   `warm-start`.

4. **Conforming shape and element type.** `b.Size() == A.Width()` and
   the destination buffer's size equals `A.Height()`, with the system
   operator `A` square (`A.Height() == A.Width()`); the element type
   matches `K`'s template parameter (`Operator` for real, `ComplexOperator`
   for complex). MFEM-side runtime checks
   (`palace/linalg/iterative.cpp:367-368`) enforce the size match;
   element-type mismatch fails at template-instantiation time (the
   `static_assert` chain at `palace/linalg/ksp.hpp:32-34`).

5. **`K`'s bound system operator `A` satisfies the per-method algebraic
   precondition.** For CG: `A` must be SPD and the bound preconditioner
   `B` must also be SPD. The `CheckDot` helper at runtime catches the
   most common violations (non-positive inner products on residual
   norms or operator quadratic forms). For GMRES / FGMRES: no symmetry
   requirement on `A`, but the orthogonalisation method (MGS / CGS /
   CGS2) and preconditioner-side choice must be consistent with the
   problem (e.g. right-preconditioning is required for FGMRES). These
   are preconditions of `K`'s opaque type at L1; violations trip the
   `CheckDot` abort or analogous L0 guards.

6. **Workspace allocation respects the `mutable` discipline.** The
   per-method bodies write through `mutable` workspace members
   (`CgSolver::{r,z,p}`; `GmresSolver::{V,r,H,s,sn,cs}`;
   `FgmresSolver::Z`) and `mutable` per-solve statistics
   (`IterativeSolver::{converged,initial_res,final_res,final_it}`) from
   inside `const` method bodies. The workspace mention erases at L1
   per [`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md);
   the per-solve statistics are the L0 slots whose values are copied
   into the L1 `SolveResult` fields by the rewrite. The discipline is
   single-writer-at-a-time per `K` instance — concurrent `ksp_solve`
   calls on the same `K` would race on the workspace (see
   [`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md)
   "Lifecycle semantics" §thread-safety).

## Justification kind

- **Sub-pattern A (outer `BaseKspSolver::Mult`)** — `structural`. The
  destination-buffer rewrite plus four absorption rules (timer erase,
  warning-to-structured-field, counter-to-driver-accumulator,
  inner-Mult-dispatch). The four rules are individually structural; the
  inner-Mult dispatch composes with sub-patterns B / C / D.
- **Sub-pattern B (inner CG body)** — `structural` with embedded algebraic
  sub-rewrites. The for-loop is a structural rewrite of the L1 opaque
  iteration; per-step `apply_linop` / `axpy` / `dot` / `AXPBY` calls
  rewrite by sister themes.
- **Sub-pattern C (inner GMRES body)** — `structural` with embedded
  algebraic sub-rewrites (same as B, plus the GMRES-specific
  restart / orthogonalisation absorption).
- **Sub-pattern D (inner FGMRES body)** — `structural`, inherits from C
  with one additional workspace member.

The theme as a whole is `structural` with four sub-rewrites that
compose along the outer-`BaseKspSolver` → inner-`IterativeSolver` axis
plus the per-step decomposition into firm sister-theme primitives. A
`lowering-verifier` audit in a later cycle should confirm sub-pattern
recognition is exhaustive over the implemented-Krylov L0 corpus,
specifically that the four-surface-concern absorption (timer, warning,
counters, destination-binding) at the outer layer is consistent with the
sister themes' workspace-mention-and-erase discipline.

## Speculative L1 operators

None.

`ksp_solve` is the firm L1 form (cycle-007); the per-step inner-body
decomposition recovers `apply_linop` / `axpy` / `axpby` / `dot` / `nrm2`
— all firm. The orthogonalisation, preconditioner-side, and
initial-guess choices that GMRES / FGMRES expose at L0 are absorbed into
`K`'s opaque `Solver[A]` type at L1; they are construction-time
parameters of the factory, not per-call L1 arguments. No rough-in L1
operator is needed for this theme.

This is the same structural property as
[`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md):
when the L1 form is the firm cohort's gate point (`apply_linop` for the
operator-vocabulary gate; `ksp_solve` for the constructed-operator gate),
the variant-axis-collapse design lets the L1>L0 lowering operate entirely
within existing L1 vocabulary. By contrast, the unimplemented-Krylov
obstruction themes ([`minres-iteration`](./minres-iteration.md),
[`bicgstab-iteration`](./bicgstab-iteration.md)) emit rough-in
operators because their L0 anchor is the *absence* of an implementation
and the L1 form must be sketched against the literature.

## Verified-against

L0 evidence ranges (verified by direct read during this cycle):

- `palace/linalg/ksp.cpp:296-310` — `BaseKspSolver<OperType>::Mult`
  definition (sub-pattern A outer body).
- `palace/linalg/ksp.cpp:299` — `BlockTimer bt(Timer::KSP, use_timer);`.
- `palace/linalg/ksp.cpp:300` — `ksp->Mult(x, y);` inner dispatch.
- `palace/linalg/ksp.cpp:301-307` — non-convergence `Mpi::Warning`.
- `palace/linalg/ksp.cpp:308-309` — cumulative counter mutations.
- `palace/linalg/ksp.cpp:34-58` — `ConfigureKrylovSolver` switch (the
  three implemented arms + the three aborting arms; documents the
  recognition-set boundary for applicability condition §1).
- `palace/linalg/ksp.cpp:53-57` — `MFEM_ABORT` fall-through for the
  three unimplemented enum cases.
- `palace/linalg/ksp.hpp:29-72` — `BaseKspSolver<OperType>` class
  declaration.
- `palace/linalg/ksp.hpp:60-61` — `NumTotalMult()` /
  `NumTotalMultIterations()` accessors (driver-side reads of the
  cumulative counters).
- `palace/linalg/ksp.hpp:74-75` — `KspSolver` / `ComplexKspSolver`
  type aliases.
- `palace/linalg/iterative.hpp:25-115` — `IterativeSolver<OperType>`
  abstract base.
- `palace/linalg/iterative.hpp:53-55` — `mutable` per-solve statistics
  (`converged`, `initial_res`, `final_res`, `final_it`).
- `palace/linalg/iterative.hpp:117-150` — `CgSolver<OperType>`
  declaration.
- `palace/linalg/iterative.hpp:144` — CG workspace `mutable VecType r,
  z, p`.
- `palace/linalg/iterative.hpp:152-217` — `GmresSolver<OperType>`
  declaration.
- `palace/linalg/iterative.hpp:190-194` — GMRES workspace.
- `palace/linalg/iterative.hpp:180` — GMRES `max_dim` restart parameter.
- `palace/linalg/iterative.hpp:184` — GMRES `gs_orthog`
  orthogonalisation choice.
- `palace/linalg/iterative.hpp:187` — GMRES `pc_side` preconditioner-side
  choice.
- `palace/linalg/iterative.hpp:219-275` — `FgmresSolver<OperType>`
  declaration.
- `palace/linalg/iterative.hpp:256` — FGMRES extra workspace `mutable
  std::vector<VecType> Z`.
- `palace/linalg/iterative.hpp:262-272` — FGMRES right-preconditioning
  constraint.
- `palace/linalg/iterative.cpp:21-32` — `CheckDot` helper (SPD-guard).
- `palace/linalg/iterative.cpp:243-250` — `ApplyB` helper
  (preconditioner-only apply with optional timing).
- `palace/linalg/iterative.cpp:252-285` — `InitialResidual` helper
  (initial-guess threading, `pc_side`-aware).
- `palace/linalg/iterative.cpp:287-305` — `ApplyBA` helper
  (combined preconditioner + operator apply).
- `palace/linalg/iterative.cpp:307-325` — `OrthogonalizeIteration`
  helper.
- `palace/linalg/iterative.cpp:360-486` — `CgSolver<OperType>::Mult`
  definition (sub-pattern B).
- `palace/linalg/iterative.cpp:369-374` — CG workspace lazy-allocation.
- `palace/linalg/iterative.cpp:377-386` — CG initial-guess threading.
- `palace/linalg/iterative.cpp:418-419` — short-circuit on zero
  initial residual.
- `palace/linalg/iterative.cpp:427-464` — CG inner for-loop.
- `palace/linalg/iterative.cpp:443` — CG per-step `A->Mult(p, z)`
  (`apply_linop` invocation).
- `palace/linalg/iterative.cpp:448-449` — CG per-step `x.Add(alpha, p)`
  and `r.Add(-alpha, z)` axpy updates.
- `palace/linalg/iterative.cpp:484-485` — CG `final_res = res;
  final_it = it;` write-out.
- `palace/linalg/iterative.cpp:488-516` — `GmresSolver::Initialize`.
- `palace/linalg/iterative.cpp:518-541` — `GmresSolver::Update(j)`.
- `palace/linalg/iterative.cpp:543-705` — `GmresSolver<OperType>::Mult`
  definition (sub-pattern C).
- `palace/linalg/iterative.cpp:566-567` — GMRES `InitialResidual`
  invocation per restart cycle.
- `palace/linalg/iterative.cpp:627` — GMRES per-step `ApplyBA`.
- `palace/linalg/iterative.cpp:630` — GMRES per-step
  `OrthogonalizeIteration`.
- `palace/linalg/iterative.cpp:636-640` — GMRES per-step Givens
  application.
- `palace/linalg/iterative.cpp:703-704` — GMRES `final_res = beta;
  final_it = it;` write-out.
- `palace/linalg/iterative.cpp:707-731` — FGMRES `Initialize` /
  `Update(j)` overrides.
- `palace/linalg/iterative.cpp:733-870` — `FgmresSolver<OperType>::Mult`
  definition (sub-pattern D).

L1 anchor:

- `book/src/L1/ksp_solve.md` — the firm L1 operator that all four
  sub-patterns lower from.

Sibling lowering themes (recursed into by per-step body rewrites):

- `book/src/L1-L0/apply-linop-mutation-rotation.md` — the per-step
  `A->Mult` / `B->Mult` invocations rewrite by sub-patterns A / D of
  this sister theme.
- `book/src/L1-L0/axpby-mutation-rotation.md` — the per-step
  `x.Add(alpha, p)` / `r.Add(-alpha, z)` / `y.Add(s[k], V[k])` /
  `linalg::AXPBY(...)` calls rewrite by this sister theme.
- `book/src/L1-L0/axpbypcz-mutation-rotation.md` — composite per-step
  updates that fuse to `AXPBYPCZ` rewrite by this sister theme.

L0 convention anchors:

- `book/src/L0/kspsolver-base-class.md` — the L0 class chapter for
  `BaseKspSolver` (sub-pattern A outer body's anchor).
- `book/src/L0/linalg-iterative-file.md` — the L0 file chapter for the
  per-method bodies (sub-patterns B / C / D anchor).
- `book/src/L0/ksp-factory-file.md` — the factory chapter that
  enumerates the recognition-set boundary (applicability condition
  §1).
- `book/src/L0/mutable-workspace-pattern.md` — the workspace-erase L0
  convention that this theme cites once and does not re-state per
  sub-pattern.
- `book/src/L0/output-arg-vs-receiver.md` — the receiver-vs-output-arg
  L0 convention that the destination-binding rewrite cites once.

Sibling obstruction themes (recognition-set boundary):

- `book/src/L1-L0/minres-iteration.md` — symmetric companion for
  `KrylovSolver::MINRES` (out-of-scope per applicability §1).
- `book/src/L1-L0/bicgstab-iteration.md` — symmetric companion for
  `KrylovSolver::BICGSTAB` (out-of-scope per applicability §1).

Coverage note: this theme cites the **three implemented `IterativeSolver`
subclasses** (`CgSolver`, `GmresSolver`, `FgmresSolver`) at the inner
sub-pattern level. The Palace corpus contains only these three
implemented Krylov methods plus the three aborting enum cases; the cited
set is exhaustive at the inner-method level. The outer
`BaseKspSolver::Mult` is also the unique outer entry point (only one
`BaseKspSolver` template class, two instantiations for `Operator` /
`ComplexOperator`); the cited set is exhaustive at the outer-composition
level. The sub-pattern recognition is **complete** for implemented-Krylov
use within Palace. Verification of the recognition-set complement (the
three aborting enum cases) is by the existing obstruction themes
([`minres-iteration`](./minres-iteration.md),
[`bicgstab-iteration`](./bicgstab-iteration.md)). Full per-step
sub-rewrite verification against the inner bodies is deferred to a
later `lowering-verifier` audit; the sister-theme citation chains
(`apply-linop-mutation-rotation`, `axpby-mutation-rotation`,
`axpbypcz-mutation-rotation`) each carry their own coverage notes for
the per-step decomposition.

## Status

`rough-in` — the four sub-pattern recognition rules are sketched; the
outer-composition rewrite at `BaseKspSolver::Mult` is fully cited; the
three inner per-method bodies are cited at the section-level. Full
per-step sub-rewrite verification (cross-checking each axpy / dot /
Mult invocation inside each Krylov body against the sister themes'
recognition rules) deferred to `lowering-verifier`. The
unimplemented-Krylov boundary is documented as applicability condition
§1 with the sibling obstruction themes carrying their own rough-in
operators.

verified_against:
  - citation: palace/linalg/ksp.cpp:296-310
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: BaseKspSolver<OperType>::Mult definition; four surface concerns visible (BlockTimer at 299, inner ksp->Mult at 300, Mpi::Warning block at 301-307, counter updates at 308-309). Matches sub-pattern A rewrite.
  - citation: palace/linalg/ksp.cpp:299
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: BlockTimer bt(Timer::KSP, use_timer); RAII timer scope spanning the inner ksp->Mult call. Transparent instrumentation; erases at L1.
  - citation: palace/linalg/ksp.cpp:300
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: ksp->Mult(x, y); inner per-method dispatch into one of CgSolver / GmresSolver / FgmresSolver. Argument-name swap (x is the RHS, y is the destination) noted on the L0 anchor chapter.
  - citation: palace/linalg/ksp.cpp:301-307
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: Non-convergence Mpi::Warning side-channel. Formatted residual-ratio warning; emits to Palace MPI-aware logger; returns iterate regardless. L1 rewrite is to result.converged structured field.
  - citation: palace/linalg/ksp.cpp:308-309
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: ksp_mult++; ksp_mult_it += ksp->GetNumIterations(); cumulative-counter mutations. L1 rewrite is to driver-side accumulator over per-call result.iterations.
  - citation: palace/linalg/ksp.cpp:34-58
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: ConfigureKrylovSolver switch; documents the three implemented arms (CG, GMRES, FGMRES) and the three aborting arms (MINRES, BICGSTAB, DEFAULT). Recognition-set boundary for applicability §1.
  - citation: palace/linalg/ksp.cpp:53-57
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: case MINRES: case BICGSTAB: case DEFAULT: MFEM_ABORT(...); three-case fall-through. Unimplemented enum tags abort at factory time; theme's recognition set excludes these.
  - citation: palace/linalg/iterative.hpp:53-55
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: mutable bool converged; mutable double initial_res, final_res; mutable int final_it; — the four L0 slots whose values are copied into L1 SolveResult fields by the rewrite.
  - citation: palace/linalg/iterative.hpp:144
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: mutable VecType r, z, p; CG workspace. Lazy-allocated on first Mult; erased at L1 per mutable-workspace-pattern.
  - citation: palace/linalg/iterative.hpp:190-194
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: GMRES workspace (V Arnoldi basis, r residual, H Hessenberg, s/sn/cs Givens state). Erased at L1.
  - citation: palace/linalg/iterative.hpp:256
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: mutable std::vector<VecType> Z; FGMRES extra workspace for flexible-preconditioner basis.
  - citation: palace/linalg/iterative.cpp:360-486
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: CgSolver<OperType>::Mult definition. Sub-pattern B inner body. Workspace allocation (369-374), initial-guess threading (377-386), inner for-loop (427-464), final-state write-out (484-485) all visible.
  - citation: palace/linalg/iterative.cpp:369-374
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: r.SetSize(A->Height()); z.SetSize(...); p.SetSize(...); + UseDevice(true) for each — canonical lazy-allocation + GPU-residency pattern.
  - citation: palace/linalg/iterative.cpp:377-386
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: if (this->initial_guess) branch: A->Mult(x, r); linalg::AXPBY(1.0, b, -1.0, r); else branch: r = b; x = 0.0; — direct evidence of the initial-guess-policy rewrite.
  - citation: palace/linalg/iterative.cpp:418-419
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: eps = std::max(rel_tol * initial_res, abs_tol); converged = (res < eps); — zero-residual short-circuit supports L1 law 2 (zero-RHS-zero-solution).
  - citation: palace/linalg/iterative.cpp:443
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: A->Mult(p, z); per-step apply_linop invocation. Rewrites by apply-linop-mutation-rotation sub-pattern A.
  - citation: palace/linalg/iterative.cpp:448-449
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: x.Add(alpha, p); r.Add(-alpha, z); per-step axpy updates. Rewrite by axpby-mutation-rotation sub-patterns A (general alpha) and C (literal -alpha as Subtract-shape).
  - citation: palace/linalg/iterative.cpp:484-485
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: final_res = res; final_it = it; — write-out into mutable IterativeSolver base fields read post-call via GetFinalRes() / GetNumIterations().
  - citation: palace/linalg/iterative.cpp:543-705
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: GmresSolver<OperType>::Mult definition. Sub-pattern C inner body. Outer restart loop (563-683), inner Arnoldi loop (615-650), per-restart InitialResidual (566-567), Givens machinery (636-640).
  - citation: palace/linalg/iterative.cpp:733-870
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: FgmresSolver<OperType>::Mult definition. Sub-pattern D inner body. Structurally inherits GMRES with the additional Z basis tracking.
  - citation: palace/linalg/iterative.cpp:252-285
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: InitialResidual helper — factored-out warm-vs-cold initial-residual computation, pc_side-aware. Shared by GMRES and FGMRES sub-patterns.
  - citation: palace/linalg/iterative.cpp:21-32
    verdict: supports
    audited_at: 2026-05-27T17:32:55Z
    note: CheckDot helper; SPD-guard for CG. Load-bearing algebraic precondition enforcement; not transparent. L1 opaque type Solver[A] elides the SPD requirement at signature level but the construction-time choice carries the obligation.
