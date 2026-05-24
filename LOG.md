# Cycle log

Per-cycle human-readable summaries, newest first. Full structured detail in `episodic.jsonl`; full meta-review records in `book/src/meta-reviews/`.

Per-cycle entry format:

```
## YYYY-MM-DD cycle-<N> — <push-kind> <slice> [<edge>] — <verdict>

- Synthesis: <one-line summary of what the cycle produced>.
- Verdict: <pass | revise | reject>. <Brief issues if not pass.>
- Friction: <none | one-line>.
- Structural change: <none | one-line>.
```

Meta-review entry format:

```
## YYYY-MM-DD meta-review (cycles <N>–<M>) — <enacted | partial | deferred>

- Window: <N> cycles. Push breakdown: <X FORWARD, Y BACK, Z SIDEWAYS>.
- Cascade: <a> LOW applied; <b> MEDIUM plan items <approved|deferred>; <c> HIGH escalated.
- Plan items enacted: <one-line summaries, or "none">.
- Recurring patterns: <none | one-line description>.
- Full record: `book/src/meta-reviews/YYYY-MM-DD.md`.
```

New entries are **prepended** immediately below the `---` separator, above prior entries.

---

## 2026-05-24 cycle-6 — back gmres — revise

- Synthesis: 2 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L0→L1 rotation does real work (state hiding: V, H, s/sn/cs, the enum dispatch, and the Givens accumulator are all hidden behind 'four concerns'), so it is a genuine rotation under criterion (a). However, the FGMRES paragraph is bolted onto the end of L1 rather than absorbed: the rotation 'GMRES is x_m = x_0 + V_m y_m' has to be locally patched to 'x_m = x_0 + Z_m y_m' for FGMRES, which suggests the L1 form should have been stated as 'x_m = x_0 + W_m y_m where W_m is the *update basis* (= V_m for GMRES, = Z_m for FGMRES) and A W_m = V_{m+1} H̄_m'. That unified form would make FGMRES a parameter choice rather than a variant..
- Structural change: none.
## 2026-05-24 cycle-5 — back gmres — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L1 description threads V, H, g, cs, sn, x, j all together through a single monolithic step 2 loop. This is fine for L1 (rotation criterion (a) state-hiding will happen at L1→L2 by introducing an arnoldi_step primitive that hides H/cs/sn/g update), but the current Procedure is written in a way that fuses (i) Arnoldi orthogonalization, (ii) Givens update, (iii) residual monitor into one numbered list. Consider whether step 2.5 and 2.6 should be presented as a separable 'projected-problem update' sub-procedure even at L1 — this would make the L1→L2 boundary cleaner. Not blocking, but worth flagging..
- Structural change: none.
## 2026-05-24 cycle-4 — forward gmres [L1→L2] — revise

- Synthesis: 4 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: Claim 2 mixes two distinct primitives (trsv_upper and gemv) into a single L1→L2 edge and then immediately equivocates in the justification ('whether the gemv is realized as one BLAS-2 call or k axpys is a transparent optimization'). This is the friction signal: if the gemv ↔ k-axpys choice is transparent, then the L2 form is not canonical — two different L2 expressions denote the same semantics. Either pin gemv as the L2 primitive and demote axpy-panel to L3 implementation, or split the solution-assembly rotation into its own edge with an explicit primitive choice.; The L1→L2 Arnoldi rotation is essentially a renaming: each L1 line maps to a single named BLAS primitive with identical sequentiality and identical threaded state (w, V columns, H column). Per rotation.md, a rotation should (a) hide state, (b) admit coarser substitution, or (c) compress threaded state. None of these holds here — w is still threaded, the MGS sequential dependency is still exposed, H[i,j] is still indexed elementwise. The genuine rotation would be to an `arnoldi_step(A, V, H, j) -> v_{j+1}` primitive that hides the index/loop and admits MGS↔CGS2 substitution at the L2 grain. As written, L2 is L1 with BLAS names sprinkled in..
- Structural change: none.
## 2026-05-24 meta-review (cycles 1–3) — enacted

