---
agent: layer-intro-author
invoked_at: 2026-06-01T154713Z
scope: concepts/erasure-scope.md — NEW cross-cutting concept page (four-root erasure-scope taxonomy)
status: integrated
integrated_at: 2026-06-01T161013Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-046 D2, applied clean — THE ONLY book/ mutation of the cycle. Created book/src/concepts/erasure-scope.md (NEW four-root erasure-scope taxonomy concept page; verified ABSENT pre-apply) + SUMMARY.md surgical insert ([erasure-scope] row after [eigsolve]) + concepts/index.md surgical insert (erasure-scope | layer-pattern row, alphabetical). The kind classification was the critic's one plan-kind-consistency:warning — repairer left unrepairable + routed to integrator; ADJUDICATED `layer-pattern` at integration (the page names how the L3>L2 layer-edge works — layer-mechanism, not process-methodology; reinforced by the layer-pattern sibling concepts sequential-obstruction + tensor-field-lift). All 14 live links resolve; built clean (concepts/erasure-scope.html, linkcheck2 green). Appended 2 OQ entries (erasure-scope-kind-classification CLOSED decision-of-record + erasure-scope-l3-l2-index-line-anchor-drift-risk open low-severity caveat). Gate hits: 0 (plan-kind adjudication non-blocking; citecheck 4 ok). No deferrals/rejections.
---

# CYCLE: concepts/erasure-scope.md

## Summary

Authors the NEW cross-cutting concept page `book/src/concepts/erasure-scope.md` (verified ABSENT on disk — a genuine create). The page gives the **four-root erasure-scope taxonomy** (RATIFIED batch-13 meta-phase) a cross-cutting home adjacent to `concepts/sequential-obstruction.md` and `concepts/tensor-field-lift.md`. The page transcribes + cross-references the canonical write-up that already exists verbatim in `book/src/L3-L2/index.md` §Working-Notes (the §Erasure-scope-taxonomy block, lines 67–71 — taxonomy intro at 67, the four roots at 68–71) and §Vocabulary-cohort (lines 56–61); it does NOT restate the per-theme algebraic content (that lives in the four substantive L3>L2 theme files), and it forwards every citation to those theme files.

The taxonomy: the substantive (non-identity) L3>L2 themes — those that carry real iteration-rotation content, where the L3 form names a first-class `sequential-obstruction` and the L3>L2 hop **erases the iteration view** — split by the **scope of what is erased** into four roots:

1. **unconditional-single-loop** — `ksp-solve-outer-driver` / `ksp_solve` (whole operator IS the Palace-authored loop).
2. **variant-conditional-single-loop** — `orthogonalize-variant-split` / `orthogonalize` (MGS branch obstructs; CGS/CGS2 lift).
3. **unconditional-nested-double-loop** — `chebyshev-nested-recurrence` / `chebyshev` (inner `k`-recurrence + outer `pc_it` sweep, both sequential).
4. **opaque-library** — `eigsolve-opaque-eigen-iteration` / `eigsolve` (loop lives entirely outside Palace; L3 marks a boundary, L2 erases the mark).

The page folds in the `concepts-sequential-obstruction-opaque-library-marker-distinction` (c045 D1): a `sequential-obstruction` marker rooted in opaque-library-ownership (no Palace recurrence to render — root 4) is structurally distinct from a Palace-authored renderable-then-erased recurrence (roots 1–3). This distinction is made explicit and cross-linked to `concepts/sequential-obstruction.md`.

## Verification performed

All four theme files confirmed on disk with accurate opening-paragraph anchors:
- `book/src/L3-L2/ksp-solve-outer-driver.md` (exists; §intro line 3 defines the unconditional driver theme).
- `book/src/L3-L2/orthogonalize-variant-split.md` (exists; §intro lines 3–15 define the variant-split theme; MGS branch obstructs).
- `book/src/L3-L2/chebyshev-nested-recurrence.md` (exists; §intro lines 3–16 define the nested-double-loop theme).
- `book/src/L3-L2/eigsolve-opaque-eigen-iteration.md` (exists; §intro lines 3–22 define the opaque-library theme + the marker-vs-rendering distinction).
- Canonical source `book/src/L3-L2/index.md` §Erasure-scope-taxonomy verified at lines 67–71 (taxonomy intro at 67; the four roots at 68/69/70/71); §Vocabulary-cohort substantive themes at lines 56–61. Cross-cutting concept anchors `concepts/sequential-obstruction.md` and `concepts/tensor-field-lift.md` both exist.

