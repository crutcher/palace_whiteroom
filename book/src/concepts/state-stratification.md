---
edges:
  reference:
    - concepts/solve-monad
    - concepts/constructed-operators
    - concepts/sequential-obstruction
    - L2/krylov-step
---
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

- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — `SimState` / `OpParams` / `Krylov` for restarted GMRES and FGMRES.
- (Pending) other Krylov slices (CG, BiCGStab) will share this template.

## See also

- [solve-monad](./solve-monad.md) — the monadic coordination that consumes a state-stratified type signature.
- [constructed-operators](./constructed-operators.md) — where the variant selectors live and get absorbed.
- [sequential-obstruction](./sequential-obstruction.md) — small-dense ephemeral state often hosts sequential obstructions (Givens-replay, back-solve) that do not lift to a global form.

## Worked example — GMRES (slice: gmres, L4)

The GMRES slice's L4 form is a worked example of the three-bundle split:

- **SimState** (externally-visible, persists across the `Mult` call): `x`, `it`, `converged`, `final_res`, `initial_res`. These are the quantities a caller observes after the solve returns.
- **OpParams** (operator-internal, captured at construction, fixed across a `Mult` call): `A`, `M`, `Mk`, `pc_side`, `gs_orthog`, `max_dim`, `max_it`, `rel_tol`, `abs_tol`, `initial_guess`, `flexible`. The `readonly` marker is load-bearing: variant-axis fields are read ONLY by the constructed-operator helpers (`initial_residual`, `apply_BA`, `apply_correction`, `build_convergence`), never by the main control flow.
- **Krylov** (ephemeral, solve-local, born at restart and discarded at restart-or-return): `V`, `Z`, `H`, `s`, `cs`, `sn`, `j`, `beta`. Mixes field-side state (`V`, `Z`) and small-dense LS-side state (`H`, `s`, `cs`, `sn`). The bundle is threaded through `inner_loop` as a plain value; it does NOT appear in SimState because it is reborn at each restart and discarded at return.

The split mirrors Palace's L0 class layout: instance fields (configuration, persistent state) ↔ OpParams; lazy `Initialize`/`Update` workspace ↔ Krylov; the externally-observable `final_res` / `converged` flags ↔ SimState. Variant absorption is preserved at L4 because the bundles type the contract: `OpParams.flexible` determines whether `Krylov.Z` is present, but the main control flow does not branch on this — `apply_correction` closes over the right basis (V or Z) based on the captured OpParams.

## Worked example — Chebyshev smoother (slice: chebyshev, L4): a fourth stratum

The three strata above are the common case. Some operators have a **fourth** stratum: per-call ephemeral state that is *threaded across an inner loop within a single call* but does not survive the call. The Chebyshev smoother's L4 form (slice: chebyshev §L4) is the canonical example — it adds a **scalar-recurrence stratum** distinct from the other three:

1. **Sim state** (caller-owned, threaded by the outer solve monad): `x` (rhs, read-only), `y` (accumulator/iterate, read-write). The capability split `{ x: Read<Field>; y: ReadWrite<Field> }` records the mutation discipline at the type surface.
2. **Operator internal params** (captured at `setup`, immutable across `apply` calls): `A`, `dinv`, `order`, `pc_it`, and the variant-specific persisted scalars (`lambda_max` for 4th-kind; `theta`/`delta` for 1st-kind). Live inside the constructed-operator closure.
3. **Ephemeral intermediates** (allocated per `apply_linop` call, discarded on return, *not* threaded): `r`, `d`, `t`, `Ay`, `Ad` — transient field-algebra values.
4. **Scalar-recurrence state** (per-call ephemeral, but threaded across the inner `k`-iterations within a single `apply` call): `rho_prev` for the 1st-kind variant, carried by the inner `foldM`'s `ScalarState`. For 4th-kind, `ScalarState = ()`.

The fourth stratum is its own category — it is neither (2) nor (3):

- **Distinct from operator-internal params (2)**: the closure does *not* retain `rho_prev` across `apply` calls. Each call restarts the recurrence from `rho_0`. If it were in stratum (2), it would persist between calls and corrupt the next solve.
- **Distinct from ordinary ephemerals (3)**: `rho_prev` is *genuinely threaded* across the `k`-loop (each step reads the previous step's value via `rho_k = 1/(2θ/δ - rho_{k-1})`), whereas `r`, `d`, `t` are transient temporaries recomputed each step. An ordinary ephemeral has no cross-iteration data dependence; the scalar-recurrence state does.

At L4 the fourth stratum is made visible at the *type* level via a stratum-specific type parameter: `ChebOp<E, S>` where `S` is the scalar-state type, statically determined by variant (`Unit` for 4th-kind, `{ rho_prev: E }` for 1st-kind). The two variants are **distinct closure types**, not a runtime-tagged union — there is no apply-time variant discriminator. The scalar-recurrence state rides inside the inner `foldM` accumulator alongside the ephemeral field tuple `(r, d, st)`, and is `O(1)` work and memory per step.

Stratum-placement check for the fourth stratum: a piece of state belongs here (not in (2) or (3)) when it is **threaded across an inner loop but reborn at each top-level call**. The lifetime is "one `apply` call, all `k`-iterations" — narrower than operator-internal (which is "all calls") and wider than an ordinary ephemeral (which is "one `k`-iteration"). When an operator has no inner-loop-threaded scalar (e.g. the GMRES example above, where the Givens registers `cs`/`sn` live in the `Krylov` ephemeral bundle and are not a separately-typed recurrence carrier), the fourth stratum is absent and the three-way split suffices.
