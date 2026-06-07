---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-07T025152Z
scope: c120 D1 — INDEPENDENT terminal-state pre-batch-38-meta plateau-confirmation audit (observation-only)
status: pending
integrated_at: 2026-06-07T040000Z
integration_commit: 09b011f5ca59b7b123e3035cd59e4c13048a20c6
integration_notes: "cycle-120 BATCH-CLOSING finalize (batch-38 position 3/3). OBSERVATION-ONLY — `## Proposed changes` = None, no artifact mutation. VERDICT plateau LARGELY CONFIRMED (both axes; rank_violations=0, promotion_frontier 6 all gated, no coverage hole, STRONGER 27/27 -> ratified RE1-RE10). 2 structured FINDINGS routed to the OQ-ledger by the per-report integrator (re10-interpolator-has-faithful-reachable-consumer-missed-ground [FINDING-1, the missed RE10 section-2f GROUND edge]; waveguide-mode-column-promotion-index-cell-drift [FINDING-2, consistency drift]) for the batch-38 meta-phase to migrate to the plan as c121 picks — NOT applied as artifact changes this cycle. cargo make book EXIT 0, no build-repair; step-5b graded-stack linters ALL HELD vs c119 (files=369, reachable=139, rank_violations=0, unresolved=0, STRONGER=27, promotion_frontier=6), both block-conditions PASS. The batch-38 meta-phase fires NEXT as a SEPARATE dispatch (aggregating 118/119/120)."
---

# CYCLE: Cross-layer observation — c120 plateau-probe terminal-state audit

## Summary

Independent re-derivation of the batch-38 terminal-state assessment (the c115 D1
plateau-probe precedent), trusting neither the planner nor the finalizes. The two
`tools/` linters were re-run on disk and the baseline is **confirmed exactly**:
`files=369, reachable=139, roots=39, detritus=132, STRONGER=27, rank_violations=0,
untyped=61, promotion_frontier=6, unresolved=0`. The plateau is **LARGELY CONFIRMED**
— Axis-1 (rank/well-foundedness) is clean, the promotion-frontier (6) is entirely
obstruction-/demand-gated, the in-scope feature + vocabulary frontier has **no coverage
hole**, and STRONGER=27 maps **exhaustively (27/27)** to the ratified RE1-RE10 reachability
baseline-exception set. BUT the sweep surfaced **2 structured findings** the meta-phase
should migrate: **(FINDING-1)** an Axis-2 **missed faithful grounding** — RE10
(`L1/interpolator`) has two faithful inbound `depends-on` consumers from REACHABLE firm
nodes (`L4/waveguide_mode_reduce` + `L1/divfree-projector`) that the c117 ratification +
c118/c119 grounding missed (its "no consumer yet" premise is FALSIFIED); **(FINDING-2)** a
**consistency-drift** — the c118 D5 `waveguide-mode` column promotion left the `.L0` level
+ two index/group-intro surfaces stale (still saying "seed"), the index-cell drift the
OWN-COMPOSITION mechanics exist to prevent. Verdict: **plateau CONFIRMED for direction-setting
purposes** (no in-scope vocabulary/feature gap, no forward frontier reopened), with 2
low-fan-out honesty/fidelity cleanups for the meta-phase plan.

## Observation kind

Two kinds, both surfaced by the broad sweep (this is the deliberate plateau-probe
broad-sweep exception to one-observation-per-invocation, per the c115 D1 precedent):
- **FINDING-1: Audit residue / Coverage gap (Axis-2)** — a `verified_against`/reachability
  baseline-exception (RE10) whose premise is falsified by a newer reachable consumer; a
  faithful missed grounding edge (§2f GROUND-priority-1).
- **FINDING-2: Consistency drift** — a column promotion that updated the chapter frontmatter
  but not the L0 level or the index/group-intro cells (index-cell drift).

## Specific finding

### FINDING-1 — RE10 (`L1/interpolator`) has a faithful reachable consumer the grounding MISSED

