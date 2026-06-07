---
agent: combinator-miner
invoked_at: 2026-06-07T153840Z
scope: Pattern proposal — inner-product-family-re-style-elimination (RE6-style reduce-family combinator-arity-notes refactor)
status: integrated
integrated_at: 2026-06-07T180000Z
integration_commit: acf65f6
integration_notes: "Applied clean (D4). inner-product-family RE-style elimination: DELETED L2/dot+L2/nrm2+L3/dot+L3/nrm2, folded into firm inner_product (dot->Specializations, nrm2->Consumer; do-NOT-merge boundary held). ~20 book edits re-pointing all inbound (frontmatter depends-on + body links + SUMMARY + index dep-map rows). The new deleted-slug FRONTMATTER-EDGE gate caught + re-pointed a legacy consumes: dangler L2/normalize->L2/nrm2 the report inventory MISSED -> unresolved_depends_on_targets stayed 0 at finalize (no c124-style build-repair). cargo make book EXIT 0; rank_violations 0; L2/L3 firm count -2. 1 OQ promoted (inner-product-combinator-section-anchor-stability)."
---

# CYCLE: Combinator candidate — inner-product-family-re-style-elimination

## Summary

This is the reduce-family analog of the cycle-124 RE6 `linear_combination` arity-leaf
elimination, migrated from OQ `inner-product-family-re-style-elimination-candidate`. The
`inner_product` combinator is ALREADY the firm L2 + L3 family entry (firm cycle-019 / cycle-050),
carrying the full reduce-to-scalar fold semantics, laws, the `dot`/`tdot`/`bilinear_form`
§"Specializations" notes, AND the `nrm2`/`matrix-weighted-norm` §"Consumer (NOT an instance)"
note. Standing **beside** the combinators are four already-reduced thin stubs —
`L2/dot.md`, `L2/nrm2.md`, `L3/dot.md`, `L3/nrm2.md` — each a specialization-stub (`dot`) or
consumer-stub (`nrm2`) that defers all substance to the combinator and retains only a few
leaf-level facts. These residual standalone leaf-floors are the **retired rectangular pattern**
(same-named base-form floors mirrored at each layer, kept only for the now-SUPERSEDED
"Identity-lowerings still require both L levels" invariant — itself retired by the
2026-06-01 vocabulary-shift redirect). I propose to **fold the four stubs' unique leaf-level
facts into the combinators' already-present §Specializations / §Consumer sections, delete the
four standalone chapters, and re-point all inbound references across the three de-link surfaces**
to the surviving combinator — exactly the RE6 shape, replace-and-propagate not mine-and-strand.

**The do-NOT-merge boundary HELD and I proceeded.** `dot` is a codomain/fold specialization →
it folds into §"Specializations" (where it already lives as a note). `nrm2` is a
`√∘abs∘inner_product` CONSUMER (NOT a member) → it folds into §"Consumer (NOT an instance)"
(where it already lives as a note). The two sections are kept distinct; `nrm2` is NEVER moved
into §Specializations nor restated as a fold member. No genuinely-distinct abstraction is
stranded: the firm L4 `dot`/`nrm2` named verbs (the kept-named-abstraction dual per
`black-box-vs-accelerated-kernels` §2) are OUT of D4 scope and SURVIVE — their `depends-on`
edges re-point to the surviving `inner_product` combinator. This is not a new operator (no
new dep-map row); it is a destructive consolidation refactor that reduces four DAG nodes.

## Pattern instances

The "residual standalone leaf-floor beside a firm combinator that already absorbed its
substance" pattern, ≥3 instances (the eliminated cohort):

- **Instance 1**: `book/src/L2/dot.md` (firm, specialization-stub, reduced cycle-052 D3) —
  `dot` at L2 is the `M = I` Hermitian/symmetric specialization of `L2/inner_product`; the
  whole chapter is a pointer up to the combinator's §"Specializations". Unique leaf facts it
  carries: the conjugation variant-axis table (`dot`/`tdot` per element-type) and `dot`'s
  unique L0 anchors (`vector.cpp:263-274` `Dot`/`TransposeDot` kernels + the `&y==this`
  self-dot fast path). **Both already present in `L2/inner_product` §Signature kernel table +
  §"tdot" + §Evidence.**
