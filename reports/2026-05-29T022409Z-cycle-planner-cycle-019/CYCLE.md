---
agent: cycle-planner
invoked_at: 2026-05-29T022409Z
scope: cycle-019 dispatch plan
status: pending
---

# Cycle-019 dispatch plan

## Goals selected this cycle

Cycle-019 is the **FIRST primary cycle of meta-batch-5** (cycles 019/020/021). The cycle-018 integrator landed the BLAS-1 human-raise **completion**: `linear_combination` L2 firm (cycle-018, cycle-017 rough-in) + `linear-combination-fold-specialization` L2>L1 theme (cycle-018) + the `inner_product` L2 rough-in row and concept page (cycle-018). The 10 stub homes were materialized 2026-05-28 so several backlog items are now "firm the stub in place" rather than "create from scratch."

**Dispatch rationale:** The cycle-019 active head prioritizes the HEADLINE `inner_product` harvester (highest-fan-out, unblocked by the rough-in row), paired with its L2>L1 lowering theme + carry-forward follow-ups on `linear-combination-fold-specialization` (mirroring the cycle-017/018 linear_combination pairing). The large carry-forwards (`gmres.md §L4 self-rotation`, NLEPS at L1+) remain high-priority but are held for likely cycle-020 dispatch (cycle-019 is dense with the inner_product pairing + the layer-intro-author fespace dispatch + the new combinator-miner family-mode test). The backlog's High-fan-out tier (l2-named-composition-lifts, ksp-solve-l2-promotion, l3-vocabulary-inventory-gap, blas1-l1-l0-lowering-theme-gap) supplies the remaining slot, plus exploratory family-mode combinator work.

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|---|---|---|---|
| 1 | **harvester** | L2 `inner_product` firm operator (stub home at `book/src/L2/inner_product.md`) | none | **HEADLINE.** Cycle-018 combinator-miner landed the rough-in dep-map row (≥3-instance bar: `dot`, `tdot`, `bilinear-form`). Author firm L2 entry mirroring how cycle-018's harvester firmed `linear_combination` off the cycle-017 rough-in. **Pin the conjugation / arg-order convention** (`Dot(comm,x,A,y) = yᴴ A x` per Palace source). Self-verify every L0 citation before emit. Forward-refs to not-yet-authored siblings (`bilinear-form` rough-in, `dot`/`tdot` firm at L1) stay plain-text per cycle-018 conventions. **Pairs with dispatch #2.** — OQ `inner-product-harvester-formalization-and-conjugation-pinning`; plan Now (active) #1; integrator-signals cycle-018 Unblocked |
| 2 | **abstractor** | L2>L1 `inner-product-fold-specialization` theme (stub home at `book/src/L2-L1/inner-product-fold-specialization.md`) + `linear-combination-fold-specialization` carry-forward follow-ups | 1 | **Lowering theme** taking the L2 `inner_product` fold into its L1 specializations (arity/conjugation variants). Mirrors the just-landed cycle-018 `linear-combination-fold-specialization` pairing. Includes pending follow-ups on the cycle-018 theme from the integrator-signals carry-forward. — OQ `inner-product-fold-sibling-candidate`, `linear-combination-fold-specialization-theme-followups`; plan Now (active) #2 |
| 3 | **layer-intro-author** | L0 bundle-6 #6 — FE-space header L0 anchor (`palace/fem/fespace.{hpp,cpp}` per Palace source check) | none | **Input-side FE-space L0 anchor.** Next ranked bundle-6 chapter after cycle-016's `fem-libceed-operator-file`. Citation-dense; emit proposed-changes blocks only (write-guard enforced). Self-verify each range via codemap before emit. — OQ `bundle-6-fespace-anchor`; plan Now (active) #5; integrator-signals cycle-018 Suggested next dispatches |
| 4 | **combinator-miner** | Parametric / variadic-family detection mode FIRST LIVE TEST — scan for the next parametric family (obvious candidates: the `inner_product` conjugation-convention cohort; longer-term, smoother/preconditioner families). Exercise the NEW cycle-018 family-mode to surface parametric siblings as a single candidate. | none | **Novel mode debut.** The cycle-018 parametric/variadic-family detection mode (HEADLINE enactment, cycle-018 meta) is ready for first live exercise. Test on a near-term candidate (conjugation variants: `dot` reduce vs `linear_combination` n-ary fold + weight variants in M-weighted forms). If ≥2 siblings confirmed, propose as a parametric-family combinator candidate. — OQ `combinator-miner-arity-blind-parametric-family-detection`; plan Now (active) #7; friction-ledger `combinator-miner-arity-blind-parametric-family-detection` addressed by meta-phase spec change |
| 5 | **harvester** | L2 `orthogonalize` firm operator promotion (stub home at `book/src/L2/orthogonalize.md`) | none | **High-fan-out Backlog tier item.** The L1 `orthogonalize` operator landed firm cycle-012; the L2 entry is a stub (claim-free placeholder, 2026-05-28 materialization). Author firm L2 entry capturing `orthogonalize` as a *first-class L2 composition* (not just an L1 leaf invoked in context). The operator is reused by GMRES/FGMRES/Arnoldi/eigenmode all consuming it at L2 — firming it sharpens every downstream Krylov lowering. Variant-axis discipline + test coverage closure per cycle-018 precedent. — OQ `orthogonalize-as-future-L2-firstclass-entry`; plan Backlog High fan-out `l2-named-composition-lifts`; roadmap Shared Infra / Orthogonalisation |
| 6 | **lifter/cross-layer-cross-cutter** | `divfree.hpp` doc-tension OQ resolution (`palace/linalg/divfree.hpp`) | none | **Carry-forward cycle-003+ OQ.** Residual doc-comment / header tension on divfree semantics (friction-ledger `divfree-mult-doc-irrotational-vs-divfree-stale`). Verify or document the source-side contradiction; surface a plan item if a substantive re-anchor is warranted. Read-only audit or propose minimal re-anchor edits. — OQ `divfree-mult-doc-irrotational-vs-divfree-stale`; plan Now (active) #6 |
| 7 | **abstractor** | L1>L0 `nrm2-mutation-rotation` theme (stub home at `book/src/L1-L0/nrm2-mutation-rotation.md`) | none | **High-fan-out Backlog tier item.** BLAS-1 L1>L0 lowering-theme gap: `nrm2` is used by orthogonalization, iterative solvers, eigenmode residual checks but only `axpby`/`axpbypcz`/`apply-linop` have explicit L1>L0 themes. Author the L1>L0 theme covering nrm2's `abs`-guarding (defensive choice, load-bearing for real-vector fallback) + Allreduce + sqrt chain. Cite the negative-result slice documentation pattern. Variant-axis: real/complex element type, with element-type collapse per `nrm2.md`. — OQ `nrm2-lowering-theme-deliverables`, `nrm2-std-abs-defensive-guard-classification`; plan Backlog High fan-out `blas1-l1-l0-lowering-theme-gap` |
| 8 | **harvester** | L1 `assemble-diagonal` primitive (stub home at `book/src/L1/assemble-diagonal.md`) | none | **Medium-fan-out Backlog tier item.** `AssembleDiagonal` is a distinct L1 operator (NOT an `apply_linop` variant per the OQ). Used by Jacobi / Chebyshev / block-Jacobi / polynomial preconditioners for diagonal extraction. Harvest as a fused `(Operator) -> (Tensor[N])` operator with variant-axis on operator type (scalar/vector/tensor-field domains) and output-storage. Road-map Intermediate-tier "Diagonal-preconditioner apply." — OQ `assemblediagonal-is-not-apply-linop-variant`; plan Backlog Medium fan-out; roadmap Intermediate-tier Diagonal-preconditioner |

