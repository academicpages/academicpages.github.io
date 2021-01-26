---
title: "Understanding Self-supervised Learning with Dual Deep Networks"
collection: publications
permalink: /publications/SSLTheory
venue: "ArXiv 2020"
date: 2020-12-02
citation: 'Yuandong Tian, <b>Lantao Yu</b>, Xinlei Chen, Surya Ganguli. <i>Preprint. arXiv:2010.00578</i>'
---

[[ArXiv]](https://arxiv.org/pdf/2010.00578.pdf)

## Abstract
We propose a novel theoretical framework to understand self-supervised learning methods that employ dual pairs of deep ReLU networks (e.g., SimCLR, BYOL). First, we prove that in each SGD update of SimCLR with various loss functions (simple contrastive loss, soft Triplet loss and InfoNCE loss), the weights at each layer are updated by a \emph{covariance operator} that specifically amplifies initial random selectivities that vary across data samples but survive averages over data augmentations. We show this leads to the emergence of hierarchical features, if the input data are generated from a hierarchical latent tree model. With the same framework, we also show analytically that in BYOL, the combination of BatchNorm and a predictor network creates an implicit contrastive term, acting as an approximate covariance operator. Additionally, for linear architectures we derive exact solutions for BYOL that provide conceptual insights into how BYOL can learn useful non-collapsed representations without any contrastive terms that separate negative pairs. Extensive ablation studies justify our theoretical findings.