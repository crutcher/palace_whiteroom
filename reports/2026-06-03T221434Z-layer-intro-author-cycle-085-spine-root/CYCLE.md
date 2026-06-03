---
agent: layer-intro-author
invoked_at: 2026-06-03T221434Z
scope: cycle-085 batch-27 LEAD — FEATURE-SURFACE SPINE all-13-column re-evaluation; D3 = SPINE-ROOT lifecycle column (lifecycle.{L4,L1,L0})
status: integrated
integrated_at: 2026-06-03T225500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean as D3 (staging row 3, byte-disjoint; does NOT touch feature/index.md — D1 sole-owns). 3 lifecycle frontmatter flips seed→firm (lifecycle.{L4,L1,L0}) + §Status OWN-COMPOSITION re-authoring (promotes on own driver-agnostic composition: mesh-build + firm fold_solve adaptive fold; the 5 per-driver columns are sibling references, NOT blocking constituents). All 6 [old] anchors matched verbatim, no transcription drift. Retroactive-budget 0. Build exit 0. Deduped feature-column-firm-token-choice OQ (promoted by D1). Part of cycle-085 batch-27 LEAD (broke the eigenmode↔eigenfrequency-qfactor mutual-blocking deadlock; spine-ROOT promotion mechanism validated)."
---

# CYCLE: feature/lifecycle (spine-ROOT) — OWN-COMPOSITION promotion re-evaluation

## Summary

