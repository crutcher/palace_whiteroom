# Build the textbook PDF.  `make` -> main.pdf ; `make clean` ; `make watch`
.PHONY: all clean watch
all: main.pdf
main.pdf: main.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
watch:
	latexmk -pdf -pvc -interaction=nonstopmode main.tex
clean:
	latexmk -C
	rm -f */*.aux
