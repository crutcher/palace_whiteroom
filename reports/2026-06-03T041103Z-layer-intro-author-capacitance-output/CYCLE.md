---
agent: layer-intro-author
invoked_at: 2026-06-03T041103Z
integrated_at: 2026-06-03T044543Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-074 D2 (output-product cohort OWNER). Applied clean — 3 new chapter files (feature/capacitance.{L4,L1,L0}.md, status seed) composing L4 gram_reduce at w=1 voltage over the electrostatic driver column; SOLE-owned the feature/index.md matrix (+output-product cohort rows with *output products* sub-header) + the SUMMARY.md # Feature surfaces block (+6 rows capacitance+inductance, after the 5 leaf drivers, before lifecycle ROOT, within-column high->low). HAPPY-PATH: inductance.* on disk before apply -> all live links, no defang. citecheck 1 ok / 1 non-blocking AMBIG (bare-basename index.md:26 prose self-reference, not a load-bearing citation). retroactive 0. cargo make book exit 0, linkcheck2 clean."
scope: capacitance output-product feature column (cycle-074 D2; output-product cohort OWNER)
status: pending
---

# CYCLE: capacitance output-product feature column (+ consolidated index/SUMMARY for both output-product columns)

## Summary

Authors the **capacitance** output-product feature column — `book/src/feature/capacitance.{L4,L1,L0}.md` — a composition-root of the **output-product** sub-kind (a **leaf feature column**) in the FEATURE-SURFACE SPINE. The capacitance product down-links to (1) the [`electrostatic`](book/src/feature/electrostatic.L4.md) **producing driver column** (which supplies the per-terminal solution family `[Vᵢ]`) and (2) the L4 [`gram_reduce`](book/src/L4/gram_reduce.md) symmetric-Gram reduction combinator at the **voltage `w = 1` specialization** (`Cᵢⱼ = Vⱼᵀ K Vᵢ`). Uniform `status: seed` (the column stays `seed`, not promotable, because `gram_reduce` is itself `rough-in (test-coverage-bounded)` — its folded L1 bilinear primitives are rough-in and no dedicated Gram-reduction test exists).

