---
agent: lowering-verifier
invoked_at: 2026-05-30T053000Z
scope: L1>L0 theme additive re-audit — back-solve-mutation-rotation (cycle-032 D2; closes c031 D2 lifter narrative-repair loop)
status: pending
integrated_at: 2026-05-30T060748Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied by integrator-per-report at 2026-05-30T060500Z; finalized cycle-032. Additive second `verified_against:` yaml block appended to book/src/L1-L0/back-solve-mutation-rotation.md at chapter :888-912 (after c030 baseline 22-row block at :796-886). 4 rows (GMRES body :653-660, FGMRES body :832-839, GMRES brace :654, FGMRES brace :833), all `supports`, audited_at: 2026-05-30T053000Z. Confirms GMRES at :653-660 byte-identical to FGMRES at :832-839 with +179-line file offset NOT brace placement. Theme stays `firm`. Proper ` ```yaml ` fence (the c030 channel-format refinement `verified-against-note-no-leading-quote-of-either-kind` held; the c031-fence-form lift held; no `~~~yaml` substitution). YAML round-trip on landed block = 4 rows all `supports`, note first-chars G/F/G/F. Closes c031 D2 lifter narrative-repair loop.
inputs:
  - book/src/L1-L0/back-solve-mutation-rotation.md (post-c031 D2 narrative-repair state)
  - reference/palace/palace/linalg/iterative.cpp:653-660 (GMRES back-solve body)
  - reference/palace/palace/linalg/iterative.cpp:832-839 (FGMRES back-solve body)
  - reference/palace/palace/linalg/iterative.cpp:645-660 / :824-839 (16-line extended block)
  - reference/palace/palace/linalg/iterative.cpp:654 / :833 (paired outer opening braces)
  - reference/palace/palace/linalg/iterative.cpp:648 / :827 (paired preceding `break;` statements)
  - reports/2026-05-30T010118Z-lowering-verifier-back-solve-mutation-rotation-audit/CYCLE.md (c030 baseline 22-row audit; not re-audited here, referenced as already-applied baseline)
  - reports/2026-05-30T050100Z-lifter-back-solve-sub-pattern-b-narrative-repair/CYCLE.md (c031 D2 narrative repair that this dispatch closes the loop on)
---

# CYCLE: Additive re-audit `back-solve-mutation-rotation` (c032 D2 — closes c031 D2 lifter narrative-repair loop)

## Summary

Targeted re-verification of the 5 narrative sites in `book/src/L1-L0/back-solve-mutation-rotation.md` that the **cycle-031 D2 lifter narrative-repair** changed, plus the verified_against row it flipped at `:832` (partially-supports → supports). The c031 D2 repair corrected a wrong "+1-line brace-placement shift" claim to "byte-for-byte identical, +179-line file offset, zero local relative shift." This dispatch INDEPENDENTLY re-verifies that the corrected narrative now matches the actual Palace source on-disk.

**Core factual claim re-verified independently:** GMRES `palace/linalg/iterative.cpp:653-660` and FGMRES `:832-839` are **byte-for-byte identical**. Three orthogonal mechanical checks all confirm:
1. `cmp <(sed -n '653,660p' ...) <(sed -n '832,839p' ...)` returns 0 (byte-identical).
2. `diff` over the same two ranges exits 0 (no character difference).
3. Per-line `tools/citecheck/citecheck.py --anchor` zero-drift on every paired anchor (`:653`/`:832` for-line, `:655`/`:834` stride, `:656`/`:835` divide, `:659`/`:838` subtract).

Extended 16-line cmp over `:645-660` ≡ `:824-839` (the back-solve body plus the preceding outer-`for(;;)` break-out epilogue) is **also byte-identical** — the byte-identical region is at least 16 lines wide, confirming the theme's "byte-identity extends 5 lines into the preceding epilogue at minimum, 16 lines in full" claim. The +179-line file offset (`832 − 653 = 179`) is uniform across every paired anchor; per-line correspondence `(653→832, 655→834, 656→835, 657→836, 659→838)` is constant `+179` with zero local relative shift.

Whole-file brace-style check: `grep -cE '(for|if|while|else)\s.*\{$' iterative.cpp` returns **0** — there are NO K&R-style braces in the entire file. The whole file uses Allman (brace-on-its-own-line) style. This corroborates the c031 D2 narrative's generalization "throughout the whole `iterative.cpp` body" (theme line 238). The repaired narrative is accurate not just locally at `:654`/`:833` but as a file-wide property.

**Verdict: fully-supported.** All 5 repaired narrative sites match on-disk Palace source. The c031 D2 `:832` row flip from partially-supports to supports is independently confirmed. This dispatch closes the c031-repair loop and is **additive** to the c030 22-row baseline audit (which I do NOT re-audit here, per dispatch scope — it remains the authoritative prior round).

## Per-citation audit

### Site 1 — Sub-pattern B header (theme line 198)

- **Theme claim** (line 198): `### Sub-pattern B — the FGMRES twin (byte-identical body, +179-line file offset)`
- **Cited evidence**: `palace/linalg/iterative.cpp:653-660` ≡ `:832-839`
- **Found**: cmp returns 0 (byte-identical); diff exit 0. `832 − 653 = 179`. Confirmed.
- **Verdict**: supports
- **Notes**: The c030 baseline audit's header read "FGMRES twin (+1-line brace-style shift, content-identical)"; the c031 D2 repair changed it to the now-confirmed "byte-identical body, +179-line file offset." On-disk source matches the corrected header.

