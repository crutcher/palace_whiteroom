## 2026-05-24 cycle-9 — back gmres — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The variant absorption is mostly clean, but the update-basis selector `W ∈ {V, Z}` driven by `side` is a conditional smuggled into the invariant and the solution-update step. It surfaces as two places in L1 where `side` is re-inspected (Arnoldi step 1 AND solution update step 3), which is a hint that the Z/V distinction is not fully absorbed. Also, the `M : j → LinearOperator` unification of GMRES/FGMRES is asserted but the spec then says `Z[j] = M_j^{-1} V[j]` only for 'right/flexible' — there is no separate FGMRES parameter, but the spec still distinguishes flexible behavior textually..
- Structural change: none.
