---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T155733Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: warning
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T160500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: repaired
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of residual-L2>L1-gap census (krylov-step + ksp_solve both genuine-missing)

## Critique

### Checks run

**citation-validity — pass.** The load-bearing anchors all check out against disk.
- `book/src/L2/krylov-step.md:121` — verbatim "the L2 form is uniformly out-of-place, **with the in-place specialisation reappearing in the L2>L1 lowering**" (variant-axis 6). The report's "forward-reference to an L2>L1 lowering that has no file" reading is exact.
- The report's claim that `krylov-step` has **no** §"Lowers from" / §"Downward to L1" section is confirmed by heading enumeration: `## ` headings are Context(5), Signature(13), Semantics(38), Algebraic laws(71), Dependencies(92), Variant axes(112), Status(125), L2 vs L1 distinction(129), Evidence(134) — no lowering section. The cited heading anchors `:92,125,129,134` are correct.
- `book/src/L2/ksp_solve.md:155-157` — §"Lowers from" (header at :155) carries "The rotation is *not* identity: L1 opacity is opened at L2…" (the "un-collapse" forward-narration) at :157. Confirmed verbatim. The report's :153 (§Status, firm) and :161 (§"Lifts to", links the L3>L2 theme) are accurate.
- `book/src/L3/apply_linop.md:142-146` — the no-L2-by-design precedent ("no interposed L2 entry, no L3-L2 theme … the L2 layer does not host an `apply_linop` entry") is verbatim at :144-146. The report's structural-difference argument (apply_linop has *no L2 entry*; krylov-step/ksp_solve have firm L2 entries) is faithful to the source.
- Mechanical scan: `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet` → `12 ok, 0 failing`. The Palace-source-relative citations (the `iterative.cpp` / `ksp.cpp` ranges reached transitively via the chapters) are in-bounds; the `book/src/*` anchors (not Palace-relative, so out of citecheck's map) were verified by hand above.

**surface-or-evidence — warning.** The gap-set (the *which-ops* finding) is accurate, but the census *denominator narrative* is off by one and self-inconsistent. The report repeatedly states "**21** `L2-L1/` theme files" (Summary :11; mechanics :45; Supporting evidence :76) and reconstructs that count as "20 `| [...]` rows plus the eigsolve row in the prose list." On disk there are **20** theme files (`ls book/src/L2-L1/*.md | grep -v index | wc -l` = 20) and `L2-L1/index.md` carries exactly **20** `| [` table rows — and `eigsolve-spectral-transform-composition` IS one of those 20 rows (index.md:30), NOT a separate prose-list entry. There is no 21st theme. The correct arithmetic is **22 L2 ops − 20 themed = 2 gaps**, which is exactly the report's gap-set; the "21" is a miscount that does not change the conclusion but mis-states the coverage denominator. Separately, I independently re-ran the enumeration: all 20 covered-row themes named in the table (lines 22-43) exist on disk; none is missing or mis-stemmed; the two flagged gaps (`krylov-step`, `ksp_solve`) are the only two firm L2 ops with no same-stem theme. I also confirmed no OTHER L2 op is silently uncovered — `eigsolve` (which the dep-map at index.md:95 likewise marks **non-identity L2↔L1**) DOES carry its theme, and `deflate` (partly-constructive) carries `deflate-composition-lowering`. So the substance is sound; only the total-count framing is defective.

**rotation-quality — pass (applied to the audit's rotation classification).** No rotation is *authored* here (observation-only). The check applies to the audit's *judgment* that the two missing rotations are non-identity/substantive. That judgment is corroborated by the corpus: `L2/ksp_solve.md:157` states the L1-opacity un-collapse is non-identity (state-hiding opened into a kernel-fold composition — a genuine abstraction rotation, not a renaming); `L2/krylov-step.md:96` shows the kernel composes seven L1 primitives under a fold (de-fusion into leaves + in-place→out-of-place buffer rotation — coarser-to-finer, substantive). The parallel with `eigsolve` (non-identity L2↔L1 AND a theme, index.md:95) makes the "non-identity ⇒ warrants a theme" inference consistent with established practice.

**variant-axis-coverage — pass.** Not a refinement proposal; no operator/theme is authored. The audit's recommendation does note `krylov-step`'s in-place-buffer variant axis (`:121`) as the specific content the missing theme would home — i.e. the audit is aware the gap has a variant-axis dimension. No hidden branch.

**cross-reference-integrity — pass.** Every slug the report names resolves: all 20 covered-row theme files exist (verified by per-slug `[ -f ]` sweep); `L3-L2/ksp-solve-outer-driver.md`, `L3/apply_linop.md`, `L2-L1/eigsolve-spectral-transform-composition.md` all exist and say what the report attributes to them. The two gap slugs are correctly identified as *absent* (no `L2-L1/krylov-step*` or `L2-L1/ksp-solve*` file). Recommendation slugs (`krylov-step-kernel-defusion`, `ksp-solve-outer-driver-unfold`) are proposed-new, correctly not asserted to exist.

**edge-label-fidelity — pass (the load-bearing check; the report's own caveat is resolved in the report's favor).** The audit's genuine-gap-vs-edge-mislabel classification turns on one question the report explicitly flagged as read-only-by-reference: does `L3-L2/ksp-solve-outer-driver` silently carry the *L2>L1* content (which would make `ksp_solve` an edge-mislabel, not a coverage gap)? I read that file in full. It is unambiguously an **L3>L2** theme: LHS = the L3 explicit `iterate_while_L3` tail recursion (:21-38), RHS = the L2 outer-driver-by-role wrap (:40-57); the rewrite is the iteration-view erasure between L3 and L2. It explicitly delegates the L2>L1 rotation elsewhere — line 15 lists "**L2>L1 firm** (recorded in-line in the L2 entry's §'Lowers from') — the un-collapse of the L1 opacity … non-identity" as a *separate* edge. So the L3>L2 file does NOT carry the L2>L1 content; `ksp_solve`'s L2>L1 edge is a genuine missing-dedicated-theme gap, not a mislabel. The report's caveat was honest and is now closed in its favor — a strengthening, not a contradiction. The kernel/driver edge labels in the report (L2>L1 for both) match the prose throughout.

One fidelity nuance the integrator/repairer should weigh (not a fail): for `ksp_solve` the L2>L1 rotation *is* narrated in-chapter at `L2/ksp_solve.md:155-157` per the high→low discipline; the gap is specifically the absence of a dedicated `L2-L1/*` theme *file*, not the absence of any L2>L1 statement. The report does represent this accurately (lines 50, 52) but the Summary's "neither has a theme" phrasing could read as "neither has any L2>L1 treatment," which is not quite true for `ksp_solve`. `krylov-step` is the stronger gap (no section AND no theme AND a dangling forward-reference).

**plan-kind-consistency — pass.** Declared shape is an observation/coverage-gap audit (frontmatter `agent: cross-layer-cross-cutter`, no `book/` mutation, deliverable = census + classification + ranked recommendation). Content matches: it is a census with a genuine-vs-by-design judgment and a fan-out-ranked cycle-047 recommendation, no artifact edits. No firm/rough-in mis-tagging (the audit makes no maturity claims about new entries).

**skill-uptake-survey — pass (telemetry only).** The audit's shape (verifying citation ranges + an inherited by-design precedent) maps to `verify-citation-range` (which carries an "Audit-report / inherited-citation sub-case"); the report does not name an invoked skill. Non-blocking. A `classify-coverage-gap-genuine-vs-by-design` procedure is not yet a skill; the audit's genuine-vs-by-design test (compare against the apply_linop no-L2-by-design precedent; require a *firm L2 entry* + *non-identity in-chapter rotation* for genuine-gap) is a crisp, reusable checklist and is a reasonable skill candidate if the pattern recurs.

### Issues found

1. **Theme-file count mis-stated as 21; actual is 20** — `CYCLE.md` Summary (:11), census mechanics (:45), Supporting evidence (:76). Disk has 20 `L2-L1/*.md` theme files (minus index) and `L2-L1/index.md` has exactly 20 `| [` table rows; `eigsolve-spectral-transform-composition` is one of those 20 rows, not a separate "prose-list" 21st. The "20 `| [...]` rows + eigsolve prose row = 21" reconstruction (:45) is the source of the error. Severity: low — the gap-set (22 ops − 20 themed = 2 gaps) and every per-op classification are unaffected; only the coverage denominator narrative is wrong. Repair = restate as 20 themes / 22 ops; drop the phantom eigsolve "prose row."

2. **Caveat resolved by critic; should not be carried as open follow-up** — `CYCLE.md` Open questions/caveats (:84). The report flags that it read `L3-L2/ksp-solve-outer-driver` only by reference and that the L2>L1 content *might* be silently parked there (edge-mislabel risk). I read the file in full: it is an L3>L2 theme that explicitly delegates the L2>L1 edge to the L2 chapter's in-line §"Lowers from" (`ksp-solve-outer-driver.md:15`). The mislabel risk does not materialize; `ksp_solve` is a genuine L2>L1 gap. Severity: low — the caveat was appropriate to raise; it is now closeable. The "follow-up should confirm" recommendation can be marked resolved rather than propagated to cycle-047.

3. **Summary phrasing "neither has a theme" understates `ksp_solve`'s in-chapter coverage** — `CYCLE.md` Summary (:11), Observation kind (:14). `ksp_solve` DOES carry an in-chapter L2>L1 forward-narration (`L2/ksp_solve.md:155-157`, §"Lowers from", non-identity); the precise gap is the absence of a dedicated `L2-L1/*` theme file. The body of the report states this correctly (:50, :52), so this is a Summary-vs-body tightness issue, not a factual error. `krylov-step` is the unqualified gap (no section, no theme, dangling `:121` forward-ref). Severity: low — clarify the Summary to distinguish "no dedicated theme file" (both) from "no in-chapter L2>L1 statement" (krylov-step only).

4. **No skill invocation surfaced for the citation-range / inherited-precedent verification** — whole report. The audit performs exactly the `verify-citation-range` "inherited-citation / by-design-precedent" sub-case but does not reference it. Severity: informational (skill-uptake telemetry, non-blocking).

---

repaired_at: 2026-06-01T160500Z
repairer_version: 1

## Repair

### Fixes attempted

- **Finding 1 (surface-or-evidence warning): theme-file count mis-stated as 21; actual is 20.**
  - **Decision**: repaired.
  - **Action**: Verified against disk (`ls book/src/L2-L1/*.md | grep -v index | wc -l` = 20; `grep -c '^| \[' book/src/L2-L1/index.md` = 20; `eigsolve-spectral-transform-composition.md` is one of the 20 files AND one of the 20 index rows — no phantom 21st). Corrected the three census-denominator occurrences: CYCLE.md Summary (:11, "21 `L2-L1/` theme files" → "20"), census mechanics (:45, dropped the phantom "+ eigsolve prose row", restated "20 themes total" + added explicit "22 − 20 = 2 gaps" arithmetic), Supporting evidence (:76, "21 theme files" → "20"; "20 rows + eigsolve prose row" → "20 rows; eigsolve is one of those rows"). Left untouched the unrelated *firm-operator* counts ("21 firm" L2 ops at scope-line / :11 / :75) and every "L2>L1" edge-label occurrence — none is the theme miscount. The gap-set and all per-op classifications were already correct and are unchanged.
  - **Rationale**: mechanical count correction against disk; no content authored.

- **Finding 3 (edge-label-fidelity nuance): Summary "neither has a theme" understates `ksp_solve`'s in-chapter coverage.**
  - **Decision**: repaired.
  - **Action**: Reworded CYCLE.md Summary (:11) and §Observation-kind (:14) to state the gap precisely — both operators lack a *dedicated `L2-L1/*` theme file*, with the parenthetical that `ksp_solve` DOES carry an in-chapter §"Lowers from" L2>L1 narration while `krylov-step` has no §"Lowers from" section at all. The report body already stated this correctly (:50, :52); this tightens the Summary to match.
  - **Rationale**: surgical phrasing precision; the distinction was already present in the body, only the Summary over-generalized.

- **Finding 2 (resolved caveat carried as open follow-up): caveat should be marked CLOSED.**
  - **Decision**: repaired.
  - **Action**: Split the CYCLE.md §"Open questions / caveats" first bullet (:84). Kept the factual "planner undercounted by one" note; extracted the edge-mislabel-risk caveat into a new **[CLOSED — resolved in critique]** bullet recording that the critic read `L3-L2/ksp-solve-outer-driver.md` in full and confirmed it is an L3>L2 theme that explicitly delegates the L2>L1 edge in-line to the L2 chapter's §"Lowers from" (`ksp-solve-outer-driver.md:15`), so `ksp_solve` is a genuine missing-dedicated-theme gap, not an edge-mislabel. Removed the "a follow-up should confirm" propagation to cycle-047.
  - **Rationale**: mechanical status update reflecting the critic's in-favor resolution; no new judgment introduced.

### Unrepairable findings

None. Finding 4 (skill-uptake telemetry) is informational/non-blocking per the critic and requires no repair.

## Suggested resolution

`ready`. The core finding — both `krylov-step` and `ksp_solve` are genuine missing-dedicated-L2>L1-theme gaps — was confirmed SOUND by the critic, who resolved the report's own edge-mislabel caveat in its favor by reading `L3-L2/ksp-solve-outer-driver.md` in full. The three repaired items were narrative-accuracy fixes (off-by-one denominator, Summary phrasing precision, resolved-caveat status) that do not invert the verdict. Integrator note: this is an observation-only audit with no `book/` mutation; the actionable output is the cycle-047 fan-out-ranked recommendation to dispatch abstractor ×2 (or one paired dispatch) on `ksp-solve-outer-driver-unfold` (rank HIGHER) and `krylov-step-kernel-defusion` (rank HIGH), plus the still-open factual note that the planner's pre-dispatch cross-check undercounted the gap-set by one (it should be 2, not 1).
