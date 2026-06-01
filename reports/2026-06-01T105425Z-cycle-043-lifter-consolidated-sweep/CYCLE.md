---
agent: lifter
invoked_at: 2026-06-01T105425Z
scope: cycle-043 D1 — consolidated floor-cohort stale-L3 sweep + 2 citation fixes + 3 slug renames (batch-12 meta decisions 2+4)
status: pending
inputs:
  - book/src/L3/reciprocal.md
  - book/src/L3/assemble-diagonal.md
  - book/src/L3/jacobi-smoother.md
  - book/src/L3/divfree-projector.md
  - book/src/L3/elementwise_product.md
  - book/src/L1/assemble-diagonal.md
  - book/src/L3/index.md
  - book/src/L2/reciprocal.md (now-present adjacent floor)
  - book/src/L2/assemble-diagonal.md
  - book/src/L2/jacobi-smoother.md
  - book/src/L2/divfree-projector.md
  - book/src/L3-L2/reciprocal-body-identity.md
  - book/src/L3-L2/assemble-diagonal-body-identity.md
  - book/src/L3-L2/jacobi-smoother-body-identity.md
  - book/src/L3-L2/divfree-projector-body-identity.md
  - book/src/L2-L1/nrm2-fold-specialization.md (→ nrm2-leaf-identity)
  - book/src/L2-L1/scal-fold-specialization.md (→ scal-leaf-identity)
  - book/src/L3-L2/elementwise_product-body-identity.md (→ elementwise-product-body-identity)
  - reference/palace/palace/linalg/rap.cpp
integrated_at: 2026-06-01T140000Z
integration_commit: 3f9a7d0
integration_notes: "cycle-043 batch integration (cohort-completing L2-floor build); D1 consolidated lifter sweep — 4 stale c042-cohort firm L3 entries re-anchored L3>L1->L3>L2>L1 (closing l3-divfree-projector-stale-no-interposed-l2-entry-lifter-reanchor) + 3 theme-slug git-mv renames + B1/B2 citation-drift fixes; ~62 proposed-changes blocks applied clean; see reports/2026-06-01T140000Z-integrator-finalize-cycle-43/CYCLE.md + cycle-043 STAGING row."
---

# CYCLE: Re-anchor cycle-043 floor-cohort stale-L3 sweep + slug renames

## Summary

When cycle-042 landed the five same-named L2 floors (`reciprocal`, `assemble-diagonal`,
`jacobi-smoother`, `divfree-projector`, `elementwise_product`) plus their matching
`*-body-identity` L3>L2 themes, four firm L3 entries' "no interposed L2 entry / no L3-L2
theme / direct L3>L1 hop" assertions went stale — those entries now lower through a
**present adjacent L2 floor** via an L3>L2 `*-body-identity` theme, exactly as the already-
reconciled `elementwise_product` L3 entry was fixed inline (c042 D3). This dispatch does three
coordinated jobs, all **pure re-anchoring / rename** (the lowering STRUCTURE stays identity-in-
form; only stale vocabulary / citations / slugs firm up):

- **(A)** Re-anchor the two stale clauses in each of `reciprocal`, `assemble-diagonal`,
  `jacobi-smoother`, `divfree-projector` (and one residual `scal`-gloss staleness at
  `elementwise_product.md:166`) to the now-present L2 floor + `*-body-identity` theme. The
  L3>L2 edge stays identity-in-form; the substantive rotation is unchanged (L1>L0). The
  cycle-012 non-adjacent-identity convention nuance is preserved — only the
  there-is-no-adjacent-L2-floor clauses change; the in-line annotation framing for any
  *non-adjacent* (L3>L1) transitive identity stays.
- **(B)** Two drifted-citation fixes: `L1/assemble-diagonal.md:111` `AbsMultTranspose` `:172`→`:174`
  (citecheck-confirmed); `L3/index.md` three self-citations `:39`→`:46` (the cycle-036 D2 (A)
  classification line moved; citecheck-confirmed `:46`).
- **(C)** Three ratified slug renames (`-fold-specialization`→`-leaf-identity`;
  underscore→hyphen on the elementwise body-identity theme) + all cross-reference rewrites.

All citation/anchor checks pass (evidence pasted in §Supporting evidence). The L3>L2 themes,
L2 floors, and new-slug rename targets were all verified on-disk.

