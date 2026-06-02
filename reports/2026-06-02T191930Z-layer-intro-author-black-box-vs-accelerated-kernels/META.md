---
verifies: ./CYCLE.md
critiqued_at: 2026-06-02T192520Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T193340Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of concepts/black-box-vs-accelerated-kernels (NEW concept page + SUMMARY alpha-wire)

## Critique

### Checks run

**citation-validity — pass.** A concept page makes few hard L0 citations; this one forwards all algebraic/source detail to canonical-instance chapters (explicitly stated, lines 24-29 of CYCLE.md and the page body). The one source pinpoint the prose leans on (libCEED `A(space, ·)` leaf, `palace/fem/bilinearform.cpp:67-70` / `:87-90`) is correctly NOT re-cited — it is forwarded to `L1/fe_assemble.md`, which I confirmed owns those anchors (verified at `L1/fe_assemble.md:171-176`, the exact `bilinearform.cpp:67-70` / `:87-90` citation). No positive claim in the page contradicts its cited canonical chapters (see cross-reference detail below for the per-chapter consistency reads). No `verified_against:` block in this report, so that sub-check no-ops. Pass.

**surface-or-evidence — pass.** Not a refinement of an existing operator/theme; it is a NEW synthesized concept (classification-vocabulary) page explicitly framed as synthesized FROM project memory `project_blackbox_vs_accelerated_kernels` + the directive-2 banner, not a fresh derivation and not a surface-modifying rotation claim. The refinement-surface check is inapplicable to a new methodology-vocabulary page; no rotation_claim is asserted. Pass.

**rotation-quality — pass.** No algebraic/structural/reduction rotation is asserted (it is a classification page, not a lowering). The only "rises/stops-low" language is dispositional vocabulary, not an L_{n+1}→L_n compaction claim. Not applicable to a concept page. Pass.

**variant-axis-coverage — pass.** The page's three-way disposition (black-box / kept-named-abstraction / accelerated-kernel) IS itself an exhaustive enumeration of the classification axis, and it explicitly handles the boundary cases: the case-1-vs-enum-only-stub distinction (page lines 112-121), the case-2-vs-case-3 "both decompose, abstraction-value decides" distinction (lines 69-78), and the combinators-rise-regardless rule (lines 163-171) that covers both case-2-dual and case-3-replacement sub-paths. No hidden branch. Pass.

**cross-reference-integrity — warning.** I verified every live `[link]` target resolves on disk: `concepts/eigsolve|dot|nrm2|scal|ksp_solve|sequential-obstruction|scope-out-obstruction|solver-as-operator.md`, `L4/eigsolve|ksp_solve|fold_solve.md`, `L1/fe_assemble.md`, `L3/inner_product|linear_combination.md`, `design/l4_calculus.md` — all PRESENT. The report's central cross-ref claim holds: `L4/fe_assemble.md` is ABSENT on disk (I confirmed), and the page correctly does NOT live-link it — it references `L1/fe_assemble.md` (PRESENT) instead, avoiding a `linkcheck2` dead-link. This is handled exactly per the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention and flagged transparently in the report's OQ. The new page itself (`concepts/black-box-vs-accelerated-kernels.md`) is correctly ABSENT (it is what the edit creates). The single warning (not a dead link — the target resolves): the link `[L4-is-the-backend-lowering-target](./solver-as-operator.md)` appears twice (page lines 48-50 and 91-93) with link TEXT "L4-is-the-backend-lowering-target" pointing at the `solver-as-operator` concept page. The backend-lowering-target framing is the project-memory item `project_l4_is_backend_lowering_target`, which has no dedicated concept page; `solver-as-operator` is a related-but-distinct concept (it names the `Solver<OperType>` inheritance rotation, not the L4-feature-surface claim). The link resolves so the build is safe, but the text/target are mismatched — a reader clicking "L4-is-the-backend-lowering-target" lands on the solver-inheritance page, not a backend-lowering page. Warning, not fail.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (concept page, no lowering edge). Not applicable. Pass.

**plan-kind-consistency — pass.** Declared shape is a concept (vocabulary/structure) page; content matches — one-line statement + discriminating test + three dispositions + see-also, no operator signature or algebraic laws (correctly, the page disclaims having any of its own, page lines 40-42). No rough-in placeholders. Classification matches content shape. Pass.

**skill-uptake-survey — pass.** No skill invocation is strongly implied for a synthesized methodology-vocabulary page (the `summary-md-surgical-insert` skill is the nearest relevant procedure for the SUMMARY wire, and the report's anchor-uniqueness + alpha-position reasoning is consistent with that skill's procedure even if not named). Telemetry only; non-blocking. Pass.

### Issues found

