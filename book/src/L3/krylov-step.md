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

Shape contract (positional values; L3 has no `readonly` annotation and no monadic effect; the solution-space shape group `S` and the square operator form `LinOp[(S: ...), (S: ...)]` follow the named-shape-group convention of [`l4_calculus`](../design/l4_calculus.md) §1.2.1–§1.2.2):

- **`op`** — operator-parameters value. Closure-captured by the body via the convention that `op` is the *first* positional argument and is never present in the return position; the value flows in, never out. The body reads `op.T` (the system operator, or constructed `apply_BA` per the preconditioner-side variant), the optional `op.orthog` (orthogonalization closure; present iff the slice uses Arnoldi / GMRES), and the optional `op.scalars` (scalar-generator closure; present iff the slice is polynomial-recurrence). Variant absorption is a **documented invariant at L3** — the kernel does not branch on any field of `op`; the variant selectors that L4 forbids by `readonly` typing are forbidden at L3 by convention and verified by inspection of the body. Slice-specific fields; this chapter does not enumerate them.
- **`K`** — iterate-bundle value. Carries the iteration-coupled fields that L4 partitions into the slice-specific ephemeral bundle: the iterate-side tensor fields (`K.<input_field>` — typically `K.r` for CG/MINRES, `K.p` for the basis-extension methods, `K.V[j]` for Arnoldi/GMRES), the basis-prefix `K.V_prefix` for orthogonalization, the polynomial-recurrence book-keeping `K.k`, `K.scalar_state`, and any per-step scalar carries (`K.α`, `K.β`, `K.ρ`, `K.ω`, `K.θ`). At L3 these are **positional fields of `K`**, not a typed record — the L3 calculus has no record-typing; `K` is a value whose internal structure is the slice's responsibility to keep consistent across the iteration.
- **`s`** — simulator-state value. Carries the persistent fields that L4 keeps in `SimState`: the iteration counter `s.it: Int`, the converged flag `s.converged: Bool`, the externally-visible iterate `s.x: Tensor[(S: ...)]` (touched at restart-cycle boundaries, not per step), and the scalar bookkeeping (`s.initial_res`, `s.final_res`). At L3 `s` is value-threaded explicitly — the L4 `Solve = StateT SimState Identity` monad has dissolved (per [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)"); `s` flows in as a positional argument, `s'` flows out as a positional return.
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

- **Operator apply** — `apply_linop op.T K.<input_field>` is one whole-tensor operator-application. The L3 form is L3-native by construction: `apply_linop` has signature `LinOp[(S: ...), (S: ...)] -> Tensor[(S: ...)] -> Tensor[S]` (a square operator on the solution-space shape group `S`; no element-loop exposed). The operator-apply count is the standard Krylov cost metric; at L3 it is structural (exactly one per step, modulo the constructed `apply_BA` per the preconditioner-side variant, which itself is one or two `apply_linop`s as documented in the slice-specific `apply_BA`).
- **Optional auxiliary stage** — present iff the slice's variant-axis profile selects it. GMRES / Arnoldi: `op.orthog (K.V_prefix, w)` dispatching on the orthogonalization variant. Chebyshev: `op.scalars (K.k, K.scalar_state)` producing the closed-form polynomial coefficients. CG: no-op (the auxiliary is identity-on-`K`). The dispatch is a single inlined closure invocation; the kernel body's textual shape does not branch on the variant — variant absorption at L3 is the documented invariant inherited from L4 (without the `readonly` typing). **Below-body sequential obstruction**: when `op.orthog` is the MGS variant, the inside of the orthogonalization carries a [`sequential-obstruction`](../concepts/sequential-obstruction.md) (the per-`i` sequencing of `H[i,j] ← ⟨w, V[i]⟩` and `w ← w − H[i,j] · V[i]`); this obstruction is **below `krylov-step`'s body** — the body calls `op.orthog` as an opaque closure — and is documented at [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"MGS as sequential-obstruction", not introduced by this entry.
- **Iterate-and-scalar update** — `krylov_update K_aux op w` is the sub-composition that updates the iterate-bundle's tensor-side fields and scalar-side fields. At L3 this is a single named sub-composition (mirroring the upstream theme's rendering); at L2 the same content is split into two textual let-bindings (iterate-stratum update via `axpy` / `axpby` / `axpbypcz`; scalar-stratum update via `dot` / `nrm2` plus scalar arithmetic). The L3 rendering treats them as one named update because at L3 the iteration view is what's load-bearing, not the stratum split — the stratum partition is documented at the consuming slice's `K`-record description per [`state-stratification`](../concepts/state-stratification.md). Each constituent primitive (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) is whole-tensor by signature shape — no element loop exposed at L3.
- **Output readout** — `derived_views K' op` is the demand-prunable projection from the post-step iterate-bundle plus the operator-parameters into the `outputs` record. Typical contents: `outputs.residual_norm = sqrt (abs K'.β)`; for GMRES `outputs.ls_residual = |K'.s[j+1]|`; for breakdown-guarding kernels `outputs.breakdown_token: BreakdownTag` per the L0 anchor `reference/palace/palace/linalg/iterative.cpp:22-32` (`CheckDot`; real overload at :22, complex overload at :28). The slot is governed by [`derived-view-hoisting`](../concepts/derived-view-hoisting.md): consumer-side reads of the surrounding `iterate_while`'s trajectory determine whether `derived_views` materializes the fields.
- **Counter increment** — `let s' = s { it = s.it + 1 }` is the **explicit record-update line** that dissolves the L4 `modify (\s -> s { it = s.it + 1 })`. At L3 this is the only line that reads or writes `s` in the per-step body; the L4 effect-localisation discipline (the kernel's effect domain is exactly `SimState`) survives as the convention "only the counter-increment line touches `s`". The simulator-state's iterate `s.x` is not updated per step — at restart-cycle boundaries the outer loop folds the correction `K.V · K.y` (GMRES) or the running iterate `K.x_running` (CG) into `s.x` exactly once. This placement is inherited from L4 per [`solve-monad`](../concepts/solve-monad.md) §"Worked example — GMRES", documented at L3 as a discipline.

The ordering of the five primitive groups is **forced by dataflow** — `apply_linop` produces `w`, which is read by both the auxiliary stage (`op.orthog`'s argument tuple, or `op.scalars`'s implicit residual access) and by `krylov_update`; the scalar-stratum update inside `krylov_update` depends on the iterate-stratum update if it reads the new residual; the output readout is downstream of both; the counter increment is independent of the body and could in principle commute with any pure binding, but is conventionally placed at the end of the let-chain so the textual sequence parallels L4's `do`-block.

The body is **stateless across calls** — `op` is closure-captured but never mutated; `K` and `s` flow in, `K'` and `s'` flow out as fresh positional values; the L1 primitives (`axpy`, `axpby`, `axpbypcz`) are pure at L1, with mutation reintroduced only in the L1>L0 lowering. This is what makes `krylov-step` foldable by an L3 tail-recursive outer loop (the value-thread-isomorphic image of L4's `iterate_while`; per the upstream theme §"What the L3 form for `iterate_while` looks like").

The body carries **breakdown signals** through `outputs.breakdown_token` (when present). The kernel itself does not branch on breakdown — the outer loop does, on inspection of `outputs.breakdown_token` per the [`convergence-test`](../concepts/convergence-test.md) discipline. The L4 form routes breakdown through `outputs` rather than `SimState`; the L3 form preserves this routing as a positional convention.

The body carries a **first-iteration branch** internally (Form A; CG v0.4) or is split into two named functions `krylov-step-first` and `krylov-step-steady` (Form B; CG v0.5; opt-in per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)). At L3 the Form-B variant adds a `carry` position to the tuple signature; the L4 closure-vs-state distinction has no operational meaning at L3.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `krylov-step`'s iteration view is the relationship between successive carries `(K, s) -> (K', s')`. **The body itself lifts as a whole-tensor operation** — every primitive in the let-chain is L3-native by signature shape. **The outer loop that folds this body does not lift** — the trajectory of carries `(K_0, s_0), (K_1, s_1), …, (K_n, s_n)` is intrinsically sequential because each step reads scalars (`α`, `β`, `ρ`, `ω`, `θ`) produced by the previous step, and the scalar dependence is not closed-form in the carry. The outer-loop sequentiality is the **outer-loop `sequential-obstruction`** documented at the firm [`sequential-obstruction`](../concepts/sequential-obstruction.md) concept page and corroborated by the live anchor `arnoldi_step.md:194-213` (the original CG evidence at `cg.md:341-349` was lifted into this §"Iteration-rotation marker" + the §"Algebraic laws" non-lift catalogue per the cycle-009 corpus reduction); it is a property of the surrounding `iterate_while_L3` tail-recursion, not of the `krylov-step` body itself. This entry's body is identity-in-form to the L2 body precisely because all sequentiality is pushed into the surrounding loop or below into the orthogonalization-MGS sub-primitive.

## Algebraic laws

The three laws that survive the full L4>L3>L2 chain hold at L3. Absences are catalogued explicitly to prevent decoration drift.

1. **Output-extras distributivity over trajectory** (the load-bearing law; inherited from [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)). For any field `f` of the `outputs` record such that `f = g(K')` for a pure function `g` of the post-step iterate-bundle, the trajectory observation `(iterate_while_L3 (krylov-step op) (K_0, s_0) p).trajectory.map(.outputs.f)` is equal to `(iterate_while_L3 (krylov-step op) (K_0, s_0) p).trajectory.map(.K).map(g)`. **Consequence**: if no downstream consumer reads `.outputs.f`, the L3 form is free to skip the `g` computation — the carry's `K` projection is unchanged. This is the demand-pruning law that underwrites the residual-norm hoisting and the §3.8 trajectory-accumulator pruning at the surrounding `iterate_while_L3` (per the upstream theme §"What the L3 form for `iterate_while` looks like"). At L3 the law is statable directly because the `outputs` record is a positional projection of `K'`; the §3.8 rule transports through the wrapper-dissolution because the body is value-thread-isomorphic to the L4 body. Witnessed by the consumer-side analysis at `reference/palace/palace/linalg/iterative.hpp:52-55` (four-scalar consumer surface) and `reference/palace/palace/linalg/ksp.cpp:296-310` (sole caller; per-iteration consumption absent in `palace/`).

2. **Primitive-count invariance under reformulation**. The number of `apply_linop` calls per step is a structural invariant of the slice's variant-axis profile — Form A and Form B of the L3 form have the same per-step `apply_linop` count (the `(first, steady)` split moves the branch, not the apply). Any reformulation that changes the count is a *different algorithm*. (CG: 1 per step. GMRES inner Arnoldi: 1 per step. Chebyshev inner k-loop: 1 per k. Arnoldi step: 1.) Inherited from the L4 entry by the value-thread-isomorphism of the body — the L4>L3 dissolution does not introduce or elide any `apply_linop` call.

3. **State-stratum non-aliasing as a documented partition**. At L3 the three strata — operator-parameters `op` (closure-captured; never returned), iterate-bundle `K` (positional input + output), simulator-state `s` (positional input + output) — are partitioned across the positional signature with **no cross-stratum aliasing**: the body's `let`-chain reads `op.*` and `K.*` to compute new `K'` fields, reads `s.it` only to increment it to `s'.it`, and never writes back to `op`. Consequence: a reordering of the iterate-and-scalar-update primitives inside `krylov_update` (subject to dataflow constraints) does not affect the counter-increment line, and vice versa — the counter increment commutes with any pure `K`-bundle binding, since `s.it` is never read inside the body. The L4 typing makes this structural via the typed record split; at L3 it is a documented partition over the positional carry, verified by reading the body. The discipline is information-equivalent to the L4 typing, just less mechanically checked.

Laws that explicitly **do not** hold:

- **Commutativity of the primitive sequence**. Inherited from the chain. The five primitive groups (apply, auxiliary, iterate-and-scalar update, output readout, counter increment) cannot be reordered without changing the value (modulo the counter-increment line, which is independent — see Law 3). The dataflow chain `apply_linop -> krylov_update` is rigid: `apply_linop` produces `w`, `krylov_update` reads it. The L3 form preserves this rigidity exactly.
- **Associativity / fold-merge**. Inherited from the chain. `iterate_while_L3 (krylov-step op) (iterate_while_L3 (krylov-step op) (K_0, s_0) p_1) p_2` is **not** equal to `iterate_while_L3 (krylov-step op) (K_0, s_0) (p_1 ‖ p_2)` for arbitrary predicates — the inner fold's `outputs` are not visible to the outer fold, and convergence predicates that depend on monotonic-loss properties do not generally compose. This is why restart logic is structured as an *outer* loop around the `krylov-step`-folding inner loop at L3 (per the GMRES outer restart loop, firm L0 `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C, `iterative.cpp:563-683`), not as a flattened single fold.
- **Identity element**. Inherited from the chain. There is no `K_id` such that `krylov-step op K_id s = (K_id, s', outputs)` in general. `α = 0` in CG is breakdown (the residual is exactly in the orthogonal complement of the Krylov subspace, signalling convergence or stagnation), not identity. The L3 form has no algebraic identity.
- **Step composition into a bigger step**. Inherited from the chain. Two successive `krylov-step` invocations do not simplify to a single `krylov-step` with combined parameters — the second step reads scalars produced by the first, and these scalars are not closed-form functions of the input carry. The kernel is intrinsically sequential at the step boundary; this is the **outer-loop `sequential-obstruction`** documented above, and is why `krylov-step` is consumed by a tail-recursive `iterate_while_L3` at L3, not by a parallel reduction.
- **Linearity in any single argument**. Inherited from the chain. `krylov-step op (α·K_1 + β·K_2) s ≠ α · krylov-step op K_1 s + β · krylov-step op K_2 s` in general, because the scalar-stratum update inside `krylov_update` involves divisions (`α = β / dot(Ap, p)`) and the convergence flag involves a comparison — neither is linear. Built from linear primitives at L1, but their composition with `dot` and scalar arithmetic destroys linearity at the L3 form's kernel level.
- **Bit-determinism across orthogonalization variants**. Inherited from the chain. Switching `op.orthog` from MGS to CGS to CGS2 produces mathematically-equivalent (under exact arithmetic) but bit-distinct carry trajectories. Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra"; the variant choice is a *different algorithm* in floating-point even though it is "the same `krylov-step`" at the L3 schema level.
- **Form-equivalence-under-positional-rebinding**. Form A and Form B (Form-B = `krylov-step-first` + `krylov-step-steady`) produce iteration-for-iteration-identical carry trajectories per `concepts/first-iteration-unrolling.md` §"What is preserved", but they are **not** related by an L3-calculus rewrite using only positional rebinding (the rotation is a structural rewrite that drops a `K`-bundle field and threads a `carry` positional argument; it is not a name-substitution). The `(first, steady)` pair is a different `krylov-step` shape at L3, not a syntactic variant of Form A. Inherited from L4 per the upstream theme.
- **Outer-loop lift to a single tensor-field op**. The trajectory of carries `(K_0, s_0), …, (K_n, s_n)` does not lift to a closed-form whole-tensor operation in `n` steps, because each step's scalar update depends on the previous step's iterate-bundle through inner products that are not closed-form in the carry. This is the outer-loop `sequential-obstruction` of L3 — the body is L3-native (whole-tensor primitives), but the fold over the body is not. Documented at the firm [`sequential-obstruction`](../concepts/sequential-obstruction.md) concept page and the live anchor `arnoldi_step.md:194-213` (the original CG evidence at `cg.md:341-349` was lifted into this non-lift catalogue + §"Iteration-rotation marker" per the cycle-009 corpus reduction). The L3 form names the loop tail-recursively; it does not claim the trajectory lifts.

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
2. **orthogonalization variant** (`gs_orthog ∈ {MGS, CGS, CGS2}`) — absorbed at level (b) into `op.orthog`. Present iff the slice uses an orthogonalize stage (GMRES, Arnoldi); absent in CG and Chebyshev. **Below-body sequential-obstruction**: the MGS variant carries a sequential obstruction inside `op.orthog` per [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"MGS as sequential-obstruction"; this obstruction is below `krylov-step`'s body — the kernel sees `op.orthog` as an opaque closure.
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
- `book/src/L3-L2/krylov-step-body-identity.md` §Verified-against (line 125; the cycle-002 combinator-miner Claim-2 verbatim quote was lifted there per the cycle-009 corpus reduction and is its terminal firm home) — the cycle-002 combinator-miner identity-in-form claim (Claim 2: "step body lifts as identity"). The L2 primitive vocabulary is L3-native by signature shape; this is the upstream evidence for both the L4>L3 wrapper-dissolution audit and the L3>L2 body-identity ratification.
- Arnoldi step — corroborating evidence for the Arnoldi step (firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop, within `iterative.cpp:563-683`). Three uncontested primitives lift as identity; `op.orthog` under MGS carries the below-body sequential obstruction (firm at [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md)). Audited cycle-006; confirms the body's identity-in-form claim.
- `reference/palace/palace/linalg/iterative.cpp:22-32` — the L0 anchor for `CheckDot` (real overload at :22, complex overload at :28), the partial-function guard whose `BreakdownTag` propagates through `outputs.breakdown_token` at L3. Cited transitively via the L2 entry.
- `reference/palace/palace/linalg/iterative.hpp:52-55` — the four-scalar KSP result-extraction surface (`converged`, `initial_res`, `final_res`, `final_it`); the consumer-side anchor for Law 1's demand-pruning chain at the surrounding `iterate_while_L3`.
- `reference/palace/palace/linalg/ksp.cpp:296-310` — the sole consumer of the KSP result-extraction surface in `palace/`; per-iteration consumption is absent. Operational evidence that the §3.8 trajectory pruning at the surrounding outer loop fires under Palace's consumer pattern.

Five Phase-1 slice instances (per combinator-miner cycle-002; inherited via the L2 entry):

- CG L2 / L4 / L4-v0.5 step bodies — firm-homed at `book/src/L2/krylov-step.md` §Evidence (the L2 terminal home, lowering to L0 Sub-pattern B `iterative.cpp:360-486`) and `book/src/L4/krylov-step.md` §Semantics Form A / Form B (the L4-v0.5 first-iteration-unrolling rendering absorbed into Form B cycle-099). The L3 form is the wrapper-dissolved image of the L4 body.
- GMRES `inner_loop` body — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`iterative.cpp:543-705`).
- `book/src/L4/chebyshev.md` §Semantics `innerStep` (firm cycle-015, absorbing the former `chebyshev.md:354-362` slice §L4).
- Arnoldi step + monadic form — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop (within `iterative.cpp:563-683`).
- `book/src/concepts/negative-result-slice.md` §Partial-positive sub-pattern + §Falsification criterion (catalog of three polynomial-recurrence sites — Chebyshev-4th, Chebyshev-1st, GMRES-Givens-stream; the L3 form is the value-thread-isomorphic image of each; Chebyshev-pair firm home `book/src/L4/chebyshev.md` §Semantics `innerStep`).

Outer-driver consumer sites at L3 (the tail-recursive `iterate_while_L3` invocations that fold `krylov-step`):

- CG `cg_solve` calling the L4 `iterate_while` / `iterate_while_with_prev` — firm-homed at `book/src/L2/krylov-step.md` §Evidence "Outer-driver consumer sites" (the L2 terminal home, lowering to L0 `BaseKspSolver::Mult` `ksp.cpp:296-310` wrapping the inner CG for-loop `iterative.cpp:427-464`) and `book/src/L4/krylov-step.md` Form B (the L4-v0.5 `cg_solve` driver with `iterate_while_with_prev`, absorbed cycle-099). At L3 these dissolve to the tail-recursive form per the upstream theme.
- GMRES restart/inner-loop nested folds (at L3 each fold dissolves independently) — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C outer restart loop (`iterative.cpp:563-683`).
- `book/src/L4/chebyshev.md` §Semantics `apply` (firm cycle-015, absorbing the former `chebyshev.md:330-353` slice §L4; at L3 the two `iterate_while_pure` folds dissolve to `iterate_while_pure_L3` tail recursions per `L3/chebyshev.md`).

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
