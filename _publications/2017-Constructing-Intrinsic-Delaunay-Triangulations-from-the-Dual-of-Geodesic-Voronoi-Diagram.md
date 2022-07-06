---
title: "Constructing Intrinsic Delaunay Triangulations from the Dual of Geodesic Voronoi Diagram"
collection: publications
permalink: /publication/2017-Constructing-Intrinsic-Delaunay-Triangulations-from-the-Dual-of-Geodesic-Voronoi-Diagram
excerpt: ''
date: 2017-04-14
venue: 'ACM Transactions on Graphics'
tags:
  - Journal Publications
citation: 'Yong-Jin Liu, Dian Fan, Chun-Xu Xu, Ying He (2017) Constructing Intrinsic Delaunay Triangulations from the Dual of Geodesic Voronoi Diagram. ACM Transactions on Graphics, Vol. 36, No. 2, Article No. 15, 2017.'
---

Abstract: Intrinsic Delaunay triangulation (IDT) naturally generalizes Delaunay triangulation from R2 to curved surfaces. Due to many favorable properties, the IDT whose vertex set includes all mesh vertices is of particular interest in polygonal mesh processing. To date, the only way for constructing such IDT is the edge-flipping algorithm, which iteratively flips non-Delaunay edges to become locally Delaunay. Although this algorithm is conceptually simple and guarantees to terminate in finite steps, it has no known time complexity and may also produce triangulations containing faces with only two edges. This article develops a new method to obtain proper IDTs on manifold triangle meshes. We first compute a geodesic Voronoi diagram (GVD) by taking all mesh vertices as generators and then find its dual graph. The sufficient condition for the dual graph to be a proper triangulation is that all Voronoi cells satisfy the so-called closed ball property. To guarantee the closed ball property everywhere, a certain sampling criterion is required. For Voronoi cells that violate the closed ball property, we fix them by computing topologically safe regions, in which auxiliary sites can be added without changing the topology of the Voronoi diagram beyond them. Given a mesh with *n* vertices, we prove that by adding at most *O*(*n*) auxiliary sites, the computed GVD satisfies the closed ball property, and hence its dual graph is a proper IDT. Our method has a theoretical worst-case time complexity *O*(*n*$^{2}$ + *tn*log *n*), where *t* is the number of obtuse angles in the mesh. Computational results show that it empirically runs in linear time on real-world models.



[Download paper here](http://yongjinliu.github.io/files/2017-Constructing-Intrinsic-Delaunay-Triangulations-from-the-Dual-of-Geodesic-Voronoi-Diagram.pdf)

[More information](https://dl.acm.org/doi/10.1145/2999532)

Recommended citation: **Yong-Jin Liu**, Dian Fan, Chun-Xu Xu, Ying He (2017) Constructing Intrinsic Delaunay Triangulations from the Dual of Geodesic Voronoi Diagram. ACM Transactions on Graphics, Vol. 36, No. 2, Article No. 15, 2017. 





