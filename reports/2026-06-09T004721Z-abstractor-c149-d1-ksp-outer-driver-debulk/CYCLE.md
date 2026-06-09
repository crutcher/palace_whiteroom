---
agent: abstractor
invoked_at: 2026-06-09T004721Z
scope: FINALIZATION de-bulk (cycle-149 D1) — book/src/L3-L2/ksp-solve-outer-driver.md
status: pending
integrated_at: 2026-06-09T010000Z
integration_commit: 0877522
integration_notes: "cycle-149 FINALIZATION de-bulk wave (D1). Applied (de-bulk ALREADY on disk per FINALIZATION convention; STAGED, not re-applied). book/src/L3-L2/ksp-solve-outer-driver.md: 13 process attributions -> 0, retired-directive footer removed, kernel/driver contrast + table + disjoint-subjects law lifted to static, Verified-against -> Evidence. Status firm sole-rank-carrier token PRESERVED. No node/edge/rank/status move. graded-stack baseline HELD EXACTLY; build EXIT 0; step-5c/5d PASS."
inputs:
  - book/src/L3-L2/ksp-solve-outer-driver.md (the target — 13 cycle/batch/wave attributions, batch-47 finalization miss)
  - skills/finalization-debulk/SKILL.md (the discipline)
  - book/src/L4/krylov_step.md (exemplar — `## Evidence` citation home, no `## Status` prose for firm-frontmatter)
---

# CYCLE: FINALIZATION de-bulk — ksp-solve-outer-driver

## Summary

