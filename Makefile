all: clean pdf latexclean build

clean: latexclean
	rm -rf _site

pdf:
	xelatex -output-directory=latex latex/main.tex -
	xelatex -output-directory=latex latex/main.tex -
	cp latex/main.pdf assets/files/Sledzieski_Samuel_CV.pdf

latexclean:
	rm -rf latex/*.aux latex/*.log latex/*.out

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve -l -H localhost
