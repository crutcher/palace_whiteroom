---
verifies: ./CYCLE.md
critiqued_at: 2026-05-29T031500Z
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
repaired_at: 2026-05-29T034500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize assemble-diagonal at L1"

## Critique

### Checks run

**citation-validity — pass.** I independently re-read every load-bearing citation via `palace-codemap` `read_range` (not trusting the report's self-verification). All verify line-exact or within the cited range:
- Fan-out chain: `jacobi.cpp:79` = `op.AssembleDiagonal(dinv);` (sig at 75, +4) followed by `dinv.Reciprocal();` at 80 ✓. Chebyshev 4th-kind `op.AssembleDiagonal(dinv); dinv.Reciprocal();` at `chebyshev.cpp:177-178` ✓; 1st-kind identical at `chebyshev.cpp:240-241` ✓. The "Jacobi / Chebyshev all reuse `op.AssembleDiagonal(dinv); dinv.Reciprocal();`" claim is exact, verbatim, at all three sites.
- `apply_linop`-vs-`assemble-diagonal` contrast anchor: `apply_linop.md:16` = `apply_linop :: (A: LinearOperator[M, N], x: Tensor[N]) -> Tensor[M]` ✓ — the rectangular `M ≠ N` signature the report contrasts against is exactly the firm sibling's signature.
- Load-bearing approximate-diagonal non-law: `jacobi.hpp:15-16` comment "allows for (approximate) diagonal construction for matrix-free operators" ✓; and the test (`test/unit/test-libceed.cpp:343-376`) reads exactly as transcribed — square-only guard `if (&a_test.GetTrialSpace() == &a_test.GetTestSpace())` (346), the comment "Diagonal assembly for high-order Nedelec spaces is only approximate due to face dofs in 3D" (358-359), `rtol = 1.0e-12` default (360) relaxed to `rtol = 1.0` (371) under the 3D + `ND_FECollection` + `GetOrder() > 1` + `!UsesTensorBasis` predicate (365-372), and `REQUIRE(d_test * d_test < rtol * std::max(d_ref * d_ref, 1.0))` (374). The reference is `mat_ref->GetDiag(d_ref)` (352) = `mfem::SparseMatrix::GetDiag` as claimed.
- Representation cohort: `hypre.cpp:85-89` exact-CSR read ✓; `libceed/operator.cpp:116-143` (square-check 120, `diag = 0.0`, `CeedOperatorLinearAssembleAddDiagonal` 138-139) ✓; `rap.cpp:154-193` `ParOperator` (square-check 165-166, convergent-diagonal comment 163-164, `AbsMultTranspose` 172, DiagonalPolicy 180-191) ✓; `rap.cpp:467-479` `ComplexParOperator` real/imag split ✓; `operator.cpp:25-28` base abort ✓; `operator.cpp:85-96` `ComplexWrapperOperator` ✓. All override decls verified: `hypre.hpp:70`, `operator.hpp:97`, `libceed/operator.hpp:56`, `operator.hpp:50-51`. The only off-by-one is `diag = 0.0` cited at `libceed/operator.cpp:122` (actual line 121) — trivial, the cited 116-143 range covers it; flagged below as a minor.

**surface-or-evidence — pass.** This is a stub→firm promotion (new surface authored), not a refinement-of-existing-surface or pure retroactive backfill, so the surface-bearing requirement is satisfied by construction. The core distinction ("operator-to-data, NOT an `apply_linop` variant") is source-grounded, not asserted: the square-only `M = N` signature is enforced at *two independent* L0 sites I verified (`rap.cpp:165` `MFEM_VERIFY(&trial_fespace == &test_fespace, ...)` and `libceed/operator.cpp:120` `MFEM_VERIFY(diag.Size() == height, ...)`), and the test's own square guard at `test-libceed.cpp:346` corroborates it. The "no input vector / result is a property of A alone" claim is directly witnessed by the `const`-method-with-output-arg signature family. The 6 algebraic laws are operator-introspection laws of the matrix-diagonal map; laws 2 and 6 (sum / complex real-imag split) are *structurally* witnessed by `ComplexWrapperOperator::AssembleDiagonal` and `ComplexParOperator::AssembleDiagonal` (independent real/imag assembly after `diag = 0.0`), which I confirmed. Laws 1/3/4/5 are standard pointwise-diagonal identities (scaling, zero, identity, Diag-round-trip) — algebraic, not requiring a positive Palace site, and correctly framed as such. The 4 non-laws are all sourced or correctly typed (diagonal-of-product = standard counter-identity; transpose-invariance = correctly demoted to a non-distinguishing identity matching the absence of an `AssembleDiagonalTranspose`; exact-vs-approximate = the load-bearing one, sourced; FP-strictness = standard).

**rotation-quality — pass.** The entry stays in L1 vocabulary (opaque `LinearOperator[N, N]`, `Tensor[N]`, pure-functional `d = diag(A)`) and is high→low throughout: the L0 mechanics (destination buffer, sizing, `diag = 0.0` zero-init, workspace, abs-prolongation-transpose assembly, Dirichlet `DiagonalPolicy`) are explicitly *named as deferred* to a forthcoming `assemble-diagonal-mutation-rotation` L1>L0 theme rather than embedded in the L1 form. The mutation rotation is genuine state-hiding: the L1 signature drops the output-arg destination buffer and the in-place overwrite, collapsing five concrete representation overrides into one opaque operator argument — strictly more compact / more abstract than the L0 virtual-method family, not a 1:1 rename. (Note: this is a harvester L1 entry, so the rotation is the mutation rotation L0→L1, not an algebraic/reduction L_{n+1}→L_n compaction; the high→low directive — §"Layers are defined high→low" — is observed correctly.)

**variant-axis-coverage — pass.** One live axis (`element-type`: real | complex), correctly kept open and parameterised, with the complex case's real/imag-split behavior pinned to law 6. The `operator-representation` axis (sparse-CSR | matrix-free | parallel-wrapped | complex-wrapped) is explicitly declared *absorbed* into the opaque `LinearOperator` type, citing `concepts/variant-absorption` — not a hidden branch. The two declared *non-axes* are both correctly classified against source: (a) `abs-vs-signed` — the absolute value is taken on the *prolongation* `|P|` not the diagonal entries; I verified `rap.cpp:163-176` (comment "|P| has entry-wise absolute values of the conforming prolongation operator", `hP->AbsMultTranspose(1.0, lx, 0.0, diag)` at 172), so the "output diagonal retains its sign; abs is an L0 assembly mechanic" claim is source-accurate, not a swept-under-the-rug variant; (b) `transpose-mode` — correctly a non-axis (diagonal is transpose-invariant; Palace exposes no `AssembleDiagonalTranspose`, which I confirmed by the absence in the override decls). The `partial-domain (abort)` is correctly framed as a *precondition* (the operator's L1 domain is the diagonal-capable subclasses) rather than a variant — `operator.cpp:25-28` base-class `MFEM_ABORT` verified.

