# krylov-step-typed-wrapper-dissolution

The L4>L3 lowering theme for `krylov-step`. Dissolves the L4 typed-wrapper machinery — three-stratum state-stratification records, the `Solve` state monad, the `OpParams` `readonly` typing, and the Form-A/Form-B presentation distinction — into the L3 value-threading form expected by the global-tensor-field calculus. The kernel body's primitive sequence is unchanged by the rotation; only the wrapper dissolves.

## Slug

`krylov-step-typed-wrapper-dissolution`

## Context

L4 `krylov-step` (per [`L4/krylov-step`](../L4/krylov-step.md)) is the typed wrapper around the L2 primitive composition. The wrapper carries four pieces of L4-only machinery:

1. **Three-stratum state-stratification records** (per [`state-stratification`](../concepts/state-stratification.md)): `SimState` (externally-visible, persists across the solve), `OpParams` (operator-internal, captured once), `Krylov` (solve-local ephemeral bundle). At L4 these are *typed records* with `readonly` annotations and lifetime enforcement.
2. **The `Solve a = StateT SimState Identity a` monad** (per [`solve-monad`](../concepts/solve-monad.md)). The kernel body lives inside a monadic action; the sole monadic effect is the `SimState.it` increment via `modify`.
3. **`OpParams` `readonly` typing**. The kernel cannot re-inspect variant selectors — this is a typing invariant at L4, sharpening the L2-level variant-absorption discipline.
4. **The Form-A vs Form-B presentation distinction** (per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)). Form A keeps the first-iteration branch inside the body; Form B splits into `(first_step, steady_step)` with `PrevCarry` threaded as a closure parameter of the outer combinator.

L3's job is the *iteration rotation*: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly (per [`sequential-obstruction`](../concepts/sequential-obstruction.md)). L3 carries neither monadic structure (that is L4's coordination layer, deliberately above L3) nor typed state-stratification records (the three strata exist at L3 only as positional values whose ordering is a convention, not a typing). The lowering is therefore the *dissolution* of the L4 wrapper, recovering the value-threading form that L3 expects.

