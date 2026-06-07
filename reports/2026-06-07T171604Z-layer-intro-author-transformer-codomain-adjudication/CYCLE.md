---
agent: layer-intro-author
invoked_at: 2026-06-07T171604Z
scope: PIN the operator-transformer-codomain adjudication into semantics §1.3.1 (oq-highorder-operator-transformer-codomain-convention)
status: integrated
integrated_at: 2026-06-07T193500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-129 D1 (LEAD, WAVE-1). Applied clean by integrator-per-report (staging row 1). Pinned the operator-transformer/-constructor codomain adjudication into semantics §1.3.1 (book/src/semantics/index.md — ruling bullet after the :155 reconciliation paragraph + a "Grouping" column + a third opaque-LinearOperator[N,N] row to the §1.3.1 table); bracketed Op[...]/LinOp[...] = already compliant, opaque LinearOperator[...] = the smell (re-spell-not-wrap). RESOLVES OQ oq-highorder-operator-transformer-codomain-convention (RESOLVED marker = batch-41 meta unify-authority; report did NOT edit open-questions.md). Supplied the scope predicate D2's sweep consumed. NO status/rank/edge change (semantic-surface prose only; no-op on graded-stack). Build EXIT 0; ZERO finalize build-repairs. All totals HELD vs c127/c128.
---

# CYCLE: semantics §1.3.1 — operator-transformer-codomain adjudication PIN

## Summary

Cycle-129 D1 (LEAD, WAVE-1). PIN the open adjudication
`oq-highorder-operator-transformer-codomain-convention` into the now-landed
§1.3.1 ("Closure-returning signatures") of the active-management semantic
surface `book/src/semantics/index.md`.

**The question settled:** does an operator→operator TRANSFORMER (a high-order
op whose codomain is *itself* an operator value), e.g.
`eliminate_essential_bc :: ... -> LinOp[$S, $S]` (`book/src/L4/eliminate_bc.md:83-84`),
which already writes its codomain in the **bracketed operator-value spelling**
`LinOp[...]` / `Op[τ_in → τ_out]`, ALREADY satisfy the §1.3.1
closure-returning-signature convention — or does it need additional outer
paren-grouping `-> (... -> ...)`?

**Ruling (the recommended reading, confirmed against the on-disk §1.3.1 text):
BRACKETED = ALREADY COMPLIANT.** §1.3.1 as authored in c128 already states
(`semantics/index.md:155`) that `Op[τ_in → τ_out]` is the operator-VALUE
spelling and that "the brackets already group the in/out arrow, so the codomain
is unambiguous without outer parens." The outer paren-grouping habit
(`foo -> (bar -> baz)`) is therefore for the **bare closure-type form ONLY**,
NOT for the bracketed `Op[...]` / `LinOp[...]` form. An operator-value codomain
written `Op[...]` / `LinOp[...]` carries the in/out arrow *inside* its brackets
— the bracket IS the grouping — so it needs no further change. The
**non-compliant smell** is specifically the **opaque type-application form**
(`LinearOperator[N,N]` / `LinearOperator (Tensor[...])`) that hides the closure
intent behind an undifferentiated type application and gives no in/out arrow.

The pin makes this explicit for the operator-TRANSFORMER / operator-CONSTRUCTOR
case (the case the existing §1.3.1 text implied but did not name): it adds a
short clause to the third bullet's reconciliation paragraph, and appends an
**operator-transformer / -constructor row** to the §1.3.1 `Op[…]`-vs-bare-closure
table. Prose-only on the semantic surface — NO status/rank/edge change, NO L4
chapter edits (those are D2).

## Proposed changes

### 1. Extend the §1.3.1 reconciliation clause (pin the operator-transformer ruling)

