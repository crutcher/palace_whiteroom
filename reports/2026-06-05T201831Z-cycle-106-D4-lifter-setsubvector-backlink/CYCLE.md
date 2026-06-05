---
agent: lifter
invoked_at: 2026-06-05T20:22:44Z
scope: concepts/set_subvector_zero frontmatter — doubly-stale reference-edge de-stale + reciprocal back-link (item-3a set-subvector-zero-references-dofset)
status: integrated
integrated_at: 2026-06-05T223000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-106 D4 (LOW), applied clean. concepts/set_subvector_zero reference back-link de-staled to [L1/set_subvector_zero, concepts/dofset] (doubly-stale reference:[] + false comment removed; edge now bidirectional). EXPECTED-NOT-DEFECT: a reference creates no reachability (cluster stays detritus; page becomes typed, untyped −1). Build EXIT 0; rank_violations 0. OQ set-subvector-zero-cluster-reachability-not-rescued-by-reference-backlink promoted (routes into the dofset/eliminate_bc follow-up)."
inputs:
  - book/src/concepts/set_subvector_zero.md
  - book/src/L1/set_subvector_zero.md
  - book/src/concepts/dofset.md
---

# CYCLE: Re-anchor concepts/set_subvector_zero frontmatter (doubly-stale back-link)

## Summary
The concept page `book/src/concepts/set_subvector_zero.md` carries a doubly-stale `reference: []` frontmatter edge with an inline comment asserting "no book home: L1/set_subvector_zero does not exist". Both halves are now false: (1) the L1 operator entry `book/src/L1/set_subvector_zero.md` landed c104/c105 (verified on disk, `firm`-rank, 24662 bytes), and (2) the reciprocal `reference` back-link to `concepts/dofset.md` was missing even though `concepts/dofset.md:18` already lists `concepts/set_subvector_zero` as one of its own `reference` targets (the edge was one-directional). This is a pure frontmatter back-link fix: replace the empty `reference: []` with a block sequence of the two now-correct slug targets (`L1/set_subvector_zero`, `concepts/dofset`) and de-stale the inline comment. No prose/semantics touched.

## Proposed changes

```edit:book/src/concepts/set_subvector_zero.md
[old]:
---
edges:
  reference: []                    # no book home: L1/set_subvector_zero does not exist; the
                                   # divfree use-site and the L3 mask-multiply lift are described
                                   # in-page. Non-node pointer page; no outbound book edges.
---
[new]:
---
edges:
  reference:
    - L1/set_subvector_zero        # authoritative L1 operator entry (landed c104/c105; firm)
    - concepts/dofset              # reciprocal back-link (dofset.md references this page)
---
```

## Discipline notes
- **Bounded, evidenced, recorded prose-correction of frontmatter (NOT page semantics).** The change is confined to the `edges:` block — a derived navigation surface — and corrects a factually-false claim ("L1/set_subvector_zero does not exist") that disk state contradicts. Supporting L0-equivalent evidence: `ls` shows `book/src/L1/set_subvector_zero.md` present (10447... 24662 bytes, mtime Jun 5 02:35); `book/src/L1/set_subvector_zero.md:1-5` shows `rank: firm`, `operator: set_subvector_zero`; `book/src/concepts/dofset.md:12-18` shows the `reference:` block already lists `concepts/set_subvector_zero` (the reciprocal half this fix completes). The page's prose body (Signature / Role in the vocabulary / etc.) is untouched.
- **Slug/path form matches the on-disk scheme, NOT the dispatch prompt's suggested `book/src/...` form.** The dispatch text suggested `reference: [book/src/L1/set_subvector_zero.md, book/src/concepts/dofset.md]`, but every sibling concept page and the graded-stack linter use **bare slugs** in `reference:` block sequences (`L1/axpy`, `concepts/dofset`, `concepts/set_subvector_zero` — see `concepts/dofset.md:13-20`, `concepts/axpy.md`, `concepts/apply_linop.md`). The dispatch instruction explicitly deferred to "whatever exact slug/path form the scheme + sibling concept pages use" — so I matched the bare-slug block-sequence convention. The linter resolves `L1/set_subvector_zero` -> `book/src/L1/set_subvector_zero.md` and `concepts/dofset` -> `book/src/concepts/dofset.md`; both files exist, so both edges resolve.
- **`reference` (not `depends-on`) is correct.** These are navigational see-also edges (a concept page pointing at its authoritative L1 home + a reciprocal record-page link), constraining neither rank nor liveness — exactly the `reference` semantics. No rank invariant is engaged (this page carries no `rank:` token; it is a non-node pointer/concept page).

