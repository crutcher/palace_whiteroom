---
agent: layer-intro-author
invoked_at: 2026-06-03T221456Z
scope: cycle-085 D1 — FEATURE-SURFACE SPINE driver-leaf cohort re-evaluation under OWN-COMPOSITION rule + sole owner of feature/index.md
status: integrated
integrated_at: 2026-06-03T225500Z
integration_commit: 7e5ab2d
integration_notes: "Applied clean as D1 (staging row 1, byte-disjoint, SOLE-owner feature/index.md). 9 driver-leaf frontmatter flips seed→firm (eigenmode/driven/transient × 3 levels) + electrostatic/magnetostatic/boundary-mode STAY seed (own-constituent gate prose) + feature/index.md 6-firm/6-seed re-narration. Retroactive-budget 0. Build exit 0, no build-repair, no new files, no SUMMARY change. 3 OQs promoted (feature-column-firm-token-choice-batch-27-meta-phase + waveguide-mode-output-product-column-would-promote-boundary-mode + electrostatic-magnetostatic-stay-seed-overrides-priorities-1-expectation). Part of cycle-085 batch-27 LEAD (the all-12-column FEATURE-SURFACE SPINE re-eval under the OWN-COMPOSITION rule; first feature columns ever off terminal seed)."
---

# CYCLE: cycle-085 D1 — driver-leaf cohort re-evaluation (OWN-COMPOSITION rule) + feature/index.md sole-owner

## Summary

The batch-26 meta-phase enacted the USER DIRECTIVE `feature-column-promotion-break-the-seed-deadlock`: a feature column promotes off `seed` when its **OWN composition + directly-owned constituents** are firm; **cross-linked SIBLING columns are references, NOT blocking constituents** (superseding the earlier "promote only once ALL composed constituents — incl. the cross-linked sibling column — are firm" rule that made `seed` a permanent terminal state). This is D1 of the all-13-column re-evaluation: the **6 driver-leaf columns** (eigenmode, driven, transient, electrostatic, magnetostatic, boundary-mode) × 3 levels {L4, L1, L0}, plus sole-ownership of the shared `feature/index.md` narrative.

**Verdict (on-disk-confirmed below):**
- **FLIP `seed → firm`:** `eigenmode.{L4,L1,L0}`, `driven.{L4,L1,L0}`, `transient.{L4,L1,L0}` — every directly-composed constituent firm.
- **STAY `seed` (own-constituent gate, NOT a sibling blocker):** `electrostatic.{L4,L1,L0}`, `magnetostatic.{L4,L1,L0}` (directly-composed `solve_family` + `gram_reduce` are `rough-in (test-coverage-bounded)`); `boundary-mode.{L4,L1,L0}` (own stage-(3) readout reduces into a waveguide-mode output product with no firm home — own-readout gate).
- All 18 column files: promotion-rule prose re-authored to the OWN-COMPOSITION rule (deadlock clause dropped).
- `feature/index.md` (D1 sole-owns): cohort-wide rule-prose (`:55`, `:57`) re-authored to the OWN-COMPOSITION rule; §Chapter-kind status (`:59-61`) re-narrated from blanket-`seed` to the post-flip cohort (6 columns `firm` / 6 `seed`). No matrix-cell flip exists (level-link cells only); no SUMMARY status tokens.

This validates the spine-promotion mechanism: the first feature columns leave terminal `seed`.

## On-disk constituent-maturity confirmation (the GROUND TRUTH that determines each verdict)

`## Status` first-line read of each directly-composed L4 constituent (grep of `book/src/L4/<op>.md`, this dispatch):

```
fe_assemble                  -> `firm`  (foldr-producing-a-sum assemble-construction combinator)
eigsolve                     -> `firm`  (Solve-monadic outer-driver cap; opaque eigen-loop the obstruction it caps)
ksp_solve                    -> `firm`  (Solve-monadic outer-driver cap)
assemble_frequency_operator  -> `firm`  (calculus rendering of the firm L1 form)
frequency_sweep              -> `firm`  (firm-on-positive-structure escape)
fold_solve                   -> `firm`  (firm-on-positive-structure escape; apply_nonlinear_pencil precedent)
solve_family                 -> `rough-in (test-coverage-bounded)`   <-- NOT firm
gram_reduce                  -> `rough-in (test-coverage-bounded)`   <-- NOT firm
```

Per-column directly-owned composition (read from each `.L4.md` `composes:` frontmatter):
- **eigenmode**: `fe_assemble`(firm ×3) + `eigsolve`(firm). Stage-(3) reduction owned by the `eigenfrequency-qfactor` SIBLING column (a reference, NOT a constituent). → **ALL firm → FLIP.**
- **driven**: `fe_assemble`(firm) + `assemble_frequency_operator`(firm) + `frequency_sweep`(firm) + `ksp_solve`(firm). → **ALL firm → FLIP.**
- **transient**: `fe_assemble`(firm) + `fold_solve`(firm). → **ALL firm → FLIP.**
- **electrostatic**: `fe_assemble`(firm) + **`solve_family`(rough-in)** + `ksp_solve`(firm) + **`gram_reduce`(rough-in)**. → **STAY seed** (own `solve_family` + own `gram_reduce` rough-in — directly-composed vocab ops, NOT sibling columns).
- **magnetostatic**: identical own-constituent set to electrostatic. → **STAY seed.**
- **boundary-mode**: `fe_assemble`(firm) + `eigsolve`(firm) — solve corner all firm — BUT its own stage-(3) readout reduces into a waveguide-mode output product with **no output-product column / no firm reduction home** (the `boundary-mode.L4:59,79` stated seed-reason). → **STAY seed** (own-readout gate; the waveguide-mode product column is demand-gated).

This matches the planner's verdict table exactly; no on-disk surprise (see Open questions for the one expectation-vs-evidence note the planner already flagged: electrostatic/magnetostatic do NOT flip, overriding priorities.md #1).

---

## Proposed changes

### Column 1 — eigenmode (FLIP seed → firm)

```edit:book/src/feature/eigenmode.L4.md
[old]: status: seed
[new]: status: firm
```

