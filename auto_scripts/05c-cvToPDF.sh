# Require latexmk, texlive-xetex

CVDIR=cv_tex
CVROOT=Sledzieski-Samuel-CV

cd "$CVDIR"
latexmk -xelatex "$CVROOT".tex
echo "Removing auxiliary files."
rm *.aux
rm *.fdb_latexmk
rm *.fls
rm *.log
rm *.out
echo "Moving PDF to files directory."
mv "$CVROOT".pdf ../../files
cd ..
