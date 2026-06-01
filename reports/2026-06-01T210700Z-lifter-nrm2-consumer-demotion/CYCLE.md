---
agent: lifter
invoked_at: 2026-06-01T210700Z
scope: L3>L2 + L2>L1 theme consumer-demotion (do-NOT-merge) — nrm2
status: integrated
integrated_at: 2026-06-01T22:14:50Z
integration_commit: 76721fec7a70c2ceed5e17de8c0f06ab3ad56205
integration_notes: "Applied clean by integrator-per-report (D3 of cycle-051); finalized cycle-051. nrm2-{body,leaf}-identity deleted; in-line CONSUMER notes on L3/nrm2 + L2/nrm2 (do-NOT-merge; std::abs guard preserved as load-bearing claim; Norml2 vector.hpp:255-260 anchor preserved); 3-way co-edit of KEPT divfree-projector-leaf-identity line 266 (nrm2- de-link); zero dangling live links to deleted slugs; build exit 0."
inputs:
  - book/src/L3-L2/nrm2-body-identity.md (DELETE)
  - book/src/L2-L1/nrm2-leaf-identity.md (DELETE)
  - book/src/L3/nrm2.md (add §"Downward to L2" consumer note)
  - book/src/L2/nrm2.md (add §"Downward to L1" consumer note)
  - book/src/L3-L2/index.md (remove dep-map row + cohort bullet)
  - book/src/L2-L1/index.md (remove dep-map row + cohort bullet)
  - book/src/SUMMARY.md (remove 2 lines)
  - book/src/L3-L2/divfree-projector-body-identity.md (de-link inbound; D4 file — EDIT DROPPED repair-phase: D4 deletes this file, edit is moot)
  - book/src/L2-L1/divfree-projector-leaf-identity.md (de-link inbound; D4 KEPT file — narrowed to distinct substring repair-phase for 3-way co-edit with D2/D4)
---

# CYCLE: Re-anchor / consumer-demote nrm2

## Summary

D3 of cycle-051 (LAST refactor-pass enactment of meta-batch-15, under the 2026-06-01 VOCABULARY-SHIFT REDIRECT). `nrm2` is the `√ ∘ abs ∘ inner_product` CONSUMER at `y=x` — explicitly **NOT a fold member** (do-NOT-merge carve-out per `L2/inner_product` §"Consumer (NOT an instance)" and `L2/nrm2` §"Consumer of `inner_product`, NOT a fold member"). Its two adjacent-edge identity themes — `nrm2-body-identity` (L3>L2) and `nrm2-leaf-identity` (L2>L1) — are degenerate identity-in-named-terms lowerings (the §1d smell the redirect names: same signature / laws / variant profile / value across each edge, the only textual delta being the inner-reduction NAME `dot`-leaf↔`inner_product`-fold and the `abs`-guard preserved/absorbed framing). Per the redirect these thin themes are demoted to **in-line consumer notes ON the `nrm2` entries themselves** (NOT absorbed into `inner_product` — `nrm2` is a consumer, not a member, so there is no fold to fold it into and no operator chapter collapses). This dispatch: **(a)** deletes the 2 theme files; **(b)** adds a §"Downward to L2" note on `L3/nrm2.md` + a §"Downward to L1" note on `L2/nrm2.md` recording the identity-in-form rotation, the consumer-not-member boundary, and the `std::abs` load-bearing guard as an explicit claim; **(c)** de-links the 2 inbound live links from D4's `divfree-projector-*` cohort-sibling references; **(d)** removes D3's own SUMMARY.md lines + dep-map rows in both indexes. The consolidated TALLY is DEFERRED to D5.

All edits are proposed-changes blocks; no direct `book/` writes this phase.

## Proposed changes

### (a) DELETE the 2 degenerate theme files

```delete:book/src/L3-L2/nrm2-body-identity.md
(delete entire file — degenerate identity-in-named-terms L3>L2 theme; content demoted to the in-line §"Downward to L2" note on book/src/L3/nrm2.md below)
```

```delete:book/src/L2-L1/nrm2-leaf-identity.md
(delete entire file — degenerate identity-in-named-terms L2>L1 theme; content demoted to the in-line §"Downward to L1" note on book/src/L2/nrm2.md below)
```

### (b1) DEMOTE-as-consumer note ON L3/nrm2.md — §"Downward to L2"

