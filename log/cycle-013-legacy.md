## 2026-05-24 cycle-13 — forward gmres [L0→L1] — pass

- Synthesis: 4 rotation_claim(s); diff applied
- Verdict: pass.
- Friction: diff-apply failed: git apply failed:
STDERR:
error: corrupt patch at line 159

DIFF:
--- /dev/null
+++ b/book/src/spec/slices/gmres.md
@@ -0,0 +1,212 @@
+# Slice: gmres
+
+Scope: GMRES and FGMRES iterative linear solvers (palace/linalg/iterative.{hpp,cpp}).
+Covers the restarted Arnoldi process with Givens-rotation-maintained least-squares
+residual, the three Gram-Schmidt orthogonalization variants (MGS, CGS, CGS2), and
+the GMRES/FGMRES split (fixed vs. variable preconditioner).
+
+## L0 citations
+
+- `palace/linalg/iterative.hpp:152-216` — `GmresSolver<OperType>` declaration
+- `palace/linalg/iterative.hpp:219-275` — `FgmresSolver<OperType>` declaration
+- `palace/linalg/iterative.cpp:227-241` — `GeneratePlaneRotation` (real / complex)
+- `palace/linalg/iterative.cpp:243-250` — `ApplyPlaneRotation`
+- `palace/linalg/iterative.cpp:252-283` — `InitialResidual`
+- `palace/linalg/iterative.cpp:285-303` — `ApplyBA`
+- `palace/linalg/iterative.cpp:305-325` — `OrthogonalizeIteration` (dispatch over MGS/CGS/CGS2)
+- `palace/linalg/iterative.cpp:489-518` — `GmresSolver::Initialize`
+- `palace/linalg/iterative.cpp:519-542` — `GmresSolver::Update`
+- `palace/linalg/iterative.cpp:544-706` — `GmresSolver::Mult`
+- `palace/linalg/iterative.cpp:708-731` — `FgmresSolver::Update`
+- `palace/linalg/iterative.cpp:733-870` — `FgmresSolver::Mult`
+- `palace/linalg/iterative.cpp:73-108` — `CheckDot` / norm reductions reused throughout
+- `palace/linalg/orthog.hpp:41-89` — Gram-Schmidt kernel called by `OrthogonalizeIteration`
+- `test/unit/test-orthog.cpp:75-103` — orthogonality invariant tested across MGS/CGS/CGS2
+
+## L1 form
+
+### State schema
+
+The solver's persistent configuration is
+
+    GmresState = {
+      max_dim   : Nat,                          -- restart length
+      gs_orthog : {MGS, CGS, CGS2},
+      pc_side   : {LEFT, RIGHT},                -- FGMRES fixes this to RIGHT
+      basis     : KrylovBasis                   -- (see concepts/krylov-basis.md)
+    }
+
+The `basis` bundle is the Synthesizer-introduced abstraction that packs the
+Arnoldi basis V, the upper-Hessenberg matrix H (column-major, leading dim
+max_dim+1), and the Givens-rotation least-squares state (s, cs, sn). FGMRES
+extends the bundle with a second basis Z storing preconditioned vectors:
+
+    FgmresState = GmresState with {
+      pc_side  := RIGHT,                        -- structurally fixed
+      basis_pc : KrylovBasis                    -- Z[k] = B_k · V[k]
+    }
+
+All entries of `basis` and `basis_pc` are ephemeral workspace: they are
+resized lazily by Initialize/Update and not part of the mathematical
+invariant.
+
+### Mathematical invariant
+
+After m Arnoldi steps from initial residual r₀ = M(b − A·x₀) (where M is the
+identity, left-preconditioner B, or right-preconditioner action encoded via
+the constructed preconditioned-operator — see L1 procedure below), the basis
+satisfies
+
+    Â · V_m  =  V_{m+1} · H̄_m,                  V_{m+1}^* · V_{m+1} = I,
+
+where Â is the preconditioned operator (the role played by `apply_op` below;
+the specific composition is a constructed-operator detail — see
+concepts/constructed-operators.md) and H̄_m is (m+1)×m upper-Hessenberg. The
+approximate solution at step m minimises the preconditioned residual norm
+over the affine Krylov subspace x₀ + V_m · ℝ^m; the minimisation reduces to
+a small (m+1)×m least-squares problem on H̄_m whose running solution is
+maintained incrementally in (s, cs, sn).
+
+### L1 procedure (uniform across GMRES and FGMRES)
+
+The variant axis (fixed vs. flexible preconditioner) is absorbed via
+constructed operators at solve start (concepts/constructed-operators.md):
+the caller binds `apply_op` and a `record_pc(j, v)` hook from the
+preconditioner-side configuration; the per-step procedure is then identical.
+
+    solve(A, B, b, x₀, cfg) :=
+      let (apply_op, residual_in, record_pc, reconstruct) =
+            build_preconditioned_ops(A, B, cfg.pc_side, cfg.variant)
+      in  outer_loop (x₀, it=0, restart=0)
+
+    outer_loop (x, it, restart) :=
+      let r        = residual_in(b, x, restart, cfg.initial_guess)
+      let beta     = norm(r)
+      let eps      = convergence_threshold(beta, b, B, cfg, restart, it)
+      if  beta < eps  then  return (x, converged=true, it)
+      let basis    = basis_with_first(r / beta, beta)
+      let (basis', j, converged) = inner_loop(basis, apply_op, record_pc, it, eps, cfg)
+      let x'       = reconstruct(x, basis', j)
+      if converged ∨ it+j+1 ≥ cfg.max_it  then  return (x', converged, it+j+1)
+      else  outer_loop (x', it+j+1, restart+1)
+
+    inner_loop (basis, apply_op, record_pc, it, eps, cfg) :=
+      iterate j = 0,1,2,... until termination:
+        let w           = apply_op(basis.V[j])         -- record_pc(j, ·) fires inside
+        let (basis_w, hcol) =
+              orthogonalize(cfg.gs_orthog, basis.V[0..j], w)
+        let h_norm      = norm(basis_w)
+        let v_next      = basis_w / h_norm
+        let basis'      = basis.append_column(v_next, hcol, h_norm)
+        let basis''     = basis'.update_least_squares(j)   -- incremental update
+        let beta_j      = basis''.residual_estimate(j)
+        let converged   = beta_j < eps
+        terminate when converged ∨ j+1 = cfg.max_dim ∨ it+j+1 = cfg.max_it
+
+### Variant absorption
+
+Per concepts/variant-absorption.md, the axes are:
+
+- **pc_side ∈ {LEFT, RIGHT, none}** × **flexible? ∈ {no (GMRES), yes (FGMRES)}**.
+  Absorbed via *constructed operators* (concepts/constructed-operators.md):
+  `build_preconditioned_ops` returns the tuple
+  (apply_op, residual_in, record_pc, reconstruct) wired for the active
+  combination.
+    - GMRES/none      : apply_op = A;        record_pc = noop; reconstruct = x + Σ s_k V_k
+    - GMRES/LEFT      : apply_op = B∘A;      record_pc = noop; reconstruct = x + Σ s_k V_k
+    - GMRES/RIGHT     : apply_op = A∘B;      record_pc = noop; reconstruct = x + B·(Σ s_k V_k)
+    - FGMRES (RIGHT,flex): apply_op = A∘B_j; record_pc = store B_j·V[j] in Z[j];
+                           reconstruct = x + Σ s_k Z_k
+  All four routes satisfy criteria (a), (b), (c) of variant-absorption.md:
+  the L1 invariant is uniform, the procedure mentions pc_side only inside
+  `build_preconditioned_ops` (single dispatch site), and the per-step
+  primitive sequence is identical.
+- **gs_orthog ∈ {MGS, CGS, CGS2}**. Absorbed *parametrically* — passed to
+  `orthogonalize`, which returns the same shape (hcol of length j+1, w
+  with the projection removed). The choice affects only the inner
+  primitive sequence of `orthogonalize` (a single MPI-reduce vs. two
+  reduces), not the GMRES procedure.
+- **restart vs. full**. Absorbed via the outer/inner split. A non-restarted
+  run is the special case max_dim ≥ max_it; the outer loop terminates after
+  one pass either way.
+- **initial_guess ∈ {true, false}**. Absorbed inside `residual_in`, which
+  takes `cfg.initial_guess` and the restart index and returns r;
+  downstream code does not re-inspect the flag.
+
+### Termination and outputs
+
+Outputs are (x_out, converged, iteration_count, final_residual_estimate).
+The least-squares state inside `basis` provides the cheap residual estimate
+|s_{j+1}| without an explicit matvec.
+
+### Open questions
+
+- No direct unit test for GmresSolver / FgmresSolver under test/unit/;
+  only configuration-level coverage via test-romoperator.cpp. (low)
+- max_dim defaults to max_it; potentially O(max_it²) memory for the V
+  basis when only max_it is set. Latent footgun or intentional? (low)
+- FgmresSolver inherits pc_side from GmresSolver and then asserts RIGHT;
+  the field is structurally dead. The L1 state schema above already
+  removes it from FgmresState. (medium — schema-level question, not
+  blocking the L1 form)
+- Forward to L2: the *incremental least-squares update* role named in
+  `inner_loop.update_least_squares(j)` is implemented at L2 via a Givens
+  QR maintained against the new Hessenberg column. That mechanism is
+  hidden from L1.
.
- Structural change: applied diff (158 lines); 4 rotation_claim(s).
