---
agent: cycle-planner
invoked_at: 2026-06-02T223001Z
scope: cycle-070 dispatch plan
status: pending
---

# Cycle 070 dispatch plan

FIRST primary cycle of meta-batch-22 (cycles 070/071/072; the batch-22 meta-phase fires after cycle-072's finalize). Session was restarted post-batch-21-meta, so the 4 edited agent-defs (meta-phase, integrator-per-report, integrator-finalize, layer-intro-author) are loaded.

## Goals selected this cycle

Push the batch-22 LEAD frontier (#1 `driven-solve-l4-lift`, HIGH) — author the driven pipeline's solve-half OWN single-witness L4 form, closing the last pipeline-half L4 gap so the whole assemble+solve deliverable reaches L4 — coupled with its L4>L3 dissolution theme. **In parallel**, seed the NEW co-equal standing goal (#6 `feature-surface-spine-seed`, MEDIUM-HIGH) by authoring the electrostatic exemplar feature column (L4+L1+L0 composition-root chapters), establishing the top-down composition-root spine pattern the batch-22 meta-phase will codify. Ride the two cheap LOW hygiene items (#3 L3 dot/nrm2 no-L4 re-anchor; #4 blackbox-page L4/fe_assemble link upgrade). **Defer #2 (directive-3 mdBook reorg)** to a later batch-22 cycle as its own dedicated structural wave (heavy `book/`-structure; convention already codified so interim landings stay alpha-correct — bundling it with this forward-frontier cycle would collide with the #1/#6 SUMMARY/index inserts). **#5 (`eliminate_*→L4`)** stays DEFERRED — its primitive-gate evidence is unchanged (the `apply_linop`/`axpy`/`set_essential` primitives don't all rise to L4 per the c069 gate-check).

## Deliverable-presence verification

Per the mandatory paste-inline-evidence procedure (CLAUDE.md / friction-ledger `cycle-planner-stale-priorities-line-recruitment` `escalating`). All commands run from repo root `/home/crutcher/git/palace_whiteroom`.

### D1 — `L4/frequency_sweep` (driven-solve L4 form): ABSENT (new authoring) ✓
```
$ ls book/src/L4/map_solve.md book/src/L4/frequency_sweep.md
ls: cannot access 'book/src/L4/map_solve.md': No such file or directory
ls: cannot access 'book/src/L4/frequency_sweep.md': No such file or directory
```
Both candidate slugs ABSENT — open by construction (new authoring). The per-ω operand it re-expresses through is PRESENT and firm:
```
$ ls book/src/L4/assemble_frequency_operator.md  →  exists
$ grep -A2 '^## Status' book/src/L4/assemble_frequency_operator.md
## Status
`firm` — the L4 form is the calculus-level rendering of the firm L1 [...]
```
Palace source confirmed via codemap (`drivensolver.cpp`): the per-ω loop assembles `A=GetSystemMatrix(1, iω, -ω², K,C,M,A2)` (`:175-177`), `ksp.SetOperators(*A,*P)` INSIDE the loop (`:180` — operator-VARYING, the `per-element` corner), `ksp.Mult(RHS,E)` (`:194`). (Priorities cites `:176-180`; on-disk confirms `SetOperators` at `:180`, solve at `:194` — producer to on-disk-confirm exact anchors.)

### D2 — `L4-L3/frequency-sweep-dissolution` (the L4>L3 lowering theme): ABSENT (new authoring) ✓
```
$ ls book/src/L4-L3/ | grep -iE 'freq|map.solve|sweep'
(no match)
```
No existing freq/map/sweep theme — open by construction. (Existing siblings for the pattern: `solve-family-map-dissolution.md` at SUMMARY `:32`, the fixed-operator analog this driven theme parallels.)

### D3 — electrostatic feature column (`L4`+`L1`+`L0` feature chapters): ABSENT (new authoring) ✓
```
$ ls book/src/L4/electrostatic*.md book/src/L1/electrostatic*.md book/src/L0/electrostatic*.md
(all: No such file or directory)
$ ls book/src/ | grep -iE 'feature|driver'   →  (no feature/driver Part dir yet)
```
All three feature-chapter slugs ABSENT — open by construction (new chapter kind). Constituent decomposed vocabulary it composes is ON DISK:
```
$ grep -A2 '^## Status' book/src/L4/fe_assemble.md     →  `firm`
$ grep -A2 '^## Status' book/src/L4/solve_family.md     →  `rough-in (test-coverage-bounded)` (fixed-operator capture; the electrostatic sweep IS this combinator's `fixed` corner)
```
Palace driver source confirmed via codemap (`electrostaticsolver.cpp`): `ElectrostaticSolver::Solve` = `:21-98`; assemble `K=GetStiffnessMatrix()` ONCE (`:30`); `KspSolver ksp` set once outside the loop; per-terminal-source loop varies only RHS (`GetExcitationVector` `:68`, `ksp.Mult` `:69`) — a FIXED-operator map (= `solve_family` `fixed`); capacitance output product `PostprocessTerminals` (`:95`, def `:100`). Clean composition-root: config→`fe_assemble`→`solve_family`(fixed)→capacitance-out.

### D4 — `l3-dot-nrm2-no-l4-reanchor` (lifter): PRESENT-and-stale ✓
```
$ grep -n 'no L4\|L4 entry' book/src/L3/dot.md
8:  - (none) — `dot` is a reduction specialization; no L4 entry exists [...]
107:`dot` has **no L4 entry** [...per the cycle-010 audit verdict...]
$ grep -n 'no L4\|L4 entry' book/src/L3/nrm2.md
8:  - (none) — `nrm2` is a leaf primitive; no L4 entry exists [...]
136:`nrm2` has **no L4 entry** [...]
```
Stale lines PRESENT on both files (the `L4/dot`/`L4/nrm2` firm entries rose c069). OQ open, not closed:
```
$ grep 'l3-dot-nrm2-stale-no-l4' scaffolding/open-questions.md
→ `l3-dot-nrm2-stale-no-l4-entry-lines-need-reanchor` (c069 D2) → plan [...] LOW fan-out, cheap hygiene.
```
Not RESOLVED/CLOSED — open. No structural block (identical thin routine c069 D3 already ran for the combinators).

### D5 — `blackbox-page-l4-fe-assemble-link-upgrade` (lifter): PRESENT-and-stale ✓
```
$ grep -n 'fe_assemble' book/src/concepts/black-box-vs-accelerated-kernels.md
69:  [`fe_assemble`](../L1/fe_assemble.md) — the element-local→global [...]
143:- [`fe_assemble`](../L1/fe_assemble.md) — the assemble fold (combinator, [...]
```
Both refs currently link the L1 cap; `L4/fe_assemble` (on disk since c068, firm) is the now-available upgrade target. OQ open:
```
$ grep 'l4-fe-assemble-absent-forward-ref-for-blackbox' scaffolding/open-questions.md
→ `l4-fe-assemble-absent-forward-ref-for-blackbox-kernel-page` (c067 D3) → plan [...] LOW fan-out / cosmetic.
```
Not closed — open. No structural block.

### STOP-PROPOSING negative-list check
No dispatch this cycle proposes any listed item (`lu_solve`/`back_solve`/`ls-update-column`/4 NLEPS atoms/`apply_nonlinear_pencil`-HELD/`polynomial_smoother`/`L3/solve_family`/`L2/fold_solve`/`L2/fe_assemble`/`weak_form_term` L2). **`map_solve` reconciliation honored:** D1 authors the DRIVEN feature's OWN single-witness L4 form (active-head #1, explicitly licensed by batch-21 meta decisions 2/4 under the completeness directive) — it does NOT author a shared generalized cross-pipeline `map_solve` combinator/parent. To keep clear of the barred shared-combinator term, the recommended slug is **`frequency_sweep`** (driven-specific, single-witness), with `map_solve` as the producer's warrant-first fallback name ONLY if the producer scopes it explicitly single-witness-driven (NOT shared/generalized). #5 (`eliminate_*`) not proposed (primitive-gated, evidence unchanged).

## Dispatches

**D1 — `harvester` — `L4/frequency_sweep` (driven-solve L4 form, the LEAD)**
- scope: Author `book/src/L4/frequency_sweep.md` — the driven pipeline's solve-half OWN single-witness L4 form: a per-ω **map over a frequency family where each member REBUILDS the operator** before solving (the operator-VARYING sweep, distinct from `solve_family`'s `fixed` capture-once map). Body re-expresses THROUGH the firm `L4/assemble_frequency_operator` as the per-ω operand (`A(ω)=K+iωC−ω²M`), then `ksp_solve` per member — replace-and-propagate, NOT a mirrored fold. L0 anchor: `palace/drivers/drivensolver.cpp` per-ω loop (`GetSystemMatrix` `:175-177` operand rebuild → `ksp.SetOperators` INSIDE the loop `:180` → `ksp.Mult` `:194`); **on-disk-confirm exact anchors (codemap hint; the `:180`/`:194` are the SetOperators/solve lines, priorities cited `:176-180`)**. **CANONICAL SLUG = `frequency_sweep`** (D2 forward-references this exact slug — `book/src/L4-L3/frequency-sweep-dissolution.md` is its dissolution theme, authored by D2 this cycle). Honor the reconciled STOP: this is the driven feature's OWN single-witness form — do NOT frame it as a shared generalized `map_solve` combinator/cross-pipeline parent. D1 is SOLE owner of the `L4/index.md` consolidated tally this cycle (bump L4 firm 13→14 + append its own alpha-positioned `frequency_sweep` row + bullet + SUMMARY alpha-insert).
- deps: none

**D2 — `abstractor` — `L4-L3/frequency-sweep-dissolution` (the coupled L4>L3 theme)**
- scope: Author `book/src/L4-L3/frequency-sweep-dissolution.md` — how the L4 `frequency_sweep` map dissolves into the L3/driver-level per-ω loop (each member: rebuild-the-operator-then-`ksp_solve` driver calls; the `SetOperators`-inside-the-loop operator-varying recurrence). Forward-references the L4 cap **canonical slug `frequency_sweep`** (`book/src/L4/frequency_sweep.md` — D1 authors it this cycle; cite by this exact slug, do NOT invent a variant). Parallels the existing fixed-operator sibling `book/src/L4-L3/solve-family-map-dissolution.md` (the `fixed`-corner analog). Appends its OWN `L4-L3/index.md` dep-map row + §cohort bullet + SUMMARY alpha-insert; does NOT touch the L4/index tally (D1 owns it).
- deps: D1 (forward-references D1's `frequency_sweep` slug; wave-2 so the per-report integrator wires a live link)

**D3 — `layer-intro-author` — `feature-surface-spine-seed`: electrostatic exemplar feature column (L4+L1+L0)**
- scope: Author the FIRST exemplar of the NEW composition-root **feature-surface** chapter kind (USER DIRECTIVE 2026-06-02, carried via this dispatch prompt until the batch-22 meta-phase codifies it). Author the **electrostatic simulation feature column** at three levels — `book/src/feature/electrostatic.L4.md`, `.L1.md`, `.L0.md` (producer picks the exact path/Part layout; a new `# Feature surfaces` Part is acceptable — integrator-per-report wires SUMMARY). A feature chapter is a NEW kind: **inputs = config**, **outputs = the physical product** (here the capacitance matrix), **body = the composition of the already-firm decomposed vocabulary at that level**, **links DOWN to constituent ops**. The composition root: config-in → `fe_assemble` (assemble `K` once, `GetStiffnessMatrix()`) → `solve_family` (`fixed` corner — the per-terminal-source RHS-varying map, operator captured once) → capacitance-matrix reduction (`PostprocessTerminals`) → capacitance-out. **L0 ground truth** = `ElectrostaticSolver::Solve` `palace/drivers/electrostaticsolver.cpp:21-98` (assemble `:30`; fixed-operator source loop `:60-90`, `ksp.Mult :69`; capacitance output `:95`/`:100`); **on-disk-confirm anchors**. **L1** = the pure-function feature (config→capacitance). **L4** = the composition-root presenting the feature as the outward backend-lowering entry point, links DOWN to firm `L4/fe_assemble` + `L4/solve_family`(rough-in, `fixed`). CRITIC-FRAMING NOTE (carry into the dispatch): the feature's "surface" check ADAPTS — the surface IS the feature, evidenced by the L0 driver-source range + the constituent-op links, NOT a single decomposed op. Lands in a NEW Part index (NOT `L4/index` — no tally conflict with D1).
- deps: none

**D4 — `lifter` — `l3-dot-nrm2-no-l4-reanchor` (LOW hygiene)**
- scope: Flip the now-stale "no L4 entry" lines to live links at the firm `L4/dot`/`L4/nrm2`: `book/src/L3/dot.md` (`:8` frontmatter line + `:107`) and `book/src/L3/nrm2.md` (`:8` + `:136`) — the identical thin routine c069 D3 ran for the combinators. Plus the matching `book/src/L3/index.md` BLAS-1-cohort "no-L4-by-design" per-case correction (the same correction `L4/index.md` already carries for these now-risen verbs). Preserve the cycle-010 superseded-reasoning as a `> Superseded` admission blockquote (per c069 D3 precedent). Closes OQ `l3-dot-nrm2-stale-no-l4-entry-lines-need-reanchor`.
- deps: none

**D5 — `lifter` — `blackbox-page-l4-fe-assemble-link-upgrade` (LOW cosmetic)**
- scope: Upgrade the two `concepts/black-box-vs-accelerated-kernels.md` refs (`:69` See-also/case-1 sibling + `:143`) from the L1 link to live-link the now-on-disk firm `L4/fe_assemble` (skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` / on-disk→live-link upgrade). Keep the L1 cap reference where the prose specifically means the L1 cap; add/redirect to `L4/fe_assemble` where the prose means the L4 feature surface. Closes OQ `l4-fe-assemble-absent-forward-ref-for-blackbox-kernel-page`.
- deps: none

## Overlap analysis

Pairwise (artifact-region / shared-operator-name test):

- **D1 × D2**: D2 forward-references D1's new slug `frequency_sweep`. Distinct files (`L4/frequency_sweep.md` vs `L4-L3/frequency-sweep-dissolution.md`). Shared index touches are DISTINCT (D1 → `L4/index.md` row+tally; D2 → `L4-L3/index.md` row) → non-overlapping at the operational level. The only true dependency is the forward-reference slug → D2 in wave-2 so the per-report integrator can wire a live link. Canonical slug stated in BOTH scopes (cross-report-forward-reference-slug-divergence convention). **Sequential (forward-ref ordering), not region-conflict.**
- **D1 × D3**: disjoint files. D3 links DOWN to `L4/fe_assemble`/`L4/solve_family` (read-only); does not name or modify `frequency_sweep`. D3 lands in a NEW Feature Part index (NOT `L4/index`), so no tally collision with D1's L4/index ownership. **PARALLEL.**
- **D1 × D4, D1 × D5**: fully disjoint (D4 = `L3/*` + `L3/index`; D5 = one concepts page). **PARALLEL.**
- **D2 × D3/D4/D5**: disjoint files; D2 touches `L4-L3/*` only. **PARALLEL.**
- **D3 × D4 × D5**: pairwise disjoint (`feature/*` new Part vs `L3/*` vs one concepts page). **PARALLEL.**
- **Shared-index count-owner:** only D1 writes an `L4/index.md` consolidated tally this cycle (13→14). D3's column lands in a new Feature Part index; D2/D4/D5 touch other indices. **No ≥2-parallel-into-one-consolidated-tally situation** → no count-owner partition needed beyond D1's sole L4/index ownership (stated in D1 scope). SUMMARY.md gains distinct lines from D1/D2/D3 — distinct alpha-positioned inserts, parallel-safe per the integrator's serial per-report re-read; interim alpha-local correctness holds (directive-3 reorg deferred).

## Sequencing schedule

- **Wave 1 (parallel):** D1, D3, D4, D5 — four independent forward-frontier + hygiene dispatches, no region conflicts, no forward-references among them.
- **Wave 2 (after D1's report lands):** D2 — forward-references D1's `frequency_sweep` slug; sequenced second so the per-report integrator wires a live link to the on-disk L4 cap. (Book is NOT rebuilt between waves; `integrator-finalize` runs ONCE at cycle end. Wave-2 is dispatch/forward-reference ordering only.)

5 dispatches total (well under the 12 cap). One `integrator-finalize` at cycle end.

## Open questions / caveats

- **#2 directive-3 mdBook reorg DEFERRED, not dropped.** It is the meta-phase-decided dedicated structural wave (batch-21 decision 5). Bundling a ~190-chapter-line by-kind regroup + global alpha re-sort with this cycle's 3 new-file SUMMARY/index inserts (D1/D2/D3) would maximize merge surface for no benefit (the alpha-insert convention is already codified into integrator-per-report + layer-intro-author, so D1/D2/D3 land alpha-correct in the current transitional state). Recommend scheduling it as the SOLE forward-frontier-free wave in cycle-071 or cycle-072. Flagging for the batch-22 meta-phase / next planner: it should fire before batch-22 closes so the book ships reorganized.
- **D3 feature-chapter kind is un-codified (carried by prompt).** The directive is carried into the D3 dispatch prompt, not yet in role-specs (that is the batch-22 meta-phase's job). If the D3 producer or critic balks at the new "surface = feature, not a single decomposed op" framing, that is itself a finding to route to the meta-phase (it will inform the codification). The recommended exemplar (electrostatic, the simplest fixed-operator pipeline) was chosen over the alternative top-level-lifecycle-root pick because the electrostatic column has a fully-firm/near-firm constituent set on disk (`fe_assemble` firm, `solve_family` rough-in-fixed-corner, capacitance output) and sets the per-pipeline pattern most cleanly; the lifecycle ROOT meta-feature is a strong cycle-071+ follow-on once the per-pipeline pattern exists to hang off it.
- **D3 path/Part layout left to producer.** A new `# Feature surfaces` (or `# Feature surfaces / entry points`) Part is the natural home (matches the directive-3 forthcoming kind). The producer picks the exact filename convention (`feature/electrostatic.{L4,L1,L0}.md` vs `feature/electrostatic/{L4,L1,L0}.md`); integrator-per-report wires SUMMARY. If the producer judges a single combined feature chapter (with L4/L1/L0 sections) cleaner than three files for the exemplar, that is acceptable and worth surfacing as a pattern note for the meta-phase.
- **`frequency_sweep` vs `map_solve` slug:** recommended `frequency_sweep` to stay clear of the negative-list `map_solve` term (which bars the SHARED generalized form). If the harvester's warrant-first analysis strongly prefers `map_solve`, it MUST scope it explicitly as the single-witness driven form (not shared/generalized) — but `frequency_sweep` is the safer canonical slug and is what D2 forward-references.
