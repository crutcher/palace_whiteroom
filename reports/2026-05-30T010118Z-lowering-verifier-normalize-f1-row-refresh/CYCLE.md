---
agent: lowering-verifier
invoked_at: 2026-05-30T01:01:18Z
scope: L1>L0 verified_against row REFRESH — normalize-mutation-rotation F1 row (palace/linalg/operator.hpp:377-384) post-c029 prose correction
status: integrated
integrated_at: 2026-05-30T050000Z
integration_commit: 21dedc3
integration_notes: Applied clean as report-5 of cycle-030; F1 row at `book/src/L1-L0/normalize-mutation-rotation.md:481-484` (NOT the stale `:466-469` ledger slug — line numbers shifted ~15 lines downward by c029 prose expansion) verdict flipped `does-not-support` → `supports`; theme stays firm. Completes the c028→c029→c030 metadata-refresh chain. Repairer prefixed 15 bare-basename `operator.{hpp,cpp}` narrative-prose refs with `palace/linalg/` for path-hygiene. See `reports/cycle-030-integrator-staging/STAGING.md` row 5 + `log/cycle-30.md` HEADLINE 3.
inputs:
  - book/src/L1-L0/normalize-mutation-rotation.md (firm theme; F1 row at :481-484; c029-corrected prose)
  - reports/2026-05-29T194558Z-lowering-verifier-normalize-mutation-rotation-audit/CYCLE.md (cycle-028 audit; F1 origin)
  - reports/2026-05-29T205945Z-abstractor-normalize-b-prose-correction/CYCLE.md (cycle-029 prose correction; routed F1 close)
  - reference/palace/palace/linalg/operator.hpp:377-384 (fused B-weighted Normalize free function — on-disk verified)
  - grep survey: 4-arg Normalize(comm, ?, B, ?) callsites across reference/palace/palace/ → zero
---

# CYCLE: Refresh F1 verified_against row — normalize-mutation-rotation

## Summary

The cycle-028 `lowering-verifier` audit of `normalize-mutation-rotation` recorded a
single `does-not-support` row (F1) against `palace/linalg/operator.hpp:377-384`, whose
note diagnosed the then-prose claim "Palace has **no** fused `linalg::Normalize`-with-`B`
free function" as factually wrong (the function IS defined at `palace/linalg/operator.hpp:378`).
Cycle-029 dispatch-3 (`abstractor-normalize-b-prose-correction`, integrated at commit
`e44896d`) applied the routed prose correction: the theme now reads "**Fused B-Normalize
exists but has no callsite**" (lines 286-303 of the on-disk theme) and the L0-form §
intro at line 51 mentions the fused overload "exists but is uncalled — see the
`normalize_B` rough-in note below". The c029 prose is now **factually accurate** against
the L0 source (the fused operator at `palace/linalg/operator.hpp:377-384` is positively anchored; the
"uncalled" claim is grep-confirmed across the tree).

