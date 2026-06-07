---
agent: lowering-verifier
invoked_at: 2026-06-07T134107Z
scope: L1 kernel-impl-realizes-kernel-api empirical-match re-audit — libceed-quadrature-kernel-impl
status: pending
integrated_at: 2026-06-07T134107Z
integration_commit: 8bdb62e
integration_notes: "Applied clean by integrator-per-report (D2); finalized cycle-126 (batch-40 CLOSER). Audit-only FIRMING empirical-match re-audit of the now-firm libceed-quadrature-kernel-impl: verified_against test-libceed.cpp:284 row upgraded empirical-anchor-confirmed-deferred->empirical-match + new :328-377 harness row; NO status/rank/edge change; DIRECTIVE-3 integrity preserved (kernel-api obstruction surface untouched). DIRECTIVE-3 impl-realizes-API empirical-match owed-debt discharged. Build EXIT 0, no finalize build-repair."
inputs:
  - book/src/L1/libceed-quadrature-kernel-impl.md
  - book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md (kernel-api surface)
  - reference/palace/test/unit/test-libceed.cpp:284,298,328-377 (the empirical-match anchor)
---

# CYCLE: Audit libceed-quadrature-kernel-impl (owed empirical-match re-audit, now firm)

## Summary

This audit discharges the **owed firming empirical-match re-audit** of the now-firm (c125 D1, commit
6da8369) `L1/libceed-quadrature-kernel-impl` — the DIRECTIVE-3 kernel-IMPL node whose constructive
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` tensor-contraction pipeline claims to realize the opaque libCEED
element-quadrature kernel that the firm `fe_assemble` fold quantifies over. When the impl was rough-in
(c124), the STRUCTURAL audit confirmed the five-stage 1:1 field-role correspondence to the kernel-api
contract but **explicitly owed** a firming empirical-match verdict (the `test-libceed.cpp:284` row
carried `verdict: empirical-anchor-confirmed-deferred`). I read the test on-disk and confirm it
constructs a Palace libCEED matrix-free operator (`PartialAssemble` → `FullAssemble`), materializes it,
and asserts it matches the MFEM-assembled reference to `1e-12` — both at the operator-application level
(`TestCeedOperatorMult`) and the assembled-matrix level (`TestCeedOperatorFullAssemble`).

**Top-level verdict: empirical-match PASS; edge-integrity PASS (reference-class, undowngraded API).**
The impl-realizes-kernel-api correspondence is empirically confirmed; the deferred row upgrades to a
concrete `empirical-match` verdict. No defect found — the `realizes-kernel-api` edge stayed
`reference`-class, the kernel-api obstruction surface stayed claim-free / undowngraded, and both
`L4/fe_assemble` and `L1/fe_assemble` stayed firm.

## Per-citation audit

- **Citation**: `reference/palace/test/unit/test-libceed.cpp:284` (+ `:298`, the assertion body)
  - **Theme claim**: `TestCeedOperatorFullAssemble` asserts the assembled libCEED matrix matches the
    MFEM reference to 1e-12 — the empirical-match anchor for the constructive `A = Gᵀ B_𝒟ᵀ D B_𝒟 G`
    impl realizing the opaque kernel-api faithfully.
  - **Found**: `void TestCeedOperatorFullAssemble(mfem::SparseMatrix &mat_test, mfem::SparseMatrix
    &mat_ref, double scaling = 1.0)` at `:284`; body computes `mat_diff = scaling*mat_test - mat_ref`
    (`mfem::Add`, `:295`) and asserts `REQUIRE(mat_diff->MaxNorm() < 1.0e-12 * std::max(mat_ref.MaxNorm(),
    1.0))` (`:298`). `mat_test` is the libCEED full-assembled matrix; `mat_ref` is the MFEM-assembled
    reference. citecheck `--anchor 'TestCeedOperatorFullAssemble'` → `[ok]` at 284; `--anchor 'MaxNorm'`
    → `[ok]` at 298. Both on-disk-exact.
  - **Verdict**: supports (empirical-match).
  - **Notes**: The deferred row was on-disk-exact already at the structural-audit stage; this audit
    elevates the verdict from `empirical-anchor-confirmed-deferred` (anchor-exists) to `empirical-match`
    (the assertion semantics confirm the impl realizes the kernel-api to 1e-12), now that the impl is firm.

- **Citation**: `reference/palace/test/unit/test-libceed.cpp:328-377` (`TestCeedOperator` harness —
    NEW anchor surfaced by this firming audit; supplies the test→impl wiring the deferred row only
    pointed at indirectly)
  - **Theme claim**: (implicit) the test exercises the matrix-free libCEED operator-application path
    against an MFEM reference.
  - **Found**: `template <typename T1, typename T2> void TestCeedOperator(T1 &a_test, T2 &a_ref, ...)`
    (`:328-329`). The reference is built MFEM-side: `a_ref.Assemble(skip_zeros)` / `a_ref.SpMat()`
    (`:332-334`). The test operator is the Palace libCEED matrix-free path: `op_test =
    a_test.PartialAssemble()` (`:338`, the un-materialized matrix-free `ceed::Operator`), then
    `mat_test = a_test.FullAssemble(*op_test, skip_zeros)` (`:342`, materialized from the matrix-free
    op). TWO empirical matches are then asserted: (i) `TestCeedOperatorMult(*op_test, *op_ref,
    test_transpose, scaling)` (`:339`) — the matrix-free `A x` / `Aᵀ x` apply matches the reference
    apply (`y_t_test*y_t_test < 1e-12*...` at `:280`); (ii) `TestCeedOperatorFullAssemble(*mat_test,
    *mat_ref, scaling)` (`:343`) — the assembled matrix match audited above. citecheck `--anchor
    'TestCeedOperatorMult'` → `[ok]` at 339.
  - **Verdict**: supports (empirical-match — both the apply-level AND assembled-matrix-level matches).
  - **Notes**: This is the load-bearing finding for the firming audit: the apply-level match
    (`TestCeedOperatorMult` at `:339`/`:280`) directly exercises the operator-application semantics —
    exactly the `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` contraction the impl realizes — not merely a materialized-matrix
    comparison. The matrix-free `op_test = PartialAssemble()` IS the un-materialized contraction pipeline
    the impl's L1 form describes (the impl's "partial assembly (matrix-free)" representation variant,
    `libceed-quadrature-kernel-impl.md:140-144`). So the empirical match covers BOTH representation
    variants the impl catalogues (partial matrix-free via Mult, full materialized via FullAssemble).

## Applicability conditions

The impl states three applicability conditions (`libceed-quadrature-kernel-impl.md:146-160`). The test
evidence corroborates the in-scope cases:

- **Condition 1 (standard FE basis with tabulated CeedBasis)**: Verifiable — the test harness builds
  `BilinearForm` / `DiscreteLinearOperator` over standard FE spaces (ND/RT/H1/L2 collections; the
  diagonal carve-out at `:365-372` for high-order Nédélec spaces names exactly the de-Rham family the
  condition scopes). **No counter-example**: the GSLIB point-interp facility the condition excludes is
  not exercised by this kernel test.
- **Condition 2 (𝒟 ∈ {Identity, Gradient, Curl, Divergence})**: Verifiable — the de-Rham basis-eval
  modes are exactly the `EvalMode` enum the impl cites (`palace/fem/libceed/integrator.hpp:14-23`). **No counter-example.**
- **Condition 3 (single-machine / per-Ceed device)**: N/A to verify from this unit test (the test is
  single-rank by construction; the multi-rank `ParMesh` overlap the condition defers is read
  single-rank per CLAUDE.md §Scope DIRECTIVE-1). **No counter-example** (consistent with the read-as-
  single-rank scope boundary).

## Algebraic laws (if cited)

The impl's justification kind is **structural** (`libceed-quadrature-kernel-impl.md:162-170`): the
decomposition `A = Gᵀ Bᵀ D B G` is read directly off the `AssembleCeedOperator` master assembler
field-wiring (no reconstructed laws). The firming promotion is on the **firm-on-positive-structure
escape** (syntactic-identity composition facts on the positively-read pipeline). The empirical-match
test does not gate a stated algebraic law; rather it **independently corroborates** the structural
correspondence by exact numerical agreement (1e-12) between the constructive-pipeline-equivalent
libCEED apply and the MFEM reference. This is stronger than the escape requires — the structure is both
read positively AND empirically confirmed against the reference operator.

## Edge / DIRECTIVE-3 integrity check

- **`realizes-kernel-api` edge stays `reference`-class — PASS.** The impl frontmatter
  (`libceed-quadrature-kernel-impl.md:21-23`) lists the edge under `edges: reference:` with `target:
  L1-L0/fe-assemble-libceed-boundary-obstruction`, `kind: realizes-kernel-api`. NOT under `depends-on:`.
  A mis-type to `depends-on` would be the DIRECTIVE-3 defect (it would falsely block the impl on the
  opaque API, rank-pin it to the obstruction, and invert the correspondence into a build dependency).
  Confirmed absent — the impl's only `depends-on` edges are the four firm `composes` substrate ops
  (`:33-40`). No defect.
- **Kernel-api obstruction surface stays claim-free / undowngraded — PASS.**
  `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` reads `status: obstruction` (`:4`),
  `justification_kind: obstruction` (`:8`), role-label `kernel-api` (`:30`), and is described as a
  `negative-result theme, claim-free` (`:182`), `obstruction (opaque-library-ownership)` (`:30`, `:182`).
  The DIRECTIVE-3 invariant holds: the firm impl realizing the kernel does NOT downgrade the API surface
  (the API genuinely IS the opaque library boundary the spine calls; the impl is the reviewed
  from-our-primitives correspondence, not a claim that Palace exposes the kernel as a callable).
- **`L4/fe_assemble` + `L1/fe_assemble` stay firm — PASS.** `L4/fe_assemble.md:4` `firmness: firm`;
  `L1/fe_assemble.md` frontmatter `rank: firm` (the firm fold whose opaque leaf this impl realizes;
  the `realizes-leaf` edge to it is also `reference`-class, `libceed-quadrature-kernel-impl.md:24-25`).

## Proposed changes

Upgrade the `test-libceed.cpp:284` row from `empirical-anchor-confirmed-deferred` to `empirical-match`
(the firming verdict) and add the `TestCeedOperator` harness anchor (`:328-377`) + the apply-level
match anchor (`TestCeedOperatorMult`, `:339`/`:280`) that the firming audit surfaced. The c124
STRUCTURAL rows are append-only after integration — leave them; **replace the single deferred row
in-place** with the upgraded row, and **append** the new harness row. The edit targets ONLY the closing
` ```yaml ` `verified_against:` block of the impl file.

