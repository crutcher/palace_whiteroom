## 2026-05-25 cycle-41 — back orthog — revise

- Synthesis: orthog L0→L1 retroactive rotation claims: variant-parametric primitive with local-dot + routine-owns-reduction contract; three claims covering state-hiding (per-variant kernel sequencing), variant absorption (algorithm tag absorbed at one dispatch site), and inner-product abstraction (dot_op hook); confirmed against test-orthog substitutability tests.
- Verdict: revise.
- Friction: Claim 1 explicitly discloses that variant-absorption level (c) (primitive-sequence) is NOT achieved — the L2 chains for MGS / CGS / CGS2 differ in shape and in number/size of collectives. The disclosure is per the variant-absorption discipline and is acceptable in principle, BUT the spec surface that would carry this disclosure is not in the diff. Without the L1/L2 text on disk, the partial absorption is silent rather than declared. Re-emit with the disclosure visible in the spec text (a 'Residual axes' or 'Primitive-sequence divergence' subsection at L2 listing the three concrete chains)..
- Structural change: none.
