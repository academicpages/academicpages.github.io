---
title: "A Confidence-based Iterative Solver of Depths and Surface Normals for Deep Multi-view Stereo"
collection: publications
permalink: /publication/2021-A-Confidence-based-Iterative-Solver-of-Depths-and-Surface-Normals-for-Deep-Multi-view-Stereo
excerpt: 'In this paper, we introduce a deep multi-view stereo (MVS) system that jointly predicts depths, surface normals and per-view confidence maps. The key to our approach is a novel solver that iteratively solves for per-view depth map and normal map by optimizing an energy potential based upon the local planar assumption. Specifically, the algorithm updates depth map by propagating from neighboring pixels with slanted planes, and updates normal map with local probabilistic plane fitting. Both two steps are monitored by a customized confidence map. This confidence-based solver is not only effective as a post-processing tool for plane based depth refinement and completion, but also differentiable such that it can be efficiently integrated into deep learning pipelines. Our multi-view stereo system employs multiple optimization steps of the solver over the initial prediction of depths and surface normals. The whole system can be trained end-to-end, decoupling the challenging problem of matching pixels within poorly textured regions from the cost volume based neural network. Experimental results on ScanNet and RGB-D Scenes V2 demonstrate state-of-the-art performance of the proposed deep MVS system on multi-view depth estimation, with our proposed solver consistently improving the depth quality over both conventional and deep learning based MVS pipelines.'
date: 2021-03-10
venue: 'ICCV'
tags:
  - Conference Publications
---

[Download paper here](http://yongjinliu.github.io/files/2021-A-Confidence-based-Iterative-Solver-of-Depths-and-Surface-Normals-for-Deep-Multi-view-Stereo.pdf)

[Download source code here](https://github.com/thuzhaowang/idn-solver)

Abstract: In this paper, we introduce a deep multi-view stereo (MVS) system that jointly predicts depths, surface normals and per-view confidence maps. The key to our approach is a novel solver that iteratively solves for per-view depth map and normal map by optimizing an energy potential based upon the local planar assumption. Specifically, the algorithm updates depth map by propagating from neighboring pixels with slanted planes, and updates normal map with local probabilistic plane fitting. Both two steps are monitored by a customized confidence map. This confidence-based solver is not only effective as a post-processing tool for plane based depth refinement and completion, but also differentiable such that it can be efficiently integrated into deep learning pipelines. Our multi-view stereo system employs multiple optimization steps of the solver over the initial prediction of depths and surface normals. The whole system can be trained end-to-end, decoupling the challenging problem of matching pixels within poorly textured regions from the cost volume based neural network. Experimental results on ScanNet and RGB-D Scenes V2 demonstrate state-of-the-art performance of the proposed deep MVS system on multi-view depth estimation, with our proposed solver consistently improving the depth quality over both conventional and deep learning based MVS pipelines.



Recommended citation: Wang Zhao, Shaohui Liu, Yi Wei, Hengkai Guo, **Yong-Jin Liu***. A Confidence-based Iterative Solver of Depths and Surface Normals for Deep Multi-view Stereo. IEEE International Conference on Computer Vision (ICCV 21), pages 6168-6177, 2021.

