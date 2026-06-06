---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-06T185234Z
scope: cycle-115 D1 — INDEPENDENT PLATEAU-PROBE — frontier-exhaustion re-derivation on BOTH axes (reachability + forward vocabulary) + true-coverage-hole sweep
status: pending
integrated_at: 2026-06-06T211500Z
integration_commit: 0666e5a
integration_notes: "cycle-115 D1. OBSERVATION-ONLY (proposed-changes = None; no book/ mutation). Applied clean (staging row 3). VERDICT = frontier-exhaustion CONFIRMED on all 3 commissioned fronts (no missed faithful ground; all 8 promotion_frontier members genuinely gated; no true in-scope coverage hole -- build_mesh is a tracked candidate-(c) Mesh-wrapper deferral). Exhaustion-OF-CURRENT-SCOPE, NOT terminal (NEW USER DIRECTIVE B 2026-06-06 opens the deferred fronts post-consolidation). 2 benign linter-semantics flags (roots=36 = 12 columns x 3 levels; boundary-mode.{L0,L1,L4} double-counted as ROOT + promotion_frontier). Reachability-neutral. Producer appended 4 plateau-probe OQs + integrator appended 1 READ-CONTEXT note. citecheck 21 ok/2 MISS (both scaffolding/priorities.md internal refs outside citecheck roots, backing a FINDING, verified to resolve; non-blocking). All carried to the IMMINENT out-of-band meta-phase."
---

# CYCLE: Cross-layer observation — plateau-probe-independent-exhaustion-audit

## Summary

I independently re-derived frontier-exhaustion on both graded-stack axes WITHOUT trusting the
batch-36 meta-phase assessment, sweeping all three commissioned fronts from the live linter state
(`rank_violations: 0`, `promotion_frontier: 8`, `detritus: 127`, `detritus_with_typed_edges_stronger_signal: 23`,
`reachable: 132`, `roots: 36`). **VERDICT: exhaustion CONFIRMED — zero missed clean picks on all three fronts.**
(1) Reachability: every one of the 23 STRONGER-GARBAGE members is covered by a ratified RE1-RE8 baseline-exception
whose §2f GROUND disposition I re-checked against the live prose; none has a genuinely-faithful inbound `depends-on`
edge from a reachable node that the c113 audit + RE ratification missed — the would-be grounds (RE2 `krylov-step→L3/orthogonalize`,
RE8 `transient→L3/fold_solve`) are confirmed UNFAITHFUL (the reachable consumers compose at L2/L4, deliberately skipping
the L3 iteration-views). (2) Forward vocabulary: all 8 `promotion_frontier` members are genuinely
obstruction-/demand-gated; I read each chapter's §Status + cited the gate. (3) Coverage holes: every in-scope
feature/vocabulary item has a chapter or is a recorded, tracked deferral — including the `build_mesh` stage, which is
the standing tracked candidate-(c) "Mesh-wrapper vocabulary proper" deferral under the MFEM-opaque + single-machine
scope-out, NOT an unfiled hole.

## Observation kind

**Coverage gap (NEGATIVE result)** — an exhaustive coverage/reachability sweep that confirms NO coverage gap,
NO mis-gated frontier member, and NO missed faithful ground exist. The load-bearing output is the negative verdict
itself (the independent confirmation the batch-37 meta-phase terminal-state decision is gated on).

## Specific finding

### Front 1 — Missed faithful ground (reachability GC over `detritus=127` / `STRONGER=23`)

The live linter `STRONGER GARBAGE SIGNAL (23)` set matches the RE1-RE8 ledger membership EXACTLY (re-counted: RE6=8
[`L2/axpy`,`L2/axpby`,`L2/axpbypcz`,`L3/axpy`,`L3/axpby`,`L3/axpbypcz`,`L2/scal`,`L3/scal`] + RE7=4
[`L2/elementwise_product`,`L3/elementwise_product`,`L3/assemble-diagonal`,`L3/jacobi-smoother`] + RE8=2
[`L3/fold_solve`,`L3/krylov-step`] + RE1=3 [`L4/preconditioning-framework`,`L2/jacobi-smoother`,`L3/chebyshev`] + RE2=1
[`L3/orthogonalize`] + RE5=5 [`L1/normalize`,`L2/normalize`,`L3/normalize`,`L2/reciprocal`,`L3/reciprocal`] = 23). Zero
undispositioned members.

