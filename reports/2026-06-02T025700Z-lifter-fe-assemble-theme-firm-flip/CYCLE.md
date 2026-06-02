---
agent: lifter
invoked_at: 2026-06-02T030406Z
scope: L1>L0 theme re-anchor + firm-flip — fe-operator-assemble-mutation-rotation
status: pending
integrated_at: 2026-06-02T050000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-057 (D2). fe-operator-assemble-mutation-rotation PROMOTED rough-in→FIRM (all 3 LHS ops now firm): 2 BC-elimination-leg re-anchors to firm eliminate_essential_bc/eliminate_rhs live links + 3 citation drift fixes (:225-253→:225-252 / :236→:238 / new :247) + a stale-back-ref fix + libCEED-boundary OQ re-anchor to the settled obstruction annotation. Index-cell anti-drift guard applied (theme ## Status + frontmatter + L1-L0/index.md row all flipped firm in one report). The FE-assembly sub-spine L1>L0 edge is now COMPLETE. L1>L0 firm themes +1. 2 OQs promoted. Build clean (firm-flip of existing registered theme, no new/removed pages)."
inputs:
  - book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
  - book/src/L1/fe_assemble.md
  - book/src/L1/eliminate_rhs.md
  - book/src/L1/eliminate_essential_bc.md
  - book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md
  - book/src/L1-L0/index.md
---

# CYCLE: Re-anchor + firm-flip fe-operator-assemble-mutation-rotation

## Summary

The `fe-operator-assemble-mutation-rotation` L1>L0 theme was authored cycle-053 as a
**thread-opener** when all three of its LHS operators were speculative. The D6/cycle-055 pass
already re-anchored its citations + LHS to the now-firm `fe_assemble`; this pass closes the loop.
All three LHS FE-assembly operators are now **firm L1**: `fe_assemble` (c054), `eliminate_rhs`
(c055), `eliminate_essential_bc` (c055), and the per-term leaf `A(·)` is documented as
`obstruction (opaque-library-ownership)` by `fe-assemble-libceed-boundary-obstruction.md` (c055).

**Clean-gate verdict: PROMOTE — clean.** (a) All 3 LHS operators firm ✓; (b) the build-then-assemble
rotation is fully cited at L0 (the integrator-fold `AddSubOperator` `:77`/`:97`/`Finalize` `:104`,
the two separable BC-elimination legs `rap.cpp:56-82` + `laplaceoperator.cpp:216-217`/`:252`) and
verifies clean against source ✓; (c) the libCEED leaf-kernel boundary is documented as an
opaque-library-ownership obstruction and — per that annotation's own §Status + the `ksp_solve`/
MINRES precedent — the firm fold quantifies over `A(·)` opaquely, so the opaque leaf does **not**
gate the theme's firmness ✓. The genuinely-new `weak_form_term` type stays a deferred rough-in
input the fold quantifies over opaquely (exactly as in the firm `fe_assemble` clean-gate), so it
does not gate the theme any more than it gated `fe_assemble`.

This pass: (1) flips `rough-in` → `firm` (frontmatter `status:`, `## Status` body, the
`L1-L0/index.md` dep-map row status cell — both updated per the cycle-056 D2 index-cell guard);
(2) re-anchors the two elimination legs from "rough-in placeholders" prose to live links at the now-firm
`eliminate_essential_bc` / `eliminate_rhs` operators; (3) replaces the `## Speculative L1 operators`
section (all promoted) with a thin residual note; (4) re-anchors the libCEED-boundary OQ to the
now-settled obstruction annotation; (5) bounded prose-corrections of three drifted citations in the
§L0-form step-5 + §Verified-against (`:236`→`:238`, `:253`→`:252`, `:225-253`→`:225-252`), matching
the verified citations the firm `eliminate_rhs` sibling carries.

## Proposed changes

### Change 1 — frontmatter status flip + lowers-list completion

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: ---
layer: L1-L0
theme: fe-operator-assemble-mutation-rotation
status: rough-in
lowers: L1/fe_assemble (firm — landed cycle-054)
l0_anchor: palace/fem/bilinearform.{hpp,cpp}, palace/fem/libceed/operator.cpp, palace/models/laplaceoperator.cpp, palace/linalg/rap.cpp
justification_kind: structural
---
[new]: ---
layer: L1-L0
theme: fe-operator-assemble-mutation-rotation
status: firm
lowers: L1/fe_assemble (firm c054), L1/eliminate_essential_bc (firm c055), L1/eliminate_rhs (firm c055)
l0_anchor: palace/fem/bilinearform.{hpp,cpp}, palace/fem/libceed/operator.cpp, palace/models/laplaceoperator.cpp, palace/linalg/rap.cpp
justification_kind: structural
---
```

### Change 2 — thread-opener banner → firm-landing note

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: **THREAD-OPENER (cycle-053, abstractor D3).** Observation-first sketch of the finite-element
assembly surface — the rewrite that takes a pure "assemble a global FE operator from a list of
weak-form terms" form into Palace's build-up-then-assemble C++ machinery. This theme **maps the
surface and names the speculative abstractions**; it is deliberately `rough-in`, not a firm
landing. FE assembly is the MFEM-equivalent assembly sub-spine (in scope per CLAUDE.md mesh/FE);
this theme opens it, a cohort of follow-on harvester/abstractor passes fills it.
[new]: **FIRM (promoted cycle-057, lifter D2; opened cycle-053, abstractor D3).** The rewrite that
takes a pure "assemble a global FE operator from a list of weak-form terms" form into Palace's
build-up-then-assemble C++ machinery, plus the two separable BC-elimination post-compositions. FE
assembly is the MFEM-equivalent assembly sub-spine (in scope per CLAUDE.md mesh/FE). Opened as a
thread-opener mapping the surface; promoted to `firm` once all three LHS operators landed firm
([`fe_assemble`](../L1/fe_assemble.md) c054, [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md)
+ [`eliminate_rhs`](../L1/eliminate_rhs.md) c055) and the libCEED leaf-kernel boundary was settled as
[`opaque-library-ownership`](./fe-assemble-libceed-boundary-obstruction.md) (c055).
```

### Change 3 — `## Status` rough-in → firm (clean-gate record)

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: ## Status

`rough-in` (thread-opener). The structural decomposition is recognized and L0-anchored, but the
theme is **not promoted** because (a) its LHS operator [`fe_assemble`](../L1/fe_assemble.md) is now
**firm** (landed cycle-054), but the remaining speculative L1 operators it lowers
(`eliminate_essential_bc`, `eliminate_rhs`) are still rough-in placeholders awaiting harvester
promotion, (b) the libCEED matrix-materialization step crosses an **upstream library boundary**
(see §"libCEED boundary" — logged as OQ, not yet classified obstruction vs. transitive-firm), and
(c) the integrator-term vocabulary (the set of weak-form terms — diffusion / mass / curl-curl /
div-div / ...) is only partially witnessed by this single electrostatic probe. Promotion route: a
harvester pass landing `fe_assemble` firm + an abstractor/lowering-verifier pass settling the
libCEED-boundary classification + a sweep enumerating the integrator-term cohort across the 5
solver pipelines.
[new]: ## Status

`firm`. **Clean-gate call: PROMOTE — clean.** The three gates that held this theme `rough-in` at
authoring time are all closed:

- **(a) all three LHS operators are firm** — [`fe_assemble`](../L1/fe_assemble.md) (c054, the
  integrator-fold `K = Σ_i A(term_i)`), [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md)
  (c055, the operator-side essential-dof pin), and [`eliminate_rhs`](../L1/eliminate_rhs.md) (c055,
  the inhomogeneous-Dirichlet RHS lift). The two elimination legs are no longer rough-in
  placeholders; they are firm separable post-compositions.
- **(b) the libCEED boundary is settled** — the per-term leaf `A(·)` is documented as
  [`obstruction (opaque-library-ownership)`](./fe-assemble-libceed-boundary-obstruction.md) (c055).
  The opaque leaf does **not** gate the theme's firmness: the firm `fe_assemble` fold quantifies
  over `A(term_i)` opaquely, exactly as `ksp_solve` stays firm while its inner MINRES/BiCGStab
  Krylov kernels are obstruction-documented (the same structural relationship — a firm
  outer form over an obstruction-tier inner leaf; see §"libCEED boundary").
- **(c) the term-cohort enumeration does not gate this theme** — the `weak_form_term` type stays a
  deferred rough-in input the assembly fold quantifies over **opaquely** (the fold never cracks open
  a term's `(coefficient, differential-operator)` internals; see `fe_assemble` §Status clean-gate).
  Enumerating the full term cohort across the 5 solver pipelines is follow-on width work, not a
  firmness gate on the rotation theme.

The rewrite's structural decomposition (build-up-then-assemble object protocol → integrator-fold +
PA/FA variant axis + separable BC-elimination post-compositions) is recognized and exhaustively
L0-anchored; the rotation is fully cited (the accumulation `AddSubOperator`
`palace/fem/bilinearform.cpp:77`/`:97` + `Finalize` `:104`, the BC legs
`palace/linalg/rap.cpp:56-82` + `palace/models/laplaceoperator.cpp:216-217`/`:252`). This is the
**firm-on-positive-structure** situation inherited from the three firm LHS operators: each leg's L0
form is read, not constructed.
```

### Change 4 — re-anchor the elimination legs (LHS prose) to firm operators

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: The BC-elimination is a **separable post-composition**, not part of the assembly fold:

    K_bc = eliminate_essential_bc(K, dbc_dofs, DIAG_ONE)
        -- pin the rows/cols of the essential (Dirichlet) dofs; place 1 on the diagonal

    (X, RHS) = eliminate_rhs(K, bc_values, dbc_dofs)
        -- lift the inhomogeneous Dirichlet data into the RHS:
        --   RHS := -K·(BC-extended x), then restore the pinned entries

Of these three pieces, [`fe_assemble`](../L1/fe_assemble.md) is now **firm** (landed cycle-054; its
signature is authoritative there). `eliminate_essential_bc` and `eliminate_rhs` remain **rough-in
placeholders** this thread proposes; their signatures are best-guess pending harvester promotion.
[new]: The BC-elimination is a **separable post-composition**, not part of the assembly fold. Both
legs are now firm L1 operators (signatures authoritative in their entries):

    K_bc = eliminate_essential_bc(K, dbc_dofs, DIAG_ONE)
        -- pin the rows/cols of the essential (Dirichlet) dofs; place 1 on the diagonal

    RHS = eliminate_rhs(K, x_bc, b, policy)
        -- lift the inhomogeneous Dirichlet data into the RHS:
        --   b' := b - K·(BC-extended x_bc), then pin the essential rows per policy

All three pieces are **firm**: [`fe_assemble`](../L1/fe_assemble.md) (c054, the assembly fold),
[`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) (c055, the operator-side essential-dof
pin), and [`eliminate_rhs`](../L1/eliminate_rhs.md) (c055, the inhomogeneous-Dirichlet RHS lift).
Their signatures are authoritative there; this theme narrates how each lowers into Palace's L0
imperative protocol.
```

### Change 5 — bounded citation-correction in §L0-form step 5 (drifted by ±1–2)

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: 5. **BC-elimination into the RHS** (`GetExcitationVector`,
   `palace/models/laplaceoperator.cpp:225-253`): project the Dirichlet boundary values into a
   grid function (`x.ProjectBdrCoefficient(one, source_marker)`, `:236`), restrict to true dofs,
   then `PtAP_K->EliminateRHS(X, RHS)` (`:253`). The elimination body
   (`palace/linalg/rap.cpp:56-82`) computes `RHS := RHS − A·(prolongated BC-extended x)` then
   restores the pinned dof entries — the L0 realization of `eliminate_rhs`.
[new]: 5. **BC-elimination into the RHS** (`GetExcitationVector`,
   `palace/models/laplaceoperator.cpp:225-252`): project the Dirichlet boundary values into a
   grid function (`x.ProjectBdrCoefficient(one, source_marker)`, `:238`), restrict to true dofs
   (`x.ParallelProject(X)`, `:247`), then `PtAP_K->EliminateRHS(X, RHS)` (`:252`). The elimination
   body (`palace/linalg/rap.cpp:56-82`) computes `RHS := RHS − A·(prolongated BC-extended x)` then
   restores the pinned dof entries — the L0 realization of the firm
   [`eliminate_rhs`](../L1/eliminate_rhs.md).
```

