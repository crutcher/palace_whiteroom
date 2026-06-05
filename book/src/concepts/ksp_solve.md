---
edges:
  reference:
    - L1/ksp_solve
    - concepts/apply_linop
    - concepts/constructed-operators
---
# ksp_solve

The primitive for **invoking a preconditioned Krylov solver** that was
constructed (operator + preconditioner + tolerances) ahead of time.

## Signature

```
ksp_solve(ksp: KSP, b: Vector) → Vector
    # returns x such that A · x ≈ b within ksp.tol
    # A and the preconditioner are bound inside ksp at construction time
```

The pure functional return form (`x = ksp_solve(ksp, b)`) is the L2 surface.
Implementations may write into a caller-supplied buffer for allocation
reasons; that is an L2-transparent optimization and does not change the
semantics.

## Role in the vocabulary

The **constructed-operator** companion to `apply_linop`: where `apply_linop`
is the action of a forward operator, `ksp_solve` is the action of an
approximate inverse. The Krylov method (CG, GMRES, MINRES, ...), the
preconditioner, the convergence tolerance, and the max-iteration count are
all bound at construction; the per-call site is variant-free.

This is the canonical example of *constructed-operator absorption* (see
`constructed-operators.md`): the per-apply L1/L2 procedure calls
`ksp_solve(ksp, b)` uniformly across configurations that differ wildly in
implementation (CG+AMG vs GMRES+ILU vs MINRES+block-Jacobi).

## Where it appears

- `divfree` slice, L2 step 3: `psi ← ksp_solve(ksp, rhs)` for the
  projected H1 Poisson solve. Construction-time configuration (MG vs AMG,
  CG with BoomerAMG preconditioner) is invisible at the call site.
- Any preconditioned-solver call inside an outer iteration (eigensolver
  inner solve, transient implicit step, flexible-Krylov inner step).

## Mutation pattern

Pure functional in the L2 surface: returns a fresh vector. Internally the
solver maintains scratch buffers; those are construction-time state
(`scratch_buffer` in the L1 mutation taxonomy), not part of the L2
interface.

## Dependencies

Depends on `apply_linop` (the solver invokes `A · x` and `M⁻¹ · r` as its
inner loop's basic operations) and on the Krylov method's primitives
(`axpy`, `dot`, `nrm2` for CG; orthogonalization for GMRES; ...).
