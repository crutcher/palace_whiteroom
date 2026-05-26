## 2026-05-26 cycle-143 — refinement arnoldi_step [Ln→Ln] — pass

- Synthesis: arnoldi_step refinement (L0→L0 + L2→L2 tightenings): separate kernel-level breakdown fact from downstream surfacing in gmres; clarify that the apply→orthog→nrm2→scal chain rigidity is w-mediated only, with H[0..j] vs H[j+1,j] writes occupying disjoint index ranges. No layer advance; no new concepts; no new dep-map edges. skills_consulted: [classify-variant-axis (n/a — no new variant axes introduced; residual gs_orthog axis already classified), verify-citation-range (applied — checked that iterative.cpp:638-640 reference in the original L0 sentence is correctly a gmres-slice citation, not arnoldi_step-slice; the edit moves the cross-slice reference into a forward-reference framing rather than treating it as an L0 fact of this slice)]
- Verdict: pass.
- Friction: none.
- Structural change: applied: 2 lesson(s); 2 rotation_claim(s).
