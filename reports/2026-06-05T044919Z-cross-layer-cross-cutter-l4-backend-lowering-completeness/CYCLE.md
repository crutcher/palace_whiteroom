---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-05T044919Z
scope: L1↔L4 cross-cut — L4 backend-lowering completeness matrix for the in-scope feature set
status: pending
integrated_at: 2026-06-05T051726Z
integration_commit: 8cb576ec1f4fcad7752ebba5bf23b16076a0cf28
integration_notes: "Applied cycle-100 (staging row 3/4). Observational evidence artifact; only book change a 2-site mechanical essential_dofs mis-attribution repoint at L4/index.md:48,:100. OQ bc-elimination-cohort-l4-disposition promoted. Survey CONFIRMED all 5 solver pipelines + 5 output-products reach firm L4 and REFUTED the stale memory project_l4_is_backend_lowering_target 'FE-assembly stranded at L1' (assemble-half closed c068). FLAGGED for batch-32 meta-phase: re-scope that memory's named hole to BC-elimination cohort. Build EXIT 0; step-5b rank_violations 0."
---

# CYCLE: Cross-layer observation — L4 backend-lowering completeness matrix

## Summary

I surveyed the in-scope stack for **L4 backend-lowering completeness** — for each in-scope feature (5 solver pipelines, FE-assembly/FE-space cohort, 5 output-products) I determined the highest layer reached on disk and whether it reaches a firm L4 cap / L4 feature surface OR carries an on-disk no-L4-by-design verdict. **The result is near-complete: all 5 solver pipelines + all 5 output-products reach `firm` L4 feature surfaces, and the FE-assembly assemble-fold reaches `firm` L4 (`fe_assemble`).** The CLAIM in memory `project_l4_is_backend_lowering_target` that "the FE-assembly/FE-space cohort stranded at L1 is a hole to close" is **REFUTED for the assemble-half** (it closed at cycle-068 — `fe_assemble` is firm at L4, and the construction-stratum constituents `fe_space`/`fe_collection`/`weak_form_term` carry an explicit on-disk no-L4-by-design verdict: absorbed into `fe_assemble`'s `readonly` construction stratum, combinator-as-entry). **One GENUINE remaining hole survives**: the **boundary-condition elimination cohort** (`eliminate_essential_bc`, `eliminate_rhs`, `essential_dofs`) is firm at L1, is **explicitly a separable post-composition that runs AFTER the `fe_assemble` fold** (so it is NOT absorbed by the assemble combinator), appears in **no L4 entry, no L2/L3 entry, and no driver feature-column body**, and carries **no no-L4-by-design verdict**. This is a firm-L1 in-scope construction that is **deferred-but-undecided** — it neither reaches L4 nor carries a no-L4 verdict, but an on-disk **c069 sibling-deferral note exists** (`L4/fe_assemble.md:119` + `L4-L3/fe-assemble-fold-dissolution.md:127` both record the BC ops as "sibling deferred operators … the rank-3/4 c069 candidates"). So the hole is real (unreached + the disposition decision unmade), but it is *deferred-pending-c069*, NOT wholly undispositioned.

## Observation kind

**Coverage gap** — a firm-L1 in-scope construction cohort (boundary-condition elimination) that reaches neither L4 nor an on-disk no-L4-by-design verdict; plus a **consistency drift** correction to memory `project_l4_is_backend_lowering_target` (the FE-assembly-stranded-at-L1 claim is stale — the assemble-half closed at cycle-068).

## Specific finding

### The completeness matrix

Status claims are the `## Status` line of each on-disk chapter unless noted.

| Feature | Highest layer reached | Verdict |
|---|---|---|
| **electrostatic** pipeline | `feature/electrostatic.L4.md` — `firm` (promoted c095) | **complete** |
| **magnetostatic** pipeline | `feature/magnetostatic.L4.md` — `firm` (promoted c095) | **complete** |
| **eigenmode** pipeline | `feature/eigenmode.L4.md` — `firm` (promoted c085) | **complete** (eigen-iteration carries `obstruction (opaque-library-ownership)` — dispositioned, not a hole) |
| **driven** pipeline | `feature/driven.L4.md` — `firm` | **complete** |
| **transient** pipeline | `feature/transient.L4.md` — `firm` (promoted c085) | **complete** (opaque integrator step absorbed by `fold_solve`, dispositioned) |
| lifecycle ROOT (meta-feature) | `feature/lifecycle.L4.md` — `firm` | **complete** |
| boundary-mode pipeline (6th driver) | `feature/boundary-mode.L4.md` — `seed` (own-readout gate; demand-gated waveguide-mode product) | **dispositioned** (`seed` is the root marker + a stated own-readout promotion route; not in the 5-pipeline scope; not a hole) |
| **FE-assembly — assemble-fold** | `L4/fe_assemble.md` — `firm` (harvested c068) | **complete** |
| FE-space constituents (`fe_space`, `fe_collection`, `weak_form_term`) | `firm` at L1; no L2/L3/L4 | **no-L4-by-design** — explicit on-disk verdict: absorbed into `fe_assemble`'s `readonly` construction stratum, "no standalone thin chapters — combinator-as-entry" (`L4/index.md:48`) |
| FE-assembly leaf `assemble_term` (libCEED) | rises as black-box-kernel `readonly` input to `fe_assemble` | **no-L4-by-design** (lifts `L1-L0/fe-assemble-libceed-boundary-obstruction`, `obstruction (opaque-library-ownership)`) |
| driven rank-2 assemble (`assemble_frequency_operator`) | `L4/assemble_frequency_operator.md` — `firm` | **complete** |
| **S-parameters** | `feature/sparameters.L4.md` — `firm`; reduce verb `L4/sparameter_reduce.md` — `firm` (c083) | **complete** |
| **capacitance** | `feature/capacitance.L4.md` — `firm` (c095); reduce verb `L4/gram_reduce.md` — `firm` (c095) | **complete** |
| **inductance** | `feature/inductance.L4.md` — `firm` (c095); reduce verb `L4/gram_reduce.md` — `firm` | **complete** |
| **eigenfrequencies+Q** | `feature/eigenfrequency-qfactor.L4.md` — `firm`; reduce verb `L4/eigenfreq_qfactor_reduce.md` — `firm` (c082) | **complete** |
| **energy-fields** | `feature/energy-fields.L4.md` — `firm`; reduce verb `L4/domain_energy_reduce.md` — `firm` (c091) | **complete** |
| **BC-elimination cohort** (`eliminate_essential_bc`, `eliminate_rhs`, `essential_dofs`) | `firm` at L1; **no L2/L3/L4; no no-L4 verdict** (but a c069 sibling-deferral note exists, `L4/fe_assemble.md:119` + `L4-L3/fe-assemble-fold-dissolution.md:127`) | **GENUINE HOLE — deferred-but-undecided** (see below) |

### The FE-assembly verdict (the highest-value cross-check)

**The memory claim is REFUTED for the assemble-half and must be updated.** Memory `project_l4_is_backend_lowering_target` says "the FE-assembly/FE-space cohort stranded at L1 is a hole to close." On disk:

- `L4/fe_assemble.md` is **`firm`** (harvested cycle-068 D1, plan-tag `fe-cohort-l4-lift`). The status line: the `foldr`-producing-a-sum combinator `fe_assemble space terms = sum (map (assemble_term space) terms)` promoted on the firm-on-positive-structure escape, ≥2-witness mining-gate met with 3 witnesses (electrostatic ∇, magnetostatic ∇×, mass I).
- The FE-space construction constituents are **explicitly dispositioned no-L4-by-design** at `L4/index.md:48`: "the three construction inputs (`fe_space`/`fe_collection`/`essential_dofs`) absorb into the `readonly` construction stratum (no standalone thin chapters — combinator-as-entry)." `weak_form_term` "rides as the fold's list element-type." `assemble_term` rises as a black-box-kernel `readonly` input.
- The L4>L3 dissolution exists: `L4-L3/fe-assemble-fold-dissolution.md` (cycle-068 D2).

So the FE-assembly cohort is NOT stranded at L1; its assemble-fold reaches firm L4 and its construction constituents are dispositioned. **The memory's hole claim is now stale by ~30 cycles.**

**CAVEAT on the disposition list — a within-disposition inconsistency:** `L4/index.md:48` groups `essential_dofs` into the assemble `readonly` construction stratum. But on disk `essential_dofs` is NOT a `fe_assemble` input — `L1/essential_dofs.md:22-23,72` states it produces the `DofSet[N]` that `eliminate_essential_bc` and `eliminate_rhs` consume (the BC-elimination cohort), and `L1/fe_assemble.md`'s signature (on-disk, `:60`) is `(space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]` — `essential_dofs` does not appear in it. So `essential_dofs` is mis-attributed to the absorbed-assemble stratum; it actually belongs to the BC-elimination cohort below, and so is part of the genuine hole, not part of the closed assemble-half.

### The genuine hole: BC-elimination cohort

`eliminate_essential_bc`, `eliminate_rhs`, and their producer `essential_dofs` are all **`firm` at L1** (`L1/eliminate_essential_bc.md`, `L1/eliminate_rhs.md`, `L1/essential_dofs.md` — all "PROMOTE — clean" / "firm — FE-space sub-spine essential-dof-set constructor"). They have **no L2/L3/L4 chapter** (confirmed: `ls L2/ L3/ L4/` shows none) and carry **no no-L4-by-design verdict** (grep for `no-l4|construction-stratum|by design|caps at L1` returns nothing in their L1 entries).

They are **not absorbed by any L4 cap**. The on-disk evidence that they are a *separate, post-assembly* step (so `fe_assemble`'s construction-stratum absorption does NOT cover them):

- `L1/eliminate_essential_bc.md:19-22`: "it composes AFTER `fe_assemble` and is NOT part of the assembly fold."
- `L1/eliminate_rhs.md:23-24`: "post-composition on the assembled operator — it composes AFTER `fe_assemble`, not as part of the assembly fold."
- `L1/eliminate_rhs.md:142-144`: the load-bearing **"Separable post-composition with `fe_assemble`"** law: "it consumes the *already-assembled* operator `K` and is independent of HOW `K` was assembled."

They appear in **no L4 chapter** (grep `eliminate_essential|eliminate_rhs` over `L4/` and `feature/` returns only `L4/fe_assemble.md`, which merely names them in the absorbed-list — the mis-attribution above) and in **no driver feature-column body** (grep over `feature/` returns nothing — the electrostatic/magnetostatic/etc. columns compose `fe_assemble → solve → reduce` and never render the BC-elimination step that Palace actually runs between assemble and solve).

This is a genuine coverage gap: a firm-L1, in-scope construction (every solver pipeline performs essential-BC elimination on the assembled operator + RHS lift before the solve) that neither reaches L4 nor carries a no-L4 disposition. It is the BC-half analog of the now-closed assemble-half.

**Disposition note (deferred-but-undecided, not undispositioned):** the cohort is NOT wholly silent on disk — an existing **c069 sibling-deferral note** records the rise-vs-no-L4 decision as *deferred*, just not *decided*:
- `L4/fe_assemble.md:119`: the BC ops "are sibling deferred operators (the rank-3/4 c069 candidates, gated on primitive-L4-presence per the planner OQ)."
- `L4-L3/fe-assemble-fold-dissolution.md:127`: "They are sibling speculative operators (the planner's ranks 3-4, deferred to c069), NOT part of this assemble-fold dissolution."

A deferral-to-a-future-candidate is **not** a no-L4-by-design verdict (the rise-vs-no-L4 decision is still open), so the hole is real — but it is *deferred-pending-c069*, which the survey's earlier "neither reaches L4 nor is dispositioned" framing overstated. The OQ recommended below carries this c069 deferral as provenance rather than filing the question as brand-new.

## Recommendation

Two follow-ups, fan-out-ranked:

1. **(Primary, dispatch a harvester/abstractor) — disposition the BC-elimination cohort's L4 reachability.** Decide whether `eliminate_essential_bc` + `eliminate_rhs` (a) rise to L4 as a small post-assembly combinator (an operator→operator BC-pin verb + an RHS-lift verb, the separable post-composition of `L1/eliminate_rhs.md:142`), or (b) carry an explicit no-L4-by-design verdict (e.g. construction/setup-stratum, absorbed into the driver feature columns' assemble preface like `fe_space`). Either resolves the hole; the on-disk separable-post-composition law makes (a) a clean small combinator candidate. This is the BC-half of the same `fe-cohort-l4-lift` plan-tag that closed the assemble-half at c068.

2. **(Mechanical, integrator/lifter — proposed-changes below) — correct the `essential_dofs` mis-attribution at `L4/index.md:48`.** It is listed in the `fe_assemble` absorbed-construction-stratum, but on disk it feeds the BC-elimination cohort, not the assemble fold. Move it from the "absorbed into `fe_assemble`'s readonly stratum" list into the BC-cohort disposition (whatever item 1 decides), OR re-word to reflect that `essential_dofs` is consumed by the *post-assembly* BC ops rather than the assemble fold.

3. **(Mechanical, defer to meta-phase) — refresh memory `project_l4_is_backend_lowering_target`.** The "FE-assembly/FE-space cohort stranded at L1 is a hole to close" sentence is stale: the assemble-half closed c068. Re-scope the named hole to the BC-elimination cohort (item 1).

### Proposed-changes block (for integrator-per-report, Phase 5 — do NOT apply in dispatch)

This is the single mechanical correction (item 2). It does NOT fill the hole (that is item 1's downstream dispatch); it only fixes the on-disk mis-attribution so the disposition list is honest.

- **File:** `book/src/L4/index.md`, line ~48 (the `fe_assemble` bullet) AND line ~100 (the `fe_assemble` table row, same parenthetical).
- **Current text (both sites):** "the three construction inputs (`fe_space`/`fe_collection`/`essential_dofs`) absorb into the `readonly` construction stratum (no standalone thin chapters — combinator-as-entry)."
- **Proposed text:** "the two construction inputs (`fe_space`/`fe_collection`) absorb into the `readonly` construction stratum (no standalone thin chapters — combinator-as-entry); `essential_dofs` is NOT a `fe_assemble` input — it produces the `DofSet[N]` consumed by the *post-assembly* boundary-condition cohort (`eliminate_essential_bc`/`eliminate_rhs`, `L1/essential_dofs.md:22-23,72`), whose L4 disposition is open (see OQ `bc-elimination-cohort-l4-disposition`)."
- **Rationale / evidence:** `L1/essential_dofs.md:22-23,72` (producer of the DofSet for the BC ops) + `L1/fe_assemble.md:60` signature `(space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]` (no `essential_dofs` parameter).

**Recurring-site note (for the integrator):** the identical `(fe_space/fe_collection/essential_dofs)` absorbed-list parenthetical also recurs in the `L4/fe_assemble.md` chapter body at lines `:69`, `:147`, and `:175` (the shape-contract bullet, the `state-stratification` concept-reference bullet, and the `## Status` variant-axis paragraph). These are the SAME `essential_dofs`-in-the-assemble-`readonly`-stratum mis-attribution as the two `index.md` sites; left uncorrected they leave the chapter body inconsistent with the corrected index. They are NOT included in the mechanical proposed-changes block above because they sit inside chapter-body combinator-as-entry prose (not a flat disposition list), so repointing them is a chapter-body edit best made together with item 1's L4-disposition decision (when the BC cohort's home is settled) rather than as a standalone parenthetical surgery. Integrator: widen the correction to these three sites if applying the index fix in isolation, or defer them to the item-1 dispatch.

(I am a DISPATCH-phase agent; I do not touch `book/`. The above is for Phase-5 application.)

## Supporting evidence

- L4 firm cohort: `book/src/L4/fe_assemble.md` §Status (firm, c068); `book/src/L4/index.md:32,48,73,100` (FE-cohort→L4 framing + construction-stratum absorption verdict); `book/src/L4/assemble_frequency_operator.md` §Status (firm); output-product reduce verbs `book/src/L4/{sparameter_reduce,gram_reduce,eigenfreq_qfactor_reduce,domain_energy_reduce}.md` §Status (all firm).
- Feature L4 surfaces (all `firm` except boundary-mode `seed`): `book/src/feature/{electrostatic,magnetostatic,eigenmode,driven,transient,lifecycle}.L4.md` §Status; `book/src/feature/{sparameters,capacitance,inductance,eigenfrequency-qfactor,energy-fields}.L4.md` §Status; `book/src/feature/boundary-mode.L4.md` §Status (`seed`, own-readout gate).
- FE-assembly cohort L1 maturity (all firm): `book/src/L1/{fe_assemble,fe_space,fe_collection,bilinear-form,weak_form_term,assemble-diagonal,divfree-projector}.md` §Status.
- The genuine hole: `book/src/L1/eliminate_essential_bc.md:19-22`; `book/src/L1/eliminate_rhs.md:23-24,142-144`; `book/src/L1/essential_dofs.md:22-23,72`; absence confirmed by `ls L2/ L3/ L4/` (no BC-op chapters) and grep of `feature/` (no BC-op references).
- Memory cross-check: `project_l4_is_backend_lowering_target` ("the FE-assembly/FE-space cohort stranded at L1 is a hole to close") — REFUTED for the assemble-half on disk.

## Open questions / caveats

- **OQ to file:** `bc-elimination-cohort-l4-disposition` — does the firm-L1 BC-elimination cohort (`eliminate_essential_bc`/`eliminate_rhs`, fed by `essential_dofs`) rise to L4 as a small post-assembly combinator, or carry an explicit no-L4-by-design (setup-stratum) verdict? It is the BC-half analog of the assemble-half closed at c068. **This is NOT a brand-new question — it is the live form of the existing c069 sibling-deferral** recorded at `L4/fe_assemble.md:119` and `L4-L3/fe-assemble-fold-dissolution.md:127` ("the rank-3/4 c069 candidates, gated on primitive-L4-presence per the planner OQ"). Filing this OQ promotes that deferral into the tracked plan (provenance: the c069 deferral note). (One observation per invocation — I surface this; abstractor/harvester resolves.)
- **Caveat on "complete" for the 5 pipelines:** several pipelines carry opaque-library obstructions inside their L4 caps (eigsolve eigen-iteration, transient/driven integrator step). Those are *dispositioned* obstructions absorbed by firm combinators (`fold_solve` quantifies over the opaque step; `eigsolve` marks the `sequential-obstruction`), NOT undispositioned holes — they do not reduce the L4-reachability verdict. I classified them complete-with-disposition, consistent with CLAUDE.md `obstruction (opaque-library-ownership)` routing.
- **Caveat on boundary-mode:** `seed` here is the feature-root marker (Axis-2 root set), NOT a maturity rung (per the graded-stack scheme §3 split). I treated it as dispositioned (own-readout promotion route stated; not in the 5-pipeline scope). If the demand-gated waveguide-mode output-product is later in-scoped, its missing reduction verb becomes a hole — out of this survey's scope.
- I did not independently re-verify the L0 line ranges cited inside the feature/L4 status lines (e.g. `electrostaticsolver.cpp:21-98`); those are lowering-verifier/citecheck territory. My maturity claims rest on the on-disk `## Status` lines + chapter presence/absence, which is the scope of a cross-layer coverage observation.
