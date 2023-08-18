---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm a doctoral researcher at UCL's Centre for Doctoral Training in Data Intensive Science working with the AstroInfo group at the Mullard Space Science Laboratory. My research focuses on developing machine learning based methods for data analysis in Astrophysics and beyond. I am enthusiastic about applying data science to solve problems in a variety of research fields and industry.


Projects
======

[harmonic](https://github.com/astro-informatics/harmonic)
------
harmonic is an open source, well tested and documented Python implementation of the learnt harmonic mean estimator (McEwen et al. 2021) to compute the marginal likelihood (Bayesian evidence), required for Bayesian model selection. My recent project focuses on introducing normalizing flows to learn the importance sampling target distribution, increasing robustness and scalability, as described [here](https://arxiv.org/abs/2307.00048).


[S2WAV: Differentiable and accelerated spherical wavelets with JAX](https://github.com/astro-informatics/s2wav) 
-------
S2WAV is a JAX package for computing wavelet transforms on the sphere and rotation group. It leverages autodiff to provide differentiable transforms, which are also deployable on modern hardware accelerators (e.g. GPUs and TPUs), and can be mapped across multiple accelerators.