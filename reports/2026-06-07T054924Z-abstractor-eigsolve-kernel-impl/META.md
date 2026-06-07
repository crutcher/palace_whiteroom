---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T061500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
  rank-invariant: pass
  reachability: warning
repaired_at: 2026-06-07T063000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
  rank-invariant: not-needed
  reachability: not-needed
  lanczos-step-scal-dep: repaired
  alpha-insert-contradiction: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of "L3 eigsolve kernel-IMPLEMENTATION — constructive Krylov-Schur eigensolve"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing Palace anchor was re-verified independently via codemap `read_range` against on-disk source. All match exactly: `slepc.cpp:635 EPSSetType(eps, EPSKRYLOVSCHUR)` (the decisive evidence — confirmed verbatim), `:638 EPSPOWER`, `:641 EPSSUBSPACE`, `:644 EPSJD`, `:648-653` the TOAR/STOAR/QARNOLDI/SLP/NLEIGS `MFEM_ABORT` arm, `:694 EPSSolve(eps)`, `:695 EPSGetConverged`, `:707 RescaleEigenvectors`, `:734 EPSGetBV`, `:607 EPS_HEP / :610 EPS_NHEP / :613 EPS_GHEP / :616 EPS_GHIEP / :619 EPS_GNHEP`, `:715 l * gamma` (the un-transform accessor). ARPACK: `:270 iparam[2] = arpack_it (Maximum number of Arnoldi iterations)`, `:273 iparam[6] = sinvert ? 3 : 1 (Problem mode)`, `:278 which::largest_magnitude`, `:318 naupd` RCI driver (the `:315-339` callback-dispatch loop is accurate — `ido` branches to `ApplyOp`/`ApplyOpB`), `:342 num_it = (int)iparam[2]`, `:369 neupd`. The book-side citations (`L1/index.md:179`, `L2/krylov-step.md:187`) verify verbatim. No DRIFT found. The report appropriately frames all Palace anchors as **kernel-api loop sites the impl realizes**, NOT as positive source FOR the speculative impl — correct for a roadmap_goal.

**surface-or-evidence — pass.** This is a roadmap_goal (rank-0 claim-free intent) plus a kept kernel-api role-label — not a refinement-shaped proposal asserting new surface claims. The constructive impl form is explicitly flagged SPECULATIVE throughout; the evidence shape is the constituent down-links (firm `krylov-step`/`ksp_solve`/`apply_linop`/`orthogonalize`) + the kernel-api loop-site anchors, which is the correct evidence shape for a kernel-impl reconstruction. Record-definition sub-check: the signatures name `EigResult`/`EigControl` (eigsolve_impl) and the `BV` carry; these are roadmap_goal intent-level sketches, not firm record claims, and the chapter is explicitly claim-free, so the in-itself-definition obligation is deferred to firming (correctly routed — the impl notes `rayleigh_ritz`/`thick_restart` and the records materialize at promotion). No gap to flag at rank-0.

**rotation-quality — pass.** This is an L3 iteration-rotation kernel-impl: it renders the opaque library loop (`EPSSolve`/`naupd`) as an explicit value-threaded `iterate_while_L3` fold over firm `krylov-step`/`lanczos_step` — a genuine structural rotation (opaque single-call → constructed outer-thick-restart-driver ▷ inner-basis-extension-loop ▷ Rayleigh-Ritz), not a rename. The construction is strictly more equational/abstract than the opaque call. The `lanczos_step` specialization (collapse `op.orthog` MGS/CGS/CGS2 to the band-3 three-term recurrence) is a genuine narrowing, not a 1:1 mapping.

**variant-axis-coverage — pass.** Five orthogonal axes are enumerated for eigsolve_impl (eigen-algorithm / problem-symmetry / spectral-transformation / problem-type / restart-shape) and two for lanczos_step (reorthogonalization / matrix-pencil), each tied to its source (e.g. eigen-algorithm ← `slepc.cpp:635-644`; problem-symmetry ← `slepc.cpp:607/613`). No hidden branches: the `MFEM_ABORT` arms (TOAR/STOAR/etc.) are scoped out as not-implemented, and the inherited-vs-new axes are distinguished.

