# iterate-while-with-prev

The carry-bootstrapped variant of [`iterate-while`](./iterate-while.md): folds a `Step` function over an initial `carry` value while threading an additional `PrevCarry` closure parameter — the previous iteration's recurrence-variable value — produced by an explicit `bootstrap_step` and updated by each `steady_step` invocation. Used exactly where the [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) rotation has hoisted a `_prev` field out of the steady-state carry and into the loop driver as a closure parameter.

## Context

The rotation [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) splits an iteration `iterate_while s_0 cond step` whose step body contains `if it == 0 then base_case else recurrence(prev_state_field)` into a straight-line bootstrap (`first_step`) producing the initial value of the recurrence variable, plus a branch-free `steady_step` consuming the recurrence variable as a *closure parameter of the loop driver*. The driver for the branch-free steady iteration is `iterate_while_with_prev`.

The combinator is needed because the recurrence variable (CG: `beta_prev`; GMRES Hessenberg: `H_{k,k-1}`; Chebyshev: `x_{k-1}`) must flow from each step to the next, but is *not* part of the steady-state carry's schema — it lives in the loop driver's closure to keep the steady carry one slot lighter. The L4 calculus admits this directly via a generic carry-bootstrapped tail recursion; the combinator just names the shape.

Per [`first-iteration-unrolling.md:34-37`](../concepts/first-iteration-unrolling.md), the rotation's natural driver is exactly this combinator. The cycle-006 wave-1 harvester on `krylov-step` adopted Form B (`first_step` / `steady_step`) without an L4 anchor for the driver; the cycle-006 wave-2 abstractor on `krylov-step-typed-wrapper-dissolution` flagged the same missing anchor (§"Speculative L4 operators"). This chapter is the missing anchor; the cycle-006 OQ `iterate-while-l4-anchor-missing` is closed jointly by this entry and the companion [`iterate-while`](./iterate-while.md) entry.

`iterate_while_with_prev` at L4 is a **methodology-level combinator**, not a Palace-source artefact. Palace's source contains the unrolled form's *opposite* — the in-step `if (!it)` branch (`reference/palace/palace/linalg/iterative.cpp:434-441`), with the recurrence variable `beta_prev` carried in the per-step local-variable scope rather than the iteration's data structure. The L4 form's hoisted closure parameter is the **presentation rotation** named at [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md), not a Palace source artefact; the L0 evidence is the in-step branch that the rotation removes.

## Signature

The signature is the closure-carry-bootstrapped value-threading combinator shape, parameterised by the carry type `α`, the prev-carry type `β`, the readout-extras type `e`, and the implicit `Solve` monad.

**Form (pure, no `Solve` threading)**:

```text
iterate_while_with_prev_pure
  :: (α -> { state: α, prev: β })            -- bootstrap_step
  -> α                                        -- initial carry
  -> ((α, β) -> { state: α, prev: β })       -- steady_step
  -> (α -> Bool)                              -- cont
  -> α
```

**Form (extras-carrying, pure)**:

```text
iterate_while_with_prev
  :: (α -> { state: α, prev: β, ...e })       -- bootstrap_step
  -> α                                        -- initial carry
  -> ((α, β) -> { state: α, prev: β, ...e })  -- steady_step
  -> (α -> Bool)                              -- cont
  -> { final_state: α, trajectory: [{ ...e }] }
```

**Form (Solve-threaded, extras-carrying)** — the form consumed by [`krylov-step`](./krylov-step.md) Form B:

```text
iterate_while_with_prev
  :: (α -> Solve { state: α, prev: β, ...e })       -- bootstrap_step
  -> α                                              -- initial carry
  -> ((α, β) -> Solve { state: α, prev: β, ...e })  -- steady_step
  -> (α -> Bool)                                    -- cont
  -> Solve { final_state: α, trajectory: [{ ...e }] }
```

