---
agent: lifter
invoked_at: 2026-06-01T21:14:28Z
scope: L3>L2 + L2>L1 theme demotion + L3-leaf re-expression — linear_combination family (8 themes deleted + 4 L3 leaves re-expressed through the combinator)
status: integrated
integrated_at: 2026-06-01T22:14:50Z
integration_commit: 76721fec7a70c2ceed5e17de8c0f06ab3ad56205
integration_notes: "Applied clean by integrator-per-report (D1, first of cycle-051); finalized cycle-051. 8 themes deleted (scal/axpy/axpby/axpbypcz-{body,leaf}-identity); 4 L3 leaves re-expressed through L3/linear_combination; BUILD-CRITICAL L3/index.md link re-points; zero dangling live links to deleted slugs; build exit 0."
inputs:
  - book/src/L3-L2/scal-body-identity.md
  - book/src/L3-L2/axpy-body-identity.md
  - book/src/L3-L2/axpby-body-identity.md
  - book/src/L3-L2/axpbypcz-body-identity.md
  - book/src/L2-L1/scal-leaf-identity.md
  - book/src/L2-L1/axpy-leaf-identity.md
  - book/src/L2-L1/axpby-leaf-identity.md
  - book/src/L2-L1/axpbypcz-leaf-identity.md
  - book/src/L3/scal.md
  - book/src/L3/axpy.md
  - book/src/L3/axpby.md
  - book/src/L3/axpbypcz.md
  - book/src/L3/linear_combination.md
  - book/src/L2/linear_combination.md
  - book/src/L2-L1/linear-combination-fold-specialization.md
  - book/src/L3-L2/index.md
  - book/src/L2-L1/index.md
  - book/src/SUMMARY.md
---

# CYCLE: Re-anchor linear_combination family — demote 8 degenerate themes + re-express 4 L3 leaves

## Summary

Cycle-051 D1 enacts the **demote half** of the cycle-049 combinator-miner replace-and-propagate map (`reports/2026-06-01T190900Z-combinator-miner-refactor-pass-linear-combination-family/CYCLE.md` (b.2)) for the `linear_combination` arity family, under the 2026-06-01 VOCABULARY-SHIFT REDIRECT (`METHODOLOGY-REDIRECT.md`; CLAUDE.md §Methodology invariants ⟢). The eight `{scal,axpy,axpby,axpbypcz}-body-identity` (L3>L2) and `{scal,axpy,axpby,axpbypcz}-leaf-identity` (L2>L1) themes each **self-describe as identity-in-named-terms** ("The body IS the identity", "no wrapper to rotate", "value-thread-isomorphic", "all fusion deferred to the fold-parent") — the §1d degenerate-lowering smell (the vocabulary did not shift; the LHS and RHS are the same named operator at the same arity). Their content is already absorbed into the pre-built combinator homes: `L3/linear_combination.md` §"Downward to L2" (`:107-113`, explicitly written "to accommodate that demotion … the pre-built home for the four leaf-edge identities") and `L2/linear_combination.md` §Dependencies (`:213-238`, which already routes the L2>L1 lowering through the KEPT `linear-combination-fold-specialization` theme). This dispatch **deletes the 8 degenerate themes** (a), **re-expresses the 4 L3 leaves to speak THROUGH `L3/linear_combination`** as arity-N specializations rather than re-deriving the base form (b), **defensively de-links** inbound live links to the deleted slugs (c), and **removes D1's own SUMMARY + dep-map rows** while DEFERRING the consolidated tally to D5 (d). The substantive arity-dispatch / pinned-summation-order translation is untouched — it lives in the KEPT `L2-L1/linear-combination-fold-specialization` theme, which the re-expressed leaves now reference as their lowering home.

## Proposed changes

### (a) DELETE the 8 degenerate identity-in-named-terms theme files

```delete:book/src/L3-L2/scal-body-identity.md
```

```delete:book/src/L3-L2/axpy-body-identity.md
```

```delete:book/src/L3-L2/axpby-body-identity.md
```

```delete:book/src/L3-L2/axpbypcz-body-identity.md
```

```delete:book/src/L2-L1/scal-leaf-identity.md
```

```delete:book/src/L2-L1/axpy-leaf-identity.md
```

```delete:book/src/L2-L1/axpby-leaf-identity.md
```

```delete:book/src/L2-L1/axpbypcz-leaf-identity.md
```

Absorption note: no new per-arity absorption pointer is needed in either combinator home. The L3 home's §"Downward to L2" (`L3/linear_combination.md:107-113`) was authored c050 explicitly as the pre-built home for the four leaf-edge identities ("the concatenation-law specializations of this one combinator identity (the arity-1/2/2/3 readings of `linear_combination`'s body-identity)"). The L2 home's §Dependencies (`L2/linear_combination.md:213-238`) already routes the family's L2>L1 lowering through the KEPT `linear-combination-fold-specialization` theme. The only stale forward-looking phrasing in the L3 home is the c050-era "scheduled to demote … at cycle-051 / once the L3 leaves are re-expressed (cycle-051)" — corrected in change (e) (bounded prose-correction: the demotion is now done, not scheduled).

### (b) RE-EXPRESS the 4 L3 leaves to speak THROUGH the combinator

Each leaf is re-expressed as the **arity-N specialization of `L3/linear_combination`**: the leaf IS the combinator at a fixed term-list length; the lowering routes through the combinator's §"Downward to L2" identity edge + the KEPT `L2-L1/linear-combination-fold-specialization` theme (which carries the substantive arity-dispatch + pinned-summation-order translation), NOT through a now-deleted per-leaf `*-body-identity` theme. Load-bearing facts (fast-path / pinned-order notes, inherited L0 anchors) are preserved. No L1/L0 base-form re-derivation is introduced (high→low).

#### (b.1) `book/src/L3/scal.md`

```edit:book/src/L3/scal.md
[old]: lowers_to:
  - book/src/L1/scal.md (identity-in-form; no `L3-L1/` directory yet — identity rotation noted in-line at "Lifts from")
lifts_from:
  - book/src/L1/scal.md (value-thread-isomorphic; same signature shape; whole-tensor by construction)
[new]: lowers_to:
  - book/src/L2/linear_combination.md (the arity-1 specialization of the firm L3/L2 `linear_combination` fold; `scal(α,x) = linear_combination [(α,x)]`; lowers via the combinator's §"Downward to L2" identity-in-form edge, then the substantive arity-dispatch is the L2>L1 `linear-combination-fold-specialization` theme) → book/src/L1/scal.md (transitive L3>L1 identity in-line; no `L3-L1/` directory)
lifts_from:
  - book/src/L3/linear_combination.md (the family combinator this leaf is the arity-1 specialization of — `scal` speaks through `linear_combination`, not as a re-derived base form, per the 2026-06-01 vocabulary-shift redirect)
```

```edit:book/src/L3/scal.md
[old]# scal

Vector-scalar multiplication as a whole-tensor field operation at L3 — the **iteration-rotation** rendering of `y ← α·y`. Consumes a scalar `α` and a tensor `x`; produces a fresh tensor of the same length axis whose every element is `α` times the corresponding input element. Companion to L1 [`scal`](../L1/scal.md) (the mutation-lifted form of the same primitive); the rotation L1 → L3 is identity-in-form because the signature exposes no element loop.
[new]# scal

Vector-scalar multiplication as a whole-tensor field operation at L3 — the **arity-1 specialization of the [`linear_combination`](./linear_combination.md) fold**: `scal(α, x) = linear_combination [(α, x)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms `scal` / `axpy` / `axpby` / `axpbypcz` speak **through** the combinator, not as re-derived base forms — `scal` is the combinator at term-list length 1. This chapter is the arity-1 readout label for the bounded-arity L0 call shape (`operator*=`); its algebra is the fold's law set read at length 1, and its lowering routes through the combinator's §"Downward to L2" identity edge + the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme.
```

The §Context "Downward to L1" identity-in-form sketch (`book/src/L3/scal.md:22-26`) re-derives the base form against L1; re-frame to the combinator route. Also re-frame the §"Lowers to" and §"Lifts from" sections that target L1 directly.

```edit:book/src/L3/scal.md
[old]The relationship to L1 is captured by an **identity-in-form** rotation:

- **Downward** to L1: the L3 form's signature `Scalar -> Tensor[N] -> Tensor[N]` is textually identical to the L1 form's signature; both forms describe pure-functional vector-scalar multiplication with no destination buffer in the signature, no per-element loop visible, no reduction, no MPI collective at the L1 / L3 surface. The L3 → L1 rotation is the identity on the primitive itself. The framing differs: L1 frames `scal` as the *mutation-rotation* image of the L0 receiver-mutating `mfem::Vector::operator*=` / `ComplexVector::operator*=` member-method idiom (the L1 surface drops the destination-buffer mention); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. **The body of `scal` is the identity rotation across this edge.**

This L3 entry is the layer-coherence anchor: a reader at L3 can find `scal` here, in L3 vocabulary, without having to reach down to L1 to recover the field-operation shape. The backfill is the cycle-011 wave-1 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification) on the BLAS-1 cohort, following the wave-1 `krylov-step` L3 backfill precedent (cycle-010). The cross-layer-cross-cutter audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`) HIGH CONFIDENCE recommendation for the BLAS-1 bundle is the load-bearing dispatch rationale: the L3 index (`book/src/L3/index.md:11-14`) already advertises `axpy / dot / nrm2` as whole-tensor field operations, and the seven L1 primitives are explicitly named L3-native by signature shape in the firm L3>L2 body-identity theme (`book/src/L3-L2/krylov-step-body-identity.md:97`). `scal` is the standalone leaf of that bundle; this dispatch closes its L3 entry.
[new]The relationship to the lower layer is the **combinator route**: `scal` is the arity-1 specialization of [`linear_combination`](./linear_combination.md), so its downward edge is the combinator's downward edge read at length 1. The L3 fold lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the combinator body (`L3/linear_combination.md:107-113` §"Downward to L2"); the substantive rotation — which L0 leaf each list-length pins, and its summation order — is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme. At length 1 there is **no sum and no arity dispatch** (one term computes one scaled pass, one rounding per element — value- and bit-exact), so `scal`'s lowering is the degenerate single-term reading of the fold's downward edge. The framing across layers differs only documentarily: L1 frames `scal` as the *mutation-rotation* image of the L0 receiver-mutating `mfem::Vector::operator*=` / `ComplexVector::operator*=` member-method idiom; L2/L3 frame it as the arity-1 fold member.

This L3 entry is the layer-coherence anchor: a reader at L3 finds `scal` here, in L3 vocabulary, as the arity-1 fold member, without re-deriving the base form. It was backfilled cycle-011 (wave-1 BLAS-1 cohort, per the cross-layer-cross-cutter audit `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` HIGH CONFIDENCE recommendation) and re-expressed through the combinator cycle-051 D1 (the propagate half of the cycle-049 replace-and-propagate map). The L3 index (`book/src/L3/index.md:11-14`) advertises the BLAS-1 cohort as whole-tensor field operations.
```

