---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T231500Z
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
repaired_at: 2026-06-07T232500Z
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

# META: verification of "# Synthesis Part shell + the `types` library"

## Critique

### Checks run

**citation-validity** — `warning`. This is a shell/intro authoring dispatch (a new implementation-VIEW chapter KIND), so most "citations" are `reference`-class cross-links to existing artifact chapters, not L0 source pinpoints; I verified those under cross-reference-integrity. The few genuine source/evidence pinpoints in §Supporting evidence are real and in-range, but one is imprecise: line 425 cites `concepts/op-params.md:24` as the evidence that `OpParams` is "read by `iteration` (krylov-step) AND `coordination` (ksp_solve/solve_family/fold_solve)". On disk, `op-params.md:24` is the **Kind callout line** (`> **Kind: record.** …`), not the multi-consumer evidence — the ≥2-consumer claim is actually borne out at `op-params.md:84-85` (the "Used by" list: `krylov-step` + `solve-monad`) and `op-params.md:97` (the Status line, which states the record is "referenced by ≥2 consumers"). The claim is true and supported within the same file; only the pinpoint is off. The `sim-state.md:66-71` ("Used by") and `config-record.md` citations check out exactly. Flagged `warning` rather than `fail` because the cited file/range is real and in-range and the substantive claim holds elsewhere in the same file.

**surface-or-evidence** — `pass`. Per the feature-surface / implementation-VIEW adaptation, this Synthesis kind makes no *new* per-op algebraic claim of its own; its "evidence" is the set of `reference`-class down-links to the authoritative L4/concepts/semantics defs, all of which I confirmed resolve (see cross-reference-integrity). **Record-definition sub-check:** the `types` chapter NAMES three records in rendered signatures (`IoData`, `OpParams`, `SimState`) — each has a definition home that EXISTS on disk (`concepts/config-record.md`, `concepts/op-params.md`, `concepts/sim-state.md`) and is back-linked, satisfying the "define once, link-don't-restate" obligation. `EigState` is named (prose only) in the deferred `coordination` stub shell and has NO `concepts/` home — but the report explicitly routes it via Open-questions flag `record-EigState-needs-definition-home`, which is exactly the discipline-conformant disposition (so not a flag here).

**rotation-quality** — `pass` (not applicable to the Synthesis implementation-VIEW kind). A Synthesis chapter rotates nothing — it renders already-firm L4 vocabulary as library code; analogous to the feature-surface / stub no-op of this check.

**variant-axis-coverage** — `pass` (not applicable). The shell/intro chapters have no variant axes of their own; the axes live in the constituent ops they will render (e.g. `OpParams.orthog?`/`scalars?` optionality, which is documented in the rendered record but is the op's axis, not the chapter's). No hidden branches.

**cross-reference-integrity** — `pass` (load-bearing for this kind, and clean). I checked every `[link]` and every `edges: reference:` target against disk: all 27 L4 chapter references resolve (incl. the three `*-combinators-intro.md` doc-group intros and the rank-0 `sharding-decompose-reduce.md`); all concept back-links resolve (`config-record`, `sim-state`, `op-params`, `krylov`, `step-outputs`, `prev-carry`, `dofset`, `WaveguideModeTable`, `solve-result`, `eigsolve`); `methodology/semantic-consolidation.md`, `feature/index.md`, `feature/lifecycle.L4.md`, `concepts/index.md`, `semantics/index.md` all resolve; casing is correct on the case-sensitive pages (`dofset.md`, `WaveguideModeTable.md`). Intra-Part forward-refs (`synthesis/index`, `synthesis/types`, `synthesis/iteration`, …) are all created within this same dispatch. The two intra-page anchors resolve: `#rendering-conventions` ← `## Rendering conventions`; `#type-placement--cluster-a-type-with-its-api-group` ← `### Type placement — cluster a type with its API group` (the ` — ` em-dash slugifies to `--`, matching the anchor). The graded-stack discipline is correct: every Synthesis chapter is `kind: navigational-container` with `reference`-edges only and NO `depends-on` — no new blocking edge, no rank/liveness constraint on any firm node (matches the landed `L4/index.md:1-11` form the linters key off). The stub shells correctly carry BOTH `status: stub` and the navigational `kind`. SUMMARY insertion is correct: the `[old]` anchor matches `SUMMARY.md:3-10` verbatim and the `# Synthesis` block is inserted immediately before `# Feature surfaces — entry points`, in the directive-mandated order types→iteration→data-algebra→coordination→drivers.

**edge-label-fidelity** — `pass`. No L_{n+1}→L_n edge labels are asserted (this is not a lowering theme); the `reference` edges are navigational and the prose discusses exactly those targets.

**plan-kind-consistency** — `pass`. Declared shapes match content: `index.md` + `types.md` are navigational-container (no rank claim) and are authored as such; `iteration`/`data-algebra`/`coordination`/`drivers` are `status: stub` shells with explicit "Wave 2 fills the bodies" framing and operator-list + topological-order + rendering-conventions scaffolding — a faithful stub, not an over-claim. `types.md` is presented as "rendered" (body present), consistent with the directive's LEAD-sequencing step (b).

