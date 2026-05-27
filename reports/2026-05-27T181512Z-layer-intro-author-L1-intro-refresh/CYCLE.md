---
agent: layer-intro-author
invoked_at: 2026-05-27T181512Z
scope: L1 intro refresh after ksp-solve-mutation-rotation L1>L0 theme landing (cycle-008)
status: integrated
integrated_at: 2026-05-27T18:35:15Z
integration_commit: PLACEHOLDER_SHA
integration_notes: cycle-008 pass 6 (wave-2). Polish refresh; motif 4 closing sentence pair appended + dep-map ksp_solve row Status-cell parenthetical (first cross-link in Status column) + Working Notes bullet. Closed cycle-007 OQ l1-intro-refresh-after-constructed-operator-gate.
---

# CYCLE: L1 intro refresh after constructed-operator-gate L1>L0 theme

## Summary

Polish-level refresh of `book/src/L1/index.md` to reflect cycle-008's
landing of the `ksp-solve-mutation-rotation` L1>L0 theme
(`book/src/L1-L0/ksp-solve-mutation-rotation.md`). The L1 vocabulary
cohort is unchanged (8 firm — no new L1 operator this cycle); what
changed is the **outbound** side of the constructed-operator gate. The
motif-4 paragraph in Semantics (overlay) registered cycle-007 with
`ksp_solve` now has its corresponding L1>L0 theme as a firm anchor, so
the paragraph closes the loop. The dep-map's `ksp_solve` row gets a
parenthetical note pointing readers to the now-firm L1>L0 theme. A new
Working Notes bullet records the theme landing and closes the
referenced OQ.

Closes OQ `l1-intro-refresh-after-constructed-operator-gate`
(cycle-007 surfaced). The OQ explicitly asked whether
`layer-intro-author` should "revisit the broader framing in a follow-up
dispatch" after motif 4 (Constructed-operator absorption) settled; this
report is that follow-up. The Context bullet 6 already calls out the
constructed-operator absorption as the layer's transition point to
upper-layer vocabulary (added cycle-007). With the L1>L0 theme now
firm, the framing is complete and the OQ's polish-level concern is
fully addressed.

## Proposed changes

