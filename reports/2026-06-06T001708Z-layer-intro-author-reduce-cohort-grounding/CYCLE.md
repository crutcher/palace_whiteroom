---
agent: layer-intro-author
invoked_at: 2026-06-06T001708Z
scope: cycle-110 D1 — reduce/orthogonalize/chebyshev cohort GROUNDING pass (batch-35 LEAD, the c109 Group-B next tranche)
status: pending
integrated_at: 2026-06-06T013000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied clean by integrator-per-report (staging row 1/2). Frontmatter-only +3 composes depends-on edges on book/src/L4/krylov-step.md grounding the reduce-to-scalar chain (L4/dot, L4/nrm2, L2/orthogonalize). D1-isolation reachable 107->117; TRUE CUMULATIVE with D2 = 119. rank_violations HELD 0. 4 OQs promoted (reduce-chain RESOLVED-PARTIAL + 3 routed). Build EXIT 0, linkcheck2 clean, no finalize build-repair. Committed in cycle-110 finalize atomic commit.
---

# CYCLE: reduce/orthogonalize/chebyshev cohort grounding (the §(g) GROUND-don't-remove next tranche)

## Summary

The batch-35 LEAD's next, structurally-distinct tranche of OQ
`l2-reduce-orthogonalize-cohort-itself-unreachable-blocks-theme-grounding` (the c109 Group-B
finding). The reduce-to-scalar chain (`inner_product`/`nrm2`/`dot`) is typed correctly DOWNWARD
(L4→L3→L2) but was DEAD AT THE TOP — nothing reachable pointed `depends-on` into
`L4/dot`/`L4/nrm2`/`L4/inner_product`. The faithful fix, applying §(g) GROUND-don't-remove as
**faithful-path-or-finding**: add `composes` `depends-on` edges from the reachable consumer
`L4/krylov-step` (reachable ← `L4/ksp_solve` ← driven/electrostatic/magnetostatic.L4) into the
reduce/orthogonalize verbs its body GENUINELY calls.

**ONE host edit (`L4/krylov-step` frontmatter, +3 `composes` edges) cascades the entire
reduce-to-scalar chain reachable + grounds the orthogonalize leg:**

- **reachable 107 → 117 (+10)** (D1 in isolation) — a single host's three body edges cascade the
  whole reduce chain down to L2.
- **rank_violations HOLDS 0** (the single-number health signal, held across the campaign).
- **STRONGER GARBAGE SIGNAL 34 → 26 (−8)** — the measurable target dropped.
- **detritus 152 → 142 (−10)**; **untyped HELD 60** (frontmatter-only, no new untyped node).

