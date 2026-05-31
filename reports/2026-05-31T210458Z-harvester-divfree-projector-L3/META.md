---
verifies: ../REPORT.md
critiqued_at: 2026-05-31T21:30:00Z
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
repaired_at: 2026-05-31T21:45:00Z
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

# META: verification of harvester divfree-projector L3 (constructed-operator-gate identity-in-form backfill)

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` on the report returns `24 ok, 0 failing (24 citations checked)` — matches the report's 24/24 claim. All six load-bearing anchors re-verified on-disk via `--anchor`: `divfree.cpp:155-187` anchor `Mult` `[ok]` at lines [155, 162, 163, 167, 175, 180, 181, 185] (exactly the set the report cites); `divfree.cpp:175` anchor `ksp` `[ok]`; `divfree.hpp:28-31` anchor `divergence` `[ok]` at :29; `eigensolver.cpp:260-262` anchor `Mult` `[ok]` at :262; `divfree.cpp:189-190` anchor `DivFreeSolver` `[ok]`; `divfree.cpp:119` anchor `SPD` `[ok]`. I also read `divfree.cpp:155-187` directly: the meaning-read confirms the four-step apply (WeakDiv→SetSubVector→ksp->Mult→Grad->AddMult), the inner `ksp->Mult(rhs, psi)` at :175, the additive `1.0` correction, and the complex Re/Im branches — all faithfully reported. No `verified_against:` YAML block is present (this is a harvester, not a lowering-verifier audit), so that round-trip sub-check is not applicable. Pass.

**surface-or-evidence — pass.** This is a new firm L3 entry (a backfill creating `book/src/L3/divfree-projector.md`), not a refinement of an existing operator/theme's surface text. It authors new L3 surface (the `## Signature` / `## Semantics` / `## Algebraic laws` chapter body) and carries identity-in-form rotation evidence (value-thread-isomorphism to the firm L1 entry, transitive L0 citations). The pure-rotation-without-surface failure mode does not apply: surface is authored. Pass.

**rotation-quality — pass (identity-in-form, correctly framed).** The rotation is L3>L1 identity-in-form on the constructed-operator-gate apply — explicitly NOT an algebraic compaction. Under the project's **Identity-lowerings still require both L levels** invariant this is a first-class, intended shape (a layer-coherence backfill, not a renaming defect): the L3 entry exists so the L3 reader finds the gate in L3 vocabulary, and the report states this directly (Context, §Lowers-to, §L3-vs-L1). The load-bearing obstruction-by-reference framing is faithfully stated and consistent with the `nested-constructed-operator-gate` fidelity rule: the gate (a) does NOT introduce a new projector-level obstruction (its four-step apply is a fixed straight-line composition — verified against source: no loop in `Mult`), and (b) does NOT erase the inner one (the CG iteration stays interior to `ksp_solve`). The report does not over-claim obstruction-freedom (it explicitly contrasts against the obstruction-free `jacobi-smoother`) nor under-claim (it places the gate with `ksp_solve`/`eigsolve` as obstruction-carrying). Pass.

**variant-axis-coverage — pass.** One orthogonal axis (element-type: `Vector` real | `ComplexVector` complex) and one absorbed axis (operator-representation, incl. the inner `ksp` solver) — matching the L1 profile, with the absorption rationale stated. The element-type axis is L0-anchored (`divfree.cpp:189-190` template instantiations, verified). The inner `ksp_solve`'s own five loop-shaping axes are explicitly scoped out as interior-to-that-gate (§Variant axes closing note). No hidden branch: the complex/real branches of `Mult` are both covered (the report cites :162-163 complex / :167 real for step 1, :180-181 / :185 for step 4). Pass.

