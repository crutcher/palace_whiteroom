## 2026-05-25 cycle-69 — forward gmres [L0→L1] — revise

- Synthesis: gmres slice L0 citation-tightening + L1 fidelity pass: corrected ±2-line drift on L0.5/5a/6/7/10–12, added L0.11a drift-warning hook (iterative.cpp:595–605), disclosed L0 storage reuse vs. L1 fresh_krylov fiction, noted RIGHT-branch r/V[0] scratch reuse in apply_correction. No layer advancement; structural form unchanged.
- Verdict: revise.
- Friction: file_edit rejected (old_string not found in book/src/spec/slices/gmres.md): '- L0.7 `OrthogonalizeIteration(gs_orthog, V, w, Hj, j)`. `palace/linalg/iterativ'.
- Structural change: none.
