# ksp-solve-driver-dissolution

The L4>L3 lowering theme for the [`ksp_solve`](../L4/ksp_solve.md) **outer-driver cap** — the `Solve`-monadic coordination `solve op inp = execState (solve_loop op inp) (initial_state inp)` that drives [`krylov-step`](../L4/krylov-step.md) to convergence and classifies termination once at the cycle boundary. The theme dissolves the L4 outer-driver machinery (the `Solve = StateT SimState Identity` monad, the `solve_loop` / `restart_cycle` `do`-block drivers, the `Outcome = Continue | Done Bool` termination sum) into the firm L3 value-threaded outer-driver fold [`L3/ksp_solve`](../L3/ksp_solve.md) `(op, K_0, s_0) -> (s_final, result)`. It is the **driver-half** companion to the kernel-half [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md): the kernel theme dissolves the per-step body; this theme dissolves the *outer coordination around the body's fold*. It **composes strictly above** the inner-fold combinator dissolution [`iterate-while-dissolution`](./iterate-while-dissolution.md) — that firm c047 theme dissolves the `iterate_while` combinator the L4 `restart_cycle` invokes; this theme dissolves the `solve_loop` / `restart_cycle` / `Outcome` driver that wraps that fold.

## Slug

`ksp-solve-driver-dissolution`

## Context

The cycle-048 R2 harvester (D1) promoted [`L4/ksp_solve`](../L4/ksp_solve.md) to a firm L4 outer-driver cap, consuming the cycle-047 `solve-monad` outer-driver vocabulary (`solve_loop` / `restart_cycle` / `Outcome`) and folding the firm [`krylov-step`](../L4/krylov-step.md) kernel via the firm [`iterate-while`](../L4/iterate-while.md) family. The cap's own §"Lowers to" (`book/src/L4/ksp_solve.md`) names the dissolution to L3 as **substantive** (not identity-in-form) and records the rotation *direction* in-line per the high→low discipline, but defers the theme itself to "a separate L4>L3 theme (`L4-L3/ksp-solve-driver-dissolution`, D3's dispatch this cycle), narrated forward from L4 to L3". This chapter is that theme.

The L4>L3 hop for the iterative-solve family splits cleanly across **three** dedicated themes, each at a different stratum:

- [`iterate-while-dissolution`](./iterate-while-dissolution.md) (firm c047) — the **inner-fold combinator**: how the L4 `iterate_while` combinator (the `Solve`-threaded extras-carrying loop) dissolves into the L3 `iterate_while_L3` tail-recursive value-threaded worker. This is what the L4 `restart_cycle` invokes to fold `krylov-step`.
- [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) (firm) — the **per-step body**: how the L4 `krylov-step` typed wrapper (records, `Solve` monad, `OpParams` `readonly`) dissolves into the L3 value-threaded kernel `(op, K, s) -> (K', s', outputs)`.
- `ksp-solve-driver-dissolution` (this theme) — the **outer driver + termination classification**: how the L4 `solve_loop` / `restart_cycle` `do`-block coordination and the `Outcome` sum dissolve into the L3 outer fold + restart nesting + the scattered per-test termination branches + the soft-fail `Bool` `result.converged`.

The three compose: the full L4 `ksp_solve` cap lowers to the full L3 `ksp_solve` driver by applying this theme to the outer coordination, [`iterate-while-dissolution`](./iterate-while-dissolution.md) to the inner fold it invokes, and [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) to the per-step body that fold runs. This theme is the **dedicated home** for the outer-coordination stratum — a reader navigating from the firm `L4/ksp_solve` cap's §"Lowers to" lands here, at the driver dissolution, rather than re-deriving it inline or conflating it with the kernel theme.

The rotation direction is **L4 → L3**, narrated forward per the high→low discipline (CLAUDE.md §Methodology invariants "Layers are defined high→low"). Notes about the reverse lift (how the L3 explicit fold lifts back into the monadic cap) live in the cap's §"L4 vs L3 distinction" and in this report's working notes, not in this formal chapter.

