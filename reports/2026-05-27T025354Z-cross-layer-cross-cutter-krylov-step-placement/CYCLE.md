---
agent: cross-layer-cross-cutter
invoked_at: 2026-05-27T02:53:54Z
scope: L2↔L4 cross-cut — krylov-step-layer-placement
status: integrated
integrated_at: 2026-05-27T07:04:24Z
integration_commit: a16c32c76f7ed73c2ab1d381d440db2cd6b2e7f9
integration_notes: Applied (observation-only; OQ-only). Recommends DUAL placement for krylov-step (L2 + L4 with L4>L3>L2 lowering edge). 4 OQs promoted naming 3 cycle-006 follow-up dispatches.
skill_uptake:
  verify-citation-range: informal — spot-checked the four concept line-ranges (solve-monad.md:14, state-stratification.md:11, first-iteration-unrolling.md:21-37, L2/index.md:21-23, L4/index.md:26-37) by direct file inspection but did not invoke the skill by name.
  classify-variant-axis: not-applicable — no new variant axes authored; variant absorption is inherited from the L2 rough-in and named by reference, not classified here.
  cross-cut-comparison: informal — pattern-instance comparison across the five slices was done by hand following the combinator-miner CYCLE.md Pattern-instances list; no formalized skill exists yet for this cross-cutter shape.
---

# REPORT: Cross-layer observation — `krylov-step` layer placement (L2 vs L4 vs both)

## Summary

The cycle-002 combinator-miner landed `krylov-step` as a `rough-in` at **L2 only** (`book/src/L2/index.md:23`), and explicitly flagged the layer-placement question for cross-layer scrutiny (combinator-miner CYCLE.md §"Open questions / caveats" item 1: "My read: L2 captures primitive composition, L4 captures typed wrapping; complementary"). Comparing the L2 entry against L4's existing concept vocabulary (`solve-monad`, `state-stratification`, `first-iteration-unrolling`, `iterate_while`, `derived-view-hoisting`) and against the five pattern instances, the two readings address **genuinely distinct aspects** — L2 names the primitive-composition shape, L4 names the typed wrapper that `iterate_while` + `solve-monad` consume. They are not interchangeable, and an L2-only stance leaves L4 without a named slot for the kernel role it already references in prose (e.g., `solve-monad.md:14`, `state-stratification.md:11`, `first-iteration-unrolling.md:21-37` all refer to "step" / `step` / `steady_step` without a vocabulary entry). The "duals OK if genuinely distinct" pattern (MEMORY: multi-formulation exploration) applies — both, with a lowering edge.

## Observation kind

**Coverage gap** — L4 needs a `krylov-step` entry to give the prose in `solve-monad.md`, `state-stratification.md`, `first-iteration-unrolling.md` a vocabulary anchor; absent that, L4's existing concepts ride on an unnamed "step" everywhere and the L2 rough-in cannot be cleanly lowered into. Equivalently: L2 has the algebraic-composition entry, L4 has the typed-wrapper hole.

## Specific finding

Three concrete pieces of evidence that L4 needs its own `krylov-step` entry distinct from L2's:

1. **Existing L4 concepts already name the role.** `book/src/concepts/solve-monad.md:14` writes `restart_cycle op inp` whose body is implicitly a fold over a step. `book/src/concepts/first-iteration-unrolling.md:21-23` gives two function signatures (`first_step`, `steady_step`) that are the L4 typed-wrapper shape of `krylov-step` — these signatures pre-exist as concept prose but have no dep-map entry. `book/src/concepts/state-stratification.md:11` similarly references step-local ephemeral state. The L2 entry's primitive-composition signature `(op_params, iter_state) -> {state, outputs}` is **not** the same thing as the L4 typed signature `first_step :: ... -> State -> StepResult` / `steady_step :: ... -> PrevCarry -> State -> StepResult` from first-iteration-unrolling.md — the L4 form carries the `PrevCarry` closure-vs-state distinction explicitly, the L2 form does not.

2. **The five pattern instances each split L2↔L4 internally.** Per combinator-miner CYCLE.md "Pattern instances": every cited slice provides **both** an L2 form (cg.md:103-115, gmres.md primitive-sequence sites, chebyshev.md:354-362, arnoldi_step.md:99-105, polynomial_recurrence_step.md:119-160) **and** an L4 form (cg.md:172-188, cg.md:393-425, gmres.md:459-471, arnoldi_step.md:285-298). Naming the combinator only at L2 conflates two slice sections that the slice authors deliberately separated. L4 form is a typed wrapper of L2 form, not a synonym.

