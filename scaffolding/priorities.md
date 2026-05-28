# Priorities

Short next-up list. Meta-phase and cycle-planner co-edit. Cycle-planner reads each cycle to inform dispatch selection.

**Discipline:**
- Keep under 10 items.
- Each item: one line, slug + one-sentence rationale.
- Meta-phase adds when friction-ledger surfaces an actionable target.
- Integrator removes when an item lands in the artifact.

## Now (active) — cycle-013+ (rewritten cycle-012 meta-phase, batch-2 closure)

Batch-2 (cycles 010/011/012) landed: L3 1→8 firm (BLAS-1 cohort closed), L1 8→10 (orthogonalize + chebyshev-smoother), L2 1→2 (chebyshev-iteration; first L2 growth since cycle-005), 8/10 slices reduced, eigsolve OQ cluster fully closed, MCP codemap operational. The list below is the cycle-013+ active surface. Pre-batch-2 landed items (krylov-step dual-placement, apply_linop/axpbypcz L1>L0 themes, matrix-weighted-norm, L0 bundles 1–5, scalar-promotion thinning, MINRES/BiCGStab obstruction policy) are in §Recently landed / git history; removed from the active list per the "keep under 10 items" discipline.

1. **(GATED cycle-013 — highest priority) eigsolve-mutation-rotation Sub-pattern B promotion** — the cycle-012 lowering-verifier audit returned confirms-with-refinement and UNBLOCKS but does NOT enact the `partly-constructive` → fully-firm promotion. The cycle-013 `abstractor` must FIRST apply audit Edit 2 (`GetConverged` public forwarder on `BaseKspSolver` mirroring `GetRelTol()` at `ksp.hpp:64`) + Edit 3 (Sub-pattern A attribution: switch+abort live in `ArpackEigenvalueSolver::SolveInternal`, not `SetWhichEigenpairs`); ONLY THEN drop the `partly-constructive` caveat on `## Status`. OQ `eigsolve-getconverged-forwarder-fix-and-gated-promotion` (cycle-012). This is the first test of whether a `partly-constructive` promotion gate closes (CLAUDE.md §Methodology invariants).
2. **(HEADLINE harvester) l1-divfree-projector-promotion** — cycle-012 batch-3 reduced `divfree.md`; 6 firm entries cite the slice as load-bearing evidence; lift the divergence-free projector to a firm L1 entry, which unblocks further divfree reduction. OQ `l1-divfree-projector-promotion` (cycle-012). Routes to `harvester`.
3. **(harvester) L3 + L4 chebyshev rows** — cycle-012 landed firm `L1/chebyshev-smoother` + `L2/chebyshev-iteration`; full `chebyshev.md` reduction is gated on the L3 (partial-obstruction) + L4 (`ChebOp<E,S>` monadic) rows per the **Identity-lowerings still require both L levels** invariant. OQ `l3-l4-chebyshev-rows-eligible` (cycle-012). Per priority #7 (lower-vocab) and the in-line non-adjacent identity convention (CLAUDE.md), annotate any L3↔L1 identity in-line, not via an `L3-L1/` directory.
4. **(abstractor) orthogonalize + chebyshev lowering themes** — `orthogonalize-mutation-rotation` (L1>L0) + `chebyshev-smoother-mutation-rotation` (L1>L0) / `chebyshev-iteration-fusion` (L2>L1); the firm L1/L2 operators landed cycle-012, their forward lowering themes are unauthored (analogous to firm `ksp-solve-mutation-rotation` / `axpby-mutation-rotation`). OQs `orthogonalize-mutation-rotation-l1-l0-theme` + `chebyshev-l1-l0-and-l2-l1-lowering-themes` (cycle-012). If a sub-part is reconstructed, mark `partly-constructive` per the new invariant.
5. **(same-layer-cross-cutter) phase-1 corpus reduction batch-4** — 8/10 reduced; final 2 slices: `cg_preconditioning_framework` (overlaps `L1/ksp_solve` + `L4/krylov-step` Form A + chebyshev consumer pattern) + `sparse_triangular_solve` (expected out-of-scope-obstruction). OQ `phase-1-corpus-reduction-batch-4-remaining-slices` (cycle-012). **Invoke skill `phase-1-slice-reduction-audit`** (promoted cycle-012; START+END boundary verification + unique-text anchors).
6. **(HEADLINE layer-intro-author) plane-rotation concept-page canonical-pointer repoint** — cycle-012 batch-3 reduced the orthog plane-rotation sub-slice + plane_rotation_stream; 3 firm concept pages still cite the orthog slice as canonical and need re-pointing to the surviving canonical surfaces. OQ `plane-rotation-concept-page-canonical-pointer-repoint` (cycle-012). **Emit proposed-changes blocks; do NOT write to `book/` directly** (cycle-012 prompt-guard — friction-ledger `specialized-agent-direct-write-to-book-during-dispatch`).