Insert a new section immediately AFTER the `## Lowers to` section's closing paragraph (after `book/src/L3/nrm2.md:130`, before `## Lifts from` at `:132`). The `lowers_to:` frontmatter line at `:6` is left unchanged (it already names the identity-in-form-on-the-primitive's-signature relationship and no longer needs a theme cross-reference). Also update the `## Lowers to` body so its forward-reference to the deleted L3>L2 theme is replaced by the in-line note.

```edit:book/src/L3/nrm2.md
[old]:
L3 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**. There is no L3-L1 lowering theme — no `book/src/L3-L1/` directory currently exists (precedent: cycle-010 `L3/krylov-step.md` records its identity-in-form lowering in-line at the entry, not in a separate theme file). The rotation work for this primitive lives in the surrounding wrapper at the consuming `krylov-step` body or outer convergence-test consumer, captured by [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (which names `nrm2` among the seven primitives that are "L3-native because [each primitive's] signature has no per-element loop visible").

The L1>L0 lowering of `nrm2` lives at the L1 entry's evidence section (`book/src/L1/nrm2.md` §Evidence) — Palace's `linalg::Norml2` template at `palace/linalg/vector.hpp:255-260` is the one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`; the `std::abs` outer guard is a load-bearing defensive non-negativity check against floating-point round-off pushing the sum slightly negative; the inner `Dot` carries the MPI_Allreduce. None of this is L3 content; the L3 form sees a single-step whole-tensor reduction.
[new]:
L3 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**. There is no L3-L1 lowering theme — no `book/src/L3-L1/` directory currently exists (precedent: cycle-010 `L3/krylov-step.md` records its identity-in-form lowering in-line at the entry, not in a separate theme file). The rotation work for this primitive lives in the surrounding wrapper at the consuming `krylov-step` body or outer convergence-test consumer, captured by [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (which names `nrm2` among the seven primitives that are "L3-native because [each primitive's] signature has no per-element loop visible").

The L1>L0 lowering of `nrm2` lives at the L1 entry's evidence section (`book/src/L1/nrm2.md` §Evidence) — Palace's `linalg::Norml2` template at `palace/linalg/vector.hpp:255-260` is the one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`; the `std::abs` outer guard is a load-bearing defensive non-negativity check against floating-point round-off pushing the sum slightly negative; the inner `Dot` carries the MPI_Allreduce. None of this is L3 content; the L3 form sees a single-step whole-tensor reduction.

### Downward to L2 (consumer identity-in-form; no theme file)

L3 `nrm2` lowers to L2 [`nrm2`](../L2/nrm2.md) as **identity-in-form on the primitive's signature**. There is no dedicated L3>L2 theme file: the rotation is a degenerate identity-in-named-terms lowering (the only textual delta is the inner-reduction NAME), so under the 2026-06-01 vocabulary-shift redirect it is recorded here in-line rather than as a thin theme.

- **`nrm2` is a CONSUMER of `inner_product`, not a fold member.** At L2 the defining identity is written through the `inner_product` fold at the diagonal — `nrm2 x = √ (abs (inner_product x x))`, the `√ ∘ abs ∘ inner_product` composition at `y = x`. `nrm2` post-composes two scalar maps (`abs`, then `√`) onto the fold's scalar output; it does NOT itself fold and is NOT a member of the fold cohort. Merging `nrm2` into `inner_product` would be a category error (the do-NOT-merge boundary, carried in the [`inner_product`](../L2/inner_product.md) dep-map row and [`L2/index`](../L2/index.md) §"Fold-cohort boundary"). The L2 entry lists `inner_product` under `consumes`, never as a fold the operator instantiates.
- **The only textual change L3 → L2 is the inner-reduction name.** L3 writes the defining identity through the same-layer `dot(x, x)` leaf (`L3/nrm2` §Dependencies); L2 writes it through the `inner_product(x, x)` fold at the diagonal `y = x`. These denote the same Hermitian self-inner-product value (`dot(x, x) = inner_product(x, x)` at `y = x` — the inner-product fold's diagonal degeneration, [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The diagonal degeneration (`y = x`)"). The signature `Tensor[N] -> Scalar` is identical at both layers; no element loop is exposed at either (the reduction over the length axis is a single semantic step), so the rotation is identity-in-form with **no wrapper to rotate** (`nrm2` is a leaf reduction — there is no `(op, K, s)` tuple or outer loop, strictly simpler than `krylov-step-body-identity`). `nrm2` is L3-native / L2-native by signature shape per [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (`:97`).
- **The `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim at L2** (it is implicit at L3, subsumed by the non-negativity claim). The guard is a no-op in exact arithmetic but load-bearing in floating point — it strips a sign that round-off in the reduction could have flipped negative on a numerically-zero vector, buying domain-safety for `√` (no NaN). Both framings are consistent (the guard implements the non-negativity invariant); the full classification lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive guard — classification".

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`): `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the L3>L2 rotation identity-in-form. (Path relative to `reference/palace/`; full L0 evidence at [`L1/nrm2`](../L1/nrm2.md) §Evidence.)
```

### (b2) DEMOTE-as-consumer note ON L2/nrm2.md — §"Downward to L1"

Update the `## Lowers to` section on `L2/nrm2.md` (`:122-124`) to replace the forward-reference to the deleted `nrm2-leaf-identity` theme with the in-line consumer note. The `lowers_to:` frontmatter at `:5-6` is updated to drop the "narrated by the D5 L2-L1 theme" clause. The `## Lifts from` section's reference to the deleted L3-L2 theme (`:126-128`) is also re-anchored to the in-line note.

```edit:book/src/L2/nrm2.md
[old]:
lowers_to:
  - book/src/L1/nrm2.md (identity-in-form on the primitive's signature; the L2>L1 nrm2 rotation is narrated by the D5 L2-L1 theme — see Lowers-to)
[new]:
lowers_to:
  - book/src/L1/nrm2.md (identity-in-form on the primitive's signature; the L2>L1 rotation is a degenerate identity-in-named-terms lowering recorded in-line at §"Lowers to" / §"Downward to L1" — no theme file per the 2026-06-01 vocabulary-shift redirect)
```

```edit:book/src/L2/nrm2.md
[old]:
L2 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**. The fusion rotation L2→L1 is a no-op on the buffer side (there is no destination buffer for `nrm2` — the result is a returned scalar; per [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) the "mutation rotation" is essentially nothing on the buffer side, and the fusion rotation likewise has no fused kernel to unfold). The L2>L1 rotation is narrated forward by the D5 L2-L1 `nrm2` lowering theme this cycle (`book/src/L2-L1/`); this entry cites it for the rotation work and does not restate it. The L1>L0 lowering — Palace's `linalg::Norml2` template at `palace/linalg/vector.hpp:255-260` expanding into the four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain — lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md). None of that is L2 content; the L2 form sees a single-step fold consumed by two scalar maps.
[new]:
L2 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**. The fusion rotation L2→L1 is a no-op on the buffer side (there is no destination buffer for `nrm2` — the result is a returned scalar; per [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) the "mutation rotation" is essentially nothing on the buffer side, and the fusion rotation likewise has no fused kernel to unfold). The L2>L1 rotation is a degenerate identity-in-named-terms lowering, recorded in-line in §"Downward to L1" below rather than as a thin theme file (per the 2026-06-01 vocabulary-shift redirect). The L1>L0 lowering — Palace's `linalg::Norml2` template at `palace/linalg/vector.hpp:255-260` expanding into the four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain — lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md). None of that is L2 content; the L2 form sees a single-step fold consumed by two scalar maps.

### Downward to L1 (consumer identity-in-form; no theme file)

L2 `nrm2` re-fuses downward onto the single L1 leaf [`nrm2`](../L1/nrm2.md) (firm cycle-003) as **identity-in-form on the primitive's signature** — value-thread-isomorphic, with **no dispatch** (one L1 leaf — there is no L1 family to dispatch into, contrast the `dot`/`tdot` inner-product cohort), **no decomposition** (the L2 fusion rotation is a no-op — `linalg::Norml2` is already the one-line unfolded composition), and **no destination-buffer concern** (the result is a returned scalar). What the hop does is two surface adjustments, both value-preserving:

1. **The `inner_product` fold at `y = x` re-fuses to the `dot` leaf at the diagonal.** L2 names the inner reduction as the length-axis `inner_product` fold (firm cycle-019); at L1 the same diagonal self-inner-product is the `dot(x, x)` leaf (the defining identity `nrm2(x) = √dot(x, x)`, L1 algebraic law 8, `book/src/L1/nrm2.md:53`). This is the **consumer's** view of the edge [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The diagonal degeneration (`y = x`)" lowers for the fold itself — that theme names `nrm2` precisely as the consumer entry point (`√ ∘ inner_product` at `y = x`, with the outer `√` a post-step "downstream of this lowering, not a dispatch within it"). The inner `inner_product(x, x) → dot(x, x)` re-fusion is inherited from the inner-product theme; the `nrm2`-specific content is the outer `√ ∘ abs` post-step. **`nrm2` is a CONSUMER of `inner_product`, not a fold member** (do-NOT-merge per [`L2/inner_product`](./inner_product.md) §"Consumer (NOT an instance)" and §"Consumer of `inner_product`, NOT a fold member" above); the namesake "fold" is the one `nrm2` *consumes* at `y = x`, not one it instantiates.
2. **The two scalar post-steps change framing, not value.** At L2 the `abs` guard is **preserved as an explicit load-bearing numerical claim** and the `√` is the principal non-negative real square root composed onto the fold output. At L1 both drop **below the layer's resolution**: the `abs` guard **disappears**, subsumed by the L1 algebraic claim that `dot(x, x)` is non-negative real (so `abs` of it equals it exactly in exact arithmetic), and the `√` is a deterministic IEEE-754 scalar primitive on the leaf's output ([`L1/nrm2`](../L1/nrm2.md) §Dependencies, `:66`). Both treatments are consistent — the guard *implements* the non-negativity claim under floating point; it is a no-op in exact arithmetic and is **NOT erasable in floating point** without introducing a NaN failure mode on numerically-zero vectors. The full load-bearing-defensive classification (property bought = domain-safety / non-negativity invariant for `√`, no NaN) lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive guard — classification", where the guard re-materializes as stage 3 of the four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain.

The mapping is total and trivial on the kernel content: the single L2 `nrm2` form maps to the single L1 `nrm2` leaf, same signature, same value, same defining identity (law 8). The element-type axis is collapsed identically at both layers (one operator, always-real result — the post-composed `abs` projects the complex self-inner-product onto its real magnitude before `√`). This is the **identity-in-form** property; the rotation is at the framing (preserved-`abs` fusion-rotation view at L2 → absorbed-`abs` mutation-rotation view at L1), not on the primitive.

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`): `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the L2>L1 fusion rotation a no-op. (Path relative to `reference/palace/`; full L0 evidence at [`L1/nrm2`](../L1/nrm2.md) §Evidence.)
```

