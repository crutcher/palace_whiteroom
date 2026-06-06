# iterate-while

The tail-recursive value-threading loop combinator at L4. Folds a `Step` function over an initial `carry` value, threading the carry forward step-by-step and accumulating per-step readout records (extras) into a trajectory, until the loop predicate `cont` returns `False` on the current carry. The body of the [`solve-monad`](../concepts/solve-monad.md)'s `inner_loop`; the outer fold consumed by [`L4/krylov-step`](./krylov-step.md) (Form A). Companion to [`iterate-while-with-prev`](./iterate-while-with-prev.md), which carries an additional closure parameter for the previous-iteration recurrence carry.

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes iteration, dispatch sites, and effect placement structural. `iterate_while` is the **canonical iteration primitive** at L4: every iterative algorithm in the spec (CG, GMRES, Chebyshev, Arnoldi, transient time-stepping, eigenmode iteration) reduces at L4 to one or more `iterate_while`-folds around per-step kernels.

The L4 strawman (`book/src/semantics/index.md` §3.7) gives this combinator as the v0.3 generalisation of the v0.2 `iterate_while_pure` sketch — generalised to carry per-step extras (a `trajectory`) so that residual histories, monitoring metrics, and breakdown tokens can be returned uniformly through the same combinator. The §3.8 demand-pruning law (`index.md:186-213`) ensures that consumers reading only `.final_state` see the trajectory pruned away — the per-step extras are never computed when no downstream consumer reads them.

