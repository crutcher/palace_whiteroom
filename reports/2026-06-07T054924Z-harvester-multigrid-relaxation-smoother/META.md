---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T064500Z
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
repaired_at: 2026-06-07T071500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: repaired
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize multigrid-relaxation-smoother at L1"

## Critique

### Checks run

**citation-validity — warning.** I verified every L0 pinpoint against the on-disk source
(`reference/palace/palace/linalg/distrelaxation.{cpp,hpp}`, read directly — the authoritative
line-map, not codemap `read_range`). The `.cpp` citations are all correct, including the two
the producer reported correcting: `AXPBY(1.0, x, -1.0, r)` is confirmed at **`:110`** (not the
codemap's reported `:113`), and the residual semantics `r = x − A·y` (`A->Mult(y,r)` `:109` then
`AXPBY` `:110`) match the law statements. Ctor `:13-36`, Chebyshev fold `:21-34`,
`B_G->SetInitialGuess(false)` `:35`, `SetOperators` `:38-69`, A/A_G capture `:49-50`,
`dbc_tdof_list_G` `:61`, `B/B_G->SetOperator` `:64-65`, `Mult2` body `:101-119`, sweep loop `:103`,
primary leg `:104-106` w/ `SetInitialGuess` `:105`, aux leg pieces `:109/:110/:111/:112-115/:116/:117`,
`MultTranspose2` `:121-152` — all verify. The `.hpp` class-decl correction also verifies: the Hiptmair
comment is `:23-28` and `class DistRelaxationSmoother : public Solver<OperType>` is **`:30`** (not codemap's
`:29`), so the cited range `:23-30` correctly encloses comment + decl. The correspondence anchors verify:
`chebyshev.hpp:82` (Adams 2003 reference comment), `amg.cpp:19` (`relax_type = 8` GS), `amg.cpp:24`
(`relax_type = 18` GPU l1-Jacobi flip), `ams.cpp:162` (`relax_type = 2` l1-SSOR).
The **warning** is the `.hpp` private-member-block pinpoints in §Record-definition and §Evidence:
the producer corrected the codemap +1 drift on the class line but did NOT correct the field-level
pinpoints, which are themselves drifted (verified by direct `grep -n` on disk):
`pc_it` cited `:35` → actually **`:36`**; `G` cited `:38` → **`:39`**; `A/A_G` cited `:40` → **`:42`**;
`dbc_tdof_list_G` cited `:41` → **`:43`**; `B/B_G` cited `:44-45` → **`:46/:47`**; scratch vectors
cited `:48` → **`:50`**. (The producer's cited values point at the preceding comment/blank lines — the
classic codemap-drift signature the producer claimed to have eliminated but evidently only applied to two
of the load-bearing pins.) The enclosing range `:34-51` is in-bounds and substantially correct, so this is
field-pinpoint drift inside a correct range, not a bounds failure — hence warning, not fail.

**surface-or-evidence — pass.** This is a `new:` constructive entry (a kernel-impl node), not a
refinement of an existing surface, so the rotation_claim/surface-modification disjunction is satisfied
by the new-surface path (it adds new operator text). The record-definition sub-check passes: the
signature names the record `DistRelaxSmoother[N, M]`, and the chapter carries an in-chapter
`## Record definition` section enumerating fields + types + meaning + construction/run-time strata +
the L0 backing struct home (single-consumer case, correctly chosen). The constituent evidence is the
positive `Mult2` body + ctor/`SetOperators` ranges, all cited and verified.

**rotation-quality — pass.** Not a cross-layer rotation claim (this is an own-layer L1 constructive
entry composing firm L1 primitives into a more-abstract relaxation action, not a 1:1 rename). The
genuine abstraction is real: the L0 output-arg-mutation `Mult2(x,y,r)` with four scratch vectors is
re-expressed as a pure `Tensor[N] -> Tensor[N]` action over named legs. No renaming-only mapping.

**variant-axis-coverage — pass.** The variant axes are correctly identified and scoped: the
4th-kind/1st-kind Chebyshev choice (`distrelaxation.cpp:20-34`) is explicitly absorbed into the
`chebyshev-smoother` closure (not a hidden branch here); the `initial_guess` flag is covered as a
degenerate-case fast path (law 5) not an algebraic variant; the `pc_it` sweep count is a pure fold
parameter (law 2). The complex-vs-real `RealAddMult`/`RealMultTranspose` overloads (`:74-94`) are
not surfaced as a variant axis, but they are a real/imag-componentwise application of the same algebra
(transparent), so scoping them out is defensible.

