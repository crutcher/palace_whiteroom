# cycle-035 integrator staging log

Append-only. Per-report integrators add a row after applying their report.
integrator-finalize reads this log to reconcile the cycle.

---

## 2026-05-31T141500Z-lifter-chebyshev-cite-tighten
applied_at: 2026-05-31T15:10:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/chebyshev-smoother-mutation-rotation.md (3 surgical edits, `:150-159` → `:147-155` in prose line 145, `verified_against:` block line 350, prose line 372; theme stays `firm`, status/claim/decomposition unchanged)
- scaffolding/open-questions.md (annotated resolved-cycle-035-D1 in-place at line 489 OQ `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten`; appended new intake `chebyshev-smoother-mutation-rotation-applyorder0-true-citation-tighten-sibling` per report §Open-questions; appended a Resolved-this-cycle pointer section)

Gate hits:
- citation-validity (citecheck `--scan` on report CYCLE.md): 8 ok / 0 failing
- citation-validity (`citecheck --anchor 'else'` on new `:147-155`): 1 ok
- YAML round-trip on edited `verified_against:` block: PASSES (parses as dict; `note:` value begins with `d`, no leading `'`/`"` quote — clears friction-ledger `verified-against-note-no-leading-quote-of-either-kind`)
- post-edit chapter sanity: `grep ':150-159'` returns zero matches; `grep ':147-155'` returns 3 expected matches (lines 145, 353, 372)
- fence-parity / cross-reference-integrity: unchanged (no fence-level edits; pure inline citation replacements)

Open questions promoted:
- chebyshev-smoother-mutation-rotation-applyorder0-true-citation-tighten-sibling (sibling `:101-110` → `:102-110` future-cycle hook; informational, citecheck-passing, low fan-out)

Open questions closed:
- chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten (resolved-on-landing per report §Discipline notes + dispatch directive; annotated in-place at scaffolding/open-questions.md:489 with cycle-035 D1 resolution + report pointer)

Build-relevant: yes

Notes: First per-report integration of cycle-035. Bounded-prose-correction lifter scope; META.md `overall_status: ready` with all 8 critic checks PASS and zero repair items. The deliberately-untouched sibling `:101-110` is citecheck-OK with current bounds (anchor at 102 within range); the report's §Open-questions tighter-to-`:102-110` observation is captured as a new low-priority intake OQ for future-cycle revisit. deferred `integrated_at:` to finalize per role-spec write-authority partition (book/, open-questions append, STAGING append only). No book rebuild, no commit — finalize will run `cargo make book` and the single commit/push.

---