3. **No lowering theme exists yet.** The L4>L3 and L3>L2 lowering Parts (`book/src/L4-L3/index.md`, `book/src/L3-L2/index.md`) have no entry that takes an L4 `krylov-step` to its L2 form. This is a coverage gap on the lowering side as well — if both layers carry the entry, the rotation between them (typed-wrapper → primitive-composition) is itself a nameable theme (likely "state-monad threading collapses to value-threaded primitive composition" at L4>L3, then identity-in-form at L3>L2 per combinator-miner's own observation that the L2→L3 rotation on the body is identity-in-form).

## Recommendation

**Dual-with-edge.** `krylov-step` belongs at **both L2 and L4**, with a lowering edge.

- **L2 `krylov-step`** (already roughed in): primitive-composition signature, dependencies on `apply_linop` / `axpy` / `dot` / `nrm2` / etc., variant axes absorbed at construction.
- **L4 `krylov-step`** (new entry needed): typed-wrapper signature in the `state-stratification` (`SimState` / `OpParams` / `Krylov`-ephemeral) idiom, consumed by `iterate_while` / `solve-monad`, with the `first-iteration-unrolling` two-signature split (`first_step` / `steady_step`) named in the entry.
- **Lowering edge**: L4 `krylov-step` (typed wrapper, state-monad threaded) → L3 `krylov-step` (state-threaded as plain values, sequential obstruction surfaced on the outer loop) → L2 `krylov-step` (primitive composition, no state-wrapper). The L3 intermediate is plausibly identity-in-form on the body per the combinator-miner's "the L2→L3 rotation on the body is identity-in-form" remark — so the practically interesting lowering is L4>L3, with L3>L2 being trivial on the kernel itself.

Follow-up routing:

- **Primary**: dispatch `harvester` on `krylov-step @ L4` once the L2 entry firms (i.e., after the parallel cycle-005 harvester landing at L2 in `reports/2026-05-27T025354Z-harvester-krylov-step-L2/`). L4 harvester deliverable: typed signature in state-stratification idiom, dependencies on the L4 concepts (`solve-monad`, `iterate_while`, `state-stratification`, `first-iteration-unrolling`, `derived-view-hoisting`), and a "Lowers to" stub pointing at the L2 `krylov-step` entry.
- **Secondary**: dispatch `abstractor` on the `L4>L3` lowering theme that takes typed-wrapper-with-state-monad → value-threaded form for `krylov-step` (this is the substantive rotation; the rest is identity-in-form).
- **Tertiary** (deferrable): dispatch `layer-intro-author` to add the L4 entry to `book/src/L4/index.md` dep-map and update L4 working notes; can also be done by the L4 harvester as part of the primary task per existing harvester+intro coordination.

## Supporting evidence

- `book/src/L2/index.md:21-23` — current L2 rough-in row (single entry, primitive-composition signature).
- `book/src/L4/index.md:26-37` — L4 dep-map currently empty, awaiting harvester promotion.
- `book/src/concepts/solve-monad.md:1-17` — L4 prose names `solve_loop` with an implicit step-fold; no dep-map anchor.
- `book/src/concepts/state-stratification.md:7-11` — three-way split (`SimState` / `OpParams` / ephemeral `Krylov`) is exactly the L4 typed-wrapper context for `krylov-step`.
- `book/src/concepts/first-iteration-unrolling.md:21-37` — already names `first_step` / `steady_step` signatures; these are the L4 typed-wrapper signatures of `krylov-step` written as prose without a dep-map anchor.
- `reports/2026-05-26T231843Z-combinator-miner-krylov-iteration-step/CYCLE.md` lines 44-46 — combinator-miner's "Not L4" reasoning explicitly punts to cross-layer-cross-cutter ("Cross-layer-cross-cutter should examine whether `krylov-step` deserves L2, L4, or both with a lowering edge").
- Five pattern instances each splitting L2↔L4 in the slice corpus, per combinator-miner Pattern-instances list (cg.md, gmres.md, chebyshev.md, arnoldi_step.md, polynomial_recurrence_step.md citations).
- Parallel-dispatched harvester directory `reports/2026-05-27T025354Z-harvester-krylov-step-L2/` exists; CYCLE.md not yet written at observation time (in-flight).

## Open questions / caveats

1. **Naming reuse vs disambiguation.** Reusing the slug `krylov-step` at both L2 and L4 may invite confusion. Alternatives: `krylov-step-kernel` (L2) + `krylov-step` (L4), or vice versa. Prefer same-slug-different-layer because the lowering edge then names itself (`L4>L3 krylov-step` theme); cross-layer reuse is the norm elsewhere in the spec. Harvester at L4 may rename if friction emerges.

2. **Is L3 really identity-in-form on the body?** Combinator-miner asserts this from cg.md:352-362 and arnoldi_step.md:185-188 but the assertion has not been independently audited. If true, the L4>L2 lowering can be a single theme without an explicit L3 entry. If false, L3 also gets a `krylov-step` row. Defer to L4>L3 abstractor; if the abstractor finds non-identity rotations on the body (e.g., the `Krylov` ephemeral bundle dissolves on the way to L3), an L3 entry would also be warranted.

3. **Is `state-stratification` an L4 concept or an L4 row?** Currently it lives only as a concept under `book/src/concepts/`. If `krylov-step @ L4` is the first L4 dep-map entry, the L4 layer-intro-author may also need to add `state-stratification`, `iterate_while`, `solve-monad` as L4 rows simultaneously to give `krylov-step @ L4` something to depend on. Worth flagging to the L4 harvester (or, if too coarse, a `layer-intro-author` dispatch on L4 first).

4. **Promotion timing.** The L2 `krylov-step` rough-in is being firmed in this same cycle (parallel harvester dispatch). L4 entry should wait until L2 firms — otherwise the L4 typed-wrapper is anchored to a moving target. Sequencing: cycle-005 firms L2; next cycle (or later in this one if the parallel harvester lands fast) opens L4 `krylov-step`.

5. **Single-observation discipline.** The L4>L3 lowering theme is a separate observation (coverage gap on the lowering Part) — this report focuses solely on the layer-placement question. The lowering-theme coverage gap is flagged in the recommendation as secondary follow-up rather than as a bundled observation.
