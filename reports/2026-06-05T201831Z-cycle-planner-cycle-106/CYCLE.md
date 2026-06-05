---
agent: cycle-planner
invoked_at: 2026-06-05T201831Z
scope: cycle-106 dispatch plan
status: pending
---

# Cycle 106 dispatch plan

FIRST primary cycle of meta-batch-34 (cycles 106/107/108; batch-34 meta-phase fires AFTER cycle-108's finalize). Session was restarted post-batch-33 (the `critic.md` + `layer-intro-author.md` edits are loaded; primary context reset).

## Goals selected this cycle

Execute THE LEAD — `graded-stack-wave-3-op-chapter-uses-record-typing` (priorities item 1, HIGH) — now UNBLOCKED and MEASURABLE by the batch-33 linter block-mapping-edge parser fix. Migrate the 5 L4 solve/BC OPERATOR chapters off pre-scheme frontmatter into typed `edges:` blocks AND add the `uses-record` `depends-on` edges that rescue the 6 internal records (`sim-state`/`krylov`/`step-outputs`/`prev-carry`/`solve-result`/`dofset`) from reachability-GC garbage. Co-schedule the two LOW loose-ends (priorities item 3a/3b) + ONE bounded MEDIUM lazy-tail sub-target (the `unresolved_depends_on_targets: 21` reclassification). FIVE dispatches, ONE wave (all 5 file sets disjoint → parallel).

## Linter baseline (verified on disk this cycle)

```
totals: files 355, typed 278, untyped 77, roots 36, rank_violations 0,
        unresolved_depends_on_targets 21, promotion_frontier 8,
        reachable 81, detritus 163
```

`--show-inbound` confirms all 6 target records are currently UNREACHABLE:
```
[garbage?] concepts/dofset
[garbage?] concepts/krylov
[garbage?] concepts/prev-carry
[garbage?] concepts/sim-state
[garbage?] concepts/solve-result
[garbage?] concepts/step-outputs
```
→ the WAVE-3 rescue is now MEASURABLE: `reachable` should climb past 81 and the 6 records flip `[garbage?]`→reachable after the cycle.

## Reachability-flow analysis (load-bearing for tranche design)

The `uses-record` edges only rescue a record if the OP CHAPTER carrying them is itself root-reachable. On-disk `--show-inbound` (verified this cycle):
- `L4/ksp_solve` ← `driven.L4`, `electrostatic.L4`, `magnetostatic.L4` (+ internal). **ROOT-REACHABLE.** Its `uses-record`→`op-params`,`sim-state` rescue lands.
- `L4/solve_family` ← `electrostatic.L4`, `magnetostatic.L4`. **ROOT-REACHABLE.**
- `L4/fold_solve` ← `lifecycle.L4`, `lifecycle.L1`, `transient.L4`, `transient.L1`. **ROOT-REACHABLE.**
- `L4/krylov-step` ← ONLY `L3/krylov-step` (itself garbage). **NOT root-reachable today** — becomes reachable via the `ksp_solve depends-on krylov-step` typed edge the migration adds (ksp_solve body refs krylov-step 18×). This is WHY `ksp_solve` + `krylov-step` are coupled in ONE dispatch (D1): the rescue of the 4 krylov-only records (`krylov`/`step-outputs`/`prev-carry`/`solve-result`) DEPENDS on ksp_solve→krylov-step being wired in the same consistent pass.
- `L4/eliminate_bc` is `[GARBAGE*]` — **NOT root-reachable**, and §(f) adds NO column→eliminate_bc edge. `eliminate_bc` composes `fe_assemble`, but edge-direction means that does not make eliminate_bc reachable. So `eliminate_bc`'s `uses-record`→`dofset` edge may NOT rescue `dofset` on its own. D3 carries an explicit post-edit verify + finding-route (do NOT force an unfaithful column→eliminate_bc edge — the c104-D2 discipline).

## Deliverable-presence verification (paste-inline-evidence; per the strengthened batch-10 procedure)

All five dispatches resolve to named `book/src/` file paths. Four-step sequence with pasted evidence:

### D1 — `L4/ksp_solve.md` + `L4/krylov-step.md` (WAVE-3 typing)
1. **File existence:** `ls book/src/L4/ksp_solve.md` → present; `ls book/src/L4/krylov-step.md` → present (both confirmed in the cycle-scan; all 5 op chapters listed OK).
2. **Maturity / already-discharged:** `ksp_solve` frontmatter is pre-scheme (`consumes:`/`lowers_to:`/`variant_axes:`) — NO typed `edges:` block, NO `uses-record` edge → WAVE-3 work OPEN. `krylov-step` line 1 = `# krylov-step` → NO frontmatter at all → author `edges:` from scratch, OPEN. `grep -c 'krylov-step' book/src/L4/ksp_solve.md` = 18 (the body-ref basis for the `depends-on` edge).
3. **OQ RESOLVED-grep:** migrated LEAD OQ `solve-record-reachability-needs-op-chapter-uses-record-edges` → `open-questions.md:1274` is `MIGRATED to the plan as the batch-34 LEAD` (open by construction — the work-item, not a closure). No RESOLVED/CLOSED for the WAVE-3 slug.
4. **Structural-block:** none. Records are `rank: firm` resting on firm L0 cites; the linter block-mapping-edge parser is FIXED (batch-33); well-foundedness holds firm/firm. OPEN.

### D2 — `L4/solve_family.md` + `L4/fold_solve.md` (WAVE-3 typing)
1. **File existence:** both present (cycle-scan: `book/src/L4/solve_family.md`, `book/src/L4/fold_solve.md` listed OK).
2. **Maturity:** both pre-scheme frontmatter (`consumes:`/`lowers_to:`/`variant_axes:`), NO typed `edges:` block, NO `uses-record` edge → OPEN.
3. **OQ:** same migrated-LEAD OQ; open by construction.
4. **Structural-block:** none. OPEN.

### D3 — `L4/eliminate_bc.md` (WAVE-3 typing + item-3b stale-prose, same file)
1. **File existence:** present (cycle-scan OK).
2. **Maturity:** frontmatter carries pre-scheme `consumes:`/`lowers_to:` PLUS a partial `depends_on:` block (NOT the scheme `edges:` block form), NO `uses-record` edge → migration OPEN. Item-3b prose at `:126` reads (pasted): `the concept page \`book/src/concepts/DofSet.md\` does **not yet exist**.` — `concepts/dofset.md` DOES exist (`head -10` shows `rank: firm`/`kind: record`) → stale, OPEN.
3. **OQ RESOLVED-grep:** `eliminate-bc-record-definition-prose-now-stale` → `open-questions.md:1278` is a KEPT-DEFERRED open item (trigger = a touch on `eliminate_bc.md`, which D3 IS) — NOT RESOLVED. OPEN.
4. **Structural-block:** none (the WAVE-3 reachability caveat is a finding-route, not a block). OPEN.

### D4 — `concepts/set_subvector_zero.md` (item-3a reciprocal back-link)
1. **File existence:** present.
2. **Maturity:** frontmatter (pasted) is `edges:\n  reference: []  # no book home: L1/set_subvector_zero does not exist; …` — `reference: []` empty + the comment is doubly-stale: `ls book/src/L1/set_subvector_zero.md` → present (exit 0; landed c104/c105), and no `reference` to `concepts/dofset.md` → OPEN.
3. **OQ RESOLVED-grep:** `set-subvector-zero-references-dofset` → `open-questions.md:1277` KEPT-DEFERRED open item (trigger = a touch on `set_subvector_zero.md`, which D4 IS). NOT RESOLVED. OPEN.
4. **Structural-block:** none. OPEN.

### D5 — the `unresolved_depends_on_targets: 21` host files (lazy-tail reclassify)
- **Open by construction** (no prior-cycle history): the `unresolved_depends_on_targets: 21` is a fresh linter-surfaced set, the bounded measurable sub-target of plan item 2 `graded-stack-lazy-tail-typing` (MEDIUM). The linter `--show-inbound`/`--strict` enumerates the hosts at dispatch; D5 must EXCLUDE the 5 WAVE-3 chapters D1/D2/D3 own (deferring any of the 5 to its owning WAVE-3 dispatch). No RESOLVED grep applies (it is a reclassification pass, not a single-slug deliverable). OPEN.

**STOP-PROPOSING NEGATIVE LIST:** no dispatch matches a disqualified slug (`lu_solve`/`back_solve`/`ls-update-column`/`nleps_*`). No `promotion_frontier: 8` obstruction-/demand-gated member proposed (`bicgstab`/`minres`/`eigsolve-convergence-reason-mapping`/`deflate*`/`boundary-mode.*`). The redirect's no-rectangular-pull-up holds — these are typed-edge migrations on already-firm chapters, not new operator algebra.

## Dispatches

1. **agent:** `layer-intro-author`
   **scope:** WAVE-3 op-chapter typing — the solve-kernel pair `book/src/L4/ksp_solve.md` + `book/src/L4/krylov-step.md` (COUPLED). Migrate `ksp_solve` off pre-scheme `consumes:`/`lowers_to:` into a typed scheme `edges:` block: preserve its real `depends-on` edges (incl. `depends-on` → `L4/krylov-step` per the 18 body refs — THIS edge makes krylov-step root-reachable) + add `uses-record` `depends-on` → `concepts/op-params`, `concepts/sim-state`; keep navigational/`reference` edges as `reference`. Author `krylov-step`'s `edges:` block FROM SCRATCH (no existing frontmatter) with `uses-record` `depends-on` → `concepts/op-params`, `concepts/krylov`, `concepts/sim-state`, `concepts/step-outputs`, `concepts/prev-carry`, `concepts/solve-result` + its real `depends-on`/`reference` book edges. Use the block-mapping edge form (`- target: …` / `  kind: uses-record`) — the batch-33 linter fix GC-traverses it. Follow the §(e) scheme conventions exactly. Re-run `graded_stack_lint.py --show-inbound` and confirm the 6 records gain inbound edges.
   **deps:** none.
   **rationale:** THE LEAD (priorities item 1). The rescue-dominant tranche — `ksp_solve` is root-reachable and pulls `krylov-step` (via the typed `depends-on`) and through it all 6 solve records into the live set. Coupling ksp_solve+krylov-step in one dispatch keeps the `depends-on krylov-step` edge consistent with krylov-step's own `edges:` block (no cross-report edge-kind mismatch). fan-out HIGH.

2. **agent:** `layer-intro-author`
   **scope:** WAVE-3 op-chapter typing — `book/src/L4/solve_family.md` + `book/src/L4/fold_solve.md`. Migrate both off pre-scheme frontmatter into typed scheme `edges:` blocks (preserve real `depends-on`/`reference` book edges, e.g. `solve_family depends-on ksp_solve`/`iterate-while`; `fold_solve depends-on iterate-while`) + add `uses-record` `depends-on`: `solve_family` → `concepts/op-params`, `concepts/sim-state`; `fold_solve` → `concepts/op-params`. Block-mapping edge form; §(e) conventions. Re-run the linter `--show-inbound`.
   **deps:** none.
   **rationale:** THE LEAD continuation. Both root-reachable (solve_family ← electrostatic/magnetostatic; fold_solve ← lifecycle/transient), so their `uses-record`→op-params/sim-state edges add real inbound edges and strengthen the rescue. fan-out HIGH.

3. **agent:** `layer-intro-author`
   **scope:** WAVE-3 op-chapter typing — `book/src/L4/eliminate_bc.md` (+ COUPLED item-3b stale-prose fix, SAME file). Migrate `eliminate_bc` off pre-scheme `consumes:`/`lowers_to:`/`depends_on:` into a single typed scheme `edges:` block (fold the existing partial `depends_on:` into the scheme block; preserve `depends-on` → `fe_assemble`/`linear_combination`, `reference` to the navigational ones) + add `uses-record` `depends-on` → `concepts/dofset`. COUPLED in-dispatch: retarget the stale §Record-definition prose at `eliminate_bc.md:126` (it says `concepts/DofSet.md` "does not yet exist" — point it at the now-existing `concepts/dofset.md`, lowercase). **Post-edit, re-run `--show-inbound`:** if `dofset` is NOT rescued because `eliminate_bc` stays `[GARBAGE*]` (not root-reachable), ROUTE the BC-driver-column→eliminate_bc edge gap AS A FINDING in §Open questions — do NOT force an unfaithful `column→eliminate_bc` edge (the c104-D2 faithful-path-or-finding discipline).
   **deps:** none.
   **rationale:** THE LEAD's dofset-rescue tranche + a stale-prose close (item 3b). The reachability caveat is faithfully surfaced as a finding rather than papered over. fan-out HIGH.

4. **agent:** `lifter`
   **scope:** item-3a `set-subvector-zero-references-dofset` — `book/src/concepts/set_subvector_zero.md` frontmatter (`:2-5`). Replace `reference: []` with `reference: [book/src/L1/set_subvector_zero.md, book/src/concepts/dofset.md]` (the reciprocal back-link to dofset; the L1 home now exists) and de-stale the inline comment ("L1/set_subvector_zero does not exist" is now FALSE — the file landed c104/c105). Re-run `citecheck`/linter on the file to confirm clean.
   **deps:** none.
   **rationale:** item 3a (LOW) — a doubly-stale frontmatter fix (empty reference + false comment), trigger-fired by this touch. fan-out LOW.

5. **agent:** `layer-intro-author`
   **scope:** item-2 lazy-tail bounded sub-target — reclassify the `unresolved_depends_on_targets: 21` prose-as-slug false-positives. Enumerate the 21 via `graded_stack_lint.py --show-inbound` / `--strict`; for each host file's frontmatter, classify the unresolved `depends-on` target: (a) prose-as-slug → re-encode as `reference` or strike; (b) legitimate L0-range `cites-evidence` edge mis-read as a book slug → confirm/apply the `cites-evidence` L0-edge linter exemption (OQ `cites-evidence-l0-edge-linter-slug-resolution-exemption`); (c) a genuine missing-target → route as a finding. Author ONLY frontmatter `edges:` corrections. **EXCLUDE the 5 WAVE-3 chapters** (`L4/ksp_solve`/`krylov-step`/`solve_family`/`fold_solve`/`eliminate_bc`) — if any is among the unresolved-target hosts, DEFER it to the owning WAVE-3 dispatch (D1/D2/D3). Re-run `--strict` and report the new `unresolved_depends_on_targets` count.
   **deps:** none (file-disjoint from D1/D2/D3 by the exclusion instruction).
   **rationale:** item 2 (MEDIUM) measurable sub-target — collapses the `unresolved_depends_on_targets` tail; sharpens the GC's detritus-vs-untyped-but-live discriminator now that the linter reads the true picture. fan-out MEDIUM. Plan-tag `graded-stack-lazy-tail-typing`.

## Overlap analysis

Pairwise (file regions / shared operator names):

- **D1 ∩ D2:** D1 = `L4/{ksp_solve,krylov-step}.md`; D2 = `L4/{solve_family,fold_solve}.md`. Disjoint files. `solve_family depends-on ksp_solve` is an edge D2 authors pointing at D1's chapter — but `ksp_solve` is an EXISTING stable slug (no slug-invention risk; edge target unchanged by D1's migration). NOT overlapping → parallel.
- **D1 ∩ D3:** `L4/{ksp_solve,krylov-step}` vs `L4/eliminate_bc`. Disjoint. Parallel.
- **D1 ∩ D4:** `L4/*` vs `concepts/set_subvector_zero.md`. Disjoint. Parallel.
- **D1 ∩ D5:** D5 EXCLUDES the 5 WAVE-3 chapters by instruction → no file overlap. Parallel.
- **D2 ∩ D3:** `L4/{solve_family,fold_solve}` vs `L4/eliminate_bc`. Disjoint. Parallel.
- **D2 ∩ D4 / D2 ∩ D5:** disjoint (D5 exclusion). Parallel.
- **D3 ∩ D4:** `L4/eliminate_bc.md` vs `concepts/set_subvector_zero.md`. Disjoint. Parallel.
- **D3 ∩ D5:** D5 excludes `eliminate_bc`. Parallel.
- **D4 ∩ D5:** `concepts/set_subvector_zero.md` is a non-node pointer page (`reference`-only, no `depends-on`) → it is NOT among the `unresolved_depends_on_targets` hosts (those are `depends-on` edges) → no overlap. Parallel.

