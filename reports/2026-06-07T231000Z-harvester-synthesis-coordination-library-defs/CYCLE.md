---
agent: harvester
invoked_at: 2026-06-07T231000Z
scope: synthesis library — coordination (outer-driver caps & coordination combinators) def bodies
status: integrated
integrated_at: 2026-06-07T230000Z
integration_commit: 5828a07
integration_notes: |
  Applied cycle-136 (batch-44 LEAD/OPENER, Wave-2). Merged def bodies onto the coordination shell — preconditioning-framework/ksp_solve/eigsolve/solve_family/frequency_sweep/fold_solve + the coordination type block. The EigState in-chapter type block RESOLVES the D1 OQ record-EigState-needs-definition-home (single-consumer, back-linked to EigResult). 2 #extern kernel-API callouts after type sigs. Reference edges all reference-class. Build EXIT 0; rank_violations=0; KaTeX $-sigil-fence PASS; closure-signature + #extern-placement COMPLIANT. Finalize normalized the `status:` token (filled VIEW chapter carries no `status:` field).
inputs:
  - reports/2026-06-07T230500Z-layer-intro-author-synthesis-section-shell/CYCLE.md (the Part shell + the coordination.md intro shell this MERGES-WITH)
  - book/src/L4/ksp_solve.md (firm — the cap def rendered)
  - book/src/L4/eigsolve.md (firm — the opaque-library cap; SLEPc EPS loop → #extern)
  - book/src/L4/preconditioning-framework.md (firm — buildKspSolver / setOperators construction surface)
  - book/src/L4/solve_family.md (firm — fixed-operator map)
  - book/src/L4/fold_solve.md (firm — state-threaded fold; opaque time_step_op → #extern)
  - book/src/L4/frequency_sweep.md (firm — operator-varying map)
  - book/src/concepts/solve-monad.md (the Solve = StateT SimState Identity surface rendered here)
  - book/src/concepts/eigsolve.md + book/src/L1/eigsolve.md (EigResult / EigState backing — the EigState resolution)
  - book/src/concepts/solve-result.md (SolveResult clustering judgment)
---

# CYCLE: Render the `coordination` library def bodies at Synthesis

## Summary

Wave 2 of the Synthesis-section build (batch-44 LEAD, user directive 2026-06-07 §"The SYNTHESIS section"). The shell for `book/src/synthesis/coordination.md` was authored this cycle by the layer-intro-author (`reports/2026-06-07T230500Z-layer-intro-author-synthesis-section-shell/CYCLE.md`). This dispatch fills its BODY: the implementation rendering of each outer-driver-cap / coordination operator in the L4 `Outer-driver caps & coordination combinators` doc-group, in topological order, in the L4 pseudo-language, with code-doc sections (I/O sets, named shape contracts, bunsen `# Arguments`/`# Returns`), closure-returning signatures paren-grouped per [`semantics/index.md`](../semantics/index.md) §1.3.1, the SLEPc EPS eigsolve loop rendered `#extern` after its type signature, deep-linked-unchanged lower artifacts inline, Haskell `where` for helpers, and a `reference`-class link from each def back to its authoritative L4 chapter. It is an **implementation VIEW** — it RENDERS the synthesized code form; it does NOT restate the semantics/laws (those live in the linked L4 chapters; `lowering-verifier` may audit the correspondence).

Operators rendered (topological order — construction/binding framework first, then the `Solve` monad surface + state carriers, then the caps, then the map/fold combinators that drive them):

1. The coordination-clustering type block (placed BEFORE the group): the `Solve` monad surface (`Solve a = StateT SimState Identity a` + `execState`), the `Outcome` / `EigOutcome` termination sums, `EigState` (the eigsolve persistent stratum — single-consumer, rendered inline here with its utility API + a back-link to the `EigResult` schema home), and the `StepReturn` accessor utility (the per-step return record, authoritatively named in `concepts/solve-result.md`) — each bundled with its **utility API** only; consumer methods stay in the group.
2. `preconditioning-framework` — `buildKspSolver` / `setOperators` (the construction-and-binding surface).
3. `ksp_solve` — the `Solve`-monadic preconditioned-Krylov cap (folds `krylov-step` from the `iteration` library).
4. `eigsolve` — the `Solve`-monadic eigenproblem cap; the SLEPc EPS loop renders `#extern eigen_iterate`; the constructive `eigsolve-impl` (Lanczos/Arnoldi/Krylov-Schur in `lanczos_step`/`krylov-step`) is the kernel-impl node, deep-linked not inlined here.
5. `solve_family` — the fixed-operator map-over-RHS-family combinator.
6. `frequency_sweep` — the operator-VARYING per-ω sweep combinator (rebuilds the operator inside the map via `assemble_frequency_operator`).
7. `fold_solve` — the state-threaded fold-over-schedule combinator; the opaque per-step `time_step_op` renders `#extern`.

**EigState resolution (the shell's flagged question):** `EigState` does **NOT** collapse to `SimState` — it is a genuinely distinct shape (`pairs` / `converged` / `requested` / `error` / `EigStatus`, vs `SimState`'s `x` / `it` / `converged` / `final_res` / `initial_res`; per `L4/eigsolve.md:70`). It is named in only ONE coordination signature (the `eigsolve` cap → single-consumer), so per the record-definition obligation it is rendered as an **in-chapter type block** here (clustered before its sole consumer `eigsolve`), bundled with its utility API, with a `reference`-class back-link to its authoritative field-schema home — the `EigResult` record defined in [`L1/eigsolve`](../L1/eigsolve.md) and navigationally homed in [`concepts/eigsolve`](../concepts/eigsolve.md). There is **no** `book/src/concepts/EigState.md` page, and one is NOT required (single-consumer → in-chapter section suffices), but I flag a lightweight OQ note (`record-EigState-schema-home-is-EigResult`) recording that the EigState↔EigResult correspondence is the authoritative schema link, in case a second consumer surfaces (then it would migrate to a `concepts/` page).

**Discipline:** every link is `reference`-class (implementation VIEW — no new `depends-on` blocking edges, no rank/liveness constraint on any firm node). The `#extern` callouts (SLEPc EPS loop in `eigsolve`, the opaque `time_step_op` in `fold_solve`) are NOT typed as `depends-on` edges to the opaque kernels (they are kernel-API boundaries; the kernel-impl correspondence is a `realizes-kernel-api` reference, owned by the impl node, not manufactured here). The `$`-sigil pseudocode is inside ` ```text ` fences (KaTeX rule). This dispatch registers NO dep-map row / cohort bullet (the Synthesis Part index is a navigational container the shell owns; this dispatch fills one chapter body, registered in SUMMARY by the shell).

## Proposed changes

The change is the FULL intended body of `book/src/synthesis/coordination.md` — it MERGES-WITH the shell's frontmatter + intro (kept verbatim from the sibling shell dispatch) and appends the rendered def bodies. The integrator applies the shell first, then this full-rewrite supersedes the `stub` body with the rendered library.

```edit:book/src/synthesis/coordination.md
[old]:
> **Status: `stub`.** This is the library intro shell. The per-operator synthesized def bodies are rendered into this chapter in Wave 2 (harvester). The shell establishes the operator list, the topological order, and the rendering conventions so the def-rendering dispatch can fill it.

The synthesized rendering of the L4 [Outer-driver caps & coordination combinators](../L4/outer-driver-combinators-intro.md) doc-group: the `Solve`-monadic outer-driver caps and the map/fold coordination combinators that drive the iteration kernels to convergence and over RHS / schedule / frequency families. Implementation VIEW — links to the authoritative L4 chapters for laws/semantics, renders the synthesized code form here.

## Operators this library holds (topological order)

A def appears after everything it uses. The expected order (refine by use) — the construction/binding framework first, then the caps, then the combinators that map/fold over them:

- [`preconditioning-framework`](../L4/preconditioning-framework.md) — the `buildKspSolver` / `setOperators` construction-and-binding framework (the non-iteration construction surface the caps run against).
- [`ksp_solve`](../L4/ksp_solve.md) — the `Solve`-monadic outer-driver cap for preconditioned Krylov solves (folds `krylov-step` from the [`iteration`](./iteration.md) library).
- [`eigsolve`](../L4/eigsolve.md) — the `Solve`-monadic eigenproblem cap; the SLEPc EPS eigsolve loop renders **`#extern`** at the kernel-API boundary, the constructive `eigsolve-impl` (Lanczos/Arnoldi/Krylov-Schur in `lanczos_step`/`krylov-step` vocabulary) renders inline where firm.
- [`solve_family`](../L4/solve_family.md) — the fixed-operator map-over-RHS-family combinator.
- [`fold_solve`](../L4/fold_solve.md) — the state-threaded fold-over-schedule combinator.
- [`frequency_sweep`](../L4/frequency_sweep.md) — the per-ω operator-VARYING sweep combinator (rebuilds the operator inside the map via `assemble_frequency_operator`).

## Clustering types (placed BEFORE the group in Wave 2)

Per the [type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group): the coordination-clustering state carriers — the per-solver state carriers `EigState` / `SimState`-family caps and [`SolveResult`](../concepts/solve-result.md) — are rendered immediately before the group, bundled with their utility API; consumer methods stay in the group. The cross-cutting `SimState` / `OpParams` / `IoData` live in [`types`](./types.md). The `Solve = StateT SimState Identity` monad (the `solve-monad` outer-driver vocabulary) is rendered here as the coordination surface.

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order; `#extern NAME` after the type signature for the SLEPc EPS loop in `eigsolve`; deep-linked-unchanged lower artifacts inline; Haskell `where` for private helpers; code-doc per def; `$`-sigil pseudocode inside ` ```text ` fences; link to `../L4/<op>.md`, do not re-cite L0.
[new]:
> **Status: `seed`.** The per-operator synthesized def bodies below are the Wave-2 (harvester) rendering of the L4 [Outer-driver caps & coordination combinators](../L4/outer-driver-combinators-intro.md) doc-group. This is the implementation VIEW — it RENDERS the synthesized code form; the authoritative semantics / algebraic laws live ONCE in the linked L4 chapters, and a rendered def's correspondence to its L4 chapter body is reviewable.

The synthesized rendering of the L4 [Outer-driver caps & coordination combinators](../L4/outer-driver-combinators-intro.md) doc-group: the `Solve`-monadic outer-driver caps and the map/fold coordination combinators that drive the iteration kernels to convergence and over RHS / schedule / frequency families. Implementation VIEW — links to the authoritative L4 chapters for laws/semantics, renders the synthesized code form here.

## Operators this library holds (topological order)

A def appears after everything it uses. The realized order — the coordination-clustering type block (the `Solve` monad surface, the termination sums, the state carriers) first; then the construction/binding framework; then the caps; then the combinators that map/fold over them:

1. **Coordination type block** (placed BEFORE the group, bundled with utility API): the `Solve` monad surface + `execState`, the `Outcome` / `EigOutcome` termination sums, `EigState` (the eigsolve persistent stratum), the `StepReturn` accessor utility (the per-step return record, authoritatively named in [`solve-result`](../concepts/solve-result.md)).
2. [`preconditioning-framework`](../L4/preconditioning-framework.md) — the `buildKspSolver` / `setOperators` construction-and-binding framework (the non-iteration construction surface the caps run against).
3. [`ksp_solve`](../L4/ksp_solve.md) — the `Solve`-monadic outer-driver cap for preconditioned Krylov solves (folds `krylov_step` from the [`iteration`](./iteration.md) library).
4. [`eigsolve`](../L4/eigsolve.md) — the `Solve`-monadic eigenproblem cap; the SLEPc EPS eigsolve loop renders **`#extern`** at the kernel-API boundary.
5. [`solve_family`](../L4/solve_family.md) — the fixed-operator map-over-RHS-family combinator.
6. [`frequency_sweep`](../L4/frequency_sweep.md) — the per-ω operator-VARYING sweep combinator.
7. [`fold_solve`](../L4/fold_solve.md) — the state-threaded fold-over-schedule combinator.

## Clustering types (placed BEFORE the group)

Per the [type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group): the coordination-clustering state carriers — `EigState` (the eigsolve persistent stratum) and the [`StepReturn`](../concepts/solve-result.md) return record — are rendered immediately before the group, bundled with their **utility API** (constructors / accessors / predicates) only; their **consumer methods stay in the group** (after the type block). The cross-cutting `SimState` / `OpParams` / `IoData` live in [`types`](./types.md). The `Solve = StateT SimState Identity` monad (the [`solve-monad`](../concepts/solve-monad.md) outer-driver vocabulary) and the `Outcome` / `EigOutcome` termination sums are rendered here as the coordination surface.

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order; `#extern NAME` after the type signature for the SLEPc EPS loop in `eigsolve` (and the opaque `time_step_op` in `fold_solve`); deep-linked-unchanged lower artifacts inline; Haskell `where` for private helpers; code-doc per def; `$`-sigil pseudocode inside ` ```text ` fences; closure-returning signatures paren-grouped per [`semantics/index.md`](../semantics/index.md) §1.3.1; link to `../L4/<op>.md`, do not re-cite L0.

---

## Coordination type block

The coordination surface threads the [`SimState`](./types.md) (cross-cutting; defined in `types`) through a state monad and classifies termination into sum types. These types are bundled here with their **utility API** only (constructors / projections / predicates); the substantive caps that *consume* them follow in the group below.

### The `Solve` monad surface

The outer-driver state monad. Authoritative threading discipline: [`solve-monad`](../concepts/solve-monad.md). Rendered here as the coordination library's effect surface.

```text
-- The outer-driver state monad: the effect domain is exactly SimState.
-- Authoritative threading discipline: concepts/solve-monad.md (define once).
type Solve a = StateT SimState Identity a

-- # Arguments / # Returns (utility API — the discharge that makes a cap a pure function)
-- execState :: Solve a -> SimState -> SimState   -- run the action, project the threaded state, drop the value
-- initial_state :: Inputs -> SimState            -- seed SimState from the per-solve Inputs (RHS / warm-start iterate)
```

### `Outcome` — the Krylov termination sum

The 3-arm termination sum the `ksp_solve` cap classifies once per cycle. Authoritative semantics: [`ksp_solve`](../L4/ksp_solve.md) §"Variant axes" + [`solve-monad`](../concepts/solve-monad.md) §"Termination as a sum type".

```text
-- classified ONCE at the cycle boundary; the Bool inside Done folds into SimState.converged.
data Outcome = Continue | Done Bool

-- # Arguments / # Returns (utility API — the predicate solve_loop reads)
done :: Outcome -> Bool
done (Done _) = True
done Continue = False
```

### `EigOutcome` / `EigStatus` — the eigsolve termination sum (richer extension)

The 4-arm extension of `Outcome`, with a first-class `PartialConverged k` arm (`0 < k < requested`) that has **no `ksp_solve` analog**. Authoritative semantics: [`eigsolve`](../L4/eigsolve.md) §"Variant axes".

```text
-- the richer termination status (Converged / partial / max-iter / inner-solve-failed)
data EigStatus  = Converged | PartialConverged Int | MaxIterReached | LinearSolveFailed
data EigOutcome = Continue | Done EigStatus

-- # Arguments / # Returns (utility API)
eig_done :: EigOutcome -> Bool
eig_done (Done _) = True
eig_done Continue = False
```

### `EigState` — the eigsolve persistent stratum

The `Solve`-threaded persistent state for the eigenproblem cap. It does **not** collapse to `SimState` — it carries the converged eigenpair family, not a single iterate. Single-consumer (only `eigsolve` names it), so it is rendered here in-chapter, bundled with its utility API. Authoritative field schema: the `EigResult` record defined in [`L1/eigsolve`](../L1/eigsolve.md) and navigationally homed in [`concepts/eigsolve`](../concepts/eigsolve.md) (the EigState↔EigResult correspondence is the authoritative schema link; this rendering does not restate the field semantics).

```text
-- the value threaded by `Solve a = StateT EigState Identity a` for the eigen cap.
-- the eigenvector x is named with shape group S (semantics/index.md §1.2.1), not a rank-1 axis;
-- the eigenvalue / error lists are genuine length-K rank-1 lists.
-- Authoritative field schema: L1/eigsolve.md (EigResult); concepts/eigsolve.md (navigational home).
type EigState = {
  pairs:     [(Complex, Tensor[(S: ...), complex])],   -- converged (λ, x), original-problem coords, un-scaled
  converged: Int,                                       -- number of converged pairs
  requested: Int,                                       -- requested mode count K_max
  error:     Tensor[K, real],                           -- genuine length-K per-pair error list
  status:    EigStatus                                  -- the terminal EigStatus
}

-- # Arguments / # Returns (utility API — construction + trivial projections)
-- initial_eig_state :: Inputs -> EigState              -- seed EigState (optional initial-subspace)
-- eigenpairs :: EigState -> [(Complex, Tensor[(S: ...), complex])]   -- accessor: the converged family
-- num_converged :: EigState -> Int                     -- accessor: the converged count
```

### `StepReturn` — the per-step return record (accessor utility)

The `krylov_step` kernel's return record, surfaced here for the cap's per-cycle classification reads. Authoritative field schema: [`solve-result`](../concepts/solve-result.md), where this record is named **`StepReturn`** (Form A) / `StepReturnB` (Form B). Rendered here under its authoritative name (link-don't-restate). (The record itself is produced by the `iteration` library's `krylov_step`; coordination consumes its `outputs`/`krylov` fields at the cycle boundary.)

```text
-- the record one krylov_step yields (Form A; Form B = StepReturnB adds a `carry` field).
-- Authoritative field schema + name: concepts/solve-result.md (StepReturn / StepReturnB).
type StepReturn = {
  sim:     SimState,     -- the next externally-visible state (monadic-effect product)
  krylov:  Krylov,       -- the next solve-local working bundle (plain returned value)
  outputs: StepOutputs   -- the demand-prunable per-step readout (residual proxy, breakdown token)
}

-- # Arguments / # Returns (utility API — the terminal-bundle reads the classifier needs)
-- residual_proxy :: StepReturn -> Scalar   -- the K.beta the Outcome classifier reads
```

---

## `preconditioning-framework`

The construction-and-binding surface one shell outside the caps: build the `(ksp, pc)` pair, bind the `(op, pc_op)` operators, and hand the bound bundle to the caps. The L4 record types (`BaseKspSolver`, `KspParams`, `PcParams`, `OpBinding`, …) are defined inline in the authoritative chapter; here we render the construction + binding def bodies.

> Rendered from [`preconditioning-framework`](../L4/preconditioning-framework.md) (firm). Implementation VIEW — the record definitions, capability-typing brands, and the derived-view-hoisting laws are owned by that chapter; this renders the synthesized construction surface.

```text
-- # Arguments
--   cfg    : LinearConfig          -- solver-pipeline knobs (absorbs ksp_method/pc_side/orthog/restart)
--   fes    : FESpaceHierarchy      -- the FE-space level stack the pc is built against
--   auxFes : Maybe AuxFESpaces     -- optional auxiliary spaces (aux-space smoothing)
-- # Returns
--   BaseKspSolver E                -- the constructed solver bundle, binding = Nothing (unbound)
buildKspSolver :: LinearConfig -> FESpaceHierarchy -> Maybe AuxFESpaces -> BaseKspSolver E
buildKspSolver cfg fes auxFes =
  let ksp = constructedOperatorFactory KrylovRole cfg            -- absorbs ksp_method, pc_side, orthog, restart
      pc  = constructedOperatorFactory PrecondRole cfg fes auxFes  -- absorbs pc_type, multigrid, aux, scalar_field
      _   = bindPreconditioner ksp pc                            -- one-shot bind on ksp internals
  in BaseKspSolver { ksp, pc, binding = Nothing, counters = Counters 0 0 }

-- # Arguments
--   op    : TrueOp E         -- the true operator (capability-branded)
--   pc_op : PcAssemblyOp E   -- the pc-assembly operator (capability-branded; may be a multigrid wrapper)
--   s     : BaseKspSolver E  -- the constructed (unbound) solver
-- # Returns
--   BaseKspSolver E          -- the solver with binding set; the bind precondition for `solve`
setOperators :: TrueOp E -> PcAssemblyOp E -> BaseKspSolver E -> BaseKspSolver E
setOperators op pc_op s =
  let binding' = OpBinding op pc_op             -- primitives stored verbatim
      pc_bound = pcBoundOp binding' s.pc        -- derived view: finest-level-unwrap when a multigrid pc_op meets a non-multigrid pc
      _        = s.ksp `setOpInternal` op
      _        = s.pc  `setOpInternal` pc_bound
  in s { binding = Just binding' }
  where
    -- the single definition site of the structural-adapter view; recomputed on demand, never cached.
    pcBoundOp binding pc =
      if isMultigridOp binding.pc_op && not (isMultigridSolver pc)
        then finestLevelUnwrap binding.pc_op
        else binding.pc_op
```

---

## `ksp_solve`

The `Solve`-monadic outer-driver cap for preconditioned Krylov solves: run the outer driver over the seeded `SimState`, classify termination once per cycle, and project the terminal state. The inner per-step body is the [`iteration`](./iteration.md) library's `krylov_step`, folded by `iterate_while`.

> Rendered from [`ksp_solve`](../L4/ksp_solve.md) (firm). The coordination identities (the `execState` discharge fusion, the `solve_loop`-as-`iterate_while_pure` fold equivalence, the `Outcome` classify-once law, the operator-inverse terminal law) are owned by that chapter.

```text
-- # Arguments
--   op  : OpParams   -- operator-internal config (readonly; closes over op.T, the preconditioner, tolerances)
--   inp : Inputs     -- the per-solve RHS b (+ optional warm-start iterate)
-- # Returns
--   SimState         -- the terminal state: .x ≈ A⁻¹·b, plus .it / .converged / .final_res / .initial_res
ksp_solve :: OpParams -> Inputs -> SimState
ksp_solve op inp = execState (solve_loop op inp) (initial_state inp)
  where
    -- outer driver: tail-recurse the per-cycle body until the Outcome says stop.
    solve_loop :: OpParams -> Inputs -> Solve ()
    solve_loop op inp = do
      o <- restart_cycle op inp          -- or: one_cycle op inp, for non-restarted solvers (CG / Chebyshev)
      unless (done o) (solve_loop op inp)

    -- per-cycle body: fresh Krylov, inner kernel-fold, fold the correction once, classify once.
    restart_cycle :: OpParams -> Inputs -> Solve Outcome
    restart_cycle op inp = do
      s <- get
      let k0        = fresh_krylov op inp s                       -- ephemeral bundle, born at cycle entry (plain value)
          (kn, _os) = iterate_while (krylov_step op k0) cont      -- inner fold of the `iteration` library kernel
      modify (\s -> s { x = s.x `plus` (kn.basis `applyBasis` kn.y) })  -- single per-cycle SimState.x write (after back_solve)
      pure (classify kn op s)            -- classify (kn.beta, kn.j, s.it, ε) into Done True / Done False / Continue
```

The inner `krylov_step` and `iterate_while` are rendered in the [`iteration`](./iteration.md) library (deep-linked, not re-rendered here — the cap *folds* them). The cap's net effect is the `SimState` transition discharged by `execState`.

---

## `eigsolve`

The `Solve`-monadic outer-driver cap for the generalized eigenproblem. Unlike `ksp_solve`, the eigen-iteration is **opaque-library-owned** (the SLEPc `EPSSolve` loop / ARPACK `naupd` RCI) — Palace authors no loop — so the cap names the iteration by role and the iteration renders **`#extern`** at the kernel-API boundary. The per-step body `apply_shift_invert` (which LIFTS) is the plain callback handed to the library.

> Rendered from [`eigsolve`](../L4/eigsolve.md) (firm). The `execState` discharge fusion, the `EigOutcome` classify-once law, and the `apply_shift_invert` body-composition identity are owned by that chapter. The opaque-library obstruction is the [`L3/eigsolve`](../L3/eigsolve.md) `sequential-obstruction`.

```text
-- # Arguments
--   op  : OpParams   -- readonly; closes over op.K / op.M (+ op.C / op.A2), the inner solver op.inv, σ, K_max
--   inp : Inputs     -- the per-solve inputs (optional initial-subspace seed)
-- # Returns
--   EigState         -- terminal: .pairs (converged (λ, x), original-problem coords), .converged / .status
eigsolve :: OpParams -> Inputs -> EigState
-- NOTE: the seed is `initial_eig_state` (the EigState constructor in the type block above),
-- DELIBERATELY eigen-specific. The authoritative L4 chapter (book/src/L4/eigsolve.md:44) writes
-- `initial_state inp`; here the cap threads `Solve a = StateT EigState Identity a`, so an
-- EigState-seeding constructor is the correct discharge (the L4 chapter's reuse of `initial_state`
-- for the EigState-threaded cap is a latent inconsistency to reconcile upstream — lowering-verifier).
eigsolve op inp = execState (solve_loop op inp) (initial_eig_state inp)
  where
    -- outer driver: a SINGLE opaque library step + one classification (NOT a Palace tail-recursion).
    solve_loop :: OpParams -> Inputs -> Solve ()
    solve_loop op inp = do
      o <- eigen_iterate op inp          -- OPAQUE library fold (see #extern below)
      classify_into_state o              -- fold the EigOutcome into EigState.status once at the boundary

-- The opaque eigen-iteration: the entire SLEPc EPSSolve / ARPACK naupd RCI loop. Palace authors NO
-- loop — the kernel-API boundary. The constructive realization (the kernel-impl node `eigsolve-impl`
-- = Lanczos / Arnoldi / Krylov-Schur in the `lanczos_step` / `krylov_step` vocabulary) is the from-our-
-- primitives version; it `realizes-kernel-api` this surface (a reviewable correspondence, not a build dep).
eigen_iterate :: OpParams -> Inputs -> Solve EigOutcome
#extern eigen_iterate

-- the per-step body the library folds internally (handed in as the ApplyOp / __pc_apply_EPS callback);
-- whole-tensor, LIFTS — identity-in-form to the firm L2/L3 apply_shift_invert composition.
apply_shift_invert :: OpParams -> Tensor[(S: ...)] -> Tensor[$S]
apply_shift_invert op v =
  let w = apply_linop op.operand v       -- apply against M (linear) / K (none) / PEP block (quadratic)
      y = ksp_solve_op op.inv w          -- inner ksp_solve inverting the shifted operator (K − σM)
  in scale_untransform op y              -- per-backend γ/δ un-scale; optional projector tail
```

The `eigen_iterate` `#extern` is the kernel-API surface (the SLEPc EPS loop is opaque-library-owned, `obstruction (opaque-library-ownership)`); the constructive `eigsolve-impl` realizes it from our `lanczos_step` / `krylov_step` primitives (deep-linked, the kernel-impl node). The callback `apply_shift_invert` lifts at both layers and is rendered inline because it is the from-our-primitives body the library folds.

---

## `solve_family`

The fixed-operator map-over-RHS-family combinator: capture the operator once, map the `ksp_solve` cap over an independent RHS family, collect the order-preserving solution family. The map is a list homomorphism (independent elements → embarrassingly parallel).

> Rendered from [`solve_family`](../L4/solve_family.md) (firm). The concatenation-homomorphism, operator-capture-once / `SetOperators`-hoist, and element-independence laws are owned by that chapter.

```text
-- # Arguments
--   op   : OpParams    -- captured ONCE outside the map; readonly; shared across the family
--   rhss : [Inputs]    -- the independent RHS family the map ranges over
-- # Returns
--   [SimState]         -- the collected solution family; solutions[i] aligns with rhss[i]
solve_family :: OpParams -> [Inputs] -> [SimState]
solve_family op rhss = map (\inp -> ksp_solve op inp) rhss
  -- op-dependent solver construction (fresh_ksp op) is invariant across the map and hoists out of it;
  -- each element's ksp_solve is independent (no cross-element threading) → the map distributes over ++.
```

---

## `frequency_sweep`

The operator-VARYING per-ω sweep combinator: capture the operator *basis* once, but REBUILD the per-member operator `A(ω)` inside the map via `assemble_frequency_operator` (from the [`data-algebra`](./data-algebra.md) library), then run one `ksp_solve` per member. The `SetOperators`-hoist does NOT apply (the operator varies); independence still holds (the rebuild is index-local).

> Rendered from [`frequency_sweep`](../L4/frequency_sweep.md) (firm). The concatenation-homomorphism (holds despite the operator varying), the NO-`SetOperators`-hoist non-law, and member-independence are owned by that chapter. Single-witness-driven by design (the driven uniform sweep).

```text
-- # Arguments
--   fam    : FrequencyOperatorFamily[N]   -- the fixed operator basis {K, C, M, A2}, captured ONCE
--   omegas : [Scalar]                     -- the swept frequency family (complex weights); the map domain
-- # Returns
--   [SimState]                            -- the collected per-ω solution family; solutions[i] ↔ omegas[i]
frequency_sweep :: FrequencyOperatorFamily[N] -> [Scalar] -> [SimState]
frequency_sweep fam omegas =
  map (\omega -> ksp_solve (assemble_frequency_operator fam omega)   -- REBUILD A(ω) per member
                           (rhs_at fam omega))                       -- ω-dependent excitation
      omegas
  where
    -- the per-member RHS (driven excitation at ω; absorbed, ω-dependent):
    rhs_at :: FrequencyOperatorFamily[N] -> Scalar -> Inputs
    rhs_at fam omega = excitation_vector fam omega
```

The per-member operator rebuild `assemble_frequency_operator fam omega` is the named affine-in-ω verb (the [`data-algebra`](./data-algebra.md) library's `assemble_frequency_operator`), NOT an opaque per-member operator — the load-bearing distinction from `fold_solve`'s opaque `time_step_op`.

---

## `fold_solve`

The state-threaded fold-over-schedule combinator: capture the operator once, seed the carry once, thread the persistent field-state through a schedule by `foldl`, advancing one opaque per-step operator at a time where **each step's input is the prior step's output**. The carry-threading is a `sequential-obstruction` (the steps do not commute); the per-step body is an opaque library step rendered **`#extern`**.

> Rendered from [`fold_solve`](../L4/fold_solve.md) (firm). The fold-threading / schedule-split law, the operator-capture-once hoist, the seed left-identity, and the load-bearing NON-commutativity non-law are owned by that chapter. The `schedule-source` variant axis (fixed-list / state-generated) is recorded there; the default surface rendered here is the fixed-list fold (the transient witness).

```text
-- # Arguments
--   op       : OpParams    -- captured ONCE at construction; readonly; threaded unchanged into every step
--   s0       : TimeState   -- the seed field-state (the initial carry)
--   schedule : [Time]      -- the fixed schedule the fold ranges over (default surface; uniform timesteps)
-- # Returns
--   TimeState              -- the final field-state after the whole schedule is threaded
fold_solve :: OpParams -> TimeState -> [Time] -> TimeState
fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule
  -- foldl (a ++ b) = foldl b . foldl a → checkpoint-and-resume; the carry-threading is sequential
  -- (each step reads the prior step's output) → no commutativity / no distribution over ++.

-- The opaque per-step operator: advances the field-state one step; bottoms out in a library integrator
-- (MFEM ODESolver::Step for transient; the RomOperator greedy sampler for the state-generated form).
-- The kernel-API boundary — Palace folds an opaque library step, NOT a Palace-authored body.
time_step_op :: OpParams -> TimeState -> Time -> TimeState
#extern time_step_op
```

The `time_step_op` `#extern` is the opaque-library per-step boundary (`obstruction (opaque-library-ownership)` at the lowering layer); the fold quantifies over it rather than rendering its body. The state-generated `schedule-source` form (driven-PROM SweepAdaptive / AMR) renders through the §3.7 carry form — see the L4 chapter.
```

## Operator content

The rendered library body above carries seven operator def renderings + a coordination type block, all inside the single `coordination.md` chapter. Each:

- **Code-doc section** — `# Arguments` / `# Returns` (bunsen style), explicit I/O sets, named shape contracts (`Tensor[(S: ...)]` binding / `Tensor[$S]` use for shape-generic; `Tensor[K, real]` / `Tensor[K]` for genuine length-K lists; `Tensor[N]` reserved for flat rank-1 dof-vectors per the named-shape-group convention).
- **Concrete def body** in the L4 pseudo-language (fenced ` ```text `; `$`-sigil content inside the fence per the KaTeX rule).
- **Closure/signature fidelity** — the caps are `OpParams -> Inputs -> SimState`/`EigState` (the discharge makes the cap a pure function, not a closure-returner, so no outer parens needed); the `Solve` monad surface uses the operator-value spelling; no opaque type-application forms.
- **`#extern NAME` after the type signature** for the two opaque-kernel boundaries (`eigen_iterate` = SLEPc EPS loop; `time_step_op` = MFEM ODESolver step).
- **`reference`-class back-link** to the authoritative L4 chapter; renders the code form, does NOT restate semantics/laws.
- **Status `seed`** for the chapter (flipped from the shell's `stub` now the bodies are rendered — a navigational-container implementation VIEW; no `rank:`, reference-edges only).

## Supporting evidence

- **Directive source:** CLAUDE.md §"The SYNTHESIS section" — implementation-VIEW (link-don't-restate); topological def order; `#extern NAME` after type sig for opaque kernels; deep-linked-unchanged lower artifacts inline; Haskell `where`; code-doc per def. Memory `project_synthesis_section_directive`.
- **Shell:** `reports/2026-06-07T230500Z-layer-intro-author-synthesis-section-shell/CYCLE.md` — defines `coordination.md`'s frontmatter (`kind: navigational-container`, `reference`-edges only, no `rank:`), the intro shell (MERGED-WITH above), the operator list + topological order, the clustering-types placement, and the `#extern` boundary (SLEPc EPS loop). The shell flagged the EigState home question — resolved below.
- **L4 chapters rendered (all firm):**
  - `ksp_solve` (`book/src/L4/ksp_solve.md`, firm c048) — the cap entry `ksp_solve op inp = execState (solve_loop op inp) (initial_state inp)` (`:56-57`), the `solve_loop`/`restart_cycle`/`Outcome` shape (`:60-73`), the four-phase restart cycle (`:98-101`).
  - `eigsolve` (`book/src/L4/eigsolve.md`, firm c048) — the cap entry + opaque `eigen_iterate` (`:43-63`), the `apply_shift_invert` body (`:59`, `:111`), the `EigState` stratum (`:70`), the `EigStatus`/`EigOutcome` sum (`:62-63`), the SLEPc `EPSSolve` opaque loop (`:90`, `:204`).
  - `preconditioning-framework` (`book/src/L4/preconditioning-framework.md`, firm c096) — `buildKspSolver` (`:171-176`), `setOperators` + `pcBoundOp` derived view (`:183-188`, `:251-258`).
  - `solve_family` (`book/src/L4/solve_family.md`, firm c086) — the map form (`:52-53`), the operator-capture-once hoist.
  - `frequency_sweep` (`book/src/L4/frequency_sweep.md`, firm c070) — the operator-varying map (`:105-109`), the `assemble_frequency_operator` per-member rebuild, the NO-hoist law.
  - `fold_solve` (`book/src/L4/fold_solve.md`, firm c058) — the fold form (`:49-50`), the opaque `time_step_op` (`:54`, `:94`), the schedule-split law.
- **`Solve` monad surface:** `book/src/concepts/solve-monad.md` (the `Solve a = StateT SimState Identity a` + `execState` shape, `:16-19`; the `Outcome` termination-sum, `:68-74`) — the authoritative threading discipline this rendering links to (define once).
- **EigState resolution evidence:** `book/src/L4/eigsolve.md:70` (EigState's distinct shape — `pairs`/`converged`/`requested`/`error`/`EigStatus`, NOT `SimState`'s five fields → does NOT collapse to SimState); `book/src/L1/eigsolve.md` + `book/src/concepts/eigsolve.md:44-48` (the `EigResult` record — EigState's authoritative field-schema home). EigState is named in only the `eigsolve` cap (single-consumer) → in-chapter type block suffices (record-definition obligation).
- **`StepReturn` clustering:** `book/src/concepts/solve-result.md` (the `StepReturn = Solve { sim, krylov, outputs }` record — firm; Form B `StepReturnB` adds `carry`) is produced by `krylov_step` (iteration library) and consumed by the caps' classification reads → rendered here as an accessor-utility surface under its authoritative name `StepReturn`, schema linked.
- **`reference`-class / no-depends-on discipline:** the navigational-container frontmatter (no `rank:`, `reference`-edges only) the shell authored; the `#extern` callouts are kernel-API boundaries, NOT `depends-on` edges to the opaque kernels (the `realizes-kernel-api` correspondence is owned by the impl node, per CLAUDE.md §"Kernel-API vs kernel-IMPLEMENTATION distinction").

## Open questions / caveats

- **EigState schema home is the `EigResult` record (RESOLVED — no new page required).** `EigState` does NOT collapse to `SimState` (genuinely distinct shape per `L4/eigsolve.md:70`). It is single-consumer (only the `eigsolve` cap), so per the record-definition obligation an in-chapter type block suffices — rendered above, clustered before `eigsolve`, with a `reference`-class back-link to its authoritative field-schema home (the `EigResult` record in `L1/eigsolve.md` / navigationally `concepts/eigsolve.md`). I did **not** file `record-EigState-needs-definition-home` because the home exists (EigResult) and the single-consumer in-chapter rendering satisfies the obligation. **Lightweight note for the integrator/meta:** `record-EigState-schema-home-is-EigResult` — if a SECOND coordination/drivers consumer of `EigState` surfaces (e.g. the eigenmode `drivers`-library column names it directly), it crosses the ≥2-consumer bar and should migrate to a dedicated `concepts/EigState.md` page (cross-referencing EigResult) rather than duplicating the in-chapter block. Not blocking.
- **`eigsolve-impl` (the kernel-impl node for the SLEPc EPS loop) is deep-linked, not inlined.** The directive says deep-linked-UNCHANGED lower artifacts render inline; the constructive `eigsolve-impl` (Lanczos/Arnoldi/Krylov-Schur in `lanczos_step`/`krylov_step`) is a SEPARATE kernel-impl node, not an unchanged lowering of the opaque `eigen_iterate` (it is the from-our-primitives REALIZATION of the kernel-API, linked by `realizes-kernel-api`). I rendered `eigen_iterate` as `#extern` (the kernel-API boundary) and noted the impl correspondence in prose, deep-linked. If a later batch-44 cycle lands a firm `eigsolve-impl` chapter, the `iteration` or a dedicated kernel-impl library may render its body inline; coordination keeps the `#extern` surface. Flag for the planner: the `eigsolve-impl` kernel-impl node is not yet a standing chapter (the L4 `eigsolve` is the cap, not the impl) — its authoring is the DIRECTIVE-3 spine-dependency kernel-impl work (geometric-multigrid / eigsolve consumer arc), not this dispatch.
- **The inner `iteration`-library names (`krylov_step`, `iterate_while`, `fresh_krylov`, `applyBasis`, `Krylov`, `StepOutputs`) are forward-references to the SIBLING `iteration` library** (Wave-2 abstractor dispatch this cycle). I wrote them as plain inline-code tokens in the rendered bodies (not live links to `synthesis/iteration.md` anchors) where they are def-body identifiers; the prose pointers use the live `[`iteration`](./iteration.md)` chapter link (the file exists per the shell). If the abstractor's canonical slug for `krylov-step`'s rendered def differs from `krylov_step`, the integrator should reconcile — I used the underscore form matching the L4 calculus identifier convention; the `iteration` library chapter link resolves regardless.
- **`fold_solve` state-generated `schedule-source` form not rendered.** Per the L4 chapter, the default signature surface is the fixed-list fold (transient); the state-generated greedy form (SweepAdaptive / AMR) renders through the §3.7 carry. I rendered only the fixed-list default surface (the firm signature) + a prose pointer to the L4 chapter for the state-generated form, matching the chapter's own treatment. Not a gap.
- **Chapter status flipped `stub` → `seed`.** The shell seeded `coordination.md` as `stub` (intro-only). With the bodies rendered it is a `seed` navigational-container implementation VIEW (consistent with the directive's chapter-KIND — it makes no resolution claim, carries `reference`-edges only). If the layer-intro-author / meta prefers a different status token for rendered Synthesis library chapters (the directive does not pin one), flag for reconciliation; I chose `seed` to mark "rendered, refinable by use" without claiming a ladder rank.
