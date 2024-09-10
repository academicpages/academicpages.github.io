---
title: "The future of cosmological likelihood-based inference: accelerated high-dimensional parameter estimation and model comparison"
collection: publications
permalink: /publication/2024-future
excerpt:
date: 2024-05-21
venue: 'Open Journal of Astrophysics, Vol. 7, 2024September 05, 2024 IST'
paperurl: 'https://astro.theoj.org/article/123368-the-future-of-cosmological-likelihood-based-inference-accelerated-high-dimensional-parameter-estimation-and-model-comparison'
---

We advocate for a new paradigm of cosmological likelihood-based inference, leveraging recent developments in machine learning and its underlying technology, to accelerate Bayesian inference in high-dimensional settings. Specifically, we combine (i) emulation, where a machine learning model is trained to mimic cosmological observables, e.g. CosmoPower-JAX; (ii) differentiable and probabilistic programming, e.g. JAX and NumPyro, respectively; (iii) scalable Markov chain Monte Carlo (MCMC) sampling techniques that exploit gradients, e.g. Hamiltonian Monte Carlo; and (iv) decoupled and scalable Bayesian model selection techniques that compute the Bayesian evidence purely from posterior samples, e.g. the learned harmonic mean implemented in harmonic. This paradigm allows us to carry out a complete Bayesian analysis, including both parameter estimation and model selection, in a fraction of the time of traditional approaches. First, we demonstrate the application of this paradigm on a simulated cosmic shear analysis for a Stage IV survey in 37- and 39-dimensional parameter spaces, comparing ΛCDM and a dynamical dark energy model (w0waCDM). We recover posterior contours and evidence estimates that are in excellent agreement with those computed by the traditional nested sampling approach while reducing the computational cost from 8 months on 48 CPU cores to 2 days on 12 GPUs. Second, we consider a joint analysis between three simulated next-generation surveys, each performing a 3x2pt analysis, resulting in 157- and 159-dimensional parameter spaces. Standard nested sampling techniques are simply not feasible in this high-dimensional setting, requiring a projected 12 years of compute time on 48 CPU cores; on the other hand, the proposed approach only requires 8 days of compute time on 24 GPUs. All packages used in our analyses are publicly available.


[Download paper here](https://astro.theoj.org/article/123368-the-future-of-cosmological-likelihood-based-inference-accelerated-high-dimensional-parameter-estimation-and-model-comparison)