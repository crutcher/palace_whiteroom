---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T220000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T223000Z
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

# META: verification of harvester `ls_update_column` firm L1 leaf (cycle-029)

## Critique

### Checks run

**citation-validity** — **warning** (one minor off-by-one anchor; all 45 source-side citations mechanically verified). The full mechanical pass via `tools/citecheck/citecheck.py --scan CYCLE.md --quiet` returned `45 ok, 0 failing`. I then anchor-verified every load-bearing pinpoint:
- GMRES per-column-update region: `iterative.cpp:634` (`for (int k = 0; k < j`), `:636` (`ApplyPlaneRotation(Hj[k]`), `:638` (`GeneratePlaneRotation(Hj[j]`), `:639` (`ApplyPlaneRotation(Hj[j]`), `:640` (`ApplyPlaneRotation(s[j]`), `:642` (`beta = std::abs`), `:644` (`converged = (beta < eps)`) — **all zero-drift**.
- FGMRES per-column-update region (the "+1-brace-offset zone" flagged in the dispatch prompt): `iterative.cpp:813-819` (`for (int k = 0; k < j`), `:815` (`ApplyPlaneRotation(Hj[k]`), `:817` (`GeneratePlaneRotation(Hj[j]`), `:818` (`ApplyPlaneRotation(Hj[j]`), `:819` (`ApplyPlaneRotation(s[j]`), `:821` (`beta = std::abs`), `:823` (`converged`) — **all zero-drift**; the dispatch-time pre-localization correctly accounted for the brace-offset.
- Upstream boundary `iterative.cpp:629-632` (`Norml2` at :631), register split `iterative.hpp:193` (`ScalarType> s, sn`) / `:194` (`RealType> cs`), scalar kernels `:73-108` / `:112-118` / `:227-241`, RHS init `:612` (`s[0] = beta`) — **all zero-drift**.
- Book cross-refs: `concepts/incremental-least-squares.md:14` (slug contract), `:22-27` (hiding list), `plane-rotation-stream.md:21-23` (Sequential character), `L2-L1/incremental-least-squares-composition-lowering.md:307-310` (speculative-L1 entry) — **all zero-drift**.

**One drift** found: `book/src/L2-L1/incremental-least-squares-composition-lowering.md:88` cited as the "forthcoming (not yet on disk)" Face-1 forward-reference; the slug `ls_update_column` actually appears at line 87 (the sentence "The `ls_update_column` column-streaming leaf is itself **forthcoming** (not yet on disk; …" spans :87-88, with `ls_update_column` at :87 and "not yet on disk" at :88). This is `[DRIFT -1]` against the slug anchor but the substantive claim ("forthcoming") IS at the cited line. Soft warning, not a load-bearing failure.

**surface-or-evidence** — **pass**. Wholly-new leaf (`new:book/src/L1/ls-update-column.md` at line 29, plus dep-map row + SUMMARY.md registration). For a new-file proposal the surface IS the entire body; the check applies primarily to refinement-shaped edits to existing operators. The L1 index dep-map row and SUMMARY.md registration provide the surrounding-surface integration. The body is sourced from positive Palace anchors (no retroactive backfill, no pure rotation_claim without surface).

**rotation-quality** — **pass** (firm-on-positive-structure correctly judged). This is an L1 leaf harvester, not a lowering theme — the proper rotation question is whether the L1 form is strictly more compact / abstract / equational than the L0 form. The pure-functional value-bundle `{h_out, cs_j, sn_j, s_j, s_jp1, beta} = ls_update_column(variant, cs, sn, s, j, h_new)` cleanly hides the in-place four-register reference-update L0 pattern (`ApplyPlaneRotation(...)` ×3 + `GeneratePlaneRotation(...)` with `Hj` column-pointer arithmetic into the flat Hessenberg register). The L1>L0 rewrite-theme is explicitly deferred to a forthcoming `ls-update-column-mutation-rotation` theme — consistent with the "Identity-lowerings still require both L levels" methodology invariant. The replay-non-commutativity-as-LAW (law 2 at lines 293-301) vs the bit-level reduction order as a non-law is a well-grounded dual recording: rotation matrices genuinely don't commute in exact arithmetic (Q'_j ≠ Q_j), so the *structural* law-2 is sound; the *finite-precision* bit-level non-law is recorded separately and correctly. The L2 entry's own law 2 frames the same point ("**The replay-before-generate ordering is load-bearing**" at L2/incremental-least-squares.md:159-161, ":236-239") — the leaf's dual recording is consistent. PASS.

