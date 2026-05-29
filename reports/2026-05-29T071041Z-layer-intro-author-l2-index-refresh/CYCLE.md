---
agent: layer-intro-author
invoked_at: 2026-05-29T071041Z
scope: L2 Part intro prose refresh (post cycle-020/021 landings)
status: pending
integrated_at: 2026-05-29T1130Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-022 report 7/9 (wave-1, final wave-1). Applied clean — navigational L2 Part-intro refresh (no firmness promotion); dropped the stale 'L3 ksp_solve not on disk' clause, live-linked the firm L3 entry + L3>L2 theme; discharged 2 L2-intro-refresh flags + 1 working-note-staleness OQ. No count change. retroactive-budget 0; build clean. See reports/cycle-022-integrator-staging/STAGING.md row 7 + reports/2026-05-29T1130Z-integrator-finalize-cycle-022/CYCLE.md."
---

# CYCLE: L2 index refresh

## Summary

Navigational hygiene refresh of `book/src/L2/index.md` to reflect the cycle-020/021 `ksp_solve` landings. Three surgical edits, all intra-book (no L0-citation changes):

1. **Dep-map `ksp_solve` row** — upgrade the stale "theme `L3-L2/ksp-solve-outer-driver` **pending**" clause to a live link; the theme is firm on disk (`book/src/L3-L2/ksp-solve-outer-driver.md`, `## Status: firm`).
2. **Working Note "Two stubs queued"** — drop the now-firm `ksp_solve` bullet (it landed firm cycle-021 wave-1; verified on-disk `## Status: firm` at `book/src/L2/ksp_solve.md:151`). Retitle to **"One stub queued"** (`incremental-least-squares` is the sole remaining L2 stub) and add a sibling **"L2 driver/kernel pair now firm"** note recording the firm `ksp_solve` landing + its non-identity L2↔L1 rotation and live-linked L3>L2 theme.
3. **Working Note "L3 driver/kernel complementarity"** — drop the stale "`L3/ksp_solve.md` not yet on disk" / "Stays a plain-text forward-reference … pending that entry's authorship" clauses (the L3 `ksp_solve` entry is firm on disk since cycle-020) and upgrade the complementarity cross-reference to a **live link** to `../L3/ksp_solve.md`.

The two L2-intro-refresh meta-flags (`L2-layer-intro-refresh-for-named-compositions`, `L2-layer-intro-refresh-for-fold-cohort`) are **discharged by this refresh** (and were already discharged in prose by the cycle-018/019 Semantics-overlay + Vocabulary-cohort edits) — see §"Meta-flag discharge". Closing them in the OQ ledger is meta-phase authority; flagged below for the integrator to promote / meta-phase to close.

## On-disk firmness survey (batch-5 meta-phase guard — surveyed from each chapter's on-disk `## Status`, NOT the cycle record)

Verified by reading each file's `## Status` line / frontmatter `firmness:` directly:

| Chapter | On-disk Status | Line |
|---|---|---|
| `book/src/L2/ksp_solve.md` | `firm` (frontmatter `firmness: firm`; `## Status` `firm` cycle-021 wave-1) | 4, 151 |
| `book/src/L2/orthogonalize.md` | `firm` | 324 |
| `book/src/L2/inner_product.md` | `firm` | 406 |
| `book/src/L2/linear_combination.md` | `firm` | 271 |
| `book/src/L2/chebyshev-iteration.md` | `firm` (with ratified test-coverage caveat) | 214 |
| `book/src/L2/krylov-step.md` | `firm` | 125 |
| `book/src/L2/incremental-least-squares.md` | `stub` (banner `> **Status: \`stub\`**`) | 3 |

**Firm count = 6** (`ksp_solve`, `orthogonalize`, `inner_product`, `linear_combination`, `chebyshev-iteration`, `krylov-step`), matching the dispatch's expectation — confirmed against on-disk Status, not the log. The Vocabulary-cohort subsection (`book/src/L2/index.md` lines 30-41) and the dep-map already list all six as firm + the one stub; the only stale residue is in the dep-map `ksp_solve` row's "theme pending" clause and the two Working Notes (already-landed entries described as queued / off-disk). The Semantics overlay (`book/src/L2/index.md` lines 15-26) and Vocabulary cohort require **no** edit — they already reflect the firm cohort.

Adjacent-layer endpoints verified on-disk (for the live-link upgrades):
- `book/src/L3/ksp_solve.md` — exists; frontmatter `firmness: firm` (cycle-020). Relative path from L2: `../L3/ksp_solve.md` (resolves).
- `book/src/L3-L2/ksp-solve-outer-driver.md` — exists; `## Status: firm` (line 171). Relative path from L2: `../L3-L2/ksp-solve-outer-driver.md` (resolves).
- `book/src/L1/ksp_solve.md` — exists (the firm L1 collapse this L2 entry opens). Relative path: `../L1/ksp_solve.md` (resolves).

## Proposed changes

### Edit 1 — dep-map `ksp_solve` row: "theme … pending" → live link

