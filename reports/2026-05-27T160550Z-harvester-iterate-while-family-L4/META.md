---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T16:17:29Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T16:35:00Z
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
overall_status: ready
follow_up_agent: null
---

# META: verification of CYCLE Formalize iterate_while + iterate_while_with_prev at L4 (family, single dispatch)

## Critique

### Checks run

**1. citation-validity — pass.** Sampled inline citations and found them in-range and content-aligned. `book/src/design/l4_calculus.md:151-184` is §3.7 Loops (line 150 is the header, body runs through ~184); `:186-228` straddles §3.8 (which actually ends ~228 — confirmed line 226 is the closing paragraph); `:164-171` is the verbatim small-step rule reproduced in the chapter; `:178-183` is the `iterate_while_pure` sugar definition; `:374-386` is the `run_lbm` example. `reference/palace/palace/linalg/iterative.cpp:427` is the PCG outer-loop `for (; it < max_it && !converged; it++)`; `:434-441` is the `if (!it) { p = z; } else { linalg::AXPBY(..., beta / beta_prev, p); }` branch; `:451` is `beta_prev = beta;`; `:615` is the GMRES inner-loop `for (;; j++, it++)`. `book/src/concepts/derived-view-hoisting.md:19` is the "Good (v0.4 revision)" paragraph stating the demand-pruning behavior. `book/src/concepts/first-iteration-unrolling.md:21-37`, `:34-37`, `:39-49`, `:17-37`, `:39-55` all fall within the 78-line file and contain the cited content (file ends at line 78). `book/src/spec/slices/cg.md:215-219` is the v0.4 `iterate_while` call site (verbatim match); `:393-446` covers v0.5 `cg_first_step`/`cg_steady_step`/`cg_solve` (lines 441-446 contain the `iterate_while_with_prev` call). `book/src/spec/slices/gmres.md:459-470` is the `inner_loop` tail-recursive definition (verified by inspection). One nit: the cycle-006-OQ-tail citation at frontmatter `scaffolding/open-questions.md:1064` is correct (the slug `iterate-while-l4-anchor-missing` block begins there).

**2. surface-or-evidence — pass.** This is a firm-operator-promotion dispatch — pure new-surface authorship (two new L4 chapter files, dep-map row replacements, SUMMARY entries, OQ status updates). The proposed-changes block clearly identifies the surface deltas (`book/src/L4/iterate-while.md`, `book/src/L4/iterate-while-with-prev.md`, `book/src/L4/index.md` dep-map rows, `book/src/SUMMARY.md` chapter listings, `scaffolding/open-questions.md` status + appends). No refinement-shaped proposals masquerading as evidence backfills.

**3. rotation-quality — pass (not the focus of this report; the relevant rotation is the L4>L3 lowering, deferred to a later cycle).** This is a harvester report formalizing operators; rotation-quality applies only to the §"Lowers to" sketch which describes the L4>L3 dissolution of: (i) Solve-monad threading, (ii) record-structured step return → positional tuple, (iii) trajectory record-list with demand-pruning → either accumulator pass-through or outright drop. These are state-hiding / coarser-substitution rotations (the L_{n+1} = L4 form is strictly more compact: row-polymorphic record spread vs. positional tuples; structural demand-pruning rule vs. resolved-per-call-site forms; implicit monad effect vs. explicit positional `sim` threading). No 1:1 renaming. The §"Lowers to" is sketch-only (the standalone L4>L3 theme is deferred — appropriately scoped out and OQ-flagged as cycle-008+ lowering-verifier follow-up). Rotation quality of the L4 family vs. the v0.4 in-step branch (Form A vs Form B): the report cleanly identifies "schema one slot lighter, branch-free steady step, static call-site obligation" — these are state-hiding / variant-axis-absorption rotations inherited from `first-iteration-unrolling`, also not new with this dispatch.