- **Instance 2**: `book/src/L2/nrm2.md` (firm, consumer-stub, reduced cycle-052 D3) — `nrm2`
  at L2 is the `√∘abs∘inner_product` CONSUMER at `y=x`. Unique leaf fact: the load-bearing
  `std::abs` defensive-guard claim + the `Norml2` L0 anchor (`vector.hpp:255-260`). **Already
  present in `L2/inner_product` §"Consumer (NOT an instance)".**
- **Instance 3**: `book/src/L3/dot.md` (firm, specialization-stub, reduced cycle-052 D3) —
  the iteration-rotation rendering; defers to `L3/inner_product` §"Specializations". Unique
  facts: conjugation variant-axis + the krylov-step consuming context. **Already present in
  `L3/inner_product` §"Specializations" + §"Semantics" consuming-context.**
- **Instance 4**: `book/src/L3/nrm2.md` (firm, consumer-stub, reduced cycle-052 D3) — the
  `√dot(x,x)` consumer; defers to the firm L1 leaf + `L3/inner_product` §"Consumer". Unique
  facts: `std::abs` guard + the Arnoldi-sub-diagonal / residual-norm consuming context.
  **Already present in `L3/inner_product` §"Consumer" + §"Semantics".**

**Precedent (the decisive same-shape sibling, already eliminated):** the four
`linear_combination` arity leaves (`scal`/`axpy`/`axpby`/`axpbypcz`) were eliminated
cycle-124 (RE6), their unique L0 anchors folded into
`L2/linear_combination` / `L3/linear_combination` §"Arity specializations", their inbound
edges re-pointed to `linear_combination#arity-specializations`. The
`fold-family-stubs-intro.md:20-23` and `blas1-intro.md:20` already document that elimination;
this D4 is its reduce-family completion. The ONLY structural difference is the surviving firm
L4 `dot`/`nrm2` verbs (the `linear_combination` arity leaves had no L4 verbs — `scal`/`axpy`
correctly stopped low), which this refactor preserves and re-edges.

## Proposed combinator

This is a **destructive consolidation refactor of an EXISTING firm combinator**, not a new
combinator proposal. No new dep-map row. The surviving entry is the already-firm
`inner_product` at L2 and L3.

- **Slug**: `inner_product` (existing; L2 `book/src/L2/inner_product.md`, L3
  `book/src/L3/inner_product.md`)
- **Layer**: L2 (fusion-rotation fold) + L3 (iteration-rotation rendering) — both already firm.
- **Action**: fold `dot` (→ §Specializations) + `nrm2` (→ §Consumer, NOT a member) leaf-level
  facts into the combinator; `delete:` the four standalone stubs; re-point all inbound refs.
- **Parameter axis** (the family the combinator unifies, unchanged): conjugation-convention
  (Hermitian `dot` / unconjugated `tdot`) × element-type × weight-presence (`bilinear_form`).
- **Over-unification guard (the HARD constraint — HELD)**: `nrm2` is NOT a fold member. It is
  the `√∘abs∘inner_product` consumer at the diagonal `y=x`; split-additivity (the defining
  fold law) is LOST under `√`, which is exactly why it is a consumer. It folds into
  §"Consumer (NOT an instance)", a section kept distinct from §"Specializations". `dot` is the
  codomain-`Scalar` Hermitian specialization (M = I); it folds into §"Specializations". The
  sibling fold `linear_combination` (reduce-to-`Tensor[N]`) stays explicitly NOT merged.

## Decision: PROCEED (boundary held, no abstraction stranded)

The do-NOT-merge boundary HELD on inspection: the combinator content already partitions `dot`
(§Specializations) from `nrm2` (§Consumer), and the fold preserves that partition. No
genuinely-distinct abstraction is stranded — the four stubs' substance already lives in the
combinators; the unique leaf facts (conjugation table, `&y==this` self-dot fast path, the
`std::abs` defensive guard, the consuming contexts) fold cleanly into the matching sections.
The firm L4 `dot`/`nrm2` named verbs are out of scope and survive with re-pointed edges. I
therefore PROCEED with the elimination rather than recording a finding-instead.

## Inbound-link inventory (all THREE de-link surfaces) and re-points

