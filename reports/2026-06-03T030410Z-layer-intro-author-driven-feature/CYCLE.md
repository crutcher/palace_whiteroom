---
agent: layer-intro-author
invoked_at: 2026-06-03T030410Z
scope: driven feature-surface column (L4/L1/L0) + sole index/SUMMARY owner for the driven+transient+eigenmode driver-column cohort
status: pending
integrated_at: 2026-06-03T214500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-073 D2 (COHORT OWNER). Applied clean — new feature/driven.{L4,L1,L0}.md (status seed) + SOLE-owned feature/index.md (matrix +3 driver rows) + SUMMARY '# Feature surfaces' rows for all 3 new columns (within-column high->low). HAPPY-PATH: D3/D4 files on disk first -> every cell a LIVE link. Completes the 5-driver leaf-column set (2->5). Build exit 0, linkcheck2 clean."
---

# CYCLE: driven feature-surface column (FEATURE-SURFACE SPINE)

## Summary

Authors the **driven (frequency-domain) simulation feature-surface column** —
`book/src/feature/driven.{L4,L1,L0}.md` — a **leaf feature column** (per-driver;
stage-2 constituents are vocabulary ops) composition-root in the FEATURE-SURFACE
SPINE, at the **operator-VARYING** corner. The driven column is the third leaf driver
column after electrostatic + magnetostatic (both fixed-operator), and is the **first
feature column all three of whose L4 composition stages compose FIRM combinators**:

- **L4 body** = `sparameter_reduce ∘ frequency_sweep ∘ fe_assemble(×3)` — assemble the
  fixed operator basis `{K, C, M}` once via [`fe_assemble`](../L4/fe_assemble.md)
  (firm), then the operator-VARYING per-ω solve map
  [`frequency_sweep`](../L4/frequency_sweep.md) (firm) composing the per-ω operand verb
  [`assemble_frequency_operator`](../L4/assemble_frequency_operator.md) (firm, `A(ω) = K
  + iωC − ω²M + A2(ω)`) with the per-member [`ksp_solve`](../L4/ksp_solve.md) (firm),
  then the S-parameter output-product reduction (forward-ref to its own column). The
  load-bearing structural fact is the **non**-hoist — `SetOperators` *inside* the loop
  (`drivensolver.cpp:180`) — which scopes driven out of `solve_family` and into
  `frequency_sweep`'s `operator-capture = per-element` axis.
- **L1 body** = the pure-function surface of the same composition (an explicit per-ω
  comprehension rebuilding the operator inside its body; all three L1 constituents firm).
- **L0** = ground truth `drivensolver.cpp` — `DrivenSolver::Solve` (`:37-75`, dispatch
  to uniform/adaptive) → `SweepUniform` (`:77-229`, the per-ω loop `:168-221`, the
  `ksp.SetOperators(*A,*P)` INSIDE the loop at `:180`).

This dispatch is **sole index/SUMMARY owner for the driver-column cohort** (cycle-073
D2): the proposed changes add `book/src/feature/index.md` matrix rows AND the
`# Feature surfaces` `SUMMARY.md` rows for **all three** driver columns — `driven`
(authored here), `transient` (D3), `eigenmode` (D4) — placed per the spine's top-down
reading order (leaf drivers grouped before the lifecycle ROOT). D3/D4 author only their
chapter files and defer their index/SUMMARY rows to this owner.

Uniform `status: seed` (the prose names the leaf-feature-column sub-kind; the column
stays `seed` because the stage-3 S-parameter output-product reduction is not yet a firm
authored constituent — a feature column promotes past `seed` only once ALL composed
constituents are firm).

All L0 line ranges self-verified on-disk this dispatch via palace-codemap `read_range`
+ direct on-disk `Read` (close-brace discipline on the loop END `:221` + function END
`:229`).

## Proposed changes

### 1. New file `book/src/feature/driven.L4.md`

```new-file:book/src/feature/driven.L4.md
[see supporting doc reports/2026-06-03T030410Z-layer-intro-author-driven-feature/driven.L4.md — the full chapter body is staged there for verbatim copy]
```

### 2. New file `book/src/feature/driven.L1.md`

```new-file:book/src/feature/driven.L1.md
[see supporting doc reports/2026-06-03T030410Z-layer-intro-author-driven-feature/driven.L1.md — the full chapter body is staged there for verbatim copy]
```

### 3. New file `book/src/feature/driven.L0.md`

```new-file:book/src/feature/driven.L0.md
[see supporting doc reports/2026-06-03T030410Z-layer-intro-author-driven-feature/driven.L0.md — the full chapter body is staged there for verbatim copy]
```

