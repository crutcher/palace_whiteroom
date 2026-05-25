## 2026-05-25 cycle-53 — forward gmres [L3→L4] — pass

- Synthesis: GMRES L3→L4 rotation: the L4 section already exists on disk (see slice content); this cycle emits the rotation_claims that the prior synthesis cycle deferred. Three claims cover (1) state stratification SimState/OpParams/Krylov hiding the Krylov bundle from the externally-visible state, (2) monadic coordination via StateT SimState collapsing the L3 imperative `state.field = ...` updates to scoped do-blocks with a single Outcome ADT subsuming the L3 termination triple, and (3) convergence-criterion absorption into a Convergence value built once per restart cycle, pulling rel_tol/abs_tol/initial_res reads out of the main control flow. Sequential obstructions on small-dense state (ls_update_column, back_solve) carry through unchanged as pure functions on Krylov.

retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L4 — calculus form, §State stratification
    quoted_lines: |
      // SimState — externally-visible, persists across the Mult call.
      type SimState = { readonly x: Vec; readonly it: int; readonly converged: bool; readonly final_res: real; readonly initial_res: real; }
      // Krylov — ephemeral, reborn at each restart, discarded at return.
      // Field-side: V, Z. LS-side: H, s, cs, sn — small dense, NOT field state.
      type Krylov = { V: Vec[]; Z: Vec[] | null; H: Dense; s: DenseVec; cs: DenseVec; sn: DenseVec; j: int; beta: real; }
      The `readonly` markers on `SimState` and `OpParams` are load-bearing: the solve produces a new `SimState` value rather than mutating in place ... `Krylov` is mutable internally but does not escape the solve.
  - claim_index: 1
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L4 — calculus form, §Monadic coordination
    quoted_lines: |
      type Solve a = StateT SimState Identity a
      data Outcome = Continue | Done Bool
      gmres_solve op b x0 = execState (solve_loop op b) (SimState x0 0 False ∞ ⊥)
      solve_loop op b = do outcome <- restart_cycle op b; case outcome of { Done _ -> pure () ; Continue -> solve_loop op b }
      ... The `do`-blocks mark the points where `SimState` is read or written; everywhere else the code is pure on `OpParams` and `Krylov`. The inner loop's only `SimState` interaction is the `it`-counter increment ... The three termination paths (converged on the LS proxy, exhausted total iterations, hit per-cycle basis dimension) are resolved from `(K.beta, K.j, SimState.it)` at the outer-loop level — the inner loop returns a single `Krylov` value and the outer loop classifies. The `Outcome` type collapses the previously-articulated `StopTag` × `final_res` × `ε` decision table into one constructor.
  - claim_index: 2
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L4 — calculus form, §Convergence-criterion absorption
    quoted_lines: |
      data Convergence = Convergence { epsilon :: real, satisfied :: real -> Bool }
      build_convergence op b β prior_initial_res =
        let ε0 = if isUnset prior_initial_res then if op.initial_guess then (if op.pc_side == LEFT then nrm2 (op.M · b) else nrm2 b) else β else prior_initial_res
            ε  = max (op.rel_tol * ε0) op.abs_tol
        in Convergence { epsilon = ε, satisfied = \β' -> β' < ε }
      The inner loop and the post-correction test below take a `Convergence` value and call `.satisfied` — they do not re-derive `ε`.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 dep-map edge(s), 2 lesson(s); 3 rotation_claim(s).