Note the argument order: `bootstrap_step` first, `init` second, `steady_step` third, `cont` fourth. This is the canonical order in which a slice's solve function builds the call — bootstrap-shape comes first (it determines the initial `prev` value), then the initial carry, then the steady-step body, then the predicate. The order matches `cg.md:441-446` (where the v0.5 CG solve passes `cg_first_step opA eps s0` first, builds `s1`, and then folds with `cg_steady_step opA eps`). The arity is fixed (no Haskell-style currying ambiguity at the combinator level). The `steady_step` closure-argument order `(α, β)` (carry first, prev second) matches both the `first-iteration-unrolling.md:34-37` pseudo-code (`\(s, carry) -> ...`) and the CG v0.5 call site (`\(s, beta_prev) -> ...` at `cg.md:443`) — state-then-prev is the canonical convention.

Shape contract (bunsen-style; the `α`, `β`, `e` slots are arbitrary L4 types instantiated per use):

- **`bootstrap_step: α -> { state: α, prev: β, ...e }`** — the bootstrap body that fires exactly once before the steady loop begins. Produces the next carry `state` *and* the initial value of the `prev` closure parameter that `steady_step` will consume. May also produce per-step extras `e`, which prepend the trajectory list (matching the CG v0.5 pattern at `cg.md:446` where `[res1] ++ trajectory.map(...)` is the residual-history shape). If the slice's bootstrap is genuinely no-extras, `e = ()`.
- **`init: α`** — the carry passed to the bootstrap step. Typically constructed by the slice's `<algo>_init` function from `OpParams` and inputs. Same role as the initial carry to [`iterate-while`](./iterate-while.md).
- **`steady_step: (α, β) -> { state: α, prev: β, ...e }`** — the branch-free steady-state body. Consumes the current carry as its *first* argument, the prior step's `prev` value as its *second* argument (the closure parameter being threaded). Produces the next `state`, the next `prev` (to thread to the next call), and the per-step extras. The body is required to be branch-free w.r.t. the iteration-zero special case — per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md), the whole point of the rotation is that the iteration-zero branch is gone from the steady body. (The combinator does not enforce this; it is a slice-level discipline.)
- **`cont: α -> Bool`** — the loop predicate. Reads the carry only; identical role to [`iterate-while`](./iterate-while.md)'s `cont`. Does *not* read the `prev` value; if the predicate cares about a quantity derived from `prev`, the slice folds it into the carry. The predicate fires before each `steady_step` call (not before `bootstrap_step` — the bootstrap always runs, by construction). It *does* fire after the bootstrap, before any steady step, to handle the "bootstrap already converged" case (see Semantics §3 below).
- **`extras: { ...e }`** — same role as in [`iterate-while`](./iterate-while.md): per-step readout records, demand-prunable per §3.8.
- **result `{ final_state: α, trajectory: [{ ...e }] }`** — the final carry value plus the trajectory of per-step extras *including the bootstrap's extras* as the first element. Demand-pruning works the same way as [`iterate-while`](./iterate-while.md); when only `final_state` is read, both `bootstrap_step` and `steady_step` are rewritten to drop their extras computations.

The signature makes two things structural that the in-step-branch form (without the rotation) leaves implicit:

