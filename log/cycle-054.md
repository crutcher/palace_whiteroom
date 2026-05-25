## 2026-05-25 cycle-54 — forward cg [L2→L3] — pass

- Synthesis: Retroactive L2→L3 rotation_claim for cg slice — formalizes the negative-L3-with-positive-step-body result already on disk in `## L3` section of book/src/spec/slices/cg.md (lines describing genuine algorithmic sequentiality as the obstruction at the outer loop, plus per-step composition lifting cleanly). No new structural writes; the L3 section was emitted in a prior cycle without a corresponding rotation_claim. Quoted-prose evidence below.

retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L3
    quoted_lines: |
      CG is an inherently **sequential** algorithm at the outer-loop level: iteration `k` depends on iteration `k−1` through the residual, search direction, and scalar accumulators. There is no global-tensor-field rewrite of the entire CG iteration. **This is a negative L3 result for the outer loop**, and it is correct — the obstruction is genuine algorithmic sequentiality, not a missing transformation.
  - claim_index: 1
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L3
    quoted_lines: |
      The **per-step** body, however, *is* a composition of L3 primitives — each of `apply A`, `apply B`, `axpy`, `dot`, `axpby`, scalar arithmetic — is a whole-tensor operation with no element loop. L3 for CG is therefore:
      - **Inner step body**: positive L3 result — pure tensor-algebra composition (already given in §L2 above).
      - **Outer iteration**: negative L3 result, **obstruction = genuine algorithmic sequentiality**. The L2→L3 rotation does not apply to the loop itself; the iteration survives into L4 as `iterate_while`.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 dep-map edge(s), 1 lesson(s); 1 rotation_claim(s).
