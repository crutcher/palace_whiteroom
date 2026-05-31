---
agent: cross-layer-cross-cutter
invoked_at: 2026-05-31T14:15:00Z
scope: L1↔L0 cross-cut — floquet-correction-operator-construction-variants
status: applied
integrated_at: 2026-05-31T18:01:20Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-035 D3 — applied (observation-only, no book changes) by integrator-per-report at 2026-05-31T16:45:00Z (staging row 3); housekept by integrator-finalize at 2026-05-31T18:01:20Z. Pure cross-layer-cross-cutter observation report — NO book/ proposed-changes block, NO artifact mutations applied (deliberately, per role-spec for observation reports). Clean MATCH negative finding on apply_linop dimension (FloquetCorrSolver::Mult :72-79 matches apply-linop-mutation-rotation sub-pattern A bit-for-bit; ::AddMult :80-85 matches sub-pattern D bit-for-bit; the existing apply-linop-overload-set.md:33 non-exhaustive caveat already accommodates constructed-operator-gate classes). OQ floquet-correction-operator-construction-variants NARROWED: apply_linop dimension RESOLVED on landing via negative finding; the L1-tier coverage gap split off as NEW plan candidate floquet-correction-l1-gate-harvest, MIGRATED to scaffolding/priorities.md Backlog (Medium fan-out, route harvester, third firm instance of nested-constructed-operator-gate, plan-tag nested-constructed-operator-gate-instance-3) by this finalize per the report's §Recommendation item 2. Critic 7/8 PASS + 1 WARNING (skill-uptake-survey telemetry-only, non-blocking, repairer marked unrepairable). Citecheck 44 ok / 2 failing (both MISS-hits are typo-style bare paths in OQ caveat #1 prose at line 129 lacking the palace/ prefix; same source sites correctly-prefixed elsewhere; report-internal only, ZERO build-artifact impact — non-blocking per role-spec). No book rebuild needed (zero book edits); finalize ran cargo make book exit 0 in 90.81s. Single commit covering all 3 cycle-035 reports + housekeeping.
---

# CYCLE: Cross-layer observation — floquet-correction-operator-construction-variants

## Summary

