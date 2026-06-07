---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-07T153702Z
scope: L1↔L2 cross-cut — matrix-free `D`-stage typing drift between the L2 combinator and its firm `quad_point_contract` substrate op
status: integrated
integrated_at: 2026-06-07T180000Z
integration_commit: acf65f6
integration_notes: "Applied clean (D3). Surgical L2 inline-annotation faithful-render realign at matrix-free-operator-apply.md:79 (quad_point_contract: drop run-time Q pre-multiplied into geom at build; output axis C->C', C'=C symmetric case). Pure inline prose in an already-firm chapter, no rank/edge change. The same drift D3 FLAGGED in D2's theme :168 (do-NOT-expand-into-D2 dispatch boundary) was applied by finalize as a within-finalize consistency fix. cargo make book EXIT 0. No OQ."
---

# CYCLE: Cross-layer observation — matrix-free-D-stage-typing-drift

## Summary

I audited the element-local rank-tensor shape-group congruence across the matrix-free / element-local
layer (L4 cap → L2 `matrix-free-operator-apply` combinator → L1 substrate ops `element_restrict` /
`basis_apply` / `quad_point_contract` / `geom_factor_build` → `concepts/element-local-tensor` →
`semantics/index.md` §1.2.3). **The named-shape-group apparatus is congruence-complete and the semantic
surface is fully consolidated:** §1.2.3 already names the element-local family as *concrete named axes of
fixed meaning* (`E`/`L`/`P`/`C`/`G`), distinct from congruence shape groups `(S: ...)`/`$S`, with
`concepts/element-local-tensor` as the authoritative definition home; the substrate ops correctly USE+LINK
the surface and do NOT restate it; the flat global axis `N` is consistently the rank-1 `Tensor[(N: ...)]`
spelling per §1.2.1. **No new shape-group rule needs relocation** — the geometry-factor `[(E,P,G)]` stratum
is already named on the surface and defined in the record page. **But I found ONE concrete consistency
drift:** the L2 combinator's *inline* `D`-stage type annotation (`matrix-free-operator-apply.md:79`)
disagrees with its own firm `quad_point_contract` substrate op's chapter signature
(`quad_point_contract.md:55`) on two coupled points — the `Q` (coefficient) arity and the input/output
component axis (`C` vs `C'`). L0 (`integrator.cpp:451-495`) confirms the *substrate chapter* is faithful
and the *combinator's inline annotation* is the drift.

## Observation kind

**Consistency drift** — a firm L1 operator's signature (`quad_point_contract`'s `D :: GeomData ->
Tensor[(E,P,C)] -> Tensor[(E,P,C')]`) is rendered with a *different* type by the L2 combinator
(`matrix-free-operator-apply`) that composes it BY NAME, and the combinator's rendering is the inaccurate
one. (Not a vocabulary mismatch — both nodes exist and are firm; not an edge-label mismatch — the
`depends-on (composes)` edge is correct; not a missing shape-group rule — the surface is congruence-complete.)

## Specific finding

The L2 combinator `matrix-free-operator-apply` writes its `D` (`quad_point_contract`) stage in the
contraction-chain pipe (`book/src/L2/matrix-free-operator-apply.md:79`) as:

```
|> quad_point_contract geom Q         -- D   :: [E, P, C] -> [E, P, C]  (pointwise, against [E, P, G])
```

The firm substrate op's own chapter signature (`book/src/L1/quad_point_contract.md:55-59`) is:

```
quad_point_contract :: GeomData -> Tensor[(E, P, C)] -> Tensor[(E, P, C')]
    --   C = trial value/derivative components;  C' = test components (often = C)
    --   GeomData :: Tensor[(E, P, G)]   the per-quad-point precomputed factor (G = geom-data components)
```

Two coupled drifts:

1. **`Q`-arity drift (the load-bearing one).** The combinator passes `quad_point_contract geom Q` — a
   *separate run-time coefficient argument `Q`*. But `quad_point_contract.md:61-65` and
   `geom_factor_build.md:66-68` both state explicitly that the material coefficient `Q` is **pre-multiplied
   into `geom_data` at build time** (the setup stratum), so the run-time apply is *a single pointwise
   multiply* `geom_data ⊙ (basis-evaluated trial)` with **no separate `Q` argument**. The substrate
   signature `D :: GeomData -> Tensor[(E,P,C)] -> ...` (one geom arg) is therefore the faithful one; the
   combinator's `quad_point_contract geom Q` (two args, `Q` threaded at run-time) contradicts the
   pre-multiply build/run-stratum semantics that BOTH substrate chapters carry. (The combinator's own
   `mk-operator` build-stratum prose at `:84-89` is correct — `geom` is the build carrier — so the drift is
   purely in the inline `apply`-chain annotation, which leaks `Q` into the run stratum.)

