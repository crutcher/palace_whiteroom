## 2026-05-24 cycle-8 — back gmres — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The rotation does perform genuine state-hiding (Givens sequence, s vector, Hessenberg storage, index j → hidden behind 'maintain QR factorization … incrementally') so it passes the rotation-quality check. However, L1 step 2 still mentions 'maintaining a QR factorization of \bar H_m via Givens rotations' and 'read off the last entry of the rotated right-hand side' — this is L0 machinery leaking through. A cleaner L1 would say only 'solve the least-squares problem incrementally, with the current residual norm available without forming y_m' and defer Givens to L2. As-is the rotation is correct but the L1 prose is half-rotated..
- Structural change: none.