Re-evaluates the **spine-ROOT `lifecycle` meta-feature column** (3 files: `lifecycle.{L4,L1,L0}.md`) under the new **OWN-COMPOSITION column-promotion rule** (USER DIRECTIVE 2026-06-03; CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`). The rule: a column promotes off `seed` when its **OWN composition + its directly-owned constituents** are firm; **cross-linked SIBLING columns are references, NOT blocking constituents.**

For the spine-ROOT sub-kind, the per-driver dispatch (stage 2) is over the 5 driver feature columns, which are **OTHER feature columns = references**, NOT directly-owned vocabulary-op constituents. The column's directly-owned driver-agnostic vocabulary is:
- **L4**: the mesh-build L0 scaffold (stage 1) + `fold_solve` (stage 3, the state-generated adaptive estimate-mark-refine outer fold).
- **L1**: the mesh-build L0 scaffold + `fe_assemble` + `ksp_solve` (the driver-agnostic assemble + solve cap every driver bottoms out in).
- **L0**: ground-truth source surface — no firm-gated vocab constituents.

**On-disk constituent-status confirmation (this dispatch):**

| Constituent | Level(s) | On-disk `## Status` / frontmatter | Firm? |
|---|---|---|---|
| `book/src/L4/fold_solve.md` | L4 | frontmatter `firmness: firm` (line 4); body §"# fold_solve" firm apparatus present | **firm** ✓ |
| `book/src/L1/fe_assemble.md` | L1 | `## Status` (line 200): `` `firm`. **Clean-gate call: PROMOTE — clean.** `` | **firm** ✓ |
| `book/src/L1/ksp_solve.md` | L1 | `## Status`: `` `firm` — signature is canonical … evidence is direct from the Palace source `` | **firm** ✓ |
| mesh-build (`mesh::Load`/`Partition`/`RefineMesh`) | L4/L1/L0 | L0 driver-agnostic scaffold (`palace/main.cpp:287-302`) — no firm-status gate | n/a (L0 scaffold) |

**Verdict: FLIP `status: seed → firm`** at all three levels. Every directly-owned driver-agnostic constituent is firm; the per-driver dispatch is over sibling feature columns (references, not blocking constituents). This matches D1's index-narrative expectation that lifecycle lands in the firm set — no contradiction to flag.

The proposed changes (1) re-author the §Status promotion-rule prose to the OWN-COMPOSITION rule (drop the deadlock / "all five columns on disk" gating clause), and (2) flip the frontmatter `status:` token, at all three levels. Within-column high→low ordering (L4→L1→L0) is preserved. I do NOT touch `book/src/feature/index.md` (D1 sole-owns it) — the matrix-cell flip for lifecycle is deferred to D1.

## Proposed changes

### lifecycle.L4.md

```edit:book/src/feature/lifecycle.L4.md
[old]: kind: feature-surface
feature: lifecycle
level: L4
status: seed
composes:
[new]: kind: feature-surface
feature: lifecycle
level: L4
status: firm
composes:
```

```edit:book/src/feature/lifecycle.L4.md
[old]: ## Status

`seed` — the spine ROOT composition root, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the first **meta-feature** of the feature-surface kind (constituents include other feature columns, not only vocabulary combinators). The composition is sound: the mesh-build + adaptive-fold stages are driver-agnostic, and stage (3) IS the firm [`fold_solve`](../L4/fold_solve.md) in its state-generated `schedule-source` form (verified firm from on-disk `## Status` this dispatch); stage (2) dispatches over the per-driver feature columns ([`electrostatic.L4`](./electrostatic.L4.md), [`magnetostatic.L4`](./magnetostatic.L4.md), [`eigenmode.L4`](./eigenmode.L4.md), [`driven.L4`](./driven.L4.md), [`transient.L4`](./transient.L4.md) — all five on disk, live-linked). This chapter carries the *compositional* claim only (lifecycle = adaptive-fold-over-driver-dispatch), not the per-column or per-op claims (those live in the linked columns / chapters). Evidence: the L0 driver-agnostic range `palace/main.cpp:158-328` + `palace/drivers/basesolver.cpp:153-276` realizing the composition, plus the firm [`fold_solve`](../L4/fold_solve.md) constituent down-link + the per-driver column down-links. Rotation / variant-axis claims no-op (no rotation, no variant-axis catalogue — the compositional claim only).
[new]: ## Status

`firm` — the spine ROOT composition root, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the first **meta-feature** of the feature-surface kind (constituents include other feature columns, not only vocabulary combinators).

**Promotion under the OWN-COMPOSITION rule** (USER DIRECTIVE 2026-06-03; CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE). This column promotes off `seed` because its **OWN driver-agnostic composition + its directly-owned constituents** are firm; the per-driver dispatch (stage 2) is over **sibling feature columns**, which are **references, NOT blocking constituents** (the spine-ROOT sub-kind: stage-(2) constituents are *other feature columns*). The directly-owned driver-agnostic constituents are: the mesh-build L0 scaffold (stage 1) + the firm [`fold_solve`](../L4/fold_solve.md) state-generated adaptive estimate-mark-refine outer fold (stage 3) — verified firm from `fold_solve.md` frontmatter `firmness: firm` on-disk this dispatch. The per-driver columns ([`electrostatic.L4`](./electrostatic.L4.md), [`magnetostatic.L4`](./magnetostatic.L4.md), [`eigenmode.L4`](./eigenmode.L4.md), [`driven.L4`](./driven.L4.md), [`transient.L4`](./transient.L4.md)) are the specializations this ROOT dispatches over; their own `status:` does not gate the ROOT's (each promotes on its own composition, the reciprocal of this rule). This supersedes the earlier "promote past `seed` only once all five driver columns are firm" gating, which (with the directive-3 reciprocal cross-linking) created the mutual-blocking `seed` deadlock the directive exists to break.

This chapter carries the *compositional* claim only (lifecycle = adaptive-fold-over-driver-dispatch), not the per-column or per-op claims (those live in the linked columns / chapters). Evidence: the L0 driver-agnostic range `palace/main.cpp:158-328` + `palace/drivers/basesolver.cpp:153-276` realizing the composition, plus the firm [`fold_solve`](../L4/fold_solve.md) constituent down-link + the per-driver column down-links. Rotation / variant-axis claims no-op (no rotation, no variant-axis catalogue — the compositional claim only).
```

### lifecycle.L1.md

```edit:book/src/feature/lifecycle.L1.md
[old]: kind: feature-surface
feature: lifecycle
level: L1
status: seed
composes:
[new]: kind: feature-surface
feature: lifecycle
level: L1
status: firm
composes:
```

```edit:book/src/feature/lifecycle.L1.md
[old]: ## Status

`seed` — the L1 pure-function composition root for the lifecycle meta-feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: the mesh-build + estimate-mark-refine fold are driver-agnostic scaffold (the fold is the firm [`fold_solve`](../L4/fold_solve.md) state-generated shape at L4); the per-driver dispatch composes the per-column pure functions (2 on disk — [`electrostatic.L1`](./electrostatic.L1.md), [`magnetostatic.L1`](./magnetostatic.L1.md); 3 forthcoming). This chapter carries the compositional claim only (lifecycle = dispatch-over-driver-columns under the adaptive fold), not the per-column algebraic claims (those live in the per-driver columns) nor the per-op claims (those live in the vocabulary chapters). Evidence: the L0 driver-agnostic range `palace/main.cpp:158-328` + `palace/drivers/basesolver.cpp:153-276` realizing the composition, plus the per-driver column down-links.
[new]: ## Status

`firm` — the L1 pure-function composition root for the lifecycle meta-feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02).

