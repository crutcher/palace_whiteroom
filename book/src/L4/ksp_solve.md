---
layer: L4
operator: ksp_solve
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L4/krylov_step
      kind: folds                     # the inner per-step fold body restart_cycle runs (18 body refs); the canonical L4 kernel/driver pair. Load-bearing: this depends-on edge makes krylov_step root-reachable via the root-reachable ksp_solve.
    - target: L4/iterate_while
      kind: folds                     # the inner kernel-fold combinator restart_cycle invokes (and solve_loop's outer tail-recursion degenerates to per Law 2)
    - target: L3/ksp_solve
      kind: lowers-to                 # the firm L3 value-threaded outer-driver fold this cap lowers to (lowering edge = depends-on on both endpoints, scheme §5)
    - target: concepts/OpParams
      kind: uses-record               # OpParams readonly operator-internal config record named in the signature (ksp_solve :: OpParams -> Inputs -> SimState); see §Signature shape contract
    - target: concepts/SimState
      kind: uses-record               # SimState the Solve = StateT SimState Identity persistent-state record discharged by execState; the cap's net effect is the SimState transition; see §Signature
  reference:
    - L4/index                        # navigational container: the L4 Part overview anchoring the firm solve_loop / restart_cycle / Outcome outer-driver vocabulary rows
    - concepts/solve-monad            # the Solve = StateT SimState Identity outer-driver pattern this cap realises (non-node narrative-pointer concept page → reference)
    - concepts/state-stratification   # the three-stratum SimState / OpParams / Krylov typing
    - concepts/convergence-test       # the stopping-predicate surface the Outcome classification reads
    - concepts/derived-view-hoisting  # §3.8 demand-pruning governing the trajectory-vs-classifier demand split
    - concepts/variant-absorption     # the body-variant absorption + readonly OpParams typing
    - concepts/sequential-obstruction # the outer-loop obstruction the cap carries at the coordination layer
    - concepts/constructed-operators  # the preconditioner-side absorption into op.T
