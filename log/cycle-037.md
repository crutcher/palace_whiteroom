## 2026-05-25 cycle-37 — forward gmres [L4→L4] — pass

- Synthesis: GMRES L4→L4 tightening: extracted the convergence test into a `Convergence` constructed-operator surface (third absorption surface alongside `apply_BA` / `apply_correction`); new concept `convergence-test`; inner loop now closes over `Convergence` rather than re-reading `op.rel_tol`/`op.abs_tol`/`s.initial_res`.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 concept_write(s), 2 dep-map edge(s), 1 lesson(s); 2 rotation_claim(s).
