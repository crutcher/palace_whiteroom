---
agent: lifter
invoked_at: 2026-06-02T223435Z
scope: L3 dot / nrm2 — re-anchor stale "no L4 entry" lines to firm L4/dot, L4/nrm2 (cycle-069 D2 rise)
status: integrated
integrated_at: 2026-06-02T233500Z
integration_commit: 502171088810f0f4bbf849acba3bf2fc9ff51f09
integration_notes: |
  Applied by integrator-per-report (staging row D4, applied_at 2026-06-02T231530Z); finalized by integrator-finalize cycle-070.
  L3/dot + L3/nrm2 LEAF stale-no-L4 → live-link re-anchor: lifts_from frontmatter + §"Lifts from" prose flipped from "no L4 entry exists" → firm live links ../L4/dot.md / ../L4/nrm2.md (identity-in-form / consumer-not-fold-member framing), each with a > Superseded blockquote preserving the cycle-010 "no-L4-by-design" rationale; L3/index.md:66 BLAS-1-cohort clause corrected in-line to the per-case black-box-vs-accelerated-kernels §2 disposition. Both L3 entries stay firm (no status flip, no index-cell touch). ENACTS+CLOSES OQ l3-dot-nrm2-stale-no-l4-entry-lines-need-reanchor (closed-ENACTED-c070-D4). Build-relevant: cargo make book exit 0; all link targets resolve. 0 OQs promoted; 1 OQ closed-in-artifact. Zero gate hits; retroactive-budget 0.
inputs:
  - book/src/L3/dot.md
  - book/src/L3/nrm2.md
  - book/src/L3/index.md
  - book/src/L4/dot.md
  - book/src/L4/nrm2.md
  - book/src/L4/index.md
---

# CYCLE: Re-anchor L3 dot / nrm2 — stale "no-L4-entry" → firm L4 live links

