## 2026-05-25 cycle-57 — forward cg [L4→L4] — pass

- Synthesis: CG L4→L4 self-rotation: extract residual_norm from PCgState by promoting it to a step-output field, mirroring the cg_step shape. Eliminates a redundant state field (res is a derived view of beta); state schema shrinks by one scalar; observably equal to the prior form.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 concept_write(s), 1 dep-map edge(s), 2 lesson(s); 2 rotation_claim(s).