```edit:book/src/L3/scal.md
[old]## Lowers to

L3 `scal` lowers to L1 [`scal`](../L1/scal.md) via an **identity-in-form** rotation: the signature `Scalar -> Tensor[N] -> Tensor[N]` is textually identical at both layers; the body is the same whole-tensor field operation. No `L3-L1/` directory exists in the artifact (the cycle-010 audit OQ `l3-l1-directory-naming-structure-policy` tracks the broader policy question of whether identity L3>L1 rotations get thin sibling themes or in-line notes); per the wave-1 `krylov-step` L3 backfill precedent this entry captures the identity rotation in-line. The L0 in-place mutation is reintroduced at the L1>L0 lowering (no firm `scal-mutation-rotation` theme yet; the L1 entry sketches the content in its §"L1 vs L0 distinction" and §Evidence).

## Lifts from

L1 `scal` lifts to this L3 entry via the **value-thread-isomorphic** identity rotation: the L1 form's signature has no element loop exposed, no destination buffer, no MPI collective, no iteration view — these are exactly the properties that make it L3-native by construction. The cross-layer-cross-cutter audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"(2) `axpy` / `axpby` / `axpbypcz` / `dot` / `nrm2` / `scal` (the BLAS-1 cohort)") HIGH CONFIDENCE recommendation classifies the rotation as identity-in-form, citing the firm L3>L2 body-identity theme's line 97 ("each L1 primitive is *also* L3-native because its signature has no per-element loop visible") and the firm L4>L3 typed-wrapper-dissolution theme's line 68 (which renders the BLAS-1 primitives in the L3 body let-chain identically to L1). **This L3 entry exists for layer-coherence reasons** — a reader navigating L3 must find `scal` defined in L3 vocabulary, not have to reach down to L1 to recover the field-operation shape.

The wave-1 `krylov-step` L3 backfill (`book/src/L3/krylov-step.md`, cycle-010) is the structural precedent: identity-in-form rotation on the body, layer-coherence backfill, methodology invariant enacted. The BLAS-1 cohort (this dispatch + the three sibling dispatches in cycle-011 wave-1) is the broader enactment per the audit's recommendation.
[new]## Lowers to

L3 `scal` lowers as the **arity-1 specialization of [`linear_combination`](./linear_combination.md)**. The combinator lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the fold body (`L3/linear_combination.md:107-113` §"Downward to L2"); read at term-list length 1 this is `scal(α, x) = linear_combination [(α, x)]`. The substantive rotation in the downward chain is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme (it reads the term-list length and selects the maximal fused L0 leaf — length 1 → `scal`'s `operator*=` — and records each lowered call's pinned summation order). At length 1 the summation order is degenerate (one term, one rounding per element — value- and bit-exact), so `scal`'s lowering carries no pinned-order residue. The transitive L3>L1 identity (the combinator's L3>L2 identity ∘ the L2>L1 fold-specialization's value-identity at length 1) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory. The L0 in-place mutation is reintroduced at the L1>L0 lowering (the L1 entry sketches the content in its §"L1 vs L0 distinction" and §Evidence).

## Lifts from

`scal` is the **arity-1 member of the [`linear_combination`](./linear_combination.md) fold** — it speaks through the combinator at L3 and above, not as a re-derived base form (the propagate half of the cycle-049 replace-and-propagate map, per the 2026-06-01 vocabulary-shift redirect). The combinator carries no L4 entry (it is a pure value-producing reduction over a term list, not a calculus combinator with monadic state-threading or a convergence predicate; `L3/linear_combination.md:152-154`); `scal` appears inside L4 operator bodies as a let-binding (the cohort audit's "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 cohort). This L3 entry exists for layer-coherence — a reader at L3 finds `scal` defined as the arity-1 fold member without re-deriving the base form.
```

The §Algebraic-laws, §Dependencies, §Variant-axes, §Status, §Evidence, and §"L3 vs L1 distinction" sections of `scal.md` need only a mechanical framing swap (re-frame "inherited verbatim from L1" as "the fold's law set read at length 1") and the §Evidence/§Dependencies references to the deleted `scal-body-identity`/`scal-leaf-identity` themes re-pointed at the combinator + the kept fold-specialization theme. `scal.md` did NOT reference its `*-body-identity` / `*-leaf-identity` themes in those sections (it pre-dated them; it referenced L1 directly and `krylov-step-body-identity:97`), so no dead-link cleanup is needed there beyond the frontmatter + §Context + §"Lowers to"/§"Lifts from" edits above. The §Status line carries no dead reference. **scal.md's algebraic-laws are a clean mechanical reframe (the nine module-action laws are the fold's coefficient-scaling/absorption laws read at length 1); no substantive rework — in-scope.**

#### (b.2) `book/src/L3/axpy.md`

`axpy.md` references the deleted `axpy-body-identity` theme in its frontmatter `lowers_to:`, §Dependencies (`:97`), §"Lowers to" (`:114`), and §Evidence (`:127`). Re-route all four to the combinator + kept fold-specialization theme.

```edit:book/src/L3/axpy.md
[old]lowers_to:
  - book/src/L2/axpy.md (present adjacent L2 floor, cycle-043; identity-in-form on the primitive's signature shape, via the `axpy-body-identity` L3>L2 theme; whole-tensor in / whole-tensor out at both layers) → book/src/L1/axpy.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
lifts_from:
  - (no L4 entry — leaf primitive, not a calculus combinator; per cycle-010 cohort audit verdict "L4 candidate CONFIRMED-NOT-NEEDED" for the BLAS-1 cohort)
[new]lowers_to:
  - book/src/L2/linear_combination.md (the arity-2 specialization of the firm L3/L2 `linear_combination` fold, second coeff fixed to 1; `axpy(α,x,y) = linear_combination [(α,x),(1,y)]`; lowers via the combinator's §"Downward to L2" identity-in-form edge, then the substantive arity-dispatch is the L2>L1 `linear-combination-fold-specialization` theme) → book/src/L1/axpy.md (transitive L3>L1 identity in-line, the fold-specialization picking the `AXPY` L0 leaf)
lifts_from:
  - book/src/L3/linear_combination.md (the family combinator this leaf is the arity-2 specialization of — `axpy` speaks through `linear_combination`, not as a re-derived base form, per the 2026-06-01 vocabulary-shift redirect; no L4 entry — the fold is a pure value-producing reduction, not a calculus combinator)
```

