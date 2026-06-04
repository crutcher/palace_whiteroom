# Resume notes — cycle-094 (post-restart) — GRADED-STACK + CORPUS-FINALIZATION campaign

**Why a restart:** a user-directed methodology enactment (2026-06-04) edited CLAUDE.md + 8 `.claude/agents/*` role-specs. New agent defs need a fresh session (friction `new-agent-defs-need-session-restart`). This restart also resets primary context after a long design conversation.

**This was NOT a meta-phase enactment** — it is a direct user directive enacted by the parent loop between the batch-29 meta-phase (commit `da91758`) and cycle-094. The batch counter is unchanged (cycle-094 is still batch-30 position 1/3).

## What was enacted (read these first)

1. **`METHODOLOGY-GRADED-STACK.md`** (root, NEW) — the authoritative full spec. Two orthogonal, mechanically-checkable axes:
   - **Axis 1 — resolution ladder + well-foundedness invariant.** Ranked ladder `roadmap_goal=0 < stub=1 < rough-in=2 < firm=3` (`partly-constructive`/`rough-in (test-coverage-bounded)` ≈ 2.5; `obstruction` is a separate *kind*, itself rankable). Invariant: for every `depends-on` edge `u→v`, `rank(u) ≤ rank(v)` — **an entry is at most as resolved as its least-resolved dependency**. Subsumes "as firm as its least-firm folded primitive" + the feature OWN-COMPOSITION rule. **`roadmap_goal` is a real book chapter** (rank 0, claim-free, carries intent + pulled-by + declared deps + working context) — the in-discipline replacement for the retired `annotated-and-retained` slice.
   - **Axis 2 — feature-root reachability/liveness.** Feature-surface columns are the **root set** (`seed` = root marker, a SEPARATE axis, NOT a ladder rung); reachability from roots over `depends-on` edges = liveness; unreachable = garbage. Detritus hunt = mark-sweep from roots.
   - **Shared substrate:** one typed dep graph — `depends-on` (blocking) vs `reference` (free; root edges are `reference`); optional ignored `kind:`. **Two linters** under `tools/` (rank check + reachability GC). **Adoption:** audit-first, hard-gate-new, bounded baseline-exceptions.
2. **CLAUDE.md** — §Methodology-invariants gained the graded-ladder bullet + the stub-tier language was revised (thinnest tier is now `roadmap_goal`).
3. **8 role-specs** got responsibility bullets (all point to `METHODOLOGY-GRADED-STACK.md` §8): abstractor (speculative → `roadmap_goal` chapters), harvester (promotion = rank-climbing + edge typing), lowering-verifier (theme ≤ min(endpoints)), layer-intro-author (authors `roadmap_goal` chapters + types edges + the methodology book page), critic (adds rank-invariant check (9) + reachability check (10)), integrator-per-report (rank gate at apply), integrator-finalize (run the linters at finalize once built), cycle-planner (fan-out = reachability weight), meta-phase (the GC sweep + baseline-exception set + book-methodology refresh).
4. **`scaffolding/priorities.md`** — CYCLE-094 active head reshaped: **item 0 = `graded-stack-and-corpus-finalization-campaign` (THE LEAD)**, P0→P3. The bilinear-form cascade is DEMOTED to item 1 (READY; now framed as the first validation of the rank linter — it IS a rank-propagation wave).

## What the post-restart session does (cycle-094 onward)

Run the **campaign** as priorities.md item 0 sequences it:
- **P0** — build the two `tools/` linters (rank check + reachability GC) + define the minimal binary edge-typing.
- **P1** — type the dep-map edges artifact-wide + run the audit (= the first detritus sweep); triage → fix small / track baseline-exceptions; adopt the invariant as a hard gate.
- **P2** — corpus finalization (the 9-slice migration; the ONE genuine gap is `L4/preconditioning-framework.md`, firm-on-first-authoring; everything else is absorb-into-concept-home + repoint + delete; HARD blockers: `polynomial_recurrence_step:119-160` ×5 firm cites, `arnoldi_step` heavy anchors, the `plane_rotation_stream` `:72-108`/`:73-108` off-by-one). Completion criterion is the GC + rank linter both clean with zero slice nodes. Slice audit detail is in the 2026-06-04 conversation; the disposition table is in `priorities.md` item 0 P2.
- **P3** — author `book/src/methodology/resolution-ladder.md` + refresh `goal-flow.md` + the `roadmap_goal` SUMMARY grouping/banner (the "update the methodology section of the book" instruction).

This is multi-cycle; let the c094 planner scope P0/P1 first (the linters + audit gate everything else). The bilinear-form cascade (item 1) can run as the P1 rank-linter's first live validation or right after.

## Caveats / open
- The audit (P1) WILL likely surface a few latent rank violations (firm-on-rough-in nobody flagged) — expected; triage per §5, don't panic.
- `git status` is clean as of the enactment commit (below). The book was NOT touched (no `book/src` edits in this enactment) — build state is unchanged from cycle-093's clean build.
- Design decisions resolved: (a) feature-`seed` stays a parallel root-set axis (does NOT collapse into the ladder); (b) minimal binary edge-typing; (c) audit-first via the GC pass. Rationale in `METHODOLOGY-GRADED-STACK.md` §3/§5 + the 2026-06-04 conversation.
