---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T181235Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T182103Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Formalize ls_update_column at L1" (cycle-027 dispatch 4)

## Critique

### Checks run

**citation-validity — warning.** Ran `tools/citecheck/citecheck.py --scan` over the report:
**43 ok / 0 failing**, matching the report's claim exactly. All 15 Palace pinpoint
citations were anchor-spot-checked against `reference/palace/` and confirmed
**zero-drift** — the cycle-026 brace-drift concern in this region does NOT recur:
`:652`/`:831` (`Reconstruct the solution`), `:653`/`:832` (`for (int i = j`), `:655`/`:834`
(`H.data() + i * (max_dim + 1)`), `:656`/`:835` (`s[i] /= Hi[i]`), `:657` (`for (int k = i - 1`),
`:659`/`:838` (`s[k] -= Hi[k] * s[i]`), `:666` (`x.Add(s[k], V[k])`), `:843`
(`x.Add(s[k], Z[k])`), `:612` (`s[0] = beta`), `:642` (`beta = std::abs`), `:644`
(`converged = (beta < eps)`), `:631` (`Norml2`), and `iterative.hpp:193-194` (`s, sn`
`ScalarType` / `cs` `RealType`) all confirmed at the exact cited line. I also `--show`-read
`iterative.cpp:648-667` (GMRES) and `:828-845` (FGMRES) in full: the back-solve loops are
**line-for-line identical** as claimed (`:652-660` ≡ `:831-840`), grounding law 6. The
**warning** is for ONE recurring citation-content drift on a non-Palace pointer: the report
asserts (Summary `:8`, Context, Dependencies §, Evidence §, Supporting-evidence §, and the
Open-questions caveat) that the concept page names the `back_solve` "via `trsv`" at
`concepts/incremental-least-squares.md:10`. Anchor-checking that pointer: `trsv` is **not in
that file at all** (`grep` returns zero hits; `--anchor 'trsv'` → `anchor not found`). The
"via `trsv`" / `back_solve` phrase actually lives in `concepts/givens.md:29`
(`--anchor 'trsv'` on `givens.md:10` → `[DRIFT] suggested givens.md:29`). The report's own
Open-questions caveat (CYCLE.md:633) also mis-cites this as `givens.md:10` (correct is `:29`).
The error is recoverable (the real source line is on record — OQ ledger `:923` already
documents `givens.md:29` as the location), so this is a `warning`, not a `fail`.

**surface-or-evidence — pass.** This is a NEW firm L1 operator (a `new:` file, not a
refinement of existing surface), so the refinement-vs-backfill gate is N/A in its strict
form; the relevant bar is that the new surface is evidence-grounded, which it is — every
structural claim is anchored to positive `iterative.cpp` source read in full. The firm
status rests on the established `lu_solve` / `apply_linop` firm-on-positive-structure
precedent, which I verified verbatim: `book/src/L1/lu_solve.md:83-85` is `firm` on exactly
the "every law a syntactic identity on positive source; a missing test does not gate
syntactic-identity laws" footing this report leans on. The footing is sound and parallel.

**rotation-quality — pass.** This is an L1 leaf harvest (mutation-rotation: L0 in-place
`s[0..j]` overwrite → pure-functional `y = ls_update_column(R, s)`), not a cross-layer
algebraic rotation, so rotation-quality applies in its L1-leaf sense: does the L1 form hide
L0 mechanism more abstractly? Yes — the signature drops the destination buffer, the flat
column-major `H` stride, the `Hi` pointer arithmetic, and the in-place RHS-as-destination
idiom, all correctly deferred to the forthcoming L1>L0 / L2>L1 lowering. The state-hiding
(destination-binding erasure) is a genuine compression, not a 1:1 rename.

