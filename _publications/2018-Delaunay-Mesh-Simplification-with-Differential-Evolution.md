---
title: "Delaunay Mesh Simplification with Differential Evolution"
collection: publications
permalink: /publication/2018-Delaunay-Mesh-Simplification-with-Differential-Evolution
excerpt: ''
date: 2018-12-04
venue: 'ACM Transactions on Graphics'
tags:
  - Journal Publications
citation: 'Ran Yi, Yong-Jin Liu*, Ying He. Delaunay Mesh Simplification with Differential Evolution. ACM Transactions on Graphics (SIGGRAPH ASIA 2018), Vol. 37, No. 6, Article No. 263, 2018.'
---

Abstract: Delaunay meshes (DM) are a special type of manifold triangle meshes --- where the local Delaunay condition holds everywhere --- and find important applications in digital geometry processing. This paper addresses the general DM simplification problem: given an arbitrary manifold triangle mesh $M$ with $n$ vertices and the user-specified resolution $m$ ($\lt n$), compute a Delaunay mesh $M^{*}$ with $m$ vertices that has the least Hausdorffdistance to $M$. To solve the problem, we abstract the simplification process using a 2D Cartesian grid model, in which each grid point corresponds to triangle meshes with a certain number of vertices and a simplification process is a monotonic path on the grid. We develop a novel differential-evolution-based method to compute a low-cost path, which leads to a high quality Delaunay mesh. Extensive evaluation shows that our method consistently outperforms the existing methods in terms of approximation error. In particular, our method is highly effective for small-scale CAD models and man-made objects with sharp features but less details. Moreover, our method is fully automatic and can preserve sharp features well and deal with models with multiple components, whereas the existing methods often fail.



[Download paper here](http://yongjinliu.github.io/files/2018-Delaunay-Mesh-Simplification-with-Differential-Evolution.pdf)

[More information](https://dl.acm.org/doi/10.1145/3272127.3275068)

Recommended citation: Ran Yi, **Yong-Jin Liu\***, Ying He. Delaunay Mesh Simplification with Differential Evolution. ACM Transactions on Graphics (SIGGRAPH ASIA 2018), Vol. 37, No. 6, Article No. 263, 2018.





