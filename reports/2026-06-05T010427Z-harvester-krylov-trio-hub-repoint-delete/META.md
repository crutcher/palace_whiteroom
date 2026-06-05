---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T01:28:04Z
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
repaired_at: 2026-06-05T02:05:00Z
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

# META: verification of krylov-trio hub-repoint + slice-corpus deletion (3→0)

## Critique

### Checks run

**citation-validity** — pass. The load-bearing new citation is the arnoldi end-bound reconcile `iterative.cpp:73-118 → :73-109`. Verified against `reference/palace/palace/linalg/iterative.cpp` on disk: line 72 = `template <typename T>`, line 73 = the real-form `inline void GeneratePlaneRotation(const T dx, const T dy, T &cs, T &sn)` signature, the real-form body closes with `}` at **line 109**, line 110 blank, and line 111 = `template <typename T>` introducing the `std::complex<T>` overload (signature at 112-113). So `:73-118` genuinely over-ran into the complex specialization and `:73-109` is the canonical real-form range — the reconcile is correct. The edit-target text at `incremental-least-squares-composition-lowering.md:112` matches on-disk exactly. The firm-home L0 ranges the repoints cite (Sub-pattern B `iterative.cpp:360-486`, Sub-pattern C `iterative.cpp:543-705` / `:563-683`, kernel for-loop `:427-464`) are consistent with the on-disk `ksp-solve-mutation-rotation.md` (Sub-pattern C confirmed at its line 371). No rotation/operator-algebra claims are introduced — this is a hub-repoint + deletion, so the new-citation surface is small and it checks out.

**surface-or-evidence** — pass. This is not a refinement-shaped proposal (no operator/theme surface change carrying a rotation claim) and not a record-definition introduction; it is detritus-GC + citation rehoming. The repoints move slice-range evidence pointers to firm homes that exist on disk (verified: `L2/krylov-step.md`, `L4/krylov-step.md`, `L1/ksp_solve.md`, `L2/ksp_solve.md`, `concepts/sequential-obstruction.md`, `L1-L0/ksp-solve-mutation-rotation.md` all present). Allowed shape.

**rotation-quality** — pass (not applicable). No algebraic/structural/reduction rotation is asserted; this dispatch removes detritus and rehomes citations.

**variant-axis-coverage** — pass (not applicable). No operator with variant axes is being authored.

**cross-reference-integrity** — warning. **The load-bearing inbound-link sweep PASSES**: I ran the independent sweep `grep -rnE '\]\([^)]*slices/(cg|gmres|arnoldi_step)\.md' book/src --include='*.md'` (excluding the slices' own source paths). It returns 30 source lines = 25 Class-A link-occurrences (24 lines; `L0/ksp-factory-file.md:56` carries two links) + 6 corpus rows (SUMMARY.md:292-294, spec/index.md:15-17). I confirmed every Class-A source file/line has a matching `edit:` block, and the inbound `](spec/index.md)` sweep returns exactly two links (SUMMARY.md:291 + introduction.md:23), both removed (the report's discovery of introduction.md:23 as a *second* inbound link beyond SUMMARY.md is correct and well-handled). I then SIMULATED applying all the report's matching edit blocks + the deletes, and re-ran both link sweeps over the simulated tree: **0 surviving inbound `](..slice..)` links and 0 surviving inbound `](spec/index.md)` links** — so the c098-style build-break (linkcheck2 hard error on deletion) does NOT recur; the deletion lands clean. The SUMMARY Part-removal block reproduces exact on-disk text (290-294) and surrounding context (line 289 closes the prior Part, 295 begins `# Concepts`) confirms no orphaned structure. The warning is for two real defects below (non-matching edit old_strings + an overstated completeness claim), neither of which is a build break.

**edge-label-fidelity** — pass. No L_{n+1}→L_n edge label is asserted; the repoints narrate firm-home provenance, and the L2/L3/L4-L3 layer references in the rehomed citations are consistent with the file each edit targets.

**plan-kind-consistency** — pass. Declared as a hub-repoint + deletion (not an operator harvest); content matches — no new operator algebra, only citation rehoming + file deletion + SUMMARY/index removal.

**skill-uptake-survey** — pass. The report performs the c098-lesson inbound-link preflight inline (the relevant procedure for this shape) and notes the campaign-completion implication for `phase-1-slice-reduction-audit` (retire — no corpus left). Telemetry only.

### Issues found

