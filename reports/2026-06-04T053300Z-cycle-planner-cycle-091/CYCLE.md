---
agent: cycle-planner
invoked_at: 2026-06-04T053300Z
scope: cycle-091 dispatch plan — the batch-29 LEAD matrix-weighted-norm-firm-flip-and-cascade-wave
status: pending
---

# Cycle 091 dispatch plan

## Goals selected this cycle

The single GO'd batch-29 LEAD: the **`matrix-weighted-norm-firm-flip-and-cascade-wave`** — a dedicated own-cycle structural wave (the cycle-071 reorg-wave precedent). The batch-28 meta-phase LICENSED the firm flip (both norm-axiom law-sides discharged c088 structure + c089 FP; gate (a) judged REDUNDANT under the firm-on-positive-structure escape, materially the same as `apply_linop`/`eigenfreq_qfactor_reduce`/`sparameter_reduce`/`solve_family`). This cycle: (1) flip the verb `rough-in (test-coverage-bounded)` → `firm`; (2) the whole-`book/src/` cross-reference re-anchor of every genuinely-stale `matrix-weighted-norm` maturity LABEL; (3) the coupled `gram_reduce`/`domain_energy_reduce` reduce-verb RE-JUDGMENTS (JUDGE, not force-firm); (4) the 5-of-6 stay-`seed` feature-column re-evaluations under the OWN-COMPOSITION rule. **No forward-frontier work this cycle** — the bottom-up width frontier is GATED behind this cascade and a rectangular pull-up is forbidden by the redirect.

## On-disk cascade-scope establishment (the critical pre-dispatch work)

Run on disk; pasted-evidence below. **The cascade is NUANCED — not a blanket flip.** The `grep -rn 'matrix-weighted-norm' book/src` returns **56 files**; the subset carrying a genuine `matrix-weighted-norm` MATURITY LABEL (the thing that flips) is **~26 files** (precise per-cluster checklist below). The rest are navigational links (e.g. `SUMMARY.md:178/:238` are pure TOC links — NO maturity token, NOT touched) or co-mentions of OTHER operators' rough-in labels.

**THREE reference-classes the producers must distinguish (load-bearing):**
- **(FLIP)** a `matrix-weighted-norm` ... `rough-in (test-coverage-bounded)` maturity label → re-anchor to `firm`.
- **(KEEP — DO NOT TOUCH)** a reference to the L1>L0 THEME `matrix-weighted-norm-mutation-rotation` (own `## Status` already `firm` on disk, `:432`, verified) — these are firm and must NOT be touched. Also the `bilinear-form` `rough-in` label co-mentioned on the same line (bilinear-form STAYS rough-in — see D3) must be PRESERVED.
- **(JUDGE)** a co-mention line that asserts BOTH `matrix-weighted-norm` rough-in AND `bilinear-form` rough-in (e.g. `gram_reduce`/`L0/linalg-operator-file.md:73`/`L4/index.md:102`): surgically re-anchor ONLY the matrix-weighted-norm half, leave the bilinear-form half rough-in. And lines that assert a DOWNSTREAM verb/column is rough-in *because* it folds matrix-weighted-norm (`gram_reduce`, `domain_energy_reduce`, energy-fields column) — the matrix-weighted-norm label flips, but whether the downstream's OWN status flips is D3/D4's judgment, NOT a mechanical re-anchor.

### Pasted evidence