I ran `--show-inbound` and inspected the inbound typed-edge set for every one of the 23. **The decisive check** (a missed
ground would be a faithful by-name `depends-on` from a REACHABLE consumer that is not yet typed): every inbound edge that
exists points to ANOTHER garbage node (e.g. `L1/normalize <- L2/normalize`; `L2/scal <- L2/normalize`; `L3/jacobi-smoother
<- L2/jacobi-smoother`; `L3/axpy <- L3/orthogonalize`); the rest have NO inbound edge at all (the absorbed-below-combinator
leaves). No reachable consumer points at any of the 23.

I then verified the two most plausible "missed faithful ground" candidates against the live prose (the §2f
faithful-edge-or-finding discipline — a ground may only be reported if it is genuine from the prose, not manufactured):

- **RE2 `L3/orthogonalize`** — the would-be ground is `L4/krylov-step → L3/orthogonalize`. CONFIRMED UNFAITHFUL: `L4/krylov-step`
  carries a typed `kind: composes` edge to **`L2/orthogonalize`** (`book/src/L4/krylov-step.md:14-15` — "no L4 orthogonalize op
  exists, so the body edge crosses to the L2 named composition the kernel folds"), and `L4/orthogonalize` is explicitly
  DEFERRED-marginal with no consumer (`book/src/L4/index.md:85`, OQ `l4-orthogonalize-cap-marginal-defer`). The reachable
  consumer composes the L2 surface directly; the L3 iteration-view (MGS `partial-obstruction` + CGS lifts) is genuinely
  unconsumed. Forcing `krylov-step → L3/orthogonalize` would assert a non-existent constituent-use. RE2 holds.
- **RE8 `L3/fold_solve` / `L3/krylov-step`** — the would-be ground is `transient`/`lifecycle → L3/fold_solve`. CONFIRMED UNFAITHFUL:
  `feature/transient.L4` (`:11,29,45,51,74`), `feature/transient.L1` (`:11,56,58,67`), and `feature/lifecycle.L4` (`:9,42,50`)
  ALL compose the firm **L4** `fold_solve` combinator directly (`transient = fold_solve ∘ fe_assemble`; lifecycle's AMR
  outer fold IS the L4 `fold_solve` state-generated form). The L3 `fold_solve` carries `lifts_from: L4/fold_solve` — the typed
  edge runs L3→L4 (UP), so grounding the reachable L4 node does not carry liveness up to the L3 view. The L3 iteration-views
  are genuine but currently-unconsumed (altitude-skip). RE8 holds.

The remaining RE entries (RE1 preconditioner-leg absorbed into the constructed `op.T = A·M⁻¹`; RE3 `L2/gram` reachable only
via the gated `deflate`; RE4 ILS absorbed; RE5 normalize/reciprocal riding the absorbed legs; RE6 arity-leaves absorbed below
the `linear_combination` combinator; RE7 diagonal-apply kernels absorbed into RE1) each rest on a reverse-direction or
absorbed-below-column relationship that the inbound report corroborates (no reachable depender). **No missed faithful ground.**

### Front 2 — Mis-gated promotion_frontier (re-verified all 8, each gate cited)

The live linter `PROMOTION FRONTIER (8)` is: `L1-L0/bicgstab-iteration`, `L1-L0/minres-iteration`,
`L1-L0/eigsolve-convergence-reason-mapping`, `L2/deflate`, `L2-L1/deflate-composition-lowering`,
`feature/boundary-mode.{L0,L1,L4}`. (Note: the priorities.md gloss lists `deflate` + `deflate-composition-lowering`
as two of the trio and folds the boundary-mode trio as one "boundary-mode" item — the live set decomposes them; the
8 reconcile.) Each gate is REAL:

- **`bicgstab` / `minres`** — `obstruction (enum-only-stub)`. Both route to `MFEM_ABORT("Unexpected solver type for Krylov
  solver configuration!")` (`bicgstab-iteration.md:39` citing `palace/linalg/ksp.cpp:53-57`; `minres-iteration.md:51-55`).
  Status `rough-in (obstruction)` / `rough-in`-as-obstruction, "awaiting an anchor (Palace implementation or admitted MFEM
  substrate)". Per CLAUDE.md §Scope (unimplemented Palace components are NOT direct implementation targets) these are correctly
  gated, NOT clean picks.