## 2026-05-31T141500Z-abstractor-cg-initial-residual-quirk-lift
applied_at: 2026-05-31T15:55:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/ksp-solve-mutation-rotation.md (2 surgical additive edits in CG Sub-pattern B: (1) new Recognition note "initial-residual `Norml2`-vs-`Dot` asymmetry — likely Palace bug; upstream confirmation pending" inserted IMMEDIATELY AFTER the existing `CheckDot` Recognition note and BEFORE the `Citations:` block — now at lines 267-318; the existing `CheckDot` note + the warm-vs-cold `:566-567` note are unchanged; (2) 2 new `Citations:` rows appended after the existing `:484-485` final-state-writeout row — `iterative.cpp:398-411` + `vector.hpp:257-260` at lines 358-368. Theme stays `firm` — additive caveat only; no laws/signatures/operators/status changes. Distinct file from D1's chebyshev theme — no in-cycle conflict.)
- scaffolding/open-questions.md (narrowed migrated-to-plan entry at line 30: struck the lift portion as LANDED cycle-035 D2, retained a narrower sub-OQ `cg-initial-residual-quirk-upstream-confirmation-pending` for the bug-vs-intentional classification question that requires Palace maintainer input; per report §Supporting-evidence §OQ-ledger and §Open-questions caveat 1 — out-of-scope for this project to resolve unilaterally)

Gate hits:
- citation-validity (citecheck `--scan` on report CYCLE.md): 26 ok / 0 failing (matches report's pre-emit claim)
- citation-validity (`citecheck --anchor 'initial_guess'` on `iterative.cpp:398-411`): 1 ok (anchor at 398 in-range)
- citation-validity (`citecheck --anchor 'Norml2'` on `vector.hpp:257-260`): 1 ok (anchor at 257 in-range)
- fence-parity: PASSES — annotation prose + indented C++ snippets are inside the `<<<OLD ... ===NEW ... >>>` block; inner code samples are 4-space-indented markdown code (NOT nested fences); the file's fence count is unchanged by these edits (only ` ```text ` codeblocks for L1 signature/laws further down are fenced — those are untouched)
- post-edit chapter sanity: `grep` finds the new Recognition note at the expected line range (267 onward) and the 2 new Citations rows at lines 358 / 365 — exactly the insertion-point rationale the report described; the existing `:484-485` final-state-writeout citation row is preserved immediately above the appended pair
- bookkeeping (firm-status preservation): theme `## Status: firm` line and all `verified_against:` blocks are untouched; no in-line `status:` reduction; the annotation explicitly hedges "likely Palace bug; upstream confirmation pending" in the section header (rotation-quality gate passes per critic META)
- cross-reference-integrity: 1 internal slug ref in new prose `cg-initial-residual-quirk-palace-bug-flag-lift-path` — points to the (now-narrowed) OQ ledger entry; resolves; the cross-link in the annotation prose stays accurate

Open questions promoted:
- cg-initial-residual-quirk-upstream-confirmation-pending (narrower sub-OQ retained at scaffolding/open-questions.md:30 in migrated-to-plan section; "upstream confirmation needed that the asymmetry is unintentional" / "file an upstream issue or `git blame` line 408 introduction commit"; out-of-scope for this project to resolve; *Trigger:* upstream surfaces or a future cycle decides to file/track)

Open questions closed (narrowed):
- cg-initial-residual-quirk-palace-bug-flag-lift-path (lift portion CLOSED on landing — the recognition-rule annotation now lives in the firm artifact at `book/src/L1-L0/ksp-solve-mutation-rotation.md` CG Sub-pattern B; upstream-confirmation portion split off as the narrower sub-OQ above per report §OQ-ledger recommendation "integrator may close the OQ … with a narrower upstream-confirmation sub-OQ"; entry strike-through at open-questions.md:30 records the lift-LANDED disposition + retains the narrower sub-OQ in-place)

Build-relevant: yes

Notes: Second per-report integration of cycle-035. Additive abstractor recognition-rule annotation into firm L1>L0 theme; META.md `overall_status: ready` with all 8 critic checks PASS and zero repair items (one trivial cosmetic narrative polish in §Verification line 177 noted in META but not blocking). The report's three §Open-questions caveats 2-4 (downstream-impact-magnitude analysis, MINRES/BiCGStab analogue audit, "B == identity" framing-is-informal note) are NOT promoted to fresh ledger entries — they are scoping notes / future-work hooks already documented in the report itself; if a future cycle wants any of them as a tracked OQ, the abstractor/lifter on the next ksp-solve dispatch can append. The bug-fix sketch (replace `Norml2` with `Dot` at iterative.cpp:408) stays informational per report §Verification line 179 — we do NOT propose modifying Palace. deferred `integrated_at:` to finalize per role-spec write-authority partition (book/, open-questions append, STAGING append only). No book rebuild, no commit — finalize will run `cargo make book` and the single commit/push for cycle-035.

---

## 2026-05-31T141500Z-cross-layer-cross-cutter-floquet-operator-construction-variants
applied_at: 2026-05-31T16:45:00Z
applied_by: integrator-per-report
status: applied (observation-only, no book changes)

Files touched:
- scaffolding/open-questions.md (annotated the migrated-to-plan entry at line 31 with the cycle-035 D3 apply_linop-dimension RESOLVED disposition (NEGATIVE finding: `apply_linop` needs NO extension — `apply-linop-mutation-rotation` sub-patterns A/D + `apply-linop-overload-set.md:33` non-exhaustive caveat already accommodate `FloquetCorrSolver`); appended a NEW intake entry `floquet-correction-l1-gate-harvest` flagged for integrator-finalize migration to `priorities.md` Backlog — the third firm instance of `nested-constructed-operator-gate`, structurally isomorphic to `divfree-projector`, routed to `harvester` with the divfree-projector L1+L1>L0 templates as the port basis, plan-tag `nested-constructed-operator-gate-instance-3`)

Gate hits:
- citation-validity (citecheck `--scan` on report CYCLE.md): 44 ok / 2 failing — both MISS hits are typo-style bare paths in OQ caveat #1 prose (line 129: `drivers/eigensolver.cpp:237,240` and `drivers/drivensolver.cpp:138,141,289,292` lack the `palace/` prefix). The SAME source sites are cited correctly with `palace/` prefix at line 108 (`palace/drivers/drivensolver.cpp:138-141, 289-292`) and elsewhere in §Supporting evidence. The MISS instances are in REPORT-INTERNAL caveat prose, NOT in any `book/` proposed-change (this is an observation-only report with NO book/ edits), so they have ZERO build-artifact impact. Non-blocking per role-spec ("Non-blocking unless a MISS/AMBIG/OOB is unrepairable"); flagged here for transparency. Spot-verified the load-bearing cites: `floquetcorrection.cpp:72-85` Mult/AddMult bodies, `apply-linop-mutation-rotation.md:43-81` (sub-pattern A), `:127-172` (sub-pattern D), `apply-linop-overload-set.md:33` (the non-exhaustive caveat verbatim present), `divfree-projector.md:25-37` (firm-precedent), `nested-constructed-operator-gate.md:62-89` (2 firm instances — third instance landing is the gap) — all anchored on disk per critic's META citation-validity PASS finding.
- write-authority: respected — only `scaffolding/open-questions.md` and `STAGING.md` written; `scaffolding/priorities.md` deliberately NOT touched (it is co-owned by meta-phase + cycle-planner; integrator-finalize does the housekeeping migration to Backlog during cycle-end). NO `book/` edits applied (the report carries no proposed-changes block).
- cross-reference-integrity: all internal slug refs in the new OQ annotations resolve on disk — `book/src/L1-L0/apply-linop-mutation-rotation.md`, `book/src/L0/apply-linop-overload-set.md`, `book/src/L1/divfree-projector.md`, `book/src/L1-L0/divfree-projector-mutation-rotation.md`, `book/src/concepts/nested-constructed-operator-gate.md` all exist.
- safety-net gates (retroactive-budget / concept_writes / forward-edge / edge-label / H1-reuse / append-on-missing-slug / variant-axis / fence-parity / SUMMARY.md / index-placeholder displacement / implied-component stub materialization): all N/A — no `book/` edits applied; gates inapplicable to observation-only OQ-ledger updates.

Open questions promoted:
- floquet-correction-l1-gate-harvest (NEW intake at scaffolding/open-questions.md:32; **FLAGGED FOR INTEGRATOR-FINALIZE → priorities.md Backlog migration as a new plan candidate** + an `integrator-signals.md` suggested-next-dispatch entry; route `harvester`, plan-tag `nested-constructed-operator-gate-instance-3`, fan-out Medium, cost small — see report §Recommendation item 2 for the full sizing / template / variant-axis / sub-recommendation notes)

Open questions closed (partial — apply_linop dimension only):
- floquet-correction-operator-construction-variants (apply_linop dimension RESOLVED on landing — NEGATIVE finding: `apply_linop` needs no extension, `apply-linop-overload-set` non-exhaustive caveat already accommodates constructed-operator-gate classes; in-place annotation at scaffolding/open-questions.md:31 records the disposition + report pointer; the L1-tier coverage gap that the OQ originally collected is now split off as the new plan candidate `floquet-correction-l1-gate-harvest` above per the CLAUDE.md "intake feeds the plan, doesn't hold work" invariant)

Build-relevant: no

Notes: THIRD/FINAL per-report integration of cycle-035. Pure cross-layer-cross-cutter observation report — NO `book/` proposed-changes block, NO artifact mutations applied (deliberately, per role-spec for observation reports). META.md `overall_status: ready` with 7/8 critic checks PASS and 1 WARNING (skill-uptake-survey — telemetry-only, non-blocking, repairer marked unrepairable; producer-time skill-invocation gap on `establish-negative-finding-exhaustiveness`). All 3 repairer-fixable findings were repaired pre-integration (call-site arithmetic prose clean-up, citation-presentation split, negative-anchor grep added to OQ #1). **PROMINENT FLAG TO INTEGRATOR-FINALIZE:** the new plan candidate `floquet-correction-l1-gate-harvest` should be migrated into `scaffolding/priorities.md` Backlog at cycle-end housekeeping (Medium rank; route `harvester`; plan-tag `nested-constructed-operator-gate-instance-3`; sized small — half of divfree-projector cost; sibling-instance precedent makes this a low-risk firm landing) AND surfaced in `scaffolding/integrator-signals.md` as a suggested next-dispatch candidate. The cross-layer-cross-cutter cycle-035 D3 dispatch is a successful demonstration of the "intake feeds the plan, doesn't hold work" workflow: an OQ migrated-to-plan (Low) was investigated, its primary suspicion (apply_linop coverage gap) was empirically discharged (clean MATCH negative finding), and the actual coverage gap (a different tier — L1 operator + L1>L0 theme) was promoted to a concrete next-dispatch plan candidate with full sizing / template / variant-axis sketch — replacing the diffuse OQ with a sharp, actionable harvester item. deferred `integrated_at:` to finalize per role-spec write-authority partition (book/, open-questions append, STAGING append only). No book rebuild, no commit — finalize will run `cargo make book` (will be a no-op for this report's no-book-edit scope) and the single commit/push for cycle-035 covering all three D1/D2/D3 landings.

---
