#!/usr/bin/env Rscript --vanilla

# Burnashev and Zigangirov
# https://people.orie.cornell.edu/shane/theses/ThesisRolfWaeber.pdf
# Plot shows how the posterior pdf shrinks

library(tidyverse)

pc <- 0.75
max_conf <- 0.99
n_bin <- 1000

g <- function(x, n = 1000) rbinom(1, n, 1 - x) / n - 0.8

stochastic_bisection <- function(f, interval, pc, n_bin, min_conf) {
  qc <- 1 - pc

  # set up a series of breakpoints at the endpoints and between the bins
  break_x <- seq(interval[1], interval[2], length.out = n_bin + 1)
  # set up the bins between the breakpoints
  bin_x <- zoo::rollmean(break_x, 2)

  # start with a flat prior
  pdf <- rep(1 / n_bin, n_bin)

  i <- 1
  while (max(pdf) < min_conf) {
    # get the median point of the PDF
    cdf <- c(0, cumsum(pdf))
    stopifnot(all.equal(last(cdf), 1))
    median_i <- abs(cdf - 0.5) %>%
      {  match(min(.), .) }

    xn <- break_x[median_i]
    yn <- f(xn)

    if (yn >= 0) {
      pdf[bin_x >= xn] <- pc * pdf[bin_x >= xn]
      pdf[bin_x < xn] <-  qc * pdf[bin_x < xn]
    } else {
      pdf[bin_x >= xn] <- qc * pdf[bin_x >= xn]
      pdf[bin_x < xn] <-  pc * pdf[bin_x < xn]
    }

    # renormalize
    pdf <- pdf / sum(pdf)

    i <- i + 1
  }

  list(x = xn, conf = max(pdf), n_iter = i)
}

stochastic_bisection(g, c(0, 1), 0.75, 1e3, 0.99)