## Proposed changes

### 1. Create `book/src/concepts/erasure-scope.md`

```edit:book/src/concepts/erasure-scope.md
[old]:
[new]:
# Concept: erasure-scope

The **erasure scope** of a substantive L3>L2 lowering is *how much* of an operator's iteration view the L3>L2 hop erases. It is the classifying axis of the **substantive / non-identity** L3>L2 themes — the themes where the rotation carries real content because the L3 form names a first-class [`sequential-obstruction`](sequential-obstruction.md) (and, where Palace authors the loop, renders an explicit `iterate_while`-family tail recursion), and the L3>L2 hop **erases the iteration view** so the obstruction survives only as L2-vocabulary non-laws.

This axis cuts across the substantive L3>L2 cohort and the [`tensor-field-lift`](tensor-field-lift.md) / [`sequential-obstruction`](sequential-obstruction.md) concepts. It does NOT apply to the thin `-body-identity` themes (the BLAS-1 leaves, the fork-independent standalone floors, the fused composites, the constructed-operator gates): those carry **no** substantive erasure — the operator is L3-native by signature shape (no element loop, no obstruction), the body IS the identity, and there is nothing to erase. Erasure scope is only meaningful where there is an iteration view to erase.

The canonical write-up of the taxonomy lives in `book/src/L3-L2/index.md` §Erasure-scope-taxonomy (lines 67–71; the four roots at 68–71) and §Vocabulary-cohort (lines 56–61). This page is the cross-cutting home; it forwards the per-theme detail to the four substantive L3>L2 theme files.

## The four roots

The four substantive L3>L2 themes populate the four corners of the axis. Each erases a different *scope* of iteration view; each forwards its algebraic detail (the explicit L3 form, the L2 shadow non-laws, the citations) to its theme file.

1. **unconditional-single-loop** — the whole Palace-authored operator *is* the loop; the erasure holds for **every** parameter value.
   - Theme: [`ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md). Operator: `ksp_solve` ([`L3/ksp_solve`](../L3/ksp_solve.md) → [`L2/ksp_solve`](../L2/ksp_solve.md)).
   - The L3 explicit `iterate_while_L3` tail recursion (carrying the outer-loop obstruction) lowers to the L2 outer-driver-by-role composition; the obstruction shadows to the L2 fold non-mergeability / no-fold-lift non-laws. Cycle-021.

2. **variant-conditional-single-loop** — the substantive erasure is confined to **one variant branch**; the other branches lift cleanly on both sides of the hop.
   - Theme: [`orthogonalize-variant-split`](../L3-L2/orthogonalize-variant-split.md). Operator: `orthogonalize` ([`L3/orthogonalize`](../L3/orthogonalize.md) → [`L2/orthogonalize`](../L2/orthogonalize.md)).
   - The MGS `j`-loop is the obstruction (numerical-stability-rooted); CGS/CGS2 are batched global statements that lift. The MGS obstruction shadows to the column-order-non-commutativity non-law + the collective-shape residual axis. The per-step body is identity-in-form across all arms. The **first** substantive theme for a `partial-obstruction` operator. Cycle-044.

