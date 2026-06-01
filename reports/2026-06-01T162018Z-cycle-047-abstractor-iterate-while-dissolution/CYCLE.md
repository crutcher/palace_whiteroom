---
agent: abstractor
invoked_at: 2026-06-01T162018Z
scope: L4>L3 theme sketch — iterate-while-dissolution (extraction + re-homing of a buried sub-component into a dedicated layer-coherent chapter)
status: integrated
integrated_at: 2026-06-01T171229Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (D1; cycle-047). NEW firm L4>L3 theme book/src/L4-L3/iterate-while-dissolution.md (the no-prev standalone dissolution; R1 lead pick of the c046 L4-frontier survey) + 3 re-anchors (L4/iterate-while.md ×2 §Lowers-to + §L4-vs-L3-distinction, L4/index.md:54 dep-map cell) + L4-L3/index row + SUMMARY line. L4>L3 firm 3->5 (with D2). Closes iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor + iterate-while-l3-rendering-trajectory-accumulation-gap (recommendations; meta-phase authority). Build clean, linkcheck2 green."
inputs:
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:158-200 (the buried sub-component being extracted)
  - book/src/L4/iterate-while.md (firm L4 LHS cap; §Semantics, Law 1, §"Lowers to", §"L4 vs L3 distinction", dep-map deferral)
  - book/src/L4/iterate-while-with-prev.md (firm L4 sibling cap; the second pointer at the buried sub-component)
  - book/src/L4/index.md:54 (dep-map cell carrying the "standalone theme pending" note)
  - book/src/design/l4_calculus.md:150-228 (§3.7 iterate_while small-step rule + §3.8 demand-pruning; Law 1's strawman source)
  - book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md (sibling L4-L3 theme; structure/altitude reference)
  - book/src/L4-L3/index.md (themes-table for own-row registration)
  - book/src/SUMMARY.md:13-17 (L4>L3 Part for own-line registration)
---

# CYCLE: L4>L3 theme sketch — iterate-while-dissolution

## Summary

This dispatch extracts the L4>L3 dissolution of the `iterate_while` combinator into a dedicated, layer-coherent chapter `book/src/L4-L3/iterate-while-dissolution.md`. The body content already exists firm as a buried sub-component of `krylov-step-typed-wrapper-dissolution.md:158-200` (§"What the L3 form for `iterate_while` looks like"), where it is sub-ordinate to the krylov-step rewrite rather than home for the two firm L4 caps (`iterate-while`, `iterate-while-with-prev`) that both point at it. The standalone theme is genuinely unauthored: the firm L4 `iterate-while` row's §"Lowers to" defers to that buried sub-component and explicitly flags it drops the trajectory (OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`). The extracted theme captures **both** L3 forms from the same L4 invocation: the **trajectory-keeping unpruned form** (`iterate_while_L3`, `:164-171`) — the ground form that materializes the `[readout]` accumulator the firm L4 Law 1 keeps — and the **§3.8-pruned form** (`iterate_while_L3_pruned`, `:176-184`) which is the **collapse-rule image** (Law 1's L3-side demand-pruning rewrite, `:188-198`), NOT a contradiction of Law 1. The prose narrates forward L4→L3 per the high→low discipline: the LHS is the L4 `iterate_while` Form A, the RHS is the two L3 tail-recursive value-threaded forms, and the §3.8 pruning collapse is the rule that takes the unpruned ground form to the pruned form under a `final_state`-only consumer. The dispatch also re-anchors the two `iterate-while.md` deferrals (§"Lowers to" / §"L4 vs L3 distinction" prose + the `book/src/L4/index.md:54` dep-map cell) to cite this dedicated chapter, and registers the new theme into `L4-L3/index.md` (own row) and `SUMMARY.md` (own line). This is the route-b realization closing OQ `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor`.

## Proposed changes

