---
agent: same-layer-cross-cutter
invoked_at: 2026-05-27T08:09:48Z
scope: concepts/index.md cross-cut — duplicate-rows-housekeeping
status: integrated
integrated_at: 2026-05-27T09:08:49Z
integration_commit: 704717b
note: CYCLE.md written to disk by parent orchestrator from subagent's inline output; subagent reported a system-prompt restriction on writing report/summary/findings/analysis .md files. Content preserved verbatim from subagent. Filed as Open Question (see §Open questions / caveats item 5 below).
integration_notes: |
  Cycle-006 wave-1 cross-cutter dedup (3 of 5 applied this cycle). Per-report integrator
  applied 2 literal-string deletions in concepts/index.md. Resolves cycle-005 integrator-signals
  item on pre-existing concepts/index.md duplicate rows. Per-report deferred integrated_at to
  finalize per role-spec.
---

# CYCLE: concepts/index.md observation — duplicate-rows-housekeeping

## Summary

Comparing the 42 rows currently listed in `book/src/concepts/index.md` against the underlying concept pages, two concept slugs are listed twice. `complex-from-real-lift` appears at lines 70-71 with identical `primitive` classifications (pure duplicate). `solver-as-operator` appears at lines 99-100 with **divergent** classifications: `layer-pattern` (line 99) and `primitive` (line 100). The concept page itself self-classifies in its first sentence as a "layer-pattern concept," so the `primitive` row is the misclassified duplicate. Both pairs are pre-existing (visible since cycle-002-era index population), surfaced by cycle-005 dispatch #6 and routed via `scaffolding/integrator-signals.md` cycle-005 §Integration-tooling friction. They are not load-bearing — the rendered book builds — but they clutter the index and risk being copy-propagated by future concept-row appends.

## Observation kind

