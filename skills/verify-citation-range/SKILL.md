---
name: verify-citation-range
description: For each L0 citation of the form `<path>:<lo>-<hi>`, verify that the range does not cross the named symbol's (function, struct, namespace block, template instantiation) lexical boundary. Applied by the Explorer when emitting L0 citations and by the Critic when verifying them. Catches the cross-function-boundary citation drift recurrence (cycles 69-70 GMRES FgmresSolver::Mult cited 733-875 when the function actually ends at 871).
status: active
---

# verify-citation-range

A citation `<path>:<lo>-<hi>` purports to cover a coherent semantic unit — typically the body of a named function, the inside of a class declaration, or the definition of a template instantiation. When the cited range crosses out of that unit (`hi` exceeds the closing brace of the named symbol and continues into adjacent unrelated code), the citation is wrong even if the prose claim it supports happens to be correct: a reader following the citation lands in the wrong code.

This skill names the verification procedure and the drift convention.

## Procedure

1. **Retrieve the source.** For each citation, read the file (via `read_range` MCP or `Read`) covering the lines `lo` through `hi`, plus enough context above and below to see the enclosing braces.

2. **Identify the named symbol.** Determine which symbol's body the citation purports to cover — usually named in the surrounding prose (e.g., "L0.13 FgmresSolver::Mult: palace/linalg/iterative.cpp:733-875"). Common forms:
   - Function or method: `<RetType> <ClassName>::<MethodName>(...) { ... }`
   - Template specialization or instantiation block: `template <typename T> ...`
   - Anonymous namespace or unnamed-scope block: `namespace { ... }`
   - Static / file-scope helper functions: `static <RetType> <name>(...) { ... }`

3. **Verify lexical containment.** Both `lo` and `hi` must fall within the named symbol's body — `lo >= <open-brace line>` and `hi <= <close-brace line>`. The opening signature line itself is part of the body for citation purposes.

4. **Catch the drift.** If `hi` exceeds the closing brace and the next lines are a different function/block:
   - **REQUIRES-RE-ANCHOR**: re-emit the citation with a `hi` clipped to the closing brace line.
   - If the prose claim relies on content past the boundary, split the citation: introduce `L0.Xa`/`L0.Xb` with separate ranges and either separate semantic roles.

5. **Multi-specialization coverage.** When the citation claims "real and complex specialisations" or "all four template instantiations," verify each specialization's range is either cited or explicitly split into sub-entries. Don't span specializations with a single range when their bodies are at different line ranges.

## Tolerance