**4. variant-axis-coverage — pass.** The `iterate-while` chapter catalogues three orthogonal axes: (1) pure vs. Solve-threaded body, (2) extras-carrying vs. no-extras (`iterate_while_pure` sugar), (3) bootstrap-free vs. carry-bootstrapped (i.e., this entry vs. the companion). The `iterate-while-with-prev` chapter catalogues two axes (pure-vs-Solve, extras-vs-no-extras) and explicitly notes the third axis is below this combinator's level of abstraction (it *is* the carry-bootstrapped form; the Form-A/B presentation choice is slice-level). The two chapters' axis surfaces are explicitly cross-referenced and the family relationship (Law 1: degeneracy when `β = ()`) makes the combinator-vs-slice variant locus explicit. No hidden branches.

**5. cross-reference-integrity — warning.** All `[link]` references and operator slugs resolve in the artifact-as-it-will-be-after-this-dispatch. `concepts/solve-monad.md`, `concepts/derived-view-hoisting.md`, `concepts/convergence-test.md`, `concepts/first-iteration-unrolling.md` all exist (confirmed in `book/src/concepts/`). `L4/krylov-step.md` exists (cycle-006). `L4-L3/krylov-step-typed-wrapper-dissolution.md` exists, and its §"Speculative L4 operators" (line 126) and §"What the L3 form for `iterate_while` looks like" (line 156) are present as cited. The two new chapters self-reference each other and reference `L4/krylov-step.md` — all targets are valid. **One issue**: the `iterate-while.md` §"L4 vs L3 distinction" mentions a `(currently being authored)` sub-theme reference to "the cycle-007 lowering-verifier follow-up"; that sub-theme is not authored by this dispatch and is appropriately flagged. **One more issue**: the §"Lowers to" of `iterate-while.md` and `iterate-while-with-prev.md` describe the L3 form as "a sub-component of the `krylov-step-typed-wrapper-dissolution` theme" but the existing theme's §"What the L3 form for `iterate_while` looks like" specifically describes a single-readout (not a trajectory) collapse — which is the very semantic gap flagged in the existing OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`. The new chapters cite the existing theme as if it provides a trajectory-shape-preserving L3 lowering, which it does NOT — the existing theme's L3 form drops the trajectory. This is a forward-reference to a not-yet-reconciled rendering; the chapters honestly defer it via the (duplicated) follow-up OQ but the §"Lowers to" prose treats the theme as the authoritative anchor when it currently is not. Minor severity (the discrepancy is self-flagged via the new OQ that mirrors the existing one); could be sharpened by a one-line "the existing theme's L3 form drops the trajectory; this discrepancy is reconciled by the follow-up theme tracked in OQ X."

**6. edge-label-fidelity — pass.** No edge labels (L_{n+1}→L_n claims) appear on this dispatch — it's a same-layer L4-formalization. The §"Lowers to" sketches reference a future L4>L3 theme but explicitly defer it; the discussion stays L4-internal modulo the obvious "this is what would dissolve at L3" sketch.

