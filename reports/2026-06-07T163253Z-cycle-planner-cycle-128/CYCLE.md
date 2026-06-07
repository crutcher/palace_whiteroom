---
agent: cycle-planner
invoked_at: 2026-06-07T163253Z
scope: cycle-128 dispatch plan
status: pending
---

# Cycle 128 dispatch plan

## Goals selected this cycle

ASK-2 "B" — the **5-driver L4-completeness audit capstone** (active-head item-3), now that "A" (the
matrix-free / element-local constructive-kernel layer) landed FULLY FIRM in c127. The audit is the
FEATURE-SURFACE SPINE's reason for existing: does every sim driver (electrostatic / magnetostatic /
eigenmode / driven / transient) reach L4 by composing **firm L4 vocabulary BY NAME**, with no
forced/absorbed/obstruction gap at the composition level? It is a COVERAGE-AUDIT (records findings),
NOT new vocabulary — and it is sharper now because the matrix-free L4 surface
(`L4/mk_matrix_free_operator` firm + `feature/matrix-free-operator` column firm) is a constituent
several drivers' assemble stage composes. Bundled with two D-opportunistic hygiene picks that the audit
naturally touches: the c127-surfaced stale L2 placeholder (`matrix-free-operator-apply.md:209-222`,
now firm-superseded by the L4 cap) and an opportunistic P1 edge-typing / true-detritus sweep on the
driver-column edges the audit reads. Deliberately modest, sharply-scoped cycle — the heavy build was
c127; c128 is the validation capstone + cheap hygiene. RE set: RE11 libceed-substrate sub-cohort
GROUNDED at c127; RE4 + residual RE11 (combinator-primary leaves, AMR reference-verbs, the dissolution
theme by-design, `libceed-quadrature-kernel-impl` itself) stay live/consumer-gated — NO consumer fires
this cycle (the audit is read-only over firm vocabulary). DIRECTIVE-1 (MPI/sharding) untouched.
Kernel-API/impl integrity untouched (the audit is read-only; D2 is a placeholder de-stale, no edge change).

## Linter baseline (c127 finalize, live on disk == cycle-record c127 `graded_stack_totals`)

```
files=385, typed=324, untyped=61, roots=45, reachable=163, reference_reachable=247,
rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=10,
detritus=122, true_detritus=50, detritus_reference_reachable_re11_cohort=72,
stronger_signal_reference_reachable=12, stronger_signal_true_detritus=7,
expected_unreachable_outside_dag=48
```

## Deliverable-presence verification

> Per the c036-strengthened mandatory pre-dispatch check (paste-inline-evidence). One row per
> named-artifact-slug dispatch; audit-class dispatch D1 is "open by construction" (fresh coverage-audit,
> no prior-cycle landing) but I verify NO prior 5-driver L4-completeness audit chapter exists.

**D1 — 5-driver L4-completeness audit (audit-class; coverage findings, the 5 driver columns are read-only inputs).**
- *No prior audit chapter on disk:*
  ```
  $ ls book/src/feature/l4-completeness*.md  book/src/feature/*completeness*.md
  ls: cannot access 'book/src/feature/l4-completeness*.md': No such file or directory
  ls: cannot access 'book/src/feature/*completeness*.md': No such file or directory
  $ grep -rl "5-driver.*L4.*complet|L4-completeness audit|five-driver" book/src/feature/   →  (no matches)
  ```
- *The 5 driver L4 columns exist + are firm (the audit inputs, read-only):*
  ```
  $ ls book/src/feature/{electrostatic,magnetostatic,eigenmode,driven,transient}.L4.md   → all 5 present
  $ grep -n "feature_root|rank:" feature/electrostatic.L4.md → 5:feature_root: seed / 6:rank: firm
    (eigenmode.L4 6:rank: firm; driven.L4 6:rank: firm; magnetostatic/transient同 — all firm, typed depends-on(composes))
  $ grep lifecycle.L4.md → 5:feature_root: seed / 6:rank: firm   (the spine ROOT, also an audit input)
  ```
