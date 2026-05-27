# Priorities

Short next-up list. Meta-phase and cycle-planner co-edit. Cycle-planner reads each cycle to inform dispatch selection.

**Discipline:**
- Keep under 10 items.
- Each item: one line, slug + one-sentence rationale.
- Meta-phase adds when friction-ledger surfaces an actionable target.
- Integrator removes when an item lands in the artifact.

## Now (active)

1. **bootstrap-L1-vocabulary** (in progress: `axpy` ✓ pilot-1, `dot` ✓ cycle-002, `axpby` rough-in ✓ cycle-002) — harvest remaining core L1 operators (`nrm2`, `scal`, `apply_linop`) into `book/src/L1/`. **Discipline:** one operator per harvester invocation (see `haiku-cycle-planner-over-scopes-harvester` friction).
2. **harvester-promote-axpby** — promote the cycle-002 rough-in `axpby` to firm L1 entry; record the fusion-vs-decomposition decision (`axpby` as primitive vs `axpy ∘ scal`) per open question `axpby-axpy-scal-decomposition-decision` in `scaffolding/decisions/`.
3. **lowering-verifier-axpby-theme** — audit the cycle-002 `axpby-mutation-rotation` theme against the full L0 corpus; resolve the three sub-patterns A/B/C per open question `axpby-lowering-verifier-audit`.
4. **same-layer-cross-cutter-reconcile-dot-concept** — `concepts/dot.md` has two contradictions with `book/src/L1/dot.md` (return-type claim; non-existent `linalg::Dotc`; inverted conjugation). Resolve per open questions `concepts-dot-return-type-correction` + `concepts-dot-dotc-and-inverted-conjugation`.
5. **harvester-promote-krylov-step** — formalize the cycle-002 L2 rough-in `krylov-step`; six deliverables per open question `krylov-step-harvester-deliverables`. Depends on L1 vocabulary firming (item #1).

## Near (queued)

6. **bootstrap-L4-state-stratification** — write the L4 layer intro / dep-map that exposes the sim-state vs operator-params vs ephemeral distinction.
7. **cross-layer-cross-cutter-krylov-step-layer-placement** — decide L2 vs L4 vs both for `krylov-step` per open question `krylov-step-layer-placement`.

## Watch list (deferred)

- **cycle-003-planner-cascade-pattern** — if haiku cycle-planner skips Write again (`haiku-subagent-anchors-to-ledger-lore`) OR over-scopes the harvester again (`haiku-cycle-planner-over-scopes-harvester`) on cycle-003, escalate: propose either swapping cycle-planner to opus or adding hard override clauses in `.claude/agents/cycle-planner.md`.
- **l2-dep-map-format-vs-l1** — open question `l2-dep-map-format-vs-l1`: decide whether the L2 Working-Notes overflow is reusable across L2/L3/L4 dep-maps or a fifth column is cleaner. Routes back to meta-phase / channel-format change.
- Phase 1 slice corpus move to `book/src/_phase1_corpus/` — 64 cross-references need rewriting; defer until pilot validates flow.
- `lessons.md` retirement — keep as historical record post-Phase-E.

## Recently landed

- **post-restart-verify-claude-agents** (cycle-002, commit c3312a6) — verified: all 13 custom `.claude/agents/<name>.md` definitions resolve via `Agent(subagent_type=<name>)`. The previous `embed-and-persist` skill is refined (not retired) — needed only for parent-pre-creates-skeleton on REPORT.md targets due to a content-pattern Write filter on `report|summary|findings|analysis` filenames. See friction-ledger entries `subagent-file-write-blocked-general-purpose` (status `resolved-with-narrowing`) and `content-pattern-write-filter-on-report-keywords` (status `addressed-by-design`).
- **bootstrap-L1-L0-theme-axpby** (cycle-002, commit c3312a6) — abstractor rough-in `axpby-mutation-rotation` theme landed at `book/src/L1-L0/axpby-mutation-rotation.md` with three sub-patterns A/B/C. Awaits lowering-verifier audit (now priority #3).
- **mine-krylov-iteration-step** (cycle-002, commit c3312a6) — combinator-miner rough-in `krylov-step` landed at `book/src/L2/index.md`. Awaits harvester promotion (now priority #5).
