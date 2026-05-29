---
agent: lifter
invoked_at: 2026-05-29T19:50:00Z
scope: cycle-028 mechanical citation-hygiene residual sweep — three carried-forward hygiene residuals (workspace-category mislabel residual lines :22/:87; incremental-least-squares stale self-description; gram forthcoming-text refresh)
status: integrated
integrated_at: 2026-05-29T205500Z
integration_commit: 3319d88
integration_notes: "cycle-028 position 2/7 (per-report). Pure mechanical citation-hygiene residual sweep. (a) L0/linalg-operator-file.md :22/:87 Category-2→Category-1 workspace relabel (now all five workspace-category mentions uniform; grounded in mutable-workspace-pattern.md:128-129); (b) L2/incremental-least-squares.md:13 dropped stale 'queued' self-description (firm since c026); (c) gram refresh verified no-op (already closed c026). No operator/theme signature/decomposition/semantics/law touched. Build clean (zero build-repairs)."
inputs:
  - book/src/L0/linalg-operator-file.md
  - book/src/L0/mutable-workspace-pattern.md
  - book/src/L2/incremental-least-squares.md
  - book/src/L2/gram.md
  - reports/2026-05-29T175529Z-lifter-cycle026-hygiene-reanchors/CYCLE.md
---

# CYCLE: citation-hygiene residual sweep (three carried-forward residuals)

## Summary
Three mechanical citation-hygiene residuals carried forward from cycle-027, all pure re-anchor / text-refresh — no content, structure, signature, decomposition, or law change. **(a)** `book/src/L0/linalg-operator-file.md` lines `:22` and `:87` still carry the "Category 2" workspace mislabel that cycle-027 D2 fixed at the named sites `:33`/`:73`/`:80` (plus the `matrix-weighted-norm.md:9` sibling) but explicitly left out of scope, opening OQ `linalg-operator-file-category-mislabel-residual-lines-22-87`; both are relabelled to **Category 1** per the convention page's own Evidence section (`mutable-workspace-pattern.md:128-129`), completing the file's internal consistency. **(b)** `book/src/L2/incremental-least-squares.md:13` self-describes as "the **queued** second named-composition motif" despite the entry being `status: firm` since cycle-026 (line 378); the stale "queued" qualifier is dropped. **(c)** `book/src/L2/gram.md` — the "(forthcoming)" residual is **already closed** (zero "forthcoming" hits on disk; all three `gram-fold-specialization` references read `(firm)`); no edit needed.

## Proposed changes

### Residual (a) — Category-2 workspace mislabel residual at `linalg-operator-file.md:22`, `:87`

