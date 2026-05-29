# Priorities

Short next-up list. Meta-phase and cycle-planner co-edit. Cycle-planner reads each cycle to inform dispatch selection.

**Discipline:**
- Keep under 10 items.
- Each item: one line, slug + one-sentence rationale.
- Meta-phase adds when friction-ledger surfaces an actionable target.
- Integrator removes when an item lands in the artifact.

## Now (active) — cycle-019+ (rewritten cycle-018 meta-phase, batch-4 closure)

Batch-4 (cycles 016/017/018) landed: the divfree-projector L1>L0 mutation-rotation theme (firm; L1>L0 themes 10→11) + L0 bundle-6 #5 `fem-libceed-operator-file` (L0 20→21) cycle-016; the krylov-step `cg.md` re-anchor chain FULLY TERMINATED (L4 + L2 + L3-L2 body-identity sweeps) and the chebyshev `forM_`/`foldM`→`iterate_while` vocabulary-lag cohort FULLY TERMINATED (L4 + L3 sweeps) across 016/017; the eigsolve-convergence-reason-mapping THIRD re-verification (correctly STAYS partly-constructive); and the **human-raised BLAS-1 variadic-fold unification fully ENACTED** — `linear_combination` L2 rough-in (017)→firm (018) + `linear-combination-fold-specialization` L2>L1 theme + `inner_product` L2 rough-in (the conjugation-convention sibling) + the `nested-constructed-operator-gate` concept page + the divfree "first→third" provenance correction (018). L2 firm 2→3, L2>L1 firm 1→2, +1 concept page. The list below is the cycle-019+ active surface (carry-forward OQs the cycle-018 finalize flagged + the cycle-018 integrator-signals suggested dispatches). Landed batch-4 items are in git history; removed from the active list per the "keep under 10 items" discipline. **The combinator-miner parametric/variadic-family detection mode (BLAS-1 prong-a) was ENACTED by THIS meta-phase** — see §Methodology priorities; it is no longer a priority item.

1. **(harvester — HEADLINE) `inner_product` L2 firm operator** — the cycle-018 combinator-miner landed the `inner_product` rough-in dep-map row (≥3-instance bar met: `dot`/`tdot`/`bilinear-form`; the conjugation-convention sibling fold of `linear_combination`, `(Tensor[N], Tensor[N]) -> Scalar`, M-weighted member `xᴴ M y`). Author `book/src/L2/inner_product.md` directly off the rough-in row, mirroring how cycle-018's harvester firmed `linear_combination` off the cycle-017 rough-in. **Pin the conjugation / arg-order convention** (`Dot(comm,x,A,y) = yᴴ A x`). OQ `inner-product-harvester-formalization-and-conjugation-pinning`. **Self-verify every citation before emitting**; **forward-references to not-yet-authored siblings stay plain-text** (cycle-018 conventions).
2. **(abstractor) `L2-L1/inner-product-fold-specialization` theme + `linear-combination-fold-specialization-theme-followups`** — the L2>L1 lowering theme taking the L2 `inner_product` fold into its L1 specializations (mirrors the cycle-018 `linear-combination-fold-specialization` pairing); plus the carry-forward follow-ups on the just-landed `linear-combination-fold-specialization` theme. OQs (cycle-018).
3. **(lifter/abstractor — large carry-forward) `gmres.md §L4 v0.6→v0.7` self-rotation** — firms both the cycle-008 GMRES + cycle-011 FGMRES sister themes; recurring across batches. Large; carried from cycles 008/011 OQs + cycle-018 suggested dispatches.
4. **(harvester — large carry-forward) NLEPS at L1+** — large multi-cycle. Carried.
5. **(layer-intro-author) bundle-6 #6 L0 candidate — `fespace.{hpp,cpp}`** — input-side FE-space L0 anchor; next ranked bundle-6 chapter after the cycle-016 `fem-libceed-operator-file`. OQ. **L0 bundle chapters are citation-dense — self-verify each range; emit proposed-changes blocks, do NOT write `book/` directly** (cycle-018 universal dispatch-phase write-guard).
6. **(lifter/cross-layer-cross-cutter) divfree.hpp doc-tension OQ** — residual divfree header/doc-comment tension (`divfree-mult-doc-irrotational-vs-divfree-stale`); resolve or document. Carry-forward OQ from batches 3/4.
7. **(combinator-miner — try the NEW family-mode) candidate parametric families** — with the cycle-018 parametric/variadic-family detection mode now in the spec, scan for the next parametric family (the `inner_product` conjugation cohort is the obvious near-term test; longer-term, smoother/preconditioner families). First live exercise of the new mode. Friction-ledger `combinator-miner-arity-blind-parametric-family-detection`.

## Near (queued)

