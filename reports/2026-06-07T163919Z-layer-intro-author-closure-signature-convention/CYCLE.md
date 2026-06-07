---
agent: layer-intro-author
invoked_at: 2026-06-07T163919Z
scope: closure-returning-signature convention — semantics surface §1.3.1 + mk_matrix_free_operator exemplar
status: pending
integrated_at: 2026-06-07T170138Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-128 D1 (batch-41 MIDDLE) applied clean by integrator-per-report (all 5 proposed-changes blocks incl. the repairer-added feature-column Change 5); finalize applied the TWO flagged lockstep consistency fixes (L4/index.md:119 dep-map mirror + the D4 L2-pointer signature mention, both LinearOperator(...)->Op[...]); semantics §1.3.1 landed; NO status/rank/edge change (graded-stack no-op, all totals HELD); 3 OQs promoted (2 routed to batch-41 meta)."
---

# CYCLE: closure-returning-signature notation convention (D1 LEAD, cycle-128 batch-41)

## Summary

USER DIRECTIVE (2026-06-07): the L4 calculus is high-order — a signature's domain and codomain may themselves be function types — and when a signature's **intended use is to yield a closure**, the closure sub-signature is **grouped in parens** so the higher-order intent is syntactically explicit (`foo -> (bar -> baz)`, not `foo -> bar -> baz` read as a 3-ary curried call producing `baz`). Per the SEMANTIC-CONSOLIDATION directive this convention lives ONCE at the semantic surface; operator chapters USE+LINK.

Two deliverables:

1. **Codify the convention** into the semantic surface `book/src/semantics/index.md` as a new **§1.3.1 "Closure-returning signatures (the calculus is high-order)"** — a sibling to §1.2.1 named-shape-groups. It (a) states the calculus is high-order; (b) gives the paren-grouping convention for closure codomains; (c) reconciles with the existing §1.1 `Op[τ_in → τ_out]` type by distinguishing the **bare closure-type form** `(τ_in -> τ_out)` from the **operator-VALUE spelling** `Op[τ_in → τ_out]`, with an explicit rule for when to use which; (d) gives the explicit term-level form of an operator value, **resolving the §Working-Notes line-518 gap**; and updates the §v0.2 iteration-log note (line 494) which currently says the curried-`Op` pattern "isn't a calculus extension, just a convention" — this directive promotes it to a stated, first-class convention with a back-reference.

