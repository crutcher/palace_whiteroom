---
agent: cycle-planner
invoked_at: 2026-06-04T204023Z
scope: cycle-095 dispatch plan
status: pending
---

# Cycle 095 dispatch plan

## Goals selected this cycle

Cycle-095 = the GRADED-STACK campaign's **P1 launch (incremental edge-typing audit)** + the **bilinear-form firm-flip-and-cascade-wave (priorities item-1)**, sequenced as ONE composed cycle. Per the 2026-06-04 user decision (`scaffolding/decisions/2026-06-04-graded-stack-p1-edge-home.md`): per-chapter `edges:` frontmatter, **incremental** — type the feature-root closure + high-fan-out frontier FIRST, lazy tail, linters warn-not-fail; rank invariant a HARD gate for NEW work; pre-existing violations → a tracked baseline-exception set, NOT open-ended fix-forward. The bilinear-form cascade (DISCHARGE landed c092; verb still `rough-in` on disk) is the **rank linter's first live validation** and composes naturally with frontier-first typing: it discharges exactly **10 of the 22** linter rank violations (the bilinear-form/gram_reduce/4-column chain). The cascade lands FIRST (waves 1-2); the P1 frontier-typing pass reads the **post-cascade firm state** (wave 3) and opens the baseline-exception set for the residual violations. **Both fit one cycle** (7 dispatches, well under 12) because the cascade is pure execution (the c091 4-dispatch template) and the typing pass is bounded to the feature-root closure + high-fan-out frontier (NOT the whole 357-file artifact).

## Deliverable-presence verification

Per `.claude/agents/cycle-planner.md` (paste-inline-evidence; STOP-PROPOSING negative-list scan; four-step sequence per named-artifact-slug scope).

**D1–D4 (bilinear-form cascade) — the cascade is OPEN on disk (verb un-flipped, columns seed, gram_reduce rough-in):**

```
$ ls book/src/L1/bilinear-form.md && grep -m1 'firmness:' book/src/L1/bilinear-form.md
book/src/L1/bilinear-form.md
firmness: rough-in                         # OPEN — the verb is still rough-in; c092 DISCHARGE landed only a verified_against: block + §Status narration, NOT the flip
$ grep -m1 '`rough-in|`firm' book/src/L4/gram_reduce.md
`rough-in (test-coverage-bounded)`.        # OPEN — gram_reduce un-firmed; its SOLE residual gate (bilinear-form) clears on the flip
$ for c in capacitance inductance electrostatic magnetostatic; do grep -m1 '^status:' book/src/feature/$c.L1.md; done
status: seed                               # capacitance.L1  — OPEN (seed)
status: seed                               # inductance.L1   — OPEN (seed)
status: seed                               # electrostatic.L1 — OPEN (seed)
status: seed                               # magnetostatic.L1 — OPEN (seed)
```

Step-2 maturity: verb at `rough-in` (the flip target is `firm`; dispatch is NOT a no-op). Step-3 OQ-RESOLVED grep: `bilinear-form-firm-flip-and-cascade-wave` was **MIGRATED to the plan as the batch-30 LEAD** (open-questions.md "Last unified 2026-06-04" line), NOT marked RESOLVED/CLOSED — OPEN. Step-4 structural-block: the firm-on-positive-structure escape APPLIES (c092 DISCHARGE on disk, `verified_against:` block present) — the gate is **discharged**, the flip is licensed. NOT on the STOP-PROPOSING negative list (`bilinear-form` is not `lu_solve`/`back_solve`/`ls-update-column`/the nleps-4/`assemble-diagonal`). Framing: dedicated structural cascade wave (the c091 template), correct.

**D5–D7 (P1 edge-typing + baseline-exceptions) — OPEN BY CONSTRUCTION (the scheme + linters just landed c094; no prior P1 typing pass):**

```
$ grep -rln '^rank:'  book/src/      # only the scheme page (which is OUTSIDE the DAG, §2d) carries it
book/src/methodology/graded-stack-scheme.md
$ grep -rln '^edges:' book/src/
book/src/methodology/graded-stack-scheme.md   # ditto — the example in the scheme page
$ grep -rln '^feature_root:' book/src/feature/ | wc -l
0                                              # NO feature column carries the feature_root: split yet (transitional status: seed only)
$ ls scaffolding/graded-stack-baseline-exceptions.md 2>&1
ls: cannot access '...': No such file or directory   # ABSENT — open by construction
```