- **Intra-function ±1-3 line drift** (citation extends 1-3 lines past closing brace into whitespace/blank lines) is audit-tolerable — the reader still lands in the right neighborhood and the prose claim is unaffected.
- **Cross-function-boundary drift** (citation extends into a different named symbol's body) is NOT audit-tolerable — the reader following the citation gets wrong code; the prose claim cannot be verified against the wrong region.

## Producer self-verification before emitting citations (added cycle-015 meta-phase)

The previous sections frame this skill as something the Explorer/Critic applies to *already-emitted* citations. Batch-3 (cycles 013/014/015) surfaced the recurring failure that this is **too late**: producer dispatch agents (harvester, abstractor, lifter, layer-intro-author — and even the citation-auditing lowering-verifier) emit `path:lo-hi` citations that drift off the true source line by 1–N lines, and only the downstream repairer/critic catches them, at a per-cycle repair-round cost. The producers cite from memory or from an earlier read whose line numbers have drifted. The fix is to **run this verification at emit time, on every citation, before the citation leaves the producer's CYCLE.md.**

This is the **strongest recurring friction of batch-3** (friction-ledger `producer-citation-drift-verify-not-self-invoked`): ~6 reports drifted in cycle-013, 5-of-8 in cycle-014 (including the auditing role), and the bilinearform `RT_FECollection`/`L2_FECollection` + 2 relocated-dangle re-anchors in cycle-015.

**Producer-emit-time procedure (run for EVERY citation before emitting):**

1. **Do NOT cite from memory or from an earlier read.** Line numbers drift between an early localization read and the final citation; the codemap is the ground truth, not your working memory.
2. **`read_range` (or codemap `get_symbol_def` / `search_text`) the exact cited lines** `lo`–`hi` plus a few lines of context.
3. **Confirm the named construct sits ON the asserted line.** The function/struct/member/statement the prose attributes to `lo` (or to a specific line within `lo`–`hi`) must be on that exact line — not merely "in the neighborhood." `get_symbol_def` returns the symbol's definition line directly; prefer it for single-symbol attributions.
4. **For a re-anchored / relocated pointer (lifter sweeps), confirm the NEW target is the TERMINAL firm home** — not another relocated-dangle that will itself need re-pointing. (Cycle-015 the L3 cg.md sweep pointed 2 re-anchors at relocated-dangle targets; the repairer corrected them to terminal L2 homes.)
5. **For citation-dense bundle chapters (L0 file-overviews), verify each of the N ranges** — the L0-bundle shape recurred ≥3× across batch-3 and is the highest-volume citation surface; do not batch-trust.

Producer role specs (harvester / abstractor / lifter / layer-intro-author §Discipline) carry a bullet pointing at this section (cycle-015 meta-phase). The role-spec bullet is necessary but — as the cycle-014 auditor-drift showed (the lowering-verifier had a citation bullet since cycle-012 and still drifted) — **not sufficient on its own**; a mechanical codemap-backed pre-integration citation-range checker tool is the durable fix and is filed as an ASK (cycle-015 meta-phase, friction-ledger `producer-citation-drift-verify-not-self-invoked`). Until that tool exists, the emit-time self-check is the front-line mitigation.

## Audit-report / inherited-citation sub-case (added cycle-012 meta-phase)

A report whose **deliverable itself is a no-drift / citations-verified claim** — lowering-verifier audits, `citation-validity` critic checks, slice-reduction audits — carries an unusually high duty to land its own anchors precisely. Its entire output is a verification assertion; an inherited drift in such a report defeats the audit's purpose.

The sharp failure mode: the report **copies a citation from the artifact it is auditing** and re-asserts it as verified WITHOUT independently confirming the line range against source. The inherited error propagates with an audit's stamp of approval on it.

Additional procedure for audit-shaped reports:

1. **Enumerate every `(file:line)` the report ASSERTS as verified** — especially ones copied from the artifact under audit.
2. **For each, `read_range` the cited line ±a few lines** (do NOT transcribe the range from the audited artifact — read source).
3. **Confirm the asserted code/construct is ON the cited line** (not merely "in the neighborhood"). An audit asserting "no drift" must land the construct on the exact line, not the enclosing range.
4. **When the citation was copied from the audited artifact, flag any drift as BOTH** a report-anchor fix AND an integrator carry-forward correction (the artifact also needs correcting — see friction-ledger `lifter-scope-content-correction-boundary`: bounded evidenced citation corrections are in-scope for the auditor).
5. **Internal-consistency check.** If the report cites the same construct at two different ranges (a precise line in one section, an enclosing range in another), RECONCILE them before asserting "no drift." An internally-inconsistent audit report is self-refuting.

**Worked example (cycle-012 SLEPc-NEP audit).** The lowering-verifier inherited an `arpack.cpp:387` miscitation verbatim from `book/src/L1/eigsolve.md:116,222` and asserted "no drift" over its own anchors while propagating the error. The un-scale `eig[i] = eig[i] * gamma;` is actually at `arpack.cpp:383` (line 387 is a sort-branch condition). The report was internally inconsistent: §Supporting-evidence cited the correct enclosing range `383-392` while body + `verified_against:` pinned `:387`. Resolution: independently `read_range`-confirm `383` carries the un-scale, fix the report anchor AND carry forward the artifact correction (`arpack.cpp:387` → `:383` at `eigsolve.md:116` + `:222`).

## Sibling-slice / inherited-precedent re-anchor sub-case (added cycle-021 meta-phase)

A dispatch whose **premise is a slice re-anchor** — "slice X was *reduced* (its v0.1–v0.4 forms lifted to firm entries), so re-anchor its drifted refs" — must NOT sweep only the focus slice. Sibling slices cited in the same paragraphs frequently underwent the *same* reduction-class drift, and the focus-slice sweep structurally skips them. A sibling cited as a **"precedent rendering"** is the high-risk case: precedents are exactly the v0.1–v0.4 forms most likely to have been lifted away, so a `<sibling>.md:NNN` ref into a reduced sibling is presumptively out of range.

Additional procedure for slice-re-anchor dispatches:

1. **Enumerate ALL distinct `<slice>.md` citations in the touched/authored content** — not just `<focus-slice>.md` refs. Include refs in NEW content you append, not only retained refs.
2. **For each *distinct* slice cited, open it and check for a reduced-slice stub-header** (`# Slice: <name> (reduced)` / "**Firm entries that supersede…**"). Its presence is the signal that the slice's old numeric line-refs are presumptively stale.
3. **If reduced, treat every numeric line-ref into that slice as presumptively drifted:** verify the ref resolves to the claimed content on the *current* file; if the cited form was lifted away (named in the stub-header's supersedes list), re-anchor to the firm home rather than the dead slice range.
4. The check is **one read + stub-header scan per distinct cited slice** — cheap relative to the repair round a dangling sibling ref costs at integration.

**Worked example (cycle-020 gmres self-rotation).** The lifter `gmres §L4 v0.6→v0.7` dispatch correctly swept every `gmres.md:NNN` ref (the focus slice it diagnosed as reduced) but re-emitted `cg.md:215-219` (the CG `iterate_while` precedent) in three places without checking that `cg.md` had undergone the *same* reduction: `cg.md` is now 166 lines and its v0.4 `iterate_while` form was lifted to `L4/krylov-step.md`, so `cg.md:215-219` is out of range. Reduction-class drift caught for the focus slice, missed for the sibling. Resolution: scan `cg.md` for its reduced-slice stub-header, re-anchor the precedent ref to the firm `L4/krylov-step.md` home.

## Worked examples

**Cycle 69 (GMRES L0.13)**: cited `FgmresSolver::Mult` as `palace/linalg/iterative.cpp:733-875`. Actual `FgmresSolver::Mult` body ends at line 871; lines 872-875 are part of explicit-template-instantiation declarations at file scope. RE-ANCHOR to `733-871`.

**Cycle 70 (GMRES L0.3 GeneratePlaneRotation)**: cited a single range, but the function has separate real and complex specializations at different line ranges (36 lines real, 112 lines complex). SPLIT to `L0.3a` (real specialization) and `L0.3b` (complex specialization).

## Cross-references

- Applied by Explorer when emitting L0 citations (`prompts/explorer.md` *Method* step 2-3).
- Applied by Critic when verifying citations (Critic check #1 *citation_does_not_support* — boundary drift is a fail mode).
- Related: cycle 21 GMRES `OrthogonalizeIteration` L0.7 originally cited 307-330, audit narrowed to 307-326 (function body) plus a separate citation for the dispatch macro outside the body.
