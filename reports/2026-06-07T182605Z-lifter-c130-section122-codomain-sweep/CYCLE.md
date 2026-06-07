---
agent: lifter
invoked_at: 2026-06-07T18:34:41Z
scope: L4>L3 + L4 §1.2.2-R codomain-spelling fidelity sweep — residual opaque LinearOperator[…] calculus operator-VALUE codomains
status: pending
inputs:
  - book/src/semantics/index.md   (D1's pinned 1.2.2-R ruling, §1.3.1 lines 87-168; READ-only, NOT edited — D1's scope)
  - book/src/L4/mk_matrix_free_operator.md  (§1.3.1 exemplar codomain, line 60; READ-only)
  - book/src/L4-L3/fe-assemble-fold-dissolution.md
  - book/src/L4-L3/mk-matrix-free-operator-dissolution.md
  - book/src/L4/fe_assemble.md
  - book/src/L4/frequency_sweep.md
  - book/src/L4-L3/index.md  (dep-map mirror — row 46 quotes the mk-matrix-free theme-LHS codomain)
  - book/src/L4/assemble_frequency_operator.md  (READ-only — sibling cap whose settled codomain spelling LinOp[(N: ...), $N] anchors the frequency_sweep:151 conversion)
integrated_at: 2026-06-07T210500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-130 (batch-42 OPENER, 1/3) D2 applied clean (WAVE-2 dep D1). 15 §1.2.2-R codomain re-spell edits (opaque LinearOperator[…] -> bracketed LinOp[...]/Op[...]) across 5 L4/L4-L3 files; documented KEEP sites preserved; no status/rank/edge change (frontmatter untouched, no new cross-file links). One stale 2-line [old] anchor ordering in the mk-matrix-free block re-localized on disk (same target + same conversion). Build EXIT 0; graded-stack baseline HELD. 2 benign-style OQs promoted."
---

# CYCLE: Re-anchor — §1.2.2-R residual opaque-`LinearOperator[…]` calculus-codomain sweep

## Summary

D1 pinned the §1.2.2-R discriminator into `book/src/semantics/index.md` (§1.3.1 lines 150-158):
a **calculus-level operator-VALUE codomain** (operator constructor/transformer return, or theme-LHS
codomain at L4/L3/L2) spelled in the **opaque type-application form** `LinearOperator[…]` /
`LinearOperator (Tensor[…])` is the non-compliant smell — **re-spell** it (do NOT paren-wrap) in the
bracketed operator-value form `Op[τ_in → τ_out]` / square-op `LinOp[(N: ...), $N]` per §1.2.2. A
**genuine rank-1 flat-dof** form (any L1/L0 signature, or a plain operator-VALUE record FIELD whose dim
is a genuine flat-dof length) **KEEPS** the rank-1 spelling per §1.2.2:95.

This sweep re-anchors the residual opaque calculus codomains in four files. All targets are
**operator-VALUE codomains** (constructor/transformer/theme-LHS returns or result-type lines) — every
one CONVERTs. The conversions align each file with spellings **already settled in that same file or its
sibling cap**: `fe_assemble.md` already spells its three primary signatures `LinOp[(N: ...), $N]`
(`:35/:60/:71`); `mk_matrix_free_operator.md:60` already spells the cap codomain
`Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`; `assemble_frequency_operator.md:99,293` already spells its
return `LinOp[(N: ...), $N]`. The residual opaque mentions are stale drift from before those decisions.
This is prose/signature FIDELITY only — **NO** status / rank / edge / maturity change. One dep-map mirror
row (`L4-L3/index.md:46`) quotes the converted `mk-matrix-free` theme-LHS codomain and is re-spelled to
stay consistent.