> **Integrator note:** the three full chapter bodies are staged as sibling files in
> this report directory (`driven.L4.md`, `driven.L1.md`, `driven.L0.md`) to keep this
> CYCLE.md free of nested-fence truncation hazards (the chapters contain ```` ```text ````
> fenced L4 signatures). Copy each staged file verbatim to its `book/src/feature/`
> target. This is the same staging pattern used for the electrostatic/magnetostatic
> seed columns.

### 4. Edit `book/src/feature/index.md` — the feature × level matrix (sole-owner; all three driver columns)

Add the three driver-column rows to the matrix table, placed AFTER the `magnetostatic`
leaf-driver row and BEFORE the `lifecycle` ROOT row (leaf drivers grouped before the
ROOT, per the spine's top-down reading order). The `transient` + `eigenmode` rows are
deferred-to-this-owner; their chapter files are authored by D3/D4 this same cycle.

```edit:book/src/feature/index.md
[old]:
| [magnetostatic](./magnetostatic.L4.md) | [L4 root](./magnetostatic.L4.md) | [L1 root](./magnetostatic.L1.md) | [L0 surface](./magnetostatic.L0.md) |
| [lifecycle](./lifecycle.L4.md) | [L4 root](./lifecycle.L4.md) | [L1 root](./lifecycle.L1.md) | [L0 surface](./lifecycle.L0.md) |
[new]:
| [magnetostatic](./magnetostatic.L4.md) | [L4 root](./magnetostatic.L4.md) | [L1 root](./magnetostatic.L1.md) | [L0 surface](./magnetostatic.L0.md) |
| [driven](./driven.L4.md) | [L4 root](./driven.L4.md) | [L1 root](./driven.L1.md) | [L0 surface](./driven.L0.md) |
| [transient](./transient.L4.md) | [L4 root](./transient.L4.md) | [L1 root](./transient.L1.md) | [L0 surface](./transient.L0.md) |
| [eigenmode](./eigenmode.L4.md) | [L4 root](./eigenmode.L4.md) | [L1 root](./eigenmode.L1.md) | [L0 surface](./eigenmode.L0.md) |
| [lifecycle](./lifecycle.L4.md) | [L4 root](./lifecycle.L4.md) | [L1 root](./lifecycle.L1.md) | [L0 surface](./lifecycle.L0.md) |
```

> **Integrator dependency note (ordering — read first):** this report is the sole
> index/SUMMARY owner for the driven/transient/eigenmode cohort; D3 (transient) and D4
> (eigenmode) author ONLY their chapter files this same cycle and defer their rows to
> here. **Expected (happy) path:** all three columns land in the same finalize batch —
> apply this block AFTER D3/D4's `transient.*` / `eigenmode.*` chapter files exist on
> disk (i.e. apply D2's cohort index/SUMMARY block last among the three reports, or in a
> single finalize where all three are present), so every cell is a live link. The
> `driven.*` links resolve to the files created in changes 1–3 of THIS report and are
> always safe. **Fallback (only if D3/D4 did NOT land in this finalize batch):** the
> `transient.*` / `eigenmode.*` cells become dead links (a `linkcheck2` build error); in
> that case defang ONLY those two rows to plain-text per the
> `rough-in-rows-must-be-plain-text-when-anchor-missing` convention until the chapters
> land. Do NOT defang the `driven` row.

Update the "Planned" paragraph to reflect the three driver columns landing this cycle:

```edit:book/src/feature/index.md
[old]:
Planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the remaining sim drivers (eigenmode, driven, transient), the output products (S-params / capacitance / inductance / eigenfreq + Q / fields), and wave-port / boundary-mode. Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
[new]:
The **driven**, **transient**, and **eigenmode** driver columns (cycle-073) complete the 5-driver leaf-column set: with electrostatic + magnetostatic (the fixed-operator pair) these three add the **operator-VARYING** corner (driven — the per-ω rebuild + `SetOperators`-inside-the-loop [`frequency_sweep`](../L4/frequency_sweep.md) map), the **state-threaded sequential-fold** corner (transient — the [`fold_solve`](../L4/fold_solve.md) time-step march), and the **opaque-library black-box** corner (eigenmode — the SLEPc eigen-iteration). The driven column is the first whose three L4 composition stages all compose FIRM combinators (the assemble basis, the per-ω operand verb, and the operator-varying solve map are each firm). Still planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the output products (S-params / capacitance / inductance / eigenfreq + Q / fields) and wave-port / boundary-mode (the 6th `ProblemType` branch, authored as a co-equal leaf driver column under the lifecycle ROOT). Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
```

> **Integrator note:** if D3/D4 (transient/eigenmode) chapters do NOT land in this
> finalize batch, soften the "(cycle-073) complete the 5-driver leaf-column set"
> framing to name only the columns that landed (driven), and revert the transient/
> eigenmode prose to the Planned list — the prose above assumes the full driver cohort
> lands together (the cycle-073 plan dispatches D2/D3/D4 in parallel for exactly this).

### 5. Edit `book/src/SUMMARY.md` — the `# Feature surfaces` Part (sole-owner; all three driver columns)

Add the three driver columns' L4/L1/L0 sub-entries (each nested high→low, the
deliberate alpha-within-cohort exception), placed AFTER the `magnetostatic` block and
BEFORE the `lifecycle` ROOT block.

