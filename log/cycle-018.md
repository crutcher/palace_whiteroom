## 2026-05-24 cycle-18 — back orthog — revise

- Synthesis: L0→L1 for orthog: orthogonalize_column primitive with variant∈{MGS,CGS,CGS2} absorbed parametrically; dot_op hook absorbs inner-product weighting; MPI collective shape disclosed as residual L2 cost axis.
- Verdict: revise.
- Friction: slice_write rejected (path exists; use mode=diff): book/src/spec/slices/orthog.md; verdict auto-downgraded pass→revise: one or more writes did not land.
- Structural change: none.
