---
title: "Local Stability and Region of Attraction Analysis for Neural Network Feedback Systems under Positivity Constraints"
collection: publications
category: conferences
permalink: /publication/2025-12-12-cdc-paper
excerpt: "Region of attraction estimates for systems with neural network controllers, using localized Aizerman conditions and tight local sector bounds."
date: 2025-12-12
authors: 'H. Montazeri Hedesh, M. K. Wafi, M. Siami'
venue: 'IEEE Conference on Decision and Control (CDC)'
paperurl: 'https://doi.org/10.1109/CDC57313.2025.11312171'
ieeeurl: 'https://ieeexplore.ieee.org/document/11312171'
arxivurl: 'https://arxiv.org/abs/2505.22889'
codeurl: 'https://github.com/hmon91/Local-stability-of-NN-controlled-systems'
libraries:
  - name: nnsector
    url: 'https://github.com/hmon91/nnsector'
  - name: nnstab
    url: 'https://github.com/hmon91/nnstab'
citation: 'H. Montazeri Hedesh, M. K. Wafi, and M. Siami. (2025). "Local Stability and Region of Attraction Analysis for Neural Network Feedback Systems under Positivity Constraints," <i>2025 IEEE 64th Conference on Decision and Control</i>, Rio de Janeiro, Brazil, pp. 1142-1149.'
---

{% include publication-meta.html post=page %}

## In short

How large is the set of starting states from which a system with a neural network controller still settles at its equilibrium (its region of attraction)? For positive Lur'e systems, the paper gives two ways to estimate it: a Lyapunov method with a linear matrix inequality (LMI) that grows invariant sets, and tight local sector bounds for the network, computed layer by layer and used in a localized Aizerman test. In the examples, both give larger regions and scale better than methods based on integral quadratic constraints (IQC).

**Topics:** region of attraction, local stability, neural network verification, local sector bounds, linear relaxations, LMI, IQC.

## Abstract

We study the local stability of nonlinear systems in the Lur'e form with static nonlinear feedback realized by feedforward neural networks (FFNNs). By leveraging positivity system constraints, we employ a localized variant of the Aizerman conjecture, which provides sufficient conditions for exponential stability of trajectories confined to a compact set. Using this foundation, we develop two distinct methods for estimating the Region of Attraction (ROA): (i) a less conservative Lyapunov-based approach that constructs invariant sublevel sets of a quadratic function satisfying a linear matrix inequality (LMI), and (ii) a novel technique for computing tight local sector bounds for FFNNs via layer-wise propagation of linear relaxations. These bounds are integrated into the localized Aizerman framework to certify local exponential stability. Numerical results demonstrate substantial improvements over existing integral quadratic constraint-based approaches in both ROA size and scalability.

## BibTeX

{% raw %}
```bibtex
@inproceedings{montazerihedesh2025local,
  author    = {Montazeri Hedesh, Hamidreza and Wafi, Moh Kamalul and Siami, Milad},
  title     = {Local Stability and Region of Attraction Analysis for Neural Network Feedback Systems under Positivity Constraints},
  booktitle = {2025 IEEE 64th Conference on Decision and Control (CDC)},
  address   = {Rio de Janeiro, Brazil},
  pages     = {1142--1149},
  year      = {2025},
  doi       = {10.1109/CDC57313.2025.11312171}
}
```
{% endraw %}