### Site 2 — Sub-pattern B prose with prior-draft retraction (theme lines 222-243)

- **Theme claim** (lines 226-243):
  - "+179-line file offset; zero local relative shift" — per-line correspondence `653→832 (+179), 655→834 (+179), 656→835 (+179), 657→836 (+179), 659→838 (+179)`.
  - "within-block relative offsets from each arm's for-line `(0, +2, +3, +4, +6)` are byte-identical in both arms."
  - "preceding-code offset is also uniform (the preceding `break;` sits at +5 lines back from each arm's for-line — GMRES `:653 − 5 = :648` `break;` ↔ FGMRES `:832 − 5 = :827` `break;` — and the byte-identity confirmed by `cmp` extends 5 lines into the preceding epilogue at minimum, 16 lines in full)."
  - **Explicit retraction**: "There is NO brace-placement shift between the arms — the prior draft's `+1-line brace-style shift` claim was wrong; both arms use brace-on-its-own-line style throughout the block (and indeed throughout the whole `iterative.cpp` body)."
  - "L1 leaf's law-6 phrasing at `L1/back_solve.md:225-226` (`back-solve code line-for-line identical`) is literally correct."
- **Cited evidence**: `palace/linalg/iterative.cpp:653-660` ≡ `:832-839` for byte-identity; `:645-660` ≡ `:824-839` for the 16-line extended; `:648` ↔ `:827` for the paired `break;`; iterative.cpp whole-file for Allman style.
- **Found**:
  - Within-block offsets `(0,+2,+3,+4,+6)`: confirmed. `653→655 = +2, 653→656 = +3, 653→657 = +4, 653→659 = +6`; same offsets from `:832`.
  - Paired `break;` lines:
    - GMRES `:648` content: `        break;` ✓
    - FGMRES `:827` content: `        break;` ✓
    - `832 − 827 = 5` ✓ (+5-back distance matches GMRES `653 − 648 = 5`).
  - Extended cmp over `:645-660` vs `:824-839` (16 lines): byte-identical (cmp returns 0).
  - Whole-file Allman style: `grep -cE '(for|if|while|else)\s.*\{$' iterative.cpp` returns 0; the file uses Allman style throughout.
  - The "prior draft's `+1-line brace-style shift` claim was wrong" retraction is the right framing — there is no brace-style shift.
- **Verdict**: supports
- **Notes**: This is the load-bearing repaired site. Every sub-claim independently confirmed against on-disk source. The retraction phrasing is explicit and accurate.

### Site 3 — §Variant axes GMRES-vs-FGMRES bullet (theme lines 591-594)

