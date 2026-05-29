---
agent: lowering-verifier
invoked_at: 2026-05-29T105500Z
scope: L1>L0 theme audit — dot-mutation-rotation §Sub-pattern D (carry-forward anchor fix orthog.hpp:34→:35)
status: pending
integrated_at: 2026-05-29T140000Z
integration_commit: f3be056
integration_notes: "Applied cycle-024 (staging row 8). dot-mutation-rotation §Sub-pattern D anchor fix orthog.hpp:34→:35 (lines 160 + 183) + verified_against: yaml append; theme stays firm. RESOLVES cycle-023 carry-forward OQ :847. Sole retroactive-evidence edit this cycle (per-slice retroactive count = 1, well under thresholds)."
inputs:
  - book/src/L1-L0/dot-mutation-rotation.md (§Sub-pattern D, lines 146-187)
  - palace/linalg/orthog.hpp:29-90 (cited L0 source)
  - reports/2026-05-29T092943Z-lowering-verifier-orthogonalize-composition-audit/ (cycle-023 carry-forward source)
---

# CYCLE: Audit dot-mutation-rotation §Sub-pattern D — orthog.hpp:34→:35 anchor fix

## Summary

Audited the single carry-forward citation surfaced (but not fixed) by the cycle-023
`orthogonalize-composition-audit`: in `book/src/L1-L0/dot-mutation-rotation.md` §Sub-pattern D
the anchor for the `IdentityInnerProduct::operator()` body `return LocalDot(x, y);` reads
`orthog.hpp:34` in two places (line 160 prose, line 183 citation list), but the cited token is
at **`orthog.hpp:35`** — line 34 is the opening brace `{` of the operator body.
Independently `read_range`-confirmed against the Palace source: the struct `IdentityInnerProduct`
spans lines 30-37 (`get_symbol_def`), the operator body `{` is at line 34, and
`return LocalDot(x, y);` is at line 35 (`search_text` exact hit). The §Sub-pattern D claim
("the canonical `IdentityInnerProduct::operator()` returns `LocalDot(x, y)`") is **fully
supported** at the corrected line — only the line number drifted by one. Verdict:
**supports-with-one-token-anchor-drift**; the theme content (status `firm`) is unaffected.
Two surgical `:34`→`:35` edits proposed below; all other §Sub-pattern D anchors
(`:48`, `:46-52`, `:70`, `:75-88`, the `:29-36` range label) independently re-confirmed correct
and NOT touched.

## Per-citation audit

### Citation 1 — line 160 (prose)
- **Citation**: `book/src/L1-L0/dot-mutation-rotation.md:160` — `IdentityInnerProduct::operator()` returns `LocalDot(x, y)` (`orthog.hpp:34`)
- **Theme claim**: the canonical hook `IdentityInnerProduct::operator()` body returns `LocalDot(x, y)`.
- **Found**: `palace/linalg/orthog.hpp:35` reads exactly `    return LocalDot(x, y);` (`search_text` returned a single hit at line 35). Line 34 is the operator body's opening brace `{`.
- **Verdict**: **supports** — the claim is correct; only the line number is off-by-one (`:34` should be `:35`).
- **Notes**: line-34 = `{`; line-35 = the `return`. Classic brace-vs-statement off-by-one.

### Citation 2 — line 183 (citation list)
- **Citation**: `book/src/L1-L0/dot-mutation-rotation.md:183` — `palace/linalg/orthog.hpp:29-36` — `IdentityInnerProduct`; `return LocalDot(x, y)` at `:34`.
- **Theme claim**: within the `IdentityInnerProduct` struct, `return LocalDot(x, y)` sits at `:34`.
- **Found**: same as Citation 1 — the `return LocalDot(x, y);` token is at `orthog.hpp:35`, not `:34`.
- **Verdict**: **supports** with the `:34`→`:35` correction. The enclosing range `:29-36` is a separate sub-token (see Notes) and is left as-is.
- **Notes**: the enclosing range `:29-36` brackets the helper from its leading comment (`// Simplest case is canonical inner product on R & C.`, line 29) through the operator-body closing `}` (line 36). `get_symbol_def` reports the struct proper at lines 30-37 (the `};` terminator is line 37). The `:29-36` range is therefore a defensible "comment + struct-body" span and is OUT OF SCOPE for this single-token carry-forward fix (the task scopes only the `:34`→`:35` token). I flag the `:29-36` END boundary as a candidate `:29-37` tidy-up (to include the `};`) under Open questions, but do NOT propose it here — it is a different anchor than the carry-forward target and changing it was not requested.

