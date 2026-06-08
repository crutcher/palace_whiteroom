---
edges:
  reference:
    - concepts/state-stratification
    - concepts/constructed-operators
    - concepts/sequential-obstruction
    - L2/krylov_step
---
# solve-monad

At L4, iterative-solve coordination is expressed as a state monad over the [state-stratified](./state-stratification.md) tuple. The monad threads `SimState` through outer / inner loops; ephemeral state (Krylov bundles, preconditioner workspaces) lives *within* a single restart cycle and is passed as plain function arguments / return values inside the monadic action.

## Shape

```haskell
type Solve a = StateT SimState Identity a

solve :: OpParams -> Inputs -> SimState
solve op inp = execState (solve_loop op inp) initial_state

solve_loop :: OpParams -> Inputs -> Solve ()
solve_loop op inp = do
  done <- restart_cycle op inp   -- or: one_cycle op inp, for non-restarted solvers
  unless done $ solve_loop op inp
```

The monadic effect is the `SimState` transition. Everything else (operator applications, dense kernels, Krylov-bundle updates) is pure on `OpParams` + ephemeral state.

## Why a monad and not just a fold

A pure fold would work for a non-restarted solver with a fixed iteration count. The monad earns its keep when:

- **Termination is interior.** Convergence is detected mid-step on a quantity (residual proxy) that depends on the inner state; the loop must short-circuit. Monadic `do`-with-`unless` makes the exit visible at the coordination layer.
- **Inner / outer structure.** Restarted Krylov methods have an outer cycle whose body is itself an inner loop; the inner loop reads `SimState.it` (to honour `max_it`) and writes back on each step. The monad makes the two-level read/write traffic explicit.
- **Side data threading.** The iterate `x` lives in `SimState`; the Krylov basis lives in the ephemeral bundle; the correction step `x += V·y` reads both. The monad makes the moment of `SimState` mutation a single named point (`modify $ \s -> s{ x = ... }`).

## What stays out of the monad

- Operator applications (`apply_linop`, `apply_BA`) — pure on inputs.
- Dense recurrences on small ephemeral state (Givens replay, back-solve) — pure on the bundle. See [sequential-obstruction](./sequential-obstruction.md): the calculus surfaces the recurrence *as* a plain function, not as a monadic effect.
- Variant dispatch — absorbed in [constructed-operators](./constructed-operators.md); the monad does not branch on `pc_side` etc.

The rule of thumb: if the action reads or writes `SimState`, it's in the monad; otherwise it's a pure function call inside a `let` or `pure` block.

## Used by

- [`krylov_step` (GMRES instance)](../L2/krylov_step.md) — restarted GMRES / FGMRES coordination over `SimState`, with `Krylov` threaded as a `let`-bound bundle inside each `restart_cycle`.

## See also

- [state-stratification](./state-stratification.md) — the three-way type split this monad acts on.
- [constructed-operators](./constructed-operators.md) — what the inner loop calls; the operator interface is variant-absorbed and lives outside the monad.
- [sequential-obstruction](./sequential-obstruction.md) — small-dense recurrences are pure inside the monad, not monadic effects.

## Worked example — GMRES

The GMRES L4 form coordinates the solve via `Solve a = StateT SimState Identity a` over the SimState bundle:

- `gmres_solve op b x0 = execState (solve_loop op b) (SimState x0 0 False ∞ ⊥)` — entry point.
- `solve_loop` recurses on `restart_cycle` until an `Outcome = Continue | Done Bool` value tells it to stop.
- `restart_cycle` builds a fresh Krylov (`fresh_krylov`), runs `inner_loop`, folds the correction into `SimState.x` via `modify` exactly once.
- `inner_loop` is pure on Krylov except for `modify (\s -> s{ it = s.it + 1 })` — the iteration counter is the sole SimState touch inside the inner loop. The iterate `x` is updated exactly once per restart cycle, after `back_solve`.

The Krylov bundle is threaded as a plain value through `inner_loop`, not as a monadic effect, because it is reborn at each restart and discarded at return — encoding it monadically would mis-represent its lifecycle. Only SimState (which persists across the call) lives in the monad.

### Termination as a sum type

The three termination paths (converged on LS proxy, exhausted total iterations, hit per-cycle basis dimension) collapse into a single `Outcome = Continue | Done Bool` value:

- `Done True` — converged on `K.beta < ε`.
- `Done False` — exhausted `op.max_it`.
- `Continue` — hit `op.max_dim`, another restart cycle warranted.

`solve_loop` pattern-matches on Outcome; `restart_cycle` classifies the returned Krylov against `(K.beta, K.j, SimState.it, ε)` once at the boundary. This replaces the L3 form's scattered termination tests (multiple inner-loop break conditions, post-correction `K.beta < ε` re-test) with a single decision site. The Bool inside Done carries `converged`, so the outer loop's fold into SimState is uniform: `Done True ⇒ converged = True`; `Done False ⇒ converged = False`.

This is the canonical pattern when an algorithm has multiple termination reasons that share a common return path: name the reasons in a sum type, classify once, fold uniformly.
