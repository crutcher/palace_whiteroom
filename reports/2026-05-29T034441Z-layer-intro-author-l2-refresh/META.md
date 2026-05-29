---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T04:04:34Z
critic_version: 1
checks:
  citation-validity: fail
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: fail
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T04:30:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: repaired
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L2 intro refresh" (layer-intro-author, cycle-020)

## Critique

### Checks run

**citation-validity — fail.** The report's central claim is the firmness survey: **5 firm + 2 stubs**. I read each L2 chapter's status declaration on disk:

- `krylov-step.md:127` → `## Status` / `firm` ✓
- `chebyshev-iteration.md:216` → `## Status` / `firm` ✓
- `linear_combination.md:273` → `## Status` / `firm` ✓
- `inner_product.md:408` → `## Status` / `firm` ✓
- `incremental-least-squares.md:3` → `> **Status: \`stub\`**` ✓
- `ksp_solve.md:3` → `> **Status: \`stub\`**` ✓
- `orthogonalize.md` → **NO status line at all.** The file is 14 lines, preamble-only: a `# orthogonalize` title and one prose paragraph. No `## Status`, no `## Signature`, no Algebraic-laws, no variant-axis section, no Evidence section.

The report's table "On-disk firmness state surveyed (**verbatim from chapter headers**)" (CYCLE.md:22–32) asserts `orthogonalize.md` status is `firm` "verbatim from chapter headers." There is no such header on disk — the verbatim-read claim is false for this row. The `incremental-least-squares`/`ksp_solve` stub rows and the other 4 firm rows are accurate; the `orthogonalize` row is not. The corroborating-evidence pointers were otherwise checked and hold: `variant-absorption.md:131` is in-range (file is 205 lines) and line 131 is exactly the MGS/CGS/CGS2 "absorb at all three levels under residual-axis disclosure" line the row cites; the stub-provenance lines (`ksp_solve.md:9–13`, `incremental-least-squares.md:9–13`) match what the report copied into the dep-map rows; the L0 anchor `L0/linalg-iterative-file.md` exists. The single but load-bearing failure is the unsubstantiated `firm` survey for `orthogonalize`.

**surface-or-evidence — pass.** This is an intro/dep-map refresh (structural), not a refinement of an existing operator's surface, and it carries no rotation_claim. The two emergent motifs accurately reflect the firm entries that DO substantiate them on disk: the fold-cohort do-NOT-merge boundary is pinned in `inner_product.md` (reduce-to-`Scalar`) and `linear_combination.md` (reduce-to-`Tensor[N]`) status/preamble text; the codomain distinction is real. The named-composition motif's *prose description* matches `orthogonalize.md`'s preamble (`project ▷ subtract`, `dot ▷ axpy`, `gs_orthog ∈ {MGS,CGS,CGS2}`, collective-shape residual axis) — the prose is not fabricated. The problem is only the *firm status assertion* attached to that motif's exemplar (see citation-validity and edge-label-fidelity), not the motif content. Pass on this check.

**rotation-quality — pass (not applicable to intro-refresh).** No algebraic/structural rotation is asserted by this report. The dep-map edge-label question is handled under edge-label-fidelity.