### Change 6 — re-anchor §"libCEED boundary" OQ to the settled obstruction annotation

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: This is **upstream library behavior** (libCEED), cited at Palace's call boundary but not itself
Palace source. **Logged as OQ** (see §Open questions): whether the FE-assembly thread treats the
element-local quadrature kernel as (a) a transitive-firm leaf cited at the Palace boundary,
(b) an `obstruction (opaque-library-ownership)` à la the HYPRE relax-type precedent, or
(c) a spine primitive to be re-expressed in tensor-field vocabulary (basis-evaluation +
quadrature-contraction as a tensor contraction). The choice gates how deep this thread goes; it is
a finding for the batch-16 meta-phase, not resolved here.
[new]: This is **upstream library behavior** (libCEED), cited at Palace's call boundary but not itself
Palace source. The classification OQ logged by the thread-opener — (a) transitive-firm leaf,
(b) `obstruction (opaque-library-ownership)`, or (c) tensor-contraction respine — was **settled as
(b)** by the batch-16 meta-phase: see the sibling annotation
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md)
(c055, opaque-library-ownership, deeper-boundary sibling of `triangular-solve-obstruction`). The
opaque leaf sits **strictly below** the firm `fe_assemble` fold — the fold quantifies over
`A(term_i)` opaquely — so the boundary does NOT downgrade the fold or gate this theme's firmness
(the `ksp_solve` / inner-Krylov-kernel structural relationship).
```

### Change 7 — replace `## Speculative L1 operators` (all promoted) with thin residual note

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: ## Speculative L1 operators (need harvester promotion)