**cross-reference-integrity — pass.** All live `[link]` targets resolve as real files: `L1/apply_linop.md`, `L0/output-arg-vs-receiver.md`, `L0/mfem-vector-types.md`, `concepts/variant-absorption.md` all exist. The not-yet-authored siblings `reciprocal` / `elementwise_product` are referenced as *plain text* (backtick code, not live `[link](...)`), correctly per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention — no dead live-link would be introduced. The MFEM-upstream boundary is handled correctly (see adversarial note below): the report cites the Palace alias site `operator.hpp:21` (`using Operator = mfem::Operator;`, which I verified, with the preceding comment "Functionality extending mfem::Operator from MFEM") and the Palace *overrides* / *call sites*, NOT the MFEM base virtual's internals, and logs the un-overridden-real-operator default-behavior gap as an explicit OQ. This matches CLAUDE.md "Specialized agents cite Palace source, not vendored upstream; if a question requires upstream behavior, log as open question."

**edge-label-fidelity — pass.** Not a lowering-edge report (no `L_{n+1}→L_n` edge label on the proposal — it is an L1 operator entry, lowering deferred). The closest "edge-label-like" carrier is the dep-map cohort count change, which the prose discusses consistently: `**Firm (11)** → **Firm (12)**` targets `L1/index.md:29` (verified that line currently reads "Firm (11)"), and the promotion adds exactly one firm operator (stub was not in the Firm cohort), so 11→12 is arithmetically correct. The dep-map row appends after the `divfree-projector` row (verified at `index.md:75`).

