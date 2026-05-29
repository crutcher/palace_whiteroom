---
agent: lifter
invoked_at: 2026-05-29T16:47:44Z
scope: eigsolve-chain cross-reference cleanup — upgrade resolvable forward-references to live links
status: pending
inputs:
  - book/src/L1/eigsolve.md
  - book/src/L2/eigsolve.md
  - book/src/L3/eigsolve.md
  - book/src/L2/gram.md
  - book/src/concepts/eigsolve.md  (target — landed cycle-025 dispatch-4; firm)
  - book/src/L2-L1/eigsolve-spectral-transform-composition.md  (target — landed cycle-025 dispatch-3; firm)
  - book/src/L2-L1/gram-fold-specialization.md  (target — landed cycle-024/025; firm)
integrated_at: 2026-05-29T203000Z
integration_commit: 1de17ed
integration_notes: "Applied clean (cycle-026 dispatch-7, 9th/final). 8 plain-text→live-link cross-ref upgrades across L1/L2/L3 eigsolve.md + L2/gram.md (concepts/eigsolve.md, L2-L1/eigsolve-spectral-transform-composition.md, L2-L1/gram-fold-specialization.md — all on-disk + SUMMARY-wired) + 1 bounded rough-in→firm prose self-description correction. L4/eigsolve + L3>L2 eigsolve correctly left plain-text (genuinely absent). 3 OQs RESOLVED. Zero gate hits, link-clean."

# CYCLE: Re-anchor eigsolve-chain cross-references

## Summary

Pure cross-reference cleanup. Three forward-reference targets that did not exist when the
eigsolve chain + gram entries were authored have now all landed firm on-disk this batch:
`book/src/concepts/eigsolve.md` (cycle-025 dispatch-4), `book/src/L2-L1/eigsolve-spectral-transform-composition.md`
(cycle-025 dispatch-3), and `book/src/L2-L1/gram-fold-specialization.md` (cycle-024/025). The
chain entries `L1/eigsolve.md`, `L2/eigsolve.md`, `L3/eigsolve.md` each carry stale prose asserting
"a cross-cutting prose treatment does not yet exist at `concepts/eigsolve`"; `L2/eigsolve.md` carries
a "pending (a future dispatch)" plain-text reference to the L2>L1 spectral-transform theme; and
`L2/gram.md` carries three "(forthcoming)" notes for its L2>L1 lowering theme. This dispatch upgrades
each to a live link with adjusted tense. **No structure, semantics, signature, or L0 claim changes** —
only plain-text references firm to live links, per the pure-re-anchoring role discipline. All targets
verified on-disk (file exists + wired into `SUMMARY.md` lines 57/59/189) so the live links resolve
under `linkcheck2`.

Verification record (on-disk, this dispatch):
- `book/src/concepts/eigsolve.md` exists, `status: firm`-equivalent (firm chain navigational home;
  opening prose lines 1–14 confirm it is the cross-cutting concept page). Relative path from
  `book/src/L{1,2,3}/eigsolve.md` is `../concepts/eigsolve.md` (the convention used throughout these
  files, e.g. `../concepts/solve-monad.md`).
- `book/src/L2-L1/eigsolve-spectral-transform-composition.md` exists, `## Status` = `firm` (cycle-023
  firm-on-positive-structure, both L1 RHS leaves firm). Relative path from `book/src/L2/eigsolve.md`
  is `../L2-L1/eigsolve-spectral-transform-composition.md` (matches the `../L1-L0/` adjacent-edge
  convention used by `book/src/L1/axpby.md`).
- `book/src/L2-L1/gram-fold-specialization.md` exists, `## Status` = `firm` (cycle-022 L2 LHS firm).
  Its body (point (a) cell-dispatch over `nleps.cpp:525-531`, point (d) per-cell pinned reduction
  tree, §"L2>L1 lowering theme" framing) covers all three "(forthcoming)" mentions in `gram.md`
  (lines 38, 176, 242). So gram.md item 3 is **NOT already-satisfied** — the notes still say
  "(forthcoming)" on-disk and need the upgrade. Relative path from `book/src/L2/gram.md` is
  `../L2-L1/gram-fold-specialization.md`.

