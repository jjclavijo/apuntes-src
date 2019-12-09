apunte.pdf: apunte_f.tex
	mv apunte_f.tex apunte.tex
	xelatex apunte.tex
	xelatex apunte.tex

apunte_f.tex: apunte.tex
	sed -E '/:::\ ([A-z]+)/ {s/:::\ ([A-z]+)/\\begin\{\1\}/;h};/::::+/{x;s/\\begin\{([^\}]*)\}.*/\\end\{\1\}/;p;x;d}' $< > $@
	sed -E 's/\\url\{eqn:/\\ref\{eqn:/' -i $@

apunte_l.org: apunte.org
	sed -E '/\#\+NAME:/ {N;s/.*\ ([^\ ]*)\n\\begin(\{.*\})/\\begin\2\n\\label\{\1\}/}' $< > $@

apunte.tex: apunte_l.org
	pandoc -t latex -o $@ -s $< --pdf-engine xelatex -H head.tex

clean:
	-@rm apunte.aux apunte.log apunte.tex apunte.pdf apunte_f.tex apunte_l.org
