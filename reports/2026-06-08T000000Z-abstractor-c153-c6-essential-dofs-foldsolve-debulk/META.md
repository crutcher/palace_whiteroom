---
verifies: ../CYCLE.md
critiqued_at: 2026-06-08T000000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-08T000000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of Cycle-153 C6 — essential-dofs + fold-solve de-bulk

## Critique

This is a finalization-debulk report (E-class date strip + a c152 residual dangling-pointer
fix) — two surgical prose-only edits across two firm lowering themes. The de-bulk-shaped report
no-ops the producer-evidence checks (no new claim/surface/rotation introduced); the load-bearing
checks are conservation (citations preserved, rank/status untouched, lint baseline held) and
cross-reference-integrity (the §-pointer rephrase correctness). All conservation claims independently
verified; one cross-reference observation surfaced (below).

### Checks run

- **citation-validity** — `pass`. Both files' citation multisets are IDENTICAL HEAD→working-tree
  (`diff` of `grep -oE '…\.(cpp|hpp|h|c|cc):lines'` sorted → empty for both). Confirmed: essential-dofs
  `multigrid.hpp`/`geodata.hpp`/`spaceoperator.cpp` ranges intact; fold-solve `timeoperator.cpp:312,410`,
  `transientsolver.cpp:33-99`, `drivensolver.cpp:231-389` ranges intact. The two edits touch ONLY
  non-citation prose (a directive-date phrase; a bare `§`-pointer clause). No claim lost.

- **surface-or-evidence** — `pass` (de-bulk shape, no-op). Neither edit modifies an algebraic surface
  or introduces a rotation_claim; both are pure process-accounting removal (the directive-date
  provenance; the dead `§Working-Notes` pointer) with the static fact retained verbatim. No record is
  named-in-signature here without a home (no record-definition obligation triggered). The
  finalization-debulk strip-keep discipline (drop process/date provenance, keep the static fact) is
  the governing rule and is satisfied: essential-dofs keeps the identity-in-named-terms-smell fact and
  "the dof set is a value over the space" clause; fold-solve keeps the erasure-scope-taxonomy
  classification fact, dropping only the dead pointer text.

- **rotation-quality** — `pass` (not applicable to de-bulk report). No rotation asserted or altered;
  the two firm themes' rotations are unchanged by prose-only edits.

- **variant-axis-coverage** — `pass` (not applicable to de-bulk report). No variant axes in scope.

- **cross-reference-integrity** — `warning`. The fold-solve rephrase (`§Working-Notes` →
  `§"Erasure-scope taxonomy"`) achieves its stated goal: line 15 now uses the SAME string as the three
  pre-existing references at lines 74/111/130 (verified those three already read `§"Erasure-scope
  taxonomy"` at HEAD — internal consistency restored, dead `§Working-Notes` token eliminated, build
  unaffected). HOWEVER the target it now points at — `L3-L2/index.md §"Erasure-scope taxonomy"` —
  is **not a literal heading** in `L3-L2/index.md`: that file's only headings are `## Context`,
  `## Theme list`, `## Vocabulary cohort`; the phrase "erasure-scope" appears there only as inline
  prose inside the theme-list table rows (lines 28/29) and one list bullet (line 53). This is a
  **bare prose `§`-pointer, not a live markdown link** (`L3-L2/index.md` is backtick-text, not
  `[…](…)`), so it is NOT a `linkcheck2`/build error and the lint baseline is unaffected. It is also
  a **pre-existing latent condition** the three sibling refs already carried at HEAD — the edit did
  not introduce it, it merely made the fourth ref consistent with the (already-imprecise) siblings,
  which is squarely within this report's narrow de-bulk scope. Hence `warning`, not `fail`: the edit
  is correct and consistent as scoped, but the navigational target heading literally does not exist —
  worth surfacing for a follow-up (either add a `## Erasure-scope taxonomy` heading to
  `L3-L2/index.md`, or re-point all four prose refs to a real anchor such as `§"Theme list"`). The
  report's framing "aligns with the three already-live refs" is accurate as to consistency, but
  slightly overstates "live": the siblings were already pointing at a non-existent heading.

- **edge-label-fidelity** — `pass`. No edge label changed. The fold-solve theme's L3>L2 framing and
  the essential-dofs L1>L0 framing are untouched by the edits; prose discusses the correct edges
  throughout (verified by the diff: only the date phrase and the pointer clause changed).

- **plan-kind-consistency** — `pass`. The report is a de-bulk/finalization pass and its content shape
  matches: surgical prose removals, conservation tables, exact-lint-hold assertion. No rough-in
  placeholder masquerading as firm; both themes retain their firm rank/status (verified below).

- **skill-uptake-survey** — `pass`. The report explicitly invokes the `finalization-debulk` skill
  (E-class date rule + strip/keep discipline) and cites the c152 pilot pattern + the
  `book/src/L4/krylov_step.md` exemplar. Skill uptake surfaced.

### Conservation verification (independently reproduced)

- **No citation lost** — CONFIRMED. Citation multiset `diff` HEAD↔working-tree is empty for BOTH files.
- **Only date/pointer fixed, fact kept** — CONFIRMED. `git diff HEAD` shows exactly two single-clause
  hunks: (1) essential-dofs line 103, `the 2026-06-01 vocabulary-shift redirect` → `the vocabulary-shift
  discipline` (the "dof set is a value over the space, not an L1 op re-mirroring MFEM internals" fact
  KEPT verbatim); (2) fold-solve line 15, `(the erasure-scope taxonomy, \`…\` §Working-Notes)` →
  `(\`…\` §"Erasure-scope taxonomy")` (the carry-threaded-sibling classification fact KEPT). No
  structural content lost.
