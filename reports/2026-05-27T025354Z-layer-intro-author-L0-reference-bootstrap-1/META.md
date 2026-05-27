---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T030500Z
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
skill_uptake:
  classify-variant-axis: not-invoked
  verify-citation-range: not-invoked
  verify-refinement-surface: not-invoked
  skill-selection: not-invoked
  plan-sideways-concept-emission: not-invoked
  embed-and-persist-subagent-dispatch: not-invoked
repaired_at: 2026-05-27T031500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of "L0 reference-notes bootstrap — bundle 1"

## Critique

### Checks run

- **citation-validity**: spot-checked ~15 source citations against `reference/palace/` clones (`vector.hpp:20`, `:23-147`, `:25-26`, `:99`, `:115-128`, `:131`, `:134-136`, `:177-194`, `:242-260`, `:262-270`, `:305-316`; `vector.cpp:203-227`, `:263-274`, `:701-712`, `:714-718`, `:720-724`, `:726-743`, `:745-758`, `:751`, `:729`; `operator.hpp:54`; `operator.cpp:428-441`, `:458-466`; `rap.cpp:195-234`; `ksp.cpp:26-101`, `:34-58`, `:53-57`, `:59-62`, `:64-95`; `iterative.cpp:379, 443`). All match the source content claimed. Wc-verified ranges in-bounds. The `ComplexVector::Dot` claim "four real `LocalDot` calls" (text on line 167) is mildly imprecise — the code at `vector.cpp:265-266` uses `Vector::operator*` (real-Dot) four times, not literal `LocalDot` symbols — but functionally accurate at the algebra level. Pass.
- **surface-or-evidence**: this is a layer-bootstrap (new-chapter) dispatch, not a refinement of existing surface. The 6 new chapters are evidence overlay; the L0/index.md edit is a re-framing of an existing 30-line stub but is additive (new "Reference-note cohort" + "Working Notes" entries) with no contradictory edits to retained content. Pass.
- **rotation-quality**: not applicable to L0 reference notes (no L_{n+1}→L_n rotation claim). The chapters describe L0 conventions and L1 lifting at a meta level without proposing new rotations. Marked pass / not applicable.
- **variant-axis-coverage**: `mfem-vector-types` explicitly enumerates the element-type axis (real/complex) and the `Par*` axis, calls them orthogonal, and scopes out MPI per CLAUDE.md. `output-arg-vs-receiver` enumerates both idioms with examples. `linalg-free-functions` enumerates wrapper / composed-scaffold / one-line shapes and explicitly notes the absence of `linalg::Scal`. Open question `scalar-promotion-typing-rule` is correctly referenced for the scalar sub-axis. Pass.
- **cross-reference-integrity**: all `[L1/*](../L1/*.md)` targets verified present (axpy, axpby, axpbypcz, scal, dot, nrm2, apply_linop). `[L1-L0/minres-iteration]` and `[L1-L0/bicgstab-iteration]` exist. `[spec/slices/cg]` and `[spec/slices/gmres]` exist. The `ksp-factory-file` cites `palace/linalg/ksp.cpp:53-57` while the existing `bicgstab-iteration.md` cites `:53-56` — minor range mismatch (off-by-one inclusion of trailing `break;`), not a broken link. Pass.
- **edge-label-fidelity**: no L_{n+1}→L_n edge-labeled proposals carried; chapters are L0-only with backward-pointing "Referenced from" annotations. Pass.
- **plan-kind-consistency**: declared kind is a layer-bootstrap (6 new chapters + index refresh + SUMMARY.md registration). Content shape matches: each chapter is 2–4 paragraphs + 3–6 representative citations + `Referenced from:` backlinks, per the stated discipline. The no-line-by-line-duplication rule (priority #10) is observed — chapters describe what's in source rather than transcribing it. One small concern: `linalg-vector-file.md` "At a glance" section enumerates many declarations with line numbers (e.g., "`operator*=` (line 99), `Conj` / `Abs` / `Reciprocal` (lines 102–108), `Dot` / `TransposeDot` / `operator*` (lines 110–113), `AXPY` / `Add` / `Subtract` / `operator+=` / `operator-=` (lines 115–128)…"). This is a navigation index, not function-declaration duplication — the signatures are not transcribed, only named — so it stays inside the discipline. Pass.
- **skill-uptake-survey**: report does not reference invocation of `verify-citation-range`, `classify-variant-axis`, or `verify-refinement-surface`, despite the chapter touching variant axes (element-type / Par axis) and load-bearing-vs-transparent classification (which `classify-variant-axis` and the trick-classification heuristic in `transparent-vs-load-bearing-tricks.md` could surface telemetrically). Pure telemetry — non-blocking. Warning.

### Issues found

1. **`ksp-factory-file` cites `ksp.cpp:53-57` but the existing `bicgstab-iteration.md` uses `:53-56`** (CYCLE.md line 418, vs. `book/src/L1-L0/bicgstab-iteration.md:39`). Both ranges cover the same switch-arm fall-through (lines 53-57 in source: three case labels + abort + break). The minor inconsistency between sibling pages doesn't break the citation but invites a normalization sweep. Severity: low.

2. **`ComplexVector::Dot` four-real-`LocalDot` phrasing in `mfem-vector-types.md`** (CYCLE.md line 167). The source uses `Vector::operator*` (method-form real Dot) four times; the symbol `LocalDot` is not invoked at `vector.cpp:263-267`. The chapter's claim is algebraically correct but the symbol attribution is loose. Severity: low.

3. **`linalg-vector-file.md` "Source" section line ranges for `linalg::AXPBYPCZ` family — claims `lines 745-772`** (CYCLE.md line 318, 346). The source `AXPBYPCZ` real-real specialisation ends at line 758, then complex specialisations run 760-772 (also `AXPBYPCZ`). The reported range 745-772 covers all three correctly — but the same chapter also says "`vector.cpp:745-758` … `gamma == 0` control-flow branch" (line 263 of CYCLE.md) which is just the real-real specialisation. Both ranges are individually correct but adjacent in the chapter; a reader could conflate them. Severity: very low (presentational).

4. **`StaticVector<N>` claim "stack-allocated subclass of `Vector` with compile-time fixed size"** (CYCLE.md line 169). Source `vector.hpp:181` shows `double buff[N];` as a member array — accurate. But `vector.hpp:177` says `template <int N> class StaticVector : public Vector` which inherits, not subclasses MFEM's `Vector` directly — `Vector` here is `using Vector = mfem::Vector;`. So it is "an `mfem::Vector` subclass with a stack-backed buffer." The chapter's claim is correct; flagged only because the wording could be sharpened. Severity: very low.

5. **No backlinks from `ksp-factory-file` to any L0 sibling page** beyond `mfem-vector-types`; for symmetry with `linalg-vector-file` (which cross-links to `transparent-vs-load-bearing-tricks`), the obstruction-theme anchor could also cross-link to `transparent-vs-load-bearing-tricks` (the abort pattern is arguably a load-bearing-vs-not classification edge case). Not a fault — observation. Severity: very low.

6. **`Referenced from:` backlinks are forward-declared** — they name L1 pages that *should* reference these conventions after the cycle-005 retroactive-thinning sweep, not pages that currently do. The CYCLE.md "Open questions / caveats" is explicit about this ("authors the L0 chapters and lays down the `Referenced from:` backlinks, but does **not** edit L1 entries"). The backlink semantics are aspirational, which is honest but potentially confusing to a reader who follows a backlink expecting to find the L1 page mentioning the convention by name today. A one-line disclaimer at the top of each `Referenced from` section ("Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-005 retroactive sweep — priority #11") would close the loop. Severity: medium (UX/honesty, not correctness).

7. **`skill-uptake-survey` warning** — see check above. The trick-classification chapter could benefit from a one-line note that `classify-variant-axis` skill is the canonical procedure for the load-bearing/transparent decision when an agent encounters a new case. Severity: low.

8. **Filename is `CYCLE.md`, not `REPORT.md`** as named by the agent-write-authority convention in CLAUDE.md (`reports/<id>/REPORT.md`). The front-matter and content are otherwise well-formed. The `verifies:` field in this META points at `../CYCLE.md` to match. Severity: low (convention drift, not blocking).

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey warning — missing `skill_uptake:` telemetry block.
  - **Decision**: repaired
  - **Action**: added `skill_uptake:` frontmatter block enumerating the 6 current skills, all marked `not-invoked` (matches critic finding that none were referenced by the producer).

- **Finding**: `ksp.cpp:53-57` vs `:53-56` across sibling pages.
  - **Decision**: repaired (verified correct range)
  - **Action**: read `reference/palace/palace/linalg/ksp.cpp:53-57` directly; the full case-fallthrough block is lines 53–57 (three case labels at 53–55, `MFEM_ABORT` at 56, `break;` at 57). CYCLE.md already cites `:53-57` consistently at lines 410 and 418 of CYCLE.md — no edit needed inside the report. The sibling book page `book/src/L1-L0/bicgstab-iteration.md:39,68` uses `:53-56` and needs reconciliation by the integrator (book-owned; outside repairer authority). Routed to integrator follow-up.

- **Finding**: `four real LocalDot calls` phrasing loose (CYCLE.md `mfem-vector-types.md` chapter, line 167).
  - **Decision**: repaired
  - **Action**: replaced "four real `LocalDot` calls combined" with explicit naming of the actual symbol invoked — `mfem::Vector::operator*` (real-Dot) — and enumerated the four invocations: `Real() * y.Real()`, `Imag() * y.Imag()`, `Imag() * y.Real()`, `Real() * y.Imag()`. Verified against `reference/palace/palace/linalg/vector.cpp:263-267`.

- **Finding**: backlinks marked aspirational without disclaimer.
  - **Decision**: repaired
  - **Action**: prepended a one-line italic disclaimer to each of the four conventions chapters' `## Referenced from` sections in CYCLE.md (`output-arg-vs-receiver.md`, `mfem-vector-types.md`, `linalg-free-functions.md`, `transparent-vs-load-bearing-tricks.md`): *"Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11)."* The `ksp-factory-file.md` `Referenced from` section is left alone — those backlinks (`L1-L0/minres-iteration`, `L1-L0/bicgstab-iteration`, `L1/index`) are not forward-declared; the cited L1-L0 pages already reference `ksp.cpp` today.

- **Finding (IGNORED)**: filename is `CYCLE.md`, not `REPORT.md`.
  - **Decision**: not-needed (critic working from stale info)
  - **Rationale**: the cycle-004 rename (commit `8ac1f37`) made `CYCLE.md` the convention. CLAUDE.md write-authority and Cycle structure both reflect `CYCLE.md`. The current filename is correct; the critic's reference to `REPORT.md` is residual from the pre-rename convention. No edit applied.

### Unrepairable findings

None requiring a follow-up dispatch. Two notes for the integrator:

1. `book/src/L1-L0/bicgstab-iteration.md` cites `ksp.cpp:53-56`; sibling `minres-iteration.md` cites `:53-57`. CYCLE.md (this report) uses the correct `:53-57`. Integrator should normalise the bicgstab-iteration page to `:53-57` (book-write authority) as part of routine link-check sweep on this cycle's apply.

2. Critic-flagged issues 3, 4, 5 are very-low severity presentational / no-fault observations the critic already classified as non-blocking; no repair attempted. Listed here only so they aren't dropped silently.

## Suggested resolution

`ready`. Integrator may apply as-is. One housekeeping fix for the integrator: reconcile `book/src/L1-L0/bicgstab-iteration.md:39,68` from `:53-56` to `:53-57` to match the new `ksp-factory-file.md` chapter and the existing `minres-iteration.md` citation.
