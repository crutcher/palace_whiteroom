# verify-dispatch-scope-not-already-discharged

**Promoted:** cycle-033 meta-phase (batch-9). **Proposer:** abstractor (cycle-031 D6 no-op) + layer-intro-author (cycle-031 D6-reroute no-op); promoted on recurrence-3 across batch-9 (c031 file-existence-staleness, c032 broader 4-of-6 deliverable-presence-staleness, c033 working precedent). **Working precedent:** `reports/2026-05-30T150000Z-cycle-planner-cycle-033/CYCLE.md` §"Deliverable-presence verification (cycle-033 deeper-check enforcement per c032 orchestrator signal)" — the c033 cycle-planner ran the procedure inline per-dispatch and landed 3/3 genuinely-open dispatches; that section is the canonical worked example.

**Audience:** cycle-planner (the primary user; runs the procedure pre-dispatch). Also: orchestrator (the safety net — runs the same procedure when the planner skipped it).

**Companion friction-ledger:** `cycle-planner-stale-priorities-line-recruitment` (the friction this skill addresses; sibling-and-deeper of `cycle-planner-reproposes-already-landed-work`, whose c027 file-existence bullet was necessary but insufficient).

## Motivating observation

The cycle-027 cycle-planner §Discipline bullet "verify each candidate is genuinely OPEN" checks the *cycle-record trail* (`counts_after`, STAGING.md, struck-Backlog markers). This catches **file-existence staleness** (the work has obviously landed and is visible in the cycle-record). But it does NOT catch the deeper **deliverable-presence staleness** — situations where a file/theme exists on disk but a dispatch against it would still be a no-op:

