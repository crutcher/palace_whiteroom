---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T08:40:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: warning
  rotation-quality: pass
  variant-axis-coverage: warning
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-05T09:30:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of feature-column → record `uses-record` reachability edges (cycle-104 D2)

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck --scan` on the report: 26 of 27 citations OK, all Palace
source ranges in-bounds (spot-confirmed `electrostaticsolver.cpp:21-98`, `main.cpp:276-278`,
`timeoperator.cpp:407-413`). The single MISS is `transient.L4:38` (CYCLE.md:226, also :37/:53), an
artifact reference written in the bare shorthand form `transient.L4` (no `feature/` prefix, no `.md`),
which the citecheck line-map cannot resolve. This is **path-hygiene noise, not a wrong claim**: I
opened `book/src/feature/transient.L4.md` and line 38 is exactly `op = time_operator (k,c,m) (dJdt
cfg)  -- the captured ODE operator (readonly; op : OpParams)`, the cited basis for the `op-params`
edge. Every other cited column signature line was confirmed verbatim on-disk (lifecycle :35/:52,
electrostatic :34/:53, magnetostatic :34/:53, driven :55, transient :32/:53, eigenmode :30/:50,
boundary-mode :32). Warning is for the unresolvable book-shorthand citation form, which recurs ~7×
in the prose; the underlying anchors are real.

**surface-or-evidence — warning.** This is a typed-edge wiring dispatch (frontmatter `depends-on
(kind: uses-record)` inserts), not a surface/algebra refinement, so the rotation_claim machinery
no-ops. The load-bearing evidential claim here is the **record→column reachability map** ("only 2 of
8 records become root-reachable; the other 6 are internal op-record shapes named in no column
signature"). I verified this directly: `grep -niE 'SimState|StepOutputs|PrevCarry|SolveResult|DofSet'`
over all `feature/*.L4.md` returns ZERO hits, and the only `Krylov` hits are in three L0 columns'
PROSE (driven/magnetostatic/electrostatic L0), exactly matching the `feature-record-mention-via-l0-
not-signature` caveat. `op-params` is surfaced only at `transient.L4:38`. So the "6 records need
op-chapter edges, not column edges" finding is **correct on the merits**. The warning is for an
under-scoped column-set claim (see variant-axis-coverage below): the report repeatedly asserts the
root set is "all 7 columns," but the on-disk feature-column root set is **12** L4 columns — the 5
output-product columns (capacitance/inductance/sparameters/eigenfrequency-qfactor/energy-fields) are
also `feature_root: seed rank: firm` and are silently outside the report's enumeration.

**rotation-quality — pass.** Not applicable: no algebraic/structural rotation is asserted — this is
pure graded-stack edge wiring (DAG-liveness plumbing), analogous to the stub/feature-surface no-op.

**variant-axis-coverage — warning.** The orthogonal axis the report under-covers is the
**feature-column root set itself**. The report frames "7 columns" (lifecycle + 5 drivers +
boundary-mode) as the complete set of config-record consumers, but 5 additional output-product
columns are equally `feature_root: seed` GC-roots, and 4 of them NAME a `*Config` record in their
input signature by the report's OWN precision rule: `capacitance :: ElectrostaticConfig -> …`
(:28), `inductance :: MagnetostaticConfig -> …` (:28), `sparameters :: DrivenConfig -> …` (:32),
`eigenfrequency_qfactor :: EigenmodeConfig -> …` (:30); `energy_fields :: PostprocessConfig ->
Field -> [DomainData]` (:51) names BOTH a `PostprocessConfig` config record AND a `DomainData`
result record. These columns get no `uses-record` edge from this dispatch and are not mentioned as
scoped-out. This is not a *reachability* hole for `config-record` (it is reached via the 7), but it
IS a hidden branch of the same precision rule applied unevenly — the same `*Config`-in-signature
basis that justified the 7 edges applies to ≥4 of the omitted columns. The report should either
extend the edge set or explicitly scope the output-product columns out (e.g. "config reaches via
the driver columns; output-product columns are deferred / route to the same OQ"). Flagged as a
candidate, not adjudicated for repairability.

**cross-reference-integrity — load-bearing for this kind; pass.** Verified all 8 edge targets exist
on-disk: `concepts/config-record.md` ✓ and `concepts/op-params.md` ✓ (the full 8-record set
present: config-record/dofset/krylov/op-params/prev-carry/sim-state/solve-result/step-outputs). All
7 `[old]` anchor blocks match the on-disk frontmatter exactly — each column's LAST `cites-evidence`
entry immediately precedes `reference:`, so the insertions are well-targeted (lifecycle
basesolver.cpp:153-276; electrostatic electrostaticsolver.cpp:21-98; magnetostatic
magnetostaticsolver.cpp:22-108; driven drivensolver.cpp:77-229; transient timeoperator.cpp:407-413;
eigenmode eigensolver.cpp:32-477; boundary-mode main.cpp:276-278). The reciprocal half is real:
`config-record.md`'s `reference:` already back-lists all 7 columns. Edges live in YAML frontmatter,
not mdBook link syntax, so `linkcheck2` is uninvolved — build-safe, as the report states.

**edge-label-fidelity (LOAD-BEARING) — pass.** Each `uses-record` edge's named basis was checked
against the column file. config-record: every one of the 7 columns names a config record in its
INPUT signature at the cited line (lifecycle `Config` :35/:52; the 6 drivers each name their
`*Config` specialization at the cited :34/:55/:32/:30 etc., each narrated "the IoData / config
surface"). op-params: `transient.L4:38` genuinely surfaces `op : OpParams` in the composition body,
and ONLY transient does (the others capture the operator stratum inside composed
ksp_solve/solve_family/fold_solve ops, confirmed by the absence of `OpParams` in their bodies). The
**"don't over-link" discipline is correct**: the 6 internal records (sim-state/krylov/step-outputs/
prev-carry/solve-result/dofset) are named in ZERO column signatures (verified by grep) — they are
the record shapes of the L4 solve/BC operators, reachable only via `column →(composes) op
→(uses-record) record`, so the `uses-record` edge belongs on the OP chapter. Adding column→internal-
record edges would indeed be the forbidden over-linking. The rank well-foundedness table is also
sound for the 7 config-record edges: boundary-mode is on-disk `rank: rough-in` (2) and config-record
is `rank: firm` (3), so `2 ≤ 3` holds; the other 6 columns are confirmed `rank: firm`.

**plan-kind-consistency — pass.** Declared kind is a graded-stack P1 typed-edge wiring dispatch
(layer-intro-author authority over frontmatter `edges:`); content matches — pure frontmatter
insertions, no body/SUMMARY change, no algebraic claim. The deferral of the op-chapter half to a
WAVE-3 dispatch via a HIGH OQ is the correct kind boundary (the op chapters carry pre-scheme
`consumes:`/`lowers_to:` frontmatter and `krylov-step` has no frontmatter at all — confirmed
on-disk — so typing them is a distinct migration, out of this feature-column scope). Routing the
6-record gap to WAVE-3 rather than fixing it here is the principled choice: doing it here would
require either over-linking the columns or editing out-of-scope op chapters.

**skill-uptake-survey — pass.** The report references the graded-stack linter
(`tools/graded-stack-lint/graded_stack_lint.py`) semantics (reachability GC marks from
`feature_root: seed` over `depends-on`, ignores `kind:`) and the scheme §2/§3 conventions — the
relevant procedural surface for this edge-wiring shape is invoked. No dedicated skill is implied
beyond the linter that is already cited.

### Issues found

1. **(citation-validity, warning) Unresolvable book-shorthand citations.** CYCLE.md:226 (and the
   prose at :37, :53, the proposed-change comments at :188) cite `transient.L4:38` in bare form
   without the `feature/` prefix or `.md` extension; citecheck cannot resolve it. The anchor is
   real (`book/src/feature/transient.L4.md:38` = `op : OpParams`), but the citation form should be
   the resolvable `feature/transient.L4.md:38` (or `book/src/feature/...`). Recurs for several
   column references throughout the prose.

2. **(variant-axis-coverage + surface-or-evidence, warning) Under-scoped "7 columns" root set —
   5 output-product GC-root columns omitted without scope-out.** The on-disk feature-column root
   set is 12 L4 columns; the report enumerates 7 and treats them as complete. The 5 output-product
   columns (`capacitance.L4`, `inductance.L4`, `sparameters.L4`, `eigenfrequency-qfactor.L4`,
   `energy-fields.L4`) are all `feature_root: seed rank: firm` and 4 of them name a `*Config`
   record in their input signature (capacitance:28 `ElectrostaticConfig`, inductance:28
   `MagnetostaticConfig`, sparameters:32 `DrivenConfig`, eigenfrequency-qfactor:30
   `EigenmodeConfig`); `energy-fields.L4:51` names `PostprocessConfig` AND a `DomainData` result
   record. By the report's OWN precision rule these are candidate `uses-record` edge sources. The
   report neither adds them nor explicitly scopes them out. (Not a reachability hole for
   config-record — it is reached via the 7 — but an unevenly-applied precision rule and an
   inaccurate "all 7 columns" framing. `config-record.md`'s own `reference:` list likewise omits
   these 5 columns.) Candidate for repair (extend the edge set to the output-product columns
   naming `*Config`, OR add an explicit scope-out note + route to the same OQ).

3. **(cross-report sequencing caveat, informational — not a fail) `op-params` rank rests on
   un-applied D1.** The rank well-foundedness table (CYCLE.md:66) asserts `transient.L4 → op-params`
   is `firm (3) → firm (3)`, justified by "op-params is D1-typed `rank: firm`, applied serially
   before this dispatch" (:74-75). On-disk RIGHT NOW `concepts/op-params.md` has **no YAML
   frontmatter and no `rank:` field** (it opens with `# OpParams`), so its firm rank is contingent
   on D1's report being integrated first. The report is transparent about this dependency, and
   per-report integration is serial, so this is a sequencing note for the integrator (apply D1
   before this report), not a defect in this report. `config-record` IS already `rank: firm`
   on-disk. Surfacing it so the integrator orders correctly.

## Repair

### Fixes attempted

- **Finding 1 (citation-validity, warning): unresolvable book-shorthand citations.** The report cited
  feature columns in bare `transient.L4:38` form (no `feature/` prefix, no `.md`) which citecheck flags
  MISS. **Decision: repaired.** **Action:** normalized the two MISS-producing `path:line` forms to the
  resolvable convention — CYCLE.md:188 (the `op-params` edge comment) and CYCLE.md:235 (Supporting-
  evidence "only … surfaces OpParams") both rewritten `transient.L4:38` / `transient.L4 :38` →
  `feature/transient.L4.md:38`. The remaining `transient.L4` / `lifecycle.L4` etc. occurrences carry no
  `:line` — they are dep-map NODE slugs (the `feature/<name>.L4` node identifier), not file:line
  citations, and citecheck does not flag them. Confirmed: `citecheck --scan` on the repaired CYCLE.md
  now reports ZERO MISS/OOB/AMBIG/DRIFT (including the newly-cited `feature/energy-fields.L4.md:51`).

- **Finding 2 (variant-axis-coverage + surface-or-evidence, warning): under-scoped 7-column root set;
  5 output-product GC-root columns omitted.** The 12-column root set includes 5 output-product columns;
  4 name a `*Config` record in their input signature (verified on-disk: `capacitance.L4` `ElectrostaticConfig`,
  `inductance.L4` `MagnetostaticConfig`, `sparameters.L4` `DrivenConfig`, `eigenfrequency-qfactor.L4`
  `EigenmodeConfig`), and `energy-fields.L4` names `PostprocessConfig` + `DomainData`. **Decision: repaired
  (4 of 5 linked; 1 flagged-not-linked).** **Action:** added a "Repairer addendum" to CYCLE.md §Proposed-
  changes inserting the analogous `depends-on (kind: uses-record) → concepts/config-record` edge into the
  4 columns that genuinely name a config-record specialization (`book/src/feature/{capacitance,inductance,
  sparameters,eigenfrequency-qfactor}.L4.md`), each anchored on its last `cites-evidence` entry immediately
  before `reference:` — the identical surgical pattern the dispatch established, applied evenly. Each edge is
  rank-well-founded: all 4 columns are `rank: firm` (verified on-disk) and `config-record` is `rank: firm`
  → `3 ≤ 3`. Also added the reciprocal back-references (the 4 columns) to `concepts/config-record.md`'s
  `reference:` list, completing the navigational pairing. Updated the §Reachability-outcome text (config-
  record now reachable from 11 columns, not "all 7"). **Flagged-not-linked:** `energy-fields.L4` was NOT
  linked — `PostprocessConfig` and `DomainData` have no `concepts/` record page on-disk, so a `uses-record`
  edge would be a dangler; routed to a new OQ (see below).

- **Finding 3 (cross-report sequencing, informational):** `op-params` rank rests on un-applied D1.
  **Decision: not-needed.** Per-report integration is serial and the report is transparent that D1 (which
  types `op-params` to `rank: firm`) applies before this report. No edit; surfaced for integrator ordering
  only. `config-record` is already `rank: firm` on-disk, so the 11 config-record edges are well-founded
  immediately regardless of D1 ordering; only the single `transient.L4 → op-params` edge depends on D1.

### Unrepairable findings

None blocking. One bounded follow-up was routed rather than authored (within the no-dangling-edge rule, not
an unrepairable defect): `energy-fields.L4`'s `PostprocessConfig`/`DomainData` records lack `concepts/`
definition pages, so the analogous `uses-record` edge could not be wired without a content judgment (does
`PostprocessConfig` fold into `config-record`, or get its own page?). Filed as OQ
`energy-fields-config-and-domaindata-records-need-concept-pages` (CYCLE.md §Open-questions), routed to a
future layer-intro-author pass. This does NOT gate `overall_status: ready` — the 4 linked edges discharge
the uneven-application finding for the columns that have a resolvable target, and the 5th is correctly
deferred under the directive's no-over-link / no-dangling-edge discipline.

## Suggested resolution

`overall_status: ready`. All three findings are resolved in-place (two repaired, one informational/not-
needed). Notes for the integrator:

1. **D1-before-this ordering** (Finding 3): apply the D1 report that types `op-params` to `rank: firm`
   before this report so the `transient.L4 → op-params` edge is rank-well-founded at apply time. The 11
   `config-record` edges are independent of D1 (`config-record` is already `rank: firm` on-disk).
2. The repair added **4 new edges** (output-product columns → config-record) + **4 back-references** in
   `config-record.md` beyond the dispatch's original 8 edges — all pure YAML-frontmatter insertions, no
   body or `SUMMARY.md` change, `linkcheck2`-uninvolved (frontmatter, not mdBook link syntax).
3. The deferred `energy-fields → PostprocessConfig` wiring is tracked as the new OQ; promote it through a
   layer-intro-author pass (decide config-record-fold vs own page) — not blocking this cycle.