**cross-reference-integrity — warning.** All `[link]` targets resolve on disk (chebyshev-smoother,
apply_linop, axpby, interpolator, set_subvector_zero, divfree-projector, jacobi-smoother,
triangular-solve-obstruction, preconditioning-framework, concepts/sequential-obstruction, L3/chebyshev
all EXIST; the new file is the one being created). The named slugs are all real. Two integration-anchor
concerns lower this to warning: (1) the **SUMMARY.md edit** is a bare nested entry
`    - [multigrid-relaxation-smoother](...)` at 4-space indent, but the L1 SUMMARY uses by-kind
sub-chapter groupings (`- [Constructed-operator gates]` etc. with 2-space-indent nested entries) — the
producer declares a NEW "Kernel-impl (smoother)" kind but supplies no SUMMARY group header / intro page
for it, leaving the entry's grouping placement underspecified for the integrator. (2) The
`## Vocabulary cohort` edit anchor is non-unique in intent: the existing section opens immediately with
the `**Firm (33 main...**` sub-list, and the producer's new `**Kernel-impl (smoother)**` bullet block
gives no before/after placement relative to it. Both are integrator-resolvable placement ambiguities,
not broken links.

**edge-label-fidelity — pass (load-bearing check; passes cleanly).** The `realizes-kernel-api` edge is
declared under the `reference:` key (not `depends-on:`), correctly making it `reference`-class — free,
constraining neither rank nor liveness. The prose, frontmatter comment, Status section, and index edits
all consistently state this ("does NOT `depends-on` that opaque API; it `realizes-kernel-api` it … a
`reference`-class correspondence … constrains neither rank nor liveness"). The four `depends-on` edges
(chebyshev-smoother, apply_linop, axpby, interpolator) are the genuine from-firm-primitives constituents.
The kept obstruction theme is NOT downgraded or deleted: the `triangular-solve-obstruction.md` edit keeps
an obstruction-kind status and role-labels it `kernel-api`. One accuracy nit (not a fidelity failure):
the on-disk Status line is bare **`obstruction`**, but the producer's prose repeatedly says the theme is
"KEPT `obstruction (opaque-library-ownership)`" as if it were already that sub-kind — the edit in fact
*upgrades* bare `obstruction` to the `(opaque-library-ownership)` sub-kind. The upgrade is justified
(HYPRE / external direct-solver ownership is genuinely opaque-library) and DIRECTIVE-3-consistent, and
status stays obstruction-kind (not firm), so this is correct in substance; the "KEPT" wording mildly
misdescribes a sub-kind addition. Noted under Issues, severity low.

**plan-kind-consistency — pass.** Declared kind is a `firm` kernel-impl constructive entry; content shape
matches — full Signature, Record definition, five stated algebraic laws (each a syntactic identity on the
read body), two non-laws, three load-bearing caveats, full Evidence. No rough-in placeholders. The
`firm`-on-positive-structure escape is correctly invoked and warranted: every law IS a syntactic
read-off of the fully-read positive `Mult2`/ctor/`SetOperators` source (e.g. law 1 reads the ordered
two-leg body; law 3 is linearity-of-zero-residual; law 5 is the documented `SetInitialGuess(false)`
zero-skip) — none requires convergence-semantics testing, so the missing dedicated
`test-distrelaxation.cpp` (multigrid-integration coverage only, NL3) is non-gating, exactly the
`chebyshev-smoother`/`jacobi-smoother` precedent. The `pc_it`-sweep sequential-obstruction (NL1) is
correctly documented as an L3-lift `partial-obstruction` concern (body-lifts/sweep-does-not, paralleling
`L3/chebyshev`) that does NOT gate the L1 firm status. The non-symmetry and non-additivity non-laws are
read correctly from the ordered body (`MultTranspose2` `:121-152` reverses leg order) and `Mult2` aux-leg
reading the post-primary-update `y` at `:109`.

**skill-uptake-survey — pass (telemetry only).** The report references `citecheck --anchor` + direct
`Read` for citation verification (the citation-drift-verify discipline) and the firm-on-positive-structure
escape and the partly-constructive/partial-obstruction status machinery. No skill whose invocation is
clearly implied-but-omitted. (Telemetry: the field-pinpoint drift in §Record-definition suggests the
`--anchor` pass was applied only to the two banner-flagged pins, not the hpp member block — a uniform
re-run would have caught the six field drifts.)

**Graded-stack additions.** (9) **rank-invariant — pass.** The entry claims `firm` (rank 3) and rests its
`depends-on` edges only on firm deps (chebyshev-smoother, apply_linop, axpby, interpolator — all firm on
disk), so `rank(impl) ≤ min(rank(deps))` holds (firm ≤ firm). The `realizes-kernel-api` edge to the
`obstruction`-kind theme is `reference`-class and correctly excluded from the rank computation. (10)
**reachability — pass.** The node is reachable from feature roots via the
`L4/preconditioning-framework` (multigrid V-cycle) consumer that installs it as the per-level smoother
(reference noted), and it is the named consumer for DIRECTIVE-2 grounded-consumer item (geometric
multigrid). Wired into `SUMMARY.md` (modulo the grouping-placement warning above).

### Issues found

1. **hpp private-member field pinpoints drifted (citation-validity, warning).**
   `book/src/L1/multigrid-relaxation-smoother.md` §Record definition (the field-comment annotations
   `:35/:38/:40/:41/:44-45/:48`) and §Evidence (`distrelaxation.hpp:34-51` sub-pins). On-disk exact lines
   (direct `grep -n`): `pc_it` **`:36`** (cited `:35`), `G` **`:39`** (`:38`), `A/A_G` **`:42`** (`:40`),
   `dbc_tdof_list_G` **`:43`** (`:41`), `B/B_G` **`:46`/`:47`** (`:44-45`), scratch `x_G,y_G,r_G,r`
   **`:50`** (`:48`). Each cited value points one-to-two lines early (at the preceding comment/blank line).
   The enclosing `:34-51` range is correct and in-bounds; only the field-level pinpoints drift. Severity:
   low-to-moderate (load-bearing for a reviewer cross-checking the record against the C++ struct).

2. **SUMMARY.md entry grouping underspecified (cross-reference-integrity, warning).**
   `reports/.../CYCLE.md` SUMMARY.md edit block (the `    - [multigrid-relaxation-smoother]` line). The
   producer introduces a new "Kernel-impl (smoother)" kind but provides no SUMMARY by-kind group header /
   intro page; the bare 4-space-indented entry has no resolved parent group in the existing by-kind nesting
   (Constructed-operator gates, BLAS-1, etc.). Integrator must decide the group placement. Severity: low
   (placement, not a broken link).

3. **`## Vocabulary cohort` edit anchor placement non-unique (cross-reference-integrity, warning).**
   `book/src/L1/index.md` — the new `**Kernel-impl (smoother)**` bullet block gives no before/after
   placement relative to the existing `**Firm (33 main…**` sub-list that immediately follows the heading.
   Integrator-resolvable. Severity: low.

4. **"KEPT `obstruction (opaque-library-ownership)`" mildly misdescribes a sub-kind upgrade
   (edge-label-fidelity, low).** `book/src/L1-L0/triangular-solve-obstruction.md` is bare `obstruction`
   on disk (`:545`); the edit + report prose describe it as KEPT-at-`(opaque-library-ownership)` when the
   edit in fact *adds* the sub-kind. Substantively correct and DIRECTIVE-3-justified (status stays
   obstruction-kind, not downgraded/deleted), so this does not fail the check — flagged for accuracy of the
   "KEPT" framing only.

## Repair

### Fixes attempted

- **Finding 1 — hpp private-member field pinpoints drifted (citation-validity, warning).**
  - **Decision**: repaired.
  - **Action**: Verified the corrected lines by direct `grep -n` on
    `reference/palace/palace/linalg/distrelaxation.hpp` (lines 34-51): `pc_it` is
    on `:36`, `G` `:39`, `A`/`A_G` `:42`, `dbc_tdof_list_G` `:43`, `B` `:46` /
    `B_G` `:47`, scratch `x_G,y_G,r_G,r` `:50` — all six match the critic's
    corrections. Applied to `reports/<id>/CYCLE.md` in three places: the
    §Record-definition record-block field annotations (added the on-disk `hpp
    field :NN` pins per field), the §Record-definition Strata "Run-time" scratch
    pin (`:48`→`:50`), the §Evidence `distrelaxation.hpp:34-51` sub-pin line
    (`:35/:38/:40/:41/:44-45/:48` → `:36/:39/:42/:43/:46/:47/:50`), and the
    §Open-questions scratch-vector pin (`:48`→`:50`). The enclosing range
    `:34-51` was already correct and left untouched. (The `:35`
    `B_G->SetInitialGuess(false)` reference is a `.cpp` line, not an hpp field —
    correctly left unchanged.)
  - In-scope per "Citation line range off by a small offset (a few lines slip)."

- **Finding 2 — SUMMARY.md entry grouping underspecified (cross-reference-integrity, warning).**
  - **Decision**: repaired.
  - **Action**: Resolved the SUMMARY placement per the kernel-impl chapter-kind
    sensible-default mechanics (no new SUMMARY machinery). The chapter
    self-identifies as "a constructed-operator gate at L1, in the family of
    `chebyshev-smoother` and `divfree-projector`" (§Context), so it is filed into
    the existing **Constructed-operator gates** by-kind sub-chapter group at its
    alpha position (after `ksp_solve`, the current last entry — `m` > `k`), as a
    2-space-indented nested entry matching the group's other entries. Rewrote the
    `edit:book/src/SUMMARY.md` block to a 2-space entry anchored on the unchanged
    `ksp_solve` line, dropping the bare 4-space orphan + the would-be new
    "Kernel-impl (smoother)" group header. The `kernel-impl` role-label lives on
    the `## Status` line + index cells, not the SUMMARY grouping. Added an inline
    note in the CYCLE.md documenting the placement decision.
  - In-scope per "Append-by-slug hint where the slug is obvious from context" +
    the kernel-impl chapter-kind sensible-default placement (CLAUDE.md
    §Methodology-invariants "Kernel-API vs kernel-IMPLEMENTATION distinction" —
    "no new linter / SUMMARY machinery required").

- **Finding 3 — `## Vocabulary cohort` + dep-map edit anchors non-unique (cross-reference-integrity, warning).**
  - **Decision**: repaired.
  - **Action**: (a) Dep-map (`book/src/L1/index.md` `## Operator dep-map`): the
    bare `| **Kernel-impl (smoother)** |` by-kind header row was dropped and the
    `multigrid-relaxation-smoother` row re-anchored into the existing
    **Constructed-operator gates** group at alpha position, anchored on the
    unchanged on-disk `ksp_solve` dep-map row (now a unique 2-line edit anchor);
    the kernel-impl-ness is carried by the `**kernel-impl**` status-cell
    role-label. (b) Vocabulary cohort (`## Vocabulary cohort`): re-anchored the new
    **Kernel-impl (smoother)** bullet block to FOLLOW the section's unique final
    paragraph (the "(empty as of cycle-010)…" Queued-list line), placing it at the
    TAIL of the section (after the Queued sub-list, before `## Operator dep-map`)
    instead of an ambiguous top-of-section insert against the `**Firm (33 main…**`
    sub-list. Both edit blocks now carry a unique on-disk anchor line; inline notes
    added.
  - In-scope per "Trivial cross-reference fix" + append-by-slug fallback
    (placement of an obvious-slug entry, no content authoring).

- **Finding 4 — "KEPT `obstruction (opaque-library-ownership)`" mildly misdescribes a sub-kind upgrade (edge-label-fidelity, low).**
  - **Decision**: repaired.
  - **Action**: Verified on disk that `book/src/L1-L0/triangular-solve-obstruction.md`
    `## Status` (`:543`) is bare `obstruction`; the edit genuinely *adds* the
    `(opaque-library-ownership)` sub-kind (substantively correct, DIRECTIVE-3
    justified — HYPRE / external direct-solver ownership is genuinely
    opaque-library, status stays obstruction-*kind*). Re-framed the misdescribing
    prose: the `edit:book/src/L1-L0/triangular-solve-obstruction.md` Status block
    now says the edit "adds the `kernel-api` role-label AND clarifies the sub-kind
    from the prior bare `obstruction` … stays obstruction-kind (NOT downgraded,
    NOT promoted)" rather than "It KEEPS `obstruction (opaque-library-ownership)`
    status"; the §Supporting-evidence "Kept kernel-api theme" note and the
    frontmatter `inputs` line were likewise corrected to "retained obstruction-kind;
    role-label added + sub-kind clarified bare obstruction → opaque-library-ownership."
    The two remaining "the KEPT … theme" adjectival uses (Summary prose, frontmatter
    comment) accurately mean "the retained theme" and were left unchanged.
  - In-scope per "Edge-label fix where the … prose" — a mechanical framing
    correction matching the substantively-correct edit; no content authored.

### Unrepairable findings

None. All four flagged findings were mechanical/surgical (citation-offset
correction, integrator-placement anchoring per the kernel-impl chapter-kind
sensible-default, edit-anchor uniqueness, framing correction of a
substantively-correct sub-kind edit). No substantive authoring was required and
no content decisions were made.

## Suggested resolution

`ready` — integrator may apply. Notes for the integrator:
- All edit blocks now carry unique on-disk anchors. The two `book/src/L1/index.md`
  edits and the `book/src/SUMMARY.md` edit place `multigrid-relaxation-smoother`
  into the existing **Constructed-operator gates** by-kind group at alpha position
  (after `ksp_solve`); no new SUMMARY/dep-map "Kernel-impl (smoother)" group is
  introduced — kernel-impl-ness rides the `## Status` / status-cell role-label.
- The `## Vocabulary cohort` bullet block lands at the TAIL of the section
  (before `## Operator dep-map`).
- The producer's `## Index tally NOT touched` open-question (CYCLE.md
  §Open-questions) is preserved for integrator confirmation: this kernel-impl is a
  distinct *kind*, so the "33 main / 43 firm" consolidated tally is intentionally
  left unchanged.
- D1 forward-reference coupling (the geometric-multigrid column forward-references
  this canonical slug) is noted in CYCLE.md §Open-questions; the per-report
  integrator wires the live link when both land.
