## 2026-05-27 cycle-005 — first cycle under split integrator — 6 wave-1 reports — krylov-step L2 firm + L0 reference-notes bundle 1 + 2 new L1>L0 themes + scalar-promotion concept

- **Phases fired**: plan (cycle-planner haiku → 8 planned, 6 dispatched after main session dropped concepts-sweep wave-2 and combinator-miner wave-2) → dispatch (6× parallel: harvester×1 / abstractor×2 / layer-intro-author×2 / cross-layer-cross-cutter×1) → critique (6× critic) → repair (6× repairer) → **integrate (6× integrator-per-report serial → 1× integrator-finalize; FIRST CYCLE UNDER SPLIT INTEGRATOR — agents added in commit `ccc5082`, required session restart to load new agent defs)** → meta (next).

- **Substantive landed (6 reports, all `ready`)**:
  - `book/src/L2/krylov-step.md` — **L2 firm operator** (promoted from cycle-002 combinator-miner rough-in). Six variant axes (preconditioner-presence, orthogonalization-variant, polynomial-kind, first-iteration-unrolled, restart shape, in-place/out-of-place); all six absorbed at construction time. Algebraic laws including the krylov-subspace invariant K_m(A, b) = span{b, Ab, …, A^(m-1)b}. **Decision NOT to promote any cycle-004 speculative L1 operators** (lanczos_step, three_term_recurrence_update, givens_apply_with_residual_min, bicgstab_step, omega_update, stabilisation_update) recorded in `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md` per the unimplemented-Palace-components policy (cycle-004 meta-phase ask resolution).
  - `book/src/L1-L0/apply-linop-mutation-rotation.md` — new L1>L0 theme; 5 sub-patterns (A: pure-real out-of-place; B: complex out-of-place; C: real in-place / accumulate; D: complex transpose; E: deferred composition). Transpose-mode × accumulate-mode variant axes rectangular.
  - `book/src/L1-L0/axpbypcz-mutation-rotation.md` — new L1>L0 theme; 4 sub-patterns (A/B/C/D) covering scalar-element-type × free-vs-member axes. **First mixed-justification sub-rule in project**: γ==0 sub-rule labelled both `algebraic` (constant-folding) and `structural` (rebind to axpby/axpy form). Methodology-novelty advisory promoted as open question `mixed-justification-sub-rule-methodology` for cross-layer-cross-cutter review.
  - **L0 bootstrap bundle 1** (priority #10): 6 new L0 reference-note chapters + L0/index.md re-framed as "citations + reference notes" overlay:
    - `book/src/L0/output-arg-vs-receiver.md` (calling-convention)
    - `book/src/L0/mfem-vector-types.md` (Vector / ComplexVector / Par* type taxonomy)
    - `book/src/L0/linalg-free-functions.md` (linalg::axpy, linalg::axpby, etc. inventory)
    - `book/src/L0/transparent-vs-load-bearing-tricks.md` (per CLAUDE.md classification rule)
    - `book/src/L0/linalg-vector-file.md` (Vector/ComplexVector file overview)
    - `book/src/L0/ksp-factory-file.md` (KrylovSolver factory file overview)
  - `book/src/concepts/scalar-promotion.md` — new methodology concept page; answers cycle-002 `scalar-promotion-typing-rule` (5 operators were past threshold). Backlinks to axpy/axpby/axpbypcz/scal and `complex-from-real-lift`.
  - `book/src/L0/index.md` — re-framed as L0 = citations + reference-note overlay; Reference-note cohort split into Conventions / File overviews.
  - `book/src/L2/index.md` — krylov-step row promoted rough-in → firm; Working Notes refreshed.
  - `book/src/concepts/index.md` — scalar-promotion row inserted after `scal`.
  - `book/src/SUMMARY.md` — L2 + L1>L0 + L0 + Concepts inserts totaling 10+ chapter rows.
  - `book/src/L1-L0/bicgstab-iteration.md` — cross-reference fix `ksp.cpp:53-56` → `:53-57` at lines 39 and 68 (matches `minres-iteration.md` and new `ksp-factory-file.md`). Folded into L0-bootstrap dispatch per resume-notes flag.
  - `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md` — decision artifact.
  - **Observation-only (no artifact)**: `cross-layer-cross-cutter-krylov-step-placement` recommended DUAL placement for `krylov-step` (L2 + L4 with L4>L3>L2 lowering edge); 4 OQs promoted naming 3 cycle-006 follow-up dispatches.

- **Wave-conflict observations** (captured in `scaffolding/integrator-signals.md`):
  - **SUMMARY.md was the load-bearing convergence point** — 5 of 6 dispatches edited it. Per-report serial dispatch order + "surgical insert preserving append-points" discipline (introduced by dispatch #1's notes; propagated through subsequent dispatch notes) meant **zero collisions**. Each per-report integrator re-read SUMMARY.md fresh and inserted at literal-string anchors. **Validates the per-report serial-dispatch design.**
  - **L1>L0 alphabetical ordering self-resolved** — `apply-linop-mutation-rotation` and `axpbypcz-mutation-rotation` independently picked positions relative to existing `axpby-mutation-rotation`; interleaved correctly via per-report serial dispatch.
  - **No deferrals, no rejections, no rework loops.** All 6 reports applied as-is.

- **Critic findings**: 48 checks total across 6 METAs; ~40 pass / 8 warning / 0 fail. All 8 warnings repaired or correctly classified `not-needed` by repairer.

- **Safety-net gates**: **0 hits cycle-wide.** Retroactive-budget per-slice / global = 0 / 0. Variant-axis-missing = 0 (6 axes for krylov-step, 4 sub-patterns for axpbypcz, transpose×accumulate×element-type for apply_linop, all absorbed). Cross-reference-integrity = 0 post-cross-ref-fix. SUMMARY-chapter-registration-auto-fix applied discretionarily ONCE (concepts/scalar-promotion — outside literal gate scope but matches established pattern).

- **Open questions promoted to ledger**: **28 new** (over 6 reports — high yield reflects the L0 bootstrap scope + krylov-step L2 surfacing L4 routing decisions). Routes: `cross-layer-cross-cutter` (3), `harvester` (4: incl. krylov-step @ L4), `abstractor` (3: incl. L4>L3 lowering), `cycle-planner` (4: routing items), `meta-phase` (3: methodology items), `none / forward-notes` (11).

- **Open questions answered**: **1** — `krylov-step-speculative-l1-promotion-decision` (answered at promotion via `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md`).

- **Build**: `cargo make book` — Build Done in 88.27 seconds, exit 0. Pre-existing katex-link warnings unchanged. No new warnings.

- **Reports applied**:
  - `reports/2026-05-27T025354Z-harvester-krylov-step-L2/` (status: ready; follow_up_agent: null)
  - `reports/2026-05-27T025354Z-abstractor-apply-linop-mutation-rotation/` (status: ready; follow_up_agent: null)
  - `reports/2026-05-27T025354Z-abstractor-axpbypcz-mutation-rotation/` (status: ready; follow_up_agent: cross-layer-cross-cutter / harvester)
  - `reports/2026-05-27T025354Z-layer-intro-author-L0-reference-bootstrap-1/` (status: ready; follow_up_agent: null; multi-cycle bundle continues cycle-006+)
  - `reports/2026-05-27T025354Z-cross-layer-cross-cutter-krylov-step-placement/` (status: ready; follow_up_agent: cycle-planner)
  - `reports/2026-05-27T025354Z-layer-intro-author-scalar-promotion-concept/` (status: ready; follow_up_agent: null)
  - `reports/2026-05-27T070424Z-integrator-finalize-cycle-005/CYCLE.md` — batch report (this finalize).

- **Integrator-signals append**: cycle-005 section prepended above cycle-004 in `scaffolding/integrator-signals.md` (newest-first per file format). Includes first-cycle-under-integrator-split observations (STAGING.md format usability, per-dispatch token budgets, surgical-SUMMARY discipline propagation) and the `concepts/index.md` duplicate-rows finding flagged by dispatch #6 for cycle-006 housekeeping.

- **First-cycle-under-split-integrator notes** (for meta-phase):
  - **Split integrator design validated.** Six per-report dispatches each had bounded scope; staging-log format made aggregation mechanical for finalize; SUMMARY.md serial-write discipline propagated cleanly via notes channel.
  - **New friction-ledger candidate**: `new-agent-defs-need-session-restart` — new `.claude/agents/<name>.md` definitions are not picked up mid-session; required restart this session to load `integrator-per-report` + `integrator-finalize`. Status `addressed-by-restart`. Routes to meta-phase.
  - **Cross-cutter krylov-step DUAL placement** routes 3 cycle-006 follow-up dispatches via `krylov-step-dual-placement-l2-l4-routing` OQ.

- **Resume-notes consumed**: `scaffolding/cycle-005-resume-notes.md` deleted in this commit per its own §"Resuming the session" step 6 instruction ("Delete or archive this resume-notes file once cycle-005 is fully complete").