- ~~`fe_assemble`~~ — **PROMOTED firm cycle-054**, see [`L1/fe_assemble`](../L1/fe_assemble.md).
- `eliminate_essential_bc` — pin essential (Dirichlet) dofs into the assembled operator.
- `eliminate_rhs` — lift inhomogeneous Dirichlet data into the RHS vector.
- `weak_form_term` (type) — the `(coefficient, differential-operator)` weak-form contribution; the
  element type of the term list `fe_assemble` folds over (diffusion / mass / curl-curl / div-div /
  ... — the term cohort is only partially witnessed here).
[new]: ## Vocabulary status (all LHS operators promoted)

All three L1 operators this theme lowers are now **firm** — no speculative LHS remains:

- [`fe_assemble`](../L1/fe_assemble.md) — **firm c054** (the assembly fold `K = Σ_i A(term_i)`).
- [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) — **firm c055** (operator-side
  essential-dof pin).
- [`eliminate_rhs`](../L1/eliminate_rhs.md) — **firm c055** (inhomogeneous-Dirichlet RHS lift).

One deferred rough-in **input** remains (it does NOT gate this theme — the fold quantifies over it
opaquely, per §Status (c)):

- `weak_form_term` (type) — the `(coefficient, differential-operator)` weak-form contribution; the
  element type of the term list `fe_assemble` folds over (diffusion / mass / curl-curl / div-div /
  ... — the term cohort is only partially witnessed by this electrostatic probe). Enumerating the
  full cohort across the 5 solver pipelines is follow-on width work tracked in the OQ ledger.
