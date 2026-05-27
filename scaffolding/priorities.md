# Priorities

Short next-up list. Meta-phase and cycle-planner co-edit. Cycle-planner reads each cycle to inform dispatch selection.

**Discipline:**
- Keep under 10 items.
- Each item: one line, slug + one-sentence rationale.
- Meta-phase adds when friction-ledger surfaces an actionable target.
- Integrator removes when an item lands in the artifact.

## Now (active)

1. **harvester-promote-krylov-step** — formalize the cycle-002 L2 rough-in `krylov-step`; six deliverables per open question `krylov-step-harvester-deliverables`. **Now unblocked** — all four L1 deps (`apply_linop`, `axpy`, `dot`, `nrm2`) are firm post-cycle-004. Listed top in `integrator-signals.md` cycle-004 §Suggested next dispatches.
2. **abstractor-apply-linop-mutation-rotation-L1-L0** — write the `apply_linop-mutation-rotation` L1>L0 lowering theme. Substantially larger than `axpby-mutation-rotation`: representation-axis + transpose-mode + accumulate-mode + parallel-wrapper. Cycle-004 harvester flagged scope (open question `apply-linop-lowering-theme-scope`). Routes to `abstractor`.
3. **abstractor-axpbypcz-mutation-rotation-L1-L0** — companion to the existing `axpby-mutation-rotation` theme; first L1>L0 theme to mix structural-rebind with algebraic-constant-folding (the `γ == 0` sub-rule). Closes open question `axpbypcz-mutation-rotation-abstractor-target`.
4. **(RESOLVED) mfem-as-l0-substrate-policy** — User directive 2026-05-27 (resolving cycle-004 ASK): **unimplemented Palace components are NOT direct implementation targets.** Document stub as obstruction theme; literature-anchored L1 form may inform higher abstractions; promote speculative operators to firm only when small AND it simplifies semantics of higher forms. See CLAUDE.md §Scope and project-memory `feedback_unimplemented_palace_components`. Resolves Shared Infrastructure scoping ambiguity for items #6–#7 below.
5. **cross-layer-cross-cutter-krylov-step-layer-placement** — decide L2 vs L4 vs both for `krylov-step` per open question `krylov-step-layer-placement`. Can co-bundle with #1's L2 firm-up to ensure the dual-placement decision is made coherently. **Note**: per #4 resolution, the cycle-004 MINRES/BiCGStab obstruction-theme L1 forms (Lanczos step, three-term recurrence, BiCGStab short-recurrence, omega-update, stabilisation-update) are available as guidance inputs — promote any of them only if doing so simplifies the L2 `krylov-step` semantics.
6. **shared-infra-Householder-QR** (user directive 2026-05-27) — slice Householder QR (orthogonalisation sibling). Roadmap §Orthogonalisation. **Pre-grep recommended** (cycle-004 MINRES precedent): check `palace/utils/labels.hpp` + relevant solver classes for enum-only / `MFEM_ABORT`-routed status. **Per #4 resolution**: if Palace defines-but-does-not-implement, route to `abstractor` for obstruction theme; do NOT target implementation. If Palace implements it, route to `harvester` / `abstractor` normally.
7. **shared-infra-Jacobi-smoother** (user directive 2026-05-27) — slice Jacobi / damped Jacobi smoother. Roadmap §Smoothers and preconditioners. Same pre-grep + #4-policy treatment as #6.
8. **concepts-sweep-cycle-005** — `same-layer-cross-cutter` replay over remaining `book/src/concepts/` pages (`axpy`, `nrm2`, `orthogonalization`, etc.) using the cycle-004 `concepts/dot.md` rewrite as pattern template. Bundles cycle-003 open question `concepts-pre-layered-era-sweep` + cycle-004 `concepts-sweep-cycle-005-candidate`.
9. **scalar-promotion-typing-rule-lift** — concept-page extraction: the rule is now visible across 5 operators (`axpy`, `dot`, `axpby`, `axpbypcz`, `scal`). Well past the threshold for promotion above per-operator prose. Routes to `layer-intro-author` for `book/src/concepts/scalar-promotion.md` authorship + per-operator citation back-references.
10. **bootstrap-L0-reference-layer** (user directive 2026-05-27) — populate `book/src/L0/` as a reference-notes layer holding cross-cutting Palace-source interpretation that L1 entries currently duplicate inline. Currently L0 is a 30-line stub. Starter chapter set (~13 chapters, flat structure mirroring other layers):
    - **Conventions:** `output-arg-vs-receiver.md`, `mfem-vector-types.md`, `linalg-free-functions.md`, `mpi-globalsum-and-collectives.md`, `par-types-single-rank-reading.md`, `mutable-workspace-pattern.md`, `transparent-vs-load-bearing-tricks.md`.
    - **File overviews:** `linalg-vector-file.md`, `linalg-operator-file.md`, `linalg-iterative-file.md`, `ksp-factory-file.md`.
    - **Tests:** `tests-as-semantic-supplement.md`.
    - **No line-by-line source duplication** (prior slice-era pitfall). Each chapter is ~paragraph-scale interpretation with pointer citations.
    - Routes to `layer-intro-author` (role spec broadened cycle-003 to cover non-layer-intro pages). Cycle-005 planner may bundle several chapters per dispatch or split — planner's call. Existing L1 entries are NOT rewritten retroactively in this priority (see #11 below).

