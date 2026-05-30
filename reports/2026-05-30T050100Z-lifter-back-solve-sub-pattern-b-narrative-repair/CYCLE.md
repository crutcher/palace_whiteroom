---
agent: lifter
invoked_at: 2026-05-30T05:01:00Z
scope: L1>L0 theme Sub-pattern B narrative repair — back-solve-mutation-rotation
status: pending
inputs:
  - book/src/L1-L0/back-solve-mutation-rotation.md
  - reference/palace/palace/linalg/iterative.cpp (GMRES :652-660, FGMRES :831-840)
  - book/src/L1/back_solve.md (the L1 leaf the theme lowers; carries the correct "line-for-line identical" phrasing at :223-230)
integrated_at: 2026-05-30T051734Z
integration_commit: 2f9c08d
integration_notes: Applied clean (cycle-031 D2). 5 narrative-only edits to back-solve-mutation-rotation.md §Sub-pattern B prose (:198-244 / :575-580 / :518-521 / :729-731 / :811-814 F1 row flip partially-supports→supports). Theme stays firm — structural decomposition unchanged. Closes c030 OQ back-solve-mutation-rotation-sub-pattern-b-brace-placement-narrative-correction-c030. The wrong "+1-line brace-placement shift" prose corrected to factual byte-identity (+179-line file offset, zero local relative shift).
---

# CYCLE: Re-anchor Sub-pattern B narrative — back-solve-mutation-rotation

## Summary

The firm + integrated L1>L0 theme `book/src/L1-L0/back-solve-mutation-rotation.md` carried a Sub-pattern B narrative asserting a "+1-line brace-placement shift" between the GMRES and FGMRES back-solve arms — claiming GMRES places `{` at the end of the `for` line and FGMRES places `{` on the next line, with the body lines therefore shifted by +1. This claim is **factually wrong**: re-verified this dispatch with `diff`, `cmp`, and `tools/citecheck/`, the two 9-line ranges `iterative.cpp:653-660` (GMRES) and `:832-839` (FGMRES) are **byte-identical**, and the byte-identity extends backward through the entire preceding outer-`for(;;)` break-out epilogue (lines `:645-660` vs `:824-839` are byte-identical, 16-line block). Both arms place `{` on its own line; the body lines `:655→:834`, `:656→:835`, `:657→:836`, `:659→:838` correspond at a uniform +179-line file offset with **zero local relative shift**, and the within-block relative offsets `(0,+2,+3,+4,+6)` from the for-line are byte-identical in both arms. The theme's L1 leaf at `book/src/L1/back_solve.md:225-226` already carries the correct phrasing ("line-for-line identical"); the theme's Sub-pattern B prose, the §"Variant axes" GMRES-vs-FGMRES bullet, the §"Justification kind" Sub-pattern B clause, the §"Status" two-form-bullet, and the §Verified-against `:832` `note` field all need to be re-stated to remove the spurious brace-shift claim and restate the offset correctly as a pure +179-line file offset with byte-identical local content. This is a pure narrative repair within lifter authority (CLAUDE.md "L0-evidence-driven prose correction is in-scope when bounded + evidenced + recorded"): correcting a backward-stated fact, directly supported by L0 citations this dispatch read with `cmp` byte-equality + `citecheck --anchor` zero-drift confirmation, bounded (no decomposition / signature / variant-axis structural change — same four-element rewrite, same two-form recognition), recorded explicitly here. The theme stays `## Status: firm`.

## Proposed changes

