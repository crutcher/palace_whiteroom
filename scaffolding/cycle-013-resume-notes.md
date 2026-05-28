# Cycle-013 resume notes (post-meta-phase-cycle-012, batch-2 closure)

**Written by**: meta-phase-cycle-012 (batch-2 closure, 2026-05-28T05:07:04Z).
**Audience**: parent orchestrator preparing the cycle-013 primary cycle (first cycle of meta-batch-3 = cycles 013/014/015).

## Session restart required

Per friction-ledger entry `new-agent-defs-need-session-restart`, **the parent should restart the Claude Code session before cycle-013 begins.** The meta-phase enacted role-spec changes affecting **7 agent definitions**:

1. **`.claude/agents/layer-intro-author.md`** — top-level Discipline prompt-guard: do NOT write to `book/`; emit proposed-changes blocks (especially for concept-page corrections). Primary mitigation for the recurrence-2 write-authority leak.
2. **`.claude/agents/cycle-planner.md`** — Discipline: verify Palace source file paths / symbol locations via MCP codemap before citing them in dispatch scopes (recurrence-3 path-drift on `linalg/*`).
3. **`.claude/agents/integrator-per-report.md`** — Process step 7 + Discipline: take the cycle-id / staging-dir path from the parent's dispatch; never infer it from report content (recurrence-1 cycle-mislabel).
4. **`.claude/agents/harvester.md`** — Discipline: annotate non-adjacent identity rotations in-line; do NOT create a non-adjacent lowering directory (`L3-L1/`, `L4-L2/`).
5. **`.claude/agents/abstractor.md`** — Discipline: use `partly-constructive` status when a theme is structurally firm but a sub-part is reconstructed (named caveat + negative anchors + promotion condition).
6. **`.claude/agents/lifter.md`** — Discipline: L0-evidence-driven prose correction is in-scope when bounded + evidenced + recorded; re-architecting re-routes.
7. **`.claude/agents/lowering-verifier.md`** — Discipline: a `partly-constructive` audit may UNBLOCK without ENACTING (gate the promotion); independently `read_range`-confirm every asserted-verified anchor (don't transcribe from the audited artifact).

A session restart ensures these definitions are loaded for cycle-013 dispatch.

## Compactification

Per CLAUDE.md §Methodology invariants "Compactify primary context after every meta-phase", **the parent should run `/compact`** after the meta-phase commit lands + pushes. With the 3:1 cadence this fires roughly every 3 primary cycles (this is the second such firing, closing batch-2).

## ASK items awaiting user decision

**NONE.** All meta-phase plans this batch were enacted as `go` (Low/Medium cascade) or declined as `no-go` with reasons. The cycle-009-meta ASK (MCP codemap rollout) is RESOLVED — the user enacted option (a) (commit `ceb87da`); the pilot succeeded and cycles 011/012 used the tools routinely. No new ASKs.

## New / updated CLAUDE.md §Methodology invariants (planner should re-read)

- **Theme/operator status `partly-constructive` is first-class** — alongside firm / rough-in / obstruction; firm-structural but a constructive sub-part reconstructed from negative anchors / literature, with a named caveat + promotion condition. Negative anchors (per-status) are distinct from obstruction-theme negative anchors. First gate-close test: cycle-013 eigsolve Sub-pattern B promotion (priority #1).
- **Identity rotations across non-adjacent layers are annotated in-line, not via a dedicated lowering directory** — lowering dirs are per-adjacent-edge only (`L4-L3/`, `L3-L2/`, `L2-L1/`, `L1-L0/`); non-adjacent identity is the transitive consequence of the adjacent themes, annotated in-line in the L_n entry. **DECISION: no `book/src/L3-L1/` directory** (signal 9 closed; option a).
- **§Target system MCP-first localization** — the `palace-codemap` MCP server is the preferred localization path for Palace C++ (localize via the codemap tools, `read_range` deliberately). Pilot succeeded cycle-010; routine cycles 011/012.

## New priorities surface (cycle-013+ active — see scaffolding/priorities.md §Now)

1. **(GATED, highest) eigsolve-mutation-rotation Sub-pattern B promotion** — cycle-013 abstractor applies audit Edits 2+3 (GetConverged forwarder + Sub-pattern A attribution), THEN drops the `partly-constructive` caveat. OQ `eigsolve-getconverged-forwarder-fix-and-gated-promotion`. **The dispatch prompt MUST state the cycle number explicitly as cycle-013** (per the new integrator-per-report cycle-id discipline + the per-report-integrator cycle-mislabel signal).
2. **(HEADLINE harvester) l1-divfree-projector-promotion** — 6 firm entries cite the now-reduced divfree slice.
3. **(harvester) L3 + L4 chebyshev rows** — unblock full `chebyshev.md` reduction (identity-lowerings both levels; annotate any L3↔L1 identity in-line).
4. **(abstractor) orthogonalize + chebyshev lowering themes** — L1>L0 + L2>L1; mark `partly-constructive` if a sub-part is reconstructed.
5. **(same-layer-cross-cutter) phase-1 corpus reduction batch-4** — final 2 slices (cg_preconditioning_framework + sparse_triangular_solve). **Invoke the new skill `phase-1-slice-reduction-audit`** (START+END boundary verification + unique-text anchors).
6. **(HEADLINE layer-intro-author) plane-rotation concept-page canonical-pointer repoint** — 3 firm concept pages still cite the orthog slice as canonical. **Emit proposed-changes blocks; do NOT write `book/` directly** (the new prompt-guard).

## Skills newly available to cycle-013 agents

- `phase-1-slice-reduction-audit` (same-layer-cross-cutter; for priority #5).
- `revert-dispatch-phase-book-mutation` (repairer safety-net for dispatch-phase artifact leaks).
- `verify-citation-range` now carries an "Audit-report / inherited-citation sub-case" section (lowering-verifier / critic audit reports).

## Friction-ledger churn this meta-phase

10 updates: 1 status flip (MCP → resolved) + 9 new/generalized entries. Cycle-013 planner does not need to read the full friction-ledger; the priorities + CLAUDE.md invariants are the planning surface. Notable: `skill-uptake-survey-non-invocation-cycle-wide` is `recurring` (telemetry-noise, NOT escalating — do not over-react to it); `specialized-agent-direct-write-to-book-during-dispatch` is recurrence-2 addressed (a THIRD leaking agent escalates to an all-specialized-agent guard + re-weigh of a tooling gate).

## Housekeeping flag carried from cycle-012 finalize

`scaffolding/integrator-signals.md` is ~900 lines (over the ~500-line soft cap). Once cycle-013 lands, cycle-002/003-era entries become archive-eligible to `scaffolding/integrator-signals-archive/cycle-002-011.md`. The cycle-013 finalize should action the archive.

## Estimated cycle-013 wave-1 candidate dispatches (suggestive, not prescriptive)

Per priorities #1–#6 + carry-forward integrator-signals:
- **abstractor** on `eigsolve-getconverged-forwarder-fix-and-gated-promotion` (GATED; highest priority; cycle number stated explicitly).
- **harvester** on `l1-divfree-projector` (HEADLINE).
- **harvester** on L3 + L4 chebyshev rows.
- **abstractor** on orthogonalize / chebyshev lowering themes.
- **same-layer-cross-cutter** on phase-1 corpus reduction batch-4 (final 2 slices; invoke the new skill).
- **layer-intro-author** on plane-rotation concept-page repoint (HEADLINE; proposed-changes only).

Planner judgment for final scope and ordering. **Meta-phase fires next after cycle-015 finalize** (batch-3 = cycles 013/014/015).
