---
verifies: ../CYCLE.md
critiqued_at: 2026-05-30T012500Z
critic_version: 1
checks:
  citation-validity: fail
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-30T013500Z
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

# META: verification of "Audit bilinear-form-mutation-rotation"

## Critique

### Checks run

**citation-validity — fail.** Ran `python3 tools/citecheck/citecheck.py --scan reports/<id>/CYCLE.md --quiet` which reports `39 ok, 1 failing (40 citations checked)`. The single failing citation is `operator.cpp:613-614` at CYCLE.md:346 (the row-4 note body for `palace/linalg/operator.cpp:621-629`): the basename `operator.cpp` matches both `reference/palace/palace/linalg/operator.cpp` and `reference/palace/palace/fem/libceed/operator.cpp`, so citecheck refuses it as ambiguous. This is doubly load-bearing because the bare-basename form is embedded INSIDE the proposed `verified_against:` YAML block that the integrator will append to the firm theme — i.e. the ambiguous citation would land in the on-disk artifact. Spot-checks of the eight load-bearing pinpoints (`operator.hpp:386-394 --anchor 'Compute the bilinear form'` -> [386, 391]; `operator.cpp:621-629 --anchor 'ComplexVector Ax'` -> [624]; `operator.cpp:631-638 --anchor 'A.Mult(x, Ax)'` -> [636]; `boundarymodeoperator.cpp:85 --anchor 'linalg::Dot'` -> [85]; `:90 --anchor 'linalg::Dot'` -> [90]; `:88-89 --anchor 'ComplexWrapperOperator'` -> [88]; `nleps.cpp:672-675 --anchor 'linalg::Dot(GetComm(), w, w0)'` -> [675]; `matrix-weighted-norm-mutation-rotation.md:194-196 --anchor 'caller-owned'` -> [194]) all land mechanically clean — every individual pinpoint the audit makes IS exact. The fail is the bare-basename mode of the parallel-structure reference, not a pinpoint-drift defect.

Separately, a second citation-channel-format defect is present: the proposed `verified_against:` YAML block does NOT round-trip through `yaml.safe_load`. Rows 17 (CYCLE.md:398) and 19 (CYCLE.md:406) have `note:` values that begin with a single-quote character (`note: 'The conjugation asymmetry — the core theme content'; the inherited reconciliation...` and `note: 'Mutation-free matrix-weighted inner-product reduction α = xᴴ M y'; the L1 closed form the theme lowers`). YAML interprets a leading `'` as opening a single-quoted scalar, then the trailing prose after the closing `'` causes `expected <block end>, but found '<scalar>'`. Confirmed by extracting the `~~~yaml` block and running `yaml.safe_load`: ParserError at line 69 column 63 (the second occurrence). The report's Summary explicitly claims "no leading-double-quote note values (yaml.safe_load hazard avoided)" — but the hazard is actually leading-quote-character (single or double), and these two single-quoted rows trip it. The block as proposed would land an unparseable metadata appendage.

