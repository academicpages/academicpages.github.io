---
title: "Towards Better Generalization: Joint Depth-Pose Learning without PoseNet"
collection: publications
permalink: /publication/2020-Towards-Better-Generalization-Joint-Depth-Pose-Learning-without-PoseNet
excerpt: ''
date: 2020-06-10
venue: 'CVPR'
tags:
  - Conference Publications
citation: 'Wang Zhao, Shaohui Liu, Yezhi Shu, Yong-Jin Liu. Towards Better Generalization: Joint Depth-Pose Learning without PoseNet. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR 20), pages 9151-9161, 2020.'
---

Abstract: In this work, we tackle the essential problem of scale inconsistency for self supervised joint depth-pose learning. Most existing methods assume that a consistent scale of depth and pose can be learned across all input samples, which makes the learning problem harder, resulting in degraded performance and limited generalization in indoor environments and long-sequence visual odometry application. To address this issue, we propose a novel system that explicitly disentangles scale from the network estimation. Instead of relying on PoseNet architecture, our method recovers relative pose by directly solving fundamental matrix from dense optical flow correspondence and makes use of a two-view triangulation module to recover an up-to-scale 3D structure. Then, we align the scale of the depth prediction with the triangulated point cloud and use the transformed depth map for depth error computation and dense reprojection check. Our whole system can be jointly trained end-to-end. Extensive experiments show that our system not only reaches state-of-the-art performance on KITTI depth and flow estimation, but also significantly improves the generalization ability of existing self-supervised depth-pose learning methods under a variety of challenging scenarios, and achieves state-of-the-art results among self-supervised learning-based methods on KITTI Odometry and NYUv2 dataset. Furthermore, we present some interesting findings on the limitation of PoseNet-based relative pose estimation methods in terms of generalization ability.



[Download paper here](http://yongjinliu.github.io/files/2020-Towards-Better-Generalization-Joint-Depth-Pose-Learning-without-PoseNet.pdf)

[Download source code here](https://github.com/B1ueber2y/TrianFlow)

[More information](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhao_Towards_Better_Generalization_Joint_Depth-Pose_Learning_Without_PoseNet_CVPR_2020_paper.html)

Recommended citation: Wang Zhao, Shaohui Liu, Yezhi Shu, **Yong-Jin Liu**. Towards Better Generalization: Joint Depth-Pose Learning without PoseNet. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR 20), pages 9151-9161, 2020.

