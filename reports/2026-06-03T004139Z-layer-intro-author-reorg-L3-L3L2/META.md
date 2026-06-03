---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T010500Z
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
  chapter-preservation: pass
  alpha-sort-correctness: warning
  small-part-guard: pass
  normalize-placement: pass
  group-intro-pages: pass
  old-anchor-fidelity: pass
repaired_at: 2026-06-03T011500Z
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
  chapter-preservation: repaired
  alpha-sort-correctness: repaired
  small-part-guard: not-needed
  normalize-placement: not-needed
  group-intro-pages: not-needed
  old-anchor-fidelity: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L3 + L3>L2 directive-3 structural reorg"

## Critique

This is a directive-3 STRUCTURAL-REORG dispatch (pure SUMMARY regroup + index dep-map / theme-table re-sort + 5 new group-intro pages; no new operator/theme claims). The four claim-shaped checks (citation-validity, surface-or-evidence, rotation-quality, variant-axis-coverage) no-op on a pure reorg and are marked `pass` as not-applicable. The adapted structural checklist is the substance.

### Checks run

**chapter-preservation (load-bearing) — pass.** Counted the actual `- [...]` lines in the on-disk `# L3` SUMMARY block (`book/src/SUMMARY.md:45-65`, excluding Overview): **21 chapters**. Cross-checked against the on-disk `book/src/L3/` directory: **21 chapter `.md` files** (excluding `index.md`). The report's five `[new]` groupings sum to **8+3+2+3+5 = 21**, and the union {apply_linop, assemble-diagonal, axpby, axpbypcz, axpy, chebyshev, divfree-projector, dot, eigsolve, elementwise_product, fold_solve, inner_product, jacobi-smoother, krylov-step, ksp_solve, linear_combination, normalize, nrm2, orthogonalize, reciprocal, scal} is **exactly** the 21 on-disk slugs — every `[old]` slug appears exactly once in `[new]`, no drop, no rename, no re-path. No dead link will result. L3>L2: on-disk `book/src/L3-L2/` has **6 theme files** (excluding index); the report's `[new]` flat group lists exactly those 6. Chapter/theme preservation is clean. **HOWEVER the report's own prose says "22 chapters" in three places (CYCLE.md:12, :283/285 "Chapters currently harvested at L3 (22…)") while its tally bullet (CYCLE.md:251, :263) says "17 firm + 4 partial-obstruction" = 21, and the actual disk count is 21.** The "22" is a stale headline count contradicting both the report's own 17+4 tally and disk. The *structural mapping is correct at 21*; only the narrative count-claim is wrong. Recorded as an issue (cosmetic, non-load-bearing — no chapter is actually unaccounted for), not a preservation failure.

**alpha-sort-correctness — warning.** Within-group alpha is clean for 4 of 5 L3 groupings and for the L3>L2 flat group (chebyshev-nested-recurrence < eigsolve-opaque-eigen-iteration < fold-solve-time-step-body < krylov-step-body-identity < ksp-solve-outer-driver < orthogonalize-variant-split; note `krylov` < `ksp` at position 2, 'r'<'s' — correct). **The BLAS-1 grouping is mis-sorted:** the report orders `axpbypcz, axpby, axpy`, but correct lexicographic order is `axpby, axpbypcz, axpy` — "axpby" is a proper prefix of "axpbypcz" so "axpby" sorts FIRST. The report has `axpbypcz` and `axpby` swapped. This defect is **replicated consistently** in three places: the SUMMARY `[new]` block (CYCLE.md:73-74), the index.md dep-map BLAS-1 sub-table `[new]` (CYCLE.md:207-208), and the §"Alpha ordering verified" evidence list (CYCLE.md:288, which asserts `{axpbypcz, axpby, axpy, …}` — itself wrong). Remaining BLAS-1 tail (dot, inner_product, linear_combination, nrm2, scal) and all other groups are correctly ordered. Flagged `warning` (not `fail`): no link breaks, the fix is a single adjacent swap propagated to the three locations.