The F1 row in the theme's `verified_against:` block (lines 481-484) is now **STALE**:
its verdict `does-not-support` and diagnostic note reference the WAS-prose ("no fused
linalg::Normalize-with-B free function") that no longer exists. **Re-auditing the
now-corrected prose**: every claim the c029-corrected prose makes about
`palace/linalg/operator.hpp:377-384` IS supported by on-disk evidence — (i) the four-step composition
at `:378-383` matches the unweighted core verbatim (`Normalize(...)` def `:378`,
`Norml2(comm,x,B,Bx)` reduction `:380`, `MFEM_ASSERT(norm > 0.0)` `:381`, `x *= 1.0 /
norm` `:382`, `return norm` `:383` — all five citecheck `--anchor` probes land within
the cited range, zero codemap drift); (ii) the "uncalled" claim is grep-verified
(`grep -rn 'Normalize(.*comm.*B' reference/palace/palace/` returns the definition
line alone — zero callsite matches). Verdict shifts **`does-not-support` →
`supports`** with an updated note that records the c029 prose alignment + the c029
audit timestamp.

This is the verified_against ROW REFRESH the cycle-029 abstractor's "Open questions /
caveats" explicitly delegated to a future verifier dispatch ("A future
lowering-verifier re-audit cycle COULD upgrade the verdict to `supports` (now that the
surrounding prose matches the source), but that is a verifier dispatch, not an
abstractor one"). This dispatch IS that re-audit. The firm theme `## Status` is
unchanged (the row refresh is metadata-only; the firm unweighted core was untouched by
both c028 and c029).

## Per-citation audit

### F1 citation re-audit — `palace/linalg/operator.hpp:377-384`

- **Citation**: `palace/linalg/operator.hpp:377-384`
  - **Theme claim (c029-corrected prose, on-disk now)**: "Palace ships a fused
    B-weighted free function `Normalize(comm, x, B, Bx)` at
    `palace/linalg/operator.hpp:377-384` (def `:378`, B-weighted reduction `:380`,
    partiality guard `:381`, rescale `:382`, return `:383`) — structurally identical
    to the unweighted `linalg::Normalize` at `palace/linalg/vector.hpp:262-270` (the
    four-step composition reduction → guard → rescale → return), differing only by
    threading `(B, Bx)` into the inner `Norml2`. **However, the fused B-Normalize is
    uncalled**: a grep across `palace/` for 4-arg `Normalize(comm, x, B, Bx)`
    invocations finds **zero** callsites." (theme `:286-303`)
  - **Found (on-disk verification this invocation)**:
    - `palace/linalg/operator.hpp:376` `// Normalize the vector with respect to an SPD matrix B.`
    - `palace/linalg/operator.hpp:378` `inline double Normalize(MPI_Comm comm, VecType &x, const Operator &B, VecType &Bx)`
    - `palace/linalg/operator.hpp:380` `double norm = Norml2(comm, x, B, Bx);`
    - `palace/linalg/operator.hpp:381` `MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!");`
    - `palace/linalg/operator.hpp:382` `x *= 1.0 / norm;`
    - `palace/linalg/operator.hpp:383` `return norm;`
    - All five `citecheck --anchor` probes land within `377-384`: def→`:378`,
      reduction→`:380`, guard→`:381`, rescale→`:382`, return→`:383`. Zero drift.
    - Grep `grep -rn 'Normalize(.*comm.*B' reference/palace/palace/
      --include='*.cpp' --include='*.hpp' --include='*.h'` returns **exactly one
      line**: `palace/linalg/operator.hpp:378` — the definition itself. **Zero callsites.**
  - **Verdict**: **supports**. The c029-corrected prose is faithful to the L0 source
    on both factual claims (the function EXISTS at the cited range with the cited
    four-step composition AND is UNCALLED).
  - **Notes**: this row was `does-not-support` against the cycle-028 audit's
    snapshot of the WAS-prose ("Palace has no fused linalg::Normalize-with-B free
    function"). The cycle-029 prose correction landed at commit `e44896d`; the
    on-disk prose now reads the corrected form. Row refresh is the natural
    follow-up.

## Applicability conditions

The cycle-028 audit recorded "applicability set is complete for the firm unweighted
core". This refresh does not touch the unweighted core's four applicability conditions;
it touches only the `verified_against:` metadata for the `normalize_B` rough-in note's
sole F1 row. No new applicability condition is introduced or invalidated by the
refresh.

## Algebraic laws (cited)

The cycle-028 audit confirmed the L1 factorisation law 6 + partiality. This refresh
does not touch the algebraic laws. The fused B-`Normalize` at `palace/linalg/operator.hpp:378` is the
B-weighted analogue (`normalize_B`-shape) and inherits the same factorisation +
partiality structure modulo threading `(B, Bx)` into the inner reduction — this is a
syntactic identity to the unweighted form (the c029 prose calls this out: "structurally
identical to the unweighted `linalg::Normalize` at `palace/linalg/vector.hpp:262-270`
... differing only by threading `(B, Bx)` into the inner `Norml2`").

## Proposed changes

Single edit: replace the F1 row in the theme's `verified_against:` block (currently at
on-disk lines 481-484) with the refreshed verdict + note.

CHANNEL-FORMAT NOTE: the new `note:` value MUST NOT begin with a literal `"` character
(the leading-`"` yaml.safe_load mis-parse hazard the dispatch brief flagged; this is
exactly the file/region where the hazard applies). The refreshed note below is
double-quote-wrapped (yaml-safe-load-safe because the leading character INSIDE the
quotes is `R`, a plain alphabetic), and contains no internal unescaped double quotes.

```edit:book/src/L1-L0/normalize-mutation-rotation.md
[at lines 481-484, replace the F1 row]
old:
  - citation: palace/linalg/operator.hpp:377-384
    verdict: does-not-support
    audited_at: 2026-05-29T19:45:58Z
    note: "Range correct, but the surrounding 'no fused linalg::Normalize-with-B free function' claim (lines 51, 285-287, 311-313) is WRONG: palace/linalg/operator.hpp:378 IS a fused B-weighted Normalize(comm, x, B, Bx) free function (reduction->guard->rescale->return, identical to vector.hpp:264). The defensible fact is that this fused B-Normalize is UNCALLED (no 4-arg rescaling callsite in the tree). Affects only the normalize_B rough-in note, NOT the firm unweighted core. Routed to follow-up abstractor (F1)."
new:
  - citation: palace/linalg/operator.hpp:377-384
    verdict: supports
    audited_at: 2026-05-30T01:01:18Z
    note: "Refreshed cycle-030 after cycle-029 abstractor prose correction (commit e44896d) aligned the surrounding prose with the L0 source. Range correct; the c029-corrected prose at theme :286-303 (Speculative L1 operators rough-in note) and :51 (L0 form intro) accurately reads 'fused B-Normalize exists but is uncalled': definition at palace/linalg/operator.hpp:378 (def, reduction :380, guard :381, rescale :382, return :383 — all citecheck --anchor probes land within 377-384) is positively anchored; the 'uncalled' claim is grep-verified (zero 4-arg Normalize(comm, x, B, Bx) callsites across reference/palace/palace/). Affects only the normalize_B rough-in note, NOT the firm unweighted core. Prior c028 verdict does-not-support was against the WAS-prose; obsolete after c029."
```

The replacement carries:
- **verdict**: `supports` (the c029-corrected prose IS faithful to the L0 source).
- **audited_at**: `2026-05-30T01:01:18Z` (this invocation's timestamp; this is a fresh
  audit, not a c028 historical record).
- **note**: a fact-accurate summary of the refresh — names the c029 commit that
  triggered the alignment, records both the positive-source verification (citecheck
  anchors) and the negative-source verification (grep zero-callsite), and notes the
  refresh does not touch the firm unweighted core. Leading character is `R` (no
  leading-`"` parse hazard); no internal unescaped `"` either.

No other edits proposed. The remaining 15 rows of the `verified_against:` block stay
intact (the cycle-028 audit upheld all of them; nothing has changed on-disk for any of
the other cited ranges). The theme's `## Status` (firm) is untouched.

## Supporting evidence

- `reference/palace/palace/linalg/operator.hpp:370-389` — read on-disk this invocation
  (the fused B-weighted `Normalize` template + the immediately-preceding `Norml2`
  forward declaration with the matching 4-arg signature). The four-step composition
  (`:380-383`) is verbatim identical to `vector.hpp:266-269` modulo `(B, Bx)` args.
- `tools/citecheck/citecheck.py 'palace/linalg/operator.hpp:377-384' --anchor ...`
  (5 invocations this session): def `:378`, reduction `:380`, guard `:381`, rescale
  `:382`, return `:383` — all five anchors land **exactly** within `377-384` (1 ok, 0
  failing per probe). Zero drift.
- `grep -rn 'Normalize(.*comm.*B' reference/palace/palace/ --include='*.cpp'
  --include='*.hpp' --include='*.h'` → exactly one match line: `palace/linalg/operator.hpp:378`
  (the definition itself). **Zero callsites.**
- `book/src/L1-L0/normalize-mutation-rotation.md` (on-disk this invocation, post-c029):
  - `:51` reads "the fused B-weighted overload `Normalize(comm, x, B, Bx)` at
    `palace/linalg/operator.hpp:377-384` exists but is uncalled" (parenthetical added
    by c029).
  - `:286-303` reads "**Fused B-Normalize exists but has no callsite**. Palace ships
    a fused B-weighted free function `Normalize(comm, x, B, Bx)` at
    `palace/linalg/operator.hpp:377-384` ..." (the c029-corrected §Speculative L1
    operators rough-in note body).
  - `:481-484` is the F1 row this dispatch refreshes (still verdict
    `does-not-support`, audited_at `2026-05-29T19:45:58Z`, note about the WAS-prose).
