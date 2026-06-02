---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T00:36:10Z
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
repaired_at: 2026-06-02T00:46:00Z
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

# META: verification of cycle-054 D2 — fe_assemble FIRM L1 promotion

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` reports 40 ok / 0 failing (all bounds + path-hygiene clean). I independently verified the load-bearing pinpoints via codemap `read_range`. The drift-correction crux holds: `palace/fem/bilinearform.cpp` line 77 IS the domain `op->AddSubOperator(sub_op)` and line 97 IS the boundary one — D2's corrected `:71-77` / `:91-97` ranges enclose them, and the rough-in theme's `:73-75` / `:93-95` is indeed a +2 drift (the off-by-two is real and corrected in-hand). `GetStiffnessMatrix` is at `laplaceoperator.cpp:184`; the witness body confirms `BilinearForm k(GetH1Space())` (191), `AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` (192), `Assemble` (194), `SetEssentialTrueDofs` (216) — all within the cited `:184-223`. The `BilinearForm` class members (`domain_integs, boundary_integs` :32), templated append (:53-63), single-space ctor delegating trial=test (:48) all confirmed in `bilinearform.hpp:25-91`. The slug-collision source citation `linalg::Dot(comm, x, A, y)` at `operator.cpp:621-639` is corroborated by the existing `bilinear-form.md` (lines 29, 157). No `verified_against:` YAML block in this report (harvester, not lowering-verifier) — round-trip sub-check N/A. The dep-map row carries the drift note honestly (`:77`/`:97` corrected; theme body `:73-75`/`:93-95` flagged for lifter re-anchor, not edited in place — respecting the dispatch-phase write partition).

**surface-or-evidence — pass.** This is a new firm operator entry (not a refinement of existing operator/theme text), so the surface-or-evidence gate applies in its constructive form: the entry modifies surface (a full new `book/src/L1/fe_assemble.md` body + index/SUMMARY/dep-map registrations) AND carries positive L0 evidence (the `PartialAssemble` fold core, the `GetStiffnessMatrix` witness, the class-shape anchors). Not a bare rotation-claim; the entry is surface + evidence throughout.

**rotation-quality — pass.** The L1>L0 rotation (mutation rotation) is genuinely state-hiding/compressive, not a rename. The L0 form is an imperative build-up-then-assemble object protocol (construct mutable `BilinearForm`, `push_back` integrators onto two owned lists, mutate a composite `ceed::Operator` via `AddSubOperator`, `Finalize`); the L1 form collapses all three mutations into a pure fold `K = Σ_i A(space, t_i)` over an immutable term list. That is a real impedance rotation (mutable container + accumulator + finalize → algebraic sum), strictly more compact and equational than the L0 protocol. The PA/FA dual collapsing to one representation-agnostic action is additional genuine compression.

**variant-axis-coverage — pass.** Three orthogonal axes are declared and each is addressed, not hidden: `assembly-representation` (partial `ceed::Operator` vs full `HypreCSRMatrix` — collapsed at L1 as same-action, with the `UseFullAssembly` performance-selector cited); `term-position` (domain vs boundary — unified into one concatenated term list per law 2, with the dimension−1 geometry branch cited); `trial-test-coincidence` (square vs rectangular — the witnessed square case is what the signature is written for, and the rectangular generalization is explicitly scoped out as a noted-but-not-exercised sub-axis with the `bilinearform.cpp:42-46` general-construction anchor). No hidden branch: the multigrid-hierarchy `Assemble(hierarchy)` overload and the per-level `ParOperator`/`MultigridOperator` wrap are explicitly carved out to OQ-6 as a sibling concern, not silently folded in.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `bilinear-form.md`, `apply_linop.md`, `axpy.md`, `fem-bilinearform-file.md`, `fe-operator-assemble-mutation-rotation.md` all exist. The `new:` block for the firm-claimed body ENCLOSES the full firm apparatus inside the fence: `# fe_assemble` (block-line 16), `## Signature` (58), `## Algebraic laws` (108), `## Status` (196, the clean-gate record), `## Evidence` (237) all sit between the `new:` open (CYCLE line 53) and its close (line 334) — no firm-body-outside-fence defect. The deferred operators (`weak_form_term`, `eliminate_essential_bc`, `eliminate_rhs`) are correctly plain-text forward-refs (no live links to missing files), per the `rough-in-forward-reference-must-be-plain-text` convention. The `bilinear-form` slug exists and the entry's distinction from it is correct (verified below). The SUMMARY insert places `fe_assemble` immediately after the existing `bilinear-form` line — correct context. The L1-L0 dep-map `edit:` old-form exactly matches the on-disk row (`L1/fe_assemble (speculative rough-in; no anchor yet)`).

**edge-label-fidelity — pass.** The single edge label is L1>L0 (`lowers_to: L1-L0/fe-operator-assemble-mutation-rotation`), and the prose throughout (§Context, §Downward to L0, §L1 vs L0) discusses exactly that edge — how the L1 fold lowers into Palace's L0 build-up-then-assemble protocol. No mislabeled edge.

