# ksp-solve-outer-driver

The L3>L2 lowering theme for the `ksp_solve` **outer-driver fold**. The rewrite is **substantive (non-identity)**: the L3 explicit value-threaded `iterate_while_L3` tail recursion — carrying the first-class **outer-loop `sequential-obstruction`** — dissolves into the L2 **outer-driver-by-role** wrap `iterate_while (krylov-step op) s_init predicate` over a unified `IterState`, and the iteration view is **erased** (the obstruction survives only as the L2 fold's non-mergeability / no-fold-lift non-laws). This is the **complement** of the sibling kernel theme [`krylov-step-body-identity`](./krylov-step-body-identity.md): there the kernel *body* is identity-in-form (the wrapper carries two information-preserving surface adjustments); here the loop *is* the operator, so the wrapper rotation is the whole content of the hop, and it is non-identity. `kernel-identity + driver-non-identity` is the full per-solver L3>L2 story.

## Slug

`ksp-solve-outer-driver`

## Context

The `ksp_solve` lowering chain stretches across the layer-edges of the artifact:

- **L1 firm** ([`L1/ksp_solve`](../L1/ksp_solve.md)) — the opaque solver-as-operator collapse `(K: Solver[A], b) -> SolveResult`; the loop and the kernel are both invisible (a solve is one indivisible operator application).
- **L2 firm** ([`L2/ksp_solve`](../L2/ksp_solve.md), firm cycle-021 wave-1) — the **outer-driver composition**: `(K, b) -> SolveResult` with body = the convergence-test fold of [`krylov-step`](../L2/krylov-step.md), the fold **named by role** (the iteration view erased). The RHS of this theme.
- **L2>L1 firm** (recorded in-line in the L2 entry's §"Lowers from") — the un-collapse of the L1 opacity into the kernel-fold composition; non-identity.
- **L3 firm** ([`L3/ksp_solve`](../L3/ksp_solve.md), firm cycle-020 wave-1) — the **iteration-rotation** view: the explicit value-threaded `iterate_while_L3` tail recursion `(op, K_0, s_0) -> (s_final, result)`, carrying the first-class outer-loop `sequential-obstruction`. The LHS of this theme.
- **L3>L2 firm — this theme.** Narrates how the L3 explicit fold lowers into the L2 outer-driver-by-role wrap. Substantive (non-identity): the iteration view is erased and the named obstruction shadows down to the L2 non-laws.

This theme is the **driver complement** of the kernel theme [`krylov-step-body-identity`](./krylov-step-body-identity.md). A Krylov solver's L3>L2 lowering has exactly two parts: the per-step kernel (identity-in-form on the body) and the per-solve driver loop (the substantive iteration-rotation erasure). The two themes together are the complete per-solver L3>L2 lowering. See §"Kernel-identity / driver-non-identity contrast".

## L3 form (LHS)

The L3 form is reproduced from [`L3/ksp_solve`](../L3/ksp_solve.md) §Signature — the value-threaded fold:

```text
ksp_solve :: (op, K_0, s_0) -> (s_final, result)
ksp_solve op K_0 s_0 =
  let s_init                = init_convergence op K_0 s_0     -- residual proxy + eps + converged_0
  let (K_n, s_n, outputs_n) = iterate_while_L3                -- the outer-driver fold (EXPLICIT tail recursion)
                                (krylov-step op)              --   body: the L3 kernel
                                (K_0, s_init)                 --   seed carry
                                (\s -> not s.converged && s.it < op.max_it)  -- predicate
  let s_final               = fold_iterate op K_n s_n         -- final iterate materialised into s.x
  let result                = extract_result s_final outputs_n -- the four-field readout
  in (s_final, result)
```

The L3 form is value-threaded (positional `(op, K, s)`; no `Solve` monad, no `readonly`, no L1 opacity) and the outer loop is rendered as an **explicit `iterate_while_L3` tail recursion**. It carries the **outer-loop `sequential-obstruction`** (per [`L3/ksp_solve`](../L3/ksp_solve.md) §"Iteration-rotation marker"): the trajectory `(K_0, s_0), …, (K_n, s_n)` does not lift to a closed-form whole-tensor operation, because each `krylov-step` reads scalars (`α`, `β`, `ρ`, `ω`, `θ`) produced by the previous step. This obstruction is the L3 entry's reason to exist — it is the load-bearing iteration-rotation content.

## L2 form (RHS)

The L2 form is reproduced from [`L2/ksp_solve`](../L2/ksp_solve.md) §Signature — the outer-driver composition:

```text
ksp_solve :: (K: Solver[A: LinOp[(S: ...), $S]], b: Tensor[$S]) -> SolveResult[S]
ksp_solve K b =
  let (op, s_0)     = setup K b                          -- bind kernel op-surface; seed state
  let s_init        = init_convergence op s_0            -- residual proxy + eps + pre-loop converged flag
  let s_n           = iterate_while                       -- the outer-driver fold (NAMED BY ROLE)
                        (\s -> (krylov-step op s).state)  --   body: the L2 kernel (state projection)
                        s_init                            --   seed
                        (\s -> not s.converged && s.it < op.max_it)  -- convergence predicate
  let s_final       = materialise_iterate op s_n          -- fold restart-cycle correction into s.x (identity for CG)
  in extract_result s_final                               -- the four-field SolveResult readout
```

The L2 form is the convergence-test fold of [`krylov-step`](../L2/krylov-step.md) over a unified `IterState` (the `s` argument; the L3 `(K, s)` split is consolidated into one record). The fold is **named by role** — the convergence-test / restart wrap of the kernel — **not** rendered as an explicit tail recursion. **No `sequential-obstruction` is named at L2** (the iteration view is erased per [`L2/index`](../L2/index.md) §Context). The obstruction survives only as the L2 §"Algebraic laws" non-laws: "Fold-merge / associativity" (the fold is not mergeable) and "Identity / lift of the fold to a single tensor-field op at L2" (the fold does not collapse to a closed-form composition).

## Rewrite shape

The rewrite is the **substantive erasure of the iteration view**, with one supporting consolidation. There is no "body" subject here (the kernel body is the sibling theme's subject); the whole content of this hop is the loop's surface.

1. **The L3 explicit `iterate_while_L3` tail recursion dissolves into the L2 `iterate_while` outer-driver-by-role wrap.** At L3 the loop is rendered as an explicit value-threaded tail recursion (per [`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"What the L3 form for `iterate_while` looks like" and the strawman `book/src/design/l4_calculus.md` §3.7 conventions). At L2 the loop is referenced **by role** — the convergence-test / restart wrap of [`krylov-step`](../L2/krylov-step.md) — not rendered as recursion. This is the same surface adjustment the kernel theme names for its wrapper ("the L3 tail-recursive outer loop collapses to L2's outer-driver-by-role reference"); but for `ksp_solve` **the loop IS the operator**, so this surface adjustment is not a wrapper change around an identity body — it is the entire rotation.

2. **The outer-loop `sequential-obstruction` erases from the surface, shadowing to the L2 non-laws.** This is the load-bearing forward-narration step. At L3 the obstruction is named and first-class (the iteration does not lift). At L2 the iteration view is erased, so the obstruction is **not expressible** at the surface — but it is not *gone*: it survives as the L2-vocabulary residue in two §"Algebraic laws" non-laws of the L2 entry:
   - "Fold-merge / associativity" does not hold (the fold cannot be merged) — the L2 statement of "the iteration is sequential," without naming the iteration.
   - "Identity / lift of the fold to a single tensor-field op at L2" does not hold (the fold does not collapse to a closed-form composition) — the L2 statement of "the trajectory does not lift to a whole-tensor op," without naming the trajectory.
   The L2 entry itself states this explicitly: "the *iteration-rotation* statement of it (the outer-loop `sequential-obstruction`) is the [`L3/ksp_solve`] concern, where the iteration view is load-bearing." This theme is the forward narration of that handoff: **obstruction named at L3 → obstruction erased to its non-law shadow at L2.**

3. **The L3 `(op, K_0, s_0)` positional triple consolidates into the L2 `(K, b)` + unified `IterState` surface (supporting consolidation).** The L3 form threads `op` (closure-captured params), `K` (ephemeral iterate-bundle), and `s` (simulator-state) positionally; the L2 form takes the construction-bound `K: Solver[A]` and RHS `b`, destructures `K` into the kernel op-surface `op` and loop-shaping fields via `setup`, and threads a single `IterState` `s` through the fold. The L3 `(K, s)` split merges into the L2 `IterState` exactly as in the kernel theme's surface-adjustment (1); the L3 `op` becomes the `setup`-extracted op-surface. **Information-preserving** — no field is added or dropped; the merge erases the L3 ephemeral-vs-persistent typing distinction, which becomes a documented stratification partition at L2 (per [`state-stratification`](../concepts/state-stratification.md)). This consolidation is supporting, not the substantive content — the substantive content is (1)+(2), the iteration-view erasure.

The mapping at the fold's structural level:

| L3 line | L2 line | Mapping |
|---|---|---|
| `let s_init = init_convergence op K_0 s_0` | `let (op, s_0) = setup K b` + `let s_init = init_convergence op s_0` | Supporting consolidation. The L3 closure-captured `op` becomes the L2 `setup`-extracted op-surface; `init_convergence` is unchanged (same residual proxy, same `eps = max(rel_tol·initial_res, abs_tol)`, same pre-loop `converged = (res < eps)`). L0 anchor `iterative.cpp:417-418`. |
| `let (K_n, s_n, outputs_n) = iterate_while_L3 (krylov-step op) (K_0, s_init) predicate` | `let s_n = iterate_while (\s -> (krylov-step op s).state) s_init predicate` | **Substantive (non-identity).** The L3 EXPLICIT tail recursion over the `(K, s)` carry dissolves into the L2 NAMED-BY-ROLE fold over the unified `IterState`. The iteration view is erased: L3 renders the recursion, L2 references it by role. The predicate (`\s -> not s.converged && s.it < op.max_it`) is identical (L0 loop guard `iterative.cpp:427`; per-step `converged = (res < eps)` at `:463`). **This is the line where the iteration-rotation is erased — the heart of the hop.** |
| (the `sequential-obstruction` named in §"Iteration-rotation marker") | (no surface statement; shadows to §"Algebraic laws" non-laws) | **Substantive (non-identity).** The L3 first-class obstruction is **erased** from the L2 surface (no explicit iteration to attach it to) and survives only as the L2 "fold-merge / associativity" and "identity / lift of the fold" non-laws. |
| `let s_final = fold_iterate op K_n s_n` | `let s_final = materialise_iterate op s_n` | Identity (renamed). Same final-iterate materialisation: identity for non-restarted (CG/Chebyshev); folds the last partial restart-cycle correction `K.V · K.y` for restarted (GMRES/FGMRES). |
| `let result = extract_result s_final outputs_n` + `in (s_final, result)` | `in extract_result s_final` | Identity (re-bundled). Same four-field readout (`converged`/`iterations`/`initial_res`/`final_res`) from the terminal carry; the L3 returns the pair `(s_final, result)` with `s_final.x` carrying the solution, the L2 folds `x` into the `SolveResult[S]` record. The `SolveResult` boundary content is the same (L0 result-write tails CG `:484-485`, GMRES `:703-704`; `GetConverged()` gate `iterative.hpp:98`). |

The mapping is total on the fold's structure, but it is **not** the identity-in-form mapping of the kernel theme: the central line (the fold) carries a genuine rotation (explicit recursion → role reference), and the obstruction line carries a genuine erasure (named → non-law shadow). These two are the non-identity content; the surrounding lines (init / materialise / extract) are identity modulo the supporting `(op, K, s)` → `(K, b)`/`IterState` consolidation.

## Applicability conditions

The rewrite is valid when all of the following hold (satisfied for the firm L3 and L2 forms by construction):

1. **The L3 form is the firm `L3/ksp_solve` outer-driver fold** — the explicit `iterate_while_L3` tail recursion over [`krylov-step`](../L3/krylov-step.md) with the named outer-loop `sequential-obstruction`. If a future Krylov-shaped slice (MINRES, BiCGStab — currently obstruction-only per [`L1-L0/minres-iteration`](../L1-L0/minres-iteration.md), [`L1-L0/bicgstab-iteration`](../L1-L0/bicgstab-iteration.md)) is firmed at L3 with a different loop structure, the erasure narration would need re-audit against the new loop. Per the unimplemented-Palace-stub policy these are not implementation targets, so re-audit is not currently planned.
2. **The L2 form is the firm `L2/ksp_solve` outer-driver composition** — the convergence-test fold of [`krylov-step`](../L2/krylov-step.md) named by role, with the iteration view erased per [`L2/index`](../L2/index.md) §Context, and the L3 obstruction's shadow present as the two §"Algebraic laws" non-laws. The firm L2 entry's §"Lifts to" records the reverse (L2 role-reference ⟷ L3 explicit fold) in-line; this theme narrates the forward L3→L2.
3. **The kernel body's L3>L2 rotation is the sibling identity theme.** This theme covers only the driver loop; the per-step kernel body is [`krylov-step-body-identity`](./krylov-step-body-identity.md). The two are disjoint and complementary (see §"Kernel-identity / driver-non-identity contrast"); neither subsumes the other. The clean division relies on the kernel/driver factoring being stable, which it is for the five-slice corpus (CG, GMRES, FGMRES, Chebyshev, divfree-CG).
4. **The variant-axis profiles are complementary.** The L3 driver's five loop-shaping axes {krylov-method, element-type, initial-guess-policy, convergence-failure-policy, **restart-shape**} shape the *fold*, not the kernel body; the L2 driver's six loop-shaping axes {solver-method, element-type, preconditioner-side, convergence-criterion, initial-guess-policy, convergence-failure-policy} likewise shape the fold. The relationship across the hop is **four shared** (element-type, initial-guess-policy, convergence-failure-policy, and L3 krylov-method ≡ L2 solver-method) plus **restart-shape folded into solver-method** (the L3 restart-shape variant collapses into the L2 solver-method axis — it does *not* survive as a separate L2 axis) plus **two new at L2** (preconditioner-side, convergence-criterion). So `L2 six = four-shared + restart-shape-folded-into-solver-method + two-new`, not `L3 five + 2`. Both forms close over the loop-shaping selectors; neither branches on the kernel body. The rotation does not interact with the kernel's six body-variant axes (those are the sibling theme's concern).

## Justification kind

**`structural`** (dominant) with secondary **`reduction-chain`**.

**Structural (dominant)**: the non-identity content is a structural fact about the layer surfaces — L3 renders the iteration explicitly (a tail recursion is a structural form), L2 erases the iteration view to a role reference (a structural absence). The `sequential-obstruction`'s erasure-to-non-law-shadow is structural: the obstruction is a property of the explicit iteration structure, so erasing the structure erases the named obstruction, leaving only the L2-expressible residue (the non-mergeability / no-fold-lift non-laws). This is a claim about the shapes of the two forms (explicit recursion vs. role reference; named obstruction vs. non-law shadow), not about algebraic laws or step-semantics — hence structural. The contrast with the kernel theme (identity-in-form on the body) is itself a structural observation: the body's primitive sequence is shape-invariant across the hop, the loop's iteration view is not.

**Reduction-chain (secondary)**: the `iterate_while_L3` → `iterate_while`-by-role consolidation is grounded in the small-step `iterate_while` semantics from the strawman `book/src/design/l4_calculus.md` §3.7 — the L3 tail recursion is the unfolded reduction sequence of the `iterate_while` combinator, and the L2 role reference is the folded (un-unfolded) form. The forward L3→L2 narration re-folds the explicit reduction sequence back into the named combinator-by-role. The §3.8 trajectory-accumulator demand-pruning (cited in the L4>L3 theme and inherited by the L3 entry) governs the result-extraction line's identity-modulo-pruning. This is the reduction-chain backing for the central fold line; it is secondary because the load-bearing content (the iteration-view erasure + obstruction shadow) is structural.

**Abstraction-direction note**: L3 is the higher-abstraction layer for this edge (it has the iteration rotation done and the obstruction named); L2 is the lower-abstraction layer (it leaves the iteration view to the consumer and erases the explicit loop). The rotation direction is L3 → L2: the L3 form lowers to the L2 form by **dissolving** the explicit tail recursion into the outer-driver-by-role reference and **erasing** the named obstruction to its non-law shadow. This matches the methodology's high→low lowering direction; the reverse (how the L2 role-reference un-erases into the L3 explicit fold + obstruction) is a working-note / OQ concern, recorded only in the L2 entry's §"Lifts to" in-line, not narrated here.

## Speculative L3 operators

**None.** This theme is the substantive erasure rotation between two firm endpoints; no new L3 vocabulary is introduced. The L3 form referenced in the LHS is the firm [`L3/ksp_solve`](../L3/ksp_solve.md) entry; the L2 form referenced in the RHS is the firm [`L2/ksp_solve`](../L2/ksp_solve.md) entry. The `iterate_while_L3` / `iterate_while` combinators are firm (`book/src/L4/iterate-while.md`, firmed cycle-007); they are referenced, not introduced. The `krylov-step` kernel both endpoints fold is firm at both layers ([`L3/krylov-step`](../L3/krylov-step.md), [`L2/krylov-step`](../L2/krylov-step.md)).

## Kernel-identity / driver-non-identity contrast

The two L3>L2 themes for a Krylov solver divide labour by subject, and the division resolves the cycle-020 critic's "mild tension" cleanly:

- **[`krylov-step-body-identity`](./krylov-step-body-identity.md) (kernel body)**: **identity-in-form** on the per-step body's primitive sequence (every primitive call maps line-for-line), with two information-preserving wrapper surface adjustments (`(op, K, s)` → unified `IterState`; outer-loop tail-recursion reference → outer-driver-by-role reference).
- **`ksp-solve-outer-driver` (this theme; driver loop)**: **substantive (non-identity)** — the loop *is* the operator, so the wrapper rotation (explicit `iterate_while_L3` tail recursion → outer-driver-by-role wrap) is the whole content of the hop, and it erases the iteration view (and the named `sequential-obstruction`, which shadows to the L2 non-laws).

The contrast table:

| Subject | L3 form | L2 form | L3>L2 rotation |
|---|---|---|---|
| **kernel body** (`krylov-step`) | five-primitive-group let-chain, value-threaded | same composition over `IterState` | **identity-in-form** + 2 wrapper surface adjustments |
| **driver loop** (`ksp_solve`) | explicit `iterate_while_L3` tail recursion + named outer-loop `sequential-obstruction` | `iterate_while (krylov-step op) …` named-by-role; obstruction erased | **substantive (non-identity)**: iteration view erased |

**`kernel-identity + driver-non-identity = the full per-solver L3>L2 story.`** The "mild tension" the cycle-020 critic noticed — that `ksp_solve` is classified non-identity while the kernel is classified identity — is **not a tension** because the two classifications are about disjoint subjects: the kernel *body* (the work inside each step, which survives the hop unchanged) versus the *iteration over the body* (the loop, whose explicit-recursion view L2 erases). The layer-edge judgment is ratified: the kernel body collapses identity-in-form, the driver loop is the genuine iteration-rotation. Both are true; they do not conflict.

This division mirrors the kernel chain's own `L3>L2 vs L4>L3` division (substantive content at one hop, identity at the other), but along a different axis: here the split is **kernel vs driver at the same hop**, not **wrapper vs body across two hops**. The pair of themes makes the kernel/driver division visible in the `book/src/L3-L2/` Part, exactly as the kernel theme's §"L3>L2 vs L4>L3 distinction" makes the wrapper/body division visible.

## Verified-against

L3 evidence (the LHS):

- `book/src/L3/ksp_solve.md` (firm, cycle-020 wave-1) — the L3 explicit-fold form this theme references as LHS. §Signature (the `iterate_while_L3` tail recursion), §"Iteration-rotation marker" (the first-class outer-loop `sequential-obstruction`), §"Lowers to" (records the L3>L2 rotation as substantive / non-identity — the same rotation this theme narrates forward).
- `book/src/L3/krylov-step.md` (firm, cycle-010) — the L3 kernel half both endpoints fold; §"Iteration-rotation marker" attributes the obstruction to "the surrounding `iterate_while_L3` tail-recursion, not the `krylov-step` body itself" — i.e., to `ksp_solve`, this theme's subject.

L2 evidence (the RHS):

- `book/src/L2/ksp_solve.md` (firm, cycle-021 wave-1) — the L2 outer-driver composition this theme references as RHS. §Signature (the `iterate_while`-by-role fold), §Semantics phase 2 (the iteration view erased to a named-by-role wrap; "the explicit-recursion iteration-rotation view, and the `sequential-obstruction` it carries, are the L3/ksp_solve concern"), §"Algebraic laws" non-laws "Fold-merge / associativity" + "Identity / lift of the fold to a single tensor-field op at L2" (the L2-vocabulary shadow of the erased obstruction), §"Lifts to" (records the reverse direction in-line: L2 role-reference ⟷ L3 explicit fold).
- `book/src/L2/krylov-step.md` (firm, cycle-005) — the L2 kernel half; §"Algebraic laws" (associativity non-law) cites the restart-as-outer-loop structure and the intrinsic step-boundary sequentiality this driver's fold is built over.

Sibling-theme evidence (the complement):

- `book/src/L3-L2/krylov-step-body-identity.md` (firm) — the kernel-body identity theme this theme complements. §"Rewrite shape" surface-adjustment (2) ("The L3 outer tail-recursive `iterate_while_L3` collapses into L2's outer-driver framing … a wrapper change, not a body change") is exactly the rotation this theme makes the *whole content* of the hop for `ksp_solve` (where the loop is the operator). §"L3>L2 vs L4>L3 distinction" is the kernel chain's labour-division template this theme's §"Kernel-identity / driver-non-identity contrast" mirrors.

L0 evidence (self-verified against `reference/palace/` source via `palace-codemap` `read_range` this dispatch):

- `reference/palace/palace/linalg/iterative.cpp:361-486` — `CgSolver<OperType>::Mult` (def `:361-486`) — the canonical single-fold outer driver the L3 form renders as a tail recursion. Setup + pre-loop test `eps = max(rel_tol·initial_res, abs_tol)` (`:417`), `converged = (res < eps)` pre-loop short-circuit (`:418`); the outer-driver loop guard `for (; it < max_it && !converged; it++)` (`:427`); the per-step in-loop convergence test `converged = (res < eps)` (`:463`); result write `final_res = res; final_it = it;` (`:484-485`).
- `reference/palace/palace/linalg/iterative.cpp:544-705` — `GmresSolver<OperType>::Mult` (def `:544-705`) — the restart-nested double-fold outer driver. The outer restart loop `for (; it < max_it; restart++)` (`:563`); result write `final_res = beta; final_it = it;` (`:703-704`).
- `reference/palace/palace/linalg/iterative.cpp:734-871` — `FgmresSolver<OperType>::Mult` (def `:734-871`) — the flexible-restart double-fold outer driver (the third implemented arm of the krylov-method axis).
- `reference/palace/palace/linalg/iterative.hpp:52-54` — `IterativeSolver<OperType>` solve-statistics members: `mutable bool converged;` (`:52`), `mutable double initial_res, final_res;` (`:53`), `mutable int final_it;` (`:54`) — the four result fields the L3 `result` and L2 `SolveResult` both project. `GetConverged()` with its `rel_tol > 0 || abs_tol > 0` gate at `:98`.
- `reference/palace/palace/linalg/ksp.cpp:297-310` — `BaseKspSolver<OperType>::Mult` (def `:297-310`) — the cumulative-statistics driver wrapper *above* this operator: `ksp->Mult(x, y)` (`:300`, the per-method fold both endpoints compose), the `GetConverged()` check + `Mpi::Warning` (`:301-306`), counter increments `ksp_mult++` / `ksp_mult_it += ksp->GetNumIterations()` (`:308-309`). Evidence that the cumulative counters are driver-side, above the per-solve fold — unchanged across the L3>L2 hop.
- `reference/palace/palace/linalg/ksp.cpp:34-56` — `ConfigureKrylovSolver` factory switch on the `KrylovSolver` enum: implemented arms CG / GMRES / FGMRES; MINRES / BICGSTAB / DEFAULT abort at `:53-55` with `MFEM_ABORT` at `:56` (the krylov-method axis closed at three implemented arms).
- `reference/palace/palace/linalg/ksp.cpp:312-313` — explicit `BaseKspSolver` template instantiations for `Operator` and `ComplexOperator` (the element-type axis).

Strawman / combinator evidence (the reduction-chain backing):

- `book/src/design/l4_calculus.md` §3.7 — the `iterate_while` conventions source; the L3 tail recursion is the unfolded reduction sequence of the combinator, the L2 role reference is the folded form. §3.8 — the trajectory-accumulator demand-pruning governing the result-extraction identity-modulo-pruning.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for `iterate_while` looks like" (firm cycle-008) — publishes the L3 tail-recursion rendering of the outer loop with the §3.8 collapse-rule cited; the conventions source the L3 form's explicit recursion follows.
- `book/src/L4/iterate-while.md` (firm cycle-007) — the firm `iterate_while` combinator both forms reference (L3 explicit tail recursion / L2 named-by-role).

Cross-cutting concept references (consumed unchanged across the rotation):

- `book/src/concepts/sequential-obstruction.md` (firm) — the canonical write-up of the outer-loop obstruction; named first-class at L3, erased to the non-law shadow at L2.
- `book/src/concepts/convergence-test.md` — the stopping-predicate surface (the `\s -> not s.converged && s.it < op.max_it` predicate; identical across the hop).
- `book/src/concepts/solve-monad.md` — the L4 outer-driver surface; dissolved to explicit tail recursion at L3, erased to role reference at L2.
- `book/src/concepts/state-stratification.md` — the three-stratum partition the L3 `(op, K, s)` triple and L2 `IterState` both record (positional at L3, documented field-partition at L2).
- `book/src/concepts/derived-view-hoisting.md` — the demand-pruning law on the result-extraction `outputs` slot, preserved identically across the rotation.

Open-questions ledger:

- `scaffolding/open-questions.md` slug `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion` (forward-referenced plain-text from the L3 §"Lowers to" and the firm L2 §"Lifts to" + dep-map) — the open question this theme closes. Status updates to `closed` on integration with answer-link `book/src/L3-L2/ksp-solve-outer-driver.md` (this file).

## Status

`firm` — the theme's content is firm: both endpoints are firm ([`L3/ksp_solve`](../L3/ksp_solve.md) cycle-020; [`L2/ksp_solve`](../L2/ksp_solve.md) cycle-021 wave-1); the substantive non-identity content (the iteration-view erasure + the obstruction's shadow-to-non-laws) is structurally grounded and citation-backed at both layers and the L0 source; the supporting `(op, K, s)` → `(K, b)`/`IterState` consolidation is information-preserving; the rewrite-shape table is total on the fold structure with the two non-identity lines (the fold line and the obstruction line) explicitly delimited; no speculative L3 vocabulary is introduced; the four applicability conditions are stated and confirmed for the five-slice corpus. The kernel-identity / driver-non-identity contrast resolves the cycle-020 critic's "mild tension" by recognizing the two classifications are about disjoint subjects (kernel body vs. iteration over the body). This theme is the **driver complement** of the sibling [`krylov-step-body-identity`](./krylov-step-body-identity.md): `kernel-identity + driver-non-identity = the full per-solver L3>L2 story`.

Authored cycle-021 wave-2 (abstractor), enacting **Identity-lowerings still require both L levels** (both layers carry a `ksp_solve` entry, this theme is the connecting rotation) and **Layers are defined high→low** (LHS L3, RHS L2, forward narration). Unlike the BLAS-1 cohort (clean identity-lowerings) and the kernel-body theme (identity-in-form on the body), the L3>L2 rotation here is **substantive** — the iteration view is erased and the named obstruction shadows down to the L2 non-laws.

## L3>L2 vs kernel-theme distinction

The two L3>L2 themes for the Krylov solver divide labour by subject:

- **`krylov-step-body-identity` (kernel body)**: identity-in-form on the per-step body's primitive sequence; two information-preserving wrapper surface adjustments.
- **`ksp-solve-outer-driver` (this theme; driver loop)**: substantive (non-identity); the loop *is* the operator, so the wrapper rotation (explicit `iterate_while_L3` → outer-driver-by-role) is the whole content of the hop, erasing the iteration view and the named `sequential-obstruction`.

Together they constitute the full per-solver L3>L2 lowering. The composition is identity-in-form on the kernel body (the work inside each step survives unchanged) and non-identity on the driver loop (the iteration view is erased). This is the precise L3>L2 statement of "the Krylov method's per-step work is composition-preserving but its iteration is sequential and not lift-preserving" — the kernel/driver division made visible in the artifact.
