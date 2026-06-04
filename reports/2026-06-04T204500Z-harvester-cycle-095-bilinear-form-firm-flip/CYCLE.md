---
agent: harvester
invoked_at: 2026-06-04T204500Z
scope: L1 operator: bilinear-form (firm-flip + HARD-gate-new typed frontmatter + within-file re-anchor + L1/index count-owner)
status: integrated
integrated_at: 2026-06-04T231500Z
integration_commit: efe6872
integration_notes: "cycle-095 D1 (staging position 1/7). bilinear-form rough-in->firm + the campaign's FIRST HARD-gate-new typed edges: block (rank-gate PASS firm-over-firm: dot/apply_linop/matrix-weighted-norm) + L1/index count-owner (firm 31->32 main / 38->39 grand). Applied clean, all 9 proposed-change blocks verbatim; retroactive-budget 0. Part of the bilinear-form firm-flip cascade contributing to the 22->1 rank-violation drop."
inputs:
  - reports/2026-06-04T204023Z-cycle-planner-cycle-095/CYCLE.md (D1 scope)
  - book/src/methodology/graded-stack-scheme.md (edges:/rank:/feature_root: grammar; §1 ladder, §2 edge block, §4(a) supersession)
  - reports/2026-06-04T065200Z-lowering-verifier-cycle-092-bilinear-form-probe/ (the DISCHARGE probe; verified_against: block on disk)
  - book/src/L1/bilinear-form.md (the operator being flipped)
  - book/src/L1/index.md (count-owner: :31 grand-total/main-cohort, :67 cohort bullet, :113 dep-map cell, :101 joint-OQ)
  - book/src/L1/dot.md:100 (firm dep), book/src/L1/apply_linop.md:87 (firm dep), book/src/L1/matrix-weighted-norm.md:110 (firm dep)
---

# CYCLE: Flip bilinear-form to firm at L1 (HARD-gate-new typed frontmatter + within-file re-anchor + count-owner)

## Summary

This is **D1, Wave 1** of cycle-095 (the bilinear-form firm-flip-and-cascade-wave / GRADED-STACK P1 launch). The L1 `bilinear-form` verb — the matrix-weighted inner-product reduction `α = xᴴ M y`, the matrix-weighted generalisation of `dot` (the `M = I` special case) — was firmability-**DISCHARGED** at cycle-092 (the scoped `lowering-verifier` probe `reports/2026-06-04T065200Z-lowering-verifier-cycle-092-bilinear-form-probe/`): the firm-on-positive-structure escape APPLIES, the `verified_against:` block is on disk (confirmed, `book/src/L1/bilinear-form.md:473-511`), and the c092 dispatch deliberately left the maturity token `rough-in` per the c088/c089 gate-test-then-separate-gated-wave discipline. **This dispatch is that gated wave's verb-flip.**

Four coupled edits, all in my ownership partition:

1. **Flip the verb firm** — `firmness: rough-in` → `firm` in frontmatter; restate the §Status conclusion as ENACTED (the verb IS firm via the discharged escape), not as a pending probe. The §Status "the maturity token stays `rough-in` in THIS dispatch by design" paragraph and the cycle-010 repair-note's open-ended "firm-promotion-eligible" tail are both re-anchored to the firm conclusion.

