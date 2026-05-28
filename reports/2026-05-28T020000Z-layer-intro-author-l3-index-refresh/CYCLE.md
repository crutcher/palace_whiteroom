---
agent: layer-intro-author
invoked_at: 2026-05-28T020000Z
scope: L3 index ## Semantics (overlay) prose refresh — BLAS-1 cohort + matvec/apply_linop naming reconcile
status: integrated
integrated_at: 2026-05-28T072500Z
integration_commit: 5964cb4
integration_notes: "Applied cycle-012 (report 5 of 8). book/src/L3/index.md ## Semantics (overlay) prose refreshed -- names all 8 firm L3 operators grouped by kind; matvec (apply_linop) parenthetical reconcile. Closes 2 cycle-011 OQs (l3-index-semantics-overlay-blas1-cohort-prose-refresh + l3-index-matvec-naming-vs-apply_linop-slug). Clean run (all 8 critic checks pass, no repair). 0 gate hits. Build exit 0. LOW-severity scal.md:137 stale-prose + 7 back-reference re-point surfaced for cycle-013 (not OQ'd)."
---

# CYCLE: L3 index intro refresh

## Summary

Refreshes the `## Semantics (overlay)` prose in `book/src/L3/index.md` to bring the L3 vocabulary inventory line into alignment with the closed BLAS-1 cohort (per cycle-011 OQ `l3-index-semantics-overlay-blas1-cohort-prose-refresh`). After cycle-011 wave-1 the L3 layer grew from 1 firm operator (krylov-step) to 8 (krylov-step + apply_linop + axpy + axpby + axpbypcz + dot + nrm2 + scal). The dep-map table already reflects all 8; only the overlay prose lagged, listing just "matvec, axpy, dot, nrm2 as field operations" — 4 of 8, and not naming `scal` / `axpby` / `axpbypcz` / `apply_linop` literally.

The refresh:

