## 2026-05-24 cycle-5 — back gmres — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L1 description threads V, H, g, cs, sn, x, j all together through a single monolithic step 2 loop. This is fine for L1 (rotation criterion (a) state-hiding will happen at L1→L2 by introducing an arnoldi_step primitive that hides H/cs/sn/g update), but the current Procedure is written in a way that fuses (i) Arnoldi orthogonalization, (ii) Givens update, (iii) residual monitor into one numbered list. Consider whether step 2.5 and 2.6 should be presented as a separable 'projected-problem update' sub-procedure even at L1 — this would make the L1→L2 boundary cleaner. Not blocking, but worth flagging..
- Structural change: none.
