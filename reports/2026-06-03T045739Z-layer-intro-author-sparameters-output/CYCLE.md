---
agent: layer-intro-author
invoked_at: 2026-06-03T05:10:06Z
integrated_at: 2026-06-03T055824Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-075 D2 (output-product cohort OWNER). Applied clean — 3 new chapter files book/src/feature/sparameters.{L4,L1,L0}.md (status seed): the port-projection output-product column composition-root down-linking to the driven driver + the sparameter_reduce reduction. SOLE-owned the consolidated feature/index.md matrix rows for BOTH new columns (alpha-within cohort: capacitance < eigenfrequency-qfactor < inductance < sparameters) + REWROTE the index output-product cohort prose to the 3-reduction-shape taxonomy + the SUMMARY.md # Feature surfaces block (+6 rows, within-column high->low). HAPPY-PATH: D6 sparameter_reduce.md + D4 eigenfrequency-qfactor.* on disk before apply -> all live links + SUMMARY rows resolve, no fallback; the D4 orphan-row guard + D6 SUMMARY-registration-partition both DISCHARGED. citecheck 5 ok / 0 fail. retroactive 0. cargo make book exit 0, linkcheck2 clean."
scope: sparameters output-product feature column (3 chapters) + consolidated feature/index.md matrix + SUMMARY.md block for BOTH new output-product columns (sparameters + eigenfrequency-qfactor); cohort OWNER (cycle-075 D2, Wave 2)
status: pending
---

# CYCLE: sparameters output-product feature column (cohort OWNER)

## Summary

Authors the **S-PARAMETERS** output-product feature column `book/src/feature/sparameters.{L4,L1,L0}.md` — a composition-root in the FEATURE-SURFACE SPINE's OUTPUT-PRODUCT cohort (a **leaf feature column**, output-product sub-kind, uniform `status: seed`). The column composes:
- **upstream** = the [`driven`](driven) driver column (produces the per-ω solution family `[Eᵢ]`);
- **reduction** = `sparameter_reduce` (the port-projection reduction mined this cycle by D1 — projects each per-ω field onto the configured port modes → the complex scattering matrix `S`). This is the **port-projection sibling** of `gram_reduce`, NOT a `gram_reduce` weight specialization (per c074 D6: linear projection ≠ bilinear self-Gram; complex + non-symmetric + inhomogeneous self-term + directional port-kind scaling).

As **cohort OWNER** this cycle, D2 also consolidates (single-index-owner discipline):
- the `feature/index.md` matrix rows for BOTH new output-product columns — **sparameters** AND **eigenfrequency-qfactor** (D4's deferred-to-D2 row; canonical slug `eigenfrequency-qfactor`), placed under the existing `*output products*` sub-header in alpha order;
- the `book/src/SUMMARY.md` `# Feature surfaces` block rows for BOTH new columns (6 rows total; within-column high→low L4→L1→L0).

The three sparameters chapter bodies are staged as sibling files (`sparameters.{L4,L1,L0}.md` in this report dir) for verbatim copy by the integrator (avoids nested-fence truncation).

## Integrator dependency notes (READ FIRST)

1. **`book/src/L4/sparameter_reduce.md` IS created this cycle by D6 (harvester).** D1 (combinator-miner, `reports/2026-06-03T045739Z-combinator-miner-sparameter-reduce/CYCLE.md`) mines the **dep-map row** for `sparameter_reduce` in `L4/index.md` + cohort note; **D6** (`reports/2026-06-03T045739Z-harvester-sparameter-reduce-chapter/CYCLE.md`) authors the full `create:book/src/L4/sparameter_reduce.md` chapter (`firmness: rough-in`) THIS cycle. **Repair update (cycle-075 critique/repair):** because D6 lands the real chapter this cycle, the `sparameter_reduce` references in my 3 chapters have been **upgraded from plain-text to live links** `[`sparameter_reduce`](../L4/sparameter_reduce.md)` (per `upgrade-plain-text-ref-to-live-link-when-target-on-disk`). No stub is needed — D6's chapter is the real target. **Per-report apply order:** D6 (and D1's dep-map row) must be applied BEFORE D2 so the live links resolve; the build is validated at finalize after D6 lands, so the live links are safe. FALLBACK (only if D6 fails to land): downgrade the `sparameter_reduce` live links in my 3 chapters back to plain-text per `rough-in-forward-reference-must-be-plain-text-not-live-link`.

