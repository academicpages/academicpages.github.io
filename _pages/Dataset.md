---
permalink: /dataset/
title: "Dataset"
author_profile: true
---


<p float="middle">
    <video autoplay="autoplay" src="../images/DataVideo.mp4" controls="false" width="100%" />
</p>

Welcome! **CarlaSC** is a semantic scene completion dataset with the aim of increasing scene understanding in dynamic environments. Dynamic environments are challenging for scene understanding because dynamic objects leave behind traces and occlusions in completed scenes. As a result, quantifying performance and supervising training of algorithms from real world data is challenging. Therefore, we propose **CarlaSC**, a synthetic outdoor driving dataset generated from *randomly sampled multi-view geometry*.

## Overview

Our dataset consists of 24 sequences, generated from eight maps with a light traffic, medium traffic, and heavy traffic sequence for each. We obtain data from the [CARLA](https://carla.org/) simulator for its realism, autonomous traffic, and synchronized ground truth. Each sequence consists of three minutes of driving sampled at 10 Hz, for a total of 1800 frames. Each frame contains ground truth data including:

* Observed **point clouds** with **semantic labels** and ego-motion compensated **scene flow** for each point.
* **Pose** and **time** of each observation.
* **Complete semantic scene** represented in Cartesian and Cylindrical coordinates. The scene is obtained from twenty randomly placed LiDAR sensors, placed in new locations for every sequence.
* **Bird's Eye View** image for verification.

Our multi-view scenes include free space labels and minimal occlusions. An example image from our dataset compared to a similar frame in the well-known [Semantic KITTI](http://www.semantic-kitti.org/) dataset is shown below. 

<p float="middle">
  <img src="../images/CarlaKITTI.png" width="100%" />
</p>

## Classes

There are 23 semantic [classes](https://carla.readthedocs.io/en/latest/ref_sensors/#semantic-segmentation-camera) in the CARLA simulator. We remove all unlabeled points, and use class 0 to instead represent free space. We also remove any observations of the ego-vehicle, resulting in a clean dataset. A histogram of the frequency of all classes is shown below. 

![All](../images/HistogramAll.png) 

As can be seen, the distribution of classes is very uneven. Some classes are nearly identical to others, and some classes such as sky do not show up at all. Therefore, we also propose a remapping of the classes to aid with training supervised learning algorithms.

<p align="center">
  <img src="../images/ClassRemapping.png" width="65%" />
</p>
<p float="middle">
  <img src="../images/HistogramRemapped.png" width="100%" /> 
</p>
  


## Format

<p align="center">
  <img src="../images/BEV.png" width="30%" />
</p>
<p align="center">
  <img src="../images/Cartesian.png" width="45%" /> 
  <img src="../images/Cylindrical.png" width="45%" /> 
</p>
