# cycle-013 integrator staging log

Per-report integration staging for cycle-013. Each `integrator-per-report` invocation
applies ONE report's proposed-changes, runs per-report safety-net gates, promotes that
report's Open questions, and appends a row below (newest LAST, append-only).
`integrator-finalize` reads this log at cycle-end to rebuild the book, repair breakage,
mark consumed reports, write the cycle-record / log / integrator-signals, and emit the
batch CYCLE.md + single commit.

---

## 2026-05-28T143232Z-abstractor-eigsolve-getconverged-forwarder-fix-and-gated-promotion
applied_at: 2026-05-28T154500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/eigsolve-mutation-rotation.md (edit — 5 proposed-changes blocks: Change 1 GetConverged forwarder snippet correction; Change 2 Sub-pattern A SetWhichEigenpairs/SolveInternal switch attribution; Change 3 Sub-pattern A citation list split; Change 4 ncv-clamp citation 518-521 + N@517 + arpack_it@522-525; Change 5a-5d partly-constructive→firm promotion)
- scaffolding/open-questions.md (append — 2 OQ sections; see below)

Gate hits:
- citation-format-sanity: 0 (all changed ranges plain-text `path:start-end`; OLD strings matched artifact pre-apply; the repaired CYCLE.md already carried the ksp.hpp:41 / ksp.hpp:64 corrections from the repair pass — applied as-repaired)
- retroactive-budget-per-slice: 0
- forward-edge-without-surface: 0
- concept_writes-on-existing-slug: 0
- variant-axis-missing: 0

Open questions promoted:
- partly-constructive-to-firm-promotion-route-ratification (routed to cycle-015 meta-phase — the escalated needs-revision methodology-judgment item: first live partly-constructive→firm promotion; ratify the "firm = no open promotion condition" reading + reconcile option-b methodology-acceptance route vs invariant per-line-audit route)
- eigsolve-mutation-rotation-embedded-audit-yaml-resolution-marker (low priority — optional `resolved cycle-013` marker on the embedded cycle-012 audit YAML so the firm status + embedded `partially-supports` entries do not appear to conflict)

Build-relevant: yes

Notes: Report META `overall_status: needs-revision`, but per the accumulate-surface-with-embedded-friction invariant needs-revision is NOT reject → the diff APPLIES. The single escalated item (repairer `unrepairable`, critic Issue 2 MEDIUM) was a methodology-judgment question only: this is the FIRST live `partly-constructive`→`firm` promotion, and the route invoked (theme `## Status` gate option-b) should be consciously ratified by integrator/meta-phase, not silently inherited. Handled per dispatch: applied the promotion (Changes 5a-5d) as a deliberate, FLAGGED decision AND promoted the ratification OQ routed to cycle-015 meta-phase. Did NOT swallow it; did NOT block on it. The repairer had already bumped the ksp.hpp citations :39→:41 and :62→:64 in CYCLE.md during the repair pass; those corrected values are what landed in the artifact (Change 1). Embedded cycle-012 audit YAML left as-is (historical record; resolution-marker filed as the second OQ). Deferred integrated_at to finalize per role-spec.

---

## 2026-05-28T143548Z-harvester-l1-divfree-projector-promotion
applied_at: 2026-05-28T160000Z
applied_by: integrator-per-report
status: applied

