---
agent: layer-intro-author
invoked_at: 2026-06-07T054924Z
scope: waveguide-mode drift / liveness hygiene (L0 stale rank + index/output-product stale seed cells)
status: pending
integrated_at: 2026-06-07T054924Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean. waveguide-mode .L0/index maturity drift cleanup; feature-column firm 12->13; feature_root: seed KEPT."
---

# CYCLE: waveguide-mode firm-flip drift cleanup (D9, cheap-openers 5b)

## Summary

The `waveguide-mode` output-product column was **promoted `rough-in` → `firm` at cycle-118 D5** (its own reduce verb [`waveguide_mode_reduce`](../../book/src/L4/waveguide_mode_reduce.md) firmed c118 D5 — OQ `waveguide-mode-reduce-needs-l4-verb-home` RESOLVED — so the OWN-COMPOSITION gate cleared, exactly as `sparameters` promoted at c083). The promotion landed on `waveguide-mode.L4` (`rank: firm` + `## Status` firm) and `waveguide-mode.L1` (`rank: firm` + `## Status` firm), but **three surfaces were never reconciled**:

1. **`feature/waveguide-mode.L0.md`** still reads `rank: rough-in` (frontmatter) and its `## Status` body still says `rough-in` with the now-RESOLVED `waveguide-mode-reduce-needs-l4-verb-home` OQ cited as the held-at gate. This is the exact `index-table-status-cell-drifts-when-theme-file-promoted` / promotion-time-reconciliation friction — a stale-on-disk surface left lagging the c118 D5 column flip.
2. **`feature/index.md`** still lists `waveguide-mode` as the lone `seed` column (the "`seed` (1 column)" Chapter-kind-status block + the §"After cycle-117 only `waveguide-mode` remains `seed`" prose + the output-product-cohort bullet) — stale; the column is firm since c118 D5.
3. **`feature/output-product.md`** still calls `waveguide_mode_reduce` **rough-in** and the column **`seed`** in two places — stale; the verb + column are firm since c118 D5.