This is the identical evidence-driven, bounded Category→Category-1 relabel the cycle-027 D2 pass (`reports/2026-05-29T175529Z-lifter-cycle026-hygiene-reanchors/CYCLE.md`) applied to `:33`/`:73`/`:80`, now extended to the two residual sites it named but held out of scope (that report's §Open questions / caveats lines 127-130 + §OQ disposition line 136). The convention page's **Evidence (representative)** section is authoritative on the category of each named workspace, and says both are **Category 1** (not Category 2):

- `book/src/L0/mutable-workspace-pattern.md:128` — "`palace/linalg/operator.hpp:120` — `SumOperator::z` (**Category 1**: sum-of-operators workspace)."
- `book/src/L0/mutable-workspace-pattern.md:129` — "`palace/linalg/operator.hpp:192` — `BaseProductOperator::z` (**Category 1**: operator-composition workspace)."
- `book/src/L0/mutable-workspace-pattern.md:29` — "## Category 1 — operator-composition workspaces" (the section heading).

After this relabel, all five workspace-category mentions in `linalg-operator-file.md` (`:22`, `:33`, `:73`, `:80`, `:87`) read "Category 1", matching the convention page. The `:87` site additionally was wrong on label-phrasing ("composition-class workspaces" — the page's term is "operator-composition workspaces"), mirroring the count/phrasing error the c027 repairer corrected at the parallel `:80` site (its old "Categories 2 and 4").

`:22` — `SumOperator`'s `mutable Vector z` (line 120) is Category 1 per Evidence `:128`:

```edit:book/src/L0/linalg-operator-file.md
[old]: - **`SumOperator` (real-only)** (`palace/linalg/operator.hpp:116-136`) — wraps a sequence of `Operator` references with optional `double` coefficients, exposing the weighted-sum action as a single `Operator`. Holds `std::vector<std::pair<const Operator *, double>> ops` (line 119) and a `mutable Vector z` workspace (line 120; Category 2 of [`mutable-workspace-pattern`](./mutable-workspace-pattern.md)). Method bodies in `operator.cpp:421-475`.
[new]: - **`SumOperator` (real-only)** (`palace/linalg/operator.hpp:116-136`) — wraps a sequence of `Operator` references with optional `double` coefficients, exposing the weighted-sum action as a single `Operator`. Holds `std::vector<std::pair<const Operator *, double>> ops` (line 119) and a `mutable Vector z` workspace (line 120; Category 1 — operator-composition workspace — of [`mutable-workspace-pattern`](./mutable-workspace-pattern.md)). Method bodies in `operator.cpp:421-475`.
```

`:87` — the "Referenced from" bullet; both `SumOperator::z` and `BaseProductOperator::z` are Category 1 per Evidence `:128-129`:

```edit:book/src/L0/linalg-operator-file.md
[old]: - [`L0/mutable-workspace-pattern`](./mutable-workspace-pattern.md) — Category 2 (composition-class workspaces) cites `SumOperator::z` and `BaseProductOperator::z`.
[new]: - [`L0/mutable-workspace-pattern`](./mutable-workspace-pattern.md) — Category 1 (operator-composition workspaces) cites `SumOperator::z` and `BaseProductOperator::z`.
```

### Residual (b) — `incremental-least-squares.md:13` stale "queued" self-description

The entry is `status: firm` (`book/src/L2/incremental-least-squares.md:378` — "`firm` — the composition is a `replay ▷ generate ▷ apply ▷ apply_rhs` pipeline…"), firmed cycle-026 (`reports/2026-05-29T163011Z-harvester-incremental-least-squares-l2/`). The opening-paragraph self-description at `:13` still says "the **queued** second named-composition motif", a staleness from when the entry was a rough-in / queued candidate. Drop the "queued" qualifier; the rest of the sentence (the named-composition role, the `orthogonalize` sibling cross-reference, the GMRES/FGMRES fold) is correct and unchanged.

```edit:book/src/L2/incremental-least-squares.md
[old]: externally-visible iterate correction is `V·y` (GMRES) / `Z·y` (FGMRES). This is
the queued second **named-composition** motif (sibling to
[`orthogonalize`](./orthogonalize.md)), the composition GMRES / FGMRES fold into
[new]: externally-visible iterate correction is `V·y` (GMRES) / `Z·y` (FGMRES). This is
the second **named-composition** motif (sibling to
[`orthogonalize`](./orthogonalize.md)), the composition GMRES / FGMRES fold into
```

### Residual (c) — `gram.md` "(forthcoming)" refresh — ALREADY CLOSED, no edit

Checked per the dispatch's conditional ("IF still present"). `grep -n -i 'forthcoming' book/src/L2/gram.md` returns zero hits. All three references to the L2>L1 lowering theme already read `(firm)`:
- `:38` — "narrated forward from L2 to L1 in [`L2-L1/gram-fold-specialization`](…) (firm) — not authored here."
- `:176` — "recorded by the L2>L1 lowering theme [`gram-fold-specialization`](…) (firm)."
- `:242` — "**L2>L1 lowering theme** [`gram-fold-specialization`](…) (firm): …"

The `gram-fold-specialization` theme firmed (cycle-024/025) and the `gram` entry (firm since cycle-021 per its §Status / provenance) was already refreshed to match. No proposed change.

## Discipline notes
- **Pure re-anchor / text-refresh** per role-spec — no operator signature, decomposition, semantics, or algebraic law changed in any of the three residuals. (a) is a category-label relabel against the L0 convention page's own Evidence taxonomy; (b) is a single-word staleness drop reflecting a status already recorded elsewhere in the same file; (c) is a no-op (already closed).
- **(a) is a bounded, L0-evidence-driven prose correction recorded here** per the `lifter-scope-content-correction-boundary` discipline (CLAUDE.md §Methodology + the role-spec in-scope clause): the correction is directly supported by `book/src/L0/mutable-workspace-pattern.md:128-129` (the convention page's own Evidence section labels both `SumOperator::z` and `BaseProductOperator::z` Category 1), it is **bounded** (a wrong category label, not a re-architecting of the workspace taxonomy or the operator decomposition), and it is recorded explicitly here with the supporting citation. It is the exact same relabel cycle-027 D2 applied to the four named sites; this dispatch only closes the two it left out of scope. No abstractor reread is needed — the firmed-up vocabulary does not contradict the file's structure.
- **(b)** drops a stale self-description word; the entry's `status: firm` line (`:378`) and the rest of the body already reflect firm status, so this is a self-consistency refresh, not a status flip (the flip itself happened in cycle-026). No `rough-in`→`firm` body-relocation is involved — the §Status section is already `firm` and stays untouched.
- **Citation self-verification**: these are `book/` prose-file line numbers, not Palace source ranges, so `citecheck --anchor` (a Palace-source line linter) does not apply. Each target line was confirmed against on-disk via direct read before emitting the `[old]` strings (the `[old]` strings are verbatim copies of the on-disk lines at `:22`/`:87`/`:13`). The category-label evidence (`mutable-workspace-pattern.md:128-129`, `:29`, `:82`) was read on-disk this dispatch.
- **No `book/` writes performed** — all three residuals are emitted as proposed-changes blocks for `integrator-per-report` (dispatch-phase write-guard; friction-ledger `specialized-agent-direct-write-to-book-during-dispatch`). (c) carries no block (already closed).

## Supporting evidence
- `book/src/L0/mutable-workspace-pattern.md:29` — "## Category 1 — operator-composition workspaces" (section heading); `:82` — "## Category 4 — assembled-matrix retention" (the distinct category the c027 named sites were originally mislabelled as); `:128` — `SumOperator::z` is **Category 1**; `:129` — `BaseProductOperator::z` is **Category 1**. The authoritative taxonomy the `:22`/`:87` relabel rests on.
- `reports/2026-05-29T175529Z-lifter-cycle026-hygiene-reanchors/CYCLE.md` — the cycle-027 D2 pass: §Correction 2 + §Correction-2-residual relabel `:33`/`:73`/`:80` Category-4→Category-1 (same convention); §Open questions / caveats (lines 127-130) + §OQ disposition (line 136) name `:22` and `:87` as the out-of-scope residuals this dispatch closes, and open the OQ `linalg-operator-file-category-mislabel-residual-lines-22-87`.
- `book/src/L2/incremental-least-squares.md:378` — `status: firm` (firmed cycle-026); the basis for dropping the stale "queued" self-description at `:13`.
- `reports/2026-05-29T163011Z-harvester-incremental-least-squares-l2/CYCLE.md` — the cycle-026 firming pass for `incremental-least-squares`.
- `book/src/L2/gram.md:38,176,242` — all three `gram-fold-specialization` references read `(firm)`; zero "forthcoming" on disk → residual (c) already closed.

## Open questions / caveats
- **OQ `linalg-operator-file-category-mislabel-residual-lines-22-87` is resolved by residual (a)** — close on integration. With `:22` and `:87` relabelled, all five workspace-category mentions in `linalg-operator-file.md` (`:22`/`:33`/`:73`/`:80`/`:87`) are uniformly "Category 1", matching the convention page; the file is fully internally consistent and no further residual sites remain (the dispatch named these two as the last, and a fresh read of the file confirms no other "Category 2"/"Category 4" workspace-label mentions).
- **OQ `l2-incremental-least-squares-self-description-still-says-queued-after-firming` is resolved by residual (b)** — close on integration.
- **OQ on `gram.md` "(forthcoming)" residual is already closed** — no edit was needed. The gram forthcoming-refresh OQ (`gram-md-forward-ref-text-refresh-to-name-gram-fold-specialization`, `scaffolding/open-questions.md:344`) was already marked **resolved cycle-026** (the "(forthcoming)" prose upgraded to a live `gram-fold-specialization` link by the c026 D7 lifter); there is no still-open gram OQ for the integrator to close (the entry and all theme references read `(firm)` on disk).
- No contradictions surfaced between the firmed-up vocabulary and the touched entries' structure — all three residuals are within pure re-anchor / text-refresh scope; no abstractor reread is needed.