**7. plan-kind-consistency — pass.** Declared kind is `harvester` → firm L4 operator chapter; the two chapters carry full Signature / Semantics (small-step rules in `$$ ... $$` math display, matching the strawman's conventions) / Algebraic laws (Laws + non-laws) / Variant axes / Status sections per the cycle-006 `krylov-step.md` precedent. Status set to `firm` is justified by the in-management strawman §3.7 anchor. No rough-in placeholders. The bundling of two operators in one dispatch is well-motivated by the §Summary "family" framing (mutually-referential signatures, Law 1 degeneracy, shared content) — not a role-spec violation. The strawman conventions are honored throughout: BNF-style signatures in `text` fences, Haskell `::` arrow form, TypeScript brace form for records, do-notation, `$$ ... $$` for reduction rules. Pseudo-language discipline matches the cycle-006 precedent and the user directive 2026-05-27.

**8. skill-uptake-survey — warning.** The report references at least three skills that could have been invoked but only one is explicitly cited:
- `classify-variant-axis` — the variant axes are catalogued in detail in both chapters; the skill is applicable but not invoked-by-name. Pass-equivalent — the catalogue is thorough.
- `verify-citation-range` — the report's citation discipline is high (per-citation in-range checks would have been the canonical invocation); no skill invocation reference.
- `verify-refinement-surface` — applicable since this dispatch involves surface authorship; would have surfaced the L3-theme-anchor-vs-actual-rendering mismatch flagged in check 5. Not invoked.
- `summary-md-surgical-insert` — explicitly relevant to the SUMMARY.md edit (insert two chapter entries after `krylov-step`); the change is described prose-only without skill invocation.
The skill-selection skill's typical pattern (preface dispatch with one-line "Skills considered: A, B, C; chose A because…") is not present. Telemetry signal: the harvester role's skill-uptake on a representative complex dispatch is light — five available skills, zero explicit invocations. Pure presence finding, not blocking.

### Issues found

1. **Duplicate OQ proposed: `iterate-while-l3-trajectory-accumulator-vs-readout-collapse`** (proposed-changes / `scaffolding/open-questions.md` append, full text at CYCLE.md lines 583-593). An existing OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` is already in the ledger at `scaffolding/open-questions.md:1177-1185`, opened in cycle-006 by the abstractor dispatch, with the *identical* two candidate resolutions (a) re-render the L3 form with explicit trajectory accumulator pass-through; (b) author an explicit demand-pruning step justifying the collapse. The new OQ also names "lowering-verifier dispatch" and "harvester on L4 loop-combinator family" as routes — the latter is exactly *this dispatch*, which is now in the past. The new OQ should either (i) be dropped in favor of a status update on the existing OQ (e.g., "harvester closed `iterate-while-l4-anchor-missing` cycle-007 but did NOT reconcile the L3 trajectory-vs-readout gap; gap remains for cycle-008+ lowering-verifier"), or (ii) explicitly name the existing OQ in its `relates_to:` field with a note that it duplicates / supersedes — and update the existing OQ's routes-to to remove "cycle-007 harvester on L4 loop-combinator family" since that route did not resolve it. Severity: medium — duplicate OQs cause ledger bloat and confuse forward-frontier planning. Repairable: yes (revise the proposed OQ to a status-update on the existing one, or drop and add a note to the existing OQ).

2. **Forward-citation to an L3 form that does not match the L4 form on a load-bearing dimension** (chapter `iterate-while.md` §"Lowers to" at CYCLE.md line 246-252; chapter `iterate-while-with-prev.md` §"Lowers to" at CYCLE.md line 485-505). Both chapters cite `krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like" as the L3 lowering anchor. The existing theme's L3 form (per the cycle-006 abstractor's rendering at `krylov-step-typed-wrapper-dissolution.md:156-168`) returns a single readout, not a trajectory — exactly the gap flagged by the existing OQ above. The new chapters' §"Lowers to" prose acknowledges this with phrases like "standalone theme pending cycle-007 lowering-verifier follow-up" but the cited theme is treated as authoritative. The prose could sharpen: explicitly state the existing theme's L3 form drops the trajectory (current discrepancy), reference the existing OQ slug `iterate-while-l3-rendering-trajectory-accumulation-gap`, and frame the standalone-theme follow-up as resolving that named gap. Severity: low — the gap is self-flagged but the citation could be more precise. Repairable: yes (sharpen the prose; cite the existing OQ slug).

3. **CG v0.5 closure-argument-position convention mismatch acknowledged but not addressed in the dep-map** (chapter `iterate-while-with-prev.md` §Evidence at CYCLE.md lines 537-538; §"Open questions / caveats" item 4 at CYCLE.md lines 640-641). The chapter's signature puts `(β, α)` (prev first, carry second) in `steady_step`'s positional argument; the actual cg.md v0.5 call site at line 441-445 uses `(s, beta_prev)` (carry first, prev second). The chapter cites this as a deliberate choice (matching `first-iteration-unrolling.md:34-37` which writes `(s, carry)` — note the strawman pseudo-code at line 36 is `(s, carry)` i.e., state first, carry/prev second). Re-reading `first-iteration-unrolling.md:34-37`: `(\(s, carry) -> (steady_step ... carry s, extract_carry s))` — the order is `(s, carry)`, i.e., state first. The chapter's signature `(β, α)` therefore *contradicts* the first-iteration-unrolling pseudo-code it claims to match, not the cg.md call site. Severity: medium — the chapter justifies its argument order by citing a pseudo-code form that uses the *opposite* order. The cg.md v0.5 form actually agrees with the first-iteration-unrolling pseudo-code; the new L4 chapter introduces the inconsistency. The §Evidence note inverts the situation. Repairable: yes — either (i) flip the chapter's signature to `(α, β)` to match both first-iteration-unrolling and the existing cg.md rendering (the simpler resolution), or (ii) keep `(β, α)` and rewrite the §Evidence note to say "departure from the cg.md and first-iteration-unrolling convention; rationale = …". Note this affects the small-step rule (`steady_loop β a f p` form throughout §Semantics), Law 1, and the §Dependencies cross-links — touches multiple lines.

4. **The new OQ `gmres-inner-loop-iterate-while-migration` is well-formed but verges on duplicating a cycle-007-already-noted opportunity.** The cycle-006 OQ list (per the report's own framing) flagged the GMRES inner-loop pattern in the §Evidence sections. The new OQ adds concrete migration target detail. No actual duplicate ledger entry; this is a new OQ. Severity: none (acceptable). Listed for telemetry only.

5. **The new OQ `iterate-while-pure-promotion-decision` is well-formed.** No duplicate; routes-to is clearly "cycle-008+ harvester or planner" with a clear cost-benefit framing; deferred-until trigger is explicit (a second non-Krylov slice exercising the sugar). No issues.

6. **The Solve-monad `>>=` trajectory-build order is hand-waved** (`iterate-while.md` §Semantics second math block at CYCLE.md lines 145-152; caveat 6 at CYCLE.md lines 644-645). The Solve-threaded reduction rule writes the trajectory accumulation as `return { final_state, trajectory: [{...e}] ++ trajectory }` inside a `do`-block — but under strict StateT evaluation order, the recursive `iterate_while a' p f` would have already produced the trajectory list before the prepend, and the trajectory is built bottom-up. The caveat 6 acknowledges this and defers to "the cycle-006 `solve-monad` concept page does not commit to evaluation order". This is correctly flagged as a low-priority refinement; not blocking. Severity: low (already self-flagged). Listed for completeness.

7. **`scaffolding/open-questions.md` resolve-mark mechanism**: the proposed-change for `iterate-while-l4-anchor-missing` says the integrator should mark it as `resolved-by: harvester:2026-05-27T160550Z-harvester-iterate-while-family-L4`. The cycle-006 OQ entry (`scaffolding/open-questions.md:1062-1071`) uses a YAML-fenced metadata block with `status: open`. The proposed resolve mark would need to flip `status: open` to `status: answered` (matching the existing convention used by `krylov-step-l3-row-contingency` at line 1078). The report describes the resolve as "mark as resolved-by:" which doesn't match the YAML schema. Severity: low — integrator-per-report can apply the right schema, but the proposed-change text should match the existing convention for clarity. Repairable: yes (rewrite the resolve-mark instruction to use `status: answered` and add `answered_at: cycle-007` and `answered_in:` keys matching the line-1078 pattern).

8. **Codemap pilot section is appropriately structured as instrumentation, not as a failure narrative.** Per the dispatch instructions, the codemap pilot was permission-denied; the user has elected to defer to cycle-009 meta-phase. The report's §codemap-pilot-instrumentation section is a structural finding (tool-call count by tool, permission-denial root cause, recommendations conditioned on permission-fix) without inflating the failure. No issue. Listed for completeness.

9. **Layer-intro refresh note** (CYCLE.md lines 647-649): the report flags that with three firm L4 rows now landing, `book/src/L4/index.md`'s "Semantics (overlay)" section is stale. This is correctly scoped-out (harvester does operators, not layer intros) and OQ-routed (cycle-008+ layer-intro-author). Not an issue with this dispatch's content. Listed for completeness.

## Repair

### Fixes attempted

- **Finding (#3, medium)**: CG v0.5 closure-argument-position inversion. The chapter's `iterate_while_with_prev` `steady_step` signature wrote `(β, α)` (prev first, carry second), contradicting both `first-iteration-unrolling.md:34-37` pseudo-code (`\(s, carry) -> ...`) AND the CG v0.5 call site at `cg.md:443` (`\(s, beta_prev) -> ...`). The §Evidence note also inverted which side was the departure.
  - **Decision**: repaired
  - **Action**: flipped the signature throughout the `iterate-while-with-prev.md` chapter content to `(α, β)` (carry first, prev second). Edits applied at CYCLE.md:
    - §Signature: all three forms (pure, extras-carrying pure, Solve-threaded) updated to `((α, β) -> ...)`.
    - §Signature shape-contract paragraph: `steady_step` argument-order description flipped (carry first, prev second).
    - §Signature post-form paragraph: new last sentence noting the convention now matches both cited evidences.
    - §Semantics: small-step rule's auxiliary `steady_loop β a f p` → `steady_loop a β f p`; `f(β, a)` → `f(a, β)`; bootstrap-then-call line updated correspondingly.
    - §Algebraic laws Law 1: degeneracy reduction `f_{\textsf{steady}}((), a)` → `f_{\textsf{steady}}(a, ())`.
    - §Evidence note: rewritten to record that the L4 row's convention is *consistent* with both upstream renderings; no v0.6 self-rotation on cg.md is needed.
    - §Open questions / caveats item 4: rewritten to record the reconciliation.
    - Dep-map row in `book/src/L4/index.md` proposed-changes block: signature inline updated to `((α, β) -> ...)`.

- **Finding (#1, medium)**: duplicate OQ `iterate-while-l3-trajectory-accumulator-vs-readout-collapse` proposed by this dispatch duplicates the existing cycle-006 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` (same theme, same two candidate resolutions, overlapping route-to targets).
  - **Decision**: repaired
  - **Action**: removed the duplicate OQ from the proposed-changes block. Replaced with a status-update note on the existing cycle-006 OQ recording that the cycle-007 harvester firmed the L4 trajectory shape but did NOT reconcile the L3-form trajectory drop, and that the gap remains open for cycle-008+ lowering-verifier. The two new OQs (`gmres-inner-loop-iterate-while-migration` and `iterate-while-pure-promotion-decision`) remain as legitimately-new entries. Edits applied to:
    - Proposed-changes block (CYCLE.md ~line 54-56): description rewritten to "two new OQs" + "status-update note on existing OQ".
    - §"Operator content — `scaffolding/open-questions.md` append": duplicate OQ block deleted; replaced with a status-update note to be appended to the existing OQ body; the two surviving new OQs reformatted with the existing ledger's `opened_at:` / `opened_by:` / `status:` schema (instead of the report's earlier `cycle:` / `proposed_by:` keys — Finding #7 schema-consistency fix folded in).
    - §"Open questions / caveats" item 1: rewritten to note no new OQ filed; the existing OQ's body is augmented instead.
    - §Status of `iterate-while.md`: updated count from "Three follow-up open questions" to "Two new follow-up open questions ... and one existing OQ augmented".
    - Dep-map row in `book/src/L4/index.md` proposed-changes block: OQ slug reference updated from the (now-deleted) `iterate-while-l3-trajectory-accumulator-vs-readout-collapse` to the existing `iterate-while-l3-rendering-trajectory-accumulation-gap`.

- **Finding (#2, low)**: forward-citation precision — both chapters' §"Lowers to" cite the cycle-006 L4-L3 theme whose L3 form drops the trajectory (the very gap), treating the theme as authoritative.
  - **Decision**: repaired
  - **Action**: added a one-sentence acknowledgment to both chapters' §"Lowers to" sections that the existing theme's L3 rendering at `krylov-step-typed-wrapper-dissolution.md:156-167` drops the trajectory (the firm L4 form keeps it via Law 1 / Law 2), naming the existing OQ slug `iterate-while-l3-rendering-trajectory-accumulation-gap` and explicitly framing the standalone-theme follow-up as resolving that named gap. Also updated `iterate-while.md` §"L4 vs L3 distinction" to route to the same existing OQ slug and to cycle-008+ rather than cycle-007.

- **Finding (#7, low)**: OQ resolve-mark schema mismatch — the dispatch wrote "mark as `resolved-by:`" which doesn't match the existing ledger's `status: answered` + `answered_at:` + `answered_in:` convention (precedent: cycle-006 `krylov-step-l3-row-contingency` at line 1078).
  - **Decision**: repaired
  - **Action**: rewrote the resolve-mark instruction in the §"Operator content — `scaffolding/open-questions.md` append" section to emit a literal YAML frontmatter block flipping `status: open` → `status: answered` and adding `answered_at: cycle-007` + `answered_in: reports/...` keys. Also reformatted the two surviving new OQs' YAML frontmatter to use the existing-ledger schema (`opened_at:` / `opened_by:` instead of `cycle:` / `proposed_by:`); fenced as `yaml` instead of `markdown` for consistency with the existing ledger entries.

- **Finding (#6, low)**: Solve-monad `>>=` trajectory build-order is hand-waved. Critic said "Severity: low (already self-flagged). Listed for completeness."
  - **Decision**: not-needed
  - **Action**: caveat is present at §"Open questions / caveats" item 6; no repair required. Future Solve-monad refinement (concept-page-level work) would address it.

- **Findings (#4, #5, #8, #9)**: catalogued by critic as "not an issue / acceptable / listed for completeness".
  - **Decision**: not-needed
  - **Action**: no action required.

- **Warnings** (cross-reference-integrity: warning; skill-uptake-survey: warning):
  - Cross-reference-integrity warning is fully addressed by the three repairs above (Findings #1, #2, #3 — all the cross-reference issues the warning surfaced). Re-classification justified.
  - Skill-uptake-survey warning is non-blocking telemetry signal about agent dispatch behaviour; cannot be repaired within report content. Surfaced for meta-phase / friction-ledger consumption only. No repair action.

### Unrepairable findings

None. All medium-severity findings are mechanical and were repaired in-place; all low-severity findings were either self-flagged (#6) or did not require action (#4, #5, #8, #9). The skill-uptake-survey warning is telemetry, not content; it does not block readiness.

## Suggested resolution

`ready` — the report's proposed-changes block is now self-consistent on the closure-argument convention (matches both cited evidences) and OQ-ledger-schema-correct (uses the existing `opened_at:` / `opened_by:` / `status: answered` / `answered_at:` / `answered_in:` convention). The duplicate OQ is removed; the existing cycle-006 OQ on the same theme is augmented with a cycle-007 status note (rather than blooming a parallel ledger entry).

**Note to the integrator-per-report**:
- The `iterate-while-l4-anchor-missing` resolution is now expressed as a YAML frontmatter edit (flip `status:` and add two keys) rather than a free-text "resolved-by:" mark. The YAML block in the proposed-changes section is the new value of the existing ledger block at `scaffolding/open-questions.md:1062-1069`.
- The `iterate-while-l3-rendering-trajectory-accumulation-gap` body augmentation is to be appended to the existing ledger block at `scaffolding/open-questions.md:1185` (immediately after the body's last paragraph, before the next `---` block) — keeping the OQ's `status: open`.
- The two new OQs (`gmres-inner-loop-iterate-while-migration` and `iterate-while-pure-promotion-decision`) are pure appends to the end of the Open section (before the `## Dropped` heading at line 1187).