> **Cumulative-vs-isolated note (integrator):** the +10/117 figure is D1's ISOLATED contribution
> (measured apply→lint→revert). The parallel D2 (axpy-family) dispatch lands a disjoint node set, so
> the TRUE CUMULATIVE reachable after BOTH apply is NOT 117 + D2 summed naively — the integrator MUST
> re-measure by running the lint after both edit-sets are applied (the combined count lands near 119,
> but the measured number is the real one; do not sum the deltas).
- **The c109-pre-laid `L2-L1/inner-product-fold-specialization` theme FLIPPED reachable** — exactly
  as predicted (its host `L2/inner_product` grounded, and the edge laid in c109 edit #5 now carries).

**The split exactly matched the planner's FAITHFUL-PATH-OR-FINDING prediction:**
- **GROUNDED (reduce-to-scalar chain + orthogonalize leg):** `L4/dot`, `L4/nrm2`, `L4/inner_product`,
  `L3/dot`, `L3/inner_product`, `L3/nrm2`, `L2/inner_product`, `L2/orthogonalize` all flipped
  reachable; the `inner-product-fold-specialization` theme flipped.
- **DECLINED as an over-edge (faithful-edge-or-finding, the c108 exemplar):** `gram_reduce → L4/inner_product`
  is a **sibling** relationship (algebra-of-folds family), NOT a `composes` — gram_reduce's body
  folds `L1/bilinear-form` + `L1/matrix-weighted-norm` (already `depends-on`), not `L4/inner_product`.
  Flipping it would misclassify a sibling as a constituent. NOT laid — and not needed (the chain
  grounds via krylov-step).
- **ROUTED as a FINDING (chebyshev/jacobi preconditioner leg):** absorbed-below-column — the
  preconditioner is absorbed into `op.T` (`concepts/constructed-operators`), and
  `L4/preconditioning-framework` *consumes* `L4/ksp_solve` rather than being a constituent of it.
  No faithful column→preconditioner edge exists. Baseline-exception recommended (the c107 BC/divfree
  pattern). Do NOT force a column→preconditioner edge.
- **ROUTED (`L2/gram`, `L2/incremental-least-squares`):** `L2/gram` (NLEPS `XᴴX`) is consumed by
  `deflate` (STOP-PROPOSING), NOT by `gram_reduce` (which is the *operator-weighted symmetric-Gram
  over a solution family* — a different op); `L2/incremental-least-squares` (GMRES running-QR) is a
  genuine GMRES constituent but absorbed into the krylov-step body / `ksp_solve materialise_iterate`
  with no separable op-edge at the L4 chapter altitude. Both routed; see Open questions.

All edits are **frontmatter-only** (no prose claims). Verified by applying to `book/`, running the
lint, recording the result, then `git checkout`-reverting (`git status --short book/` empty).

## Faithfulness confirmations (consumer-body prose + L0/chapter citations)

Each `composes` edge was confirmed REAL from the consumer's chapter body before typing:

1. **`L4/krylov-step → L4/dot` (kind: `composes`)** — the body's scalar-stratum reduce verb. The
   Form-B worked CG body literally writes `dot Ap p'`, `dot r' r'` at `book/src/L4/krylov-step.md:142,145`
   (`cg_first_step`) and `:158,161` (`cg_steady_step`). The L4 `inner_product` chapter confirms the
   altitude: `book/src/L4/inner_product.md:44-47` — *"the CG `α`/`β` coefficients … inside
   `krylov-step`'s body are `inner_product` let-bindings"* (and `dot` is the
   `M=I`/Hermitian specialization risen to L4 as the named verb, `book/src/L4/dot.md:18-20`). FAITHFUL.
   **Altitude = L4** (not L1): the L4 chapter's body is written in L4 vocabulary calling `dot`; this
   mirrors `L4/ksp_solve → L4/krylov-step` / `L4/iterate-while` (L4-chapter body edges point at L4 ops,
   `book/src/L4/ksp_solve.md:8-11`). The L2 chapter `L2/krylov-step` separately `depends-on` the L1
   leaves (`L1/dot`/`L1/nrm2`, `book/src/L2/krylov-step.md:18-19`) — that is the L2-altitude statement,
   already on disk; this edit is the complementary L4-altitude statement the L4 chapter was missing.

