# Lessons

Cross-cycle observations the Critic finds worth carrying forward. Updated on disagreement *and* on validated non-obvious choices.

Format: one-line entries, dated, terse. The point is rapid scanning during planning, not narrative.

```
YYYY-MM-DD  <one-line pattern note>
```

## Entries

2026-05-24  When a slice's own 'Open questions' section contains a link that is load-bearing for the reduction chain, the L0→L1 rotation is not closed and should be split or deferred rather than asserted.
2026-05-24  When the Synthesizer emits a full slice spec with zero rotation_claim entries, treat the diff as unverifiable and require resubmission with per-assertion claims — narrative spec prose without claim/citation pairs cannot be audited.
2026-05-24  When an L1→L2 rotation maps each L1 line 1:1 to a named BLAS call with identical threaded state, it is a renaming, not a rotation; the real L2 primitive is usually one level coarser (e.g., arnoldi_step) and admits algorithmic substitution (MGS↔CGS2) that the line-by-line form cannot.
2026-05-24  When a slice supports orthogonal axes of variation (e.g., preconditioning side, orthogonalization variant, flexible vs. fixed preconditioner), the L1 procedure must specify behavior under EACH combination or explicitly scope variants out; otherwise the L1→L2 contract has hidden branches that will surface as missing_case at L2.
2026-05-24  When a slice has a 'variant' (FGMRES vs GMRES, restarted vs full, left vs right preconditioning), the L1 form should be stated parametrically so the variant is a binding rather than a bolted-on paragraph — otherwise the rotation hides less state than it appears to.
