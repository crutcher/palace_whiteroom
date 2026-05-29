---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T10:42:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T11:05:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L1>L0 theme sketch — nleps-deflated-residual-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass.** Every claim in the proposed chapter and the report scaffolding
carries a pointer, and all pointers resolve in-range. I mechanically bounds-checked all 18
distinct `palace/linalg/nleps.cpp` pinpoints via `tools/citecheck/citecheck.py` (`18 ok, 0
failing`) and anchor-drift-checked the load-bearing ones: `:557` `BuildParSumOperator`, `:559`
`A->Mult(vv, rr)`, `:564` `A->AddMult(XSvv2, rr, 1.0)`, `:563`
`MatVecMult(X, S.fullPivLu().solve(vv2))`, `:568` `linalg::Dot(GetComm(), vv, X[j])`, `:575`
`std::sqrt(std::abs(linalg::Dot(GetComm(), rr, rr))`, `:615` `X[k] = v;` — every one `[ok]`
with the exact token on the asserted line (zero drift). The six intra-book cross-reference
ranges (`nleps_deflated_residual.md:16-29`, `:85`, `:111-117`; `apply_nonlinear_pencil.md:98`;
`dot.md:43`; `dot-mutation-rotation.md:44-81`) are all in-bounds and I read each to confirm it
*means* what the prose claims (the L1 signature, the bit-determinism non-law, the firm-status
precedents, the linearity-in-v law-1, the arg-1-conjugation convention, the fused Sub-pattern A).
The `search_text`-zero-hits test-coverage claim is accurate (re-ran over `test/unit/**` — empty).

**surface-or-evidence — pass.** Not a refinement-shaped proposal: this is a wholly-new L1>L0
theme file (`new:book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md`) plus two
append-only surface touches (index row, SUMMARY entry). It modifies surface (creates a new
chapter) rather than asserting a pure rotation_claim against an existing chapter, so the
refinement-surface gate does not apply. The index/SUMMARY edits are additive and do not alter
existing rows.

**rotation-quality — pass (the load-bearing claim is correct).** The central assertion — that
`A->Mult(vv, rr)` (`:559`) and `A->AddMult(XSvv2, rr, 1.0)` (`:564`) collapse to a single pencil
apply of `vv + X·(λI−H)⁻¹·vv₂` — is verified at source. I read `nleps.cpp:556-575` directly:
both `Mult` and `AddMult` are invoked on the SAME operator `A`, built EXACTLY ONCE at `:557-558`
(`BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2_out.get()}, true)`); `Mult` writes `rr`,
`AddMult` accumulates the second term into the same `rr` with scale `1.0`. So `rr = T(λ)·vv +
T(λ)·XSvv2`, and by `apply_nonlinear_pencil` law 1 (linearity-in-v, confirmed at
`apply_nonlinear_pencil.md:61`) this is `T(λ)·(vv + XSvv2)` — one pencil apply of the
deflation-corrected vector. The L_{n+1} (L1) form is strictly more compact/equational: it hides
the destination buffers, the `A2_out` carry-back cache, the duplicated pencil build, and the
two-step accumulation behind one pure `apply_nonlinear_pencil(T, λ, d)`. The accumulation-order
bit-difference is correctly the ONLY non-structural note — it is recorded as a load-bearing
floating-point caveat (not erased), citing the operator entry's recorded non-law (`:85`), and is
exactly the right scope: the two-step `AddMult`-into-`rr` accumulation orders the FP additions
differently from one apply of a pre-summed vector, with the matrix-free `A2` reduction tree the
locus of the difference. No renaming-only / 1:1 mapping. Strong pass.

