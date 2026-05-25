## 2026-05-24 cycle-3 — forward gmres [L1→L2] — revise

- Synthesis: 0 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L2 'Per-iteration composition' block is essentially the L1 inner loop rewritten with primitive names — the rotation L1→L2 collapses to a renaming rather than a genuine algebraic compression. Symptom: the outer composition still has to thread V, H, g, cs, sn through `arnoldi_with_givens` as an opaque bundle, and the per-iteration block exposes index arithmetic (H[0..j+1, j], V[:,0..j]) at L2..
- Structural change: none.
