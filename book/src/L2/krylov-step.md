---
layer: L2
operator: krylov-step
# Graded-stack scheme (authored from scratch, batch-35 c109; mirrors the c108 L2/divfree-projector
# from-scratch authoring). This firm L2 fold-kernel rests on its seven firm L1 leaves (depends-on)
# AND lowers through the L2>L1 kernel-defusion theme (lowers-to depends-on; mirrors how L1 ops reach
# their L1>L0 theme). The firm L1 leaf list is the chapter's own §Dependencies (:96). This node firm
# (rank 3). Of the seven L1 leaf targets, apply_linop/dot/nrm2/scal carry rank: firm; axpy/axpby/axpbypcz
# carry no rank token yet (typed-no-rank), so the rank invariant holds vacuously over those three edges
# (a no-rank target cannot be a rank violation) — rank_violations remains 0 either way.
rank: firm
edges:
  depends-on:
    - L1/apply_linop
    - L1/axpy
    - L1/axpby
    - L1/axpbypcz
    - L1/dot
    - L1/nrm2
    - L1/scal
    - target: L2-L1/krylov-step-kernel-defusion
      kind: lowers-to             # the L2>L1 lowering theme this kernel composition lowers through
  reference:
    - concepts/solver-as-operator
    - concepts/derived-view-hoisting
    - concepts/variant-absorption
    - concepts/first-iteration-unrolling
    - concepts/sequential-obstruction
    - concepts/solve-monad
    - concepts/state-stratification
    - concepts/apply_BA
    - concepts/orthogonalization
    - concepts/constructed-operators
---

# krylov-step

Pure-functional step kernel for iterative Krylov-shaped solvers and polynomial smoothers. Consumed by L4's `iterate_while` / `solve-monad` outer driver; encapsulates the primitive composition that every Krylov-shaped slice in the Palace corpus factors into.

## Context

The Phase-1 slice corpus (now fully lifted into firm entries — the three krylov slices `{cg,gmres,arnoldi_step}` were deleted cycle-099 once all material reached firm homes) exhibited a recurring pattern: every iterative method written as a per-step kernel composed of (at most) five primitive groups, threaded by an outer fold. CG (the firm CG step-body evidence lives in this entry's §Evidence and lowers to L0 at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B — `iterative.cpp:360-486`; the L4-v0.5 first-iteration-unrolled rendering is firm-homed at `book/src/L4/krylov-step.md` Form B), GMRES (firm L0 `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C — `iterative.cpp:543-705`), Chebyshev (`book/src/L4/chebyshev.md` §Semantics `innerStep` — the polynomial-recurrence kernel), Arnoldi (firm L0 Sub-pattern C inner Arnoldi loop within `iterative.cpp:563-683`; L2 instance in this entry's §Evidence), and the three polynomial-recurrence sites (Chebyshev-4th, Chebyshev-1st, GMRES-Givens-stream — the firm home is `book/src/L4/chebyshev.md` §Semantics `innerStep` for the Chebyshev pair and the cross-family non-unification catalog at `concepts/negative-result-slice.md`) all factor into the same kernel-plus-driver shape. The combinator-miner cycle-002 enumerated the five pattern instances and proposed `krylov-step` as the L2 name for the kernel. This chapter is the firm operator definition.

`krylov-step` lives at **L2**, not L3 or L4. L3 is the iteration-rotation layer; the *outer* iteration of every Krylov method carries a `sequential-obstruction` at L3 (the firm [`sequential-obstruction`](../concepts/sequential-obstruction.md) concept page; live anchor `arnoldi_step.md:194-213` — the original CG evidence `cg.md:341-349` was lifted into the concept page + `book/src/L3/krylov-step.md` §"Iteration-rotation marker" per the cycle-009 corpus reduction), and the step body composes L3-native primitives without a global lift opportunity. Putting `krylov-step` at L3 would conflate "kernel exists" with "kernel lifts to a tensor-field op" — distinct claims, only one of which holds. L4 already has `iterate_while`, `solve-monad`, `state-stratification`, `derived-view-hoisting`, and `first-iteration-unrolling`; `krylov-step` is the L2 primitive-composition shape that L4's outer driver folds. The pair `(krylov-step at L2, iterate_while at L4)` is the canonical decomposition.

