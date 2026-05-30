---
verifies: ../CYCLE.md
critiqued_at: 2026-05-30T013500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-30T015000Z
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

# META: critique of L1>L0 theme — ls-update-column-mutation-rotation

## Critique

### Checks run

**citation-validity — warning.** Mechanical scan: `python3 tools/citecheck/citecheck.py --scan reports/2026-05-30T010851Z-abstractor-ls-update-column-mutation-rotation/CYCLE.md --quiet` returns `43 ok, 0 failing (43 citations checked)`. Spot-anchor verification on the 19 load-bearing pinpoints (every line in the `Verified-against` block plus the dep-map / SUMMARY insertion targets plus the L1-leaf cross-anchors) confirmed zero-drift on-disk for every literal anchor the producer claimed to have verified — i.e. the producer's self-verification chain is reproducible. HOWEVER, two narrative-prose citation drifts surfaced on anchors the producer did NOT self-verify:
  (i) **`:632` mis-attributed for the `Hj = H.data() + j * (max_dim + 1)` column-handle setup.** Asserted in two prose locations (Justification kind block, line 235; flat-slab block §"The `max_dim + 1` stride", line 444; cited again in §"Verified-against" as part of the `:629-632` range). The on-disk column-handle setup is at **`:629`** (`ScalarType *Hj = H.data() + j * (max_dim + 1);`). Line `:632` is `w *= 1.0 / Hj[j + 1];` (the normalize step). citecheck confirms: `--anchor 'Hj = H.data()'` on `:632` → DRIFT, suggests `:629`. The `:629-632` range citation is OK (range contains the correct line), so the `--scan` check passes; but the singleton "set at `:632`" narrative is wrong, and is repeated three times across the body.
  (ii) **`:617` mis-attributed for the outer-loop `j < max_dim` termination.** §Applicability conditions item 7 says "The outer GMRES loop at `:617` terminates one short of overflow (`j < max_dim`)". Line `:617` is actually `if (print_opts.iterations)`; the loop header is `for (;; j++, it++)` at `:615` (unbounded); and the in-loop restart-exit test is `if (converged || j + 1 == max_dim || it + 1 == max_it) break;` at **`:645`-`:648`**. The literal `j < max_dim` does not occur in `iterative.cpp` at all. `--anchor 'j < max_dim'` on `:617` → NOANC. The narrative claim is wrong on both the line AND the literal text.
  Both drifts are recoverable by re-anchoring (the correct lines are right next door: `:629` for Hj setup, `:645` for the restart-cycle exit test). Surface as a `warning` — they do not undercut the rewrite, but they fail the "every claim has a verifiable citation pointer" invariant.

**surface-or-evidence — pass.** The proposal authors a NEW file (`new:book/src/L1-L0/ls-update-column-mutation-rotation.md`) plus a dep-map row in `L1-L0/index.md` and a SUMMARY entry — pure new-surface, not a refinement of existing operator text. The new-surface IS the L1>L0 theme content (the firm body lives entirely inside the `new:` fence). Out-of-scope for the refinement-shaped trigger.

**rotation-quality — pass.** The rotation is the structural four-element expansion of the L1 closed-form value bundle `{h_out, cs_j, sn_j, s_j, s_jp1, beta}` into four in-place `*PlaneRotation` calls collapsing the L1 fresh result into four already-allocated input registers. The L1>L0 form is strictly LESS abstract (introduces flat column-major slab, `Hj` stride-pointer arithmetic, four reference-update calls, replay-loop strict ordering, write-into-fresh-slot register append for `cs[j]/sn[j]`, in-place RHS overwrite for `s[j]/s[j+1]`) — the rewrite direction is L1 (more abstract, fresh values) → L0 (less abstract, four cycled registers). The destination-collapsed-into-input collapse is a genuine impedance rotation (not a renaming): the L1 form has NO destination buffer in the signature; the L0 form has four. Quality is high.

**variant-axis-coverage — pass.** §Variant axes enumerates the three relevant axes per `classify-variant-axis`: (1) element-type/scalar-kernel-variant (real/complex, absorbed at template instantiation, recorded as L1 law 7); (2) GMRES vs FGMRES (sub-patterns A and B, recorded as byte-identical and tied to L1 law 6); (3) restart-cycle column index `j` (size parameter, loop-bound adaptation). Sub-step-sequence axis explicitly scoped out (no Householder alternative per Palace stub-policy); no collective-reduction axis (no MPI in the leaf); no reduction-strategy axis (the strict ascending replay order is load-bearing per L1 law 2). All hidden branches addressed.