**plan-kind-consistency — pass.** Declared kind is `firm` (stub→firm promotion). The content shape matches: canonical signature pinned across both hierarchies, exhaustive structural citation across all five concrete representations, 6 laws + 4 non-laws, no rough-in placeholders left in the body. The single numerical caveat is correctly recorded as a load-bearing *non-law* rather than a status reduction — which is the right call (the structure is firm; the caveat is a documented, test-witnessed property, not an unresolved constructive sub-part, so `partly-constructive` would be wrong here too). The three proposed-changes blocks (`assemble-diagonal.md` full-rewrite, `index.md` count+bullet+row, `SUMMARY.md` drop "(stub)") are well-formed; the SUMMARY pre-edit string `- [assemble-diagonal (stub)](./L1/assemble-diagonal.md)` matches the current file at `SUMMARY.md:67` exactly.

**skill-uptake-survey — pass.** The report references `verify-citation-range` skill invocation explicitly (Supporting evidence: "All citations self-verified against source via `palace-codemap` `read_range` ... `verify-citation-range` skill"), which is the relevant skill for a citation-dense firm-promotion. `classify-variant-axis` would have been the other natural skill given the axis/non-axis discrimination work; it is not explicitly named, but the axis classification is sound regardless (telemetry note, non-blocking).

### Issues found

1. **Minor citation off-by-one — `CYCLE.md` §Evidence (`palace/fem/libceed/operator.cpp` bullet) and §Supporting evidence.** The report cites `diag = 0.0` at `libceed/operator.cpp:122`; the actual line is **121** (`MFEM_VERIFY(diag.Size() == height, ...)` is 120, `diag = 0.0` is 121). The square-check (120) and `CeedOperatorLinearAssembleAddDiagonal` (139) are correct; only the zero-init line is off by one. Severity: trivial — the citation's enclosing range (116-143) covers the line and the claim is unaffected. Candidate for a one-character repair (122→121) in both the Evidence bullet and the Supporting-evidence self-verification list.

2. **Test-file citation path prefix — `CYCLE.md` §Evidence / §Supporting evidence (`test-libceed.cpp`).** The report cites the test as `test/unit/test-libceed.cpp:343-376` (no `palace/` prefix), while Palace source files carry the `palace/linalg/...` prefix. I initially flagged this as inconsistent, then dismissed it: the established book convention cites test files as `test/unit/...` (confirmed across `dot.md`, `nrm2.md`, `divfree-projector.md`, `orthogonalize.md`), because tests live at `reference/palace/test/...` while source lives at `reference/palace/palace/...`. The report follows the convention correctly. **No action needed** — recorded only so the repairer does not "fix" it into a wrong `palace/test/...` form.

3. **Adversarial note (not a defect) — MFEM-upstream citation boundary.** The real-path `AssembleDiagonal` does resolve into vendored MFEM via `using Operator = mfem::Operator` (`operator.hpp:21`, verified). The report does NOT cite the MFEM base virtual's body and instead (i) cites the Palace alias site + Palace overrides + Palace call sites, and (ii) logs the genuine gap — the semantics of `mfem::Operator::AssembleDiagonal` for any Palace real-operator that does *not* override it — as an explicit OQ, with the mitigating observation that all surfaced smoother consumers call into overriding subclasses (`HypreCSRMatrix` / `ParOperator` / libCEED `Operator`), so no un-overridden real-operator path blocks firm status. This is the correct handling per CLAUDE.md's upstream-symbol policy. The boundary is respected; the firm status is not over-claimed across it. **No defect.**

4. **Adversarial note (not a defect) — approximate-diagonal non-law strength.** The load-bearing exact-vs-approximate non-law is the entry's strongest claim and the one most likely to be over-stated; I verified it is *under*-stated if anything. It is triple-anchored: the Palace `jacobi.hpp:15-16` comment ("(approximate) diagonal construction for matrix-free operators"), the `rap.cpp:163-164` convergent-diagonal AMR comment, and the test's `rtol = 1.0` relaxation gated on the exact predicate (3D, `ND_FECollection`, order > 1, non-tensor-basis). The classification as *load-bearing* (a different *value*, not merely FP reduction-order noise) is justified by the test's own structure — a `1e-12` → `1.0` tolerance jump is twelve orders of magnitude, unambiguously semantic. **No defect; the non-law is well-supported and correctly classified.**