**cross-reference-integrity — pass.** Every cross-referenced file verified on disk: `L3/eigsolve.md`, `L3/krylov-step.md`, `L4/krylov-step.md`, `L3/ksp_solve.md`, `L3/apply_linop.md`, `L2/orthogonalize.md`, `L4/eigsolve.md`, `L2/eigsolve.md`, `L2/krylov-step.md`, `L1/{dot,nrm2,axpy,scal}.md`, `L1/index.md`, `feature/eigenmode.L4.md`, `methodology/resolution-ladder.md`, `concepts/sequential-obstruction.md`, `concepts/constructed-operators.md`, `concepts/solver-as-operator.md`, `semantics/index.md`, `L1-L0/minres-iteration.md`. The two `new:` targets (`L3/eigsolve-impl.md`, `L3/lanczos_step.md`) are correctly the files this dispatch creates. Semantics section anchors verify: §1.2.1 named shape groups, §3.7 iterate_while, §3.8 demand-pruning all real. The `## Status` edit anchor on `L3/eigsolve.md:191` matches the proposed `old_string` verbatim and the `new_string` preserves the entire existing body, prepending only the kernel-api role-label sentence. SUMMARY.md insert anchors (line 121 `eigsolve`, 123 `krylov-step`) both exist.

**edge-label-fidelity — pass.** The load-bearing edge label is verified correct: `realizes-kernel-api` is declared `reference`-class in both `eigsolve-impl.md` frontmatter (`reference:` block, NOT `depends-on:`) and described in prose as navigational/free, NOT carrying liveness, NOT constraining rank. The impl→api direction is correct (impl realizes api). The kernel-api `L3/eigsolve` is KEPT at `partial-obstruction` and explicitly NOT downgraded — the `## Status` edit's `new_string` states "The `partial-obstruction` status is UNCHANGED" and preserves the full existing body. The `folds`/`composes`/`specializes` edge labels on the `depends-on` block are all `depends-on`-class (blocking) and match the prose (folds krylov-step/lanczos_step; composes ksp_solve/apply_linop/orthogonalize; lanczos_step specializes krylov-step). No L_{n+1}→L_n mislabel.

**plan-kind-consistency — pass.** Declared kind `kernel-impl` (eigsolve-impl) / `kernel-impl-constituent` (lanczos_step), status `roadmap_goal` rank 0. The content shape matches: claim-free intent banners present, no positive Palace claim, speculative-flagged constructive form, pulled-by provenance, declared deps. This is DIRECTIVE-3 item-2c executed in the kernel-API/kernel-impl distinction shape. The role-labels (`kernel-api` appended to eigsolve, `kernel-impl`/`kernel-impl-constituent` on the new nodes) are consistent with the directive's reviewable-token mechanics.

**skill-uptake-survey — pass (telemetry).** The report references `citecheck --anchor` self-verification in §Evidence and the Supporting-evidence block. No skill mis-claim. (Surfaces telemetry, non-blocking.)

**rank-invariant (graded-stack ch.9) — pass.** eigsolve-impl is rank-0 `roadmap_goal`; its `depends-on` deps include firm nodes (`krylov-step`, `ksp_solve`, `apply_linop`, `orthogonalize`, all rank-3) and one rank-0 `roadmap_goal` (`lanczos_step`). Per the well-foundedness invariant `rank(u) ≤ rank(v)`, a rank-0 node may rest on anything (rank 0 ≤ all), so resting on the not-yet-firm `lanczos_step` is permitted — confirmed against `resolution-ladder.md:75-76` ("roadmap_goals may stack on roadmap_goals... stubs, rough-ins, and firms"). lanczos_step (rank-0) resting on firm `krylov-step`/`apply_linop`/`dot`/`nrm2`/`axpy` is likewise fine. No over-claim.

