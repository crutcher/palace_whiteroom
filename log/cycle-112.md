## 2026-05-26 cycle-112 — forward sparse_triangular_solve [L0→L1] — pass

- Synthesis: sparse_triangular_solve L0→L1: obstructed (out-of-scope). Negative-result slice records the Palace/MFEM boundary; L0 lists the four wrapper facts (SuperLU/STRUMPACK/MUMPS forward as opaque ksp_solve, no Allgatherv-on-factor, no residual check, no Palace-owned L/U). L0→L1 emits an obstruction rotation_claim. Extends sequential-obstruction concept with an out-of-scope-obstruction sub-kind; proposes a follow-up sparse_direct_solver_wrapper slice.
- Verdict: pass.
- Friction: slice_index_update: appended new row for slice 'sparse_triangular_solve' (first touch).
- Structural change: applied: 1 slice_write(s), 1 concept_write(s), 1 dep-map edge(s), 2 lesson(s); 1 rotation_claim(s).