1. **Names the full firm cohort** by the kinds of whole-tensor field operations now present at L3: linear-operator application (`apply_linop`), the linear-update family (`axpy` / `axpby` / `axpbypcz` / `scal`), the reductions (`dot` / `nrm2`), and the composition (`krylov-step`).
2. **Reconciles "matvec" with the formal `apply_linop` slug** (closing OQ `l3-index-matvec-naming-vs-apply_linop-slug`). Adopts the `matvec (apply_linop)` parenthetical form: "matvec" is retained as the casual name so existing dep-map / entry back-references to `book/src/L3/index.md:13`'s "matvec ... as field operations" advertisement remain meaningful, with the formal slug parenthesized — matching the `apply_linop` entry's own framing of `apply_linop` as "the matvec generalisation" (`book/src/L3/apply_linop.md:24`).
3. **Keeps L3 vocabulary** — whole-tensor field operations, no element loops; the BLAS-1 primitives are L3-native by signature shape; `krylov-step` is the composition. Reframes the inventory as describing the *kinds* of primitives (the OQ's suggested alternative), with the concrete slugs named inline, so the line does not silt up as future cohort members (`gemv`, `trsv`) land.

This is a Part-overview refresh, not operator authoring. No dep-map rows are touched (they are already complete and firm). No `book/` files other than `index.md` are touched. The `index.md` stays at ~40 lines, well under the ~200-line split threshold — no promotion to `semantics.md` / `dep-map.md` is warranted.

Note on the Vocabulary-cohort subsection (CLAUDE.md role-spec, added cycle-004): L3 now has 8 firm operators and **no** queued / rough-in / obstruction entries (the BLAS-1 cohort is closed; krylov-step is firm). Per the role-spec discipline "Skip the subsection when the layer has only firm entries (no queue)", the subsection is **not** added — the firm-vs-queued split is only useful when both states coexist. The overlay prose is the correct home for the cohort orientation here.

## Proposed changes

```edit:book/src/L3/index.md
[old]:
## Semantics (overlay)

L3 expresses:
- Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)
- Field transitions: state evolution over a single algorithmic step expressed as `state' = f(state, params)`
- Convolution-like patterns where applicable (stencil sweeps, restriction/prolongation)
- Sequential obstructions: explicit markers where global form is unavailable, with reason
[new]:
## Semantics (overlay)

L3 expresses:
- **Whole-tensor field operations** — primitives that act on whole tensors with no element loop exposed at the layer's vocabulary, L3-native by signature shape. The closed BLAS-1 cohort: matvec (`apply_linop`, the linear-operator-application generalisation of "matvec" — square and rectangular operators, real and complex, all operator representations absorbed), the linear-update family (`axpy`, `axpby`, `axpbypcz`, `scal`), and the reductions (`dot`, `nrm2`).
- **Field transitions** — state evolution over a single algorithmic step expressed as `state' = f(state, params)`. The composition operator `krylov-step` is the canonical instance: the value-threaded per-step kernel `(op, K, s) -> (K', s', outputs)` built from the whole-tensor field operations above.
- **Convolution-like patterns** where applicable (stencil sweeps, restriction/prolongation).
- **Sequential obstructions** — explicit markers where global form is unavailable, with reason (the outer loop folding `krylov-step` does not lift; recorded per `concepts/sequential-obstruction.md`).
```

## Supporting evidence

**Operators currently harvested + firm at this layer** (8; all firm per the dep-map table at `book/src/L3/index.md:19-28`):

- `krylov-step` — the composition; value-threaded per-step kernel (harvested cycle-010).
- `apply_linop` — matvec generalisation; opaque linear-operator application (harvested cycle-011 wave-1).
- `axpy` — `(α, x, y) -> α·x + y` (harvested cycle-011 wave-1).
- `axpby` — `(α, x, β, y) -> α·x + β·y`; subsumes `axpy` at β=1 (harvested cycle-011 wave-1).
- `axpbypcz` — `(α, x, β, y, γ, z) -> α·x + β·y + γ·z`; subsumes `axpby` at γ=0 (harvested cycle-011 wave-1).
- `dot` — inner product → scalar (harvested cycle-011 wave-1).
- `nrm2` — Euclidean norm → real scalar; `nrm2(x) = √dot(x, x)` (harvested cycle-011 wave-1).
- `scal` — `(α, x) -> α·x`; sibling-subsumed by `axpby` at β=0 (harvested cycle-011 wave-1).

**Naming reconcile evidence** (matvec → `apply_linop`):

- `book/src/L3/apply_linop.md:20` frames `apply_linop` as "one of the whole-tensor field operations the L3 layer's index advertises (`book/src/L3/index.md:11-14`), the per-step matvec primitive consumed by `krylov-step`."
- `book/src/L3/apply_linop.md:24` — "The L3 index (`book/src/L3/index.md:13`) explicitly lists 'matvec, axpy, dot, nrm2 as field operations' as L3 vocabulary; `apply_linop` is the matvec generalisation." The refresh adopts exactly this framing.
- OQ `l3-index-matvec-naming-vs-apply_linop-slug` (cycle-011, harvester) recommends either "matvec → apply_linop" prose touch-up or an "also known as: matvec" annotation. The chosen `matvec (apply_linop)` parenthetical satisfies both — the casual name is retained (so the back-reference linkage from the `apply_linop` entry to `index.md:13`'s "matvec" advertisement stays valid) and the formal slug is present.

**Cross-references to adjacent layers** (orientation only; the L3 layer is defined in L3 vocabulary per CLAUDE.md §Methodology invariants "Layers are defined high→low"):

- The cohort members' L1 anchors (the identity-in-form rotation targets) are named in each entry's dep-map row; the overlay does not restate them.
- `krylov-step` lifts from L4 `krylov-step` (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) and lowers to L2 `krylov-step` (`book/src/L3-L2/krylov-step-body-identity.md`); the overlay names `krylov-step` as the composition without restating the lowering themes (those are dep-map / lowering-Part content).

**Back-reference safety**: several entries cite `book/src/L3/index.md:13` (the "matvec, axpy, dot, nrm2" line) verbatim — `apply_linop.md:24`, `apply_linop.md:150`, `apply_linop.md:173`. The refresh keeps "matvec" and "axpy, dot, nrm2" as named tokens in the prose (now alongside the rest of the cohort), so those citations still resolve to a line carrying the same advertised tokens. The line number shifts (the bullet expands), but the entries cite the *content* ("matvec ... as field operations"), which is preserved and enriched, not removed.

## Open questions / caveats

- **Closes OQ `l3-index-semantics-overlay-blas1-cohort-prose-refresh`** (cycle-011, harvester) — the overlay prose now names the full closed BLAS-1 cohort. Recommend the integrator mark this OQ `resolved` on application.
- **Closes OQ `l3-index-matvec-naming-vs-apply_linop-slug`** (cycle-011, harvester) — the matvec/apply_linop divergence is reconciled via the `matvec (apply_linop)` parenthetical in the overlay. The naming is now consistent: "matvec" survives as the casual name, `apply_linop` is the formal slug, and the equivalence is stated inline (matching the `apply_linop` entry's framing). Recommend the integrator mark this OQ `resolved` on application.
- **Line-number drift in back-references**: entries cite `book/src/L3/index.md:13` for the "matvec ... as field operations" advertisement. The refresh expands the first bullet, so the advertised tokens move off line 13 to a longer bullet (now lines ~12 onward). The citations cite the *content* not a code range, so they remain semantically valid, but a future lifter/cross-cutter sweep could re-point them to the new line range for precision. Filed as a low-priority routing note, not a blocker — not opening a new OQ for it (the cited content is preserved; the drift is cosmetic). If the integrator prefers strict line-precision, the three citations in `apply_linop.md` (lines 20, 24, 150, 173 referencing `index.md:11-14` / `:13`) could be re-pointed in a follow-on touch-up, but that is harvester/lifter territory (the `apply_linop` entry is an operator entry, out of layer-intro-author authority).
- **`l3-vocabulary-inventory-gap`** (the broader parent OQ) is NOT closed by this refresh — that OQ tracks the question of which *additional* operators (`gemv`, `trsv`, `ksp_solve`, `eigsolve` near-identity candidates) might warrant L3 backfill beyond the closed BLAS-1 cohort. The overlay's reframing as "kinds of primitives" makes that OQ's future cohort growth absorbable without further prose churn, but the inventory-gap question itself remains open and routed to cycle-012+ planner.
- No `nrm2` stability-claim correction is touched here — that is OQ `concepts-nrm2-stability-claim-correction`, scoped to `book/src/concepts/nrm2.md` (a separate concepts/ page, one-page-per-invocation discipline). Out of scope for this index refresh.
