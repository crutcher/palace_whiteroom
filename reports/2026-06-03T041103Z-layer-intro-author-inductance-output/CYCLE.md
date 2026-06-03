---
agent: layer-intro-author
invoked_at: 2026-06-03T041103Z
integrated_at: 2026-06-03T044543Z
integration_commit: f5a405c
integration_notes: "cycle-074 D3 (FIRST per-report integrator; created STAGING.md). Applied clean — 3 new chapter files (feature/inductance.{L4,L1,L0}.md, status seed) composing L4 gram_reduce at w=1/(IiIj) over the magnetostatic driver column. Per cohort-ownership created only the 3 chapter files; index/SUMMARY rows deferred to D2 (cohort owner). DEAD-LINK WATCH (./capacitance.* not yet on disk) RESOLVED by D2 landing same-cycle. citecheck 12 ok/0 fail. retroactive 0. cargo make book exit 0, linkcheck2 clean."
scope: INDUCTANCE output-product feature column (feature/inductance.{L4,L1,L0}.md)
status: pending
---

# CYCLE: inductance output-product feature column

## Summary

Authors the **INDUCTANCE output-product feature column** — three new chapters
`book/src/feature/inductance.{L4,L1,L0}.md`, a **leaf feature column** (output-product
sub-kind) in the FEATURE-SURFACE SPINE's OUTPUT-PRODUCT cohort (CLAUDE.md §Extraction-goal,
output/postprocess products kind). Uniform `status: seed`.

The column is a **composition-root**: inputs = config (the surface-current sources + their
per-source excitation currents `Iᵢ`); output = the physical product (the Maxwell inductance
matrix `M` + inverse `Minv`); body = the composition of already-firm-track L4 vocabulary —
the [`gram_reduce`](../L4/gram_reduce.md) symmetric-Gram reduction in its **current-normalized
specialization** (`w = 1/(IᵢIⱼ)`) over the [`magnetostatic`](./magnetostatic.L4.md) driver
column's solution family `[Aᵢ]`. It COMPOSES the vocabulary; it does not restate per-op
algebra (that lives in the linked `gram_reduce` / bilinear-primitive chapters). The inverse
`Minv` is a downstream consumer kept out of the reduction (the `gram_reduce` consumer split).

Within-column ordering is high→low (L4 → L1 → L0), DELIBERATELY NOT alphabetized (the
directive-3 exception for the feature-surface kind).

