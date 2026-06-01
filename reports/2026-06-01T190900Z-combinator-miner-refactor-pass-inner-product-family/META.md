---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T193000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-06-01T192555Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of "Combinator refactor-pass — `inner_product` family (`dot`/`nrm2`)"

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` over the report's `reference/`-relative
Palace citations returns 28 ok / 0 failing. I hand-verified the load-bearing book-internal
anchors the report's verdicts rest on: the KEEP-verdict anchors in
`inner-product-fold-specialization.md` (three-key dispatch `:107-135`, the conjugate-pair
re-order `:158-220`, the lowering-verifier audit block — `coverage_verdict: fully-supported`,
`status_recommendation: keep firm`, the three Ax/SPD anchor drifts `:623→624`, `:632→634`,
`:615-616→616`) all match; the four "all-Identity rewrite table" claims (`dot-body-identity.md:77-84`
is verbatim all-"Identity." rows) match; `L2/nrm2.md:29-33` ("Merging `nrm2` into
`inner_product` would be a category error") and the `L2/index.md:28,48,111` "fork-invariant on
membership" / "Fold-cohort boundary" anchors match; `L3/index.md:27-28` are exactly the firm
`dot`/`nrm2` rows. One trivial paraphrase: report says `nrm2-leaf-identity.md:5` reads
"identity-in-form on the leaf" — the live line-5 text is "identity-in-form on the **primitive's
signature**" (substance identical; not a defect). No `verified_against:` block is proposed, so
that sub-check is N/A.

**surface-or-evidence — pass.** This is a refinement of an existing combinator entry that BOTH
modifies surface (the five-site lede/§Context/§Specializations/§Dependencies/§Status rewrite of
`inner_product.md`) AND is grounded in the prior rotation evidence (the cycle-019 fold
characterization + the `inner-product-fold-specialization` lowering). The (b) map and (c) re-audit
are evidence-and-disposition framing, not bare rotation_claims. Satisfies the check.

**rotation-quality — pass.** The combinator-as-entry inversion makes the L2 representation strictly
more abstract: the same-named `L2/dot` floor + the `dot`/`tdot`/`bilinear_form` members collapse
into one fold-entry with the members as fixed-axis specialization notes (state-hiding /
coarser-substitution compression, not a 1:1 rename). The (c) KEEP verdict correctly identifies
`inner-product-fold-specialization` as a genuine translation (conjugation/element-type/weight
re-fusion + the value-bearing `xᴴy`↔`yᴴx` re-order), not an identity-in-named-terms smell — the
distinction vs. the four demoted all-"Identity" themes is sound and well-anchored.

**variant-axis-coverage — pass.** The conjugation / element-type / weight axes are each covered
in the inverted §Specializations and the (c) dispatch-key audit; the diagonal `y=x` is explicitly
scoped OUT as a consumer entry point (not an axis), and the reduction-tree is scoped OUT as an L0
non-law. The `tdot` zero-call-site type-API-surface-only caveat is carried forward as a
member-level note. No hidden branch.

**cross-reference-integrity — FAIL.** Two findings, one of them load-bearing (see Issues). The
LINKS all resolve — I enumerated every relative link in the post-edit `inner_product.md`; all
targets exist on disk, and the L3/index.md proposed-changes row correctly leaves the
not-yet-existing `L3/inner_product.md` as plain text (`` `inner_product` *(rough-in; no anchor
yet)* ``) while live-linking only the existing `../L2/inner_product.md`. The FAIL is the
write-authority-partition violation: the inversion was written directly into the artifact during
the dispatch phase (see Issue 1), which is a cross-reference / process-integrity defect the
combinator-miner spec itself instructs the critic to flag.

**edge-label-fidelity — pass.** The four demotion-targeted themes carry their edge labels
correctly (`dot-body-identity` = L3>L2, `dot-leaf-identity` = L2>L1, etc.) and the report's prose
discusses the matching edge for each. The (b.5) propagation row is labeled L2→L3 upward and the
prose matches.

**plan-kind-consistency — warning.** The declared shape is "refactor-pass: (a) ENACTED inversion +
(b) map + (c) re-audit." The (b) map and (c) re-audit are correctly scoped as deferred-to-cycle-050
and KEEP, and the map/enactment boundary is respected for everything EXCEPT (a): the (a) "ENACTED"
content has no applicable proposed-changes representation — the `` ```edit:book/src/L2/inner_product.md ``
block is a comment-only placeholder (`# (a) ENACTED …`), not a literal diff, because the change was
applied directly to the file. A dispatch-phase report's "enacted" artifact change is a category the
flow does not have a slot for (only integrator-* write `book/`); the kind is mis-fit here. See
Issue 1 / Issue 2.

**skill-uptake-survey — warning.** The report's shape (a dispatch-phase book mutation now sitting in
the working tree) implies the repairer skill `revert-dispatch-phase-book-mutation` and the
proposed-changes-fence guard are relevant, but the report does not reference invoking any skill for
the enactment (and could not have — the enactment itself is the thing to be reverted). Surfacing
only; not blocking.