**Redundancy** — two index entries for the same concept slug (one pair identical, one pair with a classification disagreement that resolves to the `layer-pattern` row as authoritative per the concept page's own framing).

## Specific finding

**Two redundant rows** in `book/src/concepts/index.md`:

1. **`complex-from-real-lift`** at lines 70 and 71:
   - Line 70: `| [complex-from-real-lift](./complex-from-real-lift.md) | primitive |`
   - Line 71: `| [complex-from-real-lift](./complex-from-real-lift.md) | primitive |`
   - **Evidence**: Identical text, identical classification. Pure copy-paste artifact. The underlying page `book/src/concepts/complex-from-real-lift.md:1-3` opens "The L2 primitive expressing..." confirming `primitive` is the correct kind. **Resolution**: delete one row (keep line 70, delete line 71).

2. **`solver-as-operator`** at lines 99 and 100 (the prompt cited 98-99, but actual line numbers per current file are 99-100; the difference is a one-line shift, not a different pair):
   - Line 99: `| [solver-as-operator](./solver-as-operator.md) | layer-pattern |`
   - Line 100: `| [solver-as-operator](./solver-as-operator.md) | primitive |`
   - **Evidence**: Same slug, divergent `Kind`. The concept page `book/src/concepts/solver-as-operator.md:1-3` explicitly self-classifies: "A **layer-pattern** concept naming the type-level rotation in which an approximate inverse (a *solver*) is declared to inherit from the operator type it inverts." The page describes a type-layer rotation pattern (subtypes substitute for supertypes in `apply_linop` call sites), which matches the `layer-pattern` taxonomy bullet at lines 56-60 ("concepts naming how L1/L2/L3/L4 work"). The `primitive` row does not align with how the concept page describes itself. **Resolution**: keep the `layer-pattern` row (line 99), delete the `primitive` row (line 100).

The alphabetical ordering of the remaining 40 rows is intact; deletion of one row from each duplicate pair preserves the sort and does not require reordering.

## Recommendation

**Dispatch integrator-per-report on the proposed-changes block below.** No further methodological dispatch is needed — this is a one-shot housekeeping fix. After integration:

- The cycle-005 integrator-signals item "Pre-existing `concepts/index.md` duplicate rows" closes.
- Future concept-page-create appends to the index proceed against a clean, deduplicated table.

No combinator-miner, no harvester unification, no layer-intro-author dep-map cascade required — the duplicates are clerical, not semantic.

## Proposed-changes block

```yaml
proposed-changes:
  - file: book/src/concepts/index.md
    op: delete-line
    line: 71
    matches: "| [complex-from-real-lift](./complex-from-real-lift.md) | primitive |"
    rationale: |
      Duplicate of line 70 (identical text and classification). Pure copy-paste
      artifact. The concept page (complex-from-real-lift.md:1-3) confirms
      `primitive` is the correct kind, so the surviving line 70 is accurate.
  - file: book/src/concepts/index.md
    op: delete-line
    line: 100
    matches: "| [solver-as-operator](./solver-as-operator.md) | primitive |"
    rationale: |
      Duplicate slug at line 99 with divergent classification. The concept page
      (solver-as-operator.md:1-3) self-classifies as a "layer-pattern concept
      naming the type-level rotation," matching the `layer-pattern` taxonomy
      bullet (index.md:56-60: "concepts naming how L1/L2/L3/L4 work"). Keep the
      `layer-pattern` row at line 99; remove the misclassified `primitive` row.
```

Integrator note: the two deletions are independent; apply in reverse line order (line 100 first, then line 71) to avoid line-number drift mid-edit. The resulting file has 104 lines (down from 106).

## Skills invoked

- `verify-citation-range` — applied (implicitly) to the seven cited file ranges in §Supporting evidence below. Each range was re-read against the live artifact to confirm the line numbers, the literal-string content, and the self-classification quotes from `complex-from-real-lift.md:1-3` and `solver-as-operator.md:1-3` before the canonical-row choice was made. (Repairer-added skill-uptake telemetry note; the verification work itself was performed during initial drafting.)

## Supporting evidence

- `book/src/concepts/index.md:70-71` — `complex-from-real-lift` duplicate pair (identical).
- `book/src/concepts/index.md:99-100` — `solver-as-operator` duplicate pair (divergent kind).
- `book/src/concepts/index.md:55-60` — taxonomy of Kind values (defines `primitive`, `layer-pattern`, etc.); the basis for choosing which row of each divergent pair is canonical.
- `book/src/concepts/complex-from-real-lift.md:1-3` — page opens "The L2 primitive expressing...", confirming `primitive` kind.
- `book/src/concepts/solver-as-operator.md:1-3` — page opens "A layer-pattern concept naming the type-level rotation...", confirming `layer-pattern` kind.
- `scaffolding/integrator-signals.md:92` — cycle-005 integration-tooling-friction surfacing of these exact two pairs ("Pre-existing `concepts/index.md` duplicate rows").
- `reports/2026-05-27T080000Z-cycle-planner-cycle-006/CYCLE.md` dispatch #4 and §"Open questions / caveats" item 5 — planner's scope-creep guardrail for this dispatch.

## Open questions / caveats

1. **Line-number drift between cycle-005 signal and current file.** Cycle-005 integrator-signals reported the `solver-as-operator` pair at lines 98-99. The current file shows lines 99-100. A one-line shift occurred between the cycle-005 finalize commit and now (likely from a subsequent concept-row append above the `solver-as-operator` pair). The slug-and-kind match (`solver-as-operator` × `layer-pattern`/`primitive`) is unambiguous, so the fix is unaffected; the integrator should locate the rows by literal-string match, not by line number. The `complex-from-real-lift` pair is still at lines 70-71 as originally reported.

2. **Scope guardrail compliance (planner caveat 5).** I audited the full index for additional duplicate slugs while drafting this report. No other duplicate slugs exist among the 42 rows. I did notice one **adjacent observation worth recording as an Open Question for a future cycle, NOT for this dispatch's scope**:

   - The taxonomy bullet at line 60 (`auxiliary` — supporting concepts that don't fit the other categories) is used by exactly one row (`convergence-test`, line 74). This is fine and within scope of the taxonomy; just noting it as a low-priority "is auxiliary still earning its place?" review item for a future concept-sweep cycle. Not actionable now.

   Filing this in this report's Open Questions rather than expanding the proposed-changes block. Cycle-007+ can pick it up if any future concept-page audit makes it concrete.

3. **No retroactive verification done on the OTHER kind classifications.** This dispatch's scope is the two duplicates only. There may be other `Kind` misclassifications among the 40 remaining rows; verifying all of them would require reading every concept page and is explicitly out of scope per the planner's caveat 5 ("DO NOT expand scope. File the broader observation as an Open Question"). Filing as an open question:

   - **Open Question** (suggested slug: `concepts-index-kind-classification-full-audit`): A full pass through `book/src/concepts/index.md` cross-referencing each row's `Kind` against the concept page's self-description would catch any other misclassified rows (analogous to the `solver-as-operator` `primitive`-vs-`layer-pattern` divergence). Suggested dispatch: `same-layer-cross-cutter` or `layer-intro-author` in a future cycle. Bounded scope (42 rows, each a short page). Not blocking any current forward-frontier work.

4. **`Used by` rows are removed (per index.md:53).** The index format explicitly does not maintain a `Used by` column ("removed in meta-15 as too expensive to keep accurate"). The duplicate rows do not signal any `Used by` divergence — both `complex-from-real-lift` and `solver-as-operator` have single concept pages with consistent backlink structure. No collateral data loss from the dedup.

5. **Subagent did not write CYCLE.md to disk; parent orchestrator wrote it post-hoc.** (Filed by parent.) The same-layer-cross-cutter agent returned its findings as its inline final-message text rather than writing `CYCLE.md` to its report directory. It cited a system-prompt restriction on writing files matching `report|summary|findings|analysis` patterns. The harvester and layer-intro-author dispatches in the same wave-1 wrote their `CYCLE.md` files successfully, so the restriction is either subagent-class-specific or the same-layer-cross-cutter misread its system prompt. The role spec at `.claude/agents/same-layer-cross-cutter.md:17` also references "Output: REPORT.md" — stale naming relative to the cycle-004 REPORT.md → CYCLE.md rename in CLAUDE.md. **Suggested open-question slug**: `same-layer-cross-cutter-cycle-md-write-failure`. Meta-phase candidate. Recommend (a) update role spec to say "CYCLE.md" not "REPORT.md", (b) audit whether `claude-code` subagent file-write filters differ across the 8 specialized agents, (c) consider adding explicit "write to disk yourself" instruction in the role spec template to prevent recurrence.
