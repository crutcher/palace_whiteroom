---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T00:38:34Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-05T01:02:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "spec-slice reduction — orthog.md verified-absorb + delete"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing firm-home citation in §1 was re-read on disk and matches verbatim. `concepts/orthogonalization.md:42-58` carries the three collective shapes (MGS m×1 / CGS 1×m / CGS2 2×m), the runtime-enum / inspected-exactly-once binding (`OrthogonalizeIteration`, `iterative.cpp:308-325`), and the residual-axis disclosure — exactly as quoted. `L1/orthogonalize.md:100-104`, `L2/orthogonalize.md:19,150,347`, and `L3/orthogonalize.md:481` all match their pasted snippets. The L0 ground truth (`palace/linalg/orthog.hpp:18-90`, `iterative.cpp:308-325`) is cited directly by the firm homes. No drift, no off-by-one. Citation content is sound.

**surface-or-evidence — pass.** This is a deletion (no surface modification, no new per-op claim), so the relevant sub-check is the load-bearing one the task names: does the slice's unique content genuinely have a firm home before deletion? I verified a sample on disk (above) — the three MPI-collective shapes, the read-only-`V` / mutated-`w` / written-`H` L1 invariant, and the inspected-once variant binding are all present in firm chapters. The absorb-is-a-no-op claim holds. (Record-definition sub-check: N/A — no new record introduced by a deletion.)

**rotation-quality — pass.** Not applicable to a slice-deletion report (no algebraic/structural rotation asserted). Marked pass per the deletion-shape carve-out the task names.

**variant-axis-coverage — pass.** Not applicable to a deletion. The MGS/CGS/CGS2 variant axis is fully covered in the firm homes (verified under surface-or-evidence); nothing about the deletion re-opens it.