```new:book/src/L4-L3/iterate-while-dissolution.md
# iterate-while-dissolution

The L4>L3 lowering theme for the [`iterate-while`](../L4/iterate-while.md) combinator — the tail-recursive value-threading loop that every L4 iterative slice folds (CG, GMRES, Chebyshev, Arnoldi, transient stepping, eigenmode iteration). The theme dissolves the L4 wrapper machinery (the `Solve` monad, the row-polymorphic `{ state: α, ...e }` step return, the demand-prunable `trajectory` accumulator) into an explicit L3 tail-recursive value-threaded loop. It is the **dedicated home** for a rewrite that previously lived only as a sub-component of [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) §"What the L3 form for `iterate_while` looks like" (`krylov-step-typed-wrapper-dissolution.md:158-200`); both firm L4 caps — [`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) — point their §"Lowers to" at that buried sub-component, so this chapter gives the combinator's own dissolution a layer-coherent L4>L3 anchor.

## Slug

`iterate-while-dissolution`

## Context

The cycle-007 harvester promoted [`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) to firm L4 rows (closing cycle-006 OQ `iterate-while-l4-anchor-missing`). The combinator's L4>L3 lowering was *described* — but only as a sub-component of the krylov-step theme, where it is sub-ordinate to the krylov-step body rewrite (`krylov-step-typed-wrapper-dissolution.md:158-200`). That sub-component is firm in content (its two L3 forms are exhaustively cited against the strawman §3.7/§3.8 and the firm L4 Law 1), but it is **not the combinator's home**: a reader navigating from the firm `iterate-while` row's §"Lowers to" lands in the middle of the krylov-step theme rather than at a chapter for the combinator itself. The firm `iterate-while` row's §"Lowers to" (`iterate-while.md:182-188`) and its §"L4 vs L3 distinction" (`iterate-while.md:218`) both defer to "the standalone L4>L3 theme pending"; the L4 dep-map cell (`book/src/L4/index.md:54`) carries the same pending note. This chapter is that standalone theme.

This is an **extraction + re-homing**, not a fresh derivation. The two L3 forms, the §3.8 collapse rule, and the identity-in-form-on-body verdict are lifted verbatim (with citations) from the firm sub-component; the new content is the layer-coherent framing — narrating the combinator's own L4→L3 dissolution forward, splitting the ground (unpruned) form from its pruned image cleanly, and reconciling the cycle-006 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` (the original krylov-step sub-component's prose at `krylov-step-typed-wrapper-dissolution.md:188` notes the existing theme *had* dropped the trajectory; the trajectory-keeping unpruned form here is the reconciliation).

This theme parallels [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) and [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) in shape — both of those are *slice-specialised* `iterate_while` dissolutions (GMRES / FGMRES inner loops with a witness-into-carry hoist). This theme is the **generic** dissolution those two specialise; where they pin the trajectory to `[]` under their specific GMRES consumer pattern, this theme carries both the generic trajectory-keeping form and its pruned image, and the slice themes are recovered by instantiating the consumer-demand condition.

## L4 form (LHS)

The L4 `iterate_while` Form A — the extras-carrying, `Solve`-threaded form consumed by [`krylov-step`](../L4/krylov-step.md) Form A (`iterate-while.md:35-43`). This is the firm L4 row's signature:

    iterate_while
      :: α
      -> (α -> Bool)
      -> (α -> Solve { state: α, ...e })
      -> Solve { final_state: α, trajectory: [{ ...e }] }

The small-step semantics are the strawman §3.7 rule, reproduced verbatim in the firm L4 row's §Semantics (`iterate-while.md:64-74`, transcribing `book/src/design/l4_calculus.md:164-171`):

$$
\begin{aligned}
\textsf{iterate\_while}\ a\ p\ f &\;\to\; \textsf{if}\ p(a) \\
&\quad \textsf{then}\ \textsf{let}\ \{\textsf{state}: a',\ \dots e\} = f(a)\ \textsf{in} \\
&\quad\quad \textsf{let}\ \{\textsf{final\_state},\ \textsf{trajectory}\} = \textsf{iterate\_while}\ a'\ p\ f\ \textsf{in} \\
&\quad\quad \{\textsf{final\_state},\ \textsf{trajectory}: [\{\dots e\}] \mathop{++} \textsf{trajectory}\} \\
&\quad \textsf{else}\ \{\textsf{final\_state}: a,\ \textsf{trajectory}: [\,]\,\}
\end{aligned}
$$

The load-bearing L4 property the lowering must transport is **Law 1 — demand-driven trajectory pruning** (`iterate-while.md:123-133`, inherited from `book/src/design/l4_calculus.md:186-213` and [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)): when a consumer observes only the `final_state` field of the result, the §3.8 rule rewrites the body `f` to the subgraph computing only the `state` field, omitting the extras computation. The L4 form is **one** combinator definition; Law 1 is the rewrite that specializes it to "residuals-on" vs "residuals-off" by consumer demand, with no runtime flag.

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

For the no-extras case (`e = ()`, the LBM step at `book/src/design/l4_calculus.md:374-386`), the L4 sugar `iterate_while_pure` (`iterate-while.md:92-98`) lowers to the textbook tail-recursive loop with no accumulator (`iterate-while.md:190-195`):

    iterate_while_pure_L3 :: α -> (α -> Bool) -> (α -> α) -> α
    iterate_while_pure_L3 a p f = if p a then iterate_while_pure_L3 (f a) p f else a

This is the degenerate case of the pruned form where `e = ()` makes the extras-pruning trivial (the trajectory is uniformly `[]`); the `sim` thread is also absent when the step is non-monadic. It is identity-in-form on the body (no primitive substitution), per the same combinator-miner cycle-002 assertion that backs the krylov-step L3>L2 identity.

### What does NOT change in the rotation

The body's primitive sequence survives the rotation textually unchanged — the dissolution is **identity-in-form on the body** (`krylov-step-typed-wrapper-dissolution.md:202-213`). The rotation touches only the **wrapper**: the `Solve` monad becomes positional `sim`, the record-spread step return becomes a positional tuple, the trajectory becomes either an explicit list accumulator (unpruned) or nothing (pruned). The `step` itself — whatever the slice's per-step kernel is — passes through unchanged in its dataflow position.

The **outer-loop `sequential-obstruction`** survives at L3: both L3 forms name the loop tail-recursively but do **not** claim it lifts to a global tensor-field op. This is the expected outcome for Krylov-family iterations at L3 per [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the live anchor is `arnoldi_step.md:194-213` (the original CG sequential-obstruction evidence has been lifted into the firm L3 entry [`L3/krylov-step`](../L3/krylov-step.md) §Algebraic-laws non-lift catalogue per the cycle-009 corpus reduction). The unpruned form additionally allocates the `O(N)` trajectory accumulator; the pruned form does not.

### What this lowering does NOT cover

- **The L3>L2 hop on the loop combinator itself**, which is *also* identity-in-form (the same tail-recursive shape is L2-native), so the full L4>L3>L2 chain for `iterate_while_pure` collapses to the L4>L3 wrapper dissolution alone (`iterate-while.md:196-197`). The L3>L2 completion is the trivial identity step, not duplicated here.
- **The `iterate-while-with-prev` bootstrap dissolution** — the [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) variant carries an additional closure-threaded `PrevCarry` (the bootstrap step's output). Its L4>L3 dissolution is this theme's pattern *plus* the additional `prev` positional dissolution (the bootstrap step becomes a non-recursive first call producing the initial `PrevCarry`, then the steady step recurses). The `_with_prev` cap's §"Lowers to" points here for the shared wrapper dissolution; the `prev`-positional addition is the only delta and is noted, not given a separate theme (it degenerates to this theme when `PrevCarry = ()`, per `iterate-while-with-prev.md` Law 1).
- **The slice-specialised dissolutions** — [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) and [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) specialise this generic dissolution with a witness-into-carry hoist and a pinned `[]` trajectory (the GMRES consumer reads only `final_state`-equivalent quantities). They are recovered by instantiating the pruned form's consumer-demand condition; they are not re-derived here.

## Applicability conditions

The rewrite is valid when all four of the following hold (inherited from `krylov-step-typed-wrapper-dissolution.md` §"Applicability conditions"):

1. **The L4 `Solve` monad's effect domain is exactly `SimState`.** The only `modify` in the body is the `it` counter increment (or whatever single `SimState` field the slice threads); no carry field is monad-touched. This lets the monad dissolve to a single positional `sim` argument (`iterate-while.md:103`, `solve-monad.md` §"What stays out of the monad").

2. **The predicate is pure on the carry** (`p :: α -> Bool`, `iterate-while.md:102`). No reads of `SimState`, `OpParams`, or the per-step extras. This is what lets the L3 branch test `not (p carry)` read only the positional `carry` argument. Slices whose termination needs `SimState.it` fold `it` into the carry (`book/src/spec/slices/cg.md:101` — the v0.5 predicate `\(s, _) -> s.it < config.max_it && not s.converged`).

3. **The body's primitive sequence is L3-native or carries its own L3 classification.** Each step-body primitive is either a whole-tensor global op (L3-native by signature) or carries a documented body-level obstruction (e.g. MGS orthogonalization). The wrapper dissolution does not change the body's L3 classification — it survives in form.

4. **Trajectory-pruning selection** (selects unpruned vs pruned form). When the downstream consumer reads `.trajectory` (or any per-step extras), the **unpruned** `iterate_while_L3` form is the rendered L3 shape. When the consumer observes only `final_state`-equivalent quantities, the **pruned** `iterate_while_L3_pruned` form is the rendered shape (per the collapse rule above; the cycle-007 lowering-verifier verdict-(c) on OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`). For Palace's actual KSP consumer surface (the four-scalar consumer at `reference/palace/palace/linalg/iterative.hpp:52-55`, consumed solely at `reference/palace/palace/linalg/ksp.cpp:296-310`), the pruned form is the rendered shape; for a monitoring consumer that reads the residual history, the unpruned form is rendered.

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
- `book/src/design/l4_calculus.md:150-184` — the strawman §3.7 `iterate_while` definition (v0.3 extras-carrying form + small-step rule at `:164-171` + `iterate_while_pure` sugar at `:178-182`).
- `book/src/design/l4_calculus.md:186-213` — the strawman §3.8 demand-driven pruning rule that underwrites Law 1.

L3 source (the RHS of this rewrite; extracted from the firm sub-component):

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:164-171` — the unpruned `iterate_while_L3` trajectory-keeping ground form (extracted verbatim).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:176-184` — the pruned `iterate_while_L3_pruned` form (the §3.8 collapse-rule image, extracted verbatim).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:188-198` — the L3-side collapse rule (extracted verbatim).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:202-213` — the §"Audit of cycle-002 identity-in-form claim" verdict that establishes the body-identity licensing the Law-1 transport.
- `book/src/L3/krylov-step.md` — the firm L3 entry holding the lifted CG non-lift catalogue (the `sequential-obstruction` evidence home post cycle-009 corpus reduction).
- `book/src/spec/slices/arnoldi_step.md:194-213` — the live `sequential-obstruction` anchor for the outer loop surviving at L3.

L0 consumer-surface evidence (selects the pruned form for Palace's KSP case, Condition 4):

- `reference/palace/palace/linalg/iterative.hpp:52-55` — the four-scalar KSP consumer surface; `reference/palace/palace/linalg/ksp.cpp:296-310` — the sole consumption site reading only `final_state`-equivalent quantities, which fires the §3.8 collapse to the pruned form.

Concept-page references:

- [`solve-monad`](../concepts/solve-monad.md) — the `Solve = StateT SimState Identity` monad that dissolves to the positional `sim` thread.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra underwriting Law 1 and the collapse rule.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the outer loop's non-lift at L3.

## Status

`firm` — extraction of an already-firm sub-component (`krylov-step-typed-wrapper-dissolution.md:158-200`) into a dedicated layer-coherent chapter. Both L4 caps it lowers are firm L4 rows; the two L3 forms, the §3.8 collapse rule, and the identity-in-form-on-body verdict are exhaustively cited against the strawman §3.7/§3.8, the firm L4 Law 1, and the parent theme's cycle-002 audit. Justification is `structural` + secondary `reduction-chain`. No speculative operator introduced. This chapter closes OQ `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor` (route-b realization) and reconciles OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` (the trajectory-keeping unpruned `iterate_while_L3` is the form the firm L4 Law 1 keeps; the original krylov-step sub-component's trajectory-drop is the pruned image, not a gap in the firm L4 form).

## L4 vs L3 distinction

- **L4**: a single combinator with structural demand-pruning of the trajectory; the body's `Solve`-monad effect is orthogonal to the value-threaded carry; the predicate is purely on the carry; the trajectory is materialised exactly when a downstream consumer reads it.
- **L3**: a tail-recursive loop with explicit `sim`-positional threading; the §3.8 pruning becomes a *call-site choice* between the unpruned `iterate_while_L3` (trajectory materialised as an explicit accumulator) and the pruned `iterate_while_L3_pruned` (trajectory dropped, `step` rendered in its `state`-only subgraph). The L3 forms do not carry the pruning *rule*; they carry its *resolved result* per consumer.

The two layers share signature shape (modulo wrapper dissolution) and small-step semantics on the body; they differ in **effect threading and demand-pruning placement**. The rotation erases the monadic packaging and resolves the demand-pruning per consumer, narrated forward L4→L3.
```

Three surgical replacements in the firm L4 `iterate-while` row's chapter + dep-map. Each `edit:` block below carries ONLY the replacement (new) text; the prose identifies the exact on-disk text to replace.

**Re-anchor 1 — `book/src/L4/iterate-while.md` §"Lowers to" deferral paragraph (`iterate-while.md:188`).** Replace the exact on-disk paragraph beginning `The L4>L3 theme for \`iterate_while\` is not yet authored as a standalone ...` (the full paragraph through `... this section will be updated to cite it directly.`) with the replacement text in this block:

```edit:book/src/L4/iterate-while.md
The L4>L3 theme for `iterate_while` is now authored as the dedicated standalone chapter [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md) (cycle-047), extracted from the sub-component description in the `krylov-step-typed-wrapper-dissolution` theme (§"What the L3 form for iterate_while looks like"). The dedicated theme captures **both** L3 forms: the **trajectory-keeping unpruned form** `iterate_while_L3` — the ground form that materialises the `[readout]` accumulator this firm L4 form keeps (per Law 1) — and the **§3.8-pruned form** `iterate_while_L3_pruned`, which is the collapse-rule image (Law 1's L3-side demand-pruning rewrite applied to the ground form under a `final_state`-only consumer). The earlier sub-component's trajectory-drop is the *pruned image*, not a gap in the firm L4 form; the unpruned ground form is the reconciliation that closes cycle-006 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`. See [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md) §"L3 form (RHS)" for the two forms and the collapse rule.
```

**Re-anchor 2 — `book/src/L4/iterate-while.md` §"L4 vs L3 distinction" closing paragraph (`iterate-while.md:218`).** Replace the exact on-disk paragraph beginning `The two layers' entries share signature shape (modulo wrapper dissolution) and small-step semantics on the body. They differ in **effect threading and demand-pruning placement**. The L4>L3 lowering (sub-theme of ...` (the full paragraph through `... resolves the demand-pruning per consumer.`) with the replacement text in this block:

```edit:book/src/L4/iterate-while.md
The two layers' entries share signature shape (modulo wrapper dissolution) and small-step semantics on the body. They differ in **effect threading and demand-pruning placement**. The L4>L3 lowering is the dedicated standalone theme [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md) (cycle-047; extracted from `krylov-step-typed-wrapper-dissolution`) — it erases the monadic packaging and resolves the demand-pruning per consumer, rendering the unpruned `iterate_while_L3` ground form when the trajectory is observed and the pruned `iterate_while_L3_pruned` form under a `final_state`-only consumer.
```

**Re-anchor 3 — `book/src/L4/index.md:54` dep-map cell.** Replace the entire `iterate-while` row (the table row beginning `| [\`iterate-while\`](./iterate-while.md) |`) — only its "Lowers to" sub-cell changes — with the full replacement row in this block:

```edit:book/src/L4/index.md
| [`iterate-while`](./iterate-while.md) | Pure: `α -> (α -> Bool) -> (α -> { state: α, ...e }) -> { final_state: α, trajectory: [{ ...e }] }`. Solve-threaded: `α -> (α -> Bool) -> (α -> Solve { state: α, ...e }) -> Solve { final_state, trajectory }`. Sugar: `iterate_while_pure :: α -> (α -> Bool) -> (α -> α) -> α`. | Concepts: `solve-monad`, `derived-view-hoisting`, `convergence-test`. L4 rows: consumed by [`krylov-step`](./krylov-step.md) Form A; companion of [`iterate-while-with-prev`](./iterate-while-with-prev.md). | L3 tail-recursive value-threading form via the dedicated theme [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md) *(firm; cycle-047 abstractor extraction — both unpruned `iterate_while_L3` ground form and §3.8-pruned `iterate_while_L3_pruned` form; closes OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`)*. The GMRES-specific re-rendering of `inner_loop` via this combinator is [`gmres-inner-loop-iterate-while-migration`](../L4-L3/gmres-inner-loop-iterate-while-migration.md) *(firm; cycle-020 wave-1 lifter re-anchor)*. | `firm` (harvested cycle-007T160550Z; closes cycle-006 OQ `iterate-while-l4-anchor-missing`) |
```

**Registration — `book/src/L4-L3/index.md` themes-table (own row).** Append the new theme row after the `fgmres-inner-loop-iterate-while-migration` row (block carries the existing row + the new row for anchoring; integrator appends only the new row):

```edit:book/src/L4-L3/index.md
| [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) | Sister-form to the GMRES theme above, specialised for `FgmresSolver<OperType>` (`iterative.cpp:734-836`, `iterative.hpp:222-270`): `pc_side` pinned to `RIGHT` and `flexible` pinned to `true` at the constructor; unconditional `K { Z = K.Z `with` (K.j, z) }` carry-update; otherwise identical L4 form. | Sister-form to the GMRES L3 theme above, specialised for FGMRES: identical wrapper dissolution; body simplifies to the FGMRES collapsed shape (`pc_side`/`flexible` variant rows removed). Textually identical break-site at `iterative.cpp:823-828` (cycle-010 MCP-pilot audit). | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-011 lifter; same upstream gmres.md §L4 v0.6→v0.7 dependency as the GMRES sister) |
| [`iterate-while-dissolution`](./iterate-while-dissolution.md) | L4 [`iterate-while`](../L4/iterate-while.md) Form A — the extras-carrying, `Solve`-threaded combinator `α -> (α -> Bool) -> (α -> Solve { state: α, ...e }) -> Solve { final_state, trajectory }`, with the §3.7 small-step rule and the load-bearing Law 1 (demand-driven trajectory pruning). The generic combinator that the gmres / fgmres inner-loop themes specialise. | Two L3 tail-recursive value-threaded forms from the same invocation: the **unpruned** `iterate_while_L3` ground form (materialises the `[readout]` trajectory accumulator) and the **§3.8-pruned** `iterate_while_L3_pruned` collapse-rule image (drops the accumulator; `step` rendered in its `state`-only subgraph); `Solve` monad dissolves to positional `sim` threading; record-spread step return dissolves to a positional tuple. | `structural` + secondary `reduction-chain` | `firm` (cycle-047 abstractor; extraction + re-homing of the firm sub-component `krylov-step-typed-wrapper-dissolution.md:158-200`; closes OQ `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor`, reconciles OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`) |
```

```edit:book/src/SUMMARY.md
- [fgmres-inner-loop-iterate-while-migration](./L4-L3/fgmres-inner-loop-iterate-while-migration.md)
- [iterate-while-dissolution](./L4-L3/iterate-while-dissolution.md)
```

## Speculative operators proposed

None. This theme is an extraction + re-homing of an already-firm sub-component (`krylov-step-typed-wrapper-dissolution.md:158-200`). Both L4 caps it lowers — [`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) — are firm L4 rows (harvested cycle-007T160550Z). No new speculative operator is introduced, and no harvester promotion is required.

## Supporting evidence

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:158-200` — the buried sub-component §"What the L3 form for `iterate_while` looks like": the unpruned `iterate_while_L3` (`:164-171`), the pruned `iterate_while_L3_pruned` (`:176-184`), the collapse rule (`:188-198`), and the survival-of-obstruction note (`:200`). All extracted verbatim with citations.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:202-213` — the §"Audit of cycle-002 identity-in-form claim" verdict establishing the body-identity that licenses Law 1's transport through the wrapper dissolution.
- `book/src/L4/iterate-while.md` — the firm L4 LHS cap: §Signature (`:28-43`), §Semantics small-step rule (`:64-74`), Law 1 (`:123-133`), `iterate_while_pure_L3` lowering (`:190-195`), L3>L2 identity note (`:196-197`); §"Lowers to" deferral (`:182-188`) and §"L4 vs L3 distinction" deferral (`:218`) re-anchored by this dispatch; dep-map cell (`book/src/L4/index.md:54`) re-anchored.
- `book/src/L4/iterate-while-with-prev.md` — the firm L4 sibling cap, the second pointer at the buried sub-component (its `prev`-positional dissolution is the only delta over this generic theme).
- `book/src/design/l4_calculus.md:150-184` (§3.7 `iterate_while`), `:186-213` (§3.8 demand-pruning) — the strawman sources for the small-step rule and Law 1. Citecheck-confirmed: §3.8 pruning anchors at `:186,201` (within `:186-213`); the §3.7 small-step rule block is `:164-171` (the strawman `iterate_while` token leads in at `:162`, the rule itself is the cited `:164-171` block reproduced verbatim by the firm L4 row).
- `reference/palace/palace/linalg/iterative.hpp:52-55` + `reference/palace/palace/linalg/ksp.cpp:296-310` — the Palace KSP four-scalar consumer surface that selects the pruned form (Condition 4).
- `book/src/spec/slices/arnoldi_step.md:194-213` — the live `sequential-obstruction` anchor for the outer loop surviving at L3.

## Open questions / caveats

- **Degenerate-extraction flag (per dispatch instruction).** The two L3 forms, the collapse rule, and the identity-in-form verdict ARE extracted verbatim from the firm sub-component (`krylov-step-typed-wrapper-dissolution.md:164-198`) — the *code forms* are identical. However, the extraction is **not** a pure re-anchor with ZERO new derivation: the new content is (a) the layer-coherent forward L4→L3 framing centred on the combinator itself rather than as a krylov-step sub-step; (b) the explicit **ground-form-vs-collapse-image split** (the planner/cycle-046-critic framing that the pruned form is Law 1's image, NOT a contradiction) — the original sub-component's prose at `:188` framed the trajectory-drop as "the very gap" (a defect note), whereas this chapter reframes it as the reconciliation (the unpruned form is what Law 1 keeps; the pruned form is its demand-pruned image); (c) the four-condition applicability section and the generic-vs-slice-specialised relationship to the gmres/fgmres themes. The planner's route-b judgement holds. If the integrator nonetheless judges the body genuinely identical and wants a thinner theme, the collapsible surface is the §"L3 form (RHS)" code blocks (which could cite the parent theme rather than reproduce) — but reproducing them keeps the chapter self-contained and layer-coherent, which is the point of the re-homing.
- **OQ `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor` — CLOSED by this dispatch** (route-b realization). The route question (lifter re-anchor vs abstractor fresh theme) is resolved: abstractor authored the dedicated chapter as an extraction; no fresh derivation was needed beyond the re-homing framing.
- **OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` — reconciled, recommend close.** The "gap" was the original krylov-step sub-component dropping the trajectory. The reconciliation: the trajectory-drop is the §3.8-**pruned** form (correct under a `final_state`-only consumer); the firm L4 Law 1 keeps the trajectory in the unpruned ground form `iterate_while_L3`, now authored here. There is no gap in the firm L4 form — only two consumer-selected L3 images. Recommend the integrator/meta-phase close this OQ on this dispatch's landing.
- **`iterate-while-with-prev` §"Lowers to" re-anchor — NOT in scope this dispatch.** The dispatch instruction named the `iterate-while.md` re-anchors (§"Lowers to", §"L4 vs L3 distinction", dep-map cell). The sibling `iterate-while-with-prev.md` §"Lowers to" also points at the buried sub-component and would benefit from re-anchoring to cite this dedicated theme (noting the `prev`-positional delta). I flag it here rather than editing it (one-theme-per-invocation discipline + dispatch scope); recommend a follow-up lifter/abstractor micro-dispatch or an integrator stub-touch. Filed as a fresh OQ candidate: `iterate-while-with-prev-lowers-to-reanchor-to-dedicated-dissolution-theme`.
- **Citation self-verification.** All load-bearing L4/L3/strawman citation ranges were citecheck-confirmed pre-emit (§3.8 pruning `:186-213` ok; Law 1 `iterate-while.md:123-133` ok; the three extracted forms `krylov-step-typed-wrapper-dissolution.md:164-171`/`:176-184`/`:188-198` ok). The strawman §3.7 small-step block is `:164-171` (the firm L4 row's §Semantics transcribes it verbatim; the `iterate_while` token first appears at `:162` in the section lead-in, the rule block itself is `:164-171`).
