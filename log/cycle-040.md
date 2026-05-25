## 2026-05-25 cycle-40 — sideways orthog,chebyshev — revise

- Synthesis: Initial L1 push on the orthogonalization slice — invariant, variant-parametric procedure absorbing CGS/MGS/CGS2/Householder, consumer interface. Extracted two concept entries: orthogonalization (the kernel family) and chebyshev-iteration (companion concept opened for a future slice; flagged as inner-product-free CG counterpart).
- Verdict: revise.
- Friction: slice_write rejected (path exists; use mode=diff): book/src/spec/slices/orthog.md; concept_write create skipped (already exists; use append-section): orthogonalization; Related to the above: variant-absorption check (#9) fails at level (c) for Householder. The slice claims all three levels of absorption but the primitive-sequence level only holds for the three Gram-Schmidt variants. This is silent partial absorption — the residual axis (Householder's reflector-accumulation state) is not declared in L1 as a variant-conditional state field, nor is the divergence in primitive sequence acknowledged at L1..
- Structural change: none.
