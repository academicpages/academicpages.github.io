---
title: "PC-NBV: A Point Cloud Based Deep Network for Efficient Next Best View Planning"
collection: publications
permalink: /publication/2020-PC-NBV-A-Point-Cloud-Based-Deep-Network-for-Efficient-Next-Best-View-Planning
excerpt: ''
date: 2020-10-24
venue: 'IROS'
tags:
  - Conference Publications
citation: 'Rui Zeng, Wang Zhao, Yong-Jin Liu*. PC-NBV: A Point Cloud Based Deep Network for Efficient Next Best View Planning. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 20), pages 7050-7057, 2020.'
---

Abstract: The Next Best View (NBV) problem is important in the active robotic reconstruction. It enables the robot system to perform scanning actions in a reasonable view sequence, and fulfil the reconstruction task in an effective way. Previous works mainly follow the volumetric methods, which convert the point cloud information collected by sensors into a voxel representation space and evaluate candidate views through ray casting simulations to pick the NBV. However, the process of volumetric data transformation and ray casting is often time-consuming. To address this issue, in this paper, we propose a point cloud based deep neural network called PC-NBV to achieve efficient view planning without these computationally expensive operations. The PC-NBV network takes the raw point cloud data and current view selection states as input, and then directly predicts the information gain of all candidate views. By avoiding costly data transformation and ray casting, and utilizing powerful neural network to learn structure priors from point cloud, our method can achieve efficient and effective NBV planning. Experiments on multiple datasets show the proposed method outperforms state-of-the-art NBV methods, giving better views for robot system with much less inference time. Furthermore, we demonstrate the robustness of our method against noise and the ability to extend to multi-view system, making it more applicable for various scenarios.



[Download paper here](http://yongjinliu.github.io/files/2020-PC-NBV-A-Point-Cloud-Based-Deep-Network-for-Efficient-Next-Best-View-Planning.pdf)

[Download source code here](https://github.com/Smile2020/PC-NBV)

[More information](https://ieeexplore.ieee.org/document/9340916)

Recommended citation: Rui Zeng, Wang Zhao, **Yong-Jin Liu***. PC-NBV: A Point Cloud Based Deep Network for Efficient Next Best View Planning. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 20), pages 7050-7057, 2020.

