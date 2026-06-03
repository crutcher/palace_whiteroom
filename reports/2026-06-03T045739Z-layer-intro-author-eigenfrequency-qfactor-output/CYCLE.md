---
agent: layer-intro-author
invoked_at: 2026-06-03T045739Z
integrated_at: 2026-06-03T055824Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-075 D4. Applied clean — 3 new chapter files book/src/feature/eigenfrequency-qfactor.{L4,L1,L0}.md (status seed): the output-product leaf feature column composition-root, down-linking to the eigenmode driver column + the eigenfreq_qfactor_reduce per-mode scalar-table reduction (D3, on disk earlier this cycle). Chapter files only; feature/index.md matrix row + SUMMARY.md rows DEFERRED to cohort-owner D2 (orphan-row guard) — discharged by D2 landing same-cycle. citecheck 21 ok / 0 fail. retroactive 0. cargo make book exit 0, linkcheck2 clean."
scope: author the eigenfrequency-qfactor output-product feature column (L4 + L1 + L0)
status: pending
---

# CYCLE: eigenfrequency-qfactor output-product feature column

## Summary

Authored the **EIGENFREQUENCY+Q-FACTOR output-product feature column** — three new
composition-root chapters under `book/src/feature/`:
`eigenfrequency-qfactor.{L4,L1,L0}.md`. This is a **leaf feature column** of the
*output-product* sub-kind in the FEATURE-SURFACE SPINE's output-product cohort (uniform
`status: seed`), the **rank-1 per-mode-table sibling** of the rank-2 Gram output products
[capacitance](../../book/src/feature/capacitance.L4.md) /
[inductance](../../book/src/feature/inductance.L4.md).

The column is a composition root: inputs = config (the eigenmode problem) → output (the
per-mode `(f, Q)` table) → body (compose DOWN). The body composes:
1. the [`eigenmode`](../../book/src/feature/eigenmode.L4.md) driver column (the producing
   column — supplies the converged eigenpair family), and
