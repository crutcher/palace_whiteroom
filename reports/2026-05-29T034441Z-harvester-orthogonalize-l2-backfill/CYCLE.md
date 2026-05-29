---
agent: harvester
invoked_at: 2026-05-29T034441Z
scope: L2 operator: orthogonalize (corrective backfill of cycle-019 fence-truncation defect)
status: integrated
integrated_at: 2026-05-29T06:05:00Z
integration_commit: 14cc0bd
integration_notes: "cycle-020 finalize (staging row #1, applied FIRST by ordering constraint). CORRECTIVE BACKFILL of the cycle-019 orthogonalize L2 fence-truncation defect — cycle-019 (efb8a0b) landed only the 14-line intro because the firm body was authored OUTSIDE the proposed-changes edit: fence; book/src/L2/orthogonalize.md was a 14-line intro with NO ## Status while L2/index.md:27 + SUMMARY.md:41 already said firm. Full-file replacement recovered the complete firm chapter (## Status firm + Signature + 7 algebraic laws + Variant axes + L2-vs-L1 + Evidence). NOT a firm-count increment (orthogonalize already counted firm cycle-019); L2 firm stays 5. No dep-map/SUMMARY edit (both already firm, correctly not re-touched). TWO skill-candidates filed (proposed-changes-fence-encloses-full-body-guard, verify-intro-firmness-survey-against-on-disk-status-lines) + OQ firm-chapter-body-authored-outside-proposed-changes-fenced-block → batch-5 meta. retroactive-budget 0; clean build."
inputs:
  - reports/2026-05-29T023000Z-harvester-orthogonalize-l2/CYCLE.md (cycle-019 source-of-truth firm body; integrated efb8a0b)
  - book/src/L2/orthogonalize.md (the truncated 15-line intro-only landed by cycle-019; this dispatch full-replaces it)
  - book/src/L2/inner_product.md, book/src/L2/linear_combination.md, book/src/L2/krylov-step.md (canonical firm-L2-entry shape reference)
  - book/src/L1/orthogonalize.md (firm L1 leaf this composition lifts; cycle-012)
  - Re-verified L0 this dispatch (read_range): palace/linalg/orthog.hpp:18-90,
    iterative.cpp:308-325/628-634/807-813, models/romoperator.cpp:51-66/222-227/631-646,
    test/unit/test-orthog.cpp TEST_CASE boundaries :99/:123/:164/:234/:276/:333 + wrapper 71-97 + orthogonality assertion :158
---

# CYCLE: Formalize orthogonalize at L2 (corrective backfill)

## Summary

This is a **corrective backfill**, not new authoring. The cycle-019 harvester
(`reports/2026-05-29T023000Z-harvester-orthogonalize-l2/CYCLE.md`, integrated `efb8a0b`)
produced a fully-vetted firm L2 `orthogonalize` body, but a **fence-truncation defect** in
that report left only the 14-line intro paragraph inside the
`edit:book/src/L2/orthogonalize.md` fenced block (report lines 46–59); the firm body
sections (`## Context` … `## Evidence`, report lines 62–468) were authored as the *report's
own* top-level sections, **outside** the fenced edit block. The integrator therefore landed
only the intro. The result: `book/src/L2/orthogonalize.md` is a 15-line intro with **no
`## Status`, no Signature, no laws, no Evidence** — while the dep-map row
(`L2/index.md`) and `SUMMARY.md:41` already mark it `firm`.

This dispatch **recovers the cycle-019 vetted firm body verbatim** (no re-authoring), assembles
intro + `## Context` … `## Evidence` into one complete firm chapter conforming to the canonical
firm-L2-entry shape (verified against `inner_product.md` / `linear_combination.md` / `krylov-step.md`:
intro → Context → Signature → Semantics → Algebraic laws → Dependencies → Variant axes → Status
(`firm`) → L2-vs-L1 → Evidence; firm L2 entries carry **no YAML frontmatter**, beginning with
`# <slug>`), and emits it as ONE clean `edit:book/src/L2/orthogonalize.md` full-file-replacement
block with the closing fence placed AFTER the entire Evidence section. Every L0 citation was
**re-verified against source this dispatch** (`palace-codemap read_range`); all of the cycle-019
report's pointers verified correct (the repairer's cycle-019 re-verification stands), with **one
off-by-one boundary correction**: the `orthogonalize_wrapper` test class closes at
`test-orthog.cpp:97` (the `};`), not `:96` — corrected `71-96` → `71-97` in the Evidence section.

The dep-map row (`L2/index.md`) and the `SUMMARY.md` entry are ALREADY correct (`firm`,
de-stubbed) from cycle-019 — this dispatch proposes **NO change to them** (no double-edit). The
single proposed change is the `book/src/L2/orthogonalize.md` body. The
`L2-L1/orthogonalize-composition-lowering` forward-reference stays plain-text (the chapter does
not yet exist).

## Proposed changes

