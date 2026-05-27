# L1 — Mutation-lifted forms

Source operations re-expressed as pure functions: explicit input set, output set; in-place mutation and aliasing patterns either erased (workspace/scratch buffers) or made explicit (semantically-meaningful aliasing). The **mutation rotation** layer.

## Context

L1 is the closest pure-functional layer to the source. Structure follows the source loop; what changes is:

- **In-place vector updates → fresh-value updates.** `y.Add(α, x)` and `y.AXPBY(α, x, β)` (mutating member methods) become `y_new = axpy(α, x, y_old)` and `y_new = axpby(α, x, β, y_old)`. The L0 destination buffer disappears from the signature; the L1>L0 lowering reintroduces it.
- **Receiver-vs-argument asymmetry → first-class conjugation argument.** `ComplexVector::Dot` is a method on `*this`, making the receiver the linear argument and the call argument the conjugated one. At L1 the method-form / free-function-form distinction is erased: `dot` is sesquilinear in fixed argument order (first argument conjugated).
- **Operator-application mutation → pure operator-as-function.** `A.Mult(x, y)` (writes into `y`) → `y = A·x` (no destination buffer mention). Pattern recurs in `apply_BA`, residuals, and B-weighted norms.
- **Pinned reduction tree → reduction as a single semantic step.** L0 `dot` and `nrm2` are layered as `Hypre per-rank kernel + MPI_Allreduce`; L1 names the reduction as one step and records floating-point reduction-tree non-associativity as a **load-bearing** algebraic claim (per `CLAUDE.md` "Optimization tricks vs. base algebra"), not as separate operators.
- **Iterative loop mutating iterate in place → functional unfold** `state_{k+1} = step(state_k)`. Workspace `tmp` is omitted (the COW backend handles allocation).

## Semantics (overlay)

L1 vocabulary mirrors the source operations but with pure-functional binding. Three semantic motifs recur across the firm operators:

1. **Element-wise pure update** (`axpy`, `axpby`) — element-local, reduction-free, every output element depends on exactly one input element from each tensor argument. Algebraic laws are linear-combination facts; constant-folding branches at L0 (e.g., `axpy`'s `α == 1.0` fast path) are transparent performance tricks that disappear at L1.
2. **Mutation-free reduction** (`dot`, `nrm2`) — reduction over the length axis to a scalar. Reduction-tree non-associativity is load-bearing and recorded as an explicit non-law; the MPI collective is folded into the L1>L0 lowering, not the L1 signature.
3. **Subsumption-as-identity rather than dependency** — when one operator is a specialisation of another (`axpy(α, x, y) = axpby(α, x, 1, y)`), both stay in the L1 dep-map as siblings; the relationship is captured by an algebraic law in the subsuming operator, not by a dep-map edge.

Shape contracts are declared at boundaries (per the bunsen `contracts::unpack_shape_contract!` style). Single-rank is in scope per `CLAUDE.md`; MPI collectives appear only in lowering themes.

## Vocabulary cohort

**Firm (7)** — element-wise updates, BLAS-1 reductions, and the opaque-operator gate:

- [`axpy`](./axpy.md) — vector-scalar fused update; canonical BLAS-1 leaf.
- [`dot`](./dot.md) — Hermitian inner-product reduction (real / complex; `tdot` for unconjugated bilinear).
- [`nrm2`](./nrm2.md) — Euclidean norm; defined as `√dot(x, x)`.
- [`axpby`](./axpby.md) — fused two-scalar two-vector update; subsumes `axpy` and pure-scaling as algebraic identities.
- [`scal`](./scal.md) — pure vector-scalar multiply; the fourth BLAS-1 floor primitive (sibling-subsumed by `axpby` β=0).
- [`apply_linop`](./apply_linop.md) — pure linear-operator application `y = A·x`; opaque-operator gate to the L2 `krylov-step` vocabulary.
- [`axpbypcz`](./axpbypcz.md) — fused three-scalar three-vector update; subsumes `axpby` (γ=0) and `axpy` (β=1, γ=0).

**Rough-in (obstruction)** — speculative L1 operators emitted by `L1>L0` obstruction themes (no Palace L0 anchor; harvester promotion gated on appearance of an anchor):

- `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min` — from [`minres-iteration`](../L1-L0/minres-iteration.md) theme.
- `bicgstab_step`, `omega_update`, `stabilisation_update` — from [`bicgstab-iteration`](../L1-L0/bicgstab-iteration.md) theme.

**Queued (open questions)** — small primitives that bottom-out remaining L0 patterns referenced by the firm cohort:

- `nrm2_B :: (x, B) → √(xᴴ B x)` — energy norm; depends on `dot` and `apply_linop`. Recorded as a boundary in `nrm2`'s entry; deferred to a separate harvest. Slug: `nrm2-B-weighted-energy-norm-harvest`.

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
