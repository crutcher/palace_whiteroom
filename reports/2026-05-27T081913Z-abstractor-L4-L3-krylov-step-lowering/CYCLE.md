---
agent: abstractor
invoked_at: 2026-05-27T08:19:13Z
scope: L4>L3 theme sketch — krylov-step typed-wrapper dissolution
status: integrated
integrated_at: 2026-05-27T09:08:49Z
integration_commit: 704717b
integration_notes: |
  Cycle-006 wave-2 abstractor L4>L3 theme (5 of 5 applied this cycle). Per-report integrator
  applied 3 explicit proposed-changes plus 1 discretionary L4-L3/index.md placeholder
  displacement (paralleling wave-1's L4/index.md pattern). The cycle-006 audit confirms-with-
  refinement the cycle-005 OQ krylov-step-l3-identity-in-form-audit. Per-report deferred
  integrated_at to finalize per role-spec.
inputs:
  - reports/2026-05-27T080944Z-harvester-krylov-step-L4/CYCLE.md (wave-1 harvester output; Form A + Form B signatures)
  - book/src/L2/krylov-step.md (cycle-005 L2 firm entry; the eventual sink of the chain via L3>L2)
  - book/src/L4-L3/index.md (current L4>L3 Part overview; empty theme list)
  - book/src/concepts/state-stratification.md (typing dissolved by this lowering)
  - book/src/concepts/solve-monad.md (monadic effect dissolved by this lowering)
  - book/src/concepts/first-iteration-unrolling.md (Form B PrevCarry threading)
  - book/src/spec/slices/cg.md:341-362 (combinator-miner's identity-in-form claim against L2>L3 edge; cited for audit)
  - book/src/spec/slices/arnoldi_step.md:178-213 (arnoldi step L2>L3 lift; partial obstruction case)
  - scaffolding/open-questions.md §`krylov-step-l3-identity-in-form-audit` (the cycle-005 question this dispatch audits)
  - reports/2026-05-27T080000Z-cycle-planner-cycle-006/CYCLE.md §"Open questions / caveats" item 2 (L3 promotion contingency)
---

# REPORT: L4>L3 theme sketch — krylov-step typed-wrapper dissolution

## Summary

The L4 `krylov-step` (wave-1 harvester output) is the typed-wrapper companion to the L2 firm entry: it re-types the kernel against a three-stratum state record (`SimState` / `OpParams` / `Krylov`), wraps the body in the `Solve a = StateT SimState Identity a` monad, and optionally splits the body into `(first_step, steady_step)` per `first-iteration-unrolling`. **L3's role** is iteration-rotation: state evolution as `state' = f(state, params)` over whole-tensor primitives, with sequential obstructions named explicitly. L3 does not carry monadic structure (that's L4's coordination layer) and does not carry typed state-stratification records (the three strata exist at L3 as positional values threaded through composition, not as typed records with enforcement). This theme — `krylov-step-typed-wrapper-dissolution` — names the four-part rewrite that takes the L4 form to its L3 form: (a) `StateT SimState` collapses to explicit `SimState` value-threading; (b) the three named records dissolve to positional tuples whose ordering is conventional, not typed; (c) `OpParams`'s `readonly` typing collapses to a documented invariant ("variant selectors are not re-inspected inside the body") that L3 cannot enforce; (d) Form B's `PrevCarry` collapses from a closure parameter of the loop combinator to an additional positional value in the threaded tuple. **Audit verdict on the combinator-miner cycle-002 assertion**: the assertion is about L2>L3, not L4>L3, and is **correct at that edge** (the L2 step body's primitives are L3-native by construction). The L4>L3 transition this dispatch covers is the **substantive rotation hop** — it is non-identity at the type/wrapper level (records, monad, readonly typing, Form-A/B presentation all dissolve), but **identity-in-form on the kernel body's dataflow shape** (the same five primitive groups in the same order). The combination — non-trivial L4>L3 wrapper rotation + identity-in-form L3>L2 body — supports the harvester's "Lowers to" claim that no L3 `krylov-step` row is needed: the L4 entry lowers via this theme to a *value-threaded form indistinguishable from L2*, and the L3>L2 hop is the identity-in-form claim already on file. **No L3 row proposed.** One speculative L4 operator surfaces — `iterate_while` (and its `_with_prev` variant) — which the harvester output already flagged as an unanchored L4 reference (caveat 2 in the wave-1 report). This theme's RHS makes the `iterate_while` shape explicit at L3 as a tail-recursive value-threading loop, sharpening the call for an L4 anchor.

## Proposed changes

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[create file — see "Theme content" below for the full body]
```

```edit:book/src/L4/index.md
[append speculative-operator entry for `iterate_while` (and `iterate_while_with_prev` variant) to the dep-map, with `(rough-in, proposed-by: abstractor:2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering)` annotation — see "L4 dep-map rough-in" below]
```

```edit:book/src/SUMMARY.md
[add chapter entry under the `# L4 > L3 — Lowering` Part, after `- [Overview](./L4-L3/index.md)`:
- [krylov-step-typed-wrapper-dissolution](./L4-L3/krylov-step-typed-wrapper-dissolution.md)
]
```

## Theme content

### File: `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`

```markdown
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

The L3 form this lowering produces is **identity-in-form** on the kernel body's primitive sequence — the same five primitive groups (apply, optional auxiliary, iterate-update, scalar-update, output-readout) in the same dataflow-forced order — but **substantively rotated** at the type/wrapper level. Crucially, the further L3>L2 lowering on the kernel body is identity-in-form per the combinator-miner cycle-002 assertion (`cg.md:341-362`, `arnoldi_step.md:178-213`), so no L3 `krylov-step` row is promoted by this theme: the L4 entry lowers via this theme to an L3 form that is value-thread-isomorphic to the L2 form, and the L3>L2 hop is the trivial completion. See §"Audit of cycle-002 identity-in-form claim" below for the full audit.

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

If a future Krylov-shaped slice violates any of these (e.g., a method whose `OpParams` needs per-step mutation, or whose step body needs effects beyond `SimState`), the L4>L3 lowering would need to be refined; the speculative-operator slot would be enlarged.

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

For completeness — this is *not* a separate theme, but the natural fall-out of the `krylov-step` body's L4>L3 lowering. The L4 `iterate_while step carry₀` form lowers to a tail-recursive L3 loop:

```text
iterate_while_L3 step (carry, sim) =
  let (carry', sim', readout, continue) = step (carry, sim)
  in if continue then iterate_while_L3 step (carry', sim')
                 else (carry', sim', readout)
```

The tail-recursive shape is value-threaded; the monad has dissolved. The `sequential-obstruction` of the outer loop survives at L3 (per `cg.md:341-349`) — the L3 form names the loop tail-recursively but does not claim it lifts to a global tensor-field op. This is the expected outcome for Krylov methods at L3 per `sequential-obstruction.md`.

## Audit of cycle-002 identity-in-form claim

The open question `krylov-step-l3-identity-in-form-audit` (scaffolding/open-questions.md) records the combinator-miner cycle-002 assertion: "the L2→L3 rotation on the `krylov-step` body is identity-in-form, citing `cg.md:351-362` and `arnoldi_step.md:185-188`." (Note: the open-questions ledger records the citation as `cg.md:352-362`; the range that fully contains Claim 2 — including its `### Claim 2: step body lifts as identity` header at line 351 — is `cg.md:351-362`. This dispatch canonicalizes to the inclusive range.) This dispatch audits the assertion as the secondary half of its job.

**Audit verdict**: The cycle-002 assertion is **correct as stated** (about L2>L3), and remains correct for the body. The L4>L3 hop this dispatch addresses is a different rotation; the two compose to give the full L4>L2 chain.

**Evidence reviewed**:

1. `cg.md:341-362` (cited by combinator-miner; re-read for this audit) — the L2→L3 rotation claims for CG. Claim 2 ("step body lifts as identity") states verbatim: *"The L2→L3 rotation on the step body is therefore the **identity in form**: no unfolding, no global lift, no schema change."* The justification is that L2's primitive vocabulary (`apply_linop`, `axpy`, `axpby`, `dot`, scalar arithmetic) is already L3-native — each is a whole-tensor operation with no element loop exposed at L2. **Audit finding**: the assertion is well-supported; the L2 primitives are L3-native by inspection of their signatures (e.g., `apply_linop : LinOp -> Tensor[N] -> Tensor[N]` is a global field operation).

2. `arnoldi_step.md:178-213` (cited by combinator-miner; re-read for this audit) — the L2→L3 rotation for the Arnoldi step. The three uncontested primitives (`apply_BA`, `subdiag_norm`, `normalize`) are listed as L3-trivial (identity lifts). The fourth (`orthogonalize` under MGS) carries a sequential obstruction — but this is at the *primitive* level, inside `op.orthog`, not at the `krylov-step` body level. **Audit finding**: the obstruction is correctly localised to the orthog primitive; the `krylov-step` body around `op.orthog` is still identity-in-form (it calls `op.orthog` as an opaque operator).

3. The L4 form's body (from `L4/krylov-step` §Semantics, reproduced in §"L4 form (LHS)" above). Each line of the body is a binding of an L1 primitive (`apply_linop`, `axpy` / `axpby` / `axpbypcz`, `dot`, `nrm2`, `scal`) to a `let`-bound variable, plus the optional `op.orthog` / `op.scalars` call and the `derived_views` readout. **Audit finding**: every primitive call survives L4>L3 textually unchanged (modulo the wrapper dissolution discussed in §"L3 form" above). The body is identity-in-form between the L4 body and the L3 body for the same reason the L2 body is identity-in-form on the way to L3 — the primitives are L3-native.

**Audit verdict — confirmed-with-refinement**: the cycle-002 framing was "L2>L3 step-body lift is identity-in-form". This dispatch sharpens to: "**L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence**; the L4>L3 hop is non-identity *at the wrapper level* (records dissolve, monad dissolves, readonly typing demotes, Form A/B presentation collapses), but the body's dataflow chain survives both hops textually unchanged." This refinement is more precise but does not contradict the original claim. The original framing was correct for the question it asked (about the body); this dispatch answers the broader question (about the wrapper).

**Consequence for L3 dep-map**: per the harvester's "Lowers to" section and per this audit, **no L3 `krylov-step` row is proposed**. The L4 entry lowers transitively to the L2 entry via this theme (L4>L3 wrapper dissolution) plus a one-line L3>L2 theme (identity-in-form on the body). The L4>L3 lowering produces an L3 form, but that L3 form is value-thread-isomorphic to the L2 form; there is no operational difference between "L3 `krylov-step`" and "L2 `krylov-step` with an outer `iterate_while` tail-recursion" — they are the same thing under two layer labels. Promoting an L3 row would duplicate content without adding semantic distinction.

**Open question disposition**: this dispatch *audits* the cycle-005 open question `krylov-step-l3-identity-in-form-audit` and proposes closing it as **confirmed-with-refinement** — the assertion holds, the framing is sharpened, no L3 row needed. Integrator will mark accordingly; if integration uncovers a non-identity finding (e.g., a corpus check on a slice this dispatch did not re-verify reveals body-level rotation), the question stays open and a cycle-007 L3 row promotion follows.

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
- `book/src/concepts/derived-view-hoisting.md` — the demand-pruning algebra preserved across the rotation.

## Status

`rough-in` — the theme's rewrite shape is sketched against the cycle-006 wave-1 firm L4 entry; the L3 form is the value-threaded dissolution of the L4 wrapper; the audit of the cycle-002 identity-in-form claim is included; the speculative `iterate_while` / `iterate_while_with_prev` L4 operators are flagged for harvester promotion. The theme is **non-blocking on L4 vocab promotion**: even with `iterate_while` unanchored, the L4>L3 rewrite on the `krylov-step` body itself is fully specified; the unanchored combinator is the *consumer*, not the rewrite target. **Lowering-verifier follow-up** (cycle-007 candidate) should confirm that the value-threaded L3 form produced by applying this theme to `L4/krylov-step` is textually equivalent to `L2/krylov-step` §Semantics body modulo the L3-level outer-loop tail-recursion wrapping. If the verifier finds a mismatch (e.g., a primitive call shape that does not survive the rewrite), the theme is refined.
```

### L4 dep-map rough-in entries (for `book/src/L4/index.md`)

Append to the operator dep-map under the L4 layer (which post-wave-1 harvester now contains the firm `krylov-step` row):

```markdown
| [`iterate_while`](./iterate_while.md) | `Step -> carry -> Solve Trajectory` where `Step = carry -> Solve { carry', readout, continue }`. Tail-recursive value-threading loop combinator that folds `Step` over an initial `carry`, threading through `SimState` (via the `Solve` monad) and accumulating readouts subject to demand-pruning. | Concepts: `solve-monad`, `derived-view-hoisting`, `convergence-test`. Consumer of L4 `krylov-step` (via the body). | `rough-in` (proposed-by: abstractor:2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering; flagged also by harvester:2026-05-27T080944Z-harvester-krylov-step-L4 caveat 2) |
| [`iterate_while_with_prev`](./iterate_while_with_prev.md) | `(PrevCarry -> Step) -> PrevCarry -> Step -> carry -> Solve Trajectory`. Variant of `iterate_while` that supplies a `PrevCarry` closure parameter to the `Step`, with a bootstrapping step producing the initial `PrevCarry`. Used by Form B of [`krylov-step`](./krylov-step.md) per `first-iteration-unrolling`. Degenerates to `iterate_while` when `PrevCarry = ()`. | Concepts: `first-iteration-unrolling`, `solve-monad`. Consumer of L4 `krylov-step` Form B. | `rough-in` (proposed-by: abstractor:2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering; flagged also by harvester:2026-05-27T080944Z-harvester-krylov-step-L4 caveat 2) |
```

(The integrator will inject these rows below the wave-1 `krylov-step` firm row in the same table; SUMMARY chapter entries are NOT proposed for these — they remain rough-in placeholders until harvester promotes.)

## Speculative operators proposed

- **`iterate_while`** — L4 loop combinator. Signature `Step -> carry -> Solve Trajectory` where `Step = carry -> Solve { carry', readout, continue }`. Tail-recursive value-threading loop that folds `Step` over an initial carry, threading `SimState` via the `Solve` monad and accumulating readouts subject to demand-pruning. **Motivation**: the L4 `krylov-step` body is consumed by an outer loop that `solve-monad.md` references informally as `inner_loop` without naming the combinator. This theme's L4 form refers to that combinator as `iterate_while`; the L3 form makes the tail-recursive shape explicit, which is the natural anchor for the speculative L4 operator. Harvester promotes when it formalises the L4 loop-combinator family (likely cycle-007).

- **`iterate_while_with_prev`** — L4 loop combinator variant. Signature `(PrevCarry -> Step) -> PrevCarry -> Step -> carry -> Solve Trajectory`. Used by Form B of `krylov-step` (first-iteration-unrolling) where a `PrevCarry` value (e.g., CG's `β_prev`) is threaded as a closure parameter of the loop rather than a state field. **Motivation**: the harvester output's Form B signatures (`first_step` and `steady_step`) imply the existence of `iterate_while_with_prev` as the consuming combinator (per `cg.md:393-425` v0.5); the combinator has no L4 anchor either. Sibling to `iterate_while`; harvested together when the L4 loop-combinator family is formalised. Degenerates to `iterate_while` when `PrevCarry = ()` (a unit-typed carry contributes no information).

Both rough-ins explicitly named, with intended signatures and motivation sketched. Promotion to firm L4 vocabulary is the harvester's job, not this dispatch's.

## Supporting evidence

The cycle-002 identity-in-form claim is independently audited against `cg.md:341-362` and `arnoldi_step.md:178-213` (re-read for this dispatch; assertion confirmed and sharpened). The L4 wrapper machinery is identified by reading the wave-1 harvester output's §Signature, §Semantics, and §"L4 vs L2 distinction" sections (all three contribute to the four-part wrapper inventory). The L3 form's value-threading shape is the standard de-monadised tail-recursive form for a `StateT s Identity a` action, applied mechanically (per the `StateT` evaluation rules). The cycle-005 cross-layer-cross-cutter's recommended L4>L3>L2 chain structure is honoured: this theme is the L4>L3 hop; the L3>L2 hop is the identity-in-form body rewrite (deferred to a separate one-line theme, not this dispatch). The harvester's "Lowers to" claim (the chain is L4>L3>L2 with no L3 row) is upheld by the audit; this dispatch produces the L4>L3 theme content but explicitly does NOT propose an L3 `krylov-step` row.

The `iterate_while` and `iterate_while_with_prev` speculative operators are re-flagging of the harvester's caveat 2 (the `iterate_while` is unanchored open question). This dispatch is not introducing fresh speculative operators — the harvester output already flagged the gap; this theme makes the gap structural by writing it into the L4 dep-map as a rough-in row that the L4>L3 lowering depends on. Promotion to firm L4 vocabulary is the right cycle-007 follow-up.

The placement-discipline preservation (the L4 form's effect-localisation — kernel writes only `SimState.it`, reads `Krylov` and `OpParams`, with the iterate update happening at restart boundaries) carries through to L3 by inspection: the explicit record update `s' = s { it = s.it + 1 }` is the only `SimState` field touched in the body; `K'` is a fresh value; `op` is closure-captured. The L3 form preserves the L4 discipline without enforcement — the `readonly` typing demotes to a comment, but the body's textual shape makes the discipline visible.

### Skills applicable to this dispatch

The following skills under `skills/` apply directly to the rotation-proposal and citation-audit work performed here. They were followed by hand without explicit invocation; surfaced for skill-uptake telemetry per the critic's checklist.

- `skills/propose-rotation/` — the four-part wrapper-dissolution rewrite (L4 LHS → L3 RHS with justification kind, applicability conditions, and what-does-not-change) follows the propose-rotation shape.
- `skills/verify-rotation-citation/` — the audit of the cycle-002 identity-in-form assertion (re-reading `cg.md:341-362` and `arnoldi_step.md:178-213`, locating Claim 2 verbatim, confirming with refinement) follows the verify-rotation-citation shape.
- `skills/verify-citation-range/` — citation ranges were verified by re-reading source. The `cg.md:351-362` canonicalization (vs. the open-question ledger's `:352-362`) is the kind of range-boundary fix this skill targets.

## Open questions / caveats

1. **Audit outcome surfaced** (per planner caveat 2): The combinator-miner cycle-002 identity-in-form claim is **confirmed-with-refinement** — confirmed at L3>L2 on the body, refined to "non-identity at wrapper level, identity-in-form on body" for the full L4>L2 chain. No L3 `krylov-step` row is proposed. The cycle-005 open question `krylov-step-l3-identity-in-form-audit` should be marked **confirmed-with-refinement** by the integrator (or the next meta-phase). **For cycle-007 planner**: no L3 promotion needed; the L4 entry transitively lowers to L2 via this theme + a one-line L3>L2 body-identity theme.

2. **L4 layer dep-map dependency**: this theme depends on `L4/krylov-step` being firm (wave-1 harvester output, this cycle), and on the dep-map's `iterate_while` / `iterate_while_with_prev` rough-in rows being present. Integration order: the per-report integrator should apply the wave-1 harvester report **before** this report, so that the L4 dep-map already has the firm `krylov-step` row when this report's rough-in rows are appended. If integration applies this report first, the L4 dep-map will have rough-in rows referring to a firm `krylov-step` row that doesn't yet exist (link-rot for one integration step); not blocking but worth noting. **Disposition**: the staging-log's per-report ordering should put harvester before abstractor; if not enforced, the integrator-finalize's book-build will surface broken links and the integrator can swap the order. **No action needed from the abstractor — flagging for the integrator-per-report dispatch.**

3. **L3 layer dep-map untouched**: this dispatch explicitly does NOT propose an L3 row. The L3 layer dep-map (`book/src/L3/index.md`) remains empty post-this-cycle. If the cycle-005 open question is marked confirmed-with-refinement (per (1) above), the L3 dep-map's eventual first entry will be a *different* operator — the lowering of an L4 form that *does* carry a substantive body rotation (e.g., the future `apply_BA` lowering, or a tensor-field lift for a smoother), not `krylov-step`. **For cycle-007 planner**: L3 layer-intro-author refresh is **not** triggered by this dispatch; it remains a future task when an L3 entry actually arrives.

4. **`iterate_while` / `iterate_while_with_prev` promotion-blocker**: the cycle-005 open question `state-stratification-as-l4-concept-or-l4-row` is the deeper convention question about whether L4 rows must depend on L4 rows (not concepts). If that convention is adopted, this theme's L4 form's reference to `iterate_while` is a dependency on a *rough-in* L4 operator, which may not satisfy the convention. **Disposition**: this theme is written defensively — the L4 form mentions `iterate_while` only as the consuming context, not as a primitive used by the rewrite. The rewrite itself acts on the `krylov-step` body and the wrapper machinery, not on the loop combinator. If the convention forbids depending on rough-ins, the theme's rough-in rows can stay flagged-but-unused until the harvester promotes them; the theme's rewrite is independent. **For cycle-007 planner**: the L4 loop-combinator harvest is unblocked by this dispatch (the speculative operators have a clear consumer context); the convention question is orthogonal.

5. **L3>L2 body-identity theme is implied but not authored here**: per the audit's verdict, the L4>L2 chain has an L4>L3 hop (this theme) plus an L3>L2 hop that is identity-in-form on the body. The L3>L2 hop has not been authored as a theme entry under `book/src/L3-L2/`. A future cycle-007 abstractor dispatch (low-cost; could be a single short theme `krylov-step-body-identity`) should land that. **Not in this dispatch's scope** (one theme per invocation). For cycle-007 planner: a sibling abstractor dispatch on the L3>L2 body-identity theme should be slotted alongside the `iterate_while` harvest.

6. **No problems/ filing.** Reviewed the dispatch surface for cross-role concerns (per `scaffolding/problems-sensitivity.md` target rate ~1/15 cycles); none rise to the bar. The audit-outcome surfacing (item 1) and the integration-order note (item 2) are scope-internal and routed through Open Questions / staging notes rather than problems/. The convention question (item 4) is already an open question (`state-stratification-as-l4-concept-or-l4-row`) and doesn't need a problems/ filing.

7. **No L0 citations.** As with the harvester output, this lowering is a methodology-level rotation between two methodology-level layers; no Palace source range "is" the L4>L3 transition. All evidence is at the spec / slice / concept level. The L0 evidence sits transitively through the L2 entry's citations (`iterative.cpp:244-250` for `CheckDot`, `test/unit/test-orthog.cpp:80-170, :234-280` for the orthog variant axis). Consistent with the discipline of upper-layer lowering themes.

8. **`iterate_while_L3` rendering drops trajectory accumulation — deferred to cycle-007 lowering-verifier or harvester** (added by repairer cycle-006 per critic finding 3). The §"What the L3 form for `iterate_while` looks like" rendering (the four-line tail-recursive value-threading sketch above) returns a single `readout` when `continue = false`, but the L4 `iterate_while` signature given in §"Speculative L4 operators" is `Step -> carry -> Solve Trajectory` with `Trajectory = [readout]` accumulated subject to demand-pruning. The L3 tail-recursive sketch as written is locally inconsistent with the L4 form's trajectory accumulation: either the L3 form should carry a `trajectory` accumulator pass-through (`[readout]` rather than a single `readout`), or the rotation should explicitly acknowledge a demand-pruning step that collapses the accumulator to a single readout when no downstream consumer reads the trajectory. Both are substantive rotation decisions that this repairer pass does not author. **Disposition**: defer to cycle-007 — the lowering-verifier dispatch follow-up already named in §Status should reconcile the L3 rendering with the L4 trajectory shape; alternatively, the cycle-007 harvester on the L4 loop-combinator family (named in caveat 4 above) should resolve as part of formalising `iterate_while`'s firm signature. Either path resolves the inconsistency. The four-part wrapper-dissolution theme for `krylov-step` itself (the primary content of this dispatch) is unaffected by this caveat — it is a sub-issue on the speculative L4 loop combinator's L3 shape, not on the `krylov-step` body's rotation.