A cross-cutting prose treatment lives at [`concepts/solver-as-operator`](../concepts/solver-as-operator.md) for the consumer-side framing; the relevant building-block concepts live at [`derived-view-hoisting`](../concepts/derived-view-hoisting.md), [`variant-absorption`](../concepts/variant-absorption.md), [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md), [`sequential-obstruction`](../concepts/sequential-obstruction.md), [`solve-monad`](../concepts/solve-monad.md), [`apply_BA`](../concepts/apply_BA.md), and [`orthogonalization`](../concepts/orthogonalization.md). The L2 entry here is the firm operator definition; the concept pages carry the narrative.

## Signature

```text
krylov-step :: (op: OpParams, s: IterState) -> { state: IterState', outputs: StepOutputs }
```

Shape contract (bunsen-style; named axes; the solution-space shape group `S` and the square operator form `LinOp[(S: ...), (S: ...)]` follow the named-shape-group convention of [`l4_calculus`](../design/l4_calculus.md) §1.2.1–§1.2.2):

- `op` — `OpParams` — closed-over operator surface. Bound at solve setup; immutable across the step. Variant axes (preconditioner side, orthogonalization variant, polynomial-kind) are absorbed into `OpParams`'s constructed-operator and scalar-generator closures (level (b)/(c) of [`variant-absorption`](../concepts/variant-absorption.md)). Concretely:
  - `op.T : LinOp[(S: ...), (S: ...)]` — the system operator (square, on the solution-space shape group `S`; or constructed `apply_BA = A·M⁻¹` / `M⁻¹·A` / `B^{1/2}·A·B^{1/2}` per pc-side variant).
  - `op.orthog? : OrthogonalizationOperator` — optional; present in Arnoldi/GMRES, absent in CG/Chebyshev.
  - `op.scalars? : (k, S) -> ((α_0, sd, sr) | (α, β), S')` — optional scalar-coefficient closure; present in polynomial methods (Chebyshev-4th / Chebyshev-1st), absent in Krylov methods (which compute scalars from in-step inner products).
  - `op.eps : Scalar` — convergence threshold; closure-captured.
- `s` — `IterState` — the threaded iteration state. Record-shaped; concrete fields are slice-specific but always partition into three strata (per [`state-stratification`](../concepts/state-stratification.md)):
  - **iterate-stratum**: `Tensor[(S: ...)]`-typed fields (`x`, `r`, optionally `z`, `p`, `r̂₀`, basis-column `V[j]`), all congruent to the solution-space shape group `S`. Field-side, MPI-collective.
  - **scalar-stratum**: `Scalar`-typed fields (`β`, `α`, `ρ`, `ω`, `θ`, optional `β_prev`). Rank-0; threaded by the recurrence.
  - **counter-stratum**: `Int`-typed `it` and `Bool`-typed `converged`. Bookkeeping; never participates in the field algebra.
- result — `{ state: IterState', outputs: StepOutputs }` — a record with two fields:
  - `state: IterState'` — the post-step iteration state. Same record shape as `s`, with one or more fields rebound.
  - `outputs: StepOutputs` — a record of step-observable outputs (typically `residual_norm: Scalar`; for GMRES `ls_residual: Scalar`; for breakdown-guarding kernels a `breakdown_token: BreakdownTag` that L4 surfaces via `convergence-test`). Subject to demand-pruning per [`derived-view-hoisting`](../concepts/derived-view-hoisting.md): consumer-side reads of `iterate_while`'s trajectory determine whether the kernel materialises these fields.

The shape contract makes the **fold-kernel role** explicit: `krylov-step`'s output is the next iteration's state plus a step-local readout; the type signature is the canonical shape for an `iterate_while`-style fold body (`carry -> { carry', readout }`). The L4 outer driver `iterate_while (carry -> krylov-step op carry) carry₀ predicate` reads as a fold over the iteration's trajectory.