- *OQ-ledger RESOLVED-grep for this audit slug:* `grep -i "5-driver.*l4.*complet|l4-completeness" open-questions.md`
  → only an unrelated batch-32 meta note ("the in-scope stack is L4-complete for backend-lowering",
  a different/older scope claim) — NO RESOLVED disposition for a *5-driver per-column coverage audit*.
- *Structural-block check:* none — this is a read-only coverage audit recording FINDINGS, no promotion,
  no no-op risk. **OPEN. Recruit.**

**D2 — `matrix-free-operator-apply.md` L2 placeholder de-stale (hygiene, `book/` write).**
- *File exists + the stale section is present:*
  ```
  $ ls book/src/L2/matrix-free-operator-apply.md  → present (firm chapter, c125)
  $ sed -n '209p'  → "## Speculative higher (L4) placeholder (rough-in, for a later harvester)"
    (section :209-222 sketches mk_matrix_free_operator "NOT authored this cycle … c126/batch-41 candidate")
  ```
- *Maturity / already-discharged:* the section is STALE — `L4/mk_matrix_free_operator` firmed c127
  (roadmap_goal→firm) and `feature/matrix-free-operator.{L4,L1}` landed firm; the placeholder's premise
  ("Left as a §Open-questions placeholder, not a chapter, this cycle") is now false. Not yet fixed on disk.
- *OQ-ledger:* `matrix-free-operator-apply-l4-placeholder-now-stale` — c127 integrator-signals flagged it
  `needs-more (low-priority prose-drift)`, NOT closed. Open.
- *Structural-block check:* none — a prose de-stale (replace the placeholder with a §-pointer to the now-firm
  `L4/mk_matrix_free_operator.md` + `feature/matrix-free-operator.L4.md`). No edge/rank/status change.
  **OPEN. Recruit.**

**D3 — P1 edge-typing / true-detritus opportunistic sweep (hygiene, item-5).**
- *Open by construction* — a lazy-tail edge-typing touch on untyped driver-column / L4-vocabulary nodes
  the audit reads this cycle (the active-head item-5 "fold into cycles that touch the relevant nodes",
  NOT a dedicated cycle). The `true_detritus=50` tier is mostly pre-P1 edge-untyped nodes; D3 types the
  `edges:` blocks on nodes D1 touches. No specific slug pre-committed (the sweep's targets are whatever
  untyped nodes the audit surfaces) → no per-slug presence check applies. **OPEN by construction. Recruit (opportunistic).**

## Dispatches