**variant-axis-coverage** — **pass**. The report enumerates three variant axes — (a) element-type / scalar-kernel (real vs complex, absorbed via `iterative.hpp:193-194` `ScalarType`/`RealType` split), (b) basis (`V` GMRES vs `Z` FGMRES, absorbed — invisible at this leaf since the per-column running-QR code is line-for-line identical at `:634-640`≡`:813-819`), (c) column-index `j` (parameterised). It explicitly scopes-out four would-be axes: no sub-step-sequence axis (Householder/two-sided alternatives scoped out per unimplemented-component policy), no collective-reduction axis (small-coordinate registers, no MPI), no reduction-strategy axis on the replay fold (strict `k=0..j-1` is load-bearing), and the basis-axis is owned by the L2 consumer. The variant-axis taxonomy is rigorous; no hidden branches.

**cross-reference-integrity** — **pass**. All cross-refs resolve on disk:
- L1 siblings: `back_solve.md`, `orthogonalize.md`, `apply_linop.md`, `lu_solve.md`, `apply_nonlinear_pencil.md`, `nrm2.md`, `dot.md` — all exist.
- L2 parent: `L2/incremental-least-squares.md` + `L2/krylov-step.md` — exist.
- L2>L1 theme: `L2-L1/incremental-least-squares-composition-lowering.md` — exists.
- Concept pages: `givens.md`, `givens_generate.md`, `givens_apply.md`, `plane-rotation-stream.md`, `incremental-least-squares.md` — all exist.

The back_solve ↔ ls_update_column distinction (terminal small-dense `R·y = s` solve vs per-column-streaming running-QR producer) is preserved cleanly throughout the body — the slug-naming distinction at `back_solve.md:30-34` ("the slug `ls_update_column` at `L2/incremental-least-squares.md:412` and `concepts/incremental-least-squares.md:14` names the DISTINCT per-column streaming update step `ls_update_column(K, j, h_new) → K'`, not this terminal back-solve") is correctly inherited as the structural precedent.

Slug/filename convention: `ls_update_column` (underscore slug) ↔ `ls-update-column.md` (hyphen filename) matches the `back_solve` / `back-solve.md` pattern (which is itself per the cycle-027 ratified convention). The L2-L1 theme's forward-ref slug `ls_update_column` (`L2-L1/.../:88,:307-310`) is preserved.

**Build-readiness guard (firm-body-inside-fence)** — **PASS**. Top-level fence enumeration shows: line 29 opens `new:book/src/L1/ls-update-column.md`, line 659 opens nested ` ```yaml ` (verified_against block), line 745 closes yaml, line 746 closes new:, line 748 opens edit:L1/index.md, line 772 closes, line 774 opens edit:SUMMARY.md, line 781 closes. Even parity (8 fences total). The `## Status` header (line 486) and full firm apparatus (`## Algebraic laws`, `## Status`, `## L1 vs L0 distinction`, `## Evidence`, complete `verified_against:` block) all sit INSIDE the outer `new:` fence (29-746). This is the same nested-yaml-fence pattern used successfully by cycle-027 `axpby-axpbypcz` (CYCLE.md lines 171-213) and bilinear-form (cycle-027) — the integrator-per-report parser pairs open/close info-strings correctly here. No fence-truncation defect. Note: cycle-024 friction-ledger documented the nested-` ```text `-fence variant as problematic, but the nested-` ```yaml ` pattern with the `verified_against:` block at the bottom of a `new:` block is the LANDED convention (cycle-026/027 precedents) and is parsed correctly.

**edge-label-fidelity** — **pass** (N/A). This is an L1 leaf-operator harvester, not a lowering theme with an L_{n+1}→L_n edge. No edge labels to verify. The deferred L1>L0 rewrite is correctly held as a forward-note for a separate `ls-update-column-mutation-rotation` theme dispatch.

**plan-kind-consistency** — **pass**. Declared kind is `firm` L1 operator. The content shape matches: full Context / Signature / Semantics / Algebraic laws (7 + 4 non-laws) / Dependencies / Variant axes / Status / L1 vs L0 distinction / Evidence sections, with a complete `verified_against:` block (24 inline entries including 11 inherited from the parent L2>L1 theme's cycle-028 audit per the `verify-citation-range` skill's Audit-report sub-case at line 832-836). The firm-on-positive-structure judgment is explicitly grounded against the established precedents (`back_solve` c027, `lu_solve` c022, `apply_linop`, `apply_nonlinear_pencil` c021), and the Status section (lines 486-523) walks through the firm-vs-rough-in-(test-coverage-bounded) judgment with the "syntactic-identity-laws-don't-test-gate" reasoning correctly applied. The Open-questions section flags the entry's own status decision (lines 906-920) explicitly for integrator/critic confirmation — appropriate self-flagging.

