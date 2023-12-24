---
title: "Vote from the Center: 6 DoF Pose Estimation in
RGB-D Images by Radial Keypoint Voting"
collection: publications
permalink: /publication/rcvpose
excerpt: 'We propose a novel keypoint voting scheme based on intersecting spheres, that is more accurate than existing schemes and allows for fewer, more disperse keypoints. The scheme is based upon the distance between points, which as a 1D quantity can be regressed more accurately than the 2D and 3D vector and offset quantities regressed in previous work, yielding more accurate keypoint localization. The scheme forms the basis of the proposed RCVPose method for 6 DoF pose estimation of 3D objects in RGB-D data, which is particularly effective at handling occlusions. A CNN is trained to estimate the distance between the 3D point corresponding to the depth mode of each RGB pixel, and a set of 3 disperse keypoints defined in the object frame. At inference, a sphere centered at each 3D point is generated, of radius equal to this estimated distance. The surfaces of these spheres vote to increment a 3D accumulator space, the peaks of which indicate keypoint locations. The proposed radial voting scheme is more accurate than previous vector or offset schemes, and is robust to disperse keypoints. Experiments demonstrate RCVPose to be highly accurate and competitive, achieving state-of-the-art results on the LINEMOD 99.7% and YCB-Video 97.2% datasets, notably scoring +4.9% higher 71.1% than previous methods on the challenging Occlusion LINEMOD dataset, and on average outperforming all other published results from the BOP benchmark for these 3 datasets. Our code is available at [github.com/aaronwool/rcvpose](https://github.com/aaronWool/rcvpose)'
date: 2022-10-23
venue: 'ECCV Oral'
paperurl: 'https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/6108_ECCV_2022_paper.php'
citation: 'Yangzheng Wu, Mohsen Zand, Ali Etemad, and Michael Greenspan.
Vote from the center: 6 dof pose estimation in rgb-d images by radial
keypoint voting, ECCV 2022.'
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/x5I1qUWVwi0?si=MWw3NinUxhCJCWFP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

[paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/6108_ECCV_2022_paper.php) [code](https://github.com/aaronWool/rcvpose) [video](https://youtu.be/x5I1qUWVwi0)