```edit:book/src/semantics/index.md
[old]:  `Op[τ_in → τ_out]` is the **specialization** of the bare closure type `(τ_in -> τ_out)` for the second ownership category of §2 (*operator internal parameters*): an `Op` value's closed-over data is `!`-tagged by construction and is read-only across a solve, and it is eliminated by `apply` (§3.5) rather than by bare juxtaposition. Prefer `Op[…]` whenever the returned closure is an operator instance with closed params (the matrix-free FE operator, a preconditioner, a constructed step); reserve the bare `(τ_in -> τ_out)` for a genuinely plain returned function (e.g. a predicate or a continuation with no operator-parameter closure). Both forms benefit from the same paren-grouping habit; for `Op[…]` the brackets already group the in/out arrow, so the codomain is unambiguous without outer parens — `mk :: A -> B -> Op[X → Y]` already reads "returns an operator."
[new]:  `Op[τ_in → τ_out]` is the **specialization** of the bare closure type `(τ_in -> τ_out)` for the second ownership category of §2 (*operator internal parameters*): an `Op` value's closed-over data is `!`-tagged by construction and is read-only across a solve, and it is eliminated by `apply` (§3.5) rather than by bare juxtaposition. Prefer `Op[…]` whenever the returned closure is an operator instance with closed params (the matrix-free FE operator, a preconditioner, a constructed step); reserve the bare `(τ_in -> τ_out)` for a genuinely plain returned function (e.g. a predicate or a continuation with no operator-parameter closure). Both forms benefit from the same paren-grouping habit; for `Op[…]` the brackets already group the in/out arrow, so the codomain is unambiguous without outer parens — `mk :: A -> B -> Op[X → Y]` already reads "returns an operator."

- **An operator-VALUE codomain written `Op[…]` / `LinOp[…]` is ALREADY COMPLIANT — the bracket IS the grouping (the operator-transformer / -constructor ruling).** The outer paren-grouping habit (`foo -> (bar -> baz)`) is for the **bare closure-type form only**. When the codomain is instead written in a bracketed operator-value spelling — an operator **constructor** `mk :: A -> B -> Op[X → Y]` (codomain is a freshly-built operator) **or** an operator **transformer** `t :: Op[X → Y] -> … -> Op[X' → Y']` (an operator-in → operator-out map, e.g. `eliminate_essential_bc :: LinOp[(S: ...), $S] -> DofSet[N] -> DiagPolicy -> LinOp[$S, $S]`) — the in/out arrow is carried **inside** the brackets, so the closure intent is already syntactically explicit and **no additional outer parens are wanted** (`-> (… -> …)` around an `Op[…]` codomain would be redundant noise). A bracketed operator-value codomain stands as-is. The **non-compliant smell** this convention targets is specifically the **opaque type-application form** — `LinearOperator[N,N]` / `LinearOperator (Tensor[…])` — which applies a bare type name to dimension/argument slots, gives **no in/out arrow**, and so **hides** the higher-order intent. The fix for an opaque-form codomain is to re-spell it in the bracketed operator-value form (`Op[Tensor[$N] → Tensor[$N]]`, or the square-operator `LinOp[(N: ...), $N]` form of §1.2.2), NOT to wrap the opaque form in outer parens. A codomain already in `Op[…]` / `LinOp[…]` form is therefore *out of scope* for any "ungrouped closure codomain" compliance sweep.
```

### 2. Append the operator-transformer / -constructor row to the §1.3.1 table

