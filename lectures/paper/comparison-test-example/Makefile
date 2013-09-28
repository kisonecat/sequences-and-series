all: $(patsubst %.tex,%.pdf,$(wildcard *.tex)) $(patsubst %.tex.erb,%.pdf,$(wildcard *.tex.erb))

%.pdf: %.tex
	pdflatex $<

%.tex: %.tex.erb
	ruby -e "require 'erb'; f = File.open( \"$@\", 'w' ); f.puts ERB.new( File.read( \"$<\" ), nil, '>' ).result(binding); f.close"

clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.pdf
	rm -f *.png
