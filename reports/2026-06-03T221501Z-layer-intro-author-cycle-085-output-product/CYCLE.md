---
agent: layer-intro-author
invoked_at: 2026-06-03T221501Z
scope: cycle-085 D2 — FEATURE-SURFACE output-product cohort re-evaluation under the OWN-COMPOSITION column-promotion rule
status: integrated
integrated_at: 2026-06-03T225500Z
integration_commit: 7e5ab2d
integration_notes: "Applied clean as D2 (staging row 2, byte-disjoint; does NOT touch feature/index.md — D1 sole-owns). 6 output-product frontmatter flips seed→firm (eigenfrequency-qfactor + sparameters × 3 levels) + sibling-relabel dep-map rows + mutual-blocking deadlock-clause retirement; capacitance/inductance/energy-fields STAY seed (own reduce-verb gate prose: gram_reduce rough-in / domain_energy_reduce + matrix-weighted-norm rough-in); the 3 STAY-seed .L0 files deliberately untouched. Retroactive-budget 0. Build exit 0. 1 OQ promoted (output-product-stay-seed-columns-gated-on-reduce-verb-firming); deduped feature-column-firm-token-choice OQ (promoted by D1). Part of cycle-085 batch-27 LEAD."
---

# CYCLE: feature output-product cohort re-evaluation (OWN-COMPOSITION rule)

## Summary

D2 of the cycle-085 batch-27 LEAD: re-evaluate the 5 output-product FEATURE-SURFACE SPINE columns (eigenfrequency-qfactor, sparameters, capacitance, inductance, energy-fields × {L4,L1,L0}) under the **OWN-COMPOSITION column-promotion rule** (USER DIRECTIVE 2026-06-03; CLAUDE.md §Extraction-goal; memory `project_feature_column_promotion_rule`). A column promotes off `seed` when its **OWN composition + directly-owned constituents** are firm; **cross-linked SIBLING columns (the producing driver column) are references, NOT blockers**. This breaks the mutual-blocking deadlock that made `seed` a permanent terminal state.