2. **`C` vs `C'` component-axis drift.** The substrate signature outputs `Tensor[(E,P,C')]` (test
   components, "often = C" but not pinned). `concepts/element-local-tensor.md:127` mirrors this faithfully
   (`D :: GeomData -> Tensor[(E,P,C)] -> Tensor[(E,P,C')]`). The combinator pins the `D` output to `C` (no
   `C'`), and the following `B_𝒟ᵀ` stage (`:80`) consumes `[E,P,C]`. L0 shows trial and test modes are
   *separately keyed* — `AddQFunctionActiveInputs(info.trial_ops, ...)` vs
   `AddQFunctionActiveOutputs(info.test_ops, ...)` (`integrator.cpp:468-469`) — so the trial-side input
   component axis and the test-side output component axis are genuinely-potentially-distinct; pinning them
   equal in the combinator is a (minor) loss of the substrate op's faithful generality.

**L0 adjudication (codemap `read_range integrator.cpp:451-495`):** the apply-QFunction has exactly TWO
inputs feeding the pointwise stage — `"geom_data"` (`CEED_EVAL_NONE`, the build carrier with `Q`
pre-multiplied) and the active trial field (`AddQFunctionActiveInputs(info.trial_ops, ...)`). There is **no
separate `Q` run-time input** to the apply QFunction. And the active inputs (`trial_ops`) and active outputs
(`test_ops`) are keyed by *distinct* `EvalMode` masks. This confirms drift-(1): the substrate chapter's
one-geom-arg signature is faithful; the combinator's `geom Q` is wrong. It confirms drift-(2): `C`
(trial-in) and `C'` (test-out) are structurally distinct axes; the substrate `[E,P,C] -> [E,P,C']` is
faithful.

The drift is small in blast radius (an inline pipe annotation inside one firm L2 chapter, not a frontmatter
edge or a propagated signature), but it is exactly the kind of substrate↔combinator congruence drift this
audit is for: the combinator's *named composition* should render its substrate ops' shapes faithfully, since
the whole point of the cohort is that the L2 form IS the named composition of those exact verbs.

## Recommendation

**Dispatch a lifter (or a small layer-intro-author touch) to re-align the L2 combinator's inline `D`-stage
annotation to its firm substrate signature** — a surgical, single-chapter edit to
`book/src/L2/matrix-free-operator-apply.md:79`:

- change `quad_point_contract geom Q` → `quad_point_contract geom` (drop the run-time `Q`; `Q` is
  pre-multiplied into `geom` at the `mk-operator` build stratum, consistent with `:84-89` and the substrate
  chapters);
- change the `D :: [E, P, C] -> [E, P, C]` comment → `D :: [E, P, C] -> [E, P, C']` to match the substrate
  signature's faithful trial-in / test-out component distinction (and, if desired, a half-line note that
  `C' = C` for the symmetric trial==test case the combinator's symmetry law `:113-122` already assumes).

This is a **proposed-changes block** (below) for `integrator-per-report` to apply in Phase 5 — I do not edit
`book/` myself. It is NOT a relocation-to-the-surface (the surface is already consolidated and correct) and
NOT a harvester/combinator-miner follow-up (no new vocabulary, no new shape group). It is a faithful-render
re-alignment of one combinator's inline substrate-op typing.

Lower-priority / optional: nothing for the geometry-factor `[(E,P,G)]` stratum itself — it is
congruence-complete (defined on the surface §1.2.3 + the record page, produced by `geom_factor_build`,
consumed by `quad_point_contract` and the combinator, all congruent).

## Proposed-changes block

