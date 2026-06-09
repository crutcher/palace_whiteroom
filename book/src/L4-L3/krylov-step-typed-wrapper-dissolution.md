# krylov-step-typed-wrapper-dissolution

The L4>L3 lowering theme for `krylov_step`. Dissolves the L4 typed-wrapper machinery — three-stratum state-stratification records, the `Solve` state monad, the `OpParams` `readonly` typing, and the Form-A/Form-B presentation distinction — into the L3 value-threading form expected by the global-tensor-field calculus. The kernel body's primitive sequence is unchanged by the rotation; only the wrapper dissolves.

## Slug

`krylov-step-typed-wrapper-dissolution`

## Context

L4 `krylov_step` (per [`L4/krylov_step`](../L4/krylov_step.md)) is the typed wrapper around the L2 primitive composition. The wrapper carries four pieces of L4-only machinery:

1. **Three-stratum state-stratification records** (per [`state-stratification`](../concepts/state-stratification.md)): `SimState` (externally-visible, persists across the solve), `OpParams` (operator-internal, captured once), `Krylov` (solve-local ephemeral bundle). At L4 these are *typed records* with `readonly` annotations and lifetime enforcement.
2. **The `Solve a = StateT SimState Identity a` monad** (per [`solve-monad`](../concepts/solve-monad.md)). The kernel body lives inside a monadic action; the sole monadic effect is the `SimState.it` increment via `modify`.
3. **`OpParams` `readonly` typing**. The kernel cannot re-inspect variant selectors — this is a typing invariant at L4, sharpening the L2-level variant-absorption discipline.
4. **The Form-A vs Form-B presentation distinction** (per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)). Form A keeps the first-iteration branch inside the body; Form B splits into `(first_step, steady_step)` with `PrevCarry` threaded as a closure parameter of the outer combinator.

L3's job is the *iteration rotation*: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly (per [`sequential-obstruction`](../concepts/sequential-obstruction.md)). L3 carries neither monadic structure (that is L4's coordination layer, deliberately above L3) nor typed state-stratification records (the three strata exist at L3 only as positional values whose ordering is a convention, not a typing). The lowering is therefore the *dissolution* of the L4 wrapper, recovering the value-threading form that L3 expects.

The L3 form this lowering produces is **identity-in-form** on the kernel body's primitive sequence — the same five primitive groups (apply, optional auxiliary, iterate-update, scalar-update, output-readout) in the same dataflow-forced order — but **substantively rotated** at the type/wrapper level. The further L3>L2 lowering on the kernel body is identity-in-form per the firm theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) (`arnoldi_step.md:178-213` is the live anchor), but this does **not** collapse the L3 row away: the L4 entry lowers via this theme to the firm L3 entry [`L3/krylov_step`](../L3/krylov_step.md) (the value-threaded RHS rendered as a layer-coherent operator), and the body's L3>L2 identity hop is completed by the separate theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md). The lowering chain is therefore L4>L3>L2>L1 with no skipped rows — each layer is coherent within itself, so an L3 reader finds `krylov_step` defined in L3 vocabulary at L3 even when the body rewrite is trivial. See §"Body identity-in-form across the L4>L3>L2 chain" below.

## L4 form (LHS)

The two L4 surface forms from the harvester output, reproduced for the LHS of the rewrite:

**Form A — branch-in-body** (default):

```text
krylov_step :: OpParams -> Krylov -> (SimState -> Solve { sim: SimState', krylov: Krylov', outputs: StepOutputs })
```

With the body shape (per `L4/krylov_step` §Semantics):

```text
krylov_step op K = \s -> do
  let w       = apply_linop op.T K.<input_field>
  let K_aux   = optionally apply op.orthog (K.V_prefix, w)        -- or op.scalars (K.k, K.scalar_state); or K (no-op)
  let K'      = krylov_update K_aux op w
  let outputs = derived_views K' op
  modify (\s -> s { it = s.it + 1 })
  pure { krylov: K', outputs }
```