- **D1 [LEAD] (`cross-layer-cross-cutter`, HIGH, WAVE-1) — `5-driver-l4-completeness-audit` (active-head item-3, ASK-2 "B" capstone).**
  - **scope:** Audit whether each of the 5 sim-driver feature columns reaches L4 by composing FIRM L4
    vocabulary BY NAME, recording a per-driver coverage FINDING (NOT a promotion — read-only over firm
    vocabulary, no no-op risk). For each driver column `book/src/feature/{electrostatic,magnetostatic,eigenmode,driven,transient}.L4.md`
    (all firm, typed `depends-on (composes)`), verify its stage decomposition composes firm L4 vocabulary
    from the L4 chapter set (`fe_assemble`, `eigsolve`, `ksp_solve`, `solve_family`, `fold_solve`,
    `frequency_sweep`, `gram_reduce`, `eigenfreq_qfactor_reduce`, `sparameter_reduce`,
    `domain_energy_reduce`, `mk_matrix_free_operator`, the iteration/data-algebra combinators) and flag
    where a stage is: (a) cleanly composed of firm L4 ops (PASS); (b) composed of a black-box/opaque-surface
    primitive at L4 (eigsolve, libceed-quadrature kernel-api — note as an EXPECTED opaque boundary, not a gap);
    (c) ABSORBED below the column (a derived view with no separable L4 op — e.g. the RE4 incremental-LS view
    in a GMRES-variant driven path; note as the absorbed-below-column disposition); (d) a genuine
    L4-completeness GAP (a driver stage with no firm L4 home). **The matrix-free L4 surface is a sharper
    input now**: assemble stages that lower to matrix-free operator application can now name
    `L4/mk_matrix_free_operator` (firm c127) — check whether any driver's assemble stage should compose it
    BY NAME (a candidate edge finding, recorded NOT forced). Also read the spine-ROOT `lifecycle.L4.md`
    (the meta-feature column) to confirm the 5 drivers hang off it cleanly. Where the audit finds an
    absorbed-below-column or opaque-boundary disposition, cite the relevant RE-tracking entry
    (`scaffolding/graded-stack-baseline-exceptions.md` RE4 / RE11) — these are TRACKED dispositions, not new gaps.
    Output: a coverage-finding section (per-driver PASS / opaque-boundary / absorbed / GAP) + any candidate
    edge findings, in the report's proposed-changes (the integrator decides whether a finding warrants an
    L4-surface chapter or an OQ). **Do NOT author new vocabulary; do NOT force a driver to compose the
    matrix-free cap if the source does not.** Single-machine-valid (read `Par*` single-rank).
  - **deps:** none.
  - **rationale:** active-head item-3 / ASK-2 "B" capstone; validates the whole FEATURE-SURFACE SPINE's L4
    reachability now that "A" is firm. fan-out HIGH. Plan-tag `feature-surface-spine`.

- **D2 (`lifter`, LOW, WAVE-1, D-opportunistic hygiene) — `matrix-free-l2-placeholder-de-stale` (c127 OQ `matrix-free-operator-apply-l4-placeholder-now-stale`).**
  - **scope:** De-stale `book/src/L2/matrix-free-operator-apply.md:209-222` "## Speculative higher (L4)
    placeholder (rough-in, for a later harvester)". The placeholder's premise is now false:
    `L4/mk_matrix_free_operator` firmed c127 (roadmap_goal→firm) and `feature/matrix-free-operator.L4.md`
    landed firm. Replace the speculative-sketch prose with a short §"Speculative higher (L4)" → now a
    §"Higher (L4)" pointer: a 2-3 line note that the L4 backend-lowering surface IS the now-firm
    `[L4/mk_matrix_free_operator](../L4/mk_matrix_free_operator.md)` (the constructor) + the firm
    `[feature/matrix-free-operator.L4](../feature/matrix-free-operator.L4.md)` column, with the apply
    lowering captured in `[L4-L3/mk-matrix-free-operator-dissolution](../L4-L3/mk-matrix-free-operator-dissolution.md)`.
    Keep the `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` contraction-form line (it is accurate). **No status/rank/edge
    change** — `L2/matrix-free-operator-apply` is already firm with its typed `depends-on`/`reference` edges;
    this is prose-only. Verify the three link targets resolve on disk before authoring (all present:
    `L4/mk_matrix_free_operator.md`, `feature/matrix-free-operator.L4.md`, `L4-L3/mk-matrix-free-operator-dissolution.md`).
  - **deps:** none.
  - **rationale:** c127 integrator-signals OQ `matrix-free-operator-apply-l4-placeholder-now-stale`
    (`needs-more, low-priority prose-drift`). Couples to D1 (the audit reads the matrix-free L4 surface; a
    stale "not authored this cycle / later capstone" placeholder is exactly the drift the capstone retires).
    fan-out LOW (honesty/liveness hygiene). Plan-tag `index-count-hygiene`/`constructive-spine-kernels`.