**Verdict (on-disk-confirmed, this dispatch):**
- **FLIP `seed → firm`:** `eigenfrequency-qfactor.{L4,L1,L0}` (own reduce verb `eigenfreq_qfactor_reduce` is `firm`, c082) and `sparameters.{L4,L1,L0}` (own reduce verb `sparameter_reduce` is `firm`, c083). For both, the producing driver column (`eigenmode` / `driven`) is a SIBLING reference, NOT a blocking constituent.
- **KEEP `seed`** (own reduce verb still rough-in): `capacitance.{L4,L1,L0}` + `inductance.{L4,L1,L0}` (own verb `gram_reduce` = `rough-in (test-coverage-bounded)`); `energy-fields.{L4,L1,L0}` (own verb `domain_energy_reduce` = `rough-in` + own folded `matrix-weighted-norm` = `rough-in (test-coverage-bounded)`). For these, the §Status / promotion-rule prose is re-authored to drop the deadlock "ALL composed constituents incl. the cross-linked driver column" clause and replace it with the OWN-COMPOSITION reason (the column's OWN reduce verb is not yet firm).

D2 does **NOT** touch `book/src/feature/index.md` (D1 sole-owns it per the single-index-owner discipline). Within-column high→low (L4→L1→L0) ordering preserved. No new claims requiring fresh citations — status + prose re-authoring only.

## On-disk verb-status confirmation (paste-inline evidence)

`grep -n "^## Status" + sed` on each output-product column's directly-owned reduce verb / folded form (the GROUND TRUTH that determines each verdict):

```
book/src/L4/eigenfreq_qfactor_reduce.md:183  ## Status
  "`firm`. **Reasoning (firm-on-positive-structure / syntactic-identity escape):** ..."   -> firm (c082)

book/src/L4/sparameter_reduce.md:240         ## Status
  "`firm`. **Reasoning (firm-on-positive-structure / syntactic-identity escape):** ..."   -> firm (c083)

book/src/L4/gram_reduce.md:225               ## Status
  "`rough-in (test-coverage-bounded)`. **Reasoning (warrant-first):** ..."                -> rough-in (test-coverage-bounded)

book/src/L4/domain_energy_reduce.md:268      ## Status
  "`rough-in`. **Reasoning (warrant-first):** ..."                                        -> rough-in

book/src/L1/matrix-weighted-norm.md:108      ## Status
  "`rough-in (test-coverage-bounded)` — signature and algebraic laws are well-anchored ..."-> rough-in (test-coverage-bounded)
```

All five match the cycle-085 plan's constituent-maturity verdict table exactly. No on-disk surprise — the two flip-column verbs are firm, the three stay-seed verbs/folded-forms are rough-in. Verdict is deterministic from this evidence + the OWN-COMPOSITION rule.

## Proposed changes

### FLIP 1 — eigenfrequency-qfactor (own verb `eigenfreq_qfactor_reduce` firm c082; the EXACT deadlock the directive breaks)

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: ---
kind: feature-surface
feature: eigenfrequency-qfactor
level: L4
status: seed
[new]: ---
kind: feature-surface
feature: eigenfrequency-qfactor
level: L4
status: firm
```

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: The whole output product therefore lowers cleanly outward to the L4 backend surface: `eigenfrequency_qfactor = eigenfreq_qfactor_reduce (ptype, κ) ∘ eigenmode_eigenpairs` — a one-reduction tail on the eigenmode driver column. The reduction verb [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is now **`firm`** (promoted cycle-082 on the firm-on-positive-structure escape — both folded per-mode primitives firm L1 (`participation_ratio` c077 + `eigenvalue-untransform` c080) and the eigenpair→`(f, Q)` assembly carries no inner-product-axiom content). The column nonetheless STAYS `seed`: a feature column may promote past `seed` only once ALL its composed constituents are firm, and the column's OTHER constituent — the upstream [`eigenmode.L4`](./eigenmode.L4.md) driver column that produces the converged eigenpair family — is itself `status: seed` (not firm). The SOLE remaining column blocker is now the `eigenmode.L4` driver column's own seed→promotion (OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column`); the verb-side gate (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`) is **discharged**.
[new]: The whole output product therefore lowers cleanly outward to the L4 backend surface: `eigenfrequency_qfactor = eigenfreq_qfactor_reduce (ptype, κ) ∘ eigenmode_eigenpairs` — a one-reduction tail on the eigenmode driver column. The reduction verb [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is **`firm`** (promoted cycle-082 on the firm-on-positive-structure escape — both folded per-mode primitives firm L1 (`participation_ratio` c077 + `eigenvalue-untransform` c080) and the eigenpair→`(f, Q)` assembly carries no inner-product-axiom content). The column therefore **promotes off `seed` to `firm`** under the **OWN-COMPOSITION rule** (USER DIRECTIVE 2026-06-03; CLAUDE.md §Extraction-goal): a column promotes when its **OWN composition + directly-owned constituents** are firm, and this column's only directly-owned constituent — the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) reduce verb — is firm. The cross-link to the [`eigenmode.L4`](./eigenmode.L4.md) driver column that produces the converged eigenpair family is a **SIBLING reference (the drift-guard), NOT a blocking constituent** — its own `seed` status does not gate this column. This retires the earlier mutual-blocking deadlock (the prior text held the column at `seed` "because the eigenmode driver column is itself seed" — the exact `eigenmode`↔`eigenfrequency-qfactor` reciprocal deadlock the batch-26 directive breaks, since `eigenmode` was symmetrically held seed for reducing into this column). The verb-side gate (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`) was discharged at c082.
```

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: | producing driver column | [`eigenmode.L4`](./eigenmode.L4.md) (driver feature column) | seed | `eigensolver.cpp:32-477` |
[new]: | producing driver column (sibling reference, not a blocker) | [`eigenmode.L4`](./eigenmode.L4.md) (driver feature column) | seed | `eigensolver.cpp:32-477` |
```

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: `seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the rank-1 per-mode-table sibling of the rank-2 Gram output products [capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md). The composition is sound: stage (1) consumes the [`eigenmode.L4`](./eigenmode.L4.md) driver column's converged eigenpair family; stage (2) composes the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode scalar-ratio reduction at the problem-type un-transform + resistive-lumped-port κ. The reduction verb is now **`firm`** (cycle-082 lowering-verifier law-confidence pass; firm-on-positive-structure escape — both folded per-mode primitives firm L1, the κ-participation-ratio half via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) and the eigenvalue-un-transform half via [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080), and the eigenpair→`(f, Q)` assembly is bare scalar arithmetic over two firm halves carrying no inner-product-axiom content). The column STAYS `seed` because a feature column may promote past `seed` only once ALL its composed constituents are firm, and the column's OTHER constituent — the upstream [`eigenmode.L4`](./eigenmode.L4.md) driver column — is itself `status: seed`. The SOLE remaining column blocker is the `eigenmode.L4` driver column's own seed→promotion (OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column`). This chapter carries the *compositional* claim (the `(f, Q)` table = the per-mode scalar-ratio reduction over the eigenmode driver's eigenpair family), not the constituents' per-op algebraic claims (those live in [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) and the [`eigenmode.L4`](./eigenmode.L4.md) driver column). The defining structural fact: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` (the eigenvalue un-transform) + `postoperator.cpp:1171-1203` (`MeasureLumpedPortsEig`, the Q-factor) realizing the reduction, all anchors confirmed on-disk via palace-codemap `read_range` + citecheck `--anchor` this dispatch, plus the constituent down-links.
[new]: `firm` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the rank-1 per-mode-table sibling of the rank-2 Gram output products [capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md). The composition is sound: stage (1) consumes the [`eigenmode.L4`](./eigenmode.L4.md) driver column's converged eigenpair family; stage (2) composes the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode scalar-ratio reduction at the problem-type un-transform + resistive-lumped-port κ. **The column promotes off `seed` to `firm` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03; codified batch-26 meta-phase; memory `project_feature_column_promotion_rule`):** a column promotes when its OWN composition + directly-owned constituents are firm. This column's sole directly-owned constituent — the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) reduce verb — is **`firm`** (cycle-082 lowering-verifier law-confidence pass; firm-on-positive-structure escape — both folded per-mode primitives firm L1, the κ-participation-ratio half via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) and the eigenvalue-un-transform half via [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080), and the eigenpair→`(f, Q)` assembly is bare scalar arithmetic over two firm halves carrying no inner-product-axiom content). The cross-link to the [`eigenmode.L4`](./eigenmode.L4.md) driver column (its own `status: seed`) is a **SIBLING reference, NOT a blocker** — it is the reciprocal drift-guard, not a constituent-firmness dependency. This retires the earlier mutual-blocking deadlock (the prior text held this column at `seed` because `eigenmode` was seed, while `eigenmode` was symmetrically held seed for reducing into this column — the exact reciprocal deadlock the directive breaks). This chapter carries the *compositional* claim (the `(f, Q)` table = the per-mode scalar-ratio reduction over the eigenmode driver's eigenpair family), not the constituents' per-op algebraic claims (those live in [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) and the [`eigenmode.L4`](./eigenmode.L4.md) driver column). The defining structural fact: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` (the eigenvalue un-transform) + `postoperator.cpp:1171-1203` (`MeasureLumpedPortsEig`, the Q-factor) realizing the reduction, all anchors confirmed on-disk via palace-codemap `read_range` + citecheck `--anchor` this dispatch, plus the constituent down-links.
```

```edit:book/src/feature/eigenfrequency-qfactor.L1.md
[old]: ---
kind: feature-surface
feature: eigenfrequency-qfactor
level: L1
status: seed
[new]: ---
kind: feature-surface
feature: eigenfrequency-qfactor
level: L1
status: firm
```

```edit:book/src/feature/eigenfrequency-qfactor.L1.md
[old]: | producing driver column | [`eigenmode.L1`](./eigenmode.L1.md) (driver feature column) | seed | `eigensolver.cpp:32-477` |
[new]: | producing driver column (sibling reference, not a blocker) | [`eigenmode.L1`](./eigenmode.L1.md) (driver feature column) | seed | `eigensolver.cpp:32-477` |
```

```edit:book/src/feature/eigenfrequency-qfactor.L1.md
[old]: `seed` — the L1 pure-function composition root for the eigenfrequency / Q-factor output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [eigenfrequency-qfactor.L4](./eigenfrequency-qfactor.L4.md) composition root. It consumes the [`eigenmode.L1`](./eigenmode.L1.md) driver column's converged eigenpair set, then maps each mode to its `(f, Q)` row (the problem-type eigenvalue un-transform + the resistive-port κ participation ratio + the `f/κ` quotient). The reduction's L4 home [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is now **`firm`** (promoted cycle-082 on the firm-on-positive-structure escape; both of its folded per-mode primitives firm L1 — the eigenvalue un-transform via [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080) and the κ participation ratio via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) — and the eigenpair→`(f, Q)` assembly carries no inner-product-axiom content). The column nonetheless STAYS `seed`: a feature column may promote past `seed` only once ALL its composed constituents are firm, and the column's OTHER constituent — the upstream [`eigenmode.L1`](./eigenmode.L1.md) driver column — is itself `status: seed`. The SOLE remaining column blocker is the eigenmode driver column's own seed→promotion (OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column`); the verb-side gate (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`) is **discharged**. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The defining structural fact carried from L4: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` + `postoperator.cpp:1171-1203` realizing the reduction, plus the constituent down-links.
[new]: `firm` — the L1 pure-function composition root for the eigenfrequency / Q-factor output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [eigenfrequency-qfactor.L4](./eigenfrequency-qfactor.L4.md) composition root. It consumes the [`eigenmode.L1`](./eigenmode.L1.md) driver column's converged eigenpair set, then maps each mode to its `(f, Q)` row (the problem-type eigenvalue un-transform + the resistive-port κ participation ratio + the `f/κ` quotient). **The column promotes off `seed` to `firm` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03):** its sole directly-owned constituent, the reduction's L4 home [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md), is **`firm`** (promoted cycle-082 on the firm-on-positive-structure escape; both of its folded per-mode primitives firm L1 — the eigenvalue un-transform via [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080) and the κ participation ratio via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) — and the eigenpair→`(f, Q)` assembly carries no inner-product-axiom content). The cross-link to the [`eigenmode.L1`](./eigenmode.L1.md) driver column (its own `status: seed`) is a **SIBLING reference, NOT a blocker** — the reciprocal drift-guard, not a constituent-firmness dependency. This retires the earlier mutual-blocking deadlock (the prior text held the column seed because `eigenmode` was seed, while `eigenmode` was symmetrically held seed for reducing into this column). The verb-side gate (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`) was discharged at c082. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The defining structural fact carried from L4: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` + `postoperator.cpp:1171-1203` realizing the reduction, plus the constituent down-links.
```

