---
title: "Learning a Mixture of Gaussians via Mixed Integer Optimization"
collection: publications
permalink: /publication/GMMs-MIO
excerpt: 'We develop a discrete optimization formulation to learn a Multivariate Gaussian mixture model (GMM) given access to n samples that are believed to have come from a mixture of multiple subpopulations. The formulation optimally recovers the parameters of a GMM by minimizing a discrepancy measure (either the Kolmogorov–Smirnov or the Total Variation distance) between the empirical distribution function and the distribution function of the GMM whenever the mixture component weights are known.'
date: 2018-04-01
venue: 'INFORMS Journal on Optimization'
paperurl: 'https://doi.org/10.1287/ijoo.2018.0009'
citation: 'Your Name, You. (2018). &quot;Paper Title Number 3.&quot; <i>Journal 1</i>. 1(3).'
coauthors: Dimitris Bertsimas and Rahul Mazumder.
paperstatus: INFORMS Journal on Optimization
---
We consider the problem of estimating the parameters of a multivariate Gaussian mixture model (GMM) given access to n samples that are believed to have come from a mixture of multiple subpopulations. State-of-the-art algorithms used to recover these parameters use heuristics to either maximize the log-likelihood of the sample or try to fit first few moments of the GMM to the sample moments. In contrast, we present here a novel Mixed-Integer Optimization (MIO) formulation that optimally recovers the parameters of the GMM by minimizing a discrepancy measure (either the Kolmogorov–Smirnov or the Total Variation distance) between the empirical distribution function and the distribution function of the GMM whenever the mixture component weights are known. We also present an algorithm for multidimensional data that optimally recovers corresponding means and covariance matrices. We show that the MIO approaches are practically solvable for data sets with n in the tens of thousands in minutes and achieve an average improvement of 60%–70% and 50%–60% on mean absolute percentage error in estimating the means and the covariance matrices, respectively, over the expectation–maximization (EM) algorithm independent of the sample size n. As the separation of the Gaussians decreases and, correspondingly, the problem becomes more difficult, the edge in performance in favor of the MIO methods widens. Finally, we also show that the MIO methods outperform the EM algorithm with an average improvement of 4%–5% on the out-of-sample accuracy for real-world data sets.
