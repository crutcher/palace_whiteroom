---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-08T193500Z
scope: maintenance-floor — batch-46 once-per-batch full-hygiene sweep (cycle-142 OPENER)
status: pending
integrated_at: 2026-06-08T194000Z
integration_commit: 234257e
integration_notes: |
  Applied clean by integrator-per-report (cycle-142 staging, single row, status applied).
  Audit-class clean-bill maintenance-floor full-hygiene sweep for batch-46 OPENER (WIND-TO-MAINTENANCE);
  NO `book/` artifact mutation (no proposed-changes / no dep-map / no node/edge/rank/status move).
  The lone load-bearing per-report gate — graded-stack baseline confirmation — re-ran at finalize and
  HELD EXACTLY vs the batch-45 terminal (files 392 / typed 331 / untyped 61 / roots 45 /
  rank_violations 0 / unresolved_depends_on_targets 0 / promotion_frontier 12 / reachable 163 /
  reference_reachable 247 / detritus 123 / true_detritus 51 / expected_unreachable_outside_dag 54).
  Build EXIT 0, zero build-repairs; step-5c KaTeX `$`-sigil `<pre>` assertion PASS (0 hits across 392 HTML).
---

# CYCLE: Maintenance-floor full-hygiene sweep — batch-46 (cycle-142 OPENER)

## Summary
The single per-batch maintenance dispatch for batch-46 (the WIND-TO-MAINTENANCE batch, 6th-consecutive
in-scope steady-state-complete). I ran the six-part full-hygiene sweep against the on-disk book (the c141
terminal — the most recent `book/src/` commit is `9ae9dbc`, the batch-45 BATCH-CLOSING; batch-46 has
dispatched NO substantive producer, only the cycle-142 planner). **CLEAN BILL.** All 12 graded-stack
baseline totals match the batch-45 terminal EXACTLY; the two hard invariants (`rank_violations == 0`,
`unresolved_depends_on_targets == 0`) hold on disk. The 3 `realizes-kernel-api` edges stay `reference`-class
on disk; the Synthesis `#extern` leaves trace to the kernel-API nodes (no fabricated impl); the semantic
surface §0.1 discipline is intact with no new restatement cohort (batch-46 authors NO vocabulary); the
DIRECTIVE-1 MPI boundary holds (no active-work lift). The eigsolve-impl promotion gate remains NON-FIRING.
The detritus escalate-guard is NOT tripped (stable 123/51). No flagged residuals, no newly-typeable
detritus node, no drift, no divergence. No OQ append warranted — a clean bill is the honest result for a
maintenance-batch opener at 6th-consecutive in-scope completeness.

## Observation kind
**Audit residue** — clean-bill maintenance sweep. No coverage gap, no edge-label mismatch, no consistency
drift, no vocabulary mismatch, no audit residue requiring action surfaced. This is the expected steady-state
outcome for a WIND-TO-MAINTENANCE batch opener.

## Specific finding