**Shared-index / consolidated-tally:** none. Each dispatch authors per-file frontmatter (op-chapter `edges:` blocks / a concept-page `reference` list / scattered frontmatter corrections). No `L_n/index.md` consolidated count, no §Vocabulary-cohort bullet cohort, no SUMMARY tally touched. The parallel-blind-shared-index guard does not apply this cycle.

**Cross-report forward-reference slugs:** none. Every edge target is an EXISTING on-disk slug — the 6 record pages (`concepts/{sim-state,krylov,step-outputs,prev-carry,solve-result}.md`), `concepts/dofset.md`, `concepts/op-params.md`, `concepts/sim-state.md`, `L1/set_subvector_zero.md`, and the inter-op `depends-on` targets (`L4/krylov-step`, `L4/ksp_solve`, `L4/iterate-while`, `L4/fe_assemble`, `L4/linear_combination`) all verified present this cycle. No new-slug forward reference → no `cross-report-forward-reference-slug-divergence` risk.

## Sequencing schedule

**ONE WAVE — all five dispatches parallel.** All file sets are disjoint (D5's WAVE-3-chapter exclusion guarantees it); the only inter-dispatch edge references (D2→ksp_solve, D1's ksp_solve→krylov-step) target existing stable slugs. Per the conflict-tolerance philosophy (when in doubt, mark PARALLEL; false-sequentialization is the worse error), there is no genuine write-conflict to serialize.

