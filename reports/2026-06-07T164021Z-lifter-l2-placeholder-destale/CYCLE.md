---
agent: lifter
invoked_at: 2026-06-07T164021Z
scope: L2 prose de-stale — matrix-free-operator-apply L4 placeholder
status: pending
inputs:
  - book/src/L2/matrix-free-operator-apply.md
  - book/src/L4/mk_matrix_free_operator.md
  - book/src/feature/matrix-free-operator.L4.md
  - book/src/L4-L3/mk-matrix-free-operator-dissolution.md
integrated_at: 2026-06-07T170138Z
integration_commit: f93eaff
integration_notes: "cycle-128 D4 (batch-41 MIDDLE) applied clean by integrator-per-report (single prose-only edit: the L2 §'Speculative higher (L4) placeholder' -> '## Higher (L4) — firm' USE+LINK pointer to the 3 now-firm c127 chapters); DISCHARGES OQ matrix-free-operator-apply-l4-placeholder-now-stale (meta to CLOSE via unify authority); finalize aligned the new pointer's reproduced signature LinearOperator(...)->Op[...] to track D1's cap fix (lockstep consistency); NO frontmatter/status/edge change, graded-stack no-op, all totals HELD."
---

# CYCLE: Re-anchor matrix-free-operator-apply L4 placeholder

## Summary
The L2 combinator `matrix-free-operator-apply` (firm, c125) carries a `## Speculative higher (L4)
placeholder (rough-in, for a later harvester)` section (lines :209-222) whose entire premise is now
FALSE: it sketched a future `mk_matrix_free_operator` "NOT authored this cycle … placeholder for a
later harvester / L4-completeness capstone" and "Left as a §Open-questions placeholder, not a
chapter, this cycle." In c127 that L4 surface LANDED FULLY FIRM — `L4/mk_matrix_free_operator.md`
(`status: firm`, `rank: firm`), the `feature/matrix-free-operator.L4.md` backend-lowering column
(`rank: firm`), and the `L4-L3/mk-matrix-free-operator-dissolution.md` dissolution theme
(`rank: firm`). This is a pure-rewrite USE+LINK de-stale: replace the speculative-sketch section
with a settled `## Higher (L4) — firm` pointer to those three now-firm chapters. **No status / rank /
frontmatter-edge change** to the L2 combinator — it stays firm; this is prose-only. The accurate
`Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` contraction-form line and the firm L4 signature (which matches the
placeholder's sketch verbatim, confirmed against `L4/mk_matrix_free_operator.md:60`) are preserved.

## Proposed changes

```edit:book/src/L2/matrix-free-operator-apply.md
[old]: ## Speculative higher (L4) placeholder (rough-in, for a later harvester)

At L4 this combinator would surface as a **matrix-free linear-operator constructor** in the
backend-lowering feature surface — the calculus form whose semantics match the burn/GPU tensor-
contraction backend directly (`project_l4_is_backend_lowering_target`). Rough sketch (NOT authored
this cycle — placeholder for a later harvester / L4-completeness capstone):

    mk_matrix_free_operator
      :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])

with the apply lowering to the L4 tensor-contraction graph `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` over the
element-local axes. This is the L4 backend-lowering entry point for matrix-free assembly; it is the
remaining ASK-2 "A" depth (matrix-free assembly fused with `fe_assemble`'s term-fold at L4) flagged as
a c126 / batch-41 candidate. Left as a §Open-questions placeholder, not a chapter, this cycle.
[new]: ## Higher (L4) — firm

At L4 this combinator's action is the **apply** of a now-firm matrix-free linear-operator constructor
in the backend-lowering feature surface — the calculus form whose semantics match the burn/GPU tensor-
contraction backend directly (`project_l4_is_backend_lowering_target`). The L4 surface landed firm in
cycle-127:

- [`L4/mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md) (firm) — the **operator-constructor**
  whose action this L2 combinator IS. Signature
  `mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])`;
  its `apply` runs the element-local tensor-contraction chain `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` — i.e. this
  combinator — over the element-local axes.
