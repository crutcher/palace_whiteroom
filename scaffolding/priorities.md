# Priorities

Short next-up list. Meta-phase and cycle-planner co-edit. Cycle-planner reads each cycle to inform dispatch selection.

**Discipline:**
- Keep under 10 items.
- Each item: one line, slug + one-sentence rationale.
- Meta-phase adds when friction-ledger surfaces an actionable target.
- Integrator removes when an item lands in the artifact.

## Now (active) — cycle-016+ (rewritten cycle-015 meta-phase, batch-3 closure)

Batch-3 (cycles 013/014/015) landed: the FULL `partly-constructive` lifecycle (eigsolve EXIT cycle-013, divfree→firm + chebyshev-L4→firm ENACT cycle-015; L1 firm 10→11, L4 firm 3→4); 2 new firm L1>L0 + 1 L2>L1 lowering themes (orthogonalize + chebyshev) cycle-013; chebyshev L3 partial-obstruction + the full chebyshev slice REMOVAL (corpus removals 8/10→9/10); L0 bundle-6 chapters #2/#3/#4 (`linalg-rap-file`, `linalg-orthog-file`, `fem-bilinearform-file`); the cg.md citation sweep across the L4>L3 theme + L3/krylov-step entry. The list below is the cycle-016+ active surface (carry-forward OQs the cycle-015 finalize flagged). Landed batch-3 items are in §Recently landed / git history; removed from the active list per the "keep under 10 items" discipline.

1. **(abstractor — HEADLINE) divfree-projector L1>L0 mutation-rotation theme** — now that `book/src/L1/divfree-projector.md` is **firm** (promoted cycle-015), author the L1>L0 lowering theme `divfree-projector-mutation-rotation` on a firm foundation (the WeakDiv-sign contradiction is resolved at the L1-entry level). Closes the long-standing divfree L1>L0 gap. OQ + cycle-015 STAGING row 1. **Self-verify every citation before emitting** (cycle-015 producer-citation-drift bullet).
2. **(lifter — small) l4-chebyshev-residual-formm-foldm-prose-cleanup** — 3 stale `forM_`/`foldM` prose mentions remain in `book/src/L4/chebyshev.md` (~L368/L382/L547) outside the cycle-015 re-anchor blocks; surgical 3-site prose refresh naming `iterate_while_pure`/`iterate_while_pure_L3`. Sibling: `l3-chebyshev-downward-prose-iterate-while-refresh` (`book/src/L3/chebyshev.md:236-238`). OQs (cycle-015).
3. **(lifter) l4-krylov-step-cg-md-citation-sweep + l2-krylov-step-cg-md-citation-sweep** — the cycle-015 L3 sweep found the SAME dangling `cg.md` pointers persist in the DISTINCT `L4/krylov-step.md` (8 pointers) and `L2/krylov-step.md` (12 pointers) operator entries; sibling sweeps applying the cycle-013/014/015 lifted-evidence convention. OQs (cycle-015). **Self-verify relocated pointers land at the TERMINAL firm home** (cycle-015 lifter citation bullet) — cycle-015 the L3 sweep pointed 2 re-anchors at relocated-dangle targets.
4. **(layer-intro-author) bundle-6 #5 fem/libceed/operator.cpp** — bundle-6 #4 (`fem-bilinearform-file`) landed cycle-015; next ranked candidate is `fem/libceed/operator.cpp` (verified callee defs `CeedOperatorFullAssemble`@:455 + `CeedOperatorCoarsen`@:525). Also retires the deliberate plain-text non-link reference in `fem-bilinearform-file.md` (convert to a live link once the chapter exists). OQ `bundle-6-l0-libceed-operator-file-next-candidate` (cycle-015). **L0 bundle chapters are citation-dense — self-verify each range** (cycle-015 layer-intro-author bullet); **emit proposed-changes blocks, do NOT write `book/` directly**.
5. **(lifter/cross-layer-cross-cutter) divfree.hpp doc-tension OQ** — the residual divfree header/doc-comment tension surfaced during the cycle-014/015 divfree firming; resolve or document. Carry-forward OQ.

