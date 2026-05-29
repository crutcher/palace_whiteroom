---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T07:26:02Z
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
repaired_at: 2026-05-29T07:31:18Z
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

# META: verification of "Formalize lu_solve at L1"

## Critique

### Checks run

**citation-validity — warning.** Independently re-verified every L0 citation against `reference/` via `palace-codemap` `read_range`. The load-bearing solve-site ranges are all **line-exact**: `nleps.cpp:533` (`SS = -S.fullPivLu().solve(SS)`), `:534` (`x2 = SS.fullPivLu().solve(x2)`), `:535` (`MatVecMult(X, S.fullPivLu().solve(x2))`), `:562` (`const Eigen::MatrixXcd S = lam * ... - H;`), `:563` (`MatVecMult(X, S.fullPivLu().solve(vv2))`), `:664` (`S = eig * ... - H`), `:665` (`const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2);`), `:667` (`MatVecMult(X, S.fullPivLu().solve(Sv2))`), `:532`, `:524`, `:397` (`Eigen::MatrixXcd H;`), `romoperator.cpp:765` (`RHSr = Ar.fullPivHouseholderQr().solve(RHSr);`), `:757-758` (the two disabled LDLT solves), `:701` (`SolvePROM` sig), `:717` (`Ar.resize(V.size(), V.size());`), and `romoperator.hpp:188-189` (`Eigen::MatrixXcd Ar; / Eigen::VectorXcd RHSr;`). The two pinpoint drifts the producer claims to have caught (`nleps:561→562`, `romoperator:716→717`) are confirmed correct — `:562` and `:717` are line-exact. **However, two SECONDARY citations carry residual pinpoint drift that the citecheck pass did not catch** (both attach to the ROM stability comment, not to a solve site): (1) the stability-comment range is cited as `romoperator.cpp:760-763` in the Context, Semantics, Algebraic-laws, Variant-axes, and Evidence sections, but the comment text actually occupies lines **762-764** (`760`=`else`, `761`=`{`, `762-764`=the three `// QR solve...` lines); the cited range straddles the `else {` and truncates the final quoted line (`// into separate columns.` at `:764`). (2) the Evidence section's parenthetical "the **disabled** (`if constexpr (false)`, `:756`) LDLT alternative" attributes `if constexpr (false)` to `:756`, but that keyword is at **`:754`** (`:756` is the `// LDLT solve.` comment). Both are off-by-2 drifts on quote/keyword pinpoints; the quoted comment text itself is verbatim-correct (modulo the source's own typo "to due"), so the claims are supported — only the line pointers are imprecise. Warning, not fail: every claim has a citation and all the structural/solve-site anchors are exact; the drift is confined to two annotative pointers around a comment.

**surface-or-evidence — pass.** Not a refinement-shaped proposal — this is a NEW firm L1 operator (`new:book/src/L1/lu_solve.md` + three dep-map/SUMMARY inserts), not a change to an existing operator/theme's surface. The surface-or-evidence gate is about refinement proposals (modify-surface-plus-rotation-claim vs retroactive-backfill); a net-new operator entry with its own full apparatus is neither. The new operator is grounded in positive source throughout. Not applicable to new-operator-creation shape; marked pass.

**rotation-quality — pass.** The L1↔L0 rotation is a genuine mutation→pure rotation, not a rename. L0 is an in-place, destination-overwriting dense Eigen factorize-and-solve (`SS = -S.fullPivLu().solve(SS)`, `RHSr = Ar.fullPivHouseholderQr().solve(RHSr)` — the destination IS the RHS argument, plus a transient decomposition-object lifetime and internal pivot/permutation state); L1 is `x = lu_solve(A, b)` with no destination buffer, no factorization-object lifetime, no pivot bookkeeping in the signature. The rotation hides state (the transient Eigen decomposition + pivot arrays) and removes the in-place RHS overwrite — strictly more abstract/equational than the L0 form. State-hiding/destination-erasure is a pass per the rotation-quality rubric.