Status adjudicated: **partly-constructive** (NOT the harvester's argued `firm`).
Reasoning: the idempotence law `P∘P=P` and the divergence-free output characterization both DEPEND on the unverified `WeakDiv ≈ Gᵀ M` sign reading — and that sign lives in the MFEM-vendored `MixedVectorWeakDivergenceIntegrator` (`divfree.cpp:113`), below the L0 scope boundary, NOT confirmed from a positive Palace source site (the report's own Evidence + OQ say so). Per the cycle-012-codified `partly-constructive` invariant, a load-bearing sub-law contingent on an unresolved *reading* (rather than a positive source confirmation) is `partly-constructive`. Dispatch directed leaning `partly-constructive` unless the report shows the sign is positively confirmed — it does not. Structure IS fully read (the firm half); the sign-contingent idempotence sub-law is the named partly-constructive sub-part. Constructive sub-part = idempotence law (+ divergence-free characterization); negative anchor = no positive Palace site exhibits the WeakDiv sign (only the integrator internals + the three-way `:177` "subtract" / additive `+1.0` / class-doc divergence-free comment tension); promotion condition = `divfree-weakdiv-sign-convention-l0-verify` resolved via verify-citation-range on `MixedVectorWeakDivergenceIntegrator`, folded into the future L1>L0 lowering-verifier audit.

Files touched:
- book/src/L1/divfree-projector.md (Write — new firm-structure L1 operator entry; `## Status` authored as `partly-constructive` with named sub-part + negative anchor + promotion condition; carries repaired citations and the `:177` contradiction anchor + idempotence sign-OQ caveat from the repair pass)
- book/src/L1/index.md (edit — appended `divfree-projector` dep-map row after the `chebyshev-smoother` row (line 73); status cell = `partly-constructive` with sign-OQ promotion note. OLD string matched verbatim)
- scaffolding/open-questions.md (append — 3 OQ sections; see below)

Gate hits:
- citation-format-sanity: 0 (all changed ranges plain-text `path:start-end`; the divfree-projector entry's citations are the repaired/drift-corrected values the repairer landed in CYCLE.md — `:113`, `:117`, `:119`, `:111-116`, `:140-142`/`:141`, `:177-186`/`:180-181`/`:185`; applied as-repaired)
- index-edit-OLD-string-match: 0 (chebyshev-smoother row anchor matched verbatim pre-apply)
- retroactive-budget-per-slice: 0
- forward-edge-without-surface: 0 (the L1>L0 theme is flagged as deferred/future, not claimed as existing surface)
- concept_writes-on-existing-slug: 0 (new L1 slug, not a concept)
- variant-axis-missing: 0 (VecType {Vector,ComplexVector} + in-place/out-of-place axes both covered)
- summary-md-registration: n/a (L1 operator chapters are not individually SUMMARY-registered; consistent with existing L1 cohort — no SUMMARY edit added)
- firm-count-prose-bump: deliberately NOT applied (the harvester deferred the "Firm (10)→(11)" prose to layer-intro-author; AND since the entry is partly-constructive not firm, the "Firm (10)" prose count remains correct — no bump warranted)

Open questions promoted:
- divfree-weakdiv-sign-convention-l0-verify (carried from report; the WeakDiv sign reading the idempotence law + divergence-free output depend on; promotion condition for firm)
- divfree-projector-l1-l0-lowering-verifier-followup (the lowering-verifier audit that resolves the three-way irrotational/subtract/additive contradiction by anchoring the WeakDiv sign; linked to the sign OQ)
- divfree-projector-status-adjudication (integrator's status-adjudication note — partly-constructive reasoning; routed informational to cycle-015 meta-phase as the SECOND live partly-constructive instance, exercising entry-INTO partly-constructive, complementing the eigsolve exit-FROM case)

Build-relevant: yes

Notes: Report META `overall_status: needs-revision`; per accumulate-surface-with-embedded-friction, needs-revision is NOT reject → the diff APPLIES. The single escalated item (repairer Issue 4 `unrepairable`, critic Issue 4 MEDIUM) was the `firm` vs `partly-constructive` status adjudication — explicitly an integrator-level content judgment. Adjudicated `partly-constructive` (see above) and authored the entry's `## Status` + index row accordingly, diverging from the harvester's drafted `firm` Status text (rewrote it to state the structure-firm / sign-contingent-sub-law split + promotion condition). The repairer's mechanical citation-drift fixes (Issue 1) and surgical caveat/cross-link additions (Issues 2-3) were already in CYCLE.md and landed as-repaired. No book rebuild / commit (finalize). Deferred integrated_at + integration_commit to finalize per role-spec.

---

## 2026-05-28T143923Z-harvester-l3-l4-chebyshev-rows-eligible
applied_at: 2026-05-28T161500Z
applied_by: integrator-per-report
status: applied

Statuses landed: **L3 `partial-obstruction`** (`book/src/L3/chebyshev.md`) + **L4 `rough-in`** (`book/src/L4/chebyshev.md`). The L4 entry landed as `rough-in` per the repairer's downgrade (firm at the body, rough-in at the wrapper) — the `forM_`/`foldM` iteration combinators are un-anchored at L4 and compete with the firm `iterate-while` family; applied with the repaired `rough-in` status + wrapper caveat, NOT the harvester's drafted `firm`. The L3 entry's `partial-obstruction` (body lifts, loops don't; non-adjacent L3↔L1 identity annotated in-line, NO `L3-L1/` or `L3-L2/` directory) landed as authored. Per accumulate-with-embedded-friction, the rough-in L4 entry lands now with the OQ-6 friction embedded.

Files touched:
- book/src/L3/chebyshev.md (Write — new `partial-obstruction` L3 operator entry; in-line non-adjacent-identity annotation per cycle-012 `l3-l1-inline-identity-rotation-convention`, no lowering directory created)
- book/src/L4/chebyshev.md (Write — new `rough-in` L4 typed-wrapper entry; carries the repairer's `## Status` rough-in downgrade + wrapper caveat as landed in CYCLE.md)
- book/src/L3/index.md (edit — appended `chebyshev` dep-map row after the `scal` row (last dep-map row, the report's "line 28" anchor verified correct by the repairer); appended one Working-Notes bullet after the cycle-011 BLAS-1-cohort-closed bullet (last bullet). Both OLD strings matched verbatim)
- book/src/L4/index.md (edit — appended `chebyshev` dep-map row after the `iterate-while-with-prev` row (last dep-map row); added a NEW "Rough-in at L4 (1)" vocabulary-cohort sub-section per the repairer note — chebyshev NOT added to "Firm at L4" and the "Firm at L4 (3)" count NOT bumped. Both OLD strings matched verbatim)
- book/src/SUMMARY.md (edit — registered `- [chebyshev](./L4/chebyshev.md)` at end of L4 Part + `- [chebyshev](./L3/chebyshev.md)` at end of L3 Part; SUMMARY auto-fix safety-net — report proposed the entries but delegated positions to integrator)
- scaffolding/open-questions.md (append — 5 OQ sections; see below)

Gate hits:
- citation-format-sanity: 0 (all changed ranges plain-text `path:start-end`; the chebyshev entries' citations are the codemap-verified ranges the critic confirmed in-range — `chebyshev.cpp:191-220`/`:261-293`, `chebyshev.hpp:14-23`/`:72-75`/`:80-114`/`:37`, slice `:229-285`/`:287-439`)
- index-edit-OLD-string-match: 0 (L3 `scal` row + Working-Notes last bullet matched; L4 `iterate-while-with-prev` row + cohort bullet matched. The report's "L3/index.md line 28" anchor and "L4/index.md line 51" anchor were both verified correct by the repairer — critic's stale-line flags (Issues 3) were the off-by-one, not the report)
- summary-md-registration: applied-discretionarily (SUMMARY auto-fix — both new chapters registered under their Parts; existing-pattern-preservation: L3/L4 operator chapters ARE individually SUMMARY-registered, unlike L1; the report proposed the entries and delegated exact positions)
- H1-reuses-page-heading: 0 (both entries' H1 is `# chebyshev`, matching the operator slug, consistent with sibling L3/L4 entries — not a page-heading reuse)
- variant-axis-missing: 0 (polynomial-kind + element-type both enumerated at both layers; critic variant-axis-coverage pass)
- forward-edge-without-surface: 0 (the in-line L4>L3 / L3>L2 / L3>L1 identity annotations cite existing adjacent-edge themes / entries; no `L3-L1/`/`L3-L2/`/`L4-L3/chebyshev` surface claimed — all flagged as deferred OQ follow-ups)
- retroactive-budget-per-slice: 0
- concept_writes-on-existing-slug: 0 (two new L_n operator slugs, no concept pages authored)

Open questions promoted:
- chebyshev-l4-wrapper-iteration-vocabulary-reconcile (OQ 6, REPAIRER-OPENED — the forM_/foldM → iterate-while re-anchor; routed to combinator-miner/lifter; this is the FIRMING CONDITION for the L4 chebyshev entry: rough-in → firm on reconciliation)
- chebyshev-l4-l3-dedicated-theme-file (OQ 1 — optional thin L4-L3 theme audit anchor; lowering-verifier; low priority)
- chebyshev-phase1-slice-reduction (OQ 2 — slice `book/src/spec/slices/chebyshev.md` now fully lifted; same-layer-cross-cutter reduction audit + concept-extension preservation note)
- partial-obstruction-status-codification (OQ 3 — methodology note: codify `partial-obstruction` as first-class status; cycle-015 meta-phase)
- chebyshev-l3-l4-layer-intro-refresh (OQ 4 — layer-intro-author narrative refresh for the L3/L4 index intros)
- (OQ 5 NOT promoted — the complex-transpose-dead-code caveat is explicitly "already an Open Question on the slice and L1 entry; not newly opened" per the report)

Build-relevant: yes

Notes: Report META `overall_status: needs-revision`; per accumulate-surface-with-embedded-friction, needs-revision is NOT reject → the diff APPLIES. The escalation (critic Issue 1 MEDIUM rotation-quality/cross-ref + Issue 2 plan-kind; repairer `unrepairable` core + `repaired` status-downgrade half) is the L4 wrapper-vocabulary reconciliation: the repairer already downgraded the L4 entry `firm` → `rough-in` IN CYCLE.md (the `## Status` text, the index dep-map row, and the cohort-list instruction all carried the downgrade), so I applied the entries AS-REPAIRED — no further status adjudication needed (unlike the divfree-projector report two rows up, where the integrator had to adjudicate). The substantive re-anchoring (re-express forM_/foldM via iterate_while_pure / iterate-while-with-prev with step-count predicates, OR anchor them as firm L4 rows) is the combinator-miner/lifter follow-up (OQ 6, promoted) — the firming condition that flips the L4 entry rough-in → firm and moves it into the "Firm at L4" cohort (count 3 → 4). Apply hiccups: none — both index OLD-string anchors matched verbatim (the report's line numbers were correct; the critic's line-28/line-51 stale-flags were the repairer-confirmed off-by-one). Followed the repairer note exactly on the L4 cohort: added a "Rough-in at L4 (1)" sub-section rather than touching "Firm at L4 (3)". Deferred integrated_at + integration_commit to finalize per role-spec. follow_up_agent in META is `combinator-miner` — finalize should route OQ 6 accordingly.

---

## 2026-05-28T0910Z-layer-intro-author-plane-rotation-concept-page-canonical-pointer-repoint
applied_at: 2026-05-28T163000Z
applied_by: integrator-per-report
status: applied

Three surgical concept-page canonical-pointer repoints — re-pointing the now-reduced `../spec/slices/orthog.md` plane-rotation sub-slice references to the surviving canonical `../spec/slices/plane_rotation_stream.md`. All three OLD strings matched the artifact byte-exact pre-apply (critic + integrator both confirmed). Closes OQ `plane-rotation-concept-page-canonical-pointer-repoint`.

Files touched:
- book/src/concepts/plane-rotation-stream.md (edit — line 37 "Used in": `orthog` "primary dissection" → `plane_rotation_stream` "primary (canonical) dissection"; the `gmres` consumer line below was carried unchanged in the same block)
- book/src/concepts/givens_generate.md (edit — line 27 "Used in": `orthog` → `plane_rotation_stream`; prose unchanged)
- book/src/concepts/givens_apply.md (edit — line 27 "Used in": `orthog` → `plane_rotation_stream`; prose unchanged)
- scaffolding/open-questions.md (append — 2 OQ sections; see below)

Gate hits:
- old-string-byte-exact-match: 0 (all 3 OLD strings matched verbatim at the cited lines pre-apply)
- citation-format-sanity: 0 (markdown link targets, relative paths; no `path:start-end` claim ranges altered)
- concept_writes-on-existing-slug: 0 (these are section_appends/in-place repoints on existing concept pages, not new concept-slug creation)
- summary-md-registration: n/a (no new pages created; all three are existing SUMMARY-registered concept pages — no SUMMARY edit)
- retroactive-budget-per-slice: 0
- forward-edge-without-surface: 0

Open questions promoted:
- dependency-map-orthog-plane-rotation-stale-edge-prune (the deferred 4th candidate — mermaid concept-DAG edge `dependency-map.md:188` `orthog --> plane-rotation-stream`, stale-in-spirit post-reduction; repairer judged it a concept-node graph arrow NOT a file pointer, so NOT repointed here — routed to a dependency-map-maintenance pass)
- plane-rotation-givens-l0-citation-range-reconcile (the separate dispatch-flagged OQ — `givens_*.md:23` cite `gmres.cpp` for the plane-rotation primitives but firm pages cite `iterative.cpp`; likely-stale file move; needs verify-citation-range, NOT a slice-pointer swap)

Build-relevant: yes

Notes: Pure pointer-hygiene maintenance downstream of cycle-012's phase-1 corpus-reduction batch-3 (the `orthog.md` plane-rotation sub-slice was reduced to a stub pointing at `plane_rotation_stream.md`). Per dispatch: applied EXACTLY the three file-pointer repoints; did NOT repoint the 4th candidate (`dependency-map.md:188`) — the repairer correctly classified it as a bare-node mermaid concept-DAG arrow (resolving it is a graph-modeling decision: delete vs. re-source, e.g. `gmres --> plane-rotation-stream`), exceeds surgical-repoint scope, promoted as OQ instead. The canonical node's own out-edges (`dependency-map.md:165/186/187/194/248`) were confirmed already-correct by the report. No new pages → no SUMMARY edit. No book rebuild / commit / roadmap / log / cycle-record (finalize). Deferred integrated_at + integration_commit to finalize per role-spec.

---

## 2026-05-28T0915Z-same-layer-cross-cutter-phase-1-corpus-reduction-batch-4-remaining-slices
applied_at: 2026-05-28T164500Z
applied_by: integrator-per-report
status: applied

The final 2 unreduced Phase-1 slices — **annotated-reduced, NOT removed** (both retain load-bearing material). Verdicts landed as authored/repaired: `cg_preconditioning_framework.md` = `partially-absorbed` (stub-and-pointer header, §L0/§L1 absorbed by firm `L1/ksp_solve` + L0 anchors + 9 concept pages; §L4/§L4-v0.2/§L4-v0.3 RETAINED verbatim as sole-source load-bearing material); `sparse_triangular_solve.md` = `not-yet-eligible` / permanent-retain (negative-result-slice annotation, canonical instance of `scope-out-obstruction` + `sequential-obstruction`'s out-of-scope sub-kind). Applied the repaired blocks: Change 2's family-attribution wording is the SOFTENED one-directional form ("in the spirit of `concepts/negative-result-slice.md`; that concept page does not yet list this slice") per repairer I1 fix, and the §"Observation kind" relabel (I2) is a CYCLE.md-only label change with no artifact effect.

Files touched:
- book/src/spec/slices/cg_preconditioning_framework.md (edit — prepend reduction-status stub-and-pointer blockquote after H1, before `## Context`; body 3–533 retained in full, NO section deleted; added a section-relative-line-numbers caveat note)
- book/src/spec/slices/sparse_triangular_solve.md (edit — prepend reduction-status negative-result annotation blockquote after H1, before `## Context`; body retained verbatim, NO section deleted)
- scaffolding/open-questions.md (append — 2 OQ sections; see below)

Gate hits:
- old-string-anchor-match: 0 (both H1+blank+`## Context` anchors matched byte-exact pre-apply; START anchors `# cg_preconditioning_framework` / `# sparse_triangular_solve` unique per the audit's `grep -c`=1; END boundaries `## Context` verified)
- unique-text-anchor-preservation: 0 (both reductions are header-prepends with zero section deletion — all H1/H2/H3 headings + slice filenames survive, so the ~10 inbound concept-page citations that reference by path + prose section label remain resolvable; scrutiny point (d) satisfied)
- citation-format-sanity: 0 (the stub blockquotes carry plain-text `path:start-end` / `concepts/<page>.md:NN` references; markdown link targets relative-pathed; no claim-range alterations)
- concept_writes-on-existing-slug: 0 (slice-surface header prepends, not concept-slug creation; the I1 repair deliberately did NOT author an Examples row into `negative-result-slice.md` — deferred as OQ)
- summary-md-registration: n/a (no new chapters; both slices already exist under `spec/slices/`, SUMMARY unchanged)
- retroactive-budget-per-slice: 0
- forward-edge-without-surface: 0 (the `L4/preconditioning-framework` removal-unblock lift is flagged as a future/deferred OQ candidate, NOT claimed as existing surface)

Open questions promoted:
- l4-preconditioning-framework-promotion (the future firm `L4/preconditioning-framework` or `L4/ksp-solve` lift that would transcribe §L4/§L4-v0.2/§L4-v0.3 and let the ~10 concept-page citations re-point — the condition that makes `cg_preconditioning_framework` REMOVABLE, not just stub-reduced; routed to harvester)
- negative-result-slice-examples-reciprocal-membership (the one-directional family-attribution note: `negative-result-slice.md:46` §"Examples in this spec" lists only `polynomial_recurrence_step`, not `sparse_triangular_solve`; optional reciprocal Examples-row append; routed to layer-intro-author / same-layer-cross-cutter — the load-bearing reciprocal citations DO hold so the verdict stands)

Build-relevant: yes

Notes: **CORPUS METRIC FRAMING FOR FINALIZE (load-bearing — record carefully):** with this batch the corpus reaches **10/10 annotated-reduced** (every Phase-1 slice now carries a reduction-status header) — that milestone IS complete. But **annotated-reduced ≠ removed**: these final 2 slices both RETAIN load-bearing material and are NOT removed/removable this cycle. Of the 10 slices, **8 are removed-equivalent** (fully absorbed → stub, prior batches 1–3) and **2 are annotated-and-retained** (this batch: 1 reducible-but-not-removable pending the `L4/preconditioning-framework` lift, 1 permanent negative-result retain). The roadmap should read "annotated-reduction 10/10 COMPLETE; removals at 8/10, 2 retained (1 pending firm-L4 lift via OQ `l4-preconditioning-framework-promotion`, 1 permanent negative-result artifact)" — do NOT record "corpus shrinks to 8 files this cycle" or "10/10 removed." Report META `overall_status: ready` (clean — both repairs were surgical CYCLE.md wording fixes within repair authority; no body authored, no artifact pre-mutated). Applied the repaired Change-2 wording (softened family attribution) and ignored the I2 observation-kind relabel (CYCLE.md-internal label only, no proposed-change effect). No book rebuild / commit / roadmap / log / cycle-record (finalize). Deferred integrated_at + integration_commit to finalize per role-spec.

---

## 2026-05-28T0915Z-abstractor-orthogonalize-mutation-rotation-l1-l0-theme
applied_at: 2026-05-28T170000Z
applied_by: integrator-per-report
status: applied

New firm/structural L1>L0 theme `orthogonalize-mutation-rotation` landed cleanly: the 3 L0 variant loop-structures (MGS single interleaved / CGS split two-phase / CGS2 doubled two-phase) with the repaired `orthog.hpp` citations as-landed in CYCLE.md (`H[j] += dH[j]` accumulate at `:85`, `int`-signedness loop at `:78`, CGS2 `if (refine)` block `:75-88`, CGS body `:57-74`). The position-11 concept-audit report's downstream link target is now in place.

Files touched:
- book/src/L1-L0/orthogonalize-mutation-rotation.md (Write — new firm/structural theme; carries the repairer's 4 codemap-corrected citations: `:85`, `:78`, `:75-88`, `:57-74`. The 2 critic-flagged drifts the repairer confirmed already-codemap-correct (`:48` comment, `:41-53` MGS range) landed unchanged per the repair "Not repaired (already codemap-correct)" verdict)
- book/src/L1-L0/index.md (edit — appended `orthogonalize-mutation-rotation` theme-table row after the `eigsolve-mutation-rotation` row, before the `minres-iteration`/`bicgstab-iteration` obstruction rows — firm themes grouped above obstructions; status cell `firm *(structural; 3 variant loop-structures)*`. OLD string matched verbatim)
- book/src/SUMMARY.md (edit — registered `- [orthogonalize-mutation-rotation](./L1-L0/orthogonalize-mutation-rotation.md)` under the `# L1 > L0` Part after the `eigsolve-mutation-rotation` entry, before `bicgstab-iteration` — matching the index ordering. The report PROPOSED this exact SUMMARY entry; applied as proposed. OLD string matched verbatim)
- scaffolding/open-questions.md (append — 3 OQ sections; see below)

Gate hits:
- citation-format-sanity: 0 (all changed ranges plain-text `path:start-end`; the 4 repaired `orthog.hpp` pointers are the repairer's codemap-ground-truth values landed in CYCLE.md — applied as-repaired; non-`orthog.hpp` pointers were critic-verified clean)
- old-string-anchor-match: 0 (index `eigsolve-mutation-rotation`+`minres-iteration` anchor matched byte-exact; SUMMARY `eigsolve-mutation-rotation`+`bicgstab-iteration` anchor matched byte-exact)
- summary-md-registration: applied-as-proposed (the report's CYCLE.md proposed the SUMMARY entry explicitly; not an auto-fix discretionary add — placed at integrator-chosen position per critic Issue 8 note that the edit block carried no positional anchor. No orphaned chapter: the new L1-L0 chapter IS now SUMMARY-registered)
- forward-edge-without-surface: 0 (the theme grounds every L0 form in a positive source site; the single L2 `krylov-step` mention is framed as a downstream-consumer note, not an existing-surface claim — flagged as deferred OQ)
- concept_writes-on-existing-slug: 0 (new L1-L0 theme slug; no concept page authored)
- variant-axis-missing: 0 (MGS/CGS/CGS2 axis exhaustive against the firm L1 `orthogonalize` operator; collective-shape m×1/1×m/2×m read off the bodies; critic variant-axis-coverage pass — the report's strong point)
- retroactive-budget-per-slice: 0
- H1-reuses-page-heading: 0 (H1 `# orthogonalize-mutation-rotation` matches the theme slug, consistent with sibling `*-mutation-rotation` themes)

Open questions promoted:
- orthogonalize-mutation-rotation-lowering-verifier-audit (abstractor OQ items 4–5 — exhaustiveness of the L0 corpus scan + B-weighted inner-product-hook loop-structure invariance; routed to lowering-verifier)
- orthogonalize-mutation-rotation-l2-krylov-step-lift-notes (abstractor OQ items 1–3 — the 2 reverse-direction L0→L1 lift notes quarantined per high→low discipline (`m` j/j+1 off-by-one; CGS2 `dH` scratch mention-and-erase) + the naming-parallel tracking note; routed to lifter for a downstream L2 krylov-step consumer)

Build-relevant: yes

Notes: Report META `overall_status: ready` (clean — repairer's fixes were all mechanical citation-line-offset corrections within repair authority; no body authored, no artifact pre-mutated). Applied AS-REPAIRED — the corrected `orthog.hpp` line numbers (`:85`, `:78`, `:75-88`, `:57-74`) are the repairer's codemap-ground-truth values that the repairer confirmed came out ONE HIGHER than the critic's candidate-fix numbers; landed the repairer's values. The repairer's "Not repaired (already codemap-correct)" verdict on Issues 3 (`:48` comment) and 4 (`:41-53` MGS range) means those stayed at the report's original values — confirmed correct against the codemap, so the critic's drive-by about a divergence from the upstream L1 entry `book/src/L1/orthogonalize.md` is MOOT (both entries cite `:48`/`:41-53` and the codemap confirms both correct; no upstream off-by-one fix needed). **DOWNSTREAM-LINK CONFIRMATION (load-bearing for finalize + position 11): the link target `book/src/L1-L0/orthogonalize-mutation-rotation.md` is now in place AND SUMMARY-registered — the position-11 concept-audit report's link to this theme will resolve.** No book rebuild / commit / roadmap / log / cycle-record (finalize). Deferred integrated_at + integration_commit to finalize per role-spec.

---

## 2026-05-28T144719Z-abstractor-chebyshev-l1-l0-and-l2-l1-lowering-themes
applied_at: 2026-05-28T173000Z
applied_by: integrator-per-report
status: applied

Two firm chebyshev lowering themes landed cleanly. (1) L1>L0 `chebyshev-smoother-mutation-rotation` — firm/structural with an algebraic transpose-alias sub-rule (sub-pattern C). (2) L2>L1 `chebyshev-iteration-fusion` — firm/algebraic recurrence↔polynomial fusion; **the FIRST real chapter under the previously-empty `book/src/L2-L1/` Part**. Both carry the repairer's tightened element-kernel citations (`:68-78` ApplyOrder0, `:112-123` ApplyOrderK) as-landed in CYCLE.md.

Files touched:
- book/src/L1-L0/chebyshev-smoother-mutation-rotation.md (Write — new firm L1>L0 theme; 4 sub-patterns A/B/C/D)
- book/src/L2-L1/chebyshev-iteration-fusion.md (Write — new firm L2>L1 fusion theme; first chapter under the L2-L1 Part)
- book/src/L1-L0/index.md (edit — appended `chebyshev-smoother-mutation-rotation` theme-table row directly after the `eigsolve-mutation-rotation` row, preserving the position-6 `orthogonalize-mutation-rotation` row that now intervenes before the obstruction rows; firm themes grouped above obstructions. OLD string matched verbatim — anchored on eigsolve+orthogonalize row pair to absorb the in-cycle position-6 landing)
- book/src/L2-L1/index.md (edit — REPLACED the Phase-B placeholder fence (` ``` ` / `(empty — Phase B skeleton.)` / ` ``` `) between `## Theme list` and `## Working Notes` with the `## Theme list` table carrying the single `chebyshev-iteration-fusion` row, per the repairer integrator-note. Placeholder displaced, NOT appended-below — rendered page shows only the table)
- book/src/SUMMARY.md (edit — 2 registrations: `- [chebyshev-smoother-mutation-rotation](./L1-L0/chebyshev-smoother-mutation-rotation.md)` after the `minres-iteration` row at end of the `# L1 > L0` Part per the repairer anchor; `- [chebyshev-iteration-fusion](./L2-L1/chebyshev-iteration-fusion.md)` after the `Overview` row under the `# L2 > L1 — Lowering` Part header. Both OLD strings matched verbatim against the freshly-read SUMMARY — which already carried the position-3 L3/L4 chebyshev rows and the position-6 orthogonalize-mutation-rotation row)
- scaffolding/open-questions.md (append — 2 OQ sections; see below)

Gate hits:
- old-string-anchor-match: 0 (L1-L0 index eigsolve+orthogonalize anchor matched; L2-L1 index placeholder fence matched byte-exact; SUMMARY minres-iteration anchor + L2-L1 Part-header+Overview anchor both matched verbatim against fresh read)
- index-placeholder-displacement-on-first-firm-row: applied-discretionarily (the L2-L1 `## Theme list` carried a fenced `(empty — Phase B skeleton.)` placeholder; the repairer explicitly directed REPLACEMENT not append, and this is the first-firm-row-displaces-placeholder gate — replaced the placeholder fence with the firm theme table. Rationale: first-firm-row-displaces-placeholder; friction-ledger index-placeholder-displacement-on-first-firm-row. NOTE: this placeholder was a fenced code block, not the literal bare `(empty — Phase B skeleton.)` line the cycle-006 precedent describes; semantically identical displacement)
- L2-L1-part-wiring: 0 (the `# L2 > L1 — Lowering` Part header ALREADY existed in SUMMARY.md (line 40) with its `Overview`/index.md row (line 41) — NOT a missing/placeholder Part; the index.md file already existed with full Context/Theme-list/Working-Notes structure. So no new Part header or index file needed — only the first chapter row added to SUMMARY + the theme table populated in index.md. `cargo make book` Part wiring is sound: Overview + 1 chapter, both files present)
- summary-md-registration: applied (both new chapters registered; L1-L0 + L2-L1 lowering chapters ARE individually SUMMARY-registered per existing pattern; the report+repairer PROPOSED both exact SUMMARY entries — applied as-proposed at the repairer-anchored positions, not an auto-fix discretionary add)
- citation-format-sanity: 0 (all changed ranges plain-text `path:start-end`; the element-kernel citations are the repairer's codemap-tightened `:68-78`/`:112-123` values landed in CYCLE.md — applied as-repaired; all other ranges critic-verified in-range)
- forward-edge-without-surface: 0 (the L1>L0 theme cites the sibling `chebyshev-iteration-fusion` for de-fusion — now in place this cycle; the L2>L1 theme's L3-obstruction mention is framed as downward context citing the position-3 L3/chebyshev row + sequential-obstruction concept, not a claimed surface)
- variant-axis-missing: 0 (polynomial-kind 4th/1st + element-type real/complex both covered via applicability conditions at both themes; critic variant-axis-coverage pass — upstream operator slices carry the granular blocks)
- H1-reuses-page-heading: 0 (both H1s match their theme slugs — `# chebyshev-smoother-mutation-rotation`, `# chebyshev-iteration-fusion` — consistent with sibling lowering themes)
- plan-kind-consistency: 0 (both `firm`; the `MFEM_VERIFY(lambda_max > 0.0)` guard correctly classified as a POSITIVE setup-time precondition site, NOT a partly-constructive negative-anchor reconstruction — distinct from the eigsolve LinearSolveFailed case; critic confirmed)
- retroactive-budget-per-slice: 0
- concept_writes-on-existing-slug: 0 (two new lowering-theme slugs; no concept page authored)

Open questions promoted:
- chebyshev-lowering-themes-lowering-verifier-followup (consolidated standard follow-up for BOTH themes — L1>L0 four-sub-pattern exhaustiveness across both kinds × both element types × consumer forwarding sites; L2>L1 per-degree-step fusion + element-kernel sub-fusion against both Mult2 bodies; routed to lowering-verifier; NOT a status reduction)
- chebyshev-dead-code-complex-transpose-kernels (the `chebyshev.cpp:101-110`/`:150-159` conjugate-dinv transpose kernels, dead code under symmetric MultTranspose2→Mult2 wiring; recognition rules for potential non-symmetric sites; routed to lowering-verifier; mirrors the axpby ComplexVector::Subtract defined-not-used precedent)
- (NOT promoted: `spectrum_estimate` opacity — already tracked in the `matrix-weighted-norm-and-bilinear-form` residual-cohort OQ, treated opaque; MPI single-rank — flag-once-per-scope-policy, not an OQ; the `MFEM_VERIFY` guard + partly-constructive non-applicability — resolution notes, not open questions; the L2>L1 reverse-direction lifting note — working-note quarantine inside the chapter per high→low discipline, not a ledger OQ)

Build-relevant: yes

Notes: Report META `overall_status: ready` (clean — repairer fixes were the SUMMARY-registration adds (Issue 1), the L2-L1 placeholder-replacement integrator-note (Issue 2), and small-offset element-kernel citation tightening (Issue 3); all surgical, within repair authority; no body authored). Applied AS-REPAIRED throughout. **L2-L1 PART WIRING (load-bearing for finalize): the `# L2 > L1 — Lowering` Part was NOT an empty placeholder at the SUMMARY level — the Part header + Overview/index.md row already existed (SUMMARY.md:40-41) and index.md already had a full Context/Theme-list/Working-Notes structure; only the `## Theme list` body carried the fenced `(empty — Phase B skeleton.)` placeholder. So the wiring fix was (a) replace that body placeholder with the firm theme table, (b) register the first chapter row in SUMMARY. The Part is now correctly wired (Overview + 1 chapter, both files present) — `cargo make book` will not break on it.** Re-read SUMMARY.md fresh immediately before both edits per the role-spec; confirmed it already carried the position-3 L3/L4 chebyshev rows + position-6 orthogonalize-mutation-rotation row — both my anchors (minres-iteration row, L2-L1 Part-header+Overview) matched verbatim, no upstream-landing collision. No book rebuild / commit / roadmap / log / cycle-record (finalize). Deferred integrated_at + integration_commit to finalize per role-spec.

---

## 2026-05-28T1447Z-lifter-krylov-step-theme-body-no-l3-row-drift-cycle-013
applied_at: 2026-05-28T175500Z
applied_by: integrator-per-report
status: applied

Two surgical theme-body re-anchors landed cleanly on `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`, striking the two surviving stale cycle-006 "no L3 row promoted / needed" residuals (Context § line 20; OQ-disposition § line 220) and re-anchoring them to the firm `L3/krylov-step.md` (cycle-010 backfill) + the L4>L3>L2>L1 no-skipped-rows chain, per the cycle-009 invariant **Identity-lowerings still require both L levels**. Applied the repaired Re-anchor 1 `[new]` block — the repairer had re-pointed the dangling `cg.md:341-362` pointer in that block to the firm `L3-L2/krylov-step-body-identity.md` (the reduced `cg.md` stub no longer holds that content); `arnoldi_step.md:178-213` kept verbatim (critic-confirmed in-range).

Files touched:
- book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (edit — 2 re-anchor blocks: Context § line 20 + OQ-disposition § line 220; Re-anchor 1 carries the repairer's `cg.md:341-362`→`L3-L2/krylov-step-body-identity` re-point)
- scaffolding/open-questions.md (append — 2 OQ sections; see below)

Gate hits:
- old-string-anchor-match: 0 (both `[old]` blocks matched the on-disk theme byte-exact at lines 20 and 220 pre-apply; the critic's grep confirmed exactly 3 stale "no L3 row" residuals at 20/218/220, with 218 already-correct/SUPERSEDED and untouched, 293 §Status already-correct and untouched)
- citation-format-sanity: 0 (Re-anchor 1's pointer is the repairer's re-anchored `L3-L2/krylov-step-body-identity.md` markdown link + the in-range `arnoldi_step.md:178-213`; applied as-repaired — no dangling citation re-blessed in the new text)
- forward-edge-without-surface: 0 (both re-anchors cite EXISTING firm surface — `L3/krylov-step.md`, `L3-L2/krylov-step-body-identity.md`, both verified-present; no claimed-but-absent surface)
- edge-label-fidelity: 0 (re-anchored prose correctly assigns L4>L3 to this theme and the L3>L2 body-identity hop to the sister theme; "no skipped rows" chain consistent with §Audit line 218 + §Status line 293)
- retroactive-budget-per-slice: 0
- variant-axis-missing: 0 (no variant axes touched — pure vocabulary re-anchor)
- H1-reuses-page-heading: 0 (no headings touched)
- summary-md-registration: n/a (no new chapter — existing theme already SUMMARY-registered)

Open questions promoted:
- krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep (the pre-existing theme-wide dangling `cg.md` pointers at lines 98/109/126/200/204/210/218/231/233 needing a dedicated re-anchor sweep to the firm `L3-L2/krylov-step-body-identity.md` — OUT of this report's narrow line-20/220 scope; ALSO folds in the critic-Issue-2 line-218 "lowers transitively to the L2 entry" relic to be brought into the no-skipped-rows vocabulary; routed to a dedicated citation-re-anchor dispatch)
- krylov-step-l3-identity-in-form-audit-already-answered-note (INFORMATIONAL — the re-anchored OQ slug `krylov-step-l3-identity-in-form-audit` already shows `answered_in: cycle-006` in the ledger; Re-anchor 2 firms its historical "no L3 row needed" disposition tail, NOT a fresh closure — finalize must NOT double-close or re-open it)

Build-relevant: yes

Notes: Report META `overall_status: ready` (clean — the sole substantive finding, Issue 1's dangling `cg.md:341-362` pointer in the report's new text, was mechanically re-anchored by the repairer to the firm `L3-L2/krylov-step-body-identity.md`, which is verified to carry the lifted content; the CYCLE.md I read already showed the repaired Re-anchor 1 `[new]` block, so I applied AS-REPAIRED). Both `[old]` anchors matched verbatim — no apply hiccups. Line 218 (§Audit, with its still-correct SUPERSEDED-cycle-010 framing) and line 293 (§Status) were correctly NOT in this report's edit window and were left untouched; the line-218 transitive relic is captured in the deferred sweep OQ. Per critic Issue 3 / repairer note: the integrator/finalize must treat OQ `krylov-step-l3-identity-in-form-audit` as already-answered (cycle-006) — NO double-close (filed as the informational OQ). Deferred integrated_at + integration_commit to finalize per role-spec.

---

## 2026-05-28T144815Z-layer-intro-author-L0-bundle-6-candidates-discovery-and-ranking
applied_at: 2026-05-28T181500Z
applied_by: integrator-per-report
status: applied

**SAFETY-GATE VERDICT: HOLDS — authored L0 chapter applied.** This was a discovery/ranking dispatch that ALSO authored a full firm-shaped L0 bundle chapter for `linalg-orthog-file` (`palace/linalg/orthog.hpp`, 93-line header-only). Per the repairer's `unrepairable`/informational routing (plan-kind stretch, defensible per critic), I applied the author-content safety net rather than treating block A as a ranking note. Three verification points all passed: (1) **MGS citation valid** — `palace-codemap get_symbol_def OrthogonalizeColumnMGS` → `palace/linalg/orthog.hpp:41-53`, exactly matching the repaired range (39-55→41-53); CGS sibling 57-89 critic-confirmed; (2) **NO collision** — target `book/src/L0/linalg-orthog-file.md` did not exist (clean Write); the position-6 in-cycle `book/src/L1-L0/orthogonalize-mutation-rotation.md` theme is a different file in a different Part (L0 file-overview vs L1>L0 theme), and the MGS range is now consistent (41-53) across both; (3) **SUMMARY (C) `palace/` prefix applies cleanly** — fresh-read line 83 `- [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)` matched the repaired OLD anchor verbatim, and the new `palace/linalg/orthog.hpp` entry carries the `palace/` prefix matching every sibling L0 `File —` entry.

Files touched:
- book/src/L0/linalg-orthog-file.md (Write — new firm L0 file-overview chapter; the authored discovery→authoring-stretch content, safety-gated; carries the repaired MGS range 41-53 as landed in CYCLE.md)
- book/src/L0/index.md (edit — appended `linalg-orthog-file` roster bullet after the `linalg-iterative-file` bullet (line 27), before `linalg-solver-file`. OLD string matched byte-exact)
- book/src/SUMMARY.md (edit — registered `- [File — palace/linalg/orthog.hpp](./L0/linalg-orthog-file.md)` after the `iterative` File entry (line 83), before the `solver` entry, with the repaired `palace/` prefix. OLD string matched byte-exact against fresh read)
- scaffolding/open-questions.md (append — 1 OQ discovery-update section; see below)

Gate hits:
- citation-format-sanity: 0 (all chapter ranges plain-text `path:start-end`; MGS range codemap-confirmed 41-53 at integration time, CGS 57-89 critic-confirmed, all others critic-verified in-range)
- mgs-range-codemap-verify: 0 (PASS — `OrthogonalizeColumnMGS` = orthog.hpp:41-53 per `get_symbol_def`; the repaired 39-55→41-53 is correct and now consistent with the firm `L1/orthogonalize.md` + position-6 theme)
- l0-file-collision-check: 0 (NO collision — new file did not exist; position-6 theme is a different file/Part)
- old-string-anchor-match: 0 (index `linalg-iterative-file`+`linalg-solver-file` anchor + SUMMARY `iterative`+`solver` File-entry anchor both matched byte-exact)
- summary-md-registration: applied-as-proposed (the report+repairer PROPOSED the exact SUMMARY entry with the repaired `palace/` prefix; applied at the repairer-anchored position — not an auto-fix discretionary add; the new L0 chapter IS now SUMMARY-registered, no orphan)
- plan-kind-consistency / discovery-authored-firm-content: 1 (the kind stretch — discovery/ranking dispatch authored a firm L0 chapter; safety-gated as in-scope authored content per the dispatch directive + repairer routing; NOT blocked — defensible, applied on its own merits)
- H1-reuses-page-heading: 0 (H1 `# File — \`palace/linalg/orthog.hpp\`` matches sibling L0 file-overview chapter convention — not a slug/heading reuse)
- variant-axis-missing: 0 (MGS|CGS|CGS2 axis fully enumerated in §"The two variants"; critic variant-axis-coverage pass)
- forward-edge-without-surface: 0 (no L_{n+1}>L_n rotation asserted — L0 source-faithful note; the upward L1 notes are framed as deferred-to-L1, not claimed surface)
- retroactive-budget-per-slice: 0
- concept_writes-on-existing-slug: 0 (new L0 file-overview chapter, no concept page)

Open questions promoted:
- l0-bundle-6-candidates (DISCOVERY UPDATE — partial-answer update to the cycle-009 OQ; #3 `linalg-orthog-file` now LANDED, #2 `linalg-rap-file` is the next ranked bundle-6 candidate for cycle-014+ as a full bundle-author dispatch with the suggested chapter outline + single-rank-reading caveat carried; status held `partially-answered`; appended as a dated discovery-update section before `## Dropped`, NOT editing the existing block at line 1539 per append-only)

Build-relevant: yes

Notes: Report META `overall_status: ready` (clean — both repairs surgical and within repair authority: citation-validity MGS 39-55→41-53 at all three sites, and the SUMMARY block-C `palace/` prefix + `[old]` anchor fix; the CYCLE.md I read already carried both repairs and I applied AS-REPAIRED). The **discovery→authoring safety-gate** was the load-bearing integrator decision this row: a discovery/ranking-scoped dispatch produced a firm-content proposed-changes block; I verified (codemap MGS range + file-non-existence collision check + SUMMARY anchor) and applied the authored chapter as in-scope content, NOT as a mere ranking note, per the dispatch directive and the repairer's `unrepairable` informational routing. Apply hiccups: one — the SUMMARY Edit initially failed because I had not Read SUMMARY.md in this session (only grepped it); re-read offset 78 then applied cleanly. The "L0 chapter count is 18" figure in the report's OQ is an integrator-finalize roadmap housekeeping number (critic Issue 5) — flagged in the promoted OQ for finalize to RE-DERIVE, not trust. No book rebuild / commit / roadmap / log / cycle-record (finalize). Deferred integrated_at + integration_commit to finalize per role-spec.

---

## 2026-05-28T144809Z-lifter-slepc-convergence-reason-lift-sub-theme
applied_at: 2026-05-28T184500Z
applied_by: integrator-per-report
status: applied

New `partly-constructive` sibling sub-theme `eigsolve-convergence-reason-mapping` (the full `EPSConvergedReason -> EigStatus` map) landed cleanly under the eigsolve L1>L0 family, discharging the parent Sub-pattern B forward-pointer. **Settled diverged-row count = 8** (3 EPS diverged + 1 `*_CONVERGED_ITERATING` sentinel + 4 NEP-family diverged; PEP shares EPS's 3 rows non-additively; the 2 converged rows are count-anchored, NOT partly-constructive). Verified both "8" headlines consistent in the landed file (§Summary line 40, §Status). The negative anchor is real and critic-confirmed: Palace only PRINTS the reason (`slepc.cpp:{699,1182,1529}` `*ConvergedReasonView`), with whole-tree ZERO `EPS_DIVERGED_*`/`EPS_CONVERGED_*` references and no `EPSGetConvergedReason` callsite. Constructive sub-part = per-row `EigStatus` assignment; promotion condition = the single global gate downstream of parent Sub-pattern B (Palace reads the reason via `EPSGetConvergedReason` + propagates to outer-loop status). All stated per the cycle-012 partly-constructive invariant.

Files touched:
- book/src/L1-L0/eigsolve-convergence-reason-mapping.md (Write — new `partly-constructive` L1>L0 sibling sub-theme; carries the repaired "8" diverged-row count + the global-coverage promotion-condition sentence as landed in CYCLE.md)
- book/src/L1-L0/eigsolve-mutation-rotation.md (edit — Change 2 parent cross-ref: appended the forward-pointer to the now-authored sibling sub-theme in the Sub-pattern B SLEPc-path paragraph; OLD string matched VERBATIM at lines 332-340 post-position-1 — position-1's Sub-pattern-B-snippet/Status edits landed in a DISJOINT earlier region, confirmed by the blank-line-341 boundary)
- book/src/L1-L0/index.md (edit — Change 3: appended the `eigsolve-convergence-reason-mapping` theme-table row directly after the `eigsolve-mutation-rotation` row (line 22); OLD single-row anchor matched verbatim. The in-cycle chebyshev-smoother (pos-7) + orthogonalize (pos-6) rows that now intervene below it were undisturbed)
- book/src/SUMMARY.md (edit — Change 4 SUMMARY registration: inserted `- [eigsolve-convergence-reason-mapping](./L1-L0/eigsolve-convergence-reason-mapping.md)` directly UNDER the `eigsolve-mutation-rotation` line in the `# L1 > L0 — Lowering` Part. NOTE: the repairer's Change-4 OLD anchor (`eigsolve-mutation-rotation`+`bicgstab-iteration`) was STALE against the freshly-read SUMMARY — position-6 had already inserted `orthogonalize-mutation-rotation` directly after the eigsolve line. Re-anchored on `eigsolve-mutation-rotation`+`orthogonalize-mutation-rotation` (the current adjacency); sibling placed directly under parent, preserving the intended index/SUMMARY ordering)
- scaffolding/open-questions.md (append — 2 OQ sections; see below)

Gate hits:
- partly-constructive-states-subpart-and-promotion-condition: 0 (PASS — §Status names (i) the constructive sub-part = per-row EigStatus assignment, (ii) the negative anchors = whole-tree zero-reference + print-only sites, (iii) the global promotion condition = upstream EPSGetConvergedReason consumption downstream of parent Sub-pattern B; cycle-012 invariant satisfied)
- partly-constructive-count-consistency: 0 (both "8" diverged-row headlines consistent in the landed file — the repairer's recount from "9" to "8" was already in CYCLE.md; applied as-repaired)
- old-string-anchor-match: 1 (SUMMARY Change-4 repairer OLD anchor was stale post-position-6; re-anchored to current adjacency — see Files-touched note. Parent cross-ref + index OLD anchors both matched verbatim)
- parent-cross-ref-disjoint-from-position-1: 0 (VERIFIED — Change-2 OLD at parent lines 332-340 matched byte-exact after position-1's edits; disjoint earlier region confirmed)
- citation-format-sanity: 0 (all changed ranges plain-text `path:start-end`; slepc.cpp print-site citations critic-confirmed exact + in-range)
- forward-edge-without-surface: 0 (the sibling cites EXISTING firm surface — parent eigsolve-mutation-rotation, ksp-solve-mutation-rotation, L1/eigsolve; the materialisation shape is framed as forward-looking, not claimed surface)
- variant-axis-missing: 0 (EPS/PEP/NEP SLEPc-family axis covered with per-family print-site citations; ARPACK/QuasiNewton explicitly scoped out)
- summary-md-registration: applied (the new chapter IS now SUMMARY-registered; report+repairer PROPOSED the entry, applied at re-anchored position — removes the deferred nav break the critic Issue 3 flagged)
- H1-reuses-page-heading: 0 (H1 `# eigsolve-convergence-reason-mapping` matches the sub-theme slug, consistent with sibling lowering themes)
- retroactive-budget-per-slice: 0
- concept_writes-on-existing-slug: 0 (new L1-L0 sub-theme slug; no concept page)

Open questions promoted:
- eigsolve-convergence-reason-mapping-promotion (the single global gate covering all 8 partly-constructive diverged rows — downstream of parent Sub-pattern B's EPSGetConvergedReason gate; lowering-verifier may UNBLOCK without ENACTING; routed to lowering-verifier; linked to the partly-constructive-to-firm-promotion-route-ratification OQ that position-1 routed to cycle-015 meta-phase)
- eigsolve-convergence-reason-mapping-slepc-enum-upstream-confirm (OQ #1 + #4 consolidated — SLEPc enum names documented-not-source-anchored (cross-check against reference/ SLEPc headers) + PEP/NEP isomorphism asserted-not-exhaustively-tabled; routed to lowering-verifier; non-status-changing)
- (NOT promoted: OQ #2 SUMMARY nav — RESOLVED by repairer as Change 4, applied this row; OQ #3 count-vs-reason redundancy — a within-chapter per-row-note observation + a future meta-phase fold-vs-keep judgment (fold the sub-theme back into parent Sub-pattern B once its gate closes vs keep separate for SLEPc-specificity), captured in the chapter, not a ledger question)

Build-relevant: yes

Notes: Report META `overall_status: ready` (clean — all 8 critic checks pass; the 5 findings were 4 mechanical/surgical repairs (count 9->8, global-coverage sentence, SUMMARY Change-4 add, parent line-count 911->910) + 1 integrator-routing awareness note (staging-order). The CYCLE.md I read already carried all repairs; applied AS-REPAIRED). **Position-ordering verification this row (load-bearing):** (a) parent cross-ref Change-2 OLD matched verbatim post-position-1 — disjoint region, no collision; (b) SUMMARY Change-4 repairer OLD anchor was STALE post-position-6 (orthogonalize-mutation-rotation now intervenes where the repairer expected bicgstab-iteration) — re-anchored to the current adjacency and placed the sibling directly under the parent, preserving the intended ordering and removing the deferred build break. No book rebuild / commit / roadmap / log / cycle-record (finalize). Deferred integrated_at + integration_commit to finalize per role-spec.

---

## 2026-05-28T1447Z-same-layer-cross-cutter-concepts-orthogonalization-coefficient-normalisation-drift
applied_at: 2026-05-28T191500Z
applied_by: integrator-per-report
status: applied

Full-file rewrite of `book/src/concepts/orthogonalization.md` landed cleanly (position 11 of 11, final per-report). The page is realigned to the firm `L1/orthogonalize` "does not normalize output" contract: the three mutually-inconsistent coefficient lengths (`j+2` / `j+1` / `j`) collapse to the one correct length-`m` convention, the duplicate second concept block (old lines 26-63, with its "`w` may be mutated; `h_coeffs` is a length-`j`" L0-leak signature) is removed, the line-3 `h_{j+1}=‖w'‖` fold-in becomes the caller's separate `nrm2` step, and the stale "separate slice" / "dedicated `orthog` slice would carry" pre-layered framing is replaced with an authoritative-definition blockquote pointing at `L1/orthogonalize` + the forward lowering `L1-L0/orthogonalize-mutation-rotation`. **DOWNSTREAM-LINK CONFIRMATION (load-bearing — the dispatch's central ordering hazard): the 3 links to `../L1-L0/orthogonalize-mutation-rotation.md` (intro blockquote + Variants § + L1>L0 placement bullet) now RESOLVE — position-6 (`2026-05-28T0915Z-abstractor-orthogonalize-mutation-rotation-l1-l0-theme`) created `book/src/L1-L0/orthogonalize-mutation-rotation.md` earlier this cycle (ls-confirmed present, 14959 bytes). The serial-apply ordering the META prescribed was honoured by the parent dispatch sequence.** The repaired citation anchor (`orthogonalize.md:175-178` → `:14-16, 54-55, 264-267`) lives in the report's prose finding, NOT in the proposed-changes block, so no separate artifact edit was needed for it.

Files touched:
- book/src/concepts/orthogonalization.md (Write — full-file rewrite of the existing concept page; single coherent block aligned to the firm L1 contract)
- scaffolding/open-questions.md (append — 3 OQ sections: 1 closure-confirmation + 2 new forward-looking caveats; see below)

Gate hits:
- old-string / full-file-content-match: 0 (the existing on-disk page matched the report's described drift verbatim — line-3 normalisation conflation, duplicate block lines 26-63, "separate slice" framing at lines 19/23 — confirming the rewrite targets the right pre-state; applied as a full-content Write after Read)
- forward-edge-without-surface: 0 (PASS — the 3 `../L1-L0/orthogonalize-mutation-rotation.md` links cite EXISTING firm surface created by position-6 this cycle; the dispatch's central verification, ls-confirmed present)
- cross-reference-integrity: 0 (ALL link targets ls-confirmed present: L1/orthogonalize.md, L1/dot.md, L1/axpy.md, L2/krylov-step.md, L1-L0/orthogonalize-mutation-rotation.md, concepts/sequential-obstruction.md, concepts/variant-absorption.md, spec/slices/orthog.md, spec/slices/gmres.md — the warning the critic flagged on the not-yet-landed theme is now MOOT, the file exists)
- concept_writes-on-existing-slug: 0 (this IS an existing concept slug `orthogonalization`, but the operation is a full-page REFRESH/rewrite of existing content — NOT a new-slug concept_writes — so the auto-rewrite-to-section_appends gate does NOT fire; consistent with the layer-intro-author concept-refresh precedent)
- summary-md-registration: n/a (`concepts/orthogonalization.md` is an EXISTING SUMMARY-registered concept page — no new chapter, no SUMMARY edit)
- H1-reuses-page-heading: 0 (H1 `# concept: orthogonalization` matches the existing concept-page H1 convention — unchanged)
- variant-axis-missing: 0 (MGS/CGS/CGS2 axis exhaustive + the second `dot_op` B-weighted inner-product-hook axis called out citing romoperator.cpp:51-66; critic variant-axis-coverage pass)
- citation-format-sanity: 0 (all ranges plain-text `path:start-end`; the Arnoldi call-site range `iterative.cpp:629-632, 808-811` intentionally wider than the firm L1 entry's `:630, 809` to include the following nrm2/scal — critic-confirmed consistent in substance, cosmetic-only)
- plan-kind-consistency / cross-cutter-emitting-concept-rewrite: 1 (the kind stretch — a same-layer-cross-cutter emitted a ~100-line full concept-page rewrite, which is layer-intro-author territory per the write-authority partition. RESOLVED by APPLYING DIRECTLY per the dispatch directive: the content is sound, self-disclosed, enacts no unification, adds no new operator/theme, and defers all mechanics to the L1 entry + the wave-1 theme. Routing-via-layer-intro-author would produce identical content — applied as-is rather than re-routing. NOT blocked)
- retroactive-budget-per-slice: 0

Open questions promoted:
- concepts-orthogonalization-coefficient-normalisation-drift (CLOSURE CONFIRMATION — the cycle-012 harvester-opened drift OQ at ledger lines ~2159-2167; this rewrite resolves every flagged drift point + discharges the L1 entry's own pre-flag at orthogonalize.md:331-335; status flips open→answered as a dated append, the original open block left in place per append-only — finalize reconciles the header field)
- concepts-orthogonalization-spec-slices-link-survival (NEW — the refreshed page links `../spec/slices/orthog.md` for the retained L2/L3/L4 unfolding; keep the path-level anchor alive if that partially-reduced slice is later stub-reduced; routed to future phase-1-slice-reduction-audit; report caveat item 3)
- concepts-sequential-obstruction-variant-absorption-drift-spot-check (NEW — the two sibling concept pages referenced by the firm L1 entry + this refreshed page were NOT audited for parallel drift; a future same-layer-cross-cutter spot-check; folds into the broader pre-layered-era concept-contamination sweep at ledger lines ~335/379; report caveat item 4)

Build-relevant: yes

Notes: Report META `overall_status: ready` (the cross-reference-integrity + plan-kind-consistency + skill-uptake-survey warnings were all `repaired`/acknowledged — the dangling-link warning was a staging-order directive (honoured: position-6 landed before this position-11), the kind-shape warning a routing question (resolved: apply-direct), the citation-anchor fix mechanical (already in CYCLE.md prose), and the skill-uptake-survey pure telemetry). **THE CENTRAL DISPATCH VERIFICATION — the 3 links to `../L1-L0/orthogonalize-mutation-rotation.md` RESOLVE: position-6 created that file this cycle (ls-confirmed, present). No dangling link; `cargo make book` at finalize will not break on it.** Applied the rewrite via Write (existing-file full-replace after Read). Caveats 1 (layer-intro-author authority) and 2 (verify cross-ref targets) were now-resolved routing/ordering notes — NOT promoted as OQs (caveat-1 resolved by apply-direct decision; caveat-2 resolved by the ls-confirmation). Caveats 3 and 4 are genuine forward-looking follow-ups — promoted. Apply hiccups: none — the on-disk page matched the report's described drift pre-state exactly, and every link target ls-confirmed present. No book rebuild / commit / roadmap / log / cycle-record (finalize). Deferred integrated_at + integration_commit to finalize per role-spec. This is position 11 of 11 — the staging log is now complete for integrator-finalize.

---
