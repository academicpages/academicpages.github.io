---
title: "A Fast Time-Stepping Strategy for Dynamical Systems Equipped with a Surrogate Model"
collection: publications
permalink: /publication/Surrogate-MR
excerpt: 'Multirate time integration, Surrogate model, General-structure additive Runge-Kutta methods, Reduced-order modeling, Machine learning'
date: '2022-01-01'
venue: SIAM Journal on Scientific Computing
paperurl: 'https://arxiv.org/abs/2011.03688'
---
Simulation of complex dynamical systems arising in many applications is computationally challenging due to their size and complexity. Model order reduction, machine learning, and other types of surrogate modeling techniques offer cheaper and simpler ways to describe the dynamics of these systems, but are inexact and introduce additional approximation errors. In order to overcome the computational difficulties of the full complex models, on one hand, and the limitations of surrogate models, on the other, this work proposes a new accelerated time-stepping strategy that combines information from both. This approach is based on the multirate infinitesimal general-structure additive Runge-Kutta (MRI-GARK) framework. The inexpensive surrogate model is integrated with a small timestep to guide the solution trajectory, and the full model is treated with a large timestep to occasionally correct for the surrogate model error and ensure convergence. We provide a theoretical error analysis, and several numerical experiments, to show that this approach can be significantly more efficient than using only the full or only the surrogate model for the integration.

[Preprint](https://arxiv.org/abs/2011.03688) / [Paper](https://epubs.siam.org/doi/abs/10.1137/20M1386281)
