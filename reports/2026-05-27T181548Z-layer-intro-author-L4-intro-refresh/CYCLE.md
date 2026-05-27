---
agent: layer-intro-author
invoked_at: 2026-05-27T18:15:48Z
scope: L4 intro refresh post 3-firm-cohort + Vocabulary-cohort subsection
status: integrated
integrated_at: 2026-05-27T18:35:15Z
integration_commit: e4929aa
integration_notes: cycle-008 pass 7 (wave-2; FINAL). Semantics-overlay placeholder replaced with grounded 4-motif overlay + new Vocabulary cohort subsection (template adapted — middle slot uses L4>L3 cross-layer themes) + dep-map widened 4->5 columns with Lowers to column split. Closed cycle-006 OQ l4-layer-intro-refresh-unblocked-by-first-firm-row (2-cycle-carried).
closes: l4-layer-intro-refresh-unblocked-by-first-firm-row
---

# CYCLE: L4 intro refresh

## Summary

`book/src/L4/index.md` carries three firm operator rows after cycle-007 (`krylov-step` from cycle-006; `iterate-while` and `iterate-while-with-prev` from cycle-007 wave-1) and one firm L4>L3 lowering theme (`krylov-step-typed-wrapper-dissolution`, promoted to firm cycle-008 wave-1 by the lifter) plus one rough-in L4>L3 theme (`gmres-inner-loop-iterate-while-migration`, landed cycle-008 wave-2). The intro's `Semantics (overlay)` section still says "To be drafted as L4 operators are formalized" — a Phase-B-skeleton placeholder that the firm-row cohort has now obsoleted.

This dispatch refreshes the intro by (1) replacing the Semantics-overlay placeholder with grounded prose describing the three-stratum state-stratification + Solve-monad + value-threaded-combinator pattern shared across the three firm operators, (2) adding a **Vocabulary cohort** subsection between the overlay and the dep-map (per the cycle-004 L1 precedent — `book/src/L1/index.md:27-47`), and (3) extending the dep-map with a `Lowers to` column entry pointing at the L4>L3 theme rows for each operator. Closes the cycle-006 OQ `l4-layer-intro-refresh-unblocked-by-first-firm-row` (expanded per cycle-007 integrator-signals to include the Vocabulary cohort subsection).

The intro stays under 200 lines, so it is not split into a separate `semantics.md` / `dep-map.md`; the existing `book/src/L4/index.md` carries everything.

## Proposed changes

