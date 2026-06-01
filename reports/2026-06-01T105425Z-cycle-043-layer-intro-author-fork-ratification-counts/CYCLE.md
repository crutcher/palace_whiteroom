---
agent: layer-intro-author
invoked_at: 2026-06-01T105425Z
scope: cycle-043 D2 — L2-index fork-ratification (batch-12 meta decisions 1+3) + SOLE consolidated-tally owner (L2/index + L2-L1/index + L3-L2/index)
status: pending
inputs:
  - book/src/L2/index.md
  - book/src/L2-L1/index.md
  - book/src/L3-L2/index.md
  - reports/2026-06-01T105425Z-cycle-planner-cycle-043/CYCLE.md
  - reports/2026-06-01T105425Z-cycle-043-lifter-consolidated-sweep/CYCLE.md (D1 — three renames; net-zero on counts; C8 co-touches L2/index lines 106/108 — DISJOINT from my edits)
  - reports/2026-06-01T105425Z-cycle-043-harvester-L2-{axpy,axpby,axpbypcz,normalize}/CYCLE.md (the 4 floors I count)
integrated_at: 2026-06-01T140000Z
integration_commit: 3f9a7d0
integration_notes: "cycle-043 batch integration (cohort-completing L2-floor build); D2 fork-ratification + SOLE count-owner (leaf-vs-fold fork flipped provisional->RATIFIED keep-(b) in all 3 indexes; L2 17->21, L2>L1 15->19, L3>L2 10->14); applied clean; see reports/2026-06-01T140000Z-integrator-finalize-cycle-43/CYCLE.md + cycle-043 STAGING row."
---

# CYCLE: L2 fork-ratification + cycle-043 consolidated index counts

## Summary

TWO jobs this dispatch (cycle-043 D2, wave-3, sole count-owner):

**(a) Fork-ratification** — enact batch-12 meta-phase **decisions 1 + 3** into `book/src/L2/index.md`:
the batch-12 meta-phase RATIFIED the leaf-vs-fold fork (`dot-l2-leaf-floor-vs-fold-only-design`)
in favour of **keeping the leaf-floor reading (b)** cohort-wide (per the c042 cross-cutter audit
recommendation). I flip every "under batch-12 meta-phase adjudication" / "recommendation, not an
enactment" passage to **RATIFIED (keep leaf-floor (b)), batch-12 meta-phase**, add the one-line
fold-cohort-boundary generalization, record the `nrm2` consumer-not-member carve-out, and rename the
"Identity-in-form BLAS-1 floors" cohort heading **cohort-neutrally** to reflect
`l2-floor-under-l3-leaf-cohort` (decision 3 — the cohort now spans non-BLAS-1 members: the cycle-043
`axpy`-family fold-parented leaves + the fused-composite `normalize`).

**(b) SOLE consolidated-tally owner** — author the three index tallies accounting for ALL cycle-043
landings (D1's renames + D3/D4/D5/D9 floors + D6/D7/D8/D10 themes). I run LAST (wave-3) so the
counts reflect the landed cohort. Verified on-disk baselines (Phase-2 enumeration of each index's
dep-map / theme-list rows, NOT the cycle log):

| index | on-disk baseline (rows) | after cycle-043 |
|---|---|---|
| `L2/index.md` dep-map | 17 firm + 1 partly-constructive (18 rows) | **21 firm + 1 partly-constructive (22 rows)** |
| `L2-L1/index.md` theme-list | 15 firm + 1 partly-constructive (16 rows) | **19 firm + 1 partly-constructive (20 rows)** |
| `L3-L2/index.md` theme-list | 10 firm (10 rows) | **14 firm (14 rows)** = `l3-l2-rotation-theme-coverage-gap` **14-of-18** |

The four cycle-043 floors split into **two sub-shapes**: `axpy`/`axpby`/`axpbypcz` are **fold-PARENTED**
arity-2/2/3 leaves of `linear_combination` (the same shape as the cycle-041 `scal` arity-1 floor, now
under the RATIFIED (b) reading); `normalize` is a **NEW thin-identity sub-shape** — a *fused composite*
`nrm2 ∘ scal` that, like `nrm2`, is a consumer-not-member with **NO fold-parent**
(fork-INDEPENDENT / design-final). D1's three slug renames (`nrm2-fold-specialization`→
`nrm2-leaf-identity`, `scal-fold-specialization`→`scal-leaf-identity` in L2-L1;
`elementwise_product-body-identity`→`elementwise-product-body-identity` in L3-L2) are **net-zero on
counts** but I reflect the new slug names in my cohort narratives.

**Disjointness with D1.** D1's C8 edits L2/index.md lines 106 (cycle-041-cohort note) and 108
(slug-naming note). My L2/index.md edits touch lines 28, 45, the §"Fold-cohort boundary" working note,
the §Vocabulary-cohort, the dep-map, line 105 (cycle-042-cohort tally — I append a cycle-043 sibling
note, I do NOT rewrite 105/106), and line 107 (the fork-signal bullet). **No shared line.** D1 also
edits L2-L1/index.md (rename rows/notes) and L3-L2/index.md (rename row/notes) — my count edits there
touch the **§Vocabulary-cohort headers and §Working-Notes cohort-growth-log**, disjoint from D1's
per-slug rename lines (by-slug matching serializes cleanly per the c041/c042 precedent). Since I run
LAST, my counts presuppose D1's renames already landed.

**Write mode.** Per `.claude/agents/layer-intro-author.md` §Discipline (first bullet) I am a
DISPATCH-phase agent: I emit proposed-changes blocks below; `integrator-per-report` applies them in
Phase 5. I do NOT mutate `book/` myself.

---

## Proposed changes

### (a) Fork-ratification + cohort-neutral rename in `book/src/L2/index.md`

#### E1 — §Semantics, fold-parented-floors bullet (line 28): flip adjudication → RATIFIED

