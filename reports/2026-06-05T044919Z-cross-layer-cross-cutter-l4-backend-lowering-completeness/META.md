---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T051500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: warning
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-05T053000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of CYCLE — Cross-layer observation: L4 backend-lowering completeness matrix

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing citation was re-read on disk and confirmed in-range and supporting.
- `L4/fe_assemble.md` is `firm` (frontmatter `firmness: firm` line 4; `## Status` "firm" at line 169, harvested cycle-068 — matches the report's "firm (harvested c068)").
- The mis-attribution quote at `L4/index.md:48` is verbatim-correct: line 48 contains "the three construction inputs (`fe_space`/`fe_collection`/`essential_dofs`) absorb into the `readonly` construction stratum (no standalone thin chapters — combinator-as-entry)." The report's claim of a *second* site (line ~100) is also correct — `L4/index.md:100` (the `fe_assemble` table row) carries "the three construction inputs `fe_space`/`fe_collection`/`essential_dofs` absorbed." (The same parenthetical also recurs at `L4/fe_assemble.md:69,147,175` — the proposed-changes block names only the two `index.md` sites, which is a scoping choice, not a citation error.)
- The mis-attribution refutation is sound: `L1/essential_dofs.md:22-23` ("the `DofSet[N]` that `eliminate_essential_bc` and `eliminate_rhs` consume") and `:72-73` ("the producer of the `DofSet[N]` those last two consume") confirm `essential_dofs` feeds the BC cohort, and `L1/fe_assemble.md:60` signature `(space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]` carries no `essential_dofs` parameter. The report's quoted curried form `FiniteElementSpace[N] -> [WeakFormTerm] -> LinearOperator[N,N]` differs cosmetically from the on-disk tuple form but the load-bearing claim ("no `essential_dofs` parameter") is exact.
- The BC-cohort post-composition citations are all in-range and supporting: `L1/eliminate_essential_bc.md:19-22` ("composes AFTER `fe_assemble` and is NOT part of the assembly fold"), `L1/eliminate_rhs.md:23-24` ("post-composition … composes AFTER `fe_assemble`, not as part of the assembly fold"), and `L1/eliminate_rhs.md:142-144` (the named "Separable post-composition with `fe_assemble`" law: "consumes the *already-assembled* operator `K` and is independent of HOW `K` was assembled"). Both BC ops are `firm` (frontmatter).
- The feature-surface and reduce-verb maturity claims check out: each `feature/<name>.L4.md` carries `rank: firm` + `feature_root: seed`, and `boundary-mode.L4.md` carries `feature_root: seed` with NO `rank: firm` line (matching the report's "`seed`, own-readout gate"); the five reduce verbs and `assemble_frequency_operator` carry `rank: firm`/`firmness: firm`. (`domain_energy_reduce.md` uses `rank: firm`, confirming the report's c091-firm claim.)
- Absence claims confirmed mechanically: `ls L2/ L3/ L4/` shows no BC-op chapter; the only L2/L3/L4/feature file referencing the BC ops is `L4/fe_assemble.md` (the absorbed-list); and grep for `no-l4|construction-stratum|by design|combinator-as-entry` over the three BC L1 entries returns nothing (no no-L4-by-design verdict in those entries).

**surface-or-evidence — warning.** This is an observational coverage-gap report (not a refinement-shaped surface change), so the refinement-shape rule no-ops; the relevant adapted question is whether the asserted "genuine hole" is real or whether a disposition exists somewhere the survey missed. The narrow claim is **true**: no *no-L4-by-design verdict* exists for the BC cohort, and it reaches no L2/L3/L4 entry. BUT a book-wide grep surfaces an **existing deferral disposition the survey did not report**: `L4/fe_assemble.md:119` states the BC ops "are sibling deferred operators (the rank-3/4 c069 candidates, gated on primitive-L4-presence per the planner OQ)," and `L4-L3/fe-assemble-fold-dissolution.md:127` independently records "they are sibling speculative operators (the planner's ranks 3-4, deferred to c069)." A deferral-to-a-future-candidate is not a no-L4 verdict, so the report's literal "no no-L4 verdict" claim survives — but the report's stronger framing in the Summary and matrix ("neither reaches L4 **nor is dispositioned**"; matrix cell "no no-L4 verdict") elides this pre-existing deferral note, and the report never mentions c069 / "sibling deferred." The hole is real (undecided + unreached); its characterization as wholly *undispositioned* overstates by omitting the on-disk deferral. This is the issue below.

**rotation-quality — pass (not applicable to observational survey).** The report asserts no algebraic/structural rotation of its own; it surveys maturity and reachability. The one structural relationship it leans on (BC elimination as a *separable post-composition* that sits after the assemble fold) is read from the existing firm L1 laws, not newly claimed as a rotation. No renaming-only or 1:1 rotation is proposed.

**variant-axis-coverage — pass.** The survey is a coverage matrix; it does not introduce an operator with orthogonal variant axes. It correctly handles the dispositioned-obstruction sub-cases (eigen-iteration `opaque-library-ownership`, transient/driven integrator step) in the §"caveat on complete" rather than hiding them, and scopes out the demand-gated waveguide-mode product. No hidden branch.

**cross-reference-integrity — pass.** All chapter references resolve on disk (`L4/fe_assemble.md`, the 12 `feature/*.L4.md`, the 5 reduce verbs, `assemble_frequency_operator.md`, the three BC L1 entries, `L4-L3/fe-assemble-fold-dissolution.md`). The slugs `eliminate_essential_bc` / `eliminate_rhs` / `essential_dofs` exist. The proposed OQ slug `bc-elimination-cohort-l4-disposition` is not yet filed (correct — it is being newly proposed).

**edge-label-fidelity — pass.** The report's framing is L1↔L4 (highest-layer-reached survey). The prose discusses exactly that span — L1 firmness vs L4 reachability — and the one lowering edge it names (`L4-L3/fe-assemble-fold-dissolution`) is discussed as the L4>L3 dissolution it is. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is an observation (coverage gap + consistency drift), and the content shape matches: it surveys, finds one gap + one stale memory claim + one mechanical mis-attribution, and routes the substantive fill to a downstream harvester/abstractor dispatch rather than authoring it. The single proposed-changes block is correctly scoped as mechanical (the `essential_dofs` mis-attribution correction), explicitly NOT the hole-fill. Consistent with the one-observation-per-invocation cross-cutter contract.

**skill-uptake-survey — pass.** The report's own §"Open questions / caveats" explicitly defers L0-line-range re-verification to "lowering-verifier/citecheck territory," correctly scoping citecheck out of a presence/absence cross-layer survey. No skill invocation is implied-but-missing for an absence-and-maturity observation of this shape.

### Issues found

1. **Existing c069 deferral disposition omitted — the "undispositioned" framing overstates** (`CYCLE.md` §Summary and §"The completeness matrix" BC-cohort row and §"The genuine hole"; severity: medium). The report states the BC cohort "neither reaches L4 nor is dispositioned" and the matrix cell reads "no L2/L3/L4; no no-L4 verdict … GENUINE HOLE." On disk, `L4/fe_assemble.md:119` AND `L4-L3/fe-assemble-fold-dissolution.md:127` both record the BC ops as "sibling deferred operators (the rank-3/4 c069 candidates, gated on primitive-L4-presence per the planner OQ)." The literal no-*no-L4-verdict* claim is correct (a deferral is not a no-L4 verdict), and the hole (unreached + undecided) is real — but the report's stronger "nor is dispositioned" language and its silence on the existing deferral note are inaccurate. The report should acknowledge the c069 deferral and re-characterize the gap as "deferred-but-undecided" rather than "undispositioned," and its proposed OQ should note the prior deferral as provenance. (This does not invalidate the recommendation — item 1 already poses the rise-to-L4-vs-no-L4 decision the deferral leaves open — but the framing must reflect the on-disk record.)

2. **Proposed-changes block names only two of the recurring mis-attribution sites** (`CYCLE.md` §"Proposed-changes block"; severity: low). The block targets `L4/index.md:48` and `:100`. The same `(fe_space/fe_collection/essential_dofs)` absorbed-list parenthetical also recurs at `L4/fe_assemble.md:69`, `:147`, and `:175`. The report's claim is scoped to `index.md`, so this is not a false statement, but if the goal is an honest disposition list the chapter-body sites carry the identical mis-attribution and would be left inconsistent with the corrected index. Worth flagging for the repairer/integrator to consider widening the correction scope (or the report explicitly noting the chapter-body sites are out-of-scope for this single mechanical fix).

3. **Signature quoted in non-on-disk form** (`CYCLE.md` §"CAVEAT on the disposition list" and the proposed-changes rationale; severity: cosmetic). The report renders the `fe_assemble` L1 signature as the curried `FiniteElementSpace[N] -> [WeakFormTerm] -> LinearOperator[N,N]`; the on-disk form (`L1/fe_assemble.md:60`) is the tuple `(space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]`. Semantically identical and the load-bearing point (no `essential_dofs` parameter) holds, but the quote is not verbatim.

---

## Repair

### Fixes attempted

- **Finding** (surface-or-evidence, medium): the "neither reaches L4 nor is dispositioned" / "no no-L4 verdict … GENUINE HOLE" framing overstates — a book-wide grep surfaces an existing c069 sibling-deferral note the survey missed (`L4/fe_assemble.md:119` + `L4-L3/fe-assemble-fold-dissolution.md:127`).
  - **Decision**: repaired.
  - **Action**: re-confirmed both citations via Read before editing (`L4/fe_assemble.md:119` = "sibling deferred operators (the rank-3/4 c069 candidates, gated on primitive-L4-presence per the planner OQ)"; `L4-L3/fe-assemble-fold-dissolution.md:127` = "sibling speculative operators (the planner's ranks 3-4, deferred to c069)"). Softened the survey framing in CYCLE.md at four sites: (1) §Summary now reads "deferred-but-undecided" with the c069 citations; (2) §"The completeness matrix" BC-cohort row verdict now "GENUINE HOLE — deferred-but-undecided" with the c069 citations in the cell; (3) §"The genuine hole" gained a "Disposition note (deferred-but-undecided, not undispositioned)" paragraph quoting both deferral lines and stating a deferral is not a no-L4 verdict; (4) §"Open questions / caveats" OQ `bc-elimination-cohort-l4-disposition` now carries the c069 deferral as provenance ("NOT a brand-new question — the live form of the existing c069 sibling-deferral") so the integrator files it as a promotion of the existing deferral, not a fresh OQ. The genuine-hole finding (unreached + decision-unmade) is PRESERVED — only the "wholly undispositioned" overstatement is corrected.

- **Finding** (mis-attribution recurrence, low): the proposed-changes block fixes only the two `L4/index.md` sites; the identical `essential_dofs`-in-the-assemble-`readonly`-stratum mis-attribution recurs at `L4/fe_assemble.md:69,147,175`.
  - **Decision**: repaired (in the report's text — noted for the integrator, not auto-widened into book/ prose).
  - **Action**: verified all three on disk — `:69` (shape-contract bullet), `:147` (state-stratification concept-reference bullet), `:175` (`## Status` variant-axis paragraph) each carry the verbatim `(fe_space / fe_collection / essential_dofs)` absorbed-list and are the SAME mis-attribution. Added a "Recurring-site note (for the integrator)" to the proposed-changes block in CYCLE.md naming the three body sites and explaining why they are NOT folded into the mechanical block: they sit inside chapter-body combinator-as-entry prose (not a flat disposition list), so repointing them is better made together with item-1's L4-disposition decision than as standalone parenthetical surgery. This honors "note it for the integrator rather than over-editing" — extending a mechanical index-list fix into surrounding chapter-body prose would cross into substantive editing.

- **Finding** (signature non-on-disk form, cosmetic): the `fe_assemble` L1 signature is quoted curried; on-disk (`L1/fe_assemble.md:60`) it is the tuple form.
  - **Decision**: repaired.
  - **Action**: confirmed `L1/fe_assemble.md:60` = `fe_assemble :: (space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]`. Replaced the curried quote at both occurrences in CYCLE.md (§"CAVEAT on the disposition list" and the proposed-changes Rationale) with the verbatim on-disk tuple form, adding the `:60` line anchor. Load-bearing claim ("no `essential_dofs` parameter") unchanged.

### Unrepairable findings

None. All three findings were mechanical/surgical (citation-grounded framing softening, an integrator-routed note, and a verbatim-quote correction). No substantive authoring was required; the genuine-hole finding, the OQ proposal, and the `L4/index.md:48/:100` mechanical correction are all preserved intact. No book/ mutation by the repairer (the report remains observational — the only proposed book change is the producer's original index mis-attribution fix, now with an explicit integrator note on the recurring body sites).

## Suggested resolution

`ready`. Notes for the integrator:
- Apply the producer's mechanical proposed-changes block (`L4/index.md:48` + `:100` `essential_dofs` mis-attribution correction) as written.
- The block now carries a recurring-site note: `L4/fe_assemble.md:69,147,175` carry the identical mis-attribution. Either widen the correction to those three body sites when applying the index fix, OR defer them to the downstream item-1 BC-disposition dispatch (the note leaves this as an integrator size/scope judgment).
- File the OQ `bc-elimination-cohort-l4-disposition` as a **promotion of the existing c069 sibling-deferral** (provenance: `L4/fe_assemble.md:119` + `L4-L3/fe-assemble-fold-dissolution.md:127`), not as a brand-new question.
- The memory-refresh recommendation (item 3, `project_l4_is_backend_lowering_target` stale "stranded at L1" claim) remains a meta-phase routing, untouched by this repair.
