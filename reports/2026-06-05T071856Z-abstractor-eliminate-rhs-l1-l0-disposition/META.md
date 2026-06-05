---
verifies: ../REPORT.md
critiqued_at: 2026-06-05T073500Z
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

# META: verification of "L1>L0 theme disposition — eliminate-rhs-mutation-rotation (SPLIT vs FOLD)"

## Critique

### Checks run

**citation-validity — pass (LOAD-BEARING, verified at the tool + meaning level).** The single
load-bearing L0 citation `reference/palace/palace/linalg/rap.cpp:56-82` (`ParOperator::EliminateRHS`)
was re-verified by `citecheck --anchor 'EliminateRHS'` → `[ok]` (anchor at lines 56, 58 within range)
and by a `read_range` of 56-85: the function opens at 56, `tx = 0.0`+`SetSubVector(tx, dbc_tdof_list, x)`
at 62-63, `GetProlongationMatrix()->Mult(tx, lx)` at 64, `A->Mult(lx, ly)` at 69,
`RestrictionMatrixMult(ly, ty)` at 72, `b.Add(-1.0, ty)` at 73, `DIAG_ONE` `SetSubVector(b,...,x)` at 76,
`DIAG_ZERO` `SetSubVector(b,...,0.0)` at 80, closing `}` at 82, `ParallelAssemble` begins at 84 — every
per-line cite in the new sub-section matches source exactly. The witness `PtAP_K->EliminateRHS(X, RHS)`
is at `laplaceoperator.cpp:252` (confirmed; `GetExcitationVector` spans 225-252). The covering-theme
back-references resolve: the L1-form `eliminate_rhs` block is at `:78-84`, the L0-form step-5 EliminateRHS
body walk at `:122-128`, the algebraic decomposition in §"What lifts cleanly" at `:217-218`, the
frontmatter `lowers:` naming `L1/eliminate_rhs (firm c055)` at `:5`, and the rap.cpp Verified-against
cite at `:207` — all on-disk-confirmed. No proposed `verified_against:` YAML block in this report, so the
round-trip sub-check no-ops.

**surface-or-evidence — pass.** This is a disposition + an evidence-backed surface change. The new
anchored sub-section "The `eliminate_rhs` leg (folded here)" modifies surface (the firm covering theme
gains a named section) AND carries the rotation_claim evidence (the rap.cpp:62-80 body walk, fully
cited). The two L1-entry corrections (`lowers_to:` re-point, §"Downward to L0" rewrite) are retroactive
defect repairs against a now-existing covering theme — allowed. No record is newly named in a signature
(the `eliminate_rhs(K, x_bc, b, policy)` signature is authoritative in the existing firm L1 entry, not
introduced here; `DiagonalPolicy` is an existing variant-axis enum, not a new record), so the
record-definition sub-check finds nothing to flag.

**rotation-quality — pass.** The FOLD call is correct under the VOCABULARY-SHIFT REDIRECT anti-mirror
rule: a dedicated `eliminate-rhs-mutation-rotation.md` sibling would be a degenerate identity-in-named-
terms split on the *same* FE-BC-elimination rotation, *same* L0 witness (`GetExcitationVector`/
`GetStiffnessMatrix`), *same* L0 file (`rap.cpp`), narrated alongside its operator-side partner — exactly
the smell the redirect names. The new sub-section is a genuine consolidation (the full rap.cpp body
walk + the in-place→pure mutation rotation, with the prolong/apply/restrict round-trip absorbed into one
`apply_linop` and `b.Add`+`SetSubVector` absorbed into the value-returning `b − K·x_bc` + pin), NOT a
1:1 mirror of the L1 entry. The rotation it documents is strictly more compact at L1 (state-hiding:
five pooled MFEM scratch vectors + in-place `b` → one pure value). The disposition is the honest "the
vocabulary did not need a second theme" call.

**variant-axis-coverage — pass.** The two variant axes of `eliminate_rhs` (`diagonal-policy`
DIAG_ONE/DIAG_ZERO; `bc-data-homogeneity`) are both covered in the new sub-section: the policy branch
appears as the `:76`/`:80` essential-row-pin bullet (both arms), and homogeneity is implicit in the
`K·x_bc` term. No hidden branch. The `operator-true-dof-representation` absorbed axis is correctly
narrated as the prolong/restrict round-trip realizing one `apply_linop`. (A folded sub-section inherits
the full axis treatment from the firm L1 entry; nothing is silently dropped.)

