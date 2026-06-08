## 2026-05-26 cycle-142 — refinement cg [Ln→Ln] — pass

- Synthesis: cg L4→L4 self-rotation: v0.5 first-iteration unrolling. Hoists the it==0 branch out of cg_step/pcg_step by splitting into cg_first_step (straight-line) + cg_steady_step (branch-free, beta_prev as closure parameter not state field). Steady-state schema loses beta_prev; equivalence to v0.4 by forget_beta_prev projection. New layer-pattern concept first-iteration-unrolling extracted with forward markers for GMRES/LOBPCG/Chebyshev/etc. Resolves the open Working Notes push-back from cycle 1. skills_consulted: [classify-variant-axis (not_applicable — no variant axis introduced), verify-citation-range (not_applicable — no new L0 citations), skill-selection (applied — surveyed skills/, no others trigger), propose-rotation (applied — self-rotation under rotation.md criterion (a) state hiding of beta_prev field and it==0 branch)]
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 concept_write(s), 2 dep-map edge(s), 2 lesson(s); 3 rotation_claim(s).
