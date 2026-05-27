---
agent: harvester
invoked_at: 2026-05-27T02:53:54Z
scope: L2 operator: krylov-step
status: integrated
integrated_at: 2026-05-27T07:04:24Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied. First firm L2 operator. Six variant axes absorbed at construction time. Decision NOT to promote any cycle-004 speculative L1 operators recorded in scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md. Cross-cutter routes L4 dual-placement to cycle-006.
inputs:
  - reports/2026-05-26T231843Z-combinator-miner-krylov-iteration-step/CYCLE.md (rough-in source; cycle-002)
  - book/src/L2/index.md (current rough-in row, single entry)
  - book/src/L1/{axpy,axpby,axpbypcz,dot,nrm2,scal,apply_linop}.md (L1 deps; all firm post-cycle-004)
  - book/src/L1-L0/minres-iteration.md (cycle-004 obstruction theme — guidance only)
  - book/src/L1-L0/bicgstab-iteration.md (cycle-004 obstruction theme — guidance only)
  - book/src/spec/slices/{cg,gmres,chebyshev,arnoldi_step,polynomial_recurrence_step}.md (five Phase-1 instance citations)
  - book/src/concepts/{derived-view-hoisting,variant-absorption,first-iteration-unrolling,sequential-obstruction,solve-monad,apply_BA,orthogonalization,constructed-operators}.md (cross-referenced; not duplicated)
skill_uptake:
  - skill: classify-variant-axis
    triggered: true
    decision: artifact_landed
    rationale: Six variant axes identified and classified (preconditioner present/absent, orthogonalization variant, polynomial-kind, first-iteration-unrolled, restart shape, in-place/out-of-place). Axis count matches the combinator-miner cycle-002 enumeration verbatim — none added, merged, or split. All six absorbed at construction time per `variant-absorption` levels (b)/(c).
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Citations verified inline by reading the cited ranges (five Phase-1 pattern-instance citations: cg.md:103-115/:172-188/:393-425, gmres.md:459-471, chebyshev.md:354-362, arnoldi_step.md:99-105/:285-298, polynomial_recurrence_step.md:119-160; plus outer-driver consumer sites and L0 test anchors). Skill invocation deferred until critic-phase mechanism stabilizes per cycle-002/cycle-004 pattern.
  - skill: skill-selection
    triggered: true
    decision: artifact_landed
    rationale: Three relevant skills considered (classify-variant-axis, verify-citation-range, verify-refinement-surface); first two applied. Refinement-surface verification not applicable (this is an L2 firm-up promoting a rough-in row to a firm chapter, not a refinement of a prior coarser surface).
---

# REPORT: Formalize `krylov-step` at L2

## Summary

