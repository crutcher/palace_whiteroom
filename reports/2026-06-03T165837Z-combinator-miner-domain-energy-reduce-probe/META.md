---
verifies: ../REPORT.md
critiqued_at: 2026-06-03T172000Z
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
repaired_at: 2026-06-03T173000Z
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

# META: verification of CYCLE "Combinator candidate — domain_energy_reduce (distinct-verb confirm probe)"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` on the report: 20 ok / 3 failing. The 3 failures are all `[MISS]` on the three load-bearing L0 Palace-source citations — `reference/palace/models/postoperator.cpp:1036-1042`, `:1061-1066`, and `reference/palace/models/domainpostoperator.cpp:255-275` (the same path form recurs throughout the report body and Supporting-evidence). The MISS is a **path-hygiene drift, not a bad pinpoint**: the tool resolves citations under `reference/palace`, so the canonical/artifact-consistent form is `palace/models/postoperator.cpp` (the on-disk file is `reference/palace/palace/models/postoperator.cpp`; the established book convention, 27 occurrences in `book/src/`, is the single-`palace` `palace/models/...` form with NO `reference/` prefix). The report prepends `reference/` AND drops the inner `palace/` segment, so the path fails mechanical resolution. Re-running every pinpoint with the corrected `palace/palace/models/...` form returns `[ok]` for all of them — the **line ranges are all valid and in-range** (`postoperator.cpp:1021-1099`, `:1036-1042`, `:1061-1066`; `domainpostoperator.cpp:255-275`, `:277-298` all OK). The load-bearing reasoning anchors the verdict leans on all verify faithfully against the artifact: `participation_ratio.md:188-191` carries the EXACT "separate energy-reduction vocabulary, named not authored" out-of-scope disclaimer the collapse-1 refutation quotes; `gram_reduce.md:178-189` carries the c074 D6 CLOSED-NEGATIVE collapse-refusal (rank-1-vs-rank-2-Gram); `eigenfreq_qfactor_reduce.md:36-41` carries the "own verb, rank-1-table-not-Gram, minted as distinct on this reasoning" precedent. The participation-guard-asymmetry drive-by is a faithful source read (electric guards `std::abs(energy_i)`, magnetic guards `std::abs(energy)`), with a minor 1-line pin drift (report says `:1038`/`:1063`; the guard expressions are actually on `:1039`/`:1064`) — both within the enclosing loop ranges the report also cites, so the drift is cosmetic, not a range failure. Net: the report's *evidence is sound and self-verifies* once the path prefix is corrected; the warning is for the mechanically-broken path form on three L0 pinpoints.

**surface-or-evidence — pass.** This is an observation-only confirm-probe that proposes NO `book/` surface change by design (Proposed-changes: "NONE to `book/`"). It is not a refinement-shaped proposal, so the surface+rotation-evidence obligation does not apply; the report's evidential burden is to support its verdict, which it does (the energy-fields column already carries the `domain_energy_reduce` rough-in down-link at `energy-fields.L4.md:8,48,62,134,156` — confirmed on disk, exact lines match). Record-definition sub-check: the report's signature sketch names `DomainOpMap` (first arg) and `DomainData` (result). `DomainData` already has a definition home (`energy-fields.L4.md:83+` `## Record definition` — confirmed on disk); the report correctly notes this. `DomainOpMap` has no definition home yet, but the report explicitly flags it in Open questions (`record-DomainOpMap-needs-definition-home`, routing it to the D3 harvester) — so it is correctly routed, not an undefined-by-use gap. No flag.

**rotation-quality — pass.** Not applicable in the strict sense: the report asserts no L_{n+1}→L_n rotation of its own. Its structural claim is a *reduce-shape classification* (the 5th member of the L4 algebra-of-folds family, reduce-to-per-domain-table) plus a collapse-refusal argument. The "more abstract / equational" judgment it makes (the verb names a doubly-folded structure as one reduction shape, unifying the electric/magnetic passes under the field-kind axis) is genuine abstraction value, not a 1:1 rename — consistent with the redirect's abstraction-value test. Pass.

**variant-axis-coverage — pass.** The report enumerates the variant axes explicitly: field-kind {electric | magnetic} (the load-bearing axis, absorbed into the `DomainOpMap`+`Field` args), element-type (complex field / real energy, the `E.HasImag()` imag-part accumulation), and the field-absent degenerate pass (all-zero rows). No hidden branches — the field-kind axis is named as THE load-bearing one and the two source loops it covers are both cited. As a probe (not a firm authoring), axis *coverage* is correctly deferred to D3/harvester, but the axes are surfaced for that handoff.