- Window: 3 cycles. Push breakdown: 3 FORWARD, 0 BACK, 0 SIDEWAYS.
- Cascade: 1 LOW applied; 3 MEDIUM plan items approved and enacted; 0 HIGH escalated.
- Plan items enacted: diff-hygiene note in `prompts/synthesizer.md`; slice-scoping rule + claim coverage in `book/src/spec/index.md`; rotation_claim coverage requirement; new `book/src/concepts/rotation.md` (rotation quality criteria) + Critic verification check #8.
- Recurring patterns: none yet (first meta-review). Watch list: Meta-Critic file-path drift, rotation-quality false positives.
- Full record: `book/src/meta-reviews/2026-05-24.md`.

## 2026-05-24 cycle-3 — forward gmres [L1→L2] — revise

- Synthesis: 0 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L2 'Per-iteration composition' block is essentially the L1 inner loop rewritten with primitive names — the rotation L1→L2 collapses to a renaming rather than a genuine algebraic compression. Symptom: the outer composition still has to thread V, H, g, cs, sn through `arnoldi_with_givens` as an opaque bundle, and the per-iteration block exposes index arithmetic (H[0..j+1, j], V[:,0..j]) at L2..
- Structural change: none.
## 2026-05-24 cycle-2 — forward gmres [L0→L1] — pass

- Synthesis: 0 rotation_claim(s); diff applied
- Verdict: pass.
- Friction: diff-apply failed: git apply failed:
STDERR:
error: corrupt patch at line 118

