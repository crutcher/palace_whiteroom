## 2026-05-24 cycle-6 — back gmres — revise

- Synthesis: 2 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L0→L1 rotation does real work (state hiding: V, H, s/sn/cs, the enum dispatch, and the Givens accumulator are all hidden behind 'four concerns'), so it is a genuine rotation under criterion (a). However, the FGMRES paragraph is bolted onto the end of L1 rather than absorbed: the rotation 'GMRES is x_m = x_0 + V_m y_m' has to be locally patched to 'x_m = x_0 + Z_m y_m' for FGMRES, which suggests the L1 form should have been stated as 'x_m = x_0 + W_m y_m where W_m is the *update basis* (= V_m for GMRES, = Z_m for FGMRES) and A W_m = V_{m+1} H̄_m'. That unified form would make FGMRES a parameter choice rather than a variant..
- Structural change: none.