## L4 form (LHS)

The L4 `ksp_solve` cap — the firm D1 outer-driver shape (`book/src/L4/ksp_solve.md` §Signature). The entry point and its two driver layers, transcribed from the firm cap (and the `solve-monad` concept §Shape, `book/src/concepts/solve-monad.md:10-17`):

    -- entry point: run the outer driver over the initial SimState, project the terminal state
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

The `restart_cycle` body has four phases in dataflow order (the firm cap §Semantics, mirroring `book/src/concepts/solve-monad.md:53-54`):

    restart_cycle op inp = do
      let K0          = fresh_krylov op inp s              -- 1. fresh ephemeral bundle (plain value)
      let (Kn, outs)  = iterate_while (krylov_step op K0) cont  -- 2. inner kernel-fold (iterate-while family)
      modify (\s -> s { x = s.x + Kn.V `dot` Kn.y })      -- 3. fold correction into SimState.x, once
      pure (classify Kn op s)                             -- 4. classify the terminal bundle into Outcome, once

The wrapper machinery this theme dissolves is **four** pieces (distinct from the inner-fold and per-step machinery the sibling themes dissolve):

1. **The `Solve = StateT SimState Identity` outer-driver threading** (`book/src/concepts/solve-monad.md:1-19`). `solve_loop`'s `do`-block and `restart_cycle`'s `Solve Outcome` action carry `SimState` (the `it` counter, the iterate `x`, the convergence flag) monadically; the entry point discharges it via `execState`.
2. **The `solve_loop` / `restart_cycle` `do`-block driver shape** — the `do { o <- restart_cycle …; unless (done o) (solve_loop …) }` tail recursion (the outer coordination), and `restart_cycle`'s four-phase `do`-block (the per-cycle coordination).
3. **The `Outcome = Continue | Done Bool` termination sum** — the single typed termination-decision site, classified once per cycle by `classify`, with `done` the pattern-match `solve_loop` reads.
4. **The once-per-cycle `modify`-correction** — the single `SimState.x` boundary write `modify (\s -> s { x = s.x + Kn.V · Kn.y })`, placed at the cycle boundary after the inner fold's `back_solve`.

The load-bearing L4 properties this lowering must transport are the cap's coordination identities (the firm cap §"Algebraic laws"): **Law 1 (`execState`/`StateT` discharge fusion)** — the cap is the `execState`-discharge of `solve_loop`, observably a pure `(op, inp) -> SimState`; **Law 2 (`solve_loop` tail-recursion ≡ `iterate_while_pure` over outer cycles)** — the outer driver degenerates to a pure fold over outer cycles because only the terminal `SimState` is observed (the `Outcome` values are consumed-and-discarded by the predicate, never accumulated); **Law 5 (`Outcome` classify-once / fold-uniformly)** — the three termination reasons are classified at exactly one site per cycle and `solve_loop` folds the `Bool` inside `Done` uniformly into `SimState.converged`.

## L3 form (RHS)

The L4>L3 dissolution produces the firm L3 value-threaded **outer-driver fold** [`L3/ksp_solve`](../L3/ksp_solve.md) `(op, K_0, s_0) -> (s_final, result)` (the firm L3 entry §Signature, `book/src/L3/ksp_solve.md:38-54`):

    ksp_solve :: (op, K_0, s_0) -> (s_final, result)

    ksp_solve op K_0 s_0 =
      let s_init                = init_convergence op K_0 s_0     -- residual proxy + eps + converged_0
      let (K_n, s_n, outputs_n) = iterate_while_L3                -- the outer-driver fold
                                    (krylov-step op)              --   body: the L3 kernel
                                    (K_0, s_init)                 --   seed carry
                                    (\s -> not s.converged && s.it < op.max_it)  -- predicate
      let s_final               = fold_iterate op K_n s_n         -- final iterate materialised into s.x
      let result                = extract_result s_final outputs_n -- the four-field readout
      in (s_final, result)

