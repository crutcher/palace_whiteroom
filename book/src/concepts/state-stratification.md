# state-stratification

At L4, the calculus distinguishes three kinds of state in an iterative solve and types them separately. This stratification is what lets a slice's L4 form be code-like-but-not-runnable while remaining unambiguous about lifetimes, mutability, and dispatch sites.

The three kinds:

1. **Sim state** — externally-visible quantities the solve evolves and reports. For Krylov solvers: the current iterate `x`, the iteration count `it`, the convergence flag, the residual proxies (`final_res`, `initial_res`). Sim state persists across the entire `Mult` call and is the return value. At L4, sim state is `readonly` from the caller's perspective; the solve produces a new `SimState` value rather than mutating in place. This is what makes the monadic coordination tractable — the solve's effect on the world is exactly the `SimState` transition.

2. **Operator internal params** — fixed across a single solve call. The configuration record: operators (`A`, `M`, per-step `Mk`), variant selectors (`pc_side`, `gs_orthog`, `flexible`), termination knobs (`max_dim`, `max_it`, `rel_tol`, `abs_tol`). Captured once at the entry to the solve. By construction these are the parameters the constructed-operator helpers close over (see [constructed-operators](./constructed-operators.md)); the main procedure body does not re-inspect them.

3. **Ephemeral intermediates** — workspace whose lifetime is strictly within the solve and which is discarded on return. For GMRES this is the `Krylov` bundle: the basis `V` (and `Z` for FGMRES), the Hessenberg matrix `H`, the LS RHS `s`, the rotation registers `cs` / `sn`. For restarted solvers, ephemeral state is *reborn* at each restart and is not threaded across restart boundaries — it does not belong in `SimState`. Mutability is internal; the bundle never escapes the solve.

## Why the three-way split is load-bearing

The split makes two things structural that are merely conventional at L1–L3:

- **Lifetimes are visible.** A reader can see at a glance which state survives the call, which survives a restart cycle, which dies at the inner loop. The L0 code mixes all three in instance fields (`V`, `H`, `s` on the solver class); the L4 form un-mixes them.
- **Variant absorption is mechanically checkable.** If `OpParams` is `readonly` and only the constructed-operator helpers close over the variant selectors, then the main procedure provably cannot re-inspect them. The variant-absorption invariant is a typing invariant, not a discipline.

## Common stratification mistakes

- Putting ephemeral workspace in `SimState` because L0 stored it as an instance field. The L0 field layout is a memory-reuse optimisation; the L4 type signature should reflect mathematical lifetime, not allocation strategy.
- Putting variant selectors in `SimState` because they are read by the procedure. They are read only by the constructed-operator helpers; the main procedure reads `OpParams` once at entry. Misplacing them defeats variant absorption.
- Forgetting that ephemeral state on a restarted solver is reborn at each restart. The `Krylov` bundle at restart `r+1` is a fresh bundle, not the bundle from restart `r` with `j` reset. If your L4 form reads from `Krylov` fields after the restart boundary, the form is broken.

## Used by

- [slice: gmres §L4](../spec/slices/gmres.md) — `SimState` / `OpParams` / `Krylov` for restarted GMRES and FGMRES.
- (Pending) other Krylov slices (CG, BiCGStab) will share this template.

## See also

- [solve-monad](./solve-monad.md) — the monadic coordination that consumes a state-stratified type signature.
- [constructed-operators](./constructed-operators.md) — where the variant selectors live and get absorbed.
- [sequential-obstruction](./sequential-obstruction.md) — small-dense ephemeral state often hosts sequential obstructions (Givens-replay, back-solve) that do not lift to a global form.