```edit:book/src/L3/axpy.md
[old]# axpy

Whole-tensor vector-scalar fused update at L3: `axpy(α, x, y) = α·x + y`. The L3-native rendering of the canonical BLAS-1 linear-update primitive — the same primitive that is firm at L1 ([`axpy`](../L1/axpy.md)), surfaced here in L3 vocabulary because **each layer is internally coherent** (CLAUDE.md §Methodology invariants).
[new]# axpy

Whole-tensor vector-scalar fused update at L3: `axpy(α, x, y) = α·x + y` — the **arity-2 specialization of the [`linear_combination`](./linear_combination.md) fold** with the second coefficient fixed to 1: `axpy(α, x, y) = linear_combination [(α, x), (1, y)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms speak **through** the combinator, not as re-derived base forms — `axpy` is the combinator at term-list length 2 with the trailing coefficient pinned to 1. This chapter is the arity-2 readout label for the bounded-arity L0 call shape (`AXPY`); its algebra is the fold's law set read at that fixed length, and its lowering routes through the combinator's §"Downward to L2" identity edge + the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme.
```

```edit:book/src/L3/axpy.md
[old]No L4 monadic vocabulary appears in the L3 signature (no `Solve`, no `modify`, no `do`-block) — `axpy` is not a calculus combinator at L4. The cohort audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`) verdict for the BLAS-1 cohort at L4 is **CONFIRMED-NOT-NEEDED**: leaf primitives don't get L4 rows. The adjacent L3>L2 rotation passes through the **present** L2 floor [`axpy`](../L2/axpy.md) (cycle-043) via the firm [`axpy-body-identity`](../L3-L2/axpy-body-identity.md) L3>L2 theme — identity-in-form on the body, no wrapper rotation; onward to L1 [`axpy`](../L1/axpy.md). The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent (per **Identity-lowerings still require both L levels**), rather than skipping a layer to L1.
[new]No L4 monadic vocabulary appears in the L3 signature (no `Solve`, no `modify`, no `do`-block) — neither `axpy` nor the `linear_combination` fold it specializes is a calculus combinator at L4 (the cohort audit verdict for the BLAS-1 cohort at L4 is **CONFIRMED-NOT-NEEDED**; `L3/linear_combination.md:152-154`). The downward rotation passes through the firm L2 [`linear_combination`](../L2/linear_combination.md) via the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at term-list length 2 (second coeff 1) — `axpy` is the arity-2 fold member. The substantive arity-dispatch (length → maximal fused L0 leaf, here the `AXPY` symbol) + the pinned summation order live in the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme, NOT in a per-leaf theme.
```

```edit:book/src/L3/axpy.md
[old]## Lowers to

L3 `axpy` lowers to the **present adjacent L2 floor** [`axpy`](../L2/axpy.md) (cycle-043) as **identity-in-form on the primitive's signature shape**, via the firm [`axpy-body-identity`](../L3-L2/axpy-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `axpy` is a leaf whole-tensor field operation, not a step body), and onward to L1 [`axpy`](../L1/axpy.md). The three surfaces are textually identical modulo layer-coherence vocabulary (L1 / L2 / L3 all see `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set, and the same variant-axis profile). The L2 floor is the standalone fold-member BLAS-1 leaf — landed by the cycle-043 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` (mirroring the cycle-041 `dot` / `nrm2` / `scal` floors) — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is annotated in-line per the cycle-012 non-adjacent-identity convention (lowering directories are per-adjacent-edge only); no `book/src/L3-L1/` directory is created. The substantive rotation in the chain is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (which covers `axpy` as the β=1 specialisation of `axpby`).
[new]## Lowers to

L3 `axpy` lowers as the **arity-2 specialization of [`linear_combination`](./linear_combination.md)** (second coefficient fixed to 1: `axpy(α, x, y) = linear_combination [(α, x), (1, y)]`). The combinator lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the fold body (`L3/linear_combination.md:107-113` §"Downward to L2"). The substantive rotation in the downward chain is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme: it reads the term-list length (here 2 with the trailing coeff 1) and selects the maximal fused L0 leaf — the `AXPY` symbol, which carries the `α == 1.0` fast-path (`palace/linalg/vector.cpp:702-712`) — and records its pinned summation order. All arity dispatch and summation-order residue are the fold-parent's, not this leaf's.

The **transitive** L3>L1 identity (the combinator's L3>L2 identity ∘ the L2>L1 fold-specialization's value-identity at this list length) is annotated in-line per the cycle-012 non-adjacent-identity convention (lowering directories are per-adjacent-edge only); no `book/src/L3-L1/` directory is created. The substantive in-place mutation rotation, reached transitively, is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (which covers `axpy` as the β=1 specialisation of `axpby`).
```

```edit:book/src/L3/axpy.md
[old]- `book/src/L2/axpy.md` (cycle-043 firm) — the present adjacent L2 floor this L3 entry lowers into via the `axpy-body-identity` theme; identity-in-form on the primitive's signature.
- `book/src/L3-L2/axpy-body-identity.md` (cycle-043 firm) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation.
- `book/src/L1/axpy.md` (cycle-002 firm) — the L1 form this L3 entry transitively rotates from (L3>L2 ∘ L2>L1). Body shape, semantics, six algebraic laws, two non-laws, variant-axis profile.
[new]- `book/src/L3/linear_combination.md` (cycle-050 firm) + `book/src/L2/linear_combination.md` (inverted-to-entry cycle-049 D1) — the family combinator this leaf is the arity-2 specialization of; §"Arity specializations" (`L3/linear_combination.md:50-61`) names `axpy = linear_combination [(α,x),(1,y)]`, §"Downward to L2" (`:107-113`) is the identity-in-form edge this leaf's lowering reads at length 2.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; cycle-049 D1(c) KEEP verdict) — the substantive L2>L1 fusion-selection theme that picks the `AXPY` L0 leaf at this list-length and records its pinned summation order (the lowering's substantive content, deferred here, not in a per-leaf theme).
- `book/src/L1/axpy.md` (cycle-002 firm) — the L1 leaf the fold-specialization recovers at this arity (the L1>L0 one-to-one `AXPY` symbol shape). Body shape, semantics, six algebraic laws, two non-laws, variant-axis profile.
```

**axpy.md's algebraic-laws are a clean mechanical reframe** (the six laws are the fold's multilinearity / coefficient-scaling laws read at length 2 with trailing coeff 1); no substantive rework — in-scope.

#### (b.3) `book/src/L3/axpby.md`

`axpby.md` references `axpby-body-identity` in frontmatter `lowers_to:`, §Dependencies (`:101`), §"Lowers to" (`:118`), and §Evidence (`:131`). Re-route all four.

```edit:book/src/L3/axpby.md
[old]lowers_to:
  - book/src/L2/axpby.md (present adjacent L2 floor, cycle-043; identity-in-form on the primitive's signature shape, via the `axpby-body-identity` L3>L2 theme; whole-tensor in / whole-tensor out at both layers) → book/src/L1/axpby.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
lifts_from:
  - (no L4 entry — leaf primitive, not a calculus combinator; per cycle-010 cohort audit verdict)
[new]lowers_to:
  - book/src/L2/linear_combination.md (the general arity-2 specialization of the firm L3/L2 `linear_combination` fold; `axpby(α,x,β,y) = linear_combination [(α,x),(β,y)]`; lowers via the combinator's §"Downward to L2" identity-in-form edge, then the substantive arity-dispatch is the L2>L1 `linear-combination-fold-specialization` theme) → book/src/L1/axpby.md (transitive L3>L1 identity in-line, the fold-specialization picking the `AXPBY` L0 leaf)
lifts_from:
  - book/src/L3/linear_combination.md (the family combinator this leaf is the general arity-2 specialization of — `axpby` speaks through `linear_combination`, not as a re-derived base form, per the 2026-06-01 vocabulary-shift redirect; no L4 entry — the fold is a pure value-producing reduction, not a calculus combinator)
```

```edit:book/src/L3/axpby.md
[old]# axpby

Whole-tensor fused two-scalar two-vector update at L3: `axpby(α, x, β, y) = α·x + β·y`. The L3-native rendering of the fused BLAS-1 primitive that subsumes [`axpy`](./axpy.md) (β=1) and pure-scaling (α=0), firm at L1 ([`axpby`](../L1/axpby.md)), surfaced here in L3 vocabulary because **each layer is internally coherent** (CLAUDE.md §Methodology invariants).
[new]# axpby

Whole-tensor fused two-scalar two-vector update at L3: `axpby(α, x, β, y) = α·x + β·y` — the **general arity-2 specialization of the [`linear_combination`](./linear_combination.md) fold**: `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms speak **through** the combinator, not as re-derived base forms — `axpby` is the combinator at term-list length 2 with both coefficients free (subsuming [`axpy`](./axpy.md) at the second-coeff-1 reading and pure-scaling at α=0). This chapter is the arity-2 readout label for the bounded-arity L0 call shape (`AXPBY`); its algebra is the fold's law set read at that fixed length, and its lowering routes through the combinator's §"Downward to L2" identity edge + the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme.
```

```edit:book/src/L3/axpby.md
[old]No L4 monadic vocabulary; `axpby` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpby` is **CONFIRMED-NOT-NEEDED** (leaf primitives don't get L4 rows). The adjacent L3>L2 rotation passes through the **present** L2 floor [`axpby`](../L2/axpby.md) (cycle-043) via the firm [`axpby-body-identity`](../L3-L2/axpby-body-identity.md) L3>L2 theme — identity-in-form on the body, no wrapper rotation; onward to L1 [`axpby`](../L1/axpby.md). The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent, per **Identity-lowerings still require both L levels**.
[new]No L4 monadic vocabulary; neither `axpby` nor the `linear_combination` fold it specializes is a calculus combinator at L4 (the cohort audit verdict is **CONFIRMED-NOT-NEEDED**; `L3/linear_combination.md:152-154`). The downward rotation passes through the firm L2 [`linear_combination`](../L2/linear_combination.md) via the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at term-list length 2 (both coefficients free) — `axpby` is the general arity-2 fold member. The substantive arity-dispatch (length → maximal fused L0 leaf, here the `AXPBY` symbol) + the pinned summation order live in the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme, NOT in a per-leaf theme.
```

