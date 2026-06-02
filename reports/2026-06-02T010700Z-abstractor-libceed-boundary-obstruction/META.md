---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T011500Z
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
repaired_at: 2026-06-02T012000Z
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

# META: verification of CYCLE-055 D5 — fe-assemble-libceed-boundary-obstruction (L1>L0 opaque-library-ownership annotation)

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing pinpoint was verified by codemap `read_range` and by `citecheck --anchor`; all zero-drift:
- `bilinearform.cpp:67-70` — `CeedBasis` anchor lands at lines [68, 69] within range; the `CeedElemRestriction` inputs actually begin at 64 (trial_restr) and 66 (test_restr), so the cited `67-70` captures the two `CeedBasis` lines plus the tail of `test_restr` but truncates the head of the restriction block (64-66). The prose claims `:67-70` "builds the CeedBasis / CeedElemRestriction inputs" — the bases are fully in-range, the restrictions partially clipped. This is a benign range-tightness imprecision, not drift (the anchor token resolves inside the range); noting it for transparency only.
- `bilinearform.cpp:75` `integ->Assemble` → [75] zero-drift. `bilinearform.cpp:77` `AddSubOperator` → [77] zero-drift. `bilinearform.cpp:118-132` `UseFullAssembly` confirmed (function def at 118, body through 132) — Palace-owned dispatch.
- `integrator.hpp:58-61` — codemap confirms line 58 = `virtual void Assemble(Ceed ceed, CeedElemRestriction trial_restr,` and `= 0` pure-virtual terminator at line 61. Exact match to the report's read-confirmed claim.
- `libceed/operator.cpp:455-490` `CeedOperatorFullAssemble` → 455 zero-drift; `:483` `CeedOperatorAssembleCOO` → [483] zero-drift; `:487-488` `OperatorCOOtoCSR` → anchor at [488] within 487-488 (the report self-disclosed the DRIFT +1 re-anchor honestly in §Supporting-evidence). All in-range.
- `verified_against:` YAML round-trip sub-check: extracted the indented block, dedented, `yaml.safe_load` succeeds (10 entries). No `note:` value begins with `'` or `"` — first non-whitespace char of every note is prose. No ParserError.
- `citecheck --scan` reports 6 `[MISS]`/`[AMBIG]` — these are path-hygiene artifacts of the abbreviated `libceed/operator.cpp` form used in prose/`//`-comments and the `integrator.hpp` basename collision (two `integrator.hpp` files in the tree). The authoritative full-path forms (`palace/fem/libceed/operator.cpp`, `palace/fem/integrator.hpp`) appear in the `inputs:` frontmatter and `verified_against:` block and all resolve in-range by codemap. Flagged as a minor path-hygiene warning (below), not a bounds failure.

**surface-or-evidence — pass.** This is a new obstruction theme (`new:` block), not a refinement of an existing operator/theme. It is claim-free negative-result documentation of a library boundary — exactly the retroactive-evidence / boundary-documentation shape the check permits. It correctly does NOT modify the `fe_assemble` surface (verified: `book/src/L1/fe_assemble.md` is untouched by the proposed-changes). The `verified_against:` block supplies positive Palace anchors for the Palace-owned sites and boundary anchors for the library-owned sites. No pure rotation_claim without surface.

**rotation-quality — pass (not a rotation; obstruction).** The theme asserts an ownership-boundary obstruction, not an algebraic/structural rotation, so the strict-compaction criterion does not apply. The §Justification-kind correctly self-classifies as a negative-result theme with no L_{n+1} representation to compact. The sub-kind reasoning (full `obstruction` not `partial-obstruction`, because the `Σ_i` fold lifts cleanly and only the leaf is opaque — a clean ownership split, not an un-liftable loop) is internally coherent and correctly distinguished from the `eigsolve` `partial-obstruction` sibling.

**variant-axis-coverage — pass.** The PA-vs-FA dispatch (the one genuine variant axis here) is explicitly handled: §Applicability-conditions item 4 scopes `UseFullAssembly` as a Palace-owned variant axis on the firm fold (obstruction does not apply); the full-assembly COO→CSR path is covered as its own libCEED-owned/Palace-owned split (items 2 and 6). The partial-assembly (matrix-free) branch is implicitly the no-materialization case. No hidden branch — the boundary table enumerates all six sub-parts (kernel, COO materialization, fold, dispatch, BC-elimination, COO→CSR shuffle) with an ownership verdict each.

**cross-reference-integrity — pass.** All four `[link]` targets resolve on disk: `../L1/fe_assemble.md`, `./fe-operator-assemble-mutation-rotation.md`, `./triangular-solve-obstruction.md`, and the self-page. The thread-opener's libCEED-boundary OQ that D5 claims to settle exists verbatim (`fe-operator-assemble-mutation-rotation.md:24-25` "logged as OQ, not yet classified obstruction vs. transitive-firm"; §"libCEED boundary" at :85-88, :125-126). The `triangular-solve-obstruction.md` precedent carries `opaque-library-ownership` (confirmed at :59, :167-170). Build-readiness / firm-body-inside-fence guard: the `## Status` apparatus sits at line 70 INSIDE the `new:` fence (42-336) — the full chapter body (Status, L1 form, L0 form, Applicability, Justification, Verified-against) is enclosed within the fence, not authored as report-top-level sections. No fence-truncation defect. New-chapter wiring: the `edit:book/src/L1-L0/index.md` block re-states the existing `triangular-solve-obstruction` row (line 48, exact match) then appends the new row, and the `edit:book/src/SUMMARY.md` block re-states the existing SUMMARY line (137, exact match) then appends — so the dep-map row and SUMMARY entry land together and the link resolves at build time.

