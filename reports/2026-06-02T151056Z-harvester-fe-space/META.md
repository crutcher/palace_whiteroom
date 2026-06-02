---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T16:10:00Z
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
repaired_at: 2026-06-02T16:40:00Z
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

# META: verification of `fe_space` L1 firm operator (cycle-064 D2)

## Critique

### Checks run

**citation-validity — warning.** Verified every load-bearing L0 citation against the `palace-codemap` authoritative line map (`search_text` line numbers, the single authoritative source map). The CORE construction claims are all exact: the variadic ctor `palace/fem/fespace.hpp:66-74` (template at :66, signature :67, forwarding init-list `fespace(&mesh.Get(), std::forward<T>(args)...)` at :68, body close at :74 — confirmed); the ND/H1/RT `ConstructFiniteElementSpaceHierarchy` construction calls at `palace/models/spaceoperator.cpp:47/49/51` (exact, all three); the 2-D L2-curl construction `:72-75` (`L2_FECollection` push_back at :72, `INTEGRAL` map-type arg at :73, hierarchy construction starting :74-75 — confirmed); `GetTrueVSize` `fespace.hpp:96` (exact); prolongation/restriction `fespace.hpp:102-103` (exact); coarse-seed `make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())` `multigrid.hpp:90` inside the `FiniteElementSpaceHierarchy fespaces(` opener at :89 (so `:89-90` is correct); `mesh::AttrToMarker` at `multigrid.hpp:98` (exact); `GetEssentialTrueDofs` at :99 (the report's `:98-99` range starts one line early — the call itself is at :99, immaterial range-start); `ConstructFECollections` body span :22-72 with `pmin` floor :30-33 and basis-type :34-38 (confirmed). The D1→D2 ctor re-anchoring (`:67-75` → `:66-74`) is CORRECT — the report's drift-correction was right. **HOWEVER**, four NON-core supporting citations carry off-by-N drift (all confirmed via `search_text`, not hand-asserted) — see Issues 1-4. These are illustrative-detail citations (the wrapped MFEM member, the non-owned mesh-ref, the two refinement-loop `AddLevel` sites), not the load-bearing construction claim, so the firm-on-positive-structure verdict is not undermined; but they are real and should be corrected. Marking `warning`, not `fail`, because no core/law-bearing citation drifts and the drifts are all ±1/±2 in supporting evidence. No `verified_against:` YAML block in this report (harvester, not lowering-verifier) — that sub-check is n/a.

**surface-or-evidence — pass.** This is a NEW firm operator entry (`new:book/src/L1/fe_space.md`), not a refinement of an existing operator/theme, so the surface-or-evidence gate is about whether new surface is matched by positive evidence. It is: every claim is anchored to a cited positive source site, and the §Evidence block enumerates them. Not a pure rotation_claim; not a refinement-shaped proposal.

**rotation-quality — pass (n/a as a rotation check).** This entry is an L1 operator formalization, not a cross-layer rotation proposal; the L1>L0 rotation `fe-space-construction-rotation` is forward-referenced to D3, not authored here. The in-entry "typed-object-construction view of the mutation rotation" is a faithful L1 framing (Palace's `FiniteElementSpace` constructed once, consumed read-only → pure `(mesh, collection) → space`), which is the genuine mutation→pure-function shift L1 is for, not a 1:1 rename. The coarse-seed identity law (law 4) is a legitimate in-line non-adjacent annotation of the `fe_space`↔`fe_space_hierarchy` relation, consistent with the in-line-identity-rotation convention.

**variant-axis-coverage — pass.** The de-Rham family is the declared variant axis and ALL FOUR points are witnessed positively at construction sites: H1 (`H1_FECollection`, `spaceoperator.cpp:49`), H(curl) (`ND_FECollection`, `:47`), H(div) (`RT_FECollection`, `:51`), L2 (`L2_FECollection`, `:72`). Verified each via `search_text`. The variant-uniformity claim (the construction body does not branch on family; family is an attribute of the `collection` argument) is correct — the three `spaceoperator.cpp:47/49/51` calls differ only in the template parameter. The 2-D L2-curl special case is correctly captured as the L2 row, not a separate axis. The collection-order-schedule (`ConstructFECollections`) is explicitly scoped OUT to the deferred `fe_collection` sibling — a clean scope-out, not a hidden branch. No uncovered combination.

**cross-reference-integrity — warning.** All internal `[link]` references in the new chapter resolve to on-disk targets (`fe_assemble.md`, `weak_form_term.md`, `eliminate_essential_bc.md`, `eliminate_rhs.md` all exist under `book/src/L1/`; `book/src/L0/fespace-file.md` exists). The L1>L0 `fe-space-construction-rotation` is correctly left as a plain-text forward-reference (theme not yet on disk — D3), consistent with the rough-in-forward-reference-must-be-plain-text convention. The `new:`/`edit:`/SUMMARY proposed-changes are fence-balanced and the `## Status` apparatus is INSIDE the `new:` fence (no fence-truncation defect). The SUMMARY anchor `- [weak_form_term](./L1/weak_form_term.md)` (SUMMARY.md:115) and the index dep-map `weak_form_term` row anchor are unique and resolvable. **The warning is the COHORT-PLACEMENT CONFLICT** (Issue 5): D2's `edit:book/src/L1/index.md` cohort bullet anchors on the `weak_form_term` bullet, which is the LAST bullet of the existing `**Firm (FE-assembly sub-spine — 4 ...)**` subsection — so D2's `fe_space` bullet lands UNDER the FE-assembly sub-spine, and D2's prose says "FE-assembly sub-spine grows 4→5". But wave-mate D4 (`layer-intro-author-fe-space-subspine`, the framing/count owner) creates a SEPARATE "FE-space sub-spine — 1" subsection (fe_space CONSTRUCTS the space; FE-assembly FOLDS over it — distinct cohorts). These placements conflict; integrator reconciliation required.

**edge-label-fidelity — pass.** The only edge label is the L1>L0 `fe-space-construction-rotation` forward-reference; the prose discussing it ("how the typed `(mesh, collection) → FiniteElementSpace[N]` construction rewrites into the L0 variadic ctor ... and the `ConstructFiniteElementSpaceHierarchy` coarse-seed") is the correct L1→L0 direction (high→low), consistent with the layers-defined-high→low invariant. No mislabeled edge.

**plan-kind-consistency — pass.** Declared kind is `firm` with the `firm-on-positive-structure` qualifier. Content matches: a fully-specified signature, a witnessed variant axis, four syntactic-identity laws on positive source, a complete §Evidence block, no rough-in placeholders in the body. The no-dedicated-test caveat is correctly handled as non-gating per the `fe_assemble`/`apply_linop` precedent (laws are syntactic identities on positive construction, not convergence/iteration semantics — the firm-on-positive-structure escape applies legitimately). The MFEM-owned-read-as-given framing (dof/vdof numbering, ordering, conformity, prolongation/restriction as thin `Get().X()` forwarders) is the CORRECT non-mirror call: minting a `dof_map` entry would be the redirect's identity-in-named-terms smell, and treating the dof structure as an opaque property of the typed value (the axis `N`) is the right move. The MPI/Par*/partitioning out-of-scope flag (single-rank reading of `loc_attr`/`loc_bdr_attr`) is appropriate per CLAUDE.md scope. The no-concept-page judgment is sound (no cross-cutting abstraction distinct from the operator entry exists until the four re-anchors land; deferred-candidate, not a blocker — correctly NOT filed in the OQ ledger as a blocker).

**skill-uptake-survey — pass.** The report references `tools/citecheck/citecheck.py --anchor` for self-verification of all load-bearing L0 citations (the `verify-citation-range` mechanical realization) and documents the two drift-corrections caught pre-emit. That is the expected skill-uptake for a harvester emitting a citation-dense firm entry. Pure telemetry surface; non-blocking.

### Issues found

**Issue 1 (citation-validity, warning) — `fe_space.md` §Evidence, "wrapped `mfem::ParFiniteElementSpace fespace` (`:24`)".** The wrapped MFEM member is at `palace/fem/fespace.hpp:25`, not :24 (DRIFT +1; confirmed `search_text` → `mfem::ParFiniteElementSpace fespace;` at line 25). Supporting-detail citation, not load-bearing.

**Issue 2 (citation-validity, warning) — `fe_space.md` §Signature, "`palace/fem/fespace.hpp:27` holds the non-owned `Mesh &mesh`".** The `Mesh &mesh;` member is at `fespace.hpp:28`, not :27 (DRIFT +1; confirmed `search_text` → `Mesh &mesh;` at line 28). The :27 line is the comment `// Reference to the underlying mesh object (not owned).`. Supporting-detail citation.

**Issue 3 (citation-validity, warning) — `fe_space.md` law 3 + §Evidence, h-refinement `AddLevel` at "`multigrid.hpp:104`".** The h-refinement `fespaces.AddLevel(std::make_unique<FiniteElementSpace>(*mesh[l], fecs[0].get()))` is at `multigrid.hpp:106`, not :104 (DRIFT +2; confirmed `search_text`). Appears in law 3 (mesh/collection separability) and the §Evidence `multigrid.hpp:78-126` breakdown. Illustrative of the h-axis, not the core construction claim.

**Issue 4 (citation-validity, warning) — `fe_space.md` law 3 + §Evidence, p-refinement `AddLevel` at "`multigrid.hpp:118`".** The p-refinement `fespaces.AddLevel(std::make_unique<FiniteElementSpace>(*mesh.back(), fecs[l].get()))` is at `multigrid.hpp:117`, not :118 (DRIFT −1; confirmed `search_text`). Same two locations as Issue 3. Illustrative of the p-axis.

**Issue 5 (cross-reference-integrity, warning) — COHORT-PLACEMENT CONFLICT; `edit:book/src/L1/index.md` cohort bullet (CYCLE.md:252-253) + prose (CYCLE.md:256, 336).** D2's cohort-bullet `edit:` anchors immediately after the existing `weak_form_term` bullet (the last bullet of the `**Firm (FE-assembly sub-spine — 4 ...)**` subsection at index.md:71-76), which places the new `fe_space` bullet UNDER the FE-assembly sub-spine. D2's prose reinforces this: "the FE-assembly sub-spine is **5** members (was 4)" (CYCLE.md:256) and "the FE-assembly sub-spine grows 4→5" (CYCLE.md:336). But wave-mate D4 (`layer-intro-author-fe-space-subspine`, the explicit count/framing owner this cycle — D2 itself defers the consolidated tally to D4 at CYCLE.md:256) creates a SEPARATE "FE-space sub-spine — 1" subsection on the rationale that `fe_space` CONSTRUCTS the space (distinct from FE-assembly, which FOLDS over it). **Reconciliation the integrator must handle:** D2's cohort bullet should land under D4's NEW "FE-space sub-spine" subsection, NOT appended after `weak_form_term` in the FE-assembly subsection; and the "FE-assembly sub-spine grows 4→5" framing is wrong under D4's authoritative cohort structure (FE-assembly stays 4; FE-space is a new sub-spine of 1). D4's framing is the authoritative cohort structure (the framing owner). Note: D2 itself flags this dependency softly — it defers the absolute tally to D4 and brackets its own count language as provisional ("D4 authors that absolute total") — so this is a known coordination seam, not a silent error. **The dep-map ROW (the separate `edit:` at CYCLE.md:260-262, appended after the `weak_form_term` dep-map row at index.md:118) is UNAFFECTED** — the dep-map table is a flat per-operator table with no sub-spine subsectioning, so `fe_space`'s dep-map row sits correctly regardless of cohort-subsection placement; only the prose cohort BULLET needs to move. The SUMMARY.md `edit:` is also unaffected (flat list).

**Issue 6 (cross-reference-integrity, informational — not blocking) — pre-existing index.md count line.** The `## Vocabulary cohort` lead (index.md:31) currently reads "31 firm grand total ... FE-assembly sub-spine adds 4". Once both D2 (`fe_space`) and D4 (the new FE-space sub-spine subsection + consolidated tally) land, this line needs the grand-total bump to 32 and the new-sub-spine accounting. D2 correctly DEFERS this to D4 (the count-owner) and does NOT touch the count line itself — so this is not a D2 defect, but flagging it so the integrator confirms D4's count `edit:` actually lands the 31→32 bump and the FE-space sub-spine line (otherwise the count line goes stale after D2 applies). No action on D2.

---

## Repair

### Fixes attempted

- **Finding (Issue 1, citation-validity)**: wrapped `mfem::ParFiniteElementSpace fespace` member cited `fespace.hpp:24`, actual `:25` (DRIFT +1).
  - **Decision**: repaired
  - **Action**: re-verified via `palace-codemap` `read_range fespace.hpp:23-29` (line 25 = `mfem::ParFiniteElementSpace fespace;`). Fixed the §Evidence occurrence inside the `new:book/src/L1/fe_space.md` block (the only place it reaches the artifact) — `(:24)` → `(:25)`.

- **Finding (Issue 2, citation-validity)**: non-owned `Mesh &mesh` member cited `fespace.hpp:27`, actual `:28` (DRIFT +1; `:27` is the comment line).
  - **Decision**: repaired
  - **Action**: same `read_range` confirmed line 28 = `Mesh &mesh;`. Fixed both artifact-bound occurrences in the `new:` block — §Signature shape-contract bullet (`:27` → `:28`) and §Evidence (`:27` → `:28`).

- **Finding (Issue 3, citation-validity)**: h-refinement `AddLevel` cited `multigrid.hpp:104`, actual `:106` (DRIFT +2).
  - **Decision**: repaired
  - **Action**: re-verified via `read_range multigrid.hpp:102-120` (line 106 = the h-refinement `fespaces.AddLevel(...*mesh[l]...)`). Fixed all three artifact-bound occurrences — §Context (`:104,118` → `:106,117`), law 3 (`:104` → `:106`), §Evidence (`:104` → `:106`).

- **Finding (Issue 4, citation-validity)**: p-refinement `AddLevel` cited `multigrid.hpp:118`, actual `:117` (DRIFT −1).
  - **Decision**: repaired
  - **Action**: same `read_range` confirmed line 117 = the p-refinement `fespaces.AddLevel(...*mesh.back()...)`. Fixed all three artifact-bound occurrences alongside Issue 3 (§Context, law 3, §Evidence) — `:118` → `:117`.

- **Finding (Ctor range `fespace.hpp:66-74`)**: critic confirmed ALREADY CORRECT (D1→D2 re-anchoring was right; `:66-74` is the variadic ctor, `:67-75` is D3's wrong range, not D2's).
  - **Decision**: not-needed
  - **Action**: no change — left `:66-74` untouched everywhere.

- **Finding (Issue 5, cross-reference-integrity, load-bearing)**: D2's prose cohort bullet anchors after `weak_form_term`, landing `fe_space` UNDER the FE-assembly sub-spine and asserting "FE-assembly sub-spine grows 4→5"; conflicts with wave-mate D4's authoritative SEPARATE "FE-space sub-spine — 1" subsection (`fe_space` CONSTRUCTS the space; FE-assembly FOLDS over it).
  - **Decision**: repaired
  - **Action**: Verified on disk that the FE-assembly subsection (`book/src/L1/index.md:71-76`) exists and ends at the `eliminate_rhs` bullet, while D4's "FE-space sub-spine" subsection is NOT yet on disk (it lives in D4's proposed-changes). Because re-anchoring D2's bullet into a subsection that isn't on disk is fragile, took the critic-sanctioned **alternative**: DROPPED D2's separate prose cohort `edit:book/src/L1/index.md` block entirely and replaced it with an **INTEGRATOR-NOTE** recording that D4's FE-space sub-spine subsection is the authoritative home for the `fe_space` cohort description (D4's subsection already describes `fe_space`). Also CORRECTED the retracted framing in two report-prose spots: the dual-registration note (removed the "FE-assembly sub-spine is 5 / grand total 32" assertion) and the §Open-questions "Layer intro refresh" caveat (now states FE-assembly STAYS 4, FE-space is a new sub-spine of 1, grand total 31→32). D2's dep-map TABLE row + SUMMARY.md line are UNAFFECTED and left to land (flat structures, no sub-spine subsectioning) — confirmed unchanged.

### Unrepairable findings

None. Both flagged checks (citation-validity, cross-reference-integrity) were repaired mechanically/surgically within repair authority: the four citation drifts are simple line-offset corrections verified against the authoritative codemap, and the cohort-placement conflict was resolved by dropping a duplicate prose bullet + recording an integrator-note (no substantive authoring — D4 owns the authoritative cohort prose).

## Suggested resolution

`ready`. Notes for the integrator:

- **Apply order (load-bearing):** D4's `book/src/L1/index.md` edit (which creates the "FE-space sub-spine — 1" subsection + the consolidated 31→32 tally) is the AUTHORITATIVE home for the `fe_space` cohort prose. D2 contributes NO cohort bullet to `index.md` — only its dep-map TABLE row (append after the `weak_form_term` dep-map row) and its `SUMMARY.md` line. There is no longer a cross-block anchor dependency from D2 onto D4's subsection, so D2 and D4 may apply in either order; just confirm D4's count `edit:` lands the FE-space sub-spine line and the 31→32 grand-total bump (Issue 6) so the `## Vocabulary cohort` lead does not go stale.
- All four supporting-citation drifts are corrected in the `new:book/src/L1/fe_space.md` body; the load-bearing construction citations (`fespace.hpp:66-74`, `spaceoperator.cpp:47/49/51`, `:72-75`, `multigrid.hpp:89-90`) were already exact and are untouched.