## Near (queued)

11. **retroactive-L1-context-thinning** — after #10 lands enough L0 reference notes, sweep existing L1 operator entries (`axpy`, `dot`, `nrm2`, `axpby`, `scal`, `apply_linop`, `axpbypcz`) to replace inline L0-interpretation prose in their "Context" sections with cross-references to L0 chapters. Cleanup pass; should noticeably shrink L1 entries. Dispatch when ≥6 of the #10 starter chapters land. Routes to `layer-intro-author` per-operator or as a single sweep.
12. **bootstrap-L4-state-stratification** — write the L4 layer intro / dep-map that exposes the sim-state vs operator-params vs ephemeral distinction.
13. **nrm2_B-weighted-energy-norm-L1** — depends on `apply_linop` (now firm) and `dot` (firm cycle-002). Citation: open question `nrm2-B-weighted-energy-norm-harvest`.
14. **shared-infra-MINRES** + **shared-infra-BiCGStab** — **closed by #4 resolution (2026-05-27).** Obstruction themes stay as documentation (`book/src/L1-L0/minres-iteration.md`, `book/src/L1-L0/bicgstab-iteration.md`). NOT direct implementation targets per the unimplemented-Palace-components policy. Their literature-anchored L1 forms remain available as guidance inputs for cycle-005+ `krylov-step` harvester promotion (item #1).
15. **enum-only-krylov-discovery-grep** — discovery pass: grep `palace/utils/labels.hpp` for additional enum values that route to `MFEM_ABORT` in `palace/linalg/ksp.cpp` (and analogous solver-selection points). Catches additional candidates for the `advertised-but-unimplemented-krylov-solvers` friction pattern before they surface ad-hoc. Cycle-005 or cycle-006.

16. **codemap-mcp-reintegration** (user directive 2026-05-27, mid-cycle-006) — re-integrate the `mcp/codemap/` Rust MCP server (built at commit `560decd`, currently inactive — `.claude/mcp.json` exists but tools not loaded in current session). Scope: (a) verify binary still launches under current rmcp 1.7 / tree-sitter 0.25 deps, rebuild if needed; (b) run `cargo test` on smoke suite against `reference/palace/`; (c) confirm `.claude/mcp.json` registration loads at next session start (post-restart deferred-tool list shows `mcp__palace-codemap__*`); (d) update `harvester` / `lowering-verifier` / `cross-layer-cross-cutter` / `same-layer-cross-cutter` / `combinator-miner` role specs to reference these tools as preferred for C++ source-localization (vs vanilla `Grep`/`Bash`); (e) pilot on one cycle-007 harvester dispatch; (f) instrument tool-call count and time vs vanilla baseline; (g) surface pilot results to user before broad role-spec rollout. **Scheduled: after cycle-006 meta-phase completes.** Routes to user-orchestrated work (not a planner dispatch — orchestration / config layer).

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
