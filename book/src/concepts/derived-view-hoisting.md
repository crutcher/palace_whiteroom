# Derived-view hoisting

*A state-hiding rotation pattern for L4 forms.*

## Pattern

A derived scalar (or small tensor) `v = f(s)` where `s` is some other piece of iteration state should NOT be stored as a separate state field. It should be either:

1. **Recomputed on demand** at consumer sites (when `f` is cheap and the value is read rarely), OR
2. **Hoisted to a step-output field** (when the value participates in §3.8 demand-driven pruning — i.e., when downstream consumers may or may not consume it).

Storing `v` as a state field creates a *redundant invariant* the step body must maintain on every transition (`s'.v == f(s')`), and forces computation of `v` even when no consumer reads it.

## Worked example: CG residual norm

In the firm [`krylov-step` (CG instance)](../L2/krylov-step.md) the residual norm `res = sqrt|beta|` is a derived view of the iteration's stored inner product `beta`. Two design choices:

- **Bad**: `CgState` includes both `beta: Scalar` and `res: Scalar`. Every step must compute `res` to maintain the invariant, even when residual history is never read. The §3.8 pruning property is defeated by the state schema.
- **Good** (v0.4 revision): `CgState` includes only `beta`. The step body computes `res = sqrt|beta|` as a local binding and returns it in the step-output record `{ state, residual_norm }`. `iterate_while` accumulates `residual_norm`s into a trajectory; consumers reading only `.final_state` cause the residual computation to be pruned.

## Worked example: Chebyshev initial-guess branch (control-flow boundary)

The CG example hoists a derived view at the *state-shape* boundary (a redundant state field becomes a step-output). The same pattern applies at the *control-flow* boundary, where a derived view replaces what would otherwise be a constructed-operator variant axis. The Chebyshev smoother's L4 form (slice: chebyshev §L4 "Initial-guess shape: branch vs. derived view") is the canonical example.

The `apply` body opens with a one-shot conditional on a Boolean parameter `initial_guess`:

```haskell
r0 <- if it == 1 && not initial_guess
        then do { writeY zero; pure x }       -- y := 0; r0 = x
        else do
          y  <- readY
          ay <- applyLinop op.A y
          pure (x .-. ay)                      -- r = x - A y
```

The `initial_guess = false` path is the algebraic *specialization* of the `true` path under `y_in = 0`: writing `y := 0` establishes the precondition that makes `A y_in = 0`, so `r = x - A y_in = x`. The branch is a **degenerate-case absorption**, not a residual variant axis — both cases are unified by the single invariant `r = x - A y_post_zeroing`.

- **Bad**: promote `initial_guess` to a constructed-operator variant — `ChebOpWithGuess` vs. `ChebOpNoGuess`, each carrying a `hasInitialGuess: Bool` field. This inflates the closure-type lattice to four (`Kind4 × {guess, no-guess}` and `Kind1 × {guess, no-guess}`) for no structural benefit; the polynomial-recurrence machinery is genuinely insensitive to `initial_guess`.
- **Good**: keep `initial_guess: Bool` as a *per-call argument* to `apply`. The branch fires at most once per call (only when `it == 1 && not initial_guess`) and only on the residual-computation step; the rest of the per-sweep procedure is uniform across both cases.

The distinction this example surfaces: a **per-call flag** and a **constructed-operator variant** are different categorical objects. A per-call flag varies invocation-to-invocation (the outer V-cycle passes a different `initial_guess` on different calls to the *same* operator); a constructed-operator variant is fixed at setup. Hoisting the degenerate case into a per-call argument rather than a variant *avoids over-absorbing* — it keeps the [`variant-absorption`](./variant-absorption.md) discipline correct by not crystallizing a fixed-at-setup variant out of something that is genuinely a per-call input.

The unifying principle with the CG example: in both cases a quantity that *looks* like it should be carried by the heavier mechanism (a state field; a constructed-operator variant) is instead expressed as the cheaper derived/parametric form (a step-output; a per-call argument), because the heavier mechanism would force redundant structure — a maintained invariant in CG, an inflated closure lattice in Chebyshev.

## When the rotation applies

A derived view `v = f(s)` is hoistable to a step-output when:

- `f` is a pure function of the state (no operator application, no global communication beyond what's already in `f`).
- `v` is not consumed *inside* the step body (only by downstream callers / monitoring / convergence checks visible at the call site).
- `v` is a candidate for §3.8 demand-driven pruning (some consumers want it, some don't).

When `v` IS consumed inside the step body (e.g., the convergence predicate `res' < eps` in CG), it remains a local binding inside the step — neither a state field nor a step-output. The convergence Bool itself goes into the state because `iterate_while`'s predicate needs it.

## Relation to state hiding

This is one of three rotation-quality criteria from [rotation](./rotation.md): the derived-view-hoisting pattern realizes **state hiding** specifically — what's hidden is the redundant field that a naïve schema would carry. The rotation is asymmetric: it shrinks the state schema (which is the visible API surface of the iteration) without changing the algorithm's observable behavior.

## Background

This pattern is implicit in functional-iteration idioms (Haskell's `unfoldr`, Lean's `Nat.rec` over an iteration), where iteration state is a closed record and per-step outputs are a separate return channel. Imperative iteration tends to conflate the two: a `for`-loop's local variables include both "state threaded across iterations" and "derived quantities computed each iteration for logging/output". The rotation makes the distinction explicit.

See also: [tensor-field-lift](./tensor-field-lift.md) (the related L3-level rotation for per-element computations); [sequential-obstruction](./sequential-obstruction.md) (which establishes when an iteration *must* be sequential — CG's case — so the question "what belongs in the threaded state vs. the per-step output" arises in the first place).
