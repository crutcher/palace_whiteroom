---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T090000Z
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
  rank-invariant: warning
  reachability: pass
repaired_at: 2026-06-05T093000Z
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
  rank-invariant: repaired
  reachability: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Disposition of three homeless concept-primitives at L1 — set_subvector_zero / trsv / gemv_basis"

## Critique

### Checks run

**citation-validity — pass.** Re-verified the load-bearing L0 sites via codemap `read_range`, all zero-drift:
- `vector.hpp:220-221` — the `double s` `SetSubVector` decl is on lines 220-221 (the doc-comment on :218-219). The report cites the decl as `:220-221` (index/Status) and `:221` (Evidence/YAML); both in-range and accurate.
- `vector.cpp:461-474` real body confirmed (`void SetSubVector(Vector &x, …)` at :461; `X[id] = sr;` at :472; `x.ReadWrite` at :467; `rows.Read` at :466).
- `vector.cpp:476-492` complex body confirmed (`template <>` at :476, `SetSubVector(ComplexVector …)` at :477; `XR[id] = sr;` at :489; `XI[id] = 0.0;` at :490).
- Use-sites all confirmed verbatim: `divfree.cpp:173`, `gmg.cpp:194`, `distrelaxation.cpp:114` and `:143`, `spaceoperator.cpp:945`, `rap.cpp:186` (the `1.0` parent-shape anchor).
- `orthog.hpp:71-74` — the CGS post-reduction loop `for (j…) { w.Add(-H[j], V[j]); }` confirmed on :71-74.
- The `trsv` NO-L0-SITE claim mechanically confirmed: codemap `search_text 'trsv|trsm|TriSolve|TriangularSolve|SpTrSV'` returns **zero hits** across the tree — the obstruction disposition is correct.
- The "~40 call sites" claim: a `SetSubVector(…, 0.0)` regex returns 37 distinct hits (rap.cpp dominates with ~21, plus divfree/gmg/distrelaxation/spaceoperator/romoperator/waveport/curlcurl); "~40" is plausible and appropriately hedged. The `verified_against:` YAML block round-trips cleanly under `yaml.safe_load` (no `note:` value opens with a quote character).

**surface-or-evidence — pass.** This is an audit-first disposition, not a refinement of existing surface. `set_subvector_zero` is a genuine reused Palace primitive (positive L0 body read in full, 37+ call sites) warranting a firm L1 entry, NOT a manufactured operator — it passes the black-box-vs-accelerated-kernels test as a named, reused vocabulary atom with a distinct BC-enforcement role (genuinely distinct from `eliminate_essential_bc`'s operator-row/column zeroing and `eliminate_rhs`'s affine lift, both of which consume it). The `trsv` and `gemv_basis` concept-only dispositions are correctly audit-first: `trsv` has no positive site (an obstruction theme already owns it; CLAUDE.md §Scope forbids manufacturing the operator) and `gemv_basis` is an inline fold-shape with no standalone callable (already lifted by firm `orthogonalize`). No operator manufactured where none exists — exactly the policy. Record-definition sub-check: the signature names `DofSet[N]`, which the entry explicitly references to the existing `essential_dofs` home rather than redefining (the §Record definition section states no new record is named) — definition-home obligation satisfied.

**rotation-quality — pass.** The projector model `Z_idx = I − P_idx` is sound on positive source: the per-index writes `X[id] = sr` (sr=0) are independent (each write reads no other entry), grounding idempotence, linearity, index-set-union commutation, self-adjointness, and the no-reduction non-law directly from the body. The L1 pure-functional form is strictly more abstract than the L0 in-place-overwrite + device-dispatch + `forall_switch` mechanism (state hiding of the `ReadWrite`/`use_dev`/buffer-threading machinery into the L1>L0 lowering). Not a rename. The complex-case whole-dof zeroing (both `XR` and `XI`) is correctly read off `:489-490`.

**variant-axis-coverage — pass.** Two axes named and dispositioned: element-type (real | complex, absorbed as a uniform parameter; complex zeros the whole dof) and index-set size (parameterised, absorbed-as-form). The scalar-value axis is explicitly scoped out — this entry is the `s = 0.0` specialization, with the general `s` (e.g. `1.0` at `rap.cpp:186`, `waveportoperator.cpp`) named as the parent shape, not folded in. No hidden branches.