with the four-field result record (the firm L3 entry, `book/src/L3/ksp_solve.md:63-70`):

    result : {
      converged  : Bool,    -- s_final.converged; the L1 SolveResult.converged
      iterations : Int,     -- s_final.it;        the L1 SolveResult.iterations
      initial_res: Real,    -- s_final.initial_res
      final_res  : Real     -- s_final.final_res
    }

The dissolution is **four** coordinated rewrites, one per piece of L4 outer-driver machinery, each value-thread-isomorphic on the per-cycle dataflow:

### 1. `Solve` monad → explicit positional `(K, s)` threading

The L4 `Solve = StateT SimState Identity` threading dissolves to the L3 explicit positional `(K, s)` value-thread: `s_0` flows in positionally, `s_final` flows out positionally; there is no `Solve`, no `modify`, no `do`-block (the firm L3 entry §Signature note, `book/src/L3/ksp_solve.md:76-80` — "No `Solve` monad … the `do`-block / `StateT` threading dissolves into the explicit `iterate_while_L3` tail recursion plus positional `(K, s)` threading"). The `execState` discharge that the cap's Law 1 names becomes definitional at L3: the L3 fold *is* a pure function `(op, K_0, s_0) -> (s_final, result)`, so the projection-out-of-monad is already the return value. This is the outer-driver image of the same `Solve`-monad dissolution the inner fold undergoes ([`iterate-while-dissolution`](./iterate-while-dissolution.md) §"Unpruned form" — the `sim` thread surfaces positionally); here it applies to the *outer* coordination, not the inner-fold body.

### 2. `solve_loop` `do`/`unless` → `iterate_while_L3` outer tail recursion with the convergence predicate

The L4 `solve_loop op inp = do { o <- restart_cycle op inp; unless (done o) (solve_loop op inp) }` dissolves to the L3 outer-driver fold `iterate_while_L3 (krylov-step op) (K_0, s_init) (\s -> not s.converged && s.it < op.max_it)`. This is the **load-bearing collapse**: the cap's Law 2 (`solve_loop` ≡ `iterate_while_pure` over outer cycles, because only the terminal `SimState` is observed) is exactly what licenses rendering `solve_loop` as the L3 `iterate_while_L3` outer tail recursion. The combinator dissolution itself — how the L4 `iterate_while` becomes the L3 `iterate_while_L3` worker — is **delegated to** [`iterate-while-dissolution`](./iterate-while-dissolution.md) (this theme composes above it); what *this* theme adds is the **`Outcome` → predicate collapse**: the L4 `unless (done o)` guard (a pattern-match on the `Outcome` sum) dissolves into the L3 predicate's read of `s.converged` (the firm L3 entry §Signature note, `book/src/L3/ksp_solve.md:78` — "the convergence-flag `modify` becomes the predicate's read of `s.converged`"). The `Outcome`'s three arms scatter as follows:

- `Done True` (converged, `K.beta < ε`) → the predicate's `not s.converged` clause flips false, where `s.converged` was set from the per-step `outputs.residual_norm < eps` readout (the L0 `converged = (res < eps)`, `reference/palace/palace/linalg/iterative.cpp:463`).
- `Done False` (exhausted `op.max_it`) → the predicate's `s.it < op.max_it` clause flips false (the L0 loop guard `it < max_it`, `reference/palace/palace/linalg/iterative.cpp:427`).
- `Continue` (hit `op.max_dim`, restart warranted) → the outer restart loop's re-seed, NOT a termination — at L3 it is the outer `iterate_while_L3` whose body re-seeds `K` (a fresh basis) and whose predicate is `it < max_it` (the L0 restart loop `for (; it < max_it; restart++)`, `reference/palace/palace/linalg/iterative.cpp:563`; the firm L3 entry §Semantics restart-nesting paragraph, `book/src/L3/ksp_solve.md:94`).

So the single typed `Outcome`-decision site of the L4 cap **scatters** into the L3 form's predicate clauses (the two `Done` arms) plus the restart-loop re-seed (the `Continue` arm) — the de-classification that the L4 sum-type *un-does*. This is the L4>L3 statement of the firm cap §"L4 vs L3 distinction" ("L4 the coordination is typed … termination is the `Outcome` sum classified once per cycle; L3 the soft-fail is a `Bool`, the termination scattered into per-test branches").

