---
agent: lifter
invoked_at: 2026-06-04T001017Z
scope: L4 consumer re-anchor — solve_family rough-in (test-coverage-bounded) → firm (D1-conditional, D1 FIRMED)
status: integrated
integrated_at: 2026-06-04T015500Z
integration_commit: 7784b49
integration_notes: "Applied clean as D2 (cycle-086, batch-27 position 2/3). Consumer re-anchor of solve_family maturity word rough-in (test-coverage-bounded) → firm across gram_reduce.md (consumes-row + dep-map) + electrostatic.L4 + magnetostatic.L4 + solve_family.md §Evidence/§Provenance; NARROWED the electrostatic/magnetostatic §Status own-constituent gate from 2 (solve_family + gram_reduce) to 1 (gram_reduce only) WITHOUT flipping status: seed (the honest 1-of-2-gates non-flip; both columns verified seed post-edit). gram_reduce's OWN firmness DELIBERATELY UNCHANGED. RESOLVED OQ solve-family-md-stale-evidence-provenance-lines-after-firm-promotion (the §Evidence/§Provenance stale lines, re-located to :213/:214 after D1's §Status body replacement, cleaned). Byte-disjoint from D1. Build clean."
inputs:
  - reports/2026-06-04T013000Z-lowering-verifier-cycle-086-solve-family/CYCLE.md (D1 — promoted solve_family → firm; 1-of-2-gates finding, NO column flip)
  - reports/2026-06-04T000130Z-cycle-planner-cycle-086/CYCLE.md (D2 scope)
  - book/src/L4/gram_reduce.md (consumer — frontmatter :8 + dep-map :202)
  - book/src/feature/electrostatic.L4.md (consumer — :8, :39, :56, :63, :69)
  - book/src/feature/magnetostatic.L4.md (consumer — :8, :39, :56, :63, :69)
  - book/src/L4/solve_family.md (§Evidence :169 + §Provenance :170 stale-after-promotion prose D1 deferred to D2)
---

# CYCLE: Re-anchor solve_family maturity in consumers — rough-in (test-coverage-bounded) → firm

## Summary

D1 (`reports/2026-06-04T013000Z-lowering-verifier-cycle-086-solve-family/CYCLE.md`) **firmed** `book/src/L4/solve_family.md` from `rough-in (test-coverage-bounded)` → `firm` via the firm-on-positive-structure / syntactic-identity escape (the c082/c083 route; all three load-bearing laws are syntactic identities / closed-form read-offs of positive source, the element-independence claim decisively discharged by the `const`-`BaseKspSolver::Mult`-with-telemetry-only-state body at `ksp.cpp:297-310`). This is the firm branch of the D2 re-anchor: I flip every stale `solve_family` maturity label in the consumer files to `firm`. **The electrostatic/magnetostatic columns STAY `status: seed`** — D1's load-bearing 1-of-2-gates finding is that firming `solve_family` discharges only the FIRST of their two own-constituent gates; the SECOND, `gram_reduce` (`rough-in (test-coverage-bounded)`, convergently blocked on the `matrix-weighted-norm` √-cascade NO-GO-HELD), still gates them. So the own-constituent-gate narration NARROWS from "two own-constituents rough-in (`solve_family` + `gram_reduce`)" to "one own-constituent rough-in (`gram_reduce`); `solve_family` now firm", and the `status: seed` frontmatter token is UNCHANGED in both columns. This is a PURE re-anchoring pass — structure/prose preserved, only the `solve_family` maturity word firms up plus the narrowed-gate narration. I also include the bounded §Evidence/§Provenance stale-prose cleanup in `solve_family.md:169-170` that D1 explicitly deferred to D2 (D1's lines-144-148-only edit did not cover them).

## Proposed changes

### 1. `book/src/L4/gram_reduce.md` — firm solve_family's maturity in the consumes-row + dep-map row (gram_reduce's OWN status UNCHANGED)

```edit:book/src/L4/gram_reduce.md
[old]:
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — produces the solution family [xᵢ] this combinator reduces over; the upstream stage in the composition root)
[new]:
  - book/src/L4/solve_family.md (firm — produces the solution family [xᵢ] this combinator reduces over; the upstream stage in the composition root)
```

