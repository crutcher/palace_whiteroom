---
agent: abstractor
invoked_at: 2026-06-05T071856Z
scope: L1>L0 theme disposition — eliminate-rhs-mutation-rotation (SPLIT vs FOLD)
status: pending
inputs:
  - reference/palace/palace/linalg/rap.cpp:56-82 (ParOperator::EliminateRHS body, codemap-confirmed)
  - reference/palace/palace/models/laplaceoperator.cpp:225-252 (GetExcitationVector witness)
  - book/src/L1-L0/fe-operator-assemble-mutation-rotation.md (firm; the fold-in candidate)
  - book/src/L1/eliminate_rhs.md (firm L1 LHS operator; lowers_to dangling)
  - OQ eliminate-rhs-mutation-rotation-l1-l0-half-forthcoming-vs-already-folded
    (== fe-bc-elimination-l1-l0-theme-split-vs-fold viewed from L4)
integrated_at: 2026-06-05T085500Z
integration_commit: e9e6556d1fe709b77124731573eafa7a638c7497
integration_notes: >
  Applied clean (cycle-103 D6, staging row 7 — the eliminate_rhs L1>L0 leg FOLD disposition).
  FOLD verdict: a new anchored §"The eliminate_rhs leg (folded here)" appended to the firm
  L1-L0/fe-operator-assemble-mutation-rotation.md (consolidating the rap.cpp:62-80 body walk as
  the linkable home) + the DANGLING lowers_to: edge in L1/eliminate_rhs.md repointed to that real
  firm theme (resolves an unsatisfiable rank constraint; firm rank 3 -> firm rank 3) + 6 de-stale
  (forthcoming) sites across L1/L4/L4-L3. Closes OQ
  eliminate-rhs-mutation-rotation-l1-l0-half-forthcoming-vs-already-folded (verdict already-folded).
  All-pass clean (critic set ready directly, no repair phase). The integrator CORRECTED the
  report's wrong L4-L3/index.md line numbers (report said 15,46; actual 35+66, located by grep).
  Build green; the lone citecheck AMBIG (index.md:15) is report-prose basename, not load-bearing.
  The 3 L4/L4-L3 de-stale touches are mechanical forward-ref corrections on already-integrated
  c101 D1 content (NOT retroactive report edits), collision-checked against D8 (a different file).
  step-5b rank_violations: 0. Opened OQ eliminate-rhs-l1-index-bullet-stale-forthcoming-prose
  (L1/index.md:96, out of scope, non-build-breaking).
---

# CYCLE: L1>L0 theme disposition — eliminate-rhs-mutation-rotation (SPLIT vs FOLD)

## Summary

**Route FOLD — confirmed; no dedicated sibling theme is warranted.** The `eliminate_rhs` L1>L0
lowering leg is already exhaustively and authoritatively homed inside the firm
`book/src/L1-L0/fe-operator-assemble-mutation-rotation.md`: that theme's L0-form **step 5**
(`book/src/L1-L0/fe-operator-assemble-mutation-rotation.md:122-128`) walks the entire
`ParOperator::EliminateRHS` body lowering against the exact `reference/palace/palace/linalg/rap.cpp:56-82`
cite, its L1-form block (`:78-84`) states the `eliminate_rhs(K, x_bc, b, policy)` signature and its
separable-post-composition role, and §"What lifts cleanly" (`:217-218`) gives the algebraic
decomposition (`apply_linop`(`A->Mult`) + `axpy`(`b.Add(-1.0,·)`) + essential-row `set_subvector`
pin). The theme's frontmatter `lowers:` line already names `L1/eliminate_rhs (firm c055)` and the
sibling operator-side leg `eliminate_essential_bc` already correctly points
`lowers_to: L1-L0/fe-operator-assemble-mutation-rotation`.

A dedicated `eliminate-rhs-mutation-rotation.md` sibling would be a **degenerate split** (anti-mirror
smell, CLAUDE.md §VOCABULARY-SHIFT REDIRECT): it is the **same** FE-BC-elimination rotation, on the
**same** L0 witness (`GetExcitationVector`/`GetStiffnessMatrix`), narrated alongside its operator-side
partner `eliminate_essential_bc` — splitting would mirror, not translate. The two BC-elimination legs
are jointly the BC-treatment post-composition half of one FE-operator-construction rotation; they
belong in one theme, which is exactly how the firm theme already structures them.

