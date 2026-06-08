# iterate-while-dissolution

The L4>L3 lowering theme for the [`iterate-while`](../L4/iterate-while.md) combinator — the tail-recursive value-threading loop that every L4 iterative slice folds (CG, GMRES, Chebyshev, Arnoldi, transient stepping, eigenmode iteration). The theme dissolves the L4 wrapper machinery (the `Solve` monad, the row-polymorphic `{ state: α, ...e }` step return, the demand-prunable `trajectory` accumulator) into an explicit L3 tail-recursive value-threaded loop. It is the **dedicated home** for a rewrite that previously lived only as a sub-component of [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) §"What the L3 form for `iterate_while` looks like" (`krylov-step-typed-wrapper-dissolution.md:158-200`); both firm L4 caps — [`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) — point their §"Lowers to" at that buried sub-component, so this chapter gives the combinator's own dissolution a layer-coherent L4>L3 anchor.

## Slug

`iterate-while-dissolution`

## Context

[`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) are firm L4 rows. The combinator's L4>L3 lowering also appears as a sub-component of the krylov-step theme, sub-ordinate to the krylov-step body rewrite (`krylov-step-typed-wrapper-dissolution.md:158-200`) — but that is **not the combinator's home**. The firm `iterate-while` row's §"Lowers to" and its §"L4 vs L3 distinction" both point here. This chapter is the standalone theme: the two L3 forms, the §3.8 collapse rule, and the identity-in-form-on-body verdict, with the layer-coherent framing — narrating the combinator's own L4→L3 dissolution forward and splitting the ground (unpruned) form from its pruned image.

This theme parallels [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) and [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) in shape — both of those are *slice-specialised* `iterate_while` dissolutions (GMRES / FGMRES inner loops with a witness-into-carry hoist). This theme is the **generic** dissolution those two specialise; where they pin the trajectory to `[]` under their specific GMRES consumer pattern, this theme carries both the generic trajectory-keeping form and its pruned image, and the slice themes are recovered by instantiating the consumer-demand condition.

## L4 form (LHS)

The L4 `iterate_while` Form A — the extras-carrying, `Solve`-threaded form consumed by [`krylov-step`](../L4/krylov-step.md) Form A (`iterate-while.md:35-43`). This is the firm L4 row's signature:

    iterate_while
      :: α
      -> (α -> Bool)
      -> (α -> Solve { state: α, ...e })
      -> Solve { final_state: α, trajectory: [{ ...e }] }

The small-step semantics are the strawman §3.7 rule, reproduced verbatim in the firm L4 row's §Semantics (`iterate-while.md:64-74`, transcribing `book/src/semantics/index.md:164-171`):

$$
\begin{aligned}
\textsf{iterate\_while}\ a\ p\ f &\;\to\; \textsf{if}\ p(a) \\
&\quad \textsf{then}\ \textsf{let}\ \{\textsf{state}: a',\ \dots e\} = f(a)\ \textsf{in} \\
&\quad\quad \textsf{let}\ \{\textsf{final\_state},\ \textsf{trajectory}\} = \textsf{iterate\_while}\ a'\ p\ f\ \textsf{in} \\
&\quad\quad \{\textsf{final\_state},\ \textsf{trajectory}: [\{\dots e\}] \mathop{++} \textsf{trajectory}\} \\
&\quad \textsf{else}\ \{\textsf{final\_state}: a,\ \textsf{trajectory}: [\,]\,\}
\end{aligned}
$$

The load-bearing L4 property the lowering must transport is **Law 1 — demand-driven trajectory pruning** (`iterate-while.md:123-133`, inherited from `book/src/semantics/index.md:186-213` and [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)): when a consumer observes only the `final_state` field of the result, the §3.8 rule rewrites the body `f` to the subgraph computing only the `state` field, omitting the extras computation. The L4 form is **one** combinator definition; Law 1 is the rewrite that specializes it to "residuals-on" vs "residuals-off" by consumer demand, with no runtime flag.

The wrapper machinery this theme dissolves is three pieces:

1. **The `Solve` monad** — `Solve = StateT SimState Identity` (`book/src/concepts/solve-monad.md:1-68`). The `Solve { final_state, trajectory }` return and the body's `Solve { state, ...e }` action carry the `SimState` (the `it` counter, written by the body's `modify`) monadically.
2. **The row-polymorphic step return `{ state: α, ...e }`** — a TypeScript-style record with a generic extras spread `...e`. L3 has no row-polymorphic record spread.
3. **The demand-prunable `trajectory: [{ ...e }]` accumulator** — the syntactic site where Law 1 fires.