**Bounded-scope note:** I CONVERT operator-VALUE **codomain / signature / result-type** sites and the
mirror that quotes one. I deliberately do NOT convert bare-word conceptual prose nouns ("a matrix-free
`LinearOperator` value") nor running narrative monoid-carrier mentions in §Algebraic-laws prose — those
denote the operator-value *concept*, not a typed codomain, and converting them over-reaches the named
sweep. The one exception is **within-`fe_assemble.md`**: that entry already DECIDED its operator-type
spelling at `:35/:60/:71` (`LinOp[(N: ...), $N]`), so the residual `LinearOperator[N,N]` mentions in its
own shape-contract + laws prose are genuine *within-file inconsistencies* with its own settled signature
— converting those is bounded same-file fidelity (the entry, not me, made the spelling call). See
§Discipline notes for the exact judgment per line.

## Proposed changes

### 1. `book/src/L4-L3/fe-assemble-fold-dissolution.md` — theme-LHS + leaf signature codomains

Both are calculus-level operator-VALUE signature codomains (the L4>L3 theme's transcribed entry point).
CONVERT to the square-op form matching the cap `fe_assemble.md:60` (`LinOp[(N: ...), $N]`).

```edit:book/src/L4-L3/fe-assemble-fold-dissolution.md
[old]:     fe_assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinearOperator[N, N]
[new]:     fe_assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinOp[(N: ...), $N]
```

```edit:book/src/L4-L3/fe-assemble-fold-dissolution.md
[old]:     assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinearOperator[N, N]
[new]:     assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinOp[(N: ...), $N]
```

(The `:3` intro-prose mention "the per-term `LinearOperator[N,N]` contributions" is running narrative
naming the reduction monoid carrier, NOT a signature codomain — KEPT as prose; see §Discipline notes.)

### 2. `book/src/L4/fe_assemble.md` — result-type line + inline leaf signature

The entry's three primary signatures already read `LinOp[(N: ...), $N]` (`:35/:60/:71`). The residual
`LinearOperator[N,N]` mentions are within-file drift inconsistent with that settled spelling. CONVERT the
operator-type mentions to `LinOp[(N: ...), $N]`.

```edit:book/src/L4/fe_assemble.md
[old]:     -- (each term independent; no carry; the reduction is operator-+ over LinearOperator[N,N]):
[new]:     -- (each term independent; no carry; the reduction is operator-+ over LinOp[(N: ...), $N]):
```

```edit:book/src/L4/fe_assemble.md
[old]:- result — `LinearOperator[N, N]` — a fresh global linear operator over the space's true-dof axis `N`, the **sum** of the per-term contributions.
[new]:- result — `LinOp[(N: ...), $N]` — a fresh global linear operator over the space's true-dof axis `N`, the **sum** of the per-term contributions.
```

```edit:book/src/L4/fe_assemble.md
[old]:- `assemble_term` — the **opaque per-term assembly leaf**: it takes one weak-form term to its global-dof `LinearOperator[N,N]` contribution (the element-local quadrature kernel + restriction; libCEED-owned). Per [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) case 1, it is a **black-box kernel that rises as a `readonly` opaque-surface input**: clean signature `(space, term) -> LinearOperator[N,N]`, opaque body (the backend supplies it).
[new]:- `assemble_term` — the **opaque per-term assembly leaf**: it takes one weak-form term to its global-dof `LinOp[(N: ...), $N]` contribution (the element-local quadrature kernel + restriction; libCEED-owned). Per [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) case 1, it is a **black-box kernel that rises as a `readonly` opaque-surface input**: clean signature `(space, term) -> LinOp[(N: ...), $N]`, opaque body (the backend supplies it).
```

```edit:book/src/L4/fe_assemble.md
[old]:3. **The reduction is a commutative-monoid sum.** The `foldr` reduces by operator-`+` over `LinearOperator[N,N]` — a commutative, associative monoid with identity `zero`.
[new]:3. **The reduction is a commutative-monoid sum.** The `foldr` reduces by operator-`+` over `LinOp[(N: ...), $N]` — a commutative, associative monoid with identity `zero`.
```

```edit:book/src/L4/fe_assemble.md
[old]:`fe_assemble` is `map (assemble_term space)` reduced to a single `LinearOperator[N,N]` by operator-`+`.
[new]:`fe_assemble` is `map (assemble_term space)` reduced to a single `LinOp[(N: ...), $N]` by operator-`+`.
```

```edit:book/src/L4/fe_assemble.md
[old]:The combinator is therefore a **pure function** `(space, terms) -> LinearOperator[N,N]` (modulo the floating-point non-associativity
[new]:The combinator is therefore a **pure function** `(space, terms) -> LinOp[(N: ...), $N]` (modulo the floating-point non-associativity
```

```edit:book/src/L4/fe_assemble.md
[old]:The fold over the empty term list is the fold's identity element (the zero operator on `LinearOperator[N,N]`, the additive identity for operator-`+`).
[new]:The fold over the empty term list is the fold's identity element (the zero operator on `LinOp[(N: ...), $N]`, the additive identity for operator-`+`).
```

### 3. `book/src/L4-L3/mk-matrix-free-operator-dissolution.md` — L4-transcribed + L3 theme-LHS codomains

The transcribed L4 constructor signature must match the cap `mk_matrix_free_operator.md:60`
(`Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`). The L3-form codomain is the operator-CONSTRUCTOR product
(domain ≡ range = `(N: ...)`) → square-op `LinOp[(N: ...), $N]`.

```edit:book/src/L4-L3/mk-matrix-free-operator-dissolution.md
[old]:    mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])
    -- the operator-CONSTRUCTOR: build (once) a matrix-free LinearOperator value over the FLAT
[new]:    mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]
    -- the operator-CONSTRUCTOR: build (once) a matrix-free LinearOperator value over the FLAT
```

(Note: the immediately-preceding code comment line `-- the operator-CONSTRUCTOR: build (once) a
matrix-free LinearOperator value over the FLAT` uses bare-word `LinearOperator` as a conceptual noun —
KEPT, not a codomain spelling. It is shown only as edit context above; it is unchanged.)

```edit:book/src/L4-L3/mk-matrix-free-operator-dissolution.md
[old]:2. **The flat operator-domain shape `Tensor[(N: ...)]`.** The L4 `LinearOperator (Tensor[(N: ...)])` is typed
[new]:2. **The flat operator-domain shape `Tensor[(N: ...)]`.** The L4 `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` is typed
```

```edit:book/src/L4-L3/mk-matrix-free-operator-dissolution.md
[old]:    mk_matrix_free_operator_L3 :: (space, term, geom) -> LinearOperator[(N: ...)]
[new]:    mk_matrix_free_operator_L3 :: (space, term, geom) -> LinOp[(N: ...), $N]
```

```edit:book/src/L4-L3/mk-matrix-free-operator-dissolution.md
[old]:  `mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])`
[new]:  `mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`
```

