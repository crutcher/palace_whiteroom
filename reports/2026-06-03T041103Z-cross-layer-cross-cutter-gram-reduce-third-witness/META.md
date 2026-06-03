---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T05:10:00Z
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
repaired_at: 2026-06-03T05:40:00Z
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

# META: verification of "Cross-layer observation — gram_reduce has NO clean 3rd witness"

## Critique

### Checks run

**citation-validity — warning.** `citecheck.py --scan` reports 17 ok / 0 failing: every cited range is in-bounds and every path is hygienic. The enclosing-range citations are all correct and content-grounded (anchor-confirmed: `eigensolver.cpp:424-471` `num_conv`/`GetEigenvalue`/`GetEigenvector` ok; `lumpedportoperator.cpp:283-294` `GetSParameter` ok; `postoperator.cpp:1246-1308` `MeasureSParameter` ok; `gram_reduce.md:75-115` `symmetric_from_upper`, `:178-182` `Candidate`, test anchors `364-367`/`717-720` all ok). I meaning-read the two load-bearing source regions and both fully support the negative finding (see surface-or-evidence below). The warning is for **pinpoint-line drift inside correctly-bounded ranges**, not for any fabricated or unsupported evidence — see issues below.

**surface-or-evidence — pass.** This is an observation-only probe, not a refinement of an operator's surface, so the refinement-shape rule applies loosely; the load-bearing question is whether the negative finding (the symmetric-Gram shape does NOT positively hold) is *established* rather than asserted. It is, decisively. I read `postoperator.cpp:1172-1221` (`MeasureLumpedPortsEig`): the Q-factor is `Q_mj = freq_re / |mode_port_kappa|` with `κ = ½R·|I_mj|²/energy_electric_all` (lines 1197-1202) — a per-mode self-energy scalar quotient inside a single-mode port loop, with NO cross-mode `Eⱼᵀ K Eᵢ` term anywhere. I read `postoperator.cpp:1246-1308` (`MeasureSParameter`) and `lumpedportoperator.cpp:283-294` (`GetSParameter`): `dot = (*s)·E` is verbatim "the projection of the field onto the port mode" (comment line 285), a single-vector linear functional, not a two-member bilinear; the assembly is one-drive-column-per-solve (`drive_port_idx = measurement_cache.ex_idx`); and the three symmetry breaks are all present in source — inhomogeneous diagonal `S.real() - 1.0` (lines 1275/1297), directional `*= sqrt(src_data.R / data.R)` (line 1280), and per-endpoint de-embedding phases (lines 1301-1302). The finding is correctly conservative: it refuses the subsume on positive-shape-failure grounds (wrong rank for (a); linear-not-bilinear + asymmetric assembly for (b)), exactly the over-unification hazard the OQ named.

**rotation-quality — pass (not applicable to observation-only report).** No algebraic/structural rotation is asserted; this is a refutation of a *candidate* unification, not a layer-to-layer rotation claim. The report explicitly declines to broaden `gram_reduce` and proposes no new equational form.

**variant-axis-coverage — pass.** The two candidate witnesses ARE the two orthogonal axes under probe (eigenmode Q-factor; driven S-parameters), and both are explicitly covered and dispositioned (NON-MATCH each, with a stated reason). Gate step-2 ("classify break-witnesses as scope boundaries, never variant axes") is applied: the report explicitly refuses to fold either candidate into a `w`-closure variant axis. No hidden branch — the report even names the un-read wave-port `GetSParameter` body (`waveportoperator.cpp:780`) as an explicit scope-out caveat.

