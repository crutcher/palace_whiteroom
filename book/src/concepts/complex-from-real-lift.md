# complex-from-real-lift

The L2 primitive expressing the action of a *real* preconditioner solver on a *complex* operand vector. Concretely: given a real solver `M_real : Vec → Vec` and a complex residual `r = r_re + i·r_im`, the lift returns `z = z_re + i·z_im` where `z_re = M_real(r_re)` and `z_im = -M_real(r_im)` (the conjugate-aware sign flip on the imaginary part).

## Background

The equivalent-real formulation of complex linear systems (Day & Heroux 2001) treats `(K_re + i·K_im) x = b` as a `2N×2N` real block system. When `K_im = 0` (or is intentionally dropped from the preconditioner-assembly operator `pc_op`), the preconditioner block-decouples and reduces to two independent real solves. The conjugate sign flip arises because Palace's complex inner product uses the conjugate-aware convention `⟨x, y⟩ = x^H y`; preconditioning the *adjoint* of the residual is the operationally-correct lift when the underlying real factorisation is computed against `pc_op = Br + Bi` (a real combination), not `Br + i·Bi`.

The canonical Palace site is `MfemWrapperSolver<ComplexOperator>::Mult` (`palace/linalg/solver.cpp:139-177`), called from inside the Krylov iteration's `apply_preconditioner` funnel.

## L2 form

```
complex-from-real-lift(M_real: Solver<Operator>, r: ComplexVector) → z: ComplexVector:
    z.Re ← apply_linop(M_real, r.Re)
    z.Im ← apply_linop(M_real, r.Im)
    z.Im ← scal(-1, z.Im)                  // conjugate-aware sign flip
    return z
```

The two `apply_linop` calls are independent and could run concurrently; the L2 form preserves the sequential statement and notes the parallelism opportunity as an L3 implementation freedom.

## Where this primitive sits in the framework

[`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) names this primitive as the L2 unfolding of `MfemWrapperSolver::Mult` on the `ComplexOperator` template specialisation. The real-solver specialisation is a passthrough (`apply_linop(M_real, r)` directly) and does NOT instantiate this primitive.

The lift is one of the operand-scalar-field absorption mechanisms (variant axis 4 in the framework slice's L1 form). The other mechanism is the compile-time `OperType` template parameter; the lift is the run-time half.

## Used by

- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L2.
- Future per-method slices when they describe how their L2 `apply_preconditioner` call expands on complex operands.

## See also

- [`apply_linop`](./apply_linop.md) — the wrapped primitive.
- [`scal`](./scal.md) — the in-place sign-flip primitive.
- [`constructed-operators`](./constructed-operators.md) — the lift is itself a constructed-operator route to scalar-field absorption.