The two records `OpParams` and `IterState'` are **slice-specific**; this chapter does not enumerate their fields, only their stratification. Each consuming slice (cg, gmres, chebyshev, arnoldi_step, the future minres / bicgstab / lobpcg) instantiates the records and writes `krylov-step` over its instantiation. The combinator names the *role*; the slice supplies the record shape.

## Semantics

`krylov-step` is a single pass of an iterative method's per-step kernel. It consumes the current iteration state `s` and the closure-captured operator surface `op`, and produces both the next state `s'` and a record of step-observable outputs. The internal body composes (at most) five primitive groups, in this dataflow-forced order:

```text
krylov-step op s =
  let w         = apply_linop op.T s.<input_field>             -- field-side operator apply
  let s_aux     = optionally apply op.orthog (V_prefix, w)     -- absorbed orthogonalize / project
                  or       apply op.scalars (k, scalar_state)  -- absorbed scalar generator
                  or       (no-op for vanilla CG)
  let s'_iter   = axpy / axpby / axpbypcz updates over          -- iterate-stratum update
                  s.{x, r, p, z, ...}                          -- (state-stratum-dependent)
  let s'_scalar = dot / nrm2 / recurrence-update                -- scalar-stratum update
  let outputs   = derived-view of s' (per derived-view-hoisting) -- ephemeral; demand-pruned
  in { state: s' ⊕ s'_iter ⊕ s'_scalar, outputs }
```

Each line corresponds to a distinct primitive group at L2:

- **Operator apply** — exactly one `apply_linop` call per step (or one constructed `apply_BA` call, which itself unfolds at L2 into one or two `apply_linop` calls per [`concepts/apply_BA`](../concepts/apply_BA.md)). The operator-apply count is the standard cost metric for Krylov methods; `krylov-step` makes it structural.
- **Optional auxiliary stage** — present iff the slice's variant-axis profile selects it. GMRES / Arnoldi: `op.orthog (V_prefix, w)`, dispatching once on `gs_orthog ∈ {MGS, CGS, CGS2}` per `arnoldi_step.md:101-108`. Chebyshev: `op.scalars (k, scalar_state)` per `book/src/L4/chebyshev.md` §Signature `scalars` field + §Semantics `op.scalars` calls. CG: absent. Variant absorption (level (b)) ensures the dispatch is a single inlined closure invocation; the step body's textual shape does not branch on the variant.
- **Iterate-stratum update** — one or more `axpy` / `axpby` / `axpbypcz` calls updating the iterate-stratum fields. Each call is a pure L1 primitive; the chain length is slice-specific (CG: two axpy + one axpby; arnoldi: one scal + the orthogonalize unfolding; chebyshev: one axpbypcz + one axpy). The fields touched are `s.x`, `s.r`, `s.p`, `s.z`, or (for basis-extending methods) `V[j+1]`.
- **Scalar-stratum update** — one or more `dot` / `nrm2` calls plus closed-form recurrence arithmetic. CG: `dot Ap p`, `dot r' r'`. GMRES: `dot v_i w` (per orthogonalize iteration). Chebyshev: closed-form `(α₀, sd, sr)` via the closure. The scalar-stratum is what threads through to the next step's iterate-update.
- **Output readout** — a derived view of the post-step state, written into the `outputs` record. Per [`derived-view-hoisting`](../concepts/derived-view-hoisting.md), this slot is the *only* place where a value that is a pure function of `state'` is exposed; the field is pruned by the demand analysis at the call site. Typical contents: `residual_norm: sqrt (abs s'.beta)`; for GMRES `ls_residual: |s'.s[j+1]|`; for Arnoldi the new Hessenberg subdiagonal `h_jp1`.

The ordering of the five primitive groups is **forced by dataflow** — `apply_linop` must precede `axpy α s.<input> w` because the latter reads `w`; the scalar-stratum update must follow the iterate-stratum update if it reads the new residual; the output readout is downstream of both. Within independent primitive groups, reorderings (e.g., CGS batching all `dot`s before all `axpy`s) are exact-arithmetic equivalent but differ in MPI-collective shape (load-bearing per CLAUDE.md §Optimization tricks). The step body is **non-commutative** in its primitive sequence (see Algebraic laws).

