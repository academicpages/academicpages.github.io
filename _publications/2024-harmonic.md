---
title: "Learned harmonic mean estimation of the Bayesian evidence with normalizing flows"
collection: publications
permalink: /publication/2024
excerpt: 'We present the learned harmonic mean estimator with normalizing flows - a robust, scalable and flexible estimator of the Bayesian evidence for model comparison. Since the estimator is agnostic to sampling strategy and simply requires posterior samples, it can be applied to compute the evidence using any Markov chain Monte Carlo (MCMC) sampling technique, including saved down MCMC chains, or any variational inference approach. The learned harmonic mean estimator was recently introduced, where machine learning techniques were developed to learn a suitable internal importance sampling target distribution to solve the issue of exploding variance of the original harmonic mean estimator. In this article we present the use of normalizing flows as the internal machine learning technique within the learned harmonic mean estimator. Normalizing flows can be elegantly coupled with the learned harmonic mean to provide an approach that is more robust, flexible and scalable than the machine learning models considered previously. We perform a series of numerical experiments, applying our method to benchmark problems and to a cosmological example in up to 21 dimensions. We find the learned harmonic mean estimator is in agreement with ground truth values and nested sampling estimates. The open-source harmonic Python package implementing the learned harmonic mean, now with normalizing flows included, is publicly available.'
date: 2024-05-09
venue:
paperurl: 'https://arxiv.org/abs/2405.05969'
---

[Download paper here](https://arxiv.org/pdf/2405.05969)