**plan-kind-consistency — pass.** Declared kind is `firm` L1 operator; the content shape matches — a complete signature, semantics, four stated-and-defended laws, dependencies, variant axes, evidence, and a clean-gate `## Status` record. No rough-in placeholders inside the firm body. The two opaque inputs (`WeakFormTerm`, `A`) are correctly classified as deferred rough-in INPUTS the firm fold quantifies over (not firm-body holes) — this is the `firm-on-positive-structure` situation (apply_linop / BLAS-1-leaf precedent), correctly invoked: the laws are syntactic identities on a fully-specified positive fold, so the missing dedicated `fe_assemble` unit test does not gate firmness.

**skill-uptake-survey — warning (non-blocking).** The report's shape implies two relevant skills whose invocation is only partially surfaced. (a) `verify-citation-range` / the `tools/citecheck` `--anchor`/`--scan` realization: explicitly invoked and logged (the §Supporting-evidence anchor table + the `--scan` 40-ok line) — good uptake. (b) `proposed-changes-fence-encloses-full-body-guard`: this is a firm-body-inside-`new:`-fence report (exactly the guard's trigger shape), but the report does not reference a self-check against it; the fence parity is in fact clean (I verified), so this is telemetry, not a defect. (c) `classify-variant-axis`: the entry does substantial variant-axis work (3 axes) without referencing the skill. Pure presence-survey; surfaced, not blocking.

### Issues found

No blocking issues. The four crux questions from the dispatch scope all resolve in the report's favor:

1. **Clean-gate call — SOUND (load-bearing, confirmed).** I read `integrator.hpp:39-70`: the `BilinearFormIntegrator` exposes a virtual `Assemble(...)` and the `PartialAssemble` fold (`bilinearform.cpp:71-103`) touches each term ONLY through `integ->Assemble(...)` + `op->AddSubOperator(sub_op)`. The term's `(coefficient Q, differential-operator)` internals live entirely behind the virtual interface; the fold never inspects them. So `fe_assemble` genuinely IS definable with `weak_form_term` opaque — the clean-gate PROMOTE is correct, not a forced/incomplete landing.

2. **The four laws over opaque `A` — all real (confirmed).** (1) Empty-term identity: the guarded `!domain_integs.empty()` / `!boundary_integs.empty()` branches (`:61`/`:84-85`) mean an all-empty list adds no sub-operators → zero-action operator after `Finalize` (`:104`); the OMP comment at `:50-52` independently corroborates the empty-operator case. Real fold-identity law, holds over opaque `A`. (2) Concatenation-homomorphism: distributes `Σ` over `++`; pure fold law, no term-internal dependence. (3) Single-term reduction: `Σ` over `[t]` = `A(t)`; fold law. (4) Term-position commutativity: rests on operator-`+` commutativity/associativity, and the L0 loop does iterate in arbitrary `push_back` order then domain-then-boundary — the algebraic-immateriality claim is correct, with the FP-non-associativity caveat properly scoped to L0 representation. The non-laws are sound: `DiffusionIntegrator` is singular before BC (constant null-space), so no single-term SPD/invertibility; BC-elimination via `SetEssentialTrueDofs` is witnessed POST the `ParOperator` wrap (`:216`), genuinely a separable post-composition, not part of the fold.

3. **Slug-collision — held distinct, distinction correct (load-bearing, confirmed).** `bilinear-form.md` is the BLAS-2 reduction `α = xᴴ M y` consuming an assembled operator (lines 19, 27, 63, 98; L0 `linalg::Dot(comm,x,A,y)` at `operator.cpp:621-639`). `fe_assemble` is the assembly constructor producing `K` (the `BilinearForm` class). They share only the phrase "bilinear form." The entry's §Slug-collision states this explicitly and routes downstream FE-assembly work to `fe_assemble` — no mis-conflation of the spine.

4. **Citation-drift — corrected correctly (confirmed).** Domain `AddSubOperator` at line 77, boundary at 97 (verified by codemap); D2's `:71-77`/`:91-97` enclose them; the theme's `:73-75`/`:93-95` +2 drift is real and is flagged-for-lifter (not edited in place) — correct dispatch-phase discipline.

Two minor, non-blocking observations (telemetry for repairer/integrator, not defects):

- **(minor / integration-shape note)** The `edit:book/src/L1/index.md` block re-states the cohort subsection header (matching on-disk line 70) and the two `eliminate_*` bullets (matching lines 73-74) verbatim while replacing the line-72 rough-in `fe_assemble` bullet with the firm bullet. This parses cleanly as a contiguous lines-70-74 replacement (header + firm-bullet + two eliminate-bullets), and the on-disk context matches exactly — flagging only so the integrator confirms it treats the block as the full contiguous replacement rather than an append. The subsection HEADER still reads "Rough-in (FE-assembly sub-spine ...)" after this edit (now 1 firm + 2 rough-in); D2 correctly defers the header reword to layer-intro-author (OQ-7) per the index-registration partition — acceptable, the header staleness is owned and routed.