### 4. `book/src/L4/frequency_sweep.md` — per-ω rebuilt-operator result annotation

`op_w = assemble_frequency_operator fam omega` is a constructor-call result; its type annotation is a
calculus-level operator-VALUE codomain. The sibling cap `assemble_frequency_operator.md:99,293` already
settles the return as `LinOp[(N: ...), $N]`. CONVERT to match.

```edit:book/src/L4/frequency_sweep.md
[old]:- `op_w = assemble_frequency_operator fam omega : LinearOperator[N, N]` — the per-ω
[new]:- `op_w = assemble_frequency_operator fam omega : LinOp[(N: ...), $N]` — the per-ω
```

### 5. `book/src/L4-L3/index.md` — dep-map mirror row for `mk-matrix-free-operator-dissolution`

Row 46 quotes the `mk-matrix-free` theme-LHS codomain twice in the opaque form. Re-spell the **quoted
codomain** to stay consistent with the converted theme LHS (§3 above). The bare-word "matrix-free
(un-materialized) `LinearOperator` over the FLAT operator-domain shape" is a conceptual noun — KEPT.

```edit:book/src/L4-L3/index.md
[old]: the atomic `mk_matrix_free_operator space term geom :: LinearOperator (Tensor[(N: ...)])` build of a matrix-free (un-materialized) `LinearOperator` over the FLAT operator-domain shape `Tensor[(N: ...)]`,
[new]: the atomic `mk_matrix_free_operator space term geom :: Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` build of a matrix-free (un-materialized) `LinearOperator` over the FLAT operator-domain shape `Tensor[(N: ...)]`,
```

