---
title: "Fast wavefront propagation (FWP) for computing exact geodesic distances on meshes"
collection: publications
permalink: /publication/2015-Fast-wavefront-propagation-(FWP)-for-computing-exact-geodesic-distances-on-meshes
excerpt: ''
date: 2015-02-26
venue: 'IEEE Transactions on Visualization and Computer Graphics'
tags:
  - Journal Publications
citation: 'Chunxu Xu, Tuanfeng Y. Wang, Yong-Jin Liu*, Ligang Liu, Ying He* (2015) Fast wavefront propagation (FWP) for computing exact geodesic distances on meshes. IEEE Transactions on Visualization and Computer Graphics, Vol. 21, No. 7, pp. 822-834, 2015.'
---

Abstract: Computing geodesic distances on triangle meshes is a fundamental problem in computational geometry and computer graphics. To date, two notable classes of algorithms, the Mitchell-Mount-Papadimitriou (MMP) algorithm and the Chen-Han (CH) algorithm, have been proposed. Although these algorithms can compute exact geodesic distances if numerical computation is exact, they are computationally expensive, which diminishes their usefulness for large-scale models and/or time-critical applications. In this paper, we propose the fast wavefront propagation (FWP) framework for improving the performance of both the MMP and CH algorithms. Unlike the original algorithms that propagate only a single window (a data structure locally encodes geodesic information) at each iteration, our method organizes windows with a bucket data structure so that it can process a large number of windows simultaneously without compromising wavefront quality. Thanks to its macro nature, the FWP method is less sensitive to mesh triangulation than the MMP and CH algorithms. We evaluate our FWP-based MMP and CH algorithms on a wide range of large-scale real-world models. Computational results show that our method can improve the speed by a factor of 3-10.



[Download paper here](http://yongjinliu.github.io/files/2015-Fast-wavefront-propagation-(FWP)-for-computing-exact-geodesic-distances-on-meshes.pdf)

[Download source code here](http://cg.cs.tsinghua.edu.cn/people/~Yongjin/FWP_executable.zip)

[More information](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=7050361&filter%3DAND%28p_IS_Number%3A7112593%29)

Recommended citation: Chunxu Xu, Tuanfeng Y. Wang, **Yong-Jin Liu***, Ligang Liu, Ying He* (2015) Fast wavefront propagation (FWP) for computing exact geodesic distances on meshes. IEEE Transactions on Visualization and Computer Graphics, Vol. 21, No. 7, pp. 822-834, 2015.