```proposed-changes
file: book/src/L2/matrix-free-operator-apply.md
edit-kind: surgical-realign (single inline annotation; faithful-render to firm substrate signature)

OLD (line ~79, inside the `apply A x` contraction pipe):
            |> quad_point_contract geom Q         -- D   :: [E, P, C] -> [E, P, C]  (pointwise, against [E, P, G])

NEW:
            |> quad_point_contract geom           -- D   :: [E, P, C] -> [E, P, C'] (pointwise, against [E, P, G]; C' = test components, = C in the symmetric trial==test case)

RATIONALE: aligns the L2 combinator's inline rendering of its firm `quad_point_contract` substrate op
(`book/src/L1/quad_point_contract.md:55`, `D :: GeomData -> Tensor[(E,P,C)] -> Tensor[(E,P,C')]`) with the
substrate signature. (1) `Q` is pre-multiplied into `geom_data` at the build stratum
(`quad_point_contract.md:61-65`, `geom_factor_build.md:66-68`), so there is no separate run-time `Q`
argument — confirmed at L0: the apply-QFunction has only `geom_data` + the active trial field, no `Q` input
(`integrator.cpp:451-469`). (2) The `D` output component axis is `C'` (test components), distinct from the
`C` (trial) input — L0 keys `trial_ops` (inputs) and `test_ops` (outputs) separately
(`integrator.cpp:468-469`). The combinator's `mk-operator` build-stratum prose (`:84-89`) already treats
`geom` as the build carrier correctly; only the inline `apply`-chain annotation drifted (leaked `Q` into the
run stratum, pinned `C'=C`).

NOTE: this is the ONLY change; the frontmatter `depends-on (composes)` edge to `quad_point_contract` is
correct and unchanged; no shape-group rule relocates (the semantic surface §1.2.3 is congruence-complete).
```

## Supporting evidence

- `book/src/L2/matrix-free-operator-apply.md:70-89` — the L2 combinator's `apply A x` contraction pipe;
  `:79` is the drifting `quad_point_contract geom Q -- D :: [E,P,C] -> [E,P,C]` annotation; `:84-89` is the
  (correct) `mk-operator` build-stratum prose treating `geom` as the build carrier.
- `book/src/L1/quad_point_contract.md:55-65` — the firm substrate signature
  `D :: GeomData -> Tensor[(E,P,C)] -> Tensor[(E,P,C')]` (one geom arg; `C'` output) + the `Q`-pre-multiplied
  prose; `:107-121` Related/element-local-tensor links.
- `book/src/L1/geom_factor_build.md:54-68` — `geom_factor_build :: MeshNodes -> QuadWeights ->
  Tensor[(E,P,G)]`; `:66-68` "Palace pre-multiplies the material coefficient `Q` into this same `geom_data`
  … so the run-time `D` apply is a single pointwise multiply" (the build/run-stratum fact the combinator
  drifts from).
- `book/src/concepts/element-local-tensor.md:74-78` (the three rank-tensors), `:97` (`[E,P,G]` wholly
  build-stratum), `:126-128` (the faithful `D :: GeomData -> Tensor[(E,P,C)] -> Tensor[(E,P,C')]` mirror) —
  the record-definition home; congruence-complete, agrees with the substrate op, NOT with the combinator.
- `book/src/semantics/index.md` §1.2.3 (`:97-101`) — the consolidated convention: the element-local family
  is *concrete named axes of fixed meaning*, NOT congruence groups; `concepts/element-local-tensor` is the
  authoritative definition home; the flat `N` stays rank-1 `Tensor[(N: ...)]`. Fully consolidated — nothing
  to relocate.
- `reference/palace/palace/fem/libceed/integrator.cpp:451-495` (codemap `read_range`, this dispatch) — the
  apply-QFunction inputs: only `"geom_data"` (`CEED_EVAL_NONE`, `:455-456`) + the active trial field
  (`AddQFunctionActiveInputs(info.trial_ops, …)`, `:468`); active outputs keyed by `info.test_ops`
  separately (`AddQFunctionActiveOutputs(…)`, `:469`). Confirms: no run-time `Q` input (drift-1 adjudicated);
  trial/test component axes distinct (drift-2 adjudicated).

## Open questions / caveats

- **Single-chapter, low blast radius.** The drift is confined to ONE inline annotation in a firm L2 chapter;
  it does not propagate to a frontmatter edge, a dep-map row, or any other chapter. The realign is surgical
  and does not change the combinator's rank, status, edges, or any law. (The symmetry law `:113-122` already
  assumes `trial==test`, where `C'=C`, so the `C'` correction is consistent with the existing prose, not in
  tension with it.)
- **`C'=C` for the common symmetric case.** The substrate chapter notes `C'` "often = C". The combinator's
  pinning `C` is not *wrong* for the symmetric trial==test operators that dominate (mass / grad-grad SPD
  terms); it is a loss of the substrate op's faithful generality (the non-self-adjoint coefficient case the
  combinator's own law-3 already contemplates). The proposed `C'` + "= C in the symmetric case" note keeps
  both readings.
- **No RE11 / reachability interaction.** This observation does not touch the RE11 grounding question (D1/D2
  build that); the combinator is already firm and root-reaching via the `fe_assemble` fold's feature-column
  inbound edges. The realign neither helps nor hinders RE11.
- **Verify before applying:** confirm the `:79` line still reads `quad_point_contract geom Q` at integrate
  time (D2 this cycle authors a new L4>L3 dissolution theme that may *also* render this chain — if D2's theme
  introduces the same drift in its RHS, the integrator should align D2's rendering to the substrate signature
  too; flagged for the finalize / critic pass on D2). The proposed-changes block targets only the L2
  combinator file (D3 owns no D2 region).