**cross-reference-integrity — FAIL (load-bearing for this report).** The report's claim (b) — "exactly 2 inbound cites" — is **incorrect**, and the deletion as proposed (PC-3) will produce **multiple `mdbook-linkcheck2` hard errors**. The report's §2 grep used `grep ... 'slices/orthog\|orthog\.md:' | grep -v 'spec/slices/orthog.md' | grep -v 'spec/index.md'`. The `grep -v 'spec/slices/orthog.md'` filter — intended to exclude the slice's own file — **also swallowed every inbound `[..](../spec/slices/orthog.md)` markdown link**, because the *link-target text* of those inbound links literally contains the string `spec/slices/orthog.md`. So the grep structurally hid exactly the links that linkcheck2 cares about. A broader scan (`grep -rnE '\]\([^)]*spec/slices/orthog\.md|\]\(\./orthog\.md'`) finds live `[..](..)` markdown links to the slice in **6 distinct external files**, none of which PC-1/PC-2 repoint. `mdbook-linkcheck2` (v0.12.0, `Makefile.toml:48-51`) is the active backstop; each unrepointed live link to a deleted file is a hard build error. This is a `fail`. Detail in Issues below.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried; the report is a same-layer corpus-reduction observation. N/A.

**plan-kind-consistency — pass.** Declared kind is a same-layer-cross-cutter Redundancy observation + corpus-reduction proposed-changes. The content shape matches: a redundancy finding (slice duplicates firm homes) with delete + repoint proposed-changes. The graded-stack rank/reachability framing (no `depends-on` edge targets the slice — independently confirmed: `grep depends-on ... | grep orthog` returns nothing) is consistent with the declared kind.

**skill-uptake-survey — warning.** A slice-deletion report directly implies the `phase-1-slice-reduction-audit` skill (concept-page-grep before recommending reduction). The report performs a manual analogue of that procedure but does not reference the skill's invocation. More importantly, had the skill's grep procedure been followed as specified (concept-page-grep for ALL inbound references, not a self-exclusion-filtered grep), the cross-reference-integrity defect would very likely have been caught. Pure telemetry surfacing, non-blocking — but it points at the same root cause as the fail.

### Issues found

**ISSUE 1 (cross-reference-integrity, severity: HIGH / build-breaking) — CYCLE.md §2 + PC-3.** The "exactly 2 inbound cites" count is wrong. There are at least **6 external files with live `[..](..)` markdown links to the slice** that PC-1/PC-2 do NOT repoint, each becoming a `linkcheck2` hard error when PC-3 deletes the file:
  - `book/src/SUMMARY.md:295` — `[Orthogonalisation (MGS / CGS / CGS2)](./spec/slices/orthog.md)` (the TOC entry; deleting the file without removing this row breaks the book outright). NOTE: the report scopes `SUMMARY.md`/`spec/index.md` row removal to **D2** — but PC-3 deletes the file in **D1**. If D1 and D2 are separate integrator-per-report applications, D1's deletion lands a dangling SUMMARY link before D2 runs. The deletion and its SUMMARY/index row-removal must be co-applied, or the build breaks between them.
  - `book/src/L0/mpi-globalsum-and-collectives.md:69` — `... see [\`spec/slices/orthog\`](../spec/slices/orthog.md)`.
  - `book/src/L0/mpi-globalsum-and-collectives.md:105` — `Recorded in [\`spec/slices/orthog\`](../spec/slices/orthog.md)`.
  - `book/src/concepts/orthogonalization.md:77` — `[\`spec/slices/orthog\`](../spec/slices/orthog.md) for the retained L2/L3/L4 unfolding`.
  - `book/src/concepts/gmres.md:23` — `... and the [orthog](../spec/slices/orthog.md) slice`.
  - `book/src/concepts/sequential-obstruction.md:48` — `See the [orthog slice](../spec/slices/orthog.md) L3 section ...`.
  All six are live prose markdown links (verified not inside code fences), not backtick inline-code. Each needs a repoint (to `concepts/orthogonalization.md` or the relevant firm `L*/orthogonalize.md`) before/with the delete. This is the exact "unrepointed inbound link → linkcheck2 hard error" failure mode the task flagged as load-bearing.

**ISSUE 2 (cross-reference-integrity, severity: MEDIUM) — `slices/arnoldi_step.md`.** Four relative `[orthog](./orthog.md)` links inside `book/src/spec/slices/arnoldi_step.md` (lines 67, 95, 115, 144) point at the slice. The report states `arnoldi_step` is the **c099 krylov-trio sub-campaign**, out of D1 scope — but that means after PC-3 deletes `orthog.md` in this cycle (c098), `arnoldi_step.md` carries 4 dangling `./orthog.md` links until c099. If `arnoldi_step.md` is still a live (non-deleted) book chapter at c098 build time, those are 4 more linkcheck2 errors. The report did not surface these (the §3 link inventory only inspected outbound links *from* orthog.md, not inbound links *to* it from sibling slices). Either arnoldi_step.md must also be deleted/stubbed this cycle, or these 4 links must be repointed, or the orthog deletion must be deferred to land atomically with the c099 trio.

**ISSUE 3 (count-claim accuracy, severity: MEDIUM) — CYCLE.md §2 + §3.** The two references PC-1/PC-2 *do* repoint (`concepts/gemv_basis.md:21` backtick `(\`slices/orthog.md\`)` and `L1/orthogonalize.md:302` backtick `\`orthog.md:18\``) are **backtick inline-code**, NOT `[..](..)` markdown links — so they are NOT linkcheck2 errors and would not break the build even if left as-is. The report repointed the two harmless references and missed all six (plus four sibling) genuine link-checked references. The §3 claim "all `](..)` targets resolve" was about *outbound* links from the slice; it does not address *inbound* links, and the §2 inbound count is the one that is wrong.

**ISSUE 4 (skill-uptake, severity: LOW) — root-cause note.** The defect traces to a grep whose `-v 'spec/slices/orthog.md'` self-exclusion filter also excluded inbound `[..](../spec/slices/orthog.md)` links. A correct inbound-link sweep for a to-be-deleted file `X` should match `\]\([^)]*X` and `\]\(\./<basename>` (relative sibling links) and exclude only lines *originating in* file `X` (by source-path prefix, e.g. `grep -v '^book/src/spec/slices/orthog.md:'`), never by link-target text. Worth crystallizing as an inbound-link-sweep procedure for slice deletions.

### Notes on what is sound (for the repairer)

- The firm-home absorb evidence (§1) is fully verified and correct — the slice genuinely carries no unique datum; the no-op-absorb conclusion stands. This part needs no repair.
- The PC-2 boundary caution is **correct and clean**: PC-2's diff targets only the `orthog.md`-referencing bullet at `L1/orthogonalize.md:299-304`; the adjacent arnoldi bullet at `:305-308` is a distinct bullet and is left untouched. No over-application risk. (Verified on disk.)
- PC-1 target (`concepts/gemv_basis.md:21`) and the PC-2 source range match the disk exactly.
- `depends-on` reachability is clean (independently confirmed: no blocking edge targets the slice). The reachability-GC argument is valid; the defect is purely navigational-link hygiene, not rank/reachability.
- The repair is well-scoped: add repoint proposed-changes for the 6 external links (Issue 1) + decide the arnoldi_step.md disposition (Issue 2) + ensure the SUMMARY/index row-removal co-applies with the file deletion. The content claims do not change.

## Repair

### Fixes attempted

- **Finding** (ISSUE 1, cross-reference-integrity FAIL, build-breaking): the §2 "exactly 2 inbound cites" count is wrong — the inbound grep's `grep -v 'spec/slices/orthog.md'` self-exclusion filter also swallowed every inbound `[..](../spec/slices/orthog.md)` markdown link (link-target text contains that string), so PC-1/PC-2 repointed 2 harmless backtick mentions and missed every load-bearing markdown link. PC-3's delete would fire multiple `mdbook-linkcheck2` hard errors.
  - **Decision**: repaired.
  - **Action**: Ran my own corrected inbound sweep (`grep -rnE '\]\([^)]*spec/slices/orthog\.md|\]\(\./orthog\.md'`, excluded by SOURCE-path prefix `^book/src/spec/slices/orthog.md:`, NEVER by link-target text). Confirmed the critic's set exactly; no additional misses. Added **PC-4** (a–f) to `CYCLE.md` §Proposed-changes — 8 surgical link repoints across 5 files + corrected the §2 inbound-cite block with a `CORRECTED` note. Each `[old]` anchor re-verified against current disk before writing:
    - `L0/mpi-globalsum-and-collectives.md:69` (PC-4a) and `:105` (PC-4b) → `concepts/orthogonalization.md` (general CGS-vs-MGS collective-shape references → firm collective-shape home).
    - `concepts/orthogonalization.md:77` (PC-4c, a self-page link to the slice) → `L2/orthogonalize.md` + `L3/orthogonalize.md` (the firm L2/L3 unfolding the link named).
    - `concepts/gmres.md:23` (PC-4d, bare provenance mention) → dropped the slice link, kept the firm `orthogonalization` concept link already present.
    - `concepts/sequential-obstruction.md:48` (PC-4e, "orthog slice L3 section") → `L3/orthogonalize.md` (firm L3 home carrying the MGS sequential-obstruction treatment, verified at L3:29-35).
    - `spec/slices/arnoldi_step.md:67,:95,:115,:144` (PC-4f) — 4 `./orthog.md` sibling links inside the SURVIVING arnoldi_step slice (c099 scope) that DANGLE at c098 build time once orthog.md is deleted → `concepts/orthogonalization.md`. Repointing a dangling link to a deleted file is a mechanical build-necessity, not krylov-trio content work — within repair authority.
  - **Note on D2/SUMMARY**: `SUMMARY.md:295` (R7 row removal) is deliberately NOT added to D1 — it is D2's single-owner scope, co-applied with the file deletion. The PC-3 out-of-scope note already records the SUMMARY/index row-removal as D2-owned; no change needed there.

- **Finding** (ISSUE 3, count-claim accuracy): §2 "exactly 2" framing + §3 "all `](..)` targets resolve" (outbound-only) understated the inbound set.
  - **Decision**: repaired (folded into the ISSUE 1 fix — the §2 `CORRECTED` note supersedes the count claim; §3 was an outbound inventory and remains accurate as scoped).

- **Finding** (ISSUE 4 / skill-uptake-survey warning): the defect traces to the self-exclusion-by-link-target-text grep antipattern; worth crystallizing an inbound-link-sweep procedure for slice deletions.
  - **Decision**: not-needed (acknowledge only). The critic already appended a `proposed` skill candidate `inbound-link-sweep-before-slice-delete` to `scaffolding/skill-candidates.md`. No repairer action — meta-phase promotes. The root-cause grep fix is embodied in this repair's corrected sweep (exclude by source-path prefix, never by link-target text), which is the procedure the candidate captures.

### Sound parts preserved (no change)

- §1 firm-home absorb-no-op verification — left intact (critic-confirmed sound; the slice carries no unique datum).
- PC-1 (`concepts/gemv_basis.md:21` backtick repoint) — left intact.
- PC-2 (`L1/orthogonalize.md:299-304` → claim-free Provenance prose) — left intact; boundary clean (the adjacent arnoldi bullet `:305-308` is NOT touched, per the report's own caution and the critic's verification).
- PC-3 (the deletion) — left intact; now `linkcheck2`-clean given PC-4 + D2's R7 SUMMARY/index row removal co-applied.

### Unrepairable findings

None. The cross-reference-integrity FAIL was entirely mechanical link-repoint hygiene (~8 swaps to known firm homes); no authoring judgment was required, so all of it was repaired in scope.

## Suggested resolution

`ready`. Integrator notes:

- **Co-application constraint (load-bearing).** PC-3 deletes `spec/slices/orthog.md` in D1, but the `SUMMARY.md:295` TOC row removal is **D2's R7**. D1's deletion lands a dangling SUMMARY link if applied before D2. The integrator must ensure the orthog deletion (D1 PC-3) and the orthog SUMMARY/`spec/index.md` row removals (D2/R7) **co-apply in the same finalize build** — i.e. do not run `cargo make book` / linkcheck2 between the D1 and D2 per-report applications, or sequence D2's R7 before/with D1's PC-3. The book build will only be link-clean once BOTH land. (This is the one inter-report ordering the integrator must respect; PC-4 handles all other inbound links.)
- All PC-4 repoint anchors were verified against current disk at repair time; if intervening cycles edit those lines, re-verify the `[old]` text before applying.