```edit:book/src/feature/eigenmode.L4.md
[old]: The whole feature therefore lowers cleanly outward to the L4 backend surface: `eigenmode = map readout ∘ eigsolve ∘ eig_pencil ∘ (fe_assemble ×3)`. Both composed combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm** — so the only thing keeping this column at `seed` (rather than promoting past it) is the readout stage's reduction into the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column, which is itself `seed`. (Its reduction verb `eigenfreq_qfactor_reduce` is now **firm** — promoted cycle-082; that column stays `seed` not on the verb but on the reciprocal cross-link to *this* driver column, which is itself `seed` — OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column`.) This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary is firm and composes without forcing the spine.
[new]: The whole feature therefore lowers cleanly outward to the L4 backend surface: `eigenmode = map readout ∘ eigsolve ∘ eig_pencil ∘ (fe_assemble ×3)`. Both directly-composed combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm**, so under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers) this column **promotes to `firm`**. The stage-(3) reduction into the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column is a **sibling cross-link** (a reference / drift-guard), not a directly-owned constituent — it does NOT gate this driver column's promotion. (That column itself promotes independently on its own firm reduce verb `eigenfreq_qfactor_reduce`, firm cycle-082; the former mutual-blocking deadlock between the two — each citing the other's `seed` state — is exactly what the directive retires.) This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the directly-owned constituent vocabulary is firm and composes without forcing the spine.
```

```edit:book/src/feature/eigenmode.L4.md
[old]: `seed` — the third per-driver feature-surface composition-root (a **leaf feature column**) authored under the FEATURE-SURFACE SPINE directive (2026-06-02), and the **cleanest test of the composition-root pattern over a single black-box-kernel constituent + assemble** (per the dispatch scope). Both composed combinators are firm: stage (1) is three single-term [`fe_assemble`](../L4/fe_assemble.md) folds (the K/C/M pencil), stage (2) is exactly one [`eigsolve`](../L4/eigsolve.md) black-box call — with NO `solve_family` map and NO `fold_solve` state-march (the explicit non-membership at `book/src/L4/solve_family.md:146`), the load-bearing structural fact that makes this the minimal composition shape. Stage (3) is a pure per-mode readout `map`; its reduction into the user-facing eigenfrequency/Q-factor product is owned by the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column (itself `seed`, though its `eigenfreq_qfactor_reduce` reduction verb is now **firm** — cycle-082) — the one reason this column stays `seed` rather than promoting (the two solve-side constituents being firm). This chapter carries the *compositional* claim (eigenmode = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `eigensolver.cpp:32-477` (`EigenSolver::Solve`) realizing the composition, all anchors confirmed on-disk via palace-codemap `read_range` this dispatch, plus the firm constituent down-links.
[new]: `firm` — the third per-driver feature-surface composition-root (a **leaf feature column**) authored under the FEATURE-SURFACE SPINE directive (2026-06-02), and the **cleanest test of the composition-root pattern over a single black-box-kernel constituent + assemble** (per the dispatch scope). **Promoted `seed → firm` cycle-085** under the OWN-COMPOSITION promotion rule (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm, and cross-linked sibling columns are references, NOT blockers. Both directly-owned constituents are firm: stage (1) is three single-term [`fe_assemble`](../L4/fe_assemble.md) folds (the K/C/M pencil, firm), stage (2) is exactly one [`eigsolve`](../L4/eigsolve.md) black-box call (firm) — with NO `solve_family` map and NO `fold_solve` state-march (the explicit non-membership at `book/src/L4/solve_family.md:146`), the load-bearing structural fact that makes this the minimal composition shape. Stage (3) is a pure per-mode readout `map`; its reduction into the user-facing eigenfrequency/Q-factor product is owned by the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column — a **sibling cross-link (a reference), NOT a directly-owned constituent**, so it does NOT gate this column's promotion (that column promotes independently on its own firm `eigenfreq_qfactor_reduce` verb, firm cycle-082; the former mutual-blocking deadlock between the two columns is exactly what the directive retires). This chapter carries the *compositional* claim (eigenmode = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `eigensolver.cpp:32-477` (`EigenSolver::Solve`) realizing the composition, all anchors confirmed on-disk via palace-codemap `read_range`, plus the firm constituent down-links.
```

```edit:book/src/feature/eigenmode.L1.md
[old]: status: seed
[new]: status: firm
```

```edit:book/src/feature/eigenmode.L1.md
[old]: `seed` — the L1 pure-function composition root for the eigenmode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [eigenmode.L4](./eigenmode.L4.md) minimal composition root. BOTH composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`eigsolve`](../L1/eigsolve.md)); the only non-firm element is the stage-3 readout's forward-ref to the not-yet-authored `eigenfrequency-qfactor` output-product column — which is why the column stays `seed`. The defining structural fact carried from L4: a single opaque eigensolver-as-operator application, with NO RHS family-map and NO value-threaded outer solve loop (the `solve_family`/`fold_solve` non-membership at `book/src/L4/solve_family.md:146`). The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The L1→L0 direction (how each pure operator lowers to the in-place driver writes — the `GetEigenvector(i, E)` destination write, the `B *= ...` accumulations) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline). Evidence: the L0 driver range `eigensolver.cpp:32-477` realizing the composition, plus the firm L1 constituent down-links.
[new]: `firm` — the L1 pure-function composition root for the eigenmode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [eigenmode.L4](./eigenmode.L4.md) minimal composition root. **Promoted `seed → firm` cycle-085** under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers). BOTH directly-composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`eigsolve`](../L1/eigsolve.md)); the stage-3 readout's reduction into the `eigenfrequency-qfactor` output-product column is a **sibling cross-link (a reference)**, NOT a directly-owned constituent, so it does not gate promotion. The defining structural fact carried from L4: a single opaque eigensolver-as-operator application, with NO RHS family-map and NO value-threaded outer solve loop (the `solve_family`/`fold_solve` non-membership at `book/src/L4/solve_family.md:146`). The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The L1→L0 direction (how each pure operator lowers to the in-place driver writes — the `GetEigenvector(i, E)` destination write, the `B *= ...` accumulations) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline). Evidence: the L0 driver range `eigensolver.cpp:32-477` realizing the composition, plus the firm L1 constituent down-links.
```

```edit:book/src/feature/eigenmode.L0.md
[old]: status: seed
[new]: status: firm
```

```edit:book/src/feature/eigenmode.L0.md
[old]: `seed` — the L0 ground-truth surface for the eigenmode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [magnetostatic.L0](./magnetostatic.L0.md) / [electrostatic.L0](./electrostatic.L0.md) exemplars. Every stage is a cited range into `palace/drivers/eigensolver.cpp`, confirmed on-disk via palace-codemap `read_range` this dispatch (the `EigenSolver::Solve` decl `:32-33`, K/C/M assembly `:40-42`, `SetOperators` pencil setup `:172-196`, the single `eigen->Solve()` `:367`, the readout loop `:424-471`). The load-bearing structural fact at L0: a single opaque `eigen->Solve()` with NO surrounding Palace-authored loop and NO per-source RHS family — the driver's only loop is the post-processing eigenpair readout (the `solve_family`/`fold_solve` non-membership recorded at `book/src/L4/solve_family.md:146`). The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
[new]: `firm` — the L0 ground-truth surface for the eigenmode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [magnetostatic.L0](./magnetostatic.L0.md) / [electrostatic.L0](./electrostatic.L0.md) exemplars. **Promoted `seed → firm` cycle-085** with the column (the L0 surface tracks the column maturity under the OWN-COMPOSITION promotion rule; the eigenmode column's directly-owned constituents — `fe_assemble`, `eigsolve` — are firm, and the `eigenfrequency-qfactor` reduction is a sibling cross-link, not a blocker). Every stage is a cited range into `palace/drivers/eigensolver.cpp`, confirmed on-disk via palace-codemap `read_range` (the `EigenSolver::Solve` decl `:32-33`, K/C/M assembly `:40-42`, `SetOperators` pencil setup `:172-196`, the single `eigen->Solve()` `:367`, the readout loop `:424-471`). The load-bearing structural fact at L0: a single opaque `eigen->Solve()` with NO surrounding Palace-authored loop and NO per-source RHS family — the driver's only loop is the post-processing eigenpair readout (the `solve_family`/`fold_solve` non-membership recorded at `book/src/L4/solve_family.md:146`). The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
```

### Column 2 — driven (FLIP seed → firm)

```edit:book/src/feature/driven.L4.md
[old]: status: seed
composes:
[new]: status: firm
composes:
```

```edit:book/src/feature/driven.L4.md
[old]: `seed` — the driven feature-surface composition-root, a **leaf feature column**
(per-driver; stage-2 constituents are vocabulary ops) authored under the
FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the
[electrostatic](./electrostatic.L4.md) / [magnetostatic](./magnetostatic.L4.md)
exemplars but at the operator-VARYING corner. The composition is sound: stage (1) is
three firm [`fe_assemble`](../L4/fe_assemble.md) folds (the fixed basis captured
once); stage (2) is the firm [`frequency_sweep`](../L4/frequency_sweep.md) map
composing the firm per-ω operand verb
[`assemble_frequency_operator`](../L4/assemble_frequency_operator.md) with the firm
per-member [`ksp_solve`](../L4/ksp_solve.md) (the operator-varying corner,
`SetOperators` inside the loop); stage (3) is the driven S-parameter output-product
surface, forward-ref'd to its own column (a fold of per-ω measurements, not authored
here). All three composition-stage L4 combinators are **firm** — the cleanest
operator-varying composition the spine carries — but the column remains uniform
`status: seed` because the stage-3 S-parameter reduction's own output-product column
[`sparameters`](./sparameters.L4.md) is itself `seed` (its [`sparameter_reduce`](../L4/sparameter_reduce.md)
verb is `rough-in`) — a feature column promotes past `seed` only once ALL composed
constituents are firm. This chapter carries the *compositional* claim
(driven = this composition of these constituent pieces), not the constituents' per-op
algebraic claims (those live in the linked chapters). Evidence: the L0 driver range
`drivensolver.cpp:37-75` (`Solve` dispatch) + `:77-229` (`SweepUniform`) realizing
the composition, plus the firm constituent down-links (all line ranges self-verified
on-disk via palace-codemap this dispatch).
[new]: `firm` — the driven feature-surface composition-root, a **leaf feature column**
(per-driver; stage-2 constituents are vocabulary ops) authored under the
FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the
[electrostatic](./electrostatic.L4.md) / [magnetostatic](./magnetostatic.L4.md)
exemplars but at the operator-VARYING corner. **Promoted `seed → firm` cycle-085**
under the OWN-COMPOSITION promotion rule (CLAUDE.md §Extraction-goal FEATURE-SURFACE
SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed`
when its OWN composition + directly-owned constituents are firm; cross-linked sibling
columns are references, NOT blockers. The composition is sound and every
directly-owned constituent is firm: stage (1) is three firm
[`fe_assemble`](../L4/fe_assemble.md) folds (the fixed basis captured once); stage (2)
is the firm [`frequency_sweep`](../L4/frequency_sweep.md) map composing the firm per-ω
operand verb [`assemble_frequency_operator`](../L4/assemble_frequency_operator.md) with
the firm per-member [`ksp_solve`](../L4/ksp_solve.md) (the operator-varying corner,
`SetOperators` inside the loop). All three directly-owned composition-stage L4
combinators are **firm** — the cleanest operator-varying composition the spine
carries. Stage (3), the S-parameter reduction, is presented as the dedicated
output-product feature column [`sparameters`](./sparameters.L4.md): that is a
**sibling cross-link (a reference / drift-guard), NOT a directly-owned constituent**,
so it does NOT gate this driver column's promotion (the `sparameters` column itself
promotes independently on its own firm reduce verb
[`sparameter_reduce`](../L4/sparameter_reduce.md), firm cycle-083). This chapter
carries the *compositional* claim (driven = this composition of these constituent
pieces), not the constituents' per-op algebraic claims (those live in the linked
chapters). Evidence: the L0 driver range `drivensolver.cpp:37-75` (`Solve` dispatch) +
`:77-229` (`SweepUniform`) realizing the composition, plus the firm constituent
down-links (all line ranges self-verified on-disk via palace-codemap).
```

```edit:book/src/feature/driven.L1.md
[old]: status: seed
composes:
[new]: status: firm
composes:
```

```edit:book/src/feature/driven.L1.md
[old]: `seed` — the L1 pure-function composition root for the driven feature, a **leaf
feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02),
mirroring the [electrostatic.L1](./electrostatic.L1.md) /
[magnetostatic.L1](./magnetostatic.L1.md) exemplars but at the operator-VARYING
corner. All three composed L1 operators are firm
([`fe_assemble`](../L1/fe_assemble.md),
[`assemble_frequency_operator`](../L1/assemble_frequency_operator.md),
[`ksp_solve`](../L1/ksp_solve.md)) — the driven L1 vocabulary is fully firm, unlike
the fixed-operator columns whose stage-3 inductance/capacitance bilinear-form
primitives are rough-in. The column remains uniform `status: seed` because the
stage-3 S-parameter reduction is the driven output-product surface, forward-ref'd to
its own column (not yet authored as a firm constituent). The chapter carries the
compositional claim only; per-op algebraic claims live in the linked chapters.
Evidence: the L0 driver range `drivensolver.cpp:77-229` (`SweepUniform`) realizing
the composition, plus the firm L1 constituent down-links (line ranges self-verified
on-disk this dispatch).
[new]: `firm` — the L1 pure-function composition root for the driven feature, a **leaf
feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02),
mirroring the [electrostatic.L1](./electrostatic.L1.md) /
[magnetostatic.L1](./magnetostatic.L1.md) exemplars but at the operator-VARYING
corner. **Promoted `seed → firm` cycle-085** under the OWN-COMPOSITION promotion rule
(a column promotes off `seed` when its OWN composition + directly-owned constituents
are firm; cross-linked sibling columns are references, NOT blockers). All three
directly-composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md),
[`assemble_frequency_operator`](../L1/assemble_frequency_operator.md),
[`ksp_solve`](../L1/ksp_solve.md)) — the driven L1 vocabulary is fully firm, unlike
the fixed-operator columns whose stage-3 inductance/capacitance bilinear-form
primitives are rough-in. The stage-3 S-parameter reduction is the driven
output-product surface, presented as its own [`sparameters`](./sparameters.L1.md)
column — a **sibling cross-link (a reference)**, NOT a directly-owned constituent, so
it does not gate promotion (the `sparameters` column promotes independently on its own
firm reduce verb). The chapter carries the compositional claim only; per-op algebraic
claims live in the linked chapters. Evidence: the L0 driver range
`drivensolver.cpp:77-229` (`SweepUniform`) realizing the composition, plus the firm L1
constituent down-links (line ranges self-verified on-disk).
```

```edit:book/src/feature/driven.L0.md
[old]: status: seed
[new]: status: firm
```

```edit:book/src/feature/driven.L0.md
[old]: `seed` — the L0 ground-truth surface for the driven feature, a **leaf feature
column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring
the [electrostatic.L0](./electrostatic.L0.md) / [magnetostatic.L0](./magnetostatic.L0.md)
exemplars but at the operator-VARYING corner (the `SetOperators`-inside-the-loop
witness). Every stage is a cited range into `palace/drivers/drivensolver.cpp`,
confirmed on-disk via palace-codemap `read_range` + direct on-disk `Read` (close-brace
discipline on the loop / function END lines) this dispatch. The chapter's evidence IS
the driver-source range + the per-stage site map to the constituent ops (the adapted
surface-or-evidence form for the feature-surface kind). The S-parameter reduction
(stage 5) is the driven output-product surface, forward-ref'd to its own column.
[new]: `firm` — the L0 ground-truth surface for the driven feature, a **leaf feature
column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring
the [electrostatic.L0](./electrostatic.L0.md) / [magnetostatic.L0](./magnetostatic.L0.md)
exemplars but at the operator-VARYING corner (the `SetOperators`-inside-the-loop
witness). **Promoted `seed → firm` cycle-085** with the column (the L0 surface tracks
the column maturity under the OWN-COMPOSITION promotion rule; the driven column's
directly-owned constituents — `fe_assemble`, `assemble_frequency_operator`,
`frequency_sweep`, `ksp_solve` — are all firm, and the S-parameter reduction is a
sibling cross-link, not a blocker). Every stage is a cited range into
`palace/drivers/drivensolver.cpp`, confirmed on-disk via palace-codemap `read_range` +
direct on-disk `Read` (close-brace discipline on the loop / function END lines). The
chapter's evidence IS the driver-source range + the per-stage site map to the
constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
The S-parameter reduction (stage 5) is the driven output-product surface, presented as
its own [`sparameters`](./sparameters.L0.md) column (a sibling cross-link).
```

### Column 3 — transient (FLIP seed → firm)

```edit:book/src/feature/transient.L4.md
[old]: status: seed
[new]: status: firm
```

```edit:book/src/feature/transient.L4.md
[old]: `seed` — the **leaf feature column** (per-driver sub-kind) for the transient pipeline, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the spine's first **fold-pipeline** witness (sibling of the [electrostatic](./electrostatic.L4.md) / [magnetostatic](./magnetostatic.L4.md) map-pipeline columns). The composition is sound and rests on **firm** constituents end-to-end: stage (1) composes the firm [`fe_assemble`](../L4/fe_assemble.md) (three operators, K/C/M), stage (2) composes the firm [`fold_solve`](../L4/fold_solve.md) (transient is its default/primary witness). The column nonetheless stays `seed` (the uniform feature-surface token; the prose names the leaf-driver sub-kind) — promotion past `seed` is reserved for the eigenmode-column clean test per the directive, and the per-step body remains an opaque-library integrator step quantified over rather than rendered. This chapter carries the *compositional* claim (transient = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `transientsolver.cpp:24-116` (`Solve`) + the K/C/M assembly and ODE-step sites in `timeoperator.cpp` realizing the composition, plus the firm constituent down-links. All L0 line ranges self-verified on-disk via palace-codemap `read_range` this dispatch (close-brace discipline applied: `Solve` ends `:116`, the loop spans `:77-109`).
[new]: `firm` — the **leaf feature column** (per-driver sub-kind) for the transient pipeline, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the spine's first **fold-pipeline** witness (sibling of the [electrostatic](./electrostatic.L4.md) / [magnetostatic](./magnetostatic.L4.md) map-pipeline columns). **Promoted `seed → firm` cycle-085** under the OWN-COMPOSITION promotion rule (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. The composition is sound and rests on **firm** directly-owned constituents end-to-end: stage (1) composes the firm [`fe_assemble`](../L4/fe_assemble.md) (three operators, K/C/M), stage (2) composes the firm [`fold_solve`](../L4/fold_solve.md) (transient is its default/primary witness). Transient owns no separate output-product sibling column (its product is the field trajectory itself, materialized in-column), so the column has no cross-link blocker; both directly-owned constituents being firm is the full promotion warrant. The per-step body remains an opaque-library integrator step quantified over rather than rendered — an obstruction the firm `fold_solve` combinator absorbs (it quantifies over the opaque step), recorded at the lowering layer, NOT a composition-level gate. This chapter carries the *compositional* claim (transient = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `transientsolver.cpp:24-116` (`Solve`) + the K/C/M assembly and ODE-step sites in `timeoperator.cpp` realizing the composition, plus the firm constituent down-links. All L0 line ranges self-verified on-disk via palace-codemap `read_range` (close-brace discipline applied: `Solve` ends `:116`, the loop spans `:77-109`).
```

```edit:book/src/feature/transient.L1.md
[old]: status: seed
[new]: status: firm
```

```edit:book/src/feature/transient.L1.md
[old]: `seed` — the L1 pure-function composition root for the transient feature, the spine's first **fold-pipeline** witness, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic.L1](./electrostatic.L1.md) / [magnetostatic.L1](./magnetostatic.L1.md) exemplars but composing a *fold* rather than a *map*. The assemble constituent is firm ([`fe_assemble`](../L1/fe_assemble.md), three operators); the march composes the firm [`fold_solve`](../L4/fold_solve.md) combinator (transient is its default/primary witness), rendered at L1 as a pure `scanl_state` over a mutation-lifted per-step advance whose body bottoms out in an opaque-library integrator step (quantified over, not rendered). The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 driver range `transientsolver.cpp:24-116` + the K/C/M assembly and ODE-step sites in `timeoperator.cpp` realizing the composition, plus the firm L1/L4 constituent down-links. All L0 line ranges self-verified on-disk via palace-codemap `read_range` this dispatch.
[new]: `firm` — the L1 pure-function composition root for the transient feature, the spine's first **fold-pipeline** witness, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic.L1](./electrostatic.L1.md) / [magnetostatic.L1](./magnetostatic.L1.md) exemplars but composing a *fold* rather than a *map*. **Promoted `seed → firm` cycle-085** under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers). Both directly-owned constituents are firm: the assemble constituent ([`fe_assemble`](../L1/fe_assemble.md), three operators) and the march constituent (the firm [`fold_solve`](../L4/fold_solve.md) combinator, transient is its default/primary witness, rendered at L1 as a pure `scanl_state` over a mutation-lifted per-step advance whose body bottoms out in an opaque-library integrator step — quantified over, not rendered). Transient owns no output-product sibling column (its product is the trajectory itself), so there is no cross-link blocker. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 driver range `transientsolver.cpp:24-116` + the K/C/M assembly and ODE-step sites in `timeoperator.cpp` realizing the composition, plus the firm L1/L4 constituent down-links. All L0 line ranges self-verified on-disk via palace-codemap `read_range`.
```

```edit:book/src/feature/transient.L0.md
[old]: status: seed
[new]: status: firm
```

```edit:book/src/feature/transient.L0.md
[old]: `seed` — the L0 ground-truth surface for the transient feature (the spine's first **fold-pipeline** witness), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic.L0](./electrostatic.L0.md) / [magnetostatic.L0](./magnetostatic.L0.md) exemplars. Every stage is a cited range into `palace/drivers/transientsolver.cpp` + `palace/models/timeoperator.cpp`, confirmed on-disk via palace-codemap `read_range` this dispatch (close-brace discipline: `Solve` spans `:24-116`, the loop `:77-109`, the `Step` method `:407-413`). The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
[new]: `firm` — the L0 ground-truth surface for the transient feature (the spine's first **fold-pipeline** witness), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic.L0](./electrostatic.L0.md) / [magnetostatic.L0](./magnetostatic.L0.md) exemplars. **Promoted `seed → firm` cycle-085** with the column (the L0 surface tracks the column maturity under the OWN-COMPOSITION promotion rule; the transient column's directly-owned constituents — `fe_assemble`, `fold_solve` — are firm, and it owns no output-product sibling cross-link). Every stage is a cited range into `palace/drivers/transientsolver.cpp` + `palace/models/timeoperator.cpp`, confirmed on-disk via palace-codemap `read_range` (close-brace discipline: `Solve` spans `:24-116`, the loop `:77-109`, the `Step` method `:407-413`). The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
```

### Column 4 — electrostatic (STAY seed; re-author to OWN-composition own-constituent gate)

```edit:book/src/feature/electrostatic.L4.md
[old]: The whole feature therefore lowers cleanly outward to the L4 backend surface: `electrostatic = capacitance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of firm combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary is firm and composes without forcing the spine.
[new]: The whole feature therefore lowers cleanly outward to the L4 backend surface: `electrostatic = capacitance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: the composition is clean, but under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers) the column stays `seed` because two of its **directly-owned** constituents — the [`solve_family`](../L4/solve_family.md) per-terminal map and the [`gram_reduce`](../L4/gram_reduce.md) capacitance reduction — are `rough-in (test-coverage-bounded)`. This is a genuine own-constituent gate (these are directly-composed vocabulary ops, NOT sibling columns); firming `solve_family` + `gram_reduce` is the promotion route.
```

```edit:book/src/feature/electrostatic.L4.md
[old]: `seed` — the first feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stages (1) and (2) compose firm/rough-in L4 combinators; stage (3) is the rough-in-track L4 [`gram_reduce`](../L4/gram_reduce.md) reduction (the `w = 1` voltage specialization), which folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) building blocks over the family-pair grid — `gram_reduce` is rough-in (test-coverage-bounded) precisely because those folded constituents are; not a blocker, the reduction composes cleanly as a fold of evaluations. This chapter carries the *compositional* claim (electrostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `electrostaticsolver.cpp:21-98` (`Solve`) + `:100-138` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
[new]: `seed` — the first feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. This column **stays `seed`** — not on a sibling-column blocker, but on a genuine **own-constituent gate**: two of its directly-composed L4 constituents are not yet firm — the [`solve_family`](../L4/solve_family.md) per-terminal solve map (`rough-in (test-coverage-bounded)`) and the [`gram_reduce`](../L4/gram_reduce.md) `w = 1` voltage-specialization capacitance reduction (`rough-in (test-coverage-bounded)`, which folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) over the family-pair grid). The composition is sound (stage (1) the firm [`fe_assemble`](../L4/fe_assemble.md), the reduction a clean fold of evaluations), but two directly-owned constituents being rough-in is the own-constituent gate; firming `solve_family` + `gram_reduce` is the promotion route (NOTE: this overrides the priorities.md #1 expectation that electrostatic flips this cycle — the on-disk constituent evidence governs). This chapter carries the *compositional* claim (electrostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `electrostaticsolver.cpp:21-98` (`Solve`) + `:100-138` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
```

*(No electrostatic.L1 / electrostatic.L0 edits: those §Status blocks carry no deadlock-clause prose and no promotion claim — a bare `seed` + provenance line — so there is nothing to re-author; they correctly stay `seed`. The substantive electrostatic re-authoring is the two `.L4.md` blocks above.)*

### Column 5 — magnetostatic (STAY seed; re-author to OWN-composition own-constituent gate)

```edit:book/src/feature/magnetostatic.L4.md
[old]: The whole feature therefore lowers cleanly outward to the L4 backend surface: `magnetostatic = inductance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of firm combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary is firm and composes without forcing the spine.
[new]: The whole feature therefore lowers cleanly outward to the L4 backend surface: `magnetostatic = inductance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: the composition is clean, but under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers) the column stays `seed` because two of its **directly-owned** constituents — the [`solve_family`](../L4/solve_family.md) per-source map and the [`gram_reduce`](../L4/gram_reduce.md) inductance reduction — are `rough-in (test-coverage-bounded)`. This is a genuine own-constituent gate (directly-composed vocabulary ops, NOT sibling columns); firming `solve_family` + `gram_reduce` is the promotion route.
```

```edit:book/src/feature/magnetostatic.L4.md
[old]: `seed` — the second feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic](./electrostatic.L4.md) exemplar. The composition is sound: stages (1) and (2) compose firm/rough-in L4 combinators (the second witness of the fixed-operator `solve_family` corner); stage (3) is the rough-in-track L4 [`gram_reduce`](../L4/gram_reduce.md) reduction (the `w = 1/(IᵢIⱼ)` current-normalized specialization — the same shared symmetric-Gram reduction as the electrostatic capacitance, the weight the only difference), which folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) building blocks over the family-pair grid — `gram_reduce` is rough-in (test-coverage-bounded) precisely because those folded constituents are; not a blocker, the reduction composes cleanly as a fold of evaluations. This chapter carries the *compositional* claim (magnetostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `magnetostaticsolver.cpp:22-108` (`Solve`) + `:110-204` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
[new]: `seed` — the second feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic](./electrostatic.L4.md) exemplar. **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. This column **stays `seed`** — not on a sibling-column blocker, but on a genuine **own-constituent gate** identical to electrostatic's: two of its directly-composed L4 constituents are not yet firm — the [`solve_family`](../L4/solve_family.md) per-source solve map (`rough-in (test-coverage-bounded)`, the second witness of the fixed-operator corner) and the [`gram_reduce`](../L4/gram_reduce.md) `w = 1/(IᵢIⱼ)` current-normalized inductance reduction (`rough-in (test-coverage-bounded)` — the same shared symmetric-Gram reduction as the electrostatic capacitance, the weight the only difference; it folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) over the family-pair grid). The composition is sound (stage (1) the firm [`fe_assemble`](../L4/fe_assemble.md), the reduction a clean fold of evaluations), but two directly-owned constituents being rough-in is the own-constituent gate; firming `solve_family` + `gram_reduce` is the promotion route (overriding the priorities.md #1 expectation that magnetostatic flips this cycle — the on-disk constituent evidence governs). This chapter carries the *compositional* claim (magnetostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `magnetostaticsolver.cpp:22-108` (`Solve`) + `:110-204` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
```

### Column 6 — boundary-mode (STAY seed; re-author to OWN-composition own-readout gate)

```edit:book/src/feature/boundary-mode.L4.md
[old]: Both composed combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm**. As with eigenmode, the solve-side constituents being firm means the only thing keeping this column at `seed` is the readout stage's reduction into the user-facing waveguide-mode product (whose dedicated output-product reduction is not yet a feature column).
[new]: Both composed solve-side combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm**. Under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers), the firm solve corner is not sufficient here: this column stays `seed` on its **own-readout gate** — its directly-owned stage-(3) readout reduces into a user-facing **waveguide-mode output product that has no firm home** (no dedicated output-product column / no firm reduction verb exists yet; the waveguide-mode product column is demand-gated). The gate is a directly-owned constituent (the column's own readout reduction), NOT a sibling-column reference; authoring a firm waveguide-mode reduction is the promotion route.
```

```edit:book/src/feature/boundary-mode.L4.md
[old]: `seed` — the **6th per-driver feature-surface composition-root** (a **leaf feature column**) authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the alpha-first column in the driver-leaf grouping, and the **second clean witness of the composition-root pattern over a single opaque-library black-box eigen-iteration** (the SAME [`eigsolve`](../L4/eigsolve.md) corner as [`eigenmode`](./eigenmode.L4.md), distinguished by the 2D-submesh extraction preface). Both composed combinators are firm: stage (1) is the [`fe_assemble`](../L4/fe_assemble.md) GEP block-pencil assemble, stage (2) is exactly one [`eigsolve`](../L4/eigsolve.md) black-box call — with NO `solve_family` map and NO `fold_solve` state-march (the minimal solve shape eigenmode established). Stage (0) is the distinguishing 2D-submesh preface; stage (3) is a pure per-mode readout `map` whose reduction into the user-facing waveguide-mode product is a forward-ref (no dedicated output-product column yet) — the one reason this column stays `seed`. This chapter carries the *compositional* claim (boundary-mode = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). The `BoundaryModeSolver` is a 6th `ProblemType` dispatch branch that routes through the same `switch` as the 5 drivers (`palace/main.cpp:276-278`), so it is a co-equal leaf driver column. Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` (`BoundaryModeSolver::Solve`) realizing the composition, all anchors confirmed on-disk this dispatch, plus the firm constituent down-links.
[new]: `seed` — the **6th per-driver feature-surface composition-root** (a **leaf feature column**) authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the alpha-first column in the driver-leaf grouping, and the **second clean witness of the composition-root pattern over a single opaque-library black-box eigen-iteration** (the SAME [`eigsolve`](../L4/eigsolve.md) corner as [`eigenmode`](./eigenmode.L4.md), distinguished by the 2D-submesh extraction preface). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. The solve corner is firm — stage (1) is the [`fe_assemble`](../L4/fe_assemble.md) GEP block-pencil assemble, stage (2) is exactly one [`eigsolve`](../L4/eigsolve.md) black-box call (with NO `solve_family` map and NO `fold_solve` state-march, the minimal solve shape eigenmode established), stage (0) is the distinguishing 2D-submesh preface — but this column **stays `seed`** on an **own-readout gate**: its directly-owned stage-(3) readout (a pure per-mode `map`) reduces into a user-facing **waveguide-mode output product that has no firm home** (no dedicated output-product column / no firm reduction verb exists yet; the waveguide-mode product column is demand-gated). This is a directly-owned constituent gate (the column's own readout reduction), NOT a sibling-column reference — so unlike its eigenmode sibling (which promotes because its reduction is owned by a *separate* `eigenfrequency-qfactor` cross-linked column), boundary-mode's readout reduction is its own unhomed constituent; authoring a firm waveguide-mode reduction is the promotion route. This chapter carries the *compositional* claim (boundary-mode = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). The `BoundaryModeSolver` is a 6th `ProblemType` dispatch branch that routes through the same `switch` as the 5 drivers (`palace/main.cpp:276-278`), so it is a co-equal leaf driver column. Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` (`BoundaryModeSolver::Solve`) realizing the composition, all anchors confirmed on-disk, plus the firm constituent down-links.
```

```edit:book/src/feature/boundary-mode.L1.md
[old]: BOTH composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`eigsolve`](../L1/eigsolve.md)); the only non-firm element is the stage-3 readout's forward-ref to a not-yet-authored waveguide-mode output-product reduction — which is why the column stays `seed`.
[new]: **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers): BOTH composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`eigsolve`](../L1/eigsolve.md)), but the column **stays `seed`** on an **own-readout gate** — its directly-owned stage-3 readout reduces into a not-yet-authored waveguide-mode output-product reduction (no firm home; the waveguide-mode product column is demand-gated). The gate is the column's own readout constituent, NOT a sibling-column reference — so authoring a firm waveguide-mode reduction is the promotion route.
```

```edit:book/src/feature/boundary-mode.L0.md
[old]: `seed` — the L0 ground-truth surface for the boundary-mode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the 6th driver-leaf column and the L0 sibling of the [eigenmode.L0](./eigenmode.L0.md) driver (the SAME opaque-library black-box eigen-iteration corner, distinguished by the 2D-submesh extraction preface).
[new]: `seed` — the L0 ground-truth surface for the boundary-mode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the 6th driver-leaf column and the L0 sibling of the [eigenmode.L0](./eigenmode.L0.md) driver (the SAME opaque-library black-box eigen-iteration corner, distinguished by the 2D-submesh extraction preface). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers): the solve corner is firm (`fe_assemble`, `eigsolve`), but the column stays `seed` on an own-readout gate — its directly-owned readout reduces into a waveguide-mode output product with no firm home yet (the waveguide-mode product column is demand-gated; unlike eigenmode, this driver's reduction is its OWN unhomed constituent, not a separate cross-linked output-product column).
```

### feature/index.md (D1 SOLE-OWNS — cohort-wide rule-prose + §Chapter-kind status)

```edit:book/src/feature/index.md
[old]: All five output-product columns stay `seed` (not promotable) because each composed reduction verb is itself `rough-in` (a feature column promotes past `seed` only once ALL its composed constituents are firm).
[new]: Under the OWN-COMPOSITION promotion rule (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; user directive 2026-06-03; memory `project_feature_column_promotion_rule`), a feature column promotes off `seed` when its **OWN composition + directly-owned constituents** are firm; **cross-linked sibling columns are references, NOT blockers**. Two output-product columns whose own reduce verb is firm therefore promote — [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) (own verb `eigenfreq_qfactor_reduce`, firm c082) and [`sparameters`](./sparameters.L4.md) (own verb `sparameter_reduce`, firm c083) — independent of their producing driver cross-links. The remaining three output-product columns stay `seed` on a genuine **own-constituent gate**: their composed reduce verbs ([`gram_reduce`](../L4/gram_reduce.md) for capacitance/inductance; `domain_energy_reduce` + the folded [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) for energy-fields) are themselves `rough-in`. (This supersedes the earlier "promote only once ALL composed constituents — including cross-linked sibling columns — are firm" rule, which combined with the output-product↔driver reciprocal cross-link to make `seed` a permanent terminal state — the mutual-blocking deadlock the directive breaks.)
```

```edit:book/src/feature/index.md
[old]: The FEATURE-SURFACE SPINE directive scope is now fully authored: cycle-078 lands the last output product ([`energy-fields`](./energy-fields.L4.md), the per-domain energy table) and the 6th-`ProblemType` wave-port / [`boundary-mode`](./boundary-mode.L4.md) driver column (a co-equal leaf driver column under the lifecycle ROOT). Every column lands `seed` and promotes only when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
[new]: The FEATURE-SURFACE SPINE directive scope is fully authored (cycle-078 landed the last output product [`energy-fields`](./energy-fields.L4.md) and the 6th-`ProblemType` wave-port / [`boundary-mode`](./boundary-mode.L4.md) driver column, a co-equal leaf driver column under the lifecycle ROOT), and cycle-085 ran the all-13-column re-evaluation under the OWN-COMPOSITION promotion rule: a column promotes off `seed` when its OWN composition + directly-owned constituents are firm (cross-linked sibling columns being references, not blockers). A column that cannot yet be cleanly composed — i.e. one of its directly-owned constituents is still rough-in or unhomed — stays `seed` as a *finding about the spine* (surfaced as an open question, the same low-priority test-load discipline the solvers carry on the vocabulary spine).
```

```edit:book/src/feature/index.md
[old]: ## Chapter-kind status

`seed` — the electrostatic column is the first exemplar of the feature-surface kind, authored under the FEATURE-SURFACE SPINE user directive (2026-06-02) ahead of role-spec codification; the magnetostatic + lifecycle columns (cycle-072) are the second-wave instances confirming the kind scales (the batch-22 meta-phase codifies the kind into the role-specs + groups it under the forthcoming directive-3 by-kind grouping). The critic's surface-or-evidence check is adapted for this kind: a feature chapter's evidence is the L0 driver-source range + the constituent-op down-links, not a single decomposed op's source site; the rotation-quality + variant-axis-coverage checks no-op (a composition root introduces no new rotation or variant axis — it composes existing firm vocabulary).
[new]: ## Chapter-kind status

The feature-surface kind was established by the electrostatic column (the first exemplar, authored under the FEATURE-SURFACE SPINE user directive 2026-06-02 ahead of role-spec codification) and confirmed to scale by the magnetostatic + lifecycle second-wave columns (cycle-072; batch-22 meta-phase codified the kind into the role-specs + the directive-3 by-kind grouping). **Cycle-085 re-evaluated all 13 columns under the OWN-COMPOSITION promotion rule** (memory `project_feature_column_promotion_rule`); the cohort is no longer blanket-`seed`:

- **`firm` (6 columns)** — own composition + directly-owned constituents all firm; cross-linked sibling columns are references, not blockers:
  - driver-leaf: [`eigenmode`](./eigenmode.L4.md) (own `fe_assemble`×3 + `eigsolve` firm; `eigenfrequency-qfactor` is a sibling cross-link), [`driven`](./driven.L4.md) (own `fe_assemble` + `assemble_frequency_operator` + `frequency_sweep` + `ksp_solve` firm; `sparameters` is a sibling cross-link), [`transient`](./transient.L4.md) (own `fe_assemble` + `fold_solve` firm; no output-product sibling).
  - output-product: [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) (own verb `eigenfreq_qfactor_reduce` firm c082; `eigenmode` is a sibling cross-link), [`sparameters`](./sparameters.L4.md) (own verb `sparameter_reduce` firm c083; `driven` is a sibling cross-link).
  - spine-ROOT: [`lifecycle`](./lifecycle.L4.md) (own driver-agnostic composition — mesh-build + the firm `fold_solve` adaptive fold — firm; the per-driver dispatch is over sibling feature columns, references not blockers).
- **`seed` (6 columns)** — held on a genuine **own-constituent gate** (a directly-owned constituent is rough-in or unhomed), NOT a sibling-column blocker:
  - [`electrostatic`](./electrostatic.L4.md) + [`magnetostatic`](./magnetostatic.L4.md) — own `solve_family` + own `gram_reduce` are `rough-in (test-coverage-bounded)`.
  - [`capacitance`](./capacitance.L4.md) + [`inductance`](./inductance.L4.md) — own reduce verb `gram_reduce` is `rough-in`.
  - [`energy-fields`](./energy-fields.L4.md) — own reduce verb `domain_energy_reduce` + own folded `matrix-weighted-norm` are `rough-in`.
  - [`boundary-mode`](./boundary-mode.L4.md) — own stage-(3) readout reduces into a waveguide-mode output product with no firm home (own-readout gate; the waveguide-mode product column is demand-gated).

The critic's surface-or-evidence check is adapted for this kind: a feature chapter's evidence is the L0 driver-source range + the constituent-op down-links, not a single decomposed op's source site; the rotation-quality + variant-axis-coverage checks no-op (a composition root introduces no new rotation or variant axis — it composes existing firm vocabulary).
```

## Supporting evidence

- **Driver-leaf columns surveyed (on-disk `## Status` + `composes:` frontmatter, this dispatch):** all 6 columns × 3 levels read in full; the 18 `status:` frontmatter values all read `seed` pre-flip (matching the planner's grep).
- **Constituent maturity (on-disk `## Status` first-line, `book/src/L4/<op>.md`):** `fe_assemble`/`eigsolve`/`ksp_solve`/`assemble_frequency_operator`/`frequency_sweep`/`fold_solve` all `firm`; `solve_family`/`gram_reduce` both `rough-in (test-coverage-bounded)`. See the confirmation block above.
- **Index narrative cross-cohort outcomes (named from the planner's canonical verdict table, deterministic):** the §Chapter-kind status names eigenfrequency-qfactor + sparameters (D2's flips) and lifecycle (D3's flip) in the `firm` set; capacitance/inductance/energy-fields in the `seed` set. D1 sole-owns the index; D2/D3 touch only their column files.
- **No matrix-cell flip / no SUMMARY status write:** the `feature/index.md` matrix (`:28-44`) carries only level-link cells (no per-column status cell); `SUMMARY.md` §Feature surfaces carries titles + links only (no status tokens). "Flip the matrix cell" reduces to the §Chapter-kind narrative re-authoring above.
- **Citations:** this is a status + prose re-authoring; no new source claims. All existing `(file:lines)` citations in the touched columns are preserved verbatim (the edits target only the promotion-rule prose + §Status blocks, never the cited line ranges).
- **Within-column high→low ordering preserved** across all touched files (L4 → L1 → L0); no reordering.

## Open questions / caveats

- **electrostatic/magnetostatic STAY-seed scope is L4-only (by design).** The ONLY electrostatic/magnetostatic prose changes are the two `.L4.md` blocks (Columns 4 + 5). The electrostatic.L1, electrostatic.L0, magnetostatic.L1, magnetostatic.L0 files carry NO deadlock-clause prose and NO promotion claim in their §Status blocks (a bare `seed` + authoring-provenance line; they never asserted the old "until ALL constituents firm" rule), so there is nothing to re-author there and they correctly stay `seed`. The L4 §Status is the column-level promotion-rule home for these two; the L1/L0 surfaces inherit the `seed` without restating the rule. (Recorded so the critic does not read the absence of an L1/L0 edit as a missed re-authoring.)
- **priorities.md #1 expectation overridden (already flagged by the planner).** The active-head expected electrostatic + magnetostatic to flip; the on-disk evidence shows their directly-composed `solve_family` + `gram_reduce` are `rough-in (test-coverage-bounded)`, so under the OWN-COMPOSITION rule they correctly STAY seed. The realized driver-leaf flip set is {eigenmode, driven, transient}; the full cohort flip set (with D2/D3) is {eigenmode, driven, transient, eigenfrequency-qfactor, sparameters, lifecycle}. This is consistent with the directive (own-composition gate), just narrower than the active-head prose anticipated. Flag stands for the batch-27 meta-phase.
- **Convergent future-promotion gate for the 4 held columns.** Firming `solve_family` (its §Status names a list-homomorphism law-confidence pass — analogous to the c082/c083 reduce-verb firm-on-positive-structure promotions — as the likely route) would unblock electrostatic + magnetostatic; firming `gram_reduce` (gated on `matrix-weighted-norm` + `bilinear-form`, the NO-GO-HELD cascade) would unblock capacitance + inductance. Not dispatched this cycle (per the planner); recorded here as the convergent gate.
- **Target promoted token = `firm`** (per the planner's note; the role-spec does not literally name a feature-column post-`seed` token, and `firm` is the natural value for a composition-root over all-firm directly-owned constituents). If the batch-27 meta-phase prefers a feature-specific token (`composed` / `promoted`), it can re-token uniformly; this cycle uses `firm`.
- **`boundary-mode` own-readout-gate finding (record-style OQ).** Boundary-mode's stage-(3) readout reduces into a waveguide-mode product that has no output-product column. Whether to author a `waveguide-mode` output-product column (which would promote boundary-mode's readout from an own unhomed constituent to a sibling cross-link, flipping the column to `firm` under the same OWN-COMPOSITION rule) is a demand-gated forward-frontier candidate — flagged for the batch-27 meta-phase / cycle-planner ranking. OQ slug suggestion: `waveguide-mode-output-product-column-would-promote-boundary-mode`.