```edit:book/src/L2/nrm2.md
[old]:
L2 `nrm2` lifts from / to L3 [`nrm2`](../L3/nrm2.md) (firm cycle-011) as **identity-in-form**. L3 is the iteration-rotation layer; its `nrm2` is the same whole-tensor reduction with the iteration view of the *surrounding* consuming context (the [`krylov-step`](./krylov-step.md) body's residual-norm readout / Arnoldi sub-diagonal) rendered explicitly. The L3>L2 rotation on the primitive itself is identity-in-form, captured by the D5 L3-L2 `nrm2` theme this cycle (and structurally justified by [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3, which names `nrm2` among the seven primitives that are L2-native / L3-native because each signature has no per-element loop visible). `nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict); at L4 it appears inside larger composed entries (e.g. `book/src/L4/krylov-step.md` §Semantics, `outputs.residual_norm`) as a let-binding consuming the L3-native primitive surface.
[new]:
L2 `nrm2` lifts from / to L3 [`nrm2`](../L3/nrm2.md) (firm cycle-011) as **identity-in-form**. L3 is the iteration-rotation layer; its `nrm2` is the same whole-tensor reduction with the iteration view of the *surrounding* consuming context (the [`krylov-step`](./krylov-step.md) body's residual-norm readout / Arnoldi sub-diagonal) rendered explicitly. The L3>L2 rotation on the primitive itself is identity-in-form, recorded in-line at the L3 entry's §"Downward to L2" note (no theme file per the 2026-06-01 vocabulary-shift redirect; structurally justified by [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3, which names `nrm2` among the seven primitives that are L2-native / L3-native because each signature has no per-element loop visible). `nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict); at L4 it appears inside larger composed entries (e.g. `book/src/L4/krylov-step.md` §Semantics, `outputs.residual_norm`) as a let-binding consuming the L3-native primitive surface.
```

Also re-anchor the §Evidence bullet on `L2/nrm2.md` that names the deleted L3-L2 theme structural justification — it already cites `krylov-step-body-identity` directly (`:139`), so no `nrm2-body-identity` reference exists in the evidence list to fix. (Verified: the only theme-file references in `L2/nrm2.md` are to `krylov-step-body-identity` and `inner-product-fold-specialization`, both surviving; the two deleted-theme references are only the two edited above.)

### (c) Re-anchor inbound live links from D4's divfree-projector cohort-sibling references

These are cohort-sibling cross-references that name the now-deleted `nrm2-*` slugs as members of the BLAS-1 `-body-identity` / `-leaf-identity` cohort. De-link defensively: drop the `nrm2-*` live link, keeping the surviving siblings (`dot-*`, `scal-*`) as the cohort exemplars. **[REPAIRED cycle-051 repair-phase:** only the `-leaf-identity` edit survives — the `-body-identity` edit was dropped as MOOT because D4 deletes `book/src/L3-L2/divfree-projector-body-identity.md` wholesale this cycle (see the repair note below). The `-leaf-identity` edit was additionally narrowed to a distinct token-substring to compose order-independently with D2's overlapping `dot-leaf-identity` de-link on the same line.**

**[REPAIRED cycle-051 repair-phase — D3's edit to `book/src/L3-L2/divfree-projector-body-identity.md` was DROPPED as MOOT.]** Sibling **D4** (`reports/2026-06-01T210700Z-lifter-jacobi-divfree-demotion/CYCLE.md`, `delete:book/src/L3-L2/divfree-projector-body-identity.md` at its report `:36`) DELETES `book/src/L3-L2/divfree-projector-body-identity.md` wholesale this cycle. D3's de-link of the inbound `nrm2-body-identity` live link inside that file is therefore a no-op against a deleted target — the link dies with the file. Edit removed to avoid a serial-apply collision against a deleted file. (Only the `-leaf-identity` de-link below survives, since D4 KEEPS `book/src/L2-L1/divfree-projector-leaf-identity.md`.)

```edit:book/src/L2-L1/divfree-projector-leaf-identity.md
[old]:
[`nrm2-leaf-identity`](./nrm2-leaf-identity.md)
[new]:
`nrm2-leaf-identity` (demoted cycle-051 to an in-line consumer note on `book/src/L2/nrm2.md` §"Downward to L1" under the 2026-06-01 vocabulary-shift redirect)
```

**[REPAIRED cycle-051 repair-phase — D3's `-leaf-identity` de-link was NARROWED to a distinct substring.]** The KEPT `book/src/L2-L1/divfree-projector-leaf-identity.md` is a **3-way co-edit** this cycle: **D2** (`reports/2026-06-01T210700Z-lifter-inner-product-dot-demotion/CYCLE.md`, 3rd block at its report `:271-275`) de-links the `dot-leaf-identity` token on the SAME cohort-tuple line (on-disk `:266`); **D3** (this report) de-links the `nrm2-leaf-identity` token on that same line; **D4** (`…jacobi-divfree-demotion`, its `:265-269`) re-anchors the live link to `divfree-projector-body-identity` at on-disk `:36` (a DISTINCT line, no overlap). D2 and D3 BOTH rewrite on-disk line `:266` (`([\`dot-leaf-identity\`](…) / [\`nrm2-leaf-identity\`](…)`). D3's original full-tuple `[old]`/`[new]` (which kept `dot-leaf-identity` live) would COLLIDE with D2's full-tuple edit (which keeps `nrm2-leaf-identity` live). To make serial application order-independent, D3's edit is narrowed to touch ONLY the `[\`nrm2-leaf-identity\`](./nrm2-leaf-identity.md)` substring (above) — D2's edit narrows to the `dot-leaf-identity` substring on the same line — so the two compose to the correct final state (both `dot-` and `nrm2-` de-linked, `scal-leaf-identity` left live) regardless of apply order. **INTEGRATOR: apply D2's, D3's, and D4's edits to this file as three narrow substring replacements; the D2+D3 pair both touch line `:266` but on disjoint tokens.** (D2 must also be repaired to a narrow `dot-leaf-identity` substring for full order-independence; the integrator should confirm D2's repaired form likewise targets only its own token.)

### (d) Remove D3's own SUMMARY.md lines + dep-map rows in both indexes

#### SUMMARY.md — remove the 2 lines (de-link AND physically remove)

```edit:book/src/SUMMARY.md
[old]:
- [axpbypcz-body-identity](./L3-L2/axpbypcz-body-identity.md)
- [nrm2-body-identity](./L3-L2/nrm2-body-identity.md)
- [ksp-solve-outer-driver](./L3-L2/ksp-solve-outer-driver.md)
[new]:
- [axpbypcz-body-identity](./L3-L2/axpbypcz-body-identity.md)
- [ksp-solve-outer-driver](./L3-L2/ksp-solve-outer-driver.md)
```

```edit:book/src/SUMMARY.md
[old]:
- [axpbypcz-leaf-identity](./L2-L1/axpbypcz-leaf-identity.md)
- [nrm2-leaf-identity](./L2-L1/nrm2-leaf-identity.md)
- [jacobi-smoother-leaf-identity](./L2-L1/jacobi-smoother-leaf-identity.md)
[new]:
- [axpbypcz-leaf-identity](./L2-L1/axpbypcz-leaf-identity.md)
- [jacobi-smoother-leaf-identity](./L2-L1/jacobi-smoother-leaf-identity.md)
```

#### L3-L2/index.md — remove dep-map row (`:15`) + cohort bullet (`:40`)

```edit:book/src/L3-L2/index.md
[old]:
| [`nrm2-body-identity`](./nrm2-body-identity.md) | L3 [`nrm2`](../L3/nrm2.md) §Signature — whole-tensor Euclidean-norm reduction `nrm2 x = √dot(x, x)`, signature `Tensor[N] -> Scalar` with no element loop; consumed-inside roles (residual-norm readout + Arnoldi sub-diagonal) belong to the surrounding `krylov-step` body, not the leaf. | L2 [`nrm2`](../L2/nrm2.md) §Signature — fusion-rotation form `nrm2 x = √ (abs (inner_product x x))` at `y=x`; `√ ∘ abs ∘ inner_product` CONSUMER of the fold (NOT a fold member), `std::abs` guard preserved as explicit load-bearing claim. | `structural` (each form is `Tensor[N] -> Scalar` — whole-tensor by construction, no per-element loop; `nrm2` L3-native/L2-native by signature shape per [`krylov-step-body-identity`](./krylov-step-body-identity.md) point 3) + secondary `empirical-match` (cycle-002 combinator-miner claim re cycle-006 audit) | `firm` (cycle-041 wave-2 abstractor D5; BLAS-1-leaf analogue of `krylov-step-body-identity` — leaf case, NO wrapper rotation; completes the adjacent edge below the firm L3 anchor under the `l2-floor-under-l3-leaf-cohort` directive) |
| [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) |
[new]:
| [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) |
```

```edit:book/src/L3-L2/index.md
[old]:
- `nrm2-body-identity` — the L3 whole-tensor `nrm2` norm lowers to the L2 `√ ∘ abs ∘ inner_product` consumer floor; the only textual change is the inner-reduction name (`dot` leaf at L3 → `inner_product` fold at the diagonal at L2) + the surfacing of the `abs` guard as an explicit L2 claim.
- `scal-body-identity` — the L3 whole-tensor `scal` field operation lowers to the L2 base scalar-vector-multiply floor leaf (arity-1 fold member); the body IS the identity, there is no wrapper to rotate.
[new]:
- *(demoted cycle-051)* `nrm2-body-identity` — DEMOTED to an in-line §"Downward to L2" consumer note on `book/src/L3/nrm2.md` (degenerate identity-in-named-terms; `nrm2` is the `√ ∘ abs ∘ inner_product` CONSUMER at `y=x`, NOT a fold member — the do-NOT-merge consumer carve-out, demoted onto the `nrm2` entry itself, NOT absorbed into `inner_product`; the `std::abs` load-bearing guard is preserved as an explicit claim in the in-line note). No longer a theme file.
- `scal-body-identity` — the L3 whole-tensor `scal` field operation lowers to the L2 base scalar-vector-multiply floor leaf (arity-1 fold member); the body IS the identity, there is no wrapper to rotate.
```

#### L2-L1/index.md — remove dep-map row (`:21`) + cohort bullet (`:55`)

```edit:book/src/L2-L1/index.md
[old]:
| [nrm2-leaf-identity](./nrm2-leaf-identity.md) | `L2/nrm2` (firm cycle-041) | `L1/nrm2` (firm cycle-003; single leaf — no L1 family to dispatch) | firm *(structural; thin-identity — BLAS-1-leaf consumer sibling of `inner-product-fold-specialization`; `nrm2` = `√ ∘ abs ∘ inner_product` CONSUMER at `y=x`, NOT a fold member; no dispatch / no decomposition / no destination buffer; `√`/`abs` scalar post-steps drop below L1 resolution + `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1; renamed cycle-043 from `nrm2-fold-specialization`)* |
| [jacobi-smoother-leaf-identity](./jacobi-smoother-leaf-identity.md) |
[new]:
| [jacobi-smoother-leaf-identity](./jacobi-smoother-leaf-identity.md) |
```

```edit:book/src/L2-L1/index.md
[old]:
- `nrm2-leaf-identity` (renamed cycle-043 from `nrm2-fold-specialization`) — the L2 `nrm2` floor lowers to the single L1 `nrm2` leaf; the BLAS-1-leaf **consumer** sibling of `inner-product-fold-specialization` (`nrm2 = √ ∘ abs ∘ inner_product` at `y=x`, NOT a fold member; no dispatch / no decomposition / no buffer); `√`/`abs` post-steps drop below L1 resolution, `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1.
- `scal-leaf-identity` (renamed cycle-043 from `scal-fold-specialization`) — the L2 `scal` floor lowers to the L1 `scal` leaf; the degenerate **arity-1 single-term shadow** of `linear-combination-fold-specialization` (no arity dispatch, no pinned-summation-order residue — one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged.
[new]:
- *(demoted cycle-051)* `nrm2-leaf-identity` — DEMOTED to an in-line §"Downward to L1" consumer note on `book/src/L2/nrm2.md` (degenerate identity-in-named-terms; `nrm2` is the `√ ∘ abs ∘ inner_product` CONSUMER at `y=x`, NOT a fold member — the do-NOT-merge consumer carve-out, demoted onto the `nrm2` entry itself, NOT absorbed into `inner_product`; `√`/`abs` post-steps drop below L1 resolution, `std::abs` guard preserved-as-claim at L2 → absorbed-by-non-negativity-claim at L1, preserved in the in-line note). No longer a theme file.
- `scal-leaf-identity` (renamed cycle-043 from `scal-fold-specialization`) — the L2 `scal` floor lowers to the L1 `scal` leaf; the degenerate **arity-1 single-term shadow** of `linear-combination-fold-specialization` (no arity dispatch, no pinned-summation-order residue — one term ⇒ one rounding, value+bit-exact); arity-1 fold member cited NOT merged.
```

## Discipline notes

- **Consumer-demotion, NOT fold-absorption (the load-bearing do-NOT-merge carve-out).** Per the dispatch directive and `L2/inner_product` §"Consumer (NOT an instance)" / `L2/nrm2` §"Consumer of `inner_product`, NOT a fold member" (`book/src/L2/nrm2.md:27-35`), `nrm2 = √ ∘ abs ∘ inner_product` at `y=x` is a CONSUMER of the fold, not a member of it. The demoted notes therefore land ON the `nrm2` entries themselves (L3/nrm2 §"Downward to L2", L2/nrm2 §"Downward to L1"), exactly as the fold-family `dot`/`scal`/`axpy*` leaves are being collapsed INTO their fold-parents (`inner_product` / `linear_combination`) by D1/D2 — but `nrm2` is NOT so collapsed (no operator chapter collapses; only the 2 thin theme files delete). I did not touch `inner_product`, `L1/nrm2`, or any fold entry.
- **Both deleted themes carried zero load-bearing facts not already in the operator entries.** Their entire content was the identity-in-form narration + the `std::abs`-guard claim + the inner-reduction-name delta + the consumer-not-member framing — all of which is already present in `L2/nrm2.md` §Semantics/§Dependencies/§"Consumer of `inner_product`, NOT a fold member" and `L3/nrm2.md` §Semantics/§Dependencies. The new in-line notes consolidate that narration at the demotion site; nothing is lost. The `std::abs` load-bearing guard is preserved as an explicit claim in BOTH new notes (directive requirement).
- **Direction discipline (high→low).** Both new notes are titled §"Downward to L_n" and narrate the rewrite forward (L3 into L2; L2 into L1), per CLAUDE.md §Methodology invariants "Layers are defined high→low". No reverse-lift prose in the formal entries.
- **Citation self-verification.** The single L0 citation reused in both notes — `palace/linalg/vector.hpp:255-260` (`Norml2` body, `std::sqrt(std::abs(Dot(...)))` at line 259) — was verified on-disk this dispatch with `python3 tools/citecheck/citecheck.py palace/linalg/vector.hpp:255-260 --anchor Norml2` → `[ok] anchor at line(s) [257] within range 255-260` and `--anchor sqrt` on `:259` → `[ok] anchor at line(s) [259]`. All other citations in the notes are intra-book cross-references to surviving entries (verified present this dispatch: `L1/nrm2.md:53` law 8, `:66` abs/sqrt-below-resolution, `inner-product-fold-specialization`, `nrm2-mutation-rotation`, `krylov-step-body-identity:97`).
- **No prose-correction landed.** I found no backward conventions / drifted citations / contradicted claims in the entries during re-anchoring; this is a pure structural demotion.
- **Inbound-link sweep.** Grepped `book/src/` for both deleted slugs. Live links (`[...](...)`): exactly the 2 dep-map rows (mine, directive d) + the 2 D4 cohort-sibling references (directive c) — all re-anchored above. The L2/index.md cohort-growth-log mentions (`:118`/`:121`/`:123`) are bare-code-span historical narrative, NOT live links (verified via `grep "](...nrm2-*-identity"`); editing append-only historical narrative is out of my scope and they do not break `linkcheck2`. Left untouched; flagged to D5 below.

## Supporting evidence

- Deleted theme files (read in full this dispatch): `book/src/L3-L2/nrm2-body-identity.md`, `book/src/L2-L1/nrm2-leaf-identity.md`.
- Operator entries receiving in-line notes: `book/src/L3/nrm2.md` (§"Lowers to" at `:126-130`, insert after), `book/src/L2/nrm2.md` (§"Lowers to" at `:122-124` + §"Lifts from" at `:126-128`, edited).
- Consumer-not-member boundary source: `book/src/L2/nrm2.md:27-35` + `book/src/L2/inner_product.md` dep-map row (do-NOT-merge).
- L0 anchor: `reference/palace/palace/linalg/vector.hpp:255-260` (`Norml2`), verified via `tools/citecheck/citecheck.py --anchor`.
- D4 cohort-sibling inbound links: `book/src/L3-L2/divfree-projector-body-identity.md:230-232`, `book/src/L2-L1/divfree-projector-leaf-identity.md:265-267`.
- Cross-report split context: `book/src/L2-L1/index.md:73` (the cycle-050 demotion log + the cycle-050-vs-051 split note: "`nrm2-leaf-identity` STAYS — `nrm2` is a do-NOT-merge consumer"). NOTE the dispatch directive supersedes that "STAYS" framing — cycle-051 DOES demote `nrm2`'s themes, but **as a consumer onto the `nrm2` entry**, NOT by folding into `inner_product`; the "STAYS" in the c050 log meant "stays NOT-merged-into-the-fold", which the consumer-demotion honors.

## Open questions / caveats

- **OQ-1 (for D5 consolidated tally — DEFERRED per directive).** This dispatch drops 1 firm L3>L2 theme (`nrm2-body-identity`) and 1 firm L2>L1 theme (`nrm2-leaf-identity`). D5 must fold these into the consolidated batch-15 demotion count and update: (i) the L3-L2 §"Vocabulary cohort" firm count + the `l3-l2-rotation-theme-coverage-gap` denominator narrative; (ii) the L2-L1 §"Cohort growth log" running count at `index.md:73` (`firm 17 → ...` after cycle-051's deletions across D1–D4); (iii) the L2/index.md cohort-growth-log historical mentions at `:118`/`:121`/`:123` IF a consolidated narrative refresh is in D5's scope (they are bare-code-span historical prose, not live links — non-blocking for the build, but they still NAME the now-deleted slugs as firm themes, so a one-line "(demoted cycle-051)" annotation there would keep the narrative honest). I left all tally/count edits and the historical-narrative refresh to D5 to avoid cross-dispatch write collisions.
- **OQ-2 (D4 + D2 collision — RESOLVED repair-phase).** Directive (c) originally had me de-link the 2 inbound references inside D4's files. The repair-phase resolved both:
  - **`book/src/L3-L2/divfree-projector-body-identity.md` — EDIT DROPPED (moot).** D4 (`…lifter-jacobi-divfree-demotion`, its `delete:` at report `:36`) DELETES this file wholesale; D3's de-link is a no-op against a deleted target. Removed.
  - **`book/src/L2-L1/divfree-projector-leaf-identity.md` — KEPT by D4, edit NARROWED + RETAINED.** This is a **3-way co-edit**: D2 (`…lifter-inner-product-dot-demotion`) de-links `dot-leaf-identity` on on-disk line `:266`; D3 (this report) de-links `nrm2-leaf-identity` on that SAME line `:266`; D4 re-anchors the `:36` `divfree-projector-body-identity` link (distinct line, no overlap). D3's original full-cohort-tuple `[old]`/`[new]` overlapped D2's. Repaired: D3's edit narrowed to the unique substring `[\`nrm2-leaf-identity\`](./nrm2-leaf-identity.md)` so D2 and D3 compose order-independently to the correct final state (`dot-` and `nrm2-` both de-linked, `scal-leaf-identity` left live). INTEGRATOR: apply D2/D3/D4 as three narrow substring replacements; confirm D2's repaired form likewise targets only its own `dot-leaf-identity` token on `:266`.
- **No abstractor reread needed.** The firmed-up signature is unchanged (the operator entries already carry the consumer framing); this is a pure structural demotion of degenerate identity themes, no content decision made.
