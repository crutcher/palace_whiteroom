---
agent: lifter
invoked_at: 2026-06-03T041103Z
integrated_at: 2026-06-03T044543Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-074 D1. Applied clean — pure in-place replace-and-propagate: electrostatic.L4 + magnetostatic.L4 stage-(3) reduction prose + §Constituent-down-links cell + composes: frontmatter + §Status reasoning re-anchored DOWN to the rough-in-track L4 gram_reduce (electrostatic w=1, magnetostatic w=1/(IiIj)); rough-in L1 matrix-weighted-norm/bilinear-form down-links kept as the fold's building blocks. The coupled replace-and-propagate is now complete (combinator-as-entry c073 + both columns linking DOWN c074). Discharges OQ gram-reduce-feature-chapter-reanchor-sequences-to-c074 (note appended). D5 boundary honored (mid-paragraph §Status edit disjoint from D5's head-token edit). citecheck 9 ok/0 fail. retroactive 0. cargo make book exit 0."
scope: feature-surface re-anchor — electrostatic.L4 + magnetostatic.L4 reduction stage → L4 gram_reduce (the c073-deferred replace-and-propagate close)
status: pending
inputs:
  - book/src/feature/electrostatic.L4.md
  - book/src/feature/magnetostatic.L4.md
  - book/src/L4/gram_reduce.md
  - scaffolding/open-questions.md (OQ gram-reduce-feature-chapter-reanchor-sequences-to-c074, c073 D1)
---

# CYCLE: Re-anchor electrostatic.L4 + magnetostatic.L4 reduction stage onto the landed L4 gram_reduce

## Summary

`gram_reduce` (`book/src/L4/gram_reduce.md`) landed c073 D1 as a `rough-in (test-coverage-bounded)` L4 combinator — the shared operator-weighted symmetric-Gram reduction `Gᵢⱼ = w(i,j)·(xⱼᵀ K xᵢ)` whose §Specialization already names the two feature columns as `w = 1` (electrostatic) / `w = 1/(IᵢIⱼ)` (magnetostatic) specializations. But the two feature columns it was mined from still describe stage (3) bottom-up as "two rough-in L1 primitives / no dedicated L4 reduction combinator yet — a forward mine." That is the mine-and-strand smell the VOCABULARY-SHIFT redirect §1 (combinator-primary, replace-and-propagate) forbids: the combinator is the entry, the per-pipeline reduction must read as a *specialization through it*. This is a **pure re-anchoring pass** — the three-stage composition structure of both columns is untouched; only the stage-(3) vocabulary firms up to cite the landed combinator. The kept-down-link discipline is preserved: the rough-in L1 `matrix-weighted-norm` / `bilinear-form` rows stay (they are the building blocks the `gram_reduce` fold composes, and they are exactly *why* `gram_reduce` is rough-in), reframed as the fold's constituents rather than as a direct hand-rolled reduction. The §Status `seed` / `seed (exemplar)` token at the head is **left untouched** (D5's normalization job this cycle); only the reduction-reasoning prose inside §Status is re-anchored.

## Proposed changes

### electrostatic.L4.md

Four loci: `composes:` frontmatter (add the gram_reduce down-link), §reduction prose (line 40), §"Constituent down-links" table (line 64), §Status reduction-reasoning prose (line 68).

```edit:book/src/feature/electrostatic.L4.md
[old]: composes:
  - book/src/L4/fe_assemble.md (firm — assemble K once: the assemble-fold combinator)
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-terminal map)
  - book/src/L4/ksp_solve.md (firm — the per-element solve cap solve_family maps)
[new]: composes:
  - book/src/L4/fe_assemble.md (firm — assemble K once: the assemble-fold combinator)
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-terminal map)
  - book/src/L4/ksp_solve.md (firm — the per-element solve cap solve_family maps)
  - book/src/L4/gram_reduce.md (rough-in (test-coverage-bounded) — the operator-weighted symmetric-Gram output-product reduction; capacitance = the w = 1 voltage specialization)
```

