---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T000000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
overall_status: ready
---

# META: verification of "Formalize correction_step at L2"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` over the report: **33 ok, 0 failing** (bounds + path-hygiene clean). Re-verified every load-bearing pinpoint independently with `citecheck --anchor` against on-disk `reference/palace/palace/linalg/`. All four decisive verbatim contract comments confirmed at the exact cited lines: `gmg.cpp:176` (`Y <- Y + B (X - A Y)`), `distrelaxation.cpp:104` (`y = y + B (x - A y)`), `chebyshev.cpp:193` and `chebyshev.cpp:264` (`y = y + p(A) (x - A y)`). The producer's claim that codemap `read_range` drifted +1 on the chebyshev comment lines and that on-disk citecheck was used instead is **vindicated** — the on-disk anchors land exactly at `:193`/`:264`. Every supporting anchor also verified: `gmg.cpp:188` `AXPBY(1.0, X[l], -1.0, R[l])`, `gmg.cpp:196` `VCycle(l - 1, false)`, `gmg.cpp:184-188` `Mult2`, `gmg.cpp:189-200` restrict/prolong (`MultTranspose(*P`/`Mult(*P`), `distrelaxation.cpp:108` `y = y + G B_G`, `:102` `it < pc_it`, `:105` `SetInitialGuess`, `:109-117` residual/restrict/inner-solve/prolong-add, `chebyshev.cpp:196-199`/`:270-271` `AXPBY(1.0, x, -1.0, r)`, `:201-204` `r = x`, `jacobi.cpp:92` `dinv *= omega`. The `book/src/L2/index.md:89` count-line pointer is correct (the "21 firm + 1 partly-constructive" line is at line 89). No drift found.

**surface-or-evidence — pass.** This is a new firm chapter (`new:book/src/L2/correction_step.md`) plus two surface-modifying propagation edits, each backed by positive-structure evidence (the verbatim contracts + all-linear-primitive bodies). The record-definition obligation is satisfied: `correction_step` is a combinator whose signature names `A`, `B`, `x`, `y` (LinOp/Tensor primitives, not undefined records), and the combinator itself is fully defined in-chapter (signature, three-stage decomposition, semantics, six laws). No signature-named record lacks a home.

**rotation-quality — pass.** Genuine in-layer conciseness-driven combinator extraction: the smoother/multigrid family's per-sweep bodies, previously each spelling out residual→precondition→add-back, collapse into one combinator with the smoothers re-expressed as B-choosing specialization notes. Strictly more compact/abstract — not a 1:1 rename. The conjugation-closure law (law 6) further unifies the de-Rham `T=G` and coarse-grid `T=P` two-operator forms into a single B-choice (`B = T·B'·Tᵀ` is itself a LinOp), a real abstraction collapse, not a stranding.

**variant-axis-coverage — pass.** Two parametric axes (B-slot; initial-guess zero/nonzero-guess) + two absorbed axes (element-type; operator-representation), all enumerated with source anchors. The over-unification guards explicitly scope OUT the three non-instances (bare-B apply, Krylov shift-invert `(K−σM)⁻¹·M·v`, libCEED `GᵀBᵀDBG` contraction) and annotate divfree-projector as a borderline-NOT-core case — no hidden branches.

**cross-reference-integrity — pass.** Every relative link in the chapter body, dep-map row, vocabulary-cohort bullet, and SUMMARY edit resolves on disk (`../L1/apply_linop.md`, `../L1/axpby.md`, `./krylov-step.md`, `./eigsolve.md`, `./assemble-diagonal.md`, `./divfree-projector.md`, `../L1/divfree-projector.md`, `../semantics/index.md` §1.2.1/§1.2.2/§0.1, the three concept pages, `L1/libceed-quadrature-kernel-impl.md`). All three propagation-edit old_strings (`chebyshev-iteration.md`, `jacobi-smoother.md`, the L2-index rough-in row, the L2-index vocab bullet, the SUMMARY chebyshev anchor) match uniquely on disk. SUMMARY insertion lands inside the "Step kernels" sub-chapter grouping in alpha position (chebyshev-iteration → correction_step → krylov-step). One minor clarity nit recorded below (divfree-projector home cited as L1 then L2 in adjacent sentences) — both targets exist and resolve, so integrity is intact.

**edge-label-fidelity — pass.** `depends-on: [L1/apply_linop, L1/axpby]` — both verified firm (rank 3) on disk. The well-foundedness claim (firm node resting only on firm deps) holds. The `reference:` edges (jacobi-smoother, chebyshev-iteration, divfree-projector, concepts) are correctly typed as navigational/non-rank-constraining specializations, consistent with the OWN-COMPOSITION / combinator-as-entry framing.

**plan-kind-consistency — pass.** Declared `firmness: firm` / `rank: firm`; content shape matches — full signature, semantics, six laws with explicit non-laws, exhaustive variant axes, firm-on-positive-structure justification. No rough-in placeholders in the firm body. The c121 rough-in dep-map row is correctly promoted (replace-and-propagate, not mine-and-strand: both L2 consumers re-expressed in-cycle).

**skill-uptake-survey — pass.** The report references `tools/citecheck/citecheck.py --anchor` for self-verification of the chebyshev drift — the relevant tool for the citation-heavy shape was invoked.

### Issues found

- **(minor / clarity) divfree-projector home cited inconsistently in §Borderline.** `correction_step.md` line 248 links the divfree-projector body to `[divfree-projector](../L1/divfree-projector.md)`, then line 258 refers to it as "firm `[L2/divfree-projector](./divfree-projector.md)`". Both files exist and are firm on disk, so neither link is broken and cross-reference-integrity is not violated — but the same borderline operator is attributed to two different layer-homes within one paragraph. Severity: low (cosmetic; integrator/reader may want a single consistent home reference). Location: `book/src/L2/correction_step.md` §Borderline (proposed-changes block, report lines 248 + 258).

### Graded-stack checks (rank-invariant, reachability)

- **rank-invariant — pass.** Firm rests only on firm `depends-on` deps (`apply_linop`, `axpby` both rank 3); no over-claim above any dep's rank.
- **reachability — pass.** Reachable from feature roots via its smoother/V-cycle consumers (chebyshev-iteration, jacobi-smoother, the GMG/distributive consumers that link down to it). Not garbage.
