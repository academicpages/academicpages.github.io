
library(tools)

tinytex::install_tinytex()

tinytex::parse_install("CV.log")

texi2pdf("CV.tex")
