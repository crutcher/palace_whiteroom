---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T23:57:30Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-30T00:01:41Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L1>L0 theme sketch — back-solve-mutation-rotation (firm)

## Critique

### Checks run

**citation-validity — pass.** Ran `python3 tools/citecheck/citecheck.py --scan reports/2026-05-29T205945Z-abstractor-back-solve-mutation-rotation/CYCLE.md --quiet` → `41 ok, 0 failing (41 citations checked)`. Then spot-anchored every load-bearing pinpoint in both GMRES (`:652`, `:653`, `:655`, `:656`, `:657`, `:659`, `:666`) and FGMRES (`:831`, `:832`, `:834`, `:835`, `:836`, `:838`, `:843`) sub-patterns plus the context citations (`:612`, `:631`, `:644`) and the `iterative.hpp` register declarations (`:192`, `:193`, `:222`, `:250`, `:256`). All 22 anchor probes returned `ok` zero-drift. The producer's claimed handling of the `codemap-read-range-plus-one-drift-on-brace-boundary` hazard is genuine: FGMRES has `{` on its own line at `:833` and `:837`, which shifts every body line by exactly +1 vs the GMRES `{`-on-`for`-line style; the producer's emit-time re-anchor caught and corrected this (the cited FGMRES outer-loop line `:832`, not the comment `:831`, is the `for` statement). The leaf-back-reference citations (`book/src/L1/back_solve.md:78` signature, `:187-195` law 1, `:207-215` law 4, `:218-221` law 5, `:223-230` law 6, `:234-243` reduction-order non-law, `:249-254` singular-R applicability) were spot-checked against the live file and all map to the cited content. The producer's reported "20+ citations zero drift this invocation" matches my independent run (41 mechanical + 22 anchor-spot-checks).

**surface-or-evidence — pass.** This is a refinement-shaped proposal that lands a NEW chapter (`book/src/L1-L0/back-solve-mutation-rotation.md`) — the proposal mutates surface (creates the chapter, edits the L1-L0 index row, registers in SUMMARY.md) AND carries rotation-claim evidence (the four-element structural decomposition: descending outer sweep, column-major stride pointer, diagonal division, inner super-diagonal subtraction). Both arms of the surface-or-evidence gate are met. Sibling-precedent grounding (`normalize-mutation-rotation`, `matrix-weighted-norm-mutation-rotation`, `lu-solve-mutation-rotation`) is appropriate; the chapter follows the firm-on-positive-structure pattern these siblings established.

**rotation-quality — pass.** The mutation→pure rotation is genuine and structurally compact: L1 names a closed-form `y = back_solve(R, s)` consuming `(UpperTri[j+1, j+1], Tensor[j+1])` and producing a fresh coordinate vector with no destination buffer or stride machinery; L0 expands this into a four-element destructive loop with in-place RHS overwrite (`s[i] /= Hi[i]`, then inner `s[k] -= Hi[k] * s[i]`), flat column-major slab access via the stride pointer `Hi = H.data() + i*(max_dim+1)`, and a descending sweep order. The L1 representation is **strictly more compact and more abstract**: state hiding (the destination-collapsed-into-RHS aliasing disappears at L1), coarser substitution (the 2D abstract `UpperTri[j+1, j+1]` replaces the 1D flat slab + stride formula), and equational form (defining identity `R · back_solve(R, s) = s` replaces the operational loop). The load-bearing numerical detail (descending column-oriented eager-subtraction reduction order, pinning the IEEE-754 summation grouping) is explicitly recorded as a non-rewrite per the CLAUDE.md "Optimization tricks vs. base algebra" load-bearing-numerical guidance — this is correct treatment, not collapsed away. This is NOT a renaming-only or 1:1 mapping.

**variant-axis-coverage — pass.** The §Variant axes section explicitly enumerates element-type (absorbed: real/complex bound at template instantiation, same loop body), GMRES vs FGMRES (the two surface sub-patterns A/B with content-identical line-shifted recognition), restart dimension `j+1` (size parameter, absorbed-as-form), and GMRES preconditioning side `pc_side ∈ {LEFT, RIGHT}` (positively classified as NOT a variant axis of the back-solve because both branches consume the same `s[0..j]` after the back-solve — recorded as evidence the back-solve is invariant under it). Reduction-strategy and alternative-kernel and storage-layout non-axes are all explicitly noted as scoped-out with reasons. The single-column `j = 0` and empty-cycle `j = -1` boundary cases are covered by both the L1 leaf reference and the sub-pattern-A prose. No hidden branches; per `classify-variant-axis`-style enumeration.

