## 2026-05-25 cycle-71 — forward gmres [L1→L2] — pass

- Synthesis: Retroactive L1→L2 rotation_claims for the gmres slice. The L2 section was section-appended in cycle 21; this cycle backfills six rotation_claims (one per L1 building block: initial_residual, apply_BA, orthogonalize, ls_update_column, back_solve, apply_correction) per the meta-12 same-cycle emission discipline applied retroactively. The load-bearing claim is ls_update_column (state-hiding rotation exposing givens_generate / givens_apply); the others are carry-through unfoldings into the support-operator vocabulary. retroactive_claim_evidence quotes the on-disk L2 sub-sections.

retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L2 — primitive composition / **`initial_residual(op, b, x)`.**
    quoted_lines: |
      **`initial_residual(op, b, x)`.** Unfolds into one `apply_linop` (and one conditional `apply_linop` for `M`):
      ```
      if not op.initial_guess: x ← 0; r ← b
      else: apply_linop(op.A, x, Ax); r ← b; axpy(-1, Ax, r)        // r = b − A·x
      if op.pc_side == LEFT: apply_linop(op.M, r, Mr); r ← Mr        // r = M·(b − A·x)
      return (r, x)
      ```
      The `pc_side == RIGHT` branch leaves `r` as the true residual.
  - claim_index: 1
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L2 — primitive composition / **`apply_BA(op, v)`.**
    quoted_lines: |
      **`apply_BA(op, v)`.** Unfolds into one or two `apply_linop` calls:
      ```
      if op.pc_side == RIGHT:                    // FGMRES always lands here
        apply_linop(op.M, v, z); apply_linop(op.A, z, w)             // z = M·v; w = A·z
      elif op.pc_side == LEFT:
        apply_linop(op.A, v, Av); apply_linop(op.M, Av, w); z = ⊥    // w = M·A·v
      else: apply_linop(op.A, v, w); z = ⊥                           // w = A·v
      return (w, z)
      ```
  - claim_index: 2
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L2 — primitive composition / **`orthogonalize(gs_orthog, V[0..j], w)`.**
    quoted_lines: |
      **`orthogonalize(gs_orthog, V[0..j], w)`.** Unfolds into a `dot`/`axpy` sequence whose shape is fixed by `gs_orthog` but whose primitives are uniform — `dot` to project, `axpy` to subtract. ...
      ```
      for k in 0..=j:
        h[k] = dot(V[k], w)                       // (CGS / MGS / CGS2 differ in batching & repeats)
        axpy(-h[k], V[k], w)
      h[j+1] = nrm2(w); scal(1/h[j+1], w)
      return (w, h)
      ```
      MGS performs `dot`+`axpy` in sequence per `k`; CGS batches all `dot`s then all `axpy`s; CGS2 repeats once. The L2 primitive set is the same; the L3 form (orthog slice) will pin the batching.
  - claim_index: 3
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L2 — primitive composition / **`ls_update_column(K, j, h_new)`.**
    quoted_lines: |
      **`ls_update_column(K, j, h_new)`.** This is the load-bearing L1→L2 unfolding — the incremental-LS role is realised by stored Givens rotations plus one new rotation:
      ```
      // (1) Replay stored rotations on the new column h_new[0..j+1].
      for k in 0..j:
        (h_new[k], h_new[k+1]) = givens_apply((K.cs[k], K.sn[k]), (h_new[k], h_new[k+1]))
      // (2) Generate a new rotation to zero h_new[j+1] against h_new[j].
      (K.cs[j], K.sn[j]) = givens_generate(h_new[j], h_new[j+1])
      // (3) Apply the new rotation to the column tail and to the RHS s.
      (h_new[j], h_new[j+1]) = givens_apply((K.cs[j], K.sn[j]), (h_new[j], h_new[j+1]))   // h_new[j+1] = 0
      (K.s[j], K.s[j+1])     = givens_apply((K.cs[j], K.sn[j]), (K.s[j], 0))              // s[j+1] = −sn[j]·s[j]
      K.H[:, j] = h_new
      K.beta = |K.s[j+1]|
      return K
      ```
      The LS-residual proxy `K.beta` updates in O(1) per step; no explicit LS solve runs inside the inner loop.
  - claim_index: 4
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L2 — primitive composition / **`back_solve(K, j)`.**
    quoted_lines: |
      **`back_solve(K, j)`.** Standard back-substitution against the now-triangular `K.H[0..=j, 0..=j]`:
      ```
      y[j] = K.s[j] / K.H[j, j]
      for k in (j-1)..0:
        y[k] = K.s[k]
        for i in (k+1)..=j: y[k] -= K.H[k, i] · y[i]
        y[k] /= K.H[k, k]
      return y
      ```
      No per-element primitive substitution; this is a small dense O(j²) kernel on the LS state, not on field state.
  - claim_index: 5
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L2 — primitive composition / **`apply_correction(op, K, y, j, x)`.**
    quoted_lines: |
      **`apply_correction(op, K, y, j, x)`.** Unfolds into `axpy`s, with one optional terminal `apply_linop`:
      ```
      if op.flexible:                              // FGMRES
        for k in 0..=j: axpy(y[k], K.Z[k], x)      // x += Σ y[k]·Z[k]
      elif op.pc_side == RIGHT:                    // fixed-M GMRES, right
        t ← 0; for k in 0..=j: axpy(y[k], K.V[k], t)
        apply_linop(op.M, t, Mt); axpy(1, Mt, x)   // x += M·(Σ y[k]·V[k])
      else:                                        // LEFT or no-preconditioner
        for k in 0..=j: axpy(y[k], K.V[k], x)      // x += Σ y[k]·V[k]
      return x
      ```
- Verdict: pass.
- Friction: none.
- Structural change: applied: 2 lesson(s); 6 rotation_claim(s).
