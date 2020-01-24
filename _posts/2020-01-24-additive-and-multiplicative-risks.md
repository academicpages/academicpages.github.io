---
title: Additive and multiplicative risks for public health
date: 2020-01-24
permalink: /posts/2020/1/additive-and-multiplicative-risks
tags:
---

I saw [this Comment](https://doi.org/10.1016/s2214-109x(19)30553-4) on [a
paper](https://doi.org/10.1016/S2214-109X(19)30541-8) in *The Lancet Global
Health* and thought is was a lovely example of why logistic regressions
can be confusing.

The paper is a study of children with malnutrition and diarrhea. These two
conditions are a [vicious cycle](https://www.ncbi.nlm.nih.gov/pubmed/1632474):
malnutrition weakens the immune system, which increases the risk of diarrhea
caused by infections, which reduces children's appetites and abilities to feed,
leading to further malnutrition. This cycle is an important problem in global
health.

In one of its analyses, the paper looks at the risk of death as a function of
nutrition status (malnourished vs. better-nourished) and pathogen (infected
with *Cryptosporidium* vs. uninfected or infected with some other pathogen).
The paper raises the question: is
[*Cryptosporidium*](https://www.who.int/bulletin/volumes/91/4/13-119990/en/), a
parasite that causes diarrhea, more dangerous for malnourished children than
better-nourished children? In other words, will malnourished children get a
greater benefit from some public health intervention that reduces
*Cryptosporidium* infections, compared to better-nourished children?

Here are some of the relevant data discussed in the Comment:

| Nutrition        | Infection         | Deaths | Total | Crude risk
|------------------|-------------------|--------|-------------------
| Malnourished     | *Cryptosporidium* | 22     | 196   | 11.2%
|                  | Other             | 70     | 875   | 8.0%
| Better-nourished | *Cryptosporidium* | 11     | 686   | 1.6%
|                  | Other             | 41     | 5697  | 0.7%

If you simply compare the crude risks among malnourished and among
better-nourished children, it appears that *Cryptosporidium* is more
problematic for malnourished children: the increase in the risk of death among
malnourished children is 3.2% ($11.2 - 8.0$) compared to 0.9% ($1.6 - 0.7$)
among the better-nourished children.

But these are not enormous effects, so I would want to do a regression to see
whether these results actually support this conclusion. My first instinct is to
do a logistic regression, predicting each child's outcome (death or survival)
from their nutrition status, infection status, and an *interaction term*. The
interaction term will tell us whether being malnourished and having
*Cryptosporidium* is worse than you would expect based on the two increases in
risk from being malnourished and from having a *Cryptosporidium* infection.

First, I'll put the data into R using the handy
[*tribble*](https://tibble.tidyverse.org/reference/tribble.html) function:
```r
library(tidyverse)

count_data <- tribble(
  ~malnourished, ~crypto, ~deaths, ~total,
  TRUE, TRUE, 22, 196,
  TRUE, FALSE, 70, 875,
  FALSE, TRUE, 11, 686,
  FALSE, FALSE, 41, 5697
)

# # A tibble: 4 x 4
#   malnourished crypto deaths total
#   <lgl>        <lgl>   <dbl> <dbl>
# 1 TRUE         TRUE       22   196
# 2 TRUE         FALSE      70   875
# 3 FALSE        TRUE       11   686
# 4 FALSE        FALSE      41  5697
```

Now I want to take this count data and "uncount" it,
so that each row represents one child:
```r
data <- count_data %>%
  mutate(death = map2(deaths, total, ~ c(rep(1, .x), rep(0, .y - .x)))) %>%
  select(malnourished, crypto, death) %>%
  unnest()

# # A tibble: 7,454 x 3
#    malnourished crypto death
#    <lgl>        <lgl>  <dbl>
#  1 TRUE         TRUE       1
#  2 TRUE         TRUE       1
#  3 TRUE         TRUE       1
#  4 TRUE         TRUE       1
#  5 TRUE         TRUE       1
#  6 TRUE         TRUE       1
#  7 TRUE         TRUE       1
#  8 TRUE         TRUE       1
#  9 TRUE         TRUE       1
# 10 TRUE         TRUE       1
# # … with 7,444 more rows
```
(There's a tidyverse
[*uncount*](https://tidyr.tidyverse.org/reference/uncount.html) function, but
it doesn't do exactly what I want, since I have two pieces of information per
row.)

I'll quickly check that I did the transformation right by looking at the crude risks:
```r
data %>%
  group_by(malnourished, crypto) %>%
  summarize(crude_risk = scales::percent(mean(death)))

# # A tibble: 4 x 3
# # Groups:   malnourished [2]
#   malnourished crypto crude_risk
#   <lgl>        <lgl>  <chr>
# 1 FALSE        FALSE  0.720%
# 2 FALSE        TRUE   1.60%
# 3 TRUE         FALSE  8.00%
# 4 TRUE         TRUE   11.2%
```

And then let's run the regression:
```r
summary(glm(formula = death ~ malnourished * crypto, family = "binomial", data = data))

# Call:
# glm(formula = death ~ malnourished * crypto, family = "binomial",
#     data = data)
#
# Coefficients:
#                             Estimate Std. Error z value Pr(>|z|)
# (Intercept)                  -4.9269     0.1567 -31.437   <2e-16 ***
# malnourishedTRUE              2.4846     0.2002  12.409   <2e-16 ***
# cryptoTRUE                    0.8101     0.3420   2.369   0.0178 *
# malnourishedTRUE:cryptoTRUE  -0.4357     0.4286  -1.017   0.3093
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```
So, as expected, being malnourished increases your risk of death (that's the
2.4 estimate, corresponding to an odds ratio of $e^{2.4} \approx 11$), and
having a *Cryptosporidium* infection does too (estimate of 0.8 yields an odds
ratio of $e^{0.8} \approx 2.2$).

If you were a skeptic, you might also not be surprised that the interaction
term (`malnourishedTRUE:cryptoTRUE`) is not statistically significant ($p =
0.3$). But even if you were a skeptic, you might be surprised that the
interaction term is *negative*, suggesting that *Cryptosporidium* infection
presents *less* of an increase in risk for malnourished children when compared
to better-nourished children.

And indeed this is true, depending on what your mean by "less" or "more" risk.
The trick is that logistic regression works on a *multiplicative*, rather than
additive scale, and the *multiplicative* increase in risk of death from having
*Cryptosporidium* is less for malnourished children. For better-nourished
children, the additive increase in risk was only 0.9 percentage points, but
this was on a baseline risk of 0.7%: *Cryptosporidium* infection more than
doubles their risk of death. For malnourished children, on the other hand, the
additive increase in risk was 3.2 percentage points, which is certainly bigger
than 0.9 percentage points, but it's less than half of the baseline risk of
8.0%.

For public health, the additive risk can more useful, since it let's you say:
"Say I could completely eliminate *Cryptosporidium* infections either in a
population of *N* malnourished children or in a population of *N*
better-nourished children. Where could I save more lives?" This is more
interesting than the multiplicative reasoning, which asks, "Where could I lead
to the greatest *fractional* reduction in the number of deaths?" You'd save
more lives by preventing infection among the malnourished children (assuming
the observed effect is causal).

Although it's problematic, I'll show the results of a binomial-linear
regression, where the risks add rather than multiply:
```r
summary(glm(death ~ malnourished * crypto, family = binomial(link = "identity"), data = data))

# Call:
# glm(formula = death ~ malnourished * crypto, family = binomial(link = "identity"),
#     data = data)
#
# Deviance Residuals:
#     Min       1Q   Median       3Q      Max
# -0.4880  -0.1202  -0.1202  -0.1202   3.1414
#
# Coefficients:
#                             Estimate Std. Error z value Pr(>|z|)
# (Intercept)                 0.007197   0.001120   6.426 1.31e-10 ***
# malnourishedTRUE            0.072803   0.009240   7.880 3.29e-15 ***
# cryptoTRUE                  0.008838   0.004925   1.795   0.0727 .
# malnourishedTRUE:cryptoTRUE 0.023407   0.024835   0.942   0.3459
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```
As expected, the interaction term is now positive (although still not significant).