`FloquetCorrSolver` (`palace/linalg/floquetcorrection.hpp:33-60` + `.cpp:19-86`) is a constructed-operator gate of *exactly* the same shape as the firm `divfree-projector` L1 entry: a templated class with a `Mult(const VecType &x, VecType &y) const` and `AddMult(const VecType &x, VecType &y, ScalarType a) const` member-method surface, a `mutable VecType rhs` workspace, and a body that composes an inner `Cross->Mult(x, rhs)` linop-apply with an inner `ksp->Mult(rhs, y)` Krylov solve. The apply-shape surface is fully covered by the existing `apply-linop-mutation-rotation` sub-patterns (A `Mult`, D `AddMult`) AND the existing `nested-constructed-operator-gate` concept — there is NO new apply-shape variant in play. The observation is therefore a clean MATCH on the apply side (no `apply-linop-mutation-rotation` extension needed) combined with a clean L1 ROUGH-IN candidate (`floquet_correction`) routable as a third firm instance of the nested-constructed-operator-gate pattern (sibling to `divfree_project` and `eigsolve`). The motivating OQ resolves with the negative finding on `apply_linop` extension + a one-step routing decision to `harvester` (or `abstractor`-first if the L1 form's algebraic-law set is uncertain).

## Observation kind

**Vocabulary mismatch (negative)** — combined with a coverage-gap finding routed away from the originally-suspected target.

The OQ predicted a possible `apply_linop` coverage gap. The actual finding is the opposite: `apply_linop`'s overload-set absorption and the `apply-linop-mutation-rotation` sub-patterns A/D already absorb `FloquetCorrSolver`'s apply surface bit-for-bit. The coverage gap is at a *different* tier — there is no firm L1 `floquet_correction` operator and no L1>L0 `floquet-correction-mutation-rotation` theme — and that gap is a `harvester` candidate, not an `apply_linop` extension.

## Specific finding

### What kind of operator does `FloquetCorrSolver` build?

`FloquetCorrSolver` (`palace/linalg/floquetcorrection.hpp:33-60`) is a class-templated-on-`VecType` whose constructor (`palace/linalg/floquetcorrection.cpp:19-70`) builds **three closure-bound fields**:

- `M : unique_ptr<OperType>` — the Raviart–Thomas vector-FE mass operator on `rt_fespace`, assembled via `BilinearForm a(rt_fespace); a.AddDomainIntegrator<VectorFEMassIntegrator>(); m = a.Assemble(skip_zeros);` then wrapped in `ParOperator` (real) / `ComplexParOperator` (complex) (`palace/linalg/floquetcorrection.cpp:27-38`).
- `Cross : unique_ptr<OperType>` — the mixed-space *cross-product-with-Floquet-wave-vector* operator from `nd_fespace` (Nédélec) to `rt_fespace` (Raviart–Thomas), assembled via `BilinearForm a(nd_fespace, rt_fespace); a.AddDomainIntegrator<VectorFEMassIntegrator>(f);` with the per-material coefficient `f` carrying `mat_op.GetFloquetCross()` (`palace/linalg/floquetcorrection.cpp:40-57`). This is the matrix that *represents the action of the cross product* `[kp x]` per the header comment at `palace/linalg/floquetcorrection.hpp:54-56`.
- `ksp : unique_ptr<BaseKspSolver<OperType>>` — a CG solver with a JacobiSmoother preconditioner, bound to `M` as both operator and preconditioner target (`palace/linalg/floquetcorrection.cpp:59-67`).

Plus the workspace `mutable VecType rhs` (`palace/linalg/floquetcorrection.hpp:48`), sized once in the constructor (`palace/linalg/floquetcorrection.cpp:69-70`). This `mutable` member is already in the firm corpus of the [`mutable-workspace-pattern`](file://book/src/L0/mutable-workspace-pattern.md) page — `book/src/L0/mutable-workspace-pattern.md:80` and `:136` cite `palace/linalg/floquetcorrection.hpp:49` as a Category-3 (solver workspace) instance.

The class is template-instantiated **complex only** at `palace/linalg/floquetcorrection.cpp:88` (`template class FloquetCorrSolver<ComplexVector>;`) — no real-branch instantiation in the source tree. (The header still allows real templating, but Palace's three call sites in `palace/drivers/{eigensolver,drivensolver}.cpp` all instantiate `FloquetCorrSolver<ComplexVector>`.)

### What is the apply-time semantics?

The `Mult` body at `palace/linalg/floquetcorrection.cpp:72-77` is two lines:

```cpp
Cross->Mult(x, rhs);
ksp->Mult(rhs, y);
```

So mathematically `y = M⁻¹ · Cross · x = M⁻¹ · [kp ×] · x` — the Raviart–Thomas projection of the Floquet-wave-vector cross-product of the Nédélec input field. The `AddMult` body at `palace/linalg/floquetcorrection.cpp:79-85` is the standard fused-axpy accumulating form `y += a · Mult(x)` implemented as `this->Mult(x, rhs); rhs *= a; y += rhs;` — three primitive steps composing `apply_linop` (the `Mult` call) with a `scal` and an `axpy` on the existing `rhs` workspace.

### Does the apply surface match the existing `apply-linop-mutation-rotation` absorption?

**Yes — bit-for-bit on the apply side.** The `Mult` and `AddMult` signatures match:

- `void FloquetCorrSolver<VecType>::Mult(const VecType &x, VecType &y) const` — sub-pattern A of [`apply-linop-mutation-rotation`](file://book/src/L1-L0/apply-linop-mutation-rotation.md) (`book/src/L1-L0/apply-linop-mutation-rotation.md:43-81`).
- `void FloquetCorrSolver<VecType>::AddMult(const VecType &x, VecType &y, ScalarType a) const` — sub-pattern D (`book/src/L1-L0/apply-linop-mutation-rotation.md:127-172`).

The class does NOT expose `MultTranspose`, `MultHermitianTranspose`, `AddMultTranspose`, or `AddMultHermitianTranspose` — so sub-patterns B, C, E of `apply-linop-mutation-rotation` do not need to apply, and their absence is consistent with `FloquetCorrSolver` not being a polymorphic subclass of `ComplexOperator` (it is a standalone class that *exposes the same overload-set surface* — `Mult` / `AddMult` — but doesn't inherit from the operator hierarchy; the inheritance distinction is in the `## Concrete-subclass family` enumeration of [`apply-linop-overload-set`](file://book/src/L0/apply-linop-overload-set.md) `book/src/L0/apply-linop-overload-set.md:22-33`, which already names ~6 concrete subclasses and explicitly says "A non-exhaustive list. Other operator-shaped types in Palace (preconditioners under `palace/linalg/`, FE assembly closures under `palace/fem/`, Jacobian-action operators) all implement the same interface; the overload-set shape is uniform.").

`FloquetCorrSolver` is in the same boat as `DivFreeSolver` — neither is a subclass of `Operator` / `ComplexOperator`, but both expose the `Mult` / `AddMult` method shape and play the role of a constructed-operator gate at L1. The `apply-linop-overload-set` page's "non-exhaustive" caveat covers them; the firm `divfree-projector` L1 entry treats `DivFreeSolver::Mult` not as an `apply_linop` sub-pattern but as the *gate operator's* apply surface, and the same routing applies to `FloquetCorrSolver`.

### Is this an apply-shape variant `apply_linop` should mention?

**No.** The `apply_linop` L1 entry (`book/src/L1/apply_linop.md`) collapses the `Operator`/`ComplexOperator` virtual hierarchy's `Mult` family. `FloquetCorrSolver` exposes a `Mult` method but is NOT a member of that hierarchy — it is a separate constructed-operator class whose `Mult` happens to use the same C++ signature shape. The L1 contract for `apply_linop` is "apply an opaque `LinearOperator[M, N]` to a vector"; `FloquetCorrSolver`'s `Mult` is "apply the constructed Floquet-correction gate to its argument," which is a different L1 operator with a different signature (`floquet_correction :: (F: FloquetCorrector[N_nd, N_rt], x: Field[N_nd]) -> Field[N_rt]` vs `apply_linop :: (A: LinearOperator[M, N], x: Tensor[N]) -> Tensor[M]`). The same routing distinction is already in firm precedent at `book/src/L1/divfree-projector.md:25-37`: "`divfree_project` is a constructed-operator gate at L1, in the same family as `ksp_solve`, `eigsolve`, and `chebyshev-smoother`" — it is NOT modeled as an `apply_linop` instance.

Inside `FloquetCorrSolver::Mult` the two genuine L1-level operator applies are `Cross->Mult(x, rhs)` (a true `apply_linop` on the constructed Cross linop) and `ksp->Mult(rhs, y)` (a true `ksp_solve` gate-apply on the constructed CG-with-Jacobi solver). These two inner calls ARE already covered by the firm `apply-linop-mutation-rotation` (sub-pattern A) + the firm `ksp-solve-mutation-rotation` themes; the L1>L0 lowering of `floquet_correction` would chain those two existing themes the same way the `divfree-projector-mutation-rotation` theme does (which composes `WeakDiv->Mult` + `ksp->Mult` + `Grad->AddMult` — `book/src/L1-L0/divfree-projector-mutation-rotation.md:55-78`).

### Is this a coverage GAP, a clean MATCH, or a candidate for a NEW L1 operator?

**Two-part finding:**

1. **Clean MATCH at the `apply_linop` tier** (the originally-suspected target of the OQ). No extension to `apply-linop-mutation-rotation` or `apply-linop-overload-set` is needed; both already accommodate `FloquetCorrSolver`'s apply surface under their existing "non-exhaustive constructed-operator-shape" caveats. Record this as a NEGATIVE finding closing the apply-linop-extension dimension of the OQ.

2. **L1 coverage GAP for a new `floquet_correction` operator + new `L1-L0/floquet-correction-mutation-rotation` theme.** Routes to `harvester` (with `abstractor` pre-pass optional). The gate's structure is a clean parallel to `divfree-projector`:
   - **Closure type**: `FloquetCorrector[N_nd, N_rt]` carrying the closure fields `M : LinearOperator[N_rt, N_rt]` (RT mass), `Cross : LinearOperator[N_nd, N_rt]` (the matrix realization of `[kp ×]`), `ksp : Solver[M]` (the inner CG-with-Jacobi gate).
   - **L1 signature**: `floquet_correction :: (F: FloquetCorrector[N_nd, N_rt], x: Field[N_nd]) -> Field[N_rt]` with `floquet_correction(F, x) = F.M⁻¹ · F.Cross · x` (where the inverse is solve-to-tolerance via `F.ksp`).
   - **Family membership**: third firm instance of [`nested-constructed-operator-gate`](file://book/src/concepts/nested-constructed-operator-gate.md), sibling to `divfree-projector` (one nested gate) and `eigsolve` (two nested gates); like `divfree-projector`, it carries one nested gate (the inner `ksp`).
   - **Lowering theme**: sub-pattern A for `Mult` (the rectangular-domain projection-style apply: `Cross->Mult` → `ksp->Mult`), sub-pattern B for `AddMult` (the fused-accumulating form composing the Mult with `scal` and `axpy` on the `rhs` workspace). The two-line constructor + the two-line `Mult` + the three-line `AddMult` give a very compact theme — comparable in size to `back-solve-mutation-rotation`.
   - **Variant axes**: element-type (`VecType ∈ {Vector, ComplexVector}` in the template; only `ComplexVector` instantiated in the source tree — collapse or note as a deliberate-real-omission caveat). No transpose-mode variants exposed.

The new L1 operator's *fan-out* is bounded: **four AddMult call sites total** — three in `palace/drivers/drivensolver.cpp:212, 336, 468` and one in `palace/drivers/eigensolver.cpp:454` (grep-verified) — all of shape `floquet_corr->AddMult(E, B, 1.0 / omega)` adding the `kp × E` correction term to the B-field `B = -1/(iω) ∇ × E + 1/ω · kp × E` (cited at `palace/drivers/eigensolver.cpp:453` comment). All call sites match sub-pattern D of `apply-linop-mutation-rotation` exactly — same `AddMult(in, out, scalar)` shape, same accumulating-axpy semantics, same one-pass-with-fused-scal-axpy lowering.

## Recommendation

**Two-part recommendation:**

1. **Close the OQ `floquet-correction-operator-construction-variants` as RESOLVED (negative on the apply_linop dimension)** — the `apply-linop-mutation-rotation` lowering needs no extension; the `apply-linop-overload-set` non-exhaustive caveat already accommodates `FloquetCorrSolver`. Record the resolution with a link to this report.

2. **Migrate a new plan item `floquet-correction-l1-gate-harvest`** (NOT just an OQ — a plan candidate, per the CLAUDE.md "intake channels feed the plan, they don't hold work" invariant) routed to `harvester` for the new L1 `floquet_correction` operator + companion `L1-L0/floquet-correction-mutation-rotation` theme. Fan-out estimate: **low-to-medium** — 4 call sites; one new firm L1 leaf + one new firm L1-L0 theme; reuses the divfree-projector precedent verbatim; adds a third firm instance to the `nested-constructed-operator-gate` concept (currently 2 firm + 1 latent). Cost: **small** — the constructor + apply bodies are ~50 lines total; the divfree-projector theme is the template (~250 lines, but FloquetCorrSolver is simpler — no `bdr_eff` boundary set, no complex-vs-real branching needed since only ComplexVector is instantiated, no `Mult(VecType &y)` in-place form). Estimated cost roughly half of divfree-projector. The L1 entry's algebraic laws are straightforward (linearity in `x`; the cross product `[kp ×]` is itself linear; the L1 form is `(F.Cross is linear, F.M⁻¹ is linear-on-its-domain) → composition of two linear maps`).

   *Sub-recommendation:* the harvester should NOT be dispatched as `abstractor-first`. The construction site (`palace/linalg/floquetcorrection.cpp:19-70`) and the apply sites (`:72-86`) are both fully present in firm Palace source; there is no negative-anchor / `partly-constructive` concern. The divfree-projector L1 entry's `## Algebraic laws` block ports directly with minor edits (drop "projector idempotence" since `floquet_correction` is not idempotent; add a note that the Cross operator is the *discretized* cross product, not arbitrary — so `floquet_correction(F, kp ∥ x) = 0` when `x` is parallel to the wave vector at every quadrature point, a strict-linearity special case).

   *Routing*: append to `scaffolding/priorities.md` Backlog with rank ~Medium (more interesting than a pure axpy-corpus completion, less interesting than a brand-new layer / brand-new vocabulary). Plan-tag `nested-constructed-operator-gate-instance-3`.

## Supporting evidence

L0 (Palace source):
- `palace/linalg/floquetcorrection.hpp:30-32` — class-purpose comment: "the correction is the cross product of the Floquet wave vector with the electric field."
- `palace/linalg/floquetcorrection.hpp:33-34` — class template declaration: `template <typename VecType> class FloquetCorrSolver`.
- `palace/linalg/floquetcorrection.hpp:35-39` — `OperType` and `ScalarType` type aliases via `std::conditional` on `VecType`.
- `palace/linalg/floquetcorrection.hpp:41-48` — private members: `M, Cross : unique_ptr<OperType>`, `ksp : unique_ptr<BaseKspSolver<OperType>>`, `mutable VecType rhs`.
- `palace/linalg/floquetcorrection.hpp:51-52` — constructor signature: `(const MaterialOperator &mat_op, FiniteElementSpace &nd_fespace, FiniteElementSpace &rt_fespace, double tol, int max_it, int print)`.
- `palace/linalg/floquetcorrection.hpp:54-56` — `Mult` doc-comment: "compute the Raviart-Thomas space field y = [kp x] x, where [kp x] is a matrix representing the action of the cross product with the Floquet wave vector."
- `palace/linalg/floquetcorrection.hpp:57-59` — `Mult` + `AddMult` declarations.
- `palace/linalg/floquetcorrection.cpp:19-38` — constructor: builds `M` (RT mass via `BilinearForm a(rt_fespace); a.AddDomainIntegrator<VectorFEMassIntegrator>(); m = a.Assemble(skip_zeros);` and wraps in `ParOperator` / `ComplexParOperator`).
- `palace/linalg/floquetcorrection.cpp:40-57` — constructor: builds `Cross` (mixed-space ND→RT bilinear form with the per-material `GetFloquetCross()` coefficient, wraps in `ParOperator` / `ComplexParOperator`).
- `palace/linalg/floquetcorrection.cpp:59-67` — constructor: builds the inner `ksp` (`CgSolver` + `JacobiSmoother`, bound to `M` as both operator and preconditioner).
- `palace/linalg/floquetcorrection.cpp:69-70` — sets up the `rhs` workspace.
- `palace/linalg/floquetcorrection.cpp:72-77` — `Mult` body: `Cross->Mult(x, rhs); ksp->Mult(rhs, y);` — the two-step composition.
- `palace/linalg/floquetcorrection.cpp:79-85` — `AddMult` body: `this->Mult(x, rhs); rhs *= a; y += rhs;` — fused-accumulating form via three primitive steps.
- `palace/linalg/floquetcorrection.cpp:88` — `template class FloquetCorrSolver<ComplexVector>;` (sole template instantiation; no `<Vector>` instantiation).
- `palace/drivers/eigensolver.cpp:236-243` — Floquet-corr instantiation guarded by `space_op.GetMaterialOp().HasWaveVector()`.
- `palace/drivers/eigensolver.cpp:448-455` — Floquet-corr `AddMult(E, B, 1.0 / omega)` consumption site with the B-field comment `B = -1/(iω) ∇ × E + 1/ω · kp × E`.
- `palace/drivers/drivensolver.cpp:138-141, 289-292` — two `floquet_corr` *declaration / instantiation* sites in the driven-solver path (`std::unique_ptr<FloquetCorrSolver<ComplexVector>> floquet_corr;` + `floquet_corr = std::make_unique<...>` pairs).
- `palace/drivers/drivensolver.cpp:212, 336, 468` — three `floquet_corr->AddMult(E, B, 1.0 / omega)` *consumption* sites in the driven-solver path.

L1 / L0 artifact (the absorptions against which the negative finding is recorded):
- `book/src/L1/apply_linop.md:7` — names the absorbed overload-set family.
- `book/src/L1/apply_linop.md:83` — Variant axes: operator-representation collapse names "all preconditioners, all FE assembly closures, all Jacobian-action operators" via the non-exhaustive caveat.
- `book/src/L1-L0/apply-linop-mutation-rotation.md:43-81` — sub-pattern A (`Mult`); covers `FloquetCorrSolver::Mult`.
- `book/src/L1-L0/apply-linop-mutation-rotation.md:127-172` — sub-pattern D (`AddMult`); covers `FloquetCorrSolver::AddMult`.
- `book/src/L0/apply-linop-overload-set.md:33` — the non-exhaustive caveat: "A non-exhaustive list. Other operator-shaped types in Palace (preconditioners under `palace/linalg/`, FE assembly closures under `palace/fem/`, Jacobian-action operators) all implement the same interface; the overload-set shape is uniform."
- `book/src/L0/mutable-workspace-pattern.md:80, 136` — already cites `FloquetCorrSolver::rhs` as a Category-3 (solver workspace) instance.
- `book/src/L1/divfree-projector.md:25-37` — the firm-precedent constructed-operator-gate framing; the routing template for the proposed `floquet_correction` L1 entry.
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:52-148` — the structural template for the proposed `floquet-correction-mutation-rotation` theme.
- `book/src/concepts/nested-constructed-operator-gate.md:62-89` — the two firm instances (`eigsolve`, `divfree-projector`); the page that grows by one entry on harvester landing.
- `book/src/L1/jacobi-smoother.md:517` — already cites `palace/linalg/floquetcorrection.cpp:65` as a JacobiSmoother consumer site, validating the inner `ksp` construction recipe and reinforcing that the Floquet site is part of the established Palace-wide ksp/preconditioner consumption corpus.

Plan / OQ:
- `scaffolding/priorities.md:63` — the plan-side entry for this OQ.
- `scaffolding/open-questions.md:31` — the OQ index entry: `floquet-correction-operator-construction-variants → plan Backlog (Low)`.

## Open questions / caveats

1. **Element-type collapse vs. ComplexVector-only instantiation.** The class is *templated* on `VecType` but only `ComplexVector` is instantiated (`palace/linalg/floquetcorrection.cpp:88`). **Negative-anchor grep** (`grep -rn "FloquetCorrSolver" reference/palace/`, repairer-verified at META repair time): the only `FloquetCorrSolver<...>` instantiations anywhere in the source tree are five `FloquetCorrSolver<ComplexVector>` sites (the one explicit template instantiation at `floquetcorrection.cpp:88` + the two `unique_ptr<FloquetCorrSolver<ComplexVector>>` + two `make_unique<FloquetCorrSolver<ComplexVector>>` sites across `drivers/eigensolver.cpp:237,240` and `drivers/drivensolver.cpp:138,141,289,292`); no `<Vector>` (real) instantiation exists. The harvester landing the L1 entry must decide whether the L1 signature is polymorphic-over-element-type (matching the template) or complex-only (matching the instantiation). The `divfree-projector` L1 entry (`book/src/L1/divfree-projector.md:39-43`) handles a similar templated-but-both-instantiated class by treating the template polymorphism as a parametric variant absorbed at L1; the `floquet_correction` entry has one less template instantiation (no `<Vector>` instantiation in source) and a harvester audit should record the missing real instantiation as either (a) a deliberate scope-out (Palace's Floquet BC corpus is complex-only because Floquet phase factors are inherently complex — physical Floquet phase factors `e^{ik·r}` are complex by construction) or (b) a `rough-in (test-coverage-bounded)`-style status with the gating reason (no real-branch test, no real-branch source-witnessed use). The grep-confirmed absence of any real-branch site favors (a) — deliberate scope-out — but the harvester should make the final scoping call.

2. **`apply-linop-overload-set` enumeration upgrade (optional, low-priority).** The `## Concrete-subclass family` section at `book/src/L0/apply-linop-overload-set.md:22-33` could be extended to add a fourth bullet under "Other operator-shaped types in Palace" explicitly naming the *constructed-operator-gate* family (`DivFreeSolver`, `FloquetCorrSolver`, etc.) as a distinct stylistic category from the polymorphic `Operator`/`ComplexOperator` subclasses — *these expose the same overload-set surface but do not inherit from the operator hierarchy*. This is a vocabulary-precision nicety, not a coverage gap (the existing non-exhaustive caveat is correct as-is). Routing: a `same-layer-cross-cutter` could surface this if it accumulates with other constructed-operator-gate instances; not worth a dedicated dispatch on its own.

3. **L2 vocabulary opportunity.** The Floquet correction is a *post-processing* step: it modifies the B-field after the E-field solve. This is structurally distinct from the per-iteration role most L1 gates play (which are per-step components of an outer iteration). When L2 vocabulary lands, the question of whether `floquet_correction` is a unique L2 verb (`post-process-with-constructed-gate`) or just an `apply_linop` at the L2 tier (composing the inner solve into a single linear-map) is open. Not a blocker for the L1 harvester landing.

4. **MPI scope.** The class uses `rt_fespace.GetComm()` for the CG comm (`palace/linalg/floquetcorrection.cpp:59`) and the `Par*` wrappers (`palace/linalg/floquetcorrection.cpp:33, 36, 49, 53`). Per CLAUDE.md §Scope, `Par*` types read as single-rank equivalents; no MPI-specific concern blocks the harvester landing. (Flag-once-skip already covered by the divfree-projector precedent.)

5. **Audit-mode classification.** This report is a pure cross-layer cross-cut; no `book/` edits proposed. The negative-on-apply_linop finding + the routing-to-harvester recommendation are both DISPATCH-phase outputs that the parent-orchestrator and meta-phase can act on without integrator intervention. The cycle-planner for the harvester landing should weight against the existing batch's L1-vs-L2 priority allocation; if the current batch is L2-weighted, this harvester sits in the Backlog as a low-effort L1 fill-in for a future L1-weighted cycle. No urgent gate.
