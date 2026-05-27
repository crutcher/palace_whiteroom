# L1 — Mutation-lifted forms

Source operations re-expressed as pure functions: explicit input set, output set; in-place mutation and aliasing patterns either erased (workspace/scratch buffers) or made explicit (semantically-meaningful aliasing). The **mutation rotation** layer.

## Context

L1 is the closest pure-functional layer to the source. Structure follows the source loop; what changes is:

- **In-place vector updates → fresh-value updates.** `y.Add(α, x)` and `y.AXPBY(α, x, β)` (mutating member methods) become `y_new = axpy(α, x, y_old)` and `y_new = axpby(α, x, β, y_old)`. The L0 destination buffer disappears from the signature; the L1>L0 lowering reintroduces it.
- **Receiver-vs-argument asymmetry → first-class conjugation argument.** `ComplexVector::Dot` is a method on `*this`, making the receiver the linear argument and the call argument the conjugated one. At L1 the method-form / free-function-form distinction is erased: `dot` is sesquilinear in fixed argument order (first argument conjugated).
- **Operator-application mutation → pure operator-as-function.** `A.Mult(x, y)` (writes into `y`) → `y = A·x` (no destination buffer mention). Pattern recurs in `apply_BA`, residuals, and B-weighted norms.
- **Pinned reduction tree → reduction as a single semantic step.** L0 `dot` and `nrm2` are layered as `Hypre per-rank kernel + MPI_Allreduce`; L1 names the reduction as one step and records floating-point reduction-tree non-associativity as a **load-bearing** algebraic claim (per `CLAUDE.md` "Optimization tricks vs. base algebra"), not as separate operators.
- **Iterative loop mutating iterate in place → functional unfold** `state_{k+1} = step(state_k)`. Workspace `tmp` is omitted (the COW backend handles allocation).
- **Construction-bound solver state → opaque type at the L1 surface.** `BaseKspSolver<OperType>::Mult(b, x)` (writes into `x`, dispatches through owned `IterativeSolver` + `Solver` `unique_ptr`s, mutates statistics counters, logs convergence warnings) becomes `(x, status) = ksp_solve(K, b)` where `K : Solver[A]` is opaque about its internal Krylov method, per-method workspace, and preconditioner representation. Per-method enum dispatch (CG / GMRES / FGMRES) is variant-absorbed; cumulative counters lift to driver-side accumulation over per-call `SolveResult.iterations`.

## Semantics (overlay)

L1 vocabulary mirrors the source operations but with pure-functional binding. Four semantic motifs recur across the firm operators:

1. **Element-wise pure update** (`axpy`, `axpby`) — element-local, reduction-free, every output element depends on exactly one input element from each tensor argument. Algebraic laws are linear-combination facts; constant-folding branches at L0 (e.g., `axpy`'s `α == 1.0` fast path) are transparent performance tricks that disappear at L1.
2. **Mutation-free reduction** (`dot`, `nrm2`) — reduction over the length axis to a scalar. Reduction-tree non-associativity is load-bearing and recorded as an explicit non-law; the MPI collective is folded into the L1>L0 lowering, not the L1 signature.
3. **Subsumption-as-identity rather than dependency** — when one operator is a specialisation of another (`axpy(α, x, y) = axpby(α, x, 1, y)`), both stay in the L1 dep-map as siblings; the relationship is captured by an algebraic law in the subsuming operator, not by a dep-map edge.
4. **Constructed-operator absorption** (`ksp_solve`) — the L1 form takes a structured opaque `Solver[A]` argument whose per-method body (CG / GMRES / FGMRES), preconditioner, tolerances, and iteration cap are bound at construction; the L1 signature is variant-free. Result is structured (`SolveResult` carries `x` + four solve-statistics fields) rather than the L0 in-place destination + side-effect logger + mutating counters. The L2 `krylov-step` operator is where the per-method body unfolds. The L1>L0 lowering — [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) (cycle-008) — is the first L1>L0 theme for a structured opaque primary argument. It decomposes into the firm sister-theme primitives ([`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md), [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md), [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md)) per-step plus four absorption rules (timer erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding) at the outer composition.

Shape contracts are declared at boundaries (per the bunsen `contracts::unpack_shape_contract!` style). Single-rank is in scope per `CLAUDE.md`; MPI collectives appear only in lowering themes.

## Vocabulary cohort

**Firm (8)** — element-wise updates, BLAS-1 reductions, the opaque-operator gate, and the constructed-operator solve gate:

- [`axpy`](./axpy.md) — vector-scalar fused update; canonical BLAS-1 leaf.
- [`dot`](./dot.md) — Hermitian inner-product reduction (real / complex; `tdot` for unconjugated bilinear).
- [`nrm2`](./nrm2.md) — Euclidean norm; defined as `√dot(x, x)`.
- [`axpby`](./axpby.md) — fused two-scalar two-vector update; subsumes `axpy` and pure-scaling as algebraic identities.
- [`scal`](./scal.md) — pure vector-scalar multiply; the fourth BLAS-1 floor primitive (sibling-subsumed by `axpby` β=0).
- [`apply_linop`](./apply_linop.md) — pure linear-operator application `y = A·x`; opaque-operator gate to the L2 `krylov-step` vocabulary.
- [`axpbypcz`](./axpbypcz.md) — fused three-scalar three-vector update; subsumes `axpby` (γ=0) and `axpy` (β=1, γ=0).
- [`ksp_solve`](./ksp_solve.md) — pure preconditioned Krylov solve `(x, status) = ksp_solve(K, b)`; constructed-operator gate. The first L1 operator whose primary argument is itself a structured value (`Solver[A]`) rather than a raw tensor or scalar.

**Rough-in (test-coverage-bounded)** — operators whose structural signature is well-anchored at L0 but whose algebraic-law confidence is reduced pending dedicated test coverage or expanded literature anchoring:

- [`eigsolve`](./eigsolve.md) — pure eigenmode solve `result = eigsolve(E, control)`; the second constructed-operator gate at L1, composing against `ksp_solve` for spectral-transformation modes. Rough-in status motivated by absence of a dedicated `test-eigensolver.cpp` (only indirect coverage via `test-boundarymodeoperator.cpp`'s three `ModeEigenSolver` cases, exercising the linear path with `LARGEST_REAL` only). Promotion to firm gated on either expanded test coverage or additional literature anchoring (Higham 2008, Lehoucq-Sorensen, Hernandez-Roman-Vidal, Jarlebring-Koskela-Mele).
- [`matrix-weighted-norm`](./matrix-weighted-norm.md) — pure operator-weighted Euclidean norm `‖x‖_B = √(xᴴ B x)` for SPD `B`; the energy-norm primitive at L1; the M-orthonormalisation norm in the generalised eigenvalue problem. Rough-in status motivated by absence of dedicated test coverage on the SPD-weighted `linalg::Norml2(comm, x, B, Bx)` overload (`test/unit/test-vector.cpp` covers only the unweighted method form). Promotion to firm gated on (a) dedicated test coverage, (b) indirect coverage via eigensolver test outputs, or (c) algebraic-law completeness verification.
- [`bilinear-form`](./bilinear-form.md) — pure matrix-weighted inner product `xᴴ M y` for arbitrary linear `M` (no SPD requirement); the matrix-weighted generalisation of [`dot`](./dot.md) (the `M = I` special case). Rough-in status motivated by narrow variant-axis coverage in Palace's two surfaced use sites (Poynting-power boundary integral with Hermitian `Bttr` at `palace/models/boundarymodeoperator.cpp:85`; non-Hermitian cross-coupling `Atn` at line 90) — the M-symmetry-property axis has two witnesses but the Cauchy–Schwarz tight case at `y = x` with non-SPD `M` is unexercised, and the real-`x`/real-`y` element-type case is not surfaced by Palace. Promotion to firm gated on either (a) expanded direct test coverage on the matrix-weighted `linalg::Dot(comm, x, A, y)` overloads, or (b) literature-anchored evidence at firm-equivalent confidence.

**Rough-in (obstruction)** — speculative L1 operators emitted by `L1>L0` obstruction themes (no Palace L0 anchor; harvester promotion gated on appearance of an anchor):

- `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min` — from [`minres-iteration`](../L1-L0/minres-iteration.md) theme.
- `bicgstab_step`, `omega_update`, `stabilisation_update` — from [`bicgstab-iteration`](../L1-L0/bicgstab-iteration.md) theme.

**Queued (open questions)** — small primitives that bottom-out remaining L0 patterns referenced by the firm cohort:

- (empty as of cycle-010) — the cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` is now `partially-answered`: both halves landed in cycle-010 wave-1 as rough-ins ([`matrix-weighted-norm`](./matrix-weighted-norm.md) and [`bilinear-form`](./bilinear-form.md)). The `SpectralNorm` (power-iteration) sibling and the L1>L0 lowering theme for both operators remain tracked under that OQ's residuals.

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |
| [`nrm2`](./nrm2.md) | `(x) → √⟨x,x⟩` | `dot` | `firm` |
| [`axpby`](./axpby.md) | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `firm` |
| [`scal`](./scal.md) | `(α, x) → α·x` | (leaf; subsumed by `axpby` via β=0) | `firm` |
| [`apply_linop`](./apply_linop.md) | `(A: LinearOperator[M, N], x: Tensor[N]) → Tensor[M]` | (leaf; opaque operator) | `firm` |
| [`axpbypcz`](./axpbypcz.md) | `(α, x, β, y, γ, z) → α·x + β·y + γ·z` | (leaf; subsumes `axpby` and `axpy`) | `firm` |
| [`ksp_solve`](./ksp_solve.md) | `(K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) → SolveResult[N]` | `apply_linop` (direct); `dot`, `nrm2`, `axpy` (transitive via per-method body) | `firm` (L1>L0: [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md), cycle-008) |
| [`eigsolve`](./eigsolve.md) | `(E: EigSolver[problem], control: EigControl) → EigResult[N, K_max]` | `ksp_solve` (direct, inner linear solver); `apply_linop` (direct, per-step matrix-vector); `dot`, `nrm2`, `axpy`, `axpby` (transitive via per-orchestration body) | `rough-in (test-coverage-bounded, harvested-by: harvester:2026-05-27T191929Z-harvester-eigsolve-L1)` |
| [`matrix-weighted-norm`](./matrix-weighted-norm.md) | `(x: Tensor[N], B: LinearOperator[N, N]) → Scalar` (real-valued, SPD `B` required for norm) | `dot`, `apply_linop` | `rough-in (test-coverage-bounded, harvested-by: harvester:2026-05-27T215334Z-harvester-matrix-weighted-norm-l1)` |
| [`bilinear-form`](./bilinear-form.md) | `(x: Tensor[M], M: LinearOperator[M, N], y: Tensor[N]) → Scalar` (i.e. `xᴴ M y`) | `apply_linop`, `dot` | `rough-in (lower-layer-shared-vocabulary, harvested-by: harvester:2026-05-27T215427Z-harvester-bilinear-form-l1)` |
| [`lanczos_step`](../L1-L0/minres-iteration.md) | `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` | `apply_linop`, `dot`, `axpy`, `nrm2` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0)` |
| [`three_term_recurrence_update`](../L1-L0/minres-iteration.md) | `(alpha_curr, beta_prev, beta_curr) → BandColumn3` | (leaf) | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0)` |
| [`givens_apply_with_residual_min`](../L1-L0/minres-iteration.md) | `(qr_state, BandColumn3) → (qr_state', s_residual)` | `givens` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0)` |
| [`bicgstab_step`](../L1-L0/bicgstab-iteration.md) | `(A, M, r̂₀, state) → state'` (state ≡ `(x, r, p, v, ρ_prev, α_prev, ω_prev)`) | `axpy, axpby, dot, apply_linop` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-BiCGStab-L1-L0)` |
| [`omega_update`](../L1-L0/bicgstab-iteration.md) | `(t, r) → ⟨t,r⟩/⟨t,t⟩` | `dot` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-BiCGStab-L1-L0)` |
| [`stabilisation_update`](../L1-L0/bicgstab-iteration.md) | `(t, r, ẑ, h) → (x_new, r_new, ω)` | `omega_update, axpy` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-BiCGStab-L1-L0)` |