**variant-axis-coverage — pass.** The variant axes are explicitly enumerated in §Applicability
conditions and each is covered or scoped: (i) the deflation cardinality `k` — covered with the
`k = 0` un-deflated degeneration handled (the `if (k > 0)` guard at `:560` / `else {
rr2.resize(0) }` at `:573`, both cited and discussed); (ii) the with-C/without-C damping axis —
explicitly absorbed into the pencil argument per `apply_nonlinear_pencil`; (iii) element type —
scoped to complex-only with the rationale (the `ComplexVector`/`Eigen::VectorXcd` carriers); (iv)
single-rank vs MPI — scoped per CLAUDE.md, with the `Mpi::GlobalSum`-no-op-on-one-rank note and
the rank-local `rr2.squaredNorm()` distinction. No hidden branches: I read the full lambda
(`:550-576`) and every branch (`Mult`, the `k>0` block, the `else`, the `sqrt`) is accounted for.

**cross-reference-integrity — warning.** Build-readiness guard PASSES; one low-severity
broken-link defect in report scaffolding. (1) Build-readiness/fence: I enumerated all 22 fences
(even parity); the `new:` block opens at CYCLE.md:38 and closes at :388, and the firm apparatus
— `## Status` (:59), the L1-form signature (:75-92), the L0 form (:94-131), and the three
Sub-patterns A/B/C (:155, :209, :266) — all sit INSIDE that fence, with 8 balanced nested
` ```text ` pairs correctly enclosed. This is the OPPOSITE of the cycle-019 fence-truncation
defect (the firm body is enclosed, not authored as the report's own top-level sections). (2) All
chapter-body live links resolve from `book/src/L1-L0/` (`../L1/nleps_deflated_residual.md`,
`../L1/lu_solve.md`, `../L2/linear_combination.md`,
`../L2-L1/linear-combination-fold-specialization.md`, `../L1/nrm2.md`, `./dot-mutation-rotation.md`,
`../L1/apply_nonlinear_pencil.md`, `../L1/dot.md` — all present). (3) Index-row anchor
(`dot-mutation-rotation` line) and SUMMARY insert anchors (between `dot-mutation-rotation` and
`nrm2-mutation-rotation`, lines 90/91 of the live SUMMARY) match the live files exactly. The
WARNING is for the report-scaffolding `## Speculative operators proposed` section (CYCLE.md
:410-413): its links use `../../../book/src/...` (three levels up), but the correct depth from
`reports/<id>/` is `../../book/src/...` (two levels) — confirmed both forms by filesystem probe.
These four links are DEAD. They live OUTSIDE the publishable `new:` fence (CYCLE.md scaffolding
that is never built into the artifact), so they do NOT break the mdBook build — hence warning,
not fail — but they are genuinely broken references and the same target slugs are linked
correctly inside the fence, so the fix is mechanical.

**edge-label-fidelity — pass (L1>L0 core check).** The theme is labeled L1>L0 and the prose is
narrated FORWARD throughout: §"L1 form (LHS)" gives the pure functional form, §"L0 form (RHS)"
gives the `compute_residual` lambda body, and §"Rewrite — forward (L1 → L0)" plus all three
Sub-patterns narrate the L1→L0 direction (LHS = L1 form, RHS = L0 lambda body). The frontmatter
`layer: L1>L0`, `l1_anchor`, `l0_anchor` are consistent with the edge. The single reverse-direction
(lifting) note is correctly quarantined to the report's §"Open questions / caveats" (CYCLE.md
:444-450) and explicitly marked "working-note only, NOT in the theme body" — per the high→low
discipline; it does not leak into the chapter. Edge label and prose agree exactly.

**plan-kind-consistency — pass.** Declared `status: firm` in both the chapter frontmatter and
the §Status block. The content shape matches firm: every constituent reads from a positive
source site (verified — the lambda at `:547-577`, `MatVecMult` body at `:329-347`, basis growth
at `:606-619`), no rough-in placeholders, no `partly-constructive` caveat is needed (no
sub-part is materialized from negative anchors — `lu_solve` reads from the positive
`fullPivLu().solve` site). The firm-on-positive-structure justification correctly mirrors the
operator it lowers (`nleps_deflated_residual.md:111-117`) and the interior atom
(`apply_nonlinear_pencil.md:98`): syntactic-identity laws on fully-specified positive source,
NLEPS test-coverage absence non-gating. Classification is sound.

