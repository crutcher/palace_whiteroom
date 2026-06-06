---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T211500Z
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
repaired_at: 2026-06-06T212000Z
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

# META: verification of "Formalize build_mesh at L1"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck --scan` (31 ok / 0 failing — bounds + path-hygiene clean) and anchor-confirmed every load-bearing pinpoint against on-disk source. The producer's claim to have corrected the prompt's off-by-one END-line hints is **fully verified**: `palace/fem/mesh.hpp` confirms variadic ctor `:72-75`, `unique_ptr`-adopting ctor `:76-81` (with `EnsureNodes()` `:79` + `Update()` `:80`), single-machine read surface `:84-96` (`Get` `:84-85`, `Dimension`/`SpaceDimension`/`GetNE`/`GetNBE` `:93-96`), libCEED accessors `:96-115` — exactly the corrected ranges, not the prompt's `:69-72`/`:73-77`/`:84-94`. The record-definition field rows (`mesh` `:49`, `loc_attr`/`loc_bdr_attr` `:51-59`, `ceed_from_self` `:60`, `geom_data` `:62-69`) all confirm. `main.cpp:286-301` confirms `mesh::Load` `:287`, `solver->Preprocess` `:288`, `mesh::Partition` `:290`, `mesh::RefineMesh` `:291`, `make_unique<Mesh>` `:299`. `geodata.hpp:25-50` confirms the four stage decls; `geodata.cpp` confirms `Load` `:122`, `use_mesh_partitioner` `:134,140-143`, `RefineMesh` `:421`, the MFEM_VERIFY single-mesh precond `:424-425`, `uniform_ref_levels` read `:426`, level-reserve `:427-430`, and the refinement loop `:448`. All citations point to real, in-range, anchor-matching locations. The single **warning** is a citation-supported-vs-prose mismatch on **region refinement** (see Issues #1): the prose repeatedly folds region (box/sphere) refinement into the `RefineMesh`/a-priori-refine stage, but the cited source (`geodata.hpp:45-46` + the in-body comment `geodata.cpp:423`) states region refinement happens in `Load` on the serial mesh and `RefineMesh` does **only** parallel uniform refinement. The citations are correct; the prose attributes a stage's behavior to the wrong cited function. Not a `fail` (no fabricated/out-of-range citation; the pipeline narration is otherwise faithful), but a real prose-vs-evidence inaccuracy.

**surface-or-evidence — pass.** This is a new firm L1 operator entry (not a refinement-shaped modification of an existing operator/theme), so the rotation_claim-vs-surface gate is the "new chapter with evidence" shape: the surface (the L1 `build_mesh :: Config -> Mesh` form + the four-stage pipeline) is backed by positive L0 evidence (the `Mesh` ctor chain `:72-81`, the `main.cpp` build referent `:287-301`, the `geodata` stage decls + bodies). The **firm-on-positive-structure escape is correctly applied**: the four laws (config determinism, pipeline-staging order, zero-refinement identity, a-priori level-monotonicity) are genuinely syntactic identities / composition facts read off positive source — there is no convergence or iteration semantics in `build_mesh` itself (the refinement *depth* is a fixed config field `uniform_ref_levels`, read at `geodata.cpp:426`; the loop `:448` is a bounded `for` over that fixed depth, not an adaptively-driven fixpoint). The adaptive estimate-mark-refine loop is correctly externalized to the `lifecycle` root as a non-law + obstruction, so it does not bear on `build_mesh`'s firm claim. This matches the cited `fe_space` / `fe_assemble` / `apply_linop` no-dedicated-test precedent — the missing mesh-construction unit test does not gate syntactic-identity laws. **Record-definition sub-check: pass.** The signature names a record (`Mesh`); the chapter authors an in-chapter `## Record definition` section (fields + types + meaning + construction-vs-run-time stratum + the L0 home `class Mesh palace/fem/mesh.hpp:44`) AND flags `record-Mesh-needs-definition-home` for a `concepts/mesh.md` page since `Mesh` has ≥2 consumers. The record has a definition home and a correct routing flag — exactly the obligation. (The `Config`/`Mesh`/`FECollection` types it references are defined elsewhere — `Config` via `concepts/config-record.md` which exists; `FECollection`/`FiniteElementSpace` in `fe_space.md` — and are merely referenced here, correctly not re-defined.)

**rotation-quality — pass.** L1 is the mutation-rotation layer; the rotation asserted is that the L0 free-function chain mutating `unique_ptr` mesh handles in place (the `mfem_mesh` vector grown in place by `RefineMesh`, the `EnsureNodes()`+`Update()` finalization) re-expresses as a pure `config → Mesh` function over an immutable typed value. This is state-hiding / mutation-erasure compression — strictly more abstract than the L0 form (the in-place handle mutation and the level-vector growth are absorbed into a value-returning pure function), not a 1:1 rename. Genuine rotation.