- **(minor / skill-uptake)** No reference to a `proposed-changes-fence-encloses-full-body-guard` or `classify-variant-axis` self-check despite the report's shape inviting both. The underlying work is correct (fence parity clean, variant axes well-covered); this is the skill-uptake-survey warning above, surfaced as telemetry only.

## Repair

### Fixes attempted

The critic returned 7 `pass` and 1 `warning` (skill-uptake-survey), with **no blocking issues**. All four load-bearing crux questions resolved in the report's favor (clean-gate PROMOTE sound; 4 laws + non-laws real over opaque `A`; slug-collision held distinct correctly; citation-drift corrected correctly with the theme-body drift flagged-for-lifter, not edited in place). Fence parity is clean (firm body fully inside the `new:` fence). Nothing in the critique requires a mechanical edit.

- **Finding**: skill-uptake-survey — warning. No referenced self-check against `proposed-changes-fence-encloses-full-body-guard` or `classify-variant-axis` despite the report's shape inviting both.
  - **Decision**: not-needed
  - **Rationale**: Pure presence-survey telemetry, explicitly non-blocking. The critic independently verified the underlying work is correct — fence parity is clean (firm body fully enclosed by the `new:` fence) and the three variant axes are well-covered and each addressed, not hidden. A skill-invocation *reference* is a process-telemetry signal, not an artifact defect; adding one would author into the report's chain-of-thought, which is out of repair scope (and pointless when the checks the skills exist to enforce already pass). No edit. Note carried for the integrator below.

- **Finding** (minor / integration-shape, non-blocking telemetry): the `edit:book/src/L1/index.md` block parses as a contiguous lines-70-74 replacement (cohort header + firm `fe_assemble` bullet + two `eliminate_*` rough-in bullets), with the on-disk context matching exactly; the subsection header still reads "Rough-in (...)" after the edit (now 1 firm + 2 rough-in), deferred to layer-intro-author (OQ-7).
  - **Decision**: not-needed
  - **Rationale**: Not a defect — the critic confirmed the `edit:` block's old-form matches on-disk exactly and parses as a clean contiguous replacement; the header-reword deferral is correctly owned and routed to OQ-7 per the index-registration partition. Surfaced for the integrator only (so it treats the block as a full contiguous replacement, not an append). No edit.

- **Finding** (minor / citation, non-blocking): the L1>L0 theme body's `bilinearform.cpp:73-75` / `:93-95` ranges are a +2 drift off the true `AddSubOperator` sites (`:77` / `:97`).
  - **Decision**: not-needed (correctly deferred by the producer)
  - **Rationale**: The drift is real but lives in a *different artifact* (`book/src/L1-L0/fe-operator-assemble-mutation-rotation.md`, the rough-in theme), not in D2's proposed-changes. D2 corrected its own ranges to the enclosing `:71-77` / `:91-97` and **flagged** the theme-body drift for lifter re-anchor without editing it in place — correct dispatch-phase write-partition discipline. Editing the theme here would exceed both the report's write-scope and the repairer's (it is an artifact file, off-limits; CLAUDE.md "do not modify artifact"). Routed via D2's OQ to the lifter follow-up.

### Unrepairable findings

None. No finding requires substantive authoring or contradicts artifact content; the single warning is non-blocking telemetry and the two minor notes are correctly-routed deferrals.

## Suggested resolution

`overall_status: ready` — this is a clean firm L1 promotion with no blocking issues and no repairs required.

Notes for the integrator:

- **D2 proposed-changes**: `new:book/src/L1/fe_assemble.md` (full firm body) + L1 index FE-cohort bullet → firm + `SUMMARY.md` entry (immediately after the existing `bilinear-form` line) + L1-L0 dep-map row (LHS firm, `L1/fe_assemble` no longer "speculative rough-in; no anchor yet").
- The `edit:book/src/L1/index.md` block is a **full contiguous lines-70-74 replacement** (cohort header + firm `fe_assemble` bullet + two `eliminate_*` rough-in bullets), not an append — apply it as such.
- The deferred operators (`weak_form_term`, `eliminate_essential_bc`, `eliminate_rhs`) stay **plain-text rough-in forward-refs** (no live links to missing files), per the `rough-in-forward-reference-must-be-plain-text` convention.
- **Promote D2's 7 OQs**, in particular: (a) theme re-anchor to the now-firm `fe_assemble` LHS [**lifter** follow-up]; (b) the `bilinearform.cpp:73-75` / `:93-95` theme-body citation +2 drift [**lifter**]; (c) the libCEED-boundary classification [**batch-16 meta-phase**]; (d) the `weak_form_term` cohort; plus the index-header reword (OQ-7, **layer-intro-author**) and the multigrid-hierarchy `Assemble(hierarchy)` / per-level wrap carve-out (OQ-6).
