apunte.pdf: apunte.org
	pandoc -t latex -o apunte.pdf apunte.org --pdf-engine xelatex -H head.tex

apunte.tex: apunte.org
	pandoc -t latex -o apunte.tex -s apunte.org --pdf-engine xelatex -H head.tex

clean:
	-@rm apunte.aux apunte.log apunte.tex apunte.pdf
