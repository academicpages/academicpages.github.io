---
title: "Solving the initial value problem of discrete geodesics"
collection: publications
permalink: /publication/2016-Solving-the-initial-value-problem-of-discrete-geodesics
excerpt: ''
date: 2016-01-01
venue: 'Computer-Aided Design'
tags:
  - Journal Publications
citation: 'Peng Cheng, Chunyan Miao, Yong-Jin Liu, Changhe Tu, Ying He (2016) Solving the initial value problem of discrete geodesics. Computer-Aided Design (Special issue of SPM 2015), vol. 70, pp. 144-152, 2016.'
---

Abstract: Computing geodesic paths and distances is a common operation in computer graphics and computer- aided geometric design. The existing discrete geodesic algorithms are mainly designed to solve the boundary value problem, i.e., to find the shortest path between two given points. In this paper, we focus on the initial value problem, i.e., finding a uniquely determined geodesic path from a given point in any direction. Since the shortest paths do not provide the unique solution on triangle meshes, we solve the initial value problem in an indirect manner: given a fixed point and an initial tangent direction on a triangle mesh M, we first compute a geodesic curve $\hat{\gamma}$ on a piecewise smooth surface $\hat{M}$, which well approximates the input mesh $M$ and can be constructed at little cost. Then, we solve a first-order ODE of the tangent vector using the fourth-order Runge–Kutta method, and parallel transport it along $\hat{\gamma}$ . When the geodesic curve reaches the boundary of the current patch, its tangent can be directly transported to the neighboring patch, thanks to the $G^{-1}$-continuity along the common boundary of two adjacent patches. Finally, once the geodesic curve $\hat{\gamma}$ is available, we project it onto the underlying mesh $M$, producing the discrete geodesic path $\gamma$, which is guaranteed to be unique on $M$. It is worth noting that our method is different from the conventional methods of directly solving the geodesic equation (i.e., a second- order ODE of the position) on piecewise smooth surfaces, which are difficult to implement due to the complicated representation of the geodesic equation involving Christoffel symbols. The proposed method, based on the first-order ODE of the tangent vector, is intuitive and easy for implementation. Our method is particularly useful for computing geodesic paths on low-resolution meshes which may have large and/or skinny triangles, since the conventional straightest geodesic paths are usually far from the ground truth.



[Download paper here](http://yongjinliu.github.io/files/2016-Solving-the-initial-value-problem-of-discrete-geodesics.pdf)

[More information](https://www.sciencedirect.com/science/article/pii/S0010448515001128)

Recommended citation: Peng Cheng, Chunyan Miao, **Yong-Jin Liu**, Changhe Tu, Ying He (2016) Solving the initial value problem of discrete geodesics. Computer-Aided Design (Special issue of SPM 2015), vol. 70, pp. 144-152, 2016.