```edit:book/src/semantics/index.md
[old]:  | Form | Meaning | Use when |
  |---|---|---|
  | `... -> (τ_in -> τ_out)` | the **general closure type** — a bare function value, applied directly by juxtaposition `(g x)` | the returned value is a *plain function* with no closed-over operator-parameter state worth naming, applied directly |
  | `... -> Op[τ_in → τ_out]` | the **operator-VALUE spelling** (§1.1 `Op[_]` type) — a closure-with-closed-params + body lambda, applied via the `apply` term (§3.5) | the returned value is a **named operator** carrying closed-over `!`-shareable parameters (matrix/basis/geometry tables, factorizations) — an *operator instance* in the §2 ownership sense, applied `apply A v` |
[new]:  | Form | Meaning | Use when | Grouping |
  |---|---|---|---|
  | `... -> (τ_in -> τ_out)` | the **general closure type** — a bare function value, applied directly by juxtaposition `(g x)` | the returned value is a *plain function* with no closed-over operator-parameter state worth naming, applied directly | **outer parens wanted** — group the bare closure codomain `-> (τ_in -> τ_out)` |
  | `... -> Op[τ_in → τ_out]` | the **operator-VALUE spelling** (§1.1 `Op[_]` type) — a closure-with-closed-params + body lambda, applied via the `apply` term (§3.5) | the returned value is a **named operator** carrying closed-over `!`-shareable parameters (matrix/basis/geometry tables, factorizations) — an *operator instance* in the §2 ownership sense, applied `apply A v` | **already grouped** — the brackets carry the in/out arrow; NO outer parens (an operator **constructor** `mk :: A -> Op[X → Y]` or **transformer** `t :: Op[X → Y] -> Op[X' → Y']` is compliant as-is) |
  | `... -> LinearOperator[N,N]` (opaque type-application) | a bare type name applied to dim/arg slots — **no in/out arrow**, the higher-order intent is hidden | **avoid** — this is the non-compliant smell | **re-spell**, do not wrap — rewrite to `Op[Tensor[$N] → Tensor[$N]]` or square-op `LinOp[(N: ...), $N]` (§1.2.2); wrapping the opaque form in outer parens does NOT make it compliant |
```

## Adjudication ruling (the one-line answer)

**A bracketed operator-value codomain (`Op[…]` / `LinOp[…]`) is ALREADY
COMPLIANT — the bracket is the grouping.** The §1.3.1 outer paren-grouping
convention applies to the **bare closure-type form only**. The non-compliant
smell is the **opaque type-application form** `LinearOperator[N,N]` /
`LinearOperator (Tensor[...])` (no in/out arrow → hidden intent); its fix is to
**re-spell** it as `Op[Tensor[$N] → Tensor[$N]]` (or the square-op
`LinOp[(N: ...), $N]` of §1.2.2), NOT to wrap it in outer parens.

This is consistent with — and makes explicit, for the operator-TRANSFORMER and
operator-CONSTRUCTOR cases — the existing §1.3.1:155 statement that for `Op[…]`
"the brackets already group the in/out arrow, so the codomain is unambiguous
without outer parens." It does not contradict or duplicate the landed text; it
extends it.

## Consequence for D2 (the WAVE-2 lifter sweep) — explicit

**`eliminate_essential_bc` is OUT of the non-compliant sweep cohort — it is
already compliant.** Its codomain at `book/src/L4/eliminate_bc.md:83-84` is the
bracketed `LinOp[$S, $S]` (an operator-in → operator-out transformer); under
this ruling the bracket already carries the in/out arrow, so it stands as-is.
Likewise the `L4/index.md` dep-map TABLE rows that are already bracketed
(`:110` `assemble_frequency_operator` `LinOp[(S: ...), $S]`; `:114`
`eliminate_bc` `LinOp[(S: ...), $S] -> ... -> LinOp[$S, $S]`) are **already
compliant — D2 must NOT rewrite them.**

**IN the sweep cohort (the opaque `LinearOperator[...]` applied-spelling
sites):**
- `assemble_frequency_operator.md` signature codomain `:99`, restated sig
  `:293`, the closure-valued record field `FrequencyOperatorFamily.A2` `:106`,
  and its prose restatement `:127` — all `-> LinearOperator[N, N]` / `Scalar ->
  LinearOperator[N, N]` opaque forms → re-spell to `Op[Tensor[$N] → Tensor[$N]]`
  (or `LinOp[(N: ...), $N]`).