### Issues found

**Issue 1 (HIGH — dispatch-phase write-authority-partition violation; `cross-reference-integrity`).**
CYCLE.md §Deliverable (a) (`:70-112`) and §Status of `book/src/L2/inner_product.md` were applied
**directly to the artifact during the dispatch phase**. `git status` confirms
`M book/src/L2/inner_product.md` (82 insertions / 29 deletions) sitting uncommitted in the working
tree. Combinator-miner is a Phase-2 specialized agent whose write authority is
`reports/<id>/CYCLE.md` + same-dir supporting docs ONLY (CLAUDE.md §Write-authority partition;
Phase 2 "No artifact mutation in this phase"). The combinator-miner spec's FIRST Discipline bullet
(`.claude/agents/combinator-miner.md:106`) states verbatim: "Do NOT write to `book/` … Writing
directly to `book/` during dispatch violates the CLAUDE.md write-authority partition; **the critic
flags it HIGH and the repairer reverts your leak** (skill `revert-dispatch-phase-book-mutation`)."
This is a recurrence of friction-ledger `specialized-agent-direct-write-to-book-during-dispatch`
(recurrence-3 at cycle-017; guard enacted across all 8 specs cycle-018). The 2026-06-01 redirect's
"replace-and-propagate" / "ENACTED" re-mandate did NOT grant book-write authority — it re-mandates
the combinator-miner to PROPOSE the full inversion + upward propagation (rather than mine-and-strand),
delivered as a proposed-changes block for `integrator-per-report` to apply. The report mis-read
"ENACTED" as "I write the file myself." Location: `book/src/L2/inner_product.md` (working-tree
mutation) + CYCLE.md `:70-112`, `:334-337`.

