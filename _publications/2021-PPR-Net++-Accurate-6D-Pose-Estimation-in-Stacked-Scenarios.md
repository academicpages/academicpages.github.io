---
title: "PPR-Net++: Accurate 6D Pose Estimation in Stacked Scenarios"
collection: publications
permalink: /publication/2021-PPR-Net++-Accurate-6D-Pose-Estimation-in-Stacked-Scenarios
excerpt: ''
date: 2021-09-14
venue: 'IEEE Transactions on Automation Science and Engineering'
tags:
  - Journal Publications
citation: 'Long Zeng, Wei Jie Lv, Zhi Kai Dong, Yong-Jin Liu*. PPR-Net++: Accurate 6D Pose Estimation in Stacked Scenarios. IEEE Transactions on Automation Science and Engineering, Vol. 19, No. 4, pp. 3139-3151, 2021.'
---

Abstract: Most supervised learning-based pose estimation methods for stacked scenes are trained on massive synthetic datasets. In most cases, the challenge is that the learned network on the training dataset is no longer optimal on the testing dataset. To address this problem, we propose a pose regression network PPR-Net++. It transforms each scene point into a point in the centroid space, followed by a clustering process and a voting process. In the training phase, a mapping function between the network's critical parameter (i.e., the bandwidth of the clustering algorithm) and the compactness of the centroid distributions is obtained. This function is used to adapt the bandwidth between centroid distributions of two different domains. In addition, to further improve the pose estimation accuracy, the network also predicts the confidence of each point, based on its visibility and pose error. Only the points with high confidence have the right to vote for the final object pose. In experiments, our method is trained on the IPA synthetic dataset and compared with the state-of-the-art algorithm. When tested with the public synthetic Siléane dataset, our method is better in all eight objects, where five of them are improved by more than 5% in average precision (AP). On IPA real dataset, our method outperforms a large margin by 20%. This lays a solid foundation for robot grasping in industrial scenarios.



[Download paper here](http://yongjinliu.github.io/files/2021-PPR-Net++-Accurate-6D-Pose-Estimation-in-Stacked-Scenarios.pdf)

[Download source code here](https://github.com/lvwj19/PPR-Net-plus)

[More information](https://ieeexplore.ieee.org/document/9537584)

Recommended citation: Long Zeng, Wei Jie Lv, Zhi Kai Dong, **Yong-Jin Liu\***. PPR-Net++: Accurate 6D Pose Estimation in Stacked Scenarios. IEEE Transactions on Automation Science and Engineering, Vol. 19, No. 4, pp. 3139-3151, 2021.



