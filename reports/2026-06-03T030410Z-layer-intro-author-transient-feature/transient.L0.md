---
kind: feature-surface
feature: transient
level: L0
status: seed
l0_ground_truth:
  - palace/drivers/transientsolver.cpp:24-116 (TransientSolver::Solve)
  - palace/drivers/transientsolver.cpp:118-175 (TransientSolver::GetTimeExcitation — the J(t) / dJ/dt pulse)
  - palace/drivers/transientsolver.hpp:21-30 (class declaration)
  - palace/models/timeoperator.cpp:65-67 (K/C/M assembled once), :311-373 (ODE operator + integrator constructed once), :407-413 (TimeOperator::Step → ode->Step)
lifts_to:
  - book/src/feature/transient.L1.md (the L1 pure-function composition root)
---

# transient — L0 ground-truth surface

The **transient simulation feature** at L0: the cited Palace driver source that realizes the composition root, with the per-stage source ranges that the L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/transientsolver.cpp` and `palace/models/timeoperator.cpp`.

The driver is `TransientSolver::Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const`, returning `std::pair<ErrorIndicator, long long int>` (`palace/drivers/transientsolver.cpp:25-27`; declared `palace/drivers/transientsolver.hpp:26-27`). The class is `TransientSolver : public BaseSolver` with a private `GetTimeExcitation(bool dot) const` and the private `Solve(...) const override` (`transientsolver.hpp:21-30`).

## The composition, in source

The driver is a **state-threaded fold** (the FOLD-pipeline driver, in contrast to the fixed-operator *map* pipelines): assemble the time-domain operators K/C/M once, build the ODE integrator once, then march the persistent field-state through a fixed uniform timestep schedule, advancing it one opaque ODE step at a time. The source stages, in order:

1. **Set up the space + excitation, build the time operator (assemble K/C/M once).** `std::function<double(double)> J_coef = GetTimeExcitation(false)` (`:30`) and `dJdt_coef = GetTimeExcitation(true)` (`:31`) build the time-domain excitation pulse `J(t)` and its derivative `dJ/dt` (`GetTimeExcitation` def `:118`). `SpaceOperator space_op(iodata, mesh)` (`:32`) constructs the operator builder from config + mesh; `TimeOperator time_op(iodata, space_op, dJdt_coef)` (`:33`) builds the time operator ONCE — inside its constructor the three system matrices are assembled once: `K = space_op.GetStiffnessMatrix<Operator>(Operator::DIAG_ZERO)` (`timeoperator.cpp:65`), `C = space_op.GetDampingMatrix<Operator>(Operator::DIAG_ZERO)` (`:66`), `M = space_op.GetMassMatrix<Operator>(Operator::DIAG_ONE)` (`:67`) — the second-order wave-equation `M s'' + C s' + K s = -dJ/dt` operators. This is the L0 site the L1/L4 [`fe_assemble`](../L1/fe_assemble.md) lift (three operators).

2. **Build the ODE integrator once — outside the loop.** Inside `TimeOperator` construction: `op = std::make_unique<TimeDependentFirstOrderOperator>(...)` with `type = mfem::TimeDependentOperator::IMPLICIT` (`timeoperator.cpp:311-313`) builds the first-order-IVP operator once; the `switch (solver.transient.type)` (`:314`+) selects + constructs the library ODE integrator once (`ode = std::make_unique<mfem::GeneralizedAlphaSolver>(rho_inf)` `:320`, or `SDIRK23Solver` `:327`, or `ARKStepSolver` `:335`, or `CVODESolver` `:360` — library-owned). This is the operator-capture-once the L4 [`fold_solve`](../L4/fold_solve.md) `op : OpParams` `readonly` stratum types.

3. **Set up the fixed schedule.** `double delta_t = iodata.solver.transient.delta_t` (`:35`) — the uniform timestep; `int n_step = config::GetNumSteps(0.0, iodata.solver.transient.max_t, delta_t)` (`:36`) — the fixed schedule length. The schedule is a fixed uniform `[Time]` list (the L4 [`fold_solve`](../L4/fold_solve.md) `fixed-list` default surface). `PostOperator<ProblemType::TRANSIENT> post_op(iodata, space_op)` (`:40`) sets up the postprocess.

