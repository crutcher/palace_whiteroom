# Open questions ledger

**This is an INTAKE channel, not a holding pen** (user directive 2026-05-28). Any agent appends a question here when it surfaces. It is **not** where open work accumulates indefinitely — actionable questions are *migrated into the plan* (`scaffolding/priorities.md`, the project's ongoing fan-out-ranked work plan); resolved/stale/duplicate ones are *closed* to the index below; genuinely-blocked ones are *kept, compacted, with their trigger condition*.

**Maintenance protocol (meta-phase owns this):**
- Between meta-phases the ledger is **append-only** (any agent appends; `integrator-per-report` promotes per-report open questions).
- At **every meta-phase**, the meta-phase runs the unification pass (see `.claude/agents/meta-phase.md` §OQ-ledger unification): triage each `Open` entry against the firm artifact → **close** (resolved/stale/duplicate), **migrate** (actionable → `priorities.md` backlog, ranked by fan-out impact), or **keep** (deferred/contingent, one-liner + trigger). Methodology/policy questions only the human can resolve are flagged `routes to meta-phase / human` and surfaced as an `ask`.
- `cycle-planner` reads this ledger each primary cycle for fresh-intake plan candidates; it does not edit it.

**Last unified:** 2026-05-28 (founding pass; reduced ~3040 lines / 89-stale-laden-`Open` + ~53 buried-open-in-`Answered` → the three-section shape below). Full prior answer prose lives in git history.

Three live sections: **Open — migrated to the plan** (pointers) · **Open — deferred / contingent** (waiting on a trigger) · **Closed (index)**.

---

## Open — migrated to the plan

These are genuinely-open AND actionable; they are tracked in `scaffolding/priorities.md` (the plan), ranked by fan-out impact. The pointer stays here so the ledger remains a complete index of open issues; the plan is the owner.

**Stub homes materialized 2026-05-28:** most of these now have claim-free `stub` entries in the artifact (L2 `inner_product`/`orthogonalize`/`incremental-least-squares`/`ksp_solve`; L2-L1 `inner-product-fold-specialization`; L1-L0 `dot`/`nrm2`/`scal`/`matrix-weighted-norm`-mutation-rotation; L1 `assemble-diagonal`). The constituent OQ slugs below remain the refinement tracking; the work is now "firm the stub in place."

- **l2-named-composition-lifts** → plan Backlog (High fan-out). Firm L2 `orthogonalize` + `incremental-least-squares`; carries `L2-layer-intro-refresh-for-named-compositions`. (Constituent OQs: `orthogonalize-as-future-L2-firstclass-entry`, `incremental-least-squares-as-future-L2-firstclass-entry`, `L2-layer-intro-refresh-for-named-compositions`.)
- **ksp-solve-l2-promotion-non-identity-substantive-gap** → plan Backlog (High fan-out). L2 `ksp_solve` outer-driver framing.
- **l3-vocabulary-inventory-gap** → plan Backlog (High fan-out). L3 backfill beyond BLAS-1 (gemv/trsv/ksp_solve/eigsolve).
- **blas1-l1-l0-lowering-theme-gap** → plan Backlog (High fan-out). Standalone L1>L0 themes for `dot`/`nrm2`/`scal`. (Constituent OQs: `l1-l0-dot-lowering-asymmetry`, `nrm2-lowering-theme-deliverables`, `scal-mutation-rotation-l1-l0-theme`, `nrm2-std-abs-defensive-guard-classification`.)
- **matrix-weighted-norm + bilinear-form firm-promotion** → plan Backlog (Medium). Mutation-rotation theme + variant-axis/test-coverage gates. (Constituent OQs: `matrix-weighted-norm-mutation-rotation-l1-l0-theme`, `matrix-weighted-norm-mixed-element-type-variant`, `bilinear-form-real-vector-coverage-gap`, `bilinear-form-variant-axis-test-coverage`.)
- **normalize-l1-primitive-harvest** → plan Backlog (Medium). (Constituent OQs: `normalize-as-fused-l1-primitive`, `normalize-and-normalize-b-weighted-l1-candidates`.)
- **diagonal-extraction-l1** → plan Backlog (Medium). Harvest `AssembleDiagonal` as an operator-to-data L1 primitive. (OQ `assemblediagonal-is-not-apply-linop-variant`.)
- **rough-in-naming-residue-l0-sweep** → plan Backlog (Low/hygiene). (Constituent OQs: `matrix-weighted-norm-naming-sweep`, `bilinear-form-slug-name-coordination`, `dependency-map-orthog-plane-rotation-stale-edge-prune`, `negative-result-slice-examples-reciprocal-membership`.)
- **cg-initial-residual-quirk-palace-bug-flag-lift** → plan Backlog (Low). (OQ `cg-initial-residual-quirk-palace-bug-flag-lift-path`.)
- **floquet-correction-operator-construction-variants** → plan Backlog (Low).
- **inner_product L2 firm operator** + **L2-L1/inner-product-fold-specialization theme** → plan **Now (active #1/#2)**. (OQs `inner-product-harvester-formalization-and-conjugation-pinning`, `linear-combination-fold-specialization-theme-followups`.)
- **gmres.md §L4 v0.6→v0.7 self-rotation** + **NLEPS at L1+** → plan **Now (active #3/#4)** (large carry-forwards).

## Open — deferred / contingent

Genuinely open but **not yet actionable** — each waits on a stated trigger (an upstream change, a not-yet-firm dependency, a "when-relevant" survey, or a downstream dispatch that will consume it). Promoted into the plan by a future meta-phase once its trigger fires.

### BLAS-1 / linear-update family
- `dot-reduction-tree-determinism-survey` — survey Palace bit-determinism claims for dot uses. *Trigger:* a deterministic-reduction solver variant becomes relevant.
- `axpby-corpus-coverage-exhaustive-indexing` — exhaustive enumeration of ~25 uncited axpy-shaped sites + 3 defined-not-used L0 forms. *Trigger:* L1 vocabulary fully firm / a consumer needs the full set.
- `scal-bit-determinism-fusion` — scal law-4 two-pass-vs-fused rounding (non-load-bearing today). *Trigger:* a deterministic-reduction solver upgrades it to load-bearing.
- `scalar-promotion-mutation-rotation-cross-family-theme` — first-class L1>L0 scalar-promotion theme across the BLAS-1 family. *Trigger:* a cycle decides to surface scalar-promotion recognition as its own theme.
- `axpbypcz-member-method-body-survey` — read the member-form `AXPBYPCZ` γ==0 branch (L1 algebra unaffected). *Trigger:* a lowering-verifier needs the member body.
- `axpbypcz-gamma-asymmetric-branching-rationale` — confirm γ-only L0 branching is by-design vs incidental. *Trigger:* combinator-miner / cross-cutter pass.
- `axpbypcz-sub-pattern-B-defined-not-used-corpus-audit` — full-tree caller audit of sub-pattern B. *Trigger:* lowering-verifier exhaustive audit.

### apply_linop / operator family
- `apply-linop-lowering-verifier-audit-cohort` (folds `apply-linop-workspace-tensor-reading-at-L0` + `apply-linop-preconditioner-application-coverage` + `apply-linop-complex-wrapper-operator-lifting` + `apply-linop-complex-operator-default-impls-of-hermitian-transpose`) — pending lowering-verifier audits on the `apply-linop-mutation-rotation` theme (workspace mention-and-erase; preconditioner-hierarchy coverage; `ComplexWrapperOperator` four-block; `MultHermitianTranspose`/`MultTranspose` defaults). *Trigger:* a lowering-verifier dispatch on the theme.
- `addmult-decomposition-bit-equivalence` — add the matrix-free fp-sum-order load-bearing caveat to `apply-linop-mutation-rotation`. *Trigger:* small abstractor/lifter edit (promote to plan if it blocks a consumer).
- `mfem-add-alias-safety` — audit MFEM `Vector::Add` aliasing semantics (upstream). *Trigger:* lowering-verifier / cross-layer pass on the axpbypcz alias claim.

### Krylov / iterate-while / NLEPS family (mostly gated on NLEPS landing at L1+)
- `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker` — NLEPS is the firm-promotion blocker for `check_stop_into_carry`. *Trigger:* NLEPS lands (plan active #4).
- `check-stop-into-carry-parameterization-over-stop-condition` — parameterized helper form. *Trigger:* `check_stop_into_carry` promotion (NLEPS).
- `iterate-while-witness-alternative-combinator-design` — witness-vs-carry design choice. *Trigger:* concurrent with NLEPS promotion.
- `standalone-iterate-while-l4-l3-theme-pending` — standalone dissolution theme. *Trigger:* a second iterate-while-using L4>L3 theme lands.
- `gmres-givens-stream-as-step-kernel-borderline` — revisit krylov-step inclusion of the Givens-stream. *Trigger:* `incremental-least-squares` firmed at L2 (plan backlog).
- `l4-v01-v06-self-rotation-history-lift-target-decision` — lift-target for the gmres.md L4 self-rotation history. *Trigger:* gmres §L4 self-rotation (plan active #3).

### eigsolve / SLEPc family (gated on upstream)
- `eigsolve-convergence-reason-mapping-promotion` — partly-constructive → firm. *Trigger:* Palace reads `EPSGetConvergedReason` (currently only prints via `EPSConvergedReasonView`).
- `eigsolve-convergence-reason-mapping-slepc-enum-upstream-confirm` — confirm per-version SLEPc enum set + table PEP rows. *Trigger:* lowering-verifier upstream pass.
- `eigsolve-driver-side-double-solve-composition` — linear-eigensolve→QuasiNewton bind at L2/L4. *Trigger:* an L2/L4 eigsolve dispatch.
- `eigsolve-nep-coordinate-convention-empirical-witness` — empirical witness for the NEP convention (source-read-confirmed only). *Trigger:* a test-eigensolver NEP case or a SlepcNEP L0 entry.
- `eigsolve-mutation-rotation-embedded-audit-yaml-resolution-marker` — append the resolved-cycle-013 marker to the embedded audit YAML (low-pri). *Trigger:* a cleanup dispatch.

### chebyshev / preconditioning family
- `spectrum_estimate-l1-rough-in-opacity` — opaque `SpectralNorm` power-iteration dependency. *Trigger:* harvester on `SpectralNorm` (plan carried-forward).
- `chebyshev-l4-l3-dedicated-theme-file` — optional thin L4>L3 chebyshev theme (in-line annotation suffices for now). *Trigger:* a lowering-verifier wants a dedicated anchor.
- `chebyshev-l3-l4-layer-intro-refresh` — refresh L3/L4 index narrative for the chebyshev rows. *Trigger:* a layer-intro-author dispatch.
- `l4-preconditioning-framework-promotion` — firm L4 lift to unblock `cg_preconditioning_framework` slice removal. *Trigger:* a harvester L4 preconditioning-framework lift.

### orthogonalize / concepts / citation hygiene
- `orthogonalize-mutation-rotation-audit-confirmed-rom-consumer-residual` — ROM greedy-loop prior-w discard unaudited. *Trigger:* a lowering-verifier ROM pass.
- `orthogonalize-mutation-rotation-l2-krylov-step-lift-notes` — reverse-lift working notes for a downstream L2 krylov-step lift. *Trigger:* a lifter consuming the theme.
- `concepts-orthogonalization-spec-slices-link-survival` — keep the orthog-slice path-anchor alive if later stub-reduced. *Trigger:* orthog.md stub-reduction.
- `concepts-sequential-obstruction-variant-absorption-drift-spot-check` — spot-check two concept pages vs firm L1. *Trigger:* a same-layer-cross-cutter dispatch.
- `plane-rotation-givens-l0-citation-range-reconcile` — givens_* concept pages cite stale gmres.cpp + off-by-one vs `plane_rotation_stream.md`. *Trigger:* a verify-citation-range pass.
- `slice-pages-l2-l3-accuracy-audit` — verify cg.md/gmres.md slices accurately describe dot L2/L3 usage. *Trigger:* a same-layer-cross-cutter on those slices.
- `axpy-test-linkages-deferred` — add test-linkage entries if axpy is exercised via integration tests. *Trigger:* a test-linkage agent dispatch.
- `mfem-wrapper-solver-l4-complex-from-real-lift-backref` — add the back-ref once `complex-from-real-lift` is firmed at L4. *Trigger:* L4 complex-from-real-lift firming.
- `l0-reference-note-citations-grep-vs-read-discipline` — re-read grep-verified ranges if a future audit extracts algebraic detail. *Trigger:* such an audit consumes those ranges.
- `iterative-file-helper-citation-granularity` — per-overload helper enumeration if the small-dense kernel becomes load-bearing. *Trigger:* that.

### Routes to meta-phase (methodology codification; next meta-phase agenda)
Mirrored in `priorities.md` §Next-meta-phase methodology agenda.
- `variant-absorption-vs-instance-counting-policy` — may already be addressed by the cycle-018 combinator-miner parametric-family mode; confirm at next meta-phase.
- `combinator-miner-authority-defer-verdict-status-edit-scope` — role-spec authority question.
- `test-coverage-bounded-rough-in-nomenclature` — canonicalize the status tier (as `partly-constructive` was).
- `partial-obstruction-status-codification` — codify the status `L3/chebyshev` already uses.

## Closed (index)

One line per slug; full prose in git history. Slugs preserved as cross-reference anchors.

### Resolved / answered in earlier cycles (compacted from the former `## Answered` section)

- `axpby-axpbypcz-next-harvest` — answered cycle-004 — both halves firm at L1; axpbypcz with subsumption chain.
- `axpbypcz-l1-harvest` — answered cycle-004 — firm L1 axpbypcz, 12 laws, two variant axes.
- `scal-primitive-l1-harvest` — answered cycle-004 — firm L1 scal, nine module-axiom laws.
- `l1-index-refresh` — answered cycle-004 — L1 index refreshed (Context/Semantics/Vocabulary-cohort).
- `l1-index-refresh-trigger-met` — answered cycle-004 — refresh landed once firm-operator trigger met.
- `concepts-dot-return-type-correction` — answered cycle-004 — element-type return rule corrected (concepts/dot.md).
- `concepts-dot-dotc-and-inverted-conjugation` — answered cycle-004 — non-existent linalg::Dotc removed; conjugation polarity fixed.
- `dot-backpointer-staleness-after-rewrite` — answered cycle-004 — stale warning replaced with clean back-pointer.
- `dot-blas-heritage-framing-salvage` — answered cycle-004 — BLAS-1 heritage framing kept while specifics corrected.
- `krylov-step-dual-placement-l2-l4-routing` — answered cycle-005 — L2 + L4 with lowering edge.
- `krylov-step-naming-reuse-vs-disambiguation` — answered cycle-005 — same-slug-different-layer; deferred to L4 harvester.
- `krylov-step-l3-identity-in-form-audit` — answered cycle-006 — confirmed-with-refinement by abstractor audit.
- `state-stratification-as-l4-concept-or-l4-row` — answered cycle-005 — flagged to L4 harvester/cycle-planner.
- `scalar-promotion-retroactive-l1-thinning` — answered cycle-005 — routed as priority; four L1 entries thinned.
- `scalar-promotion-l4-calculus-formalisation` — answered cycle-005 — deferred as L4-calculus-design work.
- `l4-row-vs-concept-dependency-convention` — answered cycle-006 — convention honoured by entry content.
- `iterate-while-l4-anchor-missing` — answered cycle-007 — iterate_while + iterate_while_with_prev firmed as L4 rows.
- `krylov-step-l3-row-contingency` — answered cycle-006 — contingency does not fire (abstractor confirms-with-refinement).
- `l4-layer-intro-refresh-unblocked-by-first-firm-row` — answered cycle-008 — L4 intro grounded in three firm operators.
- `concepts-index-kind-classification-full-audit` — answered cycle-006 — 40-row Kind-audit routed as bounded dispatch.
- `same-layer-cross-cutter-cycle-md-write-failure` — answered cycle-006 — routed to meta-phase; no content loss.
- `concepts-index-auxiliary-kind-usage-review` — answered cycle-006 — recorded as future concept-sweep review item.
- `concepts-axpby-axpbypcz-pages-absent` — answered cycle-006 — concept-page authoring routed as cycle-007+ candidate.
- `open-questions-ledger-backreference-audit` — answered cycle-006 — routed to future meta-phase/layer-intro pass (superseded by this unification).
- `krylov-step-l3-identity-in-form-audit-closure-cycle-006` — answered cycle-006 — closure-note resolving two parent OQs.
- `krylov-step-body-identity-theme-pending-cycle-007` — answered cycle-007 — theme authored (L3-L2/krylov-step-body-identity.md).
- `iterate-while-l3-rendering-trajectory-accumulation-gap` — answered cycle-008 — verdict-(c) collapse-rule + Condition 5 applied.
- `ksp-solve-concept-page-signature-update` — answered cycle-007 — concept page defers to L1 SolveResult signature.
- `ksp-solve-mutation-rotation-l1-l0-theme` — answered cycle-008 — first firm L1>L0 constructed-operator theme.
- `l1-intro-refresh-after-constructed-operator-gate` — answered cycle-008 — three surgical L1 index edits.
- `gmres-inner-loop-iterate-while-migration` — answered-by-rough-in-theme cycle-008 — L4>L3 migration theme (rough-in).
- `iterate-while-pure-promotion-decision` — answered cycle-007 — defer; keep sugar inside iterate-while.
- `iterate-while-log-effect-vs-trajectory-channel` — answered cycle-007 — routed to cycle-008+ verifier/abstractor.
- `eigsolve-l1-operator-rough-in-candidate` — answered (partially) cycle-009 — eigsolve landed rough-in (now firm).
- `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` — answered (partially) cycle-010 — both rough-ins landed; firm gates → plan.
- `l0-bundle-5-candidates` — answered cycle-009 — bundle 5 landed 2 of 3; remainder → bundle 6.
- `tests-as-semantic-supplement-l0-vs-concepts-decision` — answered cycle-009 — placement routed to planner/meta-phase.
- `l0-bundle-6-candidates` — answered (partially) cycle-011/016 — bundle-6 ongoing (next candidate fespace → plan #5).
- `eigsolve-linear-solve-failed-status-anchor` — answered cycle-010 — LinearSolveFailed kept L1-constructive with negative anchors.
- `eigsolve-scaling-coordinate-convention` — resolved cycle-011 — un-scaled eigenvalues per un-scale-at-accessor.
- `eigsolve-initial-space-axis-placement` — resolved cycle-011 — initial_space kept in EigControl per-call.
- `eigsolve-iteration-count-result-field` — resolved cycle-011 — added iterations:Int as L1-constructive field.
- `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog` — answered cycle-012 — firm L1/orthogonalize landed.
- `l3-index-matvec-naming-vs-apply_linop-slug` — answered cycle-012 — adopted matvec (apply_linop) parenthetical form.
- `concepts-nrm2-stability-claim-correction` — answered cycle-012 — false scaled-summation bullet replaced (concepts/nrm2.md).
- `l3-index-semantics-overlay-blas1-cohort-prose-refresh` — answered cycle-012 — overlay reframed; BLAS-1 cohort named.
- `eigsolve-slepc-nep-coordinate-convention-audit` — answered cycle-012 — resolved-with-refinement (NEP solves un-scaled).
- `orthog-plane-rotation-stream-sub-slice-batch-3-joint-audit` — answered cycle-012 — sub-slice reduced to stub; invariant hoisted.
- `l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion` — answered cycle-012 — both rows firm.
- `concepts-state-stratification-four-stratum-extension` — answered cycle-012 — four-stratum split added.
- `concepts-derived-view-hoisting-control-flow-boundary-extension` — answered cycle-012 — control-flow-boundary example added.
- `concepts-negative-result-slice-partial-positive-sub-pattern-extension` — answered cycle-012 — partial-positive subsection added.
- `concepts-orthogonalization-coefficient-normalisation-drift` — answered cycle-013 — concept page aligned with firm L1 contract.
- `krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` — answered cycle-014 — 8 dangling cg.md pointers re-anchored.
- `krylov-step-l3-identity-in-form-audit-already-answered-note` — informational — note: already answered cycle-006; do not double-close.
- `l3-krylov-step-cg-md-citation-sweep` — answered cycle-015 — 5 dangling cg.md pointers re-anchored to terminal firm homes.
- `chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep` — resolved cycle-015 — 7 verified citation corrections across two anchor entries.
- `divfree-projector-partly-constructive-to-firm-enactment` — resolved cycle-015 — 5 firming edits; status flipped firm.
- `partly-constructive-entry-mechanism-validated-eigsolve-convergence-reason-mapping` — answered cycle-016 — ENTRY case validated; stays partly-constructive.
- `chebyshev-slice-l4-full-removal` — resolved cycle-015 — slice §L4 re-pointed; chebyshev.md removed (corpus 9/10).
- `l3-chebyshev-downward-prose-iterate-while-refresh` — resolved cycle-016 — stale L3 prose → iterate_while_pure.
- `l4-krylov-step-cg-md-citation-sweep` — answered cycle-016 — 7 dangling cg.md pointers re-anchored.
- `l2-krylov-step-cg-md-citation-sweep` — answered cycle-016 — 12 dangling cg.md pointers re-anchored + 1 CheckDot drift.
- `bundle-6-l0-libceed-operator-file-next-candidate` — resolved cycle-016 — fem-libceed-operator-file authored.
- `l4-chebyshev-residual-formm-foldm-prose-cleanup` — resolved cycle-016 — three stale forM_/foldM prose sites refreshed.
- `divfree-l1-entry-apply-close-and-reltol-line-drift` — resolved cycle-017 — 11 surgical citation corrections in firm L1 entry.
- `divfree-closure-nesting-constructed-gate-carrying-constructed-gate` — answered cycle-017 — premise refuted; divfree is third (not first) gate-carrying instance.
- `l3-l2-body-identity-cg-md-citation-sweep` — resolved cycle-017 — 3 dangling cg.md provenance pointers re-anchored.
- `l3-chebyshev-sibling-formm-foldm-prose-sweep` — resolved cycle-017 — all five sibling mentions refreshed; zero residual.
- `blas1-variadic-linear-combination-fold-unification` — resolved cycle-018 — prong-b (linear_combination firm) + prong-a (combinator-miner parametric-family mode, cycle-018 meta) both enacted.
- `linear-combination-harvester-formalization` — resolved cycle-018 — firm L2 chapter + L2>L1 lowering theme landed.
- `inner-product-fold-sibling-candidate` — answered cycle-018 — inner_product rough-in L2 row landed (harvester/pinning → plan #1/#2).
- `nested-constructed-operator-gate-concept-and-divfree-correction` — resolved cycle-018 — concept page authored + divfree "first" claims corrected.

### Resolved by the 2026-05-28 unification pass (artifact landed earlier; ledger never pruned)

- `axpy-l1-l0-three-subpatterns` — resolved — axpby-mutation-rotation Sub-patterns A/B/C + linear-combination-fold-specialization; axpy subsumed.
- `axpby-axpy-scal-decomposition-decision` — answered cycle-003 — fused-primitive chosen (decisions/axpby-as-primitive.md).
- `scalar-promotion-typing-rule` — resolved cycle-005 — concepts/scalar-promotion.md formalizes the real⊑complex typing rule.
- `nrm2-B-weighted-energy-norm-harvest` — resolved cycle-010 — matrix-weighted-norm.md lands ‖x‖_B (firm-promotion gate → plan).
- `axpby-lowering-verifier-audit` — resolved cycle-003/014 — axpby-mutation-rotation §Verified-against audited.
- `axpbypcz-internal-sub-pattern-A` — resolved cycle-005 — axpbypcz-mutation-rotation Sub-pattern A documents the AXPBY+z.Add internal lowering.
- `axpbypcz-gamma-recognition-is-syntactic-not-semantic` — stale — informational downstream-lowering note; no deliverable.
- `fused-update-chained-collapse-combinator-mining` — resolved cycle-018 — L2/linear_combination laws capture the fused-update fold.
- `subsumption-chain-cross-cutting-concept` — resolved cycle-018 — L2/linear_combination:154-156 formalizes scal≺axpy≺axpby≺axpbypcz.
- `apply-linop-lowering-theme-scope` — resolved cycle-005 — apply-linop-mutation-rotation firm (sub-patterns A–E).
- `addmult-as-more-primitive-form-in-some-subclasses` — resolved — theme records SumOperator::Mult→AddMult + BaseProductOperator inversion.
- `apply-linop-sum-operator-mult-via-addmult-reuse` — resolved — theme records the Mult-via-AddMult reuse note (:163-165).
- `krylov-step-layer-placement` — resolved — firm at L2/L3/L4 with lowering edges.
- `krylov-step-naming-and-borderline-cases` — resolved — firm chapter kept the name with role-vs-family rationale.
- `krylov-step-harvester-deliverables` — resolved cycle-006 — krylov-step harvested firm at L2.
- `l2-dep-map-format-vs-l1` — resolved — L2 index uses the 4-column table matching L1.
- `L2-named-compositions-have-no-single-L0-citation` — stale — recognized L2-named-composition norm; informational.
- `krylov-step-naming-stretches-to-chebyshev` — resolved cycle-012 — chebyshev has its own L2 entry (chebyshev-iteration).
- `krylov-step-theme-body-no-l3-row-drift-cycle-013` — resolved cycle-017 — dissolution theme lines 20/218/220 SUPERSEDED + re-anchored to firm L3/krylov-step.
- `krylov-step-speculative-l1-promotion-decision` — answered cycle-005 — NO promotion (decisions/2026-05-27-krylov-step-speculative-l1-promotion.md).
- `concepts-page-authorship-role-scope` — resolved cycle-003 — layer-intro-author broadened to concepts/.
- `concepts-pre-layered-era-sweep` — resolved cycle-012 — concept-corrections sweep landed.
- `concepts-page-word-count-discipline` — stale — never enforced; concept pages carry inline structure.
- `concepts-sweep-cycle-005-candidate` — duplicate → `concepts-pre-layered-era-sweep`.
- `layer-intro-refresh-thresholds-l2-l3-l4` — stale — resolved by practice; all layer indices populated.
- `vocabulary-cohort-subsection-as-layer-intro-pattern` — stale — pattern adopted in layer intros.
- `lowering-verifier-yaml-in-prose-channel-format` — resolved cycle-003 — fenced ```yaml codified in lowering-verifier.md.
- `subagent-skips-edit-on-explicit-instruction` — resolved cycle-018 — dispatch-phase write-guard across all 8 specialized specs.
- `cycle-planner-grep-before-harvester` — resolved cycle-012 — MCP-first localization codified.
- `minres-mfem-as-l0-substrate-policy` — resolved 2026-05-28 (user) — obstruction stands; Palace aborts on the MINRES/BiCGStab enum (ksp.cpp:53-57), so document "not implemented in Palace", do NOT re-anchor to vendored `mfem::MINRESSolver` (cite Palace; match-not-extend).
- `bicgstab-mfem-reanchor-policy` — duplicate → `minres-mfem-as-l0-substrate-policy` (resolved 2026-05-28).
- `bicgstab-enum-intent` — stale — unanswerable without upstream; obstruction theme stands.
- `advertised-but-unimplemented-krylov-solvers-friction` — resolved — friction-ledger `advertised-but-unimplemented-krylov-solvers`.
- `shared-infra-priorities-rescope-after-obstruction` — resolved — roadmap/plan mark MINRES/BiCGStab `[stub]`.
- `minres-bicgstab-signature-sketches-not-contracts` — stale — obstruction themes stand; speculative sigs are scaffolding.
- `mfemwrappersolver-l0-coverage-candidate` — resolved cycle-007 — L0/mfem-wrapper-solver.md authored.
- `l1-ksp-solve-firm-up-anchor-ready` — resolved cycle-007 — L1/ksp_solve.md firm.
- `mutable-workspace-category-4-split-decision` — stale — split never warranted; Category 4 stays cohorted.
- `plane-rotation-concept-page-canonical-pointer-repoint` — resolved cycle-013 — 3 concept cross-refs repointed to plane_rotation_stream.
- `l1-divfree-projector-promotion` — resolved cycle-015 — L1/divfree-projector.md firm.
- `mixed-justification-sub-rule-methodology` — stale — framing ratified in-place in axpbypcz-mutation-rotation.
- `eigensolver-wrapper-l0-bundle-4-candidate` — answered cycle-008 — L0/eigensolver-wrapper.md authored.
- `l3-backfill-apply-linop-and-blas1-cohort` — resolved cycle-011 — all 8 L3 entries exist; BLAS-1 cohort closed.
- `l3-l1-directory-naming-structure-policy` — resolved cycle-012 — in-line non-adjacent-identity convention codified (no L3-L1/ dir).
- `priority-13-now-landed-as-matrix-weighted-norm` — resolved cycle-010 — routing OQ; matrix-weighted-norm landed.
- `slepc-convergence-reason-lift-sub-theme` — resolved — eigsolve-convergence-reason-mapping.md is the reason→EigStatus table.
- `eigsolve-mutation-rotation-lowering-verifier-followup` — resolved cycle-012 — audited (confirms-with-refinement).
- `orthogonalize-mutation-rotation-l1-l0-theme` — resolved cycle-013 — orthogonalize-mutation-rotation.md firm.
- `chebyshev-slice-rho_0-coefficient-correction` — stale — chebyshev.md slice removed cycle-015; firm entries correct.
- `l3-l4-chebyshev-rows-eligible` — resolved cycle-013/015 — L3/chebyshev (partial-obstruction) + L4/chebyshev (firm) landed.
- `chebyshev-l1-l0-and-l2-l1-lowering-themes` — resolved cycle-013 — chebyshev-smoother-mutation-rotation + chebyshev-iteration-fusion firm.
- `eigsolve-getconverged-forwarder-fix-and-gated-promotion` — resolved cycle-013 — forwarder + promotion landed; theme firm (structural).
- `partly-constructive-to-firm-promotion-route-ratification` — resolved cycle-015 — ratified by meta-phase (validated-by-use).
- `divfree-projector-l1-l0-lowering-verifier-followup` — resolved cycle-016 — divfree-projector-mutation-rotation firm; WeakDiv sign positively anchored.
- `divfree-projector-status-adjudication` — resolved cycle-015 — promoted partly-constructive→firm.
- `chebyshev-l4-wrapper-iteration-vocabulary-reconcile` — resolved cycle-015 — L4/chebyshev firm via iterate_while_pure folds.
- `chebyshev-phase1-slice-reduction` — resolved cycle-015 — chebyshev.md slice removed.
- `chebyshev-lowering-themes-lowering-verifier-followup` — resolved cycle-014 — both themes carry verified_against audit blocks.
- `chebyshev-dead-code-complex-transpose-kernels` — resolved cycle-014 — recorded as recognition rules in the theme.

## Dropped

(none — dropped items are filed under Closed with a `stale` disposition.)
