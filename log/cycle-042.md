# 2026-06-01 cycle-042 — integration summary

**Foundation-first L2-floor build: the 5 fork-independent standalone floors + their 10 thin-identity themes + the leaf-vs-fold adjudication-evidence audit.**

> NOTE on numbering: this is the **layered-era cycle-042** (post-2026-05-26 structural redirect). A legacy **slice-vertical-era cycle-42** entry (2026-05-25, "back orthog") is preserved at the bottom of this file for historical continuity; the two are distinct cycles that collide only on the zero-padded filename.

**Kind:** integration (primary cycle — phases plan → dispatch → critique → repair → integrate)
**Meta-batch:** batch-12, position 3 of 3 (cycles 040/041/042). **The batch-12 meta-phase fires AFTER this finalize commit, as a SEPARATE dispatch — NOT run in this cycle.** The cycle counter does NOT reset across batch boundaries.
**Written by:** `integrator-finalize` (split integrator-per-report ×11 + finalize ×1).

## Headline

The third/final primary cycle of meta-batch-12 advanced the foundation-first L2-floor build (under the 2026-05-31 `foundation_solidity` directive) with the **5 fork-INDEPENDENT standalone-floor members** + their **10 thin/pure-identity L2>L1 + L3>L2 themes** + a **leaf-vs-fold adjudication-evidence audit**:

- **L2 firm 12 → 17** — `book/src/L2/{reciprocal,elementwise_product,assemble-diagonal,jacobi-smoother,divfree-projector}.md` (5 NEW firm floors).
- **L2>L1 firm 10 → 15** — `book/src/L2-L1/{reciprocal,elementwise-product,assemble-diagonal,jacobi-smoother,divfree-projector}-leaf-identity.md` (5 NEW firm themes).
- **L3>L2 firm 5 → 10** — `book/src/L3-L2/{reciprocal,elementwise_product,assemble-diagonal,jacobi-smoother,divfree-projector}-body-identity.md` (5 NEW firm themes).
- `l3-l2-rotation-theme-coverage-gap` advanced **5-of-18 → 10-of-18**.
- `l2-floor-under-l3-blas1-cohort` now **8-of-13** (c041: dot/nrm2/scal; c042: the 5 above). Remaining 5: the `axpy`/`axpby`/`axpbypcz` arity-family (HELD pending the fork) + `chebyshev` + `normalize`.

The foundation-first directive is materially advancing the stack toward rectangular: the L2 floor now spans the BLAS-1 leaves, the elementwise primitives, the operator-to-data primitive, and the constructed-operator gates.

## The 5 floors (D2-D6)

All 5 are **fork-INDEPENDENT** (no fold-parent) — design-final regardless of the batch-12 leaf-vs-fold adjudication. The floor cohort is heterogeneous:

- **`reciprocal`** (D2) — fold-parent-free elementwise multiplicative-inverse leaf; thin identity-in-form; 8 laws inherited from L1; firm-on-positive-structure on the complex kernel.
- **`elementwise_product`** (D3) — standalone Hadamard binary field op, NO fold-parent; ten laws + two variant axes (element-type + conjugation sub-axis). D3 reconciled `L3/elementwise_product.md` INLINE (3 edits) — the only in-cycle L3 reconciliation.
- **`assemble-diagonal`** (D4) — operator-to-data diagonal-introspection primitive, sibling-of-`apply_linop`; the **load-bearing matrix-free high-order-Nedelec approximate-diagonal non-law** is preserved through the floor → `firm`, NOT `partly-constructive`.
- **`jacobi-smoother`** (D5) — the thinnest constructed-operator gate; per-call body is one elementwise product `(ω·D⁻¹) ⊙ x`; fusion-rotation is NEGATIVE (no fused multi-operation kernel to unfold).
- **`divfree-projector`** (D6) — MODERATE floor (not thin): the ONE genuine fusion-rotation = step-4 `Grad->AddMult(ψ,y,1.0)` de-fused to `apply_linop ▷ axpy`; the inner-solve `sequential-obstruction` is carried BY REFERENCE through firm `ksp_solve`, neither introduced nor erased.

## The 10 themes (D7-D10)

