---
agent: lifter
invoked_at: 2026-05-29T18:03:05Z
scope: cycle-026 mechanical hygiene re-anchor / cite-refresh — four bounded corrections (brace-boundary drift, workspace-category mislabel, givens source-cite staleness, dot_bilinear provenance-note refresh)
status: integrated
integrated_at: 2026-05-29T21:15:00Z
integration_commit: 8f14978
integration_notes: "cycle-027 finalize. 6 mechanical hygiene edits, ALL pure re-anchor/cite-refresh (no content/structure change): matrix-weighted-norm.md brace re-anchor :601-606→:602-606 at :58/:83; Category-4→Category-1 workspace relabel at linalg-operator-file.md :33/:73/:80 + matrix-weighted-norm.md:9 (four named sites now internally consistent at 'Category 1 — operator-composition workspace'; :22/:87 out of scope → NEW residual OQ linalg-operator-file-category-mislabel-residual-lines-22-87 for c028); givens.md:29 source-cite gmres.md→palace/linalg/iterative.cpp:634-640; bilinear-form.md:416 dot_bilinear provenance refresh (false slug-discrepancy premise dropped). retroactive-budget 0; clean build. The expected non-blocking citecheck operator.cpp:621-639 AMBIG is inside the Correction-2 preserve-verbatim payload (must match linalg-operator-file.md:33 bare-basename verbatim), NOT a citation defect."
inputs:
  - book/src/L1/matrix-weighted-norm.md
  - book/src/L0/linalg-operator-file.md
  - book/src/L0/mutable-workspace-pattern.md
  - book/src/concepts/givens.md
  - book/src/L1/bilinear-form.md
  - book/src/L2/incremental-least-squares.md
  - reference/palace/palace/linalg/operator.cpp
  - reference/palace/palace/linalg/iterative.cpp
---

# CYCLE: cycle-026 hygiene re-anchors (four bounded cite/name corrections)

## Summary
Four bounded mechanical-hygiene corrections carried forward from cycle-026 integrator-signals, all pure re-anchoring / cite-refresh — no content or structure changes. (1) Two `palace/linalg/operator.cpp:601-606` citations in `matrix-weighted-norm.md` (`Norml2` body) drift by including the opening brace at `:601`; the body the prose quotes is `:602-606` — corrected at sites `:58` and `:83` (site `:128` already cites the full spec `:599-607` and is left untouched per dispatch). (2) The `Bx`/`Ax` operator-composition scratch buffer is mislabelled "Category 4 — synthetic workspace" at `matrix-weighted-norm.md:9` and `linalg-operator-file.md:33`; per `L0/mutable-workspace-pattern.md` Category 4 is "assembled-matrix retention" and the apply-then-reduce intermediate is **Category 1 — operator-composition workspace** — corrected at both sites. (3) `concepts/givens.md:29` points the Givens-stream `ls_update_column` source at a `gmres.md` chapter (which does not exist on disk); the running-QR / Givens-rotation stream source is `palace/linalg/iterative.cpp:634-640` (established cycle-026 when `L2/incremental-least-squares` firmed) — re-anchored. (4) `bilinear-form.md:416` provenance note asserts "the L0 chapter uses the candidate slug `dot_bilinear`"; cycle-026's naming sweep repointed `linalg-operator-file.md` to `bilinear-form`, so that premise is now false (the only surviving `dot_bilinear` reference book-wide is this stale note) — refreshed to drop the false premise.

All on-disk-true ranges verified with `tools/citecheck/citecheck.py --show`/`--anchor` against `reference/palace/` (source-of-truth per dispatch).

## Proposed changes

### Correction 1 — `matrix-weighted-norm.md` Norml2-body brace-boundary drift (`:58`, `:83`)

citecheck confirmation (on-disk truth):
- `palace/linalg/operator.cpp:601-606` (current cite) — line `:601` is the opening brace `{`; the three-step body composition `B.Mult(x, Bx); dot = Dot(comm, Bx, x); ...; return std::sqrt(dot);` begins at `palace/linalg/operator.cpp:602`.
- `python3 tools/citecheck/citecheck.py palace/linalg/operator.cpp:602-606 --anchor 'B.Mult(x, Bx)'` → `[ok] anchor at line(s) [602] within range 602-606`. The body the prose quotes is `:602-606`.
- Site `:128` cites `:599-607` (full spec incl. signature + braces) — **not touched** per dispatch.

Both `[old]` strings quote the body; corrected to the body-only range `:602-606`.

```edit:book/src/L1/matrix-weighted-norm.md
[old]: Used directly by the L0 source (the implementation factors as `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)` — `palace/linalg/operator.cpp:601-606`).
[new]: Used directly by the L0 source (the implementation factors as `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)` — `palace/linalg/operator.cpp:602-606`).
```

