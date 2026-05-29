---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T16:55:06Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T17:05:00Z
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

# META: verification of "Audit nleps-eigenvalue-correction-mutation-rotation"

## Critique

This is an AUDIT report (lowering-verifier, cycle-026 dispatch 6b) re-auditing the firm L1>L0 theme
`nleps-eigenvalue-correction-mutation-rotation` (authored firm cycle-025, first audit) with verdict
**fully-supported**. All checks are read in the audit-report frame: the report makes no surface
claims of its own — it confirms an existing firm theme and proposes one additive metadata block. I
independently re-ran the mechanical citecheck scans and the load-bearing `--anchor` spot-checks, and
read the cited source block, the theme, and the L1 operator entry. The audit holds; no defects found.

### Checks run

**citation-validity (LOAD-BEARING) — pass.** Re-ran both scans mechanically:
`citecheck.py --scan` over the audit CYCLE.md → **25 ok, 0 failing**; over the theme → **31 ok, 0
failing** — both exactly matching the report's claims (25 / 31). Independently re-ran `--anchor` on
all five primary lines: `:672` (`Undamped Newton step for the eigenvalue`), `:673`
(`w2.adjoint() * u2`), `:674` (`delta_eig`), `:675` (`linalg::Dot(GetComm(), w, w0)`), `:676`
(`z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)`), `:677` (`z2 = -u2`) — every one resolves on-disk at the
exact cited line, zero drift. Confirmed the load-bearing context anchors (`:540` projection-direction
comment, `:657` `opJ->Mult(v, w)`, `vector.hpp:246` inner-product convention) also land. The
`:672-677` primary block carries **no codemap +1 drift** — re-confirmed by reading `:655-680`: the
correction block is on-disk exactly as the theme transcribes, and the wave-1 codemap drift is indeed
confined to the earlier deflation block (`:658-669`), which precedes this site. Pass.

**surface-or-evidence — pass.** The report is an audit confirming an existing firm theme, not a
refinement of surface; its only proposed change is the additive `verified_against:` metadata block
(retroactive-evidence backfill — explicitly allowed). I spot-checked the three sub-patterns against
source `:672-677`: A (Newton ratio δλ=−num/den over `w2ᴴu2` at `:673` + `w0ᴴu`/`w0ᴴw` at `:674-675`),
B (`z=−δλ·w−u` via `AXPBYPCZ` γ=0 at `:676`), C (`z2=−u2` via `scal` α=−1 at `:677`) — all three read
straight off positive source. The load-bearing big/coordinate asymmetry is confirmed: the Jacobian
action at `:657`/`:668`/`:669` writes only into the big-space `w` (I read `:655-670` — no `w2` write
exists anywhere in the Jacobian-action block), so δλ genuinely couples into `z` only, never `z2`. The
asymmetry's load-bearing classification (per the CLAUDE.md trick taxonomy) is sound. Pass.

**rotation-quality — pass (not the primary axis for an audit, but holds).** The theme is a
mutation-rotation lowering an existing firm L1 form; the audit does not assert a new rotation, it
confirms the theme's existing one. The L1 form (state-hiding: pure value-return `{δλ, z, z2}` over the
L0 destination-buffer + consume-then-reuse aliasing) is strictly more abstract than the L0 block —
the rotation is genuine, not a 1:1 rename. The audit faithfully re-states this without inflating it.
Pass.

**variant-axis-coverage — pass.** The theme's variant axes (deflation-present `k=0` vs `k>0`;
committed-step purpose) are covered in §Applicability conditions, and the audit verifies condition 3
(variadic-in-`k`, `k=0` un-deflated degeneration where `w2.adjoint()*u2=0` runs uniformly and `z2=[]`)
against the deflation-growth site `:606-619` (`k++` at `:619`). No hidden branch. Pass.

**cross-reference-integrity — pass.** All cross-references resolve. The L1 operator-entry pinpoints
the audit relies on for the carried laws were independently confirmed by reading
`book/src/L1/nleps_eigenvalue_correction.md:60-118`: semantics point 4 (big-space-only) at `:68`,
law 3 (Newton-ratio) at `:80`, law 4 (coordinate-RHS independence) at `:82`, over-unification guard
at `:110`, Status `firm` at `:114` — every one lands and the audit carries them faithfully. The 19
sibling/leaf theme + operator files listed in §Supporting evidence are the real on-disk slugs.
**Build-readiness guard (additive-metadata variant):** the proposed change is NOT a firm-chapter-body
authored outside a fence (the cycle-019 defect does not apply — this is a metadata append to an
already-firm theme). I enumerated the proposed-changes fences (`grep -n '\`\`\`'`): `:154`
` ```edit:...`, `:156` ` ```yaml`, `:234` ` ``` `, `:235` ` ``` ` — 4 fences, even parity, balanced
nesting (yaml nested inside the edit block). The block is well-formed. See Issue 1 for the
nested-fence integration-safety note (a forward-flag for the repairer, not a content defect). Pass.