This dispatch reconciles all three to the **firm reality** (the L4/L1 chapters' authoritative `## Status` lines, the firm `book/src/L4/waveguide_mode_reduce.md`). **`feature_root: seed` is KEPT everywhere** — it is the permanent GC-root marker, NOT a maturity rung.

**Honest-typing verification (faithful-or-finding):** every flipped cell was checked against the actual on-disk `## Status` of the referenced chapter, NOT the cycle record and NOT the index cells:
- `book/src/feature/waveguide-mode.L4.md` — frontmatter `rank: firm`; `## Status` (line 91-93): "`firm` … Promoted `rough-in` → `firm` (cycle-118 D5) … `waveguide_mode_reduce` is now **firm** (its dedicated L4 verb chapter landed c118 D5, OQ … RESOLVED)".
- `book/src/feature/waveguide-mode.L1.md` — frontmatter `rank: firm`; `## Status` (line 78-80): "`firm` … Promoted `rough-in` → `firm` (cycle-118 D5)".
- `book/src/L4/waveguide_mode_reduce.md` — frontmatter `firmness: firm` + `edges.rank: firm`; `## Status` (line 244-246): "`firm`. (firm-on-positive-structure / syntactic-identity escape)".
- The L0 citation `palace/drivers/boundarymodesolver.cpp:273-340` self-verified via `citecheck --anchor 'GetPropagationConstant'` → `[ok]` (anchor at 275, 299 within range).
- Firm sibling L0 feature surfaces (`sparameters.L0`, `eigenfrequency-qfactor.L0`, `energy-fields.L0`, `capacitance.L0`) all carry `rank: firm` + `feature_root: seed` — the L0 reconciliation matches the established firm-L0 convention.

**Well-foundedness:** the L0 surface's only `depends-on` edge is `cites-evidence` to source (`boundarymodesolver.cpp:273-340`); source ranges are rank-irrelevant, so `rank: firm` violates no `rank(u) ≤ rank(v)` constraint. The L4/L1 firm chapters rest on the firm `waveguide_mode_reduce` verb — well-founded at firm/firm.

## Proposed changes

### 1. `book/src/feature/waveguide-mode.L0.md` — flip stale `rank: rough-in` → `firm`; KEEP `feature_root: seed`

```edit:book/src/feature/waveguide-mode.L0.md
[old]: feature_root: seed
rank: rough-in
edges:
[new]: feature_root: seed
rank: firm
edges:
```

### 2. `book/src/feature/waveguide-mode.L0.md` — reconcile the `## Status` body to firm (OQ resolved, gate cleared)

```edit:book/src/feature/waveguide-mode.L0.md
[old]: `rough-in` — the L0 ground-truth surface for the waveguide-mode output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L0 surface of the readout reduction that the [`boundary-mode.L0`](./boundary-mode.L0.md) driver carries as a forward-ref. **Held at `rough-in` / `feature_root: seed` under the OWN-COMPOSITION rule:** the reduction's L4 verb home `waveguide_mode_reduce` has no firm chapter yet (OQ `waveguide-mode-reduce-needs-l4-verb-home`). Every stage is a cited range into `palace/drivers/boundarymodesolver.cpp`, self-verified on-disk this dispatch (the propagation-constant report loop `:273-277`, the mode-field readout loop `:292-334` with `GetEigenvector` `:297`, `ApplyVDBackTransform` `:300`, `ComputePoyntingPower` `:304`, the power-normalization `:305-307`, `MeasureAndPrintAll` `:314`, the `IsPropagating` branch + `Bz` formation `:316-333`, the return `:339-340`). The load-bearing structural fact at L0: the waveguide-mode product is a pair of **pure post-processing readout loops** over the converged eigenpair family — NOT a solve-iteration (the driver's only outer loops). The chapter's evidence IS the driver-source range + the per-stage site map (the adapted surface-or-evidence form for the feature-surface kind).
[new]: `firm` — the L0 ground-truth surface for the waveguide-mode output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L0 surface of the readout reduction that the [`boundary-mode.L0`](./boundary-mode.L0.md) driver carries as a forward-ref. **Promoted `rough-in` → `firm` (reconciled to the cycle-118 D5 column flip):** the column's own reduce verb [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) firmed c118 D5 (OQ `waveguide-mode-reduce-needs-l4-verb-home` RESOLVED), so the OWN-COMPOSITION promotion gate cleared and the [waveguide-mode.L4](./waveguide-mode.L4.md) + [waveguide-mode.L1](./waveguide-mode.L1.md) chapters promoted `rough-in` → `firm`; this L0 ground-truth surface is reconciled to that firm reality. **`feature_root: seed` is KEPT** (the permanent GC-root marker, NOT a maturity rung — the column is a reachability root). Every stage is a cited range into `palace/drivers/boundarymodesolver.cpp`, self-verified on-disk (the propagation-constant report loop `:273-277`, the mode-field readout loop `:292-334` with `GetEigenvector` `:297`, `ApplyVDBackTransform` `:300`, `ComputePoyntingPower` `:304`, the power-normalization `:305-307`, `MeasureAndPrintAll` `:314`, the `IsPropagating` branch + `Bz` formation `:316-333`, the return `:339-340`). The load-bearing structural fact at L0: the waveguide-mode product is a pair of **pure post-processing readout loops** over the converged eigenpair family — NOT a solve-iteration (the driver's only outer loops). The chapter's evidence IS the driver-source range + the per-stage site map (the adapted surface-or-evidence form for the feature-surface kind).
```

### 3. `book/src/feature/index.md` — reconcile the output-product-cohort bullet (`waveguide-mode` reduce verb + column firm)

```edit:book/src/feature/index.md
[old]: - **Per-mode mode-table (carrying mode-FIELDS)** — cycle-117: [`waveguide-mode`](./waveguide-mode.L4.md), over the [`boundary-mode`](./boundary-mode.L4.md) driver's converged eigenpair family. It composes the new `waveguide_mode_reduce` reduce verb (**rough-in** — no firm L4 verb chapter yet, OQ `waveguide-mode-reduce-needs-l4-verb-home`) — a per-mode map to `{kn, n_eff, (Et, En, Bz)}` (the propagation constant `kn` un-transformed from the eigenvalue, `n_eff = kn/ω`, the VD-back-transformed power-normalized mode fields `(Et, En)`, and `Bz = curl(Et)/(iω)` for propagating modes). It is the **propagation-mode** member of the output-product reduce-verb algebra: a reduce-to-mode-TABLE, but carrying mode-FIELDS (not only scalars), distinct from the scalar-only per-element tables and the rank-2 Gram / port-projection products. It homes the boundary-mode driver's stage-(3) readout that was previously a forward-ref ("no dedicated output-product column yet").
[new]: - **Per-mode mode-table (carrying mode-FIELDS)** — cycle-117: [`waveguide-mode`](./waveguide-mode.L4.md), over the [`boundary-mode`](./boundary-mode.L4.md) driver's converged eigenpair family. It composes the [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) reduce verb (**firm** c118 D5) — a per-mode map to `{kn, n_eff, (Et, En, Bz)}` (the propagation constant `kn` un-transformed from the eigenvalue, `n_eff = kn/ω`, the VD-back-transformed power-normalized mode fields `(Et, En)`, and `Bz = curl(Et)/(iω)` for propagating modes). It is the **propagation-mode** member of the output-product reduce-verb algebra: a reduce-to-mode-TABLE, but carrying mode-FIELDS (not only scalars), distinct from the scalar-only per-element tables and the rank-2 Gram / port-projection products. It homes the boundary-mode driver's stage-(3) readout that was previously a forward-ref ("no dedicated output-product column yet").
```

### 4. `book/src/feature/index.md` — reconcile the §"After cycle-117 only waveguide-mode remains seed" prose

```edit:book/src/feature/index.md
[old]: Cycle-085 ran the all-12-column re-evaluation under the OWN-COMPOSITION promotion rule, cycle-091 + cycle-095 closed the gram-Gram cascade, and cycle-117 cleared boundary-mode's own-readout gate (homing its readout in the new waveguide-mode output-product column — a SIBLING cross-link, not a blocker), promoting boundary-mode to `firm`. After cycle-117 only [`waveguide-mode`](./waveguide-mode.L4.md) remains `seed` (its own reduce verb `waveguide_mode_reduce` has no firm L4 verb home yet — an own-reduce-verb gate; promotes once that verb firms, exactly as `sparameters` promoted at c083). A column that cannot yet be cleanly composed — i.e. one of its directly-owned constituents is still rough-in or unhomed — stays `seed` as a *finding about the spine* (surfaced as an open question, the same low-priority test-load discipline the solvers carry on the vocabulary spine).
[new]: Cycle-085 ran the all-12-column re-evaluation under the OWN-COMPOSITION promotion rule, cycle-091 + cycle-095 closed the gram-Gram cascade, and cycle-117 cleared boundary-mode's own-readout gate (homing its readout in the new waveguide-mode output-product column — a SIBLING cross-link, not a blocker), promoting boundary-mode to `firm`. Cycle-118 D5 cleared the last column's gate: [`waveguide-mode`](./waveguide-mode.L4.md)'s own reduce verb [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) firmed (its dedicated L4 verb chapter landed c118 D5, OQ `waveguide-mode-reduce-needs-l4-verb-home` RESOLVED), promoting `waveguide-mode` `rough-in` → `firm` exactly as `sparameters` promoted when `sparameter_reduce` firmed at c083 — so **all 13 columns are now `firm`** (each retaining its permanent `feature_root: seed` GC-root marker). A column that cannot yet be cleanly composed — i.e. one of its directly-owned constituents is still rough-in or unhomed — stays at its constituent-gated rank as a *finding about the spine* (surfaced as an open question, the same low-priority test-load discipline the solvers carry on the vocabulary spine).
```

### 5. `book/src/feature/index.md` — reconcile the Chapter-kind-status firm/seed split (firm 12→13, seed 1→0)

```edit:book/src/feature/index.md
[old]: - **`firm` (12 columns)** — own composition + directly-owned constituents all firm; cross-linked sibling columns are references, not blockers:
[new]: - **`firm` (13 columns)** — own composition + directly-owned constituents all firm; cross-linked sibling columns are references, not blockers:
```

```edit:book/src/feature/index.md
[old]:   - spine-ROOT: [`lifecycle`](./lifecycle.L4.md) (own driver-agnostic composition — mesh-build + the firm `fold_solve` adaptive fold — firm; the per-driver dispatch is over sibling feature columns, references not blockers).
- **`seed` (1 column)** — held on a genuine **own-constituent gate** (a directly-owned constituent is rough-in or unhomed), NOT a sibling-column blocker:
  - [`waveguide-mode`](./waveguide-mode.L4.md) (cycle-117, output-product) — its own reduce verb `waveguide_mode_reduce` has no firm L4 verb home yet (own-reduce-verb gate; OQ `waveguide-mode-reduce-needs-l4-verb-home`). Promotes to `firm` once that verb firms, exactly as `sparameters` promoted at c083.
[new]:   - spine-ROOT: [`lifecycle`](./lifecycle.L4.md) (own driver-agnostic composition — mesh-build + the firm `fold_solve` adaptive fold — firm; the per-driver dispatch is over sibling feature columns, references not blockers).
  - output-product (added): [`waveguide-mode`](./waveguide-mode.L4.md) (own reduce verb [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) firm c118 D5 — promoted `rough-in` → `firm` cycle-118 D5 when its own-reduce-verb gate cleared, OQ `waveguide-mode-reduce-needs-l4-verb-home` RESOLVED; `boundary-mode` is a sibling cross-link, NOT a blocker).
- **`seed` (0 columns)** — no column is currently held on an own-constituent gate; every column has firmed its directly-owned constituents (each retaining its permanent `feature_root: seed` GC-root marker, which is the reachability root flag, NOT a maturity rung).
```

### 6. `book/src/feature/output-product.md` — reconcile the waveguide-mode cohort bullet (verb firm, column firm)

```edit:book/src/feature/output-product.md
[old]: - [`waveguide-mode`](./waveguide-mode.L4.md) — **per-mode mode-table (carrying mode-FIELDS)**, the `waveguide_mode_reduce` reduction (**rough-in** — no firm L4 verb chapter yet, OQ `waveguide-mode-reduce-needs-l4-verb-home`), over the [`boundary-mode`](./boundary-mode.L4.md) driver's converged eigenpair family — a per-mode map to `{kn, n_eff, (Et, En, Bz)}`. The propagation-mode member of the reduce-verb algebra: a reduce-to-mode-TABLE carrying mode-FIELDS (not only scalars), distinct from the scalar-only per-element tables and the rank-2 Gram / port-projection products. It homes the boundary-mode driver's stage-(3) readout that was previously a forward-ref. **The column is `seed`** (own reduce verb rough-in). Levels: [L4](./waveguide-mode.L4.md) · [L1](./waveguide-mode.L1.md) · [L0](./waveguide-mode.L0.md).
[new]: - [`waveguide-mode`](./waveguide-mode.L4.md) — **per-mode mode-table (carrying mode-FIELDS)**, the [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) reduction (**firm** c118 D5), over the [`boundary-mode`](./boundary-mode.L4.md) driver's converged eigenpair family — a per-mode map to `{kn, n_eff, (Et, En, Bz)}`. The propagation-mode member of the reduce-verb algebra: a reduce-to-mode-TABLE carrying mode-FIELDS (not only scalars), distinct from the scalar-only per-element tables and the rank-2 Gram / port-projection products. It homes the boundary-mode driver's stage-(3) readout that was previously a forward-ref. **The column is `firm`** (own reduce verb firm c118 D5; own composition all-firm — retaining its permanent `feature_root: seed` GC-root marker). Levels: [L4](./waveguide-mode.L4.md) · [L1](./waveguide-mode.L1.md) · [L0](./waveguide-mode.L0.md).
```

### 7. `book/src/feature/output-product.md` — reconcile the closing cohort summary (waveguide-mode no longer the sole seed)

```edit:book/src/feature/output-product.md
[old]: After the cycle-091 + cycle-095 energy-Gram cascade **the five reduce-verb-firm columns are `firm`** under the OWN-COMPOSITION rule (a column promotes off `seed` when its OWN reduce verb + directly-owned constituents are firm; cross-linked sibling driver columns are references, NOT blockers): [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) (own verb firm c082), [`sparameters`](./sparameters.L4.md) (own verb firm c083), [`energy-fields`](./energy-fields.L4.md) (own verb firm c091), and [`capacitance`](./capacitance.L4.md) + [`inductance`](./inductance.L4.md) (own verb [`gram_reduce`](../L4/gram_reduce.md) firm c095, once its off-diagonal `bilinear-form` folded primitive firmed). [`waveguide-mode`](./waveguide-mode.L4.md) is the sole **`seed`** output-product column — its own reduce verb `waveguide_mode_reduce` is rough-in (no firm L4 verb home yet), the promotion route being a firm `waveguide_mode_reduce` verb chapter.
[new]: After the cycle-091 + cycle-095 energy-Gram cascade and the cycle-118 D5 `waveguide_mode_reduce` firm flip, **all six output-product columns are `firm`** under the OWN-COMPOSITION rule (a column promotes off `seed`/`rough-in` when its OWN reduce verb + directly-owned constituents are firm; cross-linked sibling driver columns are references, NOT blockers): [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) (own verb firm c082), [`sparameters`](./sparameters.L4.md) (own verb firm c083), [`energy-fields`](./energy-fields.L4.md) (own verb firm c091), [`capacitance`](./capacitance.L4.md) + [`inductance`](./inductance.L4.md) (own verb [`gram_reduce`](../L4/gram_reduce.md) firm c095, once its off-diagonal `bilinear-form` folded primitive firmed), and [`waveguide-mode`](./waveguide-mode.L4.md) (own verb [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) firm c118 D5 — promoted `rough-in` → `firm` cycle-118 D5 when its own-reduce-verb gate cleared, OQ `waveguide-mode-reduce-needs-l4-verb-home` RESOLVED). Every column retains its permanent `feature_root: seed` GC-root marker (the reachability root flag, NOT a maturity rung).
```

## Supporting evidence

- **The drift is the c118 D5 promotion never reconciling three downstream surfaces.** Authoritative on-disk `## Status` lines (read directly, per the survey-firmness-from-disk discipline):
  - `book/src/feature/waveguide-mode.L4.md` frontmatter `rank: firm`, `## Status` (L91-93) firm, "Promoted `rough-in` → `firm` (cycle-118 D5)".
  - `book/src/feature/waveguide-mode.L1.md` frontmatter `rank: firm`, `## Status` (L78-80) firm, "Promoted `rough-in` → `firm` (cycle-118 D5)".
  - `book/src/L4/waveguide_mode_reduce.md` frontmatter `firmness: firm` + `edges.rank: firm`, `## Status` (L244-246) "`firm`. (firm-on-positive-structure / syntactic-identity escape)".
- **The lagging surfaces (this dispatch's targets):**
  - `book/src/feature/waveguide-mode.L0.md` frontmatter `rank: rough-in` (L6) + `## Status` (L48-50) `rough-in` with the now-RESOLVED OQ cited as the gate.
  - `book/src/feature/index.md` L67 (cohort bullet), L71 ("only waveguide-mode remains seed"), L77 ("firm (12 columns)"), L80-82 ("seed (1 column)" block).
  - `book/src/feature/output-product.md` L39 (cohort bullet), L41 (closing summary).
- **Firm-L0 convention match:** `sparameters.L0` / `eigenfrequency-qfactor.L0` / `energy-fields.L0` / `capacitance.L0` all carry `rank: firm` + `feature_root: seed`. The L0 reconciliation is consistent.
- **Citation self-verified:** `citecheck "palace/drivers/boundarymodesolver.cpp:273-340" --anchor 'GetPropagationConstant'` → `[ok]` (anchor at 275, 299 within range).
- **`feature_root: seed` KEPT on all three waveguide-mode levels** (per dispatch directive 3 + the GC-root-marker invariant) — only `rank:` and the prose `seed`/`rough-in` maturity tokens flip.

## Open questions / caveats

- **SHARED-FILE COUPLING (`feature/index.md`) — D1 also touches this file this cycle.** D1 (GMG row) edits the Feature × level matrix table to add the geometric-multigrid row; this dispatch (D9) edits ONLY the waveguide-mode/output-product **maturity cells/prose** (the cohort bullet L67, the seed-prose L71, the firm/seed split L77/L80-82). The two edit sets are anchor-distinct (D1 = matrix-table rows; D9 = prose paragraphs + the Chapter-kind-status block). **Integrator: sequence the two `feature/index.md` proposed-changes cleanly** — they do not overlap on any `[old]` anchor, but both land in the same file, so apply them one-report-at-a-time (the standard per-report serialization handles this). Flagging per the dispatch directive's shared-file-coupling note.
- **OQ `waveguide-mode-reduce-needs-l4-verb-home` is RESOLVED** (c118 D5 landed `book/src/L4/waveguide_mode_reduce.md` firm). If that OQ is still listed open in `scaffolding/open-questions.md`, it should be marked closed — flagging for the meta-phase intake→plan migration (out of this dispatch's write-scope; the meta-phase owns OQ unification).
- **No `SUMMARY.md` change needed** — the waveguide-mode chapters are already wired in (this is a maturity-token reconciliation, not a new landing).
- **`feature/index.md` "13 columns" total verified:** 1 spine-ROOT (lifecycle) + 6 driver-leaf (boundary-mode, driven, eigenmode, electrostatic, magnetostatic, transient) + 6 output-product (capacitance, eigenfrequency-qfactor, energy-fields, inductance, sparameters, waveguide-mode) = 13, now all firm.
