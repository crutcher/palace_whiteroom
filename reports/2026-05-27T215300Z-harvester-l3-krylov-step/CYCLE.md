---
agent: harvester
invoked_at: 2026-05-27T21:53:17Z
scope: L3 operator: krylov-step
status: integrated
integrated_at: 2026-05-27T230802Z
integration_commit: 30119eb
integration_notes: Applied cleanly via integrator-per-report pass 1 of cycle-010 (wave-1 first dispatch). **First firm L3 operator in the artifact** — L3 layer transitions from placeholder-only to 1-firm-operator status. Identity-lowering backfill enacting CLAUDE.md §Methodology invariants new bullet "Identity-lowerings still require both L levels" (codified cycle-009 meta-phase). Cycle-006 verdict "no L3 row needed for krylov-step" formally SUPERSEDED via cycle-010 enactment. Krylov-step chain now occupies all 7 layer/lowering positions explicitly (L4 firm > L4>L3 firm > L3 firm > L3>L2 firm > L2 firm > L1 ksp_solve firm > L1>L0 ksp-solve-mutation-rotation firm). 5 proposed-changes applied cleanly on first attempt. Index-placeholder displacement auto-fix fired (5th total: L3/index.md). L3 entry introduces 6-field YAML frontmatter — first L_n entry to carry frontmatter; future-normalization candidate forwarded to cycle-012 meta-phase batch.
inputs:
  - book/src/L2/krylov-step.md (firm; cycle-005)
  - book/src/L4/krylov-step.md (firm; cycle-006)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (firm; cycle-008)
  - book/src/L3-L2/krylov-step-body-identity.md (firm; cycle-009)
  - book/src/L3/index.md (placeholder; this dispatch's first firm operator)
  - book/src/design/l4_calculus.md §3.7 (iterate_while reduction rule)
  - CLAUDE.md §Methodology invariants ("Identity-lowerings still require both L levels"; "Layers are defined high→low")
  - scaffolding/priorities.md priority #20 (identity-lowering-both-levels-backfill)
  - scaffolding/friction-ledger.md `identity-lowering-both-levels-required`
---

# CYCLE: Formalize krylov-step at L3

## Summary

Firm L3 entry for `krylov-step`, the **first firm operator at L3**. The L4>L3 typed-wrapper-dissolution theme already publishes the L3 body shape as the RHS of its rewrite (`(op, K, s) -> (K', s', outputs)`), and the cycle-006 audit found this body to be value-thread-isomorphic to the L4 body (identity-in-form on the kernel's primitive sequence). Per the new methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md, cycle-009 meta-phase), the cycle-006 verdict "no L3 row needed for krylov-step" is **superseded**: each layer is coherent within itself, and the L3 reader must find `krylov-step` defined in L3 vocabulary at L3. This dispatch lands `book/src/L3/krylov-step.md` using L3 vocabulary (positional value-threading, no monad, no typed-record annotations, sequential-obstruction as the iteration-rotation marker), updates the L3 dep-map in `book/src/L3/index.md`, adds the SUMMARY entry, and annotates the upstream L4>L3 theme + the L3-L2 body-identity theme to record the backfill.

The signature is the value-threaded positional form. Semantics narrate the krylov-step body at L3 — operator-apply, optional auxiliary stage, iterate-and-scalar update, derived-view readout, explicit counter increment — defined in L3 vocabulary (whole-tensor primitives, positional tuples, value-threaded carry; no `Solve` monad, no `readonly` typing). Algebraic laws are the same three that survive the chain (demand-pruning over the trajectory's extras, primitive-count invariance, state-stratum non-aliasing as a documented partition rather than a typed split). Non-laws are inherited. Variant axes are inherited at six. The **Lifts from** section explicitly notes the L4 form is value-thread-isomorphic to this L3 form per the upstream theme.

## Proposed changes

```edit:book/src/L3/krylov-step.md
---
layer: L3
operator: krylov-step
firmness: firm
lowers_to:
  - book/src/L2/krylov-step.md (via book/src/L3-L2/krylov-step-body-identity.md)
lifts_from:
  - book/src/L4/krylov-step.md (via book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md; identity-in-form on the kernel body)
variant_axes:
  - preconditioner-present-or-absent
  - orthogonalization-variant (MGS / CGS / CGS2; carries below-body sequential-obstruction at MGS)
  - polynomial-kind (Chebyshev-4th / Chebyshev-1st)
  - first-iteration-unrolled-vs-branch-in-body (positional carry-threading at L3)
  - restart-shape (non-restarted / restarted-fixed-dim / restarted-adaptive)
  - in-place-vs-out-of-place-buffer-use (transparent below L3)
---

# krylov-step

Value-threaded step kernel for iterative Krylov-shaped solvers at L3 — the **iteration-rotation** rendering of the per-step body. Consumes a closure-captured operator-parameters value `op`, an iterate-bundle value `K`, and a simulator-state value `s`; produces the next iterate-bundle `K'`, the next simulator-state `s'`, and a demand-prunable readout record `outputs`. Companion to L4 [`krylov-step`](../L4/krylov-step.md) (typed wrapper around the same body) and L2 [`krylov-step`](../L2/krylov-step.md) (the primitive composition with the iteration view erased).

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `krylov-step` at L3 is the value-threaded form of the per-step Krylov / polynomial-smoother body, with the iteration view rendered as the relationship between successive carries (`(op, K, s) -> (K', s', outputs)`) rather than as the typed-wrapper-and-monad surface of L4 or the variant-absorbed primitive composition of L2.

The relationship to the adjacent layers is fully specified by two firm lowering themes:

- **Upward** to L4: [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) dissolves the L4 typed wrapper (state-stratification records, `Solve = StateT SimState Identity` monad, `OpParams` `readonly`, Form-A/B presentation) into this L3 form. The wrapper-dissolution is substantive **at the wrapper**; the kernel body's primitive sequence is **value-thread-isomorphic** between the L4 form and this L3 form. The L4 form's `do`-block dissolves to a `let`-chain; `modify (\s -> s { it = s.it + 1 })` dissolves to the explicit record-update line `s' = s { it = s.it + 1 }`; the typed three records dissolve to positional values in the signature.
- **Downward** to L2: [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) ratifies the cycle-002 combinator-miner assertion that the L3>L2 rotation on the body is identity-in-form. The two surface adjustments at the wrapper around the body (L3 `(op, K, s)` positional tuple consolidates into L2 unified `IterState`; L3 tail-recursive outer loop collapses to L2's outer-driver-by-role reference) are information-preserving; the body's let-chain maps line-for-line.

This L3 entry is the layer-coherence anchor: a reader at L3 can find `krylov-step` here, in L3 vocabulary, without having to reach up to L4 or down to L2 to recover the body shape. The backfill is the first cycle-010 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification). The cycle-006 audit verdict "no L3 row needed" is superseded: per the invariant, each layer is coherent within itself, and the L3 entry exists even when the lowering is trivial because the kernel body's primitive sequence is value-thread-isomorphic across the adjacent edges.

## Signature

```text
krylov-step :: (op, K, s) -> (K', s', outputs)
```

Two surface forms, mirroring L4 Form A / Form B inheritance, but with the L4 closure-vs-state distinction collapsed to positional carry:

**Form A — branch-in-body** (default; CG v0.4-shape; degenerate `carry = ()`):

```text
krylov-step :: (op, K, s) -> (K', s', outputs)
```

**Form B — first-iteration-unrolled** (CG v0.5-shape; opt-in per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)):

```text
krylov-step-first  :: (op, K, s)            -> (K', s', carry, outputs)
krylov-step-steady :: (op, K, s, carry)     -> (K', s', carry', outputs)
```

Shape contract (positional values; L3 has no `readonly` annotation and no monadic effect):

- **`op`** — operator-parameters value. Closure-captured by the body via the convention that `op` is the *first* positional argument and is never present in the return position; the value flows in, never out. The body reads `op.T` (the system operator, or constructed `apply_BA` per the preconditioner-side variant), the optional `op.orthog` (orthogonalization closure; present iff the slice uses Arnoldi / GMRES), and the optional `op.scalars` (scalar-generator closure; present iff the slice is polynomial-recurrence). Variant absorption is a **documented invariant at L3** — the kernel does not branch on any field of `op`; the variant selectors that L4 forbids by `readonly` typing are forbidden at L3 by convention and verified by inspection of the body. Slice-specific fields; this chapter does not enumerate them.
- **`K`** — iterate-bundle value. Carries the iteration-coupled fields that L4 partitions into the slice-specific ephemeral bundle: the iterate-side tensor fields (`K.<input_field>` — typically `K.r` for CG/MINRES, `K.p` for the basis-extension methods, `K.V[j]` for Arnoldi/GMRES), the basis-prefix `K.V_prefix` for orthogonalization, the polynomial-recurrence book-keeping `K.k`, `K.scalar_state`, and any per-step scalar carries (`K.α`, `K.β`, `K.ρ`, `K.ω`, `K.θ`). At L3 these are **positional fields of `K`**, not a typed record — the L3 calculus has no record-typing; `K` is a value whose internal structure is the slice's responsibility to keep consistent across the iteration.
- **`s`** — simulator-state value. Carries the persistent fields that L4 keeps in `SimState`: the iteration counter `s.it: Int`, the converged flag `s.converged: Bool`, the externally-visible iterate `s.x: Tensor[N]` (touched at restart-cycle boundaries, not per step), and the scalar bookkeeping (`s.initial_res`, `s.final_res`). At L3 `s` is value-threaded explicitly — the L4 `Solve = StateT SimState Identity` monad has dissolved (per [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)"); `s` flows in as a positional argument, `s'` flows out as a positional return.
- **`carry` (Form B only)** — recurrence-previous value carried positionally between `krylov-step-first` and `krylov-step-steady`. For CG: `carry = β_prev`. For GMRES (rarely Form B): `carry = H_{k,k-1}`. At L4 this is a closure parameter of the loop driver (per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)); at L3 it is **positional in the tuple** — the L4 closure-vs-state distinction has no operational meaning at L3, where there is no `iterate_while_with_prev` combinator distinct from `iterate_while` (per the upstream theme §"L3 form (RHS)" point 4). Form B at L3 is Form A with one extra position in the carry tuple.
- **result `(K', s', outputs)`** (Form A) or **`(K', s', carry', outputs)`** (Form B) — a positional tuple carrying the next iterate-bundle `K'` (value-threaded; no aliasing with the input `K`), the next simulator-state `s'` (value-threaded; explicit record-update of `s.it` and possibly `s.converged`), the demand-prunable readout record `outputs` (typically `{ residual_norm: Scalar }`; for GMRES also `ls_residual: Scalar`; for breakdown-guarding kernels a `breakdown_token: BreakdownTag`), and (Form B) the next-iteration `carry'`.

Three pieces of L4 wrapper machinery are absent at L3, and their absence is structural for the layer:

1. **No `Solve` monad.** The L4 `do`-block dissolves into a `let`-chain; `modify (\s -> s { it = s.it + 1 })` becomes the explicit `let s' = s { it = s.it + 1 }` record-update line. The monadic effect on `SimState` survives operationally as a positional thread; the L4 effect-localisation discipline survives as the convention that only the counter-update line touches `s`.
2. **No `readonly` typing.** The L4 `OpParams readonly` annotation forbids the kernel from re-inspecting variant selectors; at L3 the same absorption holds as a **documented invariant** (a coding discipline, verified by reading the body). L3's calculus has no `readonly` typing in its vocabulary; the variant-absorption discipline is preserved by convention.
3. **No Form-A-vs-Form-B presentation distinction at the combinator level.** The L4 distinction between "closure parameter of `iterate_while_with_prev`" and "state field of the iteration" loses operational meaning at L3 — both Form A and Form B are positional value-threading, distinguished only by whether the tuple has a `carry` position. The upstream theme dissolves the Form-B closure structure into the threaded tuple.

The two values `op` and `K` are **slice-specific** at L3 just as their L4 record counterparts are slice-specific (CG's `K` is `{ r, p, z?, α, β }`; GMRES's is `{ V, Z?, H, s, cs, sn, β, j }`); this chapter does not enumerate their internal structure, only their positional role. Each consuming slice instantiates `op` and `K` and writes `krylov-step` over its instantiation.

## Semantics

`krylov-step` at L3 is a single pass of the iterative method's per-step kernel, expressed as a value-threaded transformation `(op, K, s) -> (K', s', outputs)`. The body is a `let`-chain over the five primitive groups, in the same dataflow-forced order as L4 and L2 (because the body is value-thread-isomorphic across the chain). The L3 form (Form A; reproduced from the upstream theme §"L3 form (RHS)"):

```text
krylov-step op K s =
  let w       = apply_linop op.T K.<input_field>              -- operator apply on K's iterate-side input
  let K_aux   = optionally apply op.orthog (K.V_prefix, w)     -- optional auxiliary stage; one of three
                or       apply op.scalars (K.k, K.scalar_state) --   (GMRES / Arnoldi orthogonalize;
                or       K                                      --    Chebyshev scalar-generator; CG no-op)
  let K'      = krylov_update K_aux op w                       -- iterate-and-scalar update via L3-native
                                                               --   whole-tensor primitives (apply_linop,
                                                               --   axpy, axpby, axpbypcz, dot, nrm2, scal)
  let outputs = derived_views K' op                            -- demand-prunable readout (per
                                                               --   derived-view-hoisting)
  let s'      = s { it = s.it + 1 }                            -- explicit counter increment (the
                                                               --   dissolved Solve-monad `modify`)
  in (K', s', outputs)
```

Each line corresponds to a distinct L3 primitive group:

- **Operator apply** — `apply_linop op.T K.<input_field>` is one whole-tensor operator-application. The L3 form is L3-native by construction: `apply_linop` has signature `LinearOperator[N, N] -> Tensor[N] -> Tensor[N]` (no element-loop exposed). The operator-apply count is the standard Krylov cost metric; at L3 it is structural (exactly one per step, modulo the constructed `apply_BA` per the preconditioner-side variant, which itself is one or two `apply_linop`s as documented in the slice-specific `apply_BA`).
- **Optional auxiliary stage** — present iff the slice's variant-axis profile selects it. GMRES / Arnoldi: `op.orthog (K.V_prefix, w)` dispatching on the orthogonalization variant. Chebyshev: `op.scalars (K.k, K.scalar_state)` producing the closed-form polynomial coefficients. CG: no-op (the auxiliary is identity-on-`K`). The dispatch is a single inlined closure invocation; the kernel body's textual shape does not branch on the variant — variant absorption at L3 is the documented invariant inherited from L4 (without the `readonly` typing). **Below-body sequential obstruction**: when `op.orthog` is the MGS variant, the inside of the orthogonalization carries a [`sequential-obstruction`](../concepts/sequential-obstruction.md) (the per-`i` sequencing of `H[i,j] ← ⟨w, V[i]⟩` and `w ← w − H[i,j] · V[i]`); this obstruction is **below `krylov-step`'s body** — the body calls `op.orthog` as an opaque closure — and is documented at `book/src/spec/slices/arnoldi_step.md:194-213`, not introduced by this entry.
- **Iterate-and-scalar update** — `krylov_update K_aux op w` is the sub-composition that updates the iterate-bundle's tensor-side fields and scalar-side fields. At L3 this is a single named sub-composition (mirroring the upstream theme's rendering); at L2 the same content is split into two textual let-bindings (iterate-stratum update via `axpy` / `axpby` / `axpbypcz`; scalar-stratum update via `dot` / `nrm2` plus scalar arithmetic). The L3 rendering treats them as one named update because at L3 the iteration view is what's load-bearing, not the stratum split — the stratum partition is documented at the consuming slice's `K`-record description per [`state-stratification`](../concepts/state-stratification.md). Each constituent primitive (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) is whole-tensor by signature shape — no element loop exposed at L3.
- **Output readout** — `derived_views K' op` is the demand-prunable projection from the post-step iterate-bundle plus the operator-parameters into the `outputs` record. Typical contents: `outputs.residual_norm = sqrt (abs K'.β)`; for GMRES `outputs.ls_residual = |K'.s[j+1]|`; for breakdown-guarding kernels `outputs.breakdown_token: BreakdownTag` per the L0 anchor `reference/palace/palace/linalg/iterative.cpp:22-32` (`CheckDot`; real overload at :22, complex overload at :28). The slot is governed by [`derived-view-hoisting`](../concepts/derived-view-hoisting.md): consumer-side reads of the surrounding `iterate_while`'s trajectory determine whether `derived_views` materializes the fields.
- **Counter increment** — `let s' = s { it = s.it + 1 }` is the **explicit record-update line** that dissolves the L4 `modify (\s -> s { it = s.it + 1 })`. At L3 this is the only line that reads or writes `s` in the per-step body; the L4 effect-localisation discipline (the kernel's effect domain is exactly `SimState`) survives as the convention "only the counter-increment line touches `s`". The simulator-state's iterate `s.x` is not updated per step — at restart-cycle boundaries the outer loop folds the correction `K.V · K.y` (GMRES) or the running iterate `K.x_running` (CG) into `s.x` exactly once. This placement is inherited from L4 per [`solve-monad`](../concepts/solve-monad.md) §"Worked example — GMRES", documented at L3 as a discipline.

The ordering of the five primitive groups is **forced by dataflow** — `apply_linop` produces `w`, which is read by both the auxiliary stage (`op.orthog`'s argument tuple, or `op.scalars`'s implicit residual access) and by `krylov_update`; the scalar-stratum update inside `krylov_update` depends on the iterate-stratum update if it reads the new residual; the output readout is downstream of both; the counter increment is independent of the body and could in principle commute with any pure binding, but is conventionally placed at the end of the let-chain so the textual sequence parallels L4's `do`-block.

The body is **stateless across calls** — `op` is closure-captured but never mutated; `K` and `s` flow in, `K'` and `s'` flow out as fresh positional values; the L1 primitives (`axpy`, `axpby`, `axpbypcz`) are pure at L1, with mutation reintroduced only in the L1>L0 lowering. This is what makes `krylov-step` foldable by an L3 tail-recursive outer loop (the value-thread-isomorphic image of L4's `iterate_while`; per the upstream theme §"What the L3 form for `iterate_while` looks like").

The body carries **breakdown signals** through `outputs.breakdown_token` (when present). The kernel itself does not branch on breakdown — the outer loop does, on inspection of `outputs.breakdown_token` per the [`convergence-test`](../concepts/convergence-test.md) discipline. The L4 form routes breakdown through `outputs` rather than `SimState`; the L3 form preserves this routing as a positional convention.

The body carries a **first-iteration branch** internally (Form A; CG v0.4) or is split into two named functions `krylov-step-first` and `krylov-step-steady` (Form B; CG v0.5; opt-in per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)). At L3 the Form-B variant adds a `carry` position to the tuple signature; the L4 closure-vs-state distinction has no operational meaning at L3.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `krylov-step`'s iteration view is the relationship between successive carries `(K, s) -> (K', s')`. **The body itself lifts as a whole-tensor operation** — every primitive in the let-chain is L3-native by signature shape. **The outer loop that folds this body does not lift** — the trajectory of carries `(K_0, s_0), (K_1, s_1), …, (K_n, s_n)` is intrinsically sequential because each step reads scalars (`α`, `β`, `ρ`, `ω`, `θ`) produced by the previous step, and the scalar dependence is not closed-form in the carry. The outer-loop sequentiality is the **outer-loop `sequential-obstruction`** documented at `book/src/spec/slices/cg.md:341-349` and `book/src/spec/slices/arnoldi_step.md:194-213`; it is a property of the surrounding `iterate_while_L3` tail-recursion, not of the `krylov-step` body itself. This entry's body is identity-in-form to the L2 body precisely because all sequentiality is pushed into the surrounding loop or below into the orthogonalization-MGS sub-primitive.

## Algebraic laws

The three laws that survive the full L4>L3>L2 chain hold at L3. Absences are catalogued explicitly to prevent decoration drift.

1. **Output-extras distributivity over trajectory** (the load-bearing law; inherited from [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)). For any field `f` of the `outputs` record such that `f = g(K')` for a pure function `g` of the post-step iterate-bundle, the trajectory observation `(iterate_while_L3 (krylov-step op) (K_0, s_0) p).trajectory.map(.outputs.f)` is equal to `(iterate_while_L3 (krylov-step op) (K_0, s_0) p).trajectory.map(.K).map(g)`. **Consequence**: if no downstream consumer reads `.outputs.f`, the L3 form is free to skip the `g` computation — the carry's `K` projection is unchanged. This is the demand-pruning law that underwrites the residual-norm hoisting and the §3.8 trajectory-accumulator pruning at the surrounding `iterate_while_L3` (per the upstream theme §"What the L3 form for `iterate_while` looks like"). At L3 the law is statable directly because the `outputs` record is a positional projection of `K'`; the §3.8 rule transports through the wrapper-dissolution because the body is value-thread-isomorphic to the L4 body. Witnessed by the consumer-side analysis at `reference/palace/palace/linalg/iterative.hpp:52-55` (four-scalar consumer surface) and `reference/palace/palace/linalg/ksp.cpp:296-310` (sole caller; per-iteration consumption absent in `palace/`).

2. **Primitive-count invariance under reformulation**. The number of `apply_linop` calls per step is a structural invariant of the slice's variant-axis profile — Form A and Form B of the L3 form have the same per-step `apply_linop` count (the `(first, steady)` split moves the branch, not the apply). Any reformulation that changes the count is a *different algorithm*. (CG: 1 per step. GMRES inner Arnoldi: 1 per step. Chebyshev inner k-loop: 1 per k. Arnoldi step: 1.) Inherited from the L4 entry by the value-thread-isomorphism of the body — the L4>L3 dissolution does not introduce or elide any `apply_linop` call.

3. **State-stratum non-aliasing as a documented partition**. At L3 the three strata — operator-parameters `op` (closure-captured; never returned), iterate-bundle `K` (positional input + output), simulator-state `s` (positional input + output) — are partitioned across the positional signature with **no cross-stratum aliasing**: the body's `let`-chain reads `op.*` and `K.*` to compute new `K'` fields, reads `s.it` only to increment it to `s'.it`, and never writes back to `op`. Consequence: a reordering of the iterate-and-scalar-update primitives inside `krylov_update` (subject to dataflow constraints) does not affect the counter-increment line, and vice versa — the counter increment commutes with any pure `K`-bundle binding, since `s.it` is never read inside the body. The L4 typing makes this structural via the typed record split; at L3 it is a documented partition over the positional carry, verified by reading the body. The discipline is information-equivalent to the L4 typing, just less mechanically checked.

Laws that explicitly **do not** hold:

- **Commutativity of the primitive sequence**. Inherited from the chain. The five primitive groups (apply, auxiliary, iterate-and-scalar update, output readout, counter increment) cannot be reordered without changing the value (modulo the counter-increment line, which is independent — see Law 3). The dataflow chain `apply_linop -> krylov_update` is rigid: `apply_linop` produces `w`, `krylov_update` reads it. The L3 form preserves this rigidity exactly.
- **Associativity / fold-merge**. Inherited from the chain. `iterate_while_L3 (krylov-step op) (iterate_while_L3 (krylov-step op) (K_0, s_0) p_1) p_2` is **not** equal to `iterate_while_L3 (krylov-step op) (K_0, s_0) (p_1 ‖ p_2)` for arbitrary predicates — the inner fold's `outputs` are not visible to the outer fold, and convergence predicates that depend on monotonic-loss properties do not generally compose. This is why slice-level restart logic is structured as an *outer* loop around the `krylov-step`-folding inner loop at L3 (per `book/src/spec/slices/gmres.md:435-454`), not as a flattened single fold.
- **Identity element**. Inherited from the chain. There is no `K_id` such that `krylov-step op K_id s = (K_id, s', outputs)` in general. `α = 0` in CG is breakdown (the residual is exactly in the orthogonal complement of the Krylov subspace, signalling convergence or stagnation), not identity. The L3 form has no algebraic identity.
- **Step composition into a bigger step**. Inherited from the chain. Two successive `krylov-step` invocations do not simplify to a single `krylov-step` with combined parameters — the second step reads scalars produced by the first, and these scalars are not closed-form functions of the input carry. The kernel is intrinsically sequential at the step boundary; this is the **outer-loop `sequential-obstruction`** documented above, and is why `krylov-step` is consumed by a tail-recursive `iterate_while_L3` at L3, not by a parallel reduction.
- **Linearity in any single argument**. Inherited from the chain. `krylov-step op (α·K_1 + β·K_2) s ≠ α · krylov-step op K_1 s + β · krylov-step op K_2 s` in general, because the scalar-stratum update inside `krylov_update` involves divisions (`α = β / dot(Ap, p)`) and the convergence flag involves a comparison — neither is linear. Built from linear primitives at L1, but their composition with `dot` and scalar arithmetic destroys linearity at the L3 form's kernel level.
- **Bit-determinism across orthogonalization variants**. Inherited from the chain. Switching `op.orthog` from MGS to CGS to CGS2 produces mathematically-equivalent (under exact arithmetic) but bit-distinct carry trajectories. Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra"; the variant choice is a *different algorithm* in floating-point even though it is "the same `krylov-step`" at the L3 schema level.
- **Form-equivalence-under-positional-rebinding**. Form A and Form B (Form-B = `krylov-step-first` + `krylov-step-steady`) produce iteration-for-iteration-identical carry trajectories per `concepts/first-iteration-unrolling.md` §"What is preserved", but they are **not** related by an L3-calculus rewrite using only positional rebinding (the rotation is a structural rewrite that drops a `K`-bundle field and threads a `carry` positional argument; it is not a name-substitution). The `(first, steady)` pair is a different `krylov-step` shape at L3, not a syntactic variant of Form A. Inherited from L4 per the upstream theme.
- **Outer-loop lift to a single tensor-field op**. The trajectory of carries `(K_0, s_0), …, (K_n, s_n)` does not lift to a closed-form whole-tensor operation in `n` steps, because each step's scalar update depends on the previous step's iterate-bundle through inner products that are not closed-form in the carry. This is the outer-loop `sequential-obstruction` of L3 — the body is L3-native (whole-tensor primitives), but the fold over the body is not. Documented at `book/src/spec/slices/cg.md:341-349` and `book/src/spec/slices/arnoldi_step.md:194-213`. The L3 form names the loop tail-recursively; it does not claim the trajectory lifts.

## Dependencies

**Same-layer (L3)**: no other L3 operators exist yet (this is the first firm L3 entry); the body references the L3-native whole-tensor primitives by their L1 names (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) — these are L3-native by signature shape (each operates on whole tensors with no element loop exposed), and their L1 entries serve as the citation anchors. As more L3 operators land, this section will reference them directly.

**Cross-cutting concepts** (consumed unchanged across the chain):

- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the iteration-rotation marker for the **outer loop** that folds `krylov-step`; the body itself does not carry an obstruction.
- [`state-stratification`](../concepts/state-stratification.md) — the three-stratum partition discipline (typed records at L4; positional values at L3; documented field partition over `IterState` at L2).
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra underwriting Law 1.
- [`variant-absorption`](../concepts/variant-absorption.md) — the level-(b)/(c) absorption discipline; at L3 a documented invariant (no `readonly` typing).
- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the Form-A/Form-B distinction (positional carry-threading at L3).
- [`convergence-test`](../concepts/convergence-test.md) — the stopping-predicate surface consumed by the outer `iterate_while_L3` loop, not by the kernel body.
- [`solve-monad`](../concepts/solve-monad.md) — the L4 outer-driver surface; at L3 dissolved to positional `s`-threading per the upstream theme.
- [`solver-as-operator`](../concepts/solver-as-operator.md) — the consumer-side framing.
- [`apply_BA`](../concepts/apply_BA.md) — the constructed-operator preconditioner surface.
- [`orthogonalization`](../concepts/orthogonalization.md) — the orthogonalize composition (the source of the below-body MGS obstruction).
- [`constructed-operators`](../concepts/constructed-operators.md) — the level-(c) absorption of `op.T`'s preconditioner-side variant.

**Strawman reference**: `book/src/design/l4_calculus.md` §3.7 is the conventions source for the surrounding `iterate_while` shape; the L3 rendering of `iterate_while` (tail-recursive value-threading) is published as the L3 form in [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"What the L3 form for `iterate_while` looks like".

No L4 monadic vocabulary appears in the L3 signature (no `Solve`, no `modify`, no `do`-block) — the dissolution is complete at L3 per the upstream theme. No L2 unified `IterState` record appears (the L3 form keeps the `(K, s)` positional split; the consolidation happens at the L3>L2 hop). That is the discipline of the layer.

## Variant axes

Inherited unchanged from the L4 / L2 entries at six. All absorbed at construction time (per [`variant-absorption`](../concepts/variant-absorption.md)) and do not appear in the per-step body's positional signature:

1. **preconditioner present/absent** — absorbed at level (c) into `op.T` (the constructed `apply_BA`). At L3 the absorption is a documented invariant (no `readonly` typing).
2. **orthogonalization variant** (`gs_orthog ∈ {MGS, CGS, CGS2}`) — absorbed at level (b) into `op.orthog`. Present iff the slice uses an orthogonalize stage (GMRES, Arnoldi); absent in CG and Chebyshev. **Below-body sequential-obstruction**: the MGS variant carries a sequential obstruction inside `op.orthog` per `book/src/spec/slices/arnoldi_step.md:194-213`; this obstruction is below `krylov-step`'s body — the kernel sees `op.orthog` as an opaque closure.
3. **polynomial-kind** (`Chebyshev-4th | Chebyshev-1st`) — absorbed at level (c) into `op.scalars`. The closure-arity differs by variant (4th: `K.scalar_state = ()`; 1st: `K.scalar_state = { ρ_prev }`); the body sees a uniform call site.
4. **first-iteration-unrolled vs. branch-in-body** — selected at the L3 form level (Form A vs Form B); Form B adds a `carry` position to the tuple signature. The two forms produce trajectory-identical carries; the choice is a presentation rotation per `first-iteration-unrolling`. Inherited from L4 with the closure-vs-state distinction dissolved into positional carry-threading.
5. **restart shape** (`non-restarted | restarted-fixed-dim | restarted-adaptive`) — restart logic lives in the outer `solve_loop` at L4 / outer-driver-by-role at L3; the kernel body is restart-agnostic. The `K`-bundle's "born at restart, discarded at restart" lifecycle is a documented invariant at L3 (no typing enforcement).
6. **in-place vs. out-of-place buffer use** — transparent performance-equivalent below L3 per CLAUDE.md §"Optimization tricks". The L3 form is uniformly out-of-place (a fresh `K'` is returned); in-place specialisation reappears in the L2>L1 lowering, then the L1>L0 lowering, depending on the primitive (see e.g., `book/src/L1-L0/axpby-mutation-rotation.md`).

The variant-axis count of six matches the L4 and L2 entries exactly. No new axes introduced by the L3 rendering; no axes merged or split. The L4 `readonly` typing of variant absorption (axes 1, 2, 3, 5) **demotes** at L3 to a documented invariant; axis 4 is a presentation choice between Form A and Form B (positional at L3); axis 6 is a transparent rotation below L3's level of abstraction.

## Status

`firm` — value-threaded positional signature is the canonical iteration-rotation form for the per-step Krylov body; algebraic laws are the same three that survive the chain (with state-stratum non-aliasing rendered as a documented partition at L3); non-laws are catalogued explicitly including the outer-loop `sequential-obstruction` non-lift; variant-axis profile is closed at six, inherited unchanged. The pattern is well-attested via the chain: cycle-005 L2 firm-up (five slice corpus instances), cycle-006 L4 firm-up (typed wrapper), cycle-008 L4>L3 firm-up (wrapper dissolution), cycle-009 L3>L2 firm-up (body identity). This dispatch (cycle-010 wave-1) is the **layer-coherence backfill** — the L3 form was previously published only as the RHS of the upstream theme; it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md, cycle-009 meta-phase).

## Lowers to

L3 `krylov-step` lowers to L2 [`krylov-step`](../L2/krylov-step.md) via the firm L3>L2 theme [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md). The body's let-chain maps line-for-line to L2; two surface adjustments at the wrapper around the body (L3 `(op, K, s)` positional tuple consolidates into L2 unified `IterState`; L3 tail-recursive outer loop collapses to L2's outer-driver-by-role reference) are information-preserving. The body is identity-in-form across this edge.

## Lifts from

L3 `krylov-step` lifts from L4 [`krylov-step`](../L4/krylov-step.md) via the firm L4>L3 theme [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md). The wrapper-dissolution is substantive **at the wrapper** (typed three-stratum records dissolve to positional values; `Solve` monad dissolves to explicit `s`-threading; `OpParams` `readonly` demotes to documented invariant; Form-A/B presentation collapses to positional carry-threading); the kernel body's primitive sequence is **value-thread-isomorphic** between the L4 form and this L3 form.

**The L4 form is value-thread-isomorphic to this L3 form.** The L4>L3 typed-wrapper-dissolution theme (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) makes the dissolution explicit; after dissolution, the bodies are identical modulo notation (L4's `do`-block plus `modify` becomes L3's `let`-chain plus explicit record-update; L4's typed records become L3's positional values). **This L3 entry exists for layer-coherence reasons** — a reader navigating L3 must find `krylov-step` defined in L3 vocabulary, not have to reach up to L4. The cycle-006 audit verdict "no L3 row needed for krylov-step" (on identity-in-form grounds) is **superseded** by the methodology invariant **Identity-lowerings still require both L levels** codified cycle-009 meta-phase (CLAUDE.md §Methodology invariants). This entry is the first cycle-010 enactment of the invariant; priority #20 (identity-lowering-both-levels-backfill) tracks the broader follow-on audit.

## Evidence

The L3 form is value-thread-isomorphic to the L4 body (per the upstream theme's audit verdict); all L0 evidence is transitive through L4 / L2. Direct citations relevant to this L3 entry:

- `book/src/L4/krylov-step.md` (cycle-006 firm) — the L4 typed-wrapper form this L3 entry value-thread-rewrites. Body shape, semantics (effect placement, three placements made structural by the typing), variant axes (six), algebraic laws (three that hold; non-laws catalogued).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-008 firm) — the wrapper-dissolution theme. §"L3 form (RHS)" (lines 55-89) is where this L3 form is first published; §"Audit of cycle-002 identity-in-form claim" (lines 202-220) is the verdict supporting the value-thread-isomorphism. §"What the L3 form for `iterate_while` looks like" (lines 158-201) renders the surrounding outer loop at L3 with the §3.8 demand-pruning rule cited; the pruned shape is the load-bearing one for Palace's KSP consumer surface (Condition 5 of the theme).
- `book/src/L2/krylov-step.md` (cycle-005 firm) — the L2 primitive-composition form this L3 entry lowers to. The body's let-chain maps line-for-line per the L3>L2 theme.
- `book/src/L3-L2/krylov-step-body-identity.md` (cycle-009 firm) — the L3>L2 theme that ratifies the L3 body's identity-in-form rotation to L2. The §"Rewrite shape" line-by-line table is the operational evidence.
- `book/src/spec/slices/cg.md:341-362` — the cycle-002 combinator-miner identity-in-form claim (Claim 2: "step body lifts as identity"). The L2 primitive vocabulary is L3-native by signature shape; this is the upstream evidence for both the L4>L3 wrapper-dissolution audit and the L3>L2 body-identity ratification.
- `book/src/spec/slices/arnoldi_step.md:178-213` — corroborating evidence for the Arnoldi step. Three uncontested primitives lift as identity; `op.orthog` under MGS carries the below-body sequential obstruction. Audited cycle-006; confirms the body's identity-in-form claim.
- `reference/palace/palace/linalg/iterative.cpp:22-32` — the L0 anchor for `CheckDot` (real overload at :22, complex overload at :28), the partial-function guard whose `BreakdownTag` propagates through `outputs.breakdown_token` at L3. Cited transitively via the L2 entry.
- `reference/palace/palace/linalg/iterative.hpp:52-55` — the four-scalar KSP result-extraction surface (`converged`, `initial_res`, `final_res`, `final_it`); the consumer-side anchor for Law 1's demand-pruning chain at the surrounding `iterate_while_L3`.
- `reference/palace/palace/linalg/ksp.cpp:296-310` — the sole consumer of the KSP result-extraction surface in `palace/`; per-iteration consumption is absent. Operational evidence that the §3.8 trajectory pruning at the surrounding outer loop fires under Palace's consumer pattern.

Five Phase-1 slice instances (per combinator-miner cycle-002; inherited via the L2 entry):

- `book/src/spec/slices/cg.md:103-115`, `:172-188`, `:393-425` (CG L2 / L4 / L4-v0.5 step bodies; the L3 form is the wrapper-dissolved image of the L4 body).
- `book/src/spec/slices/gmres.md:459-471` (GMRES L4 `inner_loop` body).
- `book/src/spec/slices/chebyshev.md:354-362` (Chebyshev L4 `innerStep`).
- `book/src/spec/slices/arnoldi_step.md:99-105`, `:285-298` (L1 Arnoldi step + L4 monadic form).
- `book/src/spec/slices/polynomial_recurrence_step.md:119-160` (catalog of three polynomial-recurrence sites; the L3 form is the value-thread-isomorphic image of each).

Outer-driver consumer sites at L3 (the tail-recursive `iterate_while_L3` invocations that fold `krylov-step`):

- `book/src/spec/slices/cg.md:208-220, :430-446` (CG `cg_solve` calling the L4 `iterate_while` / `iterate_while_with_prev`; at L3 these dissolve to the tail-recursive form per the upstream theme).
- `book/src/spec/slices/gmres.md:430-454` (GMRES restart/inner-loop nested folds; at L3 each fold dissolves independently).
- `book/src/spec/slices/chebyshev.md:330-353` (Chebyshev `apply`; at L3 the `forM_` and `foldM` dissolve to tail recursions).

Cycle-004 obstruction-theme guidance (inherited from L2; not consumed as new evidence here):

- `book/src/L1-L0/minres-iteration.md` — MINRES is the symmetric specialisation of `arnoldiStep`; its `lanczos_step` at L3 would be a specialisation of this `krylov-step` with the orthogonalization-variant axis collapsed to a band-3 form.
- `book/src/L1-L0/bicgstab-iteration.md` — BiCGStab's `bicgstab_step` at L3 would be a specialisation with two `apply_linop` calls per step (instead of one); this changes Law 2's count but does not add a new variant axis.

## L3 vs L4 distinction

- **L4**: typed-wrapper Krylov step kernel against the three-stratum state record. Records are typed (`SimState`, `OpParams`, `Krylov`); the `Solve = StateT SimState Identity` monad threads `SimState`; `OpParams readonly` typing forbids variant re-inspection; Form-A vs Form-B is a presentation choice between `iterate_while`-consumer and `iterate_while_with_prev`-consumer.
- **L3**: value-threaded Krylov step kernel against positional values. The three pieces (`op`, `K`, `s`) are positional in the signature; the `Solve` monad has dissolved; the `readonly` typing has demoted to a documented invariant; Form-B is a `carry` position in the tuple. The kernel body's primitive sequence is value-thread-isomorphic to L4; only the wrapper differs.

## L3 vs L2 distinction

- **L3**: value-threaded positional form `(op, K, s) -> (K', s', outputs)`. The iteration view is load-bearing — the outer tail-recursive loop is rendered explicitly per the surrounding `iterate_while_L3`, and the kernel's outer-loop `sequential-obstruction` is named explicitly. The three strata (`op`, `K`, `s`) are positional values.
- **L2**: primitive-composition form `(op: OpParams, s: IterState) -> { state: IterState', outputs: StepOutputs }`. The iteration view is erased — the outer driver is referenced by role only. The three strata are consolidated into a unified `IterState` record with a documented partition (per `state-stratification`).

The L3>L2 hop consolidates `(K, s)` into `IterState` and collapses the explicit outer-loop tail recursion to outer-driver-by-role; the body's let-chain is identity-in-form per [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md).

The three layers' entries share variant-axis count, primitive-call count, and the cited slice corpus. They differ in **wrapper rendering**: L4 typed-wrapper-with-monad, L3 positional-value-threaded, L2 unified-record-with-outer-driver-by-role. The cross-layer chain L4 > L3 > L2 lowers each wrapper to the next, with the body identity-in-form throughout.
```

```edit:book/src/L3/index.md
# L3 — Global tensor-field operations

L2 algebraic decompositions re-expressed as global tensor-field / convolution-over-space operations: whole-tensor ops, no element loops. The **iteration rotation** layer.

## Context

Where the L2 algebra admits a global form, L3 captures it. Where no global form exists (Gauss-Seidel-flavored smoothers, certain triangular solves, sequentially-reordered preconditioners), the **obstruction** is recorded as a first-class output — negative L3 results are part of the deliverable.

## Semantics (overlay)

L3 expresses:
- Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)
- Field transitions: state evolution over a single algorithmic step expressed as `state' = f(state, params)`
- Convolution-like patterns where applicable (stencil sweeps, restriction/prolongation)
- Sequential obstructions: explicit markers where global form is unavailable, with reason

## Operator dep-map

| Operator | Signature | Dependencies | Lowers to | Status |
|---|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | Form A: `(op, K, s) -> (K', s', outputs)`. Form B: `krylov-step-first :: (op, K, s) -> (K', s', carry, outputs)` + `krylov-step-steady :: (op, K, s, carry) -> (K', s', carry', outputs)`. | L1 primitives (used as L3-native whole-tensor ops): `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`. Concepts: `sequential-obstruction`, `state-stratification`, `derived-view-hoisting`, `variant-absorption`, `first-iteration-unrolling`, `convergence-test`, `solve-monad`, `apply_BA`, `orthogonalization`. L4 lift via `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (identity-in-form on body). | L2 [`krylov-step`](../L2/krylov-step.md) via [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) (identity-in-form on body; surface adjustments consolidate `(K, s)` into `IterState`). | `firm` (harvested cycle-010T215300Z; first firm L3 operator; identity-lowering backfill per CLAUDE.md §Methodology invariants — supersedes cycle-006 "no L3 row needed" verdict) |

## Working Notes

- This layer is the destination of the L2-L1 lowering pipeline output AND the source for L4-L3 lowering verification.
- `concepts/sequential-obstruction.md` is the canonical write-up of when L3 lifts fail.
- **First firm L3 operator landed cycle-010**: `krylov-step` (identity-lowering backfill per CLAUDE.md §Methodology invariants new bullet **Identity-lowerings still require both L levels**, codified cycle-009 meta-phase). The L3 form is value-thread-isomorphic to the L4 body per the L4>L3 typed-wrapper-dissolution theme; the entry exists for layer-coherence reasons — each layer is coherent within itself, and the L3 reader must find `krylov-step` defined in L3 vocabulary. Supersedes cycle-006 audit verdict "no L3 row needed for krylov-step".
- **Cohort growth candidates** (per priority #20 cross-layer-cross-cutter audit, cycle-010+): other operators in the krylov-step chain (`apply_linop`, `dot`, `axpy`, `nrm2`, etc.) may also have identity-in-form rotations between adjacent layers that warrant L3 backfill. Audit deferred to a `cross-layer-cross-cutter`-scoped dispatch surveying the L4/L3/L2/L1 cohorts.
```

```edit:book/src/SUMMARY.md
# Summary

[Introduction](./introduction.md)
# Methodology
- [Overview](./methodology/overview.md)
# L4 — Graph-Evaluation Calculus
- [Overview](./L4/index.md)
- [krylov-step](./L4/krylov-step.md)
- [iterate-while](./L4/iterate-while.md)
- [iterate-while-with-prev](./L4/iterate-while-with-prev.md)

# L4 > L3 — Lowering
- [Overview](./L4-L3/index.md)
- [krylov-step-typed-wrapper-dissolution](./L4-L3/krylov-step-typed-wrapper-dissolution.md)
- [gmres-inner-loop-iterate-while-migration](./L4-L3/gmres-inner-loop-iterate-while-migration.md)

# L3 — Global Tensor-Field Operations
- [Overview](./L3/index.md)
- [krylov-step](./L3/krylov-step.md)

# L3 > L2 — Lowering
- [Overview](./L3-L2/index.md)
- [krylov-step-body-identity](./L3-L2/krylov-step-body-identity.md)

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
- [ksp_solve](./L1/ksp_solve.md)
- [eigsolve](./L1/eigsolve.md)

# L1 > L0 — Lowering
- [Overview](./L1-L0/index.md)
- [axpby-mutation-rotation](./L1-L0/axpby-mutation-rotation.md)
- [axpbypcz-mutation-rotation](./L1-L0/axpbypcz-mutation-rotation.md)
- [apply-linop-mutation-rotation](./L1-L0/apply-linop-mutation-rotation.md)
- [ksp-solve-mutation-rotation](./L1-L0/ksp-solve-mutation-rotation.md)
- [bicgstab-iteration](./L1-L0/bicgstab-iteration.md)
- [minres-iteration](./L1-L0/minres-iteration.md)

# L0 — Cited Palace Source + Reference Notes
- [Overview](./L0/index.md)
- [Convention — output-arg vs receiver](./L0/output-arg-vs-receiver.md)
- [Convention — MFEM vector types](./L0/mfem-vector-types.md)
- [Convention — Par* types and single-rank reading](./L0/par-types-single-rank-reading.md)
- [Convention — linalg:: free-function wrappers](./L0/linalg-free-functions.md)
- [Convention — transparent vs load-bearing tricks](./L0/transparent-vs-load-bearing-tricks.md)
- [Convention — mutable workspace pattern](./L0/mutable-workspace-pattern.md)
- [File — palace/linalg/vector.{hpp,cpp}](./L0/linalg-vector-file.md)
- [File — palace/linalg/operator.{hpp,cpp}](./L0/linalg-operator-file.md)
- [File — palace/linalg/ksp.cpp](./L0/ksp-factory-file.md)
- [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)
- [File — palace/utils/communication.hpp (MPI collectives)](./L0/mpi-globalsum-and-collectives.md)
- [Overload set — Mult / MultTranspose / AddMult](./L0/apply-linop-overload-set.md)
- [Class — BaseKspSolver](./L0/kspsolver-base-class.md)
- [Class — MfemWrapperSolver](./L0/mfem-wrapper-solver.md)
- [Class — EigenvalueSolver and wrappers](./L0/eigensolver-wrapper.md)
- [Class — preconditioner classes overview](./L0/preconditioner-classes-overview.md)
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
  - [scalar-promotion](./concepts/scalar-promotion.md)

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

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[Annotation-only edit to the §"Audit of cycle-002 identity-in-form claim" section's "Consequence for L3 dep-map" paragraph. Strike the cycle-006 verdict that "no L3 `krylov-step` row is proposed" and replace with a backfill note pointing at the cycle-010 L3 entry. Find this paragraph (around lines 218 in the current file):

> **Consequence for L3 dep-map**: per the harvester's "Lowers to" section and per this audit, **no L3 `krylov-step` row is proposed**. The L4 entry lowers transitively to the L2 entry via this theme (L4>L3 wrapper dissolution) plus a one-line L3>L2 theme (identity-in-form on the body). The L4>L3 lowering produces an L3 form, but that L3 form is value-thread-isomorphic to the L2 form; there is no operational difference between "L3 `krylov-step`" and "L2 `krylov-step` with an outer `iterate_while` tail-recursion" — they are the same thing under two layer labels. Promoting an L3 row would duplicate content without adding semantic distinction.

Replace with:

> **Consequence for L3 dep-map** (cycle-006 verdict, SUPERSEDED cycle-010): per the harvester's "Lowers to" section and per this audit, the cycle-006 verdict was that **no L3 `krylov-step` row was proposed** on identity-in-form grounds. This verdict is **SUPERSEDED** by the user directive 2026-05-27 mid-cycle-009 codified as the CLAUDE.md §Methodology invariants bullet **Identity-lowerings still require both L levels**: each layer is coherent within itself, and an L3 reader must find `krylov-step` defined in L3 vocabulary at L3, even when the lowering is trivial. The L4 entry lowers transitively to the L2 entry via this theme (L4>L3 wrapper dissolution) plus a one-line L3>L2 theme (identity-in-form on the body, ratified at [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) cycle-009). **Cycle-010 backfill**: the L3 entry [`L3/krylov-step`](../L3/krylov-step.md) was authored cycle-010 wave-1 (`reports/2026-05-27T215300Z-harvester-l3-krylov-step/CYCLE.md`) per priority #20 (identity-lowering-both-levels-backfill); the L3 form is the wrapper-dissolution RHS rendered as a layer-coherent operator entry, not a duplicate of L2. The "operational difference" framing was a category error — the difference between "L3 `krylov-step`" and "L2 `krylov-step` with an outer `iterate_while` tail-recursion" is the **layer rendering**, not the operational content; both renderings are needed for their respective layers to be coherent.

The audit verdict itself (§"Audit verdict — confirmed-with-refinement") is unchanged — the body's identity-in-form property is what made the backfill *trivial*, not what made it *unnecessary*.]
```

```edit:book/src/L3-L2/krylov-step-body-identity.md
[Annotation-only edit to the §"Context" section's bullet about the L3 form, around lines 14-15 in the current file. The current bullet reads:

> - **L3 form** — published only as the RHS of `L4-L3/krylov-step-typed-wrapper-dissolution` §"L3 form (RHS)" (no standalone `L3/krylov-step.md`; the audit established that an L3 row would duplicate content). The L3 form is the value-threaded shape `(op, K, s) -> (K', s', outputs)` with the same five primitive groups as L2 in the same dataflow-forced order, plus an explicit `s' = s { it = s.it + 1 }` record-update line that is the dissolved `modify`.

Replace with:

> - **L3 form** ([`L3/krylov-step`](../L3/krylov-step.md), firm cycle-010) — value-threaded shape `(op, K, s) -> (K', s', outputs)` with the same five primitive groups as L2 in the same dataflow-forced order, plus an explicit `s' = s { it = s.it + 1 }` record-update line that is the dissolved `modify`. The L3 entry was previously published only as the RHS of `L4-L3/krylov-step-typed-wrapper-dissolution` §"L3 form (RHS)" — the cycle-006 audit established that an L3 row would duplicate content. **Cycle-010 backfill**: per the CLAUDE.md §Methodology invariants bullet **Identity-lowerings still require both L levels** (codified cycle-009 meta-phase), the L3 entry was authored as a layer-coherence anchor — the body is value-thread-isomorphic to the L4 body, but each layer is coherent within itself and the L3 reader must find `krylov-step` defined in L3 vocabulary at L3. The L3 entry is the LHS of this theme; the rewrite mapping in §"Rewrite shape" is unchanged.]
```

## Operator content

The full L3 entry content is contained in the first `edit:book/src/L3/krylov-step.md` block above. Section structure:

- **Frontmatter** — `layer: L3`, `operator: krylov-step`, `firmness: firm`, `lowers_to` (L2/krylov-step + L3-L2/krylov-step-body-identity), `lifts_from` (L4/krylov-step + L4-L3/krylov-step-typed-wrapper-dissolution), `variant_axes` (six axes with L3-vocabulary phrasing — positional carry, documented invariant, etc.).
- **Title + one-line** — "Value-threaded step kernel for iterative Krylov-shaped solvers at L3 — the iteration-rotation rendering of the per-step body."
- **Context** — narrates the layer-coherence rationale; cites the cycle-009 methodology codification; references upstream L4 and downstream L2 entries.
- **Signature** — Haskell `::` form. Form A: `(op, K, s) -> (K', s', outputs)`. Form B: `(op, K, s) -> (K', s', carry, outputs)` + `(op, K, s, carry) -> (K', s', carry', outputs)`. Shape contract enumerates the three positional values; documents the three absent L4 features (`Solve` monad, `readonly` typing, Form-A/B combinator distinction).
- **Semantics** — narrates the body's let-chain at L3 (operator apply, optional auxiliary, iterate-and-scalar update, derived-view readout, explicit counter increment). Each line corresponds to a distinct L3 primitive group. Sub-section "Iteration-rotation marker" surfaces the outer-loop sequential obstruction as the load-bearing L3 phenomenon (body is L3-native; outer loop is not).
- **Algebraic laws** — three laws that hold (output-extras distributivity, primitive-count invariance, state-stratum non-aliasing as documented partition). Seven non-laws catalogued (commutativity, associativity/fold-merge, identity element, step composition, linearity, bit-determinism across orthogonalization variants, form-equivalence-under-positional-rebinding, outer-loop lift to single tensor-field op).
- **Dependencies** — no same-layer L3 operators (this is the first); 11 cross-cutting concept references; the L4 strawman §3.7 referenced for the surrounding `iterate_while` shape.
- **Variant axes** — six axes inherited unchanged from L4 / L2, rendered in L3 vocabulary (positional rather than typed; documented invariants in place of `readonly` typing).
- **Status** — `firm`; layer-coherence backfill per cycle-009 methodology invariant; supersedes cycle-006 "no L3 row needed" verdict.
- **Lowers to** — L2/krylov-step via L3-L2/krylov-step-body-identity (identity-in-form on body; two surface adjustments at wrapper).
- **Lifts from** — L4/krylov-step via L4-L3/krylov-step-typed-wrapper-dissolution. **Explicit identity-in-form annotation per role-spec requirement**: "The L4 form is value-thread-isomorphic to this L3 form... This L3 entry exists for layer-coherence reasons... The cycle-006 audit verdict 'no L3 row needed' is superseded by the methodology invariant codified cycle-009 meta-phase."
- **Evidence** — chain citations (L4, L4-L3, L2, L3-L2) + cycle-002 combinator-miner identity claim source ranges + L0 anchors (`iterative.cpp:22-32` for `CheckDot`, `iterative.hpp:52-55`, `ksp.cpp:296-310`) + five Phase-1 slice instances + outer-driver consumer sites + cycle-004 obstruction-theme guidance (inherited).
- **L3 vs L4 distinction** — wrapper differences (typed vs positional; monadic vs value-threaded; readonly vs documented invariant).
- **L3 vs L2 distinction** — wrapper differences (positional `(op, K, s)` vs unified `IterState`; explicit tail recursion vs outer-driver-by-role).

## Supporting evidence

Primary sources (read in full for this dispatch):

- `book/src/L4/krylov-step.md` — cycle-006 firm L4 entry; the upstream typed-wrapper form. Used as the conceptual source for the body shape (which is value-thread-isomorphic to the L3 body per the upstream theme); variant-axis profile; algebraic laws.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — cycle-008 firm L4>L3 theme. §"L3 form (RHS)" (lines 55-89) is where the L3 body shape is first published; §"Audit of cycle-002 identity-in-form claim" (lines 202-220) establishes the value-thread-isomorphism between L4 body and L3 body. §"What the L3 form for `iterate_while` looks like" (lines 158-201) renders the surrounding outer loop at L3 with the §3.8 demand-pruning rule cited explicitly.
- `book/src/L2/krylov-step.md` — cycle-005 firm L2 entry. Used as the downstream reference for the algebraic-laws section (the three laws and seven non-laws); for the variant-axis enumeration (six axes); for the cited evidence base (five slice instances + L0 anchors).
- `book/src/L3-L2/krylov-step-body-identity.md` — cycle-009 firm L3>L2 theme. The §"Rewrite shape" line-by-line table is the operational mapping from the L3 body to the L2 body; used to confirm the body identity claim from the L3 side.
- `book/src/L3/index.md` — placeholder dep-map; the L3 layer's existing intro prose carried forward, dep-map updated with the new firm operator row.
- `book/src/design/l4_calculus.md` §3.7 (lines 150-184) and §3.8 (lines 186-213) — the strawman's `iterate_while` reduction rule (§3.7) and demand-driven pruning rule (§3.8). Referenced for the surrounding outer-loop semantics.

Secondary sources (consulted for cross-references):

- `book/src/L4/index.md` — L4 dep-map; confirmed the L4 `krylov-step` entry's dependencies and the relationship to `iterate-while` / `iterate-while-with-prev`.
- `book/src/L4/iterate-while.md` — cycle-007 firm L4 entry; the surrounding outer-loop combinator at L4 (whose L3 dissolution renders as tail-recursive value-threading).
- `book/src/L2/index.md` — L2 dep-map; confirmed the L2 `krylov-step` entry's status (`firm` since cycle-005).
- `scaffolding/priorities.md` priority #20 — the cycle-010 dispatch target: "first cycle-010+ target of priority #20 (identity-lowering-both-levels-backfill)".
- `scaffolding/friction-ledger.md` entries `identity-lowering-both-levels-required` and `l3-layer-empty-against-lower-vocabulary-priority` (added cycle-009 meta-phase). The codification of the methodology invariant.
- `CLAUDE.md §Methodology invariants` — the two relevant bullets ("Identity-lowerings still require both L levels"; "Layers are defined high→low; lifting notes go in working notes").
- `scaffolding/open-questions.md` slug `krylov-step-l3-identity-in-form-audit` (closed cycle-006 with answer-link `reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/`) and slug `krylov-step-l3-row-contingency` (closed cycle-006). Both closures predate the cycle-009 codification; both should be carried forward (no re-open) since their closures correctly recorded the cycle-006 verdict at the time. The cycle-010 backfill is a methodology-invariant-driven new line of work, not a reopening of the closed audit questions.

Inheritance trace for the L3 body shape (from the upstream theme's §"L3 form (RHS)"):

```text
krylov-step-L3 op K s =
  let w       = apply_linop op.T K.<input_field>
  let K_aux   = optionally apply op.orthog (K.V_prefix, w)
                or       apply op.scalars (K.k, K.scalar_state)
                or       K
  let K'      = krylov_update K_aux op w
  let outputs = derived_views K' op
  let s'      = s { it = s.it + 1 }
  in (K', s', outputs)
```

This shape is reproduced verbatim into the L3 entry's §Semantics. The L3 entry's body is the canonical L3 rendering of `krylov-step`; the upstream theme remains the LHS-to-RHS rewrite narrative (L4 form → L3 form), and the downstream theme remains the L3 form → L2 form ratification.

## Open questions / caveats

1. **`krylov_update` as a named sub-composition at L3** (caveat, not a blocker). The L3 form uses `krylov_update K_aux op w` as a single named binding for the iterate-and-scalar update primitive cluster, mirroring the upstream theme's §"L3 form (RHS)" rendering. At L2 this is split textually into two let-bindings (iterate-stratum + scalar-stratum). The two renderings are information-equivalent — `krylov_update` at L3 *is* the composition of the L2 entry's `axpy`-chain and `dot`-chain — but the naming-as-a-sub-composition is not anchored anywhere in the artifact. A future cycle could either: (a) firm `krylov_update` as a standalone L2 or L3 sub-operator (likely a tight composition of `axpy` / `axpby` / `axpbypcz` / `dot` / `nrm2`), or (b) document the split-at-L2 / unified-at-L3 rendering choice in the L3-L2 theme. Neither is blocking; the current L3 entry parallels the upstream theme's rendering. Routes to a future `combinator-miner` dispatch if the pattern recurs at additional L3 entries.

2. **L3 layer-intro refresh candidate** (out of scope; routing). `book/src/L3/index.md`'s "Semantics (overlay)" section currently lists three semantic motifs (whole-tensor primitives, field transitions, convolution-like patterns, sequential obstructions). The cycle-010 backfill adds a fourth observation — **value-threaded positional form for iteration-rotation kernels** — that could be lifted into the overlay. The L3 intro should also gain a Vocabulary-cohort subsection once the L3 cohort reaches the layer-intro-author's threshold (≥3 firm operators + ≥1 queued, per cycle-004 meta-phase template). Currently L3 has 1 firm operator (this dispatch); too early for the cohort subsection. Routes to a future `layer-intro-author` dispatch on L3 (cycle-010+; perhaps after 1-2 more L3 backfills land per the cross-layer-cross-cutter audit of priority #20).

3. **Identity-lowering audit follow-up** (priority #20 second target). The cycle-009 meta-phase priority #20 entry names a second target: "`cross-layer-cross-cutter` audit for additional backfill targets" — surveying the L4 / L3 / L2 / L1 cohorts for operators whose lower-layer form is identity-in-form to the upper-layer form but not explicitly landed at the lower layer. Candidates from inspection: at the L1 layer there is no obvious gap (every L1 entry has its own L1 file); at the L2 layer the `apply_BA` concept page is currently not landed as a firm L2 row, so a `concept→L2-row` lift might be in scope (separate from identity-lowering audits). The audit is **out of scope for this dispatch** — this dispatch is the first cycle-010 enactment of the priority, not the audit-dispatch. A future cycle-010+ `cross-layer-cross-cutter` dispatch (recommended scope: "audit identity-in-form gaps in L4-L3 / L3-L2 / L2-L1 / L1-L0 dependency chains").

4. **L3 entry's reference to `iterate_while_L3` as the surrounding outer loop** (citation accuracy). The L3 entry references `iterate_while_L3` (Form A) and the unpruned vs. pruned forms thereof multiple times, deferring the rendering to the upstream theme's §"What the L3 form for `iterate_while` looks like". The upstream theme has these forms anchored explicitly; this L3 entry does not re-render them. A future `same-layer-cross-cutter` dispatch could examine whether `iterate_while_L3` deserves its own standalone L3 entry (parallel to `L4/iterate-while`) — currently it is only published in the L4>L3 theme as a worked example. This dispatch did not pursue that question; the OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` (closed cycle-008 per the lifter dispatch) is the prior treatment.

5. **`book/src/L3/index.md` placeholder dep-map**. The L3 intro currently has `(empty — Phase B skeleton.)` as the dep-map. This dispatch's proposed-changes to `book/src/L3/index.md` replaces the placeholder with the first dep-map row (krylov-step). The current intro prose ("Context", "Semantics (overlay)") is carried forward unchanged — the layer-intro-author's broader L3 intro refresh (per caveat 2 above) is a separate future dispatch. No friction expected at integration.

6. **`book/src/SUMMARY.md` re-write scope**. The SUMMARY edit adds a single line (`- [krylov-step](./L3/krylov-step.md)`) under the L3 Part. The block is reproduced in full above for the integrator's convenience, but only the one line is new — all other entries are unchanged. The integrator should apply the diff as a one-line insertion if its tooling supports that; otherwise the full-file rewrite is offered above as the alternative format.

7. **No open-questions ledger entries proposed for this dispatch's content**. The L3 entry closes the gap identified by priority #20's first target (`book/src/L3/krylov-step.md` backfill). No new open questions are surfaced — the body's identity-in-form is well-established (cycle-006 audit; cycle-009 ratification at the L3>L2 hop); the variant-axis profile is closed at six; the algebraic laws and non-laws are inherited unchanged. The five caveats above are either methodology questions (caveat 3) or routing observations (caveats 1, 2, 4, 5, 6), not substantive open questions in the citation-grounded-evidence sense.
