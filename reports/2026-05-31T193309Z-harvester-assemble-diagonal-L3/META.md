---
verifies: ../CYCLE.md
critiqued_at: 2026-05-31T19:39:31Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-31T19:45:00Z
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

# META: verification of "Formalize assemble-diagonal at L3"

## Critique

### Checks run

**citation-validity — warning.** `citecheck.py --scan` reports 18 ok / 0 failing (all in bounds, all reference paths resolve). I independently anchor-verified every load-bearing L0 pinpoint on-disk. Ten of eleven pass cleanly: `hypre.cpp:88` (`hypre_CSRMatrixExtractDiagonal`), `operator.cpp:25-28` (`MFEM_ABORT`), `operator.cpp:85-96` (`AssembleDiagonal`), `fem/libceed/operator.cpp:139` (`CeedOperatorLinearAssembleAddDiagonal`), `fem/libceed/operator.cpp:120` (`MFEM_VERIFY`), `jacobi.cpp:75-82`, `chebyshev.cpp:170-178`, `rap.cpp:467-479` (`ComplexParOperator::AssembleDiagonal`), and `test-libceed.cpp:367-376` (`rtol`) all return OK. The artifact-internal pointers (`book/src/L3/index.md:38-43`, `:39`, `:12`) verify: the (A) identity-in-form verdict the report leans on is exactly at index.md:39 and is quoted faithfully ("structurally identical to the firm `apply_linop` opaque-operator-gate precedent, with the exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law"). The L1 home (`book/src/L1/assemble-diagonal.md`) is firm, carries six laws + four non-laws, and the one-orthogonal-(element-type) + one-absorbed-(operator-representation) variant profile — all transported verbatim into the L3 entry, so the inheritance claims are sound. The single exception drives the warning: see Issue 1.

**surface-or-evidence — pass.** This is a refinement-shaped proposal in the permitted retroactive/layer-coherence sense, not a surface-modifying rotation of an existing entry: it authors a *new* L3 chapter that is value-thread-isomorphic to the firm L1 home, mandated by the "Identity-lowerings still require both L levels" invariant. The six laws + four non-laws are reproduced from L1 (CYCLE.md:94-106) and match the L1 home (L1:47-59) essentially word-for-word; the load-bearing exact-vs-approximate caveat is carried as a recorded non-law, not a status reduction. No surface of an existing operator is silently mutated. Pass.

**rotation-quality — pass (not-applicable-as-compaction-rotation by design).** The report explicitly does NOT assert an algebraic/structural compaction rotation; it asserts an **identity-in-form** L3>L1 hop (CYCLE.md:56, 84, 108, 158, 198). Per the methodology invariant, an identity-in-form backfill is expected to be 1:1 on the primitive's signature — the rotation-quality "renaming-only = fail" rule does not bite here because the entry is correctly framed as a layer-coherence backfill, not a claimed compaction. The substantive rotation (CYCLE.md:160) is correctly located at the L1>L0 `assemble-diagonal-mutation-rotation` theme, not claimed here. Pass.

**variant-axis-coverage — pass.** The two-axis profile (one orthogonal `element-type`; one absorbed `operator-representation` = sparse-CSR | matrix-free | parallel-wrapped | complex-wrapped) matches the L1 home exactly (verified against L1:77-89). The frontmatter `variant_axes` (CYCLE.md:37-39), §Variant-axes body (CYCLE.md:128-146), and the non-axes (transpose-mode, abs-vs-signed, partial-domain-abort) are all explicitly scoped — no hidden branches. The transpose-mode non-axis is correctly justified by the transpose-invariance non-law. Pass.

