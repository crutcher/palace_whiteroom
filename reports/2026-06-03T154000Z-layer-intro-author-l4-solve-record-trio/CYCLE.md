---
agent: layer-intro-author
invoked_at: 2026-06-03T154000Z
scope: concepts/ record-definition cohort #2(a) — input/state-side L4 solve records (op-params, sim-state, krylov)
status: pending
integrated_at: 2026-06-03T154500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row 1/5, FIRST per-report integrator). 3 record-definition concept pages (op-params/sim-state/krylov) + the one-time D1-exclusive `record` Kind-legend line in concepts/index.md + 3 alpha-position index/SUMMARY entries. record-definition data-shape pages (claim checks no-op); record-Kind awaits batch-24 meta ratification (OQ concepts-record-kind-needs-meta-ratification). Build clean."
---

# CYCLE: record-definition cohort #2(a) — `OpParams` / `SimState` / `Krylov`

## Summary

Authors THREE new cross-cutting **record-definition** concept pages (directive-2, the record-definition obligation — ≥2-consumer bar), the input/state-side L4 three-stratum solve records:

- `book/src/concepts/op-params.md` — `OpParams`, the construction-time readonly variant-selector + constructed-operator-surface closure (stratum 2 of state-stratification).
- `book/src/concepts/sim-state.md` — `SimState = {x, it, converged, final_res, initial_res}`, the run-time externally-visible solve state (stratum 1).
- `book/src/concepts/krylov.md` — `Krylov`, the slice-specific ephemeral per-restart workspace bundle (stratum 3; CG `{r,p,z?,α,β}`, GMRES/FGMRES `{V,Z?,H,s,cs,sn,β,j}`).

Each page is the **data shape** only — fielded `field : type — meaning` table + the construction-vs-run-time stratum of each field + the L0 source home (cited Palace `iterative.hpp` instance-field declarations). The behavior over the records (the `krylov-step` algebra) is NOT restated — it is down-linked to `L4/krylov-step.md`. The conceptual three-stratum typing in `concepts/state-stratification.md` is **cross-linked, not restated**.

This cohort discharges the three input/state-side OQs filed by the parallel c077 D2 dispatch (`record-OpParams-needs-definition-home`, `record-SimState-needs-definition-home`, `record-Krylov-needs-definition-home`). D2 (result-side: `step-outputs`/`prev-carry`/`solve-result`) + D3 (`config-record`) run in parallel; per the single-index-owner / distinct-anchor convention, this report inserts ONLY its own three slugs' rows + the one-time `record` Kind-legend line; D2/D3 insert their own rows.

**D1 owns the one-time `record` Kind-legend addition** to `concepts/index.md` (defined below; reused by D2/D3). The new `record` Kind value is **flagged for batch-24 meta-phase ratification** (OQ `concepts-record-kind-needs-meta-ratification`).

## Proposed changes

### New file: `book/src/concepts/op-params.md`

Full file content is co-located in this report directory at `op-params.md` — apply verbatim as `book/src/concepts/op-params.md`.

### New file: `book/src/concepts/sim-state.md`

Full file content is co-located in this report directory at `sim-state.md` — apply verbatim as `book/src/concepts/sim-state.md`.

### New file: `book/src/concepts/krylov.md`

Full file content is co-located in this report directory at `krylov.md` — apply verbatim as `book/src/concepts/krylov.md`.

### Edit: `book/src/concepts/index.md` — add `record` Kind-legend value (D1-owned, one-time)

```edit:book/src/concepts/index.md
[old]: - `auxiliary` — supporting concepts that don't fit the other categories.
[new]: - `auxiliary` — supporting concepts that don't fit the other categories.
- `record` — data-shape definition pages: the fields / types / meaning / construction-vs-run-time stratum / L0 backing home of a record named across ≥2 chapters (the record-definition obligation, directive-2). Counterpart to the behavior-side Kinds; defines the *data shape*, not the operator algebra over it.
```

### Edit: `book/src/concepts/index.md` — `krylov` row (alpha position: after `incremental-least-squares`, before `ksp_solve`)

```edit:book/src/concepts/index.md
[old]: | [incremental-least-squares](./incremental-least-squares.md) | algorithm |
| [ksp_solve](./ksp_solve.md) | layer-pattern |
[new]: | [incremental-least-squares](./incremental-least-squares.md) | algorithm |
| [krylov](./krylov.md) | record |
| [ksp_solve](./ksp_solve.md) | layer-pattern |
```

### Edit: `book/src/concepts/index.md` — `op-params` row (alpha position: after `nrm2`, before `orthogonalization`)

```edit:book/src/concepts/index.md
[old]: | [nrm2](./nrm2.md) | primitive |
| [orthogonalization](./orthogonalization.md) | algorithm |
[new]: | [nrm2](./nrm2.md) | primitive |
| [op-params](./op-params.md) | record |
| [orthogonalization](./orthogonalization.md) | algorithm |
```

### Edit: `book/src/concepts/index.md` — `sim-state` row (alpha position: after `set_subvector_zero`, before `solve-monad`)

```edit:book/src/concepts/index.md
[old]: | [set_subvector_zero](./set_subvector_zero.md) | primitive |
| [solve-monad](./solve-monad.md) | layer-pattern |
[new]: | [set_subvector_zero](./set_subvector_zero.md) | primitive |
| [sim-state](./sim-state.md) | record |
| [solve-monad](./solve-monad.md) | layer-pattern |
```