The step is **stateless across calls** — `op` is closed over, but no in-step mutation escapes; `s'` is a fresh record (the L1 primitives `axpy`, `axpby`, `axpbypcz` are themselves pure at L1, with mutation reintroduced only in the L1>L0 lowering). This is what makes `krylov-step` foldable: `iterate_while (krylov-step op) s₀ predicate` is a well-defined fold because the kernel has no hidden side channels.

The kernel can carry **breakdown signals** through the `outputs.breakdown_token` slot. Palace's `CheckDot` (`reference/palace/palace/linalg/iterative.cpp:21-32` — real overload at :22, complex overload at :28; called at :396, :410, :445, :461; recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B) is the L0 anchor: the dot-product is partial-functioned on finiteness and (for SPD systems) positivity. At L2 the partial-function guard surfaces as a step-local precondition on the scalar-stratum update; the corresponding L4 surface lifts it via `convergence-test` per [`concepts/convergence-test`](../concepts/convergence-test.md). The kernel itself does not branch on the breakdown — the outer driver does, on inspection of `outputs.breakdown_token`.

The kernel can carry a **first-iteration branch** internally (CG v0.4 form; the L0 `if (!it) { p = z; } else { AXPBY(...beta/beta_prev...); }` branch at `iterative.cpp:434-441`) or be unrolled out to a separate `cg_first_step` kernel before `iterate_while_with_prev` (CG v0.5 form, firm-homed at `book/src/L4/krylov-step.md` Form B). Both are valid `krylov-step` shapes; the variant axis `first-iteration-unrolled` is a *step-shape* variant, not a *step-body* variant. Each form has a fixed (different) record schema; the unrolled form's steady-state record drops `β_prev` (the `forget_beta_prev` projection making the v0.4↔v0.5 equivalence formal is firm-homed in the `book/src/L4/krylov-step.md` Form B narration). The choice is documented at [`concepts/first-iteration-unrolling`](../concepts/first-iteration-unrolling.md).

## Algebraic laws

`krylov-step` is a **fold kernel**, not an algebra in its own right. The traditional algebraic laws (commutativity, associativity, distributivity) are properties of *binary operations*; the step kernel is a unary endomorphism on `IterState` parameterised by `OpParams`. The relevant algebraic structure lives at the *trajectory* level — the kernel is the body of a fold, and the laws that hold are laws about how outputs of the fold relate to the kernel's structure.

The laws below hold; absences are deliberate and listed explicitly.