**Write mode.** Per `.claude/agents/lifter.md` §Discipline (first bullet) I am a DISPATCH-phase
agent: I emit proposed-changes blocks and `git mv` directives below; `integrator-per-report`
applies them in Phase 5. I do **not** mutate `book/` or run `git mv` myself. (The dispatch
prompt's "OR apply directly" is resolved by the role spec to the proposed-changes channel.)

---

## Proposed changes

### (A) Re-anchor 4 stale L3 entries to the present adjacent L2 floor + `*-body-identity` theme

#### A1 — `book/src/L3/reciprocal.md` (5 sites)

```edit:book/src/L3/reciprocal.md
[old]: lowers_to:
  - book/src/L1/reciprocal.md (identity-in-form on the primitive's signature; no L3-L2 entry, no L3-L1 theme — identity rotation noted in-line at "Lowers to")
[new]: lowers_to:
  - book/src/L2/reciprocal.md (identity-in-form on the primitive's signature; lowers through the present adjacent L2 floor via the `reciprocal-body-identity` L3>L2 theme — see "Lowers to")
```

```edit:book/src/L3/reciprocal.md
[old]: - **Downward** to L1: the L3 form's signature `Tensor[N] -> Tensor[N]` is textually identical to the L1 form's signature; both forms describe pure-functional elementwise reciprocation with no destination buffer in the signature, no per-element loop visible, no reduction, no MPI collective at the L1 / L3 surface. The L3 → L1 rotation is the identity on the primitive itself. The framing differs: L1 frames `reciprocal` as the *mutation-rotation* image of the L0 receiver-self-overwriting `mfem::Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method idiom (the L1 surface drops the receiver-mutation mention); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. **The body of `reciprocal` is the identity rotation across this edge.** There is **no interposed L2 entry and no `L3-L2`/`L3-L1` theme file** — the rotation carries no algebraic novelty, mirroring the BLAS-1 / `apply_linop` / `assemble-diagonal` L3>L1 discipline. The identity-in-form annotation lives in-line here, per the cycle-012 non-adjacent-identity convention (precedent: `scal`, `dot`, `apply_linop`, `assemble-diagonal`); no non-adjacent lowering directory is created. The **substantive** rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme.
[new]: - **Downward** to L2/L1: the L3 form's signature `Tensor[N] -> Tensor[N]` is textually identical to the L2 floor and L1 leaf signatures; all three forms describe pure-functional elementwise reciprocation with no destination buffer in the signature, no per-element loop visible, no reduction, no MPI collective at the L1 / L2 / L3 surface. The L3 → L2 rotation is the identity on the primitive itself. The framing differs: L1 frames `reciprocal` as the *mutation-rotation* image of the L0 receiver-self-overwriting `mfem::Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method idiom (the L1 surface drops the receiver-mutation mention); L3 frames the same operator as a *field operation* in the whole-tensor vocabulary that the iteration-rotation layer composes. **The body of `reciprocal` is the identity rotation across this edge.** It lowers to the **present adjacent L2 floor** [`reciprocal`](../L2/reciprocal.md) (cycle-042) via the `reciprocal-body-identity` L3>L2 theme — the rotation carries no algebraic novelty, mirroring the BLAS-1 / `apply_linop` / `assemble-diagonal` L3>L2 floor discipline. The L3>L2 identity-in-form annotation is captured by the adjacent-edge theme per the cycle-012 per-adjacent-edge lowering-directory convention (precedent: `scal`, `dot`, `assemble-diagonal`, `elementwise_product`); the transitive L3>L1 identity remains in-line, with no non-adjacent `L3-L1/` directory created. The **substantive** rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme.
```

```edit:book/src/L3/reciprocal.md
[old]: L3 `reciprocal` lowers to L1 [`reciprocal`](../L1/reciprocal.md) as **identity-in-form on the primitive's signature** — **no interposed L2 entry, no `L3-L2`/`L3-L1` theme file**. Both L1 and L3 see `reciprocal :: Tensor[N] -> Tensor[N]` with the same shape contract, the same eight algebraic laws, the same non-law set (partiality, nonlinearity, IEEE-754 caveats), and the same single-orthogonal-axis variant profile (element-type). The L2 layer hosts no standalone `reciprocal` entry (mirroring the BLAS-1 / `apply_linop` / `assemble-diagonal` L2 verdict — leaf primitives are referenced from L2 compositions but do not get standalone L2 entries when the rotation carries no algebraic novelty); the L3>L1 hop is therefore direct.
[new]: L3 `reciprocal` lowers to the **present adjacent L2 floor** [`reciprocal`](../L2/reciprocal.md) (cycle-042) as **identity-in-form on the primitive's signature**, via the `reciprocal-body-identity` L3>L2 theme, and onward to L1 [`reciprocal`](../L1/reciprocal.md). L1, L2, and L3 all see `reciprocal :: Tensor[N] -> Tensor[N]` with the same shape contract, the same eight algebraic laws, the same non-law set (partiality, nonlinearity, IEEE-754 caveats), and the same single-orthogonal-axis variant profile (element-type). The L2 floor is the standalone (fork-independent) elementwise multiplicative-inverse leaf — landed by the cycle-042 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-blas1-cohort`, mirroring the cycle-041 `dot` / `nrm2` / `scal` L2 floors — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.
```

```edit:book/src/L3/reciprocal.md
[old]: No `book/src/L3-L1/` directory exists in the artifact; per the cycle-010 `krylov-step`, cycle-011 BLAS-1 / `apply_linop`, and cycle-037 `assemble-diagonal` precedents this entry captures the identity rotation **in-line** (per the cycle-012 meta-phase non-adjacent-identity convention — lowering directories are per-adjacent-edge only). The substantive rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme — it lowers the L1 pure-functional form into Palace's L0 in-place receiver-self-overwrite `Reciprocal()` member-method pair (the real upstream `mfem::Vector::Reciprocal()` and the complex `ComplexVector::Reciprocal()` kernel `s = 1/(XR²+XI²); XR *= s; XI *= -s`, the `forall_switch` host/device dispatch, and the no-zero-guard policy). The L3>L1 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one.
[new]: The L3>L2 identity rotation is captured by the adjacent-edge `reciprocal-body-identity` L3>L2 theme (per the cycle-012 meta-phase per-adjacent-edge lowering-directory convention); the transitive L3>L1 identity (L3>L2 ∘ L2>L1) is annotated in-line, with no `book/src/L3-L1/` directory created. The cycle-010 `krylov-step`, cycle-011 BLAS-1 / `apply_linop`, and cycle-037 `assemble-diagonal` precedents establish the in-line identity-rotation discipline for the floor cohort. The substantive rotation in the chain is the firm L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) theme — it lowers the L1 pure-functional form into Palace's L0 in-place receiver-self-overwrite `Reciprocal()` member-method pair (the real upstream `mfem::Vector::Reciprocal()` and the complex `ComplexVector::Reciprocal()` kernel `s = 1/(XR²+XI²); XR *= s; XI *= -s`, the `forall_switch` host/device dispatch, and the no-zero-guard policy). The L3>L2 and L2>L1 hops are by contrast layer-coherence rotations (each layer is coherent within itself), not algebraic ones.
```

```edit:book/src/L3/reciprocal.md
[old]: - `book/src/L3/assemble-diagonal.md` (cycle-037 firm) — the operator-to-data L3 backfill precedent on the same diagonal-preconditioner-apply chain; `reciprocal` is the elementwise step following `assemble_diagonal`. The L3>L1 identity-in-form discipline, the no-L2-entry / no-theme-file rotation shape, and the firm-on-positive-structure status judgement are inherited from this sibling.
[new]: - `book/src/L3/assemble-diagonal.md` (cycle-037 firm) — the operator-to-data L3 backfill precedent on the same diagonal-preconditioner-apply chain; `reciprocal` is the elementwise step following `assemble_diagonal`. The L3>L2 identity-in-form discipline (through the present adjacent L2 floor via the `assemble-diagonal-body-identity` theme), the adjacent-floor rotation shape, and the firm-on-positive-structure status judgement are inherited from this sibling.
```

#### A2 — `book/src/L3/assemble-diagonal.md` (3 sites)

```edit:book/src/L3/assemble-diagonal.md
[old]: lowers_to:
  - book/src/L1/assemble-diagonal.md (identity-in-form on the primitive's signature; no L3-L1 theme — see Lowers-to)
[new]: lowers_to:
  - book/src/L2/assemble-diagonal.md (identity-in-form on the primitive's signature; lowers through the present adjacent L2 floor via the `assemble-diagonal-body-identity` L3>L2 theme — see Lowers-to)
```

```edit:book/src/L3/assemble-diagonal.md
[old]: - **Downward** to L1: `assemble_diagonal` lowers to L1 [`assemble-diagonal`](../L1/assemble-diagonal.md) directly, with **no interposed L2 entry and no `L3-L2`/`L3-L1` theme file**. The rotation is **identity-in-form on the primitive's signature** — both L1 and L3 see `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal element-type axis + one absorbed operator-representation axis). The L2 layer hosts no standalone `assemble_diagonal` entry; the L3>L1 hop is direct, mirroring the `apply_linop` L3>L1 discipline. The identity-in-form annotation lives in-line here, per the cycle-012 non-adjacent-identity convention (precedent: `apply_linop`, `dot`, `scal`, `krylov-step`); no non-adjacent lowering directory is created.
[new]: - **Downward** to L2/L1: `assemble_diagonal` lowers to the **present adjacent L2 floor** [`assemble-diagonal`](../L2/assemble-diagonal.md) (cycle-042) via the `assemble-diagonal-body-identity` L3>L2 theme, and onward to L1 [`assemble-diagonal`](../L1/assemble-diagonal.md). The rotation is **identity-in-form on the primitive's signature** — L1, L2, and L3 all see `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal element-type axis + one absorbed operator-representation axis). The L2 floor is the standalone (fork-independent) operator-to-data sibling of `apply_linop`; the L3>L2 hop passes through the adjacent floor, mirroring the `apply_linop` floor discipline. The L3>L2 identity-in-form annotation is captured by the adjacent-edge theme per the cycle-012 per-adjacent-edge lowering-directory convention (precedent: `apply_linop`, `dot`, `scal`, `krylov-step`); the transitive L3>L1 identity remains in-line, with no non-adjacent `L3-L1/` lowering directory created.
```

```edit:book/src/L3/assemble-diagonal.md
[old]: L3 `assemble_diagonal` lowers to L1 [`assemble-diagonal`](../L1/assemble-diagonal.md) as **identity-in-form on the primitive's signature** — **no interposed L2 entry, no `L3-L2`/`L3-L1` theme file**. Both L1 and L3 see `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal + one absorbed). The L2 layer does not host an `assemble_diagonal` entry (mirroring the `apply_linop` L2 verdict — primitives are referenced from L2 compositions but do not get standalone L2 entries when the rotation carries no algebraic novelty); the L3>L1 hop is therefore direct.
[new]: L3 `assemble_diagonal` lowers to the **present adjacent L2 floor** [`assemble-diagonal`](../L2/assemble-diagonal.md) (cycle-042) as **identity-in-form on the primitive's signature**, via the `assemble-diagonal-body-identity` L3>L2 theme, and onward to L1 [`assemble-diagonal`](../L1/assemble-diagonal.md). L1, L2, and L3 all see `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal + one absorbed). The L2 floor is the standalone (fork-independent) operator-to-data sibling of `apply_linop` — landed by the cycle-042 L2-floor backfill under the foundation-first directive `l2-floor-under-l3-blas1-cohort` — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.
```

```edit:book/src/L3/assemble-diagonal.md
[old]: No `book/src/L3-L1/` directory exists in the artifact; per the cycle-010 `krylov-step` and cycle-011 BLAS-1 / `apply_linop` precedents this entry captures the identity rotation **in-line** (per the cycle-012 meta-phase non-adjacent-identity convention — lowering directories are per-adjacent-edge only). The substantive rotation in the chain is the L1>L0 [`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) theme
[new]: The L3>L2 identity rotation is captured by the adjacent-edge `assemble-diagonal-body-identity` L3>L2 theme (per the cycle-012 meta-phase per-adjacent-edge lowering-directory convention); the transitive L3>L1 identity (L3>L2 ∘ L2>L1) is annotated in-line, with no `book/src/L3-L1/` directory created. Per the cycle-010 `krylov-step` and cycle-011 BLAS-1 / `apply_linop` precedents this entry captures the in-line identity-rotation discipline for the floor cohort. The substantive rotation in the chain is the L1>L0 [`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) theme
```

#### A3 — `book/src/L3/jacobi-smoother.md` (2 sites)

```edit:book/src/L3/jacobi-smoother.md
[old]: - **Downward** to L1: `jacobi-smoother` lowers to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md) directly, with no interposed L2 entry and no `L3-L2/jacobi-smoother-identity` theme. The rotation is **identity-in-form on the constructed-operator-gate apply** — both L1 and L3 see `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` with the same shape contract, the same algebraic laws, the same variant-axis profile, and the same absorbed operator-representation type. The substantive rotation in the chain is the L1>L0 leaf-mutation rotation: the apply's single elementwise product lowers to Palace's in-place `forall_switch` element-loop (`Y[i] = DI[i] * X[i]`), captured by the firm L1>L0 theme [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B) and the constructed-operator-closure theme [`jacobi-smoother-mutation-rotation`](../L1-L0/jacobi-smoother-mutation-rotation.md). The L3>L1 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one; no `L3-L2/` or non-adjacent `L3-L1/` directory is created — the identity-in-form annotation lives in-line per the cycle-012 non-adjacent-identity convention (precedent: the firm L3 `dot` / `scal` / `apply_linop` cohort, all of which note their identity rotations in-line).
[new]: - **Downward** to L2/L1: `jacobi-smoother` lowers to the **present adjacent L2 floor** [`jacobi-smoother`](../L2/jacobi-smoother.md) (cycle-042) via the `jacobi-smoother-body-identity` L3>L2 theme, and onward to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md). The rotation is **identity-in-form on the constructed-operator-gate apply** — L1, L2, and L3 all see `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` with the same shape contract, the same algebraic laws, the same variant-axis profile, and the same absorbed operator-representation type. The substantive rotation in the chain is the L1>L0 leaf-mutation rotation: the apply's single elementwise product lowers to Palace's in-place `forall_switch` element-loop (`Y[i] = DI[i] * X[i]`), captured by the firm L1>L0 theme [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B) and the constructed-operator-closure theme [`jacobi-smoother-mutation-rotation`](../L1-L0/jacobi-smoother-mutation-rotation.md). The L3>L2 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one; the L3>L2 identity-in-form annotation is captured by the adjacent-edge theme, with no non-adjacent `L3-L1/` directory created — the transitive L3>L1 identity is annotated in-line per the cycle-012 non-adjacent-identity convention (precedent: the firm L3 `dot` / `scal` / `apply_linop` cohort, all of which note their identity rotations in-line).
```

```edit:book/src/L3/jacobi-smoother.md
[old]: L3 `jacobi-smoother` lowers to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md) directly — **no interposed L2 entry, no L3-L2 theme, no non-adjacent L3-L1 directory**. The rotation is identity-in-form on the constructed-operator-gate apply: both L1 and L3 see `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same three-non-law set, and the same two-orthogonal-plus-one-absorbed variant profile. The L3>L1 hop is a layer-coherence rotation (each layer is coherent within itself), not an algebraic one; the identity-in-form annotation lives in-line here (precedent: the firm L3 `dot` / `scal` / `apply_linop` cohort, cycle-011, all of which note their identity rotations in-line rather than in a separate theme file; cycle-012 non-adjacent-identity convention).
[new]: L3 `jacobi-smoother` lowers to the **present adjacent L2 floor** [`jacobi-smoother`](../L2/jacobi-smoother.md) (cycle-042) via the `jacobi-smoother-body-identity` L3>L2 theme, and onward to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md) — **no non-adjacent L3-L1 directory**. The rotation is identity-in-form on the constructed-operator-gate apply: L1, L2, and L3 all see `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same three-non-law set, and the same two-orthogonal-plus-one-absorbed variant profile. The L2 floor is the standalone constructed-operator-gate floor (cycle-042) — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**. The L3>L2 hop is a layer-coherence rotation (each layer is coherent within itself), not an algebraic one; the L3>L2 identity-in-form annotation is captured by the adjacent-edge theme, and the transitive L3>L1 identity is annotated in-line here (precedent: the firm L3 `dot` / `scal` / `apply_linop` cohort, cycle-011, all of which note their identity rotations in-line; cycle-012 non-adjacent-identity convention).
```

#### A4 — `book/src/L3/divfree-projector.md` (3 sites)

```edit:book/src/L3/divfree-projector.md
[old]:   - book/src/L1/divfree-projector.md (identity-in-form on the constructed-operator-gate apply; no L3-L2 theme — the four-step apply is a fixed straight-line composition whose L1 form is L3-native by signature shape; the substantive leaf-mutation rotation lives at L1>L0 divfree-projector-mutation-rotation, and the inner-solve obstruction is carried BY REFERENCE through the firm-L3 ksp_solve dependency, never introduced or erased here)
[new]:   - book/src/L2/divfree-projector.md (identity-in-form on the constructed-operator-gate apply; lowers through the present adjacent L2 floor via the `divfree-projector-body-identity` L3>L2 theme — the four-step apply is a fixed straight-line composition whose L2 floor form is value-thread-isomorphic by signature shape; the substantive leaf-mutation rotation lives at L1>L0 divfree-projector-mutation-rotation, and the inner-solve obstruction is carried BY REFERENCE through the firm-L3 ksp_solve dependency, never introduced or erased here)
```

```edit:book/src/L3/divfree-projector.md
[old]: - **Downward** to L1: `divfree-projector` lowers to L1
  [`divfree-projector`](../L1/divfree-projector.md) directly, with no interposed L2
  entry (`book/src/L2/divfree-projector.md` does not exist) and no
  `L3-L2/divfree-projector-identity` theme. The rotation is **identity-in-form on the
  constructed-operator-gate apply** — both L1 and L3 see
