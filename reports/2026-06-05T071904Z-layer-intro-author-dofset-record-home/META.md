---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T073000Z
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

# META: verification of `concepts/dofset.md` — the `DofSet[N]` record-definition home

## Critique

### Checks run

**citation-validity (LOAD-BEARING) — pass.** Ran `citecheck.py --scan` over CYCLE.md: 14/14 citations OK, no `[DRIFT]`, no path-hygiene issues. Re-read the four load-bearing L0 backing ranges via codemap `read_range`:
- `rap.hpp:35-36` — `mfem::Array<int> dbc_tdof_list;` sits at line 36 with the comment "Lists of constrained essential boundary true dofs for elimination" at line 35; the `35-36` range correctly encloses comment+member. The backing-member claim is carried.
- `rap.hpp:87-91` — `GetEssentialTrueDofs()` returning `dbc_tdof_list.Size() ? &dbc_tdof_list : nullptr` lands exactly; the empty-set/`nullptr` claim is backed.
- `rap.cpp:36-47` — `SetEssentialTrueDofs`: the policy guard (`DIAG_ONE | DIAG_ZERO`) is at :39-41, the square-operator guard (`height == width`) at :42-43, and `dbc_tdof_list.MakeRef(tdof_list)` (the record-by-reference claim, also cited as `:45`) at :45. All three sub-pinpoints anchor.
- `multigrid.hpp:99-100` (prose pinpoint) / `92-101` (frontmatter range) — `fespaces.GetFinestFESpace().Get().GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())` spans :99-100; the wider `92-101` frontmatter range is the enclosing `if (dbc_attr && dbc_tdof_lists)` block. Both land on real source; the materialization claim is backed. This is **consistent with the c101 audit's `multigrid.hpp:99-100` cite** — same site, same lines.
The frontmatter `edges:` YAML block round-trips under `yaml.safe_load` (no quoted-scalar-at-start defect). All consumer-signature back-references confirmed on disk (`eliminate_bc.md:76-77,100-102`, `essential_dofs.md:19,62`).

**surface-or-evidence / record-definition obligation — pass.** This is a record-definition concept page; the adapted obligation is that it defines the DATA SHAPE (fields/types/stratum/L0 home) and does NOT restate operator algebra. Confirmed: the page gives the single-field TS-brace schema (`indices : Set<TrueDofIndex>`), a field table with type/meaning/stratum/L0-source columns, the construction-time-readonly stratum, the empty-set representation, and the `dbc_tdof_list` L0 home — and it explicitly defers behaviour ("this page does not restate that algebra") to the producer/consumer chapters. The ≥2-consumer bar is genuinely met: three distinct signature consumers verified on disk — `essential_dofs` (producer, `-> DofSet[N]`), `eliminate_essential_bc` (`dofs: DofSet[N]`), `eliminate_rhs`. Correctly above the bar ⇒ standalone `concepts/<record>.md` page rather than an in-chapter section. The record being defined HAS its definition home (this page), so no record-definition gap.

**rotation-quality — pass (not applicable).** A record-definition concept page asserts no algebraic/structural rotation; it defines a data shape. No rotation claim to grade.

**variant-axis-coverage — pass (not applicable).** A data-shape record page has no orthogonal variant axes of its own. The page correctly scopes out the one adjacent variant question (`DiagPolicy` co-homing) in Open questions, ruling it a distinct single-consumer enum below the ≥2-consumer bar.

**cross-reference-integrity (LOAD-BEARING) — pass.** All eight `edges:` targets resolve on disk: the five `.md` constituents (`L1/essential_dofs`, `L1/eliminate_essential_bc`, `L1/eliminate_rhs`, `L4/eliminate_bc`, `L1/fe_space`) and the three concept pages (`set_subvector_zero`, `state-stratification`, `build-time-vs-run-time-stratification`) all exist; the L0 `depends-on` ranges all read on disk. The new page is wired into `SUMMARY.md` so the live link resolves — `dofset.md` is the only "MISSING" path, correct since it is the file being created. SUMMARY alpha-placement verified: current lines 308 (`derived-view-hoisting`) / 309 (`dot`); insert between them; `der` < `dof` < `dot` holds. **Rank invariant holds**: all blocking (`depends-on`) edges go only to L0 ground-truth ranges (rank-terminal), so a `firm` record resting on them satisfies `rank(u) ≤ rank(v)` vacuously; the producer/consumer/L4 edges are `reference` (navigational), so the record does not block on its consumers — correct (a named-by-use record must not depend-on its consumers).

**edge-label-fidelity — pass.** The `depends-on … kind: cites-evidence` vs `reference` split is correct: blocking evidence edges point at L0 source (the data shape's actual backing), navigational edges point at the producer/consumers/L4 surface/sibling concepts. HARD-gate-new is honored — the new node is fully typed from the start (rank + kind + typed edges), not introduced untyped.

**plan-kind-consistency — pass.** Declared `kind: record`, `rank: firm`. Content shape matches: a record-definition page (Kind banner + Record-definition schema + stratum + L0 home + signatures + See-also + Status), mirroring the `op-params.md` / `config-record.md` convention. The `firm` rank is justified — a single readonly index-set field with a fully-specified positive L0 backing and a construction-vs-run-time stratum read directly from the `SetEssentialTrueDofs`/`EliminateBC` lifecycle (the firm-on-positive-structure situation). No rough-in placeholders.

**skill-uptake-survey — pass.** The report references its codemap `read_range` self-verification of the L0 ranges and follows the established record-page convention exemplars. No unreferenced relevant skill apparent for the record-definition-home shape; telemetry only, non-blocking.

### Issues found

None blocking. Observations (all already self-flagged in the report's Open questions, recorded here for the integrator, not as defects):

1. **Stale prose at `L4/eliminate_bc.md:119-134` (not build-breaking).** Confirmed on disk: line 126 reads "the concept page `book/src/concepts/DofSet.md` does **not yet exist**" (capitalized `DofSet.md`). Once this page lands the prose is factually stale. Verified this is **plain prose, not a markdown link** (`[...](...)`), so `linkcheck2` is unaffected — no build risk. The lowercase `dofset.md` filename is correct per the all-lowercase concepts-directory + mdBook-slug convention. Correctly routed as OQ `eliminate-bc-record-definition-prose-now-stale` (consumer-chapter edit, outside this single-page dispatch). No live markdown link points at the wrong case.

2. **One-way `reference` link to `set_subvector_zero` (pending reciprocal).** `dofset.md` references `set_subvector_zero`; the reciprocal `set_subvector_zero → dofset` link is correctly routed (not applied) as OQ `set-subvector-zero-references-dofset`, respecting the one-concept-page-per-invocation read-only-toward-other-pages bound. Not a cross-reference-integrity failure — both endpoints exist; only the reciprocal back-link is deferred.

All 8 checks pass; the report is clean. `overall_status: ready` set by the critic (no repairer will run).
