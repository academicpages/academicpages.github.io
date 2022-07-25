---
title: "Exact geodesic metric in 2-manifold triangle meshes using edge-based data structures"
collection: publications
permalink: /publication/2013-Exact-geodesic-metric-in-2-manifold-triangle-meshes-using-edge-based-data-structures
excerpt: ''
date: 2013-03-01
venue: 'Computer-Aided Design'
tags:
  - Journal Publications
citation: 'Yong-Jin Liu (2013) Exact geodesic metric in 2-manifold triangle meshes using edge-based data structures. Computer-Aided Design, Vol. 45, No. 3, pp. 695-704, 2013.'
---

Abstract: A natural metric in 2-manifold surfaces is to use geodesic distance. If a 2-manifold surface is represented by a triangle mesh $T$ , the geodesic metric on $T$ can be computed exactly using computational geometry methods. Previous work for establishing the geodesic metric on $T$ only supports using half-edge data structures; i.e., each edge $e$ in $T$ is split into two halves $(he_1,he_2)$ and each half-edge corresponds to one of two faces incident to $e$. In this paper, we prove that the exact-geodesic structures on two half-edges of $e$ can be merged into one structure associated with $e$. Four merits are achieved based on the properties which are studied in this paper: (1) Existing CAD systems that use edge-based data structures can directly add the geodesic distance function without changing the kernel to a half-edge data structure; (2) To find the geodesic path from inquiry points to the source, the MMP algorithm can be run in an on- the-fly fashion such that the inquiry points are covered by correct wedges; (3) The MMP algorithm is sped up by pruning unnecessary wedges during the wedge propagation process; (4) The storage of the MMP algorithm is reduced since fewer wedges need to be stored in an edge-based data structure. Experimental results show that when compared to the classic half-edge data structure, the edge-based implementation of the MMP algorithm reduces running time by 44% and storage by 29% on average.



[Download paper here](http://yongjinliu.github.io/files/2013-Exact-geodesic-metric-in-2-manifold-triangle-meshes-using-edge-based-data-structures.pdf)

[Download source code here](http://cg.cs.tsinghua.edu.cn/people/~Yongjin/Edge-based-ExactGeodesic_cmd.zip)

[More information](https://www.sciencedirect.com/science/article/pii/S0010448512002758?via%3Dihub)

Recommended citation: **Yong-Jin Liu** (2013) Exact geodesic metric in 2-manifold triangle meshes using edge-based data structures. Computer-Aided Design, Vol. 45, No. 3, pp. 695-704, 2013.





