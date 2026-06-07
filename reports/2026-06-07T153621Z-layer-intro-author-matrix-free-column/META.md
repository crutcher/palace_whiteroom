---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T161500Z
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
repaired_at: 2026-06-07T163000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of feature/matrix-free-operator column (D1 LEAD, cycle-127)

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reported 20 ok / 3 "failing"; the 3 are `[AMBIG]` (bare basenames `operator.hpp` / `integrator.cpp` / `operator.cpp` matching both `palace/fem/...` and `palace/fem/libceed/...`), all appearing in *prose* while the load-bearing *edge* and signature citations carry the fully-qualified `palace/fem/libceed/...` paths — those qualified forms all resolve `[ok]`. I verified every load-bearing pinpoint directly via codemap: `bilinearform.cpp:118` is the `UseFullAssembly` predicate, `:140` the `BilinearForm::Assemble` partial-vs-full branch, `:147` `PartialAssemble()` (matrix-free branch) — exactly as the prose claims; `operator.cpp:182-189` is `Operator::Mult` with `y = 0.0; CeedAddMult(op,u,v,x,y); y *= dof_multiplicity` — matching the L1 surface's `y = 0; CeedAddMult(...); y *= dof_multiplicity` rendering verbatim. The cap's five self-cited anchors (`operator.hpp:32,48,81-82`; `bilinearform.cpp:118,143`) and `integrator.cpp:422-445` all resolve `[ok]`. No `verified_against:` block in this report (round-trip sub-check n/a).

**surface-or-evidence — pass (feature-surface adaptation).** Both new chapters are feature-surface composition-roots; the adapted rule is "L0 driver/source range cited AND constituent down-links resolve." The L4 surface cites the `bilinearform.cpp:118-147` construct-time dispatch + the L2 combinator's `integrator.cpp:422-445` / `operator.cpp:182-189`; the L1 surface cites `operator.cpp:182-189`. All constituent down-links resolve to real firm chapters (verified below). The cap firm-flip is a surface modification (status/banner/section-header flip) backed by exhaustively-cited composition algebra — not a bare rotation_claim. Record-definition sub-check: the constructor signature names `FESpace`/`WeakFormTerm`/`GeomFactors`/`LinearOperator`, all already-homed (the report explicitly notes `weak_form_term`, `element-local-tensor`, `geom_factor_build` homes and files no `record-...-needs-definition-home` flag) — correctly no new record gap.

**rotation-quality — pass (no-op for feature-surface kind).** A feature chapter rotates nothing; it recomposes already-firm vocabulary outward. The cap firm-flip is a status promotion of a constructor, not a new rotation claim. Not applicable to this report's shape.

**variant-axis-coverage — pass (no-op for feature-surface kind).** The matrix-free column's only axis (`UseFullAssembly` true/false — full CSR vs partial matrix-free) is explicitly scoped: this column IS the partial-matrix-free branch (`:147`), and the prose names the `full` branch (`CeedOperatorFullAssemble` CSR materialization) as the sibling out of scope. No hidden branch.

**cross-reference-integrity — warning (load-bearing for this kind).** Every constituent down-link and the cap-firm-flip's well-foundedness chain was checked on disk and resolves with the claimed maturity: `L2/matrix-free-operator-apply` `rank: firm` (:16), `L1/element_restrict` firm (:14), `L1/basis_apply` firm (:10), `L1/quad_point_contract` firm (:10), `L1/geom_factor_build` firm (:14), `concepts/element-local-tensor` firm (:2), `L1/libceed-quadrature-kernel-impl` firm (:19) — all matching the report's asserted statuses exactly. `feature/index.md`, `feature/infrastructure.md`, `feature/geometric-multigrid-preconditioner.L4.md`, `concepts/black-box-vs-accelerated-kernels.md`, `semantics/index.md`, `L4/index.md`, `L1/weak_form_term.md`, `L4/fe_assemble.md` all exist. All `[old]` edit anchors (SUMMARY:58, index:60, infrastructure:11/42, and the six cap-edit anchors in `mk_matrix_free_operator.md`) match disk verbatim. The single unresolved target is `L4-L3/mk-matrix-free-operator-dissolution.md`, referenced by BOTH new L4 files AND the cap (a `lowers-to` reference). It does NOT exist on disk; the report states D2 authors it this cycle. The warning is ordering: it is referenced via `reference`-class edges only (no rank/liveness constraint), but mdBook `linkcheck2` treats a `[link](...)` to a missing file as a hard error, so if D2's file does not land in the same integration batch the build breaks. The report's own Open-questions correctly flags the D2 forward-ref and argues (correctly) no rank-coupling — but the linkcheck2 build hazard is the residual concern for the integrator to confirm D2 lands co-batch.