variant_axes:
  - outcome-classification (Done True converged / Done False exhausted-max_it / Continue restart-warranted — the 3-arm Outcome sum)
  - restart-shape (non-restarted: solve_loop recurses one_cycle / restarted: solve_loop recurses restart_cycle — selects the per-cycle driver, not the loop algebra)
  - element-type (real / complex — absorbed into OpParams; the Solve threading is element-uniform)
  - convergence-failure-policy (soft-fail; the Bool inside Done — Palace's only variant)
---

# ksp_solve

The L4 **outer-driver cap** for preconditioned Krylov solves: the `Solve`-monadic coordination that drives [`krylov_step`](./krylov_step.md) to convergence and classifies termination once at the cycle boundary. `ksp_solve` at L4 is the **cap** — the top-of-stack monadic solve entry point `solve op inp = execState (solve_loop op inp) initial_state` — whose body is assembled from the firm `solve-monad` outer-driver vocabulary (`solve_loop` / `restart_cycle` / `Outcome`) and whose fold body is the firm [`krylov_step`](./krylov_step.md) kernel. It is the driver-half companion to the kernel-half `krylov_step`: the kernel is *what gets folded*; `ksp_solve` is *the fold and its coordination*, expressed at the calculus level.

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes lifetimes, dispatch sites, and effect placement structural. `ksp_solve` at L4 is the typed coordination shape that the `solve-monad` concept ([`solve-monad`](../concepts/solve-monad.md)) sketches in prose (`solve_loop` recursing on `restart_cycle` until an `Outcome` says stop) and that the `L4/index` dep-map anchors as three firm outer-driver vocabulary rows. This chapter is the per-operator cap that *consumes* those three rows and supplies the algebraic apparatus — the monad-law fusion identities, the `solve_loop`-as-`iterate_while` fold equivalence, the `Outcome`-classification variant axis, and the demand-pruning interaction — that the vocabulary rows defer to "the forthcoming `L4/ksp_solve` cap" (`L4/index.md` dep-map `solve_loop` / `restart_cycle` / `Outcome` rows, "per-operator laws ride the forthcoming `L4/ksp_solve` cap").

The relationship to the inner kernel is **driver-to-kernel**, mirroring the L3 pair:

- [`krylov_step`](./krylov_step.md) names the per-step fold body — a single `Solve { krylov, outputs }` action whose sole `SimState` effect is the counter increment.
- `ksp_solve` (this entry) names the **outer coordination** — the `Solve ()` driver that folds `krylov_step` inside `restart_cycle`, classifies the returned bundle into an `Outcome`, and tail-recurses via `solve_loop` until `Done`. It sits *above* the [`iterate_while`](./iterate_while.md) family (the inner kernel-fold), not inside it.

The cap is defined **in L4 vocabulary** (high→low discipline): its semantics, signature, and laws are stated in terms of the `Solve` monad, the `solve-monad` outer-driver surface, and the `iterate_while` family — NOT in terms of L3 value-threading primitives. The L4>L3 dissolution (the `Solve` monad collapsing to positional `(K, s)` threading, `solve_loop`'s `do`/`unless` collapsing to the `iterate_while_L3` predicate) is a separate L4>L3 theme (`L4-L3/ksp-solve-driver-dissolution`), narrated forward from L4 to L3; it is **not** authored here. The firm L3 image of this cap is the layer-coherent [`L3/ksp_solve`](../L3/ksp_solve.md), whose body is the value-threaded `iterate_while_L3 (krylov_step op)` fold — the dissolution target.

`ksp_solve` at L4 is a **methodology-level cap**, not a Palace-source artefact — there is no L0 source range that "is" the L4 `ksp_solve`. The Palace evidence sits at L3 / L1 / L0 (the per-method `Mult` bodies and the `IterativeSolver` base); L4 cites the L3 driver and the L1 collapse as its evidence base, plus the `solve-monad` concept for the outer-driver pattern and the strawman for the monad / loop / pruning conventions.

## Signature

The L4 cap signature is the `solve-monad` outer-driver shape. The entry point and its two driver layers:

    -- entry point: run the outer driver over the initial SimState
    ksp_solve  :: OpParams -> Inputs -> SimState
    ksp_solve op inp = execState (solve_loop op inp) (initial_state inp)

    -- outer driver: tail-recurse the per-cycle body until Outcome says stop
    solve_loop :: OpParams -> Inputs -> Solve ()
    solve_loop op inp = do
      o <- restart_cycle op inp        -- or: one_cycle op inp, for non-restarted solvers
      unless (done o) (solve_loop op inp)

    -- per-cycle driver: fresh Krylov, inner kernel-fold, fold correction, classify once
    restart_cycle :: OpParams -> Inputs -> Solve Outcome

    -- termination sum, classified once at the cycle boundary
    data Outcome = Continue | Done Bool

    done :: Outcome -> Bool
    done (Done _)  = True
    done Continue  = False

Shape contract (bunsen-style; named records and axes; the three strata per [`state-stratification`](../concepts/state-stratification.md); the solution-space shape group `S` follows the named-shape-group convention of [`l4_calculus`](../semantics/index.md) §1.2.1):

- `OpParams` — operator-internal configuration, captured once at solve construction; `readonly` per [`state-stratification`](../concepts/state-stratification.md). Closes over the system operator (`op.T`, or the constructed `apply_BA`), the optional preconditioner, the convergence-control scalars (`op.rel_tol`, `op.abs_tol`, `op.max_it`, restart `op.max_dim`), and the variant selectors (krylov-method nesting, orthogonalisation, preconditioner side). The cap's driver does not branch on `OpParams` *body*-shaping fields (those are absorbed in [`krylov_step`](./krylov_step.md)); it reads only the *loop*-shaping fields (`max_it`, `max_dim`, restart cadence). Variant absorption is structural via the `readonly` typing per [`variant-absorption`](../concepts/variant-absorption.md).
- `Inputs` — the per-solve inputs that seed `initial_state` (the RHS `b` and, under the warm-start policy, the entry iterate). Read-only; consumed only at seed construction and inside `restart_cycle`'s residual-proxy initialisation.
- `SimState` — externally-visible state that persists across the entire solve call. Per [`state-stratification`](../concepts/state-stratification.md), contains `x: Tensor[(S: ...)]` (the solution-space shape group `S`), `it: Int`, `converged: Bool`, `final_res: Scalar`, `initial_res: Scalar`. Threaded by the `Solve a = StateT SimState Identity a` monad ([`solve-monad`](../concepts/solve-monad.md)); the cap's net effect is the `SimState` transition from `initial_state inp` to the converged terminal state, extracted by `execState`.
- `Krylov` — solve-local ephemeral bundle; born at restart entry (`fresh_krylov`), discarded at restart exit. Per [`state-stratification`](../concepts/state-stratification.md), **not** part of `SimState`: threaded inside `restart_cycle` as a plain `let`-bound value, never as a monadic effect. The cap names its *lifecycle role* (born at cycle entry, discarded at exit); the slice supplies its fields (CG: `{ r, z, p, β, α }`; GMRES: `{ V, H, s, cs, sn, β, j }`).
- `Outcome = Continue | Done Bool` — the termination sum, classified **once** at the cycle boundary by `restart_cycle` against `(K.beta, K.j, SimState.it, ε)`. `Done True` — converged (`K.beta < ε`); `Done False` — exhausted `op.max_it`; `Continue` — hit `op.max_dim`, another restart cycle warranted. `solve_loop` pattern-matches via `done`; the `Bool` inside `Done` folds uniformly into `SimState.converged`. This is the L4 lift of the L3 soft-fail `Bool` `result.converged` to a sum type (the cap's load-bearing variant axis; see §"Variant axes").
- `Solve a = StateT SimState Identity a` — the state monad ([`solve-monad`](../concepts/solve-monad.md)). The cap's effect domain is exactly `SimState`; the entry point discharges it via `execState`, projecting the threaded state out and discarding the `()` value.

The shape contract makes three things structural at the cap level that are merely conventional at L3:

1. **Termination is a single typed decision site.** The three termination reasons (converged, exhausted, restart-warranted) are named arms of `Outcome` and classified once per cycle, instead of scattered across the L3 fold's predicate (`not s.converged && s.it < op.max_it`) plus the inner-loop breaks and the post-correction re-test. `solve_loop` reads only `done o`.
2. **`SimState` is the sole monadic stratum; `Krylov` is a plain value.** The `execState` discharge and the `Solve ()` typing forbid the ephemeral `Krylov` bundle from leaking into the persistent state — its born-at-restart / discarded-at-exit lifecycle is enforced by it being a `let`-bound value inside `restart_cycle`, not a `StateT` field. This is the [`state-stratification`](../concepts/state-stratification.md) ephemeral-bundle discipline made structural.
3. **The outer driver sits strictly above the inner kernel-fold.** `restart_cycle` runs an [`iterate_while`](./iterate_while.md)-family fold of [`krylov_step`](./krylov_step.md) (the inner kernel whose sole `SimState` effect is `modify (\s -> s { it = s.it + 1 })`); `solve_loop`'s tail recursion is the *outer* coordination around that fold, not a flattening of it. The two-level structure is the L4 typing of the L3 restart-nesting.

## Semantics

`ksp_solve` at L4 is the complete preconditioned-Krylov solve expressed as a `Solve`-monadic outer driver. The cap assembles the three firm `solve-monad` vocabulary verbs:

`solve_loop op inp` is the **outer driver**: a `do`-block that runs one `restart_cycle` (yielding an `Outcome`), then tail-recurses on itself `unless` the `Outcome` is `Done`. For non-restarted solvers (CG, Chebyshev) the per-cycle verb specialises to `one_cycle` (a single cycle, no re-seed); for restarted solvers (GMRES, FGMRES) it is `restart_cycle` proper, re-seeding a fresh `Krylov` each iteration. The recursion is the L4 form of the iteration: each `solve_loop` invocation is one outer cycle, and the `unless (done o)` guard is the convergence test lifted to the coordination layer.

`restart_cycle op inp` is the **per-cycle body**, with four phases in dataflow order, exactly as the `solve-monad` worked example ([`solve-monad`](../concepts/solve-monad.md) §"Worked example — GMRES") describes:

1. **Build a fresh ephemeral bundle** — `let K0 = fresh_krylov op inp s` — born at cycle entry, threaded as a plain value.
2. **Run the inner kernel-fold** — `let (Kn, outs) = iterate_while (krylov_step op K0) cont` — the [`iterate_while`](./iterate_while.md)-family fold of [`krylov_step`](./krylov_step.md); the sole `SimState` effect inside is the per-step `modify (\s -> s { it = s.it + 1 })`. The iterate `x` is **not** touched per step.
3. **Fold the correction into `SimState.x` exactly once** — `modify (\s -> s { x = s.x + Kn.V · Kn.y })` — the single per-cycle `SimState.x` write, at the cycle boundary, after the inner fold's `back_solve` produces the correction.
4. **Classify the returned bundle into an `Outcome` once** — `pure (classify Kn op s)` — against `(Kn.beta, Kn.j, s.it, ε)`, producing `Done True` / `Done False` / `Continue`.

`Outcome` is the **termination sum**: classification happens once, at the cycle boundary, replacing the L3 form's scattered termination tests with a single decision site ([`solve-monad`](../concepts/solve-monad.md) §"Termination as a sum type"). `solve_loop` pattern-matches via `done`; the `Bool` inside `Done` folds uniformly into `SimState.converged` (`Done True ⇒ converged = True`; `Done False ⇒ converged = False`), so the outer fold into `SimState` is uniform.

The cap's **net effect** is the `SimState` transition discharged by `execState`: `ksp_solve op inp` projects the terminal `SimState` (whose `.x` holds the approximate solution and whose `.converged` / `.it` / `.final_res` / `.initial_res` are the four readout fields) out of the `solve_loop op inp` action run from `initial_state inp`. The statistics counters that L0 mutates cumulatively (`ksp_mult` / `ksp_mult_it`) are **driver-side accumulators above the cap**, not part of the `Solve` effect — the cap reports the per-call iteration count in `SimState.it`; the cumulative counter is `Σ_calls SimState.it`, computed by the caller. This keeps the cap referentially transparent at the per-solve granularity (it is a pure function of `(op, inp)` modulo the two load-bearing non-determinism sources inherited transitively through [`krylov_step`](./krylov_step.md)).

### Demand-pruning interaction with the outer driver

The inner kernel-fold's per-step `outputs` accumulate into the [`iterate_while`](./iterate_while.md) `trajectory` ([`derived-view-hoisting`](../concepts/derived-view-hoisting.md) §3.8, strawman `book/src/semantics/index.md:186-228`). The cap's `Outcome` classifier reads only the *terminal* bundle `(Kn.beta, Kn.j, s.it, ε)`, never the per-step trajectory; and `solve_loop` reads only `done o`. So under the §3.8 pruning rule, **the per-step residual-norm trajectory prunes whenever no external consumer reads it** — the cap's coordination demands only the terminal residual proxy (the classifier's input) and the iteration count. The convergence predicate inside `restart_cycle` *does* demand the per-step residual proxy (it gates the inner fold), so `SimState.final_res` is never fully pruned; but the *accumulated trajectory* of residual norms (used only for printing) is. This is the cap-level statement of the same demand-pruning the L3 driver inherits ([`L3/ksp_solve`](../L3/ksp_solve.md) §"Inherited demand-pruning") — at L4 it is structural because `Outcome` and `trajectory` are typed separately and the classifier's demand set is visible.

## Algebraic laws

`ksp_solve` is a **monadic outer driver**, not an algebra. The laws below are the cap's coordination identities (monad-law and `execState`/`StateT` fusion sharpenings of the strawman rules) plus the trajectory-terminal fixed-point properties inherited from the L1 collapse. Absences are catalogued explicitly to prevent decoration drift.

1. **`execState`/`StateT` discharge fusion** (the cap's defining identity). `ksp_solve op inp = execState (solve_loop op inp) (initial_state inp)` — the cap *is* the `execState`-discharge of the `solve_loop` action. By the `StateT` definition, `execState m s0 = snd (runStateT m s0)` applied to `Identity`: the threaded `SimState` is projected and the `()` value discarded. **Consequence**: the cap's observable result is exactly the terminal `SimState`; there is no residual monadic structure to inspect. This is the load-bearing identity that makes the cap a *pure function* `(op, inp) -> SimState` despite the internal `StateT` threading.

2. **`solve_loop` tail-recursion ≡ `iterate_while_pure` over outer cycles** (the fold-equivalence law). `solve_loop`'s `do { o <- restart_cycle op inp; unless (done o) (solve_loop op inp) }` is the `Solve`-threaded specialisation of the strawman `iterate_while` (`book/src/semantics/index.md:150-184`): the outer cycle index is the fold carry, `restart_cycle` is the step, and `\_ -> not (done o)` is the continuation predicate. Because the outer driver produces no per-cycle *extras* that any consumer reads (only the terminal `SimState` is observed), it degenerates to the `iterate_while_pure` sugar (`index.md:178-182`) — the trajectory is always empty. **Consequence**: the outer driver is a pure fold over outer cycles whose only output is the threaded `SimState`; the `Outcome` values are consumed-and-discarded by the predicate, never accumulated. This is the law that licenses the L4>L3 dissolution rendering `solve_loop` as `iterate_while_L3` (D3's theme).

3. **Monad-law normal form of the driver body** (sharpened from strawman §3.3–3.4, `index.md:119-136`). The `restart_cycle` body's four phases compose by `>>=`; the per-cycle `SimState` writes (the counter increments inside the inner fold, the single boundary correction `modify`) fuse by the state-effect law `modify (f ∘ g) → do { modify g; modify f }` (`index.md:134`) read right-to-left: the sequence of `modify`s in a cycle is observationally a single composite `SimState` transition. **Consequence**: the cap body has a normal form in which each outer cycle is one composite `SimState` transition followed by one `Outcome` classification; the monad laws (left/right identity, associativity — `index.md:123-125`) let the `pure`-returns and `>>=`-sequencing be normalised away, leaving the cap as `fold-of-composite-transitions`. The classification `pure (classify …)` is a right-identity terminal (`m >>= return → m`).

4. **Terminal operator-inverse** (modulo tolerance; the load-bearing terminal law, lifted from [`L1/ksp_solve`](../L1/ksp_solve.md) law 3 and [`L3/ksp_solve`](../L3/ksp_solve.md) law 1). For `op` whose system operator is `A`, `(ksp_solve op inp).x ≈ A⁻¹ · b` (with `inp` carrying RHS `b`), exact in the limit `op.rel_tol, op.abs_tol → 0`, `op.max_it → ∞`. The cap converges to the fixed point of the Krylov iteration; the four `SimState` readout fields are the finite-tolerance witnesses. The `Outcome` sum reports *which* termination reason held: `Done True` (the inverse was computed to tolerance), `Done False` (the budget ran out first).

5. **`Outcome`-classify-once / fold-uniformly** (the sum-type coordination law, from [`solve-monad`](../concepts/solve-monad.md) §"Termination as a sum type"). The three termination reasons are classified at exactly one site per cycle (`restart_cycle`'s `classify`), and `solve_loop` folds the `Bool` inside `Done` uniformly into `SimState.converged`. **Consequence**: there is no termination-reason information lost or duplicated across the coordination layer — the multi-reason classification that L3 scatters into per-test branches is, at L4, a single total function `Krylov -> OpParams -> SimState -> Outcome`. This is the law the `eigsolve` cap *extends* (a richer partial-success arm), not one it overrides.

Laws that explicitly **do not** hold:

- **Outer-cycle fold-merge / associativity**. `ksp_solve` over two `max_dim`-bounded restart cycles is **not** equal to `ksp_solve` over one `2·max_dim`-bounded cycle for restarted solvers — `restart_cycle` re-seeds (`fresh_krylov` discards the Krylov subspace), so the trajectory through two cycles differs from one larger cycle. Inherited from [`krylov_step`](./krylov_step.md) §"Algebraic laws" (associativity non-law) and [`L3/ksp_solve`](../L3/ksp_solve.md) (fold-merge non-law). This is *why* the restart structure is a tail recursion of `restart_cycle`, not a single flattened inner fold.
- **Lift of the outer fold to a closed-form whole-state op**. The trajectory of `SimState` transitions does **not** collapse to a closed-form `SimState -> SimState` in `n` cycles — the outer-loop `sequential-obstruction` ([`sequential-obstruction`](../concepts/sequential-obstruction.md); [`L3/ksp_solve`](../L3/ksp_solve.md) §"Iteration-rotation marker"): each cycle reads scalars (`β`, residual proxy) produced by the previous, not closed-form in the carry. The cap names the obstruction at the coordination layer; the monad makes the interior termination visible but does not remove the sequentiality. (The `Solve` monad's `>>=` is sequential composition, not fusion — strawman §3.3 associativity is re-bracketing, not closed-form collapse.)
- **Linearity of the readout fields in `b`**. `SimState.it` / `.initial_res` / `.final_res` are **not** linear in the RHS — different RHSes generate different residual histories and outcome trajectories. Only the *terminal* `SimState.x` is linear in `b` (modulo tolerance, law 4). Inherited from [`L1/ksp_solve`](../L1/ksp_solve.md) law 1's caveat and [`L3/ksp_solve`](../L3/ksp_solve.md).
- **Exact composition with `apply_linop`**. `apply_linop op.T (ksp_solve op inp).x ≈ b` holds only within `ε`, not exactly, at finite tolerance. Inherited from [`L1/ksp_solve`](../L1/ksp_solve.md). Iterative-refinement consumers must guard.
- **`Outcome` identity element / empty solve**. There is no `Outcome` value that makes `solve_loop` a no-op while still advancing `SimState` — a `Done`-on-entry (the zero-RHS / converged-warm-start short-circuit) terminates with `SimState.it = 0` and `SimState.x = initial_state.x`, which is the *short-circuit* fixed point, not a monadic identity element. (`StateT`'s identity is `pure ()`, which discharges to `initial_state` unchanged — a degenerate, not an algebraic, identity.) Inherited as the L4 form of [`L3/ksp_solve`](../L3/ksp_solve.md) law 2 (zero-RHS short-circuit).
- **Bit-determinism across reduction-tree / orthogonalisation / initial-guess variants**. Inherited transitively through [`krylov_step`](./krylov_step.md) and from [`L1/ksp_solve`](../L1/ksp_solve.md) / [`L3/ksp_solve`](../L3/ksp_solve.md): the outer-cycle count and terminal `final_res` depend on the inner reduction tree, the orthogonalisation variant, and the initial-guess policy at the bit level; the mathematical solution is the same, the floating-point realisation differs. Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra". The `Solve` monad's `SimState` threading does not introduce a determinising identity.
- **Commutativity of nested caps**. `ksp_solve op₁ (… ksp_solve op₂ …)` ≠ the swapped composition, since `A₁⁻¹ · A₂⁻¹` does not commute. Inherited from [`L1/ksp_solve`](../L1/ksp_solve.md).

## Dependencies

L4 outer-driver vocabulary (the firm rows this cap consumes — `book/src/L4/index.md` §Vocabulary-cohort "`solve-monad` outer-driver vocabulary"):

- `solve_loop` — the outer driver the cap's entry point runs (`execState (solve_loop op inp) …`). The cap *is* the discharge of this action.
- `restart_cycle` — the per-cycle body `solve_loop` tail-recurses on (`one_cycle` for non-restarted solvers). Supplies the four-phase cycle.
- `Outcome` — the termination sum `restart_cycle` produces and `solve_loop` pattern-matches; the cap's load-bearing variant axis.

L4 row dependencies (the inner kernel-fold the cap drives):

- [`krylov_step`](./krylov_step.md) — the per-step fold body `restart_cycle` runs inside the inner [`iterate_while`](./iterate_while.md)-family fold. The kernel supplies the body; the cap supplies the outer coordination. The canonical L4 kernel/driver pair.
- [`iterate_while`](./iterate_while.md) — the inner kernel-fold combinator `restart_cycle` invokes (and, by Law 2, the combinator `solve_loop`'s outer tail-recursion degenerates to). The cap sits strictly above this family.

L4 concept references:

- [`solve-monad`](../concepts/solve-monad.md) — the `Solve a = StateT SimState Identity a` outer-driver pattern this cap realises; §Shape (the entry point), §"Worked example — GMRES" (the `restart_cycle` four phases), §"Termination as a sum type" (the `Outcome` classify-once law).
- [`state-stratification`](../concepts/state-stratification.md) — the three-stratum (`SimState` / `OpParams` / `Krylov`) typing; the ephemeral-bundle discipline that keeps `Krylov` out of the `Solve` effect.
- [`convergence-test`](../concepts/convergence-test.md) — the stopping-predicate surface the `Outcome` classification reads.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the §3.8 demand-pruning algebra governing the trajectory-vs-classifier demand split.
- [`variant-absorption`](../concepts/variant-absorption.md) — the body-variant absorption (in `krylov_step`) and the `readonly` `OpParams` typing; the cap's loop-shaping axes are *not* absorbed (they shape the coordination).
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the outer-loop obstruction the cap carries at the coordination layer.
- [`constructed-operators`](../concepts/constructed-operators.md) — the preconditioner-side absorption into `op.T`.

**Strawman reference**: `book/src/semantics/index.md` §3.3–3.4 (monad / state-effect laws, `:119-136`), §3.7 (`iterate_while` small-step, `:150-184`), §3.8 (demand-pruning, `:186-228`) are the conventions source for this cap's laws and the loop / pruning shapes.

## Lowers to

L4 `ksp_solve` lowers to L3 [`ksp_solve`](../L3/ksp_solve.md) via the L4>L3 dissolution theme `L4-L3/ksp-solve-driver-dissolution`. The rotation is **substantive** (not identity-in-form): the `Solve a = StateT SimState Identity a` threading collapses to explicit positional `(K, s)` value-threading; `solve_loop`'s `do { o <- restart_cycle …; unless (done o) … }` collapses to the L3 `iterate_while_L3` outer tail-recursion with the predicate `\s -> not s.converged && s.it < op.max_it` (the `Outcome` pattern-match dissolving into the predicate's read of `s.converged`); the once-per-cycle `modify`-correction collapses to the L3 `fold_iterate` boundary write; and the `Outcome` sum collapses to the L3 soft-fail `Bool` `result.converged` (the multi-reason classification scattering into L3's per-test branches). This entry records the rotation *direction* (L4 monadic cap → L3 explicit fold) in-line per the high→low discipline; it does **not** author the theme. The firm L3 image is [`L3/ksp_solve`](../L3/ksp_solve.md) (the value-threaded outer-driver fold), whose own §"Lowers to" carries the further L3>L2 hop (substantive, theme pending L2 promotion).

## Variant axes

Four axes, all **coordination-shaping** (they shape the outer driver, not the per-step body — body axes live in [`krylov_step`](./krylov_step.md)):

1. **outcome-classification** (`Done True | Done False | Continue`) — the load-bearing cap axis: the 3-arm `Outcome` sum into which `restart_cycle` classifies the terminal bundle. `Done True` (converged, `K.beta < ε`), `Done False` (exhausted `op.max_it`), `Continue` (hit `op.max_dim`, restart warranted). This is the L4 lift of the L3 soft-fail `Bool` to a sum type ([`L3/ksp_solve`](../L3/ksp_solve.md):160; the `Bool` inside `Done` is the L3 `result.converged`). The `eigsolve` cap extends this axis with a partial-success arm (`0 < converged < requested`) with no `ksp_solve` analog — anchored as the `Outcome`-sum *pattern*, specialised per-cap.
2. **restart-shape** (`non-restarted | restarted`) — selects the per-cycle verb `solve_loop` recurses on: `one_cycle` (CG, Chebyshev — a single cycle, no re-seed) vs `restart_cycle` (GMRES, FGMRES — fresh `Krylov` each cycle). Selects the coordination nesting, not the `Outcome` algebra. This is the *outer* loop; the per-step body is restart-agnostic (the kernel's axis).
3. **element-type** (`real | complex`) — absorbed into `OpParams`; the `Solve` threading is element-uniform (the monad acts on `SimState` whose scalar field is the only element-typed component). Collapsed to one cap parameterised by element type, as at L3 / L1.
4. **convergence-failure-policy** (`soft-fail`) — Palace's only variant: the cap always discharges the terminal `SimState` and reports `SimState.converged` (the `Bool` inside `Done`); no hard-fail. At L4 the policy is *carried by the `Outcome` sum itself* — `Done False` is a first-class arm, not an exception. This is the structural improvement over the L3 `Bool` and the L1 boolean (where soft-fail is implicit in `converged` being a flag).

These four are **distinct from** [`krylov_step`](./krylov_step.md)'s six body-variant axes (all absorbed into the kernel's `OpParams` `readonly` typing). The only shared axis is **restart-shape**: at the body level the kernel is restart-*agnostic*; at the cap level restart-shape selects the per-cycle verb. The two appearances are complementary — the kernel ignores restart, the cap owns it.

## L4 vs L3 distinction

- **L3**: value-threaded explicit fold `ksp_solve :: (op, K_0, s_0) -> (s_final, result)`. The iteration view is load-bearing — the outer tail-recursive `iterate_while_L3 (krylov_step op)` loop is rendered explicitly, the four-field `result` is a positional projection, and the outer-loop `sequential-obstruction` is named. No `Solve` monad, no `Outcome` sum (the soft-fail is a `Bool`), no `readonly` typing.
- **L4**: `Solve`-monadic outer-driver cap `ksp_solve op inp = execState (solve_loop op inp) initial_state`. The coordination is typed — `solve_loop` / `restart_cycle` thread `SimState` through the `Solve = StateT SimState Identity` monad; `Krylov` is a `let`-bound ephemeral value structurally excluded from the state; termination is the `Outcome` sum classified once per cycle; `OpParams` is `readonly`. The L4>L3 dissolution erases the monad, the sum-type, and the `readonly` typing, recovering the L3 explicit fold.

## Evidence

`ksp_solve` at L4 is a methodology-level cap; Palace's C++ source does not realise the L4 form. The L0 evidence is transitive through the firm L3 driver and L1 collapse; the cap-level coordination apparatus is evidenced by the `solve-monad` concept and the strawman.

- `book/src/L3/ksp_solve.md` (firm) — the firm L3 driver this cap lowers to. Its body is the `iterate_while_L3 (krylov_step op)` fold; its §"Iteration-rotation marker" names the outer-loop `sequential-obstruction`; its four-field `result` is the L3 image of the cap's terminal `SimState` readout. The dissolution target.
- `book/src/L1/ksp_solve.md` (firm) — the L1 opaque collapse; the five fixed-point laws (linearity in `b`, zero-RHS-zero-solution, operator-inverse, idempotent re-solve, construction-commutes) that the cap restates as trajectory-terminal laws; the soft-fail `Bool` the `Outcome` sum lifts.
- `book/src/L4/krylov_step.md` (firm) — the inner kernel-fold body this cap drives; the kernel/driver pairing; the §"Algebraic laws" associativity non-law cited for the cap's outer-cycle fold-merge non-law.
- `book/src/L4/iterate_while.md` (firm) — the inner kernel-fold combinator `restart_cycle` invokes; the combinator Law 2 degenerates the outer driver to.
- `book/src/concepts/solve-monad.md:1-68` — the outer-driver pattern: §Shape (`:5-17`, the `solve` / `solve_loop` entry point), §"Worked example — GMRES" (`:47-56`, the `restart_cycle` four phases), §"Termination as a sum type" (`:58-68`, the `Outcome` classify-once / fold-uniformly law).
- `book/src/concepts/state-stratification.md` — the three-stratum typing and the ephemeral-`Krylov` discipline keeping the bundle out of the `Solve` effect.
- `book/src/semantics/index.md:119-136` — §3.3 monad laws (`:121-127`) + §3.4 state effects (`:131-136`); the normal-form law (Law 3) is sharpened from these. `:150-184` — §3.7 `iterate_while` small-step + the `iterate_while_pure` sugar (`:178-182`) the fold-equivalence law (Law 2) cites. `:186-228` — §3.8 demand-pruning, the trajectory-vs-classifier demand-split (§"Demand-pruning interaction").
- L0 anchors (transitive via the L3 driver):
  - `palace/linalg/iterative.cpp:361-486` — the CG `Mult` body (the non-restarted single-loop driver); `palace/linalg/iterative.cpp:544-705` — the GMRES `Mult` body (the restart-nested driver). The L0 bodies of the L3 driver this cap lowers to.
  - `palace/linalg/iterative.cpp:417-418` — `eps = max(rel_tol·initial_res, abs_tol)` + pre-loop `converged = (res < eps)` short-circuit (the cap's zero-RHS / converged-warm-start `Done`-on-entry).
  - `palace/linalg/iterative.cpp:427` — CG single-loop outer-driver `for (; it < max_it && !converged; it++)` (the `one_cycle`-specialised `solve_loop`).
  - `palace/linalg/iterative.cpp:484-485` — CG result write `final_res = res; final_it = it;` (the terminal `SimState` readout, non-restarted residual proxy).
  - `palace/linalg/iterative.cpp:563` — GMRES restart outer loop `for (; it < max_it; restart++)` (the `restart_cycle`-recursing `solve_loop`).
  - `palace/linalg/iterative.cpp:703-704` — GMRES result write `final_res = beta; final_it = it;` (the terminal readout, LS-residual proxy).
  - `palace/linalg/iterative.hpp:52-55` — the four result fields `converged` / `initial_res` / `final_res` / `final_it` (the cap's terminal `SimState` readout origins).
  - `palace/linalg/iterative.hpp:98` — `GetConverged()` with its `rel_tol > 0 || abs_tol > 0` gate (a loop-shaping convention folded into the cap's `converged` readout).
  - `palace/linalg/iterative.hpp:101-108` — accessors `GetInitialRes` / `GetFinalRes` / `GetNumIterations`.
  - `palace/linalg/ksp.cpp:296-310` — `BaseKspSolver::Mult` — the soft-fail policy: `:301-307` logs a warning and returns the iterate regardless (no abort), the basis of the cap's `Done False` first-class arm; counters `:308-309` are the driver-side cumulative accumulators above the cap.