## Overlap analysis

### Dispatch pairs and conflicts

**Dispatches #1 and #2 (harvester + abstractor on inner_product cohort):**
- **Overlap:** Dispatch #2 depends on #1 (abstractor references L2 `inner_product.md` chapter which #1 authors).
- **Sequencing:** #1 must complete before #2; marked sequential, not parallel.
- **Integration serialization:** integrator-per-report applies #1 first, then #2 when the live link resolves.

**Dispatch #5 (orthogonalize L2 harvester):**
- **No overlap with #1/#2/others.** Orthogonalize is a distinct L2 operator (sibling to `linear_combination`, not a dependency).
- **Parallel eligible:** can dispatch in wave-1 with #3/#4/#6/#7/#8.

**Dispatch #3 (layer-intro-author on fespace L0):**
- **No overlap with other dispatches.** L0 bundle work is orthogonal to L1/L2 operator work.
- **Parallel eligible:** wave-1 with #4/#5/#6/#7/#8 (and wait for #1/#2 only if there's a cross-layer cite).

**Dispatch #4 (combinator-miner family-mode test):**
- **No overlap.** The combinator audit is read-only on existing artifacts; output is a proposal in CYCLE.md, not artifact mutation.
- **Parallel eligible:** wave-1.

**Dispatch #6 (divfree.hpp doc tension):**
- **No overlap.** Read-only audit of Palace source, proposals only.
- **Parallel eligible:** wave-1.