```edit:book/src/feature/electrostatic.L4.md
[old]: 3. **Capacitance-matrix reduction** — the quadratic-form reduction `Cᵢⱼ = Vⱼᵀ K Vᵢ` over the solution family, producing the (symmetric) Maxwell capacitance matrix `C` (the COMSOL energy formulation: `Cᵢᵢ = 2Uₑ(Vᵢ)/Vᵢ²`, off-diagonals from the cross energy). At L4 this is a `map`-then-`reduce` over the solution-family pairs using the operator-weighted-bilinear primitives (the rough-in L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `Vᵢᵀ K Vᵢ` on the diagonal, the rough-in L1 [`bilinear-form`](../L1/bilinear-form.md) `Vⱼᵀ K Vᵢ` off-diagonal) — there is no *new* L4 combinator here; the reduction is a fold of these bilinear-form evaluations over the family-pair grid, with the result inverted (`Cinv = C⁻¹`, LAPACK) for the alternate Maxwell form. This stage is the **output product** half of the composition root; its dedicated L4 reduction-combinator (if the cross-pipeline post-processing proves to share a shape with the magnetostatic inductance reduction) is a forward mine, not authored here (see Open questions). L0: `PostprocessTerminals` (`electrostaticsolver.cpp:95`, def `:100`; the energy-form `Mult`/`Dot` at `:118-127`, the inverse at `:139-140`).
[new]: 3. **Capacitance-matrix reduction** — [`gram_reduce`](../L4/gram_reduce.md) (**rough-in (test-coverage-bounded)**), the `w = 1` voltage specialization. The capacitance matrix is the operator-weighted symmetric-Gram reduction `Cᵢⱼ = Vⱼᵀ K Vᵢ` over the solution family `[Vᵢ]` — the unit-weight (`w i j = 1`) member of the shared L4 reduction `gram_reduce K xs w = Gᵢⱼ = w(i,j)·(xⱼᵀ K xᵢ)` (the COMSOL energy formulation: `Cᵢᵢ = 2Uₑ(Vᵢ)/Vᵢ² ≡ ×1`, off-diagonals from the cross energy; named electrostatic specialization at `book/src/L4/gram_reduce.md:167-171`). `gram_reduce` is the **entry** (replace-and-propagate, CLAUDE.md §VOCABULARY-SHIFT redirect); the capacitance reduction re-expresses THROUGH it as the `w = 1` corner, NOT as a hand-rolled fold. The combinator's `map`-then-`reduce` body composes the rough-in L1 building blocks — the diagonal `Vᵢᵀ K Vᵢ` is the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) radicand, the off-diagonal `Vⱼᵀ K Vᵢ` is the [`bilinear-form`](../L1/bilinear-form.md) — folded over the upper-triangle family-pair grid with the symmetric mirror; `gram_reduce` is rough-in BECAUSE those folded constituents are. The inverse (`Cinv = C⁻¹`, LAPACK) is the `gram_inverse` consumer downstream of the reduction, not part of it. This stage is the **output product** half of the composition root. L0: `PostprocessTerminals` (`electrostaticsolver.cpp:95`, def `:100`; the energy-form `Mult`/`Dot` at `:118-127`, the inverse at `:139-140`).
```

```edit:book/src/feature/electrostatic.L4.md
[old]: | capacitance reduction (Vⱼᵀ K Vᵢ) | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) / [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — no dedicated L4 reduction combinator yet | rough-in / rough-in (L1) | `electrostaticsolver.cpp:95, 100-138` |
[new]: | capacitance reduction (Vⱼᵀ K Vᵢ) | [`gram_reduce`](../L4/gram_reduce.md) (`w = 1` voltage specialization) — folding L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (diagonal) / [`bilinear-form`](../L1/bilinear-form.md) (off-diagonal) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:95, 100-138` |
```

```edit:book/src/feature/electrostatic.L4.md
[old]: stage (3) composes L1 bilinear-form primitives (rough-in diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md); the capacitance reduction has no dedicated L4 reduction combinator yet — a forward mine, not a blocker, since the reduction is a plain fold of evaluations).
[new]: stage (3) is the rough-in-track L4 [`gram_reduce`](../L4/gram_reduce.md) reduction (the `w = 1` voltage specialization), which folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) building blocks over the family-pair grid — `gram_reduce` is rough-in (test-coverage-bounded) precisely because those folded constituents are; not a blocker, the reduction composes cleanly as a fold of evaluations.
```

### magnetostatic.L4.md

Four loci, mirroring electrostatic: `composes:` frontmatter, §reduction prose (line 40), §"Constituent down-links" table (line 64), §Status reduction-reasoning prose (line 68).

```edit:book/src/feature/magnetostatic.L4.md
[old]: composes:
  - book/src/L4/fe_assemble.md (firm — assemble curl-curl K once: the assemble-fold combinator)
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-source map)
  - book/src/L4/ksp_solve.md (firm — the per-source solve cap solve_family maps)