### Edit: `book/src/SUMMARY.md` — `krylov` entry (alpha position: after `incremental-least-squares`, before `ksp_solve`)

```edit:book/src/SUMMARY.md
[old]:   - [incremental-least-squares](./concepts/incremental-least-squares.md)
  - [ksp_solve](./concepts/ksp_solve.md)
[new]:   - [incremental-least-squares](./concepts/incremental-least-squares.md)
  - [krylov](./concepts/krylov.md)
  - [ksp_solve](./concepts/ksp_solve.md)
```

### Edit: `book/src/SUMMARY.md` — `op-params` entry (alpha position: after `nrm2`, before `orthogonalization`)

```edit:book/src/SUMMARY.md
[old]:   - [nrm2](./concepts/nrm2.md)
  - [orthogonalization](./concepts/orthogonalization.md)
[new]:   - [nrm2](./concepts/nrm2.md)
  - [op-params](./concepts/op-params.md)
  - [orthogonalization](./concepts/orthogonalization.md)
```

### Edit: `book/src/SUMMARY.md` — `sim-state` entry (alpha position: after `set_subvector_zero`, before `solve-monad`)

```edit:book/src/SUMMARY.md
[old]:   - [set_subvector_zero](./concepts/set_subvector_zero.md)
  - [solve-monad](./concepts/solve-monad.md)
[new]:   - [set_subvector_zero](./concepts/set_subvector_zero.md)
  - [sim-state](./concepts/sim-state.md)
  - [solve-monad](./concepts/solve-monad.md)
```

## Supporting evidence

**L0 backing home — all verified against on-disk `reference/palace/palace/linalg/iterative.hpp` via `citecheck --anchor` (codemap line-indexing drifted +1/+2 in the GMRES/FGMRES region; on-disk/citecheck is the source of truth and won every disagreement):**

- `IterativeSolver` class `:26-115` (on-disk `class` at 26, close-brace at 115 confirmed by direct Read).
  - `OpParams`-backing (non-`mutable` config): `rel_tol, abs_tol :42`, `max_it :45`, `A :49`, `B :50`.
  - `SimState`-backing (`mutable` statistics): `converged :53`, `initial_res, final_res :54`, `final_it :55`; accessors `GetConverged/GetInitialRes/GetFinalRes/GetNumIterations :97-108`.
- `CgSolver` class `:119-150` (close-brace on-disk at 150, NOT codemap's 141); CG workspace `mutable VecType r, z, p; :144`; `Mult :149`.
- `GmresSolver` class `:155-217` (close-brace on-disk at 217, NOT codemap's 219); `max_dim :180`, `gs_orthog :184`, `pc_side :187`; workspace `V :190`, `r :191`, `H :192`, `s, sn :193`, `cs :194`; `Initialize/Update :197-198`; `Mult :216`.
- `FgmresSolver` class `:222-275`; `Z :256` (on-disk, NOT codemap's 255).

Citecheck `--scan` pre-emit pass: op-params 10/10 ok, sim-state 8/8 ok, krylov 9/9 ok. Every load-bearing line citation additionally `--anchor`-verified; END close-braces of cited class ranges verified by direct on-disk Read (per the role-spec END-line guard — `--anchor` does not validate a range END).

**Consumers establishing the ≥2-consumer bar (each record):**
- `book/src/L4/krylov-step.md:37-50` (the per-record stratum prose + field schemas — the dispatch's named source material).
- `book/src/concepts/state-stratification.md:7-45` (conceptual three-stratum typing — cross-linked, not restated).
- `book/src/concepts/solve-monad.md` (the `Solve = StateT SimState` driver).
- `book/src/concepts/convergence-test.md` (reads `SimState.initial_res` / `Krylov.β`).

## Open questions / caveats

Appended to `scaffolding/open-questions.md` (cohort #2(a) block):
- `record-OpParams-needs-definition-home` / `record-SimState-needs-definition-home` / `record-Krylov-needs-definition-home` — all CLOSED-RESOLVED (the three pages authored).
- **Slug correction noted:** the dispatch prompt names the `Krylov` page slug `krylov`; the parallel c077 D2 OQ had proposed `krylov-bundle`. The **dispatch-prompt slug `krylov` is authoritative** and was used. Residual alias-OQ flagged only if a future chapter reaches for `krylov-bundle` by name.
- `concepts-record-kind-needs-meta-ratification` — the new `record` Kind value is **flagged for batch-24 meta-phase ratification** (in use now; no content blocked).

Caveats for the integrator:
- The three pages declare `## Status: firm` in-prose. Per the role-spec, the `record` Kind has no `firm` *apparatus* check (a record-definition page makes no operator-algebra claims, so the citation/surface/rotation/variant-axis critic checks largely no-op); firmness here means "every field is backed by a cited L0 declaration + stratum stated." If the critic prefers a lighter token for record pages, that is a meta-phase Kind-convention decision (folds into the `record`-Kind ratification OQ).
- D2/D3 run in parallel and insert their own index.md `## Index` rows + SUMMARY.md entries (distinct anchors). This report's `[old]` anchors for the index/SUMMARY edits are the *current* on-disk neighbor pairs; if D2/D3's integration lands first and shifts a neighbor, the integrator re-anchors against the post-D2/D3 alpha-neighbors (the `record` Kind-legend line is D1-exclusive and conflict-free).