5 L2>L1 leaf-identity + 5 L3>L2 body-identity edges, all fork-INDEPENDENT. Four leaf-identity edges are pure-identity-in-form; **`divfree-projector-leaf-identity` is the FIRST mostly-identity-with-one-rotation edge** (carries the projector's ONLY fusion — the step-4 `Grad->AddMult` re-fusion). The 5 body-identity edges are all L3-native-by-signature (per `krylov-step-body-identity.md:97`), no wrapper + no fold-parent to rotate.

## The leaf-vs-fold audit (D1) — RIPE FOR ADJUDICATION

D1's cross-cutter audit is an OBSERVATION (no `book/` mutation); its sole landing is a prominent OQ promotion annotating the canonical fork OQ `dot-l2-leaf-floor-vs-fold-only-design` with the audit VERDICT. **It RECOMMENDS keeping the leaf-floor (b) reading cohort-wide**: the `+files` are thin deferring-pointers below the duplication-explosion bar; they are genuinely-distinct duals on the layer-coherence axis; and the fork is **ASYMMETRIC** — it applies to the fold-MEMBERS `dot`/`scal`, NOT `nrm2` the consumer, NOT the 5 fork-independent c042 floors. **The batch-12 meta-phase (fires next) must adjudicate this + decide the HELD axpy-family framing.**

## Process

- **11 of 11 dispatched-ready reports applied clean.** 11/11 staging rows == dispatched-ready — the cycle-018 staging-completeness gap did NOT recur for the **TWENTY-THIRD consecutive** cycle. Zero deferrals, zero rejections, zero build-repairs.
- **Thirty-seventh consecutive cycle under the split integrator.**
- **`cycle-planner-stale-priorities-line-recruitment` did NOT recur** — the THIRD/FINAL clean opus-planner cycle of batch-12; the escalating recurrence-6 friction is structurally CLOSED across the full batch-11 + batch-12 confirmation window (the haiku→opus swap is steady-state under the 2026-05-31 blanket Opus-4.8 upgrade).
- **Count-ownership partition held** — D2-D10 each touched ONLY their own dep-map/theme rows; D11 (layer-intro-author) was the SOLE consolidated count-owner. `parallel-blind-shared-index-count-divergence` did NOT recur across the broadest 11-wide wave yet.
- **Build clean** — `cargo make book` exit 0 (~90s); the only warnings are the pre-existing KaTeX "Potential incomplete link" false-positives in `design/l4_calculus.md` (rendered-math HTML mis-parsed by mdbook-linkcheck, unrelated to this cycle). linkcheck2 green for all 15 new entries + the critical D10 `../L1-L0/reciprocal-elementwise-product-mutation-rotation.md` leaf-identity links. Zero build-repairs.

## Carry-forward to the batch-12 meta-phase (fires next, separate dispatch)

1. **ADJUDICATE `dot-l2-leaf-floor-vs-fold-only-design`** (D1 recommends keep-(b) cohort-wide; asymmetry finding) + decide the HELD axpy-family framing.
2. **Slug-naming normalization** — the cohort carries 3 conventions (`-leaf-identity`/`-body-identity`, `-fold-specialization`, + the `elementwise_product` underscore/hyphen split); consolidated as OQ `l2-floor-cohort-slug-naming-de-facto-convention`.
3. **Directive-name rename** — `l2-floor-under-l3-blas1-cohort` now spans non-BLAS-1 members (operator-to-data + constructed-operator gates).
4. **Consolidated cycle-043 lifter sweep** — re-anchor the 4 stale firm L3 entries (`reciprocal`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`) L3>L1 → L3>L2>L1 (both stale clauses); co-schedule the `:39`→`:46` self-citation sweep + the `L1/assemble-diagonal.md:111` `:172`→`:174` drift. (`elementwise_product` reconciled inline this cycle.)
5. **Next foundation slice (post-fork)** — axpy-family L2 floors (gated) + `chebyshev` + `normalize` (the last 5 of 13).

## Counts after cycle-042

L1 firm 26 · **L2 firm 17** · **L2>L1 firm 15** · L3 firm 15 + 3 partial-obstruction · **L3>L2 firm 10** · L4 firm 4 · L0 chapters 22 · Phase-1 removals 9/10.

---

## (legacy / historical) 2026-05-25 cycle-42 — back orthog — pass

- Synthesis: Orthog slice already has L1+L2 content on disk from a prior cycle; this cycle backfills the missing L0→L1 rotation_claims (variant absorption, dot_op hook, normalization-out, MGS/CGS/CGS2 substitutability) against the existing prose with file:line citations into palace/linalg/orthog.hpp and test-orthog.cpp.
- Verdict: pass.
- Friction: none.
- Structural change: none.
