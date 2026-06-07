---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T231500Z
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

# META: verification of "Audit synthesis-rendered-def-vs-l4-correspondence"

## Critique

This is an **audit-class** report (lowering-verifier, directive-sanctioned Synthesis
correspondence audit) with **no proposed changes** to the artifact. Its claims are
correspondence assertions (rendered-def location ↔ L4-chapter location ↔ L2-chain / kernel-API
node), so the 8 checks largely reduce to verifying the audit's own citations resolve and its
"FAITHFUL" verdicts are honestly supported. I spot-checked the load-bearing correspondences by
reading both endpoints on disk.

### Checks run

- **citation-validity — pass.** `citecheck --scan` on CYCLE.md returns **27 ok, 0 failing**.
  I then read both endpoints of the load-bearing correspondences: (1) `krylov_step` Form A —
  synthesis `iteration.md:220-236` vs L4 `krylov-step.md:95-116`: the five-group dataflow
  (apply_linop / optional-auxiliary / krylov_update / derived_views / sole `modify (it+1)` /
  `pure { krylov, outputs }`) matches; the synthesis result-record vs §Signature-narrative-record
  caveat is faithfully reproduced. (2) `krylov_step` Form B (CgState/cg_first_step/cg_steady_step/
  cg_solve) — synthesis `:241-298` vs L4 `:128-199`: the schema, both step bodies, and the driver
  match. (3) `mk_matrix_free_operator` inline kernel-impl — synthesis `data-algebra.md:153-165` vs
  L2 `matrix-free-operator-apply.md:70-83`: the nested `apply_chain` renders the L2 five-stage
  chain `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` with the correct stage map. (4) `linear_combination` synthesis
  `:56-57` is line-for-line identical to L4 `:88-89`. I also re-ran the two L0 anchor spot-checks
  the report itself cites: `iterative.cpp:434-441 --anchor 'beta_prev'` → ok (line 440 in range);
  `bilinearform.cpp:77 --anchor 'AddSubOperator'` → ok. The report carries no `verified_against:`
  block (no contradiction found), so the YAML round-trip sub-check is moot. All citations resolve
  in-range and back the claims.

- **surface-or-evidence — pass.** No surface modification is proposed (clean audit), so this is
  pure observation-with-evidence — allowed. The audit's evidence shape is correct for an
  implementation-VIEW correspondence audit: each verdict cites the rendered-def range AND the L4
  (and where relevant L2 / kernel-API) endpoint. No record is newly named in a signature without a
  home: every record the audit touches (`CgState`, `OpParams`, `Krylov`, `StepOutputs`,
  `WeakFormTerm`, `FiniteElementSpace`) is defined in the linked L4/concept chapters, which the
  Synthesis defs reference rather than restate — exactly the record-definition-lives-once
  discipline. No record-definition gap.

- **rotation-quality — pass (not applicable to audit-class / implementation-VIEW kind).** The
  report asserts no new algebraic/structural rotation of its own; it audits whether the Synthesis
  *implementation rendering* preserves the L4 op's dataflow. The Synthesis Part rotates nothing
  (it recomposes already-firm vocabulary as code) — analogous to the feature-surface no-op. The
  report correctly characterizes the rendered defs as faithful renderings, not as new rotations.

- **variant-axis-coverage — pass (not applicable).** The audited defs DO carry variant axes
  (krylov_step Form A/Form B; chebyshev Kind4/Kind1; linear_combination arity leaves), and the
  audit correctly notes each is rendered with its variant absorbed per the L4 chapter (Form B is a
  separate worked render; chebyshev variant absorbed into the closure type at `setup`; arity leaves
  as `where`-local specializations). No hidden branch: the audit explicitly checks the variant
  surfaces it touches against their L4 chapters.

