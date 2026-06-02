---
agent: cycle-planner
invoked_at: 2026-06-02T164202Z
scope: cycle-066 dispatch plan
status: pending
---

# Cycle 066 dispatch plan

## Goals selected this cycle

Cycle-066 is the THIRD/FINAL primary cycle of meta-batch-20 (cycles 064/065/066; the batch-20
meta-phase fires AFTER this cycle's finalize as a SEPARATE dispatch). It continues the FE-space/mesh-construction
L1 front (the user's resolved strategic steer; `fe_space` firm c064, `fe_collection` firm c065) and
prefers CLEAN CLOSES (last cycle before meta). Two fan-out-ranked axes:
1. **The FE-space sub-spine #3 pick `essential_dofs`** — WARRANT-FIRST harvest of the boundary-attribute-marker →
   essential-true-dof-set extraction, the `DofSet[N]` that `eliminate_essential_bc`/`eliminate_rhs` take opaquely.
   It straddles the MFEM-owned boundary (Palace-authored `AttrToMarker` shape lifts; MFEM `GetEssentialTrueDofs`
   read-as-given) — exactly the warrant-first question the redirect's anti-mirror discipline wants asked.
2. **The L1>L0-theme-layer re-anchor + citation hygiene** (a lifter close) — the theme-layer half of the c065
   opaque-parameter re-anchor (OQ `fe-space-opaque-param-l1-l0-theme-reanchor-to-firm-fe-space`) PLUS the cheap
   `multigrid.hpp` close-line hygiene (OQ `multigrid-hpp-template-close-line-citation-hygiene`) bundled — both
   are clean closes that tidy the front before meta.

Under the 2026-06-01 VOCABULARY-SHIFT REDIRECT: anti-mirror (no degenerate `dof_map` mirror; warrant-first
on whether `essential_dofs` is a genuine concise L1 form vs too-thin MFEM-boundary straddle), replace-and-propagate
(the theme-layer re-anchor completes the front-opening's propagation), lowerings-are-translations (the L1>L0
theme is a real rewrite, not a 1:1 rename). MPI/`Par*`/partitioning read single-rank, flagged-and-skipped.

## Deliverable-presence verification (paste-inline evidence)

**Source-citation discipline note:** the codemap `read_range` ±1 line-drift is CONFIRMED 2-of-2 this batch
on the FE-space header files (c064 `fespace.hpp`, c065 `multigrid.hpp`/`fespace.hpp`; integrator-signals
c065 §Integration-tooling friction). **All line numbers below are verified via the on-disk `Read`/`sed`/`grep`
tools against `reference/palace/`, NOT codemap** — and the dispatch scopes instruct producers to do the same.

### D1 — `essential_dofs` (harvester, warrant-first) — OPEN BY CONSTRUCTION
- **File existence:** `ls book/src/L1/essential_dofs.md` → `No such file or directory` (ABSENT). `ls book/src/L1-L0/essential-dofs*` → `No such file or directory` (ABSENT).
- **Maturity:** N/A (no file). Forward-referenced (plain-text) from `book/src/L1/fe_space.md`, `book/src/L1-L0/fe-space-construction-rotation.md`, `book/src/L1/fe_collection.md`, `book/src/L1/index.md` (`grep -rln 'essential_dofs|essential-dofs' book/src/L1/ book/src/L1-L0/` → those 4 files) — ≥2 converging references, genuinely-implied, no prior-cycle authoring history.
- **OQ-ledger RESOLVED-grep:** `grep -i 'essential_dofs.*RESOLVED|essential-dofs.*RESOLVED|essential_dofs.*CLOSED' scaffolding/open-questions.md` → no matches (open).
- **Structural-block check:** none — fully-present positive Palace source (`AttrToMarker` is Palace-authored at `palace/utils/geodata.hpp:91-96`; the dbc-marker block at `palace/fem/multigrid.hpp:92-101`). Verified open by construction (FE-space sub-spine #3 pick, no prior-cycle history; integrator-signals c064/c065 Suggested-next-dispatches name it).

### D2 — `essential-dofs-construction-rotation` (abstractor, GATED on D1 warrant=YES) — OPEN BY CONSTRUCTION
- **File existence:** ABSENT (`ls book/src/L1-L0/essential-dofs* → not found`, same grep as above).
- **OQ-ledger RESOLVED-grep:** no matches.
- **Structural-block check:** none; gated on D1's warrant (no-op if D1 declines a genuine L1 entry). Open by construction.

### D3 — L1>L0-theme re-anchor + citation hygiene (lifter) — EXISTS, gates stale
- **File existence:** `ls book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` → EXISTS; `ls book/src/L1-L0/weak-form-term-rotation.md` → EXISTS; `ls book/src/L1/fe_space.md` → EXISTS.
- **Maturity / staleness evidence:** `fe-operator-assemble-mutation-rotation.md` `## Status: firm` (`:21`), but `:227-228` reads "The **FE space** itself ... `book/src/L0/fespace-file.md` exists at L0; **no L1 form yet**" — STALE (fe_space firm since c064); `:54`/`:59` reference `space` abstractly (no live `fe_space` cross-ref). Citation-hygiene: `fe_space.md:84` + `:182` cite `multigrid.hpp:22-72` but on-disk `ConstructFECollections` closes at `:73` (`sed -n '68,76p'` → `:72` `return fecs;`, `:73` `}`) → an off-by-one close.
- **OQ-ledger RESOLVED-grep:** `grep 'fe-space-opaque-param-l1-l0-theme-reanchor.*RESOLVED' scaffolding/open-questions.md` → no matches (the theme-layer half is `needs-more`, integrator-signals c065 §Resolution-implications); `multigrid-hpp-template-close-line-citation-hygiene` → `needs-more` (c065 D2 NEW). Both OPEN.
- **Structural-block check:** none — surgical re-anchor + citation tighten on firm-on-disk targets; no gate.

### D4 — FE-space sub-spine count-owner (layer-intro-author, GATED on D1) — EXISTS
- **File existence:** `book/src/L1/index.md` EXISTS; carries the "FE-space sub-spine — 2" cohort (c065 D4 landed 1→2, L1 firm 32→33).
- **Maturity:** the cohort header/count is current at 2 as of c065; D4 bumps to 3 ONLY IF D1 lands firm (count from chapter `## Status` lines per the c057-meta count-owner guard, NEVER from drift-prone index cells).
- **Structural-block check:** none; gated on D1 outcome (refresh-only if D1 declines).

## Warrant verdict (essential_dofs)

**LEANS RECRUIT (warrant-first; D1 makes the final call).** The on-disk ownership boundary
(`multigrid.hpp:92-101`, verified by `sed`) splits cleanly:
- **Palace-authored, LIFTS:** the `bdr_attr_max` extraction (`:95-97`) + `mesh::AttrToMarker(bdr_attr_max, *dbc_attr)`
  (`:98`) — `AttrToMarker` is a Palace-OWN function (`palace/utils/geodata.hpp:91-96`, the array-returning overload),
  the attribute-list → boolean-marker transform is a genuine concise Palace shape with self-standing structure.
- **MFEM-owned, READ-AS-GIVEN (obstruction sub-part):** `GetEssentialTrueDofs(dbc_marker, list)` (`:99-100`) — the
  marker → true-dof-index-set numbering, an opaque MFEM method (dof-numbering not Palace-authored).

So `essential_dofs` has a genuine lift-able Palace-owned head (`AttrToMarker`) and a thin MFEM-opaque tail
(`GetEssentialTrueDofs`) — a natural **firm-with-opaque-tail or `partly-constructive`** entry (the marker→dof-set
read-as-given, parallel to how `fe_space` reads MFEM dof-accessors as-given and `fe_collection` warranted-YES c065).
This is NOT a degenerate mirror — it is a real composition `GetEssentialTrueDofs ∘ AttrToMarker` with a Palace-authored
constituent and a documented MFEM boundary. The redirect's anti-mirror axis is satisfied: there is genuine
representational content (the attribute-marker shape) AND a recorded boundary. **D1 confirms the warrant first**
(genuine concise L1 form? YES-axis above), authoring firm `essential_dofs` + the L1>L0 theme IF warranted, ELSE
recording a no-entry/variant-axis verdict (both VALID) — but the evidence leans YES.

## Dispatches

1. **agent:** `harvester`
   **scope:** WARRANT-FIRST harvest of `book/src/L1/essential_dofs.md` — the FE-space sub-spine #3 pick, the
   boundary-attribute-marker → essential-true-dof-set extraction `GetEssentialTrueDofs ∘ AttrToMarker`. **FIRST judge
   the warrant** (per the redirect anti-mirror): is the attribute→marker→dof-set shape a genuine concise L1 operator
   (YES-axis: `mesh::AttrToMarker` is Palace-AUTHORED `palace/utils/geodata.hpp:91-96` — the attribute-list →
   boolean-marker transform has self-standing structure; the `GetEssentialTrueDofs` tail is MFEM-opaque, read-as-given),
   or too thin / too MFEM-boundary-straddling to warrant an entry (both verdicts VALID — author firm `essential_dofs`
   + flag the L1>L0 theme for D2 IF warranted, ELSE record the no-entry/variant-axis verdict)? Closure sketch IF
   warranted: `essential_dofs :: (space: fe_space, dbc_attr: AttrList) -> DofSet[N]` realizing
   `GetEssentialTrueDofs(AttrToMarker(bdr_attr_max, dbc_attr))` — the **`AttrToMarker` head lifts** (Palace-authored),
   the **`GetEssentialTrueDofs` tail is `obstruction (opaque-library-ownership)` / read-as-given** (MFEM dof-numbering)
   — so the natural status is firm-with-opaque-tail or `partly-constructive` (D1 decides). It cross-refs the now-firm
   `fe_space` (live link `./fe_space.md`), NOT a re-mint; it is the producer of the `DofSet[N]` that
   `eliminate_essential_bc.md:56,68` + `eliminate_rhs.md` take opaquely (consumed-by relations). On-disk anchors
   (VERIFIED via `sed`/`grep`, NOT codemap — the ±1 drift is 2-of-2 this batch on FE headers; re-confirm on-disk
   before emitting any citation): the dbc-marker block `palace/fem/multigrid.hpp:92-101` (`dbc_marker` decl `:92`,
   `bdr_attr_max` `:95-97`, `AttrToMarker` `:98`, `GetEssentialTrueDofs` `:99-100`); h/p-refinement repeats `:107-110`
   / `:118-121`; `AttrToMarker` Palace def `palace/utils/geodata.hpp:91-96` (array-returning overload) + `:79-87`
   (the underlying overloads). D1 OWNS its own `book/src/L1/index.md` dep-map ROW + its own FE-space-sub-spine §cohort
   BULLET (register both — anchor-distinct, parallel-safe); D4 (count-owner) owns ONLY the consolidated tally + the
   cohort-count bump. MPI/`Par*` read single-rank (`GetFinestFESpace` is `ParFiniteElementSpace`-as-given), flagged-and-skipped.
   **deps:** none.
   **rationale:** the highest-fan-out eligible FE-space sub-spine pick (#3, integrator-signals c064/c065 Suggested-next);
   completes the boundary-condition input vocabulary that `eliminate_essential_bc`/`eliminate_rhs` consume opaquely;
   warrant-first per the redirect anti-mirror discipline; clean-closes the `fe-space-essential-dofs-straddles-mfem-owned-boundary` OQ.

2. **agent:** `abstractor`
   **scope:** `book/src/L1-L0/essential-dofs-construction-rotation.md` (canonical slug — D1/D2 coordinate; the LHS
   forward-refs D1's `essential_dofs`). The L1>L0 lowering of the `essential_dofs` form into its L0 body
   (`palace/fem/multigrid.hpp:92-101` dbc-marker block). **Lowering-is-a-translation, NOT a 1:1 rename** (redirect):
   the rewrite narrates how the L1 `GetEssentialTrueDofs ∘ AttrToMarker` form lowers into the `bdr_attr_max`-extraction
   + `mesh::AttrToMarker` call (Palace-authored, lowers here) + the `GetEssentialTrueDofs` MFEM-opaque tail (the
   obstruction sub-part — cite the MFEM method call site `:99-100`, not MFEM internals). If the lowering is degenerate
   identity-in-form → record it as a thin in-line note, NOT a mirrored theme. NO-OP if D1 declines a genuine L1 entry.
   Add the L1-L0/index theme ROW (its own anchor) + the §cohort BULLET. On-disk anchors only (re-confirm via `sed`/`grep`,
   NOT codemap).
   **deps:** D1 (GATED on D1 warrant=YES; forward-refs D1's canonical `essential_dofs` slug — both producers told the
   slug `book/src/L1/essential_dofs.md` / `book/src/L1-L0/essential-dofs-construction-rotation.md` so neither guesses).
   **rationale:** completes the L1>L0 edge for the #3 FE-space sub-spine member same-cycle (couples the floor-landing
   with its lowering per the redirect replace-and-propagate); the L1>L0 theme is the authoritative lowering home.

3. **agent:** `lifter`
   **scope:** TWO bundled clean closes (both clerical, both on firm-on-disk targets):
   (a) **Theme-layer opaque-parameter re-anchor** (OQ `fe-space-opaque-param-l1-l0-theme-reanchor-to-firm-fe-space`,
   integrator-signals c065 §Resolution-implications `needs-more`): re-anchor the FE-cohort L1>L0 THEMES' abstract
   `space` references to live `fe_space` cross-refs, the theme-layer half of the c065 operator-surface re-anchor.
   **SCOPE CORRECTION (verified on-disk):** the OQ said "4 consumer themes" but on-disk only `fe-operator-assemble-mutation-rotation.md`
   + `weak-form-term-rotation.md` carry the abstract `space` references (the BC-elimination legs are folded INTO
   `fe-operator-assemble-mutation-rotation.md`, per the c060 backlog note — there are NO separate `eliminate-rhs`/`eliminate-essential-bc`
   L1>L0 theme files; `ls book/src/L1-L0/` confirms). Re-anchor (i) `fe-operator-assemble-mutation-rotation.md:227-228`
   — the STALE "the **FE space** itself ... no L1 form yet" note → now-firm `fe_space` live link (`../L1/fe_space.md`);
   `:54`/`:59` `space` → live `fe_space` cross-ref; (ii) `weak-form-term-rotation.md` `space`/`A(space, ·)` references
   (`:98,105,133,144,148`) → live `fe_space` cross-ref where they denote the FE space. All themes stay `firm`.
   (b) **Citation hygiene** (OQ `multigrid-hpp-template-close-line-citation-hygiene`): fix the `ConstructFECollections`
   close-line off-by-one in `book/src/L1/fe_space.md` — `:84` + `:182` cite `multigrid.hpp:22-72` but on-disk the
   function closes at `:73` (`sed -n '68,76p' reference/palace/palace/fem/multigrid.hpp` → `:72` `return fecs;`, `:73` `}`).
   Re-anchor `:22-72` → `:22-73` at both loci (and any sibling `:22-72` occurrence — re-grep at fix time, belt-and-suspenders).
   Per the c057-meta lifter promotion-time guard: NO `## Status` flips here (re-anchors only), so no index-cell touch needed;
   verify on-disk before emitting (codemap ±1 drift 2-of-2 this batch — use `sed`/`grep`).
   **deps:** none (the re-anchor targets are firm-on-disk independent of D1/D2; the essential_dofs forward-refs in
   `fe_space.md` are left plain-text this cycle unless D1 lands — see Overlap analysis).
   **rationale:** clean-closes TWO `needs-more` OQs before meta; completes the replace-and-propagate at the theme layer
   (the front-opening's last propagation half); LOW-fan-out hygiene that tidies the FE front for the batch-20 meta-phase.

4. **agent:** `layer-intro-author`
   **scope:** SOLE count-owner — FE-space sub-spine count + cohort-header refresh in `book/src/L1/index.md`. IF D1
   lands `essential_dofs` firm: bump the FE-space sub-spine cohort 2→3 + the L1 firm grand total 33→34 (count from the
   chapter `## Status` line per the c057-meta count-owner guard, NEVER from drift-prone index cells; flip the cohort
   cell WITH the tally). ELSE (D1 declines): refresh the cohort prose to register the warrant-decline disposition,
   NO count change. D4 owns ONLY the consolidated tally + the cohort-count prose; D1 owns its own dep-map ROW + its
   own cohort BULLET (the dual-registration partition — D1 registers its row+bullet, D4 owns the aggregate).
   **deps:** D1 (count is read from D1's landed `## Status`).
   **rationale:** keeps the L1 index count honest at the front frontier; sole-owner discipline avoids the parallel-blind
   shared-tally divergence.

## Overlap analysis

- **D1 ↔ D2:** D2 forward-references D1's `essential_dofs` (canonical slug `book/src/L1/essential_dofs.md` stated in
  BOTH scopes — no guess). D1 authors `book/src/L1/essential_dofs.md` + its `L1/index` dep-map row + cohort bullet;
  D2 authors `book/src/L1-L0/essential-dofs-construction-rotation.md` + its `L1-L0/index` theme row. **Distinct files;
  the only coupling is D2's live link into D1's not-yet-landed chapter** → SEQUENTIAL by forward-reference (D2 wave-2),
  so the per-report integrator wires a live link. Not a same-region conflict.
- **D1 ↔ D3:** D3's re-anchor targets (`fe-operator-assemble-mutation-rotation.md`, `weak-form-term-rotation.md`,
  `fe_space.md` citations) are DISTINCT files from D1's new `essential_dofs.md`. D3 leaves the `essential_dofs`
  plain-text forward-refs in `fe_space.md`/`fe-space-construction-rotation.md` AS-IS this cycle (it touches only the
  `space`-reference and `multigrid.hpp:22-73` loci in `fe_space.md`, NOT the `essential_dofs` forward-ref lines).
  The integrator MAY upgrade the `essential_dofs` forward-refs to live links at apply-time once D1 lands (per the
  on-disk→live-link integrator convention) — that is integrator housekeeping, not a D3 task. **NON-OVERLAPPING** (no
  shared region; D3 and D1 touch disjoint files; D3's `fe_space.md` edits are at `:54/:59/:84/:182/:227-228`-class loci,
  not the `essential_dofs` forward-ref lines). PARALLEL-SAFE.
- **D1 ↔ D4:** D4 reads D1's `## Status` line and owns the `L1/index` consolidated tally + cohort-count prose; D1 owns
  its own dep-map ROW + cohort BULLET (anchor-distinct, the dual-registration partition). The ONLY shared file is
  `book/src/L1/index.md`, but the regions are partitioned (D1 = its row + its bullet; D4 = the tally + count prose).
  Per the standing convention distinct rows/bullets are parallel-safe; the consolidated tally is D4-sole-owned. D4
  needs D1's landed status → SEQUENTIAL (D4 wave-2). **Tally-ownership explicitly partitioned** (D4 sole-owns the
  count; D1 registers ONLY its row+bullet, DEFERS the tally to D4).
- **D2 ↔ D3:** disjoint files (D2 = new `essential-dofs-construction-rotation.md` + `L1-L0/index` row; D3 = existing
  `fe-operator-assemble`/`weak-form-term` themes + `fe_space.md`). Both touch `L1-L0/index.md` only via distinct
  appended rows (D2 adds its theme row; D3 touches no `L1-L0/index` row — it edits theme BODIES + `fe_space.md`).
  **NON-OVERLAPPING.** PARALLEL-SAFE.
- **D2 ↔ D4 / D3 ↔ D4:** D4 touches only `L1/index.md` (tally + count); D2 touches `L1-L0/`; D3 touches L1-L0 theme
  bodies + `fe_space.md`. No `L1/index` count region shared with D2/D3. **NON-OVERLAPPING.**

## Sequencing schedule

- **Wave 1 (parallel):** D1 (`harvester` essential_dofs, warrant-first) ‖ D3 (`lifter` theme re-anchor + citation hygiene).
  D1 and D3 touch disjoint files; D3's targets are firm-on-disk and independent of D1's warrant.
- **Wave 2 (parallel, after wave-1 reports land):** D2 (`abstractor` essential-dofs-construction-rotation, GATED on
  D1 warrant=YES, forward-refs D1's slug) ‖ D4 (`layer-intro-author` count-owner, reads D1's `## Status`).
  Both depend only on D1 (not on each other or D3).

Rationale for the split: D1 is warrant-first (its YES/NO gates D2 and D4's count direction), so D2/D4 wait one wave.
D3 is independent clean-close hygiene → runs in wave-1 alongside D1 for throughput. Per the conflict-tolerance
philosophy, D1‖D3 and D2‖D4 are marked PARALLEL (disjoint files / partitioned `L1/index` regions); any mild
`L1/index` row-vs-tally interleave is cheaply merged by the integrator and is useful integration-tooling signal.

## Open questions / caveats

- **Warrant outcome is D1's call.** The evidence leans RECRUIT (genuine Palace-authored `AttrToMarker` head + MFEM-opaque
  `GetEssentialTrueDofs` tail = a real composition with a documented boundary, parallel to the c065 `fe_collection`
  warrant-YES), but if D1 finds the lift too thin / too MFEM-boundary-dominated, the no-entry/variant-axis verdict is
  VALID and D2/D4 degrade gracefully (D2 no-op; D4 prose-only). Either outcome is a clean close.
- **OQ scope-correction surfaced (recorded for the integrator/meta-phase):** the c065 OQ
  `fe-space-opaque-param-l1-l0-theme-reanchor-to-firm-fe-space` framed the theme-layer re-anchor as "4 consumer themes,"
  but on-disk only 2 L1>L0 theme files carry the abstract `space` reference (`fe-operator-assemble-mutation-rotation.md`
  + `weak-form-term-rotation.md`); the BC-elimination legs are folded INTO the assemble theme (no separate
  `eliminate-rhs`/`eliminate-essential-bc` L1>L0 files exist). D3's scope is corrected to the actual 2 files. The
  batch-20 meta-phase should close the OQ noting the corrected denominator (2, not 4).
- **FOR THE BATCH-20 META-PHASE — codemap ±1 drift recurrence (2-of-2 this batch) warrants a friction-ledger touch.**
  The integrator flagged the `palace-codemap` `read_range` ±1 line-drift on FE-space header files at BOTH c064
  (`fespace.hpp`) and c065 (`multigrid.hpp`/`fespace.hpp`) — a 2-of-2 corroborating signal. This plan worked around it
  by verifying ALL line numbers on-disk (`sed`/`grep`), NOT codemap, and instructing every producer to do the same.
  This is a NEW boundary class (FE-space header files) for the existing `codemap-read-range-plus-one-drift-on-brace-boundary`
  friction entry; the batch-20 meta-phase should (i) increment that entry's recurrence with the FE-header datapoint,
  and (ii) consider a role-spec / skill note that FE-source citations (`fespace.hpp`/`multigrid.hpp`/`geodata.hpp`)
  prefer on-disk `Read` over codemap `read_range`. The on-disk tie-breaker has fully neutralized the drift (zero
  artifact damage both cycles), so this is a characterization upgrade + a possible localization-preference note, NOT
  an escalation (no escaped-drift evidence).
- **All other counts UNCHANGED** unless D1 lands (L2 firm 21+1pc, L2>L1 21, L3 17+4po, L3>L2 6, L4 7+1 rough-in,
  L4>L3 8, L0 22, Phase-1 removals 9/10; FE-assembly sub-spine STAYS 4). The STOP-PROPOSING negative list
  (`L3/solve_family`, `L2/fold_solve`, `L2/fe_assemble`, `lu_solve`/`back_solve`/`ls-update-column`/4 NLEPS atoms)
  is respected — none of this cycle's picks is on it.
