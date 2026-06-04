---
layer: L1
operator: prose_firm_provenance
edges:
  depends-on:
    - L0/leaf_cite
---
# prose_firm_provenance (firm, derived from the prose `## Status` line)

This node carries NO `rank:`/`firmness:`/`status:` frontmatter, so `derive_rank`
falls through to the prose `## Status` reader. It exercises the c095
token-priority bug: a genuinely **firm** node whose `## Status` paragraph
*mentions* "rough-in" and "stub" in downstream provenance phrases. A blob-scan
in priority order (rough-in/stub BEFORE firm) would mis-read it as rough-in; the
leading-inline-code-token rule reads it correctly as `firm`.

## Status

`firm` — promoted from rough-in (test-coverage-bounded) once the dedicated test
landed; it was a stub before that. The provenance words "rough-in" and "stub"
above appear ONLY as history; the leading inline-code token is the maturity word.
