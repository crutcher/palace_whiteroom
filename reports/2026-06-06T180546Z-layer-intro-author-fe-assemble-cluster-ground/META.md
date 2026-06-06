---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T18:18:26Z
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

# META: verification of FE-assemble cluster GROUND (L1/fe_assemble + L1/fe_space)

## Critique

### Checks run

**citation-validity** — pass. This is a frontmatter-only grounding migration; the load-bearing
citation is the lone L0 `cites-evidence` edge `palace/fem/fespace.hpp:67-75` on `fe_space`. Verified
mechanically: `citecheck --anchor 'FiniteElementSpace'` returns `1 ok, 0 failing`, anchor at line 68
within range 67-75, resolving to `reference/palace/palace/fem/fespace.hpp`. The slug-citations in the
producer's faithful-edge derivation (`fe_assemble.md:60/68-72/163`, `fe_space.md:9/43/50-52/89`) were
cross-read against the actual chapters and match (signature line :60, term-list element-type prose
:71-72, §Dependencies :163, etc.). No `verified_against:` YAML block in this report, so that sub-check
no-ops.

**surface-or-evidence** — pass. This is not a refinement-of-existing-surface proposal nor a
record-definition gap: it is a pure frontmatter edge-grounding migration that touches no prose body,
signature, or `## Status` line (verified: both `[old]`/`[new]` blocks are frontmatter-only). Both
chapters already define their records/types in-chapter (`FiniteElementSpace[N]`, `WeakFormTerm`,
`FECollection`) with the firm operators carrying full Signature + Algebraic-laws + Evidence. No new
claim is introduced. The migration only re-expresses pre-existing firmness as `rank: firm` and types
the edges that were already named in prose.

**rotation-quality** — pass (not applicable). No algebraic/structural/reduction rotation is asserted;
this is a graded-stack edge-typing migration, not a layer rotation. The chapters' own rotations
(fe_assemble's fold, fe_space's construction) are untouched.

**variant-axis-coverage** — pass. No variant axes are added or removed by the migration. The producer
correctly notes the `variant_axes:` frontmatter list is dropped per the canonical scheme
(set_subvector_zero / krylov-step template carry no such field) and the three axes
(assembly-representation / term-position / trial-test-coincidence) remain authoritatively documented in
`fe_assemble.md` body §Variant axes (:180-198, on-disk confirmed). This is a deliberate field-location
move, not data loss.

**cross-reference-integrity** — pass. All `depends-on` and `reference` edge targets resolve to on-disk
slugs: `L1/weak_form_term.md` (firmness: firm), `L1/fe_space.md` (status: firm), `L1/fe_collection.md`
(status: firm, cycle-065), `L1-L0/fe-operator-assemble-mutation-rotation.md` (status: firm),
`L1-L0/fe-space-construction-rotation.md` (`## Status: firm` in body), `L1/bilinear-form.md` (the
slug-collision reference), plus the `fe_space` reference siblings (`fe_assemble`,
`eliminate_essential_bc`, `eliminate_rhs`). Applied the edits and ran the lint: `unresolved: 0` held.

**edge-label-fidelity** — pass (load-bearing for this dispatch). Each `composes` edge was verified
against the actual chapter signature + prose, not just the producer's narration:
- `L1/fe_assemble →composes→ L1/weak_form_term`: faithful. `fe_assemble.md:60` signature carries
  `terms: [WeakFormTerm]`; :71-72 names the element as a firm `weak_form_term`; :163 §Dependencies
  confirms it is the term-list element type. The fold composes over the list (folds opaquely but DOES
  compose over it) — `composes`, not `reference`, is correct.
- `L1/fe_assemble →composes→ L1/fe_space`: faithful. `fe_assemble.md:60` names `space:
  FiniteElementSpace[N]`; :68-70 states it is "constructed by `fe_space`" and the directly-consumed
  input. Constituent-input composition — `composes` correct.