```edit:book/src/L1/index.md
[old]: 4. **Constructed-operator absorption** (`ksp_solve`) — the L1 form takes a structured opaque `Solver[A]` argument whose per-method body (CG / GMRES / FGMRES), preconditioner, tolerances, and iteration cap are bound at construction; the L1 signature is variant-free. Result is structured (`SolveResult` carries `x` + four solve-statistics fields) rather than the L0 in-place destination + side-effect logger + mutating counters. The L2 `krylov-step` operator is where the per-method body unfolds.
[new]: 4. **Constructed-operator absorption** (`ksp_solve`) — the L1 form takes a structured opaque `Solver[A]` argument whose per-method body (CG / GMRES / FGMRES), preconditioner, tolerances, and iteration cap are bound at construction; the L1 signature is variant-free. Result is structured (`SolveResult` carries `x` + four solve-statistics fields) rather than the L0 in-place destination + side-effect logger + mutating counters. The L2 `krylov-step` operator is where the per-method body unfolds. The L1>L0 lowering — [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) (cycle-008) — is the first L1>L0 theme for a structured opaque primary argument. It decomposes into the firm sister-theme primitives ([`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md), [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md), [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md)) per-step plus four absorption rules (timer erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding) at the outer composition.
```

```edit:book/src/L1/index.md
[old]: | [`ksp_solve`](./ksp_solve.md) | `(K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) → SolveResult[N]` | `apply_linop` (direct); `dot`, `nrm2`, `axpy` (transitive via per-method body) | `firm` |
[new]: | [`ksp_solve`](./ksp_solve.md) | `(K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) → SolveResult[N]` | `apply_linop` (direct); `dot`, `nrm2`, `axpy` (transitive via per-method body) | `firm` (L1>L0: [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md), cycle-008) |
```

```edit:book/src/L1/index.md
[old]: - `ksp_solve` is the **first firm L1 operator whose primary argument is a structured opaque value** (`Solver[A]`) rather than a raw tensor or scalar. The construction of `Solver[A]` is the [`constructed-operator-factory`](../concepts/constructed-operator-factory.md) concept; the per-method axis collapse is [`variant-absorption`](../concepts/variant-absorption.md); the L0 anchor is [`L0/kspsolver-base-class`](../L0/kspsolver-base-class.md). The variant-axis collapse covers the **implemented** three (`CG`, `GMRES`, `FGMRES`) only; the three aborting enum cases (`MINRES`, `BICGSTAB`, `DEFAULT`) are out-of-scope per CLAUDE.md "Unimplemented Palace stub policy" and remain documented as L1>L0 obstruction themes.
[new]: - `ksp_solve` is the **first firm L1 operator whose primary argument is a structured opaque value** (`Solver[A]`) rather than a raw tensor or scalar. The construction of `Solver[A]` is the [`constructed-operator-factory`](../concepts/constructed-operator-factory.md) concept; the per-method axis collapse is [`variant-absorption`](../concepts/variant-absorption.md); the L0 anchor is [`L0/kspsolver-base-class`](../L0/kspsolver-base-class.md). The variant-axis collapse covers the **implemented** three (`CG`, `GMRES`, `FGMRES`) only; the three aborting enum cases (`MINRES`, `BICGSTAB`, `DEFAULT`) are out-of-scope per CLAUDE.md "Unimplemented Palace stub policy" and remain documented as L1>L0 obstruction themes.
- **Cycle-008**: the L1>L0 mutation-rotation theme for `ksp_solve` landed at [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) — the first L1>L0 theme whose LHS takes a structured opaque primary argument (`Solver[A]`). The theme decomposes into the firm sister themes per-step ([`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md), [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md), [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md)) plus four outer-composition absorption rules (timer erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding). The "Constructed-operator absorption" motif registered cycle-007 with the `ksp_solve` L1 firming now has the closing-the-loop L1>L0 anchor.
```

## Supporting evidence

L1 operators currently harvested at this layer (firm cohort unchanged from cycle-007 closing state — 8 firm):

- `axpy`, `dot`, `nrm2`, `axpby`, `scal`, `apply_linop`, `axpbypcz`, `ksp_solve`

L1>L0 themes currently landed at the adjacent down-layer (after cycle-008 wave-1):

- `axpby-mutation-rotation` (firm), `axpbypcz-mutation-rotation` (firm),
  `apply-linop-mutation-rotation` (firm),
  `ksp-solve-mutation-rotation` (firm, cycle-008 pass 4),
  `minres-iteration` (obstruction),
  `bicgstab-iteration` (obstruction).

Cross-references for the refresh:

- `book/src/L1-L0/ksp-solve-mutation-rotation.md` (cycle-008 wave-1 pass 4) — the L1>L0 theme this refresh registers in the L1 intro. Confirms slug, scope (four sub-patterns A/B/C/D over outer `BaseKspSolver::Mult` + inner CG / GMRES / FGMRES bodies), and sister-theme composition.
- `book/src/L1-L0/index.md` row 21 — confirms slug `ksp-solve-mutation-rotation` and `rough-in (firmed cycle-008)` status used in the L1>L0 Part's dep-map.
- `book/src/L1/ksp_solve.md` (cycle-007 firm) — motif-4 anchor; no edits to the operator entry in this refresh (the L1 entry's "Context" already references `kspsolver-base-class` / `ksp-factory-file` / `apply-linop-overload-set` L0 chapters and is unchanged by the L1>L0 theme firming).
- `scaffolding/open-questions.md:1278-1288` — OQ `l1-intro-refresh-after-constructed-operator-gate` (opened cycle-007 by harvester); this report closes it.

OQ closure rationale (for `l1-intro-refresh-after-constructed-operator-gate`):

The OQ asks "should `layer-intro-author` revisit the broader framing in
a follow-up dispatch (e.g. add a paragraph in `Context` calling out the
constructed-operator absorption as the layer's transition point to
upper-layer vocabulary)?" The Context bullet 6 (added by the cycle-007
harvester at the time of the OQ filing) already explicitly frames
`ksp_solve` as "construction-bound solver state → opaque type at the L1
surface" with the four-axis absorption (per-method body, preconditioner,
tolerances, iteration cap). The Semantics-overlay motif 4 already
names the absorption pattern explicitly. The remaining polish — closing
the loop on the L1>L0 theme — is what this cycle-008 refresh does. With
the three edits above the OQ's polish-level concern is fully addressed.

## Open questions / caveats

- The Working Notes bullet I propose adding does not introduce a new
  open question; the OQ being closed (`l1-intro-refresh-after-constructed-operator-gate`)
  was the polish-level revisit the cycle-007 harvester surfaced.
- The dep-map table layout chosen — annotating the `Status` cell with a
  parenthetical `(L1>L0: [<slug>](...), cycle-N)` — is the **first
  cross-link to live in the Status column** rather than in the
  Dependencies column (existing Dependencies-column cross-links to
  lowering themes appear at `book/src/L4/index.md:30` and
  `book/src/L2/index.md:23`, both on the `krylov-step` row). The
  novelty here is the column choice, not the act of cross-linking from
  an L_n dep-map row into an adjacent-layer theme. The L1>L0 Part's
  own dep-map already cites the L1 anchor in the `L1 anchor` column,
  so the cross-link is bidirectional after this refresh lands. If
  multiple L1>L0 themes per L1 operator emerge in later cycles
  (currently 1:1 across the firm cohort), the parenthetical-in-Status
  form will need to either repeat the slug list or split into a
  separate column. Defer to the second L1>L0 theme on the same L1
  operator before structural change. Not a blocker for this refresh;
  flagged for future `layer-intro-author` dispatches on L2 / L3 / L4
  intros where multi-theme-per-operator may be more common.
- The Edit-2 Status cell embeds a markdown link with parentheses
  inside a narrow table column (`firm` (L1>L0:
  [slug-link](...), cycle-008)`). This is valid markdown but is
  visually dense and integrator-finalize's `cargo make book` render
  should be eyeballed for column-width / line-wrap behavior. If the
  cell breaks awkwardly in mdBook output, a column split (separate
  `Lowering` column) is the structural fix; until then the
  parenthetical-in-Status form is the agreed-on shape pending the
  second L1>L0 theme per operator (see prior caveat).
- No L1 operator was added or retired in cycle-008. Vocabulary cohort
  count stays at 8 firm. The "Rough-in (obstruction)" sub-section
  remains unchanged — the six speculative operators from `minres-iteration`
  and `bicgstab-iteration` are still gated on Palace gaining an
  implementation or on scope expansion to vendored MFEM
  (`bicgstab-mfem-reanchor-policy` OQ).
- The Vocabulary cohort sub-section is intentionally not edited. Both
  the firm cohort listing and the rough-in / queued sub-sections
  describe the L1 *operator vocabulary*; lowering-theme landings do
  not change the operator count or the cohort split. The Working
  Notes addition is the right place for cycle-008's update because
  the cycle-008 change is at the **edge** (L1 ↔ L1>L0), not at the
  L1-internal vocabulary.