## Working Notes

- The dep-map records **L1-internal** dependencies only. Subsumption chains (`axpy ≺ axpby ≺ axpbypcz`) are stated as algebraic laws in the subsuming operator's entry, not as dep-map edges — both operators stay as siblings in the table.
- Aliasing-aware patterns where aliasing is semantically meaningful (not just buffer reuse) are first-class L1 content; transparent buffer reuse is an L1>L0 lowering concern.
- MPI single-rank scope (per `CLAUDE.md` "Scope") applies uniformly across L1 reductions: the L1 signature never includes a communicator; the L1>L0 lowering reintroduces `MPI_Allreduce` and records bit-deterministic-reduction-order trade-offs.
- Constant-folding fast paths at L0 (e.g., `axpy`'s `α == 1.0` branch, `dot`'s self-dot `&x == &y` branch) are classified as transparent performance tricks and erased at L1 — but only after the critic confirms they are algebraically equivalent to the unfolded form. Load-bearing numerical tricks (the pinned reduction tree) are preserved as explicit non-laws.
- The MINRES / BiCGStab rough-in operators above are emitted by **obstruction** L1>L0 themes — Palace has no L0 realisation (the `KrylovSolver::MINRES` and `KrylovSolver::BICGSTAB` enum cases route to `MFEM_ABORT` at `palace/linalg/ksp.cpp:53-57`). Harvester should not attempt promotion until either (a) Palace gains the implementation or (b) the L0 scope is widened to include vendored MFEM (see open question `bicgstab-mfem-reanchor-policy`).
- `ksp_solve` is the **first firm L1 operator whose primary argument is a structured opaque value** (`Solver[A]`) rather than a raw tensor or scalar. The construction of `Solver[A]` is the [`constructed-operator-factory`](../concepts/constructed-operator-factory.md) concept; the per-method axis collapse is [`variant-absorption`](../concepts/variant-absorption.md); the L0 anchor is [`L0/kspsolver-base-class`](../L0/kspsolver-base-class.md). The variant-axis collapse covers the **implemented** three (`CG`, `GMRES`, `FGMRES`) only; the three aborting enum cases (`MINRES`, `BICGSTAB`, `DEFAULT`) are out-of-scope per CLAUDE.md "Unimplemented Palace stub policy" and remain documented as L1>L0 obstruction themes.
- **Cycle-008**: the L1>L0 mutation-rotation theme for `ksp_solve` landed at [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) — the first L1>L0 theme whose LHS takes a structured opaque primary argument (`Solver[A]`). The theme decomposes into the firm sister themes per-step ([`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md), [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md), [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md)) plus four outer-composition absorption rules (timer erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding). The "Constructed-operator absorption" motif registered cycle-007 with the `ksp_solve` L1 firming now has the closing-the-loop L1>L0 anchor.
- **Cycle-009**: the `eigsolve` rough-in lands as the **second constructed-operator gate at L1**, composing against `ksp_solve` (the inner linear solver is itself a constructed-operator absorption). Per the cycle-008 OQ `eigsolve-l1-operator-rough-in-candidate` and the pre-check verdict (no dedicated `test-eigensolver.cpp`; narrow indirect coverage via `test-boundarymodeoperator.cpp` only), status is rough-in pending either expanded test coverage or additional literature anchoring. The rough-in introduces the **partial-convergence** semantic (`PartialConverged` status) as a distinguishing feature relative to `ksp_solve`'s soft-fail — the eigenvalue iteration can converge `0 < K < K_max` pairs without being an outright failure, a case `ksp_solve` has no analog for.