- **Theme claim** (lines 591-594): "the back-solve body is byte-for-byte identical across the two surface sites (`iterative.cpp:653-660` ≡ `:832-839`, `cmp`-confirmed; both arms use the same brace-on-its-own-line style — no local relative shift, only a uniform +179-line file offset)."
- **Cited evidence**: same `:653-660` ≡ `:832-839` cmp + brace-style observation.
- **Found**: cmp returns 0; uniform +179-line offset; Allman style in both arms (`:654` and `:833` are both `    {` lines).
- **Verdict**: supports
- **Notes**: Variant-axis prose now consistent with the Sub-pattern B header and prose.

### Site 4 — §Justification clause Sub-pattern B (theme lines 532-536)

- **Theme claim** (lines 532-536): "Sub-pattern B (FGMRES twin) — `structural`. Byte-for-byte identical to A (`cmp`-confirmed over `iterative.cpp:653-660` ≡ `:832-839`; same brace style throughout; uniform +179-line file offset, zero local relative shift); the rotation is the same."
- **Cited evidence**: same cmp + brace-style.
- **Found**: same as Sites 2 & 3 — cmp returns 0; uniform +179 offset.
- **Verdict**: supports
- **Notes**: Justification-kind clause now consistent with the structural decomposition.

### Site 5 — §Status two-form bullet (theme lines 747-750)

- **Theme claim** (lines 747-750): "Both surface forms are positively anchored (GMRES `:652-660` and FGMRES `:831-840`); the two are byte-for-byte identical within the back-solve body (`cmp` over `:653-660` ≡ `:832-839`; uniform +179-line file offset, zero local relative shift, same brace-on-its-own-line style), grounding law-6 basis-lift independence."
- **Cited evidence**: same.
- **Found**: same as Sites 2-4; cmp returns 0; +179 uniform.
- **Verdict**: supports
- **Notes**: Status-tier bullet now consistent with the repaired Sub-pattern B narrative; the L1 leaf's law-6 basis-lift independence is correctly grounded.

### Verified_against row flip — `:832` (partially-supports → supports)

- **Theme claim** (line 833): "FGMRES outer descending sweep `for (int i = j; i >= 0; i--)`; byte-for-byte identical to GMRES :653 (cmp over :653-660 ≡ :832-839 zero; brace-on-its-own-line style identical in both arms; uniform +179-line file offset, zero local relative shift). Narrative Sub-pattern B repaired (cycle-031 D2 lifter): the prior `+1-line brace-style shift` claim was wrong — re-stated as byte-identical, +179-line file offset. Matches L1 leaf at L1/back_solve.md:225-226 `line-for-line identical` phrasing. citecheck --anchor zero-drift."
- **Cited evidence**: `palace/linalg/iterative.cpp:832` (anchor `'for (int i = j; i >= 0; i--)'`); paired `:653` cmp; `L1/back_solve.md:225-226` law-6.
- **Found**:
  - citecheck `--anchor 'for (int i = j; i >= 0; i--)'` on `:832-839`: anchor at line 832, zero-drift. ✓
  - Paired with `:653` via cmp: byte-identical. ✓
  - The c029 D5 baseline `partially-supports` verdict was rooted in the "+1-line brace-style shift" claim being unverified — that claim has now been independently disproven (it was actually wrong, not just unverified). The promotion to `supports` is correct.
- **Verdict**: supports (flip independently confirmed)
- **Notes**: This is the row the c031 D2 repair flipped. The flip is now grounded in: (a) independent cmp byte-identity verification; (b) the explicit retraction in the repaired narrative; (c) whole-file Allman-style corroboration. Closure complete.

## Applicability conditions

The theme's 6 applicability conditions (§Applicability conditions, lines 459-500) were exhaustively audited in the c030 baseline round and not re-checked here. They are unaffected by the c031 D2 repair (which only addressed the Sub-pattern B narrative around byte-identity vs. brace-shift). No new condition surfaced from the byte-identity confirmation that wasn't already covered.

## Algebraic laws (if cited)

The L1 leaf's law-6 (basis-lift independence) is grounded by the FGMRES `:832-839` `cmp`-identical body — the back-solve produces the same `y` regardless of whether the downstream lift reads `V[k]` (GMRES) or `Z[k]` (FGMRES). This is independently confirmed by the byte-identity of the back-solve body itself: the only differences between the arms are the downstream basis identifier (Sub-pattern C boundary, outside the leaf) and the +179-line file offset. The L1 leaf's law-6 phrasing at `L1/back_solve.md:225-226` ("back-solve code line-for-line identical") is **literally correct** as the theme prose now asserts; the LINE CONTENT is byte-identical, the LINE NUMBERS differ only by the constant +179 offset.

