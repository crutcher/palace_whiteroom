---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T201327Z
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
repaired_at: 2026-06-04T202000Z
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

# META: verification of CYCLE — graded-stack linters (P0-B)

## Critique

This report is a **TOOLING** deliverable (two linters under `tools/graded-stack-lint/`),
not a `book/` artifact entry, per the dispatch prompt. The subject-DAG checks
(surface-or-evidence, rotation-quality, variant-axis-coverage, edge-label-fidelity) therefore
no-op. The substantive verification is empirical: the tool exists on disk, so I ran it and
reproduced its reported output. The single finding is a numeric imprecision in one caveat;
everything load-bearing checks out.

### Checks run

- **citation-validity — warning.** The report's claims about D1's scheme
  (`graded-stack-scheme.md`) and `METHODOLOGY-GRADED-STACK.md` §4 are accurate; I cross-read
  both. The dry-run numbers reproduce **exactly** (see point (d) below). The one inaccuracy:
  CYCLE.md:178-180 states "18 of the 36 feature-column files promoted off `seed` to
  `status: firm`". On disk the count is **21 `status: firm` / 15 `status: seed`** among the 36
  feature files (`grep -c` over `book/src/feature/*.md`). The qualitative claim (a large chunk
  promoted off seed, so a naive "root = has `seed`" rule would drop them and collapse the GC) is
  correct and is the load-bearing motivation for the categorical-root decision — but the stated
  "18" is off by 3 from the on-disk "21". Warning, not fail: it is a number inside a transitional
  caveat, not a behavioral or contract claim, and it does not affect the implemented logic (the
  categorical-root rule keys on `kind: feature-surface`, not on the count).

- **surface-or-evidence — pass.** Not applicable to the tooling kind: this dispatch authored no
  operator/theme surface and makes no per-op algebraic claim. Record-definition sub-check: N/A —
  no signatures naming an undefined record (the report itself flags this, CYCLE.md:158-159). The
  report's evidence shape is the tool source + its reproducible dry-run, which is the correct
  evidence for a linter deliverable.

- **rotation-quality — pass.** Not applicable to the tooling kind (no algebraic/structural
  rotation asserted).

- **variant-axis-coverage — pass.** Not applicable to the tooling kind. For the record, the
  linter's *own* option surface is covered: `--strict` (unresolved-as-failure), the transitional
  dual-form root (`feature_root: seed` / legacy `status: seed` / promoted-off-seed column), and
  the migration mapping for all three legacy edge representations are each present and exercised.

- **cross-reference-integrity — pass.** All four delivered files resolve on disk
  (`graded_stack_lint.py`, `README.md`, `requirements.txt`, `fixture/`). The parse contract the
  report claims to implement (CYCLE.md:75-93) matches D1's scheme §1-§5 on every point I checked:
  rank ladder + 2.5 sub-rank (graded_stack_lint.py:52-60 vs scheme §1 table), rank read-priority
  `rank: → firmness: → status:(non-seed) → ## Status` (derive_rank, lines 328-359 vs scheme §1/§5),
  the `edges:` grammar with bare-string AND `{target:, kind:}` forms with `kind` ignored
  (lines 405-419, 228-245), the migration mapping `depends_on`/`lowers_to`/`lifts_from`/`consumes`/
  `composes`(vocab→depends-on, sibling→reference)/`l0_ground_truth`(cite, not a node)
  (lines 421-452 vs scheme §4 table), and the lowering-theme `rank ≤ min(endpoints)` post-pass
  (apply_lowering_theme_ranks, lines 473-488 vs scheme §5). No divergence from D1 found.

- **edge-label-fidelity — pass.** Not applicable (no L_{n+1}→L_n edge label on a tooling report).

- **plan-kind-consistency — pass.** Content shape (deliver + dry-run-validate two linters; no
  `book/` edit) matches the declared P0-B scope. The "Proposed changes: None to book/"
  (CYCLE.md:61-66) is correct for tooling territory and consistent with the role/write-authority
  partition.

- **skill-uptake-survey — pass.** No relevant skill is implied beyond the citecheck-mirroring
  tool-authoring convention the report already follows (stdlib-only, `<tool>.py` + README +
  requirements layout).

### Verification of the five prompt focus points

