---
agent: same-layer-cross-cutter
invoked_at: 2026-05-29T051532Z
scope: L1 cross-cut — orthog.hpp LocalDot+GlobalSum unweighted inner-product surface (the dot-census-bypass second surface)
status: integrated
integrated_at: 2026-05-29T06:14:03Z
integration_commit: 881f200
integration_notes: "cycle-021 finalize (staging row #7). APPLIED DIRECTLY (well-formed additive edits to firm themes; deferring fully-cited additive edits is friction). Proposal 1: added Sub-pattern D (unfused hook-routed LocalDot+Mpi::GlobalSum dot surface; first unweighted-observable dot use outside the SLEPc-NEP deflation cohort; IdentityInnerProduct+CGS sketch, Observability note, 5 verified citations) to book/src/L1-L0/dot-mutation-rotation.md §L0-form-RHS. Proposal 2: added a bypass-surface paragraph to book/src/L2-L1/inner-product-fold-specialization.md (cross-links Sub-pattern D; no new yaml keys). Both additive; themes STAY firm, no status change, no new files, no SUMMARY touch. CLOSES the cycle-020 dot-callers census coverage gap (OQ orthog-hpp-localdot-globalsum-unfused-dot-surface RESOLVED — recorded as append-only ...-RESOLVED for meta-phase Closed-index migration). retroactive-budget 0; clean build."
---

# CYCLE: L1 observation — the `orthog.hpp` Gram-Schmidt `LocalDot`+`GlobalSum` inner-product surface

## Summary

The cycle-020 `linalg::Dot`-caller census (`reports/2026-05-29T034441Z-cross-layer-cross-cutter-dot-callers/CYCLE.md`)
censused every `linalg::Dot` call site and flagged — but did NOT classify — a second
unweighted inner-product surface: the Gram-Schmidt routines in `palace/linalg/orthog.hpp`
compute their projection coefficients via the **`InnerProductHelper` hook** (`dot_op`),
whose canonical realization `IdentityInnerProduct` calls **`LocalDot(x, y)` directly**
(`orthog.hpp:34`), and the routine itself then applies **`Mpi::GlobalSum`** over the
coefficient buffer (`orthog.hpp:50` for MGS, `:70,:82` for CGS/CGS2). I read `orthog.hpp`
in full, plus the `LocalDot` kernels (`vector.cpp:665-685`), the `linalg::Dot` template
(`vector.hpp:247-253`), and `Mpi::GlobalSum` (`communication.hpp:266-270`). **Finding: this
is the *unfused* form of `linalg::Dot`'s `GlobalSum ∘ LocalDot` composition, computing the
identical `yᴴ x` (arg-2-conjugated) inner product, but split across the helper-hook boundary
so the GlobalSum is batched (`m`-at-once in CGS) rather than per-dot.** It is therefore
**(a) an additional call-surface / variant-axis realization of the existing `dot` operator**,
not a distinct primitive — but it carries a **distinguishing property the four `nleps.cpp`
observable sites do not**: the Gram-Schmidt coefficients `H[j]` are *unweighted observable*
**and consumed in non-deflation linear algebra** (the residual update `w.Add(-H[j], V[j])`),
making them the first cited unweighted-observable `dot` uses *outside* the SLEPc-NEP
deflation cohort.

## Observation kind

**Shared sub-pattern / redundancy (benign-but-uncited)** — the `orthog.hpp`
`LocalDot`+`GlobalSum` path and `linalg::Dot` are the **same** unweighted Hermitian
inner product (`yᴴ x`) reached by two different call shapes: `linalg::Dot` is the *fused*
`GlobalSum(LocalDot(x,y))` (`vector.hpp:247-253`); `orthog.hpp` open-codes the *unfused*
two-step (`dot_op = LocalDot` at `:34`, then a separate batched `Mpi::GlobalSum`). The
operator-level coverage already exists (the firm `L1/orthogonalize` entry names the `dot_op`
hook as its inner-product dependency; `L1-L0/dot-mutation-rotation` Sub-pattern A names the
`GlobalSum ∘ LocalDot` two-step). What is **uncited** is (i) that `orthog.hpp` is a *second
realization* of that two-step — the **unfused** one, with a **batched** collective — which
the `dot-mutation-rotation` surface-forms inventory does not enumerate, and (ii) that the
Gram-Schmidt `H[j]` coefficients are an **unweighted observable** consumption of the
arg-2-conj convention, distinct in algorithm from the `nleps.cpp` deflation cohort the
cycle-020 census found. Classification: **(a)** with a small additive citation gap; **not (b)**
(no new primitive); **not fully (c)** (the *surface form* and the *observable witness* are
uncited even though the operator relationship is covered).