2. the [`eigenfreq_qfactor_reduce`](../../book/src/L4/eigenfreq_qfactor_reduce.md)
   per-mode scalar-ratio reduction (the rough-in L4 verb authored THIS cycle by D3 — a live
   link; D3's `eigenfreq_qfactor_reduce.md` lands before this column at integration).

Per c074 D6, this is NOT a `gram_reduce` witness — it is a rank-1 per-mode scalar-ratio
table, not a rank-2 family-PAIR Gram grid (the closed-negative non-subsume, OQ
`gram-reduce-third-witness-probe-eigenmode-driven-postprocess`).

The full chapter bodies are staged as sibling files in this report directory; the integrator
copies them verbatim into `book/src/feature/` (they are `create`s — the files do not yet
exist on disk).

Canonical slug: **`eigenfrequency-qfactor`** (verified on disk: this is the exact slug
forward-referenced at `feature/eigenmode.L4.md:40,45,55,70`, `eigenmode.L1.md:36,41,57,61`,
`eigenmode.L0.md:29,36` — so D2's consolidated index/SUMMARY references will resolve).

Within-column ordering high→low (L4→L1→L0), DELIBERATELY NOT alphabetized.

## Proposed changes

Three new files (verbatim copies of the staged siblings in this report dir). All three are
`create` operations — none exists on disk.

```create:book/src/feature/eigenfrequency-qfactor.L4.md
[verbatim copy of reports/2026-06-03T045739Z-layer-intro-author-eigenfrequency-qfactor-output/eigenfrequency-qfactor.L4.md]
```

```create:book/src/feature/eigenfrequency-qfactor.L1.md
[verbatim copy of reports/2026-06-03T045739Z-layer-intro-author-eigenfrequency-qfactor-output/eigenfrequency-qfactor.L1.md]
```

```create:book/src/feature/eigenfrequency-qfactor.L0.md
[verbatim copy of reports/2026-06-03T045739Z-layer-intro-author-eigenfrequency-qfactor-output/eigenfrequency-qfactor.L0.md]
```

**Integrator note — staged-file copy:** the three chapter bodies are large and
citation-dense; rather than inline them in fenced `create` blocks (which risk
nested-fence truncation — the `proposed-changes-fence-encloses-full-body-guard` defect),
they are staged as **sibling files** in this report directory:
- `eigenfrequency-qfactor.L4.md`
- `eigenfrequency-qfactor.L1.md`
- `eigenfrequency-qfactor.L0.md`

Copy each verbatim to `book/src/feature/<same-name>`. Each contains `text`-fenced Haskell
composition blocks; copying the file verbatim avoids the nested-fence issue entirely.

## Ownership partition (DEFERRED rows)

Per the dispatch ownership partition, this report authors ONLY the 3 chapter files. The
following are **DEFERRED to D2** (the cohort owner this cycle, authoring the sparameters
column + the consolidated `feature/index.md` matrix + `# Feature surfaces` SUMMARY.md block
for BOTH new output-product columns):
- the `feature/index.md` matrix row for `eigenfrequency-qfactor` — **DEFERRED to D2** (NOT
  touched here).
- the three `# Feature surfaces` SUMMARY.md rows (`eigenfrequency-qfactor.{L4,L1,L0}`) —
  **DEFERRED to D2** (NOT touched here).

This is the parallel-blind-shared-index guard: a single dispatch owns the shared
`feature/index.md` + `# Feature surfaces` SUMMARY block for all columns landing this cycle.
D2's references will resolve because this column uses the canonical slug
`eigenfrequency-qfactor`.

The three new chapter files DO each need a SUMMARY.md entry to be reachable by the mdBook
build — those entries are part of D2's consolidated `# Feature surfaces` SUMMARY block.
If D2 does NOT enumerate the `eigenfrequency-qfactor.{L4,L1,L0}` rows (e.g. D2's scope
turns out to cover only the sparameters column), the integrator-finalize must add the three
SUMMARY rows at build-repair time (high→low order L4→L1→L0, the deliberate exception to
alpha-within-cohort) so the chapters are not orphaned — FLAGGED for the integrator to verify
the three rows are present after D2 applies.

## Supporting evidence

### Constituent down-links (composed DOWN)
- **Producing driver column:** [`eigenmode.L4`](../../book/src/feature/eigenmode.L4.md) /
  `.L1` / `.L0` (status `seed`) — supplies the converged eigenpair family. Read in full this
  dispatch; the stage-3 readout forward-references this exact `eigenfrequency-qfactor` slug.
- **Reduction verb:** [`eigenfreq_qfactor_reduce`](../../book/src/L4/eigenfreq_qfactor_reduce.md)
  (status `rough-in`) — authored THIS cycle by D3 (combinator-miner, report
  `2026-06-03T045739Z-combinator-miner-eigenfreq-qfactor-reduce`). Live link; D3's file
  lands before this column at integration (D3 owns the `L4/index.md` row + SUMMARY entry for
  the verb). Read D3's CYCLE.md this dispatch to align the signature + the rank-1-vs-Gram
  framing + the κ/un-transform citations verbatim.

### Sibling output-product precedents (house style)
- [`capacitance.{L4,L1,L0}`](../../book/src/feature/capacitance.L4.md) (c074 D-cap) — the
  unit-weight Gram output-product exemplar; the structural template for the three-level
  output-product column shape.
- [`inductance.{L4,L1,L0}`](../../book/src/feature/inductance.L4.md) (c074 D-ind) — the
  current-normalized Gram sibling.

### L0 citations — ALL self-verified on-disk via palace-codemap `read_range` this dispatch
- `palace/drivers/eigensolver.cpp:32-34` — `EigenSolver::Solve` decl (driver body to `:477`). ✓
- `palace/drivers/eigensolver.cpp:40-42` — K/C/M pencil assembly. ✓
- `palace/drivers/eigensolver.cpp:367` — `int num_conv = eigen->Solve()` (the single solve). ✓
- `palace/drivers/eigensolver.cpp:424` — readout loop `for (int i = 0; i < num_conv; i++)`. ✓
- `palace/drivers/eigensolver.cpp:427` — `omega = eigen->GetEigenvalue(i)`. ✓
- `palace/drivers/eigensolver.cpp:430-434` — linear-EVP `omega = std::sqrt(omega)` (μ = -λ² = ω²). ✓
- `palace/drivers/eigensolver.cpp:435-439` — quadratic-EVP `omega /= 1i` (λ = iω). ✓
- `palace/drivers/eigensolver.cpp:458` — `post_op.MeasureAndPrintAll(i, E, B, omega, …)`. ✓
- `palace/drivers/eigensolver.cpp:471-475` — loop close + `MFEM_VERIFY(num_conv >= …n)`. ✓
- `palace/models/postoperator.cpp:1172` — `void PostOperator<solver_t>::MeasureLumpedPortsEig() const` def. ✓ (the `template` line is `:1171`; range `:1171-1203` per dispatch scope spans template+def+body)
- `palace/models/postoperator.cpp:1175` — `if constexpr (solver_t == ProblemType::EIGENMODE)` guard. ✓
- `palace/models/postoperator.cpp:1177` — `freq_re = measurement_cache.freq.real()` (f = Re ω). ✓
- `palace/models/postoperator.cpp:1185-1191` — the κ/Q formula comment (`κ_mj = ½R_j I_mj²/E_m`, `Q_mj = ω_m/κ_mj`). ✓
- `palace/models/postoperator.cpp:1192` — `if (std::abs(data.R) > 0.0)` resistive-port test. ✓
- `palace/models/postoperator.cpp:1196-1198` — `resistor_power = 0.5·|R|·Re(I·conj(I))`. ✓
- `palace/models/postoperator.cpp:1199-1200` — `mode_port_kappa = copysign(resistor_power/energy_electric_all, …)`. ✓
- `palace/models/postoperator.cpp:1201-1203` — `quality_factor = (κ==0)? infinity() : freq_re/|κ|`. ✓
- `palace/models/postoperator.cpp:1204-1217` — the inductive-port EPR sibling (NOT a Q; `if (std::abs(data.L) > 0.0)` at `:1213-1217`). ✓

(Compositional claim only — these L0 ranges are the *site map* for the composed reduction;
the per-op algebraic claims live in the linked `eigenfreq_qfactor_reduce` + `eigenmode`
chapters, not restated here, per the feature-surface composition-root discipline.)

## Open questions / caveats

- **D3's `eigenfreq_qfactor_reduce` must land before this column** (ordering dependency).
  This column's stage-2 down-link `[`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md)`
  is a LIVE link; if D3's file is not yet on disk at integration the link is a `linkcheck2`
  build error. Integrator: apply D3's report (which `create`s
  `book/src/L4/eigenfreq_qfactor_reduce.md`) BEFORE or in the same finalize as this column.
  D3's CYCLE.md confirms it authors the file at dispatch. (If for any reason D3's file does
  NOT land, demote the two `eigenfreq_qfactor_reduce` live links in all three chapters to
  plain text `eigenfreq_qfactor_reduce *(rough-in; L4)*` per the
  `rough-in-rows-must-be-plain-text-when-anchor-missing` convention — but the expectation is
  it lands.)
- **κ-participation primitive not yet a firm L1 entry** (inherited from D3's OQ). The loss
  rate `κₘ = ½R|I|²/E` is folded as a closure in `eigenfreq_qfactor_reduce` but has no
  standalone L1 home; this is why the reduction is `rough-in` and the column is `seed`. The
  column will promote past `seed` only once `eigenfreq_qfactor_reduce` (and its folded
  primitives) firm up — recorded in the column's §Status. Not blocking; noted for the
  cycle-planner's foundation-backfill ranking. (D3 already filed the `participation-ratio`
  L1-primitive candidate; not re-filing.)
- **SUMMARY.md orphan-row guard** (see Ownership partition). The three chapter files need
  `# Feature surfaces` SUMMARY rows to be build-reachable; those rows are D2's consolidated
  block. Flagged for integrator-finalize to verify the three `eigenfrequency-qfactor.{L4,L1,L0}`
  rows are present (high→low order) after D2's block applies — add at build-repair if D2's
  scope omitted them.