```
# verb file exists + still rough-in on disk (GENUINELY OPEN — the flip has not happened):
-rw-rw-r-- book/src/L1/matrix-weighted-norm.md   (36069 bytes)
:110  `rough-in (test-coverage-bounded)` — signature and algebraic laws are well-anchored...
# verb has NO `firmness:` YAML field — maturity lives in the ## Status body line :110 (frontmatter has consumes/variant_axes only)

# L1>L0 theme own status — FIRM (must NOT be touched):
book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:432  ## Status → `firm`

# bilinear-form OWN status — STAYS rough-in (the gram_reduce residual gate):
book/src/L1/bilinear-form.md:4  firmness: rough-in
book/src/L1/bilinear-form.md:321  `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`

# gram_reduce folds matrix-weighted-norm (flips) AND bilinear-form (STAYS rough-in):
book/src/L4/gram_reduce.md:4  firmness: rough-in (test-coverage-bounded)
book/src/L4/gram_reduce.md:7  bilinear-form.md (rough-in — the off-diagonal cross-bilinear; the fold element)
book/src/L4/gram_reduce.md:235-236  the per-entry building blocks ... are themselves rough-in
  → RESIDUAL GATE: bilinear-form stays rough-in → gram_reduce STAYS rough-in (PREDICTION)

# domain_energy_reduce folds matrix-weighted-norm (flips) + participation_ratio (firm):
book/src/L4/domain_energy_reduce.md:4  firmness: rough-in
book/src/L4/domain_energy_reduce.md:3  participation_ratio.md (firm — second folded primitive)
book/src/L4/domain_energy_reduce.md:7  matrix-weighted-norm.md (rough-in — first folded; maturity INHERITED)
book/src/L4/domain_energy_reduce.md:274-289  gate (a) = matrix-weighted-norm rough-in (CLEARS this cycle);
  gate (b) = no per-domain test BUT "dischargeable in write-scope by a lowering-verifier pass raising
  map-law confidence to inner_product-equivalent (batch-24 meta-phase ruling)"
  → JUDGE: domain_energy_reduce MAY firm IF D3 discharges gate (b) (both folded primitives then firm,
    firm-on-positive-structure escape applies); else stays rough-in cleanly.

# L1/index.md count headers (pre-anticipated by the c080 count-reconciliation note):
book/src/L1/index.md:31  Firm (30 main cohort; 37 firm grand total) — "IF D1 promotes matrix-weighted-norm
  rough-in→firm, fold +1 into BOTH (30→31) and grand total (37→38), move its bullet to the firm sub-list"
book/src/L1/index.md:66  - [matrix-weighted-norm] ... Rough-in status motivated by absence of dedicated test...
book/src/L1/index.md:117  | matrix-weighted-norm | ... | dot, apply_linop | rough-in (test-coverage-bounded, ...) |

# L4/index.md headers:
book/src/L4/index.md:57  Rough-in at L4 (1) — domain_energy_reduce (gated on matrix-weighted-norm rough-in...)
  → IF D3 firms domain_energy_reduce, this becomes "Rough-in at L4 (0)" + move the bullet to firm cohort
book/src/L4/index.md:98/:102  domain_energy_reduce + gram_reduce dep-map rows fold "(rough-in) matrix-weighted-norm"

# feature columns own-status — all 5 seed on disk; lifecycle already firm (NOT in scope):
feature/electrostatic.L4.md:5  status: seed   (own gate: gram_reduce — STAYS seed)
feature/magnetostatic.L4.md:5  status: seed   (own gate: gram_reduce — STAYS seed)
feature/capacitance.L4.md:5   status: seed   (own verb gram_reduce — STAYS seed)
feature/inductance.L4.md:5    status: seed   (own verb gram_reduce — STAYS seed)
feature/energy-fields.L4.md:5 status: seed   (own verb domain_energy_reduce — FLIPS IFF D3 firms it)
feature/lifecycle.L4.md:5     status: firm   (already firm c085 — NOT in cascade scope)

# SUMMARY.md — pure TOC links, NO maturity tokens → NO SUMMARY change needed:
book/src/SUMMARY.md:178  - [matrix-weighted-norm](./L1/matrix-weighted-norm.md)
book/src/SUMMARY.md:238  - [matrix-weighted-norm-mutation-rotation](...)
```

### The genuine maturity-label re-anchor checklist (~26 files, partitioned by dispatch)

**D1 — verb own file + the two layer-index count-owner files (SOLE owner of L1/index + L4/index):**
- `book/src/L1/matrix-weighted-norm.md` — `## Status:110` flip → `firm`; the gate-redundant disposition prose at `:115`/`:116`/`:176` (the "sole remaining gate (a) ... LICENSES a future full-firm flip" → restate as enacted-firm); the OQ-partial note `:117`. (frontmatter: no `firmness:` field to flip — maturity is the `## Status` line.)
- `book/src/L1/index.md` — `:31` count header (30→31 main, 37→38 grand; fold the pre-staged c080 reconciliation note, remove it as discharged); `:66` bullet (re-anchor + move to the firm sub-list); `:117` dep-map row maturity cell → `firm`; `:101` OQ-partial note.
- `book/src/L4/index.md` — `:57` "Rough-in at L4 (1)" header (IFF D3 firms domain_energy_reduce → "(0)" + move bullet to firm cohort `:32`; ELSE keep "(1)" and re-anchor ONLY the matrix-weighted-norm-folded-primitive label inside it); `:59`/`:98`/`:102` dep-map rows — re-anchor the `(rough-in) matrix-weighted-norm` folded-primitive labels to `firm`, KEEP gram_reduce's bilinear-form rough-in. **D1 coordinates the L4/index domain_energy_reduce header with D3's verdict (wave-2 ordering).**

