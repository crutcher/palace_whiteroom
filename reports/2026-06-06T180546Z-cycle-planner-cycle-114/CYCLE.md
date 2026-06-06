---
agent: cycle-planner
invoked_at: 2026-06-06T180546Z
scope: cycle-114 dispatch plan
status: pending
---

# Cycle 114 dispatch plan

## Goals selected this cycle

THIRD/FINAL primary cycle of meta-batch-36 (cycles 112/113/114; the batch-36 meta-phase fires AFTER this finalize, aggregating 112/113/114). c113 landed `d88f003` and handed c114 TWO high-fan-out grounding candidates, BOTH real reachability +Δ via the c108 §5 faithful-edge convention. This cycle ACTS on both: (1) the **FE-assemble cluster ground** — author canonical `edges:` blocks adding the faithful `composes` `depends-on` edges `fe_assemble → weak_form_term`, `fe_assemble → fe_space`, `fe_space → fe_collection`, all read directly off the `fe_assemble` signature/prose (a real +3 — `fe_assemble` is reachable from 7 feature columns); (2) the **reachable-op L1>L0 theme-grounding sweep** — upgrade the theme edge on `dot`/`nrm2`/`scal` from `reference` → `depends-on (kind: lowers-to)` (the exact c113 D2 `set_subvector_zero` move; a real +3 — all three ops are reachable but their themes are garbage because the edge is `reference`-only). Two `layer-intro-author` frontmatter-only dispatches, DISJOINT file sets → ONE parallel wave. STOP-PROPOSING in force; the RE5 hygiene-only ops (`normalize`/`reciprocal`/`elementwise_product` — themselves garbage) are deliberately NOT scoped (routed to the batch-36 meta-phase). NO pre-ratification of RE6-RE8 (meta-phase's job).

## Dispatches

### D1 — (`layer-intro-author`, the FE-assemble cluster GROUND, deps: none)
- **scope**: Author canonical `edges:` blocks on `book/src/L1/fe_assemble.md` + `book/src/L1/fe_space.md` (frontmatter-only). Both carry only legacy/`status`-token frontmatter today (`fe_assemble.md`: `firmness: firm` + `lowers_to: [L1-L0/fe-operator-assemble-mutation-rotation]` + empty `depends_on: []`; `fe_space.md`: only `status: firm`, NO edges) → migrate to the canonical `rank:`+`edges:` form per the c109 `L2/krylov-step` / `set_subvector_zero` template. Add the faithful `composes`-kind `depends-on` edges read DIRECTLY from the signature `fe_assemble :: (space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N,N]` + prose:
  - `L1/fe_assemble → L1/weak_form_term` (the `terms: [WeakFormTerm]` fold element-type — `fe_assemble.md:60,71-72,163` "the fold quantifies over");
  - `L1/fe_assemble → L1/fe_space` (the `space:` input — `fe_assemble.md:68-70` "the axis fe_space defines");
  - `L1/fe_space → L1/fe_collection` (`fe_space` consumes ONE `FECollection` from the schedule — `fe_space.md:16,35,38`).
  - Preserve `fe_assemble`'s existing `lowers_to: L1-L0/fe-operator-assemble-mutation-rotation` as a `depends-on (kind: lowers-to)` edge in the migration. Keep `fe_space`'s firm status; add its faithful L0 `cites-evidence` if cheaply read off the existing chapter (NOT required for the +Δ).
- **deps**: none.
- **rationale**: c113 D1's 1 GROUNDABLE finding (the only groundable member of the audited STRONGER GARBAGE SIGNAL set). `L1/fe_assemble` is reachable (inbound from 7 feature columns — verified via `--show-inbound`); `weak_form_term`/`fe_space`/`fe_collection` are all firm. The three `composes` edges flip them reachable: `reachable` 124→127, `detritus` −3, STRONGER GARBAGE SIGNAL −3. Grounds the FE-assembly sub-spine's element/space/collection vocabulary (the assemble half of the deliverable). Plan-tag `graded-stack-lazy-tail-typing` (grounding sub-tranche). FAITHFUL-PATH-OR-FINDING: all three edges pre-verified faithful from the signature/prose; type only those.

### D2 — (`layer-intro-author`, the reachable-op L1>L0 theme-grounding sweep, deps: none)
- **scope**: Upgrade the L1>L0 theme edge on `book/src/L1/{dot,nrm2,scal}.md` (frontmatter-only) from `reference` (navigational) → `depends-on (kind: lowers-to)` — the c108 §5 L1-op→theme convention, the exact c113 D2 `set_subvector_zero` move. Canonical template: `book/src/L1/set_subvector_zero.md:5-19`. Edges:
  - `L1/dot → L1-L0/dot-mutation-rotation` (currently `reference`; `dot.md` also carries `reference: concepts/dot` — KEEP that);
  - `L1/nrm2 → L1-L0/nrm2-mutation-rotation` (currently `reference`; `nrm2.md` also carries `depends-on: L1/dot` — KEEP that);
  - `L1/scal → L1-L0/scal-mutation-rotation` (currently `reference`).
  - All three themes lead `## Status` with `` `firm` `` (verified) → `rank(op=3) ≤ rank(theme=3)` holds. Keep/relocate the existing `reference` per the scheme.
- **NO prose correction needed**: UNLIKE c113's `set_subvector_zero`, these three carry NO stale "rank-direction error" prose (grep-verified 0 matches in all three) — ONLY the edge upgrade.
- **deps**: none.
- **rationale**: c113 D2's candidate friction `stale-pre-c108-rank-direction-error-prose-on-L1-ops` — the systematic reachable-op subset. Each op is REACHABLE (verified not-garbage via `--show-inbound`) but its theme is STILL garbage (the theme has ZERO inbound `depends-on` — the op→theme edge is `reference`-only). Upgrading flips the three themes reachable: `reachable` +3, `detritus` −3, STRONGER GARBAGE SIGNAL −3, `rank_violations` HOLDS 0. Completes the reachable-BLAS-leaf L1>L0 theme-grounding the c110/c111 axpy-family + c113 set_subvector_zero passes began; closes the dot/nrm2/scal half of `blas1-l1-l0-lowering-theme-gap`. Plan-tag `graded-stack-lazy-tail-typing` (grounding sub-tranche).
- **HYGIENE-ONLY EXCLUSIONS (accurate framing, NOT scoped)**: `normalize`/`reciprocal`/`elementwise_product` themes are also un-grounded BUT their OPS are THEMSELVES garbage (RE5 baseline-exception nodes — `--show-inbound` confirms `L1/normalize`, `L1/reciprocal`, `L1/elementwise_product` are all `[garbage?]`), so grounding their op→theme edge would NOT flip the theme reachable (the op carries no liveness down). Left to the batch-36 meta-phase's RE-handling — explicitly NOT in D2's scope.

## Overlap analysis

- **D1 ∩ D2**: D1 writes `book/src/L1/{fe_assemble,fe_space}.md`; D2 writes `book/src/L1/{dot,nrm2,scal}.md`. **DISJOINT file sets** — no shared file, no shared operator name. Edge targets are distinct (`weak_form_term`/`fe_space`/`fe_collection` for D1; the three `-mutation-rotation` themes for D2). **NOT overlapping → PARALLEL.**
- **No consolidated-tally collision**: both are per-page frontmatter edits; neither touches a layer index, a cohort running count, or `feature/index.md`. (The parallel-blind-shared-index guard does not apply.)
- **No new-slug forward-reference**: every edge target is an EXISTING stable on-disk slug, verified present (`weak_form_term.md`, `fe_space.md`, `fe_collection.md`, `dot-mutation-rotation.md`, `nrm2-mutation-rotation.md`, `scal-mutation-rotation.md` all exist). The cross-report-forward-reference-slug-divergence guard does not apply.
- **No floor-landing/adjacent-reanchor coupling**: no new floor entry lands; these are edge upgrades on existing firm entries.
- **Contamination-friction** (`parallel-dispatch-reachability-measurement-contamination`, ledger-and-monitor, batch-35 NO-GO): disjoint file sets isolate each dispatch's reachability self-measure. Each producer reports ONLY its own standalone delta (D1 +3, D2 +3); the authoritative cumulative is the integrator-finalize step-5b re-measure on the landed tree (do NOT sum per-dispatch isolation deltas — the c110/c111/c112/c113 two-disjoint-`layer-intro-author` shape that HELD; the per-report-integrator re-measure + critic safety net catches any drift).

## Sequencing schedule

- **Wave 1 (parallel): D1, D2.** Disjoint frontmatter-only file sets; no forward-reference dependency; both grounded by edges to already-firm targets. Single wave.
- Then the standard pipeline: 2 critics (parallel) → repairers as needed → `integrator-per-report` ×2 (serial) → ONE `integrator-finalize` (rebuild book + step-5b linter re-measure + commit + push). The batch-36 meta-phase fires AFTER this finalize as a separate dispatch.

## Deliverable-presence verification (paste-inline evidence)

All scopes resolve to named `book/src/L1/*.md` paths → the four-step deliverable-presence check applies. Both dispatches are GROUNDING edge-upgrades on existing chapters (open by the c113 routing), but I verified file existence + maturity + that the grounding is genuinely undone on disk + reachability of each target.

**D1 — FE-assemble cluster (`fe_assemble`, `fe_space`, targets `weak_form_term`/`fe_space`/`fe_collection`):**
1. **File existence** — `ls` all 4 files: EXIST.
   ```
   book/src/L1/fe_assemble.md   EXISTS  (## Status @ :200)
   book/src/L1/weak_form_term.md EXISTS  (## Status @ :225)
   book/src/L1/fe_space.md      EXISTS  (## Status @ :166)
   book/src/L1/fe_collection.md EXISTS  (## Status @ :182)
   ```
2. **Maturity** — all four lead `## Status` with `` `firm` `` (fe_assemble "PROMOTE — clean"; weak_form_term "PROMOTE — clean (pulled, not speculative)"; fe_space/fe_collection "firm (firm-on-positive-structure)"). The grounding is NOT already present: `fe_assemble.md` frontmatter is LEGACY (`firmness: firm`, `lowers_to:`, **`depends_on: []`** — empty, no canonical `edges:`); `fe_space.md` has ONLY `status: firm` (no edges). The faithful `composes` edges are absent → dispatch is a real edit, not a no-op.
   - `--show-inbound` confirms: `L1/fe_assemble <- [boundary-mode/driven/eigenmode/electrostatic/lifecycle/magnetostatic/transient].L1` (REACHABLE, 7 columns); `L1/weak_form_term` = `[GARBAGE*]`; `L1/fe_space` = `[garbage?]`; `L1/fe_collection` = `[garbage?]`. The three targets are garbage AND `fe_assemble`/`fe_space` are the reachable consumers → grounding propagates liveness down = real +3.
3. **OQ RESOLVED-grep** — `weak_form_term` groundable finding is OPEN (c113 D1 routed it as a c114 candidate, NOT closed). Not stale.
4. **Structural block** — none. Faithful `composes` edges from a firm reachable op to firm deps; `rank(op=firm) ≤ rank(dep=firm)` holds for all three; no obstruction/test-coverage gate (firm-on-positive-structure). The signature `fe_assemble :: (space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> ...` (`fe_assemble.md:60`) makes both `fe_assemble` edges faithful by construction.
   - **VERDICT: D1 OPEN — 4/4 pass. Real +3 grounding.**

**D2 — reachable-op theme sweep (`dot`, `nrm2`, `scal`, targets the three `-mutation-rotation` themes):**
1. **File existence** — all 6 files (3 ops + 3 themes) EXIST.
   ```
   book/src/L1/dot.md  EXISTS  | book/src/L1-L0/dot-mutation-rotation.md  EXISTS
   book/src/L1/nrm2.md EXISTS  | book/src/L1-L0/nrm2-mutation-rotation.md EXISTS
   book/src/L1/scal.md EXISTS  | book/src/L1-L0/scal-mutation-rotation.md EXISTS
   ```
2. **Maturity / grounding-undone check** — all 3 ops are `rank: firm`; all 3 themes lead `## Status` with `` `firm` ``:
   ```
   dot-mutation-rotation:  "`firm` — the rewrite is the structural expansion of the L1 `dot` reduction..."
   nrm2-mutation-rotation: "`firm` — the rewrite is the structural expansion of the one-line L0 `Norml2`..."
   scal-mutation-rotation: "`firm` — the rewrite is a single structural buffer re-bind..."
   ```
   The grounding is NOT present — each op carries the theme as `reference`-only:
   ```
   dot.md  frontmatter: edges: reference: [L1-L0/dot-mutation-rotation, concepts/dot]   (NO depends-on to theme)
   nrm2.md frontmatter: edges: depends-on: [L1/dot]; reference: [L1-L0/nrm2-mutation-rotation]  (theme is reference-only)
   scal.md frontmatter: edges: reference: [..., L1-L0/scal-mutation-rotation]   (NO depends-on to theme)
   ```
   `--show-inbound` confirms: `L1/dot`, `L1/nrm2`, `L1/scal` all NOT in the garbage list (REACHABLE); the inbound-grep for `L1-L0/{dot,nrm2,scal}-mutation-rotation <- ...` returns EMPTY (zero inbound `depends-on` → themes garbage). Edge upgrade = real +3.
3. **OQ RESOLVED-grep** — `stale-pre-c108-rank-direction-error-prose-on-L1-ops` is the c113 D2-routed candidate friction (the systematic sweep), OPEN. Not stale.
4. **Structural block** — none. `rank(op=3) ≤ rank(theme=3)` holds (themes lead firm). NO stale "rank-direction error" prose to fight (grep: `L1/dot` 0, `L1/nrm2` 0, `L1/scal` 0 matches) — so D2 is a PURE edge upgrade (simpler than c113 D2, which also had to fix prose).
   - **VERDICT: D2 OPEN — 4/4 pass. Real +3 grounding.**

**STOP-PROPOSING negative-list check**: my target slugs (`fe_assemble`, `fe_space`, `weak_form_term`, `fe_collection`, `dot`, `nrm2`, `scal`) are NONE of the disqualified slugs (`lu_solve`, `back_solve`, `ls-update-column`, `nleps_*`). **PASS.**

**promotion_frontier check**: the 8 frontier members (`bicgstab`/`minres`/`eigsolve-convergence-reason-mapping`/`deflate`/`deflate-composition-lowering`/`boundary-mode.{L4,L1,L0}`) are all obstruction-/demand-gated — NONE proposed. **PASS.**

## Linter baseline (measured on disk this invocation, clean landed tree at `d88f003`)

```
files=355, typed=295, untyped=60, roots=36, reachable=124, rank_violations=0,
unresolved_depends_on_targets=0, promotion_frontier=8, detritus=135 (STRONGER GARBAGE SIGNAL=24)
```
Matches the c113 finalize report (`reachable=124`, `detritus=135`, STRONGER GARBAGE SIGNAL=24, `rank_violations` HELD 0). Expected after this cycle (subject to finalize step-5b authoritative re-measure): `reachable` 124 → 130 (D1 +3 fe-cluster, D2 +3 dot/nrm2/scal themes), `detritus` 135 → 129, STRONGER GARBAGE SIGNAL 24 → 18, `rank_violations` HOLDS 0, `untyped` HELD (D1 migrates `fe_assemble`'s legacy frontmatter + types `fe_space`'s — `fe_space` was shim-counted typed via `status:`, `fe_assemble` via legacy `lowers_to`, so `untyped` likely HELD per the c112 F1 auto-migration finding).

## Open questions / caveats

- **The c114 cumulative is +6 only if D1's three edges + D2's three edges all flip cleanly AND there is no shared transitive node** — they don't share nodes (D1 grounds the FE-assembly cluster; D2 grounds the BLAS-1 reduce/scal themes), so +6 is the analytic expectation. The authoritative figure is the finalize step-5b re-measure (do NOT sum per-dispatch isolation deltas).
- **`untyped` may NOT decrement** for `fe_assemble` (legacy `lowers_to`/`depends_on` auto-migrated, shim-counted typed already — the c112 F1 finding) — frame D1 as a reachability +Δ (Axis-2), NOT an `untyped` decrement (Axis-1). `fe_space` carries only `status: firm` (also a typed shim) so likewise. This cycle's measurable movement is entirely on the reachability axis.
- **For the batch-36 meta-phase (fires after this finalize):** the RE6-RE8 ratification batch (c113 D1's 12 baseline-exception recommendations) remains OPEN and is the meta-phase's job — I did NOT pre-ratify. Additionally surface: the **RE5 hygiene-only ops** (`normalize`/`reciprocal`/`elementwise_product` — themselves garbage) whose L1>L0 themes remain un-grounded reachable-dead; these are a representation-hygiene (stale `reference`-only edge) question, NOT a reachability +Δ, and should be folded into the RE5/RE6 handling (their op→theme edge can be upgraded for hygiene but will not flip the theme reachable until the op itself grounds via its consuming leg's promotion condition). Frame accurately in the RE ledger so a future cycle doesn't re-propose them as a +Δ.
- **After D1's `fe_assemble → fe_space` ground**, `fe_space`/`fe_collection` become a small reachable FE-construction sub-chain. If a later cycle wants the FE-construction L1>L0 themes (`fe-space-construction-rotation`, `fe-collection-construction-rotation`, `weak-form-term-rotation` — all currently garbage) grounded, those become the analogous reachable-op theme-sweep targets (the c114 D2 move applied to the FE cluster) once `fe_space`/`fe_collection`/`weak_form_term` are reachable post-D1. Noted as a natural next-tranche candidate, NOT scoped this cycle.