P1 is open by construction: the `edges:`/`rank:`/`feature_root:` adoption is 0 on every DAG node (the only carrier is the scheme page's own grammar example, which is outside the DAG). The baseline-exception file does not exist. No prior-cycle P1 history. These are first-landing dispatches against a brand-new convention — skip the maturity/OQ steps (explicit: open by construction, no prior-cycle history).

## Key on-disk finding driving the plan (the typing pass is MORE valuable than the raw violation count suggests)

The c094-finalize baseline linter run reports `rank_violations=22`. Partitioning them (paste below) shows **10 are the bilinear-form cascade** (discharged by D1–D4) and **12 are "residual"** — BUT the linter reads each edge's dep-rank from the **stale `composes:` qualifier string / prose dep-map**, NOT from the dep's own current `## Status`/frontmatter. Several residual "violations" are therefore **stale-edge false positives** that the P1 re-typing clears (because a typed `edges: depends-on:` edge carries NO restated maturity — the dep's rank is read from the dep's OWN frontmatter, per scheme §4(c) "the index-cell-drift lesson"):

```
=== CASCADE-DISCHARGED (D1–D4 clear these 10) ===
  L4/gram_reduce -> L1/bilinear-form (rough-in)            [x2 dup edge]
  feature/capacitance.L0   -> feature/capacitance.L1 (rough-in-tcb)
  feature/capacitance.L1   -> L1/bilinear-form (rough-in)
  feature/electrostatic.L0 -> feature/electrostatic.L1 (rough-in-tcb)
  feature/electrostatic.L1 -> L1/bilinear-form (rough-in)
  feature/inductance.L0    -> feature/inductance.L1 (rough-in-tcb)
  feature/inductance.L1    -> L1/bilinear-form (rough-in)
  feature/magnetostatic.L0 -> feature/magnetostatic.L1 (rough-in-tcb)
  feature/magnetostatic.L1 -> L1/bilinear-form (rough-in)
=== RESIDUAL (12) — but several are STALE-EDGE FALSE POSITIVES ===
  L2/normalize  -> L1/normalize (rough-in)        # FALSE: L1/normalize is `firm` on disk (verified) — stale composes-string read
  L3/normalize  -> L1/normalize (rough-in)        # FALSE: same
  L2/nrm2       -> L2/inner_product (rough-in)     # FALSE: L2/inner_product is `firm` on disk (verified) — stale read
  L3/dot        -> L2/inner_product (rough-in)     # FALSE: same
  L3/inner_product -> L2/inner_product (rough-in)  # FALSE: same
  L4/domain_energy_reduce -> L1/matrix-weighted-norm (rough-in-tcb)  # FALSE: matrix-weighted-norm FIRMED c091 — stale
  feature/energy-fields.L1 -> L1/matrix-weighted-norm (rough-in-tcb) # FALSE: same
  feature/energy-fields.L4 -> L1/matrix-weighted-norm (rough-in-tcb) # FALSE: same
  L2/eigsolve   -> L1/eigsolve (rough-in-tcb)      # GENUINE: L1/eigsolve is firm... actually firm c022 — VERIFY at typing
  feature/boundary-mode.L1 -> L1/eigsolve (rough-in-tcb)  # VERIFY
  feature/eigenmode.L1     -> L1/eigsolve (rough-in-tcb)  # VERIFY
  L4/solve_family -> L4-L3/solve-family-map-dissolution (rough-in-tcb)  # GENUINE-candidate (theme endpoint)
```

Verified on disk this cycle: `L1/normalize` §Status = `firm`; `L2/inner_product` §Status = `firm`; `L1/matrix-weighted-norm` §Status = `firm` (c091, `verified_against:` block present). So the typing pass is expected to **clear ~8 of the 12 residual violations as stale-edge false positives** (re-typed edges read live frontmatter), leaving a SMALL genuine baseline-exception seed population (the `L1/eigsolve` chain + `solve-family-map-dissolution` theme — to be confirmed at typing). This is itself a P1 audit finding: **the prose-dep-map / `composes:`-qualifier representation drifts behind the operator frontmatter** — exactly the second-source-of-truth distortion the campaign exists to remove. D6 records it.

## Dispatches

**WAVE 1 (cascade core + cascade hygiene; parallel):**

- **D1 — agent: `harvester`** — scope: `bilinear-form` verb firm-flip + count-owner. Flip `book/src/L1/bilinear-form.md` `firmness: rough-in` → `firm` + drop the rough-in token in §Status:321 (the firm-on-positive-structure escape, DISCHARGE landed c092 — the `verified_against:` block is already on disk; restate the §Status conclusion as ENACTED). **NEW under the HARD-gate-new rule:** since this dispatch promotes a node, it MUST land the node's typed `edges:` + `rank: firm` frontmatter: write `rank: firm` + an `edges: depends-on:` block listing `L1/dot`, `L1/apply_linop`, `L1/matrix-weighted-norm` (all firm — the rank invariant holds) and `edges: reference:` for the L1>L0 theme cross-link — superseding the existing `depends_on:` frontmatter block per scheme §4(a). **WITHIN-FILE self-consistency re-anchor** (the batch-29 discipline): re-read `bilinear-form.md` end-to-end and re-anchor EVERY conclusion narration to the firm §Status, INCLUDING the `:251-257` Dependencies self-note ("the bilinear-form half remains open"). **SOLE owner of `book/src/L1/index.md` count headers** (the `:31` 38→39 grand / 31→32 main-cohort firm bump per the c087/c091 precedent; `:67` bilinear-form dep-map cell rough-in→firm; `:101` joint-OQ narration "bilinear-form half remains rough-in"→firm). HARD: do NOT touch the L1>L0 theme (firm), feature columns, gram_reduce, or `feature/index.md`. — rationale: priorities item-1 (i)+(ii partial); the firm flip + count headers; the rank-invariant HARD-gate-new compliance is the campaign's first new-work gate exercise.

- **D2 — agent: `lifter`** — scope: the whole-`book/src/` cross-reference re-anchor of the ~26 genuine bilinear-form rough-in co-mentions (the 52-file mention set is mostly nav-links; the genuine-maturity cluster the c092 probe enumerated). Re-anchor stale `rough-in` co-mentions of `bilinear-form` to `firm` in: `L2/inner_product.md`, `L2/gram.md`, `L2/dot.md`, `L2/folds-intro.md`, `L2-L1/index.md`, `L1-L0/bilinear-form-mutation-rotation.md` (VERIFY the firm L1>L0 theme does not assert the OPERATOR rough-in), `L1-L0/dot-mutation-rotation.md`, `L1-L0/matrix-weighted-norm-mutation-rotation.md`, `L0/linalg-operator-file.md`, `L0/mpi-globalsum-and-collectives.md`, `L3/inner_product.md`, `L3/index.md`. HARD: do NOT touch any L1-L0 theme's own `## Status`; do NOT touch `L1/index.md` (D1-owned), `feature/*` (D4-owned), `gram_reduce`/`domain_energy_reduce` (D3-owned), `methodology/goal-flow.md` (meta-phase-owned — flag stale refs as OQ-intake). — rationale: priorities item-1 (ii); the whole-book cross-ref re-anchor discipline (`firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep`).

**WAVE 2 (cascade downstream re-judgments, after the flip lands; parallel within the wave):**

- **D3 — agent: `lowering-verifier`** — scope: the coupled `gram_reduce` firm re-judgment. `book/src/L4/gram_reduce.md` §Status — its SOLE residual gate (`bilinear-form`) now clears, so the firm-on-positive-structure escape applies as it did for its reduce-verb siblings `domain_energy_reduce` c091 / `eigenfreq_qfactor_reduce` c082 / `sparameter_reduce` c083. Re-judge → likely FIRM: two clean outcomes — (a) DISCHARGE → flip `rough-in (test-coverage-bounded)`→`firm` + the **HARD-gate-new typed frontmatter** (`rank: firm` + `edges: depends-on:` listing all folded primitives now firm: `bilinear-form` [firmed by D1], `matrix-weighted-norm`, `dot`, `apply_linop`) + re-anchor the bilinear-form labels `:6`/`:55`/`:195`/`:235`/`:242`→firm; (b) CONFIRM-RESIDUAL → record the explicit residual gate, STAYS rough-in (the honest outcome, NOT a forcing). HARD: touches `gram_reduce.md` own status ONLY; do NOT touch the 4 columns (D4), the L1/L4 indexes (D1), or `feature/index.md`. — rationale: priorities item-1 (iii); gates the 4-column flip; the rank linter must see gram_reduce's resolved rank to clear the `gram_reduce -> bilinear-form` violation.

- **D4 — agent: `layer-intro-author`** — scope: the 4-column re-evaluation + feature-index owner. `capacitance`/`inductance`/`electrostatic`/`magnetostatic` columns: under the OWN-COMPOSITION rule, flip `seed`→`firm` IFF the column's own composition + directly-owned constituents are ALL firm once D3 firms `gram_reduce` (else record the residual gate + STAY seed cleanly). Re-anchor the bilinear-form rough-in labels across the column files (`*.L0/.L1/.L4` + `output-product.md`)→firm. **NEW under HARD-gate-new:** any column promoted to `rank: firm` MUST carry the `feature_root: seed` + `rank:` SPLIT (scheme §3) and a typed `edges:` block (`depends-on:` to its vocabulary constituents — `fe_assemble`/`ksp_solve`/`matrix-weighted-norm`/`gram_reduce`/`bilinear-form`; `reference:` to any sibling COLUMN it cross-links — the OWN-COMPOSITION rule means sibling columns are `reference`, NOT blocking). **SOLE owner of `book/src/feature/index.md`** (the column-status matrix + `## Chapter-kind status` + the `# Feature surfaces` SUMMARY block) AND of the whole-`book/src/feature/` sibling-status grep. HARD: do NOT touch the L1/L4 indexes (D1) or `gram_reduce.md`/`domain_energy_reduce.md` (D3). — rationale: priorities item-1 (iv); the visible cascade payload (4 columns flip); single-index-owner discipline (the parallel-blind-shared-index guard — D4 sole-owns `feature/index.md` + the SUMMARY block; the column producers' own per-column edits are non-aggregate).