```edit:book/src/feature/eigenfrequency-qfactor.L0.md
[old]: ---
kind: feature-surface
feature: eigenfrequency-qfactor
level: L0
status: seed
[new]: ---
kind: feature-surface
feature: eigenfrequency-qfactor
level: L0
status: firm
```

```edit:book/src/feature/eigenfrequency-qfactor.L0.md
[old]: `seed` — the L0 ground-truth surface for the eigenfrequency / Q-factor output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [capacitance.L0](./capacitance.L0.md) / [inductance.L0](./inductance.L0.md) output-product exemplars. Every stage is a cited range into `palace/drivers/eigensolver.cpp` (the un-transform) + `palace/models/postoperator.cpp` (the Q-factor), confirmed on-disk via palace-codemap `read_range` this dispatch (the readout loop `:424`, eigenvalue read `:427`, the linear-EVP `std::sqrt` branch `:430-434`, the quadratic-EVP `/= 1i` branch `:435-439`, the measure `:458`, loop close `:471`, verify `:472-475`; the Q-factor def `postoperator.cpp:1172`, `freq_re` `:1177`, the κ formula comment `:1186-1191`, `resistor_power` `:1196-1198`, `mode_port_kappa` `:1199-1200`, `quality_factor` `:1201-1203`). The load-bearing structural fact at L0: a pure per-mode map (the readout loop carries no inter-mode accumulator), reducing each converged mode to its `(f, Q)` scalar row — a rank-1 per-mode table, NOT a family-PAIR Gram grid (c074 D6 closed-negative). The chapter's evidence IS the source range + the per-stage site map to the constituent reduction (the adapted surface-or-evidence form for the feature-surface kind).
[new]: `firm` — the L0 ground-truth surface for the eigenfrequency / Q-factor output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [capacitance.L0](./capacitance.L0.md) / [inductance.L0](./inductance.L0.md) output-product exemplars. **The column promotes off `seed` to `firm` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03):** its sole directly-owned constituent reduction verb [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is `firm` (c082); the producing [`eigenmode`](./eigenmode.L0.md) driver column is a sibling reference, not a blocker. Every stage is a cited range into `palace/drivers/eigensolver.cpp` (the un-transform) + `palace/models/postoperator.cpp` (the Q-factor), confirmed on-disk via palace-codemap `read_range` (the readout loop `:424`, eigenvalue read `:427`, the linear-EVP `std::sqrt` branch `:430-434`, the quadratic-EVP `/= 1i` branch `:435-439`, the measure `:458`, loop close `:471`, verify `:472-475`; the Q-factor def `postoperator.cpp:1172`, `freq_re` `:1177`, the κ formula comment `:1186-1191`, `resistor_power` `:1196-1198`, `mode_port_kappa` `:1199-1200`, `quality_factor` `:1201-1203`). The load-bearing structural fact at L0: a pure per-mode map (the readout loop carries no inter-mode accumulator), reducing each converged mode to its `(f, Q)` scalar row — a rank-1 per-mode table, NOT a family-PAIR Gram grid (c074 D6 closed-negative). The chapter's evidence IS the source range + the per-stage site map to the constituent reduction (the adapted surface-or-evidence form for the feature-surface kind).
```

