#!/usr/bin/env Rscript

library(tidyverse)
library(pwr)

# Make a figure showing how sigma, delta_mu, and Phi(delta_mu/sigma)
# relate to one another. Show visually the 2 proportions. Then show
# how powers of the 2 tests changes with changing d.

f <- function(d) {
  pwr.2p.test(h = ES.h(pnorm(d / 2), 1 - pnorm(d / 2)), power = 0.8)$n
}

g <- function(d) {
  pwr.t.test(d = d, power = 0.8)$n
}

tibble(d = c(1e-2, 1e-1, 1.0, 2.0, 3.0, 4.0)) %>%
  mutate(
    n_t = map_dbl(d, g),
    n_prop = map_dbl(d, f),
    fold = n_prop / n_t 
  )
