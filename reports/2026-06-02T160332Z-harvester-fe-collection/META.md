---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T161745Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: warning
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T163500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize fe_collection at L1" (cycle-065 D2)

## Critique

### Checks run

**citation-validity — pass.** Verified every load-bearing pinpoint against the on-disk file
`reference/palace/palace/fem/multigrid.hpp` (Read tool, not codemap — the batch ±1 hazard). All confirm:
`ConstructFECollections` template/signature `:23-26`; whole body `:22-73` with `return fecs;` at `:72` and
closing `}` at `:73` (the planner+D2 correction of codemap's `:75` is correct — confirmed); `pmin`
`constexpr` `:30-33` + `MFEM_VERIFY(p >= pmin, ...)` `:34`; basis selection (`b1=GaussLobatto`,
`b2=GaussLegendre`, `b2=IntegratedGLL if mat_lor`) `:35-39`; `if constexpr` ND/RT-vs-H1/L2 ctor branch
`:46-47` with 4-arg `:49` / 3-arg `:53` + `MFEM_CONTRACT_VAR(b2)` `:54`; early floor `break` `:56-59`;
coarsening switch LINEAR `p--` `:62-64` / LOGARITHMIC `p=(p+pmin)/2` `:65-67` (whole switch `:60-68`);
terminal `std::reverse` `:70`; loop cap `std::max(1, mg_max_levels)` `:44`. Cross-file: `MultigridCoarsening`
enum `palace/utils/labels.hpp:114-119` confirmed (`{ LINEAR, LOGARITHMIC }`); default `LOGARITHMIC`
`palace/utils/configfile.hpp:918` confirmed; `ConstructFiniteElementSpaceHierarchy` `:78-126` with `fecs[0]`
coarse-seed `:90` and p-refinement `AddLevel(... fecs[l] ...)` `:117` (and h-refinement `AddLevel` `:106`)
confirmed; `fe_space.md:84-90` sibling framing of `ConstructFECollections` as a separate construction
confirmed. No drift in this report's own citations. (The report's own §"Open questions" correctly notes the
pre-existing `:22-72`/`:22-75` close-line drift lives in already-firm `fe_space.md` + the old index
deferred-sibling bullet, out of this dispatch's write-scope — that self-flag is accurate; line 72 is the
`return`, 73 the brace.)

**surface-or-evidence (the warrant) — pass.** This is a NEW firm operator, not a refinement of an existing
one, so the check resolves to: is the warrant for a self-standing entry sound? It is. The decisive evidence
is structural and on-disk: `ConstructFECollections` returns `std::vector<std::unique_ptr<FECollection>>`
(`:24,43,72`) — a *list* — and `fe_space` consumes ONE `FECollection`. The codomain mismatch is real, not
rhetorical. The four schedule-only laws (finest-to-coarsest order sequence built then `std::reverse`'d `:70`;
family-dependent `pmin` floor `:30-34`; `mg_max_levels`-bounded length `:44`+`:56-59`;
LINEAR/LOGARITHMIC policy-determines-order-step `:60-68`) are all witnessed and none of them is expressible
on `fe_space` (which has no order-sequence, no level count, no coarsening policy). The producer→consumer
relation across the `[FECollection]` boundary is correctly framed as NOT a dependency (the dep-map and
Dependencies section both say "consumed-by / producer→consumer", not "depends-on"). The independent corroboration
— the `fe_space` author's own deferral of `ConstructFECollections` as "a separate construction"
(`fe_space.md:84-90`, confirmed) — is genuine cross-report evidence, not circular. Warrant=YES is sound.

**rotation-quality — pass (not the central axis of this report).** This is an L1 operator entry, not a
lowering-rotation report; the L1>L0 rotation itself is D3's `fe-collection-construction-rotation` (forward-
referenced). The relevant in-report rotation claim is the L1 abstraction over the L0 imperative loop:
`(p,dim,mg_max_levels,coarsening,family) → [FECollection]` as a pure schedule vs. the mutating
`push_back`/`std::reverse` loop body. That IS a genuine state-hiding compression (the accumulator `fecs`,
the in-place reverse, the per-iteration `p` mutation are all hidden behind a pure list-producing function) —
more abstract/equational than the L0 form. Not a rename. Pass.

