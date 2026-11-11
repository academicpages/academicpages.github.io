---
title: "SiGMA: Learning under Graph-Level Heterogeneity with Gated Message-Passing and Attention"
collection: publications
permalink: /publication/sigma
excerpt: 'A gated hybrid GNN that adapts message-passing and attention to graph-level heterogeneity.'
date: 2026-11-10
venue: 'Preprint'
authors: 'Raphaël Pellegrin, Lukas Fesser, Melanie Weber'
paperurl: https://openreview.net/attachment?id=OgURj8X2sT&name=pdf
tags:
  - Machine Learning
  - Geometric Machine Learning
  - GNN architecture
---

<p style="text-align:justify">
In graph-level learning, graph neural networks are typically applied with a fixed computational template: the same depth, local message-passing operator, and global attention mechanism are used for every input graph. However, different graphs within the same dataset can vary substantially in prediction difficulty and may require different mixtures of local and non-local computation. We study this phenomenon as graph-level heterogeneity in both classification and regression tasks. To address it, we propose SiGMA (Sigmoid Gated Message-Passing and Attention), a gated hybrid graph neural network architecture that combines message-passing and attention heads within each layer. Inspired by the growing use of gated attention and gated computation in large language models and vision transformers, each head in SiGMA is modulated by a learned node-wise sigmoid gate, allowing the model to adaptively regulate which local or global mechanisms are active for different nodes, layers, and input graphs. The resulting architecture can emulate expressive message-passing backbones, admits near-identity computation paths that are not forced to over-smooth, and enables direct non-local communication beyond message-passing neighborhoods to mitigate over-squashing. Empirically, SiGMA achieves strong performance across graph-level benchmarks, consistently matching or improving over competitive graph transformer and hybrid baselines. Our results suggest that adapting computation to graph-level heterogeneity is a promising direction for building more flexible and effective graph learning architectures.
</p>
