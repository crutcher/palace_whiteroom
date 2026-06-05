# Cycle-104 integrator staging log

Per-report integration rows, append-only, newest LAST. Row ORDER is the authoritative apply-order record (NOT the `applied_at` timestamps, which are advisory). integrator-finalize reconciles from this log.

---

## 2026-06-05T082335Z-layer-intro-author-p1-record-concept-pages
applied_at: 2026-06-05T08:43:41Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/krylov.md (prepend typed `edges:` frontmatter — rank: firm, kind: record; 3 depends-on cites-evidence → iterative.hpp CG/GMRES/FGMRES class ranges; 8 reference)
- book/src/concepts/op-params.md (prepend typed frontmatter — 2 depends-on cites-evidence → iterative.hpp IterativeSolver base + GmresSolver variant selectors; 9 reference)
- book/src/concepts/sim-state.md (prepend typed frontmatter — 3 depends-on cites-evidence → iterative.hpp base statistics + CG/GMRES Mult iterate arg; 6 reference)
- book/src/concepts/step-outputs.md (prepend typed frontmatter — 4 depends-on cites-evidence → iterative.cpp residual proxies + CheckDot + iterative.hpp final_res; 7 reference)
- book/src/concepts/prev-carry.md (prepend typed frontmatter — 2 depends-on cites-evidence → iterative.cpp CG beta_prev + GMRES Hessenberg; 6 reference)
- book/src/concepts/solve-result.md (prepend typed frontmatter — 4 depends-on cites-evidence → iterative.hpp mutated statistics + iterative.cpp residual readouts + CheckDot; 7 reference)
- scaffolding/open-questions.md (append-only — promoted `record-concept-prose-citation-pm1-drift`; noted closure of precursor `graded-stack-six-record-concept-pages-need-frontmatter`)

Gate hits:
- yaml-validity: 0 (all 6 frontmatter blocks round-trip via yaml.safe_load; inline `#` comments after kind: values are valid YAML comments)
- rank-invariant: 0 (every depends-on edge is kind:cites-evidence → rank-terminal L0 iterative.{hpp,cpp} source range; rank: firm rests only on firm-equivalent L0 ground truth; consumers/siblings are reference [free, non-blocking] — a record does NOT block on its consumers)
- forward-edge-without-surface: 0
- dangling-reference: 0 (all reference targets resolve on disk: book/src/{L4/krylov-step + 8 concept pages + 6 sibling record pages}.md)
- SUMMARY-registration: 0 (no new files created — all 6 are pre-existing SUMMARY-registered concept pages; pure frontmatter prepend, no chapter-registration needed)
- citecheck (--scan over CYCLE.md): 20 ok, 0 failing (no MISS/AMBIG/OOB)

Open questions promoted:
- record-concept-prose-citation-pm1-drift

Build-relevant: yes