2. **Fix the `mk_matrix_free_operator` exemplar** at `book/src/L4/mk_matrix_free_operator.md:60`. The codomain `LinearOperator (Tensor[(N: ...)])` (an opaque record-applied-to-type, obscuring the closure intent) becomes the **operator-VALUE spelling** `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` — chosen because the result is a *named operator value* carrying closed-over params (FE space / geometry factors / basis) whose action is run via `apply` (the chapter's own apply-lowering at :68-72 does exactly `apply (mk_matrix_free_operator …) v`). A USE+LINK back-reference to §1.3.1 is added; the rule itself is NOT restated in the chapter.

## Proposed changes

### Change 1 — `book/src/semantics/index.md`: add §1.3.1 (closure-returning signatures)

Insert a new subsection immediately AFTER the §1.3 Terms grammar block (after the `do`-block-statement sentence at line 128, before `## 2. Ownership categories` at line 130).

```edit:book/src/semantics/index.md
[old]: A `do`-block statement `s` is either `x ← e` (monadic bind), `let x = e` (pure binding), or just `e` (side-effect-only call returning `Sim ()`).

## 2. Ownership categories
[new]: A `do`-block statement `s` is either `x ← e` (monadic bind), `let x = e` (pure binding), or just `e` (side-effect-only call returning `Sim ()`).

#### 1.3.1 Closure-returning signatures (the calculus is high-order)

L4 is a **high-order calculus**: a function/operator signature's domain *and* codomain may themselves be function types (the `τ₁ → τ₂` and `Op[τ_in → τ_out]` type formers of §1.1). A constructor whose *intended use is to yield a closure* — a value that is **applied later**, not a fully-evaluated result — must make that higher-order intent **syntactically explicit**, so the closure codomain is not misread as the final argument of a still-curried call.

- **The paren-grouping convention.** When a signature's codomain is a closure (its intended use is to be applied later), **group the closure sub-signature in parens**:

  ```text
  example :: foo -> (bar -> baz)
  ```

  reads "`example` takes a `foo` and **returns a closure** `bar -> baz`" — the result of `example x` is *itself a function* awaiting a `bar`. This is **deliberately distinct** from the un-parenthesized

  ```text
  example :: foo -> bar -> baz
  ```

  which — although `->` associates right, so the two are the *same type* — by convention signals an ordinary **fully-curried** call: a two-argument function whose intended use is `example x y : baz`. The parens are a **reader-intent marker**, not a type-theoretic change: they say *"the codomain here is a closure you hold and apply, not the last operand of a multi-arg call."* Use them whenever a constructor's product is a function to be applied later (operator constructors, partial-application factories, continuation-returning steps).

- **Bare closure type vs the operator-VALUE spelling — reconciling with `Op[τ_in → τ_out]`.** The calculus has two spellings for "returns something applied later," and they are NOT interchangeable:

  | Form | Meaning | Use when |
  |---|---|---|
  | `... -> (τ_in -> τ_out)` | the **general closure type** — a bare function value, applied directly by juxtaposition `(g x)` | the returned value is a *plain function* with no closed-over operator-parameter state worth naming, applied directly |
  | `... -> Op[τ_in → τ_out]` | the **operator-VALUE spelling** (§1.1 `Op[_]` type) — a closure-with-closed-params + body lambda, applied via the `apply` term (§3.5) | the returned value is a **named operator** carrying closed-over `!`-shareable parameters (matrix/basis/geometry tables, factorizations) — an *operator instance* in the §2 ownership sense, applied `apply A v` |

  `Op[τ_in → τ_out]` is the **specialization** of the bare closure type `(τ_in -> τ_out)` for the second ownership category of §2 (*operator internal parameters*): an `Op` value's closed-over data is `!`-tagged by construction and is read-only across a solve, and it is eliminated by `apply` (§3.5) rather than by bare juxtaposition. Prefer `Op[…]` whenever the returned closure is an operator instance with closed params (the matrix-free FE operator, a preconditioner, a constructed step); reserve the bare `(τ_in -> τ_out)` for a genuinely plain returned function (e.g. a predicate or a continuation with no operator-parameter closure). Both forms benefit from the same paren-grouping habit; for `Op[…]` the brackets already group the in/out arrow, so the codomain is unambiguous without outer parens — `mk :: A -> B -> Op[X → Y]` already reads "returns an operator."

- **Term-level form of an operator value (resolves the §Working-Notes operator-body gap).** An `Op[τ_in → τ_out]` value is, at the term level, a closure pairing its **closed-over parameters** with a **body lambda** over the run-time argument:

  ```text
  op-with-params { p₁ = e₁, …, pₖ = eₖ ; λ(x: τ_in). e_body }   : Op[τ_in → τ_out]
  ```

  i.e. a record of closed-over (`!`-shareable) params `pᵢ` together with a body abstraction `λ(x: τ_in). e_body` of type `τ_in → τ_out` that may reference both `x` and the `pᵢ`. Its eliminator is the operator-application rule of §3.5: `apply (op-with-params p, λx. e) v → e[p/params, v/x]`. (The two halves — the closed params and the body lambda — are exactly the `op-with-params p` and `λx.e` already named in the §3.5 reduction; this subsection names the *introduction* form to match the existing elimination form.)

This is a **reader-intent / introduction-form convention**, not a calculus extension — it is the higher-order sibling of §1.2.1 (which makes shape congruence visibly rank-agnostic). Functional-unit entries that return a closure cite + link here; they do not restate the rule.

## 2. Ownership categories
```

### Change 2 — `book/src/semantics/index.md`: promote the §v0.2 iteration-log note (line 494)

The v0.2 note currently calls the curried-`Op` pattern "just a convention surfaced by the v0.2 example"; this directive promotes it to a stated first-class convention. Back-reference §1.3.1.

```edit:book/src/semantics/index.md
[old]: - Operator constructors written as curried functions returning `Op[τ_in → τ_out]`: e.g., `Bgk :: !LbmTables → Scalar → Op[…]`. This isn't a calculus extension, just a convention surfaced by the v0.2 example.
[new]: - Operator constructors written as curried functions returning `Op[τ_in → τ_out]`: e.g., `Bgk :: !LbmTables → Scalar → Op[…]`. Not a calculus extension — a reader-intent **convention** for the high-order codomain. **Promoted to a stated convention in §1.3.1** (user directive 2026-06-07): closure-returning signatures group the closure codomain (`foo -> (bar -> baz)`), and the operator-VALUE spelling `Op[τ_in → τ_out]` is the §2-ownership specialization of the bare closure type for operator instances.
```

### Change 3 — `book/src/semantics/index.md`: resolve the §Working-Notes operator-body gap (line 518)

The line-518 working note flagged that an operator's body has no explicit term-level form in §1.3. §1.3.1 now gives it; close the note.

```edit:book/src/semantics/index.md
[old]: - An operator's body `Op[τ_in → τ_out]` is described informally as "closure with params + body lambda" but not given an explicit term-level form in §1.3. Tighten when needed — possibly `Op { params; \x. e }` or similar.
[new]: - ~~An operator's body `Op[τ_in → τ_out]` is described informally as "closure with params + body lambda" but not given an explicit term-level form in §1.3.~~ **RESOLVED (§1.3.1, user directive 2026-06-07):** the operator-value introduction form is `op-with-params { p₁ = e₁, … ; λ(x: τ_in). e_body } : Op[τ_in → τ_out]` — a record of closed-over `!`-params paired with the body lambda, eliminated by the §3.5 `apply` rule. §1.3.1 also states the closure-codomain paren-grouping convention (`foo -> (bar -> baz)`) and the bare-closure-vs-`Op`-value distinction.
```

### Change 4 — `book/src/L4/mk_matrix_free_operator.md`: fix the exemplar signature + add the USE+LINK back-reference

The codomain `LinearOperator (Tensor[(N: ...)])` becomes the operator-VALUE spelling `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` (the result carries closed-over params and is applied via `apply` — the chapter's own :68 lowering); the leading prose at :58 gains a USE+LINK pointer to §1.3.1; the `result` comment at :64 is updated to name the operator-value form.

```edit:book/src/L4/mk_matrix_free_operator.md
[old]: Signature (in the project's named-shape-group notation per [`semantics/index`](../semantics/index.md) §1.2 — the operator-domain shape group `(N: ...)` is the rank-structured DOF axis family, NOT a flat `Tensor[N]`; this is the genuine vocabulary shift the [`element-local-tensor`](../concepts/element-local-tensor.md) family carries away from the BLAS-1 flat vector):

    mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])
    -- FESpace      : the finite-element space (the `readonly` construction stratum `fe_assemble` captures once)
    -- WeakFormTerm : (Q, 𝒟) — coefficient Q + differential operator 𝒟; selects the basis EvalMode B_𝒟
    -- GeomFactors  : the build-stratum [E, P, G] geometry-factor carrier (the firm `geom_factor_build` product)
    -- result       : a LinearOperator whose `apply` is the contraction chain (un-materialized)
[new]: Signature (in the project's named-shape-group notation per [`semantics/index`](../semantics/index.md) §1.2 — the operator-domain shape group `(N: ...)` is the rank-structured DOF axis family, NOT a flat `Tensor[N]`; this is the genuine vocabulary shift the [`element-local-tensor`](../concepts/element-local-tensor.md) family carries away from the BLAS-1 flat vector). The codomain is written in the **operator-VALUE spelling** `Op[τ_in → τ_out]` per the closure-returning-signature convention ([`semantics/index`](../semantics/index.md) §1.3.1) — `mk_matrix_free_operator` is a *constructor* whose product is an **operator instance** carrying closed-over params (the FE space / geometry-factor / basis tables) and applied later via `apply` (the apply-lowering below), so its higher-order intent is made explicit rather than hidden behind an opaque record-applied-to-type:

    mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]
    -- FESpace      : the finite-element space (the `readonly` construction stratum `fe_assemble` captures once)
    -- WeakFormTerm : (Q, 𝒟) — coefficient Q + differential operator 𝒟; selects the basis EvalMode B_𝒟
    -- GeomFactors  : the build-stratum [E, P, G] geometry-factor carrier (the firm `geom_factor_build` product)
    -- result       : an `Op` value (operator instance) whose closed-over params are [FESpace, WeakFormTerm, GeomFactors]
    --                and whose body lambda `\v -> apply … v` is the (un-materialized) contraction chain
```

The `## Intent` prose at line 50 ends "…a `LinearOperator` value whose action is a contraction graph, not a CSR spmv." — update "a `LinearOperator` value" to name the operator-value form, keeping the cross-reference single (the rule is NOT restated; only the wording is aligned to the chosen spelling):

```edit:book/src/L4/mk_matrix_free_operator.md
[old]: This is the L4 op a GPU/burn backend instantiates: a `LinearOperator` value whose action is a contraction graph, not a CSR spmv.
[new]: This is the L4 op a GPU/burn backend instantiates: an `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` operator-value (a closure carrying closed-over params, applied via `apply` — the operator-VALUE spelling of [`semantics/index`](../semantics/index.md) §1.3.1) whose action is a contraction graph, not a CSR spmv.
```

### Change 5 — `book/src/feature/matrix-free-operator.L4.md`: lockstep exemplar fix in the composing feature column (repairer-added, cycle-128 critique finding 1)

The feature-column composition-root at `:52-59` carries the IDENTICAL pre-fix signature `matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])` (the opaque record-applied-to-type form §1.3.1 now deprecates and Change 4 fixed in the cap). Since this column COMPOSES `mk_matrix_free_operator` by name, it must use the SAME operator-VALUE spelling `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` and a USE+LINK back-reference to §1.3.1, or it drifts from both the new convention and the now-fixed cap. Apply the identical fix (the rule is NOT restated — USE+LINK only).

```edit:book/src/feature/matrix-free-operator.L4.md
[old]:     -- input  = an FE space, a weak-form term (Q, 𝒟), and the precomputed geometry factors
    -- output = a LinearOperator whose `apply` is the un-materialized contraction graph
    matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])
[new]:     -- input  = an FE space, a weak-form term (Q, 𝒟), and the precomputed geometry factors
    -- output = an `Op` value (operator instance) whose `apply` is the un-materialized contraction graph;
    --          the codomain uses the operator-VALUE spelling `Op[τ_in → τ_out]` per the closure-returning-signature
    --          convention (`book/src/semantics/index.md` §1.3.1) — a constructor product carrying closed-over params, applied via `apply`
    matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]
```

## Supporting evidence

- Semantic surface read in full: `book/src/semantics/index.md` — §1.1 Types (the `τ₁ → τ₂` and `Op[τ_in → τ_out]` type formers, :44/:46); §1.3 Terms grammar (:103-128, has `λ(x:τ).e` abstraction + `e₁ e₂` application + `apply A e`, but NO operator-introduction form); §3.5 Operator application reduction (:184-190, `apply (op-with-params p, λx.e) v → e[p/params, v/x]` — the ELIMINATION form my §1.3.1 introduction form matches); §1.2.1 named-shape-groups (:73-85, the sibling-convention template I mirror); the §v0.2 iteration-log note (:494, "isn't a calculus extension, just a convention"); the §Working-Notes operator-body gap (:518, the explicit-term-level-form TODO this resolves).
- Exemplar chapter read in full: `book/src/L4/mk_matrix_free_operator.md` — the directive's trigger line :60; the apply-lowering :68-72 (`apply (mk_matrix_free_operator space term geom) v = … (Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G) v`) confirms the result is an `apply`-eliminated operator value carrying closed params, justifying the `Op[…]` spelling over the bare `(τ_in -> τ_out)` closure type; the `## Intent` :50 "LinearOperator value" wording aligned in the same dispatch.
- `book/src/SUMMARY.md:62` — confirms the live surface path is `semantics/index.md` (the CLAUDE.md still names the pre-move `design/l4_calculus.md` path; on-disk is `semantics/index.md`, and the exemplar chapter already cites `semantics/index`, so no path drift introduced).

## Open questions / caveats

- **Exemplar-fix spelling choice (stated, for the record).** I chose `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` (operator-VALUE spelling) over the bare `(Tensor[(N: ...)] -> Tensor[(N: ...)])` closure type because the result is unambiguously an *operator instance*: it carries closed-over `!`-params (FE space / geometry factors / basis tables — the §2 "operator internal parameters" category) and is eliminated by `apply`, not bare juxtaposition (the chapter's own :68 lowering uses `apply`). Per §1.3.1's when-to-use-which rule, that is exactly the `Op[…]` case. The `Op[…]` bracket already groups the in/out arrow, so the codomain reads as a closure without needing outer `foo -> (bar -> baz)` parens — the paren-grouping habit is for the *bare* closure-type form; for `Op[…]` the brackets do the grouping.
- **Term-level introduction form is a NEW grammar production — flag for batch-41 meta (harvester/abstractor role-spec discipline).** §1.3.1 introduces `op-with-params { p₁ = e₁, … ; λx. e_body } : Op[τ_in → τ_out]` as the explicit operator-value introduction term (matching the §3.5 elimination). I deliberately authored it in §1.3.1 prose rather than editing the §1.3 BNF `e ::=` production block (to keep the change surgical and avoid renumbering the grammar). The batch-41 meta may want to (a) decide whether this introduction form should be promoted INTO the §1.3 BNF `e ::=` list as a formal production, and (b) add a one-line USE+LINK discipline bullet to the `harvester` / `abstractor` role-specs ("a closure-returning signature uses §1.3.1 paren-grouping / `Op[…]` spelling; cite §1.3.1, don't restate") so future operator-constructor chapters comply by default. Flagging per the directive's explicit ask — NOT enacting (role-spec edits are meta-phase authority).
- **Whole-book sweep candidate (for the meta, not this dispatch).** Other operator-constructor chapters likely carry the same opaque-codomain smell (any L4 op returning an `Op`/`LinearOperator`/predicate/step closure). A restatement/compliance-cohort sweep — re-check L4 constructor signatures against §1.3.1 — is a natural meta-phase plan item (the same shape as the named-shape-groups OQ `named-shape-groups-general-rule-restatement-cohort-extent`). Not enumerated here (one-file-per-dispatch discipline); flagging the cohort exists.