**small-part-guard — pass.** All 5 L3 groupings have ≥2 members (smallest is Operator-application & introspection at 2: apply_linop, assemble-diagonal — a genuine operator-action / operator-to-data sibling pair, not a manufactured nesting). No singletons. The kinds match the `L3/index.md` §Semantics-overlay + §Working-Notes c036 cohort prose (BLAS-1 / elementwise / operator-apply / smoother-gate / solver-caps-field-transitions). L3>L2 kept flat at 6 themes (correctly below the nesting threshold; the report appropriately notes the erasure-scope taxonomy as a *future* candidate nesting axis but declines to act on it). Guard honored.

**normalize-placement — pass.** `normalize` appears exactly once, under Elementwise field operations (SUMMARY CYCLE.md:83; dep-map CYCLE.md:221). Not duplicated, not dropped. The report flags the BLAS-1-vs-Elementwise ambiguity explicitly (CYCLE.md:293) and justifies the choice via the §Semantics "fused-composite-obstruction-free" framing. Defensible either way as the task notes; placed once, correctly.

**group-intro-pages — pass.** Five `create:` blocks for `L3/blas1-intro.md`, `L3/elementwise-intro.md`, `L3/operator-apply-intro.md`, `L3/smoother-intro.md`, `L3/solver-caps-intro.md` (CYCLE.md §2-6). Each is sound orientation prose sourced from the index §Semantics overlay, and each is wired into SUMMARY as the grouping's parent link (CYCLE.md:72/81/85/88/92). Internal links in the intro pages use relative `./<slug>.md` form pointing at real sibling chapters — they resolve. The report correctly notes (CYCLE.md:295) the integrator must materialize the 5 intro files before/with the SUMMARY edit so linkcheck resolves the new parent links. No dead links.

**old-anchor-fidelity — pass.** Mechanically diffed the report's `[old]` SUMMARY block (CYCLE.md:38-69) against on-disk `book/src/SUMMARY.md:43-74`: **verbatim match** (byte-identical). The index.md dep-map `[old]` anchors (krylov-step row at CYCLE.md:194; apply_linop row at CYCLE.md:206) match the on-disk `book/src/L3/index.md` dep-map rows (lines 21, 22). The dispatch's noted initial-direct-write-then-revert left the `[old]` blocks faithful to disk. No anchor drift.