```edit:book/src/L2/index.md
[old]: Establishes the **non-identity** L2↔L1 relationship (un-collapse of the L1 opacity) and the **non-identity** L3↔L2 relationship (L2 erases the iteration view, L3 un-erases it — theme `L3-L2/ksp-solve-outer-driver` pending).
[new]: Establishes the **non-identity** L2↔L1 relationship (un-collapse of the L1 opacity) and the **non-identity** L3↔L2 relationship (L2 erases the iteration view, L3 un-erases it — theme [`L3-L2/ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md), firm cycle-021).
```

### Edit 2 — Working Note: "Two stubs queued" → "One stub queued" + firm-pair note

```edit:book/src/L2/index.md
[old]: - **Two stubs queued for harvester refinement** (materialized 2026-05-28 under the implied-component stub policy):
  - [`incremental-least-squares.md`](./incremental-least-squares.md) — the GMRES outer driver's running-QR / Givens-stream small-dense kernel, currently a concept page (`concepts/incremental-least-squares`). The queued second **named-composition** (sibling to `orthogonalize`). Plan item `l2-named-composition-lifts`.
  - [`ksp_solve.md`](./ksp_solve.md) — the L2 **outer-driver** wrap above the firm L1 `ksp_solve`: the restart / convergence-test loop that wraps the `krylov-step` kernel into a complete solve. This is the substantive **non-identity** L2 coverage gap (distinct from the identity `L3>L2` `krylov-step-body-identity` theme). Plan item `ksp-solve-l2-promotion-non-identity-substantive-gap`.