### FLIP 2 — sparameters (own verb `sparameter_reduce` firm c083; retire the "held pending batch-26 meta-phase" clause)

```edit:book/src/feature/sparameters.L4.md
[old]: ---
kind: feature-surface
feature: sparameters
level: L4
status: seed
[new]: ---
kind: feature-surface
feature: sparameters
level: L4
status: firm
```

```edit:book/src/feature/sparameters.L4.md
[old]: The whole output product therefore lowers cleanly outward to the L4 backend surface: `sparameters = sparameter_reduce (ports) ∘ driven_family` — a one-reduction tail on the driven driver column. The column is `seed`. NOTE (cycle-083): [`sparameter_reduce`](../L4/sparameter_reduce.md) was **promoted to `firm`** (the lowering-verifier firm-on-positive-structure escape) — so its constituent is now firm, but the column promotion-rule (a feature column may promote past `seed` only once ALL its composed constituents are firm) and the `seed` status are **held pending the batch-26 meta-phase** (a user directive to revise the column-promotion rule is pending; out of scope for the c083 dispatch). The earlier rough-in rationale is superseded by the firm promotion; the column-status reconciliation is the batch-26 item.
[new]: The whole output product therefore lowers cleanly outward to the L4 backend surface: `sparameters = sparameter_reduce (ports) ∘ driven_family` — a one-reduction tail on the driven driver column. The column **promotes off `seed` to `firm`** under the **OWN-COMPOSITION rule** (USER DIRECTIVE 2026-06-03; CLAUDE.md §Extraction-goal): a column promotes when its OWN composition + directly-owned constituents are firm. This column's sole directly-owned constituent — the [`sparameter_reduce`](../L4/sparameter_reduce.md) port-projection reduction verb — was **promoted to `firm`** at cycle-083 (the lowering-verifier firm-on-positive-structure escape). The batch-26 meta-phase the c083 prose deferred to has now fired and enacted the OWN-COMPOSITION rule, so the earlier "held pending the batch-26 meta-phase" clause is retired: the cross-link to the [`driven.L4`](./driven.L4.md) driver column that produces the per-ω solution family is a **SIBLING reference, NOT a blocking constituent** — its own `seed` status does not gate this column.
```

```edit:book/src/feature/sparameters.L4.md
[old]: | producing driver column | [`driven.L4`](./driven.L4.md) (driver feature column) | seed | `drivensolver.cpp:37-229` |
[new]: | producing driver column (sibling reference, not a blocker) | [`driven.L4`](./driven.L4.md) (driver feature column) | seed | `drivensolver.cpp:37-229` |
```