### Re-confirmed-correct anchors in §Sub-pattern D (NOT changed)
- `orthog.hpp:48` (line 173 prose, "// Note order is important for complex vectors") — `search_text` hit at line 48. **Correct.**
- `orthog.hpp:46-52` (line 184) — MGS per-`j` block: `H[j]=dot_op(w,V[j])` (line 49), `Mpi::GlobalSum(1,&H[j],comm)` (line 50), `w.Add(-H[j],V[j])` (line 51), closing `}` (line 52); loop head `for` at line 46. **Range correct.**
- `orthog.hpp:66-88` + `:70` + `:75-88` (line 185) — CGS `Mpi::GlobalSum(m, H, comm)` confirmed at line 70 (`search_text` hit); the `refine` second pass body runs to line 88. **Correct.**
- `orthog.hpp:49-51` (line 163 prose, MGS interleave) — matches the MGS body lines above. **Correct.**

## Applicability conditions

The §Sub-pattern D claim does not introduce new applicability conditions beyond the theme's
five (lines 260-281); this audit is a citation-anchor correction, not a semantics re-check.
Walking the one condition the corrected anchor touches:

- **Condition**: "the canonical `IdentityInnerProduct::operator()` returns `LocalDot(x, y)`, and the routine itself applies `Mpi::GlobalSum`" (the unfused two-step, line 160-161).
- **Verifiable**: yes, directly from `orthog.hpp:35` (`return LocalDot(x, y);`) + the MGS/CGS `Mpi::GlobalSum` calls (lines 50/70). The local-dot/collective split across the hook boundary is exactly as the theme narrates.
- **Found counter-example?**: no. The body is precisely the single `return LocalDot(x, y);` the theme claims; the collective is applied by the routine (MGS size-1 interleaved, CGS batched size-m), not by the hook. The unfused-vs-fused (Sub-pattern A) framing holds.

## Algebraic laws (if cited)

None newly cited in this audit. The §Sub-pattern D justification kind is `structural` (the
unfused two-step is the same `Mpi::GlobalSum ∘ LocalDot` expansion as Sub-pattern A with the
collective lifted out of the per-dot call). The value-level identity `xᴴ y = conj(yᴴ x)` lives
in §"The conjugation asymmetry" and is unaffected by the line-number correction. No law re-check
in scope.

## Proposed changes