**cross-reference-integrity — pass.** All chapter/theme slugs referenced in the new SUMMARY structure resolve to on-disk files. The new sub-chapter parent links point at the 5 to-be-created intro pages (materialized by proposed-change #2-6). Intra-intro links are relative sibling links to existing chapters. No orphaned or dangling references introduced.

**plan-kind-consistency — pass.** Content shape (SUMMARY regroup + table re-sort + intro pages, zero new operator claims, no status changes) matches a directive-3 structural-reorg dispatch. The report is explicit that it does NOT change the firm/partial-obstruction tally — consistent with the kind.

**skill-uptake-survey — pass.** No reorg-specific skill is mandated for this shape; `summary-md-surgical-insert` exists but targets single-insert, not a full regroup. Pure presence check, non-blocking.

### Issues found

1. **Stale "22 chapters" count claim** — CYCLE.md:12 ("`# L3` (22 chapters)"), CYCLE.md:283/285 ("Chapters currently harvested at L3 (22…)"). Actual disk count is **21** (21 SUMMARY entries; 21 `book/src/L3/*.md` non-index files), and the report's own tally bullet (CYCLE.md:251, :263) says "17 firm + 4 partial-obstruction" = 21. The narrative headline "22" is internally contradicted by the report's own 17+4 = 21 tally and by disk. **Severity: cosmetic.** The structural mapping is correct at 21 with every chapter accounted for; only the prose count-claim is wrong. Repair: change "22" → "21" at CYCLE.md:12, :283, :285.

2. **BLAS-1 alpha-sort defect: `axpbypcz` before `axpby`** — CYCLE.md:73-74 (SUMMARY `[new]`), CYCLE.md:207-208 (index dep-map BLAS-1 sub-table `[new]`), CYCLE.md:288 (§Alpha-ordering-verified evidence list). Correct lexicographic order is `axpby, axpbypcz, axpy` (since "axpby" is a proper prefix of "axpbypcz", it sorts first). The report consistently has `axpbypcz` and `axpby` swapped. **Severity: minor** — no link breaks, deterministic single adjacent-swap fix, but it must be applied to all three locations together (SUMMARY, dep-map sub-table, evidence list) to stay consistent. Note the §"Alpha ordering verified" claim is itself the bug being self-certified, so the verification list is not load-bearing here.

3. **(Surfaced, not a defect) cross-dispatch grouping-order convention is unresolved** — CYCLE.md:292 flags that group *ordering* (alpha-by-display-name vs semantic) is not pinned by the role-spec and the five sibling reorg dispatches should agree. This is a legitimately-raised consistency question for the integrator/meta-phase, not a defect in this report. No action required of this report; noting it surfaced correctly.

---

## Repair

Both critic-flagged issues are mechanical and surgical (deterministic alpha re-sort + a prose count correction) — squarely in repair scope. No new content authored, no `book/` mutation, no `checks:` overrides. Both applied; structural mapping (21 chapters, no drop/rename) was already clean per the critic, so `overall_status: ready`.

### Fixes attempted

- **Finding (alpha-sort-correctness, warning)**: BLAS-1 sub-group orders `axpbypcz, axpby, axpy` but C-locale order is `axpby, axpbypcz, axpy` (`axpby` is a proper prefix of `axpbypcz`, sorts first); replicated in 3 places.
  - **Decision**: repaired.
  - **Action**: corrected to `axpby, axpbypcz, axpy` at all three `[new]` sites — (1) SUMMARY `[new]` BLAS-1 sub-group (CYCLE.md §"Proposed changes" #1, the `book/src/SUMMARY.md` edit block; adjacent-swap of the two list items); (2) `L3/index.md` dep-map BLAS-1 sub-table (CYCLE.md §"Proposed changes", the `book/src/L3/index.md` dep-map edit — swapped the two full table rows so the `[new]:`-prefixed row is now `axpby`); (3) §"Supporting evidence" §Alpha-ordering-verified BLAS-1 set. The `[old]` SUMMARY block (the verbatim on-disk record) was correctly left untouched.

- **Finding (chapter-preservation issue #1 / cosmetic count, low)**: prose headline says "22 chapters" but true on-disk count is 21 (report's own 17 firm + 4 partial-obstruction = 21 tally agrees).
  - **Decision**: repaired.
  - **Action**: corrected the L3 chapter-count prose "22" → "21" at CYCLE.md §Summary headline (`# L3 (21 chapters)`) and §"Supporting evidence" first bullet (`Chapters currently harvested at L3 (21, …)`). Groupings (8+3+2+3+5 = 21) left unchanged — they were already correct. The "8" BLAS-1 member-count in the §Summary grouping list is a member count, not the chapter total, and was not touched. Grep-confirmed no remaining stray "22" chapter-count reference.

### Unrepairable findings

None. The third META item (cross-dispatch grouping-order convention, CYCLE.md:292) was explicitly recorded by the critic as *surfaced, not a defect* — no repair action required; it is a consistency question for the integrator/meta-phase across the five sibling reorg dispatches.

## Suggested resolution

`ready`. Integrator notes: (a) the report depends on the 5 new `L3/*-intro.md` group-intro files being materialized before/with the SUMMARY edit (per CYCLE.md:295) so linkcheck resolves the new parent links — proposed-changes #2–#6 supply them; (b) the five sibling reorg dispatches (L4/L4-L3, L2/L2-L1, L1/L1-L0, L0, plus this L3/L3-L2) should land a consistent group-ordering convention (alpha-by-display-name here) — a cross-dispatch coherence check for integrator-finalize / meta-phase, not a blocker on this report.