```edit:book/src/L3/axpby.md
[old]## Lowers to

L3 `axpby` lowers to the **present adjacent L2 floor** [`axpby`](../L2/axpby.md) (cycle-043) as **identity-in-form on the primitive's signature shape**, via the firm [`axpby-body-identity`](../L3-L2/axpby-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `axpby` is a leaf whole-tensor field operation, not a step body), and onward to L1 [`axpby`](../L1/axpby.md). The three surfaces are textually identical modulo layer-coherence vocabulary (L1 / L2 / L3 all see `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` with the same shape contract, the same nine algebraic laws, the same four non-laws, and the same variant-axis profile). The L2 floor is the standalone fold-member BLAS-1 leaf — landed by the cycle-043 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive rotation in the chain is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md).
[new]## Lowers to

L3 `axpby` lowers as the **general arity-2 specialization of [`linear_combination`](./linear_combination.md)** (`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`). The combinator lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the fold body (`L3/linear_combination.md:107-113` §"Downward to L2"). The substantive rotation in the downward chain is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme: it reads the term-list length (here 2, both coefficients free) and selects the maximal fused L0 leaf — the `AXPBY` symbol, realized as MFEM's single aligned `add(α, x, β, y, y)` pass (`palace/linalg/vector.cpp:726-730`) — and records its pinned summation order. All arity dispatch and summation-order residue are the fold-parent's, not this leaf's.

The **transitive** L3>L1 identity (the combinator's L3>L2 identity ∘ the L2>L1 fold-specialization's value-identity at this list length) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive in-place mutation rotation, reached transitively, is the L1>L0 [`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md).
```

```edit:book/src/L3/axpby.md
[old]- `book/src/L2/axpby.md` (cycle-043 firm) — the present adjacent L2 floor this L3 entry lowers into via the `axpby-body-identity` theme; identity-in-form on the primitive's signature.
- `book/src/L3-L2/axpby-body-identity.md` (cycle-043 firm) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation.
- `book/src/L1/axpby.md` (cycle-003 firm) — the L1 form this L3 entry transitively rotates from (L3>L2 ∘ L2>L1). Body shape, semantics, nine algebraic laws, four non-laws, variant-axis profile.
[new]- `book/src/L3/linear_combination.md` (cycle-050 firm) + `book/src/L2/linear_combination.md` (inverted-to-entry cycle-049 D1) — the family combinator this leaf is the general arity-2 specialization of; §"Arity specializations" (`L3/linear_combination.md:50-61`) names `axpby = linear_combination [(α,x),(β,y)]`, §"Downward to L2" (`:107-113`) is the identity-in-form edge this leaf's lowering reads at length 2.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; cycle-049 D1(c) KEEP verdict) — the substantive L2>L1 fusion-selection theme that picks the `AXPBY` L0 leaf at this list-length and records its pinned summation order (the lowering's substantive content, deferred here, not in a per-leaf theme).
- `book/src/L1/axpby.md` (cycle-003 firm) — the L1 leaf the fold-specialization recovers at this arity (the L1>L0 one-to-one `AXPBY` symbol shape). Body shape, semantics, nine algebraic laws, four non-laws, variant-axis profile.
```

**axpby.md's algebraic-laws are a clean mechanical reframe** (the nine laws are the fold's bilinearity / distribution / scalar-absorption laws read at length 2); no substantive rework — in-scope.

#### (b.4) `book/src/L3/axpbypcz.md`

`axpbypcz.md` references `axpbypcz-body-identity` in frontmatter `lowers_to:`, §Dependencies (`:106`), §"Lowers to" (`:125`), and §Evidence (`:138`). Re-route all four.

```edit:book/src/L3/axpbypcz.md
[old]lowers_to:
  - book/src/L2/axpbypcz.md (present adjacent L2 floor, cycle-043 D5; identity-in-form on the primitive's signature shape, via the `axpbypcz-body-identity` L3>L2 theme; whole-tensor in / whole-tensor out at both layers) → book/src/L1/axpbypcz.md (transitive L3>L1 identity in-line, L3>L2 ∘ L2>L1)
lifts_from:
  - (no L4 entry — leaf primitive, not a calculus combinator; per cycle-010 cohort audit verdict)
[new]lowers_to:
  - book/src/L2/linear_combination.md (the arity-3 specialization of the firm L3/L2 `linear_combination` fold; `axpbypcz(α,x,β,y,γ,z) = linear_combination [(α,x),(β,y),(γ,z)]`; lowers via the combinator's §"Downward to L2" identity-in-form edge, then the substantive arity-dispatch is the L2>L1 `linear-combination-fold-specialization` theme) → book/src/L1/axpbypcz.md (transitive L3>L1 identity in-line, the fold-specialization picking the `AXPBYPCZ` L0 leaf incl. the γ==0 arity-collapse)
lifts_from:
  - book/src/L3/linear_combination.md (the family combinator this leaf is the arity-3 specialization of — `axpbypcz` speaks through `linear_combination`, not as a re-derived base form, per the 2026-06-01 vocabulary-shift redirect; no L4 entry — the fold is a pure value-producing reduction, not a calculus combinator)
```

```edit:book/src/L3/axpbypcz.md
[old]# axpbypcz

Whole-tensor fused three-scalar three-vector update at L3: `axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z`. The L3-native rendering of the fused BLAS-1-extended primitive that subsumes [`axpby`](./axpby.md) (γ=0), [`axpy`](./axpy.md) (β=1, γ=0), and pure-scaling (α=0, β=0), firm at L1 ([`axpbypcz`](../L1/axpbypcz.md)), surfaced here in L3 vocabulary because **each layer is internally coherent** (CLAUDE.md §Methodology invariants).
[new]# axpbypcz

Whole-tensor fused three-scalar three-vector update at L3: `axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z` — the **arity-3 specialization of the [`linear_combination`](./linear_combination.md) fold**: `axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]` (CLAUDE.md §Methodology invariants ⟢, the 2026-06-01 vocabulary-shift redirect; `L3/linear_combination.md:50-61` §"Arity specializations"). At L3 and above the four arity forms speak **through** the combinator, not as re-derived base forms — `axpbypcz` is the combinator at term-list length 3 (subsuming [`axpby`](./axpby.md) at γ=0 and [`axpy`](./axpy.md) at β=1, γ=0). This chapter is the arity-3 readout label for the bounded-arity L0 call shape (`AXPBYPCZ`, the top of Palace's bounded-arity surface); its algebra is the fold's law set read at that fixed length, and its lowering routes through the combinator's §"Downward to L2" identity edge + the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme.
```

```edit:book/src/L3/axpbypcz.md
[old]No L4 monadic vocabulary; `axpbypcz` is not a calculus combinator at L4. Per the cycle-010 cohort audit, the L4 candidate for `axpbypcz` is **CONFIRMED-NOT-NEEDED**. The adjacent L3>L2 rotation passes through the **present** L2 floor [`axpbypcz`](../L2/axpbypcz.md) (cycle-043 D5) via the firm [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md) L3>L2 theme — identity-in-form on the body, no wrapper rotation; onward to L1 [`axpbypcz`](../L1/axpbypcz.md). The L2 floor was backfilled under the foundation-first directive `l2-floor-under-l3-leaf-cohort` so the firm L3 entry rests on a *present* adjacent L2 parent, per **Identity-lowerings still require both L levels**.
[new]No L4 monadic vocabulary; neither `axpbypcz` nor the `linear_combination` fold it specializes is a calculus combinator at L4 (the cohort audit verdict is **CONFIRMED-NOT-NEEDED**; `L3/linear_combination.md:152-154`). The downward rotation passes through the firm L2 [`linear_combination`](../L2/linear_combination.md) via the combinator's §"Downward to L2" identity edge (`L3/linear_combination.md:107-113`), read at term-list length 3 — `axpbypcz` is the arity-3 fold member. The substantive arity-dispatch (length → maximal fused L0 leaf, here the `AXPBYPCZ` symbol, including the `γ==0` arity-collapse to `axpby`) + the pinned summation order live in the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme, NOT in a per-leaf theme.
```

```edit:book/src/L3/axpbypcz.md
[old]## Lowers to

L3 `axpbypcz` lowers to the **present adjacent L2 floor** [`axpbypcz`](../L2/axpbypcz.md) (cycle-043 D5) as **identity-in-form on the primitive's signature shape**, via the firm [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md) L3>L2 theme (identity-in-form on the body, no wrapper rotation — `axpbypcz` is a leaf whole-tensor field operation, not a step body), and onward to L1 [`axpbypcz`](../L1/axpbypcz.md). The three surfaces are textually identical modulo layer-coherence vocabulary (L1 / L2 / L3 all see `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` with the same shape contract, the same twelve algebraic laws, the same four non-laws, and the same variant-axis profile). The L2 floor is the standalone fold-member BLAS-1-extended leaf — landed by the cycle-043 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-leaf-cohort` — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

The **transitive** L3>L1 identity (L3>L2 ∘ L2>L1, both identity-in-form) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive rotation in the chain is the L1>L0 [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md).
[new]## Lowers to

L3 `axpbypcz` lowers as the **arity-3 specialization of [`linear_combination`](./linear_combination.md)** (`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`). The combinator lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as identity-in-form on the fold body (`L3/linear_combination.md:107-113` §"Downward to L2"). The substantive rotation in the downward chain is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme: it reads the term-list length (here 3) and selects the maximal fused L0 leaf — the `AXPBYPCZ` symbol, including the `γ == 0` arity-collapse branch (`palace/linalg/vector.cpp:745-758`, the `:749-751` `add(α, x, β, y, z)` fast-path that is the exact algebraic content of the fold's zero-coefficient term-drop law) — and records the pinned summation order of each L0 branch. All arity dispatch and summation-order residue are the fold-parent's, not this leaf's.

The **transitive** L3>L1 identity (the combinator's L3>L2 identity ∘ the L2>L1 fold-specialization's value-identity at this list length) is annotated in-line per the cycle-012 non-adjacent-identity convention; no `book/src/L3-L1/` directory is created. The substantive in-place mutation rotation, reached transitively, is the L1>L0 [`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md).
```

```edit:book/src/L3/axpbypcz.md
[old]- `book/src/L2/axpbypcz.md` (cycle-043 D5 firm) — the present adjacent L2 floor this L3 entry lowers into via the `axpbypcz-body-identity` theme; identity-in-form on the primitive's signature.
- `book/src/L3-L2/axpbypcz-body-identity.md` (cycle-043 firm) — the adjacent L3>L2 body-identity theme; identity-in-form on the body, no wrapper rotation.
- `book/src/L1/axpbypcz.md` (cycle-003 firm) — the L1 form this L3 entry transitively rotates from (L3>L2 ∘ L2>L1). Body shape, semantics, twelve algebraic laws, four non-laws, variant-axis profile.
[new]- `book/src/L3/linear_combination.md` (cycle-050 firm) + `book/src/L2/linear_combination.md` (inverted-to-entry cycle-049 D1) — the family combinator this leaf is the arity-3 specialization of; §"Arity specializations" (`L3/linear_combination.md:50-61`) names `axpbypcz = linear_combination [(α,x),(β,y),(γ,z)]`, §"Downward to L2" (`:107-113`) is the identity-in-form edge this leaf's lowering reads at length 3.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; cycle-049 D1(c) KEEP verdict) — the substantive L2>L1 fusion-selection theme that picks the `AXPBYPCZ` L0 leaf at this list-length, handles the `γ==0` arity-collapse, and records the pinned summation order of each L0 branch (the lowering's substantive content, deferred here, not in a per-leaf theme).
- `book/src/L1/axpbypcz.md` (cycle-003 firm) — the L1 leaf the fold-specialization recovers at this arity (the L1>L0 one-to-one `AXPBYPCZ` symbol shape). Body shape, semantics, twelve algebraic laws, four non-laws, variant-axis profile.
```

**axpbypcz.md's algebraic-laws are a clean mechanical reframe** (the twelve laws are the fold's trilinearity / distribution / scalar-absorption laws read at length 3, plus the subsumption identities that ARE the concatenation law read at length 3); no substantive rework — in-scope.

### (c) Defensive de-link of inbound live links to the deleted slugs (in kept files)

Three kept files carry live links to deleted slugs as analogy references (comparing the constructed-operator gates to the BLAS-1 leaf themes). A live link to a deleted file is a hard `linkcheck2` build error. Per the c050 multi-deletion pattern, convert the link to plain-text (keep the slug name in a code-span as an analogy label; drop the `(...md)` target). Re-pointing at the combinator is NOT appropriate here — these compare the *theme's shape* to the gate's, and the gate-side themes are NOT being demoted; the cleanest bounded de-link is plain-text.

```edit:book/src/L3-L2/jacobi-smoother-body-identity.md
[old]`jacobi-smoother` has no wrapper and no loop. The body IS the identity. This is the
**constructed-operator-gate analogue** of the BLAS-1-leaf [`scal-body-identity`](./scal-body-identity.md)
— a single field operation, no wrapper to rotate — and the thinnest constructed-operator-gate
member of the L3>L2 lowering family.
[new]`jacobi-smoother` has no wrapper and no loop. The body IS the identity. This is the
**constructed-operator-gate analogue** of the BLAS-1 family's identity-in-form edge — a
single field operation, no wrapper to rotate. (The BLAS-1 per-arity `*-body-identity`
themes were demoted cycle-051 D1 into the [`linear_combination`](../L3/linear_combination.md)
combinator's §"Downward to L2" note; this gate is the standalone-gate counterpart of that
identity edge.) It is the thinnest constructed-operator-gate member of the L3>L2 lowering family.
```

```edit:book/src/L3-L2/jacobi-smoother-body-identity.md
[old]This theme is the **constructed-operator-gate counterpart** of the firm
[`scal-body-identity`](./scal-body-identity.md) (cycle-041 D6). The `scal` theme establishes
the pattern "identity-in-form on the body, **no wrapper to rotate** — `scal` is a leaf, not a
step body, so the two wrapper adjustments the `krylov-step` theme carries have no analog";
[new]This theme is the **constructed-operator-gate counterpart** of the BLAS-1 family's
identity-in-form edge (the per-arity `scal`/`axpy`/`axpby`/`axpbypcz` `*-body-identity` themes
demoted cycle-051 D1 into the [`linear_combination`](../L3/linear_combination.md) combinator's
§"Downward to L2" note). That edge establishes the pattern "identity-in-form on the body,
**no wrapper to rotate** — the leaf is not a step body, so the two wrapper adjustments the
`krylov-step` theme carries have no analog";
```

```edit:book/src/L3-L2/divfree-projector-body-identity.md
[old]This is the **constructed-operator-gate** analogue of the cycle-041 BLAS-1-leaf `-body-identity` cohort
([`dot-body-identity`](./dot-body-identity.md) / [`nrm2-body-identity`](./nrm2-body-identity.md) /
[`scal-body-identity`](./scal-body-identity.md)) — but the body is a fixed four-step composition (around
[new]This is the **constructed-operator-gate** analogue of the cycle-041 BLAS-1-leaf `-body-identity` cohort
([`dot-body-identity`](./dot-body-identity.md) / [`nrm2-body-identity`](./nrm2-body-identity.md); the
scalar-weighted-sum members `scal`/`axpy`/`axpby`/`axpbypcz` `*-body-identity` were demoted cycle-051 D1
into the [`linear_combination`](../L3/linear_combination.md) combinator's §"Downward to L2" note) — but the body is a fixed four-step composition (around
```

```edit:book/src/L2-L1/divfree-projector-leaf-identity.md
[old]This is the **standalone-gate** counterpart of the cycle-041 BLAS-1 floor-edge cohort
([`dot-leaf-identity`](./dot-leaf-identity.md) / [`nrm2-leaf-identity`](./nrm2-leaf-identity.md)
/ [`scal-leaf-identity`](./scal-leaf-identity.md)) — but with two structural differences:
[new]This is the **standalone-gate** counterpart of the cycle-041 BLAS-1 floor-edge cohort
([`dot-leaf-identity`](./dot-leaf-identity.md) / [`nrm2-leaf-identity`](./nrm2-leaf-identity.md);
the scalar-weighted-sum members `scal`/`axpy`/`axpby`/`axpbypcz` `*-leaf-identity` were demoted
cycle-051 D1, their L2>L1 edge absorbed into the [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md)
fold-parent) — but with two structural differences:
```

### (e) Bounded prose-correction in the combinator home (stale "scheduled at cycle-051" phrasing)

The c050-authored `L3/linear_combination.md` §"Downward to L2" still phrases the demotion as future-tense ("scheduled to demote into this in-line note at cycle-051", "once the L3 leaves are re-expressed through this combinator (cycle-051)"). With this dispatch landing, the demotion is done. Bounded prose-correction (a stale claim about scheduling, directly contradicted by this dispatch's own deletions; recorded in §Discipline notes). Also re-points the §111 live link to the now-deleted `axpy-body-identity` (a hard build error if left).

```edit:book/src/L3/linear_combination.md
[old]This identity is the family-entry analog of the four `{scal,axpy,axpby,axpbypcz}-body-identity` L3>L2 themes — each of which currently records the same "the body IS the identity, no wrapper rotation" verdict for its individual arity leaf (e.g. [`axpy-body-identity`](../L3-L2/axpy-body-identity.md):3-14, "The body IS the identity … `axpy` has no wrapper"). Under the cycle-049 replace-and-propagate map (b.2), those four thin per-leaf themes are degenerate identity-in-named-terms smells **scheduled to demote into this in-line note at cycle-051**: once the L3 leaves are re-expressed through this combinator (cycle-051), the four `*-body-identity` themes have no standalone leaf body to lower and collapse into this single §"Downward to L2" combinator-identity note. This note is written to accommodate that demotion — it is the pre-built home for the four leaf-edge identities, which are the concatenation-law specializations of this one combinator identity (the arity-1/2/2/3 readings of `linear_combination`'s body-identity).
[new]This identity is the family-entry analog of the four `{scal,axpy,axpby,axpbypcz}-body-identity` L3>L2 themes — each of which recorded the same "the body IS the identity, no wrapper rotation" verdict for its individual arity leaf. Under the cycle-049 replace-and-propagate map (b.2), those four thin per-leaf themes were degenerate identity-in-named-terms smells (the §1d smell — the vocabulary did not shift, LHS and RHS being the same named operator at the same arity); they were **demoted cycle-051 D1** into this single §"Downward to L2" combinator-identity note, with the four L3 leaves (`L3/{scal,axpy,axpby,axpbypcz}.md`) re-expressed to speak through this combinator as arity-1/2/2/3 specializations. This note is the home for the four leaf-edge identities, which are the concatenation-law specializations of this one combinator identity (the arity-1/2/2/3 readings of `linear_combination`'s body-identity).
```

The same §Dependencies / §"Arity specializations" / §Status / §Evidence passages in `L3/linear_combination.md` that say "still exist firm as of this cycle / their collapse into these notes is cycle-051 (gated …)" are forward-references that this dispatch resolves; they are bounded prose-corrections (future-tense → past-tense) but are NOT dead-link errors. Flagged for D5/integrator: see §Open questions — these are tense-only touches, deferrable to a follow-up sweep if D1's edit budget is a concern, since they are not build-breaking. Listed here for completeness but NOT applied in this report's fences to keep the single-writer surface bounded to build-correctness + the §111 dead-link.

### (d) Remove D1's OWN SUMMARY.md lines + dep-map ROWS (TALLY DEFERRED to D5)

#### SUMMARY.md — the 8 deleted-theme lines (remove only these 8; leave the running counts to D5)

```edit:book/src/SUMMARY.md
[old]- [axpy-body-identity](./L3-L2/axpy-body-identity.md)
- [axpby-body-identity](./L3-L2/axpby-body-identity.md)
- [axpbypcz-body-identity](./L3-L2/axpbypcz-body-identity.md)
- [nrm2-body-identity](./L3-L2/nrm2-body-identity.md)
- [ksp-solve-outer-driver](./L3-L2/ksp-solve-outer-driver.md)
- [scal-body-identity](./L3-L2/scal-body-identity.md)
- [jacobi-smoother-body-identity](./L3-L2/jacobi-smoother-body-identity.md)
[new]- [nrm2-body-identity](./L3-L2/nrm2-body-identity.md)
- [ksp-solve-outer-driver](./L3-L2/ksp-solve-outer-driver.md)
- [jacobi-smoother-body-identity](./L3-L2/jacobi-smoother-body-identity.md)
```

```edit:book/src/SUMMARY.md
[old]- [scal-leaf-identity](./L2-L1/scal-leaf-identity.md)
- [inner-product-fold-specialization](./L2-L1/inner-product-fold-specialization.md)
- [dot-leaf-identity](./L2-L1/dot-leaf-identity.md)
- [axpy-leaf-identity](./L2-L1/axpy-leaf-identity.md)
- [axpby-leaf-identity](./L2-L1/axpby-leaf-identity.md)
- [axpbypcz-leaf-identity](./L2-L1/axpbypcz-leaf-identity.md)
- [nrm2-leaf-identity](./L2-L1/nrm2-leaf-identity.md)
[new]- [inner-product-fold-specialization](./L2-L1/inner-product-fold-specialization.md)
- [dot-leaf-identity](./L2-L1/dot-leaf-identity.md)
- [nrm2-leaf-identity](./L2-L1/nrm2-leaf-identity.md)
```

#### book/src/L3-L2/index.md — remove D1's 4 dep-map rows (rows 17–20; leave counts/tally to D5)

```edit:book/src/L3-L2/index.md
[old]| [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) | L3 [`ksp_solve`](../L3/ksp_solve.md) §Signature — the value-threaded outer-driver fold `(op, K_0, s_0) -> (s_final, result)` rendered as an **explicit `iterate_while_L3` tail recursion** over [`krylov-step`](../L3/krylov-step.md), carrying the first-class **outer-loop `sequential-obstruction`**. | L2 [`ksp_solve`](../L2/ksp_solve.md) §Signature — the **outer-driver-by-role** composition `(K, b) -> SolveResult` with body = `iterate_while (krylov-step op) s_init predicate` (iteration view erased; obstruction shadows to the §"Algebraic laws" non-mergeability / no-fold-lift non-laws). | `structural` (the iteration-view erasure + obstruction-to-non-law shadow is a layer-surface-shape fact) + secondary `reduction-chain` (the `iterate_while_L3` → `iterate_while`-by-role consolidation re-folds the strawman §3.7 reduction sequence) | `firm` (cycle-021 wave-2 abstractor; the **substantive / non-identity** driver complement of the kernel-body identity theme — `kernel-identity + driver-non-identity = the full per-solver L3>L2 story`) |
| [`scal-body-identity`](./scal-body-identity.md) | L3 [`scal`](../L3/scal.md) §Signature — the whole-tensor field operation `scal :: Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`scal`](../L2/scal.md) §Signature — the base scalar-vector-multiply floor leaf (arity-1 member of `linear_combination`, cited NOT merged); identical signature. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-041 D6 abstractor; identity-in-form on the body, **no wrapper to rotate** — the leaf-primitive counterpart of `krylov-step-body-identity`) |
| [`axpy-body-identity`](./axpy-body-identity.md) | L3 [`axpy`](../L3/axpy.md) §Signature — the whole-tensor fused field operation `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`axpy`](../L2/axpy.md) §Signature — the base scalar-vector-update floor leaf (arity-2 member of `linear_combination`, second coeff fixed to 1, cited NOT merged); identical signature + six laws. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf; **fold-member but all fusion is the fold-parent's**) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-043 D6 abstractor; identity-in-form on the body, **no wrapper to rotate** — the arity-2-fold-member counterpart of the arity-1 `scal-body-identity`) |
| [`axpby-body-identity`](./axpby-body-identity.md) | L3 [`axpby`](../L3/axpby.md) §Signature — the whole-tensor fused two-scalar two-vector field operation `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`axpby`](../L2/axpby.md) §Signature — the base fused-linear-combination floor leaf (arity-2 member of `linear_combination`, cited NOT merged); identical signature. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf; `krylov-step-body-identity.md:97` names `axpby` among the seven L3-native primitives) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-043 D7 abstractor; identity-in-form on the body, **no wrapper to rotate** — the arity-2 leaf-primitive counterpart of `krylov-step-body-identity` alongside `scal-body-identity`; rides the batch-12 leaf-vs-fold fork, c042 audit recommends keeping leaf-floor (b)) |
| [`axpbypcz-body-identity`](./axpbypcz-body-identity.md) | L3 [`axpbypcz`](../L3/axpbypcz.md) §Signature — the whole-tensor fused three-term field operation `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction** (per-element fused combination, embarrassingly parallel). | L2 [`axpbypcz`](../L2/axpbypcz.md) §Signature — the base fused three-term linear-combination floor leaf (arity-3 member of `linear_combination`, cited NOT merged); identical six-arg signature. | `structural` (whole-tensor six-arg signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf, which names `axpbypcz` L3-native at `:97`) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-043 D8 abstractor; identity-in-form on the body, **no wrapper to rotate** — the arity-3 fold-member counterpart of the arity-1 `scal-body-identity`, both leaf members of the `linear_combination` fold) |
[new]| [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) | L3 [`ksp_solve`](../L3/ksp_solve.md) §Signature — the value-threaded outer-driver fold `(op, K_0, s_0) -> (s_final, result)` rendered as an **explicit `iterate_while_L3` tail recursion** over [`krylov-step`](../L3/krylov-step.md), carrying the first-class **outer-loop `sequential-obstruction`**. | L2 [`ksp_solve`](../L2/ksp_solve.md) §Signature — the **outer-driver-by-role** composition `(K, b) -> SolveResult` with body = `iterate_while (krylov-step op) s_init predicate` (iteration view erased; obstruction shadows to the §"Algebraic laws" non-mergeability / no-fold-lift non-laws). | `structural` (the iteration-view erasure + obstruction-to-non-law shadow is a layer-surface-shape fact) + secondary `reduction-chain` (the `iterate_while_L3` → `iterate_while`-by-role consolidation re-folds the strawman §3.7 reduction sequence) | `firm` (cycle-021 wave-2 abstractor; the **substantive / non-identity** driver complement of the kernel-body identity theme — `kernel-identity + driver-non-identity = the full per-solver L3>L2 story`) |
```

