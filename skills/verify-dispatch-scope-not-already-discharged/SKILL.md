# verify-dispatch-scope-not-already-discharged

**Promoted:** cycle-033 meta-phase (batch-9). **Strengthened:** cycle-036 meta-phase (batch-10) — recurrence-3 within batch-10 (c034/c035/c036) post-codification proved the skill text alone is insufficient; the paste-inline-evidence requirement is now load-bearing. **Proposer:** abstractor (cycle-031 D6 no-op) + layer-intro-author (cycle-031 D6-reroute no-op); promoted on recurrence-3 across batch-9 (c031 file-existence-staleness, c032 broader 4-of-6 deliverable-presence-staleness, c033 working precedent). **Working precedents:** `reports/2026-05-30T150000Z-cycle-planner-cycle-033/CYCLE.md` §"Deliverable-presence verification (cycle-033 deeper-check enforcement per c032 orchestrator signal)" — the c033 cycle-planner ran the procedure inline per-dispatch and landed 3/3 genuinely-open dispatches; AND `reports/2026-05-31T200000Z-cycle-planner-cycle-036/CYCLE.md` — the c036 cycle-planner correctly REJECTED stale picks WITH pasted inline evidence (the canonical paste-evidence working precedent, post-batch-10 strengthening).

**Audience:** cycle-planner (the primary user; runs the procedure pre-dispatch). Also: orchestrator (the safety net — runs the same procedure when the planner skipped it OR when the planner's "compliance" was assertion-without-paste-evidence per the batch-10 strengthening).

## Batch-10 strengthening: paste evidence, do not merely claim compliance

The batch-9 codification (this skill + role-spec bullet) was demonstrably insufficient at the planner side: c034 D3 stale-dispatch (recurrence-1), c035 2-of-3-stale plan with planner *claiming* the check ran without verifying (recurrence-2), c036 with paste-evidence working (recurrence-3, but with successful inline-evidence pattern proving the demand works). The decisive observation: **when the cycle-planner is required to paste the literal `ls`/`grep`/`## Status`-line output inline per dispatch, the check actually runs; when only required to claim compliance, the claim is sometimes false.**

The procedure below now demands:
1. Per-dispatch `## Deliverable-presence verification` section in the plan.
2. Each check's actual command output pasted as a code-fenced line (not paraphrased).
3. The `VERDICT: GENUINELY OPEN` / `STALE / DROP` decision recorded explicitly with the citation that justifies it.

**Orchestrator-side enforcement:** any plan whose deliverable-presence section asserts compliance without pasted command output is a recurrence-class fault — the orchestrator may reject the plan and request re-emission with paste evidence, OR substitute verified-open dispatches (the c034/c035/c036 orchestrator-substitution pattern).

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
- **(RETIRED — slice-reduction audit):** the Phase-1 slice corpus (`book/src/spec/slices/`) was fully lifted and DELETED (9→0, cycles 097/098/099); there are no slices left to audit and the directory no longer exists. Do NOT recruit a slice-reduction-audit dispatch. (Historical: this step checked the slice `## Status` for `annotated-and-retained`/`reduced-to-stub`/`removed`. The general inbound-link-sweep-before-delete discipline lives in the active skill `deleted-slug-inbound-live-link-sweep`.)
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

### 5. STOP-PROPOSING NEGATIVE LIST consult (added cycle-036 meta-phase, batch-10)

The c036 D2 cross-layer-cross-cutter L3-cohort-growth audit produced a 7-operator (C) NEGATIVE LIST of L1 operators that should NOT receive L3 backfills (disqualified by the small-dense coordinate-space axis criterion at `book/src/L3/index.md:10-16` — deflation rank / ROM basis size / GMRES restart-cycle is NOT the field axis `N` that the L3 layer rotates). The negative list lives at `scaffolding/priorities.md` Backlog "STOP-PROPOSING marker" + at `book/src/L3/index.md:38`:

- `lu_solve`
- `back_solve`
- `ls-update-column`
- `nleps_deflated_residual`
- `nleps_deflated_solve`
- `nleps_jacobian_action`
- `nleps_eigenvalue_correction`

If a candidate dispatch's scope is `L3 <slug>` for any of these slugs, do NOT recruit. Record the disqualification inline: "STOP-PROPOSING list (c036 D2 audit; book/src/L3/index.md:38)." Extend the list when future audits produce additional permanent disqualifications.

### 6. Audit-first vs reflexive-harvest framing (added cycle-036 meta-phase, batch-10)

For an **operator-to-data primitive** (one that produces data rather than transforming fields — `assemble-diagonal`, `reciprocal-of-vector` etc.) or a **cross-cutting cohort question** (one that affects N siblings, not just one operator), prefer the **audit-first** framing over the **reflexive-harvest** framing:

- **Reflexive-harvest**: a `harvester` dispatch directly authors the L_n entry; appropriate when the scope is a single operator with a clear identity-in-form relationship verified by the planner.
- **Audit-first**: a `cross-layer-cross-cutter` (or `same-layer-cross-cutter`) dispatch first verifies the cohort question (which operators qualify? what's the systematic classification?), then a subsequent harvester pass lands the firm entries. Appropriate when the candidate sits at a cohort boundary or carries a representation-dependent caveat.

The c036 D2 was originally proposed by the planner as `harvester` on `assemble-diagonal` L3 (reflexive identity-in-form harvest); the orchestrator reframed to `cross-layer-cross-cutter` audit-first, which CONFIRMED the same identity-in-form verdict for `assemble-diagonal` AND produced the systematic (A)/(B)/(C) classification + the (C) STOP-PROPOSING NEGATIVE LIST for the whole L3 cohort. The reframe cost was zero (one dispatch instead of one); the value was the cohort-wide settlement. **When the candidate sits at a cohort boundary, prefer audit-first.**

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
