FILES=$(wildcard *.tex) mooculus.sty

all: textbook.pdf

textbook.pdf: $(FILES)
	rm -f answers.tex
	touch answers.tex
	pdflatex textbook.tex
	cp textbook.ans answers.tex
	makeindex textbook
	pdflatex textbook.tex
	pdflatex textbook.tex
#	mv -f textbook.pdf textbook-undistilled.pdf
#	gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=textbook.pdf textbook-undistilled.pdf

textbook-print.pdf: $(FILES)
	rm -f answers.tex
	touch answers.tex
	pdflatex -jobname textbook-print textbook.tex
	cp textbook.ans answers.tex
	makeindex textbook-print
	pdflatex -jobname textbook-print textbook.tex
	pdflatex -jobname textbook-print textbook.tex
#	mv -f textbook-print.pdf textbook-print-undistilled.pdf
#	gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=textbook-print.pdf textbook-print-undistilled.pdf

textbook.png: textbook.pdf
	mudraw -r 144 -o textbook.png textbook.pdf 1

install: textbook.pdf textbook-print.pdf textbook.png
	mv -f textbook-print.pdf sequences-and-series-print.pdf
	mv -f textbook.pdf sequences-and-series.pdf
	mv -f textbook.png sequences-and-series.png
	./upload.sh sequences-and-series.pdf
	./upload.sh sequences-and-series.png
	./upload.sh sequences-and-series-print.pdf

clean:
	rm -f *.swp
	rm -f *.ans
	rm -f *.aux
	rm -f *.idx
	rm -f *.lof
	rm -f *.lot
	rm -f *.out
	rm -f *.toc
	rm -f *.log
	rm -f *.pdf
