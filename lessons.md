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
2026-05-24  Parametric variant absorption at L1 can hide a non-uniformity at L2 when one parameter value requires a post-processing step the others don't (here: right-precond fixed-M needs a terminal M.apply that left-precond and FGMRES don't); the fix is to redefine the L1 abstraction so the primitive sequence is uniform, pushing the variant into a storage/laziness choice rather than a branch in the primitive chain.
2026-05-24  When a slice's L1 parameter space collapses multiple orthogonal axes into one because the codebase only instantiates a diagonal of the product, say so explicitly — otherwise L1 overclaims generality and downstream L2 unfolds will struggle to recover the hidden axes.
2026-05-24  When source is not pre-fetched, the Critic cannot discharge citation_does_not_support / mutation_pattern_mismatch checks and must mark them `unclear` rather than passing; consider making source pre-fetch mandatory for L0→L1 rotations.
2026-05-24  When a slice cites both a single-element and a block/batched variant of the same operation, the L1 form should explicitly state whether the block form is a trivial lift or a distinct primitive — silent omission leaves an unhandled case.
