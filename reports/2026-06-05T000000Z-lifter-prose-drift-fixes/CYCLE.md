---
agent: lifter
invoked_at: 2026-06-05T00:00:00Z
scope: cycle-104 D4 — 2 prose-drift fixes (pure citation/slug hygiene, no claim change)
status: pending
inputs:
  - book/src/L1/index.md
  - book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
  - book/src/concepts/incremental-least-squares.md
  - book/src/concepts/givens.md
integrated_at: 2026-06-05T093000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-104 D4, applied clean (staging row 2/4). 2 prose-drift fixes: de-staled the eliminate_rhs cohort bullet in L1/index.md (re-anchored to the live firm theme fe-operator-assemble-mutation-rotation), slug-fixed incremental-least-squares (givens-rotation -> live givens). Resolves 2 pre-existing c103 LOW OQs (eliminate-rhs-l1-index-bullet-stale-forthcoming-prose + incremental-least-squares-prose-names-nonexistent-givens-rotation-slug). No claim/status change; build EXIT 0."
---

# CYCLE: cycle-104 D4 prose-drift fixes

## Summary
Two pure-hygiene re-anchors of stale prose, no structural or claim change. (1) The `eliminate_rhs` bullet in `book/src/L1/index.md` still says its L1>L0 lowering `eliminate-rhs-mutation-rotation` is "forthcoming (plain text — theme not yet authored)"; that leg was FOLDED into the firm `L1-L0/fe-operator-assemble-mutation-rotation.md` at c103 D6 (verified: the theme is `## Status` firm, its frontmatter `lowers:` line names `L1/eliminate_rhs (firm c055)`, and it carries a dedicated §"The `eliminate_rhs` leg (folded here)" home, line 247). The bullet is re-anchored to point at that firm covering theme and the "(forthcoming)" tail is dropped. (2) The `incremental-least-squares` concept page's §Dependencies names a slug `givens-rotation` that does not exist (predates the c103 givens/givens_apply/givens_generate split); it is repointed to the existing `concepts/givens` (verified on disk; the page documents exactly "the scalar kernel pair: generate + apply" the sentence describes, and the c103 typed `reference` edge already points L2/incremental-least-squares at `concepts/givens`). Both fixes are vocabulary/reference firm-up only; structure and claims are unchanged.

## Proposed changes