**The real defect this OQ surfaces is a reachability + staleness one, not a missing theme.** The slug
`eliminate-rhs-mutation-rotation` is referenced as **"(forthcoming)"** in five book locations
(`L1/eliminate_rhs.md` ×3, `L1/index.md` ×1 implicitly, `L4/eliminate_bc.md:312`,
`L4-L3/bc-elimination-post-composition-dissolution.md:78-80`, `L4-L3/index.md:15,46`), and
`L1/eliminate_rhs.md` frontmatter `lowers_to:` points at the non-existent file
`L1-L0/eliminate-rhs-mutation-rotation` (a dangling depends-on/lowers edge). Worse, the L1 entry's
§"Downward to L0" prose (`L1/eliminate_rhs.md:277-279`) asserts that
`fe-operator-assemble-mutation-rotation` "references but does not contain" the RHS lowering — which is
**factually wrong**: the covering theme's step-5 DOES contain it (`:122-128`). The FOLD disposition
re-points the dangling edge to the real covering theme and corrects the stale "forthcoming" /
"does-not-contain" claims.

## Disposition: FOLD (confirmed)

**Warrant-first reasoning.** The fold is the *honest* description: the RHS-side and operator-side
BC-elimination legs share L0 witness, L0 file (`rap.cpp`), upstream L1 partner, and the single
build-up-then-assemble narrative arc. The covering theme already treats them as exactly that. There
is no distinct rotation the fold "cannot cleanly carry" — the RHS leg's body is the *same kind* of
in-place-vector mutation → pure-function rotation, narrated as step 5 of the same protocol. A split
would force a reader to reconstruct the shared `GetExcitationVector` context twice and would create
two themes citing overlapping `rap.cpp` / `laplaceoperator.cpp` ranges. SPLIT is rejected.

**What the FOLD makes unambiguous (the proposed changes):**

1. **Add an explicit anchored sub-section** to the covering theme so the five forward-refs resolve to
   a named target inside it (rather than a plain-text "(forthcoming)" pointing at a never-to-exist
   file). The sub-section restates that the `eliminate_rhs` L1>L0 leg is **folded here** (with the
   `rap.cpp:56-82` body walk consolidated as its explicit home), and is the anchor the L1 entry +
   L4/L4-L3 references link to.
2. **Re-point `L1/eliminate_rhs.md` frontmatter `lowers_to:`** from the dangling
   `L1-L0/eliminate-rhs-mutation-rotation` to the real `L1-L0/fe-operator-assemble-mutation-rotation`
   (matching the sibling `eliminate_essential_bc` already-correct edge), and correct the stale
   §"Downward to L0" prose.
3. **Record the disposition** (no sibling theme; FOLD) in the covering theme's §Status so a future
   producer reading the artifact for precedent does not re-open the SPLIT question.

(The L4/`eliminate_bc.md` + L4-L3/`bc-elimination-post-composition-dissolution.md` + `L4-L3/index.md`
"(forthcoming)" mentions are sibling-scope content; I propose the minimal de-stale edits below and
flag them for integrator reconciliation — the load-bearing fix is the L1-entry edge + the covering
theme anchor.)

## Proposed changes

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[Replace the existing `## Status` block's opening (lines 21-24, the `firm. **Clean-gate call ...**`
paragraph head) by APPENDING a disposition note at the END of the `## Status` section. Insert the
following paragraph immediately BEFORE the `## L1 form (LHS)` heading (i.e. after line 49, the
"each leg's L0 form is read, not constructed." sentence):]

**Theme-split disposition (cycle-103 D6, abstractor): the `eliminate_rhs` L1>L0 leg FOLDS here — no
dedicated `eliminate-rhs-mutation-rotation` sibling theme.** The RHS-side BC-elimination rotation is
the same FE-BC-elimination rotation as its operator-side partner `eliminate_essential_bc`, on the
same L0 witness (`GetExcitationVector`/`GetStiffnessMatrix`) and the same L0 file
(`palace/linalg/rap.cpp`); it is narrated as **step 5** of the L0-form protocol below and is folded
here exactly as the operator-side leg is. A dedicated sibling theme would be a degenerate
identity-in-named-terms split (anti-mirror smell, CLAUDE.md §VOCABULARY-SHIFT REDIRECT). This closes
OQ `eliminate-rhs-mutation-rotation-l1-l0-half-forthcoming-vs-already-folded` (== the L4-side
`fe-bc-elimination-l1-l0-theme-split-vs-fold`): the answer is **already-folded**, not forthcoming.
The anchor for cross-references is §"The `eliminate_rhs` leg (folded here)" below.