```edit:book/src/L1/matrix-weighted-norm.md
[old]: The L0 implementation factors as `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)` (`palace/linalg/operator.cpp:601-606`). At L1 this is the unfolded composition `√(dot(apply_linop(B, x), x))`
[new]: The L0 implementation factors as `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)` (`palace/linalg/operator.cpp:602-606`). At L1 this is the unfolded composition `√(dot(apply_linop(B, x), x))`
```

### Correction 2 — Category-4 workspace mislabel → Category 1 (`matrix-weighted-norm.md:9`, `linalg-operator-file.md:33`)

`L0/mutable-workspace-pattern.md` confirmation (on-disk):
- `:82` — "## Category 4 — assembled-matrix retention" (`MfemWrapperSolver`'s retained `HypreParMatrix`, `solver.hpp:80`) — NOT a synthetic scratch workspace.
- `:29` — "## Category 1 — operator-composition workspaces": "a vector to hold the intermediate result" of chained applies; canonical shape `B.Mult(x, z); A.Mult(z, y)` (`:36-40`).

`Dot(comm, x, A, y)` internally allocates `ComplexVector Ax(A.Height())` then does `A.Mult(x, Ax); Dot(comm, Ax, y)` (`palace/linalg/operator.cpp:621-638`, verified `--show`) — an apply-then-reduce holding the `A·x` intermediate, i.e. the Category-1 operator-composition shape. Same for `Norml2`'s caller-owned `Bx` (`B.Mult(x, Bx); Dot(Bx, x)`, `palace/linalg/operator.cpp:602-606`). Both are **Category 1 — operator-composition workspaces**, not Category 4.

```edit:book/src/L1/matrix-weighted-norm.md
[old]: the related operator `Dot(comm, x, A, y)` uses Category 4 of [`L0/mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md) (synthetic workspace) — `matrix-weighted-norm`'s `Bx` is a *caller-owned* workspace, sliding it across the bilinear-form sibling boundary.
[new]: the related operator `Dot(comm, x, A, y)` uses Category 1 of [`L0/mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md) (operator-composition workspace, holding the `A·x` intermediate between the apply and the reduction) — `matrix-weighted-norm`'s `Bx` is a *caller-owned* workspace, sliding it across the bilinear-form sibling boundary.
```

```edit:book/src/L0/linalg-operator-file.md
[old]: implementations at `operator.cpp:621-639` use the [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) "allocates workspace internally" form (Category 4 — synthetic workspace).
[new]: implementations at `operator.cpp:621-639` use the [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) "allocates workspace internally" form (Category 1 — operator-composition workspace, holding the `A·x` intermediate between the apply and the reduction).
```

### Correction 2-residual (repairer) — Category-4 mislabel at `linalg-operator-file.md:73`, `:80`

Repairer-applied extension of Correction 2 (critic finding: the mislabel survives at two MORE sites in the same file, leaving it internally self-contradictory once `:33` is relabelled). The convention page's own **Evidence (representative)** section is authoritative on the categories of the three named workspaces:
- `mutable-workspace-pattern.md:128` — "`palace/linalg/operator.hpp:120` — `SumOperator::z` (**Category 1**: sum-of-operators workspace)."
- `mutable-workspace-pattern.md:129` — "`palace/linalg/operator.hpp:192` — `BaseProductOperator::z` (**Category 1**: operator-composition workspace)."
- `Dot`'s synthetic workspace — **Category 1** by Correction 2 (the `A.Mult(x, Ax); Dot(Ax, y)` apply-then-reduce shape is the Category-1 operator-composition form).

So all three named workspaces are **Category 1**; both `:73` ("Category 4") and `:80` ("Categories 2 and 4") are wrong on category and `:80` additionally wrong on count (names two categories for three same-category workspaces). Relabelled to a single "Category 1".

```edit:book/src/L0/linalg-operator-file.md
[old]: The workspace-internal-allocation pattern (`Dot`'s synthetic workspace) is Category 4 of [`mutable-workspace-pattern`](./mutable-workspace-pattern.md).
[new]: The workspace-internal-allocation pattern (`Dot`'s synthetic workspace) is Category 1 of [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) (operator-composition workspace, holding the `A·x` intermediate between the apply and the reduction).
```

```edit:book/src/L0/linalg-operator-file.md
[old]: - [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) — `SumOperator::z`, `BaseProductOperator::z`, and the free-function `Dot`'s synthetic workspace are Categories 2 and 4.
[new]: - [`mutable-workspace-pattern`](./mutable-workspace-pattern.md) — `SumOperator::z`, `BaseProductOperator::z`, and the free-function `Dot`'s synthetic workspace are all Category 1 (operator-composition workspaces).
```

### Correction 3 — `concepts/givens.md:29` source-cite staleness (`gmres.md` → `iterative.cpp`)

`book/src/L1/gmres.md` does **not** exist on disk (`ls` → No such file). The Givens-stream `ls_update_column` source is the GMRES loop at `palace/linalg/iterative.cpp:634-640` (verified `--show`): replay loop `:634-637`, `GeneratePlaneRotation` `:638`, `ApplyPlaneRotation` annihilate `:639` + RHS-pair `:640` — exactly the sequence this sentence narrates. This source was established cycle-026 when `L2/incremental-least-squares` firmed (it cites `iterative.cpp:634-640` for the same stream, e.g. `:158-159`, `:171-178`). The per-kernel source mappings `iterative.cpp:73-108` / `:227-241` already sit in this page's §Palace mapping (lines 33-34) and are unaffected.

```edit:book/src/concepts/givens.md
[old]: In GMRES (`gmres.md`), the inner step's `ls_update_column` is a sequence of `givens_apply2` calls (replaying stored rotations on a new column) followed by one `givens_generate` (producing the new rotation) and two `givens_apply2` calls (annihilating `h[j+1]` and updating the RHS pair).
[new]: In the GMRES inner step (`palace/linalg/iterative.cpp:634-640`), the `ls_update_column` is a sequence of `givens_apply2` calls (replaying stored rotations on a new column — `iterative.cpp:634-637`) followed by one `givens_generate` (producing the new rotation — `iterative.cpp:638`) and two `givens_apply2` calls (annihilating `h[j+1]` and updating the RHS pair — `iterative.cpp:639-640`).
```

### Correction 4 — `bilinear-form.md:416` `dot_bilinear` provenance-note refresh

The cycle-026 naming sweep repointed `L0/linalg-operator-file.md` to the `bilinear-form` slug (`grep` confirms `:73` now links `../L1/bilinear-form.md`; **no** `dot_bilinear` reference remains in `linalg-operator-file.md` or anywhere else in `book/src/` except this stale note). The note's premise — that the L0 chapter uses the candidate slug `dot_bilinear` and that a slug discrepancy persists — is now false. Refreshed to drop the false premise (cite/name refresh, not a semantic change).

```edit:book/src/L1/bilinear-form.md
[old]: matrix-weighted bilinear-form operator. The L0 chapter uses the candidate
  slug `dot_bilinear`; this entry uses the dispatch-supplied slug
  `bilinear-form` (matching the OQ candidate phrasing). The slug
  discrepancy is noted in *Open questions* below.
[new]: matrix-weighted bilinear-form operator. The L0 chapter and this entry both
  use the slug `bilinear-form` (the cycle-026 naming sweep repointed the
  former candidate slug `dot_bilinear` to `bilinear-form` throughout). No slug
  discrepancy remains.
```

## Discipline notes

- **Pure re-anchoring / cite-refresh** per role-spec — no operator signature, decomposition, semantics, or law changed. Corrections 1 and 3 are line-number / source-pointer re-anchors; Correction 2 is a category-name relabel against the L0 convention page's own definitions; Correction 4 is a provenance-note name/premise refresh following a sibling repoint.
- **Source-of-truth discipline followed**: every range verified with `tools/citecheck/citecheck.py --show`/`--anchor` against on-disk `reference/palace/` (per dispatch, codemap `read_range` is +1 behind on brace boundaries — this is exactly the `:601` opening-brace drift Correction 1 fixes). The mechanical `--anchor` check is the deterministic half of the producer self-verification (skill `verify-citation-range`, friction-ledger `producer-citation-drift-verify-not-self-invoked`).
- **Correction 1 — body vs. spec range judgment**: both `:58` and `:83` prose quote the *body* ("the implementation factors as `B.Mult...; return std::sqrt(dot)`"), so the body-only `:602-606` is correct (not the full-spec `:599-607`, which site `:128` correctly uses for the full overload incl. signature/braces). Per dispatch, `:128` is left untouched.
- **Correction 2 — bounded relabel against the L0 page's own taxonomy**: this is an L0-evidence-driven prose correction (`L0/mutable-workspace-pattern.md:82` says Category 4 = "assembled-matrix retention"; `:29` says Category 1 = "operator-composition workspaces" holding a chained-apply intermediate). It is bounded (a wrong category label, not a re-architecting of the workspace taxonomy or the operator decomposition) and evidenced (the `Dot`/`Norml2` bodies at `palace/linalg/operator.cpp:602-638` are apply-then-reduce, the Category-1 shape). Recorded here per the `lifter-scope-content-correction-boundary` discipline.
- **Correction 4 — premise refresh, not deletion of the Evidence bullet**: the bullet still documents `L0/linalg-operator-file.md` as the L0 anchor; only the now-false slug-discrepancy clause is rewritten. Kept the bullet so the L0-anchor provenance is preserved.

## Supporting evidence

- `reference/palace/palace/linalg/operator.cpp:599-640` — `Norml2` (real `:599-607`, complex `:609-619`) + `Dot(comm, x, A, y)` overloads (`:621-639`, internal `ComplexVector Ax(A.Height())` workspace). citecheck `--show` (this dispatch).
- `reference/palace/palace/linalg/iterative.cpp:634-640` — GMRES Givens-stream `ls_update_column` (replay `:634-637` / generate `:638` / two applies `:639-640`); per-kernel `GeneratePlaneRotation` `:73-108`, `ApplyPlaneRotation` `:227-241`. citecheck `--show`/`--anchor` (this dispatch).
- `book/src/L0/mutable-workspace-pattern.md:29,82` — Category 1 = operator-composition workspaces; Category 4 = assembled-matrix retention (the convention page the mislabel violates).
- `book/src/L2/incremental-least-squares.md` (firm, cycle-026) — establishes the running-QR / Givens-rotation stream source as `iterative.cpp:634-640` (e.g. `:158-159`, `:171-178`); the basis for Correction 3's re-anchor.
- `book/src/L0/linalg-operator-file.md:73` — post-cycle-026-sweep link to `../L1/bilinear-form.md` (no `dot_bilinear` slug remains); the basis for Correction 4's refresh.

## Open questions / caveats

- **Category-4 mislabel residual sites in `linalg-operator-file.md`** (UPDATED by repairer, cycle-027): the producer flagged ONE residual at `:73`; the critic found a SECOND at `:80` ("Categories 2 and 4"). **Both `:73` and `:80` are now fixed by the repairer's Correction-2-residual edits above** (relabelled to Category 1 per the convention page's Evidence section). Two FURTHER sites in the same file remain mislabelled and are OUT of this dispatch's named scope (`:33`, `:73`, `:80` only) — flagged here for a follow-up cleanup so the file is fully internally consistent:
  - `:22` — `SumOperator`'s `mutable Vector z` workspace labelled "Category 2 of [`mutable-workspace-pattern`]" (Evidence `mutable-workspace-pattern.md:128` says **Category 1**).
  - `:87` ("Referenced from") — "Category 2 (composition-class workspaces) cites `SumOperator::z` and `BaseProductOperator::z`" (both are **Category 1** per Evidence `:128-129`).
  These two were not in the dispatched/critic-named site list (`:33`/`:73`/`:80`), so the repairer did not silently widen scope into them; they are the same evidence-driven Category-1 relabel and a follow-up lifter/integrator pass should fold them in. (OQ widened: `linalg-operator-file-category-mislabel-residual` now names `:22` and `:87`.)