**cross-reference-integrity — pass.** All 10 cross-referenced chapters exist on disk (`book/src/L1/back_solve.md`, `book/src/L1-L0/{normalize,matrix-weighted-norm,lu-solve}-mutation-rotation.md`, `book/src/L2/incremental-least-squares.md`, `book/src/L2-L1/{incremental-least-squares-composition-lowering,linear-combination-fold-specialization}.md`, `book/src/concepts/givens.md`, `book/src/L1/apply_linop.md`, `book/src/L2/linear_combination.md`). The SUMMARY.md insert uses a 3-line context anchor (`normalize-mutation-rotation` → new `back-solve-mutation-rotation` → `lu-solve-mutation-rotation`) which matches the current SUMMARY.md ordering at lines 107-108 — clean surgical insert. The L1-L0/index.md insert quotes `normalize-mutation-rotation` (line 31) → new `back-solve` → `nleps-deflated-residual-mutation-rotation` (line 32 trailing anchor); insertion-point is unambiguous.

**Build-readiness fence guard — pass.** Mechanical fence enumeration via `grep -n '```' CYCLE.md` returned 6 fences = 3 balanced fenced blocks (`new:` 23-797, `edit:index.md` 799-806, `edit:SUMMARY.md` 808-812). The `new:` block contains the entire firm-body apparatus INSIDE the fence: signature/L1 form at `:50-76`, L0 form at `:78-194`, sub-patterns A/B/C at `:100-323`, applicability conditions, justification kind, variant axes, verified-against citations, and the `## Status` header at line 742 with the firm-on-positive-structure rationale at `:744-787` — all enclosed before the closing fence at `:797`. There are NO nested triple-backtick fences inside the `new:` block (only 4-space-indented Markdown code blocks at lines 60, 88, 102, 225, 296), which means the producer used the cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` defensive idiom — the cycle-019 fence-truncation defect (firm body authored OUTSIDE the fence as the report's own top-level sections) is NOT present. This passes the `proposed-changes-fence-encloses-full-body-guard` skill check.

**edge-label-fidelity — pass.** Declared edge `L1>L0` (slug `back-solve-mutation-rotation` in the `L1-L0/` directory) is consistently honored: LHS is the L1 leaf `back_solve` (vocabulary: `UpperTri[j+1, j+1]`, `Tensor[j+1]`, defining identity `R · back_solve(R, s) = s`), RHS is the L0 in-place loop at `palace/linalg/iterative.cpp:652-660` (GMRES) / `:831-840` (FGMRES) — high→low direction throughout the prose. The §"L1 form (LHS)" / §"L0 form (RHS)" sectioning is explicit. The L1 leaf is consistently positioned ABOVE the L0 loop; the prose narrates the rewrite forward (L1 → L0) per the "Layers are defined high→low" invariant. The basis-lift independence boundary (Sub-pattern C) correctly defers the L2 `linear_combination` consumer to a separate L2>L1 theme rather than absorbing it into this L1>L0 edge.

**plan-kind-consistency — pass.** Declared kind `firm` matches the content shape: positive L0 anchors for every rewrite element (descending outer sweep, column-major stride pointer formula, diagonal division compound assignment, inner super-diagonal subtraction, in-place RHS overwrite, basis-invariant downstream lift); content-identical line-shifted twin-form recognition grounds the law-6 basis-lift independence; the load-bearing reduction-order non-law is recorded as such (load-bearing-numerical per CLAUDE.md taxonomy, not as algebraic rotation); the firm-on-positive-structure escape (syntactic-identity laws on fully-specified positive source, no test gating) is invoked correctly per the cycle-021 status-tier invariant — sibling precedent `lu-solve-mutation-rotation` follows the same pattern. No `rough-in` placeholders, no `partly-constructive` sub-parts (no negative-anchor reconstruction is used), no `obstruction` framing. The "firm" claim is structurally honest.

**skill-uptake-survey — pass.** The report explicitly references `classify-variant-axis` twice (`:58`, `:589`) for the variant-axis enumeration, and `verify-citation-range` once (`:627`) for the producer-self-verification narrative. The mechanical `tools/citecheck/citecheck.py --scan` / `--anchor` invocations are mentioned in §"Verification log" (`:872-883`) consistent with the cycle-024 mechanical realization of the `verify-citation-range` skill. The sibling-theme precedent reuse (normalize / matrix-weighted-norm / lu-solve) implicitly exercises the `summary-md-surgical-insert` discipline (3-line context anchors). The skill-uptake telemetry is healthy.

### Issues found

None. The report is unusually clean for a firm L1>L0 theme dispatch:

