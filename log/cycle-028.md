## 2026-05-25 cycle-28 — forward chebyshev [L1→L2] — revise

- Synthesis: chebyshev L1→L2 unfold: Richardson-like sweep expressed as copy/zero/elementwise_product/scal/axpy/apply_linop composition; variant absorption preserved at primitive-sequence level (only the scalar generator branches on variant); fused-kernel realization treated as transparent optimization; non-associative reduction order preserved.
- Verdict: revise.
- Friction: file_edit rejected (old_string not found in book/src/spec/index.md): '| `chebyshev` | L1 | 2026-11-19 | 4th-kind & 1st-kind polynomial smoothers absor'; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
