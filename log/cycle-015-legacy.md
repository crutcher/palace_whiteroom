## 2026-05-24 cycle-15 — back gmres — pass

- Synthesis: 2 rotation_claim(s); diff applied
- Verdict: pass.
- Friction: diff-apply failed: git apply failed:
STDERR:
error: corrupt patch at line 90

DIFF:
--- /dev/null
+++ b/book/src/spec/slices/gmres.md
@@ -0,0 +1,93 @@
+# Slice: gmres
+
+Generalized Minimal Residual method for solving Ax = b where A is a general
+(possibly non-symmetric, possibly indefinite) linear operator. Krylov subspace
+projection method that minimizes the residual 2-norm over an affine Krylov
+subspace.
+
+## L0 — mutation reference
+
+Canonical reference: Saad, *Iterative Methods for Sparse Linear Systems*, 2nd
+ed., Algorithm 6.9 (GMRES) and 6.11 (Restarted GMRES). Palace's hypre/PETSc
+wrappers expose this as a black-box; the L0 mutation reference is the textbook
+pseudocode (mutable arrays for the Krylov basis V, the upper-Hessenberg H̄, the
+residual-rotated RHS vector g, and the Givens parameters (c_i, s_i)).
+
+The pseudocode threads loop counters, mutable Hessenberg entries, mutable
+Givens-rotated RHS, mutable basis-column writes, and a happy-breakdown early
+exit. This is the L0 form; the slice does not duplicate the textbook listing.
+
+## L1 — invariant form
+
+**Inputs.** Operator `A : V → V` (linear), right-hand side `b ∈ V`, initial
+guess `x_0 ∈ V`, preconditioner `M` (possibly identity), restart length `m ∈
+ℕ_{≥1}`, tolerance `τ > 0`, max outer restarts `k_max`.
+
+**Side convention.** A preconditioner side (left / right / split / none) is
+fixed at solver construction. The L1 statement is written for an effective
+operator `Â` and effective RHS `b̂` constructed once from `(A, M, side)`;
+downstream L1 does not re-inspect `side`. See
+`book/src/concepts/constructed-operators.md`.
+
+**Statement (one restart cycle).** Given current iterate `x`, with `r =
+b̂ − Â x` and `β = ‖r‖_2`:
+
+1. Build an orthonormal basis `V_m = [v_1, …, v_m]` of the Krylov subspace
+   `𝒦_m(Â, r) = span{r, Â r, Â² r, …, Â^{m−1} r}`, with `v_1 = r / β`, such
+   that there exists an upper-Hessenberg matrix `H̄_m ∈ ℝ^{(m+1)×m}` with
+   `Â V_m = V_{m+1} H̄_m`.
+2. Select `y_m ∈ ℝ^m` minimizing `‖β e_1 − H̄_m y‖_2`.
+3. Update `x ← x + V_m y_m`.
+4. The new residual norm equals the least-squares residual
+   `‖β e_1 − H̄_m y_m‖_2`; this is monitored against `τ` and may trigger
+   early termination of the inner cycle before reaching dimension `m`
+   (happy breakdown when an Arnoldi sub-diagonal vanishes; convergence when
+   the running residual estimate falls below `τ‖b̂‖_2`).
+
+The outer loop restarts steps 1–4 with the updated `x` until convergence or
+`k_max` cycles. Flexible variants (where the right-preconditioner is allowed
+to change between Arnoldi steps) replace step 1's invariant with the
+flexible-Arnoldi invariant `Â Z_m = V_{m+1} H̄_m` where `Z_m`'s columns are
+the per-step preconditioned basis; this is out of scope for this slice (see
+Open Questions).
+
+**Invariants.**
+- (Orthonormality) `V_m^T V_m = I_m`.
+- (Arnoldi relation) `Â V_m = V_{m+1} H̄_m`.
+- (Optimality) `x_m − x_0 ∈ 𝒦_m(Â, r_0)` minimizes `‖b̂ − Â x‖_2` over
+  that affine subspace.
+- (Monotonicity within a cycle) `‖r_{j+1}‖_2 ≤ ‖r_j‖_2`.
+
+**Outputs.** Final iterate `x`, achieved residual norm, iteration count,
+convergence flag.
+
+## State partition (for L4 staging)
+
+- **Sim state.** `x` (the iterate).
+- **Operator-internal / per-solve.** The Krylov basis `V_{·}`, the
+  Hessenberg `H̄_{·}`, the least-squares state used to extract `y` and the
+  running residual estimate, the Givens / orthogonalization scratch — all
+  live for one restart cycle and are reset across restarts. The L1
+  statement treats these as existentially quantified ("there exists
+  `H̄_m`…"); they are realized as mutable per-solve workspace at L2.
+- **Ephemeral.** The matvec output buffer `Â v_j`, dot-product reductions
+  inside Arnoldi.
+
+## Open questions / out of scope
+
+- Flexible GMRES (FGMRES): variable right-preconditioner per Arnoldi step.
+  Separate slice — different Arnoldi invariant.
+- Choice of orthogonalization scheme (CGS / CGS2 / MGS / Householder) is
+  an L2 implementation axis, not an L1 axis; the L1 invariant
+  `V_m^T V_m = I_m` is identical across schemes (modulo floating-point
+  loss-of-orthogonality, which is a numerical-quality claim about the L2
+  realization, not about L1).
+- Block GMRES (multiple RHS): separate slice.
+- Adaptive restart-length policies: separate slice.
.
- Structural change: applied diff (89 lines); 2 rotation_claim(s).