**Promotion under the OWN-COMPOSITION rule** (USER DIRECTIVE 2026-06-03; CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE). This column promotes off `seed` because its **OWN driver-agnostic composition + its directly-owned constituents** are firm; the per-driver dispatch is over **sibling feature columns** = **references, NOT blocking constituents** (the spine-ROOT sub-kind). The directly-owned driver-agnostic constituents are: the mesh-build L0 scaffold + the firm [`fe_assemble`](../L1/fe_assemble.md) (driver-agnostic mesh→operator assemble) + the firm [`ksp_solve`](../L1/ksp_solve.md) (the solve cap every driver's per-step body bottoms out in) + the firm [`fold_solve`](../L4/fold_solve.md) state-generated estimate-mark-refine fold (at L4) — all verified firm from their on-disk `## Status` lines this dispatch (`fe_assemble.md:200` `firm`; `ksp_solve.md` `firm`; `fold_solve.md` `firmness: firm`). The per-driver columns ([`electrostatic.L1`](./electrostatic.L1.md), [`magnetostatic.L1`](./magnetostatic.L1.md), and the eigenmode / driven / transient columns) are the specializations this ROOT dispatches over; their own `status:` does not gate the ROOT's. This supersedes the earlier "promote only once all driver columns are firm" gating that created the `seed` deadlock the directive breaks.

This chapter carries the compositional claim only (lifecycle = dispatch-over-driver-columns under the adaptive fold), not the per-column algebraic claims (those live in the per-driver columns) nor the per-op claims (those live in the vocabulary chapters). Evidence: the L0 driver-agnostic range `palace/main.cpp:158-328` + `palace/drivers/basesolver.cpp:153-276` realizing the composition, plus the per-driver column down-links.
```

### lifecycle.L0.md

```edit:book/src/feature/lifecycle.L0.md
[old]: kind: feature-surface
feature: lifecycle
level: L0
status: seed
l0_ground_truth:
[new]: kind: feature-surface
feature: lifecycle
level: L0
status: firm
l0_ground_truth:
```

```edit:book/src/feature/lifecycle.L0.md
[old]: ## Status

`seed` — the L0 ground-truth surface for the top-level lifecycle meta-feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). Every stage is a cited range into `palace/main.cpp` + `palace/drivers/basesolver.cpp` / `.hpp`, confirmed on-disk via palace-codemap `read_range` this dispatch (`palace/main.cpp:140-328`, `palace/drivers/basesolver.cpp:153-276`, `palace/drivers/basesolver.hpp:31-67`). This is a NOVEL feature sub-kind — a **meta-feature whose constituents include other feature columns** (the per-driver specializations) rather than only vocabulary ops; the surface-or-evidence evidence is the driver-agnostic source range + the specialization-seam site map + the per-driver column down-links. Rotation / variant-axis claims no-op (no rotation, no variant-axis catalogue — the chapter carries only the compositional claim).
[new]: ## Status

`firm` — the L0 ground-truth surface for the top-level lifecycle meta-feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02).