**variant-axis-coverage — warning.** Three axes are named and each is positively witnessed and exhaustively
tabulated: de-Rham family (4 subclasses × pmin × ctor arity, `:30-34,46-55`), coarsening policy
(LINEAR/LOGARITHMIC, `:60-68`), LOR basis (`b2` GaussLegendre/IntegratedGLL, `:35-39`). Coverage of the
enumerated cases is complete and well-cited. The warning is a **signature-completeness mismatch, not a hidden
branch**: the typed L1 signature is declared `(p, dim, mg_max_levels, coarsening, family) -> [FECollection]`,
which carries `family` (the L0 *template* parameter) but DROPS `mat_lor` (the L0 *runtime* 5th argument,
`:26`) — yet the report's own third variant axis ("LOR basis selection") IS exactly the `mat_lor` flag. So a
real input that the report itself treats as a variant axis is absent from the arrow type. The L0 callable is
`ConstructFECollections<family>(int p, int dim, int mg_max_levels, MultigridCoarsening mg_coarsening, bool
mat_lor)`. Either `mat_lor` should appear in the L1 signature (e.g. `... coarsening, family, lor: Bool) ->
[FECollection]`) or the entry should state explicitly that the LOR-basis axis is scoped into `family`/a
construction-context parameter rather than a top-level schedule input. This is an internal consistency gap
between the Signature section and the LOR-basis variant-axis section, not an un-witnessed branch — hence
warning, not fail.