3. **unconditional-nested-double-loop** — a **nested double loop** (inner recurrence + outer sweep, both sequential); the erasure holds for every parameter value, but over a nested structure neither single-loop sibling exhibits.
   - Theme: [`chebyshev-nested-recurrence`](../L3-L2/chebyshev-nested-recurrence.md). Operator: `chebyshev` ([`L3/chebyshev`](../L3/chebyshev.md) → [`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md)).
   - The inner degree-`order` `k`-recurrence and the outer `pc_it` Richardson sweep are both explicit `iterate_while_pure_L3` tail recursions carrying first-class obstructions; they lower to the L2 `sweep`-iterated-by-role composition. The two obstructions shadow to the step-reordering / `pc_it`-commutativity / polynomial-expansion non-laws. The inner obstruction shares `orthogonalize`'s numerical-stability root. The per-inner-step body is identity-in-form. Cycle-045.

4. **opaque-library** — the loop lives **entirely outside Palace**; Palace authors no recurrence, so L3 cannot render the loop at all and can only attach an obstruction **marker** at the library boundary, which L2 then erases.
   - Theme: [`eigsolve-opaque-eigen-iteration`](../L3-L2/eigsolve-opaque-eigen-iteration.md). Operator: `eigsolve` ([`L3/eigsolve`](../L3/eigsolve.md) → [`L2/eigsolve`](../L2/eigsolve.md)).
   - The eigen-iteration loop (Krylov-Schur restart, Arnoldi/Lanczos basis extension, Rayleigh-Ritz extraction, convergence test) is inside SLEPc `EPSSolve` / ARPACK `naupd` RCI. The L3 `eigsolve` per-step body `apply_shift_invert = apply_linop ▷ ksp_solve [▷ scale_untransform ▷ project]` lifts cleanly; the loop is named `eigen_iterate` by role with an obstruction marker; L2 references the library fold by role only, erasing the marker (it shadows to the "Opening of the eigen-iteration fold at L2" + fold-merge / restart-associativity non-laws). Obstruction sub-kind `opaque-library-ownership` (per CLAUDE.md) — never re-promotable. Cycle-045.

## Renderable vs. marker — the root-4 distinction

The four roots divide into two structural shapes by **whether L3 can render the loop**:

- **Roots 1–3 (renderable-then-erased).** Palace authors the recurrence, so the L3 form *renders* it — an explicit `iterate_while`-family tail recursion (one loop, one variant branch's loop, or two nested loops) carrying a first-class [`sequential-obstruction`](sequential-obstruction.md) over a Palace-visible loop-carried dependency. The L3>L2 hop **erases the rendered iteration view**; the obstruction survives only as L2-vocabulary non-laws. The recurrence is real, Palace-visible, and the erasure is a deliberate layer-surface choice.

- **Root 4 (marker-only, opaque-library).** Palace authors **no** recurrence — the loop is owned by a third-party library reached through a thin wrapper (SLEPc / ARPACK). The L3 form cannot render the loop as a tail recursion; the `sequential-obstruction` is present only as a **marker** at the library boundary. The L2 hop **erases the marker**. The distinguishing structural fact: a substantive iteration-rotation erasure can arise from a loop Palace never wrote.

This is the `concepts-sequential-obstruction-opaque-library-marker-distinction`: a `sequential-obstruction` rooted in opaque-library-ownership (a marker, root 4) is distinct from a Palace-authored renderable-then-erased recurrence (roots 1–3). The distinction matters for promotion routing — a renderable obstruction (roots 1–3) records the Palace recurrence that L3 chose to surface; an opaque-library marker (root 4) records a boundary that Palace never sees inside and that is `never re-promotable`. See [`sequential-obstruction`](sequential-obstruction.md) §"Sub-kind: out-of-scope-obstruction" for the L0→L1 analogue of the same opaque-library boundary at a different layer edge.

## See also

- [concept: sequential-obstruction](sequential-obstruction.md) — the first-class L3 result that the substantive themes name; the marker-vs-rendering distinction above is rooted here.
- [concept: tensor-field-lift](tensor-field-lift.md) — the transparent L2→L3 lift the substantive themes are the *non-transparent* complement of; where the lift succeeds there is no erasure scope.
- `book/src/L3-L2/index.md` §Erasure-scope-taxonomy (lines 67–71; the four roots at 68–71) + §Vocabulary-cohort (lines 56–61) — the canonical taxonomy write-up this page is the cross-cutting home for.
```

### 2. Wire into `book/src/SUMMARY.md` (concepts section)

```edit:book/src/SUMMARY.md
[old]:  - [nested-constructed-operator-gate](./concepts/nested-constructed-operator-gate.md)
  - [eigsolve](./concepts/eigsolve.md)

# Design Artifacts
[new]:  - [nested-constructed-operator-gate](./concepts/nested-constructed-operator-gate.md)
  - [eigsolve](./concepts/eigsolve.md)
  - [erasure-scope](./concepts/erasure-scope.md)

# Design Artifacts
```

### 3. Wire into `book/src/concepts/index.md` (Index table)

The index table is alphabetically ordered; insert the `erasure-scope` row between `elementwise-product` and `finest-level-unwrap`. Kind = `layer-pattern` (it names how the L3>L2 lowering edge works, alongside `sequential-obstruction` / `tensor-field-lift`).

```edit:book/src/concepts/index.md
[old]:| [elementwise-product](./elementwise-product.md) | primitive |
| [finest-level-unwrap](./finest-level-unwrap.md) | primitive |
[new]:| [elementwise-product](./elementwise-product.md) | primitive |
| [erasure-scope](./erasure-scope.md) | layer-pattern |
| [finest-level-unwrap](./finest-level-unwrap.md) | primitive |
```

## Supporting evidence

- **Canonical source (verbatim transcription target):** `book/src/L3-L2/index.md` §Erasure-scope-taxonomy lines 67–71 (taxonomy intro at 67; the four roots at 68–71) + §Vocabulary-cohort substantive themes lines 56–61. The page transcribes the one-line semantics and forwards detail; it does not restate the per-theme algebraic-laws content.
- **The four substantive L3>L2 theme files (all verified on disk):**
  - `book/src/L3-L2/ksp-solve-outer-driver.md:3` — unconditional-single-loop (cycle-021).
  - `book/src/L3-L2/orthogonalize-variant-split.md:3-15` — variant-conditional-single-loop, MGS branch obstructs (cycle-044).
  - `book/src/L3-L2/chebyshev-nested-recurrence.md:3-16` — unconditional-nested-double-loop (cycle-045).
  - `book/src/L3-L2/eigsolve-opaque-eigen-iteration.md:3-22` — opaque-library + marker-vs-rendering distinction (cycle-045).
- **Cross-cutting concept anchors (both exist, live-linked):** `concepts/sequential-obstruction.md` (the marker the substantive themes name; §"Sub-kind: out-of-scope-obstruction" at lines 50–81 is the L0→L1 opaque-library analogue), `concepts/tensor-field-lift.md` (the transparent lift this axis is the non-transparent complement of).
- **Folded-in finding:** `concepts-sequential-obstruction-opaque-library-marker-distinction` (c045 D1) — made explicit as the §"Renderable vs. marker" section dividing root 4 from roots 1–3.
- **Operator L3/L2 entries cited (all exist):** `L3/ksp_solve` + `L2/ksp_solve`; `L3/orthogonalize` + `L2/orthogonalize`; `L3/chebyshev` + `L2/chebyshev-iteration`; `L3/eigsolve` + `L2/eigsolve`.

## Open questions / caveats

- **Page is a single-dispatch concept page** — no consolidated-tally / dual-registration situation applies (not landing into a layer index with a running count). No tally to own.
- **Kind classification.** Filed `erasure-scope` as `layer-pattern` (it names how the L3>L2 edge works, the same family as `sequential-obstruction` / `tensor-field-lift`). An alternative reading is `methodology` (it is an axis used to classify themes, like `variant-absorption`). I chose `layer-pattern` because the axis is *about the L3>L2 layer-edge surface shape* specifically, not the dissection process in general; flag for the critic if `methodology` is preferred.
- **Taxonomy is RATIFIED and complete (all four roots populated).** No coverage gap on the axis itself. The one residual L3>L2 denominator note (`apply_linop` lowering directly L3→L1 with no interposed L2 entry, the by-design 18th non-applicable case) is unrelated to erasure scope — `apply_linop` is a transparent lift (`tensor-field-lift`), not a substantive erasure, so it correctly does NOT appear on this page.
- **Line-number anchors into `L3-L2/index.md`** (67–71, 56–61) are plain-text source-locator references, not live links; if the §Working-Notes of that index is later recompacted those line numbers may drift. The reference is to the section by name (§Erasure-scope-taxonomy / §Vocabulary-cohort), which is stable; the line numbers are a convenience locator captured at cycle-046.
