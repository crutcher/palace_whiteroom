# convergence-test

A *convergence test* in an iterative solver is the predicate that decides, at each step, whether the iterate is good enough to stop. The naive realisation interleaves the predicate's parameters (relative tolerance, absolute tolerance, initial-residual scaling, side-specific rescaling) into the inner loop's control flow — every iteration re-derives `ε` from `op.rel_tol`, `op.abs_tol`, `state.initial_res` and reads `pc_side` to choose what `initial_res` was computed from.

This is variant absorption in the small. Per [concept: variant-absorption](variant-absorption.md), the inner loop should mention the convergence policy at most once. Per [concept: constructed-operators](constructed-operators.md), the route is to construct a small object — a `Convergence` value — once per restart cycle that internalises the policy, and pass it through the inner loop as a single predicate.

## Shape

```
Convergence = { epsilon: real, satisfied: real -> bool }

build_convergence(op, b, β, prior_initial_res) -> Convergence:
  ε0 = (prior_initial_res unset)
         ? (op.initial_guess ? scale_initial(op, b) : β)
         : prior_initial_res
  ε  = max(op.rel_tol * ε0, op.abs_tol)
  return Convergence { epsilon = ε, satisfied = λ β' . β' < ε }
```

`scale_initial` is the side-specific rescaling (e.g., GMRES with `pc_side = LEFT` uses `‖M·b‖₂`, all other sides use `‖b‖₂`). It is itself a constructed-operator surface — pulled out of the main loop into one named site.

## Why it belongs at L4

The convergence test is the third surface (alongside `apply_BA` and `apply_correction`) through which a Krylov solver's variant axes leak into the main loop if not absorbed. At L1 / L2 / L3 the test reads as `if K.beta < ε: break` with `ε` computed once before the loop, which is already absorbed locally. At L4 the typing makes the absorption structural: the inner loop function takes a `Convergence` argument and *cannot* re-derive `ε` from `OpParams` because the policy fields are not in its closure.

This is a methodology pattern: any iterative loop whose stopping criterion has more than one input parameter is a candidate for `Convergence`-style absorption. The pattern shows up in eigensolvers (the residual on the eigenpair plus the eigenvalue gap), in nonlinear solvers (the Newton residual plus the step size), and in time-steppers (the local truncation error plus the absolute floor).

## Relation to other concepts

- [concept: constructed-operators](constructed-operators.md) — `build_convergence` is the canonical example of constructing a small operator that absorbs configuration. The output is a single closure (`satisfied`) plus the threshold it captures.
- [concept: variant-absorption](variant-absorption.md) — the policy parameters (`rel_tol`, `abs_tol`, `initial_guess`, side-specific `scale_initial`) are absorbed at all three levels: the invariant statement ("stop when β < ε") is unified; the procedure mentions the policy once (at `build_convergence`); the primitive sequence is unchanged across policy choices.
- [concept: solve-monad](solve-monad.md) — `Convergence` is *not* part of the monad state. It lives within a single restart cycle as a plain value, like `Krylov`.
