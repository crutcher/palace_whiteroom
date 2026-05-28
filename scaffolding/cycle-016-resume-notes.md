# Cycle-016 resume notes (post-meta-phase-cycle-015, batch-3 closure)

**Written by**: meta-phase-cycle-015 (batch-3 closure, 2026-05-29).
**Audience**: parent orchestrator preparing the cycle-016 primary cycle (first cycle of meta-batch-4 = cycles 016/017/018).

## Session restart required

Per friction-ledger entry `new-agent-defs-need-session-restart`, **the parent should restart the Claude Code session before cycle-016 begins.** The meta-phase enacted role-spec changes affecting **4 agent definitions** (all the same change-class: a citation self-verification Discipline bullet, plus one extra bullet on abstractor):

1. **`.claude/agents/harvester.md`** — Discipline: self-verify every L0 citation against source (`read_range` / codemap) BEFORE emitting it; do not cite from memory. Invoke `verify-citation-range`.
2. **`.claude/agents/abstractor.md`** — Discipline: (a) the same citation self-verify bullet; (b) a NEW `partly-constructive`→`firm` 4-point promotion-checklist bullet (route / evidence-vs-acceptance / two-dispatch protocol / honest-note-survives), pointing at the newly-promoted skill.
3. **`.claude/agents/lifter.md`** — Discipline: citation self-verify bullet, with the re-anchor-specific check that a relocated pointer's NEW target is the TERMINAL firm home (not another relocated-dangle).
4. **`.claude/agents/layer-intro-author.md`** — Discipline: citation self-verify bullet, noting L0-bundle chapters are the highest-volume citation surface.

A session restart ensures these definitions are loaded for cycle-016 dispatch.

## Compactification

Per CLAUDE.md §Methodology invariants "Compactify primary context after every meta-phase", **the parent should run `/compact`** after the meta-phase commit lands + pushes. With the 3:1 cadence this fires roughly every 3 primary cycles (this is the third such firing, closing batch-3).

## ASK items awaiting user decision

**ONE.** A mechanical **codemap-backed citation-range checker tool** under `tools/` — validates every `path:lo-hi` in a CYCLE.md's proposed-changes against `reference/` source (e.g. via the codemap `get_symbol_def`/`read_range`) as a pre-integration lint. Motivation: citation line-drift was the strongest recurring friction of batch-3 (every cycle, ~6 reports/013, 5-of-8/014 including the auditing role, bilinearform/015). This meta-phase enacted the cheap fix (4 producer role-spec self-verification bullets + a `verify-citation-range` skill section), but the cycle-014 evidence — the citation-AUDITING lowering-verifier itself drifted DESPITE having had a citation Discipline bullet since cycle-012 — shows role-spec bullets are necessary but NOT sufficient. A mechanical check is the durable fix. It requires writing code (not a role-spec edit), so it is ask-class per the write-authority partition + the `feedback_tooling_changes_proposable` memory (a NEW tool is proposable but a build effort the user should green-light). **Decision needed**: (a) build the tool (meta-phase can scope it, user/parent implements under `tools/`); (b) defer to batch-4 and let the producer bullets prove themselves first; (c) decline (rely on the repairer/critic catch indefinitely). Recommendation: (b) then (a) if batch-4 still drifts — the watch clause on `producer-citation-drift-verify-not-self-invoked` will trigger at recurrence-4.

## New / updated CLAUDE.md §Methodology invariants

**NONE added this meta-phase.** No new invariants — the batch-3 enactments are role-spec + skill + ledger changes, not new CLAUDE.md invariants. The existing `partly-constructive` invariant is now annotated as validated-by-use (in the friction-ledger + priorities reference block, not in CLAUDE.md itself).

## New priorities surface (cycle-016+ active — see scaffolding/priorities.md §Now)