- **cross-reference-integrity — pass.** All `[link]` targets and cited slugs resolve on disk:
  `synthesis/iteration.md`, `synthesis/data-algebra.md`, `synthesis/index.md`, the eight cited L4
  chapters, `L2/matrix-free-operator-apply.md`, and `L1-L0/fe-assemble-libceed-boundary-obstruction.md`
  all exist and back the cited ranges. The kernel-API maturity claim is correctly checked against
  on-disk state: the obstruction node carries `status: obstruction` / `sub_kind:
  opaque-library-ownership` with the `kernel-api` role-label at §Status `:30` (the report cited
  `:28-30` — accurate). The `reference`-class-only edge claim is verified against the on-disk
  data-algebra.md frontmatter (`edges: reference:` only, `kind: navigational-container`, no
  `rank:`, no `depends-on`).

- **edge-label-fidelity — pass.** The DIRECTIVE-3 dual-surface edge semantics are correctly
  assessed: `assemble_term` renders `#extern` AFTER its type signature (synthesis
  `data-algebra.md:193-194`) pointing at the kernel-API obstruction node, while
  `mk_matrix_free_operator`'s `apply_chain` renders the kernel-IMPL inline (the L2 contraction
  chain). The report correctly identifies that the Synthesis Part itself adds no blocking
  `depends-on`/`realizes-kernel-api` edges (it is a navigational container), so there is no
  rank-violation or mis-typed-edge surface to flag — an honest negative finding, not a gap.

- **plan-kind-consistency — pass.** Declared kind = lowering-verifier audit; content shape matches
  (per-citation correspondence verdicts, an Applicability-conditions block, a Proposed-changes:
  **None** disposition, L0-anchor spot-checks). No firm/rough-in placeholder mismatch. The two
  items in §Open questions (index `Status: stub (Wave 2)` cell vs rendered bodies; next-pull to
  audit coordination/drivers/types) are genuinely non-blocking and appropriately routed — NOT
  buried findings. The first is a per-chapter-status-token convention question explicitly out of
  audit scope (the chapters' own §Status notes already flag it); the second is honest
  scope-disclosure (coordination.md/drivers.md/types.md were not in this dispatch), correctly filed
  as a next-pull candidate rather than asserted-as-audited. The report does NOT overclaim coverage
  of the un-audited `eigsolve` `#extern` — it confirms only the index-partition internal consistency
  and flags the un-audited def, which is the honest disposition.

- **skill-uptake-survey — pass (telemetry).** The report invokes `citecheck --anchor` for the L0
  substrate spot-checks (the no-drift adjudicator), which is the expected tooling for an audit's
  citation layer. No further skill is implied by the shape.

### Issues found

No blocking or warning-level issues. One non-blocking observation (telemetry, not a defect):

1. **Form-B "line-for-line" slightly understates a real arg-order divergence (observation,
   non-blocking).** CYCLE.md `:106-108` describes the synthesis `cg_solve` as rendering the
   `iterate_while_with_prev` driver "matching L4 `:182-199`," and `:110-115` qualifies the
   difference as "the Synthesis chapter's own (consistent, faithful) record-return spelling." On
   disk the difference is larger than record-vs-tuple *spelling*: the synthesis `cg_solve`
   (`iteration.md:290-297`) renders the **canonical boot/init/steady/cont** arg order with record
   returns — which is exactly the authoritative `iterate_while_with_prev` signature
   (`L4/iterate-while-with-prev.md:43-50`, reproduced at synthesis `iteration.md:178-198`) — whereas
   the L4 **krylov-step.md** `cg_solve` example (`:192-197`) still uses the OLDER positional form
   `iterate_while_with_prev s1 s0.beta (cont) (steady)` with tuple returns. So the synthesis is
   correctly faithful to the *authoritative combinator signature*, and the L4 krylov-step.md
   worked example is itself stale against that signature. The audit's verdict (supports) is
   **correct** and its disclosure is honest in substance; the wording just compresses an
   arg-order-reorder into "record-return spelling." This is a content-precision nuance, not a
   citation or correspondence defect, and — if anything — points at a latent staleness in
   `L4/krylov-step.md:192-197` (a separate matter, out of this report's scope; not a finding
   against this report). Recorded as telemetry; nothing to repair here.

All 8 checks pass; the audit's correspondence verdicts are honestly supported, its citations
resolve in-range, the DIRECTIVE-3 dual-surface and `reference`-only-edge assessments are correct,
and the two Open-questions items are appropriately non-blocking. Setting `overall_status: ready`.