1. **The bootstrap is structurally distinct from the steady-state step.** Two named functions with two different signatures — the bootstrap has no `prev` input (because there is no prior iteration to thread from); the steady step does. The L4 typing forbids passing `bootstrap_step` where `steady_step` is expected and vice versa. This is the structural realisation of the [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) call-site obligation.
2. **The `prev` closure parameter is threaded by the combinator, not by the slice.** The slice's `steady_step` body sees `prev` as a positional argument and produces the next `prev` in its return record; the combinator handles the threading. The slice does not write the `let prev' = ... in let result = steady_step (prev', s) in ...` plumbing — the combinator does. (Contrast with naive expansions where each slice would re-implement the carry-threading.)

## Semantics

`iterate_while_with_prev` at L4 is the bootstrap-then-tail-recurse variant of [`iterate-while`](./iterate-while.md). The small-step rule fires the bootstrap first, then the predicate, then enters the steady tail recursion (which is identical to [`iterate-while`](./iterate-while.md)'s recursion modulo the `prev` threading).

**Reduction rule** (pure form):

$$
\begin{aligned}
\textsf{iterate\_while\_with\_prev}\ f_{\textsf{boot}}\ a_0\ f_{\textsf{steady}}\ p &\;\to\; \\
&\textsf{let}\ \{\textsf{state}: a_1,\ \textsf{prev}: \beta_0,\ \dots e_0\} = f_{\textsf{boot}}(a_0)\ \textsf{in} \\
&\textsf{let}\ \{\textsf{final\_state},\ \textsf{trajectory}\} = \textsf{steady\_loop}\ a_1\ \beta_0\ f_{\textsf{steady}}\ p\ \textsf{in} \\
&\{\textsf{final\_state},\ \textsf{trajectory}: [\{\dots e_0\}] \mathop{++} \textsf{trajectory}\}
\end{aligned}
$$

where the auxiliary `steady_loop` is the tail-recursive worker:

$$
\begin{aligned}
\textsf{steady\_loop}\ a\ \beta\ f\ p &\;\to\; \textsf{if}\ p(a) \\
&\quad \textsf{then}\ \textsf{let}\ \{\textsf{state}: a',\ \textsf{prev}: \beta',\ \dots e\} = f(a, \beta)\ \textsf{in} \\
&\quad\quad \textsf{let}\ \{\textsf{final\_state},\ \textsf{trajectory}\} = \textsf{steady\_loop}\ a'\ \beta'\ f\ p\ \textsf{in} \\
&\quad\quad \{\textsf{final\_state},\ \textsf{trajectory}: [\{\dots e\}] \mathop{++} \textsf{trajectory}\} \\
&\quad \textsf{else}\ \{\textsf{final\_state}: a,\ \textsf{trajectory}: [\,]\,\}
\end{aligned}
$$

Read in prose: bootstrap to produce the initial `prev` (`β_0`) and the bootstrap-stepped carry (`a_1`); then enter the steady loop, threading `prev` through each step's argument-and-return until the predicate fires `False` on the current carry; trajectory accumulates bootstrap-extras-then-steady-extras-in-iteration-order.

Three semantic points worth pinning explicitly:

1. **The bootstrap always runs.** Unlike [`iterate-while`](./iterate-while.md), where the predicate fires before any step, `iterate_while_with_prev` *always* fires `bootstrap_step` exactly once, before testing the predicate. This is structural: the predicate's first call needs a `prev`-threaded carry to inspect, and `bootstrap_step` is the only way to produce one. If the slice's algorithm has an "already-converged-before-first-step" case, the slice handles it outside the combinator (see `cg.md:433-434` for the CG pattern: `if sqrt (abs s0.beta) < eps then { ..., converged: True } else <iterate_while_with_prev call>`).

2. **The predicate fires after the bootstrap, before any steady step.** This means a bootstrap that itself converges (e.g., `cg_first_step` producing an `s1` with `s1.converged = True`) results in zero steady steps; the trajectory contains only the bootstrap's extras; `final_state = s1`. Slices that test for this case can do so outside the combinator (CG v0.5 does, at `cg.md:437`: `if s1.converged || s1.it >= config.max_it then { ..., residual_history: [res1] } else <iterate_while_with_prev>`); the combinator also handles it correctly if the slice trusts the predicate to fire `False` on `s1`.

3. **The `prev` value is threaded as a closure parameter of the loop, not as a field of the carry.** The Form B harvester signature names this distinction structurally; this combinator realises it. The carry `α` does not contain a `prev` field; the `prev` value lives in `steady_step`'s positional argument and the combinator's recursion. This is the load-bearing schema-narrowing that the first-iteration-unrolling rotation buys — per `first-iteration-unrolling.md:39-49`, the state schema is one slot lighter, the steady-step body is branch-free, and the precondition that would have triggered the iteration-zero branch is discharged statically by `bootstrap_step`'s construction.

The `Solve`-threaded form lifts mechanically through the `Solve` monad's `>>=`, identically to [`iterate-while`](./iterate-while.md) — the bootstrap and each steady-step call discharge as `do`-blocks; the trajectory accumulation is purely positional. No new monadic-effect placement issues arise.

The `iterate_while_with_prev_pure` sugar (no-extras case) is the analogous shortcut:

$$
\textsf{iterate\_while\_with\_prev\_pure}\ f_{\textsf{boot}}\ a_0\ f_{\textsf{steady}}\ p \;\equiv\; (\textsf{iterate\_while\_with\_prev}\ f'_{\textsf{boot}}\ a_0\ f'_{\textsf{steady}}\ p)\textsf{.final\_state}
$$

where $f'_{\textsf{boot}}(a) = \{\textsf{state}: f_{\textsf{boot}}(a).\textsf{state},\ \textsf{prev}: f_{\textsf{boot}}(a).\textsf{prev}\}$ and similarly for $f'_{\textsf{steady}}$ (extras erased to `()`).

### Predicate-on-prev anti-pattern

Mirror of the [`iterate-while`](./iterate-while.md#predicate-on-extras-anti-pattern) anti-pattern: a tempting but wrong sketch is to let the predicate inspect the threaded `prev` value:

```text
iterate_while_with_prev_BAD :: ... -> (α -> β -> Bool) -> ...
```

This typechecks but introduces the same circularity: on the first iteration after bootstrap, the `prev` value is `β_0` from the bootstrap; on subsequent iterations it is the previous steady step's output. The mixing of "bootstrap-derived prev" and "steady-derived prev" in the same predicate function obscures the iteration-zero special case that the rotation was supposed to eliminate. The strawman-canonical resolution (mirroring [`iterate-while`](./iterate-while.md)): the predicate sees the carry `α` only; any quantity derived from `prev` that the predicate needs is folded into the carry by `steady_step`'s body. CG v0.5 follows this: `s.converged` is set inside `cg_steady_step` from the freshly-computed `res'`, and the predicate reads `not s.converged` (`cg.md:442`); `beta_prev` is the `prev` closure parameter but is never read by the predicate.

## Algebraic laws

The L4 laws are stated against the v0.3-strawman-conformant form above. Absences are catalogued explicitly to prevent decoration drift.

1. **Degeneracy to [`iterate-while`](./iterate-while.md) when `PrevCarry = ()`** (the load-bearing equivalence; rationale for unifying the two combinators in one harvester dispatch). When `β = ()`, the `prev` slot carries no information; the combinator definitionally reduces to [`iterate-while`](./iterate-while.md) preceded by an outer identity-step:

   $$
   \textsf{iterate\_while\_with\_prev}\ f_{\textsf{boot}}\ a_0\ f_{\textsf{steady}}\ p \;\equiv\; \textsf{iterate\_while}\ (f_{\textsf{boot}}(a_0).\textsf{state})\ p\ (\lambda a.\ f_{\textsf{steady}}(a, ()))\ \mathop{\text{prepended with}}\ f_{\textsf{boot}}\text{'s extras}
   $$

   (the `prepended with` is the trajectory-concatenation `[bootstrap_extras] ++ steady_trajectory`). This law is what makes the two combinators a *family*: the with-prev form is the strict generalisation; the no-prev form is the `β = ()` specialisation. Slices that don't need a `prev` use [`iterate-while`](./iterate-while.md); slices that do use this combinator. (At the calculus level, slices could uniformly use this combinator and pass `β = ()`; the [`iterate-while`](./iterate-while.md) entry exists as the no-bootstrap idiom because the bootstrap call adds noise when no `prev` is needed.)

2. **Trajectory-pruning demand-rule** (inherited from [`iterate-while`](./iterate-while.md) Law 1 and the strawman §3.8). When a downstream consumer reads only `final_state`, the §3.8 pruning rule rewrites both `bootstrap_step` and `steady_step` to the subgraphs that compute only the `{ state, prev }` fields, omitting the extras. Symbolically:

   $$
   \frac{
     \text{only } \textsf{final\_state} \text{ of } \textsf{iterate\_while\_with\_prev}\ f_{\textsf{boot}}\ a_0\ f_{\textsf{steady}}\ p \text{ is observed}
   }{
     \dots \;\equiv\; \{\textsf{final\_state}: \textsf{iterate\_while\_with\_prev\_pure}\ f_{\textsf{boot}}^{\textsf{stateprev}}\ a_0\ f_{\textsf{steady}}^{\textsf{stateprev}}\ p,\ \textsf{trajectory}: [\,]\}
   }
   $$

   where the superscript `stateprev` denotes the projection to the `{state, prev}` subgraph. Same demand-pruning law as [`iterate-while`](./iterate-while.md) Law 1, lifted to handle two step bodies instead of one.

3. **Bootstrap-then-loop ordering invariance under pure shifts**. If `f_boot` and a corresponding "shifted-bootstrap" pair `(f_boot', shift)` satisfy `f_boot(a) = let { state, prev, ...e } = f_boot'(a) in { state: shift(state), prev, ...e }` (a pure post-processing of the bootstrap state by `shift :: α -> α`), and similarly `f_steady` admits a pre-processing `f_steady'((a, β)) = f_steady((shift⁻¹(a), β))`, then the two forms produce iteration-for-iteration-identical trajectories (modulo the `shift`/`shift⁻¹` re-bracketing). This is the law that justifies the v0.4-to-v0.5 CG rotation: the v0.4 step body's `if it == 0` branch is the "shift" operation that moves a not-yet-computed quantity into a sentinel; v0.5's bootstrap computes the real value and the steady step uses it without the sentinel. This law is stated narrowly (it requires the shift to be pure and invertible-up-to-the-iteration-structure); broader fold-fusion laws do *not* hold (see non-laws below).

Laws that explicitly **do not** hold:

- **Bootstrap-then-loop fold-fusion across bootstraps.** `iterate_while_with_prev f_boot a₀ f_steady p` followed by another `iterate_while_with_prev g_boot a₁ g_steady q` is *not* equivalent to a single `iterate_while_with_prev` with combined bootstrap and steady steps. The two bootstraps fire at different times and produce different `prev` values; the combined form would either fire the second bootstrap (changing the prev-threading semantics) or skip it (losing its effect). Same reason as [`iterate-while`](./iterate-while.md)'s no-step-composition law.

- **Predicate hoisting between bootstrap and steady loop.** The predicate fires after `bootstrap_step` but is not given a chance to short-circuit before it. There is no `iterate_while_with_prev_BAIL` variant that tests `p(a_0)` before running `f_boot`; slices that need this test handle it outside the combinator (see `cg.md:433-434`). The asymmetry is structural — the predicate's type is `α -> Bool` and `a_0` is in scope at the call site; the caller can test it themselves if needed.

- **Carry-projection law generalising to `prev`-projection.** [`iterate-while`](./iterate-while.md)'s Law 4 (fold-fusion-with-carry-projection) does NOT lift to a `prev`-projection law. Projecting `prev` to a lower-rank space breaks the threading invariant (the projected `prev'` is not generally a valid input to a `steady_step'` that expects the higher-rank one). A `prev`-projection law would require the slice to demonstrate that the projection commutes with both `bootstrap_step` and `steady_step` *and* with the iteration's algebraic invariants — a tall order that no consuming slice currently exercises. The law is omitted rather than weakly stated.

- **Form-equivalence to the in-step-branch form under L4 rewrites.** The Form-A (in-step `if it == 0`) and Form-B (bootstrap-then-steady-loop) versions of an algorithm produce iteration-for-iteration-identical results per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) §"What is preserved", but they are *not* related by an L4-calculus rewrite using only the monad / β / let laws. The rotation is *structural* (drops a carry field, threads a closure parameter, splits one function into two); it is not a syntactic equivalence under the calculus's reduction rules. Same non-law as the harvester's `krylov-step.md` non-law on form-equivalence-under-monad-laws.

- **Predicate fires on `(carry, prev)` rather than carry alone.** Per the predicate-on-prev anti-pattern above, the predicate is `α -> Bool`, full stop. There is no `(α, β) -> Bool` variant.

- **Identity / empty bootstrap.** A bootstrap step `f_boot = \a -> { state: a, prev: ⊥ }` that does no actual computation and produces a sentinel `prev` is *valid syntactically* but defeats the rotation's purpose — the steady step would then need to either branch on `prev == ⊥` (defeating branch-freedom) or treat the iteration-zero case implicitly (defeating the static call-site obligation). The combinator does not reject such bootstraps, but the slice that writes them is back at the in-step-branch form modulo positional permutation.

## Dependencies

L4 concept references:

- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the rotation that lands this combinator as the driver of the unrolled form. The §"The rotation" pseudo-code at `first-iteration-unrolling.md:21-37` writes a placeholder driver `iterate_while_with_carry` whose role is identical to this entry's `iterate_while_with_prev`.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra underwriting Law 2 (same role as in [`iterate-while`](./iterate-while.md)).
- [`solve-monad`](../concepts/solve-monad.md) — the `Solve` monad threaded through the Solve-threaded signature form.

L4 row dependencies:

- [`iterate-while`](./iterate-while.md) — the no-bootstrap base combinator; Law 1 of this entry states the degeneracy. The two entries are mutually-cross-referential as a family.
- [`krylov-step`](./krylov-step.md) Form B — the typed-wrapper Krylov step kernel whose `(first_step, steady_step)` pair is the canonical consumer of this combinator. The `first_step` of `krylov-step` Form B is the `bootstrap_step` of this combinator; the `steady_step` of Form B is this combinator's `steady_step`.

## Lowers to

The L4>L3 lowering for `iterate_while_with_prev` is the bootstrap-then-tail-recursive value-threading L3 form, structurally parallel to [`iterate-while`](./iterate-while.md)'s L3 lowering per `krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like". The rotation dissolves the same three pieces of L4 wrapper machinery as the no-prev combinator (Solve monad threading; record-structured step return; demand-prunable trajectory), plus a fourth piece specific to this entry: **the `prev` closure parameter dissolves into a positional argument of the L3 tail-recursive worker.** No semantic change; only the call shape changes.

```text
iterate_while_with_prev_L3 :: ... -> (α, sim) -> (α, sim, [extras])
iterate_while_with_prev_L3 f_boot a₀ f_steady p (a, sim) =
  let (a₁, β₀, e₀, sim') = f_boot (a, sim)
  in let (final, trajectory, sim'') = steady_loop_L3 a₁ β₀ f_steady p (sim')
     in (final, sim'', [e₀] ++ trajectory)

steady_loop_L3 a β f p (sim) =
  if p a then
    let (a', β', e, sim') = f (a, β, sim)
    in let (final, traj, sim'') = steady_loop_L3 a' β' f p (sim')
       in (final, [e] ++ traj, sim'')
  else
    (a, [], sim)
```

(The trajectory-vs-no-trajectory choice at L3 follows the same demand-resolution as [`iterate-while`](./iterate-while.md)'s L3 lowering; the slice's consumer determines which positional return is materialised.)

As with [`iterate-while`](./iterate-while.md), the dedicated L4>L3 theme for this combinator is now authored as the standalone chapter [`iterate-while-with-prev-dissolution`](../L4-L3/iterate-while-with-prev-dissolution.md) (cycle-047), the carry-bootstrapped sister of [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md). The dedicated theme captures **both** L3 forms: the **trajectory-keeping unpruned form** `iterate_while_with_prev_L3` — the bootstrap-then-tail-recursive ground form that materialises the `[e₀] ++ trajectory` accumulator this firm L4 form keeps (per Law 2) — and the **§3.8-pruned form** `iterate_while_with_prev_L3_pruned`, which is the collapse-rule image (Law 2's L3-side demand-pruning rewrite applied to both bodies under a `final_state`-only consumer). The earlier sub-component's trajectory-drop is the *pruned image*, not a gap in the firm L4 form; the unpruned ground form is what Law 2 keeps. See [`iterate-while-with-prev-dissolution`](../L4-L3/iterate-while-with-prev-dissolution.md) §"L3 form (RHS)" for the two forms, the `prev`-positional delta, and the collapse rule.

The L3>L2 lowering for the combinator itself is identity-in-form per the combinator-miner cycle-002 assertion, same as [`iterate-while`](./iterate-while.md).

## Variant axes

The combinator has **two variant axes**, both absorbed at the L4 form-level rather than in the consuming-slice's signature:

1. **Pure vs. Solve-threaded body.** Selected by the slice's choice of step bodies. The two forms share the same combinator definition modulo the body's monadic discharge. Identical to [`iterate-while`](./iterate-while.md)'s axis 1.

2. **Extras-carrying vs. no-extras.** Selected by whether the slice's step bodies return non-empty `e` records. The `iterate_while_with_prev_pure` sugar (defined in §Semantics) is the no-extras specialisation. Identical to [`iterate-while`](./iterate-while.md)'s axis 2.

There is **no third axis** (cf. [`iterate-while`](./iterate-while.md)'s axis 3 "bootstrap-free vs. carry-bootstrapped"): this combinator *is* the carry-bootstrapped form. The Form-A vs. Form-B presentation choice that [`krylov-step`](./krylov-step.md) Form A/B realises is the *slice-level* choice of which combinator to call — Form A calls [`iterate-while`](./iterate-while.md), Form B calls this combinator. The choice is below this combinator's level of abstraction.

## Status

`firm` — small-step semantics derived from the strawman §3.7 form by adding the bootstrap step and the closure-threaded `prev` parameter, both per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) §"The rotation"; the trajectory-pruning law (Law 2) is inherited from [`iterate-while`](./iterate-while.md); the degeneracy-to-`iterate-while` law (Law 1) is the load-bearing equivalence justifying the family framing; non-laws are catalogued explicitly (six non-laws plus the predicate-on-prev anti-pattern). The combinator is consumed by [`krylov-step`](./krylov-step.md) Form B (cycle-006 firm) and by CG v0.5 (`cg.md:441-446`); a follow-up open question is filed for GMRES Form B adoption (currently GMRES uses Form A only).

## L4 vs L3 distinction

- **L4**: a single combinator with structural bootstrap-then-loop semantics and the closure-threaded `prev` parameter; the body's `Solve`-monad effect is orthogonal to the value-threaded carry and `prev`; the predicate is purely on the carry; the trajectory is demand-pruned.
- **L3**: a bootstrap call followed by a tail-recursive loop with explicit `(carry, prev, sim)` positional threading; demand-pruning resolved per call site. The L3 form does not carry the bootstrap-then-loop *combinator name*; it carries the *unrolled tail-recursive shape* with the bootstrap as an explicit prefix.

Same effect-threading-and-demand-pruning-placement difference as [`iterate-while`](./iterate-while.md). The L4>L3 lowering is the dedicated standalone theme [`iterate-while-with-prev-dissolution`](../L4-L3/iterate-while-with-prev-dissolution.md) (cycle-047; the carry-bootstrapped sister of [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md)) — it erases the monadic packaging, positionalises the `prev` closure parameter, renders the bootstrap as a non-recursive prefix, and resolves the demand-pruning per consumer; it does *not* re-introduce the iteration-zero branch (the rotation is preserved across the lowering).

## Evidence

- `book/src/design/l4_calculus.md:151-184` — the L4 strawman's §3.7 `iterate_while` form that this entry generalises with the bootstrap-and-prev structure.
- `book/src/concepts/first-iteration-unrolling.md:17-37` — the rotation's call-shape (`first_step` / `steady_step` / `iterate_while_with_carry`) that this combinator realises. The strawman's pseudocode driver `iterate_while_with_carry` is renamed `iterate_while_with_prev` at the L4 row level for consistency with the cycle-006 harvester / abstractor signatures.
- `book/src/concepts/first-iteration-unrolling.md:39-55` — the "what gets hidden" / "what is preserved" properties: the `_prev` carry field is gone, the iteration-zero branch is gone, the steady step is branch-free; the algorithm's numerics are identical.
- `book/src/L4/krylov-step.md` (cycle-006 firm) — Form B signature consumes this combinator (`first_step` is the bootstrap, `steady_step` is the steady-step body). The harvester's caveat 2 is closed jointly by this entry and [`iterate-while`](./iterate-while.md).
- `book/src/L4/iterate-while.md` (this dispatch, companion) — Law 1 of this entry states the degeneracy to [`iterate-while`](./iterate-while.md) when `β = ()`.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-006 firm) — §"Speculative L4 operators" carries the rough-in signature `iterate_while_with_prev :: (PrevCarry -> Step) -> PrevCarry -> Step -> carry -> Solve Trajectory` that this chapter adopts and refines. (The refinement: the cycle-006 rough-in signature listed `(PrevCarry -> Step)` as the first argument, which conflates "bootstrap" with "steady-step-parameterised-by-prev"; this chapter splits the two — `bootstrap_step` produces the initial `prev`, `steady_step` consumes and threads `prev` — to match the `cg.md:441` call shape exactly.)
- `book/src/L4/krylov-step.md` Form B — the canonical v0.5 CG form using this combinator (firm-homed there cycle-099). The `cg_first_step` / `cg_steady_step` split is the prototypical Form B pair; the call `iterate_while_with_prev s1 s0.beta (\(s, _) -> ...) (\(s, beta_prev) -> ...)` is the prototypical use. **Note on closure-argument convention**: the L4 row's `steady_step` signature `((α, β) -> ...)` adopts the *carry-first, prev-second* convention. This matches the [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) pseudo-code at `first-iteration-unrolling.md:34-37` (`\(s, carry) -> (steady_step ... carry s, extract_carry s)` — `s` precedes `carry`) AND the CG v0.5 call site (`\(s, beta_prev) -> ...` — `s` precedes `beta_prev`). The L4 row's convention is therefore consistent with both renderings.
- `reference/palace/palace/linalg/iterative.cpp:434-441` — Palace's in-step `if (!it) { p = z; } else { linalg::AXPBY(..., beta / beta_prev, p); }` branch. This is the L0 evidence for *what the rotation removes*: the in-step iteration-zero special case that `iterate_while_with_prev` hoists into a bootstrap. Palace itself does not use the unrolled form; the L4 form is a presentation rotation that the Palace source does not realise.
- `reference/palace/palace/linalg/iterative.cpp:451` — the `beta_prev = beta;` line that carries the recurrence variable across iterations in Palace's in-step form. This is the L0 source for the "carry" being threaded; at L4 the carry is moved from a per-iteration local-scope variable into the combinator's closure-threaded `prev`.

No new Palace L0 source ranges are claimed beyond those already cited at `cg.md`; the combinator's L0 evidence base is the existing slice-level citations plus the two iterative.cpp ranges above (which were cited at cg.md but are re-anchored here as direct evidence for the rotation's *target* shape).