- **(a) parse contract vs D1's landed scheme — confirmed.** See cross-reference-integrity above.
  The rank-ladder mapping, the `edges:` grammar, the lowering-theme `rank=min(endpoints)` rule,
  and the dual-form `seed`/`feature_root` handling are all implemented per D1's spec. No divergence.

- **(b) algorithm correctness vs §4 — confirmed.** Rank-invariant direction: `rank_check` flags
  iff `node.rank > dep.rank` over `depends-on` edges (graded_stack_lint.py:519) — matches §4 /
  §1b `rank(u) ≤ rank(v)`. GC direction: `reachability_gc` seeds the stack with roots and pushes
  `node.depends_on` (lines 551-564) — marks forward over `depends-on` from the root set, matches §4
  "mark from the feature roots over depends-on edges."

- **(c) the two hard requirements — confirmed.** (a) Incremental-safe: untyped frontmatter sets
  the `untyped` WARNING flag (line 454) and never fails; `main` returns exit 1 only on rank
  violations (or, under `--strict`, unresolved targets) (lines 805-808). The 150 untyped real-tree
  files did NOT cause a hard failure. (b) The seed fixture exercises a KNOWN rank violation
  (`feature/widget.L4 firm → L1/weak_op rough-in`) and a KNOWN unreachable node (`L1/orphan`, firm
  yet detritus); I ran the fixture and both fire (see below).

- **(d) dry-run reproducibility — confirmed exactly.** Running
  `python3 tools/graded-stack-lint/graded_stack_lint.py --json` on the real tree:
  ```
  files=357, typed=207, untyped=150, roots=36, rank_violations=22,
  unresolved_depends_on_targets=11, promotion_frontier=30, reachable=77,
  detritus=136 (no_typed_edges=102 + with_typed_edges=34), expected_unreachable=19
  exit=1
  ```
  Every number in CYCLE.md:113-144 reproduces. The 22 rank violations are the
  `L2/normalize→L1/normalize`, `L3/dot→L2/inner_product`, `L4/gram_reduce(2.5)→L1/bilinear-form`,
  `feature/energy-fields.L4→L1/matrix-weighted-norm(2.5)` cascade the report cites — i.e. the
  linter independently rediscovers the firm-rests-on-rough-in cascade the project tracks by hand,
  which is strong evidence the rank linter is correct. The fixture run
  (`--book-src .../fixture/book/src`) reproduces `files=9, typed=8, untyped=1, roots=3,
  rank_violations=2, detritus=2, promotion_frontier=1, exit=1` (CYCLE.md:98-99) and fires every
  assertion in `fixture/README.md` (the KNOWN violation, the lowering-theme note+violation, the
  KNOWN unreachable `L1/orphan`, the legacy-seed root `L2/legacy_compose`, the
  composes→depends-on/reference split, the untyped-is-warning case).

- **(e) reconciliation points honestly surfaced — yes, with one code-comment nit.**
  - *obstruction default*: the report (CYCLE.md:166-171) states the linter treats an obstruction
    with NO `obstruction_resolution:` as **None (typed-but-rankless)**, not firm, and flags this for
    D1↔D2 sync. The implemented behavior matches the prose: `derive_rank` returns `res_val` which is
    `None` when the field is absent (line 352, 356). D1's scheme (graded-stack-scheme.md:135-137)
    specifies the firm-satisfies-consumer rule only for the *present-and-firm* case and leaves the
    absent case unspecified, so the tool's conservative None is a defensible reconciliation of a gap
    D1 left open — and it is openly flagged, not silently chosen. HONEST.
  - *permanent-categorical root vs D1's status-based seed*: the report (CYCLE.md:173-185) surfaces
    this as the resolution to OQ `graded-stack-feature-root-frontmatter-split`, with the empirical
    motivation (promoted-off-seed columns would drop out of a naive seed-only root set). The
    three-signal categorical rule is implemented (lines 393-402) and exercised by the fixture's
    `L2/legacy_compose`. HONEST.

### Issues found

- **CYCLE.md:178-180 — stale/imprecise count in a caveat (low severity).** "18 of the 36
  feature-column files promoted off `seed` to `status: firm`" — on-disk count is 21 `status: firm`
  / 15 `status: seed` (36 total). Off by 3. The qualitative claim is correct and the implemented
  categorical-root logic does not depend on this number; only the prose figure is wrong. Candidate
  for a one-word/one-number repair.