DIFF:
--- a/book/src/spec/slices/gmres.md
+++ b/book/src/spec/slices/gmres.md
@@ -0,0 +1,166 @@
+# gmres
+
+## L1 — Mutation-level decomposition
+
+### State (per solver instance, all `mutable`, persisted across `Mult` calls)
+
+- `V`: `std::vector<VecType>` of length `max_dim+1` — Krylov basis vectors. Each entry sized to `A->Height()` on demand. `V[j+1]` with `Size()==0` indicates not-yet-allocated.
+- `H`: packed Hessenberg matrix, column-major, leading dimension `max_dim+1`. Column `j` lives at `H.data() + j*(max_dim+1)`, rows `0..j+1`.
+- `s`: least-squares RHS, length up to `max_dim+1`. After step `j`, `|s[j+1]|` is the recursion-estimated residual norm.
+- `cs[0..max_dim)`: real cosines of accumulated Givens rotations.
+- `sn[0..max_dim)`: scalar (real or complex) sines of accumulated Givens rotations.
+- `r`: residual scratch, length `A->Height()`. Doubles as preconditioner-apply scratch.
+- (FGMRES only) `Z`: second basis of length `max_dim+1`, storing `B V[j]` per step.
+
+### Configuration (immutable post-construction)
+
+- `max_dim`: restart dimension (GMRES(m), m = max_dim). Defaults to `max_it` on first `Initialize`.
+- `max_it`: global iteration cap across restart cycles.
+- `rel_tol`, `abs_tol`: convergence thresholds; effective `eps = max(rel_tol * initial_res, abs_tol)`.
+- `gs_orthog ∈ {MGS, CGS, CGS2}`: orthogonalization variant.
+- `pc_side ∈ {LEFT, RIGHT, NONE}`: preconditioner side. FGMRES forces RIGHT.
+- `initial_guess`: if false, `x` is zeroed before solving.
+
+### Mutation: `Initialize()` — lazy allocation
+
+- **Pattern**: in-place overwrite (idempotent no-op on matching sizes).
+- First call: size `V` to `max_dim+1`; allocate `V[0..init_size)` at `A->Height()`, where `init_size=5`; size `s,cs,sn` to `min(init_size+1, max_dim+1)`; size `H` to `(max_dim+1) * min(init_size, max_dim)`.
+- Subsequent calls: assert operator height and `max_dim` unchanged; otherwise no-op.
+- Citations: `palace/linalg/iterative.cpp:488–515`.
+
+### Mutation: `Update(j)` — incremental growth
+
+- **Pattern**: in-place overwrite, called from Arnoldi inner loop when `V[j+1].Size()==0`.
+- Grow basis: allocate `V[j+1 .. min(j+1+add_size, max_dim+1))` at `A->Height()`, `add_size=10`.
+- Grow `H` to `(max_dim+1) * min(j+1+add_size, max_dim)` entries.
+- Grow `s,cs,sn` to `min(j+2+add_size, max_dim+1)`.
+- Citations: `palace/linalg/iterative.cpp:518–541`.
+
+### Mutation: `Mult(b, x)` — outer restart loop
+
+- **Pattern**: complex; coordinates Arnoldi inner loop, restart, and convergence.
+- Pseudocode (per restart cycle, indexed by `restart`):
+  1. `InitialResidual(pc_side, A, B, b, x, r, V[0])` populates `r`:
+     - `LEFT`: `r = B(b - A x)` (or `B b` if `!initial_guess`).
+     - `RIGHT`/`NONE`: `r = b - A x` (or `b` if `!initial_guess`).
+  2. `beta = ||r||_2` (MPI-collective via `linalg::Norml2`).
+  3. On `restart==0`: `initial_res = beta`; `eps = max(rel_tol*initial_res, abs_tol)`.
+  4. On `restart>0`: compare `beta` (recomputed) to `s[0]` from previous cycle; warn if divergence exceeds threshold (residual recursion drift).
+  5. If `beta < eps`: set `converged=true`, break outer loop.
+  6. `V[0] = r / beta`; zero `s`; `s[0] = beta`.
+  7. **Arnoldi inner loop** for `j = 0, 1, ...` (see below).
+  8. On inner-loop exit (any reason): **solution reconstruction** (see below).
+  9. If `converged`, break outer; else next restart cycle.
+- Outer termination: `it >= max_it` OR `converged`.
+- Citations: `palace/linalg/iterative.cpp:543–705`.
+
+### Mutation: Arnoldi inner step (per `j`)
+
+- **Pattern**: complex (basis extension + Hessenberg column build + Givens QR update).
+- (a) `w := V[j+1]`; if `w.Size()==0` call `Update(j)`.
+- (b) **Matvec with preconditioner dispatch** via `ApplyBA(pc_side, A, B, V[j], w, r)`:
+  - `LEFT`: `r = A V[j]; w = B r` → Krylov basis for `B A`.
+  - `RIGHT`: `r = B V[j]; w = A r` → Krylov basis for `A B`.
+  - `NONE`: `w = A V[j]`.
+  - FGMRES (RIGHT only): `Z[j] = B V[j]; w = A Z[j]` — `Z[j]` is preserved, not scratch.
+- (c) **Orthogonalize** `w` against `V[0..j]` via `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j+1)`:
+  - `MGS`: sequential — for `k=0..j`: `Hj[k] = <V[k], w>` (MPI GlobalSum per `k`); `w -= Hj[k] V[k]`. `j+1` collectives.
+  - `CGS`: batched — `Hj[0..j] = V[0..j]^H w` with one MPI GlobalSum over `j+1` dot products; then `w -= sum_k Hj[k] V[k]`.
+  - `CGS2`: CGS followed by one refinement pass, accumulating into `Hj`.
+- (d) `Hj[j+1] = ||w||_2` (MPI-collective); `w /= Hj[j+1]`. This finalizes column `j` of `H`.
+- (e) **Apply previous rotations to new column**: for `k=0..j-1`: `ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k])`.
+  - Real: `(dx,dy) ← (cs*dx + sn*dy, -sn*dx + cs*dy)`.
+  - Complex: `(dx,dy) ← (cs*dx + sn*dy, -conj(sn)*dx + cs*dy)`.
+- (f) **Generate new rotation** zeroing subdiagonal: `GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])` (LAPACK `lartg`-style, scaled to avoid over/underflow).
+- (g) **Apply new rotation** to `Hj[j..j+1]` and to `s[j..j+1]`. Now `Hj[j+1] = 0` (triangularized) and `|s[j+1]|` = current minimum-residual norm. Set `beta = |s[j+1]|`.
+- (h) Increment `it`.
+- (i) **Inner termination check**: `converged := (beta < eps)`; break if `converged OR j+1 == max_dim OR it == max_it`.
+- Citations: `palace/linalg/iterative.cpp:227–326, 562–611, 653–683`; `palace/linalg/orthog.hpp:41–88`.
+
+### Mutation: solution reconstruction (on inner-loop exit)
+
+- **Pattern**: accumulator (back-substitution + linear combination).
+- Let `j_final` be the index at break. Solve `R y = s` in place, where `R` is the upper-triangular part of `H[0..j_final+1, 0..j_final]`:
+  ```
+  for i = j_final down to 0:
+      s[i] /= H[i,i]
+      for k = 0 .. i-1:
+          s[k] -= H[k,i] * s[i]
+  ```
+- Basis combination:
+  - `LEFT` or `NONE`: `x += sum_{k=0..j_final} s[k] * V[k]`.
+  - `RIGHT` (GMRES): `r = sum_{k=0..j_final} s[k] * V[k]`; `V[0] = B r` (scratch reuse); `x += V[0]`.
+  - `RIGHT` (FGMRES): `x += sum_{k=0..j_final} s[k] * Z[k]` — direct, no second `B` apply.
+- Citations: `palace/linalg/iterative.cpp:613–651, 734–866`.
+
+### FGMRES delta from GMRES
+
+- Adds second basis `Z` of size `max_dim+1`, allocated alongside `V` in `Initialize`/`Update`.
+- Forces `pc_side = RIGHT`.
+- Arnoldi step (b) saves `Z[j] = B V[j]` (not discarded as scratch).
+- Initial residual uses `Z[0]` as buffer.
+- Solution reconstruction sums `s[k] Z[k]` directly into `x` (rationale: with a variable preconditioner, the basis for `A B` would not be recoverable by reapplying `B` to `V`).
+- Citations: `palace/linalg/iterative.cpp:734–866, 877–880`.
+
+### Type instantiation
+
+- `GmresSolver<OperType>`, `FgmresSolver<OperType>` explicitly instantiated for `OperType ∈ {Operator, ComplexOperator}`.
+- `ScalarType = double` or `std::complex<double>` via `IterativeSolver` typedef; `RealType = double` (so `cs` is always real, `sn` follows `ScalarType`).
+- Complex specialization touches: `GeneratePlaneRotation`/`ApplyPlaneRotation` (conjugation in `dy` update); `InnerProductHelper` (Hermitian inner product, order-sensitive).
+
+### Open questions (deferred)
+
+- No dedicated unit test for `GmresSolver`/`FgmresSolver` under `test/unit/`; restart/Givens/back-sub paths covered only implicitly via `test-romoperator.cpp` configured-KSP path.
+- `Update` clamp behavior at `j+1+add_size > max_dim`: `needed_cols` clamps to `max_dim` while loop writes column `j ≤ max_dim-1`; likely safe by the `j+1==max_dim` break but un-audited.
.
- Structural change: applied diff (117 lines); 0 rotation_claim(s).
## 2026-05-24 cycle-1 — forward cg_solver_integration [L0→L1] — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The slice mixes three distinct concerns at L1: (a) top-level ProblemType dispatch to BaseSolver subclasses, (b) IoData DEFAULT→CG resolution, (c) ConfigureKrylovSolver/BaseKspSolver composition. The fact that the middle link (driver Solve() → BaseKspSolver construction) is unverified and left as an open question suggests this slice is trying to span too much. The 'end-to-end linkage' diagram has a '(per driver) constructs BaseKspSolver' step that is hand-waved..
- Structural change: none.
