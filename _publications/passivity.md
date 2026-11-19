---
title: "A Passivity-Agnostic Framework for Distributed Adaptive Synchronization under Unknown Leader Dynamics"
collection: publications
category: conferences
permalink: /publication/2026-05-01-acc-passivity
excerpt: 'Distributed adaptive synchronization that drops the passivity assumption, with an unknown leader.'
date: 2026-05-01
authors: 'M. K. Wafi, H. Montazeri Hedesh, M. Siami'
venue: 'American Control Conference (ACC)'
paperurl: 'https://ieeexplore.ieee.org/document/11616306'
ieeeurl: 'https://ieeexplore.ieee.org/document/11616306'
arxivurl: 'https://arxiv.org/abs/2603.02344'
citation: 'M. K. Wafi, H. Montazeri Hedesh, and M. Siami. (2026). "A Passivity-Agnostic Framework for Distributed Adaptive Synchronization under Unknown Leader Dynamics," <i>2026 American Control Conference</i>, New Orleans, LA, USA, pp. 3385-3391.'
---

{% include publication-meta.html post=page %}

## In short

A way for a group of agents to synchronize with a leader whose dynamics are unknown, using only position information and under bounded disturbances. The design does not need the closed loop to be strictly positive real (SPR) in advance: it certifies SPR when present and recovers it by frequency shaping when absent. Lyapunov analysis gives synchronization and disturbance rejection guarantees.

**Topics:** multi-agent systems, distributed adaptive control, synchronization, passivity, strictly positive real systems.

## Abstract

We present a passivity-agnostic framework for distributed adaptive synchronization under position-only communication, bounded disturbances, and unknown leader dynamics. By passivity-agnostic we mean the design does not require the closed loop system to be strictly positive real (SPR) a priori: it certifies SPR when present and recovers it by frequency shaping when absent. Followers are heterogeneous second-order systems with unknown (possibly unstable) dynamics. In the SPR regime, a structured reparameterization yields gradient-based adaptive error dynamics; Lyapunov analysis guarantees global asymptotic synchronization in the disturbance-free case, exact rejection of constant disturbances, and bounded responses to time-varying disturbances, with parameter convergence under persistent excitation. In the non-SPR regime, frequency shaping recovers effective passivity of the unshaped transfer function, enabling the same stability guarantees via standard passivity/Lyapunov arguments using Meyer-Kalman-Yakubovich (MKY) Lemma. Simulations across star, cyclic, path, and arbitrary graphs demonstrate scalable synchronization, robust tracking, and parameter adaptation under multiple disturbance profiles, confirming that the frequency-shaped non-SPR designs match the performance of the SPR case.

## BibTeX

{% raw %}
```bibtex
@inproceedings{wafi2026passivity,
  author    = {Wafi, Moh Kamalul and Montazeri Hedesh, Hamidreza and Siami, Milad},
  title     = {A Passivity-Agnostic Framework for Distributed Adaptive Synchronization under Unknown Leader Dynamics},
  booktitle = {2026 American Control Conference (ACC)},
  address   = {New Orleans, LA, USA},
  pages     = {3385--3391},
  year      = {2026},
  url       = {https://ieeexplore.ieee.org/document/11616306}
}
```
{% endraw %}
