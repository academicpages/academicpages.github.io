---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm a doctoral researcher at UCL's Centre for Doctoral Training in Data Intensive Science working with the Scientific AI (SciAI) group at the Mullard Space Science Laboratory. My research focuses on developing machine learning and statistical methods for Astrophysics and beyond.


Projects
======

harmonic
------
harmonic is an open source, well tested and documented Python implementation of the learnt harmonic mean estimator to compute the marginal likelihood (Bayesian evidence), required for Bayesian model selection. It is available on [GitHub](https://github.com/astro-informatics/harmonic) and PyPi. My recent project focuses on introducing normalizing flows to learn the importance sampling target distribution, increasing robustness and scalability, as described [here](https://arxiv.org/abs/2405.05969). The original paper introducing the learned harmonic mean is available [here](https://arxiv.org/abs/2111.12720).


S2WAV: Differentiable and accelerated spherical wavelets with JAX
-------
S2WAV is a JAX package for computing wavelet transforms on the sphere and rotation group, available on [GitHub](https://github.com/astro-informatics/s2wav) and PyPi. It leverages autodiff to provide differentiable transforms, which are also deployable on modern hardware accelerators (e.g. GPUs and TPUs), and can be mapped across multiple accelerators. The paper introducing the algorithms is available [here](https://arxiv.org/abs/2402.01282).

Project on coreference resolution at the Guardian
-------
As part of my industry group project I had the opportunity to work with the amazing Data Science team at the Guardian on a project on coreference resolution for quote attribution in Guardian articles. Our work is described in a blog post on the Guardian website: "Who said what: using machine learning to correctly attribute quotes", [here](https://www.theguardian.com/info/2023/nov/21/who-said-what-using-machine-learning-to-correctly-attribute-quotes).


Alan Turing Institute Data Study Group
-------
Intense research sprint working on detecting land cover change in the Peak District National Park using multispectral aerial photography. Our team produced change maps using statistical and machine learning methods, explored the use of Siamese networks, autoencoders and introducing synthetic change to train supervised models for the task. Results from the project are described in a report available [here](https://www.turing.ac.uk/news/publications/data-study-group-final-report-peak-district-national-park-authority).