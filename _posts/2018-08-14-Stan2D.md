---
title: 'Using PyStan to fit a model with X and Y errors'
date: 2018-08-14
permalink: /posts/2018/08/Stan-2D/
tags:
  - notebooks
  - bayesian inference
---

After writing my first [post](https://nikhil-sarin.github.io/posts/2018/08/2derrors/). I was recommended Stan to fit more complicated models to data with X and Y uncertainties. Stan and Hamiltonian monte carlo is naturally suited to problems like this as the simplest way to treat X errors is to sample over the true x values and then marginalise. This adds a dimension for each data point which breaks most samplers, expect HMC. This example is for a simple problem like in the first post, but instead using Stan to sample.

Jupyter notebook to run through the problem [here](https://github.com/nikhil-sarin/2Derrors/blob/master/Using_stan_to_sample.ipynb)
======

======

------
