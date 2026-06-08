# iterate-while-with-prev-dissolution

The L4>L3 lowering theme for the [`iterate_while_with_prev`](../L4/iterate_while_with_prev.md) combinator — the carry-bootstrapped (first-iteration-unrolled) sister of [`iterate_while`](../L4/iterate_while.md). It folds a `steady_step` over an initial carry while threading an additional `PrevCarry` closure parameter (the prior iteration's recurrence variable: CG's `beta_prev`, GMRES Hessenberg's `H_{k,k-1}`, Chebyshev's `x_{k-1}`), produced by an explicit `bootstrap_step` that fires exactly once before the steady loop. The theme dissolves the same L4 wrapper machinery as the no-prev dissolution (the `Solve` monad, the row-polymorphic `{ state: α, prev: β, ...e }` step return, the demand-prunable `trajectory` accumulator) **plus a fourth piece specific to this combinator**: the `prev` closure parameter dissolves into a positional argument of the L3 tail-recursive worker, and the bootstrap step becomes a non-recursive first call. It is the **dedicated home** for a Form-B rewrite also expressed as the firm L4 cap's own §"Lowers to" sketch (`iterate_while_with_prev.md:182-198`) plus a sub-component of [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" point 4 (`krylov-step-typed-wrapper-dissolution.md:74-89`).

This is the **carry-bootstrapped sister** of the companion theme `iterate-while-dissolution`. The two themes share the entire wrapper-dissolution body; this chapter adds **only the `prev`-positional delta** (the bootstrap call + the closure-threaded `prev` becoming a positional tuple slot).

## Slug

`iterate-while-with-prev-dissolution`

## Context

[`iterate_while`](../L4/iterate_while.md) and [`iterate_while_with_prev`](../L4/iterate_while_with_prev.md) are firm L4 rows. The with-prev combinator's L4>L3 lowering also appears as (a) the firm L4 cap's own §"Lowers to" L3 sketch (`iterate_while_with_prev.md:182-198`) and (b) implicitly inside the Form-B treatment of [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) point 4 (`krylov-step-typed-wrapper-dissolution.md:74-89`) — but neither is the combinator's **home**. This chapter is the standalone theme: the bootstrap-then-tail-recursive L3 form, the §3.8 collapse rule, and the identity-in-form-on-body verdict, with the layer-coherent framing — narrating the combinator's own L4→L3 dissolution forward and isolating the **`prev`-positional delta** as the only difference from the companion `iterate-while-dissolution` theme.

### Companion theme — `iterate-while-dissolution`

This theme is the carry-bootstrapped specialisation of the companion theme `iterate-while-dissolution` (`book/src/L4-L3/iterate-while-dissolution.md`). The companion covers the no-prev `iterate_while` dissolution; this theme is that pattern **plus** the `prev`-positional addition. The two are related by **Law 1 of [`iterate_while_with_prev`](../L4/iterate_while_with_prev.md)** (`iterate_while_with_prev.md:129-135`): when `PrevCarry = ()` (`β = ()`), this combinator definitionally degenerates to `iterate_while` preceded by an outer identity bootstrap-step, so this theme's L3 form degenerates to the companion theme's L3 form. The companion is the `β = ()` specialisation; this theme is the strict generalisation.

## L4 form (LHS)

The L4 `iterate_while_with_prev` — the carry-bootstrapped, extras-carrying, `Solve`-threaded combinator consumed by [`krylov_step`](../L4/krylov_step.md) Form B (`iterate_while_with_prev.md:41-50`). This is the firm L4 row's `Solve`-threaded signature:

    iterate_while_with_prev
      :: (α -> Solve { state: α, prev: β, ...e })        -- bootstrap_step
      -> α                                                -- initial carry
      -> ((α, β) -> Solve { state: α, prev: β, ...e })    -- steady_step
      -> (α -> Bool)                                      -- cont
      -> Solve { final_state: α, trajectory: [{ ...e }] }

