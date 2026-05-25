## 2026-05-25 cycle-73 — forward gmres [L2→L3] — pass

- Synthesis: Retroactive L2→L3 rotation_claims for the gmres slice's already-landed L3 section (cycle 23). Two claims: (1) field-side primitives (axpy/dot/nrm2/scal/apply_linop) lift to global tensor-field operations and the CGS-shape orthogonalize/apply_correction collapse to batched tall-skinny operations; (2) obstruction record for `ls_update_column` and `back_solve` as sequential recurrences on small-dense state with no DoF index set, classified per sequential-obstruction. retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L3 — global tensor-field form
    quoted_lines: |
      - `axpy(α, x, y)`, `scal(α, x)`, `dot(x, y)`, `nrm2(x)` — pointwise / reduction over the global DoF index set. See [concept: tensor-field-lift] for the L2→L3 lift template for the support-operator family.
      - `apply_linop(L, x, y)` — `y = L · x` as a global linear map over the DoF field. `A` is an assembled (or matrix-free) operator on the field; `M` is the preconditioner as a field-to-field linear map. No per-element loop survives at L3.
      **`orthogonalize` (global, CGS shape).**
      h[0..j] = Vᴴ_{0..j} · w           // batched projection: a single (j+1)×n × n vector product
      w       = w − V_{0..j} · h[0..j]   // batched subtraction: a single n × (j+1) × (j+1) update
      This is the CGS / CGS2 form; the global tensor view treats `V_{0..j}` as an `n × (j+1)` tall-skinny matrix and the projection as a single tall-skinny-matrix transpose-times-vector reduction. MGS does not have a single-shot global form ... — this is an internal-to-`orthogonalize` obstruction routed to the `orthog` slice
  - claim_index: 1
    on_disk_path: book/src/spec/slices/gmres.md
    section: ## L3 — global tensor-field form / Obstruction: incremental LS triangularisation
    quoted_lines: |
      **Claim (L3 obstruction).** `ls_update_column` does **not** lift to a global tensor-field operation, and this is structural rather than an artifact of presentation.
      1. Replay rotations `0..j` on the new column in order — rotation `k+1` operates on the output of rotation `k`. This is a sequential reduction over `k` with no associativity (the rotation matrices do not commute), so it does not collapse to a parallel reduction.
      The loop-carried dependency is on a small dense O(j) state (the rotation registers and the RHS), not on field state. ... The LS state is not a tensor field in the L3 sense (no DoF index set), so there is no global form to lift into.
      This is a classical *sequential algorithm* obstruction in the sense of [concept: sequential-obstruction]: the recurrence is on dense state of size O(j) where `j ≤ max_dim` is typically O(10²)–O(10³).
      The terminal `back_solve(K, j)` operates on the same small dense `(j+1)×(j+1)` triangular state. The serial back-substitution is the textbook sequential triangular solve. As with `ls_update_column`, this is not field state and not a tensor-field operation; the L1 form is the L3 form.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 lesson(s); 2 rotation_claim(s).
