## 2026-05-25 cycle-25 — sideways gmres,orthog — revise

- Synthesis: Established gmres and orthog slices at L1 with concept entries; the parent gmres slice scopes orthogonalization-variant axes to the orthog slice via forward reference, achieving variant absorption (a/b/c) on the GMRES axes (preconditioner side, restart, flexibility) and explicitly deferring the orthogonalization axes to the kernel slice.
- Verdict: revise.
- Friction: slice_write rejected (path exists; use mode=diff): book/src/spec/slices/gmres.md; slice_write rejected (path exists; use mode=diff): book/src/spec/slices/orthog.md; concept_write create skipped (already exists; use append-section): orthogonalization; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