**cross-reference-integrity — warning.** All *resolving* targets verified on disk: `back_solve`, `orthogonalize`, `eliminate_essential_bc`, `eliminate_rhs`, `divfree-projector`, `lu_solve`, `reciprocal`, `elementwise_product`, `essential_dofs`, `linear_combination`, `triangular-solve-obstruction`, and the three concept pages all EXIST. The SUMMARY alpha-placement (after `scal`, in the BLAS-1 group) and the L1-index dep-map row placement (between `scal` and the `**Operator application & assembly**` group header) are both alpha-correct. The consumer concept-naming claims are verified (`divfree-projector.md` and `eliminate_rhs.md` both name `set_subvector_zero`/`set_subvector` as concept references). The warning is for **two `depends-on`/`reference` edges in the new entry that point at non-existent files**: `L1-L0/set-subvector-zero-mutation-rotation` (the `depends-on`) and `L3/set-subvector-zero-mask-multiply` (a `reference`). As live links these are hard `linkcheck2` errors at build time unless the integrator materializes stubs or demotes them. The report flags BOTH in Open questions with concrete integrator options, so this is surfaced-not-hidden — but it remains a build-readiness issue the integrator must resolve, hence warning (not pass).

**edge-label-fidelity — pass.** The new entry's typed `edges:` are coherent with the prose: the `depends-on` to the L1>L0 lowering theme matches the §Downward-to-L0 narration; the `reference` edges (eliminate_essential_bc / eliminate_rhs / divfree-projector / L3 mask-multiply / concept page) all match their in-prose roles. The §Downward "non-adjacent identity rotation, annotated in-line" L1→L3 framing correctly follows the CLAUDE.md non-adjacent-identity convention (no `L1-L3/` directory created). Edge directions are right.

**plan-kind-consistency — pass.** A new firm L1 operator with full firm apparatus (Status with firm-on-positive-structure justification + no-dedicated-test non-gating argument, Signature with named-axis shape contract, six laws + three explicit non-laws, Dependencies, Variant axes, Record-definition note, Downward, Evidence with verified_against). Content shape matches the `firm` kind; no rough-in placeholders. The two concept-only repoints are correctly NOT promoted to operators.

**skill-uptake-survey — pass.** The report cites citecheck `--anchor` self-verification on the load-bearing pinpoints and codemap `search_text`/`read_range` localization throughout — appropriate skill/tool uptake for an audit-first harvest. Pure telemetry; non-blocking.

**rank-invariant (graded-stack check 9) — warning.** The entry declares `rank: firm` (rank 3) but its sole `depends-on` edge targets `L1-L0/set-subvector-zero-mutation-rotation`, which does **not exist** (effectively rank-0/un-ranked). The well-foundedness invariant `rank(u) ≤ rank(v)` is violated by a firm node resting on a missing depends-on dep. The report itself diagnoses this precisely and recommends option (b): retype the lowering-theme edge to `reference` (navigational, rank-free), grounding firmness on the positive L0 read alone — which matches how `reciprocal`/`elementwise_product` are firm without their L1>L0 themes blocking rank. The fix is the repairer/integrator's call; flagged here per the HARD-gate-new rank rule.

**reachability (graded-stack check 10) — pass.** The new entry is reachable: it is `reference`-linked from firm consumers (`eliminate_rhs`, `divfree-projector`) which sit on live solver-pipeline columns, and is wired into SUMMARY + the L1 index. Not an orphan.

### Issues found

1. **Dangling `depends-on` target — build + rank-invariant issue** (CYCLE.md `new:book/src/L1/set_subvector_zero.md` `edges.depends-on`, and §Status well-foundedness paragraph; §Open-questions bullet 1). The firm entry's only `depends-on` is `L1-L0/set-subvector-zero-mutation-rotation`, a forthcoming file that does not exist on disk. Two coupled problems: (a) a live link to a missing file is a hard `linkcheck2` error; (b) a `firm` (rank 3) node resting on a missing/≤rank-1 `depends-on` violates the graded-stack `rank(u) ≤ rank(v)` invariant. The report flags both and recommends retyping to `reference`. Severity: medium (build-blocking unless resolved; self-flagged with a clean fix).

2. **Dangling `reference` target — build issue** (CYCLE.md `new:book/src/L1/set_subvector_zero.md` `edges.reference: L3/set-subvector-zero-mask-multiply`, and §Downward in-line L3 annotation; §Open-questions bullet 2). The `reference` edge to `L3/set-subvector-zero-mask-multiply` points at a non-existent future seed — a hard `linkcheck2` error as a live link. The report recommends dropping it to plain-text (the §Downward prose already carries the full annotation) unless an L3 seed is co-landed. Severity: low-medium (build-blocking as a live link; self-flagged with a clean fix; the in-prose annotation survives either way).