- **D3 (`lifter`, LOW, WAVE-1, D-opportunistic hygiene) — `p1-edge-typing-true-detritus-sweep` (active-head item-5, lazy-tail touch).**
  - **scope:** A lazy-tail P1 edge-typing pass on UNTYPED nodes the c128 audit touches: as D1 reads the 5
    driver L4 columns + the L4 vocabulary chapters they compose, type any node whose `edges:` block is
    missing (the `true_detritus=50` tier is mostly pre-P1 edge-untyped nodes the GC marks because their
    `depends-on` edges were never typed). Add the typed `edges: depends-on:` block (with `kind:`) to any
    untyped L4-vocabulary / driver-column node in D1's read-set, reading the maturity off the node's own
    `## Status` (do NOT change maturity — pure edge-typing, the same lazy-tail discipline as the O1 c096
    precedent). **Bounded** — only nodes the audit naturally surfaces; do NOT open a dedicated whole-tree
    sweep. If a node's edges are already typed, no-op it (skip, do not re-type). Records which nodes typed +
    the resulting `untyped`/`true_detritus` delta for the finalize linter run.
  - **deps:** none (reads the same audit-target nodes as D1 but TYPES frontmatter `edges:` blocks; D1 is
    read-only over those files for its FINDINGS — see overlap analysis; mark PARALLEL, the integrator merges
    if a contended file surfaces).
  - **rationale:** active-head item-5 (`p1-edge-typing-true-detritus-sweep`, "fold into cycles that touch
    the relevant nodes — NOT a dedicated cycle"). fan-out LOW/hygiene (cleaner health signal). Plan-tag
    `graded-stack-hygiene`.

## Overlap analysis

- **D1 ↔ D2:** DISJOINT files. D1 reads/writes a coverage-finding in its OWN report (proposed-changes;
  the integrator decides the landing home); it reads the 5 `feature/*.L4.md` columns + L4 vocabulary
  read-only. D2 edits ONLY `book/src/L2/matrix-free-operator-apply.md:209-222` (an L2 chapter D1 does not
  touch). **PARALLEL.**
- **D1 ↔ D3:** POTENTIAL light overlap — both range over the same node set (the 5 driver L4 columns + the
  L4 vocabulary chapters). But D1 is **read-only over those files** (it produces FINDINGS in its own report,
  it does not edit the driver columns) while D3 edits FRONTMATTER `edges:` blocks (a disjoint region from any
  prose D1 might propose). They do not modify the same operator-entry body or rewrite the same theme. Per the
  conflict-tolerance philosophy (when in doubt, PARALLEL; false-sequentialization is the worse error), mark
  **PARALLEL** — if D3 happens to type a node whose prose D1 also proposes a finding-edit on, that is a cheap
  merge the integrator handles (and surfaces as an integrator-signals data point). The likeliest contended
  file is a driver L4 column if D3 types its `edges:` while D1 proposes a candidate-edge finding on it — but
  D1's finding lands in D1's report, not the column file, so even that is disjoint at the byte level.
- **D2 ↔ D3:** DISJOINT. D2 = L2 prose (`matrix-free-operator-apply.md`); D3 = frontmatter `edges:` blocks
  on L4-vocabulary / driver-column nodes. No shared file. **PARALLEL.**
- **No consolidated-tally / shared-index collision** — no dispatch lands a chapter into a layer index with a
  consolidated running count this cycle (D1 = report findings; D2 = L2 prose de-stale; D3 = frontmatter edges).
  The parallel-blind-shared-index guard does not apply. No floor-landing → no adjacent-entry re-anchor coupling.
  No cross-report forward-reference to a not-yet-existing slug (no new chapters authored).

## Sequencing schedule

- **Wave 1 (all parallel):** D1, D2, D3.
- ONE `integrator-finalize` at cycle end (rebuild book + commit + push + housekeeping; re-run both linters
  step-5b; re-check the RE set on the landed tree). Waves order dispatches by forward-reference dependency
  only — there is no forward-reference this cycle, so a single wave.

## RE-discharge tracking (batch-41, c128)

- **NO RE fires this cycle.** D1 is a read-only coverage audit over FIRM vocabulary (no new faithful
  `depends-on` consumer authored); D2/D3 are prose/frontmatter hygiene (no new edges to a baseline-excepted
  node). The RE11 libceed-substrate sub-cohort GROUNDED at c127 (the predicted `fe_assemble`-body-class
  consumer — the matrix-free column + dissolution theme — landed). Residual after c127: **RE4** (consumer-gated,
  awaiting a GMRES-variant column composing the running-QR stream) + **RE11** (combinator-primary `correction_step`
  leaves, AMR reference-reachable verbs, the `mk-matrix-free-operator-dissolution` theme reference-reachable
  BY DESIGN, and `libceed-quadrature-kernel-impl` itself awaiting a firm `fe_assemble` body that composes the
  IMPL by name). **If D1's audit surfaces a candidate `driver-assemble-stage → mk_matrix_free_operator` edge
  finding, that is a FINDING for a FUTURE cycle's faithful-edge dispatch — NOT authored this cycle** (the audit
  records, it does not force). Re-check RE4 + residual RE11 premises HOLD on the landed tree at finalize (the
  §2g escalate-guard: no `detritus`/STRONGER climb unaccounted by deliberate-reference-only-reachable nodes —
  this cycle should produce NO new such nodes, so any climb would be a flag).
