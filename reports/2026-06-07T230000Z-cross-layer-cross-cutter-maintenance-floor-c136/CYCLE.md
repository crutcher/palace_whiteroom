---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-07T230000Z
scope: L-stack maintenance-floor standing hygiene — c136 (batch-44 OPENER; first per-BATCH sweep on the new cadence)
status: integrated
integrated_at: 2026-06-07T230000Z
integration_commit: 5828a07
integration_notes: |
  Applied cycle-136 (batch-44 LEAD/OPENER). AUDIT-CLASS clean-bill — NO book mutation; the only artifact write was the OQ promotion (synthesis-edges-next-batch-maintenance-floor-audit) + the staging row. The first per-BATCH-cadence maintenance-floor sweep (batch-43-enacted). No proposed-changes block; nothing to apply to book/.
---

# CYCLE: Cross-layer observation — maintenance-floor c136 clean-bill (batch-44 opener; Synthesis-LEAD surround)

## Summary

Standing maintenance-floor hygiene audit for c136 — the **OPENER of meta-batch-44** and the **first run on the new per-BATCH sweep cadence** the batch-43 meta enacted (`ad9e2b2`: full-hygiene sweep moves to one dedicated dispatch per batch; the per-cycle floor is now the lightweight `integrator-finalize` step-5b two-invariant tripwire). **Clean-bill: the disposition HELDS EXACTLY vs the c134/c135 re-baseline, all hard invariants intact, no stale-token drift, the three `realizes-kernel-api` edges stay `reference`-class, KaTeX `$`-sigil fence compliance holds, and DIRECTIVE-1 boundary holds.** The graded-stack lint reports `files=386, typed=325, untyped=61, roots=45, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=11, reachable=163, reference_reachable=247, detritus=123, true_detritus=51`, rank-histogram `roadmap_goal=4` — byte-for-byte identical to the c134-enacted re-baseline (`log/cycle-134.md:17`), held through c135 and now c136. This batch's LEAD is the new `# Synthesis` Part (wave-mate `layer-intro-author`, scope `synthesis-section-shell`); it is **NOT yet on disk** — this sweep covers the EXISTING artifact and forward-flags the incoming `synthesis/` edges for next batch's sweep. Audit-class clean-bill; NO `book/` mutation.

## Observation kind

**Audit residue** (standing-hygiene clean-bill). No coverage gap, edge-label mismatch, consistency drift, or vocabulary mismatch surfaced. One forward-looking note (the incoming Synthesis Part) recorded for the next sweep.

## Specific finding

### (i) hard invariants + disposition re-check — PASS (held exactly)

- `python3 tools/graded-stack-lint/graded_stack_lint.py --json` reports **`rank_violations=0`, `unresolved_depends_on_targets=0`** (the two per-cycle tripwire invariants) and the full totals `files=386, typed=325, untyped=61, roots=45, promotion_frontier=11, reachable=163, reference_reachable=247, detritus=123, true_detritus=51`, rank-histogram `firm=224, typed-no-rank=84, rough-in=4, partly-constructive=3, obstruction=2, partial-obstruction=4, roadmap_goal=4`.
- This **matches the c134-enacted re-baseline byte-for-byte** (`log/cycle-134.md:17`) and the c135 clean-bill (`reports/2026-06-07T210728Z-cross-layer-cross-cutter-maintenance-floor-c135/CYCLE.md:16`). No node maturity moved c135→c136 (c135 was batch-closing consolidation; c136-D-LEAD Synthesis authoring had not landed at dispatch time). Stable across c134/c135/c136.
- **RE-set premises HELD.** RE4 stays consumer-gated (no GMRES-variant feature column on disk — `feature/*gmres*` absent; the named-consumer promotion condition remains unfired). The sharding `roadmap_goal` node (`L4/sharding-decompose-reduce`) carries the standard `roadmap_goal` promotion path and remains a reference-emitting leaf under the **§2g extension the batch-43 meta enacted** (now formally covers reference-emitting `roadmap_goal` leaves — TEE-UP 1 from c135 was resolved as EXTEND, not a fresh RE; `ad9e2b2`). The RE11 §2g escalate-guard does NOT fire — `detritus=123` held (no climb).
- `roadmap_goal` bucket = 4 (held): `L4/sharding-decompose-reduce` + the 3 pre-existing rank-0 chapters. No new rank-0 landing this cycle.

### (ii) kernel-API/impl integrity — PASS