#### book/src/L2-L1/index.md — remove D1's 4 dep-map rows (scal/axpy/axpby/axpbypcz-leaf-identity; leave row 14 `linear-combination-fold-specialization` + counts/tally to D5)

```edit:book/src/L2-L1/index.md
[old]| [scal-leaf-identity](./scal-leaf-identity.md) | `L2/scal` (firm, cycle-041 D3) | `L1/scal` (firm leaf, cycle-004) | firm *(structural; identity-in-form floor edge — the degenerate arity-1 single-term shadow of `linear-combination-fold-specialization`; no arity dispatch, no pinned-summation-order residue (one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged; renamed cycle-043 from `scal-fold-specialization`)* |
| [inner-product-fold-specialization](./inner-product-fold-specialization.md) | `L2/inner_product` (firm) | `L1/dot` (firm; `dot` + `tdot`) + `L1/bilinear-form` (rough-in, M-weighted member) | firm *(algebraic; conjugation-convention / element-type / weight dispatch + value-level `xᴴ y`↔`yᴴ x` conjugate-pair re-order + pinned reduction tree)* |
| [dot-leaf-identity](./dot-leaf-identity.md) | `L2/dot` (firm, cycle-041 leaf-floor) | `L1/dot` (firm; `dot` + `tdot`) | firm *(structural; identity-in-form on the inner-product leaf — value-thread-isomorphic signature; all L2-layer fusion deferred to the fold-parent `inner-product-fold-specialization`; thin floor-edge of the BLAS-1 leaf)* |
| [axpy-leaf-identity](./axpy-leaf-identity.md) | `L2/axpy` (firm, cycle-043 D3 floor) | `L1/axpy` (firm leaf, cycle-002) | firm *(structural; identity-in-form on the arity-2 scalar-vector fused-update leaf — value-thread-isomorphic signature `Scalar -> T[N] -> T[N] -> T[N]` + six laws + fold-specialization identity (`axpy(α,x,y) = linear_combination [(α,x),(1,y)]`, second coeff fixed to 1, cited NOT merged); arity-2 shadow of `linear-combination-fold-specialization` — all fusion (arity-dispatch + summation-order table) deferred to that fold-parent, no leaf-unique surplus; IEEE summation non-law present (arity-2 computes a sum) but it is the fold's residue carried family-wide; sibling of arity-1 `scal-leaf-identity`; leaf-vs-fold fork resolved keep-(b))* |
| [axpby-leaf-identity](./axpby-leaf-identity.md) | `L2/axpby` (firming, cycle-043 D4 floor) | `L1/axpby` (firm leaf, cycle-003) | firm *(structural; identity-in-form floor edge — the **arity-2 member** of `linear-combination-fold-specialization` (cited NOT merged); thicker than `scal-leaf-identity` (its arity-2 fused `add(α,x,β,y,y)` pass IS a two-term sum, so the summation-order non-law is non-degenerate), thinner than the fold-parent (no arity dispatch — one fixed arity); single fusion note (the arity-2 single-aligned pass) is the fold's §"Fusion note", deferred there; output-aliasing axis is the FOLD's; rides the batch-12 leaf-vs-fold fork (c042 audit recommends keeping leaf-floor (b)))* |
| [axpbypcz-leaf-identity](./axpbypcz-leaf-identity.md) | `L2/axpbypcz` (firm, cycle-043 D5 leaf-floor) | `L1/axpbypcz` (firm leaf, cycle-003) | firm *(structural; identity-in-form on the fused arity-3 three-term linear-combination leaf — value-thread-isomorphic six-arg signature + twelve laws + four non-laws + two variant axes; the **arity-3 fold-member analogue** of `scal-leaf-identity` (arity-1) — all L2-layer fusion (the single-aligned `add(α,x,β,y,z)` pass + the `γ==0` arity-collapse + pinned summation order) deferred to the fold-parent `linear-combination-fold-specialization`; output-aliasing axis is the fold's; four IEEE/fusion non-laws preserved-through-the-edge NOT erased; slug `-leaf-identity` per the cycle-042 ratified convention; leaf-floor reading (b) per the batch-12-resolved `dot-l2-leaf-floor-vs-fold-only-design` fork, recommended KEEP-(b) by the cycle-042 cross-cutter audit)* |
[new]| [inner-product-fold-specialization](./inner-product-fold-specialization.md) | `L2/inner_product` (firm) | `L1/dot` (firm; `dot` + `tdot`) + `L1/bilinear-form` (rough-in, M-weighted member) | firm *(algebraic; conjugation-convention / element-type / weight dispatch + value-level `xᴴ y`↔`yᴴ x` conjugate-pair re-order + pinned reduction tree)* |
| [dot-leaf-identity](./dot-leaf-identity.md) | `L2/dot` (firm, cycle-041 leaf-floor) | `L1/dot` (firm; `dot` + `tdot`) | firm *(structural; identity-in-form on the inner-product leaf — value-thread-isomorphic signature; all L2-layer fusion deferred to the fold-parent `inner-product-fold-specialization`; thin floor-edge of the BLAS-1 leaf)* |
```

