## 2026-05-25 cycle-99 — forward arnoldi_step [L1→L2] — revise

- Synthesis: arnoldi_step L1→L2: four-primitive composition (apply_BA → orthogonalize → subdiag_norm → normalize) over apply_linop/dot/axpy/nrm2/scal; orthog and incremental-least-squares scoped out as separate slices.
- Verdict: revise.
- Friction: slice_index_update: slice_index_update: no row found for slice 'arnoldi_step' (looked for anchors ['./slices/arnoldi_step.md', './slices/arnoldi_step/index.md']). Add a row via file_edits/section_appends first, or the integrator can be extended with an append-by-slug fallback..
- Structural change: none.
