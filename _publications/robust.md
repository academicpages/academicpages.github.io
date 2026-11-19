---
title: "Robust Stability Analysis of Positive Lur'e System with Neural Network Feedback"
collection: publications
category: conferences
permalink: /publication/2025-09-01-ccta-paper
excerpt: "Closed-form stability radius for positive Lur'e systems and systems with neural network feedback, plus a refinement of the network's sector bounds."
date: 2025-09-01
authors: 'H. Montazeri Hedesh, M. K. Wafi, B. Shafai, M. Siami'
venue: 'IEEE Conference on Control Technology and Applications (CCTA)'
paperurl: 'https://doi.org/10.1109/CCTA53793.2025.11151493'
ieeeurl: 'https://ieeexplore.ieee.org/document/11151493'
arxivurl: 'https://arxiv.org/abs/2505.18912'
codeurl: 'https://github.com/hmon91/Robustness-of-NN-controlled-systems'
citation: 'H. Montazeri Hedesh, M. K. Wafi, B. Shafai and M. Siami. (2025). "Robust Stability Analysis of Positive Lur&#39;e System with Neural Network Feedback," <i>2025 IEEE Conference on Control Technology and Applications</i>, San Diego, CA, USA, pp. 976-981.'
---

{% include publication-meta.html post=page %}

## In short

How much uncertainty can a feedback loop take before it loses stability? For positive Lur'e systems in which both the linear part and the sector bound of the nonlinearity are uncertain, the paper gives an explicit formula for the stability radius, using Metzler matrices and the positive Aizerman conjecture. It extends the result to systems with neural network feedback and gives a way to refine the sector bounds of the network.

**Topics:** robust stability, stability radius, parametric uncertainty, Metzler matrices, neural network controllers.

## Abstract

This paper investigates the robustness of the Lur'e problem under positivity constraints, drawing on results from the positive Aizerman conjecture and robustness properties of Metzler matrices. Specifically, we consider a control system of Lur'e type in which not only the linear part includes parametric uncertainty but also the nonlinear sector bound is unknown. We investigate tools from positive linear systems to effectively solve the problems in complicated and uncertain nonlinear systems. By leveraging the positivity characteristic of the system, we derive an explicit formula for the stability radius of Lur'e systems. Furthermore, we extend our analysis to systems with neural network (NN) feedback loops. Building on this approach, we also propose a refinement method for sector bounds of NNs. This study introduces a scalable and efficient approach for robustness analysis of both Lur'e and NN-controlled systems. Finally, the proposed results are supported by illustrative examples.

## BibTeX

{% raw %}
```bibtex
@inproceedings{montazerihedesh2025robust,
  author    = {Montazeri Hedesh, Hamidreza and Wafi, Moh Kamalul and Shafai, Bahram and Siami, Milad},
  title     = {Robust Stability Analysis of Positive {Lur'e} System with Neural Network Feedback},
  booktitle = {2025 IEEE Conference on Control Technology and Applications (CCTA)},
  address   = {San Diego, CA, USA},
  pages     = {976--981},
  year      = {2025},
  doi       = {10.1109/CCTA53793.2025.11151493}
}
```
{% endraw %}
