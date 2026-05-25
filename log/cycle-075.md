## 2026-05-25 cycle-75 — forward gmres [L3→L4] — pass

- Synthesis: GMRES L3→L4 rotation claims (4): state stratification (SimState/OpParams/Krylov typing with readonly markers), monadic coordination (Solve = StateT SimState; Outcome = Continue|Done Bool; inner_loop pure on Krylov), Convergence absorption (rel_tol/abs_tol/initial_res policy → single .satisfied predicate built once per cycle), and sequential-obstruction carry-through (ls_update_column/back_solve typed as pure Krylov-to-Krylov). All claims are retroactive against on-disk L4 prose landed in cycle 74; no new slice or layer-section content in this plan.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 3 lesson(s); 4 rotation_claim(s).
