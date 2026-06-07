---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-07T164021Z
scope: 5-driver L4-completeness audit (ASK-2 "B" capstone) — does every sim driver reach L4 by composing FIRM L4 vocabulary BY NAME?
status: pending
integrated_at: 2026-06-07T170138Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-128 D3 (batch-41 MIDDLE) the ASK-2 'B' CAPSTONE; read-only audit, NO artifact change (no proposed-changes block); CAPSTONE VERDICT recorded prominently in roadmap/log/integrator-signals for the batch-41 meta — the in-scope FEATURE-SURFACE SPINE is L4-COMPLETE (ALL 5 drivers + lifecycle ROOT PASS, 12 named constituents firm on disk, 2 tracked opaque-library boundaries NOT gaps, NO GAP); recommends DEFER / wind the in-scope spine to MAINTENANCE; 2 c129-cleanup stale-token OQs promoted; graded-stack no-op, all totals HELD."
---

# CYCLE: Cross-layer observation — 5-driver L4-completeness audit

## Summary

This is the ASK-2 "B" capstone: a read-only coverage audit of whether each of the 5 sim-driver
feature columns (electrostatic / magnetostatic / eigenmode / driven / transient) reaches L4 by
composing **firm L4 vocabulary BY NAME**, end-to-end (config → mesh → assemble → solve →
postprocess → output product), plus the spine-ROOT `lifecycle.L4` they hang off. **Verdict: the
in-scope FEATURE-SURFACE SPINE is L4-COMPLETE.** All five drivers PASS — every composition stage
of every driver names a firm L4 combinator that I verified `firm` on disk, with the two opaque
boundaries (the eigenmode `eigsolve` black-box kernel and the transient per-step ODE integrator)
being **tracked opaque-library dispositions, not gaps**, and the matrix-free constructive interior
correctly grounded as a navigational `reference` at the `fe_assemble` leaf (NOT a driver-stage
edge). The lifecycle ROOT composes all five by canonical slug over `build_mesh` (firm) +
`fold_solve` (firm). **No genuine L4-completeness GAP found.** This is the strong signal the
planner/meta flagged: it feeds the batch-41 meta's ASK-2 capstone verdict and the "E — wind to
maintenance" judgment for the in-scope spine.

## Observation kind

**Coverage gap audit (the inverse result: NO coverage gap).** A per-driver L4-reachability coverage
audit over the FEATURE-SURFACE SPINE. The expected disposition set was PASS / opaque-boundary /
absorbed-below-column / GAP; the result is **all-PASS with two tracked opaque-boundary
constituents** — the spine is L4-complete for its in-scope drivers.

## Specific finding

### Per-driver coverage table

| Driver | Disposition | Stage-by-stage L4 vocabulary (all verified `firm` on disk) | Notes |
|---|---|---|---|
| **electrostatic** | **PASS** | assemble: `fe_assemble` (firm) · solve: `solve_family` (firm) + `ksp_solve` (firm) · reduce: `gram_reduce` (firm, `w=1` voltage specialization) | Cleanest exemplar; fixed-operator `solve_family` witness 1. Output product = `capacitance.L4` sibling reference (not a blocker). |
| **magnetostatic** | **PASS** | assemble: `fe_assemble` (firm) · solve: `solve_family` (firm) + `ksp_solve` (firm) · reduce: `gram_reduce` (firm, `w=1/(IᵢIⱼ)` current-normalized) | Sibling of electrostatic; `solve_family` witness 2. Output product = `inductance.L4` sibling reference. |
| **eigenmode** | **PASS (one tracked opaque-boundary constituent)** | assemble: `fe_assemble` ×3 (K/C/M pencil, firm) · solve: `eigsolve` (firm) · readout: pure `map` → `eigenfrequency-qfactor.L4` (firm) | `eigsolve` is the **opaque-library kernel risen to L4 as an opaque-surface primitive** (SLEPc `EPSSolve` / ARPACK `naupd` RCI; `project_blackbox_vs_accelerated_kernels` case 1). Documented obstruction, **tracked disposition NOT a gap** — the cap is firm *as a cap*; the iteration is library-owned. Minimal composition shape (no outer solve-loop the calculus owns). |
| **driven** | **PASS** | assemble: `fe_assemble` ×3 basis (firm) · per-ω rebuild: `assemble_frequency_operator` (firm) · solve map: `frequency_sweep` (firm) + `ksp_solve` (firm) · reduce: `sparameter_reduce` (firm c083) → `sparameters.L4` | Operator-VARYING corner (`SetOperators` inside the loop, the non-hoist) — all three composition stages compose firm combinators. |
| **transient** | **PASS (one tracked opaque-boundary constituent)** | assemble: `fe_assemble` ×3 (K/C/M, firm) · march: `fold_solve` (firm, default/primary witness) | Per-step body is the **opaque MFEM `ODESolver::Step`** (implicit solve inside the integrator) — `obstruction (opaque-library-ownership)` **quantified-over by the firm `fold_solve`** and recorded at the lowering layer. **Tracked disposition NOT a gap.** Product = field trajectory materialized in-column (no sibling output column). |
| **lifecycle (spine ROOT)** | **PASS** | mesh: `build_mesh` (firm, L1) · dispatch: over the 5 driver columns (sibling references) · adaptive fold: `fold_solve` (firm, state-generated `schedule-source` AMR form) | Meta-feature ROOT; the 5 drivers hang off it cleanly by canonical slug. `boundary-mode.L4` (the 6th `BOUNDARYMODE` branch) is `rank: firm` on disk but OUT of the 5-driver scope. |