**D2 — vocabulary-spine + L0 + L1-L0-theme consumer cross-reference re-anchor cluster (NO index/feature/reduce-verb-status writes):**
- `book/src/L1/normalize.md` — `:40`-ish + `:83-95` `normalize_B` "inherits matrix-weighted-norm's test-coverage bound" (JUDGE: the inherited bound is now LIFTED — re-narrate, the `normalize_B` note no longer cites a rough-in norm constituent; `normalize` itself stays firm).
- `book/src/L2/normalize.md` `:41`,`:112` — same `normalize_B` inherited-bound re-narration.
- `book/src/L3/normalize.md`, `book/src/L3/nrm2.md`, `book/src/L3/index.md` — re-anchor the matrix-weighted-norm rough-in co-mention labels; `L3/index.md`'s "rough-in at L1; do NOT dispatch" guidance is now stale (the verb firmed) — update.
- `book/src/L1/blas1-elementwise-intro.md`, `book/src/L1/chebyshev-smoother.md` — re-anchor matrix-weighted-norm rough-in labels if present.
- `book/src/L0/linalg-operator-file.md:73`,`:88` — JUDGE: `:73` says "Both are now harvested at L1 (... `rough-in`)" covering matrix-weighted-norm AND bilinear-form → split: matrix-weighted-norm firm, bilinear-form stays rough-in.
- `book/src/L0/mpi-globalsum-and-collectives.md` — re-anchor if a maturity label present.
- `book/src/L1-L0/normalize-mutation-rotation.md:305`, `book/src/L1-L0/bilinear-form-mutation-rotation.md:575`, `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:26`, `book/src/L1-L0/index.md` — re-anchor the prose "rough-in matrix-weighted-norm" REFERENCES. **DO NOT touch these theme files' own `## Status` (firm).**
- `book/src/L1/bilinear-form.md:253` — OQ-slug reference (`matrix-weighted-norm-and-bilinear-form-l1-rough-ins`); the matrix-weighted-norm half is now resolved — update the joint-OQ narration, bilinear-form half stays open.
- **D2 explicitly does NOT touch:** `book/src/methodology/goal-flow.md` (meta-phase-owned chapter — flag any stale matrix-weighted-norm rough-in ref at `:N` as an OQ-intake note for the batch-29 meta-phase, do NOT edit it).