**variant-axis-coverage — pass.** Three axes are enumerated and each is explicitly resolved:
element-type (`complex|real`, absorbed via uniform `ScalarType`, `iterative.hpp:193-194`),
basis-lift target (`V`|`Z`, explicitly NOT a structural axis — the back-solve code is
identical across the two, basis read only downstream, law 6), and restart-dimension `j+1`
(size parameter, absorbed-as-form). The report also explicitly scopes OUT a
factorisation-kernel axis (unlike `lu_solve` — `R` is already triangular, so
back-substitution is the unique kernel) and a reduction-strategy axis (the descending sweep
is fixed/load-bearing, not selectable). No hidden branches.

**cross-reference-integrity — warning.** All `[link]` targets resolve on disk
(`L2/incremental-least-squares.md`, `concepts/incremental-least-squares.md`, `L1/lu_solve.md`,
`apply_linop.md`, `ksp_solve.md`, `linear_combination.md`, `apply_nonlinear_pencil.md` all
present; the new `L1/ls_update_column.md` correctly does not pre-exist). All three `edit:`
block anchors are unique and present (`nleps_eigenvalue_correction` dep-map row + cohort
bullet, count 1 each; motif-6 at `L1/index.md:25`; `**Firm (20)**` header at `:31`). SUMMARY
insert anchors verified (`nleps_eigenvalue_correction` at `:84`, `# L1 > L0` at `:86`). The
**warning** is a slug-semantics mismatch against the report's own cited sources: the report
claims its leaf is "the terminal `back_solve` projection ... named by the L2 entry's §'L2 vs
L1 distinction' L1-leaf surface (`L2/incremental-least-squares.md:412`)" and by the concept
page. But `L2/incremental-least-squares.md:412` attaches the slug `ls_update_column` to a
DIFFERENT operation — the column-streaming `ls_update_column(K, j, h_new) → K'` incremental
triangularisation step (advancing the Krylov bundle by one column) — and
`concepts/incremental-least-squares.md:14` does the same (`ls_update_column(K, j, h_new) -> K'`,
explicitly "no explicit `y` solve is needed"). The report has re-used the existing slug
`ls_update_column` for the `back_solve` terminal projection (signature `(R, s) -> y`), which
its own L2 source (`:81-83`) calls a distinct `back_solve` projection, NOT `ls_update_column`.
This is a real name-collision the cited sources contradict: either the report's leaf should
be named `back_solve` (matching `L2:81-83`), or the existing concept/L2 surface that uses
`ls_update_column` for the column-streaming step needs reconciling. Recoverable but should be
flagged for the integrator/lifter to align the slug across L1/L2/concept. Build-readiness
fence guard: **pass** — 8 fences, even parity, cleanly paired (`new:` body `49-508`; three
`edit:` blocks); `## Status` (`:376`), `## Signature` (`:121`), `## Algebraic laws` (`:229`),
`## Evidence` (`:438`) all INSIDE the `new:` fence; no firm apparatus authored outside the
fence; no nested `text` fences (indented-code style used at `:123-126`/`:181-187`/`:421-422`).
The fence-truncation defect is absent.

**edge-label-fidelity — pass.** The report carries no L_{n+1}→L_n edge label (it is an L1
leaf, with the L1>L0 / L2>L1 lowerings explicitly deferred to other dispatches). The
"L1 vs L0 distinction" section discusses precisely the L1/L0 boundary it names. N/A in the
strict edge-label sense; no mismatch.

**plan-kind-consistency — pass.** Declared kind is `firm` L1 operator. The content is a
complete firm body (Signature, Semantics, six holding laws, four explicit non-laws,
Dependencies, Variant axes, Status, Evidence) with no rough-in placeholders. The
firm-on-positive-structure justification is concrete and matches the `lu_solve` precedent.
The load-bearing reduction-order non-law is correctly carried as a recorded non-law (not a
status reduction), consistent with the CLAUDE.md numerical-trick taxonomy
(descending-`i`/column-oriented sweep pins a finite-precision path — correctly classified
load-bearing). Classification is sound.

**skill-uptake-survey — pass.** The report explicitly references its citation-verification
tooling (`citecheck.py --scan` / `--anchor` / `--batch`) in the Evidence and
Supporting-evidence sections, which is the relevant skill-shaped procedure for a
load-bearing-citation harvest. The build-readiness fence guard
(`proposed-changes-fence-encloses-full-body-guard`) is not name-referenced but the report's
structure satisfies it. Pure telemetry surface; non-blocking.

