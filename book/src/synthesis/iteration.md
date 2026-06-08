---
kind: navigational-container (synthesis library — iteration)
# Rendered library chapter. No `rank:` — implementation VIEW, reference-class
# links only; the rendered def bodies are faithful transcriptions of the
# authoritative L4 chapter bodies (lowering-verifier may audit), they carry no
# new `depends-on` blocking edge and constrain no firm node's rank/liveness.
edges:
  reference:
    - L4/iteration-combinators-intro
    - L4/chebyshev
    - L4/iterate_while
    - L4/iterate_while_with_prev
    - L4/krylov_step
    - concepts/krylov
    - concepts/StepOutputs
    - concepts/PrevCarry
    - concepts/SimState
    - concepts/OpParams
    - concepts/solve-monad
    - concepts/first-iteration-unrolling
    - concepts/derived-view-hoisting
    - synthesis/types
    - synthesis/index
---

# Library `iteration` — iteration & step combinators

The synthesized rendering of the L4 [Iteration & step combinators](../L4/iteration-combinators-intro.md) doc-group: the value-threaded loop combinators and the step kernels that drive Palace's iterative algorithms. Implementation VIEW — links to the authoritative L4 chapters for laws/semantics, renders the synthesized code form here.

## Operators this library holds (topological order)

A def appears after everything it uses:

1. [`iterate_while`](../L4/iterate_while.md) — value-threaded tail-recursive loop with demand-pruned trajectory; the canonical iteration primitive (everything below uses it).
2. [`iterate_while_with_prev`](../L4/iterate_while_with_prev.md) — carry-bootstrapped variant threading a `PrevCarry` closure; degenerates to `iterate_while` when `β = ()`.
3. [`krylov_step`](../L4/krylov_step.md) — the typed-wrapper Krylov step kernel; Form A consumes `iterate_while`, Form B consumes `iterate_while_with_prev`.
4. [`chebyshev`](../L4/chebyshev.md) — the fixed-degree polynomial smoother; both bounded loops are `iterate_while` folds with step-count predicates.

## Clustering types (rendered before the group)

Per the [type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group), the iteration-clustering state carriers — [`Krylov`](../concepts/krylov.md), [`StepOutputs`](../concepts/StepOutputs.md), [`PrevCarry`](../concepts/PrevCarry.md) — are rendered **immediately before** the operator group, bundled with their utility API (constructors / accessors / predicates). Their consumer methods stay in the group AFTER the type+utility block. The cross-cutting `SimState` / `OpParams` are shared and live in [`types`](./types.md), not here.

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order; `#extern NAME` after the type signature for any opaque-kernel boundary; deep-linked-unchanged lower artifacts rendered inline; Haskell `where` for private helpers; code-doc per def; `$`-sigil pseudocode inside ` ```text ` fences (KaTeX rule); link to `../L4/<op>.md`, do not re-cite L0.

---

# Clustering types

These are the iteration-clustering state carriers. The authoritative field schemas (fields, types, strata, L0 source home) live in the linked `concepts/<record>.md` pages; this is the synthesized type-def form + the type's *utility* API (constructors / accessors / predicates). The substantive operators that *consume* these types are in [Library defs](#library-defs) below.

## `Krylov` — the ephemeral per-restart workspace

The ephemeral-intermediates stratum: a solve-local working bundle, born at restart entry, discarded at restart exit. Threaded through the kernel as a **plain value**, not a monadic effect (its lifetime is strictly within one restart cycle). Slice-specific schema. Authoritative schema + strata + L0 home: [`krylov`](../concepts/krylov.md).

```text
-- Slice-specific ephemeral workspace; born at restart, discarded at restart exit.
-- Authoritative schema + field strata + L0 home: concepts/krylov.md
-- iterate-stratum fields are congruent solution-space vectors over shape group S
-- (semantics/index.md §1.2.1); scalar-stratum fields are small-dense.

type Krylov_CG = {
  r  : Tensor[$S],   -- residual
  p  : Tensor[$S],   -- search direction
  z? : Tensor[$S],   -- preconditioned residual (present iff a preconditioner is set)
  alpha : Scalar,    -- step length
  beta  : Scalar     -- direction-update coefficient (the residual proxy convergence-test reads)
}

