---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T16:05:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-02T16:20:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of cross-layer fe-space-front-survey (cycle-064 D1)

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` over the whole report: **37 ok, 0 failing** (all citations in-bounds, no path-hygiene issues). Then meaning-anchored the load-bearing pinpoints on-disk + via codemap. Confirmed exact: the `FiniteElementSpace` variadic ctor at `fespace.hpp:67-75` (forwards `&mesh.Get(), args...` into the wrapped `mfem::ParFiniteElementSpace fespace`); `GetTrueVSize` `:96`; prolongation/restriction `:102-103`; MFEM-forwarding dof accessors `:93-103`; libCEED caches `:31-32`; `ConstructFECollections` body `multigrid.hpp:22-73` with switch-coarsening `:60-68`; `ConstructFiniteElementSpaceHierarchy` `:78-126` with `GetEssentialTrueDofs` at `:99/109/120` (all three exact); `spaceoperator.cpp` ND/H1/RT/L2 construct sites `:47/49/51/75` (the planner-`:47-77`-refinement is correct); the 12-site call-site map (`get_call_sites` confirms `spaceoperator.cpp:47/49/51/75`, `curlcurloperator.cpp:36/38`, `laplaceoperator.cpp:36/39`, `boundarymodeoperator.cpp:137/139/141/143` exactly). Artifact anchors (`fespace-file.md:165-169` de-Rham, `fe_assemble.md:67` opaque-`N`, `eliminate_essential_bc.md:56/67` `DofSet`) all anchor-verified for meaning. **One off-by-one drift:** the report cites `multigrid.hpp:97` for `dbc_marker = mesh::AttrToMarker(...)` (CYCLE.md §1 ~line 56–57, §2 line 98, supporting-evidence line 196); `--anchor 'AttrToMarker'` resolves the literal at **line 98** (`[DRIFT] +1`, suggested `:98`). Anchor-valid, low-severity drift (the +1 cited line is `: 0;`, the AttrToMarker call is one line below). Per the cycle directive this is a low-severity drift, not a fail — hence `warning`, not `pass`. (A few sub-anchor ranges over-extend by a blank/comment line — `ConstructFECollections` cited `:22-75` for a body that closes at `:73`; `pmin :30-34`; `basis :34-39`; these are bounded over-reaches that still enclose the cited construct, not drifts.)

**surface-or-evidence — pass.** Observation-only survey; no operator/theme surface is modified and no rotation_claim is asserted, so this is pure scoping/evidence work (allowed). The 3-way partition (in-scope: `(mesh, FECollection)→FiniteElementSpace` construction + typed identity + de-Rham family + essential-dof *shape*; MFEM-owned-read-as-given: dof/vdof numbering, ordering, conformity, prolongation/restriction; out-of-scope: MPI/`Par*`, mesh partitioning, libCEED basis/restriction caches) is sound and each bucket is evidence-backed — in-scope to the fespace.hpp ctor + multigrid.hpp schedule, MFEM-owned to the thin `return Get().X()` forwarding accessors `:93-103`, out-of-scope to `mesh.hpp` partitioning fields + the existing L0 transparent-cache classification. The partition matches CLAUDE.md §Scope (Par*-single-rank, MPI/partitioning out, transparent caches noted not lifted).

**rotation-quality — pass (n/a).** Not applicable to an observation-only front-scoping survey — no algebraic/structural rotation is asserted (the survey *recommends* a future `fe-space-construction-rotation` L1>L0 theme but does not author one).

**variant-axis-coverage — pass.** The de-Rham family variant axis (H1/H(curl)-ND/H(div)-RT/L2) is explicitly enumerated and made the recommended `fe_space` collection variant axis; the basis-type (GaussLobatto/Legendre/IntegratedGLL-LOR) and coarsening (LINEAR/LOG) sub-axes are named and scoped onto `fe_collection`/hierarchy follow-ons rather than hidden; the 2-D L2-curl INTEGRAL special case is explicitly flagged (OQ caveat). No hidden branches — the survey's job is precisely to enumerate these, and it does.

**cross-reference-integrity — pass.** All referenced files resolve on-disk (`fespace.hpp`, `multigrid.hpp`, `mesh.hpp`, the four spaceoperator/curlcurl/laplace/boundarymode sources, `L0/fespace-file.md`, the four firm L1 entries). No new firm-status claim and no proposed-changes fence (observation-only), so the firm-body-inside-fence build-readiness guard does not apply. Forward-references to not-yet-existing `book/src/L1/fe_space.md` / `fe_collection` / `fe-space-construction-rotation` are correctly framed as wave-2 dispatch scope, not live links.

**edge-label-fidelity — pass (n/a).** No edge label asserted; the survey discusses the prospective L1>L0 edge only as a future-authorable theme.

**plan-kind-consistency — pass.** Declared observation/survey kind matches content: a 3-way partition + fan-out pick-list + granularity verdict + opaque-parameter inventory, with an explicit empty proposed-changes block and "no `book/` mutation" statement. No firm/rough-in placeholders mis-tagged. Consistent.

**skill-uptake-survey — warning.** Telemetry only (non-blocking). The survey's shape implies two relevant skills that go unreferenced: `classify-variant-axis` (the de-Rham/basis/coarsening axis enumeration is exactly that skill's domain) and `verify-citation-range` / `tools/citecheck` (a producer self-check would likely have caught the `:97`→`:98` AttrToMarker drift before dispatch). Surfacing this as uptake signal, not a defect in the report.

### Issues found

1. **`multigrid.hpp:97` → `:98` off-by-one (AttrToMarker), low severity, recurs 3×.** CYCLE.md §1 (lines ~56–57), §2 (line 98), and Supporting-evidence (line 196) all cite `multigrid.hpp:97` for the `dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr)` statement. `citecheck --anchor 'AttrToMarker'` places the literal at line **98** (`+1 outside range`); line 97 is the `: 0;` tail of the preceding `bdr_attr_max` ternary. Anchor-valid drift — repair is the mechanical `:97`→`:98` substitution at all three occurrences. (`GetEssentialTrueDofs :99/109/120` immediately below is exact, so this is an isolated single-line slip, not a systemic frame-shift.)

2. **Minor sub-anchor range over-extension (cosmetic, optional).** `ConstructFECollections` is cited `multigrid.hpp:22-75` but the function body closes at `:73` (`:74` blank, `:75` is the next comment); `spaceoperator.cpp:45-89` ends the ctor at `:88`. These over-reach by a blank/comment line and still enclose the cited construct — not drifts, flagged only for tightening if the repairer is already touching the supporting-evidence block.

3. **skill-uptake telemetry (non-blocking).** No `classify-variant-axis` or citation-range/`citecheck` skill invocation referenced despite the survey's variant-axis-enumeration shape and its line-number-load-bearing citations; the unreferenced citation self-check is the plausible upstream of issue (1).

### Notes on substantive soundness (not defects)

The granularity verdict (ONE `fe_space` entry; NOT a `fe_space`+`fe_collection`+`dof_map` split) is well-grounded on the anti-mirror / identity-in-named-terms-smell reasoning — the dof-map/ordering/conformity is MFEM-owned-read-as-given and splitting it would author a thin mirror of an opaque MFEM structure, which the vocabulary-shift redirect explicitly warns against. The `fe_collection`-as-borderline-second-entry and `fe_space_hierarchy`-deferred dispositions are consistent with the foundation-solidity ranking weight and the sibling-pull-gate convention. The opaque-parameter inventory (4 firm entries — `fe_assemble`/`weak_form_term`/`eliminate_essential_bc`/`eliminate_rhs` — taking `space`/`N`/`DofSet` opaquely) is accurate against the cited anchors. These are correct as written; no repair implied.

---

## Repair

### Fixes attempted

- **Finding**: citation-validity warning — `multigrid.hpp:97` cited for `dbc_marker = mesh::AttrToMarker(...)`; literal resolves to line **98** (`[DRIFT] +1`), recurs 3×.
  - **Decision**: repaired
  - **Action**: substituted `:97`→`:98` at all three occurrences in CYCLE.md — §1 (the essential-true-dof bullet, `... *dbc_attr)`, `multigrid.hpp:98`), §2 (pick #3, `GetEssentialTrueDofs ∘ AttrToMarker, multigrid.hpp:98-99`), and the Supporting-evidence block (`dbc_marker = AttrToMarker` `:98`). Confirmed on-disk via `palace-codemap search_text 'AttrToMarker'` over `**/multigrid.hpp` → single hit at line 98 (`dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr);`). This is the in-scope "citation line range off by a small offset" repair; an isolated single-line slip (the adjacent `GetEssentialTrueDofs :99/109/120` are exact), not a systemic frame-shift.

- **Finding**: cosmetic sub-anchor range over-extension (critic issue 2, optional) — `ConstructFECollections` cited `:22-75` (body closes `:73`); `spaceoperator.cpp:45-89` (ctor ends `:88`).
  - **Decision**: not-needed
  - **Rationale**: critic explicitly flagged these as anchor-valid, bounded over-reaches (still enclose the cited construct), not drifts. On an observation-only survey whose citations inform the survey record/OQs rather than artifact content, tightening these adds no accuracy value and risks needless churn on an append-only-after-integration record. Left as-is per critic's "else leave (anchor-valid)" disposition.

- **Finding**: skill-uptake-survey warning — `classify-variant-axis` / `verify-citation-range`+`citecheck` unreferenced.
  - **Decision**: not-needed
  - **Rationale**: telemetry-only, non-blocking by the critic's own framing. Not a defect in the report and not a repairable surface — it is uptake signal for the meta-phase, not a content fix.

### Unrepairable findings

None. The single substantive finding (the +1 citation drift) was a mechanical line-range correction fully inside repair authority; the other two warnings are non-defect/optional.

## Suggested resolution

`ready`. Integrator notes: this is an observation-only DISPATCH-phase survey with an explicitly empty proposed-changes block — no `book/` mutation to apply. Its value to the integrator is (i) the granularity verdict (ONE `fe_space` L1 entry, NOT a `fe_space`+`fe_collection`+`dof_map` split) and (ii) the wave-2 dispatch scope + the two OQ-ledger items (`essential_dofs` MFEM-boundary straddle; `fe_collection` self-standing-laws deferral). The skill-uptake telemetry (`classify-variant-axis` / `citecheck` self-check non-uptake) is a meta-phase signal, surface it to the friction window.
