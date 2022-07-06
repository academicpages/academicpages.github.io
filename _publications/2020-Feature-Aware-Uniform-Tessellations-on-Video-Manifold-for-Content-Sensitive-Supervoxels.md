---
title: "Feature-Aware Uniform Tessellations on Video Manifold for Content-Sensitive Supervoxels"
collection: publications
permalink: /publication/2020-Feature-Aware-Uniform-Tessellations-on-Video-Manifold-for-Content-Sensitive-Supervoxels
excerpt: ''
date: 2020-03-10
venue: 'IEEE Transactions on Pattern Analysis and Machine Intelligence'
tags:
  - Journal Publications
citation: 'Ran Yi, Zipeng Ye, Wang Zhao, Minjing Yu, Yu-Kun Lai, Yong-Jin Liu*. Feature-Aware Uniform Tessellations on Video Manifold for Content-Sensitive Supervoxels. IEEE Transactions on Pattern Analysis and Machine Intelligence. DOI (identifier) 10.1109/TPAMI.2020.2979714, 2020.'
---

Abstract: Over-segmenting a video into supervoxels has strong potential to reduce the complexity of downstream computer vision applications. Content-sensitive supervoxels (CSSs) are typically smaller in content-dense regions (i.e., with high variation of appearance and/or motion) and larger in content-sparse regions. In this paper, we propose to compute feature-aware CSSs (FCSSs) that are regularly shaped 3D primitive volumes well aligned with local object/region/motion boundaries in video. To compute FCSSs, we map a video to a 3D manifold embedded in a combined color and spatiotemporal space, in which the volume elements of video manifold give a good measure of the video content density. Then any uniform tessellation on video manifold can induce CSS in the video. Our idea is that among all possible uniform tessellations on the video manifold, FCSS finds one whose cell boundaries well align with local video boundaries. To achieve this goal, we propose a novel restricted centroidal Voronoi tessellation method that simultaneously minimizes the tessellation energy (leading to uniform cells in the tessellation) and maximizes the average boundary distance (leading to good local feature alignment). Theoretically our method has an optimal competitive ratio O(1)O(1), and its time and space complexities are O(NK)O(NK) and O(N+K)O(N+K) for computing KK supervoxels in an NN-voxel video. We also present a simple extension of FCSS to streaming FCSS for processing long videos that cannot be loaded into main memory at once. We evaluate FCSS, streaming FCSS and ten representative supervoxel methods on four video datasets and two novel video applications. The results show that our method simultaneously achieves state-of-the-art performance with respect to various evaluation criteria.



[Download paper here](http://yongjinliu.github.io/files/2020-Feature-Aware-Uniform-Tessellations-on-Video-Manifold-for-Content-Sensitive-Supervoxels.pdf)

[Download source code here](https://github.com/yiranran/FCSS)

[More information](https://ieeexplore.ieee.org/document/9031395)

Recommended citation: Ran Yi, Zipeng Ye, Wang Zhao, Minjing Yu, Yu-Kun Lai, **Yong-Jin Liu\***. Feature-Aware Uniform Tessellations on Video Manifold for Content-Sensitive Supervoxels. IEEE Transactions on Pattern Analysis and Machine Intelligence. DOI (identifier) 10.1109/TPAMI.2020.2979714, 2020.





