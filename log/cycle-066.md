## 2026-05-25 cycle-66 — forward cg [L4→L4] — revise

- Synthesis: CG L4 v0.4 self-rotation: hoisted `res` from hypothetical state-field to step-output, made the state-hiding rotation explicit. v0.3→v0.4 is observationally no-op on the schema but names the rotation per concepts/rotation.md; adds a worked example for the GMRES slice's coming residual-tracking decision. The rotation_claim is an L4→L4 state-hiding self-rotation, not a layer advance.
- Verdict: revise.
- Friction: concept_write create skipped (already exists; use append-section): derived-view-hoisting.
- Structural change: applied: 1 concept_write(s), 1 dep-map edge(s), 2 lesson(s); 1 rotation_claim(s).
