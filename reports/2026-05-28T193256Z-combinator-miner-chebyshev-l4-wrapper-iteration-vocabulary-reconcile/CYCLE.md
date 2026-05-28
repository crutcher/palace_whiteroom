---
agent: combinator-miner
invoked_at: 2026-05-28T193256Z
scope: Pattern proposal — chebyshev-l4-wrapper-iteration-vocabulary-reconcile
status: integrated
integrated_at: 2026-05-29T003000Z
integration_commit: 73ecd3e
integration_notes: "cycle-014 position 4/8. REUSE/negative-result verdict — do NOT firm a new combinator; route (i) REUSE the iterate-while family (forM_/foldM → iterate_while_pure + step-count predicate). Applied only the dispatch-requested §Status resolution-path NOTE on L4/chebyshev.md (status NOT flipped, STAYS rough-in). The rough-in→firm flip + L4/index.md dep-map rewrite STAGED for cycle-015 (OQ chebyshev-l4-firm-via-iterate-while-reanchor → L4 firm 3→4; + chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev). The edit:book/src/L4/index.md block was follow-up-only, NOT applied. Build clean."
---

# CYCLE: Combinator candidate — fixed-count bounded iteration is `iterate_while_pure` with a step-count predicate (no new combinator)

## Summary

The cycle-013 `L4/chebyshev.md` rough-in renders its two sequential
obstructions as **un-anchored** `forM_` (outer `pc_it` Richardson sweep) and
`foldM` (inner `k`-degree recurrence) binds. The repairer correctly downgraded
the entry firm→rough-in because these combinators (i) have no L4 dep-map row,
(ii) have no concept page, and (iii) compete with the firm canonical
[`iterate-while`](../../book/src/L4/iterate-while.md) family, whose own entry
(`iterate-while.md:7`) declares itself "the **canonical iteration primitive** at
L4 … every iterative algorithm in the spec (CG, GMRES, **Chebyshev**, Arnoldi,
…) reduces at L4 to one or more `iterate_while`-folds."

**Pattern observed (route recommendation):** fixed-count bounded iteration —
loops with a *static* bound and **no convergence predicate** — is NOT a distinct
L4 primitive deserving its own row. It is the `iterate_while_pure` special case
where the predicate is a **step-count comparison** (`s.it <= bound`) with the
loop counter folded into the carry. The L4 strawman **already commits to exactly
this** at §6.5 step 5: the bunsen LBM `for t_idx in 1..=k` bounded loop "uses
`iterate_while_pure` with `s.step < maxSteps` as the continuation predicate,
encoding the `k`-step bound inside the state and the predicate"
(`l4_calculus.md:418`; the `run_lbm` worked example at `:382-385` is the live
call shape). Chebyshev's two loops are structurally **identical** to that LBM
loop: bounded `[1 .. pc_it]` / `[1 .. order-1]`, no predicate on a residual, no
inner-product. The cycle-013 `forM_`/`foldM` rendering is a verbatim promotion of
the cycle-001-era pre-redirect slice §L4 (`spec/slices/chebyshev.md:289,325,
396-397`) that pre-dates the firm `iterate-while` family (cycle-007) and was
never reconciled.