## Near (queued)

7. **lower-layer-shared-vocabulary-priority** (user directive 2026-05-27, mid-cycle-009; carried) — prefer populating lower-layer shared utility (L1/L2/L3) over expanding higher-layer vocabulary (L4) when both eligible. **Batch-2 status: substantially discharged** — L3 went 1→8 firm (BLAS-1 cohort), L2 grew 1→2 (first since cycle-005). The cycle-009 "L3 empty" signal is RESOLVED (L3 now has 8 firm operators). Remaining bias-guidance for cycle-013+: keep weighting L1/L2/L3 firm additions and lowering-theme completion above further L4 vocabulary expansion. Friction-ledger `lower-vocabulary-priority-over-higher-expansion` (recurrence-1, addressed; the paired `l3-layer-empty-against-lower-vocabulary-priority` signal is now satisfied).
8. **bootstrap-L4-state-stratification** — write the L4 layer intro / dep-map exposing the sim-state vs operator-params vs ephemeral distinction. Lower-priority than the lower-layer work above per #7.
9. **carry-forward large dispatches** — `gmres.md §L4 v0.6→v0.7 self-rotation` (firms both cycle-008 GMRES + cycle-011 FGMRES sister themes; `lifter`/`abstractor`); L0 bundle-6 candidates #2 + #3 (`layer-intro-author`; #1 landed cycle-011); NLEPS at L1+ (large multi-cycle; `harvester`); `slepc-convergence-reason-lift-sub-theme` (`abstractor`/`lifter`); `spectrum_estimate` L1 rough-in (`harvester`; shares matrix-weighted-norm cohort). Carried from cycles 008/009/011/012 OQs.

## Methodology priorities (codified; addressed — kept for planner reference)

These were active priorities #18–#20 in batch-1; all are now codified in CLAUDE.md §Methodology invariants and watched, not active work items:
- **layer-definition-discipline-high-to-low** (cycle-009 meta) — CLAUDE.md invariant + role-spec touches; watching adherence.
- **phase-1-corpus-reduction-audit** (cycle-009 meta) — CLAUDE.md invariant + skill `phase-1-slice-reduction-audit` (promoted cycle-012); active work tracked under priority #5.
- **identity-lowering-both-levels-backfill** (cycle-009 meta) — CLAUDE.md invariant; krylov-step L3 backfill landed cycle-010, BLAS-1 L3 cohort closed cycle-011. **Companion decision cycle-012 meta**: non-adjacent identity rotations are annotated **in-line**, NOT via an `L3-L1/` directory (CLAUDE.md invariant "Identity rotations across non-adjacent layers are annotated in-line"; friction-ledger `l3-l1-inline-identity-rotation-convention`).
- **partly-constructive theme-status** (cycle-012 meta) — CLAUDE.md invariant + abstractor/lowering-verifier role-spec touches; first gate-close test is priority #1.
- **codemap-mcp** (user enabled option (a) commit `ceb87da`) — pilot succeeded cycle-010, routine cycles 011/012; RESOLVED. MCP-first localization codified in CLAUDE.md §Target system.

## Methodology guidance (user directive 2026-05-27; cycle-003 + cycle-004 update)