```edit:book/src/L2/orthogonalize.md
# orthogonalize

The L2 first-class composition naming the Gram-Schmidt **orthogonalize-against-basis**
pattern: it lifts the firm L1 leaf [`orthogonalize`](../L1/orthogonalize.md) into the named
L2 surface where the `gs_orthog ∈ {MGS, CGS, CGS2}` variant axis is no longer an opaque
parameter but the **visible per-variant batching and sequencing** of the constituent
`dot` / `axpy` primitives. The fusion-rotation form: Palace exposes one runtime-dispatched
entry point (`OrthogonalizeIteration` / the ROM `OrthogonalizeColumn` wrapper) that switches
on the orthogonalization enum into three distinct loop-structures; L2 unfolds that single
dispatch into the canonical composition `(project against V) then (subtract)`, with the
variant's load-bearing difference disclosed as the **collective-shape residual axis** (`m`
reductions of size 1 vs 1 of size `m` vs 2 of size `m`). This is the level-(b)-absorbed
`op.orthog` surface that [`krylov-step`](./krylov-step.md) folds, and the composition
GMRES / FGMRES / Arnoldi / eigenmode-ROM basis-extension all consume.

## Context

At L1, `orthogonalize` is a single pure leaf with the GS variant as a parameter inspected
once; the per-variant collective shape is recorded as a *property* (a variant-axis note and
the column-order-non-commutativity non-law). L2 is the fusion-rotation layer
(`book/src/L2/index.md`): "Batched specialized BLAS calls are written as compositions of
base primitives… kernel fusion across multiple algebraic operations is unfolded into
composition." The orthogonalize family is exactly such a batched specialization — each L0
variant fuses its `dot`s and `w.Add`s into a particular synchronisation pattern, and L2
de-fuses that pattern into the canonical project-and-subtract composition, **keeping the
synchronisation pattern as the disclosed residual axis** because it is load-bearing
(MPI-collective cost shape + finite-precision stability are the entire reason three variants
exist).

This entry is a **named composition**, the structural sibling of the cycle-018 firm
[`linear_combination`](./linear_combination.md) (the BLAS-1 arity-family fold) and of
[`krylov-step`](./krylov-step.md) (the iterative-method step kernel). Per the
`krylov-step` §"L2 vs L1 distinction" forecast — "future L2 entries (likely candidates:
`orthogonalize` as an L2 first-class composition…) will follow the same pattern — name the
composition, list its variant axes, state the laws that hold *at the composition level*, do
not re-derive the laws of the constituent L1 primitives" — this is that entry. It does
**not** replace the L1 leaf; the leaf stays firm and is the form this composition lowers
*into* (the L2>L1 lowering is forthcoming; see § "Dependencies").

The composition is **value-producing and stateless**, not iteration-structural: it folds a
fixed-size basis prefix into one residual-plus-coefficients pair, with no convergence
predicate and no monadic state threading. It therefore belongs with the tensor algebra at
L2, not with L4's `iterate_while`. (The *outer* Arnoldi loop that calls it repeatedly is the
iteration-structural part, and that lives in `krylov-step` + L4's driver, not here.)

A cross-cutting prose treatment lives at
[`concepts/orthogonalization`](../concepts/orthogonalization.md); the MGS sequential-batching
obstruction is at [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md);
the residual-axis-disclosure discipline is
[`concepts/variant-absorption`](../concepts/variant-absorption.md) §"Structurally-distinct
variants" (`variant-absorption.md:131`). Where this entry and the concept pages disagree on
the coefficient/normalisation boundary, the firm L1 entry is authoritative and this entry
follows it.

## Signature

```text
orthogonalize :: (op: OrthogOp, w: Tensor[N], V: Basis[N, m]) -> { residual: Tensor[N], coeffs: Tensor[m] }
```

Shape contract (bunsen-style; named axes):

- `op` — `OrthogOp` — the closed-over orthogonalization surface, bound once at solve setup
  (the level-(b)/(c) absorbed surface `krylov-step` carries as `op.orthog`). A record:
  - `op.variant : GSVariant ∈ {MGS, CGS, CGS2}` — the orthogonalization variant; inspected
    exactly once at dispatch, never re-branched per column.
  - `op.dot : (Tensor[N], Tensor[N]) -> Scalar` — the inner-product hook. The canonical
    [`dot`](../L1/dot.md) (conjugate-linear in the first argument) by default; the SLEPc/ROM
    paths substitute a `B`-weighted dot. This is the `inner-product hook` variant axis,
    carried as a closure field exactly as Palace templates `OrthogonalizeColumn` over
    `InnerProductHelper`.
- `w` — `Tensor[N]` — read-only; the (un-normalised) candidate vector to orthogonalize.
- `V` — `Basis[N, m]` — read-only; `m` columns each of length axis `N`, the **precondition**
  being orthonormal (`⟨V[i], V[j]⟩ = δ_ij`) under `op.dot`. The composition does not enforce
  the precondition; it is the caller's contract (inherited from the L1 leaf, whose L0 header
  states it: `orthog.hpp:18-23`).
- result — `{ residual: Tensor[N], coeffs: Tensor[m] }` — a record with two fields:
  - `residual : Tensor[N]` — the orthogonal residual `w − Σ_j coeffs[j]·V[j]`, **not
    normalised**. Same length axis `N`.
  - `coeffs : Tensor[m]` — the projection coefficients `coeffs[j] = op.dot(w_eff(j), V[j])`,
    the leading `m` entries of the Arnoldi/Hessenberg column. Element type matches `w` / `V`.

The result is **record-shaped** (rather than the L1 leaf's bare tuple) to match the
[`krylov-step`](./krylov-step.md) `op.orthog (V_prefix, w)` call-shape: `krylov-step`'s
auxiliary stage consumes a `{ residual, coeffs }` and rebinds the basis-column field with
`residual` and writes `coeffs` into the Hessenberg column. The record naming is the L2
composition-surface convention; the L1 leaf's `(w', H)` is the same value-pair.

Derived specialization (the L1 leaf recovered):

```text
orthogonalize { variant, dot = ⟨·,·⟩ } w V  ==  let (w', H) = L1.orthogonalize w V variant in { residual = w', coeffs = H }
```

The L2 form differs from the L1 leaf in **resolution along the batching axis**: L1 sees one
opaque parameterised leaf (mirroring Palace's single dispatch wrapper); L2 sees the
composition `project ▷ subtract` whose *internal sequencing* the variant selects. The
element-type / `dot`-hook sub-axes are inherited unchanged from the L1 leaf (not re-derived).

The `m = 0` case (empty basis prefix) is the identity:
`orthogonalize op w [] = { residual = w, coeffs = [] }` for every variant (the L0
early-return at `orthog.hpp:62-64`, witnessed across all three variants at
`test-orthog.cpp:99-120`).

## Semantics

`orthogonalize` removes the `span(V)`-component of `w`, returning the orthogonal residual and
the coefficients of the removed component. In **exact arithmetic with an exactly orthonormal
`V`** all three variants compute the same record: `coeffs[j] = op.dot(w, V[j])` and
`residual = (I − V Vᴴ) w`, the orthogonal projection onto `span(V)`'s complement. The variants
differ only in the **composition's internal sequencing and synchronisation pattern** — and
that is precisely the L2-visible content this entry names. The canonical L2 composition is:

```text
orthogonalize op w V =
  let coeffs = project op.variant op.dot w V        -- the per-variant batched inner products
  let residual = subtract w coeffs V                -- w − Σ_j coeffs[j]·V[j]
  in { residual, coeffs }
```

where `project` / `subtract` are the two composition stages whose **interleaving** is the
variant axis:

- **CGS (classical).** `project` batches all `m` inner products against the *same original*
  `w` (`coeffs[j] = op.dot(w, V[j])` for all `j`, one reduction of size `m`), then `subtract`
  applies all `m` `axpy` updates. The two stages are **separated**: `[dot × m, allreduce_sum,
  axpy × m]`. The `m` inner products are mutually independent; no inter-`j` ordering.
- **MGS (modified).** `project` and `subtract` are **interleaved per column**: for each `j`,
  `coeffs[j] = op.dot(w^(j), V[j])` against the *progressively-subtracted* candidate, then
  immediately `w^(j+1) = w^(j) − coeffs[j]·V[j]`. The composition is the sequential chain
  `[dot, axpy] × m` — `m` reductions of size 1, each gating the next. Equivalently
  `residual = (I − V[m-1] V[m-1]ᴴ) ⋯ (I − V[0] V[0]ᴴ) w`, a left-to-right composition of `m`
  rank-1 projectors. The interleaving is the [`sequential-obstruction`](../concepts/sequential-obstruction.md)
  that blocks MGS's global tensor-field form at L3 (CGS/CGS2 lift cleanly).
- **CGS2 (re-orthogonalised classical).** The CGS composition applied **twice**:
  `[CGS chain] × 2`. A first CGS pass produces a once-orthogonalised `w` and `coeffs`; a second
  CGS pass against that `w` produces a correction `dH`; the returned `coeffs` are the
  accumulated `coeffs + dH` and the residual is the twice-projected `w`. Two reductions of
  size `m`. The second pass reads the once-orthogonalised `w` and is **not** algebraically
  fusible with the first ("twice is enough" — Kahan/Parlett — recovers MGS-level
  orthogonality precisely because `V` is only approximately orthonormal in practice). CGS2 is
  Palace's default for parallel scalability with near-MGS stability.

The variant tag is inspected **exactly once** (the dispatch in `OrthogonalizeIteration`,
`iterative.cpp:308-325`, or the ROM `OrthogonalizeColumn` wrapper, `romoperator.cpp:51-66`);
the composition body's textual shape does not branch on the variant per column. The
**collective-shape residual axis** — the *number and size* of reductions (`m×1` / `1×m` /
`2×m`) — is the load-bearing distinction and is disclosed here as a first-class property of
the composition (per `variant-absorption.md:131`, the MGS/CGS/CGS2 family absorbs at all
three levels under residual-axis disclosure for the L2 collective shape). The MPI collective
itself is not in the L2 signature (single-rank scope per `CLAUDE.md`); the residual axis is
the *shape* of the collective, which materialises as actual `MPI_Allreduce` calls only in the
L2>L1>L0 lowering.

**Normalisation is not part of this composition.** The L0 header is explicit: the routine
"assumes that the input vectors are normalized, but does not normalize the output vectors!"
(`orthog.hpp:22`). Every consumer follows the call with its own `Norml2` (the Hessenberg
sub-diagonal `H[m] = ‖residual‖`) and `scal (1/‖residual‖)` normalisation — visible at the
GMRES site `iterative.cpp:630-632`, the FGMRES site `iterative.cpp:809-811`, and the ROM
basis-extension sites `romoperator.cpp:224-226` and `:644-645`. `nrm2` / `scal` are
therefore **not** dependencies of this composition; the `{ residual, coeffs }` record stops at
the un-normalised residual and the length-`m` coefficient vector. This boundary is inherited
verbatim from the firm L1 leaf and is authoritative over the
[`concepts/orthogonalization`](../concepts/orthogonalization.md) narrative.

## Algebraic laws

`orthogonalize` is a **named composition** (a `project ▷ subtract` pipeline parameterised by
the variant), not a binary algebra. The laws below are stated at the **composition level** —
they are facts about the residual/coeffs pair the composition produces — and the constituent
L1 leaf's own laws (the `dot` conjugate-linear-first-argument convention, `axpy` bilinearity)
are inherited, not re-derived. "Exact" means exact arithmetic with an exactly orthonormal
input basis; floating-point caveats are recorded as explicit non-laws.

1. **Orthogonality (the defining contract).** `op.dot(residual, V[i]) = 0` for all
   `i ∈ [0, m)` (exact). This is the contract shared by **all three variants** — it is what
   makes them substitutable as the same composition. Witnessed empirically across MGS / CGS /
   CGS2 at `test-orthog.cpp:154-159` (the per-rank orthogonality-check loop; the
   `⟨residual, V[i]⟩ ≈ 0` assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` is at line 158),
   under both the canonical and the `B`-weighted `op.dot`.

2. **Loss-free decomposition.** In exact arithmetic with orthonormal `V`,
   `w = residual + Σ_j coeffs[j]·V[j]` — the composition is a complete (loss-free)
   decomposition of `w` into its `span(V)` and `span(V)^⊥` parts. (The composition-level
   restatement of L1 leaf law 2.)

3. **Empty-prefix identity.** `orthogonalize op w [] = { residual = w, coeffs = [] }` for any
   `w` and any variant (the `m = 0` path, `orthog.hpp:62-64`; `test-orthog.cpp:99-120`).

4. **Variant agreement (exact).** MGS, CGS, and CGS2 produce the *same* `{ residual, coeffs }`
   in exact arithmetic with exactly orthonormal `V`. At the exact-arithmetic level the three
   compositions are one composition; they diverge only in finite precision and in collective
   shape. **This is the substitutability law** that lets `krylov-step` carry the variant as a
   level-(b)-absorbed closure without per-column branching.

5. **Idempotence on the residual (exact).** `orthogonalize op residual V` returns
   `{ residual, coeffs = 0 }` — re-running the composition on an already-orthogonal residual
   is a no-op on the field and yields zero coefficients (exact). This is the projector
   identity `(I − V Vᴴ)² = (I − V Vᴴ)` for orthonormal `V`. In finite precision the second
   run yields a small non-zero correction — *which is exactly the mechanism CGS2 exploits*:
   **CGS2 is one explicit re-application of this law to recover lost orthogonality** (the
   `[CGS chain] × 2` shape is law 5 instantiated as a composition step, not an external
   identity).

6. **Linearity in the candidate (exact).** `orthogonalize op (α·w₁ + w₂) V` has residual
   `α·residual₁ + residual₂` and coeffs `α·coeffs₁ + coeffs₂` (the projection `I − V Vᴴ` and
   the coefficient map `Vᴴ` are both linear). Conjugate-linearity in the complex case follows
   the inherited `op.dot` first-argument convention.

7. **`dot`-hook invariance of shape and laws.** Substituting `op.dot` (canonical → `B`-weighted)
   leaves the composition's shape and laws 1–6 unchanged; only the inner-product realisation
   differs and the orthogonality contract reads `⟨residual, V[i]⟩_B = 0`. The hook is a closure
   substitution, not a structural variant (`romoperator.cpp:631-646` threads the weighted hook
   through the identical composition; `test-orthog.cpp:276, 333` are the weighted witnesses).

Laws that explicitly **do NOT** hold:

- **Variant agreement in floating point.** Law 4 fails in finite precision: the three
  compositions produce different `{ residual, coeffs }` at the bit level (and at larger
  amplitudes when `V` is ill-conditioned). This **is** the residual axis — recorded, not
  erased. MGS and CGS2 hold orthogonality to roundoff; CGS loses it faster for
  ill-conditioned bases. (Load-bearing numerical distinction per CLAUDE.md §Optimization
  tricks.)
- **Column-order commutativity under MGS.** Permuting the columns of `V` changes the
  intermediate `w^(j)` and hence the MGS `{ residual, coeffs }` at the bit level (CGS/CGS2 are
  column-order-invariant up to reduction-tree noise; MGS is not, because the left-to-right
  rank-1-projector composition does not commute). This is the algebraic shadow of the MGS
  sequential interleaving (Semantics, MGS bullet) — the same dependency that becomes the L3
  obstruction.
- **Reduction-tree associativity (floating point).** Inherited from [`dot`](../L1/dot.md):
  different summation orders inside `project` give different bit-level coefficients.
  Load-bearing; pinned per lowered call by the forthcoming L2>L1 theme.
- **Stage-fusion across the project/subtract boundary (CGS2).** The second CGS pass is not
  fusible with the first — fusing them would compute the correction `dH` against the
  *un*-orthogonalised `w` and destroy the re-orthogonalisation property. The `[CGS] × 2`
  composition is genuinely two passes (law 5 non-fusibility), unlike the transparent
  intra-pass fusion of `dot`/`axpy`.
- **Identity / linearity at the bit level.** Laws 5 and 6 are exact-arithmetic identities; in
  floating point they hold only up to the orthogonality floor of the chosen variant.

## Dependencies

L2 dependencies (other L2 vocabulary or below):

- L1 leaf it lifts: [`orthogonalize`](../L1/orthogonalize.md) (firm, cycle-012) — the
  parameterised primitive whose opaque variant this composition makes visible. This entry is
  the form the leaf is *named as* at L2; it does not replace the leaf.
- L1 primitives the composition stages compose: [`dot`](../L1/dot.md) (the `project` stage's
  inner product `coeffs[j] = op.dot(w_eff(j), V[j])`; the `op.dot` hook is a `dot`
  substitution), [`axpy`](../L1/axpy.md) (the `subtract` stage's rank-1 update
  `w ← w − coeffs[j]·V[j]` = `axpy(-coeffs[j], V[j], w)`). These are firm post-cycle-002.
- Sibling reduction (do **NOT** merge): the `project` stage's batched inner products are a
  use-site of the candidate L2 [`inner_product`](./inner_product.md) fold (rough-in) — but
  `orthogonalize` is the *project-and-subtract composition*, not the inner-product fold
  itself; the fold is a constituent, not a parent.

Concept references (cross-cutting; do not duplicate):

- [`orthogonalization`](../concepts/orthogonalization.md) — the narrative cross-cut (variants,
  the coefficient/normalisation boundary).
- [`variant-absorption`](../concepts/variant-absorption.md) — the residual-axis-disclosure
  discipline (`:131`) underwriting the collective-shape residual axis.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the MGS interleaving
  obstruction that surfaces at L3.

Consumers (the L2/L4 surfaces that fold or call this composition):

- [`krylov-step`](./krylov-step.md) — absorbs `orthogonalize` at level-(b) as the optional
  `op.orthog (V_prefix, w)` auxiliary stage (GMRES / Arnoldi). The `{ residual, coeffs }`
  record is the auxiliary stage's output; the basis-column field is rebound with `residual`
  and `coeffs` is written into the Hessenberg column.
- The ROM basis-extension path (`romoperator.cpp:224, 633-645`), the second consumer with the
  `B`-weighted `op.dot` hook (confirms the composition is not GMRES-specific).

L2>L1 lowering theme (forthcoming; abstractor work, **not** authored here): an
`L2-L1/orthogonalize-composition-lowering` theme will narrate how the named L2 composition
lowers into the firm L1 leaf — variant-dispatch on `op.variant`, and which L0 summation /
reduction order each lowered variant pins (the load-bearing content of the reduction-tree and
variant-agreement non-laws). Forward-reference only — that chapter does not yet exist.

## Variant axes

Following the [`classify-variant-axis`](../../../skills/classify-variant-axis/SKILL.md)
output contract (per-axis-value: absorption path, load-bearing primitive, state binding):

- `gs_orthog` ∈ {`MGS`, `CGS`, `CGS2`}: **residual-axis disclosure** (levels (a)/(b) hold —
  the orthogonality contract unifies, the variant is inspected once at dispatch; level (c)
  is the disclosed residual — the primitive *sequence* genuinely differs). This is the axis
  this composition makes visible at L2.
  - `MGS`: sequential `[dot, axpy] × m` — load-bearing primitive: per-column `dot` + `axpy`
    interleaved with sync-per-column (`m` reductions of size 1). Carries the
    [`sequential-obstruction`](../concepts/sequential-obstruction.md) at L3.
  - `CGS`: batched `[dot × m, allreduce_sum, axpy × m]` — load-bearing primitive: the batched
    `dot` block against the original `w` (one reduction of size `m`); `project` and `subtract`
    stages fully separated.
  - `CGS2`: `[CGS chain] × 2` — load-bearing primitive: the re-orthogonalisation re-entry
    accumulating `coeffs ← coeffs + dH` (two reductions of size `m`); the second pass is
    non-fusible (algebraic-laws non-law).
  - State binding: all three share the basis prefix `V[0..m-1]` and the candidate `w`;
    `op.variant` is bound once at solve setup and captured in `op`. (CGS2's `dH` scratch is
    pass-local, not threaded state.) **Householder is scoped out**: it threads a *reflector
    sequence* (fundamentally different state) with an L_{n+1} chain of `[reflect_apply,
    reflect_zero]` instead of `[dot, axpy]`, breaking level-(c) absorption
    (`variant-absorption.md:131`); Palace's L0 has no Householder path (`orthog.hpp` defines
    exactly `OrthogonalizeColumnMGS` / `OrthogonalizeColumnCGS`), so it is out of scope per the
    unimplemented-component policy.

- `dot` hook ∈ {`canonical ⟨·,·⟩`, `B-weighted`}: **parametric absorption** (a closure
  substitution; the composition shape and laws are invariant — algebraic-laws law 7).
  - `canonical`: `op.dot = ` [`dot`](../L1/dot.md) (conjugate-linear first argument); the
    GMRES / FGMRES Arnoldi default (`iterative.cpp:630, 809`, no `dot_op` passed →
    `IdentityInnerProduct`).
  - `B-weighted`: `op.dot = λ x y. W.InnerProduct(x, y, r)`; the SLEPc/ROM basis-extension
    substitution (`romoperator.cpp:631-646`). The orthogonality contract reads
    `⟨residual, V[i]⟩_B = 0`.
  - State binding: the canonical hook captures nothing; the weighted hook captures the weight
    operator `W` and the work vector `r` in the closure (`romoperator.cpp:635-636`).

The **element-type** axis (`real | complex`) is fully parametric and absorbed by the `op.dot`
dependency (the conjugation lives in `dot`, exactly as for the L1 leaf); it does not produce
distinct compositions at L2. All parametric tests cover both element types
(`test-orthog.cpp:123, 234` real/complex; `:276, 333` weighted real/complex).

## Status

`firm` — the composition is a `project ▷ subtract` pipeline over two firm L1 primitives
(`dot`, `axpy`) lifting the firm L1 leaf `orthogonalize`; the signature is the named-composition
surface that [`krylov-step`](./krylov-step.md) already absorbs at level-(b); every algebraic
law is either a composition-level restatement of an inherited L1 fact (orthogonality,
loss-free decomposition, empty-prefix identity, linearity) or a standard Gram-Schmidt
composition fact (variant agreement, idempotence-as-CGS2-mechanism) modulo the
explicitly-recorded floating-point caveats; the variant axes are closed at two (`gs_orthog`
residual-axis + `dot` hook parametric), matching the L1 leaf and `variant-absorption.md:131`.
The L0 implementation is read in full (`orthog.hpp:18-90`), both dispatch wrappers are read in
full (`iterative.cpp:308-325`, `romoperator.cpp:51-66`), all four consumer call sites are
verified (`iterative.cpp:630, 809`; `romoperator.cpp:224, 633`), and all three variants carry
dedicated parametric test coverage across real / complex / B-weighted element types plus the
empty-prefix edge case and the direct substitutability assertion
(`test-orthog.cpp:99-160, 234, 276, 333`). This matches the firmness bar of the cycle-018
`linear_combination` L2 composition (a named composition over firm L1 leaves) and the
cycle-005 `krylov-step` L2 composition.

## L2 vs L1 distinction

- **L1**: the single pure leaf `orthogonalize(w, V, variant) → (w', H)`, mirroring Palace's
  single dispatch wrapper one-to-one; the GS variant is an opaque parameter inspected once and
  the per-variant collective shape is recorded as a *property* (a variant-axis note). The leaf
  is the floor primitive.
- **L2**: the *named composition* `orthogonalize { variant, dot } w V → { residual, coeffs }`
  — the `project ▷ subtract` pipeline whose **internal sequencing and synchronisation pattern
  is the variant axis made visible**. L2's role is not to add a new primitive but to name the
  canonical composition and surface its composition-level laws: the batched-vs-interleaved
  primitive sequences (MGS `[dot,axpy]×m` / CGS `[dot×m, allreduce, axpy×m]` / CGS2 `[CGS]×2`)
  and the collective-shape residual axis become first-class L2 content, where at L1 they were
  a parameter and a note. This is the surface `krylov-step` folds at level-(b).

## Evidence

- `palace/linalg/orthog.hpp:18-23` — header scope contract: orthogonalises against a set of
  basis vectors using modified or classical Gram-Schmidt; "Assumes that the input vectors are
  normalized, but does not normalize the output vectors!" — the load-bearing
  no-output-normalisation contract (the `{ residual, coeffs }` record stops at the
  un-normalised residual). **Self-verified via `read_range` this dispatch.**
- `palace/linalg/orthog.hpp:25-37` — `IdentityInnerProduct` and the `InnerProductHelper`
  concept (`InnerProduct(VecType, VecType) -> ScalarType`, "Also add MPI reduction"): the
  `op.dot` template hook (the inner-product variant axis). **Self-verified.**
- `palace/linalg/orthog.hpp:38-53` — `OrthogonalizeColumnMGS`: the per-`j` loop
  `H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm); w.Add(-H[j], V[j])`. The
  interleaving of `dot` and `w.Add` in the same `j`-loop body is the source witness of the MGS
  sequential composition (`[dot, axpy] × m`, `m` reductions of size 1). **Self-verified.**
- `palace/linalg/orthog.hpp:55-89` — `OrthogonalizeColumnCGS`: empty-basis early return
  (`m == 0`, `:62-64`); `m` batched local dots into `H[0..m-1]`; single
  `Mpi::GlobalSum(m, H, comm)`; `m` batched `w.Add`s against the original `w`; the `refine`
  branch re-enters with `dH`, accumulating `H[j] += dH[j]` (the CGS2 `[CGS] × 2` second pass).
  One (CGS) or two (CGS2) reductions of size `m`. **Self-verified.**
- `palace/linalg/iterative.cpp:308-325` — `OrthogonalizeIteration`: the runtime variant
  dispatch (`switch (type)` over `MGS / CGS / CGS2`, `CGS2 = OrthogonalizeColumnCGS(..., true)`);
  confirms the variant is bound at solver construction and dispatched once, against the
  leading `j + 1` columns. **Self-verified.**
- `palace/linalg/iterative.cpp:630-632` — GMRES Arnoldi consumer:
  `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j)` immediately followed by
  `Hj[j + 1] = linalg::Norml2(comm, w)` (the caller's sub-diagonal) and `w *= 1.0 / Hj[j + 1]`
  (the caller's normalisation) — confirming normalisation is the caller's, outside the
  composition. **Self-verified.**
- `palace/linalg/iterative.cpp:809-811` — FGMRES Arnoldi consumer: the identical
  `OrthogonalizeIteration` call + `Norml2` + `scal` sequence (with `Z[j]` flexible-preconditioner
  basis). **Self-verified.**
- `palace/models/romoperator.cpp:51-66` — the ROM `OrthogonalizeColumn` wrapper: the second
  dispatch surface, switching on `Orthogonalization` and forwarding `dot_op` to the
  `OrthogonalizeColumn{MGS,CGS}` family (CGS2 = `refine=true`); takes the `dot_op` hook
  explicitly. **Self-verified.**
- `palace/models/romoperator.cpp:224-226` — ROM basis-extension consumer (canonical hook):
  `OrthogonalizeColumn(orthog_type, comm, Q, Q[dim_Q], R.col(dim_Q).data(), dim_Q)` followed by
  `Norml2` + `*= 1.0 / norm` — the same compose-then-normalise structure as GMRES.
  **Self-verified.**
- `palace/models/romoperator.cpp:631-646` — ROM basis-extension consumer (B-weighted hook):
  `OrthogonalizeColumn(..., [&W, &r](const Vector &x, const Vector &y){ return
  W.InnerProduct(x, y, r.Real()); })` — the `op.dot` B-weighted substitution (the
  inner-product-hook variant axis), the second consumer confirming the composition is not
  GMRES-specific. **Self-verified.**
- `test/unit/test-orthog.cpp:71-97` — `orthogonalize_wrapper` GENERATE harness running all
  three variants through one code path (the substitutability fixture; the wrapper class spans
  the comment at 71 through the closing `};` at 97). **Self-verified.**
- `test/unit/test-orthog.cpp:99-120` — empty-prefix edge case ("OrthogonalizeColumn - Real
  Empty"): all three variants leave `w` unchanged (`m = 0` identity, law 3). **Self-verified.**
- `test/unit/test-orthog.cpp:123-160` — parametric real test ("OrthogonalizeColumn
  Parameterized - Real 1"): all three variants zero the per-rank component and pass
  `⟨residual, V[i]⟩ ≈ 0` to `1e-12` (law 1, the substitutability witness); the orthogonality
  assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` is at line 158, inside the check loop
  154-159; TEST_CASE closes at 160. **Self-verified.**
- `test/unit/test-orthog.cpp:164, 234, 276, 333` — real-2 (`:164`), complex-1 (`:234`),
  weighted-real-1 (`:276`), weighted-complex-1 (`:333`) parametrisations: the element-type axis
  and the B-weighted `op.dot` variant axis. **Self-verified (TEST_CASE boundary lines).**
- `book/src/L1/orthogonalize.md` — the firm L1 leaf this composition lifts; the
  coefficient/normalisation boundary and the variant-axis contract are inherited from it.
- `book/src/L2/linear_combination.md` (cycle-018) — the structural precedent for a firm L2
  named-composition entry over firm L1 leaves.
- `book/src/L2/krylov-step.md` — the consumer that absorbs this composition at level-(b)
  (`op.orthog`); §"L2 vs L1 distinction" forecasts this exact entry.
- `book/src/concepts/variant-absorption.md:131` — the residual-axis-disclosure ground for the
  collective-shape axis and the Householder scope-out.
```

## Citation self-verification log

Every L0 citation in the recovered body was re-verified against source this dispatch via
`palace-codemap read_range` / `search_text`. All cycle-019 pointers verified **correct** (the
cycle-019 repairer's independent re-verification stands); one off-by-one boundary corrected.

| Citation | Re-verification (read this dispatch) | Verdict |
|---|---|---|
| `orthog.hpp:18-23` header scope contract; `:22` "Assumes…normalized…does not normalize" | read 18-90: line 22 = `// Assumes that the input vectors are normalized, but does not normalize the output vectors!` | CORRECT |
| `orthog.hpp:25-37` `IdentityInnerProduct` + `InnerProductHelper` concept | line 25 `// Concept: InnerProductHelper…`, struct `IdentityInnerProduct` 29–37 (`};` at 37) | CORRECT |
| `orthog.hpp:38-53` `OrthogonalizeColumnMGS`, per-`j` `dot`/`GlobalSum(1,…)`/`w.Add` | MGS template 39–53; loop body `H[j]=dot_op(...)`/`Mpi::GlobalSum(1,&H[j],comm)`/`w.Add(-H[j],V[j])` present | CORRECT |
| `orthog.hpp:55-89` `OrthogonalizeColumnCGS`; `m==0` guard `:62-64`; `GlobalSum(m,…)`; `refine`/`dH`/`H[j]+=dH[j]` | CGS template 55–89; `if (m == 0)` at 62, `return;` at 64; batched `GlobalSum(m, H, comm)`; refine block accumulates `H[j] += dH[j]` | CORRECT |
| `iterative.cpp:308-325` `OrthogonalizeIteration` switch MGS/CGS/CGS2, CGS2=`...,true`, leading `j+1` | read 308-325: `switch (type)`, `CGS2: OrthogonalizeColumnCGS(comm, V, w, Hj, j + 1, true)` | CORRECT |
| `iterative.cpp:630-632` GMRES: `OrthogonalizeIteration(...)` → `Hj[j+1]=Norml2(...)` → `w *= 1.0/Hj[j+1]` | read 628-634: line 630 call, 631 `Norml2`, 632 `w *= 1.0 / Hj[j + 1]` | CORRECT |
| `iterative.cpp:809-811` FGMRES: identical call+`Norml2`+`scal` | read 807-813: lines 809/810/811 identical sequence | CORRECT |
| `romoperator.cpp:51-66` `OrthogonalizeColumn` wrapper, switch + `dot_op` forward, CGS2=`refine=true` | read 51-66: `switch (type)` forwarding `dot_op`, `CGS2: OrthogonalizeColumnCGS(..., true, dot_op)` | CORRECT |
| `romoperator.cpp:224-226` canonical-hook consumer: call → `Norml2` → `*= 1.0/norm` | read 222-227: line 224 `OrthogonalizeColumn(orthog_type, comm, Q, Q[dim_Q], R.col(dim_Q).data(), dim_Q)`, 225 `Norml2`, 226 `*= 1.0 / R(dim_Q,dim_Q)` | CORRECT |
| `romoperator.cpp:631-646` B-weighted hook; closure capture `:635-636` | read 631-646: `OrthogonalizeColumn(..., [&W = *(this->weight_op_W), &r = this->r](const Vector &x, const Vector &y){ return W.InnerProduct(x, y, r.Real()); })`; capture line at 635, `W.InnerProduct` at 636 | CORRECT |
| `test-orthog.cpp:71-96` wrapper class "comment 71 through `};` at 96" | read 71-97: comment at 71, class `orthogonalize_wrapper` 72–97, **`};` at line 97** (line 96 = `}` closing `operator()`) | **CORRECTED → `71-97`** |
| `test-orthog.cpp:99-120` empty-prefix "Real Empty"; `m=0` identity | `TEST_CASE("OrthogonalizeColumn - Real Empty"...)` at 99 (search_text confirmed); `CHECK_THAT(w, RangeEquals(w_orig))` at 120 | CORRECT |
| `test-orthog.cpp:123-160` parametric "Real 1"; assertion `:158`; loop 154-159; close 160 | `TEST_CASE(...Real 1)` at 123; counted: `CHECK_THAT(dot, WithinAbs(0.0,1e-12))` at 158, TEST_CASE close at 160 | CORRECT |
| `test-orthog.cpp:154-159` per-rank orthogonality-check loop (iterates over MPI ranks) | comment at 154, `for` 155, `auto dot=...` 157, assertion 158, `}` 159 | CORRECT |
| `test-orthog.cpp:164, 234, 276, 333` TEST_CASE boundaries (real-2 / complex-1 / weighted-real-1 / weighted-complex-1) | `search_text ^TEST_CASE` → 164 "Real 2", 234 "Complex 1", 276 "Weighted - Real 1", 333 "Weighted - Complex 1" | CORRECT (all four exact) |

Single correction applied to the recovered body: the `orthogonalize_wrapper` Evidence line
`71-96` → `71-97` (the class `};` is at line 97; line 96 is the `}` closing `operator()`). All
other citations land on the asserted construct. No other drift found.

## Open questions / caveats

- **Provenance: this is a corrective backfill of the cycle-019 fence-truncation defect.** In
  `reports/2026-05-29T023000Z-harvester-orthogonalize-l2/CYCLE.md` (integrated `efb8a0b`), the
  firm chapter body (`## Context` … `## Evidence`, report lines 62–468) was authored as the
  report's own top-level sections — only the intro paragraph (report lines 46–59) sat INSIDE
  the `edit:book/src/L2/orthogonalize.md` fenced block. The integrator landed only the intro,
  leaving `book/src/L2/orthogonalize.md` as a 15-line intro-only chapter with no `## Status` /
  Signature / laws / Evidence, while the dep-map row and `SUMMARY.md:41` already marked it
  `firm`. This dispatch full-replaces that stub with the complete recovered firm body,
  correctly fenced (closing ``` AFTER the Evidence section). **Recommend the meta-phase log a
  friction-ledger entry** for the recurring "firm chapter body authored outside the
  proposed-changes fenced block" pattern (a producer-side fencing-discipline defect distinct
  from the citation-drift family) and that the critic's `cross-reference-integrity` /
  build-readiness checks add a guard: when a dep-map row / SUMMARY entry says `firm` but the
  target chapter has no `## Status` section, flag it. The cycle-019 critic+repairer cycle
  validated the *content* (citations correct) but did not catch that most of the content never
  entered the artifact, because the report's prose carried it.

- **No dep-map / SUMMARY change proposed (deliberate, to avoid a double-edit).** The
  `L2/index.md` `orthogonalize` dep-map row and the `SUMMARY.md:41` de-stubbed entry
  (`- [orthogonalize](./L2/orthogonalize.md)`) were both applied correctly by cycle-019 and
  already say `firm`. This dispatch's single proposed change is the chapter body. If the
  integrator finds either the dep-map row or the SUMMARY entry is somehow ALSO missing/wrong
  (it should not be — verify against `efb8a0b`), that is a separate defect to file, not to
  fold into this backfill.

- **Inherited open questions (carried from cycle-019, still open; not re-opened here).** The
  cycle-019 report's four caveats remain live and are NOT resolved by this backfill: (1) the
  `L2-L1/orthogonalize-composition-lowering` theme is still unwritten (abstractor territory;
  plain-text forward-reference retained in the chapter); (2) the `{ residual, coeffs }`
  record-naming-vs-L1-`(w', H)`-tuple convention flag stands; (3) the `inner_product`
  sibling-fold tightening (cite `inner_product` for the `project` stage once it firms) stands;
  (4) the L2 layer-intro Working-Notes refresh (OQ `L2-layer-intro-refresh-for-named-compositions`,
  layer-intro-author territory) stands. These were correctly logged at cycle-019 integration;
  this dispatch does not re-append them to the OQ ledger (no duplication).

- **`romoperator.cpp:644-645` / `:633-645` consumer-norm citations carried from the report,
  not independently line-verified this dispatch.** The Semantics/Dependencies prose cites the
  ROM second-consumer normalisation at `romoperator.cpp:224-226` (verified) and `:644-645`
  (the `else`-branch `Norml2` after the canonical `OrthogonalizeColumn`, visible in the
  631-646 read as `orth_R(dim_V, dim_V) = linalg::Norml2(...)` at the tail of that range) — the
  range I read (631-646) covers it. The `:633` call-site referenced in Dependencies/Consumers
  ("ROM basis-extension path `romoperator.cpp:224, 633-645`") is the B-weighted-branch
  `OrthogonalizeColumn(...)` call inside the 631-646 block I read; it lands within the verified
  range. No drift; flagged only for completeness since the report's prose split these into
  several sub-references.
