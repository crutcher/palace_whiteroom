---
agent: layer-intro-author
invoked_at: 2026-06-09T050310Z
scope: cycle-154 D2 — three small finite-backlog hygiene de-bulks (direct-edit, de-bulk convention)
status: pending
integrated_at: 2026-06-09T051526Z
integration_commit: 40b69f2eba4d07c7b9c75d185f6b357191fe326c
integration_notes: |
  batch-51 CONVERGENCE OPENER (cycle-154, 1/3 of meta-batch-51). Applied clean by integrator-per-report
  (1 staging row). 3 small hygiene de-bulks across 4 files (5 ins / 47 del) discharging all 3 batch-51-head
  Backlog-Low items: feature/capacitance.L4.md + feature/sparameters.L4.md (output-product) H1 gloss;
  concepts/dependency-map.md date-less meta-review #N clauses dropped; concepts/constructed-operators.md
  42-line duplicate concept body removed (2 unique links lifted). Baseline HELD EXACTLY
  (files=392, typed=331, untyped=61, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=11,
  detritus=123, true_detritus=51); cargo make book EXIT 0; step-5b/5c/5d clean. NO node/edge/rank/status moved.
---

# CYCLE: c154-D2 three small de-bulks

## Summary

Three distinct-file hygiene de-bulks landed by direct edit (de-bulk convention). All citations + live links preserved; lint baseline HELD EXACTLY; `cargo make book` EXIT 0.

Files touched (4, all distinct):
- `book/src/feature/capacitance.L4.md`
- `book/src/feature/sparameters.L4.md`
- `book/src/concepts/dependency-map.md`
- `book/src/concepts/constructed-operators.md`

## Fix 1 — `feature-l4-h1-convention-tail-normalize`

**What changed.** Confirmed the 6 output-product `feature/*.L4.md` columns by reading H1 lines: `capacitance`, `sparameters`, `inductance`, `eigenfrequency-qfactor`, `energy-fields`, `waveguide-mode`. Of these, `inductance` / `eigenfrequency-qfactor` / `energy-fields` / `waveguide-mode` already carried the `(output product)` H1 tail; **`capacitance` and `sparameters` lacked it** (exactly the planner's 2). Added `(output product)` to those two H1 tails:
- `# capacitance — L4 composition-root` → `# capacitance — L4 composition-root (output product)`
- `# sparameters — L4 composition-root` → `# sparameters — L4 composition-root (output product)`

The 6 output-product columns now uniformly carry the gloss. Left the non-output-product columns untouched (verified their H1s): driver-leaf (`boundary-mode`, `driven`, `eigenmode`, `electrostatic`, `magnetostatic`, `transient`) and spine-ROOT (`lifecycle`) read bare `— L4 composition-root`; kernel/backend-composition columns carry their own DECIDED-KEPT distinguishing glosses (`geometric-multigrid preconditioner — L4 composition-root`, `Krylov-iteration spine — L4 composition-root`, `matrix-free operator — L4 backend-lowering composition-root`). TOC-navigability gloss normalization per `heading-metadata-hygiene` — glosses kept, output-product ones made consistent.

## Fix 2 — `dependency-map-dateless-meta-review-n-refs-debulk`

**What changed.** `book/src/concepts/dependency-map.md` lines 92–93 carried date-less `meta-review #N` process-attribution clauses. Dropped the process clauses, keeping the static carry-through facts (already stated in `rotation.md` / `variant-absorption.md`):
- `rotation` bullet: `Codified meta-review #1; expanded with carry-through clause meta-review #2.` → `, with a carry-through clause.` (static fact: rotation has a carry-through clause).
- `variant-absorption` bullet: `levels-of-absorption refinement meta-review #3 (invariant / procedural / primitive-sequence)` → `refined into levels of absorption (invariant / procedural / primitive-sequence)` (static fact: the three levels).

**Verification.** `grep -nE 'meta-review #[0-9]' book/src/concepts/dependency-map.md` → exit 1, **0 matches**.

## Fix 3 — `constructed-operators-duplicate-concept-body-dedup`

**Inbound-anchor check (done first).** `grep -rn 'constructed-operators.md#' book/src` → **no output** (zero inbound anchor links targeting any heading of the page). The duplicate block's headings (`#concept-constructed-operators`, `#when-to-use`, `#canonical-example`, `#slices-that-use-this-methodology`) had no inbound link targets, so no re-pointing was required.

**Unique-content lift before removal.** The duplicate second block (former lines 175–216: `## Concept: constructed operators` / `## When to use` / `## Canonical example` / `## Slices that use this methodology`) was a pure re-statement of the canonical §9–171 content (Context / When to construct / Worked example / Use in GMRES-FGMRES). The only content NOT already in markdown-link form in the canonical block were two live links that lived only in the duplicate:
- `[apply_BA](./apply_BA.md)` — the canonical §Use-in-GMRES-FGMRES had bare-text `apply_BA`.
- the firm `[krylov_step (GMRES instance)](../L2/krylov_step.md)` cross-link.

Both are ALSO carried by the frontmatter `edges: reference:` block (`concepts/apply_BA`, `L2/krylov_step`) — the authoritative graph edges — but to preserve the reader-facing inline navigational links I lifted them into the canonical §Use-in-GMRES-FGMRES paragraph FIRST:
- bare `apply_BA(op, v) → (w, z)` → `[apply_BA(op, v) → (w, z)](./apply_BA.md)`
- appended `See the firm [krylov_step (GMRES instance)](../L2/krylov_step.md).` to that paragraph.

Then removed the duplicate second block (42 lines). Page now ends cleanly at `## Use in GMRES / FGMRES`.

**Citations / links before→after (match).** All `apply_BA` and `L2/krylov_step` references preserved: frontmatter edges intact (lines 6–7), both markdown links present in canonical §Use-in-GMRES-FGMRES (line 173). No citation dropped (this page carries no L0 pinpoint citations; it is a methodology concept page). No node/edge/rank/status/slug/anchor change.

## Safety verification

- **Citations before/after:** match (no L0 pinpoint citations on any touched file dropped; all live `[link](...)` preserved — `apply_BA.md`, `../L2/krylov_step.md` lifted-and-kept; `rotation.md`/`variant-absorption.md` links unchanged in fix 2).
- **No rank/status sole-carrier at risk:** all 4 touched files are concept/feature pages — `constructed-operators.md` carries `kind`-style frontmatter (no `rank:`/`## Status` rank-carrier); `dependency-map.md` is a navigational concept page; the two `feature/*.L4.md` are `kind: feature-surface` (no `rank:`). No sole-rank-carrier touched.
- **Lint baseline — HELD EXACTLY:** `python3 tools/graded-stack-lint/graded_stack_lint.py --book-src book/src`:
  `files=392, typed=331, untyped=61, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123 (true_detritus=51 / 72 reference-reachable)`. Matches the prescribed baseline.
- **Build:** `cargo make book` EXIT 0. The single `warning: Potential incomplete link` is in `concepts/plane-rotation-stream.md:17` (pre-existing KaTeX-in-text false positive, NOT a touched file). None of the 4 touched files appear in any build error/warning.

## Open questions / caveats

None. All three fixes are pure hygiene de-bulks within the stated finite backlog; no node/edge/rank/status/semantics movement.
