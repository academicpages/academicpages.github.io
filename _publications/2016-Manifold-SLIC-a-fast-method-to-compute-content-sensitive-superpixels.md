---
title: "Manifold SLIC: a fast method to compute content-sensitive superpixels"
collection: publications
permalink: /publication/2016-Manifold-SLIC-a-fast-method-to-compute-content-sensitive-superpixels
excerpt: ''
date: 2016-06-26
venue: 'CVPR'
tags:
  - Conference Publications
citation: 'Yong-Jin Liu*, Chengchi Yu, Minjing Yu, Ying He (2016) Manifold SLIC: a fast method to compute content-sensitive superpixels. IEEE Conference on Computer Vision and Pattern Recognition (CVPR' 16), pp.651-659, 2016.'
---



Abstract: Superpixels are perceptually meaningful atomic regions that can effectively capture image features. Among various methods for computing uniform superpixels, simple linear iterative clustering (SLIC) is popular due to its simplicity and high performance. In this paper, we extend SLIC to compute content-sensitive superpixels, i.e., small superpixels in content-dense regions (e.g., with high intensity or color variation) and large superpixels in content-sparse regions. Rather than the conventional SLIC method that clusters pixels in R5, we map the image I to a 2-dimensional manifold M in R5, whose area elements are a good measure of the content density in I. We propose an efficient method to compute restricted centroidal Voronoi tessellation (RCVT) --- a uniform tessellation --- on M, which induces the content-sensitive superpixels in I. Unlike other algorithms that characterize content-sensitivity by geodesic distances, manifold SLIC tackles the problem by measuring areas of Voronoi cells on M, which can be computed at a very low cost. As a result, it runs 10 times faster than the state-of-the-art content-sensitive superpixels algorithm. We evaluate manifold SLIC and seven representative methods on the BSDS500 benchmark and observe that our method outperforms the existing methods.



[Download paper here](http://yongjinliu.github.io/files/2016-Manifold-SLIC-a-fast-method-to-compute-content-sensitive-superpixels.pdf)

[Download source code here](https://github.com/opencv/opencv_contrib/pull/923)

[More information](http://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Liu_Manifold_SLIC_A_CVPR_2016_paper.html)

Recommended citation: **Yong-Jin Liu***, Chengchi Yu, Minjing Yu, Ying He (2016) Manifold SLIC: a fast method to compute content-sensitive superpixels. IEEE Conference on Computer Vision and Pattern Recognition (CVPR' 16), pp.651-659, 2016.