1. **Two edit `old_string`s do not match on-disk → silent apply failure** (`CYCLE.md` Step-1a, the `:131-134` "Working-Notes pattern-instance list" block at CYCLE.md L154-167, and the `:129` "Consumed-by note" block at CYCLE.md L169-176). Severity: **medium** (NON-build-breaking). I mechanically checked all 67 edit blocks against on-disk content: 65 match, these 2 do not. The on-disk `L2/krylov-step.md` contains neither the short-path `    - \`spec/slices/cg.md:103-115\`, \`:172-188\`, \`:393-425\`` indented list nor the `**Consumed-by**: L4 \`iterate_while\` + \`solve-monad\` outer driver (cg.md §L4, gmres.md §L4, ...)` note anywhere in the file (the file's actual lines 129 and 131-134 are in the `## Status` / `## L2 vs L1 distinction` sections with no slice mentions). The report's line-number labels for these two blocks have drifted off a stale copy. Both blocks target **plain-text** slice-range mentions, NOT `](..)` links, so their failure does NOT cause a linkcheck2 break — but they will fail to apply, leaving whatever they intended to repoint untouched, and the producer should either correct the old_strings to current on-disk text or drop the blocks.

2. **Overstated completeness claim re: Class-B plain-text mentions** (`CYCLE.md` Step-2 lead L527 implies the link set is the whole job; Open-questions L761 "all 25 Class-A links + all Class-B mentions repointed ... No partial ... FULL completion"). Severity: **low** (NON-build-breaking; second-source-of-truth hygiene only). The campaign's stated goal eliminates the plain-text slice-anchor "second source of truth," but a substantial residue of plain-text (non-link) slice-range mentions survives untouched after the proposed edits. In `L2/krylov-step.md` alone, lines 58, 79, 81, 86, 117, 120, 121, 172 (plus 9) carry plain-text slice-range citations (`arnoldi_step.md:101-108`, `gmres.md:471-489`, `gmres.md:435-454`, `cg.md:325-339`, `gmres.md:135-150`, `gmres.md:430-454`, `arnoldi_step.md:129-131`, `cg.md:288`, etc.) that no edit block addresses. Across the whole artifact there are ~50 such plain-text mentions (census via `grep -rnE '(cg|gmres|arnoldi_step)\.md:[0-9]' book/src --include='*.md' | grep -vE '\]\('`), some D1-owned (`L4/krylov-step.md:105/152/170/171`), some out of this report's scope (`L2-L1/krylov-step-kernel-defusion.md`, `L4/iterate-while*.md`), and many of which are deliberate frozen "Original pre-reduction slice ranges" historical-provenance narration. None break the build (plain text resolves to nothing on deletion). The defect is the FALSE "all Class-B mentions repointed / FULL completion" assertion, not the residue per se — the report should scope its completeness claim to the inbound-link set (which IS complete) and either enumerate the Class-B residue it leaves for a follow-up or soften the "no partial" language.

3. **Section-title near-miss in the sequential-obstruction repoints** (multiple Step-1 blocks reference `concepts/sequential-obstruction.md` §"MGS as sequential-obstruction"). Severity: **info** (non-blocking). The on-disk heading is `## Example: MGS as sequential-obstruction` (line 37); the repoints use prose `§"MGS as sequential-obstruction"` (no `#anchor` fragment link), so there is no broken anchor — the prose reference is close enough to navigate. Noting only so the repairer/integrator does not "fix" it into a broken `#mgs-as-sequential-obstruction` fragment.

**Confirmed clean (no issue):** (a) the R1 surgical clause-drop at `L2/krylov-step.md:7` matches on-disk as a contiguous substring and the replacement preserves the CG firm-home clause (§Evidence + Sub-pattern B lowering) while dropping only the slice-range clauses — surgical preservation verified; (b) the arnoldi reconcile is exactly correct against source (real-form body-close 109, complex overload 111); (c) the Class-A consumer-bullet repoints point at `L2/krylov-step.md`, which names CG/GMRES/Arnoldi as canonical instances (verified at its §Context line 7 + the variant/auxiliary discussion); (d) the spec/index.md deletion + `# Phase 1 corpus` SUMMARY removal is clean with no orphaned structure (option-(a) full removal; the report appropriately flags this as a producer judgment with the (b) stub fallback for the integrator); (e) the report does NOT touch `L4/krylov-step.md` (0 edit/delete blocks — D1's territory) and does NOT touch the frozen `meta-reviews/*` (0 blocks) — hard constraints honored. The `gmres.md:3` repoint's added `[ksp_solve](../L2/ksp_solve.md)` link resolves.

---

## Repair

### Fixes attempted

- **Finding (critic issue 1)**: Two edit `old_string` blocks (`:131-134` Pattern-instances sub-list + `:129` Consumed-by note) do not match on-disk `book/src/L2/krylov-step.md` → silent apply failure.
  - **Decision**: repaired.
  - **Action** (CYCLE.md Step-1a, the two blocks at the former L154-167 + L169-176): I grepped `book/src/L2/krylov-step.md` for `cg.md`/`gmres.md`/`arnoldi_step.md` plain-text mentions and confirmed it contains neither the indented `    - \`spec/slices/cg.md:103-115\`, …` Pattern-instances list nor the `**Consumed-by**: … (cg.md §L4, …)` note. I then located the intended Class-B mention: BOTH quoted texts exist VERBATIM on-disk in **`book/src/L2/index.md`** — `:129` (Consumed-by) and `:131-134` (Pattern-instances), matching the block `old_string`s exactly (Read-verified). The defect was purely a wrong **file-path label** in the two `edit:` headers (`book/src/L2/krylov-step.md` → should be `book/src/L2/index.md`); the producer's own Open-questions note (CYCLE.md "`L2/index.md:131-134` … repointed in step 1a … in my scope per the dispatch's `L2/index.md` listing") corroborates `L2/index.md` was the intended target and is in scope. Surgical fix: corrected both `edit:` block headers to `book/src/L2/index.md` (the `old_string`/`replace with` bodies were already correct + on-disk-matching for that file, repoint intent preserved). The repointed bodies drop the slice mentions to firm homes and introduce no new `](..)` links, so the build stays clean.

- **Finding (critic issue 2)**: Overstated completeness claim — report asserts "all Class-B mentions repointed / FULL completion / no partial," but ~50 plain-text slice-range mentions survive.
  - **Decision**: repaired.
  - **Action**: Softened the two overstated assertions to be accurate. (i) CYCLE.md §Summary "This is a FULL completion …" → now scopes the claim to the BUILD-CRITICAL / mechanical-completion criterion (31 inbound markdown links repointed/removed, 3 slices deleted, SUMMARY/spec-index removed, slices reachability-GC-unreachable, rank invariant holds with zero slice nodes), and explicitly states ~50 plain-text evidence-provenance mentions remain as stale-but-harmless pointers (same KIND as the `meta-reviews/*` historical-mention convention), flagging them as a tracked follow-up. (ii) CYCLE.md §Open-questions "No partial. … all Class-B mentions repointed … Nothing deferred" → rewritten to state build-critical completion is full + a scoped correction that Class-B link coverage is a subset only, and ADDED a dedicated "TRACKED FOLLOW-UP for batch-31 meta-phase — residual Class-B plain-text-mention cleanup" Open-questions item (with the census grep) directing the meta-phase to MIGRATE it into the plan and decide between (a) a dedicated cleanup pass into batch-32 or (b) accept-as-historical-provenance.

- **Finding (critic issue 3, info)**: Section-title near-miss `§"MGS as sequential-obstruction"` (prose, not a `#anchor` fragment) vs on-disk `## Example: MGS as sequential-obstruction`.
  - **Decision**: not-needed. The critic explicitly noted this is non-blocking (prose reference, no broken anchor) and warned the repairer NOT to "fix" it into a broken `#mgs-as-sequential-obstruction` fragment. Left untouched as directed.

### Unrepairable findings

None. Both real defects were mechanical/surgical and within repair authority: issue 1 was a wrong-file-path label on an otherwise on-disk-matching edit block (corrected to the verified-correct file); issue 2 was an overstated-claim softening + a tracked-follow-up Open-questions item (no substantive authoring — the repoint content is unchanged, only the completeness framing was scoped down to what the proposed edits actually accomplish).

## Suggested resolution

`ready`. The warning's load-bearing portion — inbound-link completeness — PASSED under the critic's own apply-simulation (0 surviving inbound `](..slice..)` links, 0 surviving inbound `](spec/index.md)` links), so the build is clean and the campaign's mechanical-completion criterion (corpus 3→0) is MET. The two repaired defects were non-build-breaking. Notes for the integrator:
- The two corrected blocks now target `book/src/L2/index.md:129` + `:131-134` (was mislabeled `book/src/L2/krylov-step.md`); the `old_string`s match that file on-disk.
- The campaign-COMPLETE flag stands: retire the `annotated-and-retained` carve-out + skill `phase-1-slice-reduction-audit` (no corpus left) — for integrator-finalize / batch-31 meta-phase, as the report flags.
- A NEW tracked follow-up is in the report's Open questions: the residual ~50 Class-B plain-text slice-range mentions (NON-build-breaking) for the batch-31 meta-phase to migrate (dedicated cleanup pass vs accept-as-historical-provenance). This does NOT gate this cycle's completion.
- Per critic issue 3: do NOT convert the prose `§"MGS as sequential-obstruction"` references into `#anchor` fragment links (the on-disk heading is `## Example: MGS as sequential-obstruction`; a fragment link would break).