**variant-axis-coverage — pass.** The orthogonal variant axes here are the single-machine carve-outs (single-rank vs multi-rank partition; `loc_attr`/`loc_bdr_attr` per-process remap). These are **explicitly scoped out** in a dedicated `## Scope (single-machine — flag-once-skip)` section that names each carve-out, cites the multi-rank machinery being skipped (`use_mesh_partitioner` `geodata.cpp:134,140-143`; the `MeshPartitioner`-vs-byte-string-broadcast policy), and states the two carve-outs are the only ones. No hidden branches. The MFEM-opaque adaptive AMR axis is also explicitly scoped out (non-law + obstruction routed to the lifecycle root). Per CLAUDE.md §Scope this flag-once-skip handling is correct.

**cross-reference-integrity — pass.** Every `[link]` resolves: `book/src/L1/fe_space.md` (EXISTS, and `mesh: Mesh` input confirmed at `:33,71-73`), `book/src/feature/lifecycle.L1.md` (EXISTS; forward-ref `build_mesh :: Config -> Mesh` confirmed at `:37`, stage-(1) narration at `:44`), `book/src/concepts/config-record.md` (EXISTS), `book/src/L0/fespace-file.md:159-164` (EXISTS, libCEED-cache precedent confirmed), `book/src/semantics/index.md` §1.2.1 (EXISTS, §1.2.1 "Named shape groups" present at `:73`). `concepts/mesh.md` is MISSING but is correctly *flagged as a future concept page* (`record-Mesh-needs-definition-home`), not asserted as a resolving link in this chapter. **Build-readiness guard: pass** — the firm claim's full apparatus (`## Status` + Signature + Algebraic laws + Record definition + Evidence) is INSIDE the `new:book/src/L1/build_mesh.md` fence (lines 38–275); fence enumeration shows 6 markers = 3 balanced blocks, even parity, no body authored outside the fence. The integrator NOTEs about kind-grouping placement (new `Mesh & FE-space construction` grouping vs fold into `FE-space sub-spine`) are well-formed and defer correctly to D4/integrator.

**edge-label-fidelity — pass.** The graded-stack edges declared are `depends-on` (cites-evidence to the two L0 ranges) + `reference` (to `L1/fe_space`, `feature/lifecycle.L1`). The prose discusses exactly these: the L0 evidence ranges are the cited substrate, and the references are the consumer (`fe_space`) and composition root (`lifecycle`). The chapter correctly declines to assert a `lowers-to` edge to the not-yet-authored `build-mesh-construction-rotation` L1>L0 theme (would point at a non-firm/absent node) — consistent with the well-foundedness rank invariant. No mislabeled edge.

**plan-kind-consistency — pass.** Declared kind is a firm L1 operator entry; content shape matches — no rough-in placeholders, the firm apparatus is complete and the `firm (firm-on-positive-structure)` status is justified by positive source + syntactic-identity laws. The rank-invariant (graded-stack check 9) holds: this `firm` (rank 3) node's only `depends-on` edges are cites-evidence to rank-terminal L0 source (rank-terminal ground truth ≥ 3), so it does not rest on any lower-rank node. Reachability (check 10): reachable from the `lifecycle` feature root (which forward-references it as stage 1) — live, not garbage.

**skill-uptake-survey — pass.** The report's shape (citation-heavy L0 localization with off-by-one close-brace risk) implies the `citecheck` tooling + the FE-source close-brace drift guard, and the report explicitly references self-verification with `tools/citecheck/citecheck.py --anchor` + direct `Read` confirmation of close-brace END lines (CYCLE.md §Supporting evidence). Telemetry present; no blocking concern.

### Issues found

1. **(citation-validity, warning) Region refinement attributed to the wrong pipeline stage.** Location: `build_mesh.md` body — the pipeline narration (`## Context`/signature prose "load → preprocess → partition → a-priori-refine", lines ~70-71), the §Scope intro, and especially **Algebraic law 3 (Zero-refinement identity)**: "With `uniform_ref_levels == 0` **and no region refinement**, `RefineMesh` produces the single partitioned mesh unchanged." The cited source contradicts the attribution: `geodata.hpp:45-46` ("parallel uniform refinement only; box/sphere region refinement happens in Load on the serial mesh") and the in-body comment `geodata.cpp:423` ("Box / sphere region refinement happens in Load.") establish that **region refinement is a serial-stage `Load` activity, not a `RefineMesh` activity**. `RefineMesh` (the cited `:421-455` body) does ONLY parallel uniform refinement keyed on `uniform_ref_levels`. So the zero-refinement-identity law as stated ("no region refinement → `RefineMesh` identity") conflates two stages: with `uniform_ref_levels == 0`, `RefineMesh` is the identity on the partitioned mesh *regardless of region-refinement config* (region refinement already happened upstream in `Load`). The law's conclusion (RefineMesh is identity at zero uniform levels) is correct; its stated *precondition* ("and no region refinement") mis-locates region refinement. Severity: low-moderate — the firm structure and the 4-stage decomposition are sound, but the prose miscredits which stage performs region refinement, and a reader taking law 3 literally would believe `RefineMesh` handles region refinement. Candidate fix: relocate region refinement into the `Load`/serial-prep stage in the pipeline narration and drop the "and no region refinement" clause from law 3 (or recast it as a `Load`-stage fact).