```edit:book/src/L4/gram_reduce.md
[old]:
- [`solve_family`](./solve_family.md) (rough-in (test-coverage-bounded)) — produces the
  solution family `[xᵢ]` this combinator reduces over (the upstream composition-root stage).
[new]:
- [`solve_family`](./solve_family.md) (firm) — produces the
  solution family `[xᵢ]` this combinator reduces over (the upstream composition-root stage).
```

(Note — `gram_reduce`'s own `firmness: rough-in (test-coverage-bounded)` at `:4` is DELIBERATELY UNCHANGED: gram_reduce stays rough-in because it folds the rough-in `matrix-weighted-norm` + `bilinear-form` — the √-cascade NO-GO-HELD — independent of the now-firm `solve_family` it consumes upstream.)

### 2. `book/src/feature/electrostatic.L4.md` — firm solve_family labels + narrow the own-constituent-gate narration; `status: seed` UNCHANGED

Frontmatter `composes:` row (`:8`):

```edit:book/src/feature/electrostatic.L4.md
[old]:
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-terminal map)
[new]:
  - book/src/L4/solve_family.md (firm — fixed-operator per-terminal map)
```

Stage-(2) prose label (`:39`):

```edit:book/src/feature/electrostatic.L4.md
[old]:
2. **Per-terminal map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**rough-in (test-coverage-bounded)**). The L4 fixed-operator map-over-RHS-family combinator
[new]:
2. **Per-terminal map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**firm**). The L4 fixed-operator map-over-RHS-family combinator
```

"lowers cleanly outward" promotion-route clause (`:56`):

```edit:book/src/feature/electrostatic.L4.md
[old]:
The whole feature therefore lowers cleanly outward to the L4 backend surface: `electrostatic = capacitance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: the composition is clean, but under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers) the column stays `seed` because two of its **directly-owned** constituents — the [`solve_family`](../L4/solve_family.md) per-terminal map and the [`gram_reduce`](../L4/gram_reduce.md) capacitance reduction — are `rough-in (test-coverage-bounded)`. This is a genuine own-constituent gate (these are directly-composed vocabulary ops, NOT sibling columns); firming `solve_family` + `gram_reduce` is the promotion route.
[new]:
The whole feature therefore lowers cleanly outward to the L4 backend surface: `electrostatic = capacitance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: the composition is clean, but under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers) the column stays `seed` because the [`gram_reduce`](../L4/gram_reduce.md) capacitance reduction — a **directly-owned** constituent — is `rough-in (test-coverage-bounded)`. The [`solve_family`](../L4/solve_family.md) per-terminal map is now **firm** (c086, the firm-on-positive-structure / syntactic-identity escape), so the own-constituent gate has narrowed from two directly-owned rough-in constituents to ONE: firming `gram_reduce` is the remaining promotion route — and that is itself convergently blocked on the `matrix-weighted-norm` √-cascade (NO-GO-HELD), which `gram_reduce` folds.
```

Dep-map table maturity cell (`:63`):

