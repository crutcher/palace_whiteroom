## 2026-05-27 cycle-004 — fourth cycle of new 6-phase flow — 7 wave-1 reports — concepts/dot rewrite + L1 intro refresh + scal/apply_linop/axpbypcz firm + MINRES/BiCGStab obstruction themes

- **Phases fired**: plan (cycle-planner haiku, stretch target 8-12 dispatches → 7 in wave 1) → dispatch (7× parallel: layer-intro-author×2 / harvester×3 / abstractor×2) → critique (7× critic) → repair (7× repairer) → integrate (this commit) → meta (next).

- **Substantive landed (7 reports, all `ready`)**:
  - `book/src/L1/scal.md` — firm L1 operator. Nine algebraic laws (module-over-scalar-field axioms + field-commutativity). Single variant axis (element-type) with scalar-promotion sub-axis. Fourth and last of the BLAS-1 floor primitives. The "no free-function `linalg::Scal`/`Scale`" claim verified by grep. Sibling subsumption with `axpby` (β=0).
  - `book/src/L1/apply_linop.md` — firm L1 operator. **Opaque-operator gate** to the L2 `krylov-step` vocabulary. Seven algebraic laws (linearity, composition, sum, scaling, zero/identity). Three retained variant axes (element-type, transpose-mode, accumulate-mode) + one collapsed (operator-representation — the canonical *variant absorption* application: ~10 concrete `Operator` subclasses fold into a single opaque `LinearOperator` type at L1).
  - `book/src/L1/axpbypcz.md` — firm L1 operator. **Twelve** algebraic laws including the novel Law 12 chained-collapse on shared `(x, y)` (`(α₁ + γ₁·α₂, β₁ + γ₁·β₂, γ₁·γ₂)`). Two variant axes (element-type, scalar-promotion) plus one internal L0 control-flow axis (γ==0 fast-path) explicitly classified as not-an-L1-variant. Mirrors the cycle-003 axpby fused-primitive decision.
  - `book/src/L1-L0/minres-iteration.md` — **obstruction theme**. Palace exposes `KrylovSolver::MINRES` enum but `MakeSolver` aborts on it; no L0 implementation. Three rough-in operators emitted (`lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`). New theme `justification kind: obstruction`. Negative-anchor citations: `ksp.cpp:53-57`, `labels.hpp:104-112`, `configfile.cpp:129`.
  - `book/src/L1-L0/bicgstab-iteration.md` — **obstruction theme**. Same `MFEM_ABORT` branch in `ksp.cpp` covers BiCGStab. Three rough-in operators (`bicgstab_step`, `omega_update`, `stabilisation_update`). Algorithm shape sketched against Saad 2003 §7.4.2.
  - `book/src/concepts/dot.md` — full rewrite. Fixes the three cycle-003 contradictions: (a) `ComplexVector::Dot` returns `std::complex<double>`, not real; (b) all references to non-existent `linalg::Dotc` removed; (c) bogus `vector.cpp:142-178` citation replaced with verified ranges. Preserves BLAS-1 heritage framing. ~310 words (over the 200-word target — flagged for meta-phase).
  - `book/src/L1/dot.md` — small back-pointer softening: removed the inline warning about the (now-corrected) concept page.
  - `book/src/L1/index.md` — full intro refresh + 9 new dep-map rows (3 firm: `scal`/`apply_linop`/`axpbypcz`; 6 rough-in obstruction: 3 from MINRES theme + 3 from BiCGStab theme). New "Vocabulary cohort" subsection (Firm / Rough-in / Queued split). Expanded Context (5 bullets grounded in firm operators) and Semantics (3 motifs).
  - `book/src/SUMMARY.md` — 5 new chapter lines (3 firm L1 + 2 L1>L0 themes). All applied cleanly per planner's anchor-merge plan.