```edit:book/src/L2/index.md
[old]:   - **Fold-parented floors** (cycle-041; `dot`, `nrm2`, `scal`) — same-named leaves of the L2 fold-parents `inner_product` / `linear_combination`: `dot` is the conjugation-axis *leaf-of* `inner_product` (NOT merged); `scal` is the arity-1 *member-of* `linear_combination` (NOT merged); `nrm2` is a *consumer-of* `inner_product` (`√ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member; the `std::abs` guard preserved as an explicit algebraic claim). The do-NOT-merge boundary (§"Fold-cohort boundary") is load-bearing for all three. **Their leaf-vs-fold realization is under batch-12 meta-phase adjudication** (`dot-l2-leaf-floor-vs-fold-only-design`; see §Working Notes — the c042 cross-cutter audit recommends ratifying the leaf-floor reading (b)).
[new]:   - **Fold-parented floors** (cycle-041 `dot`/`nrm2`/`scal` + cycle-043 `axpy`/`axpby`/`axpbypcz`) — same-named leaves of the L2 fold-parents `inner_product` / `linear_combination`: `dot` is the conjugation-axis *leaf-of* `inner_product` (NOT merged); `scal`/`axpy`/`axpby`/`axpbypcz` are the arity-1/2/2/3 *members-of* `linear_combination` (NOT merged); `nrm2` is a *consumer-of* `inner_product` (`√ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member; the `std::abs` guard preserved as an explicit algebraic claim). The do-NOT-merge boundary (§"Fold-cohort boundary") is load-bearing for all of them. **Their leaf-vs-fold realization is RATIFIED (keep leaf-floor (b)), batch-12 meta-phase** (`dot-l2-leaf-floor-vs-fold-only-design`; see §Working Notes — the c042 cross-cutter audit recommendation was adopted: each firm L3 leaf gets a same-named L2 floor cited as leaf-of / member-of the fold, deferring all fusion content to the fold-parent). The fork could only ever re-anchor a *fold-parented* leaf, so it governs this sub-cohort alone; the `nrm2` carve-out is **fork-invariant on membership** (it consumes the `inner_product` fold either way).
```

#### E2 — §Vocabulary-cohort, "Identity-in-form BLAS-1 floors" heading (line 45): cohort-neutral rename + flip adjudication + add axpy-family + nrm2 carve-out

```edit:book/src/L2/index.md
[old]: *Identity-in-form BLAS-1 floors (cycle-041; FOLD-PARENTED — present so the firm L3 cohort rests on adjacent same-named L2 parents; distinct from the fold-parents — do-NOT-merge; **leaf-vs-fold realization under batch-12 meta-phase adjudication**):*

- `dot` — conjugation-axis **leaf-of** `inner_product` (the plain `M = I` Hermitian / symmetric member); thin identity-in-form floor, laws inherited unchanged from the L1 leaf. Firm cycle-041 (D1).
- `nrm2` — **consumer-of** `inner_product` (`√ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member); the `std::abs` defensive guard preserved as an explicit load-bearing numerical claim. Firm cycle-041 (D2).
- `scal` — arity-1 **member-of** `linear_combination` (`scal(α,x) = linear_combination [(α,x)]`, NOT merged); firm-on-positive-structure (syntactic-identity laws on the small fully-present `operator*=` surface). Firm cycle-041 (D3).
[new]: *Identity-in-form leaf-cohort floors (`l2-floor-under-l3-leaf-cohort`; FOLD-PARENTED sub-cohort — present so the firm L3 cohort rests on adjacent same-named L2 parents; distinct from the fold-parents — do-NOT-merge; **leaf-vs-fold realization RATIFIED (keep leaf-floor (b)), batch-12 meta-phase**). The cohort heading is cohort-neutral (decision 3): the cohort spans the BLAS-1 leaves AND the cycle-043 arity-family additions, all members-of / consumers-of a fold-parent:*