**cross-reference-integrity — pass (build-readiness clean).** Fence enumeration: 6 ```` ``` ```` markers → 3 balanced `edit:` blocks (50–661 chapter, 663–669 SUMMARY, 671–680 L3 index); even parity, no nested code fences inside any block. Build-readiness guard (`proposed-changes-fence-encloses-full-body-guard`): the full firm chapter body is INSIDE the chapter fence — `## Signature` (line 170), `## Semantics` (234), `## Algebraic laws` (317), `## Status` (465), `## Evidence` (566) all sit between the opening fence (50) and closing fence (661). Signatures rendered as 4-space-indented code, NOT nested ```` ```text ```` — the cycle-019 fence-truncation defect is absent. The report's own `## Operator content` / `## Supporting evidence` sections (outside the fence) are report scaffolding, not chapter body, so this is not the firm-body-outside-fence defect. Link targets verified on disk: `L3/ksp_solve.md`, `L3/jacobi-smoother.md`, `L3/apply_linop.md`, `L3/axpy.md`, `L3/eigsolve.md`, `L3/krylov-step.md`, `L1/divfree-projector.md`, `L1-L0/divfree-projector-mutation-rotation.md`, `L1-L0/ksp-solve-mutation-rotation.md`, and concepts `nested-constructed-operator-gate` / `sequential-obstruction` / `set_subvector_zero` / `constructed-operators` / `variant-absorption` all EXIST (live links justified). `book/src/L2/divfree-projector.md` is absent on disk and is correctly kept plain-text (never linked) in the prose. `L3/divfree-projector.md` does not yet exist (this dispatch creates it). The SUMMARY insertion + L3 index dep-map row are well-formed. The "fourth obstruction profile" overlay note is correctly flagged as a layer-intro-author follow-up, not a defect. Pass.

**edge-label-fidelity — pass.** The declared edge is L3>L1 identity-in-form (no L2 interposed, no L3-L1 directory). Prose discusses exactly that edge throughout (§Lowers-to, §L3-vs-L1, dep-map "Lowers to" column). The transitive-chain claim `eigsolve ⊃ divfree-projector ⊃ ksp_solve` at L3 is anchored to `concepts/nested-constructed-operator-gate.md`, which I verified: the concept names `divfree-projector` as a firm one-nested-gate instance (lines 83-89) and gives that exact chain (lines 107-115, "Chain 1 (eigsolve pipeline)"). The cited L3 index :41 verdict ("constructed-operator gate, like firm-L3 `ksp_solve`") is verified verbatim. Pass. (See Issue 2 for a non-blocking precision note on where the chain is anchored.)

**plan-kind-consistency — pass.** Status `firm` matches content shape: every law is a syntactic identity transported from the firm L1 entry (whose laws read off positive source, not literature-inferred convergence), so the missing `test-divfree.cpp` does not gate firm — the report invokes the firm-on-positive-structure escape correctly (Status §, citing the cycle-014/015 L1 promotion). Defined in L3 vocabulary high→low (the L_n entry uses L3 vocabulary; the substantive rotation is pushed down to the L1>L0 theme, per "Layers are defined high→low"). Non-adjacent identity annotated in-line, no `L3-L1/` directory created (cycle-012 convention). No rough-in placeholders in a firm entry. Pass.

**skill-uptake-survey — pass.** The report references `tools/citecheck/citecheck.py --anchor` self-verification (the verify-citation-range mechanical realization) for all source anchors, and names `summary-md-surgical-insert` for the SUMMARY insertion (line 753). Both are the shape-appropriate skills for a firm L3 backfill. Telemetry present; no blocking concern.

### Issues found