**WAVE 3 (P1 edge-typing audit over the post-cascade state + baseline-exceptions; parallel within the wave):**

- **D5 — agent: `layer-intro-author`** — scope: P1 feature-root closure typing. Author the typed `edges:` + `feature_root: seed` + `rank:` SPLIT frontmatter (scheme §3) on the **feature-spine columns that D4 did NOT already type** — i.e. the columns NOT in the bilinear-form cascade: the 5 drivers' non-cascade levels (`driven`, `eigenmode`, `transient`, `eigenfrequency-qfactor`, `sparameters`, `energy-fields`, `boundary-mode` × {L0,L1,L4}) + the `lifecycle` spine-ROOT × {L0,L1,L4} + the group-intro pages (`driver-leaf.md`, `output-product.md`, `spine-root.md`). Convert each column's `composes:` → `edges:` per scheme §4(c): a `composes:` target that is a *vocabulary op* → `depends-on`; a *sibling feature column* → `reference` (OWN-COMPOSITION); `l0_ground_truth:` → `depends-on` with `kind: cites-evidence`. Drop the free-text maturity qualifiers from the edge (the dep's rank is read from its OWN frontmatter — this is what clears the stale-edge false positives). **SOLE owner of `feature/index.md` is D4 this cycle** — D5 does NOT touch `feature/index.md` (D5 types per-column frontmatter only; coordinate so D4 lands the index, D5 lands the column-file frontmatter — distinct anchors, but state the partition). — rationale: P1 feature-root closure (the GC root set); makes the reachability GC meaningful; clears the energy-fields/boundary-mode/eigenmode stale-edge false positives by re-typing edges to read live frontmatter.

- **D6 — agent: `cross-layer-cross-cutter`** — scope: P1 high-fan-out vocabulary-frontier typing + the stale-edge audit finding. Author the typed `edges:` + `rank:` frontmatter on the **high-fan-out firm-leaf frontier the rank check anchors on** — the most-depended-on vocabulary: `L1/dot`, `L1/apply_linop`, `L1/nrm2`, `L1/scal`, `L1/normalize`, `L1/matrix-weighted-norm`, `L2/inner_product`, `L2/linear_combination`, `L2/nrm2`, `L3/dot`, `L3/inner_product`, `L3/normalize`, `L4/domain_energy_reduce` + the `L1/eigsolve`→`L2/eigsolve` chain. For each: read the dep's OWN `## Status`, map via scheme §1, write `rank:` + the typed `edges: depends-on:`/`reference:` block (the prose `## Dependencies` cell → typed edges, classified deliberately — the typing pass IS the audit). **Record the stale-edge audit finding** (the §"Key on-disk finding" above): the prose-dep-map/`composes:`-qualifier representation drifts behind operator frontmatter, producing ~8 stale-edge false-positive rank violations that re-typing clears. HARD: type edges ONLY (the operators are already firm — do NOT re-judge maturity; this is an edge-typing + rank-token-write pass, NOT a promotion). Do NOT touch any feature column (D5) or the cascade nodes (D1–D4). — rationale: P1 high-fan-out frontier (the rank-check anchor); clears the dot/nrm2/inner_product/normalize stale false positives; the audit-first finding the campaign exists to surface.

- **D7 — agent: `same-layer-cross-cutter`** — scope: open the tracked baseline-exception set. Author `scaffolding/graded-stack-baseline-exceptions.md` (the campaign's tracked exception list, per the 2026-06-04 decision + `METHODOLOGY-GRADED-STACK.md` §5 "bounded tracked baseline-exceptions, NOT open-ended fix-forward"). After D1–D6 land, re-run `python3 tools/graded-stack-lint/graded_stack_lint.py --json` and record the **GENUINELY-residual** rank violations (the small post-typing population — expected: the `L1/eigsolve` chain if `L1/eigsolve` reads non-firm, + `L4/solve_family -> L4-L3/solve-family-map-dissolution`; verify on disk which survive after D6 re-types edges to live frontmatter). Each entry carries: the violating `src -> dep` edge, the rank gap, the cause, and the **promotion condition** (the `partly-constructive` pattern — e.g. "clears when `solve-family-map-dissolution` firms"). Distinguish CLEARED-BY-CASCADE (the 10, now discharged), CLEARED-BY-RETYPING (the stale false positives D6 cleared), and GENUINE-RESIDUAL (the tracked set). HARD: this is a `scaffolding/` deliverable + the post-D6 linter re-run; NO `book/` mutation. — rationale: the 2026-06-04 decision's "bounded tracked baseline-exception set"; the campaign's discharge-path ledger; depends on D1–D6 so the linter reads the post-cascade post-typing state.

## Overlap analysis

Pairwise (OVERLAPPING = same file region OR one names a node the other promotes/types):

- **D1 ↔ D2:** D1 owns `bilinear-form.md` + `L1/index.md`; D2 owns the ~26 OTHER consumer files (explicitly excludes `bilinear-form.md` own status + `L1/index.md`). NON-overlapping → parallel (wave 1).
- **D1 ↔ D3/D4:** D3 owns `gram_reduce.md`; D4 owns the columns + `feature/index.md`. Both READ the firmed `bilinear-form` — a forward-reference dependency (D3/D4 must read D1's flipped state), NOT a write overlap. Sequenced (wave 2 after wave 1). The node-name `bilinear-form` D3/D4 reference is authored by D1 → forward-ref handled by wave ordering.
- **D2 ↔ D3/D4:** D2 re-anchors cross-ref labels in L2/L0/L3 files; D3 owns gram_reduce; D4 owns feature/*. D2 explicitly excludes gram_reduce/domain_energy_reduce + feature/*. NON-overlapping (D2 wave-1, D3/D4 wave-2 — strictly ordered anyway).
- **D3 ↔ D4:** D3 owns `gram_reduce.md` own status; D4 reads gram_reduce's resolved rank to judge the columns. Forward-ref (D4 reads D3) → D3 and D4 are both wave-2 but D4's column-flip DEPENDS on D3's verdict. Mark D4 deps=[D3] within the wave (D4's gram_reduce-gated flip reads D3's outcome). The c091 precedent ran D3+D4 same-wave with this read-dependency; the per-report integrator serializes the gram_reduce-status read. Marked sequential-within-wave (D4 after D3).
- **D4 ↔ D5:** BOTH touch feature-column files. **D4 SOLE-owns `feature/index.md` + the SUMMARY `# Feature surfaces` block.** D4 types the 4 CASCADE columns' frontmatter (capacitance/inductance/electrostatic/magnetostatic); D5 types the NON-cascade columns' frontmatter (drivers/lifecycle/energy-fields/boundary-mode/group-intros) + does NOT touch `feature/index.md`. Distinct column FILES, distinct anchors → parallel-safe on the per-column frontmatter; the shared `feature/index.md` aggregate is D4-only. State the partition explicitly: **D4 owns `feature/index.md` + SUMMARY block + the 4 cascade columns' frontmatter; D5 owns the non-cascade columns' frontmatter ONLY, defers all `feature/index.md` writes to D4.** Wave 3 (D5) after wave 2 (D4) → strictly ordered, so even the index is serial. NON-overlapping under the partition.
- **D5 ↔ D6:** D5 types feature columns; D6 types L1/L2/L3/L4 vocabulary leaves. Disjoint file sets. Parallel-safe (both wave 3).
- **D6 ↔ D1/D3:** D6 types `L1/matrix-weighted-norm`, `L4/domain_energy_reduce` etc. — does D6 touch `bilinear-form` (D1) or `gram_reduce` (D3)? D6's frontier list EXCLUDES the cascade nodes (D1 already types `bilinear-form` frontmatter; D3 types `gram_reduce`). D6 types only the non-cascade firm leaves. NON-overlapping (and wave 3 after waves 1-2 anyway).
- **D7 ↔ all:** D7 writes `scaffolding/graded-stack-baseline-exceptions.md` (NO book/ writes) + re-runs the linter reading the post-D1–D6 state. Depends on ALL of D1–D6 (it records the residual AFTER cascade + typing). No file overlap (scaffolding-only); pure read-dependency → wave 3, last.

## Sequencing schedule

- **Wave 1 (parallel):** D1 (verb flip + L1/index counts + typed frontmatter), D2 (whole-book cross-ref re-anchor). Both land the bilinear-form firm state.
- **Wave 2 (after wave-1 reports land; D4 reads D3 within-wave):** D3 (gram_reduce re-judgment), D4 (4-column re-eval + feature/index + SUMMARY; D4's gram-gated flip reads D3's verdict). Reads the firmed bilinear-form.
- **Wave 3 (after wave-2 reports land):** D5 (feature-root closure typing — non-cascade columns), D6 (high-fan-out vocabulary-frontier typing + stale-edge audit finding), D7 (baseline-exception set + post-typing linter re-run). D5/D6 parallel; D7 reads the post-D1–D6 state (effectively last, but co-dispatched in wave 3 — its linter re-run runs at integration time after the per-report applies).

Note: ONE `integrator-finalize` runs at cycle-end (waves are dispatch/forward-ref ordering, not multiple finalizes); the book is NOT rebuilt between waves. D7's linter re-run reads the staged-then-applied per-report changes — the finalize runs the linter as a baseline record (NOT a gate this cycle, per OQ `graded-stack-finalize-json-wiring-role-spec`, which is the batch-30 meta-phase's to wire).

## HARD-gate-new compliance note (for every dispatch)

Per the 2026-06-04 decision + `METHODOLOGY-GRADED-STACK.md` §5: **any node a dispatch authors or promotes this cycle MUST carry typed `edges:` frontmatter + a `rank:` token satisfying the rank invariant** (`rank(u) ≤ min over depends-on deps`). Concretely:
- D1's `bilinear-form` firm flip → MUST land `rank: firm` + `edges: depends-on: [L1/dot, L1/apply_linop, L1/matrix-weighted-norm]` (all firm — invariant holds).
- D3's `gram_reduce` (if firmed) → MUST land `rank: firm` + `edges:` over its now-all-firm folded primitives.
- D4's column flips (if firmed) → MUST carry the `feature_root: seed` + `rank: firm` SPLIT + typed `edges:` (vocabulary = `depends-on`, sibling columns = `reference`).
- D5/D6 are pure typing passes (type existing-firm nodes; do NOT promote) — they write `rank:` matching the node's existing `## Status` + the typed `edges:` block.
The rank linter is now the gate; a promoted node without compliant frontmatter is a campaign violation. State this in each dispatch brief.

## priorities.md update (applied)

Marked item-0 P1 + item-1 the bilinear-form cascade as DISPATCHED cycle-095; appended the c095 reshape (this plan's 7-dispatch / 3-wave shape, the cascade-discharges-10 + typing-clears-~8-stale + small-genuine-residual partition, the baseline-exception file home `scaffolding/graded-stack-baseline-exceptions.md`).

## Open questions / caveats

- **Stale-edge representation is itself the P1 headline finding.** ~8 of the 12 "residual" rank violations are FALSE POSITIVES from the linter reading stale `composes:`-qualifier / prose-dep-map maturity strings rather than the dep's own frontmatter (`L1/normalize`, `L2/inner_product`, `L1/matrix-weighted-norm` are all `firm` on disk but cited `rough-in` in consumer prose). The P1 re-typing (D6) clears them by construction (typed edges restate NO maturity). This VALIDATES the campaign's core thesis (the prose dep-map is a drifting second source of truth) and should be surfaced to the batch-30 meta-phase as confirmation that the `edges:`-frontmatter-as-sole-truth migration is correct. **Flag for batch-30 meta-phase.**
- **`L1/eigsolve` rank — verify at typing.** The `L2/eigsolve -> L1/eigsolve` + `eigenmode.L1`/`boundary-mode.L1 -> L1/eigsolve` violations cite `L1/eigsolve` as `rough-in (test-coverage-bounded)`, but `L1/eigsolve` was promoted to `firm` c022 (per `L1/index.md:45`). If `L1/eigsolve` reads firm on disk, these too are stale false positives D6/D5 clear; if the linter reads a real rough-in-tcb sub-rank that genuinely gates, they go to the baseline-exception set. D6 verifies `L1/eigsolve`'s own §Status and the linter's parse. **Resolve at dispatch (D6).**
- **Feature-root frontmatter dual-form.** D4/D5 introduce the `feature_root: seed` + `rank:` SPLIT on columns currently carrying only transitional `status: seed` (OQ `graded-stack-feature-root-frontmatter-split` — the linter accepts the dual form in the interim). The columns D4 FIRMS this cycle get the split with `rank: firm`; the columns D5 types that stay seed get `feature_root: seed` + `rank:` matching their composition maturity (likely `rough-in`/`seed`-equivalent). Confirm the linter's root-detection handles both the legacy `status: seed` and the new `feature_root: seed` (D2 linter's three-signal categorical root rule, OQ `graded-stack-linter-categorical-root-rule-p1-sync`) — if D5's split breaks root detection, that is a linter-fix OQ for the batch-30 meta-phase.
- **Index-page + concept-page node-status (scheme §5) deferred.** This cycle types feature columns + high-fan-out leaves + the cascade nodes. The index pages (`L_n/index.md`) and concept pages' DAG-node-status question (OQ `graded-stack-index-and-concept-node-status`) is NOT resolved this cycle — it is the lazy-tail / P1 sub-task the decision permits. Not forced.
- **Scope-budget judgment.** I considered deferring the bilinear-form cascade to c096 and running P1 alone, OR vice versa. I ran both because: (a) the cascade is pure execution (gate-test DONE c092) and is the rank linter's first live validation — running it WITH the typing pass lets D7 confirm the cascade clears its 10 violations in the same cycle (the validation the priorities explicitly want); (b) the typing pass NEEDS the post-cascade firm state to type the column edges correctly (typing pre-cascade would bake in the rough-in bilinear-form edge, then need re-typing post-cascade — wasteful); (c) 7 dispatches is well under the 12 cap and the waves are cleanly partitioned by ownership. If wave 3 proves too heavy at integration, D7 (baseline-exceptions) is the natural defer-to-c096 candidate (it is observation/ledger, not artifact-frontier).