The body is consumed by an outer `iterate_while`-style combinator (see [Speculative L4 operators](#speculative-l4-operators)) inside `solve-monad`'s `restart_cycle` / `inner_loop`.

**Form B — first-iteration-unrolled** (opt-in per `first-iteration-unrolling`):

```text
first_step  :: OpParams -> Krylov -> (SimState -> Solve { sim: SimState', krylov: Krylov', carry: PrevCarry, outputs: StepOutputs })
steady_step :: OpParams -> Krylov -> (PrevCarry -> SimState -> Solve { sim: SimState', krylov: Krylov', carry: PrevCarry', outputs: StepOutputs })
```

The body of `steady_step` is branch-free; `PrevCarry` (e.g., CG's `β_prev`) is a *closure parameter of the loop driver*, not a *state field of the iteration* (per `first-iteration-unrolling.md:21-37`).

## L3 form (RHS)

The L3 form dissolves all four pieces of L4 wrapper machinery. The kernel body's primitive sequence is unchanged; what changes is the surface around the body.

**L3 form** (value-threaded; both forms collapse to the same L3 shape modulo carry-threading):

```text
krylov-step-L3 :: (op, K, s) -> (K', s', outputs)
krylov-step-L3 op K s =
  let w       = apply_linop op.T K.<input_field>              -- L3-native global op
  let K_aux   = optionally apply op.orthog (K.V_prefix, w)     -- L3-native; orthog at CGS/CGS2 is L3-lifted, MGS carries sequential-obstruction (inherited from arnoldi_step.md:194-213, not introduced by this lowering)
                or       apply op.scalars (K.k, K.scalar_state)
                or       K
  let K'      = krylov_update K_aux op w                       -- composition of L3-native axpy / axpby / axpbypcz / dot / nrm2 / scal
  let outputs = derived_views K' op                            -- demand-pruned per derived-view-hoisting
  let s'      = s { it = s.it + 1 }                            -- explicit record update (the dissolved `modify`)
  in (K', s', outputs)
```

**Form B in L3** (PrevCarry as a positional value in the threaded tuple, not as a closure parameter — the L4 closure structure dissolves because L3 has no `iterate_while_with_prev` combinator distinct from `iterate_while`):

```text
krylov-step-L3-first  :: (op, K, s)      -> (K', s', carry, outputs)
krylov-step-L3-steady :: (op, K, s, carry) -> (K', s', carry', outputs)
```

Three structural differences from the L4 form, all at the wrapper level:

1. **`StateT SimState` dissolves to explicit `s` argument and `s'` return position.** The `Solve a = StateT SimState Identity a` monad is L4-only — L3 has no `do`-notation, no `modify`, no monadic bind. The `SimState` is threaded as an ordinary value in the positional signature `(op, K, s) -> (K', s', outputs)`. The sole monadic effect (the `it` counter increment via `modify`) becomes an explicit record-field update `s' = s { it = s.it + 1 }` in the let-chain. Per [`counter-update`](../concepts/counter-update.md), the counter update is L3-native: it is a rank-0 scalar increment on a `SimState`-record field, no sequential obstruction.

2. **The three state-stratification records become positional tuples whose ordering is conventional.** `OpParams`, `Krylov`, `SimState` at L4 are *typed records* — their `readonly` annotations, lifetime constraints, and field-typing are enforced by the L4 calculus's type system. At L3 the same three pieces exist but as *unwrapped values* threaded through the per-step composition: `op` is closure-captured (immutable by virtue of not being in the return position), `K` is threaded explicitly (input and output position), `s` is threaded explicitly (input and output position). The L4 record-field projections (e.g., `K.<input_field>`, `K.V_prefix`, `s.it`) become L3 positional accessors that are textually identical but typing-wise erased. **What's lost in the rotation**: the L4 typing's mechanical-checkability of variant absorption. **What's preserved**: the dataflow shape and the discipline (now a documented invariant — see (3) below).

3. **`OpParams` `readonly` typing collapses to a documented invariant.** At L4 the `OpParams` `readonly` annotation forbids the kernel from re-inspecting variant selectors (`pc_side`, `gs_orthog`, polynomial-kind, etc.); the variant axes are absorbed into the constructed-operator surfaces `op.T`, `op.orthog?`, `op.scalars?`. At L3 the same absorption holds — the kernel calls `op.T`, `op.orthog`, `op.scalars` and never branches on their internal selectors — but this is a *documented invariant* (a comment, or a coding discipline) rather than a typing constraint. L3 has no `readonly` annotation in its calculus; the discipline is preserved by convention and verified by reading the body. **Per the harvester's caveat on this point** (`L4/krylov_step` §Signature, point 1), this is the load-bearing typing distinction between L4 and L3, and the rotation makes it explicit by *demoting* the constraint.

4. **Form-A vs Form-B distinction collapses into carry-threading.** At L4 Form B is a presentation rotation: `(first_step, steady_step)` is a typed pair of functions where `steady_step` takes `PrevCarry` as a closure parameter of the loop driver (`iterate_while_with_prev` rather than `iterate_while`). At L3 the same content is recovered by adding a position to the threaded tuple: the loop combinator becomes a generic tail-recursive value-threading loop, and `PrevCarry` is just another value in the tuple. The L4 distinction between "closure parameter of the combinator" and "state field of the iteration" loses operational meaning at L3 (both are positional values; there is no combinator-vs-state typing). **Consequence**: at L3 there is only one form of `krylov_step` (the value-threaded form), with the Form-B variants distinguished only by whether the threaded tuple has a `carry` position. The Form-A/Form-B presentation choice becomes an artefact of L4 alone.

### What does NOT change in the rotation

The five primitive-group dataflow chain — `apply_linop`, optional auxiliary (`op.orthog` / `op.scalars` / no-op), iterate-update (`axpy` / `axpby` / `axpbypcz`), scalar-update (`dot` / `nrm2` plus scalar arithmetic), output-readout (`derived_views`) — is **textually identical** between the L4 body and the L3 body. The dataflow constraints are unchanged (the L1 primitives are pure on their inputs; no aliasing introduced or removed). The variant-axis profile is unchanged at six (axes are absorbed in `op.*` surfaces at L3 just as they are at L4, modulo the `readonly` typing demotion).

### What this lowering does NOT cover

- **L3>L2 lowering on the body** (the iteration rotation in the negative direction). The L3 body is in primitive-composition form already; the further L3>L2 lowering on the body is identity-in-form. That lowering belongs in `book/src/L3-L2/` and is the separate theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md).
- **Outer-loop sequential obstruction**. The fact that the *outer* `iterate_while` loop carries a `sequential-obstruction` at L3 (homed in the firm L3 entry [`L3/krylov_step`](../L3/krylov_step.md) §Algebraic-laws non-lift catalogue; `arnoldi_step.md:194-213` is the live anchor) is a property of the loop, not of the step kernel. The step-body L4>L3 lowering described here is independent of the outer-loop obstruction. The loop obstruction is documented in the firm L3 entry's non-lift catalogue and the [`sequential-obstruction`](../concepts/sequential-obstruction.md) concept page; this theme does not re-state it.
- **MGS-orthogonalisation sequential obstruction**. Per `arnoldi_step.md:194-213`, the `gs_orthog = MGS` variant of `op.orthog` carries a sequential obstruction at L3 (the per-i sequencing of `H[i,j] ← ⟨w, V[i]⟩` and `w ← w − H[i,j] · V[i]`). This is a property of the `orthog` primitive under the MGS variant, not of `krylov_step` itself. The `krylov_step` body sees `op.orthog` as an opaque call site; whether that call lifts depends on the variant axis, which is absorbed below the `krylov_step` surface. This theme does not duplicate the `orthog`-variant obstruction; it cites it.

## Applicability conditions

The rewrite is valid when all four of the following hold (which they do for the firm L4 `krylov_step` entry by construction):

1. **The L4 `Solve` monad's effect domain is exactly `SimState`.** The only `modify` calls in the kernel body touch `SimState` (specifically the `it` counter); no `Krylov` field is touched via a monadic effect; no `OpParams` field is touched via a monadic effect (it is `readonly` by typing). If a future variant of `krylov_step` introduces a second `SimState`-touching `modify` (e.g., breakdown signalling via `SimState.converged`), the rewrite still applies — the L3 form just acquires a second positional update line in the let-chain. If a future variant introduces a *non-`SimState`*-effecting monadic call (e.g., logging via `tell`), the rewrite breaks at the `Solve = StateT SimState Identity` typing, and a richer L3 effect representation would be needed.

2. **`OpParams` is closure-captured at the per-step call site, not threaded.** The L4 signature has `op` as the first positional argument of `krylov_step :: OpParams -> Krylov -> ...`, and the call site uses partial application (`krylov_step op` as a curried form). At L3 this becomes `op` as a closure-captured argument of the body. The rewrite assumes `op` is not re-bound between steps; if a future variant has per-step-varying `op` (which would defeat variant absorption), the rewrite needs revision.

3. **The five primitive groups are L3-native or carry their own L3-edge classification.** Each of `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal` is an L1 primitive whose L2>L3 lift is identity (firm in [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md); `arnoldi_step.md:185-188` is the live anchor). The optional auxiliary stage (`op.orthog` under MGS) carries its own L3 obstruction (per `arnoldi_step.md:194-213`), which is independent of the `krylov_step` body rewrite. This lowering does not introduce new L3 obstructions; it inherits the existing classification of its constituent primitives.

4. **The `Krylov` ephemeral bundle has plain-value lifecycle (born at restart, discarded at restart-or-return) and is not aliased by any other state.** The L4 typing makes this structural (`Krylov` is not a field of `SimState`; lifetime is restart-scoped); at L3 it becomes a discipline. The rewrite assumes no caller threads `Krylov` across restart boundaries (which would mis-type its lifetime). Per `solve-monad.md:53`, this discipline is honoured by `restart_cycle` building a fresh `Krylov` per cycle.

5. **The downstream consumer of the surrounding `iterate_while` invocation observes only `final_state`-equivalent quantities (no per-iteration trajectory readout).** This is the precondition for the §3.8 demand-pruning collapse from the unpruned L3 form (`[readout]` accumulator) to the pruned L3 form (single readout / accumulator dropped) shown in §"What the L3 form for `iterate_while` looks like" above. Per Law 1 of [`iterate_while`](../L4/iterate_while.md) and the worked example in `book/src/concepts/derived-view-hoisting.md`, when the consumer's destructuring reads only `final_state` (or the L3-positional equivalent — the final-iteration carry value), the per-step `extras` computation in the step body is eliminated by the §3.8 rewrite, the L4 `[readout]` trajectory collapses to `[]`, and the L3 form is the pruned shape. **Palace satisfies this condition by construction**: the `IterativeSolver` result-extraction surface materializes exactly four scalars (`converged`, `initial_res`, `final_res`, `final_it` at `reference/palace/palace/linalg/iterative.hpp:52-55`), each of which is either a carry field at the final iteration or a pre-loop initialization; the sole caller `BaseKspSolver::Mult` at `reference/palace/palace/linalg/ksp.cpp:296-310` consumes only those four scalars (branch on `GetConverged`, ratio in warning via `GetFinalRes()/GetInitialRes()`, sum into counter via `GetNumIterations`). No per-iteration consumption exists in `palace/`. **When violated** — e.g., a hypothetical future Palace surface `GetResidualHistory(): std::vector<double>` reading the per-step `residual_norm` extras — Condition 5 fails, §3.8 does not fire for that consumer, and the L3 form must be re-rendered with the accumulator restored (the unpruned form). The L4 form is invariant under this consumer change; only the L4>L3 lowering's rendered L3 shape selects between the two forms.

If a future Krylov-shaped slice violates any of these (e.g., a method whose `OpParams` needs per-step mutation, or whose step body needs effects beyond `SimState`, or whose consumer reads the trajectory), the L4>L3 lowering would need to be refined; the speculative-operator slot would be enlarged.

## Justification kind

**`structural`** with a secondary **`reduction-chain`** component.

**Abstraction-direction note**: L4 is the higher-abstraction layer (typed records, monadic effect, readonly typing constraint, Form-A/B presentation distinction) and L3 is the lower-abstraction layer (positional values threaded explicitly, documented invariants in place of typing). The rotation direction is L4 → L3: the higher-level wrapper machinery *dissolves* into the value-threaded form below it. This is the correct lowering direction under the methodology's rotation-quality criterion — L_{n+1} (L4) is more compact / more abstract / more equational, and the L_n (L3) form is the dissolved trace. A reader who sees the L4 form as "more elaborate" should read the elaboration as *abstraction* (typing buys mechanical-checkability of variant absorption), not as accidental complexity.

- The dominant content is structural: the L4 wrapper (record types, monad, readonly typing, Form-A/B distinction) dissolves into an L3 value-threading form, and the kernel body's primitive sequence is preserved by construction (not by an algebraic argument, but by the syntactic shape of the rewrite — every L4 primitive call becomes an L3 primitive call at the same position in the dataflow chain).
- The secondary reduction-chain component is the `modify (\s -> s { it = s.it + 1 })` to `s' = s { it = s.it + 1 }` step. This is a one-step reduction of the `StateT` monad's `modify` operator — `modify f` in `StateT s m a` unfolds to `\s -> ((), f s)`, and the surrounding `do`-block desugars to explicit value-threading. The reduction is mechanical (the `StateT` monad's evaluation rules are standard); the L3 form is the desugared trace.

The body identity-in-form assertion (firm in [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md)) is justified as **`empirical-match`** at the L2>L3 edge — the L2 primitive-composition form is L3-native by inspection, and the assertion is the recognition that no rewrite is needed. The L4>L3 hop covered here is a different rotation (typed wrapper to value-threaded form); it is **not** identity-in-form on the wrapper, only on the body. The two rotations compose to give an L4>L2 chain that is non-identity at the wrapper level and identity-in-form on the body.

## Speculative L4 operators

The lowering's L4 form refers to an outer combinator [`iterate_while`](../L4/iterate_while.md) (and its [`_with_prev`](../L4/iterate_while_with_prev.md) variant for Form B); the L3 form makes this concrete as a tail-recursive value-threading loop. Both are firm L4 rows.

- `iterate_while` — signature:

  ```text
  iterate_while :: Step -> carry -> Solve Trajectory
    where Step       = carry -> Solve { carry', readout, continue }
          Trajectory = [readout]   -- with demand-pruning per derived-view-hoisting
  ```

  The combinator folds a `Step` over an initial `carry` value, threading the carry through and accumulating readouts, until the step signals `continue = False`. The monadic effect (`Solve`) is the `SimState`-monad of `solve-monad`. The fold body is exactly the L4 `krylov_step` shape: input is `(SimState, Krylov)` (the carry pair, where `SimState` is the monad's state and `Krylov` is the explicit value), output is the next carry plus the demand-prunable `StepOutputs` record plus the continue-bit (derived from `outputs.breakdown_token` and `convergence-test` against the residual proxy).

- `iterate_while_with_prev` — signature:

  ```text
  iterate_while_with_prev :: (PrevCarry -> Step) -> PrevCarry -> Step -> carry -> Solve Trajectory
  ```

  Where the first argument is a `PrevCarry`-parameterised step (the `steady_step` of Form B), the second is the initial `PrevCarry` value, the third is the bootstrapping step (the `first_step` of Form B that produces the initial `PrevCarry`), and the fourth is the initial carry. Used exactly when the first-iteration-unrolling rotation is applied; degenerates to `iterate_while` when `PrevCarry = ()`.

### What the L3 form for `iterate_while` looks like

For completeness — this is *not* a separate theme, but the natural fall-out of the `krylov_step` body's L4>L3 lowering. The L4 `iterate_while step carry₀` form (per the firm L4 row [`iterate_while`](../L4/iterate_while.md)) carries a `trajectory: [{ ...e }]` accumulator subject to §3.8 demand-driven pruning (Law 1 of `book/src/L4/iterate_while.md`, instantiated for the residual-norm case in `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm"). The L3 shape therefore depends on the downstream consumer's observation pattern, with two forms arising from the same L4 invocation under different consumer demands.

**Unpruned form** — the direct value-threaded dissolution of the L4 form when a downstream consumer reads `.trajectory` (no §3.8 collapse fires; the accumulator is materialized at L3):

```text
iterate_while_L3 step carry₀ sim₀ =
  let go (carry, sim, traj) =
        if not (p carry)
          then (carry, sim, reverse traj)         -- final_state, sim', trajectory
          else let (carry', sim', readout) = step (carry, sim)
               in go (carry', sim', readout : traj)
  in go (carry₀, sim₀, [])
```

**Pruned form** — the §3.8-collapsed shape that arises when the consumer observes only `final_state`-equivalent quantities (Palace's KSP case, per the four-scalar consumer surface at `reference/palace/palace/linalg/iterative.hpp:52-55` consumed solely at `reference/palace/palace/linalg/ksp.cpp:296-310`). Law 1 rewrites the body to omit the extras computation; the L3 form drops the accumulator entirely and the `step` is rendered in its `state`-only subgraph:

```text
iterate_while_L3_pruned step carry₀ sim₀ =
  let go (carry, sim) =
        if not (p carry)
          then (carry, sim)                       -- final_state, sim'
          else let (carry', sim') = step_state (carry, sim)
               in go (carry', sim')
  in go (carry₀, sim₀)
```

where `step_state = λ(carry, sim) -> let (carry', sim', _readout) = step (carry, sim) in (carry', sim')` is the §3.8-pruned subgraph of `step` that computes only the next carry (the extras computation is eliminated as dead code at the call site, not merely unused at runtime). The L3-side `step_state` has shape `(carry, sim) -> (carry', sim')` — the positional-tuple image of the L4-side `f_state : α -> α` of Law 1 (`book/src/L4/iterate_while.md:123-133`), with the `sim` thread surfacing as a positional argument at L3 because the `Solve` monad has dissolved (per §"Concept-page references" entry for `solve-monad.md`); the L4 `α` collapses to the L3 carry alone, with `sim` carried alongside positionally rather than monadically.

The L4>L3 collapse from the unpruned to the pruned form is governed by the rule:

$$
\frac{
  \text{only } \textsf{final\_state} \text{ of the L3 result is observed downstream}
}{
  \textsf{iterate\_while\_L3}\ p\ \textsf{step}\ \textsf{carry}_0\ \textsf{sim}_0 \;\equiv\; \textsf{iterate\_while\_L3\_pruned}\ p\ \textsf{step}_{\textsf{state}}\ \textsf{carry}_0\ \textsf{sim}_0
}
$$

which is exactly the L3-side image of Law 1 of [`iterate_while`](../L4/iterate_while.md) — the L4 demand-pruning law transports through the L4>L3 wrapper dissolution because the dissolution is value-thread-isomorphic on the body (established in §"Body identity-in-form across the L4>L3>L2 chain" below). The applicability of the pruned form is selected by Condition 5 in §"Applicability conditions" below; for Palace's actual KSP consumer surface, Condition 5 holds and the pruned form is the rendered L3 shape.

Both forms are tail-recursive value-threaded loops; the `Solve` monad has dissolved (the `sim` argument is positional, not monadic), and the `sequential-obstruction` of the outer loop survives at L3 (homed in the firm L3 entry [`L3/krylov_step`](../L3/krylov_step.md) §Algebraic-laws non-lift catalogue; `arnoldi_step.md:194-213` is the live anchor) — the L3 form names the loop tail-recursively but does not claim it lifts to a global tensor-field op. This is the expected outcome for Krylov methods at L3 per [`sequential-obstruction`](../concepts/sequential-obstruction.md). The unpruned form additionally allocates the trajectory list (an `O(N)` accumulator); the pruned form does not.

## Body identity-in-form across the L4>L3>L2 chain

The **L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence**: the L4>L3 hop is non-identity *at the wrapper level* (records dissolve, monad dissolves, readonly typing demotes, Form A/B presentation collapses), but the body's dataflow chain survives both hops textually unchanged. The structural facts that establish this:

1. **The L2→L3 rotation on the CG body is identity-in-form** (homed in [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md)): no unfolding, no global lift, no schema change. L2's primitive vocabulary (`apply_linop`, `axpy`, `axpby`, `dot`, scalar arithmetic) is already L3-native — each is a whole-tensor operation with no element loop exposed at L2 (e.g., `apply_linop : LinOp[(S: ...), $S] -> Tensor[$S] -> Tensor[$S]` is a global field operation, congruent over one shape group `S` of unknown rank per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2). `arnoldi_step.md:185-188` is the live anchor.

2. **The Arnoldi-step L2→L3 rotation** (`arnoldi_step.md:178-213`): the three uncontested primitives (`apply_BA`, `subdiag_norm`, `normalize`) are L3-trivial (identity lifts). The fourth (`orthogonalize` under MGS) carries a sequential obstruction — but this is at the *primitive* level, inside `op.orthog`, not at the `krylov_step` body level. The obstruction is localised to the orthog primitive; the `krylov_step` body around `op.orthog` is still identity-in-form (it calls `op.orthog` as an opaque operator).

3. **The L4 body** (from `L4/krylov_step` §Semantics, reproduced in §"L4 form (LHS)" above): each line is a binding of an L1 primitive (`apply_linop`, `axpy` / `axpby` / `axpbypcz`, `dot`, `nrm2`, `scal`) to a `let`-bound variable, plus the optional `op.orthog` / `op.scalars` call and the `derived_views` readout. Every primitive call survives L4>L3 textually unchanged (modulo the wrapper dissolution of §"L3 form" above). The body is identity-in-form between the L4 body and the L3 body for the same reason the L2 body is identity-in-form on the way to L3 — the primitives are L3-native.

**Consequence for L3 dep-map**: the body identity-in-form does **not** eliminate the L3 row — each layer is coherent within itself, and an L3 reader finds `krylov_step` defined in L3 vocabulary at L3 even when the lowering is trivial. The L4 entry lowers transitively to the L2 entry via this theme (L4>L3 wrapper dissolution) plus the L3>L2 theme (identity-in-form on the body, [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md)); the firm L3 entry [`L3/krylov_step`](../L3/krylov_step.md) is the wrapper-dissolution RHS rendered as a layer-coherent operator entry, not a duplicate of L2. The difference between "L3 `krylov_step`" and "L2 `krylov_step` with an outer `iterate_while` tail-recursion" is the **layer rendering**, not the operational content; both renderings are needed for their respective layers to be coherent.

## Evidence

L4 source (the input form of this lowering):

- `book/src/L4/krylov_step.md` — the firm L4 entry this lowering applies to: §Signature (Form A and Form B signatures), §Semantics (body shape, monadic effect placement), §"L4 vs L2 distinction" (the wrapper-vs-composition framing).

L3 evidence (the target form of this lowering, including the identity-in-form audit):

- `book/src/L3-L2/krylov-step-body-identity.md` §Evidence — the evidence for L2>L3 body identity. Claim 2 ("step body lifts as identity") is the cited support, preserved there with the verbatim claim quote.
- Arnoldi step L2>L3 lift — three uncontested primitives plus the variant-dependent `op.orthog` obstruction (localised below the step body, not at the body level). Firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop; the MGS obstruction firm at [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md). Confirms the audit.
- `book/src/L3/krylov_step.md` §Algebraic-laws non-lift catalogue — the negative L3 result for the *outer* loop. Cited for completeness; the outer-loop obstruction is independent of the step-body rotation handled by this theme.

L2 sink (the eventual target after L3>L2):

- `book/src/L2/krylov_step.md` — the L2 entry whose body shape matches the L3 form produced by this lowering. The L2 entry's §Semantics body and the L3 form's body are textually equivalent up to wrapper packaging.

Concept-page references (for the dissolved L4 vocabulary):

- `book/src/concepts/state-stratification.md:1-45` — the typed three-stratum record convention this lowering dissolves.
- `book/src/concepts/solve-monad.md:1-69` — the `Solve = StateT SimState Identity` monad this lowering dissolves.
- `book/src/concepts/first-iteration-unrolling.md:21-37` — the Form-A/Form-B distinction this lowering collapses.
- `book/src/concepts/sequential-obstruction.md` — the obstruction classification the L3 outer loop carries (referenced for completeness, not introduced).
- `book/src/concepts/derived-view-hoisting.md` — the demand-pruning algebra preserved across the rotation; the §"Worked example: CG residual norm" (lines 14-19) is the canonical §3.8 instantiation for `residual_norm` extras, cited by Condition 5 and the §"What the L3 form for `iterate_while` looks like" §3.8 preamble.

L0 consumer-surface evidence confirming Condition 5 across the KSP family (no per-iteration residual history is retained; the result is exactly four scalars):

- `reference/palace/palace/linalg/iterative.cpp:420-485` — PCG outer loop; `final_res`, `final_it` captured as scalars at `:484-485`.
- `reference/palace/palace/linalg/iterative.cpp:614-705` — GMRES inner Arnoldi loop; per-iteration beta printed or overwritten; `final_res`, `final_it` at `:703-704`.
- `reference/palace/palace/linalg/iterative.cpp:734-870` — FGMRES (one more workspace `Z[]`); same per-iteration beta discipline.
- `reference/palace/palace/linalg/iterative.hpp:52-55` — KSP result-extraction surface: exactly four mutable scalars (`converged`, `initial_res`, `final_res`, `final_it`); no trajectory-shaped field.
- `reference/palace/palace/linalg/iterative.hpp:97-108` — the four public `Get*` accessors (`GetConverged`, `GetInitialRes`, `GetFinalRes`, `GetNumIterations`); no `GetResidualHistory()` analogue.
- `reference/palace/palace/linalg/ksp.cpp:296-310` — sole caller; consumes the four scalars only; no per-iteration consumption anywhere in `palace/`.

## Status

`firm` — the rewrite shape is anchored against the firm L4 entry [`krylov_step`](../L4/krylov_step.md), the firm L4 rows [`iterate_while`](../L4/iterate_while.md) (with its Law 1 §3.8 demand-pruning rule) and [`iterate_while_with_prev`](../L4/iterate_while_with_prev.md). The L3 form is rendered in two shapes (pruned + unpruned) governed by Condition 5; the §"What the L3 form for `iterate_while` looks like" subsection cites the §3.8 collapse rule explicitly.
