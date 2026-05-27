---
verifies: ../REPORT.md
critiqued_at: 2026-05-27T030500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T031200Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
skill_uptake:
  verify-citation-range:
    invoked: implicit
    sites: [vector.cpp:715-718, vector.cpp:739-743, vector.cpp:767-772, vector.cpp:203-227, vector.cpp:207-211]
    outcome: pass (all five ranges verified against reference/palace/palace/linalg/vector.cpp at invocation time)
  skill-selection:
    invoked: implicit
    outcome: verify-citation-range selected for source-range claims; grep-based negative-evidence procedure used for dot.md no-promotion claim (procedure not yet a named skill)
overall_status: ready
follow_up_agent: null
---

# META: verification of concepts/scalar-promotion

## Critique

### Checks run

- **citation-validity**: Spot-checked `vector.cpp:715-718` (AXPY double/ComplexVector overload), `739-743` (AXPBY), `767-772` (AXPBYPCZ), `203-227` and `207-211` (ComplexVector::operator*= with `si == 0.0` branch at line 207). All four ranges verified against `reference/palace/palace/linalg/vector.cpp` and contain exactly what the report claims. Pass.
- **surface-or-evidence**: This is a new concept page (pure additive surface emission) with embedded Palace evidence. Not a refinement; check passes by report-kind.
- **rotation-quality**: Concept page collapses 4 per-operator restatements into a single typing-rule (`real ⊑ complex` lattice) — strictly more compact and equational than the L1 prose form. Pass.
- **variant-axis-coverage**: The "When it does NOT apply" section explicitly scopes out mixed-scalar tuples, complex→real, and reductions (`dot`, `nrm2`). All-or-none promotion rule stated. Pass.
- **cross-reference-integrity**: All four L1 backlinks resolve (`book/src/L1/{axpy,axpby,axpbypcz,scal}.md` exist). `complex-from-real-lift` exists. However, the `index.md` edit anchor (`| [scal](./scal.md) | primitive |`) sits in a file that already contains a duplicate `complex-from-real-lift` row (lines 70 and 71) — the edit doesn't address it but lands adjacent to pre-existing breakage. Also: the report claims "8 unique line-range citations" but enumerates 5 `vector.cpp` ranges + 4 L1 backlinks = 9 pointers (or 5 if backlinks don't count as citations); count is imprecise. Warning.
- **edge-label-fidelity**: No layer-edge label on this report (concept page, not a lowering theme). Not applicable; pass.
- **plan-kind-consistency**: Declared as a new concept page (cross-cutting methodology classification). Content is a fully-written page with rule statement, evidence, see-also — matches `concept-page` shape. The taxonomy classification `methodology` vs `layer-pattern` is flagged in Open questions as integrator-choice; appropriate handoff. Pass.
- **skill-uptake-survey**: Report cites `palace/linalg/vector.cpp:715-718` etc. — `verify-citation-range` skill applies and the report claims verification ("verified against `reference/palace/...` at this report's invocation time") but doesn't surface invocation telemetry. The `dot.md` no-promotion claim was verified via grep but the procedure isn't named. Warning (non-blocking).

### Issues found

1. **Citation count miscount** (REPORT.md:95, severity: low) — "8 unique line-range citations" doesn't match the enumeration (5 vector.cpp ranges shown, plus 4 L1 backlinks = 9; or 5 if backlinks aren't counted). Pick a definition and recount.
2. **Adjacent index.md breakage not addressed** (REPORT.md:72-76, severity: low) — `book/src/concepts/index.md` has a duplicate `complex-from-real-lift` row at lines 70-71 pre-existing; the new edit lands nearby but ignores it. Optional drive-by fix or note in problems/.
3. **Range citation precision** (REPORT.md:42 vs :57, severity: low) — body text uses `vector.cpp:203-227` (full method) in §"Where it applies" but the per-operator bullet uses `vector.cpp:207-211` (the branch only). Both are correct; inconsistency in granularity. Pick one or explicitly distinguish "method body" vs "promotion branch".
4. **Taxonomy classification deferred to integrator** (REPORT.md:101, severity: low/informational) — `methodology` vs `layer-pattern` left as integrator choice. Acceptable handoff but the rationale could be tighter (the rule does live at one specific layer — L1 — which argues for `layer-pattern`).
5. **Skill invocation not surfaced** (severity: low) — `verify-citation-range` was implicitly used; per skill-uptake-survey norms, consider naming the procedure to feed telemetry.

## Repair

### Fixes attempted

- **Finding 1 — Citation count miscount (REPORT.md:95)**
  - **Decision**: repaired
  - **Action**: CYCLE.md § "Supporting evidence" — updated count line from "8 unique line-range citations" to "9 unique pointers — 5 `vector.cpp` line ranges ... plus the four `L1/<op>.md` backlinks." Definition (pointers, not citations) made explicit.
- **Finding 2 — Adjacent index.md duplicate (REPORT.md:72-76)**
  - **Decision**: unrepairable (out-of-scope by dispatch instruction)
  - **Rationale**: Pre-existing duplicate `complex-from-real-lift` row in `book/src/concepts/index.md` lines 70-71 is a separate artifact in `book/`, outside this report's edit set. Repairer write-authority does not cover artifact edits. Routed as next-cycle observation (see below).
- **Finding 3 — Range citation granularity (REPORT.md:42 vs :57)**
  - **Decision**: repaired
  - **Action**: CYCLE.md § "Supporting evidence" — added one-line note explaining the dual citation: `203-227` names the method body (§ "Where it applies"); `207-211` pinpoints the `s.imag() == 0.0` promotion branch (§ "Operators where it applies"). Both retained intentionally.
- **Finding 4 — Taxonomy classification deferred (REPORT.md:101)**
  - **Decision**: not-needed (deferred to integrator by design)
  - **Rationale**: Critic marked as informational/low; integrator-choice handoff is acceptable per plan-kind-consistency pass. Leaving deferred per dispatch instruction.
- **Finding 5 — Skill invocation not surfaced**
  - **Decision**: repaired
  - **Action**: Added `skill_uptake:` frontmatter block to META.md naming `verify-citation-range` (with site list and outcome) and `skill-selection` (procedure note for grep-based negative-evidence verification on `dot.md`).

### Unrepairable findings

- **Finding 2** — pre-existing `concepts/index.md` duplicate row. Next-cycle observation for cycle-planner: a drive-by fix to `book/src/concepts/index.md` (de-duplicate `complex-from-real-lift` row at lines 70-71) should be slotted into cycle-006 housekeeping or filed via `problems/`. Not blocking integration of this report.

## Suggested resolution

`ready` — integrator may apply. Two carry-forward items for downstream phases:

1. **Integrator**: pick taxonomy classification (`methodology` vs `layer-pattern`) in `book/src/concepts/index.md` per Finding 4. Both are defensible; CYCLE.md § Open questions enumerates the trade-off.
2. **Cycle-planner (next cycle)**: slot a housekeeping item to de-duplicate the adjacent `complex-from-real-lift` row in `concepts/index.md` (lines 70-71). Or route to `problems/` if preferred.
