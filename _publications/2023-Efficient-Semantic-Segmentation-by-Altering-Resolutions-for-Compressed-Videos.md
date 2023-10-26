---
title: "Efficient Semantic Segmentation by Altering Resolutions for Compressed Videos"
collection: publications
permalink: /publication/2023-Efficient-Semantic-Segmentation-by-Altering-Resolutions-for-Compressed-Videos
excerpt: ''
date: 2023-06-18
venue: 'CVPR'
tags:
  - Conference Publications
citation: 'Yubin Hu, Yuze He, Yanghao Li, Jisheng Li1 Yuxing Han, Jiangtao Wen, Yong-Jin Liu*.Efficient Semantic Segmentation by Altering Resolutions for Compressed Videos. CVPR 2023.'
---

Abstract: Video semantic segmentation (VSS) is a computationally expensive task due to the per-frame prediction for videos of high frame rates. In recent work, compact models or adaptive network strategies have been proposed for efficient VSS. However, they did not consider a crucial factor that affects the computational cost from the input side: the input resolution. In this paper, we propose an altering resolution framework called AR-Seg for compressed videos to achieve efficient VSS. AR-Seg aims to reduce the computational cost by using low resolution for non-keyframes. To prevent the performance degradation caused by downsampling, we design a Cross Resolution Feature Fusion (CReFF) module, and supervise it with a novel Feature Similarity Training (FST) strategy. Specifically, CReFF first makes use of motion vectors stored in a compressed video to warp features from high-resolution keyframes to low-resolution non-keyframes for better spatial alignment, and then selectively aggregates the warped features with local attention mechanism. Furthermore, the proposed FST supervises the aggregated features with high-resolution features through an explicit similarity loss and an implicit constraint from the shared decoding layer. Extensive experiments on CamVid and Cityscapes show that AR-Seg achieves state-of-the-art performance and is compatible with different segmentation backbones. On CamVid, AR-Seg saves 67% computational cost (measured in GFLOPs) with the PSPNet18 backbone while maintaining high segmentation accuracy. Code: https://github.com/THU-LYJ-Lab/AR-Seg.




[Download paper here](http://yongjinliu.github.io/files/2023-Efficient-Semantic-Segmentation-by-Altering-Resolutions-for-Compressed-Videos.pdf)

Recommended citation: Yubin Hu, Yuze He, Yanghao Li, Jisheng Li1 Yuxing Han, Jiangtao Wen,**Yong-Jin Liu***. Efficient Semantic Segmentation by Altering Resolutions for Compressed Videos. CVPR 2023.
