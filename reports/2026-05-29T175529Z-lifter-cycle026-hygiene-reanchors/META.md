---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T18:11:19Z
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
repaired_at: 2026-05-29T18:24:40Z
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

# META: verification of cycle-026 hygiene re-anchors (four bounded cite/name corrections)

## Critique

### Checks run

**citation-validity (LOAD-BEARING) — pass.** All four corrections verified mechanically against on-disk `reference/palace/` with `tools/citecheck/citecheck.py`, plus the convention page's own taxonomy. Detail per correction:

- *Correction 1 (brace-boundary drift `:601-606` → `:602-606`):* `citecheck palace/linalg/operator.cpp:601-607 --show` confirms line `:601` is the opening brace `{`; the body `B.Mult(x, Bx); double dot = Dot(comm, Bx, x); MFEM_ASSERT(...); return std::sqrt(dot);` is exactly `:602-606`. `--anchor 'B.Mult(x, Bx)'` resolves to line 602 within `:602-606`. The corrected range is on-disk-true. Both prose sites (`:58`, `:83`) quote the *body* ("the implementation factors as `B.Mult...; return std::sqrt(dot)`"), so the body-only `:602-606` is the right range; the full-spec `:599-607` is correctly reserved for site `:128` (left untouched, as the dispatch specifies). The report's `--anchor`-confirmed correction settles this mechanically — this is precisely the off-by-one-on-the-brace case the friction-ledger warns against hand-asserting, and the producer used the tool correctly.
- *Correction 2 (Category-4 → Category-1 relabel):* I read `book/src/L0/mutable-workspace-pattern.md` directly. Category 1 (`:29`) = "operator-composition workspaces" (holds a chained-apply intermediate; canonical shape `B.Mult(x, z); A.Mult(z, y)`). Category 4 (`:82`) = "assembled-matrix retention" (`MfemWrapperSolver`'s retained `HypreParMatrix`). `citecheck operator.cpp:621-639 --show` confirms the `Dot(comm, x, A, y)` overloads internally allocate `ComplexVector Ax(A.Height())` then do `A.Mult(x, Ax); Dot(comm, Ax, y)` — an apply-then-reduce holding the `A·x` intermediate, which is structurally the Category-1 operator-composition shape, NOT assembled-matrix retention. The relabel direction is correct and L0-evidence-driven. The new prose's added clause "holding the `A·x` intermediate between the apply and the reduction" matches the source body verbatim.
- *Correction 3 (givens stream `gmres.md` → `iterative.cpp:634-640`):* `book/src/L1/gmres.md` does not exist on disk (confirmed `ls`), so the old pointer was dangling. `citecheck iterative.cpp:634-640 --show` confirms the sub-range pinpoints map EXACTLY to the prose: replay loop `for (int k=0; k<j; k++) { ApplyPlaneRotation(...) }` at `:634-637`; `GeneratePlaneRotation` at `:638`; annihilate-`h[j+1]` `ApplyPlaneRotation(Hj[j], Hj[j+1], ...)` at `:639`; RHS-pair `ApplyPlaneRotation(s[j], s[j+1], ...)` at `:640`. The per-kernel cross-references already on the page (`iterative.cpp:73-108` GeneratePlaneRotation, `:227-241` ApplyPlaneRotation) re-verified `--anchor`-OK and are unaffected by the edit.
- *Correction 4 (`dot_bilinear` provenance-note refresh):* premise genuinely stale. `grep` confirms `linalg-operator-file.md:73` now links `../L1/bilinear-form.md` (no surviving `dot_bilinear` slug in `linalg-operator-file.md` or elsewhere in `book/src/` save the stale note itself). The false "L0 chapter uses the candidate slug `dot_bilinear` / slug discrepancy persists" clause is correctly dropped; the Evidence bullet's L0-anchor provenance is preserved.

`citecheck --scan CYCLE.md --quiet` returns **22 ok, 1 failing**, and the single failure is exactly the expected `[AMBIG] operator.cpp:621-639` (bare basename matches two files). This is INSIDE the `[old]`/`[new]` edit payload that must match `linalg-operator-file.md:33` verbatim, where the L0 chapter uses the bare basename `operator.cpp` by convention (confirmed `grep` of `:33`). Preserving the bare basename verbatim is the correct decision — fully-qualifying the path inside the edit would make the `[old]` string fail to match on disk. This is a correct preserve-verbatim, NOT a citation defect.

**surface-or-evidence — pass (no-op).** No semantic / operator-surface change. Corrections 1 and 3 are line-number / source-pointer re-anchors; Correction 2 is a category-label relabel against the L0 convention page's own taxonomy; Correction 4 is a provenance-note premise refresh. No rotation_claim is asserted, no operator/theme semantics is modified. The check no-ops on a pure cite/name-hygiene pass.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted or modified. No-op for this report shape.

**variant-axis-coverage — pass (not applicable).** No operator variant axes are touched; the four corrections are surgical text edits. No hidden branches.

**cross-reference-integrity — warning.** All `[link]` references in the edited payloads resolve (`../L0/mutable-workspace-pattern.md`, `./mutable-workspace-pattern.md`, `../L1/bilinear-form.md` all exist; the `gmres.md` dangling pointer is being REMOVED by Correction 3, which improves integrity). The warning is for the **incomplete-sweep residual** the report itself partly flagged (see Issues): the Category-4 mislabel survives at MORE sites in `linalg-operator-file.md` than the report's edits + flag cover. No firm-status / fence-truncation concern applies (no `firm` claim; no body-outside-fence pattern — this is a four-edit surgical pass).

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; these are L0/L1/concept in-place corrections.

**plan-kind-consistency — pass.** Declared kind is a "pure re-anchoring / cite-refresh" hygiene pass; content shape (6 surgical `[old]`/`[new]` edits across 4 files, no new operator/theme, no status change) matches. The OQ-disposition section correctly classifies the `bilinear-form-workspace-category-4-mislabel` OQ as **partially-resolved** (not closed) given the residual — consistent with the content actually delivered.

**skill-uptake-survey — pass.** The report references `verify-citation-range` and the mechanical `tools/citecheck/citecheck.py --show`/`--anchor` realization (the cycle-024 friction-ledger `producer-citation-drift-verify-not-self-invoked` path) and invokes it on every range. Appropriate skill uptake for a cite-refresh pass; pure telemetry, non-blocking.

### Issues found

1. **[MEDIUM — incomplete sweep] Category-4 mislabel survives at a SECOND unflagged site `book/src/L0/linalg-operator-file.md:80`.** The report (Open questions / caveats, CYCLE.md:105) flags ONE residual at `:73`. But the same file carries the mislabel at **two** un-fixed sites, not one:
   - `:73` — "The workspace-internal-allocation pattern (`Dot`'s synthetic workspace) is Category 4 of [`mutable-workspace-pattern`]." — *flagged by the report, not fixed.*
   - `:80` — "[`mutable-workspace-pattern`] — `SumOperator::z`, `BaseProductOperator::z`, and the free-function `Dot`'s synthetic workspace are **Categories 2 and 4**." — *NOT flagged and NOT fixed.*

   `:80` is in fact a *doubly*-wrong line: the convention page's own Evidence section (`mutable-workspace-pattern.md:128-129`) assigns `SumOperator::z` (operator.hpp:120) and `BaseProductOperator::z` (operator.hpp:192) to **Category 1**, and the report's own Correction 2 establishes `Dot`'s workspace is **Category 1** — so all three named workspaces are Category 1, and "Categories 2 and 4" names neither the right categories nor the right count. Leaving the file with `:33` corrected to Category 1 while `:73` and `:80` still say "Category 4" / "Categories 2 and 4" is exactly the internal-inconsistency the report worried about for `:73`, compounded. **Recommend for the repairer:** if the relabel is in-scope to extend (it is the same evidence-driven L0-convention correction, mechanical and surgical), fix BOTH `:73` and `:80` this cycle so the file is internally consistent. Severity MEDIUM because the file is left actively self-contradictory on the workspace taxonomy. (The report's narrower-residual OQ candidate `linalg-operator-file-line-73-category-4-mislabel-residual` should be widened to name `:80` as well.)

