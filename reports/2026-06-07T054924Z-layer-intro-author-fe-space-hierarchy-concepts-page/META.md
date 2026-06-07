---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T060000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-07T061500Z
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

# META: verification of `FiniteElementSpaceHierarchy` record concepts-page promotion (RE9 grounding)

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` on the report: 22/22 citations in bounds. The load-bearing pinpoints were independently re-verified on disk via palace-codemap `read_range` and `citecheck --anchor`:
- `palace/fem/fespace.hpp:200-286` — `class FiniteElementSpaceHierarchy`; `--anchor 'class FiniteElementSpaceHierarchy'` resolves to line 200 within range. The close-brace `:286` was directly read on disk: line 285 is `}` (last accessor), line 286 is `};` (class close), line 287 blank — so `:286` is the exact class-closing brace, NOT off-by-one. The report's explicit close-brace off-by-one check is correct.
- All sub-line accessor citations verified accurate: `fespaces :203`, `mutable P :204`, `BuildProlongationAtLevel :206`, seed ctor `:210-213`, `AddLevel`=push_back+nullptr `:217-221`, `GetNumLevels :215`, `GetFESpaceAtLevel :223-234`, `GetFinestFESpace :236-247`, `GetProlongationAtLevel :249-255`, `GetProlongationOperators :257-267`, `GetDiscreteInterpolator(s) :269-285`.
- Consumer site: `ksp.cpp` — `GetDiscreteInterpolators(*aux_fespaces) :219`, `GetProlongationOperators() :221` and `:228` all exact.
- Producer fold: `multigrid.hpp:78-126` (`ConstructFiniteElementSpaceHierarchy`), `return fespaces :125` — exact.
- Fan-out consumers: `divfree.cpp:128`, `hcurl.cpp:101`, `errorestimator.cpp:86` all construct `GeometricMultigridSolver` — exact.

The single defect (downgrades to `warning`, not `fail`): the **Summary Part-1 prose** (CYCLE.md:20–21) cites `gmg.cpp:186,193` for "the V-cycle restricts (`Pᵀ`) / prolongs (`P`) over `P[l]`." On disk, `gmg.cpp:186` is `// Compute residual.` and `:193` is a bare `{`; the actual inter-level transfers are `RealMultTranspose(*P[l-1], R[l], X[l-1])` at **:191** (restrict Pᵀ) and `RealMult(*P[l-1], Y[l-1], R[l])` at **:199** (prolong P). The cited lines exist/are in-range (hence the scan passed) but do not anchor the claimed transfer ops. Confined-impact: this is a VERIFY-summary line for Part 1, which lands NO edit; the Part-1 Supporting-evidence block (CYCLE.md:327–333) cites only the accurate `ksp.cpp`/`fespace.hpp` ranges and omits the gmg.cpp pinpoint. No proposed-changes block carries the drifted pin.

**surface-or-evidence — pass.** This is a record-definition concepts-page promotion (the record-definition obligation path), not a refinement of operator/theme surface, so the rotation_claim framing does not apply. The record-definition sub-check is the load-bearing one here and it is satisfied: `FiniteElementSpaceHierarchy` gets a definition home (`concepts/FiniteElementSpaceHierarchy.md`) defining the data shape — fields (`fespaces`, `P`), types, meaning, per-field construction-vs-run-time stratum, and the L0 backing `class` home — with the in-chapter §Record-definition correctly trimmed to a back-link (the "a record lives ONCE" discipline). The page disclaims and does not restate the `AddLevel`-fold algebra or the V-cycle algebra (data-shape-only discipline upheld). The ≥2-consumer-bar judgment is defensible and applied consistently with the `concepts/mesh.md` precedent (producer counts among the ≥2; a `reference`-target record page does not block on consumer maturity, so the rough-in GMG column is a valid 2nd referencing chapter). Noted for the integrator's awareness, not a defect: the count is at the floor (producer + exactly one non-producer consumer), thinner than the mesh precedent which has four (and ≥2 firm non-producer consumers); the judgment still holds under the stated "≥2 consumers, not ≥2 firm consumers" rule.

