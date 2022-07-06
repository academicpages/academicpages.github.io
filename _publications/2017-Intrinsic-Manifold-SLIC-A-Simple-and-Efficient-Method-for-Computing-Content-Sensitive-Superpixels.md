---
title: "Intrinsic Manifold SLIC: A Simple and Efficient Method for Computing Content-Sensitive Superpixels"
collection: publications
permalink: /publication/2017-Intrinsic-Manifold-SLIC-A-Simple-and-Efficient-Method-for-Computing-Content-Sensitive-Superpixels
excerpt: ''
date: 2017-03-23
venue: 'IEEE Transactions on Pattern Analysis and Machine Intelligence'
tags:
  - Journal Publications
citation: 'Yong-Jin Liu, Minjing Yu, Bing-Jun Li, Ying He (2018) Intrinsic Manifold SLIC: A Simple and Efficient Method for Computing Content-Sensitive Superpixels. IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 40, No. 3, pp. 653-666, 2018.'
---

Abstract: Superpixels are perceptually meaningful atomic regions that can effectively capture image features. Among various methods for computing uniform superpixels, simple linear iterative clustering (SLIC) is popular due to its simplicity and high performance. In this paper, we extend SLIC to compute content-sensitive superpixels, i.e., small superpixels in content-dense regions with high intensity or colour variation and large superpixels in content-sparse regions. Rather than using the conventional SLIC method that clusters pixels in $R^{5}$, we map the input image Ito a 2-dimensional manifold $M\subset R^{5}$, whose area elements are a good measure of the content density in I. We propose a simple method, called intrinsic manifold SLIC (IMSLIC), for computing a geodesic centroidal Voronoi tessellation (GCVT)-a uniform tessellation-on M, which induces the content-sensitive superpixels in I. In contrast to the existing algorithms, IMSLIC characterizes the content sensitivity by measuring areas of Voronoi cells on M. Using a simple and fast approximation to a closed-form solution, the method can compute the GCVT at a very low cost and guarantees that all Voronoi cells are simply connected. We thoroughly evaluate IMSLIC and compare it with eleven representative methods on the BSDS500 dataset and seven representative methods on the NYUV2 dataset. Computational results show that IMSLIC outperforms existing methods in terms of commonly used quality measures pertaining to superpixels such as compactness, adherence to boundaries, and achievable segmentation accuracy. We also evaluate IMSLIC and seven representative methods in an image contour closure application, and the results on two datasets, WHD and WSD, show that IMSLIC achieves the best foreground segmentation performance.



[Download paper here](http://yongjinliu.github.io/files/2017-Intrinsic-Manifold-SLIC-A-Simple-and-Efficient-Method-for-Computing-Content-Sensitive-Superpixels.pdf)

[Download source code here](http://docs.opencv.org/trunk/df/d6c/group__ximgproc__superpixel.html)

[More information](https://ieeexplore.ieee.org/document/7885581)

Recommended citation: **Yong-Jin Liu**, Minjing Yu, Bing-Jun Li, Ying He (2018) Intrinsic Manifold SLIC: A Simple and Efficient Method for Computing Content-Sensitive Superpixels. IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 40, No. 3, pp. 653-666, 2018.