### Issues found

1. **Citation-content drift on the concept-page `trsv` pointer (citation-validity,
   cross-reference-integrity; warning).** The report repeatedly cites
   `concepts/incremental-least-squares.md:10` as naming the `back_solve` "via `trsv`"
   (CYCLE.md Summary `:8` / `lines 33-34`, Context `lines 79-80`, Dependencies `lines 341-343`,
   Evidence `lines 503-504`, Supporting-evidence `lines 585-587`, Open-questions `lines 633-636`).
   The string `trsv` does not occur anywhere in `concepts/incremental-least-squares.md`
   (`--anchor 'trsv'` → not found). The phrase actually lives in `concepts/givens.md:29`.
   The Open-questions caveat additionally mis-cites it as `givens.md:10` (correct: `:29`,
   `+19` drift). Severity: low — recoverable, real source on record (OQ ledger `:923`). Fix:
   re-point every "via `trsv`" reference to `concepts/givens.md:29` and drop the
   incremental-least-squares-concept-page `:10` attribution (that page frames the residual as
   a free byproduct with no explicit `y` solve — it does not mention the back-solve or `trsv`).

2. **Slug collision: `ls_update_column` already names a DIFFERENT operation in the cited L2
   entry and concept page (cross-reference-integrity; warning).** The report harvests its
   leaf under the slug `ls_update_column` with signature `(R: UpperTri[j+1,j+1], s: Tensor[j+1])
   -> Tensor[j+1]` = the terminal `R·y=s` back-solve. But `L2/incremental-least-squares.md:412`
   and `concepts/incremental-least-squares.md:14` both already bind the slug `ls_update_column`
   to the column-streaming incremental-triangularisation step `ls_update_column(K, j, h_new)
   → K'`, and `L2/incremental-least-squares.md:81-83` calls the back-solve the distinct
   `back_solve :: LsqState' -> {...}` terminal projection. So the report claims its
   `back_solve`-shaped leaf is "named by" a surface that actually attaches that slug to a
   different (column-update) operation. Location: CYCLE.md Summary (`lines 24-33`), Context
   (`lines 76-80`), Status/Evidence. Severity: medium — the two siblings (per-column update
   vs terminal back-solve) are genuinely distinct operations; using one slug for both will
   confuse the L2>L1 landing (dispatch-5) and the concept-page reconciliation. Either rename
   the leaf to `back_solve` (matching `L2:81-83`) or record an explicit note that the
   pre-existing `ls_update_column(K,j,h_new)` surface (L2:412, concept:14) is the SAME slug
   denoting the column-update step and must be reconciled. Flag for integrator/lifter.

