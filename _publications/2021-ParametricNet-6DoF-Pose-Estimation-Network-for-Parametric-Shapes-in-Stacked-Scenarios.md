---
title: "ParametricNet: 6DoF Pose Estimation Network for Parametric Shapes in Stacked Scenarios"
collection: publications
permalink: /publication/2021-ParametricNet-6DoF-Pose-Estimation-Network-for-Parametric-Shapes-in-Stacked-Scenarios
excerpt: ''
date: 2021-05-30
venue: 'ICRA'
tags:
  - Conference Publications
citation: 'Long Zeng, Weijie Lv, Xinyu Zhang, Yong-Jin Liu*. ParametricNet: 6DoF Pose Estimation Network for Parametric Shapes in Stacked Scenarios. IEEE International Conference on Robotics and Automation (ICRA), 2021.'
---

Abstract: Most industrial parts are parametric and their special properties are not fully explored yet. This paper proposes a new 6DoF pose estimation network for parametric shapes in stacked scenarios (ParametricNet). It treats a parametric shape, instead of a part object, as a category. The keypoints of individual instances are learned with point- wise regression and Hough voting scheme, from which specific parameter values are calculated. Then, the template keypoints are obtained based on the computed parameter values and the parametric shape templates. Finally, the 6DoF pose is estimated by least-square fitting between the individual instance’s and the template’s keypoints & centroid. On the public Siléane dataset, the average of APs of ParametricNet is 96%, compared with 82% for the state-of-the-art method. In addition, a new parametric dataset with four shape templates is constructed, in which the evaluated learning and generalization abilities of ParametricNet outperform the state-of-the-art methods. In particular, for the less symmetric shape, the mAP is improved by over 20%, which is an obvious improvement. Real-world experiments show that our method can grasp parametric shapes with unknown parameter values in stacked scenarios.



[Download paper here](http://yongjinliu.github.io/files/2021-ParametricNet-6DoF-Pose-Estimation-Network-for-Parametric-Shapes-in-Stacked-Scenarios.pdf)

[More information](https://ieeexplore.ieee.org/document/9561181)

Recommended citation: Long Zeng, Weijie Lv, Xinyu Zhang, **Yong-Jin Liu\***. ParametricNet: 6DoF Pose Estimation Network for Parametric Shapes in Stacked Scenario. IEEE International Conference on Robotics and Automation (ICRA), 2021.