[Then, append a new named sub-section at the END of the file (after the current last line, the
"`book/src/L0/fespace-file.md` is the L0 localization." line), so the five forward-references have an
explicit link target:]

## The `eliminate_rhs` leg (folded here)

This section is the explicit home of the `eliminate_rhs` L1>L0 lowering (the target of the
cross-references from [`eliminate_rhs`](../L1/eliminate_rhs.md), [`eliminate_bc`](../L4/eliminate_bc.md),
and [`bc-elimination-post-composition-dissolution`](../L4-L3/bc-elimination-post-composition-dissolution.md)).
There is **no** separate `eliminate-rhs-mutation-rotation.md` theme — the rotation lives here.

**L1 form (LHS).** [`eliminate_rhs`](../L1/eliminate_rhs.md) `(K, x_bc, b, policy)` — the
mutation-free inhomogeneous-Dirichlet lift `b' = b − K·x_bc` with essential rows pinned per diagonal
policy; a separable post-composition on the assembled `K` (signature authoritative in the L1 entry).

**L0 form (RHS).** `ParOperator::EliminateRHS` (`palace/linalg/rap.cpp:56-82`), reached from the
electrostatic witness `LaplaceOperator::GetExcitationVector` at `:252`
(`palace/models/laplaceoperator.cpp:252`). The in-place RHS-mutation protocol the L1 form lowers
into, line-by-line:

- **Gather the essential boundary values onto pooled true-dof scratch** — `tx = 0.0` then
  `linalg::SetSubVector(tx, dbc_tdof_list, x)` (`palace/linalg/rap.cpp:62-63`): scatter the Dirichlet
  data `x` (= `x_bc`) into a zeroed true-dof vector.
- **Prolong to the local (l-)vector** — `trial_fespace.GetProlongationMatrix()->Mult(tx, lx)`
  (`palace/linalg/rap.cpp:64`): the true→local prolongation `P·x_bc`.
- **Apply the unconstrained local operator** — `A->Mult(lx, ly)` (`palace/linalg/rap.cpp:69`): the
  local-matrix action `A·(P·x_bc)` (the single `apply_linop` of the L1 form, realized as the
  prolong/local-apply/restrict round-trip).
- **Restrict back to true dofs** — `RestrictionMatrixMult(ly, ty)` (`palace/linalg/rap.cpp:72`):
  `ty = Rᵀ·(A·P·x_bc)`, i.e. the assembled `K·x_bc` in true-dof space.
- **In-place RHS subtraction** — `b.Add(-1.0, ty)` (`palace/linalg/rap.cpp:73`): the in-place
  realization of `b' = b − K·x_bc` (the L1 `axpy`).
- **In-place essential-row pin per diagonal policy** — `DIAG_ONE` →
  `linalg::SetSubVector(b, dbc_tdof_list, x)` (`palace/linalg/rap.cpp:76`, pin essential rows to the
  boundary data); `DIAG_ZERO` → `linalg::SetSubVector(b, dbc_tdof_list, 0.0)`
  (`palace/linalg/rap.cpp:80`, pin to zero). This is the `policy`-selected essential-row overwrite of
  the L1 form (the non-law that makes `eliminate_rhs` not linear-in-`b`-as-a-whole).

**The mutation rotation.** The L0 form mutates the caller's `b` in place (`b.Add`, `SetSubVector`
both write `b`) using a pooled-scratch round-trip (`tx`/`lx`/`ly`/`ty` are reused per-solver buffers,
not fresh allocations — the transparent pooling trick). The L1 `eliminate_rhs` is the pure-function
rotation: it consumes `(K, x_bc, b, policy)` and returns a fresh `b'`, with the
prolong/apply/restrict round-trip absorbed into the single `K·x_bc` operator action and the in-place
`b.Add` + `SetSubVector` absorbed into the value-returning `b − K·x_bc` + pin. This is the same
in-place-vector → pure-function rotation as the operator-side leg, on the same witness — hence the
fold.

**Justification:** structural (shape-driven, the same as the parent theme) — read directly off the
positive `EliminateRHS` body, not constructed.
```

```edit:book/src/L1/eliminate_rhs.md
[Frontmatter: re-point the dangling lowers_to edge to the real covering theme.]
lowers_to:
  - L1-L0/fe-operator-assemble-mutation-rotation
