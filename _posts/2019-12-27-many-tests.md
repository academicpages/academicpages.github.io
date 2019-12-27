---
title: "Using R for many statistical tests"
date: 2019-12-27
permalink: /posts/2019/12/tests
mathjax: true
---

*This post is in some senses a remix of [a previous post](/posts/2018/12/purrr)
about using [purrr](https://purrr.tidyverse.org/) for analysis in R.*

As part of a [scientific project](https://elifesciences.org/articles/39435), I
was asking whether the distribution of antibiotic use is important to levels of
antibiotic resistance. Say you have two populations of people, each taking the
same average, per capita number of antibiotics, but in one population,
consumption is evenly spread, while in the other it is concentrated in a few
people. Do we expect one to have more resistance than the other?

To answer this, we looked at antibiotic use and resistance across US states in
72 pathogen/antibiotic combinations (e.g., *S. pneumoniae* resistance to
penicillin antibiotics). We partitioned antibiotic use into *first use* and
*repeat use*. One person's first use for an antibiotic a calendar year is
either 0, if they did not take that antibiotic, or 1, if they took that
antibiotic at least once. Repeat use is 0 if they never took the antibiotic, 0
if they took it once, 1 if they took it twice, 2 if they took it 3 times, etc.

The base, or "null" model, is that first and repeat use have the same
association with resistance:

$$
A_i = \mu + \beta_\mathrm{total} (F_i + R_i) + \varepsilon_i,
$$

where $A_i$ is <u>A</u>ntibiotic resistance in the $i$-th state, $\mu$ is the
grand mean, $F_i$ is first use, $R_i$ is repeat use, and $\varepsilon$
is an error term.

The "alternative" model is that first and repeat use have different
associations with resistance:

$$
A_i = \mu + \beta_F F_i + \beta_R R_i + \varepsilon_i
$$

We want to compare these two models, using a [likelihood ratio
test](https://en.wikipedia.org/wiki/Likelihood-ratio_test) to see if the
improved fit that comes from having two separate predictors ($F_i$ and $R_i$)
is evidence that $\beta_F \neq \beta_R$, that is, that we should accept that we
have reason to believe the alternative model better reflects the underlying
reality than the base model.

First, I download the relevant data from the supplemental data for the paper:
```r
library(tidyverse)
library(lmtest)

use <- read_tsv("https://elifesciences.org/download/aHR0cHM6Ly9jZG4uZWxpZmVzY2llbmNlcy5vcmcvYXJ0aWNsZXMvMzk0MzUvZWxpZmUtMzk0MzUtZmlnMy1kYXRhMS12Mi50ZHM=/elife-39435-fig3-data1-v2.tds?_hash=KZsZkTZ14Oh8yKruvuxMT1Ja%2Fy0bojoI24mne8gvd9Q%3D")
res <- read_tsv("https://elifesciences.org/download/aHR0cHM6Ly9jZG4uZWxpZmVzY2llbmNlcy5vcmcvYXJ0aWNsZXMvMzk0MzUvZWxpZmUtMzk0MzUtZmlnMy1kYXRhMi12Mi50ZHM=/elife-39435-fig3-data2-v2.tds?_hash=IMcMpKgsfLWKByV6%2B5zVYDoIMFgE2VNWV43ZR5xME8s%3D")
```

Then, I select only the relevant data (the main dataset used in the paper) and
join the use and resistance data together:
```r
data <- use %>%
  filter(source == "marketscan", data == "main") %>%
  inner_join(res, by = c("drug_group", "state_id")) %>%
  select(
    state_id, bug = pathogen, drug = drug_group,
    first_use, repeat_use, res = proportion_nonsusceptible
  ) %>%
  mutate(bug_drug = interaction(bug, drug))
```

The first way to check if $\beta_F \neq \beta_R$ is to run a global
model, incorporating all 72 pathogen/antibiotic combinations at once:
```r
null_model <- lm(res ~ bug_drug * I(first_use + repeat_use), data = data)
alt_model <- lm(res ~ bug_drug * (first_use + repeat_use), data = data)
lrtest(null_model, alt_model)

# Likelihood ratio test
#
# Model 1: res ~ bug_drug * I(first_use + repeat_use)
# Model 2: res ~ bug_drug * (first_use + repeat_use)
#   #Df LogLik Df  Chisq Pr(>Chisq)
# 1 145 2460.1
# 2 217 2482.1 72 44.025     0.9962
```
The result $p = 0.996$ tells you that the data appear to be much better
explained by the simpler, "null" model with $\beta_F = \beta_R$, and
therefore first and repeat use don't have different impacts on resistance.

But is it the case that we have good evidence for some particular
pathogen/antibiotic combinations?  To run separate models on each combination,
we can use [tidyr](https://tidyr.tidyverse.org/)'s `nest` function with purrr's
`map` functions:
```r
results <- data %>%
  nest(-bug_drug) %>%
  mutate(
    null_model = map(data, ~ lm(res ~ I(first_use + repeat_use), data = .)),
    alt_model = map(data, ~ lm(res ~ first_use + repeat_use, data = .)),
    test = map2(null_model, alt_model, lrtest),
    p = map_dbl(test, ~ .$`Pr(>Chisq)`[2])
  )
```

The `nest` command makes a tibble (aka "data frame") that has a column named
`data` that is, itself, a bunch of tibbles:
```r
data %>% nest(-bug_drug)

# A tibble: 72 x 2
#   bug_drug                  data
#   <fct>                     <list>
# 1 C. freundii.beta_lactam   <tibble [37 × 6]>
# 2 CoNS.beta_lactam          <tibble [42 × 6]>
# 3 E. cloacae.beta_lactam    <tibble [41 × 6]>
# 4 E. coli.beta_lactam       <tibble [44 × 6]>
# 5 E. faecalis.beta_lactam   <tibble [39 × 6]>
# 6 E. faecium.beta_lactam    <tibble [38 × 6]>
# 7 K. pneumoniae.beta_lactam <tibble [43 × 6]>
# 8 P. aeruginosa.beta_lactam <tibble [44 × 6]>
# 9 P. mirabilis.beta_lactam  <tibble [42 × 6]>
#10 S. aureus.beta_lactam     <tibble [43 × 6]>
# … with 62 more rows
```

For example, the first row, showing $\beta$-lactam resistance among *C.
freundii*, has a `data` fields that is a tibble with 37 rows and 6 columns:
```r
data %>% nest(-bug_drug) %>% pull(data) %>% first()

# A tibble: 37 x 6
#    state_id bug         drug        first_use repeat_use    res
#    <chr>    <chr>       <chr>           <dbl>      <dbl>  <dbl>
#  1 stateBFU C. freundii beta_lactam    0.106      0.0398 0.540
#  2 stateCCZ C. freundii beta_lactam    0.189      0.0885 0.483
#  3 stateCUX C. freundii beta_lactam    0.157      0.0705 0.2
#  4 stateCWD C. freundii beta_lactam    0.145      0.0609 0.17
#  5 stateCYL C. freundii beta_lactam    0.188      0.0837 0.509
#  6 stateELN C. freundii beta_lactam    0.0728     0.0260 0.0248
#  7 stateEPB C. freundii beta_lactam    0.177      0.0710 0.543
#  8 stateERZ C. freundii beta_lactam    0.144      0.0632 0.584
#  9 stateEVG C. freundii beta_lactam    0.137      0.0563 0
# 10 stateGKW C. freundii beta_lactam    0.162      0.0678 0.330
# … with 27 more rows
```

The `map` functions makes new columns that are linear regression objects. It's
worth noting the nifty feature in the formulas:

`lm(res ~ I(first_use + repeat_use), data = .)`
means $A_i = \beta_\mathrm{total} (F_i + R_i) + \varepsilon_i$

`r lm(res ~ first_use + repeat_use, data = .)`
means $A_i = \beta_F F_i + \beta_R R_i + \varepsilon_i$

Then we want to filter the rows based on the $p$-values:
```r
results %>%
  count(p < 0.05, p.adjust(p, "BH") < 0.05)

# A tibble: 3 x 3
#   `p < 0.05` `p.adjust(p, "BH") < 0.05`     n
#   <lgl>      <lgl>                      <int>
# 1 FALSE      FALSE                         65
# 2 TRUE       FALSE                          6
# 3 TRUE       TRUE                           1
```
So in 7 pathogen/antibiotic combinations we have $p < 0.05$, but only 1 do we
have statistical evidence after multiple hypothesis correction, and in this
case, the results are not very compelling:
```r
# get the use/resistance data for the significant bug/drug
sig_result <- results %>%
  filter(p.adjust(p, "BH") < 0.05) %>%
  as.list() %>%
  flatten()

sig_result$data %>%
  # "gather" the first and repeat use for plotting
  gather("use_type", "use", c("first_use", "repeat_use")) %>%
  ggplot(aes(use, res)) +
  # show the first/resistance and repeat/resistance relationships
  facet_wrap(~ use_type, scales = "free_x") +
  # show linear best first lines
  stat_smooth(method = "lm") +
  geom_point()
```

<img href="/files/images/2019-12-first-repeat.png" width="50%">

So when looking at first and repeat resistance on their own, we see no
relationship with first use, and a potentially *negative* association with
repeat use. The coefficients that come out of the alternative model are a bit
crazy:

```r
sig_result$null_model

# Call:
# lm(formula = res ~ I(first_use + repeat_use), data = .)
#
# Coefficients:
#               (Intercept)  I(first_use + repeat_use)
#                    0.2267                    -1.7958

sig_result$alt_model

# Call:
# lm(formula = res ~ first_use + repeat_use, data = .)
#
# Coefficients:
# (Intercept)    first_use   repeat_use
#      0.1637      38.7258     -86.7541
```

So while the null model gives a slope of $-1.8$, the alternative model gives
enormous slopes: $+38$ and $-87$! It turns out that this is a problem of
collinearity: first use and repeat use are highly correlated, which leads to
weird predictions in linear models:
```r
with(sig_result$data, cor.test(first_use, repeat_use))

#     Pearson's product-moment correlation
#
# data:  first_use and repeat_use
# t = 11.711, df = 33, p-value = 2.691e-13
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.8055830 0.9475536
# sample estimates:
#       cor
# 0.8978064
```
So we are left with the conclusion that we don't have strong evidence to
support the idea that $\beta_F \neq \beta_R$ and that the distribution of use
is important, when sliced and diced in this way.