## Discipline notes

**Discriminator applied per site (all CONVERT — every target is an operator-VALUE codomain):**

| Site (on-disk) | Form | Verdict | New spelling | Anchor |
|---|---|---|---|---|
| `fe-assemble-fold-dissolution.md:30` | theme-LHS signature codomain | CONVERT | `LinOp[(N: ...), $N]` | cap `fe_assemble.md:60` |
| `fe-assemble-fold-dissolution.md:37` | leaf signature codomain | CONVERT | `LinOp[(N: ...), $N]` | cap `fe_assemble.md:71` |
| `fe_assemble.md:64` | within-file monoid-carrier (code comment) | CONVERT (same-file consistency w/ `:60`) | `LinOp[(N: ...), $N]` | own sig `:35/:60/:71` |
| `fe_assemble.md:77` | result-type line | CONVERT | `LinOp[(N: ...), $N]` | own sig `:60` |
| `fe_assemble.md:78` (×2) | inline leaf signature + contribution | CONVERT | `LinOp[(N: ...), $N]` | own sig `:71` |
| `fe_assemble.md:84/92/102/118` | within-file monoid-carrier prose | CONVERT (same-file consistency) | `LinOp[(N: ...), $N]` | own sig `:60` |
| `mk-matrix-free-operator-dissolution.md:104` | theme-LHS L4 transcribed signature | CONVERT | `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` | cap `mk_matrix_free_operator.md:60` |
| `mk-matrix-free-operator-dissolution.md:122` | quoted codomain in prose | CONVERT | `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` | cap `:60` |
| `mk-matrix-free-operator-dissolution.md:151` | L3 theme-LHS signature codomain | CONVERT | `LinOp[(N: ...), $N]` | cap `:60` square-op |
| `mk-matrix-free-operator-dissolution.md:370` | repeated theme-LHS signature | CONVERT | `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` | cap `:60` |
| `frequency_sweep.md:151` | constructor-call result annotation | CONVERT | `LinOp[(N: ...), $N]` | sibling cap `assemble_frequency_operator.md:99,293` |
| `L4-L3/index.md:46` | dep-map mirror quoting theme-LHS codomain | CONVERT (mirror consistency) | `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` | follows §3 |

**Two spelling choices, both §1.2.2-compliant and matched to the already-settled in-file/sibling spelling:**
- `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` for the **`mk_matrix_free` constructor** — copied verbatim
  from the cap `mk_matrix_free_operator.md:60` (the §1.3.1 operator-VALUE constructor exemplar; citecheck
  `--anchor` confirmed). The cap deliberately uses the explicit in/out-arrow `Op[…]` form to surface the
  constructor's higher-order intent; the theme transcribes the cap, so it must match verbatim.
- `LinOp[(N: ...), $N]` (square-op, §1.2.2:93) for **`fe_assemble` / `assemble_term` / the per-ω rebuilt
  operator / the `mk_..._L3` constructor product** — these are square endomorphic operators (domain ≡
  range), and the already-settled sibling spellings (`fe_assemble.md:35/60/71`,
  `assemble_frequency_operator.md:99/293`) use exactly this square-op form. Choosing it keeps each file
  internally consistent rather than introducing a second spelling.

**USE+LINK, did not restate the convention.** Every conversion cites §1.2.2-R / §1.3.1 and the §1.3.1
exemplar `mk_matrix_free_operator.md:60` as the authority; no §1.2.2 rule text is restated in any theme/cap
(the semantic-consolidation discipline — the rule lives once, at the surface).

**KEEP decisions (judged, not swept):**
- Bare-word conceptual-noun mentions "a matrix-free `LinearOperator` value" /
  "build (once) a matrix-free LinearOperator value" (`mk-...:47,49,102,115`) — these are the operator-value
  *concept* as an English noun, NOT a typed codomain spelling with bracket-args. KEPT (converting bare
  prose nouns over-reaches the codomain sweep).