- `dot` — conjugation-axis **leaf-of** `inner_product` (the plain `M = I` Hermitian / symmetric member); thin identity-in-form floor, laws inherited unchanged from the L1 leaf. Firm cycle-041 (D1).
- `nrm2` — **consumer-of** `inner_product` (`√ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member); the `std::abs` defensive guard preserved as an explicit load-bearing numerical claim. **Carve-out: fork-invariant on membership** — `nrm2` consumes the `inner_product` fold either way, so the leaf-vs-fold ratification does not touch its consumer relationship; only its *floor* rides the `l2-floor-under-l3-leaf-cohort` decision. Firm cycle-041 (D2).
- `scal` — arity-1 **member-of** `linear_combination` (`scal(α,x) = linear_combination [(α,x)]`, NOT merged); firm-on-positive-structure (syntactic-identity laws on the small fully-present `operator*=` surface). Firm cycle-041 (D3).
- `axpy` — arity-2 **member-of** `linear_combination` (`axpy(α,x,y) = linear_combination [(α,x),(1,y)]`, second coefficient fixed to 1, NOT merged); thin identity-in-form floor; the output-aliasing variant axis is the **fold's**, not leaf-specific. Firm cycle-043 (D3).
- `axpby` — arity-2 **member-of** `linear_combination` (`axpby(α,x,β,y) = linear_combination [(α,x),(β,y)]`, NOT merged); thin identity-in-form floor; output-aliasing axis is the fold's. Firm cycle-043 (D4).
- `axpbypcz` — arity-3 **member-of** `linear_combination` (`axpbypcz(α,x,β,y,γ,z) = linear_combination [(α,x),(β,y),(γ,z)]`, NOT merged); thin identity-in-form floor; output-aliasing axis is the fold's. Firm cycle-043 (D5).

*Fused-composite floor (cycle-043; a NEW thin-identity sub-shape — fork-INDEPENDENT on membership like `nrm2`, but a composite-with-no-fold-parent rather than a single leaf):*

- `normalize` — the fused vector-normalisation composite `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`, returning **both** the norm and the unit vector. **NO fold-parent** — neither a member of `inner_product` (its codomain is the unit `Tensor[N]` alongside the norm `Scalar`, not a bare `Scalar`) nor of `linear_combination` (the fused norm-then-rescale pairing is not a term-axis scalar-weighted-sum). Cites the same-layer L2 `nrm2` + `scal` floors as *consumed* constituents (NOT a fold of which it is a member). Thin / identity-in-form (no genuine kernel fusion to unfold — `linalg::Normalize` is already the one-line norm-then-rescale composition); the partiality non-law at `x=0` and the IEEE-754 reduction-tree caveats transport unchanged. **Fork-invariant / design-final** — the leaf-vs-fold fork can only re-anchor a fold-parented *leaf*, and `normalize` has no fold to fold into. Firm cycle-043 (D9).
```

#### E3 — §Vocabulary-cohort: append the cycle-042 standalone-floor cohort note's fork status (line 51 stays as-is — it is already correct: "design-final … the leaf-vs-fold fork cannot reach it"). No edit needed there. (Recorded for the critic: the cycle-042 standalone bullet at line 51 already reads design-final and needs no flip.)

#### E4 — §"Fold-cohort boundary" working note (line 100): add the one-line generalization (decision 1)

```edit:book/src/L2/index.md
[old]: - **Fold-cohort boundary (load-bearing, do NOT merge).** `inner_product` (cycle-019) and `linear_combination` (cycle-018) share a `foldl` skeleton but are distinct homomorphisms targeting different codomains: `inner_product` folds the **length axis** to `Scalar`; `linear_combination` folds the **term axis**, keeping `Tensor[N]`. The do-NOT-merge note is carried in both dep-map rows and in each entry's §"Sibling fold". `nrm2` / `matrix-weighted-norm` is a *consumer* of `inner_product` (`√ ∘ inner_product` at `y=x`), not an instance.
[new]: - **Fold-cohort boundary (load-bearing, do NOT merge).** `inner_product` (cycle-019) and `linear_combination` (cycle-018) share a `foldl` skeleton but are distinct homomorphisms targeting different codomains: `inner_product` folds the **length axis** to `Scalar`; `linear_combination` folds the **term axis**, keeping `Tensor[N]`. The do-NOT-merge note is carried in both dep-map rows and in each entry's §"Sibling fold". `nrm2` / `matrix-weighted-norm` is a *consumer* of `inner_product` (`√ ∘ inner_product` at `y=x`), not an instance.
  - **Leaf-floor generalization (RATIFIED, batch-12 meta-phase, decision 1).** Each firm L3 leaf gets a same-named L2 floor (the "both L levels" invariant); the floor is cited as leaf-of / consumer-of / member-of the relevant fold and defers all fusion content to the fold-parent — a layer-coherence pointer, not a rival fold. This is the cohort-wide rule the batch-12 meta-phase ratified (keeping leaf-floor (b) over the fold-only (a) reading); it covers the held `axpy`/`axpby`/`axpbypcz` arity floors (landed cycle-043) so they do not re-litigate the leaf-vs-fold question, and the `nrm2` consumer carve-out (fork-invariant on membership — it consumes the fold either way). The do-NOT-merge boundary above is what makes the floor a *pointer* rather than a duplicate of the fold.
```

#### E5 — §Working-Notes line-107 fork-signal bullet: flip to RATIFIED

```edit:book/src/L2/index.md
[old]:   - **LOAD-BEARING META-PHASE SIGNAL — leaf-vs-fold design fork (`dot-l2-leaf-floor-vs-fold-only-design`; for the batch-12 meta-phase, post-c042; the c042 cross-cutter audit recommends KEEPING leaf-floor (b)).** Wave-1 (cycle-041) surfaced a **contradiction between two co-dispatched harvesters**: D1 built `L2/dot` as a same-named conjugation-axis **leaf floor** of `inner_product` (the **(b)** realization — a standalone `dot` chapter, cited as leaf-of, not merged); D2 argued the opposite — that the L2 inner-product surface should be **ONLY** the `inner_product` fold, with **NO `dot` leaf at L2** (the **(a) fold-only** reading), flagging the per-leaf L2 floor as arguably redundant with the fold-cohort vocabulary. **All six cycle-041 entries (the three floors + their six themes) presuppose the (b) "same-named floor" realization.** The batch-12 meta-phase must **ratify or adjust** this design before the cohort is treated as stable. **The cycle-042 cross-cutter leaf-vs-fold audit (`reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/`) recommends KEEPING the leaf-floor reading (b) and ratifying it cohort-wide**: the +files are thin pointers (≤220 ln, identity-in-form, all fusion content deferred to the fold-parent) below the duplication-explosion threshold; the leaf is a genuinely-distinct dual of the fold on the *layer-coherence* axis (the firm L3 `dot`/`scal` leaves already exist and the "both L levels" invariant compels a same-named L2 parent); and it is the consistent extension of the already-accepted L1 `axpby-as-primitive` "keep leaves firm, fuse don't decompose" decision. The audit further finds the D1-vs-D2 disagreement is **narrower than "contradiction"** — D2 never authored a fold-only `dot`, it declined to author a leaf; the live question is the narrow one "does a firm L3 leaf compel a same-named L2 floor?" (audit answer: YES per invariant). It recommends a one-line generalization into §"Fold-cohort boundary" so the held `axpy`-family arity floors don't re-litigate, and an explicit `nrm2` carve-out (consumer-not-member, fork-invariant on membership). The decision remains the **batch-12 meta-phase's to make** — this is a recommendation, not an enactment. *Were the meta-phase to instead adopt the (a) fold-only reading* (against the audit's recommendation), the leaf floors (`dot` certainly; `scal` as the arity-1 member; `nrm2` is unaffected on the fold question since it consumes the fold either way, but its L2 *floor* rides the same `l2-floor-under-l3-blas1-cohort` decision) and their adjacent themes would **re-anchor to the fold-parents**: the L2>L1 leaf-identity edges fold into `inner-product-fold-specialization` / `linear-combination-fold-specialization`, and the L3>L2 body-identity edges re-point their L2 RHS from a same-named leaf to the fold-parent. This (a)-branch consequence is upstream of the whole cohort; surfaced here in the L2 Part overview so a reader navigating the floor cohort sees the design is provisional until ratified. (Recorded by D1/D2/D4/D5/D6 in their §Open-questions; consolidated as the batch-12 meta-phase OQ.) **Note: this fork governs ONLY the cycle-041 fold-parented floors; the cycle-042 standalone-floor cohort (`reciprocal`/`elementwise_product`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`) is fork-INDEPENDENT and design-final — having no fold-parent, none can be re-anchored into a fold whatever the meta-phase decides.**
[new]:   - **RESOLVED META-PHASE SIGNAL — leaf-vs-fold design fork RATIFIED (`dot-l2-leaf-floor-vs-fold-only-design`; batch-12 meta-phase, decisions 1+3; the c042 cross-cutter audit recommendation was ADOPTED — keep leaf-floor (b)).** Wave-1 (cycle-041) surfaced a design question between two co-dispatched harvesters: D1 built `L2/dot` as a same-named conjugation-axis **leaf floor** of `inner_product` (the **(b)** realization — a standalone `dot` chapter, cited as leaf-of, not merged); D2 argued the L2 inner-product surface should be **ONLY** the `inner_product` fold, with **NO `dot` leaf at L2** (the **(a) fold-only** reading). **The batch-12 meta-phase RATIFIED the (b) leaf-floor reading cohort-wide** (decision 1), adopting the c042 cross-cutter audit (`reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/`): the +files are thin pointers (≤220 ln, identity-in-form, all fusion content deferred to the fold-parent) below the duplication-explosion threshold; the leaf is a genuinely-distinct dual of the fold on the *layer-coherence* axis (the firm L3 `dot`/`scal` leaves already exist and the "both L levels" invariant compels a same-named L2 parent); and it is the consistent extension of the already-accepted L1 `axpby-as-primitive` "keep leaves firm, fuse don't decompose" decision. The audit found the D1-vs-D2 disagreement was **narrower than "contradiction"** — D2 never authored a fold-only `dot`, it declined to author a leaf; the live question was the narrow one "does a firm L3 leaf compel a same-named L2 floor?" (ratified answer: YES per invariant). Two follow-ups landed with the ratification: (i) the one-line **leaf-floor generalization** into §"Fold-cohort boundary" (above) so the held `axpy`-family arity floors (landed cycle-043 as arity-2/2/3 members of `linear_combination`) do not re-litigate; (ii) the explicit `nrm2` **carve-out** (consumer-not-member, fork-invariant on membership). Decision 3 renamed the cohort heading cohort-neutrally (`l2-floor-under-l3-leaf-cohort`) since the cohort now spans the BLAS-1 leaves + the cycle-043 arity-family + the fused-composite `normalize`. **This fork governed ONLY the fold-parented floors; the cycle-042 standalone-floor cohort (`reciprocal`/`elementwise_product`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`) and the cycle-043 fused-composite `normalize` are fork-INDEPENDENT and design-final — having no fold-parent, none could be re-anchored into a fold whatever the meta-phase decided.** The (a)-branch consequence (themes re-anchoring to fold-parents) is now moot — the cohort is stable under (b). (Originally recorded by the cycle-041 D1/D2/D4/D5/D6 §Open-questions; consolidated + adjudicated as the batch-12 meta-phase OQ.)
```

### (b) Consolidated dep-map rows + tally + cohort narrative in `book/src/L2/index.md`

#### E6 — append 4 floor rows to the §Operator dep-map (after the `eigsolve` row, line 84)

```edit:book/src/L2/index.md
[old]: | [`eigsolve`](./eigsolve.md) | `(E: EigSolver[problem], control: EigControl) -> EigResult[N, K_max]` (per-step body ≡ named shift-invert composition `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)`; the eigen-iteration fold is opaque-library-owned, named by role) | **Named composition — shift-invert spectral-transform application** (the per-step body the opaque library eigen-iteration folds). **Direct L2 dep:** [`ksp_solve`](./ksp_solve.md) (the inner solve inverting the shifted operator `(K − σM)` — first L2 named composition whose direct constituent is itself a constructed-solver composition). Cross-layer constituents: [`apply_linop`](../L1/apply_linop.md) (L1; the `M`/PEP-block operand apply), `apply_nonlinear_pencil` (L1; the NEP operand). Concepts: `constructed-operators`, `solver-as-operator`, `variant-absorption`, `sequential-obstruction` (the library loop), `solve-monad`, `apply_BA`. **Opens the per-step-application half of the L1 opacity; the eigen-iteration loop stays a role reference** (library-owned: SLEPc `EPSSolve` / ARPACK RCI — no Palace-authored eigen-step kernel/driver pair, the inverse decomposition from `ksp_solve` which opens the loop). Establishes a **non-identity** L2↔L1 rotation (partial un-collapse). L0 anchors: ARPACK explicit `arpack.cpp:562-590`, SLEPc ST-shell `slepc.cpp:1847-1877` + `:1801-1827`, shift-invert setup `slepc.cpp:379-394`. | `firm` (harvested cycle-023 wave-1; chain-step-2 of the eigsolve prerequisite chain L1→L2→L3; composition-identity laws are syntactic identities on positive `ApplyOp`/`__pc_apply_EPS` source + fold-terminal restatements of firm L1 laws; firm-on-positive-structure per the `ksp_solve` / `apply_nonlinear_pencil` precedents. Predicts the L3 backfill lands `partial-obstruction` — body lifts, opaque-library loop does not.) |
[new]: | [`eigsolve`](./eigsolve.md) | `(E: EigSolver[problem], control: EigControl) -> EigResult[N, K_max]` (per-step body ≡ named shift-invert composition `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)`; the eigen-iteration fold is opaque-library-owned, named by role) | **Named composition — shift-invert spectral-transform application** (the per-step body the opaque library eigen-iteration folds). **Direct L2 dep:** [`ksp_solve`](./ksp_solve.md) (the inner solve inverting the shifted operator `(K − σM)` — first L2 named composition whose direct constituent is itself a constructed-solver composition). Cross-layer constituents: [`apply_linop`](../L1/apply_linop.md) (L1; the `M`/PEP-block operand apply), `apply_nonlinear_pencil` (L1; the NEP operand). Concepts: `constructed-operators`, `solver-as-operator`, `variant-absorption`, `sequential-obstruction` (the library loop), `solve-monad`, `apply_BA`. **Opens the per-step-application half of the L1 opacity; the eigen-iteration loop stays a role reference** (library-owned: SLEPc `EPSSolve` / ARPACK RCI — no Palace-authored eigen-step kernel/driver pair, the inverse decomposition from `ksp_solve` which opens the loop). Establishes a **non-identity** L2↔L1 rotation (partial un-collapse). L0 anchors: ARPACK explicit `arpack.cpp:562-590`, SLEPc ST-shell `slepc.cpp:1847-1877` + `:1801-1827`, shift-invert setup `slepc.cpp:379-394`. | `firm` (harvested cycle-023 wave-1; chain-step-2 of the eigsolve prerequisite chain L1→L2→L3; composition-identity laws are syntactic identities on positive `ApplyOp`/`__pc_apply_EPS` source + fold-terminal restatements of firm L1 laws; firm-on-positive-structure per the `ksp_solve` / `apply_nonlinear_pencil` precedents. Predicts the L3 backfill lands `partial-obstruction` — body lifts, opaque-library loop does not.) |
| [`axpy`](./axpy.md) | `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` (`α, x, y → α·x + y`) | **Arity-2 leaf of [`linear_combination`](./linear_combination.md) (cited, NOT merged — fold-cohort boundary load-bearing; second coefficient fixed to 1: `axpy(α,x,y) = linear_combination [(α,x),(1,y)]`).** Leaf primitive (no L2 constituents; sub-operations below L2 resolution). Fold-parent: `linear_combination`. The **output-aliasing variant axis is the FOLD's, not leaf-specific** (OQ `arity-family-leaf-floors-output-aliasing-axis-is-the-folds`). Concepts: [`scalar-promotion`](../concepts/scalar-promotion.md). L1 anchor: [`axpy`](../L1/axpy.md) (firm); identity-in-form rotation (whole-tensor in/out at both layers; no kernel fusion to unfold). | `firm` (harvested cycle-043 D3; L2 floor backfill under foundation-first directive `l2-floor-under-l3-leaf-cohort`; identity-lowering per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — floors the firm L3 [`axpy`](../L3/axpy.md), cycle-011; firm-on-positive-structure — syntactic-identity laws on the small fully-present `AXPY` free-function + `ComplexVector::AXPY` surface; leaf-floor (b) RATIFIED batch-12 meta-phase) |
| [`axpby`](./axpby.md) | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (`α, x, β, y → α·x + β·y`) | **Arity-2 leaf of [`linear_combination`](./linear_combination.md) (cited, NOT merged — `axpby(α,x,β,y) = linear_combination [(α,x),(β,y)]`).** Leaf primitive (no L2 constituents). Fold-parent: `linear_combination`. The output-aliasing variant axis is the FOLD's, not leaf-specific. Concepts: [`scalar-promotion`](../concepts/scalar-promotion.md). Sibling-subsumes `scal` (β=0) and `axpy` (β=1). L1 anchor: [`axpby`](../L1/axpby.md) (firm); identity-in-form rotation. | `firm` (harvested cycle-043 D4; L2 floor backfill under `l2-floor-under-l3-leaf-cohort`; identity-lowering — floors the firm L3 [`axpby`](../L3/axpby.md), cycle-011; firm-on-positive-structure on the three positive Palace entry points; leaf-floor (b) RATIFIED batch-12 meta-phase) |
| [`axpbypcz`](./axpbypcz.md) | `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (`α, x, β, y, γ, z → α·x + β·y + γ·z`) | **Arity-3 leaf of [`linear_combination`](./linear_combination.md) (cited, NOT merged — `axpbypcz(...) = linear_combination [(α,x),(β,y),(γ,z)]`).** Leaf primitive (no L2 constituents). Fold-parent: `linear_combination`. The output-aliasing variant axis is the FOLD's, not leaf-specific. Concepts: [`scalar-promotion`](../concepts/scalar-promotion.md). L1 anchor: [`axpbypcz`](../L1/axpbypcz.md) (firm); identity-in-form rotation. | `firm` (harvested cycle-043 D5; L2 floor backfill under `l2-floor-under-l3-leaf-cohort`; identity-lowering — floors the firm L3 [`axpbypcz`](../L3/axpbypcz.md), cycle-011; firm-on-positive-structure on the three positive Palace entry points; leaf-floor (b) RATIFIED batch-12 meta-phase) |
| [`normalize`](./normalize.md) | `normalize :: Tensor[N] -> { norm: Scalar, unit: Tensor[N] }` (≡ `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`; partial — defined where `‖x‖₂ > 0`; the returned norm is load-bearing) | **Fused composite over two same-layer floors — fork-INDEPENDENT, NO fold-parent.** Consumes: L2 [`nrm2`](./nrm2.md) (the norm reduction `β = √ ∘ abs ∘ inner_product` at `y=x`; supplies the reduction-tree non-associativity + `std::abs` guard) + L2 [`scal`](./scal.md) (the rescale `û = scal(1/β, x)`). NOT a fold member — neither reduce-to-`Scalar` ([`inner_product`](./inner_product.md): its codomain is the unit `Tensor[N]` alongside `β`) nor reduce-to-`Tensor[N]` ([`linear_combination`](./linear_combination.md): the fused norm-then-rescale pairing is not a term-axis scalar-weighted-sum). No genuine kernel fusion to unfold (`linalg::Normalize` is already the one-line norm-then-rescale composition); the fusion-rotation framing is the single-evaluation `nrm2 ∘ scal` pairing. Partiality non-law at `x=0` preserved as a precondition. Variant axis: element-type (real/complex; norm output always real). Consumers: [`krylov-step`](./krylov-step.md) (GMRES Arnoldi basis-normalisation — the returned norm becomes the Hessenberg sub-diagonal), [`orthogonalize`](./orthogonalize.md) (Gram-Schmidt output-normalisation). | `firm` (harvested cycle-043 D9; L2 fusion-rotation floor — the LAST genuine missing floor under `l2-floor-under-l3-leaf-cohort`; identity-lowering per **Identity-lowerings still require both L levels** — floors the firm L3 [`normalize`](../L3/normalize.md), cycle-039; **NEW thin-identity sub-shape — fused-composite-no-fold-parent**, fork-INDEPENDENT / design-final on the leaf-vs-fold fork like `nrm2`'s consumer relationship; firm-on-positive-structure — laws transported from the firm L1 leaf on the positive `linalg::Normalize` surface `vector.hpp:262-270`) |
```

#### E7 — append the cycle-043 cohort-growth tally to §Working-Notes (after line 105, the cycle-042 cohort note)

```edit:book/src/L2/index.md
[old]:   The companion adjacent thin-identity themes landed the same cycle (L2>L1 `-leaf-identity` ×5; L3>L2 `-body-identity` ×5, advancing `l3-l2-rotation-theme-coverage-gap` 5-of-18 → 10-of-18).
[new]:   The companion adjacent thin-identity themes landed the same cycle (L2>L1 `-leaf-identity` ×5; L3>L2 `-body-identity` ×5, advancing `l3-l2-rotation-theme-coverage-gap` 5-of-18 → 10-of-18).
- **Cycle-043 leaf-cohort floor batch (firm 17 → 21; the fork-RATIFICATION cycle).** Four `firm` floors landed under the now-cohort-neutral `l2-floor-under-l3-leaf-cohort` directive (renamed this cycle, decision 3), raising the firm L2 cohort **17 → 21** (partly-constructive `deflate` unchanged at 1; **dep-map now 22 rows = 21 firm + 1 partly-constructive**). The batch splits into **two sub-shapes**: (i) the **fold-PARENTED** arity-family leaves of `linear_combination` — [`axpy`](./axpy.md) (D3, arity-2, second coeff fixed to 1), [`axpby`](./axpby.md) (D4, arity-2), [`axpbypcz`](./axpbypcz.md) (D5, arity-3) — each cited as a member NOT merged, the output-aliasing variant axis belonging to the **fold** not the leaf; these are the held `axpy`-family floors UNBLOCKED by the batch-12 meta-phase ratification of the (b) leaf-floor reading (the same shape as the cycle-041 `scal` arity-1 floor). (ii) a **NEW thin-identity sub-shape** — [`normalize`](./normalize.md) (D9), the fused composite `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` returning both the norm and the unit vector; it is **fork-INDEPENDENT on membership** like `nrm2` (a consumer-not-member with NO fold-parent), but on a different basis — a *composite-with-no-fold-parent* rather than a standalone single leaf, so it is design-final regardless of the leaf-vs-fold fork. This closes the `l2-floor-under-l3-leaf-cohort` to **12-of-13** present (the 13th, `chebyshev`, already-floored via the firm `chebyshev-iteration` — see the chebyshev-reconciliation note below). The companion adjacent thin-identity themes landed the same cycle (L2>L1 `-leaf-identity` ×4 → firm 15 → 19; L3>L2 `-body-identity` ×4 → firm 10 → 14, advancing `l3-l2-rotation-theme-coverage-gap` 10-of-18 → **14-of-18**). The cycle-043 D1 lifter sweep also renamed three slugs (`nrm2-fold-specialization`→`nrm2-leaf-identity`, `scal-fold-specialization`→`scal-leaf-identity` in L2-L1; `elementwise_product-body-identity`→`elementwise-product-body-identity` in L3-L2) — net-zero on counts, reflected in the cohort narratives.
- **FOR THE BATCH-13 META-PHASE — `chebyshev` floor-cohort count reconciliation.** The `l2-floor-under-l3-leaf-cohort` denominator is "13" and lists `chebyshev` as a missing floor, but the cycle-043 deliverable-presence check found `chebyshev`'s L2 floor is **already present** as the firm [`chebyshev-iteration`](./chebyshev-iteration.md) (cycle-012; `L3/chebyshev` lowers to it). The cohort is therefore **12-of-13 present**, with the 13th (`chebyshev`) **already-floored under a non-same-named slug** — a soft inconsistency between the "same-named L2 floor" convention (ratified decision 1) and the pre-existing `chebyshev-iteration` naming. The cycle-043 planner recommends **count-correction-to-12 + naming-exception** (a same-named `L2/chebyshev.md` pointer to the existing substantive floor would be pure naming bureaucracy with zero coherence gain — the L3 reader already finds `chebyshev` floored). **Routed to the batch-13 meta-phase for ratification**; not actionable as a dispatch.
- **FOR THE BATCH-13 META-PHASE — `normalize` introduced a NEW thin-identity sub-shape (`fused-composite-no-fold-parent`).** Prior thin-identity floors were either fold-parented single leaves (cycle-041 `dot`/`scal` + cycle-043 `axpy`-family) or standalone single leaves/gates with no fold-parent (cycle-042 cohort + `nrm2`-as-consumer). `normalize` is the first floor that is a *fused composite of two same-layer floors* (`nrm2 ∘ scal`) with NO fold-parent — fork-INDEPENDENT/design-final on a distinct basis (composite, not leaf). Surfaced so the batch-13 meta-phase can decide whether the cohort-classification vocabulary should name this sub-shape explicitly (it currently reads as a third bullet under the §Vocabulary-cohort split).
```

#### E7b — (repairer) sweep surviving `l2-floor-under-l3-blas1-cohort` → `l2-floor-under-l3-leaf-cohort` directive-slug occurrences in `book/src/L2/index.md`

Appended by the repairer (cycle-043 critique Issue 1, cross-reference-integrity warning): decision 3 renamed the directive cohort-neutrally, but E1/E2/E5/E7 swept only the heading + line-107 fork-signal bullet, leaving 9 on-disk references to the OLD slug in this same file (§Semantics line 27, dep-map status-cells for `scal`/`dot`/`nrm2`/`reciprocal`/`elementwise_product`/`assemble-diagonal`, and working-notes lines 105/106). Mechanical slug-rename only — each `[old]` is a unique full-substring span, `[new]` differs only in the slug token. Disjoint from E7 (E7 anchors the trailing "The companion adjacent…" sentence of line 105; this sweeps the slug nearer the start of line 105 — non-overlapping substrings on the same line, both string-replaces resolve regardless of order). NOTE: residual occurrences in `scaffolding/priorities.md` / `roadmap.md` / `friction-ledger.md` are OUT of book/ scope and routed to a follow-up OQ (meta-phase owns the plan), NOT edited here.

```edit:book/src/L2/index.md
[old]: **), under the 2026-05-31 foundation-first directive `l2-floor-under-l3-blas1-cohort`. Each is value-thread-isomorphic
[new]: **), under the 2026-05-31 foundation-first directive `l2-floor-under-l3-leaf-cohort`. Each is value-thread-isomorphic
```

```edit:book/src/L2/index.md
[old]: D3; L2 floor backfill under foundation-first directive `l2-floor-under-l3-blas1-cohort`; identity-lowering per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — floors the firm L3 [`scal`](../L3/scal.md)
[new]: D3; L2 floor backfill under foundation-first directive `l2-floor-under-l3-leaf-cohort`; identity-lowering per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — floors the firm L3 [`scal`](../L3/scal.md)
```

```edit:book/src/L2/index.md
[old]: adjacent same-named L2 parent (foundation-first directive `l2-floor-under-l3-blas1-cohort`). Same-layer deps: none (leaf).
[new]: adjacent same-named L2 parent (foundation-first directive `l2-floor-under-l3-leaf-cohort`). Same-layer deps: none (leaf).
```

```edit:book/src/L2/index.md
[old]: floor under the firm L3 BLAS-1 cohort per the 2026-05-31 `l2-floor-under-l3-blas1-cohort` foundation-first directive;
[new]: floor under the firm L3 BLAS-1 cohort per the 2026-05-31 `l2-floor-under-l3-leaf-cohort` foundation-first directive;
```

```edit:book/src/L2/index.md
[old]: [`reciprocal`](../L3/reciprocal.md) cycle-038, per the `l2-floor-under-l3-blas1-cohort` foundation-first directive;
[new]: [`reciprocal`](../L3/reciprocal.md) cycle-038, per the `l2-floor-under-l3-leaf-cohort` foundation-first directive;
```

```edit:book/src/L2/index.md
[old]: D3; L2 floor backfill under foundation-first directive `l2-floor-under-l3-blas1-cohort`; identity-lowering per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — floors the firm L3 [`elementwise_product`](../L3/elementwise_product.md)
[new]: D3; L2 floor backfill under foundation-first directive `l2-floor-under-l3-leaf-cohort`; identity-lowering per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — floors the firm L3 [`elementwise_product`](../L3/elementwise_product.md)
```

```edit:book/src/L2/index.md
[old]: operator-to-data primitive, foundation-first directive `l2-floor-under-l3-blas1-cohort` extended from the BLAS-1 cohort
[new]: operator-to-data primitive, foundation-first directive `l2-floor-under-l3-leaf-cohort` extended from the BLAS-1 cohort
```

```edit:book/src/L2/index.md
[old]: → 17).** Five `firm` floor entries landed under the `l2-floor-under-l3-blas1-cohort` directive (extended this cycle
[new]: → 17).** Five `firm` floor entries landed under the `l2-floor-under-l3-leaf-cohort` directive (extended this cycle
```

```edit:book/src/L2/index.md
[old]: landed under the 2026-05-31 foundation-first directive `l2-floor-under-l3-blas1-cohort`, raising the firm cohort **9
[new]: landed under the 2026-05-31 foundation-first directive `l2-floor-under-l3-leaf-cohort`, raising the firm cohort **9
```

### (b) Consolidated counts in `book/src/L2-L1/index.md`

I do NOT add the 4 new `-leaf-identity` theme rows (D6/D7/D8/D10 each append their own row + Vocabulary-cohort sub-bullet per the count-ownership convention). I own only the **consolidated tally** in §Vocabulary-cohort intro and the §Working-Notes cohort-growth-log. D1 owns the rename edits (disjoint lines). My edits:

#### E8 — §Working-Notes cohort-growth-log: prepend the cycle-043 entry (after the line-63 most-recent-first head)

```edit:book/src/L2-L1/index.md
[old]: - Cohort growth log (most-recent first): `assemble-diagonal-leaf-identity` + `jacobi-smoother-leaf-identity` + `divfree-projector-leaf-identity` + `reciprocal-leaf-identity` + `elementwise-product-leaf-identity` firm cycle-042 (the **fork-INDEPENDENT standalone-floor-edge cohort**
[new]: - Cohort growth log (most-recent first): `axpy-leaf-identity` + `axpby-leaf-identity` + `axpbypcz-leaf-identity` + `normalize-leaf-identity` firm cycle-043 (the **leaf-cohort floor-edge batch** — the L2>L1 thin-identity edges of the four new same-named L2 floors; firm **15 → 19** = 19 firm + 1 partly-constructive; the `axpy`-family three are fold-PARENTED arity-2/2/3 members of `linear_combination` (UNBLOCKED by the batch-12 leaf-floor (b) ratification — RESOLVED, no longer under the §"Design fork"), `normalize-leaf-identity` is the fused-composite edge with NO fold-parent (design-final like the cycle-042 standalone edges); the cycle-043 D1 lifter sweep also normalized `nrm2-fold-specialization`→`nrm2-leaf-identity` + `scal-fold-specialization`→`scal-leaf-identity` (net-zero on counts) so the whole L2>L1 identity-edge cohort is now uniform `-leaf-identity`); `assemble-diagonal-leaf-identity` + `jacobi-smoother-leaf-identity` + `divfree-projector-leaf-identity` + `reciprocal-leaf-identity` + `elementwise-product-leaf-identity` firm cycle-042 (the **fork-INDEPENDENT standalone-floor-edge cohort**
```

#### E9 — §Working-Notes §"Design fork": flip RATIFIED + note the cycle-043 edges are RESOLVED

```edit:book/src/L2-L1/index.md
[old]: - **Design fork (`dot-l2-leaf-floor-vs-fold-only-design`; load-bearing batch-12 meta-phase signal — governs the cycle-041 cohort ONLY).** The three **cycle-041** floor-edge themes presuppose the **(b) same-named leaf-floor** realization of the L2 BLAS-1 surface (a standalone `dot`/`scal` L2 chapter, cited as leaf-of / member-of the fold-parents but NOT merged; `nrm2` a consumer-of). Wave-1 D2 argued the **(a) fold-only** reading (no `dot` leaf at L2 — the L2 inner-product surface is only the `inner_product` fold). If the meta-phase adopts (a), `dot-leaf-identity` dissolves into `inner-product-fold-specialization`'s conjugation dispatch and `scal-fold-specialization` into `linear-combination-fold-specialization`'s arity-1 row; the `nrm2` edge is unaffected on the fold question (it consumes the fold either way) but its LHS floor rides the same `l2-floor-under-l3-blas1-cohort` decision. **The cycle-042 cross-cutter audit (`reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/`) recommends KEEPING leaf-floor (b)** — the +files are thin pointers below the duplication-explosion threshold, the leaf is genuinely distinct on the layer-coherence axis, and (b) honors the already-firm L3 `dot`/`scal` leaves' "both L levels" demand; it further finds D1-vs-D2 is narrower than "contradiction" (D2 declined to author a leaf, never built a fold-only `dot`). **This fork does NOT reach the cycle-042 standalone-floor edges** (`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`/`reciprocal`/`elementwise-product`) — each has **NO fold-parent**, so there is no fold to dissolve a leaf into; that cohort is design-final regardless of the adjudication. Also flagged: the cycle-041 L2>L1 cohort slug split (`dot-leaf-identity` vs `nrm2`/`scal` `-fold-specialization`) for three structurally-similar identity edges; the cycle-042 cohort used `-leaf-identity` uniformly, making the two cycle-041 `-fold-specialization` slugs the outliers for the meta-phase to normalize.
[new]: - **Design fork RATIFIED (`dot-l2-leaf-floor-vs-fold-only-design`; batch-12 meta-phase, decisions 1+3 — keep leaf-floor (b)).** The cycle-041 floor-edge themes presuppose the **(b) same-named leaf-floor** realization of the L2 surface (a standalone `dot`/`scal` L2 chapter, cited as leaf-of / member-of the fold-parents but NOT merged; `nrm2` a consumer-of). Wave-1 D2 argued the **(a) fold-only** reading; the **batch-12 meta-phase RATIFIED (b)**, adopting the c042 cross-cutter audit (`reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/`): the +files are thin pointers below the duplication-explosion threshold, the leaf is genuinely distinct on the layer-coherence axis, and (b) honors the already-firm L3 leaves' "both L levels" demand; the audit found D1-vs-D2 narrower than "contradiction" (D2 declined to author a leaf, never built a fold-only `dot`). The (a)-branch dissolution (`dot-leaf-identity` → `inner-product-fold-specialization`; `scal-leaf-identity` → `linear-combination-fold-specialization`) is now moot — the cohort is stable under (b). The ratification **UNBLOCKED the cycle-043 `axpy`-family arity floor-edges** (`axpy`/`axpby`/`axpbypcz`-`leaf-identity`, the arity-2/2/3 members of `linear_combination`), which land under the same (b) reading and need not re-litigate (the leaf-floor generalization is recorded in `book/src/L2/index.md` §"Fold-cohort boundary"). **This fork never reached the standalone-floor / fused-composite edges** (`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`/`reciprocal`/`elementwise-product` cycle-042 + `normalize` cycle-043) — each has **NO fold-parent**, so there is no fold to dissolve a leaf into; that cohort is design-final regardless. The cycle-041 slug split was also normalized cycle-043 (D1): `nrm2-fold-specialization`→`nrm2-leaf-identity` + `scal-fold-specialization`→`scal-leaf-identity`, so the whole L2>L1 identity-edge cohort is uniform `-leaf-identity` (neither edge is a fold-dispatch).
```

### (b) Consolidated counts in `book/src/L3-L2/index.md`

I do NOT add the 4 new `-body-identity` theme rows (D6/D7/D8/D10 each append their own row + Vocabulary-cohort sub-bullet). I own the §Working-Notes cohort-growth/coverage-gap tally + the §"Design fork" flip. D1 owns the `elementwise_product-body-identity`→`elementwise-product-body-identity` rename (disjoint lines).

#### E10 — §Working-Notes cohort-growth + coverage-gap tally (line 48): advance 10→14 / 14-of-18

```edit:book/src/L3-L2/index.md
[old]: - **Cohort growth + coverage-gap progress (firm 5 → 10; `l3-l2-rotation-theme-coverage-gap` 5-of-18 → 10-of-18).** Cycle-042 landed five more L3>L2 thin-identity `-body-identity` themes — the **fork-INDEPENDENT standalone-floor** cohort (`assemble-diagonal-body-identity` / `jacobi-smoother-body-identity` / `divfree-projector-body-identity` / `reciprocal-body-identity` / `elementwise_product-body-identity`), each the leaf-/gate-primitive analogue of the firm `krylov-step-body-identity` (cycle-007/009) but strictly simpler — a single leaf or fixed-step gate, no wrapper to rotate, **no fold-parent** (distinct from the cycle-041 BLAS-1-leaf cohort, which is fold-parented and rides the batch-12 leaf-vs-fold fork; this cohort is design-final). This continues closing the `l3-l2-rotation-theme-coverage-gap` plan item: the iteration-rotation rewrite (the defining content of the L3 layer) was documented for 5 of 18 L3 entries after cycle-041; now **10 of 18**, with 8 still relying on inline identity annotations. The remaining gap splits into **thin-identity** edges (the rest of the identity-in-form L3 cohort) and **substantive** edges (`chebyshev`, `eigsolve` `partial-obstruction`, `orthogonalize` MGS-vs-CGS) — author thin where identity-in-form, firm-substantive where the rotation carries real content. (Prior: cycle-041 landed the first three BLAS-1-leaf themes `dot-body-identity` / `nrm2-body-identity` / `scal-body-identity`, taking the gap 2-of-18 → 5-of-18.)
[new]: - **Cohort growth + coverage-gap progress (firm 10 → 14; `l3-l2-rotation-theme-coverage-gap` 10-of-18 → 14-of-18).** Cycle-043 landed four more L3>L2 thin-identity `-body-identity` themes — the **leaf-cohort batch** (`axpy-body-identity` / `axpby-body-identity` / `axpbypcz-body-identity` / `normalize-body-identity`), each the leaf-/composite-primitive analogue of the firm `krylov-step-body-identity` (cycle-007/009) but strictly simpler (no wrapper to rotate). The `axpy`-family three are **fold-PARENTED** (their L2 RHS is a same-named arity-2/2/3 leaf-floor of `linear_combination`) and ride the now-RATIFIED (b) leaf-floor reading (UNBLOCKED by the batch-12 meta-phase — no longer "under adjudication"); `normalize-body-identity` is the **fused-composite** edge whose L2 RHS is the `nrm2 ∘ scal` composite floor with NO fold-parent (design-final). This advances the `l3-l2-rotation-theme-coverage-gap` from **10 of 18 → 14 of 18**, with 4 still relying on inline identity annotations. The remaining gap is the **substantive** edges (`chebyshev` — though its rotation is in-line at `chebyshev-iteration` already, `eigsolve` `partial-obstruction`, `orthogonalize` MGS-vs-CGS, and any leaf residual) — author firm-substantive where the rotation carries real content. (Prior: cycle-042 landed the five fork-INDEPENDENT standalone-floor themes `assemble-diagonal-body-identity` / `jacobi-smoother-body-identity` / `divfree-projector-body-identity` / `reciprocal-body-identity` / `elementwise-product-body-identity` (renamed cycle-043 from `elementwise_product-body-identity`, underscore→hyphen), taking the gap 5-of-18 → 10-of-18; cycle-041 landed the first three BLAS-1-leaf themes, 2-of-18 → 5-of-18.)
```

#### E11 — §Working-Notes §"Design fork" (line 50): flip to RATIFIED

```edit:book/src/L3-L2/index.md
[old]: - **Design fork (`dot-l2-leaf-floor-vs-fold-only-design`; load-bearing batch-12 meta-phase signal).** The three cycle-041 body-identity themes presuppose the **(b) same-named L2 leaf-floor** realization of the BLAS-1 surface (their L2 RHS is a same-named `dot`/`nrm2`/`scal` floor). Wave-1 D2 argued the **(a) fold-only** reading. If the meta-phase adopts (a), each theme's L2 RHS re-points from a same-named leaf to the fold-parent (`dot`/`nrm2` → `inner_product`; `scal` → `linear_combination`), weakening the "identity" claim (a same-named leaf → a differently-named fold-parent is a weaker identity). Surfaced for the meta-phase; the themes are self-coherent under the (b) reading they are built on.
[new]: - **Design fork RATIFIED (`dot-l2-leaf-floor-vs-fold-only-design`; batch-12 meta-phase, decision 1 — keep leaf-floor (b)).** The cycle-041 body-identity themes presuppose the **(b) same-named L2 leaf-floor** realization of the BLAS-1 surface (their L2 RHS is a same-named `dot`/`nrm2`/`scal` floor); the cycle-043 `axpy`-family body-identity themes do likewise (L2 RHS = a same-named arity-2/2/3 leaf-floor of `linear_combination`). Wave-1 D2 argued the **(a) fold-only** reading; the **batch-12 meta-phase RATIFIED (b)** (adopting the c042 cross-cutter audit — see `book/src/L2/index.md` §Working-Notes), so each theme's L2 RHS stays a same-named leaf-floor (the strong "identity" claim holds — the (a)-branch re-point to a differently-named fold-parent is moot). The `normalize-body-identity` edge (cycle-043) and the cycle-042 standalone-floor body-identity edges have **NO fold-parent** and were never reached by the fork — design-final regardless.
```

#### E11b — (repairer) reconcile the stale provisional fork bullet at §Working-Notes line 49 to RATIFIED

Appended by the repairer (cycle-043 critique Issue 2, cross-reference-integrity warning): §Working-Notes carries TWO adjacent "Design fork" bullets (lines 49 + 50). E11 flips only the line-50 bullet to RATIFIED, leaving the line-49 bullet in un-decided "reaches ONLY", "presuppose … under (a)", "recommends KEEPING" language — so post-flip the two adjacent bullets contradict on whether the fork is decided. This block flips the line-49 bullet to the same RATIFIED footing as E11 (the decision content already exists in E5/E9/E11; this is wording reconciliation only, no new decision authored). The line-49 bullet's distinct payload — that the fork reached ONLY the fold-parented cohort and never the cycle-042 standalone / cycle-043 fused-composite edges — is preserved, now in the past tense / ratified frame. Unique full-line `[old]` anchor (grep count 1).

```edit:book/src/L3-L2/index.md
[old]: - **Design fork (`dot-l2-leaf-floor-vs-fold-only-design`) reaches ONLY the cycle-041 cohort.** The cycle-041 `-body-identity` themes presuppose the (b) same-named L2 leaf-floor RHS and re-point to the fold-parent under (a); the cycle-042 standalone-floor `-body-identity` themes have **NO fold-parent** and so are unaffected by the adjudication (their L2 RHS is a same-named standalone floor with no fold to re-anchor into). The c042 cross-cutter audit recommends KEEPING leaf-floor (b) for the cycle-041 cohort — see `book/src/L2/index.md` §Working-Notes.
[new]: - **Design fork RATIFIED — reached ONLY the fold-parented cohort.** The batch-12 meta-phase RATIFIED leaf-floor (b) (decision 1; adopting the c042 cross-cutter audit — see `book/src/L2/index.md` §Working-Notes), so the cycle-041 + cycle-043 `axpy`-family `-body-identity` themes keep their same-named L2 leaf-floor RHS (the (a)-branch re-point to the fold-parent is moot). The fork reached ONLY the fold-parented edges; the cycle-042 standalone-floor + cycle-043 `normalize` fused-composite `-body-identity` themes have **NO fold-parent** and were never touched by the adjudication (their L2 RHS is a same-named standalone / composite floor with no fold to re-anchor into) — design-final regardless.
```

---

## Supporting evidence

### On-disk count baselines (Phase-2 enumeration; per role-spec "survey from on-disk, NOT the cycle record")

`book/src/L2/index.md` §Operator dep-map — 18 rows enumerated leading-operator + status verdict:
`krylov-step`/`chebyshev-iteration`/`linear_combination`/`scal`/`inner_product`/`dot`/`nrm2`/
`reciprocal`/`elementwise_product`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`/
`orthogonalize`/`incremental-least-squares`/`ksp_solve`/`gram`/`eigsolve` = **17 firm**; `deflate` =
**1 partly-constructive**. ⇒ baseline **17 firm + 1 PC (18 rows)**; after +4 floors ⇒ **21 firm + 1 PC
(22 rows)**.

`book/src/L2-L1/index.md` §Theme list — 16 rows: `chebyshev-iteration-fusion`,
`linear-combination-fold-specialization`, `scal-fold-specialization`(→`scal-leaf-identity`),
`inner-product-fold-specialization`, `dot-leaf-identity`, `nrm2-fold-specialization`
(→`nrm2-leaf-identity`), `assemble-diagonal-leaf-identity`, `jacobi-smoother-leaf-identity`,
`reciprocal-leaf-identity`, `elementwise-product-leaf-identity`, `orthogonalize-composition-lowering`,
`gram-fold-specialization`, `eigsolve-spectral-transform-composition`, `divfree-projector-leaf-identity`,
`incremental-least-squares-composition-lowering` = **15 firm**; `deflate-composition-lowering` =
**1 PC**. ⇒ baseline **15 firm + 1 PC (16 rows)**; after +4 themes (D1 renames net-zero) ⇒ **19 firm +
1 PC (20 rows)**.

`book/src/L3-L2/index.md` §Theme list — 10 rows, all firm: `krylov-step-body-identity`,
`dot-body-identity`, `nrm2-body-identity`, `ksp-solve-outer-driver`, `scal-body-identity`,
`assemble-diagonal-body-identity`, `jacobi-smoother-body-identity`, `reciprocal-body-identity`,
`elementwise_product-body-identity`(→`elementwise-product-body-identity`), `divfree-projector-body-identity`
= **10 firm**. ⇒ baseline **10 firm (10 rows)**; after +4 themes (D1 rename net-zero) ⇒ **14 firm
(14 rows)** = `l3-l2-rotation-theme-coverage-gap` **14-of-18**.

### Cohort sub-shape evidence (from the co-dispatched harvester reports)

- `axpy`/`axpby`/`axpbypcz` land `firm`, each the **arity-2/2/3 member of `linear_combination`**
  (cited NOT merged; second coeff fixed to 1 for `axpy`); the output-aliasing variant axis is the
  fold's (planner OQ `arity-family-leaf-floors-output-aliasing-axis-is-the-folds`). Same shape as the
  cycle-041 `scal` arity-1 floor → **fold-PARENTED**, under the RATIFIED (b) reading.
  (`reports/.../harvester-L2-axpy/CYCLE.md:46`, `-axpby/CYCLE.md:60,82`, `-axpbypcz/CYCLE.md:32,37`.)
- `normalize` lands `firm`, a **fused composite** `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` with
  **NO fold-parent** — fork-INDEPENDENT on membership (consumer-not-member like `nrm2`), design-final on
  the leaf-vs-fold fork; a *composite-with-no-fold-parent* basis distinct from the cycle-042
  standalone-leaf basis (`reports/.../harvester-L2-normalize/CYCLE.md:20,52-63,124-135`). This is the NEW
  thin-identity sub-shape surfaced for the batch-13 meta-phase.

### Fork-ratification source

Batch-12 meta-phase decisions 1 (keep leaf-floor (b) cohort-wide) + 3 (cohort-neutral heading rename)
per the cycle-043 planner (`reports/.../cycle-planner-cycle-043/CYCLE.md:18-19,183-205`) and the c042
cross-cutter audit it adopts (`reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/`).

### Disjointness verification with D1 (lifter)

D1's L2/index.md touches are C8 (lines 106 + 108 — cycle-041 cohort note + slug-naming note). My
L2/index.md touches: lines 28 (E1), 45 (E2), §Fold-cohort-boundary working note (E4), line-107
fork-signal bullet (E5), dep-map after `eigsolve` (E6), line-105 cohort note (E7 appends a sibling
bullet, does NOT rewrite 105/106). **No shared line.** In L2-L1/index.md and L3-L2/index.md, D1 edits
per-slug rename rows/links; I edit §Working-Notes cohort-growth-log + §"Design fork" bullets — disjoint.

---

## Open questions / caveats

- **`chebyshev` floor-cohort count reconciliation (routed to batch-13 meta-phase).** The
  `l2-floor-under-l3-leaf-cohort` denominator "13" lists `chebyshev` as missing, but its L2 floor is
  already present as the firm `chebyshev-iteration` (cycle-012; non-same-named slug). Cohort is
  **12-of-13** with the 13th already-floored. Planner-recommended resolution:
  **count-correction-to-12 + naming-exception** (a same-named `L2/chebyshev.md` pointer would be pure
  naming bureaucracy). Surfaced in the L2/index §Working-Notes (E7) for the batch-13 meta-phase. I did
  NOT renumber the cohort denominator in the artifact this cycle (it is the meta-phase's call); I record
  it as "12-of-13 present, 13th already-floored, reconciliation pending".

- **`normalize` NEW thin-identity sub-shape (`fused-composite-no-fold-parent`).** Surfaced in the
  L2/index §Working-Notes (E7) for the batch-13 meta-phase to decide whether the cohort-classification
  vocabulary should name this sub-shape explicitly. Currently it reads as a third bullet under the
  §Vocabulary-cohort split (fold-parented leaves / standalone leaves+gates / fused-composite).

- **axpy-family + normalize L3 entries left stale (downstream consequence; routed to c044).** Exactly
  as the c042 floor cohort left its four L3 entries stale (swept this cycle by D1), the
  `axpy`/`axpby`/`axpbypcz`/`normalize` L3 entries carry "no L2 intermediate" assertions that go stale
  when this cycle's floors land. Not in my scope (an L3-entry re-anchor is lifter work; the planner
  routed it to a c044 consolidated lifter sweep). Flagged so the next planner does not miss it.

- **D1 rename-dependency ordering (count correctness).** My L2-L1 / L3-L2 cohort narratives use the NEW
  slug names (`nrm2-leaf-identity`, `scal-leaf-identity`, `elementwise-product-body-identity`). Since I
  run LAST (wave-3, deps include D1), this presupposes D1's renames already landed on disk. If the
  serial integrator applies D1 before D2 (the planned order), my edits match; if reordered, the
  integrator's by-slug matching still resolves cleanly (the renamed targets exist either way after both
  land). No action needed — flagged for integrator awareness.

- **L2/index.md length.** The file is ~110 lines pre-edit and grows ~3 §Working-Notes bullets + 4
  dep-map rows + 2 Vocabulary-cohort sub-bullets. It remains under the ~200-line split threshold; no
  promotion to `semantics.md` / `dep-map.md` is warranted this cycle. (Re-evaluate at the next L2
  intro refresh if the dep-map crosses ~25 rows — it will be at 22 after this cycle.)