5. **Scope-edge observation (not a defect) — OQ closure + downstream stubs deferred to integrator.** The report proposes closing OQ `assemblediagonal-is-not-apply-linop-variant` and filing three follow-on Backlog items (`assemble-diagonal-mutation-rotation` L1>L0 theme; `reciprocal` / `elementwise_product` L1 primitives; L1 intro fifth-motif refresh). These are correctly routed to the integrator / meta-phase / layer-intro-author rather than enacted in-report (harvester write-authority is `CYCLE.md` + supporting docs only). The OQ-closure framing ("this harvest is the deliberate resolution") is accurate — the entry does land the operator/data divide explicitly. No defect; flagged so the integrator picks up the OQ closure and the three Backlog migrations.

## Repair

### Fixes attempted

- **Finding**: Issue 1 (citation-validity, trivial) — `diag = 0.0` cited at `palace/fem/libceed/operator.cpp:122`; actual line is 121. Appears in both the §Evidence bullet and the §Supporting-evidence self-verification list.
  - **Decision**: repaired
  - **Action**: Verified via `palace-codemap` `read_range palace/fem/libceed/operator.cpp:116-143` — line 116 = method signature, line 120 = `MFEM_VERIFY(diag.Size() == height, ...)` (square precondition, correctly cited), line 121 = `diag = 0.0;`, line 139 = `CeedOperatorLinearAssembleAddDiagonal(...)` (correctly cited). Edited both occurrences in `CYCLE.md`: §Evidence (`palace/fem/libceed/operator.cpp:116-143` bullet, `122`→`121`) and §Supporting evidence (self-verification list, zero-init `122`→`121`). One-character mechanical fix; the enclosing `116-143` range already covers the line so the claim was unaffected — only the precise pointer is corrected.

- **Finding**: Issue 2 (test-file citation path prefix, non-issue) — critic recorded only to prevent mis-"fixing" `test/unit/...` into a wrong `palace/test/...` form.
  - **Decision**: not-needed
  - **Rationale**: The critic verified `test/unit/...` follows the established book convention (tests live at `reference/palace/test/...`, source at `reference/palace/palace/...`; confirmed across `dot.md`, `nrm2.md`, `divfree-projector.md`, `orthogonalize.md`). No edit applied — deliberately left as-is.

- **Finding**: Issue 5 (scope-edge, non-issue) — OQ `assemblediagonal-is-not-apply-linop-variant` closure + three Backlog migrations (`assemble-diagonal-mutation-rotation` L1>L0 theme; `reciprocal` / `elementwise_product` L1 primitives; L1 intro fifth-motif refresh).
  - **Decision**: not-needed
  - **Rationale**: Correctly routed to the integrator / meta-phase / layer-intro-author by the report; enacting them is out of repair authority (and out of harvester write-authority). Not touched — left for the integrator to pick up.

(Issues 3 and 4 are critic "adversarial note (not a defect)" entries requiring no action.)

### Unrepairable findings

None. The single defect (citation off-by-one) was a trivial mechanical pointer fix, applied. All other findings either pass (critic) or are non-issues the critic explicitly flagged to prevent mis-"fixing".

## Suggested resolution

`ready` — all 8 critic checks pass and the one trivial citation off-by-one (`122`→`121`) is repaired in both occurrences. Notes for the integrator:
- This is a stub→firm promotion; the three proposed-changes blocks (`book/src/L1/assemble-diagonal.md` full-rewrite, `book/src/L1/index.md` cohort-count `Firm (11)`→`Firm (12)` + bullet + dep-map row, `book/src/SUMMARY.md` drop the `(stub)` label) are well-formed and verified by the critic against current file state (`index.md:29`, `index.md:75`, `SUMMARY.md:67`).
- Pick up the OQ closure (`assemblediagonal-is-not-apply-linop-variant`, resolved by this entry) and the three Backlog migrations / layer-intro fifth-motif flag from the report's §Open questions.
