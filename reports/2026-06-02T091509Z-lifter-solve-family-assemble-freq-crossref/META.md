---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T093000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
---

# META: verification of "Re-anchor solve_family map_solve scope-boundary cross-ref"

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` reports 6 ok / 0 failing. The load-bearing L0 pinpoint `drivensolver.cpp:176-180` was re-verified against source via `palace-codemap read_range` (lines 168-182): `:176-177` is `auto A = space_op.GetSystemMatrix(1.0+0.0i, 1i*omega, -omega*omega+0.0i, K, C, M, A2)` (the per-ω rebuild), `:180` is `ksp.SetOperators(*A, *P)` (per-ω capture). The framing sentence's affine form `A(ω)=K+iω·C−ω²·M+A2(ω)` matches the source weights exactly (1·K + iω·C − ω²·M + A2). The `assemble_frequency_operator` description (operator-operand specialization of `linear_combination`, fixed-basis affine, per-ω rebuild) is confirmed against the L1 entry's own §intro (`:18`, `:24`) and §Status (`:132`). No `verified_against:` YAML block in this report (not applicable). No proposed-changes fences carry nested code, no YAML round-trip sub-check needed.

**surface-or-evidence — pass.** Not a refinement of an operator's algebraic surface — this is a pure cross-reference firming on a §Status scope-boundary note (allowed retroactive cross-ref backfill: a now-firm L1 operator is named where it was previously referred to only by L0 site). No rotation_claim is asserted; none owed.

**rotation-quality — pass (not applicable).** No algebraic/structural rotation is claimed; this is a cross-ref/naming edit, not a layer rotation.

**variant-axis-coverage — pass.** The edit does not touch `solve_family`'s variant axes. The framing sentence correctly invokes the existing `operator-capture = {fixed | per-element}` axis to locate driven on the `per-element` side; this is consistent with the axis as authored at line 137. No hidden branch introduced.

**cross-reference-integrity — pass.** The new live link `../L1/assemble_frequency_operator.md` resolves: the file exists on disk (landed c062, `firmness: firm`), is wired into `SUMMARY.md:134`, and the `../L1/` cross-Part relative-link form is the established convention in this directory (e.g. `L4/eigsolve.md` uses `../L1/eigsolve.md`, `../L2/eigsolve.md`, `../L3/eigsolve.md`). The reciprocal L1→L4 cross-ref the lifter cites (`assemble_frequency_operator.md:24`, `:116`) is present and names the same scope boundary, so the bidirectional link is now mutual. No firm-body-inside-fence concern (the edit is a single prose-paragraph substring, not a chapter body). All other links in the `[new]` text (`./fold_solve.md`, the report path) are unchanged from `[old]`.

**edge-label-fidelity — pass (not applicable).** No edge label on this proposal (it is an in-layer L4 entry touch with a downward L4→L1 reference, not a lowering theme). The downward direction of the added link is consistent with high→low discipline.

**plan-kind-consistency — pass.** Confirmed the edit is genuinely surgical and status-preserving. `solve_family`'s `## Status` line remains `rough-in (test-coverage-bounded)` (frontmatter `:4` + body `:144` untouched); signature, algebraic laws, variant axes, and evidence block are all outside the matched `[old]` region and unmodified. No status flip ⇒ no `book/src/L4/index.md` status-cell update owed (the lifter's "No index-cell status flip" note at Discipline-notes is correct). The `[new]` text is a single inserted sentence restating, with the now-firm name, what lines 65/90/137/146 already assert abstractly (driven's per-ω rebuild = the `per-element` superset operator) — no new claim. Edit kind (cross-ref firming) matches content shape.

### Issues found

1. **(Non-blocking, INFO) `[old]`/`[new]` is a substring of line 146, not the full paragraph** — `reports/.../CYCLE.md` Proposed-changes. The matched region ends at "...beyond the two fixed-operator witnesses."; the on-disk paragraph continues with "The general superset is **batch-17 future work**...". The `[new]` block ends at the same boundary, so the trailing batch-17 sentence is correctly preserved (it falls after the matched region). The `[old]` substring is unique in the file, so the integrator's exact-match apply is unambiguous. No action needed — flagging only so the integrator knows the match is intentionally a leading substring, not the whole line.