- [`feature/matrix-free-operator.L4`](../feature/matrix-free-operator.L4.md) (firm) — the L4
  backend-lowering feature-surface column for matrix-free FE operators (the assemble-side
  composition-root).
- [`L4-L3/mk-matrix-free-operator-dissolution`](../L4-L3/mk-matrix-free-operator-dissolution.md) (firm)
  — the dissolution theme whose RHS composes this combinator (the flat-`Tensor[(N: ...)]` black-box
  apply → the five-stage element-local rank-tensor contraction sweep).
```

This is a prose-only USE+LINK re-anchor. No LHS/RHS shape change (the placeholder's sketched signature
matched the firm cap verbatim, so no signature adjustment was needed); no applicability-condition change
(the firm laws are the same syntactic-identity / structural facts the §Justification-kind already
records). No `## Speculative` section remains, so nothing is left to trim. The L2 combinator's
`## Status` and frontmatter (`status`/`rank`/`edges`) are untouched — it remains firm with its existing
typed `depends-on`/`reference` edges.

## Discipline notes
- **Pure rewrite, no authorship decision.** The replacement only points at chapters that already exist
  and are already firm on disk; no new content/structure is introduced. The contraction-form line and
  the L4 signature were preserved as-is (they were already accurate — the signature matches
  `L4/mk_matrix_free_operator.md:60` token-for-token).
- **No status/rank/edge change.** Per D2 scope, this is prose-only; the L2 combinator stays firm. I made
  no frontmatter edit, no `## Status` edit, no index-table-cell change (the L2 combinator's own maturity
  did not change, so the index-cell-drift guard does not fire — only the L4 surface's maturity changed,
  in c127, and that was the c127 finalize's index work).
- **High→low direction preserved.** The new section is an "upward to L4" navigational pointer (a
  `reference`-class see-also), narrated as "this combinator's action IS the L4 cap's apply" — it points
  the reader to the higher cap, it does NOT redefine the L2 combinator in L4 vocabulary. The lowering
  *direction* (L4 dissolution → L2 combinator on the RHS) lives in the dissolution theme, which the
  pointer links to; this L2 entry stays defined in its own L2 vocabulary.
- Cross-reference to the promoting work: the L4 surface was firmed by the c127 D1 matrix-free landing
  (`L4/mk_matrix_free_operator` roadmap_goal→firm + `feature/matrix-free-operator.{L4,L1}` firm +
  the dissolution theme firm), per the c128 planner CYCLE.md §Goals and the c127 integrator-signals OQ
  `matrix-free-operator-apply-l4-placeholder-now-stale`.

## Supporting evidence
- Stale section read on disk: `book/src/L2/matrix-free-operator-apply.md:209-222` (verbatim above).
- Firm targets confirmed on disk:
  - `book/src/L4/mk_matrix_free_operator.md` — `status: firm` (`:5`), `rank: firm` (`:6`); signature at
    `:60`; back-links to `../L2/matrix-free-operator-apply` at `:50`.
  - `book/src/feature/matrix-free-operator.L4.md` — `rank: firm` (`:6`); `## Status` `firm` (landed c127
    D1) at `:152-154`.
  - `book/src/L4-L3/mk-matrix-free-operator-dissolution.md` — `rank: firm` (`:18`); `## Status` `firm` on
    the structural rotation at `:437-440`.
- All three relative link targets resolve from `book/src/L2/` (filesystem-checked).

## Open questions / caveats
- None. The firm signature matched the placeholder sketch exactly, so this was a clean pure-rewrite — no
  contradiction surfaced that would warrant an abstractor reread.
- Out of D2 scope (noted, not acted on): the c128 D3 high-order-signature audit may flag this L2
  combinator's OWN signature line (`mk_matrix_free_operator`-adjacent apply signature) for the
  closure-grouping convention. That is a SIGNATURE-line concern, distinct from this L4-placeholder PROSE
  de-stale; per the dispatch note it is left to the c129 lifter sweep if D3 flags it. I touched no
  signature line.
