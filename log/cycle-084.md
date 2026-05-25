## 2026-05-25 cycle-84 — forward gmres [L2→L3] — pass

- Synthesis: GMRES L2→L3 rotation claims: field-side primitives lift cleanly (initial_residual, apply_BA, apply_correction, CGS-form orthogonalize), LS-side ls_update_column and back_solve recorded as small-dense-state sequential obstructions, MGS-form orthogonalize routed to orthog slice.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 2 lesson(s); 6 rotation_claim(s).