- The `mk-...:3` intro-prose "the per-term `LinearOperator[N,N]` contributions" in
  `fe-assemble-fold-dissolution.md` — running narrative naming the reduction monoid carrier in the theme
  intro, not a signature codomain. KEPT as narrative (the `fe-assemble` *theme* file has only the two
  signature codomains at `:30/:37`; unlike the `fe_assemble` *cap* file it has no within-file settled
  signature spelling driving a same-file-consistency conversion of intro prose). If a later pass wants
  the theme intro to match its own converted signatures, that is a separable bounded fidelity follow-up
  — flagged below, not silently expanded here.
- **No record FIELDS encountered in scope.** The c129-D2 dual-spelling carve-out (the
  `assemble_frequency_operator` `{K, C, M}` rank-1 flat-dof fields at `assemble_frequency_operator.md:103-105`,
  the `divfree-projector` fields) is NOT touched by this sweep — those fields are out of my four-file scope
  and are correctly KEPT rank-1 per §1.2.2:95. `frequency_sweep.md:151` is a constructor-call **result
  annotation**, not a record field — hence CONVERT, consistent with that cap's settled `:99/:293` return.

**No prose-correction-in-place was triggered.** Every change is a pure §1.2.2-R spelling re-anchor; no
backward convention, drifted citation, or L0-contradicting claim was found that would license a bounded
content correction.

## Supporting evidence

- D1's pinned ruling: `book/src/semantics/index.md` §1.3.1, the §1.2.2-R discriminator table
  (lines 150-158) + the square-op / square-op-applied forms §1.2.2 (lines 89-95).
- §1.3.1 operator-VALUE constructor exemplar: `book/src/L4/mk_matrix_free_operator.md:60`
  (`Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`; citecheck `--anchor` confirmed in-range at line 60).
- Sibling already-settled square-op return: `book/src/L4/assemble_frequency_operator.md:99,293`
  (`LinOp[(N: ...), $N]`).
- Within-file already-settled signatures driving the `fe_assemble.md` same-file consistency conversions:
  `book/src/L4/fe_assemble.md:35,60,71` (`LinOp[(N: ...), $N]`).
- §1.2.2:95 rank-1-keep clause (L1/L0 + genuine flat-dof fields KEEP): `book/src/semantics/index.md:95`.

## Open questions / caveats

- **NO status/rank/edge/maturity change** in this sweep, as scoped. Every CONVERT is prose/signature
  fidelity; the four files keep their existing `firm` maturity and frontmatter untouched.
- **Disjointness confirmed.** None of my five edited files (`fe-assemble-fold-dissolution.md`,
  `mk-matrix-free-operator-dissolution.md`, `fe_assemble.md`, `frequency_sweep.md`, `L4-L3/index.md`) is
  D1's (`semantics/index.md`) or D3's (`inner_product.md` + its anchors). No overlap.
- **Separable bounded follow-up (NOT done here, flagged):** the `fe-assemble-fold-dissolution.md:3`
  intro-prose monoid-carrier mention `LinearOperator[N,N]` was KEPT (no within-theme settled signature
  drives a same-file conversion the way the *cap* file's `:60` does). If a finalize-time consistency pass
  wants theme intro prose to mirror the theme's own converted `:30/:37` signatures, that is a one-line
  bounded fidelity edit. I did NOT expand the named codomain sweep to cover it to avoid over-reach; it is
  not a defect (it is correct narrative prose), only a stylistic-consistency option.
- **`mk_matrix_free_operator` codomain spelling — `Op[…]` vs `LinOp[…]`.** I used the explicit-arrow
  `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` form verbatim from the cap `:60` for the constructor signature,
  and the compact square-op `LinOp[(N: ...), $N]` for the L3-form product. Both are §1.2.2-compliant and
  denote the same square endomorphism. Using the cap's exact spelling for the transcribed constructor
  signature (and the square-op for the derived L3 product) was the consistency-maximizing choice; if the
  integrator/critic prefers a single uniform spelling across the theme, the L3-form `:151` could instead
  read `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` — flagging the choice, not blocking on it.