2. **`eigenfrequency-qfactor.{L4,L1,L0}.md` must be applied BEFORE my consolidated index/SUMMARY block.** D4 (`reports/2026-06-03T045739Z-layer-intro-author-eigenfrequency-qfactor-output/CYCLE.md`) `create:`s the three `book/src/feature/eigenfrequency-qfactor.{L4,L1,L0}.md` files (canonical slug `eigenfrequency-qfactor`, confirmed on-disk-staged this dispatch) and explicitly DEFERS its index row + 3 SUMMARY rows to me. My SUMMARY block + index matrix row reference those three files. **Per-report apply order: D4 before D2.** FALLBACK: if D4's three files are NOT on disk when this report applies, **omit the three `eigenfrequency-qfactor.*` SUMMARY rows** (a SUMMARY row to a missing file is a hard mdBook break) and **defang the `eigenfrequency-qfactor` index matrix row to plain-text** (no live links). The sparameters rows are independent (my own files land this cycle) and are unaffected by the fallback.

3. **My own three `sparameters.{L4,L1,L0}.md` files** land via the `create:` blocks below; their `# Feature surfaces` SUMMARY rows are in my consolidated block. They down-link only to on-disk files (`driven.{L4,L1}.md`, `L4/frequency_sweep.md`, `L4/gram_reduce.md`, `L4/ksp_solve.md`, `L1/bilinear-form.md`, `L1/ksp_solve.md`) plus `L4/sparameter_reduce.md` (live-linked after the cycle-075 repair upgrade; D6 lands it this cycle) — all verified resolvable under the D6-before-D2 apply order.

## Proposed changes

### (1) Create the three sparameters chapter files (verbatim copy from staged siblings)

```create:book/src/feature/sparameters.L4.md
[verbatim copy of reports/2026-06-03T045739Z-layer-intro-author-sparameters-output/sparameters.L4.md]
```

```create:book/src/feature/sparameters.L1.md
[verbatim copy of reports/2026-06-03T045739Z-layer-intro-author-sparameters-output/sparameters.L1.md]
```

```create:book/src/feature/sparameters.L0.md
[verbatim copy of reports/2026-06-03T045739Z-layer-intro-author-sparameters-output/sparameters.L0.md]
```

### (2) feature/index.md — matrix rows for BOTH new output-product columns (alpha within the output-product cohort)

The output-product sub-header block currently holds capacitance + inductance (c074). Alpha order within the output-product cohort is `capacitance < eigenfrequency-qfactor < inductance < sparameters` — so `eigenfrequency-qfactor` inserts after `capacitance`, and `sparameters` inserts after `inductance`.

```edit:book/src/feature/index.md
[old]:
| *output products* | | | |
| [capacitance](./capacitance.L4.md) | [L4 root](./capacitance.L4.md) | [L1 root](./capacitance.L1.md) | [L0 surface](./capacitance.L0.md) |
| [inductance](./inductance.L4.md) | [L4 root](./inductance.L4.md) | [L1 root](./inductance.L1.md) | [L0 surface](./inductance.L0.md) |
| *spine ROOT* | | | |
[new]:
| *output products* | | | |
| [capacitance](./capacitance.L4.md) | [L4 root](./capacitance.L4.md) | [L1 root](./capacitance.L1.md) | [L0 surface](./capacitance.L0.md) |
| [eigenfrequency-qfactor](./eigenfrequency-qfactor.L4.md) | [L4 root](./eigenfrequency-qfactor.L4.md) | [L1 root](./eigenfrequency-qfactor.L1.md) | [L0 surface](./eigenfrequency-qfactor.L0.md) |
| [inductance](./inductance.L4.md) | [L4 root](./inductance.L4.md) | [L1 root](./inductance.L1.md) | [L0 surface](./inductance.L0.md) |
| [sparameters](./sparameters.L4.md) | [L4 root](./sparameters.L4.md) | [L1 root](./sparameters.L1.md) | [L0 surface](./sparameters.L0.md) |
| *spine ROOT* | | | |
```

### (3) feature/index.md — cohort prose: record the two new output-product shapes

