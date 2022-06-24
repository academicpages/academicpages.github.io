---
title: "Fast Computation of Content-Sensitive Superpixels and Supervoxels using q-distances"
collection: publications
permalink: /publication/2019-Fast-Computation-of-Content-Sensitive-Superpixels-and-Supervoxels-using-q-distances
excerpt: ''
date: 2019-10-29
venue: 'ICCV'
tags:
  - Conference Publications
citation: 'Zipeng Ye, Ran Yi, Minjing Yu, Yong-Jin Liu*, and Ying He. Fast Computation of Content-Sensitive Superpixels and Supervoxels using q-distances. In International Conference on Computer Vision (ICCV 19), pages 3770-3779, 2019.'
---

Abstract: State-of-the-art researches model the data of images and videos as low-dimensional manifolds and generate superpixels/supervoxels in a content-sensitive way, which is achieved by computing geodesic centroidal Voronoi tessellation (GCVT) on manifolds. However, computing exact GCVTs is slow due to computationally expensive geodesic distances. In this paper, we propose a much faster queue-based graph distance (called q-distance). Our key idea is that for manifold regions in which q-distances are different from geodesic distances, GCVT is prone to placing more generators in them, and therefore after few iterations, the q-distance-induced tessellation is an exact GCVT. This idea works well in practice and we also prove it theoretically under moderate assumption. Our method is simple and easy to implement. It runs 6-8 times faster than state-of-the-art GCVT computation, and has an optimal approximation ratio O(1) and a linear time complexity O(N) for N-pixel images or N-voxel videos. A thorough evaluation of 31 superpixel methods on five image datasets and 8 supervoxel methods on four video datasets shows that our method consistently achieves the best over-segmentation accuracy. We also demonstrate the advantage of our method on one image and two video applications.



[Download paper here](http://yongjinliu.github.io/files/2019-Fast-Computation-of-Content-Sensitive-Superpixels-and-Supervoxels-using-q-distances.pdf)

[Download source code here](https://github.com/qq775193759/qdcss_open_source)

[More information](https://openaccess.thecvf.com/content_ICCV_2019/html/Ye_Fast_Computation_of_Content-Sensitive_Superpixels_and_Supervoxels_Using_Q-Distances_ICCV_2019_paper.html)

Recommended citation: Zipeng Ye, Ran Yi, Minjing Yu, **Yong-Jin Liu***, and Ying He. Fast Computation of Content-Sensitive Superpixels and Supervoxels using q-distances. In International Conference on Computer Vision (ICCV 19), pages 3770-3779, 2019.

