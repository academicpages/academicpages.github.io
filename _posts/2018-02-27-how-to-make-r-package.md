---
title: 'How to Make a R Package'
date: 2018-02-27
permalink: /posts/2018/02/how-to-make-r-package.md/
tags:
  - tutorial
  - R package
  - project
---

This post briefly introduces how to make R packages.
For more details, you can check this [Write R Extensions](https://cran.r-project.org/doc/manuals/R-exts.html#Creating-R-packages); but it is hard for beginnners to read through these details, so I recommend the Hadley's [R Packages book](http://r-pkgs.had.co.nz/intro.html). This is a very reader-friendly book that introduces the infrastructure of R packages and the basic processes that we make R packages.

The basic idea of making R packages is to make your codes, functions, and data more organized that can share with other collaborators and R community. The basic components of a R package include R code, package metadata, documentation, vignettes, tests, namespace, external data, compiled code, etc.

The basic packages we will use consist of devtools, roxygen2, testthat, and knitr. You should install these packages before moving forward.