**rotation-quality — pass.** Not applicable to a record-definition concepts page — it asserts no algebraic/structural/reduction rotation between layers; it defines a data shape. No rotation claim to grade.

**variant-axis-coverage — pass.** No orthogonal variant axes in a record-shape definition. The one variant-adjacent dimension (the auxiliary-space discrete-interpolator path vs. the plain prolongation path) is correctly attributed to the consuming GMG column / `GetDiscreteInterpolators` accessor, not to this record page; the page documents both accessors. Single-machine carve-out (Par* read single-rank, multi-rank transfer out of scope) is flagged once.

**cross-reference-integrity — pass.** All in-page links checked on disk: `L1/fe_space_hierarchy.md`, `L1/fe_space.md`, `concepts/mesh.md`, `concepts/build-time-vs-run-time-stratification.md`, `L1/build_mesh.md`, `L1/divfree-projector.md` all EXIST. The two GMG-column links (`feature/geometric-multigrid-preconditioner.{L4,L1}.md`) and the page's own new file are not yet on disk — this is the legitimate same-cycle sequenced forward-reference (D1→D2): D1's report was inspected and confirmed to author both column files at exactly those paths AND to carry the `depends-on / kind: composes` edge to `L1/fe_space_hierarchy` on both levels (annotated `GROUNDS RE9`), so the links resolve once D1 lands. The Part-1 no-duplicate VERIFY is therefore correct (D1 owns the edge; D2 must not re-author it). All three edit-block `[old]` anchors match on disk exactly (frontmatter `reference` insert at fe_space_hierarchy.md:30 before the `---` close at :31; §Record-definition trim at :120–140; result-line at :106). SUMMARY alpha-position verified: existing anchors at lines 330–331 are consecutive and match; the case-insensitive lowercased-slug sort convention is confirmed against the `DofSet — record definition`/`Mesh — record definition` precedents (both sort on their lowercased form), and `finiteelementspacehierarchy` correctly sorts `fine < fini < firs` between `finest-level-unwrap` and `first-iteration-unrolling`; the display-text `— record definition` suffix matches the convention.

**edge-label-fidelity — pass.** The Part-1 RE9 edge is `GMG → L1/fe_space_hierarchy` (`depends-on (composes)`); the prose discusses exactly that edge (GMG consumes `GetProlongationOperators()` by name). The frontmatter `cites-evidence depends-on` edge points at the L0 backing range and the prose matches. No mislabeled layer edges.

**plan-kind-consistency — pass.** Declared shape is a record-definition concepts-page promotion + a no-edit VERIFY of an inbound edge; content matches (a `kind: record`, `rank: firm` page + an explicit no-author Part-1). No rough-in placeholders sitting under a firm claim; the `firm` rank rests on the positive `class FiniteElementSpaceHierarchy` read.

**skill-uptake-survey — pass (telemetry).** The report cites use of `citecheck`/codemap `read_range` for self-verification and references the `mesh.md`/`sim-state.md` record-page template. No dedicated skill is strongly implied beyond what is referenced. (Drive-by telemetry: the report self-verifies its own close-brace off-by-one by hand via `read_range`; the citecheck `--anchor` path would have settled it mechanically — minor, not blocking.)

### Graded-stack checks

**rank-invariant — pass.** The new page is `rank: firm` with one blocking edge (`cites-evidence depends-on` to the rank-terminal L0 range), so `rank(u) ≤ rank(v)` holds vacuously. The producer/consumer edges are correctly typed `reference` (navigational, free), so the rough-in GMG consumer does NOT constrain the firm record page — correctly reasoned in the report.

