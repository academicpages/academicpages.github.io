---
title: "Distributed Adaptive Estimation with ISS Guarantees for Sensor Networks with Partially Unknown Source Dynamics"
collection: publications
category: conferences
permalink: /publication/2026-10-02-submitted-ifac
excerpt: "Distributed adaptive observers for sensor networks whose source dynamics are partly unknown, with convergence and input-to-state stability (ISS) bounds."
date: 2026-10-02
authors: 'M. K. Wafi, H. Montazeri Hedesh, M. Siami'
status: 'Accepted at the IFAC World Congress 2026'
paperurl: 'https://arxiv.org/abs/2511.07646'
arxivurl: 'https://arxiv.org/abs/2511.07646'
citation: 'M. K. Wafi, H. Montazeri Hedesh, and M. Siami. (2026). "Distributed Adaptive Estimation with ISS Guarantees for Sensor Networks with Partially Unknown Source Dynamics," <i>23rd IFAC World Congress</i>, Busan, Republic of Korea (Accepted).'
---

{% include publication-meta.html post=page %}

## In short

Each sensor in a network runs a local adaptive observer to estimate a source whose dynamics are partly unknown, and shares information with its neighbors over a directed graph. The paper gives continuous-time and discrete-time designs, proves that the estimate of every node converges to the source despite model uncertainty and disturbances, and gives input-to-state stability (ISS) bounds for bounded noise.

**Topics:** distributed estimation, adaptive observers, sensor networks, input-to-state stability.

## Abstract

This paper studies distributed adaptive estimation over sensor networks with partially unknown source dynamics. We present parallel continuous-time and discrete-time designs in which each node runs a local adaptive observer and exchanges information over a directed graph. For both time scales, we establish stability of the network coupling operators, prove boundedness of all internal signals, and show convergence of each node's estimate to the source despite model uncertainty and disturbances. We further derive input-to-state stability (ISS) bounds that quantify robustness to bounded process noise. A key distinction is that the discrete-time design uses constant adaptive gains and per-step regressor normalization to handle sampling effects, whereas the continuous-time design does not. A unified Lyapunov framework links local observer dynamics with graph topology. Simulations on star, cyclic, and path networks corroborate the analysis, demonstrating accurate tracking, robustness, and scalability with the number of sensing nodes.

## BibTeX

{% raw %}
```bibtex
@inproceedings{wafi2026distributed,
  author        = {Wafi, Moh Kamalul and Montazeri Hedesh, Hamidreza and Siami, Milad},
  title         = {Distributed Adaptive Estimation with {ISS} Guarantees for Sensor Networks with Partially Unknown Source Dynamics},
  booktitle     = {23rd IFAC World Congress},
  address       = {Busan, Republic of Korea},
  year          = {2026},
  note          = {To appear},
  eprint        = {2511.07646},
  archivePrefix = {arXiv},
  primaryClass  = {eess.SY}
}
```
{% endraw %}