**cross-reference-integrity — pass.** All cross-references resolve: `L1/ls-update-column.md`, sibling themes `back-solve-mutation-rotation` / `orthogonalize-mutation-rotation` / `nrm2-mutation-rotation`, parent L2 `incremental-least-squares.md` + lowering `incremental-least-squares-composition-lowering.md`, and concept pages `givens_generate.md`, `givens_apply.md`, `plane-rotation-stream.md` all exist on-disk. The dep-map insertion target `L1-L0/index.md:33` is the back-solve row (verified); the SUMMARY insertion target `SUMMARY.md:111` is the back-solve entry (verified). Build-readiness fence guard: `grep -n '^```'` yields 6 fences in even pairs (45-856, 858-862, 864-868); the firm body's `## Status` section (lines 792-855) is INSIDE the `new:` fence (855 < 856); all firm apparatus (Slug, L1 form, L0 form, Justification kind, Status, Speculative operators, Supporting evidence, Open questions) lives inside the fence. No nested fences (`^    ```` scan: zero matches) — the body uses 4-space-indented code blocks for L1-form and L0-form samples, exactly per the `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill. No truncation defect. The OQ slug `ls-update-column-mutation-rotation-l1l0-theme-forthcoming-c029` exists in `scaffolding/open-questions.md:984`. Build-readiness clean.

**edge-label-fidelity — pass.** The edge is L1>L0 throughout. Frontmatter `scope: L1>L0 theme sketch`; the file is proposed under `book/src/L1-L0/`; the index-row insertion is into the L1-L0 dep-map; the narrative consistently discusses L1 form → L0 form direction (the rewrite is L1 fresh-bundle → L0 four-call-in-place expansion). No L_{n+1}>L_n label leakage from sibling layers.

**plan-kind-consistency — pass.** Frontmatter declares `status: pending` and the body declares `## Status: firm` (firm-on-positive-structure, exactly matching the L1 leaf and the sibling `back-solve-mutation-rotation` theme). Content shape — exhaustive positive-source anchoring for every law, no negative anchors, no constructive sub-parts, no test-coverage-bounded qualifier needed (the laws are syntactic identities on positive source per the "firm-on-positive-structure escape" in the rough-in-test-coverage-bounded invariant) — matches the `firm` claim. The structural rationale (every rewrite element positively anchored; two surface forms positively cited byte-identical) holds. The `cycle-030+ verified_against audit pending` follow-up flag is a natural lowering-verifier handoff, NOT a status reduction.

**skill-uptake-survey — pass.** The report invokes `classify-variant-axis` (cited in §Variant axes lead and in the L1-form variant note), `verify-citation-range` "Producer self-verification before emitting citations" sub-case (cited in §Verified-against lead with the literal skill reference), `tools/citecheck/citecheck.py --anchor` (the mechanical realization, used and named throughout the verified_against block), and `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (named in OQ-3 for the follow-up L2>L1 forward-reference upgrade). Skill uptake is uniformly visible — no missing-invocation telemetry.

### Issues found

1. **(citation-validity, low-medium severity)** `Hj = H.data() + j * (max_dim + 1)` setup line mis-cited as `:632` in three prose locations:
   - §"L0 form (RHS)" introductory paragraph (line 138): "set at `:632`".
   - §"Justification kind" paragraph (line 235): "set at `:632`, the upstream boundary".
   - §"The flat column-major register `H` + `Hj` stride pointer" §"The `max_dim + 1` stride" (line 444): "(set at `:632` immediately before this leaf's loop, the upstream boundary)".
   The on-disk line is `:629`. The `:629-632` range citation in §Citations and §Verified-against is OK (the range contains the correct line), so `--scan` passes; but the singleton "`:632`" narrative is incorrect by three lines and recurs three times. Repair: re-anchor each "set at `:632`" → "set at `:629`".

2. **(citation-validity, low severity)** §Applicability conditions item 7 (line 562-568): "The outer GMRES loop at `:617` terminates one short of overflow (`j < max_dim`)". Line `:617` is `if (print_opts.iterations)`; the loop header is at `:615` (`for (;; j++, it++)`, unbounded); the restart-cycle exit test is at `:645` (`if (converged || j + 1 == max_dim || it + 1 == max_it) break;`). The literal `j < max_dim` does not occur anywhere in `iterative.cpp` — the in-source test is `j + 1 == max_dim`. Repair: re-anchor "outer GMRES loop at `:617` terminates one short of overflow (`j < max_dim`)" → "outer GMRES restart-cycle exit at `:645` triggers `break` when `j + 1 == max_dim`".

3. **(observational; no check failure)** §"L0 form (RHS)" header-comment line (line 141) reads `// iterative.cpp:632  Hj = H.data() + j * (max_dim + 1);  (column-handle for column j)` — this is the same `:632` mis-attribution shown as an in-prose explanatory comment within a sample code block. Repair as part of issue (1).

4. **(byte-identical claim — independently verified)** No issue. I independently read both source ranges and confirmed byte-identical line-for-line:
   - GMRES `:634-640` and FGMRES `:813-819` are identical character-for-character including brace style.
   - The +179 line offset between the two ranges is from preceding code; no brace-placement difference exists.
   - The report's correction of the sibling `back-solve-mutation-rotation` theme's brace-placement narrative is positively grounded. The OQ-1 follow-up flag (audit back-solve sibling's Sub-pattern B) is well-scoped — the back-solve bodies at `:653-660` and `:832-840` are ALSO byte-identical line-for-line (verified by direct read), so the sibling's "+1 line shift from brace placement" claim is plainly wrong, and the OQ correctly captures the work needed.

5. **(positive observation; not a defect)** The report's `Verified-against` block uses the `verify-citation-range` "Producer self-verification before emitting citations" sub-case end-to-end, with mechanical `--anchor` verification literally cited next to each anchor. 19 of 19 spot-checks reproduce zero-drift on-disk. The producer's self-verification chain is genuine and reproducible, modulo the two narrative-prose drifts in issues (1) and (2) that fell outside the citecheck-verified Verified-against block.

## Repair

### Fixes attempted

- **Finding 1** (citation-validity): `Hj = H.data() + j * (max_dim + 1)` column-handle setup mis-cited as `:632` in three prose locations.
  - **Decision**: repaired.
  - **Action**: re-anchored singleton `:632` → `:629` for the Hj-setup mis-attribution at the three flagged prose locations and at five further occurrences of the same defect that the critic's general directive covers ("only fix the singleton `:632` mis-attributions that should be `:629`"). On-disk verified via `mcp__palace-codemap__read_range` (line :629 is `ScalarType *Hj = H.data() + j * (max_dim + 1);`; line :632 is `w *= 1.0 / Hj[j + 1];` (the normalize step) — the `:629-632` range citations are preserved unchanged per the critic's directive (ranges contain :629, scan-valid). Files/sections edited:
    - `CYCLE.md:139` §"L0 form (RHS)" intro paragraph: "at `:632`:" → "at `:629`:".
    - `CYCLE.md:141` §"L0 form (RHS)" in-block code comment: `// iterative.cpp:632 Hj = ...` → `// iterative.cpp:629 Hj = ...`.
    - `CYCLE.md:236` §"L0 form (RHS)" Justification-kind paragraph: "(set at `:632`, the upstream boundary)" → "(set at `:629`, the upstream boundary)".
    - `CYCLE.md:262` §Citations: "`Hj = H.data() + j * (max_dim + 1);` (`:632`)" → "(`:629`)".
    - `CYCLE.md:429` §"The flat column-major register `H` + `Hj` stride pointer" §"The `max_dim + 1` stride": "(set at `:632` immediately before this leaf's loop)" → "(set at `:629` immediately before this leaf's loop)".
    - `CYCLE.md:580` §"Justification kind" Sub-pattern A summary: "set upstream at `:632`" → "set upstream at `:629`".
    - `CYCLE.md:615` §"Speculative L1 operators": "column-handle setup `Hj = H.data() + j * (max_dim + 1)` at `:632`" → "at `:629`"; coordinated tightening of the adjacent orthogonalize+nrm2 range from `:629-631` → `:630-631` (the upstream-collective sites are :630 `OrthogonalizeIteration` + :631 `Norml2`, no longer overlapping the Hj-setup line).
    - `CYCLE.md:697` §"Verified-against": "column-handle setup `Hj = H.data() + j * (max_dim + 1);` at `:632`" → "at `:629`" (the enclosing `:629-632` range citation preserved unchanged).
    - `CYCLE.md:821` §"Status": "(set at `:632`)" → "(set at `:629`)" for the column-handle pointer arithmetic.
    - `CYCLE.md:505` §"Reduction order" coordinated re-anchor (same family of defect — the producer's mental model placed the Hj setup line inside the upstream-collective range): "the upstream `orthogonalize` and `nrm2` at `:629-631` were the rank-collective sites" → "at `:630-631` were the rank-collective sites" (Hj setup at :629 is NOT a collective site; the collectives are :630 OrthogonalizeIteration + :631 Norml2).
  - **On-disk verification** (`mcp__palace-codemap__read_range palace/linalg/iterative.cpp:610-650` + `tools/citecheck/citecheck.py --anchor`): `--anchor 'Hj = H.data()' :629` → ok at line 629; the singleton `:629` re-anchors are zero-drift.

- **Finding 2** (citation-validity): §Applicability conditions item 7 (`CYCLE.md:563-568`) claimed "outer GMRES loop at `:617` terminates one short of overflow (`j < max_dim`)" — but `:617` is `if (print_opts.iterations)`, the loop header is at `:615` (unbounded `for (;; j++, it++)`), and the restart-cycle exit test is at `:645` (`if (converged || j + 1 == max_dim || it + 1 == max_it) break;`); the literal `j < max_dim` does NOT occur in `iterative.cpp`.
  - **Decision**: repaired.
  - **Action**: rewrote `CYCLE.md:563-568` item 7 to anchor the loop header at `:615` and the restart-cycle exit test at `:645`, replacing the non-existent `j < max_dim` literal with the actual in-source test `j + 1 == max_dim`. The narrative now reads: "The outer GMRES loop header at `:615` (`for (;; j++, it++)`) is unbounded; the restart-cycle exit test at `:645` (`if (converged || j + 1 == max_dim || it + 1 == max_it) break;`) triggers `break` when `j + 1 == max_dim`, terminating one short of overflow and guaranteeing the column-handle `Hj = H.data() + j * (max_dim + 1)` stays in-allocated …". Preserves the semantic claim (loop terminates before `j = max_dim`) while anchoring it to the correct on-disk lines with the correct literal.
  - **On-disk verification** (`tools/citecheck/citecheck.py --anchor`): `--anchor 'for (;; j++, it++)' :615` → ok; `--anchor 'j + 1 == max_dim' :645` → ok. Both anchors zero-drift.

- **Finding 3** (observational; no check failure): same-family `:632` mis-attribution in the §"L0 form (RHS)" in-block code-comment sample (line 141). **Repaired** as part of Finding 1's coordinated re-anchor (the code-comment is the explanatory companion to the §"L0 form (RHS)" intro paragraph and was lifted from the same producer mental-model defect).

- **Finding 4** (byte-identical claim): no issue — the critic independently confirmed the GMRES `:634-640` ≡ FGMRES `:813-819` byte-identity and the back-solve sibling's brace-placement narrative defect. **Not-needed**, no repair action.

- **Finding 5** (positive observation): no issue — Verified-against producer-self-verification chain is reproducible. **Not-needed**, no repair action.

### Post-repair scan

- `python3 tools/citecheck/citecheck.py --scan reports/2026-05-30T010851Z-abstractor-ls-update-column-mutation-rotation/CYCLE.md --quiet` → **43 ok, 0 failing (43 citations checked)** — scan parity preserved.
- All Finding-1 / Finding-2 on-disk re-anchors confirmed via `mcp__palace-codemap__read_range` + `tools/citecheck/citecheck.py --anchor`.

### Unrepairable findings

None. Both flagged citation-fidelity defects were mechanical anchor-drift corrections within repair authority (the correct lines were "right next door" per the critic's directive, and the on-disk truth was confirmed via the codemap before editing).

## Suggested resolution

`ready`. Both citation-validity defects repaired in-place; no substantive content was authored (the rewrite of Finding 2's item 7 preserves the original semantic claim — the loop terminates before `j = max_dim` — and only re-anchors the line numbers and corrects the literal text the original `j < max_dim` mis-quote referred to). The report now uniformly cites `:629` for the Hj-setup line and `:615`/`:645` for the restart-cycle loop bounds, matching on-disk truth. The byte-identical GMRES/FGMRES recognition (independently verified by the critic), the firm-on-positive-structure status, the fence-parity guard, and the cross-reference / dep-map / SUMMARY insertion targets are all undisturbed by these repairs.

Integrator notes:
- The new content is a single `new:book/src/L1-L0/ls-update-column-mutation-rotation.md` file plus a dep-map row insert at `L1-L0/index.md:33` (after `back-solve-mutation-rotation`) and a SUMMARY entry at `SUMMARY.md:111`. All three insertion targets are verified extant.
- OQ closure: this report resolves `ls-update-column-mutation-rotation-l1l0-theme-forthcoming-c029` per dispatch directive.
- The c030+ `lowering-verifier` follow-up audit flagged in §Status is a natural handoff (not a status reduction) — it can be planned for cycle-031+.
- The `cycle-030+` sibling-back-solve brace-placement-narrative correction (Open question 1 in CYCLE.md) is a separate dispatch target on `book/src/L1-L0/back-solve-mutation-rotation.md`; not consumed by this report.
