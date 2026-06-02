---
name: disciplined-cross-pipeline-combinator-mining-gate
verb: gate a cross-pipeline combinator mine behind a ≥2-witness bar + scope-boundary classification of break-witnesses + fold-vs-map over-unification check
owners: [combinator-miner, cross-layer-cross-cutter]
promoted: cycle-054 (batch-16 meta-phase)
companions: [propose-rotation, verify-rotation-citation]
---

# disciplined-cross-pipeline-combinator-mining-gate

**When to invoke.** A `combinator-miner` (or a `cross-layer-cross-cutter` probing for one) is about to propose a combinator that abstracts a shape recurring **across solver pipelines** (electrostatic / magnetostatic / eigenmode / driven / transient) or across any family of independently-witnessed call sites. This is the disciplined-mining gate the solver-test-load frontier runs on: the single-witness → 2nd-pipeline-probe → discharge → mine sequence. Invoke it before authoring the combinator entry/row, and cite it so the critic's `skill-uptake-survey` can mark `pass` rather than `warning`.

**Why it exists.** Under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, solvers are a LOW-PRIORITY test-load that advances a layer **only when cleanly describable in existing shared vocabulary** — and a combinator mined from ONE pipeline witness, then authored as if cross-pipeline-general, is exactly the mine-and-strand / over-unification failure the redirect forbids. The batch-16 arc ran this gate end-to-end correctly without it being a named skill: c052 D6 surfaced the electrostatic outer-solve-sweep as single-witness (load-bearing caveat: generality UNVERIFIED); c053 D1 probed magnetostatic as a 2nd witness and DISCHARGED the gate (2-of-N, skeleton-identical); c054 D1 mined the fixed-operator `solve_family` combinator, classified the driven-solver break (`SetOperators` inside the loop) as a SCOPE BOUNDARY (a `map_solve_over_(operator,rhs)_family` superset, NOT a variant axis), and flagged transient as an unprobed fold-vs-map hazard. The discipline was exemplary; the critic could only mark `skill-uptake-survey: warning` ("procedure followed, no skill cited"). This skill encodes it so the procedure is invocable and citable.

## Procedure

Before proposing a cross-pipeline combinator:

1. **≥2 positive witnesses, structurally identical at the load-bearing shape.** Confirm at least two pipelines exhibit the shape, and that the differences between them are **leaf-content, not structural** (e.g. curl-curl vs diffusion integrator, surface-current vs terminal excitation, `Mult` vs `AddMult` field recovery are leaf differences; the assemble-once / map-over-family / collect skeleton is the structure). Codemap-verify each pinpoint (`mcp__palace-codemap__read_range` / `get_call_sites`). A single witness is a SPINE-COVERAGE FINDING, not a mineable combinator — record it with an explicit single-witness caveat and route a 2nd-pipeline probe; do NOT author from it.

2. **Classify every negative / break witness as a SCOPE BOUNDARY, never a variant axis.** A pipeline that breaks the load-bearing structural invariant (e.g. the driven solver rebuilds its operator per family-element, breaking shared-operator capture) defines a **distinct combinator or a superset** of the mined one — the mined combinator is the specialization; the break-witness rides the superset. Do NOT silently fold a break-witness into a variant axis of the mined combinator (that asserts a generality the source contradicts).

3. **Name every unprobed pipeline as DEFERRED, with the fold-vs-map over-unification flag.** Do not implicitly claim coverage of pipelines you have not read. For each deferred pipeline, flag the load-bearing hazard: **is the unprobed shape a `map` (each element independent — `solve_family`-shaped) or a `fold` (state threaded between elements — `solve_loop` / `iterate_while`-shaped)?** Transient time-stepping is the canonical fold risk (step `n`'s solution feeds step `n+1`). Folding a fold into a map silently asserts an independence/commutativity (the concatenation-homomorphism law) that does not hold — the general-form promotion MUST clear this check first.

4. **Replace-and-propagate, not mine-and-strand.** The combinator is the ENTRY; the witnesses become specialization leaves that re-express *through* it (the redirect's combinator-as-entry model). Pick + justify the layer (a cross-pipeline outer-driver typically lands at L4 outer-driver vocabulary, above the per-solve cap). State the propagation plan even if the leaf-entries land in a follow-on cycle.

## Output

The miner: a proposal that records (1) the ≥2 codemap-verified positive witnesses, (2) each break-witness with its scope-boundary classification, (3) each deferred pipeline with its map-vs-fold flag, (4) the layer choice + propagation plan. Cite this skill so the critic marks `skill-uptake-survey: pass`.

The critic: `skill-uptake-survey: pass` when the report cites this gate and the four points are present; `warning` when the discipline is present but uncited; a `rotation-quality` / `variant-axis-coverage` finding when a break-witness was folded into a variant axis (step 2 violation) or an unprobed fold was claimed as a map (step 3 violation).

Companion to `propose-rotation` / `verify-rotation-citation` (the combinator's abstraction-over-the-lower-layer rotation).