## Proposed changes

### 1a — `book/src/L1/eigsolve.md` §Context: concept-page "does not yet exist" → live link

```edit:book/src/L1/eigsolve.md
[old]: A cross-cutting prose treatment does **not** yet exist at `concepts/eigsolve` (unlike `ksp_solve`, which had a methodology-era concept page predating the firm operator chapter). The forward-target L4 monadic coordination layer the L1 form anchors will be analogous to [`concepts/solve-monad`](../concepts/solve-monad.md) but with sum-typed termination richer than `ksp_solve`'s soft-fail (the eigenvalue iteration can hit max-iter with `0 < converged < requested`, a partial-success case that has no analog in `ksp_solve`). The L1 entry here is the rough-in operator definition; a future concept page would carry the narrative.
[new]: The cross-cutting prose treatment lives at [`concepts/eigsolve`](../concepts/eigsolve.md) (the navigational/conceptual home for the chain, landed cycle-025). The forward-target L4 monadic coordination layer the L1 form anchors will be analogous to [`concepts/solve-monad`](../concepts/solve-monad.md) but with sum-typed termination richer than `ksp_solve`'s soft-fail (the eigenvalue iteration can hit max-iter with `0 < converged < requested`, a partial-success case that has no analog in `ksp_solve`). The L1 entry here is the firm operator definition; the concept page carries the navigational narrative without restating the algebraic laws.
```

### 1b — `book/src/L1/eigsolve.md` §Supporting evidence: "a future `concepts/eigsolve.md`" → live link

```edit:book/src/L1/eigsolve.md
[old]: - `book/src/concepts/solver-as-operator.md`, `book/src/concepts/solve-monad.md` — sister concepts inherited from `ksp_solve`; a future `concepts/eigsolve.md` would extend the pattern to the eigenvalue case with sum-typed termination.
[new]: - `book/src/concepts/solver-as-operator.md`, `book/src/concepts/solve-monad.md` — sister concepts inherited from `ksp_solve`; [`concepts/eigsolve`](../concepts/eigsolve.md) extends the pattern to the eigenvalue case with sum-typed termination.
```

### 1c — `book/src/L2/eigsolve.md` §Cross-cutting concepts: concept-page "does not yet exist" → live link

```edit:book/src/L2/eigsolve.md
[old]: A cross-cutting prose treatment does not yet exist at `concepts/eigsolve` (the firm L1 entry notes this gap); a future concept page would carry the narrative. The L4 `iterate_while` (per `book/src/design/l4_calculus.md`) is the natural composition target for the eigen-iteration loop *if and when* a Palace-authored loop existed — but since the loop is library-owned, the L4/L3 treatment is the `partial-obstruction` case, not a clean `iterate_while` fold.
[new]: The cross-cutting prose treatment lives at [`concepts/eigsolve`](../concepts/eigsolve.md) (the navigational/conceptual home for the chain, landed cycle-025); it does not restate the L2 algebra. The L4 `iterate_while` (per `book/src/design/l4_calculus.md`) is the natural composition target for the eigen-iteration loop *if and when* a Palace-authored loop existed — but since the loop is library-owned, the L4/L3 treatment is the `partial-obstruction` case, not a clean `iterate_while` fold.
```

### 2 — `book/src/L2/eigsolve.md` §"L2 eigsolve lowers from L1": pending L2>L1 theme → live link

```edit:book/src/L2/eigsolve.md
[old]: The L2>L1 theme narrating this opening forward (`L2-L1/eigsolve-spectral-transform-composition`) is pending (a future dispatch).
[new]: The L2>L1 theme narrating this opening forward is [`L2-L1/eigsolve-spectral-transform-composition`](../L2-L1/eigsolve-spectral-transform-composition.md) (firm, landed cycle-025).
```

### 1d — `book/src/L3/eigsolve.md` §"Lift relationships" prose: concept-page "does not yet exist" → live link

