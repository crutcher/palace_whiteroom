# Priorities

Short next-up list. Meta-phase and cycle-planner co-edit. Cycle-planner reads each cycle to inform dispatch selection.

**Discipline:**
- Keep under 10 items.
- Each item: one line, slug + one-sentence rationale.
- Meta-phase adds when friction-ledger surfaces an actionable target.
- Integrator removes when an item lands in the artifact.

## Now (active)

1. **bootstrap-L1-vocabulary** (in progress: `axpy` ✓ pilot-1, `dot` ✓ cycle-002, `nrm2` ✓ cycle-003, `axpby` ✓ cycle-003) — harvest remaining core L1 operators (`scal`, `apply_linop`) into `book/src/L1/`. **Discipline:** one operator per harvester invocation (see `haiku-cycle-planner-over-scopes-harvester` friction).
2. **concepts-dot-rewrite** — rewrite `book/src/concepts/dot.md` to align with the L1/dot.md authoritative entry (fixes the three contradictions surfaced by cycle-003 cross-cutter: return-type, non-existent `linalg::Dotc`, inverted-conjugation, bogus `vector.cpp:142-178` citation). Routes to `layer-intro-author` (role broadened cycle-003 meta-phase to cover `concepts/<slug>.md`). Closes open questions `concepts-dot-return-type-correction` + `concepts-dot-dotc-and-inverted-conjugation`. Listed in `integrator-signals.md` cycle-003 §Suggested next dispatches.
3. **l1-index-refresh** — refresh `book/src/L1/index.md` intro + dep-map prose now that 4 firm L1 operators exist (`axpy`, `dot`, `nrm2`, `axpby`); pilot-1's threshold of ≥3 firm operators is met. Routes to `layer-intro-author`. Can co-bundle with #2 under the same role invocation. Listed in `integrator-signals.md` cycle-003 §Suggested next dispatches.
4. **harvester-scal-L1** — harvest `scal` at L1; small primitive; referenced in `axpby` laws 2/3 and in `linalg::Normalize` (`vector.hpp:262-270`). Closes open question `scal-primitive-l1-harvest`. Listed in `integrator-signals.md` cycle-003.
5. **harvester-apply_linop-L1** — harvest `apply_linop` at L1; bootstrap-L1-vocabulary item; gates `krylov-step` promotion (#6) and `nrm2_B` weighted-energy-norm. Substantial L0 surface (`mfem::Operator::Mult`, `palace::ParOperator::Mult`, `linalg::Operator`) — cycle-planner may subdivide.
6. **harvester-promote-krylov-step** — formalize the cycle-002 L2 rough-in `krylov-step`; six deliverables per open question `krylov-step-harvester-deliverables`. Depends on L1 vocabulary firming (item #5).
7. **harvester-axpbypcz-L1** — harvest `axpbypcz` at L1 (the `vector.cpp:756` internal AXPBY+Add composition; explicit pattern in `linalg::AXPBYPCZ`). Cycle-003 lowering-verifier confirmed evidence anchor. Closes open question `axpbypcz-l1-harvest`.

## Near (queued)

8. **bootstrap-L4-state-stratification** — write the L4 layer intro / dep-map that exposes the sim-state vs operator-params vs ephemeral distinction.
9. **cross-layer-cross-cutter-krylov-step-layer-placement** — decide L2 vs L4 vs both for `krylov-step` per open question `krylov-step-layer-placement`.
10. **shared-infra-MINRES** (user directive 2026-05-27: Shared Infrastructure raised) — slice MINRES (symmetric-indefinite three-term recurrence) from Palace. Roadmap §Shared infrastructure / Krylov solvers.
11. **shared-infra-BiCGStab** (same directive) — slice BiCGStab (non-symmetric short-recurrence) from Palace. Same roadmap section.
12. **shared-infra-Jacobi-smoother** (same directive) — slice Jacobi / damped Jacobi smoother. Roadmap §Smoothers and preconditioners.
13. **shared-infra-householder-QR** (same directive) — slice Householder QR (orthogonalisation sibling). Roadmap §Orthogonalisation.

## Methodology guidance (user directive 2026-05-27; cycle-003 update)

- **Dispatch target: up to 15 sub-agents per cycle** (was 1–6). Cycle-004 stretch target: **8–12 dispatches** to stress-test the higher capacity, if priorities permit (the seven Now items above plus selected Near items could populate it). Conflict-tolerance philosophy: minor wave conflict at integration is *useful tooling signal*, not friction to avoid. Cycle-planner: when in doubt, mark as PARALLEL. See `.claude/agents/cycle-planner.md` Discipline section.
- **Integrator-to-planner signals channel**: integrator now appends to `scaffolding/integrator-signals.md` after each cycle (newest at top). Cycle-planner reads the top ~3 entries each cycle. **Cycle-003 confirmed working as designed** (friction-ledger entry `integrator-signals-channel-working-as-designed`, status `addressed-by-design`). See `.claude/agents/integrator.md` step 14.
- **`verified_against:` YAML must be fenced** (cycle-003 meta-phase): lowering-verifier emissions of the `verified_against:` block must use a fenced ` ```yaml ... ``` ` code block. See `.claude/agents/lowering-verifier.md` Discipline + friction-ledger entry `lowering-verifier-yaml-in-prose-channel-format`.
- **`layer-intro-author` role broadened** (cycle-003 meta-phase): now covers `book/src/concepts/<slug>.md` authorship in addition to layer intros. See `.claude/agents/layer-intro-author.md`.

## Watch list (deferred)

- **haiku-cycle-planner-cascade-pattern (relaxed cycle-003)** — recurrence-2 of `haiku-cycle-planner-over-scopes-harvester` observed in cycle-003 (over-cautious-on-overlap, not over-scopes-harvester); addressed by user directive 8fc3a07's parallel-when-in-doubt policy. **Watch cycle-004:** if planner still classifies row-level non-overlapping edits as sequential, escalate (proposal: swap cycle-planner to opus, OR add hard parallel-default override).
- **scalar-promotion-typing-rule lift** — open question `scalar-promotion-typing-rule`: now visible across `axpy`, `dot`, `axpby` (3 operators stating the same per-operator clause). Approaching threshold for promotion above per-operator prose. Cycle-planner may want to escalate priority once a fourth operator (likely `scal` or `axpbypcz`) lands.
- **l2-dep-map-format-vs-l1** — open question `l2-dep-map-format-vs-l1`: decide whether the L2 Working-Notes overflow is reusable across L2/L3/L4 dep-maps or a fifth column is cleaner. Routes back to meta-phase / channel-format change.
- **axpby-corpus-coverage-exhaustive-indexing** — open question (cycle-003): the cycle-003 lowering-verifier deferred ~25 uncited corpus sites + 3 defined-not-used L0 forms for future exhaustive indexing. Defer until L1 vocabulary fully firm.
- Phase 1 slice corpus move to `book/src/_phase1_corpus/` — 64 cross-references need rewriting; defer until pilot validates flow.
- `lessons.md` retirement — keep as historical record post-Phase-E.

## Recently landed

- **bootstrap-L1-nrm2** (cycle-003, commit 9aa1c59) — `book/src/L1/nrm2.md` firm operator entry (10 algebraic laws + 4 non-laws; 1 variant axis with element-type collapse). Closes priority #1's nrm2 slot.
- **bootstrap-L1-axpby** (cycle-003, commit 9aa1c59) — `book/src/L1/axpby.md` firm operator entry (9 algebraic laws + 4 non-laws; 2 variant axes; fused-primitive decision recorded in `scaffolding/decisions/axpby-as-primitive.md`). Closes cycle-002 priority #2 + open question `axpby-axpy-scal-decomposition-decision`.
- **lowering-verifier-axpby-mutation-rotation** (cycle-003, commit 9aa1c59) — `book/src/L1-L0/axpby-mutation-rotation.md` `verified_against:` block (9 per-citation audit rows). Closes cycle-002 priority #3 (partially; exhaustive corpus indexing deferred to `axpby-corpus-coverage-exhaustive-indexing` open question).
- **same-layer-cross-cutter-dot-concept-contradictions** (cycle-003, commit 9aa1c59) — observation report concretely confirming three contradictions in `concepts/dot.md` vs `L1/dot.md`. Routes to cycle-004 layer-intro-author (now priority #2).
- **post-restart-verify-claude-agents** (cycle-002, commit c3312a6) — verified: all 13 custom `.claude/agents/<name>.md` definitions resolve via `Agent(subagent_type=<name>)`.
- **bootstrap-L1-L0-theme-axpby** (cycle-002, commit c3312a6) — abstractor rough-in `axpby-mutation-rotation` theme landed; audited cycle-003.
- **mine-krylov-iteration-step** (cycle-002, commit c3312a6) — combinator-miner rough-in `krylov-step` landed at `book/src/L2/index.md`. Awaits harvester promotion (priority #6).