```edit:book/src/SUMMARY.md
[old]:
- [magnetostatic — L4 composition-root](./feature/magnetostatic.L4.md)
- [magnetostatic — L1 composition-root](./feature/magnetostatic.L1.md)
- [magnetostatic — L0 ground-truth surface](./feature/magnetostatic.L0.md)
- [lifecycle — L4 composition-root](./feature/lifecycle.L4.md)
[new]:
- [magnetostatic — L4 composition-root](./feature/magnetostatic.L4.md)
- [magnetostatic — L1 composition-root](./feature/magnetostatic.L1.md)
- [magnetostatic — L0 ground-truth surface](./feature/magnetostatic.L0.md)
- [driven — L4 composition-root](./feature/driven.L4.md)
- [driven — L1 composition-root](./feature/driven.L1.md)
- [driven — L0 ground-truth surface](./feature/driven.L0.md)
- [transient — L4 composition-root](./feature/transient.L4.md)
- [transient — L1 composition-root](./feature/transient.L1.md)
- [transient — L0 ground-truth surface](./feature/transient.L0.md)
- [eigenmode — L4 composition-root](./feature/eigenmode.L4.md)
- [eigenmode — L1 composition-root](./feature/eigenmode.L1.md)
- [eigenmode — L0 ground-truth surface](./feature/eigenmode.L0.md)
- [lifecycle — L4 composition-root](./feature/lifecycle.L4.md)
```

> **Integrator dependency note (SUMMARY — ordering — read first):** mdBook requires
> every `SUMMARY.md` entry to resolve to an existing file — a row pointing at a missing
> file is a HARD build break (stronger than the index-table case, which only triggers
> `linkcheck2`). So there is NO plain-text-defang fallback for SUMMARY: an un-landed
> column's block is OMITTED, not softened. **Expected (happy) path:** all three columns
> land in the same finalize batch — apply this full block AFTER D3/D4's `transient.*` /
> `eigenmode.*` chapter files exist on disk (apply D2's cohort block last among the
> three, or in a single finalize where all three are present). The `driven.*` entries
> resolve to changes 1–3 of THIS report and are always added. **Fallback (only if D3/D4
> did NOT land in this finalize batch):** OMIT the corresponding `transient.*` and/or
> `eigenmode.*` SUMMARY blocks entirely (each independently — omit only the column(s)
> whose chapter files are absent); add each block back only when its chapter files are
> present in the batch. The `driven` block is always added.

## Supporting evidence

**Constituent L4 vocabulary (all firm; `## Status` lines read on-disk this dispatch):**
- `book/src/L4/fe_assemble.md` — firm (`firmness: firm`, `## Status` `:167`). The
  assemble-fold combinator; the driven basis `{K, C, M}` is three single-term folds.
- `book/src/L4/assemble_frequency_operator.md` — firm (`firmness: firm`, `## Status`
  `:348`). The per-ω operand verb `A(ω) = K + iωC − ω²M + A2(ω)`, the operator-operand
  `linear_combination` specialization (single-pipeline-by-design driven; affine-modulo-A2).
- `book/src/L4/frequency_sweep.md` — firm (`firmness: firm`, `## Status` `:487`). The
  operator-VARYING per-ω solve map; the load-bearing `operator-capture = per-element`
  axis + the non-hoist law 2 (`SetOperators` inside the loop). Single-witness-driven by
  design.
- `book/src/L4/ksp_solve.md` — firm (`firmness: firm`, `## Status` `:158`). The
  per-member solve cap `frequency_sweep` maps.

**Constituent L1 vocabulary (all firm; `## Status` / `firmness:` read on-disk):**
- `book/src/L1/fe_assemble.md` — firm. `book/src/L1/assemble_frequency_operator.md` —
  firm (`firmness: firm`, `## Status` `:130`). `book/src/L1/ksp_solve.md` — firm
  (`## Status` `:102`). NOTE: L1 has NO `frequency_sweep` / `solve_family` chapter — the
  outer-driver combinator naming is L4's; at L1 the sweep is an explicit comprehension
  mapping the firm per-ω rebuild + `ksp_solve` (the L1 column expresses this directly).