**cross-reference-integrity — pass.** All referenced slugs/files resolve: `book/src/L4/gram_reduce.md` (exists, 283 lines), the skill `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md`, the OQ entry at `open-questions.md:930`, and the two deferred-column OQs (lines 930/932) all present. The optional proposed-changes REPLACE block's "REPLACE:" text matches the on-disk `gram_reduce.md:178-182` paragraph verbatim, so it would apply cleanly. No firm-body-inside-fence concern (this is not a firm-chapter authoring report); fence parity in CYCLE.md is even (2 fences, balanced).

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried; this is an L4-internal combinator-witness probe reaching down to L0/L1 evidence sites. The prose direction (L4 `gram_reduce` shape tested against L0 source + L1 `bilinear-form`/`matrix-weighted-norm` folds) is internally consistent.

**plan-kind-consistency — pass.** Declared kind is observation-only (cross-layer-cross-cutter spine finding). Content matches: the report records a boundary, does NOT author a `gram_reduce` broadening, does NOT add a combinator/variant-axis edit. The single proposed-changes block is explicitly OPTIONAL and is a one-paragraph in-place REPLACE recording the negative discharge — an OQ-discharge note, not a combinator edit. A non-match correctly does not license an over-broad subsume; the report routes each deferred output-product column to its OWN reduction verb (`sparameter_reduce`, the per-mode Q-ratio map) as separate future mining targets, not as `gram_reduce` cases. Correct classification.

**skill-uptake-survey — pass.** The report cites `disciplined-cross-pipeline-combinator-mining-gate` and walks its 4 steps explicitly (step-1 positive-shape-check-FIRST, step-2 break-witness-as-scope-boundary, step-3 fold-vs-map flag, step-4 replace-and-propagate N/A). It also cites `verify-citation-range`-equivalent codemap verification. Skill uptake is present and load-bearing to the disposition.

### Issues found

1. **Pinpoint-line drift in the S-parameter inner citations (CYCLE.md §"Candidate (b)" + §Supporting evidence; severity: low — cosmetic, evidence is sound).** Several inner pinpoint line numbers cited *within* the correctly-bounded `MeasureSParameter` range (`postoperator.cpp:1246-1308`) are off:
   - Diagonal `-1` self-term: report cites `:1284` (lumped) — actual `S.real() - 1.0` is at **line 1275** (lumped) and **1297** (wave). Report's wave cite `:1296` is off-by-1 (→1297); the lumped cite `:1284` is off-by-9 (→1275). Note `:1284` is actually the `S[idx][drive]` print/format line.
   - Directional generalized-S scaling `*= sqrt(src_data.R / data.R)`: report cites `:1290` — actual is **line 1280** (off by 10).
   - `drive_port_idx = measurement_cache.ex_idx`: report cites `:1280` — actual is **line 1263** (off by 17).
   The de-embedding pair `:1301-1302` is correct. These are pinpoint drifts inside a correct enclosing range; the *content* at each is fully grounded (I confirmed every claim by direct read), so the negative finding does not rest on any false anchor. Candidate for mechanical pinpoint correction by the repairer (anchor-confirmed corrected lines in hand above).

2. **`MeasureLumpedPortsEig` function-name anchor sits 2 lines above the cited range (CYCLE.md §Supporting evidence, `postoperator.cpp:1174-1217`; severity: very low).** `citecheck --anchor 'MeasureLumpedPortsEig'` reports the function decl at line 1172, `-2` outside the cited `:1174-1217`. The cited range is the function *body* (correctly bounded for the Q-factor content the report relies on — `κ`/`Q`/`p` at 1197-1218), so this is a labeling nuance rather than a drift: the report cites the body range, not the decl line. If a precise function-span citation is wanted, `:1172-1215` (or extend to 1221 to enclose the inductive branch) is the anchor-suggested form. Not a content defect.