8. **lower-layer-shared-vocabulary-priority** (user directive 2026-05-27, mid-cycle-009; carried) — prefer populating lower-layer shared utility (L1/L2/L3) over expanding higher-layer vocabulary (L4) when both eligible. **Status: substantially discharged across batch-2+3+4** — L3 went 1→8 firm (BLAS-1 cohort), L2 1→3 firm (`linear_combination` cycle-018), L1 10→11 (divfree-projector cycle-015); the cycle-009 "L3 empty" signal is RESOLVED. Remaining bias-guidance for cycle-019+: keep weighting L1/L2/L3 firm additions and lowering-theme completion above further L4 vocabulary expansion. Friction-ledger `lower-vocabulary-priority-over-higher-expansion` (addressed).
9. **bootstrap-L4-state-stratification** — write the L4 layer intro / dep-map exposing the sim-state vs operator-params vs ephemeral distinction. Lower-priority than the lower-layer work above per #8.
10. **carry-forward large dispatches (residual)** — `slepc-convergence-reason-lift-sub-theme` (`abstractor`/`lifter`); `spectrum_estimate` L1 rough-in (`harvester`; shares matrix-weighted-norm cohort); `chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep` (firm L1/L2 chebyshev anchor reconcile; `lifter`). (`gmres.md §L4 self-rotation` + NLEPS promoted to active #3/#4.) Carried from cycles 008/009/011/012/013/014 OQs.

## Methodology priorities (codified; addressed — kept for planner reference)

These were active priorities #18–#20 in batch-1; all are now codified in CLAUDE.md §Methodology invariants and watched, not active work items:
- **layer-definition-discipline-high-to-low** (cycle-009 meta) — CLAUDE.md invariant + role-spec touches; watching adherence.
- **phase-1-corpus-reduction-audit** (cycle-009 meta) — CLAUDE.md invariant + skill `phase-1-slice-reduction-audit` (promoted cycle-012); active work tracked under priority #5.
- **identity-lowering-both-levels-backfill** (cycle-009 meta) — CLAUDE.md invariant; krylov-step L3 backfill landed cycle-010, BLAS-1 L3 cohort closed cycle-011. **Companion decision cycle-012 meta**: non-adjacent identity rotations are annotated **in-line**, NOT via an `L3-L1/` directory (CLAUDE.md invariant "Identity rotations across non-adjacent layers are annotated in-line"; friction-ledger `l3-l1-inline-identity-rotation-convention`).
- **partly-constructive theme-status** (cycle-012 meta) — CLAUDE.md invariant + abstractor/lowering-verifier role-spec touches. **VALIDATED-BY-USE batch-3** (cycle-015 meta): the full lifecycle closed 3× cleanly (eigsolve EXIT cycle-013, divfree + chebyshev-L4 ENACT cycle-015, convergence-mapping correctly STAYS); the gate CLOSES (transient, not an escape hatch). Skill `partly-constructive-promotion-checklist` promoted cycle-015 + abstractor §Discipline 4-point-checklist bullet added. Friction-ledger `partly-constructive-lowering-theme-status` (validated-by-use).
- **producer-citation-self-verification** (cycle-015 meta) — the strongest batch-3 friction; 4 producer role-spec self-verification bullets (harvester/abstractor/lifter/layer-intro-author) + `verify-citation-range` skill §"Producer self-verification" section. **Batch-4 outcome (cycle-018 meta): the bullets HELD — no new producer-emit drift across 016/017/018 despite heavy citation surface; recurrence-4 did NOT fire; the mechanical-checker tool ASK stays `reviewed: defer-confirmed`.** Friction-ledger `producer-citation-drift-verify-not-self-invoked`.
- **slice-removal non-link-grep** (cycle-015 meta) — `phase-1-slice-reduction-audit` skill extended with a removal-specific non-link prose-reference grep step (slice REMOVALS strand bare-path/inline-code prose refs the build linkcheck can't catch). Friction-ledger `slice-removal-non-link-prose-reference-grep-gap`.
- **combinator-miner parametric/variadic-family detection mode** (cycle-018 meta; HUMAN-RAISED BLAS-1 prong-a) — `.claude/agents/combinator-miner.md` gained a "Parametric / variadic-family detection mode" section + Discipline bullets so arity/element-type/conjugation/weight families surface as ONE candidate (not N missed leaves). Enacted because the instance-counting heuristic was arity-blind — proximate cause the BLAS-1 `linear_combination` fold was never auto-surfaced and had to be human-raised. First live test: cycle-019+ combinator-miner (active #7). Friction-ledger `combinator-miner-arity-blind-parametric-family-detection`.
- **dispatch-phase write-guard across ALL 8 specialized specs** (cycle-018 meta; recurrence-3 escalation) — the "Do NOT write to `book/` yourself" Discipline bullet (previously only in `layer-intro-author.md`) is now the first Discipline bullet in all 8 specialized specs. Friction-ledger `specialized-agent-direct-write-to-book-during-dispatch` (addressed). An integrator-per-report pre-dispatch clean-tree gate is a HELD ASK (enact only on recurrence-4).
- **rough-in / forward-reference plain-text convention** (cycle-018 meta) — combinator-miner forward-reference note + harvester Discipline bullet: a markdown link to a not-yet-authored chapter is a hard `linkcheck2` build error; forward-refs stay plain-text/inline-code until the target file exists. Companion to the cycle-006 dep-map-row convention. Friction-ledger `rough-in-forward-reference-must-be-plain-text-not-live-link`.
- **staging-log append completeness** (cycle-018 meta) — integrator-per-report Process step 7 is now a HARD non-skippable step; integrator-finalize Process step 1 cross-checks staging-row-count vs dispatched-report-count and flags + reconciles on mismatch. Friction-ledger `staging-log-append-completeness-gap`.
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
