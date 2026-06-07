---
name: deleted-slug-inbound-live-link-sweep
verb: enumerate-then-check the inbound live links to every slug a report deletes, before asserting de-link completeness
owners: [critic, integrator-per-report]
promoted: cycle-051 (batch-15 meta-phase)
companions: [proposed-changes-fence-encloses-full-body-guard, convert-nested-fences-to-indented-code-in-proposed-changes-block, revert-dispatch-phase-book-mutation]
---

# deleted-slug-inbound-live-link-sweep

**When to invoke.** A report's proposed-changes delete ANY `book/src/**` file (a theme/operator/feature chapter, a dep-map entry, a `roadmap_goal`/`stub`, or — historically through batch-31 — a Phase-1 slice). Run this BEFORE the critic asserts `cross-reference-integrity: pass`, and as the per-report integrator's pre-apply check. A live markdown link `](.../<deleted-file>.md)` surviving anywhere in `book/src/` after the deletion is a **hard `mdbook-linkcheck2` build error** at finalize — this skill catches it at critique/apply time instead of at the build. (The Phase-1 slice-deletion campaign that exercised this skill heavily is COMPLETE as of cycle-099, but the inbound-sweep discipline is the steady-state expectation for **every** future file deletion — it is NOT slice-specific.)

**Why it exists.** Producer-side de-link reasoning done ad-hoc per *recalled* reference is thorough-but-incomplete: cycle-051 D1 (a multi-file `delete:` of 8 themes) correctly de-linked the 4 re-expressed leaves, the combinator home, and 3 analogy-gate files — but MISSED `book/src/L3/index.md`, which carried 6 live links to the deleted slugs (caught by the critic, would have been 6 build errors). The fix is a **mechanical enumerate-then-check step** that does not rely on the producer recalling every inbound reference.

## Procedure

For EVERY slug `<slug>` appearing in a `delete:` fence (directory `<dir>`, e.g. `L3-L2`, `L2-L1`, `L2`, `L3`):

1. **Enumerate inbound LIVE links** across the whole artifact:
   ```
   grep -rnoE '\]\((\.\./)*'"<dir>"'/'"<slug>"'\.md\)' book/src
   ```
   (the `(\.\./)*` allows any relative-depth prefix; the `\]\(` … `\)` requires an actual markdown link, not a bare code-span).

2. **Subtract the two exempt sets** from the hit list:
   - **(i) files being deleted in this same report** — their internal cross-links self-resolve (they vanish with the files). Include sibling-dispatch delete targets *only if you can confirm the sibling deletes them this cycle* — otherwise treat as live (see step 4).
   - **(ii) files this report's own proposed-changes already edit** (the producer is handling those de-links) — verify the edit actually removes/de-links the reference, do not assume.

   **⚠ Exclude the target file by SOURCE-PATH prefix, NEVER by link-target text** (the cycle-098-D1 grep-bug; friction-ledger `slice-deletion-inbound-link-sweep-self-exclusion-grep-bug`). To drop the target file's *own* lines from the hit list, filter on the SOURCE path the hit originates from — `grep -v '^book/src/<dir>/<name>.md:'` — i.e. the `file:` prefix the `grep -rn` emits. Do **NOT** filter on the link-target substring (`grep -v 'spec/slices/orthog.md'`): every inbound `[..](../spec/slices/orthog.md)` link literally CONTAINS `spec/slices/orthog.md` in its target text, so a link-target-text `grep -v` SILENTLY SWALLOWS exactly the inbound links you are hunting (c098-D1 missed 8 this way — 6 external + 4 relative-sibling — and reported only the 2 backtick-inline-code refs, which are not even build-breaking). The self-exclusion predicate is about WHERE THE LINE LIVES (source path), not WHAT IT POINTS AT (link target).

3. **Any residual surviving file with a live link is an unhandled build-breaker.** Flag `cross-reference-integrity: fail` (critic) / refuse-or-defensively-de-link (integrator) with the exact `file:line`.

