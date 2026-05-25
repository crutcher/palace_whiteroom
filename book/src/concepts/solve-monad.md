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

- [slice: gmres §L4](../spec/slices/gmres.md) — restarted GMRES / FGMRES coordination over `SimState`, with `Krylov` threaded as a `let`-bound bundle inside each `restart_cycle`.

## See also

- [state-stratification](./state-stratification.md) — the three-way type split this monad acts on.
- [constructed-operators](./constructed-operators.md) — what the inner loop calls; the operator interface is variant-absorbed and lives outside the monad.
- [sequential-obstruction](./sequential-obstruction.md) — small-dense recurrences are pure inside the monad, not monadic effects.