**edge-label-fidelity — pass.** The theme is L1>L0; the prose throughout discusses the L1→L0 lowering
(pure form → `:672-677` destination-buffer block), the direction is consistent, and the audit's prose
discusses exactly that edge. No edge-label/prose mismatch. Pass.

**plan-kind-consistency — pass.** Declared kind is an audit (lowering-verifier, verdict
fully-supported). Content shape matches: per-citation audit table, applicability-condition
re-verification, carried-law soundness review, additive `verified_against:` proposal, no theme-body
mutation. No firm/rough-in mis-classification — the theme stays `firm` and the audit neither promotes
nor demotes it. Pass.

**skill-uptake-survey — pass.** The audit invokes the mechanical citecheck realization of
`verify-citation-range` (`--anchor`/`--scan`) throughout — the expected skill for a citation-heavy
audit — and references the firm-on-positive-structure escape consistently. Skill uptake is present and
appropriate. Pass.

### Issues found

**No defects.** The audit verdict (fully-supported), the citecheck claims (25/31 ok), the five
zero-drift primary anchors, the three sub-patterns, the big/coordinate asymmetry, and both non-laws
all hold under independent re-verification. The two findings below are non-blocking observations.

1. **(Non-blocking, integration-safety forward-flag) Nested-fence shape in the proposed-changes
   block** — `reports/.../CYCLE.md` §Proposed changes (`:154-235`). The proposed change nests a
   ` ```yaml ... ``` ` fence inside the ` ```edit:... ``` ` block (fences at `:154`/`:156`/`:234`/`:235`).
   Parity is even and the nesting is balanced, and the report's `:237` parenthetical correctly
   identifies the inner yaml as the actual block to append — so this is well-formed and the *intent*
   is unambiguous. But this is the same nested-fence-inside-edit-block shape that the cycle-024
   `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill exists to harden: a naive
   first-` ``` `-wins integrator fence-parser could truncate at `:234` or mis-pair the closers. Flag
   for the repairer's awareness so the integrator applies the EOF-append of the 19-entry block
   cleanly (and so the additive YAML lands as a frontmatter-adjacent block, distinct from the theme's
   existing prose `## Verified-against` section at theme `:348` — the two are different surfaces and
   must not be conflated). Confirmed the theme has **no** existing frontmatter `verified_against:`
   key, so the append is purely additive and the theme stays `firm`.

2. **(Non-blocking, already self-flagged by the audit) Two carry-forward operator-entry drifts are
   correctly scoped** — verified independently: the L1 operator entry
   `book/src/L1/nleps_eigenvalue_correction.md` cites the `while (it < nleps_it)` loop at `:596`
   (on-disk **590** — I read `:588-598`, `:596` is the `restart, res` tail of the `Mpi::Print`), and
   references the Armijo `α` update at `:709` in semantics point 5 / collapsed-axes `:108` (on-disk
   **712** — I read `:706-714`: `:708` is `eig = eig_trial`, `:709` is `res = res_trial`, `:712` is
   `alpha *= backtrack_factor`). The theme uses the corrected on-disk numbers (`:590`/`:712`) and
   already flags both. The audit correctly routes these as **operator-entry** carry-forward defects
   (co-keyed with the pre-existing OQ `nleps-eigenvalue-correction-l1-entry-two-anchor-reanchor`,
   `open-questions.md:722`), NOT as defects of this theme. The theme's own anchors all land
   zero-drift. Correctly handled — no action required of this report. (Minor: the L1 entry's
   collapsed-axes line `:108` literally reads "`:691`, `:709`" — confirms the drifted `:709` is in the
   operator entry, the eventual re-anchor target.)

3. **(Informational, no action) OQ disposition discharged.** The followup OQ
   `nleps-eigenvalue-correction-mutation-rotation-lowering-verifier-audit-followup` is marked
   **RESOLVED** at `open-questions.md:871` with a clause-scoped disposition (fully-supported /
   stays-firm), the carry-forward correctly co-keyed to the `:722` OQ, no new tracking opened, and an
   explicit meta-phase "migrate to Closed index" action. The disposition matches the CYCLE.md exactly.
   Discharged cleanly.

### Verification footnote

Independent re-runs (not inherited from the report): `citecheck --scan` on both files (25/31 ok
reproduced); `citecheck --anchor` on `:672`–`:677` (all five + `:672` comment land zero-drift),
`vector.hpp:246`, `:540`, `:657`; `--show` reads of `:655-680` (correction block + Jacobian action),
`:588-598` (`:590` loop), `:706-714` (Armijo), `:683-687` (near-singular), `:699-701` (aliasing),
`:636-647` (divergence-restart), `:604-620` (deflation growth); and `book/src/L1/nleps_eigenvalue_correction.md:60-118`
(law 3/law 4/point 4/over-unification/Status pinpoints). All confirmed.