```

### Change 8 — bounded citation-correction in §Verified-against (GetExcitationVector range)

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: - `palace/models/laplaceoperator.cpp:225-253` — `GetExcitationVector`: the BC-elimination witness
  (`ProjectBdrCoefficient` + `ParallelProject` + `EliminateRHS`).
[new]: - `palace/models/laplaceoperator.cpp:225-252` — `GetExcitationVector`: the BC-elimination witness
  (`ProjectBdrCoefficient` `:238` + `ParallelProject` `:247` + `EliminateRHS` `:252`).
```

### Change 9 — index dep-map row status-cell flip (cycle-056 D2 index-cell guard)

```edit:book/src/L1-L0/index.md
[old]: | fe-operator-assemble-mutation-rotation *(rough-in; THREAD-OPENER cycle-053)* | [`L1/fe_assemble`](../L1/fe_assemble.md) *(FIRM — cycle-054)* | `palace/fem/bilinearform.{hpp,cpp}`, `palace/fem/libceed/operator.cpp`, `palace/models/laplaceoperator.cpp:184-253`, `palace/linalg/rap.cpp:56-82` | rough-in *(structural; LHS now firm `fe_assemble` — integrator-fold `K=Σ_i A(term_i)` + PA/FA variant axis + separable BC-elimination (`eliminate_essential_bc`/`eliminate_rhs`); slug-collision noted — distinct from BLAS-2 `bilinear-form` `xᴴMy`; `AddSubOperator` accumulation at `bilinearform.cpp:77`/`:97` (theme body cites `:73-75`/`:93-95` — +2 drift, flagged for lifter re-anchor); libCEED matrix-materialization boundary logged OQ (transitive-firm vs opaque-library-ownership vs tensor-contraction-respine); theme RE-ANCHORABLE to firm LHS — lifter pass)* |
[new]: | [fe-operator-assemble-mutation-rotation](./fe-operator-assemble-mutation-rotation.md) *(firm c057; opened c053)* | [`L1/fe_assemble`](../L1/fe_assemble.md) (firm c054) + [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) + [`eliminate_rhs`](../L1/eliminate_rhs.md) (firm c055) | `palace/fem/bilinearform.{hpp,cpp}`, `palace/fem/libceed/operator.cpp`, `palace/models/laplaceoperator.cpp:184-252`, `palace/linalg/rap.cpp:56-82` | firm *(structural; all 3 LHS operators firm — integrator-fold `K=Σ_i A(term_i)` + PA/FA variant axis + separable BC-elimination (`eliminate_essential_bc`/`eliminate_rhs`); slug-collision noted — distinct from BLAS-2 `bilinear-form` `xᴴMy`; `AddSubOperator` accumulation at `bilinearform.cpp:77`/`:97` + `Finalize` `:104`; libCEED leaf-kernel boundary settled as `opaque-library-ownership` (`fe-assemble-libceed-boundary-obstruction` c055) — opaque leaf below the firm fold, does NOT downgrade; `weak_form_term` deferred rough-in input the fold quantifies over opaquely (does not gate firmness))* |
```

