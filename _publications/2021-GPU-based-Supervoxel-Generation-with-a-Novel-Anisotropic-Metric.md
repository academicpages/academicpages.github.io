---
title: "GPU-based Supervoxel Generation with a Novel Anisotropic Metric"
collection: publications
permalink: /publication/2021-GPU-based-Supervoxel-Generation-with-a-Novel-Anisotropic-Metric
excerpt: ''
date: 2021-10-22
venue: 'IEEE Transactions on Image Processing'
tags:
  - Journal Publications
citation: 'Xiao Dong, Zhonggui Chen, Yong-Jin Liu, Junfeng Yao, Xiaohu Guo. GPU-based Supervoxel Generation with a Novel Anisotropic Metric. IEEE Transactions on Image Processing, Vol. 30, pp. 8847-8860, 2021.'
---

Abstract: Video over-segmentation into supervoxels is an important pre-processing technique for many computer vision tasks. Videos are an order of magnitude larger than images. Most existing methods for generating supervovels are either memory- or time-inefficient, which limits their application in subsequent video processing tasks. In this paper, we present an anisotropic supervoxel method, which is memory-efficient and can be executed on the graphics processing unit (GPU). Therefore, our algorithm achieves good balance among segmentation quality, memory usage and processing time. In order to provide accurate segmentation for moving objects in video, we use the optical flow information to design a brand new non-Euclidean metric to calculate the anisotropic distances between seeds and voxels. To efficiently compute the anisotropic metric, we adjust the classic jump flooding algorithm (which is designed for parallel execution on the GPU) to generate anisotropic Voronoi tessellation in the combined color and spatio-temporal space. We evaluate our method and the representative supervoxel algorithms for their capability on segmentation performance, computation speed and memory efficiency. We also apply supervoxel results to the application of foreground propagation in videos to test the performance on solving practical problems. Experiments show that our algorithm is much faster than the existing methods, and achieves good balance on segmentation quality and efficiency.



[Download paper here](http://yongjinliu.github.io/files/2021-GPU-based-Supervoxel-Generation-with-a-Novel-Anisotropic-Metric.pdf)

[Download source code here](https://github.com/dongxiao0401/anisotropic_supervoxel)

[More information](https://ieeexplore.ieee.org/document/9585028)

Recommended citation: Xiao Dong, Zhonggui Chen, **Yong-Jin Liu**, Junfeng Yao, Xiaohu Guo. GPU-based Supervoxel Generation with a Novel Anisotropic Metric. IEEE Transactions on Image Processing, Vol. 30, pp. 8847-8860, 2021.