**Dispatches #7 and #8 (nrm2 L1>L0 theme + assemble-diagonal L1 harvester):**
- **No mutual overlap.** Distinct operators, distinct layers.
- **Parallel eligible:** wave-1.

### Summary

- **Wave 1 (parallel):** Dispatches #3, #4, #5, #6, #7, #8 (6 dispatches, independent).
- **Wave 2 (serial within, after wave-1 reports land):** Dispatches #1 (harvester) then #2 (abstractor, depends on #1).

**Total: 8 dispatches.** Well within the 12-dispatch target.

## Sequencing schedule

```
Wave 1 (parallel dispatch):
  - Dispatch #3 (layer-intro-author, fespace L0)
  - Dispatch #4 (combinator-miner, family-mode test)
  - Dispatch #5 (harvester, orthogonalize L2)
  - Dispatch #6 (lifter/cross-layer-cross-cutter, divfree doc audit)
  - Dispatch #7 (abstractor, nrm2 L1>L0 theme)
  - Dispatch #8 (harvester, assemble-diagonal L1)

Wave 2 (serial, after wave-1 integrator finalize):
  - Dispatch #1 (harvester, inner_product L2 firm)
  - Dispatch #2 (abstractor, inner-product-fold-specialization L2>L1 theme) [depends on #1]

Integration sequencing:
  - integrator-per-report applies all 6 wave-1 reports serially (per-report serial dispatch discipline)
  - integrator-per-report applies #1, then #2 (per-dispatch serialization for dep)
  - integrator-finalize: one-pass rebuild
```

## Open questions / caveats

### Dispatch scope refinement needed

1. **Dispatch #1 (inner_product harvester) — L0 range self-verification.** The scope says "self-verify every citation before emit" per cycle-018 discipline. The conjugation convention pinning requires identifying Palace's canonical form (`Dot(comm,x,A,y) = yᴴ A x`). The harvester should use the codemap to locate all instances and cite them by range. The OQ name is explicit: `inner-product-harvester-formalization-and-conjugation-pinning`.

2. **Dispatch #3 (fespace L0) — citation density.** Layer-intro-author prompt includes "Citation-dense; emit proposed-changes blocks only (write-guard enforced)." The `palace/fem/fespace.{hpp,cpp}` pair are entry-point for FE-space construction. The dispatch is scoped to author the L0 anchor; likely requires multiple citation ranges (FiniteElementSpace class, quadrature, basis functions, geometric-factor computation). Verify the Palace source has sufficient clarity to ground the entry, or defer to cycle-020 if coverage gaps surface.

