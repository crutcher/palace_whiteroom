---
edges:
  reference:
    - concepts/constructed-operator-factory
    - concepts/finest-level-unwrap
    - concepts/apply_linop
    - concepts/axpy
    - concepts/dot
    - concepts/solve-monad
    - concepts/constructed-operators
    - concepts/variant-absorption
    - concepts/sequential-obstruction
    - L4/preconditioning-framework
---
# build-time-vs-run-time-stratification

## Summary

Many operator-composition surfaces in Palace mix **build-time** primitives (factory calls, pointer installs, structural adapters that run once per solve session) with **run-time** primitives (per-iteration `apply_linop` calls, counter accumulations, per-element tensor-field operations). When lifting from L2 to L3 (tensor-field global form), only the run-time primitives participate in the lift — the build-time primitives are scaffolding that materializes the operator graph but does not iterate.

Making this stratification explicit at L3 is the **build-time-vs-run-time stratification** pattern. It is a layer-pattern concept (a methodology primitive about how to structure layer transitions), not a runtime primitive.

## When it applies

A slice has a stratification opportunity when its L2 form mentions both:

- **Build-time primitives**: [`constructed-operator-factory`](./constructed-operator-factory.md), `bind_preconditioner`, [`finest-level-unwrap`](./finest-level-unwrap.md), config-record parsing, FE-space hierarchy queries, etc. These run once at solver construction or at `set_operators` time.
- **Run-time primitives**: [`apply_linop`](./apply_linop.md), [`axpy`](./axpy.md), [`dot`](./dot.md), elementwise products, etc. These run inside the iteration loop.

## The rotation

At L3, the slice's prose should:

1. **List each L2 primitive** with its build-time vs. run-time classification.
2. **State that only run-time primitives participate in the tensor-field lift.** Build-time primitives are excluded by definition — they have no per-element structure to lift.
3. **Surface this for L4**: build-time primitives belong in the constructor / setup phase of the [`solve-monad`](./solve-monad.md) statement; run-time primitives belong in the monadic body. The L4 form preserves the stratification by placing the build-time work in `do { setup ← build_ksp_solver(...); ... }` outside the iteration loop, and the run-time work inside the loop.

## Relationship to other concepts

- [`constructed-operators`](./constructed-operators.md) — the canonical build-time absorption pattern. Constructed operators are built once; their `apply_linop` runs many times. The stratification pattern names the layer at which this build-time/run-time distinction becomes explicit.
- [`variant-absorption`](./variant-absorption.md) — the build-time vs. run-time split is the temporal axis along which variant absorption operates: variants are consumed at build-time, the run-time interface is uniform.
- [`solve-monad`](./solve-monad.md) — at L4, the stratification manifests as setup-before-loop in the monadic structure.
- [`sequential-obstruction`](./sequential-obstruction.md) — sequential obstructions, when they exist, are a property of run-time primitives. Build-time primitives never carry sequential obstructions because they don't iterate.

## Worked example

In [`preconditioning-framework`](../L4/preconditioning-framework.md) (§Context rotation 1; §Algebraic laws 2, 4):

- Build-time: `constructed-operator-factory` (called once at session start to build `ksp` and `pc`), `bind_preconditioner` (one-shot pointer install), `finest-level-unwrap` (executed at `set_operators`).
- Run-time: `apply_linop(ksp, b)` (delegates to the per-method iteration), `apply_linop(pc, r)` (per-iteration preconditioner application), `complex-from-real-lift` (expansion of `apply_linop` for complex pc), `counter-update` (post-solve bookkeeping).

The L3 lift applies only to the run-time set; the build-time set is recorded as composition scaffolding and is otherwise inert at L3.