```edit:book/src/L4/index.md
[old]: ## Semantics (overlay)

(To be drafted as L4 operators are formalized through the `harvester` agent pipeline. The L4 calculus strawman lives at `../design/l4_calculus.md` and seeds the formal core.)

The semantics overlay describes:

- **Grammar** for terms: variables, abstractions, applications, let-bindings, tensor literals, primitive ops, monadic bind/return.
- **Evaluation rules**: β, let-substitution, δ-rules for primitive tensor ops, monad laws, sharing rules.
- **Type and shape rules**: typed judgments with symbolic tensor shapes; linear/affine annotations distinguishing operator-params-as-closure from sim-state-being-threaded.
- **Algebraic equational laws**: commutativity, associativity, distributivity where they hold; simplification rules connecting L3 forms to L4 monadic programs.

## Operator dep-map
[new]: ## Semantics (overlay)

The L4 calculus is specified in the strawman at [`../design/l4_calculus.md`](../design/l4_calculus.md) — BNF grammar for types / shapes / terms (§1), reduction rules (§2), small-step semantics for `iterate_while` (§3.7), and demand-pruning (§3.8). Operator entries cite and continue the strawman; they do not displace it. Pseudo-language conventions at L4 are Haskell `::` signatures + TypeScript `{ field: type }` records inside `text` fences, with `$$ ... $$` LaTeX math for reduction rules (per CLAUDE.md "L4 strawman is in-management" and "L4/L3 pseudo-language" invariants).

Across the three firm operators, four semantic motifs recur and together constitute the L4-layer vocabulary the consuming-slice writes against:

1. **Three-stratum state stratification.** [`state-stratification`](../concepts/state-stratification.md) splits all algorithm-relevant state into `SimState` (externally-visible; persists across the solve; threaded by the `Solve` monad), `OpParams` (operator-internal; captured once at solve construction; `readonly`), and slice-specific ephemeral bundles like `Krylov` (born at restart entry, discarded at restart exit; threaded as a plain value, not a monadic effect). The stratification is **structural** at L4 because the typing forbids cross-stratum aliasing; at L3 and below it collapses to a positional convention.
2. **`Solve` monad with localised `SimState` effect.** [`solve-monad`](../concepts/solve-monad.md) is `Solve a = StateT SimState Identity a`. The kernel body's effect domain is exactly `SimState` — typically a single `modify (\s -> s { it = s.it + 1 })` per step; everything else (operator applications, dense recurrences, ephemeral-bundle updates) lives outside the monad in `let`-bindings. This is the effect-localisation discipline `krylov-step`, `iterate-while`, and `iterate-while-with-prev` all honour.
3. **Value-threaded loop combinators with demand-pruned trajectories.** Iteration at L4 is `iterate_while` (and its bootstrap-carry variant `iterate_while_with_prev`) — tail-recursive value-threading folds whose per-step extras pile into a `trajectory` list, with [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) §3.8 demand-pruning rewriting the body to drop extras computations when no downstream consumer reads them. Consumers that read only `.final_state` automatically specialise to the "no monitoring" variant without a runtime flag.
4. **Variant absorption via `OpParams` `readonly` typing.** Variant selectors (preconditioner-presence, orthogonalisation kind, polynomial kind, restart shape, first-iteration-unrolled vs branch-in-body, in-place vs out-of-place) are absorbed at construction into `OpParams` per [`variant-absorption`](../concepts/variant-absorption.md); the `readonly` annotation makes their absence from the per-step kernel structural, not merely conventional.

Form-A vs Form-B (`krylov-step` Form A consumes [`iterate-while`](./iterate-while.md); Form B consumes [`iterate-while-with-prev`](./iterate-while-with-prev.md)) is a presentation rotation per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md); the two forms produce iteration-for-iteration-identical trajectories. `iterate-while-with-prev` definitionally degenerates to `iterate-while` when `β = ()` (Law 1 of the with-prev entry) — the two combinators are a family parameterised by whether a bootstrap closure-carry is needed.

The L4 form is uniformly **methodology-level**: Palace's C++ source has no direct L4 realisation. The three firm operators name typed shapes that the slice corpus (cg.md, gmres.md, chebyshev.md, arnoldi_step.md, polynomial_recurrence_step.md) writes against; their L0 evidence is the in-step branches and tail-recursive C++ loops that the L4 form rotates *out* (`reference/palace/palace/linalg/iterative.cpp:427` for the `iterate_while` shape; `:434-441` for the in-step `if (!it)` branch that `iterate_while_with_prev` removes).

## Vocabulary cohort

**Firm at L4 (3)** — the typed-wrapper Krylov step kernel plus the two value-threading loop combinators that drive it:

- [`krylov-step`](./krylov-step.md) — typed-wrapper Krylov step kernel against the three-stratum state record; Form A consumes `iterate-while`, Form B consumes `iterate-while-with-prev`. The L4 calculus's first firm step-body shape.
- [`iterate-while`](./iterate-while.md) — value-threaded tail-recursive loop with demand-pruned trajectory of per-step extras; canonical iteration primitive at L4 (every iterative algorithm reduces to one or more folds). Inherits small-step semantics from the strawman §3.7.
- [`iterate-while-with-prev`](./iterate-while-with-prev.md) — carry-bootstrapped variant of `iterate-while` that threads a `PrevCarry` closure parameter for the previous-iteration recurrence variable. The driver for [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)'s unrolled form; degenerates to `iterate-while` when `β = ()`.

**L4>L3 lowering themes** — what the L4 forms rotate to:

- [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) — firm (cycle-008 wave-1 lifter promotion). The wrapper machinery (state-stratification records, `Solve` monad, `OpParams` `readonly`, Form A/B distinction) dissolves into L3 value-threading; the kernel body's primitive sequence is identity-in-form, so no intermediate L3 `krylov-step` row is needed.
- [`gmres-inner-loop-iterate-while-migration`](../L4-L3/gmres-inner-loop-iterate-while-migration.md) *(rough-in; landed cycle-008 wave-2)* — the L4>L3 dissolution of the migrated GMRES inner loop under the (speculative) upstream re-rendering of `gmres.md` §L4's `inner_loop` as a direct `iterate_while` invocation. Firms once the upstream `gmres.md` self-rotation lands.

**Queued at L4** — none currently. The three firm operators close the cohort needed for the cycle-008-frontier work; the `solve-monad`'s `restart_cycle` and `solve_loop` outer drivers are referenced from concept pages but not yet anchored as L4 rows (potential cycle-009+ harvester scope; not blocking forward-frontier work).

## Operator dep-map
```

