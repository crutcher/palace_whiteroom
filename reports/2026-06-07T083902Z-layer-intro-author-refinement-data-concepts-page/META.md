---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T091500Z
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
repaired_at: 2026-06-07T093000Z
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

# META: verification of concepts/RefinementData record-definition page (cycle-123 D4)

## Critique

### Checks run

**citation-validity — warning.** I re-verified every L0 pinpoint independently against on-disk
source via codemap (`get_symbol_def` + `read_range`), not the producer's chain-of-thought.

- The **corrected struct extent `palace/utils/configfile.hpp:97-154` is CONFIRMED exact**:
  `get_symbol_def` returns `struct RefinementData` `start_line:97, end_line:154`, and the on-disk read
  shows `struct RefinementData` on `:97`, `};` on `:154`. The producer's c122-drift correction
  (`~:96-125`/`:97-119` → `:97-154`) is right. Every per-field hpp pinpoint is exact:
  `tol :101`, `max_it :104`, `max_size :108`, `nonconformal :111`, `max_nc_levels :115`,
  `update_fraction :119` (Dörfler comment `:117-118`), `maximum_imbalance :123`,
  `save_adapt_iterations :127`, `save_adapt_mesh :130`, `uniform_ref_levels :133`,
  `ser_uniform_ref_levels :136`, private box/sphere lists `:140-141` + accessors `:144-150`,
  ctor decls `:152-153`. All eleven JSON-key pinpoints in `configfile.cpp` are also exact
  (`"Tol":321 "MaxIts":322 "MaxSize":323 "Nonconformal":324 "MaxNCLevels":325 "UpdateFraction":326
  "MaximumImbalance":327 "SaveAdaptIterations":328 "SaveAdaptMesh":329 "UniformLevels":332
  "SerialUniformLevels":333`). The consumer-side `basesolver.cpp` cites are exact too
  (`:223-224` θ-binding `ComputeDorflerThreshold(..., refinement.update_fraction)`, `:239`
  `GeneralRefinement(..., refinement.max_nc_levels)`), as is `Nondimensionalize` at
  `configfile.cpp:1535`.
- **However, two range citations are themselves drifted** (see Issues 1 and 2). The producer corrected
  the c122 *hpp* drift but introduced/carried *cpp* range drift: the JSON-ctor extent
  `configfile.cpp:318-377` over-extends the function by +18 lines into the *next* function
  (`ModelData::ModelData`), and the `ParseOptional` parse line `:378` is off-by-one (`:379` on disk).
  These are the load-bearing depends-on `cites-evidence` edge target (the ctor range) and a body/Status
  pinpoint, so they count as a real `warning` rather than cosmetic.

**surface-or-evidence — pass.** This is a record-definition concepts page (`kind: record`), so the
record-definition obligation is the relevant lens, and it is met cleanly. The page defines the **data
shape** only — fields, types, meaning, construction-vs-run-time stratum, and the L0 home (the backing
`struct RefinementData` + the `Refinement` JSON surface) — and explicitly defers behaviour to the
consumer chapters (the `dorfler_mark` θ-use, the AMR fold loop-bound reads). No operator algebra is
restated. It follows the `concepts/FiniteElementSpaceHierarchy.md` / `concepts/config-record.md`
template (kind banner, One-line semantics, Record definition table with stratum + L0-source columns,
L0 source home, See-also, Status). The page IS the definition home being created, not a use-only
description, so the obligation is discharged, not flagged.

**rotation-quality — pass (not applicable).** A record-definition concepts page asserts no
algebraic/structural rotation between layers — it pins a data shape to its L0 home. No rotation claim
to grade.

**variant-axis-coverage — pass (not applicable).** No orthogonal variant axes on a config record. The
single-machine carve-outs (`maximum_imbalance`, `uniform_ref_levels` Par* parallel levels, multi-rank
rebalancing) are explicitly scoped out per CLAUDE.md §Scope and recorded for fidelity — that is correct
scope-out handling, not a hidden branch.