2. **[LOW — pre-existing, surrounding-bullet, out-of-payload] Stale section-name cross-reference in the Correction-4 bullet's untouched tail (`bilinear-form.md:412-414`).** The evidence bullet being refreshed says "`book/src/L0/linalg-operator-file.md` §"linalg:: free functions" (lines 30-35) and §**"Why this file pair matters"** (line 73)". The L0 file has NO section titled "Why this file pair matters" (its headers are: File structure / What's not here / Test coverage / Notes for higher layers / Dependencies / Referenced from / Evidence) — line 73 actually lives under "## Notes for higher layers". This is a PRE-EXISTING inaccuracy in the part of the bullet OUTSIDE the report's `[old]`/`[new]` payload, so it is not introduced by this report; but it sits in the very bullet Correction 4 is refreshing. Flagging for repairer awareness — optionally fold a one-token section-name fix into Correction 4's `[new]` while that bullet is being touched (low severity; does not block).

3. **[INFO — verbatim/single-occurrence confirmation, no defect]** All six `[old]` strings confirmed verbatim single-occurrence on disk via `grep -c` (Correction 1a `:58` → 1; Correction 1b `:83` → 1; Correction 2a `matrix-weighted-norm.md` → 1; Correction 2b `linalg-operator-file.md` → 1; Correction 3 `givens.md` → 1; Correction 4 `bilinear-form.md` → 1). The two `operator.cpp:601-606` occurrences in `matrix-weighted-norm.md` are exactly the two targeted sites — confirming the third occurrence (`:128`, cited as `:599-607`) is correctly left untouched. The `[AMBIG] operator.cpp:621-639` in `--scan` is the expected, correct preserve-verbatim (matches `linalg-operator-file.md:33`'s bare-basename convention) — not a defect. No further edit-applicability concerns.

## Repair

### Fixes attempted

- **Finding** (cross-reference-integrity warning, Issue 1): the Category-4 workspace mislabel persists at two MORE sites in `book/src/L0/linalg-operator-file.md` than the report's Correction 2 fixes — `:73` ("`Dot`'s synthetic workspace) is Category 4", flagged-but-not-fixed by the report) and `:80` ("`SumOperator::z`, `BaseProductOperator::z`, and the free-function `Dot`'s synthetic workspace are Categories 2 and 4", UNFLAGGED). With `:33` relabelled to Category 1 but `:73`/`:80` left wrong, the file is internally self-contradictory on the workspace taxonomy.
  - **Decision**: **repaired**.
  - **Action**: appended two surgical `[old]`/`[new]` proposed-changes blocks to `CYCLE.md` §"Correction 2-residual (repairer)" targeting `book/src/L0/linalg-operator-file.md:73` and `:80`. Both relabelled to **Category 1 — operator-composition workspace**. Authority basis: the convention page's own **Evidence (representative)** section is dispositive — `mutable-workspace-pattern.md:128` assigns `SumOperator::z` (`operator.hpp:120`) to Category 1, `:129` assigns `BaseProductOperator::z` (`operator.hpp:192`) to Category 1, and the report's own Correction 2 (evidence-driven from the `A.Mult(x, Ax); Dot(Ax, y)` apply-then-reduce body) places `Dot`'s workspace at Category 1. So `:73`'s "Category 4" is a single-token category fix, and `:80`'s "Categories 2 and 4" is doubly wrong (wrong categories AND wrong count — three workspaces, all one category) → rewritten to "all Category 1 (operator-composition workspaces)". This is a mechanical label correction against the convention page's own authoritative taxonomy (no content authored), so it is in repair scope (the same shape as the report's already-accepted Correction 2). Both `[old]` strings confirmed verbatim single-occurrence on disk (`grep -Fc` → 1 each). Also widened the report's residual OQ (`Open questions / caveats` + `OQ disposition`) to record `:80` as resolved alongside `:73`, and to name the two NEWLY-DISCOVERED out-of-scope residual sites (`:22`, `:87`) for a follow-up.

### Unrepairable findings

None. The single warning finding was mechanically repairable (label correction against the convention page's own Evidence taxonomy, surgical `[old]`/`[new]` edits, verbatim single-occurrence on disk).

**Out-of-scope residual deliberately NOT widened into** (recorded, not repaired): the same Category-mislabel survives at `linalg-operator-file.md:22` (`SumOperator`'s `mutable Vector z` → labelled "Category 2", Evidence says Category 1) and `:87` ("Referenced from" → "Category 2 (composition-class workspaces)", Evidence says Category 1). These were NOT in the dispatch's named site list (`:33`/`:73`/`:80`) nor in the critic's named sites; widening into them would be the same incomplete-sweep pattern in reverse and exceeds the surgical authority handed for this repair. Flagged in the report's OQ (`linalg-operator-file-category-mislabel-residual`, now naming `:22`/`:87`) for a follow-up lifter/integrator pass — NOT a blocker on this report (the four dispatched/critic-named sites are now all consistent at Category 1).

(Issue 2 — the pre-existing stale section-name "Why this file pair matters" in the Correction-4 surrounding bullet — is LOW, out-of-payload, and explicitly non-blocking per the critic; left untouched as it is outside this report's `[old]`/`[new]` payloads and outside the cross-reference-integrity repair the dispatch handed me. Issue 3 is INFO/no-defect.)

### Verification

- `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet` → **27 ok, 1 failing** (up from the critic's 22 ok / 1 failing; the 2 new edit blocks added 5 checkable citations, all ok). The single failure is the expected, pre-existing `[AMBIG] operator.cpp:621-639` inside the Correction-2 `[old]` payload that MUST match `linalg-operator-file.md:33`'s bare-basename convention verbatim — fully-qualifying the path would make the `[old]` string fail to match on disk. This is the correct preserve-verbatim decision (the dispatch asked to confirm it; confirmed — it is NOT a citation defect).
- No artifact mutation: all edits land in `reports/<id>/CYCLE.md` (proposed-changes blocks the integrator will apply). `book/` untouched by the repairer.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:
- Apply all of CYCLE.md's proposed-changes blocks, including the two new §"Correction 2-residual (repairer)" edits to `book/src/L0/linalg-operator-file.md:73` and `:80`. After application, the four named sites (`:33`/`:73`/`:80` + `matrix-weighted-norm.md:9`) are all consistent at Category 1.
- The `[AMBIG] operator.cpp:621-639` in `--scan` is a correct preserve-verbatim (bare-basename convention at `linalg-operator-file.md:33`); do NOT "fix" it by fully-qualifying the path inside the `[old]` string — that would break edit applicability.
- Two further Category-mislabel sites remain OUT of this report's scope (`linalg-operator-file.md:22`, `:87`) — tracked in the report's widened residual OQ for a follow-up lifter/integrator pass; not a blocker on this report.
