---
edges:
  reference: []                    # no book home: L1/set_subvector_zero does not exist; the
                                   # divfree use-site and the L3 mask-multiply lift are described
                                   # in-page. Non-node pointer page; no outbound book edges.
---

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

## L3 tensor-field form

As a global tensor-field operation, `set_subvector_zero(x, S)` is the
linear projector `Z_S : V → V` with

    (Z_S x)_i = 0 if i ∈ S else x_i

i.e., the identity minus the indicator-of-S projector. It is idempotent
(`Z_S ∘ Z_S = Z_S`), self-adjoint with respect to the standard inner
product, and commutes with any operator whose support is disjoint from
`S`. At L2 the implementation is a per-dof loop over `S`; at L3 the
per-dof iteration disappears and `Z_S` is a single tensor-field map.

This lift is clean — no sequential dependency exists across the `i ∈ S`
updates (they are independent writes), so the per-element form rotates
directly to the global form without an obstruction.