### Firm-status verification (verified on disk this dispatch)

Every named constituent confirmed firm in its frontmatter:
`L4/fe_assemble` (firmness: firm), `L4/solve_family` (rank: firm), `L4/ksp_solve` (rank: firm),
`L4/gram_reduce` (rank: firm), `L4/eigsolve` (firmness: firm), `L4/frequency_sweep` (firmness: firm),
`L4/assemble_frequency_operator` (firmness: firm), `L4/fold_solve` (rank: firm),
`L4/sparameter_reduce` (firmness: firm), `L4/eigenfreq_qfactor_reduce` (firmness: firm),
`L4/mk_matrix_free_operator` (status/rank: firm), `L1/build_mesh` (rank: firm).
Zero non-firm / roadmap_goal / missing constituent named at any driver L4 stage. (`mk_matrix_free_operator`
firmed c127 — the planner's frontmatter snapshot of "roadmap_goal" is stale-against-disk; it is now firm.)

### The matrix-free candidate-edge finding (planner's sharpened input)

The planner asked whether any driver's ASSEMBLE stage should compose `mk_matrix_free_operator` (or
`fe_assemble`) BY NAME. **Finding: the edge already exists at the correct altitude, and a
driver-stage `driver-assemble → mk_matrix_free_operator` edge should NOT be authored.** All five
drivers compose `fe_assemble` BY NAME at their assemble stage (verified). `L4/fe_assemble.md:15-16,
164` already carries the matrix-free interior as a **navigational `reference` (`constructs-via`),
explicitly NOT a `depends-on`**: the matrix-free constructor is the interior of `fe_assemble`'s
opaque `assemble_term` leaf (the `UseFullAssembly`-false dispatch), which the fold quantifies over.
A direct `driver-assemble → mk_matrix_free_operator` edge would **misclassify** the relationship —
the matrix-free interior lives *below* `assemble_term`, it is not a driver-stage constituent, and a
firm node must not `depends-on` what was a rank-0 roadmap_goal (now firm, but the relationship is
still leaf-interior, not stage-composition). The faithful pull-to-root already grounds
`mk_matrix_free_operator` from `fe_assemble`. **No edge to author; no GROUND needed; this is the
faithful-edge-already-present case.** (This is the RE11 libceed-substrate cohort's prospective
grounder — see below.)

### Tracked dispositions cited (NOT gaps)

- **eigenmode `eigsolve`** — opaque-library kernel, `project_blackbox_vs_accelerated_kernels` case 1;
  the L4 echo of the `L3/eigsolve` `partial-obstruction`. RE11 tracks its kernel-impl
  (`L3/eigsolve-impl`, GROUNDED c124 by the nleps consumer). Opaque-boundary, expected.
- **transient per-step ODE body** — `obstruction (opaque-library-ownership)`, quantified-over by the
  firm `fold_solve`. Opaque-boundary, expected.
- **RE4** (`L2/incremental-least-squares`) — the GMRES running-QR stream is absorbed-below-column in
  the `krylov-step` body; NOT named at any of the 5 drivers' L4 stages (none composes a GMRES-variant
  running-QR by name). Live, consumer-gated baseline-exception — confirmed it does NOT surface as a
  driver-stage gap this audit (the 5 drivers compose `ksp_solve`/`solve_family`/`frequency_sweep`/
  `fold_solve`, none names the ILS view). Correctly tracked.
