---
verifies: ../CYCLE.md
critiqued_at: 2026-05-30T053000Z
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
repaired_at: 2026-05-30T060000Z
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

# META: verification of cycle-031 Phase-1 sparse_triangular_solve slice-reduction audit

## Critique

### Checks run

**citation-validity** — Ran `python3 tools/citecheck/citecheck.py --scan` on the report (59 citations checked; 57 ok, 2 OOB failures). Both failures are off-by-one upper-bound drift on the same slice: `book/src/spec/slices/sparse_triangular_solve.md:210-241` and `:1-241` — the file has 240 lines. Spot-checked the supporting evidence pinpoints with `--anchor`: `concepts/scope-out-obstruction.md:66-78` anchor "Canonical instance" → OK (line 66 in range); `concepts/sequential-obstruction.md:50-81` anchor "Sub-kind" → OK (line 50 in range); `concepts/negative-result-slice.md:44-47` anchor "sparse_triangular_solve" → OK (line 47 in range); `book/src/L1-L0/triangular-solve-obstruction.md:275-308` anchor "Related" → DRIFT (anchor at line 273, -2 outside range; suggested `:273-306`). The DEFER substance survives — the cited §"Related" content IS at lines 273-308 — but the heading itself sits 2 lines above the cited range. **Verdict: warning** — 3 numeric off-by-one drifts (2 OOB on the slice, 1 -2-drift on the obstruction §Related anchor); content is real but range bounds are loose.

**surface-or-evidence** — Not a refinement-shaped proposal; this is a same-layer-cross-cutter OBSERVATION report whose sole mechanical proposal is a one-sentence-plus-one-bullet append to the slice's reduction-status header to add a reciprocal cross-link to the c029 L1>L0 obstruction theme. The proposed-changes block has both a surface diff (OLD/NEW prose) and the verified retroactive evidence (the obstruction theme's reciprocal cross-link at `triangular-solve-obstruction.md:273-308` is on disk and was confirmed). **Verdict: pass.**

**rotation-quality** — Not applicable to a slice-reduction-audit observation report; no algebraic / structural / reduction rotation is asserted. The "rotation" the report discusses is the cycle-013+ Phase-1 corpus-reduction policy ("does this slice's material lift cleanly into firm layered homes?"), which is a methodology question, not an L_{n+1}→L_n representation rotation. **Verdict: pass** (not applicable to same-layer-cross-cutter observation report).

**variant-axis-coverage** — The report's "Observation kind" section explicitly names a *new* policy axis ("is the slice a §Canonical-instance worked example on a concept page?") as the load-bearing reduction-blocker, and surfaces it as a meta-phase friction-ledger candidate (`negative-result-slice-canonical-instance-blocks-reduction`) rather than enacting policy change in-cycle. The coverage table (slice section vs. firm-artifact home) is exhaustive across the 9 §-level subdivisions of the slice (Background, L0 in 5 sub-rows, L1, Disposition, Open questions). Hidden-branch risk is low. **Verdict: pass.**

**cross-reference-integrity** — All `[link]` references in the proposed-changes diff resolve on disk: `book/src/concepts/scope-out-obstruction.md` (102 lines, §"Canonical instance" at :66, slice cite at :68 ✓), `book/src/concepts/sequential-obstruction.md` (112 lines, §"Sub-kind" at :50, slice cite at :53 ✓), `book/src/concepts/negative-result-slice.md` (80 lines, slice example at :47 ✓), `book/src/L1-L0/triangular-solve-obstruction.md` (499 lines; §Related slice cross-link confirmed at :273-308 ✓, verified_against YAML at :460-475 ✓). The grep table's per-row HARD-vs-textual-orphan classification has one mislabel: `book/src/L1-L0/triangular-solve-obstruction.md:464` is a YAML `citation:` field (`- citation: book/src/spec/slices/sparse_triangular_solve.md`), NOT a markdown link, so it would NOT cause a linkcheck break — it is a textual orphan, same shape as the other YAML-note rows. The summary tally "6 hard linkcheck breaks across 5 firm files" IS correct (the 6 live-mdBook-link sites: negative-result-slice.md:47, sequential-obstruction.md:53, scope-out-obstruction.md:68, spec/index.md:21, triangular-solve-obstruction.md:277, SUMMARY.md:151); the per-row HARD label on :464 inflates the row-level tally without affecting the verdict. **Verdict: pass** (substantive cross-reference integrity confirmed; the :464 mislabel is a presentation issue not a structural one). Build-readiness guard (firm-body-inside-fence): proposed-changes block is a single ```text...``` fence enclosing the OLD/NEW prose; no firm-claim mismatch with body placement.

