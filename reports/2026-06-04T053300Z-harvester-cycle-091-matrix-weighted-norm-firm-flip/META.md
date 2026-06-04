---
verifies: ../REPORT.md
critiqued_at: 2026-06-04T061500Z
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

# META: verification of cycle-091 D1 — matrix-weighted-norm rough-in→firm flip + L1/L4 index count-ownership

## Critique

### Checks run

**citation-validity — pass.** The flip's license rests on three evidence pointers, all verified on disk:
- The two `verified_against:` YAML blocks are present in `book/src/L1/matrix-weighted-norm.md` exactly where the report claims: the **cycle-088 structure-side** block at `:145-171` (6 entries: the radicand test `test-domainpostoperator.cpp:75-93`, the energy-form body `domainpostoperator.cpp:219-231`, the `Norml2` √-overload `operator.cpp:599-619`, the SPD-construction homes `eigensolver.cpp:205-213` + `spaceoperator.cpp:530-537`, and the laws-4/6/7 structure-side-discharge note), and the **cycle-089 FP-side** block at `:179-205` (6 entries discharging the two FP non-laws by inheritance from firm `dot`/`apply_linop` through the deterministic IEEE-754 `√`, with the `nrm2` firmness precedent). Both blocks round-trip as valid YAML — every `note:` scalar begins with prose (`GetElectricFieldEnergy…`, `cycle-088 probe…`, `cycle-089 FP-residue probe…`, `firm constituent…`, `dispositive firmness…`, `outer sqrt…`), none opens with a leading `'` or `"`, so the round-trip sub-check is clean.
- The meta-phase GO is real and carries exactly the reasoning the report claims: `reports/2026-06-04T032609Z-meta-phase-cycle-090/CYCLE.md` §Decisions "go 1" (`:41-48`) GO's `matrix-weighted-norm-firm-flip-and-cascade-wave` as the batch-29 LEAD, with the structure-side (c088) + FP-side (c089) discharge and the explicit "**Gate (a) is therefore REDUNDANT** — everything the missing test would confirm … is already anchored. There is NO law/property for which the test is the only evidence" (`:46`), naming the four prior escape promotions. The cycle-record append (`:76`) carries `"batch_29_lead": "matrix-weighted-norm-firm-flip-and-cascade-wave"`.
- The report's restated §Status prose re-cites the SPD-construction comment at `eigensolver.cpp:206-207` and the `GetInnerProductMatrix` call at `:212`/`SetBMat :213` — consistent with the preserved verified_against block's `:205-213` whole-block citation; the report explicitly flags (§Supporting evidence) that it did NOT introduce a drifted `:206-207 --anchor GetInnerProductMatrix` form, and self-ran citecheck `--anchor` on `operator.cpp:606` (sqrt) and `spaceoperator.cpp:530-537` (GetInnerProductMatrix), both `[ok]`. No citation drift detected.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (modifies the §Status surface of an existing operator) and it carries the required evidence: the two discharge blocks ARE the rotation_claim evidence, and the flip modifies surface text (§Status head + index labels/counts). The decisive question for this kind — does the report smuggle a positive claim that gate (a) was the *only* evidence for? — resolves cleanly: the report restates the escape faithfully ("the missing test does not gate such laws"), and the on-disk chapter §Status `:115` already concludes "**only the entry-point test remains** … the combined discharge LICENSES … a future full-firm flip." The structure-side laws are inner-product-space theorems (exact-arithmetic, not test-gated) and the FP non-laws inherit additively from firm constituents; neither is a positive claim the missing test uniquely backs. The SPD-ness "construction-attested not runtime-verified" point is correctly framed as the scoping note the escape *requires* (§Applicability `:68` records the non-SPD-caller absence), not an independent obstruction. Record-definition sub-check no-ops: the signature names only L1 primitive shape-contract types (`Tensor[N]`, `LinearOperator[N,N]`, `Scalar`), no record/struct.

**rotation-quality — pass (not applicable to a maturity-flip report).** D1 asserts no new algebraic/structural/reduction rotation — it is a maturity promotion on an already-fully-authored firm-apparatus chapter (signature, 12 laws, variant axes, evidence all pre-existing and PRESERVED). No L_{n+1}→L_n compaction claim is made, so the rotation-quality check has nothing to adjudicate.

**variant-axis-coverage — pass.** The chapter's two orthogonal variant axes (element-type real|complex; output-arg vs return-value pattern) plus the two collapsed axes (parallel-wrapper, operator-representation of `B`) are already authored in §"Variant axes" (`:94-106`) and are not touched by the flip. No hidden branch is introduced by the maturity change.