**variant-axis-coverage — pass (not applicable to intro-refresh).** No operator/theme with variant axes is being authored or modified; this is a Part overview. The orthogonalize row mentions the `gs_orthog` axis but does not purport to enumerate coverage (that is the chapter's job).

**cross-reference-integrity — warning.** All `[link]` targets resolve except where intentionally plain-text. Verified live: `L2/{krylov-step,chebyshev-iteration,linear_combination,inner_product,orthogonalize,incremental-least-squares,ksp_solve}.md` all exist and are wired into `SUMMARY.md:37–43` (stubs at :42–43, exactly as the report claims); the two stub rows' live links are therefore build-safe. `concepts/incremental-least-squares.md`, `concepts/ksp_solve.md`, `L1/ksp_solve.md`, `L0/linalg-iterative-file.md` all exist. The L3 `ksp_solve` reference is correctly kept plain-text — `L3/ksp_solve.md` does NOT exist on disk (a live link there would break linkcheck2). The warning: the corrected "Sibling fold (constituent, not parent): `inner_product` (firm)" label (CYCLE.md:92) is the *intended* fix of the stale `(rough-in)` label in the live index.md:27 — the firmness re-label of `inner_product` is correct on disk, but `orthogonalize` itself does not carry the firm apparatus its row claims (cross-cutting with edge-label-fidelity); a cross-reference asserting a sibling relationship to a `firm` `orthogonalize` rests on a status the target file does not declare.

**edge-label-fidelity — fail.** The dep-map status column is the edge label here. Five rows assert `firm`; four are faithful to the chapter's on-disk status, but the `orthogonalize` row (CYCLE.md:92, new) carries status ``firm`` (harvested cycle-019; promoted from stub) while `book/src/L2/orthogonalize.md` declares no status and contains no firm apparatus (no Signature/laws/variant-axis/Evidence). The dep-map signature column for that row also advertises `(op: OrthogOp, w: Tensor[N], V: Basis[N, m]) → { residual: Tensor[N], coeffs: Tensor[m] }` and the row narrates laws/consumers as if a firm chapter backed them — the chapter does not. The edge label does not match the chapter's actual maturity-on-disk. (Provenance note for the repairer/integrator: cycle-019's record DID intend `orthogonalize` firm — `log/cycle-019.md:12,36` "L2 firm 3 → 5 (+orthogonalize ...)" — but the cycle-019 integrate commit `efb8a0b` net-removed 5 lines from the stub and never landed the firm body. This is an upstream cycle-019 integrator landing gap; the report faithfully reproduces the *recorded* state but not the *on-disk* state. The intro cannot assert `firm` for a chapter whose firm body is absent.)

**plan-kind-consistency — pass.** The report's kind (intro/dep-map/Working-Notes refresh) matches its content shape. Both `edit:book/src/L2/index.md` proposed-changes blocks are well-formed: the first `[old]` block reproduces the live `index.md:15–27` exactly (Semantics overlay + 5-row dep-map), and the second `[old]` reproduces `index.md:42` exactly — both will match for a clean apply. The new dep-map is 7 rows (5 firm + 2 stub), under the ~20-row promote-to-`dep-map.md` threshold; staying single-file is correct. The Vocabulary-cohort firm/stub split is appropriately scoped (no rough-in tier, correctly noted as deferred). Caveat: this `pass` is conditional on the firm/stub *labels* being correct — the orthogonalize mislabel is recorded under citation-validity and edge-label-fidelity, not double-counted here.

**skill-uptake-survey — pass (telemetry only).** The report references no skill invocation. For a purely-structural intro/dep-map refresh this is acceptable; the shape does not strongly imply a skill (no variant-axis classification, no citation-range verification beyond the one concept-line check, no rotation proposal). Pure presence surface, non-blocking. (Telemetry: a firmness-state survey of this kind is exactly the case where a lightweight "read-each-chapter-status-line" verification would have caught the orthogonalize anomaly — see skill-candidates note below.)

### Issues found

1. **[HIGH — citation-validity, edge-label-fidelity] `orthogonalize` surveyed/labeled `firm`, but on-disk chapter declares no status and carries no firm apparatus.**
   - Where: CYCLE.md:30 (firmness survey table row, claimed "verbatim from chapter headers"); CYCLE.md:71–77 (Vocabulary cohort "Firm at L2" includes `orthogonalize`); CYCLE.md:92 (new dep-map row status ``firm``); CYCLE.md:101 ("`orthogonalize` is now firm"); CYCLE.md:34 ("No rough-in entries currently exist at L2 — the Vocabulary cohort splits firm vs stub").
   - On disk: `book/src/L2/orthogonalize.md` is 14 lines, preamble-only — no `## Status` line (cf. `krylov-step.md:127`, `chebyshev-iteration.md:216`, `linear_combination.md:273`, `inner_product.md:408`, which all carry `## Status` / `firm`), no Signature/Algebraic-laws/variant-axis/Evidence sections.
   - Root cause (for downstream): cycle-019 *recorded* `orthogonalize` as a stub→firm promotion (`log/cycle-019.md:12,36`), but the cycle-019 integrate commit `efb8a0b` net-removed 5 lines (12 ins / 17 del) from the 19-line stub — it stripped the `> **Status: stub**` banner without landing the firm body. The firm chapter content the log describes does not exist on disk. This is an upstream integrator landing gap; the report propagated the recorded state, not the on-disk state.
   - Why it matters: the intro is the navigational source-of-truth for L2 maturity. Asserting `firm` for a chapter with no firm body (and using it as the "named-composition motif exemplar") tells a reader the operator is closed when its signature, laws, variant-axis, and evidence are absent. The "no rough-in cohort" claim and the firm/stub-only cohort split also depend on this status being accurate.
   - Severity HIGH because it is the crux of the dispatch (firmness-state accuracy) and it mis-states the artifact's actual maturity.

2. **[LOW — cross-reference-integrity] Sibling-fold `firm` label on `orthogonalize` is downstream of issue 1.** CYCLE.md:92 corrects the stale `inner_product (rough-in)` → `inner_product (firm)` (correct — `inner_product.md:408` is firm on disk), but the *row this lives in* (`orthogonalize`) asserts a firm status its file does not declare; a reader following the corrected sibling reference lands on a chapter that does not substantiate the firm framing. Not a broken link (the file resolves), but a status-consistency defect inheriting from issue 1.

3. **[INFO — provenance correctness, not a defect to repair here] The report correctly caught the dispatch-brief mislabel of `incremental-least-squares` as firm.** CYCLE.md:31 surveys it as `stub`; disk confirms (`incremental-least-squares.md:3` = `stub`). Recording as a positive: this row of the survey is accurate and the report's flag is correct. No action.

4. **[INFO — plain-text forward-reference correctly handled] L3 `ksp_solve` cross-reference.** CYCLE.md:20,106,121 keep the L3 `ksp_solve` driver/kernel-complementarity reference as plain-text because `L3/ksp_solve.md` is not on disk (confirmed absent; it is a cycle-020 wave-1 proposed-change, not integrated). Correct per the plain-text-when-anchor-missing convention; a live link would break linkcheck2. No action.

## Repair

### Fixes attempted

The two FAIL findings (citation-validity, edge-label-fidelity) and the dependent cross-reference-integrity warning share one root cause: `book/src/L2/orthogonalize.md` is a 14-line intro with no `## Status` / firm body, while this report surveys + dep-maps it as `firm`. The critic's own provenance note (META.md:42, :53) already diagnosed the cause as an **upstream cycle-019 integrator landing gap** (fence-truncation defect — the firm body was authored outside the `edit:` fenced block and never landed), NOT a defect in THIS report's authoring: the report faithfully reproduced the *recorded* firm state.

That recorded state becomes the *actual* on-disk state THIS cycle. A cycle-020 **corrective backfill** — `reports/2026-05-29T034441Z-harvester-orthogonalize-l2-backfill/CYCLE.md` — recovers the full cycle-019-vetted firm body and emits it as one clean `edit:book/src/L2/orthogonalize.md` full-file-replacement (closing fence after the Evidence section). I verified that backfill report:
- It emits a complete firm chapter: `# orthogonalize` intro → `## Context` → `## Signature` → `## Semantics` → `## Algebraic laws` (7 laws + non-laws) → `## Dependencies` → `## Variant axes` → **`## Status` = `firm`** → `## L2 vs L1 distinction` → `## Evidence` (CYCLE.md:51–473).
- Every L0 citation re-verified this dispatch via `palace-codemap read_range` (self-verification log, backfill CYCLE.md:481–501); one off-by-one boundary corrected (`test-orthog.cpp:71-96` → `71-97`).
- It proposes NO change to the dep-map row or `SUMMARY.md` (already `firm` / de-stubbed from cycle-019) — so there is no double-edit conflict with THIS report's dep-map rewrite.

**Integration ordering is therefore load-bearing: the orthogonalize firm-body backfill MUST integrate BEFORE this L2-refresh report.** Once it lands, `book/src/L2/orthogonalize.md` carries `## Status: firm` + Signature + laws + Evidence, and this report's `firm` dep-map row + named-composition-cohort framing + "orthogonalize is now firm" Working Note all become correct against on-disk state. Per the dispatch directive I do NOT downgrade orthogonalize to stub in the intro — that would be wrong (it IS firm post-backfill).

- **Finding 1 (citation-validity FAIL — `orthogonalize` surveyed `firm`, no on-disk status line).**
  - **Decision**: repaired (contingent on integration ordering).
  - **Action**: No edit to THIS report. The `firm` survey row + dep-map row are correct as authored once the co-cycle backfill (`reports/2026-05-29T034441Z-harvester-orthogonalize-l2-backfill/`) lands first. Verified the backfill emits a full firm body with `## Status` = `firm`. The report's other 6 survey rows (4 firm + 2 stub) were independently re-confirmed against disk: `krylov-step.md:125`, `chebyshev-iteration.md:214`, `linear_combination.md:271`, `inner_product.md:406` all carry `## Status` firm; `incremental-least-squares.md:3` and `ksp_solve.md:3` carry `> **Status: stub**`.
  - **Note**: contingent on the orthogonalize firm-body backfill integrating BEFORE this report; the integration ordering is backfill → L2-refresh.

- **Finding 2 (edge-label-fidelity FAIL — dep-map `firm` status column on `orthogonalize` not matched by on-disk maturity).**
  - **Decision**: repaired (contingent on integration ordering).
  - **Action**: No edit to THIS report. The dep-map `firm` edge label (CYCLE.md:92) and the advertised signature `(op: OrthogOp, w: Tensor[N], V: Basis[N, m]) → { residual: Tensor[N], coeffs: Tensor[m] }` match the backfilled firm chapter's `## Signature` (backfill CYCLE.md:109) and `## Status` exactly. The edge label is faithful to the chapter's maturity-on-disk once the backfill lands first.
  - **Note**: same integration-ordering contingency as Finding 1.

- **Finding 3 / cross-reference-integrity warning (sibling-fold `inner_product (firm)` label, downstream of the orthogonalize status).**
  - **Decision**: repaired.
  - **Action**: No edit needed. The corrected `Sibling fold (constituent, not parent): inner_product (firm)` label (CYCLE.md:92) is verified correct against disk — `inner_product.md:406` declares `## Status` firm (the prior stale row at live `index.md:27` read `(rough-in)`; this refresh's re-label is the intended fix). The warning's residual concern — that the sibling reference rests on an `orthogonalize` chapter not declaring `firm` — is dissolved by the backfill landing first (the chapter then substantiates the firm framing the row asserts).

### Unrepairable findings

None. All findings reduce to the single upstream landing gap, which the co-cycle orthogonalize backfill resolves; the resolution requires only correct integration ordering (a sequencing constraint the integrator controls), not substantive re-authoring of THIS report.

The remaining checks the critic passed (surface-or-evidence, rotation-quality, variant-axis-coverage, plan-kind-consistency, skill-uptake-survey) are marked `not-needed` — nothing to repair. The skill-candidate the critic filed (`verify-intro-firmness-survey-against-on-disk-status-lines`) is already in `scaffolding/skill-candidates.md`; left for the meta-phase.

## Suggested resolution

`overall_status: ready` — **with a load-bearing integration-ordering constraint.**

**The integrator MUST apply the orthogonalize firm-body backfill (`reports/2026-05-29T034441Z-harvester-orthogonalize-l2-backfill/`) BEFORE this L2-refresh report.** Ordering: **backfill → L2-refresh.**

Rationale: this report's `firm` survey row, `firm` dep-map edge label, named-composition-cohort framing, and "orthogonalize is now firm" Working Note are all correct against the *post-backfill* on-disk state but NOT against the *current* (pre-backfill) 14-line intro-only state. The backfill recovers the full firm `book/src/L2/orthogonalize.md` (`## Status` = `firm`, Signature, 7 algebraic laws, Variant axes, Evidence — all L0 citations re-verified this dispatch). Once it lands, the two FAILs and the cross-reference warning are all satisfied.

Per-report apply safety for THIS report is clean: both `[old]` blocks match live `index.md` exactly (the first reproduces `index.md:15–27`, the second reproduces `index.md:42`), so the apply is conflict-free regardless of ordering. The backfill touches `book/src/L2/orthogonalize.md` only and proposes NO dep-map / `SUMMARY.md` edit, so there is no write conflict between the two reports — the sole coupling is the semantic ordering (the firm body must exist on disk before this report asserts `firm` for it).

If for any reason the backfill does NOT land this cycle, this report should be held (do not apply a `firm` dep-map row for a chapter with no firm body); but the backfill is a sibling cycle-020 dispatch and is expected to integrate first.