**D3 — the two coupled reduce-verb RE-JUDGMENTS (lowering-verifier; touches gram_reduce.md + domain_energy_reduce.md own-status ONLY):**
- `book/src/L4/gram_reduce.md` — re-judge: matrix-weighted-norm now firm, but bilinear-form (the off-diagonal fold element) STAYS `rough-in`. **PREDICTION: STAYS `rough-in (test-coverage-bounded)`** — record the residual gate cleanly (one gate discharged, bilinear-form gate remains). Re-anchor the matrix-weighted-norm folded-primitive labels (`:6`,`:55`,`:195`,`:235`,`:242`) to firm; KEEP bilinear-form rough-in. Update the §Status promotion-route to "matrix-weighted-norm firmed c091; remaining gate = bilinear-form + dedicated Gram test."
- `book/src/L4/domain_energy_reduce.md` — re-judge: both folded primitives now potentially firm (matrix-weighted-norm flips + participation_ratio firm). Gate (a) clears; **JUDGE gate (b)** (the per-domain map-law confidence) via the in-scope route the §Status names (`:287-289`, the batch-24 ruling: a lowering-verifier pass raising map-law confidence to `inner_product`-equivalent CITING the existing `test-domainpostoperator.cpp:75-93` postprocess coverage). **TWO clean outcomes:** (a) DISCHARGE → flip `domain_energy_reduce` `rough-in` → `firm` + `verified_against:` block (this firms the energy-fields column's own reduce verb → D4 flips energy-fields); (b) CONFIRM-CEILING → stays `rough-in` with an explicit verdict (gate (a) cleared, gate (b) needs a per-domain test the corpus lacks) → energy-fields STAYS seed. NOT a forcing — the honest verdict is the finding.

**D4 — feature-column re-evaluations (layer-intro-author; SOLE owner of feature/index.md + the feature-Part §Vocabulary/SUMMARY block):**
- Re-anchor the matrix-weighted-norm rough-in labels across the 15 feature files (electrostatic/magnetostatic/capacitance/inductance/energy-fields × {L0,L1,L4} + output-product.md) to firm.
- **Column flips (per-column OWN-COMPOSITION judgment from on-disk constituent status):**
  - `electrostatic`/`magnetostatic` — own gate `gram_reduce` (D3 predicts STAYS rough-in) → **STAY seed**; re-narrate the own-constituent gate to "`gram_reduce` rough-in (residual `bilinear-form` gate)."
  - `capacitance`/`inductance` — own verb `gram_reduce` rough-in → **STAY seed**; same re-narration.
  - `energy-fields` — own verb `domain_energy_reduce`: **FLIP `seed`→`firm` IFF D3 returns outcome (a) DISCHARGE; else STAY seed.** (Wave-2: D4 reads D3's verdict.)
- D4 runs the whole-`book/src/feature/` sibling-status grep coupled to any column flip (the `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` discipline) and owns `feature/index.md` `:55`,`:67-70` (the cohort status prose + the seed-column gate narration) + the `## Chapter-kind status` block.

## Deliverable-presence verification (per-dispatch, paste-inline-evidence)

**This is a meta-phase-routed GO enactment (the batch-29 LEAD) — the cascade is open by construction** (the firm flip has NOT happened; the verb is `rough-in` on disk `:110`, pasted above). The four-step check confirms genuine-openness:

| Dispatch | (1) file exists | (2) maturity on disk | (3) OQ RESOLVED-grep | (4) structural-gate |
|---|---|---|---|---|
| D1 verb flip | `ls` → `book/src/L1/matrix-weighted-norm.md` EXISTS (36069 B) | `:110` `rough-in (test-coverage-bounded)` — NOT yet firm → flip is a real change | OQ `matrix-weighted-norm-firm-flip-and-cascade-wave` is OPEN/migrated-to-plan (NOT closed) — `open-questions.md:10` records GO-licensed, NOT enacted | gate (a) judged REDUNDANT by batch-28 meta-phase → firm-on-positive-structure escape APPLIES → no structural block. OPEN. |
| D2 re-anchor | target files exist (grep-enumerated above) | consumers carry stale `rough-in` matrix-weighted-norm labels (pasted checklist) — current-on-disk, go stale ON the D1 flip | n/a (re-anchor coupled to the flip) | none — mechanical/surgical prose re-anchor. OPEN. |
| D3 reduce-verbs | `gram_reduce.md` + `domain_energy_reduce.md` EXIST | gram_reduce `:4` rough-in; domain_energy_reduce `:4` rough-in | the reduce-verb re-judgment OQ is OPEN (coupled to the cascade) | gram_reduce structurally BLOCKED by bilinear-form (residual gate — predicted STAY); domain_energy_reduce gate (b) dischargeable in-scope (batch-24 ruling) — JUDGE. OPEN. |
| D4 columns | 15 feature files + `feature/index.md` EXIST | 5 columns `status: seed` on disk (pasted) | column-flip OQ OPEN (coupled) | electrostatic/magnetostatic/capacitance/inductance structurally gated on gram_reduce (predicted STAY seed); energy-fields gated on D3's domain_energy_reduce verdict. OPEN. |

**STOP-PROPOSING negative-list check:** none of `lu_solve`/`back_solve`/`ls-update-column`/`nleps_*` appear in any dispatch scope. PASS.

## Dispatches

1. **(harvester) D1 — verb flip + L1/index + L4/index count-owner.** Scope: flip `book/src/L1/matrix-weighted-norm.md` `## Status:110` `rough-in (test-coverage-bounded)` → `firm`, restating the gate-redundant disposition prose (`:115`/`:116`/`:176`/`:117`) as enacted (both law-sides discharged c088+c089, gate (a) redundant per the batch-28 meta-phase GO — the firm-on-positive-structure escape, materially the `apply_linop`/`eigenfreq_qfactor_reduce`/`sparameter_reduce`/`solve_family` precedent). SOLE owner of the two layer-index count-owner files: `book/src/L1/index.md` (`:31` count 30→31 main / 37→38 grand, discharge the pre-staged c080 reconciliation note; `:66` bullet move to firm sub-list; `:117` dep-map cell → firm; `:101` OQ-partial) and `book/src/L4/index.md` (`:59`/`:98`/`:102` re-anchor the matrix-weighted-norm folded-primitive labels to firm, KEEP gram_reduce's bilinear-form rough-in; the `:57` "Rough-in at L4 (N)" header is coordinated with D3's domain_energy_reduce verdict — wave-2). **rationale:** the LEAD — the firm flip itself + the count headers (the c087 solve_family count-header precedent). HARD: do NOT touch the L1>L0 theme (firm); do NOT touch any feature column or reduce-verb own-status (D3/D4 own those).

2. **(lifter) D2 — vocabulary-spine + L0 + L1-L0-theme consumer re-anchor cluster.** Scope: re-anchor the stale `matrix-weighted-norm` rough-in maturity LABELS in `book/src/L1/normalize.md`, `book/src/L2/normalize.md`, `book/src/L3/normalize.md`, `book/src/L3/nrm2.md`, `book/src/L3/index.md`, `book/src/L1/blas1-elementwise-intro.md`, `book/src/L1/chebyshev-smoother.md`, `book/src/L0/linalg-operator-file.md` (`:73`/`:88` — split the joint matrix-weighted-norm/bilinear-form rough-in claim, KEEP bilinear-form rough-in), `book/src/L0/mpi-globalsum-and-collectives.md`, `book/src/L1-L0/normalize-mutation-rotation.md:305`, `book/src/L1-L0/bilinear-form-mutation-rotation.md:575`, `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:26`, `book/src/L1-L0/index.md`, `book/src/L1/bilinear-form.md:253` (joint-OQ narration — matrix-weighted-norm half resolved, bilinear-form half open). JUDGE the `normalize_B` inherited-bound prose (now LIFTED). **HARD: do NOT touch any L1-L0 theme's own `## Status` (firm); do NOT touch `book/src/methodology/goal-flow.md` (meta-phase-owned — flag stale refs as an OQ-intake note); do NOT touch index/feature/reduce-verb files (D1/D3/D4 own those); PRESERVE every bilinear-form rough-in label.** **rationale:** the consumer cross-reference re-anchor mandated by `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` — the first ~30-file-scale exercise of the operator-side grep discipline.

3. **(lowering-verifier) D3 — the two coupled reduce-verb re-judgments.** Scope: re-judge `book/src/L4/gram_reduce.md` (PREDICT: STAYS `rough-in (test-coverage-bounded)` — bilinear-form residual gate; re-anchor the matrix-weighted-norm folded-primitive labels `:6`/`:55`/`:195`/`:235`/`:242` to firm, KEEP bilinear-form rough-in, update §Status promotion-route to the narrowed gate) and `book/src/L4/domain_energy_reduce.md` (JUDGE: gate (a) clears with the matrix-weighted-norm firm flip; discharge gate (b) — the per-domain map-law confidence — via the in-scope batch-24-ruled route (`:287-289`, a lowering-verifier pass raising map-law confidence to `inner_product`-equivalent CITING `test-domainpostoperator.cpp:75-93`); outcome (a) DISCHARGE → flip → `firm` + `verified_against:` block; outcome (b) CONFIRM-CEILING → stays `rough-in` with explicit verdict). **HARD: touch ONLY these two reduce-verb files' own status/prose; do NOT touch matrix-weighted-norm.md, the indexes, or any feature column. Record the gram_reduce residual gate as the HONEST outcome (not a forcing).** **rationale:** the coupled downstream reduce-verb re-checks; the firm flip clears the matrix-weighted-norm gate but the redirect's honesty constraint requires JUDGE-not-force (gram_reduce's bilinear-form gate is the load-bearing finding). **deps: D1 (reads the firmed matrix-weighted-norm state) — wave-2.**

4. **(layer-intro-author) D4 — feature-column re-evaluations + SOLE owner of feature/index.md.** Scope: re-anchor the matrix-weighted-norm rough-in labels across the 15 feature files (electrostatic/magnetostatic/capacitance/inductance/energy-fields × {L0,L1,L4} + `output-product.md`) to firm; per-column OWN-COMPOSITION judgment: electrostatic/magnetostatic/capacitance/inductance STAY seed (own gate `gram_reduce` rough-in per D3 — re-narrate to the narrowed `gram_reduce`/`bilinear-form` gate); energy-fields FLIP `seed`→`firm` IFF D3 returns outcome (a) DISCHARGE on domain_energy_reduce, ELSE STAY seed. SOLE owner of `book/src/feature/index.md` (`:55`,`:67-70` cohort/gate prose + `## Chapter-kind status`); run the whole-`book/src/feature/` sibling-status grep coupled to any flip. **HARD: do NOT touch the L1/L4 indexes (D1) or the reduce-verb files (D3); the column flip for energy-fields is conditional on D3's on-disk verdict.** **rationale:** the convergent column re-evaluation — the visible payload (does the cascade unblock any stay-seed column?). **deps: D1 (firmed verb state) + D3 (domain_energy_reduce verdict gates energy-fields) — wave-2.**

## Overlap analysis

| Pair | Overlap? | Disposition |
|---|---|---|
| D1 ∩ D2 | D1 owns `L1/index.md` + `L4/index.md` + `matrix-weighted-norm.md`; D2 owns vocabulary-spine/L0/L1-L0-theme files. **D2 does NOT touch any index** (the L3/index, L1-L0/index it touches are DIFFERENT files from L1/index, L4/index — distinct files, no byte overlap). NO shared file. | **PARALLEL-safe**, but D2 reads the firmed verb → wave-2 by dependency ordering (not byte conflict). |
| D1 ∩ D3 | D1 owns `L4/index.md` (which carries domain_energy_reduce's `:57` cohort header + the gram_reduce/domain_energy_reduce dep-map rows `:98`/`:102`); D3 owns the reduce-verb CHAPTER files `gram_reduce.md`/`domain_energy_reduce.md`. **Different files.** BUT D1's `L4/index.md:57` header depends on D3's domain_energy_reduce verdict (firm→"(0)" vs stay→"(1)"). | **Sequential by dep:** D3 verdict feeds D1's L4/index header. D1 applies the L4/index header AFTER D3's verdict is known (per-report integration serializes; D1 scoped to read D3's outcome). Distinct files → integrator applies in sequence cleanly. |
| D1 ∩ D4 | D1 owns L1/L4 indexes; D4 owns `feature/index.md` + feature column files. **Different files, no overlap.** | **PARALLEL-safe** (wave-2 by dep — D4 reads firmed verb). |
| D2 ∩ D3 | D2 = vocabulary-spine/L0/theme; D3 = reduce-verb chapters. No shared file. | **PARALLEL.** |
| D2 ∩ D4 | D2 = vocabulary-spine/L0/theme; D4 = feature files. No shared file. | **PARALLEL.** |
| D3 ∩ D4 | D3 = reduce-verb chapters; D4 = feature columns + feature/index. **Different files.** BUT D4's energy-fields flip DEPENDS on D3's domain_energy_reduce verdict (data dependency, not byte overlap). | **Sequential by dep:** D3 → D4 (D4 reads D3's verdict). Distinct files → integrator serializes cleanly. |

**No two dispatches modify the same file region or rewrite the same theme body.** The only cross-dispatch couplings are DATA dependencies (D3's reduce-verb verdicts feed D1's L4/index header + D4's energy-fields flip), handled by wave ordering, not byte conflict.

## Single-index-owner assignments (load-bearing)

- **`book/src/L1/index.md`** (count header `:31` + dep-map `:117` + bullet `:66`) → **D1 SOLE owner.** No other dispatch touches it.
- **`book/src/L4/index.md`** (cohort header `:57` + dep-map `:98`/`:102`) → **D1 SOLE owner** (coordinates the domain_energy_reduce header with D3's verdict).
- **`book/src/feature/index.md`** (cohort/gate prose + Chapter-kind status) → **D4 SOLE owner.**
- **`book/src/SUMMARY.md`** — pure TOC links, NO maturity tokens → **NO dispatch touches it** (no change needed).
- **`book/src/methodology/goal-flow.md`** — meta-phase-owned → **NO dispatch edits it** (D2 flags stale refs as OQ-intake for the batch-29 meta-phase).
- **L1 firm count** (30→31 main, 37→38 grand) → **D1 SOLE owner** (the pre-staged c080 reconciliation note is now discharged).

## Sequencing schedule

- **Wave 1 (parallel): D1, D2.** D1 flips the verb + the two index count-owners (deferring ONLY the `L4/index.md:57` domain_energy_reduce header line to coordinate with D3); D2 re-anchors the vocabulary-spine/L0/theme consumer cluster. These touch fully disjoint files. (D2 reads the firmed verb conceptually but does not byte-depend on D1's writes — both can author in parallel; the integrator applies D1 first by ordinal.)
- **Wave 2 (parallel after wave-1 reports land): D3, D4.** D3 re-judges the two reduce-verbs (reads the firmed matrix-weighted-norm); D4 re-evaluates the columns (reads the firmed verb + D3's domain_energy_reduce verdict for the energy-fields flip). D3 and D4 touch disjoint files (reduce-verb chapters vs feature files); D4's energy-fields decision is a data-read of D3's verdict, handled by dispatching D3 and D4 in the same wave with D4 instructed to read D3's on-disk verdict (per-report integration serializes the writes; the integrator applies D3 before D4 by ordinal so D4 reads the firmed/stayed domain_energy_reduce state).

Per-report integration applies serially in ordinal order D1→D2→D3→D4, then ONE `integrator-finalize` rebuilds + commits. The wave structure is forward-reference/data-dependency ordering, NOT multiple finalizes.

## On-disk predictions (the honest cascade outcome)

- **`matrix-weighted-norm`** → **FLIPS firm** (the GO; both law-sides discharged, gate (a) redundant).
- **`gram_reduce`** → **STAYS `rough-in (test-coverage-bounded)`** — residual gate `bilinear-form` (still rough-in on disk `:4`/`:321`). One gate discharged (matrix-weighted-norm firm), one remains. The HONEST partial outcome, not a forcing.
- **`domain_energy_reduce`** → **JUDGE (likely FIRMABLE this cycle)** — gate (a) clears; gate (b) is dischargeable in-scope per the batch-24 ruling (a map-law-confidence pass citing `test-domainpostoperator.cpp:75-93`). Predict outcome (a) DISCHARGE → firm; but D3 makes the on-disk call — if the per-domain map-law confidence does NOT cleanly reach `inner_product`-equivalent, it stays rough-in (clean ceiling).
- **`electrostatic`/`magnetostatic`/`capacitance`/`inductance` columns** → **STAY seed** (own gate `gram_reduce`, which stays rough-in).
- **`energy-fields` column** → **FLIPS firm IFF D3 firms domain_energy_reduce** (its own reduce verb is then firm + participation_ratio firm + matrix-weighted-norm firm = OWN composition all-firm). Predict FLIP, conditional on D3.
- **Cascade file count:** ~26 files carry genuine matrix-weighted-norm maturity labels (verb 1 + L1/index + L4/index + ~11 vocabulary-spine/L0/theme [D2] + 2 reduce-verbs [D3] + ~16 feature files [D4, incl. the index]); SUMMARY + goal-flow NOT touched by dispatches.

## Open questions / caveats

- **gram_reduce honesty (the central redirect-discipline test):** the meta-phase GO scope names "re-judge whether gram_reduce can now firm," but on disk gram_reduce folds STILL-rough-in `bilinear-form`. D3 must record the residual-gate partial outcome cleanly (NOT force-firm). If a future cycle wants the full electrostatic/magnetostatic/capacitance/inductance unblock, the next gate is `bilinear-form` firming (its own `rough-in (lower-layer-shared-vocabulary, cycle-010)` status — a separate dischargeability question, NOT in this cycle's scope). I have NOT added it as a fresh candidate this cycle — it is the natural batch-29 forward-frontier follow-up the meta-phase will see surface from D3's verdict.
- **domain_energy_reduce gate (b) is a genuine JUDGE, not a foregone flip:** I predict firmable (the §Status itself flags the in-scope route), but D3 owns the on-disk call. If it stays rough-in, energy-fields STAYS seed and the cascade firms ONLY the verb + gram_reduce-residual-gate-recorded — still a clean, honest landing.
- **`book/src/methodology/goal-flow.md`** carries matrix-weighted-norm rough-in references (`:N`) that go stale on the flip, but it is meta-phase-owned. D2 flags them as an OQ-intake note; the batch-29 meta-phase refreshes goal-flow at batch close. Flagging here so it is not lost.
- **The `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` discipline is exercised at ~30-file scale for the first time this cycle** (the meta-phase batch-29 watch-note). If any consumer label is missed by the D2/D4 clusters, it surfaces as a c092 land-clean residue (the c087 solve_family precedent) — acceptable, but the per-cluster checklists above are scoped to minimize it.