[new]: - **Downward** to L2/L1: `divfree-projector` lowers to the **present adjacent L2 floor**
  [`divfree-projector`](../L2/divfree-projector.md) (cycle-042) via the
  `divfree-projector-body-identity` L3>L2 theme, and onward to L1
  [`divfree-projector`](../L1/divfree-projector.md). The rotation is **identity-in-form on the
  constructed-operator-gate apply** — L1, L2, and L3 all see
```

```edit:book/src/L3/divfree-projector.md
[old]:   the same shape contract, the same five algebraic laws (plus the two
  load-bearing non-laws), and the same element-type variant axis. The substantive
  rotation in the chain is the L1>L0 leaf-mutation rotation: the four-step apply
  lowers to Palace's in-place `Mult(VecType &y)` mutation idiom, captured by the firm
  L1>L0 theme [`divfree-projector-mutation-rotation`](../L1-L0/divfree-projector-mutation-rotation.md).
  The L3>L1 hop is a layer-coherence rotation (each layer is coherent within itself),
  not an algebraic one; no `L3-L2/` or non-adjacent `L3-L1/` directory is created —
  the identity-in-form annotation lives in-line per the cycle-012 non-adjacent-identity
  convention (precedent: the firm L3 `jacobi-smoother` / `apply_linop` / `dot` / `scal`
  cohort, all of which note their identity rotations in-line).
[new]:   the same shape contract, the same five algebraic laws (plus the two
  load-bearing non-laws), and the same element-type variant axis. The L2 floor is the
  same-named fusion-rotation floor under the firm L3 gate (cycle-042); the L3>L2 hop passes
  through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings
  still require both L levels**. The substantive rotation in the chain is the L1>L0
  leaf-mutation rotation: the four-step apply lowers to Palace's in-place `Mult(VecType &y)`
  mutation idiom, captured by the firm L1>L0 theme
  [`divfree-projector-mutation-rotation`](../L1-L0/divfree-projector-mutation-rotation.md).
  The L3>L2 hop is a layer-coherence rotation (each layer is coherent within itself),
  not an algebraic one; the L3>L2 identity-in-form annotation is captured by the adjacent-edge
  `divfree-projector-body-identity` theme, with no non-adjacent `L3-L1/` directory created —
  the transitive L3>L1 identity is annotated in-line per the cycle-012 non-adjacent-identity
  convention (precedent: the firm L3 `jacobi-smoother` / `apply_linop` / `dot` / `scal`
  cohort, all of which note their identity rotations in-line).