**skill-uptake-survey** — **pass**. The report explicitly invokes:
- `tools/citecheck/citecheck.py --anchor` per individual citation (every Evidence-section entry calls out the anchor token + verified line number — e.g. lines 567, 571, 575, 578, 582, 586, 592, 595-597, 600, 605, 609, 620, 625, 629, 633).
- `verify-citation-range` skill's "Audit-report / inherited-citation sub-case" explicitly named at line 835 (justifying the inheritance of scalar-kernel + RHS-seed + convergence-test anchors from the parent L2>L1 theme's cycle-028 `verified_against:` audit at 2026-05-29T195406Z).
- `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill explicitly named at line 529 and again at line 865 as the follow-up dispatch the L2>L1 theme's three plain-text refs should be upgraded via.

Excellent skill telemetry.

### Issues found

1. **citation-validity: minor anchor drift at `book/src/L2-L1/incremental-least-squares-composition-lowering.md:88`** (Evidence section line 641; Status section line 526; OQ section line 861). Cited as the "Face-1 forward-ref `:88`" / "forthcoming (not yet on disk)". The token `ls_update_column` appears at line **87** (off-by-one); the phrase "not yet on disk" IS at line 88. If the anchor-of-record is the slug, the line should be `:87` (or the range `:87-88`); if the anchor-of-record is the "not yet on disk" phrase, `:88` is exact. The current `:88` plus three other references (`:69`, `:307-310`) are all in-context (the Face-1 plain-text-defer region :67-90 is correct). Suggest re-targeting `:88` to `:87-88` (the slug-bearing sentence spans both) or to `:87` (the slug anchor). Severity: low (no claim invalidated; mechanical bounds-pass at line 88).

No other issues.

The dispatch's three-attempt history (socket / 63-min localization timeout / constrained third-attempt success with pre-supplied L0 anchors) shows in the report quality: the FGMRES `+1-brace-offset zone` citations all land precisely, the per-line anchor-token coverage is exhaustive (every load-bearing line called out with its anchor literal), and the slug/filename/convention adherence to the back_solve template is tight. The body is value-complete and the firm judgment is well-grounded against four established precedents.

## Repair

### Fixes attempted

- **Finding**: citation-validity warning — `book/src/L2-L1/incremental-least-squares-composition-lowering.md:88` is off-by-one against the slug `ls_update_column` anchor (token at :87; the sentence "is itself forthcoming (not yet on disk)" spans :87-88).
  - **Decision**: repaired.
  - **Action**: On-disk verification of `book/src/L2-L1/incremental-least-squares-composition-lowering.md:82-90` confirms (a) the slug `ls_update_column` appears at line 87 (`leaf). The \`ls_update_column\` column-streaming leaf is itself **forthcoming** (not yet on disk; a`), and (b) the "follow-on harvester target" continuation lives at line 88. The slug-bearing sentence spans :87-88. Per the critic's suggested repair, re-targeted all three CYCLE.md references from `:88` to `:87-88` (the slug-bearing sentence range):
    - `reports/2026-05-29T205945Z-harvester-ls-update-column-leaf/CYCLE.md:89` — Context section, "L2 theme's Face-1 forward-reference was already plain-text-deferred" — re-anchored to `:87-88,307-310`.
    - `reports/2026-05-29T205945Z-harvester-ls-update-column-leaf/CYCLE.md:526` — Status section, "Resolves the L2>L1 theme's plain-text forward-reference to Face 1" — re-anchored to `:87-88,307-310`.
    - `reports/2026-05-29T205945Z-harvester-ls-update-column-leaf/CYCLE.md:861` — Open-questions section, plain-text-ref upgrade list — re-anchored to `:87-88` and quoted-phrase clarified to the slug-bearing sentence (`"The \`ls_update_column\` ... is itself forthcoming (not yet on disk)"`) to match the broader range.
  - The `verified_against:` entry at line 729-732 references `:67-90` (the full Face-1 region) plus `:307-310` (the speculative-L1 entry) — not the off-by-one anchor — so it stays as-is.

### Unrepairable findings

None. The single warning finding was mechanical (off-by-one anchor with the critic's repair recipe explicit); no substantive content authoring required.

## Suggested resolution

`ready` for integration. The repair was surgical: three in-place anchor adjustments in CYCLE.md from `:88` → `:87-88` on the report's references to the L2>L1 theme's Face-1 forward-ref. The 7 passing checks plus the now-repaired citation-validity finding leave the report at full pass. No follow-up agent needed.

The L2>L1 theme's own plain-text references at `:69` / `:87-88` / `:307-310` remain plain text on-disk (artifact mutation is out of repair scope); per the report's Open questions section, the post-integration upgrade to live links via the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill is the intended follow-up dispatch (lifter or same-layer-cross-cutter scope).
