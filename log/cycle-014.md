## 2026-05-24 cycle-14 — forward gmres [L1→L2] — revise

- Synthesis: 5 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: diff-apply failed: git apply failed:
STDERR:
error: corrupt patch at line 143

DIFF:
--- /dev/null
+++ b/book/src/spec/slices/gmres.md
@@ -0,0 +1,142 @@
+# Slice: gmres
+
+GMRES (Generalized Minimal RESidual) for solving `A x = b` with a general
+(possibly non-symmetric, possibly indefinite) linear operator `A`. The
+slice covers right-preconditioned, restarted GMRES(m) with classical or
+modified Gram-Schmidt orthogonalization, and a flexible-preconditioner
+(FGMRES) variant. Left preconditioning and unrestarted GMRES are recovered
+as degenerate cases (restart = ∞; constructed preconditioner = identity
+or wrapped on the left).
+
+## L0 — sources
+
+Pending. Explorer has not yet landed L0 facts for this slice; this push
+establishes L1 and L2 forward from textbook GMRES (Saad & Schultz 1986;
+Saad, *Iterative Methods for Sparse Linear Systems*, ch. 6) so that
+downstream rotations have a target. L0 citations will be back-filled
+from `palace/` source once Explorer reaches this slice.
+
+## L1 — unified statement
+
+**Inputs.** Linear operator `A`, right-hand side `b`, initial guess `x0`,
+preconditioner operator `M` (constructed once at solve start —
+see [constructed-operators](../../concepts/constructed-operators.md)),
+tolerances `(rtol, atol)`, restart length `m`, max outer iterations.
+
+**Constructed operator absorbs variants.** The variant axes
+— preconditioner side (left / right / split), flexibility
+(fixed `M` vs. per-step `M_k`), and identity-vs-nontrivial — are absorbed
+into `M` at construction time. The per-step procedure calls `M.apply(v)`
+uniformly and does not re-inspect the variant. See
+[variant-absorption](../../concepts/variant-absorption.md).
+
+**Invariant.** GMRES(m) produces, at the end of each inner cycle, the
+iterate `x_m ∈ x_0 + K_m(A M, r_0)` (right-preconditioned Krylov
+subspace) that minimizes the Euclidean residual norm `‖b - A x‖` over
+that affine subspace. Equivalently: with `V_m` an orthonormal basis of
+`K_m(A M, r_0)` and `H̄_m` the `(m+1) × m` upper-Hessenberg matrix
+satisfying the Arnoldi identity `A M V_m = V_{m+1} H̄_m`, the iterate is
+`x_m = x_0 + M V_m y_m` where `y_m = argmin_y ‖ β e_1 - H̄_m y ‖_2` and
+`β = ‖r_0‖`.
+
+**Procedure (one inner cycle, length up to m).**
+
+1. Form initial residual `r_0 = b - A x_0`, `β = ‖r_0‖`, `v_1 = r_0 / β`.
+2. For `j = 1, …, m` (early-exit when the residual estimate meets
+   tolerance):
+   - Apply the operator chain to produce the next Krylov direction:
+     `w = A · M.apply(v_j)`.
+   - Orthogonalize `w` against `{v_1, …, v_j}` (the orthogonalization
+     variant — CGS / MGS / CGS2 — is bound at solver construction and
+     applied uniformly here), yielding the new Hessenberg column
+     and `v_{j+1}`.
+   - Maintain an incremental least-squares solution for the projected
+     subproblem `min_y ‖β e_1 - H̄_j y‖`, exposing the current residual
+     estimate.
+3. Form `x_m = x_0 + M.apply(V_m y_m)` and either return (converged /
+   max iters) or restart with `x_0 ← x_m`.
+
+**Termination.** `‖r_k‖ ≤ max(rtol · ‖b‖, atol)`, or outer iteration
+budget exhausted. The residual estimate from the projected least-squares
+is exact for the true residual norm up to orthogonalization quality;
+slices that need a guaranteed bound recompute `‖b - A x‖` explicitly at
+restart boundaries.
+
+## L2 — primitive composition
+
+Bound at solver construction (not re-inspected per step):
+- `M : LinOp` — the constructed preconditioner (absorbs side / flexibility).
+- `orth : OrthogonalizationStrategy` — CGS / MGS / CGS2, exposing
+  `orth.extend(V_j, w) → (h_col, v_next)` that returns the new Hessenberg
+  column and the next basis vector.
+- `lsq : ProjectedLeastSquares` — an incremental solver for
+  `min_y ‖β e_1 - H̄_j y‖` exposing `lsq.push(h_col) → residual_estimate`
+  and `lsq.solve() → y`. (The internal representation — Givens-rotated
+  QR of `H̄_j`, normal-equations, or otherwise — is L3 implementation
+  detail; L2 sees only `push` / `solve` / `residual_estimate`.)
+
+Per-step primitive chain (one Arnoldi step `j`):
+
+```text
+z_j      = M.apply(v_j)                       # apply_linop
+w        = A.apply(z_j)                       # apply_linop
+(h_j, v_{j+1}) = orth.extend(V_j, w)          # orthogonalization step
+ρ_j      = lsq.push(h_j)                      # incremental LS update,
+                                               # returns residual estimate
+```
+
+At cycle close (length-`k` cycle, either converged or restart):
+
+```text
+y        = lsq.solve()                        # k-vector
+u        = matvec(V_k, y)                     # linear combination of basis
+                                               # vectors: u = Σ y_i v_i
+δx       = M.apply(u)                         # apply_linop
+x        = axpy(1, δx, x_0)                   # x ← x_0 + δx
+```
+
+At cycle open:
+
+```text
+Ax_0     = A.apply(x_0)                       # apply_linop
+r_0      = axpy(-1, Ax_0, b)                  # r_0 ← b - A x_0
+β        = norm(r_0)                          # √dot(r_0, r_0)
+v_1      = scale(1/β, r_0)                    # axpy-family
+```
+
+The primitives invoked — `apply_linop`, `axpy`, `dot`, `norm`, `scale`,
+`matvec` (in the sense of a basis-times-coefficients linear combination)
+— are the standard support-operator vocabulary; orthogonalization itself
+is a slice-local concept (see below).
+
+## Open questions / out of scope
+
+- Choice of `orth` (CGS / MGS / CGS2) and its numerical-stability
+  trade-offs are bound at construction and not re-inspected; the
+  algebraic claim that all three produce the same L1 minimum-residual
+  iterate (up to round-off) is taken for granted here and is the subject
+  of a separate orthogonalization-strategy slice.
+- Happy breakdown (`h_{j+1,j} = 0`): treated as convergence (the Krylov
+  subspace is `A M`-invariant; the current `y` is exact). Spec'd in L1
+  as part of the early-exit path; mechanism for detection lives at L2
+  inside `orth.extend`.
+- L3 (global tensor-field form) and L4 (state-typed monadic form) are
+  pending; the projected least-squares state is the non-obvious piece
+  and may force an obstruction claim at L2→L3 (the Hessenberg column is
+  sequentially extended).
+
+## Concepts referenced
+
+- [apply_linop](../../concepts/apply_linop.md)
+- [axpy](../../concepts/axpy.md)
+- [dot](../../concepts/dot.md)
+- [constructed-operators](../../concepts/constructed-operators.md)
+- [variant-absorption](../../concepts/variant-absorption.md)
+
+Slice-local concept (to be extracted when a second slice needs it):
+`orthogonalization-strategy` — the CGS/MGS/CGS2 family as a uniform
+interface `extend(V, w) → (h_col, v_next)`. Likely shared with
+block-GMRES, Arnoldi eigensolvers, and FOM.
; Variant absorption via constructed M is claimed at all three levels, but FGMRES (flexible / per-step M_k) is a known counterexample to clean absorption: the L1 update formula x_m = x_0 + M V_m y_m is INCORRECT for FGMRES — flexible GMRES must store the preconditioned basis Z_m = [z_1, …, z_m] (with z_j = M_j v_j) separately because there is no single M to apply at cycle close. The cycle-close primitive chain ( u = matvec(V_k, y); δx = M.apply(u); x = axpy(1, δx, x_0) ) therefore does NOT have the same shape across variant values: fixed-M cycle close goes through M.apply once, flexible-M cycle close skips M.apply entirely and uses δx = matvec(Z_k, y). This is variant-absorption check (c) primitive-sequence-divergence, undeclared. Either declare flexible-M as a residual axis with its own cycle-close shape, or push back: introduce Z as an additional bound state in L1 (the 'preconditioned basis' stream) so the cycle-close primitive becomes δx = matvec(Z_k, y) uniformly (and fixed-M is the case Z_j = M.apply(v_j) recomputed-or-cached).; Prose-rotation-alignment is good (L1 says 'incremental least-squares update', not 'Givens'). However, the residual estimate ρ_j returned by lsq.push is the projected-LS residual, which is NOT the true residual ‖b - A x_j‖ when orthogonalization loses orthogonality — the L1 termination prose acknowledges this ('exact ... up to orthogonalization quality') but the L2 interface presents ρ_j as if it were the convergence-test input with no further qualification. The slice should either (a) make the residual_estimate's semantics part of the interface contract (it's the projected-LS residual, valid as a convergence proxy under maintained orthogonality), or (b) declare a separate true-residual recomputation primitive at restart boundaries (which the L1 prose hints at but L2 does not surface). Currently L2 under-specifies the contract.; Same issue as claim 1: the cycle-close chain u = matvec(V_k, y); δx = M.apply(u) is only valid for fixed-M. For FGMRES, δx = matvec(Z_k, y) directly with no M.apply, because each z_j was produced by a different M_j. The claim that the rotation is mechanical and one-to-one holds only after the L1 state schema is fixed to thread Z (see push-back on claim 1)..
- Structural change: none.
