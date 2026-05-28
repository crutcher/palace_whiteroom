## 2026-05-24 cycle-16 — forward orthog [L0→L1] — revise

- Synthesis: orthog L0→L1 refinement: corrected miscited 'SLEPc wrapper' to the ROM/PROM `romoperator.cpp:49-68` dispatch, disclosed the two-wrapper structure (GMRES uses m=j+1, ROM uses m=j) as caller-index convention not primitive divergence, added per-variant m==0 micro-difference as L2-level residual, refined citation ranges per Explorer verification.
- Verdict: revise.
- Friction: slice_write diff failed for book/src/spec/slices/orthog.md: git apply failed:
STDERR:
error: corrupt patch at line 78

DIFF:
--- a/book/src/spec/slices/orthog.md
+++ b/book/src/spec/slices/orthog.md
@@ -49,12 +49,17 @@
 - **Inner-product weighting (`InnerProductW` template hook).** Absorbed as the `dot_op`
   argument. Default is the unweighted local dot; callers (e.g. weighted GMRES) pass a
   custom local inner product. The contract — `dot_op` is *local*, routine owns reduction —
   is uniform across variants.
 
 **Residual axes (disclosed, not absorbed at L1).**
 
 - MPI collective shape differs by variant (MGS: m reductions of size 1; CGS: 1 reduction
   of size m; CGS2: 2 reductions of size m). This is a performance axis surfaced at L2,
   not an L1 semantic difference. MPI structure is out of scope for this project per
   CLAUDE.md; recorded here as a cost annotation only.
+- Empty-basis (m==0) handling differs textually per variant (CGS has explicit early
+  return; MGS relies on the loop body never executing). Both satisfy the L1 contract
+  (w unchanged, H empty); the difference is a micro-implementation detail at L2, not
+  an L1 distinction.
 - Normalization of `w'` is **not** part of this primitive; callers normalize. Header TODO
   notes this asymmetry; we preserve current convention.
 
 **State / mutation pattern.** `H` is written (CGS2 accumulates across two passes; MGS/CGS
 write once). `w` is updated in place (MGS: m sequential rank-1 updates; CGS: one batched
 update from saved `H`; CGS2: two batched updates). `V_basis` is read-only throughout.
 
-**Caller interface.** GMRES/FGMRES use a single dispatch helper
-`OrthogonalizeIteration(type, comm, V, w, Hj, j)` that forwards to this primitive with
-`m = j+1`. The Arnoldi step calls it uniformly regardless of variant; the variant lives
-as a runtime field on the solver.
+**Caller interface.** Two independent dispatch wrappers forward to this primitive:
+
+- **GMRES/FGMRES path.** `OrthogonalizeIteration(type, comm, V, w, Hj, j)` in
+  `iterative.cpp` calls the primitive with `m = j+1` (orthogonalize new vector against
+  the leading `j+1` basis columns including the just-added one's predecessors). Uses
+  the default identity dot.
+- **ROM/PROM path.** `OrthogonalizeColumn(type, comm, V, w, Rj, j, dot_op)` in
+  `romoperator.cpp` calls the primitive with `m = j` and a caller-supplied weighted
+  `dot_op`. The `m = j` vs `m = j+1` difference is a caller-side index convention
+  (how many columns the caller has populated when invoking), not a primitive-level
+  difference; the primitive takes `m` directly.
+
+Both wrappers inspect `type` exactly once at the dispatch switch; the rest of the
+caller logic is uniform. The two wrappers are a structural duplication candidate
+(out of scope here).
 
 ### Citations
 
 - `palace/linalg/orthog.hpp:18-23` — header contract (input V normalized, output w not
   normalized, `dot_op` is local + routine owns reduction).
-- `palace/linalg/orthog.hpp:25-36` — MGS variant.
-- `palace/linalg/orthog.hpp:38-53` — CGS / CGS2 variant (toggled by `refine` flag).
-- `palace/linalg/orthog.hpp:55-89` — block / SLEPc-facing wrappers (same shape).
+- `palace/linalg/orthog.hpp:26-37` — `IdentityInnerProduct` default `dot_op` (LocalDot;
+  confirms local-then-reduce contract).
+- `palace/linalg/orthog.hpp:39-53` — `OrthogonalizeColumnMGS` (per-j single-element
+  reduce + rank-1 update).
+- `palace/linalg/orthog.hpp:55-87` — `OrthogonalizeColumnCGS` (single size-m reduce;
+  `refine=true` performs the second pass and accumulates `H += dH`).
 - `palace/utils/labels.hpp:163-170` — `enum Orthogonalization { MGS, CGS, CGS2 }`.
 - `palace/linalg/iterative.cpp:307-326` — `OrthogonalizeIteration` dispatch helper.
-- `test/unit/test-orthog.cpp:70-97`, `:123-160` — parametric tests over all three variants
-  + custom inner product, asserting the substitutable contract.
+- `palace/models/romoperator.cpp:49-68` — `OrthogonalizeColumn` (ROM/PROM dispatch
+  wrapper; forwards a caller-supplied weighted `dot_op`; `m = j`).
+- `palace/models/romoperator.cpp:224`, `:643` — PROM basis-extension call sites.
+- `test/unit/test-orthog.cpp:71-97` — variant-parametric test harness.
+- `test/unit/test-orthog.cpp:99-121` — m==0 early-exit (all variants leave w unchanged).
+- `test/unit/test-orthog.cpp:123-162` — real basis, ⟨w',V_i⟩ < 1e-12 across variants.
+- `test/unit/test-orthog.cpp:164-232` — multi-column orthogonality + preservation.
+- `test/unit/test-orthog.cpp:234-274` — complex case.
+- `test/unit/test-orthog.cpp:276-330` — custom `RealWeightedInnerProduct` exercises
+  the non-identity `dot_op` hook.
 
 ### Test linkage
 
 `test/unit/test-orthog.cpp` ↔ `palace/linalg/orthog.hpp` (new linkage; record in
 `scaffolding/test-linkages` when promoted). Tests confirm:
@@ -100,11 +119,14 @@
 CGS-instability stress cases (near-rank-deficient bases that distinguish CGS from CGS2
 numerically) are **not** covered by the unit tests; the variants are tested as
 substitutable, not as numerically distinguishable.
 
 ### Open questions
 
 - Lift normalization into the primitive's contract, or preserve the caller-normalizes
   convention? Header has a TODO; deferred.
 - Surface MPI collective shape as a formal cost annotation at L2 when that slice lands.
+- De-duplicate the two dispatch wrappers (`iterative.cpp::OrthogonalizeIteration` and
+  `romoperator.cpp::OrthogonalizeColumn`)? They differ only in (a) `dot_op` forwarding
+  and (b) caller index convention. Out of scope here; flagged for a future cycle.
 
 ## L1 → L2
 
 (Deferred to next cycle on this slice.)
; verdict auto-downgraded pass→revise: one or more writes did not land.
- Structural change: none.