```edit:book/src/L1/libceed-quadrature-kernel-impl.md
[replace the single `test-libceed.cpp:284` row (currently verdict `empirical-anchor-confirmed-deferred`, lines ~261-264) with the two rows below; the other six rows in the block are unchanged]

  - citation: reference/palace/test/unit/test-libceed.cpp:284
    verdict: empirical-match
    audited_at: 2026-06-07T134107Z
    note: FIRMING empirical-match re-audit (c126 D2; owed since c124 now the impl is firm c125 D1). TestCeedOperatorFullAssemble (:284) asserts mat_diff MaxNorm < 1.0e-12 * max(mat_ref MaxNorm, 1.0) at :298 — the libCEED-assembled matrix (mat_test, from a_test.PartialAssemble then FullAssemble) matches the MFEM-assembled reference (mat_ref) to 1e-12. Empirical evidence that the constructive A = Gᵀ B_𝒟ᵀ D B_𝒟 G impl realizes the opaque kernel-api faithfully. citecheck --anchor TestCeedOperatorFullAssemble [ok] :284; --anchor MaxNorm [ok] :298. Upgrades the c124 empirical-anchor-confirmed-deferred row.
  - citation: reference/palace/test/unit/test-libceed.cpp:328-377
    verdict: empirical-match
    audited_at: 2026-06-07T134107Z
    note: TestCeedOperator harness — mat_ref built MFEM-side (a_ref.Assemble/SpMat :332-334); op_test built libCEED matrix-free (a_test.PartialAssemble :338, the un-materialized ceed::Operator the impl's partial-assembly variant describes), mat_test materialized via a_test.FullAssemble :342. TWO matches asserted — apply-level TestCeedOperatorMult(op_test, op_ref) :339 (Mult/MultTranspose y_test*y_test < 1e-12 :280, directly exercises the A x contraction the impl realizes) AND assembled-matrix-level TestCeedOperatorFullAssemble :343. Covers BOTH representation variants (partial matrix-free + full materialized). citecheck --anchor TestCeedOperatorMult [ok] :339.
```

