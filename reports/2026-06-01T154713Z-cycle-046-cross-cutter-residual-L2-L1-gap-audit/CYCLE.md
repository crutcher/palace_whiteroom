---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-01T154713Z
scope: L1↔L2 cross-cut — residual-L2>L1-gap census after L2-floor reaches 21 firm operators
status: integrated
integrated_at: 2026-06-01T161013Z
integration_commit: f35507b1671d6f61814ad6425016d717443753b3
integration_notes: |
  cycle-046 D3, applied clean (observation/audit, NO book mutation — no `book/` proposed-changes block). Independent census of all 22 L2 chapters against 20 L2-L1/ theme files found TWO genuine L2>L1 gaps: ksp_solve (rank 1, driver tier) + krylov-step (rank 2, kernel tier) — both firm L2 entries with non-identity L2↔L1 rotations and no dedicated L2-L1/* theme file (NOT no-theme-by-design; the apply_linop no-L2 precedent does not transfer). Appended 4 OQ entries: ksp-solve-l2-l1-theme-gap + krylov-step-l2-l1-theme-gap (cycle-047 abstractor x2 candidates, close residual-l2-l1-gap-audit jointly) + residual-l2-l1-gap-audit-planner-undercount (benign data point: census 2 vs dispatch-framing 1) + residual-l2-l1-gap-audit-ksp-solve-edge-mislabel (CLOSED in critique in the report's favor — ksp_solve is a genuine gap). The cycle-047 abstractor x2 pick list is consumed DIRECTLY by the cycle-047 planner. Gate hits: 0 (citecheck 12 ok). No deferrals/rejections.
---

# CYCLE: Cross-layer observation — residual-L2>L1-gap census (krylov-step + ksp_solve both genuine-missing)

## Summary
Sweeping all 22 L2 operator chapters (21 `firm`, 1 `partly-constructive`) against the 20 `L2-L1/` theme files, I independently census which firm L2 operators lack a dedicated L2>L1 lowering theme. The planner's pre-dispatch cross-check reported **one** gap (`krylov-step`). My independent census finds **two**: `krylov-step` AND `ksp_solve`. Both have firm L2 entries with explicitly **non-identity** L2↔L1 rotations stated in-chapter, yet neither has a dedicated `L2-L1/*` theme file (`ksp_solve` does carry an in-chapter §"Lowers from" L2>L1 narration; the gap is the missing dedicated theme file — see below). Both are **genuine-missing-theme** gaps, NOT by-design no-theme cases — the `apply_linop` no-L2-by-design precedent does **not** transfer (apply_linop has *no L2 entry at all*; these two have firm L2 entries whose own prose names a substantive L1 rotation and, in `krylov-step`'s case, explicitly defers content "to the L2>L1 lowering"). Every other firm L2 operator (19 of them) has a same-named or clearly-corresponding L2>L1 theme. The one non-firm L2 op (`deflate`, `partly-constructive`) has its theme (`deflate-composition-lowering`).

## Observation kind
**Coverage gap** — two firm L2 operators (`krylov-step`, `ksp_solve`) have no dedicated `L2-L1/*` lowering theme file (`krylov-step` additionally has no in-chapter §"Lowers from" section at all; `ksp_solve` does carry one, so its gap is specifically the missing dedicated theme file), and the in-chapter evidence establishes the missing rotations are non-identity (substantive), so they are genuine missing-theme gaps rather than no-theme-by-design.

## Specific finding

### Gap census (L2 op × has-L2>L1-theme × genuine-vs-by-design)

| L2 op (status) | L2>L1 theme | gap? | classification |
|---|---|---|---|
| `assemble-diagonal` (firm) | `assemble-diagonal-leaf-identity` | — | covered |
| `axpby` (firm) | `axpby-leaf-identity` | — | covered |
| `axpbypcz` (firm) | `axpbypcz-leaf-identity` | — | covered |
| `axpy` (firm) | `axpy-leaf-identity` | — | covered |
| `chebyshev-iteration` (firm) | `chebyshev-iteration-fusion` | — | covered |
| `deflate` (partly-constructive) | `deflate-composition-lowering` | — | covered |
| `divfree-projector` (firm) | `divfree-projector-leaf-identity` | — | covered |
| `dot` (firm) | `dot-leaf-identity` | — | covered |
| `eigsolve` (firm) | `eigsolve-spectral-transform-composition` | — | covered |
| `elementwise_product` (firm) | `elementwise-product-leaf-identity` | — | covered |
| `gram` (firm) | `gram-fold-specialization` | — | covered |
| `incremental-least-squares` (firm) | `incremental-least-squares-composition-lowering` | — | covered |
| `inner_product` (firm) | `inner-product-fold-specialization` | — | covered |
| `jacobi-smoother` (firm) | `jacobi-smoother-leaf-identity` | — | covered |
| **`krylov-step` (firm)** | **— none —** | **GAP** | **genuine-missing-theme** |
| **`ksp_solve` (firm)** | **— none —** | **GAP** | **genuine-missing-theme** |
| `linear_combination` (firm) | `linear-combination-fold-specialization` | — | covered |
| `normalize` (firm) | `normalize-leaf-identity` | — | covered |
| `nrm2` (firm) | `nrm2-leaf-identity` | — | covered |
| `orthogonalize` (firm) | `orthogonalize-composition-lowering` | — | covered |
| `reciprocal` (firm) | `reciprocal-leaf-identity` | — | covered |
| `scal` (firm) | `scal-leaf-identity` | — | covered |

Census mechanics: 22 L2 chapters (`book/src/L2/*.md` minus `index.md`), 20 L2>L1 themes (`book/src/L2-L1/*.md` minus `index.md`), and the `L2-L1/index.md` theme table carries exactly 20 `| [...]` rows (`eigsolve-spectral-transform-composition` is one of those 20 rows, not a separate prose-list entry) — confirming 20 themes total, none stemmed `krylov-step` or `ksp_solve`. Arithmetic: 22 L2 ops − 20 themed = 2 gaps. Cross-checked by normalized stem prefix (`_`→`-`): every firm L2 op except `krylov-step` and `ksp_solve` resolves to a same-stem theme. I also grepped the theme directory for `ksp_solve`/`krylov-step` as a *subject* (a "Lowers from L2 `ksp_solve`" theme) — the only hits are cross-references inside other themes (`eigsolve-spectral-transform-composition.md`, `incremental-least-squares-composition-lowering.md`, `dot-leaf-identity.md`, `divfree-projector-leaf-identity.md`), none of which is the dedicated theme for either operator. So no mis-named or silently-mislocated theme covers them.

### Why both are genuine-missing, not by-design

**`ksp_solve` — non-identity L2↔L1 rotation stated in-chapter, no theme.**
- `book/src/L2/ksp_solve.md:155-157` (§"Lowers from"): "L2 `ksp_solve` lowers from L1 `ksp_solve` … **The rotation is *not* identity**: L1 opacity is opened at L2 (the `krylov-step` kernel and the convergence-test fold that wraps it become visible); the L1 absorbed `krylov-method` axis re-surfaces as the L2 solver-method loop-shaping axis…". This is a substantive un-collapse-the-opacity rotation — exactly the kind that warrants a dedicated L2>L1 theme.
- `book/src/L2/ksp_solve.md:153` (§Status) and `book/src/L2/index.md:92` (dep-map row) both assert the L2↔L1 relationship is **non-identity**, and the index row even links the *L3>L2* theme `L3-L2/ksp-solve-outer-driver` (firm cycle-021) — so the operator's loop-erasure story is themed *upward* (L3>L2) but the un-collapse story is *not* themed *downward* (L2>L1). Asymmetric coverage.
- The §"Lowers from" prose narrates the rewrite forward (L2 form → L1 form) but, per the high→low discipline, defers the firming-evidence / reverse direction to working-notes — i.e. the chapter explicitly does NOT carry the theme content; it expects a theme.

**`krylov-step` — chapter explicitly defers content "to the L2>L1 lowering" that does not exist.**
- `book/src/L2/krylov-step.md:121` (variant-axis 6, in-place buffer): "the L2 form is uniformly out-of-place, **with the in-place specialisation reappearing in the L2>L1 lowering**." This is a direct forward-reference to an L2>L1 lowering as the home for the in-place-buffer rotation content — and that lowering has no file.
- `krylov-step` has **no** §"Lowers from" / §"Downward to L1" section at all — its heading sequence is §Dependencies → §Status → §"L2 vs L1 distinction" → §Evidence (`book/src/L2/krylov-step.md:92,125,129,134`). It is the only firm L2 named-composition operator missing a downward-lowering section, consistent with the missing theme.
- The rotation is non-trivial: `krylov-step`'s body composes seven L1 primitives (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal` — `book/src/L2/krylov-step.md:96`) under a fold, with six variant axes absorbed at construction (`:114-123`). The de-fusion of the per-step kernel into those L1 leaves (and the in-place→out-of-place buffer rotation) is the substantive L2>L1 content — not identity-in-form.

**The `apply_linop` by-design precedent does NOT transfer.**
- `book/src/L3/apply_linop.md:142-146` frames apply_linop as no-L2-by-design: "L3 `apply_linop` lowers to L1 `apply_linop` directly — **no interposed L2 entry, no L3-L2 theme** … the L2 layer does not host an `apply_linop` entry (per the cycle-010 audit's L2 verdict, primitives like `apply_linop` are referenced from L2 compositions but do not get standalone L2 entries)." The by-design case is "**no L2 entry exists**, so no theme touching it." `krylov-step` and `ksp_solve` are the opposite: both have **firm L2 entries** (`book/src/L2/krylov-step.md:125`, `book/src/L2/ksp_solve.md:151`), so the layer-coherence invariant "each layer is coherent within itself" applies in full and the missing piece is the L2>L1 *theme*, not the operator. The `L3/apply_linop:146` no-L2-by-design framing is about a *missing operator*; here the operators are present and firm.

## Recommendation

**Dispatch abstractor (×2) on the two coverage gaps to draft the missing L2>L1 themes** — fan-out-ranked for the cycle-047 planner:

1. **`ksp_solve` L2>L1 theme (rank: HIGHER)** — route: abstractor. Slug suggestion `L2-L1/ksp-solve-outer-driver-unfold` (or `ksp-solve-opacity-uncollapse`) to parallel the existing *upward* `L3-L2/ksp-solve-outer-driver`. Fan-out: `ksp_solve` is consumed by `eigsolve` (`book/src/L2/eigsolve.md` per-step body inverts `(K−σM)`), `divfree-projector` (`book/src/L2/divfree-projector.md` inner H1 solve, carries the obstruction by reference), and `incremental-least-squares` (`book/src/L2/incremental-least-squares.md:91` `materialise_iterate`). Themeing the L2↔L1 un-collapse closes the asymmetry where the L3>L2 edge is themed but the L2>L1 edge is not. **Rank above `krylov-step`** because ksp_solve sits at the driver tier with the wider downstream-reuse set, and its non-identity rotation is the more substantive (whole-opacity un-collapse vs. a primitive de-fusion).

2. **`krylov-step` L2>L1 theme (rank: HIGH)** — route: abstractor. Slug suggestion `L2-L1/krylov-step-kernel-defusion` (the kernel-body de-fusion into the seven L1 leaves + the in-place→out-of-place buffer rotation that `book/src/L2/krylov-step.md:121` explicitly defers here). Fan-out: `krylov-step` is the kernel half folded by `ksp_solve`, `chebyshev-iteration`, and (transitively) `eigsolve`; it is the consumed-by surface for the cycle-004 MINRES/BiCGStab obstruction themes. Authoring this theme also resolves the dangling forward-reference at `:121` and lets the planner drop the perpetual re-flag.

Audit-first note: I did **not** foregone-conclude this. I read both L2 chapters' downward sections and the `apply_linop` precedent before ruling. The evidence — two firm L2 entries each asserting a non-identity L2↔L1 rotation in their own prose, one of them explicitly deferring content "to the L2>L1 lowering" — supports **genuine-gap** for both. If the planner prefers, a single abstractor dispatch could draft both as a paired `(kernel, driver)` theme set (mirroring the L2 `(krylov-step, ksp_solve)` kernel/driver pairing), but the role-spec one-theme-per-dispatch discipline favors two dispatches.

A by-design closure is **not** warranted here, so no OQ-ledger by-design-rationale recording is recommended (that path was the fallback had the ruling gone the other way).

## Supporting evidence
- `book/src/L2/` — 22 chapters; 21 `firm`, `deflate` `partly-constructive` (`book/src/L2/deflate.md` §Status).
- `book/src/L2-L1/` — 20 theme files; `L2-L1/index.md` theme table (20 `| [...]` rows; `eigsolve-spectral-transform-composition` is one of those rows).
- `book/src/L2/ksp_solve.md:151,153,155-157,161` — §Status / §"Lowers from" (non-identity L2↔L1) / §"Lifts to" (the *upward* L3>L2 theme `ksp-solve-outer-driver` is pending/firm but is the L3 edge, not L2>L1).
- `book/src/L2/krylov-step.md:92,96,114-123,125,129` — §Dependencies (7 L1 primitives), §Variant-axes (axis 6 `:121` defers in-place specialisation "to the L2>L1 lowering"), §Status (firm), §"L2 vs L1 distinction" — and the *absence* of any §"Lowers from".
- `book/src/L2/index.md:74,92,95` — dep-map rows: `krylov-step` (no L2>L1 theme named), `ksp_solve` (non-identity L2↔L1 + links the L3>L2 theme only), `eigsolve` (non-identity, but themed by `eigsolve-spectral-transform-composition`).
- `book/src/L3/apply_linop.md:142-146` — the no-L2-by-design precedent (apply_linop has *no L2 entry*; structurally different from the two gaps).
- `book/src/L2-L1/eigsolve-spectral-transform-composition.md` — confirms eigsolve's L2>L1 theme lowers eigsolve's *body* to L1 `ksp_solve` (as a leaf); it does NOT cover the `ksp_solve` or `krylov-step` L2>L1 rotations themselves.

## Open questions / caveats
- **Planner pre-dispatch undercounted by one.** The dispatch framing said "every L2 op has a same-named L2>L1 theme EXCEPT `krylov-step`." My independent census finds `ksp_solve` is *also* uncovered. Worth verifying the planner's source of the one-gap claim before the cycle-047 picks are finalized.
- **[CLOSED — resolved in critique]** The edge-mislabel risk I flagged (that `L3-L2/ksp-solve-outer-driver` might silently carry the *L2>L1* content, making `ksp_solve` a mislabel rather than a genuine gap) is **resolved against the mislabel**. The critic read `L3-L2/ksp-solve-outer-driver.md` in full: it is unambiguously an L3>L2 theme (LHS = the L3 explicit `iterate_while_L3` tail recursion :21-38, RHS = the L2 outer-driver-by-role wrap :40-57) and it **explicitly delegates the L2>L1 edge** to the L2 chapter's in-line §"Lowers from" (`ksp-solve-outer-driver.md:15` lists the L2>L1 un-collapse as a *separate* firm edge recorded in-line in the L2 entry). So the L3>L2 file does NOT carry the L2>L1 content; `ksp_solve`'s L2>L1 edge is a genuine missing-dedicated-theme gap. No cycle-047 follow-up needed on this — the caveat was honest and is now closed in the report's favor.
- The `krylov-step` §"L2 vs L1 distinction" (`:129-132`) discusses the L1-vs-L2 *conceptual* distinction but is not a forward-narrated lowering (it does not narrate L2 form → L1 form rewrite the way a theme or a §"Lowers from" does), so it does not substitute for the missing theme. Verify the abstractor treats it as context, not as the lowering.
- Both gaps are net-new theme authoring (abstractor), not lifter re-anchoring — no operator signature changed; this is a coverage gap, not a consistency drift.