## Summary
`dot` and `nrm2` rose to **firm L4 entries** in cycle-069 D2 (`book/src/L4/dot.md:201`,
`book/src/L4/nrm2.md:191`, both `## Status: firm`), riding the cycle-068 D3 rise of the
`inner_product` combinator they re-express through (`dot` = Hermitian/symmetric specialization
at `M = I`; `nrm2` = `√ ∘ abs ∘ inner_product` diagonal CONSUMER, NOT a fold member). The two
L3 entries (`L3/dot.md`, `L3/nrm2.md`) and the L3 index still carry the now-stale pre-rise
assertion that these reductions have **no L4 entry** ("leaf primitives are not first-class L4
vocabulary per the cycle-010 audit verdict" / "so neither lifts above L3"). This is the
identical thin re-anchor routine cycle-069 D3 ran for the `linear_combination`/`inner_product`
combinators: flip each stale `lifts_from: (none) … no L4 entry exists` frontmatter line and each
`## Lifts from` prose paragraph to a **live link** at `L4/dot` / `L4/nrm2`, and demote the
superseded cycle-010 "no-L4-by-design" rationale to a `> Superseded` admission blockquote
(do not delete it). Chapter structure is untouched — pure vocabulary firm. Closes OQ
`l3-dot-nrm2-stale-no-l4-entry-lines-need-reanchor`.

The L3 index's matching cohort-level stale claim is line 66's clause "the L2 combinators carried
no L4 calculus content (pure value-producing reductions, not state-monad combinators), **so
neither lifts above L3**" — the BLAS-1-cohort "no-L4-by-design" assertion. This is corrected the
same way `L4/index.md:73-74` already corrects the blanket "13-of-18 remain no-L4" inference: to
the **per-case** disposition of `concepts/black-box-vs-accelerated-kernels.md` §2 — the
combinators rise regardless (firm L4, c068 D3) and the kept named abstractions `dot`/`nrm2` rise
alongside as named verbs (firm L4, c069 D2).

## Proposed changes

### 1. `book/src/L3/dot.md` — frontmatter `lifts_from` + §"Lifts from" prose

```edit:book/src/L3/dot.md
[old]: lifts_from:
  - (none) — `dot` is a reduction specialization; no L4 entry exists (folds/leaves are not first-class L4 vocabulary per cycle-010 audit verdict; the combinator appears inside L4 composed entries like krylov-step §Semantics as a let-binding)
[new]: lifts_from:
  - book/src/L4/dot.md (firm cycle-069 D2 — the L4 Hermitian/symmetric inner-product verb `dot(p, Ap)`; the kept named abstraction risen to L4 alongside the `inner_product` combinator, `concepts/black-box-vs-accelerated-kernels.md` §2; identity-in-form on the body — value-thread-isomorphic, no dedicated L4>L3 theme, the in-line-marker route)
```

```edit:book/src/L3/dot.md
[old]: ## Lifts from

`dot` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010
audit verdict). At L4, `dot` appears inside larger composed entries (e.g.,
`book/src/L4/krylov-step.md` §Semantics) as a let-binding consuming the L3-native primitive
surface.
[new]: ## Lifts from

L3 `dot` lifts to the firm L4 [`dot`](../L4/dot.md) (firm cycle-069 D2) by **identity-in-form on
the body** — the L4 form is the calculus-level named verb re-expressing the [`inner_product`](../L4/inner_product.md)
combinator at `M = I` with the Hermitian/symmetric kernel; it is value-thread-isomorphic to this
L3 specialization-stub (the same `Tensor[N] -> Tensor[N] -> Scalar` reduction at the plain-weight
conjugation value), so there is **no dedicated L4>L3 theme** (the in-line-marker route, the
`inner_product`/`eigsolve`/`chebyshev` shape — no monadic wrapper / `Solve` monad / convergence
predicate to dissolve). `dot` is one of the **kept named abstractions** that rise to L4 as named
verbs *alongside* the general combinator (the permitted dual per
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2 — the
literature-standard unit a CG/GMRES description spells `dot(p, Ap)` / `dot(r, z)` rather than an
inlined application). At L4 `dot` also still appears *inside* larger composed entries (e.g.
`book/src/L4/krylov-step.md` §Semantics) as a let-binding consuming the primitive surface.

> **Superseded.** This entry formerly recorded `dot` as having **no L4 entry** — "leaf
> primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict); at L4 `dot`
> appears only inside larger composed entries as a let-binding." That blanket "no-L4-by-design"
> reading was **superseded cycle-069 D2** when `dot` rose to a firm L4 named verb. Under the
> 2026-06-01 VOCABULARY-SHIFT REDIRECT (L4 is the outward backend-lowering target) the per-case
> disposition of [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
> §2 governs: the `inner_product` combinator rises regardless, and the **kept named abstractions
> `dot` / `nrm2` rise alongside it as named verbs** (distinct from the *pure accelerated kernels*
> `scal` / `axpy` / `axpby` / `axpbypcz`, which correctly stay low). The cycle-010 verdict was
> right for accelerated-kernel leaves; `dot` is a kept named abstraction, not such a leaf.
```

### 2. `book/src/L3/nrm2.md` — frontmatter `lifts_from` + §"Lifts from" prose

```edit:book/src/L3/nrm2.md
[old]: lifts_from:
  - (none) — `nrm2` is a leaf primitive; no L4 entry exists (leaf primitives don't get L4 rows per cycle-010 audit verdict)
[new]: lifts_from:
  - book/src/L4/nrm2.md (firm cycle-069 D2 — the L4 Euclidean-norm verb `nrm2(r)`; the kept named abstraction risen to L4 as a named CONSUMER verb of the `inner_product` combinator at the diagonal `y = x` (`√ ∘ abs ∘ inner_product`), NOT a fold member — the do-NOT-merge guard; `concepts/black-box-vs-accelerated-kernels.md` §2; identity-in-form on the body — value-thread-isomorphic, no dedicated L4>L3 theme, the in-line-marker route)
```

```edit:book/src/L3/nrm2.md
[old]: ## Lifts from

`nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010
audit verdict). At L4, `nrm2` appears inside larger composed entries (e.g.
`book/src/L4/krylov-step.md` §Semantics body — `outputs.residual_norm`) as a let-binding consuming
the L3-native primitive surface.
[new]: ## Lifts from

