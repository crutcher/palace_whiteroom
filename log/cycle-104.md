## 2026-05-26 cycle-104 — forward gmres [L4→L4] — revise

- Synthesis: GMRES L4→L4 v0.2 tightening: build_convergence returns ε0 to close the v0.1 derive_ir gap; classify_outcome and should_stop_inner extract the remaining max_it/max_dim reads from restart_cycle and inner_loop. Variant-absorption discipline now holds uniformly. skills_consulted: [classify-variant-axis (n/a — no new variant axis introduced, existing axes' absorption tightened), verify-citation-range (n/a — no L0 edits), skill-selection (applied)]
- Verdict: revise.
- Friction: classify_outcome packaging the (converged / max_it / restart) trichotomy is a real coarser-substitution rotation — the criterion (b) argument is sound. But the framing 'a reader can replace classify_outcome with a different outcome policy' is speculative; the realistic substitution surface is narrow (the three Outcome cases are exhaustive and load-bearing). The rotation passes structurally, but the justification overclaims substitution latitude..
- Structural change: applied: 1 dep-map edge(s), 2 lesson(s); 3 rotation_claim(s).