**Route: (i) REUSE the `iterate-while` family; do NOT firm a new combinator.**
Per the coalesce-by-use / lower-level-shared-vocabulary-takes-priority
invariants, `forM_`/`foldM` capture **no genuinely distinct aspect** that
`iterate_while_pure` does not already cover: the "fixed-count vs.
convergence-gated" distinction is a property of the **predicate** (`s.it <=
bound` vs. `not s.converged`), not of the combinator. The combinator is the same
tail-recursive value-threading fold; only the predicate differs. Firming a
parallel bounded-iteration row would inflate the L4 iteration vocabulary from
two members to four for zero algebraic gain and would directly contradict
`iterate-while.md:7`'s load-bearing canonical-primitive claim.

**Layer: L4 (no new row).** The proposal is a *re-anchoring* of an existing
rough-in entry onto existing firm vocabulary, plus one optional concept-page
clarification (the "step-count-predicate" idiom) if same-layer-cross-cutter
later wants a shared anchor. It is **not** a new operator.

## Pattern instances

Fixed-count bounded iteration (static bound, no convergence predicate, rendered
canonically as `iterate_while_pure` with a step-count predicate):

- **Instance 1 — Chebyshev outer sweep** (`L4/chebyshev.md:137`, the
  `forM_ [1 .. op.pc_it]`). Pure bounded counter; the only cross-step linkage is
  the monadic `y` accumulator (`modifyY`), which threads through the `Solve`
  monad orthogonally to the value-carry (exactly the `iterate-while`
  Solve-threaded-body discipline, `iterate-while.md:59` placement-rule 3). →
  `iterate_while_pure` over a carry `{ it: Int, sweep_first: Bool }` with
  predicate `\s -> s.it <= op.pc_it`. L0: `chebyshev.cpp:191` `for (int it = 0;
  it < pc_it; it++)` (verified via cycle-013 critic).

- **Instance 2 — Chebyshev inner k-recurrence** (`L4/chebyshev.md:148`, the
  `foldM (innerStep op) (r0, d0, st0) [1 .. op.order - 1]`). Threads a genuine
  value carry `(r, d, st)` — `st` is the previous-iteration scalar-recurrence
  variable (`rho_prev` for 1st-kind). Bounded by `order-1`, no residual test. →
  `iterate_while_pure` over a carry `{ r, d, st, k: Int }` with predicate
  `\c -> c.k <= op.order - 1`. The `st`/`rho_prev` carry is the same shape as the
  CG `beta_prev` recurrence variable — which `iterate-while-with-prev` was firmed
  (cycle-007) precisely to thread; this inner loop is a candidate for the
  with-prev form if same-layer-cross-cutter prefers the schema-narrowed
  presentation (see Variant axes). L0: `chebyshev.cpp:200` `for (int k = 1; k <
  order; k++)`.

- **Instance 3 — bunsen LBM time-step loop** (the strawman's own worked example,
  `l4_calculus.md:382-385` + the L3↔L4 correspondence at `:402-418`). The
  `for t_idx in 1..=k` bounded loop maps to `iterate_while_pure initial (\s ->
  s.step < maxSteps) (\s -> lbm_step …)`. This is the **strawman-canonical
  precedent** that fixed-count loops are `iterate_while_pure` with a step-count
  predicate, decided at strawman v0.3. It is the direct authority for Instances
  1–2.

- **Instance 4 (consumer, not yet authored) — L3 `chebyshev` partial-obstruction
  loops** (`L3/chebyshev.md:231-233` `itloop` and `:221-230` `kloop`, the cycle-013 L3
  row). These are the L3 tail-recursion renderings of the same two loops; the L3
  form is the lowering image of whichever L4 vocabulary is chosen, so re-anchoring
  the L4 entry keeps the L4>L3 dissolution clean (the L3 `itloop`/`kloop` are
  already the `iterate_while_pure_L3` shape at `iterate-while.md:193-195`).

Four instances (3 firm-vocabulary call shapes + 1 lowering consumer); well above
the ≥3 soft bar. The pattern is "fixed-count bounded iteration → step-count
predicate," and the firm combinator already exists.

## Proposed combinator

- **Slug**: *(no new slug)* — the candidate is the **negative result**: do NOT
  add a `for-m`/`fold-m`/`bounded-iterate` row. Reuse
  [`iterate-while`](../../book/src/L4/iterate-while.md) /
  [`iterate-while-with-prev`](../../book/src/L4/iterate-while-with-prev.md) via
  the `iterate_while_pure` sugar with a step-count predicate.
- **Layer**: L4 (re-anchoring of the existing rough-in `L4/chebyshev.md`; no new
  layer entry). **Why not a new row:** the would-be combinator's only distinction
  from `iterate_while_pure` is the predicate shape (`s.it <= bound` vs.
  convergence). `iterate-while.md` §Signature predicate-discipline 1
  (`:57`/`:102`) and §Variant-axes already cover bounded `max_it`-folded-into-the-
  carry predicates (`cg.md:217` `s.it < config.max_it && not s.converged`). A
  separate row would duplicate the fold semantics and break the canonical-primitive
  claim. **Why L4, not adjacent:** the obstruction is a wrapper-vocabulary
  mismatch at L4 only; L3 already renders the loops as `iterate_while_pure_L3`-shape
  tail recursions, and L2 has the iteration view erased.

- **Signature sketch** (the re-anchored `apply` body; firms up by harvester/lifter
  follow-up). The `forM_`→outer `iterate_while_pure`, `foldM`→inner
  `iterate_while_pure`, both with step-count predicates and the `y` accumulator
  threaded by the `Solve` monad:

  ```text
  apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()
  apply op initial_guess = do
    x <- readX
    -- outer pc_it sweep: step-count predicate, counter folded into carry
    _ <- iterate_while_pure
           { it: 1 }                                  -- carry: bounded counter only
           (\s -> s.it <= op.pc_it)                   -- step-count predicate (NOT convergence)
           (\s -> do { sweepM op initial_guess s.it; { it: s.it + 1 } })
    pure ()
    where
      -- one Richardson sweep; the y accumulator is the Solve-monad effect
      sweepM op ig it = do
        r0 <- if it == 1 && not ig
                then do { writeY zero; pure x }
                else do { y <- readY; ay <- applyLinop op.A y; pure (x .-. ay) }
        let { α₀: c0, st: st0 } = op.scalars 0 op.scalarInit
        let d0 = c0 .* (op.dinv .*. r0)
        -- inner k-recurrence: step-count predicate, (r,d,st) value-threaded carry
        cN <- iterate_while_pure
                { r: r0, d: d0, st: st0, k: 1 }       -- carry: recurrence tuple + counter
                (\c -> c.k <= op.order - 1)           -- step-count predicate
                (\c -> do
                   modifyY (\y -> y .+. c.d)          -- y += d   (Solve effect)
                   ad <- applyLinop op.A c.d
                   let r' = c.r .-. ad
                   let { sd, sr, st: st' } = op.scalars c.k c.st
                   let t  = op.dinv .*. r'
                   let d' = sd .* c.d .+. sr .* t
                   { r: r', d: d', st: st', k: c.k + 1 })
        modifyY (\y -> y .+. cN.d)                     -- final accumulate
  ```

  (`iterate_while_pure` here is the Solve-threaded sugar: the `y` accumulator is
  the orthogonal `SimState`/`ChebSim` effect; the value-carry is `{r,d,st,k}`.
  Trajectory is uniformly empty — the smoother is convergence-test-free and
  inner-product-free, so there are no per-step extras, matching the strawman's
  `iterate_while_pure` no-extras case `l4_calculus.md:176-182`.)

- **Algebraic intuition**: the carry-counter form makes the step-count predicate
  a **bounded `iterate_while`**, which is *total* by construction (`s.it <=
  bound` strictly increments `it`, so the predicate becomes false in `bound`
  steps — discharging the `iterate-while.md` Law "Termination guarantee" totality
  obligation `:165` via the bounded-`max_it`-folded-into-carry discharge). No
  identity element, no fold-merge across the two loops (the outer-sweep
  non-commutativity is inherited from the L1/L2 non-laws; same as
  `iterate-while.md`'s no-step-composition non-law `:155`). The inner loop's `st`
  carry is exactly the previous-iteration recurrence-variable shape that
  `iterate-while-with-prev` Law 1 names.

- **Variant axes**:
  - *predicate shape* — step-count (`s.it <= bound`) vs. convergence
    (`not s.converged`). This is the axis that distinguishes Chebyshev from
    krylov-step, and it lives **in the predicate**, not the combinator. (This is
    the load-bearing argument for route (i).)
  - *inner-loop presentation* — plain `iterate_while_pure` over `{r,d,st,k}`
    (carry holds `st`) **vs.** `iterate_while_with_prev` threading `st`/`rho_prev`
    as the closure `prev` parameter (schema-narrowed carry `{r,d,k}`). Both are
    valid; the with-prev form mirrors the CG `beta_prev` treatment. Defer the
    choice to the firming follow-up (harvester/lifter) — flag for
    same-layer-cross-cutter if it wants to unify the `st`-carry with the
    `beta_prev`-carry under one recurrence-variable-threading note.

## Proposed changes

This report does **not** create a new operator file and does **not** mutate
`book/`. It records the route decision; the firming follow-up (cycle-015
lifter/abstractor) applies the re-anchor. The dep-map row for `L4/chebyshev`
already exists (cycle-013) with the `iteration combinators UNRECONCILED` flag;
the follow-up rewrites that cell rather than appending a new row. The
rough-in-entry that this proposal *resolves* is the existing
`book/src/L4/chebyshev.md` (not a new candidate), so the dep-map edit below is a
**replacement** of the existing `chebyshev` row's Dependencies + Status cells,
staged for the follow-up (NOT applied here):

```edit:book/src/L4/index.md
[follow-up (cycle-015 lifter/abstractor) — replace the `chebyshev` row's
 Dependencies cell "L4 rows: **iteration combinators UNRECONCILED** …" with:
 "L4 rows: [`iterate-while`](./iterate-while.md) (via `iterate_while_pure` with a
  **step-count predicate** `s.it <= bound`, per strawman §6.5 step 5
  `l4_calculus.md:418`; outer `pc_it` sweep and inner `k`-recurrence both); the
  inner `st`/`rho_prev` recurrence-carry may alternatively use
  [`iterate-while-with-prev`](./iterate-while-with-prev.md) (see entry §Variant
  axes)." — and flip Status `rough-in`→`firm`, moving chebyshev from the
 "Rough-in at L4 (1)" cohort into "Firm at L4" (count 3→4), per
 combinator-miner:2026-05-28T193256Z route (i).
 (reconcile, proposed-by: combinator-miner:2026-05-28T193256Z)]
```

The body re-anchor of `L4/chebyshev.md` §Signature/§Semantics (the
`forM_`/`foldM` → `iterate_while_pure`-with-step-count-predicate rewrite sketched
above) is the substantive authoring step — that is the **lifter/abstractor
follow-up's** work (re-deriving the carry-record design + predicate formulation +
effect interleaving), exactly as the cycle-013 repairer scoped it
(META.md "Unrepairable findings" → routed to combinator-miner/lifter). This
report supplies the route + the concrete body sketch so the follow-up is a
mechanical application rather than a re-investigation.

## Supporting evidence

- `book/src/L4/iterate-while.md:7` — canonical-iteration-primitive claim naming
  Chebyshev as a consumer (the load-bearing constraint route (i) satisfies).
- `book/src/L4/iterate-while.md:176-182, 193-195` — the `iterate_while_pure`
  no-extras sugar + its L3 tail-recursion image (the L4>L3 lowering the L3
  `chebyshev` `itloop`/`kloop` already match).
- `book/src/L4/iterate-while.md:57, 102, 165` — predicate-discipline (counter
  folded into carry) + bounded-`max_it` totality discharge: the step-count
  predicate is an already-covered predicate shape, not a new combinator.
- `book/src/design/l4_calculus.md:418` — **strawman §6.5 step 5**: bounded
  `for t_idx in 1..=k` → `iterate_while_pure` with step-count predicate. The
  decisive precedent.
- `book/src/design/l4_calculus.md:376-385` — `run_lbm` worked example: the live
  `iterate_while_pure … (\s -> s.step < maxSteps) …` call shape (Instance 3).
- `book/src/L4/chebyshev.md:137,148` — the two un-anchored `forM_`/`foldM` binds
  (Instances 1–2); §Status (lines 400-419) carries the cycle-013 repairer caveat
  + OQ 6 routing this dispatch.
- `book/src/L3/chebyshev.md:221-233` — the L3 `kloop` (`:221-230`) / `itloop`
  (`:231-233`) tail recursions (Instance 4; already `iterate_while_pure_L3`-shaped).
- `book/src/L4/iterate-while-with-prev.md:3,9,129-135` — the with-prev form names
  Chebyshev `x_{k-1}` as a recurrence-variable consumer; the `st`/`rho_prev`
  inner carry is the same shape (the optional inner-loop presentation variant).
- `reports/2026-05-28T143923Z-harvester-l3-l4-chebyshev-rows-eligible/META.md`
  (critic + repairer) — issue 1 (the central un-anchored-vocabulary finding),
  repairer downgrade firm→rough-in, "Unrepairable findings" routing to
  combinator-miner, "Suggested resolution" naming strawman §6 + `iterate-while.md:7`
  as the canonical target (this report selects that target).
- `palace/linalg/chebyshev.cpp:191` (outer `for it`), `:200` (inner `for k`) —
  the L0 bounded `for`-loops (verified via cycle-013 critic codemap reads); both
  are static-bound, no convergence test.

## Open questions / caveats

1. **Inner-loop presentation (`iterate_while_pure` carry-`st` vs.
   `iterate-while-with-prev` closure-`prev`)** — both are firm-vocabulary-valid.
   The with-prev form narrows the carry to `{r,d,k}` and threads `rho_prev` as the
   closure `prev`, mirroring CG `beta_prev`; the plain form keeps `st` in the
   carry. I recommend the **plain `iterate_while_pure` with `st` in the carry**
   as the default (4th-kind's `st = ()` makes it the degenerate no-prev case, so
   the carry-`st` form unifies both kinds without a bootstrap step), and flag the
   with-prev alternative for same-layer-cross-cutter if it wants to unify the
   `st`-carry with the `beta_prev`-carry. Deferred to the firming follow-up.

2. **Does re-anchoring need a `concepts/` "step-count-predicate" / "bounded-
   iteration" page?** Probably not — `iterate-while.md` §Signature already
   documents the counter-folded-into-carry discipline. But if a third fixed-count
   consumer surfaces (e.g. a transient fixed-step time-loop, or arnoldi's
   fixed-restart-dimension loop), a one-paragraph concept note "fixed-count
   bounded iteration is `iterate_while_pure` + step-count predicate" might be
   worth a layer-intro-author sideways emission. Filing as a watch-item, not a
   proposal (only 2 firm consumers today: Chebyshev + LBM).

3. **The `forM_`/`foldM` names are not strictly wrong as Haskell sugar** — in a
   real Haskell rendering `forM_ [1..n]` and `foldM` ARE the idiomatic bounded
   loops. The objection is **L4-vocabulary-coherence**, not Haskell correctness:
   L4 is a closed calculus whose iteration vocabulary is the `iterate-while`
   family (strawman §3.7 + the two firm rows), and admitting `forM_`/`foldM` as a
   second, un-reduced iteration vocabulary breaks the "every iterative algorithm
   reduces to `iterate_while`" invariant. Route (i) keeps the calculus closed. If
   a future cycle wants `forM_`/`foldM` as *surface sugar that desugars to
   `iterate_while_pure`*, that is a strawman §-addition (a desugaring rule), not a
   new L4 row — and still not this dispatch's call.

4. **CYCLE.md filename filter** — no filter block encountered writing this
   `CYCLE.md` (the canonical post-rename filename). Surfaced here per role-spec
   instruction only as confirmation that the write path is clean.
