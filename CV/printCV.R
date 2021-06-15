
library(tools)

tinytex::install_tinytex()

tinytex::parse_install("CV_JPL.log")

texi2pdf("CV.tex")