- **Wave-conflict observations** (captured in `scaffolding/integrator-signals.md`):
  - **L1/index.md dep-map**: 9 row appends from 5 wave-mates (3 firm + 6 rough-in). Each row distinct — merged cleanly per cycle-003 signal. **POSITIVE signal that the parallel-when-in-doubt philosophy is working at scale (7 wave-mates, zero structural conflicts).**
  - **SUMMARY.md L1 Part**: 3 firm-operator chapter lines, all chained after `axpby` line in dep-map row order (`scal`, `apply_linop`, `axpbypcz`).
  - **SUMMARY.md L1>L0 Part**: 2 theme chapter lines (`bicgstab-iteration`, `minres-iteration`) — both proposed `append-after axpby-mutation-rotation`. Resolved alphabetically per planner note.
  - **book/src/L1/dot.md**: 1 file written by `concepts-dot-rewrite` (back-pointer softening); no other report writes this file — no actual conflict.

- **Critic findings**: 56 checks total across 7 METAs; 53 pass / 3 warning / 0 fail. All 3 warnings (cross-reference-integrity / skill-uptake / format) `repaired` by repairer.

- **Safety-net gates**: **0 hits**. Variant-axis-missing = 0 (apply_linop has 4 axes, 3 retained + 1 collapsed; axpbypcz has 2 + 1 internal-L0). Cross-reference-integrity = 0 (rough-in links are plain text post-repair on BiCGStab; MINRES live links resolve). Edge-label-fidelity = 0 (obstruction theme correctly classified). Retroactive-budget per-slice / global = 0 / 0.

- **Open questions promoted to ledger**: **25 new** (over 7 reports — high yield reflects the wave size + the new obstruction-theme category surfacing methodology decisions). Routes: `meta-phase` (5: mfem-as-l0-substrate, advertised-but-unimplemented-krylov-solvers, shared-infra-priorities-rescope, vocabulary-cohort-pattern-promotion, subagent-skips-edit-on-explicit-instruction), `abstractor` (4: apply-linop-lowering-theme-scope, axpbypcz-mutation-rotation-abstractor-target, fused-update-chained-collapse-combinator-mining, lanczos-as-arnoldi-variant-axis), `harvester` (4: normalize-as-fused-l1-primitive, addmult-decomposition-bit-equivalence, addmult-as-more-primitive-form, floquet-correction-operator-construction-variants), `same-layer-cross-cutter` (3: concepts-sweep-cycle-005-candidate, slice-pages-l2-l3-accuracy-audit, subsumption-chain-cross-cutting-concept), others (9).

- **Open questions answered**: **9** — `axpby-axpbypcz-next-harvest`, `axpbypcz-l1-harvest`, `scal-primitive-l1-harvest`, `l1-index-refresh` (pilot-1), `l1-index-refresh-trigger-met` (cycle-003), `concepts-dot-return-type-correction`, `concepts-dot-dotc-and-inverted-conjugation`, `dot-backpointer-staleness-after-rewrite`, `dot-blas-heritage-framing-salvage`.

- **Build**: `cargo make book` — see commit. Pre-existing katex-link warnings unchanged.

- **Reports applied**:
  - `reports/2026-05-27T004641Z-layer-intro-author-concepts-dot-rewrite/` (status: ready; follow_up_agent: null)
  - `reports/2026-05-27T004641Z-layer-intro-author-L1-index-refresh/` (status: ready; follow_up_agent: null)
  - `reports/2026-05-27T004641Z-harvester-scal-L1/` (status: ready; follow_up_agent: null)
  - `reports/2026-05-27T004641Z-harvester-apply_linop-L1/` (status: ready; follow_up_agent: null)
  - `reports/2026-05-27T004641Z-harvester-axpbypcz-L1/` (status: ready; follow_up_agent: null)
  - `reports/2026-05-27T004641Z-abstractor-MINRES-L1-L0/` (status: ready; follow_up_agent: meta-phase)
  - `reports/2026-05-27T004641Z-abstractor-BiCGStab-L1-L0/` (status: ready; follow_up_agent: meta-phase)
  - `reports/2026-05-27T005952Z-integrator-cycle-004/REPORT.md` — batch report (this integration).

- **Integrator-signals append**: cycle-004 section prepended above cycle-003 in `scaffolding/integrator-signals.md` (newest-first per file format).
