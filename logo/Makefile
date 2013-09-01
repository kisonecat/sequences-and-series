all: scene.png

scene.pov: scene.py
	python scene.py > scene.pov

scene.png: scene.pov
	povray +W300 +H170 +d scene.pov

high.png: scene.pov Makefile
	povray +W600 +H340 +Q11 +A0.0 +AM1 +R5 +Ohigh.png scene.pov