## Repair

### Fixes attempted

- **Finding** (critic Issue 1, non-blocking): Nested-fence shape in the proposed-changes block
  (CYCLE.md `:154-235`) — a ` ```yaml ` fence nested inside the ` ```edit: ` block (the cycle-024
  nested-fence shape). Well-formed and even-parity, but the inner backtick ` ```yaml ` / ` ``` `
  delimiters are counted as outer fence toggles under flat first-` ``` `-wins integrator parsing, so a
  naive parser could truncate the EOF-append at `:234` or mis-pair the doubled closers at
  `:234`/`:235`.
  - **Decision**: repaired.
  - **Action**: Applied `convert-nested-fences-to-indented-code-in-proposed-changes-block` (tilde-fence
    realization, matching the landed precedent
    `reports/2026-05-29T151441Z-lowering-verifier-apply-nonlinear-pencil-audit/CYCLE.md:156-239`).
    Swapped the inner backtick fences for tilde fences: `:156` ` ```yaml ` → `~~~yaml`, `:234` ` ``` `
    → `~~~`, and dropped the now-redundant doubled outer close (the single ` ```edit: ` open at `:154`
    is now closed by exactly one ` ``` ` at `:235`). The YAML content is preserved byte-for-byte; only
    the inner fence *mechanism* changed (backtick → tilde). Verified parity:
    `grep -c '```'` = **2** (one open + one close for the single proposed-changes block), and the
    inner tilde fences (`:156`/`:234`) no longer mis-toggle the outer block. The 19-entry
    `verified_against:` YAML now sits unambiguously inside the `edit:` block and lands as a proper
    `~~~yaml … ~~~` CommonMark code block at EOF of
    `book/src/L1-L0/nleps-eigenvalue-correction-mutation-rotation.md` (tilde fences render identically
    to backtick yaml fences in mdBook/pulldown-cmark, satisfying the
    `lowering-verifier-yaml-in-prose-channel-format` channel requirement; the downstream
    `cross-layer-cross-cutter` parser keys on the `verified_against:` leading text, which survives).
    Confirmed the append target is non-colliding: the theme has a prose `## Verified-against` *section*
    at `:348` but **no** frontmatter/YAML `verified_against:` key, so the EOF append is purely additive
    and the theme stays `firm`. Also updated the `:237` parenthetical to describe the tilde form.
    (cross-reference-integrity repair — build-readiness sub-check.)

- **Finding** (task-flagged housekeeping): stale `verifies: ../REPORT.md` frontmatter key in META.md
  (pre-rename `REPORT.md`→`CYCLE.md` artifact).
  - **Decision**: repaired.
  - **Action**: META.md frontmatter `:2` `verifies: ../REPORT.md` → `verifies: ../CYCLE.md`.

### Unrepairable findings

None. The critic graded all 8 checks `pass` (clean audit, verdict fully-supported: CYCLE.md 25 ok /
theme 31 ok, 0 failing; five primary anchors land zero-drift; carry-forward L1-operator-entry drifts
correctly scoped). Critic Issue 2 (two carry-forward operator-entry citation drifts `:596`→`:590`,
`:709`→`:712`) requires no action of this report — they are operator-entry defects on
`book/src/L1/nleps_eigenvalue_correction.md`, already correctly routed by the audit as carry-forward
co-keyed to OQ `nleps-eigenvalue-correction-l1-entry-two-anchor-reanchor`
(`open-questions.md:722`); this theme's own anchors all land zero-drift. Critic Issue 3 (followup OQ
disposition) is informational, no action.

## Suggested resolution

`ready`. The audit is clean and verdict-supported; the only mechanical items were the integration-safety
fence encoding (now matching the landed tilde-fence precedent) and a stale `verifies:` key (now
`../CYCLE.md`). Note for the integrator: the proposed change is an **additive EOF append** of a 19-entry
`verified_against:` YAML block to `book/src/L1-L0/nleps-eigenvalue-correction-mutation-rotation.md`; it
must NOT be conflated with the theme's existing prose `## Verified-against` section at theme `:348` (the
theme has no prior frontmatter `verified_against:` key — the append is non-colliding and the theme stays
`firm`). The carry-forward operator-entry drifts (`:596`→`:590`, `:712`) remain tracked under OQ
`nleps-eigenvalue-correction-l1-entry-two-anchor-reanchor` for a later `lifter`/harvester re-anchor pass
on `book/src/L1/nleps_eigenvalue_correction.md` — out of scope for this theme report.