The cycle-002 combinator-miner identified `krylov-step` as a five-slice-attested pattern shape: a pure-functional **step kernel** `(OpParams, IterState) -> { state: IterState', outputs: StepOutputs }` whose primitive sequence (`apply_linop → optionally(precondition/orthogonalize/project) → axpy-class state update → small scalar update → derived view`) is invariant across CG, GMRES, Chebyshev, Arnoldi, and the polynomial-recurrence catalog. The rough-in row in `book/src/L2/index.md` carries the proposal but no firm operator chapter exists. This harvester invocation firms it up: an explicit step-record signature with three named state strata (sim / operator-internal / ephemeral, after `concepts/state-stratification.md`), six variant axes (matching the combinator-miner's enumeration), a single non-trivial algebraic law (the `output_extras` distributivity over `iterate_while` trajectories — the demand-pruning law of `derived-view-hoisting`), and explicit non-laws covering the absences (commutativity, associativity, fold-merge). The cycle-004 MINRES/BiCGStab obstruction themes are kept as guidance inputs but their five speculative L1 operators are **not** promoted to firm — they are step-bodies that would specialise to `krylov-step` rather than orthogonal axes that simplify its L2 semantics. The decision and reasoning are recorded under Open questions and as a fresh `scaffolding/decisions/` entry (proposed; integrator wires).

## Proposed changes

```edit:book/src/L2/krylov-step.md
# krylov-step

Pure-functional step kernel for iterative Krylov-shaped solvers and polynomial smoothers. Consumed by L4's `iterate_while` / `solve-monad` outer driver; encapsulates the primitive composition that every Krylov-shaped slice in the Palace corpus factors into.

## Context

The Phase-1 slice corpus exhibits a recurring pattern: every iterative method written as a per-step kernel composed of (at most) five primitive groups, threaded by an outer fold. CG (`cg.md:103-115, :172-188, :393-425`), GMRES (`gmres.md:459-471`), Chebyshev (`chebyshev.md:354-362`), Arnoldi (`arnoldi_step.md:99-105, :285-298`), and the three polynomial-recurrence sites cataloged at `polynomial_recurrence_step.md:119-160` all factor into the same kernel-plus-driver shape. The combinator-miner cycle-002 enumerated the five pattern instances and proposed `krylov-step` as the L2 name for the kernel. This chapter is the firm operator definition.

`krylov-step` lives at **L2**, not L3 or L4. L3 is the iteration-rotation layer; the *outer* iteration of every Krylov method carries a `sequential-obstruction` at L3 (cg.md:341-349, arnoldi_step.md:194-213), and the step body composes L3-native primitives without a global lift opportunity. Putting `krylov-step` at L3 would conflate "kernel exists" with "kernel lifts to a tensor-field op" — distinct claims, only one of which holds. L4 already has `iterate_while`, `solve-monad`, `state-stratification`, `derived-view-hoisting`, and `first-iteration-unrolling`; `krylov-step` is the L2 primitive-composition shape that L4's outer driver folds. The pair `(krylov-step at L2, iterate_while at L4)` is the canonical decomposition.

A cross-cutting prose treatment lives at [`concepts/solver-as-operator`](../concepts/solver-as-operator.md) for the consumer-side framing; the relevant building-block concepts live at [`derived-view-hoisting`](../concepts/derived-view-hoisting.md), [`variant-absorption`](../concepts/variant-absorption.md), [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md), [`sequential-obstruction`](../concepts/sequential-obstruction.md), [`solve-monad`](../concepts/solve-monad.md), [`apply_BA`](../concepts/apply_BA.md), and [`orthogonalization`](../concepts/orthogonalization.md). The L2 entry here is the firm operator definition; the concept pages carry the narrative.

## Signature

```text
krylov-step :: (op: OpParams, s: IterState) -> { state: IterState', outputs: StepOutputs }
```

Shape contract (bunsen-style; named axes):

- `op` — `OpParams` — closed-over operator surface. Bound at solve setup; immutable across the step. Variant axes (preconditioner side, orthogonalization variant, polynomial-kind) are absorbed into `OpParams`'s constructed-operator and scalar-generator closures (level (b)/(c) of [`variant-absorption`](../concepts/variant-absorption.md)). Concretely:
  - `op.T : LinearOperator[N, N]` — the system operator (or constructed `apply_BA = A·M⁻¹` / `M⁻¹·A` / `B^{1/2}·A·B^{1/2}` per pc-side variant).
  - `op.orthog? : OrthogonalizationOperator` — optional; present in Arnoldi/GMRES, absent in CG/Chebyshev.
  - `op.scalars? : (k, S) -> ((α_0, sd, sr) | (α, β), S')` — optional scalar-coefficient closure; present in polynomial methods (Chebyshev-4th / Chebyshev-1st), absent in Krylov methods (which compute scalars from in-step inner products).
  - `op.eps : Scalar` — convergence threshold; closure-captured.
- `s` — `IterState` — the threaded iteration state. Record-shaped; concrete fields are slice-specific but always partition into three strata (per [`state-stratification`](../concepts/state-stratification.md)):
  - **iterate-stratum**: `Tensor[N]`-typed fields (`x`, `r`, optionally `z`, `p`, `r̂₀`, basis-column `V[j]`). Field-side, MPI-collective length axis `N`.
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
- **Optional auxiliary stage** — present iff the slice's variant-axis profile selects it. GMRES / Arnoldi: `op.orthog (V_prefix, w)`, dispatching once on `gs_orthog ∈ {MGS, CGS, CGS2}` per `arnoldi_step.md:101-108`. Chebyshev: `op.scalars (k, scalar_state)` per `chebyshev.md:355-362`. CG: absent. Variant absorption (level (b)) ensures the dispatch is a single inlined closure invocation; the step body's textual shape does not branch on the variant.
- **Iterate-stratum update** — one or more `axpy` / `axpby` / `axpbypcz` calls updating the iterate-stratum fields. Each call is a pure L1 primitive; the chain length is slice-specific (CG: two axpy + one axpby; arnoldi: one scal + the orthogonalize unfolding; chebyshev: one axpbypcz + one axpy). The fields touched are `s.x`, `s.r`, `s.p`, `s.z`, or (for basis-extending methods) `V[j+1]`.
- **Scalar-stratum update** — one or more `dot` / `nrm2` calls plus closed-form recurrence arithmetic. CG: `dot Ap p`, `dot r' r'`. GMRES: `dot v_i w` (per orthogonalize iteration). Chebyshev: closed-form `(α₀, sd, sr)` via the closure. The scalar-stratum is what threads through to the next step's iterate-update.
- **Output readout** — a derived view of the post-step state, written into the `outputs` record. Per [`derived-view-hoisting`](../concepts/derived-view-hoisting.md), this slot is the *only* place where a value that is a pure function of `state'` is exposed; the field is pruned by the demand analysis at the call site. Typical contents: `residual_norm: sqrt (abs s'.beta)`; for GMRES `ls_residual: |s'.s[j+1]|`; for Arnoldi the new Hessenberg subdiagonal `h_jp1`.

The ordering of the five primitive groups is **forced by dataflow** — `apply_linop` must precede `axpy α s.<input> w` because the latter reads `w`; the scalar-stratum update must follow the iterate-stratum update if it reads the new residual; the output readout is downstream of both. Within independent primitive groups, reorderings (e.g., CGS batching all `dot`s before all `axpy`s) are exact-arithmetic equivalent but differ in MPI-collective shape (load-bearing per CLAUDE.md §Optimization tricks). The step body is **non-commutative** in its primitive sequence (see Algebraic laws).

The step is **stateless across calls** — `op` is closed over, but no in-step mutation escapes; `s'` is a fresh record (the L1 primitives `axpy`, `axpby`, `axpbypcz` are themselves pure at L1, with mutation reintroduced only in the L1>L0 lowering). This is what makes `krylov-step` foldable: `iterate_while (krylov-step op) s₀ predicate` is a well-defined fold because the kernel has no hidden side channels.

The kernel can carry **breakdown signals** through the `outputs.breakdown_token` slot. Palace's `CheckDot` (cg.md:288, iterative.cpp:244-250) is the L0 anchor: the dot-product is partial-functioned on finiteness and (for SPD systems) positivity. At L2 the partial-function guard surfaces as a step-local precondition on the scalar-stratum update; the corresponding L4 surface lifts it via `convergence-test` per [`concepts/convergence-test`](../concepts/convergence-test.md). The kernel itself does not branch on the breakdown — the outer driver does, on inspection of `outputs.breakdown_token`.

The kernel can carry a **first-iteration branch** internally (CG v0.4 form, cg.md:172-188) or be unrolled out to a separate `cg_first_step` kernel before `iterate_while_with_prev` (CG v0.5 form, cg.md:393-425). Both are valid `krylov-step` shapes; the variant axis `first-iteration-unrolled` is a *step-shape* variant, not a *step-body* variant. Each form has a fixed (different) record schema; the unrolled form's steady-state record drops `β_prev` (cg.md:381-391). The choice is documented at [`concepts/first-iteration-unrolling`](../concepts/first-iteration-unrolling.md).

## Algebraic laws

`krylov-step` is a **fold kernel**, not an algebra in its own right. The traditional algebraic laws (commutativity, associativity, distributivity) are properties of *binary operations*; the step kernel is a unary endomorphism on `IterState` parameterised by `OpParams`. The relevant algebraic structure lives at the *trajectory* level — the kernel is the body of a fold, and the laws that hold are laws about how outputs of the fold relate to the kernel's structure.

The laws below hold; absences are deliberate and listed explicitly.

1. **Output-extras distributivity over trajectory** (the load-bearing law; inherited from [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)). For any `StepOutputs`-typed field `f` such that `f = g(state')` for a pure function `g`, the trajectory observation `(iterate_while (krylov-step op) s₀ p).trajectory.map(.outputs.f)` is equal to `(iterate_while (krylov-step op) s₀ p).trajectory.map(state').map(g)`. **Consequence**: if no downstream consumer reads `.outputs.f`, the kernel is free to skip the `g` computation — the trajectory's `state'` projection is unchanged. This is the demand-pruning law that the slice corpus uses to defer residual-norm and `ls_residual` computation until a consumer (printing, regression-check, plotting) demands them. Witnessed at cg.md:325-339 (the residual-norm hoisting), chebyshev.md:421-436 (the derived-view treatment of `initial_guess`-as-control), and gmres.md:471-489 (the LS-residual proxy). This is the *only* non-trivial algebraic law `krylov-step` carries.

2. **Primitive-count invariance under reformulation**. The number of `apply_linop` calls per step is a structural invariant of the slice's variant-axis profile — equivalent reformulations (e.g., CG with branched first-iteration vs. CG with unrolled first-iteration) have the same per-step `apply_linop` count, and any reformulation that changes the count is a *different algorithm*, not a different rendering. (CG: 1 per step. GMRES inner Arnoldi: 1 per step. Chebyshev inner `k`-loop: 1 per `k`. Arnoldi step: 1.) This is the cost-metric invariant Krylov-methods literature uses; `krylov-step` makes it a first-class structural property. Witnessed by the per-slice primitive-call enumeration at cg.md:103-115, arnoldi_step.md:99-105, chebyshev.md:354-362.

3. **State-stratum independence**. The iterate-stratum update and the scalar-stratum update operate on disjoint record fields (`Tensor[N]`-typed vs. `Scalar`-typed) and have no cross-stratum aliasing within a single step. Consequence: a reordering of the iterate-stratum-update primitives among themselves (subject to dataflow constraints) does not affect the scalar-stratum-update primitives, and vice versa. This is what makes per-step parallelism *between strata* (the field-side `axpy` and the scalar-side recurrence-update at the same step time) a transparent performance optimisation at L1>L0, not an algebraic change. Witnessed at cg.md:103-115 (CG's `dot z'_A p'` reads `z'_A` from the apply, but no `axpy` reads the same scalar before the dot completes).

Laws that explicitly **do not** hold:

- **Commutativity of the primitive sequence**. The five primitive groups (apply, auxiliary, iterate-update, scalar-update, output-readout) cannot be reordered without changing the value. The dataflow chain `apply_linop → axpy(α, ·, w) → dot(w, ·)` is rigid — swapping any two adjacent groups produces a different state (or a type error). This is true even for the polynomial-recurrence variants (chebyshev.md:354-362) where the closed-form scalar-generator looks "swappable" with the axpy chain: it depends on `k` and the residual, both of which require the prior apply.
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

1. **preconditioner present/absent** — CG vs. PCG; GMRES via the `apply_BA = A·M⁻¹` / `M⁻¹·A` / `B^{1/2}·A·B^{1/2}` constructed-operator surface. Absorbed at level (c) into `op.T`. Witnessed at cg.md:228-257 (PCG vs. unpreconditioned CG), gmres.md:135-150 (`apply_BA` pc-side absorption).
2. **orthogonalization variant** — `gs_orthog ∈ {MGS, CGS, CGS2}`. Present iff the slice uses an orthogonalize stage (GMRES, Arnoldi); absent in CG and Chebyshev. Absorbed at level (b) into `op.orthog`. Witnessed at arnoldi_step.md:107-113 (one dispatch site, residual variant axis).
3. **polynomial-kind** — `Chebyshev-4th | Chebyshev-1st`. The scalar-generator closure `op.scalars (k, S) -> ((α₀, sd, sr), S')` differs in arity (4th: `S = Unit`; 1st: `S = { ρ_prev }`) and in its closed-form coefficient table. Absorbed at level (c) into `op.scalars`. Witnessed at chebyshev.md:308-323 (the `ChebOp<E, S>` parameter making the variant a type-level distinction).
4. **first-iteration-unrolled vs. branch-in-body** — CG v0.4 (cg.md:172-188) keeps the `if it == 0 then s.r else axpby ...` branch inside the kernel; CG v0.5 (cg.md:393-425) splits `cg_first_step` and `cg_steady_step` and threads `β_prev` via `iterate_while_with_prev`. Both forms are valid `krylov-step` shapes; the variant axis selects which.
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

- `book/src/spec/slices/cg.md:103-115` (CG L2 step body), `:172-188` (CG L4 `cg_step`), `:393-425` (CG L4 v0.5 split into `cg_first_step` and `cg_steady_step`).
- `book/src/spec/slices/gmres.md:459-471` (GMRES L4 `inner_loop` body — Arnoldi-step + LS-update + counter-increment + convergence-test).
- `book/src/spec/slices/chebyshev.md:354-362` (Chebyshev L4 `innerStep` — the polynomial-recurrence kernel folded by `foldM` over `[1..order-1]`).
- `book/src/spec/slices/arnoldi_step.md:99-105` (L1 Arnoldi step procedure), `:285-298` (L4 `arnoldiStep` monadic form).
- `book/src/spec/slices/polynomial_recurrence_step.md:119-160` (catalog of three polynomial-recurrence sites — Chebyshev-4th, Chebyshev-1st, GMRES-Givens-stream — all factoring into a step-kernel-plus-outer-fold shape).

Outer-driver consumer sites (the `iterate_while` / `forM_` / `foldM` calls that fold `krylov-step`):

- `book/src/spec/slices/cg.md:208-220`, `:430-446` (CG `cg_solve` calling `iterate_while` / `iterate_while_with_prev`).
- `book/src/spec/slices/gmres.md:430-454` (GMRES `solve_loop` + `restart_cycle` + `inner_loop` nested folds).
- `book/src/spec/slices/chebyshev.md:330-353` (Chebyshev `apply` with `forM_ [1..pc_it]` outer and `foldM ... [1..order-1]` inner).

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
- `reference/palace/palace/linalg/iterative.cpp:244-250` — `CheckDot` partial-function guard.
- Per cg.md:288, gmres.md:128, chebyshev.md:99-100: no direct unit tests on CG / GMRES / Chebyshev step kernels (integration tests only) — coverage gap inherited from the rough-in; not introduced by this firm-up.
```

```edit:book/src/L2/index.md
# L2 — Algebraic decompositions

The canonical algebraic decomposition: each operation written as composition of base tensor / operator / quadrature primitives, with HPC/SIMD optimization tricks **unfolded back into the base algebras**. The **fusion rotation** layer.

## Context

L2 is the layer where:
- Cache-blocked loops, SIMD intrinsics, manual unrolling are erased — they are below L2's level of abstraction.
- Kernel fusion across multiple algebraic operations is unfolded into composition.
- Packed sparse formats are de-packed to dense/symbolic algebraic operators.
- Batched specialized BLAS calls are written as compositions of base primitives.

**Load-bearing numerical tricks** (non-associative reduction orderings, fast-math, mixed-precision intermediates, deterministic-vs-atomic accumulation) are **preserved as explicit algebraic claims** with the property they buy called out.

## Semantics (overlay)

L2 vocabulary: tensors, linear operators, quadrature rules, basis transformations, primitive operations (axpy, dot, matvec, gemv, trsv, scal, nrm2, …). State threading via explicit value semantics. Compositions of L1 primitives into method-step shapes are first-class at L2.

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | `(op: OpParams, s: IterState) → { state: IterState', outputs: StepOutputs }` | L1: `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`. L2-composition: `apply_BA`, `orthogonalization`. Concepts: `derived-view-hoisting`, `variant-absorption`, `first-iteration-unrolling`, `sequential-obstruction`, `solve-monad`, `state-stratification`, `solver-as-operator`. | `firm` (harvested cycle-005; promoted from rough-in proposed-by combinator-miner:2026-05-26T231843Z) |

## Working Notes

- This is the layer most populated by `combinator-miner` output — patterns recurring across the slice corpus are L2 candidates.
- `krylov-step` was promoted from rough-in to firm in cycle-005 (harvester invocation 2026-05-27T025354Z). The firm chapter is at [`krylov-step.md`](./krylov-step.md); the rough-in's six variant axes and pattern-instance list survived intact (no axes added, none merged or split). One non-trivial algebraic law was authored (the demand-pruning law over `outputs` extras, inherited from `derived-view-hoisting`); the kernel's non-laws (commutativity, associativity, fold-merge, step-composition, linearity, bit-determinism-across-variants) are catalogued explicitly to prevent decoration drift.
- **Pattern provenance and consumers** (carried from the rough-in; combinator-miner:2026-05-26T231843Z):
  - **Consumed-by**: L4 `iterate_while` + `solve-monad` outer driver (cg.md §L4, gmres.md §L4, chebyshev.md §L4, arnoldi_step.md §L4).
  - **Pattern instances** (five, well clear of ≥3 soft bar):
    - `spec/slices/cg.md:103-115`, `:172-188`, `:393-425`
    - `spec/slices/gmres.md:459-471`
    - `spec/slices/chebyshev.md:354-362`
    - `spec/slices/arnoldi_step.md:99-105`, `:285-298`
    - `spec/slices/polynomial_recurrence_step.md:119-160` (catalog of three instances)
- **Cycle-004 obstruction-theme guidance**: the MINRES and BiCGStab L1>L0 themes (`book/src/L1-L0/minres-iteration.md`, `book/src/L1-L0/bicgstab-iteration.md`) sketch five speculative L1 operators (`lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`, `bicgstab_step`, `omega_update`, `stabilisation_update`). The cycle-005 harvester decision is to **not** promote any to firm L1: each is a *step-body specialisation* of `krylov-step` rather than an orthogonal axis that would simplify `krylov-step`'s L2 semantics. The decision is recorded at `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md` (proposed for integrator wiring).
- The cycle-005 firm-up did **not** introduce a new L2 entry for `orthogonalize` as a first-class L2 composition, even though `krylov-step` depends on it as a level-(b)-absorbed surface — that remains a candidate for a future harvester invocation. Same for `incremental-least-squares` (GMRES outer driver's small-dense kernel; currently lives as a concept page only).
```

```edit:book/src/SUMMARY.md
# Summary

[Introduction](./introduction.md)
# Methodology
- [Overview](./methodology/overview.md)
# L4 — Graph-Evaluation Calculus
- [Overview](./L4/index.md)

# L4 > L3 — Lowering
- [Overview](./L4-L3/index.md)

# L3 — Global Tensor-Field Operations
- [Overview](./L3/index.md)

# L3 > L2 — Lowering
- [Overview](./L3-L2/index.md)

# L2 — Algebraic Decompositions
- [Overview](./L2/index.md)
- [krylov-step](./L2/krylov-step.md)

# L2 > L1 — Lowering
- [Overview](./L2-L1/index.md)

# L1 — Mutation-Lifted Forms
- [Overview](./L1/index.md)
- [axpy](./L1/axpy.md)
- [dot](./L1/dot.md)
- [nrm2](./L1/nrm2.md)
- [axpby](./L1/axpby.md)
- [scal](./L1/scal.md)
- [apply_linop](./L1/apply_linop.md)
- [axpbypcz](./L1/axpbypcz.md)

# L1 > L0 — Lowering
- [Overview](./L1-L0/index.md)
- [axpby-mutation-rotation](./L1-L0/axpby-mutation-rotation.md)
- [bicgstab-iteration](./L1-L0/bicgstab-iteration.md)
- [minres-iteration](./L1-L0/minres-iteration.md)

# L0 — Cited Palace Source
- [Overview](./L0/index.md)
# Phase 1 corpus (slice-vertical; raw material for combinator extraction)
- [Index — Slice Status](./spec/index.md)
  - [CG — Preconditioned Conjugate Gradient](./spec/slices/cg.md)
  - [GMRES](./spec/slices/gmres.md)
  - [Orthogonalisation (MGS / CGS / CGS2)](./spec/slices/orthog.md)
  - [Divergence-free projection](./spec/slices/divfree.md)
  - [Chebyshev smoother](./spec/slices/chebyshev.md)
  - [Arnoldi step](./spec/slices/arnoldi_step.md)
  - [Plane rotation stream](./spec/slices/plane_rotation_stream.md)
  - [Sparse triangular solve (negative result)](./spec/slices/sparse_triangular_solve.md)
  - [CG Preconditioning Framework](./spec/slices/cg_preconditioning_framework.md)
  - [Polynomial recurrence step](./spec/slices/polynomial_recurrence_step.md)
# Concepts (shared library)
- [Index](./concepts/index.md)
  - [Dependency map](./concepts/dependency-map.md)
  - [rotation — methodology concept](./concepts/rotation.md)
  - [variant absorption — methodology concept](./concepts/variant-absorption.md)
  - [constructed operators — methodology concept](./concepts/constructed-operators.md)
  - [apply_linop](./concepts/apply_linop.md)
  - [axpy](./concepts/axpy.md)
  - [dot](./concepts/dot.md)
  - [nrm2](./concepts/nrm2.md)
  - [scal](./concepts/scal.md)
  - [givens](./concepts/givens.md)
  - [trsv](./concepts/trsv.md)
  - [gemv_basis](./concepts/gemv_basis.md)
  - [orthogonalization](./concepts/orthogonalization.md)
  - [incremental-least-squares](./concepts/incremental-least-squares.md)
  - [gmres](./concepts/gmres.md)
  - [set_subvector_zero](./concepts/set_subvector_zero.md)
  - [ksp_solve](./concepts/ksp_solve.md)
  - [tensor-field-lift](./concepts/tensor-field-lift.md)
  - [sequential-obstruction](./concepts/sequential-obstruction.md)
  - [state-stratification](./concepts/state-stratification.md)
  - [solve-monad](./concepts/solve-monad.md)
  - [convergence-test](./concepts/convergence-test.md)
  - [chebyshev-iteration](./concepts/chebyshev-iteration.md)
  - [elementwise-product](./concepts/elementwise-product.md)
  - [derived-view-hoisting](./concepts/derived-view-hoisting.md)
  - [solver-as-operator](./concepts/solver-as-operator.md)
  - [two_operator_split](./concepts/two_operator_split.md)
  - [complex-from-real-lift](./concepts/complex-from-real-lift.md)
  - [negative-result-slice](./concepts/negative-result-slice.md)
  - [constructed-operator-factory](./concepts/constructed-operator-factory.md)
  - [finest-level-unwrap](./concepts/finest-level-unwrap.md)
  - [counter-update](./concepts/counter-update.md)
  - [build-time-vs-run-time-stratification](./concepts/build-time-vs-run-time-stratification.md)
  - [first-iteration-unrolling](./concepts/first-iteration-unrolling.md)
  - [givens_generate](./concepts/givens_generate.md)
  - [givens_apply](./concepts/givens_apply.md)
  - [plane-rotation-stream](./concepts/plane-rotation-stream.md)
  - [apply_BA](./concepts/apply_BA.md)
  - [capability-typing](./concepts/capability-typing.md)
  - [scope-out-obstruction](./concepts/scope-out-obstruction.md)

# Design Artifacts
- [Index](./design/index.md)
- [L4 — Graph-Evaluation Calculus (strawman)](./design/l4_calculus.md)
# Meta-Reviews
- [Index](./meta-reviews/index.md)
  - [2026-05-24 — first meta-review (cycles 1–3)](./meta-reviews/2026-05-24.md)
  - [2026-05-24 — second meta-review (cycles 4–6)](./meta-reviews/2026-05-24-cycles-4-6.md)
  - [2026-05-24 — third meta-review (cycles 7–9)](./meta-reviews/2026-05-24-cycles-7-9.md)
  - [2026-05-24 — fourth meta-review (cycles 10–12)](./meta-reviews/2026-05-24-cycles-10-12.md)
  - [2026-05-24 — fifth meta-review (cycles 13–15)](./meta-reviews/2026-05-24-cycles-13-15.md)
  - [2026-05-24 — sixth meta-review (cycles 16–18)](./meta-reviews/2026-05-24-cycles-16-18.md)
  - [2026-05-24 — seventh meta-review (cycles 19–21)](./meta-reviews/2026-05-24-cycles-19-21.md)
  - [2026-05-24 — eighth meta-review (cycles 22–24)](./meta-reviews/2026-05-24-cycles-22-24.md)
  - [2026-05-25 — ninth meta-review (cycles 25–30)](./meta-reviews/2026-05-24-cycles-25-30.md)
  - [2026-05-25 — tenth meta-review (cycles 31–36) — Phase 6 DONE](./meta-reviews/2026-05-25-cycles-31-36.md)
  - [2026-05-25 — eleventh meta-review (cycles 37–43) — first skill extraction](./meta-reviews/2026-05-25-cycles-37-43.md)
  - [2026-05-25 — twelfth meta-review (cycles 44–49)](./meta-reviews/2026-05-25-cycles-44-49.md)
  - [2026-05-25 — thirteenth meta-review (cycles 50–55)](./meta-reviews/2026-05-25-cycles-50-55.md)
  - [2026-05-25 — fourteenth meta-review (cycles 56–61) — orthog at L4](./meta-reviews/2026-05-25-cycles-56-61.md)
  - [2026-05-25 — fifteenth meta-review (cycles 62–67)](./meta-reviews/2026-05-25-cycles-62-67.md)
  - [2026-05-25 — sixteenth meta-review (cycles 68–73) — second skill](./meta-reviews/2026-05-25-cycles-68-73.md)
  - [2026-05-25 — seventeenth meta-review (cycles 74–79) — chebyshev at L4](./meta-reviews/2026-05-25-cycles-74-79.md)
  - [2026-05-25 — eighteenth meta-review (cycles 80–85) — forward-frontier + intermediate-tier](./meta-reviews/2026-05-25-cycles-80-85.md)
  - [2026-05-26 — nineteenth meta-review (cycles 86–91) — third skill (skill-selection)](./meta-reviews/2026-05-26-cycles-86-91.md)
  - [2026-05-26 — twentieth meta-review (cycles 92–103) — arnoldi_step at L4 (first intermediate-tier)](./meta-reviews/2026-05-26-cycles-92-103.md)
  - [2026-05-26 — twenty-first meta-review (cycles 104–115) — refinement fires, 2 more intermediate-tier slices](./meta-reviews/2026-05-26-cycles-104-115.md)
  - [2026-05-26 — twenty-second meta-review (cycles 116–127) — framework slice extracted, sensitivity at cap](./meta-reviews/2026-05-26-cycles-116-127.md)
```

## Supporting evidence

The five pattern-instance citations and the outer-driver consumer sites are carried verbatim from the combinator-miner cycle-002 report. The cycle-004 obstruction themes (MINRES, BiCGStab) are read as guidance inputs but not consumed as evidence — see the speculative-operator decision below. The L1 dependencies (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) are all firm post-cycle-004 and provide a stable composition floor.

A new `scaffolding/decisions/` entry is proposed (file body below) to record the speculative-L1-operator decision per the unimplemented-Palace-components policy:

```edit:scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md
# Decision: cycle-004 MINRES/BiCGStab speculative L1 operators not promoted in cycle-005

**Date**: 2026-05-27
**Decided in**: cycle-005 harvester invocation (`reports/2026-05-27T025354Z-harvester-krylov-step-L2/CYCLE.md`)
**Decision**: Five speculative L1 operators from cycle-004 obstruction themes — `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min` (from `book/src/L1-L0/minres-iteration.md`); `bicgstab_step`, `omega_update`, `stabilisation_update` (from `book/src/L1-L0/bicgstab-iteration.md`) — are **not promoted to firm L1** as part of the `krylov-step` L2 harvest.

## Reasoning

The cycle-005 harvester role-spec applies the `feedback_unimplemented_palace_components` policy: a speculative L1 operator may be promoted to firm only if (a) doing so simplifies the L2 `krylov-step` semantics AND (b) the lift is small.

Each of the five speculative operators is a **step-body specialisation** of `krylov-step`, not an orthogonal axis that would simplify its semantics:

- `lanczos_step` — symmetric-tridiagonal specialisation of the orthogonalization-variant axis already absorbed in `krylov-step` (axis #2 of six).
- `three_term_recurrence_update` — band-3 specialisation of the `dot+axpy` chain inside `lanczos_step`'s orthogonalize stage; not a new axis.
- `givens_apply_with_residual_min` — band-3 specialisation of the `incremental-least-squares` running-QR step; structurally distinct from `krylov-step`'s primitive composition and would belong (if firmed) under a separate `incremental-least-squares` L2 entry, not under `krylov-step`.
- `bicgstab_step` — short-recurrence non-symmetric Krylov step; its per-step primitive count is **two** `apply_linop` calls instead of `krylov-step`'s typical one, but this is a slice-level instantiation, not an L1 axis change. The two-apply-per-step shape would surface in BiCGStab's slice as a numeric in the variant-axis profile (a `apply_count` field, not a new axis kind).
- `omega_update` — closed-form scalar arithmetic on two `dot` results; algebraically identical to a `dot / dot` ratio. Already expressible in `krylov-step`'s scalar-stratum-update phase using existing L1 primitives. No new operator needed.
- `stabilisation_update` — bundle of `omega_update + axpy + axpy`. Already a composition of three L1 primitives; bundling them into one named L1 operator would inflate the L1 vocabulary without algebraic gain. If BiCGStab acquires a Palace anchor, the bundle name would be appropriate at L2 (as a `krylov-step` variant), not at L1.

Promoting any of the five would **inflate** rather than simplify `krylov-step`'s L2 semantics: the variant-axis profile would gain entries for "is-this-a-lanczos-step" / "is-this-a-bicgstab-step", duplicating the slice-level instantiation surface. The variant-absorption discipline (level (c) closure into `op.T` / `op.orthog` / `op.scalars`) already handles the methods' divergences cleanly.

## Re-evaluation triggers

This decision should be re-opened if any of:

1. Palace acquires an L0 anchor for MINRES or BiCGStab (the cycle-004 obstruction themes flip from `obstruction` to affirmative).
2. The cross-layer-cross-cutter identifies a coverage gap that requires one of the speculative operators as an L1 dependency for a *firm* lowering theme (currently they live only in obstruction themes).
3. A future Phase-1 slice (LOBPCG, time-stepping, eigensolver) introduces a step kernel that genuinely requires one of the speculative operators as an L1-level primitive (not as a slice-instantiation of `krylov-step`).

## Cross-references

- `book/src/L1-L0/minres-iteration.md` — the cycle-004 obstruction theme that proposed `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`.
- `book/src/L1-L0/bicgstab-iteration.md` — the cycle-004 obstruction theme that proposed `bicgstab_step`, `omega_update`, `stabilisation_update`.
- `book/src/L2/krylov-step.md` — the cycle-005 firm operator whose variant-axis profile would absorb these step-body specialisations.
- `feedback_unimplemented_palace_components` (project memory) — the policy applied.
```

## Open questions / caveats

1. **Speculative-L1-promotion decision**: documented above and in the proposed `scaffolding/decisions/` entry. The decision applies the unimplemented-Palace-components policy and concludes NO promotion. Re-evaluation triggers are catalogued.

2. **`orthogonalize` as a future L2 first-class entry**: `krylov-step` references `orthogonalize` (via `op.orthog` closure) as a level-(b)-absorbed L2 composition surface, but no firm L2 chapter exists for it. The `orthogonalize` slice (`book/src/spec/slices/orthog.md`) and concept page (`book/src/concepts/orthogonalization.md`) exist; lifting the L2-composition story into a firm L2 entry is a future harvester candidate. Out of scope for this invocation.

3. **`incremental-least-squares` as a future L2 first-class entry**: similar to `orthogonalize`. GMRES's outer driver consumes the running-QR / Givens-stream composition as a small-dense kernel; it currently lives as a concept page only. Out of scope for this invocation.

4. **L2 layer-intro refresh**: the L2 layer-intro (`book/src/L2/index.md`) gains its first firm operator chapter as part of this work, but the Context and Semantics-overlay sections were not authored to reflect a layer with named compositions (only with primitive operators). A future `layer-intro-author` invocation should refresh the L2 intro to articulate the role of named compositions and to surface the demand-pruning law as a layer-wide algebraic feature.

5. **No L0 source citation for `krylov-step`**: per the combinator-miner cycle-002 open question, `krylov-step` is a methodology-level concept — no single Palace-source citation, only five Palace-spec-corpus citations (Phase-1 slices). This is recorded as a feature, not a bug, of the L2 layer: L2 names compositions that emerged from cross-slice pattern-matching, not from source-line identification. Flagged because future critics may surface this as a citation-validity concern; the explicit no-L0-source status is the harvester's response.

6. **Naming**: the rough-in flagged "krylov-step" as stretching to cover Chebyshev (which is not strictly Krylov-subspace per Saad 2003). The firm chapter preserves the name on grounds of (a) consistency with the cycle-002 rough-in, (b) the fact that the variant-axis absorption makes the naming a *role* description rather than a *family* description (the step is a Krylov-shaped fold-kernel; Chebyshev's polynomial-recurrence is a degenerate case where the scalar-stratum is closed-form rather than inner-product-driven). Alternative names (`iterative-step-kernel`, `fold-step`, `solver-step`) were considered and rejected as less precise. Re-naming is left for a future cross-cutter invocation if friction surfaces.

7. **GMRES-Givens-stream as a step-kernel instance**: the rough-in flagged `polynomial_recurrence_step.md:147-155` (the Givens-stream site) as a borderline case. Strict reading excludes (primitive sequence is `givens_apply`/`givens_generate`, not `apply_linop`+`axpy`+`dot`); broad reading includes (the fold-kernel-plus-outer-driver shape matches). The firm chapter records the Givens-stream case under the polynomial-recurrence-step citation but does *not* claim it as a `krylov-step` instance — it is a sibling pattern at the small-dense / `incremental-least-squares` scope.