- **Dispatch target: up to 12 sub-agents per cycle** (user directive 2026-05-27 — raised from 8 mid-cycle-006 after cycle-005 first-validation of the split integrator showed per-dispatch context stays bounded regardless of wave-mate count). Trajectory: initial 15 target → 8 at cycle-004 → cycle-005 boundary (integrator-token-budget concern at 7 wave-mates pre-split) → 12 mid-cycle-006 (post-split-validation re-expansion). Cycle-004 ran **7 wave-1 dispatches** with zero structural conflict at integration (5 wave-mates appending to `book/src/L1/index.md` cleanly). Cycle-005 ran 6 wave-1 dispatches under the split integrator with zero per-dispatch context-bound friction. Cycle-007+ target: **up to 12 dispatches**. See `.claude/agents/cycle-planner.md` Discipline section.
- **Integrator-to-planner signals channel**: integrator appends to `scaffolding/integrator-signals.md` each cycle (newest at top). Cycle-planner reads the top ~3 entries each cycle. **Validated cycles 003–004** (friction-ledger entry `integrator-signals-channel-working-as-designed`, recurrence-2). 5 of cycle-004's 7 dispatches were sourced verbatim from cycle-003's Suggested next dispatches.
- **`verified_against:` YAML must be fenced** (cycle-003 meta-phase): lowering-verifier emissions of the `verified_against:` block must use a fenced ` ```yaml ... ``` ` code block. See `.claude/agents/lowering-verifier.md` Discipline + friction-ledger entry `lowering-verifier-yaml-in-prose-channel-format`.
- **`layer-intro-author` role broadened** (cycle-003 meta-phase): covers `book/src/concepts/<slug>.md` authorship in addition to layer intros. Cycle-004 first use: `concepts/dot.md` rewrite landed cleanly. See `.claude/agents/layer-intro-author.md`.
- **`layer-intro-author` Vocabulary-cohort subsection template** (cycle-004 meta-phase): when a layer's `index.md` accumulates ≥3 firm operators + ≥1 queued (rough-in / obstruction), include a Vocabulary-cohort subsection that splits the dep-map by firmness state. Template documented in `.claude/agents/layer-intro-author.md` §Vocabulary-cohort subsection. Originated cycle-004 in L1 intro; promote to L2/L3/L4 as those reach the threshold.
- **`addressed-by-design` is NOT a workaround-active category** (cycle-004 meta-phase, user-escalation derived): if a status's mitigation couples orchestration to a quirk, escalate to user; do not file under `addressed-by-design`. See friction-ledger entry `addressed-by-design-misuse-as-workaround-silting`. Meta-phase audits surviving `addressed-by-design` entries per cycle via the counterfactual "if this quirk were removed, what process changes would I make?"
- **REPORT.md → CYCLE.md naming convention** (cycle-004 user-directive rename, commit 8ac1f37): all per-dispatch report files are named `CYCLE.md`. Content-pattern Write filter is bypassed; subagents Write directly. Skill `embed-and-persist-subagent-dispatch` is retired (kept as historical). Watch-list note: monitor other Claude Code projects for the same filter and apply the same repair pattern if it recurs.

## Watch list (deferred)