[new]: - **One stub queued for harvester refinement** (the cohort's other 2026-05-28 stub, `ksp_solve.md`, landed firm cycle-021 — see the firm-pair note below):
  - [`incremental-least-squares.md`](./incremental-least-squares.md) — the GMRES outer driver's running-QR / Givens-stream small-dense kernel, currently a concept page (`concepts/incremental-least-squares`). The queued second **named-composition** (sibling to `orthogonalize`). Plan item `l2-named-composition-lifts`.
- **L2 outer-driver `ksp_solve` is now firm** (harvested cycle-021 wave-1; promoted from the 2026-05-28 stub). [`ksp_solve.md`](./ksp_solve.md) names the **outer-driver** wrap above the firm L1 [`ksp_solve`](../L1/ksp_solve.md): the restart / convergence-test `iterate_while` fold of the [`krylov-step`](./krylov-step.md) kernel into a complete solve. It establishes the substantive **non-identity** L2↔L1 rotation (the L1 solver-as-operator opacity is opened into the kernel-fold composition while the iteration view stays erased) — distinct from the identity [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) kernel theme. The landing closes the `ksp-solve-l2-promotion-non-identity-substantive-gap` plan item / OQ and resolves the maturity-gradient inversion (the firm cycle-020 [`L3/ksp_solve`](../L3/ksp_solve.md) was sitting above an L2 stub). The companion lowering is the firm L3>L2 theme [`ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md) (cycle-021).
```

### Edit 3 — Working Note "L3 driver/kernel complementarity": drop off-disk staleness, live-link the L3 entry

```edit:book/src/L2/index.md
[old]: - **L3 driver/kernel complementarity** (cycle-020 wave-1 harvester flag, cross-reference only — `L3/ksp_solve.md` not yet on disk): the L2 `ksp_solve` outer-driver wrap and the L3 `krylov-step` kernel form a driver/kernel pair across the L2↔L3 boundary mirroring the L2-kernel/L4-driver pair (`krylov-step` at L2, `iterate_while` at L4). When the L3 `ksp_solve` entry lands (wave-1 flagged an L3-index refresh need), this Working Note should grow a forward-reference to it. Stays a plain-text forward-reference here pending that entry's authorship.
[new]: - **L3 driver/kernel complementarity** (cycle-020 harvester flag; the L3 entry [`L3/ksp_solve`](../L3/ksp_solve.md) landed firm cycle-020): the L2 [`ksp_solve`](./ksp_solve.md) outer-driver wrap and the L3 [`krylov-step`](../L3/krylov-step.md) kernel form a driver/kernel pair across the L2↔L3 boundary, mirroring the L2-kernel / L4-driver pair (`krylov-step` at L2, `iterate_while` at L4). The L3 `ksp_solve` entry re-erases the iteration view that L2 erases — the non-identity hop captured by the firm L3>L2 theme [`ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md).
```

## Meta-flag discharge

Both L2-intro-refresh flags tracked in `scaffolding/open-questions.md` are **discharged by this refresh**; their substantive content was already absorbed into the index in cycles 018/019, and this dispatch confirms + completes the navigational residue:

- **`L2-layer-intro-refresh-for-named-compositions`** (OQ ledger `scaffolding/open-questions.md` lines 123, 22) — the original staleness ("cycle-005 firm-up did not introduce a new L2 entry for `orthogonalize` … remains a candidate") was already corrected by the cycle-019 `orthogonalize` firm-up (Working Note `book/src/L2/index.md` line 70 "**`orthogonalize` is now firm**", Vocabulary-cohort line 36, dep-map row line 51). No residual stale prose for the named-composition motif remains after this refresh. **Discharged** — recommend OQ-ledger close (meta-phase authority).
- **`L2-layer-intro-refresh-for-fold-cohort`** (OQ ledger `scaffolding/open-questions.md` line 149) — the overlay primitive list that "predates the fold cohort" was already rewritten in cycle-019: the Semantics overlay now carries the **Fold cohorts** motif paragraph (`book/src/L2/index.md` lines 22-26) naming both reduce-to-`Scalar` / reduce-to-`Tensor[N]` siblings with the do-NOT-merge boundary, the Vocabulary cohort lists both as firm (lines 34-35), and a Working Note carries the fold-cohort boundary (line 71). No residual stale prose for the fold cohort remains after this refresh. **Discharged** — recommend OQ-ledger close (meta-phase authority).

Per the write-authority partition, closing/migrating OQ-ledger entries is the meta-phase's unify authority (and `scaffolding/priorities.md` line 29's dispatched-item resolution is integrator/planner). This dispatch records the discharge; it does NOT itself edit `scaffolding/`.

## Supporting evidence

**Operators currently firm at L2 (6) — verified from on-disk `## Status`:**
- `krylov-step` (`book/src/L2/krylov-step.md:125` `firm`) — kernel half of the kernel-plus-driver shape.
- `chebyshev-iteration` (`:214` `firm`, ratified test-coverage caveat) — three-term recurrence behind `krylov-step` variant-axis 3.
- `linear_combination` (`:271` `firm`) — fold-cohort, reduce-to-`Tensor[N]`.
- `inner_product` (`:406` `firm`) — fold-cohort, reduce-to-`Scalar`; sibling fold (do-NOT-merge).
- `orthogonalize` (`:324` `firm`) — named-composition `project ▷ subtract`.
- `ksp_solve` (`:151` `firm`, cycle-021 wave-1) — named-composition outer-driver wrap; non-identity L2↔L1.

**Stub at L2 (1):** `incremental-least-squares` (`book/src/L2/incremental-least-squares.md:3` banner `stub`).

**Adjacent-layer cross-references (live-link targets, all resolve from `book/src/L2/`):**
- `../L3/ksp_solve.md` — firm cycle-020 (`book/src/L3/ksp_solve.md` frontmatter `firmness: firm`).
- `../L3-L2/ksp-solve-outer-driver.md` — firm cycle-021 (`## Status: firm`, `book/src/L3-L2/ksp-solve-outer-driver.md:171`).
- `../L3/krylov-step.md`, `../L1/ksp_solve.md` — existing firm entries (unchanged; referenced for the driver/kernel pair prose).

**L0 citations carried in the (largely-untouched) `ksp_solve` dep-map row — bounds + anchor verified, NOT modified by this refresh:**
- CG `Mult` body `palace/linalg/iterative.cpp:361-486` — anchor `CgSolver<OperType>::Mult` at 361 (verified via codemap `read_range`); `tools/citecheck` `[ok]` in-bounds (882-line file).
- GMRES `Mult` body `palace/linalg/iterative.cpp:544-705` — anchor `GmresSolver<OperType>::Mult` at 544 (verified); `[ok]`.
- `IterativeSolver` base `palace/linalg/iterative.hpp:25-115` — `[ok]` in-bounds (279-line file); wide range starts at the `template <typename OperType>` prefix (line 25), class declaration at 26 — correct wide-range start, not drift.
- driver wrap `palace/linalg/ksp.cpp:296-309` — anchor `BaseKspSolver<OperType>::Mult` at 296 (verified); `[ok]` in-bounds (315-line file).

## Open questions / caveats

- **OQ-ledger close is out of my write-scope.** This refresh discharges both L2-intro meta-flags in prose; the integrator should promote the discharge and the meta-phase should close `L2-layer-intro-refresh-for-named-compositions` + `L2-layer-intro-refresh-for-fold-cohort` (OQ `scaffolding/open-questions.md` lines 123, 149) and the parent `l2-index-working-note-staleness-l3-ksp-solve-on-disk` (`scaffolding/priorities.md` line 29, item 8). No `scaffolding/` edit is made here (write-authority partition).
- **gram / deflate rough-in rows left untouched as plain-text forward-refs.** Per the dispatch note, wave-2 will add their dep-map material; both rows (`book/src/L2/index.md` lines 54-55) are already present as plain-text rough-in rows (`gram` / `deflate`, no live anchors — correct per `rough-in-rows-must-be-plain-text-when-anchor-missing`). I did not live-link them and did not alter them — they describe not-yet-on-disk components. No `gram.md` / `deflate.md` exists under `book/src/L2/` (confirmed by the directory listing); leaving them plain-text is correct.
- **Index length unchanged in scale.** Edits 1–3 are in-place clause/bullet replacements (no new sections); `index.md` stays well under the ~200-line split threshold (currently 76 lines), so no promotion to `semantics.md` / `dep-map.md` is warranted.
- **No L0-citation mutation.** This is a navigational refresh: every edit touches intra-book links or Working-Note prose only. The four L0 citations in the `ksp_solve` row are carried verbatim (verified above for hygiene, not changed).