2. **HARD-gate-new typed graded-stack frontmatter** (the campaign's FIRST new-work rank-gate exercise) — add `rank: firm` and an `edges:` block: `depends-on:` → `L1/dot`, `L1/apply_linop`, `L1/matrix-weighted-norm` (ALL verified `firm` on disk this cycle, so the rank invariant `rank(u) ≤ min over depends-on deps` holds — a firm node resting only on firm nodes), and `reference:` → the L1>L0 theme cross-link `L1-L0/bilinear-form-mutation-rotation`. This **supersedes** the ad-hoc `depends_on:` + `lowers_to:`/`lifts_from:` frontmatter (scheme §4(a)) — replaced, not duplicated.

3. **WITHIN-FILE self-consistency re-anchor** (the batch-29 discipline; THIS is the first flip to carry it) — the operator's OWN file re-read end-to-end; every conclusion narration that concluded "rough-in" re-anchored to the firm §Status: the §Context "is a **rough-in** rather than firm" paragraph (`:45-53`), the §Dependencies self-note "the `bilinear-form` half remains open" (`:251-257`), the §Status gate-(c)-style "stays rough-in by design" conclusion (`:368-375`), and the cycle-010 repair-note tail (`:377-387`).

4. **SOLE owner of `book/src/L1/index.md` count headers** — `:31` grand-total 38→39 + main-cohort firm 31→32 (verified current numbers on disk); `:113` dep-map TABLE cell rough-in→firm; `:67` the §Vocabulary-cohort BULLET moved out of the now-empty "Rough-in (test-coverage-bounded)" sub-list into the firm sub-list; `:101` the joint-OQ narration "bilinear-form half remains rough-in" → firm.

**Dependency-firmness verification (rank invariant):** `dot` §Status `firm` (`book/src/L1/dot.md:100`); `apply_linop` §Status `firm` (`book/src/L1/apply_linop.md:87`); `matrix-weighted-norm` §Status `firm` (`book/src/L1/matrix-weighted-norm.md:110`, promoted c091). All three rank-3 → `rank(bilinear-form=firm=3) ≤ min(3,3,3)` holds. The `reference:` edge to the L1>L0 theme constrains nothing (navigational; per scheme §2).

`bilinear-form` is already registered in `book/src/SUMMARY.md:176` — no SUMMARY edit needed (this is a flip, not a fresh chapter).

## Proposed changes

### (1)+(2)+(3) the operator file — frontmatter flip + typed edges + within-file re-anchor

Frontmatter: flip `firmness`, add `rank: firm`, and replace the ad-hoc `depends_on:`/`lowers_to:`/`lifts_from:` block with the typed `edges:` block (scheme §4(a) supersession).

```edit:book/src/L1/bilinear-form.md
---
layer: L1
operator: bilinear-form
firmness: firm
rank: firm
edges:
  depends-on:
    - L1/dot
    - L1/apply_linop
    - L1/matrix-weighted-norm
  reference:
    - L1-L0/bilinear-form-mutation-rotation
variant_axes:
  - precision-mode
  - output-arg-pattern
  - M-symmetry-property
  - parallel-wrapper
---
```

Note on the `edges:` block (recorded here for the integrator, not authored into the file): `L1/dot` and `L1/apply_linop` were the pre-existing `depends_on:` entries (the two folded primitives of the `dot(x, apply_linop(M, y))` unfolding); `L1/matrix-weighted-norm` is added as a `depends-on` because the SPD-diagonal `y = x` case `bilinear_form(x, B, x)` IS the firm `matrix-weighted-norm` sibling that discharges law-8 PSD content (per the c092 probe point 2 + the `verified_against:` entry `book/src/L1/matrix-weighted-norm.md:108-115`) — the dispatch brief lists exactly these three. The bare-string form is used (scheme §2: a bare string ≡ `{target: <string>}` with no kind; the linters read only `target` + the bucket). `lowers_to: []` / `lifts_from: []` were empty and are dropped (the L1>L0 lowering is a `reference` cross-link here, not a populated `lowers_to:` — the theme is firm and D2-owned; per scheme §2 the feature-/theme- navigational pointer is `reference`).

Re-anchor the §Context "is a **rough-in**" conclusion (`:45-53`):

```edit:book/src/L1/bilinear-form.md
`bilinear-form` is **firm** (promoted from `rough-in` cycle-095, the
bilinear-form-firm-flip-and-cascade-wave; firmability DISCHARGED by the
cycle-092 `lowering-verifier` probe — see *Status* below). The structural
signature is well-anchored at L0 and the algebraic laws are inherited cleanly
from the firm L1 dependencies `dot`, `apply_linop`, and `matrix-weighted-norm`;
the formerly-cited narrow-variant-axis-coverage gate was judged REDUNDANT under
the firm-on-positive-structure escape (the two surfaced use sites are the only
matrix-weighted `Dot` call sites in the tree, and the one unexercised shape —
real-`M`-real-`y` `xᵀ M y` — is not surfaced by Palace at all). *(An earlier
draft listed a second gating reason — an alleged L0 comment-vs-implementation
conjugation disagreement — that was based on a misreading of the L0 free-function
`linalg::LocalDot` convention. The L0 source is self-consistent: see Status and
the `bilinear-form-conjugation-convention-anchor` OQ for the verification.)*
```

Re-anchor the §Dependencies self-note "the `bilinear-form` half remains open" (`:251-257`):

```edit:book/src/L1/bilinear-form.md
Future `nrm2_B`-weighted operator (cycle-010 wave-1 sibling dispatch #5,
addressing cycle-008 OQ `nrm2-B-weighted-energy-norm-harvest` and the
sibling OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` — BOTH
halves of which are now resolved: the `matrix-weighted-norm` half promoted to
`firm` at cycle-091, and the `bilinear-form` half promoted to `firm` at
cycle-095 (this dispatch, the firm-flip-and-cascade wave)) will likely
depend on `bilinear-form` via `nrm2_B(x, B) = √bilinear_form(x, B, x)` when
`B` is SPD (law 8). That is the L1 statement of the energy norm.
```

Re-anchor the §Status opener (`:321-326` — the `rough-in (lower-layer-shared-vocabulary...)` token) to ENACTED firm:

```edit:book/src/L1/bilinear-form.md
## Status

