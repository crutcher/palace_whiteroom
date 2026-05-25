## 2026-05-24 cycle-20 — forward gmres [L0→L1] — pass

- Synthesis: gmres L0→L1 — cited 16 regions; L1 schema separates SimState / OpParams / Krylov (per-cycle ephemeral); six L1 building blocks (initial_residual, apply_BA, orthogonalize, ls_update_column, back_solve, apply_correction) absorb all four variant axes at single dispatch sites; extracted concept incremental-least-squares; extended constructed-operators with GMRES usage section.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 slice_write(s), 2 concept_write(s), 2 dep-map edge(s), 2 lesson(s); 5 rotation_claim(s).