## Supporting evidence
- `book/src/concepts/set_subvector_zero.md:1-6` — current doubly-stale `reference: []` frontmatter.
- `book/src/L1/set_subvector_zero.md:1-21` — the now-existing firm L1 home (`rank: firm`, landed c104/c105).
- `book/src/concepts/dofset.md:12-20` — dofset's `reference:` block already lists `concepts/set_subvector_zero` (the one-directional edge this fix reciprocates).
- Linter (current tree, pre-change): `RESULT: 0 rank violation(s), 163 detritus node(s), 77 untyped (warning).` — `concepts/set_subvector_zero`, `L1/set_subvector_zero`, and `concepts/dofset` all currently sit in the `[garbage?]` detritus set (lines for `concepts/set_subvector_zero`, `L1/set_subvector_zero` @157, `concepts/dofset` @199). No UNRESOLVED-edge error involves any of these three slugs (the 21 UNRESOLVED targets are unrelated). So the new `reference` targets resolve cleanly and introduce **no** new rank violation and **no** new unresolved edge.

## Open questions / caveats
- **Reachability is NOT resolved by this fix, and that is expected for a LOW-fan-out back-link.** All three nodes (`concepts/set_subvector_zero`, `L1/set_subvector_zero`, `concepts/dofset`) are currently detritus (unreachable from the feature-surface GC roots). Adding a `reference` edge does not change reachability (reachability is computed over `depends-on`, and `reference` edges to/among already-unreachable nodes add no liveness). This fix only corrects the false comment + completes the reciprocal `reference` link; it does not — and is not scoped to — rescue the cluster from detritus. The detritus-cluster question (whether `set_subvector_zero` / `dofset` / their BC-enforcement neighborhood should be made root-reachable via a `depends-on` edge from a feature column or a firm consumer) is a separate, higher-fan-out reachability item — flagging here so it is not silently assumed closed by this back-link fix.

## Post-change linter confirmation (run on tree WITH the proposed edit applied to a scratch copy, then restored)
The proposed edit was applied to a scratch copy of the file, the linter re-run, and the file restored to its original on-disk state (`git diff` clean). The integrator applies the real edit in Phase 5; this is the producer self-verification that the new edges resolve and introduce no regression.

Pre-change (current tree):

    RESULT: 0 rank violation(s), 163 detritus node(s), 77 untyped (warning).

Post-change (scratch tree with the proposed edit):

    RESULT: 0 rank violation(s), 164 detritus node(s), 76 untyped (warning).

- **0 rank violations held** (no new rank violation — the only invariant that hard-gates at finalize).
- **0 unresolved-edge errors involving our slugs** (`grep UNRESOLVED | grep set_subvector_zero\|dofset` -> none). Both new `reference` targets (`L1/set_subvector_zero`, `concepts/dofset`) resolve to existing files.
- **untyped 77 -> 76**: the page previously had no edges (untyped); adding the `reference` block types it, removing it from the untyped-warning set. This is the intended direction (one fewer untyped node).
- **detritus 163 -> 164 (+1)**: benign and expected. Adding outbound `reference` edges pulls this previously-edgeless page into the DAG the GC walks, so it is now *enumerated* among the unreachable cluster (it was already unreachable — see Open questions; a `reference` edge does not create reachability). No node became newly-unreachable; the +1 is the now-typed page joining the counted-detritus set rather than being skipped as edgeless. The whole `set_subvector_zero` / `L1/set_subvector_zero` / `dofset` neighborhood was already detritus pre-change.

Correction note: an earlier draft of this section asserted detritus "unchanged at 163" from memory before the scratch run; the actual measured post-change figure is 164 (+1, benign as explained). The numbers above are the real linter output.