```edit:book/src/L4/index.md
[old]: | Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | Form A: `OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs })`. Form B (first-iteration-unrolled): `first_step :: OpParams -> Krylov -> (SimState -> Solve { sim, krylov, carry, outputs })` and `steady_step :: OpParams -> Krylov -> (PrevCarry -> SimState -> Solve { sim, krylov, carry, outputs })`. | Lowers to L2 [`krylov-step`](../L2/krylov-step.md) via L4>L3>L2 (L4>L3 = state-monad-threading rotation, cycle-006 abstractor; L3>L2 plausibly identity-in-form). Concepts: `state-stratification`, `solve-monad`, `first-iteration-unrolling`, `derived-view-hoisting`, `convergence-test`, `variant-absorption`. L4 rows: [`iterate-while`](./iterate-while.md) (Form A body), [`iterate-while-with-prev`](./iterate-while-with-prev.md) (Form B body). | `firm` (harvested cycle-006; promoted from cross-layer-cross-cutter recommendation 2026-05-27T025354Z) |
| [`iterate-while`](./iterate-while.md) | Pure: `α -> (α -> Bool) -> (α -> { state: α, ...e }) -> { final_state: α, trajectory: [{ ...e }] }`. Solve-threaded: `α -> (α -> Bool) -> (α -> Solve { state: α, ...e }) -> Solve { final_state, trajectory }`. Sugar: `iterate_while_pure :: α -> (α -> Bool) -> (α -> α) -> α`. | Concepts: `solve-monad`, `derived-view-hoisting`, `convergence-test`. L4 rows: consumed by [`krylov-step`](./krylov-step.md) Form A. Lowers to L3 via the body of `krylov-step-typed-wrapper-dissolution` (standalone theme pending cycle-008+ lowering-verifier follow-up per OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`). | `firm` (harvested cycle-007T160550Z; closes cycle-006 OQ `iterate-while-l4-anchor-missing`) |
| [`iterate-while-with-prev`](./iterate-while-with-prev.md) | Pure: `(α -> { state: α, prev: β, ...e }) -> α -> ((α, β) -> { state: α, prev: β, ...e }) -> (α -> Bool) -> { final_state, trajectory }`. Solve-threaded form lifts the step bodies through `Solve`. Degenerates to [`iterate-while`](./iterate-while.md) when `β = ()` (Law 1). | Concepts: `first-iteration-unrolling`, `derived-view-hoisting`, `solve-monad`. L4 rows: [`iterate-while`](./iterate-while.md) (companion / degenerate case); consumed by [`krylov-step`](./krylov-step.md) Form B. Lowers to L3 via the same theme as the companion (standalone follow-up pending per OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`). | `firm` (harvested cycle-007T160550Z; closes cycle-006 OQ `iterate-while-l4-anchor-missing`) |

Format expected for each entry:
- **Operator slug** (e.g., `solve`, `arnoldi_step`, `apply_preconditioner`)
- **Signature** with shape contracts
- **Algebraic laws** that hold
- **Direct dependencies** (other L4 operators consumed)
- **Status**: `rough-in` | `firm` | `deprecated`

## Working Notes

- This page is generated by `layer-intro-author`; operators are authored by `harvester`. The dep-map is the consumed-by-many shared structure both agents read/write.
- Roughed-in entries are permitted as draft options before downstream lowering uses them; they get unified, rewritten, formalized, or pruned as semantics firm up.
[new]: | Operator | Signature | Dependencies | Lowers to | Status |
|---|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | Form A: `OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs })`. Form B (first-iteration-unrolled): `first_step :: OpParams -> Krylov -> (SimState -> Solve { sim, krylov, carry, outputs })` and `steady_step :: OpParams -> Krylov -> (PrevCarry -> SimState -> Solve { sim, krylov, carry, outputs })`. | Concepts: `state-stratification`, `solve-monad`, `first-iteration-unrolling`, `derived-view-hoisting`, `convergence-test`, `variant-absorption`. L4 rows: [`iterate-while`](./iterate-while.md) (Form A body), [`iterate-while-with-prev`](./iterate-while-with-prev.md) (Form B body). | L2 [`krylov-step`](../L2/krylov-step.md) via [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) (L4>L3 firm — promoted cycle-008 wave-1 lifter; L3>L2 identity-in-form per the combinator-miner cycle-002 assertion). | `firm` (harvested cycle-006; promoted from cross-layer-cross-cutter recommendation 2026-05-27T025354Z; lowering target firmed cycle-008 wave-1) |
| [`iterate-while`](./iterate-while.md) | Pure: `α -> (α -> Bool) -> (α -> { state: α, ...e }) -> { final_state: α, trajectory: [{ ...e }] }`. Solve-threaded: `α -> (α -> Bool) -> (α -> Solve { state: α, ...e }) -> Solve { final_state, trajectory }`. Sugar: `iterate_while_pure :: α -> (α -> Bool) -> (α -> α) -> α`. | Concepts: `solve-monad`, `derived-view-hoisting`, `convergence-test`. L4 rows: consumed by [`krylov-step`](./krylov-step.md) Form A; companion of [`iterate-while-with-prev`](./iterate-while-with-prev.md). | L3 tail-recursive value-threading form via the body of [`krylov-step-typed-wrapper-dissolution` §"What the L3 form for iterate_while looks like"](../L4-L3/krylov-step-typed-wrapper-dissolution.md#what-the-l3-form-for-iterate_while-looks-like); standalone L4>L3 theme pending per OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`. The GMRES-specific re-rendering of `inner_loop` via this combinator is [`gmres-inner-loop-iterate-while-migration`](../L4-L3/gmres-inner-loop-iterate-while-migration.md) *(rough-in; landed cycle-008 wave-2)*. | `firm` (harvested cycle-007T160550Z; closes cycle-006 OQ `iterate-while-l4-anchor-missing`) |
| [`iterate-while-with-prev`](./iterate-while-with-prev.md) | Pure: `(α -> { state: α, prev: β, ...e }) -> α -> ((α, β) -> { state: α, prev: β, ...e }) -> (α -> Bool) -> { final_state, trajectory }`. Solve-threaded form lifts the step bodies through `Solve`. Degenerates to [`iterate-while`](./iterate-while.md) when `β = ()` (Law 1). | Concepts: `first-iteration-unrolling`, `derived-view-hoisting`, `solve-monad`. L4 rows: [`iterate-while`](./iterate-while.md) (companion / degenerate case); consumed by [`krylov-step`](./krylov-step.md) Form B. | L3 bootstrap-then-tail-recursive form via the body of [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) (parallel to `iterate-while`'s lowering with the additional `prev` positional dissolution); standalone follow-up pending per OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`. | `firm` (harvested cycle-007T160550Z; closes cycle-006 OQ `iterate-while-l4-anchor-missing`) |

Format expected for each entry:
- **Operator** slug (e.g., `solve`, `arnoldi_step`, `apply_preconditioner`) — linked to the operator page.
- **Signature** with shape contracts.
- **Dependencies** — intra-L4 concept-page references + L4-row siblings consumed by this operator.
- **Lowers to** — cross-layer L4>L3 theme references (firm or rough-in) and the downstream L3>L2 hop where known.
- **Status**: `rough-in` | `firm` | `deprecated` (with provenance: harvest cycle, promotion source if any).

(Algebraic laws are recorded inline in each operator's own page, not enumerated in this dep-map.)

## Working Notes

- This page is generated by `layer-intro-author`; operators are authored by `harvester`. The dep-map is the consumed-by-many shared structure both agents read/write.
- Roughed-in entries are permitted as draft options before downstream lowering uses them; they get unified, rewritten, formalized, or pruned as semantics firm up.
- The dep-map's `Dependencies` column records **intra-L4** edges (concept-page references + L4-row siblings); the `Lowers to` column records the cross-layer L4>L3 theme references. The two columns were split in this dispatch (cycle-008) once the L4>L3 theme inventory grew beyond a single in-line annotation per row.
- L4 strawman authority: [`../design/l4_calculus.md`](../design/l4_calculus.md) is in-management for L4 work (per CLAUDE.md "L4 strawman is in-management"). New L4 operator entries cite the strawman's relevant section (BNF, reduction rules, demand-pruning); they do not displace it.
```

## Supporting evidence

### Operators currently harvested at L4 (with slugs)

- [`krylov-step`](../../book/src/L4/krylov-step.md) — cycle-006 firm (harvester `2026-05-27T080944Z`). Signature `OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs })` (Form A) and the Form B `(first_step, steady_step)` split.
- [`iterate-while`](../../book/src/L4/iterate-while.md) — cycle-007 firm (harvester `2026-05-27T160550Z`). Closes cycle-006 OQ `iterate-while-l4-anchor-missing` (jointly with the companion).
- [`iterate-while-with-prev`](../../book/src/L4/iterate-while-with-prev.md) — cycle-007 firm (same dispatch). Bootstrap-carry variant; closes the same OQ.

### Cross-references to adjacent layers

- L4>L3 firm theme: [`krylov-step-typed-wrapper-dissolution`](../../book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md) — cycle-006 abstractor; cycle-008 wave-1 lifter promoted to firm.
- L4>L3 rough-in theme: [`gmres-inner-loop-iterate-while-migration`](../../book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md) — cycle-008 wave-2 abstractor.
- L2: [`krylov-step`](../../book/src/L2/krylov-step.md) — cycle-005 firm; the L4 entry's `Lowers to` resolves here via the L4>L3 firm theme + identity-in-form L3>L2 hop.

### L1 Vocabulary-cohort precedent

`book/src/L1/index.md:27-47` — cycle-004 introduction of the **Vocabulary cohort** subsection; pattern reproduced here for the L4 cohort (firm split into "Firm at L4" with three entries; L4>L3 themes called out separately; no obstruction-themed rough-in operators at L4 currently — the cohort is fully firm at the operator level).

### Strawman authority

`book/src/design/l4_calculus.md` is the canonical reference for L4 calculus conventions per the CLAUDE.md "L4 strawman is in-management" + "L4/L3 pseudo-language is Haskell + TypeScript" invariants (user directive 2026-05-27, mid-cycle-006). The intro's refreshed Semantics overlay cites the strawman §1 (grammar), §3.7 (`iterate_while` small-step rule), and §3.8 (demand-pruning) as the operator entries' load-bearing references — not as displacements.

### Closes

- `l4-layer-intro-refresh-unblocked-by-first-firm-row` (cycle-006, opened by harvester; expanded per cycle-007 integrator-signals to include the Vocabulary cohort subsection). Status flip to `answered` proposed; answer is this dispatch's CYCLE.md.

## Open questions / caveats

1. **`solve-monad` / `restart_cycle` not yet L4-rowed.** The Semantics overlay calls out `solve-monad`'s `restart_cycle` and `solve_loop` outer drivers as the consumers of the firm operator cohort, but no L4 row has been promoted for them. They live as concept-page references (`book/src/concepts/solve-monad.md`). A future cycle-009+ harvester dispatch could promote `solve_loop` to an L4 row (signature: `OpParams -> SimState -> Solve SolveResult` where the body folds `restart_cycle` over an outer `iterate_while`). Not blocking the cohort framing in this dispatch — flagged for the cycle-009 planner. Suggested slug: `l4-solve-loop-harvest-candidate`.

2. **Vocabulary cohort kept despite skip-eligibility; middle subsection re-purposed for L4>L3 cross-layer themes.** Two related template-shape adaptations relative to the role spec at `.claude/agents/layer-intro-author.md:103` ("Skip the subsection when the layer has only firm entries (no queue) or only rough-ins (no firm cohort)") and the L1 precedent at `book/src/L1/index.md:27-47`:
   - **(a) Subsection retained despite firm-only operator cohort.** All three L4 operators are firm; per strict reading of the role spec the entire Vocabulary cohort subsection is skip-eligible. This dispatch keeps it (with `Queued at L4 — none currently` placeholder) to give cycle-009+ planners an obvious slot for new L4 operators (e.g., the `solve_loop` candidate above) and to keep format aligned with the L1 precedent. Defensible to drop it if the integrator prefers the minimal form.
   - **(b) Middle subsection used for L4>L3 cross-layer themes, not rough-in same-layer operators.** The L1 precedent uses the middle slot for rough-in operators at the same layer (e.g., the L1 `nrm2_B` queued case). L4 currently has no rough-in operators — only firm operators plus firm/rough-in cross-layer L4>L3 themes — so this dispatch re-purposes the middle slot for the L4>L3 theme inventory (`krylov-step-typed-wrapper-dissolution` firm + `gmres-inner-loop-iterate-while-migration` rough-in). This is a layer-N-specific adaptation that the role spec does not anticipate; the cross-layer themes are genuinely the "vocabulary in motion at this layer" answer for L4, since they are the consumed-by-L3 surface. Defer to integrator preference on whether to keep the adaptation, drop the middle subsection (collapsing to firm + queued only), or promote it to the role-spec template if precedent-setting is desired. Suggested slug if precedent-setting: `vocabulary-cohort-middle-slot-cross-layer-adaptation`.

3. **The dep-map split (`Dependencies` + `Lowers to` columns) is new in this dispatch.** Previously the L4 dep-map encoded "Lowers to" prose inline in the `Dependencies` cell (visible in the existing `krylov-step` row's first sentence). With three firm operators, the inline annotation is harder to scan, so this dispatch promotes "Lowers to" to its own column. The change is structural / cosmetic — no operator content changes; all three firm rows already named their L4>L3 lowering inline. The L1 / L2 / L3 dep-maps do not currently have a `Lowers to` column; if the integrator wants consistency, the same column split could be back-applied. Routes to cycle-009 planner if consistency wins; flagged here for visibility. Suggested slug: `dep-map-lowers-to-column-back-application`.

4. **L4>L3 theme `gmres-inner-loop-iterate-while-migration` is rough-in pending upstream `gmres.md` v0.7 self-rotation.** The dep-map's `iterate-while` row's `Lowers to` cell references this theme; the theme is rough-in (not firm). Per the role-spec discipline, rough-in cross-references in the `Lowers to` column should use plain-text names when the anchor file does not yet exist — but this theme's anchor file **does** exist (`book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md`, cycle-008 wave-2 landed), so the link form is permitted. The "rough-in" annotation in the prose makes the firmness clear to the reader; the link itself does not require defanging. Cycle-006 friction-ledger entry `rough-in-rows-must-be-plain-text-when-anchor-missing` applies only when the anchor file is missing, which is not the case here.