- **RE11** (libceed-substrate + matrix-free cohort) — reference-only-reachable BY DESIGN; the audit
  CONFIRMS the prospective grounder is `fe_assemble`'s `constructs-via` reference (above), and that no
  driver introduces a faithful `depends-on` that would change RE11's disposition this cycle. Correctly
  tracked.

## Recommendation

**Defer — no follow-up dispatch warranted; record the all-PASS result as the L4-completeness
capstone evidence.** The audit is the validation capstone the planner scoped; the result is the
strong all-PASS signal.

- **For the batch-41 meta-phase (ASK-2 capstone verdict):** the in-scope FEATURE-SURFACE SPINE is
  **L4-complete** — all 5 drivers + the spine ROOT compose firm L4 vocabulary by name, with the only
  non-PASS constituents being two *expected, tracked* opaque-library kernels. This is direct evidence
  for the ASK-2 "B" capstone judgment and supports the "E — wind to maintenance" fallback for the
  in-scope spine (the heavy "A" build landed c127; "B" confirms completeness).
- **NO c129 GAP-driven dispatch** — there is no genuine L4-completeness GAP to recruit a fix for. The
  audit-first framing returns clean.
- **Matrix-free edge:** do NOT author a `driver-assemble → mk_matrix_free_operator` edge — the
  faithful navigational `reference` already exists at the `fe_assemble` leaf altitude. Recommend the
  meta note that the planner's "candidate driver-assemble edge" resolves as "already-grounded-at-leaf,
  no driver-stage edge".

## Supporting evidence

- Driver L4 columns (all `rank: firm`): `book/src/feature/electrostatic.L4.md`,
  `book/src/feature/magnetostatic.L4.md`, `book/src/feature/eigenmode.L4.md`,
  `book/src/feature/driven.L4.md`, `book/src/feature/transient.L4.md`.
- Spine ROOT: `book/src/feature/lifecycle.L4.md` (composes `L1/build_mesh` + `L4/fold_solve` + the 5
  driver columns; `## Constituent down-links` table :67-73).
- Constituent firm-status verified in frontmatter: `book/src/L4/{fe_assemble,solve_family,ksp_solve,
  gram_reduce,eigsolve,frequency_sweep,assemble_frequency_operator,fold_solve,sparameter_reduce,
  eigenfreq_qfactor_reduce,mk_matrix_free_operator}.md` + `book/src/L1/build_mesh.md`.
- Opaque-kernel dispositions: `book/src/L4/eigsolve.md:176-178` (`## Status`, opaque-library
  constraint); `book/src/feature/transient.L4.md:53, 75` (opaque ODE-step quantified-over by
  `fold_solve`).
- Matrix-free reference edge: `book/src/L4/fe_assemble.md:15-16` (frontmatter `constructs-via`
  navigational reference) + `:164` (the leaf matrix-free interior prose).
- Tracked baseline-exceptions: `scaffolding/graded-stack-baseline-exceptions.md` RE4 (:200, :236),
  RE11 (:237).

## Open questions / caveats

- **Scope boundary confirmed:** `boundary-mode.L4` (the `BOUNDARYMODE` 6th dispatch branch, `rank: firm`
  on disk) is OUT of the 5-driver scope per the dispatch; the lifecycle ROOT references it as a sibling.
  Its readout column `waveguide-mode` is the demand-gated 6th output product (CLAUDE.md §post-consolidation
  all-fronts) — not part of this 5-driver verdict. If a future audit extends to all 6 dispatch branches,
  boundary-mode is the one to re-check (lifecycle table marks it `rank: firm`, but I did not deep-audit its
  composition this dispatch since it is out of the 5-driver scope).
- **`mk_matrix_free_operator` frontmatter-snapshot drift:** the c128 planner CYCLE.md describes
  `mk_matrix_free_operator` as a "roadmap_goal" (its c126 state); on disk it is `status: firm` / `rank: firm`
  (firmed c127). My audit reads the disk state (firm). This is consistent with the c127 lift-through landing,
  not a defect — flagged only so the meta does not treat the planner's stale token as the current state.
- **This is a per-stage composition audit, not a re-verification of each constituent's algebraic claims.**
  I verified each named constituent is `firm` and that the driver composes it by name; I did not re-audit
  the constituents' internal laws (those are the lowering-verifier's domain and already firm). The
  L4-completeness verdict is a *composition-coverage* claim, not a re-litigation of constituent firmness.
