# upgrade-plain-text-ref-to-live-link-when-target-on-disk

**Promoted:** cycle-024 meta-phase (batch-6). **Proposer:** repairer (cycle-022). **Companion (inverse) convention:** `rough-in-forward-reference-must-be-plain-text-not-live-link` (forbids live-linking a MISSING target; this skill is the opposite case — an on-disk target needlessly left plain-text).

**Audience:** repairer (the fix); also a producer self-check.

## Motivating observation

A producer keeps a cross-reference **plain-text** on a "forward-ref / high→low upward-discipline" rationale, but the referenced chapter is **actually on disk and firm**. The plain-text choice is then a missed live-link, and the surrounding §Supporting-evidence prose can mislead the integrator into thinking the file is absent. The conflation is easy: "don't *define* downward" (the high→low layer-definition discipline — semantics of L_n are defined in L_n vocabulary, not by reducing to L_{n-1}) gets misread as "don't *link* downward." But the high→low discipline governs how semantics are *defined*, not whether a cross-reference *link* is live. The artifact convention is already that firm L_n entries live-link UPWARD to existing L_{n+1} chapters (`ksp_solve`, `chebyshev-smoother`, `orthogonalize` all do) and reference firm lower/sibling chapters with live links.

This recurred as the routine **in-cycle live-link upgrade** pattern across batch-6 (cycle-022 `nleps_deflated_residual`→`lu_solve`, `deflate`→`gram`; cycle-024 `nleps_eigenvalue_correction`→`nleps_jacobian_action`, `deflate-composition-lowering`→`gram-fold-specialization`) — where a report authored before its in-cycle dependency landed referenced it plain-text, and the per-report integrator upgraded to a live link once the dependency was on disk. This skill is the deterministic procedure behind that upgrade.

## Procedure (repairer-facing; also a producer self-check)

For each cross-reference a report keeps plain-text on a "forward-ref / upward-discipline" rationale:

1. **Partition on-disk vs absent.** `ls` / `test -f` the candidate target path. A reference whose target file exists is a *missed live-link candidate*; a genuinely-absent target stays plain-text (the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention).
2. **Survey the convention for that reference KIND.** Confirm the artifact already live-links the same kind of cross-reference — e.g. `grep -rn '\.\./L2/' book/src/L1/*.md` to confirm L1→existing-L2 upward links are conventional, or `grep -rn '\./<sibling>' book/src/<layer>/*.md` for same-layer sibling links. (The high→low discipline does NOT forbid the link; it forbids defining semantics downward.)
3. **Upgrade only the on-disk references** to live links at the canonical declaration site (the §Dependencies row + any dep-map cell), using the correct relative path, and **re-verify the path resolves** (`test -f` the resolved target, or `python3 tools/citecheck/citecheck.py <book/src/...path...>:1` for a bounds check) — the dead-link direction is the only hazard, and this step closes it.
4. **Leave genuinely-absent targets plain-text.** If the report's prose lumped an on-disk reference with absent ones (telling the integrator the file is missing), correct the prose so the integrator is not misled.

Net: a deterministic on-disk partition + convention survey + relative-path upgrade + re-verify. Bounded and safe.

## When to apply it in-cycle (the live-link-upgrade pattern)

When report B (authored before its dependency report A landed) references A's chapter plain-text, and A lands earlier in the same cycle's serial integration: the per-report integrator applying B re-reads disk, finds A's chapter present, and upgrades B's plain-text reference to a live link in the same apply (re-verifying the path). This is the canonical in-cycle reconciliation, build-safe, analogous to the Firm-count serial reconciliation. Record it as `in_cycle_live_link_upgrade` in the staging row.

## Cross-references

- Friction-ledger `rough-in-forward-reference-must-be-plain-text-not-live-link` — the inverse (don't live-link a missing target).
- CLAUDE.md §Methodology invariants "Layers are defined high→low" — the discipline that governs *definition*, not *linking*.
- `skills/verify-citation-range/SKILL.md` — the path re-verify in step 3.