4. **The state-threaded time-march (the fold).** `for (int step = 0; step < n_step; step++)` (`:77`) is the fold loop over the fixed schedule. `if (step == 0) { ...; time_op.Init(); }` (`:85-90`) seeds the initial field-state `s0` (the zero IC); `else { time_op.Step(t, delta_t); }` (`:92-93`) advances the field-state one step. The step bottoms out in `TimeOperator::Step(double &t, double &dt)` (`timeoperator.cpp:407`) → `ode->Step(sol, t, dt)` (`:410`) — the **opaque MFEM `ODESolver` step advancing the persistent `sol` field-state in place; the prior step's `sol` is the next step's input — the genuine `foldl`**. Per step the fields are read out `const Vector &E = time_op.GetE()` (`:98`) / `const Vector &B = time_op.GetB()` (`:99`) and postprocessed `post_op.MeasureAndPrintAll(step, E, B, t, J_coef(t))` (`:104`), then the error estimate is accumulated (`:107-108`). This loop is the L0 site the L4 [`fold_solve`](../L4/fold_solve.md) state-threaded fold lift; the per-step `ode->Step` is the opaque per-step body (`obstruction (opaque-library-ownership)` at the lowering layer).

5. **Finalize → the physical product.** After the loop, `time_op.PrintStats()` (`:112`); `post_op.MeasureFinalize(indicator)` (`:114`) finalizes the time-domain postprocess (the trajectory of port voltages/currents, fields, energy measured per step). The driver returns `{indicator, space_op.GlobalTrueVSize()}` (`:115`) — the error indicator + the global true-dof count. The closing brace is `:116`.

## Inputs / outputs (the feature surface, in source)

- **Input — config.** `iodata` (the `IoData` config surface) + `mesh`, consumed by `SpaceOperator space_op(iodata, mesh)` (`:32`) and `TimeOperator time_op(iodata, space_op, dJdt_coef)` (`:33`). The excitation pulse is `GetTimeExcitation(false/true)` (`:30-31`, def `:118`); the schedule is `iodata.solver.transient.delta_t` / `.max_t` (`:35-36`).
- **Output — the physical product.** The **time-domain field-state trajectory** — the per-step `(E, B)` fields (`time_op.GetE()` `:98` / `time_op.GetB()` `:99`) measured by `post_op.MeasureAndPrintAll(step, E, B, t, J_coef(t))` (`:104`) and finalized by `post_op.MeasureFinalize(indicator)` (`:114`), plus the returned `{indicator, space_op.GlobalTrueVSize()}` (`:115`).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`transient.L1`](./transient.L1.md) (the in-place `ode->Step(sol, ...)` advance → a value-returning pure `step :: State -> Time -> State`, the persistent `sol` → the fold's threaded carry) and the L4 combinator composition root [`transient.L4`](./transient.L4.md) (the time-march loop → the [`fold_solve`](../L4/fold_solve.md) state-threaded fold; the K/C/M assembly → the [`fe_assemble`](../L4/fe_assemble.md) folds). The per-operator L1>L0 mutation-rotation themes of the constituent ops carry the per-write lifts; this feature surface records the composition-root *site map* (which driver range realizes which composed stage). The per-step body's opaque-library internals are recorded at the L4>L3 [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md) theme, not here.

## Status

`seed` — the L0 ground-truth surface for the transient feature (the spine's first **fold-pipeline** witness), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic.L0](./electrostatic.L0.md) / [magnetostatic.L0](./magnetostatic.L0.md) exemplars. Every stage is a cited range into `palace/drivers/transientsolver.cpp` + `palace/models/timeoperator.cpp`, confirmed on-disk via palace-codemap `read_range` this dispatch (close-brace discipline: `Solve` spans `:24-116`, the loop `:77-109`, the `Step` method `:407-413`). The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