- `L1/fe_space →composes→ L1/fe_collection`: faithful. `fe_space.md:9/43` signature `collection:
  FECollection`; :50-52 the directly-consumed second ctor arg; :89 names `fe_collection` as the
  upstream producer. A genuine constituent-use (peer L1 op producing a consumed value), NOT a
  lowering — `composes` correct.
- `lowers-to` edges preserved faithfully: `fe_assemble →lowers-to→
  L1-L0/fe-operator-assemble-mutation-rotation` is the exact pre-scheme `lowers_to:` value (old
  frontmatter :5-6), prose-named at :45/:278-285; `fe_space →lowers-to→
  L1-L0/fe-space-construction-rotation` is prose-named at :38-39/:145-150. Both targets on-disk firm.
- The DECLINED edges (faithful-edge-or-finding) are correct: `fe_space.md` §Status :181-187 names
  `essential_dofs`, `fe_space_hierarchy`, and the de-Rham interpolator machinery as deferred,
  unauthored siblings — they are sibling-pull-gated future vocabulary, not current deps, so declining
  the would-be over-edges (filed as OQ `fe_space-deferred-siblings-still-ungrounded`) is the faithful
  call. No edge-label asserts a direction the prose contradicts.

**plan-kind-consistency** — pass. Genuine grounding hygiene, not disguised authoring. Both `[old]` →
`[new]` blocks are frontmatter-only; the firm maturity pre-existed (`firmness: firm` / `status: firm`
on disk) and merely migrates to `rank: firm`. No prose body, signature, or law is added or altered.
The kind (layer-intro-author graded-stack edge-grounding) matches the content shape exactly.

**skill-uptake-survey** — pass. The dispatch shape (graded-stack reachability grounding) implies the
`graded_stack_lint.py` tool, and the report references its invocation (the standalone-delta table +
`--show-inbound`) and the git-stash isolation procedure for
`parallel-dispatch-reachability-measurement-contamination`. Telemetry surfaced; no gap.

### Independent verification performed

I applied both proposed `[new]` frontmatter blocks to a clean tree (baseline lint confirmed matching
the dispatch-given baseline: reachable=124, detritus=135, STRONGER GARBAGE SIGNAL=24, rank
violations=none), re-ran `graded_stack_lint.py` + `--show-inbound`, then reverted both files to
pristine git state (tree clean):

| metric | clean baseline | + 2 files | Δ | report claim |
|---|---|---|---|---|
| reachable from roots | 124 | 129 | +5 | +5 ✓ |
| detritus | 135 | 130 | −5 | −5 ✓ |
| STRONGER GARBAGE SIGNAL | 24 | 23 | −1 (weak_form_term) | −1 ✓ |
| rank violations | none | none | held 0 | held 0 ✓ |
| unresolved | 0 | 0 | held | held ✓ |

The +5 reproduces exactly, and `--show-inbound` confirms the rescue is measurable and non-contaminated:
`L1/weak_form_term <- L1/fe_assemble`, `L1/fe_space <- L1/fe_assemble`, `L1/fe_collection <-
L1/fe_space`, plus the two transitive L1>L0 themes (`fe-assemble-libceed-boundary-obstruction <-
weak_form_term`, `fe-space-construction-rotation <- fe_space`) accounting for +5 vs. the +3 direct-node
estimate. `RANK VIOLATIONS: none` confirms rank(u) ≤ rank(deps): both source nodes are firm (rank 3)
and every `composes` target is on-disk firm (rank 3). The contamination concern is unfounded — the
clean baseline matched and the deltas are entirely attributable to the two D1 files.

### Issues found

None. All 8 checks pass; rank well-foundedness and the +5 reachability claim independently reproduced;
all edge targets resolve and are firm-or-above; every `composes` edge is faithful to the chapter
signature + prose; the two declined over-edges are correctly filed as findings. The report is clean.
