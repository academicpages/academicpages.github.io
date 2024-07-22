---
title: "Pseudo-keypoint RKHS Learning for Self-supervised 6DoF Pose Estimation"
collection: publications
permalink: /publication/rcvpose
excerpt: 'We address the simulation-to-real domain gap in six degree-of-freedom pose estimation (6DoF PE), and propose a novel self-supervised keypoint voting-based 6DoF PE framework, effectively narrowing this gap using a learnable kernel in RKHS. We formulate this domain gap as a distance in high-dimensional feature space, distinct from previous iterative matching methods. We propose an adapter network, which is pre-trained on purely synthetic data with synthetic ground truth poses, and which evolves the network parameters from this source synthetic domain to the target real domain. Importantly, the real data training only uses pseudo-poses estimated by pseudo-keypoints, and thereby requires no real ground truth data annotations. Our proposed method is called RKHSPose, and achieves state-of-the-art performance among self-supervised methods on three commonly used 6DoF PE datasets including LINEMOD (+4.2%), Occlusion LINEMOD (+2%), and YCB-Video (+3%). It also compares favorably to fully supervised methods on all six applicable BOP core datasets, achieving within -11.3% to +0.2% of the top fully supervised results.'
date: 2024-09-28
venue: 'ECCV'
paperurl: 'https://arxiv.org/abs/2311.09500'
citation: 'Yangzheng Wu and Michael Greenspan.
Pseudo-keypoint RKHS Learning for Self-supervised 6DoF Pose Estimation, ECCV 2024.'
---

[paper](https://arxiv.org/abs/2311.09500) [code](https://arxiv.org/abs/2311.09500) [video](https://arxiv.org/abs/2311.09500)
