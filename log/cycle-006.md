## 2026-05-27 cycle-006 — second cycle under split integrator — 5 reports (4 wave-1 + 1 wave-2) — krylov-step L4 firm + L4>L3 theme + L0 bootstrap bundle 2 + L1 scalar-promotion retroactive-thinning + concepts/index dedup

- **Phases fired**: plan (cycle-planner haiku) → dispatch (4 wave-1 parallel + 1 wave-2 abstractor depending on wave-1 harvester) → critique (5× critic) → repair (5× repairer) → **integrate (5× integrator-per-report serial → 1× integrator-finalize; second cycle under split integrator, first wave-1+wave-2 ordering under split integrator)** → meta (next).

- **Substantive landed (5 reports, all `ready`)**:
  - `book/src/L4/krylov-step.md` — **L4 firm operator** (typed-wrapper companion to cycle-005 L2 entry). Form A: `OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs })`. Form B (first-iteration-unrolled): `first_step` / `steady_step` per `first-iteration-unrolling`. Six variant axes inherited from L2 (preconditioner-presence, orthogonalization-variant, polynomial-kind, first-iteration-unrolled, restart-shape, in-place/out-of-place). Algebraic laws inherited and re-stated at L4 idiom; the demand-pruning law is the only non-trivial property. **L4 dep-map row** added; cycle-006 wave-2 abstractor's two rough-in rows (`iterate_while` + `iterate_while_with_prev`) appended after.
  - `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — **first L4>L3 firm theme**. Four-part wrapper dissolution: (1) record dissolution; (2) monad dissolution; (3) readonly demotion; (4) Form A/B presentation collapse. Includes **audit-section** confirming-with-refinement the cycle-005 OQ `krylov-step-l3-identity-in-form-audit`: "L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence; the L4>L3 hop is non-identity at the wrapper level but the body's dataflow chain survives both hops textually unchanged." Consequence: no L3 `krylov-step` row promoted.
  - **L0 bootstrap bundle 2** (priority #10): 2 new L0 reference-note chapters + L0/index.md grouping addition:
    - `book/src/L0/apply-linop-overload-set.md` — `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult` overload set across Operator/ComplexOperator hierarchy + concrete-subclass family.
    - `book/src/L0/kspsolver-base-class.md` — `BaseKspSolver<OperType>` solver-interface class; anchors L4 `krylov-step` / `solve-monad` to concrete C++ surface.
    - New "Overload sets and class interfaces" L0 grouping (third grouping after Conventions / File overviews).
    - **8 L0 chapters total post-cycle-006** (bundle 1 = 6 + bundle 2 = 2). Threshold for priority #11 (≥6 chapters) now met.
  - **L1 retroactive-thinning** (cycle-005 OQ `scalar-promotion-retroactive-l1-thinning`): 8 verbatim edits across 4 L1 entries (`axpy.md`, `axpby.md`, `axpbypcz.md`, `scal.md`) replacing inline scalar-promotion prose with `concepts/scalar-promotion` backlinks. Per-operator clauses now consolidate at the concept page; thin backlinks at L1. Net prose savings ~290 words; +1 evidence citation enrichment on `axpy.md` Variant axes §.
  - **`book/src/concepts/index.md` dedup** (cycle-005 integrator-signals item): 2 duplicate rows removed (`complex-from-real-lift` pure copy-paste, `solver-as-operator` divergent-kind misclassification — kept `layer-pattern` per concept page's self-description; deleted `primitive` row). File dropped 106→104 lines.
  - `book/src/SUMMARY.md` — 4 surgical chapter inserts (L4 krylov-step, L4>L3 theme, 2× L0 bundle-2).
  - `book/src/L4/index.md` — first firm row promoted (krylov-step) + 2 rough-in rows for iterate_while/iterate_while_with_prev (defanged-to-plain-text at finalize per linkcheck2 surfacing missing files).
  - `book/src/L4-L3/index.md` — placeholder displaced by first real theme-list row (paralleling wave-1's L4/index.md pattern).

- **Wave-conflict observations** (captured in `scaffolding/integrator-signals.md`):
  - **First wave-1 + wave-2 dispatch ordering under split integrator**. The cycle-006 wave-2 abstractor depended on the wave-1 harvester's L4 entry (the "Lowers to" L4>L3 chain references the abstractor's theme; the L4 dep-map row appended after wave-1's firm row). Per-report serial dispatch order honoured: wave-1 first (rows 1-4 of STAGING.md), then wave-2 (row 5). The L4 dep-map at wave-2's edit time already had the wave-1 firm row, so wave-2's two rough-in appends went after it cleanly.
  - **Index-placeholder displacement convention** established cycle-006: when the first real entry lands under a Part that still carries the "(empty — Phase B skeleton.)" placeholder, the per-report integrator discretionarily replaces the placeholder with the first real table row. Pattern applied twice cycle-006 (wave-1 harvester on L4/index.md; wave-2 abstractor on L4-L3/index.md).
  - **No deferrals, no rejections, no rework loops.** All 5 reports applied as-is.

- **Critic findings**: ~40 checks total across 5 METAs; ~32 pass / 8 warning / 0 fail. All warnings repaired or correctly classified `not-needed` by repairer.

- **Safety-net gates**: **0 hits cycle-wide.** Retroactive-budget per-slice = 0 (max per-slice was 1 across the 4 L1 thinning edits; threshold ≥3 not approached). Retroactive-budget global = 0. Variant-axis-missing = 0. Cross-reference-integrity = 0. SUMMARY-chapter-registration-auto-fix not triggered (all 4 chapter creations explicitly proposed SUMMARY edits).

- **Build**: `cargo make book` — Build Done in 88.01 seconds, exit 0. **One build repair**: the cycle-006 wave-2 abstractor's two rough-in L4 dep-map rows initially used `[iterate_while](./iterate_while.md)` markdown links, but those files do not yet exist (rough-in status, anchor pending cycle-007 per OQ `iterate-while-l4-anchor-missing`). mdbook's linkcheck2 treated these as errors and failed the build. Finalize defanged the links to plain-text `iterate_while (rough-in; no anchor yet)` with annotation "anchor file pending cycle-007 harvester promotion per OQ `iterate-while-l4-anchor-missing`". Surgical-minimal repair; preserves intent of the rough-in placement. Pre-existing katex-link warnings unchanged.

- **Open questions promoted to ledger**: **15 new** (over 5 reports; expected high yield given L4 stack work + L0 bootstrap continuation). Includes 1 **closure-note** OQ for the cycle-005 → cycle-006 L3 identity-in-form audit resolution.

- **Open questions answered**: **2** — `krylov-step-l3-identity-in-form-audit` (cycle-005; closed by cycle-006 wave-2 abstractor audit, verdict `confirms-with-refinement`); `krylov-step-l3-row-contingency` (cycle-006 wave-1; resolved by the same audit — contingency did not fire).

- **Cycle-005 integrator-signals items resolved this cycle**:
  - "Pre-existing `concepts/index.md` duplicate rows" — resolved by wave-1 same-layer-cross-cutter dedup.

- **Priorities updated** (per caveat (d)):
  - **#1 harvester-promote-krylov-step**: LANDED cycle-006 (L4 firm; dual-placement complete).
  - **#5 cross-layer-cross-cutter-krylov-step-layer-placement**: RESOLVED cycle-006 (dual-placement decision made coherently across wave-1 harvester + wave-2 abstractor + audit).
  - **#9 scalar-promotion-typing-rule-lift**: PROGRESSED cycle-006 (4 L1 entries retroactive-thinned).
  - **#10 bootstrap-L0-reference-layer**: PROGRESSED cycle-006 (8 chapters total; threshold for #11 met).
  - **#11 retroactive-L1-context-thinning**: NOW ELIGIBLE (≥6 L0 chapters threshold met post-cycle-006).

- **Reports applied** (5 of 5):
  - `reports/2026-05-27T080944Z-harvester-krylov-step-L4/` (status: integrated; follow_up_agent: layer-intro-author for L4 dep-map refresh future cycle)
  - `reports/2026-05-27T081050Z-layer-intro-author-L0-bootstrap-bundle-2/` (status: integrated; follow_up_agent: null; multi-cycle bundle continues cycle-007+)
  - `reports/2026-05-27T080948Z-same-layer-cross-cutter-concepts-index-duplicates/` (status: integrated; follow_up_agent: meta-phase for role-spec stale REPORT.md naming + subagent file-write filter audit)
  - `reports/2026-05-27T081029Z-layer-intro-author-L1-scalar-promotion-thinning/` (status: integrated; follow_up_agent: null; priority #9 progressed)
  - `reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/` (status: integrated; follow_up_agent: abstractor for L3>L2 body-identity theme cycle-007; lowering-verifier for iterate_while L3 trajectory-accumulation gap)
  - `reports/2026-05-27T090849Z-integrator-finalize-cycle-006/CYCLE.md` — batch report (this finalize).

- **Per-report `integrated_at:` inconsistency noted** (per caveat (b) for meta-phase action):
  - Per-report dispatch #1 (harvester krylov-step L4) set `integrated_at: 2026-05-27T09:00:00Z` in its CYCLE.md frontmatter — slightly outside CLAUDE.md write-authority partition (which assigns `integrated_at` touches to integrator-finalize). The other 4 per-report dispatches deferred correctly.
  - Finalize timestamp `2026-05-27T09:08:49Z` overwrites #1's earlier value; all 5 reports now carry the same finalize timestamp + `integration_commit: <sha>`.
  - **Routes to meta-phase**: probable role-spec clarification needed in `.claude/agents/integrator-per-report.md` ("Process" or "What you DO NOT do") to explicitly call out that `integrated_at:` is finalize's domain.

- **Legacy cycle-006.md renamed**: `log/cycle-006.md` (legacy slice-vertical era; 2026-05-24 `back gmres — revise`) renamed to `log/cycle-006-legacy.md` to free the slot for the layered-era cycle-006 entry (this file). Mirrors the cycle-005 `cycle-005-legacy.md` precedent established earlier.

- **Integrator-signals append**: cycle-006 section prepended above cycle-005 in `scaffolding/integrator-signals.md`. Includes second-cycle-under-split-integrator observations (wave-1+wave-2 ordering, index-placeholder-displacement convention, integrated_at write-authority drift, mdbook-linkcheck2-fails-on-rough-in-anchor-missing build issue).

- **Resume-notes consumed**: `scaffolding/cycle-006-resume-notes.md` deleted in this commit per its own §"Resuming the session" step 4 instruction.

- **Mid-cycle directive commit `f661039` NOT part of this finalize**: wave-cap raise 8→12 + MCP reintegration scheduling was committed separately to main during cycle-006 dispatch and is already pushed. Recorded here as context for meta-phase.

- **Two-phase SHA patch** (canonical pattern per role spec process step 13): all 5 reports' `integration_commit: PLACEHOLDER_SHA` are patched in a follow-up commit immediately after finalize commit lands. Message: `patch commit-sha references for cycle-006 finalize commit (<finalize-sha>)`. Same two-phase pattern cycle-004 + cycle-005 used.
