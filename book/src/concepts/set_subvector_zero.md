# set_subvector_zero

In-place primitive that zeros entries of a vector at a specified index set.

## Signature

```
set_subvector_zero(x: Vector, idx: IndexSet) → ()
    # for i in idx: x[i] ← 0
    # in-place on x
```

For complex vectors, applied componentwise to `x.re` and `x.im` with the
same index set (the index set indexes degrees of freedom, not real numbers).

## Role in the vocabulary

The canonical primitive for **essential boundary-condition enforcement on a
residual or RHS**: after assembling a bilinear-form residual that does not
know about Dirichlet/essential dofs, zero those dofs to project onto the
free-dof subspace before passing to a solver. Distinct from
`set_subvector(x, idx, value)` (the more general form) — the
zeroing-specific name signals BC-enforcement intent at the call site.

## Where it appears

- `divfree` slice, L2 step 2: zero `rhs` on `bdr_eff` before the H1 solve,
  so the projected system `M · ψ = rhs` respects the essential BC.
- Anywhere a partially-assembled operator produces a residual that needs
  essential-BC cleanup before a linear solve.

## Mutation pattern

In-place on `x`. The index set `idx` is not mutated. The signature makes
the in-place semantics legible at the call site without consulting the
implementation.

## L3 lift

Globally, `set_subvector_zero(x, idx)` is `x ← (I − P_idx) x` where `P_idx`
is the projection onto the dofs in `idx`. The L3 tensor-field form is a
mask-multiply; the L2 primitive is the in-place realization.