- No contradictions surfaced between the firmed-up vocabulary and the themes' assumptions — all four are within pure re-anchor scope (no abstractor reread needed).

### OQ disposition (close/dispose the four dispatched OQs)

- `matrix-weighted-norm-l1-norml2-body-brace-boundary-drift-601-606` — **RESOLVED** by Correction 1 (sites `:58`, `:83` re-anchored to `:602-606`; site `:128` was already correct at `:599-607`). Close on integration.
- `bilinear-form-workspace-category-4-mislabel` — **RESOLVED for the named sites** by Correction 2 + the repairer's Correction-2-residual (`matrix-weighted-norm.md:9`, `linalg-operator-file.md:33`, `:73`, `:80` all relabelled Category 1). RESIDUAL (out of named scope, two further sites): `linalg-operator-file.md:22` and `:87` still carry the same wrong label (see Open questions / caveats above). Keep open as the narrower residual OQ `linalg-operator-file-category-mislabel-residual` (now naming `:22`, `:87`) until those two are fixed.
- `givens-concept-page-source-cite-staleness-gmres-md-should-be-iterative-cpp` — **RESOLVED** by Correction 3 (`gmres.md` → `iterative.cpp:634-640`, with sub-range pinpoints). Close on integration.
- `bilinear-form-dot-bilinear-provenance-note-refresh` (and `bilinear-form-slug-name-coordination` residual) — **RESOLVED** by Correction 4 (false `dot_bilinear`-discrepancy premise dropped; the slug is now uniformly `bilinear-form` book-wide). Close on integration.