```edit:book/src/feature/electrostatic.L4.md
[old]:
| per-terminal solve map | [`solve_family`](../L4/solve_family.md) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:34-36, 59, 68-69, 89` |
[new]:
| per-terminal solve map | [`solve_family`](../L4/solve_family.md) | firm | `electrostaticsolver.cpp:34-36, 59, 68-69, 89` |
```

§Status own-constituent-gate narration (`:69`) — narrow the gate from two constituents to one; `status: seed` UNCHANGED:

```edit:book/src/feature/electrostatic.L4.md
[old]:
`seed` — the first feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. This column **stays `seed`** — not on a sibling-column blocker, but on a genuine **own-constituent gate**: two of its directly-composed L4 constituents are not yet firm — the [`solve_family`](../L4/solve_family.md) per-terminal solve map (`rough-in (test-coverage-bounded)`) and the [`gram_reduce`](../L4/gram_reduce.md) `w = 1` voltage-specialization capacitance reduction (`rough-in (test-coverage-bounded)`, which folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) over the family-pair grid). The composition is sound (stage (1) the firm [`fe_assemble`](../L4/fe_assemble.md), the reduction a clean fold of evaluations), but two directly-owned constituents being rough-in is the own-constituent gate; firming `solve_family` + `gram_reduce` is the promotion route (NOTE: this overrides the priorities.md #1 expectation that electrostatic flips this cycle — the on-disk constituent evidence governs). This chapter carries the *compositional* claim (electrostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `electrostaticsolver.cpp:21-98` (`Solve`) + `:100-138` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
[new]:
`seed` — the first feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. This column **stays `seed`** — not on a sibling-column blocker, but on a genuine **own-constituent gate** that has now NARROWED to a single remaining constituent: the [`gram_reduce`](../L4/gram_reduce.md) `w = 1` voltage-specialization capacitance reduction (`rough-in (test-coverage-bounded)`, which folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) over the family-pair grid). The other directly-composed constituent, the [`solve_family`](../L4/solve_family.md) per-terminal solve map, is now **firm** (c086, the firm-on-positive-structure / syntactic-identity escape — its concatenation-homomorphism is `map`'s definitional list-homomorphism, its operator-capture-once hoist is read off the positive `SetOperators`-outside-the-loop source, and its element-independence is a `const`-`BaseKspSolver::Mult`-with-telemetry-only-state read-off). The composition is sound (stage (1) the firm [`fe_assemble`](../L4/fe_assemble.md), the reduction a clean fold of evaluations), but one directly-owned constituent (`gram_reduce`) remaining rough-in is the own-constituent gate; firming `gram_reduce` is the remaining promotion route — and `gram_reduce` is itself convergently blocked on the `matrix-weighted-norm` √-cascade (NO-GO-HELD), so this column does not flip this cycle. This chapter carries the *compositional* claim (electrostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `electrostaticsolver.cpp:21-98` (`Solve`) + `:100-138` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
```

### 3. `book/src/feature/magnetostatic.L4.md` — mirror of (2); `status: seed` UNCHANGED

Frontmatter `composes:` row (`:8`):

```edit:book/src/feature/magnetostatic.L4.md
[old]:
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-source map)
[new]:
  - book/src/L4/solve_family.md (firm — fixed-operator per-source map)