- **graded_stack_lint.py:353-355 — self-contradicting code comment (cosmetic, NOT a behavioral
  defect).** The comment says "treat a documented obstruction as firm-on-negative-structure …
  (default firm per §1f)" on lines 353-354, then says "leave it None when nothing says so" on line
  355. The code returns `None` (line 352/356), which matches line 355 AND the report's prose
  (CYCLE.md:166-170). So the *behavior* is correct and honestly documented in the report; only the
  first half of the inline comment is misleading. Not a contract or behavioral divergence — a code
  hygiene nit that could confuse a future reader of `derive_rank`. Candidate for a comment fix.

- **CYCLE.md:187-196 — 11 unresolved targets include known prose-as-slug false positives
  (surfaced honestly; NOT a defect).** Several "unresolved depends-on" targets are free-text prose
  parsed out of legacy `lowers_to:`/`consumes:` list items (e.g. `L3/apply_linop → "(no L4 entry;
  apply_linop appears inside …)"`). Confirmed by running the tool. The report correctly identifies
  these as a migration-mapping edge case for P1's hand-classification, declines to heuristically
  suppress them, and notes they are WARNINGs (not failures, `--strict` off). Recorded here only as
  confirmation that the report's honest framing is accurate — no repair needed.

## Repair

### Fixes attempted

- **Finding**: CYCLE.md:178-180 — "18 of the 36 feature-column files promoted off `seed` to `status: firm`"; on-disk count is 21 firm / 15 seed (off by 3).
  - **Decision**: repaired
  - **Action**: Independently re-verified the on-disk count (`grep -c "^status: firm"` / `"^status: seed"` over `book/src/feature/*.md` → 21 firm, 15 seed, 40 files total of which 36 carry a status line). Edited CYCLE.md §"DECISION carried from D1 — transitional dual-form seed" to read "21 of the 36 feature-column files promoted off seed". A one-number correction in a transitional caveat; the qualitative motivation (a large chunk promoted off seed so a naive seed-only root rule collapses the GC) is unchanged and remains the load-bearing argument for the categorical-root decision. The implemented categorical-root logic keys on `kind: feature-surface`, not on this count, so no behavioral content was touched.

- **Finding**: graded_stack_lint.py:353-355 — self-contradicting inline comment ("default firm per §1f" vs "leave it None when nothing says so"); code correctly returns None and report prose is correct.
  - **Decision**: repaired
  - **Action**: Rewrote the `derive_rank` inline comment in `tools/graded-stack-lint/graded_stack_lint.py` (obstruction branch) to describe the actual behavior — use the declared `obstruction_resolution` rank when present, else leave it None (typed-but-rankless) rather than defaulting to firm — and kept the D1↔D2 sync note. Comment-only change; no code path altered. Re-ran `graded_stack_lint.py --json` over the real tree afterward: every total reproduces exactly (files=357, typed=207, roots=36, rank_violations=22, detritus=136, …), confirming behavior is unchanged. (This is a `tools/` file, in repair scope per the role spec; not a `book/` artifact.)

- **Finding**: CYCLE.md:187-196 — 11 unresolved-target false positives from prose-in-frontmatter, surfaced honestly by the report as P1 migration-mapping input.
  - **Decision**: not-needed
  - **Action**: None. The critic recorded this as accurate honest framing, not a defect. No repair authority engaged.

### Unrepairable findings

None. Both real issues were mechanical/surgical (one prose number, one cosmetic code comment) and fully in repair scope.

## Suggested resolution

`ready`. Both citation-validity issues are corrected: the feature-column promotion count now matches disk (21 firm / 15 seed, independently verified), and the misleading obstruction-default comment in the linter now matches the code's actual None-returning behavior (verified by re-running the tool — totals unchanged). All other checks passed from the critic. No follow-up agent needed. Note for the integrator: the new tooling lives under `tools/graded-stack-lint/` (written directly per `tools/` territory, NOT via proposed-changes blocks); the report flags the integrator-finalize `--json` wiring as batch-30 meta-phase intake, not a `book/` edit.