The reachability rescue is verified at finalize step-5b (`graded_stack_lint.py` re-run): `reachable` should climb past 81 and the 6 records (`dofset`/`krylov`/`prev-carry`/`sim-state`/`solve-result`/`step-outputs`) should flip `[garbage?]`→reachable. The integrator-finalize records the new `reachable`/`rank_violations` (expected held at 0) trend.

## Open questions / caveats

- **`L4/eliminate_bc` reachability gap (surfaced this cycle, routed via D3).** `eliminate_bc` is `[GARBAGE*]` and §(f) adds no column→eliminate_bc edge, so its `uses-record`→`dofset` edge may not rescue `dofset` standalone. D3 verifies post-edit and routes the column→eliminate_bc edge question as a finding (faithful-path-or-finding). If `dofset` stays unreachable, the batch-34 meta-phase should decide whether a BC-driver-column→eliminate_bc `depends-on`/`composes` edge is faithful (electrostatic/magnetostatic columns DO eliminate-then-solve, so the edge is plausibly faithful — but the call belongs to a producer/meta judgment, not a forced planner edge). Mirrors the c104-D2 `dofset-reachability-needs-uses-record-edge` open thread.
- **`krylov-step` becomes reachable ONLY via the `ksp_solve depends-on krylov-step` edge** authored in D1. If a future refactor removes that edge or splits ksp_solve/krylov-step across dispatches, the 4 krylov-only records (`krylov`/`step-outputs`/`prev-carry`/`solve-result`) would re-orphan. Recorded so the coupling rationale is durable.
- **integrator-signals.md tail is STALE (cycle-019).** The file's most-recent in-file section is cycle-019; the actual recent handoff lives in the c103/c104/c105 finalize reports + the priorities active head. The per-batch tail-trim (batch-7 directive) appears to have over-trimmed or the recent finalizes did not append. NOT load-bearing for this plan (I read the c105 active head + cycle-record `counts_after` + the live linter instead), but flagging for the batch-34 meta-phase: confirm `integrator-finalize` is still appending integrator-signals sections (if it stopped, the planner loses its structured per-cycle handoff channel). Surfaced here per the cadence note (the friction-ledger entry may not exist yet).
- **Lazy-tail (item 2) deliberately bounded this cycle.** Only the measurable `unresolved_depends_on_targets: 21` sub-target (D5) is scheduled; the bulk lazy tail (26 L0 ground-truth + 26 meta-reviews + methodology/design/SUMMARY + the strict-zero concept pages) is left to acquire `edges:` lazily as next-touched (per priorities item 2's explicit "NOT a single heavy wave"). The WAVE-3 LEAD is the headline; manufacturing a heavy lazy-tail wave would dilute it.
