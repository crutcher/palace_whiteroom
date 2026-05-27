---
agent: harvester
invoked_at: 2026-05-27T16:05:50Z
scope: L4 operator family: iterate_while + iterate_while_with_prev
status: pending
inputs:
  - book/src/design/l4_calculus.md (L4 strawman, esp. §3.7 iterate_while sketch + §3.8 demand-pruning)
  - book/src/L4/krylov-step.md (cycle-006 firm L4 chapter; precedent for chapter shape)
  - book/src/L4/index.md (current dep-map with two rough-in rows being promoted)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (cycle-006 wave-2 theme; §Speculative L4 operators carries the rough-in signatures and §"What the L3 form for iterate_while looks like" carries the tail-recursive L3 rendering)
  - book/src/concepts/solve-monad.md (Solve = StateT SimState Identity; the monadic environment iterate_while threads through)
  - book/src/concepts/derived-view-hoisting.md (the demand-pruning algebra that prunes unread trajectory readouts)
  - book/src/concepts/first-iteration-unrolling.md (the rotation whose driver is iterate_while_with_prev)
  - book/src/concepts/convergence-test.md (Convergence value passed as a plain closure; not part of iterate_while's typing)
  - book/src/spec/slices/cg.md:215-219 (the canonical iterate_while call site at L4)
  - book/src/spec/slices/cg.md:440-446 (the canonical iterate_while_with_prev call site at L4 v0.5)
  - book/src/spec/slices/gmres.md:459-470 (the inline-tail-recursive inner_loop that iterate_while abstracts)
  - reference/palace/palace/linalg/iterative.cpp:427 (PCG outer-loop L0 evidence for iterate_while)
  - reference/palace/palace/linalg/iterative.cpp:434-441,451 (the in-step first-iteration branch + beta_prev carry — L0 evidence for iterate_while_with_prev)
  - reference/palace/palace/linalg/iterative.cpp:615-644 (GMRES inner Arnoldi loop with predicate-in-body break — second iterate_while pattern)
  - scaffolding/open-questions.md:1064 (OQ `iterate-while-l4-anchor-missing` — closed by this dispatch)
status: integrated
integrated_at: 2026-05-27T17:17:02Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied cycle-007 wave-1 per-report dispatch 4 of 6 at 18:30:00Z; finalized in batch cycle-007 at 17:17:02Z.
  Files created: book/src/L4/iterate-while.md (3 variant axes), book/src/L4/iterate-while-with-prev.md (2 variant axes; third axis below combinator level).
  Files edited: book/src/L4/index.md (2 rough-in rows → firm; krylov-step row Dependencies cell extended with 2 new L4-row dependencies = first L4-row-on-L4-row dep edge), book/src/SUMMARY.md (2 L4 Part inserts after krylov-step), scaffolding/open-questions.md (1 status flip on iterate-while-l4-anchor-missing open → answered; 1 body augmentation kept-open on iterate-while-l3-rendering-trajectory-accumulation-gap; 2 new OQs appended).
  2 new OQs: gmres-inner-loop-iterate-while-migration, iterate-while-pure-promotion-decision.
  Closes cycle-006 OQ iterate-while-l4-anchor-missing.
  L4 firm cohort: 1 → 3.
  MCP codemap pilot dispatch (priority #16 step e): permission-denied; fallback to vanilla Grep/Read worked; rollout decision deferred to cycle-009 meta-phase per user directive.
  L4 strawman in-management + pseudo-language conventions applied (Haskell :: arrow form + TypeScript record brace form in ```text``` fences; $$ ... $$ LaTeX math for small-step semantics).
  Gate hits: 0.
---

# CYCLE: Formalize iterate_while + iterate_while_with_prev at L4 (family, single dispatch)

## Summary

This dispatch promotes the two rough-in L4 dep-map rows for `iterate_while` and `iterate_while_with_prev` to firm operator chapters. The two operators are a **family** (one bootstrap-free combinator and its bootstrap-carry variant) and are firmed together per the cycle-007 planner's "Open questions §5" rationale: their signatures are mutually referential, the variant collapses to the base under `PrevCarry = ()`, and shared content (small-step semantics, demand-pruning law, predicate-as-Bool-vs-as-Outcome convention) is best stated once.

The two combinators are already in heavy load-bearing use across the cycle-006 wave artefacts — `book/src/L4/krylov-step.md` references them in §Semantics and §Algebraic laws; `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Speculative L4 operators" carries proposed signatures; `book/src/spec/slices/cg.md` calls them at the slice level (v0.4 `iterate_while`, v0.5 `iterate_while_with_prev`); `book/src/concepts/derived-view-hoisting.md` cites the trajectory-pruning behaviour; `book/src/concepts/first-iteration-unrolling.md` describes the rotation that lands `iterate_while_with_prev`. The L4 strawman (`book/src/design/l4_calculus.md` §3.7) provides the canonical small-step semantics and the `iterate_while_pure` sugar. This dispatch's job is to make the L4 anchor exist (closing the cycle-006 OQ `iterate-while-l4-anchor-missing`) and to settle the signatures that the harvester-on-`krylov-step` and the abstractor-on-`krylov-step-typed-wrapper-dissolution` left as rough-in.

The signatures adopted here are exactly the harvester / abstractor rough-ins from cycle-006, refined by the strawman §3.7 form (the strawman's extras-carrying `{ state, ...extras }` step return is the canonical shape; the predicate-on-`carry` form is the same modulo carrying `state` as the carry). One naming consolidation: the strawman uses `state` for the threaded carry and `extras` for the per-step readout record; this chapter uses `carry` (to avoid collision with `SimState`) and keeps `extras` per the strawman. The strawman's `iterate_while_pure` sugar (no-extras) is named here as well.

The chapters are explicit on six items the rough-ins left implicit: (i) the relationship to the strawman's §3.7 `iterate_while` (this chapter's form *is* the strawman's, repackaged with `carry` instead of `state`); (ii) the `Solve` monad threading discipline (the carry is value-threaded; `SimState` is monad-threaded; no double-counting); (iii) the demand-pruning law in §Algebraic laws (inherited from `derived-view-hoisting`, sharpened to a trajectory-level statement); (iv) the predicate-on-carry-only vs. predicate-on-(carry,extras) convention (predicate sees `carry` only, per the strawman); (v) the termination obligation (totality requires the predicate eventually false; non-total bodies that may never terminate are flagged at the consuming slice, not the combinator); (vi) the degeneracy `iterate_while_with_prev` with `PrevCarry = ()` reduces (definitionally) to `iterate_while` — stated as a law, not just a comment.

## Proposed changes

```edit:book/src/L4/iterate-while.md
[create — file does not exist; full body in §Operator content / iterate-while below]
```

```edit:book/src/L4/iterate-while-with-prev.md
[create — file does not exist; full body in §Operator content / iterate-while-with-prev below]
```

```edit:book/src/L4/index.md
[update dep-map: replace the two rough-in rows for `iterate_while` and `iterate_while_with_prev` with firm rows linking the new chapters; keep `krylov-step` row unchanged]
```

```edit:book/src/SUMMARY.md
[add two chapter entries under the L4 Part, after the existing `- [krylov-step](./L4/krylov-step.md)` line]
```

```edit:scaffolding/open-questions.md
[update OQ `iterate-while-l4-anchor-missing` (cycle-006) frontmatter: flip `status: open` to `status: answered`, add `answered_at: cycle-007`, add `answered_in: reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/`. Schema matches the cycle-006 `krylov-step-l3-row-contingency` resolution at line 1078. Append a status-update note onto the existing OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` (cycle-006) recording that the cycle-007 harvester firmed the L4 trajectory shape but did NOT reconcile the L3-form trajectory drop; the gap remains open for cycle-008+ lowering-verifier. Append two new OQs for follow-ups: (a) the GMRES `inner_loop` migration to use `iterate_while` directly (`gmres-inner-loop-iterate-while-migration`); (b) the `iterate_while_pure` sugar — promote as a third firm L4 chapter or keep as sugar (`iterate-while-pure-promotion-decision`)]
```

The new chapter contents follow in full below (these are the bodies the integrator-per-report writes to disk):

---

## Operator content — `book/src/L4/iterate-while.md`

```markdown
# iterate-while

The tail-recursive value-threading loop combinator at L4. Folds a `Step` function over an initial `carry` value, threading the carry forward step-by-step and accumulating per-step readout records (extras) into a trajectory, until the loop predicate `cont` returns `False` on the current carry. The body of the [`solve-monad`](../concepts/solve-monad.md)'s `inner_loop`; the outer fold consumed by [`L4/krylov-step`](./krylov-step.md) (Form A). Companion to [`iterate-while-with-prev`](./iterate-while-with-prev.md), which carries an additional closure parameter for the previous-iteration recurrence carry.

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes iteration, dispatch sites, and effect placement structural. `iterate_while` is the **canonical iteration primitive** at L4: every iterative algorithm in the spec (CG, GMRES, Chebyshev, Arnoldi, transient time-stepping, eigenmode iteration) reduces at L4 to one or more `iterate_while`-folds around per-step kernels.

The L4 strawman (`book/src/design/l4_calculus.md` §3.7) gives this combinator as the v0.3 generalisation of the v0.2 `iterate_while_pure` sketch — generalised to carry per-step extras (a `trajectory`) so that residual histories, monitoring metrics, and breakdown tokens can be returned uniformly through the same combinator. The §3.8 demand-pruning law (`l4_calculus.md:186-213`) ensures that consumers reading only `.final_state` see the trajectory pruned away — the per-step extras are never computed when no downstream consumer reads them.

This chapter is the L4-row anchor for the combinator that the cycle-006 firm L4 entry [`krylov-step`](./krylov-step.md) consumes structurally without anchor (caveat 2 of the harvester's report), and that the cycle-006 wave-2 abstractor theme [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"Speculative L4 operators" proposed as a rough-in. Promoting it closes the cycle-006 open question `iterate-while-l4-anchor-missing`.

`iterate_while` at L4 is a **methodology-level combinator**, not a Palace-source artefact — Palace's iteration loops at L0 are explicit `for`/`while` C++ constructs (e.g., the PCG main loop at `palace/linalg/iterative.cpp:427`, the GMRES inner Arnoldi at `palace/linalg/iterative.cpp:615`). The L4 form names the abstract shape those L0 loops realise. Palace evidence sits at L0 (and in the slice corpus at L2 through L4 v0.4-v0.5 renderings); L4 cites the strawman §3.7 as its conventions source.

## Signature

The L4 signature is the value-threading combinator shape, parameterised by the carry type `α`, the readout-record-extras type `e`, and the implicit `Sim` (`Solve`) monad. The strawman's v0.3 form uses `state` for the carry slot; this chapter uses `carry` to avoid collision with the `SimState` of [`solve-monad`](../concepts/solve-monad.md). The two names refer to the same syntactic role.

**Form (pure, no `Solve` threading)** — the `iterate_while_pure` sugar from `l4_calculus.md:178-183`:

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
- **`extras: { ...e }`** — the per-step readout record. Demand-prunable per §3.8 (`l4_calculus.md:186-213`). Consumers reading the trajectory's per-step extras materialize the computation; consumers reading only `final_state` cause the extras computation to be pruned at the call site. The combinator does not inspect `extras`; it forwards them positionally to the trajectory.
- **result `{ final_state: α, trajectory: [{ ...e }] }`** — a record carrying the final value of the threaded carry plus the list of all per-step extras records (in iteration order). Demand-pruning of `trajectory` cascades into demand-pruning of each `step`'s extras computation, per the chained §3.8 rewrite. When the consumer reads only `final_state`, the per-step `extras` computation in `step` is pruned at every step.

The signature makes four things structural that are merely conventional in source-level loop encodings:

1. **The predicate sees the carry only**, not the extras nor the `SimState`. This forces convergence/termination state into the carry — slices that test on residual norm carry the norm in the carry, not in the extras. (See CG's `s.converged` carry field — set inside the step body from the residual-norm computation, consumed by the predicate.)
2. **The carry is value-threaded; the trajectory is record-spread.** No fold accumulator state outside the carry — anything that needs to persist across iterations is in the carry; anything that is per-step output is in the extras and ends up in the trajectory list. This split mirrors the strawman §3.7's `state` vs `extras` distinction.
3. **The body's monadic effect (when in the Solve form) is on `SimState`, not on the carry.** The carry is a pure value; `SimState` is monad-threaded; the two compose without aliasing because `SimState` lives in the monadic environment and the carry lives in the value-threading.
4. **The trajectory is observed structurally for §3.8 pruning.** The list constructor `[{ ...e }]` is the syntactic site where per-step extras pile up; the §3.8 pruning rule rewrites the body to omit the extras computation when no downstream consumer reads the trajectory. This is the load-bearing simplification that lets one combinator definition serve both "compute residuals for monitoring" and "skip residuals for speed" use cases (per [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)).

## Semantics

`iterate_while` at L4 is the standard tail-recursive value-threading loop, with the per-step extras collected into a trajectory list. The small-step reduction rule is exactly the strawman §3.7 rule (`l4_calculus.md:164-171`):

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

The `iterate_while_pure` sugar (`l4_calculus.md:178-183`) is a closed-form definitional shortcut for the no-extras case:

$$
\textsf{iterate\_while\_pure}\ a\ p\ f \;\equiv\; (\textsf{iterate\_while}\ a\ p\ (\lambda x.\ \{\textsf{state}: f(x)\}))\textsf{.final\_state}
$$

When the step has no per-step readouts to surface (e.g., the LBM step at `l4_calculus.md:374-386`), `iterate_while_pure` is the idiomatic form; the trajectory is uniformly empty and `final_state` is the only field consumed.

Three placement disciplines that the L4 typing enforces (sharpening conventions from the strawman):

- **The predicate is pure on the carry.** No reads of `SimState`, no reads of `OpParams`, no reads of per-step extras. This is structural at L4 because the predicate's type is `α -> Bool` with no monadic effect and no closure over the extras record. If a slice's termination logic requires `SimState.it`, the slice's `α` includes `it` as a field (per `cg.md:217` — `s.it < config.max_it && not s.converged`). If termination requires per-step readouts (e.g., a breakdown token), the readout is folded into the carry by the step body — see [§"Predicate-on-extras"](#predicate-on-extras-anti-pattern) anti-pattern below.
- **The step body's `Solve` effect is on `SimState` only.** The carry transitions are pure value-threading; any monadic effect inside `f` touches `SimState` (typically the iteration counter) and no other monad state. This is the same effect-localisation discipline as [`solve-monad`](../concepts/solve-monad.md) §"What stays out of the monad" — operator applications, dense recurrences, and carry updates are pure; `SimState` writes are monadic.
- **Trajectory pruning is demand-driven, not flag-driven.** Per `derived-view-hoisting.md:19` and `l4_calculus.md:186-213`, when a downstream consumer reads only `final_state`, the per-step extras computation in `f`'s body is eliminated by the §3.8 pruning rewrite. The combinator does not branch on a "compute residuals?" flag — there is no such flag. The L4 form makes residual-monitoring vs. no-monitoring the *same algorithm*, with consumer demand picking which extras get materialised. (Contrast with Palace's L0 `print_opts.iterations`-conditional residual printing at `iterative.cpp:422-426` — at L4 the conditionality disappears.)

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

The L4>L3 theme for `iterate_while` is not yet authored as a standalone `book/src/L4-L3/iterate-while-dissolution.md` chapter — the rotation is described as a sub-component of the `krylov-step-typed-wrapper-dissolution` theme (§"What the L3 form for iterate_while looks like"). **Important caveat**: the existing theme's L3 rendering at `krylov-step-typed-wrapper-dissolution.md:156-167` drops the trajectory — it returns a single `readout` rather than the `[readout]` accumulator that the firm L4 form here keeps (per Law 1). This is the very gap tracked by the cycle-006 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`; this chapter's §"Lowers to" therefore points to the existing theme for the *wrapper-dissolution shape only* and defers the trajectory-shape reconciliation to the cycle-008+ lowering-verifier follow-up. When the dedicated theme lands, this section will be updated to cite it directly.

The L3 form for `iterate_while_pure` is the textbook tail-recursive loop with no accumulator:

```text
iterate_while_pure_L3 :: α -> (α -> Bool) -> (α -> α) -> α
iterate_while_pure_L3 a p f = if p a then iterate_while_pure_L3 (f a) p f else a
```

This L3 form is identity-in-form on the body (no primitive substitution), per the same combinator-miner cycle-002 assertion that justifies `krylov-step` L3>L2 identity. The L3>L2 lowering for the loop combinator itself is *also* identity-in-form (the same tail-recursive shape is L2-native), so the full L4>L3>L2 chain for `iterate_while_pure` collapses to the L4>L3 wrapper dissolution alone.

## Variant axes

The combinator has **three variant axes**, all absorbed at the L4 form-level rather than in the consuming-slice's signature:

1. **Pure vs. Solve-threaded body.** Selected by the slice's choice of `step :: α -> { state: α, ...e }` vs. `step :: α -> Solve { state: α, ...e }`. The two forms share the same combinator definition modulo the body's monadic discharge. The slice picks based on whether the step needs to touch `SimState`. Most algorithmic slices (Krylov solvers, time-stepping, eigensolver iteration) pick the Solve-threaded form to carry the `it` counter; pure-numerical slices (LBM at `l4_calculus.md:374-386`) pick the pure form via `iterate_while_pure`.

2. **Extras-carrying vs. no-extras.** Selected by whether the slice's step returns a non-empty `e` record. Slices that need per-step readouts (CG: `residual_norm`; GMRES: `residual_norm` + `breakdown_token`) carry extras and access `trajectory`. Slices with no readouts (LBM) use the `iterate_while_pure` sugar. The two are unified at the combinator level — `iterate_while_pure` is definitionally `iterate_while` with `e = ()` (and the no-extras case is the §3.8 trivial pruning).

3. **Bootstrap-free vs. carry-bootstrapped.** Selected by which combinator the slice picks — `iterate_while` (this entry) for the bootstrap-free case; [`iterate-while-with-prev`](./iterate-while-with-prev.md) for the variant carrying a `PrevCarry` produced by a separate bootstrap step. The two combinators are not unifiable at the signature level (the `_with_prev` form has different arity), but they are unifiable at the *semantic* level via the carry-projection law (Law 4 of this entry, Law 1 of the companion entry) — `iterate_while_with_prev` with `PrevCarry = ()` reduces to `iterate_while` plus an outer identity step.

## Status

`firm` — small-step semantics inherited verbatim from the L4 strawman §3.7 (`l4_calculus.md:164-171`); the demand-pruning law (Law 1) is the load-bearing property and is inherited from the strawman §3.8 (`l4_calculus.md:186-213`) plus the `derived-view-hoisting` concept; three variant axes (Sim threading, extras carrying, bootstrap-free vs. carry-bootstrapped) are catalogued at the combinator level rather than left to slices to re-discover; the no-laws section catalogues five non-laws explicitly (including the predicate-on-extras anti-pattern and the do-while reordering non-equivalence). The combinator is consumed structurally by [`krylov-step`](./krylov-step.md) (Form A) and by every L4 slice's solve function (`cg.md:215-219` for v0.4 CG; `cg.md:441` for v0.5 CG with the with-prev variant; LBM at `l4_calculus.md:382-385` via the pure sugar). Two new follow-up open questions are filed and one existing OQ (`iterate-while-l3-rendering-trajectory-accumulation-gap`) is augmented with a cycle-007 status note (see §Open questions in this report).

## L4 vs L3 distinction

- **L4**: a single combinator with structural demand-pruning of the trajectory; the body's `Solve`-monad effect is orthogonal to the value-threaded carry; the predicate is purely on the carry; the trajectory is materialised exactly when a downstream consumer reads it.
- **L3**: a tail-recursive loop with explicit `SimState`-positional threading; the §3.8 pruning becomes a *call-site choice* (the slice's step is rendered with or without extras based on the consumer); the trajectory accumulator is either passed through positionally or dropped. The L3 form does not carry the pruning *rule*; it carries the pruning's *result* per call site.

The two layers' entries share signature shape (modulo wrapper dissolution) and small-step semantics on the body. They differ in **effect threading and demand-pruning placement**. The L4>L3 lowering (sub-theme of `krylov-step-typed-wrapper-dissolution`; standalone theme pending the cycle-008+ lowering-verifier follow-up tracked by OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`) erases the monadic packaging and resolves the demand-pruning per consumer.

## Evidence

- `book/src/design/l4_calculus.md:151-184` — the L4 strawman's §3.7 `iterate_while` definition (v0.3 form with extras-carrying step and trajectory accumulator) plus the `iterate_while_pure` sugar. **Canonical reference**: the small-step rule in §Semantics is reproduced verbatim from `l4_calculus.md:164-171`.
- `book/src/design/l4_calculus.md:186-228` — the §3.8 demand-pruning rule that underwrites Law 1. The pruning-as-graph-DCE framing is the calculus-level justification for the trajectory-pruning behaviour.
- `book/src/design/l4_calculus.md:374-386` — the LBM `run_lbm` example at the end of the strawman: `iterate_while_pure` consumed in production. Confirms the no-extras sugar's intended call shape.
- `book/src/L4/krylov-step.md` (cycle-006 firm) — the L4 row consuming this combinator structurally as the body-fold of `inner_loop` (§Semantics, §"L4 vs L2 distinction"). Caveat 2 of that entry's open-questions records the missing-anchor question this dispatch closes.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-006 firm) — §"Speculative L4 operators" carries the rough-in signature this chapter adopts and refines; §"What the L3 form for iterate_while looks like" sketches the L3 tail-recursive form cited in §"Lowers to".
- `book/src/concepts/derived-view-hoisting.md:14-29` — the demand-pruning algebra underwriting Law 1, with the CG residual-norm hoisting worked example as canonical evidence.
- `book/src/concepts/solve-monad.md:1-69` — the `Solve a = StateT SimState Identity a` monad threaded through the Solve-threaded signature; §"What stays out of the monad" articulates the effect-localisation discipline this combinator honours.
- `book/src/spec/slices/cg.md:215-219` — the canonical `iterate_while` call site at L4 v0.4 (`iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`).
- `book/src/spec/slices/cg.md:267-269,277` — the L3↔L4 correspondence notes that explicitly map Palace's `for (; it < max_it && !converged; it++)` to `iterate_while`. **L0 evidence**: `reference/palace/palace/linalg/iterative.cpp:427` (the PCG main-loop predicate-driven `for`-loop) is the canonical Palace iteration shape this combinator names.
- `reference/palace/palace/linalg/iterative.cpp:427` — PCG outer loop. `for (; it < max_it && !converged; it++)` is the canonical Palace iterate_while pattern with bounded `max_it` and convergence flag in the predicate, both folded into the L4 `α` carry per the §Signature predicate discipline.
- `reference/palace/palace/linalg/iterative.cpp:615` — GMRES inner Arnoldi loop. `for (;; j++, it++)` with break-on-converged at line 644 is the second Palace iteration shape; the predicate-in-body break corresponds at L4 to `s.converged` being a carry field set inside the step body and read by the predicate on the next iteration. (The current GMRES slice writes this as a tail-recursive `inner_loop`; migration to `iterate_while` is filed as a cycle-007 follow-up OQ.)

No new Palace L0 source ranges are claimed beyond those already cited; the combinator's L0 evidence base is the existing slice-level citations.
```

---

## Operator content — `book/src/L4/iterate-while-with-prev.md`

```markdown
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

As with [`iterate-while`](./iterate-while.md), the dedicated L4>L3 theme for this combinator is not yet authored as a standalone `book/src/L4-L3/iterate-while-with-prev-dissolution.md`; the rotation is a sub-component of `krylov-step-typed-wrapper-dissolution` (which addresses Form B of `krylov-step` and therefore implicitly the `iterate_while_with_prev` it consumes). **Same caveat as the companion entry**: the existing theme's L3 form at `krylov-step-typed-wrapper-dissolution.md:156-167` drops the trajectory; the firm L4 form here keeps it (Law 2). The cycle-006 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` tracks this discrepancy and routes to cycle-008+ lowering-verifier for reconciliation; this entry inherits the same disposition.

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

Same effect-threading-and-demand-pruning-placement difference as [`iterate-while`](./iterate-while.md). The L4>L3 lowering erases the monadic packaging and resolves the demand-pruning per consumer; it does *not* re-introduce the iteration-zero branch (the rotation is preserved across the lowering).

## Evidence

- `book/src/design/l4_calculus.md:151-184` — the L4 strawman's §3.7 `iterate_while` form that this entry generalises with the bootstrap-and-prev structure.
- `book/src/concepts/first-iteration-unrolling.md:17-37` — the rotation's call-shape (`first_step` / `steady_step` / `iterate_while_with_carry`) that this combinator realises. The strawman's pseudocode driver `iterate_while_with_carry` is renamed `iterate_while_with_prev` at the L4 row level for consistency with the cycle-006 harvester / abstractor signatures.
- `book/src/concepts/first-iteration-unrolling.md:39-55` — the "what gets hidden" / "what is preserved" properties: the `_prev` carry field is gone, the iteration-zero branch is gone, the steady step is branch-free; the algorithm's numerics are identical.
- `book/src/L4/krylov-step.md` (cycle-006 firm) — Form B signature consumes this combinator (`first_step` is the bootstrap, `steady_step` is the steady-step body). The harvester's caveat 2 is closed jointly by this entry and [`iterate-while`](./iterate-while.md).
- `book/src/L4/iterate-while.md` (this dispatch, companion) — Law 1 of this entry states the degeneracy to [`iterate-while`](./iterate-while.md) when `β = ()`.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-006 firm) — §"Speculative L4 operators" carries the rough-in signature `iterate_while_with_prev :: (PrevCarry -> Step) -> PrevCarry -> Step -> carry -> Solve Trajectory` that this chapter adopts and refines. (The refinement: the cycle-006 rough-in signature listed `(PrevCarry -> Step)` as the first argument, which conflates "bootstrap" with "steady-step-parameterised-by-prev"; this chapter splits the two — `bootstrap_step` produces the initial `prev`, `steady_step` consumes and threads `prev` — to match the `cg.md:441` call shape exactly.)
- `book/src/spec/slices/cg.md:393-446` — the canonical v0.5 CG slice using this combinator. The `cg_first_step` / `cg_steady_step` split is the prototypical Form B pair; the call at line 441 `iterate_while_with_prev s1 s0.beta (\(s, _) -> ...) (\(s, beta_prev) -> ...)` is the prototypical use. **Note on closure-argument convention**: the L4 row's `steady_step` signature `((α, β) -> ...)` adopts the *carry-first, prev-second* convention. This matches the [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) pseudo-code at `first-iteration-unrolling.md:34-37` (`\(s, carry) -> (steady_step ... carry s, extract_carry s)` — `s` precedes `carry`) AND the cg.md v0.5 call site at `cg.md:443` (`\(s, beta_prev) -> ...` — `s` precedes `beta_prev`). The L4 row's convention is therefore consistent with both upstream renderings; no v0.6 self-rotation on cg.md is needed.
- `reference/palace/palace/linalg/iterative.cpp:434-441` — Palace's in-step `if (!it) { p = z; } else { linalg::AXPBY(..., beta / beta_prev, p); }` branch. This is the L0 evidence for *what the rotation removes*: the in-step iteration-zero special case that `iterate_while_with_prev` hoists into a bootstrap. Palace itself does not use the unrolled form; the L4 form is a presentation rotation that the Palace source does not realise.
- `reference/palace/palace/linalg/iterative.cpp:451` — the `beta_prev = beta;` line that carries the recurrence variable across iterations in Palace's in-step form. This is the L0 source for the "carry" being threaded; at L4 the carry is moved from a per-iteration local-scope variable into the combinator's closure-threaded `prev`.

No new Palace L0 source ranges are claimed beyond those already cited at `cg.md`; the combinator's L0 evidence base is the existing slice-level citations plus the two iterative.cpp ranges above (which were cited at cg.md but are re-anchored here as direct evidence for the rotation's *target* shape).
```

---

## Operator content — `book/src/L4/index.md` dep-map update (only the dep-map table; rest of file unchanged)

The dep-map table is updated to replace the two rough-in rows with firm rows. The `krylov-step` row is unchanged. Three rows total:

```markdown
| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | Form A: `OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs })`. Form B (first-iteration-unrolled): `first_step :: OpParams -> Krylov -> (SimState -> Solve { sim, krylov, carry, outputs })` and `steady_step :: OpParams -> Krylov -> (PrevCarry -> SimState -> Solve { sim, krylov, carry, outputs })`. | Lowers to L2 [`krylov-step`](../L2/krylov-step.md) via L4>L3>L2 (L4>L3 = state-monad-threading rotation, cycle-006 abstractor; L3>L2 plausibly identity-in-form). Concepts: `state-stratification`, `solve-monad`, `first-iteration-unrolling`, `derived-view-hoisting`, `convergence-test`, `variant-absorption`. L4 rows: [`iterate-while`](./iterate-while.md) (Form A body), [`iterate-while-with-prev`](./iterate-while-with-prev.md) (Form B body). | `firm` (harvested cycle-006; promoted from cross-layer-cross-cutter recommendation 2026-05-27T025354Z) |
| [`iterate-while`](./iterate-while.md) | Pure: `α -> (α -> Bool) -> (α -> { state: α, ...e }) -> { final_state: α, trajectory: [{ ...e }] }`. Solve-threaded: `α -> (α -> Bool) -> (α -> Solve { state: α, ...e }) -> Solve { final_state, trajectory }`. Sugar: `iterate_while_pure :: α -> (α -> Bool) -> (α -> α) -> α`. | Concepts: `solve-monad`, `derived-view-hoisting`, `convergence-test`. L4 rows: consumed by [`krylov-step`](./krylov-step.md) Form A. Lowers to L3 via the body of `krylov-step-typed-wrapper-dissolution` (standalone theme pending cycle-008+ lowering-verifier follow-up per OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`). | `firm` (harvested cycle-007T160550Z; closes cycle-006 OQ `iterate-while-l4-anchor-missing`) |
| [`iterate-while-with-prev`](./iterate-while-with-prev.md) | Pure: `(α -> { state: α, prev: β, ...e }) -> α -> ((α, β) -> { state: α, prev: β, ...e }) -> (α -> Bool) -> { final_state, trajectory }`. Solve-threaded form lifts the step bodies through `Solve`. Degenerates to [`iterate-while`](./iterate-while.md) when `β = ()` (Law 1). | Concepts: `first-iteration-unrolling`, `derived-view-hoisting`, `solve-monad`. L4 rows: [`iterate-while`](./iterate-while.md) (companion / degenerate case); consumed by [`krylov-step`](./krylov-step.md) Form B. Lowers to L3 via the same theme as the companion (standalone follow-up pending per OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`). | `firm` (harvested cycle-007T160550Z; closes cycle-006 OQ `iterate-while-l4-anchor-missing`) |
```

(The rest of `index.md` — opening paragraph, Context, Semantics overlay, "Format expected for each entry", Working Notes — is unchanged.)

---

## Operator content — `book/src/SUMMARY.md` insertion (under the L4 Part)

Insert after the existing `- [krylov-step](./L4/krylov-step.md)` line (currently line 8):

```markdown
- [iterate-while](./L4/iterate-while.md)
- [iterate-while-with-prev](./L4/iterate-while-with-prev.md)
```

The two new chapters become chapter slots 3 and 4 of the L4 Part (after Overview and `krylov-step`).

---

## Operator content — `scaffolding/open-questions.md` append (status updates + two new OQs)

**Status update on existing OQ** (cycle-006 entry, slug `iterate-while-l4-anchor-missing`):

The integrator-per-report applying this dispatch should edit the YAML frontmatter of the `iterate-while-l4-anchor-missing` ledger block (currently at `scaffolding/open-questions.md:1062-1069`) to flip `status: open` → `status: answered` and add two new keys, matching the cycle-006 `krylov-step-l3-row-contingency` resolution schema at `scaffolding/open-questions.md:1078`:

```yaml
---
slug: iterate-while-l4-anchor-missing
opened_at: cycle-006
opened_by: harvester
status: answered
answered_at: cycle-007
answered_in: reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/ (closes the OQ in favour of the "L4 row" resolution: both `iterate_while` and `iterate_while_with_prev` land as firm L4 rows with their own variant-axis profile and demand-pruning law)
---
```

The body of the cycle-006 OQ ("either `iterate_while` should land as a concept page (sibling to `solve-monad`) or as an L4 row") is resolved in favour of the second option.

**Status update on existing OQ** (cycle-006 entry, slug `iterate-while-l3-rendering-trajectory-accumulation-gap`):

The integrator-per-report should append the following note to the body of the existing `iterate-while-l3-rendering-trajectory-accumulation-gap` ledger block (currently at `scaffolding/open-questions.md:1177-1185`), keeping the block's `status: open`:

> **Cycle-007 update**: the cycle-007 harvester on the L4 loop-combinator family (`reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/`) firmed the L4 signature with an explicit trajectory accumulator `[{ ...e }]` and the demand-pruning law (Law 1 of [`book/src/L4/iterate-while.md`](../book/src/L4/iterate-while.md)). The harvester did NOT reconcile the L3 form (which still drops the trajectory per `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like" lines 156-167). The gap remains for cycle-008+ lowering-verifier: dispatch on `iterate-while-l4-l3` to author a standalone `book/src/L4-L3/iterate-while-dissolution.md` theme reconciling the L3 rendering with the firm L4 trajectory shape. The cycle-007 harvester explicitly scoped this out per the "one operator per invocation" discipline.

(Note to integrator: this update modifies an existing ledger block, not a new appended block. The two candidate resolutions enumerated in the original cycle-006 OQ body — (a) trajectory accumulator pass-through; (b) explicit demand-pruning step — are still the live options; the cycle-007 harvester did not pick between them.)

**Two new OQs to append** (any-agent-appendable per the role-spec):

```yaml
---
slug: gmres-inner-loop-iterate-while-migration
opened_at: cycle-007
opened_by: harvester
status: open
relates_to: iterate-while-l4-anchor-missing (cycle-006, answered cycle-007)
---
```

The cycle-007 harvester on the iterate-while family settled the L4 anchor for `iterate_while` (Form A) and `iterate_while_with_prev` (Form B). The cycle-005 GMRES slice's L4 section (`book/src/spec/slices/gmres.md:459-470`) renders `inner_loop` as an inline tail-recursive `Solve`-monad function (`inner_loop op conv K = do ... if conv.satisfied K3.beta || K3.j + 1 == op.max_dim || s.it == op.max_it then pure K3 else inner_loop op conv K3{ j = K3.j + 1 }`) rather than as a call to `iterate_while`. With the L4 row now firm, the GMRES rendering can be migrated to use `iterate_while` directly, surfacing the predicate (`\K -> not (conv.satisfied K.beta) && K.j + 1 < op.max_dim && s.it < op.max_it`) and the step body (`\K -> do { ... ; pure { state: K3{ j = K3.j + 1 }, ... } }`) as separate functions. **Benefits**: matches the CG v0.4 rendering pattern (`cg.md:215-219`); makes the trajectory shape explicit (GMRES extras are `{ residual_norm: Scalar, breakdown_token: BreakdownTag }`); enables Form-B adoption if the cycle-007/008 first-iteration-unrolling analysis on GMRES finds it warranted. **Cost**: a self-rotation v1.0→v1.1 on `gmres.md` §L4; needs a lifter or abstractor dispatch. **Routes to cycle-008+ lifter** on `gmres §L4`. Source: `reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/CYCLE.md` §"Open questions / caveats" item 2.

```yaml
---
slug: iterate-while-pure-promotion-decision
opened_at: cycle-007
opened_by: harvester
status: open
relates_to: iterate-while-l4-anchor-missing (cycle-006, answered cycle-007)
---
```

The cycle-007 harvester on the iterate-while family settled `iterate_while` and `iterate_while_with_prev` as two firm L4 rows. The strawman §3.7 also names `iterate_while_pure :: α -> (α -> Bool) -> (α -> α) -> α` as a sugar for the no-extras case; this is used by the LBM example (`l4_calculus.md:374-386`). The cycle-007 harvester adopted the sugar inside [`iterate-while`](./L4/iterate-while.md) §Semantics as a definitional shortcut (`iterate_while_pure a p f ≡ (iterate_while a p (\x -> { state: f(x) })).final_state`) rather than as a separate L4 row. **Two candidate resolutions** (deferred): (a) keep the sugar inside `iterate-while` as a definitional reduction; future slices invoking the no-extras pattern reference the sugar inline. (b) promote `iterate_while_pure` to a third firm L4 row with its own chapter; the chapter would be ~1/3 the size of `iterate-while` since most laws and discipline are identical. **Cost-benefit**: (a) keeps the L4 vocabulary small but spreads the sugar usage across slice-level pseudo-code; (b) gives sliceauthors a one-line `iterate_while_pure` to reference but adds a row whose primary content is "see `iterate-while` Laws 1-4". **Routes to cycle-008+ harvester or planner**: defer decision until a second non-Krylov slice (e.g., LBM at a future Palace transient solver write-up, or a per-element time-step iteration) actually needs the sugar enough to outweigh the "see also iterate-while" cross-reference cost. Source: `reports/2026-05-27T160550Z-harvester-iterate-while-family-L4/CYCLE.md` §"Open questions / caveats" item 3.

---

## Supporting evidence

Citations are listed inline in each chapter's §Evidence section. Cross-cutting summary:

- **L4 strawman** (`book/src/design/l4_calculus.md` §3.7, §3.8) — primary source for both chapters' small-step semantics and the demand-pruning law. The chapters cite and continue the strawman per the CLAUDE.md "L4 strawman is in-management" invariant.
- **Cycle-006 firm L4 chapter** (`book/src/L4/krylov-step.md`) — precedent for L4 chapter shape; cited by both chapters as the consumer of the combinators.
- **Cycle-006 firm L4>L3 theme** (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) — §"Speculative L4 operators" carries the rough-in signatures this dispatch refines; §"What the L3 form for iterate_while looks like" provides the L3 sketch cited in §"Lowers to" of both chapters.
- **Concept pages** — `derived-view-hoisting.md` (demand-pruning algebra), `first-iteration-unrolling.md` (the rotation `iterate_while_with_prev` realises), `solve-monad.md` (the monad threaded through the Solve-threaded form), `convergence-test.md` (the `Convergence` value consumed by predicates).
- **Slice corpus** — `cg.md:215-219, 393-446` (the canonical call sites at L4 v0.4 and v0.5); `gmres.md:459-470` (the inline-tail-recursive form that the cycle-007 OQ flags for migration).
- **Palace L0 source** — `iterative.cpp:427` (PCG outer-loop iterate_while), `iterative.cpp:434-441` and `:451` (the in-step iteration-zero branch and `beta_prev` carry that `iterate_while_with_prev` rotates away), `iterative.cpp:615` (GMRES inner-loop predicate-in-body iterate_while pattern).

## Open questions / caveats

1. **L3 trajectory-accumulator vs. readout collapse** (existing cycle-006 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` updated with a cycle-007 note): the cycle-006 abstractor's L3 rendering of `iterate_while` returns a single `readout` rather than a `[readout]` trajectory; the L4 form here keeps the trajectory. A standalone L4>L3 theme for the combinator (separate from the `krylov-step-typed-wrapper-dissolution`) should reconcile this. Out of scope for this dispatch (harvester, not lowering-verifier). No new OQ filed — the existing cycle-006 OQ already captures the same gap with the same two candidate resolutions; the integrator-per-report updates its body with a cycle-007 status note rather than appending a duplicate ledger entry.

2. **GMRES inner_loop migration** (already filed as OQ above): GMRES currently writes the inner loop as a hand-rolled tail-recursive `Solve` function; it could now consume `iterate_while` directly. A v1.0→v1.1 self-rotation on `gmres.md` §L4 is the natural follow-up. Out of scope for this dispatch (would touch a slice file outside the L4-chapter scope).

3. **`iterate_while_pure` promotion decision** (already filed as OQ above): kept as sugar inside [`iterate-while`](./L4/iterate-while.md) §Semantics for now; promotion to a third L4 row deferred until a second non-Krylov slice exercises it.

4. **CG v0.5 closure-argument position** (reconciled in repair): the L4 row's `steady_step` signature uses `(α, β)` (carry first, prev second), matching both the `first-iteration-unrolling.md:34-37` pseudo-code (`\(s, carry) -> ...`) and the cg.md v0.5 call site at line 443 (`\(s, beta_prev) -> ...`). An earlier draft inverted this; the §Evidence note is now consistent with the cited renderings. No follow-up OQ needed.

5. **Concept-page-dependencies-vs-L4-row-dependencies** (inherited from cycle-006 harvester's caveat 1, OQ `l4-row-dependencies-on-concept-pages-vs-other-l4-rows`): both new chapters list concept-page links in their §Dependencies. The cycle-006 OQ is still open; both chapters are written to honour either resolution (concept-deps OK, or promote-the-concepts) — only the link targets would change. Not addressed by this dispatch.

6. **`Solve` monad's `>>=` semantics for trajectory accumulation**: the chapters' Solve-threaded form lifts the small-step rule mechanically through the monad. A more rigorous treatment would write out the `StateT`-specific reduction (the trajectory is built bottom-up by the recursion, which is non-trivial under strict `StateT` evaluation). The current treatment is informally correct for a lazy or call-by-need `StateT`; if the calculus pins call-by-value semantics for `Solve`, the trajectory-build order may need an explicit `reverse` step. Filed as a low-priority refinement; the cycle-006 `solve-monad` concept page does not commit to evaluation order. Not addressed by this dispatch.

## Layer-intro refresh note

The L4 index.md's current "Semantics (overlay)" section reads "To be drafted as L4 operators are formalized through the harvester agent pipeline. The L4 calculus strawman lives at `../design/l4_calculus.md` and seeds the formal core." With three firm L4 rows now (after this dispatch lands), a layer-intro-author refresh on `book/src/L4/index.md` is warranted to surface: (a) the combinator-family unification across `iterate-while` + `iterate-while-with-prev` + `krylov-step` Form A/B; (b) the predicate-on-carry-only convention as an L4-wide discipline; (c) the demand-pruning-on-trajectory law as the load-bearing simplification at L4. Out of scope for this dispatch (harvester does operators, not layer intros); flagged for cycle-008+ layer-intro-author. The current `index.md` text is not blocking integration.

---

## codemap-pilot-instrumentation

**Tool-call count by tool**:

- `mcp__palace-codemap__search_text`: 1 call attempted, **PERMISSION DENIED** (`Permission to use mcp__palace-codemap__search_text has been denied.`).
- `mcp__palace-codemap__get_symbol_def`: 1 call attempted, **PERMISSION DENIED** (same error mode).
- `mcp__palace-codemap__list_files`: 0 calls (gave up after first two denials).
- `mcp__palace-codemap__get_file_subtree`: 0 calls.
- `mcp__palace-codemap__get_call_sites`: 0 calls.
- `mcp__palace-codemap__list_dependencies`: 0 calls.
- `mcp__palace-codemap__read_range`: 0 calls.

Vanilla equivalent calls actually used:
- `Bash(grep -n "for (int it" /home/.../iterative.cpp)`: 1 call.
- `Bash(grep -nE "while \(|for \(int it" /home/.../iterative.cpp)`: 1 call.
- `Bash(ls /home/.../linalg/)`: 1 call.
- `Bash(ls /home/.../linalg/ | grep -iE "iterative|ksp|cg|gmres")`: 1 call.
- `Bash(grep -n "while\|for (" /home/.../iterative.cpp)`: 1 call (the productive one — surfaced lines 427, 615, etc.).
- `Read(/home/.../iterative.cpp, offset=395-485)`: 1 call.
- `Read(/home/.../iterative.cpp, offset=605-645)`: 1 call.

Total vanilla: ~5 grep + 2 Read = 7 calls on Palace L0 source.
Total codemap: 0 productive calls (2 denied).

**Estimated wall-time per call class**: codemap unmeasured (both calls failed before returning data). Vanilla `Bash(grep -n ...)` returned in well under a second for each invocation; `Read` with explicit offset+limit returned in ~half a second. The combined L0-localization effort (find the iteration-loop shape in iterative.cpp; read the canonical loop body and the GMRES inner) took ~30 seconds of tool time end-to-end, dominated by my own reading of the returned output rather than tool wall-time.

**Coverage**: codemap surfaced nothing (both calls denied). Vanilla grep + Read fully covered the L0 evidence needs — found `for (; it < max_it && !converged; it++)` at line 427, the `if (!it) { p = z; } else { ... }` first-iteration branch at lines 434-441, the `beta_prev = beta;` carry at line 451, and the GMRES inner `for (;; j++, it++)` at line 615. Nothing was missed that a codemap call might have found. **However**: had the harvester needed to find *all* call sites of `iterative.cpp:CgSolver::Mult` across the Palace tree (e.g., for a "who consumes this iteration?" cross-cut), `get_call_sites` would have been the cheaper choice over a tree-wide grep — that capability would have been a real win on a different task shape.

**False negatives observed**: none from codemap (no codemap results to compare). No false negatives from vanilla grep either — every loop pattern I needed surfaced on the first or second grep invocation.

**Friction observations**:
- **Permission denial is the dominant friction**. Both attempted codemap calls returned `Permission to use mcp__palace-codemap__... has been denied` with the standard advisory message. Per the CLAUDE.md "Escalate process issues, don't work around indefinitely" feedback memo, this is the kind of harness/permission friction that should be raised rather than worked around. The harvester-pilot value of the codemap server is *zero* under the current permission posture; the planner / user should know.
- **Path-format**: codemap docs say "All paths relative to the target repo root (e.g., `palace/linalg/ksp.cpp`)" — readable, but it would have been useful to have a one-line confirmation on the first `list_files` call that the targeting is correct. (Not exercised here due to permission denial.)
- **Tool-call shape mismatch**: harvester work is dominated by reading book/ artefacts (40% of this dispatch's reads) and only secondarily by reading Palace L0 (15%). Codemap's value is concentrated in the L0 segment; permission denial removes its only relevant slice. Even if granted, the harvester role would see codemap value only on dispatches that need broad L0 exploration — which is a minority of harvester invocations.

**Verdict for broad role-spec rollout**:

**Recommend AGAINST broad rollout for harvester** in the current permission posture: zero codemap calls succeeded, no value delivered, and the harvester role spends most of its tool budget on book/ reads (which codemap does not address). **Conditionally recommend FOR rollout for lowering-verifier and cross-cutters** *if and only if* the permission posture is fixed — those roles do more L0-source corroboration and would see real `get_call_sites` / `search_text` / `get_symbol_def` win. **Recommend FOR combinator-miner** *if permission posture is fixed* — combinator-miner specifically scans for recurrent patterns across the L0/L1 corpus, which is exactly the `search_text` + `get_call_sites` workload codemap is built for.

**Single-paragraph recommendation**: Pause the codemap rollout-to-roles step (priority #16 step d) until the permission posture is fixed; the pilot signal is dominated by permission denial, not by tool ergonomics or capability gaps. Once permissions resolve, prioritise combinator-miner first (highest expected value), lowering-verifier second, cross-cutters third. Harvester sees minimal value on its typical workload and can be deferred. The instrumentation here is a *structural* finding (permission posture blocks pilot) rather than a *capability* finding (the tools themselves were not exercised enough to judge).