### Change 10 — stale §Justification-kind back-reference (libCEED boundary "logged as OQ" → settled)

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: matrix-materialization as the fold's action. (The libCEED boundary is the one non-structural seam;
it is logged as OQ — see §"libCEED boundary".)
[new]: matrix-materialization as the fold's action. (The libCEED boundary is the one non-structural seam;
it is settled as `obstruction (opaque-library-ownership)` — see
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md) and
§"libCEED boundary".)
```

## Discipline notes

- **Pure firm-flip + leg re-anchor; no body re-authoring.** Per lifter discipline, I changed only
  the vocabulary (rough-in placeholder prose → firm live links), the status (frontmatter + body +
  index cell), and three drifted citations. The theme's narrative structure (high→low: L1 fold +
  separable post-compositions → L0 build-up-then-assemble protocol) is untouched. No LHS/RHS shape
  changed: the firmed-up operators' signatures match what the theme already assumed (the fold +
  two separable post-compositions). The one signature-prose touch in Change 4 (the `eliminate_rhs`
  argument list `(K, bc_values, dbc_dofs)` → `(K, x_bc, b, policy)`) is a re-anchor to the firm
  `eliminate_rhs` signature (`book/src/L1/eliminate_rhs.md:51-52`), not a content decision — the
  theme's best-guess placeholder arg list is replaced by the authoritative firm one.

- **Index-cell guard (cycle-056 D2) applied.** Both the theme `## Status` AND the
  `L1-L0/index.md` dep-map row status cell are flipped in the same report (Changes 1+3+9), so the
  table cannot drift out of sync with the theme. The index cell also picks up the +2-drift note's
  resolution (the body now cites `:77`/`:97` correctly — the old "theme body cites `:73-75`/`:93-95`"
  parenthetical is removed because that drift was already corrected in the D6/c055 pass; on-disk
  citecheck confirms the theme body cites `:77`/`:97`).

- **Bounded prose-corrections (3 drifted citations), evidenced + recorded.** Per the
  L0-evidence-driven prose-correction allowance: §L0-form step 5 + §Verified-against cited the
  `GetExcitationVector` witness as `:225-253` / `ProjectBdrCoefficient :236` / `EliminateRHS :253`.
  `citecheck --anchor` against on-disk source shows these are drifted: `ProjectBdrCoefficient` is at
  `:238` (`+2`), `EliminateRHS` is at `:252` (`−1`), and the function body ends at `:252` (`:253` is
  the closing `}`). The firm `eliminate_rhs` sibling entry already carries the correct citations
  (`book/src/L1/eliminate_rhs.md:256-259`: `:225-252`, `:238`, `:247`, `:252`). The correction is
  bounded (drifted-citation fix, no decomposition/signature change) and matches the firm sibling.
  Supporting citecheck output (verified this dispatch):
  - `laplaceoperator.cpp:236 --anchor ProjectBdrCoefficient` → `[DRIFT +2]` suggested `:238`
  - `laplaceoperator.cpp:253 --anchor EliminateRHS` → `[DRIFT −1]` suggested `:252`
  - `laplaceoperator.cpp:238 --anchor ProjectBdrCoefficient` → `[ok]`; `:252 --anchor EliminateRHS` → `[ok]`

