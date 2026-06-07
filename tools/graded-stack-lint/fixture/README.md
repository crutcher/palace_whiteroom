# graded-stack-lint fixture

A small hand-authored typed graph under `book/src/` that exercises every
load-bearing behavior of the two linters, so they are **demonstrably correct**
independent of the real (mostly-untyped) tree. Run:

```bash
python3 tools/graded-stack-lint/graded_stack_lint.py \
    --book-src tools/graded-stack-lint/fixture/book/src --show-inbound
```

## The graph

```
feature/widget.L4   (root, firm)  --depends-on--> L1/good_op (firm)   --> L0/leaf_cite (firm)
                                  --depends-on--> L1/prose_firm_provenance (firm via prose ## Status)
                                  --depends-on--> L1/weak_op (rough-in) --> L0/leaf_cite
                                  --reference---> feature/sibling.L4  (sibling root; NOT blocking)
feature/sibling.L4  (root, firm)  --depends-on--> L1/good_op
L2/legacy_compose   (root via legacy status: seed)
                                  --depends-on--> L1/good_op           (composes: vocabulary op)
                                  --reference---> feature/sibling.L4   (composes: sibling column)
L1/orphan           (firm)        --depends-on--> L0/leaf_cite         (NO root depends on it)
L1/ref_only_leaf    (firm)        --depends-on--> L0/leaf_cite
                                  <--reference--   feature/widget.L4    (reachable ONLY via reference)
L1-L0/widget-lowering (declared firm)
                                  --depends-on--> L1/weak_op (rough-in), L0/leaf_cite
concepts/untyped_concept          (no frontmatter at all)
```

## Expected outcomes (the assertions)

1. **KNOWN rank violation** — `feature/widget.L4` is `firm` but `depends-on`
   `L1/weak_op` which is `rough-in` ⇒ a rank violation. (A firm node cannot rest
   on a rough-in dep, scheme §1b.)

2. **Lowering-theme rule** — `L1-L0/widget-lowering` declares `firm` but one
   endpoint (`weak_op`) is `rough-in`, so `min(endpoints) = rough-in` ⇒ a note
   "declared rank firm exceeds min-of-endpoints rough-in" AND a rank violation on
   the `weak_op` edge.

3. **KNOWN unreachable node** — `L1/orphan` is `firm` yet no feature root
   `depends-on` it ⇒ reported as DETRITUS even though its rank is firm (liveness
   ≠ resolution, scheme §2). It has a typed outbound dep, so it lands in the
   "stronger garbage signal" bucket.

4. **`reference` edges do not carry liveness** — `feature/widget.L4`'s
   `reference` to `feature/sibling.L4` is navigational; sibling roots do not gate
   each other (OWN-COMPOSITION, scheme §3). Both are independently roots anyway.

5. **Transitional dual-form root** — `L2/legacy_compose` uses legacy
   `status: seed` as its root marker (no `feature_root:`); the linter still marks
   it a root (D1 OQ `graded-stack-feature-root-frontmatter-split`).

6. **Migration mapping** — `L2/legacy_compose`'s `composes:` of a vocabulary op
   (`L1/good_op`) becomes a `depends-on`; its `composes:` of a sibling column
   (`feature/sibling.L4`) becomes a `reference`; its `l0_ground_truth:` cite
   (`palace/foo/bar.cpp:10-20`) is NOT treated as a book node.

7. **Untyped is a WARNING, not an error** — `concepts/untyped_concept` has no
   frontmatter; it is counted as untyped and never fails the run.

8. **Exit code** — 1 (because rank violations exist). With the violations
   removed the run would exit 0; untyped + detritus alone never fail.

9. **Prose `## Status` leading-token rule** (c096 token-priority-bug guard) —
   `L1/prose_firm_provenance` carries NO `rank:`/`firmness:`/`status:`
   frontmatter, so its rank is derived from the prose `## Status` line. That line
   LEADS with `` `firm` `` but its body *mentions* "rough-in" and "stub" in
   provenance phrases. The reader must read it as **firm** (the leading
   inline-code token), NOT rough-in/stub. Because it reads firm, the
   `feature/widget.L4 (firm) -> L1/prose_firm_provenance (firm)` edge is
   well-founded and produces NO rank violation. Under the OLD blob-scan
   (rough-in/stub before firm), this node would have mis-derived
   `rough-in (test-coverage-bounded)` and manufactured a spurious violation —
   the exact c095 bug (12 ledger instances) this case guards against.

10. **Reference-reachable split** (ASK-1 / scheme §2g; the deliberate-reference-
    only-reachable cohort guard) — `L1/ref_only_leaf` is `firm` and no feature
    root `depends-on` it, so the depends-on-only GC marks it DETRITUS
    (`[GARBAGE*]`, stronger-signal bucket — it declares a typed dep). But
    `feature/widget.L4` (a reachable root) points at it over a `reference` edge,
    so the reference-augmented mark REACHES it. It must therefore land in
    `detritus_reference_reachable_re11_cohort` (with back-link attribution
    `<-ref/dep- feature/widget.L4`), NOT in `true_detritus`. `L1/orphan` and
    `L1-L0/widget-lowering` have NO inbound reference from a reachable node, so
    they stay `true_detritus` — the genuine dead-intent health signal. This
    guards that the §2g split separates the deliberate cohort (firm-and-faithful,
    correctly off the depends-on spine) from real garbage, and that the split is
    a REPORTING refinement only (gate behavior — exit 1 from the rank violations —
    is unchanged; raw `detritus` still counts all three).

Confirmed outputs (cycle-123 batch-39 meta — adds assertion #10, the §2g
reference-reachable tier):
`files=11, typed=10, untyped=1, roots=3, rank_violations=2, reachable=7,
reference_reachable=8, detritus=3 (true_detritus=2 / reference_reachable=1),
promotion_frontier=1, exit=1`.
(cycle-096 was `files=10, … reachable=7, detritus=2` before the `ref_only_leaf`
reference-reachable-cohort guard node was added; cycle-094 P0-B baseline was
`files=9, typed=8, … reachable=6` before the `prose_firm_provenance` guard.)