The c117 meta-phase ratified RE10 with the premise *"`interpolator` has no faithful inbound
consumer yet — an unbuilt field-probe/divfree feature"* (OQ ledger line 10; friction-ledger
2150). That premise is **FALSIFIED**. `L1/interpolator` (a STRONGER-garbage node, the de-Rham
discrete grid-transfer operator formalizing `FiniteElementSpace::GetDiscreteInterpolator` /
`BuildDiscreteInterpolator`) has **TWO faithful inbound consumers, both firm AND reachable**:

1. **`L4/waveguide_mode_reduce`** (firm, landed c118 D2/D5; reachable via the
   `feature/waveguide-mode.L4` root). Its `Bz = curl(Et)/(iω)` formation genuinely calls the
   discrete-curl interpolator:
   `const auto &CurlOp = mode_op.GetCurlSpace().GetDiscreteInterpolator(mode_op.GetNDSpace());`
   then `CurlOp.Mult(et.Real(), curl_etr)` (`palace/drivers/boundarymodesolver.cpp:319-323`,
   read on-disk via codemap). `GetDiscreteInterpolator` at `palace/fem/fespace.hpp:107` is the
   *exact* accessor `L1/interpolator` cites and formalizes. The `waveguide_mode_reduce`
   chapter's `## Status`/site-map narrates this ("discrete-curl interpolator `:319-323`",
   `waveguide_mode_reduce.md:326`), but its `edges:` block lists **no `L1/interpolator` edge
   at all** (neither `depends-on` nor `reference`).

2. **`L1/divfree-projector`** (firm, reachable). It consumes the discrete-`Grad` interpolator
   (`palace/linalg/divfree.cpp:117` — "`Grad` = discrete interpolator",
   `divfree-projector.md:319`). The edge is in prose only — `divfree-projector`'s `depends-on`
   block has no `L1/interpolator` target.

`L1/interpolator.md`'s own opening paragraph ALREADY names both: *"the grid-transfer producer
consumed by the divergence-free projector (the `Grad` operator), the boundary-mode `Bz`
readout (the discrete `curl`), …"*. So the consumer relationship is documented prose-side; the
only thing missing is the typed `depends-on` edge from the reachable consumer down to
`L1/interpolator`. This is the §2f GROUND case (priority-1: GROUND a genuine future/absorbed
dependency via a faithful, honestly-typed edge — NOT delete, NOT force, NOT baseline-except).
The edge is faithful (a genuine constituent-use: the consumer applies the interpolator's
produced `LinOp`), not a false grounding.

**RE9 contrast (re-checked, premise HOLDS):** `L1/fe_space_hierarchy` (RE9) was independently
re-swept — no faithful inbound `depends-on` consumer exists. Every book mention
(`L1/jacobi-smoother`, `L1/essential_dofs`, `L1/set_subvector_zero`, `L4/preconditioning-framework`,
the concept pages) is navigational/cross-reference; the geometric-multigrid preconditioner that
would consume the hierarchy + its prolongation operators is genuinely unbuilt. RE9 stays
correctly baseline-excepted. The **asymmetry** (RE9 premise correct, RE10 premise falsified) is
the substance of FINDING-1 — they were ratified together (c117) under the same "no consumer
yet" framing, but only RE9's framing survived c118's landing of `waveguide_mode_reduce`.

### FINDING-2 — `waveguide-mode` column promotion left stale "seed" cells (index-cell drift)

The c118 D5 promotion (rough-in→firm, gated on `waveguide_mode_reduce` firming; OQ
`waveguide-mode-reduce-needs-l4-verb-home` RESOLVED c118 D5, ledger line 1579) flipped the
`feature/waveguide-mode.{L1,L4}` chapter frontmatter to `rank: firm` with full promotion
prose. But three surfaces are STALE:

- `feature/waveguide-mode.L0` — still `rank: rough-in`; its `## Status` note still reads
  *"Held at `rough-in` / `feature_root: seed` … the reduction's L4 verb home `waveguide_mode_reduce`
  has no firm chapter yet (OQ `waveguide-mode-reduce-needs-l4-verb-home`)"* — citing the
  now-resolved gate.