1. **All 41 citations pass `--scan` zero-drift** and 22 spot-anchored load-bearing pinpoints (GMRES + FGMRES bodies, register declarations, context anchors) all return `ok`. The +1 brace-shift hazard noted in the role prompt is correctly identified, isolated to FGMRES's `{`-on-own-line style, and every FGMRES citation is positively re-anchored against on-disk source (the producer's emit-time correction caught the hazard before it became drift).
2. **The build-readiness fence guard passes mechanically**: `new:` block fences are balanced (lines 23/797), the firm-body apparatus (`## Status`, signature, laws, verified-against) all sit INSIDE the fence, and the producer used 4-space-indented code blocks for inner code samples (the cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` defensive idiom) — no nested triple-backtick fences that could prematurely close the outer block.
3. **The rotation is genuine** (state-hiding + coarser substitution + equational form), the variant-axis enumeration is exhaustive with positive non-axis classification for `pc_side`, the edge-label `L1>L0` is consistently honored, and the firm kind matches the content shape.

The five OQ-style notes in §"Open questions / caveats" (`:884-946`) are appropriately scoped: (1) the L1 leaf's prose-tightening for "line-for-line identical" → "content-identical, line-shifted" is correctly NOT this dispatch's responsibility and queued for a future leaf-tightening pass; (2) the boundary with the staged L2>L1 `incremental-least-squares-composition-lowering` theme is clean and self-consistent; (3) the cycle-030 verified_against audit framing is correct (this audit is independent of the L2>L1 theme's audit); (4) the empty-cycle `j = -1` boundary is recorded faithfully with the runtime-reachability caveat noted as tangential; (5) the reduction-order non-law treatment matches sibling-theme precedent. None of these are defects; they are appropriate downstream-hand-off notes.

The producer's emit-time citation correction of the +1 FGMRES brace-offset — caught via `citecheck --anchor` against on-disk during authoring — is the friction-ledger-aware discipline working as intended; this is exactly the workflow the `codemap-read-range-plus-one-drift-on-brace-boundary` discipline targets, and the producer's `--anchor` self-verification before emission is the textbook realization.

## Repair

### Fixes attempted

The critic's 8-check verdict is all-pass with zero `warning` / `fail` / `unclear` findings and an explicit "Issues found: None" block. The repairer's role is to fix `warning`/`fail` findings mechanically; there are none to fix.

- **Finding**: citation-validity — pass (41/41 `--scan` zero-drift + 22 spot-anchor probes all `ok`; +1 FGMRES brace-offset hazard correctly handled at emit time via `--anchor`).
  - **Decision**: not-needed
- **Finding**: surface-or-evidence — pass (refinement-shaped proposal lands a new chapter; rotation-claim evidence carried).
  - **Decision**: not-needed
- **Finding**: rotation-quality — pass (genuine mutation→pure rotation: state-hiding + coarser substitution + equational form; load-bearing reduction-order recorded as non-rewrite per CLAUDE.md taxonomy).
  - **Decision**: not-needed
- **Finding**: variant-axis-coverage — pass (element-type / GMRES-vs-FGMRES / restart-dimension / `pc_side`-as-positively-classified-non-axis all enumerated; boundary cases `j = 0` and `j = -1` covered).
  - **Decision**: not-needed
- **Finding**: cross-reference-integrity — pass (10/10 cross-referenced chapters exist on disk; SUMMARY.md and L1-L0/index.md inserts use clean 3-line context anchors).
  - **Decision**: not-needed
- **Finding**: edge-label-fidelity — pass (L1>L0 direction consistently honored; L1 leaf above L0 loop; prose narrates forward).
  - **Decision**: not-needed
- **Finding**: plan-kind-consistency — pass (`firm` kind matches content shape; positive L0 anchors for every rewrite element; firm-on-positive-structure escape invoked correctly per cycle-021 status-tier invariant).
  - **Decision**: not-needed
- **Finding**: skill-uptake-survey — pass (`classify-variant-axis`, `verify-citation-range` mechanical realization, sibling `summary-md-surgical-insert` precedent all exercised).
  - **Decision**: not-needed
- **Finding** (auxiliary): Build-readiness fence guard — pass (3 balanced fences, firm body fully inside `new:` block, 4-space-indented inner code per cycle-024 defensive idiom; no nested triple-backtick fences).
  - **Decision**: not-needed

The five OQ-style notes in §"Open questions / caveats" are downstream-handoff scoping (leaf-prose tightening, L2>L1 boundary, cycle-030 verified_against audit framing, `j = -1` empty-cycle reachability, sibling-precedent reduction-order treatment) — the critic explicitly classifies them as "appropriate downstream-hand-off notes, not defects." No repair action is warranted on these; they will surface as OQ-ledger entries when the integrator-per-report applies the report.

### Unrepairable findings

None.

## Suggested resolution

`ready` — the integrator-per-report may apply this report's proposed-changes block as-is. Notes for the integrator:

1. The `new:` block at CYCLE.md lines 23–797 creates `book/src/L1-L0/back-solve-mutation-rotation.md` with the full firm body inside the fence (the cycle-024 4-space-indented inner-code defensive idiom is in use — apply the body as a single literal write).
2. The `edit:` blocks at lines 799–806 (L1-L0/index.md row insert) and 808–812 (SUMMARY.md surgical insert) use 3-line context anchors that match current disk state — the surgical inserts are unambiguous.
3. The five OQ-style caveats at CYCLE.md lines 884–946 should be promoted to `scaffolding/open-questions.md` per the standard per-report intake migration (the boundary with the staged L2>L1 `incremental-least-squares-composition-lowering` theme is the most actionable; the cycle-030 verified_against audit framing is a forward-pointer).
4. No follow-up dispatch is required for this report; the firm-on-positive-structure status is honest and the chapter is integration-ready.