type Krylov_GMRES = {
  V  : [Tensor[$S]],   -- Arnoldi basis (array of basis columns)
  Z? : [Tensor[$S]],   -- preconditioned basis (present iff OpParams.flexible — FGMRES)
  H  : DenseMatrix,    -- upper-Hessenberg (small-dense, scalar-stratum)
  s  : [Scalar],       -- least-squares RHS / rotated residual (small-dense)
  cs : [Scalar],       -- Givens cosines (small-dense)
  sn : [Scalar],       -- Givens sines (small-dense)
  beta : Scalar,       -- current residual proxy
  j    : Int           -- inner-iteration index within the restart cycle
}

-- # Utility API (the type's own intrinsic namespace; consumer methods are in the group below)
-- mkKrylovCG    :: OpParams -> Tensor[$S] -> Krylov_CG       -- born from b at restart/solve entry
-- mkKrylovGMRES :: OpParams -> Tensor[$S] -> Krylov_GMRES    -- fresh per restart cycle (V grown lazily)
-- residualProxy :: Krylov_CG -> Scalar                       -- beta = (Br, r); the convergence-test input
-- residualProxyGMRES :: Krylov_GMRES -> Scalar               -- |s[j+1]|; the LS-residual estimate
```

## `StepOutputs` — the demand-prunable per-step readout

The result-side record carrying the observations a step makes about itself (residual proxy, LS residual, breakdown signal), so the outer driver reads them without inspecting `Krylov` internals. Every field is a pure derived view of the post-step `Krylov` bundle and is demand-prunable (the [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) Law 1). Authoritative schema: [`StepOutputs`](../concepts/StepOutputs.md).

```text
-- result-side, per-step, derived; reborn each step. Authoritative: concepts/StepOutputs.md
type StepOutputs = {
  residual_norm    : Scalar,        -- ‖r‖ proxy this step (CG: sqrt|beta|); always present
  ls_residual?     : Scalar,        -- GMRES/FGMRES LS residual estimate |s[j+1]|
  breakdown_token? : BreakdownTag   -- partiality signal: guarded-quantity validity tag (CheckDot)
}

type BreakdownTag = Ok | NotPositiveDefinite | NotFinite   -- slice-specific (the one constructed sub-part)

-- # Utility API
-- noBreakdown  :: StepOutputs -> Bool                      -- breakdown_token absent or Ok (a predicate)
-- residualNorm :: StepOutputs -> Scalar                    -- trivial projection
```

## `PrevCarry` — the Form-B closure-threaded recurrence carry

The closure-threaded recurrence carry the [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) rotation moves *out of* the steady-state schema and threads through the loop driver as a closure argument. Appears only in **Form B** of `krylov_step`. It has no L0 struct — it is a constructive artifact of the unrolling (Palace keeps the in-loop `if it==0` branch). Authoritative schema: [`PrevCarry`](../concepts/PrevCarry.md).

```text
-- carry-stratum (threaded across steps after the first, reborn per solve); no L0 struct.
-- Authoritative schema + negative L0 anchoring: concepts/PrevCarry.md
type PrevCarry = { <recurrence-variable> }     -- slice-specific single-slot carry
-- CG / PCG:  PrevCarry = { beta_prev : Scalar }   -- β_{k-1} = (Br, r)_{k-1}
-- GMRES:     PrevCarry = { H_prev    : Scalar }   -- H_{k,k-1} sub-diagonal Hessenberg entry
```

---

# Library defs

The four iteration & step combinators, in topological order. Each is the synthesized code form of its authoritative L4 chapter body (linked); the laws/semantics live in that chapter, not here.

## `iterate_while` — canonical value-threaded loop

The tail-recursive value-threading loop combinator: folds a step over an initial carry, threading the carry forward and accumulating per-step extras into a trajectory, until the predicate returns `False`. The canonical iteration primitive — every iterative algorithm reduces to one or more `iterate_while` folds. Authoritative def + laws (incl. the demand-pruning Law 1): [`iterate_while`](../L4/iterate_while.md).

```text
-- # Arguments
--   a    : α          -- the value-threaded carry (immutable); init
--   cont : α -> Bool  -- loop predicate, PURE on the carry; fires before each step
--   step : α -> Solve { state: α, ...e }  -- per-step body; Solve effect on SimState only
-- # Returns
--   Solve { final_state: α, trajectory: [{ ...e }] }
--     final_state -- the final carry value
--     trajectory  -- per-step extras in iteration order; demand-pruned when only
--                    final_state is observed (derived-view-hoisting Law 1)
-- # Shape contract
--   α, e are arbitrary L4 types instantiated per use (CG: α = CgState, e = {residual_norm});
--   the carry's iterate fields are congruent over shape group S (semantics/index.md §1.2.1).