- **DIRECTIVE-1 boundary:** no dispatch touches the MPI-associated version. Clean.
- **Kernel-API/impl integrity:** no dispatch changes a `realizes-kernel-api` edge or a kernel-impl/kernel-api
  status. D2's L2 prose de-stale is read-only on the kernel surfaces. Clean.

## Open questions / caveats

- **The c128 slate is deliberately light (1 capstone audit + 2 cheap hygiene).** This is correct for the
  "A then B" sequencing — the heavy "A" build landed c127; "B" is a validation capstone, not a build. If
  D1's audit comes back ALL-PASS (every driver reaches L4 cleanly, all gaps are TRACKED RE4/RE11/opaque
  dispositions), that is the **strong signal the in-scope FEATURE-SURFACE SPINE is L4-complete** — which
  feeds directly into the batch-41 meta's ASK-2 capstone judgment (and the "E — wind to maintenance"
  fallback if the artifact is complete for its in-scope purpose). I flag this for the batch-41 meta-phase
  (post-c129): the c128 audit findings are the primary evidence for the L4-completeness capstone verdict.
- **If D1 surfaces a GENUINE L4-completeness gap (disposition (d))** — a driver stage with no firm L4 home
  and no tracked RE/opaque disposition — that becomes a fresh high-fan-out plan candidate for c129 (a new
  L4-surface chapter). I did not pre-recruit it (the gap is hypothetical until the audit runs); the integrator
  / c129 planner picks it up from D1's findings. This is the audit-first framing working as intended.
- **The `inner-product-combinator-section-anchor-stability` OQ (c127 D4)** — ~30+ inbound links now depend
  on two long `inner_product` §-heading anchors staying verbatim — is NOT scheduled this cycle (latent
  build-fragility, not yet biting; the c127 D4 landing already re-pointed the inbound links successfully).
  Left as a candidate count-owner sweep for a future cycle with spare budget; flagged for the batch-41 meta
  to decide whether the anchor-shortening sweep is worth a dedicated dispatch or stays a watch item.
- **`true_detritus=50` is mostly the pre-P1 edge-untyped tail** (the `detritus_no_typed_edges_pre_p1_artifact`
  bucket), not garbage — D3's bounded lazy-tail touch nibbles at it but will NOT clear it materially in one
  cycle. The full P1 edge-typing campaign remains a meta-owned hygiene track (active-head item-5 is explicitly
  "NOT a dedicated cycle"). No escalation; recorded so the c129 planner / batch-41 meta know D3 is a nibble,
  not the campaign.