**cross-reference-integrity — pass.** Ran the fence-encloses-full-body guard: the proposed-changes block has even fence parity (6 fences → 3 balanced `edit:` blocks at CYCLE.md:28-201, 203-208, 210-213). The firm apparatus (`# assemble-diagonal` :42, `## Signature` :60, `## Algebraic laws` :90, `## Status` :148, `## Evidence` :170) is ENTIRELY inside the first fence (28-201). The signature is 4-space-indented (CYCLE.md:62-63), NOT a nested ```text fence — there are zero nested triple-backtick fences inside the body. The cycle-019/021/024/036 fence-truncation defect is NOT present. Link resolution: `assemble-diagonal-mutation-rotation.md` (L1>L0) exists and is registered at SUMMARY.md:114, so the in-chapter live links to it are valid; `apply_linop`, `variant-absorption`, `sequential-obstruction` all resolve. `reciprocal.md`/`elementwise_product.md` do NOT exist on disk and are correctly referenced as plain text / inline-code (CYCLE.md:122, 236), not live links — no `linkcheck2` hazard. The SUMMARY.md insert (CYCLE.md:203-208) anchors on the real krylov-step/apply_linop/axpy block (SUMMARY.md:21-23), inserting the new row between apply_linop and axpy — well-formed. The index.md dep-map row append (CYCLE.md:210-213) anchors on the real apply_linop row (index.md:22). Pass.

**edge-label-fidelity — pass.** The edge discussed throughout is L3>L1 (identity-in-form), with the L3>L1 hop explicitly direct (no interposed L2 entry, no L3-L2/L3-L1 theme directory). Prose, frontmatter `lowers_to`, §Lowers-to, and §"L3 vs L1 distinction" all consistently discuss the L3↔L1 edge; the L3↔L4 ("Lifts from", no-L4-entry) edge is separately and correctly handled. No edge-label/prose mismatch. Pass.

**plan-kind-consistency — pass.** Declared `firmness: firm` (frontmatter CYCLE.md:32; §Status CYCLE.md:148-154). The content shape supports firm: firm L1 home + syntactic-identity laws on the matrix-diagonal map — the `apply_linop` "firm-on-positive-structure" situation (correctly distinguished from the `eigsolve`-convergence-semantics test-gated situation at CYCLE.md:152). The entry is authored in L3 vocabulary (high→low: signature/laws/variant-axes in L3 terms with upward/downward references), per the "Layers are defined high→low" invariant. The non-adjacent identity is annotated in-line; no `L3-L1/`/`L3-L2/` directory is created (CYCLE.md:160). No rough-in placeholders inside a firm-claimed body. Pass.

**skill-uptake-survey — warning.** The report references skill-shaped procedures by behavior but does not name the canonical skills its shape implies. It claims producer-side citation self-verification "via `tools/citecheck/citecheck.py --anchor`" (CYCLE.md:224, 231) — that is the `verify-citation-range` mechanical realization, but the skill is not named. The proposed-changes block is exactly the shape the `proposed-changes-fence-encloses-full-body-guard` / `convert-nested-fences-to-indented-code-in-proposed-changes-block` skills govern (4-space-indented signature inside the fence), and the SUMMARY.md insert is the `summary-md-surgical-insert` shape — none are referenced by name. Pure telemetry; non-blocking. See Issue 3.

### Issues found

**Issue 1 (citation-validity, warning) — `rap.cpp:165` anchor-mismatch / over-stated self-verification claim.** CYCLE.md:70 (and the Evidence entry CYCLE.md:185, and the self-verification roll-up CYCLE.md:231) quote the FULL two-line statement `MFEM_VERIFY(&trial_fespace == &test_fespace, "Diagonal assembly is only available for square ParOperator!")` and cite it as `palace/linalg/rap.cpp:165`. On-disk, line 165 is `MFEM_VERIFY(&trial_fespace == &test_fespace,` and the message string `"Diagonal assembly is only available for square ParOperator!"` is on line **166**. `citecheck.py rap.cpp:165 --anchor "Diagonal assembly is only available for square"` returns `[DRIFT]`; the same anchor against `:165-166` (or `:160-175`) returns OK. The cited condition `&trial_fespace == &test_fespace` (the load-bearing square-precondition predicate the prose emphasizes) IS on line 165, so the pinpoint is defensible as the statement's first line, but the citation should be `rap.cpp:165-166` to cover the quoted message. Severity is low (single-line under-citation of a two-line statement, both lines load-bearing). The secondary, slightly more material part: the report's blanket claim that ALL load-bearing L0 citations "re-verified on-disk via `tools/citecheck/citecheck.py --anchor` ... all pass" (CYCLE.md:224, 231) is **not** literally true for the message-string anchor at `:165` — it returns DRIFT until widened to `:165-166`. Candidate repair: widen the citation to `rap.cpp:165-166` at CYCLE.md:70, :185, :231.

**Issue 2 (plan-kind-consistency / cross-reference-integrity, informational — non-blocking).** The §"Open questions / caveats" (CYCLE.md:237) flags for the integrator a Working-Notes count bump from "9 firm + 2 partial-obstruction" (index.md:50) to "10 firm + 2 partial-obstruction". The current index.md:50 text confirms "9 firm + 2 `partial-obstruction`", so the bump arithmetic is correct (this entry is the 10th firm). The report correctly does NOT author that count bump itself (defers to integrator/layer-intro-author domain). No defect — recorded only so the integrator does not lose the flag; the dep-map row append + SUMMARY insert are the only index/SUMMARY changes this report authors.

**Issue 3 (skill-uptake-survey, warning — telemetry only).** No skill is referenced by name despite the report's shape implying at least four: `verify-citation-range` (the `--anchor`/`--scan` self-verification it describes performing), `proposed-changes-fence-encloses-full-body-guard` / `convert-nested-fences-to-indented-code-in-proposed-changes-block` (the 4-space-indented-signature-inside-fence discipline it followed correctly), and `summary-md-surgical-insert` (the SUMMARY.md insert shape). The procedures appear to have been followed (the artifact is clean on those axes); only the by-name invocation reference is absent. Non-blocking surface telemetry.

## Repair

### Fixes attempted

- **Finding**: Issue 1 (citation-validity, warning) — `rap.cpp:165` anchor-mismatch. The quoted message string `"Diagonal assembly is only available for square ParOperator!"` lives on line **166**; line 165 holds only the predicate `&trial_fespace == &test_fespace`. `citecheck --anchor` returns `[DRIFT]` (+1) at `:165`; OK at `:165-166`. The blanket "all anchors pass via `--anchor`" self-verification claim was consequently not literally true for the message-string anchor.
  - **Decision**: repaired.
  - **Action**: Verified the source of truth on-disk (`reference/palace/palace/linalg/rap.cpp:165-166` — confirmed :165 = `MFEM_VERIFY(&trial_fespace == &test_fespace,`, :166 = `"Diagonal assembly is only available for square ParOperator!");`). Re-ran `tools/citecheck/citecheck.py --anchor` on both ranges: `:165` → `[DRIFT] +1 → suggested :166`; `:165-166` → `[ok]` (anchor at line 166 within range). Widened the citation `:165` → `:165-166` at all three instances the critic located:
    - CYCLE.md §Signature (~line 70) — added "predicate at :165, message string at :166" parenthetical.
    - CYCLE.md §Evidence (transitive L0 list, ~line 185) — widened range + noted predicate/message split.
    - CYCLE.md §Supporting evidence / self-verification roll-up (~line 231) — widened range AND softened the blanket "all pass" claim to "all pass after one widening — the AMR square-precondition citation was widened from `:165` to `:165-166` to enclose the message-string anchor", so the claim is now accurate.
  - All other ten load-bearing anchors the critic independently checked already pass clean; no other citation touched.

- **Finding**: Issue 3 (skill-uptake-survey, warning) — report did not name the canonical skills (`verify-citation-range`, fence guards, `summary-md-surgical-insert`) whose procedures it evidently followed.
  - **Decision**: acknowledged / not-needed (no edit).
  - **Rationale**: Pure telemetry, explicitly non-blocking per the critic. The procedures WERE followed (the artifact is clean on the fence-parity, SUMMARY-insert, and citation-self-verification axes — confirmed during this repair: fence parity holds at 6 fences / 3 balanced `edit:` blocks, signature is 4-space-indented not a nested fence). Naming the skills is authoring telemetry the repairer does not retroactively insert into a producer's report; it is not a content defect. No edit required.

- **Finding**: Issue 2 (informational, non-blocking) — integrator Working-Notes count-bump flag.
  - **Decision**: not-needed (no defect; the critic recorded it as informational only, and the report correctly defers the count bump to the integrator/layer-intro-author domain).

### Post-repair integrity check

- Fence parity re-verified after edits: 6 triple-backtick fences (CYCLE.md:28/201, 203/208, 210/213) → 3 balanced `edit:` blocks; firm body fully enclosed in the first fence; signature still 4-space-indented (no nested fence introduced). The `proposed-changes-fence-encloses-full-body-guard` shape holds.
- All three citation edits land inside prose (inside the first `edit:` fence at :70/:185, and in non-fenced supporting prose at :231) — no fence boundary moved.

### Unrepairable findings

None. The one substantive warning (citation-validity) was mechanically repairable (citation-range widening + accuracy-softening of the self-verification claim); the skill-uptake warning is telemetry, not a content defect.

## Suggested resolution

`ready` (clean after repair). The citation-validity warning is resolved: the AMR square-precondition citation now reads `rap.cpp:165-166` everywhere and `citecheck --anchor` resolves clean on the widened range; the self-verification roll-up now accurately states the one widening rather than an over-broad "all pass". The skill-uptake warning is acknowledged telemetry only. Integrator note: the §"Open questions / caveats" Working-Notes count-bump flag ("9 firm + 2 partial-obstruction" → "10 firm + 2 partial-obstruction" at `book/src/L3/index.md:50`) is correct arithmetic and is the integrator/layer-intro-author's to apply; the report correctly does not author it.