[new]: composes:
  - book/src/L4/fe_assemble.md (firm — assemble curl-curl K once: the assemble-fold combinator)
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-source map)
  - book/src/L4/ksp_solve.md (firm — the per-source solve cap solve_family maps)
  - book/src/L4/gram_reduce.md (rough-in (test-coverage-bounded) — the operator-weighted symmetric-Gram output-product reduction; inductance = the w = 1/(IᵢIⱼ) current-normalized specialization)
```

```edit:book/src/feature/magnetostatic.L4.md
[old]: 3. **Inductance-matrix reduction** — the B-weighted Gram `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` over the solution family, producing the (symmetric) Maxwell inductance matrix `M` (the COMSOL magnetic-energy formulation: `Mᵢᵢ = 2Uₘ(Aᵢ)/Iᵢ²`, off-diagonals from the cross energy, normalized by the excitation currents `Iᵢ`). At L4 this is a `map`-then-`reduce` over the solution-family pairs using the operator-weighted-bilinear primitives — the rough-in L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `Aᵢᵀ K Aᵢ` on the diagonal, the rough-in L1 [`bilinear-form`](../L1/bilinear-form.md) `Aⱼᵀ K Aᵢ` off-diagonal — each divided by the current normalization `Iᵢ Iⱼ`. There is no *new* L4 combinator here; the reduction is a fold of these bilinear-form evaluations over the family-pair grid, with the result inverted (`Minv = M⁻¹`, LAPACK) for the alternate Maxwell form. This stage is the **output product** half of the composition root; its dedicated L4 reduction-combinator — if the cross-pipeline post-processing proves to share a shape with the electrostatic capacitance reduction (it does, modulo the diagonal current-vs-voltage normalization weight) — is a forward mine, not authored here (see Open questions). L0: `PostprocessTerminals` (`magnetostaticsolver.cpp:108`, def `:110`; the energy-form `Mult`/`Dot` at `:129-138`, the inverse at `:151-152`).
[new]: 3. **Inductance-matrix reduction** — [`gram_reduce`](../L4/gram_reduce.md) (**rough-in (test-coverage-bounded)**), the `w = 1/(IᵢIⱼ)` current-normalized specialization. The inductance matrix is the operator-weighted symmetric-Gram reduction `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` over the solution family `[Aᵢ]` — the current-normalized (`w i j = 1/(Iᵢ Iⱼ)`) member of the shared L4 reduction `gram_reduce K xs w = Gᵢⱼ = w(i,j)·(xⱼᵀ K xᵢ)` (the COMSOL magnetic-energy formulation: `Mᵢᵢ = 2Uₘ(Aᵢ)/Iᵢ²`, off-diagonals from the cross energy, normalized by the excitation currents `Iᵢ`; named magnetostatic specialization at `book/src/L4/gram_reduce.md:172-176`). It is the **same** reduction as the [electrostatic](./electrostatic.L4.md) capacitance Gram — differing **only** in the weight closure (`w = 1/(IᵢIⱼ)` current vs `w = 1` voltage; the operator `M_mag` and family `[Aᵢ]` are leaf-content absorbed into `K` and `xs`). `gram_reduce` is the **entry** (replace-and-propagate, CLAUDE.md §VOCABULARY-SHIFT redirect); the inductance reduction re-expresses THROUGH it as the current-normalized corner, NOT as a hand-rolled fold. The combinator's `map`-then-`reduce` body composes the rough-in L1 building blocks — the diagonal `Aᵢᵀ K Aᵢ` is the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) radicand, the off-diagonal `Aⱼᵀ K Aᵢ` is the [`bilinear-form`](../L1/bilinear-form.md), each scaled by the current normalization absorbed into `w` — folded over the upper-triangle family-pair grid with the symmetric mirror; `gram_reduce` is rough-in BECAUSE those folded constituents are. The inverse (`Minv = M⁻¹`, LAPACK) is the `gram_inverse` consumer downstream of the reduction, not part of it. This stage is the **output product** half of the composition root. L0: `PostprocessTerminals` (`magnetostaticsolver.cpp:108`, def `:110`; the energy-form `Mult`/`Dot` at `:129-138`, the inverse at `:151-152`).
```

```edit:book/src/feature/magnetostatic.L4.md
[old]: | inductance reduction (Aⱼᵀ K Aᵢ / Iᵢ Iⱼ) | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) / [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — no dedicated L4 reduction combinator yet | rough-in / rough-in (L1) | `magnetostaticsolver.cpp:108, 110-152` |
[new]: | inductance reduction (Aⱼᵀ K Aᵢ / Iᵢ Iⱼ) | [`gram_reduce`](../L4/gram_reduce.md) (`w = 1/(IᵢIⱼ)` current-normalized specialization) — folding L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (diagonal) / [`bilinear-form`](../L1/bilinear-form.md) (off-diagonal) | rough-in (test-coverage-bounded) | `magnetostaticsolver.cpp:108, 110-152` |
```

```edit:book/src/feature/magnetostatic.L4.md
[old]: stage (3) composes L1 bilinear-form primitives (rough-in diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md), each current-normalized; no dedicated L4 reduction combinator yet — a forward mine shared with the electrostatic capacitance reduction, not a blocker, since the reduction is a plain fold of evaluations).
[new]: stage (3) is the rough-in-track L4 [`gram_reduce`](../L4/gram_reduce.md) reduction (the `w = 1/(IᵢIⱼ)` current-normalized specialization — the same shared symmetric-Gram reduction as the electrostatic capacitance, the weight the only difference), which folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) building blocks over the family-pair grid — `gram_reduce` is rough-in (test-coverage-bounded) precisely because those folded constituents are; not a blocker, the reduction composes cleanly as a fold of evaluations.
```

## Discipline notes

- **Pure re-anchoring, structure preserved.** The three-stage composition (assemble-once / fixed-operator solve-family / output-product reduction) is untouched in both columns. Only stage (3)'s vocabulary firms from "no dedicated L4 reduction combinator yet — a forward mine" to "the rough-in-track L4 `gram_reduce` reduction (the `w` specialization)." No LHS/RHS shape change: `gram_reduce`'s signature `LinearOperator -> [Tensor] -> (Int->Int->Scalar) -> Matrix` is exactly the `map`-then-`reduce` over the family-pair grid the columns already described — the firmed combinator's signature MATCHES the rough-in sketch, so no LHS adjustment was needed.
- **Kept-down-link discipline (per dispatch instruction).** The rough-in L1 `matrix-weighted-norm` / `bilinear-form` rows are NOT deleted from the §"Constituent down-links" tables — they are reframed as "the building blocks the `gram_reduce` fold composes," with the table cell now leading with `gram_reduce` (the entry) and naming the two L1 rows as what it folds. This matches `gram_reduce.md` §Dependencies, which lists both L1 rows as "the diagonal consumer / the fold element." The status cell flips from `rough-in / rough-in (L1)` to `rough-in (test-coverage-bounded)` (gram_reduce's own status) — the combinator IS the down-link now, and it carries the rough-in maturity *because* its L1 constituents do.
- **Status token boundary with D5 honored.** I edited ONLY the reduction-reasoning prose inside the §Status paragraph (the "no dedicated L4 reduction combinator yet — a forward mine" clause). The head token `seed (exemplar)` (electrostatic) / `seed` (magnetostatic) is left byte-identical for D5's normalization pass. The `[old]` anchor for the §Status edit deliberately starts at "stage (3) composes…" (mid-paragraph), NOT at the leading backtick-token, to avoid touching D5's region.
- **Citation self-verification.** All re-anchored citations confirmed on disk this dispatch:
  - Link target `book/src/L4/gram_reduce.md` exists (`ls` confirmed, 17620 bytes) — the relative path `../L4/gram_reduce.md` from `book/src/feature/` resolves.
  - `gram_reduce.md:167-171` = the electrostatic specialization bullet (read on disk: line 167 `**Electrostatic capacitance** (...PostprocessTerminals)`, through 171 `Weight w = 1 (unit voltage excitation: /Vᵢ² ≡ ×1)`). Anchor token "Electrostatic capacitance" present in-range.
  - `gram_reduce.md:172-176` = the magnetostatic specialization bullet (read on disk: line 172 `**Magnetostatic inductance** (...)`, through 176 `Weight w = 1/(Iᵢ Iⱼ) (current-normalized)`). Anchor token "Magnetostatic inductance" present in-range.
  - The L0 driver-range citations in stage (3) prose (`electrostaticsolver.cpp:95/100/118-127/139-140`, `magnetostaticsolver.cpp:108/110/129-138/151-152`) are **carried verbatim from the existing column prose** (not newly introduced by this re-anchor) and match `gram_reduce.md` §Evidence's self-verified pinpoints — left unchanged.
- **This is a re-anchor, not authorship.** No new content decisions: the `w = 1` / `w = 1/(IᵢIⱼ)` specialization labels and the "weight is the only difference" framing are lifted directly from `gram_reduce.md` §Specialization / §Semantics, which the c073 combinator-miner authored. The columns now cite that pre-existing combinator vocabulary rather than restating the reduction bottom-up.

## Supporting evidence

- `book/src/L4/gram_reduce.md` (c073 D1, combinator-miner) — the landed entry; §Specialization (`:163-182`) names both columns as `w`-specializations, §Dependencies (`:184-204`) lists the two L1 rows as the fold's constituents, §Status (`:218-247`) records the double-gated rough-in reasoning the re-anchored §Status prose now mirrors.
- `scaffolding/open-questions.md:929` — OQ `gram-reduce-feature-chapter-reanchor-sequences-to-c074` (c073 D1), the exact deferral this dispatch discharges. **Recommend the integrator-per-report append a discharge note** (this dispatch's authority is append-only on the OQ ledger; the meta-phase unifies/closes). Suggested append text:
  > **Appended CYCLE-074 D1 (lifter gram_reduce feature re-anchor):** OQ `gram-reduce-feature-chapter-reanchor-sequences-to-c074` (c073 D1) **DISCHARGED**: `book/src/feature/electrostatic.L4.md` + `magnetostatic.L4.md` re-anchored — stage-(3) reduction prose, §"Constituent down-links" table, `composes:` frontmatter, and §Status reduction-reasoning all inverted from "no dedicated L4 reduction combinator yet — a forward mine" → "the rough-in-track L4 `gram_reduce` reduction" (electrostatic = `w = 1`, magnetostatic = `w = 1/(IᵢIⱼ)` specialization). The rough-in L1 `matrix-weighted-norm` / `bilinear-form` down-links kept (reframed as the fold's building blocks). The replace-and-propagate coupled half is now complete: combinator-as-entry (c073) + both feature columns linking DOWN to it (c074). The §Status `seed`/`seed (exemplar)` head token left to c074 D5's normalization pass (boundary honored).
- `electrostaticsolver.cpp:100-140` + `magnetostaticsolver.cpp:110-152` — the two skeleton-identical PostprocessTerminals Gram loops `gram_reduce` was mined from (cited verbatim in both columns' stage-(3) L0 references, unchanged here).

## Open questions / caveats

- **No abstractor reread needed.** The firmed `gram_reduce` signature matches the rough-in sketch the columns assumed (operator-weighted `map`-then-`reduce` over the family-pair grid, weight-parameterized) — there was no signature contradiction forcing a structural rewrite. This stayed a pure lift.
- **§Status table-cell status text was `rough-in / rough-in (L1)`** (the two L1 constituents' status) and is re-anchored to `rough-in (test-coverage-bounded)` (gram_reduce's own status, which the cell's combinator now carries). This is the correct propagation: the down-link is now the L4 combinator, and its maturity is what the cell should report. Flagging for critic visibility — this is a status-text change on a derived cell, intentional and consistent with `gram_reduce.md` firmness.
- **No index-table status cell to flip.** The feature columns are flat `book/src/feature/<name>.{L4,L1,L0}.md` with no per-feature index status table carrying these chapters' status (per the FEATURE-SURFACE SPINE flat-layout convention); the c073 D1 already added the `gram_reduce` dep-map row to `book/src/L4/index.md` in alpha position. No additional index-cell desync is created by this re-anchor (the columns' own §Status `seed` tokens are unchanged; D5 owns any seed-token normalization). The index-table-status-cell guard (CLAUDE.md / friction-ledger `index-table-status-cell-drifts-when-theme-file-promoted`) does not trigger: no `## Status` line is flipped by this dispatch.
- **Sequencing with D5 (the `seed (exemplar)` → `seed` token normalization).** Both my §Status edits anchor mid-paragraph ("stage (3) composes…") and never touch the leading token. If D5 runs AFTER me (per the dispatch note) and replaces the head token, the two edits are on disjoint byte regions of the same paragraph — no conflict. If the integrator applies them in the other order, still disjoint. Flagged only so the integrator confirms disjointness when staging both reports.