**cross-reference-integrity — warning.** All Markdown `[link]` targets resolve on disk
(`../L1/dorfler_mark.md`, `../L1/flux_recovery_estimate.md`, `../L1-L0/amr-estimate-mark-refine.md`,
`../feature/lifecycle.L4.md`, `../feature/lifecycle.L0.md`, `config-record.md`,
`build-time-vs-run-time-stratification.md`, `FiniteElementSpaceHierarchy.md`). The two consumer edits
target on-disk old-text that matches exactly (dorfler_mark `:249-259`; amr-theme `:112-116`), and the
SUMMARY `[old]` (rotation `:364` / scal `:365`) matches — the alpha insertion of `RefinementData`
between them is correct case-insensitive placement, consistent with the existing mixed-case ordering.
The ≥2-consumer bar is genuinely met (see below). **One issue:** the new page's `reference:` frontmatter
edge `L1/flux_recovery_estimate` is spurious — `flux_recovery_estimate.md` contains no mention of
`RefinementData`/`update_fraction`/`refinement.` (grepped, zero hits); it is not a consumer of this
record. (See Issue 3.) Since `reference` edges are navigational/free in the graded stack — they
constrain neither rank nor liveness — this is a cleanliness `warning`, not a `fail`; the link still
resolves.

**The ≥2-consumer bar judgment.** Genuinely met. Three real consumers, each naming/reading the record:
(1) `dorfler_mark` reads the θ field `update_fraction`; (2) `amr-estimate-mark-refine` names it
`RefineConfig` and reads `fraction`/`tol`/`max_it`/`max_size`/`max_nc_levels`; (3) the `lifecycle.L4`
§3 / `lifecycle.L0` AMR estimate→mark→refine fold reads `refinement.tol`/`max_it`/`update_fraction`/
`max_nc_levels` (verified on-disk: `lifecycle.L0.md:41-42` cites the `while` guard
`err >= refinement.tol`, the mark stage `update_fraction`, the refine `GeneralRefinement(...,
refinement.max_nc_levels)`). The scope discipline is also correct: only `RefineConfig`/`RefinementData`
crosses the bar this dispatch; `AmrCarry` (homed at lifecycle.L4 §3), `Estimator` (open harvester
routing), and `IndexSet[E]` (single-cohort inline) are correctly left below-bar, and
`BoxRefinementData`/`SphereRefinementData` are correctly noted as single-consumer below-bar.

**edge-label-fidelity — pass.** The typed edges match the prose: `depends-on (cites-evidence)` to the
two L0 ranges (ground-truth, rank-terminal), `reference` to the consumer chapters (navigational,
named-by-use, non-blocking). The Well-foundedness note correctly observes the only blocking edges are
to rank-terminal L0 ground truth so `rank(u) ≤ rank(v)` holds, and the consumer edges are `reference`
(do not block on consumers). This is the correct record-page edge topology.

**plan-kind-consistency — pass.** Declared `rank: firm`, `kind: record`; content shape matches — a
firm record-definition with positive-source field-by-field reads, defaults, JSON binding, and a
Status section justifying `firm` (data shape read directly off the positive `struct RefinementData`,
no constructive sub-part, no test-gate on a syntactic-identity claim). No rough-in placeholders.

**skill-uptake-survey — pass.** The producer documents the localization path (codemap `read_range` +
`search_text` + on-disk reads) and the c122-drift correction methodology. No specific skill is
mandated by this page's shape; the citation re-verification is appropriately surfaced.

### Issues found

1. **Ctor range over-extension — `configfile.cpp:318-377` should be `:318-359`** (severity: warning;
   load-bearing — it is the `depends-on (cites-evidence)` edge target). The
   `RefinementData::RefinementData(const json &)` ctor closes at `:359` on disk (`}` on `:359`;
   `get_symbol_def` confirms `start_line:318, end_line:359`). The cited end `:377` falls INSIDE the
   *next* function `ModelData::ModelData` (which opens `:361`); `:377` is
   `export_prerefined_mesh = model.value(...)`, a ModelData field, not RefinementData. The ctor's last
   scalar binding is `:333`; box/sphere parsing runs `:334-357`; close `:359`. Correct extent
   `:318-359`. Occurrences: CYCLE.md frontmatter depends-on edge (line 58), Summary (line 41), body
   "L0 source home" (line 150), Status (line 203), Supporting evidence (line 268).

2. **Off-by-one on the parse-line pinpoint — `configfile.cpp:378` should be `:379`** (severity:
   warning). `refinement = ParseOptional<RefinementData>(model, "Refinement");` is on `:379` on disk
   (`:378` is the prior ModelData binding `partitioning = ...`). Occurrences: Summary (line 45), body
   (lines 155-156), Supporting evidence (line 272).