**edge-label-fidelity** — The report does carry an implicit edge label ("L1>L0 obstruction theme cross-link to a Phase-1 slice"). The prose discusses exactly that pairing — the cycle-029 `triangular-solve-obstruction` L1>L0 theme and the Phase-1 `sparse_triangular_solve` slice — across every section. No edge-label drift. **Verdict: pass.**

**plan-kind-consistency** — Report is declared as a same-layer-cross-cutter observation (no `kind:` frontmatter, but the agent declaration in frontmatter is `same-layer-cross-cutter` and the role-spec calls these observation reports). The content shape matches: one observation (variant-axis-coverage gap in the corpus-reduction policy's audit shape), one mechanical proposed-change (the reciprocal cross-link), four follow-up dispatch recommendations with explicit fan-out judgments, and five open questions / caveats. The DEFER verdict is appropriately scoped — the report does NOT enact unification, does NOT promote the friction-ledger candidate to a real ledger entry, does NOT modify the corpus-reduction policy. **Verdict: pass.**

**skill-uptake-survey** — The report explicitly invokes the `phase-1-slice-reduction-audit` skill (lines 20, 22, 27 — START + END + grep steps follow the skill's procedure). The grep verdict cites the skill's removal-specific step structure. The `polynomial_recurrence_step` precedent is cited as the skill-anchored example. No skill exists for "concept-page §Canonical-instance check" — appropriately surfaced as a methodology question (potential new skill / new policy bullet) rather than presented as missed-skill uptake. **Verdict: pass.**

### Issues found

1. **citation-validity (warning, low severity)** — Two off-by-one upper-bound OOB drifts on the slice file: `CYCLE.md:115` cites `book/src/spec/slices/sparse_triangular_solve.md:1-241` and `CYCLE.md:27` cites `:210-241`. The file is 240 lines; bounds should be `:1-240` and `:210-240`. Both citation contents are in range (the substantive material ends at line 240); the upper bound is one past the last line. Likely off-by-one inclusive-vs-exclusive interpretation. Mechanical fix candidate.

2. **citation-validity (warning, low severity)** — `CYCLE.md:24`, `:80`, `:92`, `:111`, `:116` cite `book/src/L1-L0/triangular-solve-obstruction.md:275-308` for the §"Related" section. The §"Related" heading itself is at line 273; the cited range starts at line 275 (the first non-blank body content of the section). Citecheck `--anchor "Related"` flags this as `-2` drift; suggested `:273-306`. The cited body content is real and in-range, but per the citation convention the heading is part of the cited section. Mechanical fix candidate.

3. **cross-reference-integrity (info, presentation only)** — `CYCLE.md:68` lists `book/src/L1-L0/triangular-solve-obstruction.md:464` under "HARD linkcheck break" in the grep table, but line 464 is a YAML `citation:` field (`- citation: book/src/spec/slices/...`) inside the `verified_against` block, not a markdown live link. It would not fail linkcheck on slice removal; it would be a textual orphan only (same as the other YAML-note rows at :471 / :475). The summary tally "6 hard linkcheck breaks" on `CYCLE.md:72` IS correct (only 6 actual live-link sites: negative-result-slice.md:47, sequential-obstruction.md:53, scope-out-obstruction.md:68, spec/index.md:21, triangular-solve-obstruction.md:277, SUMMARY.md:151) — so this is a per-row mislabel that does not propagate into the verdict. The "5 firm files" tally in the summary is also correct only if `:277` and `:464` are counted as the same file (correct: both in `triangular-solve-obstruction.md`); the file-count is fine. Presentation-only issue.

4. **citation-validity (info, terminology)** — `CYCLE.md:12` and the body of the "Specific finding" section assert the slice is the "named canonical instance of three concept pages": `scope-out-obstruction.md:68`, `sequential-obstruction.md:53`, and `negative-result-slice.md:47`. The first two ARE in §-headings explicitly labeled "Canonical instance" / "Sub-kind" (with the slice link as the named instance). The third (`negative-result-slice.md:47`) is in §"Examples in this spec" — a *named example* rather than a labeled §Canonical-instance line. The substantive claim (the slice is a load-bearing referent of all three concept pages) is correct; the precise terminology "canonical instance" is a stretch for the third. Low-severity terminology inflation — doesn't change the DEFER verdict because the §"Examples in this spec" entry would still HARD-linkcheck-break on removal (the live link IS at :47).

5. **citation-validity (info, evidence section line ranges)** — `CYCLE.md:117` cites `book/src/L1-L0/triangular-solve-obstruction.md:464-475` for the verified_against YAML entries. Confirmed: the slice + scope-out + sequential-obstruction citation entries occupy lines 464-475 (slice at :464-467, scope-out at :468-471, sequential-obstruction at :472-475). Pass on cross-check. `CYCLE.md:118` cites `book/src/concepts/scope-out-obstruction.md:66-78` for §"Canonical instance" — anchor confirmed at :66, body content extends through :78. Pass. `CYCLE.md:120` cites `book/src/concepts/sequential-obstruction.md:50-81` for §"Sub-kind: out-of-scope-obstruction" — anchor confirmed at :50, body extends through :81. Pass.

6. **No structural defects in proposed-changes block** — The proposed-changes block at `CYCLE.md:89-109` uses a single ```text...``` fence containing OLD/NEW prose; no nested fences; no firm-body-outside-fence pattern. Build-readiness guard clears.

7. **Surfaced friction-ledger candidate** — `CYCLE.md:82, :129` introduces `negative-result-slice-canonical-instance-blocks-reduction` as a meta-phase candidate. This is appropriately surfaced (not enacted) and traceable to the second-axis-of-corpus-reduction-policy observation that motivates the DEFER verdict. The candidate's fan-out ranking (medium; one ledger entry + one CLAUDE.md bullet) is reasonable. No issue — recorded as evidence the report's surfacing-channel routing is correct.

## Repair

### Fixes attempted

- **Finding 1** (citation-validity, low): OOB drift `book/src/spec/slices/sparse_triangular_solve.md:1-241` (file has 240 lines).
  - **Decision**: repaired
  - **Action**: `CYCLE.md:115` — corrected upper bound `:1-241` → `:1-240`. Re-verified with `tools/citecheck/citecheck.py --scan`: now in range (file has 240 lines).

- **Finding 2** (citation-validity, low): OOB drift `book/src/spec/slices/sparse_triangular_solve.md:210-241` (file has 240 lines).
  - **Decision**: repaired
  - **Action**: `CYCLE.md:27` — corrected upper bound `:210-241` → `:210-240`. Re-verified with `tools/citecheck/citecheck.py --scan`: now in range.

- **Finding 3** (citation-validity, low): anchor drift on §"Related" citation `book/src/L1-L0/triangular-solve-obstruction.md:275-308` (anchor at line 273).
  - **Decision**: repaired
  - **Action**: `CYCLE.md:24, :92, :106, :111, :116` — corrected range `:275-308` → `:273-308` (replace_all). Chose `:273-308` over the critic's suggested `:273-306` because lines 307-308 remain part of the §"Related" body (the "See the §Open questions..." trailing sentence about the follow-up); the original upper bound 308 was structurally correct, only the lower bound was off (needed -2 to include the `## Related` heading itself). Verified on-disk: §"Related" runs 273-308 (line 309 blank; line 310 is `## Verified-against`). Re-verified with `tools/citecheck/citecheck.py --anchor "Related" book/src/L1-L0/triangular-solve-obstruction.md:273-308`: OK, anchor in range.

- **Finding 4** (cross-reference-integrity, presentation): per-row mislabel — `triangular-solve-obstruction.md:464` row tagged HARD linkcheck break but is a YAML `citation:` field, not a markdown link.
  - **Decision**: repaired
  - **Action**: `CYCLE.md:68` — corrected row form ("live link in `verified_against` YAML" → "YAML `citation:` field in `verified_against` block (not a markdown link)") and behaviour ("**HARD linkcheck break**" → "textual orphan; the `verified_against` entry becomes self-referentially incomplete, but does NOT break linkcheck"). Also corrected the dependent summary tally at `CYCLE.md:72`: 6 hard linkcheck breaks now correctly listed across 6 firm files (collapsing `triangular-solve-obstruction.md ×2` to a single `:277` HARD site; added explicit `:464` textual-orphan callout to the YAML/inline-code group). The 6-hard-breaks count remains 6 (the critic confirmed this part of the tally was correct); only the file-mention list and the ×2→×1 needed updating.

- **Finding 5** (citation-validity, terminology low): summary line 12 calls the slice "named canonical instance of three concept pages" but `negative-result-slice.md:47` is in §"Examples in this spec", not a labeled §Canonical-instance line.
  - **Decision**: repaired
  - **Action**: `CYCLE.md:12` — softened wording from "named canonical instance of three concept pages (`scope-out-obstruction.md:68`, `negative-result-slice.md:47`, `sequential-obstruction.md:53`)" to "named load-bearing referent of three concept pages — a §"Canonical instance" entry on `scope-out-obstruction.md:68`, a §"Sub-kind: out-of-scope-obstruction" canonical-instance entry on `sequential-obstruction.md:53`, and a §"Examples in this spec" worked-example entry on `negative-result-slice.md:47`". The substantive claim (all three pages would HARD-linkcheck-break on removal) is preserved; the precise §-anchor labels now match on-disk.

### Unrepairable findings

None. All five findings were mechanical / surgical and within repair authority (off-by-one citation bounds, anchor drift, per-row mislabel, terminology precision). The DEFER verdict, the proposed cross-link change, and the report's substantive analysis were not modified.

### Citecheck verification

Re-ran `python3 tools/citecheck/citecheck.py --scan reports/2026-05-30T050100Z-same-layer-cross-cutter-sparse-triangular-solve-slice-reduction/CYCLE.md` after all fixes: **63 ok, 0 failing (63 citations checked)** — clean. Citation-validity check now passes mechanically.

## Suggested resolution

`overall_status: ready`. All five low-severity findings repaired in place; no follow-up agent required. The single proposed book change (the reciprocal slice→obstruction-theme cross-link in `book/src/spec/slices/sparse_triangular_solve.md`'s reduction-status header) is sound, with all supporting citations now bound-correct and anchor-aligned. Integrator-per-report can enact the proposed-changes block at cycle-031 finalize.

Notes for integrator:
- The proposed-changes block adds one paragraph + one bullet to the slice's reduction-status header; the OLD/NEW diff is line-faithful to the current on-disk file (240-line file; reduction-status block at `:3-9`).
- The verified_against YAML cross-link from the obstruction theme at `triangular-solve-obstruction.md:464-475` already covers the slice as `verdict: positive-cross-reference`; the proposed change closes the reciprocal loop in the slice.
- The methodology observation surfaced as friction-ledger candidate `negative-result-slice-canonical-instance-blocks-reduction` is appropriately deferred to meta-phase batch-9 (not enacted in this cycle).