- `reports/2026-05-29T205945Z-abstractor-normalize-b-prose-correction/CYCLE.md` — the
  c029 dispatch. Its "Open questions / caveats" §1 explicitly delegated the F1 row
  refresh to a "future lowering-verifier re-audit cycle". This dispatch IS that
  re-audit.
- `reports/2026-05-29T194558Z-lowering-verifier-normalize-mutation-rotation-audit/CYCLE.md`
  — the c028 audit that recorded the original `does-not-support` verdict and the F1
  finding (Edit 3 routing). The audit verdict was correct AS-OF c028 against the WAS-
  prose; c029 fixed the prose; this dispatch refreshes the row to reflect the new
  on-disk state.

## Open questions / caveats

- **The 15 other `verified_against:` rows are NOT touched.** This refresh is scoped to
  the single F1 row at lines 481-484. The other rows (vector.hpp:262-270,
  vector.hpp:259, vector.hpp:267, iterative.cpp:631-632, iterative.cpp:810-811,
  palace/linalg/operator.cpp:660-661/673/676, nleps.cpp:610-611/617, the L1/cross-theme anchors, and
  the test-orthog rows + the palace/linalg/operator.cpp:599-619 B-weighted reduction row) are
  unchanged on-disk per the c029 prose correction, so their c028 verdicts stand.