L3 `nrm2` lifts to the firm L4 [`nrm2`](../L4/nrm2.md) (firm cycle-069 D2) by **identity-in-form
on the body** — the L4 form is the calculus-level named verb re-expressing the diagonal consume of
the [`inner_product`](../L4/inner_product.md) combinator under the `√ ∘ abs` scalar map; it is
value-thread-isomorphic to this L3 consumer-stub (the same `Tensor[N] -> Scalar` `√(abs(inner_product
x x))` skeleton), so there is **no dedicated L4>L3 theme** (the in-line-marker route — no monadic
wrapper / `Solve` monad / convergence predicate to dissolve; the `abs` defensive guard is preserved
as an explicit scalar-map detail at L4). `nrm2` is one of the **kept named abstractions** that rise
to L4 as named verbs *alongside* the general combinator (the permitted dual per
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2 — the
literature-standard unit a Krylov / eigen solver description spells residual `nrm2(r)` / the Arnoldi
sub-diagonal `H[j+1,j] = nrm2(w)`), but as a **CONSUMER** of `inner_product`, NOT a fold member (the
do-NOT-merge over-unification guard — split-additivity is lost under `√`). At L4 `nrm2` also still
appears *inside* larger composed entries (e.g. `book/src/L4/krylov-step.md` §Semantics body —
`outputs.residual_norm`) as a let-binding consuming the primitive surface.