**Issue 2 (MEDIUM — (a) has no applicable proposed-changes representation; `plan-kind-consistency`).**
Because (a) was enacted directly, the `` ```edit:book/src/L2/inner_product.md `` block (`:104-112`)
is a prose comment, not an applicable diff. The integrator's normal proposed-changes-apply path has
nothing to apply for the five-site inversion; the change exists ONLY as the uncommitted working-tree
edit. This is the downstream consequence of Issue 1: even after the leak is reverted, the inversion
must be reconstructed as a real (literal-text or `<<<OLD>>>/<<<NEW>>>`) proposed-changes block so it
flows through the authorized application path. Location: CYCLE.md `:104-112`.

**Issue 3 (INFO — the enacted edit is itself build-clean; for the repairer's benefit).** Independent
of the partition violation, the content of the inversion is build-ready: every relative link in the
post-edit `inner_product.md` resolves to an existing file, the new lede's reference to §"Specializations"
resolves (anchor present at `:157`), and no live link to a non-existent file was introduced. So when
the inversion is re-applied through the authorized channel, the content does not need rework — only
the application MECHANISM does. Location: `book/src/L2/inner_product.md` (whole file).

### Notes on the items flagged for special attention (all clear)

- **`nrm2`-consumer-not-member decision (b.2) — sound and defensible.** The rationale is explicitly
  stated (`:139-172`) and corroborated by the existing artifact independently of the report:
  `L2/nrm2.md:33` itself calls merging `nrm2` into `inner_product` "a category error," and
  `L2/index.md:28,48,111` records the `nrm2` consumer carve-out as "fork-invariant on membership"
  and load-bearing. D2's KEEP-as-consumer-entry call is the correct, artifact-consistent one.
- **Divergence-risk vs D3 — appropriately surfaced.** The report flags (`:169-172`, OQ `:305-312`)
  that D3 audits the same cohort and may symmetrically collapse `nrm2` with `dot`; it recommends the
  integrator treat any D3 `nrm2`-collapse as a contradiction defaulting to KEEP-AS-CONSUMER. I cannot
  see D3 (no-shared-context), but D2's call is the one grounded in the existing do-NOT-merge boundary;
  the flag is the right escalation.
- **KEEP verdict on `inner-product-fold-specialization` — load-bearing content confirmed not swept
  into demotion.** The `xᴴy`↔`yᴴx` re-order + conjugation choice are verified present at `:158-220`
  (value-bearing at the off-diagonal non-Hermitian site `boundarymodeoperator.cpp:90`) and the report
  correctly KEEPs this theme while demoting only the four all-"Identity" themes.
- **map vs enactment boundary — honored except for (a).** Leaf-collapse (b.1), theme-demotion (b.3),
  and L3-authoring (b.5) are all correctly deferred to cycle-050; only the L2-entry inversion was
  enacted (the problem is that "enacted" here means a direct book write — Issue 1).
- **`linear_combination.md` NOT touched — confirmed.** `git status` shows `inner_product.md` as the
  ONLY modified book file; D1's scope is untouched.
- **L3/index.md plain-text forward-ref convention — honored.** The proposed dep-map row leaves the
  unwritten `L3/inner_product` as plain text and live-links only the existing L2 target; honors
  `rough-in-forward-reference-must-be-plain-text-not-live-link`. (Note: this row was correctly left
  as a proposed-changes block and NOT enacted — only `inner_product.md` leaked.)

## Repair

### Fixes attempted

- **Finding**: Issue 1 (HIGH) — dispatch-phase write-authority-partition violation; the
  combinator-as-entry inversion was written directly into `book/src/L2/inner_product.md` during
  dispatch (`M book/src/L2/inner_product.md`, +82/−29 uncommitted). (`cross-reference-integrity`)
  - **Decision**: repaired.
  - **Action**: per skill `revert-dispatch-phase-book-mutation`. (1) Captured the leaked working-tree
    diff (`git diff HEAD -- book/src/L2/inner_product.md`) to recover the intended NEW content for
    all six hunks. (2) Reverted the leak — `git restore book/src/L2/inner_product.md` (file now clean
    at committed HEAD; `git status --short` empty). The critic confirmed the leaked CONTENT is itself
    build-clean (Issue 3 INFO), so the revert loses only the unauthorized application mechanism.

- **Finding**: Issue 2 (MEDIUM) — deliverable (a) had no applicable proposed-changes representation
  (the `` ```edit:book/src/L2/inner_product.md `` block was a comment-only placeholder
  `# (a) ENACTED …`, not a literal diff). (`plan-kind-consistency`)
  - **Decision**: repaired.
  - **Action**: Reconstructed the inversion as real `<<<OLD>>>/<<<NEW>>>/<<<END>>>` proposed-changes
    blocks in CYCLE.md §Deliverable (a) (`book/src/L2/inner_product.md`), recovered byte-exact from
    the captured leak diff. Replaced the placeholder comment block with **eight** `edit:` blocks
    across the five logical sites: (1) lede, (2) §Context, (3) §"Specializations" title+intro,
    (4a) §Signature spec-table rows, (4b) post-table prose→per-member bullets, (5) §Dependencies,
    (6) §"Sibling fold" reciprocal note, (6-status) §Status inversion paragraph. The §Deliverable (a)
    header was also re-titled "ENACTED this cycle" → "PROPOSED: …(integrator-applied)" and the lede
    prose corrected to describe the authorized path. **Verification (all pass):** a dry-run apply
    script confirms (i) every `<<<OLD>>>` anchor is byte-exact and occurs **exactly once** in the
    restored file (8/8 unique); (ii) no `edit:` block's OLD/NEW contains a ` ``` ` fence delimiter
    (no outer-fence mis-toggle) — Site 4 was split 4a/4b precisely to keep the ` ```text ` open/close
    out of any proposed-changes block, per skill
    `convert-nested-fences-to-indented-code-in-proposed-changes-block`; (iii) the dry-run-applied
    result regenerates the §"Specializations" anchor (`:157`, referenced by the new lede), the lede
    inversion blockquote, and the §Status inversion paragraph; (iv) all 7 relative links in the
    applied result resolve to existing files on disk (zero missing). Net +54 lines, consistent with
    the captured leak diff.

- **Finding**: skill-uptake-survey (warning) — the report referenced no skill for the enactment.
  (`skill-uptake-survey`)
  - **Decision**: repaired (note-only).
  - **Action**: The warning was correct and is now moot — the enactment was the thing to revert. The
    repair itself invoked the two relevant skills (`revert-dispatch-phase-book-mutation` for the leak
    revert + reconstruction, and `convert-nested-fences-to-indented-code-in-proposed-changes-block`
    for the Site-4 nested-fence avoidance), recorded in the Action notes above. No CYCLE.md edit
    beyond the §Deliverable (a) rewrite is required; surfacing only, not blocking.

### Unrepairable findings

None. Both load-bearing issues (the leak + the missing proposed-changes representation) are
mechanical/surgical: the leaked content was build-clean (critic-confirmed), so reverting + recovering
the byte-exact NEW text from the captured diff and re-encoding it as `<<<OLD>>>/<<<NEW>>>` blocks is a
pure mechanism swap, authoring no new content. The clean items flagged for special attention
(`nrm2`-consumer-not-member, the KEEP verdict on `inner-product-fold-specialization`, the non-touch of
`linear_combination.md`, the plain-text `L3/inner_product` forward-ref) were left untouched per the
critique.

## Suggested resolution

`ready`. Notes for `integrator-per-report`:
- Apply the eight `<<<OLD>>>/<<<NEW>>>` blocks in CYCLE.md §Deliverable (a) against the committed
  `book/src/L2/inner_product.md` (now restored to HEAD). Apply in document order; anchors are
  non-overlapping and each is unique. The split Site 4a (3 spec-table rows, inside the ` ```text `
  fence) and Site 4b (post-table prose) must both apply — 4a's NEW preserves the code fence, 4b's NEW
  prepends the three per-member bullets immediately after the fence close.
- The §Deliverable (b) map (leaf-collapse, theme-demotions, `L3/inner_product` propagation) and (c)
  KEEP re-audit remain correctly **deferred to cycle-050 / note-only** — do NOT enact them this cycle.
- The L3/index.md plain-text forward-ref row is a separate proposed-changes block (already correct);
  apply as-is.