- **Theme `## Status` remains `firm`.** The row refresh is metadata-only on a
  rough-in NOTE. The firm unweighted-normalise core was never in scope for the F1
  finding, and remains unchanged.
- **Direction-of-definition: clean.** The c029 prose narrates forward (L1 normalize →
  L0 `linalg::Normalize`), and the corrected rough-in note narrates the B-weighted
  sibling forward as well; no reverse-direction prose. No high→low violation.
- **The `does-not-support` → `supports` flip does NOT reflect any change to the L0
  source.** The on-disk `palace/linalg/operator.hpp:377-384` content is identical at c028, c029, and
  c030. What changed is the *theme prose making claims about that range* — c029
  rewrote the prose; the row verdict reflects whether the (new) prose matches the
  (unchanged) source. Both c028 and c030 verdicts are correct AS-OF their respective
  prose snapshots.
- **OQ `normalize-mutation-rotation-verified-against-row-466-469-stale-after-c029-prose-correction`
  is RESOLVED by this dispatch** once integrated. The integrator-per-report SHOULD
  close it in `scaffolding/open-questions.md` (append-only close marker) when applying
  this report — I do NOT propose the OQ-ledger close-edit here (integrator's
  authority).
- **Row-location note for the integrator.** The dispatch brief identified the F1 row
  at "around lines 466-469". On-disk verification this invocation places the F1 row at
  lines **481-484** (the row indices shifted because the c029 prose correction
  enlarged the body above the `verified_against:` block by ~15 lines; the
  `verified_against:` block itself begins at `:424`). The `edit:` block above uses the
  current on-disk row text (the `old:` chunk) for unambiguous matching, so the
  integrator's `Edit` tool will land regardless of exact line number.