> **Superseded.** This entry formerly recorded `nrm2` as having **no L4 entry** — "leaf primitives
> are not first-class L4 vocabulary (per the cycle-010 audit verdict); at L4 `nrm2` appears only
> inside larger composed entries as a let-binding." That blanket "no-L4-by-design" reading was
> **superseded cycle-069 D2** when `nrm2` rose to a firm L4 named verb. Under the 2026-06-01
> VOCABULARY-SHIFT REDIRECT (L4 is the outward backend-lowering target) the per-case disposition of
> [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2 governs:
> the `inner_product` combinator rises regardless, and the **kept named abstractions `dot` / `nrm2`
> rise alongside it as named verbs** (`nrm2` as a CONSUMER of the combinator, not a member; distinct
> from the *pure accelerated kernels* `scal` / `axpy` / `axpby` / `axpbypcz`, which correctly stay
> low). The cycle-010 verdict was right for accelerated-kernel leaves; `nrm2` is a kept named
> abstraction, not such a leaf.
```

### 3. `book/src/L3/index.md` — cohort-level stale "neither lifts above L3" clause (line 66)

This is the BLAS-1-cohort "no-L4-by-design" assertion, the L3-side analog of the per-case
correction `L4/index.md:73-74` already carries. Only the stale trailing clause is touched — the
combinator-landing narrative is otherwise preserved verbatim.

```edit:book/src/L3/index.md
[old]: Both were inverted to combinator-as-entry at L2 cycle-049 (commit `92327f7`) but never propagated to L3; the L2 combinators carried no L4 calculus content (pure value-producing reductions, not state-monad combinators), so neither lifts above L3. Both join the **obstruction-free end** of the §Semantics-overlay obstruction-profile spectrum alongside the leaves they unify
[new]: Both were inverted to combinator-as-entry at L2 cycle-049 (commit `92327f7`) but never propagated to L3. (The earlier reading that "the L2 combinators carried no L4 calculus content … so neither lifts above L3" was **superseded cycle-068 D3 / cycle-069 D2**: under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, L4 is the outward backend-lowering target, so per the **per-case** disposition of [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2 the general combinators [`inner_product`](./inner_product.md) + [`linear_combination`](./linear_combination.md) **rise to L4 regardless** as feature-surface verbs (firm L4 cycle-068 D3), and the kept named abstractions `dot` / `nrm2` rise to L4 alongside as named verbs (firm L4 cycle-069 D2 — `dot` the Hermitian/symmetric specialization, `nrm2` the `√ ∘ abs ∘ inner_product` diagonal CONSUMER, do-NOT-merge); only the *pure accelerated kernels* `scal` / `axpy` / `axpby` / `axpbypcz` correctly stay low with no L4 chapter. This corrects the L3-side cohort "no-L4-by-design" assertion the same way `L4/index.md` §"Cycle-068" already corrects the blanket "13-of-18 remain no-L4" inference.) Both join the **obstruction-free end** of the §Semantics-overlay obstruction-profile spectrum alongside the leaves they unify
```

## Discipline notes
- **Pure re-anchor / vocabulary-firm pass.** No chapter restructure, no signature change, no
  decomposition change. The L4 `dot`/`nrm2` signatures (`Tensor[N] -> Tensor[N] -> Scalar`,
  `Tensor[N] -> Scalar`) are identical to the L3 forms (the rise is identity-in-form on the body,
  per `L4/dot.md:11` / `L4/nrm2.md:11` `lowers_to`), so the L3 LHS/RHS shapes are untouched — only
  the stale "no L4 entry exists" claims firm to live links. This is the high→low discipline held:
  the L3 entries' upward `lifts_from` pointer is working-note-style upward context (kept minimal),
  the formal body stays L3-vocabulary.
- **Superseded reasoning demoted, not deleted** (per the cycle-069 D3 precedent the scope names):
  each entry's old cycle-010 "no-L4-by-design" rationale is preserved as a `> Superseded`
  admission blockquote noting it was right for accelerated-kernel leaves but wrong for these kept
  named abstractions. The cohort-level L3-index clause is demoted in-line (parenthetical
  supersession note) rather than a blockquote, matching the running-narrative register of that
  Working-Notes bullet.
- **No prose-correction beyond the re-anchor.** The cycle-010 verdict was not *wrong* when made —
  it was superseded by the 2026-06-01 redirect making L4 the backend-lowering target. So this is a
  vocabulary firm (stale→live link), not an L0-evidence prose-correction; nothing here required the
  bounded-correction carve-out.
- **Index-cell status discipline (c057 guard):** these edits do NOT flip any `## Status` line —
  the L3 `dot`/`nrm2` entries were already `firm` (specialization-stub / consumer-stub) before this
  pass and stay `firm`; the L4 `dot`/`nrm2` entries were flipped firm by cycle-069 D2, not here. So
  there is no theme-`## Status` ↔ index-cell desync for this dispatch to own. The L3 index dep-map
  rows for `dot`/`nrm2` (`:27`/`:28`) carry no L4-disposition cell and make no stale L4 claim, so
  they are untouched; the only L3-index stale L4 claim is the line-66 cohort clause corrected above.

## Supporting evidence
- `book/src/L4/dot.md:201` — `## Status` line: `firm` — the L4 Hermitian/symmetric inner-product
  verb, value-thread-isomorphic to firm L3 `dot`. (citecheck `--anchor 'firm'` → `[ok]`,
  anchor at line 201 within 199-201.)
- `book/src/L4/nrm2.md:191` — `## Status` line: `firm` — the L4 Euclidean-norm verb, diagonal
  consumer of `inner_product`, value-thread-isomorphic to firm L3 `nrm2`. (citecheck
  `--anchor 'firm'` → `[ok]`, anchor at line 191 within 189-191.)
- `book/src/L4/dot.md:11`, `book/src/L4/nrm2.md:11` — `lowers_to` frontmatter: both record
  identity-in-form-on-the-body L4>L3 with NO dedicated theme (the in-line-marker route) — the
  symmetric statement of the upward lift this re-anchor records on the L3 side.
- `book/src/L4/index.md:40` (dot dep-map row), `:43` (nrm2 dep-map row), `:72-74` (the cycle-068
  per-case correction the L3-index clause edit mirrors) — confirm the firm L4 cohort + the
  per-case "rises alongside" disposition wording.
- `book/src/concepts/black-box-vs-accelerated-kernels.md` §2 — the kept-named-abstraction
  rises-alongside disposition cited throughout (referenced by the firm L4 entries' frontmatter
  `consumes` lists, `L4/dot.md:7`, `L4/nrm2.md:7`).

## Open questions / caveats
- None blocking. The firm L4 signatures match the L3 forms exactly (identity-in-form), so this is
  a clean pure-rewrite — no abstractor reread is warranted.
- Minor downstream-hygiene observation (NOT in scope for this dispatch, flagged for the planner):
  the L3-index §Semantics-overlay bullet at line 66 still describes both combinators' L4 disposition
  in the past tense around the *leaves*; the parenthetical correction added here is the targeted fix
  for the load-bearing stale clause, but a future layer-intro-author refresh of that Working-Notes
  bullet could fold the correction into the running narrative more smoothly (low priority — the live
  links are now correct, only the prose register is slightly bolted-on).