1. **Output-extras distributivity over trajectory** (the load-bearing law; inherited from [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)). For any `StepOutputs`-typed field `f` such that `f = g(state')` for a pure function `g`, the trajectory observation `(iterate_while (krylov-step op) s₀ p).trajectory.map(.outputs.f)` is equal to `(iterate_while (krylov-step op) s₀ p).trajectory.map(state').map(g)`. **Consequence**: if no downstream consumer reads `.outputs.f`, the kernel is free to skip the `g` computation — the trajectory's `state'` projection is unchanged. This is the demand-pruning law that the slice corpus uses to defer residual-norm and `ls_residual` computation until a consumer (printing, regression-check, plotting) demands them. Witnessed at [`concepts/derived-view-hoisting`](../concepts/derived-view-hoisting.md) §"Worked example: CG residual norm" (the residual-norm hoisting; the canonical CG evidence lifted from the now-reduced slice per the cycle-009 corpus reduction — original pre-reduction range `cg.md:325-339`), `book/src/L4/chebyshev.md` §"Initial-guess shape: branch vs derived view" (the derived-view treatment of `initial_guess`-as-control), and gmres.md:471-489 (the LS-residual proxy). This is the *only* non-trivial algebraic law `krylov-step` carries.

2. **Primitive-count invariance under reformulation**. The number of `apply_linop` calls per step is a structural invariant of the slice's variant-axis profile — equivalent reformulations (e.g., CG with branched first-iteration vs. CG with unrolled first-iteration) have the same per-step `apply_linop` count, and any reformulation that changes the count is a *different algorithm*, not a different rendering. (CG: 1 per step. GMRES inner Arnoldi: 1 per step. Chebyshev inner `k`-loop: 1 per `k`. Arnoldi step: 1.) This is the cost-metric invariant Krylov-methods literature uses; `krylov-step` makes it a first-class structural property. Witnessed by the per-slice primitive-call enumeration: for CG, the one `A->Mult(p, z)` per step at `iterative.cpp:443` inside the inner for-loop `iterative.cpp:427-464` (recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B; original pre-reduction slice range `cg.md:103-115`); arnoldi_step.md:99-105; `book/src/L4/chebyshev.md` §Semantics `innerStep` (one `applyLinop op.A d` per `k`).

3. **State-stratum independence**. The iterate-stratum update and the scalar-stratum update operate on disjoint record fields (`Tensor[(S: ...)]`-typed vs. `Scalar`-typed) and have no cross-stratum aliasing within a single step. Consequence: a reordering of the iterate-stratum-update primitives among themselves (subject to dataflow constraints) does not affect the scalar-stratum-update primitives, and vice versa. This is what makes per-step parallelism *between strata* (the field-side `axpy` and the scalar-side recurrence-update at the same step time) a transparent performance optimisation at L1>L0, not an algebraic change. Witnessed at `iterative.cpp:427-464` (CG's inner loop: `denom = Dot(comm, z, p)` at :444 reads `z` from the `A->Mult(p, z)` apply at :443, but the `x.Add(alpha, p)` / `r.Add(-alpha, z)` axpy updates at :448-449 do not read `denom`/`beta` before the dot completes — recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B; original pre-reduction slice range `cg.md:103-115`).

Laws that explicitly **do not** hold:

- **Commutativity of the primitive sequence**. The five primitive groups (apply, auxiliary, iterate-update, scalar-update, output-readout) cannot be reordered without changing the value. The dataflow chain `apply_linop → axpy(α, ·, w) → dot(w, ·)` is rigid — swapping any two adjacent groups produces a different state (or a type error). This is true even for the polynomial-recurrence variants (`book/src/L4/chebyshev.md` §Semantics `innerStep`) where the closed-form scalar-generator looks "swappable" with the axpy chain: it depends on `k` and the residual, both of which require the prior apply.
- **Associativity / fold-merge**. `iterate_while (krylov-step op) (iterate_while (krylov-step op) s₀ p₁) p₂` is **not** equal to `iterate_while (krylov-step op) s₀ (p₁ ‖ p₂)` for arbitrary `p₁`, `p₂` — the trajectory observations may differ (the inner fold's `outputs` are not visible to the outer fold), and convergence-predicates that depend on monotonic-loss properties do not generally compose. This is why slice-level restart logic (gmres.md:435-454) is structured as an *outer* loop around the `krylov-step`-folding inner loop, not as a flattened single fold.
- **Identity element**. There is no `s_id` such that `krylov-step op s_id = { state: s_id, outputs: ... }` in general. `α = 0` in CG is not the identity, it is *breakdown* (the residual is exactly in the orthogonal complement of the Krylov subspace, signalling convergence or stagnation). The kernel has no algebraic identity.
- **Step composition into a bigger step**. Two successive `krylov-step` invocations do not, in general, simplify to a single `krylov-step` with combined parameters — the second step reads scalars (`β`, `α`) produced by the first, and these scalars are not closed-form functions of the input state. The kernel is intrinsically sequential at the step boundary; this is the same sequentiality observed at L3 (`sequential-obstruction`) and is why `krylov-step` is consumed by `iterate_while`, not by a parallel reduction.
- **Linearity in any single argument**. `krylov-step op (α·s₁ + β·s₂) ≠ α · krylov-step op s₁ + β · krylov-step op s₂` in general, because the scalar-stratum update involves divisions (`α = β / dot(Ap, p)`) and the convergence flag involves a comparison — neither is linear. The kernel is *built from* linear primitives (`apply_linop`, `axpy`) but their composition with `dot` and scalar arithmetic destroys linearity at the kernel level.
- **Bit-determinism across orthogonalization variants**. For the GMRES / Arnoldi specialisations, switching `gs_orthog` from MGS to CGS to CGS2 produces mathematically-equivalent (under exact arithmetic) but bit-distinct trajectories. This is recorded as load-bearing per CLAUDE.md §Optimization tricks: the variant choice is a *different algorithm* in floating-point even though it is "the same `krylov-step`" at the L2 schema level.

## Dependencies

L2 dependencies (other L2 vocabulary or below):

- L1 primitives: [`apply_linop`](../L1/apply_linop.md), [`axpy`](../L1/axpy.md), [`axpby`](../L1/axpby.md), [`axpbypcz`](../L1/axpbypcz.md), [`dot`](../L1/dot.md), [`nrm2`](../L1/nrm2.md), [`scal`](../L1/scal.md). All firm post-cycle-004.
- L2 composition surfaces: [`apply_BA`](../concepts/apply_BA.md) (the constructed-operator surface that absorbs the preconditioner-side variant axis; itself an L1-composed operator), [`orthogonalization`](../concepts/orthogonalization.md) (the projection-and-residual-update surface that absorbs the `gs_orthog` variant; itself a composition of `dot` and `axpy` plus optional batched `gemv_basis`).

Concept references (cross-cutting; do not duplicate):

- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra underwriting Law 1.
- [`variant-absorption`](../concepts/variant-absorption.md) — the level (b)/(c) discipline by which the six variant axes are kept off the kernel's per-step signature.
- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the variant axis governing whether the first-step branch lives inside the kernel or outside.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the L3-edge classification governing why `krylov-step` lives at L2 and not L3.
- [`solve-monad`](../concepts/solve-monad.md) — the L4 outer-driver surface that consumes `krylov-step` (via `iterate_while`).
- [`state-stratification`](../concepts/state-stratification.md) — the three-stratum record-shape discipline.
- [`solver-as-operator`](../concepts/solver-as-operator.md) — the consumer-side framing (`krylov-step` is the step kernel of an operator-shaped solve).
- [`constructed-operators`](../concepts/constructed-operators.md) — the level (c) absorption of `op.T`'s preconditioner-side variant.

No L3 or L4 vocabulary appears in the L2 signature — that is the discipline of the layer.

## Variant axes

`krylov-step` has **six** variant axes at L2. All are absorbed at construction time (per [`variant-absorption`](../concepts/variant-absorption.md)) and do not appear in the per-step kernel signature:

1. **preconditioner present/absent** — CG vs. PCG; GMRES via the `apply_BA = A·M⁻¹` / `M⁻¹·A` / `B^{1/2}·A·B^{1/2}` constructed-operator surface. Absorbed at level (c) into `op.T`. Witnessed for CG/PCG at the L0 `if (B) { ApplyB(B, r, z, ...); } else { z = r; }` preconditioner branch inside the inner loop `iterative.cpp:427-464` plus the initial-guess/preconditioner threading at `iterative.cpp:377-386` (the variant collapse is documented at [`L1/ksp_solve`](../L1/ksp_solve.md) Variant axes; the L1>L0 reintroduction at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B; original pre-reduction slice range `cg.md:228-257`), gmres.md:135-150 (`apply_BA` pc-side absorption).
2. **orthogonalization variant** — `gs_orthog ∈ {MGS, CGS, CGS2}`. Present iff the slice uses an orthogonalize stage (GMRES, Arnoldi); absent in CG and Chebyshev. Absorbed at level (b) into `op.orthog`. Witnessed at arnoldi_step.md:107-113 (one dispatch site, residual variant axis).
3. **polynomial-kind** — `Chebyshev-4th | Chebyshev-1st`. The scalar-generator closure `op.scalars (k, S) -> ((α₀, sd, sr), S')` differs in arity (4th: `S = Unit`; 1st: `S = { ρ_prev }`) and in its closed-form coefficient table. Absorbed at level (c) into `op.scalars`. Witnessed at `book/src/L4/chebyshev.md` §Signature `ChebOp E S` field (the `S` scalar-state type parameter — `Unit` for 4th-kind, `{ rho_prev: E }` for 1st-kind — making the variant a type-level distinction via distinct closure types).
4. **first-iteration-unrolled vs. branch-in-body** — CG v0.4 keeps the `if it == 0 then s.r else axpby ...` branch inside the kernel (L0 anchor `iterative.cpp:434-441`); CG v0.5 (firm-homed at `book/src/L4/krylov-step.md` Form B) splits `cg_first_step` and `cg_steady_step` and threads `β_prev` via `iterate_while_with_prev`. Both forms are valid `krylov-step` shapes; the variant axis selects which.
5. **restart shape** — `non-restarted | restarted-fixed-dim | restarted-adaptive`. The kernel itself is restart-agnostic; the restart logic lives in the outer driver (gmres.md:430-454 — `solve_loop` + `restart_cycle` wrap `inner_loop`). For non-restarted methods (CG, Chebyshev) the axis collapses to a single value.
6. **in-place vs. out-of-place buffer use** — Arnoldi's `w` aliases `V[j+1]` (arnoldi_step.md:129-131); CG's L1 form is textually out-of-place but L0-realised in-place via `Vector::Add`. Transparent-performance-equivalent per CLAUDE.md §Optimization tricks; the L2 form is uniformly out-of-place, with the in-place specialisation reappearing in the L2>L1 lowering.

The variant-axis count of six matches the combinator-miner's enumeration (cycle-002 CYCLE.md §"Variant axes"). No new axes have been discovered in the firm-up; no axes have been merged or split.

## Status

`firm` — signature is the canonical fold-kernel shape; algebraic laws are reduced to the one non-trivial property (the demand-pruning law) plus two structural invariants; non-laws are catalogued explicitly; variant-axis profile is closed at six. The pattern is well-attested across five Phase-1 slices (per the combinator-miner cycle-002 report) and is the consumed-by surface for the cycle-004 MINRES and BiCGStab obstruction themes (whose speculative L1 operators specialise `krylov-step` for short-recurrence Krylov methods).

## L2 vs L1 distinction

- **L1**: individual primitive operators (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`). Each operator has a self-contained shape contract and a small set of algebraic laws (linearity, identity, scaling, distribution). The L1 vocabulary is the floor of the linear-algebra primitive set.
- **L2**: the *composition* of L1 primitives into method-step shapes. `krylov-step` is the L2 name for the recurring composition pattern observed across the slice corpus. L2's role is not to add new primitive operators but to name the canonical compositions and surface their algebraic laws (which are typically trajectory-level rather than per-call). `krylov-step` is the first such named composition; future L2 entries (likely candidates: `orthogonalize` as an L2 first-class composition, `incremental-least-squares` as an L2 composition consumed by GMRES's outer driver) will follow the same pattern — name the composition, list its variant axes, state the laws that hold *at the composition level*, do not re-derive the laws of the constituent L1 primitives.

## Evidence

Five Phase-1 slice instances (per combinator-miner cycle-002):

- CG L2 / L4 / L4-v0.5 step bodies — the firm L0 terminal home is `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (the inner CG body `iterative.cpp:360-486`; the per-step kernel for-loop `iterative.cpp:427-464`). The L4-v0.5 first-iteration-unrolling rendering (`cg_first_step` / `cg_steady_step`) is firm-homed at `book/src/L4/krylov-step.md` Form B (cycle-099 absorption).
- GMRES `inner_loop` body (Arnoldi-step + LS-update + counter-increment + convergence-test) — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; inner Arnoldi loop within `iterative.cpp:563-683`).
- `book/src/L4/chebyshev.md` §Semantics `innerStep` (the polynomial-recurrence kernel folded by the inner `iterate_while_pure` step-count loop over `[1..order-1]`; firm cycle-015, absorbing the former `chebyshev.md:354-362` slice §L4).
- Arnoldi step procedure / `arnoldiStep` monadic form — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop (within `iterative.cpp:563-683`); the MGS sub-step sequential-obstruction is firm at `book/src/concepts/sequential-obstruction.md` §"MGS as sequential-obstruction".
- `book/src/concepts/negative-result-slice.md` §Partial-positive sub-pattern + §Falsification criterion (the catalog of three polynomial-recurrence sites — Chebyshev-4th, Chebyshev-1st, GMRES-Givens-stream — all factoring into a step-kernel-plus-outer-fold shape; cross-family non-unification with the five-axis difference table, plus the within-Chebyshev partial-positive). Chebyshev-pair firm home: `book/src/L4/chebyshev.md` §Semantics `innerStep`.

Outer-driver consumer sites (the `iterate_while` / `forM_` / `foldM` calls that fold `krylov-step`):

- CG `cg_solve` calling `iterate_while` / `iterate_while_with_prev` — the v0.5 driver is firm-homed at `book/src/L4/krylov-step.md` Form B; the L0 outer composition is `BaseKspSolver::Mult` at `ksp.cpp:296-310` wrapping the inner CG for-loop `iterative.cpp:427-464` (recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-patterns A/B).
- GMRES `solve_loop` + `restart_cycle` + `inner_loop` nested folds — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C outer restart loop (`iterative.cpp:563-683`).
- `book/src/L4/chebyshev.md` §Semantics `apply` (the outer `pc_it` + inner `k` bounded loops, rendered as nested `iterate_while_pure` step-count folds; firm cycle-015, absorbing the former `chebyshev.md:330-353` slice §L4).

Cycle-004 obstruction-theme guidance (read but **not** consumed as evidence — see Open questions):

- `book/src/L1-L0/minres-iteration.md` — MINRES is the symmetric specialisation of `arnoldiStep`; its `lanczos_step` would specialise `krylov-step`'s orthogonalization-variant axis to a band-3 form.
- `book/src/L1-L0/bicgstab-iteration.md` — BiCGStab's `bicgstab_step` would be a specialisation with two `apply_linop` calls per step (instead of the conventional one) and a stabilisation half-step; this expands the per-step primitive count but does not add a new variant axis to `krylov-step`.

Concept-page cross-references (do not duplicate):

- `book/src/concepts/derived-view-hoisting.md` — the algebra underwriting Law 1.
- `book/src/concepts/variant-absorption.md` — the absorption discipline applied to the six variant axes.
- `book/src/concepts/first-iteration-unrolling.md` — the variant axis governing the first-step branch.
- `book/src/concepts/sequential-obstruction.md` — the L3-edge classification.
- `book/src/concepts/solve-monad.md` — the L4 outer-driver surface.
- `book/src/concepts/state-stratification.md` — the three-stratum record-shape discipline.
- `book/src/concepts/solver-as-operator.md` — the consumer-side framing.
- `book/src/concepts/apply_BA.md` — the constructed-operator preconditioner surface.
- `book/src/concepts/orthogonalization.md` — the orthogonalize composition.
- `book/src/concepts/constructed-operators.md` — the level-(c) absorption of `op.T`.

L0 / source-side tests (consulted for `CheckDot` and orthog-variant coverage):

- `reference/palace/test/unit/test-orthog.cpp:80-170`, `:234-280` — exercises the `gs_orthog` variant axis directly.
- `reference/palace/palace/linalg/iterative.cpp:21-32` — `CheckDot` partial-function guard (real overload at :22, complex overload at :28; the `MFEM_ASSERT(std::isfinite(dot) && dot >= 0.0, ...)` guard; called for CG at :396, :410, :445, :461). The previously-cited `:244-250` is the `ApplyB` preconditioner-apply helper, not `CheckDot` — same drifted-citation correction applied at §Semantics breakdown (the kernel's `breakdown_token` slot), verified by direct L0 read this dispatch.
- Per the `CheckDot` site `reference/palace/palace/linalg/iterative.cpp:21-32` (the CG SPD-guard; no dedicated unit test references `CgSolver`/`PCG` — CG is exercised only via integration tests at `test/examples/`, per `book/src/L1-L0/ksp-solve-mutation-rotation.md`'s coverage note), gmres.md:128, and `book/src/L1/chebyshev-smoother.md:260` (no dedicated unit test under `reference/palace/test/unit/`; behaviour exercised only through multigrid integration): no direct unit tests on CG / GMRES / Chebyshev step kernels (integration tests only) — coverage gap inherited from the rough-in; not introduced by this firm-up. (Original pre-reduction slice range: `cg.md:288`.)