**Promotion under the OWN-COMPOSITION rule** (USER DIRECTIVE 2026-06-03; CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE). This column promotes off `seed` because its **OWN composition** — the driver-agnostic lifecycle source surface — is fully cited and firm; the per-driver dispatch at the `switch (iodata.problem.type)` specialization seam is over **sibling feature columns** = **references, NOT blocking constituents** (the spine-ROOT sub-kind). Every stage is a cited range into `palace/main.cpp` + `palace/drivers/basesolver.cpp` / `.hpp`, confirmed on-disk via palace-codemap `read_range` (`palace/main.cpp:140-328`, `palace/drivers/basesolver.cpp:153-276`, `palace/drivers/basesolver.hpp:31-67`); there are no firm-gated vocabulary constituents at L0 (the surface IS the ground truth). The per-driver column down-links ([`electrostatic.L0`](./electrostatic.L0.md), [`magnetostatic.L0`](./magnetostatic.L0.md), and the eigenmode / driven / transient columns) are the specializations this seam selects; their own `status:` does not gate this ROOT's. This is a NOVEL feature sub-kind — a **meta-feature whose constituents include other feature columns** (the per-driver specializations) rather than only vocabulary ops; the surface-or-evidence evidence is the driver-agnostic source range + the specialization-seam site map + the per-driver column down-links. Rotation / variant-axis claims no-op (no rotation, no variant-axis catalogue — the chapter carries only the compositional claim).
```

## Supporting evidence

- **OWN-COMPOSITION rule** — CLAUDE.md §Extraction-goal (FEATURE-SURFACE SPINE, "Column promotion off `seed`"); role-spec `.claude/agents/layer-intro-author.md` §FEATURE-SURFACE; memory `project_feature_column_promotion_rule`. The spine-ROOT sub-kind: the lifecycle chapter's stage-(2) constituents are OTHER feature columns (references) + driver-agnostic firm vocabulary; under OWN-COMPOSITION the sibling driver columns are references, NOT directly-owned vocab-op constituents.
- **Directly-owned driver-agnostic constituents — on-disk `## Status` confirmation (this dispatch):**
  - `book/src/L4/fold_solve.md` — frontmatter `firmness: firm` (line 4), full firm apparatus (signature + variant-axes + evidence) in body. **firm.**
  - `book/src/L1/fe_assemble.md` — `## Status` (line 200): `` `firm`. **Clean-gate call: PROMOTE — clean.** `` **firm.**
  - `book/src/L1/ksp_solve.md` — `## Status`: `` `firm` — signature is canonical … evidence is direct from the Palace source `` **firm.**
  - mesh-build (`mesh::Load`/`Preprocess`/`Partition`/`RefineMesh`, `palace/main.cpp:287-302`) — driver-agnostic L0 scaffold, no firm-status gate.
- **Sibling driver columns** (electrostatic / magnetostatic / eigenmode / driven / transient) at all 3 levels are on disk and live-linked; under the OWN-COMPOSITION rule they are references, so their individual `status:` (seed/firm, re-evaluated by D1) does NOT gate the lifecycle ROOT. The reciprocal cross-links stay in place (drift-guard) and are unchanged by this dispatch.
- **No new claims requiring fresh citations** — all L0 citations in the three files are pre-existing and unchanged; only the `status:` token + §Status promotion-rule prose are edited.

## Open questions / caveats

- **Index-cell flip deferred to D1 (single-index-owner).** This dispatch flips lifecycle's chapter `## Status` + frontmatter `status:` token at all 3 levels but does NOT touch `book/src/feature/index.md` (D1 sole-owns the shared matrix + the `# Feature surfaces` SUMMARY block per the single-index-owner-when-≥2-columns-land guard). Per the promotion-time index-cell-drift guard, **D1 must flip the lifecycle matrix cell(s) to `firm` in the same cycle** so the index does not lag the chapter `## Status`. Flagging here so the integrator can confirm D1 carried the matching cell flip; a lifecycle `firm` chapter with a stale `seed` index cell is the silent-drift defect.
- **No on-disk/record contradiction to flag.** The dispatch instruction's conservative branch (KEEP `seed` if a directly-owned constituent is rough-in, and flag the contradiction with D1's firm-set expectation) is NOT triggered: every directly-owned driver-agnostic constituent is firm, so lifecycle lands firm as D1's index narrative expects. No reconciliation needed.
- **Spine-ROOT nesting / by-kind grouping unchanged.** This dispatch is a status re-evaluation only; the Feature Part's three-kind grouping (spine-ROOT / driver-leaf / output-product) and the within-column high→low (L4→L1→L0) ordering are untouched. The one-time by-kind reorg remains a separately-sequenced meta-phase structural wave.
