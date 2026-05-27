## 2026-05-24 cycle-7 — forward gmres [L1→L2] — revise

- Synthesis: 3 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L1→L2 rotation for iterate update treats the right-precond unwrap as a special-case extra M.apply tacked onto the gemv, while FGMRES is the 'clean' path with no extra apply. This is a parametric variant the slice claims is absorbed (W_m = V_m vs W_m = Z_m), but the unwrap step breaks the unification: for GMRES-right you do gemv then M.apply; for FGMRES you do gemv only; for GMRES-left you do gemv only but the iterate is in preconditioned coordinates. The 'one canonical primitive sequence per parameter value' framing the synthesizer claims is therefore three sequences, not two, and the side=right-fixed-M case is the labored one..
- Structural change: none.