**Issue 1 — "six laws" miscount, recurring throughout the report (severity: medium; factual inconsistency).** The report asserts "the same six algebraic laws" / "six laws" in 7 places (Summary lines 33-34; Context; §Status line 469; the L3-index Working-Notes dep-map bullet line 679; §Lowers-to line 524; §L3-vs-L1 line 653; the proposed `lowers_to` frontmatter and prose). But the authored L3 `## Algebraic laws` section lists exactly **5 numbered laws** (1. Linearity, 2. Idempotence, 3. Range, 4. M-orthogonality, 5. Real-linearity/block-diagonal complex), followed by **2 load-bearing non-laws** (sign convention, step ordering). The firm L1 source entry (`book/src/L1/divfree-projector.md` §Algebraic laws) likewise has 5 numbered laws + 2 non-laws. Under the report's OWN taxonomy (which explicitly classifies sign-convention and step-ordering as the "two load-bearing non-laws"), the correct phrasing is "five laws + two non-laws," not "six laws." The self-consistent body (the numbered list) is correct; the recurring summary-prose "six" is wrong. Location of the canonical correct list: CYCLE.md lines 317-376 (chapter §Algebraic laws, items 1-5 + 2 non-laws). This is a candidate for mechanical repair (s/six/five/ on the law-count assertions, leaving the non-law count intact). It does not affect any citation or the firm verdict, but it is a load-bearing factual claim that should not ship inconsistent with the entry's own list.

**Issue 2 — transitive-chain anchoring is concept-level, not L3-eigsolve-entry-level (severity: low; precision note, not an over-claim).** The report cites the transitive chain `eigsolve ⊃ divfree-projector ⊃ ksp_solve` "at L3" (Summary; §Dependencies; §Supporting evidence). The chain is firmly present and correctly cited in `concepts/nested-constructed-operator-gate.md` (Chain 1). However, the firm L3 `eigsolve` entry itself (`book/src/L3/eigsolve.md:62,70,114,134,157`) renders the projector tail as a plain `apply_linop op.projector` (an opaque `LinearOperator`, witnessed `opProj->Mult`), NOT as the `divfree-projector` constructed gate — so at the L3-eigsolve-entry resolution the gate-within-gate nesting is not surfaced. The report does NOT over-claim this (it anchors the chain to the concept page, which is the correct evidence home), so this is not a fail; flagging only so the integrator/repairer is aware the chain's L3 home is the concept page, not the L3 eigsolve chapter, should anyone later try to cross-link them.

**Issue 3 — self-flagged Working-Notes count phrasing (severity: low; producer already surfaced).** The report's own §Open-questions (lines 742-749) flags that its L3-index Working-Notes bullet says "one of the six (A) backfills remains" while the explicit remaining list is three (`reciprocal`, `elementwise_product`, `normalize`). The bullet's parenthetical is internally self-correcting (it then names the three), but the lead phrasing "one ... remains" is awkward/misleading relative to "three remain." The producer correctly routes this to the integrator as a normalization nicety, not a chapter edit. Noted here for completeness; candidate for the same trivial repair pass as Issue 1.

No citation drift, no fence-truncation, no rotation-quality failure, no hidden variant branch, no edge mislabel found. The only substantive finding is the recurring law-count inconsistency (Issue 1).

## Repair

### Fixes attempted

- **Finding (Issue 1)**: "six algebraic laws" miscount recurring in summary-prose, contradicting the entry's own §Algebraic laws list (5 numbered laws + 2 non-laws).
  - **Decision**: repaired.
  - **Action**: Confirmed the true count by reading §Algebraic laws (CYCLE.md lines 326–370): 5 numbered laws (1. Linearity, 2. Idempotence, 3. Range, 4. M-orthogonality, 5. Real-linearity/block-diagonal-complex) + 2 load-bearing non-laws (sign convention, step ordering) — matching the firm L1 home. Corrected every law-count assertion `six → five` (leaving the "two non-laws" intact and the unrelated "six (A) backfills" audit-candidate count untouched), at: frontmatter `inputs:` (CYCLE.md §frontmatter, "five laws + two non-laws"); §Summary (line ~33); §Context "Downward to L1" (line ~148); §Algebraic laws lead (line ~319, "The five laws that hold at L1"); §Status (line ~469); §Lowers to (line ~524); §Evidence L1-entry bullet (line ~575); §L3-vs-L1 distinction (line ~653); §Operator content "Five hold" (line ~700). Verified by grep: all remaining "six" mentions now refer only to the cycle-036 "six (A) backfill candidates" audit count, which is correct and order-independent.
  - **Mechanical bound**: pure `s/six/five/` on law-count assertions; the canonical numbered list (the source of truth) was not touched. No content authored.

