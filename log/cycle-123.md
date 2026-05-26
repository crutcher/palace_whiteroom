## 2026-05-26 cycle-123 — forward cg_preconditioning_framework [L0→L1] — pass

- Synthesis: cg_preconditioning_framework L0→L1: established Palace's KSP composition surface — solver_as_operator, two_operator_split, complex_from_real_lift — as the abstraction layer above the per-method (cg/gmres/fgmres) slices. Four variant axes absorbed by constructed-operator factories.
- Verdict: pass.
- Friction: slice_index_update: appended new row for slice 'cg_preconditioning_framework' (first touch).
- Structural change: applied: 1 slice_write(s), 3 concept_write(s), 4 dep-map edge(s), 2 lesson(s); 8 rotation_claim(s).
