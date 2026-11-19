---
title: "Ensuring Both Positivity and Stability Using Sector-Bounded Nonlinearity for Systems With Neural Network Controllers"
collection: publications
category: manuscripts
permalink: /publication/2024-01-01-lcss-positivity
excerpt: "A fast test for global exponential stability of linear systems with neural network controllers, using sector bounds computed from the network weights."
date: 2024-01-01
authors: 'H. Montazeri Hedesh, M. Siami'
venue: 'IEEE Control Systems Letters (L-CSS)'
paperurl: 'https://doi.org/10.1109/LCSYS.2024.3416237'
ieeeurl: 'https://ieeexplore.ieee.org/document/10561541'
arxivurl: 'https://arxiv.org/abs/2406.12744'
codeurl: 'https://github.com/hmon91/Global-stability-of-NN-controlled-systems'
libraries:
  - name: nnsector
    url: 'https://github.com/hmon91/nnsector'
  - name: nnstab
    url: 'https://github.com/hmon91/nnstab'
citation: 'H. Montazeri Hedesh and M. Siami. (2024). "Ensuring Both Positivity and Stability Using Sector-Bounded Nonlinearity for Systems With Neural Network Controllers," <i>IEEE Control Systems Letters</i>, vol. 8, pp. 1685-1690.'
---

{% include publication-meta.html post=page %}

## In short

A fast way to check that a linear system with a neural network controller is globally stable. The network (fully connected, without biases) is bounded by a sector computed from its weights. Two simple matrix checks (Metzler and Hurwitz), based on positive Lur'e systems and the positive Aizerman conjecture, then take the place of a large semidefinite program.

**Topics:** stability verification of neural network controllers, absolute stability, sector bounds, positive systems, Lur'e systems.

## Abstract

This paper introduces a novel method for the stability analysis of positive feedback systems with a class of fully connected feedforward neural networks (FFNN) controllers. By establishing sector bounds for fully connected FFNNs without biases, we present a stability theorem that demonstrates the global exponential stability of linear systems under fully connected FFNN control. Utilizing principles from positive Lur'e systems and the positive Aizerman conjecture, our approach effectively addresses the challenge of ensuring stability in highly nonlinear systems. The crux of our method lies in maintaining sector bounds that preserve the positivity and Hurwitz property of the overall Lur'e system. We showcase the practical applicability of our methodology through its implementation in a linear system managed by a FFNN trained on output feedback controller data, highlighting its potential for enhancing stability in dynamic systems.

## BibTeX

{% raw %}
```bibtex
@article{montazerihedesh2024ensuring,
  author  = {Montazeri Hedesh, Hamidreza and Siami, Milad},
  title   = {Ensuring Both Positivity and Stability Using Sector-Bounded Nonlinearity for Systems With Neural Network Controllers},
  journal = {IEEE Control Systems Letters},
  volume  = {8},
  pages   = {1685--1690},
  year    = {2024},
  doi     = {10.1109/LCSYS.2024.3416237}
}
```
{% endraw %}
