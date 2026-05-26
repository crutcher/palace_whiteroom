# Scaffolding

The agent-side workshop. Cross-cutting notes, hypotheses, decision logs, and breadcrumbs that don't belong to any one slice and aren't otherwise channeled.

The book is the deliverable; scaffolding is the workshop. The workshop is not pruned for the deliverable's neatness.

## When to write here

Content that fits when:

- The note **spans multiple slices** ("L1 forms for CG and GMRES both reach for an `axpy`-shaped primitive — extractable").
- The note is a **decision log** ("considered representing residual norm at L4 as a record output vs. a separate ledger; chose record output because §3.8 demand-driven pruning makes the cost free").
- The note is a **hypothesis or open observation** that's not yet a question about source code and not yet a load-bearing claim ("I think the L2→L3 obstruction for Gauss-Seidel-flavored kernels generalizes — flag for the next time we touch a smoother").
- The note is a **methodology breadcrumb** ("the L4 calculus seems weak on representing T; provisional, escalates if it recurs").

**Small-scope speculative content is default-accepted.** Friction with what's been written is identified from use, not from prior design.

## Running ledgers (Phase B onward)

The following files are **running ledgers** — appendable cumulative state read and written by agents each cycle. See `../MIGRATION.md` Section 2 *Scaffolding layout* for the full read/write matrix.

- **`friction-ledger.md`** — named friction patterns + recurrence counts (meta-phase-maintained).
- **`skill-candidates.md`** — appendable skill proposals (any agent can append).
- **`open-questions.md`** — open questions about target source or methodology (any agent appends; integrator promotes per-report caveats; meta-phase reviews periodically).
- **`cycle-record.jsonl`** — per-cycle structured record (integrator + meta-phase append; replaces `episodic.jsonl`).
- **`problems-sensitivity.md`** — self-tuning sensitivity calibration for `problems/` (meta-phase-maintained).
- **`roadmap.md`** — relative-progress vs roadmap goals (integrator-maintained).
- **`priorities.md`** *(planned)* — short next-up list (meta-phase + cycle-planner co-edit).
- **`concept-dependency-map.md`** — cross-concept dep graph (kept; consumed by layer-intro-author).
- **`decisions/<topic>.md`** — persistent-dual trade-off logs (sub-agent appendable).
- **`test-linkages/<topic>.md`** — source→test maps (sub-agent appendable).

## When *not* to write here

These have their own channels and should not pollute `scaffolding/`:

- **Slice-local working notes** → that slice's `## Working Notes` section in `book/src/spec/slices/<X>.md` (or `book/src/L_n/<operator>.md` under the new layout).
- **Per-report artifacts** → `reports/<id>/REPORT.md` (under the new cycle structure).
- **Out-of-role authority concerns** → `problems/`.

The old channels — `lessons.md` (historical record, kept), `questions.md` (archived seed questions, kept), `episodic.jsonl` (moved to `scaffolding/cycle-record.jsonl`) — are superseded by the running ledgers above.

## Discipline

- **Append-only structurally.** New files OK; appending to existing files OK; adding subsections within an existing file's domain OK. Renames, moves, directory reorganizations, and content migration between files require meta-review (Medium cascade).
- **Stale entries are marked, not deleted.** `<!-- STALE: superseded by <link> -->` at the top of the affected section. The original content stays for audit value.
- **Promotion leaves a stub.** When a scaffolding note crystallizes into a load-bearing artifact in `book/` (a concept entry, a methodology section, a design decision), the substance moves and the scaffolding entry stays as a `→ promoted to <link>` stub. The breadcrumb has audit value even after the substance has migrated.

## File naming

Free-form. Suggested patterns:

- `<topic>.md` — running notes on a recurring topic.
- `<YYYY-MM-DD>-<short-slug>.md` — dated entries when chronological order matters more than topic affinity.
- `cross-slice/<observation>.md` — multi-slice observations.
- `decisions/<decision>.md` — decision logs.

Reach for a subdirectory when a topic accumulates 3+ related files. Keep flat otherwise.

## Access during cycles

Per-cycle agents (Explorer, Synthesizer, Critic) read **prior cycles'** scaffolding as input — same as they read `book/src/`. The Critic does **not** see the Synthesizer's scaffolding output from the **current** cycle; the no-shared-context invariant covers freshly-written scaffolding from the in-flight cycle the same way it covers live chains-of-thought. The orchestrator filters by commit-boundary / mtime.

## Lifecycle

Reviewed by the Meta-Critic during meta-review. Patterns: clustered notes pointing at the same friction may motivate a methodology change or a `concepts/` extraction; stale notes get marked; orphaned notes get retired (still not deleted).