- **(i) Firm-on-disk-already-at-proposed-maturity** — c031 D6 examples (`nleps-jacobian-action-mutation-rotation`, `concepts/eigsolve`): files firm-landed c025, the priorities lines were six cycles out of date, the file-existence check would have detected this if applied, but the planner did not apply it (the c031 incident is what surfaced the need for the codified check).
- **(ii) Audit-already-discharged** — c032 D6 examples: 4 batch-6 themes (`apply-nonlinear-pencil-mutation-rotation`, `deflate-composition-lowering`, `gram-fold-specialization`, `orthogonalize-composition-lowering`) ALREADY have `verified_against:` blocks on disk; re-proposing a lowering-verifier audit on each is a no-op (the audit block is the deliverable, and it's already there).
- **(iii) Slice-audit-completed-immediately-prior-cycle** — c032 D3 example: re-proposed the `sparse_triangular_solve` slice-reduction audit that landed c031 with verdict DEFER; the RESOLVED disposition is in the c031 OQ ledger.
- **(iv) Structurally-test-coverage-gated promotion** — c032 D4/D5 examples: `matrix-weighted-norm` rough-in→firm promotion is gated per the c021 `rough-in (test-coverage-bounded)` invariant; the gate has not changed since the priorities line was authored, so the dispatch would land another rough-in.

The c032 stale-recruitment incident (4 of 6 picks stale) is the strong evidence — the file-existence check alone is structurally insufficient. The c033 working precedent demonstrates the deeper check works: when the planner runs it inline per-dispatch, 3/3 dispatched targets are genuinely open and the cycle runs cleanly.

## Procedure (cycle-planner-facing; pre-emission per-dispatch)

For every dispatch whose `scope` resolves to a named file path under `book/src/` (an L_n operator, an L_{n+1}>L_n theme, a `concepts/<slug>` page, a Phase-1 slice-reduction audit, a `verified_against:` audit), run the **four-step deliverable-presence sequence** BEFORE finalizing the dispatch in the plan:

### 1. File existence

```bash
ls book/src/<layer>/<slug>.md
```

- **NOT found:** if the dispatch is to *author* the file, the dispatch is genuinely-open by construction (proceed to record the check outcome).
- **Found:** continue to step 2.

### 2. Maturity / already-discharged check

If the file EXISTS, read its `## Status` line: `firm` / `partly-constructive` / `rough-in` / `obstruction` / `stub`. Cross-reference the dispatch's proposed deliverable:

- **Operator/theme-authoring dispatch (harvester / abstractor):** if the on-disk maturity is at-or-above the proposed deliverable (e.g. `firm` and the dispatch is "harvest L1 operator X"), the dispatch is a no-op — do NOT recruit.
- **Audit dispatch (lowering-verifier):** `grep -c '^verified_against:' book/src/<layer>/<slug>.md`. If ≥1 block already exists at the timestamp class the audit would emit (recent-enough that the audit's scope is already discharged — typically same-batch or immediately-prior-batch), the audit is a no-op. Exception: a per-row repair audit (e.g. F1 row-refresh) is its own scope; check the OQ ledger for the specific row scope before deciding.
- **Slice-reduction audit (same-layer-cross-cutter on `book/src/spec/slices/<slice>.md`):** check the slice's `## Status` for an `annotated-and-retained` / `reduced-to-stub` / `removed` marker; check the OQ ledger for a RESOLVED disposition in the last ~3 cycles.
- **Stub→firm refinement:** the on-disk file is a `stub`, the dispatch is to refine to `rough-in` or `firm` — this is genuinely-open (proceed).

### 3. OQ-ledger RESOLVED-grep

```bash
grep '<slug>.*RESOLVED\|<slug>.*CLOSED\|RESOLVED.*<slug>' scaffolding/open-questions.md | head -5
```

If the dispatch's primary OQ slug is already in the Closed-index / has a RESOLVED disposition AND the plan line is older than the closure, the line is stale. Closed-index entries are append-only between meta-phases (meta-phase compacts in unification passes); a recent (within ~3 cycles) RESOLVED disposition is a strong stale-line signal.

### 4. Structural-block check

Is the candidate dispatch's deliverable structurally blocked by a methodology gate that has not changed since the priorities line was authored? Common blocks:

- **`rough-in (test-coverage-bounded)` promotion** (CLAUDE.md §Methodology invariants "Two rough-in qualifiers are first-class"): the firm-promotion is gated on a dedicated test exercising the operator at the exact entry point, OR a literature-anchor pass raising law-confidence. If neither has happened since the priorities line, the gate is still blocking — a re-proposed promotion lands another rough-in (no-op).
- **`partly-constructive` promotion gate** (CLAUDE.md §Methodology invariants): the constructive sub-part's promotion condition (typically a positive Palace anchor) has not changed.
- **`partial-obstruction` loop-lift** (CLAUDE.md §Methodology invariants): the operator's loop structure does not lift; the obstruction is permanent for that operator-shape.
- **`obstruction (opaque-library-ownership)`** (CLAUDE.md §Methodology invariants): permanently library-owned, never re-promotable — do NOT re-propose a firm-promotion on such a theme.

### Recruit decision

Only recruit when ALL four checks pass: target file genuinely absent (or below proposed maturity) AND OQ not RESOLVED AND no structural block. Record the check outcome **inline per-dispatch in the plan** — emit a `## Deliverable-presence verification` section (the c033 cycle-planner CYCLE.md is the canonical working example), with a per-dispatch checklist:

```markdown
### D<N>: <slug> (<agent>, <deliverable>)
- **(1) File existence:** `ls book/src/<layer>/<slug>.md` → NOT found ✓
- **(2) Maturity / already-audited check:** N/A (new file) ✓
- **(3) Recent OQ resolution search:** `grep '<slug>.*RESOLVED' open-questions.md` → NOT found ✓. OQ `<slug>` filed cycle-<N> as <routing>.
- **(4) Structural block check:** L0 sources directly readable; no test-coverage or promotion gates. ✓
- **VERDICT: GENUINELY OPEN, READY TO DISPATCH** ✓
```

Cheap (one `ls`/`grep`/`grep`/structural-check per scope; <30 seconds total for a 6-dispatch plan).

## When to skip (open-by-construction)

The procedure may be skipped for dispatches that are **open by construction**:

- A fresh harvest of a new operator with no prior-cycle history (the slug has never been mentioned in cycle-record / OQ ledger).
- A meta-phase-routed follow-up explicitly justified in the immediately-prior cycle's integrator-signals dump (e.g. the c032 routed `jacobi-smoother-mutation-rotation-l1-l0` was the c033 D1).
- A `cycle-N+1-resume-notes.md` referenced dispatch directly carried forward from the prior cycle.

Skip should be **explicit** in the plan — a per-dispatch note "open by construction (no prior-cycle history)" or "routed by c<N> integrator-signals top-of-list."

## Failure modes

- **Skipping the check on a stale plan line.** This is the recurrence-3 failure (c031 / c032). The orchestrator catches it pre-dispatch as a safety net.
- **Running the check superficially (file-existence only) without steps 2-4.** This is the c027-bullet-only failure that c032 demonstrated; the deeper steps are load-bearing.
- **Over-triggering on a stub→firm refinement.** A `stub` file existing does NOT make a refinement dispatch stale; the dispatch is genuinely-open. Step 2's "below proposed maturity" carve-out handles this.

## Cross-references

- Friction-ledger `cycle-planner-stale-priorities-line-recruitment` — the friction this skill addresses.
- Friction-ledger `cycle-planner-reproposes-already-landed-work` — the c027 sibling (file-existence layer; cycle-record-trail check).
- `.claude/agents/cycle-planner.md` §Discipline "MANDATORY pre-dispatch deliverable-presence check for every named-artifact-slug scope" — the role-spec bullet that mandates running this skill.
- `reports/2026-05-30T150000Z-cycle-planner-cycle-033/CYCLE.md` §"Deliverable-presence verification" — the canonical working precedent.
- CLAUDE.md §Methodology invariants "Two rough-in qualifiers are first-class" + "Theme/operator status `partly-constructive` is first-class" + "Obstruction themes have two sub-kinds" — the maturity-state language step 2 and step 4 operate on.
