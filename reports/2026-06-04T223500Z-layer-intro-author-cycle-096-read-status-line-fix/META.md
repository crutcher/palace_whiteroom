---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T231500Z
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

# META: verification of D4 — `read_status_line` token-priority parse-bug fix

## Critique

This is a `tools/`-ONLY report (NOT a `book/` proposed-change): it records a direct
write to `tools/graded-stack-lint/`, fixing the `read_status_line` token-priority parse
bug. The four subject-DAG checks (citation-validity-of-Palace-claims, surface-or-evidence,
rotation-quality, variant-axis-coverage) are not applicable to a tooling fix in their
operator/theme sense; I adapted them to the report's actual verifiable claims (does the
tool produce the reported outcome; is the fix correct; is the regression-guard valid) and
verified each empirically by running the tool, the fixture, and the old-vs-new logic.

### Checks run

**citation-validity** — pass. The report's load-bearing claims are tool-output numbers and
on-disk status-line forms, all of which I reproduced. `python3 tools/graded-stack-lint/graded_stack_lint.py --json`
yields `rank_violations: 0`, histogram `{firm: 191, rough-in: 7, partly-constructive: 3,
obstruction: 2, partial-obstruction: 4}`, `promotion_frontier: 10` — matching the report's
after-fix column exactly (CYCLE.md:55-64). The bug-location citation `graded_stack_lint.py:319-324`
(CYCLE.md:104) corresponds to the now-removed blob-scan; the rewritten `read_status_line`
sits at the current file's lines 331-371 with `_STATUS_TOKENS` at 318-328. Spot-check of the
named reclassified nodes (below, under surface-or-evidence) confirms each genuinely leads
with its corrected token on disk.

**surface-or-evidence** — pass (adapted: the "evidence" of a tooling fix is the tool run +
the on-disk source the parser now reads correctly). I CRITICALLY spot-checked the
false-negative risk the dispatch flagged as a serious-defect candidate. Three reclassified
nodes genuinely lead with the corrected token AND carry the downstream provenance mentions
that triggered the old bug: `L2/dot` leads `` `firm` `` but its line contains
"specialization-stub" (old blob matched `stub`); `L1/apply_nonlinear_pencil` leads `` `firm` ``
and mentions `rough-in (test-coverage-bounded)`/`partly-constructive` downstream;
`L4-L3/solve-family-map-dissolution` (the O1 dep) leads `` `firm` ``.
`L1-L0/triangular-solve-obstruction` leads `` `obstruction` `` (correct), and
`L1-L0/bicgstab-iteration` leads `` `rough-in (obstruction)` `` → reads `rough-in` (rank 2.0,
correct). These are real false-positive corrections, NOT new false-negatives. I additionally
ran a tree-wide false-NEGATIVE survey: of all prose-fallback nodes (no rank/firmness/non-seed
status) carrying a `## Status` heading, exactly ONE reads `None` — `spec/index.md`, whose
"## Status" is a Markdown table-column header (`| Slice | … | Status notes |`), a genuine
non-status-line that correctly yields None. The fix introduces zero false-negatives on the
real tree. No signature-named record is involved (tooling fix), so the record-definition
sub-check no-ops.

**rotation-quality** — pass (not applicable to a tooling fix; no layer rotation is claimed).

**variant-axis-coverage** — pass (adapted: the parser's "variant axis" is the set of
status-line decoration forms). I verified the leading-inline-code-token rule across the
forms the report claims robustness for: `` `rough-in (test-coverage-bounded)` `` → the 2.5
sub-rank (not bare rough-in); `` `firm (structural)` `` → firm; `` `rough-in (obstruction)` ``
→ rough-in; the unterminated wrapped span `` `partly-constructive (structural … `` →
partly-constructive; `**firm**` → firm; blockquoted `` > `firm` `` → firm. The qualified
spelling `` `obstruction (opaque-library-ownership)` `` reads to the bare `obstruction` kind
token, which is correct: `derive_rank` then resolves its numeric rank via
`obstruction_resolution` (verified: returns `(None, 'obstruction', True, None)` with no
resolution, `(3.0, 'obstruction', True, None)` with `obstruction_resolution: firm`), and the
histogram bins on `rank_token.split(" (")[0]` so it lands in the `obstruction` bin. One form
NOT recognized — a list-marker leading status line `` - `stub` `` returns None (`lstrip("> ")`
strips blockquote/space but not `-`) — but the tree-wide survey above confirms NO real node
uses that form, so it is not a live gap; noting it as telemetry only, not an issue.

**cross-reference-integrity** — pass. The report names five written files; all exist on disk
(`graded_stack_lint.py`, `fixture/.../prose_firm_provenance.md`, `fixture/.../widget.L4.md`,
`README.md`, `fixture/README.md`). The README parse-rule paragraph is present
(README.md:46-60); the fixture README wires the new node into the graph diagram (line 16),
adds the assertion-#9 block (lines 65-80), and updates the confirmed-output counts (lines
77-78). All reclassified-node slugs cited in CYCLE.md:75-86 resolve to real files.

**edge-label-fidelity** — pass. No L_{n+1}→L_n edge label is carried (tooling report). The
fixture edge `widget.L4 → prose_firm_provenance` (firm→firm) is real and adds no violation,
as claimed.

**plan-kind-consistency** — pass. The report is shaped as a `tools/`-only direct-write fix
record and is explicit that it is NOT a `book/` proposed-change routed through the integrator
(CYCLE.md:12-13, 36). No proposed-changes fence is expected or present; the firm-body-inside-
fence guard is inapplicable. Content shape matches the declared kind.

**skill-uptake-survey** — pass. No existing skill governs the graded-stack-lint parser; the
fix is a self-contained tooling correction with its own regression fixture. No skill
invocation is implied or missing.

### Issues found

None. All claims were reproduced empirically:
- Real-tree run reproduces `rank_violations 1→0` and the full after-fix histogram (firm 191,
  rough-in 7, partly-constructive 3, obstruction 2, partial-obstruction 4) + frontier 10.
- Fixture run reproduces `files=10 typed=9 untyped=1 roots=3 rank_violations=2 reachable=7
  detritus=2 promotion_frontier=1 exit=1`, matching both CYCLE.md:90 and the fixture README's
  confirmed-outputs block.
- The regression guard is genuine: on `prose_firm_provenance.md`, the simulated OLD blob-scan
  returns `rough-in (test-coverage-bounded)` (a spurious violation) while the NEW
  `read_status_line` returns `firm` — the fixture actually exercises the bug.
- `derive_rank` precedence is preserved: explicit `rank: stub` / `firmness: rough-in` win
  over the prose `` `firm` `` line (returns stub/rough-in respectively); only the
  no-frontmatter case falls through to the prose reader (returns firm).
- No false-negatives introduced (tree-wide survey: only `spec/index.md`'s table-header
  "## Status" reads None, which is correct).
- `python3 -m py_compile` clean.

The one observation worth recording as telemetry (not an issue, since no real node triggers
it): a list-marker-led status line `` - `stub` `` would read None; the new rule strips a
leading blockquote/space and one decoration char but not a `-` list marker. No on-disk node
uses that form today.