```edit:book/src/feature/sparameters.L4.md
[old]: `seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stage (1) consumes the [`driven.L4`](./driven.L4.md) driver column's per-ω solution family; stage (2) composes the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* port-projection reduction (the port-projection sibling of the c074 energy-Gram reductions, NOT a `gram_reduce` weight specialization). The column stays `seed` pending the batch-26 meta-phase: `sparameter_reduce` is now `firm` (c083 lowering-verifier promotion), so its constituent is firm — but a user directive to revise the column-promotion rule (a feature column may promote past `seed` only once ALL its composed constituents are firm) is pending the batch-26 meta-phase, so the column-status reconciliation is held out of scope for c083. This chapter carries the *compositional* claim (S-parameters = the port-projection reduction over the driven driver's per-ω solution family), not the constituents' per-op algebraic claims (those live in `sparameter_reduce` and the L0 projection sites). Evidence: the L0 reduction range `postoperator.cpp:1246-1307` (`MeasureSParameter`) + the port-projection verbs (`lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`), all self-verified on-disk via palace-codemap this dispatch, plus the constituent down-links.
[new]: `firm` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stage (1) consumes the [`driven.L4`](./driven.L4.md) driver column's per-ω solution family; stage (2) composes the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* port-projection reduction (the port-projection sibling of the c074 energy-Gram reductions, NOT a `gram_reduce` weight specialization). **The column promotes off `seed` to `firm` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03; codified batch-26 meta-phase; memory `project_feature_column_promotion_rule`):** a column promotes when its OWN composition + directly-owned constituents are firm. This column's sole directly-owned constituent — [`sparameter_reduce`](../L4/sparameter_reduce.md) — is `firm` (c083 lowering-verifier firm-on-positive-structure promotion). The batch-26 meta-phase the c083 prose deferred to has now fired and enacted the OWN-COMPOSITION rule, so the earlier "held pending the batch-26 meta-phase" clause is retired; the cross-link to the [`driven.L4`](./driven.L4.md) driver column (its own `status: seed`) is a **SIBLING reference, NOT a blocker** — the reciprocal drift-guard, not a constituent-firmness dependency. This chapter carries the *compositional* claim (S-parameters = the port-projection reduction over the driven driver's per-ω solution family), not the constituents' per-op algebraic claims (those live in `sparameter_reduce` and the L0 projection sites). Evidence: the L0 reduction range `postoperator.cpp:1246-1307` (`MeasureSParameter`) + the port-projection verbs (`lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`), all self-verified on-disk via palace-codemap this dispatch, plus the constituent down-links.
```

```edit:book/src/feature/sparameters.L1.md
[old]: ---
kind: feature-surface
feature: sparameters
level: L1
status: seed
[new]: ---
kind: feature-surface
feature: sparameters
level: L1
status: firm
```

```edit:book/src/feature/sparameters.L1.md
[old]: | producing driver column | [`driven.L1`](./driven.L1.md) (driver feature column) | seed | `drivensolver.cpp:37-229` |
[new]: | producing driver column (sibling reference, not a blocker) | [`driven.L1`](./driven.L1.md) (driver feature column) | seed | `drivensolver.cpp:37-229` |
```

```edit:book/src/feature/sparameters.L1.md
[old]: `seed` — the L1 pure-function composition root for the scattering-matrix output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02). It consumes the [`driven.L1`](./driven.L1.md) driver column's per-ω solution family, then folds the firm L1 port-mode projection ([`port_projection`](../L1/port_projection.md), firm as of cycle-077) over the (port, frequency) grid with the self-reflection + port-kind closing. The per-mode projection primitive is firm; as of cycle-083 the whole-grid reduction it composes — [`sparameter_reduce`](../L4/sparameter_reduce.md) at L4 — is **also `firm`** (the lowering-verifier firm-on-positive-structure promotion). The column nonetheless stays `seed` pending the batch-26 meta-phase: the promotion rule (a feature column promotes past `seed` only once ALL its composed constituents are firm) and the column status are held for the pending column-promotion-rule user directive (out of scope for c083). The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 reduction range `postoperator.cpp:1246-1307` + the port-projection verbs (`lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`), self-verified on-disk this dispatch, plus the constituent down-links.
[new]: `firm` — the L1 pure-function composition root for the scattering-matrix output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02). It consumes the [`driven.L1`](./driven.L1.md) driver column's per-ω solution family, then folds the firm L1 port-mode projection ([`port_projection`](../L1/port_projection.md), firm as of cycle-077) over the (port, frequency) grid with the self-reflection + port-kind closing. The per-mode projection primitive is firm; as of cycle-083 the whole-grid reduction it composes — [`sparameter_reduce`](../L4/sparameter_reduce.md) at L4 — is **also `firm`** (the lowering-verifier firm-on-positive-structure promotion). **The column promotes off `seed` to `firm` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03):** its sole directly-owned constituent — the reduction's L4 home [`sparameter_reduce`](../L4/sparameter_reduce.md) — is firm (c083). The batch-26 meta-phase the c083 prose deferred to has now fired and enacted the OWN-COMPOSITION rule; the cross-link to the [`driven.L1`](./driven.L1.md) driver column (its own `status: seed`) is a **SIBLING reference, NOT a blocker** — the reciprocal drift-guard, not a constituent-firmness dependency. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 reduction range `postoperator.cpp:1246-1307` + the port-projection verbs (`lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`), self-verified on-disk this dispatch, plus the constituent down-links.
```

```edit:book/src/feature/sparameters.L0.md
[old]: ---
kind: feature-surface
feature: sparameters
level: L0
status: seed
[new]: ---
kind: feature-surface
feature: sparameters
level: L0
status: firm
```

```edit:book/src/feature/sparameters.L0.md
[old]: `seed` — the L0 ground-truth surface for the scattering-matrix output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02). Every stage is a cited range into the Palace `models/` sources, confirmed on-disk via palace-codemap `read_range` this dispatch (`postoperator.cpp:1246-1307` `MeasureSParameter` body + def `:1246-1309`; the per-port projection cache `:1141` lumped / `:1239` wave; the self-reflection `:1275`/`:1297`; the lumped generalized-S `:1278-1281`; the wave de-embed `:1299-1302`; the lumped projection verb `lumpedportoperator.cpp:283-294`; the wave projection verb `waveportoperator.cpp:780-793`). The chapter's evidence IS the source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
[new]: `firm` — the L0 ground-truth surface for the scattering-matrix output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02). **The column promotes off `seed` to `firm` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03):** its sole directly-owned constituent reduction verb [`sparameter_reduce`](../L4/sparameter_reduce.md) is `firm` (c083); the producing [`driven`](./driven.L0.md) driver column is a sibling reference, not a blocker. Every stage is a cited range into the Palace `models/` sources, confirmed on-disk via palace-codemap `read_range` (`postoperator.cpp:1246-1307` `MeasureSParameter` body + def `:1246-1309`; the per-port projection cache `:1141` lumped / `:1239` wave; the self-reflection `:1275`/`:1297`; the lumped generalized-S `:1278-1281`; the wave de-embed `:1299-1302`; the lumped projection verb `lumpedportoperator.cpp:283-294`; the wave projection verb `waveportoperator.cpp:780-793`). The chapter's evidence IS the source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
```

### STAY-seed 1 — capacitance (own verb `gram_reduce` rough-in; re-author promotion-rule prose to OWN reason)

```edit:book/src/feature/capacitance.L4.md
[old]: The whole output product therefore lowers cleanly outward to the L4 backend surface: `capacitance = gram_reduce (w ≡ 1) ∘ electrostatic_family` — a one-reduction tail on the electrostatic driver column. The column is `seed` (not promoted past it) because `gram_reduce` is itself `rough-in (test-coverage-bounded)` — its folded L1 primitives are rough-in and there is no dedicated Gram-reduction test.
[new]: The whole output product therefore lowers cleanly outward to the L4 backend surface: `capacitance = gram_reduce (w ≡ 1) ∘ electrostatic_family` — a one-reduction tail on the electrostatic driver column. Under the **OWN-COMPOSITION rule** (USER DIRECTIVE 2026-06-03; CLAUDE.md §Extraction-goal) a column promotes off `seed` when its OWN directly-owned constituents are firm; this column STAYS `seed` because its OWN reduce verb [`gram_reduce`](../L4/gram_reduce.md) is `rough-in (test-coverage-bounded)` (its folded L1 bilinear primitives are rough-in and there is no dedicated Gram-reduction test). The cross-link to the [`electrostatic.L4`](./electrostatic.L4.md) producing driver column is a SIBLING reference, NOT the gate — the gate is the column's OWN rough-in reduce verb.
```

```edit:book/src/feature/capacitance.L4.md
[old]: `seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stage (1) consumes the [`electrostatic.L4`](./electrostatic.L4.md) driver column's solution family; stage (2) composes the [`gram_reduce`](../L4/gram_reduce.md) reduction at the voltage `w = 1` specialization. The column stays `seed` (does not promote) because `gram_reduce` is `rough-in (test-coverage-bounded)` — its folded L1 bilinear primitives ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md), [`bilinear-form`](../L1/bilinear-form.md)) are rough-in and no dedicated Gram-reduction test exists; a feature column may promote past `seed` only once ALL its composed constituents are firm. This chapter carries the *compositional* claim (capacitance = the `w = 1` Gram reduction over the electrostatic driver's solution family), not the constituents' per-op algebraic claims (those live in [`gram_reduce`](../L4/gram_reduce.md) and the linked L1 primitives). Evidence: the L0 reduction range `electrostaticsolver.cpp:100-140` (`PostprocessTerminals`) realizing the reduction, plus the firm-track constituent down-links.
[new]: `seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stage (1) consumes the [`electrostatic.L4`](./electrostatic.L4.md) driver column's solution family; stage (2) composes the [`gram_reduce`](../L4/gram_reduce.md) reduction at the voltage `w = 1` specialization. **Under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03; codified batch-26 meta-phase; memory `project_feature_column_promotion_rule`) a column promotes off `seed` when its OWN composition + directly-owned constituents are firm.** This column STAYS `seed` because its OWN reduce verb [`gram_reduce`](../L4/gram_reduce.md) is `rough-in (test-coverage-bounded)` — its folded L1 bilinear primitives ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md), [`bilinear-form`](../L1/bilinear-form.md)) are rough-in and no dedicated Gram-reduction test exists. This is a genuine OWN-constituent gate, NOT a cross-linked-sibling blocker: the [`electrostatic.L4`](./electrostatic.L4.md) producing driver column is a SIBLING reference, not the gate. (Firming `gram_reduce` — gated on `matrix-weighted-norm` + `bilinear-form` going firm — would unblock this column.) This chapter carries the *compositional* claim (capacitance = the `w = 1` Gram reduction over the electrostatic driver's solution family), not the constituents' per-op algebraic claims (those live in [`gram_reduce`](../L4/gram_reduce.md) and the linked L1 primitives). Evidence: the L0 reduction range `electrostaticsolver.cpp:100-140` (`PostprocessTerminals`) realizing the reduction, plus the firm-track constituent down-links.
```

```edit:book/src/feature/capacitance.L1.md
[old]: `seed` — the L1 pure-function composition root for the capacitance output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02). It consumes the [`electrostatic.L1`](./electrostatic.L1.md) driver column's solution family, then folds the two rough-in L1 bilinear primitives ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `rough-in (test-coverage-bounded)`, [`bilinear-form`](../L1/bilinear-form.md) rough-in) over the family-pair grid. The reduction therefore rests on rough-in L1 primitives — consistent with the column being `seed`, not a firm composition. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 reduction range `electrostaticsolver.cpp:100-140` realizing the composition, plus the constituent down-links.
[new]: `seed` — the L1 pure-function composition root for the capacitance output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02). It consumes the [`electrostatic.L1`](./electrostatic.L1.md) driver column's solution family, then folds the two rough-in L1 bilinear primitives ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `rough-in (test-coverage-bounded)`, [`bilinear-form`](../L1/bilinear-form.md) rough-in) over the family-pair grid. **Under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03) a column promotes off `seed` when its OWN directly-owned constituents are firm; this column STAYS `seed` because its OWN reduce primitives are rough-in** (the reduction rests on the rough-in L1 bilinear primitives, whose L4 home `gram_reduce` is `rough-in (test-coverage-bounded)`). This is an OWN-constituent gate, NOT a cross-linked-sibling blocker: the [`electrostatic.L1`](./electrostatic.L1.md) producing driver column is a SIBLING reference, not the gate. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 reduction range `electrostaticsolver.cpp:100-140` realizing the composition, plus the constituent down-links.
```

### STAY-seed 2 — inductance (own verb `gram_reduce` rough-in; re-author promotion-rule prose to OWN reason)

```edit:book/src/feature/inductance.L4.md
[old]: `seed` — an output-product leaf feature column under the FEATURE-SURFACE SPINE directive (2026-06-02), the current-normalized sibling of the [capacitance](./capacitance.L4.md) unit-weight output product. The composition is sound: the reduction is the [`gram_reduce`](../L4/gram_reduce.md) combinator's current-normalized specialization (`w = 1/(IᵢIⱼ)`), consuming the [`magnetostatic`](./magnetostatic.L4.md) driver column's solution family `[Aᵢ]`, with the inverse a downstream consumer. The column stays `seed` because `gram_reduce` is itself `rough-in (test-coverage-bounded)` (its folded L1 bilinear primitives are rough-in, and no dedicated test exercises the Gram reduction) — a feature column may promote past `seed` only once ALL its composed constituents are firm. This chapter carries the *compositional* claim (the inductance output product = this current-normalized specialization of `gram_reduce` over the magnetostatic family), NOT the combinator's per-op algebraic claims (those live in [`gram_reduce`](../L4/gram_reduce.md)). Evidence: `PostprocessTerminals` realizing the current-normalized reduction (`magnetostaticsolver.cpp:110-152`, on-disk-verified this dispatch), plus the `gram_reduce` + magnetostatic-column down-links.
[new]: `seed` — an output-product leaf feature column under the FEATURE-SURFACE SPINE directive (2026-06-02), the current-normalized sibling of the [capacitance](./capacitance.L4.md) unit-weight output product. The composition is sound: the reduction is the [`gram_reduce`](../L4/gram_reduce.md) combinator's current-normalized specialization (`w = 1/(IᵢIⱼ)`), consuming the [`magnetostatic`](./magnetostatic.L4.md) driver column's solution family `[Aᵢ]`, with the inverse a downstream consumer. **Under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03; codified batch-26 meta-phase; memory `project_feature_column_promotion_rule`) a column promotes off `seed` when its OWN composition + directly-owned constituents are firm.** This column STAYS `seed` because its OWN reduce verb [`gram_reduce`](../L4/gram_reduce.md) is `rough-in (test-coverage-bounded)` (its folded L1 bilinear primitives are rough-in, and no dedicated test exercises the Gram reduction). This is a genuine OWN-constituent gate, NOT a cross-linked-sibling blocker: the [`magnetostatic`](./magnetostatic.L4.md) producing driver column is a SIBLING reference, not the gate. (Firming `gram_reduce` would unblock this column, jointly with [capacitance](./capacitance.L4.md).) This chapter carries the *compositional* claim (the inductance output product = this current-normalized specialization of `gram_reduce` over the magnetostatic family), NOT the combinator's per-op algebraic claims (those live in [`gram_reduce`](../L4/gram_reduce.md)). Evidence: `PostprocessTerminals` realizing the current-normalized reduction (`magnetostaticsolver.cpp:110-152`, on-disk-verified this dispatch), plus the `gram_reduce` + magnetostatic-column down-links.
```

```edit:book/src/feature/inductance.L1.md
[old]: `seed` — the L1 pure-function output-product composition root for the inductance matrix, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the current-normalized sibling of the [capacitance.L1](./capacitance.L1.md) unit-weight output product. BOTH bilinear primitives are rough-in — the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)` (no dedicated test exercises the SPD-weighted overload) and the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) is rough-in (its `α = xᴴ M y` signature covers the cross-pairing). The entire reduction therefore rests on rough-in L1 primitives — consistent with the column being a `seed`. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: `PostprocessTerminals` realizing the current-normalized reduction (`magnetostaticsolver.cpp:110-152`, on-disk-verified this dispatch), plus the L1 constituent down-links.
[new]: `seed` — the L1 pure-function output-product composition root for the inductance matrix, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the current-normalized sibling of the [capacitance.L1](./capacitance.L1.md) unit-weight output product. BOTH directly-owned bilinear primitives are rough-in — the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)` (no dedicated test exercises the SPD-weighted overload) and the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) is rough-in (its `α = xᴴ M y` signature covers the cross-pairing). **Under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03) a column promotes off `seed` when its OWN directly-owned constituents are firm; this column STAYS `seed` because its OWN reduce primitives are rough-in** (the reduction rests on the rough-in L1 bilinear primitives, whose L4 home `gram_reduce` is `rough-in (test-coverage-bounded)`). This is an OWN-constituent gate, NOT a cross-linked-sibling blocker: the [`magnetostatic.L1`](./magnetostatic.L1.md) producing driver column is a SIBLING reference, not the gate. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: `PostprocessTerminals` realizing the current-normalized reduction (`magnetostaticsolver.cpp:110-152`, on-disk-verified this dispatch), plus the L1 constituent down-links.
```

### STAY-seed 3 — energy-fields (own verb `domain_energy_reduce` rough-in + own folded `matrix-weighted-norm` rough-in)

```edit:book/src/feature/energy-fields.L4.md
[old]: The whole output product therefore lowers cleanly outward to the L4 backend surface:
`energy_fields = domain_energy_reduce (doms, e_total) ∘ driver_field` — a one-reduction tail on a
field-bearing driver column. The column is `seed` (not promoted past it) because
`domain_energy_reduce` is `rough-in` (newly minted) and its
domain-restricted energy form is the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
`rough-in (test-coverage-bounded)` primitive — a feature column may promote past `seed` only once
ALL its composed constituents are firm (the firm [`participation_ratio`](../L1/participation_ratio.md)
half is necessary but not sufficient).
[new]: The whole output product therefore lowers cleanly outward to the L4 backend surface:
`energy_fields = domain_energy_reduce (doms, e_total) ∘ driver_field` — a one-reduction tail on a
field-bearing driver column. Under the **OWN-COMPOSITION rule** (USER DIRECTIVE 2026-06-03;
CLAUDE.md §Extraction-goal) a column promotes off `seed` when its OWN directly-owned constituents
are firm; this column STAYS `seed` because its OWN reduce verb
[`domain_energy_reduce`](../L4/domain_energy_reduce.md) is `rough-in` and its OWN folded
domain-restricted energy form is the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
`rough-in (test-coverage-bounded)` primitive (the firm [`participation_ratio`](../L1/participation_ratio.md)
half is necessary but not sufficient). These are genuine OWN-constituent gates, NOT cross-linked-sibling
blockers — energy-fields is driver-agnostic (a shared postprocess all field-bearing drivers point at),
so the field-bearing driver columns are SIBLING references, not the gate.
```

```edit:book/src/feature/energy-fields.L4.md
[old]: [`participation_ratio`](../L1/participation_ratio.md). The column stays `seed` because
`domain_energy_reduce` is `rough-in` (newly minted) and its domain-restricted energy form is the
`matrix-weighted-norm` `rough-in (test-coverage-bounded)` primitive — a feature column may promote
past `seed` only once ALL composed constituents are firm. This chapter carries the *compositional*
[new]: [`participation_ratio`](../L1/participation_ratio.md). **Under the OWN-COMPOSITION rule
(USER DIRECTIVE 2026-06-03; codified batch-26 meta-phase; memory `project_feature_column_promotion_rule`)
a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; this column
STAYS `seed`** because its OWN reduce verb `domain_energy_reduce` is `rough-in` and its OWN folded
domain-restricted energy form is the `matrix-weighted-norm` `rough-in (test-coverage-bounded)` primitive
(the firm `participation_ratio` half is necessary but not sufficient). These are genuine OWN-constituent
gates, NOT cross-linked-sibling blockers — the field-bearing driver columns are SIBLING references
(this is a driver-agnostic shared postprocess), not the gate. This chapter carries the *compositional*
```

```edit:book/src/feature/energy-fields.L1.md
[old]: It consumes a field-bearing driver column's solution field, then maps each configured domain to its
`(energyᵢ, pᵢ)` row (the domain-restricted energy form + the participation ratio). The reduction's
L4 home `domain_energy_reduce` is `rough-in` and its domain energy
form is the `matrix-weighted-norm` `rough-in (test-coverage-bounded)` primitive (only the
[`participation_ratio`](../L1/participation_ratio.md) half is firm) — consistent with the column
being `seed`, not a firm composition. The chapter carries the compositional claim only; per-op
[new]: It consumes a field-bearing driver column's solution field, then maps each configured domain to its
`(energyᵢ, pᵢ)` row (the domain-restricted energy form + the participation ratio). **Under the
OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03) a column promotes off `seed` when its OWN
directly-owned constituents are firm; this column STAYS `seed`** because its OWN reduce verb's L4 home
`domain_energy_reduce` is `rough-in` and its OWN folded domain energy form is the `matrix-weighted-norm`
`rough-in (test-coverage-bounded)` primitive (only the [`participation_ratio`](../L1/participation_ratio.md)
half is firm). These are OWN-constituent gates, NOT cross-linked-sibling blockers — the field-bearing
driver columns are SIBLING references (a driver-agnostic shared postprocess), not the gate. The
chapter carries the compositional claim only; per-op
```

## Supporting evidence

- **Output-product columns currently at this surface (slugs):** `eigenfrequency-qfactor`, `sparameters`, `capacitance`, `inductance`, `energy-fields` — each at L4/L1/L0 under `book/src/feature/`.
- **Own reduce-verb constituents (on-disk `## Status`, confirmed this dispatch):**
  - `eigenfrequency-qfactor` → [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) = `firm` (c082) → **FLIP**.
  - `sparameters` → [`sparameter_reduce`](../L4/sparameter_reduce.md) = `firm` (c083) → **FLIP**.
  - `capacitance` + `inductance` → [`gram_reduce`](../L4/gram_reduce.md) = `rough-in (test-coverage-bounded)` → **STAY seed**.
  - `energy-fields` → [`domain_energy_reduce`](../L4/domain_energy_reduce.md) = `rough-in` + folded [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) = `rough-in (test-coverage-bounded)` → **STAY seed**.
