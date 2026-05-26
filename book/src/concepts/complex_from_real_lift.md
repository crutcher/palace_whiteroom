# complex_from_real_lift

The universal mechanism by which any real-valued `mfem::Solver` (BoomerAMG, AMS, MUMPS, SuperLU, STRUMPACK, hypre direct) is lifted to a `Solver<ComplexOperator>`-shaped preconditioner, via Palace's `MfemWrapperSolver<ComplexOperator>`.

## Background

The equivalent-real formulation (Day & Heroux 2001) represents a complex linear system `(A_r + i A_i)(x_r + i x_i) = (b_r + i b_i)` as a real 2N×2N block system. When `A_i = 0` (or is being approximated as zero, as in Palace's preconditioner-assembly path `pc_op = Br + Bi` where the action on `{Re, Im}` decouples), the block system is block-diagonal: a single real solver applied independently to `{Re, Im}` with a sign-flip on the imaginary part to recover the complex-conjugate-aware action.

## Procedure

```
MfemWrapperSolver<ComplexOperator>::Mult(x: ComplexVector, y: ComplexVector):
    real_solver.Mult(x.Real(), y.Real())
    real_solver.Mult(x.Imag(), y.Imag())
    y.Imag() *= -1.0    // conjugate-aware sign flip
```

(Two sub-cases at L2: an `ArrayMult` path when the underlying solver supports batched-vector application; a stack-into-2N / unstack path otherwise. Both share the structural pattern.)

Citations: [palace/linalg/solver.hpp:66-134](../../../reference/palace/linalg/solver.hpp#L66-L134), [palace/linalg/solver.cpp:139-177](../../../reference/palace/linalg/solver.cpp#L139-L177).

## Significance

This is the single point at which the {real, complex} variant axis is absorbed in the preconditioner-construction path. Above this point, Krylov code holds a uniform `Solver<OperType>*` regardless of scalar field; below, it is a real `mfem::Solver` for every concrete preconditioner type. The lift makes the entire Palace preconditioner library (AMS / AMG / sparse-direct) usable for complex problems without per-type complex specialisations.

## Used by

- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md): the canonical example of [`variant-absorption`](./variant-absorption.md) at the scalar-field axis.
- All complex-typed solves in Palace (`SpaceOperator`, eigensolver, time-harmonic driven).
