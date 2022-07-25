---
title: "Efficient Construction and Simplification of Delaunay Meshes"
collection: publications
permalink: /publication/2015-Efficient-Construction-and-Simplification-of-Delaunay-Meshes
excerpt: ''
date: 2015-11-06
venue: 'ACM Transactions on Graphics'
tags:
  - Journal Publications
citation: 'Yong-Jin Liu*, Chun-Xu Xu, Dian Fan, Ying He* (2015) Efficient Construction and Simplification of Delaunay Meshes. ACM Transactions on Graphics (SIGGRAPH ASIA 2015), Vol. 34, No. 6, Article No. 174, 2015.'
---

Abstract: Delaunay meshes (DM) are a special type of triangle mesh where the local Delaunay condition holds everywhere. We present an efficient algorithm to convert an arbitrary manifold triangle mesh *M* into a Delaunay mesh. We show that the constructed DM has *O*(*Kn*) vertices, where *n* is the number of vertices in *M* and *K* is a model-dependent constant. We also develop a novel algorithm to simplify Delaunay meshes, allowing a smooth choice of detail levels. Our methods are conceptually simple, theoretically sound and easy to implement. The DM construction algorithm also scales well due to its *O*(*nK* log *K*) time complexity.

Delaunay meshes have many favorable geometric and numerical properties. For example, a DM has exactly the same geometry as the input mesh, and it can be encoded by any mesh data structure. Moreover, the empty geodesic circumcircle property implies that the commonly used cotangent Laplace-Beltrami operator has non-negative weights. Therefore, the existing digital geometry processing algorithms can benefit the numerical stability of DM without changing any codes. We observe that DMs can improve the accuracy of the heat method for computing geodesic distances. Also, popular parameterization techniques, such as discrete harmonic mapping, produce more stable results on the DMs than on the input meshes.



[Download paper here](http://yongjinliu.github.io/files/2015-Efficient-Construction-and-Simplification-of-Delaunay-Meshes.pdf)

[Download source code here](http://cg.cs.tsinghua.edu.cn/people/~Yongjin/DM-executable.zip)

[More information](https://dl.acm.org/doi/10.1145/2816795.2818076)

Recommended citation: **Yong-Jin Liu***, Chun-Xu Xu, Dian Fan, Ying He* (2015) Efficient Construction and Simplification of Delaunay Meshes. ACM Transactions on Graphics (SIGGRAPH ASIA 2015), Vol. 34, No. 6, Article No. 174, 2015.