Notes: Pure typing dispatch (frontmatter prepend onto 6 existing record-definition concept pages) per the graded-stack typed-edge campaign P1. All 6 on-disk `## Status` lines read `firm`; the 3 constructive records (step-outputs/prev-carry/solve-result) have no single named C++ struct, so their cites-evidence edges point at per-field positive L0 backing ranges (loop-body residual computations + in-place-mutated instance fields) — genuine rank-terminal backing, a legitimate by-design struct-granularity exception (critic re-verified against source: pass). Anchors all matched on disk exactly (each file began directly with its H1, no pre-existing frontmatter — clean valid-YAML prepend). This dispatch CLOSES the c103 precursor OQ `graded-stack-six-record-concept-pages-need-frontmatter` (the record-page tranche of the P1 campaign). No book rebuild / commit here (finalize's job). Deferred `integrated_at` to finalize per role-spec. First per-report integrator this cycle — created the staging dir + this log.

---

## 2026-06-05T000000Z-lifter-prose-drift-fixes
applied_at: 2026-06-05T085042Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/index.md (de-stale the `eliminate_rhs is now FIRM` cohort bullet — drop the stale plain-text tail "L1>L0 lowering `eliminate-rhs-mutation-rotation` forthcoming (theme not yet authored)"; re-anchor to a live link → `../L1-L0/fe-operator-assemble-mutation-rotation.md` (firm covering theme, c103 D6 FOLD home). All L0 citations in the bullet carried VERBATIM — no new pinpoint emitted)
- book/src/concepts/incremental-least-squares.md (slug-fix §Dependencies — repoint non-existent `givens-rotation` → live link `[givens](./givens.md)`; bare-backtick mention upgraded to a resolving markdown link)

Gate hits:
- dangling-live-link: 0 (both new live link targets confirmed on disk: `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` exists + is `status: firm`; `book/src/concepts/givens.md` exists. Stale `concepts/givens-rotation.md` confirmed ABSENT. Both new markdown links resolve by relative path — build-safe, no `linkcheck2` break; fix 2 is a NET REDUCTION in dangling-slug surface)
- rank-invariant: 0 (no rank/status flip; pure prose/reference hygiene — no `depends-on` edge added or promoted)
- forward-edge-without-surface: 0 (the re-anchored reference points at an EXISTING firm theme + its §"folded here" anchor at :247, not a forthcoming surface)
- citecheck (--scan over CYCLE.md): 7 ok, 1 failing — the single `[AMBIG]` is on `incremental-least-squares.md:43`, which is the REPORT'S OWN self-reference to the edited filename in its Discipline-notes prose (`Fix 2 (incremental-least-squares.md:43)`), NOT an emitted L0 citation; basename collides between book/src/L2/ and book/src/concepts/. Confirmed scan artifact on report prose (critic pre-flagged it), NOT a citation defect → non-blocking, no MISS/OOB

Open questions promoted:
- (none — this report's Open-questions section is "None"; no new OQ to promote)

Build-relevant: yes

Notes: D4 — pure lifter prose-drift hygiene; structure + all claims unchanged. Re-read both targets off disk immediately before editing. The `eliminate_rhs` bullet had DRIFTED from line 96 → line 97 on disk — the prior in-cycle `harvester-homeless-primitives` staging row (above) records a `book/src/L1/index.md` dep-map row + Vocabulary-cohort bullet insert, which accounts for the one-line downward shift I OBSERVED; the bullet's `[old]` text still matched VERBATIM at its new line 97, applied cleanly. The fix 2 anchor matched at line 43 exactly. RESOLVES two pre-existing c103 LOW-fan-out NON-build-breaking OQs whose recorded route was "a future touch rewrites the prose" — these edits ARE that touch, both now resolved on disk: `eliminate-rhs-l1-index-bullet-stale-forthcoming-prose` (open-questions.md:1288) and `incremental-least-squares-prose-names-nonexistent-givens-rotation-slug` (open-questions.md:1274). I did NOT edit the OQ ledger to close them (per-report integrator OQ authority is append-only promotion of NEW questions; close/unify is meta-phase authority) — flagging here so finalize/meta-phase can close both at batch unify. Deferred `integrated_at` to finalize per role-spec. This is report 3/4 per the dispatch; two prior per-report staging rows are present (record-concept-pages + homeless-primitives) and the `L1/index.md` line shift I observed on disk is consistent with the homeless-primitives row's recorded insert above the bullet — I describe only the on-disk state I directly read, not an assumed sibling apply order.

---

## 2026-06-05T082448Z-harvester-homeless-primitives-disposition
applied_at: 2026-06-05T08:49:03Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/set_subvector_zero.md (CREATE — new firm L1 operator; the `s=0.0` SetSubVector zeroing primitive, diagonal 0/1 projector Z_idx = I − P_idx; repairer-fixed edges: 3 depends-on `kind:cites-evidence` → L0 vector.cpp:461-474 real + :476-492 complex + vector.hpp:220-221 decl (rank-terminal, firm well-founded); 4 reference → eliminate_essential_bc / eliminate_rhs / divfree-projector / concepts/set_subvector_zero)
- book/src/concepts/trsv.md (repoint — `reference: []` → L1-L0/triangular-solve-obstruction + L1/back_solve; added §Disposition section; repointed Palace-mapping to iterative.cpp:652-660/:831-840 + obstruction theme)
- book/src/concepts/gemv_basis.md (repoint — reference extended → + L2/linear_combination + L1/orthogonalize; added §Disposition section; corrected citation orthog.hpp:51-53 → :71-74)
- book/src/L1/index.md (dep-map table row alpha-after `scal`; §Vocabulary-cohort bullet after `elementwise_product`)
- book/src/SUMMARY.md (chapter entry alpha-after `scal` in the BLAS-1 group, line 189)
- scaffolding/open-questions.md (append-only — promoted `set-subvector-zero-mutation-rotation-theme-forthcoming`; recorded full resolution of c103 `concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis` — all 3 legs disposed)

Gate hits:
- dangling-live-link: 0 (CRITICAL — repairer fix HOLDS: no `mutation-rotation.md`/`mask-multiply.md` live link survives in the new file; all 15 in-prose markdown links + all 4 reference edges + both repointed concept pages resolve on disk, grep-confirmed)
- rank-invariant: 0 (firm rank-3 entry rests only on `cites-evidence` edges to rank-terminal positive L0 source — `rank(u) ≤ rank(v)` holds; matches the `reciprocal`/`elementwise_product` firm-on-positive-structure precedent)
- forward-edge-without-surface: 0 (the L1>L0 theme + L3 seed are plain-text "(forthcoming)" notes, NOT live edges)
- SUMMARY-registration: 0 (registered alpha-placed; no auto-fix needed — report proposed the SUMMARY edit)
- alpha-position-insert: applied-as-specified (report specified `set_subvector_zero` after `scal`; SUMMARY + dep-map both alpha-correct after `scal`; cohort bullet placed after `elementwise_product` per report — the cohort prose list is not strictly alpha so I followed the report's stated placement, not a discretionary choice)
- citecheck (--scan over CYCLE.md): 35 ok, 0 failing (no MISS/AMBIG/OOB)

Open questions promoted:
- set-subvector-zero-mutation-rotation-theme-forthcoming
- (resolution recorded on c103 `concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis` — all 3 legs now disposed)

Build-relevant: yes

Notes: Report `ready` from the repairer (2 build-critical warnings REPAIRED — the dangling `depends-on` to forthcoming L1>L0 theme retyped to `cites-evidence` L0 deps; the dangling `reference` to the speculative L3 seed removed + demoted to plain-text). I VERIFIED the repairer fix held on the proposed `new:` content before writing: no `mutation-rotation.md`/`mask-multiply.md` live link present, and all surviving edges/links resolve on disk. All repoint targets (triangular-solve-obstruction, back_solve, lu_solve, orthogonalize, linear_combination, orthogonalization) confirmed to exist. trsv.md and gemv_basis.md were each re-read off disk immediately before editing (gemv_basis had a stale citation `orthog.hpp:51-53` and `.AXPY` form which the report corrects to `:71-74`/`.Add`; trsv had a stale `iterative.cpp:669-706` mapping the report corrects). FIRM-COUNT TALLY: the L1 firm grand total moves 39 → 40 (main cohort → 33) with set_subvector_zero — I did NOT touch the consolidated running-count prose at L1/index.md (the report explicitly defers it; the dispatch does not name me count-owner) — DEFERRED TO integrator-finalize as the count-owner. Deferred `integrated_at` to finalize per role-spec. Second per-report integrator this cycle (D1 record-concept-pages row precedes mine above).

---

## 2026-06-05T090000Z-layer-intro-author-feature-column-uses-record-edges
applied_at: 2026-06-05T085401Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/feature/lifecycle.L4.md (insert 1 depends-on `kind: uses-record` → concepts/config-record, after last cites-evidence basesolver.cpp:153-276, before reference:)
- book/src/feature/electrostatic.L4.md (insert uses-record → concepts/config-record, after electrostaticsolver.cpp:21-98)
- book/src/feature/magnetostatic.L4.md (insert uses-record → concepts/config-record, after magnetostaticsolver.cpp:22-108)
- book/src/feature/driven.L4.md (insert uses-record → concepts/config-record, after drivensolver.cpp:77-229)
- book/src/feature/transient.L4.md (insert 2 uses-record edges → concepts/config-record + concepts/op-params, after timeoperator.cpp:407-413; NOTE: this column has NO `reference:` key — anchored on the closing `---` instead, edges land in the same depends-on: list, semantics identical)
- book/src/feature/eigenmode.L4.md (insert uses-record → concepts/config-record, after eigensolver.cpp:32-477)
- book/src/feature/boundary-mode.L4.md (insert uses-record → concepts/config-record, after main.cpp:276-278)
- book/src/feature/capacitance.L4.md (repairer addendum — insert uses-record → concepts/config-record, after electrostaticsolver.cpp:100-140)
- book/src/feature/inductance.L4.md (repairer addendum — insert uses-record → concepts/config-record, after magnetostaticsolver.cpp:110-152)
- book/src/feature/sparameters.L4.md (repairer addendum — insert uses-record → concepts/config-record, after waveportoperator.cpp:780-793)
- book/src/feature/eigenfrequency-qfactor.L4.md (repairer addendum — insert uses-record → concepts/config-record, after postoperator.cpp:1171-1203)
- book/src/concepts/config-record.md (reciprocal back-references — append 4 columns capacitance/inductance/sparameters/eigenfrequency-qfactor.L4 to `reference:` list; now lists 11 columns)
- scaffolding/open-questions.md (append-only — promoted 2 OQs: `solve-record-reachability-needs-op-chapter-uses-record-edges` [HIGH, WAVE-3] + `energy-fields-config-and-domaindata-records-need-concept-pages` [MEDIUM])

Gate hits:
- rank-well-foundedness: 0 (all 12 depends-on edges satisfy rank(u) ≤ rank(v): 11 → config-record [rank firm=3] from columns rank firm=3 [3≤3] except boundary-mode rank rough-in=2 [2≤3]; transient.L4 → op-params [rank firm=3, D1-landed] from transient firm=3 [3≤3]. All hold.)
- dangling-edge / missing-target: 0 (both edge targets exist on-disk: concepts/config-record.md ✓ rank firm, concepts/op-params.md ✓ rank firm [D1 landed it firm this cycle, confirmed by re-read]; energy-fields.L4 deliberately NOT linked — confirmed 0 uses-record edges on disk, no dangler to a missing PostprocessConfig/DomainData page)
- yaml-validity: 0 (all 12 touched frontmatter blocks round-trip via yaml.safe_load; inline `#` comments after edge values are valid YAML; uses-record edge targets confirmed parsed — 11×config-record + 1×op-params)
- forward-edge-without-surface: 0 (pure frontmatter typed-edge inserts; no body/surface claim)
- citecheck (--scan over CYCLE.md): 31 ok, 0 failing (no MISS/AMBIG/OOB — repairer's bare-shorthand-citation normalization to `feature/transient.L4.md:38` held)
- SUMMARY-registration: 0 (no new files; pure frontmatter edits to pre-existing SUMMARY-registered chapters)

Open questions promoted:
- solve-record-reachability-needs-op-chapter-uses-record-edges
- energy-fields-config-and-domaindata-records-need-concept-pages

Build-relevant: yes

Notes: D2, report 4/4 — FINAL per-report integrator this cycle; staging is now COMPLETE for finalize. Applied 12 `depends-on (kind: uses-record)` edges (8 original [7 driver/lifecycle/boundary-mode columns + transient's extra op-params] + 4 repairer-addendum output-product columns) + the 4 reciprocal back-references in concepts/config-record.md. Re-read all 11 column files + both edge targets off disk this invocation before editing. PREREQUISITE CONFIRMED ON DISK: D1 (record-concept-pages, report 1/4 — its staging row is the FIRST in this log) landed `concepts/op-params.md` with `rank: firm` (I directly re-read its frontmatter: `rank: firm`, kind: record) — so the `transient.L4 → op-params` edge is rank-well-founded (3≤3). `concepts/config-record.md` was already `rank: firm` on-disk (c103). REACHABILITY OUTCOME: 2 of the 8 graded-stack record pages become root-reachable by this dispatch — `config-record` (now `depends-on`-reachable from 11 feature columns) + `op-params` (from transient.L4). The other 6 (`sim-state`/`krylov`/`step-outputs`/`prev-carry`/`solve-result`/`dofset`) are named in NO feature-column signature (they are L4 solve/BC OP record shapes) and remain expected tracked baseline-exceptions until the WAVE-3 op-chapter `uses-record` edges land (routed as the HIGH OQ above for cycle-105). The 4 output-product edges (repairer addendum) apply the precision rule evenly across the 12-column root set; they do not expand config-record reachability (it was already reached via the 7) but complete the navigational pairing. ENERGY-FIELDS DELIBERATELY NOT LINKED — its `PostprocessConfig`+`DomainData` have no concepts/ page; per the no-dangling-edge rule it carries 0 uses-record edges (confirmed on disk), routed to the MEDIUM OQ. Note transient.L4.md frontmatter has no `reference:` key (closes `---` after cites-evidence) — anchored the 2 inserts on the closing `---`; edges land in the depends-on: list identically (YAML re-validated post-edit). Deferred `integrated_at` + `integration_commit` to finalize per role-spec. No book rebuild / commit here (finalize's job).

---