- **`eigsolve-convergence-reason-mapping`** — `partly-constructive`; structure firm, the 8 diverged-reason rows reconstructed
  from literature/negative-anchors (Palace PRINTS reason codes but never INSPECTS them — the entire tree has zero
  `EPS_DIVERGED_*`/`EPS_CONVERGED_*` references, `:350-375`). Promotion gated on an upstream Palace behaviour change OR a
  lowering-verifier audit accepting the forward-looking shape. No positive source site exists. NOT a clean pick.
- **`L2/deflate` / `deflate-composition-lowering`** — both `partly-constructive`; the Galerkin-core sub-part is
  literature-anchored not positively sourced (`L2/deflate.md:362-366`; `deflate-composition-lowering.md:27-31`). `L2/deflate`
  is consumed only by the demand-gated NLEPS/deflation frontier (RE3); demand-gated on a downstream NLEPS consumer surfacing.
  NOT clean picks.
- **`boundary-mode.{L0,L1,L4}`** — `seed` (root marker; they ARE in the 36-root set). Stay `seed` on an OWN-readout gate: the
  directly-owned stage-3 readout reduces into a **waveguide-mode output product with no firm home** (the waveguide-mode product
  column is demand-gated). Re-evaluated c085 under the OWN-COMPOSITION rule; the solve corner (`fe_assemble`+`eigsolve`) is firm,
  the readout is the unhomed own-constituent gate (`boundary-mode.L4.md:86-88`). NOT a clean pick — the waveguide-mode reduction
  is the recorded demand-gated promotion route.

**All 8 gates real. No mis-gated clean pick.**

### Front 3 — True coverage holes (CLAUDE.md §Scope cross-check)

All 12 feature columns present (`ls book/src/feature/*.L4.md` = 12): 5 drivers (electrostatic, magnetostatic, eigenmode,
driven, transient) + 5 output products (sparameters, capacitance, inductance, eigenfrequency-qfactor, energy-fields) +
lifecycle spine-ROOT + boundary-mode. FE assembly: `fe_assemble`/`weak_form_term`/`eliminate_*` present. FE-space construction:
`L1/fe_space`, `L1/fe_collection`, `L1/essential_dofs`, `L1-L0/fe-space-construction-rotation`, `L0/fespace-file` present —
the in-scope, cleanly-liftable FE-space front was opened batch-20 and lifted. Wave-port: `L1/port_projection` + reduced via
`sparameter_reduce`.