**L0 driven driver source (self-verified on-disk this dispatch — palace-codemap
`read_range` + direct `Read`):**
- `drivensolver.cpp:37-75` — `DrivenSolver::Solve` entry; dispatch `return {adaptive ?
  SweepAdaptive : SweepUniform, GlobalTrueVSize()}` at `:73-74`.
- `drivensolver.cpp:77-229` — `SweepUniform` (the uniform frequency sweep); fixed basis
  assembled once `:91-93`; solver built once (no `SetOperators` here) `:98`; swept family
  `:80`; per-ω inner loop `:168-170` (close brace `:221`); per-ω rebuild `A2 :175`, `A
  :176-177`, `P :178-179`; **`ksp.SetOperators(*A, *P)` INSIDE the loop `:180`**; per-ω
  RHS `:194`; per-ω solve `ksp.Mult(RHS, E)` `:196`; B-field recovery `:205-207`; per-ω
  measurement `MeasureAndPrintAll(...)` `:215-216`; finalize `:227`; return `:228`;
  function close `:229`.
- `drivensolver.cpp:231` — `SweepAdaptive` (the adaptive PROM sweep, the `fold_solve`
  state-generated fold sibling — NOT this column's composition; named for the
  uniform/adaptive = map/fold split).
- `drivensolver.hpp:22-34` — class declaration (`DrivenSolver : public BaseSolver`;
  `Solve` override `:29-30`; `SweepUniform`/`SweepAdaptive` `:25`/`:27`).

**Cross-references to adjacent surfaces:**
- `book/src/feature/electrostatic.{L4,L1,L0}.md` + `book/src/feature/magnetostatic.{L4,L1,L0}.md`
  — the fixed-operator sibling exemplars the driven column mirrors (contrasted at the
  operator-capture axis: fixed-operator hoist vs operator-varying non-hoist).
- `book/src/L4/solve_family.md` — the fixed-operator map sibling that scopes driven OUT
  (the `per-element` superset boundary `frequency_sweep` formalizes).
- `book/src/L1-L0/assemble-frequency-operator-rotation.md` — the per-ω substantive
  rotation (the per-ω `SetOperators` capture lives here); cited as a live link in the
  driven.L1/L0 chapters (confirmed on-disk).

## Open questions / caveats

1. **Shared operator-weighted-Gram energy-form reduction combinator (≥2→3 witness
   mine).** The driven S-parameter / per-ω energy reduction (stage 3) is the same
   operator-weighted-Gram `map`-then-`reduce` shape as the electrostatic capacitance
   `Vⱼᵀ K Vᵢ` and magnetostatic inductance `(Aⱼᵀ K Aᵢ)/(IᵢIⱼ)` reductions — the driven
   case is a potential **3rd witness** strengthening the already-≥2-witness
   `shared-l4-energy-form-reduction-combinator-gram-reduce-two-witness-mine` plan item
   (migrated to the batch-23 active head). Whether the driven per-ω S-parameter
   normalization fits the same `gram_reduce` shape (it differs in the per-ω frequency
   parameterization + the port-impedance normalization) is the open sub-question. NOT a
   blocker — the driven column forward-refs the S-parameter reduction to its own
   output-product column. Routed (not authored): combinator-miner / the output-product
   column. (Appended to `scaffolding/open-questions.md`.)

2. **Driven output-product (S-parameter) column.** The driven feature's stage-3
   reduction is the S-parameter / frequency-response output product, deliberately
   forward-ref'd as `sparameter_reduce` (L4) / `sparameter_response` (L1) plain-text —
   its own output-product column lands a later cycle (the output-products are a named
   FEATURE-SURFACE SPINE scope). When that column lands, the driven L4/L1/L0 chapters'
   stage-3 down-link rows upgrade from `forward-ref` plain-text to live links, and the
   driven column may become eligible to promote past `seed` (all composed constituents
   firm). Tracked as the feature-spine status-aggregation clean-test contingency. (No
   new OQ — folded into the existing feature-spine continuation.)

3. **Sole-owner cohort dependency (driven/transient/eigenmode parallel-blind).** This
   dispatch owns the index-matrix + SUMMARY rows for ALL THREE driver columns, but D3
   (transient) / D4 (eigenmode) author their chapter FILES independently this same
   cycle. The transient/eigenmode index/SUMMARY rows are dead links until their chapter
   files land — the integrator dependency notes in changes 4–5 specify the defang
   (index table) / omit (SUMMARY) fallback if the cohort does not land together. This is
   the parallel-blind-shared-index guard the layer indexes carry, applied to the feature
   matrix. (No new OQ — the integrator-note channel handles the batch-ordering
   contingency.)
