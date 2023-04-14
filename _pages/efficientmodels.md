---
layout: archive
title: "Efficient Models"
permalink: /efficientmodels/
author_profile: true
---

Efficient Representation for Voxel Images
======
Although with recent progress, neural networks have on par ability compared to human in natural image. Currently, medical expert are more efficient at abstracting things (or say better representation ability), especially for voxel images. We have done several things to improve that:

1. We believe voxel image should be represent in a continuous form instead of a discrete one (see NeRF). This idea is verified in a super-resolution setting. Submitted to MedIA.
![](/images/2022-SAINR.png)
*Spatial Attention-based Implicit Neural Representation for Arbitrary Reduction of MRI Slice Spacing* 
X Wang\*, **S Wang\***, H Xiong, K Xuan, Z Zhuang, M Liu, Z Shen, X
Zhao, L Zhang, Q Wang

2. We recontruct vessel with its centerline, representing vessel with graph. Accepted by TMI, 2023 
![](/images/2023-TaG-Net.png)
*TaG-Net: Topology-aware Graph Network for Centerline-based Vessel Labeling*
L Yao, F Shi, **S Wang**, X Zhang, Z Xue, X Cao, Y Zhan, L Chen, Y Chen, B Song, Q Wang, D Shen


3. We recontruct knee with its surface, representing the joint structure with graph. Accepted by TMI 2022 and MICCAI 2022.
![](/images/2022-LGF.png)
*Local Graph Fusion of Multi-view MR Images for Knee Osteoarthritis Diagnosis* (MICCAI 2022)
Z Zhuang, **S Wang**, L Si, K Xuan, Z Xue, D Shen, L Zhang, W Yao, Q Wang
*Knee cartilage defect assessment by graph representation and surface convolution* (TMI 2022)
Z Zhuang, L Si, **S Wang**, K Xuan, X Ouyang, Y Zhan, Z Xue, L Zhang, D Shen, W Yao, Q Wang