Other laws (1, 4, 5) are unchanged in the c031 D2 repair scope; this dispatch did not re-audit them. They were verified in c030.

## Proposed changes

Append a second mechanically-fenced `verified_against:` YAML block to the existing `## Verified against` section in the theme file (after the closing fence of the c030 baseline block at line 886). The c030 baseline 22-row block remains authoritative and is NOT re-audited here; this 4-row block is the c032 D2 additive re-verification. Emitted as a fenced YAML code block per the channel-format requirement (downstream `cross-layer-cross-cutter` parses by fence).

```edit:book/src/L1-L0/back-solve-mutation-rotation.md
[append at end of file, after the closing ``` fence of the existing c030 baseline yaml block in ## Verified against — adding a second yaml block; do NOT modify the c030 baseline block]

    # Additive c032 D2 re-verification — closes c031 D2 lifter narrative-repair loop.
    # The 22-row c030 baseline block above remains authoritative and is NOT re-audited here.
    # This block independently confirms the 5 narrative sites the c031 D2 repair changed
    # (Sub-pattern B header :198, Sub-pattern B prose :222-243, §Variant axes :591-594,
    # §Justification clause :532-536, §Status two-form bullet :747-750) and the
    # verified_against `:832` row flip (partially-supports → supports).
    verified_against:
      - citation: palace/linalg/iterative.cpp:653-660
        verdict: supports
        audited_at: 2026-05-30T053000Z
        note: GMRES back-solve body block re-verified cycle-032 D2 — cmp of sed-extracted ranges :653-660 vs :832-839 returns 0 (byte-identical); diff exit 0. Closes c031 D2 lifter narrative-repair loop. Independent re-verification of the Sub-pattern B header (line 198), Sub-pattern B prose with prior-draft retraction (lines 222-243), §Variant axes bullet (lines 591-594), §Justification clause (lines 532-536), and §Status two-form bullet (lines 747-750) — all 5 repaired sites now match on-disk source. Extended cmp 645-660 vs 824-839 (16-line epilogue+block) also byte-identical. citecheck --anchor zero-drift on for-loop opener.
      - citation: palace/linalg/iterative.cpp:832-839
        verdict: supports
        audited_at: 2026-05-30T053000Z
        note: FGMRES back-solve body block re-verified cycle-032 D2 — paired with GMRES :653-660; uniform +179-line file offset (832-653=179), zero local relative shift. Within-block relative offsets (0,+2,+3,+4,+6) byte-identical in both arms. Preceding break sits at +5 lines back from each arm for-line (GMRES :648, FGMRES :827); confirms boundary of the 16-line cmp-identical region. Resolves c029 D5 partial→supports flip and closes c031 D2 narrative-repair loop. citecheck --anchor zero-drift.
      - citation: palace/linalg/iterative.cpp:654
        verdict: supports
        audited_at: 2026-05-30T053000Z
        note: GMRES outer opening brace on its own line — Allman style; grep -cE for K&R-style braces (opening at end of for/if/while line) in iterative.cpp returns 0 (whole-file confirmation that the brace-on-own-line claim generalizes throughout the body). Grounds "throughout the whole iterative.cpp body" prose at theme line 238.
      - citation: palace/linalg/iterative.cpp:833
        verdict: supports
        audited_at: 2026-05-30T053000Z
        note: FGMRES outer opening brace on its own line — byte-identical to GMRES :654 (both bare opening-brace lines at indent 4). Paired anchor confirming "no brace-placement shift between the arms" prose at theme line 236.

