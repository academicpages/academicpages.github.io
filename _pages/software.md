---
permalink: /software/
title: "Software"
---

As one of my two research agendas involves improving the tools we use to study peace and conflict, a good deal of my time is spent using statistical software. Below you'll find software for working with estimates from Bayesian models and some code that I've written to save time on tasks that I find myself doing over and over again.

## BayesPostEst

I am a developer of the [BayesPostEst](https://cran.r-project.org/package=BayesPostEst) R package for generating postestimation quantities of interest from Bayesian models. The package contains functions for producing regression tables, plotting predicted probabilities, calculating first differences, creating coefficient plots, and many other quantities. You can view the [Journal of Open Source Software](https://joss.theoj.org/) article for the package [here](https://doi.org/10.21105/joss.01722).

<p align="center">
  <img src="/images/software/table.png" height="225px" width="225px" />
  <img src="/images/software/coefplot.png" height="250px" width="250px" />
  <img src="/images/software/margeff.png" height="250px" width="250px" />
</p>

To install the latest release on CRAN:

```r
install.packages("BayesPostEst")
```

The latest [development version](https://github.com/ShanaScogin/BayesPostEst) on GitHub can be installed with:

```r
library(remotes)
install_github("ShanaScogin/BayesPostEst")
```

## RWmisc

I've collected convenience functions that I've written to address issues I frequently confront in my work into a personal R package called [RWmisc](https://github.com/jayrobwilliams/RWmisc). It includes:

- Managing multiple different projections for cross-national spatial data
- Correcting for overlapping polygons when aggregating raster data to polygons
- My custom minimal ggplot2 theme

![](/images/software/spatial_weighting.png)

You can install the current version with :

```r
library(remotes)
install_github("jayrobwilliams/RWmisc")
```

## Other Resources

I also have a number of other software resources focused on making computation and academic life easier:

- [The template](https://github.com/jayrobwilliams/JobMarket) I use for my academic job market materials
    - Fill in school/position information in one file and it populates to all statements
    - Generate summary statistics from teaching evaluations and integrate into statements
    - Combine multiple teaching evaluations into a single portfolio document
    - Do all of this programmatically with GNU Make!
- [The template](https://github.com/jayrobwilliams/UNC-Dissertation-Template) I used for my dissertation
    - This satisfied the formatting requirements at UNC in 2019
    - Some tweaking likely required to use at another institution or in the future
- [Scripts](https://github.com/jayrobwilliams/Teaching) that I use to save time on various teaching-related tasks like grading
- [Functions](https://github.com/jayrobwilliams/ComputerVision) for extracting still frames from videos and information from images in Python using OpenCV
- [Compiling OpenCV](/files/html/OpenCV_Install.html) from source for Anaconda virtual environments instead of Homebrew ones or system Python installations