### 3. `restart_cycle` per-cycle driver → restart nesting + once-per-cycle `fold_iterate` boundary write

The L4 `restart_cycle`'s four-phase `do`-block dissolves to the L3 restart nesting plus the `fold_iterate` boundary write:

- Phase 1 (`let K0 = fresh_krylov …`) → the L3 outer restart fold's per-cycle `K`-re-seed (`book/src/L3/ksp_solve.md:90` — the externally-visible iterate is folded "once per restart cycle from the basis correction `K.V · K.y`").
- Phase 2 (`let (Kn, outs) = iterate_while (krylov_step op K0) cont`) → the L3 inner fold `iterate_while_L3 (krylov-step op) …` — **delegated to** [`iterate-while-dissolution`](./iterate-while-dissolution.md) for the combinator dissolution and [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) for the body. The sole `SimState` effect inside (`modify (\s -> s { it = s.it + 1 })`) dissolves to the kernel's positional `s.it` increment.
- Phase 3 (`modify (\s -> s { x = s.x + Kn.V · Kn.y })`, the once-per-cycle correction) → the L3 `fold_iterate op K_n s_n` (`book/src/L3/ksp_solve.md:51,90`): for non-restarted methods (CG, Chebyshev) the running iterate `s.x` is updated in-bundle each step so `fold_iterate` is identity; for restarted methods (GMRES, FGMRES) it materialises the last partial restart-cycle's correction into `s.x`. The L4 `modify`'s single-named-mutation-point discipline (`book/src/concepts/solve-monad.md:27`) dissolves to the L3 explicit `s.x` boundary write.
- Phase 4 (`pure (classify Kn op s)`, the `Outcome` classification) → dissolves per rewrite (2) above (the predicate-read + restart re-seed) and rewrite (4) below (the `result.converged` field).

### 4. `Outcome` sum → soft-fail `Bool` `result.converged` + `extract_result`

The L4 `Outcome = Continue | Done Bool` sum dissolves to the L3 soft-fail `Bool` `result.converged`: the `Bool` inside `Done` becomes the L3 `result.converged` field, projected by `extract_result s_final outputs_n` (`book/src/L3/ksp_solve.md:52,92`). The cap's Law 5 (classify-once / fold-uniformly) dissolves into the L3 form's `extract_result`: the `converged` field is `s_final.converged` (the L0 `GetConverged()`, additionally gated on `rel_tol > 0 || abs_tol > 0`, `reference/palace/palace/linalg/iterative.hpp:98`); the `final_res` proxy is the per-method residual readout (`final_res = res` for CG, `reference/palace/palace/linalg/iterative.cpp:484-485`; `final_res = beta` for GMRES, `:703-704`). The L4 cap's structural improvement — `Done False` as a *first-class* termination arm — dissolves into the L3 form where soft-fail is *implicit* in `result.converged` being a `Bool` rather than a sum type (the firm L3 entry §"Variant axes" axis 4, `book/src/L3/ksp_solve.md:160`; the firm cap §"Variant axes" axis 1 names this as the L4 lift the dissolution reverses). The richer-than-`ksp_solve` partial-success arm the `eigsolve` cap carries (`0 < converged < requested`) has no `ksp_solve` analog — at L3 `ksp_solve`'s termination is exactly a `Bool`.

### What does NOT change in the rotation

The **per-cycle dataflow** survives the rotation textually unchanged — the four-phase cycle body's primitive sequence (`fresh_krylov`, the inner fold, the correction `+ K.V · K.y`, the classification reads `(K.beta, K.j, s.it, ε)`) passes through unchanged in dataflow position; the rotation touches only the **outer-driver wrapper**: the `Solve` monad becomes positional `(K, s)`, the `do`/`unless` driver becomes the `iterate_while_L3` predicate, the `Outcome` sum becomes the soft-fail `Bool`, the `modify`-correction becomes the `fold_iterate` boundary write. The inner kernel-fold and the per-step body pass through unchanged via the two sibling themes.