**variant-axis-coverage — pass.** Three variant axes are enumerated and each is dispositioned: (i) **factorization kernel** (`full-pivot-LU | full-pivot-QR | LDLT`) — contracted as load-bearing-numerical, correctly justified by the ROM source comment choosing QR-for-stability over the rejected LDLT; (ii) **single-RHS vs multi-RHS** — parameterised/absorbed-as-form, with both forms witnessed (`SS` multi-RHS `:533`, `x2`/`v2` single-RHS `:534`/`:665`) and tied to law 4; (iii) **element type** (`complex | real`) — absorbed, complex witnessed at every site, real explicitly flagged as permitted-but-unsurfaced. No hidden branch: the disabled LDLT path (`if constexpr (false)`) is surfaced as a kernel-axis member, not silently dropped. The `MatVecMult(X, ·)` basis-expansion adjacency is explicitly scoped out (flagged as a separate future leaf, not a `lu_solve` axis). Coverage complete.

**cross-reference-integrity — pass (incl. build-readiness fence guard).** All live links in the new chapter resolve: `./ksp_solve.md`, `./apply_linop.md`, `./apply_nonlinear_pencil.md`, `./assemble-diagonal.md` all exist on disk under `book/src/L1/`. The three components that do NOT exist on disk — `deflate`, `gram` (verified absent anywhere under `book/src/`), and the `lu_solve-mutation-rotation` L1>L0 theme (absent) — are all correctly rendered as **plain text, no live link** (Context, Dependencies, L1-vs-L0, Open-questions), per `rough-in-forward-reference-must-be-plain-text-not-live-link`; no `[...](...)` link to a missing file, so no `linkcheck2` break. The SUMMARY.md insert anchor (`- [apply_nonlinear_pencil](./L1/apply_nonlinear_pencil.md)` at SUMMARY line 70) is exact; the two `index.md` edits' anchors (the `apply_nonlinear_pencil` cohort bullet + the `apply_nonlinear_pencil` dep-map row) match the live `index.md` verbatim. **Build-readiness guard (firm-body-inside-fence): PASS.** Fence enumeration of CYCLE.md yields 12 fence markers (even parity, balanced): the `new:book/src/L1/lu_solve.md` block opens at line 21 and closes at line 129, enclosing exactly one balanced nested `text` fence (the Signature block, 39→46). The full firm apparatus — `## Status` (line 102), Signature (37-46), Algebraic-laws (72-86), Evidence (113-128) — sits ENTIRELY inside the 21-129 fence. The report's own top-level sections ("Operator content", "Supporting evidence", "Open questions") begin only at line 146, AFTER the last proposed-changes fence; they are a redundant prose recap, NOT the chapter body authored outside the fence. This is the inverse of the cycle-019 fence-truncation defect — the firm body is correctly INSIDE the fence. Nested `text` fences (39-46, and the recap's 151-155) are balanced.

**edge-label-fidelity — pass.** Not applicable to an L_n-operator entry — there is no L_{n+1}→L_n edge label on this proposal (it is a single-layer L1 operator chapter). The one cross-layer relationship asserted (the future `lu_solve-mutation-rotation` L1>L0 theme) is correctly directed (L1 form lowering into L0 source patterns) and discussed as such; the L2 `deflate`/`gram` fan-out is stated as upward dependency (L2-composed-of-L1), consistent with the high→low layering invariant. No mislabeled edge. Marked pass.

**plan-kind-consistency — pass.** Declared kind is `firm` L1 operator; content shape matches. Full apparatus present (Signature, Semantics, 5 affirmative laws + 3 explicit non-laws, Dependencies as leaf, Variant axes, Status, L1-vs-L0, Evidence). No rough-in placeholders, no `TODO`/`TBD`, no unanchored speculation in the operator body — every law is stated as an operator-algebra identity and every shape claim is source-anchored. The `firm` (not `rough-in (test-coverage-bounded)`) judgment is correctly reasoned: the laws are syntactic identities on positive source (`A⁻¹` operator-algebra facts), not convergence-semantics laws, so the firm-on-positive-structure escape applies — matching the cited `apply_linop` / `apply_nonlinear_pencil` precedent and distinct from the `eigsolve` test-gated situation. The load-bearing-numerical factorization-kernel axis is correctly NOT used to downgrade the whole entry (the value `A⁻¹b` is kernel-independent; only the bit-level/conditioning realization is kernel-dependent, recorded as a non-law). Classification sound.

**skill-uptake-survey — pass (telemetry).** The proposal's shape (new firm operator, citation-heavy) implies the citation-range and rotation-citation skills. The report's frontmatter + Supporting-evidence section record an explicit `tools/citecheck/citecheck.py --batch` run over all 17 planned citations (15 OK first pass, 2 drifts corrected), and the Status/Evidence sections record `search_text` over `test/unit/**` for the no-dedicated-test survey. Citecheck and codemap-search uptake is documented. (Note: the residual two pinpoint drifts flagged under citation-validity attach to comment/keyword pointers that the literal-anchor citecheck batch evidently did not range-pin — surfaced as telemetry, not blocking here.)

### Issues found

1. **`romoperator.cpp:760-763` comment-range pinpoint drift** — the ROM stability comment is cited as `:760-763` in five places (Context §2nd bullet implicitly, Semantics point (2), Algebraic-laws non-law (1), Variant-axes factorization-kernel bullet, and Evidence). The quoted comment text ("QR solve, for maximal stability. ... splitting of HDM solutions into Re and Im into separate columns.") actually occupies **`:762-764`**; the cited range starts on `else` (`:760`) / `{` (`:761`) and truncates the final quoted line `// into separate columns.` at `:764`. **Where:** `CYCLE.md` Semantics §point-2, Algebraic-laws non-law-1, Variant-axes kernel bullet, Evidence bullet (`romoperator.cpp:760-763`), and the `index.md` dep-map/cohort inserts (which carry `:760-763`). **Severity:** low — the quoted text is verbatim-correct and the claim is supported; only the line pointer is off by ~2 and clips the last line. Candidate for repair: retarget to `:762-764`.

2. **`if constexpr (false)` keyword cited at `:756`, actually at `:754`** — Evidence section bullet for the disabled LDLT path reads "the **disabled** (`if constexpr (false)`, `:756`) LDLT alternative". The `if constexpr (false)` guard is at **`:754`**; `:756` is the `// LDLT solve.` comment line (the LDLT solves themselves are at `:757-758`, which the report cites correctly elsewhere). **Where:** `CYCLE.md` Evidence section, `palace/models/romoperator.cpp:757-758` bullet. **Severity:** low — annotative pointer drift on a guard keyword; the LDLT-solve range `:757-758` it accompanies is exact. Candidate for repair: change the parenthetical `:756` to `:754`, or drop the line pointer.

3. **(Non-blocking, producer-flagged) layer-intro count + motif refresh deferred** — the report adds the dep-map row and cohort bullet but leaves the `**Firm (13)**` count header (should become 14) and the "Four semantic motifs" framing (candidate 5th motif: small-dense direct solve) for a layer-intro-author dispatch. **Where:** `book/src/L1/index.md:29` (`**Firm (13)**`) and `:18` ("Four semantic motifs"). **Severity:** informational — correctly out-of-role for harvester and already flagged in the report's Open-questions; noted so the integrator/planner routes the refresh. Not a defect in this report.

---

## Repair

### Fixes attempted

- **Finding (1)**: `romoperator.cpp:760-763` comment-range pinpoint drift — the ROM QR-stability comment is cited as `:760-763` in five proposed-changes locations (Semantics point (2), Algebraic-laws non-law (1), Variant-axes kernel bullet, Evidence bullet, and the `index.md` cohort-bullet insert), but the three-line comment actually occupies `:762-764`; the cited range straddles `else` (`:760`) / `{` (`:761`) and clips the final quoted line `// into separate columns.` (`:764`).
  - **Decision**: repaired
  - **Action**: Verified the corrected range against `reference/palace/palace/models/romoperator.cpp` two ways — `palace-codemap` `read_range` (752-766) and `tools/citecheck/citecheck.py --show palace/models/romoperator.cpp:762-764` (confirmed `:762-764` = the three `// QR solve...` lines exactly). Retargeted every `760-763` → `762-764` in `CYCLE.md` (5 occurrences in the proposed-changes blocks: lines 68 / 84 / 98 / 123 / 133 — full-path and bare forms; plus the 2 redundant-recap occurrences at lines 160 / 168, corrected for consistency). The quoted comment text was already verbatim-correct; only the line pointer moved.

- **Finding (2)**: `if constexpr (false)` keyword cited at `:756`, actually at `:754` — the Evidence-section parenthetical for the disabled LDLT path attributes the `if constexpr (false)` guard to `:756`, but that line is the `// LDLT solve.` comment; the guard keyword is at `:754`.
  - **Decision**: repaired
  - **Action**: Verified `:754` = `if constexpr (false)` via `palace-codemap` `read_range` and `citecheck --show palace/models/romoperator.cpp:754`. Changed the parenthetical `:756` → `:754` in `CYCLE.md` Evidence section (line 122, the `palace/models/romoperator.cpp:757-758` bullet). The accompanying LDLT-solve range `:757-758` was already exact and is unchanged.

- **Finding (3)**: layer-intro `**Firm (13)**` count + "Four semantic motifs" refresh deferred.
  - **Decision**: not-needed — the critic itself marked this informational and "Not a defect in this report"; it is correctly out-of-role for the harvester (layer-intro-author's domain) and already flagged in the report's Open-questions for the integrator/planner to route. No repair action; not a citation/surface/rotation finding.

**Confirmations (no action, critic judgments stood):**
- `firm`-not-`rough-in (test-coverage-bounded)` status: confirmed sound by the critic (plan-kind-consistency pass) — the firm-on-positive-structure escape applies (laws are syntactic operator-algebra identities on positive source, not convergence laws), matching the `apply_linop` / `apply_nonlinear_pencil` precedent. No edit.
- Load-bearing factorization-kernel variant axis: confirmed sound by the critic (variant-axis-coverage pass) — the kernel is correctly contracted as a load-bearing numerical choice (not absorbed, not used to downgrade the whole entry). No edit.

### Post-repair verification
- `citecheck --scan CYCLE.md` after edits: **22 ok, 0 failing** (all extracted citations in-bounds).
- No stale `760-763` or `:756` references remain in `CYCLE.md`; the two solve-site / structural anchor cohorts the critic verified line-exact (NLEPS `fullPivLu` sites, ROM `:765`, `hpp:188-189`) were untouched.

### Unrepairable findings
None. Both citation drifts were mechanical off-by-2 line-pointer corrections on annotative comment/keyword pointers (quoted text already verbatim-correct), squarely within repair authority — verify-corrected-line + apply.

## Suggested resolution
`ready`. The single `warning` (citation-validity) is fully resolved by the two mechanical line-pointer corrections; all 7 other checks passed. Notes for the integrator:
- The deferred layer-intro refresh (Finding 3 / report Open-question) — `book/src/L1/index.md` `**Firm (13)**` → `14` count header and the candidate 5th "small-dense direct solve" semantic motif — is out-of-role for this harvester report and should be routed to a layer-intro-author dispatch (cycle-022 wave-2 or later), not applied at integration of this report.
- The `lu_solve-mutation-rotation` L1>L0 theme and the `deflate`/`gram` L2 wave-2 combinators are correctly forward-referenced as plain text (no live link); no stub is forced by this report. Wave-2 should cite `book/src/L1/lu_solve.md` directly.
