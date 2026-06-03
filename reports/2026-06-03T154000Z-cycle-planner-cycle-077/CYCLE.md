---
agent: cycle-planner
invoked_at: 2026-06-03T154000Z
scope: cycle-077 dispatch plan
status: pending
---

# Cycle 077 dispatch plan

## Goals selected this cycle

Cycle-077 is the **SECOND** primary cycle of meta-batch-24 (cycles 076/077/078; the batch-24 meta-phase fires AFTER cycle-078's finalize). Cycle-076 landed the Feature-Part by-kind reorg (the structural surface is now settled). Per the c076 finalize signal + the batch-24 active head, this cycle LEADS with the **record-definition-pages-first-cohort (#2, HIGH — user directive 2, now codified into the role-specs)** — the supply side of the critic's new `surface-or-evidence` record-definition sub-check — and firms the two `rough-in` reduction verbs' missing L1 homes (**#3 `participation_ratio`**, **#4 `port_projection`**), which are the named gates blocking `eigenfreq_qfactor_reduce` (gate-a) and `sparameter_reduce` (gate-b) from promoting past `rough-in`. The deferred energy-fields (#5) + boundary-mode (#6) columns stay deferred this cycle — the cohort above fills the fan-out budget, and those land directly in their by-kind groupings when authored.

## Deliverable-presence verification (paste-inline-evidence; per the strengthened batch-10 bullet)

**D1 — L4 solve-record concept trio (`op-params` / `sim-state` / `krylov`):** OPEN-by-construction (no record-definition page has ever existed — directive-2 obligation is new this batch). ABSENT-verified:
```
$ ls book/src/concepts/{op-params,opparams,sim-state,simstate,krylov}.md
ABSENT: concepts/op-params.md
ABSENT: concepts/opparams.md
ABSENT: concepts/sim-state.md
ABSENT: concepts/simstate.md
ABSENT: concepts/krylov.md
```
Cross-cutting bar (≥2 consumers) — confirmed far above bar: `Krylov` 11 L4 chapters, `OpParams` 11, `SimState` 12 (grep `-rl` over `book/src/L4/`, intros excluded for Krylov). Existing `concepts/state-stratification.md` covers the three-stratum *conceptual typing* (NOT a per-record field schema + L0-struct home) → the record-definition pages are the distinct *data-shape* homes (directive-2), NOT a duplicate.

**D2 — L4 step/carry/result concept trio (`step-outputs` / `prev-carry` / `solve-result`):** OPEN-by-construction. ABSENT-verified:
```
$ ls book/src/concepts/{step-outputs,stepoutputs,prev-carry,prevcarry,solve-result}.md
ABSENT: concepts/step-outputs.md
ABSENT: concepts/stepoutputs.md
ABSENT: concepts/prev-carry.md
ABSENT: concepts/prevcarry.md
ABSENT: concepts/solve-result.md
```
Cross-cutting bar: `StepOutputs` 2 chapters (chebyshev, krylov-step — at bar), `PrevCarry` 4 (iterate-while, krylov-step, iterate-while-with-prev, index — above bar), the `Solve {...}` result record 6 chapters (above bar). All ≥2. `concepts/solve-monad.md` covers the `Solve a = StateT SimState Identity a` monad (the *effect*, NOT the result-record *shape*) → the `solve-result` page is the distinct record-shape home.

**D3 — config-record concept page (`config-record`):** OPEN-by-construction. ABSENT-verified:
```
$ ls book/src/concepts/{config-record,iodata}.md
ABSENT: concepts/config-record.md
ABSENT: concepts/iodata.md
```
Cross-cutting bar — far above: `Config`/`IoData` named in the lifecycle ROOT (3 levels) + `ElectrostaticConfig` (electrostatic + capacitance columns) + `MagnetostaticConfig` (magnetostatic + inductance) + `EigenmodeConfig` (eigenmode + eigenfrequency-qfactor) + `DrivenConfig` (driven + sparameters) — every config record is named across ≥2 feature columns. L0 home located: `IoData iodata(argv[1], false)` (`main.cpp:231`); per-driver capture sites cited in each column (e.g. `LaplaceOperator laplace_op(iodata, mesh)` `electrostaticsolver.cpp:28`).

**D4 — `participation_ratio` L1/L2 primitive:** OPEN (firm-home does not exist; OQ `participation-ratio-l1-primitive-as-eigenfreq-qfactor-firming-route` c075 D3 is unresolved). ABSENT-verified:
```
$ ls book/src/{L1,L2}/participation_ratio.md book/src/{L1,L2}/participation-ratio.md
ABSENT: L1/participation_ratio.md   L2/participation_ratio.md
ABSENT: L1/participation-ratio.md   L2/participation-ratio.md
$ grep -rln 'participation_ratio\|participation ratio' book/src/L1 book/src/L2
(no matches)
```
Gate confirmed: `L4/eigenfreq_qfactor_reduce.md` `## Status` = `rough-in`, reasoning cites `postoperator.cpp:1188-1203` Q-factor body as the un-homed constituent. Structural-block check: NOT blocked — the constituent is a positive source site (`κ_mj = ½R|I|²/E`), not a stub.

**D5 — `port_projection` L1 home:** OPEN (firm-home does not exist; OQ `sparameter-reduce-l1-port-projection-home` c075 D1 unresolved). ABSENT-verified:
```
$ ls book/src/{L1,L2}/port_projection.md book/src/{L1,L2}/port-projection.md
ABSENT: L1/port_projection.md   L2/port_projection.md   (all four)
$ grep -rln 'port_projection' book/src/L1 book/src/L2
(no matches)
```
Gate confirmed: `L4/sparameter_reduce.md` `## Status` = `rough-in`, reasoning cites the per-column `sᵢ·E` linear projection as un-homed. Unify candidate `L1/bilinear-form.md` EXISTS (the open question is whether `sᵢ·E` is a left-fixed partial-application of `bilinear-form` or its own verb). Structural-block check: NOT blocked — positive source sites.

**STOP-PROPOSING negative-list check:** none of the 5 dispatch scopes matches a disqualified slug (`lu_solve`/`back_solve`/`ls-update-column`/4 NLEPS atoms/`apply_nonlinear_pencil`). The record-definition pages are a NEW kind (data-shape concept homes), not L3-cohort backfills.

**Already-landed check (c027 bullet):** c076 `counts_after` = pure-structural (Feature-Part reorg, ZERO count/status changes; concepts count unchanged at 26). None of D1–D5 was landed by c074/c075/c076 (those landed the output-product columns + reduce verbs + the reorg, NOT record-definition pages nor the participation/port L1 homes).

## Source-anchor verification (codemap, on-disk-confirmed)

- `postoperator.cpp:1188-1203` — `κ_mj = ½R|I_mj|²/E_m`, `Q_mj = ω_m/κ_mj` (the `vi.mode_port_kappa` / `vi.quality_factor` body). Confirmed via `read_range`. **Same energy-ratio shape recurs** at the inductive EPR `p_mj = ½L|I|²/E` (`:1215-1219`, `vi.inductive_energy_participation`) and the surface-dielectric participation `p_mj = ½t Re{∫(εE)ᴴE}/(E_elec+E_cap)`, `1/Q = p·tanδ` (`:1346-1373`, `energy_participation_p = energy/energy_electric_all`). **≥3 witnesses** → clean ≥2-member `participation_ratio` cohort (the `½X|I|²/E` / `energy/E_total` energy-participation-ratio shape).
- `lumpedportoperator.cpp:283-294` — `LumpedPortData::GetSParameter`: `dot = (*s)·E.Real() [+ i (*s)·E.Imag()]` — the field-onto-port-mode linear functional. Confirmed.
- `waveportoperator.cpp:780-793` — `WavePortData::GetSParameter`: `(E×H_inc⋆)·n = E·(-n×H_inc⋆)` realized as `(*port_sr)·E_real ...` linear functionals. Confirmed. **2 witnesses** (lumped + wave) for `port_projection`.

## Dispatches

**D1 — `layer-intro-author` — `concepts/{op-params,sim-state,krylov}.md` (L4 solve-record trio; record-definition cohort #2(a), HIGH).**
Scope: author THREE record-definition concept pages, one tight cohort (the three-stratum solve records) — `concepts/op-params.md`, `concepts/sim-state.md`, `concepts/krylov.md`. Each defines the record **in itself** per the directive-2 obligation: fields + types + meaning + construction-vs-run-time stratum of each field + the L0 source home of the backing C++ struct/instance-fields it mirrors. Source material already on disk: `L4/krylov-step.md:37-50` (the per-record stratum prose + slice-specific field schemas: CG `Krylov = {r,p,z?,α,β}`, GMRES `{V,Z?,H,s,cs,sn,β,j}`; `SimState = {x,it,converged,final_res,initial_res}`; `OpParams` = readonly variant-selector + constructed-operator-surface closure) and `concepts/state-stratification.md` (the three-way typing — CROSS-LINK it, do NOT restate it). Kind = a NEW `record` value in the `concepts/index.md` Kind table (define it in the index legend). Each page is the *data shape*; do NOT restate the operator algebra over the records (that lives in `krylov-step.md` et al.). Each page adds its OWN alpha-position row to `concepts/index.md` `## Index` table AND its OWN alpha-position `SUMMARY.md` entry (distinct anchors, parallel-safe — see overlap analysis). deps: none.
rationale: directive-2 record-definition obligation, highest-fan-out targets (each record cross-cuts 11–12 L4 chapters); the critic record-definition sub-check now flags these un-homed records, so this is the supply side.

**D2 — `layer-intro-author` — `concepts/{step-outputs,prev-carry,solve-result}.md` (L4 step/carry/result trio; record-definition cohort #2(a), HIGH).**
Scope: author THREE record-definition concept pages, one tight cohort (the per-step result-side records) — `concepts/step-outputs.md` (the demand-prunable per-step readout bundle: residual norm, LS residual, breakdown tokens; `krylov-step.md:41,87,96`), `concepts/prev-carry.md` (the first-iteration-unrolling closure-threaded recurrence carry — CG `β_prev`, GMRES `H_{k,k-1}`; `krylov-step.md:40,82`; cross-link `concepts/first-iteration-unrolling.md`), `concepts/solve-result.md` (the `Solve {sim, krylov, outputs[, carry]}` return record shape — the *record fields*, distinct from the `Solve` monad effect which `concepts/solve-monad.md` owns; `krylov-step.md:41-42`). Same directive-2 obligation (fields+types+meaning+stratum+L0 home), same `record` Kind, same data-shape-not-algebra discipline, same own-row-own-bullet index/SUMMARY registration as D1. deps: none.
rationale: completes the L4-record-type cohort (the c076-finalize-named HIGH lead); these three are the result-side records distinct from D1's input/state-side trio.

**D3 — `layer-intro-author` — `concepts/config-record.md` (feature-surface config record; record-definition cohort #2(b), HIGH).**
Scope: author ONE cross-cutting record-definition page `concepts/config-record.md` defining the config record schema + its `IoData` L0 home: the spine-ROOT `Config`/`IoData` surface (`IoData iodata(argv[1], false)` `main.cpp:231`; `problem.type` → driver dispatch `main.cpp:258`; mesh+order; per-driver material/boundary/source; refinement config) AND its per-driver specializations (`ElectrostaticConfig`/`MagnetostaticConfig`/`EigenmodeConfig`/`DrivenConfig` as the readonly construction-stratum projections each feature column consumes — capture sites e.g. `LaplaceOperator laplace_op(iodata, mesh)` `electrostaticsolver.cpp:28`). Define the config-record schema as the data shape (fields + types + meaning + the construction-vs-run-time stratum — config is uniformly readonly construction-stratum), cite the `IoData` backing surface as the L0 home. Cross-link `concepts/build-time-vs-run-time-stratification.md`. Kind = `record`. Own alpha-row in `concepts/index.md` + own `SUMMARY.md` entry. deps: none.
rationale: directive-2 record-definition obligation for the feature-surface config records (named across ≥2 columns each, the spine-ROOT `Config` across all 5 driver branches); secondary-priority to the L4 record types per the finalize signal but co-equal fan-out as a cross-column home.

**D4 — `combinator-miner` / `harvester` — `participation_ratio` L1 (or L2) primitive (active head #3, MEDIUM-HIGH; firms `eigenfreq_qfactor_reduce` gate-a).**
Scope: harvest/mine the per-mode energy-participation-ratio primitive `participation_ratio` — the `½X|I|²/E` (and `energy/E_total`) energy-ratio shape folded by `eigenfreq_qfactor_reduce`. THREE witnesses establish the ≥2-member cohort: lumped-port loss-rate `κ_mj = ½R|I|²/E` (`postoperator.cpp:1188-1203`), inductive EPR `p_mj = ½L|I|²/E` (`:1215-1219`), surface-dielectric participation `p_mj = ½t Re{∫(εE)ᴴE}/(E_elec+E_cap)` (`:1346-1373`). Author the firm L1 home (and the L2 entry IF the decomposition meaningfully reshapes — apply judgment per the redirect; do NOT force a rectangular floor). Resolve OQ `participation-ratio-l1-primitive-as-eigenfreq-qfactor-firming-route`. The verb-firming closes one of the `eigenfreq_qfactor_reduce` rough-in gates (gate-a); note the coupled re-check of the eigenfrequency-qfactor column promotion in the report (do NOT re-anchor it here — that is the coupled-column pass when both gates close). deps: none.
rationale: firms `eigenfreq_qfactor_reduce`'s named L1 gate + serves the inductive/surface-dielectric participation siblings; clean-describable in shared spine vocabulary (positive source sites).

**D5 — `harvester` — `port_projection` L1 home (active head #4, MEDIUM-HIGH; firms `sparameter_reduce` gate-b).**
Scope: harvest the per-port linear-functional `port_projection` (the field-onto-port-mode projection `sᵢ·E` folded by `sparameter_reduce`). Two witnesses: lumped `(*s)·E` (`lumpedportoperator.cpp:283-294`), wave `(E×H⋆)·n = E·(-n×H⋆)` (`waveportoperator.cpp:780-793`). **The load-bearing question to resolve:** is `port_projection` a specialization of the existing `L1/bilinear-form.md` (a left-fixed partial-application at the port-mode covector `sᵢ`), or its own verb? Investigate first; if it cleanly factors through `bilinear-form`, record it as a `bilinear-form` specialization NOTE (unify, per the redirect — do NOT mint a redundant verb); if it does not (the wave-port `(E×H⋆)·n` may not be a symmetric bilinear form), author the standalone `port_projection` L1 entry. Resolve OQ `sparameter-reduce-l1-port-projection-home`. Closes the `sparameter_reduce` rough-in gate-b. deps: none.
rationale: firms `sparameter_reduce`'s named L1 gate; the unify-vs-mint decision may consolidate with `gram_reduce`'s `bilinear-form` constituent (cross-pipeline conciseness).

## Overlap analysis

Pairwise (D1–D5):

- **D1 × D2 × D3** — all three `layer-intro-author` dispatches author NEW `concepts/<slug>.md` files (disjoint slugs: D1 = {op-params, sim-state, krylov}, D2 = {step-outputs, prev-carry, solve-result}, D3 = {config-record}) and each appends its OWN alpha-position rows to `concepts/index.md` `## Index` table + `SUMMARY.md` concepts block. **Shared-index check:** `concepts/index.md` `## Index` is a `| Concept | Kind |` ALPHA table with **NO consolidated count tally** (verified — no running total / firm-count line in the Index section). Per the parallel-blind-shared-index guard, distinct alpha-position ROW inserts at distinct anchors are **parallel-safe** (the guard fires only on a shared *consolidated aggregate*, which this index does not carry). Likewise `SUMMARY.md` entries are distinct alpha-position lines. The only shared touch is the `record` Kind-legend line in `concepts/index.md` — **D1 OWNS the one-time `record` Kind-legend addition** (it is first alpha and authors the legend entry); D2/D3 add their rows using the already-defined `record` Kind and do NOT re-author the legend. → **NON-overlapping at the operational level → PARALLEL** (with the D1-owns-Kind-legend partition stated). Minor alpha-insert co-edit of `concepts/index.md`/`SUMMARY.md` is exactly the conflict-tolerance case the integrator's merge handling absorbs cleanly; when in doubt, PARALLEL.
- **D1/D2/D3 × D4 × D5** — D4 authors `L1/L2/participation_ratio.md` (+ possibly an `L1/index.md` dep-map row); D5 authors `L1/port_projection.md` OR a NOTE in `L1/bilinear-form.md` (+ possibly an `L1/index.md` dep-map row). DISJOINT file regions from the `concepts/` trio and from each other. D4/D5 both MAY append a row to `L1/index.md` — distinct alpha-position rows, NOT a shared aggregate → parallel-safe (state: each appends ONLY its own dep-map row; `L1/index.md` carries no consolidated firm-count that both would blind-write — and even the firm-count, if present, is a single integer the finalize reconciles; flag if D4/D5 both touch a firm-count line). → **NON-overlapping → PARALLEL.**
- **D4 × D5** — distinct slugs, distinct source regions, distinct OQs. The only conceptual coupling is the shared "is this a `bilinear-form` specialization?" lens (D5 asks it of `port_projection`; D4 may note `participation_ratio` is NOT a bilinear form). No file collision. → **PARALLEL.**

No two dispatches modify the same operator entry or rewrite the same theme body. No forward-reference between co-dispatched reports this cycle (each authors a self-contained home; the reduce-verb re-anchors are DEFERRED to the coupled-column pass, not done here) → the cross-report-forward-reference-slug-divergence guard is N/A this cycle.

## Sequencing schedule

**Single wave — all 5 dispatches PARALLEL** (D1, D2, D3, D4, D5). No forward-reference dependencies; the only shared surfaces (`concepts/index.md` alpha table + `SUMMARY.md` concepts block; `L1/index.md` dep-map) take distinct alpha-position row inserts with no consolidated tally, so they are parallel-safe per the conflict-tolerance philosophy. D1 owns the one-time `record` Kind-legend line in `concepts/index.md` (stated partition). Then the standard tail: 5 critics → repairers as needed → `integrator-per-report` ×(ready) serially → ONE `integrator-finalize`.

## Open questions / caveats

- **Record-page Kind value.** I propose a new `record` Kind in the `concepts/index.md` legend for the directive-2 record-definition pages (distinct from `primitive`/`layer-pattern`/`methodology`/`algorithm`/`auxiliary`). If the meta-phase prefers folding them under `layer-pattern`, that is a cheap re-label; flagging for the batch-24 meta-phase to ratify the `record` Kind (a small taxonomy addition consistent with the directive-2 obligation).
- **D5 unify-vs-mint is a genuine judgment call.** If `port_projection` factors cleanly through `bilinear-form`, the right output is a specialization NOTE (no new verb) — which would mean `sparameter_reduce`'s gate-b is satisfied by an EXISTING firm L1 entry + a note, not a new chapter. The dispatch is scoped to resolve this either way; the report should state the verdict explicitly so the c078 coupled-column re-check knows whether `port_projection` is a live slug.
- **Coupled-column promotions are NOT in this cycle.** D4/D5 firm the L1 gates; the actual `eigenfreq_qfactor_reduce` / `sparameter_reduce` rough-in→firm promotions are double-gated (L1 home firm AND a dedicated reduction test), and the eigenfrequency-qfactor / sparameters seed→promotion columns are coupled to those. When BOTH gates of a verb close (this cycle closes one gate each), the coupled-column re-check is a c078 or batch-24-meta candidate — surfaced here so it is not lost. I did NOT couple a re-anchor into D4/D5 (unlike the c045 floor-landing-implies-reanchor pattern) because the reduce-verb re-anchor is gated on the SECOND (test) gate, not merely the L1 home landing — re-anchoring now would assert a promotion that the test-gate has not cleared.
- **Energy-fields (#5) + boundary-mode (#6) columns stay deferred** this cycle (the record cohort + verb-firming fills the fan-out budget). They land directly into their by-kind groupings (output-product / driver-leaf, alpha-within-kind) when authored — c078 or batch-24 candidates.