**skill-uptake-survey — pass (non-blocking telemetry).** The report explicitly references its
mechanical-verification tooling uptake: `tools/citecheck/citecheck.py` for bounds + `--anchor`/
`--regex` token drift (CYCLE.md :370-371, :420-421), `palace-codemap read_range` for source
confirmation, and `search_text` over `test/unit/**` for the test-coverage-absence claim. The
rotation-proposal skills (`propose-rotation` / `verify-rotation-citation`) are not named, which
is appropriate — this is a structural syntactic-expansion theme, not an algebraic rotation
requiring the propose-rotation procedure. Telemetry surfaced; nothing blocking.

### Issues found

1. **Dead links in `## Speculative operators proposed` (report scaffolding).** CYCLE.md
   :410-413 — the four links `[apply_nonlinear_pencil](../../../book/src/L1/apply_nonlinear_pencil.md)`,
   `[lu_solve](../../../book/src/L1/lu_solve.md)`, `[dot](../../../book/src/L1/dot.md)`,
   `[nrm2](../../../book/src/L1/nrm2.md)` use a `../../../` prefix (three levels up) when the
   correct depth from `reports/<id>/` is `../../` (two levels). All four resolve to DEAD paths
   above the repo root; the correct `../../book/src/...` form resolves (filesystem-confirmed).
   Severity: low — these are outside the publishable `new:` fence (CYCLE.md scaffolding, never
   built into the artifact) and the same target slugs are linked correctly inside the fence, so
   the mdBook build is unaffected. Mechanical fix (change `../../../` → `../../`, or drop to
   plain-text since they duplicate in-fence links). Location: CYCLE.md §"Speculative operators
   proposed", lines 410-413.

(No other issues. The load-bearing Mult+AddMult→single-pencil-apply collapse, the Sub-pattern A
vs Sub-pattern D distinction for the `:568`/`:575` fused `linalg::Dot` calls, the arg-2-conjugation
reconciliation, the firm-on-positive-structure status, the fence-enclosure of the firm body, and
all 24 source + intra-book citations are verified correct.)

## Repair

### Fixes attempted

- **Finding**: Dead links in `## Speculative operators proposed` (report scaffolding) — CYCLE.md
  :410-413, four links use a `../../../book/src/...` prefix (three levels up) when the correct
  depth from `reports/<id>/` is `../../book/src/...` (two levels). All four resolve to dead paths
  above the repo root; outside the publishable `new:` fence so the mdBook build is unaffected.
  - **Decision**: repaired
  - **Action**: Edited CYCLE.md §"Speculative operators proposed" (lines 410-413) —
    `../../../book/src/L1/...` → `../../book/src/L1/...` on all four links
    (`apply_nonlinear_pencil`, `lu_solve`, `dot`, `nrm2`). This is the in-scope "trivial
    cross-reference fix (broken `[link]`)" repair shape: a pure path-depth correction, no content
    authored. Verified on the filesystem that all four corrected paths resolve to real files, and
    confirmed the fence count is unchanged at 22 (even parity — the edit touched no code fences).

### Unrepairable findings

None. The sole flagged finding (`cross-reference-integrity` warning) was a mechanical
link-depth defect and was repaired. All seven other checks passed at critique and required no
repair.

## Suggested resolution

`ready` — the theme passed every substantive check (citation-validity, surface-or-evidence,
rotation-quality, variant-axis-coverage, edge-label-fidelity, plan-kind-consistency,
skill-uptake-survey all `pass`; the load-bearing Mult+AddMult→single-pencil collapse and the
Sub-pattern A vs D distinction confirmed correct at source). The one low-severity
report-scaffolding broken-link defect was mechanical and is now fixed; it was outside the
publishable `new:` fence so it never affected the artifact build. No follow-up agent needed.

Integrator notes: the `new:` block (CYCLE.md :38-388), the `edit:book/src/L1-L0/index.md`
row, and the `edit:book/src/SUMMARY.md` insert (anchor = `dot-mutation-rotation` line, new row
between it and the existing `nrm2-mutation-rotation` line) are all clean and ready to apply.