iterate_while :: α -> (α -> Bool) -> (α -> Solve { state: α, ...e })
              -> Solve { final_state: α, trajectory: [{ ...e }] }
iterate_while a cont step =
  if cont a
    then do
      { state: a', ...e } <- step a
      { final_state, trajectory } <- iterate_while a' cont step
      pure { final_state, trajectory: [{ ...e }] ++ trajectory }
    else
      pure { final_state: a, trajectory: [] }

-- the no-extras / no-Solve sugar (the LBM-shape bounded loop): e = (), body non-monadic.
iterate_while_pure :: α -> (α -> Bool) -> (α -> α) -> α
iterate_while_pure a cont f =
  (iterate_while a cont (\x -> pure { state: f x })).final_state
```

## `iterate_while_with_prev` — carry-bootstrapped variant

The bootstrap-then-tail-recurse variant: fires a `bootstrap_step` once to produce the initial `prev` closure value, then threads `prev` (the prior step's recurrence variable) through each `steady_step` as a positional argument. Used exactly where [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) has hoisted a `_prev` field out of the steady carry. Degenerates to `iterate_while` when `β = ()`. Authoritative def + laws: [`iterate_while_with_prev`](../L4/iterate_while_with_prev.md).

```text
-- # Arguments
--   boot   : α -> Solve { state: α, prev: β, ...e }        -- bootstrap; fires once, produces initial prev
--   a0     : α                                             -- initial carry
--   steady : (α, β) -> Solve { state: α, prev: β, ...e }   -- branch-free steady body; (carry, prev)
--   cont   : α -> Bool                                     -- predicate, PURE on carry; fires after boot
-- # Returns
--   Solve { final_state: α, trajectory: [{ ...e }] }       -- trajectory includes boot's extras first
-- # Shape contract
--   α carry, β PrevCarry, e extras — all arbitrary L4 types. The argument order
--   boot/init/steady/cont and the (carry-first, prev-second) steady closure order
--   are canonical (match the CG v0.5 call site).

iterate_while_with_prev
  :: (α -> Solve { state: α, prev: β, ...e })
  -> α
  -> ((α, β) -> Solve { state: α, prev: β, ...e })
  -> (α -> Bool)
  -> Solve { final_state: α, trajectory: [{ ...e }] }
iterate_while_with_prev boot a0 steady cont = do
  { state: a1, prev: b0, ...e0 } <- boot a0
  { final_state, trajectory } <- steady_loop a1 b0
  pure { final_state, trajectory: [{ ...e0 }] ++ trajectory }
  where
    -- the tail-recursive worker: identical to iterate_while's recursion modulo
    -- threading prev (β) as a second positional argument.
    steady_loop a b =
      if cont a
        then do
          { state: a', prev: b', ...e } <- steady (a, b)
          { final_state, trajectory } <- steady_loop a' b'
          pure { final_state, trajectory: [{ ...e }] ++ trajectory }
        else
          pure { final_state: a, trajectory: [] }
```

## `krylov_step` — the typed-wrapper Krylov step kernel

The per-step kernel of an iterative Krylov-shaped solve, embedded in the `Solve` monad against the three-stratum state typing. The body folded by `iterate_while` (Form A) / `iterate_while_with_prev` (Form B). The kernel's sole monadic effect is the `SimState.it` counter increment; the iterate `SimState.x` is written at restart-cycle boundaries, not per step. The per-step bundle update `krylov_update` and the optional auxiliary stage `op.orthog` cross to the L2 named compositions ([`L2/krylov_step`](../L2/krylov_step.md) §Semantics; [`L2/orthogonalize`](../L2/orthogonalize.md)) — rendered here as the L4-chapter dataflow, not lifted. Authoritative def + laws: [`krylov_step`](../L4/krylov_step.md).

```text
-- # Arguments (Form A — branch-in-body, default; CG v0.4-shape)
--   op : OpParams   -- readonly operator-internal config (variant-absorbed); see types.md
--   K  : Krylov     -- the ephemeral per-restart workspace (plain value); see Krylov above
--   s  : SimState   -- threaded by Solve = StateT SimState Identity; see types.md
-- # Returns
--   Solve { krylov: Krylov', outputs: StepOutputs }
--     -- the next SimState is returned through the monadic state transition (modify),
--        not by structural projection; krylov' is a fresh plain value; outputs is
--        the demand-prunable per-step readout.
-- # Shape contract
--   OpParams readonly (variant selectors never re-inspected in the body); Krylov
--   mixed-stratum (Tensor[$S] iterate fields + scalar-stratum dense fields); the
--   Solve effect domain is exactly SimState.

krylov_step :: OpParams -> Krylov -> (SimState -> Solve { krylov: Krylov, outputs: StepOutputs })
krylov_step op K = \s -> do
  -- operator apply on the iterate-side input (no SimState read; no monad effect)
  let w     = apply_linop op.T K.<input_field>
  -- optional auxiliary stage, statically selected by op (one branch, variant-absorbed):
  --   GMRES/Arnoldi: apply op.orthog (K.V_prefix, w)   -- crosses to L2/orthogonalize
  --   Chebyshev:     apply op.scalars (K.k, K.scalar_state)
  --   CG:            no-op
  let K_aux = optionally_apply_auxiliary op K w
  -- Krylov-bundle update (pure on K; the L1 iterate/scalar primitives — axpy / axpby
  -- / axpbypcz / dot / nrm2 / scal — staged in the dataflow-forced order of L2/krylov_step)
  let K'    = krylov_update K_aux op w
  -- derived view of the post-step bundle (demand-pruned per derived-view-hoisting)
  let outputs = derived_views K' op        -- residual_norm; GMRES ls_residual; breakdown_token
  -- the sole monadic effect: increment the SimState iteration counter
  modify (\s -> s { it = s.it + 1 })
  pure { krylov: K', outputs }
```

**Form B — first-iteration-unrolled** (CG v0.5-shape; opt-in per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)). The body splits into a `first_step` (produces the initial `PrevCarry`) and a branch-free `steady_step` (consumes `PrevCarry` as a closure argument); the `Krylov` schema is one slot lighter. The canonical CG instantiation (the worked datum grounding Form B):

```text
-- The v0.5 CgState schema (one scalar lighter than v0.4 — beta_prev is gone, threaded
-- as the PrevCarry closure parameter).
type CgState = {
  x: Tensor[$S], r: Tensor[$S], p: Tensor[$S],
  beta: Scalar,          -- (r, r); nonzero on entry to a steady step
  it: Int, converged: Bool
}

-- first step (precondition it==0 ⇒ p ← r unconditionally; the Form-A branch is hoisted out)
cg_first_step :: LinOp[$S] -> Scalar -> CgState -> { state: CgState, residual_norm: Scalar }
cg_first_step opA eps s =
  let p'    = s.r in                          -- it == 0 ⇒ p ← r
  let Ap    = apply_linop opA p' in
  let alpha = s.beta / dot Ap p' in
  let x'    = axpy alpha p' s.x in
  let r'    = axpy (negate alpha) Ap s.r in
  let beta' = dot r' r' in
  let res'  = sqrt (abs beta') in
  { state: { x: x', r: r', p: p', beta: beta', it: 1, converged: res' < eps },
    residual_norm: res' }

-- steady step (branch-free; precondition it>=1, beta_prev > 0; beta_prev is the closure carry)
cg_steady_step :: LinOp[$S] -> Scalar -> Scalar -> CgState -> { state: CgState, residual_norm: Scalar }
cg_steady_step opA eps beta_prev s =
  let p'    = axpby 1.0 s.r (s.beta / beta_prev) s.p in
  let Ap    = apply_linop opA p' in
  let alpha = s.beta / dot Ap p' in
  let x'    = axpy alpha p' s.x in
  let r'    = axpy (negate alpha) Ap s.r in
  let beta' = dot r' r' in
  let res'  = sqrt (abs beta') in
  { state: { x: x', r: r', p: p', beta: beta', it: s.it + 1, converged: res' < eps },
    residual_norm: res' }

-- the driver: run the first step, then fold cg_steady_step with iterate_while_with_prev,
-- threading the prior step's beta as the next step's beta_prev (closure carry, not a field).
cg_solve :: !CgConfig -> LinOp[$S] -> Tensor[$S] -> Tensor[$S] -> Bool
         -> { final_state: CgState, residual_history: [Scalar] }
cg_solve config opA b x_initial initial_guess =
  let { state: s0, initial_res } = cg_init opA b x_initial initial_guess in
  let eps = max (config.rel_tol * initial_res) config.abs_tol in
  if sqrt (abs s0.beta) < eps
    then { final_state: { ...s0, converged: True }, residual_history: [] }
    else
      let { state: s1, residual_norm: res1 } = cg_first_step opA eps s0 in
      if s1.converged || s1.it >= config.max_it
        then { final_state: s1, residual_history: [res1] }
        else
          let { final_state, trajectory } =
            iterate_while_with_prev
              (\_ -> pure { state: s1, prev: s0.beta })          -- bootstrap: seed (s1, beta_prev=s0.beta)
              s1
              (\(s, beta_prev) ->
                 let r = cg_steady_step opA eps beta_prev s in
                 pure { state: r.state, prev: s.beta, residual_norm: r.residual_norm })
              (\s -> s.it < config.max_it && not s.converged) in
          { final_state, residual_history: [res1] ++ trajectory.map (\t -> t.residual_norm) }
```

## `chebyshev` — fixed-degree polynomial smoother

The Chebyshev smoother as a constructed `ChebOp` closure whose `apply` is a `Solve`-monad action over a capability-typed `ChebSim` (`x: Read`, `y: ReadWrite`). Inner-product-free and convergence-test-free: the two sequential obstructions (the outer `pc_it` Richardson sweep, the inner `k`-recurrence) are nested `iterate_while_pure` folds with **step-count predicates** (the bound folded into the carry counter) — they do not collapse. The variant (4th-kind / 1st-kind) is absorbed into the closure type `S` at `setup` — `apply` has no apply-time discriminator. Authoritative def + laws: [`chebyshev`](../L4/chebyshev.md).

```text
-- # Types
type ChebOp E S = {
  A: LinOp[E], dinv: Tensor[E, $V], order: Int, pc_it: Int,
  scalarInit: S,
  scalars: (Int, S) -> { α₀?: E, sd?: E, sr?: E, st: S }   -- pure scalar recurrence; variant-absorbed
}
type ChebSim E = { x: Read[Tensor[E, $V]], y: ReadWrite[Tensor[E, $V]] }
type Variant = Kind4 | Kind1   -- consumed only by setup; S = Unit (4th) | { rho_prev: E } (1st)

-- # setup — constructs the readonly ChebOp closure (a Solve action: issues a spectrum-estimate sub-solve)
-- # Arguments: A (SPD operator); p (SetupParams: order, pc_it, sf_max, sf_min); variant
-- # Returns: Solve s (ChebOp E S) — an immutable operator closure, not new SimState
setup :: LinOp[E] -> SetupParams -> Variant -> Solve s (ChebOp E S)
setup A p variant = do
  let dinv = recip (extractDiagonal A)
  lam_max <- (p.sf_max *) <$> spectrumEstimate A dinv
  case variant of
    Kind4 -> pure { A, dinv, order: p.order, pc_it: p.pc_it
                  , scalarInit: (), scalars: scalars4 lam_max }
    Kind1 -> do
      let sf_min_eff = if p.sf_min > 0 then p.sf_min
                       else 1.69 / (p.order ** 1.68 + 2.11 * p.order + 1.98)
      let lam_min = sf_min_eff * lam_max
      let theta   = (lam_max + lam_min) / 2
      let delta   = (lam_max - lam_min) / 2
      pure { A, dinv, order: p.order, pc_it: p.pc_it
           , scalarInit: { rho_prev: delta / theta }
           , scalars: scalars1 theta delta }

-- # apply — pc_it Richardson sweeps of a degree-order matrix polynomial of D⁻¹A
-- # Arguments: op (the readonly ChebOp); initial_guess (Bool; degenerate-case absorption)
-- # Returns: Solve (ChebSim E) ()  — the only product is the SimState transition (accumulated y)
apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()
apply op initial_guess = do
  x <- readX
  -- outer pc_it sweep: bounded iterate_while_pure with a step-count predicate; the sweep
  -- counter is the only carry field (y is the orthogonal Solve effect). Trajectory empty.
  _ <- iterate_while_pure
         { it: 1 }
         (\s -> s.it <= op.pc_it)
         (\s -> do { sweep op initial_guess s.it; pure { it: s.it + 1 } })
  pure ()
  where
    -- one Richardson sweep; y accumulator is the Solve-monad effect
    sweep op initial_guess it = do
      -- 1. residual r0 = x − A·y  (or r0 = x; y := 0 on first sweep without a guess)
      r0 <- if it == 1 && not initial_guess
              then do { writeY zero; pure x }
              else do { y <- readY; ay <- applyLinop op.A y; pure (x .-. ay) }
      -- 2. initial direction d0 = α₀ · (dinv ⊙ r0)
      let { α₀: c0, st: st0 } = op.scalars 0 op.scalarInit
      let d0 = c0 .* (op.dinv .*. r0)
      -- 3. inner k-recurrence: bounded iterate_while_pure with a step-count predicate;
      --    the recurrence tuple (r, d, st) plus the counter k is the value-threaded carry.
      cN <- iterate_while_pure
              { r: r0, d: d0, st: st0, k: 1 }
              (\c -> c.k <= op.order - 1)
              (\c -> do
                 modifyY (\y -> y .+. c.d)                 -- y += d  (Solve effect)
                 ad <- applyLinop op.A c.d
                 let r' = c.r .-. ad                        -- r −= A·d
                 let { sd, sr, st: st' } = op.scalars c.k c.st
                 let t  = op.dinv .*. r'                    -- dinv ⊙ r'
                 let d' = sd .* c.d .+. sr .* t             -- d = sd·d + sr·t
                 pure { r: r', d: d', st: st', k: c.k + 1 })
      -- 4. final accumulation
      modifyY (\y -> y .+. cN.d)
```

`MultTranspose` is L4-trivial under operator symmetry: `applyTranspose op = apply op` for SPD `A`.

## Kernel boundaries

This library has **no `#extern` kernel** of its own: the iteration combinators are pure calculus, and the step kernels' opaque-library boundary kernels (the libCEED quadrature inside `apply_linop` / `op.A`, the SLEPc eigsolve loop) belong to the operators that own those applies — they render `#extern` in the [`data-algebra`](./data-algebra.md) (`fe_assemble` / `mk_matrix_free_operator`) and [`coordination`](./coordination.md) (`eigsolve`) libraries. Here, `apply_linop` / `applyLinop` is the abstract operator-apply surface the step bodies fold; its constructive impl and `#extern` boundary are rendered where the operator is constructed, not here.

## Status

`navigational-container` (rendered library chapter). Holds the synthesized def bodies of the four iteration & step combinators (`iterate_while` / `iterate_while_pure`, `iterate_while_with_prev`, `krylov_step` Form A + Form B, `chebyshev`) plus the three iteration-clustering type renderings (`Krylov`, `StepOutputs`, `PrevCarry`). The rendered bodies are faithful transcriptions of the authoritative L4 chapter bodies (linked per def; lowering-verifier may audit the correspondence); the laws/semantics live in those chapters. Implementation VIEW — `reference`-class links only, no `depends-on` edge, no rank claim on any rendered form.
