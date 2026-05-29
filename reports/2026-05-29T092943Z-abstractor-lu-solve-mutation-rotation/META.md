---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T10:30:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T10:45:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "L1>L0 theme sketch — lu-solve-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass.** Every L0 claim carries a `(file, line)` pointer and all were
re-verified line-exact via `palace-codemap` `read_range` / `search_text` this invocation. The 9
Eigen-solve sites verify EXACTLY: `nleps.cpp` 533 (`SS = -S.fullPivLu().solve(SS)`), 534
(`x2 = SS.fullPivLu().solve(x2)`), 535 (`MatVecMult(X, S.fullPivLu().solve(x2))`), 563
(`MatVecMult(X, S.fullPivLu().solve(vv2))`), 665 (`Sv2 = S.fullPivLu().solve(v2)`), 667
(`MatVecMult(X, S.fullPivLu().solve(Sv2))`); `romoperator.cpp` 757/758 (disabled LDLT), 765
(active `Ar.fullPivHouseholderQr().solve(RHSr)`). Supporting anchors verify: `nleps.cpp:351`
(`QuasiNewtonSolver::Solve()`), `:397` (`Eigen::MatrixXcd H;`), `:524` (`SS(k,k)`), `:532`
(`S = eig_opInv * I - H`), `:536` (`AXPY`), `:562` (`S = lam*I - H`), `:664` (`S = eig*I - H`);
`romoperator.cpp:701` (`SolvePROM`), `:717` (`Ar.resize`), `:754` (`if constexpr (false)`),
`:762-764` (stability comment, transcribed verbatim incl. the source's "to due" typo), `hpp:188-189`
(`Ar` / `RHSr` decls). The `search_text` for the four solve patterns over `palace/**/*.cpp`
returns exactly the 9 hits and **no `palace/linalg/lu.cpp`** (the only "lu" file is
`superlu.cpp`, the unrelated distributed sparse solver) — the no-dedicated-file claim is
confirmed. The producer's `:722→:723` `ProjectMatInternal` drift correction is **correct**: line
722 is `A2 = space_op.GetExtraSystemMatrix...`, 723 is `ProjectMatInternal(...)`; the chapter body
and §Verified-against consistently use `:723`. (One minor working-note typo: OQ #1 line 524 of the
report says "`Vᴴ A2 V` projection at `722`" — the chapter body itself is right at `:723`; this is in
the report's own caveat section, not the chapter, so it does not affect the artifact.)

**surface-or-evidence — pass.** This is a new-theme creation (`new:book/src/L1-L0/lu-solve-mutation-rotation.md`),
not a refinement of an existing operator/theme — it modifies surface (creates the chapter) AND
carries the L0 evidence. The retroactive-evidence sub-case does not apply. Not a pure
rotation_claim.

**rotation-quality — pass.** The mutation rotation is genuine, not a renaming: the L0 form is
strictly less abstract than L1 — it exposes (i) the transient Eigen factorization object
`A.<kernel>()` (internal pivot/permutation arrays, rebuilt per call), (ii) the `.solve()`
back-substitution, and (iii) the in-place RHS-buffer overwrite (`b = A.<kernel>().solve(b)`), all
of which the pure L1 `x = lu_solve(A, b)` hides. The L1→L0 direction adds destination-aliasing +
factorization-state that L1 abstracts away — a true rotation of the mutation/state-hiding
impedance, parallel to the BLAS-1 sibling themes.

**variant-axis-coverage — pass.** The §Variant axes section enumerates four axes and classifies
each: factorization-kernel (load-bearing — LU / QR / rejected LDLT, all positively witnessed),
single-vs-multi-RHS (absorbed-as-form, both witnessed), in-place-vs-fresh-destination (absorbed
transparent trick, both witnessed at `:533`/`:765` vs `:665`/`:535`), element-type
(complex-witnessed / real-permitted-but-unwitnessed, explicitly scoped). No hidden branch — the
`fullPivLu` / `fullPivHouseholderQr` / `ldlt` split is the kernel axis and is exhaustively covered;
`classify-variant-axis` is invoked (line 423).

**cross-reference-integrity — FAIL (build-readiness guard).** All `[link]` targets resolve (the
six L1-L0 siblings, `../L1/lu_solve.md`, `../L1/apply_linop.md`, `../L1/ksp_solve.md`,
`../L2/deflate.md`, `../L2/gram.md` all exist on disk; the index.md and SUMMARY.md anchor rows
match the producer's quoted context exactly). **However, the build-readiness fence guard fails:**
the `firm` chapter body is authored with **nested triple-backtick ` ```text ` fences INSIDE the
` ```new: ` block** (report lines 69-74, 96-100, 112-123, 180-193) rather than as the 4-space
indented code blocks the landed L1-L0 chapters use (verified: `dot-mutation-rotation.md` and the
landed `assemble-diagonal-mutation-rotation.md` report both use indented code inside the
proposed-changes fence and contain ZERO inner ` ``` ` fences). The 14 fences pair under a flat
CommonMark toggle as (37→69),(74→96),(100→112),(123→180),(193→462),(464→468),(474→478) — i.e. the
`new:book/.../lu-solve-mutation-rotation.md` block opened at line 37 is **closed by the first
inner ` ```text ` at line 69**, so an integrator extracting the block by fence-toggle captures
only report lines 38-68 (title + intro + `## Slug` + the opening of `## L1 form`). The ENTIRE firm
apparatus — `## L0 form (RHS)`, Sub-patterns A & B, every citation list, §The factorization-kernel
axis, §Applicability conditions, §Variant axes, and crucially **`## Status` (report line 441)** —
falls OUTSIDE the captured `new:` block. This is the cycle-019 fence-truncation defect signature
(friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence`): a `firm`-claimed
chapter whose `## Status` + Signature + Algebraic-laws-reference + Evidence are not enclosed in the
proposed-changes fence. Flagged `fail` per the firm-body-inside-fence guard.

**edge-label-fidelity — pass.** The edge is L1>L0 (mutation rotation). The prose narrates exactly
that edge FORWARD: LHS = L1 `x = lu_solve(A, b)`, RHS = L0 `b = A.<kernel>().solve(b)` (skeleton
at report lines 96-100; per-sub-pattern at A `:533-535` and B `:765`). No reverse (L0→L1 lifting)
language appears inside the chapter body (lines 38-461). The single reverse-direction note (the
lifting prerequisites) is correctly quarantined in the report's `## Open questions / caveats` OQ #4
(line 537), OUTSIDE the chapter — exactly per the high→low discipline.

**plan-kind-consistency — pass.** Declared kind is an L1>L0 theme with `status: firm`; content
shape matches — exhaustive positive citations at the only two L0 use families, a structural
justification, no rough-in placeholders, no speculative L1 operators (correctly "None", since the
kernel is a contracted variant axis of the already-firm `lu_solve`, not new vocabulary). The
`firm` (not `partly-constructive`, not `rough-in (test-coverage-bounded)`) decision is internally
justified and consistent with the L1 operator's firm-on-positive-structure precedent: the
kernel-axis load-bearing recording is read off POSITIVE source (active LU/QR + the disabled-but-
present LDLT + the "for maximal stability" comment), not a negative-anchor reconstruction; and the
laws are syntactic identities on `A⁻¹`, not convergence facts, so the absent solve unit test does
not gate them. Classification is sound.

**skill-uptake-survey — pass.** The theme's shape (variant-axis classification + citation-range
verification) implies `classify-variant-axis` and `verify-citation-range`; both are referenced
(report lines 423 and 363 respectively). Telemetry only, non-blocking.

### Issues found

1. **[FAIL — cross-reference-integrity / build-readiness fence guard] Nested triple-backtick
   fences inside the `new:` block truncate the firm chapter body.** CYCLE.md, `## Proposed
   changes` → `new:book/src/L1-L0/lu-solve-mutation-rotation.md` (block opens line 37). The four
   inner ` ```text ` fenced code blocks (lines 69-74, 96-100, 112-123, 180-193) are nested inside
   the outer ` ``` `-delimited `new:` block. Under flat CommonMark fence-toggle parsing the outer
   block is closed by the first inner ` ``` ` at line 69, so only report lines 38-68 are captured
   as the file body; `## Status` (line 441) and the entire firm apparatus (§L0 form, both
   sub-patterns, all citations, §factorization-kernel axis, §Applicability conditions, §Variant
   axes) land OUTSIDE the fence. Severity: HIGH (the firm chapter would be written truncated to its
   intro, or the integrator would mis-parse the trailing sections as report-level content). The
   landed-sibling fix pattern: convert the four inner ` ```text ` blocks to 4-space-indented code
   blocks (as in the landed `dot-mutation-rotation.md` and the landed
   `assemble-diagonal-mutation-rotation.md` report), leaving a single outer fence pair for the
   `new:` block.

2. **[Minor — citation-validity, working-note only] OQ #1 internal line-number inconsistency.**
   CYCLE.md `## Open questions / caveats` OQ #1 (line 524) says "the `Vᴴ A2 V` projection at
   `722`"; the verified site is `:723` (`ProjectMatInternal`), and the chapter body + §Verified-against
   both correctly use `:723`. The discrepancy is confined to the report's own caveat text (not the
   artifact). Severity: LOW (cosmetic; does not affect the chapter or any cited claim).

3. **[Informational — out-of-scope, no action required] Pre-existing `lu_solve.md:103`
   approximation.** The firm L1 operator file cites the ROM assembly `Ar += Kr + iω Cr − ω² Mr +
   Vᴴ A2 V` at `:728-735`; verified active lines are `729`/`732`/`734` with the `Vᴴ A2 V`
   projection at `:723` — so the range under-shoots the projection and is off-by-one at the lower
   bound. The producer correctly identified this as a ±few-line approximation, flagged it as a
   working-note OQ for a future lifter/harvester citation-tightening pass on `lu_solve.md`, and did
   NOT edit that file (it is outside this theme's write-authority). The critic AGREES this is
   out-of-scope for this dispatch — `book/src/L1/lu_solve.md` is not in the theme's proposed-changes
   set, and editing it would breach the abstractor write-partition. No action for this report.

## Repair

### Fixes attempted

- **Finding 1**: [FAIL — cross-reference-integrity / build-readiness fence guard] Nested
  triple-backtick ` ```text ` fences inside the `new:book/src/L1-L0/lu-solve-mutation-rotation.md`
  block (CYCLE.md lines 69-74, 96-100, 112-123, 180-193) truncate the firm chapter body under flat
  CommonMark fence-toggle parsing — the first bare inner ` ``` ` closes the `new:` block early,
  leaving `## Status` and the entire firm apparatus outside the captured content.
  - **Decision**: repaired
  - **Action**: Converted all four nested ` ```text … ``` ` code blocks inside the
    `new:` block to **4-space-indented code blocks** (the landed sibling pattern verified in
    `book/src/L1-L0/dot-mutation-rotation.md`, e.g. its §"L1 form" / §"L0 form" indented samples,
    which contain zero inner fences). Edits applied to
    `reports/2026-05-29T092943Z-abstractor-lu-solve-mutation-rotation/CYCLE.md`:
    (i) §"L1 form (LHS)" signature block, (ii) §"L0 form (RHS)" common-skeleton block,
    (iii) §"Sub-pattern A" NLEPS code block, (iv) §"Sub-pattern B" ROM code block. Content
    preserved verbatim — only the fence mechanism changed (` ```text ` → 4-space indent). This is
    a mechanical, surgical fix per the SIDEWAYS/fence-mechanism repair authority; no substantive
    content was authored.
  - **Verification**: post-conversion the CYCLE.md has exactly **6** triple-backtick fences, all
    paired: `new:…/lu-solve-mutation-rotation.md` opens line 37 → closes line 454;
    `edit:book/src/L1-L0/index.md` opens 456 → closes 460; `edit:book/src/SUMMARY.md` opens 466 →
    closes 470. Zero bare inner fences remain inside the `new:` block. The `## Status` header (now
    line 433) and the full firm apparatus (§L0 form, Sub-patterns A & B, all citation lists,
    §The factorization-kernel axis, §The in-place RHS overwrite, §Applicability conditions,
    §Justification kind, §Speculative L1 operators, §Verified-against, §Variant axes) are all
    inside the `new:` block (< line 454). The report-level sections (§Speculative operators
    proposed, §Supporting evidence, §Open questions/caveats) correctly fall after the closing
    fence. The two `edit:` blocks are intact and balanced.

- **Finding 2**: [Minor — citation-validity, working-note only] OQ #1 internal line-number
  inconsistency — CYCLE.md §"Open questions / caveats" OQ #1 said "the `Vᴴ A2 V` projection at
  `722`"; the verified site is `:723` (`ProjectMatInternal`), and the chapter body + §Verified-against
  both already use `:723`.
  - **Decision**: repaired
  - **Action**: Changed `722` → `723` in CYCLE.md §"Open questions / caveats" OQ #1. Trivial
    off-by-one citation-line correction within the report's own caveat text (not the artifact),
    aligning the working note with the chapter body's already-correct `:723`. Mechanical fix
    within repair authority.

- **Finding 3**: [Informational — out-of-scope, no action required] Pre-existing
  `lu_solve.md:103` ROM-assembly citation approximation (`:728-735` vs verified `:723`/`729`/`732`/`734`).
  - **Decision**: not-needed
  - **Rationale**: The critic itself agreed this is out-of-scope — `book/src/L1/lu_solve.md` is
    not in this theme's proposed-changes set, and editing it would breach the abstractor
    write-partition. The producer correctly quarantined it as a working-note OQ for a future
    lifter/harvester citation-tightening pass. No repair action; not a defect in this report.

### Unrepairable findings

None. The single FAIL (cross-reference-integrity fence guard) was a mechanical fence-mechanism
defect — exactly the SIDEWAYS/fence-conversion shape in repair authority — and was repaired
in place. No substantive authoring was required: the theme content itself passed all seven other
checks (citation-validity, surface-or-evidence, rotation-quality, variant-axis-coverage,
edge-label-fidelity, plan-kind-consistency, skill-uptake-survey).

## Suggested resolution

`overall_status: ready`. The fence-truncation defect was the only blocker, and it is now fixed:
the firm chapter body (Context through Status through Verified-against through Variant axes) is
unambiguously enclosed in a single `new:` fence pair, so the integrator will extract the complete
firm chapter — not a truncated intro. Notes for the integrator:

- The `new:book/src/L1-L0/lu-solve-mutation-rotation.md` block now lands the chapter with
  4-space-indented code samples (rendered as code blocks by mdBook), matching the landed
  `dot-mutation-rotation.md` / `assemble-diagonal-mutation-rotation.md` sibling convention.
- The two `edit:` blocks insert the dep-map row in `book/src/L1-L0/index.md` (after the
  `assemble-diagonal-mutation-rotation` row) and the `SUMMARY.md` chapter entry (after the
  `matrix-weighted-norm-mutation-rotation (stub)` entry).
- Finding 3 (the `lu_solve.md:103` ±few-line citation approximation) is a standing working-note OQ
  for a future lifter/harvester citation-tightening pass on the L1 operator file — out of scope
  for this theme's write-authority, correctly not touched.