- `feature/index.md` driver-leaf narrative — *"After cycle-117 only `waveguide-mode` remains
  `seed` (its own reduce verb `waveguide_mode_reduce` has no firm L4 verb home yet … promotes
  once that verb firms)"* + the dedicated line *"`waveguide-mode` … its own reduce verb …
  has no firm L4 verb home yet … Promotes to `firm` once that verb firms."*
- `feature/output-product.md` group-intro — *"The column is `seed` (own reduce verb
  rough-in)"* + *"`waveguide-mode` is the sole `seed` output-product column — its own reduce
  verb `waveguide_mode_reduce` is rough-in (no firm L4 verb home yet)."*

The L1/L4 chapters say PROMOTED-firm; the L0 chapter + both index/group-intro surfaces say
still-seed/rough-in. This is precisely the index-cell drift the `layer-intro-author`
§FEATURE-SURFACE "index-cell + sibling-status grep coupling" / index-cell-drift guard exists
to prevent. (`feature_root: seed` itself is CORRECTLY kept on all three levels — it is the
permanent GC-root marker, not a maturity tier; the drift is only the maturity prose.)

## Recommendation

Both findings are **low fan-out, honesty/fidelity cleanups** — they do NOT reopen the forward
frontier and do NOT contradict the terminal-state posture; they are the residue the broad
sweep is for. Migrate both into the batch-38 meta-phase plan as a single small c121 dispatch:

1. **FINDING-1 → GROUND RE10 (layer-intro-author, the typed-edge home).** Add the faithful
   `depends-on` edges: `L4/waveguide_mode_reduce → L1/interpolator` (kind: `uses`/`consumes`)
   and `L1/divfree-projector → L1/interpolator` (kind: `uses`). Either alone flips RE10
   (`L1/interpolator` + its `L1-L0/interpolator-construction-rotation` theme, +2 reachable) live
   and DISCHARGES the RE10 baseline-exception; both are faithful and already prose-documented.
   Update the RE register: RE10 → discharged-by-grounding (RE9 stays). fan-out: LOW-MEDIUM.

2. **FINDING-2 → reconcile the `waveguide-mode` promotion cells (layer-intro-author, mechanical).**
   Flip `waveguide-mode.L0` `rank: rough-in` → firm + rewrite its `## Status` note; reconcile the
   `feature/index.md` driver-leaf narrative + the `output-product.md` group-intro to the firm
   reality (drop "the sole seed output-product column"). fan-out: LOW.

3. **Otherwise: terminal-state posture CORROBORATED.** No in-scope vocabulary or feature
   coverage hole; promotion-frontier all gated; Axis-1 clean. The plateau is real — the
   batch-38 meta-phase can make a terminal-state / direction decision, modulo the 2 cleanups
   above.

These are observations only — no `book/` mutation performed (DISPATCH-phase write-authority
partition; the edits above are proposed for `integrator-per-report` / a c121 dispatch to apply
in Phase 5, NOT enacted here).

## Supporting evidence

- Linter baseline re-run: `tools/graded-stack-lint/graded_stack_lint.py` (on-disk; matches
  the planner baseline exactly).
- STRONGER=27 → RE1-RE10 reconciliation (exhaustive, 27/27): RE1 = {L3/chebyshev,
  L3/jacobi-smoother, L2/jacobi-smoother, L3/assemble-diagonal, L4/preconditioning-framework};
  RE2 = {L3/orthogonalize}; RE5 = {L1,L2,L3/normalize, L2,L3/reciprocal}; RE6 = {L2,L3/scal,
  L2,L3/axpy, L2,L3/axpby, L2,L3/axpbypcz}; RE7 = {L2,L3/elementwise_product}; RE8 =
  {L3/fold_solve, L3/krylov-step}; RE9 = {L1/fe_space_hierarchy,
  L1-L0/fe-space-hierarchy-construction-rotation}; RE10 = {L1/interpolator,
  L1-L0/interpolator-construction-rotation}.