- **Cross-link references (siblings, NOT blockers):** eigenfrequency-qfactor↔eigenmode; sparameters↔driven; capacitance↔electrostatic; inductance↔magnetostatic; energy-fields↔{set of field-bearing drivers} (driver-agnostic, shared postprocess — the b-link exception, ratified batch-24).
- **L0-file note:** the L0 chapters' §Status blocks for the two FLIP columns carried NO deadlock/promotion-rule clause (pure citation-evidence prose) — the `seed`→`firm` flip there is the frontmatter token + a one-clause OWN-COMPOSITION promotion note inserted into §Status (no deadlock clause to retire). The L0 chapters for the three STAY-seed columns (capacitance.L0/inductance.L0/energy-fields.L0) likewise carry only citation-evidence §Status with no promotion-rule assertion, so they need NO prose edit and KEEP `seed` (frontmatter unchanged) — editing them would inject promotion-rule prose that does not currently exist there, over-structuring. They are intentionally left untouched.
- **Within-column high→low ordering** (L4→L1→L0) preserved across all edits; no SUMMARY / matrix changes (D2 does not touch `feature/index.md`).

## Open questions / caveats

- **D2 does NOT write `feature/index.md`** (D1 sole-owns the cohort-wide rule-prose + §Chapter-kind status narrative per the single-index-owner discipline). D1's index narrative must name `eigenfrequency-qfactor` + `sparameters` in the `firm` set and `capacitance`/`inductance`/`energy-fields` in the staying-`seed` set — the deterministic flip outcomes from this report. Flagged so the integrator can reconcile if D1's narrative drifts from the realized D2 flip set above (no drift expected; the plan's verdict table already names these outcomes).
- **`feature-column promoted token = `firm`` (matches the plan's author-confirmed expectation).** I used `firm` for the two flip columns — the natural maturity for a composition-root whose sole directly-owned constituent (the reduce verb) is firm. If the batch-27 meta-phase prefers a feature-specific promoted token (e.g. `composed`/`promoted`), it can re-token uniformly across all flipped columns; flagged per the plan's OQ.
- **No on-disk surprise.** All five reduce-verb / folded-form statuses matched the cycle-085 plan's verdict table exactly (the two flip-column verbs firm; the three stay-seed verbs/folded-forms rough-in). No forced flip; no contradiction to route.
- **Future unblock of the three stay-seed columns:** firming [`gram_reduce`](../L4/gram_reduce.md) (gated on `matrix-weighted-norm` + `bilinear-form` firm — the NO-GO-HELD cascade) would jointly unblock capacitance + inductance; firming `domain_energy_reduce` + `matrix-weighted-norm` would unblock energy-fields. Not in scope this cycle (the cascade is NO-GO HELD); noted in each column's re-authored §Status as the OWN-constituent gate.
- **`§Extraction-goal` reference reads correctly in all five re-authored columns** (self-checked; the capacitance.L4 block's `§Extraction-goal` spelling was confirmed after a draft typo was corrected).
