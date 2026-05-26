# capability-typing

## Summary

A *capability type* is a phantom-typed brand on a value that records the value's intended role in the surrounding system, without changing its run-time representation. Capability typing is the discipline of distinguishing values that share an underlying type but play distinct semantic roles, by attaching a (zero-runtime) brand that the type system enforces.

In the L4 calculus, capability typing is the standard rotation for promoting role-by-convention ("this field is named `pc_op`, so it's the pc-assembly operator") to role-by-type ("this field is `PcAssemblyOp<E>`, distinct from `TrueOp<E>` at the type level").

## Form

```ts
type RawT = ...;                                       // underlying type
type RoleA<E> = RawT & { readonly __cap: "A" };       // branded
type RoleB<E> = RawT & { readonly __cap: "B" };       // branded, distinct from RoleA

declare function asRoleA(x: RawT): RoleA<E>;          // smart constructor
declare function asRoleB(x: RawT): RoleB<E>;          // smart constructor
```

The brand `__cap` is phantom: there is no run-time field, no allocation, no dispatch. The smart constructors are the identity at run time; their job is to commit to a role at the point of construction so downstream signatures can demand a specific brand.

## When to use

Reach for capability typing when a layer state-bundle has two-or-more fields of the same underlying type playing distinct roles, AND the cost of confusing them is non-trivial (incorrect convergence, silent miscompute, security-equivalent error). Concretely, in the Palace L4 calculus:

- **`(op, pc_op)` in `BaseKspSolver`** — both are `Op<E>`; confusing them produces a wrong preconditioned Krylov iteration that may still converge to a wrong answer. See [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L4 v0.2.
- **(planned) `(coarse, fine)` operator pairs in geometric multigrid** — both are `Op<E>`; confusing them inverts the V-cycle direction.
- **(planned) `(primal, dual)` in saddle-point solvers** — both are `Vec<E>`; confusing them produces a wrong block-system solve.

Do NOT reach for capability typing when:

- The two roles are already disambiguated by their underlying type (e.g., `Op<Real>` vs `Op<Complex>` — the scalar field already separates them).
- The cost of confusion is caught loudly at the L0 layer (e.g., shape mismatch on `Mult`).
- The two values are interchangeable at the calculus level and the role distinction is purely a naming convenience.

## Relation to variant absorption

Capability typing is *complementary* to [`variant-absorption`](./variant-absorption.md). Variant absorption hides axes of *variation* (krylov-method, pc-type, scalar-field) behind a uniform interface; capability typing distinguishes axes of *role* (true-operator vs pc-assembly-operator) within a uniform interface. A field can simultaneously be absorbed (its scalar-field variant is hidden) AND brand-typed (its role is fixed): `TrueOp<E>` is uniform across `E ∈ {Real, Complex}` but distinct from `PcAssemblyOp<E>`.

## Relation to state stratification

Capability typing operates *within* a single stratum of [`state-stratification`](./state-stratification.md). The brands distinguish roles among same-stratum values (e.g., two sim-state operators); they do not stratify state by lifetime (build-time vs run-time) — that is state-stratification's job. The two disciplines compose: a state field can be (sim-state, role-A) vs (sim-state, role-B), or (build-time-params, role-A), etc.

## Background

The phantom-type / brand pattern is standard in dependently-typed and refinement-typed languages (Haskell's `newtype` wrappers, F*'s erasable refinements, Coq's `Definition` wrappers around dependent pairs, Rust's zero-sized marker types). The capability terminology comes from the capability-security literature (Miller 2006; Mark Miller's dissertation): a capability is an unforgeable token of authority. In the L4 calculus context here, the "authority" is role-specific: holding a `TrueOp<E>` is the authority to act as the Krylov-method's iteration operator; holding a `PcAssemblyOp<E>` is the authority to act as the preconditioner's construction operator.

The L4 calculus uses capability types in their *type-checking-only* form: the brand is enforced at the type system level, not by a run-time capability-machine. This is the same usage Haskell's `ST` monad makes of the `s` parameter: the brand prevents misuse but has no run-time presence.

## See also

- [`state-stratification`](./state-stratification.md) — stratifies state by lifetime; capability typing distinguishes roles within a stratum.
- [`variant-absorption`](./variant-absorption.md) — hides variant axes; capability typing surfaces role axes.
- [`solve-monad`](./solve-monad.md) — the L4 monad in whose state-bundles capability types appear.
- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L4 v0.2 — the canonical first use site (TrueOp / PcAssemblyOp brands on the KSP binding).