**edge-label-fidelity — pass.** The theme is labeled L1>L0 throughout (frontmatter `layer: L1-L0`, `lowers:` field, §"L1 form (LHS)" / §"L0 form (RHS)"). The prose discusses exactly the L1→L0 edge: the L1 `fe_assemble` fold's per-term leaf `A(term_i)` and its L0 realization across `bilinearform.cpp` / `libceed/operator.cpp`. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is obstruction (opaque-library-ownership); content shape matches — claim-free boundary documentation, no speculative operators (§Speculative-L1-operators and §Speculative-operators-proposed both correctly "None"), explicit "no promotion route" routing. The mandatory sub-kind tag IS present in the `## Status` line (`obstruction (opaque-library-ownership)`) AND in frontmatter (`sub_kind: opaque-library-ownership`). Sub-kind correctness (load-bearing, per dispatch): the element-local quadrature kernel is built by a pure-virtual `BilinearFormIntegrator::Assemble` that produces a `CeedOperator` consumed opaquely (codemap-confirmed `integrator.hpp:58-61`, `bilinearform.cpp:75`), and the numerical COO assembly runs inside `CeedOperatorAssembleCOO` (libCEED API). This is the entire-callable-lives-outside-Palace signature → `opaque-library-ownership` is the correct sub-kind, NOT `enum-only-stub` (no Palace-owned `MFEM_ABORT`/`// TODO` body). The boundary precision is drawn correctly: Palace-owned = `AddSubOperator` fold (:77), `UseFullAssembly` dispatch (:118-132), `OperatorCOOtoCSR` shuffle (:487-488); library-owned = the kernel + `CeedOperatorAssembleCOO`. All codemap-verified.

**skill-uptake-survey — pass.** The report references `tools/citecheck/citecheck.py` use at emit time (§Supporting-evidence enumerates the `--anchor` runs, including the honest DRIFT +1 disclosure). The `verify-citation-range` / citecheck procedure is the relevant skill for an obstruction-anchor report and is invoked. Telemetry surfaced; nothing blocking.

### Issues found

1. **`bilinearform.cpp:67-70` range slightly clips the CeedElemRestriction block — info/cosmetic.** (`new:` block §L0-form "libCEED-owned (leaf)", and `verified_against` entry 1, and index.md dep-map row.) The cited range `67-70` fully contains the two `CeedBasis` lines (68-69) but the `CeedElemRestriction trial_restr`/`test_restr` inputs the prose also attributes to this range actually start at lines 64 and 66. The anchor token (`CeedBasis`) resolves in-range so this is not drift, but the range under-covers the restriction inputs it names. Severity: **info** (range-tightness, not a correctness defect; the repairer may optionally widen to `:64-70` for full coverage of the named inputs).

2. **Abbreviated `libceed/operator.cpp` path in prose/comments trips `citecheck --scan` (6 MISS/AMBIG).** (`new:` block §L0-form code-comment headers `// libceed/operator.cpp:...`, and the `// integrator.hpp:...` comment header.) The in-comment `//`-anchors use the short basename form (matching the precedent house style — `triangular-solve-obstruction.md` likewise uses bare basenames in its `//` comments), but `--scan` cannot resolve the bare `libceed/operator.cpp` (no such relative path under `reference/`) and reports `integrator.hpp` as AMBIG (two such files in the tree). The authoritative `verified_against:` and `inputs:` entries DO use full paths and all resolve in-range. Severity: **warning** (path-hygiene; consistent with house style but the bare-basename comments are unresolvable by the scan tool — a repairer could promote the comment headers to full paths for scan-cleanliness without altering house-style intent).

3. **`boundary-anchor` verdict flavor is a new, un-ratified verdict vocabulary — legitimate observation for the meta-phase.** (`verified_against:` block uses `verdict: boundary-anchor` and `verdict: positive-palace-owned` / `positive-cross-reference`; flagged by D5 itself in §Open-questions.) The precedent `triangular-solve-obstruction.md` uses only `negative-anchor` for all its library-owned sites. D5's reasoning is sound: these ARE positive Palace source sites (the call-sites exist at exact cited lines) that mark a library boundary — semantically distinct from an absence/negative anchor. This is a legitimate vocabulary-extension observation that the lowering-verifier / meta-phase should reconcile (normalize `boundary-anchor` vs `negative-anchor` vs `positive-*` across the obstruction-theme corpus). Severity: **info** (correctly self-flagged, routed to meta-phase; not a defect in this report — the verdict block round-trips and is internally consistent).