The **outer-loop `sequential-obstruction`** survives at L3: the L3 form names the outer driver tail-recursively but does **not** claim it lifts to a global tensor-field op — each cycle reads scalars (`β`, residual proxy) produced by the previous cycle, not closed-form in the carry (the firm cap §"Algebraic laws" non-law "Lift of the outer fold to a closed-form whole-state op", and the firm L3 entry §"Iteration-rotation marker", `book/src/L3/ksp_solve.md:100-104`). The L4 `Solve` monad makes the interior termination *visible* but does not *remove* the sequentiality (the `>>=` is sequential composition, not fusion); the dissolution carries the obstruction down unchanged.

### What this lowering does NOT cover

- **The inner `iterate_while` combinator dissolution** — delegated to [`iterate-while-dissolution`](./iterate-while-dissolution.md) (firm c047). This theme dissolves the *outer* driver (`solve_loop` / `restart_cycle` / `Outcome`); the inner-fold combinator (`iterate_while` → `iterate_while_L3`) is that theme's job. This theme composes strictly above it.
- **The per-step body dissolution** — delegated to [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) (firm). The `krylov-step` typed wrapper → L3 value-threaded kernel is that theme; this theme treats the body as opaque (`krylov-step op`).
- **The L3>L2 hop on the driver**, which is **substantive** (the L2 anchor erases the iteration view to an outer-driver-by-role reference; firm L3 entry §"Lowers to", `book/src/L3/ksp_solve.md:169-173`), pending the L2 `ksp_solve` promotion past `stub` — a separate L3>L2 theme (`L3-L2/ksp-solve-outer-driver`, pending), not duplicated here.

## Applicability conditions

The rewrite is valid when all four of the following hold (the first three inherited from [`iterate-while-dissolution`](./iterate-while-dissolution.md) §"Applicability conditions" applied to the outer driver; the fourth is the driver-specific `Outcome` condition):

1. **The L4 `Solve` monad's outer-driver effect domain is exactly `SimState`.** The only `modify`s in `solve_loop` / `restart_cycle` are the per-step `it` increment (inside the inner fold) and the once-per-cycle `x`-correction; no carry field (`K`) is monad-touched (`book/src/concepts/solve-monad.md:29-35`). This lets the monad dissolve to the single positional `s` thread alongside the positional `K`.

2. **The outer-driver predicate is pure on `SimState`.** `solve_loop`'s continuation (`not (done o)`, with `done` reading the classified `Outcome`) and the L3 predicate `\s -> not s.converged && s.it < op.max_it` read only `SimState` fields (`converged`, `it`) and the closure-captured `op.max_it` — no per-step extras, no `K` internals. This is what lets the L3 predicate read only the positional `s` argument (the firm L3 entry §Signature, `book/src/L3/ksp_solve.md:73-74`; the L0 guard `it < max_it && !converged`, `reference/palace/palace/linalg/iterative.cpp:427`).

3. **The per-cycle body's primitive sequence is L3-native or carries its own L3 classification.** The four-phase cycle body (`fresh_krylov`, the inner fold, the correction, the classification) is composed of L3-native whole-tensor ops plus the delegated inner kernel; the outer-driver dissolution does not change the body's L3 classification — it survives in form (the §"What does NOT change" verdict above).