**cross-reference-integrity — pass.** Confirmed D1 did NOT touch the L1>L0 theme `matrix-weighted-norm-mutation-rotation` — its §Status is `firm` on disk (`book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:432-434`), matching the report's hard-constraint claim (report cites `:432`; the `## Status` header is at `:432`, the `firm` token at `:434` — accurate). The `:57`-header deferral is clean: `book/src/L4/index.md:57` still reads "**Rough-in at L4 (1)** … gated on its `matrix-weighted-norm` rough-in folded primitive" on disk, and the report leaves it unedited, correctly flagging the reduce-verb-status reconciliation (`:57`/`:59`/`:98`-Status/`:102`) as owed-to-D3 rather than guessing the verdict blind. The one L4/index edit D1 DOES take — the `:98` Folds-cell standalone `matrix-weighted-norm (rough-in → firm c091)` label — is the unambiguous matrix-weighted-norm-specific maturity label that flips regardless of D3's verdict; the `:98` row currently reads "(rough-in — the domain-restricted energy numerator …)" on disk, matching the report's OLD anchor. The `:102` joint Folds cell is correctly left to D3 (it co-covers still-rough-in `bilinear-form`). All `[link]` targets in the proposed bullets resolve to existing chapters (`dot.md`, `apply_linop.md`, `bilinear-form.md`, `matrix-weighted-norm.md`).

**edge-label-fidelity — pass (not applicable).** D1 carries no L_{n+1}→L_n edge label; it is an in-layer maturity flip plus index counts. Nothing to check.

**plan-kind-consistency — pass.** The declared kind (firm-flip / count-ownership harvest) matches the content shape, and the count deltas are arithmetically correct on disk:
- `grep -cE '\| \`firm'` on `book/src/L1/index.md` returns **37** firm dep-map rows currently; exactly ONE `matrix-weighted-norm` rough-in dep-map row exists, at `:117` (`rough-in (test-coverage-bounded, harvested-by: …)`). Flipping that one row firm gives **38** — confirming the grand 37→38 and, with the FE-assembly (4) + FE-space (3) sub-spines held constant, the main-cohort 30→31.
- The count-header anchors the report edits exist verbatim: `:31` carries "**Firm (30 main cohort; 37 firm grand total …)**" and the "30 main + 4 FE-assembly + 3 FE-space = 37" derivation, and the pre-staged c080 count-reconciliation note (the "IF D1's audit promotes … fold its +1 into BOTH" note) is present to be discharged.
- `bilinear-form` is correctly left as the SOLE remaining `**Rough-in (test-coverage-bounded)**` entry: under that header (`:64`) the two bullets are `matrix-weighted-norm` (`:66`, removed by D1) and `bilinear-form` (`:67`, untouched — its own `lower-layer-shared-vocabulary` gate, not D1's lane). The `:113` `bilinear-form` dep-map row stays `rough-in (lower-layer-shared-vocabulary)`.
- D1 stays in lane: it does NOT touch consumer files (D2's cluster), the reduce-verbs' own status tokens / gating rationale (`gram_reduce` / `domain_energy_reduce`, D3), or the feature columns (D4). The L4/index reduce-verb-status lines are explicitly deferred to a D3-coordinated follow-up.

**skill-uptake-survey — pass.** The report's shape (a firm promotion with a whole-book cross-reference cascade) implies the `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` discipline (batch-27 GO) — the report references it by name and demonstrates uptake (its in-file grep caught the stale `:40` normalize-bullet "inherits matrix-weighted-norm's test-coverage bound" clause beyond the four planner-listed anchors). Citecheck `--anchor` pre-emit self-verification is also referenced. Telemetry only; non-blocking.

### Issues found

None. All eight checks pass. The firm flip is legitimately licensed (both discharge blocks present + valid; meta-phase GO real with the redundant-gate-(a) reasoning; no smuggled positive claim), the count deltas are arithmetically correct on disk (37→38 grand, 30→31 main, exactly one rough-in row flips), `bilinear-form` is correctly left as the sole remaining rough-in (test-coverage-bounded) entry, and D1 stays cleanly within its lane (L1>L0 theme untouched/already-firm, reduce-verb + feature-column lines deferred to D3/D4, `:57` header left unedited).

This is an all-pass clean report; no repairer will run, so the critic sets the canonical `overall_status: ready`.