- FINDING-1 source: `palace/drivers/boundarymodesolver.cpp:316-333` (the `Bz` formation block,
  `GetDiscreteInterpolator` + `CurlOp.Mult`, read on-disk via codemap `read_range`);
  `book/src/L4/waveguide_mode_reduce.md` (frontmatter `edges:` block — no interpolator edge;
  `:320-326` site-map naming the discrete-curl interpolator); `book/src/L1/interpolator.md:18-40`
  (scope = de-Rham discrete grid-transfer; opening para names both consumers; cites
  `palace/fem/fespace.hpp:107`); `book/src/L1/divfree-projector.md:99,319` (the `Grad` discrete
  interpolator, `palace/linalg/divfree.cpp:117`). RE10 ratification premise: OQ ledger line 10 +
  friction-ledger line 2150 (c117 batch-37 §2f triage).
- FINDING-2 source: `book/src/feature/waveguide-mode.L0.md` (`rank: rough-in` + stale status
  note), `.L1.md` / `.L4.md` (`rank: firm` + c118 D5 promotion prose); `book/src/feature/index.md`
  (driver-leaf + dedicated waveguide-mode narrative lines); `book/src/feature/output-product.md`
  (group-intro "sole seed output-product column"); OQ ledger line 1579 (the RESOLVED gate).
- Coverage-hole sweep: `ls book/src/feature/` (all 5 drivers + lifecycle spine-root + 6
  output products + boundary-mode); `ls book/src/L1/` (mesh: `build_mesh`,
  `mesh-construction-intro`; fe_space: `fe_space`, `fe_space_hierarchy`, `fe_collection`,
  `essential_dofs`, `interpolator`; assembly: `fe_assemble`, `bilinear-form`,
  `assemble-diagonal`, `assemble_frequency_operator`) — no in-scope hole.
- Promotion-frontier (6) gating: `bicgstab-iteration`/`minres-iteration` = `obstruction`
  (no Palace L0 realization); `eigsolve-convergence-reason-mapping` = `partly-constructive`
  (negative-anchored); `L2/deflate` + `L2-L1/deflate-composition-lowering` = RE3 gram/deflate
  demand-gated; `feature/waveguide-mode.L0` = the FINDING-2 stale-`seed` L0 level (its frontier
  membership is itself a symptom of FINDING-2, not an independent clean pick).

## Open questions / caveats

- **Both findings appended to `scaffolding/open-questions.md`** as `re10-interpolator-has-faithful-reachable-consumer-missed-ground`
  (FINDING-1) and `waveguide-mode-column-promotion-index-cell-drift` (FINDING-2), under the new
  `## c120 D1 plateau-probe` section.
- FINDING-1 edge `kind:` — I recommend `uses`/`consumes` (constituent-use of the produced
  `LinOp` via `apply_linop`), matching how `L1/interpolator`'s own `reference` block tags
  `L1/apply_linop` as "consumed-by". The layer-intro-author should pick the exact registered
  kind token; the load-bearing point is it is a **blocking `depends-on`** (carries liveness),
  not a navigational `reference`. Well-foundedness holds trivially (both consumers firm rank-3,
  `interpolator` firm rank-3; 3≤3).
- FINDING-1 caveat: grounding via `L1/divfree-projector` is the safer minimal edge (an L1→L1
  constituent-use, the cleanest analog of the existing fe_space-cohort grounding); the
  `waveguide_mode_reduce → interpolator` edge is an L4→L1 altitude-crossing use (the consumer
  composes the interpolator's apply directly at the readout) — both faithful, but the
  layer-intro-author should confirm the L4→L1 altitude-crossing edge convention against the
  existing `feature → L1` grounding precedents (`energy-fields.L4 → L1/participation_ratio`,
  `lifecycle.L1/.L4 → L1/build_mesh`) before authoring; that precedent exists, so it is sound.
- This audit performed NO `book/` mutation (DISPATCH-phase discipline). No proposed-changes
  block is emitted — the two findings are recommendations for the meta-phase to migrate into
  the plan for a c121 dispatch, per the cross-layer-cross-cutter surface-don't-enact role.