## Specific finding

### What inner product `orthog.hpp:34` computes

`IdentityInnerProduct::operator()(x, y)` returns `LocalDot(x, y)` (`orthog.hpp:29-36`,
the `return` at `:34`). `LocalDot` is documented `// Calculate the local inner product
yᴴ x or yᵀ x` (`vector.hpp:242`) and its complex body
(`vector.cpp:674-685`) computes `Re = LocalDot(xr,yr)+LocalDot(xi,yi)`,
`Im = LocalDot(xi,yr)−LocalDot(xr,yi)` = `x·conj(y) = yᴴ x` — **arg-2 conjugated**, the
same convention `L1/dot.md`, `L2-L1/inner-product-fold-specialization.md`, and
`L1-L0/dot-mutation-rotation.md` all pin against the L1/L2 `xᴴ y` representation
(`xᴴ y = conj(yᴴ x)`). It is **unweighted** (no `M` operator; the weighted member is the
separate `dot_op` substitution — the B-weighted SLEPc/ROM hook noted at
`L1/orthogonalize.md:204-211`, NOT `IdentityInnerProduct`).

### How it relates to the `dot` leaf / `inner_product` fold

It IS the `dot` leaf — specifically the **complex/real Hermitian unweighted member** —
reached through the `InnerProductHelper` template hook instead of a direct `linalg::Dot`
call. The relationship to `linalg::Dot` is **fuse/unfuse**:

```text
linalg::Dot(comm, x, y)        =  Mpi::GlobalSum(1, LocalDot(x, y))     -- FUSED, per-dot collective   (vector.hpp:247-253)
orthog.hpp MGS  per j          =  Mpi::GlobalSum(1, &(LocalDot(w, V[j]))) ; w.Add(-H[j], V[j])          (orthog.hpp:49-51)
orthog.hpp CGS  (all j)        =  H[j] = LocalDot(w, V[j]) ;  Mpi::GlobalSum(m, H, comm)  -- BATCHED collective (orthog.hpp:68-70)
```

The MGS path (`orthog.hpp:46-52`) is `linalg::Dot(comm, w, V[j])` literally re-spelled
(local dot then a size-1 GlobalSum) — value-identical, just inlined so the `w.Add` can be
interleaved into the same `j`-loop (the MGS sequential dependency). The CGS path
(`orthog.hpp:66-88`) is the **fusion-relevant** difference: it does all `m` local dots
first, then ONE `Mpi::GlobalSum(m, H, comm)` (`:70`) — i.e. it **batches the collective**
across the `m` coefficients rather than doing `m` separate `linalg::Dot` calls. This batched
collective is exactly the "1 reduction of size `m`" vs MGS's "`m` reductions of size 1"
collective-shape distinction already recorded at `L1/orthogonalize.md:107-110,184-189`. So
at L1 this is wholly absorbed (it is *why* the `gs_orthog` variant axis exists); at the
**L1>L0 surface-form** level, it is a `GlobalSum ∘ LocalDot` realization the
`dot-mutation-rotation` Sub-pattern inventory (A: fused free-function; B: method-form;
C: real leaf) does **not** name — the **unfused, hook-routed, batched-collective** form.

### The observable-witness distinction (the load-bearing part)

