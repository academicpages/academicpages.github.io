---
title: "A global energy optimization framework for 2.1D sketch extraction from monocular images"
collection: publications
permalink: /publication/2014-A-global-energy-optimization-framework-for-2.1D-sketch-extraction-from-monocular-images
excerpt: ''
date: 2014-09-01
venue: 'Graphical Models'
tags:
  - Journal Publications
citation: 'Cheng-Chi Yu, Yong-Jin Liu*, Tianfu Wu, Kai-Yun Li, Xiaolan Fu (2014) A global energy optimization framework for 2.1D sketch extraction from monocular images. Graphical Models (Special issue of GMP 2014), Vol. 76, No. 5, pp. 507-521, 2014.'
---

Abstract: The 2.1D sketch is a layered image representation, which assigns a partial depth ordering of over-segmented regions in a monocular image. This paper presents a global optimization framework for inferring the 2.1D sketch from a monocular image. Our method only uses over-segmented image regions (i.e., superpixels) as input, without any information of objects in the image, since (1) segmenting objects in images is a difficult problem on its own and (2) the objective of our proposed method is to be generic as an initial module useful for downstream high-level vision tasks. This paper formulates the inference of the 2.1D sketch using a global energy optimization framework. The proposed energy function consists of two components: (1) one is defined based on the local partial ordering relations (i.e., figure-ground) between two adjacent over-segmented regions, which captures the marginal information of the global partial depth ordering and (2) the other is defined based on the same depth layer relations among all the over-segmented regions, which groups regions of the same object to account for the over-segmentation issues. A hybrid evolution algorithm is utilized to minimize the global energy function efficiently. In experiments, we evaluated our method on a test data set containing 100 diverse real images from Berkeley segmentation data set (BSDS500) with the annotated ground truth. Experimental results show that our method can infer the 2.1D sketch with high accuracy.



[Download paper here](http://yongjinliu.github.io/files/2014-A-global-energy-optimization-framework-for-2.1D-sketch-extraction-from-monocular-images.pdf)

[Download source code here](http://cg.cs.tsinghua.edu.cn/people/~Yongjin/2.1D-source.zip)

[More information](http://authors.elsevier.com/sd/article/S1524070314000228)

Recommended citation: Cheng-Chi Yu, **Yong-Jin Liu***, Tianfu Wu, Kai-Yun Li, Xiaolan Fu (2014) A global energy optimization framework for 2.1D sketch extraction from monocular images. Graphical Models (Special issue of GMP 2014), Vol. 76, No. 5, pp. 507-521, 2014.