1. **(abstractor — HEADLINE) divfree-projector L1>L0 mutation-rotation theme** — now that `L1/divfree-projector.md` is firm, author the lowering theme on a firm foundation.
2. **(lifter — small) l4-chebyshev-residual-formm-foldm-prose-cleanup** + sibling `l3-chebyshev-downward-prose-iterate-while-refresh` — surgical `forM_`/`foldM` → `iterate_while_pure` prose refreshes.
3. **(lifter) l4-krylov-step-cg-md-citation-sweep + l2-krylov-step-cg-md-citation-sweep** — sibling cg.md sweeps on the DISTINCT L4 (8 pointers) + L2 (12 pointers) krylov-step operator entries. **Confirm relocated pointers land at the terminal firm home** (the new lifter citation bullet).
4. **(layer-intro-author) bundle-6 #5 `fem/libceed/operator.cpp`** — next L0 bundle chapter; also retires the plain-text non-link reference in `fem-bilinearform-file.md`. **Citation-dense — self-verify each range; proposed-changes blocks only.**
5. **(lifter/cross-layer-cross-cutter) divfree.hpp doc-tension OQ** — resolve or document the residual divfree header/doc-comment tension.

Carry-forward (Near/queued): lower-layer-vocabulary bias guidance; bootstrap-L4-state-stratification; large carry-forwards (gmres §L4 v0.6→v0.7, NLEPS, slepc-convergence-reason-lift, spectrum_estimate, chebyshev anchor/Mult2 sweep).

## Skills newly available / updated for cycle-016 agents

- **`partly-constructive-promotion-checklist`** (NEW, promoted this meta-phase) — abstractor/lifter walk the 4-point checklist before flipping `partly-constructive`→`firm`; critic/integrator ratify.
- **`verify-citation-range`** now carries a top-level **"Producer self-verification before emitting citations"** section (the producer-emit-time self-check; the 4 producer role-spec bullets point at it).
- **`phase-1-slice-reduction-audit`** now carries a **"Removal sub-case: non-link prose-reference grep"** section — slice REMOVALS (vs reductions) require a bare-path/inline-code grep, not just a markdown-link check.

## Friction-ledger churn this meta-phase

4 updates: 2 new entries (`producer-citation-drift-verify-not-self-invoked` addressed; `slice-removal-non-link-prose-reference-grep-gap` addressed) + 2 status flips (`skill-uptake-survey-non-invocation-cycle-wide` recurring→escalating, recurrence 3→4, watch-clause fired; `partly-constructive-lowering-theme-status` validated-by-use). Cycle-016 planner does not need to read the full friction-ledger; the priorities + this resume-note are the planning surface. Notable: the citation-drift fix is role-spec bullets (necessary but not sufficient — the mechanical-tool ASK is the durable fix); the `partly-constructive` gate is now PROVEN to close (do not treat partly-constructive entries as permanent escape hatches — drive them to firm via the gated two-dispatch protocol).

## Housekeeping flag

`scaffolding/integrator-signals.md` is ~945 lines (over the ~500-line soft cap). The cycle-013 finalize was to archive cycle-002/003-era entries; verify whether the archive happened and, if not, the cycle-016 finalize should action `scaffolding/integrator-signals-archive/`.

## Estimated cycle-016 wave-1 candidate dispatches (suggestive, not prescriptive)

Per priorities #1–#5 + carry-forward integrator-signals:
- **abstractor** on `divfree-projector` L1>L0 mutation-rotation theme (HEADLINE; firm foundation).
- **lifter** on the chebyshev `forM_`/`foldM` prose cleanups (L4 + L3 siblings; small).
- **lifter** on the L4 + L2 krylov-step cg.md citation sweeps (terminal-home check).
- **layer-intro-author** on bundle-6 #5 `fem/libceed/operator.cpp` (proposed-changes only; self-verify citations).
- **lifter/cross-layer-cross-cutter** on the divfree.hpp doc-tension OQ.

Planner judgment for final scope and ordering. **Meta-phase fires next after cycle-018 finalize** (batch-4 = cycles 016/017/018).