- `fe_assemble.md` `:60` (`-> LinearOperator[N, N]`), `:35`/`:71`
  (`assemble_term :: ... -> LinearOperator[N, N]`) — opaque forms → re-spell.
- `L4/index.md` chapter-list-NARRATIVE rows (the applied-spelling sites D2 must
  on-disk re-localize — the OQ `:61,62` drifted): the `fe_assemble` narrative
  (`assemble_term :: ... -> LinearOperator[N,N]`) and the `eliminate_bc`
  narrative (`eliminate_essential_bc :: LinearOperator[N,N] ->
  LinearOperator[N,N]` — note this narrative uses the **opaque** spelling even
  though the chapter `:83-84` and the TABLE row `:114` use the **bracketed**
  compliant form) → re-spell the opaque narrative to match the bracketed
  chapter/table form (`LinOp[(S: ...), $S] -> ... -> LinOp[$S, $S]`).

**The `eliminate_bc` chapter↔index reconcile (D2):** the *direction* of the
reconcile is now pinned — the chapter `:83-84` and the index TABLE row `:114`
(both bracketed) are the CANONICAL form; the index chapter-list NARRATIVE row's
opaque `LinearOperator[N,N] -> LinearOperator[N,N]` spelling is the side that
moves, to agree with the bracketed canonical form. (Bracketed-is-compliant ⇒
the bracketed side does not change.)

Net: the ruling NARROWS D2's sweep to the opaque-`LinearOperator[...]` sites in
the two chapter bodies + the two narrative index rows; the bracketed
`eliminate_bc` chapter/table sites and the bracketed `assemble_frequency_operator`
TABLE row stand untouched.

## Supporting evidence

- `book/src/semantics/index.md:130-165` — the c128-landed §1.3.1 (paren-grouping
  convention `:134-146`; the `Op[…]`-vs-bare-closure table `:151-153`; the
  reconciliation clause ending `:155` "the brackets already group the in/out
  arrow, so the codomain is unambiguous without outer parens").
- `book/src/semantics/index.md:95` — §1.2.2 already sanctions `LinOp[(S: ...),
  $S]` as the rank-agnostic square-operator calculus spelling (the
  `LinearOperator[M, N]` rank-1 form is faithful only at L1/L0).
- `book/src/L4/eliminate_bc.md:83-84` — the operator-transformer in question, its
  codomain already bracketed `LinOp[$S, $S]`.
- `reports/2026-06-07T171246Z-cycle-planner-cycle-129/CYCLE.md` D1+overlap
  sections — the scope-gate framing and the D2 dependency.

## OQ resolution marker

`oq-highorder-operator-transformer-codomain-convention` — **RESOLVED** by this
pin (bracketed operator-value codomain = already compliant; opaque
type-application form = the non-compliant smell, re-spell not wrap). The OQ text
notes the resolution-marker append authority is the batch-41 meta (header-close
unify-authority), so this report does NOT itself edit `scaffolding/open-questions.md`;
flagging the RESOLVED disposition here for the meta to land. (The plan's D1
note also routes the marker append through the meta's unify-authority.)

## Open questions / caveats

- The two META-owned follow-on OQs are deliberately NOT touched here (per the
  plan): (a) `closure-signature-introduction-form-into-bnf-and-role-discipline-bullet`
  (promote the `op-with-params {…}` introduction form into the §1.3 BNF + add a
  producer USE+LINK discipline bullet); (b)
  `closure-signature-l4-constructor-restatement-compliance-cohort-sweep` (the
  whole-book L4-constructor compliance sweep). This pin supplies the *scope
  predicate* that cohort sweep will use ("opaque `LinearOperator[...]`
  type-application = in-scope; bracketed `Op[…]`/`LinOp[…]` = compliant").
- No status/rank/edge change; the semantic surface is the §0.1-governed
  active-management surface, not a rank'd DAG node — RE baseline holds unchanged
  (consistent with the plan's "NO RE fires" note).