4. **The `Outcome` sum is classified once per cycle against `SimState` + terminal-bundle scalars.** `restart_cycle`'s `classify Kn op s` reads `(Kn.beta, Kn.j, s.it, ε)` once at the boundary (`book/src/concepts/solve-monad.md:60-66`). This single-decision-site discipline is what lets the `Outcome` sum dissolve cleanly into the L3 predicate clauses + `result.converged` — the multi-reason classification scatters into per-test branches **only because** the L4 form concentrated it at one site (a form whose termination is already scattered at L4 would have no `Outcome` to dissolve). For Palace's `ksp_solve`, the soft-fail policy means the only `Bool` carried is `converged` (`reference/palace/palace/linalg/ksp.cpp:301-307` returns the iterate regardless; the `eigsolve` cap's richer partial-success sum has no `ksp_solve` analog).

## Justification kind

**`structural`** with secondary **`reduction-chain`**.

- **Structural** (dominant): the L4 outer-driver machinery (the `Solve` monad, the `solve_loop` / `restart_cycle` `do`-block drivers, the `Outcome` termination sum, the once-per-cycle `modify`-correction) dissolves into the L3 value-threaded outer-driver fold; the per-cycle dataflow is preserved by construction (every L4 per-cycle phase becomes an L3 per-cycle phase at the same dataflow position). The `Outcome` sum dissolves into the L3 predicate clauses + the soft-fail `Bool` `result.converged`; the `modify`-correction becomes the `fold_iterate` boundary write — both structural rewrites of the syntactic outer-driver sites.
- **Reduction-chain** (secondary): the `Solve` monad's `>>=` desugars to explicit positional `(K, s)` threading (the `modify (\s -> s { it = … })` to let-bound positional update, per `book/src/design/l4_calculus.md:131-136` §3.4 state-effect laws); the `solve_loop` `do`/`unless` tail recursion desugars to the `iterate_while_L3` outer fold (the cap's Law 2 fold-equivalence applied, `book/src/design/l4_calculus.md:150-184` §3.7); the `Outcome` pattern-match desugars to the predicate's `s.converged` read. The monad-law normal form (the firm cap §"Algebraic laws" Law 3, sharpened from `book/src/design/l4_calculus.md:119-136` §3.3-3.4) underwrites the per-cycle `modify`-fusion that licenses rendering each outer cycle as one composite `SimState` transition before the dissolution.

**Abstraction-direction note**: L4 is the higher-abstraction layer (the `Solve` monad, the typed `Outcome` sum, the single-decision-site classification, the `do`-block driver); L3 is the lower-abstraction layer (positional `(K, s)` threading, the soft-fail `Bool`, the scattered per-test predicate clauses, the explicit `iterate_while_L3` fold). The rotation direction is **L4 → L3**, narrated forward per the high→low discipline.

## Speculative L4 operators

None. This theme lowers an already-firm L4 cap ([`L4/ksp_solve`](../L4/ksp_solve.md), firm cycle-048 R2) assembled from already-firm L4 outer-driver vocabulary (`solve_loop` / `restart_cycle` / `Outcome`, firm cycle-047) folding the already-firm [`krylov-step`](../L4/krylov-step.md) kernel via the firm [`iterate-while`](../L4/iterate-while.md) family. No new speculative operator is introduced.

## Verified-against

L4 source (the LHS of this rewrite):