Two surgical single-token edits, `:34`→`:35`, applied verbatim by the integrator. Both
`old_string`s are unique in the file (verified: line 160's phrasing `returns ... (`orthog.hpp:34`)`
and line 183's phrasing `... at `:34`.` differ).

```edit:book/src/L1-L0/dot-mutation-rotation.md
[edit 1 — line 160 prose anchor]
old:
`IdentityInnerProduct::operator()` returns `LocalDot(x, y)` (`orthog.hpp:34`), and the
new:
`IdentityInnerProduct::operator()` returns `LocalDot(x, y)` (`orthog.hpp:35`), and the
```

```edit:book/src/L1-L0/dot-mutation-rotation.md
[edit 2 — line 183 citation-list anchor]
old:
- `palace/linalg/orthog.hpp:29-36` — `IdentityInnerProduct`; `return LocalDot(x, y)` at `:34`.
new:
- `palace/linalg/orthog.hpp:29-36` — `IdentityInnerProduct`; `return LocalDot(x, y)` at `:35`.
```

No status change: the theme remains `firm`. No other content edits — the claim is correct at
the corrected line; this is a pure anchor-drift repair.

## Supporting evidence

- `palace/linalg/orthog.hpp:29-37` (`read_range` this invocation): line 29 `// Simplest case is canonical inner product on R & C.`; line 30 `struct IdentityInnerProduct`; line 31 `{`; line 32 `template <typename VecType>`; line 33 `auto operator()(const VecType &x, const VecType &y) const`; line 34 `{`; line 35 `return LocalDot(x, y);`; line 36 `}`; line 37 `};`.
- `mcp__palace-codemap__search_text "return LocalDot\(x, y\);"` over `orthog.hpp` → single hit at **line 35**.
- `mcp__palace-codemap__get_symbol_def IdentityInnerProduct` → `struct_specifier`, start_line 30, end_line 37.
- `mcp__palace-codemap__search_text "Note order is important for complex vectors"` → line 48 (confirms the `:48` anchor on theme line 173).
- `mcp__palace-codemap__search_text "Mpi::GlobalSum\(m, H, comm\)"` → line 70 (confirms the `:70` anchor on theme line 185).
- `palace/linalg/orthog.hpp:64-90` (`read_range`): CGS local-dots loop, batched `Mpi::GlobalSum(m, H, comm)` (line 70), `refine` second pass through line 88 — confirms `:66-88` / `:75-88`.
- Carry-forward source: cycle-023 `reports/2026-05-29T092943Z-lowering-verifier-orthogonalize-composition-audit/` (surfaced the `:34` drift; explicitly out of that audit's scope to fix).

## verified_against metadata (proposed append)

Per the sibling-theme `verified_against:` convention (consumed by `cross-layer-cross-cutter`
for coverage analysis), append the following fenced block at the end of
`book/src/L1-L0/dot-mutation-rotation.md`. NOTE: the theme already carries a §"Verified-against"
prose section (lines 309-358); this adds the structured machine-readable block the downstream
parser extracts. Integrator may fold it into that section or append at EOF.

~~~~edit:book/src/L1-L0/dot-mutation-rotation.md
[append at end of file]
```yaml
verified_against:
  - citation: palace/linalg/orthog.hpp:35
    verdict: supports
    audited_at: 2026-05-29T105500Z
    note: IdentityInnerProduct::operator() body `return LocalDot(x, y);` confirmed at :35 (was miscited :34, the operator-body opening brace). Corrected in §Sub-pattern D lines 160 + 183.
  - citation: palace/linalg/orthog.hpp:48
    verdict: supports
    audited_at: 2026-05-29T105500Z
    note: "// Global inner product: Note order is important for complex vectors." re-confirmed at :48.
  - citation: palace/linalg/orthog.hpp:46-52
    verdict: supports
    audited_at: 2026-05-29T105500Z
    note: MGS per-j interleaved size-1 collective block re-confirmed (dot at :49, GlobalSum(1,...) at :50, Add at :51).
  - citation: palace/linalg/orthog.hpp:66-88
    verdict: supports
    audited_at: 2026-05-29T105500Z
    note: CGS m local dots then ONE Mpi::GlobalSum(m, H, comm) at :70; CGS2 refine second pass through :88.
```
~~~~

## Open questions / caveats

- **OQ close (carry-forward).** The cycle-023 carry-forward — "`dot-mutation-rotation`
  §Sub-pattern D cites `orthog.hpp:34` for `return LocalDot(x, y)`; codemap+citecheck place the
  token at `:35`" — is RESOLVED by the two proposed edits above. The integrator should close the
  corresponding OQ entry (if filed by the cycle-023 audit) / mark the carry-forward discharged in
  the staging log. No residual.
- **Adjacent range tidy-up (NOT proposed; flagged only).** The citation-list range
  `palace/linalg/orthog.hpp:29-36` (theme line 183) ends at the operator-body closing `}` (line
  36); the struct's terminating `};` is line 37 (`get_symbol_def` end_line 37). A future tidy
  could widen it to `:29-37` to include the struct terminator. This is a DIFFERENT anchor than the
  carry-forward `:34`→`:35` token and was not in scope; I do not propose it here to keep the fix
  bounded to the requested single-token correction. Logged for a future lifter/abstractor reread
  if range-precision tightening is wanted.
- No direction-of-definition violation: §Sub-pattern D narrates the L1→L0 lowering forward
  (L1 `dot` reduction lowering into the `orthog.hpp` hook-routed unfused two-step). No reverse
  (L0-lifts-to-L1) prose. Compliant with the high→low invariant.
- No runtime-state dependence; the audit is a pure static source-line confirmation.

## Relevant file paths

- Audited theme: `/home/crutcher/git/palace_whiteroom/book/src/L1-L0/dot-mutation-rotation.md` (§Sub-pattern D, lines 146-187; edits at 160 + 183)
- Cited source: `reference/palace/palace/linalg/orthog.hpp:29-90`
- This report: `/home/crutcher/git/palace_whiteroom/reports/2026-05-29T105500Z-lowering-verifier-dot-anchor-fix/CYCLE.md`