**cross-reference-integrity — pass.** Every artifact `[link]`/slug reference resolves: `book/src/L4/gram_reduce.md`, `eigenfreq_qfactor_reduce.md`, `sparameter_reduce.md`, `book/src/L1/participation_ratio.md`, `book/src/L1/matrix-weighted-norm.md`, `book/src/feature/energy-fields.L4.md` all exist on disk. The slug `domain_energy_reduce` does NOT yet have a file (`book/src/L4/domain_energy_reduce.md` absent) — correct, since the verdict's entire point is that D3/harvester mints it; the report does not claim the file exists, it confirms it should be authored. The cited line ranges in the cross-referenced chapters check out (`gram_reduce.md:178-189`, `:213-223`; `eigenfreq_qfactor_reduce.md:36-41`; `energy-fields.L4.md:83-106` record def, `:156` dep-map row). No broken links.

**edge-label-fidelity — pass.** No lowering edge label is carried (this is an L4-placement probe, not a lowering theme). The report's layer-placement rationale (L4, not inline/L1/L2/L3) discusses the correct relationships — L4 fold over L1 primitives, identity-in-form body lowering to L1 (matching `gram_reduce`/`eigenfreq_qfactor_reduce` disposition) — with no edge-direction mismatch. Pass.

**plan-kind-consistency — pass.** Declared shape is an observation-only `combinator-miner` confirm-probe (`scope: ...observation-only`, status `pending`, "Proposed changes: NONE to `book/`"). The content matches exactly: a verdict (DISTINCT-VERB-WARRANTED) + collapse-refusal reasoning + harvester-firming notes, no artifact mutation, no rough-in row emitted (correctly, because the slug is already forward-referenced — matching the role-spec "emit a dep-map row only when the slug is NOT yet referenced"). Kind and content are consistent.

**skill-uptake-survey — pass (telemetry).** The report states all L0 citations were "self-verified on-disk this dispatch via palace-codemap `read_range` / `get_symbol_def`" — MCP-first localization is referenced, consistent with the codified preference. Note: the on-disk verification claim is somewhat in tension with the citation-validity finding — the *line ranges* were evidently verified (they are all correct), but the *path form* written into the report does not match the resolvable/artifact-canonical form, so the verification did not catch the path drift. Surfacing as telemetry, not blocking. The combinator-miner write-leak watch (friction `specialized_agent_direct_write_leak`, combinator-miner 2-of-5): `git status --porcelain book/` and `git diff --stat HEAD -- book/` are both empty — the probe is CLEAN, no `book/` mutation leaked. Leak watch clears for this dispatch.

### Issues found