## Near (queued)

6. **lower-layer-shared-vocabulary-priority** (user directive 2026-05-27, mid-cycle-009; carried) — prefer populating lower-layer shared utility (L1/L2/L3) over expanding higher-layer vocabulary (L4) when both eligible. **Status: substantially discharged across batch-2+3** — L3 went 1→8 firm (BLAS-1 cohort), L2 1→2, L1 10→11 (divfree-projector cycle-015); the cycle-009 "L3 empty" signal is RESOLVED. Remaining bias-guidance for cycle-016+: keep weighting L1/L2/L3 firm additions and lowering-theme completion above further L4 vocabulary expansion. Friction-ledger `lower-vocabulary-priority-over-higher-expansion` (addressed).
7. **bootstrap-L4-state-stratification** — write the L4 layer intro / dep-map exposing the sim-state vs operator-params vs ephemeral distinction. Lower-priority than the lower-layer work above per #6.
8. **carry-forward large dispatches** — `gmres.md §L4 v0.6→v0.7 self-rotation` (firms both cycle-008 GMRES + cycle-011 FGMRES sister themes; `lifter`/`abstractor`); NLEPS at L1+ (large multi-cycle; `harvester`); `slepc-convergence-reason-lift-sub-theme` (`abstractor`/`lifter`); `spectrum_estimate` L1 rough-in (`harvester`; shares matrix-weighted-norm cohort); `chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep` (firm L1/L2 chebyshev anchor reconcile; `lifter`). Carried from cycles 008/009/011/012/013/014 OQs.

## Methodology priorities (codified; addressed — kept for planner reference)

These were active priorities #18–#20 in batch-1; all are now codified in CLAUDE.md §Methodology invariants and watched, not active work items:
- **layer-definition-discipline-high-to-low** (cycle-009 meta) — CLAUDE.md invariant + role-spec touches; watching adherence.
- **phase-1-corpus-reduction-audit** (cycle-009 meta) — CLAUDE.md invariant + skill `phase-1-slice-reduction-audit` (promoted cycle-012); active work tracked under priority #5.
- **identity-lowering-both-levels-backfill** (cycle-009 meta) — CLAUDE.md invariant; krylov-step L3 backfill landed cycle-010, BLAS-1 L3 cohort closed cycle-011. **Companion decision cycle-012 meta**: non-adjacent identity rotations are annotated **in-line**, NOT via an `L3-L1/` directory (CLAUDE.md invariant "Identity rotations across non-adjacent layers are annotated in-line"; friction-ledger `l3-l1-inline-identity-rotation-convention`).
- **partly-constructive theme-status** (cycle-012 meta) — CLAUDE.md invariant + abstractor/lowering-verifier role-spec touches. **VALIDATED-BY-USE batch-3** (cycle-015 meta): the full lifecycle closed 3× cleanly (eigsolve EXIT cycle-013, divfree + chebyshev-L4 ENACT cycle-015, convergence-mapping correctly STAYS); the gate CLOSES (transient, not an escape hatch). Skill `partly-constructive-promotion-checklist` promoted cycle-015 + abstractor §Discipline 4-point-checklist bullet added. Friction-ledger `partly-constructive-lowering-theme-status` (validated-by-use).
- **producer-citation-self-verification** (cycle-015 meta) — the strongest batch-3 friction; 4 producer role-spec self-verification bullets (harvester/abstractor/lifter/layer-intro-author) + `verify-citation-range` skill §"Producer self-verification" section. A mechanical codemap-backed citation-range checker tool is an OPEN ASK to the user (tooling/code change). Friction-ledger `producer-citation-drift-verify-not-self-invoked`.
- **slice-removal non-link-grep** (cycle-015 meta) — `phase-1-slice-reduction-audit` skill extended with a removal-specific non-link prose-reference grep step (slice REMOVALS strand bare-path/inline-code prose refs the build linkcheck can't catch). Friction-ledger `slice-removal-non-link-prose-reference-grep-gap`.
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
