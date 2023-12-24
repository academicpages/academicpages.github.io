---
title: "Learning Better Keypoints for Multi-Object 6DoF Pose Estimation"
collection: publications
permalink: /publication/keygnet
excerpt: 'We address the problem of keypoint selection, and find that the performance of 6DoF pose estimation methods can be improved when pre-defined keypoint locations are learned, rather than being heuristically selected as has been the standard approach. We found that accuracy and efficiency can be improved by training a graph network to select a set of disperse keypoints with similarly distributed votes. These votes, learned by a regression network to accumulate evidence for the keypoint locations, can be regressed more accurately compared to previous heuristic keypoint algorithms. The proposed KeyGNet, supervised by a combined loss measuring both Wasserstein distance and dispersion, learns the color and geometry features of the target objects to estimate optimal keypoint locations. Experiments demonstrate the keypoints selected by KeyGNet improved the accuracy for all evaluation metrics of all seven datasets tested, for three keypoint voting methods. The challenging Occlusion LINEMOD dataset notably improved ADD(S) by +16.4% on PVN3D, and all core BOP datasets showed an AR improvement for all objects, of between +1% and +21.5%. There was also a notable increase in performance when transitioning from single object to multiple object training using KeyGNet keypoints, essentially eliminating the SISO-MIMO gap for Occlusion LINEMOD.'
date: 2023-11-07
venue: 'WACV'
paperurl: 'https://arxiv.org/pdf/2308.07827.pdf'
citation: 'Yangzheng Wu and Michael Greenspan.
Learning Better Keypoints for Multi-Object 6DoF Pose Estimation, WACV 2024.'
---
<iframe width="560" height="315" src="https://www.youtube.com/embed/05FPOrqu_94?si=SUFPDHdrDjkVNZss" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

[paper](https://arxiv.org/pdf/2308.07827.pdf) [code](https://github.com/aaronWool/keygnet) [video](https://youtu.be/05FPOrqu_94?si=SUFPDHdrDjkVNZss)