4. **`OperatorCOOtoCSR` ownership boundary is self-flagged as a fine line — honest caveat, no action needed.** (`new:` §Applicability item 6 + §Open-questions caveat 3.) D5 classifies `OperatorCOOtoCSR` (:487-488) as Palace-owned format-conversion and notes that `operator.cpp:492-499` scales duplicated nonzeros (codemap-confirmed: lines 492-499 do `hypre_CSRMatrixSetConstantValues` + scale duplicated nonzeros across threads). The caveat correctly observes the exact boundary line could shift if the reshuffle does numerical work, while the shell/leaf split remains robust. Severity: **info** (transparent caveat; the load-bearing classification is unaffected).

5. **DEFERRED tally to D7 correctly observed.** (§Open-questions caveat 1.) D5 registers its own index TABLE row + SUMMARY entry but does NOT author any consolidated running-count / cohort-total / coverage-gap line, deferring those to D7 (count-owner) per the dispatch partition. Verified: the `edit:index.md` block adds only the one new row (no total-count edit); no growth-log mutation. Severity: **info** (correct partition compliance, noted as positive confirmation).

No fail- or fence-level defects. The load-bearing claims the dispatch flagged for special attention — sub-kind correctness, boundary precision, `fe_assemble`-stays-firm coherence, and the `triangular-solve-obstruction` precedent — all verify clean against codemap and the on-disk artifact.

## Repair

### Fixes attempted

- **Finding 1 (info)**: `bilinearform.cpp:67-70` range under-covers the `CeedElemRestriction` inputs the prose attributes to it — `trial_restr`/`test_restr` start at 64/66, only the two `CeedBasis` lines (68/69) are in-range.
  - **Decision**: repaired
  - **Action**: Widened the citation `67-70` → `64-70` everywhere it refers to this CeedBasis/CeedElemRestriction input block: `CYCLE.md` frontmatter `inputs:`, `new:` block `l0_anchor` frontmatter, §L0-form prose ("libCEED-owned (leaf)"), §Verified-against prose bullet, the `verified_against:` YAML citation+note (with a repair tag in the note), and the `edit:book/src/L1-L0/index.md` dep-map row. Verified against codemap `bilinearform.cpp:62-78`: line 64 = `CeedElemRestriction trial_restr` decl, 66 = `test_restr`, 68 = `trial_basis`, 69 = `test_basis` — `64-70` fully covers all four named inputs (70 is the `for`-loop head, a harmless tail; matches the critic's suggested end). Anchor tokens still resolve in-range; this is a range-tightness widen, not a content change.

- **Finding 2 (warning)**: abbreviated `libceed/operator.cpp` / `integrator.hpp` paths in `//`-comment headers trip citecheck `--scan` (6 MISS/AMBIG).
  - **Decision**: not-needed (accepted as house style)
  - **Rationale**: The critic explicitly scoped this as "your call; the precedent accepts the abbreviated `//`-comment form." The `triangular-solve-obstruction.md` precedent uses bare basenames in its `//` comments as established house style, and the authoritative full-path forms in `inputs:` / `verified_against:` / `l0_anchor` all resolve in-range by codemap. Promoting the in-comment headers to full paths would diverge from the precedent's settled house style for marginal scan-cleanliness; accepted as-is. No fix applied.

- **Findings 3, 4, 5 (info)**: `boundary-anchor` verdict flavor + `OperatorCOOtoCSR` fine-line ownership self-flagged to meta-phase; DEFERRED tally to D7 confirmed.
  - **Decision**: not-needed
  - **Rationale**: All three are correctly self-flagged by D5 in §Open-questions and routed to the batch-17 meta-phase / D7. They are observations, not defects — no repair authority is implicated. The `boundary-anchor` verdict block round-trips and is internally consistent; the COOtoCSR shell/leaf split is robust regardless of the fine line; the index/SUMMARY-only registration with tally deferred to D7 matches the dispatch partition.

### Unrepairable findings

None. All findings were either repaired (Finding 1) or not-needed (Findings 2-5).

## Suggested resolution

`ready` — clean obstruction annotation; the one actionable info finding (range widen) was trivially applied.

Notes for the integrator:
- D5's proposed-changes: `new:book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` (obstruction, opaque-library-ownership) + one new `edit:book/src/L1-L0/index.md` dep-map row + one new `edit:book/src/SUMMARY.md` entry (both re-state the existing sibling line then append the new one, so links resolve at build time).
- **DEFERRED tally to D7** — D5 registers only its own index row + SUMMARY entry; the consolidated obstruction-cohort running-count / coverage-gap line is D7's (count-owner) per the dispatch partition. Do not expect a total-count edit from D5.
- **Promote D5's OQs to the batch-17 meta-phase**: (a) the new `boundary-anchor` verdict flavor (vs `negative-anchor` / `positive-*`) for verdict-vocabulary reconciliation across the obstruction-theme corpus; (b) the `OperatorCOOtoCSR` (`libceed/operator.cpp:487-488`) Palace-vs-libCEED ownership fine-line (note `:492-499` scales duplicated nonzeros — the exact boundary line could shift if the reshuffle does numerical work; the shell/leaf split is robust regardless).