**cross-reference-integrity — pass (load-bearing for this disposition).** The dangling
`L1/eliminate_rhs.md` `lowers_to: L1-L0/eliminate-rhs-mutation-rotation` edge points at a file confirmed
NOT to exist (`ls` → no such file); the re-point targets `L1-L0/fe-operator-assemble-mutation-rotation`,
which exists and is `status: firm` — resolving the dangling edge to a real firm target. The sibling
precedent is exact: `L1/eliminate_essential_bc.md` already carries
`lowers_to: L1-L0/fe-operator-assemble-mutation-rotation` (confirmed at its line 5). The new sub-section
heading "The `eliminate_rhs` leg (folded here)" does NOT already exist in the covering theme (grep empty)
— a genuine new anchor, not a collision. The five forward-ref de-stale sites were each confirmed on disk:
`L1/eliminate_rhs.md` line 46 + §"Downward to L0" (271-279); `L4/eliminate_bc.md:312`;
`L4-L3/bc-elimination-post-composition-dissolution.md:78-82`; `L4-L3/index.md` lines 15 AND 46 (the exact
phrase "RHS-side `eliminate-rhs-mutation-rotation` (forthcoming)" grep-matches both). No NEW dangling
reference is introduced (every replacement points at the now-existing covering-theme anchor). The
graded-stack rank check holds: `eliminate_rhs` (firm, rank 3) → `fe-operator-assemble-mutation-rotation`
(firm, rank 3), `rank(u) ≤ rank(v)` (3 ≤ 3), and the FOLD adds no node so the HARD-gate-new has nothing
to admit.

**edge-label-fidelity — pass.** The proposal's edges are L1>L0 (the `lowers_to:` re-point and the folded
sub-section are L1→L0) and the de-stale touches at L4/L4-L3 reference the L1→L0 half explicitly (e.g.
"the L1→L0 halves are ... the RHS-side ... folded into ..."). The prose at each site discusses exactly
the edge its label names; no L-level mismatch.

**plan-kind-consistency — pass.** Declared kind is an abstractor disposition (SPLIT-vs-FOLD) resolving to
FOLD — content shape matches: no new theme/operator authored (§"Speculative operators proposed: None"),
the changes are an anchored consolidation into firm content + edge/staleness repair. This is a disposition
+ fold, correctly classified; not mis-tagged as a `firm` new-theme entry.

**skill-uptake-survey — pass (telemetry).** The report references `citecheck --anchor` invocation in its
§Supporting evidence, the appropriate skill for the load-bearing citation re-verification. No other skill
is implied by the disposition shape (no variant-axis classifier needed beyond the inherited axes; no
firm-body-fence guard since no new firm body is fenced). Telemetry adequate.

### Issues found

No blocking or warning issues. The report is internally consistent, every load-bearing citation is
tool-verified, the FOLD disposition is correctly reasoned under the anti-mirror rule, and the dangling
edge + five staleness sites are accurately located and resolved to a real firm target.

Two non-blocking observations (NOT defects — recorded for the integrator, already self-flagged by the
report):

- **Cross-scope edits (correctly flagged).** The `L4/eliminate_bc.md:312`,
  `L4-L3/bc-elimination-post-composition-dissolution.md:78-82`, and `L4-L3/index.md:15,46` de-stale edits
  touch content authored by the already-integrated cycle-101 D1 dispatch. The report self-flags these for
  integrator reconciliation and correctly identifies the load-bearing subset as (1) the covering-theme
  sub-section + disposition note and (2) the `L1/eliminate_rhs.md` edge re-point + §"Downward to L0"
  rewrite. I confirmed the only co-batch report touching the `eliminate_bc` surface
  (`layer-intro-author-l4-cohort-bullets`) edits `book/src/L4/index.md`, NOT these same lines — so there
  is no line-level write collision within the cycle-103 batch. The cross-scope edits are mechanical
  forward-ref corrections, defensible to apply or to defer.

- **Phantom slug noted in passing (correct, not a defect).** The report's §"Downward to L0" replacement
  also removes the phantom `eliminate-essential-bc-mutation-rotation` slug at `L1/eliminate_rhs.md:277`
  (the operator-side leg is likewise folded into `fe-operator-assemble-mutation-rotation`, confirmed by
  the sibling `eliminate_essential_bc.md` `lowers_to:`). This is an accurate incidental cleanup, not an
  over-reach.
