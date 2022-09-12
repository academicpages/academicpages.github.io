---
title: "Bayesian MCMC Probit"
excerpt: "Markov Chain Monte Carlo Sampling from a Probit GLM, December 2021 <br/><img src='/images/Triple_dim_acc_rej_123.png'>"
collection: portfolio
---
To access the report only, please click [here](http://simonegiancola09.github.io/files/bayesian_MCMC_analysis.pdf)


To access the repository, please click [here](https://github.com/simonegiancola09/probit_bayesian_MCMC)


Implementation & theory of a Metropolis Hastings and a Gibbs Algorithm to estimate the parameters of a Probit linear model on simulated and real data. 

### Abstract
Markov Chain Monte Carlo sampling methods are efficient procedures to generate distributions
sequentially. Our work proposes two ways to estimate the parameters of a Generalized Linear Model
of a binary target variable linked with a probit function to the covariates. The former is a Metropolis
Hastings with a Random Walk proposal algorithm. The latter method is inspired from Albert and Chib (1983), using an
instrumental variable Gibbs algorithm framework. Once full conditional closed forms of the parameter
are retrievable, we can sample from them. The procedure is carried out in blocks, to increase
efficiency. After a theoretical introduction to the techniques, we explicitly derive characterizing features
of both and provide a code to present results. Given that the distribution needs additionally to
come with ergodic properties, we construct a collection of diagnostic checks to ensure this through
plots. A randomly generated dataset and a real dataset are used to graphically derive stable
parameters’ specifications. The two methods are then compared in terms of performance and
appearance of the resulting chains.

### Authors
* Chiavarino Federico
* Giancola Simone 
* Liscai Dario
* Marchetti Simone



