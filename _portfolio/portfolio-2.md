---
title: "MatchSDF: Learning Generalizable 3D Reconstruction Using Correspondence Matching"
excerpt: "3D Surface Reconstruction from 2D Images using Correspondence Matching."
collection: portfolio
---

Recent advancements, particularly in novel view synthesis, catalyzed the pursuit of 3D reconstruction using neural implicit representations. However, per-scene optimized models do not emerge as feasible options in many real-life applications and suggest the development of generalizable 3D reconstruction models. In this paper, we present MatchSDF, a novel 3D reconstruction model that uses pairwise cosine similarity for views provided and additional geometry encoding features such as groupwise variance to improve geometric cues. In addition, MatchSDF benefits from cross-point correlation by incorporating Ray Transformer into generic SDF networks. MatchSDF is capable of performing novel view synthesis by using the recent idea of color blending to improve the appearance of views. On the DTU benchmark, MatchSDF achieves comparable and slightly better results against SparseNeuS while being reference-view agnostic and not limited by volumetric features.

For further information, please refer to the [report](/files/matchsdf/Course-Project-MatchSDF.pdf) we have prepared for the course project.

The details of the implementation can be accessed in [Github](https://github.com/EliasSalameh/SparseNeuS--MatchSDF).

<img src='/files/matchsdf/matchsdf.png' alt='MatchSDF - 3D Surface Reconstruction from 2D Images using Correspondence Matching' width='600' height='700'>