The Gram-Schmidt coefficient `H[j] = dot_op(w, V[j])` is **observable** in the cycle-020
census sense (full complex value consumed, not real-projected): `H[j]` is written through
to the caller's Hessenberg-column buffer AND consumed in the residual update
`w.Add(-H[j], V[j])` (`orthog.hpp:51,73,86`). For complex vectors the full complex `H[j]`
is load-bearing (the header comment `// Note order is important for complex vectors`
at `orthog.hpp:48` is Palace's own flag that the arg order / conjugation is value-bearing
here). This is materially different from the cycle-020 inventory's `observable_unweighted`
cohort, which is **entirely** the four `nleps.cpp` SLEPc-NEP deflation/Newton sites: the
Gram-Schmidt `H[j]` is an **unweighted observable** use of the arg-2-conj convention in
**ordinary Krylov/ROM orthogonalization** (GMRES/FGMRES Arnoldi inner loop
`iterative.cpp:630,809`; ROM basis-extension `romoperator.cpp:51-66`), not deflation algebra.
The cycle-020 headline "the convention is load-bearing in exactly ONE algorithm (SLEPc-NEP)"
is **scoped to `linalg::Dot` callers** and is correct as stated; this surface widens the
*observable-convention* footprint to a second, far more common, algorithm family — but via a
DIFFERENT L0 symbol (`LocalDot`+`GlobalSum`, not `linalg::Dot`), which is precisely why the
census did not see it.

### Already-covered-transitively check (the (c) question)

- **Operator level: covered.** `L1/orthogonalize.md:163-165` names `dot` (firm) as the
  projection-coefficient inner-product dependency with the conjugate-linear-first-arg
  convention inherited directly, and `:204-211` names the `dot_op` hook as the
  inner-product variant axis. So *that orthogonalize uses the dot inner product* is firm.
  - **Clarification (not a contradiction; for the lifter applying Proposal 1):** `L1/dot.md:119`
    describes `linalg::Dot` as "used as the orthogonalisation-coefficient primitive in MGS and
    CGS," which is the **test-reference path** — `dot.md:119` cites `test-orthog.cpp`, where the
    harness computes reference coefficients via `linalg::Dot` to check `orthog.hpp`'s output. The
    *production* `orthog.hpp` routines bypass `linalg::Dot` (the thesis of this observation). The
    two coexist: test-reference computes the coefficient via the fused `linalg::Dot`, production
    computes it via the unfused `LocalDot`+`GlobalSum` (Sub-pattern D). The lifter adding
    Sub-pattern D should NOT read `dot.md:119` as conflicting with the bypass claim.
