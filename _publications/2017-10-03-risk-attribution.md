---
title: "Nonparametric Risk Attribution for Factor Models of Portfolios"
collection: publications
permalink: /publication/2017-10-03-risk-attribution
excerpt: 'We explain a two-step process for partitioning the risk of projected returns into contributions from latent factors using nonparametric regression methods.'
date: 2017-10-03
---

[Check out the slides from my talk at the UC Berkeley Risk Management Seminar here.](https://kellieotto.github.io/files/2017-10-03-risk-attribution.pdf)


Factor models are used to predict the future returns of a portfolio with known positions in many assets. These simulations yield a distribution of future returns and various measures of the risk of the portfolio. Clients would often like to identify sources of risk in their portfolios, but this is difficult when factors influence the portfolio in nonlinear ways, such as when returns are measured on a log scale and when the portfolio contains nonlinear instruments. We develop a two-step method to partition risk among factors in a portfolio which accounts for these nonlinearities: first, model the relationship between factors and portfolio returns, and second, estimate the risk contribution of each factor as the increase in portfolio risk due to increasing the factor's weight. Both of these steps can be done using nonparametric regressions, which make no assumptions about the distribution of factors or their functional relationship with the portfolio returns.