```

```edit:book/src/L3/divfree-projector.md
[old]: L3 `divfree-projector` lowers to L1 [`divfree-projector`](../L1/divfree-projector.md)
directly — **no interposed L2 entry, no L3-L2 theme, no non-adjacent L3-L1 directory**.
The rotation is identity-in-form on the constructed-operator-gate apply: both L1 and L3
see `divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]`
with the same shape contract, the same five algebraic laws, the same two-non-law set, and
the same one-orthogonal-plus-one-absorbed variant profile. The L3>L1 hop is a
layer-coherence rotation (each layer is coherent within itself), not an algebraic one;
the identity-in-form annotation lives in-line here (precedent: the firm L3
`jacobi-smoother` / `apply_linop` / `dot` / `scal` cohort, all of which note their
identity rotations in-line rather than in a separate theme file; cycle-012
non-adjacent-identity convention).
[new]: L3 `divfree-projector` lowers to the **present adjacent L2 floor**
[`divfree-projector`](../L2/divfree-projector.md) (cycle-042) via the
`divfree-projector-body-identity` L3>L2 theme, and onward to L1
[`divfree-projector`](../L1/divfree-projector.md) — **no non-adjacent L3-L1 directory**.
The rotation is identity-in-form on the constructed-operator-gate apply: L1, L2, and L3
all see `divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]`
with the same shape contract, the same five algebraic laws, the same two-non-law set, and
the same one-orthogonal-plus-one-absorbed variant profile. The L2 floor is the same-named
fusion-rotation floor under the firm L3 gate (cycle-042); the L3>L2 hop passes through the
adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require
both L levels**. The L3>L2 hop is a layer-coherence rotation (each layer is coherent within
itself), not an algebraic one; the L3>L2 identity-in-form annotation is captured by the
adjacent-edge theme, and the transitive L3>L1 identity is annotated in-line here (precedent:
the firm L3 `jacobi-smoother` / `apply_linop` / `dot` / `scal` cohort, all of which note their
identity rotations in-line; cycle-012 non-adjacent-identity convention).
```

#### A5 — `book/src/L3/elementwise_product.md:166` (residual `scal`-gloss staleness)

```edit:book/src/L3/elementwise_product.md
[old]: - `book/src/L3/scal.md` (cycle-011 firm) — the leaf-field-operation L3 backfill precedent; `elementwise_product` is the binary-Hadamard generalisation of `scal` (broadcast specialisation, law 7). The L3>L1 identity-in-form discipline, the no-L2-entry / no-theme-file rotation shape, and the variant-absorption framing are inherited from this sibling.
[new]: - `book/src/L3/scal.md` (cycle-011 firm) — the leaf-field-operation L3 backfill precedent; `elementwise_product` is the binary-Hadamard generalisation of `scal` (broadcast specialisation, law 7). The L3>L2 identity-in-form discipline (through the present adjacent L2 `scal` floor via the `scal-body-identity` theme), the adjacent-floor rotation shape, and the variant-absorption framing are inherited from this sibling.
```

---

### (B) Two citation fixes

#### B1 — `book/src/L1/assemble-diagonal.md:111` — `AbsMultTranspose` `:172`→`:174`

`citecheck --anchor 'AbsMultTranspose'` confirms the call site is on `rap.cpp:174`, not `:172`.

```edit:book/src/L1/assemble-diagonal.md
[old]: the AMR `|P|ᵀ dₗ` absolute-value-prolongation assembly with the convergent-diagonal comment (lines 163-176, `hP->AbsMultTranspose(1.0, lx, 0.0, diag)` at line 172), and the Dirichlet `DiagonalPolicy` BC post-step `DIAG_ONE` / `DIAG_ZERO` (lines 180-191).
[new]: the AMR `|P|ᵀ dₗ` absolute-value-prolongation assembly with the convergent-diagonal comment (lines 163-176, `hP->AbsMultTranspose(1.0, lx, 0.0, diag)` at line 174), and the Dirichlet `DiagonalPolicy` BC post-step `DIAG_ONE` / `DIAG_ZERO` (lines 180-191).
```

#### B2 — `book/src/L3/index.md` — 3 self-citations `index.md:39`→`:46`

The cycle-036 D2 "(A) Identity-in-form L3 backfill candidates" classification moved from line
39 to line 46. `citecheck --anchor` confirms the (A) classification text is on `:46`. The three
self-citations in `index.md` are on lines 23, 33, 58.

```edit:book/src/L3/index.md
[old]: enacts the cycle-036 D2 L3-cohort-growth audit **(A) identity-in-form** verdict at `book/src/L3/index.md:39` — "structurally identical to the firm `apply_linop` opaque-operator-gate precedent"; first of the six (A) firm backfills to land, exact-vs-approximate caveat absorbed as a representation-aware non-law) |
[new]: enacts the cycle-036 D2 L3-cohort-growth audit **(A) identity-in-form** verdict at `book/src/L3/index.md:46` — "structurally identical to the firm `apply_linop` opaque-operator-gate precedent"; first of the six (A) firm backfills to land, exact-vs-approximate caveat absorbed as a representation-aware non-law) |
```

```edit:book/src/L3/index.md
[old]: `firm` (harvested cycle-037T193322Z; **sixth and final (A) firm identity-in-form L3 backfill** of the cycle-036 D2 audit verdict at `book/src/L3/index.md:39`; the thinnest constructed-operator gate
[new]: `firm` (harvested cycle-037T193322Z; **sixth and final (A) firm identity-in-form L3 backfill** of the cycle-036 D2 audit verdict at `book/src/L3/index.md:46`; the thinnest constructed-operator gate
```

```edit:book/src/L3/index.md
[old]: sibling of `apply_linop` on the operator-to-data side; first of the six (A) firm backfills of the cycle-036 D2 audit verdict at `book/src/L3/index.md:39`) and [`jacobi-smoother`](./jacobi-smoother.md) (11th firm
[new]: sibling of `apply_linop` on the operator-to-data side; first of the six (A) firm backfills of the cycle-036 D2 audit verdict at `book/src/L3/index.md:46`) and [`jacobi-smoother`](./jacobi-smoother.md) (11th firm
```

---

### (C) Three slug renames + cross-reference rewrites

#### C1 — `git mv` directives (integrator applies)

```sh
git mv book/src/L2-L1/nrm2-fold-specialization.md book/src/L2-L1/nrm2-leaf-identity.md
git mv book/src/L2-L1/scal-fold-specialization.md book/src/L2-L1/scal-leaf-identity.md
git mv book/src/L3-L2/elementwise_product-body-identity.md book/src/L3-L2/elementwise-product-body-identity.md
```

#### C2 — H1 / §Slug inside the renamed `nrm2-leaf-identity.md`

```edit:book/src/L2-L1/nrm2-leaf-identity.md
[old]: # nrm2-fold-specialization
[new]: # nrm2-leaf-identity
```

```edit:book/src/L2-L1/nrm2-leaf-identity.md
[old]: L1 `nrm2`. The `-fold-specialization` slug is carried for sibling-naming continuity (the
BLAS-1 reduce-to-scalar cohort), but `nrm2` is explicitly **not a fold member** (do-NOT-merge
[new]: L1 `nrm2`. The `-leaf-identity` slug names the identity-in-form lowering of the single L2
floor onto the single L1 leaf (the cycle-043 batch-12 normalization from the cycle-041
`-fold-specialization` outlier; neither edge is a fold-dispatch); `nrm2` is explicitly **not a fold member** (do-NOT-merge
```

```edit:book/src/L2-L1/nrm2-leaf-identity.md
[old]: ## Slug

`nrm2-fold-specialization`
[new]: ## Slug

`nrm2-leaf-identity`
```

#### C3 — H1 / §Slug inside the renamed `scal-leaf-identity.md`

```edit:book/src/L2-L1/scal-leaf-identity.md
[old]: # scal-fold-specialization
[new]: # scal-leaf-identity
```

```edit:book/src/L2-L1/scal-leaf-identity.md
[old]: ## Slug

`scal-fold-specialization`
[new]: ## Slug

`scal-leaf-identity`
```

#### C4 — H1 / §Slug / filename-convention note inside the renamed `elementwise-product-body-identity.md`

```edit:book/src/L3-L2/elementwise-product-body-identity.md
[old]: # elementwise_product-body-identity
[new]: # elementwise-product-body-identity
```

```edit:book/src/L3-L2/elementwise-product-body-identity.md
[old]: ## Slug

`elementwise_product-body-identity`

> **Filename-convention note.** This chapter uses the **underscore** spelling
> `elementwise_product-body-identity.md`, matching the underscore operator-chapter convention of the
> L1/L2/L3 `elementwise_product.md` entries (per the dispatch directive). The L2>L1 sibling uses the
> **hyphen** spelling `elementwise-product-leaf-identity.md` (matching the `dot-leaf-identity` /
> `nrm2-fold-specialization` L2>L1 sibling convention, which is hyphenated). The underscore-vs-hyphen
> split (underscore operator chapters + body-identity theme; hyphen concept page + leaf-identity theme)
> is consistent within the `elementwise_product` family but heterogeneous across the L2>L1 / L3>L2
> theme slugs; surfaced for the batch-12 meta-phase to normalize (see this theme's authoring report
> §Open questions).
[new]: ## Slug

`elementwise-product-body-identity`

> **Filename-convention note (normalized cycle-043).** This chapter uses the **hyphen** spelling
> `elementwise-product-body-identity.md`, matching its hyphenated L2>L1 sibling
> `elementwise-product-leaf-identity.md` and the uniform `-leaf-identity` / `-body-identity`
> theme-slug convention ratified by the batch-12 meta-phase. The underscore operator chapters
> (`L1/L2/L3 elementwise_product.md`) keep the underscore spelling that matches the firm operator
> entries; the theme slugs are hyphenated. This resolves the cycle-042 underscore-vs-hyphen split
> (the theme slug was originally underscored to match the operator chapters; the batch-12
> normalization moved all theme slugs to hyphen).
```

(The line-21 `> elementwise_product-body-identity.md, matching the underscore operator-chapter
convention…` blockquote line is consumed by the §Slug blockquote replacement above — no separate
edit needed for it.)

```edit:book/src/L3-L2/elementwise-product-body-identity.md
[old]: - **Filename underscore-vs-hyphen split (for the meta-phase).** This theme is `_`-spelled
  (`elementwise_product-body-identity.md`, matching the operator chapters); the L2>L1 sibling is
  `-`-spelled (`elementwise-product-leaf-identity.md`, matching the hyphenated L2>L1 theme-slug
  convention). Heterogeneous but each link resolves on disk; surfaced for the batch-12 meta-phase to
[new]: - **Filename convention (normalized cycle-043).** This theme is now `-`-spelled
  (`elementwise-product-body-identity.md`, matching the hyphenated theme-slug convention) and its
  L2>L1 sibling is likewise `-`-spelled (`elementwise-product-leaf-identity.md`). The batch-12
  meta-phase normalized all theme slugs to the uniform `-leaf-identity` / `-body-identity` hyphen
  convention; the underscore operator chapters are unaffected. Surfaced for the batch-12 meta-phase to
```

#### C5 — `book/src/SUMMARY.md` (3 nav rows)

```edit:book/src/SUMMARY.md
[old]: - [scal-fold-specialization](./L2-L1/scal-fold-specialization.md)
[new]: - [scal-leaf-identity](./L2-L1/scal-leaf-identity.md)
```

```edit:book/src/SUMMARY.md
[old]: - [nrm2-fold-specialization](./L2-L1/nrm2-fold-specialization.md)
[new]: - [nrm2-leaf-identity](./L2-L1/nrm2-leaf-identity.md)
```

```edit:book/src/SUMMARY.md
[old]: - [elementwise_product-body-identity](./L3-L2/elementwise_product-body-identity.md)
[new]: - [elementwise-product-body-identity](./L3-L2/elementwise-product-body-identity.md)
```

#### C6 — `book/src/L2-L1/index.md` (dep-map rows 15, 18 + working-note bullets 45, 46, 63)

```edit:book/src/L2-L1/index.md
[old]: | [scal-fold-specialization](./scal-fold-specialization.md) | `L2/scal` (firm, cycle-041 D3) | `L1/scal` (firm leaf, cycle-004) | firm *(structural; identity-in-form floor edge — the degenerate arity-1 single-term shadow of `linear-combination-fold-specialization`; no arity dispatch, no pinned-summation-order residue (one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged)* |
[new]: | [scal-leaf-identity](./scal-leaf-identity.md) | `L2/scal` (firm, cycle-041 D3) | `L1/scal` (firm leaf, cycle-004) | firm *(structural; identity-in-form floor edge — the degenerate arity-1 single-term shadow of `linear-combination-fold-specialization`; no arity dispatch, no pinned-summation-order residue (one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged; renamed cycle-043 from `scal-fold-specialization`)* |
```

```edit:book/src/L2-L1/index.md
[old]: | [nrm2-fold-specialization](./nrm2-fold-specialization.md) | `L2/nrm2` (firm cycle-041) | `L1/nrm2` (firm cycle-003; single leaf — no L1 family to dispatch) | firm *(structural; thin-identity — BLAS-1-leaf consumer sibling of `inner-product-fold-specialization`; `nrm2` = `√ ∘ abs ∘ inner_product` CONSUMER at `y=x`, NOT a fold member; no dispatch / no decomposition / no destination buffer; `√`/`abs` scalar post-steps drop below L1 resolution + `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1)* |
[new]: | [nrm2-leaf-identity](./nrm2-leaf-identity.md) | `L2/nrm2` (firm cycle-041) | `L1/nrm2` (firm cycle-003; single leaf — no L1 family to dispatch) | firm *(structural; thin-identity — BLAS-1-leaf consumer sibling of `inner-product-fold-specialization`; `nrm2` = `√ ∘ abs ∘ inner_product` CONSUMER at `y=x`, NOT a fold member; no dispatch / no decomposition / no destination buffer; `√`/`abs` scalar post-steps drop below L1 resolution + `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1; renamed cycle-043 from `nrm2-fold-specialization`)* |
```

```edit:book/src/L2-L1/index.md
[old]: - `nrm2-fold-specialization` — the L2 `nrm2` floor lowers to the single L1 `nrm2` leaf; the BLAS-1-leaf **consumer** sibling of `inner-product-fold-specialization` (`nrm2 = √ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member; no dispatch / no decomposition / no buffer); `√`/`abs` post-steps drop below L1 resolution, `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1.
[new]: - `nrm2-leaf-identity` (renamed cycle-043 from `nrm2-fold-specialization`) — the L2 `nrm2` floor lowers to the single L1 `nrm2` leaf; the BLAS-1-leaf **consumer** sibling of `inner-product-fold-specialization` (`nrm2 = √ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member; no dispatch / no decomposition / no buffer); `√`/`abs` post-steps drop below L1 resolution, `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1.
```

```edit:book/src/L2-L1/index.md
[old]: - `scal-fold-specialization` — the L2 `scal` floor lowers to the L1 `scal` leaf; the degenerate **arity-1 single-term shadow** of `linear-combination-fold-specialization` (no arity dispatch, no pinned-summation-order residue — one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged.
[new]: - `scal-leaf-identity` (renamed cycle-043 from `scal-fold-specialization`) — the L2 `scal` floor lowers to the L1 `scal` leaf; the degenerate **arity-1 single-term shadow** of `linear-combination-fold-specialization` (no arity dispatch, no pinned-summation-order residue — one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged.
```

```edit:book/src/L2-L1/index.md
[old]: `dot-leaf-identity` + `nrm2-fold-specialization` + `scal-fold-specialization` firm cycle-041 (the FOLD-PARENTED BLAS-1-floor-edge cohort — the L2>L1 thin-identity edges of the same-named L2 floors `dot`/`nrm2`/`scal`, firm 7 → 10; all fusion deferred to the fold-parents, all identity-in-form on the primitive; **presuppose the (b) leaf-floor design realization — under batch-12 meta-phase adjudication, see §"Design fork" below**);
[new]: `dot-leaf-identity` + `nrm2-leaf-identity` + `scal-leaf-identity` firm cycle-041 (the FOLD-PARENTED BLAS-1-floor-edge cohort — the L2>L1 thin-identity edges of the same-named L2 floors `dot`/`nrm2`/`scal`, firm 7 → 10; all fusion deferred to the fold-parents, all identity-in-form on the primitive; `nrm2`/`scal` renamed cycle-043 from `-fold-specialization` to the uniform `-leaf-identity` convention; **presuppose the (b) leaf-floor design realization — under batch-12 meta-phase adjudication, see §"Design fork" below**);
```

```edit:book/src/L2-L1/index.md
[old]: If the meta-phase adopts (a), `dot-leaf-identity` dissolves into `inner-product-fold-specialization`'s conjugation dispatch and `scal-fold-specialization` into `linear-combination-fold-specialization`'s arity-1 row;
[new]: If the meta-phase adopts (a), `dot-leaf-identity` dissolves into `inner-product-fold-specialization`'s conjugation dispatch and `scal-leaf-identity` into `linear-combination-fold-specialization`'s arity-1 row;
```

```edit:book/src/L2-L1/index.md
[old]: Also flagged: the cycle-041 L2>L1 cohort slug split (`dot-leaf-identity` vs `nrm2`/`scal` `-fold-specialization`) for three structurally-similar identity edges; the cycle-042 cohort used `-leaf-identity` uniformly, making the two cycle-041 `-fold-specialization` slugs the outliers for the meta-phase to normalize.
[new]: Slug normalization (cycle-043, batch-12 meta decision): the cycle-041 `nrm2`/`scal` L2>L1 edges were renamed from `-fold-specialization` to `-leaf-identity`, making the whole L2>L1 identity-edge cohort uniform (`dot-leaf-identity`, `nrm2-leaf-identity`, `scal-leaf-identity` + the cycle-042 standalone-floor edges); neither edge is a fold-dispatch.
```

#### C7 — `book/src/L3-L2/index.md` (dep-map row 21 + working-note bullets 43, 48)

```edit:book/src/L3-L2/index.md
[old]: | [`elementwise_product-body-identity`](./elementwise_product-body-identity.md) | L3 [`elementwise_product`](../L3/elementwise_product.md) §Signature
[new]: | [`elementwise-product-body-identity`](./elementwise-product-body-identity.md) | L3 [`elementwise_product`](../L3/elementwise_product.md) §Signature
```

```edit:book/src/L3-L2/index.md
[old]: - `elementwise_product-body-identity` — the L3 whole-tensor `elementwise_product` Hadamard binary field op lowers to the L2 standalone floor leaf (fork-INDEPENDENT, NO fold-parent); identity-in-form on the body (ten laws + element-type / conjugation axes); no wrapper and no fold-parent to defer to.
[new]: - `elementwise-product-body-identity` (renamed cycle-043 from `elementwise_product-body-identity`, underscore→hyphen) — the L3 whole-tensor `elementwise_product` Hadamard binary field op lowers to the L2 standalone floor leaf (fork-INDEPENDENT, NO fold-parent); identity-in-form on the body (ten laws + element-type / conjugation axes); no wrapper and no fold-parent to defer to.
```

```edit:book/src/L3-L2/index.md
[old]: the **fork-INDEPENDENT standalone-floor** cohort (`assemble-diagonal-body-identity` / `jacobi-smoother-body-identity` / `divfree-projector-body-identity` / `reciprocal-body-identity` / `elementwise_product-body-identity`),
[new]: the **fork-INDEPENDENT standalone-floor** cohort (`assemble-diagonal-body-identity` / `jacobi-smoother-body-identity` / `divfree-projector-body-identity` / `reciprocal-body-identity` / `elementwise-product-body-identity`),
```

#### C8 — `book/src/L2/index.md` (working-note passages 106, 108 — slug names in the narrative + normalization-status correction)

```edit:book/src/L2/index.md
[old]: The companion adjacent thin-identity themes landed the same cycle (L2>L1: `dot-leaf-identity` / `nrm2-fold-specialization` / `scal-fold-specialization`; L3>L2: `dot-body-identity` / `nrm2-body-identity` / `scal-body-identity`).
[new]: The companion adjacent thin-identity themes landed the same cycle (L2>L1: `dot-leaf-identity` / `nrm2-leaf-identity` / `scal-leaf-identity` — the latter two renamed cycle-043 from `-fold-specialization`; L3>L2: `dot-body-identity` / `nrm2-body-identity` / `scal-body-identity`).
```

```edit:book/src/L2/index.md
[old]:   - **Slug-naming inconsistency within the L2>L1 cohort (for the meta-phase to normalize).** The cycle-041 L2>L1 `dot` theme is `dot-leaf-identity` (D4 deliberately adjusted from the dispatch-proposed `dot-fold-specialization`, on the reasoning that the `-fold-specialization` suffix names a *fold→leaf dispatch* and would mis-name an identity-leaf-lowering + collide with the existing `inner-product-fold-specialization` whose RHS already IS `L1/dot`), while the cycle-041 `nrm2` and `scal` L2>L1 themes use `-fold-specialization` (`nrm2-fold-specialization`, `scal-fold-specialization`) for sibling-naming continuity — even though `nrm2` is a *consumer* (not a fold member) and `scal`'s edge is the degenerate arity-1 *single-term shadow* (no dispatch). **The cycle-042 cohort used `-leaf-identity` (L2>L1) / `-body-identity` (L3>L2) consistently across all five floors** (`reciprocal`/`elementwise-product`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`), establishing the uniform pairing as the de-facto convention; the cycle-041 `nrm2-fold-specialization` / `scal-fold-specialization` remain the **outliers awaiting meta-phase normalization** (candidate: rename both to `-leaf-identity`, since neither edge is a fold-dispatch — none of the L2>L1 identity edges is). One additional cycle-042 wrinkle (D10): the `elementwise_product` chapter filename is underscored (`elementwise_product.md`, matching the firm L1/L3 entries) while its concept page is hyphenated (`concepts/elementwise-product.md`) and the L2>L1 theme slug is hyphenated (`elementwise-product-leaf-identity`) but the L3>L2 theme slug is underscored (`elementwise_product-body-identity`) — the underscore-vs-hyphen split is consistent within the family but flagged for the same normalization pass.
[new]:   - **Slug-naming convention within the L2>L1 cohort (NORMALIZED cycle-043, batch-12 meta decision).** The cycle-041 L2>L1 `dot` theme is `dot-leaf-identity` (D4 deliberately adjusted from the dispatch-proposed `dot-fold-specialization`, on the reasoning that the `-fold-specialization` suffix names a *fold→leaf dispatch* and would mis-name an identity-leaf-lowering + collide with the existing `inner-product-fold-specialization` whose RHS already IS `L1/dot`). The cycle-041 `nrm2` and `scal` L2>L1 themes originally used `-fold-specialization` for sibling-naming continuity — even though `nrm2` is a *consumer* (not a fold member) and `scal`'s edge is the degenerate arity-1 *single-term shadow* (no dispatch). **The cycle-042 cohort used `-leaf-identity` (L2>L1) / `-body-identity` (L3>L2) consistently across all five floors** (`reciprocal`/`elementwise-product`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`), establishing the uniform pairing as the convention; **cycle-043 enacted the normalization** — `nrm2-fold-specialization`→`nrm2-leaf-identity` and `scal-fold-specialization`→`scal-leaf-identity` (neither edge is a fold-dispatch), so the whole L2>L1 identity-edge cohort is now uniform. The cycle-042 underscore-vs-hyphen wrinkle (D10) was also resolved cycle-043: the L3>L2 `elementwise_product-body-identity` theme slug was renamed underscore→hyphen to `elementwise-product-body-identity`, matching its hyphenated L2>L1 sibling `elementwise-product-leaf-identity` (the operator chapters `elementwise_product.md` keep the underscore spelling that matches the firm L1/L3 entries; only the theme slugs are hyphenated).
```

#### C9 — sibling-theme bodies that link the renamed slugs

```edit:book/src/L2-L1/reciprocal-leaf-identity.md
[old]: [`reciprocal-body-identity`](../L3-L2/reciprocal-body-identity.md) (the other thin edge of the same
leaf), and a sibling shape to [`scal-fold-specialization`](./scal-fold-specialization.md) and
[`nrm2-fold-specialization`](./nrm2-fold-specialization.md) — except those defer to a fold-parent or
consume a fold, while this leaf is fold-free.
[new]: [`reciprocal-body-identity`](../L3-L2/reciprocal-body-identity.md) (the other thin edge of the same
leaf), and a sibling shape to [`scal-leaf-identity`](./scal-leaf-identity.md) and
[`nrm2-leaf-identity`](./nrm2-leaf-identity.md) — except those defer to a fold-parent or
consume a fold, while this leaf is fold-free.
```

```edit:book/src/L2-L1/divfree-projector-leaf-identity.md
[old]: ([`dot-leaf-identity`](./dot-leaf-identity.md) / [`nrm2-fold-specialization`](./nrm2-fold-specialization.md)
/ [`scal-fold-specialization`](./scal-fold-specialization.md)) — but with two structural differences:
[new]: ([`dot-leaf-identity`](./dot-leaf-identity.md) / [`nrm2-leaf-identity`](./nrm2-leaf-identity.md)
/ [`scal-leaf-identity`](./scal-leaf-identity.md)) — but with two structural differences:
```

```edit:book/src/L2-L1/assemble-diagonal-leaf-identity.md
[old]: `dot-leaf-identity` / `scal-fold-specialization` edges — which presuppose the wave-1 (b) leaf-floor
[new]: `dot-leaf-identity` / `scal-leaf-identity` edges — which presuppose the wave-1 (b) leaf-floor
```

```edit:book/src/L2-L1/assemble-diagonal-leaf-identity.md
[old]: > **Fork-independence note (not a status reduction).** Unlike the cycle-041 `dot-leaf-identity` /
> `scal-fold-specialization` floor-edges, this theme does **not** presuppose any fold-design reading:
[new]: > **Fork-independence note (not a status reduction).** Unlike the cycle-041 `dot-leaf-identity` /
> `scal-leaf-identity` floor-edges, this theme does **not** presuppose any fold-design reading:
```

```edit:book/src/L3-L2/nrm2-body-identity.md
[old]:    [`nrm2-fold-specialization`](../L2-L1/nrm2-fold-specialization.md) lowers the L2 form the rest
[new]:    [`nrm2-leaf-identity`](../L2-L1/nrm2-leaf-identity.md) lowers the L2 form the rest
```

```edit:book/src/L3-L2/nrm2-body-identity.md
[old]: - [`book/src/L2-L1/nrm2-fold-specialization.md`](../L2-L1/nrm2-fold-specialization.md) (this
[new]: - [`book/src/L2-L1/nrm2-leaf-identity.md`](../L2-L1/nrm2-leaf-identity.md) (this
```

```edit:book/src/L3-L2/nrm2-body-identity.md
[old]: - **L2>L1 (`nrm2-fold-specialization`)**: the L2 fusion composition re-fuses onto the single L1
[new]: - **L2>L1 (`nrm2-leaf-identity`)**: the L2 fusion composition re-fuses onto the single L1
```

```edit:book/src/L3-L2/scal-body-identity.md
[old]: - **L2>L1 form** ([`L2-L1/scal-fold-specialization`](../L2-L1/scal-fold-specialization.md),
  firm cycle-041 D6) — the onward edge into the L1 leaf; also identity-in-form (the fold's
[new]: - **L2>L1 form** ([`L2-L1/scal-leaf-identity`](../L2-L1/scal-leaf-identity.md),
  firm cycle-041 D6) — the onward edge into the L1 leaf; also identity-in-form (the fold's
```

```edit:book/src/L3-L2/scal-body-identity.md
[old]: - `book/src/L2-L1/scal-fold-specialization.md` (cycle-041 D6) — the onward L2>L1 edge into
  the L1 leaf; also identity-in-form (the fold's arity-1 row). Co-dispatched this cycle.
[new]: - `book/src/L2-L1/scal-leaf-identity.md` (cycle-041 D6) — the onward L2>L1 edge into
  the L1 leaf; also identity-in-form (the fold's arity-1 row). Co-dispatched this cycle.
```

```edit:book/src/L3-L2/scal-body-identity.md
[old]:   identity (this theme's L3>L2 identity ∘ the L2>L1 `scal-fold-specialization` identity)
[new]:   identity (this theme's L3>L2 identity ∘ the L2>L1 `scal-leaf-identity` identity)
```

```edit:book/src/L3-L2/scal-body-identity.md
[old]:   `scal-fold-specialization` compose to capture it.
[new]:   `scal-leaf-identity` compose to capture it.
```

```edit:book/src/L3/elementwise_product.md
[old]:   - book/src/L2/elementwise_product.md (identity-in-form on the primitive's signature; lowers through the present adjacent L2 floor via the `elementwise_product-body-identity` L3>L2 theme — see Lowers-to)
[new]:   - book/src/L2/elementwise_product.md (identity-in-form on the primitive's signature; lowers through the present adjacent L2 floor via the `elementwise-product-body-identity` L3>L2 theme — see Lowers-to)
```

```edit:book/src/L3/elementwise_product.md
[old]: - **Downward** to L2: `elementwise_product` lowers to the **present adjacent L2 floor** [`elementwise_product`](../L2/elementwise_product.md) (cycle-042) via the `elementwise_product-body-identity` L3>L2 theme, and onward to L1 [`elementwise_product`](../L1/elementwise_product.md).
[new]: - **Downward** to L2: `elementwise_product` lowers to the **present adjacent L2 floor** [`elementwise_product`](../L2/elementwise_product.md) (cycle-042) via the `elementwise-product-body-identity` L3>L2 theme, and onward to L1 [`elementwise_product`](../L1/elementwise_product.md).
```

```edit:book/src/L3/elementwise_product.md
[old]: L3 `elementwise_product` lowers to the **present adjacent L2 floor** [`elementwise_product`](../L2/elementwise_product.md) (cycle-042) as **identity-in-form on the primitive's signature**, via the `elementwise_product-body-identity` L3>L2 theme, and onward to L1 [`elementwise_product`](../L1/elementwise_product.md).
[new]: L3 `elementwise_product` lowers to the **present adjacent L2 floor** [`elementwise_product`](../L2/elementwise_product.md) (cycle-042) as **identity-in-form on the primitive's signature**, via the `elementwise-product-body-identity` L3>L2 theme, and onward to L1 [`elementwise_product`](../L1/elementwise_product.md).
```

```edit:book/src/L3/elementwise_product.md
[old]: The L3>L2 identity rotation is captured by the adjacent-edge `elementwise_product-body-identity` L3>L2 theme (per the cycle-012 meta-phase per-adjacent-edge lowering-directory convention);
[new]: The L3>L2 identity rotation is captured by the adjacent-edge `elementwise-product-body-identity` L3>L2 theme (per the cycle-012 meta-phase per-adjacent-edge lowering-directory convention);
```

```edit:book/src/L2-L1/elementwise-product-leaf-identity.md
[old]: of the L3>L2 [`elementwise_product-body-identity`](../L3-L2/elementwise_product-body-identity.md) (the
other thin edge of the same leaf).
[new]: of the L3>L2 [`elementwise-product-body-identity`](../L3-L2/elementwise-product-body-identity.md) (the
other thin edge of the same leaf).
```

```edit:book/src/L2-L1/elementwise-product-leaf-identity.md
[old]: the L3>L2 [`elementwise_product-body-identity`](../L3-L2/elementwise_product-body-identity.md) theme
(the other thin edge of the same leaf).
[new]: the L3>L2 [`elementwise-product-body-identity`](../L3-L2/elementwise-product-body-identity.md) theme
(the other thin edge of the same leaf).
```

```edit:book/src/L2-L1/elementwise-product-leaf-identity.md
[old]: - `book/src/L3-L2/elementwise_product-body-identity.md` (firm cycle-042 D10) — the sibling L3>L2 edge
[new]: - `book/src/L3-L2/elementwise-product-body-identity.md` (firm cycle-042 D10) — the sibling L3>L2 edge
```

---

## Discipline notes

**Write mode (role spec compliance).** I emit proposed-changes blocks + `git mv` directives;
`integrator-per-report` applies them in Phase 5. No direct `book/` mutation or `git mv` by me
(role-spec §Discipline bullet 1; friction-ledger `specialized-agent-direct-write-to-book-during-dispatch`).
The `git mv` is rendered as a fenced `sh` directive block (C1) for the integrator, who has
`book/` write authority.

**(A) structural rewrite, not authorship.** Every (A) edit only re-points the two stale clauses
("no interposed L2 entry" / "direct L3>L1 hop" / "the no-L2-entry / no-theme-file rotation shape")
to the now-present adjacent L2 floor + `*-body-identity` theme. The lowering remains
identity-in-form; no algebraic law, signature, decomposition, or variant axis changed. This
exactly mirrors the c042 D3 inline reconciliation already landed in `elementwise_product.md`
(read on-disk; lines 6/28/149/151 are the template I followed). The cycle-012 non-adjacent-identity
convention nuance is preserved: the L3>L2 *adjacent-edge* identity is now captured by the theme
(per-adjacent-edge directory convention), while the transitive L3>L1 identity stays in-line with
no `L3-L1/` directory created.

**(A) layer-definition discipline (high→low).** All re-anchored prose narrates the rewrite forward
(L3→L2→L1). I did not invert any rotation direction; "lowers to / Downward" framing preserved.

**(B) bounded prose-corrections, both L0-evidenced (role-spec §Discipline "L0-evidence-driven prose
correction is in-scope when bounded + evidenced + recorded").**
- B1: `rap.cpp:172`→`:174` for the `AbsMultTranspose` call site, confirmed by
  `citecheck --anchor 'AbsMultTranspose'` (the anchor lands on `:174`; `:172` is +2 outside).
  Bounded: a single drifted line number, no decomposition change.
- B2: the three `L3/index.md:39` self-citations →`:46`, confirmed by `citecheck --anchor` that the
  "(A) Identity-in-form L3 backfill candidates" classification text now sits on `:46` (the audit
  block shifted when cohort-growth bullets were inserted). Bounded: self-citation line numbers only.

**(C) ratified renames (batch-12 meta decisions 2+4).** `-fold-specialization`→`-leaf-identity`
(the two cycle-041 outliers; neither edge is a fold-dispatch, per the L2-L1/index.md §"Design fork"
and L2/index.md:108 normalization candidate already on record) and underscore→hyphen on
`elementwise_product-body-identity`. I rewrote: the H1 + §Slug inside each renamed file; the three
SUMMARY.md nav rows; the L2-L1/index.md + L3-L2/index.md dep-map rows; all sibling-theme body
links; and the L3 `elementwise_product` entry's three slug references. The two filename-convention
narrative notes and the L2/index.md / L2-L1/index.md "awaiting normalization" passages were updated
from pending-decision framing to "normalized cycle-043" (bounded prose-correction — leaving a
dangling description of a now-completed action is stale; the meta decision is on-record in those
same passages). I deliberately did **not** touch `inner-product-fold-specialization` or
`linear-combination-fold-specialization` (separate, not-renamed themes).

**Scope boundary held.** I did NOT sweep the broader `L3/index.md:NN` citation drift that the grep
surfaced (`:41`, `:40-45`, `:38-43`, `:53`, `:44` in the reciprocal / assemble-diagonal / jacobi /
elementwise / normalize entries also point at shifted audit-block lines). That is a separate,
larger index-citation-drift sweep outside this dispatch's bounded (A)/(B)/(C) scope — surfaced as
an OQ below rather than silently expanded into. My (A) edits changed only the lowering-clause prose,
not those entries' `index.md:NN` self-citations.

## Supporting evidence

**citecheck — B1 (`AbsMultTranspose`):**
```
$ python3 tools/citecheck/citecheck.py palace/linalg/rap.cpp:172 --anchor 'AbsMultTranspose'
[DRIFT] palace/linalg/rap.cpp:172  (anchor lit: 'AbsMultTranspose')
       anchor at line 174, +2 outside range 172-172
       suggested: palace/linalg/rap.cpp:174
$ python3 tools/citecheck/citecheck.py palace/linalg/rap.cpp:174 --anchor 'AbsMultTranspose'
[ok  ] palace/linalg/rap.cpp:174  (anchor lit: 'AbsMultTranspose')  within range 174-174
```

**citecheck — B2 (`L3/index.md:46` (A)-classification):**
```
$ python3 tools/citecheck/citecheck.py book/src/L3/index.md:46 --anchor '(A) Identity-in-form L3 backfill candidates'
[ok  ] book/src/L3/index.md:46  anchor at line(s) [46] within range 46-46
```

**Floors + themes present on-disk (the re-anchor targets for (A)):**
```
$ ls book/src/L2/{reciprocal,assemble-diagonal,jacobi-smoother,divfree-projector}.md
   all present
$ ls book/src/L3-L2/{reciprocal,assemble-diagonal,jacobi-smoother,divfree-projector}-body-identity.md
   all present
```

**Rename targets are not-yet-present (correct — they are the `git mv` destinations):**
```
$ ls book/src/L2-L1/nrm2-leaf-identity.md book/src/L2-L1/scal-leaf-identity.md book/src/L3-L2/elementwise-product-body-identity.md
   No such file or directory (×3) — expected pre-rename
```

**Old-slug reference inventory (every reference rewritten by C2–C9):** grep for
`nrm2-fold-specialization`, `scal-fold-specialization`, `elementwise_product-body-identity` across
`book/src/` returned the complete set rewritten above (SUMMARY.md; L2/index.md; L2-L1/index.md;
L3-L2/index.md; the three renamed files' own H1/§Slug; the sibling themes
`reciprocal-leaf-identity`, `divfree-projector-leaf-identity`, `assemble-diagonal-leaf-identity`,
`nrm2-body-identity`, `scal-body-identity`, `elementwise-product-leaf-identity`; and
`L3/elementwise_product.md`). After integration, a confirming grep should return **zero** matches
for the three old slugs (and the `inner-product-fold-specialization` /
`linear-combination-fold-specialization` separate themes should remain untouched — they contain the
substring `fold-specialization` but are NOT renamed).

**Post-integration verification the integrator should run:**
```
# zero dangling old-slug refs (excluding the two not-renamed fold themes):
grep -rn 'nrm2-fold-specialization\|scal-fold-specialization\|elementwise_product-body-identity' book/src/   # expect: empty
# build clean:
cargo make book   # expect exit 0 (linkcheck2 resolves all renamed live links)
```

## Open questions / caveats

- **OQ `l3-index-audit-block-citation-drift` (NEW; surfaced, not enacted).** Beyond the 3 in-scope
  `:39`→`:46` self-citations, the cycle-036 audit-block shift left a broader `L3/index.md:NN`
  drift: `book/src/L3/reciprocal.md` cites `index.md:41` (×2) + `:40-45` (×2);
  `book/src/L3/assemble-diagonal.md` cites `index.md:39` (×4, the (A)-list line — now `:46`) +
  `:38-43` (×2); `book/src/L3/jacobi-smoother.md` cites `index.md:39` (×3) + `:38-43`;
  `book/src/L3/elementwise_product.md` cites `index.md:41`+`:53`+`:40-45`;
  `book/src/L3/normalize.md` cites `index.md:44`/`:45`/`:43-48`; `book/src/L3/orthogonalize.md`
  cites `index.md:47`. The live audit lines are now: `:45` (audit-block header), `:46` ((A) list),
  `:47` ((A) L1-gated), `:48` ((B) substantive), `:49` ((C) negative list). A dedicated
  index-citation-drift sweep (one lifter dispatch) should re-anchor all of these against
  `citecheck --anchor` — out of this dispatch's bounded (A)/(B)/(C) scope. NOTE the L3-L2 / L2-L1
  cohort already cites the *correct* `:46` (e.g. `jacobi-smoother-body-identity.md:184/:220/:262`,
  `L3-L2/index.md:19`), so the drift is confined to the L3 operator entries authored cycles 037-040.
- **No signature/law/decomposition contradiction surfaced.** Every (A) re-anchor was a pure clause
  swap; the L2 floor + L3>L2 theme signatures verified value-thread-isomorphic to the L3 entries
  (read on-disk). No abstractor reread is warranted — this was pure lifting, as scoped.
- **`scal-leaf-identity` / `nrm2-leaf-identity` content unchanged on the fold relationship.** The
  rename touched only the slug (H1/§Slug) and the slug-rationale sentence; the genuine
  fold-parent / consumer relationship prose (e.g. "degenerate arity-1 member of the
  `linear_combination` fold", "consumer of `inner_product` at `y=x`") is real content and was
  preserved verbatim. The §"Design fork" status of these two cycle-041 fold-parented edges (the
  batch-12 leaf-vs-fold adjudication) is unchanged by this rename — the rename is the slug-uniformity
  half of the meta decision, orthogonal to the leaf-vs-fold design question (which the cycle-042
  cross-cutter recommended resolving as KEEP-leaf-floor (b)).