No other edits proposed. The audit found no contradiction — the structural correspondence is sound and
now empirically confirmed; the edge typing and API-surface disposition are correct.

## Supporting evidence

- `reference/palace/test/unit/test-libceed.cpp:284,298` — `TestCeedOperatorFullAssemble` + the 1e-12
  matrix-match assertion (read on-disk + citecheck-confirmed).
- `reference/palace/test/unit/test-libceed.cpp:328-377` — `TestCeedOperator` harness: MFEM reference vs
  libCEED matrix-free `PartialAssemble`/`FullAssemble`; the apply-level (`:339`) + assembled-matrix
  (`:343`) match calls. The Mult-match assertion at `:280`.
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the firm kernel-impl under audit (frontmatter
  edges `:21-40`; L1 form `:90-144`; applicability `:146-160`; verified_against block `:231-265`).
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md:4,8,30,34,182` — the kernel-api surface;
  confirmed `status: obstruction`, role-label `kernel-api`, `realizes-kernel-api` edge described as
  `reference`-class, claim-free.
- `book/src/L4/fe_assemble.md:4` + `book/src/L1/fe_assemble.md` (frontmatter) — both firm.

## Open questions / caveats

- **Rank-invariant check (graded-stack `rank(theme) ≤ min(endpoint ranks)`):** the impl is firm and
  rests on four firm `composes` deps (min = firm) — well-founded, no rank violation. The
  `realizes-kernel-api` and `realizes-leaf` edges are `reference`-class, so they correctly do NOT
  participate in the rank cap (an obstruction-kind API surface would otherwise pin the impl). This is
  the intended RE11 deliberate-reference-only disposition for the API node, not a defect.
- **No counter-example found** in the test evidence to any of the three applicability conditions; the
  single-machine condition (3) is not unit-testable here by construction (it concerns the multi-rank
  overlap read single-rank per scope), recorded as N/A rather than a gap.
- **Direction-of-definition**: N/A — this is a kernel-impl node + its impl-realizes-API correspondence
  audit, not a lowering theme; no high→low directionality concern.
- Nothing left owed: the deferred-empirical-match half of the kernel-impl audit owed since c124 is now
  discharged.