3. **Inner participation-ratio pinpoints shifted by ~the same offset as the function (CYCLE.md §"Candidate (a)"; severity: very low — informational).** The report's `:1188-1191` (`Q_mj`), `:1183-1191` (`κ_mj`), `:1210-1217` (`p_mj`) are all in-bounds and the comment-block formulas they cite ARE in those neighborhoods (the `κ_mj`/`Q_mj` comment is at 1189-1191; the actual compute is at 1197-1202; the `p_mj` comment at 1211 with compute at 1217). The cites land on the comment/formula lines rather than the compute lines, which is acceptable for a shape-finding (the formula comment IS the semantic witness), but a repairer may wish to note the compute-line pinpoints (1197-1202 for κ/Q, 1217 for p) for precision. No correctness impact.

Net: the negative finding is well-established and correctly conservative; the only actionable issue is the mechanical pinpoint-line drift in the S-parameter inner citations (issue 1), all within correctly-bounded ranges with anchor-confirmed corrections available.

## Repair

### Fixes attempted

- **Finding (issue 1)**: Pinpoint-line drift in the S-parameter inner citations (CYCLE.md §"Candidate (b)" + §Supporting evidence) — four inner pinpoints off inside the correctly-bounded `MeasureSParameter` range.
  - **Decision**: repaired
  - **Action**: Hand-Read `reference/palace/palace/models/postoperator.cpp:1255-1308` (the `MeasureSParameter` lumped + wave loops) and confirmed all four corrected pinpoints against source, then applied the corrections in two CYCLE.md sections (§"Candidate (b)" prose enumeration + §Supporting evidence list):
    - `drive_port_idx = measurement_cache.ex_idx`: `:1280` → **`:1263`** (source line 1263, the assignment after the single-driving-port comment).
    - diagonal `vi.S.real() - 1.0` lumped: `:1284` → **`:1275`** (source line 1275, inside `if (idx == drive_port_idx)`); wave: `:1296` → **`:1297`** (source line 1297).
    - directional `vi.S *= std::sqrt(src_data.R / data.R)`: `:1290` → **`:1280`** (source line 1280).
    - de-embedding pair `:1301-1302` left unchanged (already correct — confirmed at source 1301-1302).
  - **Rationale (mechanical)**: pure pinpoint-offset corrections inside an already-correct enclosing range; the content at each line is exactly what the report claims (verified by direct read), so no substantive content authored — anchor-fix only.

- **Finding (issue 2)**: `MeasureLumpedPortsEig` function-name anchor 2 lines above the cited `:1174-1217` body range (severity very low).
  - **Decision**: not-needed
  - **Rationale**: the critic itself classified this as a labeling nuance, not a drift — the report deliberately cites the function *body* range carrying the Q-factor content, not the decl line. No false anchor; no correction warranted.

- **Finding (issue 3)**: participation-ratio inner pinpoints (`:1188-1191`/`:1183-1191`/`:1210-1217`) land on comment-formula lines rather than compute lines (severity very low, informational).
  - **Decision**: not-needed
  - **Rationale**: all cites are in-bounds and the comment-block formulas they land on ARE the semantic witnesses for a shape-finding (the formula comment IS the per-mode scalar-ratio evidence). The critic flagged this as no-correctness-impact informational; correcting comment→compute pinpoints would be a precision preference, not a mechanical anchor fix, and is not required for the negative finding to hold.

### Unrepairable findings

None. The single actionable finding (pinpoint drift) was mechanically repairable; the two further items are acknowledge-not-repair very-low-severity informational notes the critic did not flag as defects.

## Suggested resolution

`ready`. The negative/observation-only finding (`gram_reduce` has no clean 3rd witness; both candidates are NON-MATCHES on positive-shape grounds) is sound and does not rest on any false anchor — the repaired pinpoints were cosmetic offsets inside correctly-bounded enclosing ranges. For the integrator: the report's substantive output is the OQ discharge (already append-only) + the report itself; the single proposed-changes block is explicitly OPTIONAL (a one-paragraph in-place `gram_reduce.md` §Specialization note recording the CLOSED-NEGATIVE discharge) and cites only correct enclosing ranges, so it remains apply-clean if the integrator chooses to land it. No `book/` mutation was performed in this repair pass.