As the **output-product cohort OWNER**, this report ALSO consolidates the shared index/SUMMARY wiring for BOTH output-product columns (capacitance + inductance):
- `book/src/feature/index.md` — matrix rows for capacitance AND inductance (D3's deferred-to-owner row), plus the prose update demoting the "output products still planned" line and introducing the output-product cohort.
- `book/src/SUMMARY.md` — `# Feature surfaces` block rows for BOTH new columns (within-column high→low L4/L1/L0, deliberate non-alpha exception), placed AFTER the 5 leaf drivers and BEFORE the lifecycle ROOT (leaf-features-then-ROOT reading order).

The three capacitance chapter bodies are staged as sibling files (integrator copies verbatim — avoids nested-fence truncation):
- `reports/2026-06-03T041103Z-layer-intro-author-capacitance-output/staging/capacitance.L4.md`
- `reports/2026-06-03T041103Z-layer-intro-author-capacitance-output/staging/capacitance.L1.md`
- `reports/2026-06-03T041103Z-layer-intro-author-capacitance-output/staging/capacitance.L0.md`

## Integrator dependency note (READ BEFORE APPLYING)

This report references `book/src/feature/inductance.{L4,L1,L0}.md`, authored by **D3 (inductance)** THIS SAME cycle, in THREE distinct places (all three depend on D3 landing first):
1. The `SUMMARY.md` block — three `inductance — *` rows.
2. The `index.md` matrix — the `inductance` row (live links).
3. **An in-body live link inside the staged `capacitance.L4.md` §2 prose (`capacitance.L4.md:~36`): `[inductance.L4](./inductance.L4.md)`** — naming the magnetostatic `w = 1/(IᵢIⱼ)` sibling specialization. This is an INDEPENDENT hard `linkcheck2` target, NOT covered by the SUMMARY/index defangs.

**HAPPY PATH (the plan's ordering — D3 applied BEFORE D2 this same cycle):** all three references resolve at integration time. The in-body link is deliberately kept live (D3 lands first), and the index/SUMMARY rows resolve. No defanging needed. This is the expected path.

**FALLBACK (D3 files NOT on disk when this report is applied):** A `SUMMARY.md` row pointing at a missing file is a HARD mdBook break, and an `index.md` OR in-body live-link to a missing file is a hard `linkcheck2` error. If `book/src/feature/inductance.L4.md` (etc.) are NOT present when applying THIS report, ALL THREE references must be defanged:
1. In the `SUMMARY.md` proposed change: **OMIT** the three `inductance — *` rows (apply only the three `capacitance — *` rows). Re-add the inductance rows in a follow-up once D3 lands.
2. In the `index.md` matrix proposed change: **defang** the inductance row to plain-text (replace the `[inductance](...)` / `[L4 root](...)` links with plain-text `inductance` / `L4 root *(rough-in; D3 pending)*`).
3. In the staged `capacitance.L4.md:~36` §2 prose: **defang** the `[inductance.L4](./inductance.L4.md)` reference to plain-text `inductance.L4` (drop the link target; keep the prose).
The capacitance rows/links are always safe (this report's own staged files land in the same cycle).

## Proposed changes

### 1. Create `book/src/feature/capacitance.L4.md`

Copy verbatim from `reports/2026-06-03T041103Z-layer-intro-author-capacitance-output/staging/capacitance.L4.md`.

### 2. Create `book/src/feature/capacitance.L1.md`

Copy verbatim from `reports/2026-06-03T041103Z-layer-intro-author-capacitance-output/staging/capacitance.L1.md`.

### 3. Create `book/src/feature/capacitance.L0.md`

Copy verbatim from `reports/2026-06-03T041103Z-layer-intro-author-capacitance-output/staging/capacitance.L0.md`.

### 4. `book/src/feature/index.md` — matrix: add output-product cohort rows

```edit:book/src/feature/index.md
[old]: | [eigenmode](./eigenmode.L4.md) | [L4 root](./eigenmode.L4.md) | [L1 root](./eigenmode.L1.md) | [L0 surface](./eigenmode.L0.md) |
| [lifecycle](./lifecycle.L4.md) | [L4 root](./lifecycle.L4.md) | [L1 root](./lifecycle.L1.md) | [L0 surface](./lifecycle.L0.md) |
[new]: | [eigenmode](./eigenmode.L4.md) | [L4 root](./eigenmode.L4.md) | [L1 root](./eigenmode.L1.md) | [L0 surface](./eigenmode.L0.md) |
| *output products* | | | |
| [capacitance](./capacitance.L4.md) | [L4 root](./capacitance.L4.md) | [L1 root](./capacitance.L1.md) | [L0 surface](./capacitance.L0.md) |
| [inductance](./inductance.L4.md) | [L4 root](./inductance.L4.md) | [L1 root](./inductance.L1.md) | [L0 surface](./inductance.L0.md) |
| *spine ROOT* | | | |
| [lifecycle](./lifecycle.L4.md) | [L4 root](./lifecycle.L4.md) | [L1 root](./lifecycle.L1.md) | [L0 surface](./lifecycle.L0.md) |
```

### 5. `book/src/feature/index.md` — prose: demote "output products still planned"; introduce the output-product cohort

```edit:book/src/feature/index.md
[old]: The **driven**, **transient**, and **eigenmode** driver columns (cycle-073) complete the 5-driver leaf-column set: with electrostatic + magnetostatic (the fixed-operator pair) these three add the **operator-VARYING** corner (driven — the per-ω rebuild + `SetOperators`-inside-the-loop [`frequency_sweep`](../L4/frequency_sweep.md) map), the **state-threaded sequential-fold** corner (transient — the [`fold_solve`](../L4/fold_solve.md) time-step march), and the **opaque-library black-box** corner (eigenmode — the SLEPc eigen-iteration). The driven column is the first whose three L4 composition stages all compose FIRM combinators (the assemble basis, the per-ω operand verb, and the operator-varying solve map are each firm). Still planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the output products (S-params / capacitance / inductance / eigenfreq + Q / fields) and wave-port / boundary-mode (the 6th `ProblemType` branch, authored as a co-equal leaf driver column under the lifecycle ROOT). Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
[new]: The **driven**, **transient**, and **eigenmode** driver columns (cycle-073) complete the 5-driver leaf-column set: with electrostatic + magnetostatic (the fixed-operator pair) these three add the **operator-VARYING** corner (driven — the per-ω rebuild + `SetOperators`-inside-the-loop [`frequency_sweep`](../L4/frequency_sweep.md) map), the **state-threaded sequential-fold** corner (transient — the [`fold_solve`](../L4/fold_solve.md) time-step march), and the **opaque-library black-box** corner (eigenmode — the SLEPc eigen-iteration). The driven column is the first whose three L4 composition stages all compose FIRM combinators (the assemble basis, the per-ω operand verb, and the operator-varying solve map are each firm).

The **output-product cohort** (cycle-074) adds the first two **output-product leaf columns** — [`capacitance`](./capacitance.L4.md) and [`inductance`](./inductance.L4.md). These are a distinct shape from the driver columns: a driver column produces a *solution family*; an output-product column *consumes* a driver's solution family and *reduces* it to the user-facing physical product. Both compose the single L4 [`gram_reduce`](../L4/gram_reduce.md) symmetric-Gram reduction combinator, differing ONLY in the normalization weight — capacitance is the **voltage `w = 1`** specialization (`Cᵢⱼ = Vⱼᵀ K Vᵢ`, over the [`electrostatic`](./electrostatic.L4.md) driver's family), inductance the **current-normalized `w = 1/(Iᵢ Iⱼ)`** specialization (`Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`, over the [`magnetostatic`](./magnetostatic.L4.md) driver's family). Both stay `seed` (not promotable) because `gram_reduce` is itself `rough-in (test-coverage-bounded)`.

Still planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the remaining output products (S-params / eigenfreq + Q / fields) and wave-port / boundary-mode (the 6th `ProblemType` branch, authored as a co-equal leaf driver column under the lifecycle ROOT). Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
```

### 6. `book/src/SUMMARY.md` — `# Feature surfaces` block: add both output-product columns

```edit:book/src/SUMMARY.md
[old]: - [eigenmode — L4 composition-root](./feature/eigenmode.L4.md)
- [eigenmode — L1 composition-root](./feature/eigenmode.L1.md)
- [eigenmode — L0 ground-truth surface](./feature/eigenmode.L0.md)
- [lifecycle — L4 composition-root](./feature/lifecycle.L4.md)
[new]: - [eigenmode — L4 composition-root](./feature/eigenmode.L4.md)
- [eigenmode — L1 composition-root](./feature/eigenmode.L1.md)
- [eigenmode — L0 ground-truth surface](./feature/eigenmode.L0.md)
- [capacitance — L4 composition-root](./feature/capacitance.L4.md)
- [capacitance — L1 composition-root](./feature/capacitance.L1.md)
- [capacitance — L0 ground-truth surface](./feature/capacitance.L0.md)
- [inductance — L4 composition-root](./feature/inductance.L4.md)
- [inductance — L1 composition-root](./feature/inductance.L1.md)
- [inductance — L0 ground-truth surface](./feature/inductance.L0.md)
- [lifecycle — L4 composition-root](./feature/lifecycle.L4.md)
```

## Supporting evidence

### Constituent vocabulary (down-links)

- **Producing driver column:** `book/src/feature/electrostatic.{L4,L1,L0}.md` (on disk; the fixed-operator electrostatic solve producing `[Vᵢ]`).
- **L4 reduction combinator:** `book/src/L4/gram_reduce.md` (on disk; `rough-in (test-coverage-bounded)`). The capacitance product is `gram_reduce`'s voltage `w = 1` specialization — the §Specialization "Electrostatic capacitance" bullet at `gram_reduce.md:167-171` (the literal "positive witness 1" label is at `:255`). The combinator's signature/laws are stated there; this column carries only the compositional claim.
- **Folded L1 bilinear primitives:** `book/src/L1/matrix-weighted-norm.md` (rough-in (test-coverage-bounded), diagonal), `book/src/L1/bilinear-form.md` (rough-in, off-diagonal).

### L0 ground truth (all self-verified on-disk via citecheck this dispatch)

`palace/drivers/electrostaticsolver.cpp`, `ElectrostaticSolver::PostprocessTerminals`:
- `:95` — the `PostprocessTerminals(post_op, laplace_op.GetSources(), V)` call site (after the terminal loop) [citecheck ok]
- `:100` — `void ElectrostaticSolver::PostprocessTerminals(...)` def [citecheck ok]
- `:111` — `mfem::DenseMatrix C(V.size()), Cm(V.size())` allocation [citecheck ok]
- `:118-119` — diagonal `M_elec->Mult(V_gf, D_gf)` + `linalg::Dot(...)` → `Cᵢᵢ = Vᵢᵀ K Vᵢ` [citecheck ok]
- `:123` — off-diagonal inner loop `for (int j = i + 1; ...)` [citecheck ok]
- `:126` — off-diagonal `C(i,j) = linalg::Dot(...)` → `Cᵢⱼ = Vⱼᵀ K Vᵢ` [citecheck ok]
- `:132-134` — lower-triangle copy `C(i,j) = C(j,i)` (the symmetric mirror) [citecheck ok]
- `:139-140` — `mfem::DenseMatrix Cinv(C); Cinv.Invert()` (the `gram_inverse` consumer) [citecheck ok]
- `:21-22` (sig) / `:21-98` (body) — `ElectrostaticSolver::Solve` (the producing driver) [the `Solve` token sits on `:22`; signature `:21-22`]
- `:97` — `return {indicator, laplace_op.GlobalTrueVSize()}` [citecheck ok]

citecheck `--scan` pass on all three staged files: L4 9/9 ok, L1 7/7 ok, L0 5/5 ok (0 failing).

### Status discipline

- Uniform `status: seed` per the FEATURE-SURFACE SPINE batch-22 codification (no `(exemplar)` qualifier — the prose names the output-product leaf sub-kind). NOTE: the on-disk electrostatic/magnetostatic columns still carry the pre-codification `status: seed (exemplar)` token; the capacitance column uses the codified `status: seed`. (Not in scope to re-token the existing columns — flagged as an OQ below.)
- The column stays `seed` (not promotable past it) because `gram_reduce` — its sole reduction constituent — is `rough-in (test-coverage-bounded)`. Per the role-spec, a feature column may promote past `seed` only once ALL its composed constituents are firm.

## Open questions / caveats

1. **Token drift on the existing feature columns.** The electrostatic / magnetostatic / driven / transient / eigenmode / lifecycle columns on disk carry `status: seed (exemplar)` (pre-batch-22 token); the batch-22 codification mandates uniform `status: seed` (no qualifier; prose names the sub-kind). The capacitance column (this report) uses the codified `status: seed`. A future low-priority sweep should re-token the 6 existing columns to drop the `(exemplar)` qualifier for uniformity. NOT done here (one-column-per-invocation; out of scope). Appended to open-questions.

2. **`gram_reduce` shared-combinator status couples capacitance + inductance promotion.** Both output-product columns down-link the SAME `gram_reduce` combinator; neither can promote past `seed` until `gram_reduce` firms (its rough-in L1 primitives firm up AND a dedicated Gram-reduction test or lowering-verifier pass lands — `gram_reduce.md` §Status promotion route). This is the expected coupling (one reduction, two weight specializations); recording it so a future promotion cycle promotes both columns together with `gram_reduce`.

3. **Output-product cohort matrix grouping.** I added inline sub-header rows (`*output products*` / `*spine ROOT*`) to the existing flat matrix rather than splitting into separate tables, since the Feature Part "does not use by-kind nesting yet (small-Part guard)" per `index.md:26`. When the directive-3 by-kind grouping eventually nests this Part, the output-product cohort becomes a proper sub-chapter grouping with its own intro page (the leaf-driver / output-product / spine-ROOT kinds). Flagged for the meta-phase's structural reorg, not done here.
