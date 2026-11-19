---
title: "Delay Independent Safe Control with Neural Networks: Positive Lur'e Certificates for Risk Aware Autonomy"
collection: publications
category: conferences
permalink: /publication/2026-05-01-acc-delay
excerpt: "Certificates for neural feedback loops that hold across state and input delays and interval-matrix uncertainty."
date: 2026-05-01
authors: 'H. Montazeri Hedesh, M. Siami'
venue: 'American Control Conference (ACC)'
paperurl: 'https://ieeexplore.ieee.org/document/11616300'
ieeeurl: 'https://ieeexplore.ieee.org/document/11616300'
arxivurl: 'https://arxiv.org/abs/2510.06661'
codeurl: 'https://github.com/hmon91/Delay-independant-safety-of-NN-controllers'
citation: 'H. Montazeri Hedesh, and M. Siami. (2026). "Delay Independent Safe Control with Neural Networks: Positive Lur&apos;e Certificates for Risk Aware Autonomy," <i>2026 American Control Conference</i>, New Orleans, LA, USA, pp. 134-141.'
---

{% include publication-meta.html post=page %}

## In short

Safety certificates for systems with a neural network controller under two common risks: time delays in the state or the input, and interval (parametric) uncertainty in the model. The controller is enclosed by local sector bounds, and the positive structure of the system gives linear tests that hold for any delay. In the examples, these tests ran orders of magnitude faster than an SDP-based IQC verification pipeline and certified cases that the IQC test could not.

**Topics:** time-delay systems, delay-independent stability, safe learning-enabled control, interval uncertainty, neural network verification, IQC.

## Abstract

We present a risk-aware safety certification method for autonomous, learning enabled control systems. Focusing on two realistic risks, state/input delays and interval matrix uncertainty, we model the neural network (NN) controller with local sector bounds and exploit positivity structure to derive linear, delay-independent certificates that guarantee local exponential stability across admissible uncertainties. To benchmark performance, we adopt and implement a state-of-the-art IQC NN verification pipeline. On representative cases, our positivity-based tests run orders of magnitude faster than SDP-based IQC while certifying regimes the latter cannot, providing scalable safety guarantees that complement risk-aware control.

## BibTeX

{% raw %}
```bibtex
@inproceedings{montazerihedesh2026delay,
  author    = {Montazeri Hedesh, Hamidreza and Siami, Milad},
  title     = {Delay Independent Safe Control with Neural Networks: Positive {Lur'e} Certificates for Risk Aware Autonomy},
  booktitle = {2026 American Control Conference (ACC)},
  address   = {New Orleans, LA, USA},
  pages     = {134--141},
  year      = {2026},
  url       = {https://ieeexplore.ieee.org/document/11616300}
}
```
{% endraw %}