2. **(surface-or-evidence, observation — not a check failure) `Preprocess` stage anchored only at its call site.** Location: `## Context`/Evidence — `solver->Preprocess` (`main.cpp:288`) is named as pipeline stage (2) but its body is not cited (only the call site + the `BaseSolver::Preprocess` virtual, which I confirmed exists at `basesolver.hpp:54`). This is appropriate at L1 (Preprocess is a per-driver hook treated as a named opaque stage, and the firm claim rests on the construction *structure*, not Preprocess internals), so it is **not** a citation-validity failure — flagging only as a note for the downstream L1>L0 `build-mesh-construction-rotation` theme, which will need to cite the Preprocess hook bodies when it narrates the actual rewrite. No action required on this chapter.

### Notes for downstream

- The off-by-one close-brace corrections the producer self-reported are real and verified — this is exactly the FE-source close-brace drift the prompt warned about, caught correctly. No drift remains in the cited ranges.
- The firm-on-positive-structure escape is correctly applied and not an over-claim: the laws are syntactic identities, the only iteration (`RefineMesh`'s `for` loop) is a bounded sweep over a fixed config depth, and all genuinely convergence/adaptive semantics (the estimate-mark-refine fold) are externalized to the `lifecycle` root as obstruction. This is the `apply_linop`/`fe_space` situation, not the `eigsolve` situation.

## Repair

### Fixes attempted

- **Finding (citation-validity, warning)**: Region (box/sphere) refinement attributed to the wrong pipeline stage — the prose (signature/Context intro + Algebraic law 3) folds region refinement into `RefineMesh`/a-priori-refine, but the cited source places region refinement in the serial-stage `Load`; `RefineMesh` does parallel uniform refinement only.
  - **Decision**: repaired
  - **Action**: Two surgical prose edits to `reports/<id>/CYCLE.md`, both inside the `new:book/src/L1/build_mesh.md` fence.
    1. Signature/Context intro pipeline narration (`build_mesh.md` header prose): moved box/sphere **region refinement** into the load → serial-prep stage ("read the serial mesh from disk and perform all serial-stage preparation (including the box/sphere region refinement of the serial mesh)"), and re-scoped the final stage to "a-priori parallel **uniform** refinement".
    2. Algebraic law 3 (Zero-refinement identity): dropped the "and no region refinement" precondition clause; the law now reads "With `uniform_ref_levels == 0`, `RefineMesh` produces the single partitioned mesh unchanged", and adds the stage-attribution fact ("`RefineMesh` performs parallel uniform refinement only — box/sphere region refinement happens earlier, in the `Load`/serial-prep stage") with the supporting citations `geodata.hpp:25-31,45-46` + the in-body comment `geodata.cpp:423`. The law's conclusion (RefineMesh identity at zero uniform levels) is preserved; only the mis-located precondition is corrected.
  - **Verification against on-disk source**: confirmed via codemap `read_range`. `geodata.hpp:25-31` (the `Load` decl) enumerates "region-based (box/sphere) refinement" among serial-stage `Load` activities; `geodata.hpp:45-46` states `RefineMesh` is "parallel uniform refinement only; box / sphere region refinement happens in Load on the serial mesh"; `geodata.cpp:423` carries the matching in-body comment "Parallel uniform refinement only. Box / sphere region refinement happens in Load." The corrected prose is faithful to the cited source. The remaining refinement prose (law 4, the Evidence `geodata.hpp:25-50` row "parallel uniform a-priori refinement", §Scope) already attributes correctly and was left unchanged.

- **Finding (surface-or-evidence, observation #2 — non-blocking)**: `Preprocess` anchored only at its call site (`main.cpp:288` + the `BaseSolver::Preprocess` virtual); body not cited.
  - **Decision**: not-needed
  - **Note**: Accepted as appropriate at L1 — `Preprocess` is a per-driver hook treated as a named opaque stage, and the firm claim rests on the construction *structure*, not Preprocess internals. The critic correctly flagged this as not a check failure. Recorded as a forthcoming-theme item: the downstream L1>L0 `build-mesh-construction-rotation` theme will need to cite the Preprocess hook bodies when it narrates the actual rewrite. No fix required on this chapter.

### Unrepairable findings

None. The single warning was a mechanical stage-attribution prose correction faithful to the already-correct citations; the firm structure and 4-stage decomposition were sound. The non-blocking observation requires no fix.

## Suggested resolution

`ready`. The citation-validity warning is resolved by the two surgical prose edits above (region refinement relocated to the `Load`/serial-prep stage; law 3 precondition corrected), all verified against on-disk source. The firm-on-positive-structure escape, record-definition home, and graded-stack edges are intact. Integrator note: the report carries well-formed integrator NOTEs about the new `Mesh & FE-space construction` kind-grouping placement (defer to D4/layer-intro-author per the parallel-blind shared-index guard) — no repair action needed there, just honor those NOTEs at apply time.