- **Citations self-verified at emit time.** Every load-bearing rotation citation was run through
  `citecheck --anchor` against on-disk source before emitting: `bilinearform.cpp:77`/`:97`
  (`AddSubOperator`, zero-drift), `:104` (`Finalize`, zero-drift), `rap.cpp:56-82` (`EliminateRHS`
  decl, in-range), `laplaceoperator.cpp:216-217` (`SetEssentialTrueDofs`, anchor at `:217`),
  `:184-223` (`GetStiffnessMatrix`, anchor at `:184`), `:247` (`ParallelProject`, zero-drift),
  `:238`/`:252` (corrected, zero-drift). Full-file `--scan` of the theme: 15 ok, 0 failing (bounds).

- **Layer-definition discipline (high→low) preserved.** The theme stays defined L1→L0 (LHS = the
  L1 fold + post-compositions, RHS = the L0 build-then-assemble protocol, prose narrates the
  rewrite forward L1→L0). No reverse-direction (L0-lifts-to-L1) notes were added to the chapter.

## Supporting evidence

- `book/src/L1/fe_assemble.md` (firm c054) — §Status clean-gate ("the fold doesn't need to crack
  open the term"); §Downward-to-L0 (`:271-280`) explicitly flags this theme for the lifter
  re-anchor this report performs.
- `book/src/L1/eliminate_essential_bc.md` (firm c055) — §Downward-to-L0 (`:289-300`) flags the
  same re-anchor; signature `:55-58`; the BC-pin L0 sites `rap.cpp:36-47`/`:141-143` +
  `laplaceoperator.cpp:216-217`.
- `book/src/L1/eliminate_rhs.md` (firm c055) — signature `:50-58`; §Evidence (`:245-265`) carries
  the verified `GetExcitationVector` witness citations (`:225-252`, `:238`, `:247`, `:252`) this
  report re-anchors the theme to.
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` (obstruction opaque-library-ownership,
  c055) — §Status: "`fe_assemble` stays FIRM — this annotation does NOT downgrade the fold";
  settles the libCEED-boundary OQ as (b) opaque-library-ownership; the `ksp_solve`/inner-Krylov
  structural-relationship precedent (`:55-57`).
- citecheck self-verification output (this dispatch) — see §Discipline notes.

## Open questions / caveats

- **No contradiction between the firmed-up signatures and the theme's assumptions.** The three firm
  operators realize exactly the fold + two-separable-post-composition shape the theme thread-opener
  assumed; this is a clean lift, not an abstractor reread. (The only signature-prose touch is the
  `eliminate_rhs` arg-list re-anchor, Change 4, which adopts the firm signature verbatim.)
- **`weak_form_term` enumeration remains follow-on width work** (NOT a firmness gate). The
  electrostatic probe witnesses only the diffusion term; the full term cohort (mass / curl-curl /
  div-div / boundary integrators) across the 5 solver pipelines is unenumerated. This is the
  genuinely-new FE vocabulary the sub-spine introduces and is tracked in the OQ ledger; per the
  firm `fe_assemble` clean-gate, the fold quantifies over it opaquely so it does not block the
  theme. Flagging for a future harvester/abstractor term-cohort sweep (not this lifter pass).
- **Sibling `eliminate-rhs-mutation-rotation` / `eliminate-essential-bc-mutation-rotation` themes
  are still forthcoming.** The firm `eliminate_rhs` entry (§Downward-to-L0) references a
  not-yet-authored dedicated `eliminate-rhs-mutation-rotation` L1>L0 theme; this `fe-operator-
  assemble-mutation-rotation` theme currently folds both BC-elimination legs' L0 narration inline.
  Whether the two legs eventually split into dedicated sibling themes (as the firm operators'
  §Downward-to-L0 anticipates) or stay folded into this theme is an abstractor decision, out of
  lifter scope. Flagged for the planner; does not block this firm-flip (the inline narration is
  fully cited).
