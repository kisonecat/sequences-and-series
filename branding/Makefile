all: $(patsubst %.tex,%.png,$(wildcard *.tex)) $(patsubst %.tex.erb,%.png,$(wildcard *.tex.erb))

%.pdf: %.tex
	pdflatex $<

%.png: %.pdf
	mudraw -r 1200 -o $@ $<

%.tex: %.tex.erb
	ruby -e "require 'erb'; f = File.open( \"$@\", 'w' ); f.puts ERB.new( File.read( \"$<\" ), nil, '>' ).result(binding); f.close"

clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.pdf
	rm -f *.png