- **Finding (Issue 3)**: Working-Notes "one of the six (A) backfills remains" lead phrasing in the proposed `book/src/L3/index.md` dep-map bullet was awkward/misleading relative to the explicit three-name remaining list (`reciprocal`/`elementwise_product`/`normalize`); producer self-flagged.
  - **Decision**: repaired.
  - **Action**: Rewrote the closing sentence of the L3-index Working-Notes bullet (CYCLE.md §"Proposed changes" → `edit:book/src/L3/index.md` block, line ~679) to the accurate framing per the cycle-038 cohort: "Of the six (A) backfills, `reciprocal` / `elementwise_product` / `normalize` remain after this landing (`reciprocal` + `elementwise_product` landing in parallel this cycle-038 cohort, `normalize` held to cycle-039)". Also softened the same bullet's order-dependent ordinal `**fifth** of the six → one of the six`, since the parallel-cohort landing order makes a hard ordinal unstable at author time. The stable, order-independent "one of the six (A) candidates" framings elsewhere (§Status, §Evidence) were left unchanged — they are correct.
  - **Mechanical bound**: replaced an order-dependent / count-asserting phrase with the accurate cohort framing the task specified. No content authored.

- **Finding (Issue 2)**: transitive-chain `eigsolve ⊃ divfree-projector ⊃ ksp_solve` is anchored at the concept page, not the L3 `eigsolve` entry (which renders the projector as plain `apply_linop`); precision note, NOT an over-claim.
  - **Decision**: not-needed (acknowledged).
  - **Rationale**: Verified the report anchors the chain exclusively to `concepts/nested-constructed-operator-gate.md` (CYCLE.md §Dependencies line ~400, §Evidence line ~614, §Supporting-evidence lines ~731–732) — the correct evidence home. No prose reads as if the L3 `eigsolve` chapter directly renders the chain, so the soften-only-if condition does not trigger. No edit applied.

### Unrepairable findings

None. All three findings were either mechanically repaired (Issues 1, 3) or acknowledged with no edit required (Issue 2). No substantive authoring or content decision was needed; the canonical numbered law list and all citations were untouched.

### Fence-parity re-check

`proposed-changes-fence-encloses-full-body-guard`: post-repair fence enumeration unchanged — 6 ```` ``` ```` markers → 3 balanced `edit:` blocks (chapter 50–661, SUMMARY 663–669, L3 index 671–680). All edits modified text strictly inside the existing fences or in out-of-fence report scaffolding; no fence marker was added, removed, or moved. The full firm chapter body (`## Signature` / `## Semantics` / `## Algebraic laws` / `## Status` / `## Evidence`) remains inside the chapter fence. Build-readiness intact.

## Suggested resolution

`ready`. All findings were mechanical and non-blocking; the critic's 8 checks all passed and no finding required substantive authoring. Notes for the integrator:
- The repaired L3-index Working-Notes bullet now states the cohort framing explicitly (`reciprocal` + `elementwise_product` in the cycle-038 cohort, `normalize` held to c039). The integrator should reconcile this against the actual parallel cycle-038 landings before finalize — if the parallel cohort lands differently than stated, adjust the "remain after this landing" list accordingly (the OQ `l3-cohort-growth-audit-c036-verdict` tracks the residual).
- Issue 2 (concept-page-anchored chain) is informational only: should anyone later cross-link the transitive chain into the L3 `eigsolve` chapter, note that chapter renders the projector tail as plain `apply_linop` — the chain's L3 home is the concept page.
