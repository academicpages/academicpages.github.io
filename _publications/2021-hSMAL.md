---
title: "hSMAL: Detailed Horse Shape and Pose Reconstruction for Motion Pattern Recognition"
authors: 'Ci Li, Nima Ghorbani, Sofia Broomé, Maheen Rashid, Michael J. Black, Elin Hernlund, Hedvig Kjellström, Silvia Zuffi'
venue: 'CV4Animals Workshop, Proceedings IEEE Conference on Computer Vision and Pattern Recognition (CVPR)'
date: 2021-06-19
category: 'accepted'
pdf: 'https://arxiv.org/abs/2106.10102'
teaser: '2021-hSMAL.png'
bibtex: '2021-hSMAL.bib'
permalink: /publication/2021-hSMAL
collection: publications
projectpage: 'https://www.cv4animals.com/'
youtube: 'https://youtu.be/lQa4WB8ZOTA?t=1864'
---

Abstract
-------
In this paper we present our preliminary work on model-based behavioral analysis of horse motion. Our approach is
based on the SMAL model [21], a 3D articulated statistical model of animal shape. We define a novel SMAL model for
horses based on a new template, skeleton and shape space learned from 37 horse toys. 
We test the accuracy of our hSMAL model in reconstructing a horse from 3D mocap data
and images. We apply the hSMAL model to the problem of lameness detection from video, where we fit the model to images 
to recover 3D pose and train an ST-GCN network [17]
on pose data. A comparison with the same network trained on mocap points illustrates the benefit of our approach.