```

```edit:book/src/L1/eliminate_rhs.md
[Body line 46: replace the "(forthcoming; see *Downward to L0*)" plain-text forward-ref with the
real folded home.]
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md)
L1>L0 lowering theme (the `eliminate_rhs` leg is folded there — see its §"The `eliminate_rhs` leg
(folded here)"; see *Downward to L0*).
```

```edit:book/src/L1/eliminate_rhs.md
[Body §"Downward to L0" (lines 269-279): replace the stale "(forthcoming) ... references but does not
contain" prose with the correct fold pointer.]
## Downward to L0

The lowering is **folded into**
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) — the
firm L1>L0 theme that lowers the whole FE-operator construction surface (the `fe_assemble` fold +
both separable BC-elimination legs). The `eliminate_rhs` leg is its own named sub-section there,
§"The `eliminate_rhs` leg (folded here)", which narrates how this L1 post-composition lowers into
Palace's in-place RHS-mutation protocol: gather essential values onto pooled scratch
(`rap.cpp:62-63`) → prolong (`:64`) → apply local matrix (`A->Mult`, `:69`) → restrict (`:72`) →
in-place `b.Add(-1.0, ·)` (`:73`) → in-place essential-row `SetSubVector` pin (`:76`/`:80`), with the
prolongation/restriction round-trip realizing the single `apply_linop`. It shares that theme with the
operator-side leg `eliminate_essential_bc` — both BC-treatment post-compositions lower in one theme
on the shared `GetExcitationVector`/`GetStiffnessMatrix` witness. There is **no** dedicated
`eliminate-rhs-mutation-rotation` sibling theme (disposition: FOLD, cycle-103 D6 — a degenerate split
would be an anti-mirror smell).
```

```edit:book/src/L4/eliminate_bc.md
[Line 312: de-stale the forthcoming reference to point at the folded home. Replace the bare slug
`eliminate-rhs-mutation-rotation` reference with the folded-here pointer.]
(`fe-operator-assemble-mutation-rotation` for the operator pin, and the `eliminate_rhs` leg folded
into that same theme — §"The `eliminate_rhs` leg (folded here)" — for the RHS lift; there is no
separate `eliminate-rhs-mutation-rotation` theme, disposition FOLD c103)
```

```edit:book/src/L4-L3/bc-elimination-post-composition-dissolution.md
[Lines 78-80: de-stale the forthcoming reference. Replace the "(forthcoming) ... no
book/src/L1-L0/eliminate-rhs-mutation-rotation.md exists yet" prose with the folded-home pointer.]
RHS-side L1→L0 half is folded into the firm
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) theme
(§"The `eliminate_rhs` leg (folded here)") — there is no separate `eliminate-rhs-mutation-rotation`
theme (disposition FOLD, cycle-103 D6); see `L1/eliminate_rhs.md` §"Downward to L0".
```

```edit:book/src/L4-L3/index.md
[Line 15 and line 46: in both the table row and the bullet for bc-elimination-post-composition-
dissolution, replace the plain-text "the RHS-side `eliminate-rhs-mutation-rotation` (forthcoming)"
with the folded pointer. Apply this replacement to both occurrences of the
"RHS-side `eliminate-rhs-mutation-rotation` (forthcoming)" phrase:]
the RHS-side `eliminate_rhs` leg folded into [`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) (disposition FOLD c103 — no separate theme)
```

## Speculative operators proposed

None. This is a FOLD disposition — no new theme, no new operators. The LHS operator
[`eliminate_rhs`](../L1/eliminate_rhs.md) is already firm (c055); the covering theme is already firm
(c057). The disposition re-homes an edge and adds an anchored sub-section to existing firm content.

## Edge typing (graded-stack)

No new node is created (FOLD, not SPLIT), so the HARD-gate-new rank gate has nothing to admit. The
edges touched are corrected, not added:

- `L1/eliminate_rhs.md` `lowers_to:` edge re-pointed from the **dangling** non-node
  `L1-L0/eliminate-rhs-mutation-rotation` to the existing **firm** node
  `L1-L0/fe-operator-assemble-mutation-rotation`. This RESOLVES a dangling lowers/depends-on edge
  (a reachability-GC and rank-well-foundedness fix): `eliminate_rhs` (firm, rank 3) now lowers to a
  firm (rank 3) theme — `rank(u) ≤ rank(v)` holds (3 ≤ 3); before the fix the edge pointed at a
  non-existent node (an unsatisfiable rank constraint + a linkcheck/reachability hole).
- The covering theme's new sub-section depends-on the same already-firm constituents the theme
  already cites (`L1/eliminate_rhs` firm, `palace/linalg/rap.cpp:56-82` L0 cite) — no new dependency
  is introduced.

## Supporting evidence

All citations self-verified at emit time (`citecheck --anchor`, on-disk re-read of the range END):

- `reference/palace/palace/linalg/rap.cpp:56-82` — `ParOperator::EliminateRHS` full body.
  `citecheck --anchor 'EliminateRHS'` → `[ok]` (anchor at lines 56, 58 within range). Range END (`}`)
  confirmed at line 82 by direct on-disk read (line 82 is the closing `}`; line 84 begins
  `ParallelAssemble`). The body lines cited in the new sub-section verified by `read_range`:
  `tx = 0.0` + `SetSubVector(tx,...,x)` at `:62-63`; `GetProlongationMatrix()->Mult(tx, lx)` at `:64`;
  `A->Mult(lx, ly)` at `:69`; `RestrictionMatrixMult(ly, ty)` at `:72`; `b.Add(-1.0, ty)` at `:73`;
  `DIAG_ONE` `SetSubVector(b,...,x)` at `:76`; `DIAG_ZERO` `SetSubVector(b,...,0.0)` at `:80`.
- `reference/palace/palace/linalg/rap.hpp:99` — `EliminateRHS` declaration. `citecheck --anchor` →
  `[ok]`.
- `reference/palace/palace/models/laplaceoperator.cpp:252` — `PtAP_K->EliminateRHS(X, RHS)` witness
  call site. `citecheck --anchor 'EliminateRHS'` → `[ok]`.
- `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md:78-84` (L1-form `eliminate_rhs` block),
  `:122-128` (L0-form step 5, the existing EliminateRHS body walk), `:217-218` (algebraic
  decomposition), frontmatter `:5` (`lowers:` names `L1/eliminate_rhs (firm c055)`), `:207`
  (`rap.cpp:56-82` Verified-against cite) — the firm covering theme; FOLD home confirmed.
- `book/src/L1/eliminate_rhs.md:6` (dangling `lowers_to`), `:46`, `:271-279` (stale "forthcoming" /
  "does not contain") — the defects the FOLD corrects.
- `book/src/L1/eliminate_essential_bc.md:5-6` — sibling operator-side leg already correctly points
  `lowers_to: L1-L0/fe-operator-assemble-mutation-rotation` (the precedent the re-point matches).
- `book/src/L4/eliminate_bc.md:312`, `book/src/L4-L3/bc-elimination-post-composition-dissolution.md:78-80`,
  `book/src/L4-L3/index.md:15,46` — the four other "(forthcoming)" references de-staled.

## Open questions / caveats

- **Sibling-scope edits flagged for integrator reconciliation.** The L4 (`eliminate_bc.md:312`) and
  L4-L3 (`bc-elimination-post-composition-dissolution.md:78-80`, `index.md:15,46`) de-stale edits
  touch content authored by the cycle-101 D1 dispatch (a different scope). They are mechanical
  forward-ref corrections (replace "(forthcoming)" with the folded-home pointer), not substantive
  re-authoring; I propose them because they are the same reachability defect this OQ closes (the
  dangling `eliminate-rhs-mutation-rotation` slug). If the integrator prefers to defer the L4/L4-L3
  edits to a lifter/sibling pass, the **load-bearing** subset is (1) the covering-theme sub-section +
  disposition note and (2) the `L1/eliminate_rhs.md` frontmatter edge re-point + §"Downward to L0"
  correction — those two close the OQ and fix the dangling edge.
- **The `eliminate-essential-bc-mutation-rotation` slug referenced in `L1/eliminate_rhs.md:277`** is
  itself a phantom (the operator-side leg is also folded into
  `fe-operator-assemble-mutation-rotation`, not a separate `eliminate-essential-bc-mutation-rotation`
  theme). My §"Downward to L0" replacement removes that phantom reference too. No separate operator-
  side theme exists or is warranted (same FOLD logic) — noting it so a future producer does not chase
  it.
- **OQ closure.** This resolves OQ `eliminate-rhs-mutation-rotation-l1-l0-half-forthcoming-vs-already-
  folded` with verdict **already-folded** (FOLD). Per the OQ ledger this is the same thread as
  `fe-bc-elimination-l1-l0-theme-split-vs-fold` viewed from L4 — both close together. The integrator-
  per-report should mark both closed in the OQ ledger.
