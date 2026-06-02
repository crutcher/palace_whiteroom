---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T17:05:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-02T17:20:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of L1>L0 theme — fe-collection-construction-rotation

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing pinpoint was verified against the on-disk file (per the dispatch caution; codemap NOT used). The actual file path is `reference/palace/palace/fem/multigrid.hpp` (the report's `inputs:` block uses the correct `palace/palace/...` form on line 7, while the body citations use the `reference/`-relative `palace/fem/multigrid.hpp` convention — both are the project-standard relative-to-`reference/` form, no defect). Confirmed exactly:
  - `ConstructFECollections` signature at `:23-26`; template return `std::vector<std::unique_ptr<FECollection>>`.
  - `pmin` `constexpr` (`is_base_of<H1...> || is_base_of<ND...> ? 1 : 0`) at `:30-33`; `MFEM_VERIFY(p >= pmin, ...)` at `:34`. ✓
  - Basis selection `b1 = GaussLobatto`, `b2 = GaussLegendre`, `if (mat_lor) b2 = IntegratedGLL` at `:35-39`. ✓
  - Build loop `for (l=0; l < max(1, mg_max_levels); l++)` at `:44`; ctor branch `if constexpr (is_base_of<ND...> || is_base_of<RT...>)` 4-arg `:46-49` vs 3-arg + `MFEM_CONTRACT_VAR(b2)` `:51-54`; floor `break` at `:56-59`. ✓ (The report's "ctor branch :44-55" / "build loop :44-69" framings are correct.)
  - Coarsening `switch` `LINEAR: p--` / `LOGARITHMIC: p = (p+pmin)/2` at `:60-68`. ✓
  - `std::reverse(fecs.begin(), fecs.end())` at `:70`; `return fecs;` at `:72`; closing `}` at `:73`. ✓ — the report's correction of the stale prior `:22-75` close (flagged in caveats) is itself accurate.
  - Enum `enum class MultigridCoarsening : char { LINEAR, LOGARITHMIC }` at `labels.hpp:114-119`. ✓
  - Default `MultigridCoarsening mg_coarsening = MultigridCoarsening::LOGARITHMIC` at `configfile.hpp:918`. ✓
  - De-Rham instantiation sites `spaceoperator.cpp:47/49/51` (ND/H1/RT `ConstructFiniteElementSpaceHierarchy<...>`) — verified (47 ND, 49 H1, 51 RT). ✓
  - Consumer anchors `multigrid.hpp:90` (coarse-seed `fecs[0].get()`) and `:117` (p-refinement `AddLevel` per `fecs[l].get()`) — verified. ✓
  No `verified_against:` YAML round-trip sub-check applies: the report carries a `## Verified-against` prose section, not a fenced/indented `verified_against:` YAML block. No drift, no off-by-one.

**surface-or-evidence — pass.** This is a NEW L1>L0 theme entry (not a refinement of an existing operator/theme surface), so it introduces surface text in full and is backed by the read-in-full positive body. The surface-or-evidence dichotomy is satisfied trivially for net-new firm content; the `firm` claim is grounded in positive source, not a bare rotation_claim.

**rotation-quality — pass.** The L1→L0 is a genuine vocabulary translation, not a 1:1 rename. The L1 LHS is a pure declarative schedule value `(p, dim, mg_max_levels, coarsening, family) → [FECollection]` naming a coarsest-to-finest list directly; the L0 RHS is an imperative bounded `for`-loop that `push_back`es per level into a `std::vector`, steps the order via a `switch`, breaks at the `pmin` floor, and then `std::reverse`s the accumulated vector. The `std::reverse` (`:70`) is correctly identified as the load-bearing reorganization — the L0 builds finest-first (comment `:41-42`) and reverses, while the L1 value names the coarsest-first orientation directly. That orientation gap + the imperative-build-vs-declarative-value gap is a real semantic-organization shift, not an identity-in-named-terms rename. This is not a degenerate `-body-identity` smell.

**variant-axis-coverage — pass.** The three variant axes are explicitly enumerated and each maps to a positively-anchored L0 site: (A) de-Rham family → template param + `pmin` coupling (`:30-33`) + ctor arity branch (`:46-55`), with all 4 subclasses tabulated (H1/ND pmin=1, RT/L2 pmin=0; ND/RT 4-arg, H1/L2 3-arg); (B) coarsening policy → the `switch` (`:60-68`); (C) LOR basis → `mat_lor`/`b2` selection (`:35-39`), with the inert-for-3-arg case explicitly scoped (`MFEM_CONTRACT_VAR(b2)` at `:54`). No hidden branches: the `max(1, mg_max_levels)` length floor and the `p == pmin` early break are both covered as loop-invariant pieces, not axes. The axis set matches D2's fe_collection operator axes as the report asserts (I could not cross-read D2's CYCLE.md under the no-shared-context discipline, but the three axes are internally consistent and source-anchored).

**cross-reference-integrity — pass.** Build-readiness fence guard: the `new:` block for the firm chapter ENCLOSES the full firm apparatus — `## Status` (line 58), L1/L0 forms, variant-axis tables, `## Applicability conditions`, `## Justification kind`, `## Verified-against`, `## Open questions` — all INSIDE the single fence (closing ```` ``` ```` at line 292). No firm body authored outside the fence; not the cycle-019 truncation defect. The indented-code sub-blocks (signatures, source excerpts) are 4-space-indented, not nested fences, so fence parity is clean (the three fences in the report — `new:`, `edit:SUMMARY`, `edit:index` — are balanced). Cross-refs: the sibling [`fe-space-construction-rotation`](./fe-space-construction-rotation.md) resolves (on disk, 11759 bytes, c064). The forward live-link to [`L1/fe_collection`](../L1/fe_collection.md) does NOT yet exist on disk — this is expected and correctly flagged: D2 authors it the same cycle, the theme was gated on D2 warrant=YES, and the report flags the integration-order dependency (apply D2 before/with this theme to avoid transient linkcheck failure). The SUMMARY edit anchors on line 151 (`- [fe-space-construction-rotation]...`), present and unique. The index.md edit anchors on the bilinear-form row (line 31), present and matching verbatim. Tally deferred to D4 is noted, not author here. All references either resolve or are correctly flagged as same-cycle-landing.

**edge-label-fidelity — pass.** The edge is L1 → L0, forward: LHS is the L1 `fe_collection` schedule value, RHS is the L0 `ConstructFECollections` body. The prose throughout narrates exactly that direction ("the forward rewrite (L1 schedule → L0 body)", the five build-order pieces, the reverse-direction lift explicitly quarantined to a working-note caveat per the high→low directive). No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is a firm L1>L0 lowering theme; content shape matches — positive-source-anchored structural rewrite with `## Status: firm`, no rough-in placeholders, no unfilled sections. The firm-on-positive-structure rationale (syntactic-identity / loop-invariant laws, no convergence semantics to test-gate, no-dedicated-`test-multigrid.cpp` non-gating) is consistent with the cited `fe_space`/`fe_assemble`/`apply_linop` precedent and is appropriate for a structural-translation theme.

**skill-uptake-survey — warning (telemetry only, non-blocking).** The report's shape implies relevant skills exist but none are referenced by name. Specifically: `verify-citation-range` / `tools/citecheck` (the dispatch invokes on-disk citation verification — the report describes doing this manually in §Supporting evidence but does not name the skill/tool); `verify-rotation-citation` and `propose-rotation` (a rotation-bearing L1>L0 theme); `classify-variant-axis` (three enumerated variant axes); and the `proposed-changes-fence-encloses-full-body-guard` is a critic-side skill not expected in the report. This is a pure presence check and does not affect correctness — the work itself is sound — but the skill-invocation telemetry is absent.

### Issues found

No blocking issues. All citations verify on-disk with zero drift; the rotation is a genuine translation; variant axes are fully covered with scoped-out inert cases; the fence encloses the full firm body; cross-references resolve or are correctly flagged.

1. **(informational, non-blocking) Same-cycle forward-link integration ordering** — `CYCLE.md` §Proposed-changes line 49 / Open-questions. The live link `[`L1/fe_collection`](../L1/fe_collection.md)` targets D2's entry, which is not yet on disk. The report correctly flags that the integrator must apply D2's `fe_collection.md` before or in the same finalize as this theme, else `linkcheck2` transiently fails. Not a defect in this report — a sequencing note for the integrator. Surfaced here for visibility.

2. **(informational, non-blocking) skill-uptake telemetry absent** — `CYCLE.md` (whole report). No skill/tool invocation named despite citation-verification, rotation, and variant-axis classification all being in scope. Pure telemetry; the underlying work is correct.

3. **(informational, non-blocking) out-of-scope citation-hygiene follow-up** — `CYCLE.md` §Open-questions/caveats "Stale `:22-75` close". The report notes a pre-existing stale `multigrid.hpp:22-75` citation in `fe_space.md:124-126` (correct close is `:72` return / `:73` brace, which I confirmed on-disk). Correctly scoped out of this dispatch's write-authority and flagged as a later citation-hygiene pass — recorded so the integrator/next planner can route it.

## Repair

### Fixes attempted

No content findings to repair. The critic returned 7 pass + 1 warning, the lone warning being `skill-uptake-survey` (pure telemetry / presence check, explicitly non-blocking, does not affect correctness). All load-bearing citations were verified on-disk with zero drift; the rotation is a genuine vocabulary translation (not a 1:1 rename); variant axes are fully enumerated with inert cases scoped out; the fence encloses the full firm body; cross-references resolve or are correctly flagged as same-cycle-landing. Nothing fell within (or required) repair authority.

- **Finding**: skill-uptake-survey warning — no skill/tool invocation named despite citation-verification, rotation, and variant-axis classification being in scope.
  - **Decision**: not-needed (telemetry-only warning; the critic marked it explicitly non-blocking; no surface or correctness defect to mechanically fix).

### Unrepairable findings

None. No finding exceeds repair authority because no finding requires repair — the report is clean.

## Suggested resolution

`overall_status: ready`. Notes for the integrator (informational, carried from the critic's three non-blocking items — none alters readiness):

1. **Same-cycle forward-link ordering** — the firm theme contains a live link `[`L1/fe_collection`](../L1/fe_collection.md)` targeting D2's not-yet-on-disk entry. Apply D2's `book/src/L1/fe_collection.md` before/with this theme at integration so `linkcheck2` does not transiently fail. Standard same-cycle pattern; resolves at finalize.
2. **Skill-uptake telemetry** — non-blocking; underlying work is correct. No action required.
3. **Out-of-scope citation hygiene (OQ-intake)** — a pre-existing stale `multigrid.hpp:22-75` citation in `book/src/L1/fe_space.md:124-126` (correct close is `:72`/`:73`, confirmed on-disk) is flagged for a later citation-hygiene pass. NOT in this dispatch's write-authority — route as open-questions intake for a future planner/hygiene dispatch.
