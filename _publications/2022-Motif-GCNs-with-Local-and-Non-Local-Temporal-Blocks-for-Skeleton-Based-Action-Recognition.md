---
title: "Motif-GCNs with Local and Non-Local Temporal Blocks for Skeleton-Based Action Recognition"
collection: publications
permalink: /publication/2022-Motif-GCNs-with-Local-and-Non-Local-Temporal-Blocks-for-Skeleton-Based-Action-Recognition
excerpt: ''
date: 2022-04-26
venue: 'IEEE Transactions on Pattern Analysis and Machine Intelligence'
tags:
  - Journal Publications
citation: 'Yu-Hui Wen, Lin Gao, Hongbo Fu, Fang-Lue Zhang, Shihong Xia, Yong-Jin Liu*. Motif-GCNs with Local and Non-Local Temporal Blocks for Skeleton-Based Action Recognition. IEEE Transactions on Pattern Analysis and Machine Intelligence, Digital Object Identifier: 10.1109/TPAMI.2022.3170511'
---

Abstract: Recent works have achieved remarkable performance for action recognition with human skeletal data by utilizing graph convolutional models. Existing models mainly focus on developing graph convolutions to encode structural properties of the skeletal graph. Some recent works further take sample-dependent relationships among joints into consideration. However, the complex relationships are difficult to learn. In this paper, we propose a motif-based graph convolution method, which makes use of sample-dependent latent relations among non-physically connected joints to impose a high-order locality and assigns different semantic roles to physical neighbors of a joint to encode hierarchical structures. Furthermore, we propose a sparsity-promoting loss function to learn a sparse motif adjacency matrix for latent dependencies in non-physical connections. For extracting effective temporal information, we propose an efficient local temporal block. It adopts partial dense connections to reuse temporal features in local time windows, and enrich a variety of information flow by gradient combination. In addition, we introduce a non-local temporal block to capture global dependencies among frames. Comprehensive experiments on four large-scale datasets show that our model outperforms the state-of-the-art methods. Our code is publicly available at https://github.com/wenyh1616/SAMotif-GCN.



[Download paper here](http://yongjinliu.github.io/files/2022-Motif-GCNs-with-Local-and-Non-Local-Temporal-Blocks-for-Skeleton-Based-Action-Recognition.pdf)

[Download source code here](https://github.com/wenyh1616/SAMotif-GCN)

[More information](https://ieeexplore.ieee.org/document/9763364)

Recommended citation: Yu-Hui Wen, Lin Gao, Hongbo Fu, Fang-Lue Zhang, Shihong Xia, **Yong-Jin Liu\***. Motif-GCNs with Local and Non-Local Temporal Blocks for Skeleton-Based Action Recognition. IEEE Transactions on Pattern Analysis and Machine Intelligence, Digital Object Identifier: 10.1109/TPAMI.2022.3170511