Note on the L2-L1 index: the four scalar-weighted-sum `*-leaf-identity` rows (15, 18, 19, 20) are non-contiguous (rows 16/17 are the KEPT `inner-product-fold-specialization` + `dot-leaf-identity` for the *other* fold). The edit above removes row 15 and rows 18–20 in one block by re-emitting rows 16–17 with rows 15/18/19/20 dropped; row 14 (`linear-combination-fold-specialization`, KEPT) and row 21+ (`nrm2`/`jacobi`/…) are untouched.

### (f) Re-point the 3 stale live links in `book/src/L3/index.md` dep-map rows (axpy/axpby/axpbypcz)

`book/src/L3/index.md` rows 24/25/26 (the `axpy`/`axpby`/`axpbypcz` dep-map rows) each carry TWO live links to a now-deleted `*-body-identity` slug — one in the §Dependencies column, one in the §"Lowers to" column (six live links total). With change (a) deleting those theme files, all six become hard `linkcheck2` build errors. Re-point each to the combinator route — the same re-expression the (b) leaf edits apply: the L3>L2 hop is the [`linear_combination`](./linear_combination.md) combinator's §"Downward to L2" identity-in-form edge (no per-leaf body-identity theme), and the substantive rotation is the KEPT L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme. The `scal` row (row 30) carries NO `scal-body-identity` link (it links L1 `scal` directly via the in-line identity-in-form note), so it needs no change. These are D1's own leaves' per-row content; the consolidated tally rows D5 owns are untouched.