4. **Cross-dispatch danglers (multi-deletion cycles).** A live link inside a file that is a *different* dispatch's delete target is correctly LEFT untouched by this report (it dies with the file when that sibling applies — editing it would be a cross-dispatch edit conflict / moot edit). Record it as "dies-with-file (dispatch <X> delete target)" and rely on integrator-finalize's mandatory post-all-dispatches dead-link re-grep to confirm zero survivors before `cargo make book`. Do NOT de-link it in this report.

5. **KEPT-sibling exclusion.** If a slug in the cohort is KEPT-substantive (not deleted — e.g. `divfree-projector-leaf-identity` survived the c051 sweep), its live links are CORRECT and must be EXCLUDED from the sweep. Confirm the KEPT slug's file is on disk; its inbound links are not danglers.

6. **N-dispatch co-edit of one surviving line.** When ≥2 dispatches each de-link a *different* slug from the SAME surviving line (the c051 line-266 3-way case), narrow each `old_string` to the **slug-distinct substring** (not the whole line), so the edits compose order-independently across the serial per-report applies. This is the line-granularity instance of the per-anchor-distinctness wave-conflict philosophy.

7. **Frontmatter typed-edge sweep (the silent-dangler surface; added batch-40).** In ADDITION to the markdown-link grep (step 1), sweep the frontmatter typed edges for every deleted slug:
   ```
   grep -rnE '(depends-on|reference|lifts-from|lifts-kernel-impl|realizes-kernel-api)[^]]*\b'"<slug>"'\b' book/src
   ```
   (matches a slug named inside any typed `edges:` block list, regardless of bracket layout). Apply the SAME step-2 exemptions (source-path-prefix self-exclusion; files this report already edits; sibling delete targets). For each residual hit, **re-point the edge to the surviving consolidation target** (the node the deleted slug folded into — e.g. an eliminated arity-leaf folds into its combinator) or **strike it** if the relationship genuinely vanishes. Rationale: `linkcheck2` is blind to frontmatter edges; a stale `depends-on` reaches the artifact and only trips the finalize rank-linter (`unresolved_depends_on_targets`), and a stale `reference` is caught by nothing. The c124 RE6 elimination shipped two stale `depends-on` edges (`L3/normalize → L3/scal`, `L3/orthogonalize → L3/axpy`, both to deleted leaves) past the body-link sweep — this step closes that gap at critique/apply time. **The consolidation-target re-point is faithful only when the deleted slug genuinely folded into that target** (the combinator-primary case); if the deletion is a true removal with no successor, STRIKE the edge, do not invent a target.

## Tiers

- **LIVE markdown link `](.../<slug>.md)`** — build-breaking. Must be zero after all dispatches apply. This skill's primary target.
- **Frontmatter typed-edge `edges:` reference to the deleted slug** — **linter-breaking / silent-dangler tier** (added batch-40, friction `deleted-slug-frontmatter-edge-gap`). A surviving YAML frontmatter `depends-on` / `reference` / `lifts-from` / `realizes-kernel-api` edge that names a DELETED slug is **invisible to `mdbook-linkcheck2`** (frontmatter edges are not markdown links) and so does NOT surface at `cargo make book`. A stale **`depends-on`** edge IS caught by the graded-stack rank linter (`unresolved_depends_on_targets > 0`), but only at the finalize linter run — too late for the per-report integrator; and a stale **`reference`** edge is caught by NEITHER (reference targets are not rank-checked), making it a silent navigational dangler. This tier is the third de-link surface (alongside markdown links + prose mentions); a destructive deletion of a node that other chapters carry a typed `edges:` block to (the class created by the graded-stack §5 typed-edge campaign — e.g. the c124 RE6 arity-leaf elimination) MUST sweep it. See Procedure step 7.
- **Bare code-span / path reference** (backticked slug, no `](...)`) — stale-but-NOT-breaking (LOW tier). `linkcheck2` does not check prose code-spans. Flag as a narrative-honesty residual for a micro-sweep / count-owner annotation; do not block on it.

## Output

Critic: a `cross-reference-integrity` finding per residual live link with `file:line` (fail) or a one-line "inbound-sweep clean: N slugs, M exempt, 0 residual" (pass). Integrator: defensively de-link any survivor per build-repair authority, or refuse the apply if the de-link would alter load-bearing content.

Companion to `proposed-changes-fence-encloses-full-body-guard` (which guards fence shape, not inbound links).