Inductance is the **current-normalized sibling** of the capacitance unit-weight output
product (D2's column this cycle): ONE symmetric-Gram reduction across the two output
products, the weight (`w = 1/(IᵢIⱼ)` current vs `w ≡ 1` voltage) the only difference —
exactly as `gram_reduce` §Specialization documents.

**Chapter bodies are staged as sibling files in this report dir** (`inductance.L4.md`,
`inductance.L1.md`, `inductance.L0.md`) — the integrator copies them VERBATIM to
`book/src/feature/` (avoids nested-fence truncation; the proposed-changes blocks below are
file-creation directives, not inline-fenced bodies).

## Proposed changes

Three NEW files. The integrator copies each staged sibling file verbatim into `book/src/feature/`.

```create:book/src/feature/inductance.L4.md
[source]: reports/2026-06-03T041103Z-layer-intro-author-inductance-output/inductance.L4.md
[note]: copy verbatim — output-product leaf feature column, L4 composition root (gram_reduce current-normalized specialization over the magnetostatic driver family). status: seed.
```

```create:book/src/feature/inductance.L1.md
[source]: reports/2026-06-03T041103Z-layer-intro-author-inductance-output/inductance.L1.md
[note]: copy verbatim — L1 pure-function composition root (current-normalized bilinear-form fold over the solution family). status: seed.
```

```create:book/src/feature/inductance.L0.md
[source]: reports/2026-06-03T041103Z-layer-intro-author-inductance-output/inductance.L0.md
[note]: copy verbatim — L0 ground-truth surface (PostprocessTerminals reduction site map). status: seed.
```

### DEFERRED (ownership partition — do NOT apply here)

Per the dispatch ownership partition, this dispatch authors ONLY its 3 chapter files. The
following are **DEFERRED to D2** (the OUTPUT-PRODUCT cohort owner, authoring the capacitance
column + the consolidated `feature/index.md` matrix + the `# Feature surfaces` SUMMARY.md
block for BOTH output-product columns this cycle):

- The `feature/index.md` matrix row for the `inductance` column — **D2 owns** (single-index-owner
  guard: ≥2 feature columns land in one cycle → exactly one dispatch owns the shared index +
  SUMMARY block). NOT touched here.
- The `# Feature surfaces — entry points` SUMMARY.md rows for `inductance.{L4,L1,L0}.md`
  (high→low order, under the OUTPUT-PRODUCT grouping, nested under the lifecycle spine-ROOT) —
  **D2 owns**. NOT touched here.

The canonical slug `inductance` is used throughout so D2's index/SUMMARY references resolve.
D2's `capacitance` slug is cross-linked from these chapters (`./capacitance.{L4,L1,L0}.md`) and
will resolve once D2's column lands in the same cycle.

## Supporting evidence

**Composed vocabulary (down-links, all on disk):**

- [`gram_reduce`](../L4/gram_reduce.md) — `book/src/L4/gram_reduce.md`, `status: rough-in
  (test-coverage-bounded)` (read on-disk this dispatch). The symmetric-Gram reduction
  combinator; §Specialization explicitly names the magnetostatic inductance current-normalized
  specialization (`gram_reduce M_mag A (\i j -> 1/(I!!i * I!!j))`, lines 172-176) — this column
  is the feature-surface view of exactly that. The combinator's `w` weight axis is the
  load-bearing variant axis (line 13).
- [`magnetostatic.L4`](./magnetostatic.L4.md) / `.L1` / `.L0` — `status: seed` (read on-disk).
  The producing driver column; its stage (3) flags the inductance reduction as a forward mine
  and defers it (`magnetostatic.L4.md:40`, `:64`, Open questions) — this column lands that mine
  via `gram_reduce`. The driver column supplies the `(K, [Aᵢ])` pair this column consumes.
- [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in (test-coverage-bounded)) /
  [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — the diagonal + off-diagonal bilinear
  primitives `gram_reduce` folds (named in the L1 chapter's per-pair entry). Both rough-in →
  the column stays `seed`.

**L0 ground truth (all on-disk-verified this dispatch via palace-codemap `search_text` +
`read_range`; END-line close-brace discipline applied):**

- `magnetostaticsolver.cpp:105` — the `PostprocessTerminals(post_op,
  curlcurl_op.GetSurfaceCurrentOp(), A, I_inc)` call (search_text-confirmed).
- `magnetostaticsolver.cpp:110-113` — `MagnetostaticSolver::PostprocessTerminals(...)` def
  signature (read_range-confirmed; the 4-line signature `:110-113`, body opens `:114`).
- `magnetostaticsolver.cpp:115-121` — the COMSOL AC/DC Module manual p. 97 energy-formulation
  comment (read_range-confirmed).
- `magnetostaticsolver.cpp:122` — `mfem::DenseMatrix M(A.size()), Mm(A.size())` (search_text +
  read_range-confirmed; the inductance-matrix allocation, sized from the solution family).
- `magnetostaticsolver.cpp:129` — `post_op.GetDomainPostOp().M_mag->Mult(A_gf, H_gf)` (the
  `K·Aᵢ` energy-operator apply, search_text-confirmed).
- `magnetostaticsolver.cpp:131` — diagonal `linalg::Dot<Vector>(...) / (I_inc[i] * I_inc[i])`
  = `(Aᵢᵀ K Aᵢ)/Iᵢ²` (search_text-confirmed).
- `magnetostaticsolver.cpp:138` — off-diagonal `M(i, j) = linalg::Dot<Vector>(...) / (I_inc[i]
  * I_inc[j])` = `(Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` (search_text-confirmed). Energy-form computation span
  `:129-138`.
- `magnetostaticsolver.cpp:139` — `Mm(i, j) = -M(i, j)` (the mutual-inductance variant
  bookkeeping, search_text-confirmed).
- `magnetostaticsolver.cpp:143-149` — the symmetric-mirror "Copy lower triangle" loop (comment
  `:143`, `for (int j = 0; j < i; j++)` `:144`, **close brace `}` `:149` read_range-confirmed**
  per the END-line brace discipline).
- `magnetostaticsolver.cpp:151-152` — `mfem::DenseMatrix Minv(M); Minv.Invert()` (the LAPACK
  inverse consumer, search_text + read_range-confirmed).
- `magnetostaticsolver.cpp:155` — `if (!root)` root-write guard (search_text-confirmed).

**Codemap drift note:** `read_range` displayed a consistent line-offset on this file (a
requested start of 100 surfaced the line content of ~105); per the codemap-is-localization-only
discipline, all emitted `path:lo-hi` numbers are taken from `search_text` (authoritative
on-disk line numbers), not from `read_range` display positions, and the citecheck `--scan`
bounds pass ran clean on all three chapters (8/8 L4, 8/8 L1, 4/4 L0).

## Open questions / caveats

- **3rd+ witness for `gram_reduce` (eigenmode / driven post-processing).** `gram_reduce`
  §Specialization + the L4 index Open questions already flag eigenmode Q-factor and driven
  S-parameter post-processing as candidate 3rd+ witnesses (with the over-unification hazard
  that S-parameters are not symmetric-Gram in general). This inductance column does not bear on
  that — it is the established 2nd witness (current-normalized). No new OQ filed; the existing
  `gram_reduce` mine OQ covers it.
- **Promotion gate.** The column stays `seed` because `gram_reduce` is `rough-in
  (test-coverage-bounded)` (its folded L1 bilinear primitives are rough-in + no dedicated Gram
  test). Per the FEATURE-SURFACE directive, a feature column may promote past `seed` only once
  ALL composed constituents are firm; inductance's promotion is gated behind the
  `matrix-weighted-norm` / `bilinear-form` firm-up + a dedicated reduction test — the same gate
  the magnetostatic driver column and `gram_reduce` itself carry. No action needed; recorded for
  the plan.
- **`Mm` mutual-inductance variant.** The source also builds a `Mm` mutual-inductance matrix
  (`magnetostaticsolver.cpp:122, 139-140`) alongside `M`. The feature chapters treat `M` (the
  inductance matrix) as the primary physical product and note `Mm` only in the L0 site map (it
  is a sign-convention rearrangement of the same Gram entries, not a distinct reduction). If a
  downstream consumer needs `Mm` surfaced as a co-equal product, that is a refinement for the
  column's eventual promotion pass — not a blocker at `seed`. Lightweight; not filed as a
  standalone OQ.
