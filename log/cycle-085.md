## 2026-05-25 cycle-85 — forward gmres [L3→L4] — pass

- Synthesis: GMRES L3→L4 rotation_claims backfilled against the existing on-disk L4 surface (cycle 75): state stratification (SimState/OpParams/Krylov), monadic Solve coordination, constructed-operator variant absorption surface, Convergence factory, Outcome ADT for inner-loop termination, and sequential-obstruction typing of ls_update_column / back_solve.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 dep-map edge(s), 3 lesson(s); 6 rotation_claim(s).
