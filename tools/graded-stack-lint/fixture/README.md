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

Confirmed outputs (cycle-096 — adds assertion #9):
`files=10, typed=9, untyped=1, roots=3, rank_violations=2, reachable=7,
detritus=2, promotion_frontier=1, exit=1`.
(cycle-094 P0-B baseline was `files=9, typed=8, … reachable=6` before the
`prose_firm_provenance` guard node was added.)