1. **Link text/target mismatch on `L4-is-the-backend-lowering-target` → `./solver-as-operator.md`** (page body, two occurrences: §intro lines 48-50 and §"Black-box kernel" lines 91-93). Severity: low. The link resolves (no build break), but the anchor text names the L4-backend-lowering-target concept while the target is the `solver-as-operator` page, a distinct concept. Candidate repairs: (a) re-label the link text to "solver-as-operator" so text matches target; or (b) re-point to a more apt target if one exists (none does — `project_l4_is_backend_lowering_target` is a memory item, not a concept page); or (c) leave as-is and accept the gloss (the two concepts are adjacent). Surfaced for the repairer to decide; not a dead link.

2. **Directive-3 alpha-position is a local-cluster interpretation, transparently flagged** (`SUMMARY.md` insert, CYCLE.md lines 185-191 + OQ lines 225-239). Severity: informational. The dispatch spec's "between `axpy` and `build-time-vs-run-time-stratification`" is NOT a contiguous SUMMARY span — `axpy` is line 221, `build-time-vs-run-time-stratification` is line 248, and the concepts list is only locally alpha-sorted (the head BLAS-1 cluster `apply_linop`/`axpy`/`dot`/`nrm2`/`scal`, lines 220-224), not globally. I verified: the `[old]` anchor (the two-line `axpy`+`dot` pair) matches uniquely (line 221-222, single occurrence), and `black-box-vs-accelerated-kernels` does sort alphabetically after `axpy` and before `dot`/`build-time...`, so the insert position is alphabetically correct within the local cluster. The report correctly flags (OQ) that if directive-3 intends a global concepts-list re-sort, that is a larger meta-phase reorg out of this single-page dispatch's scope. No defect — the interpretation is sound and the ambiguity is surfaced for the integrator/meta-phase.

3. **No issue, recorded for completeness:** the page's case-1 "positive reframe of opaque-library-obstruction" claim (page lines 112-121) is strongly corroborated by `L4/eigsolve.md:20` and `concepts/eigsolve.md:101-129` (both frame eigsolve as a clean-surface opaque-library obstruction marker); the "combinators currently stop at L3" claim (page lines 170-171) is confirmed — `L4/inner_product.md` and `L4/linear_combination.md` are both ABSENT, so the combinators do stop at L3. No contradiction with cited canonical chapters.

## Repair

### Fixes attempted

- **Finding**: Link text/target mismatch — `[L4-is-the-backend-lowering-target](./solver-as-operator.md)` appears twice in the proposed concept page; the anchor TEXT names the L4-backend-lowering-target framing (a project-memory item with no concept page) while the TARGET is the distinct `solver-as-operator.md` page.
  - **Decision**: repaired
  - **Action**: Edited both occurrences in the `edit:book/src/concepts/black-box-vs-accelerated-kernels.md` proposed-changes block of `CYCLE.md`. Resolved per option (b) — drop the live-link, use plain text — because the surrounding prose in both sites clearly means the *principle* "L4 is the backend-lowering target," not the `solver-as-operator` concept:
    - §intro: `[L4-is-the-backend-lowering-target](./solver-as-operator.md) framing` → `**L4-is-the-backend-lowering-target** framing` (the sentence explicitly says "the L4-is-the-backend-lowering-target *framing*").
    - §"Black-box kernel": `see [L4-is-the-backend-lowering-target](./solver-as-operator.md)` → `this is the **L4-is-the-backend-lowering-target** principle` (the clause is about the backend supplying the implementation — the backend-lowering principle, not the solver-inheritance rotation).
  - **Rationale for option (b) over (a)**: option (a) would have re-labelled the text to "solver-as-operator", but the prose intent is the backend-lowering principle (memory item `project_l4_is_backend_lowering_target`), which has no concept page on disk; relabelling to `solver-as-operator` would have pointed the reader at a related-but-distinct concept and changed the author's meaning. Plain-text-ing the principle name preserves intent and matches the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention (no page on disk for the named concept). Mechanical/surgical: text-only substitution, no content authored.

### Unrepairable findings

None. The single warning was a mechanical link text/target mismatch, repaired in place. Issue 2 (directive-3 alpha-position) and Issue 3 (completeness note) were recorded by the critic as informational / no-defect — no repair needed; the alpha-position interpretation is sound and the SUMMARY insert was verified correct.

## Suggested resolution

`ready`. The concept page is integrable as proposed (after repair). Integrator note: the two `L4-is-the-backend-lowering-target` references are now plain text by design — if/when a dedicated `concepts/l4-backend-lowering-target.md` page is later authored (it is currently only a project-memory item), those two plain-text mentions become candidates for an on-disk→live-link upgrade (`upgrade-plain-text-ref-to-live-link-when-target-on-disk`). The directive-3 alpha-position OQ (global concepts-list re-sort vs. local head-cluster insert) remains correctly surfaced for the meta-phase's one-time reorg; not a per-report blocker.
