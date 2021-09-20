---
title: "Know Where To Drop Your Weights: Towards Faster Uncertainty Estimation"
collection: publications
permalink: /publication/MCDropconnect
excerpt: 'You would expect the quality of uncertainty estimation to go down if you reduce the layers with MC Dropout. Our experiments say otherwise, we can get good quality uncertianty estimates with MC dropout on a subset of layers. We also save on compute this way.'
date: 2020-10-01
venue: 'ICBINB @ NeurIPS'
paperurl: 
citation: 'Kamath, Akshatha, Dwaraknath Gnaneshwar, and Matias Valdenegro-Toro. "Know Where To Drop Your Weights: Towards Faster Uncertainty Estimation." arXiv preprint arXiv:2010.14019 (2020).'
---
Estimating epistemic uncertainty of models used in low-latency applications and Out-Of-Distribution samples detection is a challenge due to the computationally demanding nature of uncertainty estimation techniques. Estimating model uncertainty using approximation techniques like Monte Carlo Dropout (MCD), DropConnect (MCDC) requires a large number of forward passes through the network, rendering them inapt for low-latency applications. We propose Select-DC which uses a subset of layers in a neural network to model epistemic uncertainty with MCDC. Through our experiments, we show a significant reduction in the GFLOPS required to model uncertainty, compared to Monte Carlo DropConnect, with marginal trade-off in performance. We perform a suite of experiments on CIFAR 10, CIFAR 100, and SVHN datasets with ResNet and VGG models. We further show how applying DropConnect to various layers in the network with different drop probabilities affects the networks performance and the entropy of the predictive distribution.

Our paper was accepted at the ICBINB NeurIPS 2020 workshop.

[Download paper here](https://arxiv.org/abs/2010.14019)