De-bulked `book/src/L3-L2/ksp-solve-outer-driver.md` — the heaviest residue file in the batch-47 FINALIZATION miss-set (13 cycle/batch/wave attributions) — toward a clean static-state statement, applying the `finalization-debulk` skill. The file has **NO YAML frontmatter** (it opens with `# ksp-solve-outer-driver`), so its `## Status` leading `firm` token is the **SOLE rank carrier the graded-stack linter reads** — that token was preserved as the first non-empty line after `## Status` per the load-bearing no-frontmatter-rank rule. Stripped all 13 process-attribution tags; renamed `## Verified-against` → `## Evidence` (the exemplar's citation home) and dropped the `(firm, cycle-NNN wave-N)` parentheticals on cited entries; lifted the kernel-identity / driver-non-identity contrast out of "the cycle-020 critic's mild tension" meta-framing into a clean static structural statement (content preserved); deleted the provenance footer entirely (pure process provenance citing the RETIRED/SUPERSEDED "Identity-lowerings still require both L levels" directive). Edited the file directly (de-bulk convention, c148 precedent).

## Tags before / after

- **Before: 13** (`grep -cE 'cycle-[0-9]|c0[0-9][0-9]|batch-[0-9]|wave-[0-9]'`).
- **After: 0.** Confirmed `grep -nE` returns no matching lines.

Tag locations stripped: lines 14, 16 (Context `firm cycle-NNN wave-N` parentheticals), 105 (Speculative-ops `firmed cycle-007`), 109 + 121 (contrast-section "cycle-020 critic" framing), 129/130/134/135 (Evidence-section `(firm, cycle-NNN ...)`), 154/155 (strawman-evidence `(firm cycle-008/007)`), 171 (Status promotion-history prose), 173 (the deleted provenance footer).

## Citation count before / after (MUST match)

- **Inline source-line citation tokens (`:N` / `:N-M`): 33 → 33.** Identical (`grep -oE ':[0-9]+(-[0-9]+)?' | wc -l`). Every `palace/…:N-M` source range preserved verbatim — none of the 10 distinct `palace/linalg/…` ranges nor any inline `:417` / `:427` / `:463` / `:484-485` / `:563` / `:703-704` / `:52` / `:53` / `:54` / `:56` / `:98` / `:300` etc. was touched.
- **Internal book links: byte-for-byte identical** before/after (verified `grep -oE '\]\(\.\.?/…\.md\)' | sort | uniq -c` — all 11 distinct targets at identical multiplicities: `./krylov-step-body-identity.md ×5`, `../L2/ksp_solve.md ×4`, `../L3/ksp_solve.md ×5`, `../L2/krylov_step.md ×5`, etc.). No link broken, dropped, or converted to prose. No `reports/…` link existed to drop.

## Status-token preservation (no-frontmatter-rank file — load-bearing)

- The file has no YAML `rank:`/`firmness:` frontmatter → `## Status` is the sole rank carrier.
- The `## Status` section was NOT deleted. It was rewritten to a concise static statement whose **first non-empty line still leads with `` `firm` ``** (verified: `awk '/^## Status/{f=1;next} f&&NF{print;exit}'` returns the `` `firm` — both endpoints are firm … `` line).
- Stripped from `## Status`: the cycle-020/021 endpoint-firmness attributions, the "resolves the cycle-020 critic's mild tension" meta-narrative, and the entire provenance footer (which additionally cited the **retired/superseded** "Identity-lowerings still require both L levels" directive — doubly stale, removed entirely). Kept the static "what it IS" content (substantive non-identity; iteration-view erasure + obstruction shadow-to-non-laws; information-preserving consolidation; driver complement of the sibling theme; contrast to the BLAS-1 cohort).

## Lint baseline (MUST hold exactly)

`python3 tools/graded-stack-lint/graded_stack_lint.py --book-src book/src`:

```
files=392, typed=331, untyped=61, rank_violations=0,
unresolved_depends_on_targets=0, promotion_frontier=11,
detritus=123, true_detritus=51
```

**HELD EXACTLY** — matches the stated baseline on every field. The node `L3-L2/ksp-solve-outer-driver` remains typed and present (appears in `detritus`/`true_detritus` exactly as before — de-bulk was prose + `## Status`-section + section-header editing only; no node/edge/rank/status/slug/anchor moved). `cargo make book` not run by this dispatch (de-bulk is prose-only, no fence/KaTeX structure changed; the build guard is integrator-finalize's).

## Structural content LIFTED vs STRIPPED

**LIFTED (kept as clean static structural content):**
- The kernel-identity / driver-non-identity contrast (§"Kernel-identity / driver-non-identity contrast" + the §"L3>L2 vs kernel-theme distinction" tail). The structural claim is fully preserved: the kernel *body* collapses identity-in-form across the hop; the driver *loop* is the genuine iteration-rotation (its explicit-recursion view is erased at L2, along with the named `sequential-obstruction` which shadows to the L2 non-laws); the two classifications are about **disjoint subjects** so they do not conflict. Only the framing changed — "the mild tension the cycle-020 critic noticed … is not a tension because …" → a direct static statement "That `ksp_solve` is classified non-identity while the kernel is classified identity is **not a conflict**: the two classifications are about disjoint subjects …". The contrast table, the `kernel-identity + driver-non-identity` identity, and the disjoint-subjects reasoning all survive intact.
- `## Verified-against` → `## Evidence` (the exemplar's static citation home per the skill's KEEP/Evidence convention). All evidence bullets, all `§…` section pointers, and all citations preserved — only the `(firm, cycle-NNN wave-N)` process tails on the cited entries were dropped.

**STRIPPED (pure process/judgment accounting):**
- 13 `cycle-NNN` / `wave-N` / `firmed cycle-NNN` attribution tags across Context, Speculative-ops, contrast, Evidence, strawman-evidence, and Status.
- The `## Status` promotion-history prose (endpoint-firmness cycle attributions; "resolves the cycle-020 critic's mild tension" meta-judgment).
- The "self-verified against `reference/palace/` source via `palace-codemap` `read_range` this dispatch" L0-evidence process preamble → bare "L0 evidence:".
- **DELETED entirely:** the line-173 provenance footer ("Authored cycle-021 wave-2 (abstractor), enacting **Identity-lowerings still require both L levels** … and **Layers are defined high→low** …") — pure process provenance, AND it cited a methodology directive that is RETIRED/SUPERSEDED by the VOCABULARY-SHIFT REDIRECT (per CLAUDE.md). Doubly stale; its one non-process residue (the substantive-vs-BLAS-1-cohort contrast) was preserved by folding it into the rewritten `## Status` static clause.

## Supporting evidence

- Target file: `book/src/L3-L2/ksp-solve-outer-driver.md` (edited in place).
- Exemplar: `book/src/L4/krylov_step.md` (`## Evidence` citation home; firm-frontmatter ⇒ no `## Status` prose — but the target differs in having NO frontmatter, so the `## Status` `firm` token is retained as the sole rank carrier).
- Skill: `skills/finalization-debulk/SKILL.md` (STRIP/KEEP/LIFT discipline; the no-frontmatter-rank `## Status`-as-sole-carrier rule; the no-node/edge/rank/status-MOVE safety invariant).

## Open questions / caveats

- The retired-directive citation ("Identity-lowerings still require both L levels") appeared only in the deleted provenance footer; no live spec content depended on it. No other reference to a retired/superseded directive remains in the file.
- The sibling theme `krylov-step-body-identity.md` is referenced 5× and was NOT touched — those links stay valid. If that sibling is a later de-bulk target, its own `(firm)` parentheticals (not cycle-tagged here) are out of this dispatch's scope.
- Build (`cargo make book`) deferred to integrator-finalize per the write-authority partition; no fenced-block / KaTeX `$`-sigil structure was altered, so no build risk introduced.