```edit:book/src/feature/index.md
[old]:
The **output-product cohort** (cycle-074) adds the first two **output-product leaf columns** — [`capacitance`](./capacitance.L4.md) and [`inductance`](./inductance.L4.md). These are a distinct shape from the driver columns: a driver column produces a *solution family*; an output-product column *consumes* a driver's solution family and *reduces* it to the user-facing physical product. Both compose the single L4 [`gram_reduce`](../L4/gram_reduce.md) symmetric-Gram reduction combinator, differing ONLY in the normalization weight — capacitance is the **voltage `w = 1`** specialization (`Cᵢⱼ = Vⱼᵀ K Vᵢ`, over the [`electrostatic`](./electrostatic.L4.md) driver's family), inductance the **current-normalized `w = 1/(Iᵢ Iⱼ)`** specialization (`Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`, over the [`magnetostatic`](./magnetostatic.L4.md) driver's family). Both stay `seed` (not promotable) because `gram_reduce` is itself `rough-in (test-coverage-bounded)`.

Still planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the remaining output products (S-params / eigenfreq + Q / fields) and wave-port / boundary-mode (the 6th `ProblemType` branch, authored as a co-equal leaf driver column under the lifecycle ROOT). Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
[new]:
The **output-product cohort** spans **three reduction shapes**, one reduction verb each — the output-product half of the spine is a small *algebra of family-reductions*. An output-product column is a distinct shape from a driver column: a driver column produces a *solution family*; an output-product column *consumes* a driver's solution family and *reduces* it to the user-facing physical product.

- **Energy symmetric-Gram (rank-2, family-PAIR)** — cycle-074: [`capacitance`](./capacitance.L4.md) + [`inductance`](./inductance.L4.md), the first two output-product leaf columns. Both compose the single L4 [`gram_reduce`](../L4/gram_reduce.md) symmetric-Gram reduction combinator, differing ONLY in the normalization weight — capacitance is the **voltage `w = 1`** specialization (`Cᵢⱼ = Vⱼᵀ K Vᵢ`, over the [`electrostatic`](./electrostatic.L4.md) driver's family), inductance the **current-normalized `w = 1/(Iᵢ Iⱼ)`** specialization (`Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`, over the [`magnetostatic`](./magnetostatic.L4.md) driver's family).
- **Port-projection (rank-2 matrix, but a LINEAR projection — NOT a Gram)** — cycle-075: [`sparameters`](./sparameters.L4.md), over the [`driven`](./driven.L4.md) driver's per-ω solution family. It composes the new [`sparameter_reduce`](../L4/sparameter_reduce.md) reduction (mined c075 D1, authored c075 D6, `rough-in`) — projecting each per-ω field onto the configured port-mode covectors `[sₖ]` and assembling the complex scattering matrix `S`, with the driving-port self-reflection (`S_jj ← S_jj − 1`) and the per-port-kind closing (lumped generalized-S impedance normalization; wave-port phase de-embedding). It is the **port-projection sibling** of `gram_reduce` (same `Matrix[p,p]` result shape, DIFFERENT fold: linear projection vs bilinear self-Gram; complex + non-symmetric + inhomogeneous self-term + directional scaling — the c074 D6 do-NOT-merge over-unification guard, honored), NOT a `gram_reduce` weight specialization.
- **Per-mode scalar-table (rank-1)** — cycle-075: [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md), over the [`eigenmode`](./eigenmode.L4.md) driver's converged-mode family. It composes the new `eigenfreq_qfactor_reduce` reduction (mined c075 D3, `rough-in`) — a per-mode `(f, Q)` map (`f = Re ω` un-transformed; `Q = ω/κ`), the reduce-to-scalar-TABLE member, structurally distinct from both the rank-2 family-PAIR Gram and the rank-2 port-projection.

All three output-product columns stay `seed` (not promotable) because each composed reduction verb is itself `rough-in` (a feature column may promote past `seed` only once ALL its composed constituents are firm).

Still planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the remaining output product (energy/field measurements) and wave-port / boundary-mode (the 6th `ProblemType` branch, authored as a co-equal leaf driver column under the lifecycle ROOT). Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
```

### (4) SUMMARY.md — `# Feature surfaces` block rows for BOTH new columns (within-column high→low; flat list, alpha-local within the output-product cohort)