- **Lowering surface-form level: NOT enumerated.** `L1-L0/dot-mutation-rotation.md:38-145`
  lists exactly three surface forms (A free-function `linalg::Dot`, B method `(*this).Dot`,
  C real `LocalDot`). The `orthog.hpp` hook-routed `LocalDot` + **batched** `Mpi::GlobalSum`
  is a fourth surface shape (the unfused, multi-element-collective realization) — currently
  un-named there. Note: `dot-mutation-rotation` already cites
  `orthogonalization` as a witness algorithm in prose (`:333` "CG / orthogonalization /
  NLEPS sites") but does not point at `orthog.hpp:34,49-50,68-70` or characterize the
  unfused/batched shape.
- **Census-inventory level: explicitly flagged-out.** The cycle-020 inventory
  (`inner-product-fold-specialization.md:301-329` `conjugation_caller_inventory`) is scoped
  `every linalg::Dot caller` and does not — correctly, by its own scope — include the
  `LocalDot`+`GlobalSum` orthog sites. The cycle-020 report's own Open-questions
  (`:203-208`) names this as a follow-up "coverage gap of its own".

Verdict: **(a)** additional call-surface of `dot`, **benign at the operator level but with
two small additive citation gaps** (the unfused/batched surface form; the unweighted-observable
non-deflation witness).

## Proposed changes

These are **proposals for the integrator / a follow-up lifter** — I do NOT touch `book/`.
Two small additive citations; neither changes any status (every entry stays `firm`). The
cleaner carrier is the `dot-mutation-rotation` surface-forms section (the L1>L0 theme owns
the L0 realization inventory); the census-inventory yaml in
`inner-product-fold-specialization.md` can optionally gain a sibling note. Both are additive.

### Proposal 1 (preferred) — name the unfused/batched surface form in `dot-mutation-rotation`

Append a Sub-pattern D to `book/src/L1-L0/dot-mutation-rotation.md` §"L0 form (RHS)",
after Sub-pattern C (`:115-144`), recording the `orthog.hpp` hook-routed realization:

```edit:book/src/L1-L0/dot-mutation-rotation.md
[insert after Sub-pattern C, before "## The conjugation asymmetry — the core theme content"]

### Sub-pattern D — hook-routed `LocalDot` + batched `Mpi::GlobalSum` (the unfused form)

    // orthog.hpp:29-36 — the canonical InnerProductHelper
    struct IdentityInnerProduct {
      template <typename VecType>
      auto operator()(const VecType &x, const VecType &y) const { return LocalDot(x, y); }
    };
    // orthog.hpp:66-70 — CGS open-codes the two-step with a BATCHED collective
    for (std::size_t j = 0; j < m; j++) { H[j] = dot_op(w, V[j]); }   // m local dots
    Mpi::GlobalSum(m, H, comm);                                       // ONE size-m reduction

Palace's Gram-Schmidt routines (`OrthogonalizeColumnMGS` / `OrthogonalizeColumnCGS`,
`orthog.hpp`) do NOT call the fused `linalg::Dot` (Sub-pattern A). They reach the same
`yᴴ x` reduction through the `InnerProductHelper` template hook, whose canonical
`IdentityInnerProduct::operator()` returns `LocalDot(x, y)` (`orthog.hpp:34`), and the
routine itself applies `Mpi::GlobalSum` over the coefficient buffer. This is the **unfused**
realization of Sub-pattern A's `Mpi::GlobalSum ∘ LocalDot`: the local dot and the collective
are split across the hook boundary so MGS can interleave `w.Add(-H[j], V[j])` per `j`
(`:49-51`, `m` size-1 reductions) and CGS can **batch** the collective into one
`Mpi::GlobalSum(m, H, comm)` across all `m` coefficients (`:68-70`, 1 size-`m` reduction;
CGS2 = two such passes, `:75-88`). Value-identical to Sub-pattern A modulo the reduction-tree
non-law; the batching is the transparent collective-shape trick that motivates the
`L1/orthogonalize` `gs_orthog` variant axis (`book/src/L1/orthogonalize.md:107-110,184-189`).

**Observability note.** Unlike the real-projected CG coefficients, the Gram-Schmidt `H[j]`
is consumed as a **full complex value** (the residual update `w.Add(-H[j], V[j])` and the
Hessenberg-column store), so this is an **unweighted observable** use of the arg-2-conj
convention — the header's own `// Note order is important for complex vectors`
(`orthog.hpp:48`) flags it. It is the first cited unweighted-observable `dot` use OUTSIDE
the SLEPc-NEP deflation cohort (the cycle-020 `linalg::Dot`-caller census,
`book/src/L2-L1/inner-product-fold-specialization.md:301-329`, found only `nleps.cpp` because
it scoped `linalg::Dot` callers and `orthog.hpp` bypasses `linalg::Dot`).

Justification kind: **structural** — the unfused two-step is the same expansion as
Sub-pattern A with the collective lifted out of the per-dot call and (in CGS) batched.

Citations:
- `palace/linalg/orthog.hpp:29-36` — `IdentityInnerProduct`; `return LocalDot(x, y)` at `:34`.
- `palace/linalg/orthog.hpp:46-52` — MGS per-`j` `H[j]=dot_op(w,V[j]); Mpi::GlobalSum(1,&H[j],comm); w.Add(-H[j],V[j])` (m size-1 collectives, interleaved).
- `palace/linalg/orthog.hpp:66-88` — CGS `m` local dots then ONE `Mpi::GlobalSum(m, H, comm)` (`:70`); CGS2 `refine` second pass `:75-88`.
- `palace/linalg/vector.cpp:665-685` — the `LocalDot` real (Hypre) / complex (four-real-dot, `yᴴ x`) kernels the hook resolves to.
- `palace/utils/communication.hpp:266-270` — `Mpi::GlobalSum(len, buff, comm) → GlobalOp(..., MPI_SUM, ...)`.
```

### Proposal 2 (optional, additive) — sibling note in the census inventory

If the integrator prefers the census inventory to record the bypass surface too, append to
`book/src/L2-L1/inner-product-fold-specialization.md` §Applicability Condition 5, after the
`conjugation_caller_inventory` yaml block (`:329`), a one-line scope note (NOT new yaml keys —
the existing block is scoped `linalg::Dot` callers and should stay so):

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[append one paragraph after the conjugation_caller_inventory yaml fence at :329]

**Bypass surface (out of the `linalg::Dot`-caller scope, recorded for completeness).** Palace's
Gram-Schmidt routines (`palace/linalg/orthog.hpp`) reach the same unweighted `yᴴ x` reduction
WITHOUT calling `linalg::Dot`: the `InnerProductHelper` hook's `IdentityInnerProduct` calls
`LocalDot(x, y)` directly (`orthog.hpp:34`) and the routine applies `Mpi::GlobalSum` itself
(the unfused two-step; CGS batches it into one size-`m` reduction, `orthog.hpp:68-70`). The
coefficients `H[j]` are **unweighted observable** (consumed in the residual update
`w.Add(-H[j], V[j])`, header flag `// Note order is important for complex vectors` at
`orthog.hpp:48`) — the first unweighted-observable `dot` use outside the `nleps.cpp` deflation
cohort. This surface is enumerated as Sub-pattern D of
[`dot-mutation-rotation`](../L1-L0/dot-mutation-rotation.md); it is not in the
`conjugation_caller_inventory` above because that block is scoped to `linalg::Dot` call sites.
```

If the integrator prefers minimal touch, **Proposal 1 alone** suffices (it is the natural home
— the L1>L0 theme owns the L0 surface-form inventory); Proposal 2 is a convenience
cross-reference only. Either way, no status changes.

## Follow-up candidates

- **lifter** — re-anchor `L1-L0/dot-mutation-rotation` to add Sub-pattern D (Proposal 1).
  This is the load-bearing output; small, additive, no status change. The theme is `firm`
  and stays `firm`.
- **NOT harvester** — this is NOT a new primitive (rules out kind (b)); the `dot` leaf and
  `orthogonalize` operator both already exist and are firm. No harvest is warranted.
- **abstractor (deferred, low priority)** — the `orthogonalize-mutation-rotation` L1>L0 theme
  is still un-authored (`L1/orthogonalize.md:321-325` flags it as queued abstractor work).
  When authored, it will narrate the per-variant collective shape (m×1 / 1×m / 2×m
  `Mpi::GlobalSum` reductions) and should cite Sub-pattern D of `dot-mutation-rotation` for
  the inner-product realization rather than re-deriving it. Flag, do not enact here
  (one-observation discipline; that theme is its own dispatch).

## Supporting evidence

All ranges read this invocation (paths relative to `reference/`); self-verified per
`verify-citation-range`:

- `palace/linalg/orthog.hpp:1-93` (full file) — `IdentityInnerProduct` struct `:29-36`
  (`return LocalDot(x, y)` at `:34`); `OrthogonalizeColumnMGS` `:39-53` (per-`j`
  `H[j]=dot_op(w,V[j])` `:49`, `Mpi::GlobalSum(1,&H[j],comm)` `:50`, `w.Add(-H[j],V[j])`
  `:51`); `OrthogonalizeColumnCGS` `:55-89` (m local dots `:66-69`, batched
  `Mpi::GlobalSum(m,H,comm)` `:70`, m `w.Add`s `:71-74`, CGS2 `refine` second pass `:75-88`);
  scope-contract comment `:18-23` ("does not normalize"); order-matters comment `:48`.
- `palace/linalg/vector.cpp:665-672` — `LocalDot(Vector, Vector)` real, single Hypre
  `hypre_SeqVectorInnerProd`, `MFEM_ASSERT(x.Size()==y.Size())` at `:668`.
- `palace/linalg/vector.cpp:674-685` — `LocalDot(ComplexVector, ComplexVector)`: four real
  dots, `Im = LocalDot(xi,yr) − LocalDot(xr,yi)` = `yᴴ x` (arg-2 conjugated), `&x==&y`
  self-dot fast path imag=0 at `:678`.
- `palace/linalg/vector.hpp:242-244` — `LocalDot` decls + comment `// Calculate the local
  inner product yᴴ x or yᵀ x`.
- `palace/linalg/vector.hpp:247-253` — `linalg::Dot` template = `Mpi::GlobalSum(1, &dot)`
  ∘ `LocalDot(x, y)` (the FUSED form `orthog.hpp` does NOT use).
- `palace/utils/communication.hpp:265-270` — `Mpi::GlobalSum(len, buff, comm) → GlobalOp(len,
  buff, MPI_SUM, comm)` (the collective the orthog routine applies itself).
- `book/src/L1/dot.md` — firm `dot` leaf: arg-1-conj L1 convention (`:43`), the `LocalDot`/`Dot`
  family in Context (`:7`), `orthog` tests cited as orthogonalization-coefficient witness (`:119`).
- `book/src/L1/orthogonalize.md` — firm operator: `dot` dependency + conjugate-linear-first-arg
  inheritance (`:163-165`); the `dot_op` / `InnerProductHelper` inner-product variant axis
  (`:204-211`, evidence `:251-254`); the per-variant collective-shape distinction (`:107-110`,
  `:184-189`); L1>L0 theme flagged un-authored (`:321-325`).
- `book/src/L1-L0/dot-mutation-rotation.md` — firm L1>L0 theme: Sub-patterns A/B/C
  (`:44-145`); `orthogonalization` named in prose only (`:333`); the `GlobalSum ∘ LocalDot`
  two-step (Sub-pattern A, `:44-81`).
- `book/src/L2-L1/inner-product-fold-specialization.md` — the cycle-020 `conjugation_caller_inventory`
  (`:301-329`, scoped `linalg::Dot` callers) + the wave-1 re-order narration (`:158-220`).
- `reports/2026-05-29T034441Z-cross-layer-cross-cutter-dot-callers/CYCLE.md` — the cycle-020
  census that flagged this surface (`:100-103` definitions-excluded note; `:203-208`
  follow-up calling for exactly this audit).

## Open questions / caveats

- **OQ (evidence-completion, small, non-blocking)** — `orthog-hpp-localdot-globalsum-unfused-dot-surface`:
  Palace's Gram-Schmidt (`orthog.hpp`) reaches the unweighted `dot` (`yᴴ x`) reduction via the
  `InnerProductHelper` hook (`LocalDot` at `:34`) + a self-applied (and in CGS, batched)
  `Mpi::GlobalSum`, bypassing `linalg::Dot`. It is the **unfused** realization of
  `dot-mutation-rotation` Sub-pattern A and an **unweighted observable** use of the arg-2-conj
  convention outside the `nleps.cpp` deflation cohort. **Follow-up**: lifter adds Sub-pattern D
  to `dot-mutation-rotation` (Proposal 1). No status change implied. Resolves the cycle-020
  report's flagged "coverage gap of its own"
  (`reports/2026-05-29T034441Z-cross-layer-cross-cutter-dot-callers/CYCLE.md:203-208`).

- **Caveat (observability is for the *complex* element type only).** The Gram-Schmidt `H[j]`
  is observable-and-convention-sensitive only when `w`/`V` are complex (real `dot` makes the
  conjugation a no-op, so the arg order is invisible for real bases). Palace's GMRES/FGMRES
  Arnoldi runs both real and complex (`test-orthog.cpp:123,234`); the convention is load-bearing
  on the complex parametrizations. The header comment `// Note order is important for complex
  vectors` (`orthog.hpp:48`) is precisely this caveat in Palace's own words.

- **Caveat (B-weighted hook is a DIFFERENT surface — out of this observation).** The SLEPc/ROM
  `dot_op` substitution (B-weighted inner product, `L1/orthogonalize.md:204-211`,
  `romoperator.cpp:59-65`) is the *weighted* member and is NOT `IdentityInnerProduct`/`LocalDot`.
  It would route through the weighted `linalg::Dot(comm, x, A, y)` / a `bilinear_form` flavor,
  not `LocalDot`. This observation is scoped to the **unweighted** `IdentityInnerProduct` path
  (`orthog.hpp:34`) only; the weighted hook is covered by the `inner_product` weight axis and is
  a separate surface (not re-audited here, one-observation discipline).

- **Caveat (this is benign at the operator level — not a contradiction or a redundancy to
  eliminate).** The two surfaces (`linalg::Dot` fused, `orthog.hpp` unfused-batched) are not a
  redundancy to merge — the unfusing is *load-bearing* (it is what lets MGS interleave and CGS
  batch the collective, the entire reason the `gs_orthog` variant axis exists). The observation
  is that the *surface form* and the *observable witness* are uncited, not that the code is
  duplicative. No unification is proposed.

- **Direction-of-definition: clean.** Read-only L0-evidence audit feeding an additive citation
  into an existing firm L1>L0 theme (the surface-form inventory). No high→low violation; no
  `book/` mutation (the proposed-changes blocks are proposals for the integrator/lifter per the
  dispatch-phase write-guard).
