## 2026-05-24 cycle-21 — forward gmres [L1→L2] — revise

- Synthesis: GMRES L1→L2: unfolded the five L1 building-blocks (initial_residual, apply_BA, orthogonalize, ls_update_column, back_solve, apply_correction) into named base primitives (apply_linop, axpy, dot, nrm2, scal, givens_generate/apply2, trsv). Extracted seven concept entries for the BLAS-style vocabulary. orthogonalize_column remains opaque pending the orthog slice. Numerical-claim register distinguishes load-bearing claims (Givens algorithm, replay-then-generate order, β as |s[j+1]|) from transparent fusions.
- Verdict: revise.
- Friction: slice_write diff failed for book/src/spec/slices/gmres.md: git apply failed:
STDERR:
error: No valid patches in input (allow with "--allow-empty")

DIFF:
--- a/book/src/spec/slices/gmres.md
+++ b/book/src/spec/slices/gmres.md
@@
 - `CheckDot` NaN/Inf gating semantics (referenced from the inner loop's residual checks) is cross-cutting across all iterative solvers and not pinned here.
 
+## L2 — primitive composition
+
+The L2 form unfolds each L1 building-block into a sequence of named base primitives — `apply_linop`, `axpy`, `dot`, `nrm2`, `scal`, `givens_generate`, `givens_apply2`, `trsv` — plus the dispatched orthogonalisation kernel (deferred to the `orthog` slice). Optimization-transparent fusions (e.g., MGS's dot+axpy fused inner step, packed-rotation registers) are silent; load-bearing numerical choices (rotation algorithm, in-place column update order) are explicit.
+
+### Primitive vocabulary
+
+See `concepts/` for canonical definitions:
+- [`apply_linop`](../../concepts/apply_linop.md) — `y ← L · x` for an abstract linear operator `L`.
+- [`axpy`](../../concepts/axpy.md) — `y ← α·x + y`.
+- [`dot`](../../concepts/dot.md) — `α ← ⟨x, y⟩`.
+- [`nrm2`](../../concepts/nrm2.md) — `α ← ‖x‖₂`.
+- [`scal`](../../concepts/scal.md) — `x ← α·x`.
+- [`givens_generate`](../../concepts/givens.md#generate) — `(cs, sn) ← G(dx, dy)`. Cites L0.3.
+- [`givens_apply2`](../../concepts/givens.md#apply) — in-place 2-vector update `(dx, dy) ← (cs·dx + sn·dy, −s̄n·dx + cs·dy)`. Cites L0.4.
+- [`trsv`](../../concepts/trsv.md) — triangular solve `T · y = s`.
+- `orthogonalize_column(gs_orthog, V[0..j], w) → (w', h)` — dispatched at L1 into one of `mgs / cgs / cgs2`; L2 internals live in the `orthog` slice.
+
+### Building-block unfoldings
+
+**`initial_residual(op, b, x)`** (cites L0.5).
+
+```
+initial_residual(op, b, x):
+  if not op.initial_guess:
+    x ← 0                                                     // scal(0, x) or zero-fill
+    if op.pc_side == LEFT and op.B != null:
+      r0 ← apply_linop(op.B, b)                               // r0 = M·b
+    else:
+      r0 ← b                                                  // copy
+  else:
+    t ← apply_linop(op.A, x)                                  // t = A·x
+    axpy(-1, t, b_copy=b)        // r = b − A·x  (b unchanged; r0 holds result)
+    r0 ← b_copy
+    if op.pc_side == LEFT and op.B != null:
+      r0 ← apply_linop(op.B, r0)                              // r0 ← M·(b − A·x)
+  return (r0, x)
+```
+
+**`apply_BA(op, v)`** (cites L0.6). Canonical primitive sequence; `pc_side` selects which two `apply_linop` calls compose and which intermediate is exposed as `z`.
+
+```
+apply_BA(op, v):
+  if op.B == null:
+    w ← apply_linop(op.A, v); z ← ⊥
+  elif op.pc_side == LEFT:
+    t ← apply_linop(op.A, v); w ← apply_linop(op.B, t); z ← ⊥
+  else:  // RIGHT
+    z ← apply_linop(op.B, v); w ← apply_linop(op.A, z)
+  return (w, z)
+```
+
+**`orthogonalize(gs_orthog, V[0..j], w) → (w', h[0..j])`** (cites L0.7). Dispatches to the `orthog` slice. The L2 contract here: input `w`, basis prefix `V[0..j]`; output `w'` orthogonal to `span(V[0..j])` (to working precision per `gs_orthog`) and `h` the projection coefficients. The final normalisation step `h[j+1] ← nrm2(w'); scal(1/h[j+1], w')` is explicit in the L2 procedure below, not absorbed into `orthogonalize_column`.
+
+**`ls_update_column(K, j, h)`** (cites L0.3, L0.4). Incremental triangularisation of the Hessenberg column via stored Givens rotations.
+
+```
+ls_update_column(K, j, h):
+  // 1. Replay previously-recorded rotations on the new column.
+  for k in 0 .. j-1:
+    givens_apply2(h[k], h[k+1], K.cs[k], K.sn[k])
+  // 2. Generate a fresh rotation from the column tail (h[j], h[j+1]).
+  (K.cs[j], K.sn[j]) ← givens_generate(h[j], h[j+1])
+  // 3. Apply it to the column itself: h[j+1] is annihilated.
+  givens_apply2(h[j], h[j+1], K.cs[j], K.sn[j])
+  // 4. Apply the same rotation to the RHS pair (s[j], s[j+1]); s[j+1] was 0.
+  givens_apply2(K.s[j], K.s[j+1], K.cs[j], K.sn[j])
+  // 5. Store the rotated column into H and advance β.
+  K.H[:, j] ← h
+  K.beta ← |K.s[j+1]|
+  return K
+```
+
+The order (replay-then-generate-then-apply) is load-bearing: the new rotation must be generated *after* the prior rotations have been replayed on the new column, so `h[j+1]` is the post-replay tail.
+
+**`back_solve(K, j) → y`** (cites L0.12). The active block of `H` is now upper-triangular by construction of step 3 above.
+
+```
+back_solve(K, j):
+  // K.H[0..j, 0..j] is upper-triangular; K.s[0..j] is the rotated RHS.
+  y ← trsv(upper=K.H[0..j, 0..j], rhs=K.s[0..j])
+  return y
+```
+
+**`apply_correction(op, K, y, j, x)`** (cites L0.12, L0.13).
+
+```
+apply_correction(op, K, y, j, x):
+  if op.flexible:
+    for k in 0 .. j:
+      axpy(y[k], K.Z[k], x)                                   // x ← x + y[k]·Z[k]
+  elif op.pc_side == RIGHT and op.B != null:
+    t ← 0
+    for k in 0 .. j:
+      axpy(y[k], K.V[k], t)                                   // t = Σ y[k]·V[k]
+    Mt ← apply_linop(op.B, t)
+    axpy(1, Mt, x)                                            // x ← x + M·t
+  else:  // LEFT or no preconditioner
+    for k in 0 .. j:
+      axpy(y[k], K.V[k], x)
+  return x
+```
+
+### Inner-loop primitive sequence
+
+At step `j` of the inner (Arnoldi) loop the L2 primitive chain is:
+
+```
+(w, z) ← apply_BA(op, V[j])                  // 1–2 apply_linop
+if flexible: Z[j] ← z
+(w', h[0..j]) ← orthogonalize_column(gs, V[0..j], w)   // → orthog slice
+h[j+1] ← nrm2(w'); scal(1 / h[j+1], w'); V[j+1] ← w'    // basis-vector normalisation
+ls_update_column(K, j, h)                    // (j) givens_apply2 replays + 1 givens_generate + 2 givens_apply2
+```
+
+This shape is invariant across the four variant combinations `pc_side × flexible`: only `apply_BA` and the `Z[j] ← z` capture differ, exactly as the L1 absorption claims.
+
+### Numerical-claim register
+
+Load-bearing (preserved across L1→L2):
+- **Rotation algorithm.** `givens_generate` is LAPACK-style scaled (avoids overflow on large `|dx|`, `|dy|`); a naïve `(c,s) = (dx, dy)/√(dx²+dy²)` is not equivalent under finite precision.
+- **Column-update order in `ls_update_column`.** Replay-then-generate-then-apply (above). Reordering breaks the triangularisation invariant.
+- **CGS2 refinement semantics** (deferred to `orthog` slice) is load-bearing for backward stability of GMRES.
+- **β as `|s[j+1]|`.** The residual proxy used for the convergence test is the rotated-RHS tail, not a re-evaluated `‖b − A·x_j‖`. The two agree only up to LS-step accuracy.
+
+Transparent (silently unfolded):
+- Storage layout of `V` (row-major vs. column-major; packed vs. separate vectors).
+- Fusion of `dot`+`axpy` inside MGS, or of the final `nrm2`+`scal` for `V[j+1]`.
+- Whether `givens_apply2` is implemented as four FMAs or as a packed BLAS rot-call.
+- Whether `back_solve`'s `trsv` runs on a CPU triangular kernel or a dense GEMV-then-divide chain — `H` is `O(max_dim²)` and `max_dim` is small, so the choice has no algorithmic consequence.
+
+## Open questions (extends earlier list)
+
+- The exact loop structure of MGS / CGS / CGS2 (collective shape, refinement test) is deferred to the `orthog` slice. The L2 form here treats `orthogonalize_column` as one opaque primitive.
+- `back_solve`'s handling of a near-singular leading block (when GMRES has effectively converged but the LS system is rank-deficient) is not pinned at L2; the L0 code uses a straight back-substitution and relies on the convergence test to catch the case.
; dependency_map_edge failed for apply_linop: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for axpy: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for dot: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for nrm2: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for scal: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for givens: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for trsv: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for gmres: no ```mermaid block in section '## L2 —'; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
