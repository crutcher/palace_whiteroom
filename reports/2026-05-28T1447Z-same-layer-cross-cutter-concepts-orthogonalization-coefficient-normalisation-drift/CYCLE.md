---
agent: same-layer-cross-cutter
invoked_at: 2026-05-28T14:47Z
scope: L1 cross-cut — concepts/orthogonalization vs firm L1/orthogonalize coefficient/normalisation drift
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: a4d7495
integration_notes: "cycle-013 finalize. Position 11 of 11. Full-file rewrite of concepts/orthogonalization.md aligned to the firm L1/orthogonalize 'does not normalize output' contract (3 inconsistent coefficient-lengths collapsed to length-m; duplicate block removed; stale 'separate slice' framing replaced). The 3 links to L1-L0/orthogonalize-mutation-rotation.md resolve (report 6 landed it earlier this cycle). cross-cutter→concept-rewrite plan-kind stretch applied-direct (safety-gated). Closes OQ concepts-orthogonalization-coefficient-normalisation-drift."
---

# CYCLE: L1 observation — concepts/orthogonalization coefficient/normalisation drift

## Summary

Comparing the concept page `book/src/concepts/orthogonalization.md` against the firm L1
operator `book/src/L1/orthogonalize.md` (cycle-012) surfaces a **contradiction** on the
coefficient/normalisation boundary plus stale pre-layered framing. The concept page (a)
folds the caller's `nrm2` sub-diagonal `h_{j+1} = ‖w'‖` into the operator's coefficient
output, conflating the operator's length-`m` coefficient vector `H` with the caller's
normalisation step; (b) carries a **second, duplicate concept block** (lines 26-63) whose
canonical signature says "`w` may be mutated" (L0 mutating framing, contradicting the pure
L1 form) and "`h_coeffs` is a length-`j` vector" (a third, mutually-inconsistent coefficient
length); and (c) cites the orthogonalisation family as a "separate slice" / "dedicated
`orthog` slice would carry…", framing that predates both the firm L1 entry and the
cycle-013 wave-1 `orthogonalize-mutation-rotation` L1>L0 theme. The L1 entry already names
this drift authoritatively (its own §"Evidence" line and OQ "concepts/orthogonalization.md
coefficient/normalisation drift"). The wave-1 abstractor theme is fully consistent with the
L1 entry (3 variant loop-structures, "does not normalize output", length-`m` `H` distinct
from the caller's `nrm2`), so the concept page is the lone drifting artifact. Verdict:
**drift-found-with-corrections**.

## Observation kind

**Contradiction** — `concepts/orthogonalization.md` and the firm `L1/orthogonalize.md` carry
conflicting semantics on (i) what the coefficient output contains (length-`m` projection
coefficients vs a Hessenberg column with the `‖w'‖` sub-diagonal folded in) and (ii) whether
the operator mutates `w` (the duplicate block's signature says it may; the L1 contract says
the operator is pure and `w'` is a fresh value). Secondary: stale framing (the page treats
the layered entry as a not-yet-existing "separate slice").

## Specific finding

Four concrete drift points in `book/src/concepts/orthogonalization.md`, against the
authoritative `book/src/L1/orthogonalize.md`:

1. **Normalisation / coefficient-length conflation (line 3).** The page defines the output as
   `(w', h)` where `h = (h_0, …, h_{j+1})` "entries of the Hessenberg matrix's new column,
   with `h_{j+1} = ‖w'‖`". The L1 entry is explicit (`orthogonalize.md:30-33`, OQ at
   `:326-335`): the operator returns the **length-`m`** coefficient vector `H` only;
   `H[j+1] = ‖w'‖` is the **caller's** `nrm2(w')` sub-diagonal step (`arnoldi_step`), NOT a
   product of this operator, which **does not normalise its output** (`orthog.hpp:18-23`
   "does not normalize the output vectors!"). The concept page's `(h_0, …, h_{j+1})`
   (length `j+2`) folds the caller's normalisation into the operator's contract — a direct
   contradiction of the firm entry.

2. **Duplicate concept block with a contradictory L0-flavoured signature (lines 26-63).**
   The page contains a *second* "## Concept: `orthogonalization` (Gram-Schmidt variants)"
   block (lines 26-63) — its own Background, Variants, Signature, Slices sections that
   restate (and partly re-contradict) the first block. Its "Signature (canonical)" (lines
   52-55) reads `orthogonalize(variant, V_basis, w) → (h_coeffs, w')` with the comment
   "`w` may be mutated; `h_coeffs` is a length-`j` vector". This contradicts the L1 entry on
   two counts: (a) the L1 form is **pure** — `w'` is a fresh value, `w` is read-only
   (`orthogonalize.md:51`, §"L1 vs L0" `:238` "no in-place overwrite of `w`"); "`w` may be
   mutated" is L0 framing leaking into the concept layer. (b) "length-`j`" is a **third**
   coefficient length in the same file (line 3 implies `j+2`; line 15's signature implies
   `m = j+1`; line 54 says `j`), so the page is internally inconsistent on the single most
   load-bearing fact. The L1 entry fixes this as **length `m`** (`orthogonalize.md:58-59`).
   The argument order also differs between the two blocks (line 15 `(gs_orthog, V, w)`
   returning `(w', h)`; line 53 `(variant, V_basis, w)` returning `(h_coeffs, w')`).

3. **Stale "separate slice" / "dedicated `orthog` slice would carry" framing (lines 19, 23).**
   Line 19: "A dedicated `orthog` slice would carry the L2→L3 unfolding…" — the slice exists
   (`book/src/spec/slices/orthog.md`, cycle-011 partial reduction). Line 23: cites the
   `OrthogonalizeColumn{MGS,CGS,CGS2}` family as "(separate slice)" — the firm L1 entry now
   IS the authoritative layered home; the citation should point at it. This is pre-layered-era
   framing, not a semantic contradiction, but it leaves a reader unaware the firm entry exists.

4. **Variant-axis framing is otherwise correct but doubly-stated.** Both blocks list
   MGS/CGS/CGS2 with consistent stability/synchronisation framing (lines 9-11 and 37-45),
   agreeing with the L1 entry's variant axis and the wave-1 theme's three loop-structures. The
   only variant-level drift is the redundancy (two Variants sections) and line 47-48's claim
   that the enum is "on the GMRES solver" (the L1/theme show it is bound at solver setup and
   dispatched via `OrthogonalizeIteration`, reused by the ROM path too —
   `orthogonalize.md:14-16, 54-55, 264-267`, theme §"L0 form" — so "on the GMRES solver" is too narrow).

The wave-1 `orthogonalize-mutation-rotation` theme
(`reports/2026-05-28T0915Z-abstractor-orthogonalize-mutation-rotation-l1-l0-theme/CYCLE.md`)
is **consistent** with the L1 entry on every point checked: 3 variant loop-structures
(MGS single interleaved / CGS split two-phase / CGS2 doubled), "does not normalize output"
(applicability condition 3, lines 209-213), and the caller-owned `H` distinct from the
`nrm2` sub-diagonal. No drift between the theme and the L1 entry; the concept page is the
lone outlier.

## Recommendation

**Dispatch layer-intro-author to refresh `book/src/concepts/orthogonalization.md`** — collapse
the duplicate block into one coherent concept page aligned to the firm L1 entry's
coefficient/normalisation contract, fix the length-`m` coefficient convention, drop the
"`w` may be mutated" L0 leak, and refresh the stale slice references to point at the firm
`L1/orthogonalize` entry. Concept pages are layer-intro-author territory (per the
write-authority partition), so the proposed-changes block below is a surgical alignment the
integrator-per-report can apply directly; treat it as the layer-intro-author deliverable for
this OQ. This **closes** the L1 entry's pre-flagged OQ "`concepts/orthogonalization.md`
coefficient/normalisation drift" (`orthogonalize.md:331-335`).

The correction is a near-total rewrite *because the page currently holds two overlapping
concept blocks*; the new content is short, single-block, and defers all mechanics to the L1
entry + the wave-1 theme (concept pages are narrative, not the authoritative operator
definition — `orthogonalize.md:38-40`).

## Proposed changes

```edit:book/src/concepts/orthogonalization.md
# concept: orthogonalization

The Arnoldi orthogonalisation step in Krylov-subspace (and ROM basis-extension) methods:
given an orthonormal basis `V[0..m-1]` and a new candidate vector `w`, produce the residual
`w'` (the component of `w` orthogonal to `span(V)`) together with the projection
coefficients `H[0..m-1]` (the leading entries of the Arnoldi/Hessenberg column).

> **Authoritative definition:** the firm operator
> [`L1/orthogonalize`](../L1/orthogonalize.md) is the load-bearing contract; this page is the
> narrative cross-cut. The forward lowering is
> [`L1-L0/orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md).
> Where this page and the L1 entry disagree, the L1 entry wins.

## Contract (coefficients and normalisation)

The operator returns the pair `(w', H)`:

- `w'` — the orthogonal residual, **not normalised**. Palace's header is explicit:
  "Assumes that the input vectors are normalized, but does not normalize the output vectors!"
  (`palace/linalg/orthog.hpp:18-23`). Normalisation is the *caller's* job — `arnoldi_step`
  follows `orthogonalize` with `nrm2(w')` and `scal(1/‖w'‖, w')`.
- `H` — the **length-`m`** projection coefficients, `H[j] = ⟨w_eff(j), V[j]⟩`, with
  `w' = w − Σ_j H[j]·V[j]`. These are the leading `m` entries of the Hessenberg column.

The Hessenberg sub-diagonal `H[m] = ‖w'‖` is **not** produced by this operator — it is the
caller's `nrm2(w')` step. Do not fold it into `H`; that conflates the operator's coefficient
output with the caller's normalisation (the historical drift this page used to carry).

`w_eff(j)` is the candidate as seen by column `j`: for CGS/CGS2 it is the original `w` for
every `j`; for MGS it is the progressively-updated `w` after subtracting columns `0..j-1`.
The inner product follows the [`dot`](../L1/dot.md) conjugate-linear-first-argument
convention.

## Variants

Three implementations occupy the same L1 primitive role; they agree in exact arithmetic and
differ only in finite-precision stability and in collective shape (the load-bearing axis).
At L0 they are three distinct loop-structures — see
[`L1-L0/orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) for
the per-variant loop forms and citations.

- **MGS (Modified Gram–Schmidt)**: single interleaved loop — for `k = 0..m-1`:
  `H[k] = dot(w, V[k]); w ← w − H[k]·V[k]`. More stable than CGS; `m` synchronisations of
  size 1 per step. Carries a [sequential-obstruction](./sequential-obstruction.md) at L3.
- **CGS (Classical Gram–Schmidt)**: split two-phase loop — all `m` `dot`s against the
  *original* `w` (one reduction of size `m`), then all `m` updates. One synchronisation per
  step; loses orthogonality faster than MGS for ill-conditioned bases.
- **CGS2 (CGS with re-orthogonalisation)**: CGS applied twice; the second batched pass
  corrects the first (coefficients accumulate, `H ← H + dH`). Two synchronisations of size
  `m`; recovers MGS-level orthogonality up to roundoff ("twice is enough" — Kahan/Parlett).
  This is Palace's default for parallel scalability with near-MGS stability.

The variant tag is a runtime enum (`Orthogonalization ∈ {MGS, CGS, CGS2}`) bound at solver
setup and **inspected exactly once** at dispatch (`OrthogonalizeIteration`,
`palace/linalg/iterative.cpp:308-325`); downstream code never re-inspects it. Per
[`variant-absorption`](./variant-absorption.md) the three absorb at all three levels under
residual-axis disclosure (the residual being the per-variant collective shape:
m×1 / 1×m / 2×m reductions). Householder is out of scope (no Palace L0 path).

A second variant axis is the **inner-product hook** (`dot_op`): the canonical inner product
vs a `B`-weighted dot used by the SLEPc/ROM paths (`palace/models/romoperator.cpp:51-66`).
This is a substitution of the [`dot`](../L1/dot.md) dependency; the operator's shape and laws
are unchanged (the orthogonality contract becomes `⟨w', V[i]⟩_B = 0`).

## L1 / L2 / L3 placement

- **L1**: the single pure primitive `orthogonalize(w, V, variant) → (w', H)` (firm —
  [`L1/orthogonalize`](../L1/orthogonalize.md)). No destination buffers, no `comm`, no
  in-place mutation; the variant is a parameter.
- **L1>L0**: the mutation rotation
  [`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) — in-place
  `w` overwrite + raw-pointer `H` write + the three per-variant L0 loop-structures.
- **L2 / L3**: the primitive *set* — [`dot`](../L1/dot.md), [`axpy`](../L1/axpy.md), plus the
  caller's `nrm2`/`scal` — is shared across variants; the variant axis affects only the
  *sequence and batching*. The MGS branch carries a sequential-obstruction that surfaces at
  L3 (CGS/CGS2 lift to a clean batched/global form; MGS does not). See
  [`spec/slices/orthog`](../spec/slices/orthog.md) for the retained L2/L3/L4 unfolding.

## Citations

- `palace/linalg/orthog.hpp:18-90` — the `OrthogonalizeColumnMGS / CGS` family (CGS2 is
  `OrthogonalizeColumnCGS(refine=true)`); header scope contract at `:18-23`.
- `palace/linalg/iterative.cpp:308-325` — `OrthogonalizeIteration` runtime variant dispatch.
- `palace/linalg/iterative.cpp:629-632, 808-811` — GMRES / FGMRES Arnoldi call sites, each
  followed by the caller's `nrm2` sub-diagonal + `scal` normalisation.
- `palace/models/romoperator.cpp:51-66` — ROM basis-extension reuse (the second consumer;
  the B-weighted `dot_op` hook).
- `test/unit/test-orthog.cpp:99-160` — empty-basis identity + the `⟨w', V[i]⟩ ≈ 0`
  substitutability witness across MGS/CGS/CGS2.

## Consumers

- [gmres](../spec/slices/gmres.md) — orthogonalising the new Arnoldi vector against the
  existing basis; the variant axis is absorbed at this primitive's contract.
- The ROM basis-extension path (`romoperator.cpp`).
- The L2 [`krylov-step`](../L2/krylov-step.md) composition references `orthogonalization` as
  an all-three-level-absorbed (residual-axis-disclosed) component.
```

## Supporting evidence

- `book/src/concepts/orthogonalization.md:3` — the `(w', h)` with `h = (h_0, …, h_{j+1})`,
  `h_{j+1} = ‖w'‖` framing (drift point 1, normalisation conflation).
- `book/src/concepts/orthogonalization.md:13-19` — first "## L1 contract" + "## L2 / L3
  distinction"; line 19 stale "dedicated `orthog` slice would carry" (drift point 3).
- `book/src/concepts/orthogonalization.md:23` — citation "(separate slice)" (drift point 3).
- `book/src/concepts/orthogonalization.md:26-63` — the entire duplicate second concept block;
  signature at `:52-55` "`w` may be mutated; `h_coeffs` is a length-`j` vector" (drift point
  2, mutation + length contradiction); `:47-48` enum "on the GMRES solver" (drift point 4).
- `book/src/L1/orthogonalize.md:30-33` — authoritative: `H[j+1] = ‖w'‖` is the *caller's*
  `nrm2` step, "This entry returns the length-`m` coefficient vector only."
- `book/src/L1/orthogonalize.md:51, 238` — `w` is read-only; "no in-place overwrite of `w`"
  (refutes "`w` may be mutated").
- `book/src/L1/orthogonalize.md:58-59` — `H` is `Tensor[m]` (length `m`, refuting length-`j`).
- `book/src/L1/orthogonalize.md:247-250, 331-335` — the header "does not normalize" contract
  and the L1 entry's own pre-flag of this exact concept-page drift (the OQ this dispatch
  closes).
- `reports/2026-05-28T0915Z-abstractor-orthogonalize-mutation-rotation-l1-l0-theme/CYCLE.md:85-185,
  209-213` — wave-1 theme: 3 variant loop-structures + "does not normalize output"
  applicability condition; confirms the theme agrees with the L1 entry (concept page is the
  lone outlier).

## Open questions / caveats

- **Layer-intro-author authority.** Concept pages are layer-intro-author territory in the
  write-authority partition; this dispatch is a same-layer-cross-cutter *observation* that
  emits the proposed correction for integrator-per-report to apply. If the integrator prefers
  the strict partition, route the proposed-changes block through a layer-intro-author dispatch
  instead of applying directly — the content is ready either way.
- **Verify the two cross-reference targets exist at integration time.** The rewrite links to
  `../L1-L0/orthogonalize-mutation-rotation.md` and `../L2/krylov-step.md`. The former is the
  cycle-013 wave-1 theme (pending in the same batch — ordering: apply that theme's
  proposed-changes before/with this one, or the link dangles until the theme lands). The
  latter (`L2/krylov-step`) is referenced by the existing L1 entry (`:177`); confirm the path
  (`../L2/krylov-step.md`) resolves — if `krylov-step` lives at a different path, adjust the
  one link. `cargo make book` (integrator-finalize) will surface a broken link if either is
  wrong.
- **`spec/slices/orthog.md` link.** The rewrite links `../spec/slices/orthog.md` (the
  cycle-011 partially-reduced slice). If a later phase-1-corpus-reduction-audit reduces that
  slice to a stub pointing back at the firm entries, this link should survive (the stub
  retains the path); flagging only so a future slice-reduction dispatch keeps the anchor.
- **Scope discipline.** One observation (this concept page vs the firm L1 entry). I did not
  audit `concepts/sequential-obstruction.md` or `concepts/variant-absorption.md` for parallel
  drift — both are referenced by the L1 entry and the rewrite, and a future cross-cutter could
  spot-check them against the firm entry, but that is out of scope here.