## L3 form (RHS)

The L4>L3 dissolution produces a **tail-recursive value-threaded loop** with the `Solve` monad dissolved to an explicit positional `sim` thread and the record-spread step return dissolved to a positional tuple. Two L3 forms arise from the **same** L4 invocation under different consumer demands; both are extracted verbatim from `krylov-step-typed-wrapper-dissolution.md:164-184`.

### Unpruned form — the trajectory-keeping ground form

The direct value-threaded dissolution of the L4 form when a downstream consumer reads `.trajectory` (no §3.8 collapse fires; the `[readout]` accumulator the firm L4 Law 1 keeps is materialized at L3). This is the **ground form** — the faithful L3 image of the §3.7 small-step rule with the trajectory preserved (`krylov-step-typed-wrapper-dissolution.md:164-171`):

    iterate_while_L3 step carry₀ sim₀ =
      let go (carry, sim, traj) =
            if not (p carry)
              then (carry, sim, reverse traj)         -- final_state, sim', trajectory
              else let (carry', sim', readout) = step (carry, sim)
                   in go (carry', sim', readout : traj)
      in go (carry₀, sim₀, [])

The `traj` accumulator is consed in reverse (each step prepends) and `reverse`d at termination, recovering the §3.7 rule's iteration-order `[{...e}] ++ trajectory` left-bias as an `O(N)` accumulator pass. The `sim` is threaded positionally — the `Solve` monad has dissolved (per the §"Concept-page references" `solve-monad.md` entry of the parent theme), so `SimState` rides as an explicit positional argument rather than monadically. The `readout` is the positional image of the row-polymorphic `{ ...e }` extras record. This form is the L3-side image of the L4 `iterate_while` *without* the §3.8 pruning applied — it keeps the trajectory because the consumer demands it.

### Pruned form — the §3.8 collapse-rule image