2. **(Non-blocking, skill-uptake-survey warning) 3 sibling per-ω-rebuild loci left un-named; no skill invocation referenced** — `solve_family.md` lines 65, 90, 137 each cite `drivensolver.cpp:176-180` abstractly without naming `assemble_frequency_operator`. The lifter flagged this deliberately (Discipline note 3 + Open-questions) as out-of-scope for the surgical single-locus instruction, deferring it as a non-blocking optional follow-up. This is an **acceptable** scoping call: (a) the §Status scope-boundary note (line 146) is the canonical navigable home for the `map_solve` boundary and now carries the live link; (b) the other three are law/typing loci where the abstract `drivensolver.cpp:176-180` reference is sufficient and naming would be decoration; (c) the lifter verified there is no signature contradiction at any of the four loci. Recommend the follow-up be recorded as a low-value OQ/plan candidate (name the operator at all four loci in one pass) rather than left implicit — the report does flag it, which satisfies the bar. Skill-uptake note: the report does not reference `upgrade-plain-text-ref-to-live-link-when-target-on-disk`, which is the on-point skill for exactly this on-disk→live-link upgrade (the abstract L0 reference is effectively a plain-text reference to a now-on-disk firm operator); the procedure was followed in substance (verified target on disk before linking), so this is a telemetry warning, not a defect.

3. **(Non-blocking, INFO) frontmatter `verifies: ../REPORT.md`** — this critique's own frontmatter points at `../REPORT.md` per the template, but the report file in this dir is `CYCLE.md` (the post-cycle-004 rename). Cosmetic template artifact; the integrator reads META.md by directory, not by this pointer.

---
repaired_at: 2026-06-02T094500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey warning — the report follows the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` procedure in substance (verified `assemble_frequency_operator.md` on disk before linking) but does not cite the skill by slug.
  - **Decision**: not-needed
  - **Rationale**: telemetry-only. The critic confirms the procedure was followed correctly and the on-disk→live-link upgrade is sound; the missing slug citation is an instrumentation gap, not a content or correctness defect. Editing the producer's CYCLE.md to retro-insert a skill slug would author provenance the producer did not record — out of repair authority and not load-bearing for integration. No surgical fix applies.

- **Finding**: INFO note 1 — `[old]`/`[new]` is an intentional leading substring of line 146 (not the full paragraph).
  - **Decision**: not-needed
  - **Rationale**: the substring is unique in the file, so the integrator's exact-match apply is unambiguous and the trailing batch-17 sentence is correctly preserved outside the matched region. The match is intentional and correct as written; nothing to repair.

- **Finding**: INFO note 3 — META.md frontmatter `verifies: ../REPORT.md` while the report file is `CYCLE.md`.
  - **Decision**: repaired
  - **Action**: META.md frontmatter — rewrote `verifies: ../REPORT.md` → `verifies: ../CYCLE.md` (frontmatter line only; the in-body INFO-note 3 quote of the old value is left intact as the critic's verbatim record). Trivial cosmetic pointer fix within repair authority.

### Unrepairable findings

None. The single warning is telemetry (no defect to fix); the substring INFO is correct-as-authored; the frontmatter pointer was repaired.

### OQ-intake note (carried from lifter Discipline note 3 + Open-questions)

The lifter deliberately scoped the edit to the single canonical §Status scope-boundary locus (line 146). Three sibling loci — `solve_family.md:65`, `:90`, `:137` — also reference `drivensolver.cpp:176-180` (the per-ω rebuild) abstractly without naming `assemble_frequency_operator`. The lifter left these un-named per the surgical single-locus instruction and flagged the breadth pass as a non-blocking optional follow-up; the critic concurred this is an acceptable scoping call (those three are law/typing loci where the abstract L0 reference is sufficient and naming would be decoration). Recorded here as a **low-value OQ/plan candidate**: name `assemble_frequency_operator` at all four solve_family loci in one breadth pass. Not a blocker; the canonical navigable home (line 146) now carries the live link.

## Suggested resolution

`ready` — apply as-is. The single warning is telemetry-only (the on-disk→live-link procedure was followed correctly; only the skill slug citation is absent), the substring match is unambiguous, and `solve_family`'s status / signature / laws / variant axes are untouched. The cosmetic `verifies:` frontmatter pointer was repaired in place. Integrator note: the optional 3-loci breadth pass above is a low-value future candidate, not owed by this report.