NOTE TO INTEGRATOR: the `verified_against:` payload above is rendered as a 4-space-indented code block (per skill `convert-nested-fences-to-indented-code-in-proposed-changes-block`, option (b)) so it does not toggle the enclosing `edit:` fence. When materialised in the target chapter file, the integrator should re-fence the payload as a top-level ` ```yaml … ``` ` block matching the existing c030 baseline yaml block at lines 796-886 (channel-format requirement: downstream `cross-layer-cross-cutter` parses the chapter file by fence). The payload content is the entire 4-space-indented YAML block above (the leading `# Additive c032 D2 …` comment through the final `note:` line of the `:833` row), with the leading 4 spaces stripped per line.
```

(The proposed-changes block above uses 4-space-indented code rather than a nested ` ```yaml ` fence to avoid mis-toggling the outer ` ```edit:… ` fence under CommonMark — per skill `convert-nested-fences-to-indented-code-in-proposed-changes-block`. The downstream `cross-layer-cross-cutter` parses the chapter file by fence; the integrator re-fences the payload as a top-level ` ```yaml … ``` ` in the landed chapter, matching the c030 baseline block already in the file.)

The body of the theme is **NOT** rewritten — this dispatch is additive only. The c030 baseline 22-row block and the c031 D2 narrative repair both remain authoritative. The new block is appended as a second yaml block in the same `## Verified against` section, with a leading comment naming its provenance (c032 D2 re-verification, closes c031 D2 loop). No status change (theme remains `firm`). No new variant axes. No new applicability conditions.

## Supporting evidence

- `reference/palace/palace/linalg/iterative.cpp` — the Palace source of truth. Independently inspected via `cmp` (returns 0) and `diff` (exit 0) over `:653-660` ≡ `:832-839` and `:645-660` ≡ `:824-839`. Whole-file `grep -cE '(for|if|while|else)\s.*\{$' iterative.cpp` returns 0 (zero K&R-style braces in the entire file).
- `tools/citecheck/citecheck.py --anchor` — used on 8 paired anchors (`:653`/`:832`, `:655`/`:834`, `:656`/`:835`, `:659`/`:838`) all zero-drift on-disk. The shared authoritative line-map per cycle-024 meta-phase friction-ledger `producer-citation-drift-verify-not-self-invoked`. The +1 codemap-vs-on-disk drift caveat in the role spec is moot here — citecheck reads on-disk and is authoritative; codemap was not consulted.
- `book/src/L1-L0/back-solve-mutation-rotation.md` (the audit target) — post-c031 D2 state read at audit-time; 5 repaired sites located at lines 198, 222-243, 591-594, 532-536, 747-750; verified_against `:832` row at line 833.
- `book/src/L1/back_solve.md:225-226` — L1 leaf law-6 phrasing "back-solve code line-for-line identical" that the repaired narrative now matches.
- `reports/2026-05-30T010118Z-lowering-verifier-back-solve-mutation-rotation-audit/CYCLE.md` — c030 baseline 22-row audit; referenced as already-applied, NOT re-audited here.
- `reports/2026-05-30T050100Z-lifter-back-solve-sub-pattern-b-narrative-repair/CYCLE.md` — c031 D2 lifter narrative repair that this dispatch closes the loop on.

## Open questions / caveats

- **The c032 D2 additive block does not re-audit the 22-row c030 baseline.** That round remains the authoritative baseline for the other 22 rows; this dispatch only re-verifies the 5 repaired narrative sites and the `:832` row flip. If a future audit wants whole-block re-verification, that is a separate dispatch (the c029→c030→c032 metadata-refresh chain pattern from `normalize-mutation-rotation`).
- **`cmp`/`diff` byte-identity is the strongest possible mechanical confirmation.** Three orthogonal tools (cmp, diff, citecheck per-line) all agree; no remaining uncertainty about the byte-identity claim.
- **The Allman-style whole-file generalization** ("throughout the whole `iterative.cpp` body" at theme line 238) is now mechanically grounded by `grep -cE '(for|if|while|else)\s.*\{$' returns 0`. This is a file-wide property, not just a local `:654`/`:833` observation.
- **No layer-definition-discipline violation in the repaired prose.** The Sub-pattern B repair narrates the L1 → L0 rewrite direction throughout (it describes how the L1 leaf `back_solve` lowers into the L0 byte-identical body at FGMRES `:832-839`); no upward-lifting-direction prose surfaced in the 5 repaired sites.
- **No partly-constructive-promotion gating** — the theme is already `firm`. This re-audit is metadata-additive, not a status flip.
