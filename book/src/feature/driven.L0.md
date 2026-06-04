---
kind: feature-surface
feature: driven
level: L0
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: palace/drivers/drivensolver.cpp:37-75
      kind: cites-evidence
    - target: palace/drivers/drivensolver.cpp:77-229
      kind: cites-evidence
    - target: palace/drivers/drivensolver.cpp:231
      kind: cites-evidence
    - target: palace/drivers/drivensolver.hpp:22-34
      kind: cites-evidence
  reference:
    - feature/driven.L1
---

# driven — L0 ground-truth surface

The **driven (frequency-domain) simulation feature** at L0: the cited Palace driver
source that realizes the composition root, with the per-stage source ranges that the
L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a
`(file:start-end)` citation into `palace/drivers/drivensolver.cpp`.

The driver entry point is `DrivenSolver::Solve(const
std::vector<std::unique_ptr<Mesh>> &mesh) const`, returning `std::pair<ErrorIndicator,
long long int>` (`palace/drivers/drivensolver.cpp:37-75`; declared
`palace/drivers/drivensolver.hpp:29-30`). The class is `DrivenSolver : public
BaseSolver` with private `SweepUniform(...)` / `SweepAdaptive(...)` helpers and the
private `Solve(...) const override` (`drivensolver.hpp:22-34`). `Solve` constructs the
`SpaceOperator`, decides uniform-vs-adaptive, and dispatches: `return {adaptive ?
SweepAdaptive(space_op) : SweepUniform(space_op), space_op.GlobalTrueVSize()}`
(`:73-74`). The **uniform** sweep `SweepUniform` (`:77-229`) is the
[`frequency_sweep`](../L4/frequency_sweep.md) operator-varying map this feature column
composes; the **adaptive** sweep `SweepAdaptive` (`:231`) is the state-generated
greedy PROM fold (the [`fold_solve`](../L4/fold_solve.md) `schedule-source =
state-generated` sibling, NOT this column's composition — noted for the
uniform/adaptive = map/fold split).

## The composition, in source

The driver is an **operator-VARYING** sweep: assemble the fixed operator basis `{K,
C, M}` once, then sweep the swept-frequency family, **rebuilding the system operator
`A(ω)` and re-capturing it inside the loop** before each solve, reducing per-ω to the
frequency response. The source stages of `SweepUniform`, in order:

1. **Assemble the fixed operator basis `{K, C, M}` ONCE — before the loop.** `auto K =
   space_op.GetStiffnessMatrix<ComplexOperator>(Operator::DIAG_ONE)` (`:91`), `auto C =
   space_op.GetDampingMatrix<ComplexOperator>(Operator::DIAG_ZERO)` (`:92`), `auto M =
   space_op.GetMassMatrix<ComplexOperator>(Operator::DIAG_ZERO)` (`:93`) assemble the
   three fixed basis operators ONCE (the source comment `:89-90`: "Assemble the linear
   system for the initial frequency (so we can call KspSolver::SetOperators). Compute
   everything at the first frequency step."); `const auto &Curl =
   space_op.GetCurlMatrix()` (`:94`) grabs the curl operator for the B-field
   post-process. This is the L0 site the L1/L4 [`fe_assemble`](../L1/fe_assemble.md)
   (×3) lift — the once-captured `readonly` construction stratum (the basis, NOT the
   per-ω operator).

2. **Build the solver once; the operator is NOT captured here.** `ComplexKspSolver
   ksp(iodata, space_op.GetNDSpaces(), &space_op.GetH1Spaces())` (`:98`) builds the
   Krylov solver from config + the Nédélec H(curl) spaces (with the H1 spaces for the
   auxiliary-space preconditioner). Note the load-bearing contrast with the
   fixed-operator drivers: the solver is built once, but `SetOperators` is **NOT**
   called here — the operator capture is *deferred into the loop* (the source comment
   `:97`: "The operators are constructed for each frequency step and used to initialize
   the ksp.").

3. **Set up the swept-frequency family + per-ω scratch.** `const auto &omega_sample =
   iodata.solver.driven.sample_f` (`:80`) — the swept frequency family `[Scalar]`;
   `ComplexVector RHS(Curl.Width()), E(Curl.Width()), B(Curl.Height())` (`:102`) — the
   per-ω RHS / solution / B-field scratch. The outer excitation loop `for (const auto
   &[excitation_idx, excitation_spec] : port_excitations)` (`:153`) iterates the
   port-excitation set.

4. **The operator-VARYING per-ω sweep (the inner loop).** `for (std::size_t omega_i =
   ...; omega_i < omega_sample.size(); omega_i++)` (`:168-170`) iterates the swept
   frequencies. Per ω (`auto omega = omega_sample[omega_i]`, `:172`): **rebuild the
   operator INSIDE the loop** — `auto A2 =
   space_op.GetExtraSystemMatrix<ComplexOperator>(omega, Operator::DIAG_ZERO)` (`:175`,
   the ω-dependent extra term) then `auto A = space_op.GetSystemMatrix(1.0 + 0.0i, 1i *
   omega, -omega * omega + 0.0i, K.get(), C.get(), M.get(), A2.get())` (`:176-177`, the
   affine-in-ω combination `A(ω) = K + iω·C − ω²·M + A2`, the
   [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) rebuild), the
   per-ω preconditioner `auto P = space_op.GetPreconditionerMatrix<ComplexOperator>(...)`
   (`:178-179`); **capture the rebuilt operator INSIDE the loop** — `ksp.SetOperators(*A,
   *P)` (`:180`) — the operator-VARYING placement (the negation of the fixed-operator
   drivers' `SetOperators`-outside-the-loop hoist, the exact scope boundary that scopes
   driven out of [`solve_family`](../L4/solve_family.md) and into
   [`frequency_sweep`](../L4/frequency_sweep.md)'s `operator-capture = per-element`
   axis); form the per-ω RHS `space_op.GetExcitationVector(excitation_idx, omega, RHS)`
   (`:194`); solve the rebuilt system `ksp.Mult(RHS, E)` (`:196`) into the per-ω
   solution `E`. This loop is the L0 site the L4
   [`frequency_sweep`](../L4/frequency_sweep.md) map (and per-member L1/L4
   [`ksp_solve`](../L1/ksp_solve.md)) lift; the inner-loop close brace is `:221`.

5. **Per-ω reduction → the physical product.** Inside the loop, after the solve: the
   B-field recovery `Curl.Mult(E.Real(), B.Real())` / `Curl.Mult(E.Imag(), B.Imag())`
   then `B *= -1.0 / (1i * omega)` (`:205-207`, `B = −1/(iω) ∇×E`); the per-ω
   measurement `auto total_domain_energy = post_op.MeasureAndPrintAll(excitation_idx,
   int(omega_i), E, B, omega)` (`:215-216`) computes + records the per-frequency
   response (S-parameters, energy, fields); the error-estimate update `AddEstimate(E, B,
   total_domain_energy, indicator)` (`:220`). After both loops, `post_op.MeasureFinalize(indicator)`
   (`:227`) finalizes; `return indicator` (`:228`). This is the L0 site the **driven
   output-product surface** (the S-parameter reduction) lifts — a dedicated
   output-product column, NOT lifted in this driver feature surface (forward-ref).

The `Solve` entry returns `{SweepUniform/SweepAdaptive result,
space_op.GlobalTrueVSize()}` (`:73-74`) — the error indicator + the global true-dof
count.

## Inputs / outputs (the feature surface, in source)

- **Input — config.** `iodata` (the `IoData` config surface) + `mesh`, consumed by
  `SpaceOperator space_op(iodata, mesh)` (`:41`) and `ComplexKspSolver ksp(iodata, ...)`
  (`:98`). The swept frequency family is `iodata.solver.driven.sample_f` (`:45`, `:80`);
  the uniform-vs-adaptive decision is `iodata.solver.driven.adaptive_tol > 0.0` (`:47`);
  the port-excitation set is `space_op.GetPortExcitations()` (`:42`, `:153`).
- **Output — the physical product.** The per-ω frequency response (S-parameters +
  per-frequency field/energy measurements) written by the per-ω
  `post_op.MeasureAndPrintAll(...)` (`:216`) + `post_op.MeasureFinalize(indicator)`
  (`:227`), plus the per-ω fields `E` / `B` (`:196`, `:205-207`).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root
[`driven.L1`](./driven.L1.md) (each in-place driver write → a value-returning pure
operator; the per-ω comprehension rebuilds the operator inside its body) and the L4
combinator composition root [`driven.L4`](./driven.L4.md) (the per-ω loop → the
[`frequency_sweep`](../L4/frequency_sweep.md) operator-VARYING map; the per-ω rebuild →
[`assemble_frequency_operator`](../L4/assemble_frequency_operator.md); the basis
assemble → [`fe_assemble`](../L4/fe_assemble.md)). The per-operator L1>L0 rotation
themes of the constituent ops carry the per-write lifts (including the per-ω
`SetOperators`-inside-the-loop capture, in
[`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md));
this feature surface records the composition-root *site map* (which driver range
realizes which composed stage). The adaptive sweep `SweepAdaptive` (`:231`) is the
[`fold_solve`](../L4/fold_solve.md) state-generated fold sibling, NOT lifted by this
uniform-sweep column.

## Status

`firm` — the L0 ground-truth surface for the driven feature, a **leaf feature
column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring
the [electrostatic.L0](./electrostatic.L0.md) / [magnetostatic.L0](./magnetostatic.L0.md)
exemplars but at the operator-VARYING corner (the `SetOperators`-inside-the-loop
witness). **Promoted `seed → firm` cycle-085** with the column (the L0 surface tracks
the column maturity under the OWN-COMPOSITION promotion rule; the driven column's
directly-owned constituents — `fe_assemble`, `assemble_frequency_operator`,
`frequency_sweep`, `ksp_solve` — are all firm, and the S-parameter reduction is a
sibling cross-link, not a blocker). Every stage is a cited range into
`palace/drivers/drivensolver.cpp`, confirmed on-disk via palace-codemap `read_range` +
direct on-disk `Read` (close-brace discipline on the loop / function END lines). The
chapter's evidence IS the driver-source range + the per-stage site map to the
constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
The S-parameter reduction (stage 5) is the driven output-product surface, presented as
its own [`sparameters`](./sparameters.L0.md) column (a sibling cross-link).