**surface-or-evidence — pass.** This is a pure audit (no surface change to the firm theme; only an append of a `verified_against:` metadata block). The audit-report shape is the recognised retroactive-evidence backfill mode for lowering-verifier dispatches; the bar is no over-claiming. The two load-bearing semantic claims of the underlying theme — the conjugation-asymmetry reconciliation and the workspace-ownership distinction — are both genuinely evidence-grounded: the conjugation reconciliation cites both the L0 source comment "Compute the bilinear form inner product yᴴ A x" (`operator.hpp:386, :391`, verified verbatim on-disk) AND the inherited reconciliation in `dot-mutation-rotation` §189 + `L1/dot.md:43, 104-105` (verified); the workspace-ownership distinction is bidirectionally cross-attested in `matrix-weighted-norm-mutation-rotation.md:194-196` (verified on-disk — the sibling cites THIS theme's internal-`Ax` allocation at `operator.cpp:621-639`, which I read against the on-disk source at lines 621-638 and confirmed exact). The c029 repairer's two corrections (composition identity `dot(x, apply_linop(M,y))` at `L1/bilinear-form.md:111-117` and Atn span `:88-89`) both land on-disk verbatim as the audit claims.

**rotation-quality — pass.** Not applicable to an audit; the audit assesses an already-firm rotation, it does not propose a new rotation. The underlying theme's rotation (L1 `bilinear_form(x, M, y) = xᴴ M y` → L0 `linalg::Dot(comm, x, A, y)` with internal Ax workspace + arg-swap to reconcile conjugation conventions) is a genuine algebraic-equivalence-with-state-introduction lowering, not a rename. Audit does nothing to weaken that.

**variant-axis-coverage — pass.** The audit walks all 7 stated applicability conditions in §"Applicability conditions" and explicitly notes the M-symmetry-property axis (Hermitian Bttr, non-Hermitian Atn) is covered by both in-tree callsites; the element-type axis (real-A Sub-pattern A vs complex-A Sub-pattern B) is covered structurally with the honestly-recorded coverage gap that Sub-pattern A real-A has no in-tree caller (caveat 2 in §"Open questions / caveats", consistent with the L1 entry's `rough-in (test-coverage-bounded)` status). No hidden branches; the unwitnessed real-A overload is acknowledged, not silently elided.

**cross-reference-integrity — pass.** All 6 named cross-links resolve on-disk: `book/src/L1/bilinear-form.md`, `book/src/L1/dot.md`, `book/src/L1/apply_linop.md`, `book/src/L1-L0/apply-linop-mutation-rotation.md`, `book/src/L1-L0/dot-mutation-rotation.md`, `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md`. The chapter under audit is wired into `book/src/SUMMARY.md:109`. Build-readiness fence-parity guard: the proposed-changes block opens with a triple-backtick ```edit:...``` fence at CYCLE.md:326 and closes at :409; the inner YAML block uses tilde fences `~~~yaml` (:329) / `~~~` (:407) — proper nesting (outer backtick, inner tilde), exactly the construction the convert-nested-fences skill prescribes. No firm-body-outside-fence concern (this is an audit, not a firm-chapter author).

**edge-label-fidelity — pass.** Audit consistently discusses the L1>L0 edge throughout (§"L0 Palace source citations" first; §"L1 / cross-theme anchors" second; the per-applicability-condition walks all anchor to L0 source). The §"Algebraic laws (if cited)" §explicitly notes the audit does NOT introduce algebraic laws at L1 over the bilinear form (inherits them from L1/bilinear-form), so there is no L2-or-higher edge mis-discussion. Direction-of-definition observed in caveat 5 (no L0→L1 reverse-direction prose). Fidelity to L1>L0 throughout.

**plan-kind-consistency — pass.** Declared kind is "lowering-verifier audit" (per frontmatter `agent: lowering-verifier`, `scope: L1>L0 theme audit`). Content shape matches: per-citation audit table, applicability-condition walk, algebraic-laws-inherited paragraph, `verified_against:` YAML append as the standard output channel of this agent. No firm-operator authoring, no rotation proposal. Status-relative-to-existing-firm-theme is correctly "confirms-without-change" (caveat 6) rather than upgrading or downgrading.

**skill-uptake-survey — pass.** The report explicitly invokes `tools/citecheck/citecheck.py --scan` AND `--anchor` for the load-bearing pinpoints (§"Citecheck `--anchor` runs"), and explicitly cites the loaded `verify-citation-range`, `convert-nested-fences-to-indented-code-in-proposed-changes-block` (the YAML-inside-edit nesting), and the cycle-025 codemap drift discipline (§"codemap drift note"). The mechanical citation-source-of-truth tool was correctly invoked as the loaded `citation-validity` skill prescribes (cycle-024 update). Surveys the friction-ledger / skill channels in §"codemap drift note". Pure presence check passes.

### Issues found

1. **Bare-basename ambiguous citation in proposed YAML row (CYCLE.md:346, embedded in the proposed-changes block at :343-346).** The note value for the `palace/linalg/operator.cpp:621-629` row contains the parenthetical `(operator.cpp:613-614)` — a bare-basename reference that citecheck `--scan` correctly flags as ambiguous between `palace/linalg/operator.cpp:613-614` (intended — the matrix-weighted-norm Sub-pattern B lane-split in `Norml2<ComplexVector>`) and `palace/fem/libceed/operator.cpp:613-614` (unintended). Severity: medium — this lands inside the proposed `verified_against:` metadata that the integrator will append to the on-disk firm theme, so the artifact would acquire an ambiguous citation. Fix: replace `(operator.cpp:613-614)` with the full path `(palace/linalg/operator.cpp:613-614)`. Where: CYCLE.md:346 (the bare instance in the YAML note body).

2. **Channel-format violation: proposed verified_against YAML block does not round-trip through `yaml.safe_load` (CYCLE.md:398 and :406).** Rows 17 and 19 of the proposed `verified_against:` block carry `note:` values whose first character is a single quote (`'`). YAML reads a leading `'` as the start of a quoted scalar, then chokes on the trailing prose after the closing `'` with `ParserError: expected <block end>, but found '<scalar>'` (verified — full block fails safe_load at line 69 column 63). The report's Summary claims "no leading-double-quote note values (yaml.safe_load hazard avoided)" but the hazard is leading-quote-character (single OR double), not double-only. Severity: medium — the appended metadata block would be unparseable by any consumer using `yaml.safe_load`. Fix: prefix each affected note value with a non-quote character or wrap the entire value in matching outer quotes; the simplest fix is to drop the leading apostrophe and instead use unquoted prose (e.g. `note: conjugation asymmetry header — the core theme content; the inherited reconciliation...`). Where: CYCLE.md:398 (`note: 'The conjugation asymmetry...`) and CYCLE.md:406 (`note: 'Mutation-free matrix-weighted inner-product reduction...`).

3. **Summary claim narrower than channel-format spec.** The Summary's parenthetical "no leading-double-quote note values (yaml.safe_load hazard avoided)" frames the hazard as double-quote-specific when it is actually leading-quote-character-of-either-kind. Not in itself an audit-finding defect (it is prose self-description), but the misframing is what allowed defect #2 to slip past the producer's self-check. Severity: low — recording for completeness; downstream may want to amend the channel-format-self-check phrasing.

## Repair

### Fixes attempted

- **Finding 1: Bare-basename ambiguous citation `(operator.cpp:613-614)` at CYCLE.md:346.**
  - **Decision**: repaired.
  - **Action**: Edited CYCLE.md:346 (inside the proposed `verified_against:` YAML row for `palace/linalg/operator.cpp:621-629`) to prefix the parenthetical with the full path: `(palace/linalg/operator.cpp:613-614)`. Verified clean via `python3 tools/citecheck/citecheck.py --scan reports/<id>/CYCLE.md --quiet` → `40 ok, 0 failing` (was `39 ok, 1 failing`). The previously-flagged AMBIG (basename `operator.cpp` matching both `palace/linalg/operator.cpp` and `palace/fem/libceed/operator.cpp`) is resolved; the intended path was `palace/linalg/operator.cpp` (the matrix-weighted-norm Sub-pattern B lane-split) as the critic identified.

- **Finding 2: YAML parse failure on rows starting `note:` with literal single-quote (CYCLE.md:398 and :406).**
  - **Decision**: repaired.
  - **Action**: Rewrote both note values so they no longer begin with a quote character of any kind. CYCLE.md:398 changed from `note: 'The conjugation asymmetry — the core theme content'; ...` to `note: section header "The conjugation asymmetry" — the core theme content; ...` (prefix added that does NOT begin with a quote; inner section-header phrase wrapped in double quotes, but the SCALAR no longer begins with a quote so YAML reads it as plain prose). CYCLE.md:406 changed from `note: 'Mutation-free matrix-weighted inner-product reduction α = xᴴ M y'; ...` to `note: opening tagline — Mutation-free matrix-weighted inner-product reduction α = xᴴ M y; ...` (same fix-shape: a non-quote prefix that converts the scalar to a plain-string YAML reading). Verified by extracting the full `verified_against:` YAML block (`sed -n '329,407p' reports/<id>/CYCLE.md` minus the outer `~~~yaml`/`~~~` fences) and running `yaml.safe_load`: parses cleanly, 19 rows, no `ParserError`. Both load-bearing fixes (a) `--scan` clean, (b) `yaml.safe_load` parses — confirmed mechanically.

- **Finding 3: Summary prose claim narrower than channel-format spec (leading-DOUBLE-quote vs leading-quote-of-either-kind).**
  - **Decision**: not-needed (the critic itself marked this severity:low / "recording for completeness", explicitly not a blocker; the underlying YAML defect is repaired under Finding 2 above). The Summary prose is left as-is in the report (per repair authority: substantive prose rewriting to self-correct the narrower-than-spec claim is out of scope for mechanical repair; the meta-phase codification path is the correct route for the broader rule, see Skill-candidate / friction signal below).

### Unrepairable findings

None. All findings the critic flagged are either repaired (Finding 1, Finding 2) or marked not-needed per critic's own severity:low determination + meta-phase routing (Finding 3).

### Skill-candidate / friction signal (appended to `scaffolding/skill-candidates.md`)

The leading-quote-of-EITHER-kind YAML hazard is a refinement of the cycle-028-flagged leading-DOUBLE-quote hazard. The channel-format rule should be generalized to: **"no `verified_against:` `note:` value may begin with a quote character of either kind (single `'` or double `\"`)"**. The batch-8 meta-phase (firing after this cycle) should codify this generalization in the channel-format spec. Appended a candidate to `scaffolding/skill-candidates.md` recording the pattern; also flagged here in the META repair section for meta-phase visibility.

## Suggested resolution

`ready`. Both citation-validity defects are mechanically repaired; the audit's substantive findings (fully-supported verdict, 19 anchors clean, no contradictions) are unchanged. The integrator-per-report dispatch can apply the proposed `verified_against:` YAML append to `book/src/L1-L0/bilinear-form-mutation-rotation.md` as-is: the block now (a) carries no ambiguous citations, (b) round-trips through `yaml.safe_load`. Integrator note for completeness: the YAML block uses tilde fences (`~~~yaml`/`~~~`) inside the outer triple-backtick `edit:` fence, the proper nesting per `convert-nested-fences-to-indented-code-in-proposed-changes-block`.