- `book/src/L4/ksp_solve.md` (firm cycle-048 R2; **same-cycle sibling** — authored by D1, lands at integration before the single finalize build; the live link resolves once D1's create is applied) — the firm L4 outer-driver cap: §Signature (the `ksp_solve` / `solve_loop` / `restart_cycle` / `Outcome` shape), §Semantics (the four-phase `restart_cycle`), §"Algebraic laws" (Law 1 `execState`/`StateT` fusion, Law 2 `solve_loop`-as-`iterate_while_pure`, Law 5 `Outcome` classify-once — the load-bearing transported properties), §"Lowers to" (the in-line rotation-direction record this theme realizes), §"L4 vs L3 distinction".
- `book/src/L4/krylov-step.md` (firm cycle-006) — the inner kernel-fold body `restart_cycle` runs (the per-step body, delegated to its own theme).
- `book/src/L4/iterate-while.md` (firm cycle-007) — the inner-fold combinator `restart_cycle` invokes (the combinator dissolution delegated to `iterate-while-dissolution`).
- `book/src/concepts/solve-monad.md:1-68` — the `Solve = StateT SimState Identity` outer-driver pattern: §Shape (`:5-19`, the `solve` / `solve_loop` entry point), §"What stays out of the monad" (`:29-35`, the `K`-out-of-monad discipline), §"Worked example — GMRES" (`:47-56`, the four-phase `restart_cycle`), §"Termination as a sum type" (`:58-68`, the `Outcome` classify-once / fold-uniformly law).
- `book/src/design/l4_calculus.md:119-136` — §3.3 monad laws (`:121-127`) + §3.4 state effects (`:131-136`), underwriting the reduction-chain `>>=`-to-positional-threading and the monad-law normal form. `:150-184` — §3.7 `iterate_while` + `iterate_while_pure` sugar (`:178-182`), the fold-equivalence the `solve_loop` collapse cites. `:186-228` — §3.8 demand-pruning (the trajectory-vs-classifier demand split inherited through the inner fold).

L3 source (the RHS of this rewrite):

- `book/src/L3/ksp_solve.md` (firm cycle-020) — the dissolution target: §Signature (`:38-74`, the `(op, K_0, s_0) -> (s_final, result)` fold + the four-field `result` + the convergence predicate), the three-piece L4-wrapper-absent note (`:76-80`, "No `Solve` monad"), §Semantics (`:84-98`, the four-phase fold + restart nesting), §"Iteration-rotation marker" (`:100-104`, the outer-loop `sequential-obstruction`), §"Variant axes" axis 4 (`:160`, the soft-fail `Bool` the `Outcome` sum dissolves to), §"Lowers to" (`:169-173`, the further substantive L3>L2 hop).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:158-200` — the kernel-half precedent: §"What the L3 form for `iterate_while` looks like" (the unpruned/pruned L3 fold forms; the `Solve`-monad-to-positional-`sim` dissolution this theme's outer-driver dissolution parallels).
- `book/src/L4-L3/iterate-while-dissolution.md` (firm cycle-047) — the inner-fold combinator dissolution this theme composes strictly above (the `iterate_while` → `iterate_while_L3` worker dissolution `restart_cycle`'s phase 2 invokes).

L0 evidence (transitive via the firm L3 driver; citecheck-verified this dispatch):

- `reference/palace/palace/linalg/iterative.cpp:417-418` — `eps = max(rel_tol·initial_res, abs_tol)` + pre-loop `converged = (res < eps)` short-circuit (the cap's `Done`-on-entry; the L3 zero-RHS short-circuit).
- `reference/palace/palace/linalg/iterative.cpp:427` — CG single-loop outer-driver guard `for (; it < max_it && !converged; it++)` (the L3 predicate the `solve_loop` `do`/`unless` dissolves into; the `Done False` / `Done True` arms).
- `reference/palace/palace/linalg/iterative.cpp:463` — the in-loop convergence test `converged = (res < eps)` (sets `s.converged`; the `Done True` arm's predicate clause).
- `reference/palace/palace/linalg/iterative.cpp:484-485` — CG result write `final_res = res; final_it = it;` (the `extract_result` residual proxy for non-restarted).
- `reference/palace/palace/linalg/iterative.cpp:563` — GMRES restart outer loop `for (; it < max_it; restart++)` (the `Continue` arm's re-seed; the L3 restart nesting).
- `reference/palace/palace/linalg/iterative.cpp:703-704` — GMRES result write `final_res = beta; final_it = it;` (the `extract_result` LS-residual proxy for restarted).
- `reference/palace/palace/linalg/iterative.hpp:52-55` — the four result fields `converged` / `initial_res` / `final_res` / `final_it` (the L3 `result` record origins; the `Outcome`-`Bool` dissolution target).
- `reference/palace/palace/linalg/iterative.hpp:98` — `GetConverged()` with its `rel_tol > 0 || abs_tol > 0` gate (folded into the L3 `extract_result` `converged` readout).
- `reference/palace/palace/linalg/iterative.hpp:101-108` — accessors `GetInitialRes` / `GetFinalRes` / `GetNumIterations`.
- `reference/palace/palace/linalg/ksp.cpp:296-310` — `BaseKspSolver::Mult` — the soft-fail policy: `:301-307` logs a warning and returns the iterate regardless (no abort), the basis of the cap's `Done False` first-class arm / the L3 soft-fail `Bool`; counters `:308-309` are the driver-side cumulative accumulators above both the cap and the L3 fold.

Concept-page references:

- [`solve-monad`](../concepts/solve-monad.md) — the `Solve = StateT SimState Identity` outer-driver monad that dissolves to the positional `(K, s)` thread; the `Outcome` classify-once law.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the outer-loop non-lift surviving the dissolution at L3.
- [`convergence-test`](../concepts/convergence-test.md) — the stopping predicate the `Outcome` classification reads and the L3 predicate becomes.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the §3.8 demand-pruning algebra governing the trajectory-vs-classifier demand split (inherited through the inner fold).

## Status

`firm` — the dissolution of the firm L4 `ksp_solve` outer-driver cap ([`L4/ksp_solve`](../L4/ksp_solve.md), firm cycle-048 R2) into the firm L3 outer-driver fold ([`L3/ksp_solve`](../L3/ksp_solve.md), firm cycle-020). The four coordinated rewrites (the `Solve` monad → positional `(K, s)` threading; the `solve_loop` `do`/`unless` → `iterate_while_L3` predicate with the `Outcome` → predicate-read collapse; the `restart_cycle` four-phase → restart nesting + `fold_iterate` boundary write; the `Outcome` sum → soft-fail `Bool` `result.converged`) are exhaustively cited against the firm cap's §Signature / §Semantics / §"Algebraic laws", the firm L3 entry's §Signature / §Semantics / §"Variant axes", the `solve-monad` concept (`:1-68`), the strawman §3.3-3.4 / §3.7 / §3.8, and the citecheck-verified L0 anchors. Justification is `structural` + secondary `reduction-chain`. No speculative operator introduced. This theme **composes strictly above** the firm inner-fold dissolution [`iterate-while-dissolution`](./iterate-while-dissolution.md) (the combinator the L4 `restart_cycle` invokes) and is the **driver-half** companion to the firm per-step-body dissolution [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md). This chapter completes the cycle-048 R2 cap with its dedicated rotation theme (the cycle-046 survey flagged it warranted, parallel to the kernel-half theme), serving `l4-l3-coverage-and-l4-expansion`; it realizes the in-line rotation direction the firm cap's §"Lowers to" records and closes the lowering half of OQ `l4-ksp-solve-eigsolve-caps-gated-on-solve-monad-outer-driver-vocabulary` for `ksp_solve`.

## L4 vs L3 distinction

- **L4**: the `Solve`-monadic outer-driver cap. `solve_loop` / `restart_cycle` thread `SimState` through the `Solve = StateT SimState Identity` monad; termination is the `Outcome = Continue | Done Bool` sum classified once per cycle at a single typed decision site; the per-cycle `x`-correction is a single named `modify` point; the outer driver is a `do`-block tail recursion whose convergence test (`unless (done o)`) is lifted to the coordination layer.
- **L3**: the value-threaded outer-driver fold `(op, K_0, s_0) -> (s_final, result)`. The `Solve` monad has dissolved to positional `(K, s)` threading; termination is the soft-fail `Bool` `result.converged`, scattered across the predicate's two clauses (`not s.converged`, `s.it < op.max_it`) and the restart loop's re-seed; the per-cycle `x`-correction is the explicit `fold_iterate` boundary write; the outer driver is the explicit `iterate_while_L3 (krylov-step op)` tail recursion. The outer-loop `sequential-obstruction` is named at both layers (the monad makes interior termination visible but does not remove the sequentiality).

The two layers share the per-cycle dataflow shape (modulo wrapper dissolution) and the four-phase cycle body; they differ in **effect threading, termination-classification placement, and the iteration-view explicitness**. The rotation erases the monadic packaging, scatters the single `Outcome`-decision site into the L3 predicate + restart re-seed, dissolves the `Outcome` sum to the soft-fail `Bool`, and renders the outer driver as an explicit `iterate_while_L3` fold — narrated forward L4→L3.
