---
agent: abstractor
invoked_at: 2026-06-01T162018Z
scope: L4>L3 theme sketch — iterate-while-with-prev-dissolution (sister of D1; extraction + re-homing of the buried Form-B sub-component into a dedicated layer-coherent chapter)
status: integrated
integrated_at: 2026-06-01T171229Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (D2; cycle-047). NEW firm L4>L3 theme book/src/L4-L3/iterate-while-with-prev-dissolution.md (the carry-bootstrapped with-prev sister of D1) + 3 re-anchors (L4/iterate-while-with-prev.md:200/:223, L4/index.md:55 dep-map cell) + L4-L3/index row + SUMMARY line (distinct from D1, no clobber). Live-links D1's sibling chapter (same-cycle co-land, resolved). One DELIBERATE cg.md:441-446 OOB historical-provenance prose mention (by-design, not a build/link error). L4>L3 firm 3->5. Jointly closed iterate-while-l4-l3-standalone-theme-warranted + iterate-while-with-prev-lowers-to-reanchor (recommendations; meta-phase authority). Build clean, linkcheck2 green."
inputs:
  - reports/2026-06-01T162018Z-cycle-047-abstractor-iterate-while-dissolution/CYCLE.md (D1 companion theme; structure/altitude reference + same-cycle sibling cross-reference)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:74-89 (the Form-B / krylov-step-L3-first/steady L3 dissolution, point 4) + :150-154 (the iterate_while_with_prev speculative-operator signature the Form B body consumes) + :164-198 (the iterate_while L3 forms + collapse rule the with-prev form parallels)
  - book/src/L4/iterate-while-with-prev.md (firm L4 LHS cap; §Signature :32-50, §Semantics :74-93, Law 1 degeneracy :129-135, Law 2 trajectory-pruning :137-147, §"Lowers to" L3 form :182-198 + deferral :200, §"L4 vs L3 distinction" deferral :223)
  - book/src/L4/iterate-while.md:123-133 (companion Law 1 — the demand-pruning law transported through the dissolution)
  - book/src/L4/index.md:55 (dep-map cell carrying the "standalone follow-up pending" note — re-anchor target)
  - book/src/design/l4_calculus.md:150-184 (§3.7 iterate_while small-step rule + sugar — the bootstrap-then-loop semantics generalise) + :186-213 (§3.8 demand-driven pruning, Law 2's strawman source)
  - book/src/L4-L3/index.md (themes-table for own-row registration) + book/src/SUMMARY.md:14-17 (L4>L3 Part for own-line registration)
---

# CYCLE: L4>L3 theme sketch — iterate-while-with-prev-dissolution

## Summary

This dispatch is the sister of D1 (`iterate-while-dissolution`): it extracts the L4>L3 dissolution of the **carry-bootstrapped** [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) combinator (Form B, the first-iteration-unrolled `iterate_while_with_prev`) into a dedicated, layer-coherent chapter `book/src/L4-L3/iterate-while-with-prev-dissolution.md`. The body content already exists firm: the bootstrap-then-tail-recursive L3 form (`iterate_while_with_prev_L3` + `steady_loop_L3`) is the firm L4 cap's own §"Lowers to" rendering (`iterate-while-with-prev.md:182-198`), and the Form-B-collapse-into-carry-threading framing is the firm sub-component of `krylov-step-typed-wrapper-dissolution.md:74-89` (point 4 — the `krylov-step-L3-first`/`krylov-step-L3-steady` positional-carry dissolution) plus the `iterate_while_with_prev` speculative-operator signature it consumes (`:150-154`). This theme is D1's pattern **plus** the additional `prev`-positional dissolution (the bootstrap step becomes a non-recursive first call producing the initial `PrevCarry`; the steady step recurses with `prev` threaded positionally). It captures **both** the trajectory-keeping unpruned form and the §3.8-pruned form under the **same collapse-rule framing as D1** — the pruned form is the collapse-rule image of Law 2 fired under a `final_state`-only consumer, NOT a contradiction of Law 2 (which keeps the trajectory in its general statement). The prose narrates forward L4→L3 per the high→low discipline. The dispatch re-anchors the two `iterate-while-with-prev.md` deferrals (its §"Lowers to" standalone-pending paragraph `:200` + its §"L4 vs L3 distinction" closing paragraph `:223`) and the `book/src/L4/index.md:55` dep-map cell to cite this dedicated chapter, and registers the new theme into `L4-L3/index.md` (own row) and `SUMMARY.md` (own line). This + D1 jointly close OQ `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor` and address the D1-flagged `iterate-while-with-prev-lowers-to-reanchor-to-dedicated-dissolution-theme` follow-up.

## Proposed changes

```new:book/src/L4-L3/iterate-while-with-prev-dissolution.md
# iterate-while-with-prev-dissolution

The L4>L3 lowering theme for the [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) combinator — the carry-bootstrapped (first-iteration-unrolled) sister of [`iterate-while`](../L4/iterate-while.md). It folds a `steady_step` over an initial carry while threading an additional `PrevCarry` closure parameter (the prior iteration's recurrence variable: CG's `beta_prev`, GMRES Hessenberg's `H_{k,k-1}`, Chebyshev's `x_{k-1}`), produced by an explicit `bootstrap_step` that fires exactly once before the steady loop. The theme dissolves the same L4 wrapper machinery as the no-prev dissolution (the `Solve` monad, the row-polymorphic `{ state: α, prev: β, ...e }` step return, the demand-prunable `trajectory` accumulator) **plus a fourth piece specific to this combinator**: the `prev` closure parameter dissolves into a positional argument of the L3 tail-recursive worker, and the bootstrap step becomes a non-recursive first call. It is the **dedicated home** for a Form-B rewrite that previously lived only as the firm L4 cap's own §"Lowers to" sketch (`iterate-while-with-prev.md:182-198`) plus a sub-component of [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" point 4 (`krylov-step-typed-wrapper-dissolution.md:74-89`).

This is the **carry-bootstrapped sister** of the companion theme `iterate-while-dissolution` (same cycle; the file lands together at integration — see the cross-reference note in §Context). The two themes share the entire wrapper-dissolution body; this chapter adds **only the `prev`-positional delta** (the bootstrap call + the closure-threaded `prev` becoming a positional tuple slot).

## Slug

`iterate-while-with-prev-dissolution`

## Context

The cycle-007 harvester promoted [`iterate-while`](../L4/iterate-while.md) and [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) to firm L4 rows (closing cycle-006 OQ `iterate-while-l4-anchor-missing`). The with-prev combinator's L4>L3 lowering was *described* — but only as (a) the firm L4 cap's own §"Lowers to" L3 sketch (`iterate-while-with-prev.md:182-198`), which the cap itself flags is "not yet authored as a standalone `book/src/L4-L3/iterate-while-with-prev-dissolution.md`" (`iterate-while-with-prev.md:200`), and (b) implicitly inside the Form-B treatment of [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) point 4 (`krylov-step-typed-wrapper-dissolution.md:74-89`), where the `iterate_while_with_prev` it consumes is dissolved as part of the krylov-step body rewrite. Neither is the combinator's **home**: a reader navigating from the firm `iterate-while-with-prev` row's §"Lowers to" finds an inline sketch with a self-acknowledged standalone-pending deferral. This chapter is that standalone theme.

This is an **extraction + re-homing**, not a fresh derivation. The bootstrap-then-tail-recursive L3 form, the §3.8 collapse rule, and the identity-in-form-on-body verdict are lifted (with citations) from the firm cap and the firm krylov-step sub-component; the new content is the layer-coherent framing — narrating the combinator's own L4→L3 dissolution forward, splitting the ground (unpruned) form from its pruned image cleanly, and isolating the **`prev`-positional delta** as the only difference from the companion `iterate-while-dissolution` theme.

### Companion theme — `iterate-while-dissolution`

This theme is the carry-bootstrapped specialisation of the companion theme `iterate-while-dissolution` (`book/src/L4-L3/iterate-while-dissolution.md`; authored the same cycle, lands together at integration). The companion covers the no-prev `iterate_while` dissolution; this theme is that pattern **plus** the `prev`-positional addition. The two are related by **Law 1 of [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md)** (`iterate-while-with-prev.md:129-135`): when `PrevCarry = ()` (`β = ()`), this combinator definitionally degenerates to `iterate_while` preceded by an outer identity bootstrap-step, so this theme's L3 form degenerates to the companion theme's L3 form. The companion is the `β = ()` specialisation; this theme is the strict generalisation. *(Same-cycle sibling: the cross-reference resolves to a live link once both files land together at integration; if the integrator applies this report before the companion, the link is a same-cycle forward reference per the rough-in-forward-reference convention — both land in one finalize.)*

## L4 form (LHS)

The L4 `iterate_while_with_prev` — the carry-bootstrapped, extras-carrying, `Solve`-threaded combinator consumed by [`krylov-step`](../L4/krylov-step.md) Form B (`iterate-while-with-prev.md:41-50`). This is the firm L4 row's `Solve`-threaded signature:

    iterate_while_with_prev
      :: (α -> Solve { state: α, prev: β, ...e })        -- bootstrap_step
      -> α                                                -- initial carry
      -> ((α, β) -> Solve { state: α, prev: β, ...e })    -- steady_step
      -> (α -> Bool)                                      -- cont
      -> Solve { final_state: α, trajectory: [{ ...e }] }

The argument order is `bootstrap_step` first, `init` second, `steady_step` third, `cont` fourth (`iterate-while-with-prev.md:52`). The small-step semantics are the bootstrap-then-tail-recurse rule from the firm L4 row's §Semantics (`iterate-while-with-prev.md:74-93`): fire the bootstrap once to produce the initial `prev` (`β_0`) and the bootstrap-stepped carry (`a_1`), then enter the steady tail recursion `steady_loop` (identical to `iterate_while`'s recursion modulo the `prev` threading):

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

The three load-bearing L4 properties the lowering must transport (`iterate-while-with-prev.md:97-103`):

1. **The bootstrap always runs** exactly once, before the predicate's first test — structural, because the predicate's first call needs a `prev`-threaded carry to inspect.
2. **The predicate fires after the bootstrap, before any steady step**, and reads the carry `α` only (never `prev`).
3. **The `prev` value is threaded as a closure parameter of the loop, not a field of the carry** — the load-bearing schema-narrowing the first-iteration-unrolling rotation buys.

The load-bearing demand-pruning property is **Law 2 — trajectory-pruning demand-rule** (`iterate-while-with-prev.md:137-147`, inherited from [`iterate-while`](../L4/iterate-while.md) Law 1 `iterate-while.md:123-133` and the strawman §3.8): when a consumer reads only `final_state`, the §3.8 rule rewrites **both** `bootstrap_step` and `steady_step` to the subgraphs computing only the `{ state, prev }` fields, omitting the extras. (This is Law 1's single-body rule lifted to two step bodies.)

The wrapper machinery this theme dissolves is **four** pieces (the three of the no-prev dissolution plus the `prev` closure thread):

1. **The `Solve` monad** — `Solve = StateT SimState Identity` (`book/src/concepts/solve-monad.md:1-68`). Both the bootstrap and each steady step discharge as `do`-blocks carrying the `SimState` `it` counter (`iterate-while-with-prev.md:105`).
2. **The row-polymorphic step return `{ state: α, prev: β, ...e }`** — a TypeScript-style record with a generic extras spread `...e`. L3 has no row-polymorphic record spread.
3. **The demand-prunable `trajectory: [{ ...e }]` accumulator** — the syntactic site where Law 2 fires; the bootstrap's extras are the first trajectory element.
4. **The `prev` closure parameter** — threaded by the combinator (not the slice) as a positional argument of `steady_step`, with the bootstrap producing its initial value. This is the **delta over the no-prev dissolution**.

## L3 form (RHS)

The L4>L3 dissolution produces a **bootstrap call followed by a tail-recursive value-threaded loop** with the `Solve` monad dissolved to an explicit positional `sim` thread, the record-spread step return dissolved to a positional tuple, and the `prev` closure parameter dissolved to a positional tuple slot. Two L3 forms arise from the **same** L4 invocation under different consumer demands; both share the bootstrap-then-loop shape extracted from the firm cap's §"Lowers to" (`iterate-while-with-prev.md:182-198`).

### Unpruned form — the trajectory-keeping ground form

The direct value-threaded dissolution when a downstream consumer reads `.trajectory` (no §3.8 collapse fires; the `[e₀] ++ trajectory` accumulator the firm L4 Law 2 keeps is materialised at L3). This is the **ground form** — the faithful L3 image of the bootstrap-then-`steady_loop` small-step rule with the trajectory preserved (extracted from `iterate-while-with-prev.md:182-198`; `sim` threading made positional, trajectory consed in iteration order):

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

where `f_boot_sp` / `f_steady_sp` are the §3.8-pruned `{state, prev}`-subgraphs of `f_boot` / `f_steady` — the bootstrap and steady bodies with the extras computation eliminated **as dead code at the call site** (not merely unused at runtime). The L3-side `f_steady_sp` has shape `(carry, prev, sim) -> (carry', prev', sim')` — the positional-tuple image of the L4-side `steady_step^{stateprev}` of Law 2 (`iterate-while-with-prev.md:137-147`), with the `sim` thread surfacing positionally because the `Solve` monad has dissolved, and `prev` surfacing as the dedicated positional slot. The trajectory is dropped entirely (no seed, no cons, no `reverse`).

### The collapse rule

The L4>L3 collapse from the unpruned ground form to the pruned form is governed by the L3-side image of Law 2:

$$
\frac{
  \text{only } \textsf{final\_state} \text{ of the L3 result is observed downstream}
}{
  \textsf{iterate\_while\_with\_prev\_L3}\ f_{\textsf{boot}}\ a_0\ f_{\textsf{steady}}\ p\ \textsf{sim}_0 \;\equiv\; \textsf{iterate\_while\_with\_prev\_L3\_pruned}\ f_{\textsf{boot}}^{\textsf{sp}}\ a_0\ f_{\textsf{steady}}^{\textsf{sp}}\ p\ \textsf{sim}_0
}
$$

This is exactly the L3-side image of **Law 2** of [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) (`iterate-while-with-prev.md:137-147`) — the L4 demand-pruning law **transports through** the L4>L3 wrapper dissolution because the dissolution is value-thread-isomorphic on **both** step bodies (the parent theme's §"Audit of cycle-002 identity-in-form claim", `krylov-step-typed-wrapper-dissolution.md:202-213`, establishes the body-identity that licenses the transport; the bootstrap and steady bodies are the Form-B first/steady pair audited there). The unpruned `iterate_while_with_prev_L3` is the ground form; the pruned `iterate_while_with_prev_L3_pruned` is its collapse-rule image; the rule above is the rewrite between them. **Framing** (identical to the companion theme): the pruned form is NOT a contradiction of the firm L4 Law 2 (which keeps the trajectory in its general statement) — it is the *consequence* of Law 2's collapse rule fired under a `final_state`-only consumer.

### Degeneracy to the companion dissolution

When `PrevCarry = ()` (`β = ()`), this combinator definitionally reduces to `iterate_while` preceded by an outer identity bootstrap (Law 1 of [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md), `iterate-while-with-prev.md:129-135`). At L3 this means: the `β` positional slot carries no information, the bootstrap call collapses to a pure carry-shift, and `iterate_while_with_prev_L3` degenerates to the companion theme's `iterate_while_L3` (`book/src/L4-L3/iterate-while-dissolution.md` §"L3 form (RHS)"), with the bootstrap's extras `[e₀]` becoming the trajectory's first element. This is the L3-side image of the L4 degeneracy law and is what makes the two themes a **family**: this theme is the strict generalisation, the companion is the `β = ()` specialisation.

### What does NOT change in the rotation

Both step bodies' primitive sequences survive the rotation textually unchanged — the dissolution is **identity-in-form on the bodies** (`krylov-step-typed-wrapper-dissolution.md:202-213`). The rotation touches only the **wrapper**: the `Solve` monad becomes positional `sim`, the record-spread step return becomes a positional tuple, the `prev` closure parameter becomes a positional tuple slot, the bootstrap becomes a non-recursive first call, and the trajectory becomes either an explicit list accumulator (unpruned) or nothing (pruned). The bootstrap and steady kernels — whatever the slice's per-step kernels are — pass through unchanged in their dataflow positions.

The **outer-loop `sequential-obstruction`** survives at L3: both L3 forms name the steady loop tail-recursively but do **not** claim it lifts to a global tensor-field op. This is the expected outcome for Krylov-family iterations at L3 per [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the live anchor is `book/src/spec/slices/arnoldi_step.md:194-213`. The bootstrap call is a single non-recursive step and carries no loop obstruction; only the steady tail recursion does. The unpruned form additionally allocates the `O(N)` trajectory accumulator; the pruned form does not.

### What this lowering does NOT cover

- **The L3>L2 hop on the loop combinator itself**, which is *also* identity-in-form per the combinator-miner cycle-002 assertion (`iterate-while-with-prev.md:202`), the same tail-recursive shape being L2-native. The full L4>L3>L2 chain for the no-extras `iterate_while_with_prev_pure` collapses to the L4>L3 wrapper dissolution alone; the L3>L2 completion is the trivial identity step, not duplicated here.
- **The no-prev `iterate_while` dissolution** — that is the companion theme `iterate-while-dissolution` (`book/src/L4-L3/iterate-while-dissolution.md`), which this theme generalises. When `β = ()` this theme degenerates to it (Law 1; see §"Degeneracy to the companion dissolution").
- **The slice-specialised dissolutions** — the GMRES / FGMRES inner-loop themes ([`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md), [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md)) specialise the no-prev `iterate_while` dissolution (those use Form A). The Form-B `iterate_while_with_prev` consumer is CG v0.5 (`book/src/spec/slices/cg.md:100-108`); a slice-specialised CG-Form-B dissolution would instantiate this theme's pruned form under the CG four-scalar consumer, but is not re-derived here.

## Applicability conditions

The rewrite is valid when all five of the following hold (the four inherited from `krylov-step-typed-wrapper-dissolution.md` §"Applicability conditions" plus the `prev`-threading condition specific to this combinator):

1. **The L4 `Solve` monad's effect domain is exactly `SimState`.** The only `modify` in either body is the `it` counter increment; no carry or `prev` field is monad-touched. This lets the monad dissolve to a single positional `sim` argument threaded through both the bootstrap and steady calls (`iterate-while-with-prev.md:105`, `solve-monad.md` §"What stays out of the monad").

2. **The predicate is pure on the carry** (`cont :: α -> Bool`, `iterate-while-with-prev.md:59`). No reads of `SimState`, `OpParams`, the per-step extras, or **the `prev` value** (the predicate-on-prev anti-pattern, `iterate-while-with-prev.md:115-123`). This is what lets the L3 branch test `not (p a)` read only the positional `carry` argument. Slices whose termination needs a `prev`-derived quantity fold it into the carry inside `steady_step` (CG v0.5: `s.converged` is set inside `cg_steady_step` from the freshly-computed `res'`; `beta_prev` is the `prev` parameter but is never read by the predicate; the predicate-on-carry-only is at `cg.md:101`, the `beta_prev`-as-`prev`-parameter at `cg.md:102-103`: `book/src/spec/slices/cg.md:101-103`).

3. **Both step bodies' primitive sequences are L3-native or carry their own L3 classification.** Each bootstrap/steady-body primitive is either a whole-tensor global op (L3-native by signature) or carries a documented body-level obstruction. The wrapper dissolution does not change either body's L3 classification — they survive in form.

4. **The bootstrap produces the initial `prev` and `sim`-threads exactly once.** The bootstrap call is non-recursive and runs before the predicate's first test (`iterate-while-with-prev.md:99` — "The bootstrap always runs"); the L3 form renders it as the let-bound prefix `(a₁, β₀, [e₀], sim₁) = f_boot (a₀, sim₀)`. If a slice needs an "already-converged-before-first-step" guard, it lives outside the combinator (CG v0.5's outer initial-convergence test, `book/src/spec/slices/cg.md:92`) and outside this lowering.

5. **Trajectory-pruning selection** (selects unpruned vs pruned form). When the downstream consumer reads `.trajectory` (or any per-step extras, including the bootstrap's), the **unpruned** `iterate_while_with_prev_L3` form is the rendered L3 shape. When the consumer observes only `final_state`-equivalent quantities, the **pruned** `iterate_while_with_prev_L3_pruned` form is the rendered shape (per the collapse rule above). For Palace's actual KSP consumer surface (the four-scalar consumer at `reference/palace/palace/linalg/iterative.hpp:52-55`, consumed solely at `reference/palace/palace/linalg/ksp.cpp:296-310`), the pruned form is the rendered shape; for a monitoring consumer that reads the residual history, the unpruned form is rendered.

## Justification kind

**`structural`** with secondary **`reduction-chain`**.

- **Structural** (dominant): the L4 wrapper machinery (Solve monad, `iterate_while_with_prev` combinator, extras-trajectory record, `prev` closure parameter, predicate-on-carry-only discipline) dissolves into an L3 bootstrap-call-plus-tail-recursive value-threaded form; both bodies' primitive sequences are preserved by construction (every L4 primitive call becomes an L3 primitive call at the same dataflow position). The `prev` closure parameter becomes a positional tuple slot; the bootstrap becomes a non-recursive prefix; the trajectory becomes an explicit accumulator (unpruned) or is dropped (pruned), both structural rewrites of the syntactic trajectory site.
- **Reduction-chain** (secondary): the `Solve` monad's `>>=` desugars to explicit positional `sim` threading in both the bootstrap and steady calls; the bootstrap-then-`steady_loop` small-step rule desugars to the let-bound prefix plus the tail-recursive `go` worker; the §3.8 pruning collapse from the unpruned to the pruned form is the mechanical application of Law 2's L3-side image to both bodies.

**Abstraction-direction note**: L4 is the higher-abstraction layer (typed records, monadic effect, closure-threaded `prev`, structural bootstrap-then-loop, demand-prunable trajectory); L3 is the lower-abstraction layer (positional values threaded explicitly, `prev` as a positional slot, bootstrap as a non-recursive prefix, branch-on-predicate in tail recursion, trajectory as explicit accumulator or dropped). The rotation direction is **L4 → L3**, narrated forward per the high→low discipline.

## Speculative L4 operators

None. This theme is an extraction of an already-firm form; the L4 cap it lowers ([`iterate-while-with-prev`](../L4/iterate-while-with-prev.md)) is a firm L4 row, and the companion no-prev combinator ([`iterate-while`](../L4/iterate-while.md)) is firm. No new speculative operator is introduced.

## Verified-against

L4 source (the LHS of this rewrite):

- `book/src/L4/iterate-while-with-prev.md:41-50` — the firm L4 `iterate_while_with_prev` `Solve`-threaded signature (the LHS); `:52` the argument order; `:74-93` the §Semantics bootstrap-then-`steady_loop` small-step rules; `:97-103` the three semantic points (bootstrap always runs / predicate after bootstrap / `prev` as closure parameter); `:129-135` Law 1 (degeneracy to `iterate-while` when `β = ()`); `:137-147` Law 2 (trajectory-pruning, the load-bearing transported property); `:182-198` the firm §"Lowers to" L3 form (`iterate_while_with_prev_L3` + `steady_loop_L3`) extracted as the RHS; `:202` the L3>L2 identity-in-form note; `:200` the standalone-pending deferral and `:223` the §"L4 vs L3 distinction" deferral, both re-anchored by this dispatch.
- `book/src/L4/iterate-while.md:123-133` — the companion Law 1 (single-body demand-pruning) that Law 2 lifts to two bodies; the rule transported through the dissolution.
- `book/src/design/l4_calculus.md:150-184` — the strawman §3.7 `iterate_while` small-step rule the bootstrap-then-loop semantics generalise (`:164-171` the rule block, `:179-182` the `iterate_while_pure` sugar).
- `book/src/design/l4_calculus.md:186-213` — the strawman §3.8 demand-driven pruning rule that underwrites Law 2.

L3 source (the RHS of this rewrite; extracted from the firm cap + firm sub-component):

- `book/src/L4/iterate-while-with-prev.md:182-198` — the firm L4 cap's own §"Lowers to" L3 form (`iterate_while_with_prev_L3` + `steady_loop_L3`), the bootstrap-then-tail-recursive ground shape extracted here.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:74-89` — the Form-B-in-L3 dissolution (`krylov-step-L3-first`/`krylov-step-L3-steady`, point 4): the `PrevCarry`-as-positional-value-in-the-threaded-tuple framing, extracted as the `prev`-positional delta.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:150-154` — the `iterate_while_with_prev` speculative-operator signature the Form-B body consumes (the bootstrap-step / steady-step split this theme renders positionally).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:202-213` — the §"Audit of cycle-002 identity-in-form claim" verdict that establishes the body-identity licensing the Law-2 transport for both bodies.
- `book/src/spec/slices/arnoldi_step.md:194-213` — the live `sequential-obstruction` anchor for the steady loop surviving at L3.

L0 consumer-surface evidence (selects the pruned form for Palace's KSP case, Condition 5):

- `reference/palace/palace/linalg/iterative.hpp:52-55` — the four-scalar KSP consumer surface; `reference/palace/palace/linalg/ksp.cpp:296-310` — the sole consumption site reading only `final_state`-equivalent quantities, which fires the §3.8 collapse to the pruned form.

Slice evidence (the Form-B consumer):

- `book/src/spec/slices/cg.md:100-108` — the canonical v0.5 CG slice using `iterate_while_with_prev` (the call site); the `cg_first_step` / `cg_steady_step` split (`:52-108`) is the prototypical bootstrap/steady pair; `:101-103` the predicate-on-carry-only (`:101`) + `beta_prev`-as-`prev`-parameter (`:102-103`) pattern. (Re-anchored from the firm L4 cap's historical `cg.md:441-446` citation, which predates the cycle-009 corpus reduction of the cg slice to 165 lines.)

Concept-page references:

- [`solve-monad`](../concepts/solve-monad.md) — the `Solve = StateT SimState Identity` monad that dissolves to the positional `sim` thread.
- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the rotation that hoists `prev` into the closure parameter this theme dissolves positionally.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra underwriting Law 2 and the collapse rule.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the steady loop's non-lift at L3.

## Status

`firm` — extraction of an already-firm form (the firm L4 cap's own §"Lowers to" `iterate-while-with-prev.md:182-198` + the firm sub-component `krylov-step-typed-wrapper-dissolution.md:74-89` point 4) into a dedicated layer-coherent chapter. The L4 cap it lowers ([`iterate-while-with-prev`](../L4/iterate-while-with-prev.md)) and the companion combinator ([`iterate-while`](../L4/iterate-while.md)) are firm L4 rows; the two L3 forms, the §3.8 collapse rule, the bootstrap-prefix shape, and the identity-in-form-on-bodies verdict are exhaustively cited against the strawman §3.7/§3.8, the firm L4 Law 1 / Law 2, and the parent theme's cycle-002 audit. Justification is `structural` + secondary `reduction-chain`. No speculative operator introduced. This chapter (with the companion `iterate-while-dissolution`) closes OQ `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor` (route-b realization) and addresses the D1-flagged `iterate-while-with-prev-lowers-to-reanchor-to-dedicated-dissolution-theme` follow-up.

## L4 vs L3 distinction

- **L4**: a single combinator with structural bootstrap-then-loop semantics, a closure-threaded `prev` parameter, and demand-pruning of the trajectory; both bodies' `Solve`-monad effect is orthogonal to the value-threaded carry and `prev`; the predicate is purely on the carry; the trajectory is materialised exactly when a downstream consumer reads it.
- **L3**: a non-recursive bootstrap prefix followed by a tail-recursive loop with explicit `(carry, prev, sim)` positional threading; the §3.8 pruning becomes a *call-site choice* between the unpruned `iterate_while_with_prev_L3` (trajectory materialised as an explicit accumulator seeded with the bootstrap extras) and the pruned `iterate_while_with_prev_L3_pruned` (trajectory dropped, both bodies rendered in their `{state, prev}`-only subgraphs). The L3 forms do not carry the bootstrap-then-loop *combinator name* or the pruning *rule*; they carry the *unrolled tail-recursive shape with the bootstrap as an explicit prefix* and the pruning's *resolved result* per consumer.

The two layers share signature shape (modulo wrapper dissolution) and small-step semantics on both bodies; they differ in **effect threading, `prev`-parameter placement, and demand-pruning placement**. The rotation erases the monadic packaging, positionalises the `prev` closure parameter, renders the bootstrap as a non-recursive prefix, and resolves the demand-pruning per consumer; it does *not* re-introduce the iteration-zero branch (the first-iteration-unrolling rotation is preserved across the lowering). Narrated forward L4→L3.
```

**Re-anchor 1 — `book/src/L4/iterate-while-with-prev.md` §"Lowers to" standalone-pending paragraph (`iterate-while-with-prev.md:200`).** Replace the exact on-disk paragraph beginning `As with [\`iterate-while\`](./iterate-while.md), the dedicated L4>L3 theme for this combinator is not yet authored as a standalone ...` (the full paragraph through `... this entry inherits the same disposition.`) with the replacement text in this block:

```edit:book/src/L4/iterate-while-with-prev.md
As with [`iterate-while`](./iterate-while.md), the dedicated L4>L3 theme for this combinator is now authored as the standalone chapter [`iterate-while-with-prev-dissolution`](../L4-L3/iterate-while-with-prev-dissolution.md) (cycle-047), the carry-bootstrapped sister of [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md). The dedicated theme captures **both** L3 forms: the **trajectory-keeping unpruned form** `iterate_while_with_prev_L3` — the bootstrap-then-tail-recursive ground form that materialises the `[e₀] ++ trajectory` accumulator this firm L4 form keeps (per Law 2) — and the **§3.8-pruned form** `iterate_while_with_prev_L3_pruned`, which is the collapse-rule image (Law 2's L3-side demand-pruning rewrite applied to both bodies under a `final_state`-only consumer). The earlier sub-component's trajectory-drop is the *pruned image*, not a gap in the firm L4 form; the unpruned ground form is what Law 2 keeps. See [`iterate-while-with-prev-dissolution`](../L4-L3/iterate-while-with-prev-dissolution.md) §"L3 form (RHS)" for the two forms, the `prev`-positional delta, and the collapse rule.
```

**Re-anchor 2 — `book/src/L4/iterate-while-with-prev.md` §"L4 vs L3 distinction" closing paragraph (`iterate-while-with-prev.md:223`).** Replace the exact on-disk paragraph beginning `Same effect-threading-and-demand-pruning-placement difference as [\`iterate-while\`](./iterate-while.md). The L4>L3 lowering erases the monadic packaging and resolves the demand-pruning per consumer; it does *not* re-introduce the iteration-zero branch (the rotation is preserved across the lowering).` with the replacement text in this block:

```edit:book/src/L4/iterate-while-with-prev.md
Same effect-threading-and-demand-pruning-placement difference as [`iterate-while`](./iterate-while.md). The L4>L3 lowering is the dedicated standalone theme [`iterate-while-with-prev-dissolution`](../L4-L3/iterate-while-with-prev-dissolution.md) (cycle-047; the carry-bootstrapped sister of [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md)) — it erases the monadic packaging, positionalises the `prev` closure parameter, renders the bootstrap as a non-recursive prefix, and resolves the demand-pruning per consumer; it does *not* re-introduce the iteration-zero branch (the rotation is preserved across the lowering).
```

**Re-anchor 3 — `book/src/L4/index.md:55` dep-map cell.** Replace the entire `iterate-while-with-prev` row (the table row beginning `| [\`iterate-while-with-prev\`](./iterate-while-with-prev.md) |`) — only its "Lowers to" sub-cell changes — with the full replacement row in this block:

```edit:book/src/L4/index.md
| [`iterate-while-with-prev`](./iterate-while-with-prev.md) | Pure: `(α -> { state: α, prev: β, ...e }) -> α -> ((α, β) -> { state: α, prev: β, ...e }) -> (α -> Bool) -> { final_state, trajectory }`. Solve-threaded form lifts the step bodies through `Solve`. Degenerates to [`iterate-while`](./iterate-while.md) when `β = ()` (Law 1). | Concepts: `first-iteration-unrolling`, `derived-view-hoisting`, `solve-monad`. L4 rows: [`iterate-while`](./iterate-while.md) (companion / degenerate case); consumed by [`krylov-step`](./krylov-step.md) Form B. | L3 bootstrap-then-tail-recursive value-threading form via the dedicated theme [`iterate-while-with-prev-dissolution`](../L4-L3/iterate-while-with-prev-dissolution.md) *(firm; cycle-047 abstractor extraction — carry-bootstrapped sister of `iterate-while-dissolution`; both unpruned `iterate_while_with_prev_L3` ground form and §3.8-pruned `iterate_while_with_prev_L3_pruned` form; the `prev` closure parameter dissolves to a positional slot and the bootstrap to a non-recursive prefix)*. | `firm` (harvested cycle-007T160550Z; closes cycle-006 OQ `iterate-while-l4-anchor-missing`) |
```

**Registration — `book/src/L4-L3/index.md` themes-table (own row).** Append the new theme row after the `fgmres-inner-loop-iterate-while-migration` row (block carries the existing row + the new row for anchoring; integrator appends only the new row). NOTE: the companion `iterate-while-dissolution` row (D1) also appends after this same `fgmres` row — the integrator's serial per-report apply handles the two distinct appended rows; this block carries ONLY my own (`iterate-while-with-prev-dissolution`) new row:

```edit:book/src/L4-L3/index.md
| [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) | Sister-form to the GMRES theme above, specialised for `FgmresSolver<OperType>` (`iterative.cpp:734-836`, `iterative.hpp:222-270`): `pc_side` pinned to `RIGHT` and `flexible` pinned to `true` at the constructor; unconditional `K { Z = K.Z `with` (K.j, z) }` carry-update; otherwise identical L4 form. | Sister-form to the GMRES L3 theme above, specialised for FGMRES: identical wrapper dissolution; body simplifies to the FGMRES collapsed shape (`pc_side`/`flexible` variant rows removed). Textually identical break-site at `iterative.cpp:823-828` (cycle-010 MCP-pilot audit). | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-011 lifter; same upstream gmres.md §L4 v0.6→v0.7 dependency as the GMRES sister) |
| [`iterate-while-with-prev-dissolution`](./iterate-while-with-prev-dissolution.md) | L4 [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) — the carry-bootstrapped (first-iteration-unrolled) combinator `(α -> Solve { state: α, prev: β, ...e }) -> α -> ((α, β) -> Solve { state: α, prev: β, ...e }) -> (α -> Bool) -> Solve { final_state, trajectory }`, with the bootstrap-then-`steady_loop` small-step rule, Law 1 (degeneracy to `iterate-while` when `β = ()`) and Law 2 (demand-driven trajectory pruning). The carry-bootstrapped sister of `iterate-while-dissolution`. | Bootstrap call (non-recursive prefix producing the initial `prev` `β₀`) plus a tail-recursive value-threaded loop, in two forms from the same invocation: the **unpruned** `iterate_while_with_prev_L3` ground form (materialises the `[e₀] ++ trajectory` accumulator seeded with the bootstrap extras) and the **§3.8-pruned** `iterate_while_with_prev_L3_pruned` collapse-rule image (drops the accumulator; both bodies rendered in their `{state, prev}`-only subgraphs); `Solve` monad dissolves to positional `sim` threading; record-spread step return dissolves to a positional tuple; the `prev` closure parameter dissolves to a positional slot. | `structural` + secondary `reduction-chain` | `firm` (cycle-047 abstractor; extraction + re-homing of the firm cap §"Lowers to" `iterate-while-with-prev.md:182-198` + the firm sub-component `krylov-step-typed-wrapper-dissolution.md:74-89`; carry-bootstrapped sister of `iterate-while-dissolution`; closes OQ `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor` jointly with D1, addresses D1-flagged `iterate-while-with-prev-lowers-to-reanchor-to-dedicated-dissolution-theme`) |
```

**Registration — `book/src/SUMMARY.md` (own line).** Append my own chapter line under the L4>L3 Part after the `fgmres-inner-loop-iterate-while-migration` line. NOTE: D1's `iterate-while-dissolution` line also lands here (distinct line); this block carries ONLY my own line for anchoring:

```edit:book/src/SUMMARY.md
- [fgmres-inner-loop-iterate-while-migration](./L4-L3/fgmres-inner-loop-iterate-while-migration.md)
- [iterate-while-with-prev-dissolution](./L4-L3/iterate-while-with-prev-dissolution.md)
```

## Speculative operators proposed

None. This theme is an extraction + re-homing of an already-firm form (the firm L4 cap's own §"Lowers to" `iterate-while-with-prev.md:182-198` + the firm sub-component `krylov-step-typed-wrapper-dissolution.md:74-89`). The L4 cap it lowers — [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) — and the companion combinator — [`iterate-while`](../L4/iterate-while.md) — are firm L4 rows (harvested cycle-007T160550Z). No new speculative operator is introduced, and no harvester promotion is required.

## Supporting evidence

- `book/src/L4/iterate-while-with-prev.md:182-198` — the firm L4 cap's own §"Lowers to" L3 form (`iterate_while_with_prev_L3` + `steady_loop_L3`): the bootstrap prefix (`:185`), the steady worker (`:189-195`), the trajectory-vs-no-trajectory note (`:198`). Extracted as the RHS ground form.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:74-89` — the Form-B-in-L3 dissolution point 4: `PrevCarry` becomes a positional value in the threaded tuple (`:74-79`), the Form-A/Form-B distinction collapses into carry-threading (`:89`). The `prev`-positional delta over the companion theme.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:150-154` — the `iterate_while_with_prev` speculative-operator rough-in signature (bootstrap / steady split) the Form-B body consumes.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:202-213` — the §"Audit of cycle-002 identity-in-form claim" verdict establishing the body-identity that licenses Law 2's transport through the wrapper dissolution (both bootstrap and steady bodies).
- `book/src/L4/iterate-while-with-prev.md` — the firm L4 LHS cap: §Signature (`:41-50`), argument order (`:52`), §Semantics small-step rules (`:74-93`), three semantic points (`:97-103`), Law 1 degeneracy (`:129-135`), Law 2 trajectory-pruning (`:137-147`), L3>L2 identity note (`:202`); §"Lowers to" standalone-pending deferral (`:200`) and §"L4 vs L3 distinction" deferral (`:223`) re-anchored by this dispatch; dep-map cell (`book/src/L4/index.md:55`) re-anchored.
- `book/src/L4/iterate-while.md:123-133` — the companion Law 1 (single-body demand-pruning) that Law 2 lifts to two bodies. (Citecheck note: the literal token "Law 1" does not appear at `:123-133` — that range carries the numbered item "1. **Demand-driven trajectory pruning**", which IS Law 1's content; the `[DRIFT]` flag on the literal `Law 1` anchor is a token-mismatch, not a range error. The range was confirmed by direct read.)
- `book/src/design/l4_calculus.md:150-184` (§3.7 `iterate_while` small-step rule, generalised by the bootstrap-then-loop semantics), `:186-213` (§3.8 demand-pruning, Law 2's source) — citecheck-confirmed.
- `reference/palace/palace/linalg/iterative.hpp:52-55` + `reference/palace/palace/linalg/ksp.cpp:296-310` — the Palace KSP four-scalar consumer surface that selects the pruned form (Condition 5).
- `book/src/spec/slices/cg.md:100-108` — the canonical v0.5 CG slice consuming `iterate_while_with_prev` (the prototypical Form B consumer; re-anchored from the firm cap's historical `cg.md:441-446` after the cycle-009 corpus reduction).
- `book/src/spec/slices/arnoldi_step.md:194-213` — the live `sequential-obstruction` anchor for the steady loop surviving at L3.

## Open questions / caveats

- **Companion-theme cross-reference is a same-cycle forward reference.** This theme links the companion `iterate-while-dissolution.md` (D1) repeatedly (§Context, §"Degeneracy to the companion dissolution", §"What this lowering does NOT cover"). D1's file is NOT yet on disk (it lands at integration as a `new:` block in D1's report); both files land together in the same finalize. The integrator should wire both `new:` blocks in one finalize so the cross-references resolve as live links; if the per-report apply order puts this report before D1's, the link is a same-cycle forward reference (per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention, which the stub/same-cycle carve-out covers — both land in one build). I have authored the links as live links with this note flagging the dependency for the integrator. (D1 used the same pattern for its cross-sibling refs.)
- **Extraction-not-pure-re-anchor flag (parallel to D1).** The bootstrap-then-tail-recursive L3 form, the collapse rule, and the identity-in-form verdict ARE extracted from the firm cap (`iterate-while-with-prev.md:182-198`) and the firm sub-component (`krylov-step-typed-wrapper-dissolution.md:74-89`) — the *code forms* are faithful renderings of the cap's `iterate_while_with_prev_L3`/`steady_loop_L3` (I positionalised the `sim` thread and seeded the trajectory with the bootstrap extras to match the §3.7 `[{...e₀}] ++ trajectory` prepend; the cap's `:182-198` form elides the `sim`-seeding detail). The new content is (a) the layer-coherent forward L4→L3 framing centred on the combinator; (b) the **ground-form-vs-collapse-image split** (the pruned form is Law 2's image, NOT a contradiction — identical framing to D1); (c) the explicit isolation of the **`prev`-positional delta** as the only difference from the companion theme + the Law-1 degeneracy tying the two; (d) the five-condition applicability section (the four inherited plus the bootstrap-once condition). The planner's route-b judgement holds.
- **OQ `iterate-while-l4-l3-standalone-theme-warranted-lifter-vs-abstractor` — CLOSED jointly with D1** (route-b realization). The route question (lifter re-anchor vs abstractor fresh theme) is resolved for both the no-prev and with-prev combinators: abstractor authored both dedicated chapters as extractions; no fresh derivation was needed beyond the re-homing framing.
- **D1-flagged follow-up `iterate-while-with-prev-lowers-to-reanchor-to-dedicated-dissolution-theme` — ADDRESSED by this dispatch.** D1 flagged that `iterate-while-with-prev.md` §"Lowers to" + dep-map cell warranted re-anchoring to a dedicated theme; this dispatch authors that theme AND performs the three re-anchors (§"Lowers to" `:200`, §"L4 vs L3 distinction" `:223`, dep-map cell `book/src/L4/index.md:55`). Recommend the integrator/meta-phase close this follow-up on landing.
- **Trajectory-accumulation reconciliation inherited.** The `iterate-while-with-prev.md:200` deferral inherited the OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` disposition from the companion entry; the same reconciliation applies (the trajectory-drop is the §3.8-pruned form, correct under a `final_state`-only consumer; the unpruned ground form here is what Law 2 keeps). D1 recommends closing that OQ on its landing; this dispatch's with-prev unpruned form is the with-prev half of the same reconciliation.
- **Citation self-verification.** All load-bearing L4/L3/strawman citation ranges were citecheck-confirmed pre-emit: with-prev §Signature `:41-50` ok, §Semantics `:74-93` ok, §"Lowers to" L3 form `:182-198` ok, L3>L2 identity `:202` ok, Law 1 `:129-135` ok, Law 2 `:137-147` ok; strawman §3.7 `:150-184` ok, §3.8 `:186-213` ok; krylov-step Form-B `:150-154` ok. The companion `iterate-while.md:123-133` Law-1 range was confirmed by direct read (the `[DRIFT]` flag was a literal-token mismatch on the anchor word "Law 1", not a range error — the numbered item "1. Demand-driven trajectory pruning" is verbatim at `:123-133`).