1. **Non-canonical L0 citation path form on the three load-bearing Palace pinpoints — `citation-validity` warning.** Location: report body Pattern-instances (`:38-58`), Why-DISTINCT-VERB (`:127-128`), Layer-placement, and Supporting-evidence (`:203-210`). The citations are written `reference/palace/models/postoperator.cpp:...` and `reference/palace/models/domainpostoperator.cpp:...`. These FAIL `citecheck.py` resolution (3 `[MISS]`). The on-disk file is `reference/palace/palace/models/...`; the artifact-canonical, tool-resolvable form (matching 27 existing `book/src` occurrences and the energy-fields column's own dep-map row at `:156`) is `palace/models/postoperator.cpp` (no `reference/` prefix). The line ranges themselves are ALL valid under the correct path. Severity: low-moderate — evidence is sound, but the path form is mechanically broken on the report's most load-bearing L0 anchors, and a downstream harvester copying these citations into the minted `domain_energy_reduce.md` would propagate a non-resolvable path into the firm artifact. Repair candidate: normalize the path prefix on every Palace-source citation in the report to the `palace/models/...` form.

2. **Minor guard-line pin drift (cosmetic) — within `citation-validity` warning.** Location: Supporting-evidence `:206-207` and Open-questions `:238-240`. The participation-guard expressions are cited at `postoperator.cpp:1038` (electric) and `:1063` (magnetic); the `std::abs(...)` guard statements are actually on `:1039` and `:1064` respectively. Both fall inside the enclosing loop ranges (`:1036-1042` / `:1061-1066`) the report also cites, and the asymmetry claim (electric guards the numerator `energy_i`, magnetic guards the denominator `energy`) is factually correct on disk. Severity: cosmetic — flagging for completeness, optional repair.

3. **Self-attested on-disk verification did not catch the path drift — `skill-uptake-survey` telemetry, non-blocking.** Location: Supporting-evidence `:200-201`. The report asserts all L0 citations were "self-verified on-disk this dispatch." The line ranges are indeed correct, so the codemap read happened — but the path *as written into the report* is not the resolvable form, so the self-verification step verified content without normalizing the citation string. Surfacing as a procedural observation; the verdict reasoning is unaffected.

**Verdict clarity (for the downstream harvester):** the DISTINCT-VERB-WARRANTED verdict is stated unambiguously (`:15`, `:29` "D3 (Wave 2 / harvester) mints `book/src/L4/domain_energy_reduce.md`"), with a clear handoff: target layer (L4), reduce-shape class (5th algebra-of-folds member), signature sketch, three named variant axes, four harvester-firming Open-questions (land `rough-in` not `firm`; pick the uniform total-guard; `DomainOpMap` definition home; config-conditional `Σ p_i = 1` law). A harvester can act on this directly. No clarity issue.

## Repair

### Fixes attempted

- **Finding 1 — Non-canonical L0 citation path form on the three load-bearing Palace pinpoints (`citation-validity` warning).** The three citations were written `reference/palace/models/postoperator.cpp:1036-1042`, `reference/palace/models/postoperator.cpp:1061-1066`, and `reference/palace/models/domainpostoperator.cpp:255-275` — the `reference/` prefix + dropped inner `palace/` segment made all three `[MISS]` under `citecheck.py`.
  - **Decision**: repaired.
  - **Action**: rewrote all three to the artifact-canonical, tool-resolvable single-`palace` form (`palace/models/postoperator.cpp:...`, `palace/models/domainpostoperator.cpp:...`) at CYCLE.md §Pattern-instances Instance-1 (`:37`), Instance-2 (`:45`), Instance-3 (`:53`). Mechanical path-prefix normalization; the line ranges were already correct and in-bounds. Matches the 27 existing `book/src` occurrences and the energy-fields column dep-map row. (The Supporting-evidence citations at `:203`/`:208` already used the canonical form; the bare-filename continuation refs — `postoperator.cpp:1036`, `domainpostoperator.cpp:255-298`, etc. — resolve via citecheck's basename fallback and were left as-is.)

- **Finding 2 — Minor guard-line pin drift (cosmetic, within `citation-validity` warning).** Report cited the participation guards at `:1038` (electric) / `:1063` (magnetic); the `std::abs(...)` guard statements are on `:1039` / `:1064`.
  - **Decision**: repaired.
  - **Action**: bumped both pins at CYCLE.md §Supporting-evidence (`:206-207`) and §Open-questions participation-guard-asymmetry drive-by (`:239`). Verified on disk: electric `std::abs(energy_i) > 0.0` is `postoperator.cpp:1039`, magnetic `std::abs(energy) > 0.0` is `:1064`. Both remain inside the cited enclosing loop ranges (`:1036-1042` / `:1061-1066`).

- **Finding 3 — Self-attested on-disk verification did not catch the path drift (`skill-uptake-survey` telemetry, non-blocking).**
  - **Decision**: not-needed (telemetry-only; the critic surfaced it as a procedural observation, not an authoring or content gap). The path-form defect it observed is fixed by Finding-1's repair; no separate action.

### Repair verification

Re-ran `citecheck.py --scan` on the repaired CYCLE.md: **22 ok / 0 failing** (was 20 ok / 3 `[MISS]`). All three previously-failing L0 pinpoints now resolve to `reference/palace/palace/models/...`; the two bumped guard pins (`:1039`, `:1064`) resolve in-bounds.

### Unrepairable findings

None. Both citation-validity sub-issues were mechanical path/pin drift, fully in repair scope. The other 7 checks passed at critique.

## Suggested resolution

`overall_status: ready`. This is an observation-only confirm-probe with no `book/` changes proposed; the integrator applies no artifact surface from it. The DISTINCT-VERB-WARRANTED verdict + four harvester-firming Open-questions are the durable output for the downstream D3 harvester (which mints `book/src/L4/domain_energy_reduce.md`). Note for the integrator: D3 has already run this batch; the citation repair is for record-correctness so any future copy of these L0 pinpoints from the probe carries the resolvable `palace/models/...` form. Promote the four Open-questions (`rough-in`-not-`firm` gate; uniform total-guard choice; `record-DomainOpMap-needs-definition-home`; config-conditional `Σ p_i = 1` law) to the OQ ledger per normal per-report flow.
