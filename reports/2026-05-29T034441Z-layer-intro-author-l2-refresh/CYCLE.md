---
agent: layer-intro-author
invoked_at: 2026-05-29T034441Z
scope: L2 Part intro refresh (semantics overlay + Vocabulary-cohort subsection + dep-map + Working Notes)
status: integrated
integrated_at: 2026-05-29T06:05:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-020 finalize (staging row #9, LAST). Structural L2 Part-overview refresh of book/src/L2/index.md (two surgical [old]/[new] section rewrites): §Semantics-overlay + two emergent motifs (named-composition + fold cohorts) + NEW §Vocabulary cohort subsection + 5-row→7-row dep-map; §Working Notes 4 refreshed bullets. 5 firm ops + 2 live-linked stubs (incremental-least-squares, ksp_solve, materialized 2026-05-28). ORDERING PRECONDITION SATISFIED — this report's firm-orthogonalize dep-map assertions depended on the harvester-orthogonalize-l2-backfill (staging row #1) landing first; the critic's two FAILs + cross-ref warning are dissolved post-backfill (this report's critic is what CAUGHT the cycle-019 fence-truncation defect). L3 ksp_solve cross-ref left plain-text per dispatch directive (L3/ksp_solve.md now exists via row #5 — upgrade captured as OQ l2-index-ksp-solve-l3-crossref-upgrade-now-possible). NOT a count change (structural refresh). retroactive-budget 0; clean build."
---

# CYCLE: L2 intro refresh

## Summary

Refreshes `book/src/L2/index.md` to reflect L2's cycle-019 growth to **5 firm operators + 2 stubs**. The current intro is stale on three counts: (1) the dep-map lists only the 5 firm operators and omits the two now-materialized stubs (`ksp_solve`, `incremental-least-squares`); (2) there is no **Vocabulary-cohort** subsection (warranted now that firm + queued states coexist — per the cycle-004-origin role-spec template); (3) the Working Notes still claim `orthogonalize` and `incremental-least-squares` are "candidates for a future harvester" — but `orthogonalize` is now **firm** (harvested cycle-019) and both stubs now exist on disk.

This refresh also narrates the **two emergent L2 vocabulary motifs** the cycle-019 additions surfaced:
- **named-composition** — `orthogonalize` as the named `project ▷ subtract` (`dot` ▷ `axpy`) composition, the level-(b)-absorbed `op.orthog` surface `krylov-step` folds.
- **fold cohorts** — the do-NOT-merge boundary between `inner_product` (reduce-to-`Scalar`, folds the length axis) and `linear_combination` (reduce-to-`Tensor[N]`, folds the term axis, keeps `N`) — two distinct homomorphisms that share a `foldl` skeleton but must not be unified.

Two converging refresh flags fold into this dispatch: `L2-layer-intro-refresh-for-named-compositions` + `L2-layer-intro-refresh-for-fold-cohort`.

Scope confined to `book/src/L2/index.md` (75-line whole-section rewrite of lines 15–43). The cycle-020 wave-1 dot/scal/assemble-diagonal themes are L1>L0 and do not touch L2/index.md. The L3 `ksp_solve` driver/kernel complementarity flagged by wave-1 is cross-referenced as a **plain-text forward-reference** (no `L3/ksp_solve.md` on disk yet).

## On-disk firmness state surveyed (verbatim from chapter headers)

| Chapter | On-disk status | Harvest provenance |
|---|---|---|
| `krylov-step.md` | `firm` | harvested cycle-005 (2026-05-27T025354Z); promoted from rough-in (combinator-miner 2026-05-26T231843Z) |
| `chebyshev-iteration.md` | `firm` | harvested cycle-012; concrete entry behind `krylov-step` variant-axis 3 |
| `linear_combination.md` | `firm` | harvested cycle-018; constructive prong (b) of OQ blas1-variadic-linear-combination-fold-unification |
| `inner_product.md` | `firm` | harvested cycle-019; conjugation pinned per OQ inner-product-harvester-formalization-and-conjugation-pinning |
| `orthogonalize.md` | `firm` | harvested cycle-019; promoted from stub (`l2-named-composition-lifts`) |
| `incremental-least-squares.md` | `stub` | materialized 2026-05-28 (implied-component stub); owner `harvester` |
| `ksp_solve.md` | `stub` | materialized 2026-05-28 (implied-component stub); owner `harvester` |

No rough-in entries currently exist at L2 — the Vocabulary cohort splits **firm vs stub** (both states coexist, so the split is warranted; per role spec the split is skipped only when one state is empty).

Dep-map will hold 7 rows (5 firm + 2 stub) — well under the ~20-row promote-to-`dep-map.md` threshold; `index.md` stays in one file. The two stub rows use **live links** (`[slug](./slug.md)`) because the anchor files exist on disk (the plain-text-when-missing convention does not apply — both stubs are wired into `SUMMARY.md` at lines 42–43).

## Proposed changes

```edit:book/src/L2/index.md
[old]:
## Semantics (overlay)

L2 vocabulary: tensors, linear operators, quadrature rules, basis transformations, primitive operations (axpy, dot, matvec, gemv, trsv, scal, nrm2, …). State threading via explicit value semantics. Compositions of L1 primitives into method-step shapes are first-class at L2.

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | `(op: OpParams, s: IterState) → { state: IterState', outputs: StepOutputs }` | L1: `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`. L2-composition: `apply_BA`, `orthogonalization`. Concepts: `derived-view-hoisting`, `variant-absorption`, `first-iteration-unrolling`, `sequential-obstruction`, `solve-monad`, `state-stratification`, `solver-as-operator`. | `firm` (harvested cycle-005; promoted from rough-in proposed-by combinator-miner:2026-05-26T231843Z) |
| [`chebyshev-iteration`](./chebyshev-iteration.md) | `(op: ChebOp[N], x: Tensor[N], y: Tensor[N], initial_guess: Bool) → Tensor[N]` | L1: `apply_linop`, `axpy`, `axpby`, `scal`. Concepts: `elementwise-product`, `variant-absorption`, `sequential-obstruction`, `first-iteration-unrolling`. L1 sibling: `chebyshev-smoother`. L2 sibling: `krylov-step`. | `firm` (harvested cycle-012; the concrete L2 entry behind `krylov-step` variant-axis 3; test-coverage caveat, firm ratified) |
| [`linear_combination`](./linear_combination.md) | `[(Scalar, Tensor[N])] -> Tensor[N]` (≡ `foldl (\acc (a,t) -> acc + a·t) zeros pairs`) | L1 fixed-arity specializations: `scal` (arity 1), `axpy` (arity 2, coeff 1 fixed), `axpby` (arity 2), `axpbypcz` (arity 3). Concepts: `scalar-promotion` (element-type axis, concept-page-level sibling of this arity-axis unification; inherited with its open upstream dependency — OQ `scalar-promotion-typing-rule`, not yet committed). Sibling fold (do NOT merge): `dot` (reduce-to-scalar inner product). | `firm` (harvested cycle-018; promoted from rough-in proposed-by combinator-miner:2026-05-28T223022Z; constructive prong (b) of OQ blas1-variadic-linear-combination-fold-unification) |
| [`inner_product`](./inner_product.md) | `(x: Tensor[N], y: Tensor[N]) -> Scalar` (≡ `foldl (+) zero (zipWith kernel x y)`); M-weighted member `inner_product_M(x, M, y) = xᴴ M y` (arg-1-conjugated convention, pinned — matches the L1 `dot`/`bilinear-form` leaves; Palace's free-function `Dot(comm,x,y) = yᴴ x` conjugates arg-2, the deliberate L1 re-order — see entry §"Conjugation convention (pinned)"); plain ≡ `M = I` | L1 leaves it fuses up from: `dot` (Hermitian), `tdot` (unconjugated; firm but type-API-surface only — zero Palace call sites), `bilinear-form` (M-weighted member, rough-in). L2-composition for the weighted member: `apply_linop` (M applied to the linear/arg-1 operand). Concepts: `dot` (cross-cutting prose). **Sibling fold (do NOT merge):** `linear_combination` (reduce-to-`Tensor[N]`; folds the term axis, keeps `N`; different homomorphism). Consumer (NOT an instance): `nrm2` / `matrix-weighted-norm` = `√ ∘ inner_product` at `y=x`. | `firm` (harvested cycle-019; promoted from rough-in proposed-by combinator-miner:2026-05-28T231046Z; family-mode characterized combinator-miner:2026-05-29T023000Z; conjugation pinned per OQ inner-product-harvester-formalization-and-conjugation-pinning) |
| [`orthogonalize`](./orthogonalize.md) | `(op: OrthogOp, w: Tensor[N], V: Basis[N, m]) → { residual: Tensor[N], coeffs: Tensor[m] }` | L1 leaf it lifts: `orthogonalize` (firm). L1 primitives the stages compose: `dot` (project), `axpy` (subtract). Concepts: `orthogonalization`, `variant-absorption` (`:131`, residual-axis disclosure), `sequential-obstruction`. Consumers: `krylov-step` (level-(b) `op.orthog`), ROM basis-extension. Sibling fold (constituent, not parent): `inner_product` (rough-in). | `firm` (harvested cycle-019; promoted from stub; the `l2-named-composition-lifts` backlog item / OQ orthogonalize-as-future-L2-firstclass-entry) |
[new]:
## Semantics (overlay)

L2 vocabulary: tensors, linear operators, quadrature rules, basis transformations, primitive operations (axpy, dot, matvec, gemv, trsv, scal, nrm2, …). State threading via explicit value semantics. Compositions of L1 primitives into method-step shapes are first-class at L2.

Two L2 vocabulary **motifs** have emerged from the cycle-018/019 additions and now organize the firm cohort:

- **Named compositions** — a single Palace runtime-dispatched entry point unfolds into a canonical pipeline of L1 leaves under a named L2 surface. `orthogonalize` is the exemplar: it names the Gram-Schmidt `project ▷ subtract` composition (`dot` ▷ `axpy`), turning the opaque `gs_orthog ∈ {MGS, CGS, CGS2}` parameter into the visible per-variant batching/sequencing disclosed as the collective-shape residual axis. This is the level-(b)-absorbed `op.orthog` surface `krylov-step` folds. The stub `incremental-least-squares` (GMRES running-QR / Givens stream) is the queued second named composition.
- **Fold cohorts** — variadic reductions sharing a `foldl` skeleton but **distinct homomorphisms**, kept as separate L2 entries with an explicit *do-NOT-merge* boundary. The two folds:
  - `inner_product` folds the **length axis** to a `Scalar` (`foldl (+) zero (zipWith kernel x y)`) — the conjugation/element-type/weight specializations of `dot` / `tdot` / `bilinear-form`.
  - `linear_combination` folds the **term axis**, keeping `Tensor[N]` (`foldl (\acc (a,t) -> acc + a·t) zeros pairs`) — the arity specializations of `scal` / `axpy` / `axpby` / `axpbypcz`.

  They share the fold skeleton but target different codomains (`Scalar` vs `Tensor[N]`); merging them would erase the codomain distinction and the do-NOT-merge note carried in both entries' dep-map rows is load-bearing.

## Vocabulary cohort

**Firm at L2** (algebraic-laws + variant-axis-coverage complete):

- `krylov-step` — the recurring Krylov/polynomial step kernel (kernel half of the kernel-plus-driver shape; the driver half is L4 `iterate_while`).
- `chebyshev-iteration` — the three-term polynomial recurrence; concrete L2 entry behind `krylov-step` variant-axis 3.
- `linear_combination` — fold-cohort, reduce-to-`Tensor[N]`; the BLAS-1 scalar-weighted-sum arity family (`scal`/`axpy`/`axpby`/`axpbypcz`).
- `inner_product` — fold-cohort, reduce-to-`Scalar`; the BLAS-1 inner-product conjugation family (`dot`/`tdot`/`bilinear-form`); sibling fold of `linear_combination` (do-NOT-merge).
- `orthogonalize` — named-composition, `project ▷ subtract`; the Gram-Schmidt `op.orthog` surface `krylov-step` folds.

**Queued at L2** (stub — claim-free placeholder awaiting `harvester` refinement):

- `incremental-least-squares` (stub) — GMRES running-QR / Givens-rotation-stream small-dense LS update; the queued second named-composition (sibling to `orthogonalize`).
- `ksp_solve` (stub) — the L2 **outer-driver** wrap above the firm L1 `ksp_solve`: the restart / convergence-test loop that wraps the `krylov-step` kernel into a complete solve. Establishes the **non-identity** L2↔L1 relationship (distinct from the identity `L3>L2` `krylov-step-body-identity` theme).

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | `(op: OpParams, s: IterState) → { state: IterState', outputs: StepOutputs }` | L1: `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`. L2-composition: `apply_BA`, `orthogonalize` (the named composition below). Concepts: `derived-view-hoisting`, `variant-absorption`, `first-iteration-unrolling`, `sequential-obstruction`, `solve-monad`, `state-stratification`, `solver-as-operator`. | `firm` (harvested cycle-005; promoted from rough-in proposed-by combinator-miner:2026-05-26T231843Z) |
| [`chebyshev-iteration`](./chebyshev-iteration.md) | `(op: ChebOp[N], x: Tensor[N], y: Tensor[N], initial_guess: Bool) → Tensor[N]` | L1: `apply_linop`, `axpy`, `axpby`, `scal`. Concepts: `elementwise-product`, `variant-absorption`, `sequential-obstruction`, `first-iteration-unrolling`. L1 sibling: `chebyshev-smoother`. L2 sibling: `krylov-step`. | `firm` (harvested cycle-012; the concrete L2 entry behind `krylov-step` variant-axis 3; test-coverage caveat, firm ratified) |
| [`linear_combination`](./linear_combination.md) | `[(Scalar, Tensor[N])] -> Tensor[N]` (≡ `foldl (\acc (a,t) -> acc + a·t) zeros pairs`) | **Fold cohort — reduce-to-`Tensor[N]`, folds the term axis.** L1 fixed-arity specializations: `scal` (arity 1), `axpy` (arity 2, coeff 1 fixed), `axpby` (arity 2), `axpbypcz` (arity 3). Concepts: `scalar-promotion` (element-type axis, concept-page-level sibling of this arity-axis unification; inherited with its open upstream dependency — OQ `scalar-promotion-typing-rule`, not yet committed). **Sibling fold (do NOT merge):** `inner_product` (reduce-to-`Scalar`; different codomain/homomorphism). | `firm` (harvested cycle-018; promoted from rough-in proposed-by combinator-miner:2026-05-28T223022Z; constructive prong (b) of OQ blas1-variadic-linear-combination-fold-unification) |
| [`inner_product`](./inner_product.md) | `(x: Tensor[N], y: Tensor[N]) -> Scalar` (≡ `foldl (+) zero (zipWith kernel x y)`); M-weighted member `inner_product_M(x, M, y) = xᴴ M y` (arg-1-conjugated convention, pinned — matches the L1 `dot`/`bilinear-form` leaves; Palace's free-function `Dot(comm,x,y) = yᴴ x` conjugates arg-2, the deliberate L1 re-order — see entry §"Conjugation convention (pinned)"); plain ≡ `M = I` | **Fold cohort — reduce-to-`Scalar`, folds the length axis.** L1 leaves it fuses up from: `dot` (Hermitian), `tdot` (unconjugated; firm but type-API-surface only — zero Palace call sites), `bilinear-form` (M-weighted member, rough-in). L2-composition for the weighted member: `apply_linop` (M applied to the linear/arg-1 operand). Concepts: `dot` (cross-cutting prose). **Sibling fold (do NOT merge):** `linear_combination` (reduce-to-`Tensor[N]`; folds the term axis, keeps `N`; different homomorphism). Consumer (NOT an instance): `nrm2` / `matrix-weighted-norm` = `√ ∘ inner_product` at `y=x`. | `firm` (harvested cycle-019; promoted from rough-in proposed-by combinator-miner:2026-05-28T231046Z; family-mode characterized combinator-miner:2026-05-29T023000Z; conjugation pinned per OQ inner-product-harvester-formalization-and-conjugation-pinning) |
| [`orthogonalize`](./orthogonalize.md) | `(op: OrthogOp, w: Tensor[N], V: Basis[N, m]) → { residual: Tensor[N], coeffs: Tensor[m] }` | **Named composition — `project ▷ subtract`.** L1 leaf it lifts: `orthogonalize` (firm). L1 primitives the stages compose: `dot` (project), `axpy` (subtract). Concepts: `orthogonalization`, `variant-absorption` (`:131`, residual-axis disclosure), `sequential-obstruction`. Consumers: `krylov-step` (level-(b) `op.orthog`), ROM basis-extension. Sibling fold (constituent, not parent): `inner_product` (firm). | `firm` (harvested cycle-019; promoted from stub; the `l2-named-composition-lifts` backlog item / OQ orthogonalize-as-future-L2-firstclass-entry) |
| [`incremental-least-squares`](./incremental-least-squares.md) | *(stub — signature pending harvester refinement)* | **Queued named composition** (sibling to `orthogonalize`). GMRES running-QR / Givens-rotation-stream small-dense LS update. Concept page: `concepts/incremental-least-squares`. Implied-by: `krylov-step` (names it as future L2 candidate), plan item `l2-named-composition-lifts`. | `stub` (materialized 2026-05-28; owner `harvester`; OQ incremental-least-squares-as-future-L2-firstclass-entry + gmres-givens-stream-as-step-kernel-borderline) |
| [`ksp_solve`](./ksp_solve.md) | *(stub — signature pending harvester refinement)* | **Queued outer-driver** above L1 `ksp_solve`. Wraps the `krylov-step` kernel in the restart / convergence-test loop. Establishes the **non-identity** L2↔L1 relationship. L0 anchor: `L0/linalg-iterative-file`. Implied-by: firm `L1/ksp_solve` + concept `concepts/ksp_solve`, plan item `ksp-solve-l2-promotion-non-identity-substantive-gap`. | `stub` (materialized 2026-05-28; owner `harvester`; OQ ksp-solve-l2-promotion-non-identity-substantive-gap) |
```

```edit:book/src/L2/index.md
[old]:
- The cycle-005 firm-up did **not** introduce a new L2 entry for `orthogonalize` as a first-class L2 composition, even though `krylov-step` depends on it as a level-(b)-absorbed surface — that remains a candidate for a future harvester invocation. Same for `incremental-least-squares` (GMRES outer driver's small-dense kernel; currently lives as a concept page only).
[new]:
- **`orthogonalize` is now firm** (harvested cycle-019; promoted from stub). The cycle-005 deferral — "no first-class L2 entry for the level-(b)-absorbed `op.orthog` surface `krylov-step` folds" — is **closed**: [`orthogonalize.md`](./orthogonalize.md) names the `project ▷ subtract` (`dot` ▷ `axpy`) composition and discloses the `gs_orthog ∈ {MGS, CGS, CGS2}` variant as the collective-shape residual axis. It is the **named-composition** motif's exemplar.
- **Fold-cohort boundary (load-bearing, do NOT merge).** `inner_product` (cycle-019) and `linear_combination` (cycle-018) share a `foldl` skeleton but are distinct homomorphisms targeting different codomains: `inner_product` folds the **length axis** to `Scalar`; `linear_combination` folds the **term axis**, keeping `Tensor[N]`. The do-NOT-merge note is carried in both dep-map rows and in each entry's §"Sibling fold". `nrm2` / `matrix-weighted-norm` is a *consumer* of `inner_product` (`√ ∘ inner_product` at `y=x`), not an instance.
- **Two stubs queued for harvester refinement** (materialized 2026-05-28 under the implied-component stub policy):
  - [`incremental-least-squares.md`](./incremental-least-squares.md) — the GMRES outer driver's running-QR / Givens-stream small-dense kernel, currently a concept page (`concepts/incremental-least-squares`). The queued second **named-composition** (sibling to `orthogonalize`). Plan item `l2-named-composition-lifts`.
  - [`ksp_solve.md`](./ksp_solve.md) — the L2 **outer-driver** wrap above the firm L1 `ksp_solve`: the restart / convergence-test loop that wraps the `krylov-step` kernel into a complete solve. This is the substantive **non-identity** L2 coverage gap (distinct from the identity `L3>L2` `krylov-step-body-identity` theme). Plan item `ksp-solve-l2-promotion-non-identity-substantive-gap`.
- **L3 driver/kernel complementarity** (cycle-020 wave-1 harvester flag, cross-reference only — `L3/ksp_solve.md` not yet on disk): the L2 `ksp_solve` outer-driver wrap and the L3 `krylov-step` kernel form a driver/kernel pair across the L2↔L3 boundary mirroring the L2-kernel/L4-driver pair (`krylov-step` at L2, `iterate_while` at L4). When the L3 `ksp_solve` entry lands (wave-1 flagged an L3-index refresh need), this Working Note should grow a forward-reference to it. Stays a plain-text forward-reference here pending that entry's authorship.
```

## Supporting evidence

- **On-disk firmness survey** (table above) — read verbatim from each chapter's header / `## Status` line in `book/src/L2/`. 5 firm + 2 stub; zero rough-ins.
- **`SUMMARY.md` wiring** — `book/src/SUMMARY.md:36–43` lists all 7 L2 chapters under the L2 Part (`incremental-least-squares (stub)` and `ksp_solve (stub)` at lines 42–43). The two stub dep-map rows therefore use **live links** (anchor files exist + are wired); the plain-text-when-anchor-missing convention does not apply.
- **`orthogonalize` named-composition** — `book/src/L2/orthogonalize.md:1–14`: "lifts the firm L1 leaf `orthogonalize` … canonical composition `(project against V) then (subtract)` … level-(b)-absorbed `op.orthog` surface that `krylov-step` folds."
- **Fold-cohort do-NOT-merge boundary** — `book/src/L2/inner_product.md` §"Sibling fold (do NOT merge)" (dep-map row) and `book/src/L2/linear_combination.md` dep-map row; both entries pin the codomain distinction (`Scalar` vs `Tensor[N]`).
- **`variant-absorption.md:131` residual-axis citation** — carried verbatim from the existing dep-map row; it references the concept page `book/src/concepts/variant-absorption.md` line 131 (a concept-page line, not a Palace source line), used consistently in `book/src/L1/orthogonalize.md:99–105` ("MGS/CGS/CGS2 absorb at all three levels … under residual-axis disclosure"). No new Palace source claim introduced by this refresh.
- **Stub provenance** — `book/src/L2/ksp_solve.md:9–13` and `book/src/L2/incremental-least-squares.md:9–13` carry the "Implied by" provenance lists copied into the dep-map rows.
- **Dep-map row count** — 7 rows, under the ~20-row threshold; `index.md` stays single-file (no promote to `dep-map.md`).

## Open questions / caveats

- **L3 `ksp_solve` not yet authored.** Wave-1's flag for an L3-index intro refresh + L3 `ksp_solve` driver/kernel framing is out of this dispatch's L2 scope. The cross-reference in the Working Notes is intentionally a plain-text forward-reference. When the L3 entry lands, the L2 Working Note's last bullet should be upgraded to a live link, and the L2 `ksp_solve` stub's "non-identity L2↔L1" framing should be checked for consistency with the L3 `ksp_solve` kernel framing.
- **Stub-row signatures are placeholders.** The two stub rows carry *(stub — signature pending harvester refinement)* rather than a real signature, matching the claim-free stub discipline. When `harvester` refines either stub to rough-in/firm, this dep-map row gets the real signature + status bump (a future intro-refresh dispatch, or folded into the harvester's proposed-changes).
- **No rough-in cohort currently.** The Vocabulary-cohort subsection splits firm vs stub only (no rough-in state present at L2). If a future harvester lands a rough-in (e.g. promoting `incremental-least-squares` stub→rough-in mid-formalization), add a "**Rough-in at L2**" tier between the firm and stub tiers.
- **`scalar-promotion` open dependency unchanged.** The `linear_combination` row still carries its inherited open upstream dependency (OQ `scalar-promotion-typing-rule`, not yet committed) — not resolved by this refresh; carried verbatim.
