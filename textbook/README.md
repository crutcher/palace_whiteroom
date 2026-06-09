# Tensor-Field Simulation — How the Synthesis Surface Simulates Its Targets

An illustrated LaTeX textbook (memoir class, TikZ figures) teaching how the Palace
electromagnetic simulator's *synthesis surface* simulates its targets, from a college
sophomore math + engineering background. Target ≈ 800 pages.

## Build

    make            # -> main.pdf  (pdflatex + bibtex via latexmk)
    make clean

Requires TeX Live 2023+ (pdflatex, latexmk, bibtex) with memoir, tikz, pgfplots,
listings, tcolorbox, hyperref, cleveref, natbib, siunitx.

## Layout

    main.tex                  master document (\include's the parts)
    OUTLINE.md                the master plan + per-chapter authoring brief + page budget
    style/simbook.sty         preamble: packages, theorems, boxes, the L4 pseudocode listing
    style/simtikz.sty         shared TikZ styles for the recurring diagrams
    references.bib            bibliography
    frontmatter/              preface, how-to-read, notation primer
    part1-orientation/ ...    one .tex per chapter, grouped by part
    appendices/               deep computation semantics
    figures/                  standalone TikZ figures (when factored out)

Source of truth for content: the layered spec under `../book/src/**` (cited per chapter
in OUTLINE.md). The book teaches the framework; it draws physics/math from the field-theory
chapters and the calculus from `../book/src/semantics/index.md` + `../book/src/concepts/`.