```edit:book/src/L3/eigsolve.md
[old]: A cross-cutting prose treatment does not yet exist at `concepts/eigsolve` (the firm L1/L2 entries note this gap); a future concept page would carry the narrative. This L3 entry is the iteration-rotation operator definition.
[new]: The cross-cutting prose treatment lives at [`concepts/eigsolve`](../concepts/eigsolve.md) (the navigational/conceptual home for the chain, landed cycle-025); it does not restate the iteration-rotation algebra. This L3 entry is the iteration-rotation operator definition.
```

### 3a — `book/src/L2/gram.md` opening: "forthcoming theme" → name + link `gram-fold-specialization`

```edit:book/src/L2/gram.md
[old]: This entry is defined in **L2 vocabulary** (the `inner_product` fold, the `dot` hook,
matrix/basis axes); how the L2 all-pairs fold lowers onto Palace's `nleps.cpp` double-`Dot`
loop (and which reduction tree each entry pins) is L2>L1 lowering work, narrated forward from
L2 to L1 in a forthcoming theme — not authored here.
[new]: This entry is defined in **L2 vocabulary** (the `inner_product` fold, the `dot` hook,
matrix/basis axes); how the L2 all-pairs fold lowers onto Palace's `nleps.cpp` double-`Dot`
loop (and which reduction tree each entry pins) is L2>L1 lowering work, narrated forward from
L2 to L1 in [`L2-L1/gram-fold-specialization`](../L2-L1/gram-fold-specialization.md) (firm) — not authored here.
```

### 3b — `book/src/L2/gram.md` §Algebraic laws (IEEE non-law): "(forthcoming)" → link

```edit:book/src/L2/gram.md
[old]: this is recorded, not erased: **`gram` is order-agnostic for value, but bit-identical
  reproduction of an L0 Gram requires matching each cell's pinned reduction tree.** Which tree a
  given lowered Gram pins is recorded by the L2>L1 lowering theme (forthcoming).
[new]: this is recorded, not erased: **`gram` is order-agnostic for value, but bit-identical
  reproduction of an L0 Gram requires matching each cell's pinned reduction tree.** Which tree a
  given lowered Gram pins is recorded by the L2>L1 lowering theme [`gram-fold-specialization`](../L2-L1/gram-fold-specialization.md) (firm).
```

### 3c — `book/src/L2/gram.md` §Supporting evidence: "(forthcoming; abstractor work)" → link

```edit:book/src/L2/gram.md
[old]: - **L2>L1 lowering theme** (forthcoming; abstractor work — not authored here): how the L2
  all-pairs fold lowers onto Palace's `nleps.cpp:524-531` double-`linalg::Dot` loop (the dispatch
  of each cell to the Hermitian/weighted `dot` leaf; the symmetry-exploitation transparent note;
  which reduction tree each cell pins — the load-bearing content of the IEEE non-law). Forward
  reference only.
[new]: - **L2>L1 lowering theme** [`gram-fold-specialization`](../L2-L1/gram-fold-specialization.md) (firm): how the L2
  all-pairs fold lowers onto Palace's `nleps.cpp:524-531` double-`linalg::Dot` loop (the dispatch
  of each cell to the Hermitian/weighted `dot` leaf; the symmetry-exploitation transparent note;
  which reduction tree each cell pins — the load-bearing content of the IEEE non-law).
```

## Discipline notes

- **Pure re-anchoring, no content decisions.** Every edit is a plain-text-reference → live-link
  upgrade plus the minimal tense adjustment that the now-existing target forces ("does not yet exist"
  → "lives at"; "a future concept page would carry" → "carries"; "pending (a future dispatch)" →
  "(firm, landed cycle-025)"; "(forthcoming)" → "(firm)"). No signature, decomposition, algebraic law,
  variant axis, or L0 citation is touched. This is exactly the lifter cross-ref-sweep deliverable.