**reachability (graded-stack ch.10) — warning.** The resolution-ladder requires a `roadmap_goal` to carry **pulled-by provenance — ≥1 real inbound *blocking* consumer** as its Axis-2 reachability requirement (`resolution-ladder.md:159-160`). This dispatch is candid that NO blocking `depends-on` consumer wires in this cycle: the named consumers (RE3 deflate/NLEPS, RE8 krylov-iteration view) are c122 dispatches, and the only inbound edge that exists this cycle is the `realizes-kernel-api` `reference`-class edge — which the report itself correctly notes does NOT carry liveness. The report routes this through the grounding disposition (`feedback_gc_ground_dont_remove_future_deps`): a genuinely-wanted future dep of the eigenmode root, grounded as a roadmap_goal rather than left stranded. This is a sanctioned third option, and the report is honest and explicit about the gap. But strictly, the node lands this cycle WITHOUT the blocking inbound consumer the ladder text names as the reachability requirement — so it is flagged `warning` (not `fail`: the grounding disposition is in-discipline and the c122 wiring is concretely flagged), for the repairer/integrator to confirm the grounding framing is the intended disposition and the c122 consumer-wiring flag is carried forward.

### Issues found

1. **[warning] reachability — roadmap_goal lands with no blocking inbound consumer this cycle** (CYCLE.md §Pulled-by, §Open-questions first bullet; `eigsolve-impl.md` frontmatter `reference`/`depends-on` blocks). The `resolution-ladder.md:159-160` pulled-by requirement is "≥1 real inbound *blocking* consumer." The only inbound edge created this cycle is `realizes-kernel-api` (reference-class, non-liveness-bearing). Both blocking consumers (RE3, RE8) are deferred to c122. The report grounds the node via `feedback_gc_ground_dont_remove_future_deps` and flags the c122 wiring explicitly. Severity: low/structural — the disposition is sanctioned and honestly disclosed; the item is to confirm the grounding framing is intended and ensure the c122 consumer-wiring flag survives into the c122 plan. Same gap applies transitively to `lanczos_step` (its only inbound is the `pulled-by` reference edge from eigsolve-impl, itself not yet liveness-anchored).

2. **[warning] lanczos_step body uses `scal` but `scal` is absent from its declared `depends-on` constituents** (`lanczos_step.md` body line `v_next = scal (1 / β_j) w`; frontmatter `depends-on` lists `krylov-step`, `apply_linop`, `dot`, `nrm2`, `axpy` only). `book/src/L1/scal.md` exists on disk (firm). The declared dep list mirrors the `L1/index.md:179` rough-in row (which also omits `scal`), but the constructive body explicitly invokes `scal` for the normalize step, so the well-foundedness dep declaration is incomplete. Severity: low — at rank-0 the dep list is intent-level, but the missing constituent should be added for a complete declared-dependency set (repairable: append `L1/scal` to the `depends-on` block + the dep-map/index rows).

3. **[warning] internally-contradictory integrator instruction for the `lanczos_step` alpha-insert position** (CYCLE.md `edit:book/src/L3/index.md` block, the integrator note ~line 285: "insert ... `lanczos_step` after `ksp_solve`/before `krylov-step`"; and the SUMMARY.md edit block: "`lanczos_step` immediately before the existing `[krylov-step]` line"). Alphabetically `krylov-step` < `ksp_solve` < `lanczos_step` (`kr` < `ks` < `la`), so "after ksp_solve" and "before krylov-step" cannot both hold, and the SUMMARY.md "before krylov-step" placement is not the alpha position (`lanczos_step` should follow `ksp_solve`). Verified against SUMMARY.md (line 121 eigsolve, 122 fold_solve, 123 krylov-step, 124 ksp_solve). Severity: low — an integrator-instruction imprecision, not a content defect; `eigsolve-impl`'s placement (after `eigsolve`, before `fold_solve`) is correct. Repairable by correcting the insert note to place `lanczos_step` after `ksp_solve` in alpha order.

### Note on the kernel-api edit (no issue)

The `edit:book/src/L3/eigsolve.md` `## Status` change was inspected closely given the prompt emphasis: it correctly KEEPS `partial-obstruction`, prepends only the `kernel-api` role-label sentence, preserves the full existing body (verified the `old_string` matches `eigsolve.md:191` verbatim), and the frontmatter-edge handling is explicitly deferred to prose-only with a flagged follow-on (minimal blast radius, authoritative edge declared impl→api). This is the directive-correct disposition — no issue.