```edit:book/src/L1/index.md
[old]: - **`eliminate_rhs` is now FIRM** (cycle-055) — see [`eliminate_rhs`](./eliminate_rhs.md). Lift inhomogeneous Dirichlet data into the RHS as the separable post-composition `b' = b − K·x_bc` (essential rows pinned per diagonal policy); clean-gate PROMOTE (the body is `apply_linop`(`A->Mult`, `palace/linalg/rap.cpp:69`) + `axpy`(`b.Add(-1.0,·)`, `:73`) + the `set_subvector` essential-dof pin (`:64,76,80`) — entirely firm-spine vocabulary, no spine gap). **Separable post-composition**, NOT part of the `fe_assemble` fold — it consumes the already-assembled `K` (witness `laplaceoperator.cpp:252`). Laws: interior-block linearity in `b` and in `x_bc`, homogeneous-BC interior identity, separable-post-composition-with-`fe_assemble`; non-laws: not linear-in-`b`-as-a-whole (the pin overwrites), not idempotent. L1>L0 lowering `eliminate-rhs-mutation-rotation` forthcoming (plain text — theme not yet authored).
[new]: - **`eliminate_rhs` is now FIRM** (cycle-055) — see [`eliminate_rhs`](./eliminate_rhs.md). Lift inhomogeneous Dirichlet data into the RHS as the separable post-composition `b' = b − K·x_bc` (essential rows pinned per diagonal policy); clean-gate PROMOTE (the body is `apply_linop`(`A->Mult`, `palace/linalg/rap.cpp:69`) + `axpy`(`b.Add(-1.0,·)`, `:73`) + the `set_subvector` essential-dof pin (`:64,76,80`) — entirely firm-spine vocabulary, no spine gap). **Separable post-composition**, NOT part of the `fe_assemble` fold — it consumes the already-assembled `K` (witness `laplaceoperator.cpp:252`). Laws: interior-block linearity in `b` and in `x_bc`, homogeneous-BC interior identity, separable-post-composition-with-`fe_assemble`; non-laws: not linear-in-`b`-as-a-whole (the pin overwrites), not idempotent. The L1>L0 lowering for this leg is **folded into** the firm [`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) (cycle-103 D6 FOLD verdict — see its §"The `eliminate_rhs` leg (folded here)"); there is no separate `eliminate-rhs-mutation-rotation` theme.
```

```edit:book/src/concepts/incremental-least-squares.md
[old]: - L2 realisation depends on `givens-rotation` (the scalar kernel pair: generate + apply).
[new]: - L2 realisation depends on [`givens`](./givens.md) (the scalar kernel pair: generate + apply).
```

## Discipline notes
- **Fix 1 (`L1/index.md:96`)** — bounded prose-correction of a drifted forward-reference. The "(forthcoming)" tail asserted an unauthored theme; the c103 D6 abstractor FOLD verdict (recorded in `fe-operator-assemble-mutation-rotation.md:51-60` §"Theme-split disposition") established the `eliminate_rhs` L1>L0 leg has its terminal home INSIDE the firm covering theme (§"The `eliminate_rhs` leg (folded here)", line 247), with NO separate `eliminate-rhs-mutation-rotation.md`. Re-anchored the dangling forward-ref to the terminal firm home. The covering theme's `## Status` (line 21) is `firm` and its frontmatter `lowers:` line (line 5) names `L1/eliminate_rhs (firm c055)` — verified the target is the TERMINAL firm home, not a relocated-dangle. All L0 citations in the bullet (`rap.cpp:69`/`:73`/`:64,76,80`, `laplaceoperator.cpp:252`) are carried VERBATIM — unchanged, no new pinpoint citation emitted.
- **Fix 2 (`incremental-least-squares.md:43`)** — pure slug-fix. `givens-rotation` does not resolve (confirmed `ls book/src/concepts/` has `givens.md`, `givens_apply.md`, `givens_generate.md`, no `givens-rotation`). Repointed to `concepts/givens` (`givens.md`), the rotation-kernel-pair page whose §Generate + §Apply sections are precisely "the scalar kernel pair: generate + apply" the dependency sentence names. This aligns the prose with the already-present c103 typed `reference` edge (`givens.md` frontmatter `reference: L2/incremental-least-squares`) and the L2 page's existing edge to `concepts/givens`. Converted the bare-backtick mention to a live markdown link (the slug now resolves, so a live link is correct and `linkcheck2`-checkable; the prompt's "repoint the prose reference to the EXISTING `concepts/givens`" is satisfied).

## Supporting evidence
- `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md:5` (frontmatter `lowers:` names `L1/eliminate_rhs (firm c055)`), `:21` (`## Status` firm), `:51-60` (c103 D6 theme-split FOLD disposition), `:247` (§"The `eliminate_rhs` leg (folded here)") — the terminal firm home for fix 1.
- `book/src/concepts/givens.md:1-20` (frontmatter `reference: L2/incremental-least-squares`; §Generate `givens_generate`, §Apply `givens_apply2`) — the existing repoint target for fix 2.
- `ls book/src/concepts/` — confirms no `givens-rotation.md`; `givens.md` is the canonical page.

## Open questions / caveats
- None. Both fixes are within the lifter mandate (vocabulary/reference firm-up; structure and claims unchanged). No signature shift, no decomposition change, no abstractor reread implicated.
- Build-safety: fix 1's new link target `../L1-L0/fe-operator-assemble-mutation-rotation.md` exists; fix 2's new link target `./givens.md` exists — both resolve, so neither introduces a `linkcheck2` break. Fix 2 converts a non-link backtick to a live link (net reduction in stale-slug surface); fix 1 was a non-link backtick mention, now a live link.
- The two stale-prose OQs (`eliminate-rhs-l1-index-bullet-stale-forthcoming-prose`, `incremental-least-squares-prose-names-nonexistent-givens-rotation-slug`) are resolved by these edits.