- **haiku-cycle-planner-cascade-pattern** — addressed across cycles 003–004 by user directive 8fc3a07. Cycle-004 planner ran 7 dispatches cleanly with parallel-when-in-doubt; no over-scoping observed. **Status: monitoring only**; demote from watch list if cycle-005 also clean.
- **scalar-promotion-typing-rule lift** — open question `scalar-promotion-typing-rule`: now **5 operators** (`axpy`, `dot`, `axpby`, `axpbypcz`, `scal`). Promoted to active priority #9 above.
- **l2-dep-map-format-vs-l1** — open question `l2-dep-map-format-vs-l1`: decide whether the L2 Working-Notes overflow is reusable across L2/L3/L4 dep-maps or a fifth column is cleaner. Routes back to meta-phase / channel-format change.
- **axpby-corpus-coverage-exhaustive-indexing** — open question (cycle-003): the cycle-003 lowering-verifier deferred ~25 uncited corpus sites + 3 defined-not-used L0 forms for future exhaustive indexing. Defer until L1 vocabulary fully firm.
- **Obstruction-theme tooling decision** — cycle-004 introduced `justification kind: obstruction` as a new L1>L0 theme category. Cross-layer-cross-cutter consumers should treat these differently (skip evidence-walking; surface as "anticipated work"). Meta-phase to write a channel-format spec when the cross-layer-cross-cutter dispatch first encounters one.
- **Other Claude Code project filter-repair pattern** — watch-list note: if other projects we work on hit the same content-pattern Write filter on REPORT/summary/findings/analysis files, apply the cycle-004 rename pattern (project-wide rename to non-keyword filename + retire workaround skills).
- Phase 1 slice corpus move to `book/src/_phase1_corpus/` — 64 cross-references need rewriting; defer until pilot validates flow.
- `lessons.md` retirement — keep as historical record post-Phase-E.

## Recently landed

**Cycle-004 (commit b8332b9 + ed50d6e + 8ac1f37):**

- **concepts-dot-rewrite** — `book/src/concepts/dot.md` rewritten to align with L1/dot.md authoritative entry; closes 4 open questions on dot contradictions.
- **L1-index-refresh** — `book/src/L1/index.md` intro + dep-map refreshed; **Vocabulary-cohort subsection pattern originated here** (now in layer-intro-author role spec).
- **harvester-scal-L1** — `book/src/L1/scal.md` firm; module-axiom laws + scalar-promotion sub-axis.
- **harvester-apply_linop-L1** — `book/src/L1/apply_linop.md` firm; gates krylov-step (now unblocked).
- **harvester-axpbypcz-L1** — `book/src/L1/axpbypcz.md` firm; 12 laws + 1 internal-L0 control-flow axis explicitly non-L1.
- **abstractor-MINRES-L1-L0-obstruction** — `book/src/L1-L0/minres-iteration.md` obstruction theme; first instance of new `justification kind: obstruction` category.
- **abstractor-BiCGStab-L1-L0-obstruction** — `book/src/L1-L0/bicgstab-iteration.md` obstruction theme; second instance, recurrence-2 of `advertised-but-unimplemented-krylov-solvers`.
- **filter-repair-rename** (commit 8ac1f37) — project-wide `REPORT.md → CYCLE.md` rename, dodging the content-pattern Write filter. Skill `embed-and-persist-subagent-dispatch` retired.

**Cycle-003 (commit 9aa1c59):**

- **bootstrap-L1-nrm2** — `book/src/L1/nrm2.md` firm (10 algebraic laws + 4 non-laws; 1 variant axis with element-type collapse).
- **bootstrap-L1-axpby** — `book/src/L1/axpby.md` firm (9 laws + 4 non-laws; 2 variant axes; fused-primitive decision in `scaffolding/decisions/axpby-as-primitive.md`).
- **lowering-verifier-axpby-mutation-rotation** — `verified_against:` block (9 per-citation audit rows); fence-required discipline now enforced.
- **same-layer-cross-cutter-dot-concept-contradictions** — surfaced the 3 contradictions resolved cycle-004.

**Cycle-002 (commit c3312a6) + pilot-1:**

- **post-restart-verify-claude-agents** — all 13 custom `.claude/agents/<name>.md` definitions resolve via `Agent(subagent_type=<name>)`.
- **bootstrap-L1-L0-theme-axpby** — abstractor rough-in `axpby-mutation-rotation` theme landed; audited cycle-003.
- **mine-krylov-iteration-step** — combinator-miner rough-in `krylov-step` at `book/src/L2/index.md`. **Now unblocked** for harvester promotion (priority #1).
- **bootstrap-L1-axpy** (pilot-1) — `book/src/L1/axpy.md` firm.
- **bootstrap-L1-dot** (cycle-002) — `book/src/L1/dot.md` firm.