```

Stage-(2) prose label (`:39`):

```edit:book/src/feature/magnetostatic.L4.md
[old]:
2. **Per-source map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**rough-in (test-coverage-bounded)**). The L4 fixed-operator map-over-RHS-family combinator
[new]:
2. **Per-source map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**firm**). The L4 fixed-operator map-over-RHS-family combinator
```

"lowers cleanly outward" promotion-route clause (`:56`):

```edit:book/src/feature/magnetostatic.L4.md
[old]:
The whole feature therefore lowers cleanly outward to the L4 backend surface: `magnetostatic = inductance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: the composition is clean, but under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers) the column stays `seed` because two of its **directly-owned** constituents — the [`solve_family`](../L4/solve_family.md) per-source map and the [`gram_reduce`](../L4/gram_reduce.md) inductance reduction — are `rough-in (test-coverage-bounded)`. This is a genuine own-constituent gate (directly-composed vocabulary ops, NOT sibling columns); firming `solve_family` + `gram_reduce` is the promotion route.
[new]:
The whole feature therefore lowers cleanly outward to the L4 backend surface: `magnetostatic = inductance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: the composition is clean, but under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers) the column stays `seed` because the [`gram_reduce`](../L4/gram_reduce.md) inductance reduction — a **directly-owned** constituent — is `rough-in (test-coverage-bounded)`. The [`solve_family`](../L4/solve_family.md) per-source map is now **firm** (c086, the firm-on-positive-structure / syntactic-identity escape), so the own-constituent gate has narrowed from two directly-owned rough-in constituents to ONE: firming `gram_reduce` is the remaining promotion route — and that is itself convergently blocked on the `matrix-weighted-norm` √-cascade (NO-GO-HELD), which `gram_reduce` folds.
```

Dep-map table maturity cell (`:63`):

```edit:book/src/feature/magnetostatic.L4.md
[old]:
| per-source solve map | [`solve_family`](../L4/solve_family.md) | rough-in (test-coverage-bounded) | `magnetostaticsolver.cpp:34-35, 66, 76-77, 99` |
[new]:
| per-source solve map | [`solve_family`](../L4/solve_family.md) | firm | `magnetostaticsolver.cpp:34-35, 66, 76-77, 99` |
```

§Status own-constituent-gate narration (`:69`) — narrow the gate from two constituents to one; `status: seed` UNCHANGED:

```edit:book/src/feature/magnetostatic.L4.md
[old]:
`seed` — the second feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic](./electrostatic.L4.md) exemplar. **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. This column **stays `seed`** — not on a sibling-column blocker, but on a genuine **own-constituent gate** identical to electrostatic's: two of its directly-composed L4 constituents are not yet firm — the [`solve_family`](../L4/solve_family.md) per-source solve map (`rough-in (test-coverage-bounded)`, the second witness of the fixed-operator corner) and the [`gram_reduce`](../L4/gram_reduce.md) `w = 1/(IᵢIⱼ)` current-normalized inductance reduction (`rough-in (test-coverage-bounded)` — the same shared symmetric-Gram reduction as the electrostatic capacitance, the weight the only difference; it folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) over the family-pair grid). The composition is sound (stage (1) the firm [`fe_assemble`](../L4/fe_assemble.md), the reduction a clean fold of evaluations), but two directly-owned constituents being rough-in is the own-constituent gate; firming `solve_family` + `gram_reduce` is the promotion route (overriding the priorities.md #1 expectation that magnetostatic flips this cycle — the on-disk constituent evidence governs). This chapter carries the *compositional* claim (magnetostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `magnetostaticsolver.cpp:22-108` (`Solve`) + `:110-204` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
[new]:
`seed` — the second feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic](./electrostatic.L4.md) exemplar. **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. This column **stays `seed`** — not on a sibling-column blocker, but on a genuine **own-constituent gate** identical to electrostatic's, that has now NARROWED to a single remaining constituent: the [`gram_reduce`](../L4/gram_reduce.md) `w = 1/(IᵢIⱼ)` current-normalized inductance reduction (`rough-in (test-coverage-bounded)` — the same shared symmetric-Gram reduction as the electrostatic capacitance, the weight the only difference; it folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) over the family-pair grid). The other directly-composed constituent, the [`solve_family`](../L4/solve_family.md) per-source solve map (the second witness of the fixed-operator corner), is now **firm** (c086, the firm-on-positive-structure / syntactic-identity escape). The composition is sound (stage (1) the firm [`fe_assemble`](../L4/fe_assemble.md), the reduction a clean fold of evaluations), but one directly-owned constituent (`gram_reduce`) remaining rough-in is the own-constituent gate; firming `gram_reduce` is the remaining promotion route — and `gram_reduce` is itself convergently blocked on the `matrix-weighted-norm` √-cascade (NO-GO-HELD), so this column does not flip this cycle. This chapter carries the *compositional* claim (magnetostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `magnetostaticsolver.cpp:22-108` (`Solve`) + `:110-204` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
```

### 4. `book/src/L4/solve_family.md` — D1-deferred §Evidence + §Provenance stale-after-promotion cleanup (bounded; lines D1's :144-148-only edit did not cover)

D1's proposed-changes touched only the frontmatter `firmness:` line and §Status lines 144-148. D1 explicitly deferred (its §Proposed-changes closing note + §Open-questions bullet 2) the two stale-after-promotion lines at `:169` (§Evidence final bullet) and `:170` (§Provenance), which still describe the superseded `rough-in (test-coverage-bounded)` maturity. These are NOT in D1's §Status scope and ARE the "stale residual maturity prose elsewhere / §Evidence/§Provenance D1 explicitly deferred" that the D2 scope assigns to me. Minimal patches:

§Evidence final bullet (`:169`):

```edit:book/src/L4/solve_family.md
[old]:
- **No dedicated test** exercises the `Solve(mesh)` outer sweep (the drivers are integration-level, not unit-tested under `reference/palace/test/unit/`); the L0 evidence is the driver source above. This keeps the entry at `rough-in (test-coverage-bounded)` for its map-fusion / concatenation-homomorphism laws.
[new]:
- **No dedicated test** exercises the `Solve(mesh)` outer sweep (the drivers are integration-level, not unit-tested under `reference/palace/test/unit/`); the L0 evidence is the driver source above. Per the firm-on-positive-structure escape (c086 D1, CLAUDE.md §Methodology invariants, the c082/c083 route), the absence of a dedicated test does NOT gate the map-fusion / concatenation-homomorphism laws, which are syntactic identities over fully-specified positive source — see §Status for the firm verdict.
```

§Provenance line (`:170`):

```edit:book/src/L4/solve_family.md
[old]:
- **Provenance**: mined by `reports/2026-06-02T002600Z-combinator-miner-solve-family-combinator/CYCLE.md` (c054 D1; the signature, layer justification, laws, 2 witnesses); landed as the rough-in dep-map row `book/src/L4/index.md:76`; firmed (to `rough-in (test-coverage-bounded)`) by this dispatch (cycle-055 D1).
[new]:
- **Provenance**: mined by `reports/2026-06-02T002600Z-combinator-miner-solve-family-combinator/CYCLE.md` (c054 D1; the signature, layer justification, laws, 2 witnesses); landed as the rough-in dep-map row `book/src/L4/index.md:76`; landed `rough-in (test-coverage-bounded)` by cycle-055 D1; promoted to `firm` by the cycle-086 D1 lowering-verifier law-confidence pass (`reports/2026-06-04T013000Z-lowering-verifier-cycle-086-solve-family/CYCLE.md`, the firm-on-positive-structure / syntactic-identity escape).
```

## Discipline notes

- **Pure re-anchoring, high→low preserved.** Every edit is a maturity-word flip (`rough-in (test-coverage-bounded)` → `firm` for `solve_family` only) plus the narrowed-gate re-narration. No LHS/RHS shape change, no signature change, no decomposition change, no rewrite-direction inversion. The feature columns' composition prose (`electrostatic = capacitance_reduce ∘ solve_family ∘ fe_assemble`, mirror for magnetostatic) is byte-unchanged; only the gating clause narrows.
- **`status: seed` frontmatter DELIBERATELY UNCHANGED in both columns** — per D1's load-bearing 1-of-2-gates finding and the cycle-086 plan's HONEST-FINDING (`gram_reduce` still gates, convergently blocked on the `matrix-weighted-norm` √-cascade NO-GO-HELD). I flip the `solve_family` constituent maturity and narrow the gate narration from two own-constituents to one, but I do NOT touch the `status:` token. The columns are NOT promoted this cycle.
- **`gram_reduce`'s own `firmness:` UNCHANGED** — I firmed only `solve_family`'s maturity word in `gram_reduce.md`'s consumes-row + dep-map row (the upstream constituent `gram_reduce` reduces over); `gram_reduce` itself stays `rough-in (test-coverage-bounded)` (it folds the rough-in `matrix-weighted-norm` + `bilinear-form`).
- **§Evidence/§Provenance cleanup is the D1-deferred bounded touch** — D1's §Proposed-changes closing note + §Open-questions bullet 2 explicitly handed the `solve_family.md:169-170` stale-after-promotion lines to D2 (or a finalize hygiene pass), and confirmed its own edit touched only frontmatter + §Status (lines 144-148). The two lines I patch (`:169` map-fusion-laws-keep-it-rough-in bullet, `:170` Provenance "firmed (to rough-in (test-coverage-bounded))" line) are outside D1's applied edit range — no overlap, no double-write. The §Status (D1's) is now the firm authority both lines defer to.
- **No prose-correction in the L0-evidence sense was needed** — this is a clean maturity re-anchor following D1's verdict, not a backward-convention or drifted-citation fix.

## Supporting evidence

- D1 verdict + promotion: `reports/2026-06-04T013000Z-lowering-verifier-cycle-086-solve-family/CYCLE.md` (§Summary "promote `solve_family` `rough-in (test-coverage-bounded)` → `firm`"; §Proposed-changes the frontmatter `firmness: firm` flip + §Status re-narration + `verified_against:` block; §Open-questions bullet 1 the 1-of-2-gates column note, bullet 2 the §Evidence/§Provenance deferral to D2, bullet "D2 (lifter) consumer re-anchor is now UNLOCKED to the firm branch").
- The firm-on-positive-structure escape precedent: `book/src/L4/sparameter_reduce.md` §Status (c083), `book/src/L4/eigenfreq_qfactor_reduce.md` §Status (c082) — the same syntactic-identity route, the sibling output-product verbs.
- The convergent blocker keeping `gram_reduce` (and therefore the columns) gated: the `matrix-weighted-norm` √-cascade NO-GO-HELD (c080 D1; the escape ruled INAPPLICABLE there because the norm-axiom laws are inner-product-structure theorems the L0 source only numerically asserts).
- Consumer files re-anchored: `book/src/L4/gram_reduce.md` (`:8`, `:202`); `book/src/feature/electrostatic.L4.md` (`:8`, `:39`, `:56`, `:63`, `:69`); `book/src/feature/magnetostatic.L4.md` (`:8`, `:39`, `:56`, `:63`, `:69`); plus the D1-deferred `book/src/L4/solve_family.md` (`:169`, `:170`).

All `[old]` anchors were taken verbatim from the on-disk files (grep + `Read`) this dispatch and confirmed exact-match unique within their files (the `solve_family` maturity strings are distinct per-occurrence by their surrounding context; the two `gram_reduce.md` rows differ in frontmatter-vs-dep-map phrasing; each feature-file occurrence differs in its sentence context).

## Open questions / caveats

- **No `book/src/L4/index.md` / `book/src/feature/index.md` matrix-cell flip is in my scope.** The cycle-086 plan §Overlap-analysis states the `feature/index.md` matrix is NOT touched (no column `status` flips → no matrix-cell drift) and `L4/index.md`'s firm-count bump from D1's `solve_family` promotion is the integrator-finalize's housekeeping (count-owner), not a producer write. Per the index-table-status-cell guard: the column `status` cells in `feature/index.md` correctly stay `seed` (the columns did NOT promote), so there is NO index-cell desync to flip for the feature matrix. If `L4/index.md` carries a per-row maturity cell for the `solve_family` dep-map row (`book/src/L4/index.md:76`, the row D1's §Provenance names), that cell would need flipping `rough-in (test-coverage-bounded)` → `firm` in the SAME pass — but that row is the `solve_family` operator's OWN index cell (owned by D1's promotion, the `solve_family.md` `## Status` flip), NOT a consumer cell, so it belongs to D1's blast radius / the finalize count-owner, not this consumer re-anchor. **Flagging for the integrator:** confirm whether `book/src/L4/index.md:76` (the `solve_family` row) needs a `firm` maturity-cell flip alongside D1's promotion; if it is a hand-maintained status cell it should flip in D1's pass or at finalize, not silently drift. (D1's §Provenance already names `index.md:76` as the landed dep-map row.)
- **The `electrostatic`/`magnetostatic` column FLIP remains NOT scheduled and NOT claimed** — convergently gated on the now-singly-remaining `gram_reduce` → `matrix-weighted-norm` √-cascade. The batch-27 meta-phase (fires after c087) weighs whether this convergent blocker has accumulated enough downstream demand (it now gates `gram_reduce` → capacitance/inductance/electrostatic/magnetostatic AND `domain_energy_reduce` → energy-fields) to justify the dedicated √-cascade own-cycle wave under its sharpened re-weigh trigger (D1 OQ bullet 1, plan §Open-questions bullet 1). This is intake for the meta-phase, not a change I make.
- **No abstractor reread triggered** — the firmed `solve_family` signature did NOT shift (D1 firmed the laws' confidence, not the signature/notation); the lift stayed pure rewriting throughout. No firm-signature-contradicts-theme-assumption flag.