### Check 1 — Graded-stack lint `--json` totals re-confirmation: BASELINE HOLDS EXACTLY
Ran `python3 tools/graded-stack-lint/graded_stack_lint.py --json`. Every forecast/expected field
(the batch-45 terminal, the planner's on-disk-verified snapshot) matches on disk:

| field | batch-45 terminal | on-disk c142 | match |
|---|---|---|---|
| files | 392 | 392 | OK |
| typed | 331 | 331 | OK |
| untyped | 61 | 61 | OK |
| roots | 45 | 45 | OK |
| **rank_violations** | **0** | **0** | **OK (hard invariant)** |
| **unresolved_depends_on_targets** | **0** | **0** | **OK (hard invariant)** |
| promotion_frontier | 12 | 12 | OK |
| reachable | 163 | 163 | OK |
| reference_reachable | 247 | 247 | OK |
| detritus | 123 | 123 | OK |
| true_detritus | 51 | 51 | OK |
| expected_unreachable_outside_dag | 54 | 54 | OK |

Both hard invariants hold on disk. Rank histogram on disk: `firm 224, rough-in 4, partly-constructive 3,
obstruction 2, partial-obstruction 4, roadmap_goal 4, stub 1, typed-no-rank 89` — consistent with the
batch-45-complete state. NO divergence. (The batch-46 cycle is a maintenance batch with no node/edge/rank
move forecast; the baseline is expected to HOLD across the batch.)

### Check 2 — RE-set premise re-check: ALL TERMINAL PREMISES HOLD
The most recent `book/src/` commit is `9ae9dbc` (c141 batch-45 close; citation-prefix hygiene on
`L4/sharding-decompose-reduce`, "no node/edge/rank move"). **No book frontmatter status/rank changed since
the batch-45 terminal** — so every RE baseline-exception's "no faithful inbound `depends-on` consumer"
premise is unchanged. Nothing firmed → no RE promotion-condition fired on disk.

- **RE4** (`L2/incremental-least-squares`, `L2-L1/incremental-least-squares-composition-lowering`) —
  consumer-gated; premise HOLDS. No GMRES-variant feature/driver column exists on disk or in flight; the
  running-QR / Givens stream has no named L2-altitude constituent consumer. Stays correctly baseline-excepted.
- **The sharding §2g-extension member** (`L4/sharding-decompose-reduce`, rank-0 `roadmap_goal`) —
  solve-generalization-consumer-gated; premise HOLDS. Frontmatter on disk `status: roadmap_goal / rank:
  roadmap_goal`; it sits in the `true_detritus` / `no_typed_edges` bucket as a reference-EMITTING leaf (per
  the batch-43 §2g EXTENSION). No single-machine-valid domain-decomposition-preconditioner consumer is in
  flight; DIRECTIVE-1 keeps MPI/distributed OUT, so the solve-generalization promotion pull stays DEFERRED.
- **RE11 deliberate-reference-only-reachable cohort** (the kernel-impls + lowering themes + combinator-primary
  leaves + AMR reference-reachable verbs + the synthesis `expected_unreachable_outside_dag` chapters) —
  §2g-accounted by design. The `detritus_reference_reachable_re11_cohort` stands at 72 (unchanged). No climb;
  the §2g escalate-guard does NOT fire.
- **eigsolve-impl promotion gate — NON-FIRING (re-confirmed on disk).** Both arms remain unsatisfiable:
  - **Arm A** (positive structure) is **unsatisfiable from the present `palace/` corpus**: `lanczos_step`'s
    symmetric three-term recurrence is literature-anchored (Paige–Saunders), NOT a Palace L0 site — its L0
    home is the MINRES `obstruction (enum-only-stub)` (`KrylovSolver::MINRES → MFEM_ABORT`,
    `palace/linalg/ksp.cpp:53-57`; no `MinresSolver<OperType>` class; no test linkage). `lanczos_step`
    correctly STAYS `roadmap_goal` (`book/src/L3/lanczos_step.md:5-6,81-86`).
  - **Arm B** (blocking consumer) not in flight: `eigsolve-impl` is itself co-`roadmap_goal`; the RE3
    deflate / RE8 krylov-iteration blocking-`depends-on` consumer has not materialized
    (`book/src/L3/eigsolve-impl.md:122-125`).

### Check 3 — Kernel-API/impl `realizes-kernel-api` integrity (DIRECTIVE-3): ALL 3 EDGES `reference`-CLASS
Grepped the three impl chapters; each `realizes-kernel-api` edge sits under `edges.reference:`, never
`depends-on`:
- `book/src/L1/libceed-quadrature-kernel-impl.md:20-23` — `reference: target:
  L1-L0/fe-assemble-libceed-boundary-obstruction, kind: realizes-kernel-api` (free, navigational; the impl
  is `rank: firm`, blocking `depends-on` go to its tensor-contraction constituents).
- `book/src/L3/eigsolve-impl.md:19-23` — `reference:` carries TWO `realizes-kernel-api` edges (→ `L3/eigsolve`
  AND → `L4/eigsolve`), both `reference`-class; the node is rank-0 `roadmap_goal`; its blocking `depends-on`
  edges go to `L3/krylov-step` / `L3/lanczos_step` / `L3/ksp_solve` / `L3/apply_linop` / `L2/orthogonalize`.
- `book/src/L1/multigrid-relaxation-smoother.md:24-26` — `reference: target:
  L1-L0/triangular-solve-obstruction, kind: realizes-kernel-api` (free, NOT depends-on); node is `rank: firm`,
  blocking deps to its firm point-smoother / matvec / interpolator constituents.

All three keep the opaque kernel-API as a reviewed CORRESPONDENCE (reference-class), not a build dependency.
None mis-typed `depends-on`; no impl deleted/downgraded its API surface. DIRECTIVE-3 mechanics intact.

**Synthesis `#extern` leaves trace to the kernel-API nodes (not claiming an impl):** the Synthesis Part
renders the three opaque kernels as `#extern` after their type signature, each linking the kernel-API node:
- `synthesis/data-algebra.md:167-194` — `fe_assemble` renders `#extern assemble_term`, linking the
  `fe-assemble-libceed-boundary-obstruction` kernel-API node.
- `synthesis/coordination.md:236-255` — `eigsolve` renders `#extern eigen_iterate` (the SLEPc EPS loop),
  the kernel-API surface, with the constructive `eigsolve-impl` deep-linked as the realization.
- `synthesis/coordination.md:308-331` — `fold_solve` renders `#extern time_step_op` (the opaque MFEM
  ODESolver per-step boundary).
- `synthesis/index.md:55` states the rendering rule explicitly ("`#extern NAME` in place of its
  implementation def, after its type signature … Do NOT lift the opaque kernel into a fabricated def").
The `#extern` leaves correctly render the opaque boundary, NOT a fabricated impl. Intact.

### Check 4 — Semantic-surface liveness drift: NO DRIFT, NO NEW RESTATEMENT COHORT
- `book/src/semantics/index.md` §0.1 active-management discipline present and intact (`:3` the
  SEMANTIC-CONSOLIDATION directive banner; `:24` the §0.1 active-management section). The USE+LINK-don't-restate
  rule is stated as the surface's governing discipline.
- No new restatement cohort surfaced. Batch-46 authors NO new vocabulary (it is a maintenance batch), so there
  is no functional-unit entry that could restate a general semantic rule this cycle.
- No source contradiction. `SUMMARY.md` wiring intact: the top-level Part ordering is correct —
  `# Synthesis` (`:10`) → `# Feature surfaces` (`:17`) → `# Semantic surface` (`:68`) → (the `# L4` Part
  follows), matching the CLAUDE.md SYNTHESIS/SEMANTIC ordering directives.
- `semantics/index` appears in the `untyped (61)` set, as expected (a documentation surface outside the typed
  dep-graph, part of `expected_unreachable_outside_dag = 54`) — not a decay signal.

### Check 5 — Opportunistic detritus / edge-typing GC: ESCALATE-GUARD NOT TRIPPED; NO NEWLY-TYPEABLE NODE
- `detritus 123 / true_detritus 51 / detritus_reference_reachable_re11_cohort 72 / stronger_signal_true_detritus 7`
  — ALL stable at the batch-45 terminal. No climb → the §2g escalate-guard does NOT fire.
- The `true_detritus (51)` set is dominated by the consumer-gated false-detritus cohorts that
  **GROUND-don't-remove** (`feedback_gc_ground_dont_remove_future_deps`): the GMG/AMR + eigsolve-impl/NLEPS
  consumer-gated nodes (genuine future-dependencies of reachable goal nodes that collapse to reachable only
  when a blocking `depends-on` consumer wires in) + the sharding §2g-extension member + the RE4 GMRES-variant
  ILS view. NONE is genuine detritus to remove; each carries a concrete non-fix-forward promotion condition in
  `scaffolding/graded-stack-baseline-exceptions.md`.
- **No node is now cleanly typeable.** Batch-46 firms nothing and adds no consumer, so no previously-detritus
  node has gained a faithful inbound `depends-on` this batch. No FLAG warranted. (Per role discipline I do NOT
  force or remove — and there is nothing to ground here this batch.)

### Check 6 — DIRECTIVE-1 boundary re-confirmation: MPI VERSION NOT LIFTED (clean steady-state)
- Batch-46 dispatches NO sharding/MPI work — the only batch-46 report directory is
  `reports/2026-06-08T193000Z-cycle-planner-cycle-142/` (the planner's own plan). No producer dispatch lifts
  the MPI-associated version (`linalg/rap.*` RAP / `utils/geodata.cpp` distribution / the MPI collectives
  `linalg/vector.hpp`, `utils/communication.hpp`) as active work.
- `scaffolding/priorities.md` carries the DIRECTIVE-1 boundary statements (`:39` "STILL IN FORCE … catch
  it"; `:59` "MPI/distributed OUT"; the (B)/(D) sharding candidate directions explicitly gated as
  consumer-not-in-flight / DIRECTIVE-1-keeps-MPI-OUT). The grep for `rap.|geodata|ParOperator|
  communication.hpp|MPI` over priorities.md returns ONLY these boundary/deferred-future statements — zero
  active-work MPI items.
- The human resolution `cb5592a` records batch-46 = (A) wind to maintenance; no re-scope of DIRECTIVE-1.
DIRECTIVE-1 boundary intact — clean steady-state re-confirmation.

## Recommendation
**Defer — clean-bill maintenance sweep; no immediate action required of the batch-46 meta-phase.** All six
checks PASS on disk. The two hard invariants hold; the 3 kernel-API edges are `reference`-class; the Synthesis
`#extern` leaves are faithful; the semantic surface is undrifted; the detritus escalate-guard is stable; the
DIRECTIVE-1 boundary holds. This is the expected steady-state result for a WIND-TO-MAINTENANCE batch opener at
6th-consecutive in-scope completeness — the maintenance floor is grounded. The per-cycle `integrator-finalize`
step-5b tripwire (the two-invariant floor) remains the per-cycle confirmation for c143/c144; this sweep is the
per-batch full-hygiene baseline.

## Supporting evidence
- Linter: `python3 tools/graded-stack-lint/graded_stack_lint.py --json` (run 2026-06-08; totals table §Check 1;
  all 12 fields match the batch-45 terminal).
- Kernel-API edges: `book/src/L1/libceed-quadrature-kernel-impl.md:20-23`,
  `book/src/L3/eigsolve-impl.md:19-23`, `book/src/L1/multigrid-relaxation-smoother.md:24-26` (all
  `realizes-kernel-api` under `edges.reference:`).
- Synthesis `#extern`: `book/src/synthesis/index.md:55`, `synthesis/data-algebra.md:167-194`,
  `synthesis/coordination.md:236-255,308-331`.
- Semantic surface: `book/src/semantics/index.md:3,24` (§0.1 discipline); `book/src/SUMMARY.md:10,17,68`
  (Part ordering).
- eigsolve-impl gate: `book/src/L3/lanczos_step.md:5-6,81-86` (arm-A unsatisfiable, MINRES enum-only-stub
  `palace/linalg/ksp.cpp:53-57`); `book/src/L3/eigsolve-impl.md:122-125` (arm-B not in flight).
- RE-set: `scaffolding/graded-stack-baseline-exceptions.md` (terminal state: RE4 residual consumer-gated, the
  sharding §2g-extension member, RE11 deliberate-reference-only-reachable; original RE1-RE10 9-of-10
  discharged/grounded).
- DIRECTIVE-1: `scaffolding/priorities.md:39,59` (boundary statements, no active MPI item); `git log` HEAD =
  `cb5592a` (batch-46 = (A) wind to maintenance); only batch-46 report dir is the planner's.
- Git provenance: last `book/src/` commit is `9ae9dbc` (c141 batch-45 close, no node/edge/rank move) → all RE
  and frontmatter premises unchanged since the batch-45 terminal.

## Open questions / caveats
- No OQ append warranted — no new observation surfaced (no newly-typeable detritus node, no drift, no
  divergence). A clean bill is the honest result; I did not manufacture a finding.
- The on-disk state is the c141 terminal; batch-46 has dispatched no producer. As batch-46 cycles run
  (maintenance-floor consolidation only), the `integrator-finalize` step-5b per-cycle tripwire is the
  authoritative per-cycle confirmation that the two hard invariants continue to hold. This sweep is the
  per-batch baseline; the forecast is HOLD-EXACTLY across the batch (no node/edge/rank move planned).