All three `realizes-kernel-api` edges sit under `reference:` blocks (navigational, free; do NOT block, do NOT constrain rank, do NOT carry liveness), confirmed on disk:
- `book/src/L1/multigrid-relaxation-smoother.md:24-26` — `reference:` block, `kind: realizes-kernel-api` (the kept opaque GS-SSOR / `triangular-solve-obstruction` kernel-api). A separate `depends-on:` block (`:15`) carries the from-our-primitives constituents; the kernel-api edge is correctly NOT in it.
- `book/src/L1/libceed-quadrature-kernel-impl.md:21-23` — `reference:` block, `kind: realizes-kernel-api` (the libCEED element-quadrature kernel-api obstruction surface). The `depends-on:` block (`:28`) is separate.
- `book/src/L3/eigsolve-impl.md:19-23` — `reference:` block, TWO `kind: realizes-kernel-api` edges (the L3 `eigsolve` partial-obstruction kernel-api + the L4 Solve-monadic cap sibling). The `depends-on:` block (`:8`) is separate.

The impl nodes do NOT `depends-on` their opaque APIs; the correspondence is review-only per DIRECTIVE-3. No new linter edge-semantics required (the `kind:` label is documentation the linters ignore).

### (iii) semantic-surface liveness — PASS

`book/src/semantics/index.md` carries no stale path/anchor drift: a grep for the pre-c116 `design/l4_calculus` home, `book/src/design`, `REPORT.md`, or the deleted `spec/slices` corpus returns 0 matches. The cycle-116 relocation into the active semantic-management surface is clean; no degenerate identity-lowering smell or restated-semantics detritus surfaced this sweep.

### (iv) KaTeX `$`-sigil fence compliance — PASS