3. **(Telemetry, non-blocking) "~40 call sites" is ~37 by the strict-`0.0` regex** (CYCLE.md Summary, §Context, §Status, index row). The codemap `SetSubVector(…, 0.0)` count is 37 distinct hits; "~40" is appropriately hedged with "~" and "the overwhelming majority with literal 0.0", so this is accurate-within-tolerance, recorded only so a future audit does not read "~40" as an exact count.

### Note on resolution
Issues 1 and 2 are both pre-emptively diagnosed in the report's Open questions with concrete, correct integrator options — the harvester surfaced rather than buried them. They are flagged here for the repairer/integrator to enact (edge-retype to `reference` for #1; demote-to-plain-text or co-land-stub for #2), not as authoring defects.

## Repair

### Fixes attempted

- **Finding**: Dangling `depends-on` to non-existent `L1-L0/set-subvector-zero-mutation-rotation` — (a) linkcheck2 hard error on the live link, (b) rank-invariant violation (firm rank-3 node resting on a missing/un-ranked depends-on dep). (critic issue 1; `cross-reference-integrity` + `rank-invariant` warnings)
  - **Decision**: repaired
  - **Action**: Retyped the `depends-on` block in `new:book/src/L1/set_subvector_zero.md` frontmatter (CYCLE.md proposed-changes) to three `cites-evidence` edges targeting the positive L0 source — `palace/linalg/vector.cpp:461-474` (real body), `:476-492` (complex body), `vector.hpp:220-221` (decl) — all codemap-confirmed zero-drift this invocation. A firm L1 operator's blocking dependency is its rank-terminal L0 ground truth, so `rank(u) ≤ rank(v)` now holds. The forthcoming L1>L0 theme `set-subvector-zero-mutation-rotation` is demoted to a plain-text "(forthcoming)" note in §Semantics, §Status (well-foundedness paragraph rewritten), and §Downward — matching the `reciprocal` / `elementwise_product` convention (firm on positive L0 read, L1>L0 theme is a downward narration, not an upward rank-blocking dep). Removed the live markdown link `[...](../L1-L0/...mutation-rotation.md)`.

- **Finding**: Dangling `reference` edge to non-existent `L3/set-subvector-zero-mask-multiply` — linkcheck2 hard error on the live link. (critic issue 2; `cross-reference-integrity` warning)
  - **Decision**: repaired
  - **Action**: Removed the `L3/set-subvector-zero-mask-multiply` entry from the `reference:` edge list in the frontmatter, and demoted the §Downward in-line L3 annotation from a live markdown link to a plain-text "speculative future L3 seed" note (the prose already carried the full non-adjacent-identity-rotation annotation, so nothing is lost). All surviving `reference` edges (`eliminate_essential_bc`, `eliminate_rhs`, `divfree-projector`, `concepts/set_subvector_zero`) were critic-confirmed to exist on disk.

- **Coupled cleanup**: Rewrote the two §Open-questions bullets that posed these as undecided integrator options ((a)/(b) edge-typing; demote-vs-co-land-stub) to mark them RESOLVED by the repairer, so the integrator does not re-litigate a settled fix.

Telemetry issue 3 ("~40 vs ~37 call sites") is accurate-within-tolerance (appropriately hedged "~"); no edit — not a defect.

The audit-first dispositions (set_subvector_zero genuine firm L1 home; trsv / gemv_basis concept-only repoints) are sound per the critic and left untouched.

### Unrepairable findings
None. Both build-critical findings were mechanical edge-retypes within repair authority (citation/edge surgery, no substantive authoring) — the L0 source the firm rank now rests on was already cited in the entry and codemap-reconfirmed.

## Suggested resolution
`ready`. After repair, every edge in `new:book/src/L1/set_subvector_zero.md` resolves to an existing file (the four `reference` targets) or to rank-terminal L0 source (the three `cites-evidence` deps); no dangling live links remain (grep-confirmed: no `mutation-rotation.md` / `mask-multiply.md` link survives), and the `firm` rank rests only on rank-terminal evidence. Integrator note: the two demoted forward-references (`set-subvector-zero-mutation-rotation` L1>L0 theme, `set-subvector-zero-mask-multiply` L3 seed) are now plain-text future authoring items, not stubs to materialize this cycle.