**reachability — pass.** The page is reachable as a `reference` target from the firm producer `L1/fe_space_hierarchy` and the GMG column. The Part-1 contribution makes `L1/fe_space_hierarchy` reachable from the GC-root GMG column via the `depends-on` edge (RE9 grounding); the report correctly defers the authoritative RE9-discharge measurement to the c122 linter re-run rather than asserting it here.

### Issues found

1. **[warning, citation-validity] CYCLE.md:20–21 (Summary, Part 1) — gmg.cpp transfer-site drift.** Prose cites `gmg.cpp:186,193` for the V-cycle restrict (`Pᵀ`) / prolong (`P`) over `P[l]`; on disk the restrict is `RealMultTranspose(*P[l-1], …)` at **:191** and the prolong is `RealMult(*P[l-1], …)` at **:199** (line 186 is `// Compute residual.`, line 193 is `{`). The cited lines are in-range (scan passes) but do not back the claimed ops. Impact is confined: this is a no-edit VERIFY-summary line; the corresponding Part-1 Supporting-evidence block (CYCLE.md:327–333) cites only the accurate `ksp.cpp`/`fespace.hpp` ranges and does not carry this pin, and no proposed-changes block uses it. Correction in hand: `gmg.cpp:191` (restrict) / `:199` (prolong), or the inclusive transfer span `gmg.cpp:191,199` (D1's own GMG report cites the broader `gmg.cpp:182-201` for the same V-cycle body).

2. **[note, surface-or-evidence — not a defect] ≥2-consumer count at the floor.** The promotion rests on producer + exactly one non-producer consumer (the rough-in GMG column), versus the `mesh.md` precedent's four (incl. ≥2 firm non-producer consumers). The judgment is valid under the stated "≥2 consumers, not ≥2 firm" rule and the `reference`-target-doesn't-block-on-consumer-maturity reasoning; surfaced only so the integrator is aware the bar is met at its minimum, not as an issue to repair.

## Repair

### Fixes attempted

- **Finding**: [citation-validity, warning] CYCLE.md:20–21 (Summary, Part 1) — `gmg.cpp:186,193` cited for the V-cycle restrict (`Pᵀ`) / prolong (`P`) transfers, but :186 is `// Compute residual.` and :193 is a brace; the actual transfer ops are at :191 / :199.
  - **Decision**: repaired
  - **Action**: Edited the Part-1 Summary VERIFY-summary line (CYCLE.md, "the V-cycle restricts / prolongs over `P[l]`" clause). Replaced the drifted pin `gmg.cpp:186,193` with the verified op-anchored pins `RealMultTranspose(*P[l-1], …)` `gmg.cpp:191` (restrict, Pᵀ) / `RealMult(*P[l-1], …)` `gmg.cpp:199` (prolong, P). This is a small, mechanical citation-offset correction (in-scope: "citation line range off by a small offset") — no content authored.
  - **Verification**: `mcp__palace-codemap__read_range palace/linalg/gmg.cpp:184-201` confirms :186 = `// Compute residual.`, :191 = `RealMultTranspose(*P[l - 1], R[l], X[l - 1]);` (restrict), :199 = `RealMult(*P[l - 1], Y[l - 1], R[l]);` (prolong). Critic correction confirmed exactly.

- **Finding (note, not flagged for repair)**: ≥2-consumer count at the floor — surfaced by the critic as integrator awareness, explicitly "not as an issue to repair." No action.
  - **Decision**: not-needed

### Unrepairable findings

None. The single warning was a mechanical citation-offset fix fully within repair authority; all other checks passed.

## Suggested resolution

`ready`. The lone defect was a drifted VERIFY-summary pinpoint (no-edit line, no proposed-changes block carried it, confined impact) and is now corrected to the codemap-verified `gmg.cpp:191` / `:199` op anchors. Integrator note: the bar-at-floor consumer count (critic Issue 2) is a valid promotion under the "≥2 consumers, not ≥2 firm" rule — no action needed, surfaced for awareness only.