```edit:book/src/L3/index.md
[old]| [`axpy`](./axpy.md) | `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, y) -> α·x + y`) | L2 floor [`axpy`](../L2/axpy.md) (present adjacent floor, cycle-043) via [`axpy-body-identity`](../L3-L2/axpy-body-identity.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). | L2 [`axpy`](../L2/axpy.md) via [`axpy-body-identity`](../L3-L2/axpy-body-identity.md) (identity-in-form on the body, no wrapper rotation), then transitively L1 [`axpy`](../L1/axpy.md) (L3>L2 ∘ L2>L1 identity in-line; no `L3-L1/` directory). | `firm` (harvested cycle-011T234525Z; identity-lowering backfill per CLAUDE.md §Methodology invariants; re-anchored cycle-044 to the present L2 floor landed cycle-043 under `l2-floor-under-l3-leaf-cohort`; closes cohort portion of OQ `l3-backfill-apply-linop-and-blas1-cohort` HIGH CONFIDENCE) |
[new]| [`axpy`](./axpy.md) | `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, y) -> α·x + y`) | L3 family combinator [`linear_combination`](./linear_combination.md) (this leaf is its arity-2 specialization, second coeff fixed to 1; `axpy(α,x,y) = linear_combination [(α,x),(1,y)]`); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). | L2 [`linear_combination`](../L2/linear_combination.md) via the combinator's §"Downward to L2" identity-in-form edge (read at term-list length 2, trailing coeff 1; no per-leaf body-identity theme — demoted cycle-051 D1), then the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) (picks the `AXPY` L0 leaf + records its pinned summation order); transitively L1 [`axpy`](../L1/axpy.md) in-line (no `L3-L1/` directory). | `firm` (harvested cycle-011T234525Z; identity-lowering backfill per CLAUDE.md §Methodology invariants; re-anchored cycle-044 to the present L2 floor landed cycle-043 under `l2-floor-under-l3-leaf-cohort`; re-expressed cycle-051 D1 through the `linear_combination` combinator per the 2026-06-01 vocabulary-shift redirect; closes cohort portion of OQ `l3-backfill-apply-linop-and-blas1-cohort` HIGH CONFIDENCE) |
```

```edit:book/src/L3/index.md
[old]| [`axpby`](./axpby.md) | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y) -> α·x + β·y`) | L2 floor [`axpby`](../L2/axpby.md) (present adjacent floor, cycle-043) via [`axpby-body-identity`](../L3-L2/axpby-body-identity.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpy`](./axpy.md) at L3 (β=1) — same subsumption-as-identity discipline as L1. | L2 [`axpby`](../L2/axpby.md) via [`axpby-body-identity`](../L3-L2/axpby-body-identity.md) (identity-in-form on the body, no wrapper rotation), then transitively L1 [`axpby`](../L1/axpby.md) (L3>L2 ∘ L2>L1 identity in-line; no `L3-L1/` directory). | `firm` (harvested cycle-011T234525Z; identity-lowering backfill; re-anchored cycle-044 to the present L2 floor landed cycle-043 under `l2-floor-under-l3-leaf-cohort`) |
[new]| [`axpby`](./axpby.md) | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y) -> α·x + β·y`) | L3 family combinator [`linear_combination`](./linear_combination.md) (this leaf is its general arity-2 specialization; `axpby(α,x,β,y) = linear_combination [(α,x),(β,y)]`); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpy`](./axpy.md) at L3 (β=1) — same subsumption-as-identity discipline as L1. | L2 [`linear_combination`](../L2/linear_combination.md) via the combinator's §"Downward to L2" identity-in-form edge (read at term-list length 2, both coeffs free; no per-leaf body-identity theme — demoted cycle-051 D1), then the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) (picks the `AXPBY` L0 leaf + records its pinned summation order); transitively L1 [`axpby`](../L1/axpby.md) in-line (no `L3-L1/` directory). | `firm` (harvested cycle-011T234525Z; identity-lowering backfill; re-anchored cycle-044 to the present L2 floor landed cycle-043 under `l2-floor-under-l3-leaf-cohort`; re-expressed cycle-051 D1 through the `linear_combination` combinator per the 2026-06-01 vocabulary-shift redirect) |
```