```edit:book/src/L1-L0/back-solve-mutation-rotation.md
[old]: ### Sub-pattern B — the FGMRES twin (shape-identical body, line-shifted by brace placement)

    // iterative.cpp:831  "Reconstruct the solution (for restart or due to
    //                     convergence or maximum iterations)."
    for (int i = j; i >= 0; i--)                       // :832  descending sweep
    {                                                  // :833  opening brace on its own line
      ScalarType *Hi = H.data() + i * (max_dim + 1);   // :834  column i of R
      s[i] /= Hi[i];                                   // :835  y[i] = s[i] / R[i][i]
      for (int k = i - 1; k >= 0; k--)                 // :836  super-diagonal column scan
      {                                                // :837  inner brace on its own line
        s[k] -= Hi[k] * s[i];                          // :838  s[k] -= R[k][i] * y[i]
      }
    }

Structurally **identical** to Sub-pattern A — the four-element rewrite is the
same, the register `H` is the same (FGMRES inherits `H` from `GmresSolver`,
`iterative.hpp:250` — `using GmresSolver<OperType>::H`), the registers `s, sn,
cs` are also inherited (`:251-253`), and the stride formula is the same. The
only differences from Sub-pattern A are **purely textual** (lexical brace
placement) and **purely downstream** (the basis the consumer reads):

- **Brace placement / line shift.** GMRES (Sub-pattern A) places `{` at the end
  of the `for` line (one statement on the line); FGMRES (Sub-pattern B) places
  `{` on the next line. This shifts every body line by +1: GMRES `:653`/`:655`/
  `:656`/`:657`/`:659` ↔ FGMRES `:832`/`:834`/`:835`/`:836`/`:838`. The two
  bodies compute identical values; the line offset is a pure brace-style
  artefact. The L1 leaf's law-6 ("back-solve code line-for-line identical")
  is **slightly imprecise**: the LINE NUMBERS differ by +1 (brace shift), but
  the LINE CONTENT (loop bound, stride formula, division, subtraction) is
  byte-identical. This is recorded faithfully here as **content-identical,
  line-shifted** — the rotation is the same; the surface form is brace-style-
  isomorphic but not byte-identical.
- **Downstream basis.** The consuming `linear_combination` lift reads `V[k]`
  in GMRES (`x.Add(s[k], V[k])`, `:666`) and `Z[k]` in FGMRES
  (`x.Add(s[k], Z[k])`, `:843`). This is **outside the leaf** — the basis-lift
  is the L2 `linear-combination` composition consuming the coordinate vector
  `y` (left in `s[0..j]`), not part of `back_solve` itself. The `Z` register
  is declared `mutable std::vector<VecType> Z;` at `iterative.hpp:256` (FGMRES-
  specific — the right-preconditioned Krylov basis `Z[k] = M⁻¹ V[k]`). The
  basis selection is the consuming L2 composition's `op.basis_kind` axis;
  this leaf has no knowledge of it. **The back-solve itself is basis-invariant.**

Justification kind: **structural** — same as Sub-pattern A. This sub-pattern is
recorded explicitly (rather than collapsed into A) because the two-form
recognition is the load-bearing evidence for the L1 leaf's law-6 basis-lift
independence: the body must be the same shape under both downstream basis
readings, and it positively is.

[new]: ### Sub-pattern B — the FGMRES twin (byte-identical body, +179-line file offset)

        // iterative.cpp:831  "Reconstruct the solution (for restart or due to
        //                     convergence or maximum iterations)."
        for (int i = j; i >= 0; i--)                       // :832  descending sweep
        {                                                  // :833  opening brace on its own line
          ScalarType *Hi = H.data() + i * (max_dim + 1);   // :834  column i of R
          s[i] /= Hi[i];                                   // :835  y[i] = s[i] / R[i][i]
          for (int k = i - 1; k >= 0; k--)                 // :836  super-diagonal column scan
          {                                                // :837  inner brace on its own line
            s[k] -= Hi[k] * s[i];                          // :838  s[k] -= R[k][i] * y[i]
          }
        }

**Byte-for-byte identical** to Sub-pattern A — the four-element rewrite is the
same, the register `H` is the same (FGMRES inherits `H` from `GmresSolver`,
`iterative.hpp:250` — `using GmresSolver<OperType>::H`), the registers `s, sn,
cs` are also inherited (`:251-253`), the stride formula is the same, **and the
brace style is the same** (both arms place `{` on its own line — GMRES `:654`
↔ FGMRES `:833` are both bare `{` lines; both arms' inner `{` likewise sits on
its own line at `:658` ↔ `:837`). A `cmp` over the 9-line block
`iterative.cpp:653-660` vs `:832-839` returns identical; a `cmp` extended
backward through the preceding outer-`for(;;)` break-out epilogue
(`:645-660` vs `:824-839`, 16-line block) also returns identical. The only
differences from Sub-pattern A are **purely positional** (the +179-line file
offset between the two arms in `iterative.cpp`) and **purely downstream** (the
basis the consumer reads):

- **+179-line file offset; zero local relative shift.** GMRES `:653`/`:655`/
  `:656`/`:657`/`:659` ↔ FGMRES `:832`/`:834`/`:835`/`:836`/`:838`. The
  per-line correspondence is `653→832 (+179)`, `655→834 (+179)`, `656→835
  (+179)`, `657→836 (+179)`, `659→838 (+179)` — a **uniform +179-line offset
  with zero relative shift**. The within-block relative offsets from each
  arm's for-line `(0, +2, +3, +4, +6)` are byte-identical in both arms; the
  preceding-code offset is also uniform (the preceding `break;` sits at +5
  lines back from each arm's for-line — GMRES `:653 − 5 = :648` `break;` ↔
  FGMRES `:832 − 5 = :827` `break;` — and the byte-identity confirmed by
  `cmp` extends 5 lines into the preceding epilogue at minimum, 16 lines in
  full). **There is NO brace-placement shift between the arms** — the prior
  draft's "+1-line brace-style shift" claim was wrong; both arms use
  brace-on-its-own-line style throughout the block (and indeed throughout
  the whole `iterative.cpp` body). The L1 leaf's law-6 phrasing at
  [`L1/back_solve`](../L1/back_solve.md)`:225-226` ("back-solve code line-for-
  line identical") is **literally correct**: the LINE CONTENT (loop bound,
  stride formula, division, subtraction, brace style) is byte-identical;
  the LINE NUMBERS differ only by the constant +179 file offset.
- **Downstream basis.** The consuming `linear_combination` lift reads `V[k]`
  in GMRES (`x.Add(s[k], V[k])`, `:666`) and `Z[k]` in FGMRES
  (`x.Add(s[k], Z[k])`, `:843`). This is **outside the leaf** — the basis-lift
  is the L2 `linear-combination` composition consuming the coordinate vector
  `y` (left in `s[0..j]`), not part of `back_solve` itself. The `Z` register
  is declared `mutable std::vector<VecType> Z;` at `iterative.hpp:256` (FGMRES-
  specific — the right-preconditioned Krylov basis `Z[k] = M⁻¹ V[k]`). The
  basis selection is the consuming L2 composition's `op.basis_kind` axis;
  this leaf has no knowledge of it. **The back-solve itself is basis-invariant.**

Justification kind: **structural** — same as Sub-pattern A. This sub-pattern is
recorded explicitly (rather than collapsed into A) because the two-form
recognition is the load-bearing evidence for the L1 leaf's law-6 basis-lift
independence: the body must be the same shape under both downstream basis
readings, and it positively is (literally — `cmp` byte-identical).
```

```edit:book/src/L1-L0/back-solve-mutation-rotation.md
[old]: - **GMRES vs FGMRES** (the two-form recognition, Sub-patterns A and B): the
  back-solve body is **content-identical, line-shifted by +1** across the
  two surface sites. The L1 form has no GMRES/FGMRES variant — they are
  the same leaf, recorded twice in source. The basis the downstream
  consumer reads (`V` vs `Z`) is the consuming L2 composition's
  `op.basis_kind` axis (law 6), absorbed at this leaf.

[new]: - **GMRES vs FGMRES** (the two-form recognition, Sub-patterns A and B): the
  back-solve body is **byte-for-byte identical** across the two surface sites
  (`iterative.cpp:653-660` ≡ `:832-839`, `cmp`-confirmed; both arms use the
  same brace-on-its-own-line style — no local relative shift, only a uniform
  +179-line file offset). The L1 form has no GMRES/FGMRES variant — they are
  the same leaf, recorded twice in source. The basis the downstream consumer
  reads (`V` vs `Z`) is the consuming L2 composition's `op.basis_kind` axis
  (law 6), absorbed at this leaf.
```

```edit:book/src/L1-L0/back-solve-mutation-rotation.md
[old]: - **Sub-pattern B** (FGMRES twin) — `structural`. Shape-identical to A
  (content-identical, brace-style line-shifted by +1); the rotation is
  the same. Recorded explicitly to ground the L1 leaf's law-6 basis-lift
  independence.

[new]: - **Sub-pattern B** (FGMRES twin) — `structural`. **Byte-for-byte identical**
  to A (`cmp`-confirmed over `iterative.cpp:653-660` ≡ `:832-839`; same brace
  style throughout; uniform +179-line file offset, zero local relative shift);
  the rotation is the same. Recorded explicitly to ground the L1 leaf's
  law-6 basis-lift independence.
```

```edit:book/src/L1-L0/back-solve-mutation-rotation.md
[old]: - **Both surface forms are positively anchored** (GMRES `:652-660` and
  FGMRES `:831-840`); the two are content-identical, line-shifted by
  brace style, grounding law-6 basis-lift independence.

[new]: - **Both surface forms are positively anchored** (GMRES `:652-660` and
  FGMRES `:831-840`); the two are **byte-for-byte identical** within the
  back-solve body (`cmp` over `:653-660` ≡ `:832-839`; uniform +179-line
  file offset, zero local relative shift, same brace-on-its-own-line style),
  grounding law-6 basis-lift independence.
```

```edit:book/src/L1-L0/back-solve-mutation-rotation.md
[old]:   - citation: palace/linalg/iterative.cpp:832
    verdict: partially-supports
    audited_at: 2026-05-30T010118Z
    note: FGMRES outer descending sweep `for (int i = j; i >= 0; i--)` zero-drift; but the theme narrative claiming a "+1 line-shift from brace placement" is FACTUALLY WRONG (both GMRES and FGMRES place `{` on its own line; diff of :653-660 vs :832-839 is byte-for-byte zero) — repair follow-up noted; the L1 leaf at :225-226 has the correct "line-for-line identical" phrasing.

[new]:   - citation: palace/linalg/iterative.cpp:832
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: 'FGMRES outer descending sweep `for (int i = j; i >= 0; i--)`; byte-for-byte identical to GMRES :653 (cmp over :653-660 ≡ :832-839 zero; brace-on-its-own-line style identical in both arms; uniform +179-line file offset, zero local relative shift). Narrative Sub-pattern B repaired (cycle-031 D2 lifter): the prior "+1-line brace-style shift" claim was wrong — re-stated as byte-identical, +179-line file offset. Matches L1 leaf at L1/back_solve.md:225-226 "line-for-line identical" phrasing. citecheck --anchor zero-drift.'
```

## Discipline notes

This is a **bounded prose correction** within lifter authority (CLAUDE.md §Discipline, "L0-evidence-driven prose correction is in-scope when bounded + evidenced + recorded"). The correction:

- **Is directly supported by L0 citations this dispatch read.** Re-verified `iterative.cpp:653-660` and `:832-839` on-disk via `palace-codemap`-localized `Read` + `citecheck --anchor`; confirmed byte-identity over the 9-line range with `cmp` (and over a 16-line range `:645-660` vs `:824-839` extending into the preceding outer-`for(;;)` break-out epilogue); confirmed via direct read that both arms use brace-on-its-own-line style at the for-line braces (`:654` ↔ `:833`) and at the inner-for braces (`:658` ↔ `:837`). The +179-line file offset is `832 − 653 = 179`; the +5-line preceding-code anchor distance (back-solve `for` to nearest `break;` in the preceding outer-loop epilogue, `:653 − :648 = 5` ↔ `:832 − :827 = 5`) is also uniform.
- **Is bounded.** No decomposition change: still the same four-element rewrite (descending outer sweep / column-major stride / diagonal division / inner column-oriented super-diagonal subtraction), still the same two-form recognition (Sub-patterns A and B), still the same boundary-marker Sub-pattern C, still the same variant-axis set, still the same applicability conditions, still the same `partly-constructive`-vs-`firm` analysis. No signature change to the L1 leaf, no new vocabulary, no relocated citations to terminal homes — every cited line still resolves at the same range. **Status stays `firm`.** Only the **narrative description of the GMRES↔FGMRES correspondence** is corrected from "+1-line brace-shift" to "byte-identical, +179-line file offset, zero local relative shift".
- **Is recorded.** This §Discipline notes block records the correction. The §Verified-against `:832` row is flipped from `partially-supports` to `supports` with a new `audited_at` timestamp and a note that the narrative repair has been applied (replacing the prior "repair follow-up noted" wording).

The L1 leaf at [`L1/back_solve`](../L1/back_solve.md)`:225-226` already carries the correct "back-solve code line-for-line identical" phrasing — the leaf was right, only the L1>L0 theme's Sub-pattern B prose drifted into the wrong "+1 brace-shift" elaboration. The repair aligns the theme back to the leaf's correct statement.

Why "byte-identical, +179-line file offset" and not "byte-identical, +5 from preceding code": both are true and the dispatch prompt mentioned both framings. The narrative chooses "+179-line file offset, zero local relative shift" as the **primary** statement because that's the direct measurable property (`832 − 653 = 179`; `cmp` zero-byte over the body block); the "+5 preceding-code anchor distance" is a **corroborating** detail (the for-line sits at uniform +5 from the nearest `break;` in both arms — same local structure preceding) and is mentioned in the body of the new Sub-pattern B prose as part of the byte-identity-extends-into-preceding-epilogue evidence. The wrong claim being repaired was "+1 brace shift causing per-body-line offset"; the corrected story is "no brace shift, no per-body-line offset, only the constant +179 file offset between the two arms".

Note on fence rendering: the new Sub-pattern B code-snippet sample is rendered as a **4-space-indented code block** (NOT a nested ` ```text ... ``` ` fence) per the cycle-024 fence-truncation guard / skill `convert-nested-fences-to-indented-code-in-proposed-changes-block`. The original Sub-pattern B sample in the on-disk theme also uses 4-space indentation (not a nested fence), so the indentation pattern is preserved on the replacement.

## Supporting evidence

Re-verification this dispatch (citation source-of-truth = on-disk `reference/palace/`, via `cmp` + `citecheck --anchor`):

- `palace/linalg/iterative.cpp:653-660` — GMRES back-solve body (9 lines).
- `palace/linalg/iterative.cpp:832-839` — FGMRES back-solve body (9 lines).
- `cmp <(sed -n '653,660p' …) <(sed -n '832,839p' …)` → byte-identical.
- `cmp <(sed -n '648,660p' …) <(sed -n '827,839p' …)` → byte-identical (extended +5 lines back into the preceding `break;` epilogue, 13-line block).
- `cmp <(sed -n '645,660p' …) <(sed -n '824,839p' …)` → byte-identical (extended +8 lines back into the full `if (converged || …)` outer-break clause, 16-line block).
- `python3 tools/citecheck/citecheck.py reference/palace/palace/linalg/iterative.cpp:653-660 --anchor 'for (int i = j; i >= 0; i--)'` → ok, anchor at 653, zero-drift.
- `python3 tools/citecheck/citecheck.py reference/palace/palace/linalg/iterative.cpp:832-839 --anchor 'for (int i = j; i >= 0; i--)'` → ok, anchor at 832, zero-drift.
- Direct read of `:654` and `:833` → both are bare `{` lines (brace-on-its-own-line style).
- Direct read of `:658` and `:837` → both are bare `{` lines (inner-loop brace-on-its-own-line style).

Cross-references:

- The L1 leaf `book/src/L1/back_solve.md:223-230` law-6 statement uses the correct "back-solve code line-for-line identical (`iterative.cpp:652-660` ≡ `:831-840`)" phrasing — the repair aligns the theme to the leaf.
- The independent cycle-030 verification chain (auditor D1 ran `diff` → zero bytes; abstractor D4 direct read; critic D4) that produced the `:832` `partially-supports` row at `:814` of the on-disk theme — this dispatch consumes that prior verification and acts on its flagged repair condition.
- Convention reference: cycle-024 friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` recurrence-2 + skill `convert-nested-fences-to-indented-code-in-proposed-changes-block` — the 4-space-indented code block (not nested fence) is the correct rendering inside the proposed-changes block.

## Open questions / caveats

- **None.** This is a pure narrative repair: the structural decomposition (four-element rewrite, two-form recognition, sub-pattern A/B/C taxonomy, variant axes, applicability conditions, the partly-constructive-vs-firm analysis, the L1>L0 forward-edge complement with `incremental-least-squares-composition-lowering`) is unchanged; only the textual statement of the GMRES↔FGMRES correspondence is corrected. The theme stays `## Status: firm`. The cycle-030 audit's `partially-supports` flag on `:832` is now fully resolved (the narrative defect it flagged is repaired this dispatch); the corresponding row flips to `supports` with the new audit timestamp.
- **No re-architecture trigger.** Per the CLAUDE.md "Re-architecting re-routes" bullet, the correction does not require changing the entry's decomposition, adding sub-patterns, or changing the L1 leaf's signature. The same 9-line block at GMRES `:653-660` and FGMRES `:832-839` remains the surface; the L1 form `y = back_solve(R, s)` remains the LHS; the four-element rewrite remains the RHS. The correction is exactly the kind of "convention stated backwards / drifted-narrative" repair the bounded-correction policy was codified for.