3. **`L2/incremental-least-squares.md:412` cited as "L1-leaf surface" supporting the
   back-solve framing, but it describes the column-update leaf (cross-reference-integrity;
   warning, sub-issue of #2).** CYCLE.md lines 32-33 / 77 cite `:412` as the L2 entry's
   "§'L2 vs L1 distinction' L1-leaf surface" naming this back-solve leaf. `:412` reads "the
   single opaque leaf `ls_update_column(K, j, h_new) → K'` ... advancing the `Krylov` bundle
   by one column" — i.e. the per-column update, NOT the terminal back-solve. The citation
   line is in bounds and exists; the SEMANTIC support is for a different operation. Same
   recoverability/severity as #2.

### Non-blocking observations (not issues against this report)

- The report's "Resolves OQ `ls-update-column-l1-leaf`" claim is honest about there being no
  discrete ledger entry (CYCLE.md:599-601 anticipates "record as resolved-on-arrival"); grep
  confirms no standalone OQ by that slug exists. Correctly handled.
- The report correctly preserves the `trsv` L3-inventory gap as OPEN (OQ ledger `:24`/`:448`
  confirm it is genuinely BLOCKED with no firm L1 anchor, likely an obstruction-theme target).
  The "general-`trsv` membership" non-law (CYCLE.md:301-308) is a sound, well-anchored
  distinction — `ls_update_column` is the small-dense coordinate-space back-solve (dim `j+1`,
  no collective), a sibling of, not the realisation of, the sparse-triangular field-space
  smoother kernel. This does NOT falsely close the gap. Good.
- The L1 firm count was correctly NOT bumped: `L1/index.md:31` still reads `**Firm (20)**`,
  and the report's deferral note (CYCLE.md:521-522, 612-619) flags the 20→21 increment for
  layer-intro-author/finalize. No incorrect count edit.

## Repair

Both critic warnings were mechanical (a slug rename + a wrong cite pointer); neither
required substantive authoring. Both `repaired`; no findings left `unrepairable`. The
citation core (43 ok / 0 failing, all 15 Palace pinpoints zero-drift, the back-solve loop
`iterative.cpp:652-660` ≡ `:831-840` line-for-line identity, and the
firm-on-positive-structure footing) was verified-sound by the critic and untouched by the
repair — only the operator's slug/name and one off-page cite pointer changed.

### Fixes attempted

- **Finding (issue #2, the significant one): slug collision — `ls_update_column` already
  binds a DIFFERENT operation in the cited L2 entry + concept page.** The report harvested
  the terminal back-solve `(R: UpperTri, s) -> y` under the slug `ls_update_column`, but
  `L2/incremental-least-squares.md:412` + `concepts/incremental-least-squares.md:14` already
  bind `ls_update_column(K, j, h_new) → K'` to the per-column QR-streaming step, and
  `L2/incremental-least-squares.md:81-83` calls THIS operation `back_solve`.
  - **Decision: repaired** (mechanical rename to the artifact-native slug `back_solve`).
  - **Collision check (precondition for the rename being mechanical):** grepped
    `book/src/L1/` + `book/src/SUMMARY.md` for `back_solve` — **zero hits**: no `back_solve`
    file, no `back_solve` operator slug, no `back_solve` SUMMARY entry pre-exists. Neither
    slug is currently in SUMMARY (this report introduces it). `back_solve` is the free,
    correct, artifact-native slug (it is exactly the term `L2:83` and `givens.md:29` use for
    this operation). The rename is cleanly mechanical, not a second collision → `ready`, not
    `needs-revision`.
  - **Action:** renamed `ls_update_column` → `back_solve` throughout the harvested leaf's
    surface — the `new:` proposed-changes path (`new:book/src/L1/ls_update_column.md` →
    `new:book/src/L1/back_solve.md`, CYCLE.md:50), the H1 title (`:51`) and CYCLE H1
    (`:16`), the operator-body slug occurrences (Signature block `:123-126`, Context `:94`,
    `:113`, Signature prose `:153`, Semantics `:166`, laws contract `:202`, laws 1–3
    `:233-249`, non-laws `:290-297`, Dependencies `:312`/`:331`, Variant-axes lead `:347`,
    L1-vs-L0 `:428`, Evidence context `:488`), the `edit:book/src/L1/index.md` dep-map row
    (`:512` link `[`back_solve`](./back_solve.md)`) + cohort bullet (`:519`), the
    `edit:book/src/SUMMARY.md` entry (`:526` → `[back_solve](./L1/back_solve.md)`), the
    Operator-content recap (`:540`/`:543-547`), and the OQ answer-link path (`:606` →
    `book/src/L1/back_solve.md`). **The references to the DISTINCT `ls_update_column`
    column-streaming step were deliberately NOT renamed** (frontmatter input `:9`, Context
    note `:81-83`, Evidence note `:507-509`, Supporting-evidence note `:592`, and the
    verbatim L2-source quote at OQ `:606`) — those correctly name the other operation, and
    I added an explicit disambiguation note (Context `:80-84`) recording that the slug
    `ls_update_column` belongs to the column-update step so the rename rationale is on
    record for dispatch-5 / the lifter. Citations, laws, evidence, variant axes, status all
    unchanged — only the slug/name moved.

- **Finding (issue #1): citation-content drift — `concepts/incremental-least-squares.md:10`
  cited as naming the back-solve "via `trsv`", but `trsv` is absent from that file; the real
  source is `concepts/givens.md:29`, and the OQ caveat mis-cited it as `givens.md:10`.**
  - **Decision: repaired** (mechanical cite-pointer correction).
  - **Verification:** `grep trsv concepts/incremental-least-squares.md` → zero hits;
    `grep -n trsv concepts/givens.md` → `:29` (`"… enabling back_solve via trsv."`), exact
    phrase confirmed on disk.
  - **Action:** re-pointed every "via `trsv`" reference from
    `concepts/incremental-least-squares.md:10` to `concepts/givens.md:29` and re-targeted the
    `[concepts/incremental-least-squares]` links to `[concepts/givens]` where they carried the
    `trsv` attribution: Summary `:35`, Context `:79`, frontmatter inputs `:8`, Dependencies
    concept ref `:345-347`, Evidence `:508`, Supporting-evidence `:592-593`, and the
    OQ caveat block `:642-647` (also fixed the `givens.md:10` mis-cite → `:29` and corrected
    the prose to note `concepts/incremental-least-squares.md` does NOT mention `trsv`). The
    `concepts/incremental-least-squares.md:14` reference to the DISTINCT column-streaming
    `ls_update_column(K,j,h_new)→K'` op was retained where accurate (it is in-bounds and
    correct for that operation).

### Unrepairable findings

None. Both warnings were mechanical and surgical (a global slug rename with a verified
no-collision precondition + an off-page cite-pointer correction with the real source line
confirmed on disk). No substantive authoring, no contradiction requiring human/meta-phase
resolution. Sub-issue #3 (the `:412` "L1-leaf surface" semantic-support mismatch) is fully
subsumed by the issue-#2 rename: the `:412` attribution-to-this-leaf was dropped and replaced
by the correct `:81-83` `back_solve` projection attribution plus the disambiguation note.

### Post-repair verification

- `citecheck.py --scan` re-run on the repaired CYCLE.md: **43 ok, 0 failing (43 citations
  checked)**, exit 0 — the newly-pointed `concepts/givens.md:29` resolves in-bounds (file has
  58 lines); all 15 Palace pinpoints unchanged and still ok.
- Proposed-changes fence parity preserved: 8 fences, even, cleanly paired — `new:back_solve.md`
  body (CYCLE.md:50-515), two `edit:L1/index.md` blocks (`:517-520`, `:524-527`),
  `edit:SUMMARY.md` (`:531-534`); the renamed `new:` path correctly encloses the full firm body.

## Suggested resolution

`ready`. The content is sound; the only defects were the operator slug (collided with the
existing L2/concept `ls_update_column` column-streaming step) and one off-page cite pointer
(`incremental-least-squares.md:10` → `givens.md:29`), both now fixed mechanically.

Notes for the integrator:
- The leaf lands as `book/src/L1/back_solve.md` (NOT `ls_update_column.md`). The dep-map row,
  cohort bullet, and SUMMARY entry all use the `back_solve` slug. No `back_solve` file/slug
  pre-exists, so the `new:` create is collision-free.
- **Coordination:** cycle-027 dispatch 5 (`incremental-least-squares-composition-lowering`
  L2>L1 theme) forward-references this leaf — its repairer was instructed in parallel to
  rename that forward-reference to `back_solve`. The slug used here is exactly `back_solve`,
  so the two stay consistent. Confirm dispatch-5's landing also uses `back_solve` before
  finalize.
- The L1 firm-count 20→21 handoff (CYCLE.md OQ `:621-628`) and the OQ-ledger
  `ls-update-column-l1-leaf` close (answer-link now `book/src/L1/back_solve.md`) are unchanged
  by the repair and remain for layer-intro-author / finalize / meta-phase as the report
  flagged. The dispatch-scope OQ identifier `ls-update-column-l1-leaf` (a hyphenated ledger
  name, not the operator slug) was intentionally left as-is so the ledger linkage is not
  broken.