The L3 form this lowering produces is **identity-in-form** on the kernel body's primitive sequence — the same five primitive groups (apply, optional auxiliary, iterate-update, scalar-update, output-readout) in the same dataflow-forced order — but **substantively rotated** at the type/wrapper level. The further L3>L2 lowering on the kernel body is identity-in-form per the firm theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) (which ratifies the combinator-miner cycle-002 assertion; the original slice evidence at `cg.md:341-362` has been lifted into that firm entry per the cycle-009 corpus reduction, and `arnoldi_step.md:178-213` remains the valid live anchor), but this does **not** collapse the L3 row away: the L4 entry lowers via this theme to the firm L3 entry [`L3/krylov-step`](../L3/krylov-step.md) (the value-threaded RHS rendered as a layer-coherent operator), and the body's L3>L2 identity hop is completed by the separate theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md). The lowering chain is therefore L4>L3>L2>L1 with no skipped rows. (The earlier cycle-006 reading — that the body's identity-in-form lets this theme skip the L3 row and lower transitively to L2 — is SUPERSEDED by the user directive 2026-05-27 mid-cycle-009 codified as the CLAUDE.md §Methodology invariants bullet **Identity-lowerings still require both L levels**: each layer is coherent within itself, so an L3 reader must find `krylov-step` defined in L3 vocabulary at L3 even when the body rewrite is trivial.) See §"Audit of cycle-002 identity-in-form claim" below for the full audit.

## L4 form (LHS)

The two L4 surface forms from the harvester output, reproduced for the LHS of the rewrite:

**Form A — branch-in-body** (default):

```text
krylov-step :: OpParams -> Krylov -> (SimState -> Solve { sim: SimState', krylov: Krylov', outputs: StepOutputs })
```

With the body shape (per `L4/krylov-step` §Semantics):

```text
krylov-step op K = \s -> do
  let w       = apply_linop op.T K.<input_field>
  let K_aux   = optionally apply op.orthog (K.V_prefix, w)        -- or op.scalars (K.k, K.scalar_state); or K (no-op)
  let K'      = krylov_update K_aux op w
  let outputs = derived_views K' op
  modify (\s -> s { it = s.it + 1 })
  pure { krylov: K', outputs }
```

The body is consumed by an outer `iterate_while`-style combinator (currently unanchored in the L4 vocabulary — see [Speculative L4 operators](#speculative-l4-operators)) inside `solve-monad`'s `restart_cycle` / `inner_loop`.

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

3. **`OpParams` `readonly` typing collapses to a documented invariant.** At L4 the `OpParams` `readonly` annotation forbids the kernel from re-inspecting variant selectors (`pc_side`, `gs_orthog`, polynomial-kind, etc.); the variant axes are absorbed into the constructed-operator surfaces `op.T`, `op.orthog?`, `op.scalars?`. At L3 the same absorption holds — the kernel calls `op.T`, `op.orthog`, `op.scalars` and never branches on their internal selectors — but this is a *documented invariant* (a comment, or a coding discipline) rather than a typing constraint. L3 has no `readonly` annotation in its calculus; the discipline is preserved by convention and verified by reading the body. **Per the harvester's caveat on this point** (`L4/krylov-step` §Signature, point 1), this is the load-bearing typing distinction between L4 and L3, and the rotation makes it explicit by *demoting* the constraint.

4. **Form-A vs Form-B distinction collapses into carry-threading.** At L4 Form B is a presentation rotation: `(first_step, steady_step)` is a typed pair of functions where `steady_step` takes `PrevCarry` as a closure parameter of the loop driver (`iterate_while_with_prev` rather than `iterate_while`). At L3 the same content is recovered by adding a position to the threaded tuple: the loop combinator becomes a generic tail-recursive value-threading loop, and `PrevCarry` is just another value in the tuple. The L4 distinction between "closure parameter of the combinator" and "state field of the iteration" loses operational meaning at L3 (both are positional values; there is no combinator-vs-state typing). **Consequence**: at L3 there is only one form of `krylov-step` (the value-threaded form), with the Form-B variants distinguished only by whether the threaded tuple has a `carry` position. The Form-A/Form-B presentation choice becomes an artefact of L4 alone.

### What does NOT change in the rotation

The five primitive-group dataflow chain — `apply_linop`, optional auxiliary (`op.orthog` / `op.scalars` / no-op), iterate-update (`axpy` / `axpby` / `axpbypcz`), scalar-update (`dot` / `nrm2` plus scalar arithmetic), output-readout (`derived_views`) — is **textually identical** between the L4 body and the L3 body. The dataflow constraints are unchanged (the L1 primitives are pure on their inputs; no aliasing introduced or removed). The variant-axis profile is unchanged at six (axes are absorbed in `op.*` surfaces at L3 just as they are at L4, modulo the `readonly` typing demotion).

### What this lowering does NOT cover

- **L3>L2 lowering on the body** (the iteration rotation in the negative direction). The L3 body is in primitive-composition form already; the further L3>L2 lowering on the body is identity-in-form per the combinator-miner cycle-002 claim, audited and confirmed in this report. That lowering belongs in `book/src/L3-L2/` and is a separate theme (likely a one-line `krylov-step-body-identity` theme noting the L3>L2 body rewrite is the identity rotation).
- **Outer-loop sequential obstruction**. The fact that the *outer* `iterate_while` loop carries a `sequential-obstruction` at L3 (per `cg.md:341-349`, `arnoldi_step.md:194-213`) is a property of the loop, not of the step kernel. The step-body L4>L3 lowering described here is independent of the outer-loop obstruction. The loop obstruction is documented in the slice corpus's L3 sections and the `sequential-obstruction` concept page; this theme does not re-state it.
- **MGS-orthogonalisation sequential obstruction**. Per `arnoldi_step.md:194-213`, the `gs_orthog = MGS` variant of `op.orthog` carries a sequential obstruction at L3 (the per-i sequencing of `H[i,j] ← ⟨w, V[i]⟩` and `w ← w − H[i,j] · V[i]`). This is a property of the `orthog` primitive under the MGS variant, not of `krylov-step` itself. The `krylov-step` body sees `op.orthog` as an opaque call site; whether that call lifts depends on the variant axis, which is absorbed below the `krylov-step` surface. This theme does not duplicate the `orthog`-variant obstruction; it cites it.

## Applicability conditions

The rewrite is valid when all four of the following hold (which they do for the firm L4 `krylov-step` entry by construction):

1. **The L4 `Solve` monad's effect domain is exactly `SimState`.** The only `modify` calls in the kernel body touch `SimState` (specifically the `it` counter); no `Krylov` field is touched via a monadic effect; no `OpParams` field is touched via a monadic effect (it is `readonly` by typing). If a future variant of `krylov-step` introduces a second `SimState`-touching `modify` (e.g., breakdown signalling via `SimState.converged`), the rewrite still applies — the L3 form just acquires a second positional update line in the let-chain. If a future variant introduces a *non-`SimState`*-effecting monadic call (e.g., logging via `tell`), the rewrite breaks at the `Solve = StateT SimState Identity` typing, and a richer L3 effect representation would be needed.

2. **`OpParams` is closure-captured at the per-step call site, not threaded.** The L4 signature has `op` as the first positional argument of `krylov-step :: OpParams -> Krylov -> ...`, and the call site uses partial application (`krylov-step op` as a curried form). At L3 this becomes `op` as a closure-captured argument of the body. The rewrite assumes `op` is not re-bound between steps; if a future variant has per-step-varying `op` (which would defeat variant absorption), the rewrite needs revision.

3. **The five primitive groups are L3-native or carry their own L3-edge classification.** Each of `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal` is an L1 primitive whose L2>L3 lift is identity (per `cg.md:351-362`, `arnoldi_step.md:185-188`). The optional auxiliary stage (`op.orthog` under MGS) carries its own L3 obstruction (per `arnoldi_step.md:194-213`), which is independent of the `krylov-step` body rewrite. This dispatch's lowering does not introduce new L3 obstructions; it inherits the existing classification of its constituent primitives.

4. **The `Krylov` ephemeral bundle has plain-value lifecycle (born at restart, discarded at restart-or-return) and is not aliased by any other state.** The L4 typing makes this structural (`Krylov` is not a field of `SimState`; lifetime is restart-scoped); at L3 it becomes a discipline. The rewrite assumes no caller threads `Krylov` across restart boundaries (which would mis-type its lifetime). Per `solve-monad.md:53`, this discipline is honoured by `restart_cycle` building a fresh `Krylov` per cycle.

5. **The downstream consumer of the surrounding `iterate_while` invocation observes only `final_state`-equivalent quantities (no per-iteration trajectory readout).** This is the precondition for the §3.8 demand-pruning collapse from the unpruned L3 form (`[readout]` accumulator) to the pruned L3 form (single readout / accumulator dropped) shown in §"What the L3 form for `iterate_while` looks like" above. Per Law 1 of [`iterate-while`](../L4/iterate-while.md) and the worked example in `book/src/concepts/derived-view-hoisting.md`, when the consumer's destructuring reads only `final_state` (or the L3-positional equivalent — the final-iteration carry value), the per-step `extras` computation in the step body is eliminated by the §3.8 rewrite, the L4 `[readout]` trajectory collapses to `[]`, and the L3 form is the pruned shape. **Palace satisfies this condition by construction**: the `IterativeSolver` result-extraction surface materializes exactly four scalars (`converged`, `initial_res`, `final_res`, `final_it` at `reference/palace/palace/linalg/iterative.hpp:52-55`), each of which is either a carry field at the final iteration or a pre-loop initialization; the sole caller `BaseKspSolver::Mult` at `reference/palace/palace/linalg/ksp.cpp:296-310` consumes only those four scalars (branch on `GetConverged`, ratio in warning via `GetFinalRes()/GetInitialRes()`, sum into counter via `GetNumIterations`). No per-iteration consumption exists in `palace/`. **When violated** — e.g., a hypothetical future Palace surface `GetResidualHistory(): std::vector<double>` reading the per-step `residual_norm` extras — Condition 5 fails, §3.8 does not fire for that consumer, and the L3 form must be re-rendered with the accumulator restored (the unpruned form). The L4 form is invariant under this consumer change; only the L4>L3 lowering's rendered L3 shape selects between the two forms.

If a future Krylov-shaped slice violates any of these (e.g., a method whose `OpParams` needs per-step mutation, or whose step body needs effects beyond `SimState`, or whose consumer reads the trajectory), the L4>L3 lowering would need to be refined; the speculative-operator slot would be enlarged.

## Justification kind

**`structural`** with a secondary **`reduction-chain`** component.

**Abstraction-direction note**: L4 is the higher-abstraction layer (typed records, monadic effect, readonly typing constraint, Form-A/B presentation distinction) and L3 is the lower-abstraction layer (positional values threaded explicitly, documented invariants in place of typing). The rotation direction is L4 → L3: the higher-level wrapper machinery *dissolves* into the value-threaded form below it. This is the correct lowering direction under the methodology's rotation-quality criterion — L_{n+1} (L4) is more compact / more abstract / more equational, and the L_n (L3) form is the dissolved trace. A reader who sees the L4 form as "more elaborate" should read the elaboration as *abstraction* (typing buys mechanical-checkability of variant absorption), not as accidental complexity.

- The dominant content is structural: the L4 wrapper (record types, monad, readonly typing, Form-A/B distinction) dissolves into an L3 value-threading form, and the kernel body's primitive sequence is preserved by construction (not by an algebraic argument, but by the syntactic shape of the rewrite — every L4 primitive call becomes an L3 primitive call at the same position in the dataflow chain).
- The secondary reduction-chain component is the `modify (\s -> s { it = s.it + 1 })` to `s' = s { it = s.it + 1 }` step. This is a one-step reduction of the `StateT` monad's `modify` operator — `modify f` in `StateT s m a` unfolds to `\s -> ((), f s)`, and the surrounding `do`-block desugars to explicit value-threading. The reduction is mechanical (the `StateT` monad's evaluation rules are standard); the L3 form is the desugared trace.

The combinator-miner's cycle-002 assertion (cited at `cg.md:351-362`) is justified as **`empirical-match`** at the L2>L3 edge — the slice corpus's L2 prose uses primitive-composition form that is L3-native by inspection, and the assertion is the recognition that no rewrite is needed. The L4>L3 hop covered here is a different rotation (typed wrapper to value-threaded form); it is **not** identity-in-form on the wrapper, only on the body. The two rotations compose to give an L4>L2 chain that is non-identity at the wrapper level and identity-in-form on the body — which is the harvester's "Lowers to" claim.

## Speculative L4 operators

This theme surfaces one L4 vocabulary need that the harvester output flagged as unanchored (caveat 2 in the wave-1 report). The lowering's L4 form refers to an outer combinator `iterate_while` (and its `_with_prev` variant for Form B); the L3 form makes this concrete as a tail-recursive value-threading loop. **The L4 anchor for these combinators does not yet exist** — `solve-monad.md` references `inner_loop` informally without naming the combinator.

- `iterate_while` — rough-in. Intended signature (best guess based on the L4 form):

  ```text
  iterate_while :: (carry -> Solve { carry: carry', readout: r, continue: Bool }) -> carry -> Solve [r]
  ```

  Or, decomposed:

  ```text
  iterate_while :: Step -> carry -> Solve Trajectory
    where Step       = carry -> Solve { carry', readout, continue }
          Trajectory = [readout]   -- with demand-pruning per derived-view-hoisting
  ```

  The combinator folds a `Step` over an initial `carry` value, threading the carry through and accumulating readouts, until the step signals `continue = False`. The monadic effect (`Solve`) is the `SimState`-monad of `solve-monad`. The fold body is exactly the L4 `krylov-step` shape: input is `(SimState, Krylov)` (the carry pair, where `SimState` is the monad's state and `Krylov` is the explicit value), output is the next carry plus the demand-prunable `StepOutputs` record plus the continue-bit (derived from `outputs.breakdown_token` and `convergence-test` against the residual proxy).

- `iterate_while_with_prev` — rough-in. Intended signature:

  ```text
  iterate_while_with_prev :: (PrevCarry -> Step) -> PrevCarry -> Step -> carry -> Solve Trajectory
  ```

  Where the first argument is a `PrevCarry`-parameterised step (the `steady_step` of Form B), the second is the initial `PrevCarry` value, the third is the bootstrapping step (the `first_step` of Form B that produces the initial `PrevCarry`), and the fourth is the initial carry. Used exactly when the first-iteration-unrolling rotation is applied; degenerates to `iterate_while` when `PrevCarry = ()`.

Both rough-ins live in [the L4 dep-map](../L4/index.md) annotated as `(rough-in, proposed-by: abstractor:2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering)`. Harvester promotes later — likely candidate for cycle-007's `harvester` dispatch on the L4 loop-combinator family. **Note**: these are the same combinators the harvester output flagged as unanchored (caveat 2); this theme's L4 form re-uses them as already-named placeholders, not as fresh proposals. The promotion to firm L4 vocabulary is needed to honour the L4-rows-depend-on-L4-rows convention (per cycle-005 open question `state-stratification-as-l4-concept-or-l4-row`).

### What the L3 form for `iterate_while` looks like

For completeness — this is *not* a separate theme, but the natural fall-out of the `krylov-step` body's L4>L3 lowering. The L4 `iterate_while step carry₀` form (per the firm L4 row [`iterate-while`](../L4/iterate-while.md)) carries a `trajectory: [{ ...e }]` accumulator subject to §3.8 demand-driven pruning (Law 1 of `book/src/L4/iterate-while.md`, instantiated for the residual-norm case in `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm"). The L3 shape therefore depends on the downstream consumer's observation pattern, with two forms arising from the same L4 invocation under different consumer demands.

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

where `step_state = λ(carry, sim) -> let (carry', sim', _readout) = step (carry, sim) in (carry', sim')` is the §3.8-pruned subgraph of `step` that computes only the next carry (the extras computation is eliminated as dead code at the call site, not merely unused at runtime). The L3-side `step_state` has shape `(carry, sim) -> (carry', sim')` — the positional-tuple image of the L4-side `f_state : α -> α` of Law 1 (`book/src/L4/iterate-while.md:123-133`), with the `sim` thread surfacing as a positional argument at L3 because the `Solve` monad has dissolved (per §"Concept-page references" entry for `solve-monad.md`); the L4 `α` collapses to the L3 carry alone, with `sim` carried alongside positionally rather than monadically.

The L4>L3 collapse from the unpruned to the pruned form is governed by the rule:

$$
\frac{
  \text{only } \textsf{final\_state} \text{ of the L3 result is observed downstream}
}{
  \textsf{iterate\_while\_L3}\ p\ \textsf{step}\ \textsf{carry}_0\ \textsf{sim}_0 \;\equiv\; \textsf{iterate\_while\_L3\_pruned}\ p\ \textsf{step}_{\textsf{state}}\ \textsf{carry}_0\ \textsf{sim}_0
}
$$

which is exactly the L3-side image of Law 1 of [`iterate-while`](../L4/iterate-while.md) — the L4 demand-pruning law transports through the L4>L3 wrapper dissolution because the dissolution is value-thread-isomorphic on the body (the §"Audit of cycle-002 identity-in-form claim" below establishes this). The applicability of the pruned form is selected by the new Condition 5 in §"Applicability conditions" below; for Palace's actual KSP consumer surface, Condition 5 holds and the pruned form is the rendered L3 shape.

Both forms are tail-recursive value-threaded loops; the `Solve` monad has dissolved (the `sim` argument is positional, not monadic), and the `sequential-obstruction` of the outer loop survives at L3 (per `cg.md:341-349`) — the L3 form names the loop tail-recursively but does not claim it lifts to a global tensor-field op. This is the expected outcome for Krylov methods at L3 per `sequential-obstruction.md`. The unpruned form additionally allocates the trajectory list (an `O(N)` accumulator); the pruned form does not.

## Audit of cycle-002 identity-in-form claim

The open question `krylov-step-l3-identity-in-form-audit` (scaffolding/open-questions.md) records the combinator-miner cycle-002 assertion: "the L2→L3 rotation on the `krylov-step` body is identity-in-form, citing `cg.md:351-362` and `arnoldi_step.md:185-188`." (Note: the open-questions ledger records the citation as `cg.md:352-362`; the range that fully contains Claim 2 — including its `### Claim 2: step body lifts as identity` header at line 351 — is `cg.md:351-362`. This dispatch canonicalizes to the inclusive range.) This dispatch audits the assertion as the secondary half of its job.

**Audit verdict**: The cycle-002 assertion is **correct as stated** (about L2>L3), and remains correct for the body. The L4>L3 hop this dispatch addresses is a different rotation; the two compose to give the full L4>L2 chain.

**Evidence reviewed**:

1. `cg.md:341-362` (cited by combinator-miner; re-read for this audit) — the L2→L3 rotation claims for CG. Claim 2 ("step body lifts as identity") states verbatim: *"The L2→L3 rotation on the step body is therefore the **identity in form**: no unfolding, no global lift, no schema change."* The justification is that L2's primitive vocabulary (`apply_linop`, `axpy`, `axpby`, `dot`, scalar arithmetic) is already L3-native — each is a whole-tensor operation with no element loop exposed at L2. **Audit finding**: the assertion is well-supported; the L2 primitives are L3-native by inspection of their signatures (e.g., `apply_linop : LinOp -> Tensor[N] -> Tensor[N]` is a global field operation).

2. `arnoldi_step.md:178-213` (cited by combinator-miner; re-read for this audit) — the L2→L3 rotation for the Arnoldi step. The three uncontested primitives (`apply_BA`, `subdiag_norm`, `normalize`) are listed as L3-trivial (identity lifts). The fourth (`orthogonalize` under MGS) carries a sequential obstruction — but this is at the *primitive* level, inside `op.orthog`, not at the `krylov-step` body level. **Audit finding**: the obstruction is correctly localised to the orthog primitive; the `krylov-step` body around `op.orthog` is still identity-in-form (it calls `op.orthog` as an opaque operator).

3. The L4 form's body (from `L4/krylov-step` §Semantics, reproduced in §"L4 form (LHS)" above). Each line of the body is a binding of an L1 primitive (`apply_linop`, `axpy` / `axpby` / `axpbypcz`, `dot`, `nrm2`, `scal`) to a `let`-bound variable, plus the optional `op.orthog` / `op.scalars` call and the `derived_views` readout. **Audit finding**: every primitive call survives L4>L3 textually unchanged (modulo the wrapper dissolution discussed in §"L3 form" above). The body is identity-in-form between the L4 body and the L3 body for the same reason the L2 body is identity-in-form on the way to L3 — the primitives are L3-native.

**Audit verdict — confirmed-with-refinement**: the cycle-002 framing was "L2>L3 step-body lift is identity-in-form". This dispatch sharpens to: "**L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence**; the L4>L3 hop is non-identity *at the wrapper level* (records dissolve, monad dissolves, readonly typing demotes, Form A/B presentation collapses), but the body's dataflow chain survives both hops textually unchanged." This refinement is more precise but does not contradict the original claim. The original framing was correct for the question it asked (about the body); this dispatch answers the broader question (about the wrapper).

**Consequence for L3 dep-map** (cycle-006 verdict, SUPERSEDED cycle-010): per the harvester's "Lowers to" section and per this audit, the cycle-006 verdict was that **no L3 `krylov-step` row was proposed** on identity-in-form grounds. This verdict is **SUPERSEDED** by the user directive 2026-05-27 mid-cycle-009 codified as the CLAUDE.md §Methodology invariants bullet **Identity-lowerings still require both L levels**: each layer is coherent within itself, and an L3 reader must find `krylov-step` defined in L3 vocabulary at L3, even when the lowering is trivial. The L4 entry lowers transitively to the L2 entry via this theme (L4>L3 wrapper dissolution) plus a one-line L3>L2 theme (identity-in-form on the body, ratified at [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) cycle-009). **Cycle-010 backfill**: the L3 entry [`L3/krylov-step`](../L3/krylov-step.md) was authored cycle-010 wave-1 (`reports/2026-05-27T215300Z-harvester-l3-krylov-step/CYCLE.md`) per priority #20 (identity-lowering-both-levels-backfill); the L3 form is the wrapper-dissolution RHS rendered as a layer-coherent operator entry, not a duplicate of L2. The "operational difference" framing was a category error — the difference between "L3 `krylov-step`" and "L2 `krylov-step` with an outer `iterate_while` tail-recursion" is the **layer rendering**, not the operational content; both renderings are needed for their respective layers to be coherent.

**Open question disposition**: this dispatch *audits* the cycle-005 open question `krylov-step-l3-identity-in-form-audit` and proposes closing it as **confirmed-with-refinement** — the assertion holds and the framing is sharpened (the L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence; the L4>L3 hop is non-identity only at the wrapper level). This identity-in-form finding governs the *body* rewrite; it does NOT eliminate the L3 row — per the cycle-009 invariant **Identity-lowerings still require both L levels**, the firm L3 entry [`L3/krylov-step`](../L3/krylov-step.md) is its layer-coherent rendering (authored cycle-010 wave-1, see §"Audit of cycle-002 identity-in-form claim" below). Integrator will mark accordingly; if integration uncovers a non-identity finding (e.g., a corpus check on a slice this dispatch did not re-verify reveals body-level rotation), the question stays open and the L3 row is re-rendered with the body rotation made explicit.

## Verified-against

L4 source (the input form of this lowering):

- `book/src/L4/krylov-step.md` (wave-1 harvester output, this cycle; the firm L4 entry this lowering applies to) — §Signature (Form A and Form B signatures), §Semantics (body shape, monadic effect placement), §"L4 vs L2 distinction" (the wrapper-vs-composition framing).
- `reports/2026-05-27T080944Z-harvester-krylov-step-L4/CYCLE.md` — the harvester dispatch report carrying the same content plus open questions (caveat 2 on `iterate_while` anchoring, cited above).

L3 evidence (the target form of this lowering, including the identity-in-form audit):

- `book/src/spec/slices/cg.md:341-362` — the combinator-miner cycle-002 evidence for L2>L3 body identity. Claim 2 ("step body lifts as identity") is the cited support. Re-read for this audit; assertion confirmed.
- `book/src/spec/slices/arnoldi_step.md:178-213` — L2>L3 lift for arnoldi step. Three uncontested primitives plus the variant-dependent `op.orthog` obstruction (which is localised below the step body, not at the body level). Confirms the audit.
- `book/src/spec/slices/cg.md:347-350` (Claim 1, outer-loop obstruction) — the negative L3 result for the *outer* loop. Cited for completeness; the outer-loop obstruction is independent of the step-body rotation handled by this theme.

L2 sink (the eventual target after L3>L2):

- `book/src/L2/krylov-step.md` (cycle-005 firm) — the L2 entry whose body shape matches the L3 form produced by this lowering. The L2 entry's §Semantics body and the L3 form's body are textually equivalent up to wrapper packaging.

Concept-page references (for the dissolved L4 vocabulary):

- `book/src/concepts/state-stratification.md:1-45` — the typed three-stratum record convention this lowering dissolves.
- `book/src/concepts/solve-monad.md:1-69` — the `Solve = StateT SimState Identity` monad this lowering dissolves.
- `book/src/concepts/first-iteration-unrolling.md:21-37` — the Form-A/Form-B distinction this lowering collapses.
- `book/src/concepts/sequential-obstruction.md` — the obstruction classification the L3 outer loop carries (referenced for completeness, not introduced).
- `book/src/concepts/derived-view-hoisting.md` — the demand-pruning algebra preserved across the rotation; the §"Worked example: CG residual norm" (lines 14-19) is the canonical §3.8 instantiation for `residual_norm` extras, cited by Condition 5 and the §"What the L3 form for `iterate_while` looks like" §3.8 preamble.

<!-- The narrative §"Verified-against" list above carries the cycle-006 evidence registry (prose-shaped: file + section descriptor); the trailing `verified_against:` YAML block below carries the cycle-007 wave-2 audit's structured evidence trail (per-citation verdict + audited_at + note), per the trailing-YAML precedent at `book/src/L1-L0/axpby-mutation-rotation.md:173-189`. Both lists are intentionally retained: the prose form is the human-readable evidence registry; the YAML form is the machine-checkable audit-trail. -->

verified_against:
  - citation: book/src/L4/iterate-while.md:28-43
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: cycle-007 firm L4 signature explicitly carries trajectory:[{...e}]; cycle-006 L3 rendering correctly omits it per §3.8 collapse but elides the rule-citation. This dispatch adds the citation.
  - citation: book/src/L4/iterate-while.md:123-133
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Law 1 (trajectory pruning) is the rule that justifies the cycle-006 L3 single-readout rendering for Palace; now cited explicitly in §"What the L3 form for iterate_while looks like" and Condition 5.
  - citation: book/src/L4/iterate-while-with-prev.md:137-147
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Law 2 of the with-prev chapter lifts the pruning rule to both step bodies; same disposition for the Form B L3 rendering covered by this theme.
  - citation: reference/palace/palace/linalg/iterative.cpp:420-485
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: PCG outer loop retains no per-iteration residual history; final_res, final_it captured as scalars at lines 484-485. Confirms Condition 5 holds for CG.
  - citation: reference/palace/palace/linalg/iterative.cpp:614-705
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: GMRES inner Arnoldi loop same disposition as PCG; per-iteration beta either printed or overwritten; final_res, final_it captured at 703-704. Confirms Condition 5 holds for GMRES.
  - citation: reference/palace/palace/linalg/iterative.cpp:734-870
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: FGMRES structurally identical to GMRES (one more workspace Z[] for flexible-preconditioner Krylov basis); same per-iteration beta discipline. Confirms Condition 5 holds for FGMRES.
  - citation: reference/palace/palace/linalg/iterative.hpp:52-55
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: KSP result-extraction surface is exactly four mutable scalars (converged, initial_res, final_res, final_it); no list-shaped or trajectory-shaped field. Canonical structural evidence that Condition 5 holds in Palace.
  - citation: reference/palace/palace/linalg/iterative.hpp:97-108
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Four public Get* accessors parallel to the four scalars (GetConverged, GetInitialRes, GetFinalRes, GetNumIterations); no GetResidualHistory() or analogue.
  - citation: reference/palace/palace/linalg/ksp.cpp:296-310
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Sole caller of KSP result-extraction surface; consumes converged (branch), final_res/initial_res (warning ratio), final_it (counter sum); no per-iteration consumption anywhere in palace/. Operational evidence that Condition 5 holds.
  - citation: book/src/concepts/derived-view-hoisting.md:14-19
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: §"Worked example: CG residual norm" is the canonical instantiation of the §3.8 pruning for iterate_while's residual_norm extras; cross-referenced from §"What the L3 form for iterate_while looks like" §3.8 preamble and from Condition 5.

## Status

`firm` — the theme's rewrite shape is fully anchored against the cycle-006 wave-1 firm L4 entry [`krylov-step`](../L4/krylov-step.md), the cycle-007 wave-1 firm L4 row [`iterate-while`](../L4/iterate-while.md) (with its Law 1 §3.8 demand-pruning rule), the cycle-007 wave-1 firm L4 row [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md), and the cycle-007 wave-2 lowering-verifier audit (`reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md`, verdict (c) — L3 single-readout is correct under §3.8 pruning for Palace's KSP consumer surface). The L3 form is rendered in two shapes (pruned + unpruned) governed by Condition 5; the §"What the L3 form for `iterate_while` looks like" subsection cites the §3.8 collapse rule explicitly; the trailing `verified_against:` block carries the cycle-007 wave-2 audit's 10-citation evidence base. The two speculative L4 operators (`iterate_while`, `iterate_while_with_prev`) are now firm; the audit of the cycle-002 identity-in-form claim is preserved. The cycle-006 / cycle-007 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` is closed by this dispatch.