The argument order is `bootstrap_step` first, `init` second, `steady_step` third, `cont` fourth (`iterate_while_with_prev.md:52`). The small-step semantics are the bootstrap-then-tail-recurse rule from the firm L4 row's §Semantics (`iterate_while_with_prev.md:74-93`): fire the bootstrap once to produce the initial `prev` (`β_0`) and the bootstrap-stepped carry (`a_1`), then enter the steady tail recursion `steady_loop` (identical to `iterate_while`'s recursion modulo the `prev` threading):

$$
\begin{aligned}
\textsf{iterate\_while\_with\_prev}\ f_{\textsf{boot}}\ a_0\ f_{\textsf{steady}}\ p &\;\to\; \\
&\textsf{let}\ \{\textsf{state}: a_1,\ \textsf{prev}: \beta_0,\ \dots e_0\} = f_{\textsf{boot}}(a_0)\ \textsf{in} \\
&\textsf{let}\ \{\textsf{final\_state},\ \textsf{trajectory}\} = \textsf{steady\_loop}\ a_1\ \beta_0\ f_{\textsf{steady}}\ p\ \textsf{in} \\
&\{\textsf{final\_state},\ \textsf{trajectory}: [\{\dots e_0\}] \mathop{++} \textsf{trajectory}\}
\end{aligned}
$$

$$
\begin{aligned}
\textsf{steady\_loop}\ a\ \beta\ f\ p &\;\to\; \textsf{if}\ p(a) \\
&\quad \textsf{then}\ \textsf{let}\ \{\textsf{state}: a',\ \textsf{prev}: \beta',\ \dots e\} = f(a, \beta)\ \textsf{in} \\
&\quad\quad \textsf{let}\ \{\textsf{final\_state},\ \textsf{trajectory}\} = \textsf{steady\_loop}\ a'\ \beta'\ f\ p\ \textsf{in} \\
&\quad\quad \{\textsf{final\_state},\ \textsf{trajectory}: [\{\dots e\}] \mathop{++} \textsf{trajectory}\} \\
&\quad \textsf{else}\ \{\textsf{final\_state}: a,\ \textsf{trajectory}: [\,]\,\}
\end{aligned}
$$

The three load-bearing L4 properties the lowering must transport (`iterate_while_with_prev.md:97-103`):

1. **The bootstrap always runs** exactly once, before the predicate's first test — structural, because the predicate's first call needs a `prev`-threaded carry to inspect.
2. **The predicate fires after the bootstrap, before any steady step**, and reads the carry `α` only (never `prev`).
3. **The `prev` value is threaded as a closure parameter of the loop, not a field of the carry** — the load-bearing schema-narrowing the first-iteration-unrolling rotation buys.

