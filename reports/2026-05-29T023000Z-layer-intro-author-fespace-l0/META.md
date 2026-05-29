---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T03:10:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T03:25:00Z
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

# META: verification of L0 anchor — `palace/fem/fespace.{hpp,cpp}`

## Critique

### Checks run

**citation-validity (DOMINANT) — pass.** I independently re-read a wide spot-check sample of the
cited ranges via `palace-codemap` `read_range` (NOT trusting the report's own self-verification, per
the `verify-citation-range` audit sub-case). Verified: the header class/struct boundaries
(`FiniteElementSpace` opens at `fespace.hpp:21`, doc comment `18-20`; `FiniteElementSpaceHierarchy`
opens after `fespace.hpp:194`, doc comment `196-198`, body `200-286`); the member layout
(`mfem::ParFiniteElementSpace fespace` @24, `Mesh &mesh` @27, the four libCEED caches @31-32, `tx,lx,ly`
@35); the two interp predicates with their load-bearing comments (`HasUniqueInterpRestriction` 40-48
incl. the "native (not lexicographic)" comment 42-43; `HasUniqueInterpRangeRestriction` 50-61 incl.
the "special DofTransformation" comment 51-52); the variadic constructor (67-75) and destructor (76);
the MFEM-forwarding accessor block (93-103), where `GetVDim/GetVSize/GlobalVSize/GetTrueVSize` and
`GetProlongationMatrix/GetRestrictionMatrix` are each verbatim `return Get().X()`. On the .cpp side I
re-read the dominant regions in full: the two lazy caches (`GetCeedBasis` 15-25, `GetCeedElemRestriction`
28-41); both interp-specialized restrictions (`GetInterpCeedElemRestriction` 44-65 with the
`BuildCeedElemRestriction(...,true,false)` @62; `GetInterpRangeCeedElemRestriction` 67-88 with
`(...,true,true)` @83); `ResetCeedObjects` 90-132 (four destroy-loops 92-119, four clears 121-124,
per-`Ceed` re-seed 125-131); `BuildCeedBasis` 134-159 (nodal-FE selection, `DefaultIntegrationOrder::Get`
@147, `ceed::InitBasis` @158, `fespace.GetVDim()` @157); `BuildCeedElemRestriction` 162-171 (`use_bdr`
@166, `ceed::InitRestriction` @167); the full `BuildDiscreteInterpolator` 173-238 four-way dispatch; and
`BuildProlongationAtLevel` 240-261. The `BuildDiscreteInterpolator` dispatch is the most-detailed claim
and it is faithful: VALUE→H_CURL gradient (191-198), H_CURL→H_DIV 3-D curl (199-206), H_CURL→INTEGRAL
2-D scalar-curl-via-MFEM-native-assembly (207-220, comment 213-214 confirmed verbatim: "libCEED does
not support partial assembly for this operator type"), H_DIV→INTEGRAL divergence (221-228),
`MFEM_ABORT` else (230-233). `BuildProlongationAtLevel`'s different-mesh `TransferOperator` (245-251)
vs same-mesh `IdentityInterpolator` p-refinement (252-258) branches are correct. Test citations
confirmed: `test-libceed.cpp:12` `#include "fem/fespace.hpp"`; the prolongation/gradient/curl SECTIONs
(1169-1222) construct `FiniteElementSpace` + `DiscreteLinearOperator` and assert against
`mfem::PRefinementTransferOperator` / `mfem::DiscreteLinearOperator`; `test-boundarymodeoperator.cpp:75-92`
constructs `FiniteElementSpace` directly and exercises `Get().GetEssentialTrueDofs` + `GetTrueVSize`.
Accuracy is high; the only deviations found are a handful of sub-±2-line off-by-ones on interior
anchor points (see Issues), none of which misrepresents the construct at the cited location. Pass.

**surface-or-evidence — pass.** This is an L0 source-anchor chapter (descriptive map of a source
range), not a refinement-shaped proposal that modifies operator/theme surface — so the
modify-surface-AND-rotation-claim disjunct does not strictly apply. The one load-bearing *empirical*
framing claim — that `fespace.{hpp,cpp}` does NOT define dof/vdof numbering, byNODES/byVDIM ordering,
or element-to-dof tables (those forward to MFEM) — I independently re-ran via `search_text`. Confirmed:
`byNODES`, `byVDIM`, and `Ordering` appear **nowhere** in either file; `vdof`/`VDofs`/
`GetElementToDofTable` are absent; the only `DofTransformation` hits (`fespace.hpp:54` comment, `:60`
`dof_trans` lookup) are inside the libCEED interp-range predicate, NOT a dof-numbering definition. The
framing is true to source. Pass.

**rotation-quality — pass (not a rotation claim).** An L0 anchor is a source-range map, not an
algebraic/structural/reduction rotation between layers. The chapter stays descriptive throughout: it
narrates what the source does and defers semantic lifting to explicitly-labelled "Notes for higher
layers" (which speak in the conditional — "At L1 ...", "At L2 these lift as ..."). No invented
semantics; the lift notes are framed as forward-looking, not as claims about the L0 surface. Pass.

**variant-axis-coverage — pass (n/a to L0 anchor).** Not applicable to a source-range map. The
chapter does correctly *surface* the orthogonal variant structure of the interpolator family (the
plain / interp / interp-range restriction split; the 2-D-scalar-curl native-assembly branch) as L0
observations, and flags the one load-bearing variant — but as description, not as a variant-axis
obligation on a constructed operator. Pass.

**cross-reference-integrity — pass.** All six adjacent cross-ref targets resolve to existing files in
`book/src/L0/` (`fem-bilinearform-file`, `fem-libceed-operator-file`, `linalg-rap-file`,
`par-types-single-rank-reading`, `transparent-vs-load-bearing-tricks`, `preconditioner-classes-overview`),
plus `mutable-workspace-pattern.md` (Open-questions ref). `fespace-file.md` is correctly NOT present
(it is the new file being proposed). The deferred libCEED basis/restriction regions
(`fem/libceed/{basis,restriction}.hpp`) and the quadrature/geometric-factor sources are forward-
referenced as **plain text** (not live links), correct since no anchor exists yet. The SUMMARY.md
surgical-insert anchor is correct: `book/src/SUMMARY.md:103` is verbatim
`- [File — palace/fem/libceed/operator.{hpp,cpp}](./L0/fem-libceed-operator-file.md)` and `:104` is the
MPI-collectives bullet; the `[old]`/`[new]` block reproduces both and inserts between them. The flagged
drive-by drift (`fem-libceed-operator-file` is in SUMMARY.md but has no `index.md` "File overviews"
bullet) is confirmed real and is noted in Open questions, NOT silently fixed. Pass.

**edge-label-fidelity — pass (n/a; index cohort bullet).** No L_{n+1}→L_n edge label is carried (this
is an L0 file anchor, not a lowering theme). The index.md change is a "File overviews" cohort bullet;
its `[old]` anchor (the `fem-bilinearform-file` bullet, incl. the `rap.cpp:100` clause) matches the
live index text verbatim, and the inserted prose describes `palace/fem/fespace.{hpp,cpp}` — the file
this chapter is about. No mislabeled edge. Pass.

**plan-kind-consistency — pass.** Three well-formed proposed-changes blocks: (1) a new file
`book/src/L0/fespace-file.md` with complete L0-anchor section shape (header-comment intro, "At a
glance", per-region prose, "Notes for higher layers", "Referenced from", "Evidence (representative)"),
modeled on the cycle-016 `fem-libceed-operator-file` chapter; (2) a `summary-md-surgical-insert`-format
SUMMARY.md insert; (3) an index.md cohort-bullet insert. Content shape matches a firm L0 source-anchor
chapter (citation-dense, descriptive, no speculative operator construction). No direct `book/` write in
the dispatch phase — all mutations are staged as `edit:` blocks for the integrator. Pass.

**skill-uptake-survey — pass.** Both implied skills are referenced: `summary-md-surgical-insert` is
named and its format is used for change #2 (`[anchor-after]`/`[old]`/`[new]`); `verify-citation-range`
is implied by the "Source self-verified (every cited range read via `palace-codemap` `read_range`)"
supporting-evidence block. Telemetry only; non-blocking. Pass.

### Issues found

All issues are MINOR citation-precision off-by-ones. None changes which source construct a reader lands
on; recording for repairer triage and to keep L0-anchor citation hygiene tight (L0 anchors are exactly
where producer-emit drift historically crept in).

1. **MINOR — lazy-interpolator-state pair range is one line short.**
   `book/src/L0/fespace-file.md` "At a glance" (CYCLE.md:74) and Evidence (CYCLE.md:251-252) cite the
   `aux_fespace` + `G` pair as `fespace.hpp:37-38`. Actual: line 37 is the comment, `aux_fespace` is
   line 38, and `mutable std::unique_ptr<Operator> G;` is line **39**. The range `37-38` covers the
   comment and `aux_fespace` but excludes the `G` declaration it is meant to include. Should be
   `37-39` (or `38-39`). Location: file:§"At a glance" + §Evidence.

2. **MINOR — `GetCeedBasis` emplace line and function-end off by one.**
   CYCLE.md:108-111 ("§libCEED basis/restriction caches") and Evidence (CYCLE.md:291) cite the
   freshly-built `emplace(BuildCeedBasis)` at `fespace.cpp:24` and the function as `15-25`. Actual: the
   `return basis_map.emplace(geom, BuildCeedBasis(*this, ceed, geom)).first->second;` is line **25** and
   the function closes at line **26** (`15-26`). The emplace-line citation should read `:25`.

3. **MINOR — `GetInterpCeedElemRestriction` fall-through citation points at the brace, not the statement.**
   CYCLE.md:119-120 ("falls through to the plain `GetCeedElemRestriction` (`fespace.cpp:50`)") and
   Evidence (CYCLE.md:293, "guard 50"). Actual: the `if (!HasUniqueInterpRestriction(fe))` guard is
   line **49**, the opening `{` is line 50, and the fall-through `return GetCeedElemRestriction(...)` is
   line **51**. The guard/fall-through should cite 49/51 rather than 50. (`GetInterpRangeCeed...` has
   the same shape; CYCLE.md:296 "guard 72" — the guard `if` there is line 71, brace 72; same ±1.)

4. **MINOR — `BuildDiscreteInterpolator` return-line citation off by ~2.**
   CYCLE.md:168 ("The constructed `G` is cached and returned (`fespace.cpp:236`)"). Actual: the
   `MFEM_ABORT` else-block occupies through ~236 and the `return *G;` is line **238** (the function
   closes at the same range-end the report cites for the whole function, 173-238). The return-statement
   citation should read `:238`.

5. **MINOR (cosmetic, low confidence) — `GetComm` may not be exercised in the cited
   `test-boundarymodeoperator.cpp:75-92` window.**
   CYCLE.md:320-322 and Evidence list `GetComm` among the accessors exercised at
   `test-boundarymodeoperator.cpp:75-92`. The 75-92 read clearly shows `Get().GetEssentialTrueDofs` and
   `GetTrueVSize`; `GetComm` was not visible in that exact window (it may sit just outside 75-92). Not
   load-bearing — the test-as-semantic-supplement claim stands on the two confirmed accessors — but the
   `GetComm` mention either needs a widened line range or should be dropped from this citation.

6. **MINOR (informational, NOT a defect in this report) — index.md "File overviews" / SUMMARY.md
   drift by one entry, correctly flagged not fixed.**
   Confirmed: `fem-libceed-operator-file` is in `SUMMARY.md:103` but has no bullet in the `index.md`
   "File overviews" cohort. The report flags this in Open questions (CYCLE.md:402-410) and scopes the
   backfill out (one chapter per invocation). Recording here so the integrator sees the critic
   independently confirmed the drift; this is a navigation-completeness gap on a *prior* chapter, not a
   build error and not a fault of the present report. Surfaced for a future index-maintenance pass /
   integrator stub-or-backfill judgment, not for this repairer.

## Repair

All five actionable findings (1-5) are MINOR sub-±2-line citation off-by-ones on interior anchor
points — exactly the in-scope "citation line range off by a small offset" repair shape. Each was
re-verified against source via `palace-codemap` `read_range` (NOT trusting the report's or critic's
asserted lines) before editing, then the pointer was fixed in CYCLE.md. No content authored; all edits
are mechanical pointer corrections. Finding 6 is informational (a prior-chapter navigation gap the
report correctly flagged), explicitly out of this report's scope, and left as-is per the dispatch
instruction.

### Fixes attempted

1. **Finding**: lazy-interpolator-state pair `aux_fespace`+`G` cited `fespace.hpp:37-38`, cutting off the
   `G` declaration.
   - **Decision**: repaired.
   - **Verification**: `read_range hpp:35-41` — line 37 = comment, 38 = `aux_fespace`, **39** =
     `mutable std::unique_ptr<Operator> G;`. Range `37-38` excludes `G`; correct is `37-39`.
   - **Action**: CYCLE.md §"At a glance" (`37-38`→`37-39`) and §Evidence (`37-38`→`37-39`).

2. **Finding**: `GetCeedBasis` emplace cited `fespace.cpp:24`; function cited `15-25`.
   - **Decision**: repaired.
   - **Verification**: `read_range cpp:15-27` — `return basis_map.emplace(geom, BuildCeedBasis(...))...`
     is line **25**; function closing brace is line **26**. Emplace is `:25`, function `15-26`.
   - **Action**: CYCLE.md §"libCEED basis/restriction caches" prose (function `15-25`→`15-26`, emplace
     `:24`→`:25`) and §Evidence (same).

3. **Finding**: `GetInterp*CeedElemRestriction` fall-through cited the opening brace, not the statement
   (`cpp:50`; interp-range Evidence "guard 72").
   - **Decision**: repaired.
   - **Verification**: `read_range cpp:44-52` — guard `if (!HasUniqueInterpRestriction(fe))` is line
     **49**, `{` line 50, `return GetCeedElemRestriction(...)` line **51**. `read_range cpp:67-74` —
     interp-range guard line **71**, `{` line 72, fall-through `return GetInterpCeedElemRestriction(...)`
     line **73**.
   - **Action**: CYCLE.md interp-restriction prose (fall-through `:50`→guard `:49` + fall-through `:51`);
     §Evidence interp (guard `50`→`49`, add fall-through `51`) and interp-range (guard `72`→`71`, add
     fall-through `73`).

4. **Finding**: `BuildDiscreteInterpolator` return cited `fespace.cpp:236`.
   - **Decision**: repaired.
   - **Verification**: `read_range cpp:230-240` — `MFEM_ABORT` else-block runs through ~234, `return *G;`
     is line **238**, function close line 239. Return statement is `:238`.
   - **Action**: CYCLE.md §`BuildDiscreteInterpolator` prose (`:236`→`:238`). (Whole-function range
     `173-238` was already correct.)

5. **Finding**: `GetComm` listed among accessors exercised in `test-boundarymodeoperator.cpp:75-92`, but
   not visible in that window.
   - **Decision**: repaired.
   - **Verification**: `read_range test-boundarymodeoperator.cpp:75-100` — the window exercises
     `Get().GetEssentialTrueDofs` (lines 87-88) and `GetTrueVSize` (line 92); **no `GetComm`** appears in
     75-92 (nor in the widened 75-100). The test-as-semantic-supplement claim stands on the two confirmed
     accessors.
   - **Action**: CYCLE.md §Evidence — dropped `GetComm` from the exercised-accessor list (kept
     `Get().GetEssentialTrueDofs` / `GetTrueVSize`) and removed the now-unused `,186` (`GetComm`
     forwarder) line-ref from the trailing `fespace.hpp:93-103,186` parenthetical → `fespace.hpp:93-103`.

6. **Finding**: index.md / SUMMARY.md one-entry drift (`fem-libceed-operator-file` in SUMMARY but missing
   an index.md "File overviews" bullet).
   - **Decision**: not-needed (out of scope; correctly flagged by the report, not a defect in it).
   - **Rationale**: per dispatch instruction, this is a separate index-maintenance pass on a *prior*
     chapter; the report already flags it in Open questions (CYCLE.md) and the critic independently
     confirmed it. Backfilling it here would author sibling-chapter content beyond repair authority. Left
     as the report flagged it for the integrator's stub-or-backfill judgment.

### Unrepairable findings

None. All eight checks passed at critique; the only deviations were the five mechanical off-by-ones,
all repaired.

## Suggested resolution

`ready`. All 8 checks pass and the five MINOR citation off-by-ones are surgically corrected against
re-verified source lines. Notes for the integrator:
- This is a new-file L0 anchor (`book/src/L0/fespace-file.md`) plus a `summary-md-surgical-insert`
  SUMMARY.md insert and an index.md cohort-bullet insert — all staged as `edit:` blocks, no
  dispatch-phase artifact writes.
- Carry forward the report's Open-questions items: (i) the proposed follow-up L0 anchor for
  `palace/fem/libceed/{basis,restriction}.{hpp,cpp}` (forward-referenced as plain text by both this
  chapter and `fem-libceed-operator-file`); (ii) the prior-chapter index/SUMMARY one-entry drift
  (`fem-libceed-operator-file` lacks an index.md "File overviews" bullet) — a navigation-completeness
  gap, candidate for the integrator's index-maintenance/backfill judgment, not a build error.