This chapter is the L4-row anchor for the combinator that the cycle-006 firm L4 entry [`krylov-step`](./krylov-step.md) consumes structurally without anchor (caveat 2 of the harvester's report), and that the cycle-006 wave-2 abstractor theme [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"Speculative L4 operators" proposed as a rough-in. Promoting it closes the cycle-006 open question `iterate-while-l4-anchor-missing`.

`iterate_while` at L4 is a **methodology-level combinator**, not a Palace-source artefact — Palace's iteration loops at L0 are explicit `for`/`while` C++ constructs (e.g., the PCG main loop at `palace/linalg/iterative.cpp:427`, the GMRES inner Arnoldi at `palace/linalg/iterative.cpp:615`). The L4 form names the abstract shape those L0 loops realise. Palace evidence sits at L0 (and in the slice corpus at L2 through L4 v0.4-v0.5 renderings); L4 cites the strawman §3.7 as its conventions source.

## Signature

The L4 signature is the value-threading combinator shape, parameterised by the carry type `α`, the readout-record-extras type `e`, and the implicit `Sim` (`Solve`) monad. The strawman's v0.3 form uses `state` for the carry slot; this chapter uses `carry` to avoid collision with the `SimState` of [`solve-monad`](../concepts/solve-monad.md). The two names refer to the same syntactic role.

**Form (pure, no `Solve` threading)** — the `iterate_while_pure` sugar from `index.md:178-183`:

```text
iterate_while_pure :: α -> (α -> Bool) -> (α -> α) -> α
```

**Form (extras-carrying, pure)** — the strawman §3.7 v0.3 form:

```text
iterate_while
  :: α
  -> (α -> Bool)
  -> (α -> { state: α, ...e })
  -> { final_state: α, trajectory: [{ ...e }] }
```

**Form (Solve-threaded, extras-carrying)** — the form consumed by [`krylov-step`](./krylov-step.md):

```text
iterate_while
  :: α
  -> (α -> Bool)
  -> (α -> Solve { state: α, ...e })
  -> Solve { final_state: α, trajectory: [{ ...e }] }
```

The three forms collapse into one another at the calculus level: `iterate_while_pure` is the special case where `e = ()` and the body is non-monadic; the pure extras-carrying form is the special case of the `Solve`-threaded form where the body's monadic action is `pure`. The `Solve`-threaded form is the load-bearing one for Krylov solvers, where the body increments `SimState.it` via `modify` (see [`krylov-step`](./krylov-step.md) §Semantics).

Shape contract (bunsen-style; named records; the `α`, `e` slots are arbitrary L4 types, instantiated per use):

- **`carry: α`** — the iteration-threaded state. Passed positionally as the first argument (`init`); plumbed forward through each step's `{ state: α, ... }` return; surfaced as `final_state` in the return record. At the consuming slice, `α` is typically the slice's ephemeral-stratum bundle (e.g., CG's `CgState`, GMRES's `Krylov`, Chebyshev's `ChebyshevState`); at the L4 typing, it is fully general — any L4 type may inhabit the carry slot. The carry is **value-threaded** (immutable per the L4 calculus's tensor-and-record discipline); no aliasing concerns.
- **`cont: α -> Bool`** — the loop predicate. Read by the combinator before each step call. Takes the current carry as its argument; returns `False` to stop. The combinator does *not* call `cont` on `init` before testing whether `init` should be returned without ever stepping — per the strawman §3.7 small-step rule, the predicate fires first (consistent with `while`-loop convention; opposite of `do { ... } while` convention). The predicate is a **pure function**; it cannot read `SimState` (that would defeat the Sim-monad-effect localisation of the body). If a slice's predicate needs to read `SimState.it` against `op.max_it`, the slice folds `it` into its `α` carry and reads it from there — see CG's `s.it < config.max_it && not s.converged` predicate in `cg.md:217`.
- **`step: α -> { state: α, ...e }`** (pure form) or **`α -> Solve { state: α, ...e }`** (Solve-threaded form) — the per-step body. Produces the next carry value in the `state` field, plus the per-step extras `e` (a record of per-step readouts). The extras record fields are slice-specific (CG: `{ residual_norm: Scalar }`; GMRES: `{ residual_norm: Scalar, breakdown_token: BreakdownTag }`; Chebyshev: `{}`); the combinator is generic in the extras shape.
- **`extras: { ...e }`** — the per-step readout record. Demand-prunable per §3.8 (`index.md:186-213`). Consumers reading the trajectory's per-step extras materialize the computation; consumers reading only `final_state` cause the extras computation to be pruned at the call site. The combinator does not inspect `extras`; it forwards them positionally to the trajectory.
- **result `{ final_state: α, trajectory: [{ ...e }] }`** — a record carrying the final value of the threaded carry plus the list of all per-step extras records (in iteration order). Demand-pruning of `trajectory` cascades into demand-pruning of each `step`'s extras computation, per the chained §3.8 rewrite. When the consumer reads only `final_state`, the per-step `extras` computation in `step` is pruned at every step.

The signature makes four things structural that are merely conventional in source-level loop encodings:

1. **The predicate sees the carry only**, not the extras nor the `SimState`. This forces convergence/termination state into the carry — slices that test on residual norm carry the norm in the carry, not in the extras. (See CG's `s.converged` carry field — set inside the step body from the residual-norm computation, consumed by the predicate.)
2. **The carry is value-threaded; the trajectory is record-spread.** No fold accumulator state outside the carry — anything that needs to persist across iterations is in the carry; anything that is per-step output is in the extras and ends up in the trajectory list. This split mirrors the strawman §3.7's `state` vs `extras` distinction.
3. **The body's monadic effect (when in the Solve form) is on `SimState`, not on the carry.** The carry is a pure value; `SimState` is monad-threaded; the two compose without aliasing because `SimState` lives in the monadic environment and the carry lives in the value-threading.
4. **The trajectory is observed structurally for §3.8 pruning.** The list constructor `[{ ...e }]` is the syntactic site where per-step extras pile up; the §3.8 pruning rule rewrites the body to omit the extras computation when no downstream consumer reads the trajectory. This is the load-bearing simplification that lets one combinator definition serve both "compute residuals for monitoring" and "skip residuals for speed" use cases (per [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)).

## Semantics

`iterate_while` at L4 is the standard tail-recursive value-threading loop, with the per-step extras collected into a trajectory list. The small-step reduction rule is exactly the strawman §3.7 rule (`index.md:164-171`):

$$
\begin{aligned}
\textsf{iterate\_while}\ a\ p\ f &\;\to\; \textsf{if}\ p(a) \\
&\quad \textsf{then}\ \textsf{let}\ \{\textsf{state}: a',\ \dots e\} = f(a)\ \textsf{in} \\
&\quad\quad \textsf{let}\ \{\textsf{final\_state},\ \textsf{trajectory}\} = \textsf{iterate\_while}\ a'\ p\ f\ \textsf{in} \\
&\quad\quad \{\textsf{final\_state},\ \textsf{trajectory}: [\{\dots e\}] \mathop{++} \textsf{trajectory}\} \\
&\quad \textsf{else}\ \{\textsf{final\_state}: a,\ \textsf{trajectory}: [\,]\,\}
\end{aligned}
$$

Read in prose: starting from `a`, test `p(a)`; if `False`, stop with `a` as `final_state` and empty trajectory; if `True`, run one step `f(a)` producing `{ state: a', ...e }`, recurse on `a'`, and prepend the step's extras `{ ...e }` to the recursive call's trajectory. The recursion is in tail position; an L3-level implementation realises this as an explicit tail-recursive loop (per [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"What the L3 form for iterate_while looks like").

For the `Solve`-threaded form (the load-bearing form for Krylov solvers), the rule lifts mechanically through the `Solve` monad's `>>=`:

$$
\begin{aligned}
\textsf{iterate\_while}\ a\ p\ f &\;\to\; \textsf{if}\ p(a) \\
&\quad \textsf{then}\ \textsf{do}\ \{\ \{\textsf{state}: a',\ \dots e\} \leftarrow f(a);\ \\
&\quad\quad \{\textsf{final\_state},\ \textsf{trajectory}\} \leftarrow \textsf{iterate\_while}\ a'\ p\ f; \\
&\quad\quad \textsf{return}\ \{\textsf{final\_state},\ \textsf{trajectory}: [\{\dots e\}] \mathop{++} \textsf{trajectory}\}\ \} \\
&\quad \textsf{else}\ \textsf{return}\ \{\textsf{final\_state}: a,\ \textsf{trajectory}: [\,]\,\}
\end{aligned}
$$

The `Solve` monad's `SimState` effect threads transparently through the `do`-block; the combinator does not read or write `SimState` directly. Any `SimState` interaction is the responsibility of `f`'s body — typically a `modify (\s -> s { it = s.it + 1 })` in Krylov step kernels (see [`krylov-step`](./krylov-step.md) §Semantics). The `Solve`-threaded form is equivalent to the pure form modulo the `Sim` effect being orthogonal to the value-threading.

The `iterate_while_pure` sugar (`index.md:178-183`) is a closed-form definitional shortcut for the no-extras case:

$$
\textsf{iterate\_while\_pure}\ a\ p\ f \;\equiv\; (\textsf{iterate\_while}\ a\ p\ (\lambda x.\ \{\textsf{state}: f(x)\}))\textsf{.final\_state}
$$

When the step has no per-step readouts to surface (e.g., the LBM step at `index.md:374-386`), `iterate_while_pure` is the idiomatic form; the trajectory is uniformly empty and `final_state` is the only field consumed.

Three placement disciplines that the L4 typing enforces (sharpening conventions from the strawman):

- **The predicate is pure on the carry.** No reads of `SimState`, no reads of `OpParams`, no reads of per-step extras. This is structural at L4 because the predicate's type is `α -> Bool` with no monadic effect and no closure over the extras record. If a slice's termination logic requires `SimState.it`, the slice's `α` includes `it` as a field (per `cg.md:217` — `s.it < config.max_it && not s.converged`). If termination requires per-step readouts (e.g., a breakdown token), the readout is folded into the carry by the step body — see [§"Predicate-on-extras"](#predicate-on-extras-anti-pattern) anti-pattern below.
- **The step body's `Solve` effect is on `SimState` only.** The carry transitions are pure value-threading; any monadic effect inside `f` touches `SimState` (typically the iteration counter) and no other monad state. This is the same effect-localisation discipline as [`solve-monad`](../concepts/solve-monad.md) §"What stays out of the monad" — operator applications, dense recurrences, and carry updates are pure; `SimState` writes are monadic.
- **Trajectory pruning is demand-driven, not flag-driven.** Per `derived-view-hoisting.md:19` and `index.md:186-213`, when a downstream consumer reads only `final_state`, the per-step extras computation in `f`'s body is eliminated by the §3.8 pruning rewrite. The combinator does not branch on a "compute residuals?" flag — there is no such flag. The L4 form makes residual-monitoring vs. no-monitoring the *same algorithm*, with consumer demand picking which extras get materialised. (Contrast with Palace's L0 `print_opts.iterations`-conditional residual printing at `iterative.cpp:422-426` — at L4 the conditionality disappears.)

### Predicate-on-extras anti-pattern

A natural-looking but wrong sketch is to let the predicate inspect the per-step extras:

```text
iterate_while_BAD :: α -> e -> ((α, e) -> Bool) -> (α -> { state: α, ...e })
                  -> { final_state, trajectory }
```

This typechecks but introduces a *circular dependency*: the predicate decides whether to stop *before* the step that would produce the extras runs, so the predicate has no extras to read on the first iteration. The strawman §3.7 form resolves this by folding the readouts the predicate cares about into the *carry*, not the extras — the predicate reads `α` (which already contains the residual norm / convergence flag / breakdown token), and the extras hold only the per-step quantities that are *outputs* rather than control-flow inputs. This chapter adopts the strawman convention: the predicate is `α -> Bool`, full stop.

For slices where the convergence flag is genuinely a per-step computation (e.g., CG's `converged: res' < eps` set inside `cg_step`), the carry's `converged: Bool` field is the canonical home; the predicate reads `s.converged` and the step body writes it from the residual computation. The extras record holds `residual_norm` for trajectory consumers but the predicate does not consume it.

## Algebraic laws

The L4 laws are stated against the v0.3 strawman form. Absences are catalogued explicitly to prevent decoration drift.

1. **Demand-driven trajectory pruning** (the load-bearing law; inherited from [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) and the strawman §3.8). For any consumer expression `K[ iterate_while a p f ]` that observes only the `final_state` field of the combinator's result (i.e., `K` destructures with `let { final_state, trajectory: _ } = ...`), the §3.8 pruning rule rewrites the body `f` to the subgraph that computes only the `state` field of its return record, omitting the extras computation. Symbolically:

   $$
   \frac{
     \text{only } \textsf{final\_state} \text{ of } \textsf{iterate\_while}\ a\ p\ f \text{ is observed}
   }{
     \textsf{iterate\_while}\ a\ p\ f \;\equiv\; \{\textsf{final\_state}: \textsf{iterate\_while\_pure}\ a\ p\ f_{\textsf{state}},\ \textsf{trajectory}: [\,]\}
   }
   $$

   where $f_{\textsf{state}} = \lambda a.\ (f\ a).\textsf{state}$ is the subgraph of $f$ that computes only the next-carry value. **Consequence**: a single `iterate_while` invocation in the body of a slice's solve function (e.g., `cg_solve` at `cg.md:215-219`) automatically specialises to the residuals-on / residuals-off variant depending on whether the caller reads `.residual_history` or only `.final_state` — without a runtime flag, without a separate algorithm. This is the law that justifies writing one `cg_step` definition for both monitoring and production use.

2. **Definitional reduction of `iterate_while_pure` to `iterate_while`** (the strawman's sugar definition):

   $$
   \textsf{iterate\_while\_pure}\ a\ p\ f \;\equiv\; (\textsf{iterate\_while}\ a\ p\ (\lambda x.\ \{\textsf{state}: f(x)\}))\textsf{.final\_state}
   $$

   When the step has no per-step extras to surface, the sugar collapses by Law 1 (trivial application — the trajectory is always `[]` because the extras record is the empty record; `final_state` is the only consumed field). The two forms are interchangeable for no-extras steps.

3. **Empty-trajectory base case** (read-off from the small-step rule). When `p(a) = False` initially, the result is `{ final_state: a, trajectory: [] }`. Equivalently, `iterate_while a (\_ -> False) f = { final_state: a, trajectory: [] }` for any `f`. The combinator does *not* call `f` at least once before testing; the predicate fires before the body.

4. **Fold-fusion with carry-projection** (a limited associativity-like law). For any pure function `g :: β -> α` that projects a richer carry onto the actual iteration carry, and any step `f' :: β -> { state: β, ...e }` such that `g(f'(b).state) = f(g(b)).state` and `f'(b).extras = f(g(b)).extras`, the projection commutes with the fold:

   $$
   \textsf{iterate\_while}\ b\ (p \circ g)\ f' \;\equiv\; \textsf{let}\ \{\textsf{final\_state}, \textsf{trajectory}\} = \textsf{iterate\_while}\ (g\ b)\ p\ f\ \textsf{in}\ \{\textsf{final\_state}: g^{-1}\_\textsf{like}(\textsf{final\_state}),\ \textsf{trajectory}\}
   $$

   (where $g^{-1}\_\textsf{like}$ is the inverse-like map that reconstitutes the richer carry from the iteration carry plus the surrounding closure — formally the law is a bisimulation up to $g$.) This is a narrow law that holds because the combinator does not introspect the carry shape; it only threads it. The law is used informally by [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) when moving `beta_prev` from a carry field (v0.4) to a closure parameter (v0.5) — see also [`iterate-while-with-prev`](./iterate-while-with-prev.md) Law 1.

Laws that explicitly **do not** hold:

- **Step composition / fold-merge across iterations.** `iterate_while a p₁ f` followed by `iterate_while final_state₁ p₂ f` is **not** equivalent to `iterate_while a (p₁ ‖ p₂) f` for arbitrary predicates and `f`. The two-phase fold's trajectory is `traj₁ ++ traj₂` (where `traj₂` starts from `final_state₁`); the flattened single-fold trajectory is one continuous list starting from `a` with a single predicate. The two are equal only when `p₁(final_state₁) = True`-implies-`p₂(final_state₁) = True` AND vice-versa, which is generally not the case for restart-style structures (which is why GMRES uses an outer `solve_loop` around the inner `iterate_while`, not a flattened single fold — see `gmres.md:437-470`).

- **Predicate hoisting / loop-invariant motion of `cont`.** `iterate_while a p f` is **not** equivalent to `if p(a) then iterate_while a' p f else { final_state: a, trajectory: [] }` for any `a'` derived from `a` — the predicate is re-evaluated on each iteration, not once. Naive hoisting would convert the bounded `iterate_while` into an unbounded `repeat f forever` driven by the initial predicate value, which is not a refinement.

- **Reordering of step and predicate-evaluation.** The strawman §3.7 form fires the predicate *before* the step; the do-while variant (predicate after step) is a different combinator (definable as `iterate_while_post a p f = let { state, ...e } = f a in if p state then iterate_while_post state p f else { final_state: state, trajectory: [{...e}] }`). The two are not equivalent on a non-trivial initial-predicate case. This chapter formalises the strawman §3.7 form only; the do-while variant is not yet needed (no slice in the corpus uses it).

- **Commutation with the `Solve` monad's `modify`.** The trajectory accumulator's spread `[{...e}] ++ trajectory` is left-biased; reordering steps across iterations would reorder the trajectory and the `SimState.it` increments. The combinator is not invariant under monad-internal effect reorderings; the iteration order is the canonical observable.

- **Identity / unit element.** There is no `α_id` such that `iterate_while α_id p f = { final_state: α_id, trajectory: [] }` for all `p` and `f` — the trivial case `p(α_id) = False` covers only the never-step case, not a meaningful identity element. (Per the calculus, `iterate_while`-trees are not a monoid; the combinator is a fold, not a foldable structure's combining operation.)

- **Termination guarantee from the type.** The signature does not encode totality. A step that never makes the predicate false on any reachable carry diverges. Totality is an obligation on the consuming slice (per the strawman §3.7 note: "Total correctness depends on the predicate eventually becoming false; the spec records the convergence argument as part of the slice that uses the loop"). Typical slice-level discharges: bounded `max_it` folded into the carry; convergence guarantees from algorithmic analysis (Krylov methods on SPD systems); explicit `Outcome = Continue | Done` sums that always reach `Done` in finite steps (`solve-monad.md:58-66`).

## Dependencies

L4 concept references (consumed structurally; per the cycle-006 cross-cutter caveat, these are concept-page links — see Open Questions for the L4-row-vs-concept dependency question, inherited unchanged from `krylov-step.md`):

- [`solve-monad`](../concepts/solve-monad.md) — the `Solve a = StateT SimState Identity a` monad threaded through the Solve-threaded signature form.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra underwriting Law 1 (trajectory pruning when only `final_state` is consumed).
- [`convergence-test`](../concepts/convergence-test.md) — the `Convergence` value passed as a pure closure to the predicate (when convergence-on-residual is the termination criterion). The combinator does *not* depend on `Convergence` typing; `Convergence.satisfied :: Scalar -> Bool` is a closure the slice constructs and the predicate calls. Listed for completeness; the dependency is consumer-side, not combinator-side.

L4 row dependencies (operators that consume this combinator):

- [`krylov-step`](./krylov-step.md) at L4 — the typed-wrapper Krylov step kernel that `iterate_while` folds in the body of [`solve-monad`](../concepts/solve-monad.md)'s `inner_loop`. The Form A signature of `krylov-step` is exactly the step type of `iterate_while` (in its Solve-threaded form).
- [`iterate-while-with-prev`](./iterate-while-with-prev.md) at L4 — the variant carrying an additional closure-threaded `PrevCarry`. Reduces definitionally to `iterate_while` when `PrevCarry = ()`; see Law 1 of the companion entry.

## Lowers to

The L4>L3 lowering for `iterate_while` is the tail-recursive value-threading L3 form sketched in [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"What the L3 form for iterate_while looks like". The rotation dissolves three pieces of L4 wrapper machinery:

1. **The `Solve` monad threading collapses.** The L4 `Solve { final_state, trajectory }` return becomes an L3 positional `(final_state, trajectory, sim')` tuple. The `SimState` is value-threaded through the L3 recursion as an explicit positional argument.
2. **The record-structured `{ state: α, ...e }` step return becomes a positional tuple.** L3 has no row-polymorphic record spread; the step's positional shape `(α', e)` is what the recursion threads. Trajectory accumulation becomes explicit list-cons.
3. **The trajectory record-list with demand-pruning attached structurally collapses to either an explicit accumulator pass-through OR an outright drop**, depending on the slice's downstream consumer demand. The L3 form encodes the §3.8 pruning as a *call-site choice*: a slice that reads only `final_state` lowers to an L3 form whose step computes only the next carry (no extras); a slice that reads the trajectory lowers to an L3 form whose step computes both. The L3 form does not carry the demand-pruning *rewrite rule* — that lives at L4 — only the *resolved form*.

The L4>L3 theme for `iterate_while` is now authored as the dedicated standalone chapter [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md) (cycle-047), extracted from the sub-component description in the `krylov-step-typed-wrapper-dissolution` theme (§"What the L3 form for iterate_while looks like"). The dedicated theme captures **both** L3 forms: the **trajectory-keeping unpruned form** `iterate_while_L3` — the ground form that materialises the `[readout]` accumulator this firm L4 form keeps (per Law 1) — and the **§3.8-pruned form** `iterate_while_L3_pruned`, which is the collapse-rule image (Law 1's L3-side demand-pruning rewrite applied to the ground form under a `final_state`-only consumer). The earlier sub-component's trajectory-drop is the *pruned image*, not a gap in the firm L4 form; the unpruned ground form is the reconciliation that closes cycle-006 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`. See [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md) §"L3 form (RHS)" for the two forms and the collapse rule.

The L3 form for `iterate_while_pure` is the textbook tail-recursive loop with no accumulator:

```text
iterate_while_pure_L3 :: α -> (α -> Bool) -> (α -> α) -> α
iterate_while_pure_L3 a p f = if p a then iterate_while_pure_L3 (f a) p f else a
```

This L3 form is identity-in-form on the body (no primitive substitution), per the same combinator-miner cycle-002 assertion that justifies `krylov-step` L3>L2 identity. The L3>L2 lowering for the loop combinator itself is *also* identity-in-form (the same tail-recursive shape is L2-native), so the full L4>L3>L2 chain for `iterate_while_pure` collapses to the L4>L3 wrapper dissolution alone.

## Variant axes

The combinator has **three variant axes**, all absorbed at the L4 form-level rather than in the consuming-slice's signature:

1. **Pure vs. Solve-threaded body.** Selected by the slice's choice of `step :: α -> { state: α, ...e }` vs. `step :: α -> Solve { state: α, ...e }`. The two forms share the same combinator definition modulo the body's monadic discharge. The slice picks based on whether the step needs to touch `SimState`. Most algorithmic slices (Krylov solvers, time-stepping, eigensolver iteration) pick the Solve-threaded form to carry the `it` counter; pure-numerical slices (LBM at `index.md:374-386`) pick the pure form via `iterate_while_pure`.

2. **Extras-carrying vs. no-extras.** Selected by whether the slice's step returns a non-empty `e` record. Slices that need per-step readouts (CG: `residual_norm`; GMRES: `residual_norm` + `breakdown_token`) carry extras and access `trajectory`. Slices with no readouts (LBM) use the `iterate_while_pure` sugar. The two are unified at the combinator level — `iterate_while_pure` is definitionally `iterate_while` with `e = ()` (and the no-extras case is the §3.8 trivial pruning).

3. **Bootstrap-free vs. carry-bootstrapped.** Selected by which combinator the slice picks — `iterate_while` (this entry) for the bootstrap-free case; [`iterate-while-with-prev`](./iterate-while-with-prev.md) for the variant carrying a `PrevCarry` produced by a separate bootstrap step. The two combinators are not unifiable at the signature level (the `_with_prev` form has different arity), but they are unifiable at the *semantic* level via the carry-projection law (Law 4 of this entry, Law 1 of the companion entry) — `iterate_while_with_prev` with `PrevCarry = ()` reduces to `iterate_while` plus an outer identity step.

## Status

`firm` — small-step semantics inherited verbatim from the L4 strawman §3.7 (`index.md:164-171`); the demand-pruning law (Law 1) is the load-bearing property and is inherited from the strawman §3.8 (`index.md:186-213`) plus the `derived-view-hoisting` concept; three variant axes (Sim threading, extras carrying, bootstrap-free vs. carry-bootstrapped) are catalogued at the combinator level rather than left to slices to re-discover; the no-laws section catalogues five non-laws explicitly (including the predicate-on-extras anti-pattern and the do-while reordering non-equivalence). The combinator is consumed structurally by [`krylov-step`](./krylov-step.md) (Form A) and by every L4 slice's solve function (`cg.md:215-219` for v0.4 CG; `cg.md:441` for v0.5 CG with the with-prev variant; LBM at `index.md:382-385` via the pure sugar). Two new follow-up open questions are filed and one existing OQ (`iterate-while-l3-rendering-trajectory-accumulation-gap`) is augmented with a cycle-007 status note (see §Open questions in this report).

## L4 vs L3 distinction

- **L4**: a single combinator with structural demand-pruning of the trajectory; the body's `Solve`-monad effect is orthogonal to the value-threaded carry; the predicate is purely on the carry; the trajectory is materialised exactly when a downstream consumer reads it.
- **L3**: a tail-recursive loop with explicit `SimState`-positional threading; the §3.8 pruning becomes a *call-site choice* (the slice's step is rendered with or without extras based on the consumer); the trajectory accumulator is either passed through positionally or dropped. The L3 form does not carry the pruning *rule*; it carries the pruning's *result* per call site.

The two layers' entries share signature shape (modulo wrapper dissolution) and small-step semantics on the body. They differ in **effect threading and demand-pruning placement**. The L4>L3 lowering is the dedicated standalone theme [`iterate-while-dissolution`](../L4-L3/iterate-while-dissolution.md) (cycle-047; extracted from `krylov-step-typed-wrapper-dissolution`) — it erases the monadic packaging and resolves the demand-pruning per consumer, rendering the unpruned `iterate_while_L3` ground form when the trajectory is observed and the pruned `iterate_while_L3_pruned` form under a `final_state`-only consumer.

## Evidence

- `book/src/semantics/index.md:151-184` — the L4 strawman's §3.7 `iterate_while` definition (v0.3 form with extras-carrying step and trajectory accumulator) plus the `iterate_while_pure` sugar. **Canonical reference**: the small-step rule in §Semantics is reproduced verbatim from `index.md:164-171`.
- `book/src/semantics/index.md:186-228` — the §3.8 demand-pruning rule that underwrites Law 1. The pruning-as-graph-DCE framing is the calculus-level justification for the trajectory-pruning behaviour.
- `book/src/semantics/index.md:374-386` — the LBM `run_lbm` example at the end of the strawman: `iterate_while_pure` consumed in production. Confirms the no-extras sugar's intended call shape.
- `book/src/L4/krylov-step.md` (cycle-006 firm) — the L4 row consuming this combinator structurally as the body-fold of `inner_loop` (§Semantics, §"L4 vs L2 distinction"). Caveat 2 of that entry's open-questions records the missing-anchor question this dispatch closes.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-006 firm) — §"Speculative L4 operators" carries the rough-in signature this chapter adopts and refines; §"What the L3 form for iterate_while looks like" sketches the L3 tail-recursive form cited in §"Lowers to".
- `book/src/concepts/derived-view-hoisting.md:14-29` — the demand-pruning algebra underwriting Law 1, with the CG residual-norm hoisting worked example as canonical evidence.
- `book/src/concepts/solve-monad.md:1-69` — the `Solve a = StateT SimState Identity a` monad threaded through the Solve-threaded signature; §"What stays out of the monad" articulates the effect-localisation discipline this combinator honours.
- `book/src/L4/krylov-step.md` §Semantics Form A — the canonical `iterate_while` call site at L4 v0.4 (`iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`, firm-homed there).
- The L3↔L4 correspondence (firm-homed at `book/src/L4/krylov-step.md` + `book/src/L4-L3/iterate-while-dissolution.md`) explicitly maps Palace's `for (; it < max_it && !converged; it++)` to `iterate_while`. **L0 evidence**: `reference/palace/palace/linalg/iterative.cpp:427` (the PCG main-loop predicate-driven `for`-loop) is the canonical Palace iteration shape this combinator names.
- `reference/palace/palace/linalg/iterative.cpp:427` — PCG outer loop. `for (; it < max_it && !converged; it++)` is the canonical Palace iterate_while pattern with bounded `max_it` and convergence flag in the predicate, both folded into the L4 `α` carry per the §Signature predicate discipline.
- `reference/palace/palace/linalg/iterative.cpp:615` — GMRES inner Arnoldi loop. `for (;; j++, it++)` with break-on-converged at line 644 is the second Palace iteration shape; the predicate-in-body break corresponds at L4 to `s.converged` being a carry field set inside the step body and read by the predicate on the next iteration. (The current GMRES slice writes this as a tail-recursive `inner_loop`; migration to `iterate_while` is filed as a cycle-007 follow-up OQ.)

No new Palace L0 source ranges are claimed beyond those already cited; the combinator's L0 evidence base is the existing slice-level citations.