- **§"Erasure-scope taxonomy" rephrase correctness** — CONFIRMED CONSISTENT, with the caveat above:
  the new string MATCHES the 3 pre-existing sibling refs at lines 74/111/130 (all four now read
  `§"Erasure-scope taxonomy"`); but that section is not a literal heading in `L3-L2/index.md` (the
  `warning` in cross-reference-integrity). The dead `§Working-Notes` token is fully eliminated.
- **No rank/status move** — CONFIRMED. essential-dofs frontmatter `rank: firm` identical HEAD↔WT;
  fold-solve `## Status` block at line 156 with leading `firm` sole-rank-carrier token byte-identical
  HEAD↔WT (de-bulk did not strip the rank-carrier — correct per the finalization invariant).
- **Graded-stack baseline HELD EXACTLY** — CONFIRMED. Re-ran `graded_stack_lint.py`:
  `files=392, typed=331, untyped=61, rank_violations=0, unresolved_depends_on_targets=0,
  promotion_frontier=11, detritus=123, true_detritus=51`. All eight figures match.
- **0 dates + 0 dangling `§Working-Notes`** — CONFIRMED. `grep -cE '2026-[0-9]'` on essential-dofs → 0;
  `grep -cE 'Working[- ]Notes|§Working'` on fold-solve → 0.

### Issues found

1. **(cross-reference-integrity, warning) Navigational `§`-pointer target heading does not exist** —
   `book/src/L3-L2/fold-solve-time-step-body.md:15` (and the pre-existing siblings at :74, :111, :130)
   point to `L3-L2/index.md §"Erasure-scope taxonomy"`, but `L3-L2/index.md` has no such heading
   (headings are `## Context` / `## Theme list` / `## Vocabulary cohort`; "erasure-scope" is inline
   table/bullet prose only). NOT introduced by this report (the 3 siblings carried it at HEAD), NOT a
   build error (bare prose pointer, not a live link), and OUTSIDE this report's narrow scope (which was
   only to make line 15 consistent — done correctly). Surfaced for a follow-up: add a real
   `## Erasure-scope taxonomy` heading to `L3-L2/index.md`, or re-point the four prose refs to an
   existing anchor. Severity: low (navigational precision, no build/graph impact).

---

## Repair

### Fixes attempted

- **Finding** (cross-reference-integrity, warning): the four bare prose `§`-pointers in
  `book/src/L3-L2/fold-solve-time-step-body.md:15,74,111,130` name `L3-L2/index.md §"Erasure-scope
  taxonomy"`, but `L3-L2/index.md` had no such heading (its headings were `## Context` / `## Theme
  list` / `## Vocabulary cohort`; the erasure-scope taxonomy content lives as inline prose inside
  `## Vocabulary cohort`). C6 made line 15 consistent with the 3 already-imprecise siblings rather than
  introducing the condition.
  - **Decision**: repaired.
  - **Action** (heading-add, the PREFERRED fix): added a real `### Erasure-scope taxonomy` sub-heading
    under `## Vocabulary cohort` in `book/src/L3-L2/index.md:49`, immediately before the italic
    intro line "*Substantive / non-identity iteration-rotation themes …*". The block at lines 49–57
    (the italic intro + the five substantive-theme bullets `ksp-solve-outer-driver` /
    `orthogonalize-variant-split` / `eigsolve-opaque-eigen-iteration` / `fold-solve-time-step-body` /
    `chebyshev-nested-recurrence` + the closing "the substantive-erasure axis spans five roots"
    summary) is a coherent, self-contained taxonomy of the erasure-scope axis that genuinely warrants
    a heading, so the heading-add (which fixes all four prose refs at once) is apter than re-pointing.
    Heading-only edit; no node/edge/rank/status/semantics move; the `## Status` `firm` sole-rank-carrier
    in `fold-solve-time-step-body.md:156` and all citations untouched.

### Verification

- **Heading now exists**: `grep -nE '^#{2,3} Erasure-scope taxonomy' book/src/L3-L2/index.md` →
  `49:### Erasure-scope taxonomy`.
- **All 4 prose refs now name a real heading**: `fold-solve-time-step-body.md:15,74,111,130` all read
  `§"Erasure-scope taxonomy"`, which now resolves to a literal heading.
- **0 dangling `§Working-Notes`**: `grep -cE 'Working[- ]Notes|§Working' fold-solve-time-step-body.md`
  → 0.
- **Graded-stack lint baseline HELD EXACTLY**: `files=392, typed=331, untyped=61, rank_violations=0,
  unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123, true_detritus=51` — all eight
  figures match.
- **`cargo make book` builds**: EXIT=0, "Build Done". No new broken-link / linkcheck error (the
  pointers were bare prose, not markdown links; the heading-add introduces no link). The residual
  "Potential incomplete link" / "unclosed HTML tag" warnings are pre-existing and concern
  KaTeX-rendered bracket text + `L0/` / `meta-reviews/` files this repair did not touch.

### Unrepairable findings

None. The lone warning was a trivial heading-add within repair authority (prose/heading editing only,
all citations + the `firm` sole-rank-carrier preserved).

## Suggested resolution

`ready`. The cross-reference-integrity warning is fully repaired: the navigational `§`-pointer target
now exists as a real `### Erasure-scope taxonomy` heading in `L3-L2/index.md`, accurate for all four
prose refs at once. All conservation invariants the critic verified remain intact (citations, ranks,
statuses, lint baseline). Note for the integrator: the heading-add to `book/src/L3-L2/index.md` is a
repairer artifact-touch outside the report's CYCLE.md proposed-changes; it is a pure prose/heading
edit (no graph/rank/status change, lint baseline held exactly) made to discharge the warning at its
true source rather than re-pointing the four refs.