3. **Spurious `reference` edge `L1/flux_recovery_estimate`** (severity: warning; non-blocking). The new
   page's frontmatter (CYCLE.md line 62) lists `L1/flux_recovery_estimate` as a `reference` edge, but
   that chapter does not name/read `RefinementData` (grep: zero hits for
   `RefinementData|update_fraction|refinement.`). The page's own prose consumer list (lines 84-87,
   168-178) correctly omits it — only the frontmatter edge carries the stale claim (inherited from the
   pre-edit dorfler_mark "≥2 chapters (this verb, flux_recovery_estimate, ...)" text, which this
   dispatch is itself replacing). The link resolves and `reference` edges are free, so this is a
   cleanliness issue, not a fail; the edge should be dropped.

Note (not an issue): all per-field hpp/cpp pinpoints, the `basesolver.cpp:223-224`/`:239` consumer
cites, and `Nondimensionalize` at `configfile.cpp:1535` are exact; the corrected struct extent
`:97-154` is confirmed; the two re-pointed consumers received the corrected `:97-154`; the consumer
old-text and SUMMARY old-text match on-disk exactly; the ≥2-consumer bar is genuinely met.

---

## Repair

### Fixes attempted

- **Finding 1 — ctor range over-extension `configfile.cpp:318-377` → `:318-359`** (critic Issue 1).
  - **Decision**: repaired.
  - **Verification**: codemap `get_symbol_def RefinementData::RefinementData` returns
    `start_line:318, end_line:359`; `ModelData::ModelData` returns `start_line:361, end_line:379`.
    Direct on-disk Read of `reference/palace/palace/utils/configfile.cpp:315-384` confirms the ctor's
    closing `}` is on `:359` and `:375` (`export_prerefined_mesh`) onward belongs to `ModelData`. The
    box/sphere parsing block runs `:334-357` (spheres close `}` at `:357`/`:358`), so the sub-range
    `:334-377` is the same +18 drift.
  - **Action**: rewrote `configfile.cpp:318-377` → `:318-359` in all 5 cited places
    (CYCLE.md frontmatter depends-on edge line 58, Summary line 41, body "L0 source home" line ~149,
    Status line ~202, Supporting evidence line ~267) AND corrected the box/sphere sub-range
    `configfile.cpp:334-377` → `:334-357` in the Record-definition table row (line ~135) — same drift
    class, surgical. This is the load-bearing `depends-on (cites-evidence)` edge target.

- **Finding 2 — parse-line off-by-one `configfile.cpp:378` → `:379`** (critic Issue 2).
  - **Decision**: not-needed (critic error — the report citation is already correct).
  - **Verification**: codemap `search_text "ParseOptional<RefinementData>"` returns
    `line:378`, and direct on-disk Read confirms
    `refinement = ParseOptional<RefinementData>(model, "Refinement");` is on **`:378`**; `:379` is the
    closing `}` of `ModelData::ModelData`, NOT the parse line. The report's existing `:378` (Summary
    line 45, body line ~155, Supporting evidence line ~272) is exact and was left untouched. Applying
    the critic's proposed `:379` would have INTRODUCED a citation error, so no edit was made.

- **Finding 3 — spurious `reference: L1/flux_recovery_estimate` frontmatter edge** (critic Issue 3).
  - **Decision**: repaired.
  - **Verification**: `flux_recovery_estimate.md` names no `RefinementData`/`update_fraction`/
    `refinement.` (critic grepped zero hits); the page's own prose consumer list omits it. `reference`
    edges are navigational/free (constrain neither rank nor liveness), so dropping it is purely a
    fidelity cleanup with no rank/liveness blast radius.
  - **Action**: removed the `- L1/flux_recovery_estimate` line from the new page's `reference:`
    frontmatter (CYCLE.md line 62). The stale mention surviving at line ~222 is inside the
    `[old]:` match block of the `dorfler_mark.md` consumer edit (it must match on-disk to apply, and
    the paired `[new]:` block already drops the stale claim) — correctly left untouched.

### Unrepairable findings

None. All three flagged findings were either mechanically repaired (Findings 1, 3) or were a critic
mis-pinpoint where the report was already correct (Finding 2, not-needed).

## Suggested resolution

`ready`. Integrator notes:

- The corrected ctor extent `configfile.cpp:318-359` is the `depends-on (cites-evidence)` edge target;
  the box/sphere sub-range was corrected to `:334-357` (same +18 drift the critic identified but did
  not separately enumerate — included as part of the same surgical citation fix).
- Finding 2 was a critic mis-pinpoint: `ParseOptional<RefinementData>` is genuinely on `:378`
  (verified via codemap `search_text` + on-disk Read); the report's `:378` was retained. No action by
  the integrator needed — the `checks: citation-validity: warning` value is the critic's and is not
  overridden here, but the repair record documents that one of the two cited drifts (the `:378` one)
  did not exist on disk.