**skill-uptake-survey** — `pass`. No skill is squarely implied by a shell-authoring dispatch of this kind; the report appropriately cites the in-line CLAUDE.md §SYNTHESIS directive bullets and the `project_katex_dollar_sigil_fence_requirement` / navigational-container conventions in lieu. Telemetry only; non-blocking.

### Issues found

1. **(citation-validity, warning) Imprecise pinpoint** — `CYCLE.md` §Supporting evidence (line 425): `concepts/op-params.md:24` is cited as evidence of the ≥2-API-group consumer claim for `OpParams`, but line 24 is the page's "Kind: record" callout. The supporting evidence is actually at `op-params.md:84-85` ("Used by": krylov-step + solve-monad) and `op-params.md:97` (Status: "referenced by ≥2 consumers"). Claim is true; pinpoint should be corrected to one of those ranges.

2. **(cross-reference-integrity / fidelity, minor — borderline pass) Synthesized field-type names diverge from the authoritative back-linked home** — in `types.md` §`IoData` (CYCLE.md lines 130-136) the rendered record types the five sub-records as `ProblemConfig` / `ModelConfig` / `DomainConfig` / `BoundaryConfig` / `SolverConfig`, whereas the authoritative home this chapter back-links to (`concepts/config-record.md:69-73`) names them `config::ProblemData` / `config::ModelData` / `config::DomainData` / `config::BoundaryData` / `config::SolverData`. For an implementation-VIEW that renders a *synthesized* library form, a clean-name re-rendering is arguably within scope (the directive says it renders the synthesized code, not the C++ namespace), so this is not a hard cross-reference failure — but it introduces a name a reader cannot resolve back to the authoritative schema by string-match, weakening the "render-the-form + link-to-the-home" round-trip. Worth either (a) using the authoritative sub-record names, or (b) one line noting the synthesized names are clean-room renamings of `config::*Data`. Did not downgrade cross-reference-integrity to warning because the structural link to `config-record.md` itself resolves and the field *list* (problem/model/domains/boundaries/solver) matches exactly.

3. **(informational, not a defect) `EigState` definition-home gap is correctly self-flagged** — named in the deferred `coordination` stub shell prose only, no `concepts/EigState.md` on disk; the report routes it via Open-questions `record-EigState-needs-definition-home` and defers the dispatch decision to Wave-2 D4. This is the discipline-conformant disposition for a record not yet rendered in a signature; recorded here only so the integrator/repairer can see it was considered, not as a finding to repair.

## Repair

### Fixes attempted

- **Finding 1 (citation-validity, warning)**: Imprecise pinpoint — `concepts/op-params.md:24` cites the page's "Kind: record" callout, not the ≥2-consumer evidence.
  - **Decision**: repaired
  - **Action**: `CYCLE.md` §Supporting evidence (`OpParams` bullet). Corrected the pinpoint from `op-params.md:24` to `op-params.md:84-85` (the "Used by" list: `krylov-step` + `solve-monad`) and added the `op-params.md:97` Status-line reference ("referenced by ≥2 consumers"). Verified both ranges on disk: line 24 is the `> **Kind: record.**` callout; 82–85 is the `## Used by` block; 97 is the `## Status` line. This is the off-by-offset citation-slip case squarely in repair scope (claim true, pinpoint mechanically corrected to the supporting range in the same file).

- **Finding 2 (cross-reference-integrity / fidelity, minor)**: Synthesized field-type names (`ProblemConfig`/…/`SolverConfig`) diverge from the authoritative back-linked home (`config::ProblemData`/…/`config::SolverData` at `config-record.md:69-73`), so a reader cannot string-match them back to the schema.
  - **Decision**: repaired
  - **Action**: `CYCLE.md` §2 (`types.md` `IoData` rendered block). Took the critic's option (b) — added a one-line code-comment in the rendered `text` block mapping each synthesized sub-record name to its authoritative `config::*Data` type with the `config-record.md:69-73` cite, restoring the render-the-form + link-to-the-home round-trip. This is the trivial clarifying-note fix (the directive explicitly permits clean-room renaming for the implementation VIEW; the fix adds the missing back-resolution mention, authoring no new content/claim).

- **Finding 3 (informational)**: `EigState` definition-home gap.
  - **Decision**: not-needed — already discipline-conformant (routed via Open-questions `record-EigState-needs-definition-home`, deferred to Wave-2 D4); the critic flagged it as not-a-defect.

### Unrepairable findings

None. Both substantive findings were mechanical (citation-pinpoint slip + a clarifying back-reference note) and were repaired in place; the third is informational and needs no action.

## Suggested resolution

`ready`. Both flagged findings were surgically repaired in `CYCLE.md` without authoring substantive content. Notes for the integrator: this is a navigational-container / implementation-VIEW shell dispatch (no `depends-on` edges, `reference`-class links only); the `EigState` definition-home decision and the `drivers` library body are correctly deferred to later batch-44 cycles via the report's Open-questions, and the role-spec Synthesis-discipline codification is flagged for the batch-44 meta-phase — none of these block applying this shell.