The load-bearing demand-pruning property is **Law 2 — trajectory-pruning demand-rule** (`iterate_while_with_prev.md:137-147`, inherited from [`iterate_while`](../L4/iterate_while.md) Law 1 `iterate_while.md:123-133` and the strawman §3.8): when a consumer reads only `final_state`, the §3.8 rule rewrites **both** `bootstrap_step` and `steady_step` to the subgraphs computing only the `{ state, prev }` fields, omitting the extras. (This is Law 1's single-body rule lifted to two step bodies.)

The wrapper machinery this theme dissolves is **four** pieces (the three of the no-prev dissolution plus the `prev` closure thread):

1. **The `Solve` monad** — `Solve = StateT SimState Identity` (`book/src/concepts/solve-monad.md:1-68`). Both the bootstrap and each steady step discharge as `do`-blocks carrying the `SimState` `it` counter (`iterate_while_with_prev.md:105`).
2. **The row-polymorphic step return `{ state: α, prev: β, ...e }`** — a TypeScript-style record with a generic extras spread `...e`. L3 has no row-polymorphic record spread.
3. **The demand-prunable `trajectory: [{ ...e }]` accumulator** — the syntactic site where Law 2 fires; the bootstrap's extras are the first trajectory element.
4. **The `prev` closure parameter** — threaded by the combinator (not the slice) as a positional argument of `steady_step`, with the bootstrap producing its initial value. This is the **delta over the no-prev dissolution**.

## L3 form (RHS)

The L4>L3 dissolution produces a **bootstrap call followed by a tail-recursive value-threaded loop** with the `Solve` monad dissolved to an explicit positional `sim` thread, the record-spread step return dissolved to a positional tuple, and the `prev` closure parameter dissolved to a positional tuple slot. Two L3 forms arise from the **same** L4 invocation under different consumer demands; both share the bootstrap-then-loop shape extracted from the firm cap's §"Lowers to" (`iterate_while_with_prev.md:182-198`).

### Unpruned form — the trajectory-keeping ground form

The direct value-threaded dissolution when a downstream consumer reads `.trajectory` (no §3.8 collapse fires; the `[e₀] ++ trajectory` accumulator the firm L4 Law 2 keeps is materialised at L3). This is the **ground form** — the faithful L3 image of the bootstrap-then-`steady_loop` small-step rule with the trajectory preserved (extracted from `iterate_while_with_prev.md:182-198`; `sim` threading made positional, trajectory consed in iteration order):

    iterate_while_with_prev_L3 f_boot a₀ f_steady p sim₀ =
      let (a₁, β₀, e₀, sim₁) = f_boot (a₀, sim₀)              -- bootstrap fires once
      in let go (a, β, sim, traj) =
               if not (p a)
                 then (a, sim, reverse traj)                  -- final_state, sim', trajectory
                 else let (a', β', e, sim') = f_steady (a, β, sim)
                      in go (a', β', sim', e : traj)
         in go (a₁, β₀, sim₁, [e₀])                           -- seed traj with bootstrap extras

The bootstrap `f_boot` fires **once, non-recursively**, producing the initial carry `a₁`, the initial `prev` value `β₀`, the bootstrap extras `e₀`, and the threaded `sim₁`. The steady worker `go` then threads `(a, β, sim, traj)` positionally: `β` is the dissolved `prev` closure parameter, surfaced as an ordinary positional tuple slot (the combinator's closure-threading becomes explicit positional threading at L3). The `traj` accumulator is seeded with the bootstrap's extras `[e₀]` (matching the L4 rule's `[{...e₀}] ++ trajectory` first-element prepend) and consed in iteration order, `reverse`d at termination. The `sim` is threaded positionally (the `Solve` monad has dissolved, per `solve-monad.md`); the `readout`/`e` is the positional image of the row-polymorphic `{...e}` extras. This form keeps the trajectory because the consumer demands it.

### Pruned form — the §3.8 collapse-rule image

The §3.8-collapsed shape that arises when the consumer observes only `final_state`-equivalent quantities. **This form drops the accumulator BY §3.8 demand-pruning (Law 2's collapse rule), NOT against Law 2** — the pruned form is the *image* of the collapse rule applied to the unpruned ground form, so it is fully consistent with the firm L4 Law 2 that keeps the trajectory in its general statement. Law 2 *is* the rule that licenses dropping it when unobserved, rewriting **both** the bootstrap and the steady body to their `{state, prev}` subgraphs:

    iterate_while_with_prev_L3_pruned f_boot a₀ f_steady p sim₀ =
      let (a₁, β₀, sim₁) = f_boot_sp (a₀, sim₀)               -- bootstrap, extras pruned
      in let go (a, β, sim) =
               if not (p a)
                 then (a, sim)                                -- final_state, sim'
                 else let (a', β', sim') = f_steady_sp (a, β, sim)
                      in go (a', β', sim')
         in go (a₁, β₀, sim₁)

where `f_boot_sp` / `f_steady_sp` are the §3.8-pruned `{state, prev}`-subgraphs of `f_boot` / `f_steady` — the bootstrap and steady bodies with the extras computation eliminated **as dead code at the call site** (not merely unused at runtime). The L3-side `f_steady_sp` has shape `(carry, prev, sim) -> (carry', prev', sim')` — the positional-tuple image of the L4-side `steady_step^{stateprev}` of Law 2 (`iterate_while_with_prev.md:137-147`), with the `sim` thread surfacing positionally because the `Solve` monad has dissolved, and `prev` surfacing as the dedicated positional slot. The trajectory is dropped entirely (no seed, no cons, no `reverse`).

### The collapse rule

The L4>L3 collapse from the unpruned ground form to the pruned form is governed by the L3-side image of Law 2:

$$
\frac{
  \text{only } \textsf{final\_state} \text{ of the L3 result is observed downstream}
}{
  \textsf{iterate\_while\_with\_prev\_L3}\ f_{\textsf{boot}}\ a_0\ f_{\textsf{steady}}\ p\ \textsf{sim}_0 \;\equiv\; \textsf{iterate\_while\_with\_prev\_L3\_pruned}\ f_{\textsf{boot}}^{\textsf{sp}}\ a_0\ f_{\textsf{steady}}^{\textsf{sp}}\ p\ \textsf{sim}_0
}
$$

This is exactly the L3-side image of **Law 2** of [`iterate_while_with_prev`](../L4/iterate_while_with_prev.md) (`iterate_while_with_prev.md:137-147`) — the L4 demand-pruning law **transports through** the L4>L3 wrapper dissolution because the dissolution is value-thread-isomorphic on **both** step bodies (the parent theme's §"Audit of cycle-002 identity-in-form claim", `krylov-step-typed-wrapper-dissolution.md:202-213`, establishes the body-identity that licenses the transport; the bootstrap and steady bodies are the Form-B first/steady pair audited there). The unpruned `iterate_while_with_prev_L3` is the ground form; the pruned `iterate_while_with_prev_L3_pruned` is its collapse-rule image; the rule above is the rewrite between them. **Framing** (identical to the companion theme): the pruned form is NOT a contradiction of the firm L4 Law 2 (which keeps the trajectory in its general statement) — it is the *consequence* of Law 2's collapse rule fired under a `final_state`-only consumer.

### Degeneracy to the companion dissolution

When `PrevCarry = ()` (`β = ()`), this combinator definitionally reduces to `iterate_while` preceded by an outer identity bootstrap (Law 1 of [`iterate_while_with_prev`](../L4/iterate_while_with_prev.md), `iterate_while_with_prev.md:129-135`). At L3 this means: the `β` positional slot carries no information, the bootstrap call collapses to a pure carry-shift, and `iterate_while_with_prev_L3` degenerates to the companion theme's `iterate_while_L3` (`book/src/L4-L3/iterate-while-dissolution.md` §"L3 form (RHS)"), with the bootstrap's extras `[e₀]` becoming the trajectory's first element. This is the L3-side image of the L4 degeneracy law and is what makes the two themes a **family**: this theme is the strict generalisation, the companion is the `β = ()` specialisation.

### What does NOT change in the rotation

Both step bodies' primitive sequences survive the rotation textually unchanged — the dissolution is **identity-in-form on the bodies** (`krylov-step-typed-wrapper-dissolution.md:202-213`). The rotation touches only the **wrapper**: the `Solve` monad becomes positional `sim`, the record-spread step return becomes a positional tuple, the `prev` closure parameter becomes a positional tuple slot, the bootstrap becomes a non-recursive first call, and the trajectory becomes either an explicit list accumulator (unpruned) or nothing (pruned). The bootstrap and steady kernels — whatever the slice's per-step kernels are — pass through unchanged in their dataflow positions.

The **outer-loop `sequential-obstruction`** survives at L3: both L3 forms name the steady loop tail-recursively but do **not** claim it lifts to a global tensor-field op. This is the expected outcome for Krylov-family iterations at L3 per [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the firm anchor is its §"MGS as sequential-obstruction". The bootstrap call is a single non-recursive step and carries no loop obstruction; only the steady tail recursion does. The unpruned form additionally allocates the `O(N)` trajectory accumulator; the pruned form does not.

### What this lowering does NOT cover

- **The L3>L2 hop on the loop combinator itself**, which is *also* identity-in-form (`iterate_while_with_prev.md:202`), the same tail-recursive shape being L2-native. The full L4>L3>L2 chain for the no-extras `iterate_while_with_prev_pure` collapses to the L4>L3 wrapper dissolution alone; the L3>L2 completion is the trivial identity step, not duplicated here.
- **The no-prev `iterate_while` dissolution** — that is the companion theme `iterate-while-dissolution` (`book/src/L4-L3/iterate-while-dissolution.md`), which this theme generalises. When `β = ()` this theme degenerates to it (Law 1; see §"Degeneracy to the companion dissolution").
- **The slice-specialised dissolutions** — the GMRES / FGMRES inner-loop themes ([`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md), [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md)) specialise the no-prev `iterate_while` dissolution (those use Form A). The Form-B `iterate_while_with_prev` consumer is CG v0.5 (firm-homed at `book/src/L4/krylov_step.md` Form B); a CG-Form-B dissolution would instantiate this theme's pruned form under the CG four-scalar consumer, but is not re-derived here.

## Applicability conditions

The rewrite is valid when all five of the following hold (the four inherited from `krylov-step-typed-wrapper-dissolution.md` §"Applicability conditions" plus the `prev`-threading condition specific to this combinator):

1. **The L4 `Solve` monad's effect domain is exactly `SimState`.** The only `modify` in either body is the `it` counter increment; no carry or `prev` field is monad-touched. This lets the monad dissolve to a single positional `sim` argument threaded through both the bootstrap and steady calls (`iterate_while_with_prev.md:105`, `solve-monad.md` §"What stays out of the monad").

2. **The predicate is pure on the carry** (`cont :: α -> Bool`, `iterate_while_with_prev.md:59`). No reads of `SimState`, `OpParams`, the per-step extras, or **the `prev` value** (the predicate-on-prev anti-pattern, `iterate_while_with_prev.md:115-123`). This is what lets the L3 branch test `not (p a)` read only the positional `carry` argument. Slices whose termination needs a `prev`-derived quantity fold it into the carry inside `steady_step` (CG v0.5: `s.converged` is set inside `cg_steady_step` from the freshly-computed `res'`; `beta_prev` is the `prev` parameter but is never read by the predicate; the predicate-on-carry-only + the `beta_prev`-as-`prev`-parameter pattern is firm-homed at `book/src/L4/krylov_step.md` Form B).

3. **Both step bodies' primitive sequences are L3-native or carry their own L3 classification.** Each bootstrap/steady-body primitive is either a whole-tensor global op (L3-native by signature) or carries a documented body-level obstruction. The wrapper dissolution does not change either body's L3 classification — they survive in form.

4. **The bootstrap produces the initial `prev` and `sim`-threads exactly once.** The bootstrap call is non-recursive and runs before the predicate's first test (`iterate_while_with_prev.md:99` — "The bootstrap always runs"); the L3 form renders it as the let-bound prefix `(a₁, β₀, [e₀], sim₁) = f_boot (a₀, sim₀)`. If a consumer needs an "already-converged-before-first-step" guard, it lives outside the combinator (CG v0.5's outer initial-convergence test, firm-homed at `book/src/L4/krylov_step.md` Form B) and outside this lowering.

5. **Trajectory-pruning selection** (selects unpruned vs pruned form). When the downstream consumer reads `.trajectory` (or any per-step extras, including the bootstrap's), the **unpruned** `iterate_while_with_prev_L3` form is the rendered L3 shape. When the consumer observes only `final_state`-equivalent quantities, the **pruned** `iterate_while_with_prev_L3_pruned` form is the rendered shape (per the collapse rule above). For Palace's actual KSP consumer surface (the four-scalar consumer at `reference/palace/palace/linalg/iterative.hpp:52-55`, consumed solely at `reference/palace/palace/linalg/ksp.cpp:296-310`), the pruned form is the rendered shape; for a monitoring consumer that reads the residual history, the unpruned form is rendered.

## Justification kind

**`structural`** with secondary **`reduction-chain`**.

- **Structural** (dominant): the L4 wrapper machinery (Solve monad, `iterate_while_with_prev` combinator, extras-trajectory record, `prev` closure parameter, predicate-on-carry-only discipline) dissolves into an L3 bootstrap-call-plus-tail-recursive value-threaded form; both bodies' primitive sequences are preserved by construction (every L4 primitive call becomes an L3 primitive call at the same dataflow position). The `prev` closure parameter becomes a positional tuple slot; the bootstrap becomes a non-recursive prefix; the trajectory becomes an explicit accumulator (unpruned) or is dropped (pruned), both structural rewrites of the syntactic trajectory site.
- **Reduction-chain** (secondary): the `Solve` monad's `>>=` desugars to explicit positional `sim` threading in both the bootstrap and steady calls; the bootstrap-then-`steady_loop` small-step rule desugars to the let-bound prefix plus the tail-recursive `go` worker; the §3.8 pruning collapse from the unpruned to the pruned form is the mechanical application of Law 2's L3-side image to both bodies.

**Abstraction-direction note**: L4 is the higher-abstraction layer (typed records, monadic effect, closure-threaded `prev`, structural bootstrap-then-loop, demand-prunable trajectory); L3 is the lower-abstraction layer (positional values threaded explicitly, `prev` as a positional slot, bootstrap as a non-recursive prefix, branch-on-predicate in tail recursion, trajectory as explicit accumulator or dropped). The rotation direction is **L4 → L3**, narrated forward per the high→low discipline.

## Speculative L4 operators

None. This theme is an extraction of an already-firm form; the L4 cap it lowers ([`iterate_while_with_prev`](../L4/iterate_while_with_prev.md)) is a firm L4 row, and the companion no-prev combinator ([`iterate_while`](../L4/iterate_while.md)) is firm. No new speculative operator is introduced.

## Verified-against

L4 source (the LHS of this rewrite):

- `book/src/L4/iterate_while_with_prev.md:41-50` — the firm L4 `iterate_while_with_prev` `Solve`-threaded signature (the LHS); `:52` the argument order; `:74-93` the §Semantics bootstrap-then-`steady_loop` small-step rules; `:97-103` the three semantic points (bootstrap always runs / predicate after bootstrap / `prev` as closure parameter); `:129-135` Law 1 (degeneracy to `iterate_while` when `β = ()`); `:137-147` Law 2 (trajectory-pruning, the load-bearing transported property); `:182-198` the firm §"Lowers to" L3 form (`iterate_while_with_prev_L3` + `steady_loop_L3`) extracted as the RHS; `:202` the L3>L2 identity-in-form note; `:200` the standalone-pending deferral and `:223` the §"L4 vs L3 distinction" deferral, both re-anchored by this dispatch.
- `book/src/L4/iterate_while.md:123-133` — the companion Law 1 (single-body demand-pruning) that Law 2 lifts to two bodies; the rule transported through the dissolution.
- `book/src/semantics/index.md:150-184` — the strawman §3.7 `iterate_while` small-step rule the bootstrap-then-loop semantics generalise (`:164-171` the rule block, `:179-182` the `iterate_while_pure` sugar).
- `book/src/semantics/index.md:186-213` — the strawman §3.8 demand-driven pruning rule that underwrites Law 2.

L3 source (the RHS of this rewrite; extracted from the firm cap + firm sub-component):

- `book/src/L4/iterate_while_with_prev.md:182-198` — the firm L4 cap's own §"Lowers to" L3 form (`iterate_while_with_prev_L3` + `steady_loop_L3`), the bootstrap-then-tail-recursive ground shape extracted here.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:74-89` — the Form-B-in-L3 dissolution (`krylov-step-L3-first`/`krylov-step-L3-steady`, point 4): the `PrevCarry`-as-positional-value-in-the-threaded-tuple framing, extracted as the `prev`-positional delta.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:150-154` — the `iterate_while_with_prev` speculative-operator signature the Form-B body consumes (the bootstrap-step / steady-step split this theme renders positionally).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:202-213` — the §"Audit of cycle-002 identity-in-form claim" verdict that establishes the body-identity licensing the Law-2 transport for both bodies.
- [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"MGS as sequential-obstruction" — the firm `sequential-obstruction` anchor for the steady loop surviving at L3.

L0 consumer-surface evidence (selects the pruned form for Palace's KSP case, Condition 5):

- `reference/palace/palace/linalg/iterative.hpp:52-55` — the four-scalar KSP consumer surface; `reference/palace/palace/linalg/ksp.cpp:296-310` — the sole consumption site reading only `final_state`-equivalent quantities, which fires the §3.8 collapse to the pruned form.

Slice evidence (the Form-B consumer):

- `book/src/L4/krylov_step.md` Form B — the canonical CG form using `iterate_while_with_prev` (the call site); the `cg_first_step` / `cg_steady_step` split is the prototypical bootstrap/steady pair, with the predicate-on-carry-only + `beta_prev`-as-`prev`-parameter pattern.

Concept-page references:

- [`solve-monad`](../concepts/solve-monad.md) — the `Solve = StateT SimState Identity` monad that dissolves to the positional `sim` thread.
- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the rotation that hoists `prev` into the closure parameter this theme dissolves positionally.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra underwriting Law 2 and the collapse rule.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the steady loop's non-lift at L3.

## Status

`firm` — extraction of the form (the firm L4 cap's own §"Lowers to" `iterate_while_with_prev.md:182-198` + the sub-component `krylov-step-typed-wrapper-dissolution.md:74-89` point 4) into a dedicated layer-coherent chapter. The L4 cap it lowers ([`iterate_while_with_prev`](../L4/iterate_while_with_prev.md)) and the companion combinator ([`iterate_while`](../L4/iterate_while.md)) are firm L4 rows; the two L3 forms, the §3.8 collapse rule, the bootstrap-prefix shape, and the identity-in-form-on-bodies verdict are cited against the strawman §3.7/§3.8, the firm L4 Law 1 / Law 2, and the parent theme's body-identity audit. Justification is `structural` + secondary `reduction-chain`.

## L4 vs L3 distinction

- **L4**: a single combinator with structural bootstrap-then-loop semantics, a closure-threaded `prev` parameter, and demand-pruning of the trajectory; both bodies' `Solve`-monad effect is orthogonal to the value-threaded carry and `prev`; the predicate is purely on the carry; the trajectory is materialised exactly when a downstream consumer reads it.
- **L3**: a non-recursive bootstrap prefix followed by a tail-recursive loop with explicit `(carry, prev, sim)` positional threading; the §3.8 pruning becomes a *call-site choice* between the unpruned `iterate_while_with_prev_L3` (trajectory materialised as an explicit accumulator seeded with the bootstrap extras) and the pruned `iterate_while_with_prev_L3_pruned` (trajectory dropped, both bodies rendered in their `{state, prev}`-only subgraphs). The L3 forms do not carry the bootstrap-then-loop *combinator name* or the pruning *rule*; they carry the *unrolled tail-recursive shape with the bootstrap as an explicit prefix* and the pruning's *resolved result* per consumer.

The two layers share signature shape (modulo wrapper dissolution) and small-step semantics on both bodies; they differ in **effect threading, `prev`-parameter placement, and demand-pruning placement**. The rotation erases the monadic packaging, positionalises the `prev` closure parameter, renders the bootstrap as a non-recursive prefix, and resolves the demand-pruning per consumer; it does *not* re-introduce the iteration-zero branch (the first-iteration-unrolling rotation is preserved across the lowering). Narrated forward L4→L3.