3. **Dispatch #4 (combinator-miner family-mode test) — over-unification guard.** The new parametric-family mode detects arity/conjugation/weight families. The `inner_product` conjugation cohort is an obvious near-term test case (`dot`, `tdot`, `bilinear-form` — the reduce-to-scalar fold differing in conjugation convention + weight presence). The miner's CYCLE.md should state the concrete cohort, the fold-law evidence (why they're a family), and any over-unification guard (e.g., "do NOT subsume `linear_combination` because it is a *different fold* — reduce-to-Tensor[N], not reduce-to-Scalar"). The family-mode is live for the first time; this dispatch exercises and validates the new mode.

4. **Dispatch #6 (divfree doc audit) — outcome ambiguity.** The OQ `divfree-mult-doc-irrotational-vs-divfree-stale` has carried for 2+ batches. A `lifter/cross-layer-cross-cutter` dispatch is read-only; the outcome could be (a) resolve the contradiction with a clarifying note, (b) surface a re-anchor OQ if the source is genuinely ambiguous, or (c) declare the doc-tension non-actionable. The CYCLE.md should state the finding clearly. If a re-anchor is warranted, add it to the Backlog for a future abstractor dispatch.

### Coordination with integrator

- **Dispatch #3 proposed-changes blocks:** The layer-intro-author writes CYCLE.md with proposed-changes blocks (no write to `book/` during dispatch per write-guard). The integrator-per-report applies the changes when the dispatcher's context is no longer live. Verify the format matches the cycle-018 precedent (`book/src/L0/` references).

- **Wave-2 sequencing at integration:** The integrator-per-report applies #1 first. The STAGING.md row for #1 must be appended before #2 is dispatched. Confirm the staging row captures the `inner_product.md` home location so #2's link resolution is clear.

### Carry-forward notes for cycle-020

The large carry-forwards remain high-priority:
- **GMRES.md §L4 v0.6→v0.7 self-rotation** (plan Now (active) #3): large, recurring across batches. Cycles 008/011 landed GMRES/FGMRES sister themes at L4-L3; promoting to L4 entry + L4-L3 consolidation would close a multi-cycle OQ. **Candidate for cycle-020 wave-1 if wave-19 finalize is clean.**
- **NLEPS at L1+** (plan Now (active) #4): large multi-cycle carry-forward. Requires sustained context. **Defer to cycle-020 or cycle-021 dedicated slot.**

These were intentionally held for a later cycle to keep cycle-019's density manageable (8 dispatches, pairing structure on inner_product, new combinator-miner mode exercise).

### Friction and methodology observations

- **Combinator-miner parametric-family mode validation:** This is the first live test of the cycle-018 meta-phase enactment (the parametric/variadic-family detection mode in `.claude/agents/combinator-miner.md`). The instance-counting heuristic previously was arity-blind; the BLAS-1 `linear_combination` fold was never auto-surfaced and had to be human-raised. The new mode should surface parametric families as a single candidate. Cycle-019 dispatch #4 is the validation window. If the mode performs as specified, friction-ledger entry `combinator-miner-arity-blind-parametric-family-detection` is resolved. If gaps surface, they should be noted in the dispatch report for the next meta-phase.

- **Stub-to-firm promotion cadence:** Cycle-019 has 5 harvester/abstractor dispatches on stub homes (dispatches #1, #5, #7, #8 + the #2 theme depending on #1). This is the first cycle executing the "stub→rough-in→firm" lifecycle at scale. Monitoring per-report integrator performance and critic gates on stub→rough-in transitions will inform the meta-phase on whether the stub-materialization policy is sustainable.

- **Cycle-019 wave structure:** This is the first cycle under the post-meta-batch-5-kickoff cadence (session restart ensured all 11 updated agent definitions are live). The wave-1 parallel dispatch of 6 independent dispatches + wave-2 serial dispatch of the inner_product pairing tests the integrator's per-report serial application + wave-mate parallel critic+repairer handling. If integrator performance stays clean, the cadence supports future batches' 8–12 dispatch density targets.