**edge-label-fidelity — pass.** The four edge-classification claims were verified against disk. (1) `fe_assemble → mk_matrix_free_operator` STAYS `reference (constructs-via)`: confirmed — fe_assemble.md:15-16 carries `kind: constructs-via` and NO edit block in this report touches fe_assemble.md, so it is untouched. The report's prose ("fe_assemble folds the leaf OPAQUELY ... must NOT depends-on") matches the on-disk comment. (2) The cap's `→ L2/matrix-free-operator-apply` edge promotes `reference (lowers-to)` → `depends-on (lowers-to)` (firm→firm); the `[old]` block matches the current `reference:` placement and the `[new]` moves it under `depends-on:` — rank-legal. (3) L4 column → cap + L2 combinator as `depends-on (composes)`; (4) L1 column → 4 substrate ops as `depends-on (composes)`. The blocking chain feature-column → cap → L2-combinator → {4 substrate ops} is genuinely all-blocking: the L2 combinator's four substrate edges read `kind: composes` (blocking) on disk (matrix-free-operator-apply.md:21-27), so the RE11 grounding chain is a real `depends-on` flip, not reference-only.

**plan-kind-consistency — pass.** Declared kind: a `firm` feature-surface column + a `roadmap_goal → firm` cap flip. The firm content shape is well-formed — no rough-in placeholders, no "SPECULATIVE"-flagged bodies left in the *new* files. The cap firm-flip's three gates were independently verified: (a) well-foundedness — all blocking deps `rank: firm` on disk, `min(deps) = firm`, so `rank(cap) = firm` is rank-legal (the §1g invariant holds; no non-firm blocking dep caps it down); (b) composition algebra exhaustively cited and carrying NO loop/recurrence (the constructor is a fixed five-stage chain `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`, cited at the L2 combinator + construct-time dispatch — the firm-on-positive-structure escape, not forced); (c) a faithful root-reaching blocking `depends-on` pull now exists (the column). The firm-flip did NOT force the spine — the composition is positively cited and the gates are genuinely met. The cap-flip edits leave the section HEADERS flipped (`## L4 form`, `## Pull-chain`, etc.) consistent with `firm`.