**cross-reference-integrity — warning.** `fe_space.md`, `fe_assemble.md` (referenced precedents) resolve on
disk; the SUMMARY insert (existing `fe_space` anchor as context + new `fe_collection` line) resolves cleanly;
the new chapter's own internal links to `./fe_space.md` resolve. The new-chapter forward-reference to D3's
theme is correctly rendered as **plain text** ("Forward-reference `fe-collection-construction-rotation` until
that theme is on disk", body lines 90-91, 224) per the rough-in-forward-reference-must-be-plain-text rule.
HOWEVER: the two `book/src/L1/index.md` edits (the cohort bullet, line 285; the dep-map row, line 290) render
the same forward-reference as a **live link** `[fe-collection-construction-rotation](../L1-L0/fe-collection-construction-rotation.md)`,
and that file is NOT on disk (`book/src/L1-L0/fe-collection-construction-rotation.md` does not exist; it is
D3's deliverable). Under serial per-report integration, if D2 lands before D3 this is a dead link →
`linkcheck2` hard build error. The report is internally inconsistent on this point: its own body de-links the
ref, but its index edits link it. Either both index edits should de-link to plain text (fallback) until D3
lands, or integration must guarantee D3 lands in the same finalize (the directive permits an integrator stub
for a clearly-implied component, which would also clear it). Flagged for the repairer. (Note the analogous
already-firm `fe_space` row at index.md:137 keeps its `fe-space-construction-rotation` ref as **plain text**,
not a live link — the safe pattern the new edits diverge from.)

Secondary, non-blocking: the first index edit block (lines 283-286) bundles the OLD deferred-sibling bullet
(line 284, matches index.md:88 verbatim) and the NEW firm bullet (line 285) inside one ```edit fence without
an explicit old→new separator. The match anchor (line 284) is exact on disk so it is resolvable, but the
replace-directive shape is implicit — worth the integrator's attention to avoid an append-instead-of-replace.

**edge-label-fidelity — pass.** The only edge label is `L1>L0` (the forward-ref to `fe-collection-construction-rotation`)
and the §"Downward (to L0)" prose discusses exactly the L1→L0 rewrite of the `ConstructFECollections` template.
Direction and discussed edge match. The producer→consumer "upstream of `fe_space`" relation is a same-layer
(L1) data-flow statement, correctly NOT labeled as a lowering edge.

**plan-kind-consistency — pass.** Declared kind is firm operator with the `firm (firm-on-positive-structure)`
qualifier. Content matches: whole positive source body read `:22-73`, every law a syntactic identity /
loop-invariant on that body, no rough-in placeholders, no unread sub-part. The firm-on-positive-structure
escape (no-dedicated-`test-multigrid.cpp` does not gate firm because the laws are syntactic identities, not
convergence/iteration semantics) is correctly invoked with the `fe_space`/`fe_assemble`/`apply_linop`
precedent — consistent with the cycle-021 invariant ("firm-on-positive-structure escape"). The status is NOT
over-claimed (no convergence law is asserted) and NOT under-claimed (the structure genuinely is firm). Law 6
(singleton degeneracy) and the "Non-law (MFEM-owned)" note correctly bound what is and isn't L1 substrate.

**skill-uptake-survey — pass.** The report's §"Supporting evidence" states citations were self-verified via
`tools/citecheck/citecheck.py --anchor` against the on-disk file — the cycle-024 mechanical citation-range
realization, which is the relevant procedure for a heavy-citation harvester entry. The warrant-classification
shape (self-standing-operator vs variant-axis-note) does not map to a named skill in the current registry, so
no further uptake is expected. Presence check satisfied.

### Issues found

1. **[warning] variant-axis-coverage / Signature section** (`fe_collection.md` §Signature, lines 95 / 162-168):
   the typed L1 signature `(p, dim, mg_max_levels, coarsening, family) -> [FECollection]` omits `mat_lor`, the
   L0 runtime 5th argument (`multigrid.hpp:26`) that IS the report's own third variant axis ("LOR basis
   selection", `:35-39`). The arrow type and the LOR-basis variant-axis section are mutually inconsistent: a
   declared input axis is absent from the signature. Repair candidate: add `lor: Bool` (or equivalent) to the
   signature, or state explicitly that the LOR axis is folded into a construction-context / `family`-coupled
   parameter rather than a top-level schedule input.

2. **[warning] cross-reference-integrity / index edits** (`book/src/L1/index.md` edit blocks, report lines 285
   and 290): the L1>L0 forward-reference to `fe-collection-construction-rotation` is rendered as a **live link**
   `[...](../L1-L0/fe-collection-construction-rotation.md)`, but that file is not on disk (it is D3's
   deliverable). If D2 integrates before D3 (serial per-report integration), this is a `linkcheck2` hard build
   error. The new chapter body correctly de-links the same ref to plain text; the index edits diverge from both
   that and from the already-firm `fe_space` row (which keeps its rotation ref plain-text at index.md:137).
   Repair candidate: de-link both index references to plain text (fallback), or ensure D3 / an integrator stub
   materializes the theme in the same finalize.

3. **[minor / non-blocking] cross-reference-integrity / edit-directive shape** (report lines 283-286): the
   first `index.md` edit fence bundles the old deferred-sibling bullet (line 284 = index.md:88 verbatim) and the
   new firm bullet (line 285) with no explicit old→new separator. The anchor is exact and resolvable, but the
   replace-vs-append intent is implicit — integrator should treat line 284 as the match-and-replace anchor, not
   append both.

4. **[note, not an issue] pre-existing out-of-scope drift, correctly self-flagged**: `fe_space.md:84,203`
   in-prose `multigrid.hpp:22-72` and the old index deferred-sibling bullet's `:22-75` are both off-by-one/two
   on the template close (`return` at :72, `}` at :73). These are in already-firm `fe_space.md` / the bullet
   being replaced, out of this dispatch's write-scope; the report flags them for a later citation-hygiene pass.
   The replacement bullet (line 285) and dep-map row (line 290) both use the corrected `:22-73`. Accurate.

## Repair

### Fixes attempted

- **Finding (variant-axis-coverage, warning):** the typed L1 signature
  `(p, dim, mg_max_levels, coarsening, family) -> [FECollection]` dropped `mat_lor`, the L0 runtime 5th
  argument (`multigrid.hpp:26`), even though the report's own third variant axis ("LOR basis selection")
  IS the `mat_lor` flag — a signature↔variant-axis inconsistency.
  - **Decision:** repaired.
  - **Action:** Verified the on-disk `ConstructFECollections` signature via Read tool (NOT codemap, per the
    batch ±1 hazard) at `reference/palace/palace/fem/multigrid.hpp:23-26` — confirmed `bool mat_lor` is the
    5th runtime arg. Added `mat_lor: Bool` to the L1 arrow type (placed between `coarsening` and `family`,
    matching the L0 runtime-arg order) in all four signature renderings in CYCLE.md: the chapter header
    signature (`fe_collection.md` line 57), the §Signature block (line 95), the index cohort-bullet
    signature, and the index dep-map-row signature. Added a matching shape-contract bullet for `mat_lor` in
    the §Signature section (`Bool` — LOR-preconditioner basis flag, `:26`, selects `b2`, inert for H1/L2
    faces). The entry stays `firm` — this is a signature-completeness repair, no claim added or changed.

- **Finding (cross-reference-integrity, warning):** the two `book/src/L1/index.md` edits rendered the D3
  forward-reference `fe-collection-construction-rotation` as a **live link** to a not-yet-on-disk file
  (`../L1-L0/fe-collection-construction-rotation.md`, D3's deliverable), while the chapter body correctly
  de-linked it to plain text — an internal body-vs-index inconsistency and a `linkcheck2` hard-error risk if
  D2 lands before D3.
  - **Decision:** repaired.
  - **Action:** De-linked the `fe-collection-construction-rotation` reference to plain text in BOTH index
    edits (the cohort bullet and the dep-map row), matching the chapter body's existing choice and the
    already-firm sibling `fe_space` row's plain-text convention at `index.md:137`. This is the
    `rough-in-forward-reference-must-be-plain-text-not-live-link` convention for a same-cycle not-yet-on-disk
    target; the integrator / a later lifter upgrades to a live link once D3's theme is on disk (or an
    integrator stub clears it). Chose plain-text-in-both (the lower-risk, body-consistent option) over
    live-link-in-both, since serial per-report integration does not guarantee D3 lands before D2.

- **Finding (non-blocking minor, edit-directive shape, issue #3):** the first index edit fence bundles the old
  deferred-sibling bullet and the new firm bullet without an explicit old→new separator.
  - **Decision:** not-needed (no fix applied) — the critic flagged this as non-blocking with an exact,
    resolvable match anchor; it is integrator guidance, not a repair-authority item. Left as-is.

### Unrepairable findings

None. Both warnings were mechanical/surgical (signature completeness from the on-disk L0 arg list; forward-ref
link normalization to the established plain-text convention) — no substantive authoring required.

## Suggested resolution

`ready`. Notes for the integrator:
- The `mat_lor: Bool` parameter now appears in all four signature renderings; the L0 evidence row already
  carried the full C++ signature `(int p, int dim, int mg_max_levels, MultigridCoarsening mg_coarsening, bool
  mat_lor)`, so no further reconciliation is needed.
- The D3 forward-reference `fe-collection-construction-rotation` is now plain-text in both the chapter body
  and both index edits — consistent, and `linkcheck2`-safe regardless of D2/D3 integration order. Upgrade to
  a live link once `book/src/L1-L0/fe-collection-construction-rotation.md` is on disk (D3 finalize, or a
  later lifter / integrator stub).
- Issue #3 (implicit old→new separator in the first index edit fence) stands as integrator guidance: treat
  the deferred-sibling bullet (matching `index.md:88`) as the match-and-replace anchor, not an append.