Deleted slugs: `L2/dot`, `L2/nrm2`, `L3/dot`, `L3/nrm2`. Sweep run per skill
`deleted-slug-inbound-live-link-sweep` (body-link grep step 1 + frontmatter-edge grep step 7),
self-exclusion by SOURCE-PATH prefix (drop the deleted files' own internal lines).

### Surface (i) — markdown body links `](.../<slug>.md)`

Re-point convention (RE6 anchor-link precedent): a `dot` link → the combinator's
§Specializations anchor; a `nrm2` link → the combinator's §Consumer anchor; an index/intro
row → the combinator row. Anchors (mdBook-generated):
- `inner_product.md#specializations-the-members-as-notes-under-the-combinator`
- `inner_product.md#consumer-not-an-instance-nrm2--matrix-weighted-norm`

**Inbound to `L2/dot`** (excluding `L2/dot.md`'s own + `L2/nrm2.md`'s lines — those files
are deleted): `L3-L2/orthogonalize-variant-split.md:259`; `L2/divfree-projector.md:75,329`;
`L2/assemble-diagonal.md:451`; `L2/reciprocal.md:20,64,67,249,388,409`; `L2/index.md:117`
(dep-map row — STRIKE the row); `L2/fold-family-stubs-intro.md:28` (intro bullet — STRIKE).

**Inbound to `L2/nrm2`**: `L3/nrm2.md:120,197` (deleted file — self-resolves);
`L2/fold-family-stubs-intro.md:30` (STRIKE); `L2/divfree-projector.md:75,330`;
`L2/normalize.md:18,30,39,53,64,85,87,92,102,127`; `L2/index.md:118,138` (dep-map row :118
STRIKE; :138 re-point); `L2/reciprocal.md:108,388`.

**Inbound to `L3/dot`**: `L2/dot.md:25,78,94` (deleted — self-resolves);
`L3-L2/orthogonalize-variant-split.md:134,259`; `L4/dot.md:38,175,208`;
`L4/index.md:52,112(×2)`; `L3/blas1-intro.md:21` (STRIKE bullet);
`L3/nrm2.md:195` (deleted — self-resolves); `L3/chebyshev.md:385`;
`L3/index.md:29,39,78` (:39 dep-map row STRIKE; :29,:78 prose re-point);
`L3/orthogonalize.md:162,215,386,402,474`; `L3/inner_product.md:163,167,421` (combinator's own
pointers — convert to self-section refs / strike "the firm L3 leaf" framing);
`L3/ksp_solve.md:136`.

**Inbound to `L3/nrm2`**: `L2/nrm2.md:32,91,131,154` (deleted — self-resolves);
`L4/nrm2.md:39,161,195`; `L4/index.md:55,120(×2)`; `L3/blas1-intro.md:21` (STRIKE);
`L3/orthogonalize.md:409`; `L3/reciprocal.md:41`; `L3/inner_product.md:294,346,425`
(combinator's own pointers — convert/strike); `L3/index.md:42,49` (:42 dep-map row STRIKE;
:49 prose re-point); `L3/chebyshev.md:386`; `L3/normalize.md:19,25,43,54,56,77,79,84,94,119,147`;
`L3/ksp_solve.md:136`.

### Surface (ii) — prose code-spans (LOW tier, non-breaking)

Many of the body-link hits are prose mentions that double as code-spans; re-pointed together
with surface (i). No additional bare-backtick-only mentions found beyond the linked ones.

### Surface (iii) — frontmatter typed `edges:` blocks (silent-dangler tier)

`grep -rnE '(depends-on|reference|lifts-from|lifts-kernel-impl|realizes-kernel-api)[^]]*\b<slug>\b'`
plus the list-item form `- <slug>` / `- target: <slug>`. Hits (excluding deleted files'
own frontmatter + a comment-line false positive at `L3/nrm2.md:15`):

| File:line | edge | names | re-point |
|---|---|---|---|
| `L2/fold-family-stubs-intro.md:8` | `reference` | `L2/dot` | STRIKE (folded into combinator) |
| `L2/fold-family-stubs-intro.md:9` | `reference` | `L2/nrm2` | STRIKE |
| `L3/blas1-intro.md:8` | `reference` | `L3/dot` | re-point → `L3/inner_product` (dedupe; already listed :9) |
| `L3/blas1-intro.md:11` | `reference` | `L3/nrm2` | STRIKE (consumer; `L3/inner_product` already listed) |
| `L2/nrm2.md:10` | `reference` | `L3/nrm2` | deleted file — self-resolves |
| `L3/nrm2.md:23` | `depends-on (lowers-to)` | `L2/nrm2` | deleted file — self-resolves |
| `L3/nrm2.md:25` | `depends-on (composes)` | `L3/dot` | deleted file — self-resolves |
| `L3/normalize.md:7` | `depends-on` | `L3/nrm2` | **re-point → `L3/inner_product`** (consumer-of note in comment) |
| `L3/orthogonalize.md:29` | `depends-on (composes)` | `L3/dot` | **re-point → `L3/inner_product`** (specialization note in comment) |
| `L4/dot.md:9` | `depends-on` | `L3/dot` | **re-point → `L3/inner_product`** (the kept verb's lift edge) |
| `L4/nrm2.md:8` | `depends-on` | `L3/nrm2` | **re-point → `L3/inner_product`** (consumer; kept verb) |

All re-points are firm→firm (rank-legal; `unresolved_depends_on_targets` stays 0).

### SUMMARY.md (the chapter registry — must drop the deleted entries)

`SUMMARY.md:107` `[dot](./L3/dot.md)`, `:110` `[nrm2](./L3/nrm2.md)`, `:152` `[dot](./L2/dot.md)`,
`:153` `[nrm2](./L2/nrm2.md)` — STRIKE all four (the chapters no longer exist).

## Proposed changes

The full edit set is large (~60 line-level re-points). Below are the load-bearing deletions,
the combinator §-section folds (the leaf-fact absorption), the frontmatter `depends-on`
re-points (the silent-dangler tier), the SUMMARY + index + intro strikes, and the
representative consumer re-points. The harvester/integrator applies the per-anchor body-link
re-points mechanically against the inventory above (each `](./dot.md)` → the §Specializations
anchor; each `](./nrm2.md)` → the §Consumer anchor; each `](../L3/dot.md)` →
`](../L3/inner_product.md#specializations-the-members-as-notes-under-the-combinator)`; etc.).

### 1. Delete the four standalone stubs

```delete:book/src/L2/dot.md
```

```delete:book/src/L2/nrm2.md
```

```delete:book/src/L3/dot.md
```

```delete:book/src/L3/nrm2.md
```

### 2. Fold the retained leaf-level facts into the combinators

The combinators already carry the conjugation table, the `tdot` caveat, the `std::abs` guard
reference, and the consuming context. The ONE fact not yet stated at the combinator that the
stubs uniquely carried is the **`&y==this` self-dot fast-path as `dot`'s unique evidence
anchor** (already in `L2/inner_product` §Semantics + §Evidence — `vector.cpp:266,679`) and the
**`std::abs` defensive-guard load-bearing classification pointer** (already in
`L2/inner_product` §"Consumer (NOT an instance)" via the law-5 PSD-at-diagonal). On audit, the
folds are content-complete already — no leaf fact is lost on deletion. The combinator edits are
therefore (a) adding a one-line "the named members are notes here; the standalone leaf chapters
were eliminated cycle-127" provenance to each §Specializations + §Consumer, and (b) converting
the combinators' OWN inbound pointers (`L3/inner_product` lines naming `./dot.md`/`./nrm2.md`
as "the firm L3 leaf") into self-section references.

```edit:book/src/L3/inner_product.md
  The firm L3 [`dot`](./dot.md) leaf is this specialization; under the redirect it
  re-expresses through this combinator rather than re-deriving the base form (its leaf
  slim is cycle-051 — not edited here).
```
→
```edit:book/src/L3/inner_product.md
  `dot` at L3 IS this specialization (no standalone leaf chapter — the residual
  `L3/dot` specialization-stub was eliminated cycle-127, RE-style, its conjugation
  variant-axis + krylov-step consuming context folded into this section). The kept named
  L4 verb [`L4/dot`](../L4/dot.md) re-expresses through this combinator.
```

```edit:book/src/L3/inner_product.md
  Co-defined with `dot` at L3 [`dot`](./dot.md); carried with the type-API-surface-only
```
→
```edit:book/src/L3/inner_product.md
  Co-defined with `dot` (no standalone L3 chapter); carried with the type-API-surface-only
```

```edit:book/src/L3/inner_product.md
scalar map `α ↦ √|α|` applied to that output. The firm L3 [`nrm2`](./nrm2.md) leaf stays a
standalone **consumer** entry (do-NOT-merge boundary, cycle-049 D2 (b.2) DECIDED +
cycle-051 carve-out); its consumer-of-this-combinator note lands when its leaf is slimmed
(cycle-051) — **not** edited here. Law 5 (PSD at the diagonal) is exactly the property that
```
→
```edit:book/src/L3/inner_product.md
scalar map `α ↦ √|α|` applied to that output. `nrm2` at L3 IS this consumer (no standalone
leaf chapter — the residual `L3/nrm2` consumer-stub was eliminated cycle-127, RE-style, the
load-bearing `std::abs` defensive guard + the Arnoldi-sub-diagonal / residual-norm consuming
context folded into this section; do-NOT-merge boundary preserved — `nrm2` is the
`√∘abs∘inner_product` consumer, NOT a fold member). The kept named L4 verb
[`L4/nrm2`](../L4/nrm2.md) consumes this combinator at the diagonal. Law 5 (PSD at the
diagonal) is exactly the property that
```

(The §Dependencies / §Evidence list items at `L3/inner_product.md:294,346,421,425` that name
`./dot.md` / `./nrm2.md` are re-pointed to in-section anchors or struck — applied by the
integrator against the inventory; the combinator's own §Consumer / §Specializations now
contain the folded leaf facts so no outward link is needed.)

### 3. Re-point the surviving L4 verbs' frontmatter depends-on (silent-dangler tier)

```edit:book/src/L4/dot.md
  depends-on:
    - target: L4/inner_product
      kind: specializes
    - L3/dot
```
→
```edit:book/src/L4/dot.md
  depends-on:
    - target: L4/inner_product
      kind: specializes
    - L3/inner_product           # L3/dot leaf eliminated into the combinator (cycle-127, RE-style); this verb is its Hermitian/symmetric specialization (see L3/inner_product §Specializations)
```

```edit:book/src/L4/nrm2.md
  depends-on:
    - L4/inner_product
    - L3/nrm2
```
→
```edit:book/src/L4/nrm2.md
  depends-on:
    - L4/inner_product
    - L3/inner_product           # L3/nrm2 leaf eliminated into the combinator (cycle-127, RE-style); this verb is the √∘abs∘inner_product CONSUMER at the diagonal (NOT a fold member — see L3/inner_product §Consumer)
```

### 4. Re-point the consumer frontmatter depends-on

```edit:book/src/L3/normalize.md
  depends-on:
    - L3/nrm2
    - L3/linear_combination    # scal arity-1 leaf eliminated into the combinator (RE6, cycle-124); the rescale û = scal(1/β, x) is the arity-1 specialization (see linear_combination §arity-specializations)
```
→
```edit:book/src/L3/normalize.md
  depends-on:
    - L3/inner_product         # nrm2 consumer-stub eliminated into the combinator (cycle-127, RE-style); the norm β = nrm2(x) is the √∘abs∘inner_product consumer at the diagonal (see inner_product §Consumer)
    - L3/linear_combination    # scal arity-1 leaf eliminated into the combinator (RE6, cycle-124); the rescale û = scal(1/β, x) is the arity-1 specialization (see linear_combination §arity-specializations)
```

```edit:book/src/L3/orthogonalize.md
    - target: L3/dot
      kind: composes              # same-layer body primitive: the projection-coefficient inner product H_j = op.dot(w_eff(j), V[j])
```
→
```edit:book/src/L3/orthogonalize.md
    - target: L3/inner_product
      kind: composes              # same-layer body primitive: the projection-coefficient inner product H_j = op.dot(w_eff(j), V[j]); the dot specialization-stub was eliminated into the combinator (cycle-127, RE-style — see inner_product §Specializations)
```

### 5. Strike the navigational-container intro edges + bullets

```edit:book/src/L2/fold-family-stubs-intro.md
  reference:
    - L2/dot
    - L2/nrm2
---

# L2 fold-family specialization / consumer stubs

The once-standalone same-named BLAS-1 leaves, **reduced to thin specialization / consumer
stubs** under their fold combinators (cycle-052 vocabulary-shift-redirect refactor —
the combinator is the entry, these are pointers up to it). Each stub **defers** all
semantics / laws / fusion-rotation framing to its combinator and keeps only its unique
L0 anchors + its one variant-axis row.

The four `linear_combination` arity members (`scal`/`axpy`/`axpby`/`axpbypcz`) were
**eliminated cycle-124 (RE6)**, their unique L0 anchors folded into
[`linear_combination` §Arity specializations](./linear_combination.md#arity-specializations) —
the combinator is now the sole family entry.

Specialization / consumer stubs of [`inner_product`](./inner_product.md) (do-NOT-merge —
codomain / fold distinction load-bearing, §"Fold-cohort boundary"):

- [`dot`](./dot.md) — the `M = I` Hermitian/symmetric **specialization** (the conjugation
  variant-axis — `dot` Hermitian vs `tdot` unconjugated — is the value-bearing leaf fact).
- [`nrm2`](./nrm2.md) — the `√ ∘ abs ∘ inner_product` **consumer** at `y=x` (NOT a fold
  member); the `std::abs` defensive guard preserved as an explicit numerical claim.

Both `firm` (specialization / consumer stubs). Chapters are alphabetical.
```
→
```edit:book/src/L2/fold-family-stubs-intro.md
  reference:
    - L2/inner_product
    - L2/linear_combination
---

# L2 fold-family combinators (former specialization / consumer stubs — eliminated)

The once-standalone same-named BLAS-1 leaves have all been **eliminated into their fold
combinators** (the combinator is the entry; per the 2026-06-01 vocabulary-shift redirect the
residual same-named per-layer leaf-floors are the retired rectangular pattern).

The four `linear_combination` arity members (`scal`/`axpy`/`axpby`/`axpbypcz`) were
**eliminated cycle-124 (RE6)**, their unique L0 anchors folded into
[`linear_combination` §Arity specializations](./linear_combination.md#arity-specializations).

The two `inner_product` reduce-family stubs were **eliminated cycle-127 (RE-style)**, their
unique leaf-level facts folded into [`inner_product`](./inner_product.md):
- the `M = I` Hermitian/symmetric **specialization** `dot` (conjugation variant-axis + the
  `Dot`/`TransposeDot` kernels + self-dot fast path) → §"Specializations";
- the `√ ∘ abs ∘ inner_product` **consumer** `nrm2` at `y=x` (NOT a fold member — do-NOT-merge;
  the `std::abs` defensive guard preserved) → §"Consumer (NOT an instance)".

[`inner_product`](./inner_product.md) and [`linear_combination`](./linear_combination.md) are
now the sole family entries; the kept named L4 verbs `dot`/`nrm2` rise alongside the combinator
as the permitted dual.
```

(`L3/blas1-intro.md` gets the analogous strike of `- L3/dot` / `- L3/nrm2` from its
`reference:` block + the `[`dot`](./dot.md)` / `[`nrm2`](./nrm2.md)` body links re-pointed to
the `inner_product` anchors; applied per inventory.)

### 6. Strike the SUMMARY.md chapter entries

```edit:book/src/SUMMARY.md
  - [dot](./L3/dot.md)
```
→ (remove the line)

```edit:book/src/SUMMARY.md
  - [nrm2](./L3/nrm2.md)
```
→ (remove the line)

```edit:book/src/SUMMARY.md
  - [dot](./L2/dot.md)
```
→ (remove the line)

```edit:book/src/SUMMARY.md
  - [nrm2](./L2/nrm2.md)
```
→ (remove the line)

### 7. Strike the L2/index + L3/index dep-map rows for the deleted leaves

`L2/index.md:117` (`[`dot`](./dot.md)` row), `:118` (`[`nrm2`](./nrm2.md)` row),
`L3/index.md:39` (`[`dot`](./dot.md)` row), `:42` (`[`nrm2`](./nrm2.md)` row) — STRIKE the four
dep-map rows (the leaves no longer exist; the combinator `inner_product` row already stands and
its §Specializations/§Consumer now carry the folded notes). The prose mentions
`L2/index.md:138`, `L3/index.md:29,49,78` re-point to the `inner_product` anchors. NOTE: D5
(WAVE-2, this cycle) reconciles the L2/index firm-count prose against these deletions — my
strikes of :117/:118 are the deletions D5 reconciles against (the planner sequenced D5 after D4
for exactly this).

## Supporting evidence

- `book/src/L2/inner_product.md` (firm cycle-019/050) — §"Specializations" (`:176`),
  §"Consumer (NOT an instance)" (`:449`), §Signature kernel table (`:168-174`), §"tdot"
  (`:322`), §Evidence (the self-verified L0 anchors `vector.cpp:263-274,664-685`,
  `linalg/operator.cpp:598-617`). The combinator that absorbs the folded leaf facts.
- `book/src/L3/inner_product.md` (firm cycle-050) — §"Specializations" (`:146`),
  §"Consumer (NOT an instance)" (`:333`), §Semantics consuming-context (`:215`). The L3 home.
- `book/src/L2/dot.md`, `L2/nrm2.md`, `L3/dot.md`, `L3/nrm2.md` — the four stubs being
  eliminated; each already self-describes as a specialization-stub / consumer-stub deferring
  to the combinator (`L2/dot.md:1-12` lede; `L2/nrm2.md:17-25` lede; `L3/dot.md:17-26`;
  `L3/nrm2.md:37-45`).
- `book/src/L2/fold-family-stubs-intro.md:20-23` + `book/src/L3/blas1-intro.md:20` — the RE6
  precedent text (the four `linear_combination` arity members already eliminated cycle-124),
  the directly-analogous prior elimination this D4 completes.
- `book/src/L4/dot.md` / `L4/nrm2.md` (firm cycle-069 D2) — the SURVIVING kept named verbs
  (`black-box-vs-accelerated-kernels` §2 dual); their `depends-on: L3/dot`/`L3/nrm2` edges
  re-point to `L3/inner_product`. Out of D4 scope, NOT deleted.
- `book/src/concepts/black-box-vs-accelerated-kernels.md` §2 — the "kept named abstraction
  rises alongside the combinator" disposition that keeps the L4 verbs distinct (and out of
  this elimination's scope).
- Inbound-link sweep (this invocation): the four-slug grep across all three surfaces (body
  links, prose code-spans, frontmatter typed edges) is reproduced in §"Inbound-link inventory".
- OQ `inner-product-family-re-style-elimination-candidate` (the migrated plan-item source).

## Open questions / caveats

- **Body-link re-point volume.** ~60 line-level body-link re-points across ~20 consumer files
  (`L2/reciprocal` 9, `L2/normalize` 10, `L3/normalize` 11, `L3/orthogonalize` 6,
  `divfree-projector`, `chebyshev`, `ksp_solve`, the two indexes, the two intros, the two L4
  verbs, `orthogonalize-variant-split`). All re-point to two stable anchors
  (`inner_product.md#specializations-...` for `dot`; `inner_product.md#consumer-...` for
  `nrm2`). The integrator applies them mechanically against the §"Inbound-link inventory"; I
  have given the representative + load-bearing edits explicitly (deletions, combinator folds,
  frontmatter re-points, SUMMARY/index/intro strikes). Flag for the critic: verify the two
  mdBook anchor slugs resolve (`## Specializations (the members, as notes under the
  combinator)` → `#specializations-the-members-as-notes-under-the-combinator`; `## Consumer
  (NOT an instance): nrm2 / matrix-weighted-norm` → `#consumer-not-an-instance-nrm2--matrix-weighted-norm`
  — note the double-hyphen from ` / `).
- **`L4/dot` `kind: specializes` edge to `L4/inner_product` is unaffected** — only the
  `L3/dot` blocking-lift edge re-points. The L4 verb's own specialization relationship to the
  L4 combinator is intact.
- **Anchor-stability risk if the combinator §-headings are reworded.** If a future pass renames
  `## Specializations (the members, as notes under the combinator)` the ~30 inbound anchor
  links break. Consider (out of D4 scope) shortening both headings to stable
  `## Specializations` / `## Consumer (not an instance)` in a follow-up, with a single
  count-owner sweep — flagged, not done here (would widen the blast radius mid-refactor).
- **D4↔D5 coupling (handled by sequencing).** My strikes of `L2/index.md:117,118` change the
  L2 firm dep-map row count; D5 (WAVE-2, dep D4) reconciles the L2/index count prose against
  the post-D4 state. No co-write — D5 owns the count prose, D4 owns the row strikes.
- **`L3/nrm2.md:15` frontmatter-grep false positive** — the slug `L2/nrm2` appears inside a
  prose COMMENT line in `L3/nrm2.md`'s frontmatter, not a typed edge; `L3/nrm2.md` is deleted
  anyway so it self-resolves. Noted so the integrator does not chase a phantom edge.
