## 2026-05-26 cycle-166 — refinement cg_preconditioning_framework [Ln→Ln] — revise

- Synthesis: cg_preconditioning_framework L4→L4 v0.3: derived-view hoisting of `finestLevelUnwrap` out of `setOperators`'s body into a `pcBoundOp(binding, pc)` derived view; `OpBinding<E>` schema now stores only primitive operator inputs, removing the v0.2 stored-vs-bound divergence hazard. skills_consulted: [classify-variant-axis (n/a — no new variant axis introduced), verify-citation-range (applied — confirmed palace/linalg/ksp.cpp:274-296 still names SetOperators body containing the unwrap branch, citation unchanged from v0.2), skill-selection (applied — selection identified within-L4 self-rotation triggers per-building-block claim discipline and surface-or-evidence rule)].
- Verdict: revise.
- Friction: file_edit rejected (old_string not found in book/src/spec/slices/cg_preconditioning_framework.md): '- **Build-time vs. run-time as a methodology concept.** The stratification obser'.
- Structural change: none.