**skill-uptake-survey — pass (telemetry).** The relevant procedural skill for this shape would be a feature-column / firm-flip well-foundedness checklist. The report performs the §1g rank-invariant check by hand (reading each dep's on-disk `rank:` line) and references the linter backstop (`graded-stack-lint --show-inbound`, `rank_violations` must stay 0). No specific skill invocation is named, but the discipline is exercised; this check is non-blocking.

### Issues found

1. **`L4-L3/mk-matrix-free-operator-dissolution.md` does not exist on disk; referenced by three landed files (cross-reference-integrity, warning, build-ordering).** `book/src/feature/matrix-free-operator.L4.md` (reference edge + §Down-narrative prose link), and `book/src/L4/mk_matrix_free_operator.md` (the cap's `lowers-to` reference edge + §Pull-chain/banner prose) all link to `../L4-L3/mk-matrix-free-operator-dissolution.md`, which is not on disk (D2 authors it this cycle). All are `reference`-class so there is no rank/liveness coupling (the report's no-coupling-hazard argument is correct), but `linkcheck2` flags a Markdown link to a missing file as a hard build error. Severity: medium — purely an integration-ordering concern; resolved iff D2's file lands in the same integration batch. The integrator must confirm D2 co-batches (or stub the slug) before `cargo make book`.

2. **Residual "SPECULATIVE"/"roadmap_goal" framing tokens in the cap chapter not covered by the proposed edits (plan-kind-consistency, minor — self-flagged by the report).** The report's own Open-questions notes the body paragraphs at `mk_matrix_free_operator.md:50,:64` retain inline SPECULATIVE/roadmap_goal-era framing not touched by the six edit blocks (which flip frontmatter, two banners, four section headers, and the constructor-signature callout). I confirmed on disk that the edits target the right anchors and that line :58 ("The apply lowers to the firm L2 contraction-chain combinator (the `reference`-class `lowers-to` edge)") will become stale (the edge is now `depends-on`). Severity: low — prose-drift in a now-firm chapter, not a build break and not caught by linkcheck2; the report routes it to the integrator as a post-apply grep (`grep -n 'SPECULATIVE\|roadmap_goal\|speculative reconstruction\|not asserted as Palace\|reference.-class .lowers-to'`).

3. **`L2/matrix-free-operator-apply` §"Speculative higher (L4) placeholder" becomes stale on this landing (cross-reference-integrity, low — out-of-scope, self-flagged).** That section (matrix-free-operator-apply.md:209-222) calls the L4 surface "NOT authored this cycle." This report lands exactly that surface and firms the cap, so the placeholder is now stale. The report correctly flags it as out-of-write-scope (L2 chapter) and files an OQ (`matrix-free-operator-apply-l4-placeholder-now-stale`). Severity: low — prose-drift, no build impact; tracked for a future touch.

## Repair

### Fixes attempted

- **Finding 1** — `L4-L3/mk-matrix-free-operator-dissolution.md` does not exist on disk; referenced by three landed files (cross-reference-integrity, warning, build-ordering).
  - **Decision**: not-needed (deferred-to-integrator; cross-report integration-ordering note — NOT an in-place fix).
  - **Rationale**: The slug is `reference`-class everywhere it is cited (no rank/liveness coupling — the critic's no-coupling argument is correct), so there is nothing to fix in D1's report in isolation. The build hazard is purely `linkcheck2`'s missing-link hard-error, resolved iff D2's file lands in the same integration batch. I **confirmed D2 authors that exact slug**: `reports/2026-06-07T153721Z-abstractor-matrix-free-dissolution/CYCLE.md` carries `` ```edit:book/src/L4-L3/mk-matrix-free-operator-dissolution.md `` (line 50) authoring the file AND wires it into `SUMMARY.md` (line 548). Both D1 and D2 are cycle-127 WAVE-1 (same `integrator-finalize`), so the forward-ref resolves co-batch. **Integrator note: confirm D1+D2 co-batch before `cargo make book` (or stub the slug as the documented fallback).**

- **Finding 2** — residual SPECULATIVE/roadmap_goal framing + a stale "reference-class lowers-to" line at `mk_matrix_free_operator.md:50,:58,:64` not covered by the firm-flip edits (plan-kind-consistency, low — self-flagged).
  - **Decision**: repaired (fixed-in-place).
  - **Action**: Verified the on-disk content of the three lines first. `:50` (the signature-intro "per the c125 D2 OQ placeholder…" line) IS already covered by the third `mk_matrix_free_operator.md` edit block (it rewrites that exact line to drop the OQ-placeholder framing). `:64` is benign body prose carrying NO SPECULATIVE/roadmap_goal/reference-class token. The genuinely-stale line is **`:58`** ("The apply lowers to the firm L2 contraction-chain combinator (the `reference`-class `lowers-to` edge):"), which falls in the un-edited gap between the edited signature header (:46-50) and the edited Pull-chain section (:66-71) and contradicts the firm-flip's frontmatter edge-promotion (`reference (lowers-to)` → `depends-on (lowers-to)`). I added a new surgical `edit:book/src/L4/mk_matrix_free_operator.md` block to D1's CYCLE.md proposed-changes (inserted after the signature edit) flipping that line to "(the `depends-on (lowers-to)` edge — promoted from `reference` at the c127 D1 firm-flip; firm→firm, rank-legal):". This is an exact-text edge-label fix (in repair authority — the "stale `reference`-class lowers-to line" / edge-label-fidelity shape); no substantive re-authoring. The post-apply `grep` the report routes to the integrator will now find no residual stale token.

- **Finding 3** — `L2/matrix-free-operator-apply.md:209-222` placeholder now stale (cross-reference-integrity, low — out-of-scope, self-flagged).
  - **Decision**: not-needed (out-of-scope).
  - **Rationale**: The L2 chapter is outside D1's write-scope (combinator-miner/harvester lineage). I confirmed D1 already files the OQ `matrix-free-operator-apply-l4-placeholder-now-stale` in CYCLE.md §Open questions (lines 678-683) for a future touch. No build impact (`linkcheck2` does not catch prose-drift). Leave as-is.

### Unrepairable findings

None. The only deferral is finding 1, which is a cross-report integration-ordering note (D1+D2 co-batch), not a defect in D1's report — no `follow_up_agent` revision is required.

## Suggested resolution

`ready`. All findings either pass (from critic), repaired in-place (finding 2 — the `:58` stale-edge-label fix added to D1's proposed-changes), or not-needed (findings 1, 3). Note for the integrator: (a) **co-batch D1 with D2** (`reports/2026-06-07T153721Z-abstractor-matrix-free-dissolution`) so the `L4-L3/mk-matrix-free-operator-dissolution.md` forward-ref resolves before `cargo make book` — confirmed D2 authors that exact slug + its `SUMMARY.md` row; (b) the report's post-apply `grep -n 'SPECULATIVE\|roadmap_goal\|speculative reconstruction\|not asserted as Palace'` on the firmed cap should now come back clean given the added `:58` edit; (c) finding 3's OQ (`matrix-free-operator-apply-l4-placeholder-now-stale`) is recorded for a future L2 touch.