A whole-artifact scan for the `$`-sigil rendering collision (`project_katex_dollar_sigil_fence_requirement`: a `$S`/`$N`-style named-shape-group sigil in a 4-space-indented Markdown-implicit-code block collides with the KaTeX `$...$` delimiter, so it MUST be inside a ` ```text ` fence) returns **one apparent hit, confirmed a FALSE POSITIVE**:
- `book/src/L4/sharding-decompose-reduce.md:83` — `"a monoid homomorphism from \`([(Scalar,Tensor)], ++, [])\` to \`(Tensor[$S], +, zeros)\`"`. This is a **list-item continuation line** (the `- ` bullet starts at `:81`), and the `$S` sits **inside an inline backtick span** (`` `(Tensor[$S], +, zeros)` ``). Inline-code spans do not render as KaTeX, and this is prose-continuation indentation, NOT a 4-space implicit code block. The sigil is already protected. No defect; no action.
- The integrator-finalize step-5c post-build assertion (no `<pre>` may contain `class="katex"`) is the durable mechanical guard that backstops this — this sweep's source-level scan agrees with that guard.

### (v) DIRECTIVE-1 boundary — HELD

No MPI/distributed version is lifted. The only `roadmap_goal` touching sharding (`L4/sharding-decompose-reduce`) lifts the sharding-MATH decomposition-abstraction ONLY, with `reference`-class edges to the 5 firm reduce roots and MPI mechanics (`linalg/rap.*` `ParOperator`/RAP, `utils/geodata.*` distribution, `utils/dorfler.*` cross-rank bisection) cited as deferred mechanism, NEVER lifted. The Dörfler cross-rank bisection stays deferred (`book/src/L1/dorfler_mark.md`, OQ `dorfler-cross-rank-bisection-distributed-note-deferred`). No book node carries a blocking `depends-on` onto the MPI-associated version.

### (vi) FORWARD-LOOKING NOTE — the incoming `# Synthesis` Part (next batch's sweep covers it)

The batch-44 LEAD is the new top-level `# Synthesis` Part (user directive 2026-06-07; wave-mate `layer-intro-author`, scope `synthesis-section-shell`). **It is NOT yet on disk** — `book/src/synthesis/` does not exist and `SUMMARY.md` carries no `synthesis` entry at this sweep's dispatch time, so this audit correctly covers ONLY the existing artifact. **Forward-looking note for the next per-batch maintenance-floor sweep (batch-45, or whenever the Synthesis Part has landed):** the new `synthesis/` chapters are an **implementation-rendering VIEW** that LINKS to the authoritative L4/semantics defs — its outbound edges to the L4 operator chapters / `semantics/index.md` / `concepts/<record>.md` should be **`reference`-class** (navigational, free — Synthesis renders, it does not depend-on for build/rank/liveness), and any `#extern NAME` kernel callouts should trace to the kernel-API nodes via `reference`-class edges (the `realizes-kernel-api` correspondence-review pattern). The next sweep should: (a) confirm the `synthesis/` edges are `reference`-class (a Synthesis chapter pulling an L4 op `depends-on` would mis-type the rendering relationship as a build dependency); (b) re-run the KaTeX `$`-sigil fence scan over the new L4-pseudo-language def bodies (Synthesis renders concrete defs in the same notation, so it is `$`-sigil-fence-relevant); (c) check the new chapters do not RE-STATE semantics already owned by L4/`semantics/index.md` (the implementation-rendering VIEW must USE+LINK, not duplicate — the SEMANTIC-CONSOLIDATION discipline). No action this cycle — recorded so the signal is not lost.

## Recommendation

**Defer — clean-bill, no follow-up dispatch warranted.** This is the audit-class per-batch maintenance-floor sweep; all standing invariants hold and the disposition is stable across c134/c135/c136. No `book/` mutation needed (no stale token surfaced; the one KaTeX hit is a confirmed false positive). The single forward-looking note (the incoming Synthesis Part's `reference`-class edge correctness + `$`-sigil-fence + no-semantic-restatement coverage) is recorded for the **next** per-batch sweep once `synthesis/` is on disk — it is NOT actionable this cycle and is NOT a defect.

## Supporting evidence

- `tools/graded-stack-lint/graded_stack_lint.py --json` — c136 disposition (`rank_violations=0`, `unresolved=0`; `files=386, typed=325, reachable=163, reference_reachable=247, detritus=123, true_detritus=51, promotion_frontier=11, roadmap_goal=4`), matches the c134 re-baseline (`log/cycle-134.md:17`) and the c135 clean-bill.
- `book/src/L1/multigrid-relaxation-smoother.md:24-26`, `book/src/L1/libceed-quadrature-kernel-impl.md:21-23`, `book/src/L3/eigsolve-impl.md:19-23` — the three `realizes-kernel-api` edges, all under `reference:` blocks, each with a SEPARATE `depends-on:` block for the from-our-primitives constituents.
- `book/src/semantics/index.md` — no stale path/anchor drift (grep for `design/l4_calculus|book/src/design|REPORT.md|spec/slices` returns 0).
- `book/src/L4/sharding-decompose-reduce.md:81-83` — the one KaTeX `$`-sigil scan hit, confirmed a false positive (inline-backtick span inside a list-item continuation, not a 4-space code block).
- `book/src/L1/dorfler_mark.md` + OQ `dorfler-cross-rank-bisection-distributed-note-deferred` — Dörfler cross-rank bisection deferred (DIRECTIVE-1).
- `git log` `ad9e2b2` (batch-43 meta) — enacted: §2g extension to reference-emitting `roadmap_goal` leaves + maintenance-floor cadence change (full sweep per-batch; per-cycle tripwire is step-5b).
- Absence: `book/src/synthesis/` does not exist; `SUMMARY.md` has no `synthesis` entry (the incoming LEAD Part is not yet on disk).

## Open questions / caveats

- This is the FIRST sweep on the new per-BATCH cadence (batch-43 meta `ad9e2b2`): the full-hygiene sweep is now once-per-batch (this dispatch), and the per-cycle floor is the existing `integrator-finalize` step-5b two-invariant tripwire (`rank_violations==0` + no newly-orphaned node + the detritus-count escalate-guard, one command, no dedicated dispatch). No dedicated maintenance-floor cross-cutter is dispatched every cycle anymore.
- The forward-looking Synthesis note (finding vi) is NOT a defect and NOT actionable this cycle — the Part is not on disk. It is recorded so the next per-batch sweep audits the new `synthesis/` edges for `reference`-class correctness, `$`-sigil-fence compliance in the rendered def bodies, and no-semantic-restatement. If the wave-mate's Synthesis authoring lands new `reference`-class edges this same batch, the linter disposition is EXPECTED to move BY DESIGN (new files + new `reference`-class edges); the two hard invariants (`rank_violations`, `unresolved`) must still hold — the step-5b per-cycle tripwire will catch any regression at finalize.
- No baseline-exception ledger edit needed: `scaffolding/graded-stack-baseline-exceptions.md` remains the closed c094→c096 burn-down record with 0 tracked open exceptions; the live disposition lives in the per-cycle signal trail + `log/`, and the §2g-extension disposition for the sharding node is recorded in the batch-43 meta section of that ledger (`ad9e2b2`).