**The one item I examined as a candidate hole — `build_mesh` — is CONFIRMED a recorded tracked deferral, NOT an unfiled hole.**
`build_mesh :: Config -> Mesh` (mesh load/preprocess/partition/a-priori-refine) is referenced as stage (1) across
`lifecycle.{L4,L1,L0}` but has no operator chapter; its dep-map rows are marked "— (L0 scaffold)" with no link
(`lifecycle.L1.md:67`; `lifecycle.L4.md:67`; `lifecycle.L0.md:37`). This is intentional: it is the standing
**candidate-(c) "Mesh-wrapper vocabulary proper (the `Mesh` object beyond `fespace` — refinement/geometry)"** deferral
(priorities.md:801#5c, :816#c), explicitly governed by the redirect CLEAN-GATE ruling: *"what the mesh can't cleanly say
(MFEM-opaque mesh refinement, partitioning — much of which is the single-machine / `Par*`-single-rank scope-out) is a
spine-finding, not a forced land"* (priorities.md:848). Mesh partitioning is additionally MPI/`Par*` → out of scope per
CLAUDE.md §Scope. So `build_mesh`'s opaque-scaffold rendering is the deliberate scope-out outcome, exactly the tracked-deferral
class (like `fe_space_hierarchy`/de-Rham-interpolator/waveguide-mode, all OQ-tracked, none filed as chapters).

**No true coverage hole found.**

## Recommendation

**Defer / record the negative verdict — exhaustion CONFIRMED, no follow-up dispatch warranted on content grounds.**
This independent probe corroborates the batch-36 meta-phase assessment on all three fronts; the batch-37 meta-phase may
proceed to its terminal-state decision with the independent confirmation in hand. No abstractor/lifter/harvester/lowering-verifier
dispatch is recommended (no missed pick to draft, re-anchor, formalize, or deepen). The only standing promotion routes are the
recorded demand-gates (a downstream NLEPS consumer → `deflate`/RE3; a waveguide-mode output product → boundary-mode trio; a
future preconditioner-construction / L3-iteration-consuming feature column → RE1/RE2/RE7/RE8), each correctly off the active
frontier per STOP-PROPOSING.

## Supporting evidence

- Live linter state: `python3 tools/graded-stack-lint/graded_stack_lint.py --json` → `rank_violations: 0`,
  `promotion_frontier: 8`, `detritus: 127`, `detritus_with_typed_edges_stronger_signal: 23`, `reachable: 132`, `roots: 36`;
  `--show-inbound` STRONGER GARBAGE SIGNAL (23) list + per-node inbound edges.
- RE ledger: `scaffolding/graded-stack-baseline-exceptions.md` (RE1-RE5 cycle-111 §lines 116-136; RE6-RE8 cycle-114 §lines 140-154).
- Front 1: `book/src/L4/krylov-step.md:14-15` (RE2 composes-at-L2); `book/src/L4/index.md:85` (L4/orthogonalize deferred);
  `book/src/L3/fold_solve.md:5-8,18,31` (RE8 lifts_from UP); `book/src/feature/transient.L4.md:29,45,51,67`,
  `transient.L1.md:56,58,67`, `lifecycle.L4.md:42,50,61` (consumers compose L4 fold_solve directly).
- Front 2: `book/src/L1-L0/bicgstab-iteration.md:39,82-84`; `book/src/L1-L0/minres-iteration.md:51-55,151-154`;
  `book/src/L1-L0/eigsolve-convergence-reason-mapping.md:350-375`; `book/src/L2/deflate.md:5-9,23-25,362-366`;
  `book/src/L2-L1/deflate-composition-lowering.md:27-31`; `book/src/feature/boundary-mode.{L0,L1,L4}.md:50-52/68-70/86-88`.
- Front 3: `ls book/src/feature/*.L4.md` (12 columns); `book/src/feature/lifecycle.{L4,L1,L0}.md` (build_mesh stage rows);
  `scaffolding/priorities.md:801,816,848` (candidate-(c) Mesh-wrapper deferral + CLEAN-GATE scope-out ruling);
  FE-space chapters `book/src/L1/{fe_space,fe_collection,essential_dofs}.md`, `book/src/L1-L0/fe-space-construction-rotation.md`,
  `book/src/L0/fespace-file.md`.

## Open questions / caveats

- **Caveat — linter `roots: 36` vs CLAUDE.md `40 feature columns` framing.** My task brief said "all 40 feature columns off
  `seed`"; the linter reports 36 roots (= 12 columns × 3 levels, minus the L2/L3 levels not authored per the "L2/L3 feature
  chapters ONLY where reshaped" rule). The 36 vs 40 discrepancy is a counting convention (roots-as-files vs columns), NOT a
  missing column — all 12 logical columns are present. Flagging so the meta-phase reconciles the headline number, not as a hole.
- **Caveat — the boundary-mode trio is simultaneously a ROOT and a `promotion_frontier` member.** The linter treats `seed`
  roots that are sub-firm as frontier-eligible; this is benign (the gate is the waveguide-mode demand-gate, real), but the
  meta-phase may want to confirm whether a `seed` root SHOULD appear in the `promotion_frontier` count at all (it inflates the
  "8" by 3). This is a linter-semantics question, not a content finding.
- I did NOT exhaustively re-verify the `detritus_no_typed_edges_pre_p1_artifact: 104` set (the weaker `[garbage?]` signal) —
  per the brief these are edge-untypedness artifacts collapsing as the lazy tail types, and the commissioned scope was the 23
  STRONGER members. If the meta-phase wants belt-and-suspenders, a future pass could spot-check the L1-L0 mutation-rotation
  themes in that set for a reachable-consumer ground, but none is expected (they are per-op lowering themes whose ops are
  themselves off-spine).

## Proposed-changes

None. This is an observation-only DISPATCH-phase audit; no `book/` mutation, no proposed edits. (OQ-ledger append handled
separately per the append-only discipline.)