2. **`L4/krylov-step → L4/nrm2` (kind: `composes`)** — the body's residual-norm readout. The step's
   `outputs` readout is `residual_norm` (`book/src/L4/krylov-step.md:104` `derived_views K' op …
   typically residual_norm`), realized in the Form-B body as `res' = sqrt (abs beta')`
   (`:146,162`) = the Euclidean norm of the residual. `nrm2` is the named consumer verb for exactly
   this (`book/src/L4/nrm2.md:18-20` *"the named unit a Krylov / eigen solver description wants written
   as residual `nrm2(r)`"*). FAITHFUL.

3. **`L4/krylov-step → L2/orthogonalize` (kind: `composes`)** — the optional auxiliary orthogonalize
   stage. The body composes `op.orthog (K.V_prefix, w)` for GMRES/Arnoldi (`book/src/L4/krylov-step.md:94`;
   §Semantics auxiliary stage). `L2/orthogonalize` is explicitly *"the level-(b)-absorbed `op.orthog`
   surface that `krylov-step` folds, and the composition GMRES / FGMRES / Arnoldi / eigenmode-ROM
   basis-extension all consume"* (`book/src/L2/orthogonalize.md:11-13`). FAITHFUL.
   **Altitude = L2** (the deliberate exception): there is NO L4 orthogonalize op (no `L4/orthogonalize`
   chapter), so the genuine constituent edge crosses to the L2 named composition the kernel folds.
   This is the planner-anticipated altitude exception (no L4-level op forces the L2 target).

Well-foundedness over the three new edges: `L4/krylov-step` is firm (rank 3, explicit `rank: firm`);
`L4/dot`/`L4/nrm2` declare `firmness: firm` (no explicit `rank:` line, but the lint reports 0
violations over the new edges either way); `L2/orthogonalize` carries no `rank:` token yet (typed-no-rank), so the `rank(u) ≤ rank(v)`
invariant holds **vacuously** over that edge (a no-rank target cannot register a violation) —
`rank_violations` stays 0 either way. (That `L2/orthogonalize` lacks an `edges:`/`rank:` block is a
lazy-tail typing item, filed below.)

## Proposed changes

Single frontmatter-only edit. The block-mapping edge form (`- target: … / kind: …`) matches the
established scheme (c108 `L2/divfree-projector`, c109 `L2/krylov-step`). Verified to parse cleanly and
to produce the +10 reachability cascade below.

### `book/src/L4/krylov-step.md` — ADD 3 `composes` `depends-on` edges (the reduce/orthogonalize body verbs)

Insert the three edges immediately after the existing `L2/krylov-step` lowers-to edge, before the
`uses-record` block.

```edit:book/src/L4/krylov-step.md
[old]:
    - target: L2/krylov-step
      kind: lowers-to                 # the firm L2 primitive-composition row this L4 typed-wrapper lowers to (via the L4>L3>L2 chain); lowering edge = depends-on on both endpoints (scheme §5)
    - target: concepts/op-params
[new]:
    - target: L2/krylov-step
      kind: lowers-to                 # the firm L2 primitive-composition row this L4 typed-wrapper lowers to (via the L4>L3>L2 chain); lowering edge = depends-on on both endpoints (scheme §5)
    - target: L4/dot
      kind: composes                  # the body's scalar-stratum reduce verb: `dot Ap p'` / `dot r' r'` (§Semantics Form-B :142,:145,:158,:161); the CG α/β coefficients are L4 dot let-bindings (L4/inner_product.md:44-47)
    - target: L4/nrm2
      kind: composes                  # the body's residual-norm readout `res' = sqrt (abs beta')` = nrm2 of the residual (§Semantics :104 derived_views residual_norm; Form-B :146,:162); the Euclidean-norm verb the step's output readout computes
    - target: L2/orthogonalize
      kind: composes                  # the optional auxiliary orthogonalize stage `op.orthog (V_prefix, w)` GMRES/Arnoldi fold (§Semantics :94); no L4 orthogonalize op exists, so the body edge crosses to the L2 named composition the kernel folds (L2/orthogonalize.md:11 "the op.orthog surface krylov-step folds")
    - target: concepts/op-params
```

## Verification (mandatory — applied edit, ran lint, reverted to clean `book/`)

I applied the edit to `book/`, ran `python3 tools/graded-stack-lint/graded_stack_lint.py --show-inbound`,
recorded the result, then `git checkout`-reverted `book/src/L4/krylov-step.md`. Confirmed
`git status --short book/` is empty post-revert (the integrator re-applies from the proposed-changes block).

**Before (baseline, matches planner):**
```
reachable from roots: 107
RANK VIOLATIONS: none.  (rank_violations = 0)
STRONGER GARBAGE SIGNAL: 34
DETRITUS: 152   ;   untyped (WARNING): 60
```

**After (the 3 `composes` edges applied):**
```
reachable from roots: 117          (+10)
RANK VIOLATIONS: none.  (rank_violations = 0)   HELD
STRONGER GARBAGE SIGNAL: 26        (-8)
DETRITUS: 142   (-10)   ;   untyped (WARNING): 60   HELD
```

**The +10 nodes that flipped reachable** (gone from the post-edit garbage lists; confirmed by grep):
`L4/dot`, `L4/nrm2`, `L4/inner_product`, `L3/dot`, `L3/inner_product`, `L3/nrm2`, `L2/inner_product`,
`L2/orthogonalize`, plus the cascade-interior nodes the linter counts (the chain's typed mid-nodes that
were already typed but unreached). **The 8-node STRONGER-GARBAGE drop** is the reduce-to-scalar chain
core (`L4/dot`, `L4/nrm2`, `L4/inner_product`, `L3/dot`, `L3/inner_product`, `L3/nrm2`, `L2/inner_product`)
plus one.

**Per-leg outcome (the FAITHFUL-PATH-OR-FINDING split):**

| leg | edge laid | flipped reachable | disposition |
|---|---|---|---|
| reduce-to-scalar (`dot`/`inner_product`) | `L4/krylov-step → L4/dot` | `L4/dot`,`L4/inner_product`,`L3/dot`,`L3/inner_product`,`L2/inner_product` | **GROUNDED** |
| reduce-to-scalar (`nrm2`) | `L4/krylov-step → L4/nrm2` | `L4/nrm2`,`L3/nrm2` (+ `L4/inner_product` shared) | **GROUNDED** |
| `L2-L1/inner-product-fold-specialization` theme | (none — c109-pre-laid) | flipped via host `L2/inner_product` grounding | **GROUNDED (carried theme)** |
| orthogonalize | `L4/krylov-step → L2/orthogonalize` | `L2/orthogonalize` | **GROUNDED (partial — see note)** |
| `gram_reduce → inner_product` | (declined) | n/a | **DECLINED over-edge (sibling, not composes)** |
| chebyshev/jacobi preconditioner | (none) | — | **ROUTED finding + baseline-exception** |
| `L2/gram`, `L2/incremental-least-squares` | (none) | — | **ROUTED finding** |

**Carried Group-B theme confirmation:** `L2-L1/inner-product-fold-specialization` is GONE from
`[garbage?]` (grep count 0) — the c109 pre-laid edge `L2/inner_product →lowers-to→ theme` now carries
because its host `L2/inner_product` grounded this cycle, exactly the c109-routed expectation. The other 4
Group-B themes (`chebyshev-iteration-fusion`, `gram-fold-specialization`,
`incremental-least-squares-composition-lowering`, `orthogonalize-composition-lowering`) REMAIN `[garbage?]`
(their host L2 ops still off-spine OR untyped — see findings).

**Orthogonalize partial note:** `L2/orthogonalize` flipped reachable, but its theme
`L2-L1/orthogonalize-composition-lowering` did NOT cascade because `L2/orthogonalize` has no typed
`edges:` block (it begins `# orthogonalize`, no frontmatter) — so it carries no typed `lowers-to` edge to
its theme. `L3/orthogonalize` also did NOT flip (it points DOWN to L2; I grounded L2 directly, and
L3/orthogonalize has only legacy `lifts_from`/`lowers_to`, no typed inbound from a reachable node). Both
are lazy-tail typing items (filed below), not grounding failures — the GROUND of `L2/orthogonalize` itself
(the genuine krylov-step constituent) succeeded.

## Supporting evidence

- Reachable consumer chain: `L4/krylov-step ← L3/krylov-step, L4/ksp_solve`; `L4/ksp_solve ←
  feature/{driven,electrostatic,magnetostatic}.L4` (`--show-inbound`); `L4/ksp_solve → L4/krylov-step`
  (folds, `book/src/L4/ksp_solve.md:8-9`).
- Reduce-chain downward typing (pre-existing, confirmed): `L4/dot →specializes→ L4/inner_product` +
  `→ L3/dot` (`book/src/L4/dot.md:5-9`); `L4/nrm2 →depends-on→ {L4/inner_product, L3/nrm2}`
  (`book/src/L4/nrm2.md:5-8`); `L4/inner_product →depends-on→ L3/inner_product`
  (`book/src/L4/inner_product.md:5-7`); `L3/dot →depends-on→ L2/inner_product` (`book/src/L3/dot.md:5-7`);
  `L2/inner_product →lowers-to→ L2-L1/inner-product-fold-specialization` (c109 edit #5,
  `book/src/L2/inner_product.md`).
- Body-verb citations: enumerated in §Faithfulness confirmations above (`krylov-step.md:94,104,142,145,146,158,161,162`).
- c108/c109 grounding precedents: `book/src/L2/divfree-projector.md:11-17` (block-mapping edge form);
  `reports/2026-06-05T234424Z-layer-intro-author-l2-l1-theme-cohort-grounding/CYCLE.md` (the Group-B finding this advances).

## Open questions

### Progress update on the existing OQ (the grounded subset)

```append:scaffolding/open-questions.md

## OQ: reduce-to-scalar-chain-grounded-via-krylov-step-body-composes-edges

- **status:** RESOLVED-PARTIAL — cycle-110 (batch-35 D1, the reduce/orthogonalize/chebyshev cohort
  grounding pass; advances OQ `l2-reduce-orthogonalize-cohort-itself-unreachable-blocks-theme-grounding`).
- **resolution.** The reduce-to-scalar cohort (`L4/dot`/`L4/nrm2`/`L4/inner_product` + their L3/L2 chain)
  was GROUNDED §(g)-style by adding three `composes` `depends-on` edges from the reachable consumer
  `L4/krylov-step` into the reduce/orthogonalize verbs its body genuinely calls
  (`L4/dot`, `L4/nrm2`, `L2/orthogonalize`). One host edit cascades the whole chain: reachable 107→117
  (+10, D1 in isolation; the cumulative count after D2 also lands must be re-measured by the integrator,
  not summed — D1/D2 rescue disjoint sets, combined ≈ 119), STRONGER GARBAGE SIGNAL 34→26 (−8),
  rank_violations HELD 0. The c109-pre-laid
  `L2-L1/inner-product-fold-specialization` theme flipped reachable as its host `L2/inner_product`
  grounded — closing the c109 routed expectation for that one theme.
- **altitude precedent established.** An L4-chapter body-composition edge points at the **L4 reduce verb**
  (the L4 chapter's body is written in L4 vocabulary calling `dot`/`nrm2`), mirroring
  `L4/ksp_solve → L4/krylov-step`/`L4/iterate-while`. Where no L4-level op exists (orthogonalize), the
  body edge crosses to the L2 named composition the kernel folds (`L2/orthogonalize`). This answers the
  c109-flagged "altitude convention for body-composition edges" sub-question for the krylov-step body.
- **residual (the still-blocked Group-B themes).** 4 of the 5 Group-B themes remain `[garbage?]` for
  distinct, now-precisely-diagnosed reasons (see the chebyshev/jacobi + gram/ils findings below):
  `orthogonalize-composition-lowering` (host `L2/orthogonalize` now reachable but UNTYPED — needs an
  `edges:` block); `chebyshev-iteration-fusion` (host reached only via `L3/chebyshev`/the preconditioner
  leg, itself garbage — baseline-exception candidate); `gram-fold-specialization` (host `L2/gram`
  consumed only by `deflate`, STOP-PROPOSING); `incremental-least-squares-composition-lowering` (host
  absorbed into the krylov-step body, no separable L4-altitude op-edge).
```

### Finding 1 — chebyshev/jacobi preconditioner leg is absorbed-below-column; baseline-exception recommended

```append:scaffolding/open-questions.md

## OQ: chebyshev-jacobi-preconditioner-leg-absorbed-below-column-baseline-exception

- **status:** OPEN (route to batch-35 meta-phase) — filed cycle-110 (batch-35 D1).
- **observation.** `L4/chebyshev`, `L3/chebyshev`, `L2/chebyshev-iteration`, `L2/jacobi-smoother`, and
  `L4/preconditioning-framework` remain unreachable after the reduce-chain grounding. They form the
  **preconditioner/smoother leg**, distinct from the reduce-to-scalar cohort grounded this cycle.
- **why NO faithful column→preconditioner edge exists (the c107 absorbed-below-column pattern).** The
  preconditioner is **absorbed into `op.T`** as a constructed operator (`L4/ksp_solve.md:26`
  `concepts/constructed-operators` "the preconditioner-side absorption into op.T"; `L2/krylov-step.md:57`
  `op.T = constructed apply_BA = A·M⁻¹`). The kernel folds `apply_linop op.T` — it never names a concrete
  chebyshev/jacobi preconditioner as a separable composed verb. Moreover the dependency DIRECTION is
  reversed from a constituent: `L4/preconditioning-framework` *consumes* `L4/ksp_solve`
  (`L4/ksp_solve ← L4/preconditioning-framework` in `--show-inbound`), it is not a constituent of it. So
  there is NO reachable solve column that genuinely `depends-on` a concrete chebyshev/jacobi
  preconditioner via a faithful path. Forcing `ksp_solve → preconditioning-framework` (the planner's
  higher-leverage candidate to assess) would INVERT the real consumer→producer direction — an unfaithful
  over-edge, declined per §(g) (faithful-edge-or-finding, the c108 catch pattern).
- **recommendation.** Track this leg as a **baseline-exception** (the c107 BC/divfree absorbed-below-column
  precedent): the chebyshev/jacobi smoother cohort is genuine firm vocabulary that is *absorbed into the
  constructed `op.T`* rather than reached as a named constituent — correctly off the reachability spine,
  not garbage to delete. The meta-phase ratifies the baseline-exception ledger entry. Do NOT force a
  column→preconditioner edge.
```

### Finding 2 — `gram_reduce → inner_product` declined as a sibling over-edge; `L2/gram` and `L2/incremental-least-squares` routed

```append:scaffolding/open-questions.md

## OQ: gram-reduce-inner-product-is-sibling-not-composes-edge-declined

- **status:** OPEN (route to batch-35 meta-phase) — filed cycle-110 (batch-35 D1).
- **observation (the declined over-edge).** The planner's high-confidence pick `gram_reduce → L4/inner_product`
  (flip `reference`→`depends-on`) was RE-READ and DECLINED as a sibling-misclassified-as-composes
  over-edge. `gram_reduce` is *"the reduce-to-matrix member of the L4 algebra-of-folds family, the
  **sibling** of the reduce-to-scalar `inner_product`"* (`L4/gram_reduce.md:33,209-214`); its body folds
  `L1/matrix-weighted-norm` (diagonal) + `L1/bilinear-form` (off-diagonal) — both already `depends-on`
  (`L4/gram_reduce.md:7-9,91-93`) — NOT `L4/inner_product`. The off-diagonal "is an `inner_product_M`-shaped
  weighted bilinear" but is realized via `L1/bilinear-form` (which IS the weighted member of
  inner_product), so the genuine composition is the L1 leaf gram_reduce already names. Typing
  `gram_reduce →depends-on→ L4/inner_product` would force a sibling into a constituent role — unfaithful.
  Declined per §(g) faithful-edge-or-finding (the c108 BC-theme decline exemplar). **It is also unneeded:**
  the reduce-to-scalar chain grounds via the krylov-step body edges regardless. The existing
  `reference: L4/inner_product` (sibling cross-link) stays.
- **`L2/gram` routed (NLEPS, not gram_reduce).** `L2/gram` (the all-pairs `XᴴX` over a basis) is consumed
  by `deflate` (`L2/gram.md:25-26` "consumed by the sibling oblique-projection combinator `deflate` … the
  Gram matrix `gram` builds is exactly what `deflate` LU-solves"), which is on the STOP-PROPOSING
  demand-gated FRONTIER list. It is a DIFFERENT op from the L4 `gram_reduce` (operator-weighted
  symmetric-Gram over a solution family). `L2/gram` reaches root only via `deflate`; correctly stays
  garbage until deflate is demand-gated on. NOT grounded.
- **`L2/incremental-least-squares` routed (absorbed, no L4-altitude op-edge).** The GMRES running-QR /
  Givens stream IS a genuine GMRES constituent — `L2/incremental-least-squares.md:16-19` names it as the
  composition `ksp_solve §Semantics materialise_iterate` consumes and the krylov-step LS-residual proxy
  (`gmres.md:471-489`). But at the L4 chapter altitude it is **absorbed into the krylov-step body**
  (the LS-residual is a `StepOutputs` derived view, `L4/krylov-step.md:104`) and the
  `ksp_solve materialise_iterate` tail — there is no separable L4-level `incremental-least-squares` op to
  point a `composes` edge at (no `L4/incremental-least-squares` chapter). Grounding it faithfully would
  require either an L4 op (over-structure for an absorbed derived view) or a non-L4-altitude
  `L4/krylov-step → L2/incremental-least-squares` edge (altitude-inconsistent with the reduce verbs, and
  the relationship is a derived-view byproduct, not a folded constituent). ROUTED for the meta-phase to
  judge: absorbed-below-column baseline-exception (like the preconditioner leg) vs. a future L2-altitude
  grounding when the GMRES variant is exercised. NOT forced this cycle.
```

### Finding 3 — lazy-tail typing items the grounding surfaced (untyped reduce/orthogonalize mid-nodes)

```append:scaffolding/open-questions.md

## OQ: l3-l2-reduce-orthogonalize-midnodes-lack-typed-edges-blocks

- **status:** OPEN (lazy-tail typing; route to plan `graded-stack-lazy-tail-typing`) — filed cycle-110 (batch-35 D1).
- **observation.** The reduce/orthogonalize grounding surfaced three firm mid-nodes that carry only
  LEGACY frontmatter (`lifts_from`/`lowers_to` lists, no typed `edges:` block), so they neither cascade
  their own downward edges nor flip their themes:
  - `L2/orthogonalize` — NO frontmatter at all (begins `# orthogonalize`). Now reachable (grounded this
    cycle) but carries no typed `lowers-to` to `L2-L1/orthogonalize-composition-lowering`, so that theme
    stays `[garbage?]`. A from-scratch `edges:` block (mirroring the c109 `L2/krylov-step` authoring:
    `depends-on L1/orthogonalize` + `lowers-to L2-L1/orthogonalize-composition-lowering` + `lowers-from
    L3/orthogonalize`) would flip the theme.
  - `L3/orthogonalize` — only `lifts_from`/`lowers_to`, no typed `edges:`. Did not flip (no typed inbound
    from a reachable node). A typed block (`depends-on L2/orthogonalize lowers-to` + the variant-split
    theme) would ground it once L2/orthogonalize is reachable (now true).
  - `L3/nrm2` — consumer-stub with only `lifts_from`/`lowers_to`. Reachable (inbound from `L4/nrm2`) but
    carries no typed downward `depends-on` (its genuine target is `L2/inner_product` at the diagonal,
    already reachable; `lowers-to L1/nrm2`). Typing it completes the nrm2 node's edges.
  These are mechanical from-scratch `edges:` authoring (the c109 `L2/krylov-step` / c108
  `L2/divfree-projector` template), faithful and low-risk — the next lazy-tail tranche. NOT done this
  cycle (the grounding-pass scope was the reachable-consumer body edges, and adding the L2/orthogonalize
  theme edge would expand into authoring an untyped chapter's full edges block). Note: `L2/nrm2` is a
  SEPARATE cohort (the normalize/scal/elementwise tail), off the reduce-to-scalar scope — `L2/nrm2 ←
  L2/normalize` only, both off-spine; not a reduce-chain residual.
```

## Caveats

- **`deflate` excluded by design.** `L2/deflate` / `L2-L1/deflate-composition-lowering` (the demand-gated
  FRONTIER member, STOP-PROPOSING list) were NOT touched. The `L2/gram → deflate` finding above does not
  propose grounding deflate — it documents why `L2/gram` correctly stays garbage.
- **Partial-ground + routed-findings is the EXPECTED legitimate outcome**, not a shortfall (per the
  dispatch directive). The reduce-to-scalar chain + orthogonalize leg grounded (+10 reachable, −8 garbage);
  the chebyshev/jacobi preconditioner leg, the gram_reduce sibling over-edge, and the gram/ils ops routed
  with precise root-cause diagnoses + a baseline-exception recommendation for the meta-phase to ratify.
- **Frontmatter-only, single-file write-set.** One `L4/krylov-step.md` frontmatter edit (+3 edges); no
  prose claims, no `SUMMARY.md`/`index.md` change, no consolidated-tally collision. `git status --short
  book/` confirmed empty after the verify→revert. Disjoint from D2 (`L1/{axpy,axpby,axpbypcz}.md`).
```