```edit:book/src/L3/index.md
[old]| [`axpbypcz`](./axpbypcz.md) | `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y, γ, z) -> α·x + β·y + γ·z`) | L2 floor [`axpbypcz`](../L2/axpbypcz.md) (present adjacent floor, cycle-043 D5) via [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpby`](./axpby.md) at L3 (γ=0) and [`axpy`](./axpy.md) (β=1, γ=0) — same subsumption-as-identity discipline as L1. | L2 [`axpbypcz`](../L2/axpbypcz.md) via [`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md) (identity-in-form on the body, no wrapper rotation), then transitively L1 [`axpbypcz`](../L1/axpbypcz.md) (L3>L2 ∘ L2>L1 identity in-line; no `L3-L1/` directory). | `firm` (harvested cycle-011T234525Z; identity-lowering backfill; re-anchored cycle-044 to the present L2 floor landed cycle-043 under `l2-floor-under-l3-leaf-cohort`) |
[new]| [`axpbypcz`](./axpbypcz.md) | `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (whole-tensor; `(α, x, β, y, γ, z) -> α·x + β·y + γ·z`) | L3 family combinator [`linear_combination`](./linear_combination.md) (this leaf is its arity-3 specialization; `axpbypcz(α,x,β,y,γ,z) = linear_combination [(α,x),(β,y),(γ,z)]`); concepts: [`scalar-promotion`](../concepts/scalar-promotion.md), [`tensor-field-lift`](../concepts/tensor-field-lift.md). Subsumes [`axpby`](./axpby.md) at L3 (γ=0) and [`axpy`](./axpy.md) (β=1, γ=0) — same subsumption-as-identity discipline as L1. | L2 [`linear_combination`](../L2/linear_combination.md) via the combinator's §"Downward to L2" identity-in-form edge (read at term-list length 3; no per-leaf body-identity theme — demoted cycle-051 D1), then the substantive L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) (picks the `AXPBYPCZ` L0 leaf incl. the `γ==0` arity-collapse + records pinned summation order); transitively L1 [`axpbypcz`](../L1/axpbypcz.md) in-line (no `L3-L1/` directory). | `firm` (harvested cycle-011T234525Z; identity-lowering backfill; re-anchored cycle-044 to the present L2 floor landed cycle-043 under `l2-floor-under-l3-leaf-cohort`; re-expressed cycle-051 D1 through the `linear_combination` combinator per the 2026-06-01 vocabulary-shift redirect) |
```

## Discipline notes

- **What changed and why.** Eight `*-body-identity` (L3>L2) and `*-leaf-identity` (L2>L1) themes for the `linear_combination` arity family are degenerate identity-in-named-terms lowerings (the §1d smell per the 2026-06-01 vocabulary-shift redirect): each self-describes its LHS and RHS as the same named operator at the same arity, "the body IS the identity", "no wrapper to rotate", "all fusion deferred to the fold-parent". Per the redirect (degenerate identity-lowerings are resolved as in-line notes / combinator re-expression, NOT mirrored entries + thin themes), they are deleted and their content absorbed into the pre-built combinator homes. The four L3 leaves are re-expressed to speak THROUGH `L3/linear_combination` as arity-1/2/2/3 specializations (the propagate half of the cycle-049 replace-and-propagate map), routing their lowering through the combinator's §"Downward to L2" identity edge + the KEPT substantive `L2-L1/linear-combination-fold-specialization` theme.
- **High→low discipline preserved.** The re-expressed L3 leaves are defined in L3 vocabulary (the arity-N fold specialization), NOT in terms of an L1/L0 base-form re-derivation. The prose narrates the rewrite forward (L3 → L2 → L1). No reverse-direction (L1 lifts up to L3) content was introduced into the chapter bodies; the "value-thread-isomorphic"/lift framing was replaced with the combinator-membership framing.
- **Bounded prose-correction (recorded per CLAUDE.md lifter §L0-evidence-driven prose correction).** Two corrections: (1) the c050 `L3/linear_combination.md:111` "scheduled to demote at cycle-051 / once the L3 leaves are re-expressed (cycle-051)" future-tense phrasing is corrected to past-tense, directly contradicted by this dispatch's own deletions (the demotion is now done). This also resolves the §111 live link to the now-deleted `axpy-body-identity.md` (a hard build error if left). (2) The defensive de-links in (c) add a one-clause "demoted cycle-051 D1" note where they drop the dead link. Both are bounded (tense / dead-link fixes, no decomposition or signature change) and evidenced (this dispatch's own deletion set). NOT applied: the other stale future-tense passages in `L3/linear_combination.md` §"Arity specializations"/§Status/§Dependencies/§Evidence ("still exist firm as of this cycle", "collapse … is cycle-051 (gated …)") — these are non-build-breaking tense touches; flagged in Open questions for a follow-up sweep rather than expanding D1's single-writer surface (they do not break the build because they are prose, not live links).
- **Citation self-verification.** The two new L0 anchors I introduced into the re-expressed leaves' §"Lowers to"/§Evidence — `vector.cpp:702-712` (`AXPY` `α==1.0` fast-path) and `vector.cpp:745-758` incl. `:749-751` (`AXPBYPCZ` `γ==0` branch) — were verified with `tools/citecheck/citecheck.py --anchor`: both pass (`AXPY` at line 702 in 702-712; `AXPBYPCZ` at line 746 in 745-758). The `vector.cpp:726-730` (`AXPBY` real-real `add(α,x,β,y,y)`) anchor is carried verbatim from the deleted `axpby-leaf-identity` and the L2 combinator home (`L2/linear_combination.md:273`), not freshly localized. All L0 anchors remain inherited-via-the-firm-L1/L2-endpoints (the propagate half is an in-layer rendering; no re-localization claimed).
- **Cross-reference to the harvester/combinator-miner reports that promoted the operators.** The L3 combinator home was authored by harvester cycle-050 D1 (`reports/2026-06-01T195100Z-...` per `L3/linear_combination.md:174`); the L2 home was inverted-to-entry cycle-049 D1 (commit `92327f7`); the replace-and-propagate map is combinator-miner cycle-049 (`reports/2026-06-01T190900Z-combinator-miner-refactor-pass-linear-combination-family/CYCLE.md` (b.2) demote half, (b.3) propagate half).

## Supporting evidence

- Pre-built combinator homes (the absorption targets): `book/src/L3/linear_combination.md` §"Arity specializations" (`:50-61`), §"Downward to L2" (`:107-113`), §"Algebraic laws" (`:79-105`); `book/src/L2/linear_combination.md` §"Arity specializations" (`:74-99`), §Dependencies (`:213-238`), §"Fusion note" (`:269-280`).
- KEPT substantive theme (the lowering home the re-expressed leaves reference): `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; the arity-dispatch + pinned-summation-order translation).
- The 8 deleted themes' self-descriptions of the §1d smell: `scal-body-identity.md:3-11` ("The body IS the identity"), `axpy-body-identity.md:3-13`, `axpby-body-identity.md:1-15`, `axpbypcz-body-identity.md:1-12`, `scal-leaf-identity.md:1-18`, `axpy-leaf-identity.md:1-16`, `axpby-leaf-identity.md:1-15`, `axpbypcz-leaf-identity.md:1-15`.
- L0 anchors verified this pass: `reference/palace/palace/linalg/vector.cpp:702-712` (`AXPY`, citecheck `--anchor` OK), `reference/palace/palace/linalg/vector.cpp:745-758` (`AXPBYPCZ`, citecheck `--anchor` OK).

## Open questions / caveats

- **Residual stale future-tense phrasing in `L3/linear_combination.md` (NOT applied by D1).** §"Arity specializations" (`:50-61`: "The standalone L3 leaf chapters … still exist firm as of this cycle — their collapse into these notes is cycle-051 (gated …)"), §Context (`:26`: "that is cycle-051, gated …"), §Status (`:150`), §Dependencies (`:117`), §Lifts-from (`:154`), and §Evidence (`:162`: "the cycle-051 demotion of (one of the four `*-body-identity` themes)") all phrase the demotion as scheduled/gated future work. With D1 landing, these are now past-tense facts. They are **non-build-breaking** (prose, not live links — the only live-link error was `:111`, fixed in (e)). I left them for a bounded follow-up tense-sweep rather than expanding D1's single-writer edit surface on the combinator home (which D1 is otherwise NOT authoring — the home is firm and pre-built). Flag for the integrator/D5 or a batch-16 cleanup: decide whether to fold these tense touches into D5's tally pass on the indexes or a dedicated micro-sweep.
- **`L3/linear_combination.md` §"Arity specializations" (`:61`) and §Dependencies (`:117`) also assert the L3 leaves "stand firm as of this cycle / their re-expression … is cycle-051".** After D1 the leaves DO still stand firm — they are re-expressed THROUGH the combinator, not deleted (the scope deletes only the 8 themes, not the 4 leaves). So "stand firm" remains true; only the "scheduled re-expression" tense is stale. No contradiction with D1's deliverable.
- **No L4 propagation in scope.** The cycle-049 map's (b.4) low-priority L4-propagation (expressing the `krylov-step` update group through `linear_combination`) is explicitly out of this dispatch and remains flagged-not-forced (`L3/linear_combination.md:152-154`).
- **Algebraic-laws reframe judged mechanical for all four leaves.** Each leaf's law set is the combinator's multilinearity / concatenation / coefficient-scaling laws read at a fixed list length (scal: length 1; axpy: length 2, trailing coeff 1; axpby: length 2 general; axpbypcz: length 3). No leaf needed substantive law rework, so none was carried to batch-16. The leaf §Algebraic-laws section bodies are left intact (they are correct as the fixed-arity reading); only the framing sentences ("inherited verbatim from L1") could optionally be reframed as "the fold's law set read at length N" — I did NOT edit those law-section bodies, to keep the change bounded to the lowering-route re-anchor (the dead-`*-body-identity`-link cleanup + combinator framing). If the critic wants the law-section framing sentences reframed too, that is a clean mechanical follow-up, not a substantive rework.