## Repair

### Fixes attempted

- **Finding 1 — reachability (warning): roadmap_goal lands with no blocking inbound consumer this cycle.**
  - **Decision**: not-needed (accepted-with-note; NOT a forced edge).
  - **Rationale**: This is the SANCTIONED grounding disposition for a rank-0 `roadmap_goal` — per `resolution-ladder.md:75-76` a rank-0 node may rest on/await anything, and the report routes the missing blocking consumer through `feedback_gc_ground_dont_remove_future_deps` (a genuinely-wanted future dep of the eigenmode root, grounded rather than stranded). Manufacturing a consumer `depends-on` edge to RE3/RE8 would be an UNFAITHFUL edge (those are c122 dispatches that do not exist yet) — strictly out of repair authority. The c122 grounding-trigger the critic asked to be carried forward is ALREADY explicit in the report: §Open-questions first bullet — *"Flag for the c122 planner: the deflate/RE3 and krylov-iteration-view/RE8 consumers should `depends-on` `L3/eigsolve-impl` (and `L3/lanczos_step` via it), firing both roadmap_goals' `roadmap_goal → stub` promotion."* No edit needed; the flag survives into the c122 plan via the integrator's Open-questions promotion. Confirmed the grounding framing is the intended disposition.

- **Finding 2 — lanczos_step body uses `scal` but `scal` absent from declared `depends-on`.**
  - **Decision**: repaired.
  - **Action**: Verified `book/src/L1/scal.md` exists on disk (firm). Added `- target: L1/scal` (`kind: composes`, the normalize step `v_{j+1} = scal (1/β_j) w`) to the `lanczos_step.md` `depends-on` block (CYCLE.md `new:book/src/L3/lanczos_step.md` frontmatter). Also propagated `scal` into the matching `edit:book/src/L3/index.md` dep-map row and the §Evidence BLAS-1-constituents line for consistency. Surgical, faithful — the body line `v_next = scal (1 / β_j) w` was already present; only the declared dep set was incomplete.

- **Finding 3 — internally-contradictory integrator alpha-insert instruction for `lanczos_step`.**
  - **Decision**: repaired.
  - **Action**: Verified the on-disk L3 "Solver capabilities & field transitions" group ordering in `book/src/SUMMARY.md` (lines 121-125): `eigsolve / fold_solve / krylov-step / ksp_solve / orthogonalize`. Correct alpha position for `lanczos_step` is **after `ksp_solve`, before `orthogonalize`** (`la` > `ks` > `kr`, `la` < `or`) — NOT "before krylov-step." Fixed both contradictory notes: the `edit:book/src/L3/index.md` integrator note and the `edit:book/src/SUMMARY.md` insert note now both carry the single consistent instruction (lanczos_step after ksp_solve / before orthogonalize; eigsolve-impl after eigsolve / before fold_solve, which was already correct).

### Unrepairable findings

None. Findings 2 and 3 were mechanical and surgical (repaired in-place); finding 1 is a sanctioned roadmap_goal grounding disposition accepted-with-note (manufacturing a consumer edge would be unfaithful — explicitly out of authority, and not a defect blocking application).

## Suggested resolution

`ready`. Notes for the integrator:
- When promoting this report's Open questions, ensure the **c122 consumer-wiring flag** (RE3 deflate / RE8 krylov-iteration view should `depends-on` `L3/eigsolve-impl`, firing the `roadmap_goal → stub` promotion of both new nodes) lands in the c122 plan / open-questions ledger so the meta-phase RE-recheck and the c122 GC sweep pick it up. Both new nodes (`eigsolve-impl`, `lanczos_step`) land this cycle with liveness resting only on the grounding disposition; if c122 does not wire a blocking consumer, the reachability GC sweep will correctly flag them — that is the intended accountability.
- Alpha-insert positions (verified): `eigsolve-impl` after `eigsolve`; `lanczos_step` after `ksp_solve`, before `orthogonalize`.
