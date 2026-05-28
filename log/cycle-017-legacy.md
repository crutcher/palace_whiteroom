## 2026-05-24 cycle-17 — forward divfree [L0→L1] — revise

- Synthesis: divfree L0→L1 consolidated: corrected Mult(x,y) mutation pattern from alias_with_input to pure (per 2026-05-24 lesson on out-of-place wrappers); confirmed WeakDiv sign convention from explorer citations; surfaced NLEPS-exposes-but-doesn't-use observation as open question.
- Verdict: revise.
- Friction: slice_write diff failed for book/src/spec/slices/divfree.md: git apply failed:
STDERR:
error: patch fragment without header at line 18: @@ -90,8 +90,15 @@

DIFF:
--- a/book/src/spec/slices/divfree.md
+++ b/book/src/spec/slices/divfree.md
@@ -56,9 +56,9 @@
 
 ### Mutation pattern
 
 - Single-argument `Mult(y)`: `in_place_overwrite` on `y`; `psi`, `rhs` are
   `scratch_buffer` members.
-- Two-argument `Mult(x, y)`: `alias_with_input` viewed as a pure function
-  `y = P x`; implemented as `y ← x; Mult(y)`. No aliasing between `x` and
-  `y` is assumed.
+- Two-argument `Mult(x, y)`: `pure` (function `y = P x`); implemented as
+  `y ← x; Mult(y)`. The wrapper does not assume or rely on aliasing
+  between `x` and `y` — it is copy-then-apply-in-place.
 
 ## Variant axes (absorption status)
 
@@ -90,8 +90,15 @@
 - Scope description attributes use to driven/transient solvers; only
   eigensolver-path callers are visible. Stale doc, or missing call site
   outside the inspected glob?
 - No direct unit test (`test-divfree.cpp` does not exist); coverage is
   indirect via `test/examples/`. A synthetic invariant check (post-Mult,
   `WeakDiv · y` is zero on non-essential dofs to ksp tolerance) would be
   the natural unit-test surface if one were added.
-- `WeakDiv` sign-convention claim (that `MixedVectorWeakDivergenceIntegrator`
-  encodes the negative-divergence sign, making `+Grad·ψ` the correction)
+- `WeakDiv` sign-convention claim (that `MixedVectorWeakDivergenceIntegrator`
+  encodes the negative-divergence sign, making `+Grad·ψ` the correction)
+  is confirmed: `PopulateCoefficientContext` is called with factor `-1.0`
+  at `mixedvecgrad.cpp:202`, and the integrator header comment at
+  `integrator.hpp:217` states `a(u,v) = -(Q u, grad v)`.
+- `NonLinearEigenvalueSolver` exposes `SetDivFreeProjector` and stores
+  `opProj` (`nleps.cpp:38-42`) but no `opProj->Mult` call site is visible
+  inside the NLEPS iteration in this revision. Either the projection
+  step is intentionally elided on the NLEPS path or the wire-up is
+  incomplete.
; verdict auto-downgraded pass→revise: one or more writes did not land.
- Structural change: none.