The feature block is still a flat per-column list (small-Part guard; no by-kind nesting yet). Within the output-product cohort the existing order is capacitance, inductance; insert `eigenfrequency-qfactor` after the capacitance triple and `sparameters` after the inductance triple, keeping the cohort alpha-local. Within each column the level order is high→low (L4→L1→L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort.

```edit:book/src/SUMMARY.md
[old]:
- [capacitance — L4 composition-root](./feature/capacitance.L4.md)
- [capacitance — L1 composition-root](./feature/capacitance.L1.md)
- [capacitance — L0 ground-truth surface](./feature/capacitance.L0.md)
- [inductance — L4 composition-root](./feature/inductance.L4.md)
- [inductance — L1 composition-root](./feature/inductance.L1.md)
- [inductance — L0 ground-truth surface](./feature/inductance.L0.md)
- [lifecycle — L4 composition-root](./feature/lifecycle.L4.md)
[new]:
- [capacitance — L4 composition-root](./feature/capacitance.L4.md)
- [capacitance — L1 composition-root](./feature/capacitance.L1.md)
- [capacitance — L0 ground-truth surface](./feature/capacitance.L0.md)
- [eigenfrequency-qfactor — L4 composition-root](./feature/eigenfrequency-qfactor.L4.md)
- [eigenfrequency-qfactor — L1 composition-root](./feature/eigenfrequency-qfactor.L1.md)
- [eigenfrequency-qfactor — L0 ground-truth surface](./feature/eigenfrequency-qfactor.L0.md)
- [inductance — L4 composition-root](./feature/inductance.L4.md)
- [inductance — L1 composition-root](./feature/inductance.L1.md)
- [inductance — L0 ground-truth surface](./feature/inductance.L0.md)
- [sparameters — L4 composition-root](./feature/sparameters.L4.md)
- [sparameters — L1 composition-root](./feature/sparameters.L1.md)
- [sparameters — L0 ground-truth surface](./feature/sparameters.L0.md)
- [lifecycle — L4 composition-root](./feature/lifecycle.L4.md)
```

## Supporting evidence

### L0 citations (all self-verified on-disk via palace-codemap `read_range` this dispatch; citecheck `--scan` = 13 ok / 0 failing)

- `PostOperator<solver_t>::MeasureSParameter()` — def `postoperator.cpp:1246-1309` (`get_symbol_def`), meaningful body `:1246-1307` (cited per the prompt's `~:1246-1307` framing; def closing brace at `:1309` noted in L0 §Status). The S-matrix POST-PROCESS: driving-port self-reflection `vi.S.real(vi.S.real() − 1.0)` (lumped `:1275`, wave `:1297`); lumped generalized-S `vi.S *= std::sqrt(src_data.R / data.R)` (`:1280`, block `:1278-1281`); wave de-embed `vi.S *= std::exp(1i * kn0 * d_offset)` (`:1301-1302`); the single-excitation / non-mixed-port guard `:1256-1260` (`return` at `:1259`); driving-port index `measurement_cache.ex_idx` (`:1263`).
- Per-port S projection cached **before** post-process: lumped `vi.S = data.GetSParameter(*E)` `postoperator.cpp:1141` (in `MeasureLumpedPorts`); wave `vi.S = data.GetSParameter(*E)` `:1239` (in `MeasureWavePorts`). (Cross-checked the D1/c074-D6 ranges — these post-process steps all live inside the same verified `MeasureSParameter` body `:1246-1309`. **Repair note (cycle-075 critique/repair):** the interior pinpoints in this dispatch's first pass drifted low by 1–3 lines against ground truth; they were re-read directly from `reference/palace/palace/models/postoperator.cpp` (brace-boundary discipline) and corrected to: self-reflection lumped `:1275` / wave `:1297`; lumped generalized-S scale `:1280` (block `:1278-1281`); wave de-embed `:1301-1302`; `drive_port_idx = measurement_cache.ex_idx` `:1263`; non-mixed-port guard `return` `:1259`. These now harmonize with the D6 harvester chapter's verified line-map. The enclosing ranges (`:1246-1309`, `:283-294`, `:780-793`, `:1141`, `:1239`) were correct and unchanged.)
- Lumped port-mode projection verb: `LumpedPortData::GetSParameter` `lumpedportoperator.cpp:283-294` (body), the inner product `std::complex<double> dot((*s) * E.Real(), 0.0)` (`:287`) + imag `:290` + `Mpi::GlobalSum` `:292`. `--anchor 'GetSParameter'` = ok (anchor at :283 in range).
- Wave port-mode projection verb: `WavePortData::GetSParameter` `waveportoperator.cpp:780-793` (body), the surface-integral `(E × H_inc⋆)·n = E·(−n × H_inc⋆)` form (`:782-783`), transfer `:787-788`, complex dot `:789-790`, `Mpi::GlobalSum` `:791`. `--anchor 'GetSParameter'` = ok (anchor at :780 in range).
- Driven driver column producing the per-ω family: `drivensolver.cpp:37-229` (Solve + SweepUniform), per-ω solve loop `:168-196` (cited from the on-disk `feature/driven.L4.md` constituent down-link table, the producing-column reference).

### Constituent chapters (existing on-disk; down-linked, not re-authored)

- `book/src/feature/driven.L4.md` / `driven.L1.md` (the producing driver column; `## Status: seed`, on-disk) — supplies the per-ω solution family `[Eᵢ]`.
- `book/src/L4/frequency_sweep.md`, `book/src/L4/ksp_solve.md`, `book/src/L1/ksp_solve.md` (firm; orientation references within the driven-column prose).
- `book/src/L4/gram_reduce.md` (rough-in (test-coverage-bounded); referenced as the contrast/sibling reduction, NOT composed).
- `book/src/L1/bilinear-form.md` (rough-in; the L1 port-mode projection home — the linear functional `⟨sₖ, E⟩` instantiated as the left-fixed partial application of the bilinear form at the port covector).

### Output-product reduction-shape taxonomy (from the c074 D6 / c075 D1 / c075 D3 ledger)

| Shape | rank | reduction verb | over driver | cycle |
|---|---|---|---|---|
| energy symmetric-Gram (family-PAIR) | 2 | `gram_reduce` (w=1 / w=1/(IᵢIⱼ)) | electrostatic / magnetostatic | c074 |
| port-projection (linear, complex matrix) | 2 | `sparameter_reduce` | driven | c075 (this column) |
| per-mode scalar table | 1 | `eigenfreq_qfactor_reduce` | eigenmode | c075 (D3/D4) |

This column is the **port-projection** member — the c074 D6 closed-negative over-unification guard (S-params NOT a `gram_reduce` specialization) is honored: a distinct sibling reduction verb, NOT a `gram_reduce` weight axis extension.

## Open questions / caveats

(Appended to `scaffolding/open-questions.md` this dispatch.)

- **`sparameters-column-seed-promotion-coupled-to-sparameter-reduce-firming` (c075 D2)** — the sparameters output-product column cannot promote past `seed` until `sparameter_reduce` firms past `rough-in` (its per-port projection L1 home firms — see the c075 D1 `sparameter-reduce-l1-port-projection-home` OQ — AND a dedicated S-parameter-reduction test/lowering-verifier pass exists). *Trigger:* a `sparameter_reduce`-firming cycle re-checks the sparameters column's `seed`→promotion eligibility. Composes with `sparameter-reduce-l1-port-projection-home`. LOW/coupling-record. `cycle-planner`/`lifter`.
- **`sparameters-down-link-stub-upgrade-when-sparameter-reduce-lands` (c075 D2 — RESOLVED at c075 critique/repair)** — the 3 sparameters chapters originally referenced `sparameter_reduce` as plain-text (no anchor; D1 deferred the chapter to a harvester). D6 (harvester) authors the real `book/src/L4/sparameter_reduce.md` (rough-in) THIS cycle, so the repairer upgraded the plain-text refs in `sparameters.{L4,L1,L0}.md` to `../L4/sparameter_reduce.md` live links via `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (apply-order D6-before-D2; plain-text-downgrade fallback if D6 fails to land). Disposition: CLOSE on integration (no stub needed — the real chapter lands). LOW/hygiene.
- **`feature-part-by-kind-nesting-output-product-cohort-grouping` (carried from c074 D2)** — the output-product cohort is now 4 columns (capacitance/eigenfrequency-qfactor/inductance/sparameters) plus the 5 driver columns + spine ROOT in a still-flat `feature/index.md` matrix + flat SUMMARY list (small-Part guard, `feature/index.md` line 26). The Part is approaching the size where the directive-3 by-kind grouping should nest it (driver-leaf / output-product / spine-ROOT kinds, each with an intro page; the FEATURE-SURFACE within-column high→low ordering exception preserved). Flagged for the meta-phase structural-reorg wave. LOW/structural. `meta-phase`/`layer-intro-author`.