The §3.8-collapsed shape that arises when the consumer observes only `final_state`-equivalent quantities. **This form drops the accumulator BY §3.8 demand-pruning (Law 1's collapse rule), NOT against Law 1** — the pruned form is the *image* of the collapse rule applied to the unpruned ground form, so it is fully consistent with the firm L4 Law 1 that keeps the trajectory. Law 1 *is* the rule that licenses dropping it when unobserved (`krylov-step-typed-wrapper-dissolution.md:176-184`):

    iterate_while_L3_pruned step carry₀ sim₀ =
      let go (carry, sim) =
            if not (p carry)
              then (carry, sim)                       -- final_state, sim'
              else let (carry', sim') = step_state (carry, sim)
                   in go (carry', sim')
      in go (carry₀, sim₀)

where `step_state = λ(carry, sim) -> let (carry', sim', _readout) = step (carry, sim) in (carry', sim')` is the §3.8-pruned subgraph of `step` that computes only the next carry (the extras computation is eliminated as dead code **at the call site**, not merely unused at runtime). The L3-side `step_state` has shape `(carry, sim) -> (carry', sim')` — the positional-tuple image of the L4-side `f_state : α -> α` of Law 1 (`iterate-while.md:123-133`), with the `sim` thread surfacing positionally because the `Solve` monad has dissolved; the L4 `α` collapses to the L3 carry alone, with `sim` carried alongside positionally rather than monadically.

### The collapse rule

The L4>L3 collapse from the unpruned ground form to the pruned form is governed by the L3-side image of Law 1 (`krylov-step-typed-wrapper-dissolution.md:188-198`):

$$
\frac{
  \text{only } \textsf{final\_state} \text{ of the L3 result is observed downstream}
}{
  \textsf{iterate\_while\_L3}\ p\ \textsf{step}\ \textsf{carry}_0\ \textsf{sim}_0 \;\equiv\; \textsf{iterate\_while\_L3\_pruned}\ p\ \textsf{step}_{\textsf{state}}\ \textsf{carry}_0\ \textsf{sim}_0
}
$$

This is exactly the L3-side image of **Law 1** of [`iterate-while`](../L4/iterate-while.md) (`iterate-while.md:123-133`) — the L4 demand-pruning law **transports through** the L4>L3 wrapper dissolution because the dissolution is value-thread-isomorphic on the body (the parent theme's §"Audit of cycle-002 identity-in-form claim", `krylov-step-typed-wrapper-dissolution.md:202-213`, establishes the body-identity that licenses the transport). The unpruned `iterate_while_L3` is the ground form; the pruned `iterate_while_L3_pruned` is its collapse-rule image; the rule above is the rewrite between them. **Framing**: the pruned form is NOT a contradiction of the firm L4 Law 1 (which keeps the trajectory in its general statement) — it is the *consequence* of Law 1's collapse rule fired under a `final_state`-only consumer.

### `iterate_while_pure` — the no-extras sugar

For the no-extras case (`e = ()`, the LBM step at `book/src/semantics/index.md:374-386`), the L4 sugar `iterate_while_pure` (`iterate-while.md:92-98`) lowers to the textbook tail-recursive loop with no accumulator (`iterate-while.md:190-195`):

    iterate_while_pure_L3 :: α -> (α -> Bool) -> (α -> α) -> α
    iterate_while_pure_L3 a p f = if p a then iterate_while_pure_L3 (f a) p f else a

This is the degenerate case of the pruned form where `e = ()` makes the extras-pruning trivial (the trajectory is uniformly `[]`); the `sim` thread is also absent when the step is non-monadic. It is identity-in-form on the body (no primitive substitution), per the same assertion that backs the krylov-step L3>L2 identity.

### What does NOT change in the rotation

The body's primitive sequence survives the rotation textually unchanged — the dissolution is **identity-in-form on the body** (`krylov-step-typed-wrapper-dissolution.md:202-213`). The rotation touches only the **wrapper**: the `Solve` monad becomes positional `sim`, the record-spread step return becomes a positional tuple, the trajectory becomes either an explicit list accumulator (unpruned) or nothing (pruned). The `step` itself — whatever the slice's per-step kernel is — passes through unchanged in its dataflow position.

The **outer-loop `sequential-obstruction`** survives at L3: both L3 forms name the loop tail-recursively but do **not** claim it lifts to a global tensor-field op. This is the expected outcome for Krylov-family iterations at L3 per [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the live anchor is `arnoldi_step.md:194-213`; the CG sequential-obstruction evidence is homed in the firm L3 entry [`L3/krylov-step`](../L3/krylov-step.md) §Algebraic-laws non-lift catalogue. The unpruned form additionally allocates the `O(N)` trajectory accumulator; the pruned form does not.

### What this lowering does NOT cover

- **The L3>L2 hop on the loop combinator itself**, which is *also* identity-in-form (the same tail-recursive shape is L2-native), so the full L4>L3>L2 chain for `iterate_while_pure` collapses to the L4>L3 wrapper dissolution alone (`iterate-while.md:196-197`). The L3>L2 completion is the trivial identity step, not duplicated here.
- **The `iterate-while-with-prev` bootstrap dissolution** — the [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) variant carries an additional closure-threaded `PrevCarry` (the bootstrap step's output). Its L4>L3 dissolution is this theme's pattern *plus* the additional `prev` positional dissolution (the bootstrap step becomes a non-recursive first call producing the initial `PrevCarry`, then the steady step recurses). The `_with_prev` cap's §"Lowers to" points here for the shared wrapper dissolution; the `prev`-positional addition is the only delta and is noted, not given a separate theme (it degenerates to this theme when `PrevCarry = ()`, per `iterate-while-with-prev.md` Law 1).
- **The slice-specialised dissolutions** — [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) and [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) specialise this generic dissolution with a witness-into-carry hoist and a pinned `[]` trajectory (the GMRES consumer reads only `final_state`-equivalent quantities). They are recovered by instantiating the pruned form's consumer-demand condition; they are not re-derived here.

## Applicability conditions

The rewrite is valid when all four of the following hold (inherited from `krylov-step-typed-wrapper-dissolution.md` §"Applicability conditions"):

1. **The L4 `Solve` monad's effect domain is exactly `SimState`.** The only `modify` in the body is the `it` counter increment (or whatever single `SimState` field the slice threads); no carry field is monad-touched. This lets the monad dissolve to a single positional `sim` argument (`iterate-while.md:103`, `solve-monad.md` §"What stays out of the monad").

2. **The predicate is pure on the carry** (`p :: α -> Bool`, `iterate-while.md:102`). No reads of `SimState`, `OpParams`, or the per-step extras. This is what lets the L3 branch test `not (p carry)` read only the positional `carry` argument. Consumers whose termination needs `SimState.it` fold `it` into the carry (the CG v0.5 predicate `\(s, _) -> s.it < config.max_it && not s.converged`, firm-homed at `book/src/L4/krylov-step.md` Form B).

3. **The body's primitive sequence is L3-native or carries its own L3 classification.** Each step-body primitive is either a whole-tensor global op (L3-native by signature) or carries a documented body-level obstruction (e.g. MGS orthogonalization). The wrapper dissolution does not change the body's L3 classification — it survives in form.

4. **Trajectory-pruning selection** (selects unpruned vs pruned form). When the downstream consumer reads `.trajectory` (or any per-step extras), the **unpruned** `iterate_while_L3` form is the rendered L3 shape. When the consumer observes only `final_state`-equivalent quantities, the **pruned** `iterate_while_L3_pruned` form is the rendered shape (per the collapse rule above). For Palace's actual KSP consumer surface (the four-scalar consumer at `reference/palace/palace/linalg/iterative.hpp:52-55`, consumed solely at `reference/palace/palace/linalg/ksp.cpp:296-310`), the pruned form is the rendered shape; for a monitoring consumer that reads the residual history, the unpruned form is rendered.

## Justification kind

**`structural`** with secondary **`reduction-chain`**.

- **Structural** (dominant): the L4 wrapper machinery (Solve monad, `iterate_while` combinator, extras-trajectory record, predicate-on-carry-only discipline) dissolves into an L3 tail-recursive value-threaded form; the body's primitive sequence is preserved by construction (every L4 primitive call becomes an L3 primitive call at the same dataflow position). The trajectory becomes an explicit accumulator (unpruned) or is dropped (pruned), both structural rewrites of the syntactic trajectory site.
- **Reduction-chain** (secondary): the `Solve` monad's `>>=` desugars to explicit positional `sim` threading (the `modify (\s -> s { it = s.it + 1 })` to let-bound `sim' = sim { it = sim.it + 1 }` step); the `iterate_while` small-step rule desugars to the tail-recursive `go` worker; the §3.8 pruning collapse from the unpruned to the pruned form is the mechanical application of Law 1's L3-side image.

**Abstraction-direction note**: L4 is the higher-abstraction layer (typed records, monadic effect, structural predicate-on-carry-only discipline, demand-prunable trajectory); L3 is the lower-abstraction layer (positional values threaded explicitly, branch-on-predicate in tail recursion, trajectory as explicit accumulator or dropped). The rotation direction is **L4 → L3**, narrated forward per the high→low discipline.

## Speculative L4 operators

None. This theme is an extraction of an already-firm sub-component; both L4 caps it lowers ([`iterate-while`](../L4/iterate-while.md), [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md)) are firm L4 rows. No new speculative operator is introduced.

## Verified-against

L4 source (the LHS of this rewrite):

- `book/src/L4/iterate-while.md:28-43` — the firm L4 `iterate_while` Form A signature (the LHS); `:64-74` the §3.7 small-step rule reproduced verbatim; `:123-133` Law 1 (demand-driven trajectory pruning, the load-bearing transported property); `:190-195` the `iterate_while_pure_L3` no-extras lowering; `:196-197` the L3>L2 identity-in-form note.
- `book/src/L4/iterate-while-with-prev.md` — the firm L4 sibling cap, whose §"Lowers to" also points at this dissolution (the `prev`-positional addition is the only delta).
- `book/src/semantics/index.md:150-184` — the strawman §3.7 `iterate_while` definition (v0.3 extras-carrying form + small-step rule at `:164-171` + `iterate_while_pure` sugar at `:178-182`).
- `book/src/semantics/index.md:186-213` — the strawman §3.8 demand-driven pruning rule that underwrites Law 1.

L3 source (the RHS of this rewrite; extracted from the firm sub-component):

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:164-171` — the unpruned `iterate_while_L3` trajectory-keeping ground form (extracted verbatim).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:176-184` — the pruned `iterate_while_L3_pruned` form (the §3.8 collapse-rule image, extracted verbatim).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:188-198` — the L3-side collapse rule (extracted verbatim).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:202-213` — the §"Audit of cycle-002 identity-in-form claim" verdict that establishes the body-identity licensing the Law-1 transport.
- `book/src/L3/krylov-step.md` — the firm L3 entry holding the CG non-lift catalogue (the `sequential-obstruction` evidence home).
- [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"MGS as sequential-obstruction" — the firm `sequential-obstruction` anchor for the outer loop surviving at L3.

L0 consumer-surface evidence (selects the pruned form for Palace's KSP case, Condition 4):

- `reference/palace/palace/linalg/iterative.hpp:52-55` — the four-scalar KSP consumer surface; `reference/palace/palace/linalg/ksp.cpp:296-310` — the sole consumption site reading only `final_state`-equivalent quantities, which fires the §3.8 collapse to the pruned form.

Concept-page references:

- [`solve-monad`](../concepts/solve-monad.md) — the `Solve = StateT SimState Identity` monad that dissolves to the positional `sim` thread.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra underwriting Law 1 and the collapse rule.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the outer loop's non-lift at L3.

## Status

`firm` — extraction of the sub-component (`krylov-step-typed-wrapper-dissolution.md:158-200`) into a dedicated layer-coherent chapter. Both L4 caps it lowers are firm L4 rows; the two L3 forms, the §3.8 collapse rule, and the identity-in-form-on-body verdict are cited against the strawman §3.7/§3.8, the firm L4 Law 1, and the parent theme's body-identity audit. Justification is `structural` + secondary `reduction-chain`. The trajectory-keeping unpruned `iterate_while_L3` is the form the firm L4 Law 1 keeps; the krylov-step sub-component's trajectory-drop is the pruned image, not a gap in the firm L4 form.

## L4 vs L3 distinction

- **L4**: a single combinator with structural demand-pruning of the trajectory; the body's `Solve`-monad effect is orthogonal to the value-threaded carry; the predicate is purely on the carry; the trajectory is materialised exactly when a downstream consumer reads it.
- **L3**: a tail-recursive loop with explicit `sim`-positional threading; the §3.8 pruning becomes a *call-site choice* between the unpruned `iterate_while_L3` (trajectory materialised as an explicit accumulator) and the pruned `iterate_while_L3_pruned` (trajectory dropped, `step` rendered in its `state`-only subgraph). The L3 forms do not carry the pruning *rule*; they carry its *resolved result* per consumer.

The two layers share signature shape (modulo wrapper dissolution) and small-step semantics on the body; they differ in **effect threading and demand-pruning placement**. The rotation erases the monadic packaging and resolves the demand-pruning per consumer, narrated forward L4→L3.