- **Tense-only L1 wording fix (1a), bounded + evidenced.** The old L1:19 prose said "The L1 entry
  here is the **rough-in** operator definition" — but `book/src/L1/eigsolve.md` is `firm` (cycle-022
  firm flip; §Status / line 220 records "the cycle-022 firm flip"). I corrected "rough-in" → "firm"
  in the same sentence I was already re-anchoring, since leaving a stale "rough-in" self-description
  in a firm entry is a drifted claim. This is bounded (one adjective, supported by the entry's own
  `## Status`) and is recorded here per the `lifter-scope-content-correction-boundary` discipline —
  not a silent edit, not a re-architecture.
- **L4-surface mentions deliberately left untouched.** The L1/L2/L3 entries carry several mentions
  of the *L4* surface being unauthored (`L4/eigsolve.md` does not yet exist; L3 lines 19/34/78/164/166/172/191/214,
  L2 line 136 second half). Those are genuinely still true this batch — there is no firm `L4/eigsolve.md`
  — so they are correctly left as-is. Only the `concepts/eigsolve` gap and the two L2-L1 theme references
  were resolvable this dispatch. The L2-L1 frontmatter line 8 / body line 167 reference to the
  **L3>L2** theme (`L3-L2/eigsolve-*`) is also genuinely pending (no `L3-L2/eigsolve` theme on disk),
  left as plain-text correctly.
- **Cross-references to the harvester/abstractor reports that promoted the targets:** the concept
  page was promoted by the cycle-025 dispatch-4 `concepts/eigsolve` report (which flagged this exact
  live-link-upgrade follow-up); the L2>L1 spectral-transform theme by cycle-025 dispatch-3; the
  gram-fold-specialization theme by the cycle-024/025 gram-lowering dispatch.

## Supporting evidence

- `book/src/concepts/eigsolve.md:1-14` — confirms the concept page is the firm navigational/conceptual
  home for the chain and explicitly does not restate the L_n algebraic laws (matches the new prose).
- `book/src/L2-L1/eigsolve-spectral-transform-composition.md:362-365` — `## Status` = `firm`.
- `book/src/L2-L1/gram-fold-specialization.md:386-389` — `## Status` = `firm`; body points (a)/(d)
  (lines 11–17) cover the three gram.md "(forthcoming)" deferrals.
- `book/src/SUMMARY.md:57,59,189` — all three targets are wired into the book TOC, so the live links
  resolve under `linkcheck2`.
- Relative-path convention precedent: `book/src/L1/axpby.md:11,34` uses `../L1-L0/<theme>.md` for the
  analogous adjacent-edge link; `../concepts/solve-monad.md` is used throughout the eigsolve chain for
  concept links — both confirm `../concepts/eigsolve.md` and `../L2-L1/<theme>.md` are correct from the
  `book/src/L{1,2,3}/` directory depth.

## Open questions / caveats

- No contradiction surfaced between the now-firm target signatures and what the chain entries assumed —
  the upgrades are pure reference firming, so no abstractor reread is needed.
- **OQs to close (resolved by this dispatch's upgrades landing):**
  - `eigsolve-l2-entry-lowers-from-pending-forward-reference-upgrade` — CLOSE (scope item 2: the L2
    pending forward-reference to `L2-L1/eigsolve-spectral-transform-composition` is upgraded to a live link).
  - `gram-md-forward-ref-text-refresh-to-name-gram-fold-specialization` — CLOSE (scope item 3: all
    three gram.md "(forthcoming)" notes are refreshed to name + link `gram-fold-specialization`).
  - The cycle-025 `concepts/eigsolve` report's live-link-upgrade follow-up OQ (scope item 1) — CLOSE
    (the three chain entries' stale "does not yet exist at concepts/eigsolve" prose are upgraded to
    live links).
- **OQ to leave open / route:** the L4-surface gap (`L4/eigsolve.md` unauthored) and the L3>L2
  `eigsolve` theme gap remain genuinely open and were intentionally not touched. If an OQ tracks the
  L4 eigsolve surface, it stays open pending a future L4 dispatch (out of scope for this pure re-anchor).
