# File — `palace/linalg/ksp.cpp`

A file-overview reference note. The Krylov-solver factory: where Palace's enum-based solver-type selector dispatches into solver constructors. This file is the anchor for the **advertised-but-unimplemented pattern** that drives the obstruction themes for MINRES and BiCGStab.

## At a glance

The file is small (a few hundred lines) and has two main factory functions in an anonymous namespace plus a small public surface:

- **`ConfigureKrylovSolver<OperType>`** (lines 26–101). Switches on `linear.krylov_solver` (a `KrylovSolver` enum). The implemented cases construct a solver and configure it; the unimplemented cases abort.
- **`ConfigurePreconditionerSolver<OperType>`** (lines 125 onward). Switches on `linear.type` (a `LinearSolver` enum) and constructs the corresponding preconditioner (AMS, BOOMER_AMG, SUPERLU, STRUMPACK, MUMPS, JACOBI, …). Each unsupported build-time configuration aborts with a specific message.
- **Public entry point** that combines the two factories and assembles the final solver.

## The enum-routed dispatch in `ConfigureKrylovSolver`

The switch at lines 34–58 has six branches:

```cpp
switch (type)
{
  case KrylovSolver::CG:
    ksp = std::make_unique<CgSolver<OperType>>(comm, print);
    break;
  case KrylovSolver::GMRES:
    { /* GMRES + SetRestartDim */ }
    break;
  case KrylovSolver::FGMRES:
    { /* FGMRES + SetRestartDim */ }
    break;
  case KrylovSolver::MINRES:
  case KrylovSolver::BICGSTAB:
  case KrylovSolver::DEFAULT:
    MFEM_ABORT("Unexpected solver type for Krylov solver configuration!");
    break;
}
```

Three solver types are implemented (`CG`, `GMRES`, `FGMRES`); three trigger `MFEM_ABORT` (`MINRES`, `BICGSTAB`, `DEFAULT`). The fall-through on the three abort cases is deliberate — all three share the same abort message. After the switch, common configuration applies (lines 59–62): initial guess, relative tolerance, max iterations. GMRES-specific configuration follows (lines 64–95): preconditioner side, orthogonalisation method. A timer is enabled at line 98.

## The "advertised-but-unimplemented" pattern

`MINRES` and `BICGSTAB` are **enumerated solver types** — they appear in the `KrylovSolver` enum, the configuration parser accepts them as inputs, and the factory recognises them as valid switch arms — but the implementation aborts at runtime. This is the load-bearing observation behind two L1>L0 obstruction themes:

- [`L1-L0/minres-iteration`](../L1-L0/minres-iteration.md) — proposes the speculative L1 operators `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`. Harvester promotion gated on Palace gaining the implementation (or scope widening to vendored MFEM; see open question `bicgstab-mfem-reanchor-policy`).
- [`L1-L0/bicgstab-iteration`](../L1-L0/bicgstab-iteration.md) — proposes speculative L1 operators `bicgstab_step`, `omega_update`, `stabilisation_update`. Same gating.

`DEFAULT` aborting alongside `MINRES` and `BICGSTAB` indicates that the configuration layer is expected to resolve `DEFAULT` to a concrete enum value before reaching the factory — the factory does not pick a default itself. This is a separate concern (configuration layering) and not part of the obstruction theme.

## The implemented branches

For the three implemented branches (`CG`, `GMRES`, `FGMRES`), the factory:

- Constructs the solver template-instantiated on `OperType` (which is `Operator` or `ComplexOperator` — the element-type axis from [`mfem-vector-types`](./mfem-vector-types.md)).
- For GMRES / FGMRES, calls `SetRestartDim(linear.max_size)` (lines 42, 49) — the restart parameter.
- For GMRES / FGMRES, downstream of the switch, configures preconditioner side (lines 73–86) and orthogonalisation method (lines 92–94).

The solver classes themselves (`CgSolver`, `GmresSolver`, `FgmresSolver`) live in `palace/linalg/iterative.{hpp,cpp}` and are the L0 anchors for the firm [`L2/krylov-step`](../L2/krylov-step.md) kernel + [`L1/ksp_solve`](../L1/ksp_solve.md) / [`L2/ksp_solve`](../L2/ksp_solve.md) outer driver.

## Referenced from

- [`L1-L0/minres-iteration`](../L1-L0/minres-iteration.md) — obstruction theme; cites `ksp.cpp:53-57` as the enum-routed-abort anchor.
- [`L1-L0/bicgstab-iteration`](../L1-L0/bicgstab-iteration.md) — obstruction theme; same anchor.
- [`L1/index`](../L1/index.md) "Working Notes" — references the abort pattern when discussing rough-in entries from obstruction themes.

## Evidence

- `palace/linalg/ksp.cpp:26-101` — `ConfigureKrylovSolver` factory.
- `palace/linalg/ksp.cpp:34-58` — the switch on `KrylovSolver` type.
- `palace/linalg/ksp.cpp:53-57` — the three-case fall-through to `MFEM_ABORT` for `MINRES` / `BICGSTAB` / `DEFAULT`.
- `palace/linalg/ksp.cpp:59-62` — common post-switch configuration (initial guess, tolerance, max iterations).
- `palace/linalg/ksp.cpp:64-95` — GMRES-specific configuration (preconditioner side, orthogonalisation).