`firm` (promoted from `rough-in (lower-layer-shared-vocabulary,
cycle-010-wave-1)` at **cycle-095**, the `bilinear-form-firm-flip-and-cascade-wave`,
on the **firm-on-positive-structure escape** — DISCHARGE established by the
cycle-092 `lowering-verifier` probe, `verified_against:` block below). The
structural signature is anchored at L0 (`palace/linalg/operator.hpp:385-394`,
`palace/linalg/operator.cpp:621-639`), and the laws are inherited cleanly from
the firm L1 dependencies `dot` (`book/src/L1/dot.md:100`), `apply_linop`
(`book/src/L1/apply_linop.md:87`), and `matrix-weighted-norm`
(`book/src/L1/matrix-weighted-norm.md:110`, firm c091).

**Firmability DISCHARGED (cycle-092 dischargeability probe; `verified_against:`
block below) and ENACTED (cycle-095, this dispatch).** A scoped
`lowering-verifier` probe (the c088/c089 `matrix-weighted-norm` pattern) judged
that the **firm-on-positive-structure escape** (CLAUDE.md §Methodology
invariants, the `rough-in (test-coverage-bounded)` bullet) APPLIES to this
operator; cycle-095 enacts the flip:
```

Re-anchor the §Status gate-(c)-style "stays rough-in by design" conclusion (`:368-375`) to ENACTED:

```edit:book/src/L1/bilinear-form.md
**The flip is ENACTED in cycle-095** (the `bilinear-form-firm-flip-and-cascade-wave`):
the c092 probe was the gate-TEST (per the c088/c089 discipline — the probe
establishes firmability, the flip is a separate gated wave), and cycle-095 lands
the firm flip together with the coupled `gram_reduce` firm re-judgment (D3), the
4-column (capacitance/inductance/electrostatic/magnetostatic) unblock (D4), and
the whole-book cross-reference re-anchor (D2). What the probe established and this
dispatch enacts: the verb IS firm via the escape; nothing structural blocks it;
the residual coverage gate is redundant.
```

Re-anchor the cycle-010 repair-note tail (`:377-387` — the open-ended "firm-promotion-eligible" close) to the resolved firm conclusion:

```edit:book/src/L1/bilinear-form.md
*(Repair note — cycle-010 critic pass: an earlier draft listed a second
gating reason (an alleged L0 comment-vs-implementation conjugation
disagreement). That claim was based on a misreading of the L0 free-function
`linalg::LocalDot` convention. Verified at `palace/linalg/vector.cpp:674-685`
that the free-function conjugates the second argument, yielding `yᴴ x`;
this is already documented at `book/src/L1/dot.md:43, 104-105`. The L0
source `linalg::Dot(comm, A·x, y) = yᴴ A x` matches the L0 comment at
`palace/linalg/operator.hpp:386`. The false gating reason was removed; the
single remaining gating reason (narrow variant-axis coverage) was then judged
REDUNDANT under the firm-on-positive-structure escape (cycle-092 probe), and
the verb was promoted to firm at cycle-095.)*
```

### (4) `book/src/L1/index.md` — count-owner edits (SOLE owner this cycle)

Grand-total + main-cohort firm bump (`:31`). Current on disk: **31 main + 4 FE-assembly + 3 FE-space = 38**; bilinear-form joins the main cohort → **32 main / 39 grand**. (Only the count-bearing leading sentences are edited; the long enumerated tail is left intact except the two count tokens and one appended clause naming bilinear-form as the 32nd main-cohort firm member.)

```edit:book/src/L1/index.md
**Firm (32 main cohort; 39 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 32 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), and the FE-space sub-spine adds **3** more firm (`fe_space` c064 + `fe_collection` c065 + `essential_dofs` c066 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **39** (cycle-095 D1 added the 32nd main-cohort firm member `bilinear-form`, the matrix-weighted inner-product reduction `xᴴ M y` — promoted rough-in→firm by the `bilinear-form-firm-flip-and-cascade-wave` on the firm-on-positive-structure escape, firmability discharged by the cycle-092 `lowering-verifier` probe; cycle-080 D2 added the then-30th main-cohort firm member `eigenvalue-untransform`, the eigenvalue→ω un-transform scalar map `√μ`/`λ/i` — the SECOND per-mode scalar building block the L4 `eigenfreq_qfactor_reduce` fold folds, firming the eigenvalue-un-transform half of that verb's gate-(a); was 36 after cycle-077: 29 main + 4 FE-assembly + 3 FE-space; cycle-077 D5 added the main-cohort's 29th firm member `port_projection`, the port-mode linear-functional projection `⟨s, E⟩`; cycle-077 D4 added the 28th firm member `participation_ratio`, the energy-participation-ratio scalar-quotient primitive; cycle-066 D1 added the FE-space sub-spine's third firm member `essential_dofs`, the boundary-attribute→essential-true-dof-set constructor). Count discipline: the grand total is computed by reading each linked chapter's `## Status` line, not the index cells — 32 main + 4 FE-assembly + 3 FE-space = 39; equivalently the dep-map table now holds **39** `firm` rows (incl. `bilinear-form` c095 — promoted rough-in→firm by the cycle-095 firm-flip-and-cascade wave, the main-cohort's 32nd firm member) (incl. `matrix-weighted-norm` c091 — promoted rough-in (test-coverage-bounded)→firm by the batch-29 LEAD firm-flip-and-cascade wave, the main-cohort's 31st firm member) (incl. `eigenvalue-untransform` c080, `assemble_frequency_operator` c062, `port_projection` c077, `fe_assemble` c054, `fe_space` c064, `fe_collection` c065, and `essential_dofs` c066). All firm rows are now on-table; there is no off-table firm operator. **Count-reconciliation note DISCHARGED (cycle-091, batch-29 LEAD):** the pre-staged c080 reconciliation +1 is now folded — `matrix-weighted-norm` was promoted rough-in (test-coverage-bounded)→firm by the firm-flip-and-cascade wave, its bullet moved from the §"Rough-in (test-coverage-bounded)" sub-list to the firm sub-list, and BOTH the main-cohort count (30→31) and the grand total (37→38) updated above; cycle-095 then promoted `bilinear-form` rough-in→firm (32 main / 39 grand) and likewise moved its bullet out of the now-empty §"Rough-in (test-coverage-bounded)" sub-list. The 32 main-cohort firm operators are element-wise updates, BLAS-1 reductions, the matrix-weighted inner-product reduction (`bilinear-form`, c095 — `xᴴ M y` for arbitrary linear `M`, the matrix-weighted generalisation of `dot`), the fused-normalise primitive, the energy-participation-ratio scalar-quotient primitive (`participation_ratio`, c077), the eigenvalue→ω un-transform scalar map (`eigenvalue-untransform`, c080 — the `√μ`/`λ/i` per-mode un-transform keyed on EVP-degree, the second per-mode scalar building block of `eigenfreq_qfactor_reduce`), the port-mode linear-functional projection (`port_projection`, c077), the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, the NEP quasi-Newton Jacobian action, the NEP quasi-Newton eigenvalue-correction step, the GMRES/FGMRES restart-correction back-solve, the GMRES/FGMRES per-column running-QR leaf, the diagonal-preconditioner-apply Jacobi smoother, the elementwise multiplicative-inverse primitive, the elementwise (Hadamard) pointwise-product primitive, the floquet-periodicity B-field correction gate, the driven per-ω system-operator assembly (`assemble_frequency_operator`, c062), and the SPD operator-weighted energy norm (`matrix-weighted-norm`, c091 — `‖x‖_B = √(xᴴ B x)`, promoted rough-in (test-coverage-bounded)→firm by the batch-29 LEAD firm-flip-and-cascade wave on the firm-on-positive-structure escape, both norm-axiom law-sides discharged c088 structure + c089 FP, gate (a) judged redundant):
```

Move the §Vocabulary-cohort BULLET out of the now-empty "Rough-in (test-coverage-bounded)" sub-list (`:65-67`) and into the firm sub-list. The firm bullet is appended after the `matrix-weighted-norm` firm bullet (`:41`, alphabetical-within-grouping neighbour `bilinear-form` actually sorts before `dot`; I place it immediately after the `axpbypcz` BLAS-1 leaf at `:43` per the table's alpha order `axpy/axpby/axpbypcz/bilinear-form/dot/...`). Two edits:

Replace the now-empty "Rough-in (test-coverage-bounded)" sub-list header+bullet (`:65-67`) — the sub-list has exactly one member (`bilinear-form`), so it becomes empty and is retired with a discharge note:

```edit:book/src/L1/index.md
**Rough-in (test-coverage-bounded)** — operators whose structural signature is well-anchored at L0 but whose algebraic-law confidence is reduced pending dedicated test coverage or expanded literature anchoring:

- *(empty as of cycle-095)* — the sole former member [`matrix-weighted-norm`](./matrix-weighted-norm.md) was promoted to **firm** at cycle-091 (batch-29 LEAD), and the sibling [`bilinear-form`](./bilinear-form.md) — which had carried the related `rough-in (lower-layer-shared-vocabulary)` qualifier — was promoted to **firm** at cycle-095 (the firm-flip-and-cascade wave) on the firm-on-positive-structure escape. Both bullets now live in the firm sub-list above. No operator currently carries the test-coverage-bounded qualifier.
```

Append the `bilinear-form` firm bullet to the firm sub-list, immediately after the `axpbypcz` bullet (`:43`, preserving the table's BLAS-1 alpha order `axpy/axpby/axpbypcz/bilinear-form/dot`):

```edit:book/src/L1/index.md
- [`axpbypcz`](./axpbypcz.md) — fused three-scalar three-vector update; subsumes `axpby` (γ=0) and `axpy` (β=1, γ=0).
- [`bilinear-form`](./bilinear-form.md) — pure matrix-weighted inner-product reduction `xᴴ M y` for an arbitrary linear operator `M` (no SPD requirement); the matrix-weighted generalisation of [`dot`](./dot.md) (the `M = I` special case, `bilinear_form(x, I, y) = dot(x, y)`). Factors as the syntactic composition `dot(x, apply_linop(M, y))` over the firm [`dot`](./dot.md) + firm [`apply_linop`](./apply_linop.md); the SPD-diagonal `y = x` case is the firm [`matrix-weighted-norm`](./matrix-weighted-norm.md) sibling (c091) that discharges its law-8 PSD content. Promoted rough-in→**firm** cycle-095 (the `bilinear-form-firm-flip-and-cascade-wave`) on the **firm-on-positive-structure escape** — firmability discharged by the cycle-092 `lowering-verifier` probe: laws 1-6 are pure linearity/annihilation/identity-specialisation syntactic read-offs with NO inner-product-norm theorem content, laws 7-8 are M-symmetry-conditional identities with both witnesses on-disk (Hermitian `Bttr` / non-Hermitian `Atn`, `palace/models/boundarymodeoperator.cpp:85`/`:90`), and the narrow-variant-axis-coverage gate was judged REDUNDANT (the two surfaced use sites are the only matrix-weighted `Dot` call sites in the tree, and the unexercised real-`M`-real-`y` `xᵀ M y` shape is not surfaced by Palace at all). M-symmetry-property THE material variant axis (laws 7/8 conditional). L1>L0: [`bilinear-form-mutation-rotation`](../L1-L0/bilinear-form-mutation-rotation.md).
```

Dep-map TABLE cell (`:113`) rough-in→firm:

```edit:book/src/L1/index.md
| [`bilinear-form`](./bilinear-form.md) | `(x: Tensor[M], M: LinearOperator[M, N], y: Tensor[N]) → Scalar` (i.e. `xᴴ M y`) | `dot`, `apply_linop`, `matrix-weighted-norm` | `firm` (matrix-weighted inner-product reduction `xᴴ M y` for arbitrary linear `M`; the matrix-weighted generalisation of `dot`, `M = I` special case; promoted rough-in→firm cycle-095 by the `bilinear-form-firm-flip-and-cascade-wave` on the firm-on-positive-structure escape — firmability discharged by the cycle-092 `lowering-verifier` probe, laws 1-6 syntactic read-offs over firm `dot`+`apply_linop` with no norm-axiom content, laws 7-8 M-symmetry-conditional with both witnesses on-disk, narrow-variant-axis-coverage gate judged REDUNDANT; L0: `palace/linalg/operator.hpp:385-394` + `palace/linalg/operator.cpp:621-639`; L1>L0: [`bilinear-form-mutation-rotation`](../L1-L0/bilinear-form-mutation-rotation.md)) |
```

Joint-OQ narration (`:101`) rough-in→firm:

```edit:book/src/L1/index.md
- (empty as of cycle-010) — the cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` is now **fully answered**: both halves landed in cycle-010 wave-1 as rough-ins and both are now **firm** — the [`matrix-weighted-norm`](./matrix-weighted-norm.md) half promoted cycle-091 (the batch-29 LEAD firm-flip-and-cascade wave) and the [`bilinear-form`](./bilinear-form.md) half promoted cycle-095 (this cycle's firm-flip-and-cascade wave, on the firm-on-positive-structure escape). The `SpectralNorm` (power-iteration) sibling remains the OQ's sole open residual; both L1>L0 lowering themes (`matrix-weighted-norm-mutation-rotation`, `bilinear-form-mutation-rotation`) are themselves firm.
```

## Operator content (the firm bilinear-form entry, as written into the file)

- **Slug + one-line**: `bilinear-form` — mutation-free matrix-weighted inner-product reduction `α = xᴴ M y`; the matrix-weighted generalisation of `dot` (the `M = I` special case).
- **Signature**: `bilinear_form :: (x: Tensor[M], M: LinearOperator[M, N], y: Tensor[N]) -> Scalar`, `bilinear_form(x, M, y) = xᴴ M y`. Shape contract: `x : Tensor[M]` (codomain of `M`), `M : LinearOperator[M, N]`, `y : Tensor[N]` (domain of `M`), result `Scalar` (complex for the two surfaced element-type rows). Unchanged from the rough-in body (the flip does not touch Signature/Semantics/Laws/Variant-axes — only the maturity narration + frontmatter + count cells).
- **Algebraic laws**: laws 1-8 unchanged (1-6 linearity/annihilation/identity-specialisation; 7 Hermitian-`M` Hermitian symmetry, conditional; 8 PSD-at-`y=x` for SPD `M`, conditional). The two stated non-laws (general-`M` symmetry, FP Cauchy–Schwarz strictness, FP associativity) unchanged. These were the discharge substrate, not re-derived here.
- **Dependencies** (typed `edges: depends-on:`): `L1/dot`, `L1/apply_linop`, `L1/matrix-weighted-norm` — all firm. `reference:` → `L1-L0/bilinear-form-mutation-rotation`.
- **Status**: `firm` (promoted rough-in→firm cycle-095; firm-on-positive-structure escape, DISCHARGE c092, ENACTED c095).
- **Record definition**: the signature names `Tensor`, `LinearOperator`, `Scalar` — all shared L1 primitive types (no operator-local config/state record is introduced). `LinearOperator[M, N]` is the opaque-operator type defined by `apply_linop`'s chapter (cross-referenced, not redefined). No new record-definition home is owed by this entry (the record-definition obligation no-ops — the signature names no operator-specific struct).

## Supporting evidence

- **DISCHARGE provenance**: `reports/2026-06-04T065200Z-lowering-verifier-cycle-092-bilinear-form-probe/` — the scoped probe that judged the firm-on-positive-structure escape APPLIES; its `verified_against:` block (8 entries) is on disk at `book/src/L1/bilinear-form.md:473-511` (confirmed present this cycle).
- **Sibling-reduce-verb escape precedents** (cited in the restated §Status): `apply_nonlinear_pencil` (c021), `eigenfreq_qfactor_reduce` (c082), `sparameter_reduce` (c083), `solve_family` (c086), `matrix-weighted-norm` (c091) — the prior firm-on-positive-structure promotions the c092 probe and the planner brief name.
- **Rank-invariant dependency firmness (verified on disk this cycle)**: `book/src/L1/dot.md:100` (`firm`), `book/src/L1/apply_linop.md:87` (`firm`), `book/src/L1/matrix-weighted-norm.md:110` (`firm`, promoted c091). `rank(bilinear-form) = 3 ≤ min(3,3,3)` — the HARD-gate-new rank invariant holds.
- **L0 structural anchors** (restated, not re-cited — already in the `verified_against:` block): `palace/linalg/operator.hpp:385-394`, `palace/linalg/operator.cpp:621-639`, `palace/models/boundarymodeoperator.cpp:85` (Hermitian `Bttr`), `:90` (non-Hermitian `Atn`). `citecheck --anchor 'Dot'` on `palace/linalg/operator.cpp:621-639` returns `[ok]` (anchor at 621/628/631/637 within range).
- **Count verification**: `book/src/L1/index.md:31` reads "31 main cohort; 38 firm grand total" on disk → flip yields 32 main / 39 grand (matches the planner estimate).
- **SUMMARY**: `bilinear-form` already at `book/src/SUMMARY.md:176` — no edit (flip, not new chapter).

## Open questions / caveats

- **`verified_against:` block left untouched.** The c092 DISCHARGE block (`:473-511`) is the firm evidence; I did not edit it (its verdicts and audit timestamps are the discharge record). The flip restates the §Status conclusion *around* it as ENACTED; the block itself stays as authored c092.
- **HARD-gate-new first exercise — `edges:` grammar choice.** I used the bare-string `depends-on:` form (scheme §2, bare ≡ `{target}` no kind). I did NOT add a documentation `kind:` to any edge (the linters ignore it; none was load-bearing to record). If the batch-30 meta-phase wants `kind: folds` annotations on the `dot`/`apply_linop` edges and `kind: lowers-to` was expected for the theme reference, note that the theme is a `reference` (navigational), not a `depends-on` lowering edge — per scheme §2 a feature/theme navigational pointer is `reference`. (Scheme §5 says a lowering THEME's own `edges:` lists both endpoints as `depends-on`; that is the THEME's frontmatter, D2/abstractor territory, not this operator's edge to it.)
- **Within-file re-anchor scope.** I re-anchored every conclusion-prose that concluded "rough-in" within `bilinear-form.md`: §Context (`:45-53`), §Dependencies (`:251-257`), §Status opener (`:321-326`), §Status gate-(c) paragraph (`:368-375`), cycle-010 repair-note tail (`:377-387`). The §Semantics / §Algebraic-laws / §Variant-axes / §Applicability / §Evidence / §L1-vs-L0 sections carry no rough-in conclusion (they state the structure and laws, which the flip does not change) — left intact. The §Status escape-bullets (probe points 1-3, `:330-366`) are the discharge argument and are correct as-is (they argue the escape APPLIES); only their framing paragraph (`:368-375`) needed flipping from "stays rough-in by design" to "ENACTED".
- **Count-token in the index enumerated tail.** The `:31` paragraph's long enumerated-operators sentence is edited to insert `bilinear-form` as the 32nd member and update both count tokens; the rest of the enumeration is preserved verbatim. The dep-map cell `:113` and the BLAS-1-alpha-position firm bullet are the per-chapter registrations (mine to write per the index-registration partition); no consolidated tally is deferred (this cycle's count-owner for L1/index IS this dispatch — the planner names D1 as SOLE owner of the L1/index count headers).
- **D2 boundary respected.** I did NOT touch the L1>L0 theme `bilinear-form-mutation-rotation.md` (firm; D2 handles its cross-refs), nor any other consumer file, nor `gram_reduce`/the feature columns/`feature/index.md`. The `reference:` edge in my frontmatter merely *points at* the theme; it does not edit it.
