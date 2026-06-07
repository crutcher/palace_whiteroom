---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T231500Z
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

# META: verification of "CYCLE: Synthesis `drivers` library body"

## Critique

This report fills `book/src/synthesis/drivers.md` — the topological-last (6th) Synthesis
library chapter, rendering the entry-point surfaces (6 sim drivers + 6 output products +
the lifecycle ROOT) as synthesized library code composing the c136-rendered calculus
libraries by name. It is an **implementation-VIEW** chapter (a navigational-container, not a
DAG node), so several of the 8 checks are adapted along the lines of the feature-surface
composition-root kind (the Synthesis VIEW is the analogous recompose-already-firm-vocabulary
shape: it makes no new per-op algebraic claim, asserts no rotation, has no variant axes of
its own — those live in the composed L4 ops). The verifications below were run against the
on-disk artifact, not the report's self-description.

### Checks run

**citation-validity — pass.** The chapter's discipline is link-don't-restate: it re-cites no
L0 (the L4 chapters + concept pages own the citations), so there are few raw `(file:lines)`
pinpoints to bounds-check. The two L0 citations that DO appear — `palace/main.cpp:257-280`
(the `switch (iodata.problem.type)` dispatch) and `palace/main.cpp:276` (the `BOUNDARYMODE`
branch) — were verified on-disk: the switch opens at :259 and runs through the `BOUNDARYMODE`
case at :276-278 ending :280; both citations are accurate and in-range, and the rendered
`dispatch ELECTROSTATIC = electrostatic` … `dispatch BOUNDARYMODE = boundary_mode` block
faithfully transcribes the six switch cases. The config-record framing citation
(`concepts/config-record.md:107`, "There is one IoData type; the per-driver config records
are projections of it") was verified on-disk at config-record.md:107-126 — the authoritative
framing the report claims, NOT an invention. No `verified_against:` block is present, so that
sub-check no-ops.

**surface-or-evidence — pass (adapted, composition-root kind).** This is a recompose-outward
VIEW, not a refinement of an existing operator, and not a new per-op algebraic claim. Per the
feature-surface adaptation, its evidence is the constituent down-links + the authoritative
composition-root chapters. Spot-checked three: (1) `electrostatic` renders
`gram_reduce(w≡1) ∘ solve_family ∘ fe_assemble` — matches `feature/electrostatic.L4.md` "## The
composition" exactly (assemble K once → per-terminal solve_family → w=1 gram_reduce). (2)
`driven` renders `sparameter_reduce ∘ frequency_sweep ∘ fe_assemble(×3)` — matches
`feature/driven.L4.md`; the rendered `sparameter_reduce (ports cfg) (driving_columns es)`
correctly uses the canonical `sparameter_reduce :: [PortMode] -> [(Int, Tensor)] -> Matrix`
arg order (data-algebra.md:394), composing the canonical signature faithfully. (3) `lifecycle`
renders `fold_solve (dispatch (problem_type cfg)) ∘ build_mesh` — matches
`feature/lifecycle.L4.md` (build_mesh → dispatch on problem.type → state-generated fold_solve
AMR). **Record-definition sub-check:** the per-driver config records (`ElectrostaticConfig`
etc.) are named in driver signatures, but the report correctly homes them as projection-views
of the one `IoData` (definition home = `concepts/config-record.md`, back-linked, no
field-schema restatement) — the record-definition obligation is satisfied by the existing
home, not violated. `WaveguideModeTable` → `concepts/WaveguideModeTable.md` (exists);
`DomainData` → single-consumer in-chapter home, no new consumer created. No undefined
signature-named record.

**rotation-quality — pass (no-op, not applicable to Synthesis implementation-VIEW kind).**
The drivers library asserts no algebraic/structural rotation — it recomposes already-firm L4
vocabulary outward as synthesized code (the implementation VIEW). Analogous to the
feature-surface kind's formal no-op for this check.

**variant-axis-coverage — pass (no-op, not applicable).** The drivers library has no variant
axes of its own; the axes (e.g. `gram_reduce`'s weight axis distinguishing capacitance from
inductance, `fold_solve`'s schedule-source axis) live in the composed calculus ops. The
report nonetheless surfaces them inline where relevant (the `w=1` vs `w=1/(IᵢIⱼ)` weight
distinction; the state-generated vs fixed-list fold form). No hidden branch.

**cross-reference-integrity — pass (load-bearing for this kind).** All 18 `reference`-class
edges in the `[new]` frontmatter resolve on-disk: `feature/spine-root.md`, all 13
`feature/*.L4.md` (electrostatic … lifecycle), `concepts/config-record`, and the 5
`synthesis/*` siblings. In-body links verified: `concepts/WaveguideModeTable.md`,
`L4/index.md`, `semantics/index.md`, `L1/build_mesh.md` all exist. The intra-page anchors
resolve under the mdBook slugger: `#capacitance--voltage-w--1-gram-output-product` and
`#energy_fields--per-domain-energy-table-output-product-driver-agnostic` match their `###`
headings; the index.md `#type-placement--cluster-a-type-with-its-api-group` anchor matches the
on-disk `### Type placement — cluster a type with its API group` heading. The composed
calculus-op slugs all resolve to rendered defs (verified canonical signatures: `gram_reduce k
xs w`, `solve_family op rhss`, `frequency_sweep fam omegas`, `fold_solve op s0 schedule`,
`eigsolve`, `sparameter_reduce ports family`, `waveguide_mode_reduce res w`). **Build-readiness
guard:** the three proposed-changes blocks use 4-backtick outer fences with balanced parity (6
fences = 3 open + 3 close), inner ` ```text ` blocks at 3-backtick nest cleanly (28 inner
fences, even parity) — the cycle-019 truncation hazard is correctly avoided. No firm-body
fence concern (this is a VIEW chapter, no firm `## Status` apparatus claimed). **No
maturity-overclaim:** the report composes a `roadmap_goal`/un-rendered AMR leaf
(`estimate_mark_refine`) and a mesh-scaffold (`build_mesh`) BY REFERENCE rather than
fabricating defs — appropriate (the AMR synthesized impl is not a batch-44 Synthesis
deliverable; this is a named-not-invented constituent, not an evasion; flagged in Open
questions as `synthesis-lifecycle-amr-estimate-mark-refine-rendered-by-reference`).

**edge-label-fidelity — pass.** No L_{n+1}→L_n lowering-edge label is carried (this is a
within-Synthesis VIEW, not a lowering theme). The `reference`-class edges are correctly typed
and discussed (the prose repeatedly affirms `reference`-class-only, no `depends-on`, no rank/
liveness constraint — consistent with the implementation-VIEW frontmatter and the graded-stack
scheme §4/§5). Not applicable in the lowering sense; pass.

**plan-kind-consistency — pass.** Declared kind is a rendered implementation-VIEW library
chapter (filled `navigational-container`, no `status:`/`rank:`). The content shape matches:
synthesized composition defs with code-doc (`# Arguments`/`# Returns`), topological order,
`#extern` by-reference for opaque kernels, link-don't-restate. The frontmatter convention claim
was verified — `types.md`/`coordination.md`/`data-algebra.md` carry `kind:`-only frontmatter
with NO `status:` field (the body `> **Status: \`seed\`**` banners in coordination/data-algebra
are confirmed c136 residuals in the body, not frontmatter), and the drivers `[new]` correctly
carries no `status:` field and no body status banner — matching the filled-VIEW convention. The
stub→filled flip is internally consistent (no leftover `stub` placeholders in the rendered
body).

**skill-uptake-survey — pass (telemetry only).** The relevant procedural skill for this shape
is the proposed-changes-fence-encloses-full-body-guard discipline, which the report applies
(4-backtick fences, by self-statement and verified on-disk). No skill invocation is mandatory
for a VIEW-rendering dispatch; the fence + KaTeX-`$`-sigil-fence disciplines are followed.
Non-blocking.

### Issues found

None. The report is clean across all 8 checks.

Minor (non-issue, recorded for the integrator's awareness, not a finding):
- The `feature/driven.L4.md` source column renders `sparameter_reduce es (ports cfg)` (es-first),
  while the canonical `data-algebra.md` signature is `sparameter_reduce ports family` (ports-first).
  The Synthesis render correctly follows the **canonical** signature (ports-first), so this report
  is faithful; the discrepancy is a pre-existing arg-order inconsistency in the feature column, NOT
  a defect introduced here. Out of scope for this report; noted only so it is not mis-attributed.
- The two index.md edits and the drivers.md stub→body merge edit all have `[old]` blocks that
  match the on-disk files exactly (drivers.md is exactly its 30-line stub; index.md:40 and
  index.md:63 match verbatim) — the edits will apply cleanly.
