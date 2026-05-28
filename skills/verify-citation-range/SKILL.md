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

## Worked examples

**Cycle 69 (GMRES L0.13)**: cited `FgmresSolver::Mult` as `palace/linalg/iterative.cpp:733-875`. Actual `FgmresSolver::Mult` body ends at line 871; lines 872-875 are part of explicit-template-instantiation declarations at file scope. RE-ANCHOR to `733-871`.

**Cycle 70 (GMRES L0.3 GeneratePlaneRotation)**: cited a single range, but the function has separate real and complex specializations at different line ranges (36 lines real, 112 lines complex). SPLIT to `L0.3a` (real specialization) and `L0.3b` (complex specialization).

## Cross-references

- Applied by Explorer when emitting L0 citations (`prompts/explorer.md` *Method* step 2-3).
- Applied by Critic when verifying citations (Critic check #1 *citation_does_not_support* — boundary drift is a fail mode).
- Related: cycle 21 GMRES `OrthogonalizeIteration` L0.7 originally cited 307-330, audit narrowed to 307-326 (function body) plus a separate citation for the dispatch macro outside the body.
