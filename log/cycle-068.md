## 2026-05-25 cycle-68 — forward orthog [L1→L2] — pass

- Synthesis: Emit retroactive L1→L2 rotation_claims for the orthog slice, whose L2 section already exists on disk (landed in a prior cycle alongside L3/L4). Three per-variant claims (MGS, CGS, CGS2) plus one structural claim for the allreduce_sum promotion. retroactive_claim_evidence quoted below.

retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/orthog.md
    section: ## L2 — primitive composition (MGS pass)
    quoted_lines: |
      mgs_pass(V[0..m-1], w, dot_op):
          H : array of m scalars
          for j in 0..m-1:
              h_local := dot_op(V[j], w)               # local dot
              H[j]    := allreduce_sum(h_local, 1)     # global reduction, size 1
              w       := axpy(w, -H[j], V[j])          # w ← w − H[j] V[j]
          return (H, w)
      The j-th `axpy` *must* complete before the (j+1)-th `dot_op` (else the algorithm is no longer MGS).
  - claim_index: 1
    on_disk_path: book/src/spec/slices/orthog.md
    section: ## L2 — primitive composition (CGS pass)
    quoted_lines: |
      cgs_pass(V[0..m-1], w, dot_op):
          h_local[0..m-1] := [ dot_op(V[j], w) for j in 0..m-1 ]   # m local dots, no comm
          H[0..m-1]       := allreduce_sum(h_local, m)             # one reduction, size m
          w               := gemv_basis(w, -1.0, V, H)             # w ← w − V H, batched
          return (H, w)
      The local dots over j are independent (no inter-j ordering); the reduction is hoisted out of the loop and batched; the rank-1 updates fuse into one `gemv_basis`.
  - claim_index: 2
    on_disk_path: book/src/spec/slices/orthog.md
    section: ## L2 — primitive composition (CGS2)
    quoted_lines: |
      cgs2(V[0..m-1], w, dot_op):
          (H,  w) := cgs_pass(V, w, dot_op)
          (dH, w) := cgs_pass(V, w, dot_op)
          H := axpy_scalar(H, 1.0, dH)                 # H ← H + dH (length-m vector add)
          return (H, w)
      The second pass operates on the once-orthogonalized `w` and accumulates the correction `dH`.
  - claim_index: 3
    on_disk_path: book/src/spec/slices/orthog.md
    section: ## L2 — primitive composition (allreduce_sum promotion + variant absorption at L2)
    quoted_lines: |
      `allreduce_sum` (the explicit global reduction; promoted from being implicit inside `dot` to a primitive in its own right because each variant fires it a different number of times and with a different message size, which is the dominant cost structure at L2).
      ...
      The L1 procedure inspected `variant` exactly once (dispatch). The L2 primitive-sequence does **not** unify across variants: MGS's chain is `[dot, allreduce_sum, axpy] × m`, CGS's is `[dot × m, allreduce_sum, gemv_basis]`, CGS2's is `[CGS chain] × 2 + [axpy_scalar]`.
- Verdict: pass.
- Friction: none.
- Structural change: none.
