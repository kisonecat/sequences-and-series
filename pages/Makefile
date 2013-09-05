PAGES=week1.html week2.html week3.html week4.html week5.html week6.html syllabus.html GradingandLogistics.html AboutTheInstructor.html textbook.html officehours.html GettingStarted.html

all: $(PAGES)

syllabus.html: syllabus.html.erb week1.html week2.html week3.html week4.html week5.html week6.html course.rb
	ruby -e "require 'erb'; f = File.open( \"$@\", 'w' ); f.puts ERB.new( File.read( \"$<\" ), nil, '>' ).result(binding); f.close"

%.html: %.html.erb course.rb
	ruby -e "require 'erb'; f = File.open( \"$@\", 'w' ); f.puts ERB.new( File.read( \"$<\" ), nil, '>' ).result(binding); f.close"

upload: $(PAGES)
	./upload-page.sh syllabus
	./upload-page.sh week1
	./upload-page.sh week2
	./upload-page.sh week3
	./upload-page.sh week4
	./upload-page.sh week5
	./upload-page.sh week6
	./upload-page.sh GradingandLogistics
	./upload-page.sh AboutTheInstructor
	./upload-page.sh textbook
	./upload-page.sh officehours
	./upload-page.sh GettingStarted

clean:
	rm -f AboutTheInstructor.html GradingandLogistics.html syllabus.html
	rm -f week1.html week2.html week3.html week4.html week5.html week6.html 
	rm -f textbook.html
