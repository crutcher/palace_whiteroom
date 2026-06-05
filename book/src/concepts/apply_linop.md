---
edges:
  reference:
    - L1/apply_linop               # authoritative operator entry (definition)
    - concepts/constructed-operators  # sibling concept (constructed-operator unfolding)
    - L2/krylov-step               # use-site cross-link (matvec count / per-step apply)
---

# apply_linop

Base primitive: `y ← L · x` for an abstract linear operator `L` and vectors `x`, `y`. The interface is operator-shaped, not matrix-shaped: `L` may be a sparse matrix, a matrix-free operator (e.g., FE assembly closure), a composition of operators (`L = A · B`), or a preconditioner. The caller never inspects `L`'s representation.

## Contract

- Pure with respect to its operands: `apply_linop(L, x)` produces `y` without mutating `L` or `x` (in-place output is acceptable as a workspace convention).
- Shape: `L : V_in → V_out`; `x ∈ V_in`, `y ∈ V_out`. The two spaces may differ (rectangular operators).
- Linearity is implicit in the name. Nonlinear actions go through a different primitive.

## Role in the L2 vocabulary

At L2, operator actions are not unfolded into per-element loops; they are treated as opaque primitives because:

- The operator may be matrix-free (FE-assembly-free, Jacobian-action).
- The operator may be a sparse matvec, a multigrid V-cycle, an FFT-based solve, or any composition thereof.
- The iterative solver's correctness argument depends only on `apply_linop`'s linearity, not its internal structure.

This is the natural primitive at which to count operator applications — the "matvec count" / "preconditioner-apply count" used to characterise iterative-solver convergence. Each `apply_linop` call is one such application.

## Role in higher-layer rotations

`apply_linop` is the unit of operator-cost accounting: at L2 and above, an algorithm's per-step cost is typically dominated by the number of `apply_linop` calls. GMRES's inner step uses 1–2 `apply_linop` calls (one for `A`, optionally one for `M`). CG uses one `A` and one `M` per step.

## Constructed operators

When a slice's L1 names a *constructed operator* (e.g., `apply_BA` in GMRES, see [concept: constructed-operators](./constructed-operators.md)), that operator's L2 unfolding is typically a small chain of `apply_linop` calls — the constructed operator hides the chain at L1 while preserving it as the L2 primitive sequence. The fact that `apply_linop(BA, v, w)` may internally invoke two operator applications (`apply_linop(M, v, z); apply_linop(A, z, w)`) is an unfolding choice, not a change of primitive.

## Relation to matvec

The special case where `L` is a concrete sparse matrix and `apply_linop(L, x, y)` is a `y ← L·x` SpMV is one realisation. The L2 vocabulary uses `apply_linop` rather than `matvec` because matrix-free operators (FE-assembly-free, Jacobian-action, multigrid cycles) are first-class and should not be linguistically demoted.

## Palace mapping

- `mfem::Operator::Mult` and its complex analogue.
- `palace::ComplexOperator::Mult`.
- Palace `Operator::Mult(x, y)` and `ComplexOperator::Mult(x, y)` are the in-tree realisations of this primitive.
- The `OperType` template parameter on `GmresSolver` and `IterativeSolver` (`palace/linalg/iterative.hpp:152–217`) parametrises which `apply_linop` variant is instantiated.
- Any class implementing the operator-action interface (preconditioners, FE assembly closures, sum/product operators).

## L2 use in divfree

The `divfree` slice uses `apply_linop` for both forward operator actions in
the per-apply path:

- `rhs ← apply_linop(WeakDiv, y)` — partially-assembled Nedelec→H1 weak
  divergence applied to a Nedelec field.
- `t   ← apply_linop(Grad, psi)` — H1→Nedelec discrete gradient applied to
  the H1 correction potential.

Both are pure functional in the L2 surface. The construction-time
distinction between matrix-assembled and partial-assembly operators is
transparent at L2 — `apply_linop` is the uniform interface, and the
operator's internal representation is its own concern.

## L3 tensor-field form

As a global tensor-field operation, `apply_linop(A, x)` is the linear
map `A : V → W` evaluated at `x ∈ V`, returning `A x ∈ W`. At L2 the
implementation may iterate over rows / quadrature points / element
contributions; at L3 those iterations disappear and `A` is a single
linear-map node.

The lift is clean for assembled-matrix operators (the matvec is
embarrassingly data-parallel modulo reduction associativity choices),
and for matrix-free operators (each element-local apply is
independent, with a reduction collecting contributions). The reduction
associativity is a load-bearing claim when `A` involves quadrature
summation in non-deterministic order; see `dot` for the analogous
concern. For exactly-representable element-local applies followed by
assembly via `Z_S`-like masking, no such concern arises.

When `A` is itself constructed from a composition (e.g., a triple
product `Gᵀ M G`), L3 may either keep the composition explicit
(`apply_linop(Gᵀ, apply_linop(M, apply_linop(G, x)))`) or fuse it into
a single operator-valued node, depending on whether the slice cares
about the intermediate fields.

## Concept: `apply_linop`

Apply a linear operator to a vector: `y ← A x` (or `y ← A x + β y` in
the accumulating form). The fundamental Krylov primitive.

## Background

The matrix-free matrix-vector product — the abstraction over BLAS-2
`gemv` and beyond. In Palace, linear operators are not necessarily
stored as matrices; an `Operator` exposes a `Mult(x, y)` virtual call
that may perform a sparse SpMV, an FE element-wise assemble-on-the-fly,
or a composition of nested operators. The `apply_linop` role is the
client-side view: a black-box `y ← A x` whose internals are the
operator implementor's concern.

## Signature (canonical)

```
apply_linop(A, x) → y       // pure functional form, y fresh
apply_linop(A, x, y)        // mutating: y ← A x (overwrites y)
```

Palace's C++ form is `A.Mult(x, y)` (mutating, overwrites `y`).

## Variant axes

- **Scalar field**: real (`Operator`) vs. complex (`ComplexOperator`);
  the operator type carries the scalar field, so the primitive contract
  is parametric.
- **Composition**: `M⁻¹ ∘ A` (preconditioned operator) is itself an
  `apply_linop` whose internals call two underlying applies — visible
  at L2 when needed, transparent at L1.

## Slices that use this primitive

- [`krylov-step` (CG instance)](../L2/krylov-step.md) — single application per inner iteration
  (`A p`).
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — single application per Arnoldi
  step (`A v_j` or `M⁻¹ A v_j` via the constructed-operator
  `apply